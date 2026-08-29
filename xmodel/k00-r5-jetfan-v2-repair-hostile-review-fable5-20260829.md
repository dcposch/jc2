# Hostile review: K00 valuation-five v2 repair (jetfan R5)

Reviewer: Fable 5, independent adversarial mathematical reviewer
Date: 2026-08-29 UTC
Repository basis: `31777ce90994a106aade85064c0d868e32863f94`
Producer under review: `xmodel/k00-r5-jetfan-v2-repair-opus5-20260829.md`
  full SHA-256 `91dcf1731590ca2bdae53804c911c01b2a4ba1ebfc58aa6e182f402c84292d84` (verified)
  body SHA-256 `a13c02edb9e79161cb6f43c4ec05e670e65ad94c6ae83ef1447d58018b68ff21`
  (verified: 60345 bytes through the producer's unique standalone BODY-END line)
Embedded replay block: SHA-256
  `e7c6cab141c31f2732481bd8a19eeea91ac19786e8bfce81e5e4691e97f9d83a` (verified by
  extraction of the single fenced `python` block plus one trailing newline)

## Verdict summary

| item | subject | verdict |
|---|---|---|
| 1 | custody, 169/164/140 censuses, boundary zeros, opens, targets, ranges | **CONFIRMED** |
| 2 | grade calendar, leading cone, rank fan, cokernel functionals | **CONFIRMED** (erratum R1) |
| 3 | rank-two grade-14 exclusion and its divisions/localizers | **CONFIRMED** (notes R3, R5) |
| 4 | rank-one grade-13 `tau*f=0` split, both grade-14 branches, both conjugates | **CONFIRMED** |
| 5 | rank-zero minimal projection, `k10[6]`/`k6[7]`, `A^58` factor, serialization | **CONFIRMED** (erratum R2) |
| 6 | V14R1 contraction and exact grade-19 order analysis | **CONFIRMED** |
| 7 | `D6_2=-(3/512)AB`, `D10_3|V(A,B)=0`, vanished intermediates, ideal certificate | **CONFIRMED** |
| 8 | `5 Jdet[0]` in the full restricted 140-row ideal over every `Q`-algebra | **CONFIRMED** |
| 9 | replay ordinary and `-O`, five mutations, opposite-order reconstruction | **CONFIRMED** |
| 10 | scope sentences | **CONFIRMED** (repair R4 required) |

**Overall: PASS_WITH_REPAIRS.**  Theorem V5 and the scheme-theoretic rank-zero
closure survive every attack mounted here.  All repairs are display-level
wording or misprints; no verified machine fact, no banked identity, and no
step of the exclusion logic fails.  Promotion of the results listed in
"Maximum safe statement" is warranted once R1–R4 are applied.

## Method

Nothing was taken from the producer replay on trust.  I wrote a separate
verification engine from the frozen compiler declarations and the producer
prose only: my own tail/prelude parser (recursive descent, no `ast`), my own
sparse Gaussian-rational polynomial and truncated-series arithmetic, my own
serializer written from the Section 7.3 prose rule.  In addition I ran a
structurally different exact numeric path (random rational points, raw tail
monomials multiplied as numeric `Lambda`-series with **no transverse-degree
truncation at all**, two seeds), which independently corroborates every
truncation bound the symbolic paths use.  The embedded replay was run
ordinarily and under `python3 -O` from the repository root.  All computation
was desk-scale standard-library Python; no Singular, no network, no
`jc2-lean` contact, no repository write other than this file.

## 1. Custody and source (CONFIRMED)

* All five charter artifacts hash byte-exact on this basis: rejected producer
  `82e6512d...`, rejected replay `eb8513b6...`, binding audit `fee02eb0...`,
  frozen tails `d72f774c...`, frozen compiler `2ac7653c...`.  All eight V14R1
  files hash byte-exact (`5b0a77e6`, `87ced4af`, `ed096c82`, `1f8369ed`,
  `ce8b51a7`, `5d9f371c`, `135c17e3`, `93762abd`), and each of those eight
  hashes is declared inside the pinned compiler's `EXPECTED` table, so their
  custody chains through the already-pinned compiler exactly as claimed.
* Precision note (no failure): the replay pins ten files (tails, compiler,
  prelude, `h`, six multipliers).  The three rejected/audit artifacts are
  *not* replay-pinned; Section 1's "All five verified byte-exact" is a
  producer assertion outside the replay.  I re-verified all five myself, so
  custody holds; see R3.  "The four named in the charter" followed by five
  hash lines matches the charter's four bullets (the tails/compiler bullet
  carries two hashes) — cosmetic.
* Compiler declarations match Section 2 exactly: chart
  `C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3, C4=(3+d4)/8, C5=d5, C6=1`
  (`coordinate_images`); tail weights `(8,7,6,5,4,3,2|2,6,10)`; load shifts
  `p10=L^2 k10`, `p6=L^6 k6`, `p2=L^10 k2`; `target_sign=-1` with shifts
  14/16/18 and `Jdet/4` at 19; unit opens exactly `["k10_0","Jdet_0"]`;
  boundary set exactly `{k6_0, k2_0, mu2_0, mu4_0, mu6_0}`.
* Censuses recomputed: `169 = 6*19 + 18 + 14 + 10 + 6 + 4 + 2 + 1`; five
  boundary zeros leave 164; valuation five removes 24 more, leaving the
  listed 140 free coordinates (`90+18+13+9+5+3+1+1`).  569 tail terms; every
  monomial has weight `12+ell`; every load exponent in `{0,1}`, single active
  load.  My parser's seven unloaded rows equal the prelude `r1..r7` term by
  term.
* Dependency ranges, machine-derived independently: generic valuation-five
  range is exactly `d[5..14], k10[0..7], k6[1..8], k2[1..4], mu2[1..5],
  mu4[1..3], mu6[1], Jdet[0]` as full intervals with every index occurring;
  rank-zero range is exactly `d[6..13], k10[0..6], k6[1..7], k2[1..4]` plus
  the full `mu`/`Jdet` block.  Both Section 3 and Section 9 items 4–5 are
  right: the rejected producer's ranges are the generic ones, the audit's
  rank-zero ranges are off by one on `k10` and `k6`.

## 2. Calendar, cone, fan, cokernel (CONFIRMED; erratum R1)

* Grades 0..9 vanish identically; `[L^10]Phi = Q(d[5])` and
  `[L^11]Phi = DQ(d[5])[d[6]]` exactly.  Every row of the Section 3 sector
  table reproduces: quadric 10, `M4` 12, `L6` 12, cubic 15, `mu2` 15, K2 16,
  K10-cubic 17, K6-quadratic 17, `mu4` 17, `mu6`/`Jdet` 19.
* Both cone identities hold as 6-variable polynomial identities.  The
  claimed 4-plane satisfies `A=B=0`, kills all seven `Q_ell`, and its
  parameters are recoverable (`a=x1, b=x2, u=x2-x4, v=x3-8x1`), so it *is*
  `V(A,B)`; the converse set inclusion over a characteristic-zero field is
  forced by the two identities (`AB=0` and `B^2=64A^2`).  Reduced
  field-valued split correctly typed.
* The alpha/beta table is exact for all seven rows; every nonzero `2x2`
  minor is a rational multiple of `Delta=u^2+64v^2`; the fan trichotomy is
  exhaustive.  The five universal functionals annihilate
  `{alpha_i A + beta_i B}` identically in the plane point (hence also kill
  `DQ(y')[anything]` for *any* plane point `y'`, which silently underwrites
  the grade-14 computations), and they are independent, so they span the
  rank-two cokernel; at `u=eps*8i*v` the extra functional
  `E2+(eps i/2)E1` kills the image line — verified over `Q(i)` for both
  conjugates.  Field bookkeeping (`Q` universal, `Q(i)` only in rank one,
  `K-bar` reduction) is correct.
* **Erratum R1.**  The displayed vector in Section 5,
  `M4(x) = (5/8192)(-2uv, u^2-64v^2, uv/4, 0, uv/32, 0, uv/256)`, is a
  misprint.  The machine value on the plane is
  `M4(x) = (5/8192)(-32uv, u^2-64v^2, 4uv, 0, uv/4, 0, uv/32)`, i.e.
  `(-(5/256)uv, (5/8192)(u^2-64v^2), (5/2048)uv, 0, (5/32768)uv, 0,
  (5/262144)uv)`.  The printed vector violates the five universal cokernel
  conditions asserted in the same sentence (`E5+E1/128` and `E7+E1/1024`
  fail on it) and is inconsistent by a factor 16 with the verified solve
  `A(z)=(10/3)kappa v`.  Display-only: no consumed identity uses the printed
  vector, and every downstream identity verifies against the true one.

## 3. Rank two dies at grade 14 (CONFIRMED)

Independently rebuilt with all free symbols carried (`z1..z4`, `w1..w4`,
`d[9]`, `k10[1]`, `k10[2]`, `k6[1..3]`):

* grades 10–12 vanish identically under the stated solves (this pins
  `A(z)=(10/3)kappa v`, `B(z)=-(10/3)kappa u` as the unique rank-two solve
  and reconfirms `L6=0` on the whole plane and `M4(x)` in the image);
* **grade-13 rows all vanish** under the stated `w`-solve.  The producer
  replay checks only grade-13 cokernel solvability, not the row vanishing;
  I closed that hole two independent ways: (i) direct verification that all
  seven grade-13 rows vanish, and (ii) recomputation of grade 14 with `w`
  **completely unconstrained**, which returns byte-identical `E4` and
  `E3+E1/8` values — the exclusion is independent of the grade-13 solve, as
  the structure (universal functionals kill `DQ(y)[w]` for plane `y`)
  predicts.  See R5;
* grade-14 identities hold exactly:
  `E4=(25 kappa^2/131072)(64v^2-u^2)`, `E3+E1/8=(25 kappa^2/4096)uv`, and
  also the parenthetically recorded
  `E5+E1/128=-(25 kappa^2/32768)uv`, `E7+E1/1024=-(25 kappa^2/524288)uv`
  (true, though the replay computes and never checks or prints them — R3);
  `E6` is identically zero at grade 14.

Division/localizer ledger for this exclusion, complete: literal nonzero
rational constants; the declared open `k10[0]!=0` (for `kappa^2 != 0`);
characteristic zero.  No division by `v` or by `Delta` occurs, no
saturation, no localization beyond the declared opens, no quotient-ring
normal form.  The final step `uv=0` and `u^2=64v^2` forcing `u=v=0` is
integral-domain arithmetic.

## 4. Rank one: the split and both branch exclusions (CONFIRMED)

For **both** `eps in {+1,-1}` over `Q(i)`:

* grade 11 pre-solve: every one of the seven rows is a constant multiple of
  the single condition `v*(B(y)-eps*8i*A(y))` (rows 4, 6 identically zero),
  so the collapse claim is exact and the `lambda`-parametrization is the
  general solution;
* grade 12 with `y` at `A(y)=lambda v`: `E4 = -(3/4096) lambda^2 v^2`
  exactly, and `E3+E1/8 = (eps 3i/2048) lambda^2 v^2` — a nonzero multiple,
  so the "same conclusion" remark is right; `lambda=0` is forced;
* the tangent solve `A(z)=(10/3)kappa v + tau v`,
  `B(z)=eps8i A(z) - (160/3) i eps kappa v` makes all seven grade-12 rows
  vanish identically with `tau` free — I re-derived the solved combination
  by hand from the alpha/beta table and row 1 and got the same `160/3`;
* grade 13, with `d[8]` **generic** (stronger than the replay, which omits
  it): the five universal functionals vanish identically and the sixth is
  exactly `E2+(eps i/2)E1 = (eps 3i/1024) v tau f`, `f = u_y - eps*8i*v_y`.
  I also reproduced the constant `(eps 3i/1024)` by hand from the
  alpha/beta table.  Since `v != 0` on the stratum and the base field is a
  domain, `tau*f=0` is forced and the two branches are exhaustive; the
  overlap `tau=f=0` lies in both, and `v_y=0` (a rank-zero-type `y`) is
  inside the `f=0` parametrization, so **no zero branch is dropped**;
* branch `tau=0`: my own `w`-solve (row-1 division by `v`, legal on the
  stratum and verified monomial-by-monomial divisible) makes all seven
  grade-13 rows vanish; grade 14 gives
  `E4 = (25/1024) kappa^2 v^2`, nonzero under the `k10[0]` open — empty;
* branch `f=0`: same construction; grade 14 gives
  `E4=(v^2/4096)(100 kappa^2 - 3 tau^2)` and
  `E3+E1/8 = eps i (v^2/2048)(100 kappa^2 + 3 tau^2)`, whose simultaneous
  vanishing forces `200 kappa^2 = 0`, contradiction in characteristic zero —
  empty.

The `K`-rationality reduction (stratum empty over `K` outright when
`i` is absent; emptiness over `K-bar` implies emptiness over `K`) is sound.

## 5. Rank-zero residual object (CONFIRMED; erratum R2)

* `u=v=0` on the plane is exactly `d[5]=ell(s,t)=(2s,t/8,s,t,s,2t)`, and
  `(s,t)!=(0,0)` is exactly `d[5]!=0`.  At `ell`: `Q`, `DQ`, `C3`, `M4`,
  `L6` all vanish (each verified directly, including the cubic, which the
  grade-12 equality does not subsume).  Grades 0..11 vanish identically and
  `[L^12]Phi_ell = Q_ell(d[6])` exactly, all seven rows.
* Minimal coefficient projection, one type, no mixing: my independently
  computed occurrence set equals the 78-name LIVE list exactly, the 58 FREE
  coordinates occur in no equation of grade <= 19, and no omitted
  coefficient is silently zeroed — the `Z x A^58` product and the column
  bookkeeping `169 = 24+6+48+36+55` both close (`136 = 78+58 = 140-6+2`).
* `k10[6]` and `k6[7]` occur literally at grade 19.  Row-1 coefficient of
  `k10[6]` is exactly `(5/2048)(s A(d6) + t B(d6))`; rows 3, 5, 7 are its
  multiples by `-1/8, -1/128, -1/1024`; rows 4, 6 vanish.  Coefficients of
  `k6[7]`: `(3/64, -3/512, -3/8192, -3/65536)*A(d6)` on rows 1,3,5,7 and
  `(3/1024)*B(d6)` on row 2.  Every such coefficient lies in the span of
  `A(d6), B(d6)` over `Q[s,t]`, i.e. in `(A,B) = rad(grade-12 ideal)`, and
  none lies in the grade-12 ideal itself (the seven grade-12 generators are
  homogeneous quadrics, verified; a quadric ideal contains no linear form).
  The v2 object's use of the *syntactic* range, with the field-valued
  freeness of `k10[6]`, `k6[7]` as a lemma rather than a type change, is the
  correct resolution of the audit disagreement; literal ideal membership is
  nowhere replaced by radical or field-valued substitution.
  **Erratum R2:** Section 9 item 5 says the `k10[6]` coefficient appears
  "proportionally in rows 2,3,5,7"; row 2 is
  `(5/32768) s B(d6) - (5/512) t A(d6)` — in the span, **not** proportional.
  The replay's machine check (`K10_6_AND_K6_7_STATUS`) tests span
  membership and is correct; the prose word is wrong.
* Serialization: implementing the Section 7.3 prose rule myself reproduces
  the canonical bytes **byte-identically**: 207498 bytes, 318 lines
  (`4+10+7+1+1+1+3+5+4+3+1+1+78+58+140+1`), SHA-256
  `02b4cb9f90dfb72eca05608386578de57b6d4db93ef94c1ed60cb807e95f9e6e`, equal
  to the replay's `/tmp` output.  The quoted spot lines (`EQ 1 12`,
  `EQ 4 12`, `EQ 6 12 0`, the `EQ 7 19` head) match exactly.  The
  supersession of the v1 digest `b2488b33...` is correct.  Additionally, all
  140 canonical `EQ` polynomials were re-evaluated at random rational points
  against the truncation-free numeric rows and agree (two seeds), so the
  serialized object is faithful to the literal equations.

## 6. V14R1 contraction and grade-19 order analysis (CONFIRMED)

Re-proved from the artifacts with my own parser: `h*r7 = sum u_i r_i` as a
polynomial identity, `h(0)=20` (and `deg h = 1`); min transverse degrees
`D10, D6, D2 = 3, 2, 2`; `u2, u4, u6` have zero constant term and min degree
1.  The full contraction identity
`h*Phi7 - sum u_i*Phi_i = p10 D10 + p6 D6 + p2 D2 + pmu2 u2 + pmu4 u4 +
pmu6 u6 - pJ h/4` holds at **every** grade 0..19 on the rank-zero cell (my
engine), not only at 19.  Orders on the cell: `ord D10(d)=17`,
`ord D6(d)=12`, `ord D2(d)=11`; hence `ord(p10 D10)=ord(p6 D6)=19` and
`ord(p2 D2)=22>19`; `pmu2 u2 >= 20`, `pmu4 u4 >= 22`, `pmu6 u6 >= 24` — the
K2 sector and all three target-multiplier sectors are absent from `[L^19]`
for exactly the stated reasons (boundary zeros push the load orders up;
the multipliers' zero constant terms add `>= 5`), all four products verified
identically zero through grade 19.  The `Jdet` term contributes exactly
`Jdet[0]*h(0)/4 = 5 Jdet[0]`.  The corrections to the audit's
`ord K10=12, ord K6=7, ord K2=5` and to both documents' "grades 17/18 set
the load terms to zero" (on the cell they read `0=0`; both sides verified
identically zero at 17 and 18) reproduce here.

## 7. Multiplier collapse and the ideal certificate (CONFIRMED)

All verified as exact polynomial identities in my engine, plus numerically:

* `D6_2 = -(3/512) A B` identically in six variables; consequently
  `[L^10]D6(d)` and `[L^11]D6(d)` vanish identically on the cell and
  `[L^12]D6(d) = -(3/512) A(d6) B(d6)`;
* `D10_3` vanishes identically on the whole 4-plane; **stronger and
  load-bearing**: its gradient vanishes identically on the rank-zero
  2-plane (`grad D10_3(ell(s,t)) = 0`), which is what kills `[L^16]D10(d)`
  and the `d[7]`-dependence of `[L^17]D10(d)` — I verified this directly,
  since plane-vanishing alone does not imply it;
* `[L^17]D10(d) = -(295/262144) s A(d6)B(d6) - (295/524288) t
  (B(d6)^2 - 64 A(d6)^2)` exactly;
* the displayed certificate is an exact identity:
  `[L^19](p10 D10 + p6 D6) = -[(295/48) k10[0] s + 32 k6[1]]
  ([L^12]Phi_3 + (1/8)[L^12]Phi_1) - (295/3) k10[0] t [L^12]Phi_4`,
  with the constants re-derived by hand from the two cone identities
  (`295*16384/(262144*3)=295/48`, `(3/512)(16384/3)=32`, `295/3`).

## 8. Scheme-theoretic closure (CONFIRMED)

Assembled without the producer's route (opposite order): I computed
`[L^19](h Phi7 - sum u_i Phi_i)` as the raw convolution
`sum_n h_{19-n}[L^n]Phi_7 - sum_i sum_n (u_i)_{19-n}[L^n]Phi_i` and verified
`5*Jdet[0] = CERT - [that convolution]` as one polynomial identity.  Every
multiplier (`h`/`u_i` series coefficients, the two certificate brackets) is
a polynomial in the live coordinates, so `5*Jdet[0]` — hence `Jdet[0]` —
lies in the ideal generated by the 140 restricted coefficient equations in
`Q[LIVE]`.  Over any `Q`-algebra `R` and any solution with `Jdet[0]` a unit
this is a unit in the zero ideal: the rank-zero cell is empty on the
declared `Jdet[0]!=0` open, with no reducedness, radical, algebraic
closure, or localization input beyond `Jdet[0]` invertible (`k10[0]` is not
even needed for this step).  The producer's boundary statement is also
correct: without the open the certificate yields only `Jdet[0]=0` on the
residual, not emptiness.  Numeric random-point evaluation confirms the
identity on two seeds.  The claim is exactly as strong as advertised and no
stronger.

## 9. Replay, mutations, reconstruction (CONFIRMED)

* Ordinary run from the repository root: `PASS`, 9.45 s wall, 48.2 MB max
  RSS (declared 9.4 s / 47.6 MB).  `python3 -O` run: byte-identical output
  (the replay gates on `need()`, not `assert`, so `-O` removes nothing).
  The Section 10 transcript equals the actual output line for line.  The
  replay reads only the ten pinned files, writes only `/tmp`, and touches
  neither ledgers nor `jc2-lean`.
* All five mutations `DETECTED` (5/5): the grade-13 omission (my B-series
  proves the sixth functional is the nonzero polynomial
  `(eps 3i/1024)v tau f` for both conjugates, so the detection is
  substantive); target sign; target shift; live tail (the drift guard's
  anchor term `tails["4"][7] = [[0,0,0,0,0,2,5,0,0,0], "-63/1024"]` is
  byte-real in the frozen tails and is a `Q4` quadric term, so the cone
  identity, prelude match, and residual SHA all trip); serialization bit
  flip.  Independently, I flipped the target sign and the `Jdet` shift in
  my numeric path and watched the terminal identity break at grade 19, and
  I reproduced the residual digest from the prose rule alone — the
  mutations are not vacuous.
* Opposite-order/independent reconstructions performed: the convolution
  form of the terminal identity (Section 8 above), the by-hand rederivation
  of the `160/3` solve constant and the `(eps 3i/1024)` sixth-functional
  constant, the prose-only serializer, and the truncation-free numeric row
  builder.  All agree.

## 10. Scope audit (CONFIRMED with required repair R4)

Theorem V5, the Section 0 firewall, and Section 11 are clean: finite-jet
emptiness inside the registered V20R2 truncated system only; no residual
point/arc/scheme point, no map, no counterexample, no periodicity or
valuation recurrence, no K00-closure/order-two/maximum-twelve, no Keller, no
JC2 consequence; `Jdet` handled as a source parameter with the `Jdet[0]=0`
locus explicitly outside the type; jets never conflated with maps; no
floor/attainment language anywhere; the rank-one/rank-two exclusions are
correctly presented as field-valued and only the rank-zero step as
scheme-theoretic.  **One blemish:** the Section 8.3 "consistency
observation" asserts other-valuation facts in the indicative ("The same
terminal identity kills valuation >= 7 outright", and a valuation-six
reduction) before disclaiming them.  The disclaimer un-banks them, and their
order arithmetic is consistent with the degree floors verified here, but as
written the report contains other-valuation truth-claims about strata it
says were not analysed.  Repair by rewording (R4); nothing else in the
document leaks scope.

## Required repairs (all display-level)

* **R1** (Section 5): replace the printed `M4(x)` vector by the true
  `(5/8192)(-32uv, u^2-64v^2, 4uv, 0, uv/4, 0, uv/32)`.
* **R2** (Section 9 item 5): for `k10[6]`, replace "proportionally in rows
  2,3,5,7" by: rows 3,5,7 proportional with `-1/8, -1/128, -1/1024`; row 2
  equals `(5/32768) s B(d6) - (5/512) t A(d6)` (span, not proportional).
* **R3** (Sections 1 and 5): state that the three rejected/audit artifacts
  are verified by the producer outside the replay's ten pins (or add them
  to the pins); reword "the replay also records `E5+E1/128`,
  `E7+E1/1024`" — the replay computes but neither checks nor prints them
  (both values verified true here; adding the two `need()` checks is the
  cleaner fix).  Minor: Section 9 item 1's quotation "Grade 13 is again
  solvable" is the v1 rank-two sentence; v1's rank-one wording is "After
  the grade-13 image solve" — the substance of the correction is unaffected.
* **R4** (Section 8.3): strike or subjunctive-ize the two other-valuation
  sentences; keep the disclaimer.
* **R5** (optional hardening, Section 10 replay): add the rank-two
  grade-13 row-vanishing check (`P2[e].c[13]`), mirroring rank one.  Both
  the row vanishing and the independence of the grade-14 functionals from
  the `w`-solve are verified in this review, so nothing is at stake; the
  check is for symmetry and drift protection.

## Maximum exact statement safe to promote (after R1–R4)

1. **Theorem V5** exactly as stated: over any field `K` of characteristic
   zero, the registered V20R2 source (169 columns, five boundary zeros, two
   unit opens `k10[0]!=0`, `Jdet[0]!=0`, 140 coefficient equations
   `[L^n]Phi_i=0`, `0<=n<=19`) admits no valuation-five `K`-point with
   `d[5]!=0`: rank two and rank one (both conjugates, both `tau*f=0`
   branches) are empty at grade 14; rank zero is empty at grade 19.
2. **Scheme-theoretic rank-zero closure**: on the rank-zero cell
   `d[5]=ell(s,t)`, `5*Jdet[0]` lies in the ideal generated by the 140
   restricted equations in `Q[LIVE]`, via the explicit certificate through
   the grade-12 rows and the V14R1 contraction; hence the cell is empty
   over every `Q`-algebra in which `Jdet[0]` is a unit.
3. **The typed object** `K00-R5-R0-RESIDUAL/v2` = `Z x A^58`, minimal
   coefficient projection, canonical serialization SHA-256 `02b4cb9f...`
   (207498 bytes, 318 lines), with the corrected rank-zero dependency
   ranges and the literal occurrence of `k10[6]`, `k6[7]` (coefficients in
   `(A(d6),B(d6))`, not in the grade-12 ideal); item 2 proves
   `Z` meets the declared opens in the empty set.
4. **Exact supporting lemmas**: the two cone identities; the rank fan and
   the six cokernel functionals; `L6=0` on the 4-plane;
   `D6_2=-(3/512)AB`; `D10_3=0` on the 4-plane together with
   `grad D10_3=0` on the rank-zero 2-plane; the full contraction identity
   with its grade-19 scope; the generic dependency ranges.

Nothing beyond this: no other valuation, no arc/map/closure/JC2 content, no
statement about the `Jdet[0]=0` locus.

## Cheapest decisive successor

**Close valuations >= 6 by the same terminal identity (desk-scale, one
producer + one review).**  The disclaimed Section 8.3 mechanism is real and
nearly free, and this review has already verified every ingredient it
needs: for valuation `w >= 7`, `ord(p10 D10) >= 2+3w >= 23`,
`ord(p6 D6) >= 7+2w >= 21`, `ord(p2 D2) >= 11+2w`, targets `>= 15+w`, so
`[L^19]` of the load side is identically zero and the contraction alone
puts `5*Jdet[0]` in the row ideal outright — no strata, no fan.  For
valuation six, only `k6[1]*[L^12]D6(d) = -(3/512)k6[1] A(d[6])B(d[6])`
survives, and `d[6]` is the leading vector already forced onto the cone by
the first nontrivial grade (12), so `A B = (16384/3)([L^12]Phi_3 +
(1/8)[L^12]Phi_1)` collapses it by the same certificate pattern — again no
rank fan.  The packet needs only the per-valuation normalization censuses
and the two short certificates; it converts the 8.3 aside into banked
theorems and shrinks the open K00 valuation ledger to `{3,4}`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `24000`.
- Body SHA-256:
  `0d249cbd704c6c40ff594c46a3bdffe392521e5f32c458364fc03e4fa75a4f17`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
