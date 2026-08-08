# SHEET6-H3.md — Settling H3 (root-vertex kill of case-IV terminals)

Status: COMPLETE + PROMOTED (2026-08-07, SHEET6-HIII-REVIEW.md: psi-budget
CONFIRMED, G2 closure stands; the §5 survivor book is SUPERSEDED by the
composition, cases/hiii_compose.py). Auditor: Claude. All thesis citations read
on-page (papers/sigray_full.pdf; page numbers = printed = pdf pages).
Question (SHEET6-CAMPAIGN.md §6 item 1 / §0b G2; SHEET6-REVIEW.md §2 CONFIRMED
load-bearing): does a characteristic sequence terminating at the root vertex
(0,y) via Prop 9.3 case IV contradict the normalization of the Sigray engine
(papers/sigray_full.pdf)? Candidate: case IV (l) forces d_F < deg p_G at the
root; Thm 6.1 (l_f < k_f) plus a chart-matching argument should forbid it.

VERDICT: (b) H3 FALSE as a blanket kill — an explicit case-IV terminal chain
satisfying every printed normalization constraint exists (§5b, r10/M4) —
BUT a PROVED quantitative replacement (Theorem H3-psi, §4a) kills, from
printed thesis statements alone: 100% of the IV-terminals of the thesis's
own St 9.12 chains (gap G2 is thereby CLOSED, §6(ii)), and, together with
the (l)/(m)-consistency tests, closes the IV side of 8 of the 14
IV-carrying campaign runs — including 6 of the 9 sanctioned ones
(r4/M2, r10/M2, r2, r3, r8/M2, r9/M3).
The chart-matching resolves as follows: Thm 6.1's l_f < k_f transported by
St 3.12 to the (0,y) chart points the SAME way as case IV (l) (no clash);
what (l) really buys is a certified psi = ceil(deg p_G/d_F) - 1 >= 1 in
St 9.4's budget family (25), shrinking the lambda-budget below what the
campaign (and St 9.12 as printed, which uses only (26) = psi=1) assumed.
Survivors: 43 (shape,lambda) classes on sanctioned entries (15 at td=5
r10/M4, 28 at td=6 on r6/M3 + r11/M5), all with R = deg p_G/d_F in
{3/2, 2, 5/3, 3} and low lambda; plus a new side-gap (SF1, §7): possible
root-termination via case I that no one models.

## 1. Ground truth: the thesis's own root-vertex argument (Prop 8.4 proof)

Read on-page (pp. 44-45). Structure of the proof of Prop 8.4 (single pole,
assume some M_F = 1):
- Build the sequence F_0 = F, F_{i+1} = F_i° while pi(F_i) != 0; by Props
  6.7/6.8 all F_i in T_a^searrow, so F_n = (0,y). Set H := F_{n-1}.
- Prop 8.3 + induction: M_H = 1. St 8.1 (p. 39, verbatim): "there exist
  N, N_0, ..., N_m ... in Z with M_F = N deg(p_F) + N_0 deg(p_{h_0,F}) +
  ... + N_m deg(p_{h_m,F})" — i.e. M_F is the gcd of the h-family degrees
  (definition directly above St 8.1 on p. 39). With M_H = 1: pick N, N_i
  with 1 = N deg(p_H) + sum_i N_i deg(p_{h_i,H}).
- Transport to the root: (k,l) := N(deg p_{(0,y)}, d_{(0,y)}) +
  sum_i N_i (deg p_{h_i,(0,y)}, d_{h_i,(0,y)}). "From Corollary 6.1 and from
  Proposition 6.3, there exists w in Q such that (k,l) = w(k_f,l_f)." Since
  d_{h,(0,y)} in N for any polynomial h, k,l in Z.
- Compute k: deg(p_{(0,y)}) = mult(p_{(0,y)},c) (Prop 8.3(iii): under the
  M=1 hypotheses p_{(0,y)} = (eta-c)^k, one root), and mult(p_{h,(0,y)},c) =
  deg(p_{h,H}) (St 8.3(ii), p. 41, verbatim: "deg(p_{h_j,F}) =
  mult(p_{h_j,G}, c)" for F = G*c, general — no M=1 needed; its proof also
  restates St 3.17(i): "mult(p_G,c) = deg(p_F)"), so
  k = N deg(p_H) + sum N_i deg(p_{h_i,H}) = 1.
- Then w = 1/k_f > 0, l = l_f/k_f > 0, l in Z => l in N* => l_f >= k_f.
  "This, however contradicts Theorem 6.1 [l_f < k_f]." QED.

So the thesis's ONLY root-vertex kill is arithmetic on the primitive vector
(k_f,l_f): Bezout scales the h-family degree vector at H to first coordinate
1; positivity + integrality of the second coordinate forces l_f/k_f >= 1.
It NEEDS M_H = 1 (else Bezout gives M_H, not 1) — as the campaign/review
found, it does not transfer verbatim to case-IV terminals with M_G >= 2.
KEY OBSERVATION for later: with M_H = M >= 2 the same computation gives
k = M and l = M l_f/k_f in Z, i.e. exactly condition (m) of Prop 9.3(IV)
(deg(p_G) | d_F M_G after the root identifications of §2 below) — the
Bezout root-argument is ALREADY absorbed into case IV's own condition list
and yields no further contradiction for M >= 2.

## 2. Ground truth: Thm 6.1, its chart, and the normalization

Read on-page:
- Lemma 2.1 (pp. 8-9): normalized counterexample (f,g); f^+_{(1,1)} =
  ⊖x^{k_f}y^{l_f}; (i) (k_f,l_f) in N_f, (k_g,l_g) in N_g, ALL of
  k_f,l_f,k_g,l_g > 0, N_f inside rectangle (0,0),(0,l_f),(k_f,l_f),(k_f,0);
  (ii) k_f/k_g = l_f/l_g; (iii) k_f < k_g, l_f < l_g, l_f <= k_f, l_g <= k_g;
  (iv) k_g/k_f not in N*. Notation 2.4: type (alpha,beta) = (k_f,k_g) reduced.
- Thm 6.1 (p. 28): l_f < k_f. Proof: "Property (iii) of Lemma 2.1 says
  l_f <= k_f. Moreover, k_f = d_{(0,x)} and l_f = deg(p_{(0,x)}), so
  k_f != l_f, by Proposition 6.1."  [Prop 6.1: d_F != (1-pi(F))deg(p_F);
  at (0,x), pi = 0.]
- Notation 6.1 (p. 29): T_a^nearrow = {d_F > (1-pi(F))deg p_F},
  T_a^searrow = {d_F < (1-pi(F))deg p_F}.
- CHART MATCHING (cited in Prop 6.5's proof, p. 32, from Statement 3.12):
  "deg(p_{h,(0,x)}) <= d_{h,(0,y)}, d_{h,(0,x)} >= deg(p_{h,(0,y)}),
  d_{(0,x)} = deg(p_{(0,y)}) and deg(p_{(0,x)}) = d_{(0,y)}."
  So for f itself the two root charts SWAP (deg p, d):
      k_f = d_{(0,x)} = deg(p_{(0,y)}),   l_f = deg(p_{(0,x)}) = d_{(0,y)}.
  [St 3.12 verified verbatim in §2a below.]
- Consequence: Thm 6.1 at the (0,y) chart reads d_{(0,y)} < deg(p_{(0,y)}).
  This is the SAME direction as case IV (l) (d_F < deg p_G <= deg p_{(0,y)}),
  NOT opposite: the campaign's G2 candidate ("case IV (l) vs Thm 6.1 clash")
  is a chart confusion — there is no direct sign contradiction.

### 2a. St 3.12 verbatim + the mult/deg transport (verified on-page)

- St 3.12 (p. 16) verbatim: "Let h(x,y) be a polynomial. Then h^+_{(0,y)} =
  h^+_{(0,1)} and h^+_{(0,x)} = h^+_{(1,0)}. As consequence we obtain
  d_{h,(0,y)} >= deg(p_{h,(0,x)}) and d_{h,(0,x)} >= deg(p_{h,(0,y)})."
  I.e. d_{h,(0,y)} = deg_y h, d_{h,(0,x)} = deg_x h (top parts in the pure
  chart weights), and the root polynomial at one root has degree bounded by
  the d-datum at the other. For h = f, Lemma 2.1(i) (N_f inside the
  rectangle with corner (k_f,l_f) in N_f) upgrades this to the equalities
  used verbatim in the proofs of Thm 6.1 ("k_f = d_{(0,x)}, l_f =
  deg(p_{(0,x)})", p. 28) and Prop 6.5 ("d_{(0,x)} = deg(p_{(0,y)}) and
  deg(p_{(0,x)}) = d_{(0,y)}", p. 32):
      d_{(0,x)} = deg_x f = k_f,   d_{(0,y)} = deg_y f = l_f.
  (T_a is built for f-a; the additive constant does not change the top
  parts since k_f, l_f > 0.) For the H3 argument only the PRINTED
  inequality direction d_{(0,x)} >= deg(p_{(0,y)}) plus l_f = d_{(0,y)}
  is needed.
- Prop 3.2 (p. 18): for F in V_a \ {(0,x),(0,y)}, G := F°, there is a
  unique c with G * c = I_P(v); notation F =: G + c. So "+c" moves away
  from the root; in Prop 9.3's step (G = F + c, F = G°), G is the deeper
  vertex (= F_i), F the shallower (= F_{i+1}).
- St 3.17 (p. 18) verbatim: "Set F,G in V_a. Assume F = G + c for some
  c in C. Then (i) deg(p_F) = mult(p_G, c); (ii) d_F = d_G -
  (pi(F)-pi(G)) deg(p_F)."  NO M=1 hypothesis. Applied to the terminal
  step (deeper = G_IV = (0,y) + c):
      deg(p_{G_IV}) = mult(p_{(0,y)}, c) <= deg(p_{(0,y)}).
- St 3.11 (p. 16) is the general-h inequality version (mult(p_{h,F'},c) >=
  deg(p_{h,F})); St 3.16 (p. 17): for F not a root vertex, F in V_{1,a}
  cup V_{2,a} iff p_F has more than one root.

CHART-MATCHING CHAIN (all printed statements):
    k_f  =  d_{(0,x)}          [Lemma 2.1(i) + St 3.12, cited in Thm 6.1]
        >=  deg(p_{(0,y)})     [St 3.12, printed inequality]
        >=  mult(p_{(0,y)},c)  [trivial]
         =  deg(p_G)           [St 3.17(i), G = (0,y)+c = F_{n-1}]
    l_f  =  d_{(0,y)}  = d_F   [Lemma 2.1(i) + St 3.12; d_F as in 9.3(k)]
Therefore   k_f / l_f  >=  deg(p_G) / d_F  =: R  >  1   by case IV (l).

## 3. Ground truth: case IV of Prop 9.3, root data (St 9.2), budget (St 9.4)

Read on-page (pp. 48-51):
- Notation 9.1: Q(F) := (D_F, deg(p_F), nu_F, M_F, kappa_F(1-pi(F))).
- St 9.2 (p. 48), F = (0,y): (i) D_F = d_F; (ii) nu_F = 1;
  (iii) kappa_F(1-pi(F)) = 1.
- Prop 9.3 (pp. 50-51): F,G in V_a cap T_a^searrow, G = F + c (c a root of
  p_F; G deeper = F_i, F = G° = F_{i+1}). Exactly one of (I)-(IV);
  (IV): F = (0,y) and F not in V_{1,a} cup V_{2,a}. Then
    (i) nu_G = kappa_G; (j) (1-v)kappa_G < nu_G;
    (k) d_F = [D_G + (nu_G-(1-v)kappa_G) deg(p_G)]/nu_G in N;
    (l) d_F < deg(p_G); (m) d_F M_G/deg(p_G) in N.
  [(1-v)kappa_G = kappa-bar_G in campaign notation. Campaign extraction §0a
  verbatim-confirmed.]
- St 9.4 (p. 49) IS A ONE-PARAMETER FAMILY OF BUDGETS, not just (26):
  "Let F_1,...,F_n in V_a cap T_a^searrow be pairwise different. Assume that
  for psi in N one has psi l_f < k_f. Then
      sum_i lambda_{F_i} <= td(f,g) - 1 - psi.        (25)
  In particular, sum_i lambda_{F_i} <= td(f,g) - 2.   (26)"
  Proof (read): (0,x) in T_a^nearrow => exists G in T_{a,cv} cap T_{a,x}
  (St 7.3); St 3.11 => pi(G) > psi; kappa_G(pi(G)-1) in N and > psi-1, so
  >= psi; Cor 7.1 (global budget td-1) => sum lambda + psi <= td - 1.
  I.e. the x-side pole direction eats psi units of the global td-1 budget,
  and psi is limited ONLY by psi < k_f/l_f. St 9.5/9.12 use only psi = 1;
  psi >= 2 is available whenever k_f/l_f > 2 — and case IV's own data
  certifies exactly that (§4).
- St 9.12 (p. 60) verbatim kill set, proof in full: "From Statements 9.6,
  9.7, 9.8, 9.9, 9.10 and 9.11 we obtain that either the characteristic
  sequence has an element F_j with M_{F_j} = 1, or (26) does not hold. The
  first case contradicts Proposition 8.4, the second contradicts Statement
  9.4." — i.e. the printed proof invokes only the psi=1 specialization
  (26), confirming SHEET6-REVIEW.md §2: as printed it cannot kill its own
  case-IV terminals. The repair (§6(ii)) stays inside St 9.4.

## 4. The root-vertex kill: derivation

FIRST, the negative half (why the campaign's candidate as literally stated
does NOT work): Thm 6.1 (l_f < k_f) transported to the (0,y) chart via §2a
reads d_{(0,y)} < deg(p_{(0,y)}) — the SAME inequality direction as case
IV (l) (d_F < deg p_G <= deg p_{(0,y)}). There is no sign clash between
charts; the two inequalities are one inequality seen twice. Likewise the
Prop-8.4 Bezout argument run with M_G >= 2 in place of 1 yields only
k = M_G, l = M_G l_f/k_f in Z, i.e. deg(p_G) | d_F M_G — which is exactly
case IV's own printed condition (m), not a contradiction. A case-IV
terminal is NOT unconditionally inconsistent (see §4b for genuinely
consistent root data). H3 as an unconditional kill is FALSE; what is true
is a QUANTITATIVE kill that suffices for every chain the campaign found:

### 4a. Theorem (H3-psi). Let (f,g) be a normalized counterexample, and let
F_0,...,F_n = (0,y) be the characteristic sequence of the (single) pole
vertex (Prop 9.2), with terminal step in case (IV) of Prop 9.3, G :=
F_{n-1}. Set
    R := deg(p_G)/d_F   (d_F = d_{(0,y)}, the value in 9.3(k)),
    psi := ceil(R) - 1  (= the largest integer < R; R > 1 by (l)).
Then psi >= 1 and
    sum_{i=0}^{n} lambda_{F_i} <= td(f,g) - 1 - psi.        (*)
In particular any characteristic sequence whose terminal step is case IV
with sum lambda_{F_i} > td - 1 - psi is contradictory.

Proof. By (l) (p. 51), d_F < deg(p_G), so R > 1 and psi >= 1. By the §2a
chain (Lemma 2.1(i), St 3.12, St 3.17(i)): k_f >= deg(p_G) and l_f = d_F,
hence k_f/l_f >= R > psi, i.e. psi l_f < k_f. The F_i are pairwise
different elements of V_a cap T_a^searrow (Props 6.7/6.8/9.2 — same use as
St 9.5). Statement 9.4, inequality (25), applied with THIS psi (not just
psi = 1 as in (26)/St 9.5) gives (*). QED.

Remarks.
- (*) uses only printed thesis statements; the sole "new" content is
  noticing that case IV's own condition (l) certifies the hypothesis
  psi l_f < k_f of St 9.4 at psi = ceil(R)-1, because the terminal step
  pins l_f = d_F and k_f >= deg(p_G). This is the chart-matching argument
  G2 asked for: (k_f, l_f) live at (0,x), (d_F, deg p_G) at (0,y), and
  St 3.12 + St 3.17(i) transport one to the other.
- The engine's recorded lambda at an IV hit is a lower bound for
  sum lambda_{F_i} (AF2 minima, and it omits lambda_{F_n} >= 0), so
  "recorded lambda > td-1-psi" certifies the kill a fortiori.
- Two further consistency conditions the engine does not test, both
  j-free, kill additional IV hits outright:
    (l)-test: R > 1, i.e. rho_G < kappa-bar_G  (else case IV impossible);
    (m)-test: M_G/R = d_F M_G/deg(p_G) in N*   (else case IV impossible).
- In shape coordinates (rho = D/P, nu, M, kap = kappa-bar):
    d_F/P = (rho + nu - kap)/nu,   R = nu/(rho + nu - kap)   (j-free).

### 4b. Why no unconditional kill exists (the residual consistency region)

A case-IV terminal with data satisfying (j),(k),(l),(m) and
sum lambda <= td - 1 - psi violates NO statement of the thesis that this
audit could locate (§§2-8 swept for root-vertex constraints: Lemma 2.1
(i)-(iv), Prop 6.1, Thm 6.1, Prop 6.5, St 3.12, St 9.2, Prop 8.4 at the
root — all satisfiable by such data; Lemma 2.1(iv) k_g/k_f = beta/alpha
not in N* is automatic from alpha >= 2; the root M is a free parameter
even in the thesis's own terminal possibilities "for some M in N",
9.7(iii)/9.9(iii)/9.10(iii)). The consistency region is nonempty AND
reached by the campaign's chains: §5b exhibits a full chain (r10/M4,
td=5) whose terminal data satisfy every printed constraint with slack.
So H3 as a blanket hypothesis ("case-IV terminals are killed by the
root-data constraint") is FALSE; the true content is the quantitative
kill (*) plus the (l)/(m) consistency tests, which together dispose of
the majority of the campaign's IV book — including 100% of the chains
the thesis's own St 9.12 needs (§5, §6).

## 5. Full engine sweep + concrete checks (cases/h3_check.py)

`cases/h3_check.py` re-runs the campaign BFS (identical kill/budget logic to
`sheet6_campaign.bash`) and classifies EVERY IV hit by the §4 tests, exact
arithmetic, s = 0..40 for parametric shapes (R(s) is a Moebius form in s;
its s->infty limit is also computed). Results (hits deduped by (shape,lam)):

| run | entry | dead (l)/(m)/(k) | killed psi | SURVIVORS |
|---|---|---|---|---|
| td=3 | r1 (2,3)M2 | 0 | 0 | 0 (no IV at all) |
| td=4 | r4 (2,3)nu3 M2 | 1 | 4 | **0** |
| td=4 | r4 M4 (superset) | 1 | 4 | **0** |
| td=5 | r10 (4,5)nu4 M2 | 0 | 4 | **0** |
| td=5 | r10 M4 (SANCTIONED) | 0 | 5 | **15 classes** (134 (shape,s)) |
| td=6 | r2 (2,3)nu1 M2 | 0 | 2 | **0** |
| td=6 | r3 (2,3)nu2 M2 | 0 | 2 | **0** |
| td=6 | r6 (3,4)nu2 M3 | 0 | 0 | **6 classes** |
| td=6 | r8 (2,5)nu5 M2 | 7 | 0 | **0** (case IV impossible) |
| td=6 | r8 M3 (superset) | 0 | 4 | 0 |
| td=6 | r8 M6 (superset) | 9 | 15 | 30 classes |
| td=6 | r9 (3,5)nu5 M3 | 15 | 0 | **0** (case IV impossible) |
| td=6 | r9 M2/M6 (superset) | 4/15 | 1/9 | 8/45 classes |
| td=6 | r11 (5,6)nu5 M5 | 0 | 4 | **22 classes** |

### 5a. Three concrete KILL instances (hand-verified, exact)

1. The G2 escaping chain (thesis's own St 9.12 ground, td=4, budget (26)=2):
   row 4 entry (j,2j,3,2,5) -> 9.6(iii) (7j,21j,7,3,5) with lambda >= 2
   (PRINTED, p. 51) -> 9.7(iii) case-IV terminal. At G = (1/3,7,3,5):
   d_F = P(1/3+7-5)/7 = P/3 (= j', matches printed 9.7(iii)), R = 3,
   (m): M/R = 3/3 = 1 ok, psi = 2. Kill: Sum lambda = 2 > td-1-psi = 1.
   KILLED — using only printed statements (no AF2 needed: the lambda >= 2
   is 9.6(iii)'s own annotation). Same for 9.6(iv)->9.8(iii) (R=4, psi=3,
   2 > 0) and the 9.6(v)->St 9.11 exits (lambda >= 2 printed, same R's).
2. r2 (td=6): entry (2,3)D2P2nu1 M2 -> ... -> (1/3,7,3,5) at Sum lambda=4:
   same shape as (1): R=3, psi=2, kill: 4 > 6-1-2 = 3. KILLED. (Also its
   second IV shape (2/3,3s+2,3,2s+2): d_F = P/3, R = 3 for all s, psi=2,
   4 > 3 KILLED.) r3 identical => r2, r3 lose the "mod H3" qualifier.
3. (m)-kill: row-4 9.9-shape M=2 copy (3/4,4s+3,2,3s+3) (E3's mu=2
   family): d_F = P(3/4 + (4s+3) - (3s+3))/(4s+3) = P(s+3/4)/(4s+3) = P/4,
   R = 4, but (m) requires d_F M_G/deg(p_G) = 2/4 = 1/2 in N — FALSE. Case
   IV impossible outright (checked s=1,2,3 exact; engine emitted it only
   because its IV gate tests (j) alone). Same mechanism closes ALL 7
   r8/M2 hits (e.g. (2/9,9s+8,3,2s+2): R = 9/7, M=3 -> 7/3 not in N) and
   all 15 r9/M3 hits (M in {2,4,5} vs R in {4, 4/3, 10, 8/5}: M/R never
   integral; verified per-hit in the h3_check run).

### 5b. The survivor exhibit (H3 counterexample at Q-level), r10/M4, td=5

Entry r10 = type (4,5), (D,Dg)=(4,5), (P,Pg)=(4,5), nu=4, kap=9, M=4
(M | gcd(D,P): SANCTIONED menu). Chain (each step solved exactly, engine +
hand-check in cases/h3_check.py run log):
  F0 = (1,4,4,9)  --mu=4, case III, k=1, nu_F=32, m=2-->
       ((4+32)/(1+32) = 4(1+2)/(9+2) = 36/33 ok)
  F1 = (1/3,32,3,11), lambda_F1 >= 1   --mu=3, IIa_0 (k=0), family
       nu=3s+2, at s=1: n = 21+32 = 53, kap_F = (11+53)/32 = 2,
       D_F/i = 3(1/3+53)/32 = 5, (dp,dq)=(15,6), M=3, lambda = 0-->
  F2 = (1/3,5,3,2)   --mu=3, case III, k=1, nu_F=5, m=1:
       (3+5)/(1+5) = 3(1/3+1)/(2+1) = 4/3 ok-->
  F3 = (1/2,5,2,3), lambda_F3 >= 1, deg p = 8j
  Terminal, case IV: (j): 3 < 5 ok; (k): d_F = 8j(1/2+5-3)/5 = 4j in N ok;
  (l): 4j < 8j ok; (m): 4j*2/8j = 1 in N* ok.
  Root data: Q((0,y)) = (4j, k_f, 1, M, 1), l_f = d_{(0,y)} = 4j,
  k_f = deg(p_{(0,y)}) >= 8j; single-root case k_f = 8j.
  Normalization audit: l_f < k_f (Thm 6.1) ok; (k_g,l_g) = (5/4)(8j,4j) =
  (10j,5j) in N^2, k_f/k_g = 4/5 = alpha/beta ok (Lemma 2.1(i),(ii));
  k_g/k_f = 5/4 not in N* (Lemma 2.1(iv)) ok; M_{(0,y)} != 1 (Prop 8.4)
  satisfiable (root M is unconstrained by the chain — thesis's own
  terminals print "M in N"); budget: psi_max = 1 (k_f/l_f = 2), St 9.4:
  Sum lambda = 2 <= td - 1 - 1 = 3 ok. EVERY printed constraint holds.
The td=6 survivors have the same structure; recurring surviving IV-parent
families: (1/2,nu,2,(nu+1)/2) [R=2], (1/3,nu,3,(nu+1)/3) [R=3/2],
(1/3,nu,3,(2nu+1)/3) [R=3, survives only at Sum lambda <= td-4],
(1/5,2,5,1), (2/5,5s+4,5,2s+2) [R=5/3], and M=4 copies of the R=2 family.

## 6. Consequences

(i) CAMPAIGN td=6 TABLE (SHEET6-CAMPAIGN.md §5). Replace the single
hypothesis H3 by the PROVED kill set {(l)-test, (m)-test, psi-budget (*)}
(call it H3q; trust perimeter = the printed statements + H1/H4 + AF2 for
engine-lambda minima). Then:
- r2 and r3: both IV shapes killed by (*) (psi=2) => "EXCLUDED mod H3"
  upgrades to EXCLUDED (mod H1,H2,H4,AF2/AF3) — H3 no longer needed.
- r8/M2 and r9/M3 (both SANCTIONED): every IV hit has case IV impossible
  ((m) fails on every hit — §5a item 3) => IV side CLOSED; only their
  III-tails remain open.
- r6/M3: 6 surviving IV classes (all R in {2,3/2} reached at lambda <= 2)
  => r6 is now "open: 2 III-tails + 6 IV-survivor classes".
- r11/M5: 22 surviving IV classes + 8 III-tails => open, larger than
  previously booked.
- Superset entries (r8/M6, r9/M2, r9/M6): 30+8+45 = 83 more surviving
  classes (per-entry count; some shapes recur across entries), all
  conditional on AF3's menu being too generous (if AF3's sanction is
  proved, these vanish).
- NEW: td<=5 revalidation row r10/M4 (SANCTIONED) keeps 15 surviving IV
  classes. Row r10/M2 closes.
Net: the IV book shrinks from "~100 shapes, all hostage to H3" to
43 surviving (shape,lambda) classes on sanctioned entries (15 at td=5 +
28 at td=6), each pinned with Q-data and R in {3/2, 2, 5/3, 3}.

(ii) THESIS td<=5 PROOF (St 9.12, p. 60). G2 is CLOSED, in the thesis's
favor: every IV-terminal of every row-4 chain dies by St 9.4's (25) at
psi = ceil(R)-1 in {2,3}, computable from the terminal's own printed data,
with the printed lambda >= 2 annotations of St 9.6(iii)/(iv)/9.11 — no
engine input needed. St 9.12's proof is repairable verbatim: replace "or
(26) does not hold" by "or (25) fails for the psi certified by Prop 9.3
(IV)(l) at the terminal (via St 3.12 + St 3.17(i): psi l_f < k_f)". The
thesis's td>=6 theorem REMAINS incomplete as printed for the G3 rows: row
10/M4's surviving IV classes (plus rows 5,10 III-tails) are not killed by
any printed statement located here — so "incomplete as printed" is now
sharpened from "unwritten cases" to "cases the printed kill set provably
does not decide" (row 10 stays covered by Orevkov/Domrina/Zoladek
externally, as RECON already notes).

(iii) III-TAIL PRIORITY (campaign §6 items 2-3). PRIORITY RISES SHARPLY.
Every surviving IV chain in §5 passes through a case-III step (or IIb/
IIa_0 low-lambda steps) immediately before the IV-capable node — the
surviving IV-parents (1/2,nu,2,(nu+1)/2) and (1/3,nu,3,(nu+1)/3 or
(2nu+1)/3) are case-III children. The St 3.16/3.18 structural
admissibility extraction (item 3) would, if it forbids III at these
nodes, kill the IV survivors and the III-tails at once — it is now the
single highest-leverage open item for both td=6 EXCLUSION and the
independent-reproof gap at row 10/M4. Item 2's per-shape Diophantine
closure inherits the same targets. The two-pole (3,3) configuration
(item 4) and AF2/AF3 audits (items 5-6) are unchanged by this document.

## 7. Side findings + trust perimeter

- SF1 (NEW GAP, campaign-level): sequences can also TERMINATE at (0,y)
  via cases I/II/III (Prop 9.3's (I)-(III) do not exclude F = (0,y); only
  ONE of the four cases can apply, and which one depends on V_{1,a}/V_{2,a}
  membership of (0,y), i.e. on the root count of p_{(0,y)} — St 3.16).
  The engine models termination ONLY via case IV. A scan (h3_check.py,
  bottom) finds 28 CONT children with (nu_F, kap_F) = (1,1) — exactly the
  root's St 9.2 signature — all case-I self-loop shapes (1/2,1,2,1) and
  (1/3,1,3,1) at lambda >= 1..2, on r10/M4 and td=6 entries r8/M6, r9/M6,
  r11/M5 ((2,5),(3,5),(5,6) rows). If such a node is (0,y), the chain ends
  there consistently (k_f/l_f = 2 resp. 3, psi = 1 resp. 2 — budget holds).
  These are additional survivor-candidates OUTSIDE the IV book. Row 4 is
  unaffected (its printed possibility list contains no (nu,kap)=(1,1)
  shape, verified against St 9.6-9.11), so (ii) above stands.
- Trust perimeter of §4a: printed statements Lemma 2.1, Thm 6.1, St 3.12,
  St 3.17, Prop 9.3(IV), St 9.4/(25), St 8.1/8.3 — all read on-page here;
  plus the campaign's H1 (Prop 9.3 arithmetic) and, for engine-lambda
  minima only, AF2. The row-4 repair (§6(ii)) avoids AF2 entirely.
- The survivors of §5 are Q-level consistent chains (necessary conditions).
  Conditions NOT decidable at Q-level and not checked: 9.3(IV)(i)
  (nu_G = kappa_G), Puiseux-structural admissibility of each step
  (St 3.16/3.18 root patterns, campaign H4), realizability of the h-family.
  A survivor is a case the program must treat, not a counterexample to
  td >= 6.
- Adversarial self-check of §4a performed: (1) l_f = d_{(0,y)} needs only
  St 3.12's top-part identity + Lemma 2.1(i) (holds for f-a as for f);
  (2) the k_f-side uses only the PRINTED inequality of St 3.12; (3)
  St 3.17's hypotheses (F,G in V_a) are Prop 9.3's own hypothesis line;
  (4) applying St 9.4 to the full sequence F_0..F_n is exactly St 9.5's
  own printed usage; (5) psi = ceil(R)-1 < R <= k_f/l_f gives the strict
  psi l_f < k_f. No step uses unproven campaign hypotheses except where
  flagged (engine lambda minima = AF2).

## 8. Reproduction

    cd cases && python3 h3_check.py          # full sweep, ~4 min, exact
    # prints the §5 table counts, per-hit dispositions, survivor traces
    # (incl. the §5b exhibit) and the SF1 root-lookalike scan (28 hits).
    python3 sheet6_campaign.py report        # unchanged campaign digest

h3_check.py is read-only w.r.t. the campaign driver (imports step/
entry_nodes; BFS replicates bash() including budget/M=1/loop pruning and
depth cap 7).
