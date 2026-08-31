# PI1-S4 verification r2 — computation and countermodel arm

Lane: verification (independent of gate). Desk-scale exact reasoning only.
Date: 2026-08-31. Agent: grok-4.6.

Charged inputs (frozen SHA-256 verified):

- `010330d208c5899ce41832f1187b73d9a63268725d809b0370f2b4d9cd66eadd` `pi1-s4-decision-opus5-20260831.md`
- `bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963` `block-descent-a1-b0-coordinator-integration-fable5-20260831.md`

## 0. Hash check and scope

Frozen copies hashed with `shasum -a 256` before any reading; both match the boxed values:

```text
010330d208c5899ce41832f1187b73d9a63268725d809b0370f2b4d9cd66eadd  pi1-s4-decision-opus5-20260831.md
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963  block-descent-a1-b0-coordinator-integration-fable5-20260831.md
```

Coordinator residual is the PI1-S4 question (integration §2) with the binding stop that the acquisition's local-relations claim is an inference. This arm does not inspect `jc2-lean`, does not edit charged files, and runs no CAS. No primary PDF was re-fetched: the seven targets are finite-group, Hurwitz, and blow-up arithmetic. Convention throughout: Artin/Hurwitz action of `σ_i` on a `d`-tuple is

```text
(t_1,...,t_d)  |->  (..., t_i t_{i+1} t_i^{-1}, t_i, ...)
```

and a word acts left-to-right as composition, so `δ = σ_1 ... σ_{d-1}` applies `σ_{d-1}` first.

## 1. Delta-action formula (d=2,3,4; delta^d at d=3)

Claim (decision §3.3): `δ · (t_1,...,t_d) = (Π t_d Π^{-1}, t_1, ..., t_{d-1})` with `Π = t_1 ... t_d`.

**d=2.** `δ = σ_1`. Direct: `σ_1 · (t_1,t_2) = (t_1 t_2 t_1^{-1}, t_1)`. Claimed first slot: `Π t_2 Π^{-1} = (t_1 t_2) t_2 (t_1 t_2)^{-1} = t_1 t_2 t_1^{-1}`. Matches.

**d=3.** `δ = σ_1 σ_2`: apply `σ_2` then `σ_1`.

```text
(t_1,t_2,t_3)
  --σ_2-->  (t_1, t_2 t_3 t_2^{-1}, t_2)
  --σ_1-->  (t_1 t_2 t_3 t_2^{-1} t_1^{-1}, t_1, t_2)
```

Claimed first slot: `Π t_3 Π^{-1} = t_1 t_2 t_3 t_3 (t_1 t_2 t_3)^{-1} = t_1 t_2 t_3 t_2^{-1} t_1^{-1}`. Matches.

**d=4.** `δ = σ_1 σ_2 σ_3`: apply `σ_3`, `σ_2`, `σ_1`.

```text
(t_1,t_2,t_3,t_4)
  --σ_3-->  (t_1, t_2, t_3 t_4 t_3^{-1}, t_3)
  --σ_2-->  (t_1, t_2 t_3 t_4 t_3^{-1} t_2^{-1}, t_2, t_3)
  --σ_1-->  (t_1 t_2 t_3 t_4 t_3^{-1} t_2^{-1} t_1^{-1}, t_1, t_2, t_3)
```

Claimed first slot: `Π t_4 Π^{-1} = t_1 t_2 t_3 t_4 t_3^{-1} t_2^{-1} t_1^{-1}`. Matches.

Hurwitz preserves the ordered product at each step (checked at d=3 for the later iterate: new product `(Π t_3 Π^{-1}) t_1 t_2 = Π t_3 Π^{-1} Π t_3^{-1} = Π`). So the same `Π` may be reused.

**`δ^3` at d=3.** Write `T^{(0)} = (t_1,t_2,t_3)`. The formula and product-invariance give

```text
T^{(1)} = (Π t_3 Π^{-1}, t_1, t_2)
T^{(2)} = (Π t_2 Π^{-1}, Π t_3 Π^{-1}, t_1)
T^{(3)} = (Π t_1 Π^{-1}, Π t_2 Π^{-1}, Π t_3 Π^{-1})
```

Global conjugation by `Π`. HOLDS. (The identification `δ^d = Δ_d^2` is classical and not needed for the target.)

**Verdict. HOLDS.**

## 2. Theorem A(3) orbit enumeration on S_4 transpositions

Six transpositions: `(12),(13),(14),(23),(24),(34)`. Conjugacy classes of `S_4` and the `<g>`-orbits on that set. An orbit "works" if it generates `S_4`.

**g=1.** Six orbits of size 1. Each generates `Z/2`. Fails.

**g a transposition**, take `g=(12)` (class size 6). Conjugation swaps labels 1 and 2.

| seed | orbit | group |
|---|---|---|
| `(12)` | `{(12)}` | `Z/2` |
| `(13)` | `{(13),(23)}` | `S_3` on `{1,2,3}` |
| `(14)` | `{(14),(24)}` | `S_3` on `{1,2,4}` |
| `(34)` | `{(34)}` | `Z/2` |

No working orbit.

**g a double transposition**, take `g=(12)(34)` (class size 3; order 2).

| seed | orbit | group |
|---|---|---|
| `(12)` | `{(12)}` | `Z/2` |
| `(34)` | `{(34)}` | `Z/2` |
| `(13)` | `{(13),(24)}` | Klein four |
| `(14)` | `{(14),(23)}` | Klein four |

No working orbit.

**g a 3-cycle**, take `g=(123)` (class size 8; fixes 4). Labels cycle `1→2→3→1`.

| seed | orbit | group |
|---|---|---|
| `(12)` | `{(12),(23),(13)}` | `S_3` on `{1,2,3}` |
| `(14)` | `{(14),(24),(34)}` | `S_4` |

The second generates `S_4` because `(14)(24)(14)=(12)` and likewise the other transpositions on `{1,2,3}`. Exactly the two orbits of size 3 claimed: star at the fixed point works; the `S_3` on the moved letters fails.

**g a 4-cycle**, take `g=(1234)` (class size 6). Labels cycle `1→2→3→4→1`.

| seed | orbit | group |
|---|---|---|
| `(12)` | `{(12),(23),(34),(14)}` | `S_4` |
| `(13)` | `{(13),(24)}` | Klein four |

The 4-orbit generates `S_4` (`(12),(23)` give `S_3` on `{1,2,3}`, then `(34)` brings in 4). The 2-orbit of opposite edges fails. Decision §3 names the working 4-orbit and does not list this 2-orbit; the existence claim is still correct.

**Consequence.** A conjugation orbit of a transposition generates `S_4` only for `ord(g)∈{3,4}`, and then only for the star-at-fixed-point 3-orbit or the 4-cycle adjacent orbit. Two transpositions never generate `S_4` (share a letter ⇒ `S_3`; disjoint ⇒ Klein), so `n≥3`. With `Π^n=1` and `sgn(Π)=(-1)^d`: 3-cycle is even ⇒ `d` even and `3|n`; 4-cycle is odd ⇒ `d` odd and `4|n`.

**Verdict. HOLDS.**

## 3. Exponent-sum cross-check at (4,3) and (5,3)

Coprime stratum. Three evaluations of `e(ρ_∞)`:

- **(V)+factorization:** `V=d-1` simple tangency factors of exponent 1, plus exponent `2k_p` at each double point, so `e=(d-1)+2 δ_aff`.
- **(G)+cusp:** `δ_aff + δ_∞ = (d-1)(d-2)/2` and `δ_∞=(d-n-1)(d-1)/2`, hence `2 δ_aff=(n-1)(d-1)` which is **(D)**, and `e=n(d-1)`.
- **(identification):** `ρ_∞=δ^n` up to conjugacy, `e(δ)=d-1`, so `e(δ^n)=n(d-1)`.

**(d,n)=(4,3).** `gcd=1`, `a=1`, `b=4`. Flex: `δ_∞=(0)(3)/2=0`. (G): `δ_aff=3`. (V): `V=3`. Factorization: `e=3+6=9`. (D): `2 δ_aff=6=(2)(3)`. `n(d-1)=9`. All three give 9.

**(d,n)=(5,3).** `gcd=1`, `a=2`, `b=5`. `δ_∞=(1)(4)/2=2`. (G): `δ_aff+2=6`, `δ_aff=4`. (V): `V=4`. Factorization: `e=4+8=12`. (D): `8=(2)(4)`. `n(d-1)=12`. All three give 12.

(Note: `(5,3)` is later killed by Theorem A(2) because both degrees are odd; the exponent-sum identity is independent of that obstruction.)

**Verdict. HOLDS.**

## 4. Theorem A kill-list and surviving (d,n) with d<=9

Standing constraints from §1 of the decision: `d>n≥1`. (C1): `gcd(d,n)=1`. Theorem A: `n≥3` (hence `d≥4`); either (`3|n` and `d` even) or (`4|n` and `d` odd). The two branches are exclusive by sign: a 3-cycle is even, a 4-cycle is odd.

**Both odd dies.** `sgn(Π)=(-1)^d` and `sgn(Π)^n=1` force `dn` even. Any pair with both odd is dead, including coprime examples `(5,3),(7,3),(7,5),(9,5),(9,7)`.

**`n≤2` dies.** Two transpositions never generate `S_4` (§2). Kills `(d,1)` for all `d` and `(d,2)` with `d` odd (the coprime subcase).

**Survivors with `d≤9`.** Even `d∈{4,6,8}`, `n` a multiple of 3, `3≤n<d`, `gcd=1`:

- `(4,3)`: `gcd(4,3)=1`. Keep.
- `(6,3)`: `gcd=3`. Dead by (C1). No other `n`.
- `(8,3)`: `gcd=1`. Keep. `(8,6)`: `gcd=2`. Dead.

Odd `d∈{5,7,9}`, `n` a multiple of 4, `4≤n<d`, `gcd=1`:

- `(5,4)`: keep.
- `(7,4)`: keep. `(7,8)` has `n>d`.
- `(9,4)`: keep. `(9,8)`: `gcd(9,8)=1`. Keep.

Six surviving pairs: `(4,3),(5,4),(7,4),(8,3),(9,4),(9,8)`.

**Verdict. HOLDS.**

## 5. Lemma 4.4 blow-up arithmetic

Coprime `(a,b)`-cusp, `a≤b`, `gcd=1`. Euclidean blow-ups: multiplicity `a` replaces `(a,b)` by `(a,b-a)` (swap if needed), terminate at `(1,1)` with one last blow-up. Recursion `M(a,b)=a+M(a,b-a)`, `N(a,b)=a^2+N(a,b-a)`, base `M(1,1)=1`, `N(1,1)=1`, solved by `M=a+b-1`, `N=ab`. Equivalence `N-(a-1)(b-1)=M` is the identity `ab-(a-1)(b-1)=a+b-1`. Sequences recomputed (report omitted `(5,7)` from its displayed list):

| (a,b) | multiplicity sequence | M | a+b-1 | N | ab |
|---|---|---|---|---|---|
| (2,3) | 2,1,1 | 4 | 4 | 6 | 6 |
| (2,5) | 2,2,1,1 | 6 | 6 | 10 | 10 |
| (2,7) | 2,2,2,1,1 | 8 | 8 | 14 | 14 |
| (3,4) | 3,1,1,1 | 6 | 6 | 12 | 12 |
| (3,5) | 3,2,1,1 | 7 | 7 | 15 | 15 |
| (3,7) | 3,3,1,1,1 | 9 | 9 | 21 | 21 |
| (4,5) | 4,1,1,1,1 | 8 | 8 | 20 | 20 |
| (5,7) | 5,2,2,1,1 | 11 | 11 | 35 | 35 |

Each also satisfies `∑ m_j(m_j-1)=(a-1)(b-1)`. Convert `(a,b)=(d-n,d)` so `C'^2=d^2-N=d^2-(d-n)d=nd`. Three pairs:

- `(2,3)` → `(d,n)=(3,1)`: `C'^2=9-6=3=nd`.
- `(2,5)` → `(5,3)`: `C'^2=25-10=15=nd`.
- `(5,7)` → `(7,2)`: `C'^2=49-35=14=nd`.

**Verdict. HOLDS.**

## 6. Noncoprime (4,2) example and a second (6,2) or (6,3) data point

**Worked `(d,n)=(4,2)`.** `γ(t)=(t^4, t^2+t)`. Immersion: `γ'=(4t^3,2t+1)` never zero. Birational: only finitely many double parameters (computed below). Chart at `Q=[1:0:0]`: `s=1/t`, `(v,u)=(s^2+s^3,s^4)`. Tangent `u=0=L_∞`, `mult_Q=2`, `I(D̄,L_∞;Q)=4`.

`(2,5)`-cusp: `v^2=s^4(1+s)^2=u(1+s)^2`. Reparam `τ=s√(1+s)` so `v=τ^2`; invert `s=τ-(1/2)τ^2+O(τ^3)`. Then `u=s^4=τ^4-2τ^5+O(τ^6)`. Automorphism `U=u-v^2` gives `U=-2τ^5+O(τ^6)`, `V=v=τ^2`. Germ is the `(2,5)`-cusp.

Embedded resolution including transversality to `B_∞`:

1. Mult 2 at `Q`. Chart `V=v`, `U=u/v`: `(U,V)=(s^2/(1+s), s^2(1+s))`, still at the origin, mult 2, tangent `U=V` distinct from `E_1` and `L'`.
2. Mult 2. Chart `W=V`, `Z=U/V`: at `s=0`, `(W,Z)=(0,1)`. Set `ζ=Z-1~-2s`, `W~s^2`. Smooth, tangent to `E_2`, contact 2, not at a node of `B_∞`.
3. Mult 1 (simple tangency to `E_2`). After this, `C'` meets `E_2'∪E_3` at the node `E_2'∩E_3`.
4. Mult 1, separates: `C'` meets the newest exceptional transversely at a smooth point of `B_∞`.

Sequence `2,2,1,1`. `M_∞=6≤9=3d-3`. `N=10`, `C'^2=16-10=6`. `δ_∞=∑m(m-1)/2=2`, so (G) gives `δ_aff=3-2=1`.

Affine double points: `t^4=s^4` and `t^2+t=s^2+s`, `t≠s`. Then `s=tω`, `ω^4=1`, `ω≠1`. `ω=-1` forces `t=0`. `ω=i`: `t=-(1-i)/2`, `s=-(1+i)/2`, one pair. `ω=-i` repeats that pair. So `s=1` (one node, `k=1`), matching `δ_aff=1`. Decision §9's `C'^2=6>2=2s` holds.

**(M-INF) data point `(d,n)=(6,2)`.** `γ(t)=(t^6,t^2+t)`. Immersion: `γ'=(6t^5,2t+1)` never zero. Birational: `s=tω` with `ω^6=1` yields finitely many pairs (`ω=-1` gives only `t=0`; other `ω` give `t=-1/(1+ω)`). One place at infinity: `(v,u)=(s^4+s^5,s^6)`, `mult_Q=4`, `I=6`.

Blow-ups:

1. Mult 4. Chart `U=u/v`, `V=v`: `(s^2/(1+s), s^4(1+s))`, mult 2, tangent `V=0=E_1`.
2. Mult 2. Chart `X=U`, `Y=V/U`: `(s^2/(1+s), s^2(1+s)^2)`, mult 2, tangent `Y=X` distinct from `E_2` and `E_1'`.
3. Mult 2. Chart `W=Y`, `Z=X/Y`: at `s=0`, `(0,1)`. Then `ζ=Z-1~-3s`, `W~s^2`. Smooth, tangent to `E_3` at `[X:Y]=[1:1]`, which is distinct from `E_2∩E_3=[0:1]` and `E_1'∩E_3=[1:0]`. Contact 2.
4–5. Two mult-1 blow-ups, same transversality bookkeeping as above.

Sequence `4,2,2,1,1`. `M_∞=10≤15=3d-3`. (M-INF) holds on this example. `N=26`, `C'^2=10`, `δ_∞=8`, `δ_aff=2`, and `C'^2>2δ_aff` with slack 6, matching Lemma 4.3 (`3d-2-M=6`). This is one numerical point, not a proof of (M-INF) in general.

**Verdict. HOLDS** (claimed `(4,2)` data, and (M-INF) on an additional `(6,2)` example). Residual general (M-INF) remains OPEN, as the decision typed it.

## 7. Countermodel hunt: Theorem C transport at d=4,n=3

Smallest coprime survivor is `(d,n)=(4,3)`: `δ_aff=3`, `δ_∞=0` (hyperflex). Tangential members have type `A_3`+node or `A_5`.

**Concrete `A_3` member of `P_{4,3}`.** `γ(t)=(t^4+t^2-2t,\ t^3-t)`. Immersion: `γ'=(4t^3+2t-2,\ 3t^2-1)`; at `3t^2=1` one has `10/(3√3)≠2`. Parameters `0,1` both give `(0,0)` with parallel velocities `γ'(0)=(-2,-1)`, `γ'(1)=(4,2)=-2·γ'(0)`. The 2-jet obstruction is nonzero (`γ''(0)+` reparametrized `γ''(1)` is not tangent-parallel), so contact is exactly 2: type `A_3`. Remaining length 1 is the node with parameters `-1±i√2` (`σ=t+s=-2`, `π=ts=3`). No third parameter through the origin (`p(-1)=4`). So a legal PI1-S4 curve, not a triple point. (Pure fourth-power `p=t^4` was a trap: forcing a tacnode at `{1,i}` collapsed `{1,i,-i}` to a triple point.)

**Schematic ZvK.** Generic fibre meridians `ξ_1,...,ξ_4`. Discriminant: three simple vertical tangencies (`p'(t)=2(2t^3+t-1)=0`, derivative `6t^2+1` shares no root with the cubic) plus the tacnode at `x=0` plus one node. Factorization type in `B_4`, exponent sum 9:

```text
ρ_∞  ~  (w_1 σ w_1^{-1}) (w_2 σ w_2^{-1}) (w_3 σ w_3^{-1})
        (w_N σ^2 w_N^{-1}) (w_A σ^4 w_A^{-1})
```

with `ρ_∞` conjugate to `δ^3` by (C1). Relations: three of type `(T)` (identify a conjugate pair), one `(N_1)` (commute a conjugate pair), one `(N_2)` (`[(ζ_a ζ_b)^2, ζ_a]=1`). No relation `ξ_4···ξ_1=1` (affine ZvK; projection proper). Connecting braids `w_•` are the sheet-order transports from a reference fibre; they are not determined by the numerical type. Writing them requires tracking the four roots of `p(t)-x=0` around five loops, which is not desk-scale exact arithmetic.

**Theorem A tuple.** Up to conjugacy in `S_4` the only candidate is the 3-orbit of a 3-cycle: `T=((14),(34),(24),(14))` with `Π=(123)` (checked: ordered product is `(123)`, and `δ^3` acts as the period-3 shift). Consecutive entries of this `T` are never equal and never disjoint (the three distinct values are the star at 4). One Hurwitz move already produces disjoint pairs, e.g. `σ_2·T=((14),(23),(34),(14))`. So there is no cheap obstruction of the form "the reference tuple contains no disjoint pair". Whether the actual local pair at this `A_3` (the two branches with `t∈{0,1}`, as opposed to the two other points of the fibre `x=0`, namely `γ` at the roots of `t^2+t+2=0`) is a disjoint pair in some Hurwitz frame of `T` is exactly the missing connecting-braid data.

**Transport of the representation, independently of those braids.** If a disjoint-transposition `φ` exists on the `A_3` curve, §2 gives `[φ(ζ_a),φ(ζ_b)]=1` (disjoint transpositions commute; they satisfy `(N_k)` for every `k`, and the nodal relation). Lemma 5.6's local `B_2` analysis is desk-checkable and holds: an `A_3` lives in a 2-strand tube, `B_2` is abelian, so a nearby splitting into two nodes imposes twice the same relator `[w(ξ_a),w(ξ_b)]=1`. Thus `φ` kills every extra relator in `(*)` and factors through `π_1` of a nearby nodal member. Nearby nodal members exist in `P_{4,3}`: `δ_aff=3` is constant (Lemma 5.3, `a=1`), and the length-2 scheme at `{0,1}` splits. That is the representation-transport Theorem C actually uses. It does not require `π_1(C^2-D_0)≅π_1(C^2-D_t)`.

**Strictly larger complement group.** Whether `[w(ξ_a),w(ξ_b)]` is nontrivial in `π_1` of this `A_3` quartic (so the group would strictly surject onto the nodal neighbour) is a computation of that group. Theorem B makes the nodal neighbour abelian, but computing the tacnodal group from the incomplete ZvK above is not desk-scale. No family is exhibited. Typed `OPEN`, not filled by the coprime abelian conclusion or by analogy with Nori's unstated `B(C)>0` extension.

**Direct existence of `φ` for this curve.** Same missing braids. No desk enumeration of factorizations of `δ^3` in `B_4` of type `(σ,σ,σ,σ^2,σ^4)` was performed (CAS-scale).

**Verdict. HOLDS** for existence of an `A_3` member and for tautological transport of any disjoint-transposition representation through `(*)`. **UNTESTABLE-AT-DESK** for an explicit numbered ZvK, for a direct yes/no on `φ` for this curve, and for a family with strictly larger `π_1`.

## 8. Verdict table

| # | Target | Verdict |
|---|---|---|
| 1 | `δ`-action at `d=2,3,4`; `δ^3` = conjugation by `Π` at `d=3` | HOLDS |
| 2 | `<g>`-orbits on the six transpositions, all classes in `S_4`; working 3-cycle and 4-cycle orbits; failures | HOLDS |
| 3 | `e(ρ_∞)` both ways at `(4,3)` and `(5,3)` via (V), (G), (D) | HOLDS |
| 4 | Kill-list (both odd; `n≤2`); survivors `d≤9` under (C1)+A(3) | HOLDS — survivors `(4,3),(5,4),(7,4),(8,3),(9,4),(9,8)` |
| 5 | Multiplicity sequences for eight coprime pairs; `M=a+b-1`, `N=ab`; `C'^2=nd` at three pairs | HOLDS |
| 6 | `(4,2)` example is a `(2,5)`-cusp, sequence `2,2,1,1`, `M_∞=6`, `s=1`; extra `(6,2)` has `M_∞=10≤15` | HOLDS as data; general (M-INF) remains the decision's `OPEN[PI1S4-NONCOPRIME]` |
| 7 | Theorem C transport at `(4,3)`: concrete `A_3` curve; ZvK; disjoint-transposition surjection; strictly larger `π_1` | HOLDS for the `A_3` member `γ(t)=(t^4+t^2-2t,t^3-t)` and for tautological representation transport. UNTESTABLE-AT-DESK for numbered connecting braids, a direct `φ` check, and a strictly larger `π_1` family |

No target is BROKEN. No `charge_basis` line: no new exit-price assertion.

No literature was fetched. Decision's Nori citations were not re-read; they are not inputs to these seven computations.

Independent of the gate arm.

<!-- BODY-END -->
