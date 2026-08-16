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
