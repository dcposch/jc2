# AWS registration: V21 filtered-dual local-nonmembership corollary

Registered UTC: 2026-08-27T12:08:55Z

```text
host_alias=Box01
public_host=54.175.21.169
expected_private_hostname=ip-172-30-0-237
tag=max12_812_order2_u2_62_k00_filtered_dual_local_nonmembership_v21_20260827T120855Z_box01
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_filtered_dual_local_nonmembership_v21_20260827T120855Z_box01
field=Q
wall_cap_seconds=1800
virtual_memory_cap_kib=67108864
cores=1
source_freeze_manifest_sha256=97e5721a21a169a3123bd843c59ea1241126a4b0a221e2f28a89a313481069ae
input_flat_manifest_sha256=38c6dd45b888ec04a5c0b9bdd4b93625a1df491b4e4f63851f5546cb1d7d465f
source_tree_mode=read_only
input_tree_mode=read_only
live_monolithic_v17q=preserved_as_independent_crosscheck
```

The source and all 31 exact input artifacts passed their SHA-256 manifests
before launch.  This lane uses one Box01 core alongside the one-core V17-Q
cross-check; at launch the host had more than 790 GiB available and no swap.

R0 failed closed as recorded in `FAILURE_R0.md`.  The bounded R1 repair was
registered at `2026-08-27T12:13:23Z` with unchanged host, field, input bytes,
one-core allocation, 64-GiB memory cap, and 1800-second wall cap:

```text
tag=max12_812_order2_u2_62_k00_filtered_dual_local_nonmembership_v21r1_20260827T121323Z_box01
remote_job=/home/ubuntu/jobs/max12_812_order2_u2_62_k00_filtered_dual_local_nonmembership_v21r1_20260827T121323Z_box01
r1_source_freeze_manifest_sha256=4c35362b7223566317ca346bd261fb13023fbb3d8a48aef2908dd00d1a168026
r1_verifier_sha256=fd97d0b80b48bd46afd45a21a29a50f18592a68aac9047ad94d9abfb438ad875
r1_preregistration_sha256=137fdc18c349a549949e90c3d515b5e08e01d9f69a6be5f8efbbf97b78175d7d
```
