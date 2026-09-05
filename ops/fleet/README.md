# jc2 compute fleet (self-sufficient, math-hq-driven)

Ephemeral CAS workers launched from **math-hq** with the **jc2-fleet** key. No
`claude-cli` key and no IAM instance profile are needed (the role denies SSM,
EC2 Instance Connect, and PassRole; this path avoids all three).

## Stack installed per worker (worker-userdata.sh)
Singular, msolve (apt/universe), python-flint, sympy, and the campaign PyPI
tools **qqideal** and **msolveio** (latest). Provisioning is fail-gated: a worker
writes `~/PROVISION_DONE` only if `import sympy, qqideal, msolveio` succeeds;
`~/PROVISION_VERSIONS` records the versions.

## Networking
Workers get a **public IP** (needed for apt/pip outbound) but are reached from
math-hq over their **private IP** (same subnet/SG). SSH: `~/.ssh/jc2-fleet`.

## Usage
```
ops/fleet/fleet.sh launch 4 c7i.4xlarge   # 4 x86 workers (8 real cores each)
ops/fleet/fleet.sh wait all               # block until provisioned; prints versions
ops/fleet/fleet.sh ips                     # list workers
ops/fleet/fleet.sh push <IP> box/job/ '~/job/'
ops/fleet/fleet.sh run  <IP> 'cd ~/job && Singular -q run.sing > out.txt'
ops/fleet/fleet.sh pull <IP> '~/job/out.txt' ./results/
ops/fleet/fleet.sh term-all               # terminate every jc2-worker when idle
```

## Instance types (subagent research 2026-09-05)
- **Default `c7i.4xlarge`** (x86, 16 vCPU / **8 physical cores** / 32 GB). Run
  ONE Singular job per physical core (~8), leave hyperthreads idle for CAS.
- **Big-memory fallback `r7i.4xlarge`** (128 GB), `r7i.8xlarge` (256 GB) for the
  largest standard bases.
- **Cost lever `c7g.4xlarge`** (Graviton/arm64): **16 real cores**, ~half $/core.
  Ubuntu ships arm64 singular/msolve; validate once, then set `DEFAULT_TYPE=c7g.4xlarge`.
- Quota headroom ~984 On-Demand Standard vCPUs (~61 4xlarge workers). Spot is a
  separate pool, ~55-70% cheaper, ideal for this restartable batch workload.

## Stop-idle discipline
Workers are ephemeral. `term-all` when a batch finishes. Never leave idle workers.
