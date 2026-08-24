# AS wild-symplectic bounded polar-conductor gate — preregistration

Date: 2026-08-24T13:16:59Z  
Scope: structural odd-prime proof plus exact controls at `p=3,5`; no
`p=109` enumeration, no AWS, no arbitrary exponent rectangle, and no JC2
inference. This froze the final evidence run after exploratory derivation in
a private temporary directory; only the post-freeze rerun and hashes count as
replay evidence. Materialization occurred only after the coordinator's clean
bank signal.

## Basepoint and orientation

For an odd prime `p`, put

```text
g=x-x^p,             D=g'=1-p*x^(p-1),
C_p=(g, y/D) in Z_p<x,y>^2.
```

The completed-bidisc theorem is consumed in the following orientation. For a
hypothetical determinant-one polynomial lift `F` of `(x-x^p,y)`, there is a
unique restricted-analytic symplectic automorphism `Phi_F == id mod p` with

```text
C_p o Phi_F = F.
```

## Registered invariant

Over `Qpbar`, define the exterior polar conductor of a rational representative
to be its effective height-one polar divisor on algebraic `A^2`. For `C_p`
this must be

```text
Pol(C_p)=V(D)=sum_(alpha^(p-1)=1/p) V(x-alpha).
```

Every component is required to be reduced and to have
`v_p(alpha)=-1/(p-1)`, so it lies outside the integral closed unit bidisc. It
is an algebraic exterior divisor, not the usual projective line at infinity.

For a polynomial map `phi=(X,Y)` with `det J(phi)=1`, test the structural
no-cancellation claim

```text
gcd(D(X),Y)=1.
```

The registered proof must treat each irreducible factor after base change:
a common factor would be a curve contained in a fibre `phi^(-1)(alpha,0)`,
contradicting etaleness/quasi-finiteness (or directly forcing the Jacobian to
vanish along that factor). Under polynomial symplectic automorphism right
equivalence, `Pol` must pull back and nonvanishing must be invariant. The
no-cancellation lemma is deliberately stronger: polynomial invertibility of
`phi` is not assumed.

Define the canonical finite depth conductor

```text
kappa_n(F)=max degree of the canonical polynomial reductions
           of the two coordinates of Phi_F modulo p^n.
```

The structural target is `kappa_n(F) -> infinity` for every hypothetical
polynomial `F`. A uniform degree bound, or a uniform bound on the nested
canonical support cardinalities, would make `Phi_F` polynomial. Then
`C_p o Phi_F=F` would require `D(Phi_1) | Phi_2`, contradicting the registered
no-cancellation lemma. Coefficient integrality alone is not a support bound.

## Finite falsification system

Over `R_n=Z/p^n`, put

```text
S_n=sum_(j=0)^(n-1) p^j*x^(j(p-1)),
C_(p,n)=(g,y*S_n).
```

For total-degree caps `(D_F,D_phi)`, the bounded system consists of polynomial
`phi=(X,Y)` over `R_n` satisfying

```text
phi == id mod p,          det J(phi)=1,
degree(phi)<=D_phi,       degree(C_(p,n) o phi)<=D_F.
```

This is a finite nonlinear coefficient system on total-degree simplices, not
an arbitrary rectangle. If it is nonempty at every depth for fixed caps,
the finite-tree lemma must produce compatible bounded polynomial limits,
contradicting the polar conductor. Hence every fixed pair of caps must fail at
some finite depth.

## Exact controls

Run only `p=3,5` and depths `2,3,4` for the cotangent identity. For the first
nonlinear gate fix

```text
D_F=D_phi=p.
```

Required outcomes:

1. `n=2` is nonempty via `phi=id`, since `degree C_(p,2)=p`.
2. `n=3` is empty. Write
   `X=x+p*r+p^2*r2`, `Y=y+p*s+p^2*s2`, with every digit of degree at most
   `p`. Expansion modulo `p^3` must show that the first coordinate degree cap
   kills every coefficient of `r` of degree at least two; first-order
   symplecticity gives `r_x+s_y=0`; and the forbidden coefficient of
   `x^(2p-2)y` in the second coordinate remains `p^2` times one.
3. Independently row-reduce those necessary digit equations over `F_p`; the
   augmented system must be inconsistent for each of `p=3,5`.

## Stop outcomes

- `POLAR-CONDUCTOR / UNBOUNDED-GAUGE`: all structural claims and both exact
  controls pass. This is a bounded-category theorem only; it does not exclude
  a polynomial lift.
- `PULLBACK-CANCELLATION`: a determinant-one polynomial right map cancels the
  conductor. Freeze the smallest factor.
- `BOUNDED-D3-SURVIVOR`: the registered `D=p,n=3` system is not inconsistent.
  Freeze it as the next motif; do not extrapolate to `p=109`.

No outcome proves or disproves JC2.
