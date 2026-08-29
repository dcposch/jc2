Act as a hostile characteristic-zero reviewer.  Work in
`/Users/dc/code/math/jc2`.  Review the immutable provisional theorem

```text
xmodel/max12-812-order2-affine-faber-a-homogeneous-direct-unit-cone-theorem-20260826.md
SHA-256 c4926d0476f4df7d910b09645bf387f06292f3faaa25f2e7793b81ba2001bf71
```

Charge, but do not trust verdict language in, these frozen inputs:

```text
e0a64e55ea21c41ee06e635740f7b8af375ce64855638cc44109afb8b384492a
  cases/max12_812_order2_affine_faber_a_full_k_multisupport_20260826/RESULT.md
c16d31a8089dca365014a710e40d33a6e5a0b4924053439ead03f584a4e45e7b
  cases/max12_812_order2_affine_faber_a_full_k_relative_cone_v2_20260826/RESULT.md
f7606a759e5cf6f9a52432baef1af2fb170ce04b65cbd573a96a0f17bbdc0619
  cases/max12_812_order2_affine_faber_a_full_k_relative_cone_v2_20260826/EVIDENCE.sha256
743742bac469af09ccb3b46b6366657fa62c4161e6b61a11361f63cbc5f2d0c8
  cases/max12_812_order2_affine_faber_a_full_k_relative_cone_v2_20260826/FREEZE.sha256
56123a6f2b110284871fe65d664ffed89cb5004d1498e59a81719c2278c59f23
  xmodel/max12-812-order2-square-normal-first-block-divisibility-bridge-theorem-20260826.md
85389a28a69b5e030fa689ccce9dcccee484dae9169679053d0870cfe1e9f0ff
  xmodel/max12-812-order2-square-normal-first-block-divisibility-bridge-hostile-review-grok-v2-20260826.md
fef0524a91c239b9086df8377e0b1270430b2fb164915eb8286bf52f9508cf32
  xmodel/max12-812-order2-affine-faber-a-delayed-load-valuative-composition-theorem-20260826.md
a6d434b5342a32bcefc74b78fd4526eaf1a6556a73ddcc22b970c9958d248f18
  xmodel/max12-812-order2-affine-faber-a-delayed-load-valuative-composition-hostile-review-grok-20260826.md
```

Independently attack all of the following; a check of only the intrinsic
term is insufficient.

1. Rebuild or parse the complete exact-Q 371-term support of `K=E*H3+H5`.
   At weights a=5, normal=15, U=V=6, all four genuine complements=12,
   all three loads plus mu2 and mu4=42, verify every term has weight >45
   except `-E*M^3*normal^3/16`.  The frozen q6 analyzer used mu4=48, so
   separately use the exact derivatives dK/dmu4=4a and
   dK/dmu2=-aE+20a^3 to verify lowering mu4 to42 does not create a tie.
   Retain coefficient factors over Q[E,M].
2. Prove or refute the homogeneous rescaling for arbitrary positive
   rational h after finite ramification.  Check that coordinatewise larger
   valuations cannot create a new equality, including unequal U,V orders,
   complements at >=2q, all loads, targets, center/tangent series, and
   q=infinity.
3. Re-derive the complete low-kernel initial rows.  Check the strict range
   0<q<2h/5, the inequalities
   2h+2q<14h/5<3h, both D(x)/D(y) eliminations, unequal orders, and the
   absence of a center, load, target, cubic, or connection term.  At the
   equality q=2h/5, check that the high-kernel 371-term unit applies, so
   there is neither a gap nor double-counted unsupported face.
4. Audit the bound that every effective load and every target relevant to
   rows 1,3,4,6 has valuation >=14h/5.  Decide whether mu6 or J can reenter
   despite cancelling from K, and whether a target omitted from the low-q
   four-row block can tie it.  Find the smallest missing weight if any.
5. Audit the complementary-pivot argument rather than assuming R,S>=2q.
   Decide whether it is uniform under rescaling and complete-DVR leading
   coefficient absorption.
6. For the literal delayed-source corollary, check exact square division,
   first-block timing 2H<42 for every 0<H<=15, the factor conclusion
   N0=m*z*(z^2+p), and the exact D(M) coefficient entry.  Distinguish the
   proved p,m units and q>0 from the explicit center hypothesis a>=H/3.
   Check 42>=14H/5 at equality and strictly below, all later targets, and
   rational H after ramification.
7. Attack the claimed inclusion of K10=0.  Identify every point in the
   proof that used K10 as a unit in the older theorem, and decide from the
   literal rows/full K support whether the new argument truly avoids it
   when the other effective loads obey the bound.
8. Enforce the firewalls: H>15, a<H/3, q=0, p=0, m=0/reset, square and
   more-degenerate factor types, other load slopes, total-Rees/saturation,
   terminal/Taylor, order two, maximum twelve, and JC2.

Write exactly one report and no other file:

```text
xmodel/max12-812-order2-affine-faber-a-homogeneous-direct-unit-cone-hostile-review-grok-20260826.md
```

Give one verdict `CONFIRMED`, `REPAIR`, or `REJECT`, smallest failing
identity/hypothesis/valuation face, recomputed hashes, exact proof scope,
and auditable derivations.  Do not edit the target, producers, shared
ledgers, or `jc2-lean`.  Do not treat finite-field agreement or printed
PASS/verdict tokens as characteristic-zero evidence.
