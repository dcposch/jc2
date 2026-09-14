# Reduced affine boundary does not fix fibre multiplicity

ROOT, September11 2026. MANUAL / INTERNAL-UNREVIEWED strategy discriminator.
Basis0d39df3c9fd69c939a8420c54d03228b9077777d. Original publication
reserve18:40UTC / HARD18:43UTC. No scientific execution or theorem promotion.

## Exact all-exponent control

Let W=Spec C[X,Y,Z]/(XY-Z^2+1) and let E be the reduced curve X=0,Z=-1.
This is a smooth affine surface: the three partial derivatives Y,X,-2Z
cannot vanish simultaneously on W. The curve E is an affine line with
coordinate Y. Write U=W-E. The map

    (a,b) |-> (X,Y,Z)=(a, 2b+a*b^2, 1+a*b)

identifies A2 with U. Its inverse has a=X, and

    b=(Z-1)/X on X!=0,   b=Y/(Z+1) on Z+1!=0.

These opens cover U; the expressions agree by XY=(Z-1)(Z+1). Substitution
checks both inverse compositions, including the line X=0,Z=1. Near every
point of E, Z-1 is a unit, X locally defines E, and b=(Z-1)/X has pole
order one. The local equation assertion also follows from d(XY-Z^2+1)/dZ
being nonzero along E.

For ANY integers k,l>=2, choose the following two coordinates on U:

    f=a+b^k,       h=b+f^l.

They form a polynomial coordinate pair: b=h-f^l and a=f-(h-f^l)^k.
The two triangular changes have determinant one. As rational functions on W,

    N=X^(k+1)+(Z-1)^k,
    f=N/X^k,
    h=(N^l+(Z-1)*X^(k*l-1))/X^(k*l).

At E the two numerators are respectively (-2)^k and (-2)^(k*l), hence
units everywhere on E. Both f and h therefore extend to MORPHISMS
W -> P1: on U use the finite chart, and near E use the regular coordinates
1/f or 1/h at infinity. There is no remaining indeterminacy or other pole.
Every finite fibre is an affine line because f,h are coordinates on U.
Nevertheless their scheme-theoretic infinity fibres are exactly

    f^*(infinity)=k E,       h^*(infinity)=k*l E.

Indeed their local defining ideals are (X^k) and (X^(k*l)), multiplied by
units. For k=l=2 the multiplicities are 2 and 4. Thus a smooth affine W,
a reduced boundary E=A1, an actual plane open U, and two supplied coordinate
projections extending over the boundary do NOT force either extension to
be an A1-bundle or to have reduced infinity fibre. This is uniform in k,l,
not a finite-degree experiment.

This does not refute existence of SOME other bundle structure: b itself has
simple pole along E. It also does not construct a finite Keller normalization
or refute a theorem retaining that extra hypothesis. This W has trivial
canonical bundle, whereas the stipulated smooth normal-index2 Keller
normalization would have canonical class [E]. The control tests the cited
reduced-boundary-to-reduced-fibre inference alone; it is not a JC2 example.

## Literature applicability and decision

The targeted read of [Rodriguez Diaz, v2, Theorem3.5](https://arxiv.org/html/2403.02219v2)
uses a reduced affine boundary when passing to the infinity fibre of a
coordinate projection. The calculation above shows why that passage needs
an additional multiplicity argument. No full-paper refutation or independent
audit of its primary-submodule hypothesis is claimed. Its general canonical
argument also needs the ramification coefficient, not merely its support.
The September7 campaign torsor report had already withheld that import.
Decision: do not use these unverified implications as a faster all-degree
surface classification or exclusion. The exact missing hypothesis is not
resolved by another finite sheet count.

A separate [one-dicritical source note](https://raw.githubusercontent.com/alok/jacobian-two/main/docs/one-dicritical-source-smoothness.md)
has a degree-independent LOCAL index-two obstruction under explicit cyclic
endpoint-cover assumptions: invariant functions have order at least two,
so their Jacobian cannot have order one. ROOT checked that elementary order
comparison; the cited endpoint classification and its all-source attachment
were not freshly proved. The note itself retains global degree-six survivors.
It supplies no accepted all-degree exclusion or bundle classification here.

The [BGV abstract](https://arxiv.org/abs/2609.05746v1) encountered by this
search is the already-banked September9 v1/internal-version356, not a new
paper revision or new proof. Its existing weak-type1 divisor gap remains.
This is targeted primary intake, not a completed broad sweep or clock reset.

## Reading, custody and stop

The proof above is self-contained manual algebra and chart geometry. Context
pins: old Rodriguez v2 PDF55b2e1aeb226989e61e027372abdf3db969246a1afb3b8a8d7188d3e211a9d09;
its textc93a75c6dba77a8865dc90848b8ab72be3662c8845d925f61d383ca23558d7b0;
old torsor report7beff9e113580e22aba68f79811ed45f2023e195f7998a51cd224163a775db5a.
The old report was read WHOLE, and the pinned text's lines213-260 were read
for Theorem3.5. Current HTML sections1-3.6 and the external source note's
333 lines were exposed by the web tool; no fresh whole-paper proof review
or equality between current web bytes and old PDF bytes is claimed.
Some combined displays clipped; only the named fully exposed passages
support the scope decision. No downloaded code or scientific subprocess ran.

QUANTITY: infinity-fibre multiplicities for the two supplied coordinates.
CHEAPEST TEST performed: exact chart/inverse/numerator calculation, manual,
no runtime estimate. Narrow history search in AUDIT/APPROACHES and named
torsor/pseudo-plane/two-chart reports found the previous import warning,
not this exact control; no corpus-wide novelty claim. No new canonical OPEN,
echo review, source variant, worker or automatic descendant. The main global
source/landing/cofinality and polynomial-pair questions remain unresolved.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5658`.
- Body SHA-256:
  `d2ac7e044635bfb8692e1e698b44b5b1bfa16c512cc592da2ce2c87c7208170b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
