You are Fable 5 performing a short independent hostile mathematical audit in
`/Users/dc/code/math/jc2`. Do not enter, list, search, read, build, status, or
modify `jc2-lean`. Use only light standard-library exact algebra; no CAS or
heavy local computation. Preserve every frozen input byte.

Primary target (read this fully):

- `xmodel/ggv-upper-endpoint-deep-q1-q3-composition-sol-ultra-20260828.md`
  SHA256 `6958c3986022e28484ea1a0a15a0b09a562dbd94cc2154ade4fe6dbc35000715`.

Reviewed upstream atoms you may inspect and pin:

- active-c2 different-model review
  `xmodel/ggv-upper-endpoint-active-c2-d8-d15-hostile-review-fable5-20260828.md`
  SHA `042dbacdd4d7fe6e014ccfb7d82d030e633e4a1291a313b9d022d1b78e4e36a8`
  and checker SHA `505cfd93279ffe8189d25a681b8490ba71edbc5567bc5eecea70e0e2bfc52796`;
- corrected de Rham tower producer
  `xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md`
  SHA `9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1`;
- its Fable5 hostile review
  `xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-hostile-review-fable5-20260827.md`
  SHA `7ab758fa002c75cd28d81540e8f63fd8cd0de97fad791afedfeb5fb610c6cb29`;
- reviewed branch-P q1 atom / row license
  `xmodel/ggv-survivor-q1-q2-de-rham-gates-fable5-hostile-review-opus5-20260827.md`
  SHA `46736edc8aa391e50d3c6a1604937bcad85361c25c25f9e3b4c184e19f8afed1`.

Do NOT read the same-model downstream composition addendum
`ggv-upper-endpoint-deep-q1-composition-addendum-r1-sol-ultra-20260828.md`;
the point is an independent different-model check of the frozen coordinator
target.

Audit and reconstruct each point:

1. Licensing firewall: from `n+22<N`, confirm D23 licenses q1 and D25
   licenses q3 only when D23,D24,D25 are all zero. Nothing here is licensed
   by D0..D22 alone. State the exact/full-Keller-system hypothesis.
2. From the reviewed q1 condition
   `V0=A'R0+2AR0'`, `deg R0<=4`, squarefree monic quartic A and A|V0,
   verify `R0=lambda*A`, `V0=3lambda*A*A'`, `S=3lambda*A'` over the base
   field. Track the relation to the reviewed `T_A` q1 theorem.
3. Independently extract
   `q3=2/5 [t^3]F^(5/8)` and verify every coefficient in
   `p^5[F3/(4H^2)-3F1F2/(32H^4)+11F1^3/(512H^6)]`.
   Substitute the displayed reduced prefix and `2Z=S^2-AQ`; on p^2=A
   verify `q3=N/(512p)`, `N=S^3+A(16U-2SQ)`. Audit the p^2=-A twist and
   whether it changes only a harmless nonzero sign.
4. Derive exactness from a general primitive in K(X)(p), separating even
   and odd parts. Track normalization literally. In particular, check the
   target's wording “primitive p*c/512, rescaling C=256c” against its ODE
   `2AC'+A'C=N`. If the existential ODE is correct but that named scaling
   is not, classify it precisely as a normalization repair and give the
   clean corrected primitive/scaling.
5. Start with C rational, not with an unjustified localization. Prove no
   poles away from A; at a simple A-root verify the `(1-2m)A'(alpha)`
   coefficient excludes integral poles; then prove C polynomial. Check
   `deg N<=9`, leading coefficient `(2d+4)lc(C)`, and `deg C<=6`, including
   all raw degree bounds used for S,Q,U.
6. With S=3lambda*A', reduce the ODE modulo A and verify
   `C=27lambda^3(A')^2+A*r`, `deg r<=2`. Substitute and verify
   `16U=2SQ+108lambda^3 A'A''+3A'r+2Ar'` coefficientwise.
7. Consume only the reviewed exact-D=0,c2!=0 D12 conclusion `A|(QS+4U)`.
   Reduce modulo A and justify the degree comparison giving
   `r=-6lambda Q-36lambda^3A''`. Then verify exactly
   `U=-(3lambda/4)(A'Q+AQ')-(9lambda^3/2)A A'''` and
   `L=-3lambda A(Q'+6lambda^2A''')`.
8. Verify lambda=0 implies S=U=0. Audit the alternate double-divisibility
   proof and its constants/function-space/degree assumptions if useful.
   Include the control showing q3 alone (without D12 A|U) does not force
   U=0, e.g. the appropriate c=A,U=48A' normalization.
9. State field/base-extension/radical scope and exact-D=0,c2!=0 scope. Do
   not promote this to scheme membership, branch emptiness, endpoint
   exclusion, Keller theorem, or JC2.

Create a compact self-contained standard-library checker with symbolic
sparse-polynomial identities plus exact sample/mutation controls; do not
import producer checkers. Run it. Create:

- `xmodel/ggv-upper-endpoint-deep-q1-q3-composition-hostile-review-fable5-20260828.md`
- `xmodel/ggv-upper-endpoint-deep-q1-q3-composition-hostile-review-fable5-20260828-check.py`
- `cases/ggv_8_28_upper_endpoint_deep_q1_q3_composition_hostile_review_fable5_20260828/`
  with README.md, RESULT.json, SOURCE.sha256, EVIDENCE.sha256.

Give explicit PASS/REPAIR/FAIL and name every defect with impact. Include
mutations for at least one q3 binomial coefficient, ODE normalization,
D12 omission, and a final U/L constant. Hash only final bytes, make
manifests repo-root-relative and non-self-referential, rerun with
`PYTHONDONTWRITEBYTECODE=1 python3 -B`, and return paths/hashes/output.
Proceed directly to the audit and artifact construction.
