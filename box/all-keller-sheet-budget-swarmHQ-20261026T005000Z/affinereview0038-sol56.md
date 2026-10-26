# AFFINEREVIEW0038 — hostile review of all-Keller sheet-budget applicability

Status: PASS / INTERNAL / MANUAL / INDEPENDENT REVIEW.
Launch/report basis: e3939ae2ee8675e44db2f11ee932f570b383e4b8.
Selection basis: e30c44c3fd85e9bc8d2f6217fc1cc366f28e50de.
Public basis: 47cbe1093ea6ee7b4ec6d32a7eda4a79e567c061.

## Verdict and exact scope

AFFINETREE0015 proves the claimed extension for every complex polynomial Keller map.
For the finite normalization h:X->A2 of degree e, with whole source U=A2 open in X,
the omitted curves E_i are disjoint and have finite bijective normalizations A1->E_i.
If r_i, delta_i, m_x and t_x have the report's meanings, then

    e-1-sum_i r_i delta_i
      = sum_i sum_(x in E_i)(m_x-r_i t_x) >= 0.                    (SB-all)

No smoothness of E_i or rational singularities of X are needed. This is an applicability
extension of the published numerical bound, not a classification, logarithmic-thickening
result, dynamical reduction, counterexample, or proof of JC2.

## Affine enlargement and purity

Let X be normal affine with dense U=A2. If a missing point p were isolated away from the
union E of missing curves, choose f vanishing on E but not at p. The normal affine open
V=D_X(f) differs from V∩U by finitely many points. Hartogs gives equal coordinate rings;
the affine open immersion V∩U->V is therefore an isomorphism, contradiction. Thus X\U
is pure one-dimensional. This argument does not use rational singularities.

For a Keller pair, A=C[P,Q]⊂R=C[x,y], and the integral closure B of A in Frac(R) is
finite over A. Since its elements are also integral over R and R is integrally closed,
B⊂R. The induced Spec(R)->Spec(B) is birational and quasi-finite because its fibres lie
in the quasi-finite Keller fibres. Zariski Main over normal Spec(B) makes it an open
immersion. Hence every Keller pair supplies precisely the required whole-source normal
affine enlargement and finite h; no integrality of A⊂R or properness of F is assumed.

## Boundary tree and omitted-curve normalization

Normalize a projective closure of X. The pulled-back hyperplane at infinity is ample
Cartier with support equal to the projective boundary. Resolve the birational map from
P2 by point blowups away from U. On the smooth Z the full boundary D is an SNC tree of
P1s. The support C_inf of the nef-big pullback P of infinity is connected: if its support
split as disjoint effective A+B, then A.B=0, A²=P.A>=0 and B²=P.B>=0, while P²>0;
Hodge index contradicts the nonnegative square of the nonzero part orthogonal to the
positive-square part. Neither component is numerically zero because it meets an ample
divisor positively.

Each strict transform L_i of a missing curve is a P1 outside C_inf and must meet C_inf,
else its proper image would be a complete curve in affine X. It attaches exactly once,
or D would contain a cycle. Any component of D\C_inf contains at most one L_i, since two
such L_i each attach to connected C_inf and would again create a cycle.

Proper birational fibres over normal X are connected. A fibre over X\U lies in D\C_inf.
It therefore cannot join two distinct L_i. Nor can it identify two points of one L_i:
a positive-dimensional connected exceptional path between them plus the intervening
path in L_i is a cycle; a zero-dimensional connected fibre is one point. Thus the E_i
are disjoint and L_i\C_inf->E_i is bijective. It is the proper base change of L_i->barX,
quasi-finite, finite and birational. Its normal source is P1 minus its unique attachment,
namely A1, so it is the normalization. Finite bijectivity also makes it an analytic
homeomorphism; cuspidal nonnormal E_i are allowed and have chi_c=1.

## Images, flatness, and local lengths

Finite h cannot contract E_i. The finite map A1->E_i->D_i factors through the normalized
image. Its projective completion is a nonconstant P1 map, so Riemann--Hurwitz makes the
completed target P1. Every target infinity point has a source preimage, but the source
has only its one infinity point; that point cannot map into the affine target. Hence the
normalized affine image is A1 and the induced degree-delta_i map is polynomial, with

    sum_x(t_x-1)=delta_i-1.                                       (1)

Normal X is Cohen--Macaulay. Finite dominance over smooth A2 is therefore finite flat
of rank e. The fibre-length function m_x is constructible, equals one on U, and has
generic value r_i on E_i; only finitely many exceptions occur.

At any x∈E_i, base-change h along a small analytic disc in the chosen normalized image
branch. The finite flat algebra remains locally free. Separating central-fibre points
gives a summand near x of constant rank m_x. A general disc point has t_x normalization
points near the unique preimage of x; finite-bijective normalization puts them all in
this summand, and each has transverse fibre length r_i. Other sheets contribute
nonnegative length. Therefore

    m_x >= r_i t_x.                                                (2)

This conservation-of-length argument remains valid when X is singular at x, E_i is
cuspidal, or D_i has several branches; it selects one normalized branch and makes no
comparison between different branches.

## Whole-source Euler identity

Because X=U disjoint-union_i E_i and chi_c(E_i)=1, chi_c(X)=1+s. Euler integration of
sum_(x over y)m_x=e gives integral_X m=e. Stratifying by the generic r_i yields

    e-1=sum_i r_i + sum_i sum_x(m_x-r_i).                          (3)

The finite-bijective normalizations identify the point sums with those on A1. Subtracting
sum_i r_i(delta_i-1), applying (1) and (2), gives exactly (SB-all). This is one sum over
the whole source, so two omitted curves sharing an image cause neither double use of a
target sheet budget nor a missing correction.

## Limits and custody

PASS for the all-Keller applicability and exact slack identity. The already published
divisorial bound is the nearest prior result; this review makes no novelty claim. It does
not import the message-only BGV classification. The logarithmic thickening inequality,
infinitely-singular branch, and JC2 remain unresolved. No successor is authorized.

ACK: 2026-10-26T00:39:39.386354Z. Whole frozen STATE334 completed
2026-10-26T00:39:53.325659Z and matched launch STATE. Fixed48 prepins passed. Fresh whole
reads: task14, AFFINETREE153, published sheet-budget113; manifest verification and selected
prior custody are recorded separately. Prior own coverage is claimed only where exact
receipts and hashes match. No source/history query, CAS, paid/cloud action, child, protected
tree, shared/public/Git edit, control family, or successor occurred. A substantive partial
was saved at 00:41:02Z. Final postpins, blob comparisons, exact charge and collision custody
are in companion receipts.

OPEN(S) RAISED
None.

## COLLISIONS
Terminal frozen-public collision custody is recorded separately after sealing.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6935`.
- Body SHA-256:
  `142614b63a23e101cdfd9440c77da4e401e2f9513a87a3228b298d4ceaeedb5d`.
- Frozen basis: `e3939ae2ee8675e44db2f11ee932f570b383e4b8`.
