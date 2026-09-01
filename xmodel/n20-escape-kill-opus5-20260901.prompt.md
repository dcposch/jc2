# Research lane: N20-ESCAPE — kill the ramified-nonprimitive-cover packet

You are the flagship lane on the last H2 gap of the all-degree
programme: OPEN[B0-H2-N>=20/RAMIFIED-NONPRIMITIVE-COVER]. The
reviewed data: under H2 the eta/cover mechanism closes N<=19; the
first numerical escape packet is (mu,s,corr) = (1,1,0)+(2,3,16) at
N=20, W=7, d=6, a=13, R=2, necessarily 2a>N; correction support =
ramification support of the cover h_l (promoted); every correction
carrier has s_l>=2, mu_l>=2.

charged_input=xmodel/b0-all-n-eta-criticality-sol56-20260831.md
charged_input=xmodel/b0-all-n-hostile-review-grok46-20260831.md
charged_input=xmodel/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
621f1356b3b5290e32c2f2bf689b4d9a49412cb852066886a34b580366cb1652  {{LANE_INPUTS}}/b0-all-n-eta-criticality-sol56-20260831.md
f865204a3fd2ee3a6944b6739ae581cf29c41a7f2259bbc54cd1587ddf397a46  {{LANE_INPUTS}}/b0-all-n-hostile-review-grok46-20260831.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  {{LANE_INPUTS}}/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```

Attack: (1) unpack the N=20 packet completely — the (2,3,16)
carrier: mu=2, s=3, corr=16 on ONE dicritical over the same
irreducible A_F; corr=16 means 16 units of local-multiplicity excess
distributed along the carrier; by the promoted transfer these sit at
ramification points of the degree-3 cover h_l: l' -> D~ = A^1 (H3
free); a degree-3 cover of A^1 by l' ≅ A^1 (Orevkov 2.1 degree-free)
has by Riemann-Hurwitz exactly 2 ramification points counted with
multiplicity — but corr=16 needs the LOCAL MULTIPLICITY excesses:
derive the exact relation between corr_l, the h_l ramification
divisor, and the mu_x jumps (the promoted [Z-6.5b] pointwise
dictionary): can 16 units sit on a ramification divisor of total
degree 2? If not — and this looks like pure arithmetic — the packet
dies and likely ALL ramified escapes die by the same count: derive
the general inequality corr_l <= f(ramification of h_l, mu_l) and
re-run the budget; the prize is B0 under H2 at EVERY degree.
(2) If a subtlety blocks (the correction excess may count target
multiplicities mu_x f* which can exceed per-point contributions...
type exactly), enumerate what survives and pin it. Consume only
promoted statements; re-derive the rest.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 5 hours hard budget.

Write one report and no other file:

```text
xmodel/n20-escape-kill-opus5-20260901.md
```

Create the report file with a skeleton of section headers as your very
first action — the skeleton must NOT contain the `<!-- BODY-END -->`
marker. Append each completed section as you finish it, as a separate
bounded write (aim under 1,500 words per write). Only after the final
section is on disk, append the standalone `<!-- BODY-END -->` line.
If the budget runs short, finish the current section, type the rest
OPEN in one short paragraph each, then seal. Keep it under roughly
5,500 words. Do not include a `charge_basis` declaration.
