Drivers for `xmodel/rigid-congruence-grok46-20260903.md`.

- `repro/moh_skeleton_full.py`, `full_tree_partition.py`: byte copies of the charged frozen inputs (see SHA256SUMS).
- `rigid_congruence.py`: fail-closed screens, rigid ∩ screen, D=108/112/120 congruence dump, post-screen u_s / anchor-zero. Writes `results.json`, `run.log`.
- `construct_ray.py`: (d,e)-fixed linear extensions of D=108 seeds + K=16 comparison. Writes `ray-construction.json`, `ray.log`.
- `ray-B-verified.json`: six driver-checked members of the (d,e)=(2,3) ray.

Run: `python3 -u rigid_congruence.py && python3 -u construct_ray.py`.
