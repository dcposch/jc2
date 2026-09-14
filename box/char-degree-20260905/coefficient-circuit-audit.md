# Independent coefficient-circuit audit

Audited immutable driver: `d108/coefficient_circuit_backend_v2.py`, SHA-256
`17a825098e24dcbeb973d7fe6f254c6f5884f2aad9bed196e12166db0520ce35`.
The coefficient-circuit presentation is algebraically equivalent to the
previously audited full remainder row ideal under its stated input maps.

Each H,v,U coefficient is either a rational constant or a new variable
with an equation `new-variable minus its polynomial expression`.
Next the complete v^2-UH coefficient product is formed: every z-height
at least k is an equation, and each lower coefficient receives another
monic graph variable. Graphs for selected H^2 and vU coefficients are
introduced afterward. All these definitions are acyclic; they depend
only on source variables and earlier graph variables. Successively
eliminating their monic equations proves that projection to the source
ring induces a quotient-ring isomorphism. No auxiliary graph variable
is inverted and no component is lost. The graph extension can change
solver size but does not change whether the ideal is a unit or proper.

If an input supplies an additional h coefficient graph through
`graph_h_expr`, its graph variables must likewise occur monically in
h_expr and be absent from the source graph expression. This is a property
of the actual lifted inputs, which their input-map audit must bind.
The resulting coefficient difference rows then have the same exact
projection property.

All high-remainder coefficients are computed without a t cap. For the
subsequent characteristic product, all t-exponents are nonnegative.
Writing D for the target depth and r0 for the least t-exponent in R,
H^2 is needed only through `max(D-r0,D-(4k-2))`: the first bound serves
RH^2, and the second serves the scalar pH^2 term. When R has no positions,
using r0=D+1 correctly drops its contribution while preserving the pH^2
bound. The vU product is needed through D-1; vR through D-1; U^2 through
D-2. These are exact coefficient truncations because later multiplication
cannot lower t-degree. Every retained leading face coefficient is
subtracted from the matching coefficient, including the entire free
lambda target, and the leader/separation localizers are retained.

`coefficient-circuit-support-control.py/.json` independently compares the
emitter's support-cutoff arithmetic with full sparse exact-Q expansion.
All64 cases pass, covering k=2,3,33,36, empty and nonempty R, and boundaries
before/at/after pH^2 and the scalar shifts. The positive and wrong-target
CAS controls belong to the separately retained driver control receipts;
this audit does not claim to have rerun FLINT locally.

The final circuit ring contains coefficient and graph variables only;
z and t are absent after coefficient extraction. Unlike older arithmetic
backends, its raw Singular dimension therefore needs no subtraction of
two structural dimensions. A completed result must still have all rows
parsed, no CAS errors, correct script/input hashes, and passing localizer
controls. Partial graph construction or an interrupted Groebner basis
calculation proves neither unit nor properness.
