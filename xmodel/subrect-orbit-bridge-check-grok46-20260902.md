# SUBRECT-ORBIT-BRIDGE check — Grok 4.6, 2026-09-02

Lane: `SUBRECT-ORBIT-BRIDGE-CHECK`. Different-model desk check of the GPT-5.5 closure.
Scope: frozen inputs, local `refs/`, desk algebra. No web as a substitute for the book; no canonical ledger edit; no `jc2-lean`. No exit-price assertion, so no `charge_basis` line.

## 0. Custody

Frozen charged copies were hashed with `shasum -a 256` before reading. All three match the charge:

```text
75ee84f89fdb5abcc6e8f51654c618de469ae06b32d7d7a1911c5f9d6e9602c7  .../inputs/subrect-orbit-bridge-gpt55-20260902.md
b1e09351164c134ec8aa74a7b905678e70021155b23add5bec9994e9f1268ac1  .../inputs/minimal-keller-shape-review-gpt55-20260902.md
bf1d428c7ddc03ab002410174b995cdd01e8a3c76c52475b03faf959b33da2ca  .../inputs/integration14-coordinator-fable51-20260902.md
```

Primary local reference, hashed independently:

```text
8b4267512c438c7ceda7e30cb63c225a554cf0d2195dc6325e9d1e42ab520c60  refs/guccione_valqui2017_ja471_shape_counterexamples.pdf
```

GGV = J. A. Guccione, J. J. Guccione, C. Valqui, J. Algebra 471 (2017); local file is arXiv:1401.1784v3, 71 PDF pages. Proposition 4.7, Definition 4.3, Theorem 2.6(4), Proposition 5.20 and Corollary 5.21 were read from that PDF (pages 8, 15–18, 29). Auxiliary extract `box/mks-drivers-20260902/gv.txt` hashes to `449d8028da79c7f2ae9eff9161553fcc35f75a48989f169c5d9ef54edf88773f` and matches the PDF on those pages.

Van den Essen, *Polynomial Automorphisms and the Jacobian Conjecture*, Progress in Mathematics 190, Birkhäuser, 2000, is **ABSENT** from `refs/`. Exact citation: Corollary 10.2.21 (GGV's [14], MR1790619). The locally verified statement is GGV's displayed invocation (4.6) on PDF p. 17.

Shorthand: **BR** = charged bridge report; **REV** = charged shape review; **I14** = charged integration #14.

## 1. Verdict

**CONFIRMED**, with two wording repairs that do not change the bounded quantity.

`OPEN[SUBRECT-ORBIT-BRIDGE]` closes **YES** in the campaign meaning: if `F_min=(P,Q)` is a Jacobian counterexample minimizing `D=max(deg P, deg Q)` in its `Aut(C^2)×Aut(C^2)` orbit, then a source automorphism supplied by van den Essen Cor. 10.2.21 (as consumed at GGV (4.6)) may be taken affine of degree one, the image is GGV's standard subrectangular `(m,n)`-pair, both total degrees are preserved, and the top form of the max-degree coordinate is a monomial `c x^u y^v` with `u,v≥1`. Hence `nu(F_min)=2`. Integration #14's free-`E_0` reading and the vacuity of CH2 are then unconditional at every geometric degree `N`, in this degree-minimal scope.

Wording repairs, both already correct in BR §3 and only loose in BR §1:

1. The degree-lowering map is the subrectangularising source automorphism `φ` itself, not `φ^{-1}`. GGV computes `deg P = v_{1,1}(R)(a+kb) > a+b = deg φ(P)` when `ψ=φ^{-1}` is nonlinear; so `φ` strictly lowers `D` and `ψ` raises `D` on the rectangle.
2. Definition 4.3 includes `m,n>1`, which uses minimality. The monomial / `nu=2` conclusion uses only the rectangle with `a,b≥1`, not global `B` and not `m,n>1`.

The short argument "linear change plus (LF) monomializes any `H` with at least two roots" is invalid, as BR separates: `GL(2)` preserves the number of reduced roots in `P^1` and cannot send three or more roots to `x^u y^v`.

No replacement OPEN. Bounded quantity: `nu(F_min)=2`.

## 2. Van den Essen Corollary 10.2.21

**Citation.** Arno van den Essen, *Polynomial Automorphisms and the Jacobian Conjecture*, Progr. Math. 190, Birkhäuser, 2000, Corollary 10.2.21. GGV bibliography item [14]. Book not in `refs/`; not re-OCR'd here.

**Locally verified consumption** (GGV PDF p. 17, displayed (4.6)):

> Since `(P,Q)` is a counterexample to JC, by [14, Corollary 10.2.21] there exists an automorphism `φ` of `L` and integers `1≤a≤b` such that
> `(a,b) ∈ Supp(φ(P)) ⊆ {(i,j): 0≤i≤a, 0≤j≤b}`.

Here `L=K[x,y]`. This is the subrectangular support: axis rectangle with occupied northeast corner, oriented `a≤b`. The corollary as consumed does **not** claim `v_{1,1}(φ(P))=v_{1,1}(P)`. Degree preservation is GGV's subsequent argument, not vdE.

**Hypotheses reconstructed from that invocation and the standard reduction spine (GGV's use, not a substitute book quotation).** The input is a single polynomial, not a pair. The alternative branch is that the polynomial is a coordinate; for a Jacobian counterexample neither coordinate is a coordinate, so that branch is excluded. In dimension two the supplying map may be taken in `Aut(L)` (Jung–van der Kulk: tame `T(K,2)` equals `Aut(K[x,y])`). Variable interchange, if needed to arrange `a≤b`, is linear. GGV Proposition 4.1 independently forbids a Jacobian counterexample from being of the form `μx+f(y)` or `μy+f(x)`, so the occupied corner cannot lie on an axis: `a≥1` and `b≥1`.

**Degrees.** The reduction theorem behind the corollary (vdE Thm 10.2.18, as GGV's [14] is used) decreases `δ=deg_x+deg_y` along a negative-slope Newton edge by a tame (typically triangular) factor. That `δ`-drop is **not** `v_{1,1}`-preservation and is not used in the bridge. Intermediate factors in a tame word may be nonlinear; only the composite that GGV names `φ` is forced affine below.

**`a<b`.** Not in (4.6). GGV gets `a<b` from Theorem 2.6(4): `st_{ρ,σ}(P) ≁ (1,1) ≁ en_{ρ,σ}(P)` for a Jacobian pair with `v_{ρ,σ}(P)>0` and `(ρ,σ)∈V_{>0}`. At `(1,1)` one has `st_{1,1}(φ(P))=(a,b)`, so `a≠b`; with `a≤b`, `a<b`. This is Jacobian, not global-`B`. (`a=b` would still give `nu=2`; `a<b` is for the `(m,n)`-pair sign `v_{1,-1}(en_{1,0})<0`.)

## 3. Affine-linearity under orbit degree-minimality

Jung–van der Kulk / GGV's citation of vdE Cor. 5.1.6(a) and Joseph: if `ψ∈Aut(L)`, `M=v_{1,1}(ψ(x))`, `N=v_{1,1}(ψ(y))`, then `M|N` or `N|M`. If `M=N=1`, both coordinates have total degree 1, so `ψ` (and `φ=ψ^{-1}`) is affine.

**GGV inverse computation, without global `B`.** Let `P̄=φ(P)` be subrectangular as in (4.6), so `ℓ_{1,1}(P̄)=λ_P x^a y^b` with `a,b≥1`, and every other support point has strictly smaller `(1,1)`-weight. Let `ψ=φ^{-1}`. If `M|N` and `N>1`, Proposition 1.13 plus Proposition 2.1 give `ℓ_{1,1}(ψ(y))=λ R^k` with `R=ℓ_{1,1}(ψ(x))` and `k≥1`. Unique top monomial, no cancellation:

```text
v_{1,1}(ψ(x^i y^j)) = v_{1,1}(R)(i + k j)  <  v_{1,1}(R)(a + k b)
```

for all `(i,j)∈Supp(P̄)\{(a,b)}`, because `i≤a`, `j≤b`, not both equal, and `k≥1`. Hence

```text
deg P = v_{1,1}(ψ(P̄)) = v_{1,1}(R)(a + k b).
```

The same rectangle for `Q̄` is GGV (4.12), from Proposition 4.1 and Remark 3.1 (Jacobian, **before** the gcd/`B` comparison): `deg Q = v_{1,1}(R)(n ā + k n b̄)`. Since `ā,b̄>0` and either `k>1` or `v_{1,1}(R)>1`,

```text
v_{1,1}(R)(ā + k b̄) > ā + b̄,
```

so `deg P > deg P̄` and `deg Q > deg Q̄`. Thus `max(deg φ(P), deg φ(Q)) < D`. This pair is in the source orbit, contradicting Aut×Aut (even source-orbit) degree-minimality. The symmetric case `N|M` with `M>1` is the same with `(x,y)` swapped. Therefore `M=N=1`: `φ` is affine. Affine source maps preserve each total degree, so the gauge preserves both coordinate degrees.

Global `B` is used in GGV only to force the same inequality via `gcd` comparison. Orbit `D`-minimality replaces it directly, and is stronger: it yields affinity, not merely `v_{1,1}`-preservation.

**Could a nonlinear automorphism preserve `D` while changing shape?** Yes, off the rectangle, by cancellation. No, when the image has a unique occupied NE corner with `a,b≥1`. That is the only map vdE supplies.

### Both-sides triangular bookkeeping

Write `E_k:(x,y)↦(x, y+c x^k)`, `k≥2`, `c≠0`; inverse `(x, y-c x^k)`.

**Source** (algebra action / right composition): `P ↦ P(x, y+c x^k)`. Expand `P=∑_{j=0}^d p_j(x) y^j`. Absent cancellation, the `j`-summand has `(1,1)`-degree `deg p_j + k j`, against original `deg p_j + j`. Every `j≥1` term strictly rises. The new degree is `≥` the old, with equality only if `d=0` or top pieces of distinct `j` collide and cancel. Cancellation is exactly the degree-dropping inverse shear: `(y+x^k)∘E_k^{-1}=y` sends `D=k` to `1`. On a unique top `x^a y^b` with `b≥1` there is **no** such collision: the image of the NE monomial is the unique top, of degree `a+kb>a+b`. Desk: `x^2 y^3` has `D=5`, `nu=2`; after `E_2` one gets `D=8=2+3·2`, `nu=1`; the inverse shear recovers `D=5`, `nu=2`. Likewise `xy` after `E_2` is `xy+x^3`, `D:2→3`, `nu:2→1`.

**Target** (left composition): `(P,Q)↦(P, Q+c P^k)`. Then `deg(Q+c P^k)=max(deg Q, k deg P)` unless `ℓ(Q)+c ℓ(P)^k=0`. This raises `D` unless the (LF) divisibility case cancels the top of `Q`. That cancellation is `(MIN)`: at a degree-minimal counterexample one cannot have `d=1` or `d=e`, else a target elementary or target linear combination lowers `D`. Desk: on `(x,xy)`, target `Q+P^3` sends `xy` to `xy+x^3`, `D:2→3`, `nu:2→1`.

Affine source: `P(ax+by+c, dx+ey+f)` with linear part in `GL(2)` preserves total degree and the number of reduced roots of a binary form. Affine target, under `(MIN)` (`d≠e`), preserves the max-degree leading form.

## 4. GGV Proposition 4.7 / Definition 4.3 and `nu=2`

**Definition 4.3** (PDF p. 15). Coprime `m,n>1`. A Jacobian pair is an `(m,n)`-pair if `v_{1,1}(P)/v_{1,1}(Q)=v_{1,0}(P)/v_{1,0}(Q)=m/n` and `v_{1,-1}(en_{1,0}(P))<0`. It is **standard** if additionally `P,Q∈L^{(1)}` and `v_{1,-1}(st_{1,0}(P))<0`.

**Proposition 4.7** (PDF pp. 16–18), as printed, assumes a GGV-minimal pair (global `B`) and produces an `(m,n)`-pair with both `v_{1,1}` preserved and successor inequalities (4.5). The proof uses global `B` only from (4.10) onward (the inverse-degree gcd comparison) and at the last line (`m,n>1` via Remark 4.2).

**What `nu=2` actually uses.** From (4.6) alone: the unique point of the rectangle of total degree `a+b` is `(a,b)`, so `ℓ_{1,1}(P̄)=λ_P x^a y^b` (GGV p. 18, before `B`). With `a,b≥1` this is a monomial with two distinct reduced roots. Jacobian `(LF)` (GGV Prop. 2.1 at `(1,1)`, already promoted in I14) writes `ℓ(P)=α H^d`, `ℓ(Q)=β H^e`, `gcd(d,e)=1`, so `H=c' x^u y^v` with `u=a/d`, `v=b/d` and `u,v≥1`. Thus `nu=2` on the rectangle. Theorem 2.6(4), Proposition 4.1, and the `Q`-rectangle (4.12) do not use `B`. Definition 4.3's `m,n>1` is not an input to this monomial count.

At `F_min`, §3 makes `φ` affine, so the reduced root count is the same before the gauge: `nu(F_min)=2`, not merely "`nu=2` after some (possibly nonlinear) gauge". Then `m,n>1` follows from `(MIN)` (target elementary / linear combination), replacing Remark 4.2. Proposition 5.20 (PDF p. 29) standardizes any `(m,n)`-pair by `φ(x)=x`, `φ(y)=y+λ` or the identity, preserving `ℓ_{1,1}` and `en_{1,0}`. The extra successor maps GGV calls "well known" (Makar-Limanov / Lang) are absorbed into the same composite, which §3 already forces affine.

So every Aut×Aut `D`-minimal counterexample admits GGV's **standard** subrectangular gauge with both degrees preserved.

## 5. Controls

Exact arithmetic on supports and Jacobians (QQ coefficients). `nu` = number of distinct roots in `P^1` of the top form of the max-degree coordinate.

| map | `D` | top of max-deg | `nu` | Jac | note |
|---|---:|---|---:|---|---|
| `(x, y+x^k)`, `k=2,3,4` | `k` | `x^k` | 1 | `1` | auto; inverse `(x,y-x^k)` sends `D` to `1`; **not** orbit-minimal |
| `(x, xy)` | 2 | `xy` | 2 | `x` | not Keller; two-root shape |
| `(x, x^2 y^2)` | 4 | `x^2 y^2` | 2 | `2 x^2 y` | not Keller |
| `(x, xy(x-y))` | 3 | `x^2 y - x y^2` | 3 | degree 2 | not Keller; three roots |
| `(x,xy)` after source `E_2` | 3 | `x^3` | 1 | `x` | nonlinear source raises `D`, `nu:2→1` |
| inverse shear on that | 2 | `xy` | 2 | `x` | recovers; nonlinear inverse lowers `D` |
| `x^2 y^3` after `E_2` | 8 | `x^8` | 1 | — | formula `a+kb=2+6=8` |
| inverse shear | 5 | `x^2 y^3` | 2 | — | unique NE corner, no cancellation |
| linear `(x+y, x+2y)` | 1 | two distinct linears | 1 each | `1` | affine auto; `GL(2)` on a 3-root form keeps `nu=3` |
| 3-root `xy(x-y)` after `(x,y)↦(x+y,y)` or swap | 3 | two-term cubic | 3 | — | linear maps do not monomialize |

`(LF)` on `(x, y+x^k)`: `ℓ(P)=x=H^1`, `ℓ(Q)=x^k=H^k`, `gcd(1,k)=1`. This is the automorphism case `d=1`, excluded at `F_min` by `(MIN)`. For a Jacobian pair with vanishing top bracket, GGV Proposition 2.1 supplies a common homogeneous `R` with `ℓ(P)=λ_P R^m`, `ℓ(Q)=λ_Q R^n`. At degree-minimality, `m,n≥2` and unequal.

A two-root top form composed with an automorphism: `(x,xy)` after a linear source change `(x,y)↦(y,x)` remains `nu=2`; after nonlinear `E_2` it becomes `nu=1` and `D` rises. Affine preserves `nu`; nonlinear shears on a two-root rectangle raise `D` and can drop `nu` to 1. That is why a one-root representative in an Aut×Aut orbit is never `D`-minimal once a two-root (subrectangular) representative exists, which vdE supplies for every counterexample.

## 6. Promotion, AUDIT sentence, typed output

```text
ANSWER
  CONFIRMED YES: every Aut(C^2)×Aut(C^2) D-degree-minimal Jacobian
  counterexample admits GGV's degree-preserving standard subrectangular
  gauge, via an affine source automorphism.

BOUNDED QUANTITY
  nu(F_min) = 2.

PROMOTE
  Closure of OPEN[SUBRECT-ORBIT-BRIDGE]; I14's E_0-free conclusion and
  CH2 vacuity at every N, in Aut×Aut degree-minimal scope.

REPAIR (wording only)
  The subrectangularising map φ lowers D if nonlinear; ψ=φ^{-1} raises D
  on the rectangle. Do not say "the inverse lowers degree."
  nu=2 uses the rectangle with a,b≥1, not Def 4.3's m,n>1 and not B.

DO NOT PROMOTE
  "Linear change + (LF) monomializes any H with ≥2 roots."

GLOBAL-B
  Still the hypothesis of GGV Cor. 5.21 as printed, and of B≥16.
  Replaced here only for degree preservation / affinity of the
  subrectangulariser.

NO NEW OPEN
  Existing deeper-fork and satellite-mass OPENs untouched.
```

**AUDIT scope sentence (exact):**

OPEN[SUBRECT-ORBIT-BRIDGE] CLOSED YES: every Aut(C^2)×Aut(C^2) D-degree-minimal Jacobian counterexample admits a degree-preserving affine source change to GGV's standard subrectangular `(m,n)`-pair (van den Essen Cor. 10.2.21 as GGV (4.6), affinity by orbit D-minimality in place of global B), hence `nu(F_min)=2`, `E_0` is a free vertex of `T_+`, and CH2 is vacuous at every N in this scope; "linear change + (LF)" does not monomialize three or more roots.

## 7. FALLACY-v2

Flag/place/series: `nu` is the reduced root count of the top binary form on source `L_∞`; not satellite `nu_C` and not a Puiseux denominator. Carrier/attainment: non-Keller rows are shape controls, not counterexamples. Floor/attainment: Moh / `D_min≥102` are floors and are not used as kills here. No pole-identity, `sat()`, raw-remainder, variable-map, prime-label, or merge-free/M-descent argument. No new exit price.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14896`.
- Body SHA-256:
  `85f74332f22ba01a44dd876c583e726183644c58f036b3ad82c0ac5cc8c35f6e`.
- Frozen basis: `2ac86324b877714842fef09476c85fb83b0d5dee`.
