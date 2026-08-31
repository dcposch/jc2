# Fleet access + job rules (for ALL agents: Fable subagents, Sol, Grok)

## HARD RULE (strengthened 2026-08-24 after local swap incident)
Run **all heavy campaign computation on AWS**, never on the local Mac. This
includes Singular/msolve/other CAS jobs, Lean builds, and long or potentially
multi-GB Python exact-algebra replays/enumerations. The Mac is reserved for
editing, orchestration, hashing, process/status checks, and genuinely short,
low-memory validation. If a job's memory or duration is uncertain, ship it to
AWS. Do not use the former `<8 GB` local-Python allowance: several concurrent
"small" jobs can still exhaust the Mac's 32 GB and thrash swap.
New route-specific heavy runners must fail closed unless `uname -s` is
`Linux`, require a nonempty registered job tag, and record `hostname` before
starting the computational payload.  `ops/aws_exact_lane.sh` enforces Linux,
an Amazon EC2 DMI identity, and a nonempty registered lane tag for clients
that use the shared wrapper.

## Inventory
- **box01** (AWS x8i.16xlarge, 64 vCPU / 1 TiB): instance
  i-029d0899cdb7c1ed1 (profile `personal`), 100 GiB gp3 root;
  ubuntu@54.175.21.169, key ~/.ssh/claude-cli.pem. Runs the deg<=150 farm
  lanes (`~/jc72108`, `farm.log`/`farm2.log`). Current us-east-1 on-demand
  price checked 2026-08-24: ~$7.00/h; verify current pricing before a cost
  decision. Do not stack big-memory jobs without checking live RSS, and do
  not stop it until all active/checkpointed campaign processes are identified.
- **Box02** (AWS x2idn.32xlarge, 128 vCPU / 2 TiB, 3.8 TB local NVMe):
  instance i-010201a5da47795c4 (profile `personal`), 150 GiB gp3 root. IP CHANGES on stop/start —
  resolve with:
    aws ec2 describe-instances --instance-ids i-010201a5da47795c4 \
      --profile personal --query \
      'Reservations[0].Instances[0].PublicIpAddress' --output text
  (current IP also cached in /tmp/box02_ip). Start/stop with
  aws ec2 start-instances / stop-instances. ~$13/h — STOP IT when its
  queue drains (coordinator's call; don't stop it while lanes run).
  After start: `sudo ldconfig` once before msolve.
  Job dir: ~/res32 (screens + stuck7), ~/jc72108 (older Q2 work).
  Current 2026-08-25 boot IP: `34.203.207.55`.
- **Box03** (AWS r6i.16xlarge, 64 vCPU / 512 GiB): instance
  i-0ece0b9a3b4a7512f (profile `personal`), 200 GiB gp3 root, launched 2026-08-14 for the
  3 stuck7 farm big-cores idle since the Box02 cull. Same SG/subnet/key
  as Box02 (claude-ssh / subnet-948915c9 / claude-cli), us-east-1a,
  IP CHANGES on stop/start — resolve like Box02
  (cached in /tmp/box03_ip; currently 54.167.215.189). ~$4.03/h —
  STOP IT when the stuck7 lanes finish. msolve from Ubuntu apt.
  Job dir: ~/stuck7 (out/ + lanes.log).
  Current 2026-08-25 boot IP: `98.80.65.144` (the older IP in the preceding
  historical sentence is stale).
- **r6a** (AWS r6i.4xlarge, 16 vCPU / 128 GiB): instance
  `i-02cb2b4a379ffcc64`, current IP `34.229.212.201`.
- **r6b** (AWS r6i.4xlarge, 16 vCPU / 128 GiB): instance
  `i-0f089e64c378f5da3`, current IP `54.224.45.13`.
- **r6c** (AWS r6i.4xlarge, 16 vCPU / 128 GiB): instance
  `i-040b7a1c2ed72d4cc`, current IP `18.209.172.161`.
- **r6d** (AWS r6i.8xlarge, 32 vCPU / 256 GiB): instance
  `i-07eeaf8ba6f0bc419`, current IP `54.84.212.87`.  Its TD6 environment is
  `/home/ubuntu/venvs/td6` (Python 3.12 / python-flint 0.9.0).

The seven campaign instances total **336 vCPUs when all are running**. A
separate user-owned 16-vCPU formalization instance also counts against the
512-vCPU account quota and is outside this campaign's inspection/control
scope. Running-state headroom is therefore dynamic; use `sh ops/status.sh`,
which queries only the seven named campaign instance IDs and explicitly
excludes the separate instance. At the 2026-08-31T04:44Z control-plane audit,
Box02/Box03 were stopped, box01 plus `r6a`--`r6d` were running, so campaign
capacity was 144 vCPUs running; box01 alone was busy (`build_tails43.py`, one
fully used vCPU and about 132 GiB RSS), with checkpoint
`ckpt43/jet_g_04_GB42.pkl` banked and the final `GB21` orbit active, while all
four `r6*` workers were idle.
Together with the documented 16-vCPU excluded instance, current account
running use was 160 vCPUs and immediate quota headroom was 352 vCPUs. Restarting
both stopped campaign boxes would consume another 192 vCPUs, restoring the
all-in 352-vCPU allocation and leaving 160 vCPUs of headroom. Do not describe
AWS as idle while the box01 checkpoint builder remains live, and do not confuse
stopped restart capacity with current quota use.

Do not exceed the account total or inspect, stop, retag, or repurpose the
separate instance. The coordinator may add smaller workers of at most 1 TiB
RAM, or replace an audited idle instance, when independent lanes benefit from
job-level parallelism; stop/replace only after every live process and output
has been identified and preserved. The four `r6*` nodes were resized/restarted
on 2026-08-28. Their public IPs change on stop/start; resolve from the instance
IDs before use. Do not stop or repurpose one until its exact live processes and
output custody are audited.
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
- The minimal process-control recipe below is for legacy screening only; it is
  not evidence-grade because it omits the full metadata ledger. Launch every
  such lane orphan-safe and self-recording:
    nohup sh -c "timeout 43200 msolve -g 2 -t 8 -f X.ms -o out/X.out; \
      echo \"LANE X: rc=\$? size=\$(wc -c < out/X.out | tr -d ' ') \
      \$(date +%H:%M)\" >> lanes.log" >/dev/null 2>&1 &
- For evidentiary work, use a route-specific hardened wrapper that enforces the
  characteristic-zero caveat and records every field in the metadata rule
  below. Do not promote output from the minimal recipe.
- 0-byte .out = still running or timeout (check lanes.log rc), NEVER
  read it as a verdict (R6 §19.2 hygiene).
- Ship work as files via scp (scp-script pattern), not long inline ssh
  commands.
- Threads: -t 8 on Box02 (128 cores), -t 2..4 on box01.
- Caps: 43200 s default; raise only with a reason.

## Historical job snapshot (2026-08-13; never live state)

This section is incident provenance only. The newest `LIVE STATE` block in
`notes.md` and direct process checks determine current jobs.
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

## Characteristic-zero `-g` caveat (2026-08-23)
In msolve 0.10.1, a characteristic-zero `-g` run whose first machine-prime
basis is `[1]` may take a unit-basis short circuit before CRT/rational
reconstruction even though the output header repeats characteristic 0.
Therefore:
- a char-0-header `[1]` is `FIRST-PRIME-EMPTY` trace evidence, never a Q
  verdict;
- a successful char-0 non-unit output has continued through rational
  reconstruction and is a Q-level nonemptiness result within engine trust;
- finitely many modular `[1]` results do not certify characteristic-zero
  emptiness without an effective prime bound or a reconstructed exact
  cofactor;
- theorem-tier emptiness requires an independently verified identity
  `1 = sum h_i f_i` (or an equivalent exact rational certificate);
- every hardened probe lane sets and records `--random-seed` (default 0,
  overridable through `MSOLVE_SEED`), plus input hash, input characteristic,
  msolve version, host, UTC start, and, when verbose output exposes it, the
  initial prime.

## Telemetry
- ops/lane_eta.py (INTERNAL TOOLING, UNREVIEWED): msolve -v2 lane telemetry
  reader — `python3 ops/lane_eta.py --status lane.v2log` (phase / F4 rounds /
  matrix trajectory / honest NO-ETA fallback), `--compare log1 log2`
  (cross-prime divergence check), `--gates` (parse-completeness over
  ops/telemetry_samples/). -v2 goes to STDERR: launch lanes with
  `msolve -v 2 ... 2> lane.v2log`. Read-only — safe on live lanes.

## Local CAS etiquette (superseded 2026-08-24)
Do not run campaign CAS locally. Ship even exploratory Singular/Maple/etc.
jobs to AWS. If a trivial local parser/version check is ever unavoidable, it
must be batch-only with browsers disabled (`ESINGULAR_BROWSER=cat`,
`BROWSER=cat`; never interactive `help`).
