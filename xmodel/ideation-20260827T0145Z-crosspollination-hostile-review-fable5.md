# Hostile review + alternate adjudication — cross-pollination memo `20260827T0145Z` (Fable 5)

Lane: Fable 5, different-model hostile reviewer and alternate
cross-pollination adjudicator.
Date: 2026-08-27.  Repo `/Users/dc/code/math/jc2`, charged HEAD
`418e413593120d19e15e6546eb50c985f4b1f038`, dirty concurrent worktree
(pre-existing modifications and untracked case directories were left
untouched; the only repository file written is this one).

Target, rehashed before reading:

```text
c16cca5ca7aa72d7bc8eb83bc2ba2d9982bae59e251c35c1fb3ae472c095e65a
  xmodel/ideation-20260827T0145Z-crosspollination-opus5.md          MATCH
```

All four blind submissions, the four charged post-memo artifacts, the
prefix-zero-sections review `959603e3…`, and the unit-`k10` filing review
`678a087d…` were rehashed and match their pinned values.  All 22 frozen
exact-`Q` rows were rehashed against the direct-certificate report's §9
manifest and reparsed from bytes: 22/22 match, term counts
`4,5,5,2,5,0,5 | 12,14,17,3,18,0,18 | 27,36,47,12,58,9,60 | 304`,
`Tg10_6 = Tg11_6 = 0`, every `rho` exponent even.  Per instruction, the
promoted direct `T-cs` certificate (`7af66e58…`/`f16e1114…`, plus the
independent Fable review `c9abdce7…`, both verdict CONFIRMED) and the
promoted `J1=0` census (`bedb8dfe…`) are treated as charged and are not
re-proved wholesale here.

Method: exact sparse `fractions.Fraction` arithmetic on the frozen bytes;
integer nullspace by exact Gaussian elimination; exact arithmetic in the
degree-8 algebra `Q[w,s]/(w^4+1, s^2-5/12)`; three modular replays.  Twelve
short scripts under `/tmp/fx0827/` (not committed), SHA-256:

```text
a8da2a7f polylib.py   84a7a940 grading.py   1cc158d7 jet.py
514f6dea core.py      c4db328b diag.py      1076c3f2 diag2.py
aa7f7c7d point_mod3.py bd686ec6 point_char0.py e2738743 alg.py
f7afe0d3 v20eval.py   7e893263 probe136.py  6570a8fc loadunit.py
```

No web, no AWS read or mutation, no launch, no `jc2-lean`, no Groebner or
CAS.  Everything below marked **VERIFIED-HERE** is producer-tier from this
lane and itself needs different-model review before promotion.  Model
agreement is not treated as evidence anywhere in this report (§10).

---

## 0. Verdict table

| # | Memo claim | Verdict |
|---|---|---|
| 1a | Grading lattice of the 22 frozen rows has rank exactly 2 (40 vars, 641 constraints) | **CONFIRMED** (recomputed: rank 38 matrix, nullity 2) |
| 1b | `deg_s` table over all 40 names; all weights `>= 0`; `deg_s(Tg{g}_j) = g` | **CONFIRMED**, byte-identical table |
| 1c | Any lattice element with `g(rho)=0` is proportional to `deg_s`; hence no grading with `g(rho)=g(cs)=0` | **CONFIRMED** (kernel of the `rho`-functional is rank 1; `deg_s(cs)=2`) |
| 1d | opus5 blind `deg_2` refuted; `Tg12_2` spectrum `{0,1,2,3}`, `Tg14_5` spectrum `{0,1,2,3,4}` | **CONFIRMED** (13 of 20 nonzero rows inhomogeneous; both spectra exact; also fails with `e0↦1` variant) |
| 1e | Withdraw opus5 §3.4's `M >= 1` **proof** | **CONFIRMED** |
| 1f | "… the `M >= 1` V19 acceptance gate would have been unsound" | **REFUTED** — the gate is sound; `M >= 1` is true with a promoted-tier proof via `CS0` (§2.3) |
| 1g | Surviving `deg_s` bound `2N+4M >= 14` (`N+2M >= 7`) and the nonzero-`Tg14_5`-cofactor gate | **CONFIRMED** (with the `qrs,qc0,qc1` weight extension `0,3,3` made explicit) |
| 2a | Jet identity `Tg11_j = D(Tg10_j) - ell1*d_p(Tg10_j) + k*R_j`, `R_j ∈ (c0,c1)`, all `j=1..7`; displayed `R_1`, `R_4` | **CONFIRMED**, exact, residuals ≤ 2 terms each |
| 2b | Shifted-core table, `V(k)` and `V(J1)` columns (four shapes each) | **CONFIRMED** as shapes; **the printed `e0e1` cofactor is wrong by a factor 2** in both columns — correct combination is `(16/3)(Tg12_3-(p/2)Tg12_1) + (8/3)*ell1*Tg11_1` (§3.2) |
| 2c | `Tg14_5\|_{J1}` load `= -(5/128)a0a1k rho^4` "plus `cs1`-weighted corrections", "dies on `qa1=0`" | **GAP as stated** — corrections lie in `(cs1,cs2,rs1,rs2,e0,e1)`, not `(cs1)`; the load does **not** die at `a1=0` alone; the `H3` negative control survives independently via promoted `A00`/`A10` (§3.3) |
| 3a | Delayed-load point: three modular points kill all 22 rows at `k=0`, `cs*k1*rho != 0` | **CONFIRMED** — all three replays exact (§4.1) |
| 3b | Characteristic-zero status of that point | **GAP in the memo, DISCHARGED HERE**: exact point constructed in `Q(zeta_8, sqrt(5/12))`, displayed in §4.2; the memo's three primes are its residue shadows (one embedding reproduces the `F65521` point digit-for-digit) |
| 3c | Consequence: no `cs^a k1^b rho^c ∈ I + (k)` from the frozen 22 rows | **CONFIRMED over `Q` unconditionally**, given §4.2 (no longer only for `p`-integral cofactors) |
| 3d | Consequences 2–5 of memo §4.3 (fable5 counter-witness, opus5 Card B, grok Card B, sub-fan scope) | **CONFIRMED**, with the sharpening that opus5 Card B's payoff branch was already dead via promoted `CS0` alone (§4.3) |
| 3e | Post-memo collision: does §4.3 extend past the frozen 22? | **NO** — V20 returned; 13 of 14 new grade-13/14 rows are nonzero at the point, and `Tg13_6` supplies a grade-13 load unit killing the delayed-load sub-fan (VERIFIED-HERE identity, §4.4; conditional on unreviewed V20 bytes) |
| 4 | Torsion-multiplier lemma + promoted fibre theorem + reviewed grade-10 membership ⟹ some `cs^N k^M` in the honest total ideal, without branch (b) | **CONFIRMED**, existence-only exponents; every link now promoted or elementary; `rho`-parity improves the memo's `(6N+6, 6M+2)` to `(3N+6, 3M+2)` (§5) |
| 5a | fable5 Lemma A (Rabinowitsch clearing) | **CONFIRMED** (and now recorded at promoted tier as clause (C) of the converse-correction memo) |
| 5b | fable5 Lemma B endorsed as a biconditional; its E-gate inference refuted for two reasons | **CONFIRMED** (one normal-form caveat on the ⇐ direction, §6.2) |
| 5c | fable5 §3.4 `k=0` mechanism a ring/scope error; conclusion survives otherwise | **CONFIRMED**; the surviving reason is `CS0`/`A00`/`A10` plus §4.2; V20 further splits the conclusion (§6.3) |
| 6a | Memo §1 deduplication (11 mechanisms) and §1.3 adjudications | **CONFIRMED at navigation tier**, two annotations (§7.1) |
| 6b | Memo §5–§7 ranked decisions and routing | **PARTIALLY OVERTAKEN** — direct-certificate reviews returned CONFIRMED and V20 launched and returned on Box02/r6d; alternate top-five in §7.3 |

Two arithmetic defects found in the memo (1f, 2b) and two scope repairs
(2c, 3b).  No load-bearing conclusion of the memo falls; one memo decision
(drop the `M >= 1` gate) should be reversed.

---

## 1. Custody detail

`shasum -a 256` matches for: the memo; `ideation-20260827T0145Z-{root,grok,fable5,opus5}.md`
(`2b47b800…`, `08c69fd2…`, `1a65cb78…`, `60e19803…`); the direct-certificate
producer `7af66e58…`; its Grok review `f16e1114…` and Fable review
`c9abdce7…` (both verdict **CONFIRMED**, both independently reconstructed
Lemma 0 and branch (a), so the memo's §7.1 worry that reviewers would burn
budget on branch (b) instead of Lemma 0 was resolved by the reviews
themselves); the `J1=0` review `bedb8dfe…`; the zero-sections review
`959603e3…`; the `k10` filing review `678a087d…`.  The 22 row files hash to
the §9 manifest of the producer report; `Tg14_5_q.poly` = `91d96924…` =
V17 `RESULT.json` `coefficient_sha256`.

Post-memo state consulted (read-only): promotion files for the direct
certificate and the `J1=0` census; the V20 case
`cases/max12_812_order2_p0_total_rees_allrows_g13_g14_export_v20_20260827`
(launched `02:43:18Z` on Box02/Q and r6d/F65521 per `HARVEST_CUSTODY.md`,
both returned `PASS-TOTAL-REES-ALLROWS-G13-G14-EXPORT-V20`, harvested,
**no different-model review yet**).  A Grok review of the memo's algebraic
claims is queued (`…-crosspollination-algebraic-claims-review-grok-prompt.md`
exists; no report yet).

---

## 2. Item 1 — the grading lattice, recomputed

### 2.1 What the frozen 22 rows prove  [VERIFIED-HERE]

From the reparsed bytes: 40 variables, 661 monomials over 20 nonzero rows,
hence exactly `661 - 20 = 641` pairwise homogeneity constraints — the
memo's stated matrix.  Exact Gaussian elimination gives constraint-matrix
rank **38**, so the grading lattice has rank **2**.  The sublattice
`{g : g(rho) = 0}` is rank **1**; its generator, normalized by
`g(cs) = 2`, is integral, nonnegative, and reproduces the memo's §2.1
table **exactly**, all 40 names:

```text
0: rho | 1: ell1 | 2: cs, ell2, rs | 3: cs1, ell3, rs1
4: cs2, ell4, k, rs2 | 5: a0, a1, c0, c1, cs3, k1, rs3
6: aa0, aa1, cs4, e0, e1, k2c, rs4 | 7: aaa0, aaa1, ee0, ee1, k10_3
8: ac3, az3, ec3, ez3, k10_4 | 9: ac4, az4, ec4, ez4
```

`deg_s(Tg{g}_j) = g` holds for all 20 nonzero rows.  Since the
`g(rho)=0` sublattice is one-dimensional and `deg_s(cs) = 2 != 0`, **no
nonzero grading of the 22-row set has `g(rho) = g(cs) = 0`**.  opus5
blind's `deg_2` requires exactly that (plus `g(k)=2`), so `deg_2` does not
extend: with unassigned names at weight 0, the spectra are
`Tg12_2 : {0,1,2,3}` and `Tg14_5 : {0,1,2,3,4}` as the memo displayed, and
13 of the 20 nonzero rows are `deg_2`-inhomogeneous (all grade-11/12/14
rows except `Tg12_6`; the variant `e0 ↦ 1` fails identically).  Memo §2.4's
refutation and its concrete witnesses are **CONFIRMED**.  A second lattice
generator, for the record (times 3, `g(rho) = 3`): it takes negative values
(`k: -2`, `k2c: -6`, `cs3: -1`, …), so `deg_s` is, up to scale, the only
nonnegative grading with `g(rho)=0`.

**Scope, stated exactly.**  These are theorems about gradings that make the
22 frozen polynomials homogeneous.  They say nothing about unexported rows
(the V20 grade-13/14 rows are *not* in the constraint matrix — though I
checked separately that `deg_s` extends verbatim to grades 13–14 in the
sense that the jet map below raises it by one), the full source ideal, or
any other presentation.  "`deg_s` is the sigma-order" is an interpretation
supported by the tower pattern; the table itself is the theorem.

### 2.2 The surviving bound, with its missing hypothesis made explicit

Memo §2.4's surviving gate needs `deg_s` on the three chart ratio
variables.  The bilinears force `deg_s(qrs)=0`, `deg_s(qc0)=deg_s(qc1)=3`,
all `>= 0`, and then every generator of the honest `K` is
`deg_s`-homogeneous.  Extracting the `(2N+4M)`-component of a certificate
identity and reducing mod `rho`, the promoted nonempty grade-10–12 prefix
fibre forces a nonzero `Tg14_5` cofactor of degree `2N+4M-14 >= 0`.  Both
the `N+2M >= 7` bound and the nonzero-`Tg14_5`-cofactor acceptance gate are
**CONFIRMED** sound.  (With the V20 grade-13 rows admitted as generators
the bound weakens only to `2N+4M >= 13`, i.e. the same `N+2M >= 7` over
`Z`.)

### 2.3 Where the memo overreached: the `M >= 1` gate is sound

The memo withdraws opus5 §3.4 (correct — its proof is `deg_2`-based) **and**
declares the `M >= 1` V19 acceptance gate unsound.  The second half is
wrong.  Evaluate any putative certificate
`cs^N * k^M * (1 + rho*W) ∈ K` at the **promoted** `CS0` section
(`cs=1, k=0`, all other source names `0`, `rho` free, extended by
`qrs=qc0=qc1=0`): every generator of `K` maps to `0` in `Q[rho]`, while at
`M = 0` the left side maps to `1 + rho*W(CS0)`, a polynomial with constant
term 1.  Contradiction; hence `M >= 1` — a one-line consequence of the
zero-sections promotion `959603e3…`.  The same argument with `RS0`
(`rs=1, k=0`, rest `0`, `rho` free — **VERIFIED-HERE**: `RS0` kills all 22
rows, and also all 14 V20 rows, and is compatible with the `T-rs`
bilinears at `qcs=qc0=qc1=0`) gives `M >= 1` on the `rs` chart.  So opus5
§3.4's *conclusion* is true on both charts by a different, promoted-tier
reason; only its proof dies.  **Adjudication delta: keep the `M >= 1` gate
in the typing tool, with `CS0`/`RS0` provenance replacing `deg_2`.**  The
gate is fail-safe (no genuine certificate can violate it) and still catches
mis-typed harvests.

---

## 3. Item 2 — the jet-shift identity and the shifted cores

### 3.1 The seven-row identity  [CONFIRMED, exact]

With `D` the stated jet derivation (`cs↦cs1, rs↦rs1, k↦k1, c0↦e0, c1↦e1,
a0↦aa0, a1↦aa1, ell1↦ell2, rho↦0`, one further step on each tower — for
grade 10→11 only the first steps act) and `p := rho^2`:

```text
Tg11_j - [ D(Tg10_j) - ell1 * d(Tg10_j)/dp ]  =  k * R_j ,   j = 1..7
```

holds exactly on the frozen bytes, with every residual in `k*(c0, c1)`:

```text
k*R_1 = (5/16)c0*cs*k + (5/64)c1*k*rs          (matches the memo display)
k*R_2 = (5/64)c0*k*rs + (5/16)c1*cs*k*rho^2
k*R_3 = rho^2 * [ (5/32)c0*cs*k + (5/128)c1*k*rs ]
k*R_4 = 0                                       (matches)
k*R_5 = -rho^4 * [ (5/128)c0*cs*k + (5/512)c1*k*rs ]
k*R_6 = 0
k*R_7 = rho^6 * [ (5/256)c0*cs*k + (5/1024)c1*k*rs ]
```

Verdict per claim: definition of `D` — CONFIRMED (well-defined on the names
occurring in grade-10 rows; no tower end is hit); rows `j=1..7` —
CONFIRMED each; displayed `R_1`, `R_4` — CONFIRMED.  The `deg_s`
explanation (D raises `deg_s` by one, `d/dp` preserves it) is consistent
with §2.1.

### 3.2 Shifted cores: shapes CONFIRMED, one printed cofactor REFUTED

`V(J1)` (`rs=cs=c0=c1=0`), exact:

```text
(8/3)Tg11_1|  = a0e1 + a1e0            CONFIRMED
(8/3)Tg11_2|  = a0e0 + p a1e1          CONFIRMED
(32/3)Tg12_4| = e0^2 + p e1^2          CONFIRMED
(16/3)(Tg12_3 - (p/2)Tg12_1)| + (8/3)*ell1*Tg11_1| = e0e1     CONFIRMED
```

The memo prints the last cofactor as `(1/2) ell1 (8/3) Tg11_1`, i.e.
`(4/3)ell1*Tg11_1`; as printed the identity is **REFUTED** (residual
`a0e1ell1 + a1e0ell1`).  The correct coefficient is `(8/3)ell1`
(equivalently `(1/2)ell1` against `(16/3)Tg11_1`).  The **same factor-2
correction** applies to the `V(k)` column.  With it, the full `V(k)`
column (`T-cs` chart, `rs=c0=c1=0` collapse, `k=0`) is exact:

```text
(8/3)Tg11_1|  = a0e1 + a1e0 + (5/6)cs^3*k1*p                       CONFIRMED
(8/3)Tg11_2|  = a0e0 + p a1e1                                      CONFIRMED
(16/3)(Tg12_3 - (p/2)Tg12_1)| + (8/3)ell1*Tg11_1|
              = e0e1 - 2cs(a0^2 + p a1^2)                          CONFIRMED
(32/3)Tg12_4| = e0^2 + p e1^2 - 8 p cs a0a1                        CONFIRMED
```

So the memo's structural claim — the grade-10 four-shape core reappears one
jet level up with the load degenerated to `kap1 = (5/6)cs^3 k1 p` on
`V(k)` and absent on `V(J1)` — is **CONFIRMED**, and the collapse
`e0 = e1 = 0` on `D(rho)` follows by the same three-line argument as
Prop 3.1.  The correction is to the printed combination only; it must be
fixed before any lane consumes the display.

### 3.3 The grade-14 load on `V(J1)`: census, and a scope repair

`Tg14_5|_{J1}` has 62 terms, of which exactly 12 contain `k`:

```text
-(5/128) a0*a1*k*rho^4
+(5/64) cs1*e0*ell1*k*rho^2   -(5/128) cs1*ee0*k*rho^4
+(15/1024) cs1*ell1*k*rs1^2   -(15/1024) cs1*k*rs1*rs2*rho^4
-(15/128) cs1^2*cs2*k*rho^6   +(15/128) cs1^3*ell1*k*rho^4
-(5/128) cs2*e0*k*rho^4       -(15/2048) cs2*k*rho^4*rs1^2
+(5/256) e1*ell1*k*rho^2*rs1  -(5/512) e1*k*rho^4*rs2
-(5/512) ee1*k*rho^4*rs1
```

Every correction term is divisible by one of `cs1, cs2, rs1, rs2, e0, e1`
— i.e. by the *jet-shifted `J1` block and its second shift* — but **not**
by `cs1` alone and **not** by `a1`.  The memo's sentence "`-(5/128)a0a1 k
rho^4` plus `cs1`-weighted corrections; it is `a0a1`-weighted, hence dies
on the ordered stratum `qa1 = 0`" is therefore **GAP as stated**: at
`qa1 = 0` the terms `cs2*e0*k*rho^4`, `e1*k*rho^4*rs2`, … survive.  The
exact statement is: `Tg14_5|_{J1} ≡ -(5/128) a0a1 k rho^4` modulo
`(cs1, cs2, rs1, rs2, e0, e1)`.  Consequences: the derivation of the
`A00`/`A10` sections from the mechanism still goes through (both kill the
whole block), and the `H3` mandatory negative control is unaffected —
but its justification is the *promoted* `A00`/`A10` sections, not the
"load dies on `qa1=0`" sentence, which should not be quoted.

---

## 4. Item 3 — the `k=0` delayed-load point

### 4.1 Modular replay  [CONFIRMED]

At each of the memo's three primes, with `cs=rho=1`, `k=rs=c0=c1=0` and
the printed `(k1, a0, a1, e0, e1)`, solving `k2c` from `Tg12_1`, `rs1`
from `Tg12_2`, and `k10_4` from `Tg14_5` (each linear, pivots
`(5/16)cs^3rho^2`, `(15/64)cs^2k1rho^2`, `-(5/128)cs^3rho^6` as the memo
states; note `Tg14_5` also carries a `k2c*rs1^2` cross-term that must be
substituted before the `k10_4` solve):

```text
p=65521  : k2c=60476  rs1=28446  k10_4=17229  -> all 22 rows = 0
p=1000033: k2c=328895 rs1=610954 k10_4=391951 -> all 22 rows = 0
p=1000081: k2c=449769 rs1=182618 k10_4=927933 -> all 22 rows = 0
```

`k = 0`, `cs*k1*rho != 0` at all three.  Memo telemetry **CONFIRMED**.

### 4.2 The characteristic-zero gap, discharged by construction  [VERIFIED-HERE]

The prompt is right that three modular points do not by themselves prove a
characteristic-zero point.  I therefore built one.  Let
`A = Q[w,s]/(w^4+1, s^2 - 5/12)`, a nonzero free `Q`-algebra of rank 8; it
is in fact the field `Q(zeta_8, sqrt(5/12)) = Q(zeta_8, sqrt(15))`, since
`5/12` is not a square in `Q(zeta_8)` (whose quadratic subfields are
`Q(i), Q(sqrt2), Q(sqrt-2)`).  Assign `cs = rho = k1 = 1`,
`k = rs = c0 = c1 = 0`, every other name `0` except

```text
a0 = (s/2)(w^2 + w)        a1 = (s/2)(w^2 - w)
e0 = s(w^2 - w^3)          e1 = s(w^2 + w^3)
k2c   = -1/8 + (1/8)w^2 - (1/4)w^3
rs1   = -1/6 + (1/3)w - (1/6)w^2
k10_4 = -275/256 + (827/384)w - (275/256)w^2
        + s*( 1/6 + (1/3)w - (1/3)w^2 - (1/6)w^3 )
```

Then **all 22 frozen rows evaluate to `0` in `A`**, and the point extends
to the ordered `T-cs` chart presentation with `qrs = qc0 = qc1 = 0` and
`u = 1` (every generator of the honest `K` maps to 0), while
`cs*k1*rho = 1` is a unit and `k = 0`.  Because `A != 0`, any maximal
ideal of `A` gives a genuine characteristic-zero field point; no
irreducibility is even needed.  Eight sign choices work, exactly matching
the memo's `±`-correlated family (`S = a0+a1 = s w^2`, `D = a0-a1 = s w`,
`E = 2S`, `F = 2iD` with `i = w^2` realizes the memo's upper-sign branch;
`S^2 = -5/12`, `D^2 = (5/12)i` as displayed at `cs=t=k1=1`).  One
embedding `A -> F_65521` reproduces the memo's printed point
`(a0,a1,e0,e1) = (48966, 4891, 3387, 38806)` exactly: the three modular
points are residue shadows of this one exact point.

**Consequences per evidence tier, restated.**  Modular tier (memo):
excludes certificates `cs^a k1^b rho^c ∈ I + (k)` whose cofactor
denominators are integral at one of three primes.  Exact tier (now): for
any `Q`-coefficient identity, evaluation at the point sends the right side
to 0 and the left side to 1 — so **no certificate `cs^a k1^b rho^c ∈ I + (k)`
exists over `Q` at all**, from the frozen 22 rows, in either the
substituted or the honest presentation.  The same evaluation kills
`rho`-torsion certificates (`rho` is a unit at the point), which is memo
§4.3 consequence 1 at full strength, and completes root's negative
control on the delayed sub-fan.  Memo consequences 2–5 all check out
against the blind cards' actual wording, with one sharpening: opus5
Card B's payoff branch ("restricted fibre empty") tests the `rho = 0`
fibre of `V(k) ∩ V(qc0,qc1)`, and that fibre already contains `CS0` at
`rho = 0` — promoted before the memo — so the payoff branch was dead
independently of the new point; indeed by opus5's own §3.2 quadric
structure the restricted system vanishes at the zero of the jet block
tautologically.  The new point's real addition is the `rho != 0`,
`k1 != 0` (delayed-load) reading, which `CS0` does not cover; the two
sub-fan readings now have different evidence and the same verdict, as the
memo says.

This subsection is producer-tier; the construction is small enough to
re-verify by hand from the displayed coordinates.

### 4.3 Grok Card B / fable5 §3.4 / root M3, adjudicated

All as the memo has them, now at exact tier: grok Card B's first branch
("some grade `<= 16` row is a unit on this open") is refuted **for the
frozen 22 rows**; its second branch obtains.  fable5 §3.4's mechanism is
counter-witnessed by a point with `k=0` and `e1 = s(w^2+w^3) != 0`.
root's `CS0`-as-negative-control instinct is vindicated on both readings.

### 4.4 Post-memo collision: V20 changes the answer above grade 12  [VERIFIED-HERE, conditional on unreviewed V20 bytes]

V20 (launched 02:43Z on Box02/Q + r6d/F65521, both `PASS`, harvested,
**not yet different-model reviewed**) exported `Tg13_1..Tg13_7,
Tg14_1..Tg14_7`; the re-derived `Tg14_5` hash equals V17's `91d96924…`
byte-for-byte (the first independent reproduction of any frozen row from
the 569 canonical tails), all 14 rows live in the same 40 names, and V20's
own section evaluations (`CS0`, `A00`, `A10`, `Z00` all empty residuals)
replay exactly here; `RS0` also persists (my check, not in V20's
contract).

Evaluating the 14 new rows at the §4.2 exact point: **13 of 14 are
nonzero** (`Tg14_5`, already frozen, is the only zero).  `Tg13_6`
evaluates to the rational unit `35/128`.  The structural reason is an
exact identity on the frozen+V20 bytes:

```text
Tg13_6 + (1/2)*cs*rho^2*Tg11_1 - (35/128)*cs^4*k1*rho^4
        ∈  ( k, rs, c0, c1 )                     [27-term residual, checked
                                                  monomial-by-monomial]
```

Combined with the verified opus5 §3.5 collapse (`V(k) ∩ V(Tg10_1..4) ⊆
V(c0,c1)` set-theoretically, char `!= 2,3`) and the stratum equation
`rs = cs*qrs, qrs = 0`, this gives, over any field of characteristic
`∉ {2,3,5,7}`:

> at every point of the ordered `T-cs` chart stratum with `k = 0` on which
> `Tg10_1..Tg10_4, Tg11_1, Tg13_6` vanish, `cs^4*k1*rho^4 = 0`.

**The delayed-load sub-fan `V(k) ∩ D(cs*k1*rho)` dies at grade 13** —
set-theoretically, by one new row plus the frozen core.  This is exactly
the memo §4's descent mechanism firing one more time (`35/128 = 15/128 +
(1/2)(5/16)`: the exported load term plus the jet-shift correction), and
it converts memo §4.3's consequence 6 from "any future `k=0` attempt
requires genuinely new exported source" into a decided instance: the new
source arrived and the delayed reading is killed (pending V20 review),
while the zero-leading-load reading (`CS0`, whole `k`-tower zero)
**persists through grade 14** by V20's section result.  The next
stratum of the fan is `V(k, k1) ∩ D(cs*k2c*rho)`: `Tg14_6` restricted
there carries the expected `(15/128)cs^4*k2c*rho^4` load **plus a
quadratic block** (`(3/32)a0^2cs^2 + (9/32)a1^2cs^2rho^2 - (3/64)cs*e0e1 +
…`), so the grade-14 question is a genuine next-level core solve, not a
one-line identity (§7.3, item 2).

Nothing in this subsection re-scopes the memo: the memo's §8 firewall
explicitly limited §4.3 to the frozen bytes.  The point (§4.2) remains a
true and useful statement about the 22-row prefix — in particular it still
proves that no V19-style certificate from those rows can reach the
sub-fan — but the ledger record of the witness must carry the V20
counter-evaluation so nobody quotes it against the 36-row system.

---

## 5. Item 4 — the torsion-multiplier chain, audited link by link

The lemma itself is elementary and correct: if `f ≡ c*rho (mod I)` and
`g*rho^r ∈ I` then `g*f^r ≡ c^r*g*rho^r ≡ 0 (mod I)`.  The instantiated
chain, with the tier of each link as of this session:

1. **Promoted fibre emptiness.**  The grade-14 fibre promotion states the
   localized special-fibre ideal (substituted rows + `qrs` + `rho`,
   localized at `cs*k`) is the **unit ideal over `Q`** — an algebraic
   statement, Nullstellensatz/faithful-flatness tier, **no explicit
   cofactors**.
2. **Clearing (fable5 Lemma A).**  Finite generation turns that into
   `(cs*k)^m ∈ (Ehat) + (qrs) + (rho)` for some unspecified `m`.  This
   step is now *recorded at promoted tier* as clause (C) of the
   converse-correction memo, so the memo's "only unreviewed link" label is
   already discharged.
3. **`qrs` elimination.**  The retraction `qrs ↦ 0` fixes everything else
   and maps `Ehat_i` to `E_i`, giving `(cs*k)^m ∈ (E_1..E_22) + (rho)`.
   Elementary; stated here because the memo skips it.
4. **`rho`-parity upgrade (missed by the memo).**  Every generator is even
   in `rho` (rows: exponent census; bilinears and `qrs`: `rho`-free), so
   the ideal is stable under `rho ↦ -rho`; taking even parts of the
   identity in step 3 yields `(cs*k)^m ∈ (E) + (rho^2)`.  The prompt asked
   parity to be tracked; this is where it pays.
5. **Grade-10 torsion certificate.**  `cs^6*k^2*rho^6 ∈ I` — reviewed
   twice (Grok, Fable) inside the promoted direct certificate, re-expanded
   independently in the memo, and **re-expanded here in both
   presentations**, including the full honest-ordered identity with the
   printed `B_rs, B_c0, B_c1, B_qrs` (residual exactly 0).  So the
   multiplier input is available directly in the honest `K`, and Lemma 0
   is needed only in its easy direction (`E_i ∈ K`), which both
   certificate reviews reconstructed.
6. **Composition.**  With `f = cs^m k^m ≡ rho^2*c (mod K)` (step 4 read in
   `K`) and `g*rho^6 = cs^6k^2rho^6 ∈ K`:  `f^3 ≡ rho^6 c^3`, hence

   ```text
   cs^{3m+6} * k^{3m+2}  ∈  K        (W = 0),
   ```

   versus the memo's `cs^{6N+6} k^{6M+2}` from `r = 6`.  Same conclusion,
   half the exponent inflation; the producer's own §6.1 cube is this
   composition against its explicit branch (b).

**Answer to the prompt's question: YES** — the promoted localized
special-fibre theorem plus the reviewed grade-10 membership imply a direct
monomial `cs^N k^M` in the honest total ideal with no branch-(b) input,
**as a pure existence statement**: step 2's `m` is not effective, so no
explicit exponents and no exponent-quality claims transfer; the
`(447,164)` certificate remains the only explicit instance.  The chain
never invokes the corrected false converse: at no point is the
`rho`-cofactor of step 3 required to be divisible by anything — the
divisibility is *bought* by multiplying with the torsion certificate,
which is precisely the legal repair the correction memo leaves open.  As
a control, the correction memo's own counterexample `I = (cs - rho)`
correctly defeats the chain at step 5 (no monomial times a `rho`-power
lies in `(cs - rho)`: set `cs = rho`), so the lemma cannot resurrect the
false converse.  Memo §3.1 and its Branch-B insurance argument are
**CONFIRMED**; both hostile reviews returning CONFIRMED has since made the
insurance moot, but it remains a genuinely independent second derivation
of existence.

---

## 6. Item 5 — the memo's repairs to the Fable blind claims

### 6.1 Lemma A — CONFIRMED

As §5 steps 2–3.  Also correctly scoped in the blind report itself
("off-E part only").

### 6.2 Lemma B and the E-gate — memo's two-defect repair CONFIRMED, one caveat

Lemma B as an existence-iff is correct (⇒ is trivial; the memo endorses
it and I concur), with one normal-form caveat the memo does not state: the
⇐ direction produces `cs^N*(k^M - rho*W') ∈ I`, which is the registered
staged triple only after reading `k^M - rho W'` as `k^M*(1 + rho*(-W'/k^M))`
in the `k`-localized ring; the staged conclusions (localized fibre
emptiness, DVR-arc exclusion) do follow, but the literal
`f^N s (1+rho W)` shape does not without a further `k`-power.  Harmless
here; worth a sentence in any ledger copy.

The memo's two refutations of the *inference* are both right and both
verified: (i) divisibility can be bought (that is §5's chain; failure at
one `(N,M)` proves nothing about existence); (ii) the proposed E-gate
computes with the naive divided rows, which generate a subideal of
`(I : cs^∞)`, so a positive-dimensional `rho`-non-unit locus for the
subideal obstructs nothing.  The memo's empirical discharge also checks:
from the verified `cs^6k^2rho^6 ∈ I`, `k^2rho^6 ∈ (I : cs^6) ⊆ (I : cs^∞)`,
so `rho^6 = 0` in the `cs`-saturated `k`-localized chart ring, including
its restriction to `E`; fable5 Card 1 outcome (ii) cannot occur on `D(k)`.
**Card 1 off the critical path: CONFIRMED.**

### 6.3 fable5 §3.4's `k=0` mechanism — scope error CONFIRMED; what survives, by which reason

The relation `12e1^2 = 5cs^4k` is the restriction of `Tg12_2` (36 terms in
full) to the five-zero slice *inside* `D(cs*k)`; on that locus `k = 0` is
vacuous, so the argument proves nothing at `k = 0`.  The counter-witness
is now exact: §4.2's point has `k = 0`, `e1 != 0`, all 22 rows zero.  The
*conclusion* — grade `<= 14` frozen rows cannot decide `k=0` — survives
via the promoted `CS0`/`A00`/`A10` sections and, for the delayed reading,
via §4.2.  Post-V20 the conclusion itself bifurcates: with the grade-13
export the delayed reading **is** decided (killed, §4.4, pending review),
while the zero-load reading persists through grade 14 — so fable5's
"needs grade `>= 16` rows or rerouting" was wrong in both directions:
grade 13 sufficed for one reading, and no grade `<= 14` suffices for the
other.

### 6.4 The other fable5-adjacent repairs

Memo §2.8 (grok's odd-sheet merge: theorem for the leading-form equality,
NAVIGATION for the scheme identification) and §2.9 (the `k10` filing:
`k = k0 = const(k10)`; the three-rings warning; `D(k)` intrinsic;
sibling fan with readings the review refuses to collapse) were both
checked against the underlying review `678a087d…` line by line and are
faithful restatements.  §4.4's split of the sibling fan (delayed reading
killed at grade 13, zero-load reading open) is consistent with — and is
the first internal stratification of — the fan that review left
unstructured.

---

## 7. Item 6 — deduplication audit, decision audit, alternate queue

### 7.1 Deduplication (§1) — CONFIRMED at navigation tier

The eleven-mechanism reduction is accurate against the four blind texts;
attributions spot-checked (M1 root §3.1; M3 root §3.2; M4/M5 fable5
§3.2–3.4; M6 three-lane; M7 three-way with three different predicted
outcomes — the census resolved it grok-branch-3 / fable5-discharged /
opus5-refuted, as the memo adjudicates; M8 grok; M10 opus5; M11 fable5).
Two annotations.  (a) In C-A, "four different derivations, no shared
premise beyond the freeze" overstates independence: all four lanes read
the same 22 frozen rows, so the convergence is correlated through the
bytes (see §10).  (b) The §1.3 row-5/21/18/31 adjudications are
avenue-table routing; I audited the mechanics beneath them (row 18's
reopen is exactly §2.1's rank-2 torus, confirmed) and defer the rest as
navigation.

### 7.2 Decision audit (§5–§6) against the post-memo record

- "J1 completion: the remaining work is review, not computation" —
  correct, and now discharged: both hostile reviews returned CONFIRMED and
  the promotion is filed.  The memo's worry that reviewers would skip
  Lemma 0 for branch (b) did not materialize; both reviews reconstructed
  Lemma 0 independently.
- "`k10=0` sibling: stop as Gate-T computation; record the §4.3 witness" —
  correct then; **update now**: record the witness *with* §4.4's V20
  counter-evaluation and the grade-13 kill identity, and re-file the
  sibling as: delayed reading killed at grade 13 (pending V20 review),
  zero-load reading open above grade 14.
- "Drop the `M >= 1` gate (unsound)" — **reverse this** (§2.3): keep the
  gate with `CS0`/`RS0` provenance.  Keep dropping the `deg_2` citation
  and the `(5,1)`-minimality prediction.
- "V19: stop the mathematics, let the protocol run" — still right, and
  stronger now that the certificate is promoted.
- §5.3 routing (H1→Box02, H2→r6d, H3→Box03) — **overtaken**: V20 occupied
  and then freed Box02/r6d (it ran in ~34 s plus validation).  H1/H2
  remain sound job designs; the corrected gate list applies (drop `deg_2`;
  keep nonzero-`Tg14_5` cofactor; keep `M >= 1` per §2.3; add
  `deg_s`-homogeneity and Lemma-0 translation fail-closed fields).
- "Not routed, deliberately: no `k=0` emptiness job on the frozen
  prefix" — still right for the frozen 22; §4.4 shows the *enlarged*
  system decides the delayed reading at a desk, so still no AWS needed.

### 7.3 Alternate top-five bounded queue (incorporating V20; nothing launched)

1. **V20 custody + different-model hostile review, bundled with the two
   §4.4 desk facts.**  Review the 14 new rows (emitter reproduction of all
   21 V9 rows + byte-identical `Tg14_5` is a strong custody signal), the
   section-persistence result (including my `RS0` addition), the
   13-of-14 nonzero evaluation at the §4.2 point, and the grade-13 kill
   identity `Tg13_6 + (1/2)cs*rho^2*Tg11_1 - (35/128)cs^4k1rho^4 ∈
   (k,rs,c0,c1)`.  Also file the §3.2 factor-2 correction before the
   shifted-core display propagates.  Desk; highest information per hour;
   converts the `k=0` fan from "parked" to "half decided".
2. **Next fan stratum: `V(k,k1) ∩ D(cs*k2c*rho)` against the 36-row
   system.**  `Tg14_6`'s restriction carries the `(15/128)cs^4k2c rho^4`
   load plus a quadratic block; run the §4.2-style core solve one level
   down: outcome is either the next exact point (stratum survives grade
   14) or the next kill identity (whole delayed tower collapses
   grade-by-grade, leaving only the zero-load limit as the true sibling).
   Desk, one sitting; stop on first surviving grade, per grok Card B's
   stop shape.
3. **DD1, upgraded.**  The first-order jet shift is now testable at
   grades 12→13 and 13→14 on the V20 bytes, alongside the memo's
   second-order grade-12 question.  If the shift-with-corrections holds
   through grade 14, the descent is a tower and the stage-two certificate
   shape is determined without search.  Desk, hours; one sitting, report
   the exact obstruction if the connection terms fail to close.
4. **Stage-two ordered `T-a0` core on `D(qa1)` (memo H3), corrected.**
   Keep `A00`/`A10` as the mandatory must-fail control (their persistence
   through grade 14 is now V20-tested); do not cite the "load dies on
   `qa1=0`" sentence (§3.3).  Host Box03 or freed Box02/r6d, after root
   static audit and coordinator sign-off; H2 (the `rho^2`-order question,
   the only certificate-quality item) can share the launch batch.
5. **AS109 `n = 2` arithmetic-Newton corner with the gauge-section
   preprocessor** (memo's #5, unchanged).  Three-way independent
   convergence, hand-scale, symmetric payoff, two-increment stop rule;
   keeps the queue from collapsing to proof-side only.

Dropped from the memo's five: re-pointing the certificate reviews (OBE —
returned CONFIRMED) and the standalone corrections filing (absorbed into
item 1); DD2 (`deg_s`-type the D1/affine-Faber/TD6 row sets) slips to
sixth — still cheap and worthwhile, but the `k`-tower items above it are
now decision-relevant.

---

## 8. Theorem vs navigation ledger

**Theorem-tier (exact, on the frozen or V20 bytes; VERIFIED-HERE unless
marked promoted):** the rank-2 lattice and `deg_s` table (§2.1); the
impossibility of `g(rho)=g(cs)=0`; the `deg_2` inhomogeneity spectra; the
`M >= 1` statement via promoted `CS0`/`RS0` evaluation (§2.3); the
seven-row jet identity and both corrected shifted-core columns (§3);
the `Tg14_5|_{J1}` `k`-census (§3.3); the three modular replays and the
exact `A`-point with all 22 rows zero (§4.1–4.2); the honest-presentation
grade-10 identity (§5, step 5); the grade-13 kill identity and the
13-of-14 nonzero evaluation (§4.4, conditional on V20 bytes); the
torsion-multiplier composition with parity (§5).

**Navigation (correct but not theorems):** "`deg_s` is the sigma-order";
the descent mechanism as a predictor; the sibling-fan re-filing; the
queue of §7.3; all adjudications of blind-card outcome branches.

**Corrections owed to the ledger before consumption:** the §3.2 factor-2
cofactor; the §3.3 "cs1-weighted / dies on `qa1=0`" sentence; the memo's
"`M >= 1` gate unsound" decision (§2.3); the §4.3 witness record must
carry the §4.4 V20 counter-evaluation.

---

## 9. Replay telemetry summary

```text
custody      22/22 frozen row hashes match; 14/14 V20 hashes match RESULT.json;
             memo + 4 blinds + 6 charged artifacts rehashed, all MATCH
grading      constraints 641, vars 40, rank 38, nullity 2; deg_s integral,
             >=0, row degree = grade for 20/20 nonzero rows
deg_2        inhomogeneous rows: Tg11_{1,2,3,4,5,7}, Tg12_{1,2,3,4,5,7}, Tg14_5
jet          7/7 rows exact; residuals in k*(c0,c1), <=2 terms each
cores        V(J1) 4/4 and V(k) 4/4 shapes exact after the (8/3)ell1 fix
sections     CS0/A00/A10/RS0 kill 22/22 frozen rows and 14/14 V20 rows (Q[rho])
J1 census    12 survivors, first grade 11, a0/a1 absent only in Tg12_4
branch (a)   substituted and honest identities: residual 0
point        3/3 primes replay; exact A-point kills 22/22; one embedding
             reproduces the memo's F65521 point; k1 monomial count 93
V20 vs point 13/14 new rows nonzero; Tg13_6 = 35/128; kill identity residual
             (27 terms) wholly inside (k,rs,c0,c1)
```

---

## 10. Correlated-dependence flags

Every quantitative convergence in this round — the four blind lanes'
`k=0` consensus, the two-lane syzygy agreement (memo C-E), the memo's
verifications, both certificate reviews, and this report — is conditional
on the **same** frozen V9/V17 bytes and inherits their single upstream
literal-source (Faber emitter) provenance debt.  Agreement across models
therefore bounds transcription and reasoning error, not source error.
The only independent re-derivation of any frozen row to date is V20's
emitter rebuild (21 V9 rows + `Tg14_5` reproduced, `Tg14_5`
byte-identical), which is itself single-producer dual-host and unreviewed;
its review (queue item 1) is currently the cheapest way to shrink the
common-mode risk.  A parallel Grok review of this same memo is queued;
its agreement with this report, if it comes, will also be
frozen-byte-correlated and should not be double-counted.

---

## 11. Scope firewall

Everything new in this report — the exact characteristic-zero point, the
corrected shifted-core combinations, the `M >= 1` gate repair, the parity
refinement, the grade-13 kill identity, the 13-of-14 evaluation, the
`RS0` section, and the alternate queue — is **producer-tier from this
lane and unreviewed**; §4.4 additionally depends on unreviewed V20 bytes.
Nothing here establishes or refutes: JC2; Gate T; the `k10=0` sibling fan
as a whole (one reading is killed only pending V20 review; the zero-load
reading is open); either `J2` chart; the terminal receiver; chart
overlaps; the deck/square bridge; the generic comparison; literal source
universe or coverage; TD6, SP-2, or the omitted-moduli cover; order two;
maximum twelve; arbitrary-standard-pair landing; `G2-PSC`; any invoked
`G2-BD`; any cofinal degree/type bound; existence or nonexistence of an
AS109 lift; or any Lean statement.  All statements about the 22 rows and
the 14 V20 rows are statements about those frozen bytes, not about the
source ideal, and say nothing about grades above 14.  No AWS state was
read beyond harvested case files, none was mutated, nothing was launched,
`jc2-lean` was not accessed, no web was used, and no Groebner/CAS was run.
The only repository file written is this one.
