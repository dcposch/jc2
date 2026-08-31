# Hostile review: rank-four reducible component-tree ledger

**Charged producer:** Grok 4.6  
**Frozen charge:** `block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md` and `block_descent_a1_rank4_reducible_tree_ledger_replay.py`  
**Review date:** 2026-08-31

## 1. Charge integrity and review boundary

Before mathematical reading, I recomputed SHA-256 on the two frozen copies. The results were, exactly,

```text
513fe4c022b3a84531c0e42e4cc61a1c9cf2732dde4a5931cb6f8384e166ad4d  block-descent-a1-rank4-reducible-component-tree-ledger-grok46-20260831.md
81ed58e39ddc29a5f8ddc27e10c7cc9ab93602a080800da5b5bbf0c940374066  block_descent_a1_rank4_reducible_tree_ledger_replay.py
```

Both match the charge. **Verdict: CONFIRMED.** I treat only those frozen bytes as charged. Live-repository consultation is restricted to the expressly permitted current-state/interface packets; I did not inspect `jc2-lean`. No canonical or charged file was edited.

## 2. Executive verdict

**Overall verdict: REFUTED.** The four *unlabelled source-forest shapes* are the right combinatorial list conditional on `m<=3`, and the three finite-`T31` Euler solutions are correct. The advertised 16-row component/inertia ledger is nevertheless not exhaustive:

1. its R10--R14 split rows contradict its own forest estimate and are empty;
2. it omits connected `h=1` trees with positive-dimensional `T31` support and mixed `211/31` inertia;
3. its replay hard-codes both mistakes and does not check the estimate that exposes them;
4. Lemma 2.2's indispensable series-to-line and positive-`mu_l` interfaces are not typed or pinned in the permitted packets.

The exact five-way split requested in the charge is:

| claim | verdict | hostile result |
|---|---|---|
| consumed promoted interface | **GAP** | the core rank-four interface is confirmed, but the cited all-degree theorem is used beyond its target and Lemma 2.2 imports an untyped series/line bridge; three status labels are stale |
| Lemma 2.1 / Euler packet | **REFUTED** | E1--E3 are exhaustive only in the finite stratum; the positive-dimensional classification loses connected mixed rows and retains impossible split rows |
| Lemma 2.2, `m<=3` | **GAP** | the count is valid under an exact missing typed hypothesis, but that hypothesis is neither in the allowed promoted packets nor proved in the charge |
| Lemma 2.3 conditional implication | **CONFIRMED** | (2.3) is honestly OPEN and, if assumed with the typed dicritical partition, its inequality gives `m=1`; the displayed equality needs an extra nonnegative term when `B` is a proper subcurve of `A_F` |
| forest shapes | **CONFIRMED** | no fifth unlabelled source forest exists on two or three component vertices under the stated forest and `m>=2h-1` constraints |
| inertia/local `S22` rule | **CONFIRMED** | a `T31` meridian cannot occur in a pair-preserving local group; R15 and R16 are dead, though the replay does not derive either death |
| 16 rows / 4 kills / 12 survivors | **REFUTED** | R10--R14 must be removed, connected mixed-inertia rows must be added, and R2/R3 need an unproved critical-value premise |
| unbounded-family statement | **GAP** | Euler cancellation is exact; Orevkov-freeness is proved only for distinct *immersed* parameter values, while immersion of every `S22` preimage is not pinned |
| replay execution | **CONFIRMED** | all hashes/exits reproduce |
| replay semantic coverage | **REFUTED** | forests, `m<=3`, split kills, support placement, and unboundedness are literals or hard-coded records, not verified consequences |

## 3. Consumed interfaces and scope

### 3.1 Promoted rank-four core

**Verdict: CONFIRMED.** The current `AUDIT.md:142-157` promotes the reviewed rank-four theorem. The integration `xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md:15-25` pins `b1(B)>=1`, an `S22` fibre, `G=S4`, `n22>=h-k+1`, and `m>=2h-1`; lines 82-104 pin that each `B_i` is an `A_F` component with normalization `A1`; lines 108-127 pin stars, the source incidence forest, and the quotient-graph formulas; lines 185-208 pin the component lower bound. The Euler producer `xmodel/block-descent-a1-quartic-branch-topology-acyclic-obstruction-sol56-20260830.md:18-46` pins the fibre census and both signed-Euler equations, while lines 318-363 pin `S4` and the exclusion of a `T31` branch through an `S22` point.

The report correctly distinguishes the `m` analytic places of a reducible curve from Chau's one *set-theoretic* point at infinity. The integration binds Chau Theorem 1 and Corollary 2 at lines 66-70, although it restates only the per-component normalization result. This infinity assertion is non-load-bearing here and must not be strengthened to one analytic branch for all of `B`.

### 3.2 Mis-cited topology and stale labels

**Verdict: REFUTED AS SCOPED; conclusion salvaged.** Charged line 19 attributes “some connected component of `B` has nontrivial `pi1`” to integration `9579d3a1...`. The promoted all-degree theorem in `AUDIT.md:77-95` guarantees such a component of the original `A_F`, not of an arbitrary proper-block subcurve `B`; the rank-four integration expressly does not assert `B=A_F` (`5d7df7ce...:103-104`). The conclusion for `B` follows instead from the separately promoted `b1(B)>=1` (`5d7df7ce...:148-154`). Replace the citation; no mathematical row changes.

**Verdict: CORRECTION, zero blast radius.** The latest `AUDIT.md:8-33` now promotes the genus ladder through conductor 28, the exact-ring one-cusp Poisson result, and the one-node obstruction. Charged lines 9, 29, 31, 167, and 202 call them provisional or review-gated. Those labels were historically conservative but are stale at review time. None is load-bearing: the first two retain their narrow irreducible/exact-ring scopes, and every charged row is reducible. The one-node scope should also say that the named irreducible curve is the complete reduced branch support, with no unrecorded branch component; the hostile review states the safe theorem at lines 586-600 and warns about the cover interpretation at lines 471-490. Charged lines 196-200 correctly refuse to apply it.

**Verdict: CONFIRMED.** Lemma 2.3 is repeatedly and unambiguously typed conditional/OPEN. Current `AUDIT.md:27-33` still identifies (2.3) as its sole advertised bridge. No unconditional row kill is attributed to it.

## 4. Euler recomputation and the lost rows

### 4.1 Finite `T31`

**Verdict: CONFIRMED.** Here `e(T31)=t>=0`, `h>=1`, and all other variables are nonnegative integers. For `C=A1`,

```text
2h+t+2n4+Q=3
```

forces `h=1`, `n4=0`, and `(t,Q)=(1,0)` or `(0,1)`. For `C=P1`,

```text
2h+t+2n4+Q=2
```

forces `h=1` and `t=n4=Q=0`. These are exactly E1--E3; no `t>=2` or `n4>=1` row exists.

### 4.2 The report's own estimate kills every split `T31` row

**Verdict: REFUTED.** Accept for the moment charged line 80's formula and cap

```text
e(T31)=h31-sigma,       sigma<=n4+(m-h).
```

Then exactly as charged line 83 states,

```text
2h+e(T31)+2n4+Q >= 3h+h31-m+n4+Q.       (4.1)
```

For R10--R14, `h=2`, `m=3`, and `h31>=1`, so the right side is at least `4`; the Euler target is only `3` (`A1`) or `2` (`P1`). This is an immediate contradiction for every `n4,Q`, not merely for the cheapest `n4=Q=0` case. At that cheapest value the table itself displays the failure: R10--R12 require `sigma=2` and R13 requires `sigma=3`, whereas the cap is `sigma<=3-2=1`. Thus R10--R14 are unconditional EULER/FOREST kills, not OPEN rows. Their survivor ranking and the claimed need for Lemma 2.3 are false.

The line-192 repair attempt is also arithmetically invalid: an “extra unibranch point already in `T31`” is not a deleted point and cannot increase `sigma`; if its fibre stays `(3,1)`, it remains part of the constructible locus and contributes normally to its Euler number.

### 4.3 Positive-dimensional `T31` does not force `h=2`

**Verdict: REFUTED.** Charged line 171 makes the unsupported converse jump “one-dimensional `T31` plus `m<=3` forces `h=2,m=3`.” Inequality (4.1) permits `h=1`, and the report never enumerates it. Within its own bookkeeping, the explicit omitted arithmetic row

```text
T2; h=1, m=2; (m211,m31)=(1,1);
h31=1, sigma=1, e(T31)=0;
C=P1, n4=0, Q=0
```

satisfies both Euler (`2+0=2`) and the stated forest cap (`1<=0+(2-1)`). The `C=A1,Q=1` analogue also satisfies them. An `S22` self-identification can be supported on the `T211` component, so the local pair rule does not remove the abstract row. Whether a deeper local theorem excludes its mixed point is a separate geometric obligation absent from the ledger; it cannot justify omission.

More basically, if a positive-dimensional `T31` stratum coexists with isolated `(3,1)` values on `T211` components, the exact constructible formula must contain their cardinality `t0>=0`:

```text
e(T31)=h31-sigma+t0.
```

Charged line 80 silently drops `t0`, even though E1 elsewhere relies on precisely such isolated points. The lower bound (4.1) remains valid, and becomes stronger after `+t0`, so the split-row contradiction survives; exact row enumeration does not. Connected mixed assignments on T2, T3path, and T3star must be generated and tested. This is the requested Euler row lost by the signed replacement.

Using the promoted specialization rule more precisely makes the omission sharper. A point on the closure of a `T31` component is still in `T31` when its fibre remains `(3,1)`; a mixed component intersection is not automatically a puncture. Specialization from generic `(3,1)` to `(2,1,1)` is forbidden, and `S22` is forbidden on that component, so only `S4` points puncture it. Thus the safe exact form is

```text
e(T31)=h31-s4+t0,       0<=s4<=n4.
```

The Euler equations then force `C=A1,h=1,h31=1,n4=Q=t0=s4=0` for every positive-dimensional survivor. Up to graph automorphism and requiring at least one `T211` component, this supplies six omitted generic-inertia colourings: one on T2; three on T3path (one `31` at an end, one `31` at the centre, or two adjacent `31`s); and two on T3star (one or two `31`s). A minimal witness is

```text
T2 with one T31 component and one T211 component;
the mixed point remains fibre type (3,1);
one S22 self-pair lies on the T211 component;
e(T31)=1, C=A1, h=k=1, n4=Q=0, n22=1.
```

This mixed point is not locally absurd: for two smooth branches tangent with intersection multiplicity two, the local Artin relation `abab=baba` is satisfied by `a=(123)`, `b=(12)`, since both `ab` and `ba` are transpositions. Adding the self-pair meridians `(12),(34)` generates `S4`. This is a ledger-level counterconfiguration, not an assertion that a global Keller cover exists. Conversely, all-`T31` colourings are killed by parity. Exact corrected counts depend on whether those already-dead colourings and finer pairing data are called rows; the charged `16/4/12` counts are untenable under either convention.

## 5. Lemma 2.2: the dicritical count

**Verdict: GAP.** The proof at charged line 92 crosses precisely the flag/place/series firewall. Chau 2004 Lemma 1 is quoted as producing a dicritical **series** `phi` and a nonconstant curve `f_phi(C)`. The next sentence silently replaces it by an Orevkov dicritical **line** `l subset L_F`, then replaces `deg(f_phi)>0` by `mu_l>=1`. Neither permitted rank-four packet contains Chau Lemma 1, Orevkov's identity/definitions, the series-to-line map, or the identification of `mu_l` with a positive mapping degree. The integration pins only `B_i subset A_F`, equality with an `A_F` component, and normalization `A1`. Its warning `B` need not equal `A_F` is explicit.

The weakest exact hypothesis that repairs the proof is:

```text
(D1) every Orevkov l in L_F has one irreducible nonconstant image alpha(l);
(D2) alpha:L_F -> Irr(A_F) is surjective;
(D3) mu_l is a positive integer for every such l;
(D4) N-1=sum_l(mu_l+corr_l), with every corr_l>=0.
```

Then one irreducible line cannot map onto two different irreducible components, so distinct target components require distinct chosen lines, and

```text
m <= #Irr(A_F) <= #L_F <= sum_l mu_l <= N-1=3.
```

This also settles both requested attacks *conditionally*: two components cannot share one irreducible line as their full image; several lines sharing one component only wastes more budget. A realizing line with `mu_l=0`, however, breaks the count, and the charge does not rule it out because it never types `mu_l`. Until (D1)--(D4) are sourced, `m<=3`, the four-forest finiteness, every leftover calculation, and the entire row ledger remain review-gated. The replay's `require(3 <= 3)` is not evidence for any link in this chain.

### 5.1 R2 and R3 are not safely killed as written

**Verdict: GAP.** Charged line 151 says E1's one finite `T31` point consumes a correction *if* it is a unibranch critical parametrization value; lines 156-157 then kill R2/R3 as though the antecedent were forced. It is not pinned. The finite `(3,1)` value can, at the ledger's level of information, coincide with a source-forest intersection of immersed `T211` components, giving a local three-sheet orbit without a unibranch critical value. Such distinct immersed parameter values are exactly the class the report calls budget-free.

The weakest kill hypothesis is: “the unique finite `T31` value in E1 is a unibranch critical value of at least one relevant dicritical parametrization and contributes a positive Orevkov correction not already counted by `mu_l`.” Under it, `m=3` has zero leftover and R2/R3 die. Without it, split each into a killed unibranch subrow and an OPEN incidence-point subrow. Charged line 132's assertion that the displayed `paff` vectors are “exactly” the finite places is similarly false once E1 cusps or any other unibranch singularities are allowed.

## 6. Lemma 2.3 and the unbounded parameter

### 6.1 Conditional summation

**Verdict: CONFIRMED WITH A NOTATIONAL CORRECTION.** Assume (D1)--(D4), the generic identity (2.3) for every `B_i`, and the companion bounds

```text
1 <= f(B_i) <= u_i,       u_i=2 on T211, u_i=1 on T31.
```

The upper bound is the canonical `d1=1` fibre census. The lower companion-sheet floor is load-bearing but is not listed in §0 or restated in either permitted rank-four packet; it should be an explicit consumed hypothesis rather than hidden behind charged line 110.

The sets of lines mapping onto distinct `B_i` are disjoint. Orevkov's equality therefore reads exactly

```text
3 = sum_i(4-f(B_i)) + E + Corr,
```

where `E>=0` is the sum of base multiplicities of dicritical lines mapping to components of `A_F` outside `B`, and `Corr>=0` is the correction sum. Charged line 107 omits `E` while calling the remainder only “corr”; folding `E` into a newly defined nonnegative remainder repairs the display. Since `4-f(B_i)>=2` for every component (and at least `3` on `T31`),

```text
3 >= 2m,
```

so `m<=1`. The implication is exact. The identity (2.3), not its summation, remains OPEN, and the charge does not silently use it in the unconditional Euler or parity arguments. R1 and R4--R14 are explicitly marked `OREV-MISS`; R2/R3, R15, and R16 are the only advertised independent kills, although R2/R3 have the separate gap above and R10--R14 actually die earlier.

### 6.2 `n22`

**Euler verdict: CONFIRMED.** Substitution of `e(B)=h-n22` into the pinned fibre census cancels `n22` exactly, as `768cf08f...:174-188` shows. No Euler upper bound follows.

**Orevkov verdict: GAP.** The charge pins only the conditional statement that identifying two distinct **immersed** parameter values is correction-free. The promoted quotient theorem gives two distinct reduced source preimages at an `S22` point, but the authorized packets do not prove that both component parametrizations are immersed there. A critical branch can carry a positive correction. The weakest safe statement is therefore: ordinary immersed conductor identifications have zero individual Orevkov charge; the current Euler/Orevkov ledgers supply no upper bound on how many such identifications an actual curve may have.

**Honesty verdict: CONFIRMED AS NON-ATTAINMENT BOOKKEEPING.** The report does not impose a numerical cutoff and explicitly disclaims finiteness of embedded curves. But “`n22` is unbounded” must mean “unbounded by these ledgers,” not attainment of every `n22`; absence of a promoted cap is not an existence theorem. Its finite claim is only about coarse source-tree and generic-inertia labels. It is not finite in detailed node-placement/pairing data unless that data is deliberately quotiented out.

## 7. Forests and inertia

### 7.1 No fifth source forest

**Verdict: CONFIRMED, conditional on Lemma 2.2.** For `m=2,h=1`, connected acyclicity gives T2. For `m=3,h=1`, either one three-branch incidence point gives T3star or two two-branch points give T3path; any extra incidence makes a cycle. For `m=3,h=2`, the only abstract forest is an edge plus an isolated vertex, T3split. The cases `m=2,h=2` and `m=3,h=3` violate `m>=2h-1`. Unibranch singularities decorate these forests but do not create a fifth incidence forest. Once the full Euler/inertia constraints are imposed, T3split has no actual row at all.

### 7.2 Pair support and `S4`

**Local-support verdict: CONFIRMED.** A local `(2,2)` group preserves two pairs and lies in `S2 x S2`, which contains no three-cycle. Hence no `S22` point can lie on a `T31`-generic component. The requested attempt to place a legal `(2,2)` pair on `T31` support fails for this exact reason.

This exposes additional errors in the split narrative even before its Euler death. If `h=2,k=1`, then `n22>=h-k+1=2`, not `1`: one cross-identification merely connects the source components and a second is needed to create `b1>=1`. Moreover R10, R12, and R13 cannot use an `S22` edge to join the isolated source piece without touching `T31`; only the R11 support pattern has two `T211` components on opposite source pieces. The replay records `k="1-or-2"`, `n22_min=1` for all and never assigns pairing endpoints.

**Raw group verdict: CONFIRMED.** Relative to a fixed pairing `12|34`, the stabilizer has two orbits of transpositions, not “three conjugacy-class types”: pair-aligned `{(12),(34)}` and overlapping `{(13),(14),(23),(24)}`. The subgroup generated by the aligned pair has order four and two orbits `{1,2}`, `{3,4}`; adjoining any overlapping transposition gives all of `S4`. R15 is dead because three-cycles are even and cannot generate `S4`; R16 is dead because all components `T211` makes `T31` finite, and `h=2` is impossible in the finite Euler equations.

**Application verdict: GAP.** A component meridian is defined only after a base path, and different `S22` points may carry different transported pairings. The charged ledger defines `rho_i` but never enumerates it or node-to-component incidence. The two elementary subgroup calculations therefore do not prove that an actual row must contain a globally well-defined “overlapping component”; the promoted theorem uses *normal* generation, and transporters outside a fixed pair stabilizer can supply conjugates. Multiple pairing configurations are suppressed inside the allegedly unbounded `n22` family. This does not revive a `T31`-supported pair, but it invalidates the replay's claim to have screened complete row-level pairing data.

## 8. Replay audit

### 8.1 Required executions

**Execution verdict: CONFIRMED.** I ran only the named frozen Python script. The three ordinary modes gave byte-identical stdout:

| mode | exit | stdout bytes | stdout SHA-256 |
|---|---:|---:|---|
| normal | 0 | 4857 | `54df64d29d363581e4d1aa8c19c67da54a2b7c070e5aedd58d77d5e70ded2baa` |
| `-O` | 0 | 4857 | same |
| `-OO` | 0 | 4857 | same |

The printed payload digest is `bd6cedfd0328f68780c60844a4c7cb428a2a1d6fa55218911e2476588e27c283`, and the status is `PASS-RANK4-REDUCIBLE-TREE-LEDGER`. Each documented mutation exited `1` with the advertised rejection:

```text
--mutate-allow-h-two-finite-t31  -> FAIL: ... h>=2 with finite T31 is empty
--mutate-apply-one-node-to-T2    -> FAIL: ... one-node does not apply at m=2
--mutate-drop-overlapping-screen -> FAIL: ... pair-aligned generators do not give S4
```

The script is stdlib-only, has no `assert`, CAS, network access, or file write. Optimization cannot disable its `require` gates.

### 8.2 What it checks

**Semantic verdict: REFUTED.** The successful deterministic run does substantially less than charged lines 206 and 233 claim.

- The finite Euler loop does output exactly E1--E3, and desk arithmetic proves exhaustiveness. Internally it checks only `expected_h1 <= h1_keys`, not equality, over finite ad hoc ranges.
- The four forests are literal dictionaries. The script checks only that each listed dictionary satisfies `m>=2h-1`; it generates no forests and cannot detect a fifth.
- “Orevkov `m<=3`” is the tautology `require(3 <= 3)`. No dicritical object or multiplicity exists in the program.
- R1--R16 are hard-coded dictionaries. R10--R13 check only `h31-sigma=-1`; the decisive cap `sigma<=n4+(m-h)` is absent. R14, R15, and R16 are appended with conclusions as literal strings/booleans rather than derived.
- It never enumerates connected positive-dimensional `T31` support, so the six mixed colourings above cannot appear.
- The aligned and overlapping subgroup *orders* `4` and `24` are correctly computed. But `orbit_size()` traverses every orbit, unions all four letters, and consequently returns `4` for every subgroup. Its assertion that `<(12),(34)>` is transitive is false; that group has two two-letter orbits. The order test still proves it is not `S4`.
- Pair endpoints/support, `k`, and the formula for `n22_min` are not modeled. The one-node firewall is a literal false boolean, not a derivation from `m>=2`. The R2/R3 “leftover” arithmetic is correct only after the unencoded cusp premise.
- `n22_unbounded=True` and `live_with_lemma_23=0` are payload literals. The report honestly says (2.3) is not encoded, but the payload is not evidence for either proposition.

The mutations are fail-path smoke tests, not semantic mutations: the first executes an unconditional `require(False)`, the second flips a literal scope boolean, and the third demands the already-known false equality `4=24`. Thus “all mutations fail” is true but does not validate ledger exhaustiveness.

## 9. Correction, blast radius, and next falsification

### 9.1 Weakest safe replacement

The precise hierarchy is:

1. **Promoted, unconditional:** every actual rank-four proper block has `G=S4`, `b1(B)>=1`, at least one `S22`, component normalizations `A1`, the source-forest/quotient formulas, `m>=2h-1`, and the two signed-Euler equations. No bound `m<=3` follows from the permitted packets alone.
2. **Conditional on (D1)--(D4):** `m<=3`, so the four abstract forests exhaust the coarse source shapes. Full Euler accounting then removes T3split and admits connected mixed `T31/T211` colourings; it does not give the charged 16 rows.
3. **Conditional R2/R3 kill:** additionally require their finite `T31` value to be a positively charged unibranch critical value. Otherwise their immersed-incidence subrows remain OPEN.
4. **Conditional `n22` freedom:** require every counted conductor identification to join distinct immersed values. The conclusion is only “not bounded by these two ledgers,” never attainment.
5. **Conditional irreducibility:** add (2.3), the companion floor `f(B_i)>=1`, and the typed dicritical partition. Then the exact inequality `3>=2m` excludes every reducible row, independently of the erroneous tree ledger.

### 9.2 Blast radius

The missing dicritical typing affects Lemma 2.2, every finite-tree claim, every leftover, and the maximum-safe statement. The signed-Euler error removes R10--R14, adds at least six mixed generic-inertia classes, changes the survivor ranking, and invalidates the `16/4/12` counts and both replay digests for any corrected script. The R2/R3 premise changes the advertised independent-kill count. Pair-transport omissions invalidate only the finer `rho_i` screen, not the local ban on `S22` at `T31`. Stale promotion labels and the all-degree citation have zero row-level blast radius. The promoted rank-four theorem and the conditional implication of Lemma 2.3 survive.

No charged or canonical packet should consume the claimed 16-row ledger, its survivor ranking, or its replay PASS as an exhaustive result.

### 9.3 Single best next falsification test

For any replacement replay, require one two-sided exact test: it must **accept** the minimal `h=k=1` mixed T2 record

```text
(m211,m31)=(1,1), e(T31)=1, C=A1, n4=Q=0,
one S22 self-pair on T211,
```

while **rejecting every** `h=2,m=3,h31>=1` record directly from the corrected signed-Euler inequality. This single test catches both the lost connected family and the spurious split family before any splice or existence computation is attempted.

<!-- BODY-END -->
