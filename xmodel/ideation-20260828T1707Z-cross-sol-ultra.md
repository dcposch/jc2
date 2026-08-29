# Cross-pollination review — Sol Ultra — `20260828T1707Z`

## Verdict

No proof or counterexample to JC2 is obtained. The highest-information result of
the cross-read is that `ROOT-W2` should be **PROMOTED**, but only as a theorem
for the two-pole, on-axis `td=6` root sector. The unique surviving interior
object remains residue A. MFE gives it no kill: the selected-exit weight is 2;
the `R3` cap is 3 and the `R4` cap is 2. The q-only resonant orbit is invisible
to the f-tree selected-exit geometry, so none of `MERGE-DIFFERENT`, `RES-AV`,
`Q-GHOST`, or `A47-BUDGET` may count it until a new off-tree object is built and
then related injectively to a bounded global resource.

The fastest complete GGV route is a hybrid: repair and mutation-gate the
existing complement-recursion adapter on one full `Q1P03` node, then organize
all descendants by Fitting rank level and use deterministic pivot charts inside
each level. Do not launch a six-branch fanout before that one node passes.

## 1. `ROOT-W2`: line-by-line dependency audit

Claim under review: no genuine root merge occurs in the two-pole `td=6`
sector.

1. `td=6`, two poles, and `Lambda_i>=beta>=3` force
   `Lambda_1=Lambda_2=3`, type `(alpha,beta)=(2,3)`, and the unique row-1
   entry. This is the MP4/table-(23) entry pin. **Promoted.**
2. Each pole has `M=gcd(2,3)=1`. **Promoted.**
3. `L1a(b)` says every chain vertex strictly above the meet has `M=1`, a
   single simple `nu`-orbit, and `lambda=0`. Its proof uses Statement 8.4 on
   the nonroot pre-meet child, the already-present chain edge to obtain
   `deg q>deg p`, corrected Statement 3.18 for any second direction, and
   repaired Propositions 6.7--6.8 to manufacture a third pole. It does not
   apply Proposition 8.4 at the root. **Promoted at this scope.**
4. The potentially weak clause is whether step 3 survives when the meet itself
   is `(0,y)`. It does: the induction is only over vertices strictly above the
   meet; its third-pole contradiction is completed before the root endpoint is
   used. `SHEET6-A3L1-REVIEW` independently confirms the induction “at every
   vertex and every merge depth,” including immediate merges. Thus every actual
   parent arriving at such a root carries the certified alphabet `W={2}`.
5. The post-cutoff mixed-root theorem says every actual searrow root-parent
   edge is Proposition 9.3 case I and satisfies
   `X_R=mu_e(1-w_e)=A/B`, hence `0<w_e<1`, for arbitrary `mu_e`. This step
   needs neither the all-simple formula nor a root use of Statement 8.2.
   **Promoted.**
6. Steps 4 and 5 contradict each other: the same parent invariant would be
   both `w_e=2` and `0<w_e<1`. Therefore no such root merge exists.

**Disposition: `PROMOTE`.** Exact scope: two poles, `td=6`, forced row-1
on-axis entries, genuine contact-zero root meet. This does not prove root/SF1
landing completeness, exclude single-pole root signatures, treat `m>=3`, or
give an all-`mu>=2` formula `A=sum mu`, `B=r+l`, `k=0`, or `B>A`. The weakest
dependency is `L1a(b)`'s row-1-to-meet propagation; it survives the audit.

## 2. Residue A: comparison of proposed attacks

All proposals must respect the exact MFE ledger:

```text
two pole endpoints:       0
merge:                    0
shared suffix exit:       2
R3 terminal psi=2:        2 <= 3
R4 terminal psi=3:        2 <= 2
```

The merge has two pole arrivals and one q-only resonant orbit. The first two
are excluded arrivals; the third is not a root of `p`, hence supplies no
`T_a` direction, vertex, selected exit, or cv witness.

| Proposal | Exact useful content | Does it geometrically see the q-only orbit? | First missing implication / verdict |
|---|---|---|---|
| simultaneous coefficient/parent match | Impose both Proposition 9.3 edge equations on one rigid child with `a1/a2=2+-sqrt(3)` | Yes, as a coefficient of the common q-pattern coupled simultaneously to both p-parents | Need a provenance-complete two-edge substitution through the first mixed resonant jet. **Run first.** |
| coefficient-complete seed-to-jet lifting | Extends a compatible two-edge solution through Jacobian and h-family equations | Yes, if the q-root coefficient is retained as its own variable and not projected to Q-data | First require the simultaneous parent match; then prove every denominator/chart branch is covered. **Run on survival.** |
| `MERGE-DIFFERENT` | Attempts to turn local different/conductor length into actual flags | It sees the q-root in the completed local algebra | Missing an injection from the non-pole different summands to distinct actual cv flags. Without it, this is merely a local length. **Provisional.** |
| `RES-AV` | Interprets the q-only direction as a possible asymptotic-value branch | Potentially: ambient rays, not `T_a`, are the intended object | `D_g=-1` does not itself prove `g` has a finite limit, that the limit varies, or that one-fibre data vary generically in `a`. **Conjectural; test after coefficient match.** |
| `Q-GHOST` | Moves to a translated pair/tree where the invisible direction might become visible | Not yet; it currently renames the desired translated threshold | Must exhibit a shift `b`, an actual translated-tree direction, and a distinct witness not already owning the suffix charge. Even +1 does not kill R3. **Low priority.** |
| `A47-BUDGET` | Uses the auxiliary map `(f,h_1)` and its explicit ramification divisor | It sees q-roots as h-pattern roots off the f-pattern | Missing both an ambient attachment theorem for non-`T_a` directions and a computable global branch bound. The MFE attachment lemma cannot be transferred verbatim because the flags do not exist in `T_a`. **Identity promoted; budget conjectural.** |

The synthesis is a two-stage discriminator. First solve the simultaneous
coefficient/parent system, which is the only proposal already formulated on
the actual rigid q-pattern and both incoming p-parents. If it survives, retain
the q-only coefficient in a coefficient-complete jet lift. Only then compute
the local different and asymptotic limit on that same exact algebra; this lets
`MERGE-DIFFERENT` and `RES-AV` share a proof object rather than proliferating
unrelated models.

## 3. `A47`: exact identity and missing theorem

For `h_1=g^alpha-s_0 f^beta` and `J(f,g)=1`, bilinearity and the chain rule give

```text
J(f,h_1)
 = J(f,g^alpha)-s_0 J(f,f^beta)
 = alpha*g^(alpha-1) J(f,g)
 = alpha*g^(alpha-1),

J(h_1,g) = -s_0*beta*f^(beta-1).
```

Thus the elementary identity is correct. It says the ramification divisor of
`(f,h_1)` is supported on `g=0`, with multiplicity `alpha-1`; it does **not**
count branches at infinity or attach q-only roots to tree flags.

The first exact missing implication for `A47-BUDGET` is:

```text
each effective root of q_F not shared by p_F
  -> a well-defined branch of h_1 at infinity in the relevant fibre-a sector,
with distinct (F,orbit) producing distinct branches.
```

Only after that injection is proved may one seek a finite, coefficient-level
upper bound for those branches from `J(f,h_1)=alpha*g^(alpha-1)`. The promoted
contact-tree attachment theorem does not supply this arrow because its witness
starts from an actual selected `T_a` direction. Consequently `A47.1/A47.2` are
**promoted elementary facts**; `A47-BUDGET` remains a **conjecture**.

## 4. Fastest complete GGV route

Choose a **hybrid**, ordered by current proof-object maturity.

1. Repair the substitution adapter and run exactly one complete `Q1P03`
   complement node. The prior `REDUCER_PLACEHOLDER`/rc0 event is purely an
   adapter failure and provides no mathematical evidence.
2. Require the node to reproduce all 95 rational pivots, with zero parser
   diagnostics, before accepting any endpoint computation.
3. Once that node passes, stratify descendants by Fitting/rank level. At each
   closed rank-drop locus select a deterministic nonzero minor and use the
   already-working adjugate kernel on its open; return the complement to the
   next closed Fitting level. This combines canonical termination by rank drop
   with the presently verified chart calculation.
4. Do not rely on a global syzygy module over a possibly nonreduced quotient
   without proving local freeness/base-change on the stratum. Do not claim that
   a nonzero endpoint coefficient in the quotient automatically has a complex
   point where it is nonzero without a properness/radical witness.

Fail-closed proof-object contract for every node:

- frozen hashes for the branch ideal, matrix, endpoint, reducer, pivot list,
  generator, and generated script;
- literal absence of placeholders and parser diagnostics; process rc alone is
  insufficient;
- the exact `95 pivots replayed` marker and ambient-normal-form replay after
  every lift/operation;
- residual/total-rank certificate: explicit nonzero-minor NF witness plus
  exhaustive next-minor vanishing;
- kernel certificate `NF(M*N)=0` and chart certificate `NF(Delta)!=0`;
- every pulled-back endpoint coefficient banked in NF;
- a child manifest for `Delta=0`, never dense-open-to-component inference;
- terminal leaf only as `EMPTY` (unit certificate), `ENDPOINT-DEAD` (all
  coefficients zero on a certified cover), or `SURVIVOR` (explicit exact
  point/nonzero witness); otherwise `NO_VERDICT_UNCOVERED`;
- zero swap and independent replay from the frozen manifest.

**AWS fanout trigger:** one repaired full `Q1P03` node must pass every gate,
including a mutation test in which a changed reducer/pivot/endpoint is rejected
or changes the proof object as expected. Only then launch the six top branches,
one 16-vCPU/128-GiB zero-swap worker each. Spawn complement children only for
mathematically distinct rank-drop ideals; review at six completed first-level
children before expanding beyond 12 workers.

## 5. New cross-peer connections (three only)

1. **`ROOT-W2` = mixed-root edge theorem + old row-1 propagation.** Opus's
   proposed theorem was not justified by its all-simple formula; the post-cutoff
   mixed-root theorem supplies the missing arbitrary-`mu` edge inequality, while
   the narrow `L1a(b)` audit supplies the parent alphabet. Neither alone closes
   the sector.
2. **Coefficient match -> shared local algebra -> different/asymptotic forks.**
   The simultaneous two-parent solve should emit one coefficient-complete local
   algebra used by both `MERGE-DIFFERENT` and `RES-AV`. A failed coefficient
   match kills residue A before either speculative global bridge; a surviving
   match prevents those proposals from silently studying different germs.
3. **Fitting levels control recursion; pivot charts carry proofs.** Fable/Opus's
   canonical Fitting stratification and Sol/Grok's reducer-safe adjugate charts
   are complementary, not competing: the former supplies a rank-decreasing
   recursion invariant, the latter supplies verified local kernel and endpoint
   identities. The adapter gate must precede both.

## 6. Ranked six-hour execution queue

Resource split: **65% proof / 35% disproof-falsification**. The coefficient
calculation is dual-use; charge its first half to proof and any surviving lift
to disproof.

1. **0:00--0:40, proof — bank `ROOT-W2` dependency certificate.** Write a
   citation-level proof trace with the six steps in section 1 and submit it to a
   hostile reader. Stop immediately on any root use of Proposition 8.4 or any
   failure of `L1a(b)` at an immediate/root meet.
2. **0:00--1:15, compute infrastructure — repair/mutation-gate one `Q1P03`
   complement node.** Stop on any placeholder, parser diagnostic, missing
   95-pivot marker, NF mismatch, swap, or non-reproducible manifest. No fanout.
3. **0:40--3:10, proof/dual-use — simultaneous coefficient/parent match.** Work
   over `Q(sqrt(3))`, both conjugate ratios, both parent labels, with literal
   edge and h-family provenance. Stop with `NO VERDICT` if any equation exceeds
   its reviewed theorem scope. Unit ideal/incompatible scales kills residue A;
   compatibility emits the exact seed.
4. **1:15--2:15, proof — specify first Fitting child from the passed node.**
   Verify the rank-drop ideal and deterministic minor selection. Stop if the
   proposed module statement needs unproved reducedness/local freeness; retain
   chart recursion instead.
5. **3:10--5:10, disproof — coefficient-complete seed-to-jet lift, only if step
   3 survives.** Extend through the first order where the q-only coefficient
   couples to both parent corrections. Stop on denominator loss, uncovered
   chart, singular isolated point without a controlled next lift, or failure of
   exact substitution replay. A smooth component becomes the falsification
   seed; an inconsistency is a proof-side kill.
6. **5:10--6:00, proof — one shared local-algebra probe.** Compute either the
   local different length and direction map or the `RES-AV` finite-limit
   condition on the step-5 algebra, choosing whichever uses no new assumption.
   Stop if it merely relabels the q-root, assumes genericity in `a`, or cannot
   map its object to a distinct global resource.

If step 3 kills residue A, reassign steps 5--6 to the single-pole/SF1 landing
audit, not to an MFE `+1` refinement. If the GGV adapter passes before hour 2,
the six-branch AWS launch is authorized but its results are outside this
six-hour reasoning queue.

## 7. Epistemic ledger

### Promoted facts

- Every genuine contact-zero root edge is Proposition 9.3 case I and satisfies
  `X_R=mu_e(1-w_e)=A/B`, `0<w_e<1`.
- The narrow audit promotes `ROOT-W2` only in the two-pole on-axis `td=6`
  sector.
- MFE is valid at selected-exit/shared-inequality scope. Residue A has weight 2;
  its `R3` cap is 3 and its `R4` cap is 2.
- All six current GGV `D(Delta)` endpoint charts are dead, with 95-pivot replay,
  zero bordered identities/lifts, zero endpoint coefficients, and proper
  `I+(Delta)`. Complements remain open.
- The two `A47` Jacobian identities in section 3 are elementary exact facts.

### Provisional claims

- The simultaneous coefficient/parent system and coefficient-complete jet
  compiler are exact experiments, not theorems until their emitted equations
  and coverage are reviewed.
- The Fitting-level recursion is a design; local module/base-change claims need
  certification on each stratum.

### Conjectures

- `MERGE-DIFFERENT` may inject non-pole different summands into distinct actual
  flags.
- `RES-AV` may turn the q-only orbit into a finite asymptotic-value branch.
- `Q-GHOST` may reveal it in a translated tree.
- `A47-BUDGET` may bound it through branches of `h_1` at infinity.

### Failed or stopped ideas

- Literal MFE composition is `NO HIT`; a single extra unit still leaves R3 at
  equality.
- Pricing the q-only orbit as a `T_a` selected exit is a category error.
- Printed `(22)`, `(22-cl)`, fixed/cross-fibre `kappa`, equality/slack, and MP8
  no-refinement remain rejected.
- Dense-open GGV death is not component death.
- The first complement pilot is an adapter failure only; it is not mathematical
  evidence.

### Disclosure and scope

The cross-packet and all ten fully specified frozen/overlay hashes matched
before their contents were used. I read the four peer reports completely and
the root/MFE overlay sources, plus only the non-`jc2-lean` dependency passages
needed to audit `L1a(b)`. I ran no CAS, AWS, network, or heavy computation and
used no subagents. `jc2-lean` was not entered, listed, searched, read, built,
modified, status-checked, or controlled. No canonical ledger or peer report was
modified. This file is the only write. A model verdict is not mathematical
evidence; promotion still requires the campaign's ordinary integration gate.
