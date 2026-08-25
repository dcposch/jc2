# Hostile review — general Faber exceptional-support theorem

| Field | Value |
|---|---|
| Target | `xmodel/max12-general-faber-exceptional-support-mason-20260825.md` |
| Target SHA-256 | `7d5271e8caf6d6d071819e8b2a670ac79d2063882a90d4916060b3e4deb95919` |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. The companion review `xmodel/max12-general-faber-exceptional-support-mason-review-20260825.md` was inspected as required and is not evidence |
| Method | source reading and hand derivation only; no CAS, solver, or substantive Python |
| Git HEAD | `24184c989634b40b00da1bbc3328bcc6ab92fa9b` (producer uncommitted) |
| Required repairs | none |
| Overall verdict | **CONFIRMED** |

Independently recomputed SHA-256 of the producer is `7d5271e8caf6d6d071819e8b2a670ac79d2063882a90d4916060b3e4deb95919`, matching the charged target.

## Verdict

The charged theorem is correct over an arbitrary characteristic-zero field. Vanishing of the first `m-1` Faber tails of `g=F_n(f)` forces `deg_z(g^a-f^b)≤N-m-n`. Substitution `z(w)=w+O(w^{-1})` cannot conceal a larger ordinary degree: the coefficient of `w^{deg W}` is exactly the leading coefficient of `W`. If that bound is negative — equivalently `a=1` or `b=1` — then `W=0` already. If not, Mason–Stothers after dividing by `gcd(g^a,f^b)` is the strict inequality `N-e≤N-e-1`, including the constant-`W` and apparent `e=N` edges. Unique factorization in `L[z]` produces a unique monic `K∈L[z]` of degree `d=gcd(m,n)` with `f=K^a` and `g=K^b`; depression of `f` forces depression of `K`. The converse is the inverse-root characterization of `F_n`, not an analytic extra. The reduced zero scheme of the first `m-1` tails is that power locus, a closed prime copy of `A_L^{d-1}`; for `d≥2` its weighted `Proj` is `P(2,3,…,d)`, and for `d=1` the projective locus is empty. The `(9,12)` and `(8,12)` substitutions are correct. The tail ideal is not claimed reduced, and a Rees exceptional fibre is not identified with these ordinary unloaded tails.

No identity failed. No hypothesis is missing from the reduced-support claim.

## Strongest exact theorem

Let `L` be a field of characteristic zero, `m≥2`, and `n≥1`. Let `f∈L[z]` be monic of degree `m` and depressed, and let `g=F_n(f)` be the unique monic degree-`n` polynomial satisfying

```text
g(z(w))=w^n-T(w),    T(w)=sum_{ℓ≥1} r_ℓ w^{-ℓ},
```

where `z(w)=w+O(w^{-1})` is the inverse of the monic `m`-th root `w=f(z)^{1/m}=z+O(z^{-1})`. Put `d=gcd(m,n)`, `a=m/d`, `b=n/d`, and `N=lcm(m,n)=an=bm`.

The following are equivalent:

1. `r_1=⋯=r_{m-1}=0`.
2. `g^a=f^b` in `L[z]`.
3. There is a unique monic depressed `K∈L[z]` of degree `d` with `f=K^a` and `g=K^b`.

In that case every Faber tail vanishes, not merely the first `m-1`. Consequently, in the affine space `A_L^{m-1}` of depressed monic degree-`m` polynomials, the reduced zero scheme of `(r_1,…,r_{m-1})` equals the common-`d`th-root locus. That locus is closed and prime, and the power parametrization is an `L`-isomorphism onto it from `A_L^{d-1}` with coordinates the depressed coefficients of `K`. For `d≥2` the weighted-projective reduction, with `c_j` of weight `d-j`, is `P(2,3,…,d)`. For `d=1` the affine locus is only the origin `f=z^m`, and its weighted `Proj` is empty.

Specializations: the ordinary unloaded eight-tail system `(m,n)=(9,12)` has reduced support `f=K^3`, `g=K^4` with `K=z^3+pz+c`, projectively `P(2,3)`; the ordinary unloaded seven-tail system `(m,n)=(8,12)` has reduced support `f=K^2`, `g=K^3` with `K` a depressed monic quartic, projectively `P(2,3,4)`.

## Required repairs

None.

Wording that is not a mathematical repair: the producer writes a monic degree-`n` Faber polynomial rather than the inequality `n≥1`. That convention is already the characterization. The `b=1` edge is not named in §1, but it is the case `D=-n<0` and is covered by the displayed negative-degree vanishing.

## Strict scope firewall

This is a reduced-support theorem for the ordinary unloaded tails of `F_n(f)` on the affine space of depressed monic degree-`m` polynomials. It does **not**:

- prove that the tail ideal `(r_1,…,r_{m-1})` is reduced, or determine embedded or nilpotent structure;
- identify a weighted Rees exceptional fibre with these tails, unless that client separately proves that lower Faber terms and nonzero target loads acquire positive Rees weight and vanish, and that the descended exceptional rows are the ordinary first `m-1` tails;
- give a formal lifting or exclusion theorem, bound contact order, turn an algebraic arc into a rational constant-field section, or establish Taylor polynomiality;
- close a passport, produce a counterexample, or close JC2.

The producer’s own firewall and the Rees-client paragraph match this boundary. No creep was found.

---

## Finding 1 — spectral degree bound

**Severity: none.**

Let `W=g^a-f^b`. Condition (1) is `T=O(w^{-m})` in the inverse-root coordinate, and `f(z(w))=w^m`, so

```text
W(z(w))=(w^n-T)^a-w^N
        =sum_{j=1}^a binom(a,j) w^{n(a-j)}(-T)^j.
```

The binomial expansion is finite because `a` is a positive integer. The series `T` has only strictly negative powers of `w` by the Faber characterization, so there is no leftover nonnegative Laurent term to cancel or inflate the count. The `j`-th summand is `O(w^{n(a-j)-jm})=O(w^{N-j(n+m)})`. The exponent `N-j(n+m)` is strictly decreasing in `j`, so the largest possible power is the `j=1` term `N-m-n`. Characteristic zero is not required for this upper bound (it would only be needed to guarantee that `binom(a,1)=a` is nonzero, which is irrelevant to an `O(·)` estimate). Thus `W(z(w))=O(w^D)` with `D:=N-m-n`, in the filtration at infinity.

It remains to pass from that filtration to ordinary `z`-degree. The change of coordinate is `z(w)=w+O(w^{-1})`; depression of `f` in fact gives no constant term in `z-w`, but a constant term would not affect the leading power. If `W` is a nonzero polynomial of degree `δ` with leading coefficient `c≠0`, then

```text
z(w)^δ=w^δ+O(w^{δ-2}),    W(z(w))=c w^δ+O(w^{δ-1}).
```

The coefficient of `w^δ` is exactly `c`: no lower `z`-power can contribute to `w^δ`, and the `O(w^{-1})` correction in `z(w)` cannot produce a power larger than `δ` or cancel `c`. Therefore substitution preserves both the degree and the leading coefficient of every nonzero polynomial in `z`, and cannot hide a polynomial of degree larger than `D` behind the coordinate change. Combined with the previous paragraph, `deg_z W≤D` whenever `W≠0`.

If `D<0`, the series `W(z(w))` has only negative powers of `w`, so the polynomial `W` is zero. Explicitly `D=d((a-1)(b-1)-1)`, so `D<0` if and only if `a=1` or `b=1`:

- `a=1` (`m∣n`) gives `D=-m` and `W(z(w))=-T`, so the first `m-1` tails already force `W=0`. In this edge `F_n(f)=f^b` for every depressed monic `f`, and the tail hypothesis is automatic.
- `b=1` (`n∣m`) gives `D=-n`; under (1) one gets `F_n(f)^a=f`.

The producer names `a=1` and the general `D<0` vanishing; `b=1` is included.

Attacks that failed: cancellation among the `j≥2` terms can only lower the `w`-order; a hidden nonnegative Laurent term in `T` is forbidden by the characterization `T=sum_{ℓ≥1} r_ℓ w^{-ℓ}`; replacing `O(w^{-m})` by the weaker `O(w^{-(m-1)})` would raise the bound to `D+1` and destroy the later Mason contradiction, so `m-1` tails are the correct count.

## Finding 2 — Mason–Stothers after `D_0=gcd(g^a,f^b)`

**Severity: none.**

It remains to treat `D≥0` with `W≠0`, equivalently `a≥2` and `b≥2`. Let `D_0=gcd(g^a,f^b)` be monic in `L[z]` of degree `e`. Then `D_0` divides `W`, so `0≤e≤deg W≤D=N-m-n<N`. Set

```text
A=g^a/D_0,    B=-f^b/D_0,    C=-W/D_0.
```

Then `A+B+C=0`. None is zero (`f` and `g` are monic of degrees `m,n≥1`; `W≠0`). Also `deg A=deg B=N-e≥m+n≥4`, so `A` and `B` are nonconstant, and `deg C≤D-e`. In particular `max(deg A,deg B,deg C)=N-e`.

Pairwise coprimality: `gcd(A,B)=1` by construction of `D_0`. For any three polynomials summing to zero, a prime dividing two divides the third, so `gcd(A,B)=1` is equivalent to pairwise coprimality.

Mason–Stothers over a characteristic-zero field applies to pairwise coprime `A,B,C∈L[z]`, not all constant, not all of vanishing derivative: the last is free because `A` is nonconstant in characteristic zero. Thus

```text
N-e ≤ deg rad(ABC)-1.
```

Primes of `A` divide `g` and primes of `B` divide `f`, so the geometric roots of `AB` lie among those of `fg`. Pairwise coprimality splits the radical, and `deg rad(C)≤deg C≤D-e` (a constant contributes no roots). Squarefreeness of `f` or `g` is not used: `deg rad(fg)≤m+n` always, and repeated or shared roots only shrink the right-hand side. Therefore

```text
N-e ≤ deg rad(ABC)-1 ≤ (m+n)+(D-e)-1 = N-e-1,
```

which is absurd.

Edges:

- Nonzero constant `W`. Then `e=0` and `C` is a nonzero constant, contributing no radical roots. The same chain reads `N≤(m+n)+D-1=N-1`. Directly one even has `N≤deg rad(fg)-1≤m+n-1`, a stronger contradiction. Leading terms of `A` and `B` cancel (monic of degree `N` up to the sign of `B`), consistent with `A+B` constant.
- `D<0` is already `W=0` by Finding 1; Mason is not invoked.
- `a=1` and `b=1` are the two `D<0` divisibility edges.
- Apparent edge `e=N`. Forbidden by `e≤D<N`. Directly: a monic degree-`N` common divisor of the two monic degree-`N` polynomials `g^a` and `f^b` is equality, hence `W=0`.
- The count is unchanged by extending the constant field: in characteristic zero, `deg rad` of a univariate polynomial equals the number of distinct geometric roots.

Hence `W=0` in every case, i.e. `g^a=f^b`.

## Finding 3 — UFD, same field, depression of `K`

**Severity: none.**

Now `g^a=f^b` in the UFD `L[z]`, with `gcd(a,b)=1` by construction of `d`. For each irreducible `p∈L[z]` one has `a v_p(g)=b v_p(f)`, so `a` divides `v_p(f)` and `b` divides `v_p(g)`. Writing `v_p(f)=a c_p` and `v_p(g)=b c_p`, the monic product `K=∏ p^{c_p}` lies in `L[z]` (no algebraic closure, and no Galois descent, because the factorization is already taken in `L[z]`). Monicity of `f` and `g` removes the unit ambiguity, so this `K` is the unique monic polynomial with `f=K^a` and `g=K^b`. Degrees give `deg K=d`.

Write `K=z^d+c_{d-1}z^{d-1}+⋯+c_0`. The coefficient of `z^{m-1}` in `K^a` comes only from the `a` choices of one factor `c_{d-1}z^{d-1}` and `a-1` factors `z^d`, hence equals `a c_{d-1}`. Depression of `f` and characteristic zero (`a` invertible in `L`) force `c_{d-1}=0`. Depression therefore descends to `K`. Uniqueness of monic `K` is unchanged.

The `d=1` case is included: `K=z+c_0` and `a c_0=0` give `K=z`, so `f=z^m` and `g=z^n`.

## Finding 4 — converse from the Faber characterization

**Severity: none.**

Let `K∈L[z]` be monic depressed of degree `d` and set `f=K^a`. The inverse root of `f` satisfies `K(z(w))^a=w^{ad}=w^m`. In the formal Laurent series ring the unique `a`-th root with leading term `w^d` is `w^d` itself: if `X=w^d+c_k w^k+⋯` with `k<d`, then `X^a=w^m+a c_k w^{(a-1)d+k}+⋯`, and `a≠0` forces `c_k=0`. Thus `K(z(w))=w^d` as series, and `K^b(z(w))=w^{db}=w^n`. The polynomial `K^b` is monic of degree `n`, so the characterizing identity `g(z(w))=w^n-T` forces `T=0` and `F_n(f)=K^b`. Every tail vanishes.

This is the producer’s opening definition of `F_n`, not an unstated analytic identification. Equivalently in the `z`-coordinate, the monic branch of `f^{n/m}` is already the polynomial `K^b`, whose polynomial part is itself.

## Finding 5 — scheme language, radical, `A^{d-1}`, weighted `Proj`, `d=1`

**Severity: none.**

The power map `φ:A_L^{d-1}→A_L^{m-1}` sends the depressed coefficients `(c_0,…,c_{d-2})` of `K` to those of `K^a`. Write `K=z^d+Q` with `deg Q≤d-2`. In `K^a=(z^d+Q)^a` the summand `a z^{m-d}Q` contributes `a c_j` to the coefficient of `z^{m-d+j}`. For `k≥2`, the coefficient of `z^{m-d+j}` in `z^{d(a-k)}Q^k` is the coefficient of `z^{(k-1)d+j}` in `Q^k`. Reaching that degree requires every factor of `Q` to have degree `>j`, hence depends only on `c_{j+1},…,c_{d-2}`. Working downwards from `j=d-2` (the `z^{m-2}` coefficient, which is exactly `a c_{d-2}`) therefore recovers each `c_j` as `(1/a)` times that coefficient of `K^a` minus a polynomial in already recovered higher `c`’s. The diagonal `a` is invertible in `L`. So `φ` is an `L`-isomorphism onto a closed image, the image is isomorphic to `A_L^{d-1}`, and its ideal `P` is prime.

By Findings 1–4, over an algebraic closure the geometric zero set of `(r_1,…,r_{m-1})` equals `V(P)`. The converse puts each tail in `P`, so `I:=(r_1,…,r_{m-1})⊂P`. Hilbert Nullstellensatz over the closure gives `rad(I^e)=P^e`. Affine space is geometrically integral, so `P^e` remains prime. Faithful flatness of `L[B]→\bar L[B]` (or linear independence of a basis of the scalar extension) contracts this to `rad(I)=P` over `L`. The reduced zero scheme of the first `m-1` tails is therefore exactly the power locus.

This does **not** prove `I=P`. The producer never claims that the tail ideal is reduced; the firewall forbids it, and the triangular argument is about the power parametrization, not about generators of `I`.

Weighted homogeneity: `c_j` has weight `d-j` under the Faber/`G_m` scaling for which `z` has weight `1`. After depression the surviving weights are `2,3,…,d`, so for `d≥2` the `Proj` of the affine cone is `P(2,3,…,d)`, with coordinates the depressed coefficients of `K`. The missing weight `1` is precisely the `z^{d-1}` coefficient already set to zero.

For `d=1` there are no positive-degree parameters. The affine locus is the single point `f=z^m` (the origin of `A_L^{m-1}`), a closed prime copy of `A_L^0`. That point is the irrelevant vertex of the weighted cone, so its projectivization is empty. Three distinct objects remain distinct: the affine origin (present), an origin-supported embedded component of the raw tail ideal (not classified), and the irrelevant point of `Proj` (not a projective point).

## Finding 6 — `(9,12)` and `(8,12)` clients, Rees firewall

**Severity: none.**

```text
(m,n)=(9,12): d=3, a=3, b=4, N=36, D=15, first 8 tails,
              K=z^3+pz+c,  f=K^3, g=K^4,  Proj = P(2,3).
(m,n)=(8,12): d=4, a=2, b=3, N=24, D=4,  first 7 tails,
              K depressed monic quartic, f=K^2, g=K^3,  Proj = P(2,3,4).
```

Both have `a,b≥2`, so Mason is needed and applies. These are the reduced supports of the ordinary unloaded tail systems. The producer correctly refuses to identify a weighted Rees exceptional fibre with those systems until the charged client proves that lower Faber terms and loads acquire positive Rees weight and vanish, and that the descended exceptional rows are the ordinary first `m-1` tails. Reduced support is not promoted to scheme reducedness, deformation exclusion, rationality, Taylor polynomiality, a passport closure, or JC2.

---

## Independent reconstruction (compressed)

Depression gives `z(w)=w+O(w^{-1})`. With `T=O(w^{-m})`,

```text
(g^a-f^b)(z(w))=sum_{j≥1} binom(a,j) w^{n(a-j)}(-T)^j = O(w^{N-m-n}).
```

A nonzero polynomial keeps its degree and leading coefficient under `z=z(w)`, so `deg(g^a-f^b)≤N-m-n`, and a negative bound forces vanishing. For a nonnegative bound, divide `g^a-f^b=0`’s putative nonzero instance by `D_0=gcd(g^a,f^b)` of degree `e≤D<N`. Mason–Stothers on the pairwise-coprime triple yields `N-e≤m+n+D-e-1=N-e-1`. Thus `g^a=f^b`. Unique factorization in `L[z]` with `gcd(a,b)=1` and monicity give unique monic `K∈L[z]` of degree `d` with `f=K^a`, `g=K^b`; `a c_{d-1}=0` depresses `K`. Conversely `K(z(w))=w^d` by uniqueness of the monic `a`-th root, so `K^b(z(w))=w^n` and `F_n(K^a)=K^b`. Triangular inversion of `K↦K^a` on depressed coefficients is an isomorphism `A_L^{d-1}≅` the power image, hence that image is closed and prime. Geometric equality of zero sets plus contraction gives `rad(r_1,…,r_{m-1})=P`. Weights `d-j` after depression yield `P(2,3,…,d)`, empty at `d=1`.

## Model identity and evidence boundary

Reviewer: Grok 4.6, released by xAI. Different-model hostile rederivation of the charged producer. The same-directory independent review dated 2026-08-25 was opened only to obey the inspection clause; its `CONFIRMED` string was not used. No prior stdout, no CAS, no solver, and no Python reconstruction was used as evidence. The load-bearing chain is the inverse-root characterization of `F_n`, the formal binomial expansion, preservation of polynomial degree under `z(w)=w+O(w^{-1})`, Mason–Stothers in characteristic zero, unique factorization in `L[z]`, and Nullstellensatz plus contraction.

CONFIRMED
