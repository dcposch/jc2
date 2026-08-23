# NF-Z.md — the neutral-word future quotient (CLOSED RECORD)

Status: **REDUCED-WITH-PROVED-IN-ZONE-CORE (2026-08-14, post-review
round 3 — the QUOTIENT PROGRAM IS CLOSED; superseded by the depth-cap
program, `NF-D.md`).**

**Round-4 verdict (`xmodel/grok-nfz-final.md`): STILL-SHORT — the
round-3 SD-conditional exchange theorem is REFUTED.** CE3: after the
last skeleton death at `theta* = 1/13566`, Z1 forces
`den(alpha_*) = 13566` (the numerator `13566(l+1)−1` is coprime to
`13566` for every integer register), while `P` after
`Z = (3,5,7,9,11)` is `20790`, carrying neither `17` nor `19`; the
equal-`I` free tails `(323,13,15,17)` vs `(13,15,323,17)` then flip
the first-atom live-factor-cap boolean (`k = 39270 | P_1` vs
`k = 87297210 ∤ P_1`) and the μ-boolean `P_1(alpha_*−1) ∈ N` —
Sol-item-3 consumed fields. Lemma 4.2a below is a PURE-WORD lemma;
the interleaved tail does not inherit its hypothesis
(`den(alpha_entry) | P_0` does not give `den(alpha_*) | P_Z`), so the
§4.2 cap row is false in the interleaved ladder and SD is
**necessary but NOT sufficient**. Three counterexamples over four
rounds (register CE1, prefix-δ CE2, cap/μ CE3) each flip a consumed
field between equal-`I` words: the free zone carries ordered
arithmetic no finite invariant compresses. All six CE configurations
are DEAD (`cases/nfd_check.py`), so the census-relevant theorem is a
DEPTH CAP, not a quotient — see `NF-D.md`. What survives of this
document per round 4: the in-zone ordered core (`Z`, `L*`,
`theta*`/WIN, composition), Z1–Z3, the CE record, SD-necessity, the
fail-closed policies. Grok's round-4 finding 2 also stands: block G8
is hardcoded dens, not a menu-deriving corpus gate; SD is unproved on
11-B/13-2d. Round-3 text below is kept as the record, with the
refuted claims flagged in place.

Round-3 summary (SUPERSEDED where flagged):

* **COUNTEREXAMPLE — unconditional free-zone commutativity is
  FALSE.** Prefix-δ integrality `D_f·g − kbar ∈ N` at the entry's
  prefix-menu gaps `g = a/d` is a residue condition on the ORDERED
  prefix products `P_j`, not on letters (re-review finding 1,
  confirmed). Two legal all-free words with equal invariants can
  differ on this consumed boolean whenever some menu denominator `d`
  does not divide `P_0`: `(5,3,7,11)` vs `(5,7,3,11)` at
  `P_0 = 30002`, `g = 7/3` — same ledger, empty `Z`, same head 5,
  endpoint 11, product 1155, classes; the atom-2 boolean flips
  (§4.3, gate block G). Grok's lattice `(3,5,7)/(5,3,7)` and the
  den-5 flip at `g = 8/5` replay exactly.
* **[REFUTED IN ROUND 4 — see the verdict block above]** ~~PROVED~~ —
  the SD-conditional exchange theorem. Under **SD**
  (scale divisibility: every prefix-menu denominator divides `P_0`,
  with margin `g >= w·theta*`) and entry compatibility
  (`den(alpha_entry) | P_0`), every CONS-consumed boolean or export
  of a legal single-word free tail is either AUTOMATIC (constant over
  all legal words, any order) or a function of the written invariants
  — proved field-by-field (§4.2), with the terminal register
  discharged by a gap-order argument (Lemma 4.2b), not a slogan.
* **SD holds on every filed packet** (td-7 prefix menu `{1, 3/2, 2}`,
  dens `{1,2,2}`, `P_0 = 2`; type `(2,3)` pole top `5/2` with even
  packet degrees; 13-2d type `(3,4)` pole top `7/3` with
  `P_0 ∈ {3,9}`; 11-B type `(2,5)` pole top `7/2` with
  `P_0 ∈ {2,6}`) — the lemma the re-review identified as "true on
  some filed packets, unstated", now stated and machine-checked
  (§4.4, gate block G).
* **Architecture consequence:** NO third zone. Entries failing SD
  keep an **ordered free zone** (equivalently: the invariant is
  enriched by the ordered chain of prefix residues mod the lcm of
  menu denominators) and stay fail-closed on the exact fat record;
  entries passing SD — all filed ones — get the commutative free
  zone by the theorem.
* **NF-Z† is POLICY, not a check** (§6, relabelled per the re-review
  and coordinator): fail-closed default-deny in the sense of Sol
  interface rule 6; no per-entry algorithm is claimed.

Machine gate: `cases/nfz_check.py` (39 checks, exit 0; the count is
printed by the script), including Grok's exact counterexample tables
from both review rounds and the free-zone commutator (exhaustive over
residue classes + exact-word instances). Sources:
`xmodel/sol-normalform.md` §§0–4, `xmodel/grok-normalform-review.md`,
`xmodel/grok-nfz-review.md`, `xmodel/grok-nfz-rereview.md`,
`xmodel/sol-td11-13-scope.md` §3, `TOWER-UNIFORM.md`. No git commit.

## 0. Setting

Fix `td`, an L6-surviving entry, a labelled hierarchy, and a bounded
non-neutral skeleton. A **neutral word** at a state `(w = a/d, M_0)`
with poleward degree anchor `P_0` is a sequence of cylinder-(2.5)
letters

```text
letter j: (l_j, u_j),  l_j | M_{j-1},  u_j >= 2,  d | u_j + 1,
          gcd(a, u_j) = 1,  M_j = gcd(l_j, u_j + 1),
frame:    (nu, kbar, rho)_j = (u_j, w(u_j + 1), w),
degree:   P_j = P_0 u_1 ... u_j,     gap:  gamma_j = (u_j + 1)/P_j,
price:    0.
```

`nu = 1` insertions are outside the cylinder (grok-normalform
finding 2) and outside this paper (NF-P). The letters' local
coefficient certificate is the parametric one-orbit solve
`C = -u A/(u+1)` — **Lemma Z-Omega**, whose scope is exactly the
CLEAN-NEUTRAL rows of the promoted certificates (the `N`/`X` rows;
NOT the merge or dirty rows — grok-nfz finding 6).

**CONS** (the consumer list — a list of predicates, NOT the promoted
kernel; grok-nfz finding 4): P0/P1 price and budget; E5F
`n = nu_U kbar_G - nu_G kbar_U`; H8/equal-quotient and scale; M and
terminal data; the promoted ladder calculus — death gaps `kbar/D_f`,
delta descent and death equations, mu-recursion with
`k_v = i_v(alpha - 1) in N`, aliveness with integral factor exponents,
count monotonicity, N1–N4, **WIN and the single-ladder identification
St 8.3(i) + Not 4.1** (added per finding 4), R1.0–R2.2 as the frame
laws. Root-interior tower depth is residual in CONS (the promoted
certificates never compute it) — this is load-bearing for §4.
**Carve-out:** simultaneous sibling-`X` gap ties (the 13-4
configuration) are not handled here.

## 1. What a word touches (unchanged, review-confirmed)

Zero price: `chi, L` untouched. Frame/`C`/`A`: endpoint only. `S`: the
product `Pi = u_1...u_r` only. `Omega`: Lemma Z-Omega's family.
`Theta`: every letter contributes the atom
`(P_j, gamma_j, exponent P_{j-1})`. Grok finding 5/6 confirmed the
non-ladder consumer analysis (§3 of round 1); the ladder consumer is
where round 1 broke.

## 2. The corrected invariants

Let `theta* :=` the **minimum** death gap over the (finite, fixed)
non-word skeleton's competing vertices — the DEFINITION, now also the
instantiation (grok-nfz finding 2 repair; td-7 direct instance:
`theta* = 1/13566`, NOT `2/5`). The `2/5` object of TOWER-UNIFORM is
the **WIN ceiling** (the maximum non-`X` competing gap); it plays a
role only in kill arithmetic (§5) and is never called `theta` again.

```text
I(word) = ( tau,      # the M-ledger as the DROP-VALUE chain in the
                      # divisor poset (positions live in Z, not tau --
                      # grok finding 6 repair)
            Z,        # THE ORDERED INTERLEAVED-ZONE WORD: the exact
                      # sequence of letters with gamma_j >= theta*,
                      # each an exact symbolic parameter over its
                      # residue-class domain, IN ORDER
            u_r,      # endpoint parameter (domain: residue classes)
            Pi,       # the product, one symbolic parameter, plus its
                      # consumer projections (residues, valuations)
            F )       # the free-zone summary (symbolic schema, §4):
                      # the sub-theta* letters' product factor Pi_free
                      # as ONE symbolic parameter plus its consumer
                      # projections (residues, valuations), the class
                      # COUNTS per residue class (symbolic integers;
                      # the free length r_free is their sum), the
                      # endpoint if it lies in the free zone, and the
                      # HEAD letter u_1 when the whole word is free
                      # (Z empty) — E5F reads the junction vertex,
                      # which is then u_1.  On SD-failing entries F is
                      # additionally enriched by the ORDERED chain of
                      # prefix residues P_j mod lcm(menu dens) — §4.3
```

`Z` is an element of the **free monoid** on the (finitely many)
parametric letter classes, of length at most
`L* = floor(log2(3/(2 theta* P_0))) + 1` (a letter has
`gamma_j >= theta*` only while `P_{j-1} <= 3/(2 theta*)`, and `P` at
least doubles per letter; letters never re-enter the zone — monotone).
**Composition** (concatenation of words `W_L . W_R`, poleward factor
left): `Z(W_L . W_R) = Z(W_L) . rethreshold(Z(W_R), P_0 Pi(W_L))` —
re-thresholding drops the right factor's letters whose shifted gaps
fall below `theta*`; this is well-defined and associative because `P`
is monotone (verified on lattices, `nfz_check.py` block D). **`F` has
the induced composition law** (re-review finding 3 artifact row): the
letters dropped by re-thresholding join the free summary — `Pi_free`
multiplies, class counts add, the endpoint comes from the right
factor, and the head slot is filled by the left factor's junction
(only an entirely-free concatenation keeps `u_1` in `F`). The letter
action is **non-commutative** — that is not a defect but the content:
the ladder register genuinely depends on order (§3), so the invariant
must be ordered, and Grok's finding-1 counterexample becomes the
canonical separating example of the corrected definition.

## 3. The ladder register and why order is retained

The three identities of round 1 stand (review-confirmed, machine gate
block A):

* **Z1 (alpha-exit):** a death at gap `g` with step `(k, l)` exports
  `alpha_next = l + 1 - g`.
* **Z2 (difference denominator):** consecutive ladder deaths obey
  `l''/k'' = (g' - g) + l'`; for consecutive WORD deaths **within one
  run** (no intervening skeleton death),
  `gamma_{j+1} - gamma_j = (1 - u_j u_{j+1})/P_{j+1}` and
  `k' = u_j u_{j+1} P_0 / gcd(u_j u_{j+1} - 1, P_0) >= u_j u_{j+1}
  >= 4`.
* **Z3 (decay):** `gamma_{j+1}/gamma_j <= 1/2`.

What round 1 missed (grok finding 1, verified exactly in block B): the
death-step NUMERATOR `l'` is a register threaded through the deaths in
GLOBAL GAP ORDER — the interleaving merge of the word's `gamma`
sequence with the skeleton's gap sequence. `alpha_exit` is
`l'_r + 1 - gamma_r`, and `l'_r` depends on the whole ordered
register: the pair `(3,5,7,9)` vs `(3,7,5,9)` at `w = 2, P_0 = 2`
yields death steps

```text
(6,7),(15,98),(105,10273),(945, 9707954),  alpha_exit = 1834803494/189
(6,7),(21,137),(105,14368),(945,13577738), alpha_exit = 2566192670/189
```

— identical product, endpoint, and first-letter gap; different
exported `alpha` and different `k_x = i_x(alpha - 1)` labels at every
later skeleton vertex. Under the corrected `I` the two words have
DIFFERENT `Z` (order differs at position 2) — separated, as required.
Every register-reading consumer reads it at a skeleton vertex or
through `alpha` at such a vertex; the register position at a skeleton
vertex is a function of the ordered in-zone prefix (the letters with
gaps above that vertex's gap — all in `Z` by the definition of
`theta*` as the MINIMUM skeleton gap). The repaired completeness
mechanism, stated precisely (round 3 corrects round 2's unconditional
version): **everything above `theta*` is retained in order; below
`theta*`, order-sensitivity persists in the register values and — on
SD-failing entries — in the consumed prefix-δ booleans (§4.3); under
SD every consumed output below `theta*` is order-free (§4.2), and
the register is discharged (Lemma 4.2b).**

## 4. The theorem (round 3) and the free zone

**Definition (SD, scale divisibility).** An entry satisfies **SD** if
every gap `g = a/d` (lowest terms) in its prefix menu — the charged
prefix gaps at which Sol's NF-Z item 3 evaluates prefix-δ integrality
`D_f·g − kbar ∈ N` on every created atom, free-zone pads included —
has `d | P_0`, and `g >= w·theta*` (positivity margin; on the filed
packets the menu gaps are `>= 1`, so the margin holds by four orders
of magnitude). **Entry compatibility:** `den(alpha_entry) | P_0`
(td-7: `alpha_1 = 3/2`, `P_0 = 2`).

**Theorem NF-Z-core (single-word configurations, relative to CONS).**
**[FREE-ZONE PART (ii) REFUTED IN ROUND 4** — grok-nfz-final finding
1: the cap/μ row of §4.2 fails in the interleaved ladder
(`den(alpha_*) = 13566 ∤ P_Z`); part (i), the in-zone core, stands.
Kept as the record; see the header block and `NF-D.md`.]
*Fix `(td, entry, hierarchy, skeleton)` satisfying SD and entry
compatibility, and suppose the deep zone (below `theta*`) contains
the vertices of at most one neutral word (plus the CONS-residual root
interior). Two legal neutral words with equal corrected invariants
`I = (tau, Z, u_r, Pi, F)` have identical CONS-labelled futures. The
invariant set is a finite schema family: finitely many ledgers
(divisor chains), finitely many zone SHAPES (ordered words of length
`<= L*` over finitely many letter classes, each letter an exact
symbolic parameter on a residue-class domain), the endpoint, product,
and free-summary parameters symbolic; concatenation is closed (§2).
WITHOUT SD the conclusion is FALSE — §4.3 exhibits two legal words
with equal `I` and different consumed prefix-δ booleans — and the
free zone must stay ordered on such entries.*

*Proof.* Non-ladder consumers: as round 1 §3 (review-confirmed) —
price is word-blind; E5F is affine in the JUNCTION letter (head) with
reroutes as further letters (the offset law is EQUIVALENT to the pad
closed form under the pad handshake — not "verbatim"; grok finding
6), and the head is in `Z` when `Z` is nonempty, in `F` when the word
is entirely free; H8 reads `P_0 Pi` symbolically; M/terminal read
`tau, w`; coefficients are Lemma Z-Omega. Ladder consumer: order the
route's deaths by decreasing gap. (i) Deaths at gaps `>= theta*`: the
participating word letters are exactly `Z`, retained in order; the
register through this range is a function of `Z`, the skeleton, and
the entry packet — equal `Z` implies equal steps, equal `alpha` at
every skeleton vertex, equal `k_x`/degree labels. (ii) Deaths at gaps
`< theta*`: by the definition of `theta*` no skeleton vertex lies
below, so (single-word hypothesis) these are word deaths and the root
residual only. By the field algebra of §4.2, every CONS item's
consumed output on the free tail is either AUTOMATIC — a boolean that
holds for every legal word in every order (descent, caps, WIN/N4
comparisons, and, **under SD**, every prefix-δ atom) — or a function
of the written invariants (`Pi` and its projections, class counts,
endpoint, head, `tau`, count sequence); the register is discharged by
Lemma 4.2b. Hence equal `I` gives equal labels everywhere. ∎

### 4.2 The free-zone field algebra (the commutator, field by field)

Throughout, "free tail" means every gap `< theta*` in the order
written. The zone boundary itself is order-sensitive — a swap can
push a letter's gap above `theta*` (`gamma'_first = u·gamma_second`)
— but such pairs have DIFFERENT `Z` and are separated by the in-zone
invariant (gate row G10); the commutation question is confined to
reorderings that stay entirely sub-`theta*`. Field by field:

| CONS item | what it consumes from the tail | order behaviour |
|---|---|---|
| price / lambda-budget (P0/P1) | sum of prices `= 0` | constant (letters are price-0) |
| E5F | `(nu, kbar)` of the junction vertex | = head `u_1`: in `Z` if `Z != ∅`, else in `F` |
| H8 / equal-quotient, 11-A `v_p` | `P_0 Pi` and its valuations | symmetric function of the multiset — commutes |
| M / terminal | ledger chain, final `M` | `= tau ∈ I` (equal-`tau` hypothesis); `l_j | M_{j-1}` is domain legality, not a consumed output |
| gap comparisons (WIN `2/5`, N4 `3/8`, skeleton order) | booleans `gamma_j < c` | automatic: every free gap `< theta* << 3/8 < 2/5` |
| intra-tail death order, delta descent | strict decrease | automatic in EVERY order: `gamma_{j+1}/gamma_j = (u_{j+1}+1)/((u_j+1)u_{j+1}) <= 1/2` (Z3) |
| death-equation caps / aliveness | `k_j |` exponent budget | automatic in every order: Lemma 4.2a gives `k_j | P_j`; the factor exponents are supplied by the Z1/Z2 cylinder construction |
| **prefix-δ at menu gaps `a/d`** | boolean `w P_j g − w(u_j+1) ∈ N` per atom | **automatic IFF SD**: `d | P_0 | P_j` gives integrality in every order, and the margin gives positivity (`g >= w theta* > w gamma_j`). WITHOUT SD: order-sensitive — §4.3 |
| count monotonicity | the count sequence | function of `r` (class-count sum, in `F`) and the skeleton |
| mu-recursion: register `alpha_j`, steps `(k_j, l_j)` | — | order-sensitive VALUES with NO consumer: every boolean they feed is automatic (rows above), and `alpha_exit` is terminal (Lemma 4.2b) |

**Lemma 4.2a (automatic caps, any order).** If
`den(alpha_entry) | P_0`, then along any legal word in any order,
`den(alpha_j) | P_{j-1}` and `k_j = den(gamma_j + alpha_j − 1)` divides
`P_j`. *Proof:* induction — `den(gamma_j) | P_j`, `P_{j-1} | P_j`, and
`alpha_{j+1} = l_j + 1 − gamma_j` has denominator dividing `P_j`; the
step denominator divides `lcm(P_{j-1}, P_j) = P_j`. The hypothesis is
NECESSARY: `P_0 = 3`, `alpha = 3/2`, `u = 5` gives `k = 10 ∤ 15`
(gate row); it holds on the filed packets. ∎

**Lemma 4.2b (terminal-register discharge).** `theta*` is the MINIMUM
skeleton competing gap, so no skeleton vertex lies below `theta*`;
deaths are processed in decreasing gap order, so every free-tail
death occurs after every skeleton death, and after the tail's last
death the branch is exhausted. CONS reads the register only (a) as
the input of the NEXT death (mu-recursion/Z1) or (b) through
`k_x = i_x(alpha − 1)` at a SKELETON vertex. Below `theta*` there is
no skeleton vertex, so (b) is empty; the (a)-feeds are internal to
the tail, and their consumed outputs are exactly the automatic
booleans of the table; after the final letter there is no next death.
The rootward exports of the completed branch — depth `r`, endpoint
`u_r`, scale `P_0 Pi`, terminal `M`, junction data — are all in `I`.
Hence `alpha_exit` and the interior `(k_j, l_j)` values have no CONS
consumer. This is a computation over the CONS list of §0, not a
scope slogan; a future consumer of root-interior atoms re-opens it
(§7). ∎

### 4.3 The counterexample: SD is necessary, and what fails without it

Prefix-δ integrality is a condition on the ordered prefix product:
at menu gap `a/d` the atom for letter `u_j` passes iff
`d | a·w·P_j` (equivalently `d_eff | P_j` with
`d_eff = d/gcd(d, aw)`) and the margin holds. Reordering the word
redistributes the prime factors of `Pi` among the prefixes `P_j`.
Exact instance (gate block G, all-free, legal, `w = 2`):

```text
P_0 = 30002 (3 ∤ P_0), menu gap g = 7/3:
  (5,3,7,11): prefix-δ booleans [F,T,T,T]
  (5,7,3,11): prefix-δ booleans [F,F,T,T]
```

Both words lie entirely below `theta* = 1/13566` with the SAME
`tau` (trivial), `Z` (empty), head `5`, endpoint `11`, `Pi = 1155`,
and classes — equal `I`, different consumed boolean. Grok's
re-review lattice replays exactly: `(3,5,7)` vs `(5,3,7)` at
`g = 7/3` gives `[T,T,T]` vs `[F,T,T]` for
`P_0 ∈ {2,4,8,30001,30002}` and both-pass at `P_0 = 30000`
(`3 | P_0`); the den-5 flip `g = 8/5` at `P_0 = 2` distinguishes
`(3,5,7)` from `(3,7,5)`. (These flip rows have `gcd(d, aw) = 1`, so
they are identical under both `D_f` normalizations, `P_j` and
`w P_j`.)

**Architecture consequence (honest answer to the either/or).** The
commutator fails on exactly one consumed field, and the missing datum
is exactly the ordered chain of prefix residues
`P_j mod lcm(menu denominators)`. So: NO third zone. Entries failing
SD keep an **ordered free zone** — equivalently, `F` enriched by that
finite-modulus ordered residue chain — and stay fail-closed on the
exact fat record. Entries passing SD get the commutative free zone by
the theorem. SD is a per-entry finite check: one divisibility per
menu gap.

### 4.4 SD on the filed corpus (why the re-review hunt found no boolean hit)

td-7 (11-A shape): the certified Case-C prefix menu is
`{1, 3/2, 2}` (`cases/towers/t9_15_direct.json`,
`tower.obstruction`), dens `{1, 2, 2}`, `P_0 = 2` — SD holds. Type
`(2,3)` packets (11-A/C, 13-2a/b/c, 13-3, 13-4): pole top `5/2`, den
`2`, and every packet degree `p = b·alpha` is even. 13-2d (type
`(3,4)`): pole top `7/3`, den `3`, `p ∈ {3,9}`. 11-B (type `(2,5)`):
pole top `7/2`, den `2`, `p ∈ {2,6}` (`xmodel/sol-td11-13-scope.md`
§3.1). In each case `den | P_0` because the menu gaps live over the
pole degree itself: `g_top = (alpha+beta)/alpha` with
`alpha | b·alpha = P_0`. This is the lemma the re-review identified
as "true on some filed packets, unstated" — now stated, per-entry
checkable, and machine-checked (gate block G). It is why Grok's
free-zone anagram hunt produced same-`I`/different-register pairs
but no CONS-boolean hit against any named promoted entry.

**Finiteness** is by the bounded zone (not by a finite transformation
monoid — the register is integer-valued and unbounded; grok finding 3
is accepted: no finite-state `sigma` carries it. The finite object is
the SCHEMA set: `#ledgers x #zone-shapes x #domains`, with `Z`'s
letters, `u_r`, `Pi`, and `F`'s parameters (`Pi_free`, class counts,
head) exact symbolic parameters — Sol's demanded shape; re-review
finding 3's quotient of `F` to symbolic form is adopted in §2).

## 5. Specialization and kill-arithmetic corrections (grok finding 5)

* **N1** is IMPORTED (the promoted `(n-1)(nu-1) >= 1` forcing makes
  state-preserving zero-cost steps `n = 1`); cylinder membership is
  its conclusion, not a derivation.
* **N2** = the letter-domain fact `d | u+1` forces `u` odd at
  `w = 3/2` (equivalently the `v_2(Pi) = 0` projection of `Pi` — a
  `Pi`-projection, NOT a `sigma` component).
* **N3** = the window-zone aliveness cap (`gcd(4, 2P_pre) = 2`),
  carried by §3's in-zone analysis.
* **N4** = the absolute one-insertion gap bound
  `(u+1)/(D_prev u) <= 3/8` at `D_prev >= 4` (Z3 is the DECAY ratio —
  a different statement; both hold).
* **The td-7 Case A kill step is `k' = 2 nu_X`** — the pole-to-X death
  (`l/k = (u+1)/(2u) + 1/2 = (2u+1)/(2u)`), NOT the word-word
  corollary. The corollary (`k' >= u_j u_{j+1} >= 4` vs caps) applies
  to consecutive word deaths WITHIN A RUN and is a second, distinct
  window-zone kill mechanism; round 1's attribution is withdrawn.
* **11-A**: unchanged and review-confirmed — the odd-letter domain
  gives `v_2(2 Pi) = 1` vs the resonance's `v_2 >= 3`;
  `H8_EQUAL_QUOTIENT_VP_MISMATCH` at `p = 2` is a `Pi`-projection
  consumer. The `5/8` resonance itself is NF-P material (a
  state-changing clean step, not a (2.5) letter).

## 6. POLICY NF-Z† (multi-word deep coexistence): fail-closed, Rule-6 style

When several neutral words coexist below `theta*` (padding on several
chains at once), a deep death on one word must keep levels alive on
the other words' deep vertices: its `k'` must divide the OTHER
branches' nested-product exponents, and cross-branch
`gcd(P^{(1)}-part, P^{(2)}-part)` is not automatic. The single-word
theorem does not cover this coupling — its hypothesis is FALSE there,
and `F` is not a joint invariant of two interleaved free tails.

**This is a POLICY, not a check** (relabelled per the re-review and
the coordinator). Round 2 sketched a per-entry quantity `c_x` and
called it "a finite check"; the re-review is right that the sketch is
not an algorithm (which exponents, which gcd, over which unbounded
word tails — undefined), and nothing in `nfz_check.py` implements it.
The sketch is withdrawn as a check. The earlier sentence "on every
configuration inspected in the promoted corpus the deep coupling
resolved as kills" is withdrawn as evidence — it had no lattice, no
log, no gate row. What remains true and citable is only the td-7
pattern that a future check would formalize: uniform deep kills of
the shape `k' <= c_x < 4 <= u u'`.

**POLICY (fail-closed default-deny; Sol interface rule 6).** An entry
whose deep zone can carry more than one neutral word is UNRESOLVED by
NF-Z, unconditionally, unless and until a future, explicitly stated
finite check certifies deep decoupling for that entry. Unresolved
entries stay on the exact fat record; the single-word core MUST NOT
be applied to them; no emptiness certificate may use the quotient
there; a run that needs the quotient on such an entry emits
`NEEDS_NF_Z` / `OPEN`, never an empty-panel certificate. This
constrains what a compiler may emit (exactly Rule 6's shape: an open
obligation may yield OPEN or a symbolic candidate, never a certified
empty panel); it is not a theorem, and no completeness is claimed for
the quotient on multi-word entries.

**Round-6 addendum (2026-08-14, TOWER-TD11.md §15):** the first
per-entry instantiation exists — for the three td-11 entries the
policy resolves on the DIE horn (every cross-branch coupling event
lies strictly below the refused X-death, so multi-word
configurations die before any coupling acts; finite check = coupling
census + coupled-cap divisor completion + monotonicity). That
instantiation is finite BECAUSE the entry-level clash kills first;
it does NOT supply the general algorithm this section lacks — for
entries without an entry-level kill, which exponents/gcds over which
unbounded tails remains undefined. The definition gap stands.

## 7. Trust perimeter

* Relative to **CONS as a consumer list** (§0) — explicitly NOT "the
  promoted kernel" (grok finding 4); a consumer beyond CONS re-opens
  the §1 audit. The free-zone half now rests on the §4.2 field table
  and Lemmas 4.2a/4.2b (computations over the CONS list), no longer
  on a "root-interior residual" scope sentence; a future consumer of
  root-interior atoms or of the interior register re-opens §4.2b.
* **SD is part of the theorem's hypothesis.** Applying the free-zone
  quotient to an entry without checking SD (one divisibility per
  prefix-menu gap, plus `den(alpha_entry) | P_0`) is out of
  perimeter; §4.3's counterexample is what goes wrong.
* The ladder laws are the promoted calculus (td=6-calibrated,
  reviewed on td-7); Z1–Z3 are algebraic identities on them.
* Sibling-`X` gap ties: carved out (§0).
* **Compiler gating is unchanged:** even with NF-Z-core, the census
  compiler remains gated on NF-P (parametric charged letters,
  `nu = 1` schemas, the 11-A resonance class) and NF-M (multi-orbit
  merge ODE types). This document ungates only the neutral-word
  slice, and only per entry where (a) SD and entry compatibility
  hold, AND (b) the deep zone is single-word — multi-word entries are
  UNRESOLVED by the §6 policy (default-deny; NF-Z† is not a check).

## 8. What NF-P and NF-M need (updated)

* **NF-P** inherits Z1/Z2 verbatim (price-free identities), the
  ordered-zone/free-zone split, and the composition law; its charged
  letter sits at ONE position, so its register effect is one ordered
  slot in `Z`-position terms. It must supply the `w`-changing closure
  and the `nu = 1` schemas, and it owns the 11-A `5/8` resonance.
* **NF-M** consumes Lemma Z-Omega with the corrected scope
  (clean-neutral rows only) and the schema format of §2.

## 9. Reproduction

```bash
python3 cases/nfz_check.py     # 39 checks, exit 0 (count printed)
```

Blocks: A core identities (Z1 algebra + td=6 template `1003/42`; Z2
word formula, `k' >= uv`, coprimality; Z3); B Grok's round-1
counterexample pair replayed EXACTLY (both step tables and both
`alpha_exit` values), collision under the round-1 invariants,
separation under the corrected ordered `Z`, non-commutativity of the
letter action; C `theta*` vs the WIN ceiling on the td-7 skeleton
(`1/13566` vs `2/5`) and zone boundedness
(`P_prev <= 3/(2 theta*) = 20349`); D the composition law (sample +
associativity + REAL Z3 monotone decay along all orders — the round-2
tautology row is replaced, re-review finding 3); E free-zone export
equalities and letter-local congruences; F 11-A `v_2` and the td-7
N2/N3/N4 numbers with the corrected Case-A attribution; **G round 3:
the free-zone commutator** — the re-review's sub-`theta*`
same-endpoint anagram pairs with EXACT `alpha_exit` values (both
rows of its finding-1 table), all consumed booleans equal under SD,
the prefix-δ lattice at `g = 7/3` and `g = 8/5` replayed exactly,
the same-`I` counterexample `(5,3,7,11)/(5,7,3,11)` at
`P_0 = 30002`, the exhaustive residue-class commutator
(`d_eff ∈ {2,3,5}`: `d | P_0` forces constant-TRUE over ALL orders,
`d ∤ P_0` admits flips for every modulus), Lemma 4.2a with its
necessity witness, the SD corpus row, the coarse-pair identification
soundness row, and the order-sensitive zone boundary.
`cases/tower_check.py` remains the promoted N1–N4/tower gate (exit 0,
unchanged). No git commit.
