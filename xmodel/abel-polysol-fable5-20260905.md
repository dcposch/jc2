# UNIFORM lane: (UF) is an Abel equation of the SECOND kind; the polynomial-solution finiteness theory yields no uniform-in-t statement; the exact structure that survives (two singular points, a universal Briot–Bouquet recursion, the monomial stratum in closed form)

Lane: `abel-polysol-fable5-20260905`. Fable 5.1. 2026-09-05.

**VERDICT: NO uniform-in-t statement follows from the theory of polynomial solutions of polynomial ODEs. (R) is not proved; theorem (T) is not promoted for any new index. (UF) is classified exactly (an Abel equation of the second kind in P, first kind only in 1/P), every derived identity is verified by exact computation, and the (UF)-based row emitter reproduces Astra's frozen t=3,4,5 rows and the t=3,4 exact conclusions.**

```text
REQUESTED  (1) standard form of (UF) and the unknown the finiteness theory must bound;  (2) apply the
           Cima–Gasull–Mañosas / Gasull–Torregrosa–Zhang / Bautin–Briskin–Françoise–Yomdin / Malmquist–Rainville
           results and decide whether a uniform bound is incompatible with deg V = 2t−1;  (3) combine a count with the
           marked jets and the weight grading;  (4) otherwise deliver the exact classification, the precise obstruction
           and the best finite-t instrument;  verify at t=3,4 against the frozen certificates.
ANSWER     (1) After solving for the highest derivative, (UF) is the Abel equation of the SECOND kind
               P P' = (3/(2x)) P^2 + ((Bx − (3/2)L(L+b))/(2x)) P + Rfree/(2x),           [§2, identity (I4)]
               equivalently (θ−3)(P^2) + G P = Rfree with θ = x d/dx, G = (3/2)L(L+b) − Bx  [Euler form (I3)];
               it is of the FIRST kind only in z = 1/P (A3 = −Rfree/(2x), A2 = G/(2x), A1 = −3/(2x), A0 = 0),
               where a polynomial P is a RATIONAL solution; in V it is (2P)V' = (quadratic in V), the general
               second-kind shape (g1 V + g0)V' = f2 V^2 + f1 V + f0 with g1 = 2x^3.  It is not Bernoulli, not Riccati.
               The unknown to bound is P (degree exactly 2N = 2t+2, equivalently V of degree 2t−1), but the
               "coefficient" polynomial L (degree N = t+1, with N−1 free coefficients) is ALSO unknown: (UF) is one
               identity in two unknown polynomials, 3t+1 scalars against 4t equations.
           (2) NONE of the cited results gives a uniform bound, and none is incompatible with deg V = 2t−1.
               Degree comparison forces deg P = 2·deg L exactly and the top identity (UT), whose discriminant is 3N:
               that step is the SOURCE of the field Q(√(3(t+1))), not a contradiction.  The counting theorems live on
               first-kind equations with FIXED polynomial coefficients (their mechanism: polynomial solutions differ by
               constants); for the second kind that mechanism fails, and here the coefficients vary with L.  Worse,
               for fixed (L, field factor) the polynomial P is UNIQUE (all pivots at x = ∞ are units, closed form
               λ(m) = 2ω(2N+m+6d)), so any bound on the NUMBER of solutions is vacuous: the residual is about WHICH L
               admit a P.  The Bautin/moment machinery needs a fixed parameter space; here it grows with t.
           (3) The weight grading is exactly the x-Euler operator and is already consumed by U ≅ G_m × X; it forces
               nothing beyond that.  The monomial stratum c = 0 always has B = η = 0 and solves (UF) iff
               e(N,d) = −3(d+1)(6d²−1)²(9d³+8d²−1) / (d²(2d+1)(3d+1)²(3d+2)²) = 0, i.e. iff (N,d) = (3,−1):
               Astra's exceptional t=2 family, and nothing else for any t ≥ 3 (closed form, §5).
           (4) Precise obstruction: the E_k are the consistency conditions of a unit-pivot recursion at x = ∞
               (Theorem H) — equivalently the truncation conditions Φ_{2N+1} = … = Φ_{4N} = 0 of a t-INDEPENDENT
               universal Briot–Bouquet recursion at x = 0 (pivots −(k−3)b²/2, resonance k = 3, §4).  A uniform proof
               must show a growing family of such conditions has no common zero off Bη = 0; no ODE theorem does that.
               Best finite-t instrument: Theorem H rows + the weight-graded Macaulay certificate for (Bη)^n (§6);
               the bottom-up recursion is validated (unit at t=3 exact/modular, t=4 modular) but is more expensive.
CUSTODY    (UF)-emitter (built from P·Hdiff − Rfree, not from eq. (1)) reproduces the frozen rows, B, η, target
           at t = 3, 4, 5 exactly; exact std: t=3 dim 0 vdim 66, t=4 dim 0 vdim 338, T ∉ J, T² ∈ J at both;
           t=5 modular control p=31991: dim 0, vdim 1709, T² ∈ J mod p (Astra's exact t=5 conclusion is consumed).
NOTIFY     not warranted (no new index closed, no exit claim; charge_basis declaration inapplicable).
```

## 1. Custody

The receipt `xmodel/abel-polysol-fable5-20260905.run.v2` was parsed with `awk -F=`, pairing `charged_input_<i>_sha256=`
with `_basename=` into `box/abel-polysol-20260905/manifest.sha256`; `sha256sum -c` returned **4/4 OK**
(`manifest.check.log`). No digest was retyped.
All four charged inputs were read from `/tmp/jc2-lane.LxxlVg/inputs` before any driver ran. The (RC1)–(RC2) identity
is consumed as restated in the charged Astra report §7.1 (`k16-xempty-astra-20260905.md`); the uncharged
`k16-f3abel-astra-20260905.md` was opened only to confirm its printed (RC1) line and is not otherwise used. The frozen certificates replayed are `box/k16xempty-20260905/controls_t{3,4,5}_raw.sing` and
`controls_t3_emit.log` (byte-unchanged; embedded with identifiers renamed only).
No ledger, jc2-lean, or ideation file was edited or written. All drivers and outputs are in `box/abel-polysol-20260905/`.

## 2. Task (1): (UF) in standard form, and what has to be bounded

Notation as in the charged §7.1: N = t+1, q = 2N−1, L = K/y = x²C/y − b (deg N, lc 1/y, L'(0) = 0, L(0) = −b),
P = xW − b²/4 (deg 2N, lc ω), Hdiff = 2xP' − 3P − Bx + (3/2)L(L+b),
Rfree = (3/16)L²(L(L+2b) − 4Bx) − ηx²(bL/2 + Bx). (UF) is P·Hdiff = Rfree, with jets (UJ) P(0) = −b²/4, P'(0) = −B,
P''(0) = 2η and normalisation (UL).

**Verified identities** (`uf_verify.py`, W, W', C, b, B, η, x, 1/y independent symbols; `uf_verify.json`):

```text
(I1)  x²·F = P·Hdiff − Rfree                       F = the charged polynomial of eq. (1)      → 0
(I2)  Rfree = 3K²Q/(16y⁴) − ηx²J                  (RC1) with K = yL, Q = y²(L(L+2b)−4Bx), J = bL/2+Bx → 0
(I3)  P·Hdiff − Rfree = (θ−3)(P²) + G·P − Rfree    θ = x d/dx,  G = (3/2)L(L+b) − Bx         → 0
(I4)  P·Hdiff − Rfree = 2x·( P P' − f2 P² − f1 P − f0 ),  f2 = 3/(2x), f1 = (Bx−(3/2)L(L+b))/(2x), f0 = Rfree/(2x) → 0
```

**Classification.** Solving (UF) for the highest derivative gives P' = f2 P + f1 + f0/P, i.e. the canonical Abel
equation of the second kind P P' = f2 P² + f1 P + f0 (I4). Its coefficients are rational in x with a simple pole at x = 0 (x·f0 → −3b⁴/32 when b ≠ 0). The reduction P = x^{3/2}w, ξ = ∫f1 x^{−3/2}dx gives the canonical form w·dw/dξ − w = Φ(ξ); Φ carries the unknown L.
The FIRST-kind form is obtained only by z = 1/P: z' = A3 z³ + A2 z² + A1 z with A3 = −Rfree/(2x), A2 = G/(2x),
A1 = −3/(2x), A0 = 0; a polynomial P of degree 2N is a rational solution z with 2N poles and a zero of order 2N at
infinity, which the polynomial-solution theorems do not address. In the V variable of the charged §7.2
(W = −B + ηx + x²V, deg V = 2t−1) the equation is (2P)V' = (quadratic in V) with 2P = 2x³V + 2ηx² − 2Bx − b²/2,
i.e. the general second-kind shape (g1 V + g0)V' = f2 V² + f1 V + f0 with g1 = 2x³: not a first-kind Abel equation in
V, not Bernoulli (the P-linear term G·P is present and G ≠ 0 on the target: G(0) = 0 but G'(0) = −B), not Riccati.

**Which unknown, which degree.** The unknown polynomial the finiteness theory would have to bound is P (degree
2N = 2t+2; equivalently V of degree 2t−1 or W of degree 2t+1). But L is not a coefficient: its N−1 free scalars
(c_1..c_{t−1}, b) are unknowns of the same problem, and B, η are read off P's jets. (UF) is therefore a single
polynomial identity in TWO unknown polynomials: 3N−2 = 3t+1 unknown scalars against 4N−2 = 4t coefficient
equations (rows x⁰..x³ vanish identically by the jets, row x^{4N} by (UL)), overdetermined by t−1.

**Degree comparison (the Malmquist/Rainville step) is exact and harmless.** If deg P = m ≠ 2N then either the top
of Rfree (degree 4N, coefficient 3/(16y⁴) ≠ 0) is uncancelled (m < 2N) or the top of (θ−3)(P²) forces 2m = 3
(m > 2N); and if deg L = N' ≠ N with deg P = 2N one gets the same contradiction. So deg P = 2·deg L exactly for every
polynomial solution, and the top row is (UT): (4N−3)p² + (3/2)p − 3/16 = 0 with p = ω y², whose discriminant is
exactly 3N (checked). The top step thus forces sqrt(3N) = 3d into the field: the quadratic field A_t = Q(√(3(t+1)))
is the OUTPUT of the leading comparison, not an obstruction. It is consistent at every N, as Astra already noted.

## 3. Task (2): the finiteness theory, applied honestly

**What the theorems do.** For a first-kind equation y' = Σ_{i≤n} A_i(x) y^i with polynomial A_i and A_n ≢ 0, two
polynomial solutions y_1, y_2 satisfy (y_1−y_2)'/(y_1−y_2) = polynomial, hence y_1 − y_2 is a CONSTANT k; substituting
y_1 + k back gives a polynomial identity of degree n−1 in k, so at most n polynomial solutions (Riccati ≤ 2, Abel ≤ 3).
This "solutions differ by constants" mechanism underlies the counts of Gasull–Torregrosa–Zhang (Riccati, JDE 2016)
and Cima–Gasull–Mañosas (Bernoulli/Abel, JDE 2017); I use only the mechanism, not any statement beyond it.

**Why it does not reach (UF).**
- It is a first-kind mechanism. For the second kind, two polynomial solutions P_1, P_2 of (θ−3)(P²) + GP = R with the
  SAME L give, with u = P_1 − P_2, s = P_1 + P_2, only x s u' = u(3s − x s' − G): every root of u is a common root of
  P_1, P_2, and nothing forces u constant. (y y' = y has the polynomial solutions x − c for every c.)
- Even a count would be vacuous. For fixed (L, field factor) the polynomial P is UNIQUE: the coefficient of a
  perturbation ε x^m of P in row x^{m+2N} of P·Hdiff − Rfree is λ(m) = 2ω(2N + m + 6d) (verified at every
  m ≥ 0 for t = 2, 3, 4; λ(k+1) is Theorem H's λ_k and the B-pivot −ω(4N+6d) = −2αd is recovered), and
  2N + m + 6d ≠ 0 for all m ≥ 0 when t ≥ 3 on both factors. So the top-down recursion determines P from L. The
  uniform residual is the statement that NO L (off Bη = 0) admits a P — a statement about an (N−1)-parameter
  family of Abel equations, which a per-equation count cannot see. This is the FALLACY-v2 "number is not degree"
  point in its sharpest form: the relevant number is ≤ 1 at every L already.
- Degree bounds (Malmquist, Rainville, Eremenko's rational-solution bound for first-order AODEs) are per-equation and
  return deg P = 2N here, which is exactly the prescribed degree. Nothing is incompatible with deg V = 2t−1, for
  t ≥ 8 or t ≥ 6.
- Bautin ideals and the Briskin–Françoise–Yomdin polynomial moment problem concern closed (centre) solutions of
  y' = p(x)y² + q(x)y³ over a fixed coefficient space, where Noetherianity of a FIXED ring bounds the number of
  conditions. Here the coefficient ring k[c_1..c_{t−1}, b] and the number of conditions 2t−1 both grow with t;
  Noetherianity gives no uniformity across t. The only faithful analogue is the universal recursion of §4, which
  is a moment-like sequence in infinitely many variables and is covered by no theorem I know.

**Conclusion of task (2).** No cited theory yields a uniform-in-t bound on the degree or number of polynomial
solutions of (UF) with the marked jets that conflicts with deg V = 2t−1. (R) remains open; (T) is not promoted.
No generic-coefficient theorem was applied to the marked-jet family: its hypotheses fail outright.

## 4. What the ODE viewpoint does establish: two singular points and a t-independent recursion

(UF) has two special points for a polynomial solution, and the whole finite problem is the matching of the formal
solutions there. All statements below are verified in `uf_verify.json` (t = 2, 3, 4) and `bottom_up_*.out`.

**x = ∞ (Theorem H rewritten).** With P = Σ_{m≤2N} P_m x^m, row x^{m+2N} is linear in P_m with pivot
λ(m) = 2ω(2N + m + 6d); rows x^{4N−1}..x^{2N+1} determine P_{2N−1}..P_2 and B = −P_1 (unit pivots); the rows
x^{2N}..x^{4} with P_0 = −b²/4 imposed are E_{2t}..E_2: the E_k are exactly the conditions that the unique formal
Laurent solution at infinity TERMINATES at the marked constant term. λ(m) = 0 iff m = −(2N+6d), integral only at the
split indices t = 3m_0²−1 (A_t = Q, d = ±m_0):

```text
m_0  t    d=−m_0: resonance index m = −6m_0(m_0−1)   in the truncation zone [−(2N−4),−1]?   d=+m_0
 1   2    m = 0   (the P_0 = −b²/4 slot, row E_4)     hits the marked slot: b-axis free       m = −12  below zone
 2   11   m = −12 (row E_10)                          yes                                    m = −36  below zone
 3   26   m = −36 (row E_16)                          yes                                    m = −72  below zone
 4   47   m = −72 (row E_22)                          yes                                    m = −120 below zone
```

At t = 2, d = −1 the resonance sits on the marked slot: [b²]E_4 = 0 there (Astra's E_4 = 177c⁶/50 − 33c³b/2 has no
b² term, while at d = +1 it is −2b² + …), which is the structural reason for the free b-axis and the failure of (V0)
with (8.1) intact. For m_0 ≥ 2 the resonance is invisible to the polynomial problem (that coefficient is zero anyway);
it only says the Laurent-tail reformulation is not a unit change of generators on d = −m_0 at t = 11, 26, 47, ….
This is a prediction about the structure of one row, not a kill.

**x = 0 (Briot–Bouquet point).** Row x^k of (θ−3)(P²) + GP − R is linear in P_k with pivot −(k−3)b²/2, INDEPENDENT
of t, d, ω, y (verified k = 0..2N at t = 2, 3, 4). So x = 0 is a Briot–Bouquet singular point of exponent 3: P_0, P_1,
P_2 are the marked jets, row x³ is the compatibility condition and vanishes identically by the jet linkage (it is the
residue [x³](R − GP) = 0 forced by (θ−3)⁻¹), and P_3 = w_2 is FREE. For k ≥ 4,

```text
P_k = Φ_k(b, B, η, w_2, l_2, …, l_k)
    = [ (k−3) Σ_{i=1}^{k−1} P_i P_{k−i} + Σ_{i=1}^{k} G_i P_{k−i} − R_k ] · 2/((k−3) b²),
```

a UNIVERSAL rational function (denominator a power of b), the same for every t; t enters only through
l_N = 1/y, l_j = 0 (j > N), and the truncation window. Polynomial solution at index t ⟺ Φ_{2N+1} = … = Φ_{4N} = 0
(then P_k = 0 for all k > 4N automatically, since rows above 4N contain no other term), after which the top row
forces Φ_{2N} ∈ {ω_+, ω_−}; the declared factor is imposed by adding Φ_{2N} − ω. Dehomogenising b = 1 (G_m, wt b = N)
gives 2N+1 equations in t+3 unknowns (c, B, η, w_2), valid for b ≠ 0.

Validation (`bottom_up.py`, Singular; `bottom_up_t3*.out`, `bottom_up_t4*.out`): at t = 3 over F_31991 (d ↦ 14162)
the ideals with the declared root, without any top equation, and with the other root are all UNIT (0–1 s); at t = 4
over F_31991 (d ↦ 4933) the declared-root ideal is UNIT (27 s). The exact Q(d) run at t = 3 and the negative controls
(first t+1 rows only, which must be non-unit) are recorded in §9. So the bottom-up recursion is a correct second
instrument, but it is NOT cheaper: Φ_9..Φ_16 at t = 3 have 55..385 terms in 5 variables and Φ_20 at t = 4 has 1272
terms, against raw E_k term counts 16,12,12,9,9 (t=3), 54..20 (t=4), 171..44 (t=5) in t variables.

**Meeting in the middle is the E_k again.** Matching the two recursions on b ≠ 0 generates the same locus; both have
unit pivots and the only freedom is L, so no independent uniform constraint appears.

## 5. Task (3): the grading forces nothing beyond the quotient; the monomial stratum in closed form

Homogeneity (wt x = 1, wt c_j = j, wt b = N, wt B = 2N−1, wt η = 2N−2) says the Euler derivation D on k[c,b][x]
multiplies each row by its weight, so (UF) ⟺ D_param(P²) = (4N−3)P² + GP − R with D_param = Σ j c_j ∂_{c_j} + N b ∂_b,
an identity with NO x-derivative: θ and the parameter weights are the same G_m. That G_m is exactly
the one Astra quotiented (U ≅ G_m × X); the slice X still has the t−1 coordinates c_j, so the grading cannot force a
solution to be a monomial family — it only lets one normalise B = η (or b = 1).

The monomial stratum c = 0 is a finite check with a closed form (`monomial_family.py`, symbolic in N with u = x^N,
θ u^j = jN u^j, reduced by 3d² = N, y = (d+N)/(2(2N−1)), ω y² = 1/(4(2d+1))). On c = 0 the weights force
L = u/y − b, P = ω u² + p_1 b u − b²/4, and B = η = 0 (weights 2N−1, 2N−2 are not multiples of N for N ≥ 3): the
stratum is NEVER in the target locus Bη ≠ 0. Row u³ gives p_1 = −(6d²−1)/(d(3d+1)(3d+2)); rows u⁴ and u⁰ vanish; the
remaining rows are

```text
[u²] = e(N,d) b²,   e(N,d) = −3(d+1)(6d²−1)²(9d³+8d²−1) / ( d²(2d+1)(3d+1)²(3d+2)² )      (= E_{2t} on the axis)
[u¹] = 3b³(d²−1)(6d²−1) / ( 2d(3d+1)(3d+2) )                                          (= E_{t−1} on the axis, t ≥ 3)
```

The zeros of e in d are d = −1, d = ±1/√6 (N = 1/2) and the roots of 9d³+8d²−1 (real root ≈ 0.305, N ≈ 0.28); with
N = 3d² an integer ≥ 3 only (N,d) = (3,−1), i.e. t = 2, d = −1, survives, and the [u¹] row vanishes exactly at d = ±1.
Checks: e(3,−1) = 0 (the exceptional family), e(3,+1) = −2 (Astra's residual −2b²x⁴), e ≠ 0 on both embeddings
for t = 3..12 (`monomial_family.json`; at t = 11: −490383/62720 and 21689/1600). So: the monomial family exists only at (t,d) = (2,−1), always has B = η = 0, and is irrelevant to (R).

## 6. Task (4): precise obstruction and the best finite-t instrument

**Obstruction, stated exactly.** The E_k (top-down) and the Φ_{2N+1..4N} (bottom-up) are consistency conditions of
recursions whose pivots are units; each is a family of 2N−3 (resp. 2N) weighted-homogeneous polynomials in a
parameter ring that grows with t. The residual (R) asks that these families have no common zero off Bη = 0 for all
N ≥ 9 (t ≥ 8). Polynomial-ODE theory bounds solutions of ONE equation; it has no statement about the emptiness of a
t-indexed family of such loci. That is the precise gap, and it is the same gap as OPEN[K16-INTRINSIC-SLICE-UNIT].

**Best finite-t instrument (unchanged in kind, sharpened in description).** Theorem H's top-down recursion IS the
"degree-by-degree linear recursion for V's coefficients whose consistency conditions are the E_k" requested in (4):
rows x^{4N−1}..x^{2N+1} are linear in the next unknown with the scalar-unit pivot λ(m); the E_k are the remaining rows.
Closing (8.1) at a fixed t is then the certificate (Bη)^n ∈ J = (E_2..E_{2t}) by the weight-(n(4t+1)) Macaulay matrix
(Astra's linear-certificate route, n = 2 through t = 5 exact), with n governed by the socle law when (V0) holds; the
bottom-up instrument is a valid cross-check but costs more (§4). No ODE shortcut (Darboux cofactor, canonical second-kind form) lowers this cost; each still carries the unknown L.

**Custody replay from (UF) alone** (`uf_emit.py`, Singular, exact coefficient field Q(d)/(3d²−N), identity map on
(c_i, b) with the parameter declared, `imap` from the embedded frozen ring):

```text
t   pivots (UF-emitter)                    frozen rows/B/η/target equal   std over Q(d)         T ∈ J   T² ∈ J   B², η² ∈ J
3   67473/1573·d − 78939/3146, …, B: −5733/242·d + 1764/121   yes (5 rows)   dim 0, vdim 66     no      yes      no, no
4   184437/4165·d − 110808/4165, …, B: −5832/245·d + 729/49    yes (7 rows)   dim 0, vdim 338    no      yes      no, no
5   —                                                          yes (9 rows)   not run exactly    (modular p=31991, d↦6434: dim 0, vdim 1709, T² ∈ J mod p — control only)
```

The t = 3 pivots are byte-identical to `controls_t3_emit.log`; Astra's t = 3, 4 conclusions are reproduced from
P·Hdiff − Rfree alone; the exact t = 5 conclusion is consumed, not re-proved (vdim 1709 is modular only). Note B², η² ∉ J at t = 3, 4: only the product's square lies in J, so the B–η jet linkage is essential to every
certificate, a further reason no single-unknown ODE theorem can do the work.

## 7. FALLACY-v2 check

- Number vs degree: the counts are per fixed equation and per-L uniqueness makes them vacuous; no degree conclusion
  was drawn from a count (§3). Generic-coefficient theorems: hypotheses (first kind, fixed polynomial coefficients)
  checked and found failing; none applied.
- Prime label/derivative: P', W', L' are genuine x-derivatives (charged §7.1); θ = x d/dx is declared; Astra's H of
  (RC1) is Hdiff, distinct from the slice determinant H.
- Variable/ring map: emitters declare the ring, the parameter d with its minimal polynomial, the generator order and
  the identity map on (c_i, b); frozen rows are compared by `imap`, not by name matching.
- Floor/attainment: deg P = 2N is an exact degree, proved by leading-term comparison in both directions (§2).
- Raw remainder degree / `sat()`: not used; unit tests are `std` = 1 with negative controls (§9).
- Flag/place/series, exit sets, pole identities, 8.5, arrival index: not touched here.
- No exit-price assertion is made; the `charge_basis` line is inapplicable.

## 8. OPENs

OPENS RAISED

- `OPEN[K16-UF-SECOND-KIND-FAMILY]` — a theorem on polynomial solutions of the SECOND-kind Abel family
  (θ−3)(P²) + G_L P = R_L with L ranging over monic-type polynomials of degree N and the marked jets, uniform in N.
  QUANTITY: number of known theorems bounding solutions across a family of Abel equations of the second kind whose
  coefficient polynomial is itself unknown = 0; a proof needs a statement of that type or a different mechanism.

OPENS RETAINED

- `OPEN[K16-INTRINSIC-SLICE-UNIT]` (charged §8): unchanged; equivalent to (UF) having no polynomial solution off
  Bη = 0. QUANTITY: first index without an exact certificate = 8 (unchanged); this lane adds structure (§4), not a closure.
- `OPEN[K16-UNIFORM-POINT]` (charged Galois lane): untouched. QUANTITY: #{t : a closed-form point of Γ_t is known} = 0.
- `OPEN[K16-ONE-POINT-T8]` (charged Galois lane): untouched. QUANTITY: verified simple F_p-points of Γ_8 with W ≠ 0 = 0.

## 9. Computation record (`box/abel-polysol-20260905/`), collisions, completion

```text
uf_verify.py / .json / .log     (I1)–(I4) with independent symbols; pivot laws at ∞ (m=0..2N−1) and at 0 (k=0..2N);
                                Theorem H pivots; (UT), (UL), disc 3N — t = 2,3,4 exact: UF_VERIFY_ALL_PASS
monomial_family.py / .json      closed forms of §5, symbolic in N; table t = 2..12 both embeddings
uf_emit.py → uf_emit_t{3,4,5}.sing/.out   (UF)-emitter + frozen-row custody (exact); std at t=3 (66), t=4 (338)
uf_emit_t5_p31991_d6434.out     modular t=5 control: dim 0, vdim 1709, T² ∈ J mod p          (control only)
bottom_up.py → bottom_up_t3_p31991_d14162.out   J1, J0, J2 all UNIT (≤ 1 s);  bottom_up_t4_p31991_d4933.out
                                J1 UNIT 27 s, J0 UNIT 420 s, J2 UNIT 28 s;  bottom_up_t3_p31991_negctrl.out
                                one row: dim 4 NONUNIT, two rows: dim 3 NONUNIT (four rows: timeout 110 s)
bottom_up_t3.out                exact Q(d) std of J1 at t=3: INCONCLUSIVE_TIMEOUT (reaped at 11.7 min CPU);
                                the exact bottom-up unit at t=3 is NOT claimed, only the modular one
resonance_table.txt             the ∞-resonance table (§4)
manifest.sha256, manifest.check.log, input-verification-final.log (4/4 OK at start and at sealing)
artifacts.sha256                sha256 of every file above
```

Reproduction: run the four `.py` drivers from the repository root (`uf_emit.py t [--std] [--prime p --droot r]`,
`bottom_up.py t [--prime p --droot r]`), then `Singular -q --cpus=1` on the emitted scripts.
All CAS work ran locally under `--cpus=1` (≤ 5 processes); no fleet worker; nothing running at sealing.

Collision scan (`collision_scan.txt`, filtered in `collision_scan.filtered.txt`): CANDIDATES. `OPEN[K16-UF-SECOND-KIND-FAMILY]`:
hits 17(ccccccc) (the charged Astra delta that states (UF): KNOWN, source) and 17(yyyyyy)/(zzzzzz) (Moh-lane
deltas: lexical noise). `OPEN[K16-INTRINSIC-SLICE-UNIT]`: 17(ccccccc) (source) and 17(eeeeeee) (census: noise).
`OPEN[K16-UNIFORM-POINT]` (retained): the K16 deltas 17(xx)–(vvvvvv), KNOWN. Nothing closes any OPEN.

<!-- BODY-END -->
