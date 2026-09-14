# Adversarial cross exchange — 20260906T1435Z — Sol 5.6

## Evidence boundary and decision

I read the four immutable blind submissions whole, after reading and verifying
`collection.json`. The five packet/report SHA-256 values recompute to the
manifest values. The manifest says `body_read_before_collection=false`; all
three peer reports were sealed by 15:02:41Z, while collection resumed only at
21:24Z (`collection.json:3-14`). This is therefore a late cross exchange, not a
new blind scan, and the delay was coordinator collection latency rather than
peer completion latency.

I also read whole every charged source report used below, `FALLACY-v2.md`, and
`strinz-THEOREMS.md`; read all of `astra_diagonal.py` before writing/running my
own control; and inspected the relevant primary GGV definitions, Proposition
2.1, Lemma 2.2, Theorem 2.6 with proof, and Proposition 2.11 with proof, plus
GGHV Theorem 2.1 and Proposition 4.3. I inspected Roy's source-band, linear-row,
layer, and payload code, not its unrelated intermediate classification
routines. No live peer cross body/code/log/receipt, AWS/CAS, K7 output, remote,
public classifier execution, or `jc2-lean` was accessed.

**Decision:** CONFIRM Astra Card 2 only as a restricted published-theorem-tier
support lemma; do not cut a receiver or source without a licensed forced edge.
Use the normalized complete literal D125 exporter as the next CE discriminator
after root code review; defer further elimination expansion. JC2 remains open.

## Hostile gate: monomial-J Euler support

Let `l=k+1`, with `P,Q in K[gamma,pi]`, characteristic zero,
`[P,Q]=c gamma^k`, `c!=0`, and let `(rho,sigma)` be primitive with both entries
positive.

1. **GGV existence and transport — CONFIRMED at external-theorem tier.** Under
   `t=gamma^l`, `Pbar,Qbar in K[t^(1/l),pi] subset L^(l)` and
   `[Pbar,Qbar]=c/l`. The GGV direction is the primitive reduction of
   `(l*rho,sigma)`; Astra omitted this harmless gcd normalization. Positivity
   gives membership in `V_{>0}` and positive degree. Theorem 2.6 supplies the
   homogeneous Laurent Euler element and both endpoint alternatives
   (`core-ggv-layout.txt:22-24,128-141,192-194,364-392`). Pullback gives
   `[Fpull,R]=l gamma^k R`; hence `E=Fpull/l` satisfies
   `[E,R]=gamma^k R`, has original weight `l*rho+sigma`, and sends the
   exceptional `(1,1)` to `(l,1)`. The source theorem's proof imports its own
   `[8, Lemma 2.2]` (`core-ggv-layout.txt:376-381`), which I did not have;
   self-contained existence is therefore GAP, not claimed.

2. **Least-gamma pole removal — CONFIRMED, but redundant here.** If
   `ord_gamma(E)=u<0` and `ord_gamma(R)=s>=0`, with bottom coefficients
   `e(pi),r(pi)` and `deg r>0`, the unique coefficient at
   `gamma^(u+s-1)` in `[E,R]` is `u e r'-s e' r`. Its highest-pi coefficient is
   `lc(e)lc(r)(u deg(r)-s deg(e))`, strictly nonzero in characteristic zero,
   whereas `gamma^k R` starts at `s+k`. Astra's argument
   (`ideation-20260906T1435Z-astra.md:70-88`) is sound.

   There is a stronger repair at this exact object. Each endpoint of `Pbar` is
   coordinatewise nonnegative. An aligned endpoint of GGV's `F` is its
   corresponding `Pbar` endpoint multiplied by the positive scalar
   `(rho'+sigma')/v(Pbar)`; the alternative `(1,1)` is also nonnegative. Thus
   both endpoints, and the whole homogeneous support segment, have nonnegative
   t-exponent. The endpoint clauses alone put `F` in the positive Puiseux
   subring. The report's general warning that GGV permits Laurent poles remains
   true, but poles cannot occur for this positive-source/positive-direction
   specialization.

3. **Final nonmonomial slope exclusion — CONFIRMED exactly.** Suppose the face
   `R` is nonmonomial, `st(R)=(a,b)` with `a,b>0`, and
   `sigma>l*rho>0`. Its minimum-gamma endpoint has positive pi-degree. The
   preceding positivity (or Astra's pole lemma) makes `E` polynomial, and
   weight `l*rho+sigma<2*sigma` limits its pi-degree to 0 or 1. Any pi-degree-0
   term is `st(E)`, neither aligned with the mixed `st(R)` nor the transported
   exception `(l,1)`, contradicting Theorem 2.6(2). Hence
   `E=lambda gamma^l pi`. Every `(i,j)` in `Supp(R)` then satisfies both
   `lambda(lj-i)=1` and `rho*i+sigma*j=v(R)`; their determinant is nonzero, so
   all exponents coincide, contradicting nonmonomiality. This excludes only
   that face configuration. No supplied immutable receiver/K7 source report
   licenses such a forced face, so the receiver/source conclusion is **GAP**.

The strongest falsification controls remain the same-ring failure of an
ordinary Euler import, `P=gamma*pi,Q=gamma^2`
(`monomial-jacobian-euler-interface-astra-20260906.md:110-150`), and Astra's
changed object outside the steep cone (`ideation-20260906T1435Z-astra.md:88-90`).

## Fable weight-line claim

**REFUTED as written:** Fable says the weight-`(rho+sigma)` monomials of full
`L^(l)` with nonnegative pi exponent are finite and uses that to bound roots
(`ideation-20260906T1435Z-fable5.md:38-43,48-64,97`). But
`L^(l)=K[t^(1/l),t^(-1/l),pi]`; at `(1,1)`, every
`t^(2-b) pi^b`, `b>=0`, has weight 2. Thus the raw weight line gives no upper
pi-degree, and its stated counting proof—and any root cap derived from that
alone—fails.

The actual receiver-specific conclusion is repairable, not refuted: positive
source support plus both GGV endpoint alternatives force the Euler element into
the positive Puiseux subring. For `sigma>0`, its pi-degree is then at most
`floor((rho+sigma)/sigma)`; Proposition 2.11(1)'s separability/divisibility
statement (`core-ggv-layout.txt:420-470`) bounds distinct roots accordingly,
giving at most two at `(1,1)`. A forced face and a growing root lower bound are
still absent. No receiver nonexistence follows.

## D125: literal construction versus elimination

The post-cutoff source-contract and triangular-normalization confirmations
compose narrowly. The literal object retains the original supports
`706+1901`, all 189 jets, five pins, every ordinary coefficient of
`J(P,Q)-1/5`, and `Z*P_15_15*Q_25_25-1`; the guard preserves exact degrees
75/125 (`d125-source-contract-gate-fable5-20260906.md:36-55,80-87`). The
confirmed normalization specializes to `571+1551` source coordinates before
jets/pins and preserves those rows and the guard, but gives only
characteristic-zero field-point/nonemptiness equivalence (and, over Q, the
stated properness equivalence via Nullstellensatz)—not ideal equality, scheme
isomorphism, or mod-p equivalence
(`d125-triangular-normalization-gate-fable5-20260906.md:55-65`).

Roy's classifier is not that literal ideal: it hashes linear rows and
quadratic contribution descriptors and retains summaries/digests
(`roy-classify.py:203-378,4023-4069`). The exporter specification is the first
complete literal route: normalized mode has 2123 variables including `Z` and
3987 labelled rows including zero slots and the guard; original mode has
2608/4767. These are prospective bookkeeping counts, not measured artifacts
(`d125-physical-exporter-preflight-astra-20260906.md:41-49`).

Astra's terminal-face proposal adds two target gauges and proves a filtered
full-Q map has constant diagonal blocks; the source-preserving gauges leave the
terminal pins, Jacobian, and guarded degree endpoints unchanged
(`ideation-20260906T1435Z-astra.md:32-68`). Its algebraic injectivity mechanism
is credible at desk scope. It has not emitted a literal adapted basis, selected
minor/inverse, or every substituted remaining row, and it has not measured
coefficient fill or runtime. The reported maximum 6-by-5 block is not such a
measurement. Therefore: **CONFIRMED** source/gauge and associated-graded scope;
**GAP** complete elimination implementation and cost.

Normalization does not license reuse of Astra's unnormalized 1760-column
figure. A normalized adapted basis, column count, constant minor, inverse,
substitution into every residual row, and transformed guard would all have to
be literalized before comparison.

The physical exporter preflight instead specifies every original/normalized
variable, jet, pin, guard, and physical row, including zero rows
(`d125-physical-exporter-preflight-astra-20260906.md:17-49`). Its terminal
report/transaction/pins are accepted by the post-cutoff delta, but code root
review is pending and no production/import/solve occurred. Fable's proposed
D125 `q/sigma` case reduction remains **GAP**: its arithmetic is explicitly a
guess (`ideation-20260906T1435Z-fable5.md:66-78,97`), while primary GGHV
Theorem 2.1 covers `<125` and Proposition 4.3 only the `(8,28)` case
(`ggvh-2204.14178v1.txt:94-126,492-504`).

## Deduplicated ranking and at most two launches

1. **Proof card: licensed-edge Card 2 screen.** Dependency: an immutable,
   source-licensed forced nonmonomial face with its actual endpoints for one
   current receiver. Test the transported positivity, steep inequality, and
   root data. Outcome: a violation excludes that face/row only; otherwise bank
   the lemma as vacuous. **STOP** immediately if the edge is unforced or the
   mixed-start/positive-direction hypotheses fail. No inferred source cut.

2. **CE/software card: normalized complete-source export.** After root reviews
   the exporter code and issues explicit authority, run one capped construction
   plus strict full replay, retaining all 2122 source variables, `Z`, every jet,
   pin, physical row, and guard. No import or solver in this task. Outcome: a
   complete measured literal client, or an exact mismatch/cap profile.
   **STOP** on any omitted row/guard, footer/hash failure, cap, or source-map
   mismatch; do not expand Astra's elimination until this baseline exists.

Strongest proof attack is the repaired restricted GGV slope screen; strongest
CE attack is the guarded complete D125 source, not a carrier/receiver survivor.
These are distinct target/mechanism/object/tests, not model votes.

Major lanes: **CONTINUE** the licensed receiver-edge audit and untouched K7
`.73` jobs under the original caps/September 7 harvest; **REDESIGN** D125 around
code review and one literal baseline; **STOP** further D125 elimination for now,
Fable's guessed degree-125 reduction, the low-marginal D108 dependency shrink,
retired 99/D108 computation, and duplicate K16 square/finite-m work. No point,
unit, properness, global-125 theorem, or JC2 solution is asserted.

## Controls, systems, and unread dependencies

My stdlib exact script
`box/ideation-20260906T1435Z/cross-sol56-check.py` (SHA-256
`839bdb97548eeb95bb6911e79497bbb8403279aa584defbced860624c4499d12`)
was read before execution and uses explicit exceptions plus 25-CPU-second/
512-MiB self-caps. Normal and `-O` runs passed the twisted Euler positive case,
the inconsistent steep-face coefficients, changed monomial-J object, infinite
Laurent weight line, D125 counts/guard endpoints, pinned top bracket, and sign
mutation in 0.02/0.09 seconds. Output is retained at
`box/ideation-20260906T1435Z/cross-sol56-check.out` (SHA-256
`d630888faca006edca64808a0cb77ad4131b6436a6c96e63f4471539d2a28e03`).

**Systems: UPGRADE, procedural only; NO_CHANGE to ledger/launcher/adapter.** The
promised 15:25 collection and downstream deadlines (`packet.md:15-18`) missed
by roughly six hours although every peer was terminal. With no durable assistant
wake mechanism, launch a timed round only with a present collection owner and
an acknowledged handoff; otherwise describe collection as event-triggered, not
wall-clock guaranteed. Fable's checker-AST preflight does not address this miss.

Unread/unavailable dependencies: GGV's upstream `[8, Lemma 2.2]`; the actual
receiver/K7 forced-face artifacts and Moh proofs referenced but absent from
these snapshots; Fable's `[2]/[5]/[6]` D125-chain sources; Strinz Theorem A's
proof bundle; exporter source code and production artifacts; full GGV/GGHV
proofs outside the cited load-bearing text; Helali/Suzuki certificates; all live
K7/D125/cross state.

<!-- BODY-END -->
