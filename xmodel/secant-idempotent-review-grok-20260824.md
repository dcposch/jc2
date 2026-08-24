# Hostile different-model review — `SECANT-IDEMPOTENT`

| Field | Value |
|---|---|
| Claim under review | Frozen fresh-connection gate: for a polynomial map with constant invertible Jacobian, the determinant of any polynomial secant matrix is the unique diagonal idempotent in the self-fiber product, and `I:(x-u,y-v)^infinity = I+(det A)` exactly |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none (algebra holds). Smallest overclaim: calling the exact saturation identity campaign-new. It is already the planar secant/colon theorem in the public collision-ideals neighbor; McKean's Bézoutian is the same telescoping matrix |
| Evidence tier | independent polynomial identities over `Q` and `F_p`; two-engine replay of the frozen scripts; independent Singular `sat`/`quotient` (not producer verdict strings); primary-source comparison to McKean arXiv:2005.09797 and the collision-ideals README |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, fresh-connection lane) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T09:20:00Z – 2026-08-24T09:50:00Z |
| Python | host 3.14.6; attack interpreter 3.11.11 with `sympy==1.14.0` |
| Singular | 4.4.1 (`elim.lib` `sat` / `quotient`) |
| Host | Darwin arm64 |

Producer inputs reread in full before any verdict:

- `xmodel/fresh-connection-gate-20260824.md` (SHA-256 `666bde51ea8bb78bd2c031122183148708b2b7de08547dc407191e633a712c4b`, matches the launch prompt)
- `cases/fresh_connection_20260824/secant_idempotent.py` (SHA-256 `c55f9f1173aef8a16ecc13c2162ee2fd89bb6916cfaa95f4e9d57b7030105eef`)
- `cases/fresh_connection_20260824/independent_replay.sing` (SHA-256 `bd5469b4a28f4a84c8f6635f6c95b3dcc6295d94a195d6ad2e36f903edefc891`)

Cited local notes reread against the committed basis `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`:

- `APPROACHES.md` avenue 32 (off-diagonal collision ideal / Cynk–Rusek, Ax–Grothendieck)
- `AUDIT.md` (no secant/Bezoutian collision entry; saturation there is GGV-corner language, unused)
- `xmodel/websweep-2026-08-16.md` A2 (collision-ideals neighbor, “secant-determinant constructions”)
- `xmodel/grok-approaches.md` §25, `xmodel/ox-approaches.md` A10, `xmodel/sol-lateral.md` §9 (McKean Bézoutian)

No producer, canonical, or case file was edited. No generic collision search was started. The Python script’s hardcoded `"theorem_checks": true` block is not evidence.

**Promotion.** Accept as a correctly proved *software/theory accelerator* for avenue 32: saturation of the collision ideal by the diagonal is exactly adjoining one secant determinant. Do **not** promote a literature-new theorem, a degree/support bound, or a JC2 decision.

**Quarantine.** `I+(det A)=(1)` for every characteristic-zero Keller map is the injectivity endpoint (Cynk–Rusek / Bass–Connell–Wright). The Artin–Schreier `F_3` survivor is the known collision, not a characteristic-zero counterexample. The identity is standard unramified-diagonal + secant/Bézoutian algebra; the public neighbor already writes it as `I_R:I_Delta = I_R+(delta_F)`.

---

## Headline and subclaim table

Let `k` be a field, `F=(P,Q)` a polynomial endomorphism of `A^2_k`, and

```text
S = k[x,y,u,v],
f1 = P(x,y)-P(u,v),     f2 = Q(x,y)-Q(u,v),
I = (f1,f2),            C = S/I,
delta = (x-u, y-v)^T,   J_delta = (x-u, y-v) C.
```

A *polynomial secant matrix* is any `A in M_2(S)` with `A delta = (f1,f2)^T`. Write `e = c^{-1} det A` when `det J_F = c in k^x`.

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | For every such `A`, the adjugate identities `e(x-u)=a22 f1 - a12 f2` and `e(y-v)=-a21 f1 + a11 f2` hold in `S`, hence `e J_delta=0` in `C` | **CONFIRMED** | a polynomial `A` with `A delta = (f1,f2)^T` for which `adj(A)A != (det A) I_2` |
| 2 | Every such `A`, not merely the `x`-then-`y` telescoper, restricts to `J_F` on the diagonal. For constant `c != 0`, `e=c^{-1} det A` satisfies `e J_delta=0`, `1-e in J_delta`, and `e^2=e` in `C` | **CONFIRMED** | a polynomial secant with `A\|_(x=u,y=v) != J_F`; cofactors for `e(e-1)` failing when `c=2` |
| 3 | Uniqueness holds exactly among elements of `C` with `e J_delta=0` and `1-e in J_delta`. It is not uniqueness among all idempotents of `C` | **CONFIRMED** (exact scope). Reject the stronger reading | a second element of `C` annihilating `J_delta` and congruent to `1` modulo `J_delta`; the producer claiming uniqueness among all idempotents |
| 4 | Scheme-theoretically `I : (x-u,y-v)^infinity = I+(det A)`. Both containments, ideal (not element) saturation, `eC` the diagonal quotient, product decomposition. Strengthening: the first colon already equals the saturation | **CONFIRMED** | `sat(I,J)` properly containing or missing `I+(det A)`; `I+(1-e) != (x-u,y-v)`; only radical equality |
| 5 | Two polynomial secant matrices give the same class of `e` in `C`, hence the same three-generator ideal `I+(det A)` | **CONFIRMED** | `det A_xy - det A_yx` or `det A - det A_pert` nonzero in `C` on a Keller control |
| 6 | Characteristic-zero automorphism controls have off ideal `(1)`; the `F_3` Artin–Schreier marked pair is an honest off-diagonal collision with proper off ideal; `(x^2,y)` is rejected by non-idempotence. Producer verdict strings unused | **CONFIRMED** | tame off Gröbner not `[1]`; marked `(0,0),(1,0)` missing `V(f1,f2,det A)`; square remainder `d^2-d` in `I` |
| 7 | The theorem removes saturation computationally. `I+(det A)=(1)` for every char-0 Keller map is injectivity, hence JC2. No degree/support bound. Identity is standard secant/Bézoutian + unramified-diagonal algebra; no literature novelty | **CONFIRMED** (scope). Priority caveat below | a finite bound on `det A`; a JC2 implication; a primary source the producer claimed and did not have |

All remarks below are non-blocking unless marked otherwise. None changes an identity, a Gröbner basis, or a numbered verdict.

---

## Replay and hashes

Frozen artifact SHA-256 values match the launch prompt:

| Artifact | SHA-256 |
|---|---|
| `xmodel/fresh-connection-gate-20260824.md` | `666bde51ea8bb78bd2c031122183148708b2b7de08547dc407191e633a712c4b` |
| `cases/fresh_connection_20260824/secant_idempotent.py` | `c55f9f1173aef8a16ecc13c2162ee2fd89bb6916cfaa95f4e9d57b7030105eef` |
| `cases/fresh_connection_20260824/independent_replay.sing` | `bd5469b4a28f4a84c8f6635f6c95b3dcc6295d94a195d6ad2e36f903edefc891` |

Independent rerun of the frozen engines, locale warnings excluded from the hash:

```text
uv run --no-project --with sympy==1.14.0 \
  python3 cases/fresh_connection_20260824/secant_idempotent.py
```

Stdout SHA-256 `1e0d473785ebe403db50248642c26e29831328fb8865fe2a2e91ce862326d4a3`, identical to the producer report. The script’s own 44 Boolean checks all returned true. Those checks were then discarded as evidence; every numbered claim below is re-derived or re-reduced independently.

```text
Singular -q cases/fresh_connection_20260824/independent_replay.sing
```

Stdout SHA-256 `06678206d168206341293bca00788c22dfa1cff729327d851b16d261ba4572c6`, identical to the producer report. Four `PASS` lines, exit 0.

A second, reviewer-owned Singular script (`elim.lib` `sat` and `quotient`, perturbed secant, `c=2`, Artin–Schreier `p=3` and `p=5`) returned `ALL_SINGULAR_ATTACKS_PASSED`. A reviewer-owned sympy attack confirmed adjugate identities, diagonal restriction, convention independence, and the `c=2` cofactors on identity, triangular, tame, `(2x+y^2,y)`, Artin–Schreier `p=3` and `p=5`, plus the square rejection. (An initial sympy “saturation” helper that coloned by `(x-u)` then `(y-v)` separately was rejected: that is saturation by the *product* hypersurface, which kills the off-diagonal `V(y-v)` and spuriously returns `(1)`. It is not used.)

Producer Python `theorem_checks` are string constants, not reductions. They are ignored.

---

## 1. Adjugate identities, arbitrary polynomial secant

`adj(A) A = (det A) I_2` is an identity of `2 x 2` matrices over any commutative ring. Substituting `A delta = (f1,f2)^T` gives, in `S`,

```text
e (x-u) = a22 f1 - a12 f2,
e (y-v) = -a21 f1 + a11 f2.
```

These are polynomial identities, stronger than membership in `I`. In `C` they read `e J_delta = 0`. No Keller hypothesis is used. The same identities were checked as exact zero polynomials on the telescoping matrix, the `y`-then-`x` telescoper, and the perturbation

```text
A' = A + [[ alpha (y-v), -alpha (x-u) ],
          [ beta  (y-v), -beta  (x-u) ]]
```

for polynomial `alpha, beta` (the general kernel of `(-) delta`), on every registered map including the non-Keller square.

---

## 2. Diagonal restriction and the constant-Jacobian idempotent

Write `B(s,t) = A(u+s, v+t; u, v)`. Then `F(u+s,v+t)-F(u,v) = B(s,t) (s,t)^T`. The right-hand side is `B(0,0)(s,t)^T` plus terms of degree `>= 2` in `(s,t)`, with no characteristic restriction (finite Taylor grouping, no division). The left-hand Jacobian at the origin is `J_F(u,v)`. Hence `A` restricted to the diagonal is `J_F`.

Alternatively: the difference of two polynomial secants annihilates `delta`, so each of its rows is a polynomial multiple of `(y-v, -(x-u))` and vanishes on `x=u, y=v`. The diagonal value is therefore *unique* among polynomial secants, and equals the telescoper’s value, which is `J_F` by the usual exact quotient `(P(x,y)-P(u,y))/(x-u) |_{x=u} = P_x`. Independent Singular check: a perturbed tame secant still satisfies `A'|_(diag) = J_F` and `det A'|_(diag) = 1`.

If `det J_F = c in k^x`, then `e := c^{-1} det A` satisfies `e(u,v;u,v) = 1`. Polynomial divided differences therefore give `e-1 = c_x (x-u)+c_y (y-v)` in `S`, i.e. `1-e in J_delta` in `C`. Multiply by `e` and apply §1:

```text
e(e-1) = c_x e (x-u) + c_y e (y-v)
       = c^{-1} ( (c_x a22 - c_y a21) f1 + (-c_x a12 + c_y a11) f2 ).
```

So `e^2=e` in `C`. This was reduced independently for `c=1` (all Keller controls, all three secant conventions) and for `c=2` on `F=(2x+y^2,y)`, where `det A=2`, `e=1`, `e^2-e` reduces to `0` modulo `I`, and `I+(1-e)=(x-u,y-v)`.

The producer Python only exercises the `x`-then-`y` telescoper with `c=1`. The gap is in the replay coverage, not in the algebra. The independent attack covers the missing cases.

---

## 3. Uniqueness, exact scope

If `e, e' in C` both satisfy `e J_delta = 0 = e' J_delta` and `1-e, 1-e' in J_delta`, then

```text
e = e · 1 = e(e' + (1-e')) = e e',
e' = e' e = e e',
```

so `e=e'`. The two properties already imply idempotence, so this is uniqueness among *all elements* of `C` with those two properties, not merely among idempotents.

It is **not** uniqueness among all idempotents of `C`. The Pierce decomposition `C ≅ eC × (1-e)C` produces at least `{0, e, 1-e, 1}`. On the Artin–Schreier control `F=(x-x^3,y)` over `F_3`, Singular reduces both `d^2-d` and `(1-d)^2-(1-d)` to `0` modulo `I`, while `(1-d)(x-u)` does **not** reduce to `0`. So `1-e` is a genuine extra idempotent and is not the diagonal projector. If the off-diagonal factor is disconnected there can be still more.

The producer body (§2.2) states uniqueness under exactly the two properties. The headline “the unique idempotent cutting out the diagonal component” is acceptable with that meaning (the clopen projector of the connected diagonal factor `eC ≅ k[x,y]`). Any reading “the unique idempotent of `C`” is false and is rejected.

---

## 4. Exact saturation identity

Write `J=(x-u,y-v)` and `e = c^{-1} det A`. Since `c` is a unit, `(e)=(det A)` in `S`.

### Both containments, as ideals

**`I+(e) ⊆ I:J ⊆ I:J^infinity`.** From §1, `e(x-u)` and `e(y-v)` lie in `I`, so `e in I:J`.

**`I:J^infinity ⊆ I+(e)`.** Let `h J^m ⊆ I`. In `C`, `h J_delta^m = 0`. From §2, `1-e in J_delta`, so `(1-e)^m in J_delta^m` and `h(1-e)^m=0`. Idempotence gives `(1-e)^2=1-e`, hence `(1-e)^m=1-e` for all `m>=1`. Thus `h(1-e)=0` in `C`, i.e. `h=he in (e)`. Therefore `h in I+(e)`.

This is colon of *ideals*, not saturation by a single element, and not radical membership. The identity is

```text
I : (x-u,y-v)^infinity = I + (det A)     in S,
0 : J_delta^infinity = (e)               in C.
```

**Strengthening, also confirmed.** The first inclusion already puts `I+(e)` inside the *first* colon `I:J`. Combined with the converse, `I:J = I:J^infinity = I+(e)`. The colon stabilizes at `m=1` because the complementary ideal is generated by an idempotent. Independent Singular `quotient(I,J)` and `sat(I,J)` return identical Gröbner bases on Artin–Schreier `p=3` and `p=5`, both equal to `std(I+(det A))`; a second colon `quotient(I:J, J)` does not grow.

### Nilpotents / embedded diagonal / product / `eC`

In `C`, `1-e in J_delta` and `e J_delta=0` imply `J_delta ⊆ (0:e)=(1-e)` (idempotent) and therefore `J_delta=(1-e)` as ideals. Consequently:

```text
C / J_delta ≅ C / (1-e) ≅ eC.
```

On the other side, `f1,f2 in J` identically (because `A delta = (f1,f2)^T`), so `I ⊆ J` and `I+J=J`. Thus `S/(I+(1-e)) = S/J ≅ k[x,y]`. Independent Singular equality of `std(I+(1-e))` with `std(x-u,y-v)` on tame, `c=2`, and Artin–Schreier `p=3` confirms `eC` is the diagonal quotient, reduced.

There is therefore **no embedded diagonal structure left in `C`** for constant-Jacobian maps: the diagonal factor is `k[x,y]`. The producer sentence that saturation “removes embedded diagonal structure as well as diagonal points” describes what saturation *does in general*. Under the Keller hypothesis the diagonal is already a reduced clopen component (unramified + separated ⇒ the diagonal of `X → Y` is an open-and-closed immersion). The identity still equals saturation as schemes, not merely as sets: Gröbner bases of `sat(I,J)` and `I+(det A)` coincide, including on the nonempty off-diagonal Artin–Schreier components.

The Pierce decomposition `C ≅ eC × (1-e)C` is the Chinese remainder theorem for complementary idempotents, with

```text
eC ≅ k[x,y]                 (diagonal),
(1-e)C ≅ C/(e) ≅ S/(I+(e))  (off-diagonal closed-open piece).
```

### Independent nonempty test of the equality

Characteristic-zero automorphisms make both sides `(1)`, which is too weak to distinguish the identity from “both unit”. The honest test is a Keller map with a genuine collision. Over `F_3`, `F=(x-x^3,y)` has `det J_F=1` and

```text
det A = 1 - x^2 - x u - u^2,
I + (det A) = (y-v, x^2 + x u + u^2 - 1).
```

Singular `sat(I,(x-u,y-v))` and `quotient(I,(x-u,y-v))` return that same basis. The marked pair `(x,y)=(0,0)`, `(u,v)=(1,0)` satisfies `F(0,0)=F(1,0)=(0,0)` and `det A=0`. The same equality holds for `F=(x-x^5,y)` over `F_5`, with off basis `(y-v, x^4+x^3 u+x^2 u^2+x u^3+u^4-1)`.

Observation, not claimed: for the non-Keller square `F=(x^2,y)` one still has `sat(I,J)=I+(x+u)=(y-v,x+u)`, while `d^2-d` is *not* in `I`. Idempotence uses constant Jacobian; the colon identity can hold more broadly and is not the producer’s theorem.

---

## 5. Convention independence

§2 and §3 give uniqueness of the class of `e` in `C`. Hence any two polynomial secants `A, A'` satisfy `det A ≡ det A' (mod I)` after the same constant scaling, and `I+(det A)=I+(det A')` as ideals.

Independently reduced:

- `x`-then-`y` versus `y`-then-`x` telescopers: difference of determinants is `0` in `C` on identity, triangular, tame, `c=2`, Artin–Schreier `p=3` and `p=5`. On the tame automorphism the two determinants are *unequal as polynomials* (`dxy_minus_dyx_is_zero_poly = false`) but congruent modulo `I`.
- Telescoper versus a rank-one kernel perturbation: same, on all those maps. The perturbed matrix remains a polynomial secant and still restricts to `J_F`.

This is the covariance safety the producer contrasts with the raw-boundary failure. It is uniqueness in `C`, not uniqueness of the polynomial `det A` in `S`.

---

## 6. Controls, independently recomputed

Producer verdict strings were not used. Each Jacobian, secant determinant, remainder, and off Gröbner basis was rebuilt.

**Identity** `(x,y)` over `Q`. `J=1`, `det A=1`, `I+(det A)=(1)`.

**Triangular** `(x, y+x^4)` over `Q`. `J=1`, `det A=1` (lower-triangular secant), off ideal `(1)`.

**Tame two-step** `P=x+(y+x^2)^2`, `Q=y+x^2` over `Q`. This is `tau compose sigma` with `sigma=(x,y+x^2)`, `tau=(x+y^2,y)`, hence an automorphism. Independent expansion of the `x`-then-`y` secant:

```text
a11 = 1 + (x+u)(2y + x^2 + u^2),
a12 = y + v + 2 u^2,
a21 = x + u,
a22 = 1,
det A = 1 + x^3 + x^2 u - x u^2 - u^3 + x y - x v + u y - u v
      = -u^3 - u^2 x - u v + u x^2 + u y - v x + x^3 + x y + 1.
```

Nine terms, matching the producer polynomial as an element of `Q[x,y,u,v]`. Off Gröbner basis `[1]` in both sympy grevlex and Singular `dp`. The test is therefore not “`det A` happened to be the constant `1`”.

**Artin–Schreier** `(x-x^3, y)` over `F_3`. `J=1-3x^2=1`. `det A=1-x^2-x u-u^2`. Off basis `(y-v, x^2+x u+u^2-1)`, not unit. Marked pair `(0,0),(1,0)`: `F(0,0)=F(1,0)=(0,0)` and `det A(0,0,1,0)=0`. This is the classical `F_3` collision (the map `x |-> x-x^3` is identically zero on `F_3`). It is not a characteristic-zero counterexample.

**Non-Keller** `(x^2,y)` over `Q`. `J=2x != 1`, `det A=x+u`, diagonal value `2x != 1`. Collision remainder of `d^2-d` is `2u^2+2 u x - u - x != 0`. Idempotence correctly rejected.

---

## 7. Scope, priority, promotion

### What the theorem does and does not do

It replaces the computation of `I : (x-u,y-v)^infinity` by the three-generator ideal `(f1,f2,det A)`. That is exact, scheme-theoretic, and convention-safe.

It does **not** prove `I+(det A)=(1)` for an arbitrary characteristic-zero Keller map. That assertion is injectivity of `F`. Over an algebraically closed field of characteristic zero, injective polynomial endomorphisms of `A^n` are automorphisms (Bass–Connell–Wright Theorem 2.1; the planar case is the classical Cynk–Rusek / Ax–Grothendieck interface already named in avenue 32). So emptiness of the off ideal on every complex Keller map *is* JC2. The producer states this and does not claim otherwise.

No degree, support, height, or Gröbner bound on `det A` follows from the identity. The tame control already has a nonconstant nine-term determinant. Avenue 32 remains “hollow” as a proof route in the sense of `APPROACHES.md` row 32 and `xmodel/grok-approaches.md` §25: the collision ideal is a reformulation of injectivity, not a new obstruction.

No GGV packet, sheet-six class, characteristic-109 lift, or JC2 decision is in scope.

### Priority: the identity is not campaign-new

McKean, *Bézoutians and injectivity of polynomial maps*, arXiv:2005.09797 (J. Pure Appl. Algebra 2023), Definition 1.1, is the sequential divided-difference matrix whose determinant is the multivariate Bézoutian. Proposition 2.3 is `delta(Béz(f)) = Jac(f)`, i.e. restriction to the diagonal is the Jacobian (Scheja–Storch 1975, Becker–Cardinal–Roy–Szafraniec 1996). McKean’s theorem is different and stronger-hypothesised: a *constant* Bézoutian implies injectivity on rational points, and in characteristic zero with `Jac(f) in k^x` a constant Bézoutian implies invertibility. The tame automorphism is a Keller map whose secant determinant is *not* constant, so McKean does not prove JC2 and does not prove the colon identity. The matrix is the same object.

The public neighbor already recorded in `xmodel/websweep-2026-08-16.md` A2 (`what-social-construct/collision-ideals`, README also served from `jacobian-collision-geometry`) states the *same* planar theorem, including the complementary idempotent, the clopen diagonal, and the colon:

```text
delta_F I_Delta ⊆ I_R(F),     delta_F ≡ c  (mod I_Delta),
q_F = 1 - delta_F / c,        Obs(F) = C_F q_F,
I_off = I_R : I_Delta = I_R + (delta_F).
```

Their `q_F` is the producer’s `1-e`. Their first-colon form is the strengthening of §4. They also record that saturation stabilizes at the first colon when the diagonal is clopen. Abstractly this is the standard fact that an unramified separated morphism has clopen diagonal (Stacks / EGA: unramified iff the diagonal is an open immersion; affine morphisms are separated), plus the explicit generator `det A`.

The producer is right to claim **no literature novelty**, and wrong to call the exact saturation identity a “campaign-new point”. The campaign-local content is the explicit cofactor certificates (2.1)–(2.3), the two-engine replay, and the software interface. That is the smallest overclaim. It does not disturb the algebra.

### Promotion advice

**Theorem.** Do not promote `SECANT-IDEMPOTENT` as a new theorem, as an avenue-32 proof promotion, or as a public claim. Internally, record it as an exact, hostile-confirmed packaging of classical secant/Bézoutian algebra that makes the off-diagonal collision ideal three-generated without a saturating Gröbner engine.

**Software interface.** Do promote a small source-independent collision module that emits `f1, f2, det A` and uses the four controls (identity, triangular, tame, Artin–Schreier, plus the square rejection) as mandatory gates. The first worthwhile client is a *named, bounded, polynomial-origin family* for which saturation was the actual bottleneck. This is not a license for generic sparse widening, AWS search, or an implicit `I+(det A)=(1)` chase on unstructured Keller maps.

Absent one of the producer’s three resurrection conditions (checked unit certificate on an honest exhaustive family; a characteristic-zero nonunit off ideal with an explicit collision and `J=1`; or a structural degree/support theorem for `det A`), the gate stays an accelerator.

No statement in the producer report, and no statement in this review, proves or disproves JC2.
