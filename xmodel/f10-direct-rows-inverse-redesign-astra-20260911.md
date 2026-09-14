# Direct rows: inverse-chart representation redesign

STATIC mathematical redesign / UNREVIEWED; no implementation or execution authority.

Actual first action 2026-09-11 05:11:02 UTC. Fixed reserve 05:30 and hard stop 05:33. Targets initially absent. ROOT's terminal producer observation is attributed, not independently replayed.

## Diagnosis

ROOT reports a terminal NORMAL_EXIT1 after 218.021168898 wall seconds, no signal/resource termination, with producer path 382→361→274 and arithmetic add204→bounded169 raising `ValueError('STOP_INTERNAL_TERM_CAP')`. Reported stderr SHA256 is `b6a24cb04793c5f499464112f397229732072cfc16be4363f1407d40e684858b`. This is ROOT's observation after terminal custody, not independently replayed evidence. No baseline, positive checker, mutator or semantic negative completed. It establishes an intentional internal-storage refusal, not a mathematical contradiction or a measured operating-system memory requirement.

Static source agrees with that diagnosis: producer builds each entire inverse in one seven-exponent dictionary, adding every expanded `chartS**i * q**(-j)`. `bounded` rejects dictionary length above 100000. The checker likewise accumulates `inverse_poly` for both sources and its separate arithmetic imposes the same 100000-term cap during sums/products. Its repeated-multiplication power differs from the producer's corrected binary power, but it does not remove aggregate materialization. The traceback does not identify which A/B iteration failed. The failed partial sum does not prove the FINAL inverse has more than 100000 terms: later exact cancellation is possible. Nor does arrival at this line prove that the later diagnostic partition or graph checks passed.

Recommendation: change ONLY the inverse stage's internal representation to a complete coefficient-block family, indexed by q, P and z, processing one output coefficient block at a time with bounded power/product scratch. Keep all other circuit nodes, diagnostics, graph outputs and tripwires. A proof below bounds every inverse-stage polynomial accumulator by 3234 terms for A and 14490 for B, including transient partial sums. These are conservative structural counts, not measured sizes or runtime forecasts.

## Exact replacement contract

Let R be any commutative coefficient ring; in the registered numerical client R=k is its independently authenticated finite field. Set X=(X1,X2,X3,X4), weights (1,2,3,4). For F=Ahat use (D,J)=(10,3); for F=Bhat use (17,5). The accepted raw envelope uniquely writes

F=Σ f_{ijr}(X) S^i theta^j z^r,

over all fixed i,j,r≥0 with j≤J and i+3j+7r≤D, where f_{ijr} has X-weight D-i-3j-7r. Zero coefficient positions remain present conceptually. U has X-weight4 and is z,S,theta-free; z-freeness also follows from its nonnegative weight4 with wt(z)=7.

The inverse homomorphism σ fixes R[X,z], sends theta to q^-1 and sends S to q(U-zq+Pq²). It lands in R[X,z,P,q,q^-1]. No coefficient parameter or U is inverted. Give P weight10 and q weight−3; σ preserves the raw total weight. For each n,a,t define the complete block

I_F(n,a,t)=[q^n P^a z^t]σ(F) ∈ R[X].

An explicit coefficient contract is

I_F(n,a,t)=Σ_(i,j) (-1)^b multinomial(i;a,b,c) f_(i,j,t-b)(X) U^c,

where b=n+j-i-2a, c=i-a-b=2i+a-n-j. A summand exists exactly when a,b,c,t-b≥0, a+b+c=i and i+3j+7(t-b)≤D. Every other summand is structurally zero, not omitted because of its value. The sum uses the full fixed raw i,j range. The multinomial is an INTEGER, formed in Z then mapped to R; no factorial division in k and no new excluded prime are licensed.

Proof: choose a factors Pq³, b factors −zq² and c factors Uq from the i copies of σ(S). The q exponent is 3a+2b+c−j=i+2a+b−j, and the final z exponent is t=r+b. This is the polynomial multinomial theorem before any specialization, valid with nilpotents and in every characteristic. Thus every coefficient is recovered exactly and every permitted zero/cancellation survives.

The retained inverse records are the distinct indexed objects

σ(Ahat)=Σ_(n=-3..30,a=0..10,t=0..10) I_A(n,a,t) P^a z^t q^n,

σ(Bhat)=Σ_(n=-5..51,a=0..17,t=0..17) I_B(n,a,t) P^a z^t q^n.

They retain 34 and57 q-coefficient positions, respectively; splitting a q coefficient into P,z blocks is not shrinking that position. Separate pole views retain precisely n<0, namely all three A and five B negative-q positions. A zero block is a legitimate exact value; a missing block/evaluation is not. Neither pole view is required to vanish by the alternative-object acceptance contract.

The object can be backed by immutable source coefficient blocks, the independently reconstructed U, fixed index tables and a total coefficient evaluator. Every structurally admissible block must be evaluated before success; blocks proved impossible by index/weight inequalities are exact predefined zeros. After evaluation a block may be released and reconstructed from that backing data. The retained object is NOT just a hash, Boolean polynomiality claim, or an unbound formula string. No expanded union dictionary is built, and both source labels and both pole views persist.

## Bounds, partial accumulators and independent contraction

For a contributing summand with r=t-b, its X-weight is

w=D-i-3j-7r+4c = D+3n-10a-7t ≤ D+3i-3j-7r ≤4D.

It is nonnegative. All summands of a fixed block have exactly this SAME w; hence every partial sum, including uncancelled transients, is homogeneous of weight w and has no greater support bound. Each partial polynomial product f_{ijr}U^c also has that weight; its individual monomial products do too. U^c, c≤D, has weight4c≤4D. Form its powers in ascending order or otherwise forbid unused powers beyond D; the original powerfix principle remains relevant.

For a four-variable homogeneous polynomial of weight w≤68, choices of exponents e2,e3,e4 determine e1 uniquely if nonnegative. Therefore its support is at most (floor(68/2)+1)(floor(68/3)+1)(floor(68/4)+1)=35·23·18=14490. For A replace68 by40 to obtain21·14·11=3234. These bounds apply to multiplication accumulators as well as completed products and block sums. Multiplication by z^b or P^a is external index movement, never a new aggregate polynomial. Integer multinomial scalar arithmetic does not introduce X terms.

Off-window handling is structural, not truncate-and-hope: every monomial has i−j≤n≤3i−j, so −J≤n≤3D; also a≤i≤D and t=r+b≤r+i≤D. The stronger per-summand inequalities and w≥0 must be checked. A malformed input violating its raw envelope STOPs BEFORE inversion; it is never silently projected into these bounds. X exponents≤68, z/P exponents≤17 and q exponents between−5 and51 are all strictly within the inherited absolute256 cap. Only q is signed in this type. For negative q, w≤D−3, giving even smaller pole blocks (at most weight7 for A and14 for B), without assuming polynomiality or reducing their inventory.

Independent checker option: compute signed integer coefficients κ_i(a,b) from κ_0(0,0)=1 and

κ_i(a,b)=κ_(i−1)(a,b)−κ_(i−1)(a,b−1)+κ_(i−1)(a−1,b),

with out-of-range entries0. Induction on multiplication by u−zq+Pq² gives coefficient κ_i(a,b)u^(i−a−b)P^a z^b q^(2a+b); the outer q^i and theta shift recover n=i+2a+b−j. This additive recurrence is independent of producer multinomial evaluation, has no modular division, and gives the same coefficient contraction only after the checker reconstructs its OWN f and U. Its existing separate field arithmetic, coefficient-pair band/Euler reconstruction and graph Horner remain independent.

A concrete bounded scheduling option is one output block at a time, traversing c=0..D and forming U^c in ascending order; process all admissible (i,j) having that c before advancing. Cap the new inverse workspace at six derived X-polynomial buffers, including extracted source block, current/next power, product, and old/new accumulator. Free temporaries before advancing. Each is subject to the block weight/type and100000-term checks; together their structural upper bound is six times14490=86940 stored terms for B (19404 for A), excluding immutable pre-existing circuit inputs. All κ_i(a,b), i≤17, fit a fixed1140-entry triangular scalar table. This is a mathematical scheduling/buffer contract, not a measured Python allocation bound; an implementation must enforce it explicitly and must not retain all completed blocks or powers. Recomputing powers for the next block trades time for this bounded workspace.

## Coverage, controls and next discriminator

All unchanged finite-circuit operations remain mandatory: the literal septic/place and exact field checks; all125 named rational denominators and15 scalar inverse nodes; finite series/integration with their fixed index ranges; six completed matrix maps/two-sided inverse products; full formal-band recursion and mixed forcing, including critical z−U*d0, gap8 fixed U²theta³ and target−U²theta5, gap10 variation; fixed installation/discards; separate all-index Euler construction and its two fixed resonance gauges; full derivatives/products and all108 Jacobian positions,45 low copies,63 upper coefficients and22 readbacks. No Euler-extracted bands feed the formal recurrence.

The complete diagnostic partition is preserved, not inferred from output equality:

| Canonical-zero records | Count |
|---|---:|
| upper h1..6 particular/basis0..2; upper7 particular/variation |24+2|
| early h1..6 residual/rho; middle h5,6 U2/V4 |12+4|
| install(5,2),(6,2); Euler-band0..7 |2+8|
| low-band0..7, both rows; upper-J weight≤7 |16+41|
| both auxiliary negative-S records |2|

These total111 and still STOP on nonzero residue. The39 retained alternative records are upper8..10 particular/variation6; Euler resonances2; Euler-band8..10 three; low-band8..10 six; upper-J weight≥8 twenty-two. Their possible nonzero values remain computed, not added as graph generators. The two pole views are ADDITIONAL to150 labels and may be nonzero. In particular, streaming only poles would not implement the full inverse stage.

The Laurent-S auxiliary definitions and the SEPARATE scale boundary are unchanged: z=s², theta=s*t, scale factors s^-3/s^-5 for A/B, and original d,v,k,u,ell definitions. Preserve all13 scale fields and all six comparison groups, including every21/24 low-array DIFFERENCE and the leading guard product. Raw low source coefficients are not themselves required zero. Preserve omega=W*t5*s^8, graph guard g=Hq*ell and zeta*ell=−c^-1*g; do not set s=1, z=1 or substitute zeta into the inverse stage. No mate/source guard or canonical ordinaryness hypothesis is removed.

Success may be emitted only after each implementation has completed its own circuit and passed its own unchanged partition. The graph is still computed/checked literally: Hq,c,c^-1,zeta; slots K8,K9,K10, A1_1..A1_9, A0_1..A0_12, T; ell,g,U. Slot weights stay8,9,10;19..11;22..11;27, and Hq/zeta7,ell23,g30,U4. The mixed T=(zP1_0−U P0_0)(zeta) is retained before graph substitution. All30 polynomial positions/two scalars, zero/duplicate slots, strict rows-only bytes and individually named T comparison remain. The new inverse representation is not fed into their formulas, so its exact extensional equivalence leaves every displayed value unchanged; agreement alone still does not replace internal checks. This does not reorder unrelated acceptance stages.

**Guard-contract change, explicitly prospective:** the old100000 guard bounds a MATERIALIZED dictionary, not a proved global source-support hypothesis. A new inverse-block type must enforce fixed indices, exact block weight/type, per-block term/exponent ceilings and a separately bounded cache; existing raw/band/auxiliary/scale/graph guards and external runtime/wire caps remain. It must NOT be described as unchanged whole-inverse support enforcement. If ROOT instead wants a100000 ceiling on FINAL semantic inverse support, streaming can count the exact nonzero terms across disjoint blocks and STOP at100001 without materializing them; whether that stricter policy succeeds is unknown. This design does not raise100000 to another number or guarantee the old aggregate-workspace acceptance event.

The blocks prove elimination of THIS aggregate-dictionary failure mode. They do not prove the remaining stages fit time/memory/wire limits; scalar bit sizes, total products, recomputation/cache overhead and later graph/scale costs remain unmeasured. No wall-time forecast, new source pin, cap change, registration or run is supplied.

Manual changed-object controls: the homogeneous A-envelope toy F=X1*theta³ must retain pole X1*q^-3; dropping negative positions fails exact reconstruction although poles need not vanish. F=X1^6*S*theta must map to X1^6*(U−zq+Pq²); omitting the theta shift or changing the z sign fails specific coefficients. At U=0 the universal formula still works with U^0=1, so a proposed U inversion or division-based multinomial evaluator is an unjustified restriction. These are inert algebraic controls, not generated fixtures or observed executions. The future authenticated T+X1^27 semantic control remains necessary and unchanged; inverse storage success earns no T or rank credit.

## Simpler logical route and smallest next discriminator

A still smaller exact symbolic representation is the factored composition σ(F) itself, with its fixed coefficient/pole operators: its equality is a universal substitution identity and it is not an ordinary-source existence claim. But a descriptor-only implementation that never evaluates stipulated inverse coefficients would NOT meet the currently accepted whole-circuit computation obligation. Adopting such proof-backed laziness would be a separately reviewed contract change. It is not silently substituted here for the full block traversal.

There is also a NEW-instrument dependency lemma, distinct from current-contract compliance. In the pinned producer, the completed `inverses` and `poles` lists have no later arithmetic consumer: their later uses are inventory lengths. In the checker, `inverse_maps` and `poles` likewise feed only their own length checks. Their construction has local Laurent-envelope/resource predicates, but there is no inverse-coefficient zero predicate. In particular SCALE's field named `A_inverse` is a DIFFERENT expression, origA minus its Laurent-S reconstruction; it does not consume these inverse maps and must stay. Neither do the denominator/scalar/matrix inverses share this removable role.

The actual graph dependency is leading constants → formal bands/Psi,U,E → fixed Ahat and separate Euler Bhat → J−Delta → P1/P0 → critical zeta →25 rows,ell,g,U. The inverse-chart branch leaves Ahat/Bhat/U/z for two derived Laurent records, then ends; it writes none of those upstream inputs or the scalar-unit/denominator registries. Its polynomial operations return fresh results rather than mutating source operands. This is visible in BOTH frozen source bodies, not assumed from a matching output or from the failure traceback.

The incoming accepted implication is exactly charged wire-FIRST section A: 23z attaches these25 alternative rows F'_j to the kernel of B[X]→the canonical LOCALIZED source algebra A and sends g' to its unit g; 19z transfers a source-bound full weight30 rank certificate at a genuine place to B, giving g' in the row ideal and therefore A=0. It uses the same rows/guard, not numerical values of the alternative inverse/pole arrays. No unsaturated-ideal equality, source point or ordinary reconstruction is used. This paragraph composes that accepted scope; it does not re-review19z/23z.

Consequently, a separately reviewed NEW necessary-row instrument which deletes ONLY that inverse/pole branch and its local inventory/resource tests, but independently reconstructs the identical remaining graph expressions and retains every other place/source/diagnostic/scale/row predicate, preserves that FULL canonical-source EXCLUSION implication. Its graph equality is a syntactic dependency result over the symbolic coefficient ring, not inferred from one modular agreement. The q-envelope checks can additionally be discharged by the structural substitution bounds above. This is not a new current-contract acceptance: the accepted circuit explicitly requires computing the branch, so authoring, source attachment, status/contract binding and FIRST would all need an explicit transition. No old receipt or source authority can be reused silently.

Thus (a) the main coefficient-block design preserves the current entire mathematical circuit; (b) the smaller branch-free instrument is justified for the SAME necessary-row exclusion scope by this conditional dependency lemma, but would surrender its alternative inverse diagnostic/reconstruction service and is not currently licensed. Neither is an actual rank/source result. ROOT can select which contract to gate; no implementation or follow-on is authorized here.

OPEN quantity: does an independently implemented block evaluator cover every fixed inverse coefficient and preserve the complete current circuit/checker acceptance, within existing resource limits? CHEAPEST TEST: first a focused different-model STATIC check of the formula, transient support bound and explicit new type/cache contract; only after separate authoring and source/runtime approval, one newly registered complete evaluation and the existing T control. Runtime is UNMEASURED; no wall forecast. Stop on missing coefficient, type/weight/index disagreement, cap or any existing anomaly. Do not retry the old aggregate expansion or infer rank/source exclusion from storage progress.

## Scope and publication

Fourteen inputs were hash-pinned before fresh WHOLE reads: current COORDINATION, the five nominated final source files, ROOT-SOURCE-CONTRACT, four operation/assertion/wire/correction documents, and the rows proposal/FIRST/adopted wire pins. These last three resolve the current rows-only interface rather than inheriting obsolete full-trace wording. Exact pins are in PINS.json. The three optional new terminal files offered later by ROOT were NOT read; the observation above remains attributed. No linked provenance, coefficient/candidate/fixture body, protected repository or unrelated live lane was inspected. Exact AGENTS.md checks at /home/ubuntu and the workspace returned no file. A few combined displays clipped; the affected operations, arithmetic and wire gate were reread separately through EOF, and ASSERTIONS was separately reread as well.

Only this owned report transaction and same-tag documentary box may change. No source code, implementation, arithmetic execution, AST/import/syntax/test, network/AWS/SSH, worker control or delegation occurred. Prior authored checker involvement is disclosed; this is a redesign from its frozen current bytes, not an independent model promotion. Own WHOLE/postpins and own-only collision/OPEN checks precede the final marker; expected transaction verification and custody follow.

Closeout: own report and PINS received untruncated WHOLE readback by05:24:23 UTC; all14 inputs and the owned PINS hash were rechecked unchanged05:24:45. Own-only COLLISIONS: NONE; final report/manifest destinations were still absent. The raised quantity and cheapest static gate are explicit above; no new canonical OPEN identifier or corpus-wide collision claim is made. All scientific reasoning is now closed; only documentary transaction/custody and terminal readback remain, before the original05:30 reserve/05:33 hard stop.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19608`.
- Body SHA-256:
  `c98b49870c73fa5b1c57ff9d09a530b33d4ebf03f52486893c7e15752a17fc71`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
