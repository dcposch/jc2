# Audit of monic coefficient-quotient computation

The quotient optimization is safe only after its relation is proved on the
current full source locus. The intended transition obtains exact generators
of the current residual ideal, including a monic quadratic q in the retained
face coefficient d, and verifies both ideal inclusions before changing the
residual presentation. An unverified relation or a relation from a convenient
point would instead define a restricted chart and could not support a kill.

Write q=d^2+a*d+b, where a,b lie in the polynomial coefficient ring R of all
other retained source coordinates. Because q is monic, polynomial division
works over R itself: it never divides by a parameter or a potentially
vanishing leading coefficient. The quotient R[d]/(q) is a free R-module with
basis1,d. Its exact multiplication law is

    (A+B*d)(C+D*d) = (A*C-b*B*D) + (A*D+B*C-a*B*D)*d.

This proves the rank2 representation on every base point, including repeated
or nilpotent specializations of the quadratic. It chooses no conjugate and
requires no discriminant or parameter localization. d remains an unknown in
the represented ring. The base implementation may omit d from the native
polynomial coefficient context only because its image is explicitly the
module element(0,1), and the decoder restores the combined polynomial A+B*d.

A new equation is the SINGLE polynomial A+B*d=0 in the declared quotient.
Replacing it by A=0 and B=0 would impose a stronger condition and is not
permitted. The production pair kernel and the independent direct-F/G kernel
both decode one combined row. The defining q must remain explicit in every
ambient residual ideal/Singular computation, even though its normal form is
zero in the quotient implementation.

For every raw source coefficient f, division gives the exact identity
f=NF_q(f)+q*g for a polynomial g. Thus f=0 and NF_q(f)=0 are equivalent on
the already proved q-locus. Addition, multiplication and the t/w coefficient
projections commute with this quotient map. The quadratic coefficients depend
only on the unknown source coefficients, not on the physical source
coordinates x,y or their normalized variables t,w. Hence the source
derivations also commute with the quotient. This justifies reducing during
the polynomial products rather than first constructing enormous unreduced
intermediate expressions.

The independent helper `minor_flint_quotient_direct.py` implements a generic
monic quadratic, supplied as data rather than entering the production q
coefficients in its code. It constructs complete normalized F/G in the rank2
ring, differentiates those polynomials directly, and changes z to w-1 only
after extracting the requested coefficient. Its algorithm therefore differs
from the production factored-Jacobian kernel. It declares each native QQ
generator image, retains d as(0,1), verifies q maps to zero while d does not,
and emits the combined rows. Controls compare every coefficient t0..6 with
an unreduced SymPy construction followed by ordinary monic polynomial
remainder; they include d^3 and d^4 source coefficients and rational quadratic
coefficients. The comparisons pass without selecting either root of q.

During review, a real closure-shadowing hazard was found in an early scalar
normalizer: its quadratic constants A,B were subsequently rebound to outer
series dictionaries. A high-power input happened to fill the recurrence cache
before rebinding and masked that path. The production helper was corrected to
use distinct names qA_native/qB_native before any quotient production launch;
a new control starts with only d-linear inputs so exponent2 first appears
during multiplication. Earlier versions remain controls only.

The terminal verifier must regenerate the rows in the same proved quotient,
carry its exact generator order and relation, and compare the combined
polynomials before the new reduction. The full source maps must remain
equivalent modulo q, with q explicitly retained. A final unit is meaningful
only after the source, graph, gauge, quotient-transition, ancestry and endpoint
checks all pass. This note does not assert a branch verdict.

## Frozen v4 actual-locus verification

`minor-verification-code-v4/` is an immutable six-file snapshot. The first
actual δ2 run, `authoritative-v4-delta2-verify.json`, passed the entire
ancestry through J66 and the quotient transition at dimension230. The
previously executed v2 source/weak/merged prefix is reused only after each
individual phase's content hash, the exact previous input hash, the loaded
frozen verifier hashes, and all source and antecedent identities match.
The newly encountered maps are replayed as ordinary polynomial identities.
No equality modulo q is used to justify a QQ* coordinate elimination.

`minor_quotient_transition_verify.py` independently takes the current
`residual_before`, the four actual new rows and the complete declared
coordinate ring. It reconstructs the ring in Singular, checks the ordered
variable images and characteristic, clears denominators by recorded nonzero
rational scalars, and computes K⊂I, std(I)⊂std(I+K), and the reverse inclusion.
It checks equal dimensions and positive/negative branch-localizer wrappers.
Only after these three exact ideal inclusions pass does the verifier activate
the monic quadratic relation. It verifies the explicit polynomial is monic
in d, the three graph rows have their recorded polynomial images, and every
following phase retains q as an actual residual generator and never pivots
on d or e. This is a quotient by an already imposed equation, not a floor
restriction, root selection, or coordinate deletion.

For a subsequent Jacobian band the independent backend constructs complete
normalized F and G in the rank-two coefficient algebra and differentiates
them directly. It substitutes z=w−1 after obtaining the band. The production
backend instead substitutes w first and expands the factored bracket. The
verifier checks the entire total-degree support, including every omitted
zero coefficient. Each recorded row minus the independently regenerated row
has zero monic remainder; the row remains a single A+B·d polynomial. Cached
production bands may acquire higher powers of d after later QQ* graph
substitutions; this is handled by comparing their classes in the same proved
q ideal, not by changing the recorded elimination equations.

`minor-v4-controls.json` passed fourteen generic direct F/G controls: all
bands t0–6 with initially d-linear inputs, and all bands t0–6 with nontrivial
higher d powers. Raw SymPy differentiation followed by monic division agrees
coefficient by coefficient with the frozen independent pair arithmetic.
The controls reject a nonmonic relation, wrong coefficient field, bad pivot
leader and undeclared map coordinate. The example q=d²−e with the combined
row d−1 is nonunit; illegally separating its two coefficients gives a unit,
which the control explicitly demonstrates. Thus neither quotient conjugate
is silently selected or discarded.
