# AS109 bounded polar conductor / completed-orbit algebraization gate

Date: 2026-08-24T13:18:41Z  
Charged clean-bank basis: `6f2e49e63d74493910fa357a8adc82f0e40d219a`  
Status: **FROZEN PRODUCER / HOSTILE REVIEW REQUIRED**  
Verdict: **`POLAR-CONDUCTOR / UNBOUNDED-GAUGE`**

## 0. Verdict

Let `p` be an odd prime. The rational cotangent control

```text
g=x-x^p,       D=g'=1-p*x^(p-1),       C_p=(g,y/D)
```

is an integral restricted-analytic determinant-one lift of
`(x-x^p,y)` on the closed unit bidisc. Its denominator defines a genuine
algebraic exterior polar divisor

```text
E_p=V(D) over Qpbar.
```

It has `p-1` reduced vertical components, all at source valuation
`-1/(p-1)`, hence outside the closed unit bidisc.

This divisor cannot be erased by polynomial Keller right composition. For
every polynomial `phi=(X,Y)` with `det J(phi)=1`,

```text
gcd(D(X),Y)=1,
Pol(C_p o phi)=div_0(D(X)) != 0.                         (0.1)
```

Polynomial invertibility of `phi` is not needed. Under the narrower genuine
equivalence by polynomial symplectic automorphisms, the divisor is pulled
back isomorphically, so its nonvanishing and its `p-1` geometric components
are invariants.

Now conditionally let `F` be any determinant-one **polynomial** lift of the
same special fibre. In the exact orientation supplied by the reviewed wild
gate, there is a unique restricted-analytic symplectic automorphism
`Phi_F == id mod p` such that

```text
C_p o Phi_F=F.                                           (0.2)
```

Let `kappa_n(F)` be the largest total degree occurring in the canonical
polynomial reduction of `Phi_F` modulo `p^n`. Then

```text
kappa_n(F) -> infinity.                                  (0.3)
```

Indeed, a uniform degree bound would make `Phi_F` polynomial, and (0.2)
would force `D(Phi_1)` to divide `Phi_2`, contradicting (0.1). The same holds
for a uniform bound on the nested canonical support cardinalities.

This is the requested bounded-category invariant: every polynomial point of
the unique completed orbit, if such a point exists, has infinite relative
algebraization conductor from the rational cotangent basepoint. It is not a
proof that the completed orbit contains no polynomial point.

A finite nonlinear coefficient system tests any fixed map/gauge degree caps.
For every fixed pair of caps, it must become empty at some finite `p`-adic
depth. At the first natural cap `D_F=D_phi=p`, depth two survives by the
cotangent truncation and depth three is already empty. Independent exact
row reductions verify the depth-three obstruction at `p=3,5`.

No `p=109` enumeration was performed, and no conclusion about JC2 follows.

## 1. The cotangent basepoint is integral analytic and symplectic

In the integral Tate algebra,

```text
D^(-1)=sum_(j>=0) p^j*x^(j(p-1)) in Z_p<x>              (1.1)
```

because the coefficient valuations tend to infinity. Thus `C_p` is defined
on the entire closed unit bidisc, reduces to `(x-x^p,y)`, and has

```text
det J(C_p)=g'(x) * partial_y(y/D)=D*(1/D)=1.             (1.2)
```

This is an exact characteristic-zero restricted-analytic identity, not only
a congruence at finite depth.

The denominator vanishes algebraically when

```text
alpha^(p-1)=1/p,
```

so `v_p(alpha)=-1/(p-1)`. Therefore its poles are invisible on the integral
unit bidisc but present on algebraic affine space after base extension. The
phrase *exterior polar divisor* means the boundary of the integral affinoid
in this valuation sense; it is not being identified with the projective line
at infinity or with the campaign's `A_infinity` factor.

Since

```text
D'(x)=-p*(p-1)*x^(p-2),       gcd(D,D')=1,               (1.3)
```

`E_p` is reduced. Over `Qpbar` it is the disjoint sum of the `p-1` lines
`x=alpha`.

## 2. Exact orientation of completed right equivalence

The reviewed completed-bidisc theorem says that for any two determinant-one
restricted-analytic lifts `A,B` of the fixed special map there is a unique
near-identity restricted-analytic symplectomorphism `phi` with

```text
A o phi=B.
```

Take `A=C_p` and `B=F`. This gives (0.2), not its reverse. The chain rule
gives `det J(Phi_F)=1`. Uniqueness is in the identity residue branch; it also
makes every reduction `Phi_F mod p^n` canonical. No rational or polynomial
descent is inserted here.

## 3. Polynomial Keller gauges cannot cancel the exterior pole

Work over `K=Qpbar`. Let `phi=(X,Y) in K[x,y]^2` satisfy
`det J(phi)=1`. Then `X` is nonconstant, so `D(X)` is nonconstant.

Suppose an irreducible polynomial `h` divides both `D(X)` and `Y`. Since

```text
D(T)=-p*product_(alpha^(p-1)=1/p) (T-alpha),              (3.1)
```

primality of `(h)` gives `h | X-alpha` for some root `alpha`. Hence the
curve `V(h)` is contained in the fibre

```text
phi^(-1)(alpha,0).                                       (3.2)
```

But `det J(phi)=1` makes `phi` etale, hence quasi-finite, and a quasi-finite
morphism has no curve in a point fibre. Equivalently, at the generic point
of `V(h)`, both `dX` and `dY` are multiples of `dh` (or one vanishes if the
factor has multiplicity), so their wedge and therefore the Jacobian vanish
modulo `h`, contradicting `det J(phi)=1`. This factorwise argument handles a
reducible pullback cleanly and also shows each pullback component is reduced.

Consequently

```text
gcd(D(X),Y)=1.                                           (3.3)
```

The second coordinate of `C_p o phi` is the reduced rational function

```text
Y/D(X),                                                  (3.4)
```

so it has a nonempty pole divisor. If `phi` is a polynomial symplectic
automorphism, (3.4) says precisely

```text
Pol(C_p o phi)=phi^* E_p,                                (3.5)
```

and the inverse automorphism makes this a genuine equivalence invariant. The
stronger no-cancellation statement (3.3) remains valid even if one refuses to
assume that every polynomial Keller map is invertible.

## 4. Canonical finite conductors and unboundedness

Write

```text
Phi_F=(A,B) in Z_p<x,y>^2.
```

For a restricted series `H=sum c_ij x^i y^j`, its reduction modulo `p^n`
has finite support. Define

```text
deg_n(H)=max {i+j : v_p(c_ij)<n},
kappa_n(F)=max(deg_n(A),deg_n(B)).                        (4.1)
```

These are finite, exactly computable invariants of the unique identity-branch
gauge, and they are nondecreasing in `n`.

If `kappa_n(F)<=B_0` for every `n`, then every coefficient of `A,B` above
degree `B_0` is divisible by every power of `p`, hence is zero. Thus `Phi_F`
is a polynomial map. From (0.2),

```text
F_2=B/D(A) in Q_p(x,y).                                  (4.2)
```

Polynomiality of `F_2` forces `D(A)|B`, while
`det J(Phi_F)=1` and Section 3 force `gcd(D(A),B)=1`. Since `D(A)` is
nonconstant, this is impossible. Therefore (0.3) holds.

The canonical supports modulo `p^n` are nested. A uniform bound on their
cardinalities also makes their union finite and gives the same contradiction.
A common fixed finite support is stronger still. By contrast, coefficient
integrality or Gauss norm at most one is automatic in `Z_p<x,y>` and does not
control algebraization: the infinite series in (1.1) is the basic example.
This theorem proves support/degree escape, not a rate or coefficient-height
lower bound.

## 5. A genuinely finite bounded coefficient gate

Let `R_n=Z/p^n` and

```text
S_n=sum_(j=0)^(n-1) p^j*x^(j(p-1)),
C_(p,n)=(g,y*S_n) in R_n[x,y]^2.                          (5.1)
```

The exact identity

```text
(1-p*x^(p-1))*S_n=1-p^n*x^(n(p-1))                       (5.2)
```

gives `det J(C_(p,n))=1` in `R_n[x,y]`.

For fixed total-degree caps `(D_F,D_phi)`, define
`B_(p,n)(D_F,D_phi)` to be the coefficient system for maps
`phi=(X,Y)` over `R_n` satisfying

```text
X=x, Y=y mod p,                det J(X,Y)=1,
deg(X),deg(Y)<=D_phi,
deg(g(X)),deg(Y*S_n(X))<=D_F.                              (5.3)
```

These are finitely many explicit polynomial congruences in coefficients on
total-degree simplices. There is no arbitrary rectangular support choice.
When a point exists, `F=C_(p,n) o phi` is automatically a determinant-one
lift at that depth.

For every fixed `(D_F,D_phi)`, (5.3) is empty for at least one finite `n`.
Otherwise its finite solution sets at all levels, linked by reduction, form
an infinite finitely branching tree. Konig's lemma gives a compatible path.
The inverse limits `X,Y` are polynomials of degree at most `D_phi`, and the
compositions have degree at most `D_F`; all identities hold over `Z_p`.
This produces a polynomial Keller `phi` for which `C_p o phi` is polynomial,
contradicting Section 3.

Thus (5.3) is a falsifiable finite search for any announced caps. This is an
existence-of-a-finite-obstruction theorem; it does not give a uniform formula
for the first failing depth at arbitrary caps.

Digit lifting is linear once a depth-`n` point is fixed: append
`p^n(r,s)` and expand modulo `p^(n+1)`. The new equations are linear over
`F_p` in the fresh digit coefficients. The base search may be nonlinear, so
both layers must be retained in a serious compiler.

## 6. First nonlinear cap: `D_F=D_phi=p`

Depth two survives with `phi=id`:

```text
C_(p,2)=(x-x^p, y+p*x^(p-1)y),       degree=p.             (6.1)
```

At depth three, write the general bounded gauge as

```text
X=x+p*r+p^2*r2,
Y=y+p*s+p^2*s2,                       deg(r,s,r2,s2)<=p.    (6.2)
```

For every odd `p`, exact binomial expansion modulo `p^3` gives

```text
g(X)=g(x)+p*r+p^2*(r2-x^(p-1)r),                         (6.3)

Y*S_3(X)=y+p*(s+x^(p-1)y)
 +p^2*(s2+x^(p-1)s+(p-1)x^(p-2)r*y+x^(2p-2)y).           (6.4)
```

Terms with at least two copies of `p*r` in `X^p` have valuation at least
three; this uses oddness of `p` and is exact also at `p=3`.

The degree-`p` cap in (6.3) forces every monomial of `r` of total degree at
least two to vanish: multiplication by `x^(p-1)` would otherwise create a
unique term of degree greater than `p` at the `p^2` digit. In particular,

```text
[x^p]r=0.                                                (6.5)
```

The first determinant digit is

```text
r_x+s_y=0.                                               (6.6)
```

Taking the coefficient of `x^(p-1)` in (6.6), characteristic `p` kills the
only possible `r_x` source `p*[x^p]r`; hence

```text
[x^(p-1)y]s=0.                                           (6.7)
```

Finally, after dividing its `p^2` digit by `p^2`, the coefficient of the
forbidden degree-`2p-1` monomial `x^(2p-2)y` in (6.4) is

```text
[x^(p-1)y]s + (p-1)[x^p]r + 1 = 1.                       (6.8)
```

Neither `s2` nor `r2` can reach that degree under the cap. Thus (6.8) cannot
vanish and

```text
B_(p,3)(p,p)=empty                                      (6.9)
```

for every odd prime `p`. This is a nonlinear bounded-gauge statement: the
full gauge in (6.2) was allowed. The contradiction happens in a necessary
linear digit subsystem, which the replay row-reduces independently.

## 7. Exact `p=3,5` controls

The frozen standard-library replay returns:

| `p` | exterior components | exterior valuation | `n=2` degree | forbidden `n=3` monomial | variables in necessary digit system | coefficient / augmented rank | verdict |
|---:|---:|---:|---:|---:|---:|---:|---|
| 3 | 2 | `-1/2` | 3 | `x^4 y` | 20 | `12 / 13` | inconsistent |
| 5 | 4 | `-1/4` | 5 | `x^8 y` | 42 | `32 / 33` | inconsistent |

It also checks `gcd(D,D')=1` over the rationals and the exact cotangent
identity through depths `2,3,4`. The total degrees of the displayed control
are

```text
p=3: 3,5,7;             p=5: 5,9,13.                    (7.1)
```

The replay is a verification of the registered structural formulas, not a
sample-based proof of the all-odd-prime theorem.

## 8. Interpretation and next gate

Promote only the following:

1. the completed orbit has a nontrivial polynomial-gauge stratification even
   though unrestricted analytic gauge is transitive;
2. every hypothetical polynomial lift has unbounded canonical gauge degree
   and support relative to `C_p`;
3. every fixed simultaneous map/gauge degree cap is killed at some finite
   Witt depth;
4. the first natural simultaneous cap `p` dies exactly at depth three.

Do **not** promote this to nonexistence of a polynomial lift. A polynomial
lift may have a unique analytic gauge whose truncation degrees grow without
bound; (0.3) says it must. The theorem also does not identify `E_p` with
`A_infinity`, prove rational deck descent, bound global generic degree beyond
the reviewed `d>=p`, or perform a `p=109` calculation.

The sharp successor is quantitative: derive a lower growth law for
`kappa_n(F)` from a fixed degree/support bound on `F`, or eliminate
`B_(p,n)(D_F,D_phi)` for increasing intrinsic total-degree caps using
digit-by-digit linear lifting plus exact nonlinear base components. A second,
independent direction is to compare the exterior valuation
`-1/(p-1)` with the valued initial systems governing `A_infinity`; that
comparison is not automatic and must be proved before using the same word
*boundary* for both.

## 9. Replay and provenance

Frozen artifacts:

```text
PREREGISTRATION.md  9e291d17a1d8f2fe83c8ebad9f7a4d799304398629a794d790c4fe81bfc0ee6a
replay.py           26ead3001ce1e9bf939e47a4e9e529785561357dc9e95479823b3347841aca85
replay.stdout.json  0b0ad8c2d0c05d0628a1efb3853f72be5f4234dbfbf81ab596cbf632066b1d99
```

Final repository-location replay completed at `2026-08-24T13:29:37Z` with all
assertions passing. Consumed frozen inputs, read without modification:

```text
c7ad3660c136bbee7105e786cc8b717d025534b67ac63cababb33c4b6de29e7c  xmodel/as109-wild-symplectic-conductor-gate-20260824.md
a59c7ccbf39971ad7ab47f8e865926c93e4ac9d46305be076f4bd0193b2b1a9a  xmodel/as109-wild-symplectic-conductor-review-grok-20260824.md
c38d0209b8bc4b4d2ad4fd3d371966fac5441e8e10c029d837647b6797fb8eb2  xmodel/witt-tate-control-20260824.md
b3eae1f5a1420cec99bb8d75c8b0cddfd7a2db1e2027032e3f0be3b4fc6735a2  xmodel/review-witt-tate-control-claude.md
f1cf4991e92e502459ca6c61a3cb4d0e346a65e6221890c8c64a808ec2e3b64b  xmodel/as109-ainfinity-deck-descent-gate-20260824.md
a86b694364ebaf28a3890b7bd73aafb5057ddae100172db78a9490e7a2b55d76  xmodel/as109-ainfinity-review-grok-20260824.md
```

The producer used no network call, external solver, AWS instance, or
`p=109` computation. All work remained in a private temporary directory
pending the coordinator's clean-bank signal.
