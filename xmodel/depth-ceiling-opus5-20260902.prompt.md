# Research lane: DEPTH-CEILING — the Puiseux depth at infinity of a degree-minimal Jacobian pair (flagship effort; the campaign's core question, restated)

Today's chain (integrations #12–#13 and the charged MINIMAL-KELLER-
SHAPE report, review running — consume it as a PROPOSAL and re-derive)
reduced the campaign's all-degree ceiling to one object and then
located it exactly: for a DEGREE-MINIMAL Jacobian pair (P, Q) (no
elementary automorphism on either side lowers D = max(deg P, deg Q);
by Moh D >= 101, by GGV/Heitmann D = K·max(d,e) with K = gcd >= 16, and
in the degree-preserving subrectangular gauge the top form is a
monomial x^u y^v), the satellite mass T = sum (nu_C − 1) c_C of the
base cluster at infinity satisfies T <= tau ⇔ D_min <= 2(tau + N) (in
H2 cells with one dicritical, W <= 3), so tau <= 50 − N would kill the
cell against Moh — and T is exactly the continuant data of the
satellite chains, i.e. the PUISEUX CHARACTERISTIC of the branches at
infinity of the generic pencil member. Newton-polygon theory pins only
the FIRST corner (GGV: u >= 4, v <= u(u − 1), u + v >= 16); the depth is
free. Every other instrument in the record (cusp cage, source curve,
boundary determinants, meridian floor, polar ledger, pencil genus)
produces floors only. The campaign's original GGV corner farm
(APPROACHES row 1, charged) stalled on "always a next pair" — the same
depth, seen from the corner side. This lane is charged with the depth
itself. Creativity and directness are wanted; a negative theorem with
an exact free datum is as valuable as a bound.
Tasks:
(1) STATE the object: the Puiseux (characteristic) sequence at infinity
    of a degree-minimal Jacobian pair — for the max-degree coordinate
    P (and for the generic member alpha P + beta Q) expand the branch(es)
    at infinity in x^{−1/m} (subrectangular gauge); define the
    characteristic pairs (m_1; beta_1, beta_2, …), the approximate roots
    (Abhyankar–Moh), and the correspondence between the characteristic
    sequence, the satellite chains of the base cluster, and T. Write the
    automorphism case (x, y + x^k) and the standard Jacobian-pair
    normal forms as controls.
(2) WHAT THE JACOBIAN CONDITION SAYS AT DEPTH. The classical analysis
    (Abhyankar 1977 lectures; Moh 1983; Appelgate–Onishi 1985; Nagata;
    Heitmann 1990; GGV 2010s "corner" papers; Cassou-Noguès) derives from
    [P, Q] = 1 a recursion on the successive corners/characteristic
    pairs of the pair: each corner of the Newton polygon (in the
    appropriate weights) is constrained by the previous ones, and the
    known bounds (Moh's 100, the excluded degree pairs, GGV's u >= 4 etc.)
    come from running that recursion a finite number of steps. Write the
    recursion down exactly (the "next pair" step): given the first k
    characteristic pairs of a Jacobian pair, what does [P, Q] = 1 force
    on the (k+1)-st? Where is the freedom (the free datum at each step),
    and what is its size? This is the "always a next pair" statement of
    the GGV farm — state it as a theorem or as a conjecture with the
    exact free parameter.
(3) THE CEILING QUESTION IN DEPTH FORM. T (equivalently the depth of the
    satellite chains, equivalently the sum over characteristic pairs of
    the continuant contributions) — is it bounded in the geometric
    degree N? N enters the depth recursion how? (The dicritical
    multiplicity mu and degree s, the sheet count over L_infty kappa,
    and W = N − a are read off from the resolution; which
    characteristic pairs do they touch?) Prove a bound T <= tau(N) if
    the recursion has one; if not, EXHIBIT the free datum: a family of
    numerical characteristic sequences satisfying every step of the
    Jacobian recursion with T → ∞ at fixed (N, W, S, kappa) — the
    depth-level analogue of the ledger-blind families — and say whether
    it is a numerical artefact (no actual polynomials) or realisable
    (GGV's cCa families were modular-only; say what is known).
(4) MOH'S METHOD REVISITED. Moh's 100-bound was obtained by the same
    recursion with computer assistance; state what limited it to 100
    (which step's branching) and whether N (the geometric degree, not
    D) enters anywhere in his argument — if it does not, the depth
    recursion is blind to N and a ceiling in N cannot come from it,
    which would be the decisive negative for the whole boundary
    program; if it does, name the step.
(5) CONSEQUENCES: price whatever you find against MOH-CROSS
    (D_min <= 100 kills N), the sharpened floor D_min >= 102 with a
    divisor K in [16, D/3], and the (B2)/(B3) cells.
Discipline: consume the reviewed ledgers (#12, #13) at their scopes;
the MINIMAL-KELLER-SHAPE report as a proposal; literature from refs/
(GGV, Moh, Heitmann are present — hash what you read) or with exact
citation and LITERATURE-TYPED marking; case (A) EMPTY; no Z(G) = 1; no
A2 cells. Desk-scale CAS (< 15 min, < 4 GB); state the bounded quantity
of every OPEN you raise; do not edit canonical ledgers; do not inspect
jc2-lean.
Report: xmodel/depth-ceiling-opus5-20260902.md
Seal-at-completion; bounded writes; target 25-40KB.
charged_input=xmodel/minimal-keller-shape-opus5-20260902.md
charged_input=xmodel/integration13-coordinator-fable51-20260902.md
charged_input=xmodel/integration12-coordinator-fable51-20260902.md
charged_input=xmodel/sat-mass-opus5-20260902.md
charged_input=APPROACHES.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
7b0ffec769314ce91a0831f7b2a88f5d5c8c97c08bfa56bd1e9bb8dbfb5c23f0  {{LANE_INPUTS}}/minimal-keller-shape-opus5-20260902.md
0b55a2c8bf7a8ab64fadf458e8a51bc5390bcb4808bd3c97d58a8769a97cc4a7  {{LANE_INPUTS}}/integration13-coordinator-fable51-20260902.md
ac0f48adf730dfb2d67b224cadb978fd1afc77bd71a2250127dee3ef3f60a644  {{LANE_INPUTS}}/integration12-coordinator-fable51-20260902.md
3fee2e6a8a2b18fdd54a5c6be913853c2ba1b09301e0729cc7c5271bb9797c2e  {{LANE_INPUTS}}/sat-mass-opus5-20260902.md
eed289e8fe1abf77b91e19c0aceea6b55c0300944f6b2eb9f5c5d471c330433b  {{LANE_INPUTS}}/APPROACHES.md
```
