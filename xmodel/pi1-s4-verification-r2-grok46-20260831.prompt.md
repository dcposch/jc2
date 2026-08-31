# Verification lane: PI1-S4 decision report — computation and countermodel arm

Second arm of a paired review; independent of the gate. Explicit
computations and countermodel hunts only.

charged_input=xmodel/pi1-s4-decision-opus5-20260831.md
charged_input=xmodel/block-descent-a1-b0-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
010330d208c5899ce41832f1187b73d9a63268725d809b0370f2b4d9cd66eadd  {{LANE_INPUTS}}/pi1-s4-decision-opus5-20260831.md
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963  {{LANE_INPUTS}}/block-descent-a1-b0-coordinator-integration-fable5-20260831.md
```

Targets:

1. The delta-action formula `delta.(t_1,...,t_d) = (Pi t_d Pi^{-1},
   t_1, ..., t_{d-1})`: verify by direct Hurwitz computation at
   d=2,3,4, and verify `delta^d` = global conjugation by Pi at d=3.
2. Theorem A(3)'s orbit enumeration: for EVERY g in S_4 (by conjugacy
   class), compute the conjugation orbits of <g> on all six
   transpositions and check exactly which orbits generate S_4;
   verify the claimed 3-cycle and 4-cycle orbits and the failures.
3. Exponent-sum cross-check: recompute e(rho_infty) both ways at
   (d,n)=(4,3) and (5,3) using (V), (G), (D).
4. Theorem A consequences: verify the kill-list — (d,n) both odd
   dies; n<=2 dies; and enumerate the surviving (d,n) pairs with
   d<=9 under (C1) + Theorem A(3) divisibility (3|n,d even) or
   (4|n,d odd).
5. Lemma 4.4 blow-up arithmetic: recompute the multiplicity sequences
   for (a,b) in {(2,3),(2,5),(3,4),(3,5),(2,7),(3,7),(4,5),(5,7)}
   and check M=a+b-1, N=ab each time; verify C'^2=nd at three pairs.
6. The (4,2) noncoprime worked example gamma(t)=(t^4, t^2+t): verify
   its place at infinity is a (2,5)-cusp, the multiplicity sequence
   2,2,1,1, M_infty=6, and the s count; then construct ONE more
   noncoprime example (d,n)=(6,2) or (6,3), compute M_infty, and
   check (M-INF) M_infty <= 3d-3 there (data point for the residual).
7. Countermodel hunt for Theorem C's transport: try to build a small
   explicit family where a tangential curve's complement group is
   strictly larger than the nodal neighbour's (the report only needs
   the REPRESENTATION to transport — check on the smallest case
   d=4,n=3: write the ZvK presentation for a concrete tangential
   member if one exists in P_{4,3} with an A_3 point, and check
   directly whether an S_4 transposition surjection with disjoint
   local pairs exists).

Verdict per target: HOLDS / BROKEN (explicit) / UNTESTABLE-AT-DESK.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/pi1-s4-verification-r2-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write; never attempt the
whole report in one response). Only after the final section is on
disk, append the standalone `<!-- BODY-END -->` line. If the budget
runs short, finish the current section, type every remaining section
OPEN in one short paragraph each, then seal. An unsealed report with
real content is recoverable; a sealed skeleton is not. Keep
it under roughly 5,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
