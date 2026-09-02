# Research lane: KELLER-PENCIL-GENUS — bound the genus of the generic member of a Keller pencil (flagship effort)

Everything the campaign's H2 program below N = 17 still needs funnels
into ONE quantity. The reviewed MF-EXACT identity (integration #11): for
a noninvertible Keller map F = (P, Q) of geometric degree N under H2 and
a generic line L, the generic member C_L = F^{-1}(L) = {alpha P + beta Q
= gamma} of the affine pencil is a smooth curve with
      n (W − S) = N − 2 + 2 g_L + theta_inf,
n = deg A_F-bar, W = N − a, S = sum s_l, g_L its genus, theta_inf its
target-escaping places at infinity (1 <= theta_inf <= N). The ceiling
flagship (charged as a PROPOSAL; its review runs in parallel — consume
only what you re-derive) shows no intersection-theoretic boundary
instrument can bound the map degree at fixed N, and reduces the ceiling
to one integer, the anticanonical defect Z·K_X = sum a_i − 3D of the
polar divisor; the coordinator's desk note (unreviewed, notes ~11:25Z)
observes by adjunction on the resolution that Z·K_X = 2 g_L − 2 − N, so
that integer IS the genus. Bounding g_L in N bounds n, hence delta_aff,
hence makes the (B3) enumeration finite at every N; and by Moh 1983
(D_min >= 101), any bound D_min <= 100 kills every (B2)/(B3) cell at
4 <= N <= 16 outright. The lower bounds are exact and priced: g_L >= 0
(floor), and the +1 question OPEN[MF-DEFECT] (is 2 g_L + theta_inf >= 2
always) is in a parallel lane. Nothing reviewed gives an UPPER bound.

Your task: find the mechanism, or the exact obstruction, for an upper
bound g_L <= f(N). The datum no lane has consumed is the SYMPLECTIC
structure: dP ∧ dQ = dx ∧ dy exactly, so (i) for u = alpha P + beta Q the
Hamiltonian field X_u = (−u_y, u_x) is a nonvanishing polynomial vector
field tangent to every fibre C_t; (ii) for any linearly independent
v = gamma P + delta Q, {u, v} = alpha delta − beta gamma is a nonzero
CONSTANT, so v restricted to each fibre C_t has nowhere-vanishing
derivative along X_u — v|_{C_t} : C_t → A^1 is an étale map of degree N
whose non-properness set is exactly the n points of L_t ∩ A_F; (iii) the
flow of X_u moves v at unit speed on every fibre, so the pair (u, v)
gives every fibre the structure of an étale "unit-speed" cover of A^1
with escapes at n points. Attack:
(1) Write the fibre C_t with its étale degree-N map v : C_t → A^1 and
    the unit-speed structure; derive what the monodromy of that cover
    around the n non-proper points and around ∞ can be (this is the
    cycle-type data the meridian floor uses — re-derive MF-EXACT from
    it as your control), and then ask what the symplectic unit-speed
    condition adds: the differential dv restricted to C_t equals the
    dual of X_u, a nowhere-vanishing REGULAR 1-form on C_t with
    prescribed poles at the places at infinity (the 1-form dx∧dy /du).
    A nowhere-vanishing regular 1-form omega on a smooth affine curve
    C with theta_L places at infinity: its divisor on the compactified
    curve is supported at infinity with total degree 2 g_L − 2, so the
    pole orders at the theta_L places sum to 2 − 2 g_L … and they are
    NEGATIVE (poles) unless g_L = 0 — make this precise: omega = dv|_C
    is regular and nonvanishing on C, hence (omega) = −sum_places
    c_P · P with c_P >= 1 wherever it has a pole, and deg(omega) =
    2 g_L − 2 gives 2 g_L − 2 = −sum c_P <= −theta_L ... which would
    force g_L = 0 and theta_L <= 2?! That cannot be right for N >= 2 —
    find the error (omega = dv|_C is the pullback of dt from A^1 by an
    étale map, so it is regular nonvanishing on C — the pole orders at
    infinity are (e_P + 1) where e_P is the ramification of v at that
    place, giving 2 g_L − 2 = −sum (e_P + 1) — this is just
    Riemann–Hurwitz for the compactification of v and says nothing
    new) — and then look for what IS new: the unit-speed structure
    couples the two coordinates: dv/dx_u = 1 means the 1-form
    omega_u := (dx ∧ dy)/du restricted to C_t equals dv|_{C_t} for
    EVERY v with {u, v} = 1, i.e. the residue/period structure of
    omega_u on C_t is that of an exact form of a polynomial. The
    periods of dv over cycles of C_t vanish (v is single-valued); so
    the nonvanishing regular 1-form omega_u = dv on C_t has ALL periods
    zero. On a curve of genus g_L with theta_L punctures, a
    holomorphic 1-form with all periods zero (over H_1 of the open
    curve, rank 2 g_L + theta_L − 1) is exact; that is automatic here.
    Where a constraint appears is at the places at infinity: v has a
    pole of order e_P at each place; the pole orders are bounded by
    the degree D of v … which bounds nothing in N. So the naive
    1-form route is a wash — state this cleanly and move to (2).
(2) The RELATIVE structure: F maps C_t étale onto L_t \ (its
    non-proper points) as an N-sheeted cover; the symplectic form
    identifies the normal structure of the pencil: the family t ↦ C_t
    is the fibration u : A^2 → A^1 with no critical points, and dx∧dy
    trivialises its relative canonical bundle: omega_{A^2/A^1} =
    (dx∧dy)/du is a nowhere-vanishing relative 1-form. On the
    compactified fibration X → P^1 (the pencil of |Z| resolved), the
    relative canonical bundle is K_X − pi^* K_{P^1} = K_X + 2 Z (Z the
    fibre class); its restriction to a fibre is K_{C-bar}, of degree
    2 g_L − 2; the boundary divisor B = X \ A^2 carries the poles.
    Compute K_X + 2Z in terms of the boundary components and Z
    (K_X = −3H + sum E_i on the blow-up; Z = D H − sum mu_i E_i), and
    express 2 g_L − 2 = Z·(K_X + 2Z) = Z·K_X + 2N as a sum of boundary
    contributions; identify which boundary components can carry
    POSITIVE contributions (those are exactly what an upper bound must
    control) and whether the Keller condition (the ramification
    divisor R of Phi is supported on the boundary and R = K_X + 3Z, a
    consequence of Jac F ∈ C^*) bounds them. This is the same object as
    the ceiling flagship's NOETHER-K read on the pencil; re-derive it
    independently and say precisely where Jac F ∈ C^* enters and what
    it forbids.
(3) The DEGENERATION route: the pencil has finitely many atypical
    members (tangent lines to A_F-bar in the pencil direction, lines
    through Sing A_F); their Euler defects sum to nW − N + 1 (Suzuki;
    Hà–Lê nonnegativity), and the coordinator's desk check shows this
    reproduces the (K) ledger. Ask instead about the GENUS drop at
    atypical members and the monodromy of the pencil ON H_1(C_t): the
    Picard–Lefschetz-type data at infinity for a family of curves with
    no affine critical points. Is the monodromy group of the pencil
    (acting on H_1 of the generic fibre, rank 2 g_L + theta_L − 1)
    constrained by the fact that every vanishing cycle lives at
    infinity over the n points of L ∩ A_F and the escapes have the
    meridian cycle type? A bound on the number of atypical members
    (n − 1 + #Sing, from the parametrisation) versus the rank of the
    vanishing-cycle lattice needed to generate H_1 is a candidate
    inequality relating g_L to n and N — write it down and test it on
    the promoted N = 4 (B3) data and on the automorphism case.
(4) NEGATIVE ROUTE: attempt to construct, for a fixed N, a family of
    "Keller-like" pencils (étale, symplectic, non-proper over n points)
    with g_L → ∞ — the ceiling flagship's families (x, x^c y^N) are NOT
    Keller; find where the symplectic condition stops them, or show it
    does not.
(5) Consequences: any bound you prove, priced through MF-EXACT
    (n <= (N − 2 + 2 g_L + theta_inf)/(W − S)), the (B3) list, the
    (B2) delta_aff thresholds, and MOH-CROSS.
Discipline: consume MF-EXACT, LOC-MULT, MF-SHARP, SHARP-CHAU and the
DEG-AF set at their reviewed typings; the ceiling flagship is a
PROPOSAL; MPRIME at banked typing; case (A) is EMPTY; no Z(G) = 1; no
A2 cells. Desk-scale CAS (< 15 min, < 4 GB); state the bounded quantity
of every OPEN you raise; do not edit canonical ledgers; do not inspect
jc2-lean.
Report: xmodel/keller-pencil-genus-opus5-20260902.md
Seal-at-completion; bounded writes; target 25-40KB.
charged_input=xmodel/meridian-floor-sharpen-opus5-20260902.md
charged_input=xmodel/meridian-floor-sharpen-review-gpt55-20260902.md
charged_input=xmodel/n-vs-mapdeg-opus5-20260902.md
charged_input=xmodel/deg-af-vs-n-opus5-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
4fa4b5f60692ade07b3ce45405ab2623edb4ef3aef1174e34beaf2373ce2f2a4  {{LANE_INPUTS}}/meridian-floor-sharpen-opus5-20260902.md
32c043320d11b619ef717cbb2dc5f3ca1ec7756abaa5f470d2ee0fb49dfe7b82  {{LANE_INPUTS}}/meridian-floor-sharpen-review-gpt55-20260902.md
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  {{LANE_INPUTS}}/n-vs-mapdeg-opus5-20260902.md
d7cff053a856a61cc2401585737fc47c093eb6edb0562b1c3f4b82420deeb853  {{LANE_INPUTS}}/deg-af-vs-n-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
```
