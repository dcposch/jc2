# TOWER-9-15.md — tower certificate for the direct (9,15,7,3)@mu0=2 route

Status: **MILESTONE 1 EXECUTED (2026-08-13) — spine + local + LEAD-PILOT
banked; tower tier OBSTRUCTED (new result, UNREVIEWED — requires hostile
review before promotion).**
Engine: `cases/tower_check.py` (exact `Fraction`, no floats, no solver;
258 checks incl. a 7-case negative-perturbation self-test, exit 0).
Certificate: `cases/towers/t9_15_direct.json`.
Task source: `xmodel/sol-gluing-design.md` §5.4 first solver objective,
milestone 1: "finish one complete tower certificate for the direct
`(9,15)` route."

VERDICT IN ONE PARAGRAPH. The synchronized direct route of design §3.2
(the `(w,M,psi)=(2/3,3,2)` case-IV completion of `(9,15,7,3)@2`, with the
chain-1 synchronization stack that (H8) i-sync forces) admits a complete,
exactly verified decoration of every vertex and edge at the numerical and
leading-coefficient tiers — every `(kappa, pi, kbar, nu, rho, w, M, i,
d_p, d_q, deg p_f, D_f, d_f, d_g)` closes under the printed transport laws
with the promoted Q-value/H5a kappa and the E5 case-III identities, and
the design's §3.5 LEAD-PILOT (83 vars / 74 rows, SAT over Q) regenerates
from the certificate token-for-token. But the **approximate-root tower
layer cannot be completed**: level 1 of the global Prop 4.2 ladder is
claimed by both branches of the route with incompatible death data, and
the incompatibility survives *every* admissible choice of the chain-1
synchronization stack (15-case exhaustion, plus two structural lemmas
that close the family). Under the formalized tower laws — calibrated to
reproduce the td=6 template genome exactly — the direct synchronized
route family is **DEAD at the tower tier**. This is a KILL of the direct
completion's coefficient route as designed, not of the `(9,15,7,3)@2`
cell: the trunk completion `(35,15,7,5)@(2/5,5,1)` is untouched and now
becomes the cell's only live completion pending review.

---

## 0. Trust perimeter

Everything below is conditional on exactly these inputs, all named in the
certificate's `dependencies` field:

| input | role | status |
|---|---|---|
| H5a resolution: Q-value `kappa_F = nu_F kappa_G / nu_G` + E5 `(g')/(h')` | all case-III transports | PROMOTED (`AUDIT.md` H5a resolution; `xmodel/sol-h5a.md` + `grok-h5a-review.md` SOUND) |
| E5 corrected case-III row | zero-edge frame transport | PROMOTED (`SHEET6-III.md:131-147`) |
| Prop 4.2 (pp. 19–20) | global `(k_j,l_j)` ladder, `gcd(k_j,l_j)=1`, mu-recursion (9), `delta_j in N` strict descent, alive identity (iii) | printed; delta form verified at `SHEET6-TEMPLATE.md:53-55`, `SHEET6-R6.md:126-128` |
| Prop 8.1(i)–(v) (pp. 39–41) | `p_f = S p^i`, terminal `p_{h_m} = S p^k q`, `k = i(mu-1)`, `M = gcd` | printed (`SHEET6-L1.md:70-92`) |
| Cor 6.1 (p. 32) | degree law / q-law `d_q = kbar deg p_f / D_f` | printed; holds at all 10 route vertices (checker C1) |
| St 3.9 / 3.17(i) / 3.11(i) | elementary equality / composite f-equality / monotone counts | printed (`SHEET6-R6-REVIEW.md:50-66`) |
| St 8.3(ii) | member count equality | **NOT relied on at the dead member** (scoping correction `SHEET6-R6.md:137-140`); used only where re-derivable from Prop 8.1 + monotonicity |
| BOOK R1.0–R1.4, R2.1/R2.2, P1, P2 | chain/merge/terminal numerics | PROMOTED (`BOOK-OFFAXIS.md`) |
| §11a census row `(9,15,7,3)@2` | the priced arrival `w_U=1/2 (lambda 4; M2,4)`, recorded `nu_U=7` legal | PROMOTED |
| grok-sixcells replay | per-vertex T1 substitutions (ground truth) | SOUND (`xmodel/grok-sixcells-review.md`) |
| **campaign formalization of the tower laws** (§2 below) | the delta/death-gap/aliveness calculus | **calibrated, not printed-verbatim**: reproduces the entire td=6 template genome (checker C2) but has not itself been hostile-reviewed. This is the first thing a reviewer should attack. |

No CONJECTURE beyond the promoted set enters the kill. The kill is
route-family-scoped, not cell-scoped (§6). Fiber-zero gauge throughout
(`f := f_old - a`); PLUS tower `h_0 = g`, base `f`; orientation
`L = rootward -> U = poleward` everywhere.

## 1. The route and its decorated spine (banked, all-green)

Tree (design §3.2, arrows poleward):

```text
R0
|
G
+-- N  -- P1                    (chain 1: synchronization stack)
+-- H2 -- F3 -- F2 -- F1 -- P2  (chain 2: the priced lambda=4 witness)
```

Complete decoration table (all entries verified by checker C1 against
(F3)/(F4), R1.2 (H1–H2), R2.1-II (H4), E5-III (H5–H6), Prop 9.3 offsets
(J4), the x-degree drop law (J5)/St 3.17(i), the q-law, and (H7)/(H8)
with exact i-sync):

| v | kappa | pi | kbar | nu | rho | w | M | (d_p,d_q) | i | deg p_f | D_f | d_f | d_g |
|---|---:|---|---:|---:|---|---|---:|---|---:|---:|---:|---|---|
| R0 | 1 | 0 | 1 | 1 | 1/3 | — | — | root | — | 203490 | 67830 | 67830 | 101745 |
| G  | 7 | 2/7 | 5 | 7 | 1/3 | 2/3 | 3 | (9,15) | 22610 | 203490 | 67830 | 9690 | 14535 |
| N  | 79135 | 56523/79135 | 22612 | 11305 | 2 | 2 | 1 | (11305,11306) | 2 | 22610 | 45220 | 4/7 | 6/7 |
| P1 | 158270 | 31653/31654 | 5 | 2 | 1 | 2 | 1 | pole (2,3) | — | 2 | 2 | 1/79135 | 3/158270 |
| H2 | **7** | 3/7 | 4 | 7 | 1/2 | 1/2 | 2 | (14,8) | 3230 | 45220 | 22610 | 3230 | 4845 |
| F3 | 35 | 32/35 | 3 | 5 | 1/2 | 1/2 | 2 | (38,6) | 170 | 6460 | 3230 | 646/7 | 969/7 |
| F2 | 595 | 118/119 | 5 | 17 | 1/7 | 2/7 | 7 | (119,35) | 10 | 1190 | 170 | 2/7 | 3/7 |
| F1 | 2975 | 2971/2975 | 4 | 5 | 1/4 | 3/4 | 4 | (20,16) | 2 | 40 | 10 | 2/595 | 3/595 |
| P2 | 8925 | 1784/1785 | 5 | 3 | 1/2 | 3/2 | 2 | pole (4,6) | — | 4 | 2 | 2/8925 | 3/8925 |

Highlights, each an exact identity in the checker:

- **H5a in action.** `kappa_H2 = 7 = nu_H2*kappa_G/nu_G`, *not*
  `kappa_G*nu_H2 = 49`. With 49 the frame `kbar_H2 = 4` is unreachable;
  with the Q-value the (J4) case-III offset `n/(nu_G*kappa_H2) = 1/7`
  lands `pi_H2 = 3/7` and `kbar = 7(1-3/7) = 4` exactly. E5 `(g')/(h')`
  and the congruence `n = -nu_F*kbar_G (mod nu_G)` hold with the raw
  `n = 7`.
- **Both pole equalities.** `d_f + d_g = 1 - pi` (Prop 4.1) closes at
  P1 (`5/158270`) and P2 (`5/8925`) after nine transported edges — a
  stringent end-to-end audit of the whole x-degree layer.
- **Terminal package.** `(R1)-(R3)`: `w_G = 2/3`, `M_G = 3`, `j = 1`,
  `R_term = 3`, `psi = 2`, budget `4 = 6 - psi` attained by the arrival
  ledger `2+1+1+0+0`; `k_f = 203490`, `l_f = 67830`, corrected (R5)
  chart swap recorded; the (R6) Keller identity is *stated* in the
  certificate with `K = 2374050 = lcm(kappa_v)` (emission is milestone
  2 and is moot for this route unless review overturns §5).
- **Arrival.** The recorded §11a arrival `(w_U, nu_U) = (1/2, 7)` at
  `lambda = 4` (raw `M2 = 2` and `4`) is H2's frame; the P2-legality
  `mu0 | M`, `nu = -1 (mod mu0)` is checked.
- **Local layer.** All six T1 rows (G, N, H2, F3, F2, F1) re-derived
  from the factored patterns by exact eta-calculus at two generic A
  samples — the certified `s(t)` and `C~` of
  `xmodel/sol-td7-law.md:270-283` / grok's table, including
  `C~_G = -14A^2/15` with `B_g = (2/3)A_g` — plus both Prop 5.3 pole
  Wronskians (P6)/(P7).
- **LEAD-PILOT gate.** The 83/74 system regenerates from certificate
  data alone (local rows from the T1/Wronskian layer, (L9) direction and
  derivative rows from the edges, (P9) separations, (P10) scale
  transports with per-edge exponent audits, all 37 guards) and is
  token-for-token identical to the literal block extracted from
  `xmodel/sol-gluing-design.md` §3.5 at check time; the (P11)–(P13)
  rational anchor satisfies all 74 regenerated rows exactly (including
  the `7^22610`-sized scale values, evaluated as exact integers).

## 2. The tower calculus (formalization + template calibration)

The certificate's tower laws, assembled from the printed statements:

- ladder: `h_0 = g`, `h_{j+1} = h_j^{k_j} - sigma_j f^{l_j}`,
  `gcd(k_j, l_j) = 1`; `alpha_0 = 0`,
  `alpha_{j+1} = alpha_j + (k_j - 1) l_j / k_j` (Prop 4.2 (9));
- per vertex: `delta_j(v) = kappa_v (d_f + d_{h_j} - alpha_j d_f - 1 +
  pi_v) in N`, strictly decreasing; `m_v` = first zero (Prop 4.2 proof,
  p. 20); equivalently `delta_j(v) = D_{f,v} * g_j - kbar_v` with the
  **level gap** `g_j := l_j/k_j + 1 - alpha_j`;
- alive (`j < m_v`): `(h_j^+)^{k_j} = sigma_j (f^+)^{l_j}` at `v`
  (Prop 4.2(iii)); so `p_{h_j,v} = H * p_{f,v}^{l_j/k_j}` with **every
  factor exponent a nonnegative integer**, and
  `d_{h_j,v} = (l_j/k_j) d_{f,v}`;
- dead (`j = m_v`): `p_{h_m,v} = S p_red^{k_v} q_v`,
  `k_v = i_v(mu_v - 1)`, `mu_v = alpha_{m_v}` (Prop 8.1(ii)/(iv));
- **death equation**: `delta_{m_v}(v) = 0` is equivalent to
  `g_{m_v} = kbar_v / D_{f,v}`, and (lemma, verified both ways in the
  checker) this is the same statement as Cor 6.1's q-law
  `d_q = kbar * deg p_f / D_f` combined with the St 3.17(i)-transported
  x-degrees — three interlocking derivations of one number;
- counts: St 3.9 elementary equality (all labels), St 3.17(i) composite
  f-equality, St 3.11(i) monotone `deg_U <= mult_L` in general; the
  St 8.3(ii) *dead-member* equality is deliberately **not** assumed
  (`SHEET6-R6.md:137-140`); at a death transition (alive at L, dead at
  U) count equality is *derived*: `mult = (l/k) deg p_{f,U} = k_U d_p +
  d_q = deg`, exactly;
- `M_v = gcd(deg p_f, deg p_g, deg p_{h_1}, ..., deg p_{h_{m_v}})`
  (Not 8.1).

Calibration (checker C2): on the td=6 template
(`SHEET6-TEMPLATE.md` §1) this calculus reproduces, with zero free
parameters: the delta tables `(104,34,4)/(100,30,0)/(10,0)/(0)` at
R/F_s/G_m/P_i; the depths `m = (>=3, 2, 1, 0)`; the gaps
`5/2, 5/6, 5/42`; the ladder `(2,3), (3,4), (7,23)`; the Prop 8.1
exponents `k_{F_s} = 19`, `k_{G_m} = 1` with degrees 414 and 16; and the
Not 8.1 M-gcds `3, 2, 1`. Every one of these is an independent exact
match against filed template data.

Route instantiation. The two poles pin the type: the pole death equation
`g_0 = kbar/D_f = 5/2 = l_0/k_0 + 1` holds at **both** P1 and P2, giving
`(k_0, l_0) = (alpha, beta) = (2, 3)`, `alpha_1 = 3/2`, i.e.
`h_1 = g^2 - sigma_0 f^3`. The level-0 pole collapses replay the
template mechanism exactly and are re-derived in the checker by exact
polynomial arithmetic:

- at P1, `(eta(eta^2 - (3/2)A))^2 - (eta^2 - A)^3` collapses to
  `-(3/4)A^2(eta^2 - (4/3)A)` — degree 2, the forced `B_{p1} = (3/2)A`
  being precisely the pilot's pole row, with the scale relation
  `m^2 = sigma_0 lam^3`;
- at P2, `(eta^6 + U eta^3 + V)^2 - (eta^4 - A eta)^3` collapses to
  `-(1/8)A^3 eta^3 + (9/64)A^4` — degree 3; the eta^12, eta^9, eta^6
  rows are killed exactly by `sigma_0`-normalization, `2U + 3A = 0` and
  `AU + 4V = 0` — the pilot's P2 rows are the level-0 tower collapse in
  disguise; and 3 equals the h_1-branch count arriving from F1's dead
  member (`mult(eta(t-A)^3 R1^2, c_f1) = 3`), an exact handoff.

So level 0 of the tower is not just consistent — it *is* the pole part
of the certified pilot.

## 3. The death-gap table and the level-1 clash

`g_j = kbar_v / D_{f,v}` at each prospective killer:

| vertex | gap | | vertex | gap |
|---|---|---|---|---|
| F1 | **2/5** | | H2 | 2/11305 |
| F2 | 1/34 | | G | 1/13566 |
| F3 | 3/3230 | | N (nu=11305 rep.) | **5653/11305 ≈ 0.50004** |

Since `delta_j(v) = D_{f,v} g_j - kbar_v` must be strictly decreasing in
`j` at every vertex (in particular at G, which sees all levels), the
levels are globally sorted by gap, descending. Chain-2's five gaps are
already strictly decreasing rootward — internally consistent. The
problem is chain 1.

**Chain 1 is forced to exist and forced to be neutral.** (H8) i-sync at
G requires `deg p_{f,P1} = 2` to ladder up to `i_G = 22610` through
chain-1 vertices; the merge handshake fixes the arriving state at
`w = 2` (chain 1 frozen, `BOOK-OFFAXIS.md:521-529`); the budget is
saturated (`4 = 6 - psi`), so every chain-1 step is uncharged; and the
R1.2 w-law gives `w_child = w_par * n/Delta` with `n/Delta < 1` for
every `n >= 2` — once w drops below 2 it can never return (verified for
a lattice of `(n, nu)` in the checker). Hence chain 1 is a stack of
clean `n = 1` neutrals. The f-degree ladder `2 -> ... -> 22610` forces
the product of the stack's characteristics to be `22610/2 = 11305 =
5*7*17*19`, an **odd** number; and the pole-adjacent stack vertex X has
(root law + pole mult 2, any shape) `deg p_{f,X} = 2 nu_X`,
`d_{q,X} = nu_X + 1`, so its death gap is

```
gap(X) = (nu_X + 1)/(2 nu_X)  in  (1/2, 3/5],   nu_X | 11305, nu_X >= 5,
```

shape-independent. The design's §3.2 representative is the one-vertex
stack `X = N`, `nu_X = 11305`, gap `5653/11305`.

**The clash.** `gap(X) > 1/2 > 2/5 = gap(F1)` always, so ladder level 1
belongs either to X or (impossibly, see case B) to F1:

- **Case A (X kills level 1).** Then `l_1/k_1 = gap + alpha_1 - 1 =
  (2 nu_X + 1)/(2 nu_X)`, i.e. `(k_1, l_1) = (2 nu_X, 2 nu_X + 1)` with
  `k_1 >= 10`. At F1, level 1 must then be either *dead* — impossible,
  `delta_1(F1) = 0` would force `gap(X) = kbar_{F1}/D_{F1} = 2/5` — or
  *alive*, which by Prop 4.2(iii) forces the factor exponents of
  `p_{f,F1}^{l_1/k_1} = [(t-A)^2(t-B)(t-D)]^{2 l_1/k_1}` to be integers:
  `4 l_1 / k_1` and `2 l_1 / k_1`, i.e. `k_1 | 2`. But `k_1 = 2 nu_X >=
  10`. Contradiction. (Independently, `delta_1(F1) = 1 + 5/nu_X` is a
  positive integer only for `nu_X = 5`, so 14 of the 15 stacks die
  already at delta-integrality; `nu_X = 5` dies at the exponents
  `(22/5, 11/5)`.)
- **Case B (F1 kills level 1).** Then `(k_1, l_1) = (10, 9)` from
  `2/5 + 1/2 = 9/10`. At X, level 1 must be dead — needs
  `(nu_X + 1)/(2 nu_X) = 2/5`, i.e. `nu_X = -5`, impossible — or
  alive — needs `2 l_1/k_1 = 9/5 in N`, false. Contradiction, for every
  stack (X always exists).

The checker runs both cases for all 15 admissible `nu_X` and requires
every one refuted. **No global ladder exists; the tower certificate
cannot be completed for any representative of the synchronized direct
route family.**

Fixed-representative corroboration (`nu_N = 11305`, the design's own
choice), banked as `m2_branch` in the certificate: `m_G = 1` dies
because Prop 8.1 at N demands `deg p_{h_1,N} = 1*11305 + 11306 = 22611`
while only `mult(p_red^11305 q, c_g) = 11306` h_1-branches arrive
(St 3.11(i)); `m_G = 2` with h_1 alive at G with exponent `s` dies
because the N-side valuation-drop window
`[deg_U * dpi, mult_L * dpi]` pins `s = 22611` *exactly* while the
H2-side window pins `s = 11309` *exactly* (both windows degenerate to a
point; the checker verifies both boundary coincidences).

## 4. Why this does not contradict anything banked

- The §11 ADDENDUM certifies the transport tier + vertex-local T1 +
  both priced completions. All of that is *reproduced* here (checker
  C1/C4). The tower/coefficient tier was explicitly left open
  ("the remaining instrument for the six is the coefficient-gluing
  tier").
- The design's §3 pilot is the *leading* tier; its SAT verdict is
  reproduced from this certificate and stands. §3.7 explicitly lists the
  tower data as "not present in the filed route artifacts and may not be
  guessed"; CONJECTURE (full-pilot survival) anticipated exactly this
  test — the answer for the direct route family is negative.
- §11a's census is arrival-tier and untouched.
- The kill needs no St 8.3(ii) dead-member equality (the scoping
  correction is respected); it uses only the monotone count law plus
  vertex-local Prop 8.1/4.2/Cor 6.1.

## 5. What would have to be wrong for the route to survive

For a hostile reviewer; the checker's obstruction block fails loudly if
any of these is repaired and re-run:

1. **The global-single-ladder reading of Prop 4.2.** If the thesis's
   tower could branch per pole (different `(k_j, l_j)` on chain 1 vs
   chain 2 at the same level index), the clash dissolves. The printed
   tower is one sequence `h_0, h_1, ...` of global polynomials; the td=6
   template uses one ladder across both poles (both P_i share
   `(2,3),(3,4),(7,23)`), and `SHEET6-R6.md:10` reads `gcd(k1,l1)=1`
   from Prop 4.2(i) as global data. A per-branch tower would be a new
   reading requiring its own review.
2. **The aliveness identity Prop 4.2(iii) at non-killed levels.** If a
   level can sit strictly between alive and dead at a vertex (delta_j >
   0 without the leading-part identity), case A/B both reopen. The
   template exhibits no such state and `SHEET6-R6.md:126` uses "h2 ALIVE
   at F_s" as the delta_2 > 0 reading.
3. **The death equation `g_m = kbar/D_f`.** It is forced by delta_m = 0
   plus Cor 6.1's q-law plus f-transport — three independently printed
   inputs that interlock (checker verifies the equivalence numerically
   at all vertices). An error here would have to break one of the three.
4. **The chain-1 forcing.** If a charged chain-1 step were budget-legal
   (it is not: equality `4 = 6 - psi`), or w could return to 2 after an
   `n >= 2` clean step (it cannot: `n < Delta`), or the pole-adjacent
   shape could evade `gap = (nu+1)/(2nu)` (root law + pole mult 2
   close this), the stack family would widen.
5. **H5a/E5.** Under the forced-nu reading the route data change; the
   two-cell sub-book (CONJECTURE U_7C) is a different perimeter. This
   certificate lives on the promoted Q-value book, as instructed.

## 6. Scope and consequences

- **KILLED (pending review):** the tower tier of every synchronized
  representative of the *direct* `(2/3,3,2)` completion of
  `(9,15,7,3)@2` in the design §3.2 family — the design's milestone-1
  target route. Milestone 2 (jet-window emission) for this route is moot
  unless §5 overturns a dependency: there is no tower certificate to
  emit windows from.
- **NOT killed:** the `(9,15,7,3)@2` cell. Its second budget-equality
  completion — the trunk `(35,15,7,5)` step to `(2/5,5,1)` — has a
  different terminal frame (`psi = 1`, budget 5) and a different
  synchronization problem; nothing here examines its tower. The other
  16 §11a cells are untouched.
- **Structural lesson** (conjecture-flavored, for the next certificate):
  the clash mechanism is parity — the type-(2,3) half-integer
  `alpha_1 = 3/2` meets a pole-adjacent gap `(nu+1)/(2nu)` whose ladder
  step `k_1 = 2 nu_X` is even and large, while the smallest-i chain-2
  vertex (`i_{F1} = 2`, forced by the (1,2,3) pole) caps `k_1 | 2`. Any
  route whose two pole chains meet the same merge with coprime-odd
  degree ratio on one side and a tiny `i` on the other faces the same
  squeeze; this is a candidate general kill lemma for the trunk route
  and the other 16 cells, and the natural milestone-2 replacement.

## 7. Reproduction

```bash
cd /Users/dc/code/math/jc72108
python3 cases/tower_check.py    # < 1 s, exit 0, 258 checks
```

The engine validates `cases/towers/t9_15_direct.json` (C1 spine, C1b
scale-exponent audits, C2 td=6 calibration, C3 tower layer + 15-stack
two-case obstruction exhaustion, C4 T1/Wronskian layer at two generic
A-points, C5 LEAD-PILOT token-for-token regeneration against the literal
§3.5 block extracted from `xmodel/sol-gluing-design.md` at run time,
C5b the exact rational anchor on all 74 regenerated rows, C6 the design
§3.6 negative-perturbation list — T1 sign flip, omitted nu in a
derivative, `B_g = (3/2)A`, non-H5a `kappa_H2 = 49`, mixed-reading
case-III `n`, one-slot scale shift, tampered obstruction record — each
must raise at least one failure, and does). No msolve, no
network, no floats; `ops/FLEET.md` untouched. The certificate JSON is
the machine-readable statement of record; this file is its derivation.

Files: `cases/towers/t9_15_direct.json` (certificate),
`cases/tower_check.py` (checker), this document. No git commit was made.
