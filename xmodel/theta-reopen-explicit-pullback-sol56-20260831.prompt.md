# Construction lane: THETA reopen data — the explicit one-cusp pullback

You are a bounded construction lane executing the slimmed THETA reopen
gate. The Stage-0 OPEN is confirmed in both directions: nothing in the
promoted packets pins the charged pullback. Your job is to SUPPLY it —
or prove it cannot be supplied within the promoted constraints.

charged_input=xmodel/round1033-theta-staged-sol56-20260831.md
charged_input=xmodel/round1033-theta-staged-hostile-review-grok46-20260831.md
charged_input=xmodel/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
charged_input=xmodel/block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md
charged_input=xmodel/block-descent-a1-mprime-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
1cf8f9d75e17efd2fc5d43861d721a1eb3b3c0d468e93c75d571f875576012fb  {{LANE_INPUTS}}/round1033-theta-staged-sol56-20260831.md
cad4a29d4ffd7c405b6530afaac48b2ec1f71617810987a43d038f085c50023b  {{LANE_INPUTS}}/round1033-theta-staged-hostile-review-grok46-20260831.md
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5  {{LANE_INPUTS}}/block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
7a60ff245fc351a99a23815908909327dc6a9644f849a4d3b289079c98488474  {{LANE_INPUTS}}/block-descent-a1-one-cusp-fibre-connectedness-sol56-20260831.md
69970f4d2c4a2c5760e116400b1b27426edc41fdf6a8d15936df14cc567855c9  {{LANE_INPUTS}}/block-descent-a1-mprime-coordinator-integration-fable5-20260831.md
```

The slimmed gate (review §7): only items (1)-(2) are the numerical
gate — (1) explicit checked images `f = P_f(A,Z) + U·Q_f(A,Z)`,
`g = P_g(A,Z) + U·Q_g(A,Z)` in `R=C[A,U,Z]/(U^2-A-A^2Z)` for a map
`pi=(f,g): Spec R -> A^2` satisfying the charged block properties the
promoted packets assume (locally finite, the completion identities
(1.3)/(1.12)-(1.14) of the structure packet, hyperbolic generic
fibres, the promoted partition-table interface), or an equivalent
complete divisorial pole ledger; and (2) an equation and normalized
parametrization of the target curve `B` (one place at infinity,
normalization `A^1`). Uniqueness-of-lift and minimality conditions are
NOT required for the number `Theta_h`.

Protocol, fail closed:

1. Determine the constraint system the promoted packets impose on
   `(P_f,Q_f,P_g,Q_g)` — degrees along the ruling `A`, the wild
   valuation data, the completion identities — and derive the LOWEST-
   complexity admissible shape. State every free parameter.
2. Either construct one explicit admissible `(f,g)` with all charged
   properties VERIFIED by hand (each identity checked term-by-term in
   the displayed normal form — no "similarly"), or prove a typed
   obstruction: the constraint system is inconsistent at every finite
   complexity you can bound, with the first inconsistency exhibited.
   An inconsistency finding is major: it would kill the one-cusp horn
   configuration outright — type its scope precisely (which promoted
   interface it contradicts).
3. If a construction lands: compute `d_h = -ord_infty(h∘beta_B)` and
   `r_h` (poles of the mate on the normalized generic fibre) two
   independent ways each, then `Theta_h = d_h - r_h - 2`. Negative or
   odd kills the charged configuration; nonnegative even selects one
   partition row (never attainment). This is the payoff of the round's
   top-ranked composite — but do NOT force it: a typed OPEN with the
   constraint system fully written is a good outcome.

Guardrails (from the confirmed report): the chart `iota: A|->x^2,
U|->x+x^3y, Z|->2y+x^2y^2` is source-side and may NOT be reused as
the pullback; the target place `q_infty`, source places on the generic
fibre, and the interior divisor `Phi=V(A,U)` stay distinct; no pole
identity before its valuation is typed.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation
of uncertain duration on this machine. Do not edit canonical ledgers,
any charged file, or inspect `jc2-lean`. Six hours hard budget.

Write one report and no other file:

```text
xmodel/theta-reopen-explicit-pullback-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your
very first action and append each completed section as you finish it.
Keep it under roughly 6,000 words. End its body with a single
standalone `<!-- BODY-END -->` line and write absolutely nothing
after that line. Include a `charge_basis` declaration only if you
assert a genuinely new exit price with a direct mathematical-source
citation; otherwise omit it entirely.
