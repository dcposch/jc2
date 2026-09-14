# Ni HC4 / JC2 interface audit

2026-09-06. Astra. Basis `0d39df3c9fd69c939a8420c54d03228b9077777d`.
Bounded desk audit; PRODUCER-CHECKED, not a promotion of the external paper.

## Disposition

**NO_NEW_MECHANISM for unrestricted JC2.** The arbitrary-P assertion covers
an unbounded-degree class of potentials, but its direct pairing application
requires a plane component of degree at most two. Removing that restriction
on the pairing subclass is exactly the unresolved plane Jacobian problem;
the leading coefficient test becomes an identity there.

There is a useful limited strengthening: the nonzero quadratic-direction
branch works for arbitrary Q as well. It does not apply to the standard
pairing potential, whose quadratic-direction coefficient is zero. A small
Keller example below disproves the proposed repair by simply adding a
nonzero quadratic term.

## Primary paper and checked scope

I read the entire versioned primary HTML, from introduction through all
proofs, discussion and references:
[Zixiang Ni, arXiv:2608.14217v1](https://arxiv.org/html/2608.14217v1).
The abstract and submission record were also checked at the version's arXiv
entry. No conclusion is drawn from the source-size metadata or crosslisting.

The paper proves its quartic claim by separating ternary, binary and unary
cone tops, then obtaining a direction affine-linear in the cubic part.
Its Proposition 6.1 addresses `P(X)+u*Q(X)+a*u^2`, with arbitrary P and
quadratic-or-lower Q. For a=0 it classifies the constant matrix Hess Q;
rank two is excluded, rank one admits an explicit inverse, and rank zero
uses HC2. The other branch uses HC3 and inverse descent. The paper itself
keeps full HC4 and JC2 open.

No flaw was found in that a=0 argument in this bounded audit. I checked its
matrix identities independently and its rank-one coordinate inverse. HC2,
HC3 and the low-dimensional homogeneous Hesse theorem remain cited inputs;
their historical proofs were not independently re-audited. This is not a
formal verification or a publication-level review of the entire theorem.

## Independent check of the a=0 algebra

Let T be an arbitrary symmetric 3-by-3 matrix, representing Hess P, and
`M=Hess Q`, `w=grad Q`. All identities here are polynomial identities, so no
generic-matrix invertibility assumption is hidden. The determinant is

```
c = -w^T adj(T+u*M) w.
```

For quadratic Q, M is constant. Nonzero constant determinant forbids any
point with w=0. Hence rank three is already impossible. In rank two,
constant congruence and translation give `M=diag(1,1,0)` and
`w=(x,y,ell)`. The u^2 coefficient is `-ell^2`, so ell=0; then w vanishes
at x=y=0, an immediate contradiction. As a second check, the complete
expansion has u coefficient `-(x^2+y^2)*T33`; after T33=0 its constant
part is `(x*T23-y*T13)^2`, which likewise vanishes there.

For rank one, normalize `Q=x^2/2+alpha*y`. If alpha=0, w vanishes on x=0.
Otherwise the u coefficient is `-alpha^2*T33`, forcing `P=R(x,y)+z*S(x,y)`.
The remaining determinant is `(x*S_y-alpha*S_x)^2=c`. Choose a constant
nonzero square root kappa, with the appropriate sign. Put

```
q=x^2/2+alpha*y,   s=-x/alpha,
D=x*d/dy-alpha*d/dx.
```

These are actual polynomial coordinates, with Dq=0 and Ds=1. Thus DS=kappa
gives `S=kappa*s+h(q)`. The outputs S,q recover x,y; the remaining two
outputs solve for z,u through a 2-by-2 matrix of determinant -kappa.
This uses a polynomial coordinate system, not an assumption that an arbitrary
Hamiltonian derivation with a slice is already a coordinate derivation.

In rank zero Q is a nonconstant affine form. Choosing Q=lambda*z+q0 leaves
a two-variable Hessian determinant equal to `-c/lambda^2`, over C[z].
HC2 over C(z), followed by the unit-Jacobian formal-inverse descent, recovers
x,y polynomially over C[z]; Q recovers z and the remaining output recovers u.
There is no division by a source-dependent determinant.

## The plane pairing: exact equivalence, not a reduction of degree

For a plane Keller map K=(F,G), with J(F,G)=j!=0, define

```
Phi(x,y,u,v)=u*F(x,y)+v*G(x,y).
grad Phi = (u*F_x+v*G_x, u*F_y+v*G_y, F, G),
Hess Phi = [[u*Hess F+v*Hess G, J(K)^T], [J(K),0]],
det Hess Phi = j^2.
```

This gradient is an automorphism if and only if K is one. In one direction,
use K's inverse to recover x,y from the last two outputs, then solve the
first two using the polynomial inverse of J(K)^T. Conversely, let L be the
polynomial inverse of grad Phi. The first two components of
`L(0,0,A,B)` are an inverse of K: grad Phi at (x,y,0,0) is
`(0,0,F(x,y),G(x,y))`, and the invertible Jacobian matrix forces u=v=0 when
the first outputs vanish. Both compositions follow directly.

In Proposition 6.1's coordinates, take X=(x,y,u), singled variable v,

```
P(X)=u*F(x,y),       Q(X)=G(x,y),       a=0.
```

Its hypothesis is literally deg G<=2, regardless of deg F. This is broader
in degree than the quartic-potential case but does not advance the open
plane frontier. Independently: a quadratic G with a Keller mate has no
critical point. A rank-two quadratic has a critical point and is impossible;
a rank-one quadratic must have a nonzero linear kernel term, so it is
`x^2/2+alpha*y` in affine coordinates. The same (q,s) calculation makes any
Keller mate linear in s plus a polynomial in q. The affine G case is simpler.
Thus this plane subclass already has an elementary proof.

A constant target combination with degree <=2 gives the same conclusion.
No argument here proves such a combination exists for an arbitrary pair.
Also `deg Phi=1+max(deg F,deg G)`: quartic HC4 directly covers only pairs
of degree at most three through this construction. No dimension-preserving
cubic or quartic reduction has been supplied.

## Why the rank mechanism does not extend by dropping deg Q<=2

With Q=G(x,y) viewed in three variables (x,y,u),

```
M = [[G_xx,G_xy,0],[G_xy,G_yy,0],[0,0,0]],
w = (G_x,G_y,0)^T.
```

For arbitrary G, `w^T adj(M) w=0` identically, because adj(M) is supported
only in its last entry. This remains true when the two-variable Hessian of
G has rank two. More generally, the entire Hessian determinant of the
pairing is j^2, independent of u,v: all coefficients of positive u or v
degree vanish identically for every F,G. Its surviving constraint is exactly
the original plane Jacobian equation.

There is no permissible replacement of this variable M by a constant
diagonal matrix at every source point. Such a point-dependent change is
not a constant linear change of the polynomial potential. A concrete control:

```
p=x+y^2,       G=y+p^3,       F=p+G^2.
J(F,G)=1,     (deg F,deg G)=(12,6),
det Hess G=36*p^3,
G_y-2*y*G_x=1.
```

This is a composition of two triangular plane automorphisms. G has generic
Hessian rank two but no critical point. It invalidates extending the
quadratic rank-two exclusion to variable Hessians, while satisfying the
pairing's adjugate identity exactly. It is a positive automorphism control,
not a counterexample search.

For arbitrary G, asking for F with `G_y*F_x-G_x*F_y=j` and then proving that
(F,G) are polynomial coordinates is precisely the original problem. Calling
the left side a Hamiltonian derivation or replacing it by a variable-matrix
rank condition does not provide a new mechanism.

## A genuine extension of the other branch, and its boundary

The a!=0 proof can be independently extended to **arbitrary Q**. Let

```
z=u+Q(X)/(2a),
R=P-Q^2/(4a),
S_z=R+z*Q.
```

The gradient outputs are `(grad_X S_z,2a*z)`. Differentiation at fixed z
and substitution give, without assuming Hess Q constant,

```
Hess_X S_z = Hess P+u*Hess Q - (grad Q)(grad Q)^T/(2a),
det Hess_X S_z = c/(2a).
```

HC3 over C(z), and descent of the formal inverse to C[z] because the
Jacobian determinant is a constant unit, give the polynomial inverse.
This conditional-on-HC3 extension is mathematical content beyond the stated
Q bound, but it still requires a!=0.

The pairing has a=0 in both multiplier directions. Adding `a*v^2` does not
generally preserve its determinant: even

```
Phi=u*(x+y^2)+v*y,      det Hess Phi=1,
det Hess(Phi+a*v^2)=1-4*a*u.
```

So this extension gives no automatic escape from the a=0 branch. A new
constant-direction theorem or another explicit equivalence would be needed;
none was obtained in this bounded audit.

## Verification and handoff

Run `python3 box/ni-hc4-interface-20260906/check.py`. Exact symbolic checks
pass: both rank coefficients/squares, the pairing block determinant, its
tautological adjugate condition, the variable-rank automorphism, the
quadratic-addition countercontrol, and rank-one coordinate identities.
No AWS, numerical search, heavy CAS, shared ledger, or live-report work.

Checker SHA-256:
`11b44378e31d65a8a18af08771d9d380c9de02ab2f083d210e089b64266189b1`.

Recommendation: retain the a!=0 arbitrary-Q extension and the explicit
interface boundaries as reusable facts pending normal review. Do not give
the quadratic-Q rank analysis a new all-degree JC2 lane without a concrete
additional hypothesis or source-to-normal-form map.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9061`.
- Body SHA-256:
  `7b715700920fec5a727dbf26a282e7de53aa82234d8cca907f716fdab4d62815`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
