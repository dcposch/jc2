# Hostile review: direct three-row strict unique-`AC` certificate

Date: 2026-08-27
Reviewer: Grok 4.6 (xAI), adversarial exact-algebra and Faber-support desk review.
Independence: every identity, polar grade, coefficient, and contact in this
file was re-derived here.  Producer `PASS` strings, the Opus5 B22 observation,
and the Fable review lane were not used as evidence.  The uniform
contact-shift naturality review is cited only for its formula-level row
connection `Phi4=h4+(P/2)h2` and the direction of the jet-reindexing map, not
as a chamber-purity theorem.

Candidate (hash re-verified byte-exact):

```text
2354703a559a5da2b4f2032560a5740b2cda1f3160f5c6598dcdbe1c4c1432be
  xmodel/max12-812-order2-gate-t-strict-uac-three-row-syzygy-interface-sol-20260827.md
56edb06f57c657534b46f1c406363de7821e240ccc1eb7d8529be7eeb2c5c3f4
  xmodel/max12-812-order2-gate-t-strict-uac-three-row-syzygy-interface-replay-20260827.py
```

Mandated prompt (hash re-verified):

```text
a232ab4393b7b9893f183500cea269f574be1b97583df4c9f4c46056d0bdc73a
  xmodel/max12-812-order2-gate-t-strict-uac-three-row-syzygy-interface-hostile-review-fable5-prompt-20260827.md
```

Tuple pin used throughout this review: a contact is `(a,d,r)` with `c=a+d`,
equivalently `(a,c,r)`.  The pair `(2,5,r)` in the Grok launch prompt is
`(a,c,r)`, i.e. `(a,d,r)=(2,3,r)`, the current `B23` tail.  The candidate
switches conventions inside §2; that switch is recorded in Attack 5 and is
not allowed to blur the `(2,5,r=3,4)` decision.

## 0. Verdict summary

| # | Mandated attack | Verdict |
|---|---|---|
| 1 | Re-expand (1.2); radical / open-set conclusion; inverted factors | **PASS** |
| 2 | Polar contributors to `Phi1[G]`, `Phi2[G]`, `Phi4[T_C2]`; simple-pole cancellation; hidden higher-pole/load/target terms | **PASS** |
| 3 | Twelve baseline contacts, raised-`r` subtails, every named wall; `(2,5,r=3,4)` vs `r>=5` | **PASS** |
| 4 | Literal-row direction, source-to-total transport, replace vs corroborate | **PASS** at stated scope (replacement not licensed) |
| 5 | Replay: transcription, stale hashes, inventory, tuples, mutation controls | **REPAIR** |
| 6 | Minimal reviewed linker/schema delta | **REPAIR** (delta below; not yet frozen) |

**Overall: REPAIR.**  The core algebraic lemma is proved, the polar
contributors are the claimed ones, and the contact list including the
`(2,5,r=3,4)` split is exact.  The lemma does not yet replace any promoted
endpoint: the desk replay is not a linker verifier, and the §4 sketch is
missing several fail-closed pins.

**Smallest failing identity:** none of (1.2).  All four are the zero
polynomial over `Z[1/6][A0c,A1,C0c,C1,rho]`.

**Smallest failing hypothesis:** that the desk replay together with the §4
sketch already licenses replacing a promoted D1 endpoint.  They do not.  The
smallest executable hole is that the replay has no mutation control which can
fire on the target walls `G<28` / `T_C2<32` or on the AC / `C^2` coefficients,
and that the linker sketch re-uses the label `(1.1)` for a different object
than the uniform-transport emitter formulas.

**Not concluded here:** a strict-fan cover, the ramified fibre `rho=0`,
equality faces, Rees charts, the terminal receiver, Gate T, order two,
maximum twelve, JC2, or a counterexample.

---

## 1. Custody

Recomputed SHA-256 in this session, matching the launch pins:

```text
2354703a559a5da2b4f2032560a5740b2cda1f3160f5c6598dcdbe1c4c1432be  sol
56edb06f57c657534b46f1c406363de7821e240ccc1eb7d8529be7eeb2c5c3f4  replay
a232ab4393b7b9893f183500cea269f574be1b97583df4c9f4c46056d0bdc73a  fable5 prompt
0e94e5408b8a3b5db06c8eff5c759df1c75a2e8bb4563aa4964f42c39952fe9a  mine_support.py
1cfa10b45d83ba4ecd98861c1f82e9bd41056d1cef7eaa43ad2802aa73aada5d  uniform-transport sol (cited, formula-level only)
23007a2bb15e866f87a05bdff9f7a0ea0f1b05588d721d4b03bd377f0b89ce12  Opus5 a2d2 review (cited by producer; not authority here)
```

The miner pin inside both the candidate and the replay matches the bytes on
disk.  `enumerate_primitives` is ordinary Python; `main()` is AWS-gated and
was not run.  No `jc2-lean` path was entered.  Producer replay output (not
evidence, only a mutation-style self-check of the file that was audited):

```text
PASS-UAC-THREE-ROW-SYZYGY-INTERFACE
SYZYGIES=4
BASELINE_CONTACTS=12
RECOVERED_SUBTAIL_BASES=4
CURRENT_B23_R3_R4=REJECT
CURRENT_B23_RGE5=ACCEPT
```

---

## 2. Attack 1 — the four identities and the radical conclusion: PASS

Work in characteristic zero, or any `Z[1/6]`-algebra.  Write

```text
L = z^2 - rho^2,
A0 = A1*z + A0c,
C0 = (C1*z + C0c)/2,
D = rho^2*C1^2 - C0c^2,
```

and (1.1) exactly as displayed:

```text
g1 = (3/8)*(A0c*C1 + A1*C0c),
g2 = (3/8)*(A0c*C0c + rho^2*A1*C1),
g4 = (3/32)*(C0c^2 + rho^2*C1^2).
```

The factor `/2` on `C0` is the generating-function chart factor; dropping it
replaces `3/8, 3/32` by `3/4, 3/16` and breaks (1.2).

**Identity 1.**

```text
C1*g2 - C0c*g1
  = (3/8)*C1*(A0c*C0c + rho^2*A1*C1)
    - (3/8)*C0c*(A0c*C1 + A1*C0c)
  = (3/8)*A1*(rho^2*C1^2 - C0c^2)
  = (3/8)*A1*D.
```

The `A0c C1 C0c` terms cancel.

**Identity 2.**

```text
C0c*g2 - rho^2*C1*g1
  = (3/8)*C0c*(A0c*C0c + rho^2*A1*C1)
    - (3/8)*rho^2*C1*(A0c*C1 + A1*C0c)
  = (3/8)*A0c*(C0c^2 - rho^2*C1^2)
  = -(3/8)*A0c*D.
```

The `rho^2 A1 C1 C0c` terms cancel.

**Identities 3 and 4.**  `(32/3)*g4 = C0c^2 + rho^2*C1^2`, so

```text
(32/3)*g4 + D = 2*rho^2*C1^2,
(32/3)*g4 - D = 2*C0c^2.
```

An independent sparse-polynomial engine (monomials as sorted exponent
tuples, coefficients in `Fraction`, different variable names `A0c,C0c` from
the replay's `A0,C0`) returns four empty dictionaries.  Mutations fire:
`3/8 -> 3/4` in `g1` makes identity 1 nonzero; `3/32 -> 3/16` in `g4` makes
identity 3 nonzero.

**Localization and radical.**  Let `I = (g1,g2,g4)` in
`Z[1/6][A0c,A1,C0c,C1,rho]`.  Identities 1–2 put `A1 D` and `A0c D` in `I`.
After inverting `A1` (resp. `A0c`), `D` itself lies in the localized ideal.
Identities 3–4 then put `C0c^2` and `rho^2 C1^2` in
`I[A1^{-1}]` (resp. `I[A0c^{-1}]`).  After inverting `rho`, `C1^2` lies in
the same localized ideal.  Hence

```text
C0c, C1  in  radical(I[rho^{-1}, A0c^{-1}])
and
C0c, C1  in  radical(I[rho^{-1}, A1^{-1}]).
```

This is exactly (1.3).  Set-theoretically, on the Zariski open

```text
D(rho) intersect (D(A0c) union D(A1)),
```

the three equations `g1=g2=g4=0` force `C0c=C1=0`.  Combined with exact
nonzero leading `A` (the point already lies on that open) this contradicts
exact nonzero leading `C`.

**What is not claimed, and is not true.**  The localized ideal need not be
the unit ideal: it contains the squares `C0c^2` and `C1^2`, so the scheme
may be non-reduced in the `C` directions.  Over a domain (in particular a
DVR arc) `C^2=0` implies `C=0`, which is the load-bearing emptiness for
arcs.  A scheme-theoretic unit-ideal endpoint is strictly stronger and is
not supplied.

**Inverted factors, all of them:** `2` and `3` (from `3/8` and `32/3`),
`rho`, and exactly one of `A0c`, `A1`.  No leading `C`, no `k10`, no `J`,
no Hensel root, no deck sign.  Characteristic zero is stronger than needed;
`Z[1/6]` suffices.

**Load-bearing hypotheses, independently checked.**

- If `A0c=A1=0`, then `g1=g2=0` identically and `g4=0` only forces
  `C0c^2 + rho^2 C1^2 = 0`, not both coefficients zero.  Exact `A` is
  necessary.
- If `rho=0`, then `g4=0` forces `C0c=0`, and `g1=(3/8) A0c C1`.  On
  `A0c=0`, `A1` nonzero, `C1` is free.  The ramified fibre is not covered,
  matching the candidate's refusal.
- If `g4` is dropped, identities 1–2 only recover `D=0`, i.e. a shared-root
  condition `C0(rho) C0(-rho)=0`, which is the old allocation lemma, not
  `C=0`.  All four identities are used.

The candidate's wording that this is a set-theoretic/radical statement, and
not a unit ideal before localization or radical, is the correct strength.

---

## 3. Attack 2 — polar contributors and `Phi4` cancellation: PASS

Frozen row connection (the literal `Phi` rows, not an unbridged `H`):

```text
Phi1 = h1,
Phi2 = h2,
Phi4 = h4 + (P/2)*h2.
```

### 3.1 `AC/L` produces `g1,g2` and nothing in `Phi4`

Unloaded two-atom family `A+C`: denominator `7`, `4*alpha=6`, pole `1`,
fixed `10`, grade `G=10+a+c`, coefficient

```text
binom(3/2, 2) * 2!/(1!1!) = (3/8)*2 = 3/4.
```

Numerator `(3/4) A0 C0`.  Expanding and reducing `z^2 = rho^2` along `L`:

```text
A0 C0 = (A1 C1 rho^2 + A0c C0c + (A1 C0c + A0c C1) z)/2.
```

Times `3/4`:

```text
[z]     = (3/8)(A0c C1 + A1 C0c) = g1 = Phi1[G],
[const] = (3/8)(A0c C0c + rho^2 A1 C1) = g2 = Phi2[G].
```

This is a genuine simple pole after reduction (remainder of `z`-degree `<2`),
so it contributes `0` to `Phi4` by §3.3.  That is why `g4` is not taken from
grade `G`.

### 3.2 `C^2/L^2` produces `g4`

Unloaded two-atom family `C+C`: denominator `8`, pole `2`, fixed `10`, grade
`T_C2=10+2c`, coefficient `binom(3/2,2)=3/8`.  The `L^2` numerator is
`(3/8) C0^2`.  With the chart factor, `N(±rho)=(3/32)(±C1 rho + C0c)^2`, so
the even combination is

```text
[N(rho)+N(-rho)]/2 = (3/32)(C0c^2 + rho^2 C1^2) = g4 = Phi4[T_C2].
```

(The `/2` on `C0` is again load-bearing: it supplies the extra `4` that turns
`3/8` into `3/32`.)

### 3.3 Simple poles cancel from `Phi4` with moving `P`

For a simple pole, `H = N_s * Inv1` with `Inv1 = (1+(P/2) t^2)^{-1}` and
`N_s` of `z`-degree `<2`.  The inverse-series recurrence is

```text
h_{k+2} = -(P/2) h_k
```

in the power-series ring, with the full moving `P = p0 + sigma ell_1 +
cdots`, not a frozen `p0`.  Therefore

```text
Phi4 = h4 + (P/2) h2 = 0
```

identically, as a polynomial identity of jets, for every pole-one family.
Equivalently: rewritten over `L^2`, a simple pole has numerator `N_s L`,
which vanishes at both roots of `L`, so both the even combination `Phi4` and
the odd combination `Phi3+(P/4)Phi1` vanish.

This licenses the candidate's sentence that pole-one loads and moving
connection jets "cancel from `Phi4` rather than being set to zero".  It does
**not** license them in `Phi1[G]` or `Phi2[G]`.  Those two coefficients are
source-pure only when `AC/L` is the unique polar primitive at or before `G`
(condition 1).  The first `ell_1` correction to a simple pole is at grade
`G+1`, so it cannot contaminate `Phi1[G]`, `Phi2[G]`; it can reach `Phi4` at
`T_C2 >= G+1` and then cancels by the recurrence.

### 3.4 Families that would survive on a claimed pure contact, and do not

A global pole `>=2` other than `C^2` contributes a genuine even double-pole
term to `Phi4` **unless a root of `A` is allocated**.  The three-row lemma
allocates no root, so the correct purity predicate is global pole, not the
miner's `local_pole_upper_at_A_root`.  The candidate's `eligible` test in the
replay uses global pole.  That is the right test for this lemma and a
different test from the miner's `SAFE_C2_ONLY` census (seventeen locally safe
`d=2,3` blocks, of which only seven are globally three-row-pure at the
registered tail).

On every contact declared pure in Attack 3, an independent aggregated
binomial census (same four atoms and four summands as the miner, own
aggregation, pad `+1` sentinel stable) finds:

- unique primitive at or before `G`: unloaded `AC/L` with coefficient `3/4`;
- unique pole-`>=2` primitive through `T_C2`: unloaded `C^2/L^2` with
  coefficient `3/8`;
- every other in-window family pole one (`k10 A^2`, `k10 RC`, `k10 R^3`,
  `k6 C`, `k6 R^2`, `k2 R` when present).

No target enters: `mu2` is at grade `28` in row 2, `mu4` at grade `32` in
row 4, and every pure cell has `G<28`, `T_C2<32`.

**Aggregation trap, independently closed.**  The unloaded family `R^2 C`
has two atomizations, coefficients `+3/4` (the `R2` atom plus `C`) and
`-3/4` (two `R` atoms plus `C`), same key `(fixed,R,A,C,pole)=(9,2,0,1,2)`.
They cancel.  A naive monomial list without aggregation would have rejected
`(a,d,r)=(2,1,2)` as carrying a second double pole at `T_C2=16`.  Both the
pinned miner and the independent enumerator return coefficient `0` and omit
the family.  Own-vs-miner signature comparison on the box
`a<=7`, `d in {1,2,3}`, `r=a..a+5` : **zero mismatches**, pad-`+1` stable.

---

## 4. Attack 3 — contacts, subtails, and walls: PASS

Closed forms used, then checked against the enumerator (not against the
producer's hardcoded list):

```text
G     = 10 + a + c = 10 + 2a + d
T_C2  = 10 + 2c
s_min = 1 if a <= d else 0     (for d=1,2,3 with a+d >= 3)
r_fl  = a + s_min
RA^2/L^2 : grade 12+r+2a, coeff -3/8, enters T_C2 iff r <= 2d-2
A^3/L^3  : grade 15+3a,   coeff -1/16, enters T_C2 iff a <= 2d-5
k10 R^2 A/L^2 : grade 13+2r+a, coeff -5/32
k6 C/L   : grade 17+c, pole 1; ties G iff a=7; precedes G iff a>=8
k2 R/L   : grade 22+r, pole 1; ties/precedes G iff 22+r <= 10+2a+d
k2 A/L^2 : grade 25+a, pole 2; reaches T_C2 iff 15-a-2d <= 0
mu2 in Phi2 at 28; mu4 in Phi4 at 32.
```

Eligibility is monotonic in `r` at fixed `(a,d)`: raising `r` only delays
`R`-containing families, `G` and `T_C2` are independent of `r`, and `A^3`
and `k6 C` do not depend on `r`.  So a threshold `r` is a complete subtail.

### 4.1 The twelve baseline contacts

Registered tails `r=a+s_min` that pass the four purity conditions:

```text
d=1, r=a :  (2,1,2), (3,1,3), (4,1,4), (5,1,5), (6,1,6)
d=2      :  (2,2,3), (3,2,3), (4,2,4), (5,2,5), (6,2,6)
d=3      :  (5,3,5), (6,3,6)
```

Twelve, matching the candidate.  Explicit `(G, T_C2)`:

| (a,d,r) | (a,c,r) | G | T_C2 |
|---|---|---|---|
| (2,1,2) | (2,3,2) | 15 | 16 |
| (3,1,3) | (3,4,3) | 17 | 18 |
| (4,1,4) | (4,5,4) | 19 | 20 |
| (5,1,5) | (5,6,5) | 21 | 22 |
| (6,1,6) | (6,7,6) | 23 | 24 |
| (2,2,3) | (2,4,3) | 16 | 18 |
| (3,2,3) | (3,5,3) | 18 | 20 |
| (4,2,4) | (4,6,4) | 20 | 22 |
| (5,2,5) | (5,7,5) | 22 | 24 |
| (6,2,6) | (6,8,6) | 24 | 26 |
| (5,3,5) | (5,8,5) | 23 | 26 |
| (6,3,6) | (6,9,6) | 25 | 28 |

All have `G<28` and `T_C2<32`.  At `(6,1,6)`, `k6 C` arrives at `24=T_C2`,
after `G=23`, pole one: `Phi1[G],Phi2[G]` stay pure AC; `Phi4` still cancels
it.  At `(6,3,6)`, `k2 R` arrives at `28=T_C2`, pole one, same story.

### 4.2 Raised-`r` subtails

```text
(a,d)=(1,2):  r=2 fails (RA^2 at 16=T_C2); r>=3 admits.
(a,d)=(2,3):  r=3,4 fail; r>=5 admits.          <-- (a,c,r)=(2,5,r)
(a,d)=(3,3):  r=4 fails (RA^2 at 22=T_C2); r>=5 admits.
(a,d)=(4,3):  r=4 fails (RA^2 at 24=T_C2); r>=5 admits.
(a,d)=(1,3):  no r admits (A^3 at 18=T_C2 for every r).
```

**The `(2,5,r)` decision, exactly.**  Here `(a,c)=(2,5)`, so `d=3`,
`G=17`, `T_C2=20`, and `RA^2` has grade `16+r`:

| r | RA^2 grade | in window? | unique AC at G? | eligible |
|---|---|---|---|---|
| 3 | 19 | yes, coeff `-3/8` | yes | **NO** |
| 4 | 20 | yes, at `T_C2` | yes | **NO** |
| >=5 | >=21 | no | yes | **YES** |

So `(2,5,r=3,4)` fails the three-row shortcut and `r>=5` admits it.  The
current contact `(2,5,>=3)` is not wholly a three-row contact.  The `r=3,4`
cells still need a certificate that retains `RA^2` (the existing `B23`
endpoint, or a stronger one).  This is a mathematical wall, not a
documentary one: `Phi4[20]` at `r=3` (resp. `r=4`) is `g4` plus a nonzero
`(R A^2)` even double-pole term, and identities 3–4 no longer recover
`C0c^2` and `rho^2 C1^2` from `I`.

### 4.3 Every named wall

**Exceptional `E=(1,3,r>=2)`.**  `A^3/L^3` at grade `18=T_C2`, coefficient
`-1/16`, independent of `r`.  At the least tail `r=2` one also has `RA^2`
at `16` and `k10 R^2 A` at `18` (coeff `-5/32`).  Raising `r` kills the
`R`-families and leaves `A^3`.  Enumerator at `r=20`: the only remaining
pole-`>=2` non-`C^2` family is `A^3`.  Cannot be repaired.  Separate
pole-three endpoint, as claimed.

**`RA^2/L^2`.**  Enters `T_C2` iff `r<=2d-2`.  Registered-tail failures
inside the low band: `(1,2,2)`, `(2,3,3)`, `(3,3,4)`, `(4,3,4)`, matching
the candidate, plus `E`.  Grades at `B23`: `19` and `20`, matching.

**`A^3/L^3`.**  Enters iff `a<=2d-5`.  Among strict cells this is only `E`
(`a=1`, `2d-5=1`).  No other `a<=6` cell.

**`a=7` `k6` tie.**  `k6 C` and `AC` both at `G` for every `d=1,2,3`:
grades `25,26,27`.  Initial inventory has two pole-one primitives;
`Phi1[G],Phi2[G]` are coefficients of `C(A+k60)`, not of `AC` alone.
Pole-one cancellation in `Phi4` does not repair that.  For `a>=8`, `k6`
precedes `AC` (load-first).  First load wall, as claimed.

**Later `k2` walls.**  At registered tails the first ties of `k2 R` with
`G` are exactly `(a,d)=(9,3),(10,2),(11,1)`.  The pole-two `k2 A/L^2`
reaches `T_C2` when `a+2d>=15`, first at `(9,3)` among these.  Both are
strictly beyond the `k6` wall (`a=7`) and, for these cells, also beyond
the `mu2` wall (`G>=28` already at `a=8` for `d=2,3` and at `a=9` for
`d=1`).  Later failures, as claimed.

**Target walls.**  `G>=28` first at `(8,2,8)` (`G=28`) and `(8,3,8)`
(`G=29`); `T_C2>=32` first at `(8,3,8)` (`T_C2=32`) and `(9,2,9)`.  A
source identity `g1=g2=g4=0 => C=0` may remain true, but those
coefficients are not equations of the target problem.  The candidate's
separation is correct.

**Strict unique-`AC` hull, for orientation only.**  The criterion
`a+c < min(2c, 3r, 1+r+c, 4+2a)` holds at every cell above and fails at
the equality faces `(a,c,r)=(2,2,2)` and `(3,3,3)`, which are outside
this lemma.  Not a fan-cover claim.

---

## 5. Attack 4 — literal-row direction and replace vs corroborate: PASS

**Direction.**  The three extracted quantities are `Phi1[G]`, `Phi2[G]`,
`Phi4[T_C2]`, i.e. literal source rows after the frozen connection, not
analytic `H`-rows.  Substituting `h4` for `Phi4` would be a different
polynomial (`h4 = Phi4 - (P/2) h2`) and would not equal `g4`.  An
analytic-only `H` certificate without a reviewed bridge to these `Phi`
rows must be rejected; the candidate says so.

The coordinates `(A0c,A1,C0c,C1)` are the shifted D1 leading jets of
orders `(a,c)`, not the stage-zero pairs `(a0,a1)`, `(c0,c1)`, `(rs,cs)`.
The erratum that `delta_D1` annihilates `J1+J2` forbids substituting the
stage-zero names.  D1AC's reuse of `a1,a0,c1,c0` for shifted leadings is
a live naming hazard the linker must pin (Attack 6).

No `rho=0` face byte is used.  The open is `D(rho)`.  Relabelling a
ramified-fibre row as a general-`rho` coefficient must be rejected.

**Source-to-total transport.**  This note does not prove transport.  At
formula level, the uniform contact-shift identity says the jet-reindexing
map `(D)` identifies `[sigma^g] Phi_ell^{D1}` with `[sigma^g] Phi_ell^{tot}`
in every grade, with no `rho`-inversion.  Emptiness of DVR arcs of an
exact contact therefore carries from D1 to total by factorization through
`(D)`, and not in reverse without a finite-jet factorization.  The two
interfaces are complementary: the present lemma kills three D1
coefficients on a pure contact; transport, once its own schema is frozen,
carries the same three equations to the total emitter.  Neither is a
chamber-purity theorem for a contact that fails Attack 3.

**Which imports can be replaced, which only corroborated.**  After a
frozen linker certifies conditions 1–4 on a manifest, the present lemma
can **replace** the moving-root / allocation step in a D1 emptiness proof
on the twelve baseline cells of §4.1, and on the raised subtails of §4.2
at those `r` that pass.  Via transport it can replace the corresponding
total-side comparison at the same grades.  It replaces only the
arcwise/set-theoretic unique-`AC` contradiction.  It does **not** replace
a scheme-theoretic unit-ideal claim.

It does **not** replace, and at most corroborates a subtail of:

- the exceptional pole-three endpoint `E`;
- the current `(a,c,r)=(2,5,>=3)` endpoint on `r=3,4` (and likewise the
  registered `(3,3,4)` and `(4,3,4)` cells);
- the `(1,2,>=2)` endpoint on `r=2`;
- any `a>=7` `k6` (or later `k2` / target) endpoint;
- equality faces, `rho=0`, positive-order loads, `V(k)`.

The candidate's own status line already withholds replacement pending a
frozen linker and a different-model review.  This review is the latter
and still withholds replacement pending the former.

---

## 6. Attack 5 — replay adequacy: REPAIR

What the replay actually does, executed unmodified:

- expands the four polynomials of (1.2) in its own sparse engine and
  demands they vanish;
- rehashes the miner against `0e94e540…` and imports
  `enumerate_primitives`;
- classifies registered tails for `a=1..6`, `d=1,2,3` against a hardcoded
  twelve-set;
- checks four recovered threshold cells and four controls (`E` at
  `r=20`, `B23` `r=3,4` reject, `B23` `r=5` accept, `a=7` `d=1` reject).

**Real work, not a tautology:** the syzygies are computed; a wrong `3/8`
fires.  The classification is computed from the miner; a wrong `is_c2`
that accepted `RA^2` would fail the `B23 r=3,4` control.  The miner hash
is not stale.

**Defects, all present.**

1. **Transcription of the expected twelve.**  The set is typed in, not
   derived from the wall formulas of §3 of the candidate.  A coordinated
   error in the report list and the expected set would pass.  This review
   derived the list from the walls and the enumerator; the replay does not.

2. **No coefficient pin.**  `is_ac` / `is_c2` test only
   `(load,R,A,C,pole)`.  A miner that returned AC with coefficient `1`
   instead of `3/4` would still classify as eligible, while (1.1) would be
   the wrong `Phi` identification.

3. **No pad-`+1` sentinel.**  The miner's `main()` runs it; the replay
   does not.  (Independently: it is stable on the whole tested box.)

4. **Incomplete negative controls.**  Missing `(1,2,2)`, `(3,3,4)`,
   `(4,3,4)`, any `k2` cell, and any cell with `G>=28` or `T_C2>=32`.
   Recovered subtails are checked only at the threshold `r`, not as
   `r>=` (monotonicity, proved in §4, makes this mathematically harmless
   but the replay does not know that).

5. **Mutation controls that cannot fire.**  There are no explicit
   mutations at all.  The cell controls that exist cannot see the target
   walls: every cell the replay touches has `a<=7`, hence `G<=27` and
   `T_C2<=30` except `d=3,a=7` which is already rejected by `k6`.
   Changing `G<28` into `G<100` or `T<32` into `T<100` would still print
   `PASS`.  Changing the AC coefficient test, if one existed, is
   impossible because the test does not exist.

6. **Tuple convention.**  Replay is internally `(a,d,r)`.  The candidate
   writes the twelve as `(a,d)`, then the subtails as `(a,d)`, then
   suddenly `(a,c,r)=(2,5,>=3)` for the same cell the next paragraph
   calls `(2,3,>=3)`.  This is the same trap as `(1,3,2)` denoting both
   `E` and the low-`a` `d=2` cell in the a2d2 ledger.  The replay cannot
   catch a reader who feeds it `(2,5,3)` as `(a,d,r)` (that would be
   `a=2,d=5`, off the `d in {1,2,3}` loop, silently untested).

7. **Variable names.**  Replay `A0,C0` are the candidate's `A0c,C0c`.
   Harmless for (1.2), lethal if a linker wires those names to stage-zero
   `a0,c0`.

8. **Scope the replay does not touch:** `Phi4` cancellation, the
   radical/open-set statement, equality of `(g1,g2,g4)` to compiler
   `Phi` rows, the transport map, any emitter/tail hash, any promotion
   hash.

The replay is an honest desk check of (1.2) plus a regression pin of the
twelve-set.  It is not a verifier for the polar-contribution theorem or
for replacement of an endpoint.  That is a **REPAIR**, not a
refutation of (1.2).

---

## 7. Attack 6 — minimal linker/schema delta: REPAIR

Producer §4 is the right shape and is not yet enough.  The minimal
reviewed delta, all fail-closed:

1. **Disambiguate `(1.1)`.**  This note's `(1.1)` is the triple
   `(g1,g2,g4)`.  The uniform-transport note's `(1.1)` is the seven
   total-emitter formulas.  The schema must not reuse the number.  Suggest
   `g-triple` vs `emitter-7`.

2. **Pin the tuple.**  One convention per field, written out:
   `a, d, c=a+d, r`.  Reject a manifest that quotes `(2,5,3)` without
   saying which.  Hard-reject `(a,c,r) in {(2,5,3),(2,5,4)}` and the
   registered `(1,2,2),(3,3,4),(4,3,4)` and all of `E`.

3. **Purity predicate is global pole.**  Accept iff
   (i) unique primitive at or before `G` is unloaded `AC/L` with
   coefficient `3/4` and `(R,A,C,pole)=(0,1,1,1)`,
   (ii) every other primitive through `T_C2` except unloaded `C^2/L^2`
   (coefficient `3/8`, `(0,0,2,2)`) has pole `1`,
   (iii) `G<28` and `T_C2<32`.
   Do **not** import the miner's `SAFE_C2_ONLY` /
   `local_pole_upper_at_A_root` bit; that is the allocation-endpoint
   predicate.

4. **Pin the chart and the rows.**
   `C0=(C1 z+C0c)/2`, `A0=A1 z+A0c`, `L=z^2-rho^2`;
   `Phi1=h1`, `Phi2=h2`, `Phi4=h4+(P/2)h2`;
   extracted coefficients equal the `g`-triple symbolically.
   Reject `h4`, reject unbridged `H`, reject stage-zero
   `(a0,a1,c0,c1,rs,cs)` in place of `(A0c,A1,C0c,C1)`.

5. **Theorem type on the output.**  Radical / set-theoretic / DVR-arc
   emptiness on `D(rho) ∩ (D(A0c) ∪ D(A1))`.  Do not emit "unit ideal".

6. **Transport is a separate consumed interface.**  This lemma does not
   identify D1 rows with total rows.  The linker may cite the uniform
   naturality identity at formula level after *that* schema is frozen,
   with generated renaming maps (`k2c` vs `k2load`; D1AC `a1` vs total
   `a1`).  Reverse-direction emptiness is forbidden.

7. **Hashes, not filenames.**  Miner `0e94e540…`; tails / emitter hashes
   from the transport schema; per-contact promotion and review hashes.
   The `(8,3)` filename trap (a file named promotion whose status is
   route falsification) is not in this lemma's twelve, but the same
   discipline applies.

8. **Per-manifest pad-`+1` sentinel** on the polar census.

9. **Mutation controls that must fire**, at predicted grades/cells:
   - `g1` coefficient `3/8 -> 3/4`;
   - `g4` coefficient `3/32 -> 3/16`;
   - drop the `/2` on `C0`;
   - `is_c2` accepts `RA^2`;
   - drop uniqueness at `G` (must fail `a=7`);
   - `G<28` / `T_C2<32` mutated open, on a synthetic or high-`a` cell
     that actually crosses the wall;
   - stage-zero names substituted for shifted leadings;
   - `rho=0` face bytes offered as general-`rho` `Phi[G]`.

10. **Complementary, not competing, with the moving-root linker.**  On a
    contact that fails (3), keep the allocation endpoint.  On a contact
    that passes (3), the three-row lemma may replace the allocation step
    after this schema is frozen and this review's pins are compiled in.
    Until then, no promoted D1 endpoint is replaced.

Producer §4 already lists contact, inventory, bridge hashes, target
schedule, the three coefficients, (1.2), and exact-`A`/`C` plus `D(rho)`.
Items 1–9 above are the delta.

---

## 8. Strongest exact surviving theorem

**Theorem (three-row unique-`AC` syzygy, this review).**
Let `R` be a `Z[1/6]`-algebra.  On the polynomial ring
`R[A0c,A1,C0c,C1,rho]`, the four identities (1.2) hold as equalities of
polynomials.  Consequently, in the radical sense (1.3),

```text
V(g1,g2,g4)  subset  V(C0c, C1)
```

on `D(rho) ∩ (D(A0c) ∪ D(A1))`.  If in addition a contact `(a,c,r)` has
a complete polar inventory through `T_C2=10+2c` in which `AC/L` is the
unique primitive at or before `G=10+a+c`, every other primitive through
`T_C2` except `C^2/L^2` has pole one, `G<28`, and `T_C2<32`, then the
literal source coefficients satisfy

```text
Phi1[G] = g1,   Phi2[G] = g2,   Phi4[T_C2] = g4
```

with `g_i` formed from the shifted leading jets of exact orders `(a,c)`,
and the three equations contradict exact nonzero leading `C` given exact
nonzero leading `A`, on `D(rho)`, at the level of points / DVR arcs.

The contacts for which the inventory hypothesis has been independently
verified in this session are exactly the twelve registered tails of §4.1
and the raised subtails

```text
(a,d,r) = (1,2, r>=3),
          (2,3, r>=5),     i.e. (a,c,r)=(2,5, r>=5),
          (3,3, r>=5),
          (4,3, r>=5).
```

The contacts `(a,c,r)=(2,5,3)` and `(2,5,4)` fail the inventory
hypothesis by a nonzero `RA^2/L^2` term in `Phi4`.  `E` fails by `A^3`.
`a=7` fails by a `k6 C` tie at `G`.  No root allocation, Hensel series,
deck involution, `k10` unit, or `J` unit is used.

Transport of these three equations from D1 to the total emitter is a
separate formula-level identity and is not part of this theorem.
Replacement of any promoted endpoint is not part of this theorem.

---

## 9. Firewalls

Checked against the candidate's text and against the theorem just stated.

- No strict-fan cover.  One lemma plus a finite inventory list.
- No ramified-fibre statement.  `D(rho)` only; the `rho=0` countermodel
  of Attack 1 is explicit.
- No equality-face statement.  `(2,2,2)` and `(3,3,3)` are outside.
- No Rees chart, no terminal receiver.
- No Gate T, order-two, maximum-twelve, JC2, or counterexample claim.
- No whole-fan uniqueness, no claim that `r>=5` repairs `E` or `a=7`.

The candidate's closing denial list is accurate and is adopted here.

---

## 10. Execution record

Desk only.  Independent `Fraction` sparse polynomials for (1.2);
independent four-atom binomial enumerator with aggregation and pad `+1`;
signature comparison to the pinned miner's `enumerate_primitives` (zero
mismatches on the tested box); closed-form wall check against that
census; unmodified producer replay as a self-check of the audited file.
Python 3.14.6, stdlib only.  No AWS, no heavy CAS, no web sweep, no
canonical-ledger edit, no entry into `jc2-lean`.  No campaign artifact
other than this file was written.  Throwaway harness lived in the
process and was discarded.

Git HEAD at review time: `418e413593120d19e15e6546eb50c985f4b1f038`.

**REPAIR** — lemma and contact list hold; replay and linker schema do not
yet license replacement of a promoted endpoint.
