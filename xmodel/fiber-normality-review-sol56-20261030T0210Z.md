# FIBERREVIEW0210 — hostile review of proper-model fibre cohomology

Verdict: **PASS_CONDITIONAL.** This is the first independent hostile review of this new proof, not a retry. Requested identity was the existing Sol adapter/model `gpt-5.6-sol`, ultra; actual hosted identity is unverified. No agents, jobs, workers, or coordinator actions were launched.

I found no counterexample or missing condition in the stated proper-model argument. The exact accepted theorem is: let `X` be a finite-type normal integral affine complex surface containing a specified dense open `U=A2=Spec C[ell,v]`, and suppose `q:X->P1` is a morphism with `q|U=ell` and scheme-theoretically `q^{-1}(A1)=U`. Then every omitted prime curve `E` (with its reduced integral structure) is smooth. If, in addition, the separately inherited boundary theorem supplies a finite birational normalization `A1->E`, then it is an isomorphism and `E=A1`. The Keller application remains conditional on the inherited marked open-immersion/ruling and boundary-normalization packages. No Keller exclusion follows.

Concrete checks completed so far:

1. Normalizing the projective graph closure does preserve `X`: the graph is closed in `A^m x P1`, hence is the intersection of its projective closure with that open; normalization commutes with restriction to the open, and normality of `X` makes the restriction an isomorphism. The second projection therefore extends `q`.
2. The singularity of the normal projective target `T` is not an obstruction. Resolve `T`, resolve the induced birational rational map from `P1 x P1` by point blowups of the smooth source, and compose to `T`. The two maps to `P1` agree on dense `U`, hence everywhere. This supplies a smooth `Z`, a point-blowup composite `pi:Z->P1 x P1`, and a proper birational `rho:Z->T` over the same base.
3. On a point blowup, the two standard affine charts have overlap `A[t,t^{-1}]/(xt-y)`. Splitting a Laurent representative into nonnegative and negative powers gives Cech `H1=0`; the two-affine cover gives higher vanishing. Together with proper birational pushforward to the regular/normal intermediate surfaces this yields `R^j pi_*O_Z=0` for `j>0` and `pi_*O_Z=O`.
4. For affine `V` in the base, `H1(P1 x V,O)=0`, so `H1(Z_V,O)=0`. Normality of `T_V` gives `rho_*O_Z=O_T`; the five-term/low-degree Leray sequence therefore injects `H1(T_V,O)` into `H1(Z_V,O)`. No vanishing of `R^1 rho_*O_Z`, and hence no rational-singularity hypothesis, is used.
5. A generic first hyperplane meets the projective one-dimensional fibre over `b` in finitely many points, and a second can avoid those points. Properness lets one shrink affine `V` so their common zero locus misses all of `T_V`. The two affine hyperplane complements, with affine intersection, cover `T_V`, giving `H2(T_V,F)=0` for every quasicoherent `F`.
6. Dominance and integrality make the base parameter a nonzerodivisor, so the exact sequence for the full scheme-theoretic, possibly nonreduced fibre gives `H1(F_b,O)=0`. For every reduced irreducible component `C`, the quotient `O_F -> O_C` and the same two-affine cover give `H2(F,K)=0`, hence `H1(C,O_C)=0`.
7. For the finite normalization of integral projective `C`, both global-function spaces are `C`; the normalization exact sequence forces its zero-dimensional cokernel to vanish. Thus `C` is normal, smooth, genus zero, and `C=P1`. For an omitted prime `E`, its reduced closure is a fibre component and intersects `X` exactly in `E`; hence `E` is smooth. The retained finite birational `A1->E` is then an isomorphism.

The remaining Keller gap is unchanged: nothing here makes the infinity fibre empty, reduced, or connected; makes `X` smooth; makes the target map etale on `E`; makes the target image of `E` nonsingular or immersed; or proves properness, `N=1`, or JC2.

## Hostile disposition and foundation boundary

The proof does not silently apply the supplied Stacks factorization excerpt to singular `T`: that excerpt states the regular-surface result. The valid route explicitly imports resolution of a normal complex surface, chosen isomorphic over the smooth open `U`, followed by resolution of the induced rational map from the smooth ruled surface by closed-point blowups; composing with the target resolution gives `rho`. This is exactly the named standard surface-resolution foundation allowed by the task. Agreement on dense `U` proves the resulting diagram is over the same `P1`.

Likewise, the supplied excerpt of Stacks 50.16.3 has setup not reproduced in the packet and is not broadened here. The required structure-sheaf assertion was checked directly: locally the blowup ideal is the regular-parameter ideal `(x,y)`; the two affine charts and their affine overlap give the stated Laurent splitting. The calculation is local on the base, applies after restricting over any affine `V`, and iterates through the point blowups. The remaining named foundations used at their standard scopes are: projective normalization, resolution of complex surfaces/rational maps, proper birational pushforward of `O` to a normal target, low-degree Leray, affine Cech cohomology, finite normalization of curves, and the genus-zero classification over `C`.

No rational-singularity premise enters: only `rho_*O_Z=O_T` is needed for the Leray edge injection. No flatness or reducedness of `f` is needed: dominance from an integral surface to the smooth curve makes a local base parameter a nonzerodivisor, so the exact sequence is for the full scheme fibre. The quotient argument is separately applied to every reduced component. I found no defect after attacking all seven requested transitions.

This review makes no novelty judgment, no downstream image-immersion inference, and no exit-price assertion. The smoothness result does not say that `X` is smooth, that the total infinity fibre is reduced or connected, that the finite target map is etale on `E`, that the target image is nonsingular, that `E` is empty, or that JC2 holds.

## Remaining Keller gap

The retained Keller packages may now replace “finite-bijective `A1` normalization” by “omitted prime curve is actually `A1`” at the exact stated conditional scope. They still do not exclude a nonempty infinity fibre. A Keller-specific global argument must show the fibre is empty or otherwise contradict the finite map and constant-Jacobian source geometry. Normal ramification, singular/nonimmersed target images, fibre multiplicities, sheet-budget slack, nonproperness, and degree `N>1` all remain possible under this lemma. Thus no properness, surjectivity, polynomial inverse, `N=1`, or JC2 conclusion is obtained.

## Independent custody, coverage, and events

Measured events (all UTC): first action `2026-10-30T02:09:08Z`, sampled immediately before the first manifest window in the same command; full nine-governor plus `HQ-STATE.md` coverage observed complete `2026-10-30T02:13:43Z`; substantive unsealed partial observed to exist after its write `2026-10-30T02:16:02Z` (`3906` bytes, `19` LF, SHA-256 `77e268440965e05f358102d124c25890f8b77a27da8be2386968327fc0ebd92f`); input post-hash pass observed complete `2026-10-30T02:16:22Z`. A terminal body and post-seal existence time can only be observed after writing stops and are therefore left to the post-write tool receipt; none of these preceding clocks is called a write-completion time.

The manifest was read first and wholly in bounded windows. Its pre/post SHA-256 was `cd81b84f4cab1995fcae5ab2c7410fccd0fbe1c510f52aa682b34ce01843ad6a`, exactly the admitted hash; it was `8086` bytes and `232` LF. Before any declared body, one metadata-only pass covered all 16 declared records in two groups of eight. Every record had actual launcher snapshot mode `0400` (manifest-declared original packet mode `0444`) and no symlink ancestor or leaf. Every byte/LF/hash matched; the post-pass was unchanged. Original provenance paths were not read.

Exact metadata and pre/post full-file hashes:

- `HQ-AGENTS.md`: `1520` bytes, `23` LF; pre `06ba4c0898c8a4272478b16f8b72f2877cf235ed3a8af5016059d1114dd0c34f`; post `06ba4c0898c8a4272478b16f8b72f2877cf235ed3a8af5016059d1114dd0c34f`.
- `HQ-POLICY.md`: `6755` bytes, `112` LF; pre `6e53d77c4bfca8553df5510bbe5f94f7d0955347c4d8bba58a67e4c15a275634`; post `6e53d77c4bfca8553df5510bbe5f94f7d0955347c4d8bba58a67e4c15a275634`.
- `HQ-RESEARCH_POLICY.md`: `9551` bytes, `162` LF; pre `1ce21f90ddbfad47bdbeff07940f1704643465df5a0bd8446fc2b8e9cc614c62`; post `1ce21f90ddbfad47bdbeff07940f1704643465df5a0bd8446fc2b8e9cc614c62`.
- `HQ-RESTRICTIONS.md`: `18817` bytes, `259` LF; pre `f90beac94a223085b0b4d342138a40200b2779869d0d29fc75caf4a0a60477ed`; post `f90beac94a223085b0b4d342138a40200b2779869d0d29fc75caf4a0a60477ed`.
- `HQ-RUNBOOK.md`: `34745` bytes, `507` LF; pre `4e874134c6bbb925415545050eb3e30de3d61171899ba727ed2123c9a3eb0c06`; post `4e874134c6bbb925415545050eb3e30de3d61171899ba727ed2123c9a3eb0c06`.
- `HQ-STATE.md`: `62858` bytes, `222` LF; pre `3790126f7febc44f1d9d2dd9a7bd54f94ae8297a738fcd4000d9c7f3972c48d6`; post `3790126f7febc44f1d9d2dd9a7bd54f94ae8297a738fcd4000d9c7f3972c48d6`.
- `PUBLIC-AGENTS.md`: `1229` bytes, `22` LF; pre `31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f`; post `31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f`.
- `PUBLIC-README.md`: `5391` bytes, `102` LF; pre `7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf`; post `7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf`.
- `PUBLIC-COORDINATION.md`: `6042` bytes, `107` LF; pre `9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e`; post `9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e`.
- `PUBLIC-FALLACY-v2.md`: `1985` bytes, `36` LF; pre `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5`; post `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5`.
- `candidate.md`: `7577` bytes, `72` LF; pre `219cff47b913f049978591804db72848458c9db509e50c717ffdada0ef6c44b7`; post `219cff47b913f049978591804db72848458c9db509e50c717ffdada0ef6c44b7`.
- `ruling-lemma.md`: `4542` bytes, `42` LF; pre `d86012d37f83631b4a61744362c3e836776bd5c66324062b772b380775bb69f3`; post `d86012d37f83631b4a61744362c3e836776bd5c66324062b772b380775bb69f3`.
- `ruling-review.md`: `15974` bytes, `156` LF; pre `902033f3447213d602c2cd6e4cf8227b85528bb124752bc9f63b5157ee5ba5e7`; post `902033f3447213d602c2cd6e4cf8227b85528bb124752bc9f63b5157ee5ba5e7`.
- `boundary-normalization.md`: `11382` bytes, `153` LF; pre `8b1f594c59d71e05a5b5cfd78869280c06279a5fd823b6899c9912733c4f37c7`; post `8b1f594c59d71e05a5b5cfd78869280c06279a5fd823b6899c9912733c4f37c7`.
- `source-factorization.txt`: `5072` bytes, `48` LF; pre `6510fb16ed699da09416db28f51c353e4d56acd51b541ab780b3637c1bf95b85`; post `6510fb16ed699da09416db28f51c353e4d56acd51b541ab780b3637c1bf95b85`.
- `source-blowup.txt`: `2967` bytes, `48` LF; pre `5a74a03e31d16763ed03753596c764addbb4186c186941fa483b3907b6430a68`; post `5a74a03e31d16763ed03753596c764addbb4186c186941fa483b3907b6430a68`.

Before their bodies, all four manifest-marked mathematical seals verified:

- `candidate.md`: body `7245` bytes, SHA-256 `1ff97f73faf8199e750faf246b1f73e2e98286b65d0a0a69f6cd247138ccc362`, basis `a0b799468cd065da71cbd13b8bb578438ca5e9f3`.
- `ruling-lemma.md`: body `4210` bytes, SHA-256 `0009790aec1450b97bd80e89515345f47c5ef0798983f75fab390faffbf2fc2f`, basis `a0b799468cd065da71cbd13b8bb578438ca5e9f3`.
- `ruling-review.md`: body `15641` bytes, SHA-256 `b9839bb3bd09a3cea41f0e3a70c8e5fff2094e25b4966e5b18efd2c3ffd2db9b`, basis `a0b799468cd065da71cbd13b8bb578438ca5e9f3`.
- `boundary-normalization.md`: body `11049` bytes, SHA-256 `7e5383ddfac0af238d2668a077af1aed32f6199d1ccfc5e7eb63754284380f35`, basis `3271d021f9f89db8972a8d090768ea3e1013d03f`.

Actual displayed body ranges were contiguous and complete, in the required order:

- `input-manifest.json`: `1-24,25-48,49-72,73-96,97-120,121-144,145-168,169-192,193-216,217-232` (`232` LF).
- `HQ-AGENTS.md`: `1-23` (`23` LF).
- `HQ-POLICY.md`: `1-24,25-48,49-72,73-96,97-112` (`112` LF).
- `HQ-RESEARCH_POLICY.md`: `1-24,25-48,49-72,73-96,97-120,121-144,145-162` (`162` LF).
- `HQ-RESTRICTIONS.md`: `1-24,25-48,49-72,73-96,97-120,121-144,145-168,169-192,193-216,217-240,241-259` (`259` LF).
- `HQ-RUNBOOK.md`: `1-24,25-48,49-72,73-96,97-120,121-144,145-168,169-192,193-216,217-240,241-264,265-288,289-312,313-336,337-360,361-384,385-408,409-432,433-456,457-480,481-504,505-507` (`507` LF).
- `PUBLIC-AGENTS.md`: `1-22` (`22` LF).
- `PUBLIC-README.md`: `1-24,25-48,49-72,73-96,97-102` (`102` LF).
- `PUBLIC-COORDINATION.md`: `1-24,25-48,49-72,73-96,97-107` (`107` LF).
- `PUBLIC-FALLACY-v2.md`: `1-24,25-36` (`36` LF).
- `HQ-STATE.md`: `1-8,9-16,17-24,25-32,33-40,41-48,49-52,53-56,57-60,61-64,65-72,73-80,81-88,89-96,97-104,105-112,113-120,121-128,129-136,137-144,145-152,153-160,161-168,169-176,177-184,185-192,193-200,201-208,209-216,217-222` (`222` LF, separately charged).
- `candidate.md`: `1-24,25-48,49-72` (`72` LF).
- `ruling-lemma.md`: `1-24,25-42` (`42` LF).
- `ruling-review.md`: `1-24,25-48,49-72,73-96,97-120,121-144,145-156` (`156` LF).
- `boundary-normalization.md`: `1-24,25-48,49-72,73-96,97-120,121-144,145-153` (`153` LF).
- `source-factorization.txt`: `1-24,25-48` (`48` LF).
- `source-blowup.txt`: `1-24,25-48` (`48` LF).

The nine copied non-STATE governors totalled exactly `1330` LF. The six mathematical/source inputs totalled exactly `519` LF. Thus declared non-STATE input bodies were exactly `1849` LF; adding the manifest gives actual non-STATE displayed coverage `2081` LF. STATE was separately exactly `222` LF. Total displayed input body coverage was `2303` LF. Primary coverage was exactly `96` LF, the two supplied 48-LF excerpts and nothing else. There were no repeated, clipped, cropped, or unread ranges; every body response contained one contiguous window, every non-STATE window was at most 24 LF/8192 serialized bytes, and every STATE window was at most 8 LF (reduced to 4 LF around the dense range).

Source searches/downloads: `0`. Repository/history queries: `0`. CAS/computation: `0`. Control-family exploration: `0`. Agents/jobs: `0`. Shared-document/input/source edits, commits, pushes, auth/configuration changes, operational ticks, and automatic-memory writes: `0`. Own-report body rereads: `0` LF; only metadata/hash observations and the mandated terminal stamp/verify remain. No excluded repository or `max11` was inspected or enumerated.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14496`.
- Body SHA-256:
  `236a0bf00d632280137ece4d547a7428f2c89fece8ae24d925dbd18ad9ffd87b`.
- Frozen basis: `a0b799468cd065da71cbd13b8bb578438ca5e9f3`.
