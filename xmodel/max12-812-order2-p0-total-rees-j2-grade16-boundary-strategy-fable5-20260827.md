# J2 ordered-a1 boundary after grade 16: independent verification, an exact surviving witness, and the grade-17 fork (Fable 5)

Date: 2026-08-27

Lane: speculative, reversible ideation child of V27/V28, blind to V29's
verdict and to all other-model review outputs.  Sole write of this lane.
Author: Fable 5, equal independent co-researcher.

Status: **V27 AND V28 INDEPENDENTLY CONFIRMED FROM LITERAL BYTES AND FROM THE
PINNED SOURCE TAILS; THE GRADE-16 `rho=0, a1!=0` STRATUM IS NONEMPTY — EXACT
RATIONAL WITNESSES CONSTRUCTED, INCLUDING ONE WITH `k!=0`; EVERY TYPED
`a1^N k^M (1+rho W)` CERTIFICATE FROM GRADES <= 16 IS REFUTED; V29 IS
PREDICTED NONUNIT; THE WITNESS FAMILY DIES AT GRADE 17 BY A JET-FREE
CONSTANT.  NO CHART, GATE-T, ORDER-TWO, MAX-12, OR JC2 VERDICT.**

## 0. Inputs, custody, execution disclosure

All hashes observed by me with `shasum -a 256`/hashlib on 2026-08-27.  All
computations below are my own scanner-based parser plus exact `Fraction`
arithmetic in `/tmp` scratch; nothing was written outside this file.

- V23R1 census: `output_r1/RESULT.json` at `ce4d0adb…d14641`; all 42
  `a1_ordered` row files rehashed against **both** the V23R1 table and the
  V27 `row_sha256` table — 42/42 agree.  All 42 rows re-verified
  sigma-homogeneous at their grades and rho-even.
- V27: `aws_q_dual/output/CERTIFICATE.json` at `7558ec42…908995`; producer
  wall time < 1 s on the registered lane.
- V28: `aws_q/RESULT.json` at `c9f89344…4b293` (inner `result_sha256`
  `7e00fc2c…ece3ae`), `aws_p65521/RESULT.json` at `b89f63af…45fef7`
  (`ec3e8041…04289c`); both lanes' `EVIDENCE.sha256` verify 29/29 after
  stripping the absolute `/home/ubuntu/jobs/...` prefixes.  Grade-16 row
  pins (char 0): Tg16_1 `b11e2acb…`, Tg16_2 `e755109d…`, Tg16_3
  `df4c5fd2…`, Tg16_4 `647f852c…`, Tg16_5 `4d410a5a…`, Tg16_6 `e6ccc2b6…`,
  Tg16_7 `c288672a…`.
- Source spec: V20 module `5c233e0f…443a587` (pin matches V28's compiler
  constant), `tails.json` `d72f774c…813848` (569 tails: 36/54/58/81/89/120/
  131).
- V29 preregistrations `34668ead…` and R1 `94f9b2e3…` read; **no V29
  output was read or assumed**.

Two custody notes for successors (defects, not verdict changes):
(a) V28's `EVIDENCE.sha256` records absolute host paths — the same
portability defect family as the V29 V1 custody erratum; freeze relative
paths.  (b) V28's `specialize_old_point` sets the eight new grade-16 jets
to zero rather than solving for them ("new weight-16 coordinates" means
sigma-weight exactly 16, of which none occur).  That convention is **sound
here only because** the emitted dual is supported on the jet-free row
`Tg16_4`; as a general prolongation test it produces false negatives.  V30
must treat jets as honest affine unknowns.

## 1. V27 confirmed, and reduced to an eight-lookup hand certificate

I re-enumerated the complete weight-15 graded piece myself: 23 nonzero
`rho=0` generators, 53 products `m*Tg(g,r)` with `weight(m)=15-g`, exact
RREF rank 46, and `a1^3` outside the span (residual support 1).  The
emitted two-coordinate functional

```text
phi = 1*[a1^3] - (1/3)*[a1*aa0*rs2],   phi(a1^3)=1,
```

annihilates all 53 products in my replay.  Because the generators are
sigma-homogeneous and `rho` has weight 0, the weight-15 piece is the whole
membership question: **`a1^3 ∉ I|rho=0` for the full grade-<=15 row ideal,
with no degree cap** (this retires V26's incomplete-basis caveat, and by
reduction mod rho it refutes the `(N,M)=(3,0)` typed shape cap-free).

Divisor arithmetic collapses the entire verification to eight byte
lookups.  `phi(m*row)=0` can only be violated when `m` divides `a1^3`
(divisor weights 0,5,10,15) or `a1*aa0*rs2` (relevant divisor: `rs2`,
weight 4).  Rows exist at grades 11-15; at `rho=0` only one grade-11 row
survives.  So the complete content of the dual is:

1. `Tg11_1|rho=0 = (3/8)*a1*e0` contains no `a1*aa0` monomial (trivial);
2. each of the seven grade-15 rows satisfies
   `3*coeff(a1^3) = coeff(a1*aa0*rs2)`: six have both coefficients zero,
   and `Tg15_3` has literally `(-1/16)*a1^3` and `(-3/16)*a1*aa0*rs2`.

Any different-model reviewer can confirm V27 from these bytes alone.

## 2. V28 confirmed, and the `-47/384` explained in closed form

Independent checks, all passing: term counts 63/86/98/45/77/22/33 in both
lanes; the p65521 rows equal the char-0 rows reduced mod 65521 term by
term; all seven rows sigma-homogeneous at 16 (weight table extended by
`ell5`:5, `cs4`:6, `rs4`:6, `k10_3`:7, `ac5,az5,ez5`:10, `ec6`:11); all 42
old rows vanish at the V28 point; the `Tg14_2` engine control equals
`1/32`; the seven zero-extension values are `(0,0,0,-47/384,0,0,0)`.

**Jet census (new, load-bearing):** no grade-16 monomial contains two new
jets or a jet squared, so every row is affine in the jets, and

```text
Tg16_1: jets {ac5,az5,cs4,ec6,ez5,k10_3,rs4}
Tg16_2: jets {ac5,ell5,ez5,k10_3,rs4}
Tg16_3: jets {ell5,ez5}, jet part = (3/16)*e0*(ez5 - a1*ell5)
Tg16_4, Tg16_5, Tg16_6, Tg16_7: NO new variables at all.
```

Because `Tg16_4` is jet-free, the V28 point dies under **every** jet
extension, so the verdict is robust despite the zero-jet convention.

The death is now a one-line law.  On the support
`S0={a1,aa0,cs1,ec3,rs2}` the entire 30-equation old-variable system
restricts to four equations, solved in closed form by triangular
elimination (each step linear in one variable, `a1,aa0 != 0`):

```text
Tg13_1|S0: ec3 = a1*cs1
Tg14_2|S0: rs2 = -(2/3)*a1^2/aa0
Tg15_3|S0: cs1 = a1^3/(6*aa0^2)
Tg16_4|S0 = (1/8)*a1^2*aa0*(r - 1),   r := a1^6/(48*aa0^5).
```

The V28 point `a1=aa0=1` has `r=1/48`, giving exactly
`(1/8)(1/48-1) = -47/384`.  The point was killed by its orbit invariant,
not by the stratum: `r` is the free Gm-invariant modulus of the grade-15
`S0` family, and grade 16 pins `r=1` instead of killing the family.

## 3. The main news: the grade-16 stratum is NONEMPTY — exact witnesses

Setting `r=1` rationally (`a1=48u^5, aa0=48u^6`) gives, with everything
unlisted zero and `rho=0`:

```text
WITNESS A (k=0):   a1=48, aa0=48, cs1=8, ec3=384, rs2=-32.
```

All 49 rows of grades 10-16 vanish, with **all eight new jets zero** —
verified against the exported bytes and, independently, against the pinned
569-tail source itself (section 4).  For the unit-`k10` family the
campaign needs `k != 0`; on `S0∪{k}` the only k-carrying old row is
`Tg15_1|S0∪{k} = (5/16)*k*X` with `X|family = a1*aa0*(1+(4/3)r)`, which is
nonzero at `r=1` — so on the minimal support, `k != 0` provably dies
(`X=0` needs `r=-3/4`, clashing with `r=1`).  One support extension fixes
it: `aaa1` enters `Tg15_1` linearly with pivot `-(3/8)*a1*cs1 != 0`, and:

```text
WITNESS B (k=1):   a1=48, aa0=48, cs1=8, ec3=384, rs2=-32,
                   k=1, aaa1=35/3, rs4=-55/27, all else (incl. rho) 0.
```

All 49 rows vanish exactly.  Family laws (verified at four `(u,k)`
values): `aaa1=(35/3)*k*aa0^3/a1^3`, `rs4=-(55/27)*k*u^2`; grade-16 rows 1
and 2 pin two jet combinations (`rs4`; `ec6=48*cs4-ez5`), leaving six free
jets; row 3's jet part vanishes identically on the stratum because
`Tg11_1=(3/8)*a1*e0` forces `e0=0` there.  So the surviving locus through
grade 16 contains a rational family with two essential moduli `(u,k)` plus
six jet parameters.

Consequences:

- **V29 must report nonunit** if it completes honestly: over `Q̄` the
  witness rescales to `a1=1` (weighted torus, `t^5=1/48`), so
  `1 ∉ I|a1=1,rho=0` through grade 16.  A unit verdict would mean a defect
  somewhere; section 6 gives the cross-examination.
- **Every typed certificate `a1^N k^M (1+rho W)` from rows of grade <= 16
  is refuted, for all `(N,M)`**: reduction mod rho would give
  `a1^N k^M ∈ I|rho=0`, but Witness B evaluates the left side to
  `48^N != 0` and the ideal to zero.  This supersedes my grade-15
  refutation table, V27's `N=3` statement, and closes the `M>=1` escape
  hatch, through the exported grades.

Also byte-verified for later use: the exact identity
`a1*Tg16_3 - (1/2)*(ez5 - a1*ell5)*Tg11_1 = a1*T3^0`, where `T3^0` is
row 3 minus its two jet terms (96 terms) — so row 3 contributes `T3^0` to
the old-variable ideal after `a1`-saturation.

**Reduction theorem (hand-proved from the census).**  Let
`I_ext ⊂ Q[31 old vars]` be generated by the 23 nonzero `rho=0` rows plus
`T3^0, Tg16_4, Tg16_5, Tg16_6, Tg16_7`.  Then
`V(I_16) ∩ {a1 != 0} ≠ ∅  ⟺  V(I_ext) ∩ {a1 != 0} ≠ ∅` over any
algebraically closed field.  Proof sketch, all pivots literal bytes:
`ec6` occurs only in row 1 with coefficient `(3/8)*a1`; row 2 always has a
nonzero jet pivot on `{a1 != 0, e0=0}` (if `rs1=0` the `rs4` pivot is
`-(3/32)*a1^2`; if `rs1 != 0` the `k10_3` pivot is `(5/1024)*rs1^3`); row
3 reduces to `T3^0` by the identity above.  Hence **V29's verdict equals
the unit test for the 28-generator, 31-variable `I_ext`** — a smaller
decisive object for every follow-up.

## 4. Independent source-level verification, and the grade-17 fork

To remove all dependence on exported `.poly` bytes I re-implemented the
source emitter from the frozen V28 compiler's formulas (scalar series over
`Fraction`, my own code) driven by the pinned `tails.json`, and compared:
at two random rational points (with `rho != 0` for grades 10-15, `rho=0`
for grade 16, deep coordinates `cs5, rs5, ell6, ec7, k6,…` randomized),
**all 42 V23R1 rows and all 7 V28 rows match the engine's t-coefficients
exactly, 49/49 per point**.  The same engine confirms Witnesses A/B kill
every t-order <= 16 of all seven rows.

The engine then answers the prolongation question one grade up.  With the
witness family numeric and *every* grade-16 and deeper series entry
symbolic (`ell5..ell17, cs4..cs14, rs4..rs14, k10_3..k10_12, ac5..,
az5.., ez5.., ec6.., k6, k6_1..k6_4`), the t^17 layer at `(u=1,k=1)` is:

```text
row 1: -350 - 30*rs4 - 864*cs5 + 18*ec7 + 18*ez6
row 2: -1728*cs4 + 18*ec6 - 216*rs5
row 3: -2000 - 432*rs4
row 5: -20736            <- constant, no jet of any depth enters
rows 4, 6, 7: 0
```

Two independent kill mechanisms: **row 5's t^17 coefficient is the
jet-free constant `-20736*u^17`** (k-independent; the exact grade-17
analog of `Tg16_4`), and rows 2/3 clash on `rs4` (grade 16 forces
`-55/27`, grade-17 row 3 forces `-125/27`).  So the explicit `(u,k)`
family does **not** prolong to grade 17.  This does *not* decide the
grade-17 stratum: the grade-16 stratum is larger than my family (six free
jets, and enlarged supports as in the `aaa1` repair), and the V28 story
one level up shows exactly how a "dead point" can hide a living stratum.
Trust status: grade-17 numbers come from my engine on the pinned tails;
no frozen case exports grade 17 yet, so they are preregistration-grade
evidence only, to be reproduced under custody by V30.

## 5. What this changes for the branch (Gate T, receiver, tree)

- **T-a1 vs T-a0 asymmetry is now proven**: T-a0 died at grade 15 (my pure
  `a0^3` certificate, under different-model review), while T-a1's rho=0
  face is alive through grade 16.  The staged tree cannot close T-a1 by
  the same finite-grade typed-certificate pattern at <= 16.
- **The pivotal fallback is Gate T's total-vs-special comparison**, not
  deeper grades alone.  The witnesses live on the *raw row ideal's* rho=0
  face.  The actual chart is the saturated Rees presentation
  (obligation-table formula (2.3)), and the Gate-T map for this chart is
  still MISSING.  V24's finding (per V26's preregistration) that `a1^3`
  enters only after inverting `rho` hints the surviving stratum may be
  rho-torsion: killed in `K^tot + (rho)` while present in `K^0`.  If so,
  the campaign survives with the stratum alive, and the decisive object is
  the rho-direction deformation: does Witness B extend to a solution mod
  `rho^2`, `rho^4`, …, of the total (rho-even) rows?  That is per-order
  linear algebra in the same coordinates, cheap, and never yet run.
- **Terminal receiver**: untouched (witnesses have `a1 != 0`, hence lie in
  the a1-chart, not `V(J1+J2)`).  But if T-a1 stays alive at every finite
  grade and is not rho-torsion, the "all mass to the receiver" landing
  plan fails for this branch — worth knowing before funding the grade-38
  receiver window.
- The grade-16 jet-free rows 4-7 (and the emerging grade-17 analog behind
  row 5's `-20736`) suggest each grade `g` contributes a small set of
  jet-free old-variable constraints; the prolongation tower on old
  variables is where the emptiness/aliveness question actually lives.
  This is the structure V30 should exploit before any generic Groebner.

## 6. V29 landing protocol (both branches prepared)

- **Nonunit (predicted)**: do not spend AWS on Singular witness
  extraction.  Freeze a V30w case whose validator (i) rehashes the 49
  rows, (ii) evaluates them at Witness B (nine rationals), (iii) runs the
  perturbation negative control (`aaa1=0` must leave `Tg15_1 = 1680*k`)
  and the V28-point positive control (`Tg16_4=-47/384`).  Different-model
  review is then a half-hour byte exercise.  Report `k != 0` explicitly so
  the unit-`k10` consequence (all `(N,M)` refuted) is promoted with it.
- **Unit (unexpected)**: treat as a defect signal, not a result.  Demand
  the explicit lift `1 = sum h_i * row_i|a1=1` and evaluate it at Witness
  B rescaled (`u` with `u^5=1/48` adjoined, or evaluate the homogenized
  identity directly at Witness B): the failing summand pinpoints the
  defective row/byte or the unsound step.  Check first the R1 path remap
  (the known custody weak point) and char/lane agreement.
- Either way, V29's verdict must be cross-checked against the 31-variable
  `I_ext` reduction (section 3), which an independent lane can std in a
  fraction of the 39-variable cost.

## 7. Ranked next-experiment queue

1. **V30w — witness freeze + hostile review** (desk-scale, decisive for
   "grade <= 16 alive").  Contents as in section 6; also record Witness A
   and the family laws.  This is the branch's new anchor fact; it should
   not remain only in this ideation file.
2. **V30 — grade-17 export and honest prolongation** (one AWS pair,
   V28-sized: 73 s compile per lane at grade 16).  Export the seven
   grade-17 rows (bridge grades <= 16 to pinned bytes); preregistered
   controls: on the Witness-B family the jet-free part of row 5 at t^17
   must equal `-20736*u^17`, rows 4/6/7 must vanish, and row 3 must force
   `rs4=-125/27`.  Then compute the jet-free census at 17 (which rows are
   old-variable-only) and re-run the V29-style unit screen on grades
   <= 17, ideally in the eliminated `I_ext,17` form.  Stop rule: verdict
   plus either witness or dual, nothing else.
3. **V31 — rho-direction torsion probe at Witness B** (desk-to-small-AWS).
   Solve the total rho-even rows at Witness B order by order in `rho^2`
   (unknowns: corrections to all coordinates, plus the six free jets);
   report the first obstructed order or a mod-`rho^6` extension.  This is
   the Gate-T (2.5) question made concrete at one point, and it decides
   whether "alive at rho=0" even threatens the total chart.
4. **Weight-20/25 complete graded ladder on `I_ext`** (only if V30 kills
   the grade-17 stratum): V27-style Groebner-free membership for `a1^4`,
   `a1^5` with the grade-17 jet-free rows added — the certificate
   extractor of record for a unit ending, with a dual emitted on failure.
5. **Enlarged-support grade-17 witness hunt** (only if V30's export lands
   and its unit screen is nonunit or times out): extend the triangular
   ladder by `{aa1, cs2, ec4}`, `{ell1, rs1}`-tower branches against the
   frozen grade-17 rows, exactly as `aaa1` repaired `k`.
6. **Engine-independence upgrade** (background): a second-implementation
   replay of the 569-tail emitter (mine exists in `/tmp`, matching 49/49
   rows at random points; promote it into a frozen validator so future
   exports are checked against the tails, not only lane-vs-lane).

## 8. Scope firewall

Everything here concerns the literal 569-tail actual-total source rows,
specialized to the ordered-a1 stage-two chart over `V(J1)` (`J1`, `a0`
killed), on the closed face `rho=0`, in the *raw row ideal* — not the
saturated Rees chart kernel, whose Gate-T comparison remains missing.
The witnesses prove nonemptiness through grade 16 and refute typed
certificates built from rows of grade <= 16 only; they say nothing about
grades >= 17 (where my engine shows the explicit family dies), about the
total family (`rho != 0`), other J2 localizers, the J1 charts, the
terminal receiver, Gate T as a whole, order two, maximum twelve, or JC2.
V29's verdict is not assumed; if it lands unit, section 6's
cross-examination governs before anyone promotes either side.  Grade-17
coefficients are my-engine values from pinned tails, not yet a frozen
case.  All local work was read-only, exact, under two minutes and well
under 1 GiB per step; scripts staged in `/tmp/fable5-g16/`; this file is
the lane's sole repository write.
