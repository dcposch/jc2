# Hostile review — TD6 fixed two-center open-cover kill

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`. Treat every existing producer, case, canonical,
coordination, prompt, log, run, and review byte as immutable. Do not use Bash
or run any local computation. Read in full:

- `xmodel/td6-c1-c3-two-center-cover-gate-20260824.md`;
- every source, manifest, metadata, stdout, stderr, and registration file in
  `cases/td6_c1_c3_two_center_cover_20260824/`;
- only the frozen source-typing/orbit parents cited there, as needed to audit
  the meaning of `(c1,c2,c3)=(C,1,U)` and the original rows.

Charged hashes:

```text
report                 2ada2d70fbdb9db2cf6d93c3b8d3ba0b1f19be1dd5530365a0b3b235e230fbd6
top manifest           e3af7ba9859ddb17516c6950efc062e525330317f5eb7d48495f9ae55a360440
generic stdout         08a4320433c765fbfc101cd2a6c49e7af7f0aa73ff81e84237f3a31dd15f343c
B-local stdout         2532ff680b358201ac4e50e15b8fb86a9d1c38a7a29b589fe3b1c7dac41e00e4
H-zero stdout          68d3a56bcd1fb2f5b0467896cec8995407c22fadd340d2e4aab4f0dfc3116c9e
U-zero stdout          0943cc4235a7b3280c841f402e68c670f16b8597ca01a67f59b85e6154e541a6
intersection stdout    91f2940154d8bcdbbcefaa5e3c9a2af02d555334cda9cc5cf0a83c795e4dcc78
raw quotient stdout    b4c9eb15f50fc45479609c7bd3d71516239ee54994cae46fdbff7348d52d6bcf
```

All substantive replays ran on AWS. Do not rerun them locally. Inspect the
frozen programs and outputs rather than trusting PASS. Independently attack:

1. Source typing. Verify exactly what fixed family the three center
   coefficients parameterize, whether `c2=1` is a genuine restriction rather
   than a gauge, and that every compiled first-band/P12 row is an original
   source row or has an explicitly checked lift to the 28 original rows.
2. The generic/B-local open cover. Derive the chart conditions from the
   printed denominators, distinguish the polynomials `B` and `T`, and check
   that `Res_C(B,T)=64 U^10` plus `B(C,0)=1` really covers every point off
   `U*H=0`. Look for a lost component caused by saturation, fraction-field
   inversion, or a chart factor silently treated as a unit.
3. The complete `U=0` divisor. Check the exact left-null incompatibility on
   `C!=0`, the raw `(C,U)=(0,0)` rebuild, and that the two arguments meet with
   no excluded point or source mismatch.
4. The complete `H=0` divisor. Check the raw certificate off `U*P`, the
   overlap with the already empty `U=0` stratum, irreducibility/squarefreeness
   of `P=128U^6-32U^3+1`, and the raw rebuild over `Q[U]/(P)`. In particular,
   verify that `-k/50` is a unit in the actual coefficient/base extension and
   that all 7,590 inverse checks certify the inversions used, not unrelated
   pivots.
5. The V6 failure and V7 repair. Decide whether the denominator factor `P`
   genuinely invalidates V6 and whether V7 reconstructs the finite fibre
   independently rather than cancelling the same forbidden factor under a
   new name. Audit the genuine 2,885-term P12 and the 28-row/1,540-slot source
   lift, including the perturbation negative control.
6. Evidence custody and logical scope. Check source-closure manifests,
   stdout/stderr/meta consistency, and whether the union of the displayed
   loci is exhaustive. The strongest possible conclusion is only emptiness
   of the frozen source-typed fixed family `(C,1,U)` at this gate. It is not a
   full-centering, neighbourhood, SP-2, maximum-degree, or JC2 theorem.

State the smallest false identity, missing stratum, or missing hypothesis if
one exists. Give one exact promotable sentence with its strict scope. Write
exactly `xmodel/td6-c1-c3-two-center-cover-review-claude-20260825.md`. Do not
edit any other file. End with exactly one verdict: `CONFIRMED`, `GAP`, or
`REFUTED`.
