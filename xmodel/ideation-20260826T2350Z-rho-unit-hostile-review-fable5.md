# Hostile review — rho-unit certificate calculus (Opus 5 lane, 20260826T2350Z)

Round: `20260826T2350Z`
Reviewer: Fable 5, adversarial algebraic-geometry review, post-blind phase
Date: 2026-08-26

Verdict: **REPAIRABLE.**

- Lemma 3.1 as stated: **CONFIRMED EXACT** (full re-derivation, §2, including
  the zero-divisor, covering, and universal-property fine print).
- The three claimed obligation removals — special-fibre base-change equality
  (2.5), pairwise overlap/gluing, nilpotent analysis — are **legitimately
  removed from the emptiness/arc-exclusion endpoint, and only from it** (§4).
- The claim that the promoted `T-rs` identity is "literally of this shape"
  (*) is **false as written**: `T-rs` instantiates a *localized,
  presented-ring* variant that Opus never states (§3).  The §3.3 certificate
  type **cannot express the one promoted certificate it is modeled on**
  without falsely registering the exceptional coordinate `rs` as a unit —
  the exact hazard verifier step 4 exists to refuse (§5).
- Root's `PROJ-IRR` irrelevant ideal `B=(rs,cs,c0,c1,a0,a1)` is **mistyped**
  for the staged `J1`-then-`J2` construction and **needs replacement** by a
  staged pair; its pigeonhole and power-containment mechanics are sound (§7).
- Minimal corrected lemma: §6.  Removed/retained ledger: §8.  Cleanest next
  exact discriminator: §9.

Per instruction, every broad JC2 claim is treated as false unless proved
here; nothing below proves any chart empty beyond the charged `T-rs` scope.

## 0. Charged inputs, tool boundary, execution gaps

Read in full, rehashed this session:

```text
43adf31727136c68c3f2ce1f8465517382262d0d5e04493a00bf49d101bac4b9  ideation-20260826T2350Z-opus5.md
50db2706f5a8d435618e615bfc393d2eb7dd22828a9a3fa35ac8a2e685ab15c4  max12-812-order2-p0-total-rees-gate-t-obligation-table-20260826.md
6995a991b1e7803a26bbf5374b10d54a0cda7d17158ad9f1595db76218aadb92  cross-iterated-blowup-cech-valuative-propagation-20260826.md
52b59e8d546b9996160c1262e1dcf9b5f0434992882128cc18dc7258881ee783  max12-812-order2-p0-total-rees-t-rs-rho-unit-v16-promotion-sol-20260826.md
c67a78e135ec3bffc3e1884513f8e20ac3cfe9b6db661ff95b3a7393f7209f58  ideation-20260826T2350Z-root.md
```

Cross-checks: the coverage theorem's hash equals the citation in the
obligation table §1, and the `T-rs` promotion's hash equals Opus §1's
`52b59e8d...` citation.  Both provenance chains are intact.

Boundary: no web, no AWS mutation, no `jc2-lean`, no heavy computation;
local tool use was one `shasum` invocation.  All verdicts rest on hand
algebra reproduced below plus frozen attestations.  Execution gaps:

- I did **not** re-expand the `T-rs` identity against the four hash-pinned
  V9 row files and did not open any case artifact.  The polynomial expansion
  is CHARGED to the promoted hostile review (`b32de58c...`, `CONFIRMED`).
  What I verify here is the promotion's complete internal algebra and its
  exact compatibility with the frozen specialized cusp identity — the
  strongest checks available without the row files, and independent of them.
- Whether the grade `<=12` total rows involve `a0,a1` is not determinable
  from the charged `.md` set; flagged where it matters (§7).

Labels: **EXACT** (proved here), **CHARGED** (repository attestation),
**GAP** (not verifiable this session).

## 1. Summary of findings

The calculus's core is correct: Lemma 3.1 is exact, and its reading of what
Gate T's *emptiness* endpoint does and does not require is right.  Opus also
correctly distinguishes, in his own §§3.2(b)–(d), the retained obligations
(provenance, terminal receiver, localizer strata, deck/square bridge) from
the removed ones; on the central question this submission is honest and
sound.  The defects are at the instantiation and type level, and they are
load-bearing for the five searches the calculus proposes to launch:

1. `T-rs` does not satisfy (*) as literally stated (extra non-unit factor
   `k`; relation list is divided source-row transforms, not the bilinears).
2. The §3.3 type's `s in S` slot conflates two objects with different
   geometric costs: exceptional powers `f_i^N` (absorbed free by
   saturation) and genuine localizers (which cost a residual closed
   stratum).  As written it cannot express `T-rs`.
3. Root's single irrelevant ideal `B` types no charged object.
4. Minor overstatements: "certified finite decisive prefixes" (they are
   design expectations); Card A's "there is no null outcome" (a bounded
   failed search with no proven non-membership witness is null).

All four are repairable without touching the architecture; §6 is the
corrected lemma the next producers should target.

## 2. Lemma 3.1 is exact — re-derivation with the fine print  [EXACT]

Setup: `A` any commutative ring, `rho in A`, `I=(f_0,...,f_n)`,
`S = Rees_A(I) = A[It] subset A[t]`, `X = Proj S`.

**(2a) Chart ring.**  `(S_{f_i t})_0`: a degree-zero fraction is
`a t^m/(f_i t)^m = a/f_i^m` with `a in I^m`, computed inside
`S_{f_i t} subset A[t]_{f_i t} = A_{f_i}[t,1/t]` (localization is exact on
the subring inclusion).  Hence `C_i = A[I/f_i] subset A_{f_i}`, the
`A`-subalgebra generated by the `f_j/f_i`.  Valid when `f_i` is a zero
divisor; if `f_i` is nilpotent, `A_{f_i}=0`, `C_i=0`, and the saturation
below is the unit ideal.  This confirms the obligation table's (2.1).

**(2b) Kernel = saturation.**  Let `phi: A[y_j] -> A_{f_i}`,
`y_j -> f_j/f_i`, and `P_i = (f_i y_j - f_j)`.
`(P_i : f_i^infty) subset ker phi`: generators die, and `f_i` is invertible
in `A_{f_i}` so an `f_i`-power multiple of a kernel element forces the
element into the kernel.  Conversely, for `g in ker phi` of degree `d`,
reduction mod `P_i` gives `f_i^d g ≡ c in A` (replace `f_i^{|α|} y^α` by
`f^α`); `phi(g)=0` forces `f_i^M c = 0` in `A`, so
`f_i^{M+d} g in P_i`.  Hence `ker phi = (P_i : f_i^infty)` exactly — the
obligation table's (2.3) — and the Rabinowitsch elimination (2.4) computes
the same ideal.  **Confirmed in full generality.**

**(2c) Covering.**  `S` is generated in degree one by the `f_i t`; a
homogeneous prime containing every `f_i t` contains `S_+`.  So the
`Spec C_i` cover `X` by construction.  Chartwise emptiness of the `rho`
fibre is therefore global emptiness; no transition data enter.

**(2d) Saturation inference.**  From (*):
`f_i^{N_i}(1+rho W_i) in P_i` gives `1+rho W_i in (P_i:f_i^infty)`, so
`1 in (P_i:f_i^infty)+(rho)` and `C_i/rho C_i = 0`.  Correct.

**(2e) DVR consequence.**  For `phi: A -> R`, `R` a DVR, `IR != 0`: `IR` is
a nonzero finitely generated ideal of a DVR, hence principal and
invertible; the universal property of blowing up (valid for any scheme and
finite-type quasi-coherent ideal — no noetherian hypothesis needed, so the
lemma's bare "commutative ring" is fine) lifts the arc uniquely to `X`.
`ord_R(rho)>0` puts the closed point's image in `V(rho)`, so the lift's
closed point lies in the empty fibre.  The degenerate case `phi(rho)=0`
(`ord = infty`) is excluded a fortiori.  Correct.

**(2f) Two bonuses Opus does not state, both favorable.**
(i) `C_i subset A_{f_i}` and multiplication by `f_i` is injective on
`A_{f_i}`, so **`C_i` is `f_i`-torsion-free**: absorbing `f_i`-powers costs
nothing and no stratum.  This is what licenses the `rs^2` in `T-rs`.
(ii) (*) requires membership only in the **unsaturated** `P_i`, and
`P_i subset (P_i:f_i^infty)`: the symmetric-vs-Rees torsion gap points the
favorable way for emptiness.  A certificate found against the naive
presentation is automatically valid for the actual Rees chart.

**Lemma 3.1: CONFIRMED.**

## 3. Does `T-rs` instantiate the lemma?  Yes — but not "literally"

The promoted identity (`52b59e8d...`) is

```text
35*rs^2*k*U = 32768*P126 + 4096*P2 + 8192*qcs*P3 + 12288*rho^2*qcs*P1,
U = 1 + 32*rho^2*qcs^2*(8*rho^2*qcs^2+3),
```

over the chart polynomial ring with `P_j = Tg10_j/rs` (`j=1,2,3`),
`P126 = Tg12_6/rs^2` — divided source-row transforms, `rs`-valuations
`(1,1,1,2)` per the charged review.  Against (*):

- the relation list is **not** the bilinears `f_i y_j - f_j`: it is the
  transformed source rows;
- the left side carries an extra factor `k`, which is **not** covered by
  any slot of (*).

**Bridging identity [EXACT, given row provenance].**  Substituting
`cs = rs*qcs`, `c0 = rs*qc0`, `c1 = rs*qc1` is reduction modulo the
bilinear ideal, so `rs*P_j ≡ Tg10_j` and `rs^2*P126 ≡ Tg12_6` modulo the
bilinears in the presentation ring.  Multiplying the promoted identity by
`rs^2` and using `rs*qcs ≡ cs`:

```text
35*rs^4*k*U ≡ 32768*Tg12_6 + 4096*rs*Tg10_2 + 8192*cs*Tg10_3
             + 12288*rho^2*cs*Tg10_1        (mod bilinears).
```

That is `rs^4 * (35k) * (1 + rho*W) in (bilinears) + (source rows)`:
exactly the **localized presented-ring form** of the lemma (§6) with
`N=4`, localizer `s = 35k`, and the source rows adjoined to the relation
list.  The `rs^4` is absorbed free by §2(f)(i); the `k` is a genuine
localizer (or a family-registered unit — see the naming note below); the
conclusion is emptiness of the chart's `rho` fibre **on `D(k)`**, which is
precisely the promotion's stated scope.

**Hand checks passed [EXACT]:**

1. **`rho = 0` reduction.**  `U ≡ 1 (mod rho^2)` and the `12288`-term dies,
   leaving `32768*Tg12_6^0 - 35*k*rs^4 = -4096*rs*Tg10_2^0 - 8192*cs*Tg10_3^0`
   — verbatim the frozen specialized cusp identity of obligation table §5.4
   (`32768*g12_6 - 35*k10*rs^4 = -4096*rs*g10_2 - 8192*cs*g10_3`) under
   `Tg^0 <-> g`, `k <-> k10`.  `T-rs` delivered exactly the lift §5.4
   demanded, sign-exact.
2. **`rho^2` sentinel (table §5.4).**  Every newly introduced total term is
   divisible by `rho^2`: the `12288*rho^2*qcs*P1` term and
   `U - 1 = 32*rho^2*qcs^2*(...)`.  Sentinel satisfied.
3. **Promotion internals.**  `U ≡ 0` on the localized quotient gives
   `1 = 1-U = rho*(-32*rho*qcs^2*(8*rho^2*qcs^2+3))`, the printed
   `rho^{-1}`; `k*U in J` gives `k in J+(rho)`; adjoining `1-v*k` gives the
   unit ideal.  All check.
4. **Cross-file arithmetic.**  Cross §4's (4.1): from `5*k0*rs^3 = -96*c1^2`
   and `row(6,12) = -(21/1024)*rs*c1^2`, one gets
   `(21*5)/(1024*96) = 105/98304 = 35/32768`, so
   `row(6,12) = (35/32768)*k0*rs^4`.  Confirms the constant.

**Defects [EXACT]:**

- Opus §3.2(a): "The already promoted `T-rs` lemma is literally of this
  shape."  False as written, on two counts (relation list; `k`).  The
  repair is a restatement, not a retraction — the promotion itself is fine
  and its scope discipline (saturate `rs`, localize only `k`) is *cleaner*
  than both the older cross-file language ("registered factors `k0*rs`",
  which treats `rs` as a localizer — wrong on the total chart, where `rs`
  is the exceptional equation and the fibre of interest lies on `rs = 0`)
  and Opus's own §3.3 type.
- **Naming drift [GAP/nit].**  The same coefficient appears as `k0`
  (cross §4), `k10` (table §§1,5), `k` (promotion).  Under the family's own
  name ("post-`M=0`, unit-`k10`") `k` is a registered unit of the source
  and `D(k)` is scope-free, with the `k10=0` case a firewalled sibling
  family; under the literal promotion text `V(k)` is a residual chart
  stratum.  Either filing leaves the same total debt; the ledger should pin
  one name and one filing.  Opus §3.2(d) lists "`V(k)`, `V(k10)`" as if two
  strata — likely a double count.
- **Row provenance [CHARGED, retained].**  The four V9 rows are hash-pinned
  but not re-extracted from the total emitter; the promotion's own firewall
  says so.  The bridging identity above is conditional on that provenance.

## 4. The three removals are legitimate — for emptiness only  [EXACT]

**(4a) Base-change equality (2.5).**  For any `g` with `f_i^M g in P_i`,
reduction mod `rho` gives `f̄_i^M ḡ in P̄_i`; hence always

```text
(K_i^tot + (rho))/(rho)  subseteq  K_i^0,
```

so there is a canonical surjection `C_i^tot/rho ->> C_i^0`: the specialized
blowup chart is a closed subscheme of the total special fibre.  Degree-`n`
kernel of `Rees_A(I) ⊗ A/rho ->> Rees_{A/rho}(Ī)`:
`(I^n ∩ (rho))/rho*I^n` — confirming Opus's Valabrega–Valla criterion
exactly as stated.  Consequences, all as Opus types them:
total emptiness ⟹ specialized emptiness (**necessary screen**);
the converse fails — one-line witness: `A = k[rho,u]`, `I = (rho*u)`:
the specialized ideal is zero, so the specialized blowup is `Bl_0 = ∅`,
while the total blowup is `Spec A` (Cartier divisor) with nonempty `rho`
fibre, and the degree-`n` kernel `(rho^n u^n)/(rho^{n+1} u^n) != 0` names
the torsion.  A direct total certificate needs no comparison at all.
**(2.5) equality is legitimately removed from the emptiness endpoint;
specialized endpoints are retyped as screens/negative controls.**  Note
what this does *not* do: it discharges nothing — every MISSING row now
requires a new total certificate instead of a comparison.  Opus's Card A
says this correctly; his §2.1.4 summary line is lossy but not wrong.

**(4b) Overlaps.**  (i) Full charts: covering is tautological (§2c) and
emptiness is local; no gluing.  (ii) Ordered strata: a point of `Proj` has
a least `i` with `f_i t` outside its prime; for `j<i` the ratio
`y_j = f_j t/(f_i t)` vanishes there.  So the strata
`V(y_j : j<i) ∩ D_+(f_i)` cover set-theoretically; and since on chart `i`
one has `f_j = f_i*y_j`, `V(y_j) subseteq V(f_j)`, the base-function strata
`V(f_j : j<i) ∩ D_+(f_i)` (the obligation table's naming, matching how the
frozen specialized endpoints were built) are larger and also cover.  A
scheme with empty underlying space is empty, so set-theoretic covering
suffices for the emptiness endpoint; the DVR routing is even exact
stratum-wise (an arc routes to the least index attaining the minimal
valuation, and for `j` below it, `ord(f_j/f_i) > 0` puts the closed point
in `V(y_j)`).  What survives of table §6 is **provenance**: the
certificate's relation list must be *proven* members of the honest stratum
ideal (images of total rows + bilinears + stratum generators).  Certifying
against a larger unproven ideal would be unsound; against the honest or
any smaller one is safe — "similar-looking Laurent receivers are not
enough" is retained verbatim.  **Overlap isomorphisms and scheme-theoretic
restriction maps are legitimately removed from the emptiness endpoint;
the residue is a generator-level provenance check.**

**(4c) Nilpotents.**  `1 in J` is insensitive to scheme structure, and by
§2(f)(ii) the certificate may even target the unsaturated presentation.
**Removed from the emptiness endpoint.**  Retained exactly where Opus
retains it: the terminal receiver's own analysis and the deck/square
comparison are not emptiness statements.

## 5. The §3.3 certificate-type defect  [EXACT]

The type validates `s^N * U == sum H_j Phi_j` with "`s in S` # registered
units".  For `T-rs` the left factor is `35*rs^2*k`; `rs` is not a unit on
its chart (it is the exceptional equation) and must never enter `S`; it is
absorbed by the free saturation.  As written, the type either cannot
express the flagship promoted certificate or forces a false unit
registration of `rs` — precisely the "unregistered factor inverted"
failure mode Opus's own verifier step 4 exists to refuse (the `K = 2R38`
incident class).  The obligation table §3's certificate form
(`s = sum H_i*Phi_i + rho*H`, "only registered chart units in `s`") has the
same conflation.  Repair (folded into §6): three separated slots,

```text
f_i^N        exceptional power — free, no stratum cost (§2f(i));
s in S       registered localizer — costs the residual stratum V(s),
             or is a family-registered unit of A (then no stratum);
U ≡ 1 mod rho.
```

plus a stratum-generator list (ordered form) and a stage tag (`J1` chart
over `A` versus `J2` chart over `A/J1`).  Verifier steps 2–4 then check the
right identity and the ledger emission in step 5 becomes forced rather than
optional.

## 6. Minimal corrected lemma

**Lemma (localized rho-unit chart certificate, presented staged form).**
Let `R` be a commutative ring, `Q subset R` an ideal (source relations),
`A = R/Q`; let `rho, s in R`, and `I = (f_0,...,f_n) subset A` with chosen
lifts to `R`.  Let `X = Proj Rees_A(I)`.  Fix `i` and ratio variables
`y_j` (`j != i`); fix a subset `E ⊂ {j : j < i}` of earlier indices
(empty for the full-chart form).  Suppose in `R[y]`:

```text
f_i^N * s * (1 + rho*W)
  = sum_j H_j*(f_i*y_j - f_j) + sum_m G_m*q_m + sum_{j in E} L_j*z_j   (*_s)
```

with `z_j in {y_j, f_j}` (ratio or base-function stratum form).  Then

```text
D_+(f_i) ∩ V(z_j : j in E) ∩ (X ×_A V(rho))  subseteq  V(s).
```

If certificates `(*_{s_i})` exist for a stratification covering all `i`
(least-index strata with either `z`-choice cover set-theoretically), then
`X ×_A V(rho) subseteq ∪_i V(s_i)`, and every morphism `Spec R' -> Spec A`
with `R'` a DVR, `I*R' != 0`, `ord(rho) > 0` lifts uniquely to `X` with
closed point in the `V(s_i)` locus of its least-minimal-valuation stratum.
If each `s_i` is invertible in `A` (family-registered units), no such
morphism exists.  **Staged form:** apply to `(A, J1)` and to
`(A/J1, J2)`; morphisms with `(J1+J2)R' = 0` factor through the terminal
receiver `V(J1+J2)` and are untouched.  **Homogeneous equivalent (per
chart):** `s*f_i^{N'} in rho*I^{N'} + Q` (degree-`N'` part, in `R`) for
some `N'` ⟺ the same localized chart-fibre emptiness.

*Proof.*  All ingredients are proved above: (2b) kernel = saturation and
(2f)(i) free absorption of `f_i^N`; localization at `s` commutes with the
quotient; (2c)/(4b) covering, in both `z`-readings; (2e) DVR lift and
least-index routing; the staged trichotomy is the charged iterated theorem
(`6995a991...` §2).  For the homogeneous equivalence: from `(*_s)`, clear
the saturation and homogenize `W` to get `s*f_i^{N'} - rho*(deg-N'
combination of f-monomials) in Q`; conversely divide by `f_i^{N'}` in
`C_i` to get `s in rho*C_i`, i.e. `1 in rho*C_i[1/s]`.  ∎

Lemma 3.1 is the special case `Q = 0` (or `Q` folded into `A`), `s = 1`,
`E = ∅`.  Every certificate the campaign has produced or planned (`T-rs`
with `N=4, s=35k`; the five pending charts; the stratum forms matching the
frozen endpoints) is an instance of the corrected statement; none but the
hypothetical `s=1` case instantiates the original.

## 7. Root's `PROJ-IRR`: mistyped; needs replacement  [EXACT]

**No charged object has irrelevant ideal `(rs,cs,c0,c1,a0,a1)`.**  Stage
one is `Rees_A(J1)` — four degree-one generators; stage two is
`Rees_{A/J1}(J2)` — two, over the receiver.  The staged construction is
two schemes plus a receiver, not one `Proj`.  Read instead as the single
blowup `Bl_{J1+J2}(X)`, root's `B` types a *valid but uncharged*
alternative geometry: its DVR dichotomy (`B*R' != 0` lifts; `B*R' = 0`
routes to the same terminal receiver) is sound, but its `rs`-chart carries
five ratios including `a0/rs, a1/rs`, so **the promoted `T-rs` certificate
does not automatically re-embed**: if any grade `<=12` row involves
`a0` or `a1`, the substitution changes the transforms and their
`rs`-valuations.  Not determinable from the charged `.md` set [GAP]; it
would have to be checked before any single-`B` founding, and root's card's
"no new Gröbner basis is needed for this gate" is unsafe as stated (the
card's own stop condition half-anticipates this, to its credit).

**Replacement (minimal, staged):**

```text
B1 = (rs,cs,c0,c1) over A:      s*b^{N_b} in rho*J1^{N_b} + Q   for each b;
B2 = (a0,a1)       over A/J1:   s*a^{N_a} in rho*J2^{N_a} + Q'  for each a;
pigeonhole (N = sum(N_b - 1) + 1, exact) per stage;
terminal receiver V(J1+J2) separate, untouched.
```

Each per-generator containment is equivalent to the corresponding
localized chart-fibre emptiness (§6, both directions proved), so the
repaired `PROJ-IRR` is exactly the homogeneous face of the corrected
lemma — root's instinct that "nilpotents are controlled by the power
containment itself" and that this replaces six unrelated radical verdicts
is correct *in the staged form*.  The `T-rs` certificate already yields a
mechanically extractable first input `k*rs^{N} in rho*J1^{N} + Q` (§9);
the pending `T-cs` lift is the second.  Root's `b_i^{N_i} in I + (rho)`
also omits the `s`-decoration; on `D(k)` scope it needs the same localizer
slot as everything else.

## 8. Obligation ledger

**Legitimately removed (emptiness/arc-exclusion endpoint only):**

1. Obligation (2.5): scheme-theoretic equality `K^tot+(rho) = K^0`, and its
   kernel/cokernel alternative.  Specialized endpoints retyped as necessary
   screens and negative controls.
2. Pairwise overlap isomorphisms and table §6's scheme-theoretic
   restriction-map demand.  Reduced to stratum-ideal provenance
   (generator-level).
3. Nilpotent/embedded-structure analysis in the special-fibre comparison;
   the saturation itself may be bypassed on the favorable side (§2f(ii)).

**Retained (unchanged by the calculus):**

1. The five chart certificates themselves (`cs`, `c0`, `c1`; `a0`, `a1`
   over `A/J1`) — retyped as bounded searches, not discharged.
2. The terminal receiver `V(J1+J2)`: routing case three; grade-38 window;
   no blowup consequence applies.
3. The localizer ledger: `D(k)` scope with its `k10=0` sibling family
   (naming to be pinned, §3), plus every future per-chart `s_i`.
4. Provenance: total-emitter extraction of every relation row (the `T-rs`
   promotion's own flagged upstream dependency); honest stratum ideals;
   the two-sided name maps to frozen clients.
5. The seven `A` source shards with the `ROUTE_CONSTANT_A` /
   `STAY_TANGENT` dichotomy: the stage-two receiver ring must retain shard
   moduli; zeroing later constant-`A` coefficients is not a cover.
6. The generic deck/square `D(rho)` bridge: a comparison obligation, not
   an emptiness one (cross §5.6); untouched, exactly as Opus says.
7. The finite-prefix side conditions (common bivariate emitter; every
   contributing term retained; restricted names).  The persistence lemma is
   exact, and the search is complete in the limit — a certificate over
   `A_full` descends to some finite `A_g`, since the defining identity
   involves finitely many relation multiples [EXACT] — but there is **no
   effective grade bound**: Opus's "certified finite decisive prefixes" are
   design expectations, and Card A's "there is no null outcome" is
   oversold.  A bounded failed search with no proven non-membership
   witness is a null outcome; the two-extension stop rule is the honest
   handling, and naming the obstruction requires actually running the
   Valabrega–Valla probe (first `n` with `I^n ∩ (rho) != rho*I^n`), which
   is a separate computation, not a byproduct of failure.

## 9. Cleanest next exact discriminator

**Preliminary, zero cost, do first:** re-express the promoted `T-rs`
certificate in the §6 type (`N=4`, `s = 35k`, stage tag `J1`, `E = ∅`,
relation list = four pinned rows + bilinears) and mechanically extract its
homogeneous containment `k*rs^{N} in rho*J1^{N} + Q`.  This validates the
repaired type against the only existing instance and supplies the first
staged `PROJ-IRR` input.  No search, no new mathematics.

**Primary discriminator: the grade-10 `c0` stratum certificate.**  Search,
by bounded linear algebra over the grade-10 coefficient module, for

```text
c0^N * s * (1 + rho*W) in (bilinears) + (stratum generators rs, cs)
                         + (grade-10 total rows)
```

on the `V(rs,cs) ∩ D_+(c0)` stratum (base-function form, matching how the
frozen `(3/32)c0^2` endpoint was built; the ratio form is licensed too and
either covers).  This beats Card A's odd-sheet grade-14 choice on Opus's
own terms: once specialized endpoints are retyped as screens, "smallest
chart with a *promoted* endpoint" is no longer the right selection rule —
the cheapest total search is, and that is grade 10, with the same template
serving `c1` immediately and the stratum slots of the corrected lemma
exercised for the first time.  Outcomes: a certificate closes two of the
five charts on their strata and gives the calculus its second instance and
first ordered-stratum instance; failure after the two-extension rule
triggers the Valabrega–Valla probe at the minimal possible grade — a named
obstruction only if the probe is run (§8.7).

## 10. Nonclaims and firewall

- Nothing here proves any chart, stratum, or receiver empty beyond the
  charged `T-rs` scope on `D(k)`.  No landing, Gate-T, order-two,
  maximum-twelve, or JC2 progress of any kind.
- The removal verdicts in §8 are conditional on the retained ledger; the
  corrected lemma proves nothing by itself.
- The bridging identity of §3 is conditional on the charged provenance of
  the four V9 rows; I did not re-extract or re-expand them (§0).
- Whether grade `<=12` rows involve `a0,a1` (single-`B` re-embedding, §7)
  is undetermined this session.
- This file is my only repository edit.
