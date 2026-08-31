# Producer-side pre-review: wild one-cusp valuation/completion structure

Act as an independent hostile referee for a producer-side pre-review
pass. The packet named below was produced by a different session of your
own model family; your report is an UNCHARGED advisory filter — it can
never satisfy the different-model promotion rule, and a separate charged
gate runs independently. Work blind: do not look for, read, or reference
any other review of this packet. Attack it exactly as a hostile referee
would. Do not promote, edit any
charged file, edit canonical ledgers, or inspect `jc2-lean`.

charged_input=xmodel/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
charged_input=xmodel/block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md
charged_input=xmodel/block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md
charged_input=xmodel/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md

Your charged inputs are frozen read-only copies in `{{LANE_INPUTS}}`. Read
them there. Reproduce these SHA-256 hashes first and stop on mismatch:

```text
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5  {{LANE_INPUTS}}/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
cd27b7f6687103fae0fc4e5fe19772e0f8e62939d73a655ebf04e57905ddba05  {{LANE_INPUTS}}/block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md
2531a89d6c939aee6e0d402408f15d28a228927dc15d82c10d430e67164cb190  {{LANE_INPUTS}}/block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md
0a6272060a03c0071ad8b4c71aef00f3c724284d9590dcab61a2e75169a8713f  {{LANE_INPUTS}}/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md
```

Status update the packet predates: the Poisson parent (second input) was
PROMOTED on 2026-08-31 after independent review, so its consumed
conclusions are no longer provisional; the packet's PROVISIONAL labels on
them may be relabeled but this does not weaken your duty to recheck each
use. Other cited files may be read from the live repository for interface
checking only.

Independently recompute, hunting for errors:

1. the completion isomorphism `R^_P = C[Z][[u]]` via the implicit-function
   solution `a(u,Z)=(sqrt(1+4Zu^2)-1)/(2Z)`, the orders
   `ord_P(U)=1, ord_P(A)=2`, and the bracket normal form (1.3);
2. the associated-graded identities (1.4)--(1.6), the unimodular identity
   (1.9) (including its claimed consequence `deg f_0, deg g_0 >= 2`), and
   the local nilpotence of the degree `-1` symbols (1.10);
3. the cusp-companion rectification (1.11): both fields formally constant
   translations at `u_c`, and the infinite-jet restatement of wildness —
   check the claim that no local invariant at `u_c` can detect it;
4. the generic-boundary computation (1.12)--(1.15): the tame `s^2` form,
   the degree `-2` normal symbols, the existence of `h in O(S)` with
   negative boundary valuation, and whether (1.15) really is an
   independent proof of non-local-finiteness from the reviewed boundary
   packet alone — this claimed redundant second proof is load-bearing, so
   attack the leading-coefficient product `prod(k-2i)` and the
   linear-independence step hard;
5. the flow divisor (2.1) with attainment, the iterate formulas
   (2.4)/(2.6), and the Riemann--Hurwitz degree accounting (2.5);
6. the necessary-tuple table of §3.1: the transversality argument
   forcing `e_p=2` at every finite deleted point, the equality
   `d_f=2*gamma_f+2+r_f`, the four-row partition table, and the exact
   sub-strata closures (3.6) — hunt for a fibre through a singular point
   of `Y` or a tangency that the genericity choice cannot avoid;
7. §3.2: that the inverse-Kummer collision contributes order-index only,
   never a place of (2.1) or an `e_p` change, and the valuation identity
   (3.10);
8. the maximum-safe conclusion list and every OPEN typing — flag any
   overreach or any place where a PROVISIONAL label hides a use of an
   unproved statement in a proved-labelled line.

State the weakest exact hypotheses, any correction and blast radius, and
one best next falsification test. Give a per-claim verdict from
`CONFIRMED`, `REFUTED`, `GAP`, with the attack shown.

Computation rules: short exact desk arithmetic and symbolic checks by hand
only. Never run Singular, msolve, any CAS, or any computation of uncertain
duration or memory on this machine.

Write one report and no other file:

```text
xmodel/block-descent-a1-one-cusp-wild-valuation-prereview-sol56-20260831.md
```

Write the report incrementally as you work — create it at the start and
append each completed section. Keep it under roughly 6,000 words. End its
body with a single standalone `<!-- BODY-END -->` line and write
absolutely nothing after that line. Do not include a `charge_basis`
declaration: this review asserts no new exit price.
