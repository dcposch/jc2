# Hostile review: D1 weighted-infinity exceptional support

| Field | Value |
|---|---|
| Target | `xmodel/max12-912-order3-d1-weighted-infinity-exceptional-support-20260825.md` |
| Target SHA-256 | `de7dd223d472508e057db72a5ec466c6362b762b4ba9a50f4ff823f585e774c7` |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation; the existing same-model review was not opened and is not evidence |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Missing hypothesis | none that affects the reduced-support claim |
| Method | source reading and hand derivation only; no CAS, solver, or compiler execution |

## Verdict

**CONFIRMED**

The eight-tail exceptional ideal `I_inf` of the cyclic-D1 coefficient-infinity Rees gate, evaluated on the `t=1` étale sheet above `s=1` and transported along its `μ_3` orbit, is the ordinary Faber system `k=0`, `r_1=⋯=r_8=0` for `g=F_{12}(f)`. Vanishing of those eight tails forces `g(z(w))=w^{12}+O(w^{-9})` in the exact inverse-root convention, hence `deg_z(g^3-f^4)≤15`. Mason–Stothers after dividing by `D=gcd(g^3,f^4)` is a strict inequality `36-e≤35-e` in characteristic zero, so `g^3=f^4`. Unique factorization and depression yield the graph of `C=z^3+pz+r`, `f=C^3`, `g=C^4`. The converse is the Faber identity `F_{12}(C^3)=C^4`. After saturating the irrelevant ideal, the reduced support is that graph; in weighted projective space it is `P(2,3)`, including both axes and the discriminant-zero locus. Rational poles on this reduced support have denominator `n=1` generically, `n∣2` on `r=0`, and `n∣3` on `p=0`. The numerator `m` is unbounded, and order-zero survival is not a deformation.

No identity failed. The argument classifies reduced exceptional support only.

## Strongest exact claim that survives

Over a characteristic-zero field, let `I_inf` be the eight-tail exceptional ideal of the cyclic-D1 Rees gate: `s=1`, finite-load coordinates `K=M=N=R=0`, and the eight homogenized descended Faber rows. On the `t=1` sheet (and therefore on its cube-root orbit) this is the ordinary system `r_1=⋯=r_8=0` for the depressed monic pair

```text
f=z^9+B_7 z^7+⋯+B_0,    g=F_{12}(f).
```

The reduced affine support of `I_inf`, equivalently of its saturation by `(B_0,…,B_7)`, is the image of

```text
C=z^3+p z+r,    f=C^3,    g=C^4,
```

i.e. the closed graph

```text
B_7=3p, B_6=3r, B_5=3p^2, B_4=6pr,
B_3=p^3+3r^2, B_2=3p^2 r, B_1=3pr^2, B_0=r^3.
```

In the weighted projective space of the `B_i` this is `P(2,3)`. For a rational coefficient pole of slope `m/n>3` in lowest terms, the only possible denominators on this reduced support are `1`; `1` or `2` on the axis `r=0`, `p≠0`; and `1` or `3` on the axis `p=0`, `r≠0`.

## Sharpest non-claim

This is a reduced-support theorem for one associated-graded divisor. It does not assert that the raw eight-tail ideal is radical, does not classify embedded or nilpotent thickness, does not lift a leading cubic along `τ`, does not bound the numerator `m`, does not exclude a D1 coefficient-infinity arc, does not produce a counterexample, and is not JC2.

---

## Sources actually used

Read in full, and used only as definitions, grading conventions, and character descent:

- `cases/max12_912_order3_fibre_20260824/order3_fibre.py`
- `cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/compile_gate_v2.py`
- `cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py`
- `cases/max12_912_order3_d1_weighted_infinity_20260825/PREREGISTRATION.md`
- `xmodel/max12-912-order3-d1-classical-degree-split-20260825.md`

The target hash was checked with `shasum -a 256` against the immutable value above. No producer review, no same-model review, no CAS, and no Python reconstruction was executed. Explicit tail polynomials are not needed: the argument uses the inverse-root convention and weighted homogeneity, not a Gröbner basis of `I_inf`.

---

## Bridge 1 — exceptional fibre is `k=0` and `r_1=⋯=r_8=0`

**CONFIRMED**

### Rees special fibre

Preregistration weights: `w(A_i)=9-i`, `w(k)=6`, `w(μ)=15`, `w(ν)=18`, `w(ρ)=20`, and row `R_ℓ` has weight `12+ℓ`. The Rees coordinates are

```text
B_i=e^{9-i} A_i,    K=e^6 k,    M=e^{15} μ,    N=e^{18} ν,    R=e^{20}.
```

Cyclic D1 takes `k∈L` finite, and a finite-load section takes `μ,ν` finite. On any chart with slope `p=m/n>3` one has `e=τ^m→0` as `τ→0`, so the special fibre is exactly `s=1`, `K=M=N=R=0`. Because `w(k)=6` is strictly positive, every monomial containing `k` (or `μ,ν`) is of strictly lower `A`-weight than a pure `A`-monomial of row-weight `12+ℓ`. Substituting the Rees scaling therefore sends those terms to positive powers of `K,M,N`. The associated-graded rows are the `k=μ=ν=0` tails in the `B_i`. In particular the associated-graded partner is `g=F_{12}(f)`, not `F_{12}(f)+k F_6(f)`.

The affine D1 chart is the descended row `R_8-1=0`. Homogenization replaces the constant `1` by `R`. On the special fibre `R=0`, so the eighth leading form is `r_8=0` rather than `r_8=1`. This is load-bearing: seven vanished tails would give only `deg W≤16` and Mason equality, not a contradiction.

### Character descent, `t=1` sheet, `μ_3` orbit

The fibre compiler assigns `σ(z)=ζz`, hence `wt(a_i)≡-i\pmod{3}` and `wt(r_ℓ)≡ℓ\pmod{3}`. The D1 descent of the V2 gate is

```text
σ(u)=ζ u,    σ(t)=ζ^2 t,    a_i=t^{i mod 3} A_i(s),
```

with `t^3=s`. This matches: `(i\bmod 3)·wt(t)≡-i\pmod{3}` forces `wt(t)≡2`. The invariant row is `r_ℓ` divided by `t^{2ℓ\bmod 3}`, and the V2 quotient exponents `(0,2,1)` for `ℓ\bmod 3∈{0,1,2}` are exactly those. Every monomial of each tail is divisible in this character (the swapped-character negative is a compiler check, not used here). The descended rows are therefore polynomials in `(A_i,s,k,μ,ν)`, with nonnegative powers of `s`.

Above `s=1` the cover `T^3-s` is étale in characteristic zero: `3T^2≠0` on `T^3=1`. The three sheets are `t=1,ω,ω^2`. On the principal sheet `t=1` one has `a_i=A_i` and `t^{2ℓ\bmod 3}=1`, so the descended row at `s=1` is the original tail. On the other sheets `a_i=ω^{i\bmod 3}A_i` and `r_ℓ` picks up `ω^ℓ`. Vanishing is `μ_3`-equivariant, so the descended rows vanish if and only if the eight original tails vanish on the orbit.

The variable `s` has Rees weight `0`. Every monomial of a descended row has the same `(A,k)`-weight `12+ℓ`, so at a pole of slope `m/n` they all contribute to one leading form, and `s=1+τ^n→1` merely sums the `s`-graded pieces. The exceptional equations in `B`-space are therefore the ordinary tails of `F_{12}` at `s=1`.

Attack that failed: an infinite `k` would keep `K` possibly nonzero and would contaminate the associated graded by `F_6`. Cyclic D1 forbids it (`k∈L`). An infinite `μ` or `ν` would be a different load stratum (`M` or `N` nonzero). The theorem is the finite-load coefficient-infinity divisor named in the preregistration.

---

## Bridge 2 — eight vanished tails imply `deg_z(g^3-f^4)≤15`

**CONFIRMED**

### Convention and nonnegative Laurent part

The inverse root is the unique formal series `z(w)=w+O(w^{-1})` with `f(z(w))=w^9`. The independent reconstruction forbids a `w^0` term, but that is unnecessary for the degree claim below: any series `z=w+` (terms of order `≤0`) still has `[w^d]z^d=1`.

Write `f=z^9(1+U)` with `U∈z^{-2}k[z^{-1}]` (depression kills `z^{-1}`). The Faber polynomial `F_{12}(f)` is the nonnegative part, in `z`, of `z^{12}(1+U)^{4/3}`. Substituting the inverse root,

```text
z(w)^{12}\bigl(1+U(z(w))\bigr)^{4/3}
  = z(w)^{12}\bigl(w^9/z(w)^9\bigr)^{4/3}
  = w^{12},
```

principal branch at infinity. The discarded `z`-principal part is a series in `z^{-k}` for `k≥1`; each such term satisfies `z(w)^{-k}=w^{-k}+O(w^{-k-2})`, hence contributes only strictly negative powers of `w`. Therefore

```text
g(z(w))=F_{12}(f)(z(w))=w^{12}+O(w^{-1}),
```

with no terms `w^{11},…,w^0`. The sign convention in both compilers is `r_ℓ=-[w^{-ℓ}]g(z(w))`, i.e.

```text
g(z(w))=w^{12}-\sum_{ℓ≥1} r_ℓ w^{-ℓ}.
```

Vanishing of `r_1,…,r_8` upgrades this to `g(z(w))=w^{12}+O(w^{-9})`. There is no leftover positive or constant Laurent term, and the first possibly surviving tail is `w^{-9}`.

### Cubing and the `w`-order of `W`

Let `W=g^3-f^4` and `T=g(z(w))-w^{12}=O(w^{-9})`. Then `f(z(w))^4=w^{36}` and

```text
g(z(w))^3
  = w^{36}+3w^{24}T+3w^{12}T^2+T^3
  = w^{36}+O(w^{15})+O(w^{-6})+O(w^{-27}).
```

Hence `W(z(w))=O(w^{15})` in the filtration at infinity: no power `w^{≥16}` occurs. (If the first surviving tail is exactly `r_9`, the term `3w^{24}·O(w^{-9})` can realize order `15`; the bound is sharp and that is harmless.)

### Passage from `w`-order to ordinary `z`-degree

`W` is an ordinary polynomial in `z` (coefficients in the base field of a geometric point). If `deg_z W=d` with leading coefficient `c_d≠0`, then

```text
z(w)^d=w^d+O(w^{d-2}),    W(z(w))=c_d w^d+O(w^{d-1}).
```

The coefficient of `w^d` is exactly `c_d`. A nonzero polynomial therefore retains its ordinary degree under the substitution. Combined with the previous paragraph, `d≤15`, which is (3) in the target.

Attacks that failed:

- Cancellation among several high `z`-degrees cannot kill the top `w`-power, because degree `d` is the unique contributor to `w^d`.
- Leading terms of `g^3` and `f^4` cancel (`z^{36}-z^{36}`), but that only gives `deg W≤35` a priori; the eight tails are what drop it to `15`.
- A hidden `w^6` would require `k≠0`, already excluded on this fibre.
- The `O(w^{15})` notation is the filtration at infinity, as in `z(w)=w+O(w^{-1})`. The opposite interpretation (order at `w=0`) is inconsistent with the rest of the display.

The complementary fibre fact `r_8≠0 ⇒ deg W=16` (Mason equality, not contradiction) is consistent and shows why the eighth homogenized row is indispensable.

---

## Bridge 3 — Mason–Stothers after `D=gcd(g^3,f^4)`

**CONFIRMED**

Assume `W≠0`. The ring `k[z]` is a Euclidean domain. Let `D=gcd(g^3,f^4)` be monic of degree `e`, and set

```text
A=g^3/D,    B=-f^4/D,    C=-W/D.
```

Then `A+B+C=0`. The polynomial `D` divides both `g^3` and `f^4`, hence divides `W=g^3-f^4`. For nonzero `W` one has `e≤deg W≤15`, and `deg C=deg W-e≤15-e`. Always `deg g=12` (`F_{12}` is monic of degree `12`) and `deg f=9`, so `deg A=deg B=36-e≥21`. In particular `A,B` are nonconstant.

If `e=36`, then `D` has the full monic degree of `g^3` and of `f^4`, so `g^3=f^4=D` and `W=0`, contradicting the standing hypothesis. This edge is closed.

Pairwise coprimeness: `gcd(A,B)=1` by construction of `D`. For any triple with `A+B+C=0`, a prime dividing two of them divides the third, so `gcd(A,B)=1` is equivalent to pairwise coprimeness. Explicitly: a common prime of `A` and `C` divides `B`, and a common prime of `B` and `C` divides `A`.

None of `A,B,C` is zero (`g` and `f` are monic; `W≠0`). They are not all constant. Characteristic zero excludes the `k[z^p]` degeneration of Mason–Stothers. Therefore

```text
36-e = max(deg A,deg B,deg C)
     ≤ deg rad(ABC)-1.
```

Primes of `A` divide `g`; primes of `B` divide `f`. Hence `rad(A)rad(B)` divides `rad(fg)`, and

```text
deg rad(ABC)=deg rad(A)+deg rad(B)+deg rad(C)
            ≤ deg rad(fg)+deg C
            ≤ deg rad(fg)+(15-e).
```

The degree of a squarefree kernel is independent of the constant-field extension (it equals the number of distinct roots in an algebraic closure; characteristic zero is separable). Also `deg rad(fg)≤deg f+deg g=21`, whether or not `f` and `g` are squarefree or coprime. Thus

```text
36-e ≤ deg rad(fg)+(15-e)-1 ≤ 21+(15-e)-1 = 35-e,
```

so `36≤35`. Strict contradiction.

Edges:

- If `C` is a nonzero constant, then `deg C=0` and the same estimate still reads `36-e≤35-e`. Directly one even has `36-e≤deg rad(fg)-1≤20` with `36-e≥21`, a stronger contradiction. Leadings of `A` and `B` cancel in the sum (both monic of degree `36-e` up to the sign of `B`), which is consistent with `A+B` being constant, and does not affect Mason’s use of `max(deg A,deg B)`.
- Shared factors of `f` and `g` shrink `rad(fg)` and strengthen the contradiction.
- A prime with `3v_p(g)=4v_p(f)` is absorbed entirely into `D`. It is absent from `A` and `B`; if it survives in `C` it is counted on the right via `deg C` and not double-counted against pairwise coprimeness.
- Base change to a finite constant extension, or to an algebraic closure, does not change degrees of radicals of univariate polynomials in characteristic zero.

Hence `W=0`, i.e. `g^3=f^4`.

---

## Bridge 4 — UFD, depression, graph, saturation, Nullstellensatz

**CONFIRMED**

### Unique factorization

From `g^3=f^4` in the UFD `k[z]`, `f` and `g` have the same irreducible factors. Writing `v_p(f)=a_p` and `v_p(g)=b_p` gives `3b_p=4a_p`. Since `gcd(3,4)=1` one has `a_p=3c_p` and `b_p=4c_p`. Taking the monic product `C=∏ p^{c_p}` (Galois-stable, hence defined over the same field) yields monic identities `f=C^3`, `g=C^4` with `deg C=3`.

### Depression

Write `C=z^3+c_2 z^2+p z+r`. Expanding,

```text
C^3=z^9+3c_2 z^8+ (terms of degree ≤7).
```

The `z^8` term arises only from `3z^6·(c_2 z^2)`; the summands `3z^3(c_2 z^2)^2` and `(c_2 z^2)^3` have degrees `7` and `6`. Depression of `f` forces `3c_2=0`, hence `c_2=0` in characteristic zero. This is (1).

### The six graph equations

The binomial expansion of `(z^3+pz+r)^3` is

```text
z^9 + 3z^6(pz+r) + 3z^3(pz+r)^2 + (pz+r)^3,
```

which collects to (2):

```text
B_7=3p,     B_6=3r,      B_5=3p^2,     B_4=6pr,
B_3=p^3+3r^2,  B_2=3p^2 r,  B_1=3pr^2,  B_0=r^3.
```

Over `Q`, this is the graph of a polynomial map `A^2_{B_6,B_7}→A^6`. Equivalently, writing `p=B_7/3` and `r=B_6/3` (valid in characteristic zero), the six Cartesian equations are

```text
3B_5-B_7^2=0,
3B_4-2B_6 B_7=0,
27B_3-B_7^3-9B_6^2=0,
9B_2-B_7^2 B_6=0,
9B_1-B_7 B_6^2=0,
27B_0-B_6^3=0.
```

The inverse `(B_i)↦(B_7/3,B_6/3)` is polynomial, so the image is closed in `A^8`, isomorphic to `A^2`, and irreducible. Its vanishing ideal is prime. If `B_7=B_6=0` then all six equations force every `B_i=0`, so there is no stray component supported away from the `(p,r)`-plane.

### Converse: the graph lies in `V(I_inf)`

If `f=C^3`, then `C(z(w))^3=w^9`. The unique Laurent solution with leading term `w^3` is `C(z(w))=w^3`: if `X=w^3(1+u)` with `u=O(w^{-2})`, then `(1+u)^3=1` forces `u=0` in characteristic zero. Thus `C^4(z(w))=w^{12}`. A polynomial which becomes `O(w^{-1})` after substituting `z(w)` is zero, and `F_{12}(f)(z(w))=w^{12}+O(w^{-1})`, so `F_{12}(C^3)=C^4`. All tails vanish. The two reduced supports therefore agree as sets.

### Affine origin, origin-supported component, irrelevant point of `Proj`

The point `(p,r)=(0,0)` maps to the affine origin `B=0`, which is the cube `C=z^3`, `f=z^9`, `g=z^{12}`, and lies on the graph. Hilbert Nullstellensatz over an algebraic closure therefore gives `rad(I_inf)=I(\text{graph})`, already a saturated prime: the only associated prime of a prime ideal is itself, and that prime is not the irrelevant maximal ideal `m=(B_0,…,B_7)` because `V` is two-dimensional. Saturation `I_inf:m^∞` can drop an embedded `m`-primary component, but it does not change reduced support and does not delete the origin from the affine cone.

Three distinct objects:

1. The affine origin, a point of the cone (present after saturation).
2. An origin-supported (embedded or isolated `m`-primary) component, which saturation removes and which the theorem does not classify.
3. The irrelevant point of `Proj`, which is not a point of the weighted projective exceptional divisor.

The theorem’s reduced-support statement is the first object, not the second, and the projective statement ignores the third. No localization by `p r \operatorname{disc}(C)` occurs.

---

## Bridge 5 — reduced exceptional divisor is weighted `P(2,3)`

**CONFIRMED**

The `B_i` are weighted-homogeneous of weights `9-i`, and (2) is equivariant for

```text
(p,r) ↦ (λ^2 p, λ^3 r),    B_i ↦ λ^{9-i} B_i.
```

The affine reduced support is the cone on that action. Its `Proj` is the weighted line `P(2,3)`. Every point other than the vertex has `(p,r)≠(0,0)`, hence `B_7=3p` or `B_6=3r` nonzero, so it is a genuine projective point.

Both axes survive: `r=0`, `p≠0` is the point `(1:0)∈P(2,3)`; `p=0`, `r≠0` is `(0:1)`. The discriminant `-4p^3-27r^2=0` is a nonempty closed subset of `P(2,3)` and is not inverted. These are the orbifold points of `P(2,3)` (stabilizers `μ_2` and `μ_3`), which is the geometric reason the ramification corollary permits denominators `2` and `3` precisely on those axes.

There is no extra projective component: every nonzero point of `V(I_inf)` is `φ(p,r)` for a unique `(p,r)≠(0,0)`.

---

## Bridge 6 — rational ramification corollary

**CONFIRMED**

On a ramified chart of a genuine rational pole write `m/n>3` in lowest terms and

```text
s-1=τ^n,    e=τ^m,    B_i(τ)=τ^{m(9-i)} A_i(1+τ^n).
```

The functions `A_i` depend on `s=1+τ^n`, hence are invariant under `τ↦ζτ` for `ζ^n=1`. Therefore

```text
B_i(ζτ)=ζ^{m(9-i)} B_i(τ).
```

Evaluating constant terms, `B_i(0)(ζ^{m(9-i)}-1)=0`. Equivalently, the expansion of `A_i` is in powers of `τ^n`, so `B_i` has exponents `m(9-i)+nk`; a constant term exists if and only if `n∣m(9-i)`. Thus every active leading index `i∈S` (those with `B_i(0)≠0`) satisfies `n∣m(9-i)`, hence `n` divides `gcd\{m(9-i):i∈S\}`.

Because `m/n` is in lowest terms, `gcd(m,n)=1`. Euclid then upgrades `n∣m(9-i)` to `n∣(9-i)`. (Without lowest terms one could inflate `n` by a common factor; that is a reparametrization, not a new denominator.)

On the reduced support (2), the weights `9-i` and vanishing pattern are:

- `p r≠0`: `B_7=3p≠0` (weight `2`) and `B_6=3r≠0` (weight `3`) are both active, so `n∣2` and `n∣3`, hence `n=1`. Vanishing of `B_3=p^3+3r^2` on a discriminant-zero point does not kill weights `2` and `3`.
- `r=0`, `p≠0`: active values `B_7=3p`, `B_5=3p^2`, `B_3=p^3`, all nonzero in characteristic zero. Active weights `2,4,6`, so `n∣2`.
- `p=0`, `r≠0`: active values `B_6=3r`, `B_3=3r^2`, `B_0=r^3`. Active weights `3,6,9`, so `n∣3`.

If `B_7=B_6=0` then (2) forces the origin, which is not a projective leading point of a coefficient-infinity chart (the slope would not have been realized). For rational functions `A_i∈L(s)` every pole order is an integer, so every genuine D1 slope is rational; the corollary is not restricted to a proper subclass of actual poles.

The numerator `m` is unconstrained except by `m/n>3` and coprimeness, hence unbounded. Integer slopes `m≥4` and the licensed half- and third-axis slopes all satisfy the leading equations on this support. That is order-zero survival of the associated-graded system, not a `τ`-deformation: the common cubics solve the eight tails identically, which says nothing about the normal Kuranishi obstruction at positive order.

---

## Bridge 7 — scope firewall

**CONFIRMED; no creep in the target**

The target, read literally, asserts reduced support of one exceptional divisor plus a denominator reduction for rational poles. The following implications are **not** licensed and are **not** made.

| Forbidden reading | Why it fails |
|---|---|
| `I_inf` is radical | Only `V(rad(I_inf))` is identified. Embedded thickness is explicitly declined. |
| Formal / analytic lifting | Associated-graded cubics need not persist. Persistence is the unproved normal Kuranishi problem; a persistent common cubic would have vanishing source bracket along the arc. |
| D1 exclusion | The classical degree split only forces counterexample clients onto this sector. The sector’s reduced exceptional support is nonempty, `m` is unbounded, and lifting is open. |
| Finite-chart check | `n∈{1,2,3}` is a denominator reduction, not a numerator reduction. Infinitely many slopes remain. |
| Counterexample | A leading cubic is not a polynomial automorphism and not a Taylor realization. |
| JC2 | Explicitly declined. Fixed-total-D12 work and the `(6,9)` common-cubic theorem do not cover this unbounded-total divisor. |
| Reducedness of the scheme | Reduced support is not reducedness. |
| Order-zero survival is a deformation | The cubics solve the tails identically; that is the special fibre, not a jet in `τ`. |

The affine origin remains a point of the cone and is not a coefficient-infinity leading term. Confusing those three origin-objects is a misreading, not a theorem.

Two further firewalls inherited from the frozen parents and not to be collapsed into this note: the V2 gate emits source rows only, and the classical degree split is a split, not a closure of the strict inequality `d_i>3(9-i)`.

---

## Attacks recorded and rejected

1. **Seven tails instead of eight.** Vanishing `r_1=⋯=r_7` only yields `deg W≤16`, hence Mason equality `36-e≤36-e`. The homogenized `R=0` row is what drops the bound to `15` and produces a contradiction. The target includes `r_8=0`.
2. **`k F_6` contamination of the associated graded.** Finite `k` has strictly lower weight; `K=0` on the special fibre.
3. **Positive Laurent terms in `g(z(w))`.** Discarded negative `z`-powers compose to negative `w`-powers only. Faber supplies `w^{12}` and nothing in `w^{11},…,w^0` when `k=0`.
4. **Leading-term cancellation hiding `deg_z W>15`.** The top `w`-power of a degree-`d` polynomial is uncancellable.
5. **Failure of pairwise coprimeness after dividing by `D`.** `gcd(A,B)=1` by construction, and `A+B+C=0` promotes that to a pairwise statement.
6. **Mason equality on a squarefree coprime pair with `deg W=15`.** The estimate is `36-e≤35-e` even in the most generous case `deg rad(fg)=21` and `deg C=15-e`.
7. **`C` not defined over the same field.** Monic cube-root extraction in a UFD is Galois-stable.
8. **Extra component with `B_7=B_6=0` but some `B_i≠0`.** The six graph equations forbid it.
9. **Denominator `n>3` on a nonreduced structure.** Ramification of an actual pole is a statement about leading (reduced) coefficients. An embedded origin is not a leading `B`.
10. **Irrational slopes escaping the corollary.** Valuations of rational functions are integers, so every genuine D1 slope is rational.

No repair is required. The claim is confirmed at the exact scope of reduced exceptional support.
