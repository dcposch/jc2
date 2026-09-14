# Operator-authorized idle fleet retirement

2026-09-10 13:39 UTC. DC explicitly directed: keep only instances actively
being used and terminate the rest; prior idle-worker policy locks cleared.
This is infrastructure cleanup, not scientific execution or a JC2 result.

The current jc2fleet=1 inventory contains nine workers: five running and four
stopped. None has an active assigned scientific job in the current campaign
state. Check exact running process identities and instance-store mounts before
termination. The coordinator host and separate formalization infrastructure
are outside this target set and will not be inspected or controlled.

Before terminating any instance, preserve its exact attached EBS root volume
by setting and independently verifying DeleteOnTermination=false. This also
preserves the sole-source vol-0eb6450d18ffa89f1. No volume deletion is authorized
by this cleanup; retained volumes may be attached to future workers. Check
the x2idn worker for mounted instance-store data, which EBS retention alone
cannot preserve. If scientific processes or unpreserved instance-store data
are found, resolve them before terminating that exact target.

Exact instance/root-volume pairs from the current AWS read-only inventory:

- i-054caf7aff0720142 / vol-09639c2b3913406aa / running
- i-04fcf19f9dfa5e32e / vol-02551baa5db44faf2 / running
- i-0e91c47db37aa6598 / vol-09d2ca3957d4a5d76 / running
- i-0cd415bd9d3abed39 / vol-00bde9f1f49cb1e16 / running
- i-025410e620b1d65c9 / vol-0be96430c433dfbe2 / running
- i-07e1212591a6acae9 / vol-09c6e3133f3442e56 / stopped
- i-0da0cebfc97c9fd54 / vol-0eb6450d18ffa89f1 / stopped, sole-source data
- i-08d2a40f272ee9fa2 / vol-0574e0fa5aed1f5e3 / stopped
- i-0e5c65e66b8dc4dfc / vol-01155d0dba3e3db78 / stopped

All nine currently report one attached EBS mapping, /dev/sda1, initially with
DeleteOnTermination=true. Do not use term-all or infer targets from stale IPs.
Freeze actual inspection, preservation, termination and completion evidence.
