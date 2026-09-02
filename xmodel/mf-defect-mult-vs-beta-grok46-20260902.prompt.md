# Desk lane: MF-DEFECT and MULT-VS-BETA — the two priced +1 questions on the meridian floor

The reviewed MF-EXACT identity (charged producer + review): for a
noninvertible Keller map F = (P,Q) of geometric degree N under H2 and a
generic line L, the generic member C_L = F^{-1}(L) = {alpha P + beta Q =
gamma} of the pencil is a smooth affine curve with
n (W − S) = N − 2 + 2 g_L + theta_inf, where n = deg A_F-bar, W = N − a,
S = sum_l s_l, g_L the genus of C_L and theta_inf its number of
target-escaping places at infinity (theta_L = nS + theta_inf places in
all). The banked floor n >= ceil((N−1)/(W−S)) is the case g_L = 0,
theta_inf = 1. Two questions were priced by the producer and left OPEN:
(Q1) OPEN[MF-DEFECT]: is 2 g_L + theta_inf >= 2 for EVERY noninvertible
     Keller F and generic L — i.e. is the floor never attained? Bounded
     quantity: (g_L, theta_inf) with g_L <= p_a(D_F), 1 <= theta_inf <= N.
     PROVED by the producer at W = 2 with beta = 1. A YES adds +1 to the
     floor at every cell. This is a question about the generic fibre of
     a polynomial SUBMERSION C^2 → C (u∘F has no critical points): can
     it be rational with exactly nS + 1 places at infinity, nS of them
     over the n points of L ∩ A_F? Attack with the classical theory —
     Suzuki's formula (sum of fibre defects = 1 − chi_gen), Hà–Lê
     nonnegativity, Abhyankar–Moh–Suzuki (a fibre ≅ A^1 forces a
     variable, impossible for noninvertible Keller), Zaidenberg–Lin /
     Kaliman on polynomials with rational or C^*-type generic fibres,
     the Neumann–Rudolph / Cassou-Noguès theory of links at infinity of
     fibres of polynomials; note the coordinator's desk check (notes
     ~11:05Z) that the defect budget nW − N + 1 is fully spent by the
     (K) ledger, so the answer must come from the STRUCTURE of the
     fibre, not from counting. Give a proof, a counterexample-shaped
     obstruction, or the exact classical statement that decides it.
(Q2) OPEN[MULT-VS-BETA]: in case (B3) at W = 2 for N >= 5, is beta = 1
     forced (beta = number of singular branches at the multibranch
     points)? Bounded quantity: beta in {1, …, N − 3}. N4-PIN gives it at
     N = 4 (a − 1 = 1 forces it). The producer says this is a finite
     question on the constraints (C3) and MPRIME Lemma 4.3 (each s_l = 1
     contributes k_t >= 1 at the NI place) with the (K) ledger. Decide
     it for N = 5, 6, 7 explicitly and give the general argument or the
     exact obstruction. A YES lifts the whole W = 2 column to
     n_min >= N.
Discipline: consume MF-EXACT, LOC-MULT, MF-SHARP, SHARP-CHAU at the
review's CONFIRMED typing WITH its repairs (the S-known vs W-only floor
distinction; the orbit hypothesis in LOC-MULT; no Z(G) = 1 anywhere);
MPRIME and HF at banked typing; case (A) is EMPTY (integration #9) —
do not use PERIPHERAL-RANK/MERIDIAN-SPAN. Desk only, sympy allowed;
state the bounded quantity of every OPEN you raise; do not edit
canonical ledgers; do not inspect jc2-lean.
Report: xmodel/mf-defect-mult-vs-beta-grok46-20260902.md
Seal-at-completion; bounded writes; target 12-20KB; 75 minutes.
charged_input=xmodel/meridian-floor-sharpen-opus5-20260902.md
charged_input=xmodel/meridian-floor-sharpen-review-gpt55-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md
charged_input=xmodel/horn-flagship-opus5-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
4fa4b5f60692ade07b3ce45405ab2623edb4ef3aef1174e34beaf2373ce2f2a4  {{LANE_INPUTS}}/meridian-floor-sharpen-opus5-20260902.md
32c043320d11b619ef717cbb2dc5f3ca1ec7756abaa5f470d2ee0fb49dfe7b82  {{LANE_INPUTS}}/meridian-floor-sharpen-review-gpt55-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  {{LANE_INPUTS}}/horn-flagship-opus5-20260902.md
```
