# Computation lane: EXACT-PACKET filter — assuming EXACT-N, which Moh skeletons at the admissible degrees admit an integer N >= 6?

CONDITIONAL on the PROPOSAL EXACT-N / D1-SELF-DIFFERENT (Sol round
submission sec.2, SD1-SD6; coordinator's exact-n-rigidity prompt; under
hostile review in a parallel lane — do NOT re-prove it here, and type
every output "CONDITIONAL on EXACT-N"): for a degree-minimal Keller pair
in Moh's gauge, the geometric degree is
   N = sum over bottom-major discs B of  e*V_2(B) * d*(1 - delta_1(B))/(d+e),
   with sum_B e*V_2(B) <= u*e,
where each bottom branch B carries its own admissible V-vector
(V_2(B), ..., V_{s-1}(B)) inside Moh's Def 5.1(2) windows (all with the
same (n, m, M_2..M_s, V_s)? — state precisely which data are shared
across branches and which are per-branch, following Moh's Def 5.1 and
Sol sec.2; if V_s or higher V's must be common to all branches, say so
and enforce it). N must be an INTEGER, and the campaign frontier is
N >= 6 (integration #16 delta (a): N <= 5 is closed; do NOT use 4).
The coordinator's proxies (uint2.log): with a single branch type per
group only 3,424 groups at D <= 400 admit an integer N >= 6 and none an
integer in [6,16]; with an unconstrained count, 190,167 admit
N in [6,16]. Sol's permissive prototype at D = 105: 59 -> 21.
YOUR TASK (desk-scale, exact rational arithmetic):
(1) Using box/moh_skeleton_N.py (census(n, with_V=True) enumerates
    V-skeletons; the Skel class exposes n, m, M, s, u, dd=d, e, V, delta
    and windows_ok), enumerate for each group (n, m, M_2..M_s, V_s) at
    D in {105, 108, 112, 117, 120} EVERY admissible branch type (full
    V-vector in the windows) with its weight w(B) = e V_2 d (1 -
    delta_1)/(d+e) and its root count r(B) = e V_2. Report the number
    of branch types per group and the set of distinct weights.
(2) Solve the exact packet knapsack per group: does a multiset of branch
    types exist with sum r(B) <= u e and sum w(B) an integer >= 6?
    Separately: an integer in [6,16]? Use a DP over (roots used,
    fractional part) with Fractions; report per degree the number of
    surviving groups and the list of achievable N values; report which
    of the five degrees are EMPTIED under each variant.
(3) Extend (2) to all D <= 200 (and to 400 if it runs in < 15 min on one
    core; otherwise report the wall time at 200 and stop) and list every
    emptied degree.
(4) For the SMALLEST surviving group (if any) at D = 105, print the full
    packet (branch types, V-vectors, delta_1's, weights) and the value
    of N; that is the realisation target for the next lane.
(5) Controls: (y, x + y^5)-type automorphism rows cannot be run through
    the census (nu = 1); instead verify on Moh's six survivor rows
    (U_tower 9, 6, 10.5, 12, 8, 16 from the N-ON-THE-TREE report) which
    admit an exact packet with integer N >= 6 and which die.
Discipline: CONDITIONAL typing throughout; no claim that any degree is
"proved empty" — the theorem is under review; state the bounded quantity
of any OPEN you raise; do not edit canonical ledgers; do not inspect
jc2-lean; one core, < 4 GB.
Report: xmodel/exact-packet-filter-gpt55-20260902.md
Seal-at-completion; bounded writes; target 15-25KB; 60 minutes.
charged_input=xmodel/ideation-20260902T1608Z-sol56.md
charged_input=xmodel/ideation-20260902T1608Z-synthesis.md
charged_input=xmodel/exact-n-rigidity-opus5-20260902.prompt.md
charged_input=xmodel/n-on-the-tree-opus5-20260902.md
charged_input=xmodel/n-on-the-tree-review-grok46-20260902.md
charged_input=box/moh_skeleton_N.py
charged_input=box/coordinator-recounts-20260902/uint2.py
charged_input=box/coordinator-recounts-20260902/uint2.log

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
3a4744ddb23e6659ad1ab752e7d7b531c8a325f041971b7d72ec1179f11155e1  {{LANE_INPUTS}}/ideation-20260902T1608Z-sol56.md
7c5e97459541d6ba3842561b5af71a9352fe916b8687fda640ccf099237913c1  {{LANE_INPUTS}}/ideation-20260902T1608Z-synthesis.md
60cb5f57723fd4980fd1edb5aa491b5921b3ac27f8779effbcfe75872b81cc47  {{LANE_INPUTS}}/exact-n-rigidity-opus5-20260902.prompt.md
44223b324641e75be374f09c4b6daead796937d3176d8841844551e2d19c3967  {{LANE_INPUTS}}/n-on-the-tree-opus5-20260902.md
481d71bfdb9f5237405c671234c751b7c9a3d5339a23f676aa947b7fc69c5ba9  {{LANE_INPUTS}}/n-on-the-tree-review-grok46-20260902.md
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  {{LANE_INPUTS}}/moh_skeleton_N.py
77d4982cd491cb0ee2633a0d2bb8a63edcb7be05573c50ddd7794d55a326d398  {{LANE_INPUTS}}/uint2.py
9c862d850badeeeb5f9a3c27b6c45078a4504803112ed4d0f8d691a43ffb2a49  {{LANE_INPUTS}}/uint2.log
```
