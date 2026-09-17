# Zero-free branch-model criterion and uniform rational-Liouville client — hostile Sol FIRST

Reviewer: swarmHQ native Sol fallback review seat; exact hosted model ID is not independently exposed. September 17, 2026. Frozen producer commit `65c6bebcf082cae28e433290b6ffde7999fb12d6`. Evidence: MANUAL proof audit, with precisely the classical imports named in the prior promoted smooth-branch theorem. No CAS, scientific interpreter, source fetch, or new primary-source proof. This review has no independent promotion authority.

Verdict: **CONFIRMED** for the two exact producer claims: (A) the general zero-free smooth-branch-model obstruction, and (B) its all-`Q`, all-integration-constant rational-Liouville client. This is conditional on an *already given* smooth projective rational target model satisfying both hypotheses; it does not assert that one exists for an arbitrary Keller extension. The target change has scalar, nonzero constant Jacobian and is birational in the fixed target field; the proposed output is a polynomial Keller pair on the *whole* affine source. Arbitrary finite rational source embeddings are covered. Nonconstant-Jacobian target changes are not.

## Frozen custody and charged evidence

The frozen producer `xmodel/zero-free-branch-model-swarmHQ-root-20260917T044000Z.md` was read in full, 296 lines. Its full SHA-256 is `d52eee9548049a52fe3cca997423837d1da2aecff3e0780a54b5da4ece07dd54`; the artifact verifier returned `VERIFIED`, body SHA-256 `5a389ebac77d76d0ba321bfb5b1793be7a0e92f964f6e5a47d314f60a3b59dd3`, manifest SHA-256 `53e47e3a353a1c88fa863911f8d586b16cb0229f6733820e35d5e51c63be613c`, basis `b6e4515c7175b8d87d80c2dfce05f8d460d3be6c`, and both artifact and manifest mode `0444`. Git HEAD was the frozen commit, with the producer in its tree as a regular `100644` blob. The whole prior smooth-branch producer and prior Sol FIRST matched respectively `f839a4b8d6734d73e45850ed3253211f946ca192eab99c30d2663e0deaf8a85a` and `cadbc15edc36fd88ac973f42fcf5d8efcd18a42a00ea74adc60f7f143f7188eb`. Their exact imported theorem scopes were checked, not independently reproved.

The review also read HQ AGENTS, POLICY, RESEARCH_POLICY and the active zero-free admission at the top of STATE; public AGENTS, README, COORDINATION, FALLACY, the relevant current APPROACHES section, and the accepted AUDIT entry including its binding nonconstant-J wording correction. AUDIT and APPROACHES were scoped reads, not whole-read claims. Input pins before report writing: HQ AGENTS `06ba4c08`, POLICY `29d6bcea`, RESEARCH_POLICY `710fcf0c`, STATE `a3505934`; public AGENTS `31f54fa5`, README `7181a9dd`, COORDINATION `9b7a45ae`, APPROACHES `e52e7bd6`, FALLACY `e47fd16c`, AUDIT `95347abe`; the three whole report hashes above. These are SHA-256 prefixes except where full hashes are displayed. Postwriting checks below confirm the unchanged charged reports and public contract. STATE is a live operational ledger and is not assumed byte-immutable after the review.

## A. General zero-free-model criterion — CONFIRMED

Let `K0=C(p,q)`, `K/K0` finite of degree greater than one, and `Z` a smooth projective rational surface with identified function field `K0`. Assume `div_Z(dp∧dq) <= 0` and that every irreducible component of the reduced branch divisor of the finite normalization of `Z` in `K` is smooth. Let `(p',q')` generate `K0` and satisfy `dp'∧dq'=c dp∧dq`, `c∈C*`. The direction needed is the rational map `r:P2_(p',q') ---> Z`, not its inverse.

Resolve `r` by `pi:W->P2_new` and `psi:W->Z`. At any finite new-plane point `a`, `dp'∧dq'` is regular and nowhere zero. The first exceptional divisor of a point blowup above `a` has order `+1` in its pullback; every subsequent exceptional divisor has order `1` plus nonnegative zero-divisor multiplicities at the center. If a `pi`-exceptional divisor above `a` were not contracted by `psi`, its generic DVR would identify with that of a curve on `Z`, where `dp∧dq` has order at most zero. This contradicts `pi*(dp'∧dq')=c psi*(dp∧dq)`. Hence all such exceptional divisors are `psi`-contracted. The whole `pi`-fiber is connected and maps to one point. The reduced graph of `r` has singleton fiber at `a`; properness and quasi-finiteness near `a` make its projection finite, and finite birationality over normal `P2_new` makes it an isomorphism there. Thus `r` is a morphism on the entire `A2_new` *to projective* `Z`. It may have affine coordinate poles; no polynomiality of the target change is inferred.

Resolve the now-regular `r` using centers outside `A2_new`. Then `W` contains that plane unchanged, and `psi` is a proper birational morphism between smooth surfaces, factoring into point blowups by the inherited Stacks 0C5H/0C5R surface inputs. For a ramified affine curve `D` of the normalization of `A2_new` in `K`, its closure in `W` either dominates a curve `B⊂Z` or is `psi`-exceptional. In the first case generic DVRs agree, so `B` is a branch component on `Z`; its smooth strict transform contains `D` as an open subset. In the second case `D` lies in a smooth rational exceptional curve. This accounts for branch divisors produced by a target chart at old infinity, rather than only the visible old branch components. Intersections among components and singularities of the covering normalization are immaterial.

If no affine branch `D` existed, purity would make the finite connected normal cover of regular `A2_new` étale. The accepted triviality of connected finite étale covers of complex `A2` would force degree one. Thus at least one smooth affine branch curve exists. The purity/trivial-cover assertions retain the accepted imported tier; they are not silently replaced by smoothness of the cover.

Now suppose there is a finite embedding `K->L=C(u,v)` making `F=(p',q')` polynomial Keller on the whole source. For a ramified valuation `v_K` over `ord_D`, any extension `w` to `L` has `e(w/ord_D)=e(w/v_K)e(v_K/ord_D)>1`. If `F` were proper over a neighborhood of the generic point of `D`, Keller implies quasi-finite étale, and proper plus quasi-finite makes the restriction finite étale. The actual source there is normal and has *full* function field `L`, so it equals the normalization in `L`; all divisors above `D` then have ramification index one. This contradiction attaches `D` to the actual polynomial map's nonproper-value set, not merely to an intermediate normalization. Since that set is a proper algebraic curve for a generically finite plane polynomial map, `D` is an irreducible component.

The named Jelonek polynomial-coverage input supplies a nonconstant `A1->D`. As `D` is already smooth, it extends to a finite map `P1` onto the projective completion of `D`, forcing genus zero. Every omitted completion point must have preimage at the single parameter infinity; the complement is nonempty because `D` is affine, so it is exactly one point. Hence `D≅A1`, contradicted by the named Chau no-`A1`-component theorem for nonsingular polynomial plane maps. These are the same imported statements, at the same use-scope, as the promoted prior FIRST. I find no new source-scope gap in this extension.

## B. Uniform rational-Liouville client — CONFIRMED

Take `Q∈C[t]` nonzero, `I'=Q` with arbitrary additive constant, and `t=x^3 y`, `p=x^2 Q(t)`, `q=I(t)/(2p^2)`. Directly, with `y=t/x^3`, one has `dp=2xQ dx+x^2Q' dt`, `dq=Q dt/(2p^2)-I dp/p^3`, and `dp∧dq=x^-3 dx∧dt=dx∧dy`. This is a rational constant-area donor, not a polynomial Keller pair.

Write `d=deg I=deg Q+1≥1`. Since `p,t` are independent, `C(p,t)/C(p,I(t))` has degree `d`, even for repeated roots or coincident critical values. Then `K=C(p,t)(x)` with `x²=p/Q(t)`. The `p`-valuation of this radicand in `C(t)(p)` is exactly one, so it is nonsquare and `[K:K0]=2d>1`. This explicitly retains the hidden quadratic leg; `Q` constant gives degree two, not identity. The formula `y=t/x³` recovers the full source field.

Let `V={I(a):Q(a)=0}` as a finite set. On `U={p≠0}∩∩_{b∈V}{2p²q≠b}`, the equation `I(t)=2p²q` is finite étale: its leading coefficient is a nonzero scalar and its derivative `Q(t)` is invertible on this base change. There `Q(t)` and `p` are units, so adjoining `x` by `x²=p/Q(t)` is also finite étale in characteristic zero. The composite is a connected regular, hence normal, finite cover with the full field `K`. Thus no affine branch divisor is hidden outside `p=0` or `2p²q=b`; this handles multiple roots, repeated critical values, and the quadratic cover together. At `b=0`, the latter reduced support is just the two smooth coordinate lines. For `b≠0`, it is the irreducible cubic `A²B=(b/2)C³` in old projective coordinates; all other projective branch components can only lie on the smooth line at infinity.

Each nonzero-value cubic is singular only at `o=[0:1:0]`. In local coordinates `a=A/B`, `b0=C/B`, its equation is `a²=(b/2)b0³`. Blow up `o`; the chart `a=b0 s` gives strict transform `s²=(b/2)b0`, smooth at its unique exceptional point. The other blowup chart contributes no further point of the strict transform over `o`. The same single blowup resolves every such cubic simultaneously, regardless of `b`. The coordinate lines and infinity have smooth strict transforms; the new exceptional curve is smooth. The branch divisor on `Z=Bl_o P2` is supported among precisely these strict transforms and the exceptional curve because the blowup is an isomorphism away from that curve. Actual ramification of each listed component is not required.

On old `P2`, `div(dp∧dq)=-3L_infinity`. Because `o∈L_infinity`, the point-blowup formula yields `div_Z(dp∧dq)=-3L_strict-2E`, with no zero component. Both hypotheses of A hold on this one explicit rational model for every allowed `Q,I`. Therefore every scalar-constant-Jacobian birational rational target change in the fixed field `C(p,q)`, followed by every finite rational source embedding, fails to make a whole-plane polynomial Keller pair. This is uniform in degree, critical multiplicity and integration constant; it is not a finite target-word or source-degree search.

## Hostile controls and limits

- Map direction is essential: the descent proves `P2_new->Z` projectively defined on all of `A2_new`. It does not assert an inverse morphism `Z->P2_new` or an affine-valued map.
- Zero-freeness is essential: a blowup at a finite point of a regular area form creates an exceptional zero. Resolving arbitrary singular branch curves does not manufacture an eligible model. No theorem here places arbitrary Keller extensions on one.
- If `K=K0`, the purity step supplies no nontrivial branch and the identity Keller map is a countercontrol. The client always has degree `2d>1`.
- The old birational cusp map with *nonconstant* Jacobian refutes unrestricted smooth transport only. The binding AUDIT correction explicitly forbids calling it a counterexample to donor exclusion for all nonconstant-J target maps. Such maps remain outside both claims here.
- The pole-bearing scalar-Jacobian map `(u,v)->(u+1/v,v)` confirms why projective regularity is weaker than affine regularity or polynomiality.
- No nonbirational target postcomposition, different target subfield, arbitrary donor, or JC2 resolution is claimed. No new source existence, degree ceiling or automatic successor follows.

## Postwriting custody check

Before closure, the charged producer and prior producer/FIRST SHA-256 values, and the public COORDINATION, APPROACHES, FALLACY and AUDIT pins were rechecked unchanged. No Git files or shared ledgers were modified by this review; the only authorized publication is this report and its artifact custodian files. Independently owned `jc2-lean` and `jc2-web` were not entered or inspected.

## COLLISIONS

status: EMPTY

- NONE — no explicitly tagged `OPEN[...]` is raised in this review.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11862`.
- Body SHA-256:
  `9afbe5835a2d656b7d2e00d05ba8e4fada3a591ca7a50836bc8c6075e1a209cc`.
- Frozen basis: `65c6bebcf082cae28e433290b6ffde7999fb12d6`.
