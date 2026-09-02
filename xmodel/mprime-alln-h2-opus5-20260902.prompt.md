# Research lane: MPRIME-ALLN-H2 — generalize the (M') nodal kill to all degrees under H2 (Path-1 flagship)

DC directive (standing): the campaign optimizes for RESOLVING JC2;
this lane is one of the two endorsed all-degree critical paths.

Context. Under Keller + (H2: A_F irreducible) + (H3), the (M')
identity (round1033-sheet-gate:442, restated in the charged
integrations) reads a(nu+s-1) - sum_p a_p = d*nu - 1 with
1 <= a <= d-2, 0 <= a_p <= a, nu = sum_p (r_p - 1), s = #Sing A_F,
d = N. The charged REP-96 report §7 (R4) verified: at N=4, for
NODAL A_F (nu = s), the identity collapses to
sum_p (a - a_p) = (a-1) + s(4-a), impossible for every s at both
a=1 and a=2 — reproducing the promoted B0-at-N=4-under-H2.
Theorem 7.B (charged all-degree H2 integration) kills trivial
dicriticals at every N >= 3 under H2, so m_triv = 0 and the
weighted budget is 2*m_nt <= N-2.

Task, flagship effort — close the H2 branch at ALL degrees, or
state exactly what survives:
(1) NODAL CASE, ALL N: run the (M') collapse at general d = N.
    For nodal A_F: sum_p (a - a_p) = (a-1) + s(d-a) with
    0 <= a_p <= a, so LHS <= sa. Determine for which (d, a, s)
    the identity is satisfiable and prove the nodal kill at every
    N where it holds. Be exact about small-s and boundary-a
    cases; no hand-waving at a = d-2.
(2) NON-NODAL CASE: nu > s. Classify the singularity profiles of
    A_F (cusps, tacnodes, higher r_p) for which (M') remains
    unsatisfiable, and characterize the survivor profiles
    exactly. Combine with: the budget 2*m_nt <= N-2 (b=0,
    m_triv=0 under 7.B), Theorem N-A where it applies, and the
    dicritical valuation formula e_j = 1 + v_j(dx dy). The goal
    is a theorem of the form "under H2, a Keller map at degree N
    forces A_F's singularity profile into <explicit finite
    family>", ideally empty.
(3) If the family is not empty: name each surviving profile as a
    typed OPEN with its exact data, and identify for each the
    cheapest decisive instrument (the campaign now has: exact
    Groebner via msolve 0.10.1/qqideal, SIROCCO braid monodromy +
    ZvK enumeration, the S_N representation gates TB-GERM/CABLE-3
    and their proven-general congruences, Shirane/N-A/torus
    exclusions).
(4) Interface check (theorem-interface composition pass, per
    protocol): does your all-N nodal kill compose with the
    one-cusp horn work (A2 horn, OPEN[A2-CELL-32]) — i.e., does
    the horn case sit inside a profile your (2) kills or keeps?
    State the exact interface.
(5) Typed verdict block + deviations. Hostile standard; every
    inequality derived, not asserted; watch the a_p <= a
    saturation cases.

Report: `xmodel/mprime-alln-h2-opus5-20260902.md`.
Seal-at-completion contract: skeleton WITHOUT the marker, bounded
per-section writes (<1500 words each), seal only at completion.
Target 25-35KB.
charged_input=xmodel/rep-96-inner-opus5-20260901.md
charged_input=xmodel/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
charged_input=xmodel/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  {{LANE_INPUTS}}/rep-96-inner-opus5-20260901.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  {{LANE_INPUTS}}/block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  {{LANE_INPUTS}}/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```
