# Hostile review assignment: corrected missing-multiplicity identity (2.3')

Act as an independent hostile mathematical referee. Review exactly the
Opus packet named below. It claims four things: the original identity
(2.3) is REFUTED by the hand control `F(x,y)=(x, x^2 y^4)`; a corrected
identity (2.3') `N = f(z) + sum s_l mu_l` is proved unconditionally for
dominant etale morphisms; on the charged rank-four rows the promoted
inertia constraint forces `s_l=1` recovering (2.3); and — decisive —
`m=1` for the reducible branch follows WITHOUT (2.3), from the promoted
inputs plus Orevkov's formula: each component gets its own dicritical
with bracket `>= mu >= 2`, so `2m <= N-1 = 3`. If that chain survives
your attack, every reducible rank-four row is dead. Attack accordingly.
Do not promote, edit any charged file, edit canonical ledgers, or
inspect `jc2-lean`.

charged_input=xmodel/block-descent-a1-rank4-missing-multiplicity-identity-opus5-r2-20260831.md
charged_input=xmodel/block-descent-a1-rank4-dicritical-typing-d1-d4-grok46-20260831.md
charged_input=xmodel/block-descent-a1-rank4-reducible-component-tree-ledger-hostile-review-sol56-20260831.md

Your charged inputs are frozen read-only copies in `{{LANE_INPUTS}}`.
Reproduce these SHA-256 hashes first and stop on mismatch:

```text
634940bb13bb0ad28a7bfa51f76abd987acc2b6382e3d5688262fcdb747ab23a  {{LANE_INPUTS}}/block-descent-a1-rank4-missing-multiplicity-identity-opus5-r2-20260831.md
eeb4670511f35b7c52f03fa03d334eadff9eb3b7f3b6e18011beb7de4e73c54b  {{LANE_INPUTS}}/block-descent-a1-rank4-dicritical-typing-d1-d4-grok46-20260831.md
ed0d288bec800bc1cfb59506a60ac76243aa47378692330f54f9d0860d754fb9  {{LANE_INPUTS}}/block-descent-a1-rank4-reducible-component-tree-ledger-hostile-review-sol56-20260831.md
```

The second input (the dicritical typing packet, itself PROVISIONAL and
under separate review) supplies the sourced statements of Orevkov's
identity and Chau's lemmas; use it as the declared source interface, and
flag any place where the Opus packet's use of Orevkov/Chau exceeds what
the typing packet actually sourced.

Independently recompute, hunting for errors:

1. the compactification and boundary typing (packet §2): that every
   boundary curve is dicritical, polar/constant, or finite-contracted,
   and the proof that only dicriticals meet generic fibres of a branch
   component — hunt for a boundary place evading the trichotomy;
2. the counterexample (V2): the control's Jacobian is `4 x^2 y^3`,
   which vanishes on `{xy=0}` — determine exactly on what domain `S`
   the packet runs this control, whether the control is honestly within
   (V1)'s etale hypotheses on that domain, and whether it then refutes
   (2.3) as the ledger stated it (for the Keller map itself at generic
   `z` of a branch component) or only a broader reading; this is the
   single most important check;
3. the local-multiplicity section (§4): `mu_l` as generic local degree
   along a dicritical equals the Orevkov base term — compare with the
   typing packet's (D3) derivation, which located positivity elsewhere
   than `deg f_phi > 0`;
4. the corrected identity proof (§5) including the cycle-type
   Proposition 5.3 and both corollaries; check the monodromy argument
   forcing `(mu,s)=(2,1)` and `(3,1)` on the charged rows;
5. the de-conditionalized Theorem 10.1: distinctness of the `l_i`,
   `bracket_{l_i} >= mu_{l_i}`, nonnegativity of every other bracket,
   and the sum bound — and whether the promoted inputs it cites are
   genuinely promoted at the scope used (cross-check against the third
   input's §9.1 hierarchy);
6. genericity (§6): the open-dense locus claims and what happens at
   special points of `B_i`;
7. the hand controls (§7): recompute each;
8. scope (§9): etale-ness versus Keller, `N` arbitrary, reducedness of
   `A_F` not needed — flag overreach.

State the weakest exact hypotheses, any correction and blast radius, and
one best next falsification test. Give a per-claim verdict from
`CONFIRMED`, `REFUTED`, `GAP`, with the attack shown.

Computation rules: short exact desk arithmetic only. Never run Singular,
msolve, any CAS, or any computation of uncertain duration or memory on
this machine.

Write one report and no other file:

```text
xmodel/block-descent-a1-rank4-mm-identity-hostile-review-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your first
action and append each completed section as you finish it. Keep it under
roughly 6,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration: this review asserts no new
exit price.
