# Metadata-only comparison over the charged snapshot. Reads JSON metadata,
# hashes bytes, compares strings/decimals. Never opens exact/retained/fixture
# bodies beyond hashing; never imports or executes any charged source.
import json, hashlib, os, sys
D = "/tmp/jc2-lane.aAujJ6/inputs"
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()
def J(name):
    with open(os.path.join(D, name), "r", encoding="utf-8") as f:
        return json.load(f)
reg = J("dispatch.registration.json")
batch = J("batch.PASS.json")
pre = J("preflight.PASS.json")
fp = J("argv-fingerprints.json")
ops = ["gate-disabled","gate-wronghost","gate-argv","gate-cap","gate-missing-input","gate-valid","dummy-descendant","transform","full-check","semantic-controls"]
prof = {"gate-disabled":"probe","gate-wronghost":"probe","gate-argv":"probe","gate-cap":"probe","gate-missing-input":"probe","gate-valid":"probe","dummy-descendant":"dummy","transform":"transform","full-check":"check","semantic-controls":"controls"}
print("REG enabled", reg.get("enabled"), "agg", reg.get("aggregate_wall_seconds"), "fsize", reg.get("file_size_limit_bytes"), "math", reg.get("mathematical_deadline_utc"), "task", reg.get("task_deadline_utc"), "excl", reg.get("exclusive_no_concurrent_authority_writer"))
print("REG keys", sorted(reg.keys()))
for k, v in reg["file_sha256"].items():
    b = os.path.basename(k)
    local = os.path.join(D, b)
    print("REGPIN", b, "match" if os.path.exists(local) and sha(local) == v else ("ABSENT-LOCAL" if not os.path.exists(local) else "MISMATCH"), v[:12])
names = [r["name"] for r in batch["records"]]
print("BATCH order", names == ops, names)
print("PRE order", [r["name"] for r in pre["records"]] == ops[:7])
print("batch first_math", batch["first_math_epoch"], "end", batch["end_epoch"], "status", batch["status"])
for r in batch["records"]:
    n = r["name"]
    a = J(n + ".authority.json"); t = J(n + ".telemetry.json"); d = J(n + ".dispatch.json")
    pr = reg["profiles"][prof[n]]
    prec = [x for x in pre["records"] if x["name"] == n]
    row = {
      "n": n,
      "disp==batchrec": d == r,
      "pre==batchrec": (prec[0] == r) if prec else "n/a",
      "auth_sha": sha(os.path.join(D, n + ".authority.json")) == r["authority_sha256"] == d["authority_sha256"],
      "tele_sha": sha(os.path.join(D, n + ".telemetry.json")) == r["telemetry_sha256"] == d["telemetry_sha256"],
      "caps_auth_vs_prof": (int(a["caps"]["wall_seconds"]), int(a["caps"]["cpu_seconds"]), int(a["caps"]["rss_bytes"])) == (pr["wall_seconds"], pr["cpu_seconds"], pr["rss_bytes"]),
      "caps_tele_vs_prof": (t["caps"]["wall_seconds"], t["caps"]["cpu_seconds"], t["caps"]["rss_bytes"]) == (float(pr["wall_seconds"]), pr["cpu_seconds"], pr["rss_bytes"]),
      "enabled": a.get("enabled"), "op": a.get("operation"),
      "host": (a.get("hostname"), a.get("instance_id"), a.get("job_tag")),
      "argv_fp": hashlib.sha256((json.dumps(a["child_argv"], separators=(",",":")) + "\n").encode()).hexdigest() == t["argv_sha256"],
      "argv_fp_alt": hashlib.sha256(json.dumps(a["child_argv"], separators=(",",":")).encode()).hexdigest() == t["argv_sha256"],
      "argv_count": t["argv_count"] == len(a["child_argv"]),
      "parent_caps": [a["parent_argv"][a["parent_argv"].index(f)+1] for f in ("--wall-seconds","--cpu-seconds","--rss-bytes") if f in a["parent_argv"]],
      "parent_tail_is_child": a["parent_argv"][-len(a["child_argv"]):] == a["child_argv"],
      "parent_has_sep": "--" in a["parent_argv"],
      "pid=pgid": t.get("pid") == t.get("pgid"), "pid": t.get("pid"),
      "status": t.get("status"), "resource": t.get("resource"), "runner_exit": t.get("runner_exit_code"), "child_rc": t.get("child_returncode"),
      "rss_obs": t.get("max_observed_group_rss_bytes"),
      "start_id": t.get("start_identity"),
      "term": t.get("termination"),
      "stdout_sha_ok": t["stdout"]["sha256"] == sha(os.path.join(D, n + ".stdout")) and t["stdout"]["bytes"] == os.path.getsize(os.path.join(D, n + ".stdout")),
      "stderr_sha_ok": t["stderr"]["sha256"] == sha(os.path.join(D, n + ".stderr")) and t["stderr"]["bytes"] == os.path.getsize(os.path.join(D, n + ".stderr")),
      "ns": r["namespace"], "caller_ppid_pgid": r["caller_stat"].split()[3:6],
      "returned<cutoff": r["returned_epoch"] < r["hard_cutoff_epoch"], "cutoff": r["hard_cutoff_epoch"], "rc": r["returncode"], "margin": r["admission_margin_seconds"],
      "auth_file_pins": all(os.path.exists(os.path.join(D, os.path.basename(k))) and sha(os.path.join(D, os.path.basename(k))) == v for k, v in a["file_sha256"].items() if os.path.basename(k) != "python3"),
      "auth_pin_count": len(a["file_sha256"]),
      "auth_missing_local": [os.path.basename(k) for k in a["file_sha256"] if not os.path.exists(os.path.join(D, os.path.basename(k)))],
      "fp_json": fp.get(n) if isinstance(fp, dict) else None,
      "sentinel": os.path.exists(os.path.join(D, n + ".sentinel")),
    }
    print("OP", json.dumps(row, default=str))
print("FP file", json.dumps(fp)[:1500])
import datetime
print("cutoff utc", datetime.datetime.fromtimestamp(1788977640.0, datetime.timezone.utc).isoformat(), "first_math utc", datetime.datetime.fromtimestamp(batch["first_math_epoch"], datetime.timezone.utc).isoformat(), "end utc", datetime.datetime.fromtimestamp(batch["end_epoch"], datetime.timezone.utc).isoformat())
# remote manifest
lines = [l.split() for l in open(os.path.join(D, "remote-prepull.sha256")).read().splitlines() if l.strip()]
ok = bad = absent = 0
for h, p in lines:
    b = os.path.basename(p)
    lp = os.path.join(D, b)
    if not os.path.exists(lp): absent += 1; print("MANIFEST-ABSENT", p)
    elif sha(lp) == h: ok += 1
    else: bad += 1; print("MANIFEST-MISMATCH", p)
print("MANIFEST lines", len(lines), "ok", ok, "bad", bad, "absent", absent, "sample path", lines[0][1])
cu = J("custody.json")
print("CUSTODY keys", sorted(cu.keys()), "owned", cu.get("owned_count"), "inputs", cu.get("input_count"), "frozen", cu.get("frozen_at_utc"))
own = {os.path.basename(e["path"]): e["sha256"] for e in cu.get("owned", [])}
miss = [b for b in os.listdir(D) if b not in own]
mm = [b for b in own if os.path.exists(os.path.join(D, b)) and sha(os.path.join(D, b)) != own[b]]
print("CUSTODY owned basenames", len(own), "charged-not-in-owned", miss, "owned-mismatch", mm)
for e in cu.get("inputs", []):
    b = os.path.basename(e.get("path", ""))
    lp = os.path.join(D, b)
    print("CUSTODY-INPUT", e.get("path"), "match" if os.path.exists(lp) and sha(lp) == e.get("sha256") else ("absent-local" if not os.path.exists(lp) else "MISMATCH"))
