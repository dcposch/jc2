# Verification lane: N20-ESCAPE — computation arm

Second arm of the paired review; independent; computations only.
Targets: (1) re-derive the corr budget of the (2,3,16) packet: a
degree-3 cover A^1 -> A^1 has ramification divisor degree 2 (RH:
-2 = 3(-2) + deg R => deg R = 4? recompute carefully: chi(A^1)=1,
so 1 = 3*1 - deg R, deg R = 2); test the charged relation between
corr_l and the ramification data at three synthetic packets of your
own design (small s, various mu, corr) — verify the claimed general
inequality on each and find its equality cases; (2) enumerate ALL
numerically-admissible escape packets at N=20,21,24 under the
promoted budget WITHOUT the new inequality, then apply the
inequality and confirm each dies; hunt for any packet shape the
charged proof's case analysis might miss (large s, multiple
carriers, mu large); (3) the W/R bookkeeping identities at the
charged packet values (W=7, d=6, a=13, R=2); (4) the H3-free
l' ≅ A^1 step at a NON-minimal example. Verdict per target:
HOLDS / BROKEN / UNTESTABLE.
charged_input=xmodel/n20-escape-kill-opus5-20260901.md
charged_input=xmodel/b0-all-n-hostile-review-grok46-20260831.md
charged_input=xmodel/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
46c5f62fe92fd5ecbd12b1f74d83d272624253f1f06e9324c9fa1b1c21eac619  {{LANE_INPUTS}}/n20-escape-kill-opus5-20260901.md
f865204a3fd2ee3a6944b6739ae581cf29c41a7f2259bbc54cd1587ddf397a46  {{LANE_INPUTS}}/b0-all-n-hostile-review-grok46-20260831.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  {{LANE_INPUTS}}/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 3 hours hard budget.

Write one report and no other file:

```text
xmodel/n20-escape-verification-grok46-20260901.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,000 words. Do not include a `charge_basis` declaration.
