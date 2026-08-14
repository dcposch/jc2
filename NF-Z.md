# NF-Z.md — the neutral-word future quotient

Status: **PROVED-RELATIVE (2026-08-14): CONJECTURE NF-Z holds relative
to the promoted consumer set, with the quotient data computable per
entry — NEW RESULT, UNREVIEWED.** Statement, proof, td-7/11-A
specialization checks, and trust perimeter below. Sources:
`xmodel/sol-normalform.md` §§0–3 (the fat record, cylinder (2.5), the
NF-Z statement), `xmodel/grok-normalform-review.md` (findings 1, 2, 5 —
the fifth-pair obstruction, the nu=1 nuance, why fat-state enumeration
cannot certify emptiness), `TOWER-UNIFORM.md` (the promoted ladder
calculus and N1–N4, of which this is the generalization). No git
commit.

## 0. Setting and the objects

Fix `td`, an L6-surviving entry, a labelled hierarchy, and a bounded
non-neutral skeleton (Sol §2.1–2.2: finitely many such skeletons per
entry and budget). A **neutral word** is a finite sequence of cylinder
(2.5) cells inserted between two priced events at a state
`(w, M_0)`, `w = a/d` reduced:

```text
letter j:  (l_j, u_j),  l_j | M_{j-1},  u_j >= 2,
           d | u_j + 1  (vertex integrality),
           gcd(a, u_j) = 1  (BOOK-N1),
           M_j = gcd(l_j, u_j + 1),
frame:     (nu, kbar, rho)_j = (u_j, w(u_j+1), w),
degree:    P_j = P_0 * u_1 ... u_j       (P_0 = the poleward anchor),
price:     0 at every letter.
```

Per grok-normalform finding 2, `nu = 1` insertions are NOT in this
cylinder (N1 is scoped to `nu >= 2`; `px2` never emits them); if a
future convention admits them they are degree-preserving
(`P' = P`) and are a separate one-letter schema — noted in §5, outside
the word calculus proper. The letters' own local coefficient data is
the single parametric one-orbit Prop 8.1(iv) solve

```text
p = t - A, q = eta(t - A),  C = -(d_p/d_q) A = -(u/(nu-tail)) ... :
concretely C = -nu*A/(n*nu+1)|_{n=1} = -u A/(u+1),
```

one closed form for the whole family (the promoted N/X rows of the
tower certificates are instances) — call this **Lemma Z-Omega**; it is
what NF-M consumes for neutral letters.

**Futures** are labelled as in Sol §0: price/terminal budget, arrival
vertex + E5F offset and reroutes, merge multiplicities and full-degree
synchronization (H8/equal quotient), and every tower predicate of the
promoted ladder calculus (death gaps `kbar/D_f`, delta descent
`delta_g(v) = D_v g - kbar_v in N`, death equations
`g_m = kbar/D_f`, mu-recursion `alpha' = alpha + (k-1)l/k` with
`k_v = i_v(alpha_m - 1) in N`, aliveness `(h^+)^k = sigma (f^+)^l`
with integral factor exponents, count monotonicity, N1–N4). This
consumer list is the **promoted consumer set** `CONS`; the theorem is
relative to it (§6).

## 1. What a neutral word can touch (the Markov-bounded audit)

Against the fat record (1.2) of `sol-normalform.md`, a neutral word
touches exactly:

| field | touched? | how |
|---|---|---|
| `chi`, `L` (context, budget) | **NO** | every letter has price 0, no charge atom, no cv inventory |
| frame | endpoint only | `(nu, kbar, rho, M) = (u_r, w(u_r+1), w, M_r)`; `w` invariant |
| `C` (last cell) | endpoint only | the last letter `(l_r, u_r)` |
| `A` (arrival witness) | endpoint only | the endpoint is the only new arrival candidate; its pads are further letters |
| `S` (scale) | product only | `P_r = P_0 * Pi`, `Pi = u_1...u_r` |
| `Theta` (tower atoms) | **every letter** | atom `(P_j, gap_j = (u_j+1)/P_j, exponent P_{j-1}, delta data)` |
| `Omega` (coefficients) | one schema | Lemma Z-Omega, parametric in `(u, A)` |

So completeness reduces to two questions: (a) do the non-`Theta`
consumers factor through finite data plus the symbolic product; (b)
does the `Theta` (ladder) consumer factor through finite data. (a) is
§3; (b) is §4 — the actual content, and exactly grok-normalform
finding 1's "fifth pair" obstruction.

## 2. The quotient data (the invariants)

For fixed `(td, entry, hierarchy, skeleton)` define

```text
I(word) = ( tau,            # the M-ledger: the chain M_0 ) M_1 ) ... in the
                            # divisor poset, with letter positions of drops
            W_theta,        # the exact WINDOW ZONE: the (bounded) prefix of
                            # letters whose gap (u_j+1)/P_j >= theta, each
                            # letter kept as a parametric symbol with its
                            # residue-class domain
            u_r,            # endpoint characteristic: parametric, domain =
                            # finitely many classes mod lcm(d, divisors of M)
            Pi,             # the product: ONE symbolic parameter, domain =
                            # the letter semigroup, PLUS its finitely many
                            # consumer projections: residues mod m*, p-adic
                            # valuations for p | m*, and the bound Pi >= 2^r
            sigma )         # the deep-zone interface state: residues mod m*
                            # of (previous letter, running product) plus the
                            # ledger position -- an element of a FINITE set
```

where `theta` is the skeleton-computable window threshold (the smallest
death gap of any non-word competing vertex, td-7 instance: `2/5`), and

```text
m* = lcm( d, a, divisors of M_0, den(rho_x) and factor-exponent gcds
          c_x over the finitely many skeleton vertices x, P_0 )
```

is the **interface modulus** — an explicit, entry-computable integer.

**The schema set** = (finitely many M-ledgers) x (finitely many
window-zone shapes) x (finitely many endpoint/domain descriptors) x
(finitely many sigma values). Concatenation is closed: ledgers
concatenate in the divisor poset; window zones re-truncate under the
product action (`P` shifts by the left factor's `Pi`, and thresholding
commutes with that shift); `Pi` multiplies (semigroup); `sigma`
composes as a transition-monoid element (§4). This is the "closed
concatenation operation" NF-Z demands.

## 3. Completeness for the non-ladder consumers (unconditional)

* **Price/budget (P0, P1).** Word-blind: zero cost, no atoms (§1).
* **Endpoint frame and E5F.** The frame is `(u_r, w(u_r+1), w, M_r)`.
  The E5F offset at a next merge `(kbar_G, nu_G)` is affine in `u_r`:
  `n = u_r kbar_G - nu_G w (u_r + 1)`, so legality (`n >= 1`) plus the
  offset value are exact functions of the parameter `u_r`; every
  cost-coupled reroute is a further letter, i.e. stays inside the
  calculus with domains as in §0 (this is TOWER-UNIFORM Lemma E5F's pad
  closed form, verbatim: `n = ((u+1)X - mu0 kbar_G)/mu0`).
* **H8 / equal quotient / scale.** These read `P_r = P_0 Pi` exactly;
  `Pi` is retained symbolically (never truncated), and the promoted
  uniform kills consume only its projections: parity/valuations
  (11-A's `v_2`), residues (cap congruences), and growth (`>= 2^r`) —
  all in `I`.
* **M and terminal data.** `M_r` from `tau`; `w` invariant; P1 reads
  `(w, M_r)` only.
* **Coefficients.** Lemma Z-Omega: one parametric certificate; no two
  distinguishable coefficient futures are identified (the solve is
  unique per letter and carries no free coefficient beyond `A`).

## 4. Completeness for the ladder consumer (the theorem's core)

Grok's fifth pair (`(3,5,7)` vs `(5,3,7)` at `w = 2`: same endpoint,
same product, different intermediate atoms) shows the atom LIST cannot
be replaced by max-gap + product. The resolution is that the ladder
calculus itself collapses the deep atoms. Three exact identities:

**(Z1) The alpha-exit identity.** When a ladder level dies at gap
`gamma` with step `(k', l')` (death equation
`l'/k' = gamma + alpha - 1`), the mu-recursion gives

```text
alpha_next = alpha + (k'-1) l'/k' = l' + 1 - gamma .
```

*(Verified on the td=6 template: after F_s's level-2 death,
`alpha_3 = 23 + 1 - 5/42 = 1003/42`, equal to the recursion value.)*

**(Z2) The difference-denominator lemma.** For two consecutive deaths
at gaps `gamma`, `gamma'`, (Z1) gives
`l''/k'' = gamma' - gamma + l'`; hence `k''` is the reduced denominator
of `gamma' - gamma` — the unbounded exit-alpha denominators cancel
pairwise. For consecutive WORD deaths,

```text
gamma_{j+1} - gamma_j = (1 - u_j u_{j+1}) / P_{j+1},
```

and since `gcd(u_j u_{j+1} - 1, u_j) = gcd(u_j u_{j+1} - 1, u_{j+1})
= 1`,

```text
k'_{j+1} = P_{j+1} / gcd(u_j u_{j+1} - 1, P_{j+1})
         = (u_j u_{j+1}) * P_{j-1} / gcd(u_j u_{j+1} - 1, P_{j-1})
         >= u_j u_{j+1} >= 4 .
```

*(Numerical check: `P_0 = 2`, word `(3,5)`: `den(1/5 - 2/3) = 15 =
30/gcd(14,30)`.)*

**(Z3) Word deaths are forced and ordered.** Every non-pole vertex has
`m_v` finite (Prop 4.2 delta descent hits 0), so every word vertex
hosts exactly one ladder death, at its own gap
`gamma_j = (u_j+1)/P_j`; and `gamma_{j+1}/gamma_j =
(u_{j+1}+1)/(u_{j+1}(u_j+1)) <= 1/2`, so the word's deaths occur in
word order with geometrically decreasing gaps — at most
`log_2(3/(2 theta P_0))` of them lie in the window zone (the
generalization of N4), and the zone's letters have bounded prefix
product `P_{j-1} <= 3/(2 theta)` (though the letter `u_j` itself stays
parametric — the td-7 `X`-family).

**Aliveness caps.** A level dying at word vertex `v_{j+1}` must be
alive at every vertex with a smaller death gap (rootward of it in the
ladder order): the rootward word vertices contribute exponent cap
`k' | P_{j+1}` — automatic by (Z2) — and the skeleton vertices still
alive contribute their factor-exponent gcds, all divisors of the fixed
`c_x`-data in `m*`. Window-zone deaths additionally face the
*other-branch* small-`i` caps (the td-7 `k | 2`); deep-zone deaths face
the rootward-context integrality conditions instead:

**Deep-zone congruences.** For word levels, integrality of the
mu-recursion and delta laws at each still-alive vertex `x` reduces,
after (Z1)–(Z2) cancellation, to finite-modulus conditions: e.g.
`k_{v_j} = i_{v_j}(alpha_j - 1) in N` is exactly
`l_j | u_{j-1} + 1` (modulus `<= M_0`); `delta_{gamma_j}(x) in N` is a
residue condition on the product ratio `P_x/P_j` modulo `den(rho_x)`;
the death-step compatibility is a residue condition on
`u_j u_{j+1} - 1` modulo divisors of `m*`. **Every one of these
conditions reads only: the previous letter's residues mod `m*`, the
running product's residues mod `m*`, and the ledger position.** That
data is the interface state `sigma` — an element of a finite set of
size at most `m*^2 · |divisor poset of M_0|` — and each letter acts on
it by an explicit map. The word's entire deep-zone ladder effect is
therefore an element of the **finite transition monoid** generated by
the letter classes (the monoid Sol's NF-Z asked to be exhibited), and
the exported interface (the alpha entering the post-word context) is
`alpha_exit = l'_r + 1 - gamma_r`, a function of `(u_r, Pi)` — already
invariants.

**Theorem NF-Z (relative form).** *For fixed
`(td, entry, hierarchy, skeleton)`, two neutral words with equal
invariants `I` (§2) — same ledger, same window-zone schema and
parameters, same endpoint parameter, same product as a symbolic value,
same interface-monoid element — have identical labelled futures for
every consumer in `CONS`. The invariant set is finite as a schema set
(finitely many ledgers, zone shapes, domains, monoid elements), with
`Pi` and the zone/endpoint letters retained as exact symbolic
parameters over finite residue-class domains, and concatenation is
closed.* Proof: §1 bounds the touched fields; §3 handles the
non-ladder consumers; (Z1)–(Z3) + the cap/congruence analysis show the
ladder verdict and all its labels are functions of `I`; closure of the
monoid is closure of residue arithmetic mod `m*`. QED (relative to
`CONS`; see §6).

**Corollary (neutral-depth rigidity — the surprise).** In the window
zone, the death-step denominators `k'_{j+1} >= u_j u_{j+1} >= 4` must
divide the small other-branch caps `c_0`; hence if `c_0 < 4` no
interior window death exists at all, and generally
`u_j u_{j+1} <= c_0` with the letter congruences — for many entries
this makes long window-zone words tower-dead outright, the exact
mechanism of the td-7 kill. Deep-zone words are constrained by the
finite congruence system instead of a length bound; solvable words
correspond to accepting paths of the automaton, and emptiness of a
schema is decidable (finite monoid).

## 5. Specialization checks

**td-7 (TOWER-UNIFORM N1–N4 falls out).** Entry data: chain-1 anchor
`P_0 = 2` (`w = 2, M = 1`: ledger trivial, `l = 1`, N1 = the letter
domain `gcd(2, u) = ...` wait — at `w = 2 = 2/1`: `d = 1`, BOOK-N1
`gcd(kbar, nu) = gcd(2(u+1), u) = gcd(2, u) = 1` forces `u` odd = the
domain description); chain-2 pre-first-charged `P_0 = 4`
(`w = 3/2, M = 2`: `d = 2 | u+1` — odd `u` again = **N2**, i.e. the
`v_2(Pi) = 0` projection). **N1** (state-preservation forces `n = 1`)
is the cylinder membership itself. **N3** (joint cap
`gcd(4, 2 P_pre) = 2`) is the window-zone aliveness cap with the
first-letter exponent `P_0 = 4` and the other-branch charged cap
`2 P_pre` — the `c_0`-data of §4. **N4** (`(u+1)/(D_prev u) <= 3/8`)
is the `gamma_j`-decay bound anchored at `P_0 >= 4`. The td-7
window-zone schema is the single parametric letter `X` with gap
`(u+1)/(2u)` and universal-`u` refutation — exactly the
`W_theta`-schema at `theta = 2/5` with zone length 1; the three-case
exhaustion is the emptiness decision for that schema's automaton. The
kill's `u_j u_{j+1} <= c_0 = 2 < 4` instance is the corollary above.

**11-A (the 2-adic certificate).** The strict branch's neutral words at
`(w, M) = (2, 1)` have domain `u` odd, so the `Pi`-projection
`v_2(Pi) = 0` gives `v_2(P_1) = v_2(2 Pi) = 1`; the resonance branch
exports `v_2 = 3` (`+ v_2(A) >= 0` for prefix pads). H8 equal quotient
reads exactly these two projections and emits
`H8_EQUAL_QUOTIENT_VP_MISMATCH` — the `p = 2` component of `sigma`,
no enumeration of the odd family (Sol §4.3 verbatim).

## 6. Trust perimeter and honest residue

* **Relative to `CONS`.** The proof enumerates the promoted consumer
  set (Sol's fat-record §1.2 checklist + the TOWER-UNIFORM ladder
  calculus: Prop 4.2 ladder/delta/aliveness, Prop 8.1(i)–(v), Cor 6.1,
  counts St 3.9/3.17(i)/3.11(i), E5F, H8, N1–N4, P0/P1). A future
  consumer outside `CONS` (e.g. a jet/coefficient predicate beyond
  Lemma Z-Omega's family, or chart data of milestone-2 gluing) re-opens
  the §1 audit for its fields. This is the same trust shape as the fat
  record's own Markov theorem (grok-normalform finding 1: retention
  arguments are relative to the consumer list), made explicit.
* **Ladder-law perimeter.** (Z1)–(Z3) use the campaign tower
  formalization (calibrated on the td=6 template, quadruple-reviewed on
  td-7). The laws are per-vertex printed propositions, entry-generic;
  no td-7-specific constant enters the identities.
* **Entry-conditional data, not entry-conditional truth.** `theta`,
  `c_0`/`c_x`, `m*`, the domains, and the monoid are COMPUTED per
  entry/skeleton (finite closure computation = the compiler's
  NF-Z pass); the finiteness and completeness proofs are uniform. If a
  computed `m*` failed to stabilize the congruence moduli (not observed
  in any inspected instance, and excluded by the explicit modulus
  formula), that entry's NF-Z status degrades to the exact fat record —
  fail-closed, per Sol interface rule 6.
* **`nu = 1` insertions** are outside cylinder (2.5) and outside this
  proof (grok finding 2); if legalized they are one extra
  degree-preserving schema letter and belong to NF-P's `nu = 1`
  obligations.
* The corollary's kill mechanism is stated but not instantiated beyond
  td-7 here; per-entry kills still require their own certificates.

## 7. What NF-P and NF-M need from this result

* **NF-P** inherits the whole interface algebra: a pure-(b) letter
  (cylinder (2.6)) is one CHARGED letter with the same
  (Z1)–(Z2) death arithmetic (the identities never use price or
  `w`-preservation), frame update `w' = lw/e`, degree factor
  `(eps + l u)/l`, and residue-class domain; NF-P must add (i) the
  `w`-changing clean-resonance closure — pointwise numerator descent
  is promoted; the uniform symbolic closure is NF-P's own content —
  and (ii) the `nu = 1` merge schemas. The concatenation law of §2
  composes NF-Z summaries around each NF-P letter, so NF-P only ever
  handles ONE parametric charged letter at a time between NF-Z blocks.
* **NF-M** consumes Lemma Z-Omega (neutral letters have one parametric
  coefficient type — proved here), reducing NF-M's scope to
  multi-orbit/mixed/`nu = 1` merge ODEs exactly as Sol stated; and the
  finite-monoid format of §4 is the shape its "finite computable
  certificate type" should take.

## 8. Reproduction of the verified identities

The three load-bearing identities were machine-verified during
construction (exact `Fraction`): the alpha-exit identity on the td=6
template (`alpha_3 = 1003/42` both ways); the difference-denominator
computation `den(1/5 - 2/3) = 15 = P_2/gcd(u_1 u_2 - 1, P_2)` at
`P_0 = 2`, word `(3,5)`; and the td-7/11-A specializations of §5
against the promoted TOWER-UNIFORM gate values (`n` offsets, `v_2`
projections, N2–N4 constants). A compiler-grade `nfz_check.py` (schema
enumeration + monoid closure per entry) is the natural next artifact
once NF-P fixes the charged-letter interface it must compose with.
