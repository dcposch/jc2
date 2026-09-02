# 964-NODALITY-REVIEW — hostile gate of Sol's six-node claim

**Lane.** `964-NODALITY-REVIEW`. Date 2026-09-02. Reviewer grok-4.6.
**Charged producer.** Sol §6 of `ideation-20260902T0022Z-sol56.md` (EXACT-DESK /
UNREVIEWED). Parametrization and `Δ_aff=6` from charged
`hf-twin-964-grok46-20260831.md` §3.2 (lines 109–148).
**Method.** Independent exact replay in `sympy` over `QQ`. No `sat()`, no
msolve, no SIROCCO binary, no ledger edit, no `jc2-lean`. Default to
refutation; every displayed identity was recomputed.

**Headline.** All four charged items are **CONFIRMED**. The banked HF-twin
parametrization is an ordinary six-nodal polynomial curve of type `(9,6,4)`.
This is a curve realization, not a representation and not
`FULL_ACTUAL_EXIT` of the census row. No exit price is asserted;
`charge_basis` is inapplicable.

## Verdict table

| # | Item | Verdict |
|---|---|---|
| (1) | Divided-difference system in `(u,v)`; every displayed identity and eliminant factor | **CONFIRMED** |
| (2) | Distinctness of the six nodes and transversality | **CONFIRMED** |
| (3) | `delta_aff=6` exhaustion (immersivity + exact affine delta) | **CONFIRMED** |
| (4) | Predicted SIROCCO census (degree-8 squarefree tangency resultant; no tangency at `x=0` or the new node values; ledger 20) | **CONFIRMED** |
| — | Explicit `(9,6,4)` curve is six-nodal / `REALIZED` | **CONFIRMED** |

---

## 0. Custody

Frozen charged inputs, hashed on this host with `shasum -a 256` **before any
reading**. Both match the charge exactly:

```text
4b0e4dde91a8bbe06dfde68e0c8c4559d92bcb8355a0b57acf32ba8b36a7d3b4  [frozen]/ideation-20260902T0022Z-sol56.md
7cef355be1af63e71bc24361955ad19755598c3925fa1cb2612e62e186f4a35b  [frozen]/hf-twin-964-grok46-20260831.md
```

Line citations `SOL:L` and `HF:L` refer to these frozen copies. Campaign
FALLACY-v2 is in force. No sibling ideation from this round was read.

**Ring map (FALLACY variable/ring).** Coefficient field `QQ`. Parameter ring
`QQ[t]`. Pair ring `QQ[s,t]`. Unordered-pair ring `QQ[u,v]` with the
elementary-symmetric map `u=s+t`, `v=st`. Divided differences are converted
by the recurrence `Δ(t^0)=0`, `Δ(t^1)=1`, `Δ(t^n)=u Δ(t^{n-1}) - v Δ(t^{n-2})`
for `n≥2`. Image check: substituting `(u,v)=(s+t,st)` recovers
`(x(s)-x(t))/(s-t)` and `(y(s)-y(t))/(s-t)` identically. Matching names are
not used as a map proof. No `sat()`. Remainders are taken in the declared
univariate quotient (leaders `u^2+35/8`, `v+11/8`, `d^2-(u^2-4v)`), including
the zero remainder.

---

## 1. Item (1) — divided-difference system

**Verdict: CONFIRMED.**

Charged parametrization `HF:120-122`:

```text
x(t) = t^9 + 3 t^7 + (21/4) t^5 + (35/8) t^3 + (63/32) t
y(t) = t^6 + 2 t^4 + (5/2) t^2 + 3/4
```

Replay of the HF identities consumed by Sol, all exact:

- `x` odd, `y` even.
- `y^3-x^2 = (27/1024)(8 t^4 + 13 t^2 + 16)`, degree 4, leading `27/128`.
- `y' = t(6 t^4 + 8 t^2 + 5)`, `disc(6z^2+8z+5)=-56`.
- `x' = 9 t^8 + 21 t^6 + (105/4) t^4 + (105/8) t^2 + 63/32`, `x'(0)=63/32`.
- `x'` reduced along `6z^2+8z+5` is `(-27/8)z-117/32`, vanishing only at
  `z=-13/12`, where the quadratic equals `27/8≠0`.
- `gcd(x',y')=1` in `QQ[t]`.
- Even factor of `x/t` is `q(z)/32` with
  `q=32z^4+96z^3+168z^2+140z+63`; `gcd(q,q')=1`; `res(q,6z^2+8z+5)=15120≠0`.

(The Euclidean last remainder on the displayed `q` is `225/8`, not HF's
`15/4`. Squarefreeness is unaffected. See §7.)

Let `A=(x(s)-x(t))/(s-t)`, `B=(y(s)-y(t))/(s-t)` in `QQ[u,v]`. Direct
expansion via `Δ` gives Sol's `B` identity identically (`SOL:146`):

```text
B = u (2u^4 - 8 u^2 v + 4 u^2 + 6 v^2 - 8 v + 5)/2.
```

`A` is the unique degree-8 polynomial

```text
A = u^8 - 7 u^6 v + 3 u^6 + 15 u^4 v^2 - 15 u^4 v + (21/4) u^4
    - 10 u^2 v^3 + 18 u^2 v^2 - (63/4) u^2 v + (35/8) u^2
    + v^4 - 3 v^3 + (21/4) v^2 - (35/8) v + 63/32.
```

Primitive integer generators of `(A,B)` (contents 1 after clearing
denominators 32 and 2): `B_pr = u(2u^4-8u^2 v+4u^2+6v^2-8v+5)` and
`A_pr = 32 A`, which at `u=0` is exactly `q(-v)`.

Groebner basis of `I=(A,B)` in `QQ[u,v]`, grevlex `(u,v)`:

```text
v^4 - 3 v^3 + (3427/512) u^2 + (21/4) v^2 - (35/8) v + 63/32,
u (u^2 + 35/8),
u (v + 11/8).
```

Zero-dimensional. Leading monomials `v^4`, `u^3`, `uv`. Standard monomials
`{1,u,u^2,v,v^2,v^3}`, quotient length 6.

The two displayed memberships `SOL:147` lie in the ideal, not merely on the
variety: grevlex reduction of `u(8v+11)` and of `u(8u^2+35)` has remainder
0. Equivalently the GB already contains those generators up to units in `QQ`.

Eliminants, factored over `QQ`:

```text
Res_u(A,B) = 729 (8v+11)^2 (32 v^4 - 96 v^3 + 168 v^2 - 140 v + 63) / 2^25
Res_v(A,B) = 27 u^4 (8 u^2 + 35) / 2^{10}
```

The degree-4 factor is `q(-v)`, the banked `u=0` quartic. The only other
irreducible of the `v`-eliminant is the linear factor `8v+11` (square because
the two new pairs share `v`). Sol's sentence “the `v`-eliminant has only this
linear factor besides the `u=0` quartic” is therefore exact as to support;
the multiplicity 2 is the two `u`-values at that `v`. The `u`-eliminant is
`u^4` (four nodes at `u=0`) times the quadratic `8u^2+35`.

On `u=0`, `B≡0` (because `y` is even) and `32 A = q(-v)`. On `u≠0` the GB
forces `v=-11/8` and `u^2=-35/8`. Direct remainder of `A` and of `B` along
`(u^2+35/8,\ v+11/8)` is 0, so substitution hits `V(A,B)` as claimed.

Positive controls: both components satisfy `A=B=0`. Negative controls:
`A(1,1)=-9/32`, `B(1,1)=1/2`; `A(0,-11/8)=119945/4096≠0` (the components
are disjoint: `gcd(8v+11, q(-v))=1` and `q(11/8)=119945/128≠0`);
`A(1,-11/8)=750393/4096≠0`. Diagonal `v=u^2/4`: `A,B` pull back to `x'(u/2)`,
`y'(u/2)` with ratio 1, and `gcd(A|_{diag}, B|_{diag})=1` in `QQ[u]`, so the
diagonal is not in `V(I)`.

---

## 2. Item (2) — six distinct ordinary nodes

**Verdict: CONFIRMED.**

**Banked four, `u=0`.** Unordered pairs `{t,-t}` with `t^2=z` a root of `q`.
`gcd(q,q')=1` gives four distinct `z`; `q(0)=63≠0` so `t≠0` and
`(s-t)^2=4z≠0`. Images `(0, p(z))` with `p(z)=z^3+2z^2+(5/2)z+3/4`. The
eliminant `Res_z(q, p-w) = 32768 w^4 + 12288 w^3 + 6912 w^2 - 1728 w + 567`
is squarefree of degree 4 (`gcd` with its derivative is 1), so four distinct
`y`-values. HF's two cubics are recovered exactly as the remainder
coefficients of `q` modulo `z^2-σz+π` after imposing
`Q=σ^2-π+2σ+5/2=0`:

```text
c0|Q = -(32 σ^3 + 152 σ^2 + 256 σ + 157),
cz|Q = -4 (8 σ^3 + 32 σ^2 + 46 σ + 25),
gcd = 1,  resultant = -373248 ≠ 0.
```

No two roots of `q` share a `p`-value. Velocities at `{t,-t}` are
`(x',y')` and `(x',-y')`. At `q(z)=0` one has `x'=z q'(z)/16` with `z≠0`
and `q'≠0`, and `res(q, 6z^2+8z+5)≠0` so `y'≠0`; the tangent determinant
is `-2 x' y' ≠ 0`. Independently, the converted Wronskian `W/(s-t)` at
`u=0` is coprime to `A(u=0)` (`res=2126649735/524288≠0`).

**Two further pairs, `u≠0`.** `u^2=-35/8` gives two distinct `u` (since
`u≠-u`); common `v=-11/8`. Pair discriminant `(s-t)^2=u^2-4v=9/8≠0`.
Images, by reducing `x(s)=a_x s + b_x` and `y(s)=a_y s + b_y` along the
quadratic `T^2-u T+v` and then along the locus: `a_x=a_y=0` and

```text
y = 21/512,     x = -297 u / 4096.
```

Both displayed formulae hold as remainders. The two points therefore have
opposite nonzero `x` and the same `y`. They are distinct from the `x=0`
nodes because `u≠0`. They are distinct from each other because `x` is odd
in `u`. They do not share a `y`-value with any banked node:
`Res_z(q,p-w)` at `w=21/512` equals `1066807665/2097152≠0`.

**Transversality of the new pair.** Convert
`W=(x'(s)y'(t)-x'(t)y'(s))` to `QQ[u,v]` by `s,t=(u±d)/2` and remainder
along `d^2=u^2-4v`. On the new locus the remainder is the constant
`315/8≠0`. Both new germs are ordinary nodes (two immersed branches, distinct
tangents), not an `A_3`.

**No triple fibre / no reused parameter.** The parameter polynomial
`F(T)=∏(T^2-u T+v)` over the six pairs is

```text
F = q(T^2)/32 · (T^4 + (13/8) T^2 + 121/64),
```

degree 12, `gcd(F,F')=1`, `F(0)≠0`. Twelve distinct parameters; `t=0` is
not a node parameter.

Six geometric points in the `(u,v)`-plane, scheme length 6, hence `I` is
radical. Six distinct points in the affine plane, each an ordinary node.

---

## 3. Item (3) — `delta_aff=6` exhaustion

**Verdict: CONFIRMED.**

Immersivity is `gcd(x',y')=1`, replayed in §1; no affine cusp.

Properness: `[C(t):C(x,y)]` divides `gcd(9,6)=3`. A cubic reparametrization
would place `x,y` in `C[t^3]`, but `y` has `t^4` coefficient `2≠0`. The
map `A^1→C` is birational onto its image, normalisation `A^1`, `g_{\rm geom}=0`.
The z-eliminant `Res_z(Y-p(z),\ X^2-z h(z)^2)` (with `h=x/t` in `z`) is a
degree-9 polynomial `F(X,Y)` vanishing on the image (`F(x(t),y(t))=0`)
and of `y`-degree 9, hence the implicit equation of an irreducible degree-9
curve. Sequence `(r_0,r_1,r_2)=(9,6,4)` as charged.

Affine delta from the value semigroup, replayed from `HF:133,65-70`:
`Γ=⟨4,6,9⟩`, Frobenius `F=2·6+2·4-9=11`, conductor 12, six gaps
`{1,2,3,5,7,11}`, genus 6. For a proper polynomial (one-place, rational)
curve this genus is `Δ_aff`. Independently, `p_a=28` and the unibranch
infinity semigroup `⟨3,23⟩` has `δ_∞=(3-1)(23-1)/2=22`, so
`28=0+Δ_aff+22` forces `Δ_aff=6`. Both routes agree. This consumes the
charged HF split; it is an identity, not a floor.

Six ordinary nodes contribute local delta `1+1+1+1+1+1=6`. The double-point
scheme is reduced of length 6, immersive, with no triple fibre, so there is
no further affine germ. Remaining-delta 2 in `HF:148-154` is therefore split
as two nodes, not one `A_3`. Completeness is the delta budget plus the
exact fibre analysis, matching the HF completeness licence (`HF:43`), not a
derivative-only argument.

This is a representative of the census row, not `FULL_ACTUAL_EXIT`. Other
AG-S moduli are not claimed six-nodal. The explicit curve meets the campaign
`I_DP` realization test (immersive, 0-dimensional of degree `Δ_aff`, radical,
`W` nonvanishing, parameter polynomial squarefree). Type `(9,6,4)` is
**REALIZED** by this witness.

---

## 4. Item (4) — predicted SIROCCO census

**Verdict: CONFIRMED.**

Tangency resultant `R(c)=Res_t(x(t)-c,\ x'(t))` is the even octic

```text
R(c) = 387420489 c^8 + 37642182543 c^6/128
     + 2310817602051 c^4/32768
     + 11816941917501 c^2/2097152
     + 319057431772527 / 2147483648
     = 19683 · Ω(c) / 2^{31},
```

with primitive octic

```text
Ω = 42268920643584 c^8 + 32085100199936 c^6 + 7694037614592 c^4
    + 614771555328 c^2 + 16209796869.
```

Degree 8, `gcd(R,R')=1`, so eight distinct critical values. Also
`gcd(x',x'')=1`, so each is simple ramification of `t↦x`; with
`gcd(x',y')=1` each is a simple vertical tangent of a smooth branch.
`R(0)=319057431772527/2^{31}≠0`: no tangency at `x=0`. At the new node
abscissae, `x^2=-297^2·35/(4096^2·8)=-3087315/134217728`, and
`Res_c(R,\ c^2-x_{\rm new}^2)≠0`. Equivalently `gcd(Ω,\ 134217728 c^2+3087315)=1`.

Fibre over `x=0`: `x(t)=t·q(t^2)/32`, so `t=0` together with the eight
parameters of the four banked nodes. Point `t=0` is `(0,3/4)` with
`x'(0)≠0`, a residual smooth point. This is one four-node fibre, not a
tangency. The two new nodes have distinct nonzero `x` (opposite, purely
imaginary over `R`, distinct over `C`) and are two one-node fibres.

Global check, not an analogy: the polar discriminant
`Δ(X)=Res_Y(F, F_Y)` of the implicit equation factors over `QQ` as

```text
Δ(X) ∼ X^8 · (134217728 X^2 + 3087315)^2 · Ω(X)
```

up to a nonzero rational. Degrees `8+4+8=20`. Support:

- `X^8`: four-node fibre at `x=0`, multiplicity `2·4=8`;
- `(X^2 - x_{\rm new}^2)^2`: two one-node fibres, multiplicity 2 each;
- `Ω(X)`: eight simple tangencies, multiplicity 1 each.

No other affine factor. `gcd(Δ,Δ')=X^7(X^2+3087315/134217728)` is exactly
the non-squarefree part predicted by those multiplicities; the tangency
octic is squarefree and coprime to the node factors. Ledger
`8+2(4+1+1)=20`, which also equals `2 Δ_aff + deg_t x - 1 = 12+9-1`.
Sol's predicted census (`SOL:178-180`) is the factorization of `Δ`.

---

## 5. Gate

Sol §6 is promoted from `EXACT-DESK/UNREVIEWED` to **CONFIRMED** on this
explicit curve. `(9,6,4)` is `REALIZED` by the HF-twin parametrization as an
ordinary six-nodal polynomial curve. The running Box03 locus job is
superseded as an existence search: a witness is in hand. It is not a proof
that every AG-S member of the row is six-nodal, and it is not a braid
factorisation. The successor is the predicted native BM job on this curve
(eight simple tangencies, one four-node fibre, two one-node fibres, exponent
20), with output `SURVIVOR` / `NATIVE_ZERO_CURVE_ONLY` / `OPEN` as Sol
stated — never a row-level kill.

No `GAP-CANDIDATE[964-NODAL-*]` is opened on the four charged items.

---

## 6. FALLACY-v2

- Flag / place / series not identified: AG-S sequence, affine nodes, and
  `K_∞=C_{(3,4)}(T(2,3))` remain distinct objects; infinity semigroup
  `⟨3,23⟩` is used only as the charged `δ_∞` input to the genus split.
- Carrier: this curve is a `REPRESENTATIVE`, not `FULL_ACTUAL_EXIT` of the
  census row. Realization is a witness, not row-attainment.
- Floor / attainment: six ordinary nodes are a covering witness for
  `Δ_aff=6`, matched to the exact semigroup genus and to `p_a=δ_∞+Δ_aff`.
  Equality is not inferred from a lower bound alone.
- `sat()` wrapping: not used. Ideal `(A,B)` in `QQ[u,v]`, Groebner, length
  and radicality from leading monomials plus six geometric points.
- Raw remainder: leaders `u^2+35/8`, `v+11/8`, `d^2-(u^2-4v)` declared;
  zero remainders recorded as zero.
- Variable / ring map: §0. Image checks `A_st=A(s+t,st)` and
  `B_st=B(s+t,st)` identically.
- Prime marks `x',y'` are derivatives in `QQ[t]`.
- No pole identity, no M-descent, no target/arrival index, no per-ray
  charge. No new exit-price assertion.

---

## 7. Charged-source slip, not load-bearing

`HF:144` writes “final remainder `15/4≠0`” for `gcd(q,q')`. The Euclidean
last nonzero remainder on the displayed `q` is `225/8`; on the monic even
factor of `x/t` it is `225/256`. Neither is `15/4`. The gcd is still 1, and
Sol does not quote the `15/4`. No Sol identity is affected.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14280`.
- Body SHA-256:
  `290c7d43d899090300816394507887b18bf0e35d673b8745dbd8f81ef2c9252a`.
- Frozen basis: `f35adc89bec33c1e1a2df50ac3d8bcd99f762218`.
