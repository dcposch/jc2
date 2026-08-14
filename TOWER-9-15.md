# TOWER-9-15.md — tower certificates for the (9,15,7,3)@mu0=2 completions

Status: **MILESTONE 1 EXECUTED (2026-08-13); direct-route kill REVIEWED
SOUND-WITH-ERRATA (`xmodel/grok-tower-review.md`), errata folded in
(Case C §3, trunk §7); Sol's pre-repair review (`sol-tower-review.md`,
BROKEN) triaged: finding 1 = the already-repaired Case C (identity
verified row-for-row, §5), findings 2/3 repaired here (§8 schema
reconciliation; §7a `M_U`/free-characteristic coverage via the
universal exhaustion); the CELL-LEVEL kill is ON HOLD pending Sol
re-review.**
Engine: `cases/tower_check.py` (exact `Fraction`, no floats, no solver;
647 checks over both certificates incl. a 12-case negative-perturbation
self-test, exit 0). Certificates: `cases/towers/t9_15_direct.json`,
`cases/towers/t9_15_trunk.json`.
Task source: `xmodel/sol-gluing-design.md` §5.4 first solver objective,
milestone 1, plus the coordinator's post-review work items (Case C
repair; trunk machine-check; Sol finding-2/3 disposition).

VERDICT IN ONE PARAGRAPH. Both priced completions of `(9,15,7,3)@2`
(direct case-IV at `(2/3,3,2)`, λ=4; one trunk step through `(35,15,7,5)`
to `(2/5,5,1)`, λ=5) admit complete, exactly verified decorations of
every vertex and edge at the numerical and leading-coefficient tiers —
every `(kappa, pi, kbar, nu, rho, w, M, i, d_p, d_q, deg p_f, D_f, d_f,
d_g)` closes under the printed transport laws with the promoted
Q-value/H5a kappa and the E5 case-III identities, and the design's §3.5
LEAD-PILOT (83 vars / 74 rows, SAT over Q) regenerates from the direct
certificate token-for-token. But in **both** cases the approximate-root
tower layer cannot be completed: ladder level 1 sits in a window claimed
by the (H8)-forced chain-1 synchronization stack whose death step can
never be integral while the chain-2 vertex F1 is alive — a three-case
exhaustion (empty prefix / F1-first / non-killing prefix then X-death)
over all 15 admissible stacks, terminal-independent because the clash
lives entirely on the pole-to-merge subtree the two completions share.
Under the formalized tower laws — calibrated to reproduce the td=6
template genome exactly, and with the single-ladder reading now pinned
to printed St 8.3(i) + Cor 6.1 + Not 4.1 per the review — the
`(9,15,7,3)@2` **CELL is tower-dead: both §11a deduplicated equality
completions are obstructed**. This would be the campaign's first
cell-level next-tier kill; it is pending review. "Untouched" below
always means "not machine-checked", never a survival claim.

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
| St 8.3(i) (p. 41) + Cor 6.1 searrow + Not 4.1 prefix order | single shared ladder + same `h_j` on both merge branches while alive | printed; the review's citation upgrade (`grok-tower-review.md` finding 3: every non-pole route vertex is searrow `T_a^&`, `(1-pi) deg p_f/d_f > 1` re-derived there) |
| alive/dead dichotomy of printed (10), p. 19 | no third J-state; `delta_j > 0 <=> alive with (iii)` | printed (`grok-tower-review.md` finding 4) |
| **campaign formalization of the tower laws** (§2 below) | the delta/death-gap/aliveness calculus | reviewed against pp. 19–22/32/39–41: SOUND-WITH-ERRATA; the two errata (Case C, trunk scope) are repaired in this revision |
| trunk step data | the unique λ=1 menu edge `(35,15,7,5)`, `n=16`, `B=2A`, `C=14A²/3` | dual-certified (`sol-sixcells.md` §2.4, `grok-sixcells-review.md` findings 1–3) |

No CONJECTURE beyond the promoted set enters either kill. The
direct-family kill is reviewed; the joint cell-level statement (§7) is
new. Fiber-zero gauge throughout (`f := f_old - a`); PLUS tower
`h_0 = g`, base `f`; orientation `L = rootward -> U = poleward`.

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

Since `delta_j(v) = D_{f,v} g_j - kbar_v in N` is strictly decreasing in
`j` at every vertex, the ladder gaps `g_j` strictly decrease, each
vertex dies at the first index whose `g_j` equals its own `kbar/D_f`,
and a vertex's descent can never *skip* its own zero (that would make
some `delta_j(v) < 0`). Note carefully — this is the review's finding-1
correction — the descent does **not** force every ladder index to be
some vertex's death: non-killing indices are legal (see Case C below).
Chain-2's five gaps are already strictly decreasing rootward —
internally consistent. The problem is chain 1.

**Chain 1 is forced to exist and forced to be neutral.** (H8) i-sync at
G requires `deg p_{f,P1} = 2` to ladder up to `i_G = 22610` through
chain-1 vertices; the merge handshake fixes the arriving state at
`w = 2` (chain 1 frozen, `BOOK-OFFAXIS.md:521-529`); the budget is
saturated (`4 = 6 - psi`), so every chain-1 step is uncharged; and the
R1.2 w-law gives `w_child = w_par * n/Delta` with
`Delta - n = (n-1)(nu-1) >= 1` for every `n >= 2` — once w drops below
2 it can never return. Hence chain 1 is a stack of
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

**The clash (three-case form; erratum repair per review finding 1).**
The first writeup claimed level 1 belongs to X or F1 outright. That
dichotomy was not exhaustive: Prop 4.2 does *not* require some vertex to
die at every ladder index, and a **non-killing prefix** of ladder steps
is printed-legal. The review exhibited the exact menu, now machine-
checked: while X and F1 are both alive, Prop 4.2(iii)/Prop 8.1
(`i l_j/k_j in N` at `i = 2` with `gcd(k_j, l_j) = 1`) cap every prefix
step at `k_j | 2`; the half-integer gap grid meets every window
`(gap(X), 5/2)` in the same three points, so the legal non-killing
level-1 pairs are exactly `(k,l) in {(1,2), (2,3), (2,5)}` (gaps
`3/2, 1, 2`), and each has positive-**integer** `delta_1` at every
non-pole vertex (checker prints all of them — they kill nobody and are
genuinely legal). The repaired exhaustion:

- **Case A (empty prefix; X kills level 1).** `(k_1, l_1) =
  (2 nu_X, 2 nu_X + 1)` with `k_1 >= 10`: refused by the `k | 2`
  aliveness cap at F1 (exponents `2(2 nu_X + 1)/nu_X`-type nonintegral).
  (Independently, `delta_1(F1) = 1 + 5/nu_X in N` only for `nu_X = 5`,
  which dies at the exponents `(22/5, 11/5)`.)
- **Case B (F1 kills level 1 first).** Impossible outright:
  `delta(X) in N` strictly descends and cannot skip its own zero, so X
  (gap `> 2/5`) must die strictly before any `g_j = 2/5` level exists;
  death at X with gap `2/5` would need `nu_X = -5`. (And h1 alive at X
  under `(k_1, l_1) = (10, 9)` needs `2*9/10 = 9/5 in N`, false.)
- **Case C (nonempty non-killing prefix, then X dies).** After `r`
  prefix steps with `k = 2` (each adds an odd `l/2` to alpha; `k = 1`
  steps add 0), `alpha_m = 3/2 + r/2 (mod 1)`. X-death at level `m`
  demands `l_m/k_m = gap(X) + alpha_m - 1 = alpha_m - 1/2 +
  1/(2 nu_X)` with `k_m | 2` (F1 still alive):
  `k_m = 1` forces `2 nu_X | r nu_X + 1` — impossible for `r` even
  (`1`) or odd (`nu_X + 1 < 2 nu_X`); `k_m = 2` forces `nu_X | 1`.
  No prefix length escapes (closed form over the `r`-parity, plus
  explicit `r = 0..5` in the checker).

The checker runs all three cases; the prefix menu, the `k | 2` cap, and
the window-emptiness (`no vertex gap inside (gap(X), 5/2)`; intermediate
stack gaps `< 2/5`) are each separate checks.

**What the original 15-stack exhaustion covered, precisely** (Sol
finding-3 hygiene): it quantified over the chain-1 synchronization
stacks — via their pole-adjacent class `nu_X | 11305` — of the *fixed*
chain-2 representative (`M_U = 2` at H2, `nu_F3 = 5`, the unique charged
predecessor DAG, one padding vertex `nu = 7`). It did not by itself
cover the `M_U = 4` raw arrival, the free pure-b characteristic, or
other padding stacks.

**Universality (the extension).** Inspect the three refutations: none
uses `nu_X | 11305`, oddness, or any other trace of the fixed chain-2
realization. They are identities in `nu_X >= 2`: case A needs only
`2 nu_X > 2`; case C needs only that `2 nu_X` never divides
`r nu_X + 1` (from `2nu - (nu+1) = nu - 1 >= 1`) and that `nu_X` never
divides 1; case B needs only
`5(nu+1) - 4nu = nu + 5 > 0`. The checker states each as an algebraic
identity instantiated on `nu_X = 2..300` (`UNIVERSAL case A/B/C`
checks), so **every chain-1 stack of every chain-2 realization is
covered** — the 15 divisor classes are the displayed representative's
instantiation, not the coverage boundary. The chain-2-side freedom
(`M_U`, free characteristic, padding) is closed in §7a. **No global
ladder exists for any representative of either completion's route
family.**

Fixed-representative corroboration (`nu_N = 11305`, the design's own
choice), banked as `m2_branch` in the certificate: `m_G = 1` dies
because Prop 8.1 at N demands `deg p_{h_1,N} = 1*11305 + 11306 = 22611`
while only `mult(p_red^11305 q, c_g) = 11306` h_1-branches arrive
(St 3.11(i)); `m_G = 2` with h_1 alive at G with exponent `s` dies
because the N-side valuation-drop window
`[deg_U * dpi, mult_L * dpi]` pins `s = 22611` *exactly* while the
H2-side window pins `s = 11309` *exactly* (both windows degenerate to a
point; the checker verifies both boundary coincidences).

## 4. Review status and what the errata changed

`xmodel/grok-tower-review.md` (hostile, on-page against
`refs/sigray_full.pdf` pp. 19–22/32/39–41): **SOUND-WITH-ERRATA** — the
direct-family kill stands; attacks on the single-ladder reading, the
alive/dead dichotomy, and the death equation all fail on the printed
pages (findings 3–5). Two errata, both repaired in this revision:

1. **Case C** (findings 1 + 6): the original A/B dichotomy silently
   assumed every ladder index kills a vertex; the printed theory allows
   non-killing steps. Repaired in §3 and in the engine (the prefix menu,
   its delta-integrality, the `k | 2` cap, and the all-lengths closed
   form are now explicit checks; the reviewed `3 == 3` tautology in the
   F1→P2 handoff is replaced by the real `mult(eta(t-A)^3 R1^2, c) = 3`
   computation at two exact points, matched against the degree of the
   computed P2 collapse).
2. **Trunk scope** (finding 2): "different synchronization problem;
   nothing here examines its tower" was too strong — the clash is
   terminal-independent. Now machine-checked: §7.

Also folded: the single-ladder dependency is cited to printed
St 8.3(i) + Cor 6.1 + Not 4.1 (not to `SHEET6-R6.md:10`); the q-law is
labeled the Prop 8.1/theta rewrite consistent with Cor 6.1, not Cor 6.1
verbatim; `Delta - n = (n-1)(nu-1) >= 1` replaces the w-monotonicity
lattice as the cited identity; check counts below are transcript counts,
not theorems.

**Sol review timeline** (`xmodel/sol-tower-review.md`, BROKEN verdict):
Sol reviewed the pre-repair snapshot (258-check engine, two-case
exhaustion, direct certificate only). Its CRITICAL finding 1 is the
same gap Grok found: the alive-alive level-1 pairs — and its table is
*exactly* the repaired Case C menu (§5 for the row-for-row identity).
Its finding 6 overlaps Grok's finding 6 (tautology, hard-coding), both
repaired. Its findings 2 (schema) and 3 (`M_U = 4` / free-characteristic
coverage) were live against the current revision and are addressed in
§8 and §7a respectively. Its findings 4 and 5 CONFIRM (H8) usage and
the gap arithmetic.

## 5. Why this does not contradict anything banked

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
- §11a's census is arrival-tier: the 17-cell list and this cell's
  arrival row are reproduced, not retracted. What the joint kill removes
  is the *tower/coefficient* life of both deduplicated `(9,15)` equality
  routes (all 4 raw arrivals), not the cell's row in the arrival book.
- The kill needs no St 8.3(ii) dead-member equality (the scoping
  correction is respected); it uses only the monotone count law plus
  vertex-local Prop 8.1/4.2/Cor 6.1, with St 8.3(i) entering only for
  the shared-ladder identification of live members.
- **Sol finding 1: resolved by repair, same pairs.** Sol's CRITICAL
  table of unhandled alive-alive level-1 pairs
  (`sol-tower-review.md:56-69`) is the Case C menu of §3, identically:
  pairs `{(1,2),(2,3),(2,5)}`, gaps `3/2, 1, 2`, X-exponents `4, 3, 5`,
  F1-exponents `(8,4), (6,3), (10,5)`, `delta_1(F1) = 11, 6, 16`, and
  the full delta rows at `(G,H2,F3,F2,F1)` —
  `(101740,33911,4842,250,11)`, `(67825,22606,3227,165,6)`,
  `(135655,45216,6457,335,16)`. The checker verifies this identity
  row-for-row (`Sol table row` checks) on both certificates, and Sol's
  disposition item 2 ("continue the three branches to their later
  deaths") is exactly the Case C closed form (any prefix length, both
  `k_m` values). The finding was found independently by both reviewers
  and repaired once.

## 6. What would have to be wrong for the kills to fail

For a hostile reviewer; the checker's obstruction block fails loudly if
any of these is repaired and re-run. Doors 1–3 were attacked by the
review and held (findings 3–5); the sixth door (a non-killing level 1)
was found, entered, and closed (finding 1 / §3 Case C).

1. **The single-ladder reading.** Now pinned to printed St 8.3(i)
   (`h_{j,F} = h_{j,G}` and `(k_j, l_j, s_j)` agree for `j < m_F` on
   `F = G*c`) + Cor 6.1 searrow (`F < F'` at every non-pole route
   vertex: `(1-pi) deg p_f/d_f > 1` at all of them) + Not 4.1 prefix
   order. A per-pole ladder at a shared alive level contradicts these
   pages (review finding 3); if only one branch is alive, that is Case
   A/B/C, refuted.
2. **The aliveness dichotomy.** Printed (10) has exactly two states
   (`J = 0` alive with (iii), equality dead); a third state would need a
   new page (review finding 4).
3. **The death equation `g_m = kbar/D_f`.** The alive rewrite of the
   printed delta plus (10) at `m`; interlocks with the Prop 8.1/theta
   q-law rewrite and St 3.17(i) transport (review finding 5).
4. **The chain-1 forcing.** If a charged chain-1 step were budget-legal
   (it is not: `4 = 6 - psi` direct, `5 = 6 - psi` trunk, both
   saturated), or w could return to 2 after an `n >= 2` clean step
   (`Delta - n = (n-1)(nu-1) >= 1`), or the pole-adjacent shape could
   evade `gap = (nu+1)/(2nu)` (root law + pole mult 2 close this), the
   stack family would widen.
5. **H5a/E5.** Under the forced-nu reading the route data change; the
   two-cell sub-book (CONJECTURE U_7C) is a different perimeter. These
   certificates live on the promoted Q-value book, as instructed.

## 7. The trunk completion dies by the same clash: the cell-level kill

`cases/towers/t9_15_trunk.json` is the complete decorated spine of the
second (and last) §11a deduplicated equality completion: the trunk
vertex `T = (35,15,7,5)` at frame `(1/5,3,7;2/5,5)` inserted rootward of
G via the unique λ=1 menu edge (`n = 16`, continuation at T's triple
orbit, `mu_e = 3`), case-IV terminal at T with `(w,M,psi) = (2/5,5,1)`,
`j = 3`, `R_term = 5/3`, budget `5 = 6 - psi` saturated,
`k_f = 2374050 = 35*67830`, `l_f = (3/5)k_f = 1424430`. The whole spine
re-closes exactly (checker C1 on the trunk certificate): T's Cor 6.1
q-law `15 = 3*2374050/474810`, the (2.1) row `(1/3+16)/21 = 7/9 =
35/45`, kappa doubling `kappa_G = 49`, `kappa_H2 = 49` (H5a Q-value),
both pole Prop 4.1 equalities at the rescaled charts (`5/1107890`,
`5/62475`), T's T1 row `B = 2A, C = 14A^2/3` re-derived at two points,
and `K = 16618350`.

**Terminal-independence, machine-checked** (review finding 2, upgraded
from argument to checks): (H8) at G reads `deg p_{f,H2} = i_G*mu0 =
45220` up from the priced chain-2 regardless of G's rootward neighbour,
so `i_G = 22610`, the chain-1 f-ladder `2 -> 22610` (nu-product 11305,
odd), `i_{F1} = 2`, both pole types (2,3), and the entire death-gap
table on `{X-stack, F1, F2, F3, H2, G}` are *identical* to the direct
route (same `kbar/D_f` at every shared vertex — the kappa rescaling
cancels). The only new datum is T's own gap `1/158270 < 1/13566 =
gap(G)`, far below the level-1 window `(gap(X), 5/2)` — checked
explicitly ("no non-stack death gap inside the window"). The three-case
exhaustion of §3 then runs verbatim on the trunk certificate: all 15
stacks, cases A/B/C, every one refuted.

### 7a. Arrival and predecessor variants: all four raw records covered

Sol finding 3: the census dedup drops `M_U`, leaving 4 raw equality
records (`M_U in {2,4}` x `{direct, trunk}`), and the chain-2
predecessor is free in the pure-b characteristic and in zero-cost
neutral padding. Coverage, machine-checked (C3-V on both certificates):

- **The free data are exactly `(nu3, padding, M_U)`.** The charged
  predecessor DAG is unique (`grok-sixcells-review.md` finding 4, SOUND:
  `(3/2,2) -λ2- (20,16) -λ1- (119,35) -λ1- pure-b l7e3 - (1/2,*)`; "no
  other charged parent exists"), so F1 = `(20,16)` with `i = 2` and
  F2 = `(119,35)` with `i = 10` sit on *every* realization, and the
  freedom is the pure-b characteristic `nu3`, the neutral padding
  stack, and the arrival `M_U`.
- **`M_U` realization.** The pure-b family `(3+7 nu3, 1+nu3)` has
  `M = gcd(4, nu3+1)`: `nu3 = 1 (mod 4)` gives `M = 2` (displayed:
  `nu3 = 5`, then padding `H2 = (14,8)` arrives with `M_U = 2`);
  `nu3 = 3 (mod 4)` gives `M = 4` and the pure-b vertex itself is the
  legal odd-characteristic arrival (minimal: `nu3 = 7`, cell `(52,8)`,
  `i_G = 4420`, chain-1 product `2210`). Both variants' frames,
  BOOK-2.1 transports (`n = (7+17 nu3)/2`), `kbar = (1+nu3)/2`,
  `rho = w = 1/2`, i-ledgers, `k_f`/`i_T` data, and E5 (I4)
  `nu_U`-freeness are individually checked, per terminal.
- **Characteristic-independence of the clash** (the finding-2 method,
  applied to predecessors): the clash needs only (i) `gap(X) =
  (nu_X+1)/(2 nu_X)` — chain-1-side, derived from P1's frame alone;
  (ii) F1's cap `k | 2` and gap `2/5` — fixed by the unique charged
  DAG and the P2 handoff; (iii) window emptiness — parametric bounds
  `gap(F3'(nu)) = (1+nu)/(170(3+7nu)) < 2/5`, padding gaps
  `< 2/5` once `i >= 170`, intermediate chain-1 gaps `< 1/2`, all
  stated as identities and instantiated on `nu = 2..300`; (iv) budget
  saturation and the w-freeze — realization-independent. The universal
  `nu_X >= 2` refutation (§3) then applies to every stack of every
  variant — including the `M_U = 4` variant's *even* chain-1 product
  `2210` (e.g. `nu_X = 2`, gap `3/4`, case A pair `(4,5)`: refused).
  Parity note: if a variant made `i_G` odd, the chain-1 product
  `i_G/2` would not be integral and (H8) i-sync would fail at the
  spine tier — dead either way.

**Consequence (NEW, pending hostile review): the `(9,15,7,3)@2 cell is
tower-dead.** All four §11a raw equality completion records — both
deduplicated summaries, both `M_U` arrivals, every free-characteristic
and padding realization, every chain-1 stack — are obstructed at the
tower tier; there is no other completion in the promoted book
(`grok-sixcells-review.md` finding 2: the px5 census has exactly
these). This is the campaign's first cell-level next-tier kill.
Milestone-2 emission for this cell is moot unless review overturns a
dependency. An escape would have to change `i_{F1}`, the pole types,
the `gap(X)` formula, or the budget saturation — each pinned by data
shared across all variants and re-verified per certificate.

## 8. Schema reconciliation: design §1 `RouteCertificate` vs `td7-tower-certificate/v1`

Sol finding 2: the JSON schema is not the design's (F2) record. It was
never meant to be byte-compatible — it is an *obstruction* certificate —
but every design field must map to a field here, an equivalent, or an
explicit honest absence. The table below is normative; genuine semantic
omissions found in the audit have been fixed (marked FIXED).

| design §1 field | this certificate | status |
|---|---|---|
| `V, E, v_root, {v_pole}, K` (F2) | `vertices[]`, `edges[]`, `type: root/pole`, `K` | match |
| `pi_v, kappa_v, nu_v, kbar_v` | same names per vertex | match |
| `d_{f,v}` (x-degree) | `d_f` (rational) + `D_f = kappa*d_f` + `Dint = K*d_f` (K-integrality checked) | match (three normalizations recorded) |
| `i_v, d_{p,v}, d_{q,v}, M_v, rho_v, w_v` | same names | match |
| `lambda_v^lb / lambda_v^exact / authority` | `arrival.lambda_steps` + `terminal.budget` (equality-saturated; authority = px5 census + `grok-sixcells-review.md` finding 4 unique charged DAG) | match at route level; per-vertex split not separated (equality leaves no slack to allocate) |
| `mu_v, k_v` (F2a: `mu_v = alpha_{m_v}`, `k_v = i_v(mu_v-1)`) | `m` / `mu_k_note` per non-pole vertex: **proved jointly unrealizable** — these are the obstructed fields; poles carry `m = 0` | honest absence, FIXED (was silent; now stated per vertex) |
| `case_e, n_e, mu_e` | `case`, `n`, `mu_e` per edge | match |
| `chartMode_e, slots_e / {c_{e,j}}` | `chartMode: "PREFIX"` per edge — no slot certificate exists (milestone-2 object; design §1.5 names this label for partial projections) | honest absence, FIXED (was silent) |
| `TransportAuthority_{e,h}` | `transport_authority: {f: ST3.17_F, g: ST8.3_LIVE_j0, other_labels: NONE-fails-closed}` per edge | FIXED (was silent); h_j-labels beyond g have no authority — that is the obstruction |
| `Derived(N_e, {r_{e,h}}_h)` | `N_e, r_f, r_g` per edge, machine-checked: `N_e = K(pi_U - pi_L)`, `r_h = K(d_{h,L} - d_{h,U}) = deg p_{h,U} * N_e` | FIXED (was absent; now derived + verified on every edge, both certificates) |
| zero/nonzero + arrival label | `continuation` presence/absence + `arrival` block + case-III notes | match |
| shape `(eps, l, k, (m_j), ell_ex)` | `t1_local[].p_factors/q_factors/eps` (full factored shapes) + `type` strings | match (factored form) |
| tower labels `h_0..h_m, (k_j, l_j), side/base, d_{h_j,v}, m_v` | `tower.side/h0/base/type/ladder` level 0 complete (`(k_0,l_0) = (2,3)`, both pole collapses, `d_g` at every vertex = level-0 `d_{h_0,v}`); levels ≥ 1: `OBSTRUCTED` with the three-case proof | level 0 match; deeper levels are the theorem |
| `tower_s[j]` (sigma) | `sigma_relations` (P1/P2 scale relations `m^2 = sigma0 lam^3` etc.) — prose-level, not owned algebraic variables | honest partial: milestone-2 object; the obstruction needs no sigma value |
| `TopPatternCertificate` (pole/root) | `poles[].rows` + `root_pattern` + the C3 collapse checks (exact polynomials in-engine) | match at the tier used |
| `JetWindows / Omega_B` | none — no jet emission | honest absence (milestone 2; moot under the obstruction) |
| root/x-side terminal data | `terminal` block: (R1)–(R6) with k_f, l_f, d_0x, swap | match at numerical tier; (R6) stated not emitted |
| root-of-unity choices (F5) | none — no branch choices reached (obstruction precedes) | honest absence |
| `K` + Prop 3.1 suitability witnesses (J0) | `K = lcm(kappa_v)` labeled a **candidate** with per-chart `kappa_v \| K` rider; no Prop 3.1 witnesses | honest partial (Sol confirmed the checker tests only `K*pi, K*d_f`; `N_e/r_h` integrality now also exercises K on every edge) |
| completeness label | `tier` field: "spine COMPLETE, level-0 COMPLETE, levels >= 1 PROVED EMPTY" | FIXED (was only a status string) |

Two schema-level review points adopted verbatim: Sol's correction that
Prop 4.2 constructs per-vertex data and a common label needs a prefix
authority — recorded as the `single_ladder` law with St 8.3(i) +
Not 4.1 + Cor 6.1 and the searrow membership of every non-pole vertex;
and the relabeling demand — the `tier` field now says exactly what is
complete and what is proved empty, and the LEAD-PILOT gate is described
as a stored-fixture regression *plus* edge-derived direction/derivative
rows, not full IR validation (design §2.3 canonicalization is a
milestone-2 object).

## 9. Scope and consequences

- **KILLED, reviewed (Grok), Case C erratum repaired:** the tower tier
  of every synchronized representative of the direct `(2/3,3,2)`
  completion, now for every `M_U`/characteristic/padding realization
  (§3 universality + §7a).
- **KILLED, new, ON HOLD pending Sol re-review:** the trunk `(2/5,5,1)`
  completion (§7) and hence the `(9,15,7,3)@2` **cell** at the tower
  tier — all four §11a raw equality records (§7a). Per the
  coordinator, the cell-kill claim is not promoted until Sol re-reviews
  this revision; §11a is not edited from here.
- **NOT machine-checked** (never "safe", only unexamined): the other 16
  §11a cells. The mechanism is a candidate lemma for them, not a
  theorem (Grok finding 7): per-cell it needs (i) type-(2,3) poles,
  (ii) a pole-adjacent chain-1 gap in `(1/2, 3/4]` — universality
  removed the oddness ingredient — (iii) a small-`i` chain-2 vertex
  alive at the stack death (`k | i` tight; here `i_{F1} = 2`), (iv)
  budget saturation forbidding a charged chain-1 step. The right next
  artifact is the finding-7 checklist run over the 17-cell book —
  (type, min i on the priced chain-2, chain-1 budget residual,
  pole-adjacent gap vs smallest chain-2 gap) — each row either
  instantiating this squeeze as a corollary or naming its escape
  ingredient; that replaces milestone 2 for this cell.
- The LEAD-PILOT leading tier (83/74, SAT over Q — a necessary-prefix
  SAT point on a route family now tower-obstructed above it, per Sol's
  closing remark) and the §11a arrival census are reproduced and stand.

## 10. Reproduction

```bash
cd /Users/dc/code/math/jc72108
python3 cases/tower_check.py    # < 1 s, exit 0, 647 checks (transcript count)
```

The engine validates **both** certificates (`t9_15_direct.json`, then
`t9_15_trunk.json`): C1 spine incl. the g-layer (J5) drops and the
derived `N_e/r_f/r_g/chartMode/TransportAuthority` edge data, C1b
scale-exponent audits (direct), C2 td=6 calibration, C3 tower layer +
the **three-case universal** obstruction exhaustion (prefix menu with
the Sol-table row-for-row identity, `k | 2` cap, window emptiness,
UNIVERSAL `nu_X >= 2` closed forms + `2..300` lattice + the 15
displayed divisor classes, real F1→P2 `mult = 3` handoff), C3-V the
`M_U`/free-characteristic/padding variant coverage (both raw records
per terminal + parametric family bounds), C4 T1/Wronskian layer at two
generic A-points (7 rows on the trunk, incl. T), C5 LEAD-PILOT
token-for-token regeneration against the literal §3.5 block extracted
from `xmodel/sol-gluing-design.md` at run time (direct only — the trunk
has no design pilot block to gate against), C5b the exact rational
anchor on all 74 regenerated rows, C6 twelve negative perturbations —
T1 sign flip, omitted nu in a derivative, `B_g = (3/2)A`, non-H5a
`kappa_H2` composition, mixed-reading case-III `n`, one-slot scale
shift, tampered obstruction record, case list without Case C, `M_U=4`
variant with a `gcd = 2` cell, `M_U=4` record without a realized
variant, tampered trunk terminal `w`, tampered trunk (2.1) `l` — each
must raise at least one failure, and does. No msolve, no network, no
floats; `ops/FLEET.md` respected. The certificate JSONs are the
machine-readable statements of record; this file is their derivation.

Files: `cases/towers/t9_15_direct.json`, `cases/towers/t9_15_trunk.json`
(certificates), `cases/tower_check.py` (checker), this document,
`xmodel/grok-tower-review.md` + `xmodel/sol-tower-review.md` (reviews;
Grok = review of record for the direct kill, Sol = pre-repair snapshot
whose live findings 2/3 are addressed in §8/§7a). No git commit was
made.
