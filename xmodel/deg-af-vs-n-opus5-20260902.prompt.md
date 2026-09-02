# Research lane: DEG-AF-VS-N — the one gate between the ledger and a degree-monotone obstruction (flagship effort)

Today's (B3) flagship (charged) ran the counting-versus-covering table at
every N and found no crossing: the covering cap on g(E) grows with the
number of double points of A_F, i.e. with deg A_F-bar, and NOTHING in the
record bounds that in the geometric degree N. It concludes that
OPEN[DEG-AF-VS-N] is "the ONLY thing between the present ledger and a
degree-monotone obstruction". Two blind ideation submissions (charged)
sharpened the question: the RAW bound deg A_F <= f(N) is FALSE (target
automorphisms move A_F without changing N — Grok), and Chau gives
deg A_F = m·max(d,e) <= max(deg P, deg Q) with one place at infinity
(Opus; checked by GPT-5.5 with a notation repair), which N does not
bound (OPEN[N-VS-MAPDEG]). MPRIME (charged) says a bound n <= f(N)
converts directly into a beta-bound for (B2) at 5 <= N <= 16, and the
(B3) delta-budget delta(p,q) + sum t_i + delta_infty = (n-1)(n-2)/2
becomes a finite enumeration with it.

Your task: settle the CORRECT form of the question and prove the best
bound you can, or exhibit the obstruction to any bound.
(1) Define the invariant: n_min(F) := the minimal degree of A_{psi o F}
    over target automorphisms psi (equivalently the minimal degree of
    A_F-bar in its Aut(C^2)-orbit). Show it is well-defined and how it
    relates to (a) the number of double points k and the cusp type, which
    ARE Aut-invariant (the profile is), and (b) Chau's (m,d,e).
(2) Is n_min bounded in N? Attack from the dicritical side: A_F is the
    image of a finite map l' = A^1 -> A_F of degree s_l <= N/2 (MPRIME
    Lemma A, 7.B budget), so deg A_F = (deg of the parametrisation)/s_l;
    what bounds the parametrisation's degree after Aut-normalisation?
    Use Abhyankar–Moh/Suzuki (one place at infinity: the semigroup of
    the place), the Orevkov/Chau invariants, Riemann–Hurwitz on
    F|_{a~}: P^1 -> P^1 over the dicritical, and the determinant package
    of Domrina–Orevkov (which IS degree-free — the flagship's section 6).
    A bound of the form k <= C(N) on the number of double points is
    equally acceptable: it is what the delta-budget and the (B2)
    beta-bound consume.
(3) If no bound exists: construct a family of rational one-place curves
    with fixed profile data compatible with a fixed N and unbounded
    Aut-minimal degree, and say exactly which banked constraint fails to
    see it (this would type OPEN[N-VS-MAPDEG] as FALSE with a witness
    family — also decisive).
(4) Consequences either way, written out: for (B2) at 5 <= N <= 16 (the
    beta-bound via MPRIME's inequality), for (B3) at N = 4..8 (the finite
    list of the Chau lane's section 5), and for the all-degree program
    (does a bound k <= C(N) with C growing slower than the covering cap's
    slope produce the crossing the flagship's G-ANTI table lacks? compute
    the threshold).
(5) Literature custody: Jelonek's bounds on the degree of the
    non-properness set (in terms of deg F, not N) and any result bounding
    the degree of a curve by the degree of a finite étale map onto its
    complement — cite exactly or state ABSENT; no fetching beyond
    refs/ unless needed, and hash anything fetched.
Discipline: the flagship's theorems are UNREVIEWED proposals (its review
runs in parallel) — consume only its bookkeeping you re-derive; MPRIME,
HF, COMPANION at banked typing; the two ideation submissions are
proposals. Desk-scale CAS only (< 15 min, < 4 GB per job); qqideal 0.2.0
+ msolveio 0.2.1 are the default stack. Do not edit canonical ledgers;
do not inspect jc2-lean.
Report: xmodel/deg-af-vs-n-opus5-20260902.md
Seal-at-completion; bounded writes; target 25-40KB.
charged_input=xmodel/b3-e-geometry-opus5-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md
charged_input=xmodel/horn-flagship-opus5-20260902.md
charged_input=xmodel/chau-delta-budget-gpt55-20260902.md
charged_input=xmodel/companion-curve-alln-opus5-20260902.md
charged_input=xmodel/ideation-20260902T0741Z-grok46.md
charged_input=xmodel/ideation-20260902T0741Z-opus5.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
87fa5cb23ca59cf8f059a6710a1a460ebf323cee6166da43db2a75ea07666cb2  {{LANE_INPUTS}}/b3-e-geometry-opus5-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  {{LANE_INPUTS}}/horn-flagship-opus5-20260902.md
99ade6345041eef819cf8d76707091fb65feb7c8712c7626feb33204b15308dd  {{LANE_INPUTS}}/chau-delta-budget-gpt55-20260902.md
bf6b82e91c9441fea1998fb157289f44becf7cf6603b61b3c21c229272f4b943  {{LANE_INPUTS}}/companion-curve-alln-opus5-20260902.md
e30c80f34d04ceecf0575541401bb57956464925a894117920006072a7bd3f3e  {{LANE_INPUTS}}/ideation-20260902T0741Z-grok46.md
e67b2cd027e0cdbfc249d057d929e72a3e553ca61256f48b9978bedda358e9ce  {{LANE_INPUTS}}/ideation-20260902T0741Z-opus5.md
```
