# Fleet access + job rules (for ALL agents: Fable subagents, Sol, Grok)

## HARD RULE (2026-08-13 incident)
NEVER run msolve (or any multi-GB solver) on the local Mac — it has 32 GB
and thrashes. ALL solver jobs go to the AWS/GCP fleet. Local python for
exact small linear algebra (sympy, <8 GB) is fine.

## Inventory
- **box01** (AWS, farm): ubuntu@54.175.21.169, key ~/.ssh/claude-cli.pem.
  Runs the deg<=150 farm lanes (~/jc72108, farm.log/farm2.log). Moderate
  size — do not stack big cores here.
- **Box02** (AWS x2idn.32xlarge, 128 vCPU / 2 TB): instance
  i-010201a5da47795c4 (profile `personal`). IP CHANGES on stop/start —
  resolve with:
    aws ec2 describe-instances --instance-ids i-010201a5da47795c4 \
      --profile personal --query \
      'Reservations[0].Instances[0].PublicIpAddress' --output text
  (current IP also cached in /tmp/box02_ip). Start/stop with
  aws ec2 start-instances / stop-instances. ~$13/h — STOP IT when its
  queue drains (coordinator's call; don't stop it while lanes run).
  After start: `sudo ldconfig` once before msolve.
  Job dir: ~/res32 (screens + stuck7), ~/jc72108 (older Q2 work).
- **Box03** (AWS r6i.16xlarge, 64 vCPU / 512 GB): instance
  i-0ece0b9a3b4a7512f (profile `personal`), launched 2026-08-14 for the
  3 stuck7 farm big-cores idle since the Box02 cull. Same SG/subnet/key
  as Box02 (claude-ssh / subnet-948915c9 / claude-cli), us-east-1a,
  200 GB gp3 root. IP CHANGES on stop/start — resolve like Box02
  (cached in /tmp/box03_ip; currently 54.167.215.189). ~$4.03/h —
  STOP IT when the stuck7 lanes finish. msolve from Ubuntu apt.
  Job dir: ~/stuck7 (out/ + lanes.log).
- **ultramem** (GCP): RETIRED 2026-08-16 per DC (AWS-only policy).
  Instance stopped/terminated; two disks remain in dclanker (jc-b 200G,
  ultramem-1 100G, ~$15-30/mo) holding old run outputs — deletion is
  DC's call, not the loop's.

## SG auto-update (2026-08-20)
DC's local public IP drifts (three ssh-breaking incidents 2026-08-19,
latest 149.22.81.x -> 149.88.22.138). Fix: `ops/sg_autoupdate.sh` keeps
the current IP authorized for port 22 on the fleet security group
sg-09ffa8932558f0a79 (profile `personal`).
- Usage: `ops/sg_autoupdate.sh` — no args. Idempotent, safe every tick,
  exactly one status line: "SG: current" (no change), "SG: added
  <ip>/32 (pruned ...)", or "SG: ip-lookup failed (no change)". Exit
  nonzero ONLY on AWS CLI errors.
- CONSERVATIVE PRUNE POLICY: after adding a new IP it removes ONLY
  stale /32 rules inside the two known personal ranges 149.22.81.* and
  149.88.22.*. It NEVER touches 69.181.195.82/32 or any rule outside
  those ranges — other rules may be intentional. If DC's ISP moves to a
  new range, add it to PRUNE_RE in the script (old-range stragglers are
  pruned on the next drift, not before).
- STANDING INSTRUCTION (all agents): on ANY ssh timeout to a fleet box,
  run `ops/sg_autoupdate.sh` once BEFORE diagnosing further — IP drift
  is the most common cause. If it prints "SG: added ...", retry the ssh;
  only then escalate to instance/network debugging.

## Run conventions (remote)
- Launch every lane orphan-safe and self-recording:
    nohup sh -c "timeout 43200 msolve -g 2 -t 8 -f X.ms -o out/X.out; \
      echo \"LANE X: rc=\$? size=\$(wc -c < out/X.out | tr -d ' ') \
      \$(date +%H:%M)\" >> lanes.log" >/dev/null 2>&1 &
- 0-byte .out = still running or timeout (check lanes.log rc), NEVER
  read it as a verdict (R6 §19.2 hygiene).
- Ship work as files via scp (scp-script pattern), not long inline ssh
  commands.
- Threads: -t 8 on Box02 (128 cores), -t 2..4 on box01.
- Caps: 43200 s default; raise only with a reason.

## Current standing jobs (2026-08-13)
- Box02 ~/res32: 6 nolog screens (DECISIVE for residue-A), 4 plain/ctl0
  screens, 3 stuck7 farm cores; lanes.log self-records.
- Box02 ~/jc72108 (2026-08-19 restart): 3 ROW22R-B2 decisive reduced
  systems (directionb_row22red p105337/p105673/p200257), msolve 0.10.1,
  -t 32, -v2 telemetry, 48h caps expire 2026-08-21 06:46Z; lanes.log
  self-records. IP 35.175.192.141 this boot (/tmp/box02_ip).
- box01: farm lanes (13 EMPTYs banked so far).
- ultramem: sat23 (r1_23sat).
- Box03 ~/stuck7 (2026-08-14): 3 stuck7 big-cores (12_33 c10.RED,
  6_15 c1.RED, 6_15 c2.q), 48h cap, lanes.log self-records.

## Version caveat (2026-08-14)
Box03 runs apt msolve 0.6.5 (not the campaign-standard 0.10.1). Any
verdict produced there is SCREENING-TIER until re-confirmed on a
0.10.1 box (Box02 post-drain) — record the version in every AUDIT
citation of a Box03 result. Rationale: our hazard ledger is calibrated
to 0.10.1; 0.6.5 may lack fixes or carry different bugs.

## Telemetry
- ops/lane_eta.py (INTERNAL TOOLING, UNREVIEWED): msolve -v2 lane telemetry
  reader — `python3 ops/lane_eta.py --status lane.v2log` (phase / F4 rounds /
  matrix trajectory / honest NO-ETA fallback), `--compare log1 log2`
  (cross-prime divergence check), `--gates` (parse-completeness over
  ops/telemetry_samples/). -v2 goes to STDERR: launch lanes with
  `msolve -v 2 ... 2> lane.v2log`. Read-only — safe on live lanes.

## Local CAS etiquette (2026-08-17)
Agent lanes exploring Singular/Maple/etc. on the local Mac MUST run
batch mode with browsers disabled (Singular: `Singular -q < script`,
never interactive `help`; or export ESINGULAR_BROWSER=cat BROWSER=cat).
Interactive help shells out to `open` and spams DC's Safari with
file:// doc pages. Include this rule in any prompt that authorizes
local CAS use.
