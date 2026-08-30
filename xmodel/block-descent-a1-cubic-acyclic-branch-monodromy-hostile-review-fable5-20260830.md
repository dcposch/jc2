# Hostile review: acyclic branch obstruction to the proper cubic block

Date: 2026-08-30 UTC  
Reviewer: Fable 5, independent hostile reconstruction  
Reviewed producer: `xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-obstruction-sol56-20260830.md`  
Verdict: **CONFIRM_WITH_CORRECTIONS** — the obstruction theorem is correct and
closes the promoted proper-cubic branch row; two proof-articulation repairs
are required, neither of which changes the conclusion.

## 0. Custody and execution

All nine charged SHA-256 hashes were recomputed and matched the prompt
manifest exactly:

```text
5be2e2af32c0f6201637a652d28a0ff5f6992c5ebde696b1198d7b94e4829cf7  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-obstruction-sol56-20260830.md
5fd8b854452bf4e42a96ccaea89ca8b4be09310dc0cff424ae6dd0261392a455  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-obstruction-sol56-20260830.md.artifact.json
648022d35191b67d9f1e1eec61cddc95bbee745001410ad1fbbffa1044417389  ops/block_descent_a1_cubic_acyclic_branch_monodromy_replay.py
41245c20b1b61a0dcf8116340672d037b977e6759d5d99054fc06c292d5c36fc  refs/arzhantsev_zaidenberg_acyclic_curves_arxiv1110.3028v2.pdf
2e6d82035df6717d1a39f31dc19b23b7c727bb940d4730d2c7ea9400e5433cce  xmodel/block-descent-a1-cubic-affine-survivor-funnel-sol56-20260830.md
9e32b0fe8835b6ea6002036b95e2261a612754d73d796cb10edda347cf3cf65e  xmodel/block-descent-a1-cubic-affine-survivor-funnel-hostile-review-gpt55-20260830.md
8ccb92fd3676e9f8b58e3ace4eb9157d0fa290ea24abc84d9913e94ec407e16d  xmodel/block-descent-a1-cubic-one-place-euler-obstruction-coordinator-integration-sol56-20260830.md
7df557cc5e9e16d7f7b9b3a0fd1d476a26d41dfbc046736fa7a35c7f87197e29  xmodel/block-descent-a1-ruling-transfer-coordinator-integration-sol56-20260830.md
f97207189cc80f1a3c1c80dca9cb172dbeeb4fbd99b61266b4ed5c1d3f9b0ff8  xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md
```

The producer artifact JSON is internally consistent (body 9646 bytes, body
hash `1153c316...`, full-file hash equal to the charged hash).  A shell was
available; the replay was actually executed (Section 1, item 7).  The
Arzhantsev--Zaidenberg PDF was read from rendered pages, not layout text
extraction.  I did not inspect `jc2-lean`, sibling external-model prompts,
logs, reports, or receipts, canonical ledgers, or unrelated files, and ran
no heavy CAS.  This review makes no exit-price assertion and emits no
`charge_basis` line; receipt status `ABSENT` is expected.

## 1. Itemized audit

### 1. Classification source coverage — CONFIRMED

Verified against the pinned PDF.  Printed page 3, subsection 1.1: a curve is
acyclic iff `pi0(C)=pi1(C)=1`.  Theorem 1.3(b) (Lin--Zaidenberg, ref [55])
states verbatim: *any reduced, simply connected plane curve* is equivalent,
under `Aut(A2)`, to

```text
(1) y^eps_y p(x)=0        or        (2) x^eps_x y^eps_y prod_(i=1)^r (y^a-kappa_i x^b)=0,
```

with `eps_x,eps_y in {0,1}`, `p` with simple roots, `a,b>=1` coprime,
`r>0`, `kappa_i in C^x` pairwise distinct.  This matches the producer's
Section 1 side conditions symbol for symbol.  Irreducibility is genuinely
not assumed: part (a) is the irreducible singular case; part (b) is the full
reduced statement, and connectivity is not even required (Corollary 1.2
handles disconnected simply connected curves, which reappear as form (1)
with `eps_y=0`).  A connected contractible curve is a fortiori reduced,
connected, and simply connected, so the survivor's branch is covered.

Hypothesis check against the charged survivor, not via Euler characteristic
alone: contractibility of `B` is supplied by the funnel Section 7 direct
argument (component normalizations `A1` by the Chau input, unibranch
singularities homeomorphic to their normalizations, multibranch gluing
along the promoted forest incidence), with `b0(B)=1` from the one-place
Euler integration (0.3).  Both normal forms are in fact simply connected,
so the classification list is internally sane: every component of form (2)
is the homeomorphic image of `C` under `s -> (c1 s^a, c2 s^b)` with
`gcd(a,b)=1`, components meet pairwise only at the origin, and form (1)
curves are disjoint lines or a tree of lines.

Nit: Theorem 1.3(b), including both displayed equations and the side
conditions, sits entirely on printed page 3; the producer cites "pages
3--4".  Cosmetic.

### 2. Henselian splitting, local companion, global transitivity — CONFIRM_WITH_CORRECTIONS

Reconstructed independently.  At any `b in B` (smooth or singular on `B`,
above singular points of `Y` included), the fibre partition `(2,1)` gives
the closed-fibre algebra two local factors of lengths two and one; over the
henselian (equivalently analytic) local base the two idempotents lift
uniquely, splitting the finite flat rank-three algebra as
`A = A_2 x A_1` with flat factors of constant ranks two and one.  The
Nakayama argument confirms `A_1 =` the base itself: the unit generates the
rank-one closed fibre, hence the module.  Therefore the entire local
complement group preserves the companion sheet, and its image lies in one
conjugate of `S2`.  Nothing about smoothness is used, so the statement holds
at singular branch points exactly as claimed; and the producer correctly
refrains from choosing any globally based companion letter.  Globally,
`Y` integral makes `V=Y-pi^(-1)(B)` a nonempty irreducible open, so
`V->A2-B` is connected finite etale of degree three and the monodromy is
transitive.  All confirmed.

**Correction (a), load-bearing.**  The Section 2 sentence "at a generic
smooth point of every branch component its meridian is a nonidentity
transposition" is not free and is never justified in the text.  It needs
local analytic irreducibility of `Y` at the non-etale point: the rank-two
factor is then the henselian/analytic local ring of a normal (hence
analytically irreducible, by excellence) surface germ, so its restriction
over the punctured transverse disk is a connected double cover and the
meridian swaps its two sheets.  Charged normality of `Y` supplies this, but
Section 2 never invokes it, and integrality alone is insufficient.  Control:
the integral, non-normal, finite flat degree-two cover

```text
z^2 = x^2(1+y)
```

is non-etale along `x=0` with fibre partition `(2)` there, yet the meridian
of `x=0` acts trivially, because analytically the surface is the two
crossing sheets `z=+-x sqrt(1+y)`.  Genuine ramification does not imply a
nontrivial meridian without unibranchness.  The transposition claim feeds
`rho(h)=tau` in Section 3, so this is a required repair, not a nicety.
With normality invoked, the claim is correct.

**Correction (b), presentational.**  The bridge from the henselian
splitting to the topological local complement group should say that the
idempotents converge on some small analytic ball, over which the cover
splits off the companion as an actual section; then every loop in that
punctured ball preserves it.  Standard, but the text jumps from henselian
algebra to `pi1` without the comparison.

### 3. Form (I): lines and combs — CONFIRMED

(Consuming the repaired item 2.)  The connected-degeneration census of
`y^eps_y p(x)=0` is complete: `eps_y=0` gives `s` disjoint vertical lines,
connected iff `s=1` (a nonzero constant `p` gives the empty curve, excluded
by `b0(B)=1`, and independently by integrality of `Y`, since an etale
degree-three cover of the simply connected `A2` is trivial); `eps_y=1` with
`p` constant gives the horizontal line; `eps_y=1` with `s>=1` gives the
comb, connected for every `s`.

For the comb, `U=(C-{alpha_1..alpha_s}) x C^*`, so
`pi1(U)=F_s x Z` and the `C^*` generator `h` is central; every based
meridian of the spine is conjugate to `h`, hence equal to it by centrality.
This is exactly the right basepoint discipline: no tooth meridian is typed,
no common local label is transported.  With `rho(h)=tau` a transposition
(item 2 repaired), centrality forces the whole image into the centralizer
of `tau`.  I enumerated the full centralizers independently: for each of
the three transpositions, exactly `{id, tau}`, order two — note this is the
full-`S3` fact, stronger than the transposition-only commutation the replay
enumerates.  Orbits have size at most two; intransitive.  Single-line rows:
`pi1=Z`, meridian a transposition, image order two.  The two
infinity-phrase readings are handled correctly: individual comb lines are
one-place, while a whole-curve one-point reading already kills every comb
with a tooth because the spine closure passes through `[1:0:0]` and every
tooth through `[0:1:0]`; both readings land in cases the argument covers.

### 4. Form (II): weighted cones — CONFIRM_WITH_CORRECTIONS

Weights verified: under `r.(x,y)=(r^a x, r^b y)` both `y^a` and `x^b` have
weight `ab`, the axes are invariant, every component of (4.1) passes
through the origin, and `N(x,y)=|x|^(2/a)+|y|^(2/b)` satisfies
`N(r.(x,y))=r^2 N(x,y)`, so each positive orbit in `A2-{0}` meets `{N=1}`
exactly once.

**Correction (c), wording, required.**  "Ordinary and weighted balls are
cofinal neighborhoods of the origin, so (4.3)" is not an argument:
cofinality of two neighborhood systems does not by itself transfer `pi1`
of the deleted neighborhoods without a pro-constancy (local conic
structure) input.  The clean repair, which I verified and which the rest of
the section already contains in substance: take the ordinary ball `B_eps`
on which the analytic idempotent splitting of item 2 at the origin
converges; choose a weighted ball `{N<delta}` inside it; the radial flow
`(x,y) -> min(1, sqrt(delta/(2N)))^. (x,y)` deformation-retracts `A2-B`
onto `{N<delta}-B`, every intermediate scaling staying in the complement
because `B` is a positive weighted cone.  Hence the inclusion induces
`pi1({N<delta}-B) ~= pi1(A2-B)` directly, ordinary balls never being
needed.  With that repair, yes: the single origin-local rank-one factor
puts the **whole** global image inside one companion-fixing `S2`, which is
intransitive.  This uses the `(2,1)` hypothesis at the origin itself —
exactly the point where `S0=empty` is consumed; a totally ramified origin
fibre would void the argument, and the producer's hypothesis correctly
excludes it.  The one-point-at-infinity subrow analysis
(`a<b`, `a>b`, `a=b=1`) was checked and is right, and rightly unnecessary.

### 5. Edge cases — CONFIRMED

* One line, one tooth, several teeth: all die under items 3--4; the
  one-tooth case `xy=0` is the `s=1` comb, so crossing axes are form (I),
  not a missing row.
* Axes rows `eps_x=eps_y=1` and the concurrent-line pencils `a=b=1`
  (coprimality allows it): weighted cones, item 4.
* Irreducible cusps `y^a=x^b`: complement group is the nonabelian torus-knot
  group `<u,v | u^a=v^b>`; the cone identification still confines the image,
  consistent, and this is precisely the case the funnel's smooth-branch
  argument could not reach.
* Alternative infinity readings: both verified (items 3--4); neither leaves
  a gap because the proof never uses the one-place phrase.
* Disconnected `S3` control `z^3-3z+2+xy`: its branch `xy(xy+4)=0` has
  `b0=2`, and additionally the hyperbola component `xy=-4 ~= C^*` is not
  even simply connected, so it fails the LZ hypotheses twice over.  It is
  correctly quarantined as the warning that local companion labels do not
  globalize; I checked the producer's two arguments never propagate a local
  label — form (I) uses one central element, form (II) one local group that
  is already global.

### 6. Proper-block interface — CONFIRMED

Hypothesis supply chain, checked against the charged inputs only:
finite flat degree-three `g2` with `Y` integral, normal, affine from the
block factorization (ruling-transfer integration, Section 2); `B` the
reduced branch support, pure one-dimensional by promoted purity of `R`;
`b0(B)=1` and `S0=empty` from the one-place Euler integration (0.3) on the
`A1`-base row; contractibility from the funnel Section 7; the `(2,1)`
partition at every affine branch value from `S0=empty` plus the rank-three
partition dichotomy `{(2,1),(3)}`.  So every hypothesis of the obstruction
is genuinely supplied, and the producer's conditionality statement is
accurate.  The `P1`-base row was already empty by (0.3).  Consequently,
conditional on the promoted chain (block factorization, fixed sheet,
morphic forest, ruling transfer, Euler census, funnel), **the entire proper
cubic block is empty**: a hypothetical noninvertible Keller map admits no
proper intermediate field with `d2=[K:C(f,g)]=3`.  Combined with the
promoted Galois obstruction `d2!=2`, any proper block has `d2>=4`.  The
theorem says nothing about `d2>=4` rows (the `2+2>3` bridge behind
`R_red->B` fails at rank four), nothing about the primitive/no-proper-block
horn, and nothing about JC2 itself — all correctly disclaimed.  The remark
that an "earlier provisional infinity-gate producer" is superseded points
at an uncharged file; unverifiable here and load-free.

### 7. Desk replay — CONFIRMED

Executed, not trusted:

```text
ordinary / -O / -OO payload identical; payload_sha256
0e1afb3f3d226393fa143d972620607d46ee3db7daf8b37751fee2d2402db740  (matches Section 6);
payload hash independently recomputed from the payload content: match;
--mutate-drop-comb-centrality: RuntimeError
  "comb with 1 teeth must have one common transposition label",
  exit 1 in all three modes (require(), not assert);
AST Assert nodes: 0 (verified by ast walk).
```

The mutation trips the admissible-count gate before any image check, in
every optimization mode, so there is no fail-open path.  Scope is honestly
declared: the script verifies finite `S3` facts only (transposition count,
commuting-transposition enumeration for one through six teeth, cone image
order, the two-transposition `S3` warning).  One delta worth recording: the
proof in Section 3 uses the **full** centralizer of a transposition, while
the replay enumerates only transposition-valued teeth; the missing part (no
3-cycle centralizes a transposition) is trivial and I enumerated it
directly.  The replay does not and cannot check the Lin--Zaidenberg
classification, the product presentation (3.2), the radial equivalence
(4.3), henselian splitting, or any cover realization — the finite
permutation check must not be mistaken for the geometric proof, and the
producer does not so mistake it.

## 2. Consolidated corrections

1. **C1 (mathematical articulation, load-bearing).**  Section 2 must invoke
   normality of `Y` (charged in Section 0) for the generic-meridian
   transposition claim, via analytic irreducibility at the non-etale point;
   integrality alone fails (`z^2=x^2(1+y)` control).  Only Section 3
   consumes this claim; Section 4 does not need it.
2. **C2 (proof wording).**  Replace the cofinal-balls sentence in Section 4
   by the direct route: analytic splitting on a small ball, weighted ball
   inside it, radial flow retraction; (4.3) then holds by a single
   inclusion-induced isomorphism.
3. **C3 (nits).**  Theorem 1.3(b) is on printed page 3; the empty-curve
   degeneration of form (I) deserves one clause (excluded by `b0(B)=1`, and
   automatically by integrality of `Y`).

Unpromoted observation, recorded for the campaign but not needed here: a
conductor/invariant-pair argument suggests normality may be droppable —
for an integral non-normal `Y` with `(2,1)` fibres along a spine, the
normalization glues a monodromy-invariant pair of sheets, which already
contradicts transitivity.  Typed `OPEN`; do not consume without review.

## 3. Maximum-safe theorem

> **Acyclic-branch cubic monodromy obstruction (confirmed scope).**  Let
> `pi:Y->A2_C` be finite flat of degree three with `Y` integral and
> **normal**, etale exactly outside the reduced branch curve `B`.  Assume
> `B` is connected and simply connected (in particular, connected and
> contractible), and that every geometric fibre over every point of `B` has
> partition `(2,1)`.  Then no such `pi` exists.  Proof scope: AZ Theorem
> 1.3(b) normal forms; henselian companion splitting (2.1) at every branch
> point; for form (I), centrality of the spine meridian plus its
> transposition image, the latter using normality; for form (II), the
> weighted radial retraction identifying the global complement group with
> the origin-local one.

> **Conditional block consequence.**  Assuming the promoted proper-block
> chain (block factorization with `Y` integral normal; fixed sheet; morphic
> forest; `A1`-ruling transfer; one-place Euler census (0.2)--(0.3); funnel
> contractibility), the proper cubic block row is empty: no proper
> intermediate field with `d2=3`.  With the promoted `d2!=2`, every proper
> block of a hypothetical noninvertible Keller map has `d2>=4`.

Not established: anything at `d2>=4`; the primitive/no-proper-block horn;
any unconditional statement about JC2; removal of normality; removal of the
`(2,1)`-everywhere hypothesis (the cyclic cover `z^3=y^2-x^3` shows a
totally ramified acyclic branch is realizable, so `S0=empty` is essential).

## 4. Cheapest useful successor

1. **Integration (bookkeeping, cheapest).**  Coordinator integration
   banking the composite `d2 not-in {2,3}` block theorem, with this review
   and the queued second independent review as evidence, and C1/C2 folded
   into the bound statement.
2. **Nearly free strengthening to bank before quartic work.**  The same
   proof generalizes to every degree `d>=3` with `S0=empty`: in form (II)
   the image fixes the origin companion letter, landing in an intransitive
   `S_(d-1)`; in form (I) the spine meridian is a nonidentity permutation
   with a nonempty fixed set (the companion), and its centralizer preserves
   that fixed set, which is proper, so the image is intransitive.  Two-line
   fix-set argument replacing the `S3` centralizer table; unreviewed, typed
   proposal only.
3. **The genuine quartic gate.**  For `d2=4` the load-bearing new
   difficulty is the no-etale-sheet fibre values (partitions `(2,2)` and
   `(4)`), where both the rank-three homeomorphism bridge (`2+2=4`) and the
   fix-set monodromy arguments fail — e.g. a `(2,2)` spine meridian
   `(12)(34)` has transitive dihedral centralizer in `S4`.  The successor
   is the quartic fibre census/Euler ledger controlling that locus, not
   another monodromy pass.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18345`.
- Body SHA-256:
  `d69ce1e97bea3b57d6a5dd297bb5bdb637859123ec5aa1b9819d852e7fc84ea9`.
- Frozen basis: `03a4d8dc557abf1e23e5a039ff5c995131935ff2`.
