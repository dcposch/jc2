# F9 cubic double/simple roots: the Euler equation forces ratio3/2

PROVISIONAL PROSE candidate, /root, September9,2026. Basis0d39df3c9fd69c939a8420c54d03228b9077777d. This is a conditional face constraint, not a receiver exclusion or a source-existence theorem. Different-model review required. ZERO mathematical subprocess of any size.

## 1. Exact source and imported Euler element

Let an actual ordinary constant-nonzero-Jacobian pair over C have first (7,-2)-face

P_w=alpha*R^m, R=u*r(z), z=u^2*v^7,
r(z)=(z-a)^2*(z-b), a*b*(a-b)!=0, alpha!=0, m>0.

This includes the explicit F9,j1 source with m=3, provided its selected double-root/remaining simple-root data are attached. Those data are assumed here; this proof does not import a provisional all84/140 source arrow. Scalar normalization makes r monic without changing its roots.

GGV1401.1784v3 Theorem2.6 at w=(7,-2) supplies an ORDINARY polynomial Euler element E, of weight7-2=5, with [E,P_w]=P_w. The positivity hypothesis holds since w(P)=7m>0. Because the polynomial ring is a domain, [mE,R]=R. Set F=mE. It remains polynomial and weight5. The factor m is essential: the original E satisfies [E,R]=R/m, not R.

All ordinary monomials of weight5 have exponents(i,j)=(1+2k,1+7k) for integer k>=0. Consequently F=u*v*f(z) for a polynomial f in C[z]. This ordinaryness is essential; arbitrary rational f would give a different problem.

## 2. The scalar ODE and its complete polynomial solution condition

Differentiate the displayed factored expressions by hand, with z_u=2z/u and z_v=7z/v. One obtains

[u*v*f(z),u*r(z)]
 =u*(5*z*r'(z)*f(z)-7*z*r(z)*f'(z)-r(z)*f(z)).

Thus the exact equation is

5*z*r'*f-7*z*r*f'-r*f=r.                         (1)

Divide by r in C(z):

5*z*(2/(z-a)+1/(z-b))*f-7*z*f'-f=1.              (2)

At each of the distinct nonzero a,b, every term except the displayed logarithmic-derivative term is polynomial. Its nonzero residue coefficient forces f(a)=f(b)=0. Therefore deg f>=2. If d=deg f>2, the leading coefficient of the left side of(1) is the leading coefficient of f times

15-7d-1=14-7d !=0,

at degree d+3>3, impossible since deg r=3. Hence d=2 and

f=C*(z-a)*(z-b), C!=0.

Substitution in(2), still in factored form, gives the polynomial identity

C*((3*a-2*b)*z-a*b)=1.

It follows necessarily that

b=(3/2)*a, C=-1/(a*b).                          (3)

Conversely, if(3) holds, the displayed quadratic f satisfies(1) exactly. This proves the complete polynomial-Euler condition under the exact assumed double/simple cubic profile. It does NOT show that the face has an actual Keller completion. The double root is a; interchanging the roles without also changing their multiplicities changes the statement.

Manual rejecting control: with the same nonzero distinct a,b and f=-(z-a)(z-b)/(a*b), equation(2) has left side 1-(3*a-2*b)*z/(a*b). A different root ratio leaves that explicit nonzero residual. No CAS, expansion program, scalar subprocess or finite test is used.

## 3. Conditional receiver normalization, with field and scalar guards

If the separately proposed F9 opposite-edge map is valid, it produces ordinary receivers A,B, degrees21/35, [A,B]=c*g, c!=0, with (2,1)-faces alpha*H^3,beta*H^5, where

H=g^3*p*r(p^2/g)=p*(p^2-a*g)^2*(p^2-b*g),

and (1,-1)-faces

alpha*r(0)^3*g^6*(g*p+lambda)^3,
beta*r(0)^5*g^10*(g*p+lambda)^5,

where lambda!=0. This subsection is a CONDITIONAL composition with that map, not a proof of its source arrow, ordinaryness or hull.

Over C choose mu!=0 with mu^3=a*lambda and put kappa=lambda/mu. Apply the diagonal source change(g,p)->(kappa*g,mu*p). Then the root parameters change to a*kappa/mu^2=1 and b*kappa/mu^2=3/2, while lambda changes to lambda/(kappa*mu)=1. The common face acquires only the nonzero scalar mu^7. Divide the outputs by alpha*mu^21 and beta*mu^35, respectively. The resulting upper faces are exactly H_*^3,H_*^5 with

H_*=p*(p^2-g)^2*(p^2-(3/2)*g),

and the lower faces are exactly

(-3/2)^3*g^6*(g*p+1)^3,
(-3/2)^5*g^10*(g*p+1)^5.

Diagonal nonzero scaling preserves the whole support/hull and all attained-vertex guards; nonzero independent output scalings do too. The Jacobian remains c_*g for SOME nonzero c_*; it is not simultaneously normalized to g. Output constants remain free. A cubic-root extension may be required over a nonclosed coefficient field, so the normalization is asserted over C, not automatically over K. No scheme-equivalence or nilpotent-base claim.

This removes the free double/simple root ratio, and conditionally the two nonzero diagonal-scaling parameters, from a prospective receiver contract. It does not supply the lower coefficient equations, a reverse ordinary lift, a point, a proper ideal, a unit certificate or an exclusion.

## 4. Read/dependency boundary and status

The Euler theorem's complete statement/proof and the F9 source/face formulas were read in the current logical turn. Primary source https://arxiv.org/pdf/1401.1784v3, frozen text SHAe3694dde3f83c2ab6ed8d957fc6b53472e6a6dd55486af1dff345eade39e37b1. This uses only Theorem2.6 at the explicit ordinary face, not a generalized theorem for Jacobian c*g. No invocation of that constant-J theorem directly on the receiver occurs.

Sections1–2 assume their exact source and stand independently of the provisional normalization and opposite-edge maps. Section3 uses the explicit conditional receiver formulas in xmodel/f9-polynomial-receiver-interface-astra-20260909.md, SHA8bad927c8ef369a211fe3b1467efe6f9f40f26141e6338c1a470eb918a2fa50c, whose root custody20pins were checked05:07:25 before WHOLE reading. The source intake4b9ff7f41df4c98cd0dacd526b734e997dfc78c1783ea7cbc5fa7be4ad9bde78 was previously read WHOLE. Bounded named-report and2022-primary-text searches did not find this root ratio explicitly in those F9 descriptions; this is not an exhaustive history or novelty claim.

No live0445 blind/gate, protected project, mathematical subprocess, source builder, solver or AWS/SSH was accessed or executed. The root0445 blind is immutable; this is postblind research and not an added peer-blind premise. Different-model joint review of the source map, receiver map and this face constraint may give separate verdicts; failure of one does not silently promote the others. Stop after this finite face-constraint candidate.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6320`.
- Body SHA-256:
  `198fa7c9e9b5e3d408b72ca1eecd36b6689b53bf7871872374f8d5c5f7a74307`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
