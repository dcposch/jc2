# Independent coefficient-circuit audit

The coefficient circuit is algebraically equivalent to the full remainder
backend. Its graph construction, exact t cutoffs, whole leader subtraction,
and positive/negative controls pass independent review. This does not assert
a unit or a proper ideal for either actual source client.

Every nonconstant coefficient of H,v,U first receives a fresh graph variable
with equation `new-old_expression=0`. Next the code computes the coefficient
convolution of v^2-UH. It keeps **every** coefficient with z-degree>=k as a
zero equation. Each coefficient at z-degree<k receives its own monic graph
variable R. Finally selected coefficients of H^2 and vU receive monic graph
variables before the characteristic coefficient convolutions are formed.

These definitions are acyclic: each new expression uses only source variables
and earlier graph variables. Their coefficients of the newly defined variables
are exactly1. Successive elimination therefore gives an isomorphism from the
graph scheme to the full original coefficient scheme, with no localization,
specialization, extra component, or point selection. Keeping graph variables
instead of expanding their substitutions changes arithmetic cost only.

All products are indexed by exact t,z positions. The full remainder R is kept,
including its high t bands. A product term can be discarded from the final Q
coefficient computation precisely when its t order exceeds the required
inclusive depth, since all participating t exponents are nonnegative. The H^2
graph is retained through `max(depth-minR,depth-(4k-2))`, covering both RH^2
and p*t^(4k-2)*H^2. The vU graph is retained through depth-1 for its later
factor tH. The t*vR and t^2*U^2 products have their corresponding depth-1
and depth-2 cutoffs. The p*v and q terms use their actual shifts. Thus none
of these bounds assumes a parameter polynomial is zero or replaces its true
coefficient expansion by a support picture.

The final Q expression is the already proved identity

    (3R/4+p)H^2-vUH/8+vR-9U^2/64+pv+q

with the exact normalized shifts. The whole target is subtracted at depth141
for99 or151 for108. The source H0 times the H-adic quotient face gives the
printed homogeneous target; any optional source graph defining H also remains
as coefficient equations. The leader and separation localizers are retained.

The optional `graph_h_expr` input is valid provided its new source-H coefficient
variables occur monically at their declared positions and are absent from the
old graph expression. That is a separate input-map obligation; matching names
alone cannot prove it. The18 prepared99 circuit inputs do not use this extra
input graph: their full h3/C2/C3 expressions are retained and the backend makes
the ordinary internal H coefficient graph described above.

The final Singular ring contains the complete input parameter list followed
by the new graph variables. It omits the physical coefficient-extraction
variables t,z. Accordingly its dimension is already the coefficient-scheme
dimension. Do not subtract the two physical variables as in older normalized
backends. A99 jet0 gauge run still requires the separate +1 adjustment when
comparing with the free-centre source chart.

The result reader was hardened during review to require a successful process
return, no parser/CAS error, full result markers, controls exactly0/1, and an
unchanged emitted-script hash. Any incomplete or resource-bound computation
remains OPEN; a printed intermediate ideal size is not a properness proof.
New graph generator names must also remain distinct from all input generators.

`circuit_projection_control.py/.json` independently reads the actual positive
and wrong-face negative Singular scripts. It successively eliminates all10
monic graph variables in each, checking that every image lies in the original
parameter ring. The resulting nonzero row multisets are **exactly equal** to
the independently expanded Sympy source equations, all high-z remainder rows,
full inclusive Q coefficient rows, and localizers over Q. This checks all graph
layers together, including the p contribution and leader subtraction.

Both actual scripts were rerun with local Singular. The correct-face control
returned reduce-one1, dimension0; the wrong-face control returned reduce-one0,
dimension-1. Both returned the complete0/1 localization controls without parser
errors. Their input, script, output and independent-verifier hashes are retained.
These are backend controls and deliberately do not satisfy the actual D2 faces.

The complete18-input99 preparation has a further independent audit at
`../g9966/circuit-inputs/verification.json`, statusPASS. It checks every original
source image under jet0->0 and then under every rational front graph, each raw
front row after the map, every retained residual, declared generator closure,
the stage-specific proved cutoffs, and exact regeneration of the circuit API
expressions. All18 inputs passed sha256sum-c locally and on the worker. Exact
snapshots of all10 proof/control sources are retained under that directory's
`proofs/`, linked by `proof-custody.json`. No missing coordinate or inferred
gauge is hidden by the coefficient-circuit optimization.
