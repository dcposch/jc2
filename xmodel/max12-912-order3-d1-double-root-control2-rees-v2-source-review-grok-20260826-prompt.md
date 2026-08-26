# Text-only hostile review — exact D1 control-2 Rees v2

Act as a hostile algebraic-geometry and computer-algebra referee.  This is a
**text-only review**.  HARD RULE: do not execute Python, Singular, Sage,
msolve, Lean, Gfan, a solver, or substantive symbolic computation on the
local Mac.  Read frozen sources and already-emitted AWS text only; lightweight
hash/status commands are allowed.  State explicitly that no local substantive
computation was run.

Audit the source-distinct v2 package

```text
cases/max12_912_order3_d1_double_root_control2_rees_v2_20260826/
```

and these identities:

```text
6ca862b7e0569e58ab04e3bfd18c6230ffe24d83e9461f97dd753396dd8dee95  SOURCE_CLOSURE.sha256
bc57933f4b8d96837e9598dd340077f83099861ddca992060d55449cd6bed876  PRESOLVE_FREEZE.sha256
77c933be81b3242ccf8bf06ef96ca458584b94519a10028431a92e0a69ac2a36  aws_r6d_B/singular.stdout
ec9fe740de4d330fbeaba7a5af5db4e56b36d62f417f051f3c35f85599edd3f1  xmodel/max12-912-order3-d1-double-root-newton-correction-review-grok-v2-20260825.md
```

Read `PREREGISTRATION.md`, `compile_control2_rees_v2.py`,
`remote_worker_v2.sh`, `AWS_REGISTRATION.md`, `COMPILE_CUSTODY.md`, the
complete emitted r6d input/stdout/stderr/time/rc/result hashes, and the v1
`SOFTWARE_CONTROL.md`.  Encoding A may still be live; do not infer its result.

Charge each point explicitly.

1. Re-expand by hand all nine specialized coefficient images for
   `f=(z^3-3z+2)^3+(z^3-3z+2)(q1*z+q0)+(r2*z^2+r1*z+r0)`.  Verify
   `a=1,h=q2=k=nu=0,mu=2/3`, the row-3 and row-8 targets, and the toric
   relation.
2. Verify the support mask, weight vector
   `(4,1,1,22,22,30,30,30)`, and residue
   `(1,1,1,1,-1,1,1,-2)`.  Explain why `-t^38/2` is a later coefficient of
   `r0`, not a missing variable.
3. Audit the sparse substitution, target subtraction, minimum-weight
   generator check, compact factored encoding A, independently expanded
   encoding B, normalized dual-host source identities, and fixed-load
   semantics.
4. Prove or reject that substituting `X -> s^w X`, then either saturating by
   `s` or eliminating from `u*s-1`, computes the exact contraction from
   `s!=0`; adding `s=0` computes the full initial degeneration, including all
   S-polynomial consequences rather than only the submitted generator
   initials.
5. Audit torus localization by
   `Lambda*tau*rho*q1*q0*r2*r1*r0`: A uses principal saturation, B uses the
   independent inverse `v`.  Check the B `(lp(3),dp(8))` blocks and both
   eliminations.  Decide whether `GHT[1]=1` rigorously means the whole stated
   weight/support stratum is absent.
6. Explain why it is consistent for the displayed residue to annihilate the
   initial form of every submitted generator while the **full** torus initial
   ideal is unit: a polynomial consequence/S-polynomial may have a monomial
   initial form.  Confirm that the code does not equate prevariety membership
   with tropical membership.
7. Audit exact result semantics: `RESIDUE_SURVIVES=0` is defined by
   `Htor+M_residue=(1)`; `TORUS_SPECIAL_FIBRE_IS_UNIT=1` is stronger.  State
   what a dual clean unit can exclude and why it says nothing about moving
   axis, `q2!=0`, other weights/residues/loads, the full fan, D1, or JC2.
8. Audit v2 custody: timing is in `singular.time`, CAS stderr is empty, source
   hashes are checked before compile/solve, and rc/PASS/FAIL gates are
   fail-closed.  Confirm v1 is correctly quarantined and cannot support math.
9. Search specifically for minimum/maximum weight reversal, a missed target
   coefficient, inadequate saturation, hidden load variation, a malformed
   Singular ideal/elimination, or overstrong curve-selection language.

Write exactly one report and make no other repository edits:

`xmodel/max12-912-order3-d1-double-root-control2-rees-v2-source-review-grok-20260826.md`

End with exactly one token on its own line:
`REES_V2_CONFIRMED`, `REES_V2_REPAIRED`, or `REES_V2_REJECTED`.

