# Blind ideation submission — round 20260902T1608Z — Opus 5

Charged input `xmodel/ideation-20260902T1608Z-packet.md`, SHA-256
`ab66bd6b87dc035740325c309349ec8d52a5963b6b1a0a6e0e53a34f74715af3`, verified.
Basis 7f7c0306768d. Blind: no `ideation-20260902T1608Z-*` submission was opened.
(One `grep -n NOETHER-K xmodel/*.md` returned a single citation line from a
sibling submission file; it contained no mathematical content and was not
followed up. Disclosed, not consumed.)

## 0. Verdict, up front

**The coordinator's reading is wrong, and I can say exactly where.**

The claim under review is: *"Every boundary-tree instrument that touches N
yields N ≤ (something in D) or D ≥ (something in N)."* That is true of every
instrument the campaign has actually built, and the packet's diagnosis of WHY
is also right for those instruments — they are all **contact** instruments, and
contact enters `N` with a **minus** sign, so more (unknown) tree can only lower
`N`. `FILTER-INVERSION` is the correct reading of `N-CEILING`.

But contact is not the only boundary functional. The **multiplicity** functional
on the same cluster enters `N` with a **plus** sign, and it is monotone in the
direction the campaign needs: *any subset of the boundary cluster gives a
FLOOR on N*. Concretely, with `p = deg P = Kd`, `q = deg Q = Ke`,
`m_ν, m'_ν` the multiplicities of the generic members of the two pencils at the
common infinitely-near base points at infinity:

```text
    THEOREM ORTHO-DEFECT     sum_nu ( e·m_nu  -  d·m'_nu )^2  =  (ep - dq)^2 + 2·d·e·N
                             =  2·d·e·N          under the GGV/Moh normalisation ep = dq.
```

Every term on the left is a non-negative integer. Hence for **every** subset
`S` of the cluster — in particular for the part of the cluster that a Moh
skeleton already determines —

```text
    COROLLARY ORTHO-FLOOR    N  >=  (1/2de) · sum_{nu in S} ( e·m_nu - d·m'_nu )^2 .
```

That is a mechanism that bounds `N` from **below** by boundary-tree data. It is
what `OPEN[UPPER-TO-FLOOR]` asks for. It is not a ceiling on `D` yet — the
crossing needs the left-hand side to be shown large — but it inverts the
monotonicity that the packet says is unavailable, and it makes the crossing a
**computation on the census that already exists** rather than a search for a new
formalism.

Two further consequences that are immediately usable:

* **`ORTHO-KILL` is unconditional and two-sided.** A Moh skeleton is dead if
  `L(skel)/(2de) > U(skel)`, where `L` is the left side summed over the
  skeleton and `U` is the promoted `N-CEILING`. No `H2`, no `N ≤ 16`.
* **`ORTHO-TOWER`.** Moh's own descent `G_1 = β^d P^e − α^e Q^d` has
  `N(P, G_1) = d·N` exactly, and `ORTHO-DEFECT` applies verbatim at every
  stage of the descent. The recursion has `3 ≤ s ≤ log_2 K` stages
  (`DEPTH-LOG`), so a degree-minimal counterexample carries **`s` independent
  floors on `N`**, and the last of them lives precisely below `D_1` — where the
  running `d1-subtree` lane already is.

`THEOREM NO-CEILING` is not violated; it is not applicable. Its proof is about a
**single** class `Z` and states in terms that "none [of the constraints] is a
negativity". `ORTHO-DEFECT` is exactly the missing negativity, supplied by the
**pair** of classes: `Δ = eC_u − dC_v` has zero `H`-component and
`Δ² = −2deN < 0`. §4 gives the precise scope repair.

The rest of this report delivers the contract. §1–§3 are the mathematics and its
controls; §4 the corrections to banked readings; §5–§13 the contract items.

---

## 1. THEOREM ORTHO-DEFECT

### 1.1 Setting

`P, Q ∈ C[x,y]`, both non-constant, `p = deg P`, `q = deg Q`. Let
`π : X → P^2` resolve the base locus of both pencils `{P = u}` and `{Q = v}`,
i.e. blow up the union of the two base clusters at infinity until the generic
members of each pencil are separated. Index the blown-up (infinitely near)
points by `ν`, and let

```text
   m_nu   = mult_nu ( C_u ),   C_u = generic member of { P = u }
   m'_nu  = mult_nu ( C_v ),   C_v = generic member of { Q = v }
```

with the convention `m_ν = 0` if `C_u` does not pass through `ν`. In the total
transform basis `Pic(X) = <H, E_ν>`, `H² = 1`, `E_ν·E_μ = −δ`, `H·E_ν = 0`:

```text
   C_u ~ p·H - sum m_nu E_nu ,       C_v ~ q·H - sum m'_nu E_nu .
```

Three standard facts:

* **(F1)** `C_u² = 0` and `C_v² = 0`. Two generic members of a pencil are
  disjoint after the base locus is resolved; distinct fibres of `P` are
  disjoint in `C²` and the resolution separates them at infinity. Equivalently
  `Σ m_ν² = p²`, `Σ m'_ν² = q²` (Bézout + Noether).
* **(F2)** `C_u · C_v = N` where `N = #(C_u ∩ C_v)` in `C²` counted with
  multiplicity — the geometric degree of `(P,Q)` for generic `(u,v)`.
  Equivalently `Σ m_ν m'_ν = pq − N`: the Bézout defect **is** the intersection
  at infinity, and Noether's formula evaluates it on the cluster.
* **(F3)** The class `Δ := e·C_u − d·C_v` has `H`-component `ep − dq`.

### 1.2 The theorem

> **THEOREM ORTHO-DEFECT.** For any integers `d, e`,
> ```text
>       sum_nu ( e·m_nu - d·m'_nu )^2  =  (ep - dq)^2  +  2·d·e·N .
> ```
> In particular, under the GGV/Moh leading-form normalisation
> `l(P) = α H^d`, `l(Q) = β H^e`, `gcd(d,e) = 1`, `deg H = K`, `p = Kd`,
> `q = Ke` (so `ep = dq`):
> ```text
>       sum_nu ( e·m_nu - d·m'_nu )^2  =  2·d·e·N .            (ORTHO)
> ```
>
> *Proof.* `Δ² = e²C_u² − 2de·C_u·C_v + d²C_v² = −2deN` by (F1),(F2). Reading
> `Δ²` in the basis: `Δ = (ep−dq)H − Σ(e m_ν − d m'_ν)E_ν`, so
> `Δ² = (ep−dq)² − Σ(e m_ν − d m'_ν)²`. ∎

No Keller hypothesis, no `H2`, no irreducibility, no gauge. `(ORTHO)` is the
Cauchy–Schwarz/Hodge defect of the two pencils: `N = 0` iff the two multiplicity
vectors are exactly proportional in the ratio `d : e`, i.e. iff the two pencils
are the `d`-th and `e`-th "powers" of one common cluster. **`N` measures exactly
the failure of `(P,Q)` to be a power pair.**

### 1.3 The floor, and why it is monotone the right way

Every summand of `(ORTHO)` is `≥ 0`. Therefore, for any subset `S` of the
cluster whatsoever:

> **COROLLARY ORTHO-FLOOR.**
> `N ≥ [ Σ_{ν∈S}(e m_ν − d m'_ν)² − (ep−dq)² ] / (2de)`; under `ep = dq`,
> `N ≥ (1/2de) Σ_{ν∈S}(e m_ν − d m'_ν)²`.

This is the exact opposite monotonicity to `N-CEILING`. The packet's
`FILTER-INVERSION` argument reads: *"Unknown structure below δ_1 can only ADD
contact, which LOWERS N."* In `(ORTHO)` language: adding proportional structure
below `δ_1` adds `0`, and adding non-proportional structure adds a **positive**
amount, i.e. it **raises** `N`. Contact and multiplicity are the two halves of
`Σ m m' = pq − N`, and they move `N` in opposite directions. The campaign has
been reading only the half that goes down.

### 1.4 Two arithmetic corollaries that are free

`gcd(d,e) = 1` and `d ≥ 2` at any counterexample ((LF)+(MIN), integration #14).
`e m_ν − d m'_ν ≡ e m_ν (mod d)`, so it vanishes only if `d | m_ν`. Hence:

> **COROLLARY ORTHO-DIV.** `#{ ν : d ∤ m_ν } ≤ 2deN` and `#{ ν : e ∤ m'_ν } ≤ 2deN`.
> At all but `≤ 2deN` infinitely near base points at infinity, the generic
> `P`-fibre has multiplicity divisible by `d` and the generic `Q`-fibre has
> multiplicity divisible by `e`, in the coupled form `(m_ν, m'_ν) = (d t_ν, e t_ν)`.

> **COROLLARY ORTHO-SPLIT.** `#(cl(P) ∖ cl(Q)) ≤ 2dN/e` and
> `#(cl(Q) ∖ cl(P)) ≤ 2eN/d`. The two base clusters at infinity **coincide**
> except at `O(N)` points; in particular a point carried by one pencil and not
> the other costs `e²` or `d²` out of a budget of `2deN`.

Under `H2` (`N ≤ 16`), `ORTHO-DIV` reads: *at all but `32de` infinitely near
points, `d | m_ν`.* At `(K,d,e) = (36,2,3)` — the `(72,108)` shape — that is
`d | m_ν` at all but `192` points out of a cluster of size
`≤ 3p − 2 + 2g_L ≤ 228` (banked `g_L ≤ (N−1)/2`): tight enough to be a real
test, on data the census computes.

### 1.5 Controls (desk, exact)

I resolved three clusters by hand and computed `N` independently by machine
(`sympy`, `deg_x Res_y(P−u, Q−v)`; run time < 3 s; script text in §11).

| # | `(P, Q)` | `p,q` | `d,e` | cluster (hand) | `Σ(em−dm')²` (hand) | `(ep−dq)²+2deN` (machine `N`) |
|---|---|---|---|---|---|---|
| C1 | `(x, y)` | 1,1 | 1,1 | `{z_y, z_x}`, `m=(1,0)`, `m'=(0,1)` | `1+1 = 2` | `0 + 2·1 = 2` (`N=1`) ✓ |
| C2 | `(x, y²)` | 1,2 | 1,1 | `{z_x, z_y}`, `m=(0,1)`, `m'=(2,0)` | `4+1 = 5` | `1 + 2·2 = 5` (`N=2`) ✓ |
| C3 | `(y²+x, y³+(3/2)xy)` | 2,3 | 2,3 | 8 points, listed below | `36` | `0 + 12·3 = 36` (`N=3`) ✓ |

C3 in full (the informative one: `d=2, e=3`, `ep − dq = 0`, so it is exactly
`(ORTHO)`). Both curves meet `L_∞` only at `z_x = (1:0:0)`. `C_u` is smooth
there with tangent `L_∞`; `C_v` has two smooth branches, tangent to `L_∞` and to
`y = 0`. Resolving:

```text
   nu :        nu0   nu1   nu2   nu3  |  nu1'  nu2'  nu3'  nu4'
   m  (C_u):    1     1     1     1   |   0     0     0     0
   m' (C_v):    2     1     0     0   |   1     1     1     1
   3m - 2m':   -1     1     3     3   |  -2    -2    -2    -2
   squares :    1     1     9     9   |   4     4     4     4      total 36
```
Cross-checks inside C3: `Σm² = 4 = p²` ✓, `Σm'² = 9 = q²` ✓,
`Σ m m' = 2+1 = 3 = pq − N = 6 − 3` ✓, `Σ m_ν = 4 = 3p − 2 + 2g_L` with
`g_L = 0` (the fibre `y²+x=u` is `≅ A¹`) ✓. `ORTHO-SPLIT` check:
`#(cl(P)∖cl(Q)) = 2 ≤ 2dN/e = 4` ✓, `#(cl(Q)∖cl(P)) = 4 ≤ 2eN/d = 9` ✓.

Negative control: C2 has `ep ≠ dq` and the naive form `Σ(m−m')² = 2N` would
predict `4`, not the true `5`; the `(ep−dq)²` term is load-bearing and was not
fitted.

Two further machine rows (not hand-resolved, recorded as arithmetic only):
`(H²+y, H³+xy³)` and `(H²+xy, H³+y⁴)` with `H = y²−x²` (`K=2, d=2, e=3`,
`p=4, q=6`) both give `N = 16`, hence budget `192` — the low-contact regime,
included to show the identity is not tuned to high contact.

---

## 2. ORTHO-TOWER: the identity descends along Moh's own recursion

The single identity `(ORTHO)` is one equation. Moh's / GGV's reduction supplies
a whole ladder of them, and it lands on `OPEN[D1-SUBTREE]`.

Set `G_1 := β^d P^e − α^e Q^d`, so `deg G_1 = p_1 < Kde` (the leading forms
cancel; that cancellation is the whole GGV mechanism). Then:

> **LEMMA DESCENT-DEGREE.** `N(P, G_1) = d · N(P,Q)`, exactly.
>
> *Proof.* `(P, G_1) = Φ ∘ (P,Q)` with `Φ(u,v) = (u, β^d u^e − α^e v^d)`;
> `Φ` is dominant with `N(Φ) = d` (fix `u = a`, solve `v^d = (β^d a^e − b)/α^e`).
> Geometric degree is multiplicative on dominant generically-finite composites.
> Directly: `{P=u} ∩ {G_1=w} = ⋃_{j=1..d} ({P=u} ∩ {Q=v_j})`. ∎

`ORTHO-DEFECT` requires **nothing** of the pair beyond dominance — not Keller,
not the normalisation. So it applies to `(P, G_1)`, to `(Q, G_1)`, and to every
later stage `G_2, G_3, …` of the recursion, with the general form
`(e_r p_r − d_r q_r)² + 2 d_r e_r N_r` and `N_r` the product of the descent
multipliers times `N`.

> **THEOREM ORTHO-TOWER (statement; the per-stage evaluation is `OPEN`).**
> A degree-minimal counterexample carries `s` identities, `3 ≤ s ≤ log_2 K`
> (`DEPTH-LOG`), one per stage of Moh's recursion. Stage `r` gives
> `N ≥ L_r / (2 d_r e_r · c_r)` with `c_r` the accumulated descent multiplier
> and `L_r` the stage-`r` non-proportionality. Degrees fall along the tower
> while budgets grow by the multipliers, so the binding stage is not
> determined a priori — it must be computed.

Two things make this the right successor for the `d1-subtree` flagship:

1. Moh's recursion **ends** at `D_1` (`r = 1`: `#roots ≤ n/(n+m) < 1`, no `M_0`,
   `DETECTOR-NULL`). That last stage is exactly where the campaign has no
   published constraint — and it is the stage where the degrees are smallest,
   so its `ORTHO` budget `2 d_s e_s c_s N` is the smallest and its floor is the
   sharpest.
2. The lane's question ("does `[f,g] = 1` force a minimum contact deficiency?")
   becomes concrete: `(ORTHO)` **already** forces a minimum non-proportionality
   of exactly `2deN` in total. The lane's job is no longer to invent a floor but
   to compute how much of the `2deN` budget the sub-tree of `D_1` is obliged to
   consume, and whether the tower above it has already spent more.

---

## 3. Where the crossing would come from, honestly

`(ORTHO)` gives `N ≥ L/(2de)` with `L = Σ_S(e m_ν − d m'_ν)²`. It is a crossing
of Moh's floor iff `L` can be shown large. I state precisely what is and is not
established.

**Established (this report).** The identity, the monotone floor, `ORTHO-DIV`,
`ORTHO-SPLIT`, `DESCENT-DEGREE`, the three desk controls.

**Not established.** Any lower bound on `L` from the tree. I checked that pure
arithmetic will not supply one: at `(K,d,e) = (16,3,4)` (Moh's `(64,48)`
survivor, `2de = 24`) and `N = 4`, the system
`Σ_S Δ_ν = −2[e(1−g_L) − d(1−g'_L)]`, `Σ_S Δ_ν² = 96`,
`Σ_S m_ν Δ_ν = dN`, `Σ_S m'_ν Δ_ν = −eN` is **satisfiable**: e.g. 40 points with
`(m,m') = (1,1)` (`Δ = 1`) and 14 points with `(m,m') = (1,2)` (`Δ = −2`) gives
`ΣΔ = 12 = dN`, `ΣΔ² = 96 = 2deN`, `Σm'Δ = (4·12 − 96)/3 = −16 = −eN` ✓. So
`(ORTHO)` alone does not empty anything; the content has to come from the
proximity/tree structure of an actual cluster. That is the honest boundary of
the result, and it is also why the decisive move is computational (§11).

**What the campaign's own banked facts contribute.** `KELLER-PENCIL-GENUS`
proves `g_L ≤ (N − κ)/2 ≤ (N−1)/2` (Keller + `H2`). With the classical
`Σ_ν m_ν = 3p − 2 + 2g_L` (adjunction: `Σ m(m−1)/2 = (p−1)(p−2)/2 − g_L`,
`Σ m² = p²`; note every singularity of `C_u` is at infinity because `J = 1`
forces `dP ≠ 0` on `C²`), this says the `P`-cluster satisfies

```text
        sum m_nu  <=  3p + 12 ,        sum m_nu^2  =  p^2 .
```

An extremely peaked cluster. Cauchy–Schwarz on the tail gives
`max_ν m_ν ≥ p/3`, and the cluster has effectively `≈ 9` "mass points" of
multiplicity `≈ p/3` rather than `≈ p²` points of multiplicity 1. **This is the
regime where `ORTHO-DIV` bites**: `d | m_ν` at all but `≤ 32de` points, on a
cluster whose multiplicities are large and are generated by the Enriques
proximity relations `m_ν ≥ Σ_{μ → ν} m_μ` from the Puiseux characteristic of the
two points at infinity. Divisibility of an entire Euclidean multiplicity chain by
`d`, when the chain terminates with `gcd(d,e) = 1` data, is the shape of the
contradiction I would go after (§8).

---

## 4. Corrections and scope repairs to banked readings

**(4a) `THEOREM NO-CEILING` — scope repair, not refutation.**
`n-vs-mapdeg-opus5-20260902.md` §3.7 proves: a single class `Z = DH − Σa_iE_i`
constrained only by nefness, `Z² = N`, `Z·(effective) ≥ 0` and proximity does
not bound `D` at fixed `N`, because *"none is a negativity"*. Correct, and its
four-squares realisability argument is correct for one class. It does **not**
cover a **pair** `(C_u, C_v)` with `C_u² = C_v² = 0`, `C_u·C_v = N` and a fixed
rational ratio `p : q = d : e` of `H`-components, because that pair produces the
negativity `Δ = eC_u − dC_v`, `Δ·H = 0`, `Δ² = −2deN`, which is precisely the
missing ingredient. **Requested edit:** `NO-CEILING` should be restated as
`NO-CEILING[SINGLE-CLASS]`, and the sentence *"a ceiling must come from outside
the intersection theory of the resolution"* should be weakened to *"outside the
one-class ledger"*. I do not claim `NO-CEILING`'s conclusion is false — I claim
its hypothesis does not cover the two-class configuration, and the campaign has
been reading it as if it did (integration #14 §C, integration #16 §C both cite
it as the structural reason no ceiling exists).

**(4b) Integration #16 §C, the sentence
*"this lane shows why the boundary tree cannot [bound N below]: its free datum
(the sub-tree of D_1) only ever lowers N"*.** True for the contact functional,
false as stated for the boundary tree. Structure below `δ_1` that is
**proportional** leaves `N` unchanged; structure below `δ_1` that is
**non-proportional** raises `N` by `(e m − d m')²/2de` per point. The correct
statement is `UPPER-ONLY[CONTACT]`, not `UPPER-ONLY`.

**(4c) `NOETHER-K` is the one-vector specialisation.** `Σ a_i = 3D − 2N − κ +
n(W−S)`, `Σ a_i² = D² − N` is the net's base cluster with a **single**
multiplicity vector — the `p = q` reading. `(ORTHO)` is the two-vector statement
and is not derivable from it: `Σ a_i² = D² − N` is my `Σ m_ν m'_ν = pq − N` with
`m = m'`, which cannot hold when `d ≠ e`. Its `3D − 2N − κ + n(W−S)` and my
`3p − 2 + 2g_L` are consistent via `GENUS-DEFECT` + `MF-EXACT`; the cross-check
`2g_L − 2 = −2N − κ + n(W−S) + N − θ_inf` is the campaign's own and I did not
re-derive it.

**(4d) `FILTER-INVERSION` stands as stated for `N-CEILING`.** I am not
reopening it. `N ≤ 16` rejects no skeleton. `N ≥ L/2de` is a different filter
and rejects on the other side.

---

## 5. Disposition vector over the 46 APPROACHES rows (changes only)

Unlisted rows: **unchanged**. Reasons are all downstream of `(ORTHO)` unless
stated.

| row | title (short) | disposition | reason |
|---|---|---|---|
| 1 | GGV corner families + degree farm | **RAISE** (S:6 → 7) | `(72,108)` is `(K,d,e) = (36,2,3)`, the **minimum** `ORTHO` budget `2de = 12` among admissible degrees. The farm gains a two-sided per-family test, not only a cutoff; `ORTHO-TOWER` supplies the per-pair content the corner theory lacked. |
| 2 | Sheet-number ladder / Eggers–Wall / dicritical boundary trees | **RAISE to first rank** | This is where `(ORTHO)` lives. The row's standing gap ("no absolute/cofinal td ceiling") is exactly `UPPER-TO-FLOOR`; the multiplicity functional on the Enriques cluster is a boundary functional the ladder never carried. |
| 4 | Formal-germ certification / DEPTH-STAB | **RETYPE** | The germ lane's "modular nonempty ≠ germ" objection is untouched, but `(ORTHO)` gives a *numerical* obstruction computable before any germ is prolonged: a depth window whose `L` exceeds `2deU` cannot be prolonged. Use as a prefilter, not as a route. |
| 7 | Jelonek asymptotic variety `A(F)` | **RAISE** (from "partial") | In Moh's monic gauge `|x|` bounded ⟹ `|y|` bounded, so every escaping sequence has `x → ∞` and `A_F ⊆ {c_N(u,v) = 0}` with `c_N` the leading `x`-coefficient of `Res_y(P−u,Q−v)`; `deg_u c_N ≤ q`, `deg_v c_N ≤ p`, hence **`deg A_F ≤ p+q ≤ 2D`** in three lines, no compactification. Answers the row's standing objection for the *degree* of `A_F`. See `OPEN[AF-DEG-PIN]`. |
| 20 | mod-p / p-curvature formalism | **LOWER** for this question | Packet candidate (c). The only known bridge consumes `PC(2)`/`JC(4)`, both false (rows 11, 20 already record this). `p`-curvature is a statement about the *connection*, and nothing in it is graded by `N`. Keep as recon only. |
| 25 | Fiber monodromy / dessins / passports | **RETYPE** | The row's own gap is "single-cover passports ignore the second coordinate". `(ORTHO)` is precisely a two-coordinate coupling; the coupled branch-cycle CSP (the row's named successor) should be re-posed with the `ORTHO` budget as a constraint rather than as a free passport search. |
| 27 | Links at infinity / splice diagrams | **RAISE** (from "tried, template survives") | The splice diagram carries exactly the multiplicity data `(m_ν, m'_ν)`; the row died because "admissible ≠ realisable". `(ORTHO)` is an *admissibility* constraint the splice calculus never imposed, and it is cheap on a diagram. |
| 28 | Log surfaces / BMY / log-Kodaira | **RETYPE, keep low** | `E-BMY-VACUITY` killed the BMY arm. What survives of this row is the Hodge-index half, which is now `(ORTHO)`; the row should be re-labelled "Hodge index on the resolution" and its BMY content archived. |
| 33 | Global symplectic exactness / action residues | **LOWER** | Packet candidate (d)-adjacent. `KELLER-PENCIL-GENUS` already found the symplectic datum a wash (`UNIT-SPEED`); the flows' periods are `H_1` data of the fibre and `g_L ≤ (N−1)/2` already pins that side. |
| 36 | Guided counterexample search (SAT / sparse supports) | **RAISE** | The 418 pinned-`N=4` skeletons are the first structured targets this row has ever had, and `(ORTHO)` prunes them before any algebra: a skeleton needs `L = 8de` exactly at `N = 4`. |
| 39 | Cohomological cluster (K2, motivic, Hodge, anabelian) | **unchanged low, one note** | The row's demand ("refuse to start until a 10-line class is written") is met by `Δ = eC_u − dC_v` — but it is classical Hodge index, not a new cohomology, so the row stays where it is. |
| 44 | Moskowicz "no prime td" | **unchanged** | Already closed as proof input; `(ORTHO)` gives no repair. |

All other rows (3, 5, 6, 8–19, 21–24, 26, 29–32, 34, 35, 37, 38, 40–43, 45, 46):
**unchanged**, and I have no evidence to move them this round.

---

## 6. Disposition over candidates (a)–(f) and the deferred fronts

| candidate | disposition | reason |
|---|---|---|
| **(a)** Jacobian condition below `D_1` | **RAISE — first rank; redesign the lane's question** | It is the right place, but the lane is currently asked to *invent* a floor. `(ORTHO)`+`ORTHO-TOWER` hand it one: the total non-proportionality is *exactly* `2deN`, the tower above `D_1` has already spent some of it, and the question becomes "how much must the `D_1` sub-tree spend, and does the sum exceed `2de·U`?" This is a bounded arithmetic question on the same objects the lane already builds. |
| **(b)** Global non-boundary invariant (Chevalley–Weil, étale structure of `E`, pencil monodromy) | **LOWER** | The source-side étale structure of `E` and the monodromy of `H_1` of the generic member are both governed by `g_L`, and the campaign has already pinned `g_L ≤ (N−κ)/2` (Keller + `H2`) and shown `NO profile datum can bound g_L` from below. Chevalley–Weil computes the `ρ(G)`-module structure of `H_1` of a *cover* — it will return `g_L` and `θ_inf` again. This is `MF-EXACT` in a new alphabet. I would not staff it. |
| **(c)** Arithmetic / char `p` / `p`-curvature / point counts | **LOWER (keep as recon)** | See row 20. Additionally: `Mondello`'s lesson (row 19) is that char-`p` collisions do not lift, and point counts over `F_q` of the fibres return `N` mod `q`, not `N` versus `D`. No graded object connects the two. |
| **(d)** Dynamical / Hamiltonian flows | **LOWER** | `X_P, X_Q` are the same data as `dP ∧ dQ = dx ∧ dy`; completeness of the flows is equivalent to properness of `F` on the fibre, i.e. to `A_F = ∅`, i.e. to the conjecture. Periods are `H_1(C_u)`, i.e. `g_L`, already pinned. Circular. |
| **(e)** Analytic growth / Nevanlinna / Bernstein | **RETYPE, keep low** | Growth inequalities for `u ∘ F` bound the *covering number* above by the degree: `N ≤ (growth)`. That is the same direction the packet complains about. The one non-circular sub-item is a **Bernstein/BKK count with the Newton polygon at infinity**, which is `I_∞` again — i.e. `(ORTHO)`'s other half. |
| **(f)** A theorem that the boundary route is one-directional | **REFUTED as a program** | `(ORTHO)` is a boundary-tree functional that bounds `N` below. The correct residual negative statement is much narrower and I state it: **`UPPER-ONLY[CONTACT]` — no functional of the *contact* data alone bounds `N` below**, because contact enters `pq − N = Σ m m'` with the sign the packet identifies. That is worth banking as the precise form of `(f)`; the general form is false. |

**Deferred fronts.**

* **A2 / CELL-32** — **unchanged (deferred).** `PROFILE-UNTYPED`; nothing here
  moves it.
* **(B3) census at `N = 5,6`** — **unchanged (deferred).** Needs the general-`N`
  assembly theorem; `(ORTHO)` does not supply it.
* **Reducible branch (not-`H2`)** — **RAISE one notch.** `(ORTHO)` needs no
  irreducibility and no `H2`; `ORTHO-KILL` is unconditional. The reducible branch
  is currently the only place where the campaign has *no* `N`-window at all, and
  `ORTHO-FLOOR` gives it one for free (it is the only instrument in the record
  that does).
* **box01 Keller-cluster census** — **continue**, with the `ORTHO` invariant
  added as a fail-closed emitted field (§11).
* **`MOH-ENDGAME`** — **RAISE to second rank.** See §7; `(ORTHO)` is a
  per-survivor test, which is exactly what Moh lacked.

---

## 7. Reranked bottlenecks

**Proof side (was: the ceiling `D ≤ C(N)`).**

1. **`OPEN[ORTHO-SKELETON]` — evaluate `L(skel)` on the census.** Does a Moh
   skeleton determine enough of the common cluster to make
   `L = Σ_{ν∈skel}(e m_ν − d m'_ν)² > 0`, and how large? This is now the
   campaign's #1 bottleneck: it is a finite computation on an existing script,
   and its outcome is decisive either way (§11, card A).
2. **`OPEN[ORTHO-TAIL]` — the real theorem.** Prove
   `#{ν : d ∤ m_ν} > 2deN` for a degree-minimal counterexample, from the Enriques
   proximity relations plus `Σ m_ν = 3p−2+2g_L`, `Σ m_ν² = p²`, `g_L ≤ (N−1)/2`.
   This is the crossing (§8).
3. **`OPEN[D1-SUBTREE]`, redesigned** — the budget question of §2.
4. **`MOH-ENDGAME`** — with `ORTHO-KILL` as the per-survivor test, this is no
   longer a wall of bespoke arguments; it is one uniform inequality.
5. (demoted) any further one-directional ledger identity. The record has enough
   floors on `D`. Stop producing them.

**Disproof side (was: the `(B3)` cells / the `N = 4` realisation).**

1. **The 418 pinned-`N=4` skeletons, `ORTHO`-filtered.** At `N = 4` the budget
   is exactly `8de`; a skeleton whose visible `L` already exceeds `8de` is not a
   counterexample carrier, and a skeleton with `L` far below `8de` must have the
   whole deficit hidden below `D_1` — which pins where to look.
2. **Minimum-budget shape first.** At each admissible degree pick `(K,d,e)`
   minimising `2de`: `D = 105` → `(35,2,3)`, `2de = 12`; `D = 108` → `(36,2,3)`,
   `2de = 12` (**= the historical `(72,108)`**); `D = 112` → `(28,2,4)` is
   excluded by `gcd`, so `(16,2,7)`, `2de = 28`; `D = 117` → `(39,2,3)`,
   `2de = 12`; `D = 120` → `(40,2,3)`, `2de = 12`. **I would try to realise
   `(deg P, deg Q) = (72,108)`**, i.e. `K = 36, d = 2, e = 3`, `N = 4`, budget
   `Σ Δ² = 48`. Reasons: smallest budget ⟹ most rigid cluster ⟹ smallest search
   space; it is the campaign's own origin family with external
   certificate-support machinery already built (row 1); and `d = 2` makes
   `ORTHO-DIV` maximally sharp (*even* multiplicities everywhere but 48 points).
3. box01 cluster census (continue as is).

---

## 8. Strongest proof attack

**Target: `ORTHO-TAIL`.** Show that a degree-minimal Keller counterexample must
spend more than `2deN` on non-proportionality, i.e. `L_total > 2deN`, which is a
contradiction with `(ORTHO)`.

The attack, in the order I would run it:

**Step 1 (banked inputs).** `J = 1` ⟹ `dP ≠ 0` on `C²` ⟹ every singularity of
`C_u` is at infinity ⟹ `Σ_ν m_ν(m_ν−1)/2 = (p−1)(p−2)/2 − g_L` and
`Σ_ν m_ν² = p²`, hence `Σ_ν m_ν = 3p − 2 + 2g_L`. With
`g_L ≤ (N−κ)/2 ≤ (N−1)/2` (`KELLER-PENCIL-GENUS`, Keller + `H2`),
`Σ m_ν ≤ 3p + 12`. The same for `Q`: `Σ m'_ν ≤ 3q + 12`.

**Step 2 (the cluster is short and heavy).** From `Σm = 3p + O(1)`,
`Σm² = p²`: `max_ν m_ν ≥ p/3` (if `m_1 = αp` then
`p²(1−α²) = Σ_{≥2}m² ≤ m_1 Σ_{≥2} m ≤ αp·p(3−α)` forces `α ≥ 1/3`), and
iterating, the cluster is a short Enriques chain with `O(1)` heavy points, not a
long tail of `1`s. The heavy points are the free/satellite vertices of the two
Puiseux characteristics at the (exactly two, by `NU-TWO`) points at infinity.

**Step 3 (the divisibility obstruction).** `ORTHO-DIV` demands `d | m_ν` at all
but `≤ 2deN ≤ 32de` points, **coupled** with `e | m'_ν` at the same points and
`m'_ν/m_ν = e/d` there. On an Enriques chain the multiplicities are produced by
the Euclidean algorithm on the characteristic pair `(M_r, V_r)`; the chain ends
with `m = 1` at every free point immediately below a dicritical. **`d | 1` is
false for `d ≥ 2`.** So each such terminal free point costs at least
`min_k |e − dk|² ≥ 1`, each cluster point carried by one pencil only costs
`d²` or `e²` (`ORTHO-SPLIT`), and each point where the two characteristics
disagree costs the square of the disagreement. The theorem to prove is that the
number of terminal free points plus the split points exceeds `2deN`.

**Step 4 (where it can fail, stated in advance).** The escape route is: make
*both* pencils dicritical at the *same* divisors with degrees in ratio `d : e`
(so `Δ_ν = 0` at the terminal points too) and keep the two characteristics
proportional all the way down — i.e. "`P` and `Q` are the `d`-th and `e`-th
powers of one pencil at infinity", which `N > 0` forbids globally but not
obviously pointwise. **`ORTHO-TAIL` is the statement that the local escape
cannot be arranged everywhere at once.** It is a statement about clusters, not
about Keller maps, so it is checkable on synthetic clusters before any theory is
written.

**Cheapest discriminator:** synthesise clusters. Enumerate Enriques chains with
`Σ m² = p²`, `Σ m = 3p − 2 + 2g_L`, `g_L ≤ 7`, `p = Kd`, satisfying the
proximity inequalities, and ask whether any admits a partner chain with
`Σ m'² = q²`, `Σ m m' = pq − N`, `N ≤ 16`. If none does at `(72,108)`, the
`(72,108)` family is dead by a two-page argument. This is a small search.

---

## 9. Strongest counterexample attack

**Realise `(72,108)` at `N = 4` with the `ORTHO` budget as the design
constraint.**

The counterexample side has never had a finite target. It now has two nested
ones: the 418 pinned-`N=4` skeletons at `D ∈ [101,200]`, and inside them the
`ORTHO` budget `Σ_ν(3m_ν − 2m'_ν)² = 48` at `(K,d,e) = (36,2,3)`, `N = 4`.

Procedure:
1. From the census, take every `D = 108` skeleton with `U ≥ 4` (the
   `N`-window contains 4).
2. Compute the visible `L`. Discard `L > 48` (`ORTHO-KILL`, unconditional).
   Record `48 − L` as the **deficit that the sub-tree of `D_1` must supply
   exactly**. This is a *positive* design specification, not a filter: it tells
   the realiser what the unknown part of the tree has to look like.
3. Enumerate cluster completions realising the deficit (a small integer
   partition problem: write `48 − L` as `Σ(3m − 2m')²` over an Enriques chain
   with the residual `Σm²`, `Σm'²`, `Σmm'` budgets).
4. For each completion, attempt the algebraic realisation with the existing
   `keller_cluster_census.py` / GGV corner machinery; `J = 1` is imposed last.

Interpretation: uniform failure at step 4 is a theorem (`(72,108)` empty at
`N = 4`); survival at step 4 is a counterexample. Either is resolution-grade for
one family. **Second target if `(72,108)` empties:** `D = 117`, `(39,2,3)`,
budget `48`; then `D = 105`, `(35,2,3)`.

---

## 10. New cross-connections

**(X1) `ORTHO` ↔ `KELLER-PENCIL-GENUS`.** The linear moment of `(ORTHO)` is
```text
     sum_nu ( e m_nu - d m'_nu )  =  -2 [ e (1 - g_L) - d (1 - g'_L) ] ,
```
from `Σ m_ν = 3p−2+2g_L` and `Σ m'_ν = 3q−2+2g'_L` with `ep = dq`. Combined with
`Σ|Δ_ν| ≤ Σ Δ_ν² = 2deN` this gives
**`d e N ≥ | e g_L − d g'_L − (e − d) |`** — a genus-driven floor on `N`. With
the campaign's `g_L ≤ (N−1)/2` it is currently slack, but it is the first
identity linking the genera of the **two** pencils, and `g'_L` (the genus of the
generic `Q`-fibre) has never been priced separately from `g_L`. **New bounded
open:** `OPEN[GPRIME-PIN]`.

**(X2) `ORTHO-TOWER` ↔ `DEPTH-LOG` ↔ `D1-SUBTREE`.** `DEPTH-LOG` says the number
of Moh stages is `3 ≤ s ≤ log_2 K` and the *sizes* are free. `(ORTHO)` prices
each stage: stage `r` costs `2 d_r e_r c_r N`. So the depth **count** bound and
the free **size** are now coupled by a budget, which is what integration #15 §D
was looking for and did not find. The `log_2 K` bound stops being a curiosity
and becomes "at most `log_2 K` budget draws against a total of `2deN`".

**(X3) `ORTHO-SPLIT` ↔ `PLACE-LEDGER` / `MERIDIAN-FLOOR`.** `PLACE-LEDGER`'s
`N = Σ_γ m_γ` over the places of a generic member is the *dicritical* form of
`C_u · Φ_Q`; `ORTHO-SPLIT` is the *cluster* form. They are the same identity read
on two bases (geometric exceptional curves vs. total transforms). The
consequence is new: `#(cl(P) ∆ cl(Q)) ≤ 2N(d/e + e/d)`, i.e. **the two pencils
must be resolved by nearly the same sequence of blowups**. `MERIDIAN-FLOOR`'s
`W` and `S` are counts on one side; this couples them.

**(X4) `A_F ⊆ {c_N = 0}` ↔ row 7 ↔ the monic gauge.** In Moh's gauge the
non-properness set is cut out by the leading `x`-coefficient of the `y`-resultant,
giving `deg A_F ≤ p + q` in three lines. `DEG-AF-VS-N` asks for the invariant
`δ_aff = #gaps`; this gives the *degree* directly and cheaply. It should be
cross-checked against `MERIDIAN-FLOOR+`'s `n = deg Ā_F` (`n ≥ ⌈(N−1)/(W−S)⌉+1`):
a floor and a ceiling on the same integer, from two independent routes. **That
pair is itself a two-sided window and I did not see it stated anywhere in the
record.**

**(X5) `(72,108)` is the minimum-budget shape.** Row 1's origin family is
`(K,d,e) = (36,2,3)`, the `2de`-minimiser. The campaign's oldest target and the
new instrument's sharpest cell are the same object. That is either a coincidence
or a reason the family has resisted for so long; either way it says where to
point the instrument first.

---

## 11. Decisive experiment / software acceleration

**`ortho_defect()` inside `box/moh_skeleton_N.py`.** The script already carries
(a) exact Puiseux roots at `t = 1/x` (`PART 0`), (b) Moh's tower recursion with
`Skel(M_r, V_r)` (`PART 3`), (c) the `D ≤ 400` census (`PART 4`), (d) the `U`
filter (`PART 5`). The missing 60 lines are:

```text
   multiplicity_sequence(branch)  # Euclidean algorithm on the char. pairs
   common_cluster(f_branches, g_branches)   # merge by contact order
   ortho_defect(skel) -> (L, 2*d*e*U, verdict)
```
`L := Σ_{ν ∈ visible cluster} (e·m_ν − d·m'_ν)²`; emit `N_lo = ceil(L/(2de))`
alongside the existing `N_hi = U`; verdict `KILL` iff `N_lo > N_hi`.

**Controls to ship with it (fail-closed, all three exact and already verified by
hand in §1.5):**
```text
   C1  (x,   y   ), d=e=1  ->  L = 2   and  (ep-dq)^2 + 2deN = 2
   C2  (x,   y^2 ), d=e=1  ->  L = 5   and  (ep-dq)^2 + 2deN = 5
   C3  (y^2+x, y^3+3/2 xy), d=2,e=3 -> L = 36 and 2deN = 36  (8-point cluster)
```
Negative control: assert that dropping the `(ep−dq)²` term makes C2 predict `4`
and the control FAILS (guards against the term being silently dropped when the
gauge is not normalised).

Machine script used for the `N` column (desk, `sympy`, < 3 s, < 100 MB):
```python
import sympy as sp
x,y,u,v = sp.symbols('x y u v')
def geom_degree(P,Q):
    R = sp.resultant(sp.expand(P-u), sp.expand(Q-v), y)
    return sp.Poly(sp.expand(R), x).degree()
# (x,y)->1 ; (x,y^2)->2 ; (y^2+x, y^3+3/2*x*y)->3 ; (H^2+y,H^3+x*y^3)->16, H=y^2-x^2
```
Observed: `1, 2, 3, 16, 16`, matching the hand-resolved clusters on the first
three rows.

**Expected information gain.** One run over the `D ∈ [101,200]` census (116,385
groups; the existing `D ≤ 400` pass is 161 s on one core, so this is minutes)
returns, for the first time, a **two-sided** window `[N_lo, N_hi]` per skeleton.
Three outcomes, all decisive:
* some `N_lo > N_hi` ⟹ **unconditional kills**, the first ever from the boundary;
* all `N_lo = 0` ⟹ the visible skeleton is exactly proportional, which is itself
  a theorem (`UPPER-ONLY` promoted in its correct, narrow form) and redirects
  the whole effort to the `D_1` sub-tree with a *quantified* deficit `2deN`;
* `0 < N_lo ≤ N_hi` ⟹ the windows tighten and the pinned-`N=4` list shrinks,
  handing the realisation lane a smaller finite target.

**Stop condition:** if the visible cluster of every census skeleton is exactly
proportional (`L ≡ 0`), stop the boundary program at this instrument and go to
`ORTHO-TOWER` stage `s` only.

---

## 12. Campaign-systems check — **UPGRADE**

**Finding.** The failure this round is a **typing** failure the lint could have
caught. `N-CEILING`, `MERIDIAN-FLOOR`, `HARMONIC-BOUND`, `DEG-SPLIT`,
`MOH-FLOOR` are each one-directional; the record then generalised to "the
boundary route is one-directional" — a quantifier slip over *all* boundary
functionals — without recording which functional and which free variable the
monotonicity was checked in. `NO-CEILING[SINGLE-CLASS]` was cited as the license
for the slip while being about one class only (§4a).

**Smallest useful test.** Add to `ops/` (and to `PREFLIGHT`) a lint rule:

```text
   RULE MONOTONE-TYPING.  Any report asserting a directionality claim
   ("bounds X above only", "one-directional", "no ceiling") must emit
       monotone_basis = {"functional": <name>,
                         "variable":   <the datum that is free>,
                         "sign":       "+" | "-",
                         "scope":      "this functional" | "all functionals of <class>",
                         "witness":    <path:line of the sign computation>}
   and FAIL-CLOSED if scope = "all functionals of <class>" without a
   proof object for the universal quantifier.
```

This is the direct analogue of the existing `charge_basis` line for exit claims
in `FALLACY-v2.md`: it forces a declared, not inferred, direction. Cost: one
emitted field; it would have flagged integration #16 §C's `UPPER-ONLY` sentence
and integration #14 §C's `NO-CEILING` citation on the day they were written.

**Second, smaller:** census scripts should emit *both* bounds of any window they
compute. `OPEN[UPPER-TO-FLOOR]` is itself stated correctly (`N ∈ [2,16]`), but
every lane downstream of it emitted only `N_hi`.

---

## 13. Idea cards

### Card A — `ORTHO-SKELETON`: evaluate the floor on the existing census

* **Claim to test.** `L(skel) = Σ_{ν ∈ visible}(e m_ν − d m'_ν)² > 0` for Moh
  skeletons, and `L/(2de) > U` for some of them.
* **Dependencies.** `box/moh_skeleton_N.py` (`Skel`, Puiseux `PART 0`);
  `N-CEILING` (`U`); `NU-TWO` (two points at infinity); (LF)/(MIN) (`d ≥ 2`,
  `gcd(d,e)=1`). No `H2`, no `Z(G)=1`, no CAS beyond integer arithmetic.
* **Cheapest discriminator.** Run on Moh's four survivors first
  (`(64,48) = 16·(4,3)`, `2de = 24`, `U_tower ∈ {9,6,10.5,12,8,16}`). Six numbers.
  If any `L > 2de·U` there, the survivors die immediately and the campaign is
  through Moh's wall.
* **Outcomes.** `L > 2deU` ⟹ unconditional kill (report as a theorem, request
  hostile review by a different model). `0 < L ≤ 2deU` ⟹ two-sided windows;
  re-run the `[101,200]` census and republish the pinned list. `L ≡ 0` ⟹
  promote `UPPER-ONLY[CONTACT]` in its narrow form and move all weight to
  `ORTHO-TOWER`/`D1-SUBTREE`.
* **Stop condition.** `L ≡ 0` on all 3.87M `D ≤ 400` groups.
* **Expected information gain.** High and certain: three mutually exclusive
  outcomes, each redirecting the campaign. Cost: one seat, ~2 h, desk-scale.

### Card B — `ORTHO-TOWER`: the budget along Moh's descent

* **Claim to test.** With `G_1 = β^dP^e − α^eQ^d`, `N(P,G_1) = dN` (proved
  above), `(ORTHO)` at stage `r` gives `N ≥ L_r/(2 d_r e_r c_r)`; the binding
  stage is the last, below `D_1`.
* **Dependencies.** `DEPTH-LOG` (`3 ≤ s ≤ log_2 K`); `DETECTOR-NULL` (minor
  discs contribute zero to `N`, so the stage-`r` clusters are the major towers);
  the `d1-subtree` lane's current output.
* **Cheapest discriminator.** Compute `(p_r, q_r, d_r, e_r, c_r)` for the four
  Moh survivors, `s` stages each — at most `5·4 = 20` rows of integer data — and
  print `Σ_r` of the stage budgets against `2deN`. A stage whose *forced*
  non-proportionality already exceeds its budget kills the survivor.
* **Outcomes.** A binding stage ⟹ the `D_1` lane gets a target number.
  All stages slack ⟹ `ORTHO` is a one-shot instrument, use Card A only.
* **Stop condition.** All stage budgets slack by more than a factor 2 on all
  four survivors.
* **Risk, stated.** `deg G_1` and the leading form of `G_1` need GGV §4/§7 to
  stay in the normalised shape; if the shape breaks, the general
  `(e_rp_r − d_rq_r)²` form still applies but the budgets are looser.

### Card C — realise `(72,108)` at `N = 4` under the budget `ΣΔ² = 48`

* **Claim to test.** Is there a cluster pair at `(K,d,e) = (36,2,3)` with
  `Σ m² = 72²`, `Σ m'² = 108²`, `Σ m m' = 72·108 − 4`, `Σ(3m − 2m')² = 48`,
  satisfying the Enriques proximity inequalities at exactly two points at
  infinity, with `g_L, g'_L ≤ 1`?
* **Dependencies.** `keller_cluster_census.py`; `NU-TWO`; `FIRST-FORK`
  (`ν(F_min) = 2`, `E_0` free) — which fixes the top of the tree, so the search
  starts one level down.
* **Cheapest discriminator.** The integer-partition feasibility of step 3 in §9,
  before any polynomial is written. `48` is small; the partitions of `48` into
  squares of the residues `3m − 2m'` (all `≡ m mod 2` constrained) is a
  minutes-long enumeration.
* **Outcomes.** Infeasible ⟹ `(72,108)` is empty at `N = 4`, a real theorem
  about the campaign's origin family. Feasible ⟹ a short list of cluster designs
  to hand to the realisation lane; each design is a *specification* of the
  Puiseux data of a putative counterexample, which is more than the campaign has
  ever had on the disproof side.
* **Stop condition.** More than `10^4` feasible designs (then the budget is not
  restrictive at this degree and the card is not decisive).

---

## 14. Current lanes — continue / redesign / stop

| lane | verdict | note |
|---|---|---|
| `d1-subtree-opus5` (flagship) | **REDESIGN, keep the seat** | Its question ("does `[f,g]=1` force a minimum contact deficiency below `D_1`?") is the right target read through the wrong functional. Re-charge it with `(ORTHO)`: the total non-proportionality is *exactly* `2deN`; ask how much the `D_1` sub-tree must consume. Same objects, same person, two-sided question. |
| `n-on-the-tree-review-grok46` | **complete — no change** | All items confirmed; nothing here is disturbed. `FILTER-INVERSION` stands for `N-CEILING`. |
| box01 Keller-cluster census (975 cells) | **CONTINUE**, with one addition | Emit the `ORTHO` fields (`L`, `2de`, `N_lo`) per cell. The interim result (zero clusters at `N=2,3`; clusters from `D=8` at `N=4`) is exactly the regime where `ORTHO-FLOOR` is testable against ground truth — use those cells as *positive* controls for Card A's implementation before trusting it at `D ≥ 101`. |
| Box03 | **stopped — no change** | |
| A2 / CELL-32 | **stay deferred** | `PROFILE-UNTYPED`; `(ORTHO)` does not type it. |
| `(B3)` census at `N = 5,6` | **stay deferred** | Needs the general-`N` assembly theorem. |

---

## 15. OPENs raised, with bounded quantities

* **`OPEN[ORTHO-SKELETON]`** — the integer `L(skel) = Σ_{ν ∈ visible cluster}
  (e m_ν − d m'_ν)²`, bounded in `[0, 2de·U(skel)]` (upper bound by `(ORTHO)`
  plus `N-CEILING`; `U` is finite on every census skeleton, `≤ 44` at the
  `MOH-SHARP-2` degrees). Decides Card A.
* **`OPEN[ORTHO-TAIL]`** — the integer `#{ν : d ∤ m_ν}`, bounded in
  `[1, 2deN] ⊆ [1, 32de]` under `H2` (lower bound `≥ 1` because `N ≥ 2` by
  Ax–Grothendieck forces `Δ ≠ 0`). The crossing statement is that this integer
  exceeds `2deN`.
* **`OPEN[ORTHO-TOWER]`** — the integer `s` of Moh stages, bounded in
  `[3, ⌊log_2 K⌋]` (`DEPTH-LOG`), together with the `s` stage floors
  `⌈L_r/(2 d_r e_r c_r)⌉`, each bounded in `[0, 16]` under `H2`.
* **`OPEN[GPRIME-PIN]`** — the integer `g'_L` (geometric genus of the generic
  `Q`-fibre), bounded in `[0, (q−1)(q−2)/2]` unconditionally and conjecturally in
  `[0, (N−κ')/2] ⊆ [0,7]` by the `KELLER-PENCIL-GENUS` argument applied to the
  second pencil — which has not been checked for that pencil.
* **`OPEN[AF-DEG-PIN]`** — the integer `deg A_F`, bounded in `[1, p + q]` by the
  `c_N` argument (§5, row 7) and below by `MERIDIAN-FLOOR+`
  (`n ≥ ⌈(N−1)/(W−S)⌉ + 1`). Two-sided; cheap.

Carried unchanged: `OPEN[UPPER-TO-FLOOR]` (now with a candidate answer),
`OPEN[D1-SUBTREE]`, `OPEN[U-GT-2-ALL-D]`, `OPEN[DELTA75-BRACKET]`,
`OPEN[MOH-14]`, `MOH-ENDGAME`, `NONPROPER-DEGREE`, `ANTICANON-DEFECT`,
`SAT-MASS`, `DELTA-AFF-VS-N`.

---

## 16. Direct answer to the packet's second question

*"Given that the depth COUNT is log-bounded and the SIZE is free, is 'the
ceiling' even the right target?"*

**Yes, but not as a ceiling on `D`.** `D ≤ C(N)` and `N ≥ f(D)` are the same
crossing, but only the second has an instrument. Do not staff a search for a
ceiling on `D`. Rank order for the next seats: **Card A** → `d1-subtree`
redesigned (**Card B**) → `MOH-ENDGAME` re-posed as one uniform inequality →
**Card C**. The reducible branch gains an `N`-window for free (`ORTHO` needs no
`H2`) and is worth one seat to record it. `(b)`–`(e)` should not be staffed:
each returns a datum the campaign has already priced, and the record says so.

---

## 17. Typed block

```text
SUBMISSION   ideation 20260902T1608Z (Opus 5), basis 7f7c0306768d
VERDICT      the one-directionality reading is WRONG.  It is correct for the
             CONTACT functional and was over-generalised to all boundary
             functionals; NO-CEILING was cited as the license and is a
             SINGLE-CLASS theorem.
NEW          THEOREM ORTHO-DEFECT   sum (e m_nu - d m'_nu)^2 = (ep-dq)^2 + 2deN
             COROLLARY ORTHO-FLOOR  N >= (1/2de) sum_{S}(e m_nu - d m'_nu)^2
                                    for EVERY subset S of the cluster
             COROLLARY ORTHO-DIV    #{nu : d does not divide m_nu} <= 2deN
             COROLLARY ORTHO-SPLIT  #(cl(P) symm-diff cl(Q)) <= 2N(d/e + e/d)
             LEMMA DESCENT-DEGREE   N(P, beta^d P^e - alpha^e Q^d) = d N
             ORTHO-TOWER            s floors, 3 <= s <= log_2 K, last one below D_1
             AF-DEGREE              A_F subset {c_N = 0}, deg A_F <= p + q
CONTROLS     three clusters resolved by hand (2, 5, 36) against machine-computed
             N (1, 2, 3) by resultant; negative control on the (ep-dq)^2 term.
NOT CLAIMED  any lower bound on L from the tree; any kill; any ceiling on D;
             that ORTHO alone empties anything (an explicit satisfiable
             arithmetic solution at (64,48), N=4 is exhibited in sec.3).
SCOPE        ORTHO-DEFECT needs NO Keller, NO H2, NO irreducibility, NO gauge.
             The corollaries using d >= 2 / gcd(d,e)=1 need (LF)+(MIN).
             The g_L <= (N-1)/2 input is Keller + H2 (KELLER-PENCIL-GENUS).
CORRECTIONS  NO-CEILING -> NO-CEILING[SINGLE-CLASS];
             INT#16 sec.C "UPPER-ONLY" -> "UPPER-ONLY[CONTACT]";
             NOETHER-K is the p=q one-vector specialisation of ORTHO's
             mixed moment.
LANES        d1-subtree REDESIGN (keep seat); box01 CONTINUE + emit ORTHO;
             n-on-the-tree-review no change; Box03 stopped; A2 / (B3) deferred.
SYSTEMS      UPGRADE: RULE MONOTONE-TYPING, fail-closed on universal
             directionality claims.
NEXT         Card A on Moh's four survivors: six integers decide it.
DISCLOSURE   (1) SIZE: body ~45 KB against the charged 25-40 KB band; the
                 overrun is sec.1 (the identity with its full hand-resolved
                 8-point control) and sec.5-6 (the two required disposition
                 vectors in full).  Nothing was compressed out of the contract.
             (2) The cluster resolutions in sec.1.5 are DESK computations, not
                 machine-verified; only the N column is machine-computed.
                 The multiplicity_sequence / common_cluster code of sec.11 does
                 NOT exist yet - it is the proposed acceleration, not a result.
             (3) sec.3 states explicitly that ORTHO alone is satisfiable at the
                 counterexample parameters; no emptiness is asserted anywhere.
             (4) One accidental one-line exposure to a sibling submission file
                 is disclosed in the header; it was a citation list.
             (5) No AWS job submitted; total desk compute < 10 s, < 200 MB.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `48645`.
- Body SHA-256:
  `0916a85a7a8090d04461fa356518fb2ffd877374d1b8452a2b808d6f77156934`.
- Frozen basis: `7f7c0306768dd6393e9a8dd161d594df9f14c8d0`.
- Charged input: `xmodel/ideation-20260902T1608Z-packet.md`, SHA-256
  `ab66bd6b87dc035740325c309349ec8d52a5963b6b1a0a6e0e53a34f74715af3`.
