# AWS launch metadata

## Authoritative V2 execution

- Host: Box02, AWS instance `i-010201a5da47795c4`, recorded hostname
  `ip-172-30-0-186`.
- Registered tag:
  `max12_812_order2_square_positive_load_fan_z3_v2_box02_20260826T111832Z`.
- Remote directory:
  `/home/ubuntu/runs/max12_812_order2_square_positive_load_fan_z3_v2_box02_20260826T111832Z`.
- Start/end: `2026-08-26T11:18:50Z` / `2026-08-26T11:18:56Z`.
- Frozen archive SHA-256:
  `77d9d4b86a1eea928edd842d96234cc4d8a8a9481fdbaade324eac901e955a76`.
- Exit status: `0`; stderr and wrapper log are empty.
- Python package: `z3-solver==4.13.3.0`.  The exact downloaded wheel was
  installed offline and is preserved under `evidence/box02_v2/output/wheel/`;
  wheel SHA-256 is
  `794843e4946ade1561e40a75ffc1163b45d36b493fd6cc269ad1d6a65bddb8e5`.
- Evidence manifest: `EVIDENCE_V2.sha256`.

The downloaded evidence was checked again locally with the dependency-free
exact-rational witness checker: `PASS_EXACT_RATIONAL_WITNESSES`, 80 cells.

## V1 negative control

The first Box02 execution is retained under `evidence/box02/`.  Its
enumeration and exact witness check passed and its JSON is byte-identical to
V2, but it did not record the exact wheel hash promised by preregistration.
It is therefore custody-negative and supplies no authoritative result.  See
`V2_CUSTODY_ERRATUM.md`.
