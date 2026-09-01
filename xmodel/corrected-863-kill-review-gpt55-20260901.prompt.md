# Review lane: CORRECTED-863-KILL-REVIEW — gate the (8,6,3) curve-level kill

Two-engine computational result to be gated: the corrected
Delta=(8,6,3) incidence system is EMPTY over QQ — msolve
Groebner mode returned basis=[1] (unit ideal) and the M2 mirror
returned dim=-1, gb=|1|, rc=0, char 0. If the ENCODING is right,
type (8,6,3) is killed at the curve level (this was the last
curve-level path for it: the Moh route died, and TB-G2 found no
local rep-level obstruction). Your job: hostile review of the
encoding chain, NOT of the computation.

Review tasks:
(1) The charged codegen report's derivation section for P1
    (8,6,3): verify coefficient-by-coefficient that the encoded
    system IS the charged audit's corrected specification
    (audit §7.1): closed conditions g_j=[t^j]G86=0 for j=4..22
    with G86 = p^3-q^4+a22 p^2 q+a20 p q^2+a18 q^3+a16 p^2+
    a14 p q+a12 q^2+a8 p+a6 q, open g_3 != 0 (Rabinowitsch),
    gcd-cover colon (B,D,F,gam,e). Re-derive independently from
    the audit's spec; do not trust the codegen's own transcript.
(2) The job files as-run. Verify hashes, then read from the repo:
    `box/corrected_863.ms` SHA-256
    cd13e1c25bcfcc43d30c238420ab8383580b8c078b16c0b0ff967ff43761d75b
    `box/corrected_863.m2` SHA-256
    411b2e865602aefc8c3bc9993318e3980a62cf21ae5ad3ac30c3b4ec446fd74f
    Check BOTH files encode the same ideal (same generators, same
    ring, same opens), and that the .ms variable order/count
    matches its polynomial list (msolve parses line 1 as the
    variable list — in-band-comment hazard is documented handled).
(3) COORDINATOR PATCH AUDIT: the .m2 file was patched by the
    coordinator after the codegen lane sealed (tower-ring
    numgens asserts corrected to ==1; the killt map rewritten as
    map(R0, St, {0_R0}); gj rewritten from
    killt(coefficient(G86poly, t^j)) to coefficient(t^j, G86poly)
    per an on-box probe showing coefficient(monomial, poly)
    returns base-ring elements). Verify the patched gj extracts
    the SAME coefficients the audit spec means: in the tower ring
    R0[t], is coefficient(t^j, G86poly) the coefficient of t^j
    with all a-variables and chart variables in the base? Any
    silent-zero hazard (wrong-ring monomial, degree-0 edge at
    j=4..22)? A silent-zero here would fake EMPTY — treat this as
    the single most dangerous failure mode of the whole kill.
    Cross-check at least three g_j against a sympy expansion of
    G86 with the audit's p,q normal forms.
(4) The EMPTY semantics: unit ideal BEFORE the colon/saturation
    steps — confirm from the .m2 flow that Iopen==(1) suffices
    for the kill claim (the Rabinowitsch open is part of Iopen;
    emptiness of the open locus is what the type needs — check
    against the audit's statement of what the corrected locus
    parametrizes, including whether any LEGITIMATE (8,6,3) curve
    could sit inside the gcd-cover locus that the Rabinowitsch
    var does not already exclude).
(5) Self-check (i)-(iii) transcripts in the codegen report:
    re-run at least (ii) ((9,6,2) exhibit passes its corrected
    membership) yourself in sympy as a positive control of the
    corrected-encoding METHOD (a method that kills everything
    would also kill the realized curve's system).

Verdict: KILL-BINDING / KILL-BLOCKED (name the defect) /
REPAIRS (list). Report:
`xmodel/corrected-863-kill-review-gpt55-20260901.md`.
Seal-at-completion contract; target 15-25KB.
charged_input=xmodel/corrected-suite-codegen-grok46-20260901.md
charged_input=xmodel/encoding-faithfulness-audit-r2-sol56-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
d80c691861d362f1569b38c80a222c2df4992e62f13297adc2e5a996d99a0f18  {{LANE_INPUTS}}/corrected-suite-codegen-grok46-20260901.md
a3c7137cdb2cf46c7d9026cfbcba54b0b6e5b47a6ef36ad7ee2976a905c8b196  {{LANE_INPUTS}}/encoding-faithfulness-audit-r2-sol56-20260901.md
```
