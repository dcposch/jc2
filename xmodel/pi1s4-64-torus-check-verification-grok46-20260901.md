# TORUS-CHECK verification (computation and countermodel arm)

Lane: TORUS-CHECK, computation/countermodel only.
Date: 2026-09-01.
Verifier: grok-4.6.
Independence: this arm does not consult the gate lane and does not inspect `jc2-lean`.

Charged frozen inputs (paths under `/private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.VGQvGD/inputs/`):

- `pi1s4-64-torus-check-opus5-20260831.md`
- `pi1s4-64-zvk-u6-opus5-20260831.md`
- `block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md`

## 0. Hash check and source inventory

Frozen inputs were hashed with `shasum -a 256` before any was read. All three match the boxed manifest; the stop condition was not triggered.

```text
a352be2af1aebb5e158cb541a6eacdd0feb90f2ea3aa6750fb4bf1969c6bfefe  pi1s4-64-torus-check-opus5-20260831.md
d0dc4f7971b39f516dae2337cb172f8357bb1618b1143b800c524dbf95b5f31a  pi1s4-64-zvk-u6-opus5-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Literature re-fetched from arXiv and re-hashed (PDFs, not paraphrases). Both reproduce the charged torus-check §0 receipts byte-for-byte.

| tag | source | URL | SHA-256 |
|---|---|---|---|
| Sh12 | Shirane, arXiv:1211.2526v1, 9 pp. | `https://arxiv.org/pdf/1211.2526v1` | `b37e8d45381a299e489516fd479ec896a016f06c402b16ae049d310aa1618153` |
| Oka05 | Oka, arXiv:math/0507051v1, 12 pp. | `https://arxiv.org/pdf/math/0507051v1` | `2a864cdd2530533c30f45d2cf9e9435e24f6a53b3788094df26a63e7208213e4` |

Sh12 Corollary 0.6 is the displayed identity `G_2^3+G_3^2=0` with the printed `i=1,2` a typo for `i=2,3` (the identity names `G_2,G_3`). Oka05 Proposition 2 and Lemma 3 match the charged quotes. No CAS was run; no job of uncertain duration was run. Arithmetic below is hand expansion, evaluated on the parametrisation.

ROW-NF (charged `zvk-u6` §1.3, consumed as a statement): every residual row member is, after a target automorphism,

```text
x = r(t)^2 ,  y = q(t) ,  r = t^3 + b t + c ,  q = t^4 + (2b/3) t^2 + (4c/3) t ,  c ≠ 0 ,
```

with modulus `j = b^3/c^2`. The identity `q = t r − (b/3) t^2 + (c/3) t` is used throughout. Plus-branch singular pairs are the roots of `h(e_1) = e_1^3 + (4b/3) e_1 − 4c/3`, `e_2 = e_1^2+b`. At a plus-pair the image point is

```text
r_node = (b e_1 + c)/3 ,   x_node = (b e_1 + c)^2 / 9 ,   y_node = (b/3)(e_1^2 + b) .
```

Charged torus-check excludes only `j ∈ {-27/4, -81/16}`. The two test points are `(b,c)=(0,1)` (`j=0`) and `(1,1)` (`j=1`), as the charge suggests.

Execution constraint observed: no `jc2-lean`, no charged-file writes, no canonical ledgers. No `charge_basis` line is declared (no new exit-price assertion).

## 1. Implicit sextic F_j at two parameter points

Structured elimination: first the degree-4 equation `G(u,y)=0` of `D' = {(r(t),q(t))}`, then `F(x,y) = G(√x,y)\,G(-√x,y)` (equivalently `Res_u(u^2-x, G)`). This is the resultant of `x-r(t)^2` and `y-q(t)` factored through the fold.

### 1.1 Point `(b,c)=(0,1)`

Here `r=t^3+1`, `q=t^4+(4/3)t`, so `t^3=u-1` and `y=t(u+1/3)`. Hence `y^3=(u-1)(u+1/3)^3`. Expanding the right-hand side:

```text
(u-1)(u+1/3)^3 = u^4 − (2/3) u^2 − (8/27) u − 1/27 ,
G(u,y) = y^3 − u^4 + (2/3) u^2 + (8/27) u + 1/27 .
```

Writing `A = y^3 − x^2 + (2/3)x + 1/27` one gets `G(√x,y)=A+(8/27)√x` and `G(-√x,y)=A-(8/27)√x`, so

```text
F_{(0,1)} = A^2 − (64/729) x
         = y^6 − 2 x^2 y^3 + (4/3) x y^3 + x^4 − (4/3) x^3
           + (2/27) y^3 + (10/27) x^2 − (28/729) x + 1/729 .
```

The `y^6` term is present, so `deg F=6`. Clearing `729`: `729 y^6 − 1458 x^2 y^3 + 972 x y^3 + 729 x^4 − 972 x^3 + 54 y^3 + 270 x^2 − 28 x + 1`. Checks: `t=0` gives `(x,y)=(1,0)` and `F=0`; `t=1` gives `(4,7/3)` and `F=0`.

The image of irreducible `A^1` is irreducible, and a generic line pulls back to degree 6, so `F` is reduced irreducible of degree 6. Homogenising the parametrisation in the chart `X=1` (charged (1.1), re-derived): `v(s)=s^2 U(s)`, `w(s)=s^6 V(s)` with `U(0)=V(0)=1`. One place `Q_∞=[1:0:0]`, `mult=2`, `I(C,L_∞;Q_∞)=6`, so `C ∩ L_∞ = {Q_∞}`. Arithmetic genus `p_a=10`.

**Nodes fail.** The three plus-pairs have `e_1^3=4/3` and `y_node=(b/3)(e_1^2+b)=0`, `x_node=c^2/9=1/9`. All three parameter-pairs map to the single point `P=(1/9,0)`. The six putative parameters collapse to the three cube roots of `-4/3`, each with `γ'≠0` and three distinct slopes `dy/dx=2/t^2`. Translating `X=x-1/9`, `Y=y` in `F`, linear and quadratic parts vanish and the cubic tangent cone is `(8/81)(2Y^3−9X^3)`, three distinct lines. So `P` is an ordinary triple point (analytically `D_4`), with `δ=(μ+r−1)/2=(4+3−1)/2=3`. Thus `δ_aff=3` still, `δ_∞=7`, unibranch multiplicity 2 gives semigroup `⟨2,15⟩` and type `A_{14}` at `Q_∞`. The charged `3A_1` is false at `j=0`.

This is uniform in `c`: `y_node=(b/3)(e_1^2+b)` is independent of the three roots of `h` if and only if `b=0`, and then `x_node=c^2/9` is likewise constant. Distinct geometric nodes require `b≠0` (i.e. `j≠0`) in addition to `disc h ≠ 0` (`j≠-81/16`) and `disc r ≠ 0` (`j≠-27/4`). The charged three-ordinary-node stratum is missing `j=0`. Charged `zvk-u6` §3.5 uses `(b,c)=(0,1)` as a regular row member; that use is the same miss.

### 1.2 Point `(b,c)=(1,1)`

From `q = t r − t^2/3 + t/3` one has the quadratic `t^2 − (3u+1)t + 3y = 0`. Euclidean remainder of `t^3+t+(1-u)` against this quadratic is `P t + Q` with `P=(3u+1)^2+1-3y` and `Q=1-u-3y(3u+1)`. The resultant is `3y P^2 + (3u+1) P Q + Q^2`. Substituting `w=3u+1`, `z=3y` and collecting powers of `z`, the degree-5 terms cancel and

```text
G(u,y) = −27 u^4 + (54 y + 16) u^2 + 8 u + 27 y^3 − 18 y^2 − 3 y + 3 .
```

(Checked: `G(1,0)=0` for `t=0`; `G(3,3)=0` for `t=1`.) Then `G(√x,y)=M+8√x`, `G(-√x,y)=M-8√x` with

```text
M = −27 x^2 + (54 y + 16) x + 27 y^3 − 18 y^2 − 3 y + 3 ,
F_{(1,1)} = M^2 − 64 x .
```

Leading term `729 y^6`, so degree 6, irreducible by the same parametrisation argument. Checks: `(x,y)=(1,0)` and `(9,3)` vanish. Infinity germ identical to §1.1 (the Puiseux leading terms do not use `(b,c)` except through units `U(0)=V(0)=1`): `A_{14}` at `Q_∞`.

**Three ordinary nodes hold.** The cubic `h(e)=e^3+(4/3)e-4/3` has derivative `3e^2+4/3>0`, hence three distinct roots (one real). Then `y_node=(e^2+1)/3` are distinct (a pair `e,-e` cannot both be roots: `h(e)+h(-e)=-8/3≠0`). The parameters of each pair are distinct because the quadratic discriminant `-3e^2-4<0`. Both branches are smooth (`r_node=(e+1)/3≠0` since `h(-1)≠0`; `q'≠0` whenever `r'=0`). Tangents are distinct: the Wronskian `r'(t)q'(s)-r'(s)q'(t)` reduces on a plus-pair to a factor `B=3e^2+9e+4`, and `gcd(B,h)=1` by the Euclidean check that `e=-8/27` is not a root of `h`. So three ordinary nodes, `δ_aff=3`, `δ_∞=7`, `A_{14}`.

### 1.3 Verdict

**BROKEN** as a uniform `3A_1` claim on the charged stratum `j∉{-27/4,-81/16}`. Degree 6 and the `A_{14}` germ **hold at both test points**. The three-node configuration holds at `(1,1)` and fails at `(0,1)`, where the affine singularity is a single ordinary triple point (`D_4`) of `δ=3`. The missing excluded modulus is `j=0`. Theorem NO-TORUS as stated applies on `j≠0`; the `j=0` fibre is a different equisingular type and is tested separately in §2.

## 2. Theorem NO-TORUS at the two points

The affine identity is `A^3 − B^2 = λ F` with `deg A ≤ 2` (6 coefficients), `deg B ≤ 3` (10 coefficients), and scalar `λ`. This is 28 equations (monomials of degree `≤ 6` in two variables), cubic in `A` and quadratic in `B`. Elimination is by (i) the parametrisation, (ii) the degree-6 homogeneous part (uniformly a multiple of `y^6`, because `F̄ ∩ {Z=0} = {Q_∞}` with multiplicity 6), and (iii) the degree-4 remainder `x^4`.

On the curve, `a(t) := A(r(t)^2,q(t))` and `b(t) := B(r(t)^2,q(t))` satisfy `a^3=b^2` in `C[t]`. The six monomials of a degree-`≤2` polynomial pull back with pairwise distinct `t`-degrees `12,10,8,6,4,0` and leading coefficient `1` at both test points, so the evaluation map on coefficients of `A` is triangular of rank 6.

### 2.1 Point `(1,1)` — parametrisation kill

Affine singularities are three ordinary nodes. Lemma 2.2 (inner points of `A^3+B^2` cannot be ordinary nodes: the degree-2 part is a square, hence a double line or else multiplicity `≥3`) implies `A` cannot vanish at a node. There are no other affine singularities, so `a(t)` has no root, hence `a=α ∈ C^*` and, by the triangular degrees, `A` is constant. Then `F = (α^3 − B^2)/λ` is a difference of a constant and a square, a product of two cubics, contradicting irreducibility. This is charged §3.2, and the only geometric input that needed checking was that the three nodes are distinct ordinary nodes, done in §1.2.

The same conclusion follows from leading forms without Lemma 2.2; that argument is recorded in §2.2 because it is the one that still works at `j=0`.

### 2.2 Point `(0,1)` — leading-form elimination (Lemma 2.2 fails)

At `j=0` the affine singularity is `D_4`, which *can* be inner, so `A(P)=B(P)=0` is not excluded and the parametrisation may vanish at the three roots of `t^3+4/3=0`. That loophole is closed by homogeneous parts of `F_{(0,1)}`:

```text
F_6 = y^6 ,   F_5 = −2 x^2 y^3 ,   F_4 contains x^4 .
```

(The identity `F_6 = κ y^6` is row-level, not special to `(0,1)`.) Write `A_2`, `B_3` for the top homogeneous pieces. Then `A_2^3 − B_3^2 = λ y^6`. Setting `f(z)=A_2(z,1)`, `g(z)=B_3(z,1)`, one has `f^3−g^2=λ`.

- If `deg f=2` and `λ≠0`, this is a nonconstant polynomial parametrisation of the elliptic curve `Y^2=X^3−λ`, genus 1, impossible. If `λ=0` the degree-6 part of `F` vanishes, contradicting `y^6`. So the top of `A` cannot involve `x^2` or `xy`.
- Hence `A_2 = r y^2`, `B_3 = v y^3` with `r^3−v^2=λ`.

If `r=0`, then `λ=−v^2` and `B = v U + C` with `U=y^3−x^2+(2/3)x+1/27` and `deg C≤2` actually `≤1` after matching `x^2 y^3`. The identity `A^3 − (v U+C)^2 = −v^2 (U^2−(64/729)x)` collapses to `A^3 − 2v C U − C^2 = (64 v^2/729) x`. Degree 5 in `C U` forces `C` constant; cubics then force the linear part of `A` to vanish; the remainder is a constant cube equal to a multiple of `x`, hence `λ=0`, contradiction.

If `r≠0` then `v≠0` (else `λ=r^3` and the `x^2 y^3` coefficient of `−B^2` cannot match `−2λ`). Matching `x^2 y^3` gives `v e = λ` where `e` is the coefficient of `x^2` in `B`; matching `x^4` gives `−e^2=λ`. Then `λ=−v^2`, so `r^3−v^2=−v^2`, hence `r=0`, contradiction.

No solution at `(0,1)`. Independently, Oka05 Proposition 2 (fetched) forbids an inner `D_4` (admissible inner simple types are `A_{3ι−1}` and `E_6` only), so the only candidate inner point is `Q_∞` of type `A_{14}`, contributing `ρ=5≠6`. That argument also kills torus type at `j=0`, but uses the fetched proposition; the leading-form kill does not.

### 2.3 Point `(1,1)` — leading forms as a second kill

`F_{(1,1)}=M^2−64x` has `F_6=729 y^6` and `F_4` containing `729 x^4`, plus an extra `F_5=2916 x y^4 − 1458 x^2 y^3`. The genus-1 obstruction on `F_6` still forces `A_2 ∥ y^2`, `B_3 ∥ y^3`. Matching `x^2 y^3` and `x^4` again yields `r^3=0`, contradiction. The extra `x y^4` term does not open a solution.

### 2.4 Verdict

**HOLDS** at both parameter points. At `(1,1)` this is Theorem NO-TORUS on the three-node stratum. At `(0,1)` the charged proof that uses Lemma 2.2 on nodes does not apply, but exact elimination of `A^3−B^2=λ F` still has no solution, and Oka's `ρ`-count supplies an independent literature kill. No torus structure exists at either test point.

## 3. Conic-criterion count (§2)

Space of conics: homogeneous quadrics on `P^2`, dimension 6, basis `X^2, XY, Y^2, XZ, YZ, Z^2`. In the chart `X=1` these restrict to `1, v, v^2, w, vw, w^2`. On the `A_{14}` branch, using `v=s^2 U`, `w=s^6 V` with `U(0)=V(0)=1` (valid at both test points, and at every `(b,c)` with those leadings):

```text
ord 1 = 0 ,  ord v = 2 ,  ord v^2 = 4 ,  ord w = 6 ,  ord vw = 8 ,  ord w^2 = 12 .
```

All six orders are distinct; order 10 is absent. Distinctness is triangular (each leading coefficient is `1`), so a general conic has `ord_s = min{ orders of nonzero terms }` with no cancellation. In particular there is no conic of exact contact `10`.

**Prescribed contact at `Q_∞`.** Tokunaga (Oka05 Lemma 3, fetched) asks `I(C,C_2;P)=2ρ(P,5)` at each intersection point. An inner `A_{14}` has `ρ=5`, so contact `10`. Because order 10 is missing, `I≥10` is the same five linear conditions as `I≥12` (kill orders `0,2,4,6,8`), and the solution is exactly `C · Z^2`, which realises contact `12`, not `10`. Bézout for a torus conic gives total intersection `12`; if the only point is `Q_∞` then `I=12` and the germ would be `A_{17}` (`ι=6`), not `A_{14}`. Either reading: the contact conditions at `A_{14}` are **five independent linear conditions**, corank 1, unique candidate the double line at infinity.

**Through the three nodes.** Vanishing at an affine ordinary node is one linear condition per node. The unique candidate `Z^2` does not contain any affine point, so the three node conditions are independent of the five at infinity and the combined system is empty. (At `(0,1)` there is one triple point rather than three nodes: imposing passage through `P` is still one condition, and `Z^2` still misses it.)

Charged torus-check Lemma 2.2 already inverts the original budget: for a torus structure the conic must *avoid* ordinary nodes (they cannot be inner). The load-bearing count is therefore the five conditions at `Q_∞`, not three node incidences. The naive count "3 nodes + infinity contact" overdetermines and is empty; the correct torus-side count is 5, leaving `⟨Z^2⟩`, excluded by irreducibility (`Z^6+G_3^2` splits).

Oka05 Proposition 2 supplies the global arithmetic: inner simple `ρ`-sum equals 6, while `A_{14}` contributes 5 and `A_1`/`D_4` cannot be inner, so the sum is `0` or `5`, never `6`. That is a count of inner types, not of linear conditions on conics, and it is consistent with the linear algebra above.

### Verdict

**HOLDS.** Five independent conditions at the `A_{14}` place on a 6-dimensional space of conics, unique candidate `Z^2`, excluded. Imposing the three nodes in addition makes the system empty. The charged correction that nodes are not imposed is confirmed; the original "3 conditions for 3 nodes" is the wrong linear algebra. The count is the same at `(1,1)` and (with one triple point in place of three nodes) at `(0,1)`.

## 4. INF-TRIVIAL feeds: x-projection discriminant census

Vertical critical points of `D → C_x` occur where `dx=0`, i.e. `2 r r' dt=0`, together with the nodes (identified parameters). Equivalently, `Res_y(F, ∂F/∂y)=0`. The charged census is `|Σ_x|=6` downstairs and `|Σ_u|=11` upstairs, with three simultaneous half-twists over `x=0`.

### 4.1 Direct `∂F/∂y` at `(b,c)=(0,1)`

`F=U^2−(64/729)x` with `U=y^3−x^2+(2/3)x+1/27`, so `F_y=6 y^2 U`. Common zeros of `F` and `F_y` are:

- `U=0` and `F=0` ⇒ `x=0`. Then `U(0,y)=y^3+1/27=0`, three values `y=−1/3` and the two complex cube roots. These are the three roots of `r(t)=t^3+1=0`, each simple (`r'=3t^2≠0` there), with `q'(τ)=−8/3≠0`.
- `y=0` and `F(x,0)=0`. Expanding gives the degree-4 equation `729 x^4 − 972 x^3 + 270 x^2 − 28 x + 1 = (9x−1)^3 (x−1)`. So `x=1/9` (the triple point, multiplicity 3 along `y=0`, not a smooth vertical tangency) and `x=1` (the collided `r'=3t^2=0` at `t=0`: `x−1=2t^3+t^6`, ramification index 3, `q'(0)=4/3≠0`, a genuine vertical tangent).

Thus `Σ_x = {0, 1/9, 1}`, cardinality **3**, not 6. The upstairs count is `|Σ_u|=2|Σ_x|−1=5` (`u ∈ {0, ±1/3, ±1}`), not 11. The parenthetical "11 values" **fails at the requested point**. The failure is the `j=0` degeneration of §1.1: three nodes coalesce at `x=1/9` and the two roots of `r'` coalesce at `t=0`.

### 4.2 The three `x=0` half-twists, still at `(0,1)`

Near `x=0`, `r(t)=±√x` about each simple root `τ` of `r`, and `y=q(τ)±(q'(τ)/r'(τ))√x+O(x)`. The three centres are `q(τ)=τ/3` for `τ^3=−1`, i.e. `−1/3` and `(1/2±i√3/2)/3`, **three distinct `y`-levels**. For small `x` the six points therefore occupy three disjoint disks, each disk containing a swapping pair. In a geometric basis adapted to the three clusters the local braid is a product of three pairwise disjoint half-twists (a perfect matching of the six strands). They remain disjoint transpositions in the fibre ordering. This subclaim **holds** at `(0,1)`, and is the only input INF-TRIVIAL needs from the census (charged (5.2)–(5.3)).

### 4.3 Generic census, checked at `(1,1)`

At `(1,1)`: `r'=3t^2+1=0` gives `t=±i/√3`, two distinct values; `r(t_j)=1±2i/(3√3)`, two distinct nonreal, nonzero, non-opposite `x`-values `23/27±4i/(3√3)`. Node `x=(e+1)^2/9` for the three roots of `3e^3+4e−4=0`. The real root is not `-1`, so no node at `x=0`. Real parts of the complex node-`x` and of the tangency-`x` cannot agree: equating them forces `e^2+2e+16=0`, no real `e`. Conjugate node-`x` have nonzero imaginary part (`e=2` is not a root of `h`). Hence five distinct nonzero values plus `{0}`, so `|Σ_x|=6` and `|Σ_u|=11`. The charged census holds on `j∉{0,-27/4,-81/16}`, not merely on the charged two-point complement.

### 4.4 Verdict

**BROKEN** for the charged 11-value census at the requested point `(0,1)`. The three simultaneous tangencies over `x=0` and the disjointness of the three half-twists **hold** at `(0,1)` and at `(1,1)`, so the feed actually used by Theorem INF-TRIVIAL is intact. The 11-count is a generic-stratum statement; `j=0` is an extra discriminant collision, missed by both charged reports. INF-TRIVIAL itself does not consume `|Σ_x|=6` or `|Σ_u|=11`.

## 5. Riemann-Hurwitz fibre-line identity (§5.5)

Let `L ≅ P^1` be a fibre line of a degree-4 cover with six finite transposition branch points and monodromy `Π` about the remaining point of `L`. Riemann-Hurwitz:

```text
2g−2 = 4(−2) + 6·1 + (4 − c(Π)) = 2 − c(Π) .
```

`Π` is even (six transpositions), hence `Π ∈ A_4`, so `c(Π) ∈ {2,4}` (identity: `c=4`; 3-cycles and double transpositions: `c=2`). Both candidate pairs are integral:

| `(c(Π), g_L)` | `2g−2` | `2−c` | RH |
|---|---|---|---|
| `(2,1)` | `0` | `0` | yes |
| `(4,0)` | `−2` | `−2` | yes |

The D1-DEGREE relation `d = 2 g_L + c(Π) + 2` at `d=6` is the same identity rewritten: `6 = 2g_L + c + 2` is equivalent to `2g_L = 4−c`, which is RH. Both pairs satisfy it; the second constraint is not independent of the first.

**Euler characteristic `χ_c(Y)=3`.** This is an invariant of the affine 4-cover `Y → C^2` branched along `D`, not of a fibre pencil. Directly: `χ_c(C^2−D)=3` (affine `D` has `χ_c=−2`), an unramified 4-cover contributes `12`; the smooth part of `D` has `χ_c=−5` and three preimages, contributing `−15`; three nodes with `a_p=0` contribute two points each, `+6`. Total `12−15+6=3`. The charged stratification of `zvk-u6` §4.4 (generic `−2`, three node fibres `−2`, two tangency fibres `−1`, the `x=0` fibre `+1`, over `χ_c(C_x∖Σ_x)=−5`) reproduces `3` on the generic stratum `|Σ_x|=6`. None of these terms involves `(c(Π),g_L)`, which records only how the *compactified* fibre meets `L_∞`. Both pairs are compatible with `χ_c(Y)=3`.

**Which survives all three constraints?** Both. The three constraints do not adjudicate charged §5.5.

What *does* select a value is the identification of the pencil. Vertical lines `{x=const}` all pass through `Q'=[0:1:0]`. By §1, `C ∩ L_∞ = {Q_∞}=[1:0:0] ≠ Q'`, so a generic vertical line meets `C` in six affine points only. The product `Π` of the six fibre meridians is a meridian of `L_∞`. Theorem INF-TRIVIAL then gives `Π=e` for any involution-valued representation, hence `(c,g_L)=(4,0)` for the `x`-pencil (and likewise for a generic pencil, whose base point is also off `C`). The pair `(2,1)` is the RH datum of a *different* pencil: horizontal lines `{y=const}` pass through `Q_∞`, meet the `A_{14}` germ with contact `2`, and `Π` is not a meridian of `L_∞`. Charged `zvk-u6` §4.2's justification ("the line `x=c` meets `D̄` at `Q_D` where the place is unibranch of multiplicity 2") describes the horizontal pencil and is false for the vertical one. That is the location of the conflict, not a failure of RH.

On the `j=0` fibre the affine Euler computation must be rewritten (one `D_4` instead of three nodes; `|Σ_x|=3`), so `χ_c(Y)=3` is not claimed there. The RH identity itself is pencil-and-stratum independent.

### Verdict

**HOLDS** as an identity. Both `(2,1)` and `(4,0)` survive all three written constraints. For the `x`-projection used by INF-TRIVIAL, the incidence `Q' ∉ C` plus involution meridians selects `(4,0)` uniquely. The promoted downstairs `(2,1)` is the correct arithmetic for a pencil through `Q_∞` and is not a competitor on the vertical pencil. The three constraints alone do not kill `(2,1)`; the geometric pencil-identification does.

## 6. Sanity: ROW-KILL chain on the known-good (4,2) case

The coordinator (`126c2d29` §2) records that the `(4,2)` analogue of the fixed-tuple problem collapsed to `S_3` and is promoted, and that `(4,2)` nodal is closed. The ROW-KILL chain of charged torus-check §8 is:

1. Geometry: irreducible sextic, affine `3A_1`, infinity `A_{14}`.
2. Theorem NO-TORUS: not of `(2,3)`-torus type.
3. Resolvent: an `S_4` transposition representation yields a surjective `S_3` transposition representation `ψ`.
4. INF-TRIVIAL: involution meridians force `ψ(γ_∞)=1`.
5. Sh12 Corollary 0.6 (fetched): a normal triple cover of `P^2` with `deg Δ_π=6` exists iff the branch divisor is of `(2,3)`-torus type, contradicting 2.

Apply the *shape* of this chain, not the sextic-specific geometry, to a residual nodal `(4,2)` curve `D_4` of degree 4.

**Step 1 fails to produce a sextic.** The object is a quartic. There is no `(2,3)`-torus identity `G_2^3+G_3^2` of degree 6 to test, so step 2 is vacuous rather than false. (A quartic may or may not be of some other "torus" shape; that is a different identity and is not NO-TORUS.)

**Step 5 is degree-sensitive.** Sh12 Corollary 0.6 quantifies over `deg Δ=6`. Sh12's introduction lists the solved cases `(deg S_π, deg T_π) ∈ {(2,1),(2,2),(4,0),(4,1)}` plus `T_π=0` with `deg S_π=6`. A triple cover of `P^2` branched along a quartic (`deg Δ=4`, type `(4,0)`) is among the *existing* cases, not among the forbidden ones. If a fold analogue of INF-TRIVIAL still forces `ψ(γ_∞)=1` for `(4,2)` — e.g. if `x=r(t)^2` with `deg r=2`, giving two disjoint half-twists over `x=0` and `γ_∞` a product of two squares of involutions — then `ψ` extends to `P^2` with branch divisor of degree 4, which Sh12 does not prohibit. The `S_3` quotient is allowed to exist. If the fold geometry is absent, INF-TRIVIAL's proof simply does not run, and the chain does not fire either.

**No false negative.** The two load-bearing inputs of ROW-KILL that could have killed an `S_3` cover (NO-TORUS for sextics, and Sh12 for degree 6) both require `deg=6`. On `(4,2)` they are inapplicable, the chain does not produce a contradiction, and the promoted `S_3` collapse is compatible with the machinery. The chain is not a general "no `S_3` cover of any polynomial complement" argument; it is a degree-6 classification argument.

A secondary check of the RH arithmetic: `d=2g_L+c(Π)+2` at `d=4` gives `2=2g_L+c(Π)`. The pairs `(c,g_L)=(2,0)` and `(0,1)` are the numerical options; `(4,0)` would require `d=6`. An `S_3` cover of a quartic with `Π=e` would have `c=3` in `S_3` (three 1-cycles? identity in `S_3` has `c=3`), and the D1-DEGREE formula as written is for an `S_4` 4-cover (`c` counted in `{1,2,3,4}`). The formula is cover-degree-specific; applying it unchanged at `d=4` with `S_4`-cycle counts is not the `(4,2)` situation. No contradiction arises.

### Verdict

**HOLDS.** The ROW-KILL shape applied to the known-good `(4,2)` case does not fire and does not contradict the promoted `S_3` collapse. The kill is confined to degree 6 by Sh12 Corollary 0.6 and by the torus identity of degree 6.

## 7. Verdict table and residual OPEN items

| # | target | verdict | one-line |
|---|---|---|---|
| 1 | implicit sextic at `(0,1)` and `(1,1)` | **BROKEN** | Degree 6 and `A_{14}` hold at both; three ordinary nodes hold at `(1,1)` and fail at `(0,1)` (`D_4` at `(1/9,0)`). Missing excluded modulus: `j=0`. |
| 2 | `A^3−B^2=λ F` at both points | **HOLDS** | No solution at either point. At `(1,1)` by triangular `t`-degrees plus Lemma 2.2; at `(0,1)` by leading-form elimination (`y^6` vs `x^4`). |
| 3 | conic-criterion count | **HOLDS** | Five independent conditions at `A_{14}` on a 6-dimensional space; unique candidate `Z^2`, excluded. Nodes are not imposed; adding them empties the system. |
| 4 | discriminant census at `(0,1)` | **BROKEN** | `|Σ_x|=3` not 6, `|Σ_u|=5` not 11. Three disjoint `x=0` half-twists hold, so INF-TRIVIAL's actual feed is intact. |
| 5 | RH identity and `(2,1)` vs `(4,0)` | **HOLDS** | Both pairs satisfy RH, `d=2g_L+c+2`, and `χ_c(Y)=3`. The `x`-pencil with `Q'∉C` selects `(4,0)`; `(2,1)` belongs to the pencil through `Q_∞`. |
| 6 | ROW-KILL on known-good `(4,2)` | **HOLDS** | Sh12 and NO-TORUS are degree-6; the chain does not fire on a quartic and does not contradict the promoted `S_3` collapse. |

**What is confirmed.** Theorem NO-TORUS at the actual three-node member `(1,1)`, and also at the missed `D_4` member `(0,1)`. The conic linear algebra of charged §2.1. The three disjoint half-twists over `x=0`. The RH identity. Degree-sensitivity of ROW-KILL.

**What is broken.** The charged three-ordinary-node stratum omits `j=0`. At `j=0` the affine type is `D_4` of `δ=3`, the discriminant collapses, and Lemma 2.2 is unavailable. Charged `zvk-u6` §3.5 treats `(0,1)` as a regular member. Theorem ROW-NF's `δ_aff=3` remains true; its reading as "three singular pairs ⇒ three nodes" does not, because distinct plus-pairs may share an image point.

**What remains OPEN (not filled by cap or analogy).**

- `OPEN[STRATUM-J=0]`: the equisingular type, fundamental group, and torus-check applicability on `j=0` are not the three-node residual. NO-TORUS still holds there by §2.2, but ROW-KILL as assembled in charged §8 uses the three-node geometry in steps 1 and 4's braid description.
- `OPEN[c(Π)-PENCIL]`: the numerical conflict `(2,1)` vs `(4,0)` is a pencil mismatch, not an inconsistency of RH. Coordinator adjudication is still needed if FIXED-TUPLE's `(2,1)` is consumed elsewhere as an `x`-projection datum.
- ROW-NF and Theorem FOLD remain `PROVISIONAL` as in the charge; this arm does not upgrade them. Theorem ROW-KILL inherits that scope. The `(8,4)` transfer is not claimed.

Sh12 Corollary 0.6 and Oka05 Proposition 2 / Lemma 3 were fetched, hashed, and quoted from the PDFs; their proofs were not re-verified. No exit price is asserted.

<!-- BODY-END -->
