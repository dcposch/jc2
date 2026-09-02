# Blind ideation submission — round 20260902T0741Z — lane fable51

Submitter: Fable 5.1 (blind, equal standing). Started 07:41:17Z. Packet
`ideation-20260902T0741Z-packet.md`, SHA-256 verified before reading:

```text
2646ac692c292c30597f9c830fd145c85e020207d803927825b8a162086055cf  ideation-20260902T0741Z-packet.md
```

Basis 8939320b. Read: the packet; APPROACHES.md (46 rows + overlays);
COORDINATION.md full-spectrum contract; the 0022Z synthesis; HORN-A2 r2
(one-cusp-a2-r2), RAY-KILL, N2-DERIVE, CELL-32 spec, HORN-FLAGSHIP,
MPRIME-ALLN-H2, HOMCOVER-TRANSFER, CASE-A-SWEEP, COMPANION-CURVE-ALLN,
theta-reopen (Sol 08-31), block-descent one-cusp structure (Sol 08-31),
integration #8, the two live lane prompts, the 07:25Z LIVE STATE. No other
lane's 0741Z submission was opened; the running web-sweep was not consumed.
Desk only: no CAS, no AWS, no literature fetch, no repository file edited
except this report. No `charge_basis` line: no exit price is asserted.

Typing used below: PROVED-HERE/UNREVIEWED (desk proof displayed);
DERIVED (routine consequence of promoted items); PROPOSED; MEASURED (none).

## 1. Headline — the gap framing is wrong in two places, for ONE reason

Both findings are consequences of a single elementary mechanism the campaign
uses only in fragments (ACS-FIX-VS-DEFICIT, LEMMA B3-LOC), never as a rule:

> **LOCAL-ISO TRANSPORT.** `F` is étale, so at every affine preimage `y` of a
> point `p ∈ A_F`, `F` is a biholomorphism from a neighbourhood `V` of `y`
> onto a neighbourhood `B` of `p`. Hence (i) the germs `(E,y)` and `(A_F,p)`
> are analytically isomorphic (`E := F^{-1}(A_F)`); (ii) `V \ E -> B \ A_F` is
> a homeomorphism and `V \ E` is a **whole connected component** of
> `F^{-1}(B \ A_F)` (closedness: if `y_n ∈ V\E`, `y_n -> y ∉ E`, then
> `y_n = (F|_V)^{-1}(F(y_n)) -> (F|_V)^{-1}(F(y)) ∈ V \ E`); so the degree-`N`
> unbranched cover `Y = C^2 \ E -> C^2 \ A_F` has a TRIVIAL SHEET over `B \ A_F`,
> and `rho(im(pi_1(B \ A_F) -> G))` FIXES that sheet.

### 1.1 THEOREM CUSP-A-ALL-N (PROVED-HERE/UNREVIEWED): case (A) is EMPTY at every N

Under H2, case (A) has `A_F ≅_{Aut(C^2)} {x^p = y^q}` (Lin–Zaidenberg, as HT
consumes it) and, by MPRIME Prop 6.1, the cusp `p_0` has `a_{p_0} = 1`: one
affine preimage `y_0`. The curve `{x^p=y^q}` is quasi-homogeneous, so for a
small weighted ball `B` around `p_0` the inclusion `B \ A_F ⊂ C^2 \ A_F` is a
homotopy equivalence (both are `(S^3_w \ T(p,q)) × interval`); hence
`pi_1(B \ A_F) -> G` is an ISOMORPHISM, not merely the map `iota` of HF §2.1.
By LOCAL-ISO TRANSPORT at `y_0`, `rho(G) = rho(pi_1(B \ A_F))` fixes the
`y_0`-sheet. `Y` is connected (complement of a curve), so `rho` is transitive
on `N` sheets. A transitive permutation group with a fixed point has `N = 1`.
Contradiction for `N >= 2`. ∎

Dependencies, all promoted: (M') via Prop 6.1 (`a_{p_0} = 1`); Lin–Zaidenberg
(already the case-(A) substrate in HT/CUSP-A-EMPTY); `F` proper over
`C^2 \ A_F` (definition of `A_F`, used verbatim in the CUSP-A-N8 charge).
Hostile checks the reviewer should run: (a) that Prop 6.1 really forces
`a_{p_0} >= 1` (if `a_{p_0} = 0` were admissible the theorem does not fire and
the sweep must be re-run with the fibre partition `(N)` over the cusp);
(b) the conical homotopy equivalence for `x^p = y^q` (standard, but it is the
whole load); (c) that no (B3) transfer is used — none is: in (B3) `A_F` is not
conical, `Loc_{p_0} -> G` is not surjective, and the fixed sheet is exactly
HF's affine orbit `|O| = 1`; the theorem is the case-(A) specialisation of
LEMMA B3-LOC plus surjectivity.

Consistency with the record: the N=8 trefoil survivors have
`rho(alpha) ~ (4,4)` — NO fixed point — so their fibre partition over the cusp
is `(8)`, i.e. `a_{p_0} = 0`, contradicting the Prop 6.1 value the sweep says
it consumed. The arsenal applied `a_{p_0} = 1` only numerically inside `(K)`,
never as "the local group at the cusp fixes a sheet". That is why 26 survivors
passed every homological gate: the killing gate is not homological.
Consequences if it holds: gap (c) CLOSED (no new N=8 gate is needed);
CONJECTURE CUSP-A-KAPPA is moot; OPEN[HOMCOVER-CUSP-A-N8] and
OPEN[MPRIME-CUSP-J2] CLOSED NEGATIVE at every N; THEOREM PROFILE loses row (A)
at all `N`: under H2 the all-degree residual is (B2) 5<=N<=16, (B3), and (B1)
at N>=17.

### 1.2 THEOREM PHI-IMMERSION (PROVED-HERE/UNREVIEWED): the A2 analytic model cannot carry the (B3) cusp

The A2 model is `S = Spec R`, `R = C[A,U,Z]/(U^2 - A - A^2 Z)`, with the first
map `iota : A^2 -> S`, `A = x^2, U = x + x^3 y, Z = 2y + x^2 y^2` (the
"retained cyclic chart"), and `pi = (f,g) : S -> A^2` étale (structure §1.2),
`F = pi ∘ iota`. Facts, each checked by hand here:

1. `iota` is étale and surjective; its Jelonek set is exactly `Phi = V(A,U)`:
   along `(x_n, y_n) = (eps, -2/eps^2 + c)`, `A -> 0`, `U = -eps + c eps^3 -> 0`,
   `Z = -2c + c^2 eps^2 -> -2c`, so every point of `Phi` is a limit from
   infinity (this is the structure report's "deleted source-boundary line
   `L_1`": the twin of `L_0 = {x=0}` escapes). No other limits exist.
2. Therefore `C_0 := pi(Phi) = closure{(f_0(Z), g_0(Z))} ⊆ A_F` (Jelonek
   composition: `A_F ⊆ A_pi ∪ pi(A_iota)` and `A_F ⊇ pi(A_iota)` by the
   sequence above), and `L_0 = {x = 0} ⊆ E`.
3. `E0` (the degree-0 Keller coefficient, (1.9) of the structure report)
   is `2(f_1 g_0' - f_0' g_1) = kappa`, so `(f_0', g_0')` never vanish
   together: `Z |-> (f_0(Z), g_0(Z))` is an IMMERSION of `A^1` — the
   function-pair theorem the campaign already has ("immersive normalisation
   `Phi = A^1 -> C_0`", structure:179).
4. Under H2, `A_F` is irreducible, so `A_F = C_0`, and `F|_{L_0} : L_0 -> A_F`
   is a surjective immersion of a smooth line. By LOCAL-ISO TRANSPORT at any
   `y ∈ L_0`, the germ `(A_F, F(y))` contains the smooth branch `F(L_0, y)`.
   So EVERY point of `A_F` has a smooth branch through it: `A_F` has no
   unibranch singular point. ∎

Hence, under H2, a Keller map factoring through the A2 model has `A_F` with
every branch smooth: THEOREM PROFILE case (0) or (B1), EMPTY for `N <= 16`
(SMOOTH-KILL, NODAL-ALL-N). It is NOT in (B3) and NOT in (A). In particular:

* The A2 residual — cells `(e,U)`, OPEN[A2-CELL-32], OPEN[A2-U-BOUND],
  OPEN[A2-O0-O1], the E1-wall, the box01 window — is MOOT for `N <= 16`
  under H2. A cell EMPTY there proves nothing not already proved; a cell
  NONEMPTY would be a (B1) object at `N >= 17` (or a reducible-`A_F` object),
  never an N=4 horn point. The cell computations are confirmatory at best.
* The "(B3) horn" has NO analytic model in the campaign. The block-descent
  structure report itself carries the tension: it records both the immersive
  normalisation `Phi -> C_0` (line 179) and a cusp `c ∈ B` with
  `u_c ∈ pi^{-1}(B) ∩ S` (§1.2). Under H2 `B = C_0`, so `c = pi(0,0,z_c)`
  for some `z_c`; if `u_c = (0,0,z_c) ∈ Phi` the branch is smooth, if
  `u_c ∉ Phi` then `a_c >= 2`, against N4-PIN's `a_{p_0} = 1`. Either way the
  one-cusp structure with this `Phi` is contradictory under H2. (N=4 is
  already closed by other routes; the value here is all-degree typing.)
* Gap (k) is answered: the two instruments act on different objects because
  the analytic one is not a (B3) object. Gap (l) is answered: the ladder's
  non-termination is HORN-A2 r2 Cor 3.3 (formal unobstructedness along `Phi`,
  free `C[Z]` at every level) — a formal-versus-polynomial phenomenon of the
  same kind as row 4's germs, not a positive-side signal.

What a genuine (B3) analytic model must have (DERIVED): a first map whose
Jelonek set `A_iota` maps onto `A_F` NON-immersively — the "escape locus" in
the source must itself pass through a cuspidal point of `E`. A smooth source
line whose twin escapes (the A2 model's `L_0`) can never do it, because
`F|_{smooth curve}` is always an immersion.

## 2. Disposition over gaps (a)–(l)

| gap | disposition | reason |
|---|---|---|
| (a) A2-U-BOUND | **RETYPE + LOWER** | not the horn's missing theorem (§1.2); it bounds a (0)/(B1)-profile object; relevant only if a cell survivor is shown to sit at N>=17 or off H2 |
| (b) (B3) cage 4<=N<=16 | **RAISE** (now THE H2 neck) | with (A) closed at all N (§1.1) and A2 mis-filed, (B3) has no analytic model at all; the replacement for CUSP-KILL and OPEN[DEG-AF-VS-N] are the only handles |
| (c) case (A) N>=8 | **CLOSE (pending review of §1.1)** | trivial-sheet argument; no enumeration or Alexander gate needed |
| (d) (B2) 5<=N<=16 | **RAISE** | it is now one of only two H2 residual species below 17; instrument is a bound on `beta`, i.e. OPEN[DEG-AF-VS-N] |
| (e) (B1) N>=17 / ceiling | **unchanged; sharpen** | H2 = "`A_F` irreducible"; complement = reducible cage/companion front (CAGE-N-R2 + COMPANION-EXISTS, no `N_0`). The bounded-N architecture cannot finish: every closure is a numerical inequality with an N-cap. The two degree-monotone candidates in the record are `R <= 1` (kills (B1) at EVERY N, MPRIME §9) and `deg A_F <= f(N)`. Both are statements about the dicritical covers `l' = A^1 -> A_F` of one polynomial map; that is where a degree-free theorem must come from |
| (f) companion / R0 | unchanged | no new lever found; LOCAL-ISO TRANSPORT also applies per component and gives `a^{(i)}` fixed sheets of the component's local groups — worth a desk check on the (9,6,2)+cubic companion datum |
| (g) N>=6 census | **RETYPE** | with (A) gone everywhere and (B1) gone below 17, the H2 side at 6<=N<=16 is (B2) beta-forced or (B3); a census should be designed per profile, not per `S_N` |
| (h) infinite-U family as CE target | **LOWER hard** | at N<=16 under H2 it is dead by theorem; a survivor would be N>=17 (B1) or reducible — still a target, but not "where a counterexample could live" at small N |
| (i) (B3) N=4 rigid survivor | unchanged (calibration only) | N=4 closed; keep as the instrument test-bed |
| (j) char-p / AS109 | unchanged | orthogonal; no new information |
| (k) bridge A2 <-> (B3) | **CLOSED NEGATIVE** | no bridge exists because the A2 object is not (B3); the correct bridge is A2 -> MPRIME PROFILE, and it kills |
| (l) non-termination as signal | **CLOSED NEGATIVE** | formal unobstructedness (HORN-A2 r2 Cor 3.3), not a family |

## 3. Disposition over the 46 APPROACHES rows (changes only)

* **Row 7 (A(F) as the object): RAISE, retype Tried -> "the H2 backbone".**
  MPRIME PROFILE, N4-PIN, CUSP-A-EMPTY and both theorems of §1 are theorems
  about `A_F` and `E = F^{-1}(A_F)`. Grok's "would not start here" is
  overtaken; Sol's S9 is vindicated. The table's "A(F) never constructed" is
  stale: `A_F = pi(Phi)` is constructed explicitly in the A2 model.
* **Row 6 (AM / one-place): RAISE.** Case (A)'s substrate was exactly a
  one-place curve and died to conical structure; in (B3) the object with one
  place is `A_F` (Lemma A) while `E` has `3+4k-2k_odd` places — the
  place-count contrast is the datum CUSP-KILL lacks (OPEN[B3-J1-KILL]).
* **Row 5 (JvdK descent): RAISE (as a lens, not a program).** HORN-A2 r2 §5
  kills cells (3,1),(2,1) by `f -> f - c g^k` then `Aff_2`: literally
  elementary automorphisms of the target. The survivor (3,2) is a coprime
  pole-order pair along one divisor at infinity of `S` — the cusp
  leading-form wall of row 5, on the block surface. Its plane analogue
  (gcd of degrees 1) is Magnus' theorem. See §5.2.
* **Row 1 (GGV corner farm): unchanged, but record the recurrence.** The A2
  residual cells `(e,U)` are a Newton-polygon corner farm in the
  `(A, Z)`-bidegree on `S`; "the ladder does not terminate" is row 1's
  "always a next pair" transplanted. Do not fund it as if it were new.
* **Row 4 (formal germs): unchanged; cross-cite.** Cor 3.3 of HORN-A2 r2 is
  the horn's version of "formal nonempty ≠ polynomial".
* **Row 26 (primitive monodromy) and Row 25 (passports): unchanged; note**
  that the decisive case-(A) gate was a fixed point of a transitive group —
  the cheapest group-theoretic fact there is — and that every N=8 survivor
  should be re-run with "`rho(alpha), rho(beta)` share a fixed point"
  imposed (they cannot; §1.1).
* **Row 28 (log surfaces / BMY): RAISE for (B3) only.** B3-N4 makes `E`
  explicit (irreducible, genus `k_odd - 1`, `3+4k-2k_odd` ends, one cusp).
  A log-BMY / Miyaoka-type inequality on `(compactified A^2, E)` is now a
  well-posed way to bound `k` and feed OPEN[DEG-AF-VS-N]. Needs data, not
  new machinery.
* **Row 36 (guided CE search): LOWER for the A2 ray** (gap (h)).
* All other rows unchanged.

## 4. Reranked bottlenecks

**Proof side (H2 branch and complement), in order:**

1. **(B3) at 5<=N<=16: a mechanism replacing CUSP-KILL when E has genus**,
   or **OPEN[DEG-AF-VS-N]** (bounds `k`, the Puiseux pair, and (B2)'s `beta`
   at once). This is the single H2 neck below 17 once §1 is banked.
2. **All-degree: `R <= 1`** (total finite ramification of the dicritical
   covers). Kills (B1) at every N and is the only degree-free statement in the
   record with a known consequence chain. Valuation-theoretic; belongs to row
   3's Favre–Jonsson lens.
3. **(B2) beta bound** (same source as 1).
4. **Reducible branch: OPEN[COMPANION-R0-REALISATION]** — unchanged.
5. **(B3) analytic model** — does not exist; building one is prerequisite to
   any analytic attack on (B3) (§1.2 last paragraph).

**Disproof side:** 1. the reducible branch at N=6,7 via COMPANION-EXISTS
realizations pushed through the validated pipeline (realization -> SIROCCO ->
ZvK -> `S_N`); 2. (B3) rigid objects at N=5,6 as construction targets (the
N=4 one is a calibration piece); 3. A2 cell survivors only if re-typed to
N>=17 (B1) — a much longer shot than before; 4. char-p / AS109 unchanged.

## 5. New mechanism and new cross-connections

### 5.1 NEW mechanism: LOCAL-ISO TRANSPORT as a rule (not a fragment)

Stated in §1. Novelty check against the banked record: ACS-FIX-VS-DEFICIT
(`a = #Fix rho(m)`) and LEMMA B3-LOC (`r_O = 0` at affine orbits) are its
codimension-one and per-orbit shadows; neither is stated as "the local group
at `p` fixes `a_p` sheets, and the germs transport isomorphically". Stated as
a rule it yields, beyond §1.1–1.2:

* **E-structure in any profile (DERIVED).** Every affine preimage `y` of `p`
  has `(E,y) ≅ (A_F,p)`. Hence `#cusps of E = a_{p_0}` (= 1 in case (A) and
  at N=4 in (B3)), NOT `a`. The CUSP-A-N8 charge's "`a` copies of the local
  Alexander factor" over-counts; if that lane continues in any form the
  Libgober product must use ONE cusp factor.
* **Component decomposition in case (A), a = 2 (DERIVED, now moot but a
  template for (B3)).** Each component `E_i -> A_F` is a birational local
  isomorphism, so `E_1 ≅ A_F` (through the cusp) and `E_2 ≅ A_F \ {p_0} ≅ C^*`,
  `E_1 ∩ E_2 = ∅` since `A_F` is unibranch everywhere. The same reasoning in
  (B3) at N=4 reproduces B3-N4's hyperelliptic cover `Ē -> P^1` and adds:
  the branch points of `Ẽ -> A^1_t` all lie over double points of `A_F`
  (count `2k_odd`), never over smooth points (a smooth point has `a_p = 2`
  distinct affine preimages, hence two unramified sheets). Cheap
  cross-check of B3-N4; consistent.

### 5.2 Cross-connection A: A2 (3,2) cell = JvdK/Magnus configuration on the block surface

In the `(T,V)` chart the Keller condition on `S` reads
`2(f_V ∂_tau g - ∂_tau f g_V) = kappa`, `tau = log T`: a constant-Jacobian
condition on the symplectic cylinder. HORN-A2 r2's (N0) gives leading forms
`(c_1 h^3, c_2 h^2)`: the pole orders along `{T=0}` are coprime. In the plane,
"Keller pair with coprime degrees" is Magnus' theorem (automorphism, hence no
noninvertible example); the Nakai–Baba / Appelgate–Onishi weight argument
is the plane proof. The cylinder version fails to be immediate for one
reason only: the `T`-adic grading treats `V` as degree 0, so `h` is any odd
polynomial in `V` — that freedom IS the parameter `e = deg eta`. A second
grading at `V = infinity` is what the campaign's `U`-corner analysis supplies;
so the two-grading corner farm on `S` is the GGV farm (row 1) and Magnus'
theorem is the statement the farm is circling. Only matters now for N>=17 or
off-H2 (§1.2), but it is the right theorem to aim at if the A2 class is
ever re-funded.

### 5.3 Cross-connection B: THEOREM PROFILE is the fibre-partition gate's parent

Both §1 theorems are the same inequality read two ways: `a_p >= 1` at a point
of `A_F` forces a fixed sheet of `Loc_p`. In case (A), `Loc_{p_0} = G`
(conical) so `a_{p_0} = 1` is fatal; in the A2 model `a_p >= 1` at EVERY
`p ∈ A_F` (the `L_0` sheet) so no cusp can exist. The general lesson, worth a
line in the (B3) charge: **the set `{p : a_p >= 1}` and the surjectivity
defect of `Loc_p -> G` are one datum**; in (B3) at N=4, `a_p = 2` generically,
`a_{p_0} = 1`, `a_{q_i} = 0` — the node has NO affine preimage, so `Loc_{q_i}`
(free of rank 2 for contact 1) acts with no fixed sheet on the 4 sheets:
`rho(g_1), rho(g_2)` disjoint transpositions (HF Prop 3.1) — consistent, and
now explained rather than derived case by case.

## 6. Strongest attacks

**Proof.** Bank §1.1 and §1.2 through different-model review (one desk hour
each), then re-issue THEOREM PROFILE without row (A) and with the A2 model
re-filed under (0)/(B1). The H2 residual below 17 is then exactly
(B2) ∪ (B3). Attack (B3) via OPEN[DEG-AF-VS-N] with the now-explicit `E`:
apply the log-BMY inequality to `(X, D_infty + E)` for a minimal SNC
compactification of `A^2 \ E`, using genus `k_odd - 1`, `3+4k-2k_odd` ends,
one `(p,q)` cusp with `(2|p,3|q)` or `(3|p,2|q)`; the output is an
inequality in `(k, k_odd, p, q)`. Even a bound `k <= k_0` at N=4 is a
template for the N=5,6 (B3) profiles.

**Counterexample / falsification.** Not the A2 ray (§1.2). The live CE
substrate is the reducible branch at N=6: COMPANION-EXISTS realizes the
forced companion datum at every N, and the pipeline is validated on two
curves. Design: pick the smallest `(d,e)` three-row family member at N=6,
realize `A_F = D_1 ∪ D_2` with the CAGE-N-R2 profile, run SIROCCO -> ZvK ->
`S_6` with the fixed-sheet constraint of §5.3 imposed per component
(`a^{(i)}` fixed sheets of each `Loc_p` for `p ∈ D_i`): the constraint is
free to impose and is expected to cut the representation space by an order
of magnitude before any curve-level work.

## 7. Software acceleration / decisive experiment

**PROFILE-PREFLIGHT (decisive, one afternoon).** For any analytic model the
campaign builds (the A2 model today, a (B3) model tomorrow), compute
mechanically before any Gröbner job: (1) `A_iota` of the declared first map
(limit test along the escaping family; for the A2 model the 3-line check of
§1.2 item 1); (2) `pi(A_iota)` and the immersivity of its parametrization
(gcd of the two derivative polynomials); (3) the THEOREM PROFILE case this
forces under H2. Emit `PROFILE = (0)|(A)|(B1)|(B2)|(B3)|REDUCIBLE` beside the
`.ms` file and REFUSE the job when the profile is already EMPTY at the
target N. Positive control: the A2 model must tag `(0)/(B1)`; negative
control: a hand-built model with a cuspidal `pi(A_iota)` must tag `(B3)`.
This would have stopped the box01 window before (1,3). It is also the
instrument that decides §1.2 for the reviewer.

## 8. Campaign-systems check — UPGRADE (rotation: claim/review propagation)

**Finding.** Two promoted objects carried contradictory properties for about
two days without detection: "`Phi = A^1 -> C_0` is an immersive
normalisation" (structure, 08-31, reviewed) and "`A_F = B` has a unibranch
singular point" (N4-PIN, 09-02, reviewed), with `B = C_0` under the promoted
`m = 1`. Each review was correct in isolation; the contradiction lives in the
join. The same pattern produced the case-(A) survivors: `a_{p_0} = 1` was
consumed numerically and never as a permutation fact.

**UPGRADE card: OBJECT-LEDGER at integration.** For each named object
(`A_F`, `E`, `Phi`, `S`, `rho`), maintain one file listing every promoted
property with its source line; at every integration the coordinator appends
the new properties and reads the whole list once. Smallest useful test:
build the `A_F` ledger for basis 8939320b by grep over `xmodel/*integration*`
and the four flagship reports (30 minutes), and check whether the
immersive/cusp pair surfaces. If it does, the upgrade paid for itself
retroactively; if not, `NO_CHANGE` with that evidence. Regression risk: none
(read-only artefact). Opportunity cost: half a coordinator hour per
integration.

## 9. Idea cards (three)

**Card A — CUSP-A-ALL-N review-and-bank.** Dependencies: Prop 6.1
(`a_{p_0}=1`), Lin–Zaidenberg, conical structure of `{x^p=y^q}`. Cheapest
discriminator: a different-model desk review of §1.1 (one hour), plus one
machine control — impose "`rho(alpha)` and `rho(beta)` share a fixed point"
on the sweep's 26 N=8 survivors (expected: 0 survive; `(4,4)` has no fixed
point). Outcomes: CONFIRMED -> gap (c) closed at all N, two lanes freed;
REFUTED at Prop 6.1 -> `a_{p_0}=0` is admissible and the sweep must be redone
with cusp partition `(N)` (a different, smaller residual); REFUTED at the
conical step -> impossible unless Lin–Zaidenberg is misapplied, which would
also break CUSP-A-EMPTY. Stop: one review. Information gain: an entire
profile row at every degree.

**Card B — PHI-IMMERSION review-and-refile.** Dependencies: the A2 model's
first map is the retained chart (or any étale degree-2 `iota` with a
one-point fibre over `Phi`); H2 assumed in the A2 lane (the packet frames it
so). Discriminator: the 3-line limit computation of §1.2 item 1 and (1.9) of
the structure report, checked by a reviewer; then read off the PROFILE case.
Outcomes: CONFIRMED -> A2 residual re-filed to (0)/(B1), MOOT for N<=16;
box01 window stopped or demoted to confirmatory; a2-ubound retargeted;
"(B3) analytic model" becomes a named OPEN. REFUTED because `Phi ⊄ A_iota`
-> the model's first map has two preimages over `Phi`, so its relation to any
Keller map must be re-declared (equally decisive for allocation). REFUTED
because H2 is not assumed -> the A2 object is a reducible-`A_F` model and
belongs to the companion front. Stop: one integration. Gain: a frontier
seat and a 64-vCPU box redirected.

**Card C — (B3) `k`-bound via log-BMY on the explicit `E` (the successor
attack).** Dependencies: B3-N4 (E irreducible, genus `k_odd-1`,
`3+4k-2k_odd` ends, one cusp of type `(2|p,3|q)` or `(3|p,2|q)`), a minimal
SNC compactification of `A^2 \ E` (one blow-up sequence at the cusp and at
the ends; Sol-scale desk work), and the log-Miyaoka–Yau / Kobayashi
inequality for open surfaces with the log-canonical divisor pinned. Cheapest
discriminator: compute `bar-kappa(A^2 \ E)` and `c_1^2, c_2` of the log
pair at `k = 1, 2, 3`; if `bar-kappa = -infty` (as for `A^2 \ A_F`, row 28's
known wall) the card stops immediately with a typed NO. Outcomes: an
inequality in `(k, k_odd, p, q)` -> finite list at N=4 (calibration: must
kill nothing already alive, since N=4 is closed independently) and a
template for N=5,6; NO -> row 28 stays where it is and OPEN[DEG-AF-VS-N]
needs a non-BMY source. Stop: `bar-kappa` sign. Gain: the first bound on `k`
anywhere in the record.

## 10. Current lanes

* `a2-ubound-opus5-20260902`: **REDESIGN NOW.** First task: adjudicate §1.2
  (30 min). If confirmed, drop the U-bound hunt and spend the seat on either
  (i) the degree `[Frac R : C(f,g)]` of the A2 class (decides whether any cell
  can be N>=17) or (ii) the missing (B3) analytic model. Its lead (L5), the
  "infinite-U family as counterexample-level object", must be re-typed
  (0)/(B1) before any report calls it a candidate.
* `cusp-a-n8-gate-opus5-20260902`: **REDESIGN NOW.** Replace the charge with:
  verify §1.1 hostilely; if it stands, close OPEN[HOMCOVER-CUSP-A-N8] and
  CUSP-A-KAPPA and stop. If the lane continues on any residual, correct
  "`a` cusp factors" to `a_{p_0} = 1` in the Libgober product (§5.1).
* box01 A2 cells window: **STOP after the running (1,9) job** (do not
  waste the checkpoint); redirect box01 to the N=6 reducible realization
  census (§6) with the fixed-sheet prefilter.
* `web-sweep-20260902-grok46`: continue. Box03 869: continue to cap
  (confirmatory, cheap).

## 11. FALLACY-v2 audit and typed verdict

Flag/place/series: `Phi` (interior), `{T=0}` (divisor at infinity of `S`),
the target place, `A_F`, `E`, `L_0` kept distinct throughout; `Loc_{p_0} = G`
asserted only in case (A) with the conical reason displayed. Carrier /
attainment: nothing here asserts a Keller map exists; both theorems are
emptiness statements. Floor/attainment: none. `sat()` / remainder / ring map:
no CAS run. Prime label: `f_0'` is `d/dZ`, `t_i^±` are labels; never mixed.
Not filled by cap or analogy: where a dependency could fail (Prop 6.1's
`a_{p_0} >= 1`; the identity of the A2 first map) it is named as the hostile
check, and the alternative outcome is typed in the card.

```text
PROVED-HERE/UNREVIEWED   CUSP-A-ALL-N   (Sec 1.1)   case (A) EMPTY, every N
PROVED-HERE/UNREVIEWED   PHI-IMMERSION  (Sec 1.2)   A2 model => A_F immersed;
                                                     under H2 profile (0)/(B1);
                                                     EMPTY N<=16 by MPRIME
DERIVED                  #cusps(E) = a_{p_0};  E_1 ⊔ E_2 in case (A) a=2;
                         (B3) N=4 branch points over double points only
PROPOSED                 LOCAL-ISO TRANSPORT as a rule; PROFILE-PREFLIGHT;
                         OBJECT-LEDGER; Cards A-C; Magnus-on-S lens
NOT CLAIMED              any all-degree closure; any (B3) kill; anything about
                         the reducible branch beyond a prefilter; N=4 re-hardening
```

Timing: sealed at completion, within the 75-minute window; not DEGRADED.
Size deviation: body about 26KB against the 15-25KB target; logged, not trimmed (Sec 1 proofs are the deliverable).

<!-- BODY-END -->
