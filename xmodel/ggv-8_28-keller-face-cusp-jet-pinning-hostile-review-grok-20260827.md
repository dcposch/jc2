# Hostile review: bounded GGV `8_28` Keller-face cusp-jet pinning control

**Reviewer:** Grok 4.6 (independent hostile referee). **Date:** 2026-08-27.  
**Target:** the charged freeze of Sol's bounded jet/pinning control

`cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/`  
together with `xmodel/ggv-8_28-keller-face-cusp-jet-pinning-sol-20260827.md`.

**Claim under review (narrow):** one exact square/cube-edge Jacobian recurrence
for `F_0=H^2`, `G_0=H^3` with `H=X^8-1`; `E_1=0` forces `G_1=(3/2)HF_1` and
`E_2=0` forces `H\mid F_1` with a unique polynomial `G_2`; a generic tagged
branch of this square edge is finite for `g` at order `O(t^6)`; two same-support
root-sign packets through `E_22=0` are rejected by polynomial source provenance;
the first rootwise unit carrier is `6H'(c)V_8(c)U_{14}(c)=1`, leaving an explicit
global remainder `(13/12)H`. **Not** under review: a Keller pair, a
counterexample, a global GGV-to-tree functor, source/landing coverage, `G2-PSC`,
`G2-BD`, or JC2.

**Method.** Rehashed the five charged artifacts and the five live source pins.
Rehashed the prior one-chain freeze and confirmed those R0 bytes are unchanged.
Independently derived the coordinate Jacobian, the `(4,-1)` faces and `y`-edge,
the coefficient recurrence, the `E_1`/`E_2` algebra, the fibre ODE, the two
root-sign packets, the source pullback, the local unit carrier, and the global
`E_22` polynomial, using only desk-scale exact arithmetic in `Q[X]` and sparse
`Q[t,X]`. Producer `PASS`, the producer symbolic engine, reported identities,
and the prior non-Keller `8_28` prototype were not used as evidence. No AWS, no
CAS, no producer-file edits, no canonical-ledger edits.

**Firewall.** This control is not a Keller pair and not a counterexample. It
cannot prove a GGV-to-tree functor, global source/landing coverage, `G2-PSC`,
`G2-BD`, or JC2. A square/cube leading face is not a Keller jet. Formal
root-sign packets with Laurent source monomials are not polynomial-source
mutations.

---

## Verdict table

| Item | Verdict |
|---|---|
| Custody | **CONFIRMED** |
| Coordinate / Jacobian sign | **CONFIRMED** |
| Native face | **CONFIRMED** |
| General recurrence | **CONFIRMED** |
| Squarefree uniqueness / divisibility | **CONFIRMED** |
| `G_2` coefficient formula | **CONFIRMED** |
| Cusp normalization / map | **CONFIRMED** |
| Fibre ODE / generic-finite scope | **CONFIRMED** |
| Both formal mutations | **CONFIRMED** |
| Polynomial provenance rejection | **CONFIRMED** |
| Determinant carrier | **CONFIRMED** |
| Global `13H/12` gap | **CONFIRMED** |
| Final scope | **CONFIRMED** |

No item is **REFUTED**. No item is **GAP/REPAIR**. No smallest failing identity,
root, or source exponent was found. The producer verifier does not itself
derive the coordinate Jacobian, the fibre ODE, uniqueness, the residue squares,
or the pullback; those were rederived here and survive.

---

## Independent hashes

Recomputed SHA-256, all matching the charged prompt and the internal
`FREEZE.sha256` lines:

```text
ef9acfa90935b32e244367dada67ab35d6454f431f6d43dc35d144b3d08fe46c
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/verify.py
46e1b3434badcea007a914ec71bf60d9758ee76d312dc00d252342d52beed76d
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/RESULT.json
79a16f282f0a3a3e5409b3e0b6d4a8dc61e2fedaa6babdf673b5645d64c38530
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/README.md
3e4e608d32c44b1b0208bd5472257ba1dbe4cadf4ef5efb2ace49d3d47d756be
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-sol-20260827.md
6928428f9cc46641a80275e2bbfa62e784c4290ff041f5089ae789507fa8804f
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/FREEZE.sha256
```

Live source pins, all matching the freeze table:

```text
MATCH  xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-sol-20260827.md
       7647f2f118d4fe9fdd060b9e3e9450b58a62e287a80e942cad6de752a3f34ae8
MATCH  cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/FREEZE.sha256
       676bdd3ce960221072f037e7160d457a9d1d64c8e7353891f69e9931ae71149b
MATCH  xmodel/sol-connections.md
       3fe165e55704e0a4b5dba3b5968ea995846a81f58b65968fa89521ef8595895c
MATCH  ladder/TRANSPORT.md
       9750aa9d14650a22a410803022d42fa523e3993a21ee9a27714386fa1150047c
MATCH  ladder/REDUCTION.md
       1ff57e1f8a632f33d3558c924dadf26bdd1d389797d48be43515b88718a2e725
```

Prior R0 frozen bytes, still identical to the original freeze:

```text
4dfe7c6dc1e873892f9128ac2712f319a8c85ffb051701ddafa442d779e11f28  prior verify.py
deb3a6308e07137c4113a45d4edafdd7a0be34d954d600b33d85ddb8acba57bd  prior RESULT.json
f5d8e4efd33064dc23dbef3e7b7ad2bd1285631d095922ff6e2894e50863af0a  prior README.md
7647f2f118d4fe9fdd060b9e3e9450b58a62e287a80e942cad6de752a3f34ae8  prior sol report
676bdd3ce960221072f037e7160d457a9d1d64c8e7353891f69e9931ae71149b  prior FREEZE.sha256
```

Repository `HEAD` is still `418e413593120d19e15e6546eb50c985f4b1f038`. The
approximate-root design file is still the blob from commit
`11329d236d53a5b466f4b7076857174d557a3f3d`.

---

## 1. Custody — CONFIRMED

All five charged digests match the prompt. The four lines inside
`FREEZE.sha256` match the four hashed producer files. All five pins match the
live bytes.

The prior one-chain control is immutable as an R0 freeze: its four frozen
files and its freeze list still hash to the values recorded on 2026-08-27.
Additive R1 custody files in that directory do not alter those R0 bytes. This
case does not rewrite that freeze, `RESULT.json`, or the prior sol report.

The history/dedup statement is correct. The pinned
`xmodel/sol-connections.md` proposes enriching a GGV flag by the cusp remainder

```text
h_1 = d^m P^n - c^n Q^m
```

and the paired residual/approximate-root tower (Conjecture 1, the `(2,3)`
form `g^2-const*f^3`, and the concrete `(8,28)` experiment list). It does not
contain the edge recurrence `(3.2)`, the `E_2` divisibility obstruction, the
fibre ODE `(0.1)`, or an executable `(U,V,W)` map. The new control is additive
to that design note, not a silent restatement of it, and not a reuse of the
prior non-Keller prototype as a Keller witness.

`ladder/TRANSPORT.md` is still the already-reviewed dirty working-tree rewrite
(45 lines: 28 insertions, 17 deletions). This freeze pins the live digest
`9750aa9d…`, not the stale `HEAD` blob. That is the correct pin for the bytes
actually consumed.

A freeze-internal replay of `verify.py` reproduces the frozen `RESULT.json`.
That is custody consistency only. It is not evidence for any identity below.

---

## 2. Coordinate / Jacobian sign — CONFIRMED

Start with

```text
x = t^3 X,    y = t^{-1},    f = t^{-8} F,    g = t^{-12} G.
```

The coordinate Jacobian is

```text
∂(x,y)/∂(X,t) = | t^3    3 t^2 X |
                | 0     -t^{-2}  |,
```

with determinant `-t`. The chain rule for Jacobian determinants is

```text
[f,g]_{X,t} = [f,g]_{x,y} · det ∂(x,y)/∂(X,t),
```

where `[f,g]_{x,y} = f_x g_y - f_y g_x` and `[f,g]_{X,t} = f_X g_t - f_t g_X`.
Hence

```text
[f,g]_{x,y} = - t^{-1} [f,g]_{X,t}.
```

Substitute `f=t^{-8}F` and `g=t^{-12}G`:

```text
f_X = t^{-8} F_X,
f_t = -8 t^{-9} F + t^{-8} F_t,
g_X = t^{-12} G_X,
g_t = -12 t^{-13} G + t^{-12} G_t.
```

Then

```text
[f,g]_{X,t}
  = t^{-21}(-12 F_X G + 8 F G_X) + t^{-20}(F_X G_t - F_t G_X),
```

and

```text
[f,g]_{x,y}
  = t^{-22} ( 12 F_X G - 8 F G_X - t(F_X G_t - F_t G_X) )
  = t^{-22} E.
```

So `[f,g]=1` is exactly `E=t^{22}`. A sign error in the bracket, a swap of
`(f,g)`, a wrong power of `t`, or a wrong coordinate determinant would change
this identity and the downstream ODE. None of those errors is present.

Two independent numerical specializations confirm the sign and the `-t`
bracket term:

- `F=X`, `G=1` gives `f=x y^{11}`, `g=y^{12}`, `[f,g]=12 y^{22}=12 t^{-22}`,
  and `E=12`.
- `F=t`, `G=X` gives `f=y^7`, `g=x y^{15}`, `[f,g]=-7 t^{-21}`, and
  `E=-7t`, hence `t^{-22}E=-7 t^{-21}`.

Component-order note, not a defect: GGV native order on this edge is
`(P,Q)=(g,f)`. The campaign Jacobian used here, and in the prior non-Keller
witness, is `[f,g]`. Replacing it by `[g,f]=1` would send `E` to `-t^{22}` and
flip the ODE sign, but would not change finiteness or `g-g(0)=O(t^6)`. The ODE
as stated is the `[f,g]=1` convention, and that convention is internally
consistent.

The producer verifier never derives this identity: it hard-codes the formula
for `E`. The identity is nevertheless correct.

---

## 3. Native face — CONFIRMED

Let `z=xy^4` and `B=x(z-1)^7`. Every monomial of `B` is
`\binom{7}{k}(-1)^{7-k} x^{k+1} y^{4k}` and has `(4,-1)`-weight `4`. Thus
`B^2` is homogeneous of weight `8` and `B^3` of weight `12`.

The added `f` terms have weights `4·8-32=0` and `-8`, both strictly below `8`.
The added `g` terms have weights `4`, `-4`, and `-12`, all strictly below `12`.
Independent expansion of the sparse polynomials therefore gives

```text
in_{4,-1}(f_face) = B^2,    in_{4,-1}(g_face) = B^3,
```

with the entire supports of `B^2` (15 terms) and `B^3` (22 terms) retained.
This is a maximum-face statement, not a claim that the extra terms vanish.

The `y=\infty` chart `x=t^3 X`, `y=t^{-1}`, `F=t^8 f`, `G=t^{12} g` selects
the Newton edge `j=3i+8` on `f` and `j=3i+12` on `g`. On that edge the only
`B^2` contribution is the vertex `x^{16} y^{56}`, and the only `B^3`
contribution is `x^{24} y^{84}`. The extra terms all lie on those edges, and
the closed forms in the chart are

```text
F = X^2 (X-t)^{14} - 2 X^8 + 1,
G = X^3 (X-t)^{21} - 3 X^{16} + 3 X^8 - 1.
```

The `t^0` coefficients are exactly `H^2` and `H^3` with `H=X^8-1`. Direct
extraction of the `y`-edge from the original `(x,y)` supports recovers the
same polynomials. So the face replacement does both jobs at once: it keeps the
native `(4,-1)` faces `B^2/B^3` at weights `8/12`, and it completes the
`y`-edge to `H^2/H^3`.

`H'=8X^7`. Euclid gives `gcd(H,H')=1` in `Q[X]`. `H` is squarefree, with eight
simple roots, the 8th roots of unity. Over `C` the factorization
`(X-1)(X+1)(X^2+1)(X^4+1)` is a product of distinct irreducibles over `Q`.

Firewall on this item: the full face polynomials are **not** a jet solution.
The same closed forms give native `F_1=-14 X^{15}` and native
`G_1=-21 X^{23}`, so

```text
D = G_1 - (3/2) H F_1 = -21 X^{15} ≠ 0,
```

and the native pair has `E_1≠0`. That is compatible with the writeup, which
claims only faces and the leading edge, then studies a general jet
`F=H^2+t F_1+\cdots` separately. Formula `(2.1)` is not a Keller pair.

---

## 4. General recurrence — CONFIRMED

With `F=\sum_i F_i(X) t^i` and `G=\sum_j G_j(X) t^j`, the coefficient of `t^n`
in `E` is obtained by collecting

```text
12 F_X G         ↝  12 F_i' G_j,
-8 F G_X         ↝  -8 F_i G_j',
- t F_X G_t      ↝  - j F_i' G_j,
+ t F_t G_X      ↝  + i F_i G_j'.
```

Hence, for every `n`,

```text
E_n = \sum_{i+j=n} ( (12-j) F_i' G_j + (i-8) F_i G_j' ).
```

This is an identity of formal power series in `t` with coefficients in any
`Q`-algebra, not a specialization. Independent comparison of this sum against
the expanded bivariate formula for `E` on a generic 2-jet
`(F_0,F_1,F_2)=(H^2,A,C)`, `(G_0,G_1,G_2)=(H^3,B,D)` matches for every
`n=0..4`. The same comparison on the two displayed root-sign packets matches
through `n=24`.

**Symbolic-ring audit.** The producer ring treats
`H,H',A,A',B,B',C,C',D,D',a,a'` as independent commuting indeterminates and
imposes the product rule by hand on `F_0=H^2`, `G_0=H^3`, on
`D=G_1-(3/2)HF_1`, and on the substituted `G_2` formula. That is the right
way to prove a polynomial identity, and it is stronger than a numerical
sample.

- Aliasing: the name `D` is the `E_1` deviation and later the `G_2` slot.
  The two uses are sequential, not simultaneous. No false identification.
- Omitted derivatives: `E_1` and `E_2` never need `H''`. Product rules for
  `F_0'`, `G_0'`, `G_1'`, and the substituted `G_2'` are present.
- Hard-coded output: `expected_e1` and `expected_e2` are independently built
  closed forms, then compared to the recurrence. That is a real identity
  check. Several later `RESULT.json` strings (fibre ODE, residue squares,
  pullback, raw map) are not computed by the verifier; they are checked in
  the sections below rather than accepted from the engine.
- Specialization: the free-ring identities restrict to any squarefree `H`.
  The same `E_1` factorization, `E_2` remainder, and `G_2` existence were
  rerun on `H=X^2-2` and `H=X^3-X-1` and hold verbatim. The check is not
  an `H=X^8-1` accident.

The ring does not prove uniqueness of `D` or of `G_2`, because uniqueness
uses that `'` is differentiation in a single variable `X`. Uniqueness is a
separate ODE argument, attacked in §§5–6.

---

## 5. Squarefree uniqueness / divisibility — CONFIRMED

Leading cancellation is the `n=0` case:

```text
E_0 = 12 F_0' G_0 - 8 F_0 G_0' = 24 H^4 H' - 24 H^4 H' = 0.
```

For `n=1`, with `A=F_1`, `B=G_1`, and `D=B-(3/2)HA`,

```text
E_1 = 22 H H' B - 8 H^2 B' + 12 H^3 A' - 21 H^2 H' A.
```

The claimed factorization expands, using the product rule on `D`, to the same
polynomial:

```text
E_1 = 2H ( 11 H' D - 4 H D' ).
```

This is an identity in the free jet, confirmed on `H=X^8-1`, `X^2-2`, and
`X^3-X-1`.

`E_1=0` in characteristic 0 therefore forces `11 H' D = 4 H D'`. At a simple
root `c` of squarefree `H`, this is `11 H'(c) D(c)=0`, so `D(c)=0`. Writing
`D=(X-c)^k u` with `u(c)≠0` and `k\in\mathbb{Z}_{\ge 0}`, the leading term of
`11 H'D-4HD'` is `H'(c) u(c) (11-4k)(X-c)^k`. Vanishing requires `k=11/4`,
which is not an integer. The only polynomial (or regular) solution is `D=0`.
Equivalently, `D'/D=(11/4)(H'/H)`, so `D=C H^{11/4}`, which is not a
polynomial unless `C=0`, because `H` is squarefree hence not a fourth power.

A nonzero polynomial `D` **cannot** appear after extending the coefficient
field. The map `D\mapsto 11 H'D-4HD'` is `Q`-linear on each finite-degree
slice of `Q[X]`. Gaussian elimination on degrees `\le 24` has kernel
dimension `0` for each of the three test `H`. Extending scalars to an
algebraic extension `K/Q` cannot create kernel. A ramified local solution
`D=H^{11/4}` exists in a Puiseux extension and is excluded by the
polynomial-coefficient hypothesis. So `E_1=0` forces `G_1=(3/2) H F_1` in
`k[X]` for every characteristic-0 field `k`.

After that substitution, the `n=2` recurrence expands to the identity

```text
E_2 = 20 H H' G_2 - 8 H^2 G_2' + 6 H F_1 F_1'
      - (21/2) H' F_1^2 + 12 H^3 F_2' - 18 H^2 H' F_2.
```

Every term except `-(21/2) H' F_1^2` is visibly divisible by `H`, so

```text
E_2 \equiv -(21/2) H' F_1^2  \pmod{H}.
```

Confirmed as a polynomial identity, not merely after reducing `F_1` modulo
`H`, and confirmed for `H=X^2-2` as well. Since `gcd(H,H')=1`, `E_2=0`
implies `H\mid F_1^2`. Squarefreeness upgrades this to `H\mid F_1`. In the
reduced ring `k[X]/(H)`, which is a product of fields, `F_1^2=0` still forces
`F_1=0`. No nilpotent escape exists over an algebraic extension.

Thus `E_1=E_2=0` forces `H\mid F_1` in polynomial coefficients. The tempting
jet with `F_1(c)\neq 0` at a root of `H` is nonextendable at `E_2`, even if it
passes `E_0` and `E_1`.

---

## 6. `G_2` coefficient formula — CONFIRMED

Write `F_1=Ha`. The claimed second coefficient is

```text
G_2 = (3/2) H F_2 + (3/8) H a^2.
```

Direct substitution into the `E_2` identity cancels in four blocks
(`H^2 H' F_2`, `H^3 F_2'`, `H^2 H' a^2`, `H^3 a a'`), so `E_2=0`. The same
substitution works for `H=X^2-2`. This is also the `t^2` coefficient of the
binomial expansion of `(H^2 + t H a + t^2 F_2)^{3/2}`, which is why the
writeup calls it the second coefficient of `F^{3/2}`.

Uniqueness: a homogeneous correction `Δ` satisfies
`20 H H' Δ - 8 H^2 Δ'=0`, i.e. `Δ'/Δ=(5/2)(H'/H)`, so `Δ=C H^{5/2}`. Not a
polynomial unless `C=0`, again because `H` is squarefree. The local
multiplicity test is `k=20/8=5/2`, not an integer. Linear algebra on degrees
`\le 20` has homogeneous kernel dimension `0`. Existence and uniqueness of
the polynomial `G_2` both hold.

The producer ring proves existence (`e2div={}`) after imposing the product
rule. It does not prove uniqueness; the ODE argument does, and it survives.

---

## 7. Rejected first jet — CONFIRMED

(The assignment listed this inside the `E_1/E_2` attack. It is recorded
separately because it is a negative mutation, not part of uniqueness.)

Native `F_1=-14 X^{15}` is the `t^1` coefficient of `X^2(X-t)^{14}`. The
family

```text
F_{1,λ} = -14 X^{15} + λ,    G_{1,λ} = (3/2) H F_{1,λ}
```

passes `E_1=0` for every `λ` by §5. Full expansion of `E`, not the remainder
shortcut, gives `E_0=E_1=0` and

```text
E_2 mod H:
  λ=13:  (0,0,0,0,0,-16464, 30576, -14196),
  λ=14:  (0,0,0,0,0,-16464, 32928, -16464).
```

Both are nonzero as polynomials, and both match the frozen table. At
`λ=14` one has `F_1(1)=0` and the remainder vanishes at `X=1`, which is the
tempting local cancellation, but the remainder does not vanish at `X=-1`
(`F_1(-1)=28`, remainder `65856`). The jet is not extendable at `E_2` and
cannot be used for a pole-count or splitting-count conclusion. Native
`λ=0` is likewise nonextendable (`remainder=-16464 X^5`).

---

## 8. Cusp normalization / map — CONFIRMED

At a simple root `c` of `H`, `u=H(X)` is an étale local coordinate because
`H'(c)\neq 0`. This identification is global as a polynomial and local as a
coordinate chart.

**Local / formal.** In a formal or analytic neighbourhood of `(X,t)=(c,0)`,
the Morse lemma with parameters puts `F` in the form `ũ^2+U(t)` by a
right-equivalence in `u`, and Weierstrass division of `G` by the quadratic
`F` puts `G` in the form `ũ^3+V(t)ũ+W(t)`. That is the bounded `A_2`
interface

```text
F = u^2 + U(t),    G = u^3 + V(t) u + W(t).
```

It is not a global polynomial automorphism of `(x,y)` or of `(X,t)`, and it
does not by itself preserve the global coefficient polynomial `E`.

**Raw map, before cleanup.** Expand `F=u^2+t F_1(X)+O(t^2)` and
`G=u^3+t·(3/2)u F_1+O(t^2)`. Evaluation at `u=0` (i.e. at `X=c`) gives

```text
U_1(c) = F_1(c),    V_1(c) = (3/2) F_1(c),    W_1(c) = 0.
```

No omitted unit, `H'(c)`, deck, or chart factor belongs in these *values*:
they are function evaluations. The chart Jacobian `dX/du=1/H'(c)` is already
absorbed by taking `u=H(X)` rather than `ξ=X-c`. Deck and chart tags still
have to travel with the tuple `(U_i(c),V_i(c),W_i(c))`; the writeup records
that tagging.

**Cleanup.** `U(t)` equals `F` along `u=0`, so it is invariant under unit
rescaling `ũ=u·(\mathrm{unit})^{1/2}` and under shifts `ũ=u+α t^k` that are
then re-completed to Morse form (those shifts change `U` only at order
`2k\ge 2`). Thus `U_1` is invariant. Section 5 forces `F_1(c)=0`, hence
`U_1(c)=0` both before and after cleanup. With `U_1=V_1=W_1=0`, first-order
unit mixing does not create a new weight-one cusp parameter.

**Global / polynomial.** A global polynomial with `U` independent of `X` is a
special ansatz, not the output of local Morse. The later choice `U_{14}=X` is
an interpolant of the eight local values `U_{14}(c)=c`. It is
`X`-dependent, so it is not in the strict local normal form globally. That
is why a rootwise unit can hold while a global `E_{22}=1` fails (§12).

Weight eight is resonant for `U` (the local operator coefficient `k-8`
vanishes at `k=8`); `V_8` and `U_8` become independent cusp data. Weight
twelve is the first `W` resonance. Those statements are about the local
interface, not about a global polynomial lift.

---

## 9. Fibre ODE / generic-finite scope — CONFIRMED

On a branch of the fibre `F(X(t),t)=a t^8`,

```text
X' = (8 a t^7 - F_t) / F_X.
```

Along that branch,

```text
t^{13} F_X \frac{d}{dt}(t^{-12} G)
  = -12 F_X G + t F_X G_X X' + t F_X G_t
  = -12 F_X G + 8 F G_X - t F_t G_X + t F_X G_t
  = -E.
```

For a Keller jet, `E=t^{22}`, so

```text
\frac{d}{dt}(t^{-12} G) = - t^9 / F_X.
```

Sign and powers match the assignment. The producer verifier stores this as a
string; the derivation above does not use that string.

**When `ord_t(F_X)=4`.** On this square edge write
`F=H(X)^2 + t^8 S(X) + \cdots`. The fibre equation is
`H(X(t))^2=(a-S(X(t))) t^8+\cdots`. At a simple root `c`,
`H(X)\sim H'(c)(X-c)`. If `a\neq S(c)` (equivalently the local cusp
discriminant `q^2=a-U_8(c)` is nonzero), one has
`H(X(t))=q t^4+O(t^5)` with `q\neq 0`, and

```text
F_X = 2 H H' + t^8 S' + \cdots = 2 q H'(c) t^4 + O(t^5),
```

so `ord_t(F_X)=4` because `q H'(c)\neq 0`. Then
`-t^9/F_X=O(t^5)`, hence `dg/dt=O(t^5)` and `g=g(0)+O(t^6)`. A pole of `g` at
`t=0` would make `g'` of strictly more negative order, contradicting
`O(t^5)`. So `g` is finite on the branch.

**When this fails.** The order-four count is invalidated by a
cusp-discriminant / special-fibre collision `a=S(c)` (or `a=U_8(c)` in the
normalized packet), by a multiple root `H'(c)=0` (excluded here by
squarefreeness), or by an accidental cancellation of the `t^4` coefficient of
`F_X` against higher `X`-dependent terms. Those collisions can change the
Eggers–Wall tree. They do not license a *generic* pole mutation on this edge.

**Narrow conclusion, accepted:** on generic tagged branches of this square
edge, in the `y=\infty` chart, `g` is finite and `g-g(0)=O(t^6)`. Rejected:
any claim about all fibres, all edges, the `x=\infty` chart, or the absence of
global poles of a completed polynomial pair. The writeup and `RESULT.json`
stay inside the narrow statement (`PINNED-FINITE for generic tagged fibres`).

---

## 10. Both formal mutations — CONFIRMED

The displayed packets are

```text
S_+ = (1/4)( 3 + X - X^2 + X^3 - X^4 + X^5 - X^6 + X^7 ),
S_- = (1/4)(-1 + X - X^2 + X^3 + 3 X^4 + X^5 - X^6 + X^7 ).
```

All eight coefficients of each are nonzero. Both satisfy `S^2\equiv 1\pmod H`.
Independent division gives polynomial quotients, and

```text
Q_S = 3(S^2-1)/(8H) = (3/8)(S^2-1)/H
```

has every degree `0..6` coefficient nonzero:

```text
Q_+:  (21/128, -9/64, 15/128, -3/32, 9/128, -3/64, 3/128),
Q_-:  (45/128,  3/64, -9/128,  3/32,  9/128, -3/64, 3/128).
```

The pairs

```text
F_S = H^2 + t^8 S,
G_S = H^3 + (3/2) t^8 H S + t^{16} Q_S
```

have identical `(t,X)` support

```text
F: t^0 X^{0..16}, t^8 X^{0..7};
G: t^0 X^{0..24}, t^8 X^{0..15}, t^{16} X^{0..6}.
```

Independent expansion of `E` yields `E_n=0` for all `n=0..23`, in particular
`E_0=\cdots=E_{21}=0` and `E_{22}=0`. Support alone already forces `E_{22}=0`:
the only bidegrees present in `(F,G)` sum to `n\in\{0,8,16,24\}`. The packets
therefore satisfy every vanishing coefficient before the constant-Jacobian
slot and do not supply that slot. They are not Keller jets. (As a side
observation, not claimed by the producer: `E_{24}\neq 0` for both packets.)

Remainders modulo the four rational factors of `H` are the constants

```text
S_+ :  (X-1, X+1, X^2+1, X^4+1)  ↦  (+1, -1, +1, +1),
S_- :  (X-1, X+1, X^2+1, X^4+1)  ↦  (+1, -1, +1, -1).
```

On the tagged fibre `a=1`, degeneracy is `S(c)=1`. The `+1` loci have degrees
`1+2+4=7` and `1+2=3` respectively.

On the generic tagged fibre `a=2`, `q^2=2-S(c)` is `1` or `3`, never `0`. The
finite residue of `g` at `t=0` is `q^3+(3/2)S(c)q`, and

```text
(q^3 + (3/2) S q)^2 = (2-S)(2 + S/2)^2
  = 25/4  if S=+1,
  = 27/4  if S=-1.
```

These squares are identities in `S=\pm 1`; they do not use `Q_S`. They are
hard-coded as strings in the producer verifier and are nevertheless correct.

The two packets are formal local mutations with the same coarse `H^2/H^3`
face and the same `(t,X)` support, but different deck/Galois sign patterns
and different degeneracy degrees. They are not polynomial-source mutations
and not Keller mutations.

---

## 11. Polynomial provenance rejection — CONFIRMED

A term `t^{16} X^i` in `G` pulls back under `x=t^3 X`, `y=t^{-1}`,
`g=t^{-12}G` as

```text
t^4 X^i = y^{-4} (x y^3)^i = x^i y^{3i-4}.
```

The exponents `3i-4` are negative precisely for `i=0,1`, giving Laurent
monomials `y^{-4}` and `x y^{-1}`. Both displayed `Q_S` have nonzero
coefficients in degrees `0` and `1`, so both packets are excluded by
polynomial source support.

The general low-coefficient argument is also correct in this window. For
`\deg S<8` (the displayed `t^8` support), `S^2-1=(X^8-1)q` with `\deg q\le 6`
gives

```text
s_0^2 - 1 = -q_0,    2 s_0 s_1 = -q_1.
```

Polynomial source requires `q_0=q_1=0`, hence `s_0^2=1` and `s_1=0`. If
additionally `S(c)=\pm 1` at all eight roots of `H` — which is `S^2\equiv 1
\pmod H` — then `S` is the unique degree-`<8` interpolant of those signs, and

```text
s_0 = (1/8) \sum_{ω^8=1} S(ω)
```

is their average. Then `s_0=\pm 1` forces every sign to be the same. Uniform
packets are `S\equiv\pm 1`, for which `q=0` identically. No nonconstant
root-sign mutation survives this bounded polynomial-source window.

The averaging step uses that the roots are exactly `μ_8`. It is not a
statement about a general squarefree `H`. That is the correct scope for this
edge. Allowing `S=S_{\mathrm{red}}+H T` with `T\neq 0` leaves the displayed
support window; it is not a counterexample to the bounded claim.

These examples must not be called polynomial-source or Keller mutations. The
writeup and `RESULT.json` do not do so.

---

## 12. Determinant carrier — CONFIRMED

In the local normal form, at `u=0`,

```text
F_X=0,   G_X=V H',   F_t=U',   G_t=W',   F=U,   G=W,
```

so

```text
E = H' V (-8U + t U').
```

For `U=U_k t^k` and `V=V_m t^m` with `k+m=22`,

```text
E_{22} \big|_{u=0} = (k-8) H'(c) V_m(c) U_k(c).
```

The weight-eight slot `k=8` is resonant (`k-8=0`) and cannot carry the unit.
The first slot that uses the native `t^8` deformation of `G` is `k=14`,
`m=8`, with coefficient `6`:

```text
6 H'(c) V_8(c) U_{14}(c) = 1.
```

The global interpolant `U_{14}=X`, `V_8=1/48` satisfies this modulo `H`,
because

```text
6 H' X · (1/48) = X H' / 8 = X·8X^7 / 8 = X^8 \equiv 1 \pmod{H}.
```

The congruence is an identity in `Q[X]/(H)`, so it holds at all eight roots,
not only at the rational roots `X=\pm 1`. Independent reduction confirms
`6 H' U_{14} V_8 \equiv 1\pmod H`.

This pair is a truncated global ansatz
`F=H^2+t^{14}X`, `G=H^3+t^8 H/48`, not a completed Keller jet: `E_{14}\neq 0`
already. The claim is only that this is a rootwise unit carrier in the
support window, which it is.

---

## 13. Global `13H/12` gap — CONFIRMED

Full expansion of `E` for that truncated pair, using only the `(i,j)=(14,8)`
summand in the recurrence, gives

```text
E_{22} = 4 U_{14}' V_8 + 6 U_{14} V_8'
        = 4·1·(H/48) + 6 X (H'/48)
        = H/12 + X^8
        = 1 + (13/12) H.
```

Independent bivariate expansion matches this polynomial exactly
(`E_{22}=-1/12+(13/12)X^8`). Reducing modulo `H` recovers the rootwise unit
`1`. The extra `(13/12)H` is therefore a genuine global remainder, not an
artifact of a local chart factor already cancelled by `U_{14}=X`.

The rootwise fixture cannot remove it. Any polynomial `U_{14}` with
`6 H' V_8 U_{14}=1` identically in `Q[X]` would require `X^7 U_{14}` constant
when `V_8=1/48`, hence `U_{14}` Laurent. Adding a multiple of `H` to `U_{14}`
or `V_8` is a higher-`u` correction, which is exactly the unsolved lift named
in the writeup. Residue agreement at the eight roots is not a global
`E_{22}=1` polynomial lift.

---

## 14. Final scope — CONFIRMED

The charged artifacts claim, and only claim:

1. one exact square/cube-edge recurrence for this `y=\infty` face;
2. a generic finite-pole pinning statement on tagged branches of that square
   edge;
3. two rejected formal root-sign mutations, fail-closed at polynomial
   provenance;
4. a bounded cusp provenance interface `(U,V,W)` with an explicit unsolved
   global `E_{22}=1` lift.

They do not claim a Keller pair, a counterexample, a global GGV-to-tree
functor, source/landing coverage, `G2-PSC`, `G2-BD`, or JC2. The title phrase
“Keller-face” refers to the square/cube leading form, not to a completed
Keller jet. The phrase “`G2-PSC`-adjacent carrier” is explicitly not a
`G2-PSC` theorem. The compiler interface is described as the *kind* of typed
map a later global argument would need, with the gluing, landing, and
both-chart coverage steps listed as unasserted.

Maximum permitted result reached, not exceeded.

---

## Independent arithmetic (desk scale)

All identities above were rerun in `Q` with univariate polynomials (low
coefficient first) and sparse `(t,X)` supports. No producer function was
imported. The producer `PASS` token was not used. A freeze-consistency replay
of `verify.py` matches frozen `RESULT.json` and is not a mathematical
witness.

No failing identity, root, source exponent, or missing hypothesis was found,
so no additive repair is required on the charged control.
