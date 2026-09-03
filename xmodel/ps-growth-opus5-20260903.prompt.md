# Flagship lane: PS-GROWTH / TRACE-CONSTANCY — the degree-free identity family d/dx Tr(f^{k+1}) = (k+1) J · [y^{n−1}](f^k mod (g − c₂)); prove it, measure it, and attack the residue lower bound that would turn it into a ceiling

Two blind submissions of round 20260903T1015Z converged on the same object
(charged: ideation-20260903T1015Z-opus5.md §0.3, §2, §5–§7, §11 card 2;
ideation-20260903T1015Z-opus5-coordinator.md §0.3, §4, card 2). For a
Keller pair in Moh's monic gauge (deg_y g = n, deg_y f = m < n, generic
fibre g = c₂ with roots τ_i), with P_k := Σ_i f(x,τ_i)^k ∈ C[x,c₂] and
R_k := [y^{n−1}](f^k mod (g − c₂)) ∈ C[x,c₂]:
  (PS-1)  dP_{k+1}/dx = (k+1) J R_k            (JAC-FIBRE + Euler–Jacobi)
  (PS-2)  deg_x P_{k+1} ≤ (k+1)·max_i (1 − δ⁰_i)⁺ ≤ (k+1)·N   (DICT-N)
  (PS-3)  deg_x R_k ≤ (k+1)·max_i(1 − δ⁰_i)⁺ − 1
  TRACE-CONSTANCY: P_{k+1} ∈ C[c₂] whenever km ≤ n − 2 (R_k ≡ 0 by degree).
Sharpening (coordinator, unproved): by D1-PIN the per-root pole of f on a
bottom-major root is d(1−δ₁)/(d+e) < d/(d+e) < 1 (δ₁ ≥ 0 by Lemma 6.1), and
non-proper roots have pole ≤ 0, so max_i(1−δ⁰_i)⁺ = max_B q(B)/e < 1 and
(PS-3) reads deg_x R_k ≤ (k+1)·q_max/e − 1: hence R_k ≡ 0 for all
k < e/q_max − 1 and R_k is x-INDEPENDENT for all k < 2e/q_max − 1, at every
degree. Example: the D = 105 group A (q = 1/2, e = 3): R_2 = R_3 = R_4 ≡ 0
and R_5..R_11 ∈ C[c₂]. Control: (f,g) = (y, x + y³) gives R_2 = 1, P_3 =
3(c₂ − x), J = −1: PS-1 exact, PS-3 tight.
YOUR TASK (flagship; be direct):
(1) PROVE PS-0..PS-3 and TRACE-CONSTANCY with exact hypotheses (which need
    monicity, which need generic c₂, which need Keller, which need Moh's
    gauge/D1-PIN), and the sharpened per-root form; state precisely what
    "pole" means (x-growth exponent along a branch) and why deg_x of a
    polynomial in C[x,c₂] is bounded by the max branch growth.
(2) BUILD box/psgrowth-drivers-20260903/psgrowth.py: given (f,g), compute
    P_k via Newton's identities from χ(T) = Res_y(g − c₂, T − f), compute
    R_k directly, check PS-1 exactly, and print deg_x R_k vs the PS-3 bound.
    Controls: automorphisms in Moh's gauge at n = 2..6 (include the
    composition (x + y⁵, y + (x + y⁵)³) and a degree-6 tame automorphism);
    negative: a non-Keller pair must FAIL PS-1; vacuity guard: a Keller pair
    with N deliberately understated must fail PS-3. Then OPEN[PS-VACUITY]:
    is R_k identically zero on Keller pairs? sweep k ≤ 20, n ≤ 6 and report.
(3) THE RESIDUE LOWER BOUND — the one theorem the route needs. In Moh's
    gauge the top forms are l(f) = α H^d, l(g) = β H^e, H = L₁^u L₂^v
    (u > v, u + v = K), plus the tower data. Attack: is the leading x-term
    of R_k = [y^{n−1}](f^k mod (g − c₂)) determined by the initial forms /
    the approximate-root (g-adic) expansion of f^k, and can it be shown
    NONZERO with x-degree ≥ φ(k, m, n) → ∞ for a non-invertible pair? Work
    it on: (a) the automorphism controls (where it must be consistent with
    the tiny bound); (b) the seven non-Keller two-tower rows
    (box/tfe-drivers-20260902/); (c) a formal ansatz for a D = 105-type pair
    (top forms of the trio, k = 2, 3) computing the leading term of R_k
    symbolically in the tame coefficients — does the tiny bound force
    identities among the top-form coefficients that contradict
    Davenport–Stothers extremality of the bottom star? Type every step;
    if the leading term can cancel, say exactly which coefficient relation
    is needed and whether the skeleton (V_2 = 1, (2,3), δ₁) makes it
    impossible.
(4) RES-DEGREE (Opus §6): deg_x Res_y(g − c₂, f) = Σ_i (1 − δ⁰_i) = N − shed;
    verify on controls; compute the shed term on the three D = 105 groups
    from their tree data; state whether ORTHO-DEFECT minus RES-DEGREE gives
    a skeleton kill test and run it on the trio.
(5) READING: is PS-GROWTH a ceiling route (D ≤ C(N)) or a shape constraint
    (bounds m/n) or vacuous; what is the exact statement of the lemma still
    needed; and the single cheapest next experiment.
Discipline: PROVED-HERE/UNREVIEWED; bounded quantity of every OPEN; desk-
scale CAS (< 30 min one core, < 6 GB); do not edit canonical ledgers; do
not inspect jc2-lean; do not read other ideation-20260903T1015Z-* files
than the two charged; do not read other running lanes' reports.
Report: xmodel/ps-growth-opus5-20260903.md
Seal-at-completion (standard <!-- BODY-END --> marker; skeleton without it);
bounded writes; target 30-45KB; 150 minutes.
charged_input=xmodel/ideation-20260903T1015Z-opus5.md
charged_input=xmodel/ideation-20260903T1015Z-opus5-coordinator.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=xmodel/exact-n-rigidity-opus5-20260902.md
charged_input=xmodel/census-rebase-opus5-20260902.md
charged_input=box/tfe-drivers-20260902/bottomode.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
b13149ecac656f7f3548e6cd388b1699c514ff49a53882f7239039a2c0022562  {{LANE_INPUTS}}/ideation-20260903T1015Z-opus5.md
52af9fcab43fbdb66b4f3f0eeec83b255faf5dd5ae966a3cb1e7f657de57481c  {{LANE_INPUTS}}/ideation-20260903T1015Z-opus5-coordinator.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
e639fdbf5cdbdf0756d9d8287b52c0183b07e2bf8ab7d4b293c242ea2c35f37c  {{LANE_INPUTS}}/exact-n-rigidity-opus5-20260902.md
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  {{LANE_INPUTS}}/census-rebase-opus5-20260902.md
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  {{LANE_INPUTS}}/bottomode.py
```
