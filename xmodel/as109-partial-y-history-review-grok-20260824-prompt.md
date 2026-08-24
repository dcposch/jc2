# Hostile different-model review — partial-`y` history stop and `(6,9)` frontier

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
artifacts on top. Do not trust producer PASS strings, campaign summaries,
or secondary-source paraphrases.

Read in full:

- `xmodel/as109-partial-y-history-stop-20260824.md`
- every file under `cases/as109_partial_y_history_stop_20260824/`
- the primary sources named and hashed in producer section 2, retrieving or
  independently checking the official text where needed
- `xmodel/as109-support-gate-20260824.md` and its landed hostile review
  `xmodel/as109-support-review-grok-20260824.md`, but only for the conditional
  AS109 residue-ball noninjectivity input
- the landed bounded-degree synthesis and review
  `xmodel/as109-bounded-y6-chain-audit-20260824.md` and
  `xmodel/as109-bounded-y6-chain-review-grok-20260824.md`, to determine exactly
  what this history correction supersedes without importing their novelty

Frozen hashes:

- producer report:
  `6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe`
- coverage replay:
  `0e07b8fcc51a7b3cf2b84985aff0bf0fce6f8eeb06e76b6e60d2b1ac6ccc6f9f`
- `(6,9)` / AS109 replay:
  `980a44cfd5f0ab8fa6f3ed7cd91c15704bcd49bc59f2bc97a4fadcaa5c9ea8fd`
- freeze manifest:
  `f3d0dc4167cb1df4537f6ff2aeee37252c0c4be6cb3431e30920b85952158d34`

Independently rerun both registered replays and attack exactly:

1. **Top-row UFD and source shear.** Re-derive
   `n*a_m'*b_n-m*a_m*b_n'=0`, the factorization
   `a_m=alpha*h^a`, `b_n=beta*h^b` for
   `m=d*a,n=d*b`, and the exact transformed total degrees
   `a(H+dL),b(H+dL)`. Check arbitrary characteristic-zero constants,
   constant `h`, scalar extension, the orientation of the source
   automorphism, the domination bound on `L`, uniqueness of the top term,
   and absence of cancellation. Verify automorphy is equivalent before and
   after the shear.
2. **Primary-source theorem chain.** Read the actual theorem statements and
   corrections. Check that Nagata really repairs the Appelgate--Onishi
   prime-total-gcd result in the scope consumed here, and that the
   peer-reviewed Guccione--Guccione--Valqui result independently excludes
   total-degree gcd `2p` for every needed prime. Distinguish these from
   Magnus's coprime result and from the gap in Zoladek. Check field hypotheses
   and descent from `C` to an arbitrary characteristic-zero coefficient
   field. A citation or theorem-scope error is a mathematical GAP even if the
   finite scripts pass.
3. **Dirichlet arithmetic and coverage.** Check the progression after
   dividing by `g=gcd(H,d)`, the ability to choose arbitrarily large `L`, and
   the cases `g=1,2`. Independently enumerate all 81 ordered pairs with
   maximum actual partial `y`-degree at most eight, including zeros, equal
   degrees, divisible-degree target shears, constant leading coefficients,
   and termination of lexicographic descent. Independently audit the complete
   maximum-nine row. Verify that the sole fundamental residual is `(6,9)`
   with `3|H`, while `(9,9)` is derivative rather than independently closed.
4. **Novelty/history conclusion.** Decide whether the prior `(4,6)`, `(5,6)`,
   and bounded-`y<=6` certificates remain correct but cease to be new
   coverage. Search specifically for an older theorem even stronger than the
   producer's formulation. Separate priority from mathematical validity.
5. **`(6,9)` common-cubic stop.** Re-expand
   `K=z^3+u*t^2*z+v*t^3`, `F=K^2`, `G=K^3`; recompute the binary Jacobian,
   depressed rows, boundary ideal dimension, and Kummer weights. Check that
   this proves only failure of the prior finite-map mechanism, not existence
   of a Keller pair or impossibility of some other `(6,9)` method. Challenge
   whether the claimed two-dimensional family and descent survive all stated
   normalizations.
6. **AS109 integral specialization.** Verify that the seed congruence forces
   divisibility of the relevant high-`y` coefficients; that primitive-core
   normalization justifies `v_109(alpha),v_109(beta)>=1`; and that the exact
   `y^13` row is
   `8*a'*d+9*c'*b-6*a*d'-5*c*b'=0`. Check its valuation bounds and the
   explicit zero-Jacobian control without mistaking that control for the
   seed or a Keller pair.
7. **Conditional maximum-nine implication.** Recheck the integral constant
   target `GL_2` step for raw `(9,9)`, especially the direction chosen by
   coefficient contents and preservation of the integral seed/high-row
   divisibility. With the separately reviewed Hensel noninjectivity only,
   determine whether every exact AS109 lift of maximum actual `y`-degree
   exactly nine must reduce to `(6,9)` with `3|H`, and whether maximum at most
   eight is excluded. Quarantine existence, arbitrary support, higher degree,
   and JC2.
8. **Artifact and scope audit.** Verify every frozen hash, write at least one
   independently implemented pair enumeration or exact algebra check, and
   identify the smallest statement that would fail under any discovered
   issue. Do not launch AWS or edit producer/canonical/ladder files.

Write exactly one report file:

`xmodel/as109-partial-y-history-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
exact primary-source citations/theorem statements, hashes, independent
checks, scope exclusions, and precise promotion advice.
