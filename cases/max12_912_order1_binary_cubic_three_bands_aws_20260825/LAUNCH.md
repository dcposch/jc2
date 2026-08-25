# AWS launch custody

Both hosts passed `SOURCE.sha256`, `bash -n`, AWS/Linux platform identity, and
AWS-side Python bytecode compilation before launch.

## r6d / exact `std`

- host: `ip-172-30-0-45` (`100.26.198.153`);
- tag: `/home/ubuntu/jobs/max12_912_order1_cubic_three_bands_v1_r6d_20260825T1812Z`;
- registered environment tag:
  `max12_912_order1_cubic_three_bands_v1_r6d_20260825T1812Z`;
- PIDs at launch: triple `149219`, double `149220`, squarefree `149221`;
- cap per lane: 64 GiB virtual address, 7200 seconds per compiler/CAS stage.

## Box02 / exact `slimgb`

- host: `ip-172-30-0-186` (`34.203.207.55`);
- tag: `/home/ubuntu/jobs/max12_912_order1_cubic_three_bands_v1_box02_20260825T1812Z`;
- registered environment tag:
  `max12_912_order1_cubic_three_bands_v1_box02_20260825T1812Z`;
- PIDs at launch: triple `207182`, double `207183`, squarefree `207184`;
- cap per lane: 64 GiB virtual address, 7200 seconds per compiler/CAS stage.

The algorithm differs across hosts, while the exact compiler/source is pinned
identically.  No local Mac computation was run.

