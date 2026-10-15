# Constant-gamma tangent graphs: arbitrary polynomial outputs are not Keller

Producer: swarmHQ ROOT. Date: 2026-10-15.
Basis: 38b0886e06f7e5aaf22a7c143630d3b8dd628c31.
Status: MANUAL / PROVISIONAL; independent different-model review required.
Claim: CONSTANT-GAMMA-NONLINEAR-PROJECTION-1.
This excludes a construction class, not arbitrary Keller pairs or JC2.

## Statement and exact ring

Work over C. Let R=C[x,y], choose c in C* and p,q in C[w] with
deg(p)=d>=2 and q'(w)=w*p'(w)/2. Put w=c*(1+x*y), and suppose
the following literal rational expressions are polynomials in the WHOLE R:

    C0=c*x,
    D0=(p(w)+2*c)/(c*x),
    E0=(q(w)+c*w)/(c^2*x^2).

Then the subalgebra B=C[C0,D0,E0] contains no pair P,Q with
J_xy(P,Q) in C*. Equivalently, no polynomial map C^3 -> C^2, of any
degree, applied to this triple is a plane Keller map.

Whole-plane polynomiality is an assumption, not inferred from a localized
formula. It implies p(c)=-2*c, q(c)=-c^2 and p'(c)=-2 by expanding at x=0.
The proof below does not require a claim that the triple is finite, injective,
a normalization map, or a restriction of every three-dimensional example.

## 1. The parameter curve must have a collision

Set r(w)=q(w)+c*w and rho(w)=(p(w),r(w)). Then

    r'(w) - (w/2)*p'(w) = c != 0.                         (1)

Thus rho is an immersion at every finite parameter: its two derivatives
cannot vanish together. Its coordinate degrees are d and d+1.
The following argument uses the classical arithmetic-genus formula for a
projective plane curve, not the Abhyankar-Moh embedding theorem.

Let K=C(p,r) inside C(w). The degree [C(w):K] divides both d and d+1,
by the towers through C(p) and C(r), hence equals 1. The parameter is
therefore birational onto its image. The map A1 -> rho(A1) is finite:
w satisfies the monic equation obtained from p(w)-p by its constant leading
coefficient. It is the normalization of its affine image.

The projective parametrization of degree d+1 has no base point. It has
exactly one preimage of the line at infinity, namely w=infinity, mapping
to [0:1:0]. In the chart where the second coordinate is 1, with tau=1/w,
the two image coordinates are

    p(w)/r(w) = a*tau + O(tau^2),  a != 0,
    1/r(w) = b*tau^(d+1) + O(tau^(d+2)),  b != 0.

Consequently the image is smooth at infinity. Birationality and a general
line pullback give projective image degree d+1, with normalization P1.
Its arithmetic genus is d*(d-1)/2>0, whereas its geometric genus is zero.
It must therefore have a singular point, and that point is affine.

If an affine image point had a single preimage, (1) would give a local
coordinate with nonzero derivative there. The inverse-function theorem
then makes that image germ a smooth graph; finiteness rules out additional
branches arriving from elsewhere. Hence an affine singularity has at least
two distinct preimages. There exist w0 != w1 in C with

    p(w0)=p(w1),             r(w0)=r(w1).                 (2)

No numerical enumeration of these parameters is required.

## 2. Attach the collision to the actual source plane

For i=0,1 put ai=wi/c-1 and define regular maps from C* into A2 by

    psi_i(s) = (s, ai/s).

Zero ai is allowed. Since c != 0, a0 != a1. Substitution gives

    C0(psi_i(s)) = c*s,
    D0(psi_i(s)) = (p(wi)+2*c)/(c*s),
    E0(psi_i(s)) = r(wi)/(c^2*s^2).

Equation (2) makes all three pullbacks equal. Thus every pair P,Q in B
has equal pullbacks under psi_0 and psi_1. These are actual maps into the
whole source plane; using C* to compare them does not localize the claim.

## 3. A Keller pair cannot identify these two maps

Suppose J_xy(P,Q)=kappa != 0. The polynomial one-form

    beta=P*dQ-kappa*x*dy

is closed. Polynomial integration in characteristic zero gives T in R
with beta=dT. Explicitly, for beta=A dx+B dy and A_y=B_x, one may take
T=integral_0^x A(s,y)ds + integral_0^y B(0,t)dt.

Equal pullbacks of P and Q imply equal pullbacks of P*dQ. Also
psi_i^*(x*dy)=-ai*ds/s. Subtracting the two primitive identities yields

    d(T(psi_0(s))-T(psi_1(s)))
        = kappa*(a0-a1)*ds/s.                            (3)

The expression inside d on the left is a Laurent polynomial in s.
Its derivative has zero residue at s=0, while the right side has the
nonzero residue kappa*(a0-a1). This contradiction proves the statement.

## 4. Controls and limits

The hypotheses are nonempty. For c=1 take

    p(w)=10*w-24*w^2+12*w^3,
    q(w)=(5/2)*w^2-8*w^3+(9/2)*w^4.

Direct differentiation gives q'=w*p'/2. The whole-plane triple is

    C0=x,
    D0=y*(-2+12*x*y+12*x^2*y^2),
    E0=y^2*((11/2)+10*x*y+(9/2)*x^2*y^2).

The degree hypothesis is essential. For d=1, p(w)=-2*w and
q(w)=-w^2/2-c^2/2 give C0=c*x,D0=-2*y,E0=-y^2/2.
Here C0,D0 themselves have Jacobian -2*c in C*.
The parameter curve is a smooth conic, so the positive-genus step correctly
does not apply. All checks here are by hand; no CAS or exhaustive search.

The nearest prior results are the all-seed LINEAR projection identity in
[the tangent-graph report](tangent-graph-linear-projections-swarmHQ-root-20260916T182800Z.md)
and the fixed-core constant-z graph obstruction in
[the collision-residue report](graph-collision-residue-astra-20260912.md).
The exact-Liouville collision principle is already known. The proposed
additional scope here is constant gamma, ALL eligible seeds, and ARBITRARY
polynomial target outputs. Constant gamma is not silently identified with
the constant-z graph in another chart. No external novelty claim is made.

Nonconstant gamma, other source parametrizations, and other construction
mechanisms remain outside scope. No reduction of arbitrary JC2 sources to
this class, counterexample, full JC2 proof, or automatic successor follows.
No exit-price assertion is made. FALLACY-v2 ring/scope checks were applied.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5818`.
- Body SHA-256:
  `9dea0e6c17ab75813a1b52bfe768681109b4f060358c4d1b68f3ffa079d31f8d`.
- Frozen basis: `38b0886e06f7e5aaf22a7c143630d3b8dd628c31`.
