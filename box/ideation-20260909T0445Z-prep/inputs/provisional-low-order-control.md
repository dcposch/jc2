# Proper-power reference: a low-order polynomial countercontrol

/root coordinator, 2026-09-09. Basis0d39df3c9fd69c939a8420c54d03228b9077777d.
PRODUCER-CHECKED / UNREVIEWED hand control. ZERO mathematical subprocesses.
This is post-cross-freeze local work; no live cross or proof-gate body was read.
It is not a Keller pair, a counterexample to JC2, a source-realization claim,
or a refutation of any accepted theorem.

## Exact tested inference

Replacing a common top H by its primitive root h changes exponents3:5 to
3e:5e. The old kernel induction cannot simply assert ord_s G>=2j from
polynomiality, the closed centralizer of h, combined homogeneity, and the
vanishing of the source Jacobian BELOW order2j. The explicit polynomial
object below satisfies those low-order conditions but has an earlier G.

The control attacks the proposed automatic induction step in Fable0310
blind ecd7305aa30862716a78452bd284211f15873b12587493df7fc96e5ee5866383.
Root blind64d3b5a24b382a7833479e4c7c41b3b28c73d67964bc73a8e7c7fc2552393d47
and Astra blind47e1475aeb83b53446e2e8f5df3fae7136941d68715b654d537ddd7e30b36d1a
already identified the derivative-remainder obstruction. This note makes it
a changed-object control. Those reports were terminal/collected before use.

It does NOT refute a theorem imposing the entire nonzero constant-Jacobian
identity: our object deliberately has a nonconstant Jacobian at later
orders. A valid stronger argument could use those later equations, but
would need a new step beyond the claimed low-order kernel induction.

## 1. Exact scalar-reference identity

Let K have characteristic zero. Brackets differentiate u,v only; s is a
parameter. Write

A=a(R)+F,  B=b(R)+q(R)F+G,

where a,b,q have coefficients in K[s], and define rho=b'-a'q, derivatives
being in R. Direct use of the product rule, WITHOUT any power expansion, gives

[A,B]=[R,T]+[F,G],
T=a'G-rho F-(q'/2)F^2.

Indeed dA=a'dR+dF and
dB=(b'+q'F)dR+q dF+dG. Their wedge has dR/dF coefficient
a'q-b'-q'F=-rho-q'F, exactly the displayed derivative of T.

If a,b are monic scalar references of respective degrees 1<M<N in R,
R has combined degree d, and a(R),b(R) are combined-homogeneous of
degrees Md,Nd respectively, division q=quotient(b',a') leaves
deg_R rho<=M-2. A term rho_i(s)R^i has
ord_s rho_i=(N-1-i)d when present. Thus its first allowed order is
(N-M+1)d, NOT necessarily greater than the first F order j.
For M=3e,N=5e this is (2e+1)d; the old3/5 argument used its special
inequality3d>j. There is no analogous automatic inequality when e>1.

## 2. One ordinary factored control over Q

Set R=h=u*v^3, d=4, M=21, N=35 and j=79. Work in Q[s,u,v],
with s,u,v each having degree1. The exact closed centralizer holds:
[h,u^i*v^k]=(k-3i)u^i*v^(k+2), whose distinct input monomials have distinct
output monomials, so ker[h,-]=Q[h].

Choose the polynomial references and remainders

a(R)=R^21,
b(R)=R^35+s^60*R^20,
F=s^79*R*u,
q(R)=(5/3)*R^14,
rho(R)=20*s^60*R^19,
G=(20/21)*s^139*u.

Then a'=21R^20 and b'=35R^34+20s^60R^19, so q is exactly the
Euclidean quotient and rho the remainder. Both A and B above are ordinary
polynomials, given in compact FACTORED form only. No coefficient stream,
large polynomial object, arithmetic script or source builder was created.

A has combined degree84, and B combined degree140. At s=0 their top
forms are h^21,h^35. At s=1 their actual ordinary degrees remain84,140.
The primitive root has unequal multiplicities1,3, not the already
classically excluded balanced h=uv. The common degree-28 root for the
coprime3:5 description is H=h^7, which is NOT closed.

The canonical A reference is compatible with R=h: below order79 all
remainders vanish, and F_79=hu has degree5, so it is not divisible by
h^20 and cannot be absorbed by the degree-4 reference correction. Nor
is it a scalar polynomial in h, since its degree is not a multiple of4.
The scalar b term s^60R^20 is among the allowed lower B kernels.
There is no illicit fractional coefficient, negative exponent or gauge.

## 3. Bracket and order checks, entirely by hand

Here a'G-rho F=0 exactly, while q'/2=(35/3)R^13. Consequently

T=-(35/3)*s^158*R^15*u^2.

Since [R,u]=-3u*v^2 and [R,u^2]=-6u^2*v^2,

[R,T]=70*s^158*R^15*u^2*v^2,
[F,G]=-(20/7)*s^218*u^2*v^2.

Thus

[A,B]=70*s^158*R^15*u^2*v^2-(20/7)*s^218*u^2*v^2.

This nonzero polynomial is combined-homogeneous of degree222, as required
for a bracket of combined degrees84,140. Its s-order is158=2j.
Every coefficient at order less than2j vanishes. Nevertheless

ord_s G=139=j+60 <158=2j.

This is a genuine polynomial countercontrol to the stated low-order
inference, not a predicate toggle or a sample evaluation. The earlier
G term cancels rho F exactly, which is the missing mechanism.

The control even lies in the proposed numerical "late" interval:
3j=237>(M+N-1)d=220. But its full Jacobian is NOT c*s^222 for a
nonzero constant c. In particular the order158 coefficient is nonzero.
No actual Keller source or possible counterexample has been exhibited.

## 4. Disposition and source boundary

The safe generalized identity retains rho. Polynomiality below2j can
force early compensating G terms rather than their vanishing. The next
useful question is which ADDITIONAL full-source equations eliminate or
control those terms, or force a further approximate-root decomposition
of the scalar curve R -> (a(R),b(R)). This report answers neither.

The exponents were chosen to match the proposed primitive top of the
published F9j1 source, but the actual source audit is separate and was
still running when this control was derived. Matching those tops does
not give its first edge, complete chain, source nonemptiness, or a
constant Jacobian. No pending F9 result or fixed-degree-normalization
verdict is a premise of this hand calculation. No new mathematical
OPEN identifier, compute job, public artifact or dependent lane is
authorized. Different-model review is required before promoting the
new control/inference-refutation. JC2 remains unresolved.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6128`.
- Body SHA-256:
  `8ded9ec00877446df422c24f9d99295e1f04f6c94f13a3d910eefb9723342652`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
