# Final audit of OwnVRouteTree

Reviewed `box/lib/own_v_routes.py` against the existing operative
`box/centre-gate-20260903/opus5_probe.py` structural/ODE tree and the printed
major-disc construction. No library edits or additional screens were made.

**Verdict:** no unsound exclusion or missing denominator state was found
within the stated reduced-source necessary-configuration scope. A passing
witness remains a combinatorial necessary witness, not coefficient or pair
realization, and does not close the Prop6.3 radius licence for u_s>1.

The current centre stabilizer is determined by the nonzero exponents already
in its common centre. If their denominator lcm is L, the fixing group is the
Galois group over k((t^(1/L))). At a radius delta the relative coefficient
orbit length is den(L*delta). A zero coefficient does not change this field;
a nonzero coefficient changes it to denominator lcm(L,den(delta)). Distinct
nonzero coefficients or common terms within the same field do not change
that denominator rule.

There is no omitted source of denominator enlargement between recorded
radii. In the subgroup fixing the inherited centre, the selected multiset
from Prop5.3 is invariant. Any term shared by that entire multiset before
its next minimal-disc radius must be fixed by this subgroup. Otherwise its
conjugates would already part at that exponent, contradicting the next
radius's minimality. Such a shared off-radius coefficient therefore lies
in k((t^(1/L))) and its denominator divides L. The first-support zero-centre
argument is the L=1 instance of this same statement.

The bottom predicate correctly uses A1=den(L_actual*delta1). The p.188
conjugation/coprimality argument for (12)/(13) needs the cyclic group fixing
the common centre. Replacing that group by the smaller one fixing every
previous *radius denominator*, even when its coefficient was zero, weakens
the necessary test. The corrected modulus can therefore reject rows that
passed the old abstract-radius modulus; this is an intended correction,
not a new cap. The reduced-source Prop5.6 rule is required for the bottom
all-zero/removable-centre rejection and remains an explicit hypothesis.

Every above-threshold p factor extends to a major disc by Prop5.3 (also
p.200(4)); this includes compulsory nonselected siblings. The recursion
checks the zero major sibling and every nonzero major orbit multiplicity.
Conjugate coefficients have isomorphic numerical subtrees, so one witness
per such multiplicity is sufficient for a necessary test. Distinct
nonconjugate orbits with the same multiplicity may share that numerical
witness here because compatibility of their actual coefficients is not
claimed. This can retain unrealizable objects, but cannot wrongly exclude
an actual source whose subtrees would furnish witnesses.

The loops are exhaustive for the declared combinatorial model: every
nonnegative z congruent to P modulo A is considered; remaining mass is
partitioned into all permitted positive orbit multiplicities with repetition;
selected zero/nonzero modes and the requested first-support index are
handled separately. The memo key retains j, upper multiplicities, L, danger,
selected suffix, and requested first-support index. The ODE resonance
exclusion, basic q-root orbit capacity, and bottom (12)/(13) tests match the
original operative settings. No stronger q-capacity congruence, passport,
child U-NEG, C-TOP, or child-major bound was added by this audit.

`audit_route_witnesses.py` is an independent validator that does not import
`own_v_routes`. It recomputes radii, P,Q,A, centre lattices, bottom moduli,
selected first-support constraints, and all compulsory major continuations
from the saved witnesses. It checks exact p mass, q-root capacity, resonance
exclusions, and the bottom congruences. **DETERMINED:** 90 root witnesses,
442 node occurrences and 244 bottom occurrences PASS. These are artifact
counts; repeated subtrees can be checked more than once.

The recorded refinement considers the 327 preliminary routes and retains
90 routes in 90 rows, all with a singleton necessary vector. Of those, 25
are among the separately excluded finite-pole rows. **DETERMINED:** 65
nonempty necessary vectors remain: 45 with u_s=1 and 20 with u_s>1. The
last 20 still require the actual Prop6.3 radius hypothesis before descent
is licensed. No count here asserts how many polynomial pairs exist.

Evidence: `route-witness-audit.json`, `audit_route_witnesses.py`, and the
existing `full-source-routes.json`. No new exit-price assertion is made.
