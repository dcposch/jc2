# Coordinator integration: affine-linear cubic blocks are closed

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `a619157b73c1dee1ca0599db47321ffd7588d748`  
Lifecycle: **BINDING INTEGRATION / BASIS-DEPENDENT AFFINE-LINEAR SCOPE**

## 0. Disposition and custody

The bounded different-model rerun by Fable 5 returned
`CONFIRM_WITH_CORRECTIONS` on the exact load-bearing chain.  Its sandboxed
receipt has exit code zero and pins unchanged prompt, adapter, launcher,
Seatbelt profile, validator, fallacy appendix, and composed model-prompt
hashes.  The raw reviewed body is

```text
9d131643ed51c13468e2fb2414f33923c481c919de78002da1e991479b244c76
  xmodel/bd-fix3-affine-linear-log-closure-bounded-hostile-review-fable5-20260830.md
```

and the sealed full-file SHA-256 is
`04a401582d4b242efe499c43a59aa0939d29f9c2a65997d84131db701bc76b46`.
The review consumes the binding structure sandwich
`ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778`,
binding Galois/nonmonogenicity integration
`f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8`,
and binding log theorem
`ff25ba27388c02698013483e2e5537f18ed39e918e5cb0cb4c099a75ef42f298`.

The producer's residual-control sections on almost-surjectivity, its explicit
non-Keller model, and any general nonlinear corollary were deliberately
outside the bounded review and remain nonbinding.

## 1. Maximum theorem

> **AL3-CLOSED.**  Let `F=(f,g)` be a hypothetical noninvertible plane Keller
> map and suppose it has a proper cubic intermediate field
> `C(f,g) < K < C(x,y)`.  Let `B_K` be the integral closure of
> `A=C[f,g]` in `K`.  If there exists a global `A`-basis of the trace-zero
> module of `B_K` in which all four Miranda coefficients `a,b,c,d` have
> total degree at most one in `(f,g)`, then contradiction.

Equivalently, no proper cubic intermediate block of a plane Keller map has
affine-linear Miranda coefficients in any fixed global trace-zero basis.
The hypothesis is existential in a basis choice; no invariance of coefficient
degree under basis change is asserted.

## 2. Exact algebraic reduction

Normality of `B_K`, miracle flatness over `A=C[u,v]`, trace splitting, and
Quillen--Suslin give

```text
B_K=A direct-sum E,          E=A*z direct-sum A*w.
```

In any trace-zero basis the multiplication table is

```text
z^2 = 2(a^2-bd) + a*z + b*w,
z*w = -(ad-bc) - d*z - a*w,
w^2 = 2(d^2-ac) + c*z + d*w,
```

with binary cubic

```text
Phi(X,Y)=bX^3-3aX^2Y+3dXY^2-cY^3.
```

For `t=r*z+s*w`, the determinant of `(t,t^2)` in `E` is `Phi(r,s)`.
Consequently

```text
B_K is monogenic over A
  iff Phi(r,s) is in C^* for some r,s in A.            (2.1)
```

Binding nonmonogenicity forbids (2.1).

Write the affine-linear cubic as

```text
Phi=P0+u*P1+v*P2
```

with fixed binary cubics `Pj`.

## 3. Common coefficient zero

The common zero set of `a,b,c,d` is an affine subspace.  It cannot be all of
`A^2`, since the generic algebra would not be a field.  It cannot contain a
line: at the generic DVR of such a line, the Miranda special fibre would be

```text
kappa[z,w]/(z,w)^2,
```

whose two-dimensional radical has square zero.  Normality makes the localized
rank-three algebra a semilocal Dedekind domain.  Locality of that special
fibre leaves one prime: residue degree three would have zero radical, whereas
total ramification gives `DVR/(t^3)`, whose radical has nonzero square.  Both
contradict the displayed fibre.  Thus a nonempty common zero is isolated.

After translation it is the origin and `Phi=uP1+vP2`.  Giving
`u,v,z,w` degree one makes `B_K` a graded domain with Hilbert function
`3n+1`.  Its Proj is the twisted cubic; hence

```text
B_K = direct-sum_(n>=0) H^0(P^1,O(3n)).               (3.1)
```

The incidence surface is literally `Tot O_P1(-3)` with

```text
(u,v)=tau*(-P2,P1),                                   (3.2)
```

and its affinization is `Spec B_K`, contracting exactly the zero section.
Therefore `O(Y)^*=C^*` and `Cl(Y)=Z/3`.  The nonempty ramification support
on `Y` gives a nonzero kernel from its free boundary-divisor group to the
finite class group, hence a nonconstant unit on the etale complement.  The
dominant first leg pulls that unit to a nowhere-zero polynomial on `A^2`, a
contradiction.  This closes the common-zero case.

## 4. No common coefficient zero

A common zero of `P0,P1,P2` would give a nonzero trace-zero element of degree
at most two in the cubic field, impossible.  If `P1,P2` have a common zero,
then `P0` is nonzero there and `Phi` represents a scalar unit, contradicting
(2.1).  Thus `(P1,P2)` is basepoint-free, including the cases in which one
was hypothesized identically zero, and

```text
rho=[P1:P2]:P^1 -> P^1
```

has degree three and nonzero Wronskian.

The review supplies the missing scheme bridge: the Miranda presentation is
isomorphic over `A^2` to

```text
Y={P0+uP1+vP2=0} subset A^2 times P^1.                (4.1)
```

Fibrewise determinant checks cover every coefficient degeneration.  The
projection `q:Y->P^1` is therefore a smooth affine-line torsor under
`O(-3)`, with

```text
O(Y)^*=C^*,             Cl(Y)=Pic(Y)=Z.               (4.2)
```

If the ramification support `R` has at least two irreducible components,
localization maps a free group of rank at least two to `Z`; its nonzero
kernel again gives a forbidden unit on `U=Y-R`.

Suppose instead that `R` is irreducible.  The equations
`Phi=d_(P1)Phi=0` are a two-by-two affine-linear system in `(u,v)`.  Away
from `Crit(rho)` they give one graph point.  At a critical direction their
matrix has rank one, so compatibility would give the entire vertical fibre,
a second ramification component; irreducibility forces inconsistency.
Purity and the binding simple-transposition input give the reduced support

```text
R isomorphic to P^1 minus Crit(rho).                  (4.3)
```

Riemann--Hurwitz for the degree-three map `rho` gives at least two distinct
critical directions.  In the ruled completion of the torsor, the closure of
`R` is a section meeting the infinity section exactly over those directions.
The binding log theorem therefore forbids any dominant `A^2->U`.  The
binding first-leg sandwich supplies exactly such a dominant map, closing the
last case.

## 5. Scope firewall

`AL3-CLOSED` says nothing about Miranda coefficients of degree at least two,
about the minimum achievable coefficient degree across all bases, or about
proper blocks of degree other than three.  It neither proves primitivity nor
asserts that any intermediate field exists.  It constructs no polynomial
map or counterexample and proves no unconditional JC2 statement.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6641`.
- Body SHA-256:
  `14d47db4730ffd3c06168bc0ada4dd7584df397fdc871a72e701fbd576a89275`.
- Frozen basis: `a619157b73c1dee1ca0599db47321ffd7588d748`.
