# Research lane: CARD-C-STEP0 — pin the degrees for the direct F solve

Round-20260902T0022Z synthesis: the highest single-shot item is
the direct solve for a Keller F from prescribed dicritical data
(opus submission §6/Card C): td=4, W=(1,2), D_1 = the realized
(9,6,2) curve (q=t^6+8t^2, p=t^9+12t^5+24t as its
parametrization), J(F)=1. EMPTY kills (9,6,2) outright; NONEMPTY
is a CE candidate. The BLOCKING desk step is yours:
(1) From td=4, the weight vector W=(1,2), and the (9,6) place at
    infinity, derive deg f, deg g, and the contact order of F
    with L_inf. Derive, not assume: use the charged cage r2's
    component/weight constraints and REP-96 §1/§7 profile data.
    If the degrees are NOT pinned by this data, say so exactly
    and enumerate the finite set of admissible degree pairs if
    one exists; if unbounded, the card dies (SCOPE-CONFLICT with
    the banked-tried GGV degree farm — typed, do not drift).
(2) Write the exact ideal specification (variables, generators
    schematically, the two germ conditions as coefficient
    equations) ready for qqideal transcription — do NOT run CAS;
    spec only, coefficient-level, with the (9,6,2)
    parametrization embedded as boundary data.
(3) GGV firewall (fable submission §4c): the gcd>=16 / !=2p
    bounds apply to (deg P, deg Q) of the MAP — check your pinned
    degrees against them; a violation kills the configuration at
    desk level (state it as such, sourced to GGV custody
    8b426751).
Report: xmodel/card-c-step0-opus5-20260902.md
Seal-at-completion contract; target 15-25KB.
charged_input=xmodel/ideation-20260902T0022Z-opus5.md
charged_input=xmodel/rep-96-inner-opus5-20260901.md
charged_input=xmodel/reducible-all-n-r2-opus5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
dcd40a425b2a2782deebec3f01c3b6859a8aa8d46b3e60639f9865a807d5ddba  {{LANE_INPUTS}}/ideation-20260902T0022Z-opus5.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  {{LANE_INPUTS}}/rep-96-inner-opus5-20260901.md
bdd857c9d8c55fa000fcffee05f9f3084c5d073fb4d06285edf2af0d3c369339  {{LANE_INPUTS}}/reducible-all-n-r2-opus5-20260901.md
```
