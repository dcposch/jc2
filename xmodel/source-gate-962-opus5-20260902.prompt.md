# Research lane: SOURCE-GATE-962 — the retyped source question with three stacked razors, Mode 1 on (9,6,2)

Round-20260902T0022Z synthesis merge lane. Three blind
submissions independently retyped OPEN[REP-96-SOURCE-IS-C2]:
the SHEET-GATE Y=Spec B is NEVER C^2 (charged sheet-gate report,
Lemma 2.2); the correct question — now OPEN[SOURCE-OPEN-U] — is
whether the Riemann-existence cover of a surviving representation
admits a Zariski-open U ~ A^2 with curve complement and
SHEET-GATE-matching four-box numbers. Your tasks:
(1) Formalize the retype precisely (charged: grok submission §3,
    sol submission §1/§4, opus submission §3.1 — reconcile their
    three statements into ONE typed object; they are consistent
    but differently worded).
(2) Stack the three razors as necessary conditions on one input
    and run MODE 1 (irreducible A_F) on the realized (9,6,2)
    with its banked SIROCCO cycle types:
    (a) HOM-COVER: H^ab torsion=0 and rank = component count
        (opus submission §3, instrument box/cover_h1.py in repo —
        verify its 4 controls yourself before trusting);
    (b) FOUR-BOX EULER: chi_c(Y)_RH vs 1+chi_c(B_Y) from
        conjugacy-invariant cycle types only (grok submission §3;
        (a,sigma,ram)=(2,2,2) expected; compactification must be
        NAMED or the run returns OPEN[RH-LINE-AT-INFINITY]);
    (c) BOUNDARY LATTICE: det L-tilde-infinity <= 0 on the
        declared U-completion (sol submission §4; DET-LINF is
        banked unconditional).
    Mode-1 expectations are typed in grok submission Card I
    (mismatch = confirmatory of H2+(M'); match =
    OPEN[MODE1-MATCH-VS-H2], not a CE).
(3) Also emit the cycle-type->chi calculator spec serving BOTH
    this and (8,6,9)'s c_2(T) (grok submission §4: same Chern
    species) — box/covergeo.py, fail-closed, footguns #10/#11
    honored, positive control (9,6,2) four-box, negative control
    (6,4) at E=-3.
(4) Carry OPEN[ACS-FIX-VS-DEFICIT] (opus submission §4)
    throughout: a^(i) <= #Fix, equality is a hypothesis.
Typed verdicts; deviations; hostile standard.
Report: xmodel/source-gate-962-opus5-20260902.md
Seal-at-completion contract; bounded writes; target 25-35KB.
charged_input=xmodel/ideation-20260902T0022Z-opus5.md
charged_input=xmodel/ideation-20260902T0022Z-grok46.md
charged_input=xmodel/ideation-20260902T0022Z-sol56.md
charged_input=xmodel/rep-96-inner-opus5-20260901.md
charged_input=xmodel/round1033-sheet-gate-opus5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
dcd40a425b2a2782deebec3f01c3b6859a8aa8d46b3e60639f9865a807d5ddba  {{LANE_INPUTS}}/ideation-20260902T0022Z-opus5.md
83319c5e0ddbdb2bfa43b983aae28c57474703205e244cda6e1460942e5809b9  {{LANE_INPUTS}}/ideation-20260902T0022Z-grok46.md
4b0e4dde91a8bbe06dfde68e0c8c4559d92bcb8355a0b57acf32ba8b36a7d3b4  {{LANE_INPUTS}}/ideation-20260902T0022Z-sol56.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  {{LANE_INPUTS}}/rep-96-inner-opus5-20260901.md
6d8f6667fc7d52d1e46fc4ac55f2aa2049603f06c1764ae4ac51b078435d90eb  {{LANE_INPUTS}}/round1033-sheet-gate-opus5-20260831.md
```
