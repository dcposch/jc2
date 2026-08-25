# Hostile different-model review — D1 classical degree split at coefficient infinity

| Field | Value |
|---|---|
| Claim under review | After an allowed polynomial source shear making `R0` regular at `s=1`, if `d_i=max(0,-v_(s=1)(A_i))<=3(9-i)` for all `i`, then a Taylor-realizable cyclic `D=e=1` order-three `(9,12)` pair has exact ordinary total degrees `(27,36)`, hence cannot be a characteristic-zero Jacobian counterexample because `gcd(27,36)=9<16` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks the numbered implication `(1)=>(2)` or the GGV consequence. Non-blocking remarks: (i) the exact pair `(27,36)` is for the *sheared* representative; (ii) `k≠0` is unused by the degree identities, so the bounded sector is closed even on `k=0`; (iii) the GGV bound is consumed from the already primary-source-checked classical-closure parent, not re-fetched |
| Evidence tier | independent hand re-derivation of the source shear, the place `s=1` in `L(s)` and in `L(t)/(t^3-s)`, Stage-B conversion of pole order to `x`-degree, the Taylor expansion of `P`, the Faber weight of every monomial of `F_12+k F_6`, the Taylor expansion of `Q`, cancellation/degree-drop/field-extension exceptions, and the arithmetic `gcd(27,36)=9`. Full read of the seven named inputs. The same-model review of this fragment is not used as evidence |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the composition producer |
| Repo | `/Users/dc/code/math/jc2` |
| Date | 2026-08-25 |
| Execution constraint | Source-reading and hand derivation only. No CAS, solver, substantive Python, shell hashing, web search, or other heavy work. Target SHA recorded from the launch pin, not recomputed |

The seven named inputs were read in full before any verdict. No producer, case, canonical, coordination, prompt, run, log, or same-model review file was edited. The only file written is this review.

Target: `xmodel/max12-912-order3-d1-classical-degree-split-20260825.md`  
Target SHA-256 (launch pin): `1424037680ac7ceeb0927388c59e5028f43ca9b7d37916cfea61809ca5ed7361`

---

## Verdict in one paragraph

On a Taylor-realizable cyclic `D=e=1` order-three `(9,12)` pair, the source shear `(x,y)|->(x,y-q(x))` by the polynomial part of `R0` at `x=infinity` replaces `R0` by a function regular at `s=1`, leaves the depressed cores `f,g` and the invariants `A_i` untouched, and preserves both the constant-Jacobian property and automorphism versus nonautomorphism status. After that gauge, `t^3=s` is étale at `s=1`, `t` is a unit, and `v(u)=-2` with no hidden ramification. Stage-B membership puts every Taylor coefficient in `L[x]`, so its ordinary `x`-degree equals its pole order at `s=1`. The bound `d_i<=3(9-i)` then gives `deg_x([y^ell]P)<=27-ell` and `deg_x([y^ell]Q)<=36-ell` by the exact Faber grading of every monomial of `F_12+k F_6` (including those with a single factor of `k`). The top coefficients `[y^9]P=u^9=h^3` and `[y^12]Q=u^{12}=h^4` are monic in `x` of degrees `18` and `24`, producing uncancellable ordinary total degrees `27` and `36`. Guccione--Guccione--Valqui/Heitmann therefore forbids a counterexample, because `gcd(27,36)=9<16`. The argument does not touch the strict complementary sector `d_i>3(9-i)` for some `i`, nor any other passport, cell, or Kummer leaf.

**CONFIRMED**

---

## Scope actually confirmed

The implication is only this:

```text
Taylor-realizable cyclic D=e=1 order-three (9,12) pair
over a characteristic-zero finite constant field L,
written in the stated normalization
  s=x/(x-1), t^3=s, u=t^2/(s-1)^2, h=u^3=x^2(x-1)^4,
  f=z^9+sum_{i=0}^7 a_i z^i,  a_i=t^(i mod 3) A_i(s),
  g=F_12(f)+k F_6(f),  z=u(y+R0),  k in L,
after the polynomial source shear that makes R0 regular at s=1,
and under  d_i := max(0, -v_(s-1)(A_i)) <= 3(9-i) for 0<=i<=7
==>
the sheared pair has ordinary total degrees (27,36),
hence is not a characteristic-zero Jacobian counterexample.
```

No claim is confirmed about the complementary divisor (3), about existence or emptiness of Stage-A sections, about SAT or UNSAT of any Stage-B Taylor ideal, about `k=0` as a full fibre chart (see Attack 8), about a higher passport, about the order-one Kummer leaf, about `(8,12)`, about the full partial-`y` `(9,12)` cell, or about JC2.

---

## Attack 1 — the polynomial source shear

**CONFIRMED.** The shear leaves `f`, `g`, every `A_i`, Keller status, and counterexample status unchanged. The exact degree pair `(27,36)` is for the sheared representative.

**Depression and the `y^8` coefficient.** The core is monic depressed of degree 9, so the only contribution to `y^8` in `P=f(u(y+R0))` is from `z^9=u^9(y+R0)^9`. Thus

```text
[y^8]P = 9 u^9 R0 = 9 h^3 R0.
```

Taylor polynomiality puts `[y^8]P` in `L[x]`. Since `h=x^2(x-1)^4` is a non-zero polynomial, `R0` is rational on `P^1_x`. Its only possible finite poles lie among the zeros of `h^3` (orders at most `6` at `x=0` and `12` at `x=1`, matching the Stage-B finite ansatz, which is not otherwise used). Write `R0=q+R0_reg` with `q in L[x]` the unique polynomial part at `x=infinity` and `R0_reg` regular at infinity.

**Precomposition.** Let `φ(x,y)=(x, y-q(x))`. Then `det Dφ=1`, so

```text
P_new(x,y)=P(x,y-q(x))=f(u(y+R0-q)),
```

and likewise for `Q`. This is a source shear: `R0` is replaced by `R0-q`, which is regular at `x=infinity`. The cores `f,g` are polynomials in `z` with coefficients `a_i=t^(i mod 3)A_i(s)` and `k`; none of these data mentions the Taylor centre, so they are literally unchanged. In particular every `d_i` is unchanged.

The sign convention `y |-> y±q` is irrelevant: it only swaps `q` with `-q`.

**Status.** `φ` is a polynomial automorphism of `A^2_L`. Constant Jacobian is preserved because `J(F∘φ)=J(F)(φ)·J(φ)=J(F)`. Automorphism versus nonautomorphism is preserved because `F` is an automorphism if and only if `F∘φ` is. Therefore a pair is a Jacobian counterexample if and only if its shear is. It is enough to test the sheared pair.

**Degree caveat, not a gap.** If `deg q>=1`, the unsheared pair may have strictly larger ordinary total degrees than the sheared pair. The numbered claim (2) is about the sheared coordinates, as the producer writes. Counterexample status does not care: if the sheared pair is not a counterexample, neither is the original.

**Finite poles versus regularity at `s=1`.** The identities `s=x/(x-1)` and `s-1=1/(x-1)` show that `x=infinity` is exactly the place `s=1`. Regularity of `R0` at infinity is regularity at `s=1`, i.e. `v_(s-1)(R0)>=0`. A residual constant in `R0` is regular and may be kept or gauged away; it does not affect any pole bound used below.

---

## Attack 2 — places, valuations, and `t^3=s` at `s=1`

**CONFIRMED.** No fractional valuation is hidden at `s=1`.

Work with `v=v_(s-1)` on `L(s)`, normalised by `v(s-1)=1`. The coordinate identities used below are elementary and match both the producer and the D1 preregistration fixture:

```text
s = x/(x-1),     x = s/(s-1) = t^3/(t^3-1),
s-1 = 1/(x-1),   u = t^2/(s-1)^2 = t^2/(t^3-1)^2,
u^3 = t^6/(s-1)^6 = s^2/(s-1)^6
    = (s/(s-1))^2 · (1/(s-1))^4 = x^2(x-1)^4 = h.
```

The finite extension `L(t)/L(s)` is `T^3-s`. Its fibre at `s=1` is `T^3-1`. In characteristic zero this polynomial is separable (`gcd(T^3-1, 3T^2)=1` because every cube root of unity is non-zero and `3≠0`). Hence the extension is étale at `s=1`: every place of `L(t)` above `s=1` has ramification index one. Whether `T^3-1` splits completely over `L` (if `μ_3 subset L`, as in the campaign generator) or remains of residue degree two or three does not matter.

At each such place, `s=1+(s-1)` is a unit, so `t^3=s` forces `v(t)=0`: `t` is a unit. Therefore

```text
v(u) = 2 v(t) - 2 v(s-1) = -2
```

with the same normalisation `v(s-1)=1`. There is no denominator `3` from ramification. The three (or fewer) places above `s=1` all see the same valuation of every element of `L(s)`, in particular of every `A_i` and of `R0`.

The functions `a_i=t^(i mod 3) A_i` therefore satisfy `v(a_i)=v(A_i)` at every place above `s=1`. The quantity `d_i=max(0,-v(A_i))` is the pole order of `A_i` at `s=1`, or zero if `A_i` is regular or zero (`v(0)=+∞`).

A uniformizer check, not used as a second valuation: `s-1=1/(x-1)` and `1/(x-1)=x^{-1}(1-x^{-1})^{-1}`, so `v_(x=infinity)(s-1)=1` as well. Pole order at `s=1` of an element of `L(x)` is pole order at `x=infinity`.

---

## Attack 3 — Stage B licenses converting pole order to `x`-degree

**CONFIRMED.** The conversion is not a general fact about rational functions of `s`; it uses Taylor-realizability.

The function field is `L(s)=L(x)` with `x=s/(s-1)=1+1/(s-1)`, so `L[x]=L[1/(s-1)]`. A rational function `F in L(x)` lies in `L[x]` if and only if its only pole on `P^1` is at `x=infinity`, equivalently: it is regular at every finite `s`, including `s=infinity` (the point `x=1`), and it is allowed a pole only at `s=1`. In that case

```text
deg_x(F) = -v_(s-1)(F),
```

with the convention `deg(0)=-∞`. This is exactly the membership criterion compiled in `stage_b_taylor.py`: after stripping all factors `s-1` from the denominator, the remaining denominator must divide the numerator, and the quotient must have degree at most the stripped pole order (otherwise `F` is not regular at `s=infinity`, or equivalently not a polynomial in `1/(s-1)`). The compiled controls (`1+c x+x^2` accepted; `1/(s+1)` and `s^2/(s-1)` rejected) match this criterion and are not used as evidence for the algebra.

Taylor-realizability is the hypothesis that every coefficient `[y^ell]P` and `[y^ell]Q` *equals* an element of `L[x]`. In the cubic basis `1,t,t^2` of `L(t)/L(s)`, that forces the `t` and `t^2` components to vanish and puts the invariant component in `L[x]`. For such a coefficient, ordinary `x`-degree equals pole order at `s=1`.

**Upper bounds from `L(t)`.** Individual Taylor summands live in `L(t)`. One does not pass through their invariant parts. If each summand has `v_𝔭 >= -N` at every place `𝔭` of `L(t)` above `s=1`, the sum `S` satisfies the same bound. Stage B identifies `S` with an element of `L[x]`, hence `deg_x(S)<=N`. Galois averaging cannot increase the pole: even if one extracted the invariant part of a single summand, each conjugate would have the same pole bound because `A_i`, `R0`, and `s-1` are in `L(s)` and `t` is a unit at every place above `s=1`. Cancellation among summands, or among Galois components, can only drop the pole, which is harmless for an upper bound.

Finite constant extension does not change polynomial degree in `x,y`. The pair is in `L[x,y]`.

---

## Attack 4 — degree of `P`

**CONFIRMED.** Exact ordinary total degree `27`.

Expand the depressed monic core, writing `a_9=1` and `d_9=0`:

```text
[y^ell]P = sum_{i>=ell} binom(i,ell) a_i u^i R0^{i-ell},
           0 <= ell <= 9.
```

Binomial coefficients lie in `Q` and have valuation `0` or else the summand is identically zero. At every place above `s=1`,

```text
v(a_i) = v(A_i) >= -d_i,     v(u^i) = -2i,     v(R0^{i-ell}) >= 0,
```

the last because `R0` is regular at `s=1` after the shear. Hence each summand has pole order at most `d_i+2i`. Hypothesis (1) gives

```text
d_i + 2i <= 3(9-i) + 2i = 27 - i <= 27 - ell,
```

since `i>=ell`. Stage B therefore yields `deg_x([y^ell]P)<=27-ell`. Writing `P=sum_ell p_ell(x) y^ell`,

```text
deg_total P = max_ell (deg_x p_ell + ell) <= max_ell (27-ell+ell) = 27.
```

For the matching lower bound, the top coefficient is a single summand

```text
[y^9]P = u^9 = h^3 = x^6 (x-1)^{12}.
```

This is already in `L[x]`, monic of `x`-degree `18` (leading term `x^{18}`). The monomial `x^{18} y^9` has ordinary total degree `27`. No other `y`-degree can cancel a `y^9` monomial, and the leading coefficient `1` is non-zero in characteristic zero. Therefore `deg_total P=27` exactly.

Degree drop in lower `y`-coefficients is allowed and irrelevant. The zero polynomial is excluded by `h^3≠0`. Vanishing of some `A_i` only lowers `d_i`, which cannot increase the pole bound.

The numerical factor `3` is `v_infinity(u)+1=2+1`. Each unit of Faber weight contributes total degree at most `3` after substituting `z=u(y+R0)` with `R0` regular at infinity; `f` has weight `9`, and `9·3=27`. The bound `d_i<=3(9-i)` is exactly the statement that `A_i` does not exceed this budget. It is D1-specific: a higher balanced passport has a larger pole of `h` at infinity, hence a larger pole of `u`, and is not treated here.

---

## Attack 5 — Faber grading of `F_12+k F_6` and degree of `Q`

**CONFIRMED.** Every monomial, including those carrying `k`, has weight `12`. Exact ordinary total degree `36`.

**Form of `g`.** Shared Faber plus the order-three character filter and the three target gauges `h_9=h_0=h_3=0` leave

```text
g = F_12(f) + k F_6(f),     F_j = [w^j]_+ = z^j [sum_q binom(j/9, q) U^q]_+,
U = sum_{i=0}^7 a_i z^{i-9}.
```

This is the displayed normalization, and it is what `order3_fibre.py` and `stage_b_taylor.py` compile (`normalized_H=w^{12}+k w^6`). There is no `k^2` summand: `F_6` depends only on `f`.

**Weights.** Assign `wt(z)=1`, `wt(a_i)=9-i`, `wt(k)=6`. Then `f=z^9+sum a_i z^i` is homogeneous of weight `9`. Each term of `U` has weight `(9-i)+(i-9)=0`, so every `U^q` has weight `0`, and `F_j` is homogeneous of weight `j`. Truncation to non-negative `z`-powers does not mix weights. Consequently every monomial of `F_12` has weight `12`, every monomial of `F_6` has weight `6`, and every monomial of `k F_6` has weight `12`. The coefficient of `z^j` in `g` is therefore a sum of monomials `k^{e_k} prod_i a_i^{e_i}` with `e_k in {0,1}` and

```text
sum_i e_i (9-i) + 6 e_k + j = 12.                 (4)
```

Explicitly:

- `e_k=0` (from `F_12`): `sum_i e_i(9-i)+j=12` and `0<=j<=12`. The monic term is `e_i=0`, `j=12`. For `q>=1`, `U` has strictly negative `z`-exponents, so `[z^{12}]F_12=1` with no contamination.
- `e_k=1` (from `k F_6`): `sum_i e_i(9-i)+j=6` and `0<=j<=6`. In particular the term `k z^6` has no `a_i`. No monomial with `e_k>=2` occurs.

Those are all of the `k` monomials.

**Pole bound after `z=u(y+R0)`.** A monomial of `z`-degree `j>=ell` contributes to `[y^ell]Q` through `z^j=u^j(y+R0)^j`, hence through `u^j R0^{j-ell}`, times `k^{e_k} prod a_i^{e_i}`. Using `v(k)=0` (`k in L`, including the case `k=0` in which those summands vanish), `v(R0)>=0`, and `v(a_i)>=-d_i`,

```text
pole order  <=  sum_i e_i d_i + 2j
             <=  3 sum_i e_i(9-i) + 2j
              =  3(12 - 6 e_k - j) + 2j
              =  36 - 18 e_k - j
             <=  36 - j
             <=  36 - ell.
```

The slack `-18 e_k` shows that every genuine `k` monomial is *stricter* than the `e_k=0` bound: `k` consumes six units of Faber weight without contributing any pole at `s=1`. Stage B therefore gives `deg_x([y^ell]Q)<=36-ell`, hence `deg_total Q<=36`.

**Lower bound.** The top coefficient is again a single summand,

```text
[y^{12}]Q = u^{12} = h^4 = x^8 (x-1)^{16},
```

monic of `x`-degree `24`. The monomial `x^{24} y^{12}` has ordinary total degree `36`. Terms from `k F_6` have `z`-degree at most `6` and cannot touch `y^{12}`. The leading coefficient `1` cannot cancel. Thus `deg_total Q=36` exactly.

Check on the two top identities as functions of `s`: `u^9=s^6/(s-1)^{18}` has pole order `18`, matching `deg_x(h^3)`; `u^{12}=s^8/(s-1)^{24}` has pole order `24`, matching `deg_x(h^4)`. The conversion of Attack 3 is saturated on the uncancellable terms.

---

## Attack 6 — cancellation, zeros, degree drop, constant extensions, normalizations

**CONFIRMED.** None of the standard exceptions breaks exactness of `(27,36)`.

| Exception | Why it fails to drop the total degrees |
|---|---|
| Cancellation among `i` in `[y^ell]P` or among Faber monomials in `[y^ell]Q` | Only lowers pole orders of lower `y`-coefficients. The top coefficients `[y^9]P=h^3` and `[y^{12}]Q=h^4` are single monic summands |
| Cancellation among different `y`-degrees | Distinct monomials `x^{27-ell} y^ell`; they cannot cancel `x^{18} y^9` or `x^{24} y^{12}` |
| Leading-form degeneration toward `f=K^3`, `g=K^4+k K^2` | That degeneration lives on the complementary divisor (3) and on the common-cubic fibre, both firewalled. Under (1) the monic `z^9` and `z^{12}` terms survive |
| Zero polynomial / zero coefficient | `h^3≠0`, `h^4≠0`. Vanishing `A_i` is allowed and only helps the upper bound. `d_9=0` for the monic `a_9=1` |
| Degree drop of `h` | `h=x^2(x-1)^4` is monic of degree `6` over any characteristic-zero field |
| `R0` vanishing at `s=1` | Raises `v(R0)`, which can only drop lower-coefficient poles |
| Finite constant extension `L/Q` | Ordinary `x,y`-degrees are invariant. GGV is stated over an arbitrary characteristic-zero field, so it applies directly to `L` with no descent argument |
| Residual constant shear of `y` | Does not create a pole at `s=1` and does not touch `[y^9]P` or `[y^{12}]Q` |
| Target gauges `Q |-> Q-λP`, `P |-> P+c` | Already built into `g=F_12+k F_6`; they are not re-applied after the source shear. Adding a constant to `P` or `Q` cannot change total degrees `27` and `36` |
| Affine source change `x |-> αx+β` with `α≠0` | Part of the D1 fixture's uniqueness; does not change ordinary total degrees |
| Non-depressed `a_8` | Excluded by the displayed normalization. The shear of `R0` does not reintroduce a `z^8` term in `f` |
| `t,t^2` components of a Taylor coefficient | Stage B kills them; the sum is identified with an element of `L[x]` before degrees are read |
| `k=0` | Then `g=F_12` still has weight `12` and leading term `z^{12}`. The identities `(27,36)` still hold on the bounded sector (see Attack 8) |

A source automorphism that mixed `x` and `y` could change total degrees, but no such automorphism is applied. GGV is a condition on the pair as written, not on an orbit.

---

## Attack 7 — GGV/Heitmann scope

**CONFIRMED** for the consequence `gcd(27,36)=9<16`. The bound itself is consumed from the licensed classical-closure parent, not re-proved.

The already primary-source-checked note `xmodel/sol-fixed-total-d12-classical-closure-v2-20260825.md` and its hostile review record that Guccione--Guccione--Valqui, arXiv:1401.1784v3, work over an arbitrary characteristic-zero field, take a counterexample to be a pair in `K[x,y]` with non-zero constant Jacobian which is not an automorphism, and prove Heitmann's necessary condition on *ordinary* total degrees `v_(1,1)`:

```text
gcd(deg_total P, deg_total Q) >= 16.
```

That is the only use of GGV here. Independently: `27=3^3`, `36=2^2·3^2`, `gcd=9`, and `9<16`. Both coordinates are non-constant. The field of coefficients is a characteristic-zero finite constant extension `L`, which is inside the GGV scope. No leading-form hypothesis, no coprimeness of `P` and `Q`, and no bound `deg_total<=12` is required. The earlier D12 envelope closure is a strictly weaker special case; the present pair has total degrees larger than `12` and is killed only by the gcd, not by the D12 envelope.

If the sheared pair fails to have constant Jacobian, it is not a Jacobian counterexample either. The fibre/terminal row is not needed for the exclusion.

---

## Attack 8 — scope creep onto (3) or other branches

**CONFIRMED** that the conclusion does not close the complementary sector or any firewalled branch.

Hypothesis (1) is `d_i<=3(9-i)` for every `i`, including equality. Equality still yields exact `(27,36)`, because the top `y`-coefficients do not use the `A_i`. The complementary sector is the strict inequality (3),

```text
d_0>27 or d_1>24 or d_2>21 or d_3>18
or d_4>15 or d_5>12 or d_6>9  or d_7>6,
```

on which the pole budget of some `a_i` can push some `deg_x([y^ell])+ell` strictly above `27` or `36`. Ordinary total degrees may then rise, the leading equations may degenerate, and GGV may cease to apply. The producer correctly calls this a split, not a closure of (3). Neither Stage-A finite fibres nor affine Groebner data are claimed to cover that divisor.

The same numerical list is the first integer violation of (1); it is not an existence statement.

**What is not covered, and is not smuggled in:**

- The strict weighted coefficient-infinity sector (3), including its integer valuation branches and any degeneration toward the common-cubic locus `f=K^3`, `g=K^4+k K^2`.
- Completeness of D1 Stage-A sections, and SAT/UNSAT of any Stage-B Taylor ideal. The present implication assumes Taylor-realizability and then reads degrees; it does not produce or exclude a section.
- Higher passports. The factor `3=v_infinity(u)+1` is D1-specific (`deg h=6`, `v_infinity(u)=2`). A larger balanced `e` changes the pole of `u` and the total-degree budget.
- The order-one Kummer leaf, `(8,12)`, and the full partial-`y` `(9,12)` cell.
- JC2.

**`k=0`, non-blocking.** The degree identities never use `k≠0`: `v(k)>=0` holds for `k=0`, and `g=F_12` remains monic of weight `12`. Thus `k=0` intersected with (1), after the same shear, is also classically closed. The producer's firewall that the note does not close `k=0` is still the right global statement: it refuses to close the *unbounded* `k=0` chart, where some `d_i` may violate (1). The sentence "every D1 counterexample client must lie on (3)" is correct for Taylor-realizable cyclic D1 pairs, including those with `k=0`.

**Coefficient-infinity language.** The preregistration's weighted projective divisor (weights `wt(a_i)=9-i`, `wt(k)=6`, `wt(μ)=15`, `wt(ν)=18`, `wt(r8)=20`) is a compactification of coefficient space. The quantity `d_i` is instead the pole order of the rational function `A_i in L(s)` at `s=1`. For a degree-one section these are the same growth at `x=infinity`; they are not a classification of that projective divisor. The present split does not pretend otherwise.

---

## Independent derivation (compressed)

Let `F=(P,Q)` be Taylor-realizable in the stated D1 order-three normalization over `L`. Shear `R0` by its polynomial part at `x=infinity`; replace `F` by `F∘φ`. Cores and `A_i` are unchanged, `v_(s-1)(R0)>=0`, and counterexample status is unchanged.

At every place of `L(t)` above `s=1`, `e=1`, `t` is a unit, `v(u)=-2`, and `v(a_i)=v(A_i)>=-d_i`. For `0<=ell<=9`,

```text
v([y^ell]P) >= min_{i>=ell} (-d_i-2i) >= min_{i>=ell} (i-27) = ell-27.
```

Stage B puts `[y^ell]P` in `L[x]`, so `deg_x<=27-ell` and `deg_total P<=27`. But `[y^9]P=h^3` is monic of degree `18`, so `deg_total P=27`.

Every monomial of `g=F_12+k F_6` has Faber weight `12`, i.e. satisfies (4) with `e_k in {0,1}`. For `0<=ell<=12` and `j>=ell`,

```text
pole of a contributing monomial <= 3 sum e_i(9-i)+2j = 36-18 e_k-j <= 36-ell.
```

Stage B gives `deg_total Q<=36`. But `[y^{12}]Q=h^4` is monic of degree `24`, so `deg_total Q=36`.

Therefore `gcd(deg_total P, deg_total Q)=gcd(27,36)=9<16`. By GGV/Heitmann the sheared pair, hence the original pair, is not a characteristic-zero Jacobian counterexample.

---

## Firewall

This review confirms only the implication `(1)=>(2)` for Taylor-realizable cyclic `D=e=1` order-three `(9,12)` pairs after the stated source shear, and the resulting GGV exclusion of that bounded sector. It does not:

- close, or even bound, the strict sector (3);
- certify any Stage-A section, or solve any Stage-B Taylor ideal;
- close the full `k=0` chart, a higher passport, the order-one Kummer leaf, `(8,12)`, the full partial-`y` `(9,12)` cell, or JC2;
- re-prove Heitmann's theorem from first principles;
- assert that unsheared raw total degrees equal `(27,36)`.

The live D1 counterexample client, if any, must violate (1) for some `i`. That residue is completely untouched.
