# HOSTILE GATE: the six rows, the carry rule, and R063 — Opus 5 — 2026-09-06

```text
VERDICT
  R025 CONFIRMED-WITH-FIX   R026 CONFIRMED-WITH-FIX   R027 CONFIRMED-WITH-FIX
  R028 CONFIRMED-WITH-FIX   R057 CONFIRMED-WITH-FIX   R058 CONFIRMED-WITH-FIX
  R063 CONFIRMED (DEAD).    Residual stays 64.  No ledger edit made.

(1) The carry rule is TRUE as printed.  Prop 5.3 (p.180, not "181ff") takes ANY
    factor with V_r > d_r/(n-M_r) at D_r (r>=2) to D_{r-1}, the MINIMAL disc on
    that factor's cluster, at the radius prescribed by Def 5.1(3), and the
    extended tower is again major.  So the unselected D'_3 packet is not final
    at D'_3.  All six rows SURVIVE: integral complete sums exist and include the
    exact-contact parent certificates 17,17,17,22,18,18.

FIX 1 (diagnosis, not verdict).  The frozen fractional values are NOT truncation
    artifacts.  I prove the identity: an unsplit pass through a prescribed level
    gives exactly the same final radius as skipping the level.  So 75/4 and
    128/9 are the honest values of the NO-SPLIT branch (r=P_2), which is a
    licensed member of the fixed list.  What removes them is the actual-
    stabilizer residue test, not the carry.  The producer's headline mechanism
    is wrong; its conclusion is right.
FIX 2 (labelling).  The at-level parting bound is Q_i = deg q (Prop 4.6(2)-(4)),
    not "r-1".  The two coincide numerically at 4 and 3 in these two children
    and NOT at R063 (Q_2 = 7, r-1 = 13).

(3) R063 re-run under EXACTLY this rule: 6 complete configurations, ONE
    multiplicity pattern (5,3,3,3), ONE sum 71/4, nonintegral, and zero of the
    6 pass the residue test.  NO integral complete sum exists.  Kill stands.
    I also exhibit the (5,3,3,3) ODE face, which the r063 gate did not: the
    exclusion is arithmetic, not a missing face.
```

No new exit-price assertion is made, so no `charge_basis=` line applies.

## 0. Custody

I paired the numbered `charged_input_<i>_sha256=`/`_basename=` lines of
`xmodel/six-rows-gate-opus5-20260906.run.v2` with `awk`, wrote the manifest to
`/tmp/manifest.sha256`, and ran `sha256sum -c`: **9/9 OK**.  My driver re-asserts
all nine digests at import.  Mathematical inputs are the frozen copies in
`/tmp/jc2-lane.gFUAtE/inputs` plus the page images I rendered from the frozen
PDF (`pdftoppm -r 200`, journal page N = PDF page N-139).  No fleet, no ledger
edit, no `jc2-lean`, no `ideation-*`.  Own code and JSON in
`box/six-rows-gate-20260906/` (36 KB total; report + JSON well under 1 MB).

Typing is fixed throughout: the roster semantic type is
`NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`.  **SURVIVES = a necessary
configuration consistent with every printed constraint exists.**  It is not a
pair, not a `FULL_ACTUAL_EXIT`, and carries no attainment claim.  **DEAD** is the
dual: under the assumption that a pair realises the row, every configuration it
must have is excluded.

## 1. The print, read from the page images

**Prop 5.3, p.180** (the producer's "p.181ff" is the proof, not the statement):

> Let π−C_r be a factor of p(π) as in the conclusions of Prop 4.6 with
> multiplicity V_r satisfying deg p(π) = V_{r+1}(d_r/d_{r+1}) ≥ V_r > d_r/(n−M_r).
> Let δ_{r−1} = min{ord(τ_i−τ_j)} … = the logarithmic radius of D_{r−1}, the
> **minimal** disc containing all roots τ_i with ord(τ−τ_i) > δ_r.  Then
> δ_{r−1} = 1 − (n−M_{r−1})∏_{j=r}^{s}[V_j(n−M_j)−d_j] /
>            ((n−M_s−1)∏_{j=r}^{s}[V_j(n−M_{j−1})−d_j]).
> Moreover D_s ⊋ … ⊋ D_r ⊋ D_{r−1} is a tower of major discs.

Three consequences, all load-bearing here.

* **The carry is mandatory, and it is per-factor, not per-tower.**  The
  hypothesis names *a* factor, and p.179's note on Prop 5.2 says *any* subdisc
  above the average may serve as the next level.  So an above-average factor at
  D'_3 has a genuine D'_2 beneath it whether or not the tower selected it.
* **D_{r−1} is the minimal disc on the cluster.**  Its radius is the *minimum*
  pairwise distance inside the cluster.  A cluster whose roots were all strictly
  closer than δ_{r−1} would contradict the displayed equality.  So the cluster
  really does part at D_{r−1}: p_{r−1} has ≥ 2 distinct roots or the branch has
  a single root.  This is what makes the fixed list at D'_2 nonempty.
* **δ_{r−1} depends on V_j only for j ≥ r.**  Both D'_3 packets of the six rows
  carry V_3 = 1, so both land at the *same* prescribed δ'_2.  The producer's
  "prescribed D'_2" is correct.

**Def 5.1(2),(3),(4), p.179** are as the producer quotes.  I re-derived the
ℓ-shift independently: replacing Moh's `1 − X` by `H(1 − X)`, H = 1+ℓ (the shape
forced by (3)* on p.171, `λ = (−1−ℓ+δ)/(n−m_r)`), reproduces **all four radii on
all seven rows** from `(n,m,M,d,V)` alone — 28/28 exact matches, asserted in
`gate.py:analyse`.  That is an independent confirmation of the roster's
`delta_prime` column, not a re-read of it.

**Prop 4.6, p.170** gives deg p = v =: P_i, and conclusion (2) gives
T*_{r,σ} = p^E·q with **deg q = v(n−M_r)/d_r =: Q_i**, q squarefree (3),
roots(p) ⊆ roots(q) (4).  Hence *the number of distinct roots of p_i is at most
Q_i* — this, not "r−1", is the printed parting bound.  For r = 1 the equation is
`D(n,−M_1,g_σ,T*_1σ) = nonzero constant`, which forces g_σ and T*_1σ squarefree
and coprime (any multiple or common root kills both terms), i.e. **D_1 is
final**.  Tree depth is therefore exactly s' = 3 for all seven rows.

**p.171 (6), simplified**: `D(v(−μ_r/d_r), v, p, T*_{r,σ}) = C* p^{E+1}`.
Substituting conclusion (2) and dividing by p^E collapses this to

>  **P p q′ − Q p′ q = c·p,  c ≠ 0,  P = deg p, Q = deg q.**

At a root c₀ of p of multiplicity k, with q = (π−c₀)h and p = (π−c₀)^k u, the
coefficient of (π−c₀)^k on the left is (P − Qk)·u(c₀)h(c₀); the right side has
valuation exactly k; u(c₀), h(c₀) ≠ 0.  Hence **k ≠ P/Q**.

### 1.1 Two identities I did not find in either input

**(I1)  P_i/Q_i = d_i/(n−M_i) identically.**  P_i/Q_i =
(V_{i+1}d_i/d_{i+1})/(V_{i+1}(n−M_i)/d_{i+1}) = d_i/(n−M_i).  So Moh's forbidden
multiplicity is *exactly* Xu's major/minor threshold, and at k = P/Q the final
radius degenerates to δ_f = H = 1+ℓ — neither a final major disc (δ < 1+ℓ) nor a
final minor one (δ > 1+ℓ).  Verified on R025, R057, R063 at both levels.  The
rule is therefore doubly grounded, which matters in §4.

**(I2)  Unsplit pass = level skip.**  Write G(i,k) = (H−δ_{i−1})/(H−δ_i) =
(n−M_{i−1})(k(n−M_i)−d_i) / ((n−M_i)(k(n−M_{i−1})−d_i)).  Then for
V_{i−1} = P_{i−1} = V_i d_{i−1}/d_i (the no-split maximum),
G(i,V_i)·G(i−1,P_{i−1}) equals the one-step expression from D_i with M_{i−2}
in place of M_{i−1}.  Proof: cross-multiplying reduces to
(V_{i−1}(n−M_{i−1})−d_{i−1})(V_i(n−M_{i−2})−d_i) =
(V_i(n−M_{i−1})−d_i)(V_{i−1}(n−M_{i−2})−d_{i−1}), which is an identity once
V_{i−1}d_i = V_i d_{i−1}.  Checked numerically: R025 both routes give 7/8,
R057 both give 52/27, R063 both give −2/69.

**(I2) is fatal to the producer's diagnosis.**  Carrying the unselected D'_3
packet to D'_2 and *not* splitting it there returns the very same 7/8 and the
very same term 75/4.  The frozen 127/4, 107/4, 91/4, 111/4, 209/9 are therefore
not "artifacts of terminating the packet at D'_3"; they are the honest values of
the no-split branch r = P_2, a licensed member of the same fixed list.  The
producer's own §3.1 table already lists that branch as r = 5 with δ_f = 7/8 and
J_f = 75/4 and rejects it on residues — its §4 narrative contradicts its own
table.  The conclusion (integral sums exist) survives; the mechanism does not.

## 2. Independent recomputation

`box/six-rows-gate-20260906/gate.py` is my own driver.  It reads only
`roster.jsonl`, rebuilds δ from Def 5.1(3), and enumerates the whole tree:
at D'_i it forms every Galois-stable multiplicity multiset of p_i (multiplicity
z at π = 0 plus orbits of size A_i = den(L·δ_i)), rejects any with more than Q_i
distinct roots or a multiplicity equal to P_i/Q_i, sends every major factor to
D'_{i−1} at the Def-5.1(3) radius for that factor's V, terminates every minor
factor at δ_i + (H−δ_i)d_i/(k(n−M_i)), and terminates every major factor
reaching D'_1.  Two internal controls fire on every branch: minor ⟺ δ_f > H and
major ⟺ δ_{i−1} < H.  `L` is the actual centre stabilizer: it multiplies by A_i
only on a nonzero centre.  The final residue test is
ρ_P mod A_1 ∈ {0,1} and ρ_Q mod A_1 ∈ {0,1}, A_1 = den(L·δ_1) — the μ_{A_1}
action on the D'_1 π-line has orbits of size A_1 plus the fixed point π = 0, and
the r = 1 equation makes both root sets squarefree and disjoint there.

| row | (n′,m′) ℓ | configs | Galois-valid | integral | after minor floor | complete sums |
|---|---|---:|---:|---:|---:|---|
| R025 | (30,20) 3 | 816 | 576 | 576 | 540 | 12,13,16,17,21,22,26 |
| R026 | (30,20) 3 | 816 | 576 | 576 | 540 | 12,13,16,17,21,22,26 |
| R027 | (30,20) 3 | 408 | 288 | 288 | 288 | 13,17,18,21,22,26 |
| R028 | (30,20) 3 | 408 | 288 | 288 | 288 | 13,17,18,21,22,26 |
| R057 | (32,24) 3 | 120 | 36 | 36 | 36 | 18 |
| R058 | (32,24) 3 | 120 | 36 | 36 | 36 | 18 |
| R063 | (42,28) 1 | 6 | **0** | **0** | **0** | (only 71/4) |

Every parent certificate is present: 17 ∈ R025/R026/R027, 22 ∈ R028, 18 = the
unique R057/R058 value.  The rejected values reproduce the frozen flat numbers
exactly — 127/4, 107/4, 91/4 appear in R025/R026's full set, 111/4, 127/4 in
R027/R028's, 209/9 in R057/R058's — and every one of them is a no-split or an
r = 4 branch failed by the residue test.

**Top pattern.**  P_3 = 2 and V'_3 = 1 leaves only the multiplicity pattern
(1,1) (a degree-2 p containing multiplicity 1 has two simple roots); A_3 =
den(1·δ'_3) = 1, so the two roots are unconstrained and both are major
(1 > 2/5 resp. 1 > 2/3).  **D'_2 data.**  P_2 = V'_3d'_2/d'_3 = 5 resp. 4,
Q_2 = V'_3(n′−M'_2)/d'_3 = 4 resp. 3, A_2 = den(L·δ'_2) = den(0) = den(1) = 1;
L = 1 because δ'_3 ∈ ℤ and the top-disc centre is Galois-invariant.  No
multiplicity is forbidden (P/Q = 5/4, 4/3 ∉ ℤ).  So the fixed list is the
partitions of 5 into ≤ 4 parts (six of them) resp. of 4 into ≤ 3 parts (four),
exactly the producer's (6) and its four-element list.

**Residue rejections, recomputed.**  (30,20) at D'_2:
r=1 minor δ_f=5; r=2 δ=7/3 A=3 (4,6)≡(1,0) pass, term 4; r=3 δ=3/2 A=2
(6,9)≡(0,1) pass, term 9; **r=4 δ=21/19 A=19 (8,12) FAIL**, term 264/19;
**r=5 δ=7/8 A=8 (10,15)≡(2,7) FAIL**, term 75/4.  (32,24): r=1 minor δ_f=5;
**r=2 δ=38/13 A=13 FAIL** 48/13; r=3 δ=9/4 A=4 (9,12)≡(1,0) pass, term 9;
**r=4 δ=52/27 A=27 FAIL** 128/9.  Identical to both frozen tables.

**Branch sums** A=(3,2)→13, B=(3,1,1)→9, C=(2,2,1)→8, D=(2,1,1,1)→4,
E=(3,1)→9, and the 4×4 matrix reproduces the producer's exactly.

**Shifted minor floor.**  I_m^ℓ = (1+ℓ) + Σ_{minor}(δ_σ−1−ℓ).  D+D has six
multiplicity-1 minors at δ_f = 5, so I_m = 4+6 = 10 > 8 = I_M: rejected.  It is
the only rejection, and it removes exactly one value (8) from R025/R026.

**ODE witnesses, exact.**  All eight faces verified by exact polynomial
division, with deg p = P, deg q = Q, q squarefree, roots(p) ⊆ roots(q):
top(30/20) D(2,5)=6p; A 21p; B −105p; **C 3√5/5·p** (sympy's `simplify` leaves
this as a ratio of linears — the exact quotient by `sp.div` is 3√5/5 with zero
remainder, so the producer's value is right and only its presentation is
fragile); D 3p; top(32/24) −2p; E 20p; R063 top D(7,2,z⁷,z(z−1)) = 7p.

**Own data.**  I re-ran the frozen `descend_own` on all seven roster sources:
`V_type = DETERMINED` and `V_vectors` a singleton on every row, equal to the
roster's `V_prime` — (2,1),(2,1),(3,1),(3,1),(3,1),(3,1),(3,7).  `copied_V`
differs from the own value on five rows (R063: 21 vs 7), so the child V is
genuinely own-derived.

**Diff against `box/six-rows-child-20260906/audit.json`.**  Child data, P_i, Q_i,
A_i, δ'_i, branch tables, flat negative controls and parent certificates:
identical.  Complete-sum sets: identical, with one presentational difference —
audit.json keeps D+D (I_M = 8) in `complete_partitions` carrying
`xu_minor_bound_ok: false`, my run drops it.  Same conclusion.

## 3. Reconstructing what actually separates the six rows from R063

The producer never says *why* its instrument frees the six rows but not R063.
The separation is entirely at D'_2 and it is structural, not ad hoc:

| | A_2 | Q_2 (distinct-root cap) | forbidden mult P_2/Q_2 | fixed list |
|---|---:|---:|---|---:|
| (30,20) child | 1 | 4 | 5/4 ∉ ℤ — none | 6 patterns |
| (32,24) child | 1 | 3 | 4/3 ∉ ℤ — none | 4 patterns |
| R063 child | **3** | 7 | **2** | **1 pattern** |

A_2 = den(L'_2·δ'_2).  L'_2 = 1 on all three (the top disc is the minimal disc
on a Galois-stable root set, so its centre is Galois-invariant, and δ'_3 ∈ ℤ
adds no denominator).  Then A_2 = den(0) = den(1) = 1 for the six rows but
den(−1/3) = 3 for R063.  That single fact — plus P_2/Q_2 = 2 ∈ ℤ at R063 and
∉ ℤ at the six — is the whole asymmetry.  It is not a difference of instrument.

## 4. R063 under exactly this rule

Same driver, same code path, no special casing.

* **D'_3.**  P_3 = V'_4d'_3/d'_4 = 7, Q_3 = 2, A_3 = den(1·(−2)) = 1.  A degree-7
  p containing multiplicity V'_3 = 7 is (π−c)^7: one packet, no sibling.  **The
  producer's carry issue cannot arise at R063 — there is no unselected top
  packet.**  It is major (7 > 7/2) and Prop 5.3 carries it to D'_2.
* **D'_2.**  P_2 = 14, Q_2 = 7, A_2 = 3, forbidden multiplicity 2.  Writing
  p_2 = π^z∏(π³−c_j)^{r_j}: z ≡ 14 ≡ 2 (mod 3) so z ∈ {2,5,8,11,14}; z = 2 is
  forbidden; ≤ 7 distinct roots caps the orbit count at 2; and V'_2 = 3 must
  occur.  z = 8,11,14 cannot contain a 3; z = 5 forces Σr_j = 3 with (2,1)
  forbidden and (1,1,1) needing 10 distinct roots.  **Unique pattern (5,3,3,3)**,
  P′-counts (10,6,6,6) = 28, Q′-counts (15,9,9,9) = 42.  My enumerator returns 6
  configurations: 2 placements of the D'_3 root (π = 0 or π ≠ 0, indistinguishable
  since A_3 = 1) × 3 choices of which conjugate carries the tower.  All six have
  the same multiset of leaves.
* **D'_1.**  All four are major (5,3 > 2), so all four go to D'_1, which is final
  by the r = 1 equation.  Three at δ_1 = 7/6 with L = 3, A_1 = 2, (6,9) ≡ (0,1):
  pass, term 3 each.  One (the π^5 zero lane) at δ_1 = 13/24 with L = 1,
  A_1 = 24, (10,15): **fail**.
* **Sum.**  I′_M = 3·3 + 35/4 = **71/4** on every one of the six configurations.
  I′_m = 2 (minor-free).  71/4 ∉ ℤ contradicts deg_X Res_Y(P′_ξ,Q′) ∈ ℤ_{≥0}.

**No integral complete sum exists for R063.**  Zero of the six even pass the
residue test.  The kill is confirmed; the residual does not return to 65.

I add one thing the r063 gate did not supply.  It never exhibits a Prop 4.6 face
for (5,3,3,3), leaving open whether the pattern is even realisable.  It is:
p = z⁵(z³−c)³, q = z(z³−c)(z³−c/2) gives D(14,7,p,q) = −(21c²/2)p with q
squarefree for c ≠ 0 (`Res(q,q′) = −729c¹⁴/1024`), and the parameter is forced —
the z³ coefficient of D/p is 21(2e−c), so e = c/2 is the only face.  So the
exclusion of R063 is purely arithmetic, not a vacuous face condition.  That
makes the kill stronger, not weaker.

**What the kill rests on (sensitivity, run explicitly).**  Relaxing each printed
constraint in turn:

* A_2 = 1 instead of 3 (coarse stabilizer): 81 patterns and **12 is attainable**
  — would REFUTE.  Blocked by L'_2 = 1 above, which is forced, not conventional.
* dropping k ≠ P_2/Q_2 = 2: 2 patterns and **9 is attainable** — would REFUTE.
  Blocked twice: by p.171 (6) and, by identity (I1), because k = 2 is exactly the
  point where δ_f = H = 2, which is neither a final major nor a final minor disc.
* dropping "contains V'_2 = 3": 4 patterns, sums {71/4, 224/13, 77/3, 784/23},
  all nonintegral — not load-bearing.

Both live dependencies are print-derived and one of them is now doubly derived.
I record them as the exact places a future refutation would have to attack.

## 5. Verdicts

| row | claim gated | verdict | basis |
|---|---|---|---|
| R025 | SURVIVES, sums 17/22 | **CONFIRMED-WITH-FIX** | integral set {12,13,16,17,21,22,26}; 17 and 22 present |
| R026 | SURVIVES, sum 17 | **CONFIRMED-WITH-FIX** | same set; 17 present |
| R027 | SURVIVES, sums 17/22 | **CONFIRMED-WITH-FIX** | integral set {13,17,18,21,22,26} |
| R028 | SURVIVES, sum 22 | **CONFIRMED-WITH-FIX** | same set; 22 present |
| R057 | SURVIVES, sum 18 | **CONFIRMED-WITH-FIX** | unique complete sum 18 |
| R058 | SURVIVES, sum 18 | **CONFIRMED-WITH-FIX** | unique complete sum 18 |
| R063 | DEAD | **CONFIRMED** | unique pattern, unique sum 71/4, zero residue-valid configs |

The "-WITH-FIX" on the six rows is FIX 1 (the fractional values are the no-split
branch, killed by the residue test, not truncation artifacts) and FIX 2 (the
parting bound is Q_i, not r−1).  Neither moves a verdict.  Every one of the six
remains a **necessary configuration**: an integral complete partition exists and
matches the parent certificate, so the R063 template supplies no contradiction.
That is not attainment and not a Keller pair; global coefficient compatibility is
untouched and the parent certificates keep their own typing.

## 6. FALLACY-v2 audit

* **Flag/place/series.** Source tower, child coefficient discs and final child
  discs are kept apart; A_i is recomputed per branch from the actual centre, and
  the zero lane never inherits the nonzero lane's denominator (this is what makes
  R063's π^5 packet A_1 = 24 and not 8).
* **Carrier/attainment.** No `REPRESENTATIVE` is promoted.  SURVIVES is existence
  of a necessary configuration; DEAD is exclusion under an assumed realisation.
* **Floor/attainment.** I_m^ℓ is used only as a lower bound and only to remove
  D+D.  I′_M is used as the resultant degree only after the partition is proved
  complete (root counts exhaust both degrees: 2·(10,15) = (20,30), 2·(12,16) =
  (24,32), (10,6,6,6)/(15,9,9,9) = (28,42)).
* **Pole/interior.** Every packet is classified major/minor against
  d_i/(n−M_i) before any continuation formula is applied; identity (I1) shows the
  classification and the Prop 4.6 exclusion are the same condition.
* **Variable/ring map.** Child ring k[X,Y] = k[γ,π]; P′ = T̄_1^ψ(σ) of Y-degree
  m′, Q′ = ḡ(σ) of Y-degree n′; primes are generation labels, derivatives are
  written explicitly.
* **Raw remainder degree.** The C witness was re-done by exact `sp.div` with
  remainder 0 rather than trusting `simplify`; the R063 face parameter was solved
  from a coefficient, not fitted.
* **Merge-free/M-descent.** V′ is the singleton own vector from `descend_own`,
  re-run here; no free W level is inserted below D'_2, and D'_1 finality is the
  printed r = 1 equation, not a depth cap.
* **Target/arrival index.** Prescribed arrival levels D'_2, D'_1 are kept
  distinct from the packet's own final radius δ_f; identity (I2) is what shows
  the two coincide only in the no-split case.
* One over-permissiveness is declared: conjugate subtrees under an orbit of size
  A > 1 are expanded independently in my enumerator, which can only enlarge the
  configuration set.  It changes nothing here (R063's four D'_2 packets are all
  forced to final D'_1), and enlarging cannot rescue a kill.

Exact arithmetic, the sensitivity runs, the identities and the lane diff are in
`box/six-rows-gate-20260906/gate.json` (7.7 KB).  Reproduce with
`python3 box/six-rows-gate-20260906/gate.py`, `probe.py`, `ode.py`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19876`.
- Body SHA-256:
  `c54cce92255d19c885a66c79c44fb7618d4ba3f729bc3ffed6fb6eb50a8d568a`.
- Frozen basis: `8f363843528ad3e38db95908f0a687596645ad81`.
