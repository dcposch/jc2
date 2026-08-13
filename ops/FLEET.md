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
- **ultramem** (GCP, project dclanker, zone us-central1-a, instance
  ultramem-1): access ONLY via
    gcloud compute ssh ultramem-1 --project dclanker --zone us-central1-a
  (plain ssh key not authorized; sshd sometimes starves under load —
  retry later, don't fight it). Runs sat23.

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
