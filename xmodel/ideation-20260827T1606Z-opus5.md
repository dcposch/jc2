# Blind whole-portfolio ideation — Opus5, round `20260827T1606Z`

Author: Opus 5 (Anthropic), equal-standing whole-portfolio researcher
Sealed packet: `xmodel/ideation-20260827T1606Z-packet.md`
Basis verified: `418e413593120d19e15e6546eb50c985f4b1f038`; all seven frozen-basis
hashes and all six pinned producer/adjudication hashes recomputed and matched
before any analysis (transcript in §11).

Status: **INDEPENDENT IDEATION SUBMISSION.** Nothing here is promoted
evidence. Everything labelled *verified* was computed by me this session with
exact rational arithmetic at desk scale; everything else is explicitly marked
conjecture, premise, or design.

---

## 0. Executive summary

My single highest-value finding is that the campaign's entire GGV instrument
stack — the mode schedule (R3/R4/R5), the survivor geometry (R6), the
quarter-root de Rham tower (R7R1), and the literal raw determinant compilers
(D3/D4R1/D5G/D5N/D5G35) — is **indexed by a choice of Newton face**, and the
campaign has spent its whole GGV effort on **one** of the `8_28` corner's
**two** faces. The other face is a second, complete, exactly parallel
instance of the identical differential operator, on the identical 442 raw
slots, which nobody has written down.

Verified this session, exactly:

- The same operator with a different target exponent. With
  `x=tau^-4 xi`, `y=tau`, `ftil=tau^8 f`, `gtil=tau^12 g`,

  ```text
  12 ftil_xi gtil - 8 ftil gtil_xi - tau(ftil_xi gtil_tau - ftil_tau gtil_xi)
      = -tau^17 * J(f,g).
  ```

  This is the **same** left-hand side as the campaign's `E`, whose upper-face
  identity is `E = t^22 * J`. Both identities were checked against random
  Laurent data with exact `Fraction` arithmetic.
- The second grading re-partitions **exactly** the same raw lattice: my
  independently derived `nu`-windows recount D3's census to the digit,
  `141` `f`-slots + `301` `g`-slots = `442`.
- A general face-endpoint theorem that subsumes and explains R5/R7R1's
  exponents: for an extremal face with outward normal `w`, the endpoint
  condition is exactness of `K^{-w(1,1)/m} dxi`, `m = gcd(w(f),w(g))`.
  Upper face: `w(1,1) = -2`, `m = 4`, exponent `+1/2` — the recorded
  `[w dX]` criterion. Lower face: `w(1,1) = +3`, `m = 4`, exponent `-3/4`.
- **The sign flips.** A positive exponent puts all poles at infinity and
  needs a de Rham reduction; a negative exponent puts poles at the roots of
  `K` and turns the endpoint into a residue/holomorphy question on a
  `mu_4`-cover. On the lower face the relevant differential is *holomorphic*
  in the generic case, hence never exact, hence the filter is enormously
  stronger.
- The complete exact classification at the lower face for `deg K <= 8`, and
  the resulting corner-farm arithmetic filter `gamma = 3 (mod 4)` on the GGV
  residual-root multiplicity. `8_28` has `gamma = 7` and **passes** — a
  nonvacuous positive control, not a kill.
- My solver reproduces R5's promoted degree-eight criterion `4a0+D*a2=0` on
  120/120 samples plus the `b=0` and `b=8` controls, which validates the
  instantiation machinery before it is used at `N=17`.

The second consequence is strategic and, I believe, decision-changing: on the
upper face the campaign works with an **artificial squarefree replacement**
`H=X^8-1`, because the genuine `8_28` control's upper face degenerates to the
single monomial `x^16 y^56` (verified: `max(j-3i)=8` is attained only at
`(16,56)` in `B^2`), i.e. `H = X^8`, `delta = 8`, and *every* weight then
carries a rational mode. On the lower face the leading form is **pinned by
the GGV chain data itself** (`B = x(z-1)^7`, so `K = xi(xi-1)^7`,
`delta = 1`), and only weights `nu = 0,4,8,12` carry a polynomial mode below
the target. The rigidity the upper-face program has to manufacture is
already present, for free, on the face nobody analysed.

---

## 1. Disposition over the complete numbered avenue inventory

`APPROACHES.md` §1 master union table, rows 1–46. Reasons are given for every
change; `unchanged` rows carry no obligation.

| # | Avenue | Disposition | Reason (changes only) |
|--:|---|---|---|
| 1 | GGV corner families / degree farm | **raise** | First face-level necessary condition that needs no artificial replacement edge: the `(4,-1)` face endpoint gives `gamma = 3 (mod 4)` for single-residual-root corners (§3.5). Cheap, arithmetic, farm-wide. |
| 2 | Sheet ladder / Eggers–Wall / td6 | unchanged | |
| 3 | Vertex-gap / strip ODEs / residue functional | **raise** | This avenue's essence — "face valuation orders bracket equations; the block collapses to a rigid ODE" — is exactly the mechanism in §3. My result upgrades the per-case rigidity to a single closed exactness criterion valid at every face, with the face normal as the parameter. The avenue was scoped to strips, `d1=1`, depth two; that scope restriction is an artifact of the old derivation, not of the mechanism. |
| 4 | Formal-germ certification / D-series windows | **lower** | Dominated. A face-endpoint exactness test costs seconds and answers the same necessary question that a depth-`k` prolongation answers after hours; and the campaign has now repeatedly re-learned that a nonempty formal window is not an arc. Keep only as custody infrastructure. |
| 5 | Jung–van der Kulk descent | unchanged | |
| 6 | Abhyankar–Moh / one-place | unchanged | |
| 7 | Nonproperness / Jelonek `A(F)` | unchanged | |
| 8 | Formal-inverse combinatorics | unchanged | |
| 9 | Lee–Li conjecture E | unchanged | |
| 10 | HC4 ⇒ JC2 Hessian bridge | unchanged | |
| 11 | Mathieu / GMC ladder | unchanged | dead, stays dead |
| 12 | Face isolation / p-adic multinomials | **raise** | The campaign scored this Low with "no integer `m` to send to infinity". My criterion *is* a face-isolation obstruction and it has an arithmetic character (`mod 4` divisibility of multiplicities, `mu_4` Kummer descent) rather than a limit. Wilson's GMC(2) proof isolates a Newton face; so does §3. Give it a live client. |
| 13 | Dixmier DC(2) | unchanged | |
| 14 | `End(A_1)` / Zheglov audit | unchanged | |
| 15 | Spectral surfaces / commuting PDOs | unchanged | |
| 16 | D-module / holonomic index | unchanged | |
| 17 | BCW / Druzkowski / Yagzhev | unchanged | |
| 18 | Graded / equivariant / GIT | unchanged | closed by Shaska 2026 |
| 19 | Char-p counterexamples + Witt | unchanged | AS109 `n=6` stays narrow |
| 20 | Reduction mod p / p-curvature | unchanged | |
| 21 | p-adic injectivity / Hensel | unchanged | |
| 22 | Diophantine / heights | unchanged | |
| 23 | Analytic global inverse | unchanged | |
| 24 | Real JC / Pinchuk | unchanged | |
| 25 | Fiber monodromy / dessins / passports | unchanged | see §4 for a new but not-yet-decisive connection |
| 26 | Primitive-monodromy bound on td | unchanged | |
| 27 | Links at infinity / splice diagrams | unchanged | |
| 28 | Log surfaces / BMY | unchanged | |
| 29 | LND / Hamiltonian completeness | unchanged | |
| 30 | Affine-surface classification / ML | unchanged | |
| 31 | Integrality / ZMT / Rees valuations | unchanged | |
| 32 | Off-diagonal collision ideal | unchanged | |
| 33 | Global symplectic exactness / action residues | **raise** | The ordinary untwisted gate returned exact-form `COSTUME` precisely because it tested the *global untwisted* primitive. §3 shows the live object is the **face-twisted** residue class `[K^{-w(1,1)/m} dxi]` on a cyclic cover — a genuine action-residue obstruction attached to `J=1`, which is what this avenue always wanted and never had. |
| 34 | 2D tangent-sweep / pole removal | unchanged | |
| 35 | Descent of dim ≥ 3 counterexamples | unchanged | |
| 36 | Guided CE search (SAT/fewnomial/sparse) | unchanged | already capped correctly |
| 37 | Finite-field census | unchanged | |
| 38 | Tropical geometry beyond Newton polygons | **raise** | Grok's objection was "no tropical invariant without a Newton name". There is one now: the face normal indexes the obstruction, and the tropical/normal fan is exactly the right bookkeeping for *which faces to test*. Modest raise, as an organizing instrument for avenue 1, not a standalone route. |
| 39 | Cohomological cluster (K2, motivic, Hodge, prismatic) | **raise** | "No vanishing theorem attached to `J=1`" is no longer accurate at face level: `J=1` forces `[K^{-w(1,1)/m} dxi] = 0` in the de Rham cohomology of an explicit cyclic cover. Small, but it is a real cohomological consequence of the Keller hypothesis and it is computable. |
| 40 | Free-associative Jacobian lift | unchanged | |
| 41 | Naive scaling deformation | unchanged | falsified |
| 42 | Markus–Yamabe / Hurwitz | unchanged | |
| 43 | Ritt decomposition | unchanged | |
| 44 | Moskowicz "no prime td" | unchanged | REFUTED-AS-PROOF |
| 45 | Differential Galois / Liouvillian inverse | **reopen** (low intensity) | The recorded kill — "the inverse PDE is tautological; univariate reduction reproduces Zoladek A.7" — does not apply to the object in §3. "Is `K^{alpha} dxi` exact with primitive in a prescribed eigen-coset?" is a decidable Risch/Trager–Rothstein question on an algebraic extension. Reopen strictly as the **decision procedure** for the face-endpoint criterion at arbitrary `(a,b,N,K)`, replacing my ad-hoc linear algebra. No revival of the general Liouvillian-inverse programme. |
| 46 | Lean / AI formal certification | unchanged | user-owned lane, untouched |

Net: six raises (1, 3, 12, 33, 38, 39), one lower (4), one reopen (45),
thirty-eight unchanged. Every change traces to the single mechanism in §3;
I am deliberately not inflating the count.

---

## 2. Three highest-value proof bottlenecks, two strongest falsifications

### Bottleneck B1 — the lower-row gate (highest fanout)

D5N's `I_<22` has **608 coefficient generators** over the 400-slot ring and
is undecided. Every downstream statement is licensed only modulo it: D5N's
simplification `R22(c)=H'(c)*C22`, R7R1's tower rows, D5G's `Q22` custody,
D5G35's `D23..D34` target gate, and my `nu`-tower rows. Nobody has decided
whether `C/I_<22` has a point, is proper, or is the unit ring. This is one
question with the largest downstream fanout in the campaign and it is not
anyone's named deliverable. Note the sharp asymmetry: **if `C/I_<22` is the
unit ring, the `8_28` face dies immediately** and every endpoint, mode, and
de Rham refinement above it is retroactively unnecessary.

### Bottleneck B2 — artificial replacement edge vs. genuine face

R3, R4, R5, R6, D3, D5G, D5N and D5G35 all fix `F0=(X^8-1)^2`,
`G0=(X^8-1)^3`. The campaign correctly labels this the *artificial squarefree
replacement edge* and correctly refuses to transfer its conclusions to the
original object. But the gap is larger than "a scope caveat": I verified that
the frozen `8_28` control `f = B^2 = x^2(xy^4-1)^14` has
`max(j-3i)=8` attained **only** at `(16,56)`, so its genuine upper face is a
monomial and `H = X^8`. Under R5 that is `delta = 8`, `4 | delta*(12-n)` for
**every** `n`, so every weight `0..22` carries a rational mode and the whole
upper-face mode/endpoint programme is vacuous on it. Whether the `8_28`
*family* pins `H` or leaves it free is a two-line census nobody has run
(Card B). Until it is run, the campaign does not know whether its largest
compute investment is aimed at a real object or a proxy.

### Bottleneck B3 — K00 chart-free nonemptiness with a representation-free invariant

V24R6R1 is accepted at exactly the right scope, and the adjudication is
correct that `W=0` is redundant. I record one clarification: given
`W = A1Q1+A3Q3+A4Q4`, the second accepted statement
`(Q1,...,Q5,F10,zW-1) = (1)` is a **formal consequence** of the first
(modulo the base ideal, `W = 0`, so `zW-1 = -1`). The two accepted lines are
therefore one piece of evidence, not two, and the load-bearing object is the
syzygy. The real bottleneck is that no chart-free statement about the base
scheme exists at all, and materialising the minors of a `140 x 169` matrix is
the wrong way to get one. Card C proposes the right way.

### Falsification F1 — build a `nu`-jet through row 17 and kill my own route

Pin `K = xi(xi-1)^7`, solve `Dtil_1 = ... = Dtil_16 = 0` inside the raw
`nu`-windows, and test whether `Dtil_17 = -1` is reachable. This is the
cheapest honest attempt at a **positive** fixture the GGV lane has ever had:
the target row has a genuine *linear* handle (`gtil_17`, degrees `0..7`,
8 slots), unlike `D_22` which is purely bilinear with both windows empty. If
it succeeds, my exclusion route dies and the campaign gains its first
constructive object. Either outcome is worth more than another exclusion
lemma.

### Falsification F2 — falsify the upper-face programme by pinning the face

If the `8_28` chain data pins the `(-3,1)`-face to a perfect eighth power
(as it does for the control), then R3/R4/R5/R6 give **zero** information
about `8_28`: R4's theorem needs `deg H >= 2` squarefree, R5's degree-eight
reduction needs a nontrivial squarefree part, and `H = X^8` is the maximally
degenerate `b=0` branch that R5 declares always solvable. This is a
falsification of the *route*, not of the theorems, and it is decided by
reading the frozen chain data. It should be run before any further upper-face
compute is authorised.

---

## 3. New mechanism: the second face of the corner, and the sign of `w(1,1)`

### 3.1 The frozen object has two faces

D3's lattice is
`2S = conv{(0,0),(2,0),(16,56),(0,8)}`, `3S = conv{(0,0),(3,0),(24,84),(0,12)}`.
`(16,56)` and `(24,84)` are **corner vertices**: two extremal edges meet
there.

* Upper face, outward normal `w' = (-3,1)`, i.e. `w'(i,j) = j-3i`. Maxima
  `8` on `2S`, `12` on `3S`. This is the face the campaign uses; it is the
  face that forces the chart `x=t^3X`, `y=t^-1`, and it produces the
  grading `n = 8 + 3i - j`.
* Lower face, outward normal `w = (4,-1)`, i.e. `w(i,j) = 4i-j`. Maxima `8`
  on `2S`, `12` on `3S`. This is the `(4,-1)` face already named in the
  campaign's fibre-tagged prototype review as carrying `B^2` and `B^3`. It
  produces the grading `nu = 8 - 4i + j`.

Both faces are genuine constraints on the object: the raw slot list *is* the
lattice-point set of `2S`/`3S`, so `f` has no monomial strictly below the
`(4,-1)` face any more than it has one strictly above the `(-3,1)` face.

### 3.2 The same operator, a different target (verified)

Substituting `x = tau^-4 xi`, `y = tau` and setting
`ftil = tau^8 f`, `gtil = tau^12 g`:

```text
J(f,g)_{xi,tau} = tau^-4 J(f,g)_{x,y},
J(f,g)_{xi,tau} = tau^-21 [ -12 ftil_xi gtil + 8 ftil gtil_xi
                            + tau(ftil_xi gtil_tau - ftil_tau gtil_xi) ],
```

hence, writing the campaign's operator

```text
Etil := 12 ftil_xi gtil - 8 ftil gtil_xi - tau(ftil_xi gtil_tau - ftil_tau gtil_xi),
```

a Keller pair gives

```text
Etil = -tau^17.
```

I verified this identity **and** the corresponding upper-face identity
`E = t^22 J(t^3X, t^-1)` on random exact Laurent data; both returned `True`.
The coefficient recurrence is therefore literally the same one D5G compiles:

```text
Dtil_nu = sum_{i+j=nu} [ (12-j) ftil_i' gtil_j + (i-8) ftil_i gtil_j' ],
Dtil_nu = 0 for nu != 17,       Dtil_17 = -1.
```

The `12` and `8` are unchanged. Only the target exponent moves, `22 -> 17`,
and the sign flips.

Where the two exponents come from, in one line: for a face with normal `w`,
`w(J) = w(f) + w(g) - w(1,1)`, and the target exponent is that number.
Upper: `8+12-(1-3) = 22`. Lower: `8+12-(4-1) = 17`.

### 3.3 The `nu`-grading re-partitions the identical raw lattice (verified)

Deriving the windows from the polygon inequalities:

```text
ftil_nu:  max(0, ceil((8-nu)/4))  <= i <= 16-nu
gtil_nu:  max(0, ceil((12-nu)/4)) <= i <= 24-nu
```

Census check against D3: my `nu`-windows give `141` `f`-slots and `301`
`g`-slots, total `442`, identical to D3's `t`-grading census and to a direct
lattice-point count of `2S`/`3S`. **The two towers are two gradings of one
equation system, not two systems.** That is exactly why this is a face
isolation and not new data: the same identity, read along a different face,
yields a different leading-order obstruction.

Two structural differences that matter:

* `ftil_17` is **empty** but `gtil_17` has 8 slots (degrees `0..7`). The
  lower target row therefore has a *linear handle*, whereas `D_22` is purely
  bilinear (`F_22` and `G_22` both empty).
* The lower edge is exactly saturated by the frozen face: `ftil_0` occupies
  degrees `2..16` and `gtil_0` degrees `3..24`, which is precisely
  `xi^2 htil^2` and `xi^3 htil^3` with `deg htil = 7`.

### 3.4 The general face-endpoint theorem

Both faces have square/cube leading forms, and this is forced rather than
lucky: `Dtil_0 = 0` reads `12 ftil_0' gtil_0 - 8 ftil_0 gtil_0' = 0`, i.e.
`3 ftil_0'/ftil_0 = 2 gtil_0'/gtil_0`, so `ftil_0^3 ∝ gtil_0^2` and, in a
UFD, `ftil_0 = alpha K^2`, `gtil_0 = beta K^3`. With the windows above,
`xi^2 | ftil_0` forces `xi | K`, so on the lower face `K = xi * htil`.

Now perturb `gtil` by `tau^N d` at relative weight `N` above an edge with
`ftil = c K^{a/m}`, `gtil = c' K^{b/m}`, `a = 8-nu_f`, `b = 12-nu_g`,
`m = gcd(a,b)`. The weight-`N` row is

```text
(b-N) ftil' d - a ftil d'
   = -c a K^{a/m + q} * (K^{-q} d)',        q := (b-N)/m.
```

Setting this equal to a nonzero constant gives

**Theorem (face-endpoint criterion).** The weight-`N` endpoint above a face
with data `(a,b,m)` is rationally solvable if and only if

```text
K^{(N - a - b)/m} dxi     is exact
```

in the corresponding cyclic cover. Since `N = w(f)+w(g)-w(1,1)` and
`a+b = w(f)+w(g)`, the exponent is **`-w(1,1)/m`, independent of the shift
`(nu_f, nu_g)`**.

Instantiations:

```text
upper face:  w(1,1) = 1-3 = -2,  m=4  ->  K^{+1/2} dX     (hyperelliptic; matches the recorded [w dX] criterion)
lower face:  w(1,1) = 4-1 = +3,  m=4  ->  K^{-3/4} dxi    (mu_4 cover; NEW)
```

This is the unification the packet asked for in item 4: R5's `2Hg'+H'g=2H`,
Opus5's earlier `M(Y) = 4H^{-1/2} d/dX(H^{3/2}Y)`, and R7R1's `p^4 = H` are
all the `m=4` slices of one face-indexed statement, and the exponent is a
pure Newton-geometric invariant of the face.

### 3.5 The lower-face endpoint, solved exactly

At `N = 17`, `q = -5/4`, the endpoint ODE is (with `g = 8K^2 d`)

```text
4 K g' - 3 K' g = 4 K,          equivalently  (K^{-3/4} g)' = K^{-3/4}.
```

**Poles are impossible.** At a prime `p` of multiplicity `e` with
`v_p(g) = mu < 0`, the leading coefficient of the left side is
`mu - (3/4)e != 0` (it vanishes only at `mu = 3e/4 >= 0`), so
`v(LHS) = mu - 1 < 0 = v(RHS)`. Hence `g` is a **polynomial**. This is the
exact point where the lower face differs from the upper: at `N=22` the same
coefficient is `mu + e/2`, which *does* vanish at `mu = -e/2`, which is
precisely R5's "reduced denominator divides `A`". The lower face has no such
escape.

Degree law: `deg(4Kg') = deg(3K'g) = deg g + 7`, with leading coefficient
`(4r-24) lc(K) lc(g)`, so `r = deg g in {1, 6}` exactly.

Exhaustive exact classification (all multiplicity patterns, `deg K <= 8`;
two-root patterns to `deg K <= 12`; root positions sampled 15x per pattern):

```text
deg K = 1..3, 5..7 :  solvable only for a single root, K = c (xi-a)^D
deg K = 4          :  [4], [3,1], [2,2]
deg K = 8          :  [8], [7,1], [6,2], [5,3]
```

Closed form of the observed rule, over the algebraic closure:

> `K^{-3/4} dxi` is exact iff `K` has **one** distinct root, or **exactly
> two** distinct roots with `4 | (e_1+e_2)` and `4 ∤ e_1`.
> Three or more distinct roots: never.

Proof sketch (not a proof): on `y^4 = K` the differential `dxi/y^3` is exact
iff the cover is rational and all residues vanish. The cover has genus `0`
only with at most two branch points; with `>= 3` it has genus `>= 1` and
`dxi/y^3` acquires a nonzero holomorphic component — for `K` squarefree of
degree `8` I computed `div(dxi/y^3) = 4 * (four points at infinity)`, degree
`16 = 2g-2` with `g = 9`, i.e. `dxi/y^3` is a nonzero **holomorphic**
differential and therefore never exact. `4 | e_1` makes the cover reducible
with `K^{-3/4} = (pq)^{-3}` rational and nonzero residues.

**Corner-farm consequence.** For a GGV corner whose `(4,-1)` face has a
single residual root of multiplicity `gamma` (so `K = xi (xi-rho)^gamma`,
`deg K = gamma+1`), the endpoint survives iff

```text
gamma = 3 (mod 4).
```

Verified for `gamma = 1..20`: solvable exactly at `gamma = 3,7,11,15,19`.

**`8_28` has `gamma = 7`, and therefore passes.** I emphasise this: the new
filter does not kill the campaign's flagship face. That is the right sanity
check — a filter that killed everything would be wrong — and it means the
`8_28` payoff lies one level deeper (Card A), while the *farm-wide* payoff is
immediate (`gamma != 3 mod 4` corners die at the face, for free).

### 3.6 Why the lower face is the rigid one

For `K = xi(xi-1)^7`, `delta = gcd(1,7) = 1`, so R5's mode schedule
`4 | delta(12-nu)` admits modes only at `nu = 0,4,8,12,16`, with leading
terms `K^3, K^2, K, 1, K^-1`. The last is **not** a polynomial and is
excluded by the raw window, so exactly **four** homogeneous modes exist below
the target. There is **no weight-17 kernel** (`4 | 5 delta` fails), so the
endpoint residual is unique, with no affine freedom.

Contrast the genuine upper face of the control, `H = X^8`, `delta = 8`:
`4 | 8(12-n)` for every `n`, so **all 23** weights carry a mode. The upper
face of the real object is the maximally floppy case; the lower face of the
same object is the maximally rigid one.

I computed the unique lower endpoint residual for `8_28`:
`g = 4xi - (84/5)xi^2 + (448/15)xi^3 - (1792/65)xi^4 + (14336/1105)xi^5
- (8192/3315)xi^6`, with `g(0) = g(1) = 0`, so

```text
d = g/(8K^2) = q(xi) / (8 xi (xi-1)^13),      deg q = 4.
```

The residual has a pole of order 13 at the residual root and order 1 at
`xi = 0`, and is **not** a polynomial. If the R3-style argument (lower rows
force the solution into the mode span, so the endpoint residual is unique)
transfers to `N=17` — which is precisely what Card A tests — then the `8_28`
`(4,-1)` face is excluded outright. I am **not** claiming that; the mixed
lower-row terms are exactly the part I have not done.

---

## 4. New cross-avenue connection

**Avenue 33 (global symplectic exactness / action residues) x avenue 1 (GGV
corner farm) x avenue 12 (face isolation), through avenue 39.**

The action-residue gate was closed as `COSTUME` because `P dQ - x dy = dS`
holds polynomially, so the *untwisted global* divisorial residues are
automatic. §3.4 shows the non-automatic object: for each extremal face `w`,
the Keller identity forces the vanishing of a **twisted** class

```text
[ K^{-w(1,1)/m} dxi ]  in  H^1_dR( y^m = K ).
```

This is a residue/period obstruction attached to `J = 1`, it is face-indexed
(so the Newton fan — avenue 38 — is the correct enumeration of the tests), it
is arithmetic (`mod m` divisibility of the face-form multiplicities, plus a
`mu_m` Kummer descent — avenue 12), and it is computable by a decision
procedure (avenue 45). None of those five avenues, alone, produced this
object; the connection is what makes it decidable.

A second, weaker connection worth recording: avenue 25 (dessins/passports).
The external Suzuki classification the campaign cites is of the **top** edge
of `(8,28)`. The `(4,-1)` face carries an independent one-place datum
`K = xi(xi-rho)^gamma`, so a passport constraint derived from the top edge
and one derived from the bottom edge are logically independent constraints on
the same cover. I have no decisive test for this and do not claim novelty
credit for it.

---

## 5. Packet item 4 — connecting the tower, the raw determinant, and the survivor geometry

They should **not** remain separate. They compose, in this exact shape:

```text
  D5G / D5G35 (compiler)  --supplies-->  literal rows D_n
  R7R1 (tower)            --converts-->  row D_(n+22)  ->  exactness of q_n dX
  R5 / R6 (geometry)      --is-->        the n = 0 slice of that tower
  [NEW] face index w      --parametrises--> which grading the rows are read in
```

Concretely:

1. **R5 is R7R1's first row.** R7R1 already records that trace descent
   recovers R5 from `q_0`. §3.4 explains *why* the exponent is `1/2`: it is
   `-w'(1,1)/m = 2/4`. So R5/R6's survivor geometry is the `n=0`,
   `w=(-3,1)` corner of a two-parameter family of conditions.
2. **D5G35 already supplies the missing tower rows.** R7R1 says `q_1` needs
   `D_23` and `q_2` needs `D_24`, and that D5G stops at `D_22`. The live
   direct extension reaches `D_35` (the structural addendum in that live
   tree, which I read only for deduplication, notes `D_35 ≡ 0` by
   cancellation and `D_34` as the last nontrivial row). That licenses rows
   `q_0 .. q_13` — **fourteen** independent exactness conditions on the same
   `H`, where R5 uses one. The correct composition target is therefore not
   "one more endpoint" but the **de Rham ladder** `[q_n dX] = 0`,
   `n = 0..13`, whose `n`-th condition is a differential of increasing pole
   order at infinity and which should generically fail at small `n`.
3. **The shared blocker is B1.** Every one of those rows is licensed only
   after `I_<22` (608 generators) is imposed; D5N's negative fixture
   (`D21 = X`, `s = t` contributing `1` to the endpoint) is exactly the
   demonstration that no row may be read locally while a lower row is live.
   So the composition is real but gated on one undecided ideal.
4. **The new degree of freedom is the face.** Everything above is the
   `w = (-3,1)` column of the table. The `w = (4,-1)` column has target 17,
   exponent `-3/4`, and — critically — a leading form that is *pinned by the
   chain* rather than artificially replaced.

The honest summary: the three objects are one object with two indices
(face, row); the campaign has been computing the `(face = upper, row = 0)`
entry with an artificial input, at high cost, while `(face = lower, row = 0)`
is exact, pinned, cheap, and unattempted.

---

## 6. Software / AWS acceleration, with firewall

**Acceleration: re-grade, do not re-derive.**

`compile_d5g.py` consumes (i) the 442-slot lattice, (ii) a weight functional
that assigns each slot a `t`-degree and an `X`-degree, and (iii) the pair
`(8,12)`. Every one of those is already parameterised in substance. Replacing
the hard-coded `n = 8+3i-j`, `X-degree = i` by a face-normal argument
`--face p,q` yields the entire second tower at essentially **zero marginal
implementation cost** and reuses the reviewed sparse arithmetic verbatim.

The acceleration is also a **free hostile test of D5G itself**. Both gradings
expand the *same* polynomial `E`. Therefore:

```text
multiset of (x,y)-monomials of 12 f_x g - 8 f g_x - (Jacobian correction)
  computed via the (-3,1) grading
= the same multiset computed via the (4,-1) grading.
```

A cross-grading digest comparison is an end-to-end checksum on 32,135 terms
and 58,572 contributions that no single-grading replay can provide — it
catches exactly the class of error (a wrong `(i-8)`/`(12-j)` coefficient, a
dropped slot) that D5G's own mutation tests probe only pointwise. D5G's audit
already found `(i-8) -> (i-7)` detectable; the cross-grading check detects
that plus every grading-asymmetric transcription error, at one extra run.

**Evidence firewall (exact):**

1. The re-graded compiler is a **new artifact** at tier
   `INTERNAL-UNREVIEWED`, in a new case directory, with its own
   `PREREGISTRATION.md` and freeze. It does not modify, re-freeze, or
   re-hash D5G, D5G35, D5N, D3 or D4R1, and it does not enter `AUDIT.md`.
2. Cross-grading agreement is a **consistency** result. It is not
   independent confirmation of D5G (same source lattice, same author
   lineage) and must never be reported as different-model review. A
   disagreement is a `TYPE-FAIL` that quarantines *both* gradings until
   resolved; an agreement upgrades nothing.
3. Every `nu`-tower mathematical claim carries the premise
   `PROVISIONAL: face-endpoint criterion at N=17`, names R5 as the
   instantiated theorem, and rolls back with it.
4. Desk-scale only until the row count exceeds the D5G budget; heavy runs go
   to AWS with a registered tag, recorded hostname, and the classical
   frontier gate rerun on the new scope (this lane is `NOT_CLOSED_BY_THIS_
   GATE`: it is unbounded-total, partial-`y`-frontier work).
5. No claim of GGV landing, family exclusion, `G2-PSC`, `G2-BD`,
   cofinality, or JC2 may be attached to any output of this lane.

---

## 7. Idea cards

### Card A — `NU17`: the second-face determinant tower and its endpoint

**Target gap.** B2 (artificial-edge scope) and, through it, the first
face-level exclusion of the genuine `8_28` object. The upper-face programme
cannot exclude `8_28` because its genuine leading form degenerates; the lower
face is pinned and rigid.

**Exact dependencies.**
- D3 raw lattice `RAW_INPUT.json` (frozen, `012acfe5...`) — the only input.
- R5's endpoint theorem, *instantiated at `N=17` instead of `N=22`*. This is
  a premise: R5's proof must be re-audited for `N`-genericity. The mode
  schedule `4 | e_i(12-n)` is manifestly `N`-independent; the endpoint
  reduction depends on `N` only through `q = (12-N)/4`.
- My §3 identities (verified) and §3.5 classification (verified).
- **Not** dependent on D4R1, D5G, D5N, R6, R7R1, or any K00 object.

**Cheapest discriminator.** Three staged tests, all desk-to-small scale:
1. *(minutes, already done)* Confirm `Etil = -tau^17 J`, the `nu`-window
   census `141/301/442`, and `K = xi(xi-rho)^gamma` with `gamma = 7`.
2. *(hours)* Re-grade the D5G compiler by `--face 4,-1` and emit
   `Dtil_0..Dtil_17` literally, with the cross-grading digest check of §6.
3. *(hours)* Impose `Dtil_1 = ... = Dtil_16 = 0` on the raw `nu`-windows
   with `ftil_0 = alpha K^2`, `gtil_0 = beta K^3`, `K = xi(xi-1)^7`, and
   decide whether `Dtil_17 = -1` is reachable. The linear handle `gtil_17`
   (8 slots) makes the last row an inhomogeneous linear test against a
   bilinear residue, not a blind search.

**PASS meaning (row 17 unreachable).** The `8_28` `(4,-1)` face admits no raw
polynomial jet. That is a face-level exclusion of the *genuine* frozen
object — strictly stronger than every current GGV result, all of which are
scoped to the artificial replacement edge. It is still not GGV landing, not a
family theorem, and not `G2-PSC`.

**FAIL meaning (row 17 reachable).** The campaign gains its **first positive
fixture**: an explicit raw jet satisfying a complete face system through its
target. That immediately re-ranks the whole GGV lane toward realisation, and
it falsifies my §3.6 rigidity intuition. This is the outcome I would bet
against and would most like to see.

**Stop condition.** Stop at the first `nu <= 16` whose row is unsatisfiable
in the raw windows (early kill, cheaper than the full run); stop after row 17
either way; stop immediately if the cross-grading digest disagrees with D5G.
Hard cap: one D5G-equivalent compute budget. Two non-informative rows in a
row without a rank change forces a redesign, per `COORDINATION.md`.

**Rollback subtree.** Everything under `NU17` rolls back if (a) R5's
`N`-genericity audit fails, (b) the chain does not pin `K` (Card B returns
"lower face free"), or (c) the cross-grading digest disagrees. Nothing in the
existing `t`-tower depends on `NU17`, so rollback is a directory deletion.

**Expected information gain.** High and two-sided. It is the only current
GGV proposal whose leading input is pinned by frozen chain data rather than
replaced, and both outcomes change the campaign's top-lane ranking.

---

### Card B — `FACEPIN`: which of the two faces does the `8_28` chain actually pin?

**Target gap.** B2, directly. The campaign does not currently know whether
its upper-face compute is aimed at the real object.

**Exact dependencies.** The frozen chain data only
(`final=(11,4,7)`, `steps=((4,-1,3,4),)`, `mn=(3,2)`, `degs=(108,72)`,
`gamma=7`), the D3 lattice, and GGV Algorithm 3 as already transcribed in
`AUDIT.md`'s founding audit. No new theorem, no compute beyond desk scale.

**Cheapest discriminator.** For the `8_28` family as defined by the frozen
chain, determine for each face separately whether the leading form is
*pinned* (determined by the chain data up to normalisation) or *free* (an
unconstrained degree-eight parameter). Two concrete checks:
- upper: is `H` forced to be a perfect eighth power, as it is for the frozen
  control `f = B^2` (verified: `max(j-3i)` attained only at `(16,56)`), or is
  the whole 17-point face free?
- lower: is `K = xi(xi-rho)^7` forced by `gamma = 7` with a single residual
  root, or may the `(4,-1)` face carry additional residual roots?

**PASS meaning (upper free, lower pinned).** The current reading is
vindicated in form but the ranking inverts: the artificial replacement is a
legitimate generic model of a free face, while the *other* face carries an
exactly known form. Card A becomes the top GGV lane.

**FAIL meaning (upper pinned to `X^8`).** R3, R4, R5, R6 and R7R1 give no
information about `8_28`: `H = X^8` is R5's always-solvable `b=0` branch and
R4's hypotheses fail. The upper-face compute must be relabelled
`method-control` and the lane re-rooted. This is the single cheapest way the
campaign can discover that a large investment is aimed at a proxy.

**Stop condition.** One desk session. If the chain data are ambiguous, record
`SCOPE-UNDECIDED` and escalate rather than guessing — do not let an
assumption about pinning enter any freeze.

**Rollback subtree.** None; this card only *reads*. Its output re-scopes
existing claims, so its own outputs are scope annotations, appended, never
overwriting.

**Expected information gain.** Very high per unit cost. It is a read, and it
can invalidate the top lane's relevance.

---

### Card C — `FITMEM`: replace the K00 Fitting atlas by minor-membership certificates

**Target gap.** B3: a chart-free, representation-independent statement about
the K00 grade-seven base scheme, without materialising the minors of a
`140 x 169` matrix.

**Exact dependencies.** V24R6R1's accepted syzygy `W = A1Q1+A3Q3+A4Q4`
(provisional, `1883b74b...`), the frozen six-variable base
`B = (six quadratic initials, F10)`, and the existing exact-Q membership
tooling that returned in 0.13 s.

**Mechanism.** V24R6R1's content is exactly: *one* `5x5` minor lies in the
base ideal, i.e. vanishes identically on the base scheme. (I note the printed
unit-ideal line `(Q1..Q5,F10,zW-1)=(1)` follows formally from that syzygy and
is not independent evidence.) The representation-independent successor is not
"compute `I_5(A)`"; it is the sequence of questions

```text
for each 5x5 minor  M_k  of the frozen matrix:   is  M_k  in  B ?
```

Each is one exact ideal-membership test emitting an explicit cofactor
certificate — the same shape and cost as the one already computed — and each
is division-free and replayable. `M_k in B` for all `k` proves rank `<= 4` on
the whole base scheme, chart-free, with no Gröbner basis of `I_5` and no
localisation. The first `M_k not in B` names the unique live chart and the
atlas collapses to it.

**Cheapest discriminator.** Run the membership test on a *stratified sample*
of minors first — the ones sharing the most columns with `W`, then a random
sample — before any exhaustive pass. If the sampled minors are all in `B`,
the exhaustive pass is worth its cost; if the first sampled minor is not, the
atlas has already collapsed to one chart.

**PASS meaning (all sampled minors in `B`).** Strong evidence for rank `<= 4`
on the base scheme, obtained as a list of exact certificates rather than one
Gröbner run, and the exhaustive pass becomes a bounded, shardable, embarrassingly
parallel AWS job with a per-minor certificate.

**FAIL meaning (some minor not in `B`).** The rank-five stratum is nonempty
somewhere; that minor's chart is the unique live one and every other branch
of the preregistered atlas is dead. Either way the atlas shrinks.

**Stop condition.** Stop at the first non-member (chart named) or after the
sampled batch plus one exhaustive shard without a new rank/codimension fact.
No modular evidence may substitute for an exact certificate at any step.

**Rollback subtree.** Rolls back with V24R6R1 if the live Opus5 cross-audit
refutes the syzygy; the membership tests themselves are independent of it and
survive as raw data.

**Expected information gain.** Medium-high, and it directly implements the
already-agreed principle "every cut must carry an exact invariant" without
the intractable step everyone flagged.

---

## 8. `continue` / `redesign` / `stop` per current major lane

| Lane | Decision | Immediate rule |
|---|---|---|
| GGV upper-face R3–R7 tower (R5 promoted, R6/R7R1 in review) | **redesign** | Finish the live reviews, then **freeze new upper-face theorem production** until `FACEPIN` says whether the face is free or pinned. R5/R6 are correct and should keep their scope; more refinements of an artificial edge have falling marginal value. |
| D5G / D5G35 raw-global compiler | **continue** | Highest-value infrastructure in the campaign. Add the `--face` parameter and the cross-grading digest (§6) as the next increment, not a new tower from scratch. |
| D5N naturality bridge / lower-row gate `I_<22` | **continue and raise to top proof priority** | This is B1. It should be somebody's named deliverable with a stop condition, not a caveat repeated in four reports. |
| `NU17` second face | **launch** (Card A) | New. Depends on nothing under review except an `N`-genericity audit of R5. |
| K00 V24 / V26 Fitting atlas | **redesign** | Replace minor materialisation by minor-membership certificates (Card C). Keep the long exact-Q R2/R5 lanes as independent cross-checks. |
| K00 exact-Q long jobs | **continue** | Unchanged; they are the only independent cross-check. |
| C5 total certificate / typed transport | **stop as a research lane** | Reviewed at its narrow scope; V43C6 gave the correct fail-closed transport answer. Bank and stop; no new exponent ladders, no alias-based receivers. |
| Global landing / `G2-PSC` / `G2-BD` / cofinality | **continue at top proof priority** | Unchanged. A face endpoint, on either face, is an input and never the transport/coverage theorem. |
| V47/V48 strict compiler | **stop** | Unchanged from the prior synthesis. |
| Ramified / equality / positive-load / off-family coverage | **continue** | Select from a coverage inventory. |
| AS109 `n=6` | **continue narrowly** | Surviving content strata, fixed support, no duplicate floors. |
| Formal / TD6 | **continue at registered caps** | New work needs source reachability or an algebraization invariant. |
| Matysiak / external intelligence | **continue bounded** | Lawful acquisition, dependency-first. The abstract is not evidence and the 2024 history is a prior, not a refutation. |
| Dead ladders (11, 18, 41, 44) | **stop** | No revival without a named client and a decisive test. |

---

## 9. The insight a differently-trained researcher is most likely to miss

**The two faces of the corner are not symmetric, and the asymmetry is the
sign of `w(1,1)`.**

A strong researcher who is told "there is a second face" will re-run the
superelliptic analysis there and expect a structurally similar answer — a
second hyperelliptic exactness condition, a second `A = Bv' + (3/2)B'v`, a
second codimension-four survivor stratum. That expectation is wrong, and the
reason is a single line of weight bookkeeping that is easy to skip because
`dx ^ dy` looks like a symmetric object.

Derivation. For a face with outward normal `w`, `w(x^i y^j) = w(i,j)`, and

```text
w(J(f,g)) = w(f) + w(g) - w(1,1),
```

because `J` differentiates once in `x` and once in `y`, costing `w(1,0)` and
`w(0,1)`. The Keller target `J = 1` therefore sits at face-height
`w(f)+w(g)-w(1,1)`, and by §3.4 the endpoint differential is
`K^{-w(1,1)/m} dxi`.

Now `w(1,1) = p + q` for the normal `(p,q)`. For a Newton polygon in the
first quadrant, the two edges meeting at the far corner have normals of
**opposite** `p+q` sign: here `(-3,1)` gives `-2` and `(4,-1)` gives `+3`.
Hence:

```text
upper face:  exponent  +1/2   ->  poles only at infinity
                                  -> de Rham reduction, [w dX] = -(4/5)[omega],
                                     a computation whose answer depends on H
lower face:  exponent  -3/4   ->  poles at every root of K
                                  -> residue/holomorphy question on a mu_4 cover,
                                     answered by the multiplicity pattern alone
```

Three consequences that fall out only after you notice the sign:

1. The escape hatch differs. At `+1/2` the local coefficient
   `mu + e/2` vanishes at `mu = -e/2`, so rational solutions with
   denominators exist — this is exactly R5's "reduced denominator divides
   `A`". At `-3/4` the coefficient `mu - 3e/4` never vanishes for `mu < 0`,
   so **`g` is forced polynomial** and the entire denominator branch that
   R5 needed simply does not exist.
2. Consequently the survivor locus is far thinner: R6 gets codimension
   `floor(h/2) = 4` at degree eight; the lower face gets *at most two
   distinct roots*, i.e. three parameters out of nine, and two after
   `xi | K` — codimension seven.
3. And the modes invert. The `8_28` control's upper face has `delta = 8`, so
   every weight carries a mode and the face is maximally floppy; its lower
   face has `delta = 1`, so only `nu = 0,4,8,12` carry a polynomial mode and
   there is no kernel at the target at all.

The trap is that "the corner has two edges" is completely standard GGV
language — the campaign already names the `(4,-1)` face — so it is natural to
assume the second edge has been folded in, or that it is the same
computation. It has not been, and it is not: it is the same *operator* with
an inverted endpoint exponent, and that inversion is where the rigidity is.

---

## 10. Honest ledger

### Conjectural leaps

1. **R5's `N`-genericity.** I instantiate the endpoint criterion at `N=17`.
   R5's promoted statement is at `N=22`. I checked that the mode schedule is
   `N`-independent and that the endpoint reduction depends on `N` only
   through `q=(12-N)/4`, and I validated my solver against R5's `N=22`
   answers, but I did **not** re-derive R5's mode-completeness proof at
   `N=17`. Card A names this as its first dependency.
2. **Uniqueness of the endpoint residual.** §3.6 computes the residual as if
   the lower rows force the solution into the mode span. That is R3's
   structure at `N=22`; I have not established it at `N=17`, and the mixed
   lower-row terms are exactly what Card A step 3 computes. **No exclusion
   of `8_28` is claimed.**
3. **Face pinning.** I infer `K = xi(xi-rho)^7` from the campaign's own
   record that the `(4,-1)`-maximum faces are `B^2`, `B^3` with
   `B = x(z-1)^7` and `gamma = 7`. Whether the chain *forces* a single
   residual root for the whole family is Card B, not a verified fact.
4. **The classification's closed form.** Exhaustively verified for
   `deg K <= 8` (all partitions) and two-root patterns to `deg K <= 12`. The
   genus/residue argument in §3.5 is a sketch, not a proof.
5. **Shifted-edge cases.** If `ftil_0 = 0` or `gtil_0 = 0` the parameters
   become `(a,b) = (8-nu_f, 12-nu_g)` and `m` changes, so the exponent
   `-3/m` changes. I checked that the exponent numerator is invariant
   (`N-a-b = -w(1,1)` always) but did not enumerate the finite shifted case
   list (`nu_f+nu_g <= 17`), and `a`, `b` may be negative there.

### Failed attempts and self-corrections

- My first pole analysis assumed `g` polynomial for **both** faces. That is
  false at `N=22` and my R5 control failed 203/240. Correcting it (rational
  `g` with denominator dividing `A`, via R5's own `g = Bz/A`) brought the
  control to 120/120. The failure was informative: it is precisely the
  asymmetry in §9 point 1.
- My first guess at the `N=17` classification was "only `K = c(xi-a)^8`",
  from the `deg g = 1` branch. `K = xi^7(xi-1)` is solvable with
  `deg g = 6`, which refuted it; the `deg g in {1,6}` dichotomy is what
  survives.
- I initially thought the top determinant rows `D_23..D_35` were unimposed
  new equations. They are the same equations regraded, and the live D5G35
  tree had already found `D_35 ≡ 0` by cancellation. I dropped that as a
  contribution; it is not mine and it is not new.

### Checks actually performed (all exact, local, desk-scale)

1. All seven frozen-basis SHA-256 values and the basis commit — matched.
2. All four pinned GGV producer hashes, the Grok producer hash, and the K00
   adjudication hash — matched.
3. `D_n = sum_{i+j=n}[(12-j)F_i'G_j + (i-8)F_iG_j']` verified against the
   literal expansion of `E` on random exact data, all `n` in `0..12`.
4. Upper identity `E = t^22 J(t^3X,t^-1)` — `True` on random Laurent data.
5. Lower identity `Etil = -tau^17 J(tau^-4 xi, tau)` — `True`, same data.
6. `nu`-window census `141 / 301 / 442`, matching D3's `t`-grading census and
   a direct lattice count of `2S`, `3S`.
7. R5 control: `4a0 + D a2 = 0` reproduced on 120/120 samples (60 random,
   60 forced hits); `b=0` always solvable (20/20); `b=8` squarefree not
   solvable.
8. `N=17` denominator impossibility: `g = u/K^k`, `k = 0..3`, no solution for
   `K = X^8-1` and `K = X^4(X-1)^4`.
9. Full partition sweep at `deg K = 8` (22 patterns), sweeps at
   `deg K = 1..7`, two-root sweep to `deg K = 12`, 15 random root-position
   samples per solvable pattern, and irreducible-quadratic cases.
10. `gamma = 1..20` single-residual-root sweep: solvable exactly at
    `gamma = 3,7,11,15,19`.
11. `8_28` endpoint residual computed exactly and re-verified as a rational
    identity `Dtil_17 = -1`; `g(0) = g(1) = 0` confirmed.
12. `8_28` control upper face: `max(j-3i) = 8` attained only at `(16,56)`.

No AWS was launched, no canonical ledger was changed, no freeze was written,
no heavy local algebra was run (peak working set well under a megabyte), and
`jc2-lean` was never entered, read, built, status-inspected, or modified.

### Scope firewall

- Nothing here proves or disproves JC2, a GGV family, GGV landing,
  `G2-PSC`, `G2-BD`, cofinality, Gate T, order two, maximum twelve,
  terminal reachability, or K00 closure incidence.
- The `gamma = 3 (mod 4)` filter is a **necessary** face condition on a
  restricted corner shape, verified computationally in a stated range. It
  excludes no family until the corresponding corner data are matched to it.
- `8_28` **passes** the new filter. This submission contains no exclusion of
  `8_28`.
- A face endpoint is not a jet; a jet is not an arc; an arc is not a
  polynomial map; a compiler is not a theorem; and a consistency checksum
  between two gradings is not different-model review.

---

## 11. Custody and blindness

Verified before analysis (recomputed locally, all matched):

```text
418e413593120d19e15e6546eb50c985f4b1f038   git basis
f834120a...  COORDINATION.md      a80aab6d...  APPROACHES.md
53ce5232...  AUDIT.md             7560da66...  PROGRESS.md
a83f6c9a...  notes.md             a03936b7...  ideation-20260827T1349Z-synthesis-sol.md
a8a1ae4f...  websweep-20260827T1348Z.md
59e9bf2c...  d5g          ed0e3460...  r6          9d35c678...  r7r1
a0257c26...  d5n          43a949b2...  grok survivor raw-support
1883b74b...  ADJUDICATION_V24R6R1.md
```

**Blindness disclosure.**

1. I read exactly two `ideation-20260827T1606Z-*` files: my own prompt and
   the sealed packet. At the start of my session `ls xmodel/ | grep 1606Z`
   returned only three entries — the two prompts and the packet — so no peer
   submission existed while I did the analysis in §3–§5. On my final
   write-scope check, `xmodel/ideation-20260827T1606Z-fable5.md` had appeared
   on disk. **I did not open it, list its contents, hash it, or search it**,
   and it postdates every mathematical claim above. Every repository search I
   ran excluded the `1606Z` pattern explicitly, before and after.
2. **Live-job artifact, disclosed.** During the mandatory novelty search I
   read `cases/ggv_8_28_raw_global_determinant_d5g35_20260827/STRUCTURAL_D35_
   ADDENDUM.md`, which belongs to a job the packet declares live and outside
   the snapshot. I read it **only** to deduplicate, and it correctly
   deduplicated one candidate contribution of mine (the top determinant row
   `D_35 ≡ 0`), which I then withdrew (§10). No claim in this report depends
   on it; §5 cites it only as "the live tree already reaches `D_35`", which
   the packet itself states.
3. **Incidental prior-round lines.** Two `grep` passes surfaced roughly
   seven single context lines from four prior-round individual ideator
   submissions (`0635Z-fable5`, `0935Z-grok`, `0935Z-grok-crossreview`,
   `0935Z-opus5-crossreview`). All concerned K00/V43 weight-30/35
   bookkeeping and stop rules. None concerned Newton faces, gradings,
   superelliptic endpoints, or anything in §3–§5. I opened none of those
   files.
4. I read the prior-round synthesis as the packet's designated dedup
   baseline, and the Grok survivor report, D5G, D5N, R6 and R7R1 as pinned
   packet evidence.

I therefore report this submission as **CLEAN-BLIND for the round**, with the
two disclosures above (a live-job artifact read for deduplication, and
incidental prior-round grep context) recorded for the coordinator to weigh.
