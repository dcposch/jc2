# Small certificate gate: nonemptiness acceptance and rank-filter vacuity

2026-09-06. Reviewer: Fable (this lane). Producer: Astra (both charged reports).
Lifecycle: REVIEWED, verdicts per claim below. **No candidate, no properness
claim, no JC2 conclusion, no exit-price claim.** Both producer reports stay
frozen and unmodified; their seals were re-verified at HEAD
`0d39df3c9fd69c939a8420c54d03228b9077777d`.

Verdicts:

- **Claim 1 (nonemptiness certificate contract): CONFIRMED** as a sufficient
  acceptance contract. The identification of the acyclic circuit's 4,470
  slots with the complete client ideal is book-relative (frozen compressor
  gate), and no verifier implementation exists yet; both are separated below.
- **Claim 2 (rank-vacuity lemma): CONFIRMED** as an elementary theorem with
  the stated scope. Atwell/Zenodo provenance, the "64 rows" count and the
  physical top forms are book-relative metadata, not audited here.

## 0. Manifest, seals, replays

Manifest `/tmp/jc2-lane.RyzDSk/charged-inputs.list` (5 entries) verified by
sha256 against both the lane copies and the repo paths; all five match:

| Input | SHA-256 |
|---|---|
| `xmodel/nonemptiness-certificate-astra-20260906.md` | `14694cb07c25403e4bb8400d34c8e52b224d6778a1d25488c9ea426f486c735c` |
| `box/nonemptiness-certificate-20260906/preflight_controls.py` | `1c183967e67100d5309b0b8aba3d996368c91cfc03ec1e50db013bc270ee3893` |
| `xmodel/relative-rank-vacuity-astra-20260906.md` | `c5b48d06e8d7fb7fc57910b7074dddb72943a8f32c9180a4c3584e75ceb64011` |
| `box/relative-rank-vacuity-20260906/check.py` | `f84ce2910e2a5e43cab4b85fcccdd90d65cfb0fc58dc959a781dfad21e99702e` |
| `FALLACY-v2.md` | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` |

Seals: `seal.py verify --expected-basis 0d39df3c...` PASS for both frozen
reports (body 13083 B / sha `6a3818f0...`; body 5245 B / sha `b2a3c3f9...`).

Referenced immutable sources, recomputed: compressor gate report
`3f768563da1a...` (15,910 B); compactness theorem report `81ab0e5cce46...`;
all five `PINS` of the preflight script match; `box/t2t3-compressor-gate-20260906/graph-replay.json`
contains `graph_ledger_sha256 = f04474ab8227...`, `case = 99-delta2`,
`graph_generator_count = 7136`, `constraint_row_count = 4470`,
`presentation_generator_count = 7585 = 449 + 7136`,
`graph_dependencies_all_preceding = True`,
`graph_rows_all_monic_rational_leader_plus_one = True`,
`all_graph_roundtrips_exact_zero = True`.

Replays (repo paths, `timeout 120`, host python 3.12.3, sympy 1.12):

| Script | normal / -O / -OO | stdout sha256 (identical in all modes) | wall |
|---|---|---|---|
| `preflight_controls.py` | rc 0 / 0 / 0, stderr empty | `dc7f189ed3db2b6189727820aff71dfe3ae72cd374deb901a09a1a62a20c903d` | <= 0.2 s |
| `preflight_controls.py --mutate-local-containment` | rc 1 / 1 / 1, `ValueError: Local containment`, empty stdout | n/a | <= 0.2 s |
| `check.py` | rc 0 / 0 / 0, stderr empty | `1580bb79848220cc69ec5cf95720bf7cb2a25a1cbf33b087db697d56bcacaf39` | <= 2.2 s |
| reviewer control (section 2.5) | rc 0 / 0 / 0 | `1ea93594d263b6c7fd2eb86f5dd2d85de38c432db670e395c36451d813c47ffc` | <= 2.1 s |

AST walk: zero `Assert` nodes in `check.py`, `preflight_controls.py` and the
reviewer control, so `-O`/`-OO` strip nothing. (`build_direct.py`, not gated
here and never executed here, has 26 bare `assert` lines; irrelevant to these
controls.) The preflight must run from its repo path because it resolves
`ROOT` as `parents[2]`; the lane copy is byte-identical.

## 1. Claim 1: the nonemptiness certificate contract

Let `I = (f_1..f_M) <= Q[s_1..s_N]` be the complete chart ideal.

**1a. Witness algebra, reducible or non-squarefree H. CONFIRMED.** Let
`H in Q[T]` be monic of degree `d >= 1` and `A = Q[T]/(H)`. Then `A` is a
Q-vector space with basis `1, T, ..., T^(d-1)`, so `A != 0`. If every
generator `f_i(r_1(T), ..., r_N(T))` reduces to 0 mod H, the substitution
`s_i -> r_i(T)` is a unital ring map `Q[s]/I -> A`; since `1 -> 1 != 0`,
`1 notin I`, so I is proper. Only `A != 0` is used, so H may be reducible or
non-squarefree. A field point follows without the Nullstellensatz: any
maximal ideal `m` of A has `A/m = Q[T]/(H_j)` for an irreducible factor
`H_j`, a number field, hence a Qbar-point of I. Map declaration for the
record: source ring `Q[s]` in the chart's semantic generator order,
coefficient field Q, target `A`, image check = every full row (including the
three inverse rows) evaluates to 0 in A.

**1b. Acyclic definition circuit. CONFIRMED (mathematics); circuit-equals-
complete-ideal BOOK-RELATIVE.** Ring homomorphisms commute with polynomial
substitution. If each of the 7,136 graph rows defines a fresh auxiliary
generator as a polynomial in earlier generators with a unit (monic rational)
leader, the quotient by the graph rows is isomorphic to `Q[s]` on the 449
semantic generators, and each constraint slot `c_k(s,u)` equals a generator
`f_k(s) = c_k(s,u(s))` of I. Evaluating the definitions successively in A,
then every slot, computes exactly `ev(f_k)`; all-zero output is therefore
precisely the hypothesis of 1a. Requirements: exact arithmetic in A (reduce
mod H after each step), no numerical approximation; any division must go
through an inverse variable whose row `Z*x - 1` is itself checked (it is one
of the three `inverse` rows). Keeping the 1,716 identically-zero slots is
harmless (they evaluate to 0 in any A). That the 4,470 slots ARE the complete
client ideal is the frozen compressor gate's claim (DONE, BODY_SEALED), whose
graph-replay metadata is consistent with the structure used above; it is not
re-audited here. `graph-replay.json` covers `99-delta2` only, matching the
report's stated implementation client.

**1c. Hensel smooth-subsystem plus local containment. CONFIRMED as a
sufficient criterion.** Fix the `N-r` free coordinates in `O_K` (K the
unramified extension of `Q_p` with residue field kappa; `O_K` is a complete
DVR). The square system `g_1..g_r` in the remaining r coordinates has a
residue root with unit Jacobian minor, so multivariate Hensel gives a unique
root `a in O_K^N`. For each row, `h_i f_i = sum_j A_ij g_j` is an identity in
`Q[s]`, so it holds after evaluation at `a` in K whatever denominators the
`A_ij` carry; `h_i` p-integral with `h_i(a_bar) != 0` makes `h_i(a)` a unit,
hence `f_i(a) = 0`. So `Q[s]/I -> K` is unital, I is proper; `I*Qbar[s]` is
proper by faithful flatness of `Qbar[s]` over `Q[s]`, and the weak
Nullstellensatz gives a Qbar-point. The `g_j` need not lie in I, so rational
slice equations are admissible, and every displayed containment identity is
owed for every full row. The "flatness is not supplied by special-fibre
smoothness" remark is exactly what control 1f exhibits. Stacks tag numbers
(01V4, 04GE) were not checked offline; they are not load-bearing.

**1d. Fixed-support condition. CONFIRMED as scoped.** The Hensel point lives
in `K^N` for the fixed N of the chart; whether that vector is a polynomial
pair of the intended degrees is delegated by the report to the client
reconstruction (book-relative). The growing-support identity
`(1-px) S_n - 1 = -p^n x^n` is verified by hand (telescoping) and by replay
at depths 1,2,4,8,16; its p-adic limit `1/(1-px)` is not polynomial, so
finite-precision survival with growing support proves nothing.

**1e. Rational denominators. CONFIRMED.** Scalar rational denominators are
units in the Q-algebra A. A non-scalar denominator `q(T)` is a unit in A iff
an explicit Bezout identity `u q + v H = 1` exists, or the coordinate is
replaced by its residue. In the Hensel contract, `A_ij` may carry p in
denominators while `h_i` must be p-integral with unit value; the positive
example uses `h = x+1`, `h(1) = 2`, a unit mod 5.

**1f. `(x, x+p^L)` negative control. CONFIRMED.** Both rows primitive; the
special fibre is the reduced point `x = 0` with Jacobian rank 1 (maximal);
`x = 0` solves both rows mod `p^n` for all `n <= L`; the difference is `p^L`,
so `I_L Q[x] = (1)` and no lift exists at precision `L+1`. Reviewer
consistency check: the contract itself rejects this input, because
`h*(x+p^L) = A*x` evaluated at `x = 0` forces `h(0) p^L = 0`, so
`h(a_bar) = 0`; identically for `(x, p)`: `h*p = A*x` forces `h(0) = 0`.
Both negative controls are thus refused by the unit-multiplier clause, not
merely observed. The `--mutate-local-containment` switch replaces `h = x+1`
by `h = x`, which breaks the identity `h*f_4 = g_1` itself, so it exercises
the conjunction (identity and unit value), not the unit clause alone; the
unit clause alone is documented by the `(x,p)` lines. The script contains no
general certificate verifier; its controls are exact transcriptions of the
report's hand identities. An acceptance implementation, when one exists,
needs its own gate, as the report says.

**1g. Counting specializations fail; they are not lift seeds. CONFIRMED.**
From the pinned `support-counts.jsonl` I recomputed the inverse residuals
`(Z*x - 1) mod 1000000007`:

| Case | separation | T2 leader | T3 leader |
|---|---:|---:|---:|
| 99-delta2 | 600678998 | 401774531 | 258548891 |
| 99-delta52 | 924753348 | 354255143 | 56672515 |
| 108-free-mean | 962644304 | 925354621 | 436036465 |

The delta=2 triple matches the report. All nine are nonzero, so each
assignment violates all three `inverse` rows, which are generators (row block
`inverse = 3` in the builder). The stronger metadata statement
`checked_nonzero_values = nonzero_generator_total` (2754/2754/3196) with
`zero_witness_values = 0` says the assignments satisfy no row at all; that
field is book-relative, the three residuals are recomputed here. A Hensel
seed must satisfy every row mod p; these satisfy none.

**1h. `target_e` rowlessness at exactly the checked scope. CONFIRMED at the
literal scope, which is:** (i) the JSON expression fields `build_direct.py`
consumes: for the 99 charts `maps.h3/C2/C3/B2/A3` term strings and
`residual_rows` (asserted empty, builder line 145); for 108 `h_expr`,
`D_expr`, `C_expr`, `residual_strings`; these use real coordinate names (437
identifiers in the delta=2 scan, no `v<digits>` aliases); and (ii) the
builder's explicit variable references inside synthesized rows:
`target_a..d` (line 530), `lam2` (593), `t3eq`, `t3_fq`, `t3_fgq`, `t3_fq2`
(614-632), `lambda3` (641), and the three inverse rows `zlam2*lam2`,
`Z3*lambda3`, `zsep*sep` (645-647). This set equals the preflight's
hard-coded `direct` set exactly. `target_e` appears in `build_direct.py` only
in the site/weight table (line 351), which feeds the monomial order, not a
row. In the three source JSONs `target_e` occurs only inside name lists
(`full_free_coordinates` / `names`, and `source_gauge.retained_free_coordinates`).
Hence `target_e` occurs in no emitted constraint row of any of the three
charts. Consequences: zero Jacobian column, rank `<= N-1`, minimum
left-cokernel `rows - (N-1)` = 2306 / 2308 / 2690 (arithmetic checked); and
`I = I_0 * Q[s]` with `I_0` in the ring without `target_e`, so `target_e = 0`
preserves properness in both directions. Not proved, and not claimed:
independence of any occurring column. Semantic counts check: delta=2
`444 + Zrho + t3eq + t3_fq + lambda3 + Z3 = 449`; 108 `names` already
contains `Zc`, so `502 + 3 + 2 = 507`.

**1i. Framing.** "A finite-field point plus a Jacobian minor is not a
characteristic-zero certificate for overdetermined systems": CONFIRMED by 1f.
"Excess-row relations can be as hard as ideal membership": a heuristic, not a
theorem; do not cite it as proved. The decision paragraph is a recommendation
and is not gated as mathematics. The report makes no candidate, properness or
existence claim, consistent with the lane brief.

## 2. Claim 2: the rank-vacuity lemma

Setting: char 0, `det J(F,G) = j in k*`, `n = deg F > deg G = m >= 1`,
`F_n` with no nonzero constant null direction.

**2a. Statement and proof. CONFIRMED.** Polarization for symbolic 2x2
matrices: `det(M-A) = det M + det A - (dr - cs - bt + aw)`, checked by hand
(expand `(r-a)(w-d) - (s-b)(t-c)`) and symbolically. With `M = J(x,y)`,
`A = J(a) = [[A,B],[C,D]]` and `det J = j`:
`det(J - J(a)) = 2j - D F_x + C F_y + B G_x - A G_y`. Degrees:
`B G_x - A G_y` has degree `<= m-1 < n-1`; `2j` has degree `0 < n-1` since
`n > m >= 1` gives `n >= 2`; the degree-`(n-1)` part is
`-D d_x F_n + C d_y F_n`; `(-D, C) != 0` because `det J(a) = j != 0`; the
hypothesis makes it nonzero. So the determinant has exact degree `n-1`, is
nonzero, the generic rank is 2 at every geometric `a`, and `rho_rel = 2`.
The hypothesis is base-change invariant: null directions form the kernel of
a k-linear map `k^2 -> k[x,y]_(n-1)`, whose dimension is unchanged over
kbar, so imposing it over kbar is equivalent.

**2b. Two-line criterion. CONFIRMED.** For `F_n = c y^p (y-x)^q`, `p,q > 0`:
`v_x d_x + v_y d_y` applied gives
`c y^(p-1) (y-x)^(q-1) [p v_y (y-x) + q (v_y - v_x) y]` (hand check:
`d_x = -q y^p (y-x)^(q-1)`, `d_y = p y^(p-1)(y-x)^q + q y^p (y-x)^(q-1)`).
Bracket coefficients: `x: -p v_y`, `y: (p+q) v_y - q v_x`; matrix
`[[0,-p],[-q,p+q]]` has determinant `-pq != 0` in char 0, so only `v = 0`.
The general statement (a binary form has a constant null direction iff it is
a scalar times a power of one linear form) is right: straighten `v` to
`d_x'`, then `d_x' F_n = 0` forces `F_n in k[y']` in char 0. Any top form with
two distinct linear factors therefore satisfies the hypothesis.

**2c. Negative automorphism controls. CONFIRMED.** `(y+x^2, x)`: `j = -1`,
`J - J(a) = [[2(x-a_x),0],[0,0]]`, rank 1 at every `a`; its top `x^2` is a
power of one linear form, so the hypothesis fails, which isolates it as
load-bearing. Affine automorphisms have `J - J(a) = 0`, rank 0. Both are
Keller pairs with `n = 2 > m = 1`, so they refute "every Keller pair has
`rho_rel = 2`" without touching the lemma. The affine line in `check.py`
only checks that the zero matrix has rank 0; cosmetic, harmless.

**2d. Scope statement. CONFIRMED as literal.** Any genuine Keller pair in the
campaign's normalized two-line unequal-degree locus has, after the linear
normalization, `F_n = c y^p (y-x)^q` with `p,q > 0` and `n > m`, so the lemma
applies and `rho_rel = 2` holds automatically. A necessary condition met
automatically by every realizing pair excludes nothing; this is row-by-row
and independent of how many rows there are. Two supporting remarks: `rho_rel`
is invariant under affine changes on source and target (`J` becomes
`L * J(phi(x)) * Dphi`), so normalization does not affect it; and for a
Keller pair with `n > m`, `J(F_n, G_m) = 0` forces `F_n^m` proportional to
`G_m^n`, so both tops carry the same two lines and the hypothesis holds
whichever component the normalization names. Not extended, correctly:
`n = m` (the G terms reach degree `n-1` and can cancel), non-Keller chart
points (`det J(x,y)` is then a polynomial that can have degree `>= n-1`),
positive characteristic (`p v_y = 0` no longer forces `v_y = 0`). Book-
relative, not audited: the Zenodo record and Atwell's theorem (discovery
provenance only), the "64 finite-window rows" count, and the physical tops
`y^27 (y-x)^72`, `y^24 (y-x)^84`. None of these is a premise of the lemma.

**2e. Reviewer control.** `box/small-certificate-gate-20260906/reviewer_topdegree_control.py`
(sha256 `328d52d73fc6fcdbff3f120d5cbcd5a4604fa593727db73d8ed99f68ba7a4454`,
explicit exceptions, no assert nodes) checks the symbolic polarization and,
for random `F` with two-line tops `(p,q) = (1,1),(2,3),(4,2),(3,5)` plus
random lower-degree `G` at random rational basepoints, that the
degree-`(n-1)` part of `-D F_x + C F_y + B G_x - A G_y` equals
`-D d_x F_n + C d_y F_n`, that this mixed term has exact degree `n-1`, and
that the directional-derivative coefficient matrix has exact rank 2 over Q.
These are not Keller pairs (none with a two-line top is available; one would
be a counterexample), so the control audits only the degree bookkeeping the
proof uses. Output saved as `reviewer_topdegree_control.stdout.json`.

## 3. FALLACY-v2 checklist

No exit-price assertion is made, so no `charge_basis` line (validator:
ABSENT). Variable/ring maps are declared in 1a and 1b. The rank bounds of
1h are floors on the cokernel and ceilings on rank, never attainment. No
`sat()`, raw-remainder, pole or exit-set reasoning is used. Book-relative
items are labelled, not promoted; no typed OPEN is needed because no gap was
filled by cap or analogy.

## 4. Notes written

`box/small-certificate-gate-20260906/`: `replay-receipts.txt`,
`reviewer_topdegree_control.py`, `reviewer_topdegree_control.stdout.json`.
No live report, shared ledger, `jc2-lean` or tool file was touched; no AWS
or heavy CAS was used.

<!-- BODY-END -->
