# Hostile review: NORI-BC report (Opus) — is Theorem N-A sound?

Different-model gate for a flagship extension. The charged report
claims: Theorem N-A (Nori 3.27 extended to double points of smooth
branches via k_p blow-ups at each A_{2k_p-1}: hypothesis
`C^2 > 2r_1 + 4T + T_x`, conclusion kernel abelian); sharpness of the
`T_x` coefficient (two bitangent conics fail by one unit and the
conclusion is FALSE there); REFUTATIONS of the naive `B(C)>0`
extension (Zariski sextic; bitangent conics), of local-transversality
replacement, and of the 3.26 substitution; Corollary N-A-RES: the
residual gate becomes `M_infty + 2T <= 3d-3` implying
`pi_1(C^2-D_1) = Z`; the (6,3) row closed except
`(beta_1,T) in {(7,4),(8,3)}`; two errata in Nori's printed text
(the factor 2 inside A(C;P); Remark 6.6's s(node)); and typed OPENs
including OPEN[NORI-BC-SELF-TANGENT-COEFF] with the rational-sextic-
with-5-tacnodes extremal test. Default to refutation.

charged_input=xmodel/nori-bc-extension-opus5-20260831.md
charged_input=xmodel/pi1s4-close-residual-hostile-review-sol56-20260831.md
charged_input=xmodel/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
64bcabd1e14d69026cc86e101ff266a92009c7f15e9dfc00dce88fb607e7560f  {{LANE_INPUTS}}/nori-bc-extension-opus5-20260831.md
aa41551f14f34bdae34d9f172be253882f67c8cc3c6cc699ed98b5b85bbc60f0  {{LANE_INPUTS}}/pi1s4-close-residual-hostile-review-sol56-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  {{LANE_INPUTS}}/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

Verify: (1) §1's verbatim Nori consumption — re-fetch Numdam
(`1b848c19...`), check EVERY quoted statement and BOTH claimed errata
against the actual pages (the errata are load-bearing: if the printed
text is right and the report wrong, N-A's numerics shift); (2) §2's
location of the transversality consumption (two places) and the
normal-bundle reading `B(C) >= deg N_h`; (3) Lemma 3.1 (s=4k and the
resolution shape: k blow-ups separating branches, exceptional
configuration, transversality of the last E_k) — re-derive at k=1,2;
Lemma 3.2 (blow-up invariance of the kernel); (4) Theorem N-A's proof
assembly: nodality of the strict transform, transversality with
E-tilde, the numerics `C~^2 = C^2 - 4T - T_x`, `r(C~) = r_1`, and
Nori 3.27's hypotheses ALL discharged on X-tilde; (5) both pi_1
countermodel computations in §4 (Zariski sextic pi_1 = Z/2 * Z/3;
bitangent conics Z * Z/2) — re-derive or source them; (6) Cor
N-A-RES: the algebra from charged Lemma 4.3, the T_x=0 claim for
irreducible D, the simply-connected endgame, and the (6,3) table row
by row (re-derive beta_1 parity/divisibility, delta_infty, M_infty,
delta_aff for each beta_1); (7) §6's (ii-a) refutation and the two
remaining halves. Verdict per item + promotion recommendation with
exact scopes.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 4 hours hard budget.

Write one report and no other file:

```text
xmodel/nori-bc-hostile-review-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
6,000 words. Do not include a `charge_basis` declaration.
