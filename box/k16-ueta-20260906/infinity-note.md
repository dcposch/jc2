# Whole-polynomial infinity analysis and two uniform support consequences

Frozen mathematical inputs: `k16-utac-astra-20260906.md` §§2,4,8 and `k16-universal-series-fable5-20260905.md` §§3–4, `k16-tacnode-fable5-20260905.md` §§2–3, all read from `/tmp/jc2-lane.fImwPK/inputs/` after the root lane's mechanical hash verification. No external input or source code was used. This note is a mathematical supplement, not a claim of the full classification.

## 1. Every possible leading-degree case

Normalize b=1 on b≠0. The equation is

```
F=(theta-3)(P^2)+((3/2)L(L+1)-Bx)P
  -(3/16)L^2(L(L+2)-4Bx)+eta*x^2(L/2+Bx)=0,
theta=x*d/dx,
L=-1+sum_(j>=2) l_j*x^j,
P=-1/4-B*x+eta*x^2+w2*x^3+... .
```

The marked constant terms show that neither L nor P is zero. Put a=deg L and c=deg P. Thus a=0 or a≥2 and c≥0.

* a=0: L=-1. If c≥2, the term `(2c-3)lc(P)^2*x^(2c)` from `(theta-3)P²` has strictly greater degree than every other term (which have degrees ≤c+1 or 3). Its coefficient is nonzero in characteristic zero. Hence c≤1. The jets give eta=w2=0 and P=-1/4-Bx; direct substitution gives F=0. If B=0, c=0; if B≠0, c=1.
* a=1 is excluded by the marked condition L_1=0.
* a≥2 and c<2a: the unique term of degree 4a is `-(3/16)lc(L)^4*x^(4a)`. Indeed, the possible competing degrees are 2c, 2a+c, c+1, 2a+1, a+2 and 3, all <4a. This is impossible.
* a≥2 and c>2a: the unique term of degree 2c is `(2c-3)lc(P)^2*x^(2c)`. All other possible degrees listed above and 4a are smaller. This is impossible.
* a≥2 and c=2a: with A=lc L and p=lc(P)/A², the highest row is
  `(4a-3)p²+(3/2)p-3/16=0`.
  The discriminant is 3a, which is nonzero. Its two distinct nonzero roots are
  `p=1/(4(2d+1)), 3d²=a`.
  Neither root is excluded by this balance for any integer a≥2. This is exactly UT, not an obstruction to arbitrary a.

These cases include vanishing B and eta, either sign/embedding of d, cancellation of all three degree-4a summands, and all lower actual degrees. The cancellation in the final bullet is essential: treating one of those three summands as the unique leader would give an incorrect classification.

## 2. Coefficient factors and all polynomial-range resonances

Normalize A=1 by x scaling over an algebraic closure and retain b as a weighted parameter. The top equation has the coefficient algebra Q[d]/(3d²-m). It is a quadratic field unless m=3s² for a positive integer s, when it is the product of the two Q factors d=s and d=-s. Passing to geometric points in an algebraic closure covers both embeddings of the irreducible field. No factor can be dropped.

For coefficient P_j, the descending row x^(2m+j) has scalar pivot

```
A_j=2(2m+j-3)p+3/2=(2m+j+6d)/(2(2d+1)).
```

For every m≥4 and every j≥0 this pivot is nonzero. A zero would imply 2m+j=-6d, hence `(2m+j)^2=12m`; but `(2m)^2>12m` for m>3. Thus every coefficient in the polynomial range can be reconstructed without resonance on either factor. At split m=3s² with s≥2, the negative-root resonance lies at `j=-6s(s-1)<0`; the positive-root resonance is also negative. At m=3,d=-1 the constant coefficient j=0 is resonant and must be retained as an equation, as the frozen UTAC reconstruction does.

The high rows j≥2 are independent of B and eta. Eta forcing has degree at most m+2≤2m. B forcing has degree at most 2m+1. Descending reconstruction therefore gives P_j (j≥2) as polynomials in b and the L coefficients over Q(d), with only scalar divisions. The row x^(2m+1), after P1=-B and P0=-b²/4, has the nonzero B pivot `-((4m-3)p+3/4)=-3d/2`. It reconstructs B, and eta=P2. The leftover rows are exactly the frozen K_m equations; a finite reconstruction for each m is not a finite bound on all m.

The weights `(m-2,m-3,...,1,m)` on `(l2,...,l_(m-1),b)` make K_m homogeneous. They do not bound m: both the variable list and the number of residual rows grow. No argument in this note reduces arbitrary m to a fixed finite collection of exact computations.

## 3. A uniform support symmetry consequence

Suppose the nonconstant support of L has gcd g>1. Then L(ζx)=L(x) for every gth root of unity ζ. The transformation

```
P(x) -> P(ζx), B -> ζ B, eta -> ζ² eta, w2 -> ζ³ w2
```

preserves UF and the marked jets. The uniquely reconstructed high coefficients P_j (j≥2) are determined by L, so they are invariant. The nonzero B pivot then forces B invariant as well. Consequently B=0 and P_j=0 whenever j≥2 and g does not divide j. In particular eta=0 when g≥3. Any η≠0 counterexample must have support gcd 1 or 2. This is a uniform partial assertion and does not imply classification of arbitrary support.

## 4. Uniform classification when L has one nonconstant monomial

Suppose L=-b+A*x^m, bA≠0, m≥3. Normalize b=A=1. The symmetry above and high reconstruction give B=eta=0 and

```
L=x^m-1,
P=p*x^(2m)+q*x^m-1/4,
p=1/(4(2d+1)), 3d²=m.
```

Let z=x^m, so theta=m*z*d/dz. Direct expansion of the whole polynomial residual gives

```
[z^4]F = (4m-3)p²+(3/2)p-3/16,
[z^3]F = 6(m-1)pq-(3/2)p+(3/2)q+3/8,
[z^2]F = -mp+(2m-3)q²+(3/2)p-(3/2)q-3/8,
[z^1]F = (3-m)q/2,
[z^0]F = 0.
```

The z³ equation and the top relation give `q=-1/(2(3d+2))`, whose denominator and value are nonzero for integer m≥3. Thus z¹ forces m=3. If d=+1, p=1/12,q=-1/10 and the z² residual is nonzero (equivalently the formula below does not vanish). If d=-1, p=-1/4,q=1/2 and every row vanishes, giving C3. Explicitly, after p and q substitution,

```
[z^2]F = -3(d+1)(9d³+8d²-1)/(4(2d+1)(3d+2)²).
```

This proves that among all polynomials L=-b+A*x^m with m≥3 the only solutions are C3. The expansion was checked by an exact SymPy calculation over Q(m,p,q), followed by substitution m=3d² and p=1/(4(2d+1)); no modular statement is used. The subcase does not cover L with two or more nonzero nonconstant coefficients.

## 5. Precise unresolved step

The leading balance and nonvanishing pivots leave, for every m≥4 and every coefficient-field factor k, the finite ideal K_m in k[l2,...,l_(m-1),b]. The desired weak assertion is `V(K_m)∩{b*eta_m≠0}=empty` for all those m and factors. The stronger assertion is `V(K_m)∩{b≠0}=empty`. Local infinity consistency supplies neither assertion. The new support arguments exclude the one-monomial L subspace uniformly and give eta=0 on support gcd≥3, but they do not eliminate the remaining gcd 1 and 2 cases or establish any uniform degree cutoff.

## 6. Uniform classification of the composed autonomous subcase

Assume b≠0, B=eta=0, m=deg L≥2 and P∈k(L), with P nevertheless a polynomial in x. Because L is a nonconstant polynomial, a reduced rational expression in L with a genuine finite pole cannot be polynomial in x: after passing to an algebraic closure, any finite pole value has a preimage under L, and the coprime numerator stays nonzero there. Consequently P=F(L) with F∈k[L]. The leading-degree result deg P=2m gives deg F=2, so both F and F' are nonzero in characteristic zero.

The whole UF identity gives in k(x)

```
theta L = R(L),
R(z) = [3F(z)^2 -(3/2)z(z+b)F(z)+(3/16)z^3(z+2b)]/[2F(z)F'(z)].
```

Reduce this rational fraction first. The same pole-pullback argument implies R∈k[z], since theta L is polynomial. Moreover theta L has degree m, with nonzero leading coefficient m*lc L. Thus deg R=1 and its slope is m. Evaluation at x=0 gives R(-b)=0, so `theta L=m(L+b)`. Coefficient comparison yields `L=-b+a*x^m` with a≠0.

Normalize b=a=1. Since B=eta=0 already, the sparse calculation of §4 applies also at m=2: P has the form p*x^(2m)+q*x^m-1/4, its x^(3m) row gives q=-1/(2(3d+2))≠0, and the x^m row gives `(3-m)q/2=0`. Hence m=3. The remaining x^6 row excludes d=+1 and leaves d=-1, exactly C3. Thus every nonconstant solution in this composed autonomous subcase is the cubic family.

This proof explicitly allows cancellation in the rational fraction defining R before applying its pole argument. It does not claim that a general polynomial pair P,L satisfies P∈k(L). Establishing that missing composition property for B=eta=0 would finish the classification on that subspace; it would still leave the general B,eta case.
