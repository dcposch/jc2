# Significant-news full-spectrum packet — `20260828T1149Z`

Freeze time: 2026-08-28 11:49Z  
Coordinator: Sol Ultra  
Status: **SEALED SAME-INPUT BLIND ROUND**

## 0. Custody gate

Verify every hash below before reading the corresponding file.  Fail closed
and report only the mismatch if any value differs.  Canonical files will not
be mutated until the blind submissions have sealed.

```text
f5b16a545a1f2bac90e0aed50c2d86870ab9787b63197aa7a594f64687735bf4  APPROACHES.md
92220e1fee14f63c703cf24ee20b0b6679cc2db06c43aded9c1abd3ad9b6b581  AUDIT.md
3fc3c9d9e024d215040e7b389f3622a9ef1e5c640b848188bd4ff855c9bb35e6  COORDINATION.md
bd48c82ada1af5a16b31c70216a5e937fcc94f3e0e17d717c638b116eecb9a90  PROGRESS.md
eba9b04f1c851775e1d664cd27d1772263a837682c8bf2a694aad1fcad550c6f  notes.md
df6f019c7ca2d3172c25cf4c02a582159c4ee27f6f5a209ddd1280b8212b138b  ladder/REDUCTION.md
6d1c34d1484fc52d9971d9a91caf1ab2aed9f20b108b508c06d708eda25671fd  ladder/SIGRAY-AUDIT.md
0c0a94505684473f66488b9861b2a8434bb13956b2f1c964f7fd3a5a9b865b24  xmodel/ideation-20260828T0702Z-synthesis.md
```

The repository basis is HEAD
`418e413593120d19e15e6546eb50c985f4b1f038` plus the explicitly hashed dirty
artifacts.  Do not infer a clean worktree.  Never enter, list, search, read,
build, status, or modify the nested user-owned `jc2-lean` tree.

Load-bearing new reports and checkers:

```text
841c848eb98aa234fe6429006b3f84958c042869db395d61f2394a6c6c7c81d0  xmodel/g2-intrinsic-exact-pair-l3-l5-newton-puiseux-sol-ultra-20260828.md
5e8bc3c54007e9c471a8cb86b51929172c0b749156b1843c013c259d41ea70d9  xmodel/g2-intrinsic-exact-pair-l5-reduced-denominator-independent-review-sol-ultra-20260828.md
5d219c53cc800e81171f7237af730f05d865088e36171d222050ccdda5dff0ed  xmodel/g2-intrinsic-exact-pair-l3-l5-hostile-review-opus5-20260828-v1.md
26e24ec9667b2525efe20288db67aa8a7897038f8acb0f4f1a0549bb9d0f5154  cases/g2_intrinsic_exact_pair_l3_l5_opus5_review_20260828/verify.py
10bc55d53f9cf9a9e6a4535787f6e208a25f0ebfbd6dbd803f68b00f8ca8f5cd  xmodel/sigray-prop42-constant-shift-repair-sol-ultra-20260828.md
47f2b608f47bc7f426c6cf3e8634c8704bdd675aa909eb63e3f4c6861c21dfb1  xmodel/sigray-prop42-constant-shift-repair-hostile-review-opus5-20260828-r1.md
8396a44c5f81f011a8a343124bd0de21329d0f1756a99fcf4cc9df718baf3e14  cases/sigray_prop42_constant_shift_repair_20260828/verify_constant_shift.py
0775a496a0b2d174fe944a6caa0ab695155b0381cbf0b1c799c6a382ce8058bd  xmodel/ggv-upper-endpoint-deep-q1-lambda0-quadratic-q-generic-symbolic-sol-ultra-20260828.md
83ab6c75e60b0a54ef1d930787e0dfa87d77310a411e7239647faaaca05381e9  cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_quadratic_q_symbolic_20260828/verify_symbolic_quadratic_q_generic.py
c3f03f370eec64375af19dc684a17c52ee176b2aa1f6179cfedfa0c3a15cdb9a  xmodel/ggv-upper-endpoint-lambda-nonzero-unit-s-first-correction-sol-ultra-20260828.md
79076a9cf41f799218aa9075d219b79547991011b8038b379bd81b995ebf325c  xmodel/ggv-upper-endpoint-lambda-nonzero-unit-s-first-correction-independent-review-sol-ultra-20260828.md
874bcd98b21c19546db67e6dc4599aebd800259687c45ecc0780ab282119e92d  xmodel/ggv-upper-endpoint-lambda-nonzero-unit-s-order4-cancellation-sol-ultra-20260828.md
aa88f1904ac14f05cbac193dac12ef054ba3928306811a253abb840656fc7138  xmodel/ggv-upper-endpoint-lambda-nonzero-unit-s-order5-row-identity-sol-ultra-20260828.md
e03a5bec4278362e8941312115b7bb7bdd9a7b6dd3eee6b58d836e5dbeb55701  xmodel/websweep-20260828T0524Z.md
c5655b43144f5dcfdf218c2a4b7f4bc3687fd7cdaac1e555e346545f74de45fc  xmodel/downloaded-papers-first-look-fable5-20260828.md
```

## 1. Blindness and execution boundary

Read no peer `20260828T1149Z` response before sealing yours.  Do not read any
file whose name begins `xmodel/ideation-20260828T1149Z-` except this packet,
your assigned prompt, and your own assigned output.  Disclose accidental
contamination and fail closed if it can affect independence.

Do not touch AWS or running jobs.  Do not run Singular, msolve, Sage, Lean,
or heavy/uncertain local algebra.  Short read-only inspection, hashes, and
small standard-library exact checks are allowed.  Do not edit canonical files
or cases.  Your only write is the assigned
`xmodel/ideation-20260828T1149Z-<lane>.md`.  Print its SHA-256 and disclose the
exact model, files read, checks run, failed attempts, assumptions,
contamination, and scope.

## 2. Authoritative significant news

### 2.1 Intrinsic exact-pair L3/L4/L5 is now available

The different-model Opus review confirms, after repair, the exact
normalization--Kummer theorem.  For a normalized Sigray Lemma 2.1
rectangle/NE-corner fibre:

```text
L3-exact  all-root prefixes are actual fibre truncations             AVAILABLE
L4-exact  the intrinsic x/y charts cover every boundary place        AVAILABLE
L5-exact  certified terminal deck orbits biject normalized places    AVAILABLE
```

The exact law is `orbit size = reduced denominator = e_S` and `stabilizer
size = kappa/e_S`.  A terminal is the node-evaluable record

```text
(h, chart, kappa, strict truncation F),  deg p_{h,F}=1.
```

It continues uniquely by Hensel on the shifted, `t`-cleared equation.  Raw
cover order is `(kappa/e_S)` times place order.  Coverage is false for a
general reduced curve (`y-x^2` is the control), so the normalized-fibre
hypothesis is load-bearing.

This closes only the intrinsic exact-pair constructor.  Hybrid VGG/GGV
`H-TRUNC`, two-source-chart coverage, and uncertified source-leaf terminality
remain open/ill-typed.  Do not silently transfer the exact theorem to the
hybrid source lane.

### 2.2 Sigray Proposition 4.2 is now completely repaired

Opus confirms the positive-tree constant-shift theorem and finds the
producer's omitted downstream typing work.  At a fibre flag, `p_F` is
nonconstant.  For leading forms `xi^d p` and `xi^e q`, a vanishing bracket
`d p q'-e p' q` makes `e<0` impossible, `e=0` constant, and `e>0` the usual
positive-power case.  The zero case is uniquely

```text
(k,l,s)=(1,0,c),  h_next=h-c,
```

after which the leading order is negative, the next bracket is nonzero, and
the remaining defect is zero.  Its terminal degree is
`(mu-1)deg p_F+1` and must enter `M_F`.  The corner is `T_a^nearrow`, hence
absent from pole characteristic `T_a^searrow` paths.

The full erratum is mandatory: delete the circular p. 20 Remark, retain
condition (7), transport zero-order constants to parents by Fact A, exclude
them at the axes by Fact B, and cross-multiply the affected Proposition
6.2/6.3 ratios.  Merely replacing `N*` by `N` is incomplete.  Proposition
4.3, Proposition 5.1 at finite nonzero punctures, later source gaps, landing,
`RPMC(C)`, the type/cofinal ceiling, and JC2 are untouched.  The 72-item
source-audit census is now 21 verified, 33 verified-with-nit, 10 errata,
2 known errata, and 6 gaps.

### 2.3 GGV local algebra has compressed but not closed

On the lambda-zero even face

```text
A=X^4-1, Q=q0+q1 X+q2 X^2, S=U=0,
e=F8=F10=F12=F14=0, c2=1,
```

the complete q7--q15/G9/G11/G13/G15 odd receiver matrix is 106 by 105 and
has rank 105 over `Q(q0,q1,q2,c4,c6,c8)`.  Thus the odd fibre and origin
endpoint vanish on a nonempty open set.  Every survivor lies on the
unresolved maximal-minor/rank-drop variety.  This is a generic theorem, not
universal; G16--G21, four-root equations, released even tails and special
rank-drop loci remain outside it.

The arbitrary-Q ideal was deduplicated exactly from 169 presented rows to 17
equivalent generators.  Degree-7 sparse syzygy searches on 1,102/28,136 and
14,396/99,877 column/row systems returned no certificate in those bounded
ansatz spaces; this is not ideal nonmembership.  Several exact AWS
term-order/block-order/maximal-minor variants remain live.

On the lambda-nonzero unit-S branch the first correction is reviewed and is
regular through relative order three.  Provisional exact calculations show
that both possible order-four poles cancel by the reviewed D12 lifts, and the
sole order-five residue is the already reviewed D12 product
`J(20c2J+3N)`, hence also regular.  A different-model dependency review is
live.  Treat orders four/five as provisional.  Even if confirmed, they say
the isolated face expansion is repackaging the determinant cascade; route to
raw windows/endpoint or prove a general redundancy theorem instead of blindly
incrementing the face order.

The large lambda-one compiler and fixed-q1 raw solves produced strict timeout
NO_VERDICT packets, not mathematical evidence.  Do not rerun unchanged.

### 2.4 Compute and external state at the cutoff

All heavy algebra is AWS-only and every audited host has zero swap.  At
11:48Z four independent one-core arbitrary-Q variants were live under
1,800-second inner caps: G15-core block `std` on r6c (31.2 GiB RSS), full-core
block `slimgb` on r6b (5.10 GiB), reverse-variable full `slimgb` on r6a
(7.33 GiB), and full-endpoint msolve on r6d (8.77 GiB).  Shared exact source
archive SHA is `b2e67b16...`; all passed preflight/dedup and had no marker.
Three older one-core symbolic, symbolic-screen and maximal-minor/rank-drop
jobs were also live on zero-swap Box03 under 43,200-second caps; they had only
the 105-variable/106-equation or 106-by-105 matrix census, no basis/minor
marker.  Exact terminal markers and custody are required; timeout or absence
of a marker is no verdict.  HENS-CT passed its upstream exact adapter gate but
timed out before creative telescoping on the charged control and is stopped
pending a structural backend redesign.  The campaign may use up to 512 AWS
vCPU and launch additional instances of at most 1 TiB RAM, but fanout must be
mathematically nonduplicate and safety-gated.

The 05:24Z sweep found no external proof or counterexample.  Matysiak SSRN
7229358/7229458 are refuted on primary-text audit: the claimed JC2 proof
confuses injectivity with surjectivity and its dependency assumes the etale
form of JC and an invalid Druz kowski Jordan reduction.  Van Dobben de Bruyn
arXiv:2608.27341 supplies only a possible boundary-at-infinity bridge; its
naive plane symmetric-power descent fails.  Next broad sweep is due by
2026-08-29 05:24Z unless significant external news fires earlier.

## 3. Whole-campaign task

Think independently about the **entire** JC2 campaign, all 46 numbered
avenues, current gaps, software, and counterexample routes.  Read all of
`APPROACHES.md`, the current/top corrections of `AUDIT.md`, the current day
of `PROGRESS.md`, the newest live state and later events in `notes.md`, the
prior synthesis, and the exact new reports.  Victory may come from a new
avenue or a connection no prior round considered.  Agreement with this
packet is not a goal; attack its framing.

Answer these questions inside the whole-portfolio scan:

1. With intrinsic L3/L4/L5 and Proposition 4.2 removed from the gap list,
   what is the **first exact unproved implication** on the shortest pure-
   Sigray route to JC2?  Distinguish source audit, decoration, landing,
   `RPMC(C)`, type control and cofinality.  Determine whether Proposition
   5.1's finite-nonzero-puncture repair is truly critical-path or bypassable.
2. Can the terminal certificate `deg p_{h,F}=1`, the exact orbit law, and the
   corrected positive tower compose with Riemann--Hurwitz, conductor/delta,
   semigroup, proximity, Chau finite-end identities, or Sigray mass formulas
   to prove a new global bound?  Give a literal theorem interface or `NO HIT`.
3. Which source item should be repaired/audited next for maximum fanout:
   Proposition 5.1, the candidate Proposition 5.4 repair, Statement 6.2,
   Propositions 6.3--6.8, or Sections 7--9?  Identify the cheapest exact
   proof/refutation/bypass triad rather than voting by apparent proximity.
4. Is there a direct intrinsic exact-pair route to landing or `RPMC(C)` that
   bypasses the hybrid GGV source entirely?  Conversely, can any reviewed
   GGV endpoint fact now discharge a hypothesis of the pure tree route?
5. For the GGV finite lane, what is the fastest exact discriminator on the
   quadratic-Q rank-drop variety and on lambda-nonzero raw windows?  Prefer
   Fitting ideals, minors, saturation, symmetry, cokernels or dual
   certificates over another equivalent timeout.  State AWS targets and
   stop conditions.
6. Which counterexample/disproof avenue is under-resourced?  Seek a
   source-complete, all-depth, bounded-support family and a characteristic-
   zero algebraization/collision mechanism; do not mistake formal or modular
   survival for a counterexample.
7. Perform a theorem-interface composition pass across **all** avenues and
   propose at least one genuinely new mechanism.  Include software ideas:
   source-audit automation, exact Puiseux/tree compilation, proof-object
   extraction, distributed algebra, or a better CT/integrability backend.

## 4. Required submission contract

Your report must contain all of the following:

1. A compact disposition vector for every numbered avenue 1 through 46:
   `unchanged`, `raise`, `lower`, or `reopen`, with reasons for every change.
   Group unchanged entries compactly, but omit none and never merge `G2-PSC`
   with `G2-BD`.
2. A reranking of the three principal proof bottlenecks and two principal
   disproof/counterexample bottlenecks.
3. At least one genuinely new avenue or mechanism, compared explicitly with
   repository history, and at least one new connection between existing
   avenues.
4. The strongest proof attack and strongest counterexample/falsification
   attack to run next.
5. One software acceleration or decisive experiment, with exact target and
   verification gate.
6. No more than three detailed idea cards.  Each names exact dependencies and
   licensed assumptions, cheapest decisive discriminator, materially
   different outcomes, stop/rollback condition, estimated compute/review
   cost, and expected information gain.
7. `continue`, `redesign`, or `stop` for every major current lane, including
   pure Sigray/exact-pair, hybrid G2-PSC, arbitrary-Q/rank-drop GGV,
   lambda-nonzero/raw-window GGV, LF40, K00/order-two/TD6, D43,
   Artin--Schreier, HENS-CT and external intelligence.
8. One likely-missed insight and its cheapest test.
9. A full epistemic ledger: proved/promoted facts, provisional inputs,
   conjectures, failed approaches, hidden assumptions, checks and failed
   attempts, contamination, and exact scope.  A model verdict is not
   mathematical evidence.

Do not output a generic brainstorm.  Rank by expected information gain per
wall-clock hour and probability of resolving JC2, not ease.  Reasonable
provisional work may seed reversible descendants while review continues;
review still gates promotion, publication, irreversible action and expensive
fanout.
