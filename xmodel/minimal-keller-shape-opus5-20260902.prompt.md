# Research lane: MINIMAL-KELLER-SHAPE — what degree-minimality and the Jacobian condition force on the boundary tree (flagship effort)

The campaign's remaining price below N = 17 (integration #12, reviewed)
is a bound on a degree-minimal Keller pair against Moh's D >= 101. Two
lanes landed this hour (charged as PROPOSALS — their reviews run in
parallel; re-derive what you use) and say where the bound must come
from: (i) FORK-GENUS — on the resolution of the net <P, Q, 1> with polar
subtree T_+ = supp Z, 2 g_L − 2 = N − kappa − Lambda + Psi and Z·K_X =
Psi − Lambda − kappa (Lambda the leaf mass, Psi the fork mass of T_+), so
the anticanonical defect is the FORK MASS; Psi = 0 (polar tree a chain)
gives n(W − S) <= 2N − 2, and "E_0 a leaf of T_+" gives nW <= 2N − 2,
which kills every cell with N = 2W including the live N = 4 (B3) cell;
and NOETHER-K alone cannot produce a ceiling (a non-Keller family
matching every profile constraint has genus → ∞ while its affine
ramification term stays N − 1). (ii) SAT-WEIGHT / HALF-CAP — T = sum
(nu_C − 1) c_C with nu_C the SOURCE polar multiplicity and c_C the
proximity excess; T is invariant-blind (source composition keeps every
ledger entry and sends T → ∞) so it has content only for a
DEGREE-MINIMAL representative; and with one dicritical (forced when
W <= 3) D <= 2(T + kappa), so a bound T <= 50 − N on a degree-minimal
Keller pair closes the cell outright via Moh. Both halves reduce to
ONE question: what does "degree-minimal in the Aut × Aut orbit" plus
"Jac F ∈ C^*" force on the SHAPE of the base cluster at infinity — the
polar tree's branching (Psi) and the source polar multiplicities
(nu_C, hence T)?

This is classical territory that the campaign has not entered: the
NEWTON-POLYGON theory of Jacobian pairs. Your task:
(1) Assemble, with exact statements and hypotheses, the classical
    results on a Jacobian pair (P, Q) with Jac = const ≠ 0 that is NOT
    an automorphism: Abhyankar's and Nagata's theorems on the Newton
    polygons (they are similar; the leading forms are powers of a
    common form; the shape of the polygon at the top vertex; Nagata
    1988/1989 "Some remarks on the two-dimensional Jacobian
    conjecture" and "Two-dimensional Jacobian conjecture"), Appelgate–
    Onishi 1985 (the Jacobian conjecture in two variables: the
    principal parts and the "characteristic sequence" of the pair),
    Abhyankar–Moh's approximate roots and the semigroup of the place at
    infinity of a generic fibre of P (a one-place curve at infinity
    when P has one place; the characteristic pairs), Heitmann 1990
    (gcd(deg P, deg Q) >= 16 and the structure of minimal
    counterexamples), Nowicki–Nakai / Nakai–Baba, Moh 1983 (the
    100-bound and the list of excluded degree pairs), and the
    Cassou-Noguès / Kaliman results on the "Jacobian pair
    approximate-root tree". Use refs/ where present (hash what you
    read); otherwise state each theorem with its precise source and
    mark it LITERATURE-TYPED, not banked.
(2) TRANSLATE. The base cluster at infinity of the net <P^h, Q^h, z^D>
    is the resolution of the singularity at infinity of the general
    pencil member; its first stages are the Newton polygon and the
    Puiseux/characteristic pairs of the branch(es) at infinity. Express
    the polar tree T_+, its leaf mass Lambda, its fork mass Psi, the
    dicriticals and their (s_l, mu_l), kappa, and the satellite mass T
    in terms of the Newton-polygon and characteristic-pair data of a
    DEGREE-MINIMAL pair. For an AUTOMORPHISM (N = 1) all of this is
    known exactly (JvdK: the tree is the chain of the elementary word;
    T = word length data); write it out as the control.
(3) DECIDE, or price exactly: for a degree-minimal Keller pair of
    geometric degree N >= 2 (which by Moh has D >= 101 and by Heitmann
    gcd(deg P, deg Q) >= 16 with neither degree dividing the other),
    (a) is the polar tree a chain (Psi = 0)? (b) is E_0 a leaf of T_+?
    (c) is T bounded by a function of N — in particular T <= 50 − N —
    or does the Newton-polygon theory leave T free? Use the fact that
    minimality means no elementary automorphism (on either side)
    lowers max(deg P, deg Q): Abhyankar–Moh–Nagata characterise exactly
    when the top forms permit a reduction; the residual structure is
    the "irreducible" Jacobian-pair Newton polygon — what does it force
    on the FIRST characteristic pair, and hence on the first fork of
    the tree?
(4) TEST every statement on: the automorphism controls; the non-Keller
    PROFILE-WITNESS family psi_k∘(x, x y^4 − y^2) (it must FAIL the
    Keller-specific steps — say which); the two-dicritical witnesses of
    HALF-CAP's refutation; and the promoted N = 4 (B3) numerical data.
(5) CONSEQUENCES: for whatever you prove, the cells it kills via
    nW <= 2N − 2 or via D_min <= 2(tau + N) <= 100; for what you cannot,
    the exact typed OPEN with its bounded quantity and the single
    classical statement that would decide it.
Discipline: consume integration #12's polar ledger at its reviewed
typing; the two proposals only through re-derivation; MI/THEOREM
PROFILE at banked typing; case (A) EMPTY; no Z(G) = 1; no A2 cells.
Desk-scale CAS (< 15 min, < 4 GB); state the bounded quantity of every
OPEN you raise; do not edit canonical ledgers; do not inspect jc2-lean.
Report: xmodel/minimal-keller-shape-opus5-20260902.md
Seal-at-completion; bounded writes; target 25-40KB.
charged_input=xmodel/integration12-coordinator-fable51-20260902.md
charged_input=xmodel/keller-pencil-genus-opus5-20260902.md
charged_input=xmodel/sat-mass-opus5-20260902.md
charged_input=xmodel/n-vs-mapdeg-opus5-20260902.md
charged_input=xmodel/n-vs-mapdeg-review-gpt55-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
ac0f48adf730dfb2d67b224cadb978fd1afc77bd71a2250127dee3ef3f60a644  {{LANE_INPUTS}}/integration12-coordinator-fable51-20260902.md
5d2723e36476903392fd79b3791d1bd9830a0dea6f4693070ae8f89ccc06d6e1  {{LANE_INPUTS}}/keller-pencil-genus-opus5-20260902.md
3fee2e6a8a2b18fdd54a5c6be913853c2ba1b09301e0729cc7c5271bb9797c2e  {{LANE_INPUTS}}/sat-mass-opus5-20260902.md
ca9157617ecfd05fc21bffa6814aea830d1826c75b2ff7965c0128919f8da64a  {{LANE_INPUTS}}/n-vs-mapdeg-opus5-20260902.md
05d59097a3712d855ffd050aa8dc585af1860b606f53675340d0e334ea05c10b  {{LANE_INPUTS}}/n-vs-mapdeg-review-gpt55-20260902.md
```
