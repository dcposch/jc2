# Flagship lane: M2-DESCENT — prove or refute M_2 > m for a Keller skeleton in Moh's gauge; close OPEN[DESCENT-POLYGON]; write and attack the two descended D = 105 problems (15,10; γ⁴) and (21,14; γ²)

From the blind Fable submission of round 20260903T1015Z (charged), which read
Moh 1983 pp.148–151, 188–189, 196–202, 207–212 from the page images:
(i) MEASURED on box/moh_skeleton_full.py: the predicate M_2 > m (the first
non-K-divisible characteristic exponent of f in η = g^{−1/n} beyond −m
exceeds m) keeps all six p.202 rows, cuts the (1)–(13) survivors at n ≤ 100
from 658 to 94 rows / 32 classes, pins (75,50) to M_2 ∈ {55,60} (and with
integral N ≥ 6 to exactly Moh's two rows), cuts 1,189 → 179 groups at
48 ≤ D ≤ 120 (63 alive at N ≥ 6), EMPTIES twelve degrees including D = 105
(the trio has M_2 ∈ {28,40} < 70), and leaves D = 108 with two groups in
[6,16]; the Abhyankar–Moh semigroup conditions are AUTOMATIC on all 658
rows. M_2 > m was NOT found printed on the pages read: OPEN[M2-ABOVE-M].
(ii) Moh's program = the (1)–(13) sieve + a DESCENT: when u_s = 1, Prop 6.4
(p.198: δ*_{s−1} ≥ v_s) and Prop 6.3 (p.197) send the pair to polynomials
ḡ(σ), T̄_1^ψ(σ) ∈ k[γ,π], monic in π of π-degrees (n/d_s, m/d_s), with
J_{γ,π} = −(u_s/b) γ^{v_s−u_s−1} and characteristic data {M_i/d_s, d_i/d_s};
checked against the p.207 table: (64,48) → (16,12), X; (84,56) → (21,14), X;
(75,50) → (15,10), X². Appendix II then kills each by polynomiality of the
quasi-approximate-root expansion at the major and minor π-roots (10–22
coefficients). For the D = 105 trio (n = 105, m = 70, K = 35, (d,e) = (2,3)):
G2 = (M = [28,103], V_s = 6, d_3 = 7, u_3 = 1) → (15,10) with [P,Q] ∝ γ⁴,
M_2' = 4; G3 = (M = [40,103], V_s = 4, d_3 = 5, u_3 = 1) → (21,14) with
[P,Q] ∝ γ², M_2' = 8; G1 (u_3 = 2) needs the p.209 minor-disc dichotomy.
The Moh PDF is at refs/moh1983_jram340_configurations_of_roots.pdf (sha256
6c8847a8…; journal page N = PDF page N−139); render with pdftoppm -r 300 and
READ THE IMAGES.
YOUR TASK (flagship; direct; every step typed):
(1) M_2 > m. Reproduce the measurement first (fail-closed: 6/6 printed rows
    kept; 658 → 94; the (75,50) residue). Then PROVE OR REFUTE it as a
    theorem for Keller pairs in Moh's gauge. Routes to try, with the source
    open: (H1) Moh §2–§3 pp.148–160 — the tree data of the n conjugates
    Ω_i f determined by {M_j, d_j} and Lemma 2.1 (f_i(x) constant for
    i < n−1, deg_x f_{n−1} = 1): does the Ω-symmetry with constant
    coefficients forbid a non-K-divisible exponent in (−m, m]? (H2) the
    coprimality of g and T_1^ψ (Prop 5.6 remark p.189) at the top π-root
    σ_s: an order inequality forcing M_2 > m? (H3) the elementary route:
    with n = Ke, m = Kd, h := f^e − c g^d has [h, g] = e f^{e−1}[f,g], so
    deg h ≥ K(de − d − e) + 2 — is there a matching UPPER bound on deg h
    (equivalently a lower bound on M_2) from the Jacobian condition, e.g.
    via the Newton polygon of h or via Abhyankar's approximate-root theory
    (f is close to the d-th approximate root of g^{?}…)? Quote Moh where
    M_2 is constrained (Def 5.1, (1)–(7), Prop 5.5). State the theorem
    with exact hypotheses, or the exact obstruction and a candidate
    (1)–(13) skeleton with M_2 ≤ m that no known necessary condition kills.
(2) OPEN[DESCENT-POLYGON]: from the tower data (δ_s = −1, δ_{s−1}, …, δ_1,
    the V_j, d_j) compute the γ-degrees / Newton polygon in (γ, π) of the
    descended pair (P, Q) = (ḡ(σ), T̄_1^ψ(σ)); verify on Moh's three p.207
    rows (the transformed data must match to the unit, including
    M_2/d_s = 13, 16[18], 11); state which of (1)–(13) and M_2 > m the
    descended pair inherits (OPEN[DESCENT-CLOSURE]).
(3) THE TWO DESCENDED PROBLEMS. Write G2's (15,10; γ⁴; M_2' = 4, d_2' = 5)
    and G3's (21,14; γ²; M_2' = 8, d_2' = 7) as explicit polynomial systems
    in k[γ,π] following Moh pp.210–211 ((15,10; X²): P = h³ + 3βh + …, the
    θ^{−1}-series cancellation, the minor-disc shapes (5)–(6), deg_γ ≤ 2 ⇒
    three quadratic equations), impose the inherited characteristic data,
    and SOLVE exactly (sympy/Gröbner over Q, saturate at the unit leaders;
    desk-scale < 30 min one core, < 6 GB; if a system exceeds that, emit
    it with counts and stop). Type: SATURATED-EMPTY (a kill of that group
    at D = 105) / SURVIVES (print the solution set — the first positive
    signal above D = 100; then OPEN[DESCENT-LIFT]) / COUNTING-BOUND only.
    Control: run the same pipeline on Moh's (15,10; X²) row and reproduce
    his contradiction (pp.210–211); on a planted automorphism descended
    pair it must SURVIVE.
(4) READING: is "sieve + typed descent recursion" (Fable §8 DESCENT-
    RECURSION) a candidate all-degree mechanism — what does the recursion
    terminate in, and what theorem would make it a proof; what is the
    single cheapest next experiment.
Discipline: PROVED-HERE/UNREVIEWED; SOURCE-READ vs SOURCE-UNVERIFIED typing
per Moh citation; bounded quantity of every OPEN (ops/open_collision.py);
do not edit canonical ledgers; do not inspect jc2-lean; do not read other
ideation-20260903T1015Z-* files than the charged Fable one; do not read
other running lanes' reports. Drivers to box/m2descent-drivers-20260903/.
Report: xmodel/m2-descent-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 30-45KB; 180 minutes.
charged_input=xmodel/ideation-20260903T1015Z-fable5.md
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/time-function-endgame-review-sol56-20260902.md
charged_input=box/moh_skeleton_full.py
charged_input=box/censusrebase-drivers-20260902/survivors-D48-120.txt
charged_input=refs/moh1983_jram340_configurations_of_roots.pdf

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
486b0192d6cb1f3e064e00d16b57877ed67a2360543d8ec662c837afe5fc6456  {{LANE_INPUTS}}/ideation-20260903T1015Z-fable5.md
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
9e485492940818ea25b955af1713de53bc823af78f9f00a8991aaba9372f527d  {{LANE_INPUTS}}/time-function-endgame-review-sol56-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  {{LANE_INPUTS}}/moh_skeleton_full.py
47f59906927ff9d2b38b25b11c2e46cef3c472b3d8db300f12c12f22906848e1  {{LANE_INPUTS}}/survivors-D48-120.txt
6c8847a8d8374f7d7725c7e2ede2895a2c30034af6a7f28c511a471c41aa6a51  {{LANE_INPUTS}}/moh1983_jram340_configurations_of_roots.pdf
```
