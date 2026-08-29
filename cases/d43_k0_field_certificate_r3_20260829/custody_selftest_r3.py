#!/usr/bin/env python3
"""Executable custody-boundary controls for the D43 `K0` field certificate, R3.

Every control here runs the **real** functions of ``aws_supervisor_r3.py``
against a **real** filesystem tree: real ``lstat`` results, real uid and gid
values, real POSIX permission bits, real ``O_EXCL`` semantics.  Nothing about
ownership or permission is simulated by patching ``os.stat``.

Two modes:

``run_controls(sup)`` (the default, used by ``preflight_r3.py`` P11)
    builds fixture trees under a temporary directory and drives them with a
    :class:`CustodyPolicy` whose custodian uid is the *running* uid.  That is
    the one thing an unprivileged producer host cannot reproduce: it cannot
    create a root-owned object.  Everything else -- the mode laws, the
    exclusive-create law, the "a 0444 file cannot be rewritten by its owner"
    law, the "an unprivileged process cannot chown to root" law, the ordering
    law that says a failed precondition never burns the authorization -- is
    executed exactly as it will execute on the host.  The two facts the fixture
    policy replaces are pinned separately by
    :func:`production_policy_controls`, which asserts that production builds
    its policy with the literal custodian uid 0 and refuses to run as root.

``--on-host-dry-run`` (run by ops on the deployed host, as the service user)
    calls ``aws_supervisor_r3.verify_custody_preconditions`` with the
    **production** policy against the real root-owned tree and prints its JSON
    record.  It creates, writes and deletes nothing, and it stops before the
    lease, so it cannot consume the authorization.  This is how the root-owned
    half of the boundary is verified where root-owned objects actually exist.

The module refuses to run its fixtures as root: as root every permission
denial the controls depend on would silently succeed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

SCHEMA = "d43-k0-field-certificate-custody-selftest-r3"
FIXTURE_AUTH_SHA = "0" * 63 + "1"
OTHER_AUTH_SHA = "f" * 63 + "e"


# --------------------------------------------------------------------------
# fixture construction
# --------------------------------------------------------------------------


def fixture_policy(sup, service_uid=None, service_gid=None, custodian_uid=None):
    """A policy a non-root user can satisfy, built from the *running* ids."""
    return sup.CustodyPolicy(
        custodian_uid=os.geteuid() if custodian_uid is None else custodian_uid,
        service_user="fixture-service-user",
        service_uid=os.geteuid() if service_uid is None else service_uid,
        service_gid=os.getegid() if service_gid is None else service_gid,
        run_dir_mode=sup.RUN_DIR_MODE,
        claim_mode=sup.CLAIM_TOKEN_MODE)


def build_tree(sup, root, policy, auth_sha=FIXTURE_AUTH_SHA, parent_mode=0o755,
               run_mode=0o700, claim_mode=0o444, with_claim=True,
               claim_overrides=None, run_name="run-20260829T010727Z"):
    """A sealed parent, a service-owned run directory and a claim token.

    The token is written and then chmod-ed exactly as ``mint_claim_r3.sh``
    writes it, with the same JSON keys, so the fixture exercises the real
    binding comparison and not a paraphrase of it.
    """
    parent = Path(root) / "sealed"
    parent.mkdir(mode=parent_mode)
    os.chmod(str(parent), parent_mode)
    run_dir = parent / run_name
    run_dir.mkdir(mode=run_mode)
    os.chmod(str(run_dir), run_mode)
    token = None
    if with_claim:
        claim = {"authorization_sha256": auth_sha,
                 "minted_utc": "2026-08-29T00:00:00Z",
                 "route": sup.ROUTE,
                 "run_path": str(run_dir),
                 "schema": sup.CLAIM_SCHEMA,
                 "service_user": policy.service_user}
        claim.update(claim_overrides or {})
        token = run_dir / sup.claim_token_name(auth_sha)
        token.write_text(json.dumps(claim, sort_keys=True) + "\n")
        os.chmod(str(token), claim_mode)
    return {"parent": parent, "run_dir": run_dir, "token": token,
            "record": {"run_path": str(run_dir)}}


def _leases_anywhere(root, sup):
    """Every authorization lease in the whole fixture tree, by name."""
    out = []
    for base, _dirs, files in os.walk(str(root)):
        for name in files:
            if name.startswith(sup.AUTHORIZATION_LEASE_PREFIX):
                out.append(str(Path(base) / name))
    return sorted(out)


def _expect_fault(sup, fn, code, exc_type=None):
    """Run ``fn``; require exactly ``code``, from the packet's own fault type.

    A raw exception is a failure of the control, not of the fixture: the R2
    defect this file exists to close was an uncaught ``PermissionError``.
    ``code=None`` means "any fault of the right type, but nothing else".
    """
    exc_type = exc_type or sup.CustodyFault
    try:
        fn()
    except exc_type as exc:
        return {"raised": exc_type.__name__, "code": exc.code,
                "detail": str(exc)[:200],
                "ok": code is None or exc.code == code}
    except Exception as exc:                                  # noqa: BLE001
        return {"raised": type(exc).__name__, "code": None,
                "detail": repr(exc)[:200], "ok": False}
    return {"raised": None, "code": None, "detail": "no fault raised",
            "ok": False}


# --------------------------------------------------------------------------
# the controls
# --------------------------------------------------------------------------


def production_policy_controls(sup, packet_dir):
    """What the fixture policy replaces, pinned by static source census.

    ``production_policy`` must build the one production policy with the
    literal custodian uid 0, and it must be the only ``CustodyPolicy(``
    construction in the supervisor.  Everything else in this file runs under a
    fixture policy, so these two facts carry the whole weight of "the deployed
    custodian is root".
    """
    text = (Path(packet_dir) / "aws_supervisor_r3.py").read_text()
    constructions = text.count("CustodyPolicy(")
    body = text.split("def production_policy(")[1].split("\ndef ")[0]
    out = {
        "custody_policy_constructions_in_supervisor": constructions,
        "production_policy_pins_uid_zero": "custodian_uid=0" in body,
        "production_policy_resolves_service_user_from_passwd":
            "pwd.getpwnam(DEDICATED_SERVICE_USER)" in body,
        "production_policy_resolves_service_group_from_group_db":
            "grp.getgrnam(DEDICATED_SERVICE_GROUP)" in body,
        "run_job_uses_production_policy":
            "policy = production_policy()" in text,
        "run_job_calls_establish_custody":
            "establish_custody(policy, authorization, auth_sha)" in text,
        "supervisor_refuses_root": "the supervisor must never run as root" in text,
        "no_environment_override":
            "environ" not in body and "argv" not in body,
    }
    # exactly two: the class definition line is "class CustodyPolicy", the two
    # hits are production_policy's construction and the docstring reference
    out["ok"] = (out["custody_policy_constructions_in_supervisor"] == 1
                 and all(v for k, v in out.items()
                         if isinstance(v, bool)))
    return out


def posix_semantics_controls(root):
    """The three POSIX facts the whole boundary rests on, executed for real.

    None of these touches the packet: they are statements about the kernel this
    process is running on, and they are what makes the root-owned claim token
    unforgeable and the sealed parent unwritable on the deployed host.
    """
    out = {"euid": os.geteuid(), "running_as_root": os.geteuid() == 0}

    # 1. a directory without a write bit refuses creation, even to its owner
    nodir = Path(root) / "no-write-dir"
    nodir.mkdir(mode=0o555)
    os.chmod(str(nodir), 0o555)
    try:
        os.open(str(nodir / "x"), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o444)
        out["dir_without_write_bit_refuses_create"] = False
    except PermissionError:
        out["dir_without_write_bit_refuses_create"] = True
    os.chmod(str(nodir), 0o755)

    # 2. a 0444 file refuses a write, even to its owner
    ro = Path(root) / "read-only-file"
    ro.write_text("{}\n")
    os.chmod(str(ro), 0o444)
    try:
        with ro.open("w"):
            pass
        out["mode_0444_refuses_write_by_owner"] = False
    except PermissionError:
        out["mode_0444_refuses_write_by_owner"] = True

    # 3. an unprivileged process cannot give a file to root
    try:
        os.chown(str(ro), 0, 0)
        out["unprivileged_chown_to_root_refused"] = False
    except (PermissionError, OSError):
        out["unprivileged_chown_to_root_refused"] = True

    # 4. O_EXCL is exclusive
    once = Path(root) / "exclusive"
    os.close(os.open(str(once), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o444))
    try:
        os.open(str(once), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o444)
        out["o_excl_refuses_second_create"] = False
    except FileExistsError:
        out["o_excl_refuses_second_create"] = True

    out["ok"] = (not out["running_as_root"]) and all(
        v for k, v in out.items()
        if isinstance(v, bool) and k != "running_as_root")
    return out


def boundary_controls(sup, root):
    """The custody sequence, driven end to end against real directories."""
    controls = {}
    policy = fixture_policy(sup)

    # ---- 1. the happy path: verify, then burn, exactly once --------------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy)
        first = sup.establish_custody(policy, tree["record"], FIXTURE_AUTH_SHA)
        lease = Path(first["authorization_lease"])
        second = _expect_fault(
            sup, lambda: sup.establish_custody(policy, tree["record"],
                                               FIXTURE_AUTH_SHA),
            "AUTHORIZATION_REUSE")
        controls["one_time_claim"] = {
            "lease": lease.name,
            "lease_exists": lease.is_file(),
            "lease_mode": oct(stat.S_IMODE(lease.lstat().st_mode)),
            "lease_binds_authorization":
                json.loads(lease.read_text())["authorization_sha256"]
                == FIXTURE_AUTH_SHA,
            "lease_binds_run_path":
                json.loads(lease.read_text())["run_path"] == str(tree["run_dir"]),
            "second_claim": second,
            "leases_in_tree": len(_leases_anywhere(tmp, sup)),
            "ok": lease.is_file()
                  and stat.S_IMODE(lease.lstat().st_mode) == 0o444
                  and second["ok"]
                  and len(_leases_anywhere(tmp, sup)) == 1}

    # ---- 2. the sealed-parent gate, both branches ------------------------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy)
        prod_like = fixture_policy(sup, custodian_uid=os.geteuid() + 1)
        controls["parent_wrong_owner"] = _expect_fault(
            sup, lambda: sup.verify_custody_preconditions(
                prod_like, tree["record"], FIXTURE_AUTH_SHA), "PATH_OWNER")
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy, parent_mode=0o775)
        controls["parent_group_writable"] = _expect_fault(
            sup, lambda: sup.verify_custody_preconditions(
                policy, tree["record"], FIXTURE_AUTH_SHA), "PATH_MODE")

    # ---- 3. the run directory -------------------------------------------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy)
        shutil.rmtree(str(tree["run_dir"]))
        controls["run_dir_absent"] = _expect_fault(
            sup, lambda: sup.verify_custody_preconditions(
                policy, tree["record"], FIXTURE_AUTH_SHA), "RUN_DIR_ABSENT")
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy, run_mode=0o750)
        controls["run_dir_wrong_mode"] = _expect_fault(
            sup, lambda: sup.verify_custody_preconditions(
                policy, tree["record"], FIXTURE_AUTH_SHA), "RUN_DIR_MODE")
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy)
        other = fixture_policy(sup, service_uid=os.geteuid() + 1)
        controls["run_dir_wrong_owner"] = _expect_fault(
            sup, lambda: sup.verify_custody_preconditions(
                other, tree["record"], FIXTURE_AUTH_SHA), "RUN_DIR_OWNER")

    # ---- 4. the root-minted claim token ----------------------------------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy, with_claim=False)
        controls["claim_absent"] = _expect_fault(
            sup, lambda: sup.verify_custody_preconditions(
                policy, tree["record"], FIXTURE_AUTH_SHA), "CLAIM_ABSENT")
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy, claim_mode=0o644)
        controls["claim_wrong_mode"] = _expect_fault(
            sup, lambda: sup.verify_custody_preconditions(
                policy, tree["record"], FIXTURE_AUTH_SHA), "CLAIM_MODE")
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy)
        forger = sup.CustodyPolicy(
            custodian_uid=os.geteuid() + 1, service_user=policy.service_user,
            service_uid=os.geteuid(), service_gid=os.getegid(),
            run_dir_mode=sup.RUN_DIR_MODE, claim_mode=sup.CLAIM_TOKEN_MODE)
        # the parent is fixture-owned, so the parent gate would fire first;
        # call the token check directly to isolate the ownership branch
        controls["claim_service_written_refused"] = _expect_fault(
            sup, lambda: sup.verify_claim_token(
                forger, tree["run_dir"], FIXTURE_AUTH_SHA, tree["record"]),
            "CLAIM_OWNER")
    for key, override in (("claim_wrong_route", {"route": "D43-K0-FIELD-CERT-R2"}),
                          ("claim_wrong_digest",
                           {"authorization_sha256": OTHER_AUTH_SHA}),
                          ("claim_wrong_run_path", {"run_path": "/var/lib/elsewhere"}),
                          ("claim_wrong_schema", {"schema": "something-else"}),
                          ("claim_wrong_service_user", {"service_user": "root"})):
        with tempfile.TemporaryDirectory(dir=root) as tmp:
            tree = build_tree(sup, tmp, policy, claim_overrides=override)
            controls[key] = _expect_fault(
                sup, lambda t=tree: sup.verify_custody_preconditions(
                    policy, t["record"], FIXTURE_AUTH_SHA), "CLAIM_BINDING")

    # ---- 5. the token cannot be altered by the service user -------------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy)
        token = tree["token"]
        probe = {"write_refused": False, "chown_to_root_refused": False}
        try:
            with token.open("w"):
                pass
        except PermissionError:
            probe["write_refused"] = True
        try:
            os.chown(str(token), 0, 0)
        except (PermissionError, OSError):
            probe["chown_to_root_refused"] = True
        # deleting it is the one thing the service can do, and it only denies
        # itself: the launch then refuses CLAIM_ABSENT and burns nothing
        token.unlink()
        probe["after_delete"] = _expect_fault(
            sup, lambda: sup.establish_custody(policy, tree["record"],
                                               FIXTURE_AUTH_SHA),
            "CLAIM_ABSENT")
        probe["leases_in_tree"] = len(_leases_anywhere(tmp, sup))
        probe["ok"] = (probe["write_refused"] and probe["chown_to_root_refused"]
                       and probe["after_delete"]["ok"]
                       and probe["leases_in_tree"] == 0)
        controls["claim_token_immutable_to_service"] = probe

    # ---- 6. crash and restart -------------------------------------------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy)
        sup.establish_custody(policy, tree["record"], FIXTURE_AUTH_SHA)
        (tree["run_dir"] / "job_marker.json").write_text("{}")
        (tree["run_dir"] / "supervisor_terminal.json").write_text("{}")
        controls["crashed_run_refused"] = _expect_fault(
            sup, lambda: sup.establish_custody(policy, tree["record"],
                                               FIXTURE_AUTH_SHA),
            "RUN_DIR_DIRTY")
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy)
        sup.establish_custody(policy, tree["record"], FIXTURE_AUTH_SHA)
        controls["restart_after_clean_claim_refused"] = _expect_fault(
            sup, lambda: sup.establish_custody(policy, tree["record"],
                                               FIXTURE_AUTH_SHA),
            "AUTHORIZATION_REUSE")

    # ---- 7. an unwritable run directory is a fault, not a traceback ------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy)
        os.chmod(str(tree["run_dir"]), 0o500)
        controls["lease_unwritable"] = _expect_fault(
            sup, lambda: sup.claim_authorization_lease(tree["run_dir"],
                                                       FIXTURE_AUTH_SHA),
            "LEASE_UNWRITABLE")
        os.chmod(str(tree["run_dir"]), 0o700)

    # ---- 8. no pre-lease refusal ever burns the authorization ------------
    burn = {"cases": [], "ok": True}
    cases = (
        ("parent_group_writable", dict(parent_mode=0o775)),
        ("run_dir_wrong_mode", dict(run_mode=0o750)),
        ("claim_absent", dict(with_claim=False)),
        ("claim_wrong_mode", dict(claim_mode=0o644)),
        ("claim_wrong_digest",
         dict(claim_overrides={"authorization_sha256": OTHER_AUTH_SHA})),
        ("claim_wrong_run_path",
         dict(claim_overrides={"run_path": "/var/lib/elsewhere"})),
    )
    for name, kwargs in cases:
        with tempfile.TemporaryDirectory(dir=root) as tmp:
            tree = build_tree(sup, tmp, policy, **kwargs)
            faulted = _expect_fault(
                sup, lambda t=tree: sup.establish_custody(
                    policy, t["record"], FIXTURE_AUTH_SHA), None)
            leases = _leases_anywhere(tmp, sup)
            entry = {"case": name, "code": faulted["code"],
                     "raised": faulted["raised"], "leases_after": len(leases),
                     "ok": faulted["ok"] and not leases}
            burn["cases"].append(entry)
            burn["ok"] = burn["ok"] and entry["ok"]
    controls["no_burn_before_verification"] = burn

    # ---- 9. the runner's pre-run directory law, end to end ---------------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = build_tree(sup, tmp, policy)
        custody = sup.establish_custody(policy, tree["record"], FIXTURE_AUTH_SHA)
        controls["custody_then_runner_handshake"] = {
            "pre_launch_entries": custody["pre_launch_entries"],
            "run_dir": str(tree["run_dir"]),
            "ok": custody["pre_launch_entries"]
                  == sorted([sup.claim_token_name(FIXTURE_AUTH_SHA)])}

    for value in controls.values():
        if "ok" not in value:
            value["ok"] = bool(value.get("ok", True))
    controls["ok"] = all(v["ok"] for v in controls.values()
                         if isinstance(v, dict))
    return controls


def runner_pre_run_controls(sup, run, root):
    """The runner's pre-run directory law, against a real staged directory.

    This is the R3 producer-found repair (REPAIR-2): the R2 law admitted only
    ``job_marker.json`` and ``execution_pins_live.json``, while the supervisor
    always extracts the archive to ``<run dir>/source`` before spawning the
    runner, so every real launch would have died on ``RUN_DIR_REUSE`` one step
    after the boundary fault the R2 review found.  Nothing in R1 or R2 executed
    this path; it is executed here.
    """
    policy = fixture_policy(sup)
    fault_type = run.RunnerFault
    out = {}

    def staged(tmp, with_source=True, with_lease=True, extra=None,
               auth_sha=FIXTURE_AUTH_SHA):
        tree = build_tree(sup, tmp, policy, auth_sha=auth_sha)
        if with_lease:
            sup.claim_authorization_lease(tree["run_dir"], auth_sha)
        rd = tree["run_dir"]
        if with_source:
            (rd / "source").mkdir()
        (rd / "job_marker.json").write_text("{}")
        (rd / "execution_pins_live.json").write_text("{}")
        for name in (extra or ()):
            (rd / name).write_text("{}")
        return rd

    with tempfile.TemporaryDirectory(dir=root) as tmp:
        rd = staged(tmp)
        try:
            listing = run.check_run_dir_clean(rd, FIXTURE_AUTH_SHA)
            out["clean_launch_accepted"] = {
                "listing": listing, "entries": len(listing),
                "ok": len(listing) == 5 and "source" in listing}
        except Exception as exc:                              # noqa: BLE001
            # a refusal here is the R2 defect: a correctly staged launch that
            # the runner will not start
            out["clean_launch_accepted"] = {
                "listing": [], "entries": 0, "ok": False,
                "refused": "%s: %s" % (type(exc).__name__, str(exc)[:200])}
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        rd = staged(tmp, extra=("terminal.json",))
        out["stale_artifact_refused"] = _expect_fault(
            sup, lambda: run.check_run_dir_clean(rd, FIXTURE_AUTH_SHA),
            "RUN_DIR_REUSE", fault_type)
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        rd = staged(tmp, with_source=False)
        out["unstaged_source_refused"] = _expect_fault(
            sup, lambda: run.check_run_dir_clean(rd, FIXTURE_AUTH_SHA),
            "RUN_DIR_INCOMPLETE", fault_type)
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        rd = staged(tmp, with_lease=False)
        out["missing_lease_refused"] = _expect_fault(
            sup, lambda: run.check_run_dir_clean(rd, FIXTURE_AUTH_SHA),
            "RUN_DIR_INCOMPLETE", fault_type)
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        rd = staged(tmp)
        out["foreign_authorization_refused"] = _expect_fault(
            sup, lambda: run.check_run_dir_clean(rd, OTHER_AUTH_SHA),
            "RUN_DIR_REUSE", fault_type)
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        rd = staged(tmp)
        out["non_sha_marker_refused"] = _expect_fault(
            sup, lambda: run.check_run_dir_clean(rd, "not-a-digest"),
            "MARKER_AUTHORIZATION", fault_type)
    out["ok"] = all(v["ok"] for v in out.values() if isinstance(v, dict))
    return out


def mint_script_controls(packet_dir):
    """The root-side primitive: executed where it can be, read where it cannot.

    The refusal paths run for real (this process is not root, which is exactly
    the case the script must refuse).  The minting path cannot run off-host, so
    its one-shot ordering is asserted against the source text: the spent marker
    must be created with noclobber before the run directory exists.
    """
    mint = Path(packet_dir) / "mint_claim_r3.sh"
    retire = Path(packet_dir) / "retire_claim_r3.sh"
    text = mint.read_text()
    spent_at = text.index('> "$SPENT"')
    mkdir_at = text.index('mkdir -m 0700 "$RUN_DIR"')
    token_at = text.index('> "$TOKEN"')
    chown_at = text.index('chown "$SERVICE_USER:$SERVICE_USER" "$RUN_DIR"')

    def run(script, args):
        proc = subprocess.run(["/bin/bash", str(script)] + args,
                              capture_output=True, text=True, timeout=30)
        return {"rc": proc.returncode,
                "stderr": proc.stderr.strip()[:200]}

    no_args = run(mint, [])
    not_root = run(mint, ["/var/lib/jc2-k0", "run-20260829T010727Z",
                          "/etc/jc2-authorization.json", "jc2k0"])
    retire_not_root = run(retire, ["/var/lib/jc2-k0/run-20260829T010727Z"])
    syntax = subprocess.run(["/bin/bash", "-n", str(mint)],
                            capture_output=True, text=True).returncode
    syntax_retire = subprocess.run(["/bin/bash", "-n", str(retire)],
                                   capture_output=True, text=True).returncode
    out = {
        "mint_usage_rc": no_args["rc"],
        "mint_not_root_rc": not_root["rc"],
        "mint_not_root_stderr": not_root["stderr"],
        "retire_not_root_rc": retire_not_root["rc"],
        "mint_syntax_rc": syntax,
        "retire_syntax_rc": syntax_retire,
        "spent_marker_before_run_dir": spent_at < mkdir_at,
        "token_written_before_chown_to_service": token_at < chown_at,
        "noclobber_set_before_spent": text.index("set -C") < spent_at,
        "mint_requires_root": "MINT_NOT_ROOT" in not_root["stderr"],
        "mint_checks_parent_owner": "MINT_PARENT_OWNER" in text,
        "mint_checks_parent_realpath": "MINT_PARENT_SYMLINK" in text,
        "mint_uses_no_json_parser":
            not any(tool in text.split("set -euo")[1]
                    for tool in ("python", "jq ", "perl", "awk")),
    }
    out["ok"] = (out["mint_usage_rc"] == 64 and out["mint_not_root_rc"] == 77
                 and out["retire_not_root_rc"] == 77
                 and out["mint_syntax_rc"] == 0 and out["retire_syntax_rc"] == 0
                 and out["spent_marker_before_run_dir"]
                 and out["token_written_before_chown_to_service"]
                 and out["noclobber_set_before_spent"]
                 and out["mint_requires_root"]
                 and out["mint_checks_parent_owner"]
                 and out["mint_checks_parent_realpath"])
    return out


def unit_contract_controls(sup, packet_dir):
    """The unit template and the supervisor must agree on one identity.

    A mismatch between ``User=``/``Group=`` and ``DEDICATED_SERVICE_USER`` is a
    guaranteed ``SERVICE_USER`` refusal on the host, which is precisely the
    kind of never-executed integration fault this packet keeps hitting.
    """
    text = (Path(packet_dir) / "systemd_unit_template_r3.service").read_text()
    # systemd continues a directive across a trailing backslash; the contract
    # is about whole directives, so join them before looking at prefixes
    joined, buf = [], ""
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("#"):
            continue
        buf += line[:-1] + " " if line.endswith("\\") else line
        if not line.endswith("\\"):
            joined.append(buf)
            buf = ""
    lines = [l for l in joined if l]
    out = {
        "user_matches_supervisor":
            ("User=%s" % sup.DEDICATED_SERVICE_USER) in lines,
        "group_matches_supervisor":
            ("Group=%s" % sup.DEDICATED_SERVICE_GROUP) in lines,
        "mints_as_root":
            any(l.startswith("ExecStartPre=+") and "mint_claim_r3.sh" in l
                for l in lines),
        "retires_as_root":
            any(l.startswith("ExecStopPost=+") and "retire_claim_r3.sh" in l
                for l in lines),
        "start_is_unprivileged":
            any(l.startswith("ExecStart=") and not l.startswith("ExecStart=+")
                for l in lines),
        "writable_path_is_the_run_directory":
            "ReadWritePaths=<ABSOLUTE_RUN_DIRECTORY>" in lines,
        "run_parent_is_not_writable":
            not any(l.startswith("ReadWritePaths=") and "PARENT" in l
                    for l in lines),
        "capabilities_empty": "CapabilityBoundingSet=" in lines
                              and "AmbientCapabilities=" in lines,
        "no_new_privileges": "NoNewPrivileges=yes" in lines,
        "no_restart": "Restart=no" in lines,
    }
    out["ok"] = all(v for v in out.values() if isinstance(v, bool))
    return out


def run_controls(sup, packet_dir=None, tmp_root=None, run=None):
    """Every custody control, against the supervisor module handed in."""
    packet_dir = Path(packet_dir or Path(sup.__file__).resolve().parent)
    report = {"schema": SCHEMA, "euid": os.geteuid(), "egid": os.getegid()}
    if os.geteuid() == 0:
        report["ok"] = False
        report["refused"] = ("the custody fixtures must not run as root: root "
                             "bypasses every permission denial they assert")
        return report
    made = tmp_root is None
    root = Path(tmp_root or tempfile.mkdtemp(prefix="jc2-k0-r3-custody-"))
    try:
        report["production_policy"] = production_policy_controls(sup, packet_dir)
        report["posix_semantics"] = posix_semantics_controls(root)
        report["boundary"] = boundary_controls(sup, root)
        report["mint_script"] = mint_script_controls(packet_dir)
        report["unit_contract"] = unit_contract_controls(sup, packet_dir)
        if run is not None:
            report["runner_pre_run_law"] = runner_pre_run_controls(sup, run, root)
    finally:
        if made:
            shutil.rmtree(str(root), ignore_errors=True)
    report["ok"] = all(report[k]["ok"] for k in
                       ("production_policy", "posix_semantics", "boundary",
                        "mint_script", "unit_contract")) \
        and (run is None or report["runner_pre_run_law"]["ok"])
    return report


# --------------------------------------------------------------------------
# the on-host dry run
# --------------------------------------------------------------------------


def on_host_dry_run(sup, run_path, authorization_path):
    """Production policy, real tree, no writes, no lease.

    Run this as the service user on the deployed host before starting the unit.
    It calls the same :func:`verify_custody_preconditions` the supervisor calls
    and stops there, so a refusal costs nothing: the authorization is still
    unconsumed and the coordinator record is still usable once the fault named
    below is fixed.
    """
    policy = sup.production_policy()
    sup.require_service_identity(policy)
    blob = Path(authorization_path).read_bytes()
    auth_sha = hashlib.sha256(blob).hexdigest()
    record = json.loads(blob)
    sup.validate_authorization_record(record)
    if str(record.get("run_path")) != str(Path(run_path)):
        sup.fault("RUN_DIR_SHAPE",
                  "the authorization names run_path %r, not %s"
                  % (record.get("run_path"), run_path))
    custody = sup.verify_custody_preconditions(policy, record, auth_sha)
    custody["authorization_sha256"] = auth_sha
    custody["consumed"] = False
    return custody


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--on-host-dry-run", action="store_true")
    ap.add_argument("--run-path")
    ap.add_argument("--authorization")
    ap.add_argument("--out", default="-")
    args = ap.parse_args(argv)

    packet = Path(__file__).resolve().parent
    sys.path.insert(0, str(packet))
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "aws_supervisor_r3", str(packet / "aws_supervisor_r3.py"))
    sup = importlib.util.module_from_spec(spec)
    sys.modules["aws_supervisor_r3"] = sup
    spec.loader.exec_module(sup)

    if args.on_host_dry_run:
        if not args.run_path or not args.authorization:
            ap.error("--on-host-dry-run needs --run-path and --authorization")
        try:
            report = {"schema": SCHEMA, "mode": "on-host-dry-run",
                      "custody": on_host_dry_run(sup, args.run_path,
                                                 args.authorization),
                      "ok": True}
        except sup.CustodyFault as exc:
            report = {"schema": SCHEMA, "mode": "on-host-dry-run",
                      "fault": {"code": exc.code, "detail": str(exc)},
                      "consumed": False, "ok": False}
    else:
        report = run_controls(sup, packet)
    text = json.dumps(report, sort_keys=True, indent=1) + "\n"
    if args.out == "-":
        sys.stdout.write(text)
    else:
        Path(args.out).write_text(text)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
