# Ideation round 20260902T1608Z — coordinator's own blind submission (Fable 5.1)

Written before reading any other submission of this round (GPT-5.5 and
Grok had sealed; neither opened). Packet ab66bd6b, basis 7f7c0306.
Everything below is PROPOSAL unless it cites a bound integration.

## 0. Verdict up front

1. **The one-directionality is not an accident of the instruments; it
   is an identity.** Write m = deg P = Kd, n = deg Q = Ke, gcd(d,e) = 1,
   and let e_i, e'_i be the multiplicities of the two pencils {P = c},
   {Q = c'} at the i-th infinitely near base point at infinity (the
   total-transform basis, E_i² = −1). Then A² = 0, B² = 0, A·B = N for
   the fibre classes A = mL − Σ e_i E_i, B = nL − Σ e'_i E_i on any
   common resolution, so
   Σ e_i² = m², Σ e'_i² = n², Σ e_i e'_i = mn − N, and therefore

       2·d·e·N = Σ_i (e·e_i − d·e'_i)².                       (LATTICE)

   N is the squared distance of the two multiplicity sequences from
   proportionality, divided by 2de. Every i where (e_i, e'_i) is
   proportional to (d, e) contributes ZERO, and those are exactly Moh's
   proportional (minor / distribution-detector) discs: DETECTOR-NULL is
   the term-by-term form of (LATTICE). The degree D = Ke lives in
   Σ e'_i² = K²e², i.e. in the LENGTH of the proportional part; N lives
   in the divergent tail. That is why every boundary instrument gives
   D ≥ (something in N) and N ≤ (something in D): (LATTICE) is a sum of
   squares whose zero terms carry all of D. This restates the campaign's
   polar ledger (NOETHER-K's Σ a_i² = D² − N is the same quadratic form)
   as the reason, not a symptom.
2. **Consequently OPEN[UPPER-TO-FLOOR] has a definite answer on the
   boundary: NO.** Any function of the boundary tree that is invariant
   under lengthening a proportional chain (V_j ↦ V_j + 1 inside a
   Def 5.1(2) window) cannot bound N below by D, because (LATTICE) is
   invariant under it and the windows are nonempty at every D (the
   census to D ≤ 400). The only boundary datum NOT of this kind is the
   bottom of the tower (OPEN[D1-SUBTREE]), and there the best a
   Jacobian-forced minimum can do is N|_{D_1} ≥ (number of bottom-major
   discs) — a floor in the number of proper places, i.e. in
   PLACE-LEDGER data, not in D. So the D1 lane can make the filter
   two-sided in PLACE data but cannot, even in the best case, produce
   D ≤ C(N). I predict it returns exactly that, and that this should be
   banked as THEOREM UPPER-ONLY (boundary).
3. **A concrete error in the freshest record (P1, coordinator-caught).**
   The N-ON-THE-TREE lane and its review took N_min = 4 from the H2
   window of integration #14. The record's counterexample frontier is
   N ≥ 6 (notes LIVE STATE 01:10Z, "N=5 SOUNDLY CLOSED BY DEPENDENCY
   AUDIT; CE FRONTIER MOVES TO N>=6"; unconditional, not H2). The
   operative test is therefore U ≥ 6, not U ≥ 4: every skeleton with
   U < 6 is dead, including all 418 "pinned to N = 4" groups at
   D ∈ [101,200] (which are DEAD, not realisation targets — integration
   #16 §C and §D.3 must be corrected), and the survivor windows are
   [6, min(⌊U⌋,16)]. A recount at D ≤ 400 with N_min = 6 is running on
   one core; it is a delta to #16, not a reversal: FILTER-INVERSION and
   the CANNOT list stand.
4. **Is the ceiling the right target? No.** A ceiling D_min ≤ C(N) for
   hypothetical counterexamples is a statement about all degrees at
   once, and by (LATTICE) it cannot come from the boundary; the only
   degree-growing orbit invariants a general map has (deg Jac, the
   critical curve, the discriminant) are identically zero for Keller
   maps. What is left is the Jacobian IDENTITY as an identity, which
   is the all-degree program. The N-first strategy has therefore done
   what it can: it has typed the residual (cells, windows, skeleton
   lists) but cannot close it by crossing with Moh. The campaign should
   say so and put the flagship seats on the all-degree formulation
   below, keeping the cell machinery as the verifier of whatever that
   produces at small N.

## 1. The new avenue: the Jacobian condition as a PERIOD condition on
##    one polynomial, and its degree content

Let f be a Keller polynomial (no critical points; a counterexample's
P). Then f has a Jacobian mate g iff

    dx∧dy ∈ df ∧ dC[x,y],   i.e.  [dx∧dy] = 0 in H''_f := Ω²/(df∧dΩ⁰),

the Brieskorn module of f. (Proof: df∧dg = [f,g] dx∧dy; conversely
1 ∈ (f_x, f_y) gives a solution (a,b) of a f_x + b f_y = 1, all
solutions are (a + h f_y, b − h f_x), and the closedness of
−b dx + a dy is the equation [f,h] = div(a,b), solvable iff
div(a,b)·vol ∈ df∧dΩ⁰; H¹_dR(C²) = 0 then integrates.) Equivalently,
the Gelfand–Leray form ω = dx∧dy/df has all periods zero on every
fibre: for every c and every γ ∈ H_1(f = c), ∫_γ ω = 0, and every
residue of ω at every place at infinity of f = c is zero.

Three things follow that the boundary tree does not see.

(a) **N as pole orders of ω.** On the fibre f = c, ω = dg, so at a
    place at infinity where g has a pole of order ν, ω has a pole of
    order ν + 1, and where g is finite (a non-proper place, mapping
    into A_F) ω is regular. Hence
    N = Σ_places (−ord_place ω − 1)⁺ = Σ_places (a_place + ord_t f_y|branch)⁺,
    with a_place the pole order of x on the branch. This is FRONTIER-N
    with the Jacobian condition built in: the pole order of the POLAR
    f_y along each branch at infinity of f = c replaces the
    g-tree. The polar is a polynomial of degree m − 1 whose behaviour
    along the branches of f = c is a classical object (the polar
    quotients / Teissier–Merle at infinity), and N ≤ 16 says every
    proper place has pole(f_y|branch) ≥ a_place − 16: the polar is
    asymptotically tangent to the fibre at every proper place. That is
    a statement purely about f.

(b) **The residue conditions are conditions on the proportional chain.**
    Res_{place}(dx/f_y(x, φ(x))) = 0 at every place of every fibre. The
    x^{−1} coefficient of 1/f_y along the branch φ involves ALL the
    tame coefficients of φ between two characteristic exponents, i.e.
    the coefficients Moh's recursion treats as free once the V_j are
    chosen. This is the first equation of the record that couples the
    inside of a proportional chain to the Jacobian condition. By the
    global residue theorem the residues at the r_f places of a fibre
    sum to zero, so there are r_f − 1 independent residue equations
    per fibre, and 2g_f further period equations (γ running over the
    cycles of the fibre, which for a Keller f are all vanishing cycles
    at infinity). The count 2g_f + r_f − 1 = rank H''_f is the rank of
    the Gauss–Manin system of f; JC2 in this language is:

       a Keller f with [vol]_f = 0 has rank H''_f = 0
       (generic fibre ≅ C, so f is a coordinate by Abhyankar–Moh–Suzuki).

(c) **Where the degree enters, honestly.** The relation vol = df∧dg
    realising [vol] = 0 has degree m + n − 2 ≥ 208 at the admissible
    degrees, while the module H''_f is "generated" in degrees governed
    by the Newton polygon at infinity of f (the spectrum at infinity;
    Sabbah, Dimca–Saito for non-tame f). A theorem of the form "if
    [vol] = 0 then it is zero already in degree ≤ B(Newton data)" would
    be a CEILING, the first of the campaign; whether such a bound exists
    for non-tame f is exactly the question of the regularity of the
    Gauss–Manin system at infinity of f. I do not claim it. I claim it
    is the one place where a degree ceiling is even the right type of
    statement, because the unknown is a relation, not a multiplicity.

## 2. Idea cards

**CARD 1 — RESIDUE-AT-THE-BOTTOM (bridges to D1-SUBTREE).** For the
smallest surviving skeleton at D = 105 (after the N_min = 6 recount),
write the generic branch of f = c below the last major disc with
undetermined tame coefficients, compute the residue of dx/f_y along it
symbolically, and ask whether Res = 0 admits solutions with contact to
the g-roots unbounded (N|_{D_1} → 0). Dependencies: box/moh_skeleton_N.py
for the skeleton; sympy Puiseux at depth ≤ 3. Cheapest discriminator:
the residue as a polynomial in the tame coefficients — if it is
identically zero along the chain the period route says nothing new at
the bottom; if it is a nonzero polynomial its zero set is the true
D_1-subtree. Interpretation: (i) Res ≡ 0: THEOREM UPPER-ONLY, bank and
redirect; (ii) Res ≢ 0 with solutions: the D1 residue is a floor of
PLACE type, not D type — still UPPER-ONLY for the ceiling; (iii) Res
≢ 0 without solutions at some skeleton: that skeleton dies — a genuine
endgame kill. Stop condition: 2 h desk CAS. Gain: decides the boundary
route on a real skeleton rather than in the abstract.

**CARD 2 — PERIOD-RANK.** Compute rank H''_f (= 2g_f + r_f − 1) for the
generic fibre of a surviving skeleton from its Puiseux data (g_f from
the resolution graph, r_f from the dicritical degrees) and compare with
the number of independent conditions the residues + cycle periods
impose on the tame coefficients. If conditions ≥ free coefficients at
every skeleton of the admissible list, the endgame is a finite
elimination and the census machinery already exists. Dependencies:
CARD 1's residue formula, the (B3) boundary census. Discriminator: the
integer (conditions − unknowns) at D = 105. Stop: one skeleton.

**CARD 3 — CHAR-p CROSS-CHECK (cheap, different in kind).** A char-0
counterexample with N ≤ 16 reduces, for every p > 16 not dividing
finitely many integers, to a separable Keller map over F_p with the
same N and degree, p ∤ N, that is not an automorphism for almost all p
(an automorphism mod p for infinitely many p with inverse degree ≤ D
lifts). So JC2 ⟸ "a separable Keller map over F̄_p with p ∤ N is an
automorphism". In char p the derivations ∂_P = {Q,·}, ∂_Q = {·,P} are
restricted: ∂_P^p is again Hamiltonian and vertical, so Q^{[p]} is a
first integral of both flows. Discriminator: whether p ∤ N forces the
p-curvature to vanish AND vanishing p-curvature forces p | N (the
Artin–Schreier example (x + x^p, y) has both p-curvature 0 and N = p).
If both hold, JC2 follows; each is a finite-field statement checkable
on the char-p Keller maps of degree ≤ 6 by brute force (a weekend
box01 job). Gain: an all-degree, all-N mechanism that is not the
boundary; expected outcome: the second implication fails, but the
failure exhibits what a char-p counterexample must look like.

## 3. Disposition vector (changes only)

- Row 1 (GGV next pair / Moh endgame): RAISE to the flagship; run it in
  the period form (§1) rather than the recursion form.
- Rows on boundary instruments (cage, DO package, meridian floor, polar
  ledger, pencil genus, satellite mass, depth, N-on-tree): RETYPE all as
  "floor / window instruments, closed for ceilings" per (LATTICE).
- Row 20 (characteristic p): RAISE (CARD 3); it was never run as a
  formalism.
- Candidates (a)–(f) of the packet: (a) continue, expected UPPER-ONLY;
  (b) LOWER — Chevalley–Weil and the étale structure of E are
  topological, hence floors by the same quadratic-form argument;
  (c) RAISE; (d) MERGE into §1 (the Hamiltonian flow of X_P IS the
  Gelfand–Leray form; its completeness is the period condition);
  (e) LOWER (growth inequalities are degree floors); (f) RAISE and
  CLOSE: (LATTICE) is the theorem, at the level of the skeleton.
- Reducible branch: unchanged; no instrument today touched it.
- A2 residual: unchanged, deferred.

## 4. Bottlenecks reranked

Proof: (1) an all-degree mechanism; the period formulation is the
candidate with degree content; (2) Moh's endgame at the admissible
degrees as a finite elimination (CARD 2); (3) the reducible branch.
Disproof: (1) the finite skeleton list with U ≥ 6 at D ∈ {105,…,120}
(recount pending) — realisation via the census pipeline; (2) nothing
else concrete.

## 5. Strongest attacks

Proof: §1(c) — a degree bound for the vanishing of [vol] in the
Brieskorn module of a non-tame polynomial, in terms of its Newton data
at infinity. Counterexample: take the skeleton with the smallest U ≥ 6
at D = 105 and try to realise its major tower with undetermined bottom
coefficients, imposing the residue equations of CARD 1 rather than the
full Jacobian system; the residues are polynomial in far fewer
unknowns than the (B3) cells.

## 6. Experiment / software

The N_min = 6 recount (running); then a `--nmin` option and a
per-skeleton residue exporter in box/moh_skeleton_N.py (CARD 1 needs
the branch data the census already computes). Campaign-systems check:
UPGRADE — the operative N_min must be read from one canonical place
(AUDIT's frontier line), not re-derived by lanes; smallest test: grep
every sealed report of today for "N_min" or "N >= 4" and list the
consumers (the N-ON-THE-TREE pair is the first known miss).

## 7. Current lanes

d1-subtree: CONTINUE, with the reading of §0.2 (a PLACE floor is the
ceiling of what it can give). Cluster census: CONTINUE to cap.
Box03: stay stopped. A2 / (B3)-census lanes: stay deferred.

## 8. Opens raised (bounded)

OPEN[NMIN-CONSUMPTION] — bounded quantity: the number of sealed reports
since 01:10Z that use N_min = 4 or an H2 window [4,16] as the operative
frontier (first two: n-on-the-tree and its review).
OPEN[VOL-DEGREE] — bounded quantity: the least degree of a relation
dx∧dy = df∧dg for a Keller f with rank H''_f > 0, as a function of the
Newton polygon at infinity of f; the ceiling question in its only
well-typed form.
OPEN[RESIDUE-CHAIN] — bounded quantity: the number of independent
residue equations on the tame coefficients of one proportional chain of
length V (CARD 1 answers it at V ≤ 3).

<!-- BODY-END -->
