# Whole-polynomial structural lemmas for UF

Source scope: only the mechanically verified frozen inputs in
`/tmp/jc2-lane.fImwPK/inputs` were consumed. All assertions below are over an
algebraically closed field `k` of characteristic zero. These lemmas do **not**
prove the requested classification for arbitrary polynomial `L`.

Write `theta=x d/dx` and

```
F=(theta-3)(P^2)+((3/2)L(L+b)-Bx)P
  -(3/16)L^2(L(L+2b)-4Bx)+eta*x^2*(bL/2+Bx).
```

The marked jets are `L(0)=-b`, `L_1=0`, `P_0=-b^2/4`, `P_1=-B`,
`P_2=eta`; assume `b != 0`. For `m=deg L>=2`, whole-polynomial leading balance
gives `deg P=2m`, and after `lc L=1`,

```
(4m-3)p^2+(3/2)p-3/16=0,
p=1/(4(2d+1)),  3d^2=m.
```

Both roots exist and are distinct for every integer `m>=2`. This leading
equation is consistent at every degree; it supplies no degree bound.

## 1. Same-branch uniqueness, and inheritance of a monomial symmetry

**Lemma (including the low parameters).** If `m>=2`, fixed `L,b` admit two
marked polynomial solutions `(P,B,eta)` and `(Q,C,epsilon)` with the same
leading coefficient `p`, then the entire tuples are equal.

Proof: subtract the two UF equations. With `D=P-Q`, `deltaB=B-C`,
`deltaeta=eta-epsilon`,

```
(theta-3)((P+Q)D)+(3/2)L(L+b)D-x(BP-CQ)
  +(3/4)deltaB*x*L^2+(b/2)deltaeta*x^2*L
  +(B*eta-C*epsilon)*x^3=0.
```

If `k=deg D>=2`, necessarily `k<2m`. The parameter-difference terms have
degree at most `2m+1`; the eta term has degree at most `m+2<=2m`. Hence
the row of degree `2m+k` has coefficient

```
A_k=2(2m+k-3)p+3/2=(2m+k+6d)/(2(2d+1)).
```

This is nonzero on every coefficient-field factor. Its vanishing would imply
`(2m+k)^2=12m`, whereas `(2m+k)^2>12m` for `m>=2,k>=2`. Thus `deg D<=1`.
The marked jets give `D=-deltaB*x`, `deltaeta=0`. Now the row of degree
`2m+1` has coefficient

```
-deltaB*((4m-3)p+3/4)=-(3d/2)*deltaB,
```

so `deltaB=0` and `D=0`. Undoing leading normalization proves the general
case. No constant-term resonance is divided out in this argument.

**Corollary.** If `m>=2` and `L` belongs to `k[x^j]`, then every marked
polynomial solution `P` belongs to `k[x^j]` as well. Moreover `B=0` if
`j>=2`, and `eta=0` if `j>=3`. Indeed, for every `j`th root of unity `zeta`,
the substitution `x -> zeta*x` sends the solution tuple to
`(P(zeta*x),zeta*B,zeta^2*eta)` with the same `L`. Because `j` divides `m`
and `deg P=2m`, the transformed `P` has the same leading coefficient. The
lemma makes the entire tuple invariant. This proves each claim.

This corollary is a whole-polynomial statement. It does not assume that a
series parameter of weight three vanishes; its vanishing, when `j` does
not divide three, follows from the proved symmetry.

## 2. Complete finite-root multiplicity table when B=eta=0

Set

```
H=2 theta(P)-3P+(3/2)L(L+b).
```

Then UF is the exact factorization

```
P*H=(3/16)L^3(L+2b).                         (M)
```

Here `deg H=2m`: with normalized `lc L=1`, its leading coefficient is

```
(4m-3)p+3/2=3(2d+1)/4 != 0.
```

Every zero of `P` is therefore a zero of `L` or `L+2b`. Such a zero `r`
is nonzero, since `L(0)=-b`, `P(0)=-b^2/4`. In a local coordinate `z=x-r`,
Euler differentiation of a zero of multiplicity `k` lowers the order by one.

The exhaustive table is:

| position | given multiplicity | allowed `ord_r P` | resulting `ord_r H` |
|---|---:|---:|---:|
| `L(r)=0` | `ord_r L=s>=1` | `0` | `3s` |
| `L(r)=0` | `ord_r L=s>=1` | `s+1` | `2s-1` |
| `L(r)=0` | `ord_r L=s>=1` | `2s` | `s` |
| `L(r)=-2b` | `ord_r(L+2b)=t>=1` | `0` | `t` |
| `L(r)=-2b` | `ord_r(L+2b)=t>=1` | `1` | `t-1` |
| `L(r)=-2b` | `ord_r(L+2b)=t>=1` | `t` | `0` |

Coincident entries (`s=1` or `t=1`) describe the same alternative once.
These are necessary conditions, not assertions of existence for every row.

Proof for a common root `P=L=0`: put `k=ord_r P>0`. In UF, the three
potentially lowest orders are `2k-1`, `k+s`, `3s`. At least two must attain
the minimum. If `k<=s`, the first is uniquely smallest. If
`s+1<k<2s`, the second is uniquely smallest. If `k>2s`, the third is uniquely
smallest. Thus `k=s+1` or `k=2s`, with the simultaneous three-way equality
when `s=1`. Formula (M) gives the H orders.

At a common root `P=0,L=-2b`, the corresponding orders are `2k-1`, `k`,
`t`, since `(3/2)L(L+b)` is a unit there. For `k>=2`, the derivative order
is strictly larger than `k`, so `k=t`. The remaining possibility is `k=1`.
Unshared roots give the zero-multiplicity rows directly from (M).

**Important audit.** Squarefreeness of `L` alone does not imply `L^2 | P`:
the first row of the table allows a root of `L` to be absorbed entirely by
`H`. Any argument forgetting this row is invalid.

**Conditional classification.** If additionally `gcd(P,L+2b)=1`, all roots
of `P` lie on `L`, and the table gives `P | L^2`. Equal degrees then imply
`P=cL^2`, and the constant jets give `c=-1/4`. Direct substitution gives
`theta L=3(L+b)`. Hence `L=-b+a*x^3` and `P=-L^2/4`.

Consequently a noncubic solution on `B=eta=0` must have a common root of
`P` and `L+2b`. The root-allocation alternatives in the table remain genuine
unexcluded algebraic alternatives. The table does not classify them globally.

## 3. Uniform exclusion of every nontrivial pure-power shape

**Theorem.** Suppose `B=eta=0`, `b != 0`, and

```
L=-b*(1+a*x^j)^s,   a != 0,   j>=1,   s>=2,
```

with the marked jets and actual degree `m=s*j>=4`. There is no polynomial
solution `P` of UF.

First normalize `b=1` using `L/b,P/b^2`. Put `f=1+a*x^j`. The symmetry
corollary proves `P in k[f]`, with degree `2s` as a polynomial in `f`.
Also `theta f=j(f-1)`. The only possible finite roots of `P(f)` are `f=0`
and the `s` distinct roots of `f^s=2`. At the latter, `L+2` has simple
roots, so each can occur in `P` with multiplicity at most one. A factor at
`f=0` is indispensable because `2s>s`; its allowed multiplicities are
`s+1` and `2s` by the table. The preimages in `x` of these `f` values are
all nonzero and unramified, so multiplicity in `f` agrees with multiplicity
in `x` at every preimage.

If the multiplicity at zero is `2s`, then `P` is a scalar multiple of
`f^(2s)`, and the constant jet makes `P=-L^2/4`. UF forces
`theta L=3(L+1)`, so

```
s*j*f^(s-1)=3*(1+f+...+f^(s-1))
```

after dividing by the nonzero polynomial `f-1`. The constant coefficients
are unequal for `s>=2`, a contradiction.

Otherwise the multiplicity is `s+1`, leaving precisely `s-1` simple roots
among those of `f^s=2`. Thus exactly one such root `r` is omitted and

```
r^s=2,
P=k*f^(s+1)*(f^s-2)/(f-r),
k=(1-r)/4 != 0,                              (P*)
```

where the last equality follows from `P(f=1)=-1/4`. This factor allocation
is exhaustive: it uses the entire degree `2s`, with no roots omitted from
consideration.

Equation (M), expressed in `f`, now reads

```
2j(f-1) P_f -3P +(3/2)f^s(f^s-1)
       =(3/(16k))*f^(2s-1)*(f-r).            (H*)
```

The coefficient of `f^(s+1)` in (P*) is `2k/r`. Hence the coefficient of
`f^s` on the left of (H*) is

```
-4j(s+1)k/r -3/2.
```

The right side has order `2s-1>s`, so this coefficient must vanish. Using
`k=(1-r)/4` gives

```
j=3r/(2(s+1)(r-1)).                          (J)
```

Because `j,s` are integers, (J) forces `r` to be rational; the possible
zero denominator after solving for `r` gives `0=-3`, so it is not an
exception. But `r^s=2` has no rational root for `s>=2` (Eisenstein at 2,
or the elementary numerator/denominator prime-valuation argument). This
is a contradiction. The proof is independent of the factor of `3d^2-m`.

The required jet `L_1=0` in fact imposes `j>=2` here, but the proof only
uses the stated `m>=4`; the strengthened same-branch lemma itself holds
already for `m>=2`. If `j>=3`, the assumptions `B=eta=0` of the pure-power
theorem follow automatically from the corollary.

## 4. A second uniform structured family: quadratic in x^j

**Theorem.** For every integer `j>=2`, there is no marked polynomial
solution with `B=eta=0`, `b != 0`, and

```
L=-b+A*x^j+C*x^(2j),   C != 0.
```

For `j>=3` the assumptions `B=eta=0` are automatic by section 1. For
`j=2`, removing the eta assumption is exactly an actual-degree-four
subcase and is excluded by the frozen Utac section 4 exact-Q theorem.
Thus, after consuming that precisely bounded theorem, the displayed
L shapes are all excluded without assumptions on B or eta.

Proof: normalize `b=1` by the stated UF map and normalize the top
coefficient by an `x` scaling. Put `t=x^j`. Section 1 gives `P in k[t]`,
`deg_t P=4`. The case `A=0` is the monomial shape `L=-1+t^2`.
Its inherited symmetry makes `P=-1/4+v*t^2+w*t^4`; in `y=t^2`, the
rows of degrees one, three, two force successively `v=0`, `w=1/4`,
and `0=-2j/4`. Thus `A != 0` for any possible solution.

When `j != 3`, row t of UF is `-(j-3)P_t/2=0`, so write

```
L=-1+A*t+t^2,
P=-1/4+v*t^2+w*t^3+z*t^4.
```

The Euler derivation on these polynomials is `j*t*d/dt`. Rows 2, 3,
and 4 give the exact reconstruction

```
v=-3A^2/(4(2j-3)),
w=A*(A^2*j-2j+3)/(2(j-1)(2j-3)),
z=-3*(2A^4*j^3-4A^4*j^2-12A^2*j^3+34A^2*j^2
       -24A^2*j+4j^3-16j^2+21j-9)
       /(4(j-1)(2j-3)^2(4j-3)).
```

The low-row pivot exceptions are `j=3` for `P_t`, `j=3/2` for v,
`j=1` for w, and `j=3/4` for z. Among integers `j>=2`, only `j=3`
occurs; it is handled below with its free coefficient retained.

Substitute these rational functions into rows 5, 6, and 7. Divide the
odd rows by the explicitly nonzero A, put `U=A^2`, and take primitive
integer numerators. This defines polynomials `Q5,Q6,Q7 in Q[j,U]`;
the map is justified because the remaining powers of A are all even.
The driver `structure-quadratic.py` declares this construction directly
from UF and checks the following exact resultants, using U as the
elimination variable:

```
resultant_U(Q5,Q6)=-D(j)*C1(j),
resultant_U(Q5,Q7)= D(j)*C2(j),
D(j)=j^8*(j-1)^2*(2j-3)^6*(4j-3)^2,
C1=6272j^5-12670j^4+243j^3+7505j^2+1409j-3267,
C2=1792j^5-890j^4-8547j^3+15481j^2-11687j+3267,
resultant_j(C1,C2)=669531824097600026204667144843558912 != 0.
```

Only nonzero rational constants are removed when primitive numerators
are chosen. Every rational denominator is a product of powers of the
listed nonzero pivot factors. The other branch operation, division by A,
was explicitly separated from `A=0`. Resultants supply necessary common
root conditions even at parameter values where a leading coefficient
in U drops; no fixed U degree is assumed to persist after specialization.
Since `D(j) != 0` at every integer `j>=2`, the two resultants cannot
both vanish. This excludes every nonresonant integer j simultaneously,
not by checking a bounded list of j values.

At `j=3`, retain `q=P_t`. Rows 2, 3, and 4 reconstruct

```
v=(-A^2-4Aq+8q^2)/4,
w=(A^3-20Aq^2-A+32q^3-2q)/4,
z=(-A^4+20A^3q+28A^2q^2+5A^2-368Aq^3+2Aq
       +480q^4-32q^2-1)/12.
```

Rows 5 through 8 now form an explicit ideal in `Q[A,q]`. The emitted
`structure-quadratic.sing` declares that ring with generator order
`(A,q)` and `dp`, takes the primitive row numerators, and computes the
standard basis `(1)`. The independent Sympy calculation over Q gives
the same unit ideal. The exact cubic substitution is a nonempty
control in the same Singular replay; it gives residual zero. The
resultant identities and both unit-basis calculations were actually
executed; `structure-quadratic-check.txt` records their compact output.

The only invocation of a finite-index result to remove hypotheses is
the explicit actual-degree-four case `j=2`; all integer `j>=3` are
covered by the parameter-j calculation plus its single justified
resonance. This does not give a cutoff for arbitrary L.

## 5. What remains

The same-branch lemma and the two structured-family theorems do not bound the degree of an
arbitrary polynomial `L`, do not prove `eta=0`, and do not dispose of the
common-root alternatives in section 2. In particular no whole-ray theorem
is promoted from these lemmas. The remaining requested assertion is still
the universal no-zero statement for `K_m` on `b*eta_m != 0`, for every
actual `m>=4` and every coefficient-field factor.
