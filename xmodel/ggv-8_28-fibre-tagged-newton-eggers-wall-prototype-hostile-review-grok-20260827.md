# Hostile review: one GGV `8_28` fibre-tagged Newton/Eggers--Wall prototype

**Reviewer:** Grok 4.6 (independent hostile referee). **Date:** 2026-08-27.  
**Target:** the charged freeze of Sol's one-chain control

`cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/`  
together with `xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-sol-20260827.md`.

**Claim under review (narrow):** one explicit non-Keller pair realizes the live GGV `8_28` MN edge, carries fibre-tagged Puiseux/Eggers--Wall data in both infinity charts, and exhibits a coefficient mutation invisible to the current GGV ledger that changes one pole order. **Not** under review: `G2-PSC`, `G2-BD`, a GGV-to-tree functor, global source/landing coverage, a cofinal ceiling, Gate T, order two, maximum twelve, JC2, a Keller counterexample, or a V43-to-K00 ring map.

**Method.** Rehashed the five charged artifacts and the six live source pins. Attempted an independent replay of `verify.py` from the repository root (producer `PASS` was not treated as evidence). Loaded pinned `lib/families.py` and reconstructed the live `8_28` record from `get_pllc` / `get_starting_edges` / `get_complete_chains` / `get_mn_families` / `corner_data`, rather than from a restated table. Rebuilt `z=xy^4`, `B=x(z-1)^7`, `f=B^2-x-y^8`, `g_τ=B^3-2x^2y^2+y^{12}+τ x y^{15}` as sparse integer polynomials. Derived both chart identities, the first fibre-dependent Puiseux coefficients, both deck orientations, the Q/jump/max arithmetic against the pinned Sigray readings (Notation 3.5 Q/max, Statement 3.8, Statement 3.17(ii), Notation 9.1, Proposition 5.5 `c≠0`), the `y=∞` gcd pair by a `μ_{16}` case analysis, and the mutated next coefficient from implicit differentiation. Mutated two asserted formulae and watched them fail. No AWS, no CAS, no `jc2-lean`, no producer-file edits, no canonical-ledger edits.

**Firewall.** This example is non-Keller. It cannot prove a GGV-to-tree functor, global source/landing coverage, `G2-PSC`, `G2-BD`, a cofinal ceiling, Gate T, order two, maximum twelve, JC2, or a counterexample. It supplies no V43-to-K00 ring map. A non-Keller control is not silently upgraded to a Keller-domain counterexample below.

---

## Verdict table

| Item | Verdict |
|---|---|
| Custody | **GAP/REPAIR** |
| GGV-edge realization | **CONFIRMED** |
| `x`-chart / sheets | **CONFIRMED** |
| Q/jump/max and residual descent | **CONFIRMED** |
| `y`-chart / mutation | **CONFIRMED** |
| Global sheet/pole accounting | **CONFIRMED** |
| Fidelity conclusion | **CONFIRMED** (licensed as (a) only) |
| Minimal-packet claim | **GAP/REPAIR** |

No item is **REFUTED**. Two items fail a hostile custody/scope test; the mathematics of the pair, both charts, the Q-data, the mutation, and the sheet/pole arithmetic survive independent replay.

---

## 1. Custody — GAP/REPAIR

Charged freeze SHA256 values all match the review prompt and the internal `FREEZE.sha256` lines:

```text
f5d8e4efd33064dc23dbef3e7b7ad2bd1285631d095922ff6e2894e50863af0a  README.md
4dfe7c6dc1e873892f9128ac2712f319a8c85ffb051701ddafa442d779e11f28  verify.py
deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd  RESULT.json
676bdd3ce960221072f037e7160d457a9d1d64c8e7353891f69e9931ae71149b  FREEZE.sha256
7647f2f118d4fe9fdd060b9e3e9450b58a62e287a80e942cad6de752a3f34ae8  sol report
```

Five of the six live source pins still match. One does not.

```text
MATCH  lib/families.py
MATCH  tests/test_families.py
FAIL   ladder/TRANSPORT.md
       pin  39a607c8935153c814cd51fb65a2f1c708a9e4ba5e1dd0f38f9c96401fc4a624
       live 9750aa9d14650a22a410803022d42fa523e3993a21ee9a27714386fa1150047c
MATCH  xmodel/grok-transport-review.md
MATCH  xmodel/sol-h5a.md
MATCH  xmodel/grok-h5a-review.md
```

The pinned blob is exactly `HEAD:ladder/TRANSPORT.md`. The working tree is a dirty 45-line rewrite (machine gate demoted to a fixture, “repairs G2” rewritten as the T2-to-T4 normalization fork). Those edits follow `xmodel/grok-transport-review.md`; they are not part of this freeze. `python3 cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/verify.py` now exits 1 on `assert observed_pins == SOURCE_PINS` before importing `8_28`. Fail-closed is the correct pin behaviour. It also means the producer `PASS` token in `RESULT.json` cannot be reproduced on the live tree, and is not evidence.

The live `8_28` object itself is intact. From pinned `lib/families.py`, the unique complete chain with path `((8,28),(11/4,7))` and `(m,n)=(3,2)` is

```text
A0=(8,1,28), A0p=(1,1,0), edges=(((8,1,28),(1,1,0)),),
final=(11,4,7), steps=((4,-1,3,4),), mn=(3,2), degs=(108,72),
S=((0,0),(1,0),(8,28),(0,4)), c=4, upper_dir=(-3,1), rhs_exp=2,
SuppP=3S, SuppQ=2S.
```

That is GATE_B / `tests/test_families.py:230-235`, not a restated target. Sol's git archaeology for `families.py`, `test_families.py`, the two H5a notes, and the transport review matches `git log -1` on those paths. Repository HEAD is still the claimed construction commit `418e413593120d19e15e6546eb50c985f4b1f038`.

**Smallest failing hypothesis.** `sha256(ladder/TRANSPORT.md) = 39a607c8935153c814cd51fb65a2f1c708a9e4ba5e1dd0f38f9c96401fc4a624`.

**Minimal additive repair.** Restore `ladder/TRANSPORT.md` to the pinned HEAD blob, *or* commit the working-tree rewrite and re-pin / re-freeze. Do not treat the frozen `PASS` as a live replay until one of those happens. This review did not restore the file.

The Conjecture T warnings Sol cites (HEAD lines 459–463 and 699–701) survive in the dirty file at shifted line numbers. They are not the reason the pin fails.

---

## 2. GGV-edge realization — CONFIRMED

Put `z=xy^4` and `B=x(z-1)^7`. The eight terms of `B` are `x^{k+1} y^{4k}` with binomial signs. Sparse expansion gives `deg f=72` (17 terms) and `deg g_τ=108` (25 terms). Convex hulls:

```text
conv({0} ∪ Supp f) = 2S = {(0,0),(2,0),(16,56),(0,8)},
conv({0} ∪ Supp g_τ) = 3S = {(0,0),(3,0),(24,84),(0,12)}.
```

`Supp g_1 = Supp g_2` as sets: both coefficients of `x y^{15}` are nonzero, and `(1,15)` lies on the Newton edge from `(0,12)` to `(24,84)`, not as an extra vertex. The `(4,-1)`-maximum faces are exactly `B^2` and `B^3` (weights 8 and 12). The monomial `x y^{15}` has weight `4-15=-11`, so it is off the initial face.

Native GGV orientation is `(P,Q)=(g,f)` with multipliers `(3,2)` and degrees `(108,72)`, matching live `cd.mn` and `(cd.degP, cd.degQ)`. Degree-sorted Sigray order is `(f,g)`, type `(2,3)`. The prototype uses the native order for the ledger and the Sigray order for Q-data; that is the correct split, not a silent swap.

Common residual root `z=1` has multiplicity `γ=7`. Face valuation `v_{4,-1}(A_0)=4`, ratio `(ρ+σ)/v=3/4`, and the Algorithm 3 endpoint

```text
a1 = 8·4 + (7-28)·1 = 11,  l1 = 4,  b1 = 7
```

is `(11/4,7)`, equal to live `cd.final`. The same number is `(γ+4)/4=11/4`. The live complete `8_28` chain *is* this single MN edge. Realizing the edge, the `(4,-1)` face, `γ=7`, and the generated corner therefore realizes the complete claimed chain, not a proper sub-edge of a longer GGV path.

Non-Keller witness, recomputed from the sparse Jacobian (93 terms):

```text
[f, g_1]|_{x=0} = -12 y^{11} + 8 y^{22}.
```

A constant Jacobian would restrict to a constant. This slice is nonconstant, so the pair is not Keller. The mutated pair is not Keller either: `[f,g_2]|_{x=0}=-12 y^{11}+16 y^{22}`. The control is not upgraded.

The unique total-degree-72 term of `f` is `x^{16} y^{56}`. That fact is used in §6, not as a Keller claim.

---

## 3. `x`-chart / sheets — CONFIRMED

Substitution `x=s^{-28}`, `y^4=z s^{28}` on every monomial of `f` (all `y`-exponents are multiples of 4) yields the exact identity

```text
s^{56}(f-a) = (z-1)^{14} - s^{28} - z^2 s^{112} - a s^{56},
```

i.e. Sol (3.1). Setting `z=1+ξ s^2 w` with `ξ^{14}=1` and `w(0)=1` gives `w^{14}=1+a s^{28}+z^2 s^{84}`. The `z^2 s^{84}` term starts at order 84, so

```text
w = (1+a s^{28})^{1/14} + O(s^{84}) = 1 + (a/14) s^{28} + O(s^{56}),
z = 1 + ξ s^2 + (a ξ/14) s^{30} + O(s^{58}).
```

The first fibre-dependent coefficient of `z` is therefore `ξ/14` at `s^{30}` for `a=1` versus `a=0`. Then `y=ζ s^7 z^{1/4}` produces

```text
y = ζ s^7 + (ζ ξ/4) s^9 + ⋯ + (a ζ ξ/56) s^{37} + ⋯,
```

so the first fibre-dependent `y` coefficient is `ζ ξ/56` at `s^{37}`. Both match (3.2) and the `RESULT.json` delta strings. The `O(s^{30})` remainder inside Sol's parentheses is weaker than the actual `O(s^{56})`; it is not false.

There are `4·14=56` presentations `(ζ,ξ)`. For primitive `ω∈μ_{28}`, `s↦ω^{±1}s` acts by

```text
(ζ,ξ) ↦ (ζ ω^{±7}, ξ ω^{±2}).
```

Indexing `ζ=i^u`, `ξ=exp(2π i v/14)` makes this the diagonal action `(u,v)↦(u±1,v±1)` modulo `(4,14)`. Both orientations generate the same two free orbits of length 28 (`lcm(4,14)=28`). The bit

```text
ε = ζ^2 / ξ^7 = (-1)^{u-v} ∈ {+1,-1}
```

is constant on each orbit and opposite on the two orbits; `ξ^7` alone is not invariant. So this chart has exactly two geometric places, each of ramification 28 over `x=∞`.

**Overlap/loss attack.** These places have `x→∞` and `y∼ζ s^7→0`, i.e. the projective point `[1:0:0]`. The `y=∞` places of §5 have `y→∞` and `x=t^3 X→0`, i.e. `[0:1:0]`. The unique degree-72 form `x^{16} y^{56}` meets the line at infinity only at those two points, with intersection multiplicities 56 and 16. There is no `(∞,∞)` branch, no double-counted place, and no missing infinity place. Completeness is the Bézout count `56+16=72`, refined as `2·28+16·1`, not a bare degree sum.

The producer verifier never expands the Puiseux series: its fibre-delta “check” is the tautology `(1/14)·14=1`. That is a gate weakness, not a hole in (3.1)–(3.2). The expansions above do not depend on the producer `PASS`.

---

## 4. Q/jump/max and residual descent — CONFIRMED

As a series in `X=1/x=s^{28}`,

```text
y = ζ X^{7/28} + (ζ ξ/4) X^{9/28} + ⋯.
```

Characteristic numerators `(κ; β_1,β_2)=(28;7,9)`: 9 is not in the semigroup `7+7ℕ`. Gcd chain `e_0=28`, `e_1=gcd(28,7)=7`, `e_2=gcd(7,9)=1`. Jump indices `ν=(28/7,7/1)=(4,7)`. Q/max values `κ_F: 1 → 4 → 28` (initial lattice, then `e_0/e_1`, then `e_0/e_2`). Characteristic exponents `π=(1/4,9/28)`. Barred values `κ̄=κ(1-π)` give `4·(3/4)=3` and `28·(19/28)=19`, with `gcd(3,4)=gcd(19,7)=1` (N1). This is Notation 3.5 evaluated on the jump/max presentation, the unique uniform repair forced by printed Statement 3.8 and recorded in pinned `xmodel/sol-h5a.md` / `xmodel/grok-h5a-review.md`.

Coarse cut `η=x^{1/4} y` has `f`-residual `(η^4-1)^{14}`, i.e. `(η^ν-1)^M` with `ν=4`, `M=14`, `deg p_f=56`. Leading `d_f=2`, `d_g=3` are the type-`(2,3)` root values (Sigray order, not native `(3,2)`). Notation 9.1 tuple:

```text
Q(F_0) = (κ d_f, deg p_f, ν, M, κ̄) = (8,56,4,14,3).
```

Refinement `η=ζ+x^{-1/14} θ` and Statement 3.17(ii) in the deeper-child direction:

```text
d_{f,1} = 2 - (9/28-1/4)·14 = 1,
d_{g,1} = 3 - (9/28-1/4)·21 = 3/2.
```

The ratio `d_g/d_f=3/2` is preserved, matching corrected Proposition 5.3(ii) for type `(2,3)`. Residuals (3.6):

```text
p_f = K_ζ^2 θ^{14} - 1,     K_ζ=(4ζ^3)^7,  d_f=1,
p_g = K_ζ^3 θ^{21} - 2ζ^2,                 d_g=3/2.
```

At the `f`-root `θ=ζ ξ/4` one has `p_f=0` and `p_g=ξ^7-2ζ^2`. On the two orbits, with `ξ^7=(-1)^v` and `ζ^2=(-1)^u`, this is one of `{±1,±3}`, never zero. Noncancellation on both orbits. Refined tuple and paired degree:

```text
Q(F_1)=(28,14,7,1,19),   D_{g,F_1}=28·(3/2)=42.
```

Using the coarse value 4 at the second cut would give `D_f=4` and `κ̄=19/7∉ℤ`, contradicting Statement 3.8 and destroying the integer Q-datum. Proposition 5.5 with `c≠0` labels each place a `g`-pole of order `D_g=42`. Total

```text
Λ_x = D_g · deg(p_f)/ν = 42·14/7 = 84 = 2·42.
```

Component-order check: native `(m,n)=(3,2)` was *not* fed to Sigray Q. Descent, type ratio, and pole order all use `(f,g)=(2,3)`. No convention mismatch.

---

## 5. `y`-chart / mutation — CONFIRMED

Newton edge of `f` from `(0,8)` to `(16,56)` forces the chart `x=t^3 X`, `y=t^{-1}`. Exact identities:

```text
t^8(f-a) = X^2(X-t)^{14} - 1 - a t^8 - X t^{11},          (4.1)
t^{12} g_τ = X^3(X-t)^{21} + 1 + τ X - 2 X^2 t^{16}.      (4.3)
```

At `t=0`, `X^{16}-1=0`, 16 simple roots, 16 unramified places. Implicit differentiation of (4.1) at `t=0` gives `∂F/∂X=16 c^{15}` and `∂F/∂a=-t^8`, so the first `a`-dependent coefficient is

```text
X_1(t)-X_0(t) = (c/16) t^8 + O(t^9),
x_1-x_0 = (c/16) t^{11} + O(t^{12}).
```

Pole residual of `g` on an `f`-leaf: `c^{24}+1+τ c=c^8+1+τ c`.

**Gcd statements, proved on `μ_{16}` rather than by a black-box Euclidean run.** If `c^{16}=1` then `c^8=±1`.

- `τ=1`: `c^8=1` forces `c=-2∉μ_{16}`; `c^8=-1` forces `c=0`. Hence `gcd(X^{16}-1,X^8+X+1)=1`.
- `τ=2`: `c^8=1` forces `c=-1∈μ_{16}`; `c^8=-1` forces `c=0`. Derivative `8X^7+2` at `-1` is `-6≠0`, so the common factor is exactly `X+1`. Euclidean algorithm independently returns `[1]` and `[1,1]`.

Thus `τ=1` has no cancellation (all 16 places are poles of order 12) and `τ=2` cancels only at `c=-1`.

At *every* `c∈μ_{16}`, including the cancelled root, `X'(0)=14/16=7/8`. Differentiating (4.3) at `c=-1`, `τ=2`:

```text
G'(0) = (24 c^{23}+τ) X'(0) - 21 c^{23} = 21 - 22·(7/8) = 7/4 ≠ 0.
```

The `t^{16}` term does not contribute at order 1. So `t^{12} g_2 = (7/4) t + O(t^2)` along that branch, and the pole order drops `12→11` because the next coefficient is nonzero, not because the leading residual vanished. The producer formula `21-22·(7/8)` is the `c=-1` specialisation of the general derivative, not a lucky coincidence.

**Sensitivity.** Replacing the asserted next-coefficient identity by `21-21·(7/8)` yields `21/8 ≠ 7/4`. Replacing (3.1) by `(z-1)^{15}=…` falsifies the exact `x`-chart identity. The review is sensitive to both mutations.

The mutation `τ=1→2` does not change support, Newton polygons, the live GGV record, the `(4,-1)` faces, `γ`, the two fibre-tree sheet counts, or the `x=∞` paired residual `ξ^7-2ζ^2`.

---

## 6. Global sheet/pole accounting — CONFIRMED

What `2·28+16=72` has been shown to be: the intersection of the degree-72 curve `{f=a}` with the line at infinity, split as two ramified-28 places at `[1:0:0]` (multiplicity 56) and sixteen unramified places at `[0:1:0]` (multiplicity 16), with no overlap and no missing infinity place (§3). It is the sheet count of the smaller component at infinity. It is **not** the topological degree of a proper Keller map, **not** a proof that a Sigray tree functor has been defined, and **not** an exhaustion of finite places.

Pole masses then follow from the per-place orders, given noncancellation:

```text
baseline:  2·42 + 16·12 = 84+192 = 276,
mutated:   2·42 + 15·12 + 11 = 84+180+11 = 275.
```

These are sums of `ord_P(g)_∞` over the 18 geometric infinity places of `{f=a}`. They are not Sigray `td` (and `276≠72`, as expected for a non-proper non-Keller pair). All 18 places remain pole-labelled after the mutation; only one order drops.

---

## 7. Fidelity conclusion — CONFIRMED as (a) only

Live GGV fields unchanged by `τ=1→2`, because none of them depends on the lower term `τ x y^{15}`:

```text
A0, A0', chain, final, steps=(4,-1,3,4), k, family, mn=(3,2),
degP, degQ, S, c, upper_dir, rhs_exp.
```

Polynomial-visible GGV data likewise unchanged: support, Newton polygons `2S`/`3S`, common `(4,-1)` faces `B^2`/`B^3`, `γ=7`, endpoint `(11/4,7)`, both fibre-tree sheet counts, and the `x=∞` residual `ξ^7-2ζ^2`.

The pair realizes the *complete* live `8_28` chain, which happens to be one MN edge. It does not realize a longer GGV path.

The mutation proves **(a)**: the current GGV ledger is insufficient to determine this fibre-tagged residual/pole packet for arbitrary polynomial controls with that ledger. Two polynomials with identical support, Newton polygons, complete-chain record, initial face, `γ`, and sheet counts have pole masses 276 and 275, distinguished immediately by `gcd(X^{16}-1,X^8+1+τ X)`.

The mutation does **not** prove **(b)**: insufficiency for actual Keller pairs. Jacobian-one may still pin down residuals that the ledger alone does not. Sol §0 and §7 already refuse G2-PSC, Conjecture T, and any Keller promotion. Section 5's phrase “any proposed transport whose input is only the current GGV packet” is licensed only as (a). This review does not strengthen it.

---

## 8. Minimal-packet claim — GAP/REPAIR

Sol §6 lists eight fields as a “minimal sufficient typed packet.” As a *sufficient* packet for *this* example the list is reasonable. As a *minimal* list, and as a list of fields *proved necessary by this collision*, it is too large.

**Proved necessary by the `τ=1→2` collision**

- the `y=∞` paired residual `X^8+1+τ X` (equivalently `X^{24}+1+τ X` modulo `X^{16}-1`);
- roots and cancellation multiplicity of that residual on `μ_{16}`;
- the resulting pole orders `{12^{×16}}` versus `{12^{×15},11^{×1}}`;
- the source monomial `x y^{15}` that feeds `τ`.

**Supported by the example, but not by the collision**

- fibre tag `a`: `a=0` versus `a=1` changes the `s^{30}`/`s^{37}`/`t^8` coefficients and is invisible to the GGV ledger; both fibres see the same `τ`-mutation;
- both chart maps: the collision is detected entirely in the `y`-chart; the `x`-chart is required for the complete packet of this pair (two ramified places, Q-data, pole 42) and to rule out overlap, not to separate `g_1` from `g_2`;
- `x`-chart paired residuals, deck/`μ_{28}` grouping into two places, Q/jump/max: identical for both `τ`;
- a general inverse map “tying each residual coefficient back to the polynomial coefficient that produced it”: the example traces `τ x y^{15}` to (4.4) and `B=(z-1)^7` to the faces. It does not construct such a map for every coefficient.

**Merely listed, not evidenced as necessary**

- named parent/child flag identifiers beyond the two `x`-cuts and the 16 `y`-keys actually computed;
- “exact source pair and component orientation” as a packet *field* rather than as the definition of the example;
- a provenance map at the strength of item 8 of §6.

The existing lattice fields `(A_0,A'_0)`, `(ρ,σ,p,q)`, `(m,n)`, `S`, `c`, `upper_dir`, `rhs_exp`, `A_γ` are correctly described as enough for the edge skeleton and not enough for (3.2), (4.4), pole orders, or pole mass.

**Smallest failing hypothesis.** “The eight listed fields are a *minimal* typed packet forced by this collision.”

**Minimal additive repair.** Relabel §6 as “sufficient packet for this example.” Mark as collision-necessary only the `y`-chart paired residual, its roots/multiplicities, the pole-order vector, and the source term `x y^{15}`. Mark as example-supported, not collision-forced: fibre tag, both chart substitutions, `x`-chart residuals, deck/place grouping, Q/jump/max, and the fragmentary provenance of `τ` and `γ`. Do not require a total inverse/source map on the strength of this one pair.

---

## Replay record (independent, not the producer `PASS`)

- Freeze artifacts: 5/5 SHA256 match.
- Live pins: 5/6 match; `ladder/TRANSPORT.md` working tree drifted from the pinned HEAD blob.
- Producer verifier: exits 1 on the pin assert; `RESULT.json` `"status":"PASS"` was not replayed and is not used as evidence.
- Live `8_28` from pinned `lib/families.py` constructors: GATE_B match.
- Sparse pair, hulls, faces, Algorithm 3 endpoint, Jacobian slice: match Sol (2.1) and the non-Keller witness.
- Chart identities (3.1), (4.1), (4.3): exact.
- First fibre-dependent coefficients: `ξ/14` at `s^{30}`, `ζξ/56` at `s^{37}`, `c/16` at `t^8`.
- Deck: 56 presentations, both orientations, two length-28 orbits, invariant `{±1}`, residual `ξ^7-2ζ^2≠0`.
- Q-data: `(8,56,4,14,3)` and `(28,14,7,1,19)`, `D_g=42`, mass 84, descent `1` and `3/2`, barred `3,19`.
- Gcds: `1` and `X+1`. At `τ=2`, `c=-1`: `X'(0)=7/8`, next coefficient `7/4`, pole `12→11`.
- Accounting: `2·28+16=72`, masses `276/275`.
- Sensitivity: `21-21·(7/8)=21/8≠7/4`; `(z-1)^{15}` fails the `x`-chart identity.

---

## Licensed conclusion

The prototype does what it claims at the one-chain, non-Keller, one-mutation scope: it realizes live GGV `8_28`, attaches fibre-tagged Newton/Eggers--Wall data in both infinity charts, tests Q/jump/max `1→4→28` against the pinned Sigray readings, and shows that the current lattice ledger does not determine pole orders for polynomial controls with that ledger. Two repairs remain: restore or re-pin `ladder/TRANSPORT.md` so the desk verifier can actually replay, and stop calling the §6 field list minimal. Nothing here is a GGV-to-tree functor, a Keller counterexample, or G2-PSC.
