# Finite-normalization relative duality: actual-source gap check

Producer: Astra (gpt-6-astra), swarmHQ native lane source_boundary_bypass.
Basis: 49d9c0d9bc23f14ffaa5e4b81521498889663591.
Evidence: MANUAL. Lifecycle: PRODUCER-CHECKED, UNPROMOTED.
Scope: one bounded all-degree actual-source test; no calculation, family
extension, imported proof of JC2, or different-model FIRST.

## Assignment and literal rings

For an assumed complex polynomial Keller map F=(f,g), normalize its
Jacobian to one. Put A=C[f,g], R=C[x,y], K=Frac(A), L=Frac(R), and let
S be the integral closure of A in L. The accepted full-normalization
attachment gives A subset S subset R and the open immersion
j:Spec R=A2 -> Y=Spec S; pi:Y->Spec A is finite. Let B be the omitted
prime divisors and Ram the ramification divisor of pi. The task is to
extract a new closing consequence from the relative dual/codifferent,
using the whole-plane open and ramification supported on B.

## Research outcome

GAP / NO_NEW_CLOSING_TEST. The literal whole-plane source places the
codifferent inside the polynomial source ring, but does not make it an
algebra or make its quadratic traces regular on the target. The proposed
multiplication shortcut therefore returns to the existing trace-regularity
gap. No new boundary-class incompatibility was obtained. This is a stop
record, not a new conditional route selected for investment.

## 1. Fixed-form identification and the sign check

Use field trace Tr=Tr_(L/K) to identify the relative dual with the fractional
S-module

    M = {h in L : Tr(hS) subset A} = Hom_A(S,A).

The equality means h corresponds to the functional s -> Tr(hs), not an
unspecified module isomorphism. Finite normal surface normalization is CM
and finite flat over the regular two-dimensional A. Thus S and its A-dual
are finite projective A-modules. The accepted structure-morphism finite
duality identifies M*(df wedge dg) with omega_Y. On the smooth source
open, df wedge dg=dx wedge dy. Consequently each h in M is a regular
function on the WHOLE source, so

    S subset M subset R.

The first inclusion also follows directly because traces of integral
elements belong to the normal ring A. This inclusion is not the opposite
one: the codifferent permits poles on omitted ramification components.
For a height-one prime T of S of ramification index e_T, the tame
codifferent formula is

    M_T = t^(1-e_T) S_T = O_Y(Ram)_T,

up to a local unit and the fixed trace identification. Equivalently,
df wedge dg vanishes to order e_T-1 relative to a local canonical
generator. These statements agree in sign. Reflexivity gives the global
identification M=Gamma(Y,O_Y(Ram)). At e_T>1 the local inclusion S_T in
M_T is strict, so globally M differs from S; localization of the finite
module cannot hide that strictness. No arbitrary rational local function
has been declared a global source polynomial.

Rational or sandwiched singularities are not used in this argument.
Normal CM/reflexive duality is enough. No conclusion that omega_Y is
globally free follows from local freeness in codimension one or from
its trivialization on the open source.

## 2. Multiplication and quadratic trace do not acquire the missing bound

If M*M subset M, then 1 in M and M finite over A would make M a finite
A-algebra inside L. Every element would be integral over A, hence in its
integral closure S. Thus M=S and no ramification would remain. This is a
sufficient extra premise, not a consequence of M subset R. Multiplying
two source polynomials keeps them in R but may double their permitted
negative boundary valuations.

A compact version of the same gap is available without asking for full
multiplication closure. Since S is finite projective over A and the
generic trace pairing is perfect, its double trace dual is S:

    {z in L : Tr(zM) subset A} = S.

Suppose Tr(h^2) belongs to A for EVERY h in M. Polarization in
characteristic zero gives

    2 Tr(hk) = Tr((h+k)^2)-Tr(h^2)-Tr(k^2) in A,

so M is contained in its trace dual S. Therefore, under a hypothetical
nontrivial source normalization, some polynomial h in M necessarily has
Tr(h^2) outside A. This is an elementary diagnostic description of the
same obstruction, not a source contradiction: no reason was found that
these quadratic traces must be target polynomials. The campaign already
distinguishes polynomiality on the source from regularity of field trace
on the target. In particular, no trace-image theorem supplies this A
membership merely because h is a source polynomial.

This does not propose a computable two-moment test on a known basis of an
actual counterexample: no counterexample, S, M basis or offending h is
available. It supplies no effective degree or pole cutoff for arbitrary
source elements and is not a successor to the stopped moment families.

## 3. Negative control with the exact volume retained on a punctured source

Take just the fixed double-cover control

    A0=C[a,b], S0=C[t,w], a=t^2, b=w,
    R0=C[t,t^-1,v], w=v/(2t).

The open Spec R0 embeds in Spec S0 as t!=0. Its composite to Spec A0 is

    (t,v) -> (t^2,v/(2t)),

and direct differentiation gives da wedge db=dt wedge dv. Thus the
Jacobian is exactly one on this open, and all ramification of the finite
normalization lies on the omitted t=0. Its trace codifferent is

    M0=(1/(2t))*S0.

In particular 1/t belongs to M0 and to R0; its square does not belong to
M0, and Tr((1/t)^2)=2/a is not in A0. This verifies both the valuation
sign and the precise failed inference. It does NOT have whole-plane
source: t is a nonconstant unit in R0, and the omitted divisor is
principal. Hence it cannot refute an actual whole-plane theorem; it
prevents replacing that missing theorem by generic finite-duality,
constant-Jacobian-on-an-open, or regular-source-function arguments.

For the positive control F=id, S=M=R=A, Ram is empty and all products and
quadratic traces are regular, exactly as the argument requires.

## 4. Global boundary-class check and stopping decision

The known class injection uses the whole-plane open essentially: if a
rational function has divisor supported on omitted components, it and its
inverse restrict to units of C[x,y], hence are constant. The usual
localization sequence also makes the omitted prime classes generate Cl(Y),
since Cl(A2)=0. This leaves a free boundary lattice, not a torsion group.
Ram is an effective nonzero combination in that lattice for a hypothetical
nontrivial normalization; K_Y has that same class in the fixed volume.

The principal discriminant downstairs does not create a contradictory
principal divisor supported only on omitted components upstairs. For a
branch equation p in A, div_Y(p) contains not only the omitted ramified
components, but also retained components dominating p=0. The accepted
fixed-sheet argument supplies a retained unramified component: p(f,g) is a
nonconstant polynomial and quasi-finiteness makes each source curve in
its zero set dominate the target divisor. Therefore its class relation
includes retained prime classes. In the boundary basis those retained
classes can cancel the omitted terms. Taking norms merely gives principal
divisors on the factorial target and does not assert injectivity of norm
on the boundary class group. Neither calculation kills Ram.

No extra global relation followed from rationality of affine singularities.
Local dualizing freeness, when present, is weaker than global freeness;
the latter is already forbidden by the accepted full-normalization
attachment. No classification of rational singularities or canonical
algebras was imported to bridge that distinction.

Decision: STOP this bounded duality/multiplication attempt as KNOWN/GAP.
No closing source implication, new cheapest decisive test, pair,
counterexample, global rank change or proof of JC2. Do not commission a
boundary-class, canonical-algebra, trace-square or relaxed-control family
from this report. The missing result would have to add actual whole-plane
compatibility beyond the finite-module and boundary identities above;
this report does not supply it.

## 5. History, read scope, evidence and custody

The main lane read AGENTS.md, README.md, the entire 694-line
COORDINATION.md, the entire 273-line team/swarmHQ/README.md, and all of
FALLACY-v2.md. Relevant APPROACHES sections 5 and 8 were read in selected
ranges, including the trace-splitting, full-normalization, affine
singularity, and adjoint-derivation stop entries; no whole-map reading is
claimed. AUDIT navigation and the BD-GAL, TRACE-CUTOFF/SPLIT and
full-normalization source material were targeted, not a whole-ledger
reread. Some broad filename/regex outputs were clipped and are not
charged as exhaustive history checks.

Source history used:

- xmodel/full-normalization-genus-scope-astra-20260912.md, read completely;
  SHA256 5f9be737ef4a37be884be4655b9d19de9284f1abdd16bdbe5d08454dd40b35d9.
- Its Fable FIRST, xmodel/full-normalization-genus-scope-gate-fable5-20260912.md,
  source attachment/class/dual sections read; SHA256
  8211cdb2acc8fe20f492fbe703938335c62f42e8119aa6bf2f93b0bef482ac5c.
- xmodel/block-descent-d2-galois-obstruction-producer-sol56-20260830.md,
  sections 0--6 targeted (not whole report); SHA256
  766a843a25eaf560840f15afa8971dd39246fc8b15290491d18e7f4a4c6bb7f7.
- box/adjoint-derivation-discriminator-astra-20260912/ROOT-INTAKE.md,
  read completely, and its producer's sections 1--4. This already records
  the canonical lattice inside source polynomials, global attainment at
  valuation 1-e, and derivative loss to 1-2e. ROOT was notified of this
  existing hit before closure of the parallel derivative lens.

Canonical pins: APPROACHES
2e80cbcde1f4aeb9e520ac4609ea509f1930d0a0022625f06b73cec2da17306a;
AUDIT bda4b17b6afb67a8408c2a461dc2fd44cc96d281dea1522c54392a993d92149a;
COORDINATION 4ce5b29af5a70e096a04b942cb978b1df425f9f0648decb720ec1f089ff37ac4;
team/swarmHQ/README.md
50cf45483cddf637e717ddfa2d136be4df074d13d360b851c1fb62a9e73edb0a;
FALLACY-v2 e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.

No new primary source/theorem imported; zero web pages read. Standard
finite-duality and tame-DVR formulas are consumed from the accepted source
attachment, not newly primary-audited. The multiplication and double-dual
scope checks and the fixed punctured control above are manual algebra,
not a computation or certificate. No science/CAS/Python calculation,
paid-model lane, AWS action, submodule inspection, or shared-ledger edit.
Administrative finalizer and hashes only. No different-model FIRST is
claimed, and no promotion or dependent research is requested.

## COLLISIONS

Manual targeted history check: EMPTY for newly raised OPEN identifiers;
none is raised. The mathematical bottleneck collides with the existing
trace-regularity/canonical-lattice gap, which is why the attempt stops.
No whole-corpus collision scan or exhaustive novelty claim.

Research stopped before 15:16:35 UTC on 2026-09-14; full report readback
and unchanged canonical postpins completed before sealing. The original
12-minute research cap was not extended; no successor was launched.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11152`.
- Body SHA-256:
  `ebf01896cfe1bbae45dc4d5fb94bff92317b1ffc0e767c02455d0d209eb4dcb1`.
- Frozen basis: `49d9c0d9bc23f14ffaa5e4b81521498889663591`.
