# Blind whole-portfolio ideation — Opus5 — `20260827T1349Z`

Author lane: Opus5 (equal-standing core researcher).
Date: 2026-08-27.
Packet: `xmodel/ideation-20260827T1349Z-packet.md`,
SHA-256 `8af21da712a3de8184ca708d75e7461e831f597aac459317d8871176e73b48c3`
— **verified byte-identical by local `shasum -a 256`.**

## 0. Custody, blindness disclosure, and what I actually executed

### 0.1 Canonical basis verified

All seven frozen hashes in the packet reproduce exactly from the worktree:

```text
1112706cd6182d23e360a6e76e5555fcd54264c6470155157f3f7ce42366482b  APPROACHES.md
fca661f1c1c041b2a8648d2b6e5bf5f4834d3e44004bada23e5182ca79b08fbc  AUDIT.md
7ba7ef761d9ee3022eb861daab798d1980efa4fcc881d1675b6ddc0d1c4db40e  PROGRESS.md
039bcdabd9959066b74141262acf109bd9ece326580e56c81f24493c8336c76a  COORDINATION.md
d2ace1aeb635711daa6f4eaca77644ee65bf5861157509f8c1dff83e93db8105  notes.md
df8c920f019f1d99053af6d81f4eee52ad88c23d2c8e7bc513782ea06efe0eba  xmodel/ideation-20260827T1104Z-synthesis-sol.md
a8a1ae4f888a73a7db7ea9d639088c8cdb3c480600e67104955bdd4b535ac5c8  xmodel/websweep-20260827T1348Z.md
```

### 0.2 BLINDNESS DISCLOSURE — one contaminating line, reported in full

**I saw exactly one line fragment of one peer report in this round.** A
repository novelty search (`rg` for
`superelliptic|Risch|elementary antiderivative|Hermite reduction|...`) returned,
among its hits, this single line:

```text
xmodel/ideation-20260827T1349Z-grok.md:209:`8_28`. The integrating factor of `M` is `H^{-1/2}`; making `H` a
```

Nothing else from that or any other `ideation-20260827T1349Z-*` file was read.
I opened no peer report. On seeing the hit I immediately re-ran all subsequent
searches with those files excluded and recorded the incident before continuing.

**Consequences the coordinator must apply, not me:**

- My §3 mechanism was derived and exactly verified *before* that search — the
  execution record shows the identity `H*g' + g*H'/2 = (H/4)*M(Y)` and the
  de Rham class `[w dX] = -(4/5)[dX/w]` computed earlier in the session — but
  the fragment shows at least one peer independently reached the integrating
  factor `H^{-1/2}`. **I therefore claim no sole novelty for the integrating
  factor / `H^{3/2}`-primitive observation.** Treat it as convergent.
- What I still submit as mine to adjudicate is the part beyond that fragment:
  the closed-form criterion in §3.2 (`A in im(N_B)`), its degree-uniformity,
  the exact a-priori bound that makes the negative side certifiable, and the
  cross-avenue identification with the max-12 Chebyshev/Pell receiver and with
  rows 33/45. The coordinator should dedupe those against the peer text, which
  I cannot see.
- My submission is **BLINDNESS-DEGRADED-BY-ONE-RG-LINE**, not clean-blind. It
  should be discounted exactly as the `1104Z` K00 lane was, and no more.

### 0.3 What I executed locally (desk scale only)

No AWS, no Singular, no CAS, no heavy algebra, no canonical-ledger edit, no
`jc2-lean` access of any kind. Everything below is exact `Fraction` arithmetic
in pure Python, total runtime under 30 seconds:

1. Verified `(x-y)*Phi + y^6 = x^6` for the C5 converter and `4 + 6*104 = 628`.
2. Verified the R1 operator identity `H*g' + g*H'/2 = (H/4)*M(Y)` for `g = H*Y`
   on four independent `Y`, i.e. `M(Y) = 4*H^(-1/2) * d/dX (H^(3/2) Y)`.
3. Computed the de Rham reduction on `w^2 = X^8-1`: `X^7*omega` is exact,
   `X^8*omega = (1/5)*omega`, hence `[w dX] = -(4/5)[dX/w] != 0`.
4. Built a reference decision procedure for `2*H*g' + g*H' = 2*H` over `Q(X)`
   (denominator sweep `g = G/Dn`, `Dn` in `{1,H,H^2}`, degrees to 30) and ran
   it on 18 hand-chosen and 28 random `H`.
5. Derived and verified the sharp a-priori bound (`deg g = 1` exactly,
   denominator exactly `A0 = prod_{e_i even} p_i^(e_i/2)`) — agreed with the
   unbounded reference on 10/10 structured cases.
6. Derived and verified the closed-form criterion `A in im(N_B)`,
   `N_B(v) = B*v' + (3/2)*B'*v` — **agreed with the reference search on 33/33
   cases**, including the case that refuted my own first guess.
7. Confirmed `lib/families.py` runs at desk scale:
   `enumerate_families(35)` = 24 rows in 0.01 s, `case_rows(150)` = 34 cases
   in 0.02 s, `section4_families()` = `{7_21, 8_28, 9_24, 9_27}` in 0.01 s.
8. Timed the criterion itself: `H = X^D - 1` for `D` up to 80 decides in
   1.63 s. It is degree-uniform in cost as well as in conclusion.

Post-cutoff worktree observation (not packet evidence): the file
`xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-hostile-review-grok-20260827.md`
now carries eighteen `CONFIRMED` verdicts and no `REFUTED`/`GAP`. The packet
records R3's review as live; I treat R3 at **packet scope only** and flag the
discrepancy for the coordinator rather than promoting it.

---

## 1. Disposition vector over every numbered avenue in `APPROACHES.md`

Five changes. I deliberately did **not** churn the other forty-one: a
disposition vector whose value is legible needs its changes to be load-bearing.
Where a prior Opus5 raise (rows 7, 18, 31, 36, 41) was recorded and either
retained-as-reframe or not funded, I mark `unchanged` rather than re-raising
without new evidence.

| # | avenue | disposition | reason (only for changes) |
|---|---|---|---|
| 1 | GGV Newton-polygon corner families + degree farm | **raise** | §3 converts the `8_28` Keller-face endpoint from a per-family Gröbner/msolve grind into a **closed-form linear criterion on the leading edge alone**, decided in `O(deg H)` exact arithmetic and **uniform in degree** (verified to `deg H = 80` in 1.6 s). Row 1's two recorded stuck-points are exactly "no degree/td ceiling" and "char-0 certificate memory wall". This is the first instrument in the portfolio that attacks the *first* one and dissolves the *second* for this class of face. It is scoped to square/cube edges, so it is not the family farm — but the farm's cost model changes. |
| 2 | Sheet ladder / Eggers–Wall / Sigray | unchanged | `G2-PSC` is untouched by everything in this packet. `TRANSPORT.md` normalization is not transport. |
| 3 | Vertex-gap / strip ODEs / residue functional `R_{k,d2}` | **raise** | The R3 endpoint *is* a strip-type rigid first-order ODE with a residue obstruction: `2*H*g' + g*H' = 2*H`. Row 3's recorded scope limit is "strips, `d1=1`, depth two, `k>=2` only", and its recorded stuck point is that y-axis columns block the `(8,28)` subcase. §3 supplies a residue/exactness functional for exactly the `8_28` face with **no** strip, depth, or `d1` restriction. That is the row's own mechanism escaping its own scope box. |
| 4 | Formal-germ certification + algebraization | unchanged | R3's `K(X)[[t]]` mode classification is a formal-germ technique that worked, but it changes no D-series/DEPTH-STAB status. |
| 5 | Jung–van der Kulk degree descent / amalgam | unchanged | |
| 6 | Abhyankar–Moh one-place / coordinate recognition | unchanged | |
| 7 | Nonproperness / Jelonek `A(F)` | unchanged | My prior-round raise was primary-source checked by Sol: the componentwise-density *reframe* was retained, the search raise was not adopted, and my stronger component-purity bridge was correctly withdrawn. No new evidence this round. |
| 8 | Formal-inverse combinatorics (BCW tree) | unchanged | |
| 9 | Lee–Li Conjecture E | unchanged | |
| 10 | HC4 ⇒ JC2 Hessian bridge | unchanged | `NO LEVERAGE` stands. |
| 11 | Mathieu / GMC / Poisson / Zhao ladder | unchanged | refuted. |
| 12 | Face isolation / p-adic multinomials | unchanged | |
| 13 | Dixmier DC(2) | unchanged | |
| 14 | `End(A_1)` disproof / Zheglov audit | unchanged | |
| 15 | Spectral surfaces / commuting PDOs | unchanged | |
| 16 | D-module / holonomic index | unchanged | |
| 17 | BCW / Druzkowski / Yagzhev stabilization | unchanged | |
| 18 | Graded / equivariant / GIT symmetry | unchanged | My prior lemma-only reopen (Shaska's graded theorem as a `t -> 0` degeneration lemma) stands unconsumed; nothing new. |
| 19 | Char-p counterexamples + Witt lifting (AS109) | unchanged | My prior-round **lower** stands and is corroborated: the low-Witt Cartier gate is a genuine theorem that cuts one content stratum and explicitly does not empty `n=6`. `deg_y` floor `2 -> 6 -> 12` is still a floor-raising mill with no termination theorem in either direction. Keep funded, capped, and labelled as buying negative information. |
| 20 | Reduction mod p / p-curvature | unchanged | |
| 21 | p-adic injectivity / Hensel / model theory | unchanged | |
| 22 | Diophantine integral points / heights | unchanged | |
| 23 | Analytic global inverse / holomorphic analog | unchanged | |
| 24 | Real JC / Pinchuk | unchanged | |
| 25 | Fiber monodromy / dessins / passports | unchanged | |
| 26 | Primitive-monodromy `td` bound | unchanged | |
| 27 | Links at infinity / splice diagrams | unchanged | |
| 28 | Log surfaces / BMY / log-Kodaira | unchanged | §3 lives on the boundary curve, but produces no log-Chern or adjunction input. Resist the temptation to score it here. |
| 29 | LND / Hamiltonian-derivation completeness | unchanged | |
| 30 | Affine-surface classification / ML invariant | unchanged | |
| 31 | Integrality / ZMT / Rees valuations | unchanged | My prior cost-collapse raise stands unconsumed; no new evidence, and restating it would be noise. |
| 32 | Off-diagonal collision ideal / injectivity | unchanged | |
| 33 | Global symplectic exactness / action residues | **reopen, narrow scope only** | The row is filed `COSTUME` for one exact reason: `P dQ - x dy = dS` polynomially, i.e. `H^1_dR(A^2) = 0`, so ambient divisorial residues are automatic. §3 shows the *same* exactness question moved to the **boundary curve of the face** is not automatic: `H^1_dR` of `w^2 = H` has dimension `2g+1 > 0` and `[w dX]` is a nonzero multiple of the holomorphic class `[dX/w]`. Reopen at exactly the scope "exactness/residues of the face differential on the boundary curve", **not** as a revival of ambient action residues, and **not** as a claim about `f dg - x dy`. |
| 34 | 2D tangent-sweep / pole removal | unchanged | |
| 35 | Descent of dim ≥ 3 counterexamples | unchanged | |
| 36 | Guided counterexample search / sparse supports | unchanged | Its prior reframe was retained; the raise was not adopted. But note §4.2: the criterion is two-sided and names the surviving edge class exactly. If that class is ever enumerated, *this* row is where the search belongs. |
| 37 | Finite-field census | unchanged | |
| 38 | Tropical geometry | unchanged | |
| 39 | Cohomological cluster (K2, motivic, `A^1`-degree, Hodge) | **reopen, narrow scope only** | Grok's recorded position is "refuse to start until a 10-line class is written". A 10-line class now exists: `[dX/w] != 0` in `H^1_dR(w^2 = H)`, computed exactly above. **Honest firewall:** this obstructs a *face jet*, not "a nonproper étale endomorphism"; it is de Rham of the boundary curve, not a motivic degree of the map, and Sol's recorded fact that local `A^1`-degree is `+1` everywhere is untouched. Reopen only as "boundary-curve de Rham class as a face obstruction", which is a different and much smaller object than the row's original ambition. |
| 40 | Free-associative / noncommutative Jacobian lift | unchanged | |
| 41 | Naive scaling deformation | unchanged | My prior lemma-only reopen stands. |
| 42 | Markus–Yamabe / Hurwitz realization | unchanged | |
| 43 | Ritt decomposition / composite coordinates | unchanged | |
| 44 | Moskowicz "no prime td" | unchanged | Closed as proof input; the repaired membership theorem already carries the AS109 floor. |
| 45 | Differential Galois / Liouvillian inverse | **raise** | Dismissed on the grounds that "the inverse PDE is tautological" and "univariate reduction reproduces Żołądek A.7" — both true, and both about the *wrong object*. The right object is the face endpoint, and "does `sqrt(H) dX` have an algebraic antiderivative" is precisely a Liouville/Risch decision problem, with a complete classical decision procedure. §3 is a hand-built special case of that procedure. Raise at the scope "algebraic-antiderivative decision procedure as a face instrument", not "differential Galois of the inverse". |
| 46 | Lean / AI formal certification | unchanged | Not inspected, by instruction. Boundary respected. |

---

## 2. Reranked bottlenecks

### 2.1 Proof side

| rank | bottleneck | move | why |
|---|---|---|---|
| 1 | **Cofinal degree/type control (absolute `td`/degree ceiling)** | **up from #6 (prior round) / #1-tied** | `REDUCTION.md` executive verdict item 5 is unchanged: *no theorem bounds the topological degree of a counterexample above*. Every other item on this list is fatal to a chart; this one is fatal to the architecture. It moves to #1 not because it got worse but because §3 is **the first candidate instrument that is uniform in degree** and therefore the first time this bottleneck is attackable at all. An unattackable #1 is a wall; an attackable #1 is the work. |
| 2 | Complete source/landing theorem + `G2-PSC` | unchanged (structurally co-#1) | Still the largest hole. `TRANSPORT.md` closed the T2→T4 normalization fork; that is not transport. No lane has an instrument. |
| 3 | Terminal receiver / common mixed K00 reachability | **down from #1 in the current allocation** | Not because it got harder — because it is now *saturated with instruments and starved of decisions*. V20R2/V21R1/V22R1 are all reviewed; V23/V24 are running; the exact-Q properness gate is the single binary that matters. Adding a fourth parallel stratum lane buys nothing until that returns. Fund the gate, not the lane. |
| 4 | Ramified `rho=0` / equality / positive-load / off-family faces | unchanged | V47R1 and V48 are complete compilers that add no endpoint. This is the honest residue of the contact program and nobody is attacking it. |
| 5 | Finite chart completion — ordered `T-a1` total certificate | **down from #4** | On a C5 PASS this closes, and its remaining risk is a composition bug, not mathematics. §6 Card B removes even that risk for ~1 core-hour. It should stop consuming 20% of capacity. |

**The single sentence that reorders this list:** the campaign has three
well-instrumented local lanes and two uninstrumented global lanes, and it has
been allocating 63% to the instrumented ones. §3's only strategic claim is that
one of the global lanes now has a candidate instrument, so the allocation
should follow.

### 2.2 Counterexample side

| rank | bottleneck | move | why |
|---|---|---|---|
| 1 | No termination theorem in either direction for AS109 | unchanged | Floors rise (`2 -> 6 -> 12`), no ceiling, no construction. Third necessary-condition mill in the portfolio. |
| 2 | **No named surviving class to search in** | **new #2** | Every disproof lane in the campaign is a *mill*: it excludes and excludes and never emits "here is exactly what could still exist". §3 is the first mechanism in the portfolio that is genuinely **two-sided**: it returns not only `EXCLUDED` but the explicit linear condition `A in im(N_B)` that a surviving edge must satisfy. That converts row 36 from blind search into constrained search. See §4.2. |
| 3 | Polynomial algebraization of any formal survivor | unchanged | Every formal survivor the campaign has ever produced still owes bounded support, algebraization, collision, and a direct Jacobian replay. |
| 4 | Max-12 / TD6 survivors are target-shear, not source | unchanged | q15 is target-shear; TD6 has no source/landing composition. |

---

## 3. New mechanism, and the new cross-avenue connection

### 3.1 Repository/history check performed first

Searches run (`rg`, markdown/python/json, `jc2-lean` and — after the incident —
`ideation-20260827T1349Z-*` excluded):

- `hyperelliptic|de[ -]?Rham|abelian differential|second-kind differential|Weierstrass point`
  — 30+ files, **every** hit is one of: (a) characteristic-`p` Cartier/de Rham–Witt in the AS109 lane, (b) "polynomial de Rham exactness on `A^2`" (rows 29/33, the automatic statement), (c) the *hyperelliptic deck* `sqrt(Q) -> -sqrt(Q)` as a group action in the max-12 order-two lane. **No hit attaches a hyperelliptic curve, a genus, or a de Rham class to a GGV face or to the `M(Y)` operator.**
- `superelliptic|Risch|elementary antiderivative|Hermite reduction|integrating factor`
  — hits are AS109 sextic ("do not search blindly for an ambient integrating factor"), TD6 orbifold vocabulary, and a Kummer-cube genus test. None is this object. (This is the search that produced the one contaminating line; see §0.2.)
- `4\*H\*Y|4HY|M\(Y\)|H\^\(3/2\)|w\^2 ?= ?X\^8|X\^8-1` — hits confined to the R1/R2/R3 artifacts, their reviews, and the four canonical ledgers.
- `Pell.*8_28|8_28.*Pell|Chebyshev.*GGV|Keller-face.*Pell|carrier.*Pell` — **zero matches.** The two lanes have never been connected.
- `mod t\^6|J \+ \(t\^|Q\[t\]/\(t\^|thicken|t-adic filtration` — the only `thickening` hits are TD6's `c1_c3_thickening.py` (`eps^2`, a different object) and a non-prime-thickening remark in `AUDIT.md`. **Nothing computes the ordered-`a1` membership at `t`-order above one.**
- `git log --all --grep` over 395 commits: no hyperelliptic/de Rham GGV commit.

### 3.2 The mechanism: the GGV Keller-face endpoint is an algebraic-antiderivative obstruction on the boundary curve

R1 and R3 both terminate at the same wall, stated as a degree accident:

```text
M(Y) = 4*H*Y' + 6*H'*Y = 1  has no polynomial solution,
because deg M(Y) = deg Y + 7 with leading coefficient (4*deg Y + 48)*lc(Y).
```

That is not an accident. The operator has an integrating factor (I verified
`H*g' + g*H'/2 = (H/4)*M(Y)` exactly for `g = H*Y`):

```text
M(Y) = 4 * H^(-1/2) * d/dX ( H^(3/2) * Y ).
```

So `M(Y) = 1` says exactly: **`(1/4)*sqrt(H) dX` is an exact differential on the
curve `C: w^2 = H`, with primitive `w^3*Y`.** For `H = X^8-1`, `C` is a genus-3
hyperelliptic curve, and the exact de Rham reduction (verified above) gives

```text
[X^7*omega] = 0,   [X^8*omega] = (1/5)[omega],   omega = dX/w,
=>  [w dX] = [(X^8-1)*omega] = -(4/5)*[omega] != 0.
```

`[dX/w]` is a holomorphic differential on a curve of genus 3; a holomorphic
differential on a positive-genus complete curve is exact for **no** meromorphic
primitive whatever (if `dZ` is holomorphic and nonzero then `Z` is nonconstant,
but then `dZ` has poles of order `>= 2` at the poles of `Z`). So the obstruction
is not a property of the two ansatzes R1 tested, and not of the module R3
allowed — it is a cohomology class.

**Corrected general criterion (this is the actual deliverable, and it is not
the guess I started with).** Drop `H = X^8-1`. Take any nonconstant `H` over a
characteristic-zero field, write `H = A^2*B` with `B` squarefree. Solving the
endpoint is equivalent to `2*H*g' + g*H' = 2*H` for `g` rational. Then:

- `g` has poles only at roots of `H` of *even* multiplicity, of order exactly
  half; and `deg g = 1` **exactly** (the leading coefficient `2*deg g + deg H`
  never vanishes in characteristic zero). So the denominator is exactly
  `A0 = prod_{e_i even} p_i^(e_i/2)` and the whole decision is a linear system
  in `deg A0 + 2` unknowns — an a-priori bound, not a search cap.
- Substituting `u = A*g` gives `(u*sqrt(B))' = A*sqrt(B)`, i.e. `2*B*u' + u*B' = 2*A*B`.
  `u` is a polynomial (no cancellation is possible at a simple root, since it
  would need `s = 1/2`), and `B | u*B'` with `gcd(B,B') = 1` forces `B | u`.
  Writing `u = B*v`:

```text
SOLVABLE  <=>  A in image of  N_B(v) = B*v' + (3/2)*B'*v.
```

`N_B` is injective with `deg N_B(v) = deg v + deg B - 1` and never-vanishing
leading coefficient, so its image contains no nonzero polynomial of degree
below `deg B - 1`. Hence

```text
deg A < deg B - 1   =>   EXCLUDED, uniformly in deg H.
```

**Verification.** I implemented an independent reference decision procedure
(denominator sweep, degrees to 30) and compared it against the closed-form
criterion on **33 cases** — structured and random, `deg H` from 1 to 16,
multiplicities to 5. **33/33 agreement.** The sharp `deg g = 1`/`A0` bound
agreed with the unbounded reference on 10/10. Recovered specialisations:

```text
H = X^8-1   : A=1, deg B-1 = 7 > 0  -> EXCLUDED   (recovers R3 in one line)
H = X^16-1  : A=1, deg B-1 = 15 > 0 -> EXCLUDED   (R3 explicitly disclaims this)
H = X^D-1   : EXCLUDED for every D >= 2; decided in 1.63 s at D = 80
H = h^2     : SOLVABLE (g = (integral h)/h) -- the perfect-square escape
H = c(X-r)^D: SOLVABLE -- the single-root degenerate escape
H = X^2*(X^2-1) : SOLVABLE, deg A = 1, deg B = 2
```

That last line matters and I flag it against myself: my first guess was
"solvable iff `deg B <= 1`", and it is **false**. The `A in im(N_B)` form is the
one that survived testing. A criterion that is not tested against a reference
implementation is a slogan.

**General `(alpha, beta, N)` form.** For the general face operator
`E = alpha*F_X*G - beta*F*G_X - t*(F_X*G_t - F_t*G_X)` and charged weight `N`,
the same derivation gives homogeneous modes at `gamma = (alpha-n)/beta` and
endpoint `(alpha-N)*F_0'*d - beta*F_0*d' = 1`, whose general solution is
`d = F_0^((alpha-N)/beta) * v` with

```text
v' = -1 / ( beta * F_0^((alpha+beta-N)/beta) ).
```

So the endpoint is always "**is this differential exact on the superelliptic
cover `u^beta = F_0^(N-alpha-beta)`**". With `(alpha,beta,N) = (12,8,22)` this
is `v' = -(1/8)*H^(1/2)`, exactly the case above. **The `8_28` cusp obstruction
is one point of a two-parameter family of superelliptic exactness criteria,
one per GGV face and charged weight.**

**What this does not do.** It does not supply the mode/denominator-provenance
step for non-squarefree `H` (extra homogeneous modes appear whenever
`H^((12-n)/4)` becomes rational, so R3's induction must be redone); it does not
touch the original non-Keller `8_28` witness at its own leading data; it does
not prove raw polynomial provenance; it is not `G2-PSC`, not `G2-BD`, not a
counterexample, not JC2.

### 3.3 The new cross-avenue connection: one instrument serves two lanes that have never been connected

The max-12 order-two "all-zero exact-square/all-load receiver" carries a live,
explicitly nonempty survivor (`xmodel/max12-812-order2-p0-cech-lowcontact-pell-total-rees-successor-design-20260826.md` §4):

```text
H = sqrt(Q)*P(Q),   Q = z^4 + p*z^2 + c*z + r,   P(T) = k10*T^2 + k6*T + k2,
A = k10*(T^5 - (5*Delta/16)*T^3 + (5*Delta^2/256)*T),
A^2 - Q*P(Q)^2 = k10^2*Delta^5/262144,
and for Q = z^4-1, P(Q) = 16Q^2+20Q+5:   A^2 - Q*P(Q)^2 = 1.
```

That is a **polynomial Pell equation on the hyperelliptic curve `w^2 = Q`**, and
the campaign correctly treats its Chebyshev solution as a mandatory positive
control that no exclusion may contradict. The GGV face endpoint is a
**de Rham exactness** question on `w^2 = H`. `rg` finds **zero** artifacts
connecting them.

They are two members of one classical family: *when does a `sqrt(polynomial)`
expression admit an algebraic closed form?* — Pell solvability being the
torsion criterion for `[infinity_+ - infinity_-]` in the Jacobian, exactness
being the de Rham criterion. **They are not the same criterion, and conflating
them is the trap I want on the record**: `Q = z^4-1` has a Pell solution
(Chebyshev, verified in the design document) while `H = z^4-1` is de-Rham
**excluded** by my criterion. One lane's survivor and the other lane's
obstruction sit on the *same curve* under *different* tests.

The actionable consequence is small, concrete, and cheap: build **one** exact
`sqrt`-algebraicity instrument with two entry points — `is_exact(A, B)` and
`pell_solvable(Q, degree)` — used by both lanes, with a shared regression
fixture asserting that `z^4-1` returns `EXCLUDED` for the first and
`SOLVABLE` for the second. That single fixture permanently vaccinates both
lanes against the conflation, and it is why this is a connection worth filing
rather than a coincidence worth admiring.

---

## 4. Strongest proof attack and strongest falsification attack

### 4.1 Strongest proof attack

**Attack the cofinal ceiling with the face-endpoint criterion, not with another
chart.**

Concretely: promote §3.2 from "the `8_28` square/cube edge at weight 22" to the
two-parameter statement, then evaluate it across the GGV face table.

1. Redo R3's mode classification and denominator provenance for general
   `H = A^2*B` (the one genuinely open step; extra modes appear exactly when
   `H^((12-n)/4)` is rational, i.e. when the multiplicities acquire a common
   factor). This is a desk-scale differential-field argument, not compute.
2. With that, the theorem reads: *for every square/cube leading edge with
   `deg A < deg B - 1`, no polynomial-`X` formal jet reaches `E = t^22 + O(t^23)`,
   for every degree.* This is degree-uniform — which is the property no other
   campaign exclusion has.
3. Then instantiate over `lib/families.py`. That library already ports GGV5
   Algorithms 1–9 exactly and returns `case_rows(150)` in 0.02 s. For each case,
   extract the leading edge polynomial and evaluate the criterion.

**Why this is the strongest proof attack available.** Every other proof lane in
the portfolio produces statements bounded by a fixed grade, a fixed contact, a
fixed degree, or a fixed chart. `REDUCTION.md` item 5 says plainly that no
theorem bounds `td` above and that a run over `td = 6..14` therefore cannot be
an end-to-end reduction *even if every book were complete*. A criterion that
returns the same answer at `deg H = 8` and `deg H = 80` in the same 1.6 seconds
is a different kind of object. It may still fail — the mode step may not
generalize, or the GGV faces may not be square/cube after normalization — but
it is the only attack on the list whose *success mode* is cofinal.

**Honest ceiling.** Even complete success excludes one edge type across all
degrees. It does not supply `G2-PSC`, does not land an arbitrary Keller pair in
a book, and does not bound `td`. It converts "no ceiling anywhere" into "a
ceiling on one named face family", which is the first brick, not the wall.

### 4.2 Strongest falsification attack

**Invert the criterion and search only where it says survival is possible.**

The criterion is two-sided, and the surviving class is small and explicit:
`A in im(N_B)`, a codimension-`(deg B - 1)` linear condition. Concretely the
escapes are (i) `H` a perfect square, (ii) `H` a power of a linear form,
(iii) the sporadic solutions like `H = X^2*(X^2-1)`, plus (iv) the weight
resonances `N ≡ alpha (mod beta)` where the endpoint is itself a homogeneous
mode and the pole lemma has no bite.

Attack:

1. Enumerate GGV faces whose normalized edge lands in one of those four
   classes. This is exact lattice arithmetic on top of `lib/families.py` — no
   Gröbner basis, no msolve, no memory wall.
2. In that class only, run the existing jet-realization machinery, since the
   cheap obstruction is known to be silent there.
3. **Mandatory positive control:** the max-12 Chebyshev/Pell survivor must be
   reproduced, not killed, by the instrument (see §3.3). If the instrument
   kills it, the instrument is wrong and the whole attack halts.

**Why this over the alternatives.** AS109 `n=6` is a floor-raising mill with no
construction; TD6 survivors are target-shear; ambient/random search is held.
This is the only falsification route that has just acquired a *named finite
target class* rather than a direction. And it is symmetric with §4.1 at zero
extra cost: the same instrument, read the other way.

**Honest ceiling.** A formal survivor in the surviving class is not a Keller
pair. It owes bounded support, algebraization, an explicit collision, and a
direct Jacobian replay — every one of which the campaign has previously
consumed a survivor with.

---

## 5. One software / AWS acceleration and its exact correctness firewall

**Acceleration.** Replace the per-face Gröbner/pole-order analysis with the
closed-form endpoint decision procedure of §3.2: a linear solve in
`deg A0 + 2` unknowns over exact `Q`. Measured cost on this laptop, pure Python
`Fraction`, no CAS: `deg H = 8` in 0.05 s, `deg H = 80` in 1.63 s. Compare with
the campaign's recorded GGV cost model — 761 GB peak and 17 h 43 m for one
`cCa6` char-0 basis. The speedup is not a constant factor; it is a change of
complexity class for this decision.

**The exact correctness firewall.** The failure mode of every fast "no solution
exists" instrument is a search cap silently reported as nonexistence. This one
is immune, and provably so, because both verdicts carry certificates:

- **SOLVABLE:** the instrument must emit `g` explicitly and the caller verifies
  `2*H*g' + g*H' - 2*H == 0` by direct exact substitution. One line, no trust.
- **EXCLUDED:** the instrument must emit (a) the explicit rational dual
  functional `lambda` with `lambda(2*H*v' + v*H') = 0` for all `v` in the
  bounded space and `lambda(2*H) != 0`, **and** (b) the a-priori bound proof —
  `deg g = 1` exactly, because the leading coefficient of `2*H*g' + g*H'` is
  `(2*deg g + deg H)*lc(g)`, which is nonzero in characteristic zero for every
  `deg g >= 0`; and denominator exactly `A0`, because a pole of order `s` at a
  root of multiplicity `e` contributes leading coefficient
  `((12-N)*e + 4*s)`, which forces `s = e/2` and hence `e` even.
  **The bound is derived, not configured.** There is no `dmax` parameter whose
  wrong value could produce a false `EXCLUDED`.
- **Cross-check gate:** the sharp bounded solver must agree with the unbounded
  reference solver on the frozen fixture set. I ran exactly this and got
  10/10 and 33/33; that fixture set is the regression suite.
- **Characteristic gate:** every step divides by integers of the form
  `2*d + deg H`, `4*d + 6*deg H`, `2*k+1`. The instrument must refuse to run
  over any field where one of them can vanish, and must state characteristic
  zero in its verdict string.
- **Scope gate:** the verdict string must name the leading edge, `alpha`,
  `beta`, and `N`, and must carry `mode_completeness_dependency=OPEN` until the
  general-`H` mode step of §4.1 step 1 is separately proved and reviewed.

That last gate is the one I most want enforced: the fast criterion is exact,
but it decides the *endpoint*, and the endpoint is only the whole problem once
the mode classification is generalized. An instrument that forgets its own
dependency is how a correct computation becomes a wrong theorem.

---

## 6. Idea cards

### Card A — Superelliptic exactness criterion for GGV Keller-face endpoints

- **Target obstruction.** Cofinal degree ceiling (bottleneck 2.1 #1); the
  `8_28` face family; the recorded non-claims of R3 ("does not apply to the
  original witness", "does not exclude multiple-root or non-squarefree
  square/cube edges").
- **Object.** For a face with weights `(alpha, beta)` and charged weight `N`,
  the differential `F_0^((N-alpha-beta)/beta) dX` on the superelliptic cover
  `u^beta = F_0^(N-alpha-beta)`; for `(12,8,22)` and `F_0 = H^2`, the class
  `[sqrt(H) dX]` on `w^2 = H`.
- **Dependencies.** R1 (`66121bdd...`, reviewed), R2 (`0f8f3833...`, reviewed),
  R3 (`—` provisional at packet scope) for the mode classification and
  denominator provenance at `H = X^8-1`; `lib/families.py` for instantiation.
  **Named open dependency:** general-`H` mode completeness.
- **Cheapest discriminator.** Two desk-scale steps, in order.
  (i) *Zero compute:* re-derive R3's §3 induction with `H = A^2*B` and record
  the enlarged mode list `{n : H^((12-n)/4) in K(X)}`. If the enlarged list
  contains `n = 22`, that `H` is out of scope and must be listed, not hidden.
  (ii) *Seconds:* run the certified criterion over `case_rows(150)`.
- **PASS means.** For every square/cube edge with `deg A < deg B - 1`, no
  polynomial jet reaches the charged weight — for every degree. First
  degree-uniform exclusion in the portfolio. **PASS does not** mean any GGV
  family is empty, `G2-PSC`, `G2-BD`, a `td` bound, or JC2.
- **FAIL means.** Either the mode list swallows weight 22 for the multiple-root
  edges (then the theorem is confined to `H` squarefree and to
  `A in im(N_B)`-negative edges, still strictly more than R3), or the GGV faces
  do not normalize to square/cube form (then the whole card retracts to the
  `8_28` lane and Card A's cofinal claim is withdrawn). Both are informative.
- **Stop condition.** Stop if step (i) shows weight 22 is a homogeneous mode for
  the generic multiple-root edge, or if the criterion's regression fixture ever
  disagrees with the unbounded reference. Do not escalate to AWS: if this needs
  AWS it has already failed, since its entire value is being degree-uniform and
  cheap.
- **Rollback subtree.** Nothing depends on it yet. It is additive to R1/R2/R3
  and consumes none of them beyond their stated scope. If R3's review reverses,
  Card A loses its mode input and reverts to a conjecture with 33/33
  verification of its *endpoint* half only.
- **Expected information gain.** High and two-sided. Even total failure of the
  cofinal claim leaves a certified `O(deg H)` decision procedure for a question
  that currently costs a Gröbner basis, plus the explicit surviving class for
  §4.2. This is the only card in this submission whose success mode touches the
  #1 bottleneck.

### Card B — The thickened special fibre: compute `a1^N` modulo `t^6`, not modulo `t`

- **Target obstruction.** The `T-a1` total certificate's composition risk, and
  the exponent 628.
- **The mathematics.** Define `N(s) = min{N : a1^N in J_total + (t^s)}`.
  Given the reviewed generic identity `5*t^6*a1^4 in J_total`:

```text
a1^N = j + t^s*c  =>  a1^(k*N) == t^(s*k)*c^k  (mod J),
so with k = ceil(6/s):  a1^(4 + k*N(s)) in J_total.
```

  Hence the achievable exponent is `E(s) = 4 + ceil(6/s)*N(s)`, and
  `E(6) = 4 + N(6)` is **the sharp optimum obtainable from a pole-6 generic
  identity** — not a heuristic improvement. The current route is the `s = 1`
  instance with the certified input `N(1) <= 104`, giving `4 + 6*104 = 628`
  (arithmetic verified). The current certificate additionally proves
  `a1^624 in J + (t^6)`, so `N(6) <= 624`; and `J + (t^6)` is contained in
  `J + (t)`, so `N(6) >= N(1) >= 7` by V38's reviewed `a1^6 notin J0`.
- **Why the cost is negligible.** C4's cascade lives in `Q[X19_rho0]`, i.e.
  `Q[t,X]/(t)`. `Q[t,X]/(t^6)` is local with the same residue field, so **every
  C4 clear or division by an element that is a unit at `t = 0` remains legal
  verbatim** — and each such element must already be a `t = 0` unit or C4 would
  have divided by zero. The job is a coefficient-ring swap on a run that took
  239 s on one core at 153 MiB.
- **Why it is worth more than the exponent.** Mod `t^s` for `s >= 2`, the eight
  rows that vanish at `rho = 0` become live (they are divisible by `t`). So this
  is not a re-run of C4 with better bookkeeping — it is a **strictly larger
  input system**, reaching a total membership **without the C5 converter at
  all**. That is exactly the joint where C1/C2 died (a crossed multiplier at the
  branch combination) and exactly the live risk in C5.
- **Dependencies.** The frozen 70-slot/59-row corpus and its hashes; V43C4's
  cascade design (reviewed, `3e0e80c0...` / `6a8ab201...`); V43G4
  (reviewed, `ae7beed3...` / `8a34756e...`). It does **not** depend on C5.
- **Cheapest discriminator.** Replay the C4 derivation over `Q[t]/(t^2)` first.
  If it closes, report `N(2)` and `E(2) = 4 + 3*N(2)` immediately, then go to
  `t^6`. `s = 2` is the cheapest possible signal and already caps the exponent
  near `3*N(2)`.
- **PASS means.** An independent, structurally different total certificate with
  a sharp exponent `4 + N(6)`, plus the new invariant profile
  `N(1) <= N(2) <= ... <= N(6)`. If C5 also passes, they corroborate each other
  through disjoint failure modes. **PASS does not** mean terminal receiver,
  K00, Gate T, order two, maximum twelve, or JC2 — the firewall is identical to
  C5's.
- **FAIL means.** The cascade does not close mod `t^s`. This **does not refute
  C5**; it means the direct route needs more grades or a different rebase. Report
  the profile obtained and stop. Fail-closed.
- **Stop condition.** Stop at 30× the C4 node count, or two core-hours, or the
  first non-unit division attempt (which must abort, not be "handled").
- **Rollback subtree.** None — nothing is built on it. It is a parallel
  corroboration lane, which is precisely its point.
- **Expected information gain.** Moderate-high, at near-zero cost. The strongest
  argument is not the exponent: it is that the campaign currently has **one**
  path to its headline provisional result, and that path's two ancestors were
  both formally withdrawn for a composition bug. A second path with a disjoint
  failure mode is cheap insurance on the round's trigger event.
- **Secondary, speculative.** A certificate in `Q[t,X]/(t^6)` is a jet-ring
  object, structurally the same kind as the K00 `Q[Lambda]/(Lambda^20)` jet ring,
  whereas `a1^628 in J` transports only as ordinary membership. If a row-origin
  chain map is ever built, the jet form is the one that can carry filtration
  information. **No such map exists today**; this is a reason to prefer the
  form, not a claim about K00.

### Card C — K00: dual-driven hypersurface chain with a mandatory nonemptiness invariant

- **Target obstruction.** Terminal receiver / common mixed reachability, and the
  packet's explicit question: successive strata, Fitting/derived rewrite, or a
  new receiver connection?
- **My answer to that question: none of the three as posed.** Not successive
  rank strata — that is what produced the vacuous V24 normal forms. Not a
  Fitting/derived rewrite as the primary engine — the minors of a 140×169
  parametric matrix are not computable and the packet's own reviewed evidence
  (V21R1's Gröbner-free finite-truncation proof, V22R1's exact rational dual
  pairing `25/45056`) shows the campaign's working instrument is *duals*, not
  minors. Use duals to progress and Fitting only to certify
  representation-independence of the final statement.
- **The redesign.** Maintain the pair `(Z_k, cert_k)`:
  `Z_k = V(f_1, ..., f_k)` in the parameter space, each `f_i = lambda_i^T b`
  with `lambda_i^T M == 0` modulo `(f_1,...,f_{i-1})`; and `cert_k` an
  **exact-`Q` nonemptiness certificate for `Z_k`** — a rational point, or a
  Gröbner basis that is not `(1)` together with its dimension. Loop:
  compute a dual on `Z_k`, form `f_{k+1}`, and **test `Z_{k+1}` for nonemptiness
  before computing anything on it.** Each stratum is cut by one polynomial with
  an explicit certificate, not by a rank condition.
- **The reframing that matters most.** The `F_65521` finding that the
  prior-plus-`F10` localized ideal is the unit ideal is being carried as a
  defect that made V24 vacuous. It is *also* the leading hypothesis that the
  exact-`Q` answer is the same — in which case the entire valuation-one stratum
  is empty and **K00 closes at valuation one**. The running exact-`Q`
  properness/nonemptiness job is therefore not hygiene; it is a **two-sided
  decision**, and it should be reported as `EXCLUDED` / `SURVIVES`, never as
  `REPAIRED`. Note the compatibility: V22R1's promoted statement is that the
  *homogeneous cone* `(Q1..Q6,F10)` is proper of affine dimension three; the
  unit-ideal finding is about the *localized normalized chart*. Those are
  different ideals and there is no contradiction to resolve — only a
  characteristic to settle.
- **Dependencies.** V20R2 (reviewed, `9e304f58...` / `c37cdc4f...`),
  V21R1 (reviewed, `b514ef72...` / `aa1a57cd...`), V22R1 (reviewed,
  `494075c5...` / `f834cb99...`). V23/V24 provisional; the mod-`p` localization
  test.
- **Cheapest discriminator.** The already-launched exact-`Q` chart
  properness/nonemptiness test. **Do not start a fourth stratum lane until it
  returns.** Adding V25 now repeats the exact error that made V24 vacuous.
- **PASS (`EXCLUDED`, unit ideal over `Q`) means.** The valuation-one normalized
  stratum is empty; that whole branch of K00 mixed reachability closes. It does
  **not** decide other valuations, full jets, arcs, closure incidence, order
  two, maximum twelve, or JC2.
- **FAIL (`SURVIVES`) means.** A nonempty stratum with an explicit certificate,
  and V23/V24's compatibility polynomials become non-vacuous and can be
  contracted on it. Also informative.
- **Stop condition.** Stop the whole chain if two consecutive duals produce
  `f_i` that are units on `Z_{i-1}` (the chain has degenerated), or if any
  `Z_k` nonemptiness test is answered only modulo `p`. A mod-`p` nonemptiness
  answer is not admissible as the loop invariant — that is the exact defect
  being repaired.
- **Rollback subtree.** V23/V24 and every descendant of the conditional Cramer
  theorem. The reviewed V20R2/V21R1/V22R1 layer is untouched by any outcome.
- **Expected information gain.** High on either branch, and — unusually — the
  branch currently filed as bad news is the one that produces a theorem.

---

## 7. `continue` / `redesign` / `stop` for every current major lane

| lane | verdict | reasoning |
|---|---|---|
| V43 ordered `T-a1` total certificate (C5 + review) | **continue, at reduced share** | Nearly closed; the remaining risk is composition, not mathematics. Finish the review, add Card B as an independent path, then hand the capacity to the global lane. |
| V43 G5 / G5S circuit and minimal-pole minimizer | **redesign** | Minimizing the pole of the *generic* identity attacks `e` in `4 + e*M`. Card B attacks the same product from the `s` side at a fraction of the cost and with a sharper endpoint (`E(6)` is optimal, not merely smaller). Retask the 32-way shard budget to the `t`-adic profile. |
| K00 common mixed `Lambda<=19` reachability | **redesign** | Card C. Dual-driven chain, mandatory exact-`Q` nonemptiness invariant, unit-ideal treated as a verdict. |
| K00 pure-coefficient D9+ Macaulay | **stop** (already stopped) | Permanently. Reaffirmed. |
| GGV `8_28` Keller-face endpoint (R1/R2/R3 line) | **continue and raise** | This is where Card A lives and where the only degree-uniform mechanism in the portfolio appeared. Highest-marginal-value continuation in the round. |
| GGV/global `G2-PSC` fidelity prototype | **continue, small share** | One chain plus one mutation can identify missing packet fields; it can never prove the functor. Keep it at reconnaissance funding. Do not let Card A be mistaken for it. |
| V47/V47R1/V48 bounded contact/chamber compilers | **stop the compiler lane** | Both are complete, reviewed, and explicitly add no endpoint and no fan cover. Further compiler work is negative-value. Keep the artifacts as the endpoint authority. |
| Equality faces, positive loads, ramified `rho=0` deck/square, off-family | **continue** | This is the honest residue of the contact program and the only part of it still capable of producing an endpoint. It is currently the least-attacked open face set. |
| AS109 residual `n=6` disproof | **continue, capped** | Reviewed low-Witt gate is real and cuts one content stratum. No termination theorem either way. Fund capped; label as negative information. No W2/W3, no new support rectangles. |
| TD6 | **continue, capped** | H19R1 repair (38 original-FIRST multipliers, denominator-cleared identity with total `F`) only. No new atlas, no new `q` clients. |
| D1 / affine-Faber order two | **continue, capped** | The Chebyshev/Pell receiver is the live positive control and now shares an instrument with Card A (§3.3). Build the shared fixture. |
| External intelligence / Matysiak | **continue** | §8.2. Acquisition is human-gated; the audit template is not, and should be written now. |
| `jc2-lean` | **out of campaign custody** | Untouched, unread, unbuilt, unmentioned beyond this line. |

**Allocation.** Current is 28 / 22 / 20 / 15 / 10 / 5. I propose:

```text
30%  global source/landing, G2-PSC/G2-BD separation, and the cofinal ceiling
     (funded by Card A -- this lane finally has a candidate instrument)
24%  terminal receiver and common mixed K00 reachability (Card C loop)
14%  V43: C5 review plus Card B independent path
12%  ramified / equality / positive-load / off-family faces
12%  disciplined disproof (AS109 capped, TD6 capped, and the §4.2 surviving class)
 8%  integration, external intelligence, Matysiak audit template
```

The single change I would defend hardest: **+8 to the global lane, −4 from K00**.
Not because K00 is less important, but because K00's decision is gated on one
running job and cannot absorb more capacity this round, while the global lane has
been at 22% with no instrument for weeks and now has one to try.

---

## 8. The two branch analyses the packet requires

### 8.1 The provisional total certificate: PASS and reversal

**On PASS (Grok hostile review confirms `a1^628 in J_total`):**

- Promote exactly `a1^628 in J_total` for the frozen literal total raw
  ordered-`a1` chart through grade 19, `W = 0`, no localization, no division
  by `t`.
- **The structural consequence worth stating in the headline:** with `T-a0`
  already closed by the reviewed pure cubic `a0^3 in I`, and all four
  `J1 = (rs,cs,c0,c1)` strata closed **for the named unit-load family**, a C5
  PASS closes **both** `J2` charts at that same scope. The
  on-family landing critical path then collapses from "six charts plus a
  receiver" to **"the terminal receiver `V(J1+J2)`, plus coverage, ramified, and
  off-family"**. That is a genuine milestone and it is *also* the moment the
  V43 lane should stop consuming capacity.
- **The one review item I would not sign without:** confirm the mutations
  actually fire against a *non-vacuous* baseline. The known failure mode here is
  a replay that passes because nothing was tested. Nine registered mutations are
  listed; each must be shown to change the output, not merely to be present.
  Second: the corpus census (70 slots, 59 nonzero, 11 zero) is load-bearing in
  the wrong direction for a membership claim — an over-large `J` would make the
  certificate true and meaningless. Every one of the 25 used rows must be
  re-derived from the primitive source emitters, not read from the frozen corpus
  file. Third: a positive control — relax one Keller condition so the system has
  a known point, and confirm the certificate **fails** there.
- **What does not follow, and must be in the promotion text:** no terminal
  receiver, no normalized K00 reachability, no Gate T, no source/landing
  coverage, no order two, no maximum twelve, no JC2, no counterexample.
- **Capacity:** move V43's freed share to the global lane first (per §7), not to
  K00.

**On reversal (review refutes C5):**

- Roll back **only** C5 and its descendants. C4 (`a1^104 in J0`) and G4
  (`5*t^6*a1^4 in J_total`) are separately reviewed and survive; V42 survives.
  This is the same containment that worked for C1/C2.
- **Predicted failure joint,** from the C1/C2 precedent: not the inputs, but the
  composition. Two specific places. (i) `R_j(t) = R_j(0) + t*Delta_j` silently
  requires that C4's `rho=0` rows be *literally* the `t=0` specializations of the
  same 59 named slots — row-name identification across two rings is exactly what
  killed C1/C2, and matching variable names are not a map. (ii) the `1/5`
  normalization and the eleven zero slots, both of which are mutation-tested but
  whose *provenance* is separate from their arithmetic.
- **Rollback subtree:** any statement that both `J2` charts are closed; any
  claim of ordered-chart closure; any downstream that reads `a1^628` as a
  transported object.
- **Immediate successor:** Card B, which is why I recommend launching it *now*
  rather than after the review. It reaches the same target through a route that
  does not contain the suspected joint at all.

### 8.2 Matysiak SSRN 7229458: acquisition and audit branches

**Branch 1 — primary text acquired.**

The abstract structure makes this audit unusually short, and I would pre-commit
its shape before the bytes arrive:

- The predecessor (SSRN 7229358) advertises `5''s` as *a characterization of
  constant-Jacobian endomorphisms* — i.e. `5''s <=> Keller`. The JC2 paper must
  then prove `5''s => automorphism`. **All the content is in that single
  implication**, and it is 19 pages. Read that proof and nothing else first.
- If `5''s <=> Keller` and `5''s => automorphism` both hold, then `5''s` is
  equivalent to being an automorphism. So the audit's first question is not "is
  the proof right" but **"which of the two claimed implications is doing the
  work, and is the other one a definition in disguise?"**
- Named traps, in the order they are most likely to appear: (a) treating the
  image subring `C[P,Q]` as a UFD or integrally closed — it is a polynomial ring
  precisely when the map is an automorphism, so any square-free-factorization
  argument *inside the image* is a candidate circularity; (b) assuming
  injectivity or properness to get the factorization to descend; (c) a dimension
  count that silently assumes the fibres are finite; (d) birationality assumed
  rather than derived.
- Map any surviving lemma into the claim DAG. Rerank nothing before that.

**Branch 2 — primary text not acquired (the current state).**

Three things are worth doing *without* the PDF, in increasing order of value:

1. **Escalate acquisition as a human decision.** SSRN's Cloudflare challenge is
   an interactive-session problem, and both remaining lawful routes — an
   interactive browser session and direct author contact — are outside my
   authority: the second is external communication. Surface it; do not
   improvise around it.
2. **Write the audit template now** (the §8.2 Branch-1 checklist, as a file with
   slots for the exact definition of `5''s` and the exact statement of each
   implication). The audit then costs hours, not a day, whenever bytes arrive.
3. **Run the char-`p` countermodel test, which needs no PDF and is
   campaign-native.** The campaign owns explicit characteristic-`p` Keller
   non-automorphisms — the Artin–Schreier `F_3` collision and the AS109 family.
   Reconstruct the most plausible readings of an "endomorphic square-free
   factorization condition" and evaluate them on `(x - x^p, y)`. If a reading
   holds there while the claimed implication `5''s => automorphism` never uses
   characteristic zero essentially, that is a **decisive structural objection
   obtainable today**, and it also tells the eventual reader exactly which line
   of the paper to check first. If every reading fails there, that is genuine
   evidence the condition is characteristic-sensitive and the claim deserves a
   careful read.

**Prior, stated once and not repeated:** the author's 2024 preprint also
advertised a full proof. That lowers the prior. It is not a refutation, it does
not license dismissal, and it must not appear in place of reading the paper.

**Allocation discipline for both branches.** Matysiak is an intelligence lane at
8% shared with integration. It does not touch the exact-certification critical
path in either branch. The classification stays `ACTIONABLE-UNAUDITED /
BLOCKED-BY-PRIMARY-TEXT-ACCESS` until bytes exist and are read.

---

## 9. Scope firewall for this submission

- Nothing in this report is a promoted claim. §3.2's criterion is exactly
  verified at desk scale against an independent reference implementation on
  33/33 cases; it has had **no different-model hostile review** and its general-`H`
  mode-completeness dependency is **open**.
- The `[dX/w] != 0` computation is a statement about a curve, not about a
  Keller map. It obstructs a face jet at one charged weight.
- Card A does not exclude any GGV family, does not supply `G2-PSC` or `G2-BD`,
  does not bound `td`, and does not touch the original non-Keller `8_28` witness
  at its own leading data.
- Card B changes an exponent and adds an independent path. It closes no new
  object.
- Card C's `EXCLUDED` branch would close one valuation-one stratum, not K00.
- No result here proves or disproves JC2, and none produces a counterexample.
- My blindness is **degraded**: §0.2 records the single peer line I saw. The
  coordinator should dedupe §3 against the peer text I cannot read, and should
  discount this submission's independence accordingly.
