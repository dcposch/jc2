# Flagship, hostile: EXACT-N — is the sub-tree of the last major disc a STAR, and is N an exact function of the Moh skeleton?

PROPOSAL (coordinator, Fable 5.1, 2026-09-02 ~16:55Z; unreviewed; prove
or refute). Setting: Keller pair (f, g) in Moh's gauge (monic in y,
deg = deg_y, two points at infinity), degree-minimal, NU-TWO; m = deg f
= Kd, n = deg g = Ke, gcd(d,e) = 1; t = x^{-1}; Puiseux roots rho_j of
g (unshifted) and tau_i of g - c_2 (generic c_2); lambda_h^{(i)}(delta)
= sum_k min(delta, ord_t(rho_i - root_k of h)) as in FRONTIER-N
(reviewed); delta^0_i the g-frontier of rho_i (lambda_g^{(i)}(delta^0_i)
= 0); D_1 the last major disc of radius delta_1 with a_1 = eV_2 roots
of g and b_1 = dV_2 roots of f.

STEP 1 (the dictionary; Grok round submission sec.4, elementary).
Along tau_i: d/dx f(x, tau_i(x)) = [f,g]/g_y(x, tau_i(x)) = +-1/g_y(tau_i),
and g_y(tau_i) = prod_{j != i}(tau_i - tau_j) since g - c_2 is monic.
By FRONTIER-N's shifted-tree structure (the roots of g - c_2 follow the
unshifted tree to delta^0 and separate there as a star, generic c_2),
sum_{j != i} ord_t(tau_i - tau_j) = sum_{j != i} min(delta^0_i,
ord_t(rho_i - rho_j)) = lambda_g^{(i)}(delta^0_i) - delta^0_i = -delta^0_i.
Hence ord_t g_y(tau_i) = -delta^0_i and, integrating in x (no log term
can occur because f(x,tau_i(x)) is a Puiseux series), the POLE of f along
tau_i is EXACTLY 1 - delta^0_i when delta^0_i < 1 (proper place), f has a
finite limit when delta^0_i > 1 (non-proper place), and delta^0_i = 1 is
IMPOSSIBLE. So
      N = sum_i (1 - delta^0_i)^+   over the n roots of g - c_2,   (DICT-N)
a function of the UNSHIFTED g-TREE ALONE. Control: (y, x + y^5):
delta^0 = 4/5 for each of the 5 roots, N = 5 * 1/5 = 1.

STEP 2 (frontier bound, trivial). For rho_i in D_1: lambda_g^{(i)}(delta)
= lambda_g(delta_1) + int_{delta_1}^{delta} a^{(i)}(s) ds with a^{(i)}(s)
= #{j : ord_t(rho_i - rho_j) >= s} >= 1. So delta^0_i <= delta_1 -
lambda_g(delta_1) =: delta^0_star, with EQUALITY iff rho_i is alone in
every ball of radius > delta_1 (no other g-root of D_1 has contact
> delta_1 with rho_i). Deeper g-g contact LOWERS delta^0 and RAISES the
pole: the opposite of the N-ON-THE-TREE lane's "the free sub-tree can
only lower N" (which assumed the f-tree free; by STEP 1 it is slaved).

STEP 3 (N-CEILING density, reviewed). FRONTIER-N gives pole_i =
-lambda_f^{(i)}(delta^0_i) <= -lambda_f^{(i)}(delta_1) (monotone,
delta^0_i >= delta_1 since lambda_g(delta_1) < 0) = (d/e)(-lambda_g(delta_1))
(proportionality on the major tower) = d(1 - delta_1)/(d + e) by
RADIUS-ORDER at r = 1 (lambda_g(delta_1) = -n(1-delta_1)/(n+m)).

STEP 4 (the squeeze). By STEPS 1-2, pole_i = 1 - delta^0_i >= 1 -
delta^0_star = 1 - delta_1 + lambda_g(delta_1) = (1 - delta_1) -
e(1-delta_1)/(d+e) = d(1 - delta_1)/(d + e). By STEP 3, pole_i <=
d(1 - delta_1)/(d + e). Hence EQUALITY throughout, for EVERY root of
every bottom-major disc:
  (i) delta^0_i = delta^0_star: the a_1 g-roots of D_1 pairwise separate
      at EXACTLY delta_1 (STAR), and likewise no f-root has contact
      > delta_1 with any of them (lambda_f^{(i)}(delta^0_i) =
      lambda_f^{(i)}(delta_1));
  (ii) pole_i = d(1 - delta_1)/(d + e) exactly;
  (iii) with DETECTOR-NULL (minor discs contribute 0, reviewed),
      N = A_bot * d (1 - delta_1)/(d + e)                         (EXACT-N)
      where A_bot is the number of g-roots lying in bottom-major discs
      (sum per disc if different major branches carry different
      delta_1). A_bot <= ue with equality iff the crude cover of
      N-CEILING is exact; then N = U.
  (iv) OPEN[D1-SUBTREE] is CLOSED by rigidity; the filter becomes
      EXACT and TWO-SIDED: a skeleton is admissible only if
      A_bot * d (1 - delta_1)/(d + e) is an INTEGER in [6, 16] (the
      campaign's frontier N >= 6, integration #16 delta (a)) for some
      admissible A_bot (a multiple of a_1 = eV_2, at most ue). Moh's
      survivor with U_tower = 10.5 dies if A_bot = ue there.

YOUR TASK, hostile and computational.
(a) Find the flaw if there is one. Check every step against the frozen
    inputs: the dictionary's integration step (no log: the x^{-1}
    coefficient of 1/g_y(tau_i) must vanish — is that automatic or a
    constraint?); the shifted-tree contact formula; the sign and scope
    of monotonicity; the proportionality lambda_f = (d/e) lambda_g at
    the general point of D_1 including the OUTSIDE contributions;
    RADIUS-ORDER's scope (M_s = n-2; M_1 = -m); whether the r = 1
    identity (1 - delta_1) + lambda_g(delta_1) = -lambda_f(delta_1)
    (Grok sec.4.3, recomputed on six Moh rows) is what makes the squeeze
    tight and whether it could be an artefact of how Def 5.1(3)
    DEFINES delta_1 (if Moh's delta_1 is defined by termination of the
    recursion, is the star already Moh's own statement? quote him).
(b) Controls: the automorphism (y, x + y^5) and (y + x^2, x + (y+x^2)^2)
    (Jacobian -1): verify DICT-N gives N = 1 and delta^0 != 1; the
    NON-Keller two-tower rows of N-ON-THE-TREE CONTROL 1: verify the
    dictionary FAILS there (Grok's Res_y(J, g) check) — the negative
    control is load-bearing.
(c) If the argument survives: state THEOREM D1-STAR and THEOREM EXACT-N
    with exact hypotheses; compute A_bot from the skeleton (conjugate
    copies of D_1 inside D_2, ..., and across major branches) so that
    N is a closed-form function of (n, m, M_2..M_s, V_2..V_s, u, v);
    verify on Moh's six survivor rows (U_tower = 9, 6, 10.5, 12, 8, 16)
    and say which die by non-integrality; then RUN the exact filter
    over the census (box/moh_skeleton_N.py, D <= 400, one core, minutes):
    report per degree the number of skeletons with EXACT-N an integer in
    [6,16], and list every degree D <= 400 that is EMPTIED, in
    particular the MOH-SHARP-2 degrees {105,108,112,117,120}. If all
    degrees <= 400 empty, say what the arithmetic of EXACT-N (a
    divisibility condition on (d+e) | A_bot d (1-delta_1)) implies for
    D > 400 and whether a uniform elimination is in reach.
(d) If the argument fails: say exactly where, what survives (e.g. a
    two-sided floor N >= A_bot d(1-delta_1)/(d+e) from STEPS 1-2 alone,
    which would already invert FILTER-INVERSION), and rerun the filter
    with whatever is proved.
Discipline: everything charged is a PROPOSAL except items marked
reviewed (FRONTIER-N, RADIUS-ORDER in scope, DETECTOR-NULL, N-CEILING,
MOH-SHARP-2, NU-TWO); Moh 1983 in refs/ (hash). Desk-scale CAS only
(< 15 min, < 4 GB; the census is an integer script). State the bounded
quantity of every OPEN you raise; do not edit canonical ledgers; do not
inspect jc2-lean.
Report: xmodel/exact-n-rigidity-opus5-20260902.md
Seal-at-completion; bounded writes; target 25-40KB; typed verdict block
with CONFIRMED / GAP / REFUTED per step.
charged_input=xmodel/n-on-the-tree-opus5-20260902.md
charged_input=xmodel/n-on-the-tree-review-grok46-20260902.md
charged_input=xmodel/ideation-20260902T1608Z-grok46.md
charged_input=xmodel/integration16-coordinator-fable51-20260902.md
charged_input=xmodel/depth-ceiling-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
44223b324641e75be374f09c4b6daead796937d3176d8841844551e2d19c3967  {{LANE_INPUTS}}/n-on-the-tree-opus5-20260902.md
481d71bfdb9f5237405c671234c751b7c9a3d5339a23f676aa947b7fc69c5ba9  {{LANE_INPUTS}}/n-on-the-tree-review-grok46-20260902.md
8982e7ba896fa84e4b85e46de7d60f2e22001b3ca4e74b793c45a6f496f59e84  {{LANE_INPUTS}}/ideation-20260902T1608Z-grok46.md
6b8a712344397e1248e4efe230f5fcbeb41ae8b64423de272a77e98ae6b1a241  {{LANE_INPUTS}}/integration16-coordinator-fable51-20260902.md
863b05dbbd425035a09265cacdf6c418a2a3a1a7fadbeb303571bb5ccba618d6  {{LANE_INPUTS}}/depth-ceiling-opus5-20260902.md
```
