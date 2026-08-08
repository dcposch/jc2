# SHEET6-TEMPLATE.md — coefficient-level lift of the two-pole rigid template

Status: PROMOTED WITH CORRECTIONS (SHEET6-LT-REVIEW.md: fronts 3-5 confirmed; kill chances (i)/(iv) exponent-trivial so 3 genuine not 5; E11 REFUTED as erratum (follows from Prop 8.1(i)+3.17(i)+8.4, which also forces m_Fs=2 printed-tier); R1 spec SUPERSEDED by LT-REVIEW front 7 redesign: tower g^2 - s0*f^3 per Prop 4.2 (gauge a=0), R6 first, co-stage g, x-side lead, terminal J-closure). Original status: COMPLETE (2026-08-07, UNREVIEWED). Target: SHEET6-L1.md §7.2 — the lift from
Q-data + merge-local coefficients (SHEET6-2POLE.md §6a exhibit, L1c rigid
solution) to an explicit candidate Puiseux/Newton-tree data set for the
distinguished sheet-6 counterexample template, and the edge-by-edge
coefficient consistency sweep (St 3.9 transport). Ground truth:
papers/sigray_full.pdf read on-page. Engine: cases/template_lift.py (new,
additive; exact arithmetic over Q(sqrt 3) via Fraction pairs).

VERDICT: **FORMAL-CANDIDATE — the lift EXISTS and is STRICTLY RIGIDER than
L1 left it.** The coefficient-level sweep does not kill the template; it
(a) proves the naive h-tower reading (m_{F_s} = 1) IMPOSSIBLE by h1-branch
counting (16 <= 7 violation of St 3.11(i)+St 8.3(ii), sec 2c-E2), forcing
approximate-root tower depth m = 2 at the suffix vertex with
(k1,l1) = (3,4) UNIQUE (sec 2c-E3) — h1 = g^2 - s0(f-a)^3 "behaves like
f^{4/3}"; (b) RE-DERIVES the L1c rigid coefficients (a1a2 = sigma^2/6,
b = 2sigma/3) from pure branch counting, independently of the Prop 8.1(iv)
ODE (sec 2c-E4: the h2-collapse W(t) = t(t-b)^3 - (t-a1)^2(t-a2)^2 must
drop to degree 1); (c) passes three further nontrivial kill opportunities
by exact cancellation over Q(sqrt3): pole-lead cancellation m_i^2 =
s0*lam_i^3 automatic, h2-lead transport 27a_i(a_i-b)^3 =
sigma^3(a_i - (3/4)sigma) exact at both poles, every h-branch count
edge-EXACT (leak-free) for h in {f-a, g, h1, h2} on every template edge.
New pinned data: h2 = h1^3 - s1(f-a)^4 with resonant direction
b2 = (3/4)sigma at G_m; pole h1-pattern eta^2 - (4/3)w_i^2; w_i^4 pinned
by the merge data (sec 2c-E5). Bonus: in the minimal-tower branch the
FIRST-STEP merge is restored (m-growth lock, sec 2c-E2). Residual
problem set (sec 3): 6 items, all transport/global-tier, none
vertex-local. Engine: cases/template_lift.py — 11 check families,
46 checks, 0 FAIL, exact arithmetic.

## 0. Setting and conventions

Chain (root at the bottom; ° moves toward the root, + c away from it):

    P_1, P_2  (pole vertices, deepest)      pi = 37/42, kappa = 42
       \   /   two merge edges, mu=(1,1), n=(5,5)
        G_m   (merge vertex, V_{2,a})       pi = 16/21, kappa = 21
         |     suffix edge, mu=2 (IIa k=1), n=10
        F_s   (St 9.6(iii)(A) shape)        pi = 2/7,   kappa = 7
         |     terminal edge, case IV, R = 3, psi = 2
       (0,y)  =: R (root)                   pi = 0,     kappa = 1

Q(F) = (D_F, deg p_F, nu_F, M_F, kappa_F(1-pi(F))): P_i = (2,2,2,1,5),
G_m = (6,12,3,2,5), F_s = (42,126,7,3,5), R = (42,126,1,M_R,1).
Patterns p_{h,F} are the ACTUAL top polynomials of Not 3.10 (specific,
not up-to-constant); "reduced" refers to Prop 8.1's p_F = ⊖p^i,
p_{h_m,F} = p^k q, k = i(mu_F - 1), i = deg(p_F)/M*_F. h-tower
(Prop 4.2, T_a^+ everywhere on the chain since all D > 0): h_0 = g,
h_{j+1} = h_j^{k_j} - s_j(f-a)^{l_j}, (h_j^+)^{k_j} = s_j((f-a)^+)^{l_j}
at vertices where the tower is alive (j < m_F); m_F = the j at which
delta_j := kappa(d_F + d_{h_j,F} - alpha_j d_F - 1 + u) hits 0;
mu_F = alpha_{m_F} = sum_{j<m}(k_j-1)l_j/k_j. All arithmetic below is
exact over Q(sqrt3) (a_{1,2} = (sigma/2)(1 ± 1/sqrt3)).

## 1. The genome: full explicit tree data

### 1a. Exponent ladder and global frame

Global: type (alpha,beta) = (2,3); (k_f,l_f) = (126,42), (k_g,l_g) =
(189,63); deg(f-a) = 168, deg g = 252; td = 6 = Lambda(P_1)+Lambda(P_2)
= 3+3. Branch chart: (0,y)-side Puiseux series y = sum c_j x^{-j},
j in (1/42)N increasing, common root kappa = 42.

Ladder (kappa_F = product of nu's root-to-F; pi from kappa_F(1-pi) =
kappa-bar; d = D/kappa; ALL verified against St 3.17(ii) and the n-data):

| F   | pi(F) | kappa | nu | d_F  | D_F | d_g   | D_g | d_h1 | d_h2  | m_F |
|-----|-------|-------|----|------|-----|-------|-----|------|-------|-----|
| R   | 0     | 1     | 1  | 42   | 42  | 63    | 63  | 56   | 138   | >=3 |
| F_s | 2/7   | 7     | 7  | 6    | 42  | 9     | 63  | 8    | 138/7 | 2   |
| G_m | 16/21 | 21    | 3  | 2/7  | 6   | 3/7   | 9   | 8/21 | 8/7   | 1   |
| P_i | 37/42 | 42    | 2  | 1/21 | 2   | 1/14  | 3   | 1/7  | 3/7   | 0   |

d + d_g = 1 - pi holds exactly at P_i (5/42; Prop 4.1 equality = pole);
delta-table (Prop 4.2): delta_j(P_i) = (0): m=0. delta(G_m) = (10, 0):
m=1. delta(F_s) = (100, 30, 0): m=2. delta(R) = (104, 34, 4, ...): the
root tower continues to depth >= 3 with (k_2,l_2) = (7,23)
(d_h2/d = 138/42 = 23/7); root depth m_R is residual (sec 3, R4).

### 1b. Vertex data (patterns with explicit coefficients)

Scales: sigma (merge), A (suffix), w_1, w_2 (poles), c0 (root direction);
leads S_* (f-a), G_* (g), H_* (h1), K_* (h2); tower constants s0, s1.
a_{1,2} = (sigma/2)(1 ± 1/sqrt3) (a1+a2 = sigma, a1a2 = sigma^2/6,
a1/a2 = 2+sqrt3), b = (2/3)sigma, b2 = (3/4)sigma, B = (3/2)A.

R = (0,y): p = S_R (eta-c0)^126; p_g = G_R (eta-c0)^189, G_R^2 = s0 S_R^3
  (forced, sec 2c-E1); p_h1: mult(.,c0) = 168, level d_h1 = 56;
  p_h2: mult(.,c0) = 414, level 138.
F_s (M* = 21, i = 6, mu = 25/6, k_{h2} = 19):
  p    = S_F [(eta^7-A)^2(eta^7-B)]^6            (deg 126)
  p_g  = G_F [(eta^7-A)^2(eta^7-B)]^9            (deg 189), G_F^2 = s0 S_F^3
  p_h1 = H_F [(eta^7-A)^2(eta^7-B)]^8            (deg 168), H_F^3 = s1 S_F^4
  p_h2 = K_F [(eta^7-A)^2(eta^7-B)]^19 eta(eta^7-A)(eta^7-B)   (deg 414)
  reduced (p,q) = ((t-A)^2(t-B), eta(t-A)(t-B))|_{t=eta^7}, rho = 21/15;
  B = (3/2)A unique (Prop 8.1(iv), L1 family C re-verified).
G_m (M* = 6, i = 2, mu = 3/2, k_{h1} = 1):
  p    = S_M [(eta^3-a1)(eta^3-a2)]^2            (deg 12)
  p_g  = G_M [(eta^3-a1)(eta^3-a2)]^3            (deg 18), G_M^2 = s0 S_M^3
  p_h1 = H_M eta [(eta^3-a1)(eta^3-a2)]^2 (eta^3-b)          (deg 16)
  p_h2 = (sigma^3/27) H_M^3 [(eta^3-a1)(eta^3-a2)]^6 (eta^3-b2) (deg 39)
  reduced (p,q) = ((t-a1)(t-a2), eta(t-a1)(t-a2)(t-b))|_{t=eta^3}; the
  L1c solution, unique given sigma (re-verified).
P_i (M* = 2, i = 1, m = 0):
  p    = lam_i (eta^2 - w_i^2)
  p_g  = m_i eta (eta^2 - (3/2)w_i^2)   [2 p p_g' - 3 p' p_g = 3 lam m w^4]
  p_h1 = -(3/4) s0 lam_i^3 w_i^4 (eta^2 - (4/3)w_i^2)   (deg 2; sec 2c-E5)
  p_h2 = (p_h1)^3 = [-(3/4)s0 lam_i^3 w_i^4]^3 (eta^2-(4/3)w_i^2)^3 (deg 6)
  with m_i^2 = s0 lam_i^3 (forced AND automatic, sec 2c-E5).

### 1c. Edge data (n, mu, i, case labels, free dead-stretch coefficients)

| edge      | n  | steps at 1/kappa_G | mu | Prop 9.3 | free coeffs (grid) |
|-----------|----|--------------------|----|----------|--------------------|
| R->F_s    | -  | 2 at 1/7           | 6* | IV (terminal read up) | none (no integer in (0,2/7)) |
| F_s->G_m  | 10 | 10 at 1/21         | 2  | II(a) k=1, l=0 | 3 at 9/21,12/21,15/21 |
| G_m->P_i  | 5  | 5 at 1/42          | 1  | II(a) k=0, l=1 (merged IIa(3,1)) | 2 at 17/21,18/21 |

n == -kappa-bar mod nu checks: 10 == 1 mod 3, 5 == 1 mod 2; off-grid
intermediate coefficients vanish (a nonzero one would relocate the
characteristic exponent and change Q); on-grid ones are free template
parameters (7 total). *mu on R->F_s: mult(p_R, c0)/M*-bookkeeping at the
root; the terminal step is case IV with R = deg p_{F_s}/d_R = 3, psi = 2.

### 1d. Branch/puncture bookkeeping (y-side)

126 = k_f series: puncture P_1 (x-degree 42, all 42 conjugate series,
g-pole order 3), P_2 (same), B-side punctures totaling 42 series (6 per
eta-direction of the B-orbit at F_s; g finite there; carriers of the
lambda_{F_s} = 2 charge). Conjugacy audit: mu_42-action distributes P_i's
42 series as 7 x 3 x 2 over the (A-orbit x a_i-cube-orbit x ±w_i) tree
directions — deg p at each vertex = series through the prefix: 126/12/2
check exactly. h1-directions with NO f-branch: b-orbit at G_m (3
directions, 1 h1-series each, +1 at the eta = 0 direction: 12+3+1 = 16 =
deg p_{h1,G_m}); h2: b2-orbit (36+3 = 39). x-side: l_f = 42 series,
carries the psi = 2 charge (not modeled here; residual R5).

## 2. The consistency sweep: edge-by-edge coefficient transport

### 2a. What the printed statements pin (all read on-page this session)

Per edge (shallow F, deep G = F + c), for EVERY polynomial h:
St 3.9(i)-(iii): mult(p_{h,F},c) = deg(p_{h,F*c}); the LEADING coefficient
of the deeper pattern = the mult-th Taylor coefficient of the shallower
one at c; d drops by mult/kappa per elementary step. St 3.11(i): branch
counts are MONOTONE (deg at deeper <= mult at shallower) — the count law.
St 8.3(ii): EQUALITY of counts for tower members h_j, j <= m_F. Composite
edges: leads transport unchanged along dead stretches (single-rooted
patterns: Taylor coeff at own root = lead). Per vertex: Prop 8.1(i)-(v)
(reduced ODE + M = gcd), Prop 4.2 (tower + delta-recursion), Prop 5.3
(pole ODE, squarefree, coprime), Prop 4.6 (11)-(17). NOT printed, NOT
used: anything pinning sub-leading pattern coefficients across edges.

### 2b. Vertex-local solves (recap; all re-verified in template_lift.py)

Poles: 2 p p_g' - 3 p' p_g = ⊖ with p = eta^2 - w^2 forces p_g =
⊖ eta(eta^2 - (3/2)w^2), ⊖ = 3w^4 != 0. G_m: L1c unique given sigma.
F_s: B = (3/2)A unique (computed here in the honest i-normalization
p = phi^6 psi^3, q = eta phi psi, phi = eta^7 - A, psi = eta^7 - B:
identity 3 phi psi - (9/7)eta phi' psi + (6/7)eta phi psi' = (9/2)A^2,
constant iff B = (3/2)A — same answer as L1's t-form). Root: p_g,R
proportional to p_R^{3/2} forces the single g-direction e0 = c0 and
G_R^2 = s0 S_R^3 once h1 enters the St 8.3 family (E1 below).

### 2c. Edge transports, solved in order (the new content)

E1 (terminal edge, g and h1). St 8.3(ii) at F_s (m_{F_s} >= 1):
deg p_{g,F_s} = 189 = mult(p_{g,R}, c0): exact, leak-free. Once
m_{F_s} = 2 (E2): deg p_{h1,F_s} = mult(p_{h1,R}, c0) must hold; if the
level-126 tops of g^2 and s0(f-a)^3 did NOT cancel at R, p_{h1,R} would
be ∝ (eta-c0)^378 with mult 378 != deg p_{h1,F_s}: St 8.3(ii) forces
G_R^2 = s0 S_R^3 (root-lead cancellation).

E2 (suffix edge, h1 count — the m_{F_s} dichotomy). m_{G_m} = 1 is FORCED
(m = 0 only at poles, m monotone along depth). So p_{h1,G_m} = p q,
deg 16, by Prop 8.1(ii) (i = 2, mu = 3/2, k = 1; deg q = 10 is forced by
the printed merge ratio 9.3(b), L1a/L1c). IF m_{F_s} = 1: i_{F_s} = 2
(M* = gcd(126,189) = 63), p_{h1,F_s} = p63 q15 with mult at c_m =
6 + 1 = 7. St 3.11(i) composed along the edge: 16 <= 7, FALSE.
**m_{F_s} = 1 is impossible.** Corroboration, printed-tier: St 8.3's
proof line "F ≺ G" (Not 4.1: m_F < m_G, F the deeper vertex) gives
strict m-growth along every chain edge: m_{G_m} = 1 < m_{F_s} directly.
Hence m_{F_s} = 2: h1 is still tower-ALIVE at F_s: p_{h1,F_s} =
⊖ p21^{6 l1/k1}, and the thesis's own silent normalization in St 9.6
("i = deg(p_G)/M_G = j", p. 52, never justified in print) is CORRECT —
our count argument supplies its missing proof. M*_{F_s} =
gcd(63, 126 l1/k1) = 21 forces k1 in {3,6}.

SIDE THEOREM (merge depth locked to tower depth). In the minimal-tower
branch (m_{G_m} = 1), strict m-growth leaves no room for pre-merge
chain vertices (they would need 0 = m_{P_i} < m < m_{G_m} = 1): the
merge is the FIRST °-step of both chains. SHEET6-2POLE §7.3's original
"must merge immediately" — retracted by L1 §7.1 at Q-level — is
RESTORED at the lift level for this branch; deeper merges live only in
the deeper-tower variants (R6 below), with depth_premerge locked to
m_{G_m} - 1 per chain.

E3 (suffix edge, h2 count — (k1,l1) = (3,4) UNIQUE in the minimal-tower
branch m_{G_m} = 1). h1-count needs
deg p_{h1,G_m} = 16 <= mult(p_{h1,F_s}, c_m) = 12 l1/k1, i.e.
l1/k1 >= 4/3. At G_m the tower is dead at j = 1, so p_{h2,G_m} is the
top of h1^{k1} - s1(f-a)^{l1} there: levels k1 d_{h1,G_m} = 8k1/21 vs
l1 d_{G_m} = 6l1/21 cancel iff 4k1 = 3l1, i.e. (k1,l1) = (3,4). For any
other admissible (k1,l1) (l1/k1 > 4/3), the f-side wins and p_{h2,G_m} ∝
p_{G_m}^{l1}, deg 12 l1, while mult(p_{h2,F_s}, c_m) = 2 i(mu2 - 1) + 1
= 8 l1 + 7 (k1=3) or 10 l1 + 7 (k1=6): 12 l1 <= 8 l1 + 7 forces
l1 <= 7/4 — contradiction. **(k1,l1) = (3,4)**: h1 "is" f^{4/3};
deg p_{h1,F_s} = 168, both h1- and h2-counts EXACTLY leak-free (16 = 16).

E4 (suffix edge, h2 collapse — independent re-derivation of L1c). With
(3,4), the level-8/7 top at G_m is P^6 [H_M^3 eta^3(eta^3-b)^3 -
s1 S_M^4 P^2], P = (eta^3-a1)(eta^3-a2). H_M^3 = s1 S_M^4 transports
from F_s (E6), so the bracket = H_M^3 W(eta^3),
    W(t) = t(t-b)^3 - (t-a1)^2(t-a2)^2.
h2-count at the suffix edge: deg p_{h2,G_m} = 36 + deg_t W * 3 <=
mult(p_{h2,F_s}, c_m) = 39 forces deg_t W <= 1:
    t^3: 2 sigma - 3b = 0        <=> b = (2/3) sigma
    t^2: 3b^2 - sigma^2 - 2 a1a2 = 0  <=> a1 a2 = sigma^2/6.
These are EXACTLY the L1c coefficients — re-derived from branch counting
alone, with no use of Prop 8.1(iv). Two independent derivations agree.
Result: W = (sigma^3/27)(t - (3/4)sigma): p_{h2,G_m} =
(sigma^3/27) H_M^3 P^6 (eta^3 - b2), b2 = (3/4)sigma, deg 39 = 39 EXACT.

E5 (merge edges, h1 at the poles). mult(p_{h1,G_m}, c_i) = 2 (pq: 1+1),
so deg p_{h1,P_i} <= 2. At P_i the tower is dead at j = 0: p_{h1,P_i} =
top of g^2 - s0(f-a)^3: levels 2d_g = 3d = 1/7 equal; the degree-6
polynomial m_i^2 eta^2(eta^2-(3/2)w_i^2)^2 - s0 lam_i^3 (eta^2-w_i^2)^3
must drop to degree <= 2: eta^6-coefficient m_i^2 - s0 lam_i^3 = 0 is
FORCED — and it is AUTOMATIC: m_i = G_M 27 c_i^6 (a_i-a_j)^3, lam_i =
S_M 9 c_i^4 (a_i-a_j)^2 (St 3.9(ii) Taylor transports), so m_i^2 =
s0 lam_i^3 <=> G_M^2 = s0 S_M^3, the transported tower relation. With it,
in z = eta^2: z(z-(3/2)w^2)^2 - (z-w^2)^3 = -(3/4)w^4 z + w^6 (the z^2
term cancels IDENTICALLY): p_{h1,P_i} = -(3/4) s0 lam_i^3 w_i^4
(eta^2 - (4/3)w_i^2), deg 2 = 2 EXACT. Lead transport (St 3.9(ii)):
    H_M 9 c_i^5 (a1-a2)^2 (a_i - b) = -(3/4) s0 lam_i^3 w_i^4
pins w_i^4 (nonzero, solvable: a_i != b) — no obstruction, no freedom:
    w_i^4 = -(4/3) H_M (a_i-b) / (243 s0 S_M^3 (a1-a2)^4 a_i^2 c_i).

E6 (lead-coherence across edges; all automatic, verified exactly).
Taylor factors: F_s->G_m: (7c_m^6)^N (A-B)^{N/2 or N/3...}: S_M =
S_F 7^12 A^16 c_m^2/2^6, G_M = -G_F 7^18 A^24 c_m^3/2^9, H_M =
H_F 7^16 A^21 c_m^5/2^8 (c_m^7 = A). Then G_M^2 - s0 S_M^3 =
(G_F^2 - s0 S_F^3) x (common factor): the tower relation transports to 0
AUTOMATICALLY; likewise H_M^3/S_M^4 = H_F^3/S_F^4 = s1 exactly (the
c_m^7 = A reduction is what makes it close). G_m->P_i for h2: p_{h2,P_i}
= (p_{h1,P_i})^3 (levels 18/42 > 8/42: no cancellation), and its lead
must equal the 6-Taylor coefficient of p_{h2,G_m} at c_i:
    [H_M 9 c_i^5 (a1-a2)^2(a_i-b)]^3
      = (sigma^3/27) H_M^3 (3c_i^2)^6 (a1-a2)^6 (a_i-b2)
    <=>  27 a_i (a_i - b)^3 = sigma^3 (a_i - (3/4) sigma),
a NEW closed condition on the L1c data. It HOLDS exactly: both sides =
sigma^4 (2 sqrt3 - 3)/12 at a_1 (and the sqrt3 -> -sqrt3 conjugate at
a_2). Verified over Q(sqrt3). A failure here would have killed the
template; it passes with no slack.

E7 (count/d-ladder matrix). For h in {f-a, g, h1, h2} and every edge,
the branch counts are EXACT (mult upstream = deg downstream) and the
d-drops add up exactly (e.g. h2 on the suffix edge: 10 steps x 39/21 =
130/7 = 138/7 - 8/7). Every one of the 16 cells closes. See engine
output; any single cell failing would have been a DIES-AT-EDGE verdict.

## 3. Verdict and residual problem set

**FORMAL-CANDIDATE.** No edge of the template dies at coefficient level.
The sweep had five independent chances to kill it and each closed by an
exact identity rather than by slack: (i) pole-lead cancellation forced
AND automatic (E5); (ii) h2-collapse forced to degree 1 and the L1c
coefficients are exactly the collapsing values (E4) — the ODE-derivation
and the count-derivation of a1a2 = sigma^2/6, b = 2sigma/3 AGREE; (iii)
the (F_i) identity 27a(a-b)^3 = sigma^3(a - 3sigma/4) holds over
Q(sqrt3) at both poles (E6); (iv) H^3/S^4-invariance closes via
c_m^7 = A; (v) all 12 (edge,h) count/d-ladder cells are exact. The lift
also STRENGTHENS the template: forced new data (tower (2,3),(3,4);
m = 0/1/2/(>=3) at P/G_m/F_s/R; h2-direction b2 = (3/4)sigma;
p_{h1,P_i} = ⊖(eta^2-(4/3)w_i^2); w_i^4 formulas; deg_y h1-corner
(k_h1,l_h1) = (4/3)(k_f,l_f) = (168,56)).

Residual problem set (everything that still stands between this genome
and an actual pair (f,g) — or its refutation):

R1 (CANCELLATION-DEPTH / Puiseux transport; sharpest residual). The
  tower memberships force EXACT sub-top cancellation depths of
  g^2 - s0(f-a)^3: at R from level 126 down to 56 (70 kappa-units), at
  F_s from 18 down to 8 with the quotient pattern the PURE POWER
  ⊖p21^8, at G_m from 18/21-level to 8/21 with quotient p*q (the b-orbit
  surfacing). These are conditions on the free dead-stretch coefficients
  (sec 1c: 7 of them) and on sub-pattern tails — finitely many unknowns,
  polynomially many conditions; not decidable from printed statements;
  THE natural next computation (sec 4).
R2 (h-Newton budgets). h1's own branch bookkeeping at infinity: y-side
  count 168 through c0 + b-orbit + B-side leaks vs deg_y h1 = 56-corner
  arithmetic; same for h2 (corner (7/2)(126,42) -> (441,147), root level
  138). A contradiction here would be an L2-successor theorem; the
  in-template cells all closed, so any kill must use x-side + global
  degree data not modeled in T_a.
R3 (lambda/psi realizability). The B-orbit cv-vertices behind
  lambda_{F_s} = 2 and the x-side vertex pricing psi = 2 (St 9.3/9.4
  budgets pass with slack 1; the cv-side patterns are unconstructed).
  SHEET6-LROOT.md (parallel session) sharpens the x-side half: a single
  x-side cv vertex, kappa_G = 1, one unsplit Puiseux cluster below
  height R = 3 — merge that pin with this genome when constructing the
  42 x-side series.
R4 (root tower / M_R arithmetic). delta(R) = (104, 34, 4, ...): the root
  tower runs to depth >= 3 with (k2,l2) = (7,23); M_R = gcd(3,
  deg p_{h3,R}) in {1,3}; if the two-pole-restored Prop 8.4 layer can be
  pushed to the root vertex itself, M_R = 1 would need re-examination —
  currently no printed statement decides it (H3 KEY OBSERVATION: the
  Bezout run at M >= 2 reproduces case IV (m), no contradiction).
R5 (Jacobian closure). Nothing above uses J(f,g) = 1 beyond the tower
  identities; the final candidate must of course satisfy it globally.
R6 (deeper-tower variants). The sweep pins the MINIMAL assignment
  m_{G_m} = 1. The alternative m_{G_m} = 2 (tower alive at j = 1 at the
  merge; b-orbit shifted into h2's pattern; pre-merge depth 1 allowed)
  is partially killed here: (k1,l1) = (1,3) dies by a level
  contradiction (d_h1 = 3d requires no cancellation in g^2 - s0 f^3,
  but the tower-0 relation forces strict cancellation), and l1 > 3k1
  dies by the h2-count at the pole edges (2 l1 <= 2 + 2 l1 - 2 l1/k1
  forces l1 <= k1); the window 4/3 < l1/k1 < 3 with delta-integrality
  6 l1/k1 in N survives these tests and would need the same E3-E6
  mechanism run one tower level higher (finite recursion, same shape;
  not run here — expected to close or reproduce an isomorphic genome).

## 4. Compute sizing (direct algebraic verification/refutation)

Naive Ansatz (msolve on coefficients of (f,g) with Newton rectangles
(126,42), (189,63)): 127*43 + 190*64 = 5461 + 12160 ~ 17.6k unknowns,
J(f,g) = const gives ~(314)(104)/1-ish ~ 32k bilinear equations. NOT
runnable — two orders of magnitude past the farm's msolve envelope.

Template-constrained Ansatz (the right formulation): build f-a from its
PINNED y-side branch data — 2 punctures P_1, P_2 with 42-conjugate
series each, prefix structure fully pinned by the genome up to: sigma, A
(one of which is a global scale: 1 essential), c0, w_1, w_2 (pinned to
4th roots by E5), 7 dead-stretch coefficients, B-side/x-side tail data.
Stage k imposes "the elementary symmetric functions of the 126 series
truncated at x^{-k/42} are polynomials in x" (Prop 3.1 direction) plus
the R1 cancellation depths: each stage is LINEAR in the O(1) new
unknowns per level with ~168 conditions per level; ~50-100 levels to
exhaust deg f = 168. Estimated: ~10^2-10^3 unknowns total over Q(sqrt3),
processed level-by-level (lib/jc.py fastcoef-style staging; no Groebner
until a terminal nonlinear core of expected size <= 20 vars, msolve-easy)
— hours-to-days on the existing farm, NOT a big-iron run. The FIRST
obstruction, if any, will appear as an inconsistent linear stage at the
R1 depths (levels 3..10 past F_s) — a cheap, decisive first experiment:
prototype ~300 lines on top of lib/jc.py, JC_BACKEND=flint for the
series products (degree-168 polynomial arithmetic over Q(sqrt3) embeds
as pairs; flint handles the Fraction bignums).

## 5. Consequences for the td = 6 fork

1. The distinguished configuration SURVIVES one full level deeper than
   SHEET6-L1 left it, and is now rigid to the point of having NO free
   discrete data: every branch datum, tower exponent, and lead relation
   is pinned; the continuous data is (scale) + (w_i 4th-root choices) +
   7 dead-stretch coefficients subject to R1.
2. The thesis's silent i = deg(p_G)/M_G normalization in St 9.6 (p. 52)
   acquires its missing proof here (E2) — but ONLY via m_{F_s} = 2,
   which no printed statement supplies. Ledger candidate E11 (E10 taken
   by SHEET6-LROOT.md): St 9.6's
   proof implicitly assumes the h-tower is alive to depth 2 at the
   child; provable via the h1-branch count, this document.
3. The h1-blind-spot diagnosis of L1 sec 3 is now sharper: the resonant
   b-orbit is REAL h1-content (3+1 h1-branches with no f-branch), it
   propagates (b2-orbit for h2), and counting it is exactly what forced
   the tower and re-derived the rigid coefficients. The natural L2' =
   "h-branch budget at infinity" is formulated and PASSES locally; only
   its global/x-side half (R2) remains as a potential kill.
4. Next decisive moves, in order of cost: (a) run the R1 staged linear
   system (sec 4) — cheapest decisive experiment; (b) do the x-side/R2
   Newton-budget arithmetic on (168,56)/(441,147); (c) root-tower M_R
   arithmetic (R4). Any one could still kill td = 6's last
   configuration; all three surviving would make this the strongest
   sub-9 candidate structure known in the Sigray frame (the td = 9
   (48,64) tree being the proven consistent one).

## 6. Trust perimeter

Printed statements used, all read on-page this session: Not 3.9/3.10,
Prop 3.1, St 3.7-3.18 (esp. 3.9, 3.11, 3.12, 3.16-3.18), Prop 4.1-4.6
((9),(10),(11),(16), delta-recursion), Prop 5.1-5.8 + (18)/(19) +
table (23), Not 8.1, St 8.1-8.5, Prop 8.1 ((i)-(v), incl. the proof line
mult(p_h,c) = (mu-1)mult(p,c)+1), Not 9.1-9.3, St 9.1-9.6, Prop 9.2-9.3.
Inherited: SHEET6-L1 (L1a/L1c, promoted), SHEET6-2POLE (config layer,
promoted), H3q psi-budget. NEW derivations here (unreviewed): E1-E7 of
sec 2c; the m-monotonicity along depth (from St 8.5's proof structure /
Not 4.1 nesting — used only qualitatively: m = 0 iff pole, m
nondecreasing toward the root); leak-free lead composition along dead
stretches (single-rooted patterns, St 3.9(ii) iterated). Caveats: (a)
composite-edge St 8.3(ii) equalities are used as in the thesis's own
chain steps; (b) the h2-anatomy at G_m assumes the generic reading of
"p_{h,F} is the top p_j" for the DEAD tower member (h2 at G_m is not a
tower element there; its pattern is computed from the polynomial
identity h2 = h1^3 - s1(f-a)^4, which is definition-level, not
hypothesis-level). No unproven campaign hypotheses (M-PAT etc.) enter:
L1a discharged them for this configuration.

## 7. Reproduction

    cd cases && python3 template_lift.py     # ~2 s, 42 checks, exact
    python3 l1_ode_check.py                  # L1 locals (unchanged)
    python3 twopole_check.py l1only          # phase-4 funnel (unchanged)
