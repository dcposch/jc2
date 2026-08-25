# Double-`B` leaf: algebraicity of `p` over characteristic zero

Date: `2026-08-24`  
Researcher: Grok 4.6 (xAI), independent exact-algebra lane  
Repo: `/Users/dc/code/math/jc2`  
Git HEAD: `2e6104a417cfe15a93a901aa0a9129094a2ae11b`  
Scratch: `/tmp/doubleb_src/` only  
No producer, case, canonical, coordination, prompt, log, run, or review file was edited.

**Status: `INCONCLUSIVE` for the claim that the elimination ideal in `Q[p]` is nonzero.**

What is proved over `Q`, what is only modular, and why that split matters for the proposed terminal kill are separated below. The modular picture is consistent and specific; it is not a characteristic-zero Groebner certificate.

---

## 0. Claim, leaf, and source

The target is the normalized maximum-12 `(9,12)` order-three double-`B` coefficient fibre

```text
k = mu = 0,   nu = 1,
r1 = r2 = r3 = r4 = r5 = r7 = 0,   r6 = 1,
3*p + 10*r8 = 0.
```

The last equation is `s=0` on the reviewed unordered critical-value stratifier: after `nu=1` one has `B=54(z^2-s)` with `s=-(a7+10*r8)/9` and `p=a7/3`, so `3*p+10*r8=0` is the double root of the leaf quadratic. Source rows are the eight transverse tails `r1,...,r8` of the exact order-three fibre compiler, specialized at `k=0`. They were reconstructed from that compiler, not from modular probe output.

The question is whether `I ∩ Q[p]` is nonzero, where `I` is the ideal of the displayed leaf in `Q[x0,...,x5,q,p]`. If a nonzero `P(p)` lies in `I`, then on every actual function-field trajectory `p` is algebraic over the constant field `C`, hence constant, hence `r8=-3p/10` is constant, hence `r8'=0`, contradicting the reviewed terminal row `r8'=j/(9u)` with `j≠0`.

Discovery evidence, used only as a routing hint: modulo `1000003` the full double-`B` ideal has dimension one and degree five; the `p=0` slice has the same dimension and degree with free `q`; the `p=1` slice is empty.

---

## 1. Inputs actually consumed

| Artifact | SHA-256 | Role |
|---|---|---|
| `cases/max12_912_order3_fibre_20260824/order3_fibre.py` | `a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf` | exact source of `r1,...,r8`; pinned by the unfrozen probes |
| `xmodel/max12-912-order3-critical-value-norm-20260824.md` | `7339478798e00894c7b975c60aca821ec7ff2da383ffe5165a93cfa361bb6cb6` | confirmed root-free pair-norm; double-`B` is the retained `s=0` stratum |
| `xmodel/max12-912-order3-critical-value-norm-review-grok-20260824.md` | `b6ae9516430073e177a5174684109b437ab278fa04dd066686c58af57715588e` | different-model `CONFIRMED` of that stratifier |
| `xmodel/max12-912-order3-nu-belyi-collision-boundary-20260824.md` | `9b717712e59b70a6b06303f745a9c70b2152e3f624d03162741e3338ef1168b7` | terminal row `r8'=j/(9u)` and the identity `B=54*nu*z^2+18*nu*p+60*r8` |
| `xmodel/max12-912-order3-spectral-wronskian-ladder-20260824.md` | `6a7715597126b2b655bf0f8cc955597c093420132b240c1d31780f6221ef3a05` | ladder identity; not used as a component theorem |

The fibre compiler is not a reviewed theorem. Tails used as evidence were rebuilt by calling `compile_fibre()` and substituting `k=0`. The unfrozen scripts under `cases/max12_912_order3_nu1_probe_20260824/` were read as support-learning templates; their finite-field output was not treated as a characteristic-zero certificate. Parent hash check inside those scripts matches the fibre compiler bytes above.

Environment: CPython 3.14.6, Singular 4.4.1, msolve 0.10.1, python-flint. Characteristic not `2` or `3`.

---

## 2. Reconstructed source rows

After `k=0` the transverse tails live in `Q[x0,...,x5,p,q]`. They are weighted homogeneous for

```text
wt(x_i) = 9-i,   wt(p) = 2,   wt(q) = 3,   wt(r_ell) = 12+ell,
```

with no linear part in `(x0,...,x5)` (the normal linear map of the compiler is `(2/3)k` and vanishes at `k=0`). Term counts and total-degree maxima:

| row | terms | max total deg | x-degree support | weight |
|---|---:|---:|---|---:|
| `r1` | 10 | 4 | 2,3 | 13 |
| `r2` | 16 | 5 | 2,3 | 14 |
| `r3` | 20 | 5 | 2,3 | 15 |
| `r4` | 29 | 6 | 2,3,4 | 16 |
| `r5` | 35 | 6 | 2,3,4 | 17 |
| `r6` | 48 | 7 | 2,3,4 | 18 |
| `r7` | 57 | 7 | 2,3,4 | 19 |
| `r8` | 73 | 8 | 2,3,4,5 | 20 |

Denominators are powers of three. The normalized leaf is `r1=...=r5=r7=0`, `r6-1=0`, `10*r8+3*p=0`. The equation `r6=1` is not weighted homogeneous; keeping `nu` with `r6-nu` restores homogeneity, which is why the exceptional `p`-minpoly below is a polynomial in `p^9`.

The first row, as an exact integer multiple, is

```text
27*r1 = 12*x0*x5 + 12*x1*x4 + 12*x2*x3 - 24*x2*x5*p - 24*x3*x4*p
        - 24*x3*x5*q - 12*x4^2*q - 4*x4*x5^2 + 36*x4*x5*p^2 + 36*x5^2*p*q.
```

---

## 3. Characteristic-zero `p=0` slice — proved

Set `p=0`. Then `3*p+10*r8=0` is `r8=0`. The seven remaining equations live in `Q[x0,...,x5,q]`.

### 3.1 Two explicit families

**Family A.** Restrict to `x1=x2=x3=x4=x5=0`. Every reconstructed tail vanishes identically except `r6=2/9*x0^2`. The double-`B` generator collapses to `3*p`. The system is therefore

```text
p = 0,   x1 = x2 = x3 = x4 = x5 = 0,   2*x0^2 - 9 = 0,
```

with `q` free. This is a reduced affine curve of dimension one and degree two, defined over `Q(sqrt(2))`.

**Family B.** Restrict to `x1=x2=x4=x5=0` and substitute `x0=x3*q`. The reconstructed tails become

```text
r1 = r2 = r3 = r4 = r5 = r7 = r8 = 0,   r6 = -4/81*x3^3.
```

Imposing `r6=1` and `p=0` gives

```text
p = 0,   x1 = x2 = x4 = x5 = 0,   4*x3^3 + 81 = 0,   x0 = x3*q,
```

with `q` free. This is a reduced affine curve of dimension one and degree three, defined over `Q(∛-81/4)`. The extra Groebner elements `4*x0*x3^2+81*q`, `4*x0^2*x3+81*q^2`, `4*x0^3+81*q^3` are consequences of those two equations.

Both families were checked by substituting the reconstructed `k=0` tails, not by trusting a primary decomposition.

### 3.2 Completeness of the `p=0` slice over `Q`

Singular `std` plus `primdecGTZ` over `Q` on the integer-cleared `p=0` system returns dimension one, degree five, and exactly two primary components. After taking standard bases of the printed radicals one has

```text
C1: dim 1, degree 2,   (x1, x2, x3, x4, x5, 2*x0^2-9)
C2: dim 1, degree 3,   (x1, x2, x4, x5, 4*x3^3+81, x0-x3*q)
```

matching Families A and B. The raw `primdec` `dim()` calls on non-standard bases printed a spurious dimension two for C2; that figure is discarded. Degrees `2+3=5` match the standard-basis multiplicity of the whole `p=0` slice. Component and radical degrees agree, so both components are reduced.

Thus, over characteristic zero, the `p=0` slice is a reduced curve of degree five with free `q`, and it is nonempty.

### 3.3 Actual trajectories on these components die

On both families `p=0` and `r8=0` identically. An actual Keller trajectory is a point of the coefficient fibre over the function field `L=C(x)(u)` with `u^3=h`. Algebraicity of `p` over `C` is automatic on these components because `p` is the constant `0`. Then `r8=-3p/10=0` is constant, so `r8'=0`. The reviewed terminal identity on this landing is `r8'=j/(9u)` with `j≠0`, equivalently `9*h*R'+6*h'*R=j` with `r8=u^2*R` and `R=0`. This is a contradiction.

So neither Family A nor Family B supports an actual `(9,12)` order-three Keller trajectory. That is a kill of the `p=0` reduced support of the double-`B` leaf. It is not yet a kill of every double-`B` point.

---

## 4. Nonzero-`p` locus — modular, not characteristic zero

### 4.1 Saturation `I + (p*ip-1)`

At every prime tested in `{32003, 65521, 100003, 1000003, 1048573, 104729, 2147483629, 1184018179}` the saturated system

```text
r1 = r2 = r3 = r4 = r5 = r7 = 0,   r6 = 1,   10*r8+3*p = 0,   p*ip-1 = 0
```

is zero-dimensional of degree `1188` (Singular `slimgb`, both `dp` and the product order `(dp(8),dp(1))`). The product-order basis has ten elements.

This contradicts a naive reading of msolve over `Q` on the same cleared-integer input, which printed `[-1]` (no solution) after a single prime `1184018179`. At that same prime Singular returns dimension zero and degree `1188`. Finite-character msolve on the same input reports `[1, 9, -1, []]` (positive-dimensional), i.e. a genericity/staircase failure, not emptiness. msolve's characteristic-zero unsat is therefore not used.

### 4.2 Elimination polynomial in `p`, modulo several primes

In the product order `(x0,...,x5,q,ip | p)` the first Groebner element is univariate in `p` and is a polynomial in `t=p^9` of degree `70`:

```text
P_sat(p) = p^{630} + c_{69} p^{621} + c_{68} p^{612} + ... + c_1 p^9 + c_0.
```

Seventy-one terms, exponents `9k` for `k=0,...,70`, leading coefficient `1`, at each of `32003`, `65521`, `100003`, `104729`. The constant term is nonzero (e.g. `-22193` modulo `65521`), so these points have `p≠0`. The shape `P_sat ∈ F[p^9]` is the `nu=1` slice of a weighted-homogeneous relation of weight `18*70` in `(p,nu)`.

The rest of that ten-element basis is triangular: `x1,x3,x5` are polynomials in `p`; `x0,x2,x4` are `q` times polynomials in `p`; `q^2` is a polynomial in `p` of weight six; `ip` is a polynomial in `p`. Degree `1188` is compatible with a degree-`630` minpoly in `p` together with a quadratic in `q` and the auxiliary relation `q*p^{558}=...`.

Integer `p`-slices `{1,2,3,4,5,7,9,10,16,27,81,-1}` are all empty modulo `65521`, matching `P_sat(1)≠0` and the original `p=1` emptiness modulo `1000003`.

Four-prime Farey reconstruction of the seventy coefficients of `P_sat` as a polynomial in `t=p^9` fails a leave-one-out test: the rational heights exceed a `65`-bit modulus. No characteristic-zero lift of `P_sat` is claimed.

### 4.3 Why this does not yet certify `I ∩ Q[p] ≠ (0)`

If the degree-`1188` locus spreads out from a zero-dimensional `Q`-scheme, then the projection of `V(I)` to the `p`-line is `{0}` union a finite nonempty set of roots of a lift of `P_sat`, so `I ∩ Q[p] = (p^k * P_Q)` is nonzero. If that locus is a modular ghost and the only characteristic-zero components are Families A and B, then `I ∩ Q[p] = (p^k)` is still nonzero. The unique way for the elimination ideal to vanish is a dimension-one component over `Q` on which `p` is nonconstant, hence a dominant projection to `A^1`.

A Groebner basis of the unsaturated ideal over `Q` would decide this: it would have dimension one and degree five if and only if every top-dimensional component lies in `p=0`, and it would display `p^k` or `p^k P_Q` as a univariate. That computation was started (`std` in `dp` over `Q`) and had not finished in a short window; it is the size of the degree-`1188` exceptional scheme that makes the unsaturated basis large, whereas the `p=0` slice (those points removed) is immediate.

Modular dimension/degree matching at `1000003` (`dim I = dim I|_{p=0} = 1`, `deg = 5`) is the expected reduction of a `Q`-scheme with top-dimensional part equal to Families A and B. By the launch constraint, that matching is support, not a characteristic-zero certificate.

python-flint `buchberger_naive` over `Z` on the `p=1` slice and on the saturation, with limits up to basis length `300`, did not reach a Groebner basis and produced no constant.

---

## 5. What a nonzero `P(p)` would do to a trajectory

Suppose `P(p) ∈ I` with `P ≠ 0`. On any actual trajectory the coordinates `(x0,...,x5,q,p)` lie in `L`, so `P(p)=0` in `L`. The constant field of `L` is `C`, algebraically closed, so `p ∈ C`. The double-`B` equation then forces `r8=-3p/10 ∈ C`. Differentiating a constant gives `r8'=0`. The reviewed identity `r8'=j/(9u)` with `j≠0` is then impossible.

This kill applies equally to:

- Families A and B (already `p=0`, proved over `Q`);
- any lifted zero-dimensional `p≠0` point (a constant tuple in a finite extension of `C`);
- any component on which `p` is a constant algebraic number.

It does **not** apply to a dimension-one component on which `p` is a nonconstant rational function. That is exactly the case `I ∩ Q[p]=(0)`. No such component was constructed. No characteristic-zero Groebner basis has ruled it out.

If `P` exists, `r8` is a constant, so the identity `9*r8'=j/u` in the launch prompt is the same obstruction as `r8'=j/(9u)`: both say that a nonzero multiple of `j/u` equals a derivative of `r8`.

---

## 6. Embedded, nilpotent, and exceptional structure

| Piece | Over `Q` | Modular |
|---|---|---|
| Family A, `p=0` | proved, reduced, dim 1, deg 2, `q` free | present |
| Family B, `p=0` | proved, reduced, dim 1, deg 3, `q` free | present |
| Nilpotents along `p=0` | not seen: component degrees equal radical degrees | unsaturated `deg=5` equals the reduced `p=0` degree |
| Zero-dimensional `p≠0` | not constructed; not excluded by a `Q`-basis | dim 0, deg 1188, minpoly of degree `630` in `p` and `70` in `p^9` |
| Dimension-one `p` nonconstant | not constructed | invisible in top dimension/degree at `1000003` |

The `p=1` emptiness, over `Q` via msolve and over several `F_p` via Singular, only says that `1` is not a root of a putative `P`. It does not by itself empty every nonzero `p`.

---

## 7. Smallest missing certificate, and the next gate

The smallest source-honest characteristic-zero certificate still missing is one of:

1. A Groebner or membership certificate over `Q` that a nonzero polynomial in `p` lies in `I` (the unsaturated product-order basis, or a lift of `P_sat(p)` with a membership combination);
2. The weighted-homogeneous elimination in `(p,nu,r8)` over `Q`, followed by the slice `nu=1`, `3*nu*p+10*r8=0`, which should produce a polynomial in `p^9` of degree `70` if the modular shape is honest;
3. An explicit invariant identity forcing `p` algebraic, e.g. a combination of the eight reconstructed rows equal to `p^k` or to a lift of `P_sat`.

The right next coordinate/differential gate if that certificate is obtained is the terminal row already written: constant `p` implies constant `r8=-3p/10`, which contradicts `r8'=j/(9u)`. If instead a characteristic-zero point with nonconstant `p` is found, that point is the smallest counterexample to the proposed kill, and the next gate is whatever differential identity still moves on that curve (most likely a genuine `r8'` computation along the family, or a Hurwitz/passport constraint on the double critical point off `W=0`).

Reproducible reconstructions used here, all from the pinned fibre compiler with scratch in `/tmp`:

```sh
# p=0 primdec over Q, and std of the two radicals
singular -q /tmp/doubleb_src/p0_primdec.sing
singular -q /tmp/doubleb_src/p0_dims.sing

# saturated product-order basis modulo 65521 (univariate P of degree 630)
singular -q /tmp/doubleb_src/printgb_65521.sing
```

---

## 8. Scope (not enlarged)

Proved only: the reduced `p=0` support of the displayed double-`B` coefficient fibre over `Q`, as two explicit families of dimensions/degrees `1/2` and `1/3`, and the impossibility of an actual Keller trajectory on those families via `r8'=0`. Not proved: nonzeroness of `I ∩ Q[p]`; emptiness of the nonzero-`p` locus over `Q`; a lift of the modular degree-`70` polynomial in `p^9`; weighted-homogeneous elimination over `Q`; other loads; `mu≠0`; `k≠0`; the order-one core; `(8,12)`; residual leaves of the pair-norm (`W0≠0` double-`B` four-point family is exactly this leaf, not emptied); Taylor boundaries; maximum-twelve automorphy; a counterexample; or JC2.

---

## Research status

`INCONCLUSIVE`

**Strict scope.** On the normalized `(9,12)` order-three double-`B` leaf `k=mu=0`, `nu=1`, `r1=r2=r3=r4=r5=r7=0`, `r6=1`, `3*p+10*r8=0`, with source rows reconstructed from `cases/max12_912_order3_fibre_20260824/order3_fibre.py` at `k=0`: the elimination ideal `I ∩ Q[p]` has not been proved nonzero and has not been proved zero. Characteristic zero supplies a reduced `p=0` curve of degree five, which cannot be an actual trajectory. Finite-field Groebner bases supply a complementary zero-dimensional `p≠0` scheme of degree `1188` whose `p`-minpoly is a degree-`70` polynomial in `p^9`; that scheme and that polynomial have not been lifted to `Q`.
