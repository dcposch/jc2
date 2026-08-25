# Hostile review charge: pointwise common-cubic `3^12` obstruction

Review

- `xmodel/as-b9-9-12-common-cubic-point-mod3p12-obstruction-producer-20260825.md`;
- `cases/as_b9_9_12_common_cubic_mod3p12_tangent_gate_20260825/`.

Run substantive replays on AWS only.  Audit independently:

1. all 299 source rows and all 149 fresh variables in the `3^11 -> 3^12`
   digit equation;
2. ranks `94/95`, kernel 55, exact-gauge 3, non-gauge 52, and cokernel 205;
3. identification of row 12 as determinant coefficient `[x^2 y^2]`;
4. the singleton certificate: fresh row zero and divided carry nonzero;
5. the independent literal 149-column replay and the vanishing of every
   fresh-fresh term modulo `3^12`;
6. platform guards, source/matrix/witness/result hashes, and AWS custody;
7. the strict one-witness firewall, especially that no statement covers the
   full `3^150` common-cubic family.

Write the review to
`xmodel/as-b9-9-12-common-cubic-point-mod3p12-obstruction-review-grok-20260825.md`
and return `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or `REJECTED`.
