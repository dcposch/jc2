# Character cubics: the fixed area form stays nonexact under finite covers

Producer: swarmHQ ROOT (Astra), September17,2026.
Basis: 3214fd164b78aaf49a2a6c7b231ad7f2d8c20010.
Evidence: MANUAL; native Astra co-check completed, same-model only.
Lifecycle: PROVISIONAL / UNPROMOTED; different-model FIRST required.
Claim ID: CHARACTER-CUBIC-NONEXACTNESS-1. No novelty claim.

## Statement and construction consequence

For ANY constants A,B,C,D in C, put

    S: x^2+y^2+z^2+xyz-Ax-By-Cz-D=0,
    K=C(S),       omega=dx wedge dy/(2z+xy-C).

The surface is integral, and omega is NOT the exterior derivative of a
rational one-form over K. It remains nonexact after EVERY finite field
extension L/K. Consequently:

1. There is no dominant rational map phi:A2_(u,v) --> S satisfying
   phi^*omega=c du wedge dv for a nonzero CONSTANT c.
2. There are no f,g in K with df wedge dg=c omega for such a c.
   In particular the fixed Poisson bracket on S admits no rational,
   and hence no regular, pair with nonzero constant bracket.

The first statement covers arbitrary finite source degree, including
degree one. It is not limited to the degrees of known Painleve
transformations, nor does it require S smooth in the affine chart.
The exact fixed form and constant multiplier are essential. It does
NOT prohibit arbitrary dominant rational maps, multiplication of omega
by a nonconstant function, or constructions with unrelated source and
target forms. It supplies neither a general Keller-source reduction
nor a proof or counterexample for JC2.

## 1. All-parameter integrality

As a monic quadratic in z, the defining polynomial has discriminant

    Delta=(xy-C)^2-4(x^2+y^2-Ax-By-D).

If Delta is a square in C(x,y), its square root is in C[x,y]: it is
integral over the integrally closed polynomial ring. Its leading
homogeneous part must be xy or -xy. Absence of cubic terms in Delta
forces the root's degree-one part to be zero. The root would therefore
be +/-xy+k for a constant k, whose square has x^2 coefficient zero.
But Delta has x^2 coefficient -4. This contradiction proves
irreducibility over C(x,y), hence over C[x,y,z] by monicity/Gauss.
Thus K is well-defined for all four parameters. The quadratic is
separable, so 2z+xy-C is not zero in K and omega is nonzero.

## 2. A single smooth infinity flag

Homogenize in [X:Y:Z:W]. The point P=[1:0:0:0] belongs to the projective
closure. On X=1 use r=Y/X, s=Z/X, w=W/X; its equation is

    F=w(1+r^2+s^2)+rs-Aw^2-Brw^2-Csw^2-Dw^3=0.             (1)

At the origin F_w=1, for EVERY parameter choice. This is a smooth
surface point, with regular parameters r,s. Its completed local ring
is C[[r,s]], and the implicit solution w has the form

    U=1+r^2+s^2-Aw-Brw-Csw-Dw^2,
    w U=-rs,           U(0,0)=1.                          (2)

The two boundary branches at P are r=0 and s=0. These assertions use
only this smooth neighborhood, not global smoothness or a resolution
of possible affine singularities.

On the affine overlap x=1/w, y=r/w, z=s/w, direct differentiation gives

    dx wedge dy = dr wedge dw / w^3,
    2z+xy-C=(r+2sw-Cw^2)/w^2=F_s/w^2.

Taking the wedge of dF=0 with dr yields
dr wedge dw=-(F_s/F_w) dr wedge ds. Therefore

    omega=-dr wedge ds/(w F_w)
         =(U/F_w) (dr/r) wedge (ds/s).                    (3)

Both U and F_w are formal units with constant term1. The coefficient
of r^-1 s^-1 in the coefficient of dr wedge ds in (3) is exactly1.

## 3. The residue detects rational nonexactness

The smooth local ring at P injects into its completion, so its function
field K embeds in Frac(C[[r,s]]) and hence in E=C((r))((s)).
Use the CONTINUOUS coordinate differential complex on E, with its
termwise derivatives partial_r, partial_s and formal basis dr,ds.
The embedding of K induces a map from its algebraic differential
complex to this coordinate complex, commuting with exterior d.
No claim identifies all abstract Kahler differentials of the series
field E with the two-dimensional coordinate complex.

For h in E, let Res(h dr wedge ds) be its r^-1 s^-1 coefficient.
For any a,b in E,

    Res(d(a dr+b ds))
      =Res((partial_r b-partial_s a) dr wedge ds)=0.        (4)

A termwise derivative can produce exponent -1 only by differentiating
exponent0, which gives zero. This applies to the iterated Laurent
series coefficients, including arbitrary finite-order poles in either
coordinate. Equations(3)--(4) give Res(omega)=1 and prove that omega
cannot equal d eta for any rational eta over K.

This is nonexactness in the FUNCTION FIELD, stronger than failure to
have a globally regular primitive on an affine surface. Removing more
divisors cannot remove the obstruction from the same rational form.

## 4. Finite extensions cannot erase it

Let L/K be finite, necessarily separable, of degree n. Standard
separability gives

    Omega^j_(L/C)=L tensor_K Omega^j_(K/C).

Define Tr on these forms by field trace on the coefficient. This map
commutes with exterior d. Explicitly, choose the transcendence basis
r,s of K/C. Their coordinate derivations extend uniquely through every
finite separable extension. In a normal closure those extensions commute
with every K-embedding, so differentiation commutes with the sum of
conjugates defining Tr_(L/K). The formula holds on zero-forms and on
the dr,ds basis, hence on the whole differential complex.

If the pullback of omega were d eta in L, then

    n omega=Tr(d eta)=d(Tr eta).

Division by the nonzero constant n would make omega exact in K,
contradicting Section3. This argument requires neither an unramified
extension at the infinity flag nor a Galois extension L/K.

For a dominant rational phi:A2 --> S, the induced extension
C(u,v)/K is finite: both fields have transcendence degree2 and are
finitely generated. The proposed pullback c du wedge dv=d(cu dv)
would be exact, proving consequence1. Likewise df wedge dg=d(f dg)
proves consequence2 directly over K. With the Poisson convention
{x,y}=2z+xy-C, the identity df wedge dg={f,g} omega translates it to
the constant-bracket statement.

## 5. Checks and scope boundaries

- The identity on the Euclidean plane preserves the exact form du wedge dv;
  the obstruction does not reject this necessary positive control.
- Even the degree-two RATIONAL map (u,v)->(u^2,v/(2u)) pulls the target
  Euclidean area form back to du wedge dv. Thus finite degree greater
  than one is not itself the obstruction; nonexactness of the fixed
  character form is. This map has a pole and is not a Keller counterexample.
- The singular Cayley specialization A=B=C=0,D=4 retains F_w(P)=1
  and residue1. No generic-parameter or affine-smoothness loophole is used.
- A local holomorphic Darboux chart is not a finite rational function-field
  extension. The proof does not rule out analytic symplectic coordinates.
- Rational changes of coordinates carrying the SAME form preserve the
  conclusion. Arbitrary nonconstant rescalings of that form are outside it.
- Maps between two character surfaces may preserve their respective
  nonexact forms up to constants. The theorem does not refute their
  existence; it blocks a finite rational Euclidean symplectic source
  parametrization of either endpoint with this fixed form.

## 6. Primary attachment and historical comparison

Mazzocco--Vidunas, *Cubic and quartic transformations of the sixth
Painleve equation in terms of Riemann--Hilbert correspondence*,
[arXiv:1011.6036v2](https://arxiv.org/pdf/1011.6036v2), revised
October12,2011; Studies in Applied Mathematics130(2013),17--48,
supplies the concrete family in equation(2.3), with
(u1,u2,u3,u0)=(A,B,C,-D), and its Poisson brackets in(2.5).
ROOT read the opening statements and these formula passages, including
the infinity triangle(2.9)--(2.10). No whole classification-proof audit,
all-degree classification import, or algebraicity assertion about the
Riemann--Hilbert correspondence is used. All calculations in Sections1--4
are derived here; the paper is a source of the tested construction object.

Nearest campaign evidence:

- [Source-volume integration](source-volume-residue-integration-root-20260911.md),
  SHA91ce3ee72fcdf88091806a9c7990f0c0be48006c45b42930272f5bc1a34f5eb8,
  distinguishes regular primitive obstruction for the Wright chart from
  exact higher-order transitions. That Wright form IS rationally exact
  in its original plane chart; its affine regularity obstruction must
  not be substituted for the function-field obstruction proved here.
- [Volume-neutral torus quotient](volume-neutral-torus-quotient-swarmHQ-root-20260915.md),
  SHA181d7ae11675d27a61da977f143abaf5797415d6c64923e11be336281ce6df80,
  concerns linear actions on affine space with polynomial plane quotient,
  not this singular/affine cubic with its fixed logarithmic form.
- [Trace-node calculation](keller-trace-node-astra-20260911.md), Section5,
  already uses a continuous double-residue detector. That standard
  detector is not claimed new; this report attaches it to a different
  complete source and uses finite-field trace to cover all source degrees.

The first two reports were read whole; the trace-node comparison is
selected Section5 with surrounding scope. Scoped frozen-history searches
found no prior character-cubic attachment, not an exhaustive priority
search. This is one construction-source gate, not an automatic cubic,
character-variety, multiplier or Painleve-family program. No new degree
bound, general integrality theorem, actual-source landing, or JC2 result.

## Custody and next gate

ROOT's manual reconstruction uses no scientific code, numerical experiment,
CAS, cloud worker or finite parameter sample. Artifact/collision tools
check publication integrity only. Native Astra completed its independent
manual attack at20:08:39 UTC, confirming irreducibility, residue sign,
continuous-coordinate detector, finite trace and both scoped consequences.
ROOT collected that terminal answer before freezing these bytes. This is
a same-model co-check, not independent FIRST. The next gate is one
different-model hostile review
of the exact all-parameter residue, finite-trace and construction scope.
No descendant is admitted before that review.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10317`.
- Body SHA-256:
  `3c8269195f409abff6af6b156491a3b78d23aec5abcb6fb76e08e546efd00086`.
- Frozen basis: `3214fd164b78aaf49a2a6c7b231ad7f2d8c20010`.
