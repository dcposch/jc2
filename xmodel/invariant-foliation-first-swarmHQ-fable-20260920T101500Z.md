# Hostile FIRST: invariant foliations force polynomial Keller invertibility

Reviewer: Fable5.1, requested effortmax; hosted identity NOT independently
attested. Lane invariant-foliation-20260920T100525Z, September 20, 2026.
Startup 10:19:02Z; partial saved 10:25:29Z. Review type: different-model
hostile FIRST of one frozen conditional proof. No generative round.
Contribution commit d5bc2d536f50caa815ad24049e348ece68f1639d; producer
public basis e906062fcaea8ee479c37ffd13b87dc1ee63f0ca; HQ governance basis
2df010a6fefcd68bc575b60e1230a4ca204e07b4.

## 1. Verdict

INVARIANT-FOLIATION-KELLER-1 is CONFIRMED at the producer's stated import
scope. Exact statement reviewed: a polynomial map F of the complex affine
plane with constant nonzero Jacobian determinant c, preserving (by pullback
invariance) any algebraic foliation, is a polynomial automorphism; likewise if
some positive iterate preserves one. All six charged interfaces are CONFIRMED
below, each independently reconstructed. No REFUTED or GAP interface.

Two non-blocking adjustments are recommended for integration, neither of
which changes the conclusion or requires a producer correction:

- Route EVERY fibration case (any generic genus) through the Section 5 pencil
  argument, and invoke Corollary B only for foliations WITHOUT rational first
  integral. The producer's text sends genus>=2 fibrations through Corollary
  B's terse "(Fib1)" branch, which is valid but relies on an unstated descent
  detail (Section 3 below). The pencil route needs no genus restriction.
- Record that the proof is robust even if Corollary B were read as producing
  the two foliations only for an iterate: the iterate clause and Interface 6
  already convert an invertible iterate into invertibility of F.

This is a conditional theorem. It supplies NO invariant foliation for a
hypothetical noninvertible Keller map, NO JC2 proof, NO rational-map
extension, and NO literature-novelty verdict (ROOT owns the bounded history
selection). It does not declare an exit price; no charge_basis line applies.

## 2. Interface verdicts

**Interface 1, primitive form and constant multiplier: CONFIRMED.** A
holomorphic foliation of the projective plane is algebraic by GAGA and restricts
to the affine chart as a nonzero rational one-form; clearing denominators and
dividing by the gcd gives a primitive polynomial form omega=A dx+B dy with
gcd(A,B)=1, isolated zeros allowed. Pullback: the coefficient vector of
F*omega is the transposed Jacobian matrix applied to (A(F),B(F)); I checked
this by expanding A(F) dF1+B(F) dF2. Because det DF=c is a nonzero constant,
the adjugate divided by c is a polynomial inverse, so the coefficient ideal of
F*omega equals (A(F),B(F)). If an irreducible q divided both coefficients, the
curve V(q) would map into V(A,B). That set is finite: a one-dimensional
component with irreducible equation p would give p dividing A and B by the
Nullstellensatz and primality, contradicting coprimality. Keller maps are
etale hence quasifinite, so no curve maps into a finite set. Thus F*omega is
primitive. Preservation means F*omega and omega are proportional over C(x,y);
F*omega is nonzero since F is dominant. Writing the ratio p/q reduced, q
divides both A and B, hence is a unit; then p divides both primitive
coefficients of F*omega, hence is a unit. So the multiplier is a nonzero
constant. No properness, surjectivity, or unit-ideal claim is used; the zero-
coefficient case forces the other coefficient to be a unit and is covered.

**Interface 2, curl identity and integration: CONFIRMED.** With
d omega=h dx wedge dy, h=B_x-A_y, differentiating F*omega=lambda omega gives
F*(d omega)=lambda h dx wedge dy, while F*(h dx wedge dy)=c h(F) dx wedge dy.
Hence c h(F)=lambda h. Nonconstant h: h(F)=(lambda/c)h is a nonconstant
polynomial pencil with a linear base map, and the accepted pencil theorem
applies at exactly its stated scope. Zero h: omega is closed; integrate A in x
to H0, then B-partial_y H0 has zero x-derivative by closedness, so it is a
polynomial in y alone with a polynomial antiderivative; H=H0+G satisfies
dH=omega, nonconstant since omega is nonzero. Then d(H(F)-lambda H)=0 gives
H(F)=lambda H+b, again a pencil with nonconstant base map since lambda is
nonzero. Remaining case: h a nonzero constant, so c h=lambda h forces
lambda=c. Reconstructed without gaps.

**Interface 3, two distinct foliations: CONFIRMED.** Distinct foliations on
the projective plane restrict to distinct foliations on the dense affine
chart, so primitive forms omega1, omega2 are not proportional over C(x,y).
Unless one of them already yields a pencil by Interface 2, both curls h1, h2
are nonzero constants and both multipliers equal c. Then
eta=h2 omega1-h1 omega2 has d eta=(h2 h1-h1 h2)dx wedge dy=0 and
F*eta=c eta. It is NONZERO: eta=0 would make omega1 and omega2 proportional
with nonzero constant ratio, contradicting distinctness. Interface 2's
integration gives a nonconstant polynomial H with H(F)=cH+b, and the pencil
theorem applies. No wedge-constancy, determinant, or common integrating
factor is assumed anywhere; primitivity of eta is not needed because the
pencil theorem imposes no primitivity. Using one foliation twice gives
eta=0 and is excluded, as the producer states.

**Interface 4, Corollary B: CONFIRMED with the adjustment in Section 1.**
Details in Section 3. The hypothesis "not tangent to a rational or elliptic
fibration" means the foliation is not itself such a fibration. The
statement concerns the same rational map on the same surface, not a cover
or an iterate; the proof descends each second foliation to the quotient by
G-invariance or uniqueness and transports it across the birational
conjugacy. On the projective plane the second foliation is algebraic by
GAGA, so Interface 1 applies to it. Theorem C, the holomorphic-endomorphism
classification, is not used and would not apply, since the extension of F
to the projective plane is in general only rational.

**Interface 5, fibration exception: CONFIRMED.** If the foliation is a
fibration with rational first integral r, choose the Stein-factored
primitive base: resolve r on the projective plane to a morphism from a smooth
projective rational surface X, Stein-factor through a smooth curve C with
connected fibers. Since the direct image of O_X is O_C, the Leray sequence
injects H1(C,O_C) into H1(X,O_X)=0, so C is P1 with function field C(r')
for some r' in C(x,y), relatively algebraically closed in C(x,y) because the
generic fiber is geometrically integral (generic smoothness in
characteristic zero). Passing to r' is necessary: a non-primitive r=g(r')
need not satisfy a semiconjugacy. Invariance gives d r' wedge d(r'(F))=0,
so r'(F) is algebraic over C(r') (in characteristic zero, vanishing wedge of
differentials means algebraic dependence), hence lies in C(r') by relative
closure: r'(F)=phi(r'). It is nonconstant because F is dominant and r' is
nonconstant. The accepted theorem covers any nonconstant rational pencil,
including affine base points of r' and any generic genus, so the
rational/elliptic restriction is never used here.

**Interface 6, N=1 and iterates: CONFIRMED.** Generic degree one makes F a
birational Keller map, and the inherited endpoint gives an automorphism. For
N>1, the extension is a dominant non-invertible rational self-map, so
Corollary B or Interface 5 applies and yields invertibility, a contradiction;
the structure is sound. Iterates: F^m is polynomial Keller with determinant
c^m; if G is its polynomial inverse, then G commutes with F (multiply
F^m F=F F^m by G on both sides), and G F^(m-1) is a two-sided polynomial
inverse of F. No modulus, exact-area, or dynamical-degree assumption enters:
lambda=c is derived, and the pencil theorem holds for every nonzero c. There
is no circularity: the theorem assumes a preserved foliation and only
manufactures a SECOND one from Corollary B; no foliation-existence theorem
for arbitrary Keller maps is used or implied. Accepted pencil dependencies
are inherited; I found no concrete new doubt warranting a foundation re-audit.

## 3. Corollary B: exact reading

Read via pdftotext from the local author PDF: page 2 (statement) and pages
16-17 (complete corollary proof and Theorem A proof). Statement, in
paraphrase: a dominant non-invertible rational self-map of a projective
surface that preserves a holomorphic foliation not tangent to a rational or
elliptic fibration preserves at least two foliations. The authors' own
necessity example, the non-Keller map (x,y)->(x^2,xy^2) preserving only
x=constant, confirms that "tangent to" means the foliation IS the fibration.

Proof structure as printed. Without first integral and Kodaira dimension 0:
by Theorem 4.3 the triple is birationally conjugate to a quotient by a
cyclic automorphism group G of a listed model. Cases kappa0(2)-(4): a unique
invariant rational fibration, automatically G-invariant, so the original map
preserves a rational pencil (distinct from the given foliation, which has no
first integral). Cases kappa0(1) and (5): the linear part of the lift is
diagonalizable and commutes with G, so two common fixed points on the
projective line of directions give two G-invariant linear foliations. I
checked the linear-algebra step: distinct eigenvalues force a commuting
matrix to preserve each eigenline; a scalar lift leaves the finite-order
generator's eigenlines. Kodaira dimension 1: Theorem 4.4; kappa1(1) has two
explicitly G-invariant rational fibrations, kappa1(2) a unique invariant
elliptic fibration. Fibration neither rational nor elliptic: "(Fib1)".

To understand (Fib1) I additionally read the statement of Theorem 4.6 on
pages 14-15 (grep window): up to birational conjugacy and finite cyclic
cover, a preserved fibration of positive fiber genus with base genus at most
one is a product B x F with a product map. There the second foliation is the
horizontal projection. Its descent to the quotient is not spelled out in the
corollary proof; under the corollary hypothesis the fiber genus is at least
two, the automorphism group of the fiber is finite, so a fiber-preserving
automorphism of the product acts on the second factor by a constant
automorphism and preserves the horizontal foliation. This closes the branch,
but the producer's theorem does not need it: Interface 5 handles every
fibration. Hence the Section 1 adjustment.

Remaining named imports, not audited: Theorem A's reduction (Miyaoka and
McQuillan models, Proposition 3.4 excluding general type, Proposition 4.7
excluding modular foliations), the normal forms of Theorems 4.3 and 4.4
including diagonalizability of the lift and the explicit groups G, and
Theorem 4.6. Page 1 (Theorem A statement) was read in a grep window. The
paper's formal definition of preservation was not located in my grep of
pages 3-4; I used the standard meaning, pullback of the foliation equals
the foliation, which is what the producer's affine identity expresses.
Custody caveat: this is the July 8, 2009 author preprint; agreement with
the published version is not verified, since no network retrieval is
authorized. The producer's paraphrase is accurate to the local text.

## 4. Controls

Identity and diagonal automorphisms (alpha x, beta y): dx pulls back to
alpha dx, curl zero, H=x, H(F)=alpha x; consistent. The form x dy-y dx is
primitive with an isolated zero at the origin; the diagonal map pulls it
back to alpha beta times itself, its curl is the constant 2, and
c h(F)=lambda h gives lambda=c=alpha beta, matching Interface 2. The
non-Keller map (x^2,y) pulls dx back to 2x dx: the multiplier is
nonconstant precisely because the Jacobian matrix has no polynomial inverse,
isolating the role of etaleness in Interface 1. Two copies of one foliation
give eta=0, correctly excluded. No computation was needed or performed.

## 5. Exact dependencies

- RATIONAL-PENCIL-UNIFICATION-1 (accepted, PROMOTED per the frozen
  integration): used for polynomial pencils h, H (Interfaces 2-3) and for
  the rational pencil r' (Interface 5), all at its binding scope. Its named
  resolution, Stein, curve, nonproper-value and hyperbolic-moduli imports
  are inherited unchanged.
- Birational Keller endpoint (accepted): Interface 6.
- Favre-Pereira Corollary B, local author PDF, named theorem import with
  the dependency list in Section 3.
- Classical facts reconstructed or checked here: primitive polynomial
  representatives; GAGA algebraicity of holomorphic foliations on the
  projective plane; birational transport of foliations and invariance;
  etale implies quasifinite; resolution and Stein factorization; H1(O)=0 for
  smooth projective rational surfaces; characteristic-zero wedge criterion
  for algebraic dependence; the polynomial Poincare lemma (Interface 2).

## 6. Read scope, omissions, custody, and completion

Whole-read: the nine charged snapshots under /tmp/jc2-lane.nEjGqM/inputs and
the four frozen HQ governance files via git show at the governance pin. PDF
pages read: 2 and 16-17 whole; grep windows on pages 1, 3-4, 14-15 as stated.
Not read: mutable STATE, peer reports, additional Git history, other
repository files, jc2-lean, jc2-web. No network, CAS, delegation, or model
calls. Authored outputs: the chmod-444 startup ACK at
/home/ubuntu/swarmHQ/runtime/invariant-foliation-20260920T100525Z/FABLE-STARTUP.md
and this report. Deviation disclosed: my first draft write failed (missing
patch terminator) and was repaired immediately at 10:19Z before any evidence
reading. Bash tool output was not clipped for any read. Hosted model identity,
cost and absence of other side effects are not independently certified. This
report is not sealed; legacy parent custody applies.

## Read manifest (excluded from word count)

Pre-hash 10:20:00Z, post-hash 10:27:12Z and a full sha256sum -c comparison at
10:29:28Z all matched the pinned SHA256:
README.md 7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf;
AGENTS.md 31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f;
COORDINATION.md 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e;
APPROACHES.md 2ec3b6a4c1531308747fa9b0b30c3d17d353b826f29184f00aea6e0a3919e741;
FALLACY-v2.md e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5;
invariant-foliation-keller-swarmHQ-root-20260920T100525Z.md
1ccc0fc8d9f70ca9d9743efee2d63aa5d390219f0f87fb045be88d543e7a9054;
its .artifact.json
40cedeb33602a6167ba53ef0a3e0853cf301d7a50f632566d517644bd3245423;
rational-pencil-unification-swarmHQ-root-20260920T033600Z.md
3e0fa8f18601be655958dd3712df60fdcf9b30e0ab07daa4c39928f1a2c022b9;
rational-pencil-unification-integration-swarmHQ-root-20260920T040300Z.md
433840900e0edd661cce65557e1f05b8fbf8acc4dd00f90ece863c9d82896926.
HQ pins at 2df010a6: AGENTS.md 06ba4c08...0c34f, POLICY.md 29d6bcea...2393,
RESEARCH_POLICY.md 710fcf0c...0778, RUNBOOK.md 67f2cbff...7c81 (full values
matched the prompt's pins). PDF favre-pereira-ratfol6.pdf
fb63dcf42b7ebe436f819749751011aadbfc6a59e5e790c2be4af41ac2cb2f9a, mode 444,
308050 bytes, 17 pages, CreationDate 2009-07-08, unchanged pre/post.
Tools: claude, node, apply_patch present and executable;
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 recorded; no other environment recorded.

## OPEN(S) RAISED

None. No bounded experiment, control family, or descendant is proposed.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Trusted command `python3 ops/open_collision.py <this-report> --root .` run at
10:29:28Z on the completed body returned EMPTY; the block above reproduces
its output. It checks identifiers, not novelty.

Author completion (body): 2026-09-20T10:30:28Z, after whole-body readback and correction
of one wording passage and one manifest line. The completion marker is
appended immediately after readback of the changed passages, as the last
writing.

<!-- BODY-END -->
