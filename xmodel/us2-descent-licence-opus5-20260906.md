# The two u_s >= 2 licences — Opus 5 — 2026-09-06

```text
VERDICT (1) RADIUS  [PROP6.3-RADIUS-US>1] ...... OPEN
        The printed obstruction is one line of p.199.  Reconstructed below:
        u_s = 1 enters Prop 6.4's proof EXACTLY ONCE, at the gcd step, and the
        same computation at u_s >= 2 yields only  deg p | u_s , which for
        u_s >= 2 is consistent with p.191's definition of delta*_{s-1}.  This
        is PROVED-NEGATIVE, not a reading gap: the surviving branch is exactly
        the split branch the frozen screen already carries.  Prop 6.1,
        Lemma 6.2, the p.194-196 normalisation, Prop 5.3 and Def 5.1(3) are
        each checked and none supplies the hypothesis.
VERDICT (2) TERMINAL [CHILD-TERMINAL-SUPPORT-US>1] ... PROVED FINITE
        Three printed conditions (p.150 gcd rule, p.174 Definition-Remark,
        Def 5.1(2)) bound the child's terminal part to at most Omega(u_s) <= 2
        further levels and to an EXPLICIT list: 138 completions over the twenty
        rows, <= 22 per row, and exactly ONE on R066 (DETERMINED).  It is not
        unbounded.  Which member is realised stays OPEN on 19 rows.
PER ROW: 20/20 NOT-LICENSED (radius).  Terminal: 19 FINITE, 1 DETERMINED.
        0 rows become unconditionally testable; under a supplied radius all 20
        become finite-branch testable and R066 becomes single-branch.
NUMERIC: 0 rows fail the inequality numerically and 0 rows pass it.  By p.191
        delta*_{s-1} is a minimum of contact orders of ACTUAL roots, so it is
        not a function of a configuration row; v_s/u_s > 1 strictly on all 20,
        so Prop 6.1's printed floor delta*_{s-1} >= 1 never reaches it.
```

## 0. Custody

Receipt `charged_input_<i>_sha256=`/`_basename=` paired with `awk`, manifest written to
`/tmp/lane_manifest.sha256`, `sha256sum -c`: **8/8 OK** before any mathematical read.
All reads are the frozen copies in `/tmp/jc2-lane.QdmVTB/inputs`. Moh's decisive displays are
OCR-dead, so pp. 150, 170, 174, 191-193, 196-199 were rendered with `pdftoppm -r 200` (PDF page
= printed page - 139, pinned by p. 178 = PDF 39) and read as images. No fleet, no ledger edit,
no `jc2-lean`, no `ideation-*` input, no uncharged mathematical report. Drivers and JSON in
`box/us2-descent-licence-20260906/`. No new exit-price assertion is made, so no `charge_basis=`
line applies.

## 1. Prop 6.4 reconstructed, and where u_s = 1 is used

**Prop 6.4, p.198 (statement) / p.199 (proof).** *g monic in y, deg g = deg_y g = n > 1,
delta_s = -1 and* **u_s = 1**. *Then the logarithmic radius delta\*\_{s-1} of the minor disc
D\*\_{s-1} >= v_s/u_s = v_s.* The six steps of the printed proof:

```text
(P1) Assume delta*_{s-1} < v_s.  sigma = sum a_j t^j + pi t^{delta*_{s-1}} is the unique
     pi-root in D*_{s-1}.
(P2) ord g(sigma) = -(v_s n/d_s) + delta*_{s-1}(u_s n/d_s) = (n/d_s)(u_s delta*_{s-1} - v_s) < 0
(P3) Prop 6.1(2), p.191:  ord g(sigma) < 0  =>  sigma is a distribution detector for
     g(y), T_1^psi(y), ..., T_{s-1}^psi(y).
(P4) leading coefficients g_sigma(pi), T_{i,sigma}^psi(pi) are powers of a common p(pi);
     their degrees are  u_s n/d_s  and  u_s(-mu_i)/d_s.
(P5) g.c.d.(n/d_s, -mu_1/d_s, ..., -mu_{s-1}/d_s) = 1   =>   deg p | u_s.
(P6) u_s = 1  =>  deg p = 1: "powers of a common LINEAR polynomial".  A linear p has one
     root, so the cluster does not separate at delta*_{s-1} — contradicting p.191's
     definition of delta*_{s-1} as min ord(tau_i - tau_j), the MINIMAL-disc radius.
```

**Localisation.** `u_s = 1` is used **exactly once**, at (P6) — equivalently at (P5) read with
gcd `= 1` in place of `= u_s`. Steps (P1)-(P4) are `u_s`-free, and Moh himself prints (P2) in
its general form `-(v_s n/d_s) + delta*_{s-1}(u_s n/d_s)` before specialising: the negation of
the hypothesis, `delta*_{s-1} < v_s/u_s`, is *precisely* what makes (P2) negative at any `u_s`,
and (P3) is quoted from Prop 6.1(2), whose hypothesis is only `ord g(sigma) < 0`. The
degrees in (P4) are the p.193 display `V_r(n/d_r), V_r(-mu_1/d_r), ...` with the minor
multiplicity `V_s = u_s` (Prop 6.1 is stated at `V_r <= d_r/(n-M_r)`, the minor side).

**What the same argument yields at u_s >= 2.** (P1)-(P5) still run and give the dichotomy

```text
(R)  delta*_{s-1} >= v_s/u_s                                     [the Prop 6.3 hypothesis]
(S)  1 <= delta*_{s-1} < v_s/u_s, and the minor cluster (u_s units) splits there into
     t >= 2 sub-clusters with multiplicities lambda = (w_1,...,w_t) |- u_s, with
     g_sigma = p^{n/d_s},  p = prod (pi - c_j)^{w_j},  deg p = u_s.
```

The floor `1` is Prop 6.1's own estimate; p.193 states it in words: *"The above proposition
does not specify the logarithmic radius delta\*\_{r-1} of D\*\_{r-1}. We only get an estimate
delta\*\_{r-1} >= 1."* At `u_s >= 2` branch (S) is internally consistent, so no contradiction is
available and the licence is not implied. **This is a sharp negative, not a gap:** (S) is
exactly the split branch the frozen screen enumerates (section 2).

**The other printed candidates, each checked.**

| Candidate | What it actually gives | Supplies (R)? |
|---|---|---|
| Prop 6.1, pp.191-193 | `delta*_{r-1} >= 1` only; its proof verifies Prop 4.4 cond. (7), and p.193 shows (7) `<=> delta*_{r-1} < 1`, so the route is **structurally capped at 1** | no |
| Lemma 6.2, p.196 | inversion lemma `x(theta) mod theta^q <-> y(t) mod t^q`. p.198 line 1: *"By the assumption on the logarithmic radius ... all e_i's are common. Hence it follows from Lemma 6.2 ..."* — it **consumes** the radius | no |
| p.194-196 (Prop 6.2) | the `z`-normal form and `ord g(sigma) < (u_s - v_s)n/d_s`; used inside Prop 6.3 **after** the radius | no |
| Prop 5.3, pp.180-182 | successor radius of a **major** sub-disc; never bounds a minor `delta*` | no |
| Def 5.1(3), p.179 | computes the **major** radii `delta_i`. Computed on all 20 rows: `max delta_{s-1} = 4/7 < 1 <= delta*_{s-1}` — a different quantity, never at the threshold | no |

## 2. The numeric check, and the split window

By p.191, `delta*_{s-1} = min{ord(tau_i - tau_j)}` over the roots of `g prod T_i^psi` in the
cluster — a contact order of **actual roots**. The roster rows are typed
`NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`, so `delta*_{s-1}` is not a function of a
row and the inequality cannot be decided numerically. What *is* computable is the threshold and
the gap the printed floor leaves open (`radius_data.py`, cross-checked against the frozen
`source.delta`):

| Row | (n,m) | d_s | u_s | v_s | v_s/u_s | delta_{s-1} | deg p \| u_s | window (1, v_s/u_s), den <= u_s | ES leaves |
|---|---|---:|---:|---:|---:|---:|---:|---|---:|
| R012 | 108,72 | 9 | 2 | 7 | 7/2 | 1/4 | 2 | 3/2,2,5/2,3 | 1 |
| R015 | 99,66 | 11 | 3 | 8 | 8/3 | 1/3 | 3 | 4/3,3/2,5/3,2,7/3,5/2 | 2 |
| R016 | 168,112 | 7 | 2 | 5 | 5/2 | 3/8 | 2 | 3/2,2 | 1 |
| R023 | 165,110 | 11 | 2 | 9 | 9/2 | 1/5 | 2 | 3/2,2,5/2,3,7/2,4 | 1 |
| R024 | 165,110 | 11 | 2 | 9 | 9/2 | 1/5 | 2 | 3/2,2,5/2,3,7/2,4 | 1 |
| R029 | 168,112 | 8 | 3 | 5 | 5/3 | 4/7 | 3 | 4/3,3/2 | 1 |
| R035 | 144,108 | 9 | 2 | 7 | 7/2 | 1/4 | 2 | 3/2,2,5/2,3 | 1 |
| R038 | 135,90 | 15 | 4 | 11 | 11/4 | 1/3 | 4 | 5/4 ... 8/3 (10) | 4 |
| R043 | 168,112 | 14 | 3 | 11 | 11/3 | 1/4 | 3 | 4/3 ... 7/2 (10) | 3 |
| R044 | 147,42 | 7 | 2 | 5 | 5/2 | 1/3 | 2 | 3/2,2 | 1 |
| R045 | 147,63 | 7 | 2 | 5 | 5/2 | 1/3 | 2 | 3/2,2 | 1 |
| R049 | 189,126 | 9 | 2 | 7 | 7/2 | 1/4 | 2 | 3/2,2,5/2,3 | 1 |
| R051 | 180,144 | 9 | 2 | 7 | 7/2 | 1/4 | 2 | 3/2,2,5/2,3 | 1 |
| R052 | 165,99 | 11 | 3 | 8 | 8/3 | 1/3 | 3 | 4/3,3/2,5/3,2,7/3,5/2 | 2 |
| R053 | 200,150 | 10 | 3 | 7 | 7/3 | 2/5 | 3 | 4/3,3/2,5/3,2 | 2 |
| R054 | 175,70 | 7 | 2 | 5 | 5/2 | 1/3 | 2 | 3/2,2 | 1 |
| R055 | 171,114 | 19 | 5 | 14 | 14/5 | 1/3 | 5 | 6/5 ... 11/4 (18) | 6 |
| R062 | 180,135 | 15 | 4 | 11 | 11/4 | 1/3 | 4 | 5/4 ... 8/3 (10) | 4 |
| R065 | 180,120 | 12 | 3 | 9 | 3 | 1/4 | 3 | 4/3 ... 8/3 (7) | 1 |
| R066 | 162,108 | 9 | 2 | 7 | 7/2 | 1/6 | 2 | 3/2,2,5/2,3 | 1 |

`v_s/u_s > 1` **strictly on all twenty rows**, so Prop 6.1's floor licenses nothing anywhere;
and there is no printed upper bound on `delta*_{s-1}`, so no row is refuted either. The gcd of
the (P4) degrees is `u_s` on 20/20 rows, as the closed form predicts.

Two independent checks were run against the frozen screen. First, the window
`{rho in (1, v_s/u_s) : den(rho) <= u_s}` recomputed from `(u_s, v_s)` reproduces
`split_window.orders` on **20/20** rows. Second, the print-derived shape of branch (S) —
`lambda` a partition of `u_s` with `t >= 2` parts, and `den(rho) = Q` — was checked against
all **36** frozen `ES_NECESSARY_LEAF_NOT_ATTAINMENT` leaves: **0 violations** (a fabricated
`lambda` that is not a partition of `u_s` trips the same assertion). So the frozen screen is
faithful to Prop 6.4's mechanism, and re-running that mechanism yields **no new cut**: not one
row's window empties. `sum leaf_count = sum len(leaves) = 36` (the frozen prefixes report's 36,
not the older 38), `descent_forced = false` and `D2_branch = REMAINS_AS_ALTERNATIVE` on 20/20.

Because branch (R) is what a licence needs and branch (S) survives on every row, **all twenty
rows are NOT-LICENSED for the radius**, and no per-row exception exists.

## 3. Terminal identification: the family is finite and explicit

Three printed conditions bound the child's terminal part below the copied prefix.

**(T1) p.150.** `d_1 = n`, `d_{j+1} = g.c.d.(n, M_1, ..., M_j)`,
`M_j = min{i : f_i(x) != 0, d_j /| i}`, `M_{h+1} = infinity`. Hence the `M'` strictly increase
and each strictly drops the running gcd. The retained prefix has `d'_s = u_s` (Prop 6.3(2)), so
the number of **further** levels is at most `Omega(u_s)`, the number of prime factors of `u_s`
with multiplicity: `Omega = 1` for `u_s in {2,3,5}` and `2` for `u_s = 4`. **At most two.**

**(T2) p.174.** `deg q(pi) = n - M_{h-1} >= 2` bounds every characteristic exponent by `n-1`,
and the printed Definition-Remark says `M_h = n-1` *"should be dropped from our own
consideration ... the last effective characteristic pair is denoted by M_s"*.

**(T3) Def 5.1(2), p.179.** `V'_{i+1} d'_i/d'_{i+1} >= V'_i > d'_i/(n' - M'_i)`, `V'` a
positive integer, with the truncation convention `V'_{s'+1} = d'_{s'+1}` (which is Prop 5.1(2)'s
printed `v = d_h`).

`terminal_full.py` enumerates every `(M'`-tail, `V'` at the new levels`)` pair under (T1)-(T3),
with the prefix `(n', m', M'_1..M'_{s'}, V'_2..V'_{s'})` taken from the frozen roster:

| Row | u_s | (n',m') | prefix M' | #M'-tails | #full | terminal status |
|---|---:|---|---|---:|---:|---|
| R012 | 2 | 24,16 | -16,18 | 4 | 3 | FINITE |
| R015 | 3 | 27,18 | -18,21 | 5 | 4 | FINITE |
| R016 | 2 | 48,32 | -32,38 | 6 | 9 | FINITE |
| R023 | 2 | 30,20 | -20,22 | 5 | 7 | FINITE |
| R024 | 2 | 30,20 | -20,22 | 5 | 7 | FINITE |
| R029 | 3 | 63,42 | -42,54 | 7 | 15 | FINITE |
| R035 | 2 | 32,24 | -24,26 | 4 | 5 | FINITE |
| R038 | 4 | 36,24 | -24,28 | 11 | 15 | FINITE |
| R043 | 3 | 36,24 | -24,27 | 7 | 11 | FINITE |
| R044 | 2 | 42,12 | -12,38 | 3 | 2 | FINITE |
| R045 | 2 | 42,18 | -18,38 | 3 | 2 | FINITE |
| R049 | 2 | 42,28 | -28,36 | 4 | 5 | FINITE |
| R051 | 2 | 40,32 | -32,34 | 4 | 3 | FINITE |
| R052 | 3 | 45,27 | -27,39 | 5 | 4 | FINITE |
| R053 | 3 | 60,45 | -45,51 | 7 | 11 | FINITE |
| R054 | 2 | 50,20 | -20,46 | 3 | 2 | FINITE |
| R055 | 5 | 45,30 | -30,35 | 9 | 22 | FINITE |
| R062 | 4 | 48,36 | -36,40 | 11 | 8 | FINITE |
| R065 | 3 | 45,30 | -30,42 | 3 | 2 | FINITE |
| R066 | 2 | 36,24 | -24,28,34 | 2 | 1 | **DETERMINED** |

**138 completions in all, at most 22 per row.** Every row retains the `INFINITY` tail (the child
chain stops at `d' = u_s`), so no row is emptied. Three by-products:

* **R066 is DETERMINED**: its only admissible completion is `INFINITY | V' = 8,3`. Its finite
  tail `M'_4 = 35 = n'-1` is killed by (T3), because `V'_4 > d'_4/(n'-M'_4) = 2` and
  `V'_4 <= V'_5 d'_4/d'_5 = 2` are incompatible.
* That killing is **general**: a tail ending at `n'-1` forces `V > d` and `V <= d` for the same
  `d`, so (T3) alone reproduces p.174's Definition-Remark. This is a positive control on the
  enumerator rather than a new fact.
* Seven rows — R015, R029, R043, R052, R053, R055, R065 — admit a completion with
  `M'_last = n'-2` (12 of the 138), i.e. a child that is itself a campaign-normalised source
  with `delta'_last = -1`; the other thirteen do not, so on them a second Prop 6.3 descent is
  out of scope on every branch.

**Verdict (2): PROVED FINITE.** The terminal part is not unbounded. What remains open is
*identification* — which member — and that is now a finite disjunction, exactly the shape a
kill needs (refute all branches) and a survival needs (exhibit one). FALLACY-v2, *prefix is not
a chain*: a finite family of chains is still not a chain, and nothing here asserts realisation.
Not applied, and the cheapest next cut: Prop 5.1(2) p.174 states that at `M_h < n-1` the
Prop 4.6 conditions hold at the top disc with `r = h`, `v = d_h`, so Prop 4.6(3)-(5) (`q`
squarefree, roots of `p` are roots of `q`, `p` not a power of `q`) applies branch by branch.

## 4. LEMMA [CHILD-INTEGRALITY] in outline

The promoted lemma is conditional on (i) the Prop 6.3 radius and (ii) a certified **complete**
child major list; it then gives `I'_M in Z` as necessary, with `I'_M = u_s I_M` on the
transported part. Neither licence is discharged here, so no row becomes unconditionally
testable. What the two results above change:

* Licence (1) is refused on 20/20, so **0 rows are testable now**. Any conditional child
  assertion — including the frozen prefixes lane's `SURVIVES` on all twenty with
  `I'_M = u I_M` — keeps `OPEN[PROP6.3-RADIUS-US>1]` verbatim, as that report itself states.
* Under a *supplied* radius, licence (2) is no longer a blocker in kind: the missing child data
  ranges over `<= 22` explicit branches per row, so the integrality test becomes a finite
  branch check. On **R066** it is a single branch, so R066 is exactly one licence away from a
  decisive test — the cheapest target of the twenty.
* The direction matters. `SURVIVES` is existential and the frozen prefixes lane obtains it by
  transporting the **parent's** major list, so it needs no terminal at all. A **kill** is
  universal and does need the terminal: it must refute every one of the row's branches. The
  finite family is therefore of use only on the kill side.

Sums were not computed (the task licenses them only if cheap; each of the 138 branches needs
its own Def 5.1 radii and the printed final-major gate).

## 5. Verdicts

**Licence (1) RADIUS — OPEN.** Exact printed obstruction: p.199,
*"Note that g.c.d.(n/d_s, -mu_1/d_s, ..., -mu_{s-1}/d_s) = 1. Thus the polynomials
g_sigma(pi), T_{1,sigma}^psi(pi), ..., T_{s-1,sigma}^psi(pi) are powers of a common linear
polynomial."* At `u_s >= 2` the identical computation gives only `deg p | u_s`, and
`deg p = u_s >= 2` is consistent with p.191's definition of `delta*_{s-1}`. Proved in addition:
the argument cannot be repaired within the print, and none of Prop 6.1, Lemma 6.2, the
p.194-196 normalisation, Prop 5.3 or Def 5.1(3) supplies the hypothesis, under a printed extra
hypothesis or otherwise. No numerical failure and no numerical success on any row.

**Licence (2) TERMINAL — PROVED FINITE** (identification OPEN on 19 rows, DETERMINED on R066).

**Per row.** Radius: `NOT-LICENSED` on R012, R015, R016, R023, R024, R029, R035, R038, R043,
R044, R045, R049, R051, R052, R053, R054, R055, R062, R065, R066 — 20/20, each with a nonempty
surviving split window. Terminal: `FINITE` on 19; `DETERMINED` on R066. Testable under
LEMMA [CHILD-INTEGRALITY]: **none** unconditionally.

**FALLACY-v2.** *A numerical inequality is not a radius proof*: no value of `delta*_{s-1}` is
asserted; the table reports the threshold and the gap, and section 2 states why the quantity is
not a function of a configuration row. *A prefix is not a chain*: section 3 delivers a finite
family of chains and says explicitly that this is not identification. *Floor/attainment*: the
Prop 6.1 floor `>= 1` is used only as a floor, never as the value; `ES_NECESSARY_LEAF` is never
read as attainment. *Pole/interior*: Prop 6.1(2) is invoked only after `ord g(sigma) < 0` is
established. *Prime label/derivative*: `delta*` is Moh's minor-disc radius (p.191), kept
distinct throughout from the major `delta_i` of Def 5.1(3) and from Prop 5.2's `delta*(L)`.
No `sat()`, no remainder degree, no ring map, no exit-price assertion.

<!-- BODY-END -->
