# Audit of the complete-source graph merge and remaining Jacobian bands

The merge in `deep_resume_jacobian.py` is a valid way to add already-certified
necessary rows, provided both complete antecedent chains and their source
coordinate map are verified. It does not infer an earlier locus by deleting
keys from a solved map. This note does not assert that either branch is dead.

An exact QQ* pivot replaces a coordinate by a polynomial in the other
coordinates, giving an isomorphism with the graph of that polynomial. A
certified single-factor power step a*f^n=0, with a in Q*, preserves the zero
set on every component. Thus a saved complete weak endpoint consisting of a
resolved map m and residual rows R is equivalent, as a zero set, to

    x-m[x]=0 for every coordinate in the map domain,
    R=0, and the declared nonzero branch localization.

Adjoining these equations to a stronger source locus intersects the two
necessary loci. Any solution of the full printed chart lies in that
intersection. No coefficient is projected away, and no component is chosen
from a product of distinct factors. A resulting unit therefore excludes the
full chart once the global jet0 gauge coverage has also been checked.

The two antecedents use different wrappers because the stronger computation
adds the D1 nonzero differential face. Matching variable names alone would
not justify their identification. The merge driver now compares actual
h3,C2,C3 and outer-block coefficient images, all residual source equations,
the ordered generator list and the coefficient field against a separately
materialized weak source state. The independent verifier also rebuilds the
source state and checks both antecedents' h3/source map images and outer
specifications; the coefficient engine and source derivation hashes match.
It records an explicit ordered [v,v] coordinate map with its SHA-256.

`minor_merged_verify.py` checks both saved source chains from phase0000,
including every QQ* leader, selected equation, map image and radical power
identity. It independently regenerates the exact graph definitions of every
D1 face coefficient and the D1 differential equations. For the merge phase
it reconstructs EVERY relation x-m[x] from the verified weak endpoint,
substitutes the strong `map_before`, and checks that the complete nonzero
relation set is exactly the saved raw row set. A row can disappear only when
its image is the zero polynomial. The explicit graph-extension generators
remain part of the ring unless an actual QQ* equation subsequently solves
them. Any weak residual rows receive the same treatment.

The remaining global bands follow from the exact source coordinate map
t=1/x,w=y/x. Write F=t^-99*KF and G=t^-66*KG. The coordinate determinant
d(t,w)/d(x,y)=-t^3 gives

    t^163 J(F,G)
      =99 KF KG_w -66 KF_w KG
       +t*(KF_w KG_t-KF_t KG_w).

The monomial coefficient rule for a normalized bracket of degree bounds D,E
is ((D-r)k-(E-s)q) for a t^r w^q and b t^s w^k, contributing at
t^(r+s)w^(q+k-1). Those are normalization degree bounds; a lower-degree
coefficient need not attain its bound. The four outer remainders retain
their extra t factor exactly once.

The product-rule identity for F=H^3+A*H+B and G=H^2+C*H+D removes the
identically cancelling pure H powers before coefficient multiplication.
This is an exact polynomial identity, not a restriction of the chart.
Substituting z=w-1 into the small source blocks before multiplication is a
polynomial ring automorphism and commutes with both derivatives. All the
unknowns remain in the coefficient ring, even when a requested coefficient
does not depend on them.

The maximum actual Jacobian degree is99+66-2=163. The normalized coefficient
at t^r is therefore its homogeneous physical degree163-r part, expressed in
the w^k basis. For each new r the driver includes every coefficient
0<=k<=163-r. At r=163 the sole coefficient is equated to the SAME nonzero
Jc used by the printed D1 face. Thus a run through t163 exhausts the full
Jacobian equation, including its constant coefficient. A unit at an earlier
band already suffices; a nonunit prefix is only a surviving necessary locus.

The verifier can independently differentiate the fully constructed KF/KG to
regenerate terminal rows on the recorded preceding locus. Its optional
factored mode uses the separately checked product-rule identity when direct
construction is too large. Either way, fresh Singular verification first
scales every rational row by a checked nonzero rational to a primitive
integer polynomial, declares the actual ordered QQ ring, applies the branch
localizer, and runs positive and negative inverse-wrapper controls. No
endpoint with parser errors is accepted. Computation stopping before t163
without a unit remains compute-bound; dimension alone is not a survivor
witness of the full chart.
