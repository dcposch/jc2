# Verification lane: NORI-BC report — computation and countermodel arm

Second arm of a paired review; independent of the gate; computations
and countermodels only.

charged_input=xmodel/nori-bc-extension-opus5-20260831.md
charged_input=xmodel/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
64bcabd1e14d69026cc86e101ff266a92009c7f15e9dfc00dce88fb607e7560f  {{LANE_INPUTS}}/nori-bc-extension-opus5-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  {{LANE_INPUTS}}/block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

Targets: (1) Lemma 3.1 blow-up bookkeeping at k=1,2,3 explicitly
(multiplicity sequences, self-intersection drops, s(A_{2k-1})=4k);
(2) Theorem N-A numerics on three synthetic configurations of your
own design (choose C^2, r_1, T, T_x on both sides of (3.1)) plus the
two bitangent conics (compute B(C_i), the failure by one unit, and
verify pi_1(P^2 - two bitangent conics) = Z * Z/2 by an independent
route — e.g. the double cover or known references you fetch and
hash); (3) the Zariski-sextic data (B=36>0, pi_1 = Z/2 * Z/3 —
source it); (4) Cor N-A-RES algebra: re-derive
`C'^2 - 2r_1 - 4T = 3d-2-M_infty-2T` from the charged Lemma 4.3 and
check the (6,3) table completely (every beta_1 with 3∤beta_1,
7<=beta_1<=10: the delta_infty, M_infty, delta_aff, gate, and which
T survive); also run the SAME analysis at (6,2) and (6,4) rows
(a=4 resp 2 at infinity — derive the germ constraints and the
(M-INF-T) gate numbers; note the banked (6,4) beta_h=15 curve from
the M-INF review has a TRIPLE point — check whether its infinity
type is compatible with the double-points-only residual class);
(5) the rational-sextic-with-5-tacnodes extremal object: compute its
would-be invariants (delta=T=10, genus 0 check via
(d-1)(d-2)/2 = 10) and survey sources (fetch/hash) for existence or
impossibility of a rational plane sextic with 5 tacnodes and no
other singularities. Verdict per target: HOLDS / BROKEN /
UNTESTABLE-AT-DESK.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/nori-bc-verification-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,000 words. Do not include a `charge_basis` declaration.
