# Fable 5 cross-pollination and adversarial synthesis — round `20260827T0935Z`

You are Fable 5, an equal-standing JC2 co-researcher.  This is the
cross-pollination phase after four sealed, blind, whole-portfolio submissions.
Work independently from the coordinator's eventual synthesis.  Compare all
four reports, attack their mathematics and scope, identify connections none
of the individual reports made, and return a decision-ready merged strategy.
Audit your own blind submission at least as strictly as the others.

Read every file below in full and verify its SHA-256 before relying on it:

```text
e871e3d71a8777ca50f7c796bf7547023a8c2ca8e2930c6a0981ddcebd6ae3db  xmodel/ideation-20260827T0935Z-packet.md
98a494a561f39cfef770eec11c07eca3e17e4e9fac61a1a3d143f614d991b90c  xmodel/ideation-20260827T0935Z-sol.md
098b81d19cba6f278e93a809e60a3a4892eea7979758ffe6b0bb2997163b98c0  xmodel/ideation-20260827T0935Z-fable5.md
265cfa731dd0e1614966c5eec3367d0dc38a959a2b43a848256c64c4be0b6217  xmodel/ideation-20260827T0935Z-grok.md
3295402670b65b0a61d56aa9d4f117084b282d649eb72a2afd7df6fe3195782e  xmodel/ideation-20260827T0935Z-opus5.md
7345d4a8dda7afd9f45dd6b938a5ec0e15ff642e4809da5434ef35eb505f446d  xmodel/max12-812-order2-p0-total-rees-j2-a1-w30-n6-rho0-dual-nonmembership-v43-sol-20260827.md
64e49a369470fb452b53334d92298a1bdb50d9c897afd197ced8b0312e69afcb  xmodel/max12-812-order2-p0-total-rees-j2-a1-w30-n6-rho0-dual-nonmembership-v43-hostile-review-opus5-20260827.md
1cfa10b45d83ba4ecd98861c1f82e9bd41056d1cef7eaa43ad2802aa73aada5d  xmodel/max12-812-order2-gate-t-uniform-contact-shift-naturality-interface-sol-20260827.md
b66f8c0cf342e497e9117306de3d4aaa5d8b537c5929f99d2b32765ed855f164  xmodel/max12-812-order2-gate-t-uniform-contact-shift-naturality-interface-hostile-review-fable5-20260827.md
2354703a559a5da2b4f2032560a5740b2cda1f3160f5c6598dcdbe1c4c1432be  xmodel/max12-812-order2-gate-t-strict-uac-three-row-syzygy-interface-sol-20260827.md
234cc4021e03e8c40b694e7757bfb2d1bad51e8eafe66c417b231e59550a1af8  cases/max12_812_order2_gate_t_drho_a2d3_composition_v45_20260827/RESULT.md
b669f942ff48360dba0e915057ff49c28ada71c4833fb414c66106b770da7ca6  cases/max12_812_order2_gate_t_drho_a2d3_composition_v45_20260827/PASS_EVIDENCE.sha256
ecbc2c200a9c1b80da6e32ded0c10557e647c78a86294b526f4ce8c838e96daf  cases/max12_812_order2_u2_62_k00_colon_local_v14_20260827/CUSTODY_GAP.md
65ee7849741bd64adbb842139f12d538e63337aa9cd3c4d6c8c89c49782bbbfd  cases/max12_812_order2_u2_62_k00_colon_local_v14r1_20260827/PREREGISTRATION.md
```

The sources after the four blind reports are post-snapshot evidence.  Do not
rewrite the blind record.  V45 is exact producer evidence but remains under
Opus review.  K00 V14 had a serialization defect; V14R1 was preregistered to
repair it.  The coordinator reports that exact-Q and p=65521 V14R1 endpoints
now pass, including all 36 lift entries and a fresh-process replay of
`-h*r7 + sum u_i*r_i = 0` with `h=63*d4+20`, but the portable report and
different-model review were not frozen at prompt time.  Treat that statement
as provisional delta context, not promotable evidence.

Required adversarial work:

1. Prove or refute the proposed two-fibre criterion carefully.  Let
   `S=Q[rho,X]`, give every `X` variable positive weight and `rho` weight zero,
   let `J` be homogeneous, `K=J:a1^infinity`, and
   `T={u(rho):u(0) != 0}`.  Decide whether
   `K+(rho)=S`, `a1 in sqrt(J T^-1 S)`, radical membership in both the generic
   fibre `Q(rho)[X]` and special fibre `rho=0`, and unit ideals after full
   dehomogenization `a1=1` are genuinely equivalent.  State every hypothesis,
   contraction/localization step, and failure mode.  Test nonhomogeneous and
   non-flat counterexamples.  Explain exactly what the already-proved special
   fibre unit contributes.
2. Audit the generic-eliminant computational predicate.  Distinguish a
   selected-row subideal from the full 59-row ideal.  Decide what conclusions
   follow from: unit ideal; a nonzero elimination polynomial in `Q[rho]`;
   constant elimination polynomial; zero elimination ideal; and modular
   specializations `rho=c`.  In particular check Opus's claim that the current
   selected total-rho code may wrongly require a nonzero constant rather than
   any nonzero eliminant once the special fibre is known empty.
3. Audit Sol's constructive radical-certificate tree.  Formalize the proposed
   combination lemmas for `fg in I`, `x^m in I+(f)`, `x^n in I+(g)`, and for
   `x f in I`.  Determine whether the known cascade branches can be combined
   into an explicit unsplit `a1^N in J0`; give a correct exponent recurrence
   and an executable certificate DAG if possible.  Separate ideal identities
   from radical/pointwise reasoning.
4. Reconcile the exact N=6 dual, the seeded N=7 experiment, and the generic
   fibre decision.  Is the exponent ladder still decision-relevant, merely a
   certificate-compression route, or now dominated?  Respect the Opus review's
   custody repairs: do not treat the target-coefficient mutation as an
   independent check.
5. Integrate K00 V8/V9/D8 and provisional V14R1.  Explain how global
   nonmembership coexists with local membership; decide whether the full
   syzygy module yields a representation-invariant first deformation
   obstruction for the mixed `Lambda19`/load/target/Jdet problem.  Give the
   cheapest exact discriminator and a stop rule.  Do not infer closure or JC2
   from the unloaded local identity.
6. Integrate the uniform contact-shift naturality theorem, direct three-row
   syzygy, and exact V45.  Check whether they really remove serial G22/G24+
   exporters from the critical path and identify the finite schema/verifier
   still required.  Keep strict unique-AC contact exclusions separate from
   global coverage.
7. Scan the whole 46-avenue inventory again.  Identify any genuinely new
   connection or avenue suggested by the combined evidence, including your
   AS109 face-isolation, b-function/D-module, and primitive-group proposals.
   Run a history checksum against the packet/canonical inventory before
   calling anything new.  No web search: source-dependent ideas remain
   explicitly conditional.

Deliver:

- a claim matrix for every material cross-report claim, marked `sound`,
  `sound with scope correction`, `unsupported`, or `wrong`;
- the strongest unique contribution of Sol, Fable, Grok, and Opus after
  deduplication, plus any independent convergence that raises confidence;
- at most four merged executable idea cards, each with mathematical target,
  dependencies, cheapest discriminator, both-outcome interpretation, AWS or
  desk resource class, stop rule, and scope firewall;
- explicit `launch now`, `continue in background`, `hold`, `merge`, and
  `stop` decisions, optimized for wall-clock speed and nonblocking review;
- a short evaluation of whether Opus adds significant correctness-adjusted
  unique capability beyond Fable in this round.

Do not claim a proof/counterexample of JC2.  Do not browse or use AWS.  Do not
run heavy CAS locally.  Do not read, enter, build, inspect status of, edit,
stage, clean, or otherwise touch `jc2-lean`.  Edit no campaign artifact except
the single output file below.  Write the complete report to:

`xmodel/ideation-20260827T0935Z-fable5-crossreview.md`

End with a file-read/tool/edit disclosure.
