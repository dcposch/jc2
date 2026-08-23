# SHEET6-L1.md — settling L1 (merged-pattern l >= 1 inadmissibility)

Status: COMPLETE + PROMOTED (SHEET6-A3L1-REVIEW.md: L1a induction sound, eta-gap closed kill-direction, L1c closed forms re-derived) (2026-08-07, this session; L1 was declared out of scope by
SHEET6-A2P-REVIEW and is settled here). Target: SHEET6-2POLE.md §6c item
L1, the fork-deciding lemma of the two-pole (3,3) td=6 program. Baseline
state: SHEET6-2POLE.md as PROMOTED at 8f3364f (A2P fixes applied: derived
IIb default, §2d M_pole pin; survivor book = residue A + 2 boundary
classes). The mission brief pinned 284d847 (legacy 3+9 book); BOTH books
are adjudicated below (§6). Ground truth: refs/sigray_full.pdf, read
on-page (printed page = pdf page). Engines: cases/twopole_check.py (new
additive PHASE 4 `l1_stage`; phases 1-3 untouched, baseline reproduced)
and cases/l1_ode_check.py (new: exact coefficient solver for Prop 8.1(iv)
at the merge and suffix patterns).

VERDICT: **PARTIAL — proved for every family except one, where it is
FALSE at every level the printed thesis can see.**
(i) L1a (§2, printed-tier): M = 1 propagates from the poles down BOTH
pre-merge chains, forcing mu = (1,1), k = 0, lambda = 0 at any merge.
This upgrades the A2P §2d entry-label kill of residue B to a structural
merge-impossibility (mu = (2,2) cannot occur), re-kills A' independently
of the AF2 pricing tier, and forces the full merged-pattern anatomy into
three families (§0): IIa(l) [both chains at nonzero orbits], ZCH(l) [one
chain at the 0-direction], I(l) [nu = 1] — the last two MISSING from
every prior enumeration.
(ii) L1 HOLDS on the two new families: nu = 1 is empty outright (L1b,
§4: exact calculus on Prop 8.1(iv)); the zero-chain family is dead for
everything reachable (§4b: the one in-caps cell is suffix-DEAD and
ODE-degenerate).
(iii) The remaining family (nu = 3, l = 1 is the only reachable case in
caps, §5-6): L1 FAILS locally. The merged pattern SOLVES Prop 8.1(iv)
with explicit coefficients, unique up to one scale, and no printed
statement bounds l at a two-searrow-orbit vertex: the thesis's own l = 0
arguments (St 9.6's proof, p. 52) all pass through a NORTHEAST root of p,
which a merge vertex does not have (§3). Residue A survives with a
coefficient-level consistent, RIGID template: pole-direction cubes in
ratio 2 + sqrt(3), suffix scale pinned by B = (3/2)A (§5).
Net: legacy book 12 classes -> 4; promoted book unchanged at A's 4 IV
classes (2 robust R3 + 2 boundary R4), now with the merge child proved
UNIQUE: Q(G_m) = (6,12,3,2,5) @ Sigma-lambda = 0. td=6 exclusion remains
conditional on exactly this one rigid configuration; closing it now
provably requires a global (not vertex-local) argument, or a coefficient
construction one level deeper than patterns (§7).

## 0. L1 made precise

Setting (SHEET6-2POLE §1c, §4a): T_{a,pole} = {P_1, P_2}, both row 1 of
table (23) (p. 46); chains merge at an interior G_m in V_{2,a}; (p, q) =
reduced patterns of Prop 8.1 at G_m; mu_i = mult(p, c_i) at the two
chain orbits; l = number of q-orbits at non-roots of p ("resonant
q-orbit family"). L1 as posed in SHEET6-2POLE §6c:

    (L1) At a V_{2,a} merge vertex with mu = (1,1), l >= 1 is
    impossible. [Then l = 0 gives M(G_m) = gcd(2nu, 2nu+1) = 1, and the
    restored Prop 8.4 kills the merge: the whole book closes.]

Sharpened by L1a (§2): mu = (1,1) and k = 0 are forced, and the merged
pattern falls into exactly three families (both chain orbits nonzero /
one chain at the 0-direction / nu = 1), so L1 splits into three claims:
  (L1-IIa) nu >= 2, p = (t-a_1)(t-a_2)|_{t=eta^nu}: l >= 1 impossible.
           M = gcd(2nu,(l+2)nu+1) | 2; = 2 iff nu, l odd.
           [FALSE locally at the unique reachable cell (nu,l) = (3,1), §5]
  (L1-zch) nu >= 2, p = eta(eta^nu - c^nu) (one CHAIN at 0):
           M = gcd(nu+1, (l+1)nu+1) = gcd(nu+1, l), unbounded a priori.
           [TRUE for everything reachable: the only in-caps cell
           (nu,l) = (2,3) is suffix-DEAD and ODE-degenerate, §4b]
  (L1-nu1) nu = 1: M = gcd(2, 2+l) = 2 for l even. [TRUE, §4 = L1b]

## 1. Ground truth assembled (all read on-page this session)

- Prop 4.6 (p. 23): full-pattern ODE d_F p q' - d_{h,F} p' q = ⊖p^{mu_F}
  (11), with root dichotomy (12)/(13) vs (14) and degree dichotomy
  (15)/(16) vs (17).
- Prop 8.1 (pp. 39-41): reduced patterns; (iv) delta p q' - (1-u) p' q =
  ⊖p, delta = d_F/i, u = pi(F); (v) M_F = gcd(deg p, deg q). [(iv) is
  (11) under p_F = p^i, p_{h,F} = p^k q, k = i(mu_F - 1); exponent check
  done exactly.]
- Cor 6.1 (p. 32): at V_a searrow vertices != (0,y), case (16) always
  holds: deg p_{h,F} = (d_{h,F}/d_F) deg p_F; reduced: deg q =
  (1-u) deg p_F / d_F; equivalently the top of (iv) cancels at rho :=
  delta/(1-u) = deg p/deg q. (Its proof also derives, via Prop 6.7 and
  the (12)/(13)-vs-(14) dichotomy, the count deg q >= (mu-1)deg p + #roots.)
- Prop 6.2/6.3 (pp. 29-31): (14) holds at every root whose deeper vertex
  is searrow.
- St 8.2 (p. 41): searrow test deg(q) mult(p,c) > deg(p).
- St 8.4 (p. 42): mult(p,c) | M_G (G = F + c deeper). St 8.5 (p. 42):
  M_G | M_F for G = F° not in V_{2,a} (proof line: p_{h,G} = eta r(eta^nu)).
- Not 8.1 (p. 39): M_F = gcd(deg p_F, deg p_{h_0,F}, ..., deg p_{h_m,F}),
  h_0 = g (Prop 4.2, p. 19), m = m_F. Prop 5.1(i) + Not 5.1/5.2
  (pp. 23-26): pole vertices have m_F = 0, so M_pole =
  gcd(deg p_F, deg p_{g,F}) — the §2d/A2P-front-7 pin. Cross-check found
  here: St 9.6's row-4 entry (p. 51) has M = 2 = gcd(4,6), i.e. the
  thesis's own printed entry M-values ARE this gcd.
- Table (23) (p. 46), row 1 (unique Lambda = 3 row): (D, D_g) = (2,3),
  (deg p, deg p_g) = (2,3), nu = 2. So M_{P_i} = gcd(2,3) = 1.
- St 9.6's proof (p. 52), printed step zoo: mult(p,c) = 1 case: "p(eta) =
  ⊖(eta^nu - c^nu) ... deg(q) = n nu + 1 for some n in N*. From (v) ...
  M_F = 1." mult(p,c) = 2, (II)(a), k != 0: "by Statement 8.2, l = 0."
- Prop 5.3(iii),(v),(vi) (p. 25): pole-pattern ODE k_f p p_g' -
  k_g p' p_g = ⊖ (constant), p squarefree, p and p_g coprime. Solved
  exactly here (row 1): p = eta^2 - w^2 forces p_g = ⊖ eta (eta^2 -
  (3/2) w^2) — the pole's own g-pattern has exactly one "extra" orbit.

### 1a. Two pattern laws (exact consequences of Prop 8.1(iv))

ROOT LAW. At every root of p (any mult m >= 1), q has mult EXACTLY 1;
roots of q away from p are simple; and rho != m at each p-root. Proof:
orders in (iv): if mult(q) = n >= 2 at a common root, both LHS terms
have order >= m + n - 1 > m = RHS order (cancellation only raises
order); n = 0 makes the p'q term order m - 1 < m. So q = eta^{e0} *
rad(p) * (simple extras), and deg q = #distinct-roots + #extras, with
the total pinned by Cor 6.1. Corroborates erratum E7 (SHEET6-AF2): the
printed (II)(a)/(II)(b) q-patterns with (eta^nu - c^nu)^2 are not just
inconsistent with their own Diophantine — they violate Prop 8.1(iv)
itself. E7 upgrades from "cosmetic" to "forced at proof level".

ETA LAW. For nu >= 2: q = eta * r(eta^nu) with eta-multiplicity exactly
1 (nu-equivariance makes e0 ≡ 1 mod nu; the root law caps it at 1 —
whether 0 is a simple chain root of p, as in the ZCH family, or not a
root at all).

## 2. L1a: printed-tier forcing along the chains

**Lemma L1a.** In the two-pole (3,3) configuration:
(a) M_{P_1} = M_{P_2} = 1;
(b) every chain vertex strictly above G_m has M = 1, reduced pattern a
single SIMPLE nu-orbit (dp = nu_F, dq = n nu_F + 1, some n >= 1), and
lambda = 0;
(c) at G_m: mu_1 = mu_2 = 1 and no NON-CHAIN root of p exists (k = 0,
and an eta-factor is excluded UNLESS the 0-direction carries one of the
two chains); q = eta * rad(p)-part * (l extra simple nu-orbits) (root
law + eta law). So exactly three shapes remain: IIa(l): p =
(eta^nu-c_1^nu)(eta^nu-c_2^nu), (dp,dq) = (2nu, (l+2)nu+1); ZCH(l): one
chain at 0, p = eta(eta^nu-c^nu), (dp,dq) = (nu+1, (l+1)nu+1); I(l):
nu = 1, (dp,dq) = (2, 2+l); M(G_m) = gcd(dp,dq) in each case.

[The "no eta-factor" clause of the older draft claims is stated
carefully: an eta-root of p that is NOT a chain is a third searrow
branch (excluded); an eta-root that IS a chain is the legitimate ZCH
family, adjudicated in §4b.]

Proof. (a) Is the §2d pin (SHEET6-2POLE §2d / A2P front 7), grounded
here on-page: Lambda = 3 + 3 forces row 1 at both poles (Prop 5.8 (20),
5.7, 9.1); m_F = 0 at pole vertices (Prop 5.1(i), Not 5.1/5.2); Not 8.1
then gives M = gcd(deg p, deg p_g) = gcd(2, 3) = 1; sanity: the same
formula reproduces the thesis's own printed entry values (row 4: M = 2 =
gcd(4,6), St 9.6).
(b) Induction down each pre-merge segment. Given M = 1 at the deeper
vertex, St 8.4 makes the chain orbit simple in the child's reduced p.
Any OTHER root c' of that p would pass the searrow test (the chain
orbit's own test gives deg q * 1 > deg p, so deg q * mult(p,c') > deg p
a fortiori — St 8.2 leaves no northeast option), creating a second
searrow V_a-branch; the vertex above c' has deg p = i * mult >= 2
(i = deg p of the deeper chain vertex >= 2, St 3.16/St 3.17(i)), so
Prop 6.8 manufactures a pole in a subtree disjoint from both chains — a
THIRD pole. So p is the single simple chain orbit; this is verbatim the
thesis's mult(p,c) = 1 case (St 9.6's proof): dq = n nu + 1 and M_child
= gcd(nu, n nu + 1) = 1. lambda = 0 because a lambda-charge needs a
northeast direction (St 9.3's hypothesis) and none exists. Same
argument at a root 0 (mult i * l_0 >= 2 since i >= 2).
(c) At G_m, repeat (b)'s third-pole argument for every non-chain root of
p (extra orbits, and 0 when neither chain sits there); mu_i | M_{H_i} =
1 (St 8.4); c_1, c_2 lie in distinct nu-orbits (Prop 5.6's proof /
St 3.18: one tree continuation per orbit), so the three listed shapes
are exhaustive; the q-anatomy is the root law + eta law. M-values:
IIa: d | 2nu and d | (l+2)nu+1 give d | 2; ZCH: (l+1)nu+1 =
(l+1)(nu+1) - l gives gcd = gcd(nu+1, l). QED.

Trust: printed statements + the third-pole regularity argument already
sanctioned in SHEET6-2POLE §1c(ii). NOT used: AF2 pricing, AF3 menu,
M-PAT. Consequences:
- Residue B is impossible STRUCTURALLY (mu = (2,2) unreachable) — the
  A2P kill ("entry labels inconsistent with the pin") becomes a merge
  theorem, independent of how B is priced or entered.
- A' is impossible unconditionally (its Sigma-lambda = 1 needs a charged
  pre-merge step; all pre-merge steps are lambda-free) — previously A'
  died only through the AF2-derived IIb repricing (A2P front 7).
- Root merges: re-killed without budgets (they need some mu_i >= 2;
  phase 3 had already found 0 solutions).
- M-PAT (SHEET6-2POLE §4a) is DERIVED for everything that survives: the
  hypothesis tier drops out of the two-pole result entirely.

## 3. Why no printed statement kills l >= 1 at a merge

The thesis proves l = 0 in §9 exactly where a p-root is NORTHEAST: then
St 8.2 forces deg q * mult < deg p, an upper bound deg q < deg p, and
extra q-orbits would break it ("Assume k != 0. Then by Statement 8.2,
l = 0", p. 52 — and every recurrence of that line). At a merge vertex
both p-orbits are searrow chain-carriers: the test points the other way
(deg q > deg p, twice), and NO upper bound on deg q exists. Swept for
an alternative on-page: Prop 4.6's dichotomies, Cor 6.1 (pins deg q to
exactly the value the merge ratio equations already assign — consistent),
Prop 6.2/6.3 ((14) = the root law, satisfied), St 8.2/8.4/8.5 (8.5
explicitly exempts V_{2,a}), Prop 8.2/8.3/8.4 (need regularity/M = 1
below, which the merge child escapes with M = 2), St 9.3/9.4 budgets
(Sigma-lambda = 0 + 2 <= 3 at psi = 2, slack 1), H3q terminal tests
((l)/(m)/psi: satisfied — SHEET6-2POLE §6a). The l extra q-orbits sit at
directions b_j that are NOT roots of p: F * b_j does not exist (St 3.18
requires a root of p_F), so they carry no tree vertex, no cv-vertex, no
lambda, no pole — nothing printed sees them except deg q. That is the
precise structural blind spot; L1-IIa cannot be proved from the printed
statement list.

## 4. L1b: the nu = 1 half HOLDS (and closes an enumeration gap)

The engine's merged menu (and doc §4a) carried the l-family only on the
IIa shape; the nu = 1 I-like merge with l extras — p = (eta-a_1)
(eta-a_2), q = p * s, deg s = l, M = gcd(2, 2+l) = 2 for l EVEN — was
never enumerated, and it IS Q-reachable: phase 4 finds 601 in-caps
parent-pair solutions, e.g. both poles first-step-merging via I(l=2),
n = (3,3), into child Q-shape (1,1,2,4), and via I(l=4), n = (1,1),
into (1/2,1,2,3). These would have been NEW residue classes.

They are all empty at coefficient level. Prop 8.1(iv) at nu = 1 reads
rho p s' + (rho - 1) p' s = c, rho = 2/(2+l), i.e. 2 p s' - l p' s =
c' != 0, i.e.

    (s / p^{l/2})' = (c'/2) p^{-(l+2)/2}.

For l even and p a squarefree quadratic, the partial fractions of
p^{-(l+2)/2} have nonzero 1/(t - a_i) residues (l = 2: -+2/(a_1-a_2)^3;
computed exactly), so the antiderivative has log terms: no rational s
unless c' = 0, contradicting ⊖ != 0. Direct l = 2 check: p s' - p' s
constant implies (p s' - p' s)' = 2(p - s) = 0, so s = p, sharing roots
— contradicts the root law. The e0 = 1 variant (q = eta p s~, 0 among
the extras) fails too: l = 2 solves uniquely to pi = 0 AND s~ sharing a
root of p (both fatal); l = 4's determining polynomial has no admissible
root (cases/l1_ode_check.py, families B/B-eta).

**Lemma L1b.** nu = 1 interior merges violate Prop 8.1(iv): impossible.
(Trust: exact calculus on a printed identity; no hypotheses.)

### 4b. The zero-chain family (L1-zch): everything reachable is dead

If one of the two chains sits at the 0-direction (a legitimate Puiseux
possibility the older M-PAT menu also missed), p = eta(eta^nu - c^nu),
q = eta(eta^nu - c^nu) s(eta^nu), deg s = l, and dividing 8.1(iv) by
eta * pt gives (pt := t - c^nu)

    (rho-1) pt s + (rho-1) nu t pt' s + rho nu t pt s' = c~,
    rho = (nu+1)/((l+1)nu + 1),  M = gcd(nu+1, l).

l = 0 forces rho = 1 and c~ = 0: impossible. l >= 1 solves linearly and
EXACTLY (family Z, l1_ode_check.py): e.g. l = 1: s = t - [nu/(nu+1)]c^nu
(but M = 1: dead by restored 8.4); l = 2, nu odd: s = t^2 -
[2nu/(nu+1)] c^nu t + [nu(nu-1)/(nu+1)^2] c^{2nu}, M = 2, all side
conditions pass — the pattern EXISTS locally. Adjudication is by REACH:
the double ratio equations from row-1 chains admit, within caps, exactly
one ZCH cell, (nu, l) = (2, 3) (first-step closed form n = ((4-l)nu+4)/
(l nu), n odd: only (2,1,5) [M=1, dead] and (2,3,1) [M=3]). The (2,3)
cell dies TWICE over: its merge child (rho,nu,M,kap-bar) = (1/3,2,3,3)
is suffix-DEAD (engine phase 4, 276/276 parent pairs), AND its
coefficient system degenerates (c~ = 0 forced, s = t(t-1)^2 sharing the
p-root and hitting 0: triple violation of the root law). The locally
solvable M = 2 cells (nu odd, l = 2) are not reachable by any in-caps
chain pair. So L1 HOLDS on the zero-chain family for everything
reachable — but by reach + suffix + coefficients, NOT by a printed
statement (the blind spot of §3 applies here too).

## 5. L1-IIa is locally FALSE: the l = 1 pattern exists and is rigid

Reduced ODE at G_m in t = eta^nu (p = pt = (t-a_1)(t-a_2), q = eta pt s,
s = t - b, rho = dp/dq = 2nu/(3nu+1)):

    rho pt s + nu rho t pt s' + (rho - 1) nu t pt' s = c~,   c~ != 0.

Top degree cancels precisely at rho = 2nu/(3nu+1) (consistent with
Cor 6.1 = the merge ratio equations, dp/dq = 6/10 at nu = 3). The rest
is a linear system with UNIQUE solution given the scale sigma := a_1 +
a_2 != 0:

    a_1 a_2 = sigma^2 (nu-1)/(4nu),    b = sigma (nu+1)/(2nu),
    i.e.  a_{1,2} = (sigma/2)(1 ± nu^{-1/2}),

all side conditions holding (roots distinct, nonzero, b not a root,
c~ != 0) — verified exactly for nu = 3, 5, 7, 9 (l1_ode_check.py family
A). For the one reachable M = 2 case nu = 3 (see §6):

    a_{1,2} = (sigma/2)(1 ± 1/sqrt 3),  b = 2 sigma / 3,
    a_1 / a_2 = 2 + sqrt 3.

So the two pole-direction cubes c_i^3 = a_i have PINNED ratio 2 ± sqrt 3,
and the resonant direction e (e^3 = b) is pinned to (2/3) sigma. This is
simultaneously (i) the disproof of any vertex-local L1-IIa — the pattern
exists — and (ii) a rigid, falsifiable prediction for any candidate
counterexample pair. (At (nu, l) = (3,3), (5,3), (3,5), (5,1), (7,1) the
analogous systems also have solutions over C — nonconstant determining
polynomials — but none of these is reachable by the double ratio
equations from row-1 chains: §6. First-step closed forms: IIa: n =
((8-l)nu - 1)/(l nu + 1), n odd: exactly (nu,l,n) = (3,1,5) — the
exhibit; I(nu=1): n = 8/l - 1: (1,2,3) and (1,4,1), dead by L1b; ZCH:
n = ((4-l)nu + 4)/(l nu): (2,1,5) [M=1] and (2,3,1), dead by §4b.
Deeper merges change nothing: every in-caps parent pair lands on the
same cell list with the same unique survivor.)

Suffix-side (same tier): the St 9.7/exhibit suffix shape (42,126,7,3,5)
= St 9.6(iii) case (A) pattern, p = (t-A)^2 (t-B), q = eta (t-A)(t-B),
nu = 7, rho = 7/5 (q-shape forced by the root law — E7 corrected form).
The overdetermined coefficient system (3 residual polynomials in B after
gauge A = 1) has gcd exactly (t - 3/2): unique solution B = (3/2)A, side
conditions fine (family C). The distinguished chain is coefficient-
consistent at BOTH its non-generic vertices, each rigid up to one scale.
The pole vertices are too: p_g = ⊖ eta (eta^2 - (3/2) w_i^2) (§1). What
remains unchecked is one level deeper still: the SUBSTITUTION transport
between levels (only degrees + top coefficients are pinned by printed
St 3.9), i.e. genuine Puiseux realizability — the same tier open for
every campaign survivor, but now with every pattern datum explicit.

## 6. Engine adjudication and per-class verdicts

Reproduction: `python3 twopole_check.py` (phases 1-3 = HEAD engine,
derived-IIb default): 133 pre-merge shapes; 47 970 merges = 46 337
M=1-at-merge + 745 suffix-DEAD + 336 N1 + 552 residue pairs; 2 residue
classes + 6 IV classes (A@0 with 4; B@1 with 2); 0 root merges —
matching SHEET6-A2P-REVIEW front 7's re-run (legacy-flag numbers
163/52389/3+9 per front 6). NEW PHASE 4 (l1_stage; printed-forced tree,
incl. the zero-chain pre-merge and merge variants): 26 pre-merge shapes
(all M = 1, lambda = 0); 18 427 merge children = 17 199 killed
M=1-at-merge + 601 nu=1 (Q-reachable, dead by L1b: children (1,1,2,4),
(1/2,1,2,3)) + 276 ZCH (2,3)-cell (child (1/3,2,3,3): suffix-DEAD, and
ODE-degenerate, §4b) + 351 parent-pairs ALL landing on the single
residue child (1/2,3,2,5)@0 — i.e. within caps (LMAX=8, NUMAX=48,
DEPTH=6, NU1MAX=24) the surviving merged child Q-datum is UNIQUE,
reached at every merge depth, always via IIa(l=1), nu = 3.

Verdicts on the legacy 12 (mission brief, 284d847 book), with the
promoted-book (8f3364f) mapping in brackets:

| # | legacy book entry | verdict | ground |
|---|---|---|---|
| 1 | merge A (6,12,3,2,5)@0 | **OPEN — survives, strengthened** [= promoted A] | §3, §5 |
| 2 | A-IV (1/3,7,3,5)@2 R3 | OPEN (robust; suffix coeff-consistent) [promoted robust] | §5, phase 4 |
| 3 | A-IV (2/3,3s+2,3,2s+2)@2 R3 | OPEN (robust) [promoted robust] | phase 4 |
| 4 | A-IV (1/4,5,4,4)@2 R4 | OPEN (boundary) [promoted boundary] | phase 4 |
| 5 | A-IV (3/4,4s+3,4,3s+3)@2 R4 | OPEN (boundary) [promoted boundary] | phase 4 |
| 6 | merge A' (6,12,3,2,5)@1 | **DEAD — L1a(b)** [A2P: repriced out; now unconditional] | §2 |
| 7 | A'-IV (1/3,7,3,5)@3 | DEAD (with #6) | §2 |
| 8 | A'-IV (2/3,3s+2,3,2s+2)@3 | DEAD (with #6) | §2 |
| 9 | merge B (1/5,6,5,5)@1 mu=(2,2) | **DEAD — L1a(c)** [A2P §2d: entry; now structural] | §2 |
| 10 | B-IV (4/5,5s+4,5,4s+4)@1 R5 | DEAD (with #9) [promoted B-IV] | §2 |
| 11 | B-IV (1/3,4,3,3)@3 R3 | DEAD (with #9) [already repriced out by A2P] | §2 |
| 12 | B-IV (2/3,3s+2,3,2s+2)@3 R3 | DEAD (with #9) [already repriced out by A2P] | §2 |

Plus the three never-enumerated merge children: nu = 1 (1,1,2,4)@0 and
(1/2,1,2,3)@0, Q-live but DEAD by L1b (§4); zero-chain (1/3,2,3,3)@0,
DEAD twice over (§4b). Final surviving book: lines 1-5 only = ONE merge
class, 4 IV classes (2 robust R3 + 2 boundary R4; the boundary pair
dies under any lambda_{(0,y)} >= 1 strengthening, unchanged from A2P).

## 7. Consequences

1. td = 6 status: still conditional on exactly one configuration, now
   maximally pinned. Any counterexample must have: two row-1 poles with
   M = 1 (printed value), lambda-free mu = 1 chains, an interior merge
   (any depth; child Q invariant) into (D,deg p,nu,M,kappa-bar) =
   (6,12,3,2,5) with merged pattern p = (t-a_1)(t-a_2)|_{t=eta^3},
   q = eta (t-a_1)(t-a_2)(t-b), a_1/a_2 = 2 + sqrt 3, b = (2/3)(a_1 +
   a_2); then the §6a suffix through (42,126,7,3,5) with pattern scale
   B = (3/2)A, case-IV terminal R = 3, psi = 2, budget slack 1.
   (SHEET6-2POLE §7.3's "must merge IMMEDIATELY" is corrected: merge
   depth is free; the child datum is what is forced.)
2. What could still close the book (both beyond the printed list):
   (i) GLOBAL accounting of the extra q-orbit: b carries branches of
   h_1 = g^2 - s_0 f^3 with no f-branch; nothing in §§3-9 counts
   h_1-branches at non-p directions — a Newton-polygon/branch budget for
   h_1 at infinity is the natural candidate and would be new mathematics
   in the frame (this is L2's successor, sharpened to one polynomial and
   one direction). (ii) Puiseux transport: impose the actual substitution
   between the pole patterns (pinned, §1) and the merged pattern (pinned,
   §5) at coefficient level beyond top terms; the one free scale on each
   side leaves little room — a finite computation could decide it, but
   it needs machinery (blow-up/Newton data) the thesis does not print.
3. Ledger updates: E7 upgraded (proof-level: violates Prop 8.1(iv), §1a).
   M-PAT: derived for all surviving shapes (hypothesis discharged inside
   the two-pole thread, §2). AF3: superseded at two-pole entries by the
   printed M = 1 (already noted by A2P; now load-bearing via L1a). TWO
   new enumeration-gap classes (nu = 1 and zero-chain merges) found AND
   closed (L1b, §4b) — worth porting the I(l)/IIa(l)/ZCH(l) menu review
   to any future multi-pole engine.
4. The historical pattern (SHEET6-2POLE §3) sharpens: the multi-pole
   case does not just resist the uniqueness-based kills — it bottoms out
   in a single rigid coefficient-consistent local model, i.e. an
   existence question, exactly the layer (actual Puiseux data) where
   Domrina-Orevkov's splice methods also stopped.

## 8. Trust perimeter

L1a: printed statements (Not 8.1, Prop 5.1(i)+Not 5.1/5.2, table (23),
Prop 5.8/5.7/9.1, St 8.2, St 8.4, St 3.16, St 3.17(i), St 3.18, St 9.3,
St 9.6-proof) + the Prop 6.8 third-pole argument (SHEET6-2POLE §1c
tier). L1b + §5: exact arithmetic on Prop 8.1(iv)/Cor 6.1 (printed
identities), machine-verified (l1_ode_check.py), no hypotheses. Phase 4
caps as in §6; the l1 pre-merge tree is a strict subset of baseline
phase 1, itself cap-stable per SHEET6-2POLE §8. Unmodeled, unchanged:
pi-positivity (H1 tier), absolute-degree (P-)realizability across the
merge, h-family realizability above pattern level, lambda_{(0,y)}
(would kill only the 2 boundary classes). The (I)/(II)/(III) case-label
bookkeeping at the merge vertex carries no arithmetic weight here: the
double ratio equation used is common to (I)/(II) ((a)-(d), p. 50), and a
(III)-form merge would need G_m in V_{1,a} with u > alpha_{j-1}, which
the two-orbit structure of p_{G_m} (distinct orbits, St 3.18) excludes
on the same grounds the doc already used for St 8.5's V_{2,a} exemption.

## 9. Reproduction

    cd cases && python3 twopole_check.py          # phases 1-4, ~4 min
    python3 twopole_check.py l1only               # phase 4 alone, ~40 s
    python3 l1_ode_check.py                       # coefficient checks, ~5 s
