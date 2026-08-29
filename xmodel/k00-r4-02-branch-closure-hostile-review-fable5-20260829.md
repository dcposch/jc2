# K00 V20R2 valuation four `R4-02` branch closure: different-model hostile review

Reviewer: Fable 5 (independent adversarial lane)
Date: 2026-08-29 UTC
Review basis commit: `0375694aa21fd8db3b465ef2098ca539106a1582`
Reviewed report frozen at `31777ce90994a106aade85064c0d868e32863f94` (parent of the
review basis; every pinned input is blob-identical at both, verified in Section 1)
Lifecycle: `HOSTILE_REVIEW_COMPLETE / PASS_WITH_MINOR_REPAIRS`

## 0. Verdict

| # | attack area (per review charge) | verdict |
|---|---|---|
| 1 | custody; source/open typing; grade calendar; variable ranges; reduced next-rank-two localization | `CONFIRMED` |
| 2 | fixed two-plane `W = im DQ(y)`; five universal cokernel functionals; grade 11 carries no inhomogeneity and forces `A(d[6]) = B(d[6]) = 0` | `CONFIRMED` |
| 3 | raw grade-15 identities `D1`, `D2`, `D3` with every later jet, load, target symbolic, all scalars and signs | `CONFIRMED` (coefficient-exact) |
| 4 | branch units on `u_y = 0` and `u_y^2 = 192 v_y^2`; uniform `Phi = Psi = 0` vs `Delta_y != 0` contradiction over arbitrary characteristic-zero fields | `CONFIRMED` |
| 5 | no rescue by `k2[1]`, `k6[1]`, free cone variables, or target columns; grades 16–19 vacuous only after the grade-15 unit | `CONFIRMED` |
| 6 | certificate localization; field descent; set-theoretic vs scheme-theoretic scope; residual becomes `R4-00` alone | `CONFIRMED` (conditional exactly as declared) |
| 7 | mutation/sensitivity claims; overstatement and missing-dependency sweep | `CONFIRMED`, three wording-level findings |

No claim is `GAP` or `REFUTED` at mathematical scope.  Both branch closures, the
uniform strengthening, and the unit-ideal certificate are exact.  Three
wording-level repairs are required before promotion (Section 10); none touches
an identity, a unit, a scalar, or the conclusion.

## 1. Custody

Verified byte-exactly on the review basis working tree:

```text
a4fe05d33066d956016b3ef152fc138b5bd3a1dd0a4eec77f8ba05ada2c5f812  (full)
32f79463afee2083dd5ca010d8783942484961a290766d06c707a2ed99c0a6b0  (body, 23493 bytes)
  xmodel/k00-r4-02-branch-closure-opus5-20260829.md               (report under review)
be37360e22524c0f5e7a739753c237c3c94f71f0b5d44bfd9dcd89dddade134a  (full)
3bb710d39c8fea9663bb1e6c1ed4d7c5b323a8741921b75aef2e8b844377bb40  (body, 10719 bytes)
  xmodel/k00-r4-jetfan-provisional-sol56-20260829.md              (producer)
2ce2e4bfd9c23564a8e2be66437772d1cb9855ece4ebaf8ee37b005436c4ff43  (full)
220569e13dd5fbd14baffb53951992dbacbf5975e3c5a91795dced556ccf09d0  (body, 21336 bytes)
  xmodel/k00-r4-jetfan-hostile-review-fable5-20260829-r1.md       (R1 review)
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
```

All match the coordinator pins and the report's own Section-1 pins.  Git blob
identity of `tails.json` (`7e598255…`) and the compiler (`890605a2…`) holds at
all three of `e930fa90` (producer basis), `31777ce9` (report basis), `0375694a`
(review basis): no drift anywhere in the chain.  The report itself is untracked
at the review basis, as expected pre-promotion; its declared frozen basis is the
parent of mine, with no pinned input differing.

## 2. Review protocol

Clean-room reconstruction in `/tmp/k00r402rev/` (seven stdlib-only Python
scripts; exact `Fraction`, formal `1/v_y`, and `Q[r]/(r^2-192)` arithmetic
written from scratch).  The 569-tail JSON was parsed independently; every
convention (ten exponents, weights `[8,7,6,5,4,3,2 | 2,6,10]`, weight law
`12+ell`, at-most-one load with exponent in `{0,1}`, coordinate images, load
shifts `Lambda^2/Lambda^6/Lambda^10`, targets `-Lambda^14 mu2`, `-Lambda^16
mu4`, `-Lambda^18 mu6`, `-(Lambda^19/4) Jdet`, truncation `Lambda^20`, 169/164
column census with the five boundary zeros and the two unit opens) was read from
the frozen compiler only.  Neither the producer replay
`xmodel/k00-r4-jetfan-replay-sol56-20260829.py` nor any Opus scratch or run log
was read or executed.  Two independent evaluation paths were built: (i) a full
symbolic seven-row build on the `R4-02` stratum (`x = ell(s,t)`,
`y = cone(a_y,b_y,u_y,v_y)`, `d[6..19]` free six-vectors, all load and target
columns free), and (ii) a direct `Fraction`-series evaluator with no polynomial
layer.  They agree on all `7 x 20` row-grade cells at 8 random rational points
(zero mismatches).  Every claim check below is exact polynomial equality, not
sampling, unless explicitly marked as a spot check.

## 3. Area 1: source, typing, calendar, ranges, localization — `CONFIRMED`

- Tail census 569 with the exact weight law and load linearity; constant-term
  cancellation `R_i(0) = M_i(0) = N_i(0) = P_i(0) = 0` re-proved.
- Degree censuses reproduce the report's Section 2 lists exactly, including its
  two corrections to the R1 census: the row-7 `P`-cubic (`P` row 7 `{1,2,3}`)
  and the row-5/6/7 `M`-quintics are real, and first arrive at grades 23 and 22
  respectively — outside the window, so the calendar is unaffected, exactly as
  stated.
- Window calendar `Q:8, C3:12, C4:16 | M2:10, M3:14, M4:18 | N1:11, N2:15,
  N3:19 | P1:15, P2:19`, `mu2[j]:14+j`, `mu4[j]:16+j`, `mu6[1]:19`,
  `Jdet[0]/4:19` follows arithmetically from the censuses and is reproduced by
  the stratum build's actual variable incidence (row-2 target hits at grades
  15–19, row-4 at 17–19, rows 6 and 7 at 19; rows 1, 3, 5 target-free through
  19).  Grades 0–7 vanish identically on the stratum.
- Variable ranges: the in-window census `d[4..15]`, `k10[0..9]`, `k6[1..9]`,
  `k2[1..5]`, `mu2[1..5]`, `mu4[1..3]`, `mu6[1]`, `Jdet[0]` is correct as a raw
  window statement.  Refinement (consistent, not an error): on the `R4-02`
  stratum only `k10[0..7]` and `k6[1..7]` actually occur — `k10[8..9]`,
  `k6[8..9]`, and all of `d[15]` multiply identically-vanishing functionals
  (`M2(ell) = 0`, `polar_M2(ell,cone) = 0`, `N1|cone = 0`, `DQ(ell)`-columns),
  so `d[15]` is invisible in the window exactly as claimed, and `d[16..19]`
  never appear.
- Localization: `rank DQ(y) = 2 <=> Delta_y != 0` on the cone (from the
  `W`-structure below); on branch `a`, `Delta = 64 v_y^2`, on branch `b`,
  `Delta = 256 v_y^2`, so the `v_y`-localizer is exactly the branch open in both
  cases and the localization is legitimate.

## 4. Area 2: `W`, the five functionals, and grade 11 — `CONFIRMED`

- The adapted map `(a,b,u,v,A,B) -> cone(a,b,u,v) + e(A,B)` has determinant
  `-1` and `A(p) = A`, `B(p) = B`.  The full `alpha_i/beta_i/q_i` table of
  Section 3 is reproduced coefficient-exactly, along with `Q_1 + 8Q_3 =
  (3/2048)AB`, `Q_4` pure, `Q_6 = 0` (consistent with row 6 having no
  quadratic part at all), and the two-line reduced-cone proof over any field.
- `alpha = (3u/1024)w + (3v/256)e_2` and `beta = (-3v/1024)w + (3u/16384)e_2`
  with `w = (1,0,-1/8,0,-1/128,0,-1/1024)`: exact.  Hence `im DQ(y)` sits in
  the fixed plane `W` for every `(u_y,v_y)` and equals `W` iff `Delta != 0`;
  `K1..K5` annihilate `W`; rows 1, 2 have determinant `(9/16777216) Delta`
  (`(9/65536) v_y^2` at `u_y = r v_y`, `(9/262144) v_y^2` at `u_y = 0`).
- Grade 11 on the stratum is **exactly** `alpha_i(u_y,v_y) A_6 +
  beta_i(u_y,v_y) B_6` for all seven rows, as a raw polynomial identity with
  all of `d[6..14]`, all loads, and all targets symbolic — the load-bearing
  no-inhomogeneity claim.  The mechanism, each part verified as an exact
  identity: `DQ(ell) = 0`; `k10[1] M2(ell) = 0`; `k6[1] N1(ell) = 0`; and
  `kappa`-polar `polar_M2(ell(s,t), cone(a,b,u,v)) = 0` identically (because
  `M2|cone` is a quadratic in `(u,v)` alone with values in `W`, and `ell` has
  `u = v = 0`).  With `Delta_y != 0` this forces `A_6 = B_6 = 0` on both
  branches; the displayed branch-`a` and branch-`b` grade-11 row forms are
  exact.
- I also re-derived the surrounding ledger: grade 12 mod `(G11)` equals
  `alpha_i(A_7 - (10/3)kappa v_y) + beta_i(B_7 + (10/3)kappa u_y)` for **all
  seven rows** simultaneously, so rows 1, 2 determine the displayed `(A_7,B_7)`
  with zero kernel and the cokernel rows vanish; `K@13` vanishes mod `(G11)`
  alone; `K2@14 = 0` and `K1@14` equals the five-term row-4 equation
  coefficient-exactly, with `K3@14`, `K4@14`, `K5@14` computed in general
  `(u_y,v_y)` and found mutually proportional (`K4 = -(1/8)K3`,
  `K5 = -(1/128)K3`) — so grade 14 imposes exactly two independent conditions,
  whose branch forms reproduce the displayed `t = 0`, `s = -(25/12)kappa^2`
  and the branch-`b` `E1/E2` system with determinant `-4r/3`.

## 5. Area 3: the raw grade-15 identities — `CONFIRMED` coefficient-exactly

`D1 = 16G_7,15 - G_5,15 + (1/128)G_1,15`, `D2 = G_3,15 + 8G_5,15 +
(3/16)G_1,15`, `D3 = G_6,15` (combination arithmetic `D1 = 16K5 - K4`,
`D2 = K3 + 8K4`, `D3 = K2` checked) equal the displayed right-hand sides —
`Phi`/`Psi` leading terms, both `A_6`- and `B_6`-brackets, every scalar and
every sign — as **raw polynomial identities** with `s, t, a_y, b_y, u_y, v_y`,
all thirty-six components of `d[6..11]` and the rest of `d[8..14]`, all live
load columns, and all live target columns free.  No substitution was applied.
The verified support of all three is exactly
`{s, t, u_y, v_y, d[6], d[7], k10[0], k10[1]}`, with `d[6]`, `d[7]` entering
only through `A_6, B_6, A_7, B_7`.

Structural mechanism (verified, and worth recording): the `q_i(A,B)`-parts of
the three combinations vanish **as forms**, which is why no
`A_8/B_8`-polar-terms survive in `D1`–`D3` even though the individual `K@15`
rows do contain `d[8]`; and the `(16K5-K4)`-, `(K3+8K4)`-, `K2`-projections of
the cone cubic `C3|cone` are exactly `(3/4096)Phi`, `-(1/512)Phi`,
`(1/65536)Psi` as cubics in `(u,v)` only — no `(a,b)`-dependence, which is why
`a_y, b_y` are absent.  Imposing only `(G11)` gives `D1 = (3/4096)Phi`,
`D2 = -(1/512)Phi`, `D3 = (1/65536)Psi` identically in everything else,
including free `A_7, B_7`.

## 6. Area 4: branch units and the uniform contradiction — `CONFIRMED`

- Branch `a` (`u_y = 0`): `D1 = (3/64)v_y^3`, `D2 = -(1/8)v_y^3`, `D3 = 0`
  identically.  Empty with `v_y != 0`.
- Branch `b` (`u_y = r v_y`, exact `Q[r]/(r^2-192)` arithmetic): `D1 =
  -(3/8)v_y^3`, `D2 = v_y^3`, `D3 = 0`; both values `r`-free, so the
  conclusion transfers along both roots and descends to any characteristic-zero
  field containing a square root of 192, and the branch is trivially empty
  otherwise.  `Q[r]/(r^2-192)` is a field (192 is not a rational square).
- Uniform strengthening: the identities hold with `u_y` free, `(G11)` needs
  only `Delta_y != 0`, and `Phi = Psi = 0` with `Delta_y != 0` is contradictory
  over any characteristic-zero field by the displayed two-chart argument
  (`v_y = 0 => Psi = -u_y^3 != 0`; `v_y != 0 => 512 v_y^2 = 0`); the only
  coefficients consumed are units away from characteristics 2 and 3, so
  characteristic zero is safe.  This is genuinely stronger than the producer
  scope: `Psi = 0` (the producer's `R4-02` restriction) and `v_y != 0` are
  derived, not assumed.

## 7. Area 5: rescue exclusion and grades 16–19 — `CONFIRMED`

- `k2[1]`: `P1_i(ell) = (t/2)w_i + (s/32)(e_2)_i` exactly, hence in `W` and
  annihilated by all five functionals — the grade-15 `k2[1]` column moves only
  `(A_10,B_10)` and never `D1`–`D3`.
- `k6[1]`: the grade-15 `D`-combinations are `k6`-free (raw support above);
  `N2_i(ell)` has vanishing `D`-projections; `N1` factors through `(A,B)`
  exactly (`N1_i = nA_i A + nB_i B`), so all grade-15 `k6[j] N1(d[9-j])`
  contributions die under `(G11)`; and raw `K@16` does contain `k6[1]` — first
  cokernel reach at grade 16, as claimed.
- Free cone variables, higher jets, targets: excluded by the verified raw
  support of `D1`–`D3` and by rows 1, 3, 5, 7 being target-free at grade 15
  (row-6 and row-7 targets first arrive at grade 19; the certificate avoids
  row 2 entirely).
- Grades 16–19 vacuous only after the grade-15 unit: an exact witness point on
  branch `a` (with the forced `s = -(25/12)kappa^2`, `t = 0`) satisfies **all
  49 literal rows of grades 8–14** while `D1` evaluates to `3/64 != 0` — so
  grade 15 is the first kill, not earlier.  The Section-9.1 negative control
  was independently rebuilt: withholding only `K@15` (whose `D`-combinations
  carry exactly the `(3/64)v_y^3` and `-(1/8)v_y^3` kills) and solving rows
  1, 2 forward, grade 16 forces exactly `v_6 = 0` and
  `u_6 = (625/432)kappa^3`: on branch `a` fully symbolically —
  `K2@16 = (3/1024)v_y^2 (u_6 - (625/432)kappa^3)` and, after that pin,
  `16K5-K4 = (9/64)v_6 v_y^2`, `K3+8K4 = -(3/8)v_6 v_y^2` — and on branch `b`
  by an exact `Q(r)`-arithmetic spot check at a random rational point
  (`kappa = 2`: solved `u_6 = 625/54 = (625/432)kappa^3`, `v_6 = 0`).  The
  remaining grade-16 rows consume free load/jet columns (`K10_2`, `K6_1`,
  `K2_1`, `a_6`, `b_6`), so the machinery manufactures no contradiction.

## 8. Area 6: certificate, descent, scope, residual — `CONFIRMED`

- The grade-11 solve formulas are exact on both branches (branch-`b`
  determinant `(9/65536)v_y^2`; `3v_y A_6 = 4(r G_1,11 + 16 G_2,11)`,
  `3v_y B_6 = 64 r G_2,11 - 256 G_1,11` verified in `r`-arithmetic), and the
  assembled Section-6.3 membership was verified as an exact polynomial identity
  on both branches after clearing `9 v_y^2`: the certificate exhibits
  `c v_y^3` (branch units `3/64` and `-3/8`) in the ideal generated by the five
  quoted literal rows, quadratically in the grade-11 generators, so `1` lies in
  the localized ideal and the cell has no `F`-point for any characteristic-zero
  `F` or algebraic closure.  Five generators suffice as claimed; minimality of
  the five-element set is not established and not needed.
- Set-vs-scheme scope is typed correctly: reduced, field-valued emptiness only,
  no nilpotent claim.  The `R4-00`-alone conclusion is drawn exactly as
  conditioned: the grade-12 leading-rank exclusions and the next-rank-one
  grade-15 exclusion are consumed as reviewed hypotheses selecting the stratum
  (they are `CONFIRMED` in the R1 parent), the next-coefficient trichotomy on
  the reduced cone is complete over a field, and next-rank-two is now closed
  here; nothing else is needed.
- The `R4-00` entry facts quoted for the successor were re-verified on a
  separate `y = ell(s1,t1)` stratum build: grades 0–11 vanish identically,
  `G_i,12 = Q_i(z) + kappa*polar_M2_i(x,z)` for all seven rows with support
  exactly `{s, t, kappa, z}` (no `s1, t1`, no `d[7]`, no other load), row 6
  identically zero — six live affine quadrics; and `C3_i(ell) = 0`,
  `M2_i(ell) = 0` for all seven rows, `C4_i(ell) != 0` exactly for `i != 6`.

## 9. Area 7: mutations, overstatements, dependencies — `CONFIRMED` with findings

Source-level mutations independently rebuilt and detected: `+1` on the row-6
tail monomial `C4*C5^2*C6^4` (present in the frozen tails) changes `G_6,15`;
`C4 = (3+d4)/8 -> (1+d4)/8` breaks the constant cancellation and floods grades
0–7.  The `192 -> 193` control mutates a derived quantity (the cone cubic), so
it is the weakest of the three; the other two are genuine source sensitivity.
The dependency sweep found no missing hypothesis: the closure consumes exactly
the two reviewed stratum-selection results plus raw grades 11 and 15.

Findings (all wording-level, none mathematical):

1. Section 5's sentence "`K1..K5` at grades 11, 12, 13 are identically zero on
   the whole stratum" is raw-true only at grade 11.  At grades 12–13 the
   cokernel rows vanish only modulo `(G11)`: raw
   `K1@12 = -(3/8192)A_6^2 + (3/524288)B_6^2 != 0` (and raw `K@13` carries
   `A_6/B_6`-multiples).  The sequential reading is clearly intended (the
   grade-14 paragraph says "after `(G11)`"), and Section 6 is explicitly raw,
   but the sentence as written overstates.
2. Section 10 item 2 attributes the uniform set-emptiness to "the explicit unit
   `(3/4096)v_y(64v_y^2-3u_y^2)` of Section 6.3".  On the uniform cell that
   expression alone is not a unit (`Phi = 0` has field points with
   `v_y != 0`), and the `v_y = 0` chart is killed by `D3`'s `-u_y^3/65536`, not
   by the `v_y`-localized certificate.  Section 8's two-chart argument and
   Section 10 items 1–2 read together are correct; the attribution clause is
   loose.
3. `CERTIFICATE_DIGEST` (57 records) cannot be independently recomputed from
   the body: the record serialization (variable naming, monomial order) is not
   pinned.  The count arithmetic is consistent (3 strata x (7 + 5 + 5 + 2) =
   57), and the certificate itself is fully displayed in the body, so the
   digest is auxiliary; it should either be spec'd or dropped at promotion.

## 10. Repairs required for promotion

1. Reword Section 5 as in Finding 1: "identically zero after imposing `(G11)`"
   for grades 12–13, optionally recording raw `K1@12 = q_4(A_6,B_6)`.
2. Tighten the Section 10 item-2 attribution as in Finding 2 (cite the
   `Phi = Psi = 0` pair / the `u_y`-chart for `v_y = 0`, reserving the
   `v_y`-localized unit for the two `R4-02` branches).
3. Pin or drop `CERTIFICATE_DIGEST` (Finding 3).

Nothing else.  All identities, units, solve formulas, calendar rows, control
values (`v_6 = 0`, `u_6 = (625/432)kappa^3`, both branches), and scope
declarations survived the attack.

## 11. Maximum exact statement safe to promote

The report's Section 10 statement is safe verbatim once Repair 2 is applied:
over any characteristic-zero field, on the exact normalized V20R2 source with
the declared opens and boundary zeros, `d = Lambda^4 x + Lambda^5 y + ...`,
`x != 0` on the old plane and `rank DQ(y) = 2`: grade 11 forces
`A(y') = B(y') = 0` for the next visible coefficient, grade 15 forces
`Phi = Psi = 0`, these contradict `Delta_y != 0`, so the whole cell — in
particular both `R4-02` branches — is empty as a set at grade 15, with the
branch-specific units `(3/64)v_y^3` and `-(3/8)v_y^3` and the displayed
five-row membership certificate; hence, jointly with the promoted
producer/review grade-12 and next-rank-one results, the exact valuation-four
grade-19 residual is `R4-00` alone.  Reduced, field-valued, finite-jet scope
only.

## 12. Cheapest successor

Unchanged from the report and now better grounded: the `R4-00` entry solve.
Its grade-12 system is verified here to be exactly the six affine quadrics
`Q_i(z) + kappa*polar_M2_i(x,z) = 0` (row 6 identically zero, no cubic or `M2`
inhomogeneity, first old-plane inhomogeneity the quartic `C4_i(ell)` at grade
16 for `i != 6`), over the `(s,t,kappa)` base with `(s,t) != (0,0)`,
`kappa != 0`.  Desk-scale with exactly this review's machinery; the stated
frozen AWS fallback packet is well-posed.  The suggestion that the Section-8
argument reapplies one grade lower on the resulting next-rank-two subcell is
plausible but unverified here and must be treated as a fresh claim by its
producer.

## 13. Scope, nonclaims, FALLACY-v2

Formal jets are not arcs, germs, or maps; a grade-19 residual point would be
none of these.  Nothing here asserts or denies attainment, nonemptiness of
`R4-00`, exact valuations three or five, any cross-valuation periodicity or
transfer, any other support or normalization, any polynomial Keller map, any
counterexample, or JC2.  This review asserts no exit price and no
`charge_basis` (none is declared, consumed, or implied; the reviewed report
correctly declares none either).  Floor-vs-attainment, carrier typing, and
typed-`OPEN` discipline in the reviewed report are FALLACY-v2-conform; the
residual `R4-00` remains typed `OPEN`.

## 14. Review compute and firewall

Clean-room scratch confined to `/tmp/k00r402rev/` (seven stdlib-only Python
scripts; heaviest single run 6.0 s, full-row symbolic build 1.5 s, total well
under desk caps).  No Singular, no AWS job, no web request, no external model,
no `jc2-lean` access of any kind, no execution or reading of the producer
replay or any Opus run artifact.  Exactly one repository file was created —
this report; no canonical or existing artifact was edited, and no git
state-changing operation was run.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `20330`.
- Body SHA-256:
  `83ccbb0f7d03992addc429e9e630f4ec4d7b63df3b99b6f14cb64421e717a863`.
- Frozen basis: `0375694aa21fd8db3b465ef2098ca539106a1582`.
