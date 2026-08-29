#!/usr/bin/env python3
"""Executable custody-boundary controls for the D43 `K0` field certificate, R4.

Every control here runs the **real** functions of ``aws_supervisor_r4.py``
against a **real** filesystem tree: real ``lstat`` results, real uid and gid
values, real POSIX permission bits, real ``O_EXCL`` semantics.  Nothing about
ownership or permission is simulated by patching ``os.stat``.

Two modes:

``run_controls(sup)`` (the default, used by ``preflight_r4.py`` P11)
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

``--on-host-dry-run`` (the unit's second ``ExecStartPre=``, run by systemd as
    ``User=jc2k0`` in the unit's own sandbox, after the root mint and before
    ``ExecStart=``)
    calls ``aws_supervisor_r4.verify_custody_preconditions`` with the
    **production** policy against the real root-owned tree and prints its JSON
    record.  It creates, writes and deletes nothing, it never reaches
    ``claim_authorization_lease``, and it therefore cannot consume the
    one-shot claim.  This is how the root-owned half of the boundary is
    verified where root-owned objects actually exist.  It is **not** free:
    ``ExecStartPre=+ mint_claim_r4.sh`` has already spent the digest by the
    time it runs, so a refusal here retires the coordinator record exactly as
    a supervisor refusal does.  What it buys is that a misconfigured host is
    refused by the service identity, in the service sandbox, before the
    supervisor stages any source or takes any lease.

``--pre-mint-advisory`` (optional, run by ops before the unit is started)
    the only check that really costs nothing.  It verifies the sealed parent,
    the authorization record and the service identity, and it **requires that
    nothing has been minted yet**: the run directory must not exist and the
    spent marker must be absent.  It can therefore never be mistaken for, or
    run in place of, the unit's dry run, and it can never mint or lease.

The module refuses to run its fixtures as root: as root every permission
denial the controls depend on would silently succeed.

R4 (the R3 review's REPAIR-1) adds four control blocks to the three R3
shipped: :func:`choreography_controls` (the unit is one ordered path, mints
once, dry-runs once, unprivileged, fail-closed), :func:`dry_run_controls`
(the dry run executed against real trees, proving it consumes nothing and
that a launch after it still works), :func:`call_graph_controls` (a static
proof that the dry run's call graph reaches no write and no lease), and
:func:`wording_controls` (the sealed prose says the mint is already spent).
"""

from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import shutil
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

SCHEMA = "d43-k0-field-certificate-custody-selftest-r4"
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

    The token is written and then chmod-ed exactly as ``mint_claim_r4.sh``
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


def fixture_authorization(sup, run_dir, **overrides):
    """A record ``validate_authorization_record`` accepts, aimed at ``run_dir``.

    Used by the dry-run controls so that the on-host entry point can be driven
    off-host end to end: the record is validated by the real validator, not by
    a paraphrase of it.
    """
    record = {
        "schema": sup.AUTH_SCHEMA,
        "route": sup.ROUTE,
        "status": "AUTHORIZED",
        "coordinator_go": True,
        "reviewer_pass": {"model": "Grok 4.6",
                          "report_path": "xmodel/some-different-model-review.md",
                          "report_sha256": "a" * 64,
                          "verdict": "PASS"},
        "host": {"host_label": "r6b", "instance_id": "i-0",
                 "instance_type": "r6i.large", "image_id": "ami-0",
                 "region": "us-east-1", "gp_version": "2.15.4"},
        "gp_binary_path": "/usr/bin/gp",
        "gp_binary_sha256": "b" * 64,
        "source_archive": "/opt/jc2/SOURCE_ARCHIVE.tar",
        "source_archive_sha256": "c" * 64,
        "packet_manifest_sha256": "d" * 64,
        "run_path": str(run_dir),
    }
    record.update(overrides)
    return record


def _tree_snapshot(root):
    """Every path under ``root`` with the attributes a write would move."""
    out = {}
    for base, dirs, files in os.walk(str(root)):
        for name in list(dirs) + list(files):
            full = Path(base) / name
            st = full.lstat()
            out[str(full.relative_to(root))] = (
                stat.S_IFMT(st.st_mode), stat.S_IMODE(st.st_mode), st.st_size,
                st.st_mtime_ns, st.st_ino, st.st_nlink)
    return out


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
    text = (Path(packet_dir) / "aws_supervisor_r4.py").read_text()
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
    mint = Path(packet_dir) / "mint_claim_r4.sh"
    retire = Path(packet_dir) / "retire_claim_r4.sh"
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
    not_root = run(mint, ["/var/lib/jc2-k0/run-20260829T010727Z",
                          "/etc/jc2-authorization.json", "jc2k0"])
    # R3's four-argument call must now be a usage refusal, not a mint: the
    # unit and the script have to agree on one arity, and a stale deployment
    # that still passes <parent> <name> <auth> <user> is refused before root
    # touches anything.
    r3_arity = run(mint, ["/var/lib/jc2-k0", "run-20260829T010727Z",
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
        "mint_r3_four_argument_call_rc": r3_arity["rc"],
        "mint_declares_three_arguments": "if (( $# != 3 ))" in text,
        "mint_takes_the_run_directory":
            'RUN_ARG=${1%/}' in text
            and 'PARENT=$(dirname "$RUN_ARG")' in text
            and 'RUN_NAME=$(basename "$RUN_ARG")' in text,
        "mint_recomposes_the_run_directory":
            '[[ "$RUN_DIR" == "$RUN_ARG" ]]' in text,
        "mint_rejects_unnormalised_paths":
            '*/../*' in text and '*//*' in text,
        "mint_says_there_is_no_external_mint":
            "THERE IS NO EXTERNAL MINT" in text,
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
                 and out["mint_r3_four_argument_call_rc"] == 64
                 and out["mint_declares_three_arguments"]
                 and out["mint_takes_the_run_directory"]
                 and out["mint_recomposes_the_run_directory"]
                 and out["mint_rejects_unnormalised_paths"]
                 and out["mint_says_there_is_no_external_mint"]
                 and out["retire_not_root_rc"] == 77
                 and out["mint_syntax_rc"] == 0 and out["retire_syntax_rc"] == 0
                 and out["spent_marker_before_run_dir"]
                 and out["token_written_before_chown_to_service"]
                 and out["noclobber_set_before_spent"]
                 and out["mint_requires_root"]
                 and out["mint_checks_parent_owner"]
                 and out["mint_checks_parent_realpath"])
    return out


EXEC_KEYS = ("ExecStartPre", "ExecStart", "ExecStartPost", "ExecReload",
             "ExecStop", "ExecStopPost", "ExecCondition")
# systemd's special executable prefixes.  "+" runs the command as root with
# the sandbox dropped; "!" and "!!" drop only part of the user switch; "-"
# makes a non-zero exit non-fatal; "@" rewrites argv[0]; ":" suppresses
# environment-variable substitution.  Only "+" is permitted in this unit, and
# only on the two root commands.
EXEC_PREFIX_CHARS = "+-!@:"


def unit_directives(text):
    """The unit's non-comment directives, with backslash continuations joined."""
    joined, buf = [], ""
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("#"):
            continue
        buf += line[:-1] + " " if line.endswith("\\") else line
        if not line.endswith("\\"):
            joined.append(buf)
            buf = ""
    return [l for l in joined if l]


def _exec_entries(lines):
    """Every Exec* directive as (key, prefixes, command), in file order."""
    out = []
    for line in lines:
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key not in EXEC_KEYS:
            continue
        prefixes = ""
        while value and value[0] in EXEC_PREFIX_CHARS:
            prefixes += value[0]
            value = value[1:]
        out.append((key, prefixes, value.strip()))
    return out


def unit_contract_controls(sup, packet_dir):
    """The unit template and the supervisor must agree on one identity.

    A mismatch between ``User=``/``Group=`` and ``DEDICATED_SERVICE_USER`` is a
    guaranteed ``SERVICE_USER`` refusal on the host, which is precisely the
    kind of never-executed integration fault this packet keeps hitting.
    """
    text = (Path(packet_dir) / "systemd_unit_template_r4.service").read_text()
    lines = unit_directives(text)
    execs = _exec_entries(lines)
    out = {
        "user_matches_supervisor":
            ("User=%s" % sup.DEDICATED_SERVICE_USER) in lines,
        "group_matches_supervisor":
            ("Group=%s" % sup.DEDICATED_SERVICE_GROUP) in lines,
        "mints_as_root":
            any(k == "ExecStartPre" and p == "+" and "mint_claim_r4.sh" in c
                for k, p, c in execs),
        "retires_as_root":
            any(k == "ExecStopPost" and p == "+" and "retire_claim_r4.sh" in c
                for k, p, c in execs),
        "start_is_unprivileged":
            any(k == "ExecStart" and p == "" for k, p, c in execs),
        "writable_path_is_the_run_directory":
            "ReadWritePaths=<ABSOLUTE_RUN_DIRECTORY>" in lines,
        "run_parent_is_not_writable":
            not any(l.startswith("ReadWritePaths=") and "PARENT" in l
                    for l in lines),
        "capabilities_empty": "CapabilityBoundingSet=" in lines
                              and "AmbientCapabilities=" in lines,
        "no_new_privileges": "NoNewPrivileges=yes" in lines,
        "no_restart": "Restart=no" in lines,
        "type_oneshot": "Type=oneshot" in lines,
    }
    out["ok"] = all(v for v in out.values() if isinstance(v, bool))
    return out


def choreography_controls(sup, packet_dir):
    """R4's REPAIR-1: the unit *is* the deployment order, and it is one path.

    The R3 review's blocking finding was that the sealed authorization
    template told a coordinator to mint by hand, dry-run, then start a unit
    whose own ``ExecStartPre=+`` mints again -- so an honest launch on a
    correctly configured host died ``MINT_ALREADY_SPENT`` before any
    mathematics.  These controls read the shipped unit and the shipped
    coordinator template and require exactly one ordered path:

        root mint  ->  service-identity dry run  ->  supervisor  ->  root retire

    with one mint, one dry run, one ``ExecStart``, one ``ExecStopPost``, no
    failure-tolerant prefixes, and a single sentinel for the run directory and
    for the authorization so that the four commands provably name the same
    two paths.
    """
    unit_path = Path(packet_dir) / "systemd_unit_template_r4.service"
    text = unit_path.read_text()
    lines = unit_directives(text)
    execs = _exec_entries(lines)
    pres = [(p, c) for k, p, c in execs if k == "ExecStartPre"]
    starts = [(p, c) for k, p, c in execs if k == "ExecStart"]
    posts = [(p, c) for k, p, c in execs if k == "ExecStopPost"]

    mint_idx = [i for i, (_p, c) in enumerate(pres)
                if "mint_claim_r4.sh" in c]
    dry_idx = [i for i, (_p, c) in enumerate(pres)
               if "--on-host-dry-run" in c]
    mint_cmd = pres[mint_idx[0]] if mint_idx else ("", "")
    dry_cmd = pres[dry_idx[0]] if dry_idx else ("", "")

    # the mint's argument tail, which must match the script's own arity
    mint_args = []
    if mint_cmd[1]:
        tail = mint_cmd[1].split("mint_claim_r4.sh", 1)[1]
        mint_args = tail.split()

    def token_users(token):
        return sorted({k for k, _p, c in execs if token in c}
                      | ({"ReadWritePaths"}
                         if ("ReadWritePaths=" + token) in lines else set()))

    out = {
        # --- shape: two ExecStartPre, in this order ----------------------
        "exec_start_pre_count": len(pres),
        "exec_start_count": len(starts),
        "exec_stop_post_count": len(posts),
        "no_exec_start_post": not any(k == "ExecStartPost" for k, _p, _c in execs),
        "mint_is_the_first_exec_start_pre": mint_idx == [0],
        "dry_run_is_the_second_exec_start_pre": dry_idx == [1],
        "dry_run_after_mint": bool(mint_idx and dry_idx
                                   and mint_idx[0] < dry_idx[0]),
        # --- one-shot: the unit mints once and dry-runs once -------------
        "unit_mints_exactly_once":
            sum("mint_claim_r4.sh" in c for _k, _p, c in execs) == 1,
        "unit_dry_runs_exactly_once":
            sum("--on-host-dry-run" in c for _k, _p, c in execs) == 1,
        # --- identity: root mints, the SERVICE USER dry-runs -------------
        "mint_is_root_prefixed": mint_cmd[0] == "+",
        "dry_run_carries_no_prefix": dry_cmd[0] == "",
        "dry_run_runs_as_service_identity":
            dry_cmd[0] == "" and ("User=%s" % sup.DEDICATED_SERVICE_USER)
            in lines,
        "dry_run_is_the_packet_selftest":
            "custody_selftest_r4.py" in dry_cmd[1],
        "dry_run_uses_isolated_interpreter":
            " -I " in dry_cmd[1] and " -B " in dry_cmd[1],
        "start_carries_no_prefix": all(p == "" for p, _c in starts),
        "retire_is_root_prefixed": all(p == "+" for p, _c in posts),
        # --- fail-closed: no "-", "!", "!!", "@" or ":" anywhere ---------
        "no_failure_tolerant_exec_prefixes":
            all(set(p) <= {"+"} for _k, p, _c in execs),
        "only_mint_and_retire_are_privileged":
            sorted(k for k, p, _c in execs if p) == ["ExecStartPre",
                                                     "ExecStopPost"],
        # --- one sentinel per path, so the four commands compose ---------
        "run_directory_sentinel_users": token_users("<ABSOLUTE_RUN_DIRECTORY>"),
        "authorization_sentinel_users":
            token_users("<ABSOLUTE_AUTHORIZATION_JSON>"),
        "no_split_run_directory_sentinels":
            "<ABSOLUTE_SEALED_PARENT_DIRECTORY>" not in text
            and "<RUN_DIRECTORY_NAME>" not in text,
        # --- the mint call matches the mint script -----------------------
        "mint_argument_count": len(mint_args),
        "mint_arguments":
            mint_args == ["<ABSOLUTE_RUN_DIRECTORY>",
                          "<ABSOLUTE_AUTHORIZATION_JSON>",
                          sup.DEDICATED_SERVICE_USER],
        "dry_run_binds_run_path":
            "--run-path <ABSOLUTE_RUN_DIRECTORY>" in dry_cmd[1],
        "dry_run_binds_authorization":
            "--authorization <ABSOLUTE_AUTHORIZATION_JSON>" in dry_cmd[1],
    }
    out["ok"] = (
        out["exec_start_pre_count"] == 2
        and out["exec_start_count"] == 1
        and out["exec_stop_post_count"] == 1
        and out["mint_argument_count"] == 3
        and out["run_directory_sentinel_users"] == ["ExecStartPre",
                                                    "ExecStopPost",
                                                    "ReadWritePaths"]
        and out["authorization_sentinel_users"] == ["ExecStart", "ExecStartPre"]
        and all(v for k, v in out.items() if isinstance(v, bool)))
    return out


# --------------------------------------------------------------------------
# R4: the dry run, executed, and proved unable to consume the one-shot claim
# --------------------------------------------------------------------------


def _dry_run_fixture(sup, tmp, policy, run_name="run-20260829T010727Z",
                     record_overrides=None, record_run_dir=None, **tree_kwargs):
    """A sealed tree whose claim token is named after the REAL record digest.

    The authorization is frozen on disk first, its SHA-256 is read back from
    the bytes exactly as the dry run reads it, and only then is the claim
    token minted for that digest.  Nothing here hands a digest to the code
    under test.
    """
    run_dir = Path(tmp) / "sealed" / run_name
    auth_path = Path(tmp) / "authorization.json"
    blob = (json.dumps(fixture_authorization(
        sup, record_run_dir if record_run_dir is not None else run_dir,
        **(record_overrides or {})), sort_keys=True, indent=1) + "\n"
    ).encode("ascii")
    auth_path.write_bytes(blob)
    auth_sha = hashlib.sha256(blob).hexdigest()
    tree = build_tree(sup, tmp, policy, auth_sha=auth_sha, run_name=run_name,
                      **tree_kwargs)
    tree["auth_path"] = str(auth_path)
    tree["auth_sha"] = auth_sha
    return tree


def dry_run_controls(sup, root, cs=None, cli_dir=None):
    """The unit's second ``ExecStartPre``, driven against real trees.

    ``cs`` is the module that owns ``on_host_dry_run``; ``preflight_r4.py``
    passes a *mutated* copy so that this control -- which stays sealed -- can
    show the mutation breaks it.  ``cli_dir`` is the directory whose
    ``custody_selftest_r4.py`` is executed as a subprocess for the exit-code
    controls.

    The load-bearing claim is ``dry_run_then_launch_still_succeeds``: after two
    dry runs the launch still works and takes exactly one lease.  A dry run
    that consumed the one-shot claim could not leave that true.
    """
    cs = cs or sys.modules[__name__]
    cli_dir = Path(cli_dir or Path(__file__).resolve().parent)
    policy = fixture_policy(sup)
    controls = {}

    # ---- 1. a good tree verifies, and nothing in it moves ---------------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = _dry_run_fixture(sup, tmp, policy)
        spent_dir = tree["parent"] / sup.SPENT_DIRNAME
        spent_dir.mkdir(mode=0o700)
        spent = spent_dir / (tree["auth_sha"] + ".spent")
        spent.write_text("{}\n")
        os.chmod(str(spent), 0o444)
        before = _tree_snapshot(tmp)
        try:
            custody = cs.on_host_dry_run(sup, str(tree["run_dir"]),
                                         tree["auth_path"], policy=policy)
        except Exception as exc:                              # noqa: BLE001
            custody = {"unexpected_fault": repr(exc)[:200]}
        after = _tree_snapshot(tmp)
        controls["dry_run_verifies_a_good_tree"] = {
            "run_dir_matches": custody.get("run_dir") == str(tree["run_dir"]),
            "claim_seen": bool(custody.get("claim")),
            "authorization_sha256_matches":
                custody.get("authorization_sha256") == tree["auth_sha"],
            "lease_taken_flag": custody.get("lease_taken"),
            "ok": custody.get("run_dir") == str(tree["run_dir"])
                  and custody.get("authorization_sha256") == tree["auth_sha"]
                  and custody.get("lease_taken") is False}
        controls["dry_run_creates_nothing"] = {
            "paths_before": len(before), "paths_after": len(after),
            "identical": before == after,
            "changed": sorted(set(before) ^ set(after)),
            "leases_in_tree": _leases_anywhere(tmp, sup),
            "ok": before == after and not _leases_anywhere(tmp, sup)}
        controls["dry_run_does_not_spend_the_mint"] = {
            "spent_files": sorted(f.name for f in spent_dir.iterdir()),
            "ok": sorted(f.name for f in spent_dir.iterdir())
                  == [tree["auth_sha"] + ".spent"]}

    # ---- 2. two dry runs, then the launch still works -------------------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = _dry_run_fixture(sup, tmp, policy)
        dry_faults = []
        for _ in range(2):
            try:
                cs.on_host_dry_run(sup, str(tree["run_dir"]),
                                   tree["auth_path"], policy=policy)
            except Exception as exc:                          # noqa: BLE001
                dry_faults.append(repr(exc)[:160])
        leases_after_dry = _leases_anywhere(tmp, sup)
        try:
            established = sup.establish_custody(policy, tree["record"],
                                                tree["auth_sha"])
            lease = Path(established["authorization_lease"]).name
            launched = True
        except Exception as exc:                              # noqa: BLE001
            lease, launched = repr(exc)[:160], False
        leases_after_launch = _leases_anywhere(tmp, sup)
        controls["dry_run_then_launch_still_succeeds"] = {
            "dry_run_faults": dry_faults,
            "leases_after_two_dry_runs": leases_after_dry,
            "leases_after_launch": len(leases_after_launch),
            "launch_succeeded": launched,
            "lease": lease,
            "ok": not dry_faults and leases_after_dry == [] and launched
                  and len(leases_after_launch) == 1}

    # ---- 3. identity is checked, and checked first ----------------------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        # the tree is also broken (no claim token); if identity were checked
        # after the filesystem the fault would be CLAIM_ABSENT instead
        tree = _dry_run_fixture(sup, tmp, policy, with_claim=False)
        stranger = fixture_policy(sup, service_uid=os.geteuid() + 1)
        controls["dry_run_requires_service_identity"] = _expect_fault(
            sup, lambda: cs.on_host_dry_run(sup, str(tree["run_dir"]),
                                            tree["auth_path"],
                                            policy=stranger), "SERVICE_USER")

    # ---- 4. every precondition fault propagates out of the dry run ------
    for label, kwargs, code in (
            ("dry_run_reports_claim_absent", {"with_claim": False},
             "CLAIM_ABSENT"),
            ("dry_run_reports_group_writable_parent", {"parent_mode": 0o775},
             "PATH_MODE"),
            ("dry_run_reports_wrong_run_dir_mode", {"run_mode": 0o750},
             "RUN_DIR_MODE")):
        with tempfile.TemporaryDirectory(dir=root) as tmp:
            tree = _dry_run_fixture(sup, tmp, policy, **kwargs)
            entry = _expect_fault(
                sup, lambda tr=tree: cs.on_host_dry_run(
                    sup, str(tr["run_dir"]), tr["auth_path"], policy=policy),
                code)
            entry["leases_in_tree"] = len(_leases_anywhere(tmp, sup))
            entry["ok"] = entry["ok"] and entry["leases_in_tree"] == 0
            controls[label] = entry

    # ---- 5. the record must name the directory the unit passes ----------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = _dry_run_fixture(
            sup, tmp, policy,
            record_run_dir=Path(tmp) / "sealed" / "run-20260829T999999Z")
        controls["dry_run_refuses_run_path_mismatch"] = _expect_fault(
            sup, lambda: cs.on_host_dry_run(sup, str(tree["run_dir"]),
                                            tree["auth_path"], policy=policy),
            "RUN_DIR_SHAPE")

    # ---- 6. the dry run validates the record it is handed ---------------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = _dry_run_fixture(
            sup, tmp, policy,
            record_overrides={"status": "TEMPLATE_NOT_AUTHORIZED"})
        controls["dry_run_refuses_an_unauthorized_record"] = _expect_fault(
            sup, lambda: cs.on_host_dry_run(sup, str(tree["run_dir"]),
                                            tree["auth_path"], policy=policy),
            "AUTHORIZATION_STATUS")

    # ---- 7. the CLI fails closed, which is what systemd reads -----------
    script = cli_dir / "custody_selftest_r4.py"
    missing = subprocess.run(
        [sys.executable, "-I", "-B", str(script), "--on-host-dry-run",
         "--run-path", "/nonexistent/jc2-k0/run-20260829T010727Z",
         "--authorization", "/nonexistent/authorization.json", "--out", "-"],
        capture_output=True, text=True, timeout=120)
    no_args = subprocess.run(
        [sys.executable, "-I", "-B", str(script), "--on-host-dry-run"],
        capture_output=True, text=True, timeout=120)
    try:
        payload = json.loads(missing.stdout or "{}")
    except ValueError:
        payload = {}
    controls["dry_run_cli_fails_closed"] = {
        "rc": missing.returncode,
        "reported_ok": payload.get("ok"),
        "consumed": payload.get("consumed"),
        "stderr": missing.stderr.strip()[:200],
        "ok": missing.returncode == 70 and payload.get("ok") is False
              and payload.get("consumed") is False}
    both = subprocess.run(
        [sys.executable, "-I", "-B", str(script), "--on-host-dry-run",
         "--pre-mint-advisory", "--run-path", "/nonexistent/run-20260829T010727Z",
         "--authorization", "/nonexistent/authorization.json"],
        capture_output=True, text=True, timeout=120)
    controls["dry_run_cli_requires_its_arguments"] = {
        "rc": no_args.returncode, "ok": no_args.returncode == 2}
    controls["dry_run_and_advisory_are_never_combined"] = {
        "rc": both.returncode,
        "stderr": both.stderr.strip()[-160:],
        "ok": both.returncode == 2 and "never combined" in both.stderr}

    controls["ok"] = all(v["ok"] for v in controls.values()
                         if isinstance(v, dict))
    return controls


def pre_mint_advisory_controls(sup, root, cs=None):
    """The optional ops check is read-only and cannot stand in for the unit.

    It must accept a sealed parent with nothing minted, refuse the moment the
    run directory or the spent marker exists, and never create anything.
    """
    cs = cs or sys.modules[__name__]
    policy = fixture_policy(sup)
    controls = {}

    # ---- the pre-mint state: parent sealed, nothing minted yet ----------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = _dry_run_fixture(sup, tmp, policy)
        shutil.rmtree(str(tree["run_dir"]))          # back to the pre-mint state
        before = _tree_snapshot(tmp)
        record = cs.pre_mint_advisory(sup, str(tree["run_dir"]),
                                      tree["auth_path"], policy=policy)
        after = _tree_snapshot(tmp)
        controls["advisory_accepts_a_premint_tree"] = {
            "advisory_only": record.get("advisory_only"),
            "minted": record.get("minted"),
            "creates_nothing": before == after,
            "ok": record.get("advisory_only") is True
                  and record.get("minted") is False
                  and record.get("consumed") is False
                  and before == after
                  and not _leases_anywhere(tmp, sup)}

    # ---- once the unit has minted, the advisory refuses -----------------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = _dry_run_fixture(sup, tmp, policy)
        controls["advisory_refuses_after_the_mint"] = _expect_fault(
            sup, lambda: cs.pre_mint_advisory(sup, str(tree["run_dir"]),
                                              tree["auth_path"],
                                              policy=policy),
            "PREMINT_ALREADY_MINTED")

    # ---- a spent digest is refused even if the run directory is gone ----
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = _dry_run_fixture(sup, tmp, policy)
        shutil.rmtree(str(tree["run_dir"]))
        spent_dir = tree["parent"] / sup.SPENT_DIRNAME
        spent_dir.mkdir(mode=0o700)
        (spent_dir / (tree["auth_sha"] + ".spent")).write_text("{}\n")
        controls["advisory_refuses_a_spent_digest"] = _expect_fault(
            sup, lambda: cs.pre_mint_advisory(sup, str(tree["run_dir"]),
                                              tree["auth_path"],
                                              policy=policy),
            "PREMINT_ALREADY_MINTED")

    # ---- a bad parent is refused before anything else -------------------
    with tempfile.TemporaryDirectory(dir=root) as tmp:
        tree = _dry_run_fixture(sup, tmp, policy, parent_mode=0o775)
        shutil.rmtree(str(tree["run_dir"]))
        controls["advisory_refuses_a_writable_parent"] = _expect_fault(
            sup, lambda: cs.pre_mint_advisory(sup, str(tree["run_dir"]),
                                              tree["auth_path"],
                                              policy=policy), "PATH_MODE")

    controls["ok"] = all(v["ok"] for v in controls.values()
                         if isinstance(v, dict))
    return controls


# --------------------------------------------------------------------------
# R4: a static proof that the dry run cannot write or lease
# --------------------------------------------------------------------------

# Anything that could create, alter or remove a filesystem object, plus the
# two functions that take the one-shot lease.  If the dry run's call graph
# reaches any of these, the "it consumes nothing" claim is not a claim about
# code, and the control fails.
WRITE_PRIMITIVES = frozenset({
    "mkdir", "makedirs", "rmdir", "remove", "unlink", "rename", "replace",
    "chmod", "chown", "lchmod", "symlink", "link", "truncate", "write",
    "write_text", "write_bytes", "touch", "rmtree", "copy", "copy2",
    "copyfile", "copytree", "move", "mkstemp", "mkdtemp", "fsync",
    "fsync_directory", "atomic_bytes", "claim_authorization_lease",
    "establish_custody", "extractall", "extract",
})
DRY_RUN_SUPERVISOR_CALLS = frozenset({
    "production_policy", "require_service_identity",
    "validate_authorization_record", "verify_custody_preconditions", "fault",
})


def _module_functions(tree):
    """Module-level functions *and* class methods, by name.

    Methods are included so that an attribute call such as ``policy.describe()``
    on the dry-run path is walked rather than merely recorded: the reachability
    below follows any attribute whose name matches a function defined in this
    module, which over-approximates in the safe direction.
    """
    out = {}
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            out[node.name] = node
        elif isinstance(node, ast.ClassDef):
            for sub in node.body:
                if isinstance(sub, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    out.setdefault(sub.name, sub)
    return out


def _calls_in(node):
    """(local function names, attribute names, non-read ``open`` flag)."""
    names, attrs, bad_open = set(), set(), False
    for sub in ast.walk(node):
        if not isinstance(sub, ast.Call):
            continue
        fn = sub.func
        if isinstance(fn, ast.Name):
            names.add(fn.id)
            if fn.id == "open":
                bad_open = bad_open or not _is_read_open(sub)
        elif isinstance(fn, ast.Attribute):
            attrs.add(fn.attr)
            if fn.attr == "open":
                bad_open = bad_open or not _is_read_open(sub)
    return names, attrs, bad_open


def _is_read_open(call):
    mode = None
    if call.args:
        first = call.args[0]
        if isinstance(first, ast.Constant) and isinstance(first.value, str) \
                and set(first.value) <= set("rbt+wxa"):
            mode = first.value
    for kw in call.keywords:
        if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
            mode = kw.value.value
    if mode is None:
        return len(call.args) == 0 and not call.keywords     # bare .open()
    return set(mode) <= set("rbt")


def call_graph_controls(sup, packet_dir):
    """``verify_custody_preconditions`` reaches no write and no lease.

    This is the static half of "the dry run cannot consume the claim".  The
    executed half is :func:`dry_run_controls`; this half says the property is
    structural rather than a fact about the particular fixtures.
    """
    packet_dir = Path(packet_dir)
    sup_tree = ast.parse((packet_dir / "aws_supervisor_r4.py").read_text())
    funcs = _module_functions(sup_tree)

    reached, frontier = set(), ["verify_custody_preconditions"]
    attrs, opens = set(), False
    while frontier:
        name = frontier.pop()
        if name in reached or name not in funcs:
            continue
        reached.add(name)
        local, attr, bad_open = _calls_in(funcs[name])
        attrs |= attr
        opens = opens or bad_open
        frontier.extend(sorted(local))
        frontier.extend(sorted(a for a in attr if a in funcs))

    hits = sorted((reached | attrs) & WRITE_PRIMITIVES)

    cs_tree = ast.parse((packet_dir / "custody_selftest_r4.py").read_text())
    dry = _module_functions(cs_tree).get("on_host_dry_run")
    sup_calls = set()
    if dry is not None:
        for sub in ast.walk(dry):
            if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute) \
                    and isinstance(sub.func.value, ast.Name) \
                    and sub.func.value.id == "sup":
                sup_calls.add(sub.func.attr)

    out = {
        "reachable_from_verify_custody_preconditions": sorted(reached),
        "write_primitive_hits": hits,
        "all_opens_are_read_only": not opens,
        "reaches_no_write_primitive": hits == [] and not opens,
        "covers_the_four_gates":
            {"require_root_owned_immutable", "require_service_owned_run_dir",
             "verify_claim_token", "require_run_dir_pristine"} <= reached,
        "lease_is_unreachable":
            "claim_authorization_lease" not in reached
            and "claim_authorization_lease" not in attrs,
        "dry_run_supervisor_calls": sorted(sup_calls),
        "dry_run_calls_only_read_only_supervisor_api":
            bool(sup_calls) and sup_calls <= DRY_RUN_SUPERVISOR_CALLS,
        "dry_run_verifies_preconditions":
            "verify_custody_preconditions" in sup_calls,
        "dry_run_checks_identity": "require_service_identity" in sup_calls,
        "establish_custody_verifies_before_leasing":
            _verify_precedes_lease(funcs.get("establish_custody")),
    }
    out["ok"] = all(v for v in out.values() if isinstance(v, bool))
    return out


def _verify_precedes_lease(node):
    """In ``establish_custody``, the verify call must come before the burn."""
    if node is None:
        return False
    order = []
    for sub in ast.walk(node):
        if isinstance(sub, ast.Call) and isinstance(sub.func, ast.Name):
            if sub.func.id in ("verify_custody_preconditions",
                               "claim_authorization_lease"):
                order.append((sub.lineno, sub.col_offset, sub.func.id))
    order.sort()
    return [n for _l, _c, n in order] == ["verify_custody_preconditions",
                                          "claim_authorization_lease"]


# --------------------------------------------------------------------------
# R4: the sealed prose must state what the dry run actually costs
# --------------------------------------------------------------------------

# The R3 review's second finding: the packet said a refused precondition
# "never consumes this record" and that the dry run "consumes nothing".  Both
# are true of the LEASE and false of the MINT, which spends the digest first.
# These controls freeze the repaired wording so a future edit cannot quietly
# restore the claim that a refusal is free.
# The phrases are assembled from fragments so that this control file does not
# itself contain the strings it forbids; a literal table would make the scan
# report its own source.
_FREE = " costs nothing"
_NEVER = " never consumes this record"
FORBIDDEN_WORDING = [
    ("authorization_template_r4.json", "so a failed precondition" + _NEVER),
    ("authorization_template_r4.json", "It consumes"),
    ("authorization_template_r4.json", "only then start the unit"),
    ("systemd_unit_template_r4.service",
     "and consumes nothing: it stops before the lease"),
    ("custody_selftest_r4.py", "so a refusal" + _FREE),
    ("README.md", "so a refusal there costs no coordinator record"),
    ("preregistration_r4.json", "which consumes nothing."),
    ("REVIEW_REQUEST.md", "run by ops on the deployed host"),
]
# the repaired sentence, in every file a coordinator or reviewer reads
REQUIRED_WORDING = [
    ("authorization_template_r4.json", "the mint has already spent the digest"),
    ("systemd_unit_template_r4.service",
     "the mint has already spent the digest"),
    ("custody_selftest_r4.py", "the mint has already spent the digest"),
    ("README.md", "the mint has already spent the digest"),
    ("preregistration_r4.json", "the mint has already spent the digest"),
    ("authorization_template_r4.json", "systemctl start"),
    ("mint_claim_r4.sh", "THERE IS NO EXTERNAL MINT"),
]


def wording_controls(packet_dir):
    """No sealed file may tell a coordinator that a refusal is free."""
    packet_dir = Path(packet_dir)
    present, absent = [], []
    for name, phrase in FORBIDDEN_WORDING:
        if phrase.lower() in (packet_dir / name).read_text().lower():
            present.append([name, phrase])
    for name, phrase in REQUIRED_WORDING:
        if phrase.lower() not in (packet_dir / name).read_text().lower():
            absent.append([name, phrase])
    return {"forbidden_phrases_present": present,
            "required_phrases_absent": absent,
            "forbidden_checked": len(FORBIDDEN_WORDING),
            "required_checked": len(REQUIRED_WORDING),
            "no_forbidden_phrase": not present,
            "no_missing_required_phrase": not absent,
            "ok": not present and not absent}


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
    root = Path(tmp_root or tempfile.mkdtemp(prefix="jc2-k0-r4-custody-"))
    try:
        report["production_policy"] = production_policy_controls(sup, packet_dir)
        report["posix_semantics"] = posix_semantics_controls(root)
        report["boundary"] = boundary_controls(sup, root)
        report["mint_script"] = mint_script_controls(packet_dir)
        report["unit_contract"] = unit_contract_controls(sup, packet_dir)
        report["choreography"] = choreography_controls(sup, packet_dir)
        report["dry_run"] = dry_run_controls(sup, root, cli_dir=packet_dir)
        report["pre_mint_advisory"] = pre_mint_advisory_controls(sup, root)
        report["call_graph"] = call_graph_controls(sup, packet_dir)
        report["wording"] = wording_controls(packet_dir)
        if run is not None:
            report["runner_pre_run_law"] = runner_pre_run_controls(sup, run, root)
    finally:
        if made:
            shutil.rmtree(str(root), ignore_errors=True)
    report["ok"] = all(report[k]["ok"] for k in
                       ("production_policy", "posix_semantics", "boundary",
                        "mint_script", "unit_contract", "choreography",
                        "dry_run", "pre_mint_advisory", "call_graph",
                        "wording")) \
        and (run is None or report["runner_pre_run_law"]["ok"])
    return report


# --------------------------------------------------------------------------
# the on-host dry run (the unit's second ExecStartPre) and the ops advisory
# --------------------------------------------------------------------------


def on_host_dry_run(sup, run_path, authorization_path, policy=None):
    """Production policy, real tree, no writes, no lease.

    This is the unit's second ``ExecStartPre=``.  systemd runs it with no
    ``+`` prefix, so it executes as ``User=jc2k0`` / ``Group=jc2k0`` inside
    the unit's own sandbox and mount namespace -- the same identity and the
    same view of the filesystem ``ExecStart=`` gets -- immediately after the
    root ``ExecStartPre=+`` mint and before the supervisor.

    It calls the same :func:`verify_custody_preconditions` the supervisor
    calls and stops there.  It creates, writes and removes nothing, and its
    call graph never reaches ``claim_authorization_lease``
    (:func:`call_graph_controls` proves both statically,
    :func:`dry_run_controls` executes them), so it cannot consume the one-shot
    claim: a launch after any number of dry runs still takes its lease.

    It is not free.  By the time it runs, the mint has already spent the
    digest, so a refusal here retires the coordinator record exactly as a
    supervisor refusal does; what it buys is that a misconfigured host is
    refused by the service identity, in the service sandbox, before the
    supervisor stages any source.  The only check that costs nothing is
    :func:`pre_mint_advisory`, which runs before the unit is started.

    ``policy`` exists so the controls can drive this function off-host; the
    production caller (:func:`main`) never passes it, so the deployed dry run
    always builds ``sup.production_policy()``.
    """
    policy = sup.production_policy() if policy is None else policy
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
    custody["lease_taken"] = False
    custody["cost"] = ("the mint has already spent the digest; this check "
                       "does not take the consumption lease, and a refusal "
                       "here retires the coordinator record")
    return custody


def pre_mint_advisory(sup, run_path, authorization_path, policy=None):
    """ADVISORY ONLY, and the one check that really costs nothing.

    Run by ops **before** ``systemctl start``, as an optional step that
    changes nothing: it verifies the sealed parent, the frozen authorization
    record and the service identity, and it **requires that nothing has been
    minted yet** -- the run directory must not exist and
    ``<sealed parent>/spent/<digest>.spent`` must be absent.

    That last requirement is what keeps R4 on one path.  This function cannot
    be mistaken for the unit's dry run and cannot be run in its place: the
    moment ``ExecStartPre=+ mint_claim_r4.sh`` has run, this refuses
    ``PREMINT_ALREADY_MINTED``.  It creates nothing, it mints nothing, and it
    takes no lease.
    """
    policy = sup.production_policy() if policy is None else policy
    blob = Path(authorization_path).read_bytes()
    auth_sha = hashlib.sha256(blob).hexdigest()
    record = json.loads(blob)
    sup.validate_authorization_record(record)
    run_dir = Path(run_path)
    if str(record.get("run_path")) != str(run_dir):
        sup.fault("RUN_DIR_SHAPE",
                  "the authorization names run_path %r, not %s"
                  % (record.get("run_path"), run_path))
    parent = sup.require_root_owned_immutable(policy, run_dir.parent,
                                              "run parent directory")
    if run_dir.exists() or run_dir.is_symlink():
        sup.fault("PREMINT_ALREADY_MINTED",
                  "%s already exists: this advisory runs BEFORE the unit is "
                  "started and before anything is minted.  Once the unit's "
                  "ExecStartPre=+ mint has run, the unit's own second "
                  "ExecStartPre dry run is the check that applies." % run_dir)
    spent = parent / sup.SPENT_DIRNAME / (auth_sha + ".spent")
    if spent.exists() or spent.is_symlink():
        sup.fault("PREMINT_ALREADY_MINTED",
                  "%s exists: this authorization digest has already been "
                  "minted and cannot be launched again" % spent)
    return {"mode": "pre-mint-advisory", "advisory_only": True,
            "sealed_parent": str(parent), "run_path": str(run_dir),
            "authorization_sha256": auth_sha,
            "minted": False, "consumed": False, "lease_taken": False,
            "identity_is_service_user": os.geteuid() == policy.service_uid,
            "policy": policy.describe()}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--on-host-dry-run", action="store_true",
                    help="the unit's second ExecStartPre; verifies the minted "
                         "tree as the service user and takes no lease")
    ap.add_argument("--pre-mint-advisory", action="store_true",
                    help="optional ops check BEFORE the unit is started; "
                         "refuses once anything has been minted")
    ap.add_argument("--run-path")
    ap.add_argument("--authorization")
    ap.add_argument("--out", default="-")
    args = ap.parse_args(argv)

    packet = Path(__file__).resolve().parent
    sys.path.insert(0, str(packet))
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "aws_supervisor_r4", str(packet / "aws_supervisor_r4.py"))
    sup = importlib.util.module_from_spec(spec)
    sys.modules["aws_supervisor_r4"] = sup
    spec.loader.exec_module(sup)

    if args.on_host_dry_run and args.pre_mint_advisory:
        ap.error("--on-host-dry-run and --pre-mint-advisory are different "
                 "steps and are never combined")
    rc_on_refusal = 0
    if args.on_host_dry_run or args.pre_mint_advisory:
        mode = ("on-host-dry-run" if args.on_host_dry_run
                else "pre-mint-advisory")
        if not args.run_path or not args.authorization:
            ap.error("--%s needs --run-path and --authorization" % mode)
        entry = (on_host_dry_run if args.on_host_dry_run
                 else pre_mint_advisory)
        # Fail closed for systemd: any refusal, of any kind, must be a
        # non-zero exit, because a zero exit lets ExecStart= run.
        rc_on_refusal = 70
        try:
            report = {"schema": SCHEMA, "mode": mode,
                      "custody": entry(sup, args.run_path, args.authorization),
                      "consumed": False, "ok": True}
        except sup.CustodyFault as exc:
            report = {"schema": SCHEMA, "mode": mode,
                      "fault": {"code": exc.code, "detail": str(exc)[:600]},
                      "consumed": False, "ok": False}
            sys.stderr.write("CUSTODY_%s_FAULT %s %s\n"
                             % (mode.upper().replace("-", "_"), exc.code, exc))
        except Exception as exc:                # no custody path shows a trace
            report = {"schema": SCHEMA, "mode": mode,
                      "fault": {"code": "UNCLASSIFIED", "detail": repr(exc)[:600]},
                      "consumed": False, "ok": False}
            sys.stderr.write("CUSTODY_%s_FAULT UNCLASSIFIED %r\n"
                             % (mode.upper().replace("-", "_"), exc))
    else:
        report = run_controls(sup, packet)
        rc_on_refusal = 1
    text = json.dumps(report, sort_keys=True, indent=1) + "\n"
    if args.out == "-":
        sys.stdout.write(text)
    else:
        Path(args.out).write_text(text)
    return 0 if report["ok"] else rc_on_refusal


if __name__ == "__main__":
    raise SystemExit(main())
