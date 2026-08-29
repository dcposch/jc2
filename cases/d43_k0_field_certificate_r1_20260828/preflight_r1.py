#!/usr/bin/env python3
"""Bounded local preflight for the D43 `K0` field certificate, R1.

Runs everything that can honestly be run without AWS and without PARI:

  P1  packet manifest replay (PAYLOAD.sha256)
  P2  sealed source archive replay, byte for byte
  P3  static census audit of the PARI/GP script: the number of gate lines it
      will print is derived from the file and compared against its own
      ``nexpect``, so a deleted or added line is caught before the host runs
  P4  the stdlib-Python engine, all gates
  P5  the hostile mutation battery, including the two MUST_SURVIVE entries
  P6  the census and observable hashes pinned in execution_pins_r1.json
  P7  the emission policy: no artifact may name a component other than K0

It does NOT run PARI/GP (there is no gp on the producer host) and it does not
touch AWS.  Both facts are reported, not hidden.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tarfile
from pathlib import Path

import k0_field_checker_r1 as CK
import k0_mutations_r1 as MB

PACKET = Path(__file__).resolve().parent
SCHEMA = "d43-k0-field-certificate-preflight-r1"


def sha256_path(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def gp_static_census(gp_path):
    """Predict the GP gate count without running gp.

    ``chk(`` sites outside comments are counted; sites inside a ``for`` block
    are multiplied by that block's trip count.  The three loops are declared
    here explicitly so a reviewer can check the arithmetic by eye.
    """
    text = Path(gp_path).read_text()
    lines = text.splitlines()
    declared = int(re.search(r"nexpect\s*=\s*(\d+)", text).group(1))
    sites = [i for i, line in enumerate(lines)
             if re.search(r"(?<!\w)chk\(", line)
             and not line.lstrip().startswith("\\\\")
             and not line.startswith("chk(lab")]
    loops = []
    for i, line in enumerate(lines):
        m = re.match(r"for \((\w+) = 1, #?(\w+|\d+),", line)
        if m and not line.lstrip().startswith("\\\\"):
            depth, end = 0, None
            for j in range(i, len(lines)):
                depth += lines[j].count("(") - lines[j].count(")")
                if j > i and depth <= 0:
                    end = j
                    break
            trips = {"CERTPRIMES": 2, "SILENT": 2, "2": 2}.get(m.group(2))
            if trips and end is not None:
                loops.append((i, end, trips))
    total = 0
    breakdown = []
    for s in sites:
        trips = 1
        for (lo, hi, t) in loops:
            if lo < s <= hi:
                trips = max(trips, t)
        total += trips
        breakdown.append({"line": s + 1, "trips": trips})
    obs_sites = [i for i, line in enumerate(lines)
                 if re.search(r"(?<!\w)obs\(", line)
                 and not line.lstrip().startswith("\\\\")
                 and not line.startswith("obs(k, v)")]
    obs_total = 0
    for s in obs_sites:
        trips = 1
        for (lo, hi, t) in loops:
            if lo < s <= hi:
                trips = max(trips, t)
        obs_total += trips
    return {"declared_nexpect": declared, "predicted_gate_count": total,
            "static_sites": len(sites), "loops": len(loops),
            "predicted_observable_count": obs_total,
            "agrees": total == declared}


def replay_archive(archive, seal):
    """Replay every sealed member out of the tar, plus the tar's own hash.

    The first line of SOURCE_ARCHIVE.sha256 is the archive's own digest keyed
    on its own path; it is not a member and is checked separately.
    """
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
        members = tar.getmembers()
        got = {}
        for m in members:
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


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", required=True, help="repository root")
    ap.add_argument("--out", default="-")
    args = ap.parse_args(argv)
    root = Path(args.root)
    pins = json.loads((PACKET / "execution_pins_r1.json").read_bytes())

    report = {"schema": SCHEMA, "packet": PACKET.name,
              "gp_executed": False,
              "gp_not_executed_reason":
                  "no PARI/GP on the producer host; the GP layer is reviewed "
                  "statically here and executed only on the registered AWS "
                  "host by runner_r1.py",
              "aws_executed": False,
              "aws_not_executed_reason":
                  "status is R1_SOURCE_READY_AWS_NOT_AUTHORIZED"}

    manifest = PACKET / "PAYLOAD.sha256"
    p1 = {"present": manifest.is_file()}
    if p1["present"]:
        bad = []
        for line in manifest.read_text().splitlines():
            if not line.strip():
                continue
            sha, rel = line.split(None, 1)
            path = root / rel.strip()
            if not path.is_file() or sha256_path(path) != sha:
                bad.append(rel.strip())
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

    report["P3_gp_static_census"] = gp_static_census(PACKET / "k0_field_cert_r1.gp")

    banks = CK.read_pointbanks(
        [(int(p), str(root / rel), sha) for p, rel, sha in pins["pointbanks"]])
    result = CK.run(CK.Spec(label="PREFLIGHT"), root, pins["sources"],
                    pins["emitter_rel"], pins["rows_rel"], banks)
    report["P4_python_engine"] = {
        "gate_count": result["gate_count"],
        "failed": [g["gate"] for g in result["gates"] if g["status"] != "PASS"],
        "unconditional_k0_theorem": result["unconditional_k0_theorem"],
        "e_conditional_ratio_theorem": result["e_conditional_ratio_theorem"],
        "corroboration_ok": result["corroboration_ok"],
        "ok": result["all_pass"]}

    battery = MB.run_battery(root, pins, banks)
    report["P5_mutation_battery"] = {
        "must_fail": battery["must_fail_count"],
        "must_survive": battery["must_survive_count"],
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
            sha256_path(PACKET / "k0_field_cert_r1.gp")
            == pins["gp_script_sha256"],
        "observable_count_matches_gp":
            len(result["observables"])
            == report["P3_gp_static_census"]["predicted_observable_count"],
    }
    report["P6_pinned_hashes"]["ok"] = all(
        v for k, v in report["P6_pinned_hashes"].items() if k.endswith("pin")
        or k.endswith("gp"))

    emission = {"components": result["components"],
                "idempotents": result["idempotents"],
                "component_count": result["component_count"]}
    emission["ok"] = (emission["components"] == ["K0"]
                      and emission["idempotents"] == [0, 1]
                      and emission["component_count"] == 1)
    report["P7_emission_policy"] = emission

    report["preflight_pass"] = all(
        report[k].get("ok") for k in
        ("P1_packet_manifest", "P2_source_archive", "P4_python_engine",
         "P5_mutation_battery", "P6_pinned_hashes", "P7_emission_policy")) \
        and report["P3_gp_static_census"]["agrees"]

    blob = CK.canonical(report)
    if args.out == "-":
        sys.stdout.write(json.dumps(report, sort_keys=True, indent=1) + "\n")
    else:
        Path(args.out).write_bytes(blob)
    return 0 if report["preflight_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
