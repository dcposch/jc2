# Desk lane: SUBRECT-ORBIT-BRIDGE — does every degree-minimal counterexample admit the degree-preserving subrectangular gauge?

Integration #14 (charged) promotes, in GGV's scope, that a GGV-minimal
Jacobian counterexample (minimal B = gcd(deg P, deg Q) over ALL
counterexamples) can be moved by a degree-preserving change to a
standard subrectangular (m,n)-pair whose top form is a monomial x^u y^v
with u, v >= 1 — so nu = 2 and E_0 is a free vertex of the polar tree
(THEOREM FIRST-FORK). The producer had applied it to EVERY Aut × Aut
degree-minimal representative; the reviewer scoped it and raised
OPEN[SUBRECT-ORBIT-BRIDGE]: for an arbitrary counterexample F of
geometric degree N and its degree-minimal representative F_min in the
Aut(C^2) × Aut(C^2) orbit, does F_min admit a subrectangular gauge
preserving both degrees (hence with nu = 2)? Bounded quantity: nu(F_min)
∈ {1, 2, >= 3}, equivalently the number of distinct roots of the top
form of the max-degree coordinate at a degree-minimal representative.
Task, classical and exact: (1) State GGV's theorem precisely from
refs/ (guccione_valqui2017_ja471_shape_counterexamples.pdf is present;
hash it): what "minimal" means there, what the subrectangular normal
form is, and which of its steps use global minimality of B rather than
degree-minimality of the given pair. (2) Decide the bridge: is the
argument that makes the top form a monomial (a linear change of
coordinates plus the (LF) leading-form theorem l(P) = alpha H^d) valid
for ANY counterexample with H having >= 2 distinct roots after a linear
change — in particular, does H always have exactly two distinct roots
(up to linear change, x^u y^v) or can a degree-minimal pair have H with
3 or more distinct roots (nu >= 3, a FORK at E_0) or a single root
(nu = 1, E_0 a leaf)? Use (LF), (MIN), and the classical fact that for a
Jacobian pair the top forms' common factor H is a power of a linear
form only if an elementary automorphism lowers the degree (state and
prove or cite). Give a proof or a counterexample-shaped obstruction.
(3) Consequence: if nu = 2 holds for every degree-minimal
representative, integration #14's E_0-free conclusion and the vacuity
of CH2 become unconditional at every N; if nu = 1 is possible, CH2's
hypothesis is live for those pairs and E0-LEAF-CAP + Moh then bounds
them — compute what that gives; if nu >= 3 is possible, Psi >= D and
the fork mass is large — say what follows. (4) Controls: automorphisms
(nu = 1 after any non-linear elementary map; nu = 2 for (x, xy)-type
maps), the (LF) normal forms, and the N = 4 (B3) data. Discipline:
consume #14 at its scopes; MKS as a proposal where the review scoped
it; literature from refs/ with hashes or exact citation; no case (A),
no A2, no Z(G) = 1. Desk only (sympy allowed); state the bounded
quantity of any OPEN you raise; do not edit canonical ledgers; do not
inspect jc2-lean.
Report: xmodel/subrect-orbit-bridge-gpt55-20260902.md
Seal-at-completion; bounded writes; target 10-18KB; 60 minutes.
charged_input=xmodel/minimal-keller-shape-opus5-20260902.md
charged_input=xmodel/minimal-keller-shape-review-gpt55-20260902.md
charged_input=xmodel/integration14-coordinator-fable51-20260902.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
7b0ffec769314ce91a0831f7b2a88f5d5c8c97c08bfa56bd1e9bb8dbfb5c23f0  {{LANE_INPUTS}}/minimal-keller-shape-opus5-20260902.md
b1e09351164c134ec8aa74a7b905678e70021155b23add5bec9994e9f1268ac1  {{LANE_INPUTS}}/minimal-keller-shape-review-gpt55-20260902.md
bf1d428c7ddc03ab002410174b995cdd01e8a3c76c52475b03faf959b33da2ca  {{LANE_INPUTS}}/integration14-coordinator-fable51-20260902.md
```
