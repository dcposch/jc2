# Hostile review: all `e=2,m=1` boundary faces and the `e=3` counterfixture

Date: 2026-08-29
Reviewer: Fable 5 (independent; producer was Sol 5.6 Ultra)
Reviewed object: `xmodel/k00-ram-e2m1-allfaces-uniformity-audit-sol56-20260829.md`
Review basis commit: `9b64db896b65e100839f6d75fbeea661cd818b9c`
Frozen specification followed: `xmodel/k00-ram-e2m1-allfaces-uniformity-hostile-review-grok46-20260829.prompt.md`
(SHA-256 `028fa0b2e78c6920b181400ea2eed04c47694400960363e685b883fa9b713d36`,
reviewer-identity and output-path overrides only; the Grok launch produced no
model work and none of it was used here).

## Verdicts

```text
All-face theorem (audit claim 1):   CONFIRM_WITH_CORRECTIONS
e=3,m=1 G8 counterfixture (claim 2): CONFIRM_WITH_CORRECTIONS
```

Every mathematical statement I tested in both claims is exactly true, and I
reproduced the load-bearing content clean-room from the 569 frozen tails with
my own parser and my own exact `Q(i)` arithmetic, not the producer engine.
The corrections are documentation-level: the new replay's `MUTATIONS=` banner
claims a control that does not exist in its code, and one described mutation
differs from the implemented one. Neither touches the truth of (0.1)/(0.2),
the fixture, or any displayed identity. I additionally close the one genuine
verification gap I found — the general-`n` framing of §4, which the replay
samples only at `n=3` (and `n=3` vs `n=4` loaded) — by proving it for all
`n>=3` from a one-line mechanism the producer did not state (§4 below).

## 0. Custody and execution boundary

All five packet pins hash exactly as charged, and every additional artifact
pinned inside the replay matches its declared digest:

```text
64eaafe3...  allfaces audit (body 13029 B, SHA 5925efef... = declared seal)
0e7f98d1...  uniform replay          2c918d5b...  exact engine
07c4ad13...  Opus G7 review (body 23079 B seal 48734eae... verified)
d72f774c...  tails.json              2ac7653c...  V20R2 compiler
66b4f59e...  corrected G7 report (body seal c9a96bd9... verified)
981b39f9...  corrected G7 replay     d453b956...  promoted G3 integration
98fb3853...  valuative comparison packet (cell definition; seal verified)
```

This session had a shell. All computation is exact rational and exact
Gaussian-rational pure-Python-stdlib arithmetic written by me; the longest
single stage ran 11.8 s; no CAS, no network, no AWS, no mod-p step anywhere.
`jc2-lean` was not inspected, listed, built, or controlled. `apply_patch` is
not exposed in this session; the deliverable was created with the harness's
single-file write, the same one-file create. Both producer replays were run
only after §1–§2 below were complete, per the specification.

## 1. Independent source and calendar analysis (attack 2, run first)

I parsed `tails.json` directly and rebuilt `R/A10/A6/A2` through the literal
normalization `C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3, C4=(3+d4)/8,
C5=d5, C6=1`. Census `569 = 36+54+58+81+89+120+131`; every monomial has
weight `12+l` under `w(C_i)=8-i, w(k10,k6,k2)=(2,6,10)`; load degree at most
one. Only afterwards did I compare with the engine: my four sector
dictionaries are **exactly equal** to `module.reconstruct_rows()`.

Normal-order stencils, reproduced: `ord_d R=(2,2,2,2,2,3,2)`,
`ord_d A10=(2,...,2)`, `ord_d A6=(1,1,1,2,1,2,1)`, `ord_d A2=(1,...,1)`; no
sector has a constant term. With `ord_t(d_i)>=1` for every `i` (the `d`
columns literally start at index 1), `ord_t(k10)=0`, and each boundary series
in `t*K[[t]]` (any positive order or the zero series), the literal first
possible `t`-grades at `e=2` are

```text
R rows 1-5,7: 2   row 6: 3            t^4 k10 A10: all rows >= 6
t^12 k6 A6: rows 1,2,3,5,7 >= 14, rows 4,6 >= 15
t^20 k2 A2: all rows >= 22
targets: mu2 >= 29 (row 2), mu4 >= 33 (row 4), mu6 >= 37 (row 6), Jdet = 38 (row 7)
```

matching the valuative packet's table row for row, and the audit's (2.2) as
lower bounds. The uniform inequality `min arrival of K6/K2/targets > 2e+3`
holds for every `e` in `2..99` (recomputed).

**Face identity, proved.** For every boundary load-order face — any exact
orders `h6,h2,hmu2,hmu4,hmu6 in {1,2,...} cup {infinity}` — the grade-`g`
equations for `g<=13` are the *same polynomials* in `{d_i[1..g], k10[0..]}`:
the five boundary series' variables first occur at grade 14 or later, so
faces differ only in constraints on variables absent from G0–G7. I verified
this both by the stencil argument and by a bidirectional numeric control: two
deterministic pseudorandom Gaussian-rational assignments sharing `d,k10`,
one with all five boundary series order-1 units and one with all five zero,
produce identical grades 0–13 and first diverge exactly at G14 in rows
1,2,3,5,7 (at `e=3`: identical 0–19, diverging at G20). The opens: every
face's constructible set is contained in
`V(G0..G7) cap D(k10[0]) cap (union_i D(d_i[1]))`
because each face keeps the `m=1` and `k10`-unit opens, and its extra
exact-order opens only shrink the set. The exact-order faces partition the
stratum `k6,k2,mu2,mu4,mu6 in t*K[[t]]` completely, so stratum emptiness and
all-face emptiness are equivalent. The audit's corollary logic is exactly
right, including dropping the late exactness opens.

**Units and field/Kummer extensions.** `C6=1` comes from the licensed
weight-2 Kummer extension `a(t)^2 C6(t)=1`; `a=C6^{-1/2}` exists after at
most a quadratic residue-field extension by Hensel in characteristic zero,
and since `a(t)` is a unit acting through the weight grading, every displayed
order, boundary condition, and face label is unchanged — the normalization is
face-uniform, so the corollary inherits it verbatim. `Lambda=t^e` costs an
`e`-th root of a unit, same argument. `k10` and `Jdet` units are forced by
the generic-ray localizer `H=B:(C6*k10*Jdet)^infinity`; `k10[0]!=0` is
load-bearing (twice, below); the `Jdet`-unit hypothesis is *nowhere used* by
the G0–G7 kill and rides along only as part of the cell definition. The two
rank-one charts need `i`; emptiness is proved over an algebraic closure,
which dominates every licensed extension and descends to every subfield.

## 2. The all-face theorem: proof audit and fresh recomputation (attack 3)

The theorem is a corollary with exactly three inputs: (a) the corrected G7
certificate's emptiness of `V(G0..G7) cap D(k10[0]) cap (D(s) cup D(t))` for
the `B11111` cell; (b) the calendar/face-identity lemma of §1; (c) the fact
that (a)'s proof consumes no K6/K2/target coefficient, equation, or open.
Opus confirmed (a) and (c) (`CONFIRM_WITH_CORRECTIONS`, C1–C8 all
incorporated in the audit body: `mu` and `nu2` are now displayed at (2.4a),
and the post-G3 open identification follows (2.6)). I did not defer to that:
I freshly recomputed the **entire** kill chain from my own parse, loads
carried literally with symbolic `k10[0]=k, k10[1]=k1`:

* G2 rows are the quadrics `Q_r(d[1])`; `Q_6=0`; `Q_r(cone(a,b,p,q))=0`;
  `Q_r in (A,B)` by direct substitution, and the cone parameterization
  inverts, so `V(Q)=V(A,B)` exactly; `A*B` in the `Q`-span, `A^2,B^2` not,
  `A^3,B^3` in the degree-3 piece — the nonreduced-cone/radical usage is
  point-set only, exactly as claimed.
* G3 spot-kill: on `d[1]=ell(s,t)+rT(p,q)`, row 6 on the rank-one charts is
  the unit `eps*i*q^3/32`, and at `p=q=0` all seven G3 rows vanish for
  arbitrary `d[2]` — the promoted reduction's decisive facts, re-derived.
* First fan: `G4_r = Q_r(d[2]-nu2)` exactly; G5 rows are
  `alpha_r X + beta_r Y + N_r` with the printed `alpha,beta`; the (3.3)
  determinant `(27/2^35)Delta*C`, row 4 `(3/2^15)E`, and all three syzygies;
  the `(s,t)`-determinant of `(C,E)` is `-Delta^2` (rank-2 kill); the
  rank-one survivor is exact at G5 and dies at G6 by
  `(-q^3/16, eps*i*q^3/32, q^3/128)`; the rank-zero branch has all seven G5
  rows identically zero.
* Second fan: `G6_r = Q_r(d[3]-nu3)` with arbitrary `d[4]` and arbitrary
  `k10`; G7 rows are free of `a,b,c,d` and of `k10[1]` (the latter because
  `[t^2]A10(d)=M4(d[1])` and `M4(ell)=0` — I verified the polar facts and the
  erratum identity `A10^[3](ell) = -(1/2)DM4(ell)[mu]`, which is (2.4));
  rank-2: load cancels from the determinant and row 4, `-Delta^2` again;
  rank-1: `G7_2+(eps*i/2)G7_1 = -eps*(5i/16)*k10[0]*t^3` on both charts;
  rank-0: `G7 = k10[0]*W` with `W_1,W_2` as (2.6), `W_4=W_6=0`,
  `W_3,W_5,W_7` proportional to `W_1`, and `(0,0)` the only common zero.

Every branch matches the audit's (2.3)–(2.6). The unloaded surface identity
`R_r(D(S,T))=0`, the `16T^2 -> 15T^2` mutation (breaks six rows), the `J^2`
containment (3.3) in graph coordinates, the sector minima (5.1), and the
leading restrictions (5.2) including the total row-4 exception all check.
The `union_i D(d_i[1]) = {(s,t)!=(0,0)}` identification is exact
(`s=d2[1], t=d3[1]`). A formal solution would restrict to a G0–G7 point in
the proven-empty constructible set, and the 273-equation grade-38 face cells
contain G0–G7 verbatim, so both the formal and every truncated face cell are
empty. **The theorem is exactly true at its stated scope.**

## 3. G7 dependency inventory (attack 4)

Mathematically consumed by the G0–G7 kill, for every face:

* **Sectors.** `R` and `A10` only, with `k10[0]` the only load coefficient;
  `k10[1]` appears in G7 only against `M4(ell)=0`. No `k6, k2, mu2, mu4,
  mu6, Jdet` coefficient, equation, or open (§1 proves their variables are
  absent below G14).
* **Rows.** Row 6 is decisive at G3 (unit `eps*i*q^3/32`); post-G3 the kills
  use rows `{1,2,3,4}` (both rank-2 branches), `{1,3,5}` (G5-rank-1 at G6;
  rows 6 and 7 give redundant second kills), `{1,2}` (G7 rank-1 and rank-0).
  Rows `{1,2,3,4,5}` suffice after G3, confirming Opus C3; all seven stay in
  the serialization.
* **Opens.** `D(k10[0])` used exactly twice (G7 rank-1 terminal, rank-0
  `kW`); `union_i D(d_i[1])` used at both rank-2 kills and as `t!=0` on the
  rank-one charts. `D(Jdet[0])` and all five exact-order opens: unused.

**Custody vs verification in the new replay.** Freshly recomputed in-run:
surface/`J^2`, all sector restrictions (the K6/K2 quadric/linear leading
forms are now exercised — an improvement over the G7 replay, whose
assertions covered only `R` and `A10` per Opus C8; my harness confirms a
perturbed `A6` or `A2` coefficient now fails closed), the stable fan and
rank-one cokernel with survivor at `n=3`, the e=3 fixture, the loaded final
fan at `n=3` and `n=4` with all three terminal identities, and the calendar
loop. Custody-only (hashed, never recomputed there): compiler, G3 promotion,
G7 report, G7 replay, Opus review. In particular the **first fan (G4 cone,
G5 kills, G5-rank-1's G6 kill) and the G3 reduction are inherited, not
recomputed, by the new replay** — the audit says so honestly ("corollary of
those reviewed facts... review-gated in its enlarged scope"). After my §2
recomputation, every load-bearing link now has two independent
different-model recomputations.

## 4. The stable claims: from sampled to proved (`n>=3`)

The replay realizes the grade-`2n+1` fan and the grade-`2n+2` rank-one
cokernel only at `n=3` and checks the loaded final fan only at `n in {3,4}`,
while audit §4 and the banner `...SHIFT_INDEPENDENT_FOR_N_GE3` speak of all
`n>=3`. I close this gap rather than just flagging it.

**Gradient lemma (new, verified exactly).** Each `R_r` lies in `J^2` (§2),
hence all 42 compositions `(dR_r/dd_i)(D(S,T))` are the **zero polynomial**
in `(S,T)` — I computed them; all vanish identically. Consequently, for
*every* surface prefix `d0(t)=D(S(t),T(t))` and every constant direction
`c`, `DR(d0(t))[c] = 0` identically: single-deviation contributions vanish
at every grade. This is the one mechanism behind `DQ(ell)=0`, the
`a,b,c,d`-freeness of G7, and the absence of `d[7]` from G9 (§5).

**Census.** With deviations `w@n, newest@n+1, z@n+2` and a quadratically
truncated surface prefix, a term at grade `2n+1` or `2n+2` with at least two
deviation factors has deviation grade-sum `>= 2n`, forcing its surface
cofactors into grades `<= 2`. Pure-surface terms vanish
(`R(D(S,T)) = 0`), single-deviation terms vanish (lemma), and three
deviations overshoot. So for **every** `n>=3` the fan and cokernel have
literally the same contribution shapes with the same coefficient objects:

```text
grade 2n+1: (1/2)D^2C3(ell)[w,w] + DQ(w)[newest]
grade 2n+2: DQ(w)[z] + Q(newest) + D^2C3(ell)[w,newest]
            + D^2C3(d0[2])[w,w]-polar + (1/2)D^4C4(ell,ell)[w,w]-polar
```

with `d0[2]` carrying the second surface coefficients `alpha,beta` — the
same for all `n`. The K10 load at grade `2n+1` with `e=n-1` is
`k10[0]*[t^3]A10(d) = k10[0]*(1/2)DM4(ell)[mu] = kW` for every `n>=3` (the
transverse block cannot reach grade 3, and `k10[1]` meets `M4(ell)=0`). I
also directly verified the unloaded fan at `n=5` equals the `n=3` fan.
So the banner and §4's general-`n` display (4.2) are **true and now proved**,
not merely sampled. The audit's (4.2)/(4.3) themselves: recomputed exactly at
`n=3`, both signs — the `512/640` brackets, `y/z`-freeness of the two
combinations, the `alpha=beta=0` clash `128t^2q^2` (the false induction),
and the survivor `X=eps*24i*tq, alpha=-4t^2, beta=0` killing both forms.

## 5. The `e=3,m=1` fixture (attack 5)

I substituted the displayed fixture into the **full literal `e=3` source**
with my own evaluator: `R(d) + t^6*k10*A10(d) + t^18*k6*A6(d) +
t^30*k2*A2(d) - targets` at their literal shifts `42/48/54/57` and signs
`(-1,-1,-1,-1/4)`, with `k10=Jdet=1` and the five boundary series carried
literally as zero series in the code path. With
`S=8i*t-4t^2, T=t, d=D(S,T)+t^3w+t^4v+t^5z` as displayed:

* All seven full rows vanish in G0–G8 — 63 exact `Q(i)` coefficients.
* `ord_t(d)=1` (`d[1]=ell(8i,1)!=0`), `k10,Jdet` units, all boundary
  conditions hold; the chart data are consistent:
  `w=cone(0,0,8i,1)` (`p=8iq`, `eps=+1`), `A(v)=X=24i`,
  `B(v)-8i*A(v)=-320+192=-128=-128tq`, and `C3/C4` brackets evaluate to
  `576-512-64=0` and `576-640+64=0`.
* The K10 sector's first nonzero grade on the fixture is exactly **G9**
  (rows 1,2,3,5,7), as claimed: `[t^8]` meets `M4(ell)=0`.
* A unit `k6` order-1 series first changes any row at **G21**, matching the
  audit's surface-restricted calendar `nu6=6e+h6+2m=21` and empirically
  separating it from the raw stencil floor G20 — the (5.3)/(5.4) table's
  conditional status is exactly right (its resonance-wall arithmetic and the
  §6 tie examples `e=2,m=9` and the `m=2e` wall also check by hand).
* **Mutations.** The propagated mutation the audit describes — `S`'s
  coefficient `-4 -> -3` pushed through `D(S,T)` — fails **exactly and
  only** at G8 (rows 1–5,7), as does propagated `alpha=0`; this is the
  sharpest possible old-pass/new-fail pair for the cokernel grade, and it is
  the honest content of "disappears if one incorrectly sets the second
  surface coefficient to zero". The replay instead mutates only the `d4[2]`
  slot without propagation, which already breaks G4–G7 in some rows; its
  guard samples G8 only and does fire. See correction F2.

**G9 observation (beyond the charged claims, decides nothing).** Freezing
every displayed fixture coefficient, G9 is linear in `(d[6],d[7])`;
`d[7]` does not occur at all (gradient lemma at the grade-2 prefix), the
`d[6]` block factors through `(A,B)` with rank exactly 1 on the isotropic
chart, and rows 4 and 6 are forced constants `-51i/32` and `i/32` — row 6's
value being the familiar reactivated `eps*i*q^3/32` unit. So **this
particular G8 jet does not extend to G9 with the retained block frozen**;
any G9 carry must move `alpha,beta,X`, the `v`-directions, or the lift
fiber, which is precisely the audit's ranked next cell 1 and makes its
"retain everything; `alpha=0` forbidden" design necessary, not optional.
This sharpens, and is fully consistent with, `G9_UNDECIDED`; it is not a
cell verdict, and I draw none.

## 6. What the fixture refutes (attack 6)

Exactly this: any induction or theorem asserting that the `e=3,m=1`
generic-ray equations G0–G8, with all five boundary series zero and
`k10=Jdet=1`, are inconsistent — in particular the coefficient-blind
recentering induction that discards the second surface coefficients and
kills the stable rank-one branch at grade `2n+2` via the `128t^2q^2` clash.
It does **not** refute: the `e=2` all-face theorem (different `e`; its kill
uses the G7 load arrival, which at `e=3` moves to G9); the reviewed G7
certificate; the promoted G3 reduction (the fixture's `d[1]` is on the
`ell`-plane, consistent); or any promoted ledger claim. No such stronger
theorem exists in the ledger to threaten. The fixture is a finite G8 jet: it
is not an arc, not a formal or algebraic solution, not Taylor-realizable
data, not a map, and proves no G9 lift — the audit's own scoping (§4, §7)
says exactly this and my G9 probe underlines it.

## 7. Replay execution and control audit (attack 1, run last)

```text
python3 -B    uniform replay -> PASS, 2.1 s
python3 -B -O uniform replay -> PASS, byte-identical output
python3 -B / -B -O G7 replay -> PASS, byte-identical (2.9 s)
```

Banner, `CERTIFICATE_BYTES=3910`, and
`CERTIFICATE_SHA256=afd1bf52...` match the audit's §1 exactly; the
certificate is rebuilt in memory and not written; there are zero bare
`assert` statements in the replay and engine, so `-O` is not vacuous; the
engine import is hash-gated before `exec_module` and `__main__`-guarded.
My mutation harness (patching `reconstruct_rows` below the custody gate):
perturbing `R` row 1/7, `A10` row 1/2, `A6` row 1, `A2` row 1 each fails
closed (`surface row`, `K10 surface cubic`, `surface sector minima`,
`K2 surface linear`). All four sectors are exercised by in-run assertions.

**F1 (material, documentation).** The printed line
`MUTATIONS=CUSTODY,SURFACE_16_TO_15,K10_CUBIC,STABLE_640_TO_639,E3_SURFACE_COEFF,FINAL_SHIFT`
overstates the control set. Only `SURFACE_16_TO_15`, `STABLE_640_TO_639`,
and `E3_SURFACE_COEFF` are fired in-run negative controls. `CUSTODY` is a
fail-closed hash gate with no executed vacuity control (the engine's lives
behind its own `__main__`); `FINAL_SHIFT` is the positive `final3==final4`
equality assertion; and `K10_CUBIC` has **no corresponding code in this
replay at all** — it appears inherited from the G7 replay's genuine
`OMIT_A10_CUBIC` control. The cubic is still verified positively (the final
fan's expected value contains it, and my §2 recomputation confirms the
corrected load), so nothing mathematical is at risk; but a banner naming a
nonexistent control is exactly the pattern Opus flagged as C3/C7 on the
predecessor replay, now recurring.

**F2 (minor).** Audit §4's "changing the coefficient `-4` in `S` to `-3`
makes G8 nonzero" describes the propagated mutation (verified: fails exactly
at G8); the replay implements an unpropagated `d4[2]` edit that also breaks
G4–G7. Both fire; the prose and code should name the same object.

## 8. Coverage and noncoverage (attack 6, scope)

Proved here, and only here: for `Lambda=t^2`, `ord_t(d)=1`, `C6=1`,
`ord_t(k10)=ord_t(Jdet)=0`, over an algebraic closure in characteristic
zero, the whole boundary stratum `k6,k2,mu2,mu4,mu6 in t*K[[t]]` — hence
every exact load-order face, including all infinite/zero-series faces —
satisfies `V(G0..G7) cap D(k10[0]) cap (union_i D(d_i[1])) = empty`, so
every truncated grade-38 face cell and the formal cell are empty.

Not covered, by anything in this packet or this review: `m>=2` (the
lexicographically next transverse valuation `e=2,m=2` is open), the `C6=0`
tip, `k10=0`, `Jdet=0`, any `e>=3` cell (the rank-one carry is open at G9),
other K00 supports or load rays, positive characteristic, scheme structure
or multiplicities (point-set only), jet lifting beyond G8 at `e=3`, arcs,
Taylor/algebraic/rational/polynomial realizability, Keller pairs,
counterexamples, attainment, Gate T, order two, maximum twelve, and JC2.
Floors are not attainment anywhere in this packet, and none of its lower
bounds are read as exact orders.

## 9. Correction register

| id | severity | where | correction |
|---|---|---|---|
| F1 | material (documentation) | replay banner / audit §1 quote | `MUTATIONS=` lists `K10_CUBIC` (no such control exists in this replay), `CUSTODY` and `FINAL_SHIFT` (checks, not fired mutations); only 3 of 6 entries are in-run negative controls. Append an erratum line at promotion; no code or seal change. |
| F2 | minor | audit §4 vs replay `e3` mutation | described mutation is `S` propagated (fails exactly at G8, verified); implemented mutation is unpropagated `d4[2]` (also breaks G4–G7). Both fire. |
| F3 | resolved upward | audit §4 / `N_GE3` banner | general-`n` fan/cokernel claims were sampled at `n=3` (and `n=3,4` loaded); now proved for all `n>=3` via the gradient lemma `R in J^2 => grad R|_D = 0` and the deviation-grade census (§4). Worth banking as the reusable mechanism. |
| F4 | observation | §5 | frozen-fixture G9 is inconsistent (rank 1 vs 2; rows 4,6 forced constants; `d[7]` absent); the G9 carry must vary the retained block. Confirms and sharpens `G9_UNDECIDED`; no cell verdict. |
| F5 | note | (0.1) | the `Jdet`-unit hypothesis is unused by the kill (cell-definition only); `k10[0]!=0` is used exactly twice; `C6` unit is consumed by the face-uniform Kummer normalization. |

None of F1–F5 changes the truth value of either charged claim.

## 10. Promotion recommendation

```text
PROMOTE claim 1 at EXACT / POINT-SET-EMPTY, all-face scope, conditional on
a one-line F1 erratum accompanying the AUDIT.md entry.
BANK claim 2 at EXACT / FINITE-G8-JET as a refutation of the named
coefficient-blind induction only; it licenses no cell, arc, or lifting
statement and must remain a mandatory old-pass control (with the propagated
mutation of F2 preferred) for the e=3 G9 rank-one-carry lane.
```

Exact scope to record for claim 1, and nothing beyond it:

> For the normalized generic K00 ray at `Lambda=t^2`, `ord_t(d)=1`, `C6=1`,
> `ord_t(k10)=ord_t(Jdet)=0`, over an algebraic closure in characteristic
> zero: for every choice of `k6,k2,mu2,mu4,mu6 in t*K[[t]]` (arbitrary
> positive orders or zero series),
> `V(G0,...,G7) cap D(k10[0]) cap (union_i D(d_i[1])) = empty`; hence every
> boundary load-order face of the `e=2,m=1` cell, truncated or formal, is
> empty.

By-products worth banking from this review: the gradient lemma with its
census (F3), which upgrades every "stable/shift-independent" statement in
the packet to a theorem and explains `DQ(ell)=0`, the `a,b,c,d`-freeness of
G7, and the `d[7]`-absence at G9 from one containment; and the G9 probe data
(F4) as a fixed signpost for ranked next cell 1.

No new exit-price assertion is made anywhere in this review, so per
`FALLACY-v2.md` no `charge_basis` line is declared; adding one would be a
false declaration.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22894`.
- Body SHA-256:
  `57de629f083c4d2f7316726cd433d9ac9520a6836a2b478635587f0a79e49205`.
- Frozen basis: `9b64db896b65e100839f6d75fbeea661cd818b9c`.
