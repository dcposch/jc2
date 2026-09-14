# Hostile FIRST: canonical Liouville field generator and saturation boundary

Fable 5.1, different-model hostile FIRST of two completed manual proofs.
Tag liouville-generator-gate-fable5-20260912. First action 12:23:36 UTC,
September 12, 2026; original reserve 12:40 UTC, HARD 12:43 UTC, never reset.
Mathematics remains PROVISIONAL; no JC2 result is asserted. Independent
MANUAL reconstruction only: no interpreter, CAS, code, network, corpus,
linked body, live peer output or inherited reader.

## Custody (pre-read)

Three snapshots hashed in /tmp/jc2-lane.yDGQSO/inputs before any body,
all equal to the expected values, then each read WHOLE, COORDINATION
first (806 lines in four unclipped chunks 1-200, 201-400, 401-600,
601-806), then Astra (103 lines, one chunk), then ROOT (183 lines, one
chunk):

- COORDINATION.md 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597
- liouville-primitive-element-astra-20260912.md 6a9e43ec24bbf35624e887eb48abe33723a9fa93f6f5ac54135f49679df5b5cc
- liouville-saturation-control-root-20260912.md 4e0e8c4915a47893df9cc9640fbb9878f040609e3e41d63d0d46d27ad18f7462

## A. Full-plane field generator

Theorem under test (Astra). For f,g in C[x,y] with J(f,g)=1 and any
polynomial S with dS = x dy - f dg, the field C(f,g,S) equals C(x,y).

Own derivation. Write L=C(x,y), F=C(f,g), K=F(S). The matrix
[[f_x,f_y],[g_x,g_y]] has determinant 1, so the derivations of L with
D(f)=1,D(g)=0 and D(f)=0,D(g)=1 are

    d_f = g_y d_x - g_x d_y,      d_g = -f_y d_x + f_x d_y,

checked directly: d_f(f)=g_y f_x - g_x f_y = J = 1, d_f(g)=0, d_g(g)=J=1,
d_g(f)=0. The potential equation says S_x = -f g_x and S_y = x - f g_y.
Hence

    S_f = g_y(-f g_x) - g_x(x - f g_y) = -x g_x,
    S_g = -f_y(-f g_x) + f_x(x - f g_y) = x f_x - f J = x f_x - f,

identical to Astra's displayed values. For E = x d_x: E(f)=x f_x=f+S_g,
E(g)=x g_x=-S_f, E(S)=x S_x=-x f g_x=f S_f. All three agree with Astra.

Descent, attacked two ways. (i) L/F is algebraic (both have
transcendence degree 2, f,g independent since df^dg = dx^dy is nonzero)
and separable (characteristic 0), so d/df, d/dg on F extend uniquely to K
and to L; the restriction of d_f to K is such an extension, so by
uniqueness d_f(K) and d_g(K) lie in K. Explicitly, if m is the minimal
polynomial of S over F then d_g(S) = -m^{d_g}(S)/m'(S), with m'(S)
nonzero by separability. (ii) My own second route: d_f,d_g are an
L-basis of Der_C(L), so E = E(f) d_f + E(g) d_g = (f+S_g) d_f - S_f d_g
with coefficients in K; therefore E(K) is inside K without a separate
E(S) computation, and this route reproduces E(S) = (f+S_g)S_f - S_f S_g
= f S_f as a consistency check. Astra's remark that E(S) must not be
omitted is correct within Astra's route and harmless in mine. No group
action on K is used anywhere: only the derivation E and its iterates.

Weight interpolation. If A = sum_{i=0}^N x^i A_i(y) is a polynomial in
K, then E^k A is in K for all k, and P_i(E)A with P_i(E) = prod_{j != i}
(E-j)/(i-j) is a complex-coefficient polynomial in E applied to A, hence
in K. On the j-th term (E-j) is zero and on the i-th term the product is
1, so P_i(E)A = x^i A_i(y). Denominators i-j are nonzero integers. Thus
f_0, x f_1, g_0, x g_1 are in K with no group-action premise. CONFIRMED.

Own controls. Pair f=x, g=y+x^2: J=1, S=-2x^3/3; S_f=-x g_x=-2x^2 equals
d_f(S) with d_f = d_x - 2x d_y; S_g = x-x = 0 equals d_y(S); E(S)=-2x^3
= f S_f. Pair f=y, g=-x: S=xy, S_f = x = d_y(xy), S_g = -y = -d_x(xy),
E(f)=0=f+S_g, E(g)=-x=-S_f, E(S)=xy=f S_f. Both pass every identity.

## B. Global axis and polynomial Luroth

Axis equation. J(f,g)=1 is a polynomial identity, so it may be restricted
to x=0, where f_x|_{x=0}=f_1(y), f_y|_{x=0}=f_0'(y), and likewise for g.
This gives f_1 g_0' - f_0' g_1 = 1. So f_0,g_0 are not both constant and
f_1,g_1 are not both zero. CONFIRMED.

Polynomial generator. M=C(f_0,g_0) is a nonconstant subfield of C(y), so
C(y)/M is finite, and the inclusion is a finite separable morphism pi
from P^1_y onto the smooth projective model X of M. Riemann-Hurwitz,
-2 = deg(pi)(2g(X)-2) + deg R with deg R >= 0, forces g(X)=0, so X is
P^1. Let u be a nonconstant member of {f_0,g_0}. On P^1_y its only pole
is infinity. If q is a pole of u on X, every point of pi^{-1}(q) is a
pole of pi^*u = u because pullback multiplies orders by positive
ramification indices, and pi^{-1}(q) is nonempty by surjectivity; so
pi^{-1}(q) = {infinity}. Two distinct poles cannot share this preimage,
so u has exactly one pole q = pi(infinity), and this q is the same point
for f_0 and for g_0. A coordinate h on X with unique simple pole at q
pulls back to a rational function with poles only in pi^{-1}(q) =
{infinity}, hence h(y) is in C[y], nonconstant, and M = C(h). Each of
f_0,g_0 is regular on X minus q = Spec C[h], so f_0=F_0(h), g_0=G_0(h)
with F_0,G_0 in C[T]. The chain rule turns the axis equation into
1 = h'(y)(f_1 G_0'(h) - F_0'(h) g_1), a product of two polynomials in
C[y] equal to 1, so h' is a unit. In characteristic 0 this forces deg h
= 1, so y is in M, which is inside K. CONFIRMED.

Constant cases. Both constant contradicts the axis equation. If f_0 is
constant, f_1 g_0' = 1 makes g_0 linear and f_1 a nonzero constant; if
g_0 is constant, -f_0' g_1 = 1 does the symmetric job. My control f=y,
g=-x is exactly the g_0-constant case: f_0=y, g_1=-1. CONFIRMED; the
general argument already covers these once one of f_0,g_0 is nonconstant.

Recovery of x is field division only. Some a(y) in {f_1,g_1} is a
nonzero polynomial; y in K gives a(y) in K, the weight projection gives
x a(y) in K, and x = (x a(y))/a(y) in the FIELD K. Where a(y) vanishes
the quotient is not defined at the ring level, so no statement
C[f,g,S] = C[x,y] follows; Astra says exactly this. CONFIRMED.

Controls. Identity pair f=x,g=y: dS=0, S constant, K=F=L; the theorem is
trivially true and needs no nonconstant S. Rational punctured degree-2
control on x != 0: f=x^2, g=y/(2x), S=xy/2=fg. I recomputed
J = 2x/(2x) = 1, f dg = (x/2)dy - (y/2)dx, x dy - f dg = d(xy/2). Here
K=F, L=F(x), x^2 = f, y=2gx, and (x,y) -> (-x,-y) fixes f,g,S but not x,
so [L:F]=2 exactly and K is a proper subfield. This is a control on the
global-polynomial hypothesis and is a different object from ROOT's
degree-3 cover p=x^3; the two must not be conflated. The ring control
C[x,xy] (fraction field C(x,y), y absent, J=x) only limits the
field-to-ring inference. CONFIRMED as controls.

## C. Canonical-potential saturation control

Control under test (ROOT). R=C[x,x^-1,y], A=C[p,p^-1,q], p=x^3,
q=y/(3x^2)+(4/9)x+2/(3x), S=(2/3)xy-x^4/9+x^2/3. Target localization
p != 0 is carried in A throughout; nothing below evaluates at p=0.

Jacobian and potential, recomputed. p_x=3x^2, p_y=0, q_y=1/(3x^2), so
J(p,q)=p_x q_y - p_y q_x = 1 identically on x != 0. q_x =
-2y/(3x^3)+4/9-2/(3x^2), so p dq = [-2y/3+(4/9)x^3-(2/3)x]dx + (x/3)dy
and x dy - p dq = (2x/3)dy + [2y/3-(4/9)x^3+(2/3)x]dx. Since S_y=(2/3)x
and S_x=(2/3)y-(4/9)x^3+(2/3)x, this is exactly dS. CONFIRMED. S is a
polynomial on all of A^2; q is not, because 3x^2 q = y+(4/3)x^3+2x
restricts to y at x=0.

Actual ring maps. The C-algebra map A -> R sends p to the unit x^3, so it
is well defined on p^-1. It is injective because p,q have nonzero
Jacobian, hence are algebraically independent, and inverting p keeps
injectivity. Solving the q formula gives y = 3x^2 q - (4/3)x^3 - 2x and
x^-1 = x^2/p, so A[X]/(X^3-p) -> R, X -> x, is surjective. It is
injective: the source is A-free of rank 3, X^3-p is irreducible over
C(p,q) since ord_p(p)=1 is not a multiple of 3 and a cubic without a root
is irreducible, so C(p,q)[X]/(X^3-p) is a field mapping nontrivially to
C(x,y), and the free module embeds in that tensor. Thus R = A[X]/(X^3-p),
finite free rank 3, etale because 3X^2 is a unit in R. Generic degree
exactly 3. CONFIRMED.

Primitivity. 2pq = (2/3)xy+(8/9)x^4+(4/3)x^2, so T = 2pq-S = x^4+x^2 =
px+x^2. Then x(T+p^2) = x^5+x^3+x^7 = x^3(x^4+x^2+1) = p(T+1); ROOT's
derivation via x^2=T-px gives the same. T+p^2 is 3 at x=1, hence nonzero,
so x = p(T+1)/(T+p^2) lies in C(p,q,T)=C(p,q,S) and y follows from the
ring map. C(p,q,S)=C(x,y) with no use of A. CONFIRMED.

Graph relation. (x^4+x^2)^3 = x^12+3x^10+3x^8+x^6 and 3p^2T+p^4+p^2 =
3x^10+3x^8+x^12+x^6, so W = T^3-3p^2T-p^4-p^2 vanishes at T. W is monic
of T-degree 3 over A and [C(x,y):C(p,q)]=3 with T a generator, so W is
the minimal polynomial; division by the monic W shows the kernel of
A[T] -> R is exactly (W). So B = A[T]/(W) is the image ring, R = B[x]
is finite over B, B -> R injective gives surjectivity of Spec R -> Spec B
by lying over, and j is finite birational. R is regular, so R is the
normalization of B. CONFIRMED.

## D. Actual divisor and positive control

Fibre over (p,q)=(1,q_0). x^3=1 gives x in {1,omega,omega^2}; with x^3=1,
T=x^4+x^2=x+x^2, which is 2 at x=1 and omega+omega^2=-1 at the other two.
S=2q_0-T gives 2q_0-2 and 2q_0+1 twice. CONFIRMED.

Singular locus of W. W_T=3(T^2-p^2), W_p=-6pT-4p^3-2p, W_q=0. At (1,-1):
W=-1+3-1-1=0, W_T=0, W_p=6-4-2=0, singular. At (1,2): W=8-6-1-1=0 and
W_T=9, smooth; this is the honest third sheet. Full support: W_T=0
forces T=p or T=-p; substitution gives W=-p^2(p+1)^2 and W=-p^2(p-1)^2,
and p is a unit, so the only candidates are (p,T)=(-1,-1) and (1,-1),
where W_p is -6(-1)(-1)+4+2=0 and 0 respectively. Sing Z is exactly
those two lines times the free q-line. CONFIRMED. Own check of the
second line: p=-1 has x in {-1,-omega,-omega^2} with T=-x+x^2 equal to
2,-1,-1, the same collision pattern with smooth sheet x=-1, and W_T=9
at (-1,2). Inverse singular support is the four lines x in
{omega,omega^2,-omega,-omega^2}. CONFIRMED.

Individual divisor and entire saturation. D={x=omega} is a global
irreducible divisor of X. On D, q = y/(3omega^2)+const is affine-linear
in y with nonzero slope, so F(D) is the whole closed line {p=1}; set
image equals closure. F^{-1}({p=1}) = {x^3=1} = {x=1} u {x=omega} u
{x=omega^2}, strictly larger than D. So the saturation predicate
F^{-1}(F(D)) = D fails for an individual component of j^{-1}(Sing Z),
with constant J, exact canonical potential, primitivity and even
finiteness all present. CONFIRMED.

Transversality. On the normalization parametrized by x, dT/dp =
(4x^3+2x)/(3x^2) = (4x+2/x)/3, and each branch is smooth since dp/dx
is nonzero. At omega and omega^2 the slopes are (4omega+2omega^2)/3 and
(4omega^2+2omega)/3, differing by (2/3)(omega-omega^2) != 0. Ordinary
node, not a repeated factor. CONFIRMED.

Positive control. Dropping 2/(3x) from q and x^2/3 from S removes
matched contributions (4/3)x^2 and -x^2/3 from T, leaving T_0=x^4; I
recomputed p dq_0 = [-2y/3+(4/9)x^3]dx+(x/3)dy and dS_0 = x dy - p dq_0
with S_0=(2/3)xy-x^4/9, and J(p,q_0)=1. In A_0[T_0]/(T_0^3-p^4) the
element T_0 is a unit (p^4 is), x=T_0/p, x^-1=p/T_0 and y=3x^2q_0-(4/3)p
are all in the graph ring, and T_0^3-p^4 is irreducible over C(p,q_0)
since ord_p(p^4)=4 is not a multiple of 3, so the graph ring is R_0 and
j_0 is a closed embedding onto the smooth surface T_0^3=p^4 (3T_0^2 is a
unit on it). The cover x -> x^3 still has degree 3. CONFIRMED.

Boundary. Neither q nor q_0 extends polynomially over x=0 (the y/(3x^2)
term survives), so neither open-plane map is a Keller pair on A^2 and
neither is a JC2 counterexample. "Punctured plane" in ROOT literally
means the complement of the line x=0, not of a point; the rings are
explicit so this wording carries no error.

## E. Composition and scope

What survives from both sources, each read on its own scope:

- Full plane (Astra): for every polynomial Keller pair the canonical
  potential S is a primitive element, C(f,g,S)=C(x,y). This is a field
  statement about the generic fibre of (f,g,S). It gives a distinguished
  birational graph Z = closure of the image of (f,g,S) in A^3, with j:
  A^2 -> Z birational. It does not give j finite, Z normal, C[f,g,S] =
  C[x,y], or any saturation of individual inverse-singular divisors;
  finiteness of the Keller map (f,g) itself would already be the
  finite-etale-over-A^2 case, which is the conclusion, not a hypothesis.
- Open plane (ROOT): constant J, exact canonical potential, primitivity
  and finiteness together do not force F^{-1}(F(D)) = D for an
  individual component D of j^{-1}(Sing Z). The positive control shows
  the failure is not automatic for every special potential on the open
  plane. Only this explicit saturation predicate, as stated in the two
  reports, is tested; no external BGV proof text was charged or read,
  and no BGV theorem is contradicted, because ROOT's map is not a
  polynomial map of A^2.

Composition. The two results are consistent and independent: ROOT's
primitivity is proved by the explicit x = p(T+1)/(T+p^2), not by A, and
A's hypotheses (polynomial q on all of A^2) fail for ROOT's map. The
composed conclusion is negative in a useful way: the canonical potential
by itself gives only a distinguished birational graph, and any
saturation or normality claim for the full-plane graph must use the
full-plane polynomial hypothesis in an essential way. My own scope
observation: ROOT's source is C* x A^1, whose fundamental group is Z, so
degree-3 finite etale self-covers exist there and the collision is
topologically permitted; A^2 is simply connected, so the same package on
the full plane would make a finite j an isomorphism. The open-plane
control therefore drops exactly the property that a full-plane argument
must exploit, which is why it cannot be read as a counterexample to any
full-plane implication.

Not established by either report and not claimed here: ring equality,
finiteness or injectivity of a Keller map, normality of Z, any degree
exclusion, any literature novelty, or any JC2 result. Ordinary action
exactness and generic auxiliary primitives were previously known; the
new content is that the canonical S itself is primitive on the full
plane and that this alone is insufficient for saturation.

## Verdict table and closeout

| Part | Verdict | Basis |
|---|---|---|
| A | CONFIRMED | S_f, S_g, E(f), E(g), E(S) rederived; descent by uniqueness and by the basis expansion E=(f+S_g)d_f-S_f d_g; interpolation is a polynomial in E, no group action |
| B | CONFIRMED | axis equation, genus 0 by Riemann-Hurwitz, single pole and single preimage, h' unit, both constant cases, x by field division; degree-2 and identity controls recomputed |
| C | CONFIRMED | J=1, dS=x dy-p dq exact, R=A[X]/(X^3-p) finite etale rank 3 with injectivity argued, x(T+p^2)=p(T+1), W the exact kernel, p != 0 tracked |
| D | CONFIRMED | two singular lines (1,-1),(-1,-1) x q-line verified, node with slope gap (2/3)(omega-omega^2), D={x=omega} with F^{-1}(F(D)) = three lines, positive control T_0^3=p^4 smooth and embedded, degree still 3 |
| E | CONFIRMED as scoped | canonical potential gives a distinguished birational graph only; full-plane saturation is untested by both reports and remains open; no counterexample label, no BGV refutation |

No REFUTED item. GAP items: none inside the charged scope; the open
full-plane saturation question is outside both reports' claims and is
recorded as their stated boundary, not as a defect. Own meaningful
checks: the derivation-basis proof of descent, two full-plane pairs run
through every identity, the p=-1 fibre and its smooth sheet, the
irreducibility of T_0^3-p^4, and the fundamental-group scope remark.

No charge_basis is declared (no exit price asserted). No canonical OPEN
is raised. No artifact_finalize for this external lane. All writes to
this single file were apply_patch; no other file was created or edited.
Read-only commands used: date, ls, wc, sha256sum, sed, cat, grep.
Post-body custody (postpins of all three inputs and own WHOLE readback)
is recorded in the closing block before the marker.

## Closing custody

Own WHOLE readback of this file performed at 12:30:00 UTC (273 lines,
15801 bytes before this block): every section A-E and the verdict table
present, no placeholder left, no marker present before this seal, no
charge_basis line, no OPEN[...] raised, exactly one file at the
destination xmodel/liouville-generator-gate-fable5-20260912.md.
Scope/control check: five separate verdicts, exact theorem and control
statements restated in each part, at least one own meaningful check in
each of A-E, degree-2 (Astra) and degree-3 (ROOT) controls kept distinct,
no counterexample or JC2 label attached to either open-plane map.

Postpins of the three inputs after the body, unchanged from the pre-read
values and from the expected values:

- COORDINATION.md 33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597
- liouville-primitive-element-astra-20260912.md 6a9e43ec24bbf35624e887eb48abe33723a9fa93f6f5ac54135f49679df5b5cc
- liouville-saturation-control-root-20260912.md 4e0e8c4915a47893df9cc9640fbb9878f040609e3e41d63d0d46d27ad18f7462

Sealed before the 12:40 UTC original reserve; no edits after this seal.

<!-- BODY-END -->
