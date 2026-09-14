# Hostile review: no homogeneous Hamiltonian slice on the exact pseudo-plane

INTERNAL / DIFFERENT-MODEL HOSTILE REVIEW / MANUAL MATHEMATICS ONLY.
Reviewer: Fable 5.1 (claude-fable-5-1), 2026-09-11. Lane inputs frozen at
`/tmp/jc2-lane.LM8wRa/inputs`. First action 07:51:28 UTC: both owned targets
absent, both input hashes matched the charged pins before any body was read.
Reserve 08:05 UTC / HARD 08:08 UTC, never reset. No subprocess, CAS, code,
network, git, or process control was used; every identity below was
recomputed by hand from the two frozen inputs only. Older linked reports were
not opened.

## 0. Inputs and custody

```
9909649753927f2dbb19bf1701b7f9b0442e1fbcf1a934b3f9080c7f81e43a14  pseudoplane-homogeneous-hamiltonian-root-20260911.md
bdba5b1c0c5eddca59d05bbabe83f429bd730f5607e1f13523e4df1751a8abde  pseudoplane-homogeneous-hamiltonian-root-20260911.md.artifact.json
```
Administrative seal check: the first 8872 bytes of the root file end at the
root's own standalone body-end marker line, newline included, and hash to
the body SHA-256 recorded in both the Seal and the artifact JSON (see
input_custody.md). Post-pins are
recorded in Section 9 after the body was written.

## 1. Overall verdict

All six verdicts are CONFIRMED. The candidate theorem, "for every
homogeneous H in R and every G in R, {H,G} is not a nonzero scalar", holds
over every characteristic-zero field with exactly the hypotheses ROOT
states: entries in R (not R[A^-1]), H homogeneous for the integer grading
wt(A,U,Z)=(2,1,-2), characteristic zero. No step of Sections 1-5 is refuted
and no gap in truth was found. Two expository corrections, neither changing
the mathematics: Section 3 should state the Leibniz reason that a
nonzero-scalar bracket forces nonzero differentials at o, and Section 1 may
record that Phi is a Casimir on k[A,U,Z] (the bracket is -2 times the
Jacobian determinant against Phi), which is the actual reason the bracket
descends. Collateral qualifications: the corollary in Section 5 needs only
a target map with nonzero constant Jacobian; the local-finiteness remark in
Section 1 is unproved and unused. Nothing here is a computational replay, a
silent repair, a mixed/mixed result, or a JC2 claim.

## 2. Verdict A: bracket, relation, Jacobi, grading, normal form, weight shift

**CONFIRMED.** Hypotheses: k any field, char 0 used nowhere in A.
Let S=k[A,U,Z], Phi=U^2-A-A^2 Z, and let the biderivation on S be fixed by
{A,U}=2A^2, {A,Z}=4U, {U,Z}=2+4AZ.

Relation preservation, recomputed (stronger than ROOT states: Phi is a
Casimir on S, not merely {Phi,S} in (Phi)):
```
{Phi,A} = 2U{U,A} - A^2{Z,A}          = -4A^2U + 4A^2U          = 0
{Phi,U} = -{A,U} - 2AZ{A,U} - A^2{Z,U} = -2A^2 -4A^3Z +2A^2 +4A^3Z = 0
{Phi,Z} = 2U{U,Z} - {A,Z} - 2AZ{A,Z}   = 4U+8AUZ -4U -8AUZ         = 0
```
So (Phi) is a Poisson ideal and the bracket descends to R. Structurally the
bracket equals -2 det d(a,b,Phi)/d(A,U,Z): the determinant gives
{A,U}=Phi_Z=-A^2, {U,Z}=Phi_A=-1-2AZ, {A,Z}=-Phi_U=-2U, and -2 times these
is ROOT's table. The Casimir property is then the repeated-row determinant.

Jacobi on generators, recomputed: {A,{U,Z}}={A,2+4AZ}=4A{A,Z}=16AU;
{U,{Z,A}}={U,-4U}=0; {Z,{A,U}}={Z,2A^2}=4A{Z,A}=-16AU. Sum 0, matching
ROOT's "16AU+0-16AU". The Jacobiator of an antisymmetric biderivation is a
triderivation, so the generator check suffices on S and Jacobi passes to R.

Grading: wt(U^2)=2, wt(A)=2, wt(A^2 Z)=4-2=2, so Phi is homogeneous of
weight 2 and R is the direct sum of its integer weight spaces; every
element has finitely many weights. Weight shift: {A,U} has weight 4 against
3, {A,Z} weight 1 against 0, {U,Z} weight 0 against -1; each generator
bracket shifts by exactly +1, and for a biderivation the shift on monomials
is wt(a)-wt(x_i)+wt(b)-wt(x_j)+wt({x_i,x_j}) = wt(a)+wt(b)+1. So
{R_v,R_w} is contained in R_{v+w+1}.

Normal form: Phi is monic of degree 2 in U, so R is free over k[A,Z] with
basis 1,U and k[A,Z] embeds. The division by a homogeneous monic
preserves weight, so R_w is spanned by the basis monomials A^i U^e Z^j of
weight 2(i-j)+e. Attack tried: R a domain is not needed by ROOT, but it
holds (A(1+AZ) is not a square in k[A,Z]) and the surface is smooth
(Phi_A=-1-2AZ, Phi_U=2U, Phi_Z=-A^2 have no common zero). No correction.

## 3. Verdict B: homogeneous mate selection and fixed-point weights

**CONFIRMED.** Hypotheses: H homogeneous of weight w (H=0 excluded since
{0,G}=0), G arbitrary in R, {H,G}=c in k with c nonzero.

Mate selection: G=sum_v G_v is a finite sum. {H,G_v} lies in R_{w+v+1} by A,
and c lies in R_0 (R_0=k[AZ] contains k). Direct-sum comparison of the
weight-0 component gives {H,G_{-w-1}}=c exactly; the other components land
in other weight spaces and cannot cancel against c. This uses that H has a
single weight; for mixed H the products {H_u,G_v} of several (u,v) share a
weight and the reduction fails, exactly as ROOT says.

Fixed point: Phi(0,0,0)=0. In S, Phi = -A + (U^2 - A^2 Z) with the bracketed
part in m_S^2, so m_R/m_R^2 = (A,U,Z)/(A, m_S^2) = kU + kZ, graded with
weights 1 and -2; o is a smooth point. The step ROOT asserts without proof,
"a scalar nonzero bracket forces both differentials nonzero at o", is true
by Leibniz: if H-H(o) = sum a_i b_i with a_i,b_i in m_o then
{H,G} = sum({a_i,G}b_i + a_i{b_i,G}) lies in m_o, so {H,G}(o)=0, not c.
More precisely {H,G}(o) = 2(alpha beta' - alpha' beta) where dH_o = alpha dU
+ beta dZ and dG_o = alpha' dU + beta' dZ, using {U,Z}(o)=2; so the two
differentials must even be independent.

Weights, all cases: a normal-form monomial A^i U^e Z^j is a single variable
only for A (weight 2, and A = U^2 - A^2 Z lies in m_R^2), U (weight 1), Z
(weight -2); every other monomial has S-degree at least 2. Hence for
homogeneous H the class in m_R/m_R^2 is zero unless w=1 or w=-2.
Constants: w=0 gives H in k[t], t=AZ in m_R^2, so H-H(o) in m_R^2 and
dH_o=0; a pure constant has {H,G}=0 outright. Negative weights other than
-2: R_{-1}=UZ k[t], R_{-3}=UZ^2 k[t], R_{-4}=Z^2 k[t], all inside m_R^2.
Positive weights other than 1: R_2 = A k[t] inside m_R^2, and so on.
Applying this to H (weight w) and the homogeneous mate (weight -w-1) forces
{w,-w-1}={1,-2}; antisymmetry swaps the pair at the cost of the sign of c.
Cross-check of the excluded weight 0 by the polynomial identity: for
H=h(t), G=UZ g(t) one gets {H,G} = 2h'(t) t(1+t) g(t), which vanishes at
t=0 and so is never a nonzero scalar. Smallest correction: add the one-line
Leibniz argument above to Section 3; no mathematical change.

## 4. Verdict C: weight spaces, bracket formula, leading coefficient

**CONFIRMED.** Hypotheses: k of characteristic zero; f,g in k[t] nonzero.

Weight spaces: weight 1 forces e=1 and i=j, giving U(AZ)^i; weight -2
forces e=0 and j=i+1, giving Z(AZ)^i. Since the normal-form basis is
weight-homogeneous these span exactly: R_1 = U k[t], R_{-2} = Z k[t].
k[t] embeds: k[A,Z] embeds by the normal form and AZ is transcendental over
k in k[A,Z]. So U f(t) = 0 forces f = 0 and likewise for Z g(t).

Auxiliary identities, recomputed:
```
{U,t} = {U,A}Z + A{U,Z} = -2A^2Z + 2A + 4A^2Z = 2A(1+AZ) = 2U^2
{t,Z} = {A,Z}Z = 4UZ
U^2 Z = (A + A^2 Z)Z = t + t^2 = t(1+t)
```
Bracket, by the biderivation Leibniz rule with {f(t),g(t)} = f'g'{t,t} = 0
and {U,g(t)} = g'(t){U,t}, {f(t),Z} = f'(t){t,Z}:
```
{Uf, Zg} = (2+4t)fg + Zf g'(2U^2) + Ug f'(4UZ)
         = (2+4t)fg + 2 t(1+t) f g' + 4 t(1+t) f' g
         = 2[(1+2t) fg + 2t(1+t) f'g + t(1+t) fg'].
```
This is ROOT's display, term for term, and it lies in k[t]=R_0 as the
weight count 1-2+1=0 predicts. Coefficient of t^{n+m+1}: 2 lc(f)lc(g) from
(1+2t)fg, 2n lc(f)lc(g) from 2t(1+t)f'g, m lc(f)lc(g) from t(1+t)fg';
total 2(2+2n+m) lc(f)lc(g), as displayed. When n=0 or m=0 the derivative
term is zero and the formula still holds with n=0 or m=0. In characteristic
zero 2+2n+m is at least 2, so the bracket has exact t-degree n+m+1, at least
1, and p(t)-c is a nonzero element of k[t], hence of R. Spot check f=g=1:
{U,Z}=2+4t, coefficient 4 = 2(2+0+0). The prime is explicitly defined as
d/dt in ROOT, so the FALLACY prime-label item does not fire. Attack tried:
f or g zero gives bracket 0, excluded by ROOT's sentence. No correction.

## 5. Verdict D: pullback relation, brackets, two-point collision

**CONFIRMED** as a sufficient counterexample interface only. Map
A=x^2, U=x+x^3y, Z=2y+x^2y^2. Relation: U^2 = x^2(1+x^2y)^2 and
A+A^2Z = x^2 + 2x^4y + x^6y^2 = x^2(1+x^2y)^2, equal. Ordinary Jacobians
J(a,b)=a_x b_y - a_y b_x with A_x=2x, A_y=0, U_x=1+3x^2y, U_y=x^3,
Z_x=2xy^2, Z_y=2+2x^2y:
```
J(A,U) = 2x*x^3 = 2x^4 = 2A^2
J(A,Z) = 2x(2+2x^2y) = 4(x+x^3y) = 4U
J(U,Z) = (1+3x^2y)(2+2x^2y) - 2x^4y^2 = 2 + 8x^2y + 4x^4y^2 = 2+4AZ
```
since 4AZ = 4x^2(2y+x^2y^2) = 8x^2y+4x^4y^2. So R -> k[x,y] is a Poisson
homomorphism to the Jacobian bracket, and {F,G}=c in R pulls back to a
Keller pair. Collision: (1,0) maps to (1,1,0); (-1,-2) maps to
(1, -1+2, -4+4) = (1,1,0). Both are Q-points, so the collision exists over
every characteristic-zero k. Any Keller pair factoring through the plane
map identifies these two points and is not injective, hence not an
automorphism. Status: sufficient only. Nothing says a Keller counterexample
must factor through R, and no F,G is supplied; the theorem removes only
endpoints with a homogeneous coordinate. Attack tried: the dominance of the
plane map (J(A,U) nonzero) makes R embed in k[x,y], which is unused.
No correction.

## 6. Verdict E: target-automorphism corollary and localization countercontrol

**CONFIRMED**, with the collateral hypothesis made explicit. Corollary:
let (F,G) be a constant-bracket pair in R and sigma=(p,q) a polynomial
automorphism of the target plane. In characteristic zero det J(sigma) is a
unit of k[X,Y], hence a nonzero constant j. The biderivation chain rule
{p(F,G),q(F,G)} = (p_X q_Y - p_Y q_X)(F,G) {F,G} = jc gives another
constant-bracket pair in R, so by the theorem neither p(F,G) nor q(F,G) is
homogeneous. The hypothesis actually used is only that sigma has nonzero
constant Jacobian; automorphism is more than needed. ROOT does not claim a
normalizing sigma exists, and none is implied.

Localization countercontrol, recomputed in R[A^-1]:
{A, U/(2A^2)} = (1/2)({A,U}A^-2 + U{A,A^-2}) = (1/2)(2A^2 A^-2 + 0) = 1.
Weights 2 and 1-4=-3, sum -1 as the +1 shift requires for a weight-0 value.
Pole order: P=(A,U) is prime with R/P=k[Z], so Z is the residue coordinate;
R is smooth so R_P is a DVR; 1+AZ maps to 1 in k[Z] and is a unit in R_P;
A = U^2(1+AZ)^-1 gives ord_P(A) = 2 ord_P(U), and P R_P=(U), so ord U=1,
ord A=2, ord U/(2A^2) = 1-4 = -3. Pole order 3 as stated. The pair is
therefore not in R and the theorem's "H in R and G in R" is load-bearing:
the failing step in R[A^-1] is Section 3 (o is not a point of
Spec R[A^-1]) together with the weight-space description. Regularity at
A=0 must remain in every restatement; the candidate theorem keeps it.
The control f=g=1, {U,Z}=2+4t, correctly shows fixed-point evaluation
alone (value 2) is not the argument; the polynomial identity is.

## 7. Verdict F: scope firewall

**CONFIRMED.** The proof of the exact theorem uses only: the displayed
ring and bracket (A), the direct grading and normal form (A), the finite
weight decomposition of the mate (B), the fixed point o with its two
cotangent weights (B), the two weight spaces and the polynomial identity
with its leading coefficient in characteristic zero (C). No locally-finite
Hamiltonian theorem, no ruling-aligned obstruction, no wild/mixed safeguard
and none of the four listed old reports enter any step; I did not open them
and did not need them. ROOT makes no mixed/mixed claim, no claim that a
target normalization exists, no all-source or JC2 claim, and Section 1
states the pullback is an endpoint, not a source coverage. The collateral
remark that the U and Z Hamiltonians need not be locally finite is outside
the theorem; it is plausible (ad U sends A to -2A^2, then to powers of A
of increasing degree) but is not proved in ROOT and is not consumed.

## 8. Negative control, QUANTITY, CHEAPEST TEST, planning wall

**Negative control (own, meaningful).** Drop characteristic zero. With
f=1, g=t-1 the displayed formula gives 2[(1+2t)(t-1) + t(1+t)] = 6t^2 - 2.
Direct recomputation in R: {U, AZ^2 - Z} = -2A^2Z^2 + 2AZ(2+4AZ) - (2+4AZ)
= 6A^2Z^2 - 2. In characteristic 3 this is 1, so U has the regular
homogeneous slice Z(AZ-1) of weight -2 and the candidate theorem is FALSE
there. Every step other than the leading coefficient 2(2+2n+m) is
characteristic-free (char 2 aside, where the bracket vanishes), so the
control shows the char-0 hypothesis is consumed exactly where ROOT consumes
it and nowhere else. The control is a hypothesis mutation, not a changed
object, and it fired.

**Remaining QUANTITY.** Whether a mixed/mixed pair F,G in R (both
coordinates inhomogeneous, and their images under every target Keller map)
can have {F,G} in k*. The theorem is silent there. The next bounded
research possibility is a question: do the top-weight and bottom-weight
components of a hypothetical mixed slice, which must Poisson-commute
whenever their weight sum is not -1, force an algebraic dependence that the
fixed point o then excludes? This is a question, not an authorization for
a second lane, a source search, or any computation.

**CHEAPEST TEST.** A static desk derivation of the top/bottom-weight
commutation constraints on a mixed pair, on this exact R, reading nothing
new. Planning wall: approximately 20 minutes UNMEASURED manual time, no
subprocess, hard cap fixed before any launch. Not run here.

## 9. Post-pins, readback, COLLISIONS

Post-pins measured 07:58:23 UTC, after sections 1-8 were written and
before this section:
```
9909649753927f2dbb19bf1701b7f9b0442e1fbcf1a934b3f9080c7f81e43a14  pseudoplane-homogeneous-hamiltonian-root-20260911.md
bdba5b1c0c5eddca59d05bbabe83f429bd730f5607e1f13523e4df1751a8abde  pseudoplane-homogeneous-hamiltonian-root-20260911.md.artifact.json
```
Identical to the pre-pins of 07:51:28 UTC; the input directory is
unchanged. Custody detail, the administrative seal cross-check and the
whole-read record are in
`box/pseudoplane-homogeneous-gate-fable5-20260911/input_custody.md`.

Own whole readback: both owned files were read back whole by cat after
this section was written and before the marker was appended; the marker
was appended only after that readback showed no placeholder and no stray
marker. Timing: skeleton 07:55:55 UTC, verdicts A-C 07:56:39, verdicts
D-F and section 8 07:57:49, custody 07:58:23, all inside the 08:05 reserve.
No process control was exercised by this lane; TERM/KILL arming belongs
to the adapter.

COLLISIONS (own-only): none. Both owned targets were absent at
07:51:28 UTC; nothing outside the two owned paths was created or
modified. No Seal, charge_basis, or artifact transaction was authored.
No exit-price assertion is made, so no charge_basis line is declared.
No new canonical OPEN id is needed.

Final write: this marker append at 07:59:32 UTC, inside the
08:05 reserve. ALL WRITERS IDLE after this line; the adapter seals.

<!-- BODY-END -->
