# D125 hybrid affine constructor: preparation only

2026-09-07. **IMPLEMENTED / TINY-CHECKED, NOT EXECUTED ON THE ACTUAL SOURCE.** This is the one authorized provisional child of the hybrid desk result. Its independent mathematical gate was live and was not read. No production coefficient maps, source rows, receiver pairs, full polynomiality expansion, CAS, AWS/SSH or deployment were run. There is no point, ideal decision or measured production speedup.

## New instrument and exact client

Owned files are in `box/d125-hybrid-affine-code-prep-20260907/`:

- `construct.py` (250 lines): normalized affine Hermite maps and complete literal rows; one-process construction/replay entry, no subprocess or solver API.
- `replay.py` (145 lines): separate substitution of the frozen original literal stream into the exact normalization cover. It does not call the normalized Jacobian or polynomiality row generators.
- `baseline.py`: byte-identical accepted metadata source, SHA `ec2fa2d1e23bc16bc07c9208f648e3b17561cbfddaaf04fed28d7ffc9a428d53`. Its production-sized metadata routines were not called locally.
- `test_tiny.py`, complete normal/optimized transcript and tool receipt, pins, and `REPLAY-CONTRACT.md`.

The sole client is unequal/rational, odd A/B, lambda2=0, normalized lambda3=1, whole beta15 shear slice. Its81 generators are20 retained A coefficient slots,59 retained B slots,k,z, in that order, over Q with displayed dp order. k is not specialized: **zk−1 is mandatory**. The moving coefficients are A_(2,1)=k, B_(8,5)=5k/3, B_(1,0)=5k²/9 and the target residual is J(A,B)+5k³*g²/9. Every other fixed coefficient, including zeros and the two target constants, is preserved. Counts are generator counts, never dimensions.

Both standalone polynomiality graphs are constructed in descending odd total degree:13 A and34 B pivots. B15 uses columns1,2,3 with the determinant−1 matrix from the desk lemma. The constructor uses none of the92 nonlinear B-Jacobian graph eliminations. All maps are checked against the A22/B62 affine coefficient spaces; denominator bounds are1 and9. Every Jacobian row must satisfy the1,362-monomial, degree≤3, denominator-dividing9 bound. All105 polynomiality rows must become exact identities.

Serialization retains each original coefficient entry and all803 original indexed labels, including every660-row Jacobian-envelope slot, all105 negative-row positions, fixed assignments and guards. The804th row is UNIT/kz. Moving inverse-guard copies are explicitly (kz)^r−1, r=1,2,3, with the cofactor sum_(j=0)^(r−1)(kz)^j. Their degrees are2/4/6; the complete literal list is not falsely labelled cubic. No original zero label or residual is silently removed. Output is canonical rational JSONL with complete prefix digest/footer, row/term/zero counts, coefficient-map term count, unused residual coordinates, time/RSS and arithmetic statistics. Actual counts beyond the registered expectations are unmeasured.

## The replay arrow, including fixed faces

The original source SHA remains `b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac`, on retained EBS only. The replay first checks that hash and every269 variable name/index and coefficient metadata entry. It does **not** identify the normalized coefficient maps with the old raw variables.

Instead work in

    Q[a1..a20,b1..b59,k,z,ell]/(kz−1,ell^6*k−1)
       = Q[a1..a20,b1..b59,ell,ell^-1].

Replay's separate sparse Laurent arithmetic substitutes k=ell^-6,z=ell^6. For a member of degree D and coefficient total degree d, the raw old coefficient is ell^((D−d)/2) times its normalized map. Even-degree coefficients are zero. The old lambda variables map to0 andell. This exactly reduces both cover relations and retains the whole unit parameter, rather than sampling or assuming same-field inverse normalization.

Each original row is compared to ell^q times the corresponding normalized row: q=(38−I−J)/2 for even Jacobian rows and q=(D+e−5t)/2 for surviving negative rows. Wrong-parity cases require both sides zero. In particular, q=18 at the target sends5k³/9 to5/9. Source fixed-assignment rows themselves are zero, so separate coefficient checks enforce their actual pullbacks: k*ell^6=1, (5k/3)*ell^6=5/3 and (5k²/9)*ell^12=5/9. Guard polynomials and explicit cofactors are also checked, not merely their zero cover evaluations. The extra inverse row cannot be omitted.

Strict replay requires every803 original row label/index, exactly one extra guard, canonical rational wires, no field-part splitting, correct normalized target/header, fixed/retained coefficient maps, graph inverse orientation, complete count/footer/hash and no trailing bytes. It rehashes the original source afterwards. The source-stream substitution arithmetic differs from the constructor's forced-exponent formulas; nevertheless this remains producer code, not different-model certification. The accepted normalization/faithful-cover theorem and provisional whole-shear/Hermite composition are explicit external dependencies. No further theorem-interface gap is currently identified, but the full implementation has not been exercised on production data.

## Fail-closed execution and bounded evidence

The only production entry requires a fresh exact cwd `/home/ubuntu/d125-hybrid-affine-pilot-20260907`, Linux/Amazon EC2 DMI for i-0da0cebfc97c9fd54, current boot identity, new registration and physical root-GREEN hashes, explicit construction-only authority, accepted hybrid/code gate pins and exact source/code pins. No such authority or registration is created here. Source reads occur only after authorization; the old source path is hard-bound. Caps cannot exceed300 shared wall/CPU seconds,4GiB AS,128MiB per regular file,100k terms,1m multiplication pairs/retained terms and4096 coefficient bits; core files are disabled. Fresh output paths use exclusive creation. One main process constructs then replays under the same timer; there are no descendants, solver calls, retries or alternative modes.

Future execution still needs separately scoped actual-host controls and root's unchanged exact-PGID CAPRUN for sampled group RSS/reaping. No runner rewrite is supplied. Stage telemetry records member, degree, pivots or row before arithmetic; cap errors include pending term/pair counts and context, addressing the previous missing-layer evidence. Serialization checks bytes before creating polynomial wire lists. Stage records intentionally use stderr; this construction instrument must not inherit the solver instrument's empty-stderr success rule. Success requires normal completion plus the explicit full replay receipt. A completed construction footer alone is not a completed replay.

Twenty tiny methods passed normally and−O; final paired command took0.279s, with12 CPU seconds and512MiB AS per interpreter, each externally bounded by30s. Controls include the actual shifted3x3 matrix and orientation, small independent Laurent-power lift expansion, target/factor mutations, fixed-face and fixed-zero corruption through the actual map checker, field splitting, missing/reindexed rows, wrong guards/cofactors, whole lower-coefficient shear inverse, both cover identities, cap-stage identity, off-host/missing-authority/wrong-boot/registration/gate failures, and an actual serialized row corruption with a recomputed valid footer hash. Zero Assert nodes. No full81-coordinate map or803-row loop was run locally.

Exact frozen code pins: constructor `aa65e7104d3fcf5ad868eea952587a6841d784c6f9469c6c42ea2a02913ef264`; replay `06475a2a566b4ed617068d65f3a0473ef83c16e2cb357dcb959ee46716781c23`; tests `54f03f6af6c8e7462f620e11f588bcf0aa209cca18c2fbb465da938c7c3ad2db`. Full input/evidence pins and custody accompany this report. Old code/source/report bytes were not edited. **STOP: prepared only, no launch authority. All writers/jobs idle at handoff.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7913`.
- Body SHA-256:
  `c593088de458e957b940d487111b5ad2c194b53d7d54bb1f8f9489c3bcf57cb1`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
