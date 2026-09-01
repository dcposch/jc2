# Research lane: BM-FACT-CODEGEN — braid-monodromy decision computation for the realized (9,6,2) curve

The charged REP-96 report §7 (R1) names the cheapest decisive
step on the campaign's strongest counterexample substrate: for
the realized (9,6,2) curve
  q = t^6 + 8 t^2,   p = t^9 + 12 t^5 + 24 t
(D = closure of the image of t -> (x,y) = (p(t), q(t)); exact
relation x^2 - y^3 - 64 y = 64 t^2 on the curve), compute the
full braid-monodromy factorisation of D with respect to the
vertical projection (x,y) -> x, extract the Zariski-van Kampen
relations on the nine meridians, and intersect the fixed-tuple
conditions with the surviving S_4 class list (REP-96 §5, six
classes, 144 tuples). Outcome is binary: an explicit surviving
phi (the campaign's first representation on pi_1(C^2 - D)) or
the kill of (9,6,2) at the representation level.

Your deliverables (codegen + desk math; you do NOT run the heavy
computation — the coordinator runs it on AWS):

(1) `box/bmfact_962.sage` — a Sage script (target: Sage with
    SIROCCO in conda env "sage" on the compute box) that:
    (a) builds the defining polynomial F(x,y) of D (resultant of
        p(t)-x, q(t)-y; verify irreducibility and bidegree; check
        F against the exact relation x^2-y^3-64y-64t^2 by
        eliminating t symbolically as a cross-check);
    (b) computes the certified braid monodromy of the AFFINE
        curve F=0 w.r.t. x-projection (sirocco-backed; document
        which Sage entry point you use and its convention for
        base point, generator ordering, and braid orientation —
        misread conventions are the top hazard class here);
    (c) VALIDATES the REP-96 §1 census from the computed braids:
        eight simple tangency braids (single sigma_i) in eight
        distinct fibres + one fibre (x=0) with four commuting
        sigma_i^2; exponent ledger 8 + 4*2 = 16. ABORT with a
        loud marker if the census disagrees (that would refute
        REP-96 §1 and must surface, not be papered over);
    (d) emits the nine-strand permutation data and, for each
        braid in the factorisation, its induced automorphism of
        the free group F_9 (ZvK action) in a machine-readable
        form (JSON lines).
(2) `box/bmfact_enum.py` — pure python (no Sage) that consumes
    (1d)'s JSON plus the REP-96 §5 class list HARD-CODED FROM THE
    CHARGED REPORT (all six classes; also carry the Pi-tau pin as
    an assertion, not a filter) and enumerates ALL maps
    xi_1..xi_9 -> transpositions of S_4 satisfying every ZvK
    fixed-tuple relation with im = S_4. Print: per-class counts,
    total survivors, and if nonzero, the explicit surviving
    phi(s) verbatim. Include a NEGATIVE CONTROL (a fake extra
    relation that provably empties the set — run and show 0) and
    a POSITIVE CONTROL (drop all relations except the product
    relation — count must match REP-96's 144).
(3) Derivation section: the ZvK relation extraction from a braid
    word (state the convention and cite it), why the affine
    computation suffices for the meridian data here, and the
    exact correspondence between REP-96's (X, Y, T_1) classes and
    your xi-tuples. Any ambiguity in REP-96's conventions: STOP,
    type it OPEN, encode both readings as variants.
(4) Self-checks runnable WITHOUT Sage (sympy): the resultant
    F(x,y) expansion double-check; the discriminant-in-x root
    count (expect: eight simple tangency values + x=0 + anything
    else? account for EVERY root of disc_y F including infinity
    contributions, verbatim table).

Report: `xmodel/bm-fact-codegen-grok46-20260901.md`, per-file
SHA-256 of emitted scripts, self-check transcripts verbatim.
Seal-at-completion contract; target 20-30KB.
charged_input=xmodel/rep-96-inner-opus5-20260901.md
charged_input=xmodel/encoding-faithfulness-audit-r2-sol56-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  {{LANE_INPUTS}}/rep-96-inner-opus5-20260901.md
a3c7137cdb2cf46c7d9026cfbcba54b0b6e5b47a6ef36ad7ee2976a905c8b196  {{LANE_INPUTS}}/encoding-faithfulness-audit-r2-sol56-20260901.md
```
