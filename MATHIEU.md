# MATHIEU.md — Mathieu–Zhao framing of R_{k,d2}, and the rigidity half of conj:R

Subject: the Mathieu subspace (Mathieu–Zhao) formulation of the residue
functional R_{k,d2} (RESIDUE.md), and an attack on the rigidity half of
paper1 conj:R through it.  Sources read: RESIDUE.md (full), SURPLUS.md,
SURPLUS-EXT.md §§0–1, LEMMA.md, paper1/main.tex §§ variants+functional.
Machine layer: cases/residue_check.py, new `mathieu` mode (§7; exit 0).

## 0. Headline

The Mathieu–Zhao lens does three things here.

1. BRIDGE (§3): with M_A := Im(L_A), L_A := A d/dy − kA′ (the 1-variable
   shadow of ad_{xA}, RESIDUE.md interp (c)), the rigidity half of conj:R
   at (k,d2) is EXACTLY the statement "1 ∉ M_A for every A with
   2 ≤ deg A ≤ d2".  If M_A is a Mathieu subspace, this follows at once,
   because a Mathieu subspace containing 1 is the whole algebra and M_A is
   provably proper.  Derived in full in §3.
2. APPLICABILITY (§4): the outer functional R is an honest Laurent-
   polynomial constant term (machine check M3), so Duistermaat–van der
   Kallen applies literally there — but vacuously.  The inner (rigidity)
   functional lives on a (δ+1)-punctured line, outside every proved
   instance of the MZ program; the Mathieu property of M_A is open (§6).
3. ATTACK (§5): the DvdK MECHANISM — the valuation-at-infinity /
   one-sided-support argument that proves the 1-variable case — applies
   directly to L_A and CLOSES the rigidity half: an elementary,
   coordinate-free proof (Theorem A) that A C′ − k A′ C = 1 with A, C
   polynomials forces deg A ≤ 1, for every k ≥ 1, in characteristic 0.
   Consequently (with RESIDUE.md §4b's uniform outer theorem) conj:R
   holds at ALL cells k, d2 ≥ 2 — including the previously open
   (3,4), (4,4), (5,4) and all d2 ≥ 5.  Status: new proof, this file;
   machine-corroborated at every step (§7); NEEDS adversarial review
   before the paper absorbs it (repo practice: LEMMA-REVIEW pattern).

## 1. The Mathieu–Zhao frame

### 1.1 Definitions (Zhao)

Let 𝒜 be a commutative algebra over a field F.  A subspace M ⊆ 𝒜 is a
MATHIEU SUBSPACE (Mathieu–Zhao space) if: for every a ∈ 𝒜 such that
a^m ∈ M for ALL m ≥ 1, and every b ∈ 𝒜, there is N = N(a,b) with
b·a^m ∈ M for all m ≥ N.  Every ideal is Mathieu (with N = 1); the point
of the notion is that M need not be closed under multiplication by 𝒜 —
only powers of "radical-like" elements eventually absorb factors.
Radical language: r(M) := {a : a^m ∈ M for all m ≫ 0} and
sr(M) := {a : ∀b, b·a^m ∈ M for all m ≫ 0}; M is Mathieu iff every a
with all powers in M lies in sr(M).

Trivial but load-bearing lemma (used in §3): if M is Mathieu and 1 ∈ M,
then M = 𝒜.  Proof: take a = 1; then 1^m = 1 ∈ M for all m, so for every
b there is N with b = b·1^m ∈ M.  ∎

### 1.2 The Duistermaat–van der Kallen theorem

THEOREM (DvdK, Indag. Math. 9 (1998)).  Let 𝒜 = C[x_1^{±1},…,x_n^{±1}]
and CT: 𝒜 → C the constant-term functional.  Then ker CT is a Mathieu
subspace of 𝒜: if CT(f^m) = 0 for all m ≥ 1, then for every g ∈ 𝒜,
CT(g f^m) = 0 for all large m.

This is the abelian (torus) case of Mathieu's 1995 conjecture for compact
connected Lie groups, and it is the ONE deep proved instance of the
program.  In one variable the proof yields the sharp support dichotomy:

  (DvdK-1D)  CT(f^m) = 0 for all m ≥ 1  ⟺  supp(f) ⊆ Z_{>0} or
             supp(f) ⊆ Z_{<0}  (f a Laurent polynomial, f = 0 allowed).

The mechanism of the 1-variable proof is a VALUATION argument at the two
punctures 0, ∞: if the support is two-sided, the leading behavior of f^m
at one puncture cannot cancel out of the constant term for every m.
That mechanism — leading-term one-sidedness at a distinguished place —
is what we transport in §5.  (Confidence: statement of the theorem HIGH;
the 1-D dichotomy as stated HIGH on truth, MEDIUM on being verbatim in
the paper.)

### 1.3 Ledger: theorem vs conjecture in the MZ literature

From memory (no web access); confidence labels per line.

PROVED:
- DvdK theorem, all n (above).  [HIGH]
- Zhao's framework papers exist and fix the definitions used here:
  "Generalizations of the image conjecture and the Mathieu conjecture"
  (J. Pure Appl. Algebra 214 (2010)) and "Mathieu subspaces of
  associative algebras" (J. Algebra 350 (2012)).  [HIGH]
- van den Essen–Wright–Zhao: the Image Conjecture for COMMUTING
  order-one operators with CONSTANT leading coefficients (the family
  containing the Gaussian-moment / ∂_i − x_i reformulations of JC),
  and: images of LOCALLY FINITE derivations of C[x,y] are Mathieu
  (J. Pure Appl. Algebra 215 (2011)).  [MEDIUM]
- Muzychuk–Pakovich: solution of the polynomial moment problem
  (vanishing of all moments forces composition structure) — the closest
  proved relative of "all residues of all powers vanish ⟹ structural
  degeneration" on multiply-punctured domains.  [MEDIUM-HIGH]

CONJECTURAL / NOT AVAILABLE:
- Mathieu's conjecture for nonabelian compact G: open.  [HIGH]
- Zhao's Image Conjecture in general: open.  [HIGH]
- Images of order-one operators with NON-CONSTANT leading coefficient
  (our L_A = A∂ − kA′): no proved Mathieu statement I can cite.  [HIGH
  that I cannot cite one; the statement itself is §6's SC1.]
- CT/residue functionals at ≥ 3 punctures (algebra C[y, 1/A], deg A ≥ 2):
  outside DvdK and outside every weighted-CT extension known to me; the
  weighted/twisted CT results in the MZ corpus stay on the 2-punctured
  torus with monomial or Gaussian weights.  [MEDIUM-HIGH]
- Laurent-SERIES analogues of DvdK (completed algebras): status unknown
  to me; not usable as a theorem.  [MEDIUM]

## 2. Our objects: algebras, functionals, candidate M

The campaign's functional (paper1 §functional, RESIDUE.md):
R_{k,d2} = Σ_{j=max(k+2,d2)}^{2d2} (−1)^j C(j,k+2) a2^{2d2−j} b_j,
with three verified interpretations: CT-at-infinity (b), iterated
Grothendieck residue of dP∧dQ/(x^{k+2}A^{k+2}) at the toric boundary
point (a), Koszul moment functional μ spanning the reachable cokernel of
ad_{xA} (c).  Three candidate (algebra, subspace) pairs present
themselves; choosing correctly is most of the work.

(i) OUTER pair — 𝒜 = C[w^{±1}], w = A(y) = 1 + a2·y the edge coordinate
on the binomial locus (a2 ≠ 0), M = ker CT.  Here R is literally a
Laurent-polynomial constant term:
    R_{k,d2} = CT_w( β′(w) · w^{−(k+1)} ),   β(w) := B((w−1)/a2),
equivalently a2^{2d2}·β_{k+2} = (−1)^k R (machine check M3, 12 cells —
this identity also re-derives the max(k+2,d2) lower-limit correction of
RESIDUE.md §1, since C(j,k+2) = 0 for j < k+2 and b_j is absent for
j < d2).  So on the binomial locus the torus normalization is exact and
NO twist blocks DvdK: it applies as stated.  But its conclusions are
eventual-vanishing statements, and on the elements we care about
(one-sided supports in w) those hold for trivial degree reasons; DvdK
gives no leverage on the outer half — which RESIDUE.md §4b anyway proved
uniformly.  The outer half is not where MZ content lives.

(ii) INNER localized pair — 𝒜 = W := C[y][1/A] (the coefficient ring
with the strip's edge polynomial inverted; A = P-column-1, deg A =: δ),
M = Im(d/dy|_W) = ∩_{A(r)=0} ker Res_r(· dy).  This is the right
invariant content: rigidity concerns the powers A^{−(k+1)}, and W is the
function ring of the (δ+1)-punctured projective line (roots of A and ∞).
For δ = 1 and A = y this is (a residue twist of) the DvdK 1-D situation;
for δ ≥ 2 it is outside every proved MZ instance (§1.3).

(iii) INNER polynomial pair (THE BRIDGE FRAME) — 𝒜 = C[y],
    L_A := A·d/dy − k·A′  (multiplication),   M_A := Im(L_A).
L_A is the 1-variable shadow of ad_{xA} on the inner column (RESIDUE.md
interp (c), weight k), and L_A(C) = A^{k+1}·(C/A^k)′.  Note that
ker(R) itself — the hyperplane in the b-coordinates — is NOT the right
M: R is the pairing of the FIXED cokernel functional μ against the
variable inhomogeneity G; the Mathieu structure lives on the μ/image
side, i.e. in M_A, not in one hyperplane of values.

Basic structure of M_A (proved in §3): μ_i ∘ L_A = 0 for the residue
functionals μ_i(f) := Res_{r_i}(f·A^{−(k+1)} dy) at the roots r_i of A —
the global, multi-point form of RESIDUE.md's μ; for squarefree A,
M_A = ∩_i ker μ_i, of codimension exactly δ in C[y].  So M_A is a
finite-codimension residue-kernel subspace — precisely the multi-point
generalization of DvdK's ker CT.

## 3. The bridge theorem

Throughout §§3–5, F is a field of characteristic 0 (see §5.4 for char p),
A ∈ F[y] with A(0) = 1 (units a1 = c1 = 1 scaled out as in SURPLUS-EXT
§0), δ := deg A, and k ≥ 1.

LEMMA B (block ⟺ ODE; the precise content of "rigidity half").  Fix
k ≥ 2, d2 ≥ 2 and a point a = (a2,…,a_{d2+1}), A = 1 + Σ_{i≥1} a_{i+1}y^i.
The d2 − 1 inner extras of the depth-2 block vanish at a if and only if
there exists C ∈ F[y] with support in {y,…,y^{kd2}} such that
    (ODE)   A·C′ − k·A′·C = 1 .
Proof.  Post-gap-kill, bracket Minkowski column k+1, read as a
polynomial in y, is A C′ − k A′ C with C = Q-column-k (SURPLUS-EXT §0,
cross-verified against the independent lattice-determinant enumeration
by surplus_ext.wide_W1).  The pair (A_i, c_j) contributes
(j − ki)·a_{(1,i)}c_j·y^{i+j−1}, so with deg A ≤ d2, supp C ⊆ {1..kd2}:
the y^0-coefficient is c_1 (the vertex equation, = 1 after unit
scaling); the y^{(k+1)d2−1}-coefficient is (kd2 − k·d2)a_{(1,d2)}c_{kd2}
= 0 identically (Prop A's stratum w = 0); and the block keys
(k+1, s), s = 2..(k+1)d2−1 are exactly the remaining coefficients
y^1..y^{(k+1)d2−2} of (ODE).  The triangular solve (col_series, pivots
n+1 ≠ 0 in char 0) uses the equations y^1..y^{kd2−1} to determine
c_2,…,c_{kd2} uniquely from c_1 = 1; the extras are the leftover
equations y^{kd2}..y^{(k+1)d2−2}.  If the extras vanish, the solved C
witnesses (ODE).  Conversely, a witness C of (ODE) with the stated
support is UNIQUE: two solutions differ by an element of
ker L_A = F·A^k (if A K′ = k A′ K then (K/A^k)′ = 0 in F(y), and the
constants of (F(y), d/dy) are F in char 0), and A^k(0) = 1 forces the
difference's constant term — hence the difference — to be 0 when both
have zero constant term.  So the solved series equals C and the extras
vanish.  ∎

BRIDGE THEOREM.  Fix k ≥ 1 and A with δ = deg A ≥ 2.  Then:
(a) (properness) No element of M_A = Im(L_A) has y-degree (k+1)δ − 1;
    in particular y^{(k+1)δ−1} ∉ M_A and M_A ⊊ C[y].
(b) (residue description) μ_i ∘ L_A = 0 for every root r_i of A, where
    μ_i(f) := Res_{r_i}(f·A^{−(k+1)}dy); if A is squarefree,
    M_A = ∩_{i=1}^{δ} ker μ_i, of codimension exactly δ.
(c) (bridge) If M_A is a Mathieu subspace of C[y], then 1 ∉ M_A.
(d) Hence: if M_A is Mathieu for every A with 2 ≤ deg A ≤ d2, then the
    rigidity half of conj:R holds at (k, d2): the inner extras force
    a_{(1,i)} = 0 for 2 ≤ i ≤ d2 ("A binomial").

Proof.
(a) LEADING-COEFFICIENT LEMMA (the engine of everything below): for
D ∈ F[y] nonzero with d := deg D,
    lc-formula:  coefficient of y^{δ+d−1} in L_A(D) = (d − kδ)·lc(A)·lc(D),
and L_A(D) has no coefficient above y^{δ+d−1}.  [Only the top×top pair
(i,j) = (δ,d) reaches i+j−1 = δ+d−1; its weight is (j − ki) = d − kδ.
Machine check M4b, symbolic, k, δ = 1..4, all d ≤ kδ+2.]  So:
if d ≠ kδ then deg L_A(D) = δ+d−1 exactly (char 0: d − kδ ≠ 0 in F);
if d = kδ the top cancels and deg L_A(D) ≤ (k+1)δ − 2.  Now take any
C with L_A(C) of degree (k+1)δ−1: writing C = α·y^{kδ} + (rest), the
y^{kδ}-part contributes degree ≤ (k+1)δ−2 and each other degree d
contributes exact degree δ+d−1 ≠ (k+1)δ−1 with no cross-cancellation at
distinct degrees — the top degree present among the parts survives.
Hence degree (k+1)δ−1 is never attained.  [Machine check M2a.]
(b) μ_i(L_A(C)) = Res_{r_i}((A C′ − kA′C)A^{−(k+1)}dy)
= Res_{r_i}((C/A^k)′ dy) = 0: the residue of an exact rational form
vanishes.  This is RESIDUE.md interp (c)'s "μ ∘ L = 0", globalized from
the binomial locus to every root of every A.  Codimension: L_A maps
F[y]_{≤n} to F[y]_{≤n+δ−1} with 1-dimensional kernel F·A^k (n ≥ kδ), so
dim L_A(F[y]_{≤n}) = n; and no C with deg C > n has L_A(C) in
F[y]_{≤n+δ−1} (by the lc-formula its degree is δ + deg C − 1 > n+δ−1
unless deg C = kδ ≤ n), so Im(L_A) ∩ F[y]_{≤n+δ−1} = L_A(F[y]_{≤n})
has codimension δ in F[y]_{≤n+δ−1}, stably in n.  For squarefree A the δ
functionals μ_i are linearly independent (f = (A/(y−r_i))^{k+1}·(y−r_i)^k
separates them) and annihilate Im(L_A) by the above, so they cut it out.
(c) By §1.1's lemma, a Mathieu M_A containing 1 would equal C[y],
contradicting (a).  So 1 ∉ M_A.
(d) 1 ∉ M_A for all 2 ≤ deg A ≤ d2 says (ODE) has no polynomial
solution when deg A ≥ 2 (the support cap is automatic: any solution has
deg C = kδ ≤ kd2 by the lc-formula, and can be normalized to zero
constant term by subtracting C(0)·A^k, which preserves deg ≤ kδ).  By
Lemma B the inner extras then vanish only where deg A ≤ 1.  Conversely
on the binomial locus C = ((1+a2y)^k − 1)/(ka2) (or C = y at a2 = 0)
solves (ODE) within the support, so the extras vanish there — the
variety of the inner extras is exactly {A binomial}.  ∎

Remark (shape of the bridge).  The mission's expected reduction was
"powers of a unit-type element have eventually-vanishing R".  The frame
that closes is sharper and simpler: the unit-type element is 1 itself,
whose powers are constant — so "eventually" collapses to "now", and the
Mathieu property is consumed exactly once, through "1 ∈ M ⟹ M = 𝒜".
In the localized frame (ii) the same statement reads: rigidity at all
weights simultaneously ⟺ NO power A^{−m} (m ≥ 2) of the unit 1/A of W
lies in Im(d/dy|_W) when δ ≥ 2 — a per-power nonvanishing, which is
strictly stronger than what Mathieu-ness of Im(d/dy|_W) asserts.  This
is the honest reason MZ theorems alone cannot finish: they control
eventual behavior, rigidity needs every power.  The proof in §5 supplies
the per-power statement directly.

## 4. Applicability of DvdK: exact diagnosis

Is our CT form literally a Laurent-polynomial constant term?
- OUTER: YES, with no twist.  R = CT_w(β′(w)·w^{−(k+1)}) on the binomial
  locus (M3).  DvdK applies as a theorem; its conclusion is vacuous for
  our purposes (§2(i)).  No weighted/twisted extension is needed.
- INNER: NO.  Off the binomial locus the natural expansion places are
  the δ roots of A plus ∞; the algebra is W = C[y,1/A], the function
  ring of a (δ+1)-punctured P^1, and the functional is a TUPLE of
  residues (μ_1,…,μ_δ), not one CT.  The DvdK hypothesis that fails is
  the algebra itself: C[w^{±1}] is the 2-punctured case δ = 1.  The
  minimal degeneration is visible already there: for δ = 1 the powers
  A^{−m} (m ≥ 2) DO all lie in ker Res (one-sided Laurent support — no
  obstruction: the binomial locus), while for δ ≥ 2 Theorem A says no
  power does.  The rigidity dichotomy of conj:R IS the DvdK 1-D support
  dichotomy transported to the strip's toric boundary: "1/A behaves
  like a one-sided Laurent monomial ⟺ deg A ≤ 1 ⟺ the edge polynomial
  meets the boundary in at most one simple point".
- Zhao's known extensions (weighted CT, image-conjecture cases with
  constant leading coefficients, locally finite derivations in 2
  variables) all stay on ≤ 2 punctures or constant-coefficient
  operators; none covers L_A = A∂ − kA′ with deg A ≥ 2 (§1.3).  So the
  bridge hypothesis of §3(c) is genuinely conjectural (SC1, §6) — but,
  decisively, it is NOT needed: the DvdK mechanism itself closes the
  problem at the one place where our geometry is still one-sided for
  every A — the puncture at infinity.  That is §5.

## 5. The attack: the rigidity half, proved

### 5.1 Theorem A

THEOREM A (rigidity, all weights).  Let F have characteristic 0, let
w ≥ 1 be an integer, and let A, C ∈ F[y] satisfy
    A·C′ − w·A′·C = c   for some constant c ∈ F, c ≠ 0.
Then deg A ≤ 1.

Proof.  Both A and C are nonzero (else the left side is 0 ≠ c).  Write
δ := deg A, α := lc(A), and suppose δ ≥ 2.

Step 1 (leading-coefficient lemma).  For any nonzero D ∈ F[y] with
d := deg D, the coefficient of y^{δ+d−1} in A D′ − w A′ D is
(d − wδ)·α·lc(D), and no higher power of y occurs.  Indeed the pair
(A_i, D_j) contributes A_i D_j (j − wi) y^{i+j−1}, maximized at
(i,j) = (δ,d).  [Machine check M4b.]  In char 0, d ≠ wδ implies
(d − wδ) ≠ 0 in F, so then deg(A D′ − w A′ D) = δ + d − 1 exactly.

Step 2 (top degree of C).  If deg C ≠ wδ, Step 1 gives
deg(A C′ − w A′ C) = δ + deg C − 1 ≥ δ − 1 ≥ 1 > 0 = deg c,
a contradiction.  Hence deg C = wδ.

Step 3 (kernel element).  A·(A^w)′ − w·A′·A^w = wA^wA′ − wA′A^w = 0.
[Machine check M4a.]

Step 4 (subtract the kernel at top degree).  Let β := lc(C)/α^w ∈ F^×
and D := C − β·A^w.  By Step 3, A D′ − w A′ D = c still; by
construction deg D < wδ.  If D = 0 then c = 0, a contradiction.  If
D ≠ 0 then d := deg D < wδ, so by Step 1
deg(A D′ − w A′ D) = δ + d − 1 ≥ δ − 1 ≥ 1 > 0 = deg c,
again a contradiction.  Hence δ ≥ 2 is impossible.  ∎

For δ ≤ 1 the equation IS solvable (C = ((1+a2y)^w − 1)/(wa2), resp.
C = y at a2 = 0, for c = 1), so Theorem A is sharp; and it is exactly
the "valuation at infinity" DvdK mechanism: ord_∞ applied to
dt = dy/A^{w+1}, t = C/A^w, says t − t(∞) vanishes at ∞ to order
(w+1)δ − 1, which exceeds the map degree wδ as soon as δ ≥ 2 — the
support of the would-be solution is forced one-sided past its own
budget.  (The algebraic Steps 1–4 are that valuation argument made
elementary; no Riemann–Hurwitz needed.)

### 5.2 The rigidity half of conj:R

COROLLARY C (rigidity half, ALL cells).  For every k ≥ 2, d2 ≥ 2, over
any field of characteristic 0: the inner extras of the depth-2 block
vanish at a = (a2,…,a_{d2+1}) iff a3 = … = a_{d2+1} = 0.  Equivalently
V(inner extras) = {A binomial}: the inner column forces deg A ≤ 1.

Proof.  (⇐) On the binomial locus the explicit C above solves (ODE)
within the support {y,…,y^k} ⊆ {y,…,y^{kd2}}; by Lemma B the extras
vanish.  (⇒) If the extras vanish, Lemma B produces a polynomial C with
A C′ − k A′ C = 1; Theorem A (w = k ≥ 2 ≥ 1) forces deg A ≤ 1.  ∎

This settles, structurally and uniformly, the cells proved before by
per-cell work — (2,2) (inner extra −a3^k), (2,3)/(2,4) (squarefree +
A | N(A) divisibility), (3,3),(4,3),(5,3) (resultant certificates
with exponents (15,12),(26,34),(40,44)) — and the OPEN cells
(3,4),(4,4),(5,4) and all d2 ≥ 5, where the perfect-power component of
the divisibility route was the obstacle.  Note how the two halves of
the old argument collapse: perfect powers (1+uy)^δ die by evaluating
(ODE) at the multiple root (0 = 1) — no squarefreeness lemma needed —
and squarefree A of degree ≥ 2 die by Step 4 — no residue divisibility
A | N(A) needed.  The residue condition is bypassed, not solved:
Theorem A proves it could never hold (Corollary E).

COROLLARY D (conj:R, full statement).  For every k, d2 ≥ 2, char 0:
    V(extras) = {A binomial} ∩ ({a2 = 0} ∪ {R_{k,d2} = 0}).
Proof.  Corollary C reduces V(extras) to {A binomial} ∩ V(outer extras).
On the binomial locus, RESIDUE.md §4b (uniform outer theorem, chain
S1–S5; polynomial identities in (a2, b), so valid at a2 = 0 too) gives:
outer extras t ≥ 1 vanish identically and
extra_0 = ±(k+2)/C((k+1)d2, k+1)·a2^{(k−1)d2}·R_{k,d2}, which vanishes
iff a2 = 0 or R = 0 (note (k−1)d2 > 0).  ∎
Dependency note, honestly: §4b's S1–S5 is stated in RESIDUE.md as a
general derivation with each step a short general argument, machine-
verified at 11 cells; Corollary D inherits exactly that status plus
this file's review status.  Corollary C itself depends only on Lemma B
and Theorem A.

### 5.3 The residue dichotomy (the statement MZ was circling)

COROLLARY E.  Let A ∈ C[y] be squarefree with deg A ≥ 2.  Then for
EVERY m ≥ 2 there is a root r of A with Res_r(A^{−m} dy) ≠ 0.  (For
m = 1 all residues 1/A′(r) are nonzero; for deg A ≤ 1 all residues of
all powers m ≥ 2 vanish.)

Proof.  Suppose all residues of A^{−m}dy vanish.  Partial fractions
(simple roots): A^{−m} = Σ_i Σ_{l=2}^{m} c_{i,l}(y−r_i)^{−l} with no
l = 1 terms and no polynomial part; termwise integration gives
g ∈ C(y) with g′ = A^{−m} and pole order ≤ m−1 at each r_i and no other
poles.  Then C := A^{m−1}·g is pole-free, hence a polynomial, and
A C′ − (m−1) A′ C = A^m g′ = 1.  Theorem A (w = m−1 ≥ 1) forces
deg A ≤ 1, a contradiction.  ∎

Corollary E is the exact multi-place analogue of DvdK-1D: "all powers
of 1/A residue-free ⟺ the pole configuration is one-sided (a single
simple point)".  It also explains RESIDUE.md §5's observation that
perfect powers pass the residue test but fail the valuation: the
residue test alone (A | N(A) for k = 2) has the perfect-power
solutions, but the INTEGRATED statement — polynomiality of A^{m−1}g —
never survives past degree 1.

### 5.4 Characteristic

Theorem A as stated uses char 0 twice: (d − wδ) ≠ 0 in Step 1/2/4, and
"constants of (F(y), d/dy) = F" inside Lemma B's uniqueness (and the
triangular pivots n+1).  For the block instance all degrees are capped:
deg C ≤ kd2, |d − kδ| ≤ kd2, pivots n+1 ≤ (k+1)d2 − 1.  So Corollary C
holds over any field of characteristic p > (k+1)·d2 (conservative), in
the spirit of the campaign's per-cell prime exclusions ({2,3,5} at
(2,2), etc.).  In small characteristic Step 2 genuinely fails (deg C
can be wδ + p with vanishing leading weight), consistent with the
Mondello example living in char 2.

## 6. What remains for the MZ program proper: SC1

The bridge hypothesis of §3(c) is now not needed, but it is the
sharpest statement that MZ machinery would settle, and rigidity gives
it evidence.  Recording it precisely:

SUB-CONJECTURE SC1.  (a) Polynomial form: for every A ∈ C[y] squarefree
with deg A = δ ≥ 1 and every k ≥ 1, M_A = Im(A∂ − kA′) =
∩_{i=1}^δ ker(f ↦ Res_{r_i}(f A^{−(k+1)}dy)) is a Mathieu subspace of
C[y].  (b) Localized form: Im(d/dy) = ∩_i ker Res_{r_i}(· dy) is a
Mathieu subspace of C[y, 1/A].

Status: open; not covered by DvdK (wrong algebra for δ ≥ 2: δ+1
punctures) nor by any proved image-conjecture case (non-constant
leading coefficient).  Evidence from this file: (1) Corollary E
computes the full power-behavior of the natural test element a = 1/A in
frame (b): for δ ≥ 2 NO power lies in M (so a imposes no Mathieu
condition — consistency is free but meaningful: a genuinely fails the
membership test at every m, not just at one); for δ = 1 all powers
m ≥ 2 lie in M and the Mathieu conclusion holds explicitly —
Res_r(b·A^{−m}) = u^{−m}b^{(m−1)}(r)/(m−1)! = 0 as soon as
m > deg b + 1.  So SC1 passes every test reachable through powers of
1/A.  (2) DvdK-1D is (a twist of) the case δ = 1 of (b).  A proof of
SC1 for δ ≥ 2 would be the first Mathieu theorem on a curve with more
than two punctures, and this repo's block geometry is a ready-made
consumer; conversely a COUNTEREXAMPLE to SC1 would not damage conj:R
(Theorem A stands independently).

## 7. Mechanical verification (exact arithmetic)

cases/residue_check.py, new additive mode:
    python3 cases/residue_check.py mathieu     (exit 0 = all OK)
Default invocation is unchanged (T0–T5 suite re-run: ALL OK).  Checks,
all exact Fractions, run 2026-08-12, 0.3 s, MATHIEU OK:
- M1 rigidity dichotomy: for k = 1..5, d2 = 2..5, every deg A = δ ≤ d2,
  random/perfect-power/mixed numeric A: inner extras vanish ⟺ δ ≤ 1.
  (Sampled corroboration of Corollary C on and off the repo grid.)
- M2 bridge: (a) y^{(k+1)δ−1} ∉ Im(L_A) — properness witness of §3(a) —
  and (b) 1 ∈ Im(L_A) ⟺ δ ≤ 1, both by exact inconsistency/solvability
  of the full linear system (Gaussian elimination, generous degree cap),
  k = 1..4, δ = 1..4, including non-squarefree A.  The δ = 1 solvable
  control confirms the checker detects consistency when present.
- M3 CT form: a2^{2d2}·β_{k+2} = (−1)^k R_{k,d2} symbolically at 12
  cells (11 repo cells + (2,6)): R is an honest Laurent constant term;
  independently re-derives the max(k+2,d2) lower-limit correction.
- M4 Theorem A's two computational identities, SYMBOLICALLY (generic A
  and D, k, δ = 1..4, all d ≤ kδ+2): L_A(A^k) ≡ 0, and the
  leading-coefficient formula lc(L_A(D)) = (d − kδ)·lc(A)·lc(D) with
  exact cancellation at d = kδ and no overflow above δ+d−1.  With these
  two identities verified, the remaining content of Theorem A's proof
  is integer inequalities (δ + d − 1 ≥ 1, d − wδ ≠ 0).
- M5 per-cell tie at (2,2),(2,3),(3,3),(3,4),(4,4),(5,4),(2,5),(3,5),
  (2,6) — including every previously OPEN cell within reach: symbolic
  inner extras vanish identically on the binomial locus; are nonzero at
  all perfect-power points (1+uy)^δ, 2 ≤ δ ≤ d2 (the historically
  dangerous family) and at random off-binomial points; and the symbolic
  and numeric solve paths agree.

## 8. Consequences and next steps

For conj:R: the conjecture's rigidity half is a theorem (Corollary C),
and with RESIDUE.md §4b the full conj:R variety statement holds at every
cell k, d2 ≥ 2 (Corollary D).  Downstream (paper1 §functional's own
list): no depth-2 block point with all coordinates nonzero for any
k, d2 ≥ 2; pinning-type obstruction only at (2,2); no b-side obstruction
for d2 ≥ 3; no residue condition for k > 2d2 − 2.  The (3,3),(4,3),(5,3)
certificates upgrade from certified computation to structural theorem;
(3,4),(4,4),(5,4) and d2 ≥ 5 close.

For the strip program: every strip-shaped reduced subcase with k ≥ 2,
d2 ≥ 2 now carries the uniform support-rigidity + residue-hyperplane
constraint at depth 2 — the case analysis of SECTION4/coverage can cite
one theorem instead of a cell table.  Unchanged scope limits: strip
hypotheses (gap-kill, full block columns), d1 = 1, no y-axis support;
depth ≥ 3 untouched — though Theorem A is already the homogeneous
engine at every weight w = k+D−1, so the depth-D prediction of
RESIDUE.md §5 (one residue functional per deeper column) should now be
attackable by the same two lemmas.

Recommended next steps, in order: (1) adversarial review of Lemma B +
Theorem A (the proof is 15 lines; the risk concentrates in Lemma B's
block ⟺ ODE identification, which M5 tests at 9 cells); (2) absorb
into paper1 (§ variants shrinks: thm:23/thm:24 rigidity halves and
thm:k3 become corollaries; §functional's conjecture becomes a theorem
modulo §4b's write-up); (3) Lean formalization of Theorem A (kernel +
leading-coefficient argument; small, fits the repo's lean/ practice);
(4) depth ≥ 3 via the weight-w engine; (5) SC1 as a standalone MZ
contribution (first ≥ 3-puncture Mathieu statement), with Corollary E
as its power ledger.

## 9. Files

- MATHIEU.md (this file).
- cases/residue_check.py — `mathieu` mode appended (M1–M5); default
  T0–T5 suite unchanged and re-verified.
