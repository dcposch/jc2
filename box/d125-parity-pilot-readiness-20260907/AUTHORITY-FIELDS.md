# Future authorities: schema notes only, no GREEN

Control files have exact paths engineering/authorize.authority.json and engineering/rss.authority.json. Required common fields are:

- schema `jc2.d125-parity-engineering-authority/v1`;
- engineering_control_only=true; control exactly authorize or rss; mode=slice;
- root_green=true ONLY AFTER fresh root engineering GREEN, and construction_only=true solely for the unchanged no-solver authorize interface;
- job: fresh nonempty registered control ID; boot_id: freshly observed exact boot;
- registration_sha256: SHA256 of the sealed prospective REGISTRATION.md, verified against the worker copy;
- symmetry_gate_accepted=true, symmetry_gate_sha256=`3940ba00aca8033bd8206250dc007881b9b50113061dc85588e06d1ccbe7c47d`;
- symmetry_sha256=`9bed554644b1bd3c881ba4e289ea0950601ed6141677a45152577442fd477b12`;
- source_sha256=`b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac`;
- code_sha256: exact map of all six host_control.PINS entries plus host_control.py itself; no unchecked substitutions;
- caps: exact host_control.CAPS map; expires_unix: shared control absolute deadline, no more than10 seconds ahead when validated.

These files are distinct from production root/authority.json. The production schema is jc2.d125-parity-construction-authority/v1, with mode=slice, root-issued construction GREEN, the same exact source/symmetry/math-gate/registration/charged-code pins and fresh boot/job, and the300-second/4GiB caps in REGISTRATION.md. Root must separately accept the independent code gate. All missing/expired authority information remains a blocker; do not fill a real boot, deadline or true root_green in this preparation.

Future control code deliberately does not open, hash, parse or evaluate the source input. Future production run_once opens the one pinned source only after its own gates. The local mock fixture runs real host-control comparisons and real frozen authorize with OS reads/setters mocked, and makes production calls raise; it is not an actual-host success receipt.
