# Hostile Review: REDUCIBLE-ALL-N — THEOREM CAGE-N gate (sol56)

## 0. Executive verdict

**REFUTED AS CHARGED.** `THEOREM CAGE-N` is not promotion-safe at its stated
scope.  Its budget, component bounds, embedding gates, local fibre identity and
single-branched-component Lin--Zaidenberg kill are substantial and mostly sound,
but five advertised load-bearing conclusions fail review:

1. `CUSP-2` is proved only for a finite holomorphic germ at a smooth point of the
   resolved source with residual Jacobian a unit.  A correction point may instead
   be the attachment to a contracted `L_C` bamboo, where Orevkov's quotient source
   is singular.  The report never excludes this case.  Hence `NO-RAM-2`, the
   universal cusp dictionary, and the `N=10` ramification threshold are OPEN, not
   theorems.
2. The survivor enumeration omits the componentwise common-normalization gate.
   With `s_l=1`, one correction-free carrier makes `eta_i` immersive and forces
   every other carrier on that component to be correction-free.  This invalidates
   many trivial placements and kills the unramified class `[22^(1)]` outright.
3. `DEG-PER` confuses normal generation with ordinary generation.  Its
   per-component floor is proved only when that component's meridians themselves
   generate a transitive group (in particular `b=1`), not for general primitive
   mixed-component monodromy.
4. One transposition meridian does not force `G=S_N`.  The live `N=8` type
   `[2+22]` admits the exact group-theoretic countermodel
   `S_2 wr S_4 < S_8`, transitive and imprimitive.
5. `NO-DEG-CAP` is a valid *conditional automorphism-orbit unboundedness* lemma
   after a small repair.  It neither proves the negation of a universal cap (which
   may hold vacuously if there is no counterexample) nor proves that no future
   numerical gate can leave a uniform finite list.

The printed `N=6,7,8` row multiplicities are also false: their entries sum to
`13,28,90`, not their own headers `14,31,104`.  Correct enumeration under the
report's advertised numerical gates gives the header totals, but consuming the
already available common-`eta` gate gives `13,27,82` in the all-`s=1` model; once
the unproved `NO-RAM-2` exclusion is removed, the sound discrete residual through
`N=8` has `13,27,91` profiles at `N=6,7,8`, with `29` carrier-level cores at
`N=8`.  Thus neither the tables nor the per-class OPEN questions can be promoted.

**Recommendation:** reject the theorem, `NO-RAM-2`, `DEG-PER`, the `S_N` pin,
the no-numeric-gate claim, the tables, and the class questions as stated.  Promote
only the corrected fragments listed in SS9.  The `N=4` and `N=5` data are recovered
only after projection to coarse dicritical/ownership profiles, not as the full
currently promoted cages.

## 1. Frozen basis, scope, and review standard

Hash verification was the first action and all four frozen files matched exactly:

```text
7c63614eff87640789d4591c67d8f8ce7d48645310d3146e87c44ddfc0dddf89  reducible-all-n-opus5-20260901.md
48d417d6980e52d61550a733f0dcded7d26a0c4e127677ac73bd544a8a00713b  b0-reducible-n5-opus5-20260831.md
bd6443b34e95213b0b2950e45c896417c492487c38a0a721eae4977d1e73f5d6  b0-reducible-n5-hostile-review-sol56-20260831.md
763eec05eb6bc00f1c13e6ff25c2b275ef3c97f20a22e6ba34621244981c56c9  block-descent-a1-alldegree-h2-coordinator-integration-fable5-20260901.md
```

I write `RN:n`, `N5:n`, `REV:n`, and `C6:n` for their frozen line numbers in
that order.  The review retains RN's scope `RED-N`: a hypothetical noninvertible
plane Keller map of geometric degree `N>=4`, reducible `A_F`, and at least one
`mu=1` affine-image dicritical.  Necessary cages are never read as witnesses.

No CAS was used.  The finite partition counts below were derived from the stated
cost and placement recurrences and cross-checked by an ephemeral integer
enumerator; it supplied no mathematical gate and created no file.  I did not
inspect `jc2-lean`, edit a charged input or canonical ledger, or create any file
other than this report.

The three local primary PDFs rehash to the custody values quoted by RN:
Orevkov `f80d4a...32db`, Zoladek `88d5a3...49ad`, and Chau
`8e70c5...1ce2`.  Palka's arXiv PDF was streamed and rehashed to
`644552...34fdd`.  I also streamed Hamm--Le, *Ann. ENS* 6 (1973),
DOI `10.24033/asens.1250`, SHA-256 `47a8c9...c596460`; its Theorem 0.2.1 is
the primary Zariski--Lefschetz source relevant to the generic-hyperplane
surjection.  No source file was retained.

## 2. General-`N` enumeration audit

The correct finite bookkeeping starts from RN:63-73.  For a nontrivial carrier
record the **carrier-level** triple

```text
(mu_l,s_l,K_l),       cost c_l=mu_l s_l+K_l >=2,
```

and record each trivial as `(1,1,0)` of cost one.  Choose a nonempty multiset of
nontrivial triples, put `T=N-1-sum c_l >=1`, and take an unlabeled set partition
of all carriers into component owners, with at least two blocks.  This is finite
for each fixed `N`: `mu_l s_l+K_l<=N-2`, the number of nontrivial carriers is at
most `floor((N-2)/2)`, and `T<=N-3`.  BUD, RC, SELF and LZ can then be checked
block by block.  This is a valid enumeration framework.

RN:438-456 is nevertheless false as an **iff** and its phrase “subject only to”
misses an existing gate.  If `s_l=1`, then `h_l` is an isomorphism.  If one such
carrier on `D_i` has zero correction, the pointwise jump law makes
`phi_l=eta_i o h_l` immersive, hence `eta_i` immersive; every other `s=1`
carrier on `D_i` must then also have zero correction.  Conversely, if `eta_i`
has a critical place, every degree-one carrier sees it and has positive
correction.  This is exactly the componentwise discipline already stated at
N5:261-274.  Consequences omitted by RN include:

- a trivial carrier cannot share a component with a positive-`K`, `s=1`
  carrier;
- zero and positive `K_l` cannot be mixed among degree-one carriers on one
  component;
- `[22^(1)]` with two degree-one `mu=2` carriers is impossible, and in the
  unramified `[22^(2)]` packet only `(K_1,K_2)=(1,1)`, not `(2,0)`, remains.

Thus a class needs the carrier triples, their owner partition, and the common
normalization critical places.  The component aggregate `(lambda_i,K_i)` in
RN:467-471 is not injective.  Already `[22^(2)]` merges the distinct formal cores
`{(2,1,2),(2,1,0)}` and `{(2,1,1),(2,1,1)}`; the first is killed by the preceding
gate.  From `N>=10`, a cycle type such as `mu^s` also fails to distinguish one
degree-`s` carrier from `s` degree-one carriers.

For a one-block branched core of weight `w`, with `T` indistinguishable trivials,
the advertised SELF/LZ placement count is

```text
sum_{x=0}^{min(T-1,floor(N/2)-w)} p_H(T-x),   H=floor(N/2),
```

where `x` trivials are placed on the marked branched block and `p_H(r)` counts
partitions of `r` into unbranched block sizes at most `H`.  The common-`eta` gate
additionally forces `x=0` when that all-`s=1` core has positive correction.  For
several branched blocks one marks them separately, applies the same compatibility
and SELF tests, then partitions the remaining trivials into unbranched blocks.
This recurrence explains and independently checks the residual counts in SS6.

There is a growing family under the **current** gates: for every `N`, the cores
`[2^(k)]`, `0<=k<=N-4`, with all trivials on separate unbranched components pass
the displayed profile inequalities.  That proves only that RN's present formal
list grows with `N`.  It does not prove the universal meta-claim that no additional
numeric or minimal-gauge theorem could reduce it to finitely many types.

## 3. Gate-consumption audit

| item | hostile verdict | reason |
|---|---|---|
| `COST/BUD`, `LOC`, `IND` (RN:53-105) | **PASS** | They are direct sums of promoted Lemmas A/B and the local multiplicity identity; no attainment is used. |
| Proposition RC (RN:107-141) | **PASS** | The other `m-1` owners cost at least one; a branched owner costs at least two; `mu=1` has `corr=0,s=1`.  The inequalities follow in the printed directions. |
| NL, EMB, SELF (RN:143-180) | **PASS, with SELF strengthened** | Chau gives the common leading exponents; Palka supplies rectification.  One zero-correction degree-one carrier, not merely “all carriers,” already forces common `eta_i` immersive. |
| Lemma D / TRANS-LOC (RN:188-217) | **PASS as a necessary topological decomposition** | Affine inverse points and the points of the finite quotient fibre give invariant connected local covering components.  Distinct normalization branches have disjoint clusters.  This does not identify a quotient-singular point with a smooth resolved point. |
| LZ-KILL (RN:219-236) | **PASS** | For `b=1`, `2W>N` forces injectivity; Lin--Zaidenberg gives a weighted-homogeneous contractible curve, whose local complement generates the global complement; TRANS-LOC contradicts transitivity. |
| `CUSP-2` (RN:243-276) | **CONDITIONAL ONLY** | The coefficient calculation is sound if the source germ is finite and smooth and `J=y^(mu-1)` times a unit.  Those hypotheses are not proved for every correction point. |
| `NO-RAM-2` and cusp dictionary (RN:278-298) | **OPEN / NOT PROVED** | They apply conditional CUSP-2 to an arbitrary ramification point, which may be the contracted-bamboo attachment. |
| `TG-N` total identity (RN:302-320) | **PASS with connected generic-section hypothesis explicit** | The Euler/Riemann--Hurwitz calculation is correct.  RN itself leaves the global generic-line surjection OPEN at RN:568-571; Hamm--Le is the right primary source, but RN did not bind the exact affine reduction. |
| `DEG-PER` (RN:322-329) | **FAIL at stated scope** | `H_i` is normally generated by the `D_i` meridians; the `d_i` generic-line images need not ordinarily generate it.  The total TG floor remains; the per-component floor is safe for `b=1`. |
| monodromy pins (RN:360-390) | **PARTIAL** | Nonabelian image is sound.  “Any transposition” implies `S_N` only with primitivity, or when all nonidentity component meridians are transpositions.  The resolvent conclusion is consequently restricted to independently established `S_N` cases. |

Accordingly, CAGE-N items 1-3 pass as necessary structure; item 4 retains SELF
and LZ but loses NO-RAM and its threshold; item 5 fails at universal scope; item 6
retains transitivity, nonabelianity and the cycle dictionary but loses the general
`S_N` pin; and item 7 retains conditional TG and the orbit lemma only in their
corrected forms.  The conjunction called `THEOREM CAGE-N` is therefore false even
though several of its clauses are promotable separately.

The analytic scope failure is concrete, not a custody technicality.  Orevkov's
construction contracts each `L_C` chain to a point.  His Lemma 5.2 explicitly
treats both smooth points and the resulting singular points of the quotient source;
RN instead chooses holomorphic surface coordinates at every `t` and asserts that
any zero of the residual Jacobian would give a critical curve off `l`
(RN:243-248).  At the attachment point another boundary divisor is present before
contraction, and after contraction there is no smooth two-coordinate source germ.
The calculation therefore proves:

> **Corrected CUSP-2.** At a correction point away from contracted boundary
> attachments, if the finite resolved germ has critical divisor exactly `l` with
> residual unit, a `mu=2` critical parametrized branch has `e=1` and reduced germ
> `(nu,nu+1)` with `k=nu-1`.

It does not show that every finite ramification point of `h_l` is of this kind.
Orevkov Lemma 5.2 by itself gives equality of multiplicities implies a nonsingular
branch, not the converse used at RN:280-282; the stronger pointwise derivative
equivalence quoted from Zoladek supplies criticality of the parametrization but
still does not supply RN's smooth-source/unit-Jacobian hypotheses.  Consequently
the correction pin for the promoted `N=5` S1 cage, the exclusion of `(2,9)`, and
the claim “no ramified carrier below `N=10`” all revert to typed OPEN.

The group defect also has an exact small-degree model.  On four two-letter blocks,
`G=S_2 wr S_4` is generated by conjugates of `(12)` and the adjacent block swaps
`(13)(24)`, `(35)(46)`, `(57)(68)`.  It is transitive, proper and imprimitive, and
has precisely the abstract meridian types `[2]` and `[22]` occurring in RN's live
`N=8` class `[2+22]`.  Hence neither the `S_8` conclusion nor the asserted absence
of a useful proper quotient follows for that class.

Finally, primitivity alone does not repair the printed proof of `DEG-PER`.
A nontrivial normal subgroup of a primitive group is transitive, but a transitive
normal closure can be normally generated by one low-index element.  Connectivity
bounds apply to an ordinary generating tuple, not to normal generators.  For
`b=1`, all other component meridians are trivial, so the `d_i` generic-line images
do generate the global transitive image and `d_i iota_i>=N-1` is valid.  No such
argument is present for `b>=2`.

## 4. `NO-DEG-CAP`: theorem, proof, and exact scope

There is a proof here, but of a narrower conditional statement.  Let
`K_N` be the hypothetical RED-N counterexample class.  The safe formulation is

```text
for every F in K_N and every B, some T in Aut(C^2) has deg A_(T o F)>B.
```

RN:337-340 omits one needed sentence.  Choose a linear target coordinate `x`
nonconstant on at least one component (a component on which `x` is constant is a
line, already excluded by NL).  For a normalization parametrization
`(x(t),y(t))`, the shear `T_k(x,y)=(x,y+x^k)` has second-coordinate pole order
`k deg x(t)` for all sufficiently large `k`, with no cancellation against the
fixed `y(t)`.  Hence that component, and therefore `A_(T_k o F)`, has unbounded
raw degree.  This repairs the orbit lemma.

It follows that

```text
K_N nonempty  =>  sup{deg A_F : F in K_N}=infinity,
```

or equivalently that any universal raw-coordinate cap would imply `K_N` empty.
It does **not** prove that no cap theorem exists: if the Keller counterexample
class is empty, every cap is vacuously true.  Thus RN:342-344 and 547-549 commit a
quantifier error by declaring N5 DQ-3 refuted/closed negative.  A proved cap would
still close that lane--indeed all counterexample lanes--by contradiction.  The
useful campaign conclusion is instead that a nonvacuous within-cage degree bound
must be stated in an automorphism-normalized gauge such as `d_min`.

The claims at RN:346-356 go further and are false.  A target automorphism is an
isomorphism of affine curves: it preserves normalization, affine singular points
and their analytic types; geometric genus remains zero.  It changes projective
degree and the singularity data at infinity, which compensate in the genus
formula.  Raw-degree unboundedness therefore does not imply that “genera and
singularity counts are all unbounded,” nor that no inequality using
degree/genus/delta data can close a class.  The common-`eta` compatibility gate in
SS2 is already a finite counterexample to the alleged exhaustion of the numerical
layer.  `NO-DEG-CAP` is a proved conditional gauge observation, not an
impossibility theorem about future gates or survivor classifications.

## 5. Survivor-shape and class decomposition

RN's “core plus trivial distribution” is a useful **one-way necessary
parametrization**, after adding the common-`eta` rule.  It is not a classification
by the displayed class label.  Four independent typing failures prevent one OPEN
question per `[lambda_i^(k_i)]` from deciding the carrier profiles.

First, `lambda_i` records only moved cycles.  If `r` trivial carriers lie on its
component, `a_i=N-W_i` counts affine fixed sheets but omits the `r` fixed boundary
clusters.  The meridian's permutation type is

```text
lambda_i * 1^(N-|lambda_i|),
```

not `lambda_i * 1^(a_i)` as RN:503-504 states.  As printed, some permutations do
not even have degree `N`; this also explains why placements with different `a_i`
cannot be encoded by that OPEN.

Second, the cusp clause RN:499-502 applies the `mu=2` calculation to every
correction.  `[3^(1)]` at `N=6` is already a counterexample to the scope; the
`mu=3,4` correction germs in the `N=7,8` rows are explicitly left OPEN by
RN:560-563.  A negative answer to RN's artificially narrow ordinary-cusp question
would not kill the true `mu>=3` class.

Third, component-total `K_i` is not a physical singularity weight.  If two
degree-one carriers own the same component, they see the same critical
normalization places.  Even granting RN's global `mu=2` cusp dictionary for an
internal consistency test, two `(2,1,1)` carriers in `[22^(2)]` see the **same**
ordinary cusp of curve weight one; summing carrier corrections gives `K_i=2`.
RN's demand `sum(nu-1)=k_i` double-charges one physical place.  Without the
unproved global dictionary the germ is simply OPEN, but the carrier/place
conflation remains.

Fourth, the abstract curve question omits conditions asserted by CAGE-N itself:
the common Newton--Puiseux exponent pair and degree divisibility, exclusion of a
smoothly embedded `A^1` (not merely a literal line), TRANS-LOC, the unbranched
component incidence needed to state LOC, and carrier-to-cluster decorations.
Its TG variables `g` and `Sigma_inf` are not defined from the abstract
representation.  A positive answer is only a broad topological possibility, not
a profile witness; for corrected `mu>=3` rows even a negative answer is aimed at
the wrong hypothesis class.

The safe successor is therefore

```text
OPEN[PI1-S_N-CAGE(carriers, owners, places)]
```

with every `(mu,s,K)` retained; degree-one carriers coupled through their common
normalization map; ramification points separated from contracted attachments;
each physical singular branch listed once; `mu>=3` germs unrestricted and typed
OPEN; total fixed exponent `N-|lambda|`; and unbranched owners retained for LOC
even though their meridians die in the global representation.  Several such
decorated questions may project to the same moved-cycle label.  Consequently the
claimed general survivor-shape classification and the `6/10/26` per-class OPEN
package are not promotable.

## 6. Degree-specific recomputation for `N <= 8`

There are three distinct counts; RN conflates them.

| `N` | sum of RN's printed `#` | marked placements under RN's advertised numeric gates, assuming all `s=1` | after common-`eta` compatibility, still assuming all `s=1` | sound discrete residual with `NO-RAM-2` reopened |
|---:|---:|---:|---:|---:|
| 6 | 13 | 14 | 13 | **13** |
| 7 | 28 | 31 | 27 | **27** |
| 8 | 90 | 104 | 82 | **91** |

The second column directly refutes RN:473-495.  To recover its header totals before
the missing common-`eta` gate, the changed entries are: `N=6 [2]:5`; `N=7
[2]:7, [2^(1)]:5, [2+2^(1)]:3`; and at `N=8`, `[2]:14,
[2^(1)]:10, [2^(2)]:6, [22^(2)]:2, [3]:8, [2+2]:8,
[2+2^(1)]:7, [2+2^(2)]:3, [2+3]:6`.  All other entries are as printed.
For example, `N=6 [2]` has five placements: put zero trivials on the marked
branched owner and partition three trivials as `3`, `2+1`, or `1+1+1`; or put one
there and partition the other two as `2` or `1+1`.  RN silently merges placements
when their *unmarked* `W` multisets coincide, contrary to its definition of `#` as
profiles.

Consuming the common-`eta` gate gives the following exact all-`s=1` counts:

```text
N=6: [2] 5, [2^(1)] 2, [2^(2)] 1, [3] 2, [3^(1)] 1,
     [2+2] 2.                                             total 13

N=7: [2] 7, [2^(1)] 3, [2^(2)] 2, [2^(3)] 1,
     [3] 3, [3^(1)] 2, [3^(2)] 1,
     [2+2] 4, [2+2^(1)] 2, [2+3] 2.                     total 27
```

No ramified carrier passes LZ below `N=8`, so these are also the sound discrete
residuals at `N=6,7`.  At `N=8`, removing `NO-RAM-2` adds nine profiles.  Six have
one carrier `(mu,s,K)=(2,2,k)`, `k=0,1,2`, and respectively `3,2,1` trivials
partitioned among unbranched owners.  Three have separate branched owners
`(2,2,0)` and `(2,1,0)` plus one trivial, placed on either marked owner or on a new
unbranched owner.  They satisfy BUD, RC, SELF and LZ (`W=4`, with equality in the
one-branched case).  The ramification must be supported at a contracted attachment
to evade corrected CUSP-2, but RN has no gate excluding that typed OPEN case.

The resulting `N=8` moved-type projection is:

```text
b=1: [2]14, [2^(1)]5, [2^(2)]3, [2^(3)]2, [2^(4)]1,
     [22]6, [22^(1)]2, [22^(2)]2,
     [3]8, [3^(1)]3, [3^(2)]2, [3^(3)]1,
     [4]3, [4^(1)]2, [4^(2)]1.                           subtotal 55
b=2: [2+2]8, [2+2^(1)]4, [2+2^(2)]2,
     [2^(1)+2^(1)]1, [2+22]5,
     [2+3]6, [2+3^(1)]2, [2^(1)+3]2,
     [3+3]2, [2+4]2.                                     subtotal 34
b=3: [2+2+2]2.                                            total 91
```

These are profile counts after the sound discrete gates, not witnesses and not a
claim that TG or the PI1 questions are attained.  They project to 26 coarse moved
types but **29 carrier-level cores**: `[22]`, `[22^(2)]`, and `[2+22]` each have
distinct ramified/unramified carrier realizations (while `[22^(1)]` survives only
in its ramified realization).  This is why a moved-cycle “class count” is not a
survivor-shape classification.

## 7. Recovery of the promoted `N=4` and `N=5` cages

**`N=4`: coarse control passes, exact-instance claim fails.**  BUD leaves the
unique carrier packet `(2,1,0)+(1,1,0)` with separate owners, hence one `[2]`
profile and `W=(2,1)`.  This correctly recovers the dicritical/ownership
projection used by the earlier lane.  It does not recover the full promoted
`N=4` cage: C6:65-73 still records six AM-numerical types, narrowed shape-family
residuals and PI1 strata.  RN's one core row contains none of those refinements,
and its TG degree statement was itself left custody-OPEN.

**`N=5`: the profile/incidence control passes, the promoted cage does not reappear
verbatim.**  Exact enumeration gives three ownership profiles in two coarse
classes:

```text
[2^(1)] : P1 = S1;
[2]     : P3a and P3b = S2;
```

with P2 and P3c killed by the sound `W=3` embedding/LZ gate.  This agrees with
REV:68-76 and confirms that no coarse survivor was lost or added.  But RN then
replaces promoted S1's typed correction question by the unproved global ordinary
`(2,3)` pin.  It also fails to incorporate C6:52-58: the promoted
`S5-COPRIME-KILL` has already removed S2's coprime stratum and `(6,4)` slice and
left narrower row-pin questions, while S1 retains its correction and infinity-word
OPENs.  Therefore RN recovers the `N=4,5` **budget profiles**, not the promoted
cages “as instances.”

## 8. FALLACY-v2 guardrail audit

**FAIL before promotion.**  The decisive failure is flag/place/series separation.
RN:243-282 moves from a point `t` on the resolved dicritical to a smooth finite
surface germ without excluding that `pi(t)` is the singular quotient point made
by contracting an `L_C` chain.  Those are different objects with different local
rings.  RN:497-505 then sums carrier corrections into `k_i` and reads that sum as
physical cusp weight; repeated carriers can charge the same normalization place,
so this counts one physical branch more than once.

Carrier/attainment is otherwise mostly respected--the listed packets are called
necessary--but “survives iff” upgrades incomplete bookkeeping into an exhaustive
cage without the common-`eta`, PI1 or curve-existence data.  Floor/attainment is
handled correctly for BUD, RC and the total TG inequality; `DEG-PER` fails for the
different reason that normal generation is not ordinary generation.  The raw
degree discussion correctly notices gauge dependence but then makes the invalid
quantifier jump audited in SS4.  The target linear changes and shears preserve the
Keller property and geometric degree; the repaired shear argument explicitly
checks the nonconstant coordinate and cancellation.

Pole/interior, `sat()`, raw quotient remainders, prime-label/derivative,
merge-free descent, and target/arrival indices are not used.  No exit price is
asserted in this report.

## 9. Promotion recommendation and required repairs

**Promote as corrected fragments:**

- Lemmas A/B and `COST/BUD`, `LOC`, `IND`, and Proposition RC at their necessary
  scopes.
- Lemma NL, EMB, and SELF, strengthened by the componentwise rule: one
  zero-correction degree-one carrier forces every degree-one carrier on that
  component to have zero correction.
- Lemma D, TRANS-LOC, and LZ-KILL, preserving quotient-fibre points and resolved
  points as distinct.
- corrected CUSP-2 only at a smooth finite resolved germ with no other critical
  boundary divisor and unit residual Jacobian.
- TG-N as an identity conditional on connected generic section; retain only the
  total floor unless `b=1` or an ordinary per-component generating theorem is
  supplied.
- target-automorphism orbit unboundedness of raw degree, conditional on a
  hypothetical counterexample, and the carrier/set-partition framework as a
  one-way finite enumeration at each `N`.
- `G=S_N` when all nonidentity component meridians are actual transpositions, or
  when primitivity plus a transposition has independently been proved.

**Do not promote:** `THEOREM CAGE-N` as a unit; universal CUSP-2/NO-RAM-2; the
`N=10` threshold; per-component `DEG-PER` for `b>=2`; any-transposition
`=>S_N`; the all-`N` no-resolvent statement outside independently pinned `S_N`
classes; closure of N5 DQ-3 as negative; “numeric layer exhausted”; survivor-shape
“iff”; any printed `N<=8` count; the `6/10/26` class claim; or the present
`OPEN[PI1-S_N-CAGE(class)]` formulations.

Required successor work is sharply typed: analyze `mu=2` at contracted bamboo
attachments; rerun the carrier/owner census with common-normalization critical
supports; formulate PI1 questions with carrier/place decorations and unrestricted
`mu>=3` germs; and seek a real ordinary-generation or block-system theorem for
`b>=2`.  Until then the proper lane status is

```text
OPEN[RED-N-CAGE/CORRECTED-CARRIERS+CONTRACTED-RAMIFICATION+PI1].
```

## 10. References checked

1. S. Yu. Orevkov, “On Three-Sheeted Polynomial Mappings of `C^2`,” *Math.
   USSR-Izv.* 29 (1987), especially Lemmas 2.1, 3.1, 4.2 and 5.2, local PDF
   SHA-256 `f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db`.
   Lemma 5.2 expressly treats the quotient singularities made by contracting
   `L_C`; this is the source of the CUSP-2 scope objection.
2. H. Zoladek, “The Jacobian Conjecture,” *Topology* 47 (2008), Proposition
   6.5(b), local PDF SHA-256
   `88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad`.
3. Nguyen Van Chau, “Non-proper value set and the Jacobian condition,”
   arXiv:math/0305088v1, Theorem 1 and Corollaries 1-2, local PDF SHA-256
   `8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f`.
4. K. Palka, “A New Proof of the Theorems of Lin--Zaidenberg and
   Abhyankar--Moh--Suzuki,” arXiv:1405.5391v2, Theorems A-B, streamed SHA-256
   `644552cf8d543868f44d6fdf40420c2885e6d0e4255e18c03fe0af8980d34fdd`.
5. H. A. Hamm and Le Dung Trang, “Un theoreme de Zariski du type de
   Lefschetz,” *Ann. Sci. ENS* 6 (1973), Theorem 0.2.1, DOI
   `10.24033/asens.1250`, streamed SHA-256
   `47a8c9077d0af4ddfc9a0c391d66620e1c70b88c2391af507fc8ea831c596460`.

<!-- BODY-END -->
