#!/usr/bin/env python3
"""Pull fleet certificates, write tally + hard-row list. Does not terminate."""
from __future__ import annotations
import json, subprocess, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/home/ubuntu/jc2")
DEST = ROOT / "box" / "operative-sweep-20260905"
FLEET_KEY = Path.home() / ".ssh" / "jc2-fleet"
SSH_OPTS = (
    "-i", str(FLEET_KEY),
    "-o", "StrictHostKeyChecking=no",
    "-o", "BatchMode=yes",
    "-o", "ConnectTimeout=12",
)
sys.path.insert(0, str(ROOT / "box" / "lib"))
import census_sweep as CS  # noqa: E402

TIERS = ("live_us1", "us_ge2", "ctop_killed")


def pull():
    pairs = []
    for line in (DEST / "job-map.txt").read_text().splitlines():
        cid, ip = line.split()
        pairs.append((cid, ip))
        target = DEST / "classes" / cid
        target.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            ["rsync", "-az", "-e", "ssh %s" % " ".join(SSH_OPTS),
             "ubuntu@%s:/home/ubuntu/jc2/box/operative-sweep-20260905/classes/%s/"
             % (ip, cid), "%s/" % target],
            check=False,
        )
        subprocess.run(
            ["rsync", "-az", "-e", "ssh %s" % " ".join(SSH_OPTS),
             "ubuntu@%s:~/operative-sweep-%s.log" % (ip, cid),
             str(DEST / "classes" / cid / "worker.log")],
            check=False,
        )
    return pairs


def load_cert(cid: str) -> dict | None:
    p = DEST / "classes" / cid / "certificate.json"
    if not p.is_file():
        return None
    return json.loads(p.read_text())


def main() -> int:
    pairs = pull()
    inventory = json.loads((DEST / "inventory.json").read_text())
    swept = {}
    for cid, ip in pairs:
        cert = load_cert(cid)
        swept[cid] = dict(ip=ip, certificate=cert)
        print("PULLED", cid, "verdict", (cert or {}).get("class_verdict"),
              "nunk", (cert or {}).get("n_unknowns"),
              "eq", ((cert or {}).get("union") or {}).get("equations")
                    or ((cert or {}).get("extract") or {}).get("declared_equations")
                    or ((cert or {}).get("extract_union") or {}).get("declared_equations"),
              "msolve", ((cert or {}).get("msolve_screen") or {}).get("status"),
              "wall", (cert or {}).get("wall_seconds"))

    hard = []
    tally = {t: dict(classes=0, rows=0, dead=0, open_compute=0, open_split=0,
                     uneg=0, swept=0, timeout=0) for t in TIERS}
    for tier in TIERS:
        for cls in inventory["classes_by_tier"][tier]:
            tally[tier]["classes"] += 1
            tally[tier]["rows"] += cls["fibre_size"]
            cid = cls["class_id"]
            nunk = cls["nunk"] if cls["nunk"] < 10 ** 8 else None
            sc = (cls.get("counts") or {}).get("nunk_source_complete")
            kind = cls["kind"]
            leaves = cls.get("split_survivor_count") or 0
            uneg = bool(cls.get("n_uneg"))
            cert = load_cert(cid)
            if cert and cert.get("class_verdict") == "DEAD":
                tally[tier]["dead"] += 1
                continue
            if uneg:
                reason = "U-NEGATIVE (Def 5.1(1); no honest chart)"
                tally[tier]["uneg"] += 1
                bucket = "U-NEGATIVE"
            elif kind in ("split", "mixed"):
                reason = "OPEN-split leaves=%d nunk=%s" % (leaves, nunk)
                tally[tier]["open_split"] += 1
                if nunk and nunk > 100:
                    tally[tier]["open_compute"] += 1
                    reason += "; OPEN-compute nunk>100"
                bucket = "OPEN-split"
            elif cert and cert.get("class_verdict") in ("TIMEOUT", "OPEN"):
                eqs = ((cert.get("union") or {}).get("equations")
                       or (cert.get("extract_union") or {}).get("declared_equations")
                       or (cert.get("extract") or {}).get("declared_equations"))
                wall = cert.get("wall_seconds")
                reason = "OPEN-compute nunk=%s eqs=%s wall=%ss verdict=%s" % (
                    cert.get("n_unknowns") or nunk, eqs, wall,
                    cert.get("class_verdict"))
                tally[tier]["open_compute"] += 1
                tally[tier]["swept"] += 1
                if cert.get("class_verdict") == "TIMEOUT":
                    tally[tier]["timeout"] += 1
                bucket = "OPEN-compute"
            elif cls.get("engine") == "k4ray_pin_lower_band" and (sc or 0) > 100:
                reason = "OPEN-compute source-complete nunk=%s (k4ray 36-var engine not transported)" % sc
                tally[tier]["open_compute"] += 1
                bucket = "OPEN-compute"
            else:
                reason = "OPEN-compute nunk=%s" % nunk
                tally[tier]["open_compute"] += 1
                bucket = "OPEN-compute"
            hard.append(dict(
                class_id=cid, tier=tier, nunk=nunk, nunk_source_complete=sc,
                kind=kind, engine=cls.get("engine"), leaves=leaves,
                uneg=uneg, reason=reason, bucket=bucket,
                window=cls.get("window") or [],
            ))

    payload = dict(
        schema="operative-sweep-tally-v1",
        per_tier=tally,
        swept_jobs={cid: {k: v for k, v in rec.items() if k != "certificate"}
                    | dict(class_verdict=(rec["certificate"] or {}).get("class_verdict"),
                           n_unknowns=(rec["certificate"] or {}).get("n_unknowns"),
                           exact_q=(rec["certificate"] or {}).get("exact_q"),
                           msolve=((rec["certificate"] or {}).get("msolve_screen") or {}).get("status"),
                           wall=(rec["certificate"] or {}).get("wall_seconds"),
                           jacobian_identically_zero=(rec["certificate"] or {}).get("jacobian_identically_zero"))
                    for cid, rec in swept.items()},
        n_hard_rows=len(hard),
        n_dead=sum(tally[t]["dead"] for t in TIERS),
    )
    CS.atomic_json(DEST / "tally.json", payload)
    with (DEST / "hard-rows.jsonl").open("w") as fh:
        for row in hard:
            fh.write(json.dumps(row, sort_keys=True) + "\n")
    print("TALLY", json.dumps(payload, indent=2, default=str))
    print("hard_rows", len(hard))
    print("by bucket", Counter(r["bucket"] for r in hard))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
