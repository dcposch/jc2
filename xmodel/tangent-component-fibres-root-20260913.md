# Component-fibre obstruction for the unbounded tangent-sweep family

ROOT, September13,2026. MANUAL / PRODUCER-CHECKED / UNPROMOTED.
No CAS, numerical experiment, claimed new literature theorem or JC2 resolution.

## Exact object and decision

Over C put u=1+xy, gamma=gamma0+a*xy+b*x^2*z, w=gamma*u, C=x*gamma,
where b!=0. Let p,q in C[w], q'=w*p'/2, and suppose the three expressions

    F1=C, F2=(p(w)+2gamma)/C, F3=(q(w)+gamma*w)/C^2

are POLYNOMIAL on the whole A3. These are the three-dimensional tangent-sweep
forms in [Gao, section3.3](https://arxiv.org/html/2608.00222v1#S3.SS3).
The theorem below is conditional on these literal polynomial divisibilities;
it does not assert that arbitrary p or arbitrary coefficients supply them.
No geometric-degree bound or ambient counterexample verification is needed.

**Claim. None of F1,F2,F3 is a polynomial coordinate of C[x,y,z].**
For every c!=0, F1=c and F3=c carry explicit nonconstant units. If
p(w)=w*A(w), s is the number of DISTINCT complex roots of A, then

    [F2=c] = L^2+s   in K0(Var_C), and chi_c(F2=c)=1+s>=2.

Here L=[A1]; multiplicities do not count toward s. In particular the second
fibre is not A2 either. These statements are uniform in all admissible
parameters and all degrees, not an enumeration of a finite support family.

## Source identities and necessary admissibility facts

On x*gamma!=0, the variable changes (x,y,z)->(x,u,gamma)->(x,gamma,w),
the padded sweep, and the target division have determinants b*x^3,
-gamma, 2gamma^2, and C^-3. Therefore J(F)=-2b. Since F is polynomial,
this holds everywhere. In particular every Fi is a submersion.

Polynomiality along gamma=0 on x!=0 gives p(0)=q(0)=0. The differential
identity then gives polynomials A,B with p(w)=w*A(w), q(w)=w^2*B(w), and

    x*F2 = u*A(gamma*u)+2,
    x^2*F3 = u*(u*B(gamma*u)+1).                     (1)

Also gamma0!=0: otherwise dF1 vanishes on x=0, contradicting J(F)!=0.
Evaluating (1) on x=0 gives A(gamma0)=-2 and B(gamma0)=-1.
If A were constant then A=-2 and q'=w*p'/2 would give B=-1/2,
contradicting B(gamma0)=-1. Thus A, and consequently B, are nonconstant.

The coefficient of x in u*A(gamma*u)+2 is k*y, where

    k=A(gamma0)+(gamma0+a)*A'(gamma0).

Hence F2|_(x=0)=k*y. Necessarily k!=0: if it vanished, both dF1 and dF2
would be multiples of dx at x=0, contradicting the nonzero Jacobian.
These facts use the full polynomial triple, not the rational sweep alone.

## First component: an invertible coordinate function on the fibre

On F1=c!=0, x is a unit with inverse gamma/c. In fact the fibre is
Gm_x times A1_y: gamma=c/x and

    z=(c/x-gamma0-a*xy)/(b*x^2)

give the inverse parameterization. Thus x is nonconstant. A2 has only
constant units, so this fibre cannot be A2 and F1 cannot be a coordinate.

## Second component: the complete fibre class, including x=0

Fix c!=0 and set N(u,gamma)=u*A(gamma*u)+2. On x!=0 the change of
variables is invertible, with

    x=N/c, y=(u-1)/x,
    z=(gamma-gamma0-a*(u-1))/(b*x^2).

Consequently (F2=c) intersect (x!=0) is exactly A2_(u,gamma) minus
D={N=0}. On D, u and A(w) are nonzero. The maps

    w=gamma*u,
    u=-2/A(w), gamma=-w*A(w)/2

identify D with A1 minus the s distinct roots of A. The omitted part of
the ORIGINAL fibre is x=0, y=c/k, with z arbitrary, hence one A1.
Additivity, with both the open part and this closed part retained, gives

    [F2=c]=L^2-(L-s)+L=L^2+s.

Compactly supported Euler characteristic therefore gives 1+s, not 1.
This is not an inference from an open chart or a generic degree: it is an
explicit decomposition of the entire fibre. A nonconstant A has s>=1.

## Third component: explicit unit survives the entire fibre

On F3=c!=0, identity (1) implies that u cannot vanish: u=0 would force
x=0, while u=1+xy would then equal1. More strongly, an explicit polynomial
inverse in C[x,y,z]/(F3-c) is

    u^-1 = 2-u + (y^2/c)*(u*B(w)+1).                (2)

Indeed the product with u is 2u-u^2+x^2*y^2=1. This uses the full fibre,
including x=0, and does not silently localize it.

The unit is nonconstant. For any t in C*, set x=1, y=t-1. Since B is
nonconstant, choose w with B(w)=(c-t)/t^2, then set gamma=w/t and
z=(gamma-gamma0-a*(t-1))/b. These points lie on F3=c and have u=t.
Thus u takes every nonzero complex value on that fibre. Again F3 is not
a polynomial coordinate, even in cases where an Euler test alone gives1.

## What this changes, and what remains missing

The current construction client asks for a TARGET polynomial coordinate h
whose pullback h(F) is a SOURCE polynomial coordinate. This would permit
genuine plane-fibre restriction after source/target coordinate changes.
The displayed choices h=target coordinate1,2,3 all fail throughout the
entire admissible family. No component-fibre solve or larger-degree replay
can repair those choices. Polynomial SOURCE automorphisms preserve this
failure; a target permutation/scaling/translation also does not change it.

An arbitrary affine combination or nonlinear target coordinate is NOT
covered. Neither is a different ambient direction-field construction, an
arbitrary embedded plane, or arbitrary birational modifications. This result
does not say that a smooth A2 fibre alone makes a polynomial a coordinate.
It supplies no new exclusion for arbitrary plane Keller maps.

The accepted plane mapping-degree<=5 bound remains a separate imported
stop, not a premise reproved here. The old direct rational S(x,y/x)
polynomialization stop in xmodel/sol-tangentsweep.md concerns a different
object. Focused history searches found no matching component-fibre argument
in the current map, audit and that report; no exhaustive novelty claim.

No automatic family extension, computational launch, or additional review
is selected merely to harden this lemma. Its sole client is the bounded
inhomogeneous-coordinate discriminator, and the global JC2 goal stays open.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5914`.
- Body SHA-256:
  `3da0f92e09c47f612a596f3bf3832bee3847ba046dc6787872d533c904e3c64b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
