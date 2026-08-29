#!/usr/bin/env python3
"""Bounded local preflight for the D43 `K0` field certificate, R4.

Runs everything that can honestly be run without AWS and without PARI:

  P1   packet manifest replay (PAYLOAD.sha256)
  P2   sealed source archive replay, byte for byte
  P3   static census audit of the PARI/GP script, with the R1 review's D12
       fragilities repaired: nested loops multiply, comments and strings are
       stripped before the parenthesis scan, and loop bounds are resolved from
       the file instead of a hardcoded table; plus a hygiene scan for the
       constructs R2 deleted and an executed bound on every printed gate
       label's width, which R1 checked only by hand
  P4   the stdlib-Python engine, all gates
  P5   the hostile mutation battery, including the MUST_SURVIVE entries and
       the theorem-separation controls
  P6   the census and observable hashes pinned in execution_pins_r4.json
  P7   the emission policy over the real artifact blobs
  P8   the isolated-import controls: a live ``python3 -I -B`` reproduction of
       the exact R1 AWS failure, the repaired sealed loader, and four negative
       controls on the loader's authority
  P9   the authority-surface controls: the coordinator-authorization validator
       against a table of crafted records, and the artifact/run-directory
       collision semantics
  P10  the gate-surface controls: for each R1 defect, the mutation that R1
       passed and R2 must fail, plus static-census mutations
  P11  the custody-boundary controls: the privilege boundary carried from R3
       executed against real directories, real uid/gid values and real POSIX
       permission bits by a non-root user, the runner's pre-run directory
       law, the root-side mint script's refusal paths, the unit-to-supervisor
       identity contract, and -- new in R4 -- the deployment choreography
       (the shipped unit parsed as ordered systemd directives), the on-host
       dry run executed end to end and proved unable to consume the one-shot
       claim, the static call-graph proof behind that, the pre-mint advisory,
       and the cost wording; plus a hostile source-mutation battery, in five
       kinds, that shows every one of those controls is load-bearing

It does NOT run PARI/GP (there is no gp on the producer host) and it does not
touch AWS.  Both facts are reported, not hidden.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from dataclasses import replace
from pathlib import Path

PACKET = Path(__file__).resolve().parent
SCHEMA = "d43-k0-field-certificate-preflight-r4"
PACKET_DIRNAME = "d43_k0_field_certificate_r4_20260829"
SEALED_MODULES = ("k0_algebra_r4", "k0_field_checker_r4", "k0_mutations_r4",
                  "runner_r4", "aws_supervisor_r4", "custody_selftest_r4")


def sha256_path(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def _load_by_path(name, path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# The preflight uses the same explicit-path import discipline as the runner:
# it never relies on the script directory being on sys.path, so it behaves
# identically under ``python3 -I``.
for _name in SEALED_MODULES:
    _load_by_path(_name, PACKET / (_name + ".py"))
CK = sys.modules["k0_field_checker_r4"]
MB = sys.modules["k0_mutations_r4"]
KA = sys.modules["k0_algebra_r4"]
RUN = sys.modules["runner_r4"]
SUP = sys.modules["aws_supervisor_r4"]
CS = sys.modules["custody_selftest_r4"]


# --------------------------------------------------------------------------
# P3: GP static census, D12-repaired
# --------------------------------------------------------------------------


def _strip(line):
    """Drop double-quoted strings and any ``\\\\`` comment tail.

    R1's predictor counted parentheses on the raw line, so a parenthesis
    inside a comment or a label string would have shifted every loop end.
    """
    out, i, n, in_str = [], 0, len(line), False
    while i < n:
        c = line[i]
        if in_str:
            if c == '"':
                in_str = False
            i += 1
            continue
        if c == '"':
            in_str = True
            i += 1
            continue
        if c == "\\" and i + 1 < n and line[i + 1] == "\\":
            break
        out.append(c)
        i += 1
    return "".join(out)


def _strip_comment(line):
    """Drop a ``\\`` comment tail but keep string literals (labels live there)."""
    out, i, n, in_str = [], 0, len(line), False
    while i < n:
        c = line[i]
        if in_str:
            out.append(c)
            if c == '"':
                in_str = False
            i += 1
            continue
        if c == '"':
            in_str = True
            out.append(c)
            i += 1
            continue
        if c == "\\" and i + 1 < n and line[i + 1] == "\\":
            break
        out.append(c)
        i += 1
    return "".join(out)


def _vector_length(text, name):
    m = re.search(r"(?m)^%s\s*=\s*\[" % re.escape(name), text)
    if not m:
        return None
    i = m.end() - 1
    depth, count, j = 0, 1, i
    while j < len(text):
        c = text[j]
        if c == "[":
            depth += 1
        elif c == "]":
            depth -= 1
            if depth == 0:
                break
        elif c == "," and depth == 1:
            count += 1
        j += 1
    return 0 if text[i:j + 1].strip() == "[]" else count


def gp_static_census(gp_text):
    """Predict the GP gate and observable counts without running gp."""
    raw = gp_text.splitlines()
    lines = [_strip(l) for l in raw]
    declared = int(re.search(r"nexpect\s*=\s*(\d+)", gp_text).group(1))
    chk_sites = [i for i, l in enumerate(lines)
                 if re.search(r"(?<!\w)chkE?\(", l)
                 and not re.match(r"\s*chkE?\(lab", l)]
    obs_sites = [i for i, l in enumerate(lines)
                 if re.search(r"(?<!\w)obs\(", l)
                 and not re.match(r"\s*obs\(k, v\)", l)]
    loops = []
    for i, l in enumerate(lines):
        m = re.match(r"\s*for \(\s*(\w+)\s*=\s*(#?\w+|\d+)\s*,\s*(#?\w+|\d+)\s*,",
                     l)
        if not m:
            continue

        def value(tok):
            if tok.isdigit():
                return int(tok)
            if tok.startswith("#"):
                return _vector_length(gp_text, tok[1:])
            return None

        lo, hi = value(m.group(2)), value(m.group(3))
        trips = None if (lo is None or hi is None) else hi - lo + 1
        depth, end = 0, None
        for j in range(i, len(lines)):
            depth += lines[j].count("(") - lines[j].count(")")
            if j > i and depth <= 0:
                end = j
                break
        loops.append({"line": i + 1, "end": None if end is None else end + 1,
                      "trips": trips})

    def multiplicity(site):
        m, unresolved = 1, []
        for lp in loops:
            if lp["end"] is not None and lp["line"] - 1 < site <= lp["end"] - 1:
                if lp["trips"] is None:
                    unresolved.append(lp["line"])
                else:
                    m *= lp["trips"]                    # D12: product, not max
        return m, unresolved

    total, obs_total, unresolved = 0, 0, []
    for s in chk_sites:
        m, u = multiplicity(s)
        total += m
        unresolved += u
    for s in obs_sites:
        m, u = multiplicity(s)
        obs_total += m
        unresolved += u
    return {"declared_nexpect": declared, "predicted_gate_count": total,
            "static_sites": len(chk_sites), "loops": len(loops),
            "predicted_observable_count": obs_total,
            "unresolved_loops_over_gates": sorted(set(unresolved)),
            "agrees": total == declared and not unresolved}


GP_LABEL_WIDTH_CAP = 80          # runner_r4.GATE_LINE allows \S.{0,80}


def gp_label_audit(gp_text):
    """Every printed gate label must fit the runner's parse window.

    A label longer than the window makes the runner fault GP_UNPARSED_LINE, so
    this is a fail-closed hazard rather than a wrong verdict -- but it would
    burn the one licensed rehearsal, exactly as the R1 import fault did.  The
    R1 review checked this by hand; here it is executed.  ``Str(...)`` labels
    are over-estimated by the literal parts plus eight characters per
    interpolated argument (a comma inside a label string is conservatively
    counted as one more argument), which bounds every value this file can
    print: the widest is the six-digit prime 105673.
    """
    text = "\n".join(_strip_comment(l) for l in gp_text.splitlines())
    widths, worst = [], None
    i = 0
    while True:
        m = re.search(r"(?<!\w)chkE?\(", text[i:])
        if not m:
            break
        start = i + m.end()
        if text[start:start + 4] == "lab,":
            i = start
            continue
        depth, j = 1, start
        while j < len(text) and depth > 0:
            if text[j] == "(":
                depth += 1
            elif text[j] == ")":
                depth -= 1
            elif text[j] == "," and depth == 1:
                break
            j += 1
        label = text[start:j]
        literals = re.findall(r'"([^"]*)"', label)
        interpolated = 0
        if label.lstrip().startswith("Str("):
            inner = label.strip()[4:-1]
            depth2, part = 0, []
            args = []
            for ch in inner:
                if ch in "([":
                    depth2 += 1
                elif ch in ")]":
                    depth2 -= 1
                if ch == "," and depth2 == 0:
                    args.append("".join(part))
                    part = []
                else:
                    part.append(ch)
            args.append("".join(part))
            interpolated = sum(1 for a in args if not a.strip().startswith('"'))
        width = sum(len(x) for x in literals) + 8 * interpolated
        widths.append(width)
        if worst is None or width > worst[0]:
            worst = (width, label.strip()[:60])
        i = j
    return {"labels": len(widths), "max_width": max(widths) if widths else 0,
            "cap": GP_LABEL_WIDTH_CAP, "widest": worst[1] if worst else None,
            "ascii_only": all(ord(c) < 128 for c in gp_text),
            "no_tabs": "\t" not in gp_text,
            "ok": bool(widths) and max(widths) <= GP_LABEL_WIDTH_CAP
                  and all(ord(c) < 128 for c in gp_text)
                  and "\t" not in gp_text}


GP_FORBIDDEN = ("alarm(", "nffactor", "nfinit", "rnfequation", "znlog",
                "znprimroot", "OPTIONAL", "Map(", "mapput", "mapget",
                "mapisdefined", "select(", "->")


def gp_hygiene(gp_text):
    """Constructs R2 deliberately removed; each is a fail-closed simplification."""
    body = "\n".join(_strip(l) for l in gp_text.splitlines())
    hits = sorted(t for t in GP_FORBIDDEN if t in body)
    return {"forbidden_constructs": hits, "ok": not hits,
            "note": "R2 deletes the optional nffactor block (D9), the Map "
                    "layer (D10 vacuous fibre test) and every discrete-log "
                    "helper, so the runner may treat any unrecognised output "
                    "line as a fault"}


def replay_archive(archive, seal):
    """Replay every sealed member out of the tar, plus the tar's own hash."""
    expect = {}
    archive_expect = None
    for line in Path(seal).read_text().splitlines():
        if not line.strip():
            continue
        sha, rel = line.split(None, 1)
        rel = rel.strip()
        if rel.endswith("SOURCE_ARCHIVE.tar"):
            archive_expect = sha
            continue
        expect[rel] = sha
    if archive_expect is None:
        return {"ok": False, "reason": "seal does not carry the archive digest"}
    if sha256_path(archive) != archive_expect:
        return {"ok": False, "reason": "archive digest drift"}
    with tarfile.open(str(archive), "r") as tar:
        got = {}
        for m in tar.getmembers():
            if not m.isfile() or m.issym() or m.islnk():
                return {"ok": False, "reason": "member %s is not a file" % m.name}
            if m.name.startswith("/") or ".." in Path(m.name).parts:
                return {"ok": False, "reason": "unsafe member %s" % m.name}
            got[m.name] = hashlib.sha256(tar.extractfile(m).read()).hexdigest()
    missing = sorted(set(expect) - set(got))
    extra = sorted(set(got) - set(expect))
    bad = sorted(k for k in set(expect) & set(got) if expect[k] != got[k])
    return {"ok": not (missing or extra or bad), "members": len(got),
            "archive_sha256": archive_expect,
            "missing": missing, "extra": extra, "hash_mismatch": bad}


# --------------------------------------------------------------------------
# P8: the isolated-import controls
# --------------------------------------------------------------------------


def _run(argv, cwd=None):
    proc = subprocess.run(argv, capture_output=True, text=True, cwd=cwd,
                          timeout=120)
    return {"argv": [str(a) for a in argv], "returncode": proc.returncode,
            "stdout": proc.stdout[-600:], "stderr": proc.stderr[-600:]}


def _smoke_copy(tmp, mutate):
    """A minimal packet copy: the manifest plus the three sealed modules."""
    dst = Path(tmp) / "packet"
    dst.mkdir()
    for name in ("PAYLOAD.sha256", "k0_algebra_r4.py",
                 "k0_field_checker_r4.py", "k0_mutations_r4.py"):
        shutil.copy2(str(PACKET / name), str(dst / name))
    mutate(dst)
    return dst


def isolated_import_controls():
    out = {}
    runner = str(PACKET / "runner_r4.py")

    # N1: the exact R1 failure, reproduced live.  Isolated mode drops the
    # script directory from sys.path, so a bare sibling import must fail.
    r = _run([sys.executable, "-I", "-B", "-c",
              "import k0_field_checker_r4"], cwd=str(PACKET))
    out["N1_r1_failure_reproduced"] = {
        "expect": "ModuleNotFoundError under python3 -I",
        "returncode": r["returncode"], "stderr": r["stderr"],
        "ok": r["returncode"] != 0 and "ModuleNotFoundError" in r["stderr"]}

    # N2: the repaired loader, in the same isolated shape.
    r = _run([sys.executable, "-I", "-B", runner, "--import-smoke"])
    out["N2_sealed_loader_ok"] = {
        "returncode": r["returncode"], "stdout": r["stdout"],
        "ok": r["returncode"] == 0 and r["stdout"].startswith("IMPORT_SMOKE_OK")}

    # N3: a tampered sealed module must not load.
    with tempfile.TemporaryDirectory() as tmp:
        def flip(dst):
            path = dst / "k0_algebra_r4.py"
            blob = path.read_bytes()
            path.write_bytes(blob + b"\n# tamper\n")
        dst = _smoke_copy(tmp, flip)
        r = _run([sys.executable, "-I", "-B", runner, "--import-smoke",
                  "--smoke-packet-dir", str(dst)])
        out["N3_tampered_module_refused"] = {
            "returncode": r["returncode"], "stderr": r["stderr"],
            "ok": r["returncode"] == 70 and "SEALED_MODULE_HASH" in r["stderr"]}

    # N4: a module missing from the manifest must not load.
    with tempfile.TemporaryDirectory() as tmp:
        def drop(dst):
            path = dst / "PAYLOAD.sha256"
            keep = [l for l in path.read_text().splitlines()
                    if "k0_field_checker_r4.py" not in l]
            path.write_text("\n".join(keep) + "\n")
        dst = _smoke_copy(tmp, drop)
        r = _run([sys.executable, "-I", "-B", runner, "--import-smoke",
                  "--smoke-packet-dir", str(dst)])
        out["N4_unmanifested_module_refused"] = {
            "returncode": r["returncode"], "stderr": r["stderr"],
            "ok": r["returncode"] == 70
                  and "SEALED_MODULE_UNMANIFESTED" in r["stderr"]}

    # N5: the manifest itself is bound to the coordinator authorization.
    r = _run([sys.executable, "-I", "-B", runner, "--import-smoke",
              "--packet-manifest-sha256", "0" * 64])
    out["N5_manifest_binding_enforced"] = {
        "returncode": r["returncode"], "stderr": r["stderr"],
        "ok": r["returncode"] == 70 and "PACKET_MANIFEST_BINDING" in r["stderr"]}

    # N6: the smoke must itself be isolated, or it is not testing R1's shape.
    r = _run([sys.executable, "-B", runner, "--import-smoke"])
    out["N6_smoke_requires_isolated"] = {
        "returncode": r["returncode"], "stderr": r["stderr"],
        "ok": r["returncode"] == 70 and "SMOKE_NOT_ISOLATED" in r["stderr"]}

    # N7: the test-only flag cannot leak into the production path.
    r = _run([sys.executable, "-I", "-B", runner,
              "--smoke-packet-dir", str(PACKET)])
    out["N7_smoke_flag_isolated_from_production"] = {
        "returncode": r["returncode"], "stderr": r["stderr"],
        "ok": r["returncode"] == 70 and "SMOKE_FLAG_MISUSE" in r["stderr"]}

    # N8: production mode refuses a non-isolated interpreter.
    r = _run([sys.executable, "-B", runner, "--execution-root", "/tmp",
              "--run-dir", "/tmp", "--marker", "/tmp/x", "--gp", "/tmp/gp",
              "--pins", "/tmp/p", "--source-root", "/tmp",
              "--packet-manifest-sha256", "0" * 64])
    out["N8_production_requires_isolated"] = {
        "returncode": r["returncode"], "stderr": r["stderr"],
        "ok": r["returncode"] == 70 and "NOT_ISOLATED" in r["stderr"]}

    out["ok"] = all(v["ok"] for v in out.values() if isinstance(v, dict))
    return out


# --------------------------------------------------------------------------
# P9: the authority-surface controls
# --------------------------------------------------------------------------


def _authorization_base():
    return {
        "schema": SUP.AUTH_SCHEMA,
        "route": SUP.ROUTE,
        "status": "AUTHORIZED",
        "coordinator_go": True,
        "reviewer_pass": {"model": "Fable 5",
                          "report_path": "xmodel/some-review.md",
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
        "run_path": "/var/lib/jc2-k0/run-1",
    }


def _with(path, value):
    rec = _authorization_base()
    node = rec
    for key in path[:-1]:
        node = node[key]
    if value is None:
        node.pop(path[-1], None)
    else:
        node[path[-1]] = value
    return rec


AUTHORIZATION_CASES = [
    ("valid", _authorization_base(), True, None),
    ("verdict_lowercase", _with(["reviewer_pass", "verdict"], "pass"),
     False, "REVIEW_VERDICT"),
    ("verdict_trailing_space", _with(["reviewer_pass", "verdict"], "PASS "),
     False, "REVIEW_VERDICT"),
    ("verdict_titlecase", _with(["reviewer_pass", "verdict"], "Pass"),
     False, "REVIEW_VERDICT"),
    ("verdict_passed", _with(["reviewer_pass", "verdict"], "PASSED"),
     False, "REVIEW_VERDICT"),
    ("verdict_sentinel",
     _with(["reviewer_pass", "verdict"], "<MUST_BE_PASS>"),
     False, "REVIEW_VERDICT"),
    ("verdict_absent", _with(["reviewer_pass", "verdict"], None),
     False, "REVIEW_VERDICT"),
    ("verdict_true", _with(["reviewer_pass", "verdict"], True),
     False, "REVIEW_VERDICT"),
    ("model_producer_spaced", _with(["reviewer_pass", "model"], "Opus 5"),
     False, "SAME_MODEL_REVIEW"),
    ("model_producer_upper", _with(["reviewer_pass", "model"], "OPUS5"),
     False, "SAME_MODEL_REVIEW"),
    ("model_producer_hyphen", _with(["reviewer_pass", "model"], "opus-5"),
     False, "SAME_MODEL_REVIEW"),
    ("model_producer_tight", _with(["reviewer_pass", "model"], "Opus5"),
     False, "SAME_MODEL_REVIEW"),
    ("model_producer_padded",
     _with(["reviewer_pass", "model"], "  Opus  5  "),
     False, "SAME_MODEL_REVIEW"),
    ("model_producer_vendor",
     _with(["reviewer_pass", "model"], "claude-opus-5"),
     False, "SAME_MODEL_REVIEW"),
    ("model_producer_suffixed",
     _with(["reviewer_pass", "model"], "Opus 5 (max reasoning)"),
     False, "SAME_MODEL_REVIEW"),
    ("model_empty", _with(["reviewer_pass", "model"], ""),
     False, "SAME_MODEL_REVIEW"),
    ("model_absent", _with(["reviewer_pass", "model"], None),
     False, "SAME_MODEL_REVIEW"),
    ("model_grok", _with(["reviewer_pass", "model"], "Grok 4.6"), True, None),
    ("model_gpt", _with(["reviewer_pass", "model"], "GPT-5.6"), True, None),
    ("report_hash_short", _with(["reviewer_pass", "report_sha256"], "a" * 63),
     False, "NO_REVIEWER_PASS"),
    ("report_path_blank", _with(["reviewer_pass", "report_path"], "   "),
     False, "NO_REVIEWER_PASS"),
    ("go_string", _with(["coordinator_go"], "true"), False, "NO_COORDINATOR_GO"),
    ("go_absent", _with(["coordinator_go"], None), False, "AUTHORIZATION_SHAPE"),
    ("status_template", _with(["status"], "TEMPLATE_NOT_AUTHORIZED"),
     False, "AUTHORIZATION_STATUS"),
    ("route_r1", _with(["route"], "D43-K0-FIELD-CERT-R1"),
     False, "AUTHORIZATION_ROUTE"),
    ("schema_r1", _with(["schema"], "d43-k0-field-certificate-launch-auth-r1"),
     False, "AUTHORIZATION_SCHEMA"),
    ("instance_type_r6a", _with(["host", "instance_type"], "r6a.large"),
     False, "INSTANCE_TYPE"),
    ("host_label_wrong", _with(["host", "host_label"], "r6d"),
     False, "HOST_BINDING"),
    ("gp_version_wrong", _with(["host", "gp_version"], "2.15.5"),
     False, "HOST_BINDING"),
    ("gp_hash_short", _with(["gp_binary_sha256"], "b" * 10),
     False, "AUTHORIZATION_SHAPE"),
    ("manifest_hash_absent", _with(["packet_manifest_sha256"], None),
     False, "AUTHORIZATION_SHAPE"),
    ("run_path_relative", _with(["run_path"], "run-1"), False, "PATH_SHAPE"),
    ("gp_path_relative", _with(["gp_binary_path"], "gp"), False, "PATH_SHAPE"),
]


def authority_controls():
    out = {"authorization_cases": [], "ok": True}
    for name, record, should_pass, code in AUTHORIZATION_CASES:
        try:
            SUP.validate_authorization_record(record)
            got_pass, got_code = True, None
        except SUP.CustodyFault as exc:
            got_pass, got_code = False, exc.code
        ok = (got_pass == should_pass) and (code is None or got_code == code)
        out["authorization_cases"].append(
            {"case": name, "expected_pass": should_pass,
             "expected_code": code, "got_pass": got_pass,
             "got_code": got_code, "ok": ok})
        out["ok"] = out["ok"] and ok
    out["authorization_case_count"] = len(AUTHORIZATION_CASES)

    # the template that ships with the packet must NOT validate
    template = json.loads((PACKET / "authorization_template_r4.json").read_bytes())
    try:
        SUP.validate_authorization_record(template)
        template_ok, template_code = False, "TEMPLATE_VALIDATED"
    except SUP.CustodyFault as exc:
        template_ok, template_code = True, exc.code
    out["template_refused"] = {"ok": template_ok, "code": template_code}
    out["ok"] = out["ok"] and template_ok

    # artifact collision semantics: exclusive create, 0444, no overwrite
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "result.json"
        first = RUN.emit_immutable(path, b'{"a":1}')
        mode = oct(os.stat(str(path)).st_mode & 0o777)
        try:
            RUN.emit_immutable(path, b'{"a":2}')
            collided, code = False, None
        except RUN.RunnerFault as exc:
            collided, code = True, exc.code
        oversize = False
        try:
            RUN.emit_immutable(Path(tmp) / "big.json",
                               b"x" * (RUN.ARTIFACT_BYTE_CAP + 1))
        except RUN.RunnerFault as exc:
            oversize = exc.code == "ARTIFACT_TOO_LARGE"
        out["artifact_collision"] = {
            "first_sha256": first, "mode": mode, "second_refused": collided,
            "code": code, "oversize_refused": oversize,
            "ok": collided and code == "ARTIFACT_COLLISION" and mode == "0o444"
                  and oversize}
        out["ok"] = out["ok"] and out["artifact_collision"]["ok"]

    # run-directory reuse: exactly the entries the supervisor staged, nothing
    # else.  P11 drives the whole law (both directions, custody objects
    # included) against a real staged directory; this stays here as the
    # authority-surface smoke test of the same function.
    auth_sha = "a" * 64
    with tempfile.TemporaryDirectory() as tmp:
        run_dir = Path(tmp) / "run"
        run_dir.mkdir()
        (run_dir / "source").mkdir()
        (run_dir / "job_marker.json").write_text("{}")
        (run_dir / "execution_pins_live.json").write_text("{}")
        (run_dir / (RUN.CLAIM_TOKEN_PREFIX + auth_sha
                    + RUN.CLAIM_TOKEN_SUFFIX)).write_text("{}")
        (run_dir / (RUN.AUTHORIZATION_LEASE_PREFIX + auth_sha
                    + RUN.AUTHORIZATION_LEASE_SUFFIX)).write_text("{}")
        clean = RUN.check_run_dir_clean(run_dir, auth_sha)
        (run_dir / "terminal.json").write_text("{}")
        try:
            RUN.check_run_dir_clean(run_dir, auth_sha)
            reused, code = False, None
        except RUN.RunnerFault as exc:
            reused, code = True, exc.code
        out["run_dir_reuse"] = {"clean_listing": clean, "stale_refused": reused,
                                "code": code,
                                "ok": reused and code == "RUN_DIR_REUSE"
                                      and len(clean) == 5}
        out["ok"] = out["ok"] and out["run_dir_reuse"]["ok"]
    return out


# --------------------------------------------------------------------------
# P10: gate-surface controls, one per R1 defect
# --------------------------------------------------------------------------

X12_PLUS_5 = (5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1)


def gate_surface_controls(root, pins, banks):
    def statuses(**overrides):
        spec = replace(CK.Spec(label="PROBE"), **overrides)
        payload = CK.run_from_pins(spec, root, pins, banks)
        return ({g["gate"]: g["status"] for g in payload["gates"]}, payload)

    out = {"probes": [], "ok": True}

    def record(name, defect, r1_behaviour, requirement, ok, detail):
        out["probes"].append({"probe": name, "r1_defect": defect,
                              "r1_behaviour": r1_behaviour,
                              "r2_requirement": requirement,
                              "detail": detail, "ok": ok})
        out["ok"] = out["ok"] and ok

    st, _ = statuses(phi42=X12_PLUS_5)
    record("D2_absurd_phi42", "D2",
           "RANK432_MONIC_BASIS, GALOIS_STABILITY and NONABELIAN all PASSED on "
           "the absurd monic datum x^12+5",
           "RANK432_INDEPENDENCE must FAIL; RELATION_LEADING_TERMS must PASS, "
           "because freeness of rank 432 really does hold for any monic "
           "degree-12 datum and the specific Phi42 is pinned elsewhere",
           st["RANK432_INDEPENDENCE"] == "FAIL"
           and st["RELATION_LEADING_TERMS"] == "PASS"
           and st["SRC_PHI42_LITERAL"] == "FAIL"
           and st["PHI42_DISCRIMINANT"] == "FAIL",
           {k: st[k] for k in ("RANK432_INDEPENDENCE", "RELATION_LEADING_TERMS",
                               "SRC_PHI42_LITERAL", "PHI42_DISCRIMINANT",
                               "RANK432_NORMAL_FORM")})

    st, _ = statuses(sigma_images=((0, 1), (1, 1), (3, 1), (2, 1), (4, 1)))
    record("D3_broken_sigma", "D3",
           "the R1 relation loop computed sigma({}) == {} five times and could "
           "not fail",
           "GALOIS_STABILITY_FREE must FAIL on a sigma that is not a ring map "
           "of this presentation",
           st["GALOIS_STABILITY_FREE"] == "FAIL",
           {"GALOIS_STABILITY_FREE": st["GALOIS_STABILITY_FREE"]})

    base = CK.Spec()
    st, _ = statuses(frames=(base.frames[0],))
    record("D4_frames_halved", "D4",
           "dropping the 105673 frame passed all 36 R1 gates while the "
           "terminal still asserted both registered frames",
           "FRAME_RELATIONS must FAIL on a halved frame list",
           st["FRAME_RELATIONS"] == "FAIL",
           {"FRAME_RELATIONS": st["FRAME_RELATIONS"]})

    st, _ = statuses(pointbank_expected=(base.pointbank_expected[0],))
    record("D4_pointbank_halved", "D4",
           "dropping the 105673 regression passed all 36 R1 gates with no "
           "observable shadow at all",
           "POINTBANK_REGRESSION must FAIL on a halved pointbank list",
           st["POINTBANK_REGRESSION"] == "FAIL",
           {"POINTBANK_REGRESSION": st["POINTBANK_REGRESSION"]})

    st, _ = statuses(r3_exponents=(12, 156))
    record("D5_r4_exponent_duplication", "D5",
           "_character_frames hardcoded 14/154, so an r3_exponents mutation "
           "failed L1 while L2 kept certifying the true object",
           "both BASE_WELLDEFINED and the L2 character layer must see the "
           "mutated exponents",
           st["BASE_WELLDEFINED"] == "FAIL"
           and st["KUMMER_HOMS_EXHIBITED"] == "FAIL",
           {"BASE_WELLDEFINED": st["BASE_WELLDEFINED"],
            "KUMMER_HOMS_EXHIBITED": st["KUMMER_HOMS_EXHIBITED"]})

    st, payload = statuses(
        q0_terms=MB._q0_with((0, 0, 2, 1, 0), CK.Fr(-5, 7)))
    record("D1_pure_L5_mutation", "D1",
           "R1 reported unconditional_k0_theorem FALSE for a q0 perturbation "
           "that failed no L0-L4 gate, because both booleans required the "
           "single shared census",
           "the unconditional theorem must stay TRUE and only the E theorem "
           "may fall",
           payload["unconditional_k0_theorem"] is True
           and payload["e_conditional_ratio_theorem"] is False
           and not [g for g, s in st.items()
                    if s != "PASS" and g.startswith(("SRC_", "PHI", "RANK",
                                                     "RELATION", "BASE",
                                                     "KUMMER", "FIELD",
                                                     "IDEMP", "GALOIS", "NONAB",
                                                     "ETALE", "RAMIF", "FRAME",
                                                     "SPLIT", "P2_"))],
           {"unconditional_k0_theorem": payload["unconditional_k0_theorem"],
            "e_conditional_ratio_theorem":
                payload["e_conditional_ratio_theorem"],
            "failed": [g for g, s in st.items() if s != "PASS"]})

    st, payload = statuses(
        pointbank_expected=((105337, 7211, 3), (105673, 14755, 0)))
    record("D1_corroboration_only", "D1",
           "a corroboration failure fed both theorem booleans through the "
           "shared census",
           "a CORROBORATION failure must leave both theorem booleans TRUE and "
           "only all_pass may fall",
           payload["unconditional_k0_theorem"] is True
           and payload["e_conditional_ratio_theorem"] is True
           and payload["all_pass"] is False,
           {"unconditional_k0_theorem": payload["unconditional_k0_theorem"],
            "e_conditional_ratio_theorem":
                payload["e_conditional_ratio_theorem"],
            "all_pass": payload["all_pass"]})

    st, _ = statuses(class_representatives=((1, 0), (0, 1), (1, 1), (0, 0)))
    record("D10_trivial_representative", "D10",
           "the (i,j) != (0,0) need was dead code behind the witness search",
           "KUMMER_REPRESENTATIVE_CLASSES must fail with the trivial-class "
           "message",
           st["KUMMER_REPRESENTATIVE_CLASSES"] == "FAIL",
           {"KUMMER_REPRESENTATIVE_CLASSES":
                st["KUMMER_REPRESENTATIVE_CLASSES"]})

    st, _ = statuses(eps_data=(3, 1))
    record("D10_eps_datum", "D10",
           "the R1 eps line was constant-true and its message was backwards",
           "KUMMER_NORM_COROBORATION must fail on a non-unit eps",
           st["KUMMER_NORM_COROBORATION"] == "FAIL",
           {"KUMMER_NORM_COROBORATION": st["KUMMER_NORM_COROBORATION"]})

    # D12: the static-census predictor must itself be falsifiable
    text = (PACKET / "k0_field_cert_r4.gp").read_text()
    lines = text.splitlines()
    idx = next(i for i, l in enumerate(lines)
               if l.startswith('chk("L0 declared rank'))
    deleted = gp_static_census("\n".join(lines[:idx] + lines[idx + 1:]))
    duplicated = gp_static_census("\n".join(lines[:idx] + [lines[idx]] + lines[idx:]))
    commented = gp_static_census(
        "\n".join(lines[:idx] + ["\\\\ a comment with ( unbalanced parens"]
                  + lines[idx:]))
    record("D12_static_census_falsifiable", "D12",
           "the R1 predictor combined nested loops by max, and counted "
           "parentheses on raw lines",
           "deleting or duplicating a gate line must break the prediction, and "
           "a parenthesised comment must not move it",
           (not deleted["agrees"]) and (not duplicated["agrees"])
           and commented["agrees"],
           {"deleted": deleted["predicted_gate_count"],
            "duplicated": duplicated["predicted_gate_count"],
            "with_paren_comment": commented["predicted_gate_count"],
            "declared": deleted["declared_nexpect"]})
    return out


# --------------------------------------------------------------------------
# P11: the custody boundary, executed, plus its hostile source mutations
# --------------------------------------------------------------------------

# Each entry patches exactly one anchor in the sealed supervisor (or runner)
# source, loads the patched module, and requires the named controls to stop
# holding.  A control nobody can break is a control that proves nothing; this
# is the custody-side counterpart of the mathematics battery, and it is the
# test discipline the R1 import fault and the R2 lease fault both escaped.
CUSTODY_MUTATIONS = [
    ("CM1_custodian_uid_not_root", "supervisor", "static",
     "custodian_uid=0,", "custodian_uid=os.geteuid(),",
     ["production_policy_pins_uid_zero"],
     "production builds its policy with the running uid instead of root"),
    ("CM2_parent_mode_gate_removed", "supervisor", "boundary",
     '    if st.st_mode & (stat.S_IWGRP | stat.S_IWOTH):\n'
     '        fault("PATH_MODE"',
     '    if False:\n'
     '        fault("PATH_MODE"',
     ["parent_group_writable"],
     "a group-writable sealed parent is accepted"),
    ("CM3_claim_owner_gate_removed", "supervisor", "boundary",
     '    if st.st_uid != policy.custodian_uid:\n        fault("CLAIM_OWNER"',
     '    if False:\n        fault("CLAIM_OWNER"',
     ["claim_service_written_refused"],
     "a claim token the service could have written is accepted"),
    ("CM4_lease_not_exclusive", "supervisor", "boundary",
     'fd = os.open(str(lease), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o444)',
     'fd = os.open(str(lease), os.O_WRONLY | os.O_CREAT, 0o444)',
     ["one_time_claim", "restart_after_clean_claim_refused"],
     "the authorization can be presented twice"),
    ("CM5_burn_before_verification", "supervisor", "boundary",
     '    custody = verify_custody_preconditions(policy, record, auth_sha)\n'
     '    custody["authorization_lease"] = claim_authorization_lease(\n'
     '        custody["run_dir"], auth_sha)',
     '    lease = claim_authorization_lease(Path(record["run_path"]), auth_sha)\n'
     '    custody = verify_custody_preconditions(policy, record, auth_sha)\n'
     '    custody["authorization_lease"] = lease',
     ["no_burn_before_verification"],
     "a failed precondition consumes the authorization"),
    ("CM6_lease_oserror_uncaught", "supervisor", "boundary",
     '    except OSError as exc:\n'
     '        # R2 let this escape as a bare PermissionError traceback',
     '    except InterruptedError as exc:\n'
     '        # R2 let this escape as a bare PermissionError traceback',
     ["lease_unwritable"],
     "an unwritable run directory raises a traceback, as it did in R2"),
    ("CM7_run_dir_mode_gate_removed", "supervisor", "boundary",
     '    if stat.S_IMODE(st.st_mode) != policy.run_dir_mode:',
     '    if False:',
     ["run_dir_wrong_mode"],
     "a group-readable run directory is accepted"),
    ("CM8_run_dir_owner_gate_removed", "supervisor", "boundary",
     '    if st.st_uid != policy.service_uid:',
     '    if False:',
     ["run_dir_wrong_owner"],
     "a run directory owned by somebody else is accepted"),
    ("CM9_claim_run_path_binding_dropped", "supervisor", "boundary",
     '            "run_path": str(Path(run_dir)),\n'
     '            "service_user": policy.service_user}',
     '            "service_user": policy.service_user}',
     ["claim_wrong_run_path"],
     "a claim minted for another run directory is accepted"),
    ("CM10_pristine_gate_removed", "supervisor", "boundary",
     '    extra = sorted(present - allowed)',
     '    extra = []',
     ["crashed_run_refused"],
     "a crashed run is relaunched in place"),
    ("CM11_runner_source_not_expected", "runner", "runner",
     'PRE_RUN_FILES = frozenset({"job_marker.json", "execution_pins_live.json",\n'
     '                           "source"})',
     'PRE_RUN_FILES = frozenset({"job_marker.json", "execution_pins_live.json"})',
     ["clean_launch_accepted"],
     "the R2 law: every real launch dies on RUN_DIR_REUSE"),
    ("CM12_runner_completeness_dropped", "runner", "runner",
     '    missing = sorted((REQUIRED_PRE_RUN_FILES | custody) - present)',
     '    missing = []',
     ["missing_lease_refused"],
     "a run that never took its authorization lease is accepted; an unstaged "
     "source tree still fails, because the source directory is checked twice "
     "on purpose"),
    ("CM13_runner_both_completeness_checks_dropped", "runner", "runner",
     '    missing = sorted((REQUIRED_PRE_RUN_FILES | custody) - present)\n'
     '    if missing:\n'
     '        fault("RUN_DIR_INCOMPLETE",\n'
     '              "the run directory is missing %s; the supervisor stages the "\n'
     '              "source tree and takes the authorization lease before the "\n'
     '              "runner starts" % missing)\n'
     '    if not (Path(run_dir) / "source").is_dir():\n'
     '        fault("RUN_DIR_INCOMPLETE", "<run dir>/source is not a directory")',
     '    missing = []',
     ["unstaged_source_refused", "missing_lease_refused"],
     "both completeness checks gone: a run that staged nothing is accepted"),
    # ---- R4: the choreography (the R3 review's REPAIR-1) ----------------
    ("CM14_unit_mints_twice", "unit", "unit",
     'ExecStartPre=+<ABSOLUTE_BASH> --noprofile --norc \\\n  <ABSOLUTE_PACKET_DIR>/mint_claim_r4.sh \\\n  <ABSOLUTE_RUN_DIRECTORY> \\\n  <ABSOLUTE_AUTHORIZATION_JSON> \\\n  jc2k0',
     'ExecStartPre=+<ABSOLUTE_BASH> --noprofile --norc \\\n  <ABSOLUTE_PACKET_DIR>/mint_claim_r4.sh \\\n  <ABSOLUTE_RUN_DIRECTORY> \\\n  <ABSOLUTE_AUTHORIZATION_JSON> \\\n  jc2k0' + "\n" + 'ExecStartPre=+<ABSOLUTE_BASH> --noprofile --norc \\\n  <ABSOLUTE_PACKET_DIR>/mint_claim_r4.sh \\\n  <ABSOLUTE_RUN_DIRECTORY> \\\n  <ABSOLUTE_AUTHORIZATION_JSON> \\\n  jc2k0',
     ["unit_mints_exactly_once", "mint_is_the_first_exec_start_pre",
      "dry_run_is_the_second_exec_start_pre"],
     "the unit mints twice: the second mint dies MINT_ALREADY_SPENT"),
    ("CM15_template_restores_external_mint_order", "template", "template",
     '" e. systemctl start jc2-d43-k0-field-cert-r4.service.  This is the only",',
     '" e. only then start the unit.",',
     ["no_forbidden_phrase", "no_missing_required_phrase"],
     "**the R3 defect**: the coordinator record tells a coordinator to mint "
     "by hand and then start the unit, which mints again"),
    ("CM16_dry_run_runs_as_root", "unit", "unit",
     "ExecStartPre=<ABSOLUTE_PYTHON3> -I -B",
     "ExecStartPre=+<ABSOLUTE_PYTHON3> -I -B",
     ["dry_run_carries_no_prefix", "dry_run_runs_as_service_identity",
      "only_mint_and_retire_are_privileged"],
     "the dry run runs as root, so it proves nothing about the service "
     "identity that ExecStart will actually have"),
    ("CM17_dry_run_before_mint", "unit", "unit",
     '# 1. root: mint the one-shot claim.  A second start of this unit dies here\n#    with MINT_ALREADY_SPENT and never reaches the dry run or the supervisor.\n#    This is the ONLY mint; the coordinator never runs mint_claim_r4.sh.\nExecStartPre=+<ABSOLUTE_BASH> --noprofile --norc \\\n  <ABSOLUTE_PACKET_DIR>/mint_claim_r4.sh \\\n  <ABSOLUTE_RUN_DIRECTORY> \\\n  <ABSOLUTE_AUTHORIZATION_JSON> \\\n  jc2k0\n\n# 2. jc2k0, in this unit\'s sandbox: the on-host dry run.  No "+", so systemd\n#    applies User=/Group= and every sandbox setting above, exactly as for\n#    ExecStart= below.  It calls aws_supervisor_r4.verify_custody_preconditions\n#    against the tree step 1 just minted and stops there: no lease, no writes,\n#    no directory creation.  A non-zero exit aborts the start, so ExecStart=\n#    never runs against a tree the service identity could not verify.\nExecStartPre=<ABSOLUTE_PYTHON3> -I -B \\\n  <ABSOLUTE_PACKET_DIR>/custody_selftest_r4.py \\\n  --on-host-dry-run \\\n  --run-path <ABSOLUTE_RUN_DIRECTORY> \\\n  --authorization <ABSOLUTE_AUTHORIZATION_JSON> \\\n  --out -\n\n',
     '# 2. jc2k0, in this unit\'s sandbox: the on-host dry run.  No "+", so systemd\n#    applies User=/Group= and every sandbox setting above, exactly as for\n#    ExecStart= below.  It calls aws_supervisor_r4.verify_custody_preconditions\n#    against the tree step 1 just minted and stops there: no lease, no writes,\n#    no directory creation.  A non-zero exit aborts the start, so ExecStart=\n#    never runs against a tree the service identity could not verify.\nExecStartPre=<ABSOLUTE_PYTHON3> -I -B \\\n  <ABSOLUTE_PACKET_DIR>/custody_selftest_r4.py \\\n  --on-host-dry-run \\\n  --run-path <ABSOLUTE_RUN_DIRECTORY> \\\n  --authorization <ABSOLUTE_AUTHORIZATION_JSON> \\\n  --out -\n\n# 1. root: mint the one-shot claim.  A second start of this unit dies here\n#    with MINT_ALREADY_SPENT and never reaches the dry run or the supervisor.\n#    This is the ONLY mint; the coordinator never runs mint_claim_r4.sh.\nExecStartPre=+<ABSOLUTE_BASH> --noprofile --norc \\\n  <ABSOLUTE_PACKET_DIR>/mint_claim_r4.sh \\\n  <ABSOLUTE_RUN_DIRECTORY> \\\n  <ABSOLUTE_AUTHORIZATION_JSON> \\\n  jc2k0\n\n',
     ["mint_is_the_first_exec_start_pre",
      "dry_run_is_the_second_exec_start_pre", "dry_run_after_mint"],
     "the dry run precedes the mint, so it always dies RUN_DIR_ABSENT"),
    ("CM18_dry_run_failure_tolerated", "unit", "unit",
     "ExecStartPre=<ABSOLUTE_PYTHON3> -I -B",
     "ExecStartPre=-<ABSOLUTE_PYTHON3> -I -B",
     ["no_failure_tolerant_exec_prefixes", "dry_run_carries_no_prefix"],
     'the "-" prefix makes a refused dry run non-fatal and ExecStart runs '
     "anyway"),
    ("CM19_dry_run_takes_the_lease", "selftest", "selftest",
     "    custody = sup.verify_custody_preconditions(policy, record, auth_sha)",
     "    custody = sup.establish_custody(policy, record, auth_sha)",
     ["dry_run_creates_nothing", "dry_run_then_launch_still_succeeds"],
     "the dry run burns the authorization it was supposed to check"),
    ("CM20_dry_run_skips_the_identity_check", "selftest", "selftest",
     "    policy = sup.production_policy() if policy is None else policy\n"
     "    sup.require_service_identity(policy)",
     "    policy = sup.production_policy() if policy is None else policy",
     ["dry_run_requires_service_identity", "dry_run_checks_identity"],
     "the dry run no longer proves it ran as the service user"),
    ("CM21_dry_run_cli_exits_zero", "selftest", "selftest",
     "        rc_on_refusal = 70",
     "        rc_on_refusal = 0",
     ["dry_run_cli_fails_closed"],
     "a refused dry run exits 0, so systemd runs ExecStart anyway"),
    ("CM22_verify_preconditions_writes", "supervisor", "callgraph",
     '    present = require_run_dir_pristine(run_dir, auth_sha)\n'
     '    return {"sealed_parent": str(parent), "run_dir": str(run_dir),',
     '    present = require_run_dir_pristine(run_dir, auth_sha)\n'
     '    (Path(run_dir) / "dry-run-touched").touch()\n'
     '    return {"sealed_parent": str(parent), "run_dir": str(run_dir),',
     ["reaches_no_write_primitive"],
     "the dry run's own call graph writes, so it is no longer read-only"),
    ("CM23_template_restores_free_refusal_wording", "template", "template",
     '"never takes; the digest is already gone.",',
     '"never takes, so a failed precondition never consumes this record.",',
     ["no_forbidden_phrase"],
     "the coordinator record claims again that a refusal after the mint is "
     "free"),
    ("CM24_unit_splits_the_run_directory_sentinel", "unit", "unit",
     "  <ABSOLUTE_RUN_DIRECTORY> \\\n  <ABSOLUTE_AUTHORIZATION_JSON> \\\n  jc2k0",
     "  <ABSOLUTE_SEALED_PARENT_DIRECTORY> \\\n  <RUN_DIRECTORY_NAME> \\\n"
     "  <ABSOLUTE_AUTHORIZATION_JSON> \\\n  jc2k0",
     ["mint_arguments", "no_split_run_directory_sentinels"],
     "R3's two-sentinel mint call returns: nothing checks that the parent and "
     "the name compose to the directory the dry run and ReadWritePaths name, "
     "and the script now refuses it as a usage error"),
]


def _load_mutated(name, source_name, text, tmp):
    """Write a patched copy of a sealed module and import it by path."""
    target = Path(tmp) / (source_name + ".py")
    target.write_text(text)
    return _load_by_path("%s__%s" % (source_name, name), str(target))


# every file wording_controls reads, so a template mutation can be scanned in
# a temporary directory without touching the sealed packet
WORDING_FILES = ("authorization_template_r4.json",
                 "systemd_unit_template_r4.service", "custody_selftest_r4.py",
                 "README.md", "preregistration_r4.json", "mint_claim_r4.sh",
                 "REVIEW_REQUEST.md")
MUTATION_SOURCE = {
    "supervisor": "aws_supervisor_r4.py",
    "runner": "runner_r4.py",
    "unit": "systemd_unit_template_r4.service",
    "template": "authorization_template_r4.json",
    "selftest": "custody_selftest_r4.py",
}


def _stage(tmp, names, patched=None):
    """Copy sealed members into ``tmp``, overwriting one with patched text."""
    for name in names:
        shutil.copyfile(str(PACKET / name), str(Path(tmp) / name))
    if patched is not None:
        (Path(tmp) / patched[0]).write_text(patched[1])
    return Path(tmp)


def custody_controls():
    """P11: run the controls, then break each one on purpose."""
    out = {}
    out["baseline"] = CS.run_controls(SUP, PACKET, run=RUN)
    entries = []
    for (name, module, kind, old, new, controls, why) in CUSTODY_MUTATIONS:
        base_text = (PACKET / MUTATION_SOURCE[module]).read_text()
        hits = base_text.count(old)
        entry = {"mutation": name, "module": module, "kind": kind,
                 "anchor_hits": hits, "controls": controls, "effect": why}
        if hits != 1:
            entry.update({"verdict": "FAIL",
                          "reason": "anchor is not unique in the sealed source"})
            entries.append(entry)
            continue
        patched = base_text.replace(old, new)
        with tempfile.TemporaryDirectory() as tmp:
            if kind == "static":
                (Path(tmp) / "aws_supervisor_r4.py").write_text(patched)
                report = {"production_policy":
                          CS.production_policy_controls(SUP, Path(tmp))}
                observed = {c: report["production_policy"].get(c)
                            for c in controls}
                broke = all(observed[c] is False for c in controls)
            elif kind == "boundary":
                sup_mut = _load_mutated(name, "aws_supervisor_r4", patched, tmp)
                root = Path(tmp) / "fixtures"
                root.mkdir()
                report = CS.boundary_controls(sup_mut, root)
                observed = {c: report.get(c, {}).get("ok") for c in controls}
                broke = all(observed[c] is False for c in controls)
            elif kind == "runner":
                run_mut = _load_mutated(name, "runner_r4", patched, tmp)
                root = Path(tmp) / "fixtures"
                root.mkdir()
                report = CS.runner_pre_run_controls(SUP, run_mut, root)
                observed = {c: report.get(c, {}).get("ok") for c in controls}
                broke = all(observed[c] is False for c in controls)
            elif kind == "unit":
                # the shipped unit, parsed as ordered systemd directives
                staged = _stage(tmp, ["systemd_unit_template_r4.service"],
                                ("systemd_unit_template_r4.service", patched))
                report = CS.choreography_controls(SUP, staged)
                observed = {c: report.get(c) for c in controls}
                broke = all(observed[c] is False for c in controls)
            elif kind == "template":
                # the coordinator record and every other file the wording scan
                # reads, so the scan sees a complete packet
                staged = _stage(tmp, WORDING_FILES,
                                (MUTATION_SOURCE[module], patched))
                report = CS.wording_controls(staged)
                observed = {c: report.get(c) for c in controls}
                broke = all(observed[c] is False for c in controls)
            elif kind == "callgraph":
                staged = _stage(tmp, ["aws_supervisor_r4.py",
                                      "custody_selftest_r4.py"],
                                (MUTATION_SOURCE[module], patched))
                report = CS.call_graph_controls(SUP, staged)
                observed = {c: report.get(c) for c in controls}
                broke = all(observed[c] is False for c in controls)
            else:                                            # kind == selftest
                # the SEALED controls drive the MUTATED entry point, so the
                # mutation cannot also weaken the control that catches it
                staged = _stage(tmp, ["aws_supervisor_r4.py",
                                      "custody_selftest_r4.py"],
                                ("custody_selftest_r4.py", patched))
                cs_mut = _load_by_path("custody_selftest__%s" % name,
                                       str(staged / "custody_selftest_r4.py"))
                root = staged / "fixtures"
                root.mkdir()
                report = CS.dry_run_controls(SUP, root, cs=cs_mut,
                                             cli_dir=staged)
                report.update(CS.call_graph_controls(SUP, staged))
                observed = {c: (report.get(c, {}).get("ok")
                                if isinstance(report.get(c), dict)
                                else report.get(c)) for c in controls}
                broke = all(observed[c] is False for c in controls)
        entry["observed"] = observed
        entry["verdict"] = "PASS" if broke else "FAIL"
        entries.append(entry)
    out["mutations"] = entries
    out["mutation_count"] = len(entries)
    out["failed_mutations"] = [e["mutation"] for e in entries
                               if e["verdict"] != "PASS"]
    out["ok"] = out["baseline"]["ok"] and not out["failed_mutations"]
    return out


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", required=True, help="repository root")
    ap.add_argument("--out", default="-")
    args = ap.parse_args(argv)
    root = Path(args.root)
    pins = json.loads((PACKET / "execution_pins_r4.json").read_bytes())

    report = {"schema": SCHEMA, "packet": PACKET.name,
              "route": pins["route"],
              "gp_executed": False,
              "gp_not_executed_reason":
                  "no PARI/GP on the producer host; the GP layer is reviewed "
                  "statically here and executed only on the registered AWS "
                  "host by runner_r4.py.  No claim is made that the GP "
                  "syntax or API has run.",
              "aws_executed": False,
              "aws_not_executed_reason":
                  "status is R4_SOURCE_READY_AWS_NOT_AUTHORIZED"}

    manifest = PACKET / "PAYLOAD.sha256"
    p1 = {"present": manifest.is_file()}
    if p1["present"]:
        bad, count = [], 0
        for line in manifest.read_text().splitlines():
            if not line.strip():
                continue
            count += 1
            sha, rel = line.split(None, 1)
            path = root / rel.strip()
            if not path.is_file() or sha256_path(path) != sha:
                bad.append(rel.strip())
        p1["members"] = count
        p1["mismatched"] = bad
        p1["ok"] = not bad
    else:
        p1["ok"] = False
    report["P1_packet_manifest"] = p1

    archive = PACKET / "SOURCE_ARCHIVE.tar"
    seal = PACKET / "SOURCE_ARCHIVE.sha256"
    report["P2_source_archive"] = (replay_archive(archive, seal)
                                   if archive.is_file() and seal.is_file()
                                   else {"ok": False, "reason": "not sealed yet"})

    gp_text = (PACKET / "k0_field_cert_r4.gp").read_text()
    census = gp_static_census(gp_text)
    census["hygiene"] = gp_hygiene(gp_text)
    census["labels"] = gp_label_audit(gp_text)
    census["agrees"] = (census["agrees"] and census["hygiene"]["ok"]
                        and census["labels"]["ok"])
    report["P3_gp_static_census"] = census

    banks = CK.read_pointbanks(
        [(int(p), str(root / rel), sha) for p, rel, sha in pins["pointbanks"]])
    result = CK.run_from_pins(CK.Spec(label="PREFLIGHT"), root, pins, banks)
    report["P4_python_engine"] = {
        "gate_count": result["gate_count"],
        "failed": [g["gate"] for g in result["gates"] if g["status"] != "PASS"],
        "unconditional_k0_theorem": result["unconditional_k0_theorem"],
        "e_conditional_ratio_theorem": result["e_conditional_ratio_theorem"],
        "corroboration_ok": result["corroboration_ok"],
        "execution_integrity": result["execution_integrity"],
        "theorem_inputs_disjoint":
            not (set(result["theorem_inputs"]["unconditional"])
                 & set(result["theorem_inputs"]["conditional"]))
            and not (set(result["theorem_inputs"]["unconditional"])
                     & set(result["theorem_inputs"]["corroboration"]))
            and not (set(result["theorem_inputs"]["conditional"])
                     & set(result["theorem_inputs"]["corroboration"])),
        "ok": result["all_pass"]}
    report["P4_python_engine"]["ok"] = (
        report["P4_python_engine"]["ok"]
        and report["P4_python_engine"]["theorem_inputs_disjoint"])

    battery = MB.run_battery(root, pins, banks)
    report["P5_mutation_battery"] = {
        "must_fail": battery["must_fail_count"],
        "must_survive": battery["must_survive_count"],
        "theorem_separation_controls": battery["theorem_separation_controls"],
        "theorem_separation_census": battery["theorem_separation_census"],
        "failed_entries": [e["mutation"] for e in battery["mutations"]
                           if e["verdict"] != "PASS"],
        "gate_unit_tests": {k: v["verdict"]
                            for k, v in battery["gate_unit_tests"].items()},
        "battery_sha256": battery["battery_sha256"],
        "ok": battery["battery_pass"]}

    report["P6_pinned_hashes"] = {
        "census_sha256": result["census_sha256"],
        "observable_sha256": result["observable_sha256"],
        "census_matches_pin":
            result["census_sha256"] == pins["expected_census_sha256"],
        "observable_matches_pin":
            result["observable_sha256"] == pins["expected_observable_sha256"],
        "gp_script_sha256_matches_pin":
            sha256_path(PACKET / "k0_field_cert_r4.gp")
            == pins["gp_script_sha256"],
        "observable_count_matches_gp":
            len(result["observables"])
            == census["predicted_observable_count"],
        "gate_count_matches_gp":
            census["declared_nexpect"] == pins["gp_gate_count"],
        "observable_count_matches_pin":
            len(result["observables"]) == pins["shared_observable_count"],
        "runner_constants_match":
            RUN.GP_CENSUS_EXPECTED == pins["gp_gate_count"]
            and RUN.GP_OBSERVABLE_COUNT == pins["shared_observable_count"],
        "e_layer_observables_match":
            sorted(CK.E_LAYER_OBSERVABLES) == sorted(pins["e_layer_observables"]),
    }
    # every boolean in the block is required; no key-name filter to get wrong
    report["P6_pinned_hashes"]["ok"] = all(
        v for v in report["P6_pinned_hashes"].values() if isinstance(v, bool))

    emission = {"components": result["components"],
                "idempotents": result["idempotents"],
                "component_count": result["component_count"]}
    scans = {}
    for name, blob, refusal in (
            ("result.json", RUN.canonical(result), False),
            ("mutations.json", RUN.canonical(battery), True),
            # proxy for gp_stdout.txt: every label the GP engine can print
            ("gp_stdout.txt(proxy)", gp_text.encode("ascii"), False)):
        try:
            RUN._forbidden_language_scan(name, blob, refusal_record=refusal)
            scans[name] = "CLEAN"
        except RUN.RunnerFault as exc:
            scans[name] = "%s %s" % (exc.code, exc)
    emission["forbidden_language_scan"] = scans
    emission["ok"] = (emission["components"] == ["K0"]
                      and emission["idempotents"] == [0, 1]
                      and emission["component_count"] == 1
                      and all(v == "CLEAN" for v in scans.values()))
    report["P7_emission_policy"] = emission

    report["P8_isolated_import_controls"] = isolated_import_controls()
    report["P9_authority_controls"] = authority_controls()
    report["P10_gate_surface_controls"] = gate_surface_controls(root, pins, banks)
    report["P11_custody_boundary"] = custody_controls()

    report["preflight_pass"] = all(
        report[k].get("ok") for k in
        ("P1_packet_manifest", "P2_source_archive", "P4_python_engine",
         "P5_mutation_battery", "P6_pinned_hashes", "P7_emission_policy",
         "P8_isolated_import_controls", "P9_authority_controls",
         "P10_gate_surface_controls", "P11_custody_boundary")) \
        and report["P3_gp_static_census"]["agrees"]

    blob = CK.canonical(report)
    if args.out == "-":
        sys.stdout.write(json.dumps(report, sort_keys=True, indent=1) + "\n")
    else:
        Path(args.out).write_bytes(blob)
    return 0 if report["preflight_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
