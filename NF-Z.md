# NF-Z.md — the neutral-word future quotient

Status: **REDUCED-WITH-PROVED-CORE (2026-08-14, post-review round 1).**
Review chain: first submission claimed PROVED-RELATIVE; Grok returned
**NOT-PROVED** (`xmodel/grok-nfz-review.md`) with three breaks — deep
anagrams colliding under the written invariants (finding 1), a
min/max mismatch in the window threshold (finding 2), and a
state-vs-monoid-element gap in `sigma` (finding 3) — plus errata
(findings 5–6). **This revision repairs all three breaks**: the
invariant is now the ORDERED zone word (the letter action is
non-commutative, so Grok's counterexample pair separates — verified
exactly in `cases/nfz_check.py`), the threshold is fixed to its
definition (`theta* = min` skeleton gap; the old `2/5` object is the
distinct WIN ceiling), and the free monoid on parametric letter
classes with its concatenate-and-re-threshold composition replaces the
unsupported finite-state `sigma`. Honest verdict after repair:

* **PROVED (relative to CONS):** the quotient for single-word
  configurations — bounded ordered interleaved zone + commutative free
  zone + the non-ladder consumers.
* **NF-Z† (entry-conditional residue):** multi-word deep-zone
  coexistence (cross-branch cap coupling below `theta*`); per-entry
  finite check stated in §6.

Machine gate: `cases/nfz_check.py` (25 checks, exit 0), including
Grok's exact counterexample table. Sources: `xmodel/sol-normalform.md`
§§0–4, `xmodel/grok-normalform-review.md`, `xmodel/grok-nfz-review.md`,
`TOWER-UNIFORM.md`. No git commit.

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
            F )       # the free-zone summary: the sub-theta* letters'
                      # MULTISET-level exports only: their product
                      # factor, their letter-local congruence classes,
                      # and the endpoint if it lies in the free zone
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
is monotone (verified on lattices, `nfz_check.py` block D). The letter
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
`theta*` as the MINIMUM skeleton gap). This is the repaired
completeness mechanism: **everything order-sensitive is above
`theta*`, and everything above `theta*` is retained in order.**

## 4. The theorem (repaired) and the free zone

**Theorem NF-Z-core (single-word configurations, relative to CONS).**
*Fix `(td, entry, hierarchy, skeleton)` and suppose the deep zone
(below `theta*`) contains the vertices of at most one neutral word
(plus the CONS-residual root interior). Two neutral words with equal
corrected invariants `I = (tau, Z, u_r, Pi, F)` have identical
CONS-labelled futures. The invariant set is a finite schema family:
finitely many ledgers (divisor chains), finitely many zone SHAPES
(ordered words of length `<= L*` over finitely many letter classes,
each letter an exact symbolic parameter on a residue-class domain),
the endpoint and product as symbolic parameters, and the free-zone
summary; concatenation is closed (§2).*

*Proof.* Non-ladder consumers: as round 1 §3 (review-confirmed) —
price is word-blind; E5F is affine in `u_r` with reroutes as further
letters (the offset law is EQUIVALENT to the pad closed form under the
pad handshake — not "verbatim"; grok finding 6); H8 reads `P_0 Pi`
symbolically; M/terminal read `tau, w`; coefficients are Lemma
Z-Omega. Ladder consumer: order the route's deaths by decreasing gap.
(i) Deaths at gaps `>= theta*`: the participating word letters are
exactly `Z`, retained in order; the register through this range is a
function of `Z`, the skeleton, and the entry packet — equal `Z`
implies equal steps, equal `alpha` at every skeleton vertex, equal
`k_x`/degree labels. (ii) Deaths at gaps `< theta*`: by the definition
of `theta*` no skeleton vertex lies below, so (single-word hypothesis)
these are word deaths and the root residual only. Their cap conditions
are automatic: `k' | P_{j+1}` by Z2 (nested-product divisibility,
machine block E), and every rootward-alive vertex's factor exponent is
a multiple of the relevant nested product (word-rootward part) or of
the full product (root/terminal side, H8), so no non-automatic cap
fires. Their legality is letter-local congruences (`d | u + 1`,
`gcd(a, u) = 1`, `l_j | u_{j-1} + 1`, and the finite-modulus residue
conditions of the sub-`theta*` delta consumers). Their exports are
order-free: the product factor (into `Pi`), the congruence classes
(into `F`), and the endpoint if last; the register values below
`theta*` are read by NO CONS consumer (root-interior depth is
residual) — machine block E demonstrates equal exports with unequal
internal registers. Hence equal `I` gives equal labels everywhere. ∎

**Finiteness** is by the bounded zone (not by a finite transformation
monoid — the register is integer-valued and unbounded; grok finding 3
is accepted: no finite-state `sigma` carries it. The finite object is
the SCHEMA set: `#ledgers x #zone-shapes x #domains`, with `Z`'s
letters, `u_r`, and `Pi` as exact symbolic parameters — Sol's
demanded shape).

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

## 6. The honest residue: NF-Z† (multi-word deep coexistence)

When several neutral words coexist below `theta*` (padding on several
chains at once), a deep death on one word must keep levels alive on
the other words' deep vertices: its `k'` must divide the OTHER
branches' nested-product exponents, and cross-branch
`gcd(P^{(1)}-part, P^{(2)}-part)` is not automatic. The single-word
theorem does not cover this coupling.

**Hypothesis NF-Z† (per-entry check, compiler-usable).** For the fixed
entry/skeleton, compute the cross-branch deep cap
`c_x := gcd`-bound exported by each branch's rootward exponents to the
other branches' sub-`theta*` deaths. If the resulting constraint
system forces `k' <= c_x < u u' <=` every consecutive deep pair (the
td-7 pattern: deep cross-coupled configurations are tower-dead), the
deep zones decouple-or-die and NF-Z closes for that entry; the check
is finite (finitely many branch pairs, divisor arithmetic). If some
entry fails the check, that entry's neutral words stay on the exact
fat record (fail-closed, Sol interface rule 6) — no emptiness
certificate may use the quotient there.

This is the minimal additional hypothesis; it is checkable per entry;
and on every configuration inspected in the promoted corpus (td-7
direct/trunk, the 16 uniform cells, 11-A) the deep coupling resolved
as kills, never as live complexity.

## 7. Trust perimeter

* Relative to **CONS as a consumer list** (§0) — explicitly NOT "the
  promoted kernel" (grok finding 4); a consumer beyond CONS re-opens
  the §1 audit. Root-interior residual status is load-bearing for the
  free zone; a future consumer of root-interior atoms re-opens §4(ii).
* The ladder laws are the promoted calculus (td=6-calibrated,
  reviewed on td-7); Z1–Z3 are algebraic identities on them.
* Sibling-`X` gap ties: carved out (§0).
* **Compiler gating is unchanged:** even with NF-Z-core + NF-Z†,
  the census compiler remains gated on NF-P (parametric charged
  letters, `nu = 1` schemas, the 11-A resonance class) and NF-M
  (multi-orbit merge ODE types). This document ungates only the
  neutral-word slice, and only per-entry where NF-Z† checks.

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
python3 cases/nfz_check.py     # 25 checks, exit 0
```

Blocks: A core identities (Z1 algebra + td=6 template `1003/42`; Z2
word formula, `k' >= uv`, coprimality; Z3); B Grok's counterexample
pair replayed EXACTLY (both step tables and both `alpha_exit` values),
collision under the round-1 invariants, separation under the corrected
ordered `Z`, non-commutativity of the letter action; C `theta*` vs the
WIN ceiling on the td-7 skeleton (`1/13566` vs `2/5`) and zone
boundedness (`P_prev <= 3/(2 theta*) = 20349`); D the composition law
(sample + associativity + monotonicity); E free-zone order-freeness
(equal exports, unequal CONS-unread registers, automatic caps,
letter-local congruences); F 11-A `v_2` and the td-7 N2/N3/N4 numbers
with the corrected Case-A attribution. `cases/tower_check.py` remains
the promoted N1–N4/tower gate (exit 0, unchanged). No git commit.
