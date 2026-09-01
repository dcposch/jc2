# Research lane: CORRECTED-SUITE-CODEGEN — faithful characteristic ideals as runnable jobs

The encoding audit (charged) proved all six generated
characteristic ideals UNFAITHFUL: the (8,6) jobs used odd
coefficients of the RAW binomial p^3-q^4 without reducing even
pole-order terms; the (9,6) jobs forced the raw binomial p^2-q^3
to the target degree, zeroing legitimate approximate-root
coefficients. The audit specifies corrected equations per type
(its sections 4-5 and the per-type table). The Moh check
(charged) independently specifies the same job for (8,6,3) as
FSY's I_29: after the NR normal form, nine coefficients remain
and ten odd vanishings h_23..h_5 are imposed, h_23 already spent.

Task: transcribe the audit's CORRECTED equations into runnable
jobs, one file per type, for the four types still needing
computation:
  P1 (8,6,3)  — the I_29 job (decisive; MOH-CHECK route died, this
                is the only curve-level kill path left for it)
  P2 (8,6,9)  — corrected type B
  P3 (9,6,4)  — corrected locus is NONEMPTY; encode the SIX-NODE
                question (corrected ideal + the I_DP nodal
                conditions: delta_aff=6 for this type — verify
                the census number from the audit before encoding)
  P4 (8,6,11)+(8,6,7) — corrected ideals for the record ONLY
                (rep-level dead; mark files as archival, lowest
                priority, do not let them consume P1-P3 effort)

For each type produce:
(a) `box/corrected_<type>.ms` — msolve GROBNER-mode input
    (remember the convention: basis=[1] means UNIT IDEAL means
    EMPTY — write this in a header comment in every file);
(b) `box/corrected_<type>.m2` — Macaulay2 mirror (M2
    authoritative; recall the footguns: `first degree`, no `pi`
    as a variable, `diff(var,poly)` argument order, name maps
    before applying, close stdin);
(c) a derivation section in your report showing, coefficient by
    coefficient, that the encoded equations ARE the audit's
    corrected ones — the reduced-remainder h_k (or the audit's
    corrected residual with added degrees), not raw coefficients.
    Any place the audit's spec is ambiguous: STOP, record the
    ambiguity as an OPEN, encode both readings as _a/_b variants.

Self-checks REQUIRED before sealing: (i) the audit's charged A
false-positive point must FAIL your corrected (8,6,11) system;
(ii) the audit's explicit (9,6,2) curve (q=t^6+8t^2,
p=t^9+12t^5+24t) must PASS a corrected (9,6,2)-membership check
if you encode one; (iii) the HF-twin (9,6,4) point must PASS your
corrected (9,6,4) locus equations (before the nodal conditions).
Run these checks symbolically in your sandbox (sympy is
available); record pass/fail verbatim.

Report: `xmodel/corrected-suite-codegen-grok46-20260901.md` with
derivations, self-check transcripts, and per-file SHA-256 of the
emitted job files. Seal-at-completion contract: skeleton without
the marker, bounded per-section writes, seal at completion.
charged_input=xmodel/encoding-faithfulness-audit-r2-sol56-20260901.md
charged_input=xmodel/moh-check-863-grok46-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
a3c7137cdb2cf46c7d9026cfbcba54b0b6e5b47a6ef36ad7ee2976a905c8b196  {{LANE_INPUTS}}/encoding-faithfulness-audit-r2-sol56-20260901.md
c4ee11caa6e5b37e1c7b3a3089709b98d3e07612eee2913418c183195d756c7f  {{LANE_INPUTS}}/moh-check-863-grok46-20260901.md
```
