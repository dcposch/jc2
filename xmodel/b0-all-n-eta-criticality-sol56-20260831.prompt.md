# Research lane: B0-ALL-N — the eta-criticality mechanism at every degree

You are a bounded primary research lane. The N=5 companion lane killed
the trivial-dicritical profile under H2 by an eta-criticality clash:
under H2 every dicritical parametrization factors through the ONE
normalization eta of A_F; a correction point forces d eta = 0
somewhere; a birational (s=1) trivial dicritical forces eta immersive
everywhere. Your task: prove the sharpest general theorem this
mechanism supports, targeting

> **(B0-H2-ALL-N)** For every noninvertible Keller map with `A_F`
> irreducible, there is NO dicritical with affine image and `mu_l=1`.

charged_input=xmodel/corr-budget-n5-sol56-20260831.md
charged_input=xmodel/b0-trivial-dicritical-proof-opus5-20260831.md
charged_input=xmodel/block-descent-a1-b0-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
67a9482eecd3fcb5f06bcf2967d4b73f5761429b5be597f2809b8e0767b1b02c  {{LANE_INPUTS}}/corr-budget-n5-sol56-20260831.md
b37ec3bfd41eb22c14e29b06284100a61c50fd849150fefe2eab89e1d1a78c55  {{LANE_INPUTS}}/b0-trivial-dicritical-proof-opus5-20260831.md
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963  {{LANE_INPUTS}}/block-descent-a1-b0-coordinator-integration-fable5-20260831.md
```

Skeleton to formalize, fail closed at each step:

1. Under H2 all dicriticals map onto the single component D; each
   `phi_l: l' -> D` factors as `eta ∘ h_l` with `h_l: l' -> D~` of
   degree `s_l` (promoted normalization/covering data — state the
   exact promoted licence, including at points over Sing D).
2. If some dicritical `l_0` has `mu_0 = 1`: by promoted [Z-6.5b],
   `corr_0 = 0` and `phi_0` is everywhere immersive. Derive what that
   forces on `h_0` and `eta`: at any point where `d h_0 != 0`, eta is
   immersive at the image; where `d h_0 = 0`, the composite is
   critical — contradiction with immersivity of `phi_0`. So `h_0` is
   unramified everywhere on `l_0'`. Then eta is immersive at every
   point of `h_0(l_0')` — determine when `h_0` must be surjective
   onto `D~` (properness/finiteness of `l_0' -> D`), giving eta
   immersive EVERYWHERE.
3. By promoted Cor 3.7 (H2 strictness), `sum corr_l >= 1`: some
   correction point exists on some dicritical `l_1`. By [O-5.2]'s
   contrapositive at that point, the image has a non-immersive
   parametrization point: derive `d eta = 0` somewhere — here the
   `s_1 >= 2` case needs care (the critical point might live in
   `h_1`, not eta; determine exactly what [O-5.2]/[Z-6.5b] force on
   the IMAGE germ, which is eta's germ, independent of h_1 — a
   singular point of the immersed image curve is a critical point of
   eta OR a multiple point; type which, and whether the multiple-
   point case escapes).
4. Assemble the contradiction, stating the theorem at its true scope:
   all N under H2, or the exact obstruction class that escapes (e.g.
   corrections whose image singularity is multibranch — reconcile
   with promoted Lemma 3.3 smooth-branches). Also state the
   unramified-cover step: `h_0` unramified of degree `s_0` onto
   `D~ = ?` — under H3, `D~ = A^1` has no nontrivial connected
   unramified covers, forcing `s_0 = 1`; WITHOUT H3, type what
   survives.
5. Consequences if the theorem lands: b=0 at every N under H2(+H3?);
   the strong bound `2m<=N-1` under which hypotheses; and the exact
   remaining reducible-A_F gap at each N (the N=4 reducible residual
   rides PI1-S4; state the N>=5 analogue precisely).

Consume only promoted statements (cite both integrations) and hashed
primary sources; re-derive everything else. A typed OPEN at a named
step is a good outcome.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 6 hours hard budget.

Write one report and no other file:

```text
xmodel/b0-all-n-eta-criticality-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 5,500 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
