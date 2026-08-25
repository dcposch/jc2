# Box02 basis-formula solver cutoff custody

Date: 2026-08-25  
Host: Box02 (`34.203.207.55`)  
Remote job: `/home/ubuntu/jobs/as_b9_common_cubic_kuranishi_basis_20260825T192400Z_box02`  
Scope: method-only solver control for the frozen strict-D12 B9 Kuranishi map

The exact 111-original-row formula was emitted successfully:

```text
basis111.smt2 SHA-256 = ed5e5629103c50e526ae268f0052140d49c66dff4dc21f71c3dd0e5a77a10db8
full parent SMT SHA-256 = 108cfdaae0c897ab66518e18d5e38d0969a1f8f936eeb488fd9144e4fbfe0f4c
relation certificate SHA-256 = 45b40fd0540e060869a25683c0f5d852a0a24c39e4d04ff17d60af568453d578
```

Z3 produced no verdict by the preregistered 20:00Z method-only cutoff.
Immediately before stopping, the exact process group was:

```text
wrapper PID/PGID 218572
python child PID 218575
elapsed 36:07
python RSS 58,011,548 KiB
python VSZ 62,596,344 KiB
```

At `20260825T195942Z`, after resolving and validating the recorded PID,
PGID, and command, the registered group received `TERM`.  The wrapper and
`/usr/bin/time` exited; one zero-RSS `[python3]` residual remained briefly
under the same PGID and received a second `TERM`.  No `KILL` was used.  The
final exact-PGID snapshot is empty and a separate post-stop search found no
related solver worker.

Both solver stdout and stderr are empty (SHA-256 `e3b0c442...`); there is no
SAT, UNSAT, UNKNOWN, timeout, or mathematical evidence.  The files in
`AWS_BOX02/` are the harvested remote stop metadata, exact pre-stop hashes,
emitter custody, and empty solver logs.  This supplement does not mutate the
previously frozen producer/case and does not revive strict-D12 as a live
counterexample lane.

