# Opus 5 hostile review: complete irreducible charged genus-three row

Date: 2026-08-31 UTC
Reviewer: Opus 5, independent hostile referee
Packet: `f26953c6ba20fb5b03db890c99a1964c12cbaa96f7961469565f8ca5927cf85e`
Lifecycle: **INDEPENDENT HOSTILE REVIEW / NO PROMOTION AUTHORITY**

## 0. Custody

All twenty charged files were hashed before any mathematical reading.  All
twenty match the packet byte for byte.  Custody therefore does **not** fail
and this report proceeds.

Additional custody checks performed, none of them requested but all of them
passed:

* Body seals.  For each of the eight charged markdown artifacts there is
  exactly one standalone `<!-- BODY-END -->` line, and the declared body byte
  count and body SHA-256 both reproduce.  (`10493`, `17337`, `17754`,
  `18228`, `12436`, `11924`, `11376`, `2829` bytes respectively.)
* Artifact JSONs.  Each charged `.artifact.json` records `full_sha256` and
  `file_bytes` agreeing with the packet hash and the file on disk.
* Replay determinism.  All five charged replays run under `python3`,
  `python3 -O`, and `python3 -OO` with byte-identical stdout.  The four
  published stdout digests reproduce exactly:

  ```text
  8887e27ce81d4ca54ee114bbcbb6b4a503cef2fdd525d5d73934bd0e653a67ed  cable_b1
  42074e7effccc2d3beb75074a281f83c121ba5e0aaa3278b96d922f3bf4a8013  m0_ramification
  3d502c2a70391497024dfa6ec5d438d5b57710e533051899e3d78f94e4bd6e41  t34_m0_projection
  bd215282fcf28572401de5d2318c1cf7894ee56739e546a532d9c20cf6f9819a  t34_m1_ramification
  ```

  The total-delta replay publishes no stdout digest; it is byte-stable and
  its payload is `926434991de015d440b393687fc3de4bb91e788d92b96a5ac3f53ca375821c6d`.
* Mutations.  All eight declared mutations exit `1` with their intended
  `RuntimeError`, and still exit `1` under `-O`/`-OO`.  No script contains an
  `assert`, so there is no `-O` fail-open hole of the kind seen earlier in
  this campaign.  An undeclared flag is rejected by `argparse` with exit `2`
  rather than silently passing.  I record that my own first mutation sweep
  produced a **vacuous pass**: a `zsh` word-splitting error made every
  invocation a file-not-found `exit 2` that superficially reads as
  "nonzero, as expected".  The results above are from the corrected run.

Corrigendum provenance.  Every checkable assertion of
`post-ledger-dependency-hash-corrigendum-sol56-20260831.md` is true.  Hashing
only, reading no content, I confirm

```text
72cf5510...c347 = significant-news-ideation-rank4-cycle-grok46-20260830.md   (misbinding real)
440c83af...3bf7 = block-descent-a1-total-delta-fox-localization-hostile-review-gpt55-20260830.md
60ba8f433f4ecd98ead9820dc627c9a88f927851d3289af07de2c68b005824a0
                = block-descent-a1-quartic-double-plane-fox-localization-kernel-sol56-20260830.md
a25d4b2f...52c5 = block-descent-a1-genus-three-spectator-fox-local-kernel-sol56-20260830.md
```

The cable artifact's §1 does bind the GPT-5.5 review path to the grok46
ideation digest, so the defect the corrigendum reports is genuine and its
correction is exact.

## 1. What I reproduced independently

Everything below was recomputed from scratch, not read off the artifacts.

**Exact symbolic (sympy, desk-small).**  Cable §4–§5: solving
`[t^10..t^6](V^2-U^3)=0` for `b4..b0` returns precisely (4.3); the residual
`[t^5]` coefficient is `-3a1(4a0-a2^2)/8`, precisely (4.4).  With `a1=c!=0`
and `a0=a2^2/4`, `h=a2/2`, the normal form (0.4) follows and
`V^2-U^3-(3/4)c^2 h U = (c^3/64)(8t^3+24ht+9c)` holds identically, so (4.5)
is exact.  `Res_t(U',V') = -1728c^5`, exactly (4.6).  Reducing the two
divided differences modulo `t^2-st+p` gives (5.1) verbatim, and
`Res_p(E1,E2) = -s^4(s^3+4hs-c)`, i.e. (5.2) up to a unit.  Substituting
`p=c/s-h` annihilates **both** divided differences modulo `H`, and
`s^2-4p+3c/s ≡ 0 mod H`, so (5.4)–(5.5) are exact.

**Finite group/braid (stdlib).**  Independent Artin-action enumeration
reproduces every entry of cable (6.5): `T(2,7)` 0, `T(3,4)` 24, all four
winding-two rows 72, all four winding-three rows 0.  Independent reduced-Burau
computation reproduces (6.3) for all eight sign/chirality variants, and shows
the framing convention is genuinely load-bearing: for the `p=2`, `eps=+1`
family, `q=±1` gives `t^4-t^2+1` (determinant 1), `q=±5,±7` give different
polynomials, and only `q=±3` gives `(t^2-t+1)(t^4-t^2+1)` and 72 colorings.
The `q=±1` row independently re-derives total-delta (5.4)'s
`det(C_(2,±1)(J))=1`.  I also confirm `216 = 96 + …` with `96` ordered
full-`S4` transposition triples (= 16 spanning trees of `K4` times `3!`),
`96` triples with a repeated edge, and `0` in the intersection.

**By hand.**  All eight Artin steps of total-delta (7.4) close on
`((12),(13),(14))`; the semigroup `<3,4>` has gaps `{1,2,5}`.  The genus-two
census (4.2) and the genus-three census (0.3) are re-derived from
`(p-1)(|q|-1)=2g` with `gcd(p,q)=1` plus `p·g(J)<=g`.  The determinant lemma
of total-delta §5 is correct in every step.  The conductor-six delta-sequence
arithmetic is re-derived: `h=1` forces `(r0-1)(r1-1)=6` hence `(7,2),(4,3)`;
`h=2` forces `3d-1<=6` hence `d=2`, then `(a-1)(b-1)-1=1` hence `(a,b)=(3,2)`
and `r2=3`, so `(6,4,3)` is unique; `(9,6,1)` fails freeness because
`1 ∉ <3,2>`.

**Cross-artifact consistency I derived and the artifacts never state.**  The
Euler ledger `e(U)=4-2h-|T31|-2n4` follows from
`e(Y)=4(1-e(B))+e(R)+e(W)` with `e(B)=h-n22`; this is threat-map (2.3) with
no assumption beyond the stated ones.  Applying it to the threat map's own
§6 spectator (`h=1`, `m=2`, `n4=0`) predicts `e(U)=0`, and I verified
directly that `U ≅ Gm × A1`.  Better: normalizing that spectator's branch
`(4t-4t^3, 2t^2-3t^4)` by `X=t^3-t`, `Y=t^4-(2/3)t^2` puts it at `a=-1`,
`b=-2/3`, `c=0`, which is **exactly stratum III** of T34-m0 (3.6) with
`q^2=4/3`; its node at `t=±1` and its cusps at `t^2=1/3` are then forced,
and they match the threat map's independently computed values.  Two
artifacts written in different lanes agree to the last coefficient.

I also verified the delta allocations of (3.6) directly: stratum II's
conductor endpoint `t=-r` has local semigroup `<2,3>` (`δ=1`), stratum IV's
`t=q/2` has local semigroup `<2,5>` (`δ=2`), stratum III's `t=±q/2` are
ordinary cusps.  A stdlib sweep over a rational grid found **no fifth
stratum**.

## 2. Claim 1 — total-delta reduction: `CONFIRM_WITH_CORRECTIONS`

**Weakest exact hypotheses.**  `B` reduced irreducible affine plane curve
over `C`; `normalization(B) = A1` (equivalently one place at infinity);
`Δ_aff(B) = 3`; `b1(B) = 1`; a transitive `ρ: π1(A^2-B) -> S4` sending every
positive generic meridian to a transposition.  Conclusion: the delta-sequence
is `(4,3)` and `K_infinity = T(3,4)` up to mirror.

The mathematics reproduces.  All twelve numbered identities I could test are
exact, the ten coloring counts are exact, the census is complete, and the
`b1>=2` inference from the `(6,4,3)` normal form is airtight: `H(s)` cannot
have a triple root when `c!=0` because `H''(s)=6s` forces `s=0` while
`H(0)=-c!=0`; two distinct roots give two distinct unordered pairs because
their sums differ; and `b1(B) = Σ_z(#ν^{-1}(z)-1)` follows from the
Mayer–Vietoris sequence of the pushout `Z -> X`, `Z -> ν(Z)` with `X = A1`
contractible, giving `0 -> H1(B) -> Z^N -> Z^{1+k} -> Z -> 0`.

**Corrections.**

1. *Notation collision on `m`, and it is live in the combined row.*  The
   coordinator uses `m` for the number of irreducible components of `B`
   ((0.1), (6.2) `m >= 2h-1`); the threat map and both projection artifacts
   use `m = |T31|`.  The combined genus-three row consumes both artifacts.
   Any downstream statement must qualify which `m` it means.  This is exactly
   the FALLACY-v2 target/arrival-index hazard and it should be repaired by
   renaming one of them before promotion.

2. *`(6,4,3)` and `(4,3)` have the same value semigroup.*  Both generate
   `Γ = <3,4>`, gaps `{1,2,5}`, conductor `6`.  §3 is therefore **not** a
   semigroup census; it is a census of delta-*sequences*, and `δ_0` (the
   plane degree: `6` versus `4`) is what separates the two rows and what
   determines `K_infinity`.  The artifacts never say this, and a reader who
   reads §3 as a semigroup classification will conclude the two rows are the
   same curve type.  State it.

3. *The primeness interface is redundant for this row.*  `#gaps(Γ_infinity)
   = dim_C C[t]/C[X,Y] = Δ_aff(B)` is a purely algebraic identity; with
   `Γ` symmetric its conductor is `2·3 = 6`, and §3's arithmetic then yields
   `(7,2),(4,3),(6,4,3)` with no knot theory whatsoever.  So even if Neumann's
   rooted-splice/Rudolph/Schubert primeness chain were withdrawn, the census
   survives.  This makes the row *stronger* than the artifacts claim and
   removes the largest uncharged-source exposure from the critical path.

4. *`(7,2)` admits a knot-free exclusion.*  `δ_1 = 2` gives a degree-two
   linear projection, so `π1(A^2-B)` is generated by **two** meridians, whose
   images are two transpositions.  Two transpositions never act transitively
   on four letters (equal → `C2`; overlapping → `S3`; disjoint → `C2×C2`,
   orbits `{i,j},{k,l}`).  No `T(2,7)` boundary computation is needed.

5. *Uncharged dependency surface, listed so it is not mistaken for audited.*
   The GPT-5.5 fox-localization review is not charged; the corrigendum stands
   in for it.  Of the three interfaces it is said to confirm, I verified two
   from first principles — the nearby-fibre genus identity `χ(F_ε)=1-2Σδ_p`
   via `μ_p = 2δ_p - r_p + 1` and circle gluing, and the meridian-compatible
   surjection `π1(S^3-K_infinity) ->> π1(A^2-B)` (the individual relations
   `x_j = β_v(x_j)` imply `x_j = β_1···β_s(x_j)`, so the Artin presentation of
   the closed boundary braid maps onto the ZvK presentation).  The third,
   prime iterated-cable classification, rests on Neumann 1989 Thm 2(i),
   Rudolph §4/§6, and Schubert; no web access, so it is typed as an
   **uncharged primary-source dependency**, not as a checked step — but by
   correction 3 it is not load-bearing here.  Also uncharged in this packet:
   `ops/block_descent_a1_quartic_minimal_cycle_replay.py` (so the threat map's
   `df9ffae6…`/`561550f5…` digests are unverified here), the ruling-transfer
   integration supplying `e_c(U)=e(C)+Q>=1`, the morphic forest theorem, the
   Chau source audit, and Arzhantsev–Zaidenberg Cor 1.2.

**Attempted failure model.**  I tried to keep `b1 = 1` inside the winding-two
row by collapsing the two self-pairs onto one image point; (5.6) defeats this,
since two distinct two-element sets have a union of size at least three and
that fibre alone contributes `2`.  I tried a repeated root of `H` as an
escape; (5.5) keeps the endpoints distinct and the no-triple-root argument
still leaves two distinct roots.  I tried sign and mirror variants; the
coloring counts are sign-insensitive (verified for all eight variants) and
the delta-sequence arithmetic uses absolute characteristic data.  I tried
`K_infinity` composite — the connected sum of two trefoils has determinant
`9` and does survive the determinant filter at genus two — but it is removed
by one-place primeness at genus two and, at genus three, is never reachable
because the delta-sequence census admits no composite row.

**Blast radius if wrong.**  If `Δ_aff = 3` were wrong (i.e. the total-delta
`<=2` theorem or the gap-count identity failed), the entire reduction
restarts.  If the `(6,4,3)` normal form were incomplete, the winding-two row
reopens as a *group-level survivor with 72 colorings*, which is the single
most dangerous shape in the packet.

## 3. Claim 2 — the `m=0` row: `CONFIRM_WITH_CORRECTIONS`

**Weakest exact hypotheses.**  Everything in Claim 1, plus `n4 = 0`,
`|T31| = 0`, `n22 = 1`, and the local point-stabiliser reading of the fibre
partition.  Conclusion: no such packet, so `Δ_aff >= 4` in the no-cusp row.

The argument is correct.  The fibre-length step is right and sharp: two
distinct critical points cannot both be conductor endpoints (`2+2>3`), and a
totally ramified critical point cannot be a conductor endpoint (`3+1>3`), so
a critical parameter `γ ∉ {a,b}` always exists.  Stratum II of (3.6) shows the
bound is *attained* — there one critical point genuinely **is** a conductor
endpoint — so this is not slack.

**Corrections and supplied proofs.**

6. *The "degree-three coordinate is a linear projection" step is asserted,
   never proved, in both `m=0` artifacts, and the whole Zariski–van Kampen
   layer rests on it.*  It is true.  Proof: in the `(4,3)` row `B̄` is a plane
   quartic with `p_a = 3`, geometric genus `0`, hence `δ_total = 3`; since
   `Δ_aff = 3` we get `δ_infinity = 0`, so the unique point at infinity
   `P_infinity` is a **smooth** point of `B̄`.  For any line `ℓ` through
   `P_infinity` other than `ℓ_infinity`,
   `div(ℓ/ℓ_infinity) = (P_infinity + D) - 4P_infinity`, so `ℓ/ℓ_infinity` is
   an affine-**linear** function with pole order exactly `3`; the pencil of
   such `ℓ` is a pencil of parallel affine lines, and `X|_B` is finite of
   degree `3` because `C[t]` is free of rank `3` over `C[X(t)]`.  This
   simultaneously supplies `deg X = 3`, the linearity ZvK needs, and the
   properness ZvK needs.  Without it §3.1 is a bare assertion.

7. *`H_{ν(γ)} = C2` should be derived from orbits, not from a "table".*  For
   a finite flat degree-four map with `Y` normal, the points of the fibre over
   `z` correspond to the orbits of `π1(N_z-B)` on the four sheets, with local
   degree equal to orbit size.  Partition `(2,1,1)` therefore forces orbits
   `{i,j},{k},{l}`, so `H_z ⊆ ⟨(ij)⟩` and is nontrivial, hence `= C2` — with
   no smoothness hypothesis anywhere.  This is exactly the robustness the
   artifact claims but does not demonstrate.

8. *The load-bearing detail of the duplicate is the shared path, and neither
   artifact states it.*  Write the two cluster meridians as
   `m_i = γ λ_i γ^{-1}` with a **common** trunk `γ` and `λ_i ∈ π1(N-B)`.  Then
   `ρ(m_i) = ρ(γ)ρ(λ_i)ρ(γ)^{-1}` and `ρ(λ_1) = ρ(λ_2) = τ` because both are
   nonidentity elements of the abelian group `C2`.  Hence
   `ρ(m_1) = ρ(m_2)` *on the nose*.  Route the two spokes differently and one
   obtains only conjugate images, not equal ones, and the argument dies.  This
   is the single place where the proof could have been fudged; it is not
   fudged, but it is not written either.

9. *A transport-free route exists and should be preferred.*  Put the fibre
   basepoint inside `N ∩ F`, choose all spokes inside `N ∩ F`; the resulting
   triple is a free basis of `π1(F-B)` (so it surjects onto `π1(A^2-B)` by
   ZvK) and lies in `π1(N-B)`.  No braid tail is ever invoked.  The Hurwitz
   argument the artifacts give is correct — `(A,B) ↦ (ABA^{-1},A)` is a
   Nielsen transformation and `B_3` acts transitively on geometric bases — but
   it is a heavier road to the same fact.

10. *Generic `(2,1,1)` is forced, not assumed.*  Threat-map (2.3)/(0.1)
    assume every component is generically `(2,1,1)`.  In the irreducible row
    this is automatic: all meridians of an irreducible `B` are conjugate, so
    if `ρ(meridian)` were a three-cycle the image would lie in `A4`,
    contradicting the charged `S4`.  Record it as a consequence.

11. *Replay evidentiary force is lower than the prose suggests.*  In
    `ops/block_descent_a1_genus_three_t34_m0_projection_replay.py`, the lines
    `DUPLICATE_COLOR_FULL_S4=0`, `HURWITZ_GENERATED_SUBGROUP=INVARIANT`, and
    `CUBIC_CONDUCTOR_RAMIFICATION_CAPACITY=FAILS` are **string literals**, not
    computed values.  They are gated by preceding `check()` calls so they are
    not false, but they carry no independent force.  Worse,
    `multiplicity_checks()` verifies only `2+2>3` and `3+1>3` on hardcoded
    integers: it encodes nothing about cubics, fibres, or conductors.  The
    same holds for the `m=1` replay's `require(3+1>3,…)`, `require(2+2>3,…)`,
    `require(2+1==3,…)`.  Describing these as "the two cubic fibre-length
    inequalities" overstates them.  The geometry is entirely theorem-layer.
    (The artifacts do firewall this in prose; the wording should be tightened.)

12. *(3.6) completeness is asserted in one line; the replay only spot-checks
    four numeric instances.*  I supply the proof.  `G` is depressed, so its
    roots sum to zero, and `D(s) = -3s^2-4a` has exactly two roots `±q`, so at
    most two roots of `G` can be diagonal.  `b1=1` means exactly one distinct
    admissible root.  One distinct root ⟹ triple root at `0`, admissible ⟹
    stratum I.  Two distinct roots `r, -2r` ⟹ either `r` admissible and `-2r`
    diagonal (stratum II) or `r` a diagonal double root and `-2r` admissible
    (stratum IV); both-admissible and both-diagonal are excluded by `b1=1`.
    Three distinct roots ⟹ the two diagonals are `±q` and the third is `0`,
    admissible (stratum III).  Solving the coefficient identities in each case
    returns (3.6) verbatim.  A stdlib sweep found no fifth stratum.

**Attempted failure model.**  I tried to enlarge `H_{ν(γ)}` past `C2` by
putting a unibranch singularity there — blocked by correction 7, since `H` is
fixed by orbit sizes, not by local topology.  I tried to break the duplicate by
re-routing spokes — blocked by correction 8.  I tried to force every critical
point onto the conductor pair — blocked by `2+2>3` and `3+1>3`, and stratum II
shows the inequality is exactly attained rather than generously slack.

**Blast radius.**  If correction 6 failed — if the `(4,3)` row admitted no
degree-three *linear* projection — the entire `m=0` and `m=1` argument
collapses, because both rest on "three meridians generate".  It does not fail,
but it is the load-bearing hinge and it is currently unwritten.

## 4. Claim 3 — the `m=1` row: `CONFIRM_WITH_CORRECTIONS`

**Weakest exact hypotheses.**  Claim 1's, plus `n4 = 0`, `|T31| = 1`,
`n22 = 1`, and `Δ_aff = 3`.  Conclusion: no such packet.

The exhaustion is correct.  `z31 ≠ n` because a closed fibre has one partition
of four, so `c ∉ {a,b}`.  Double root at `c` traps the whole triple in the
fixed-sheet `S3`; double root at a conductor endpoint is impossible by
`3+1>3`; double root elsewhere traps the triple in `C2`.  Two simple roots:
at most one is `c`, and the other is either `T211` (duplicate cluster) or a
conductor endpoint, in which case `X^{-1}(X(a)) = 2a+b` saturates at `n` and
the triple lands in `C2 × C2`.  Both roots being conductor endpoints needs
`2+2>3` and is out.

I independently confirm the local table (1.1) rather than taking it: `T211`
(orbits `2,1,1`) forces `C2`; `T31` (orbits `3,1`) forces the group generated
by transpositions inside a three-set and transitive on it, i.e. `S3` fixing
the fourth sheet; `S22` with exactly two branches forces the two branch
meridians to be *disjoint* transpositions, hence `C2 × C2`.  Each uses only
that the local complement group of a plane curve germ is generated by
meridians and that all meridians of one branch are conjugate.

**Corrections and strengthenings.**

13. *The argument does not need the group identifications at all, and is much
    more robust without them.*  Every non-generic fibre partition of a
    degree-four cover has at least two orbits, so **every** `H_z` is
    intransitive.  Hence: if the vertical fibre over a critical value is
    saturated over one target point, the whole triple lies in a conjugate of
    an intransitive `H_z`; otherwise the ramified cluster of size `e >= 2`
    contributes `e` equal transpositions, leaving at most `3-e+1 <= 2`
    distinct edges.  This single dichotomy covers `m=0` and `m=1` uniformly
    and never mentions `C2`, `S3`, or `C2 × C2`.  I recommend re-basing both
    theorems on it.

14. *A `T31` point is necessarily a singular point of `B`, which narrows the
    `m=1` row to two of the four strata.*  At a smooth point of an irreducible
    `B`, the meridian is conjugate to a generic meridian, so `H = C2` and the
    fibre is `(2,1,1)`.  Strata I and II of (3.6) have `B` with only one
    singular point (the `S22` point), so `m=1` is vacuous there.  The `m=1`
    row therefore lives exactly in stratum III (two ordinary cusps, one `T31`
    and one `T211`, and these two cusps *are* the two critical points `±q/2`)
    and stratum IV (a `<2,5>` point at `t=q/2` which is one critical point,
    the other critical point `-q/2` lying over a smooth point).  In both, the
    surviving critical point is `T211` and the artifact's case (i) fires.
    This is a sharpening, not a repair — the artifact's exhaustion is valid
    without it — but it makes the row concretely checkable.

15. *Uncharged input.*  The `m=1` artifact lists
    `xmodel/block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md`
    (`2531a89d…`) among its charged interfaces; it is not in this packet's
    charged set and is unverified here.

16. Correction 11 (replay force) applies verbatim to the `m=1` replay.  Its
    `cubic_critical_census` is a bookkeeping enumeration of `3` double-root
    events and `9-1 = 8` ordered simple-root assignments minus the one
    impossible both-`T22` case; the counts `3/8/1/7` reproduce, but the three
    `require` calls inside it are arithmetic tautologies.

**Attempted failure model.**  The obvious escape is the `S3` at the cusp: two
overlapping transpositions plus a third edge really can form a spanning tree,
and the threat map's own §6 spectator realizes full `S4` with exactly that
mechanism.  The escape is closed because the cubic carries a *second* unit of
ramification which cannot also hide at the unique `T31`; and if both units
coalesce there, the whole fibre is trapped inside that one `S3`.  I could not
find a third place to put the second unit: `n4 = 0` removes `(4)`, uniqueness
removes a second `T31`, and `2+2>3` removes the double-conductor allocation.
I also checked the reverse direction — whether the spectator of threat-map §6
is a counterexample to this row — and it is not: it is stratum III with
`m = 2`, excluded by `e(U) = 2-m = 0 < 1`, exactly as the threat map states.

**Blast radius.**  If the ruling identity `e_c(U) = e(C)+Q >= 1` (uncharged
here) failed, `m >= 2` reopens and the §6 spectator's shape becomes live at
the local level; only the block gates would then separate it.  That is the
largest single-point exposure of the combined row and it sits outside this
packet.

## 5. Claim 4 — global interface: `CONFIRMED`

Both halves hold, and I supply the proofs the artifacts omit.

*Generation.*  With correction 6 in place, `X` is a linear projection with
parallel-line fibres and `X|_B` finite of degree three; Zariski–van Kampen
then gives `π1(A^2-B) = ⟨g_1,g_2,g_3 | g_j = β_v(g_j)⟩` for a geometric basis
of a regular fibre, so the three fibre meridians generate.  The base `A^1` is
contractible, which is what kills the would-be `π1(A^1 - Disc)` generators;
this is why the affine statement is available at all.

*Transport.*  Any two geometric bases of `π1(D - 3\ \mathrm{pts})` differ by
the `B_3` action; each elementary move `(A,B) ↦ (ABA^{-1},A)` is a Nielsen
transformation with `⟨ABA^{-1},A⟩ = ⟨A,B⟩`, and its inverse likewise, so the
subgroup generated by the whole tuple is invariant; changing the ambient
basepoint conjugates the tuple simultaneously, preserving order and orbit
partition.  Transitivity is therefore a Hurwitz-and-conjugacy invariant of
the whole tuple.  The artifacts' explicit refusal to identify *individual*
colors across tails is the correct discipline and is respected throughout.

*But prefer the transport-free route.*  Correction 9 gives the same
conclusion by choosing the geometric basis adapted to the local frame in the
first place, and never asks what the tail is.  Since "the tail is a braid" is
precisely where an unsupported identification could hide, I regard the
transport-free version as the one that should be promoted, with the Hurwitz
statement retained as a cross-check.

I found no refutation of either half.  The only genuine subtlety is
correction 8, the shared trunk, which is necessary and true.

## 6. Claim 5 — scope: `CONFIRMED`

The closure covers **only**: `B` irreducible and reduced; `normalization(B) =
A1`, hence one place at infinity; `h = k = 1`; `b1(B) = n22 = 1`; `n4 = 0`;
`Δ_aff(B) = 3`; transitive meridional `S4`; the minimal rank-four
`Δ_aff = 3` row with generic `(2,1,1)`.

It says nothing about, and must not be restated as covering: reducible target
branches or source forests with several components; `h >= 2`; `Δ_aff >= 4`;
nonminimal quartic rows; more than one place at infinity; higher generic
degree; the primitive/no-proper-block horn; existence of a proper block; or
JC2.  The `m >= 2` rows are excluded only through the *uncharged* ruling
identity.

One scope caveat the artifacts do not flag.  The identification "the unique
two-point normalization fibre is the unique `(2,2)` conductor pair"
(m0 §1 interface 4) needs two upstream facts: `B` irreducible, and the
morphic forest theorem forbidding a *node* in `R` (so that `R̃ -> R` is
bijective and `B̃ = R̃`).  The forest theorem permits several components to
meet at one point; if that happens with `B` reducible, then
`b1(B) = Σ_z(#ν^{-1}(z)-1) - (m_comp - 1)`, the count of two-point
normalization fibres is no longer `n22`, and interface 4 fails.  Irreducibility
is what saves it, and irreducibility is a hypothesis of the row, not a
theorem — coordinator (6.2) `m >= 2h-1` is vacuous at `h = 1`.

## 7. Maximum-safe theorem

> **Theorem (charged genus-three closure, maximum safe form).**  Let
> `π: Y -> A^2` be finite flat of degree four with `Y` integral and normal,
> with reduced branch curve `B ⊂ A^2` irreducible and `normalization(B) = A1`.
> Assume the monodromy `ρ: π1(A^2-B) -> S4` is transitive and sends every
> positive generic meridian to a transposition, and assume
>
> ```text
> b1(B) = 1,        Δ_aff(B) = 3,        n4 = 0,        |T31| <= 1.
> ```
>
> Then no such `π` exists.
>
> The proof needs exactly four inputs, none of them knot-theoretic:
>
> 1. `#gaps(Γ_infinity) = dim_C C[t]/C[B] = Δ_aff(B) = 3`, and `Γ_infinity`
>    symmetric, so its conductor is `6`; the delta-sequence is therefore one
>    of `(7,2)`, `(4,3)`, `(6,4,3)`.
> 2. The `(6,4,3)` row has the complete normal form `U = (t^2+h)^2 + ct`,
>    `V = (t^2+h)^3 + (3/2)ct(t^2+h) + (3/8)c^2`, `c != 0`, whose self-pair
>    cubic `H(s) = s^3 + 4hs - c` has no triple root; hence `b1 >= 2` and the
>    row is excluded.
> 3. In the `(7,2)` and `(4,3)` rows, `δ_infinity` forces a *linear*
>    projection `X` with `X|_B` finite of degree `n = 2` and `n = 3`
>    respectively; by affine Zariski–van Kampen the `n` meridians of a regular
>    fibre generate `π1(A^2-B)`.
> 4. **Ramification-cluster dichotomy.**  Let `x_1` be a critical value of
>    `X` on the normalization, with fibre divisor `Σ e_i γ_i`.  Choosing all
>    spokes of a regular nearby fibre through a common trunk into a small ball
>    at each `ν(γ_i)`, the `e_i` meridians of each cluster lie in one
>    conjugate of the local group `H_{ν(γ_i)}`.  Since every non-generic
>    degree-four fibre partition has at least two orbits, every `H_z` is
>    intransitive; and over a unibranch point with `H_z = C2` the `e_i`
>    cluster meridians have **equal** image.  Hence either the fibre is
>    saturated over one target point, and the whole tuple lies in a conjugate
>    of one intransitive `H_z`; or some cluster has `e_i >= 2` and the tuple
>    has at most `n - e_i + 1 <= n - 1` distinct transpositions.
>
> For `n = 2` the image is generated by two transpositions and is never
> transitive.  For `n = 3` the critical divisor of `X'` has length two, and
> every allocation of it — double root at the `T31` point, at a conductor
> endpoint, or elsewhere; two simple roots with at most one at the unique
> `T31`, at most one at a conductor endpoint — yields a saturated fibre or a
> duplicated cluster, hence at most two distinct edges on four sheets, hence
> intransitivity.  This contradicts transitivity of `ρ`. ∎

Everything outside this statement — `Δ_aff >= 4`, reducibility, `h >= 2`,
higher degree, existence of a block, JC2 — is untouched.

## 8. Next falsification test

The closure hangs entirely on `n = deg(X|_B) <= 3`.  At `n = 4` the dichotomy
of input 4 no longer bites, because a length-three critical divisor can in
principle be allocated so that three *distinct* edges survive on four sheets —
and the threat map's own §6 spectator proves that four sheets with one node
and two cusps do generate `S4`.

**NFT-G4.**  Enumerate the conductor-eight (`Δ_aff = 4`) one-place
delta-sequences by the same `d_k`/freeness arithmetic (`h <= log2(g+1) = 2`,
so `h ∈ {1,2}`).  For each surviving sequence record `n = δ_1` and the
critical-divisor length `n-1`.  Then run the ramification-cluster dichotomy as
a purely finite check: for each allocation of the length-`(n-1)` critical
divisor to the strata `{T31, T211, S22}` under the charged multiplicities,
decide whether the induced `n`-tuple of transpositions can have `3` distinct
edges forming a spanning tree with no cluster duplication and no saturated
fibre.

Predicted outcome, stated so it can falsify me: every conductor-eight row with
`δ_1 <= 3` is closed by the same argument, and the **first genuine escape is a
row with `δ_1 = 4`** whose length-three critical divisor admits an allocation
with three distinct cluster edges.  If such a row exists, the method stops at
`Δ_aff = 3` and the campaign needs the global first-leg/ruling/class data,
not more local monodromy.  If no such row exists, the closure extends to
`Δ_aff = 4` for free.

A cheaper, higher-yield second test lives entirely upstream: exhibit or
exclude an actual rank-four block whose ramification curve `R` has two
components meeting at a point.  The morphic forest theorem permits this
(it forbids only cycles), and if it occurs with reducible `B` then
`b1(B) = 1` no longer implies a unique two-point *normalization* fibre.  Both
the `(6,4,3)` exclusion and the conductor-pair fibre-length argument would
then lose their hypothesis, and the "complete" genus-three row would be
complete only for irreducible `B`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `30556`.
- Body SHA-256:
  `2a58b600e311d63ce90dc324481d39bc49249450b49a33e807e1d2e7bf5c7884`.
- Frozen basis: `892179b5d833f89123852b2562afd4b65a4fb1e2`.
