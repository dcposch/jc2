# Field traces of a plane Keller map: the minimal boundary module

ROOT/Astra manual mathematics, PRODUCER-CHECKED candidate, NOT PROMOTED.
First publication action2026-09-11 20:05:09UTC; original publication
reserve20:24UTC, HARD20:27UTC. No scientific computation or AWS allocation.
This is a necessary-condition theorem for arbitrary actual complex Keller
maps, not a proof or counterexample to JC2. No novelty claim is made.

## 1. Exact statement

Let F=(P,Q):A2_C->A2_C have Jacobian c in C*. Put A=C[p,q]=C[P,Q],
R=C[x,y], K=Frac(A), L=Frac(R), N=[L:K], and let D=(d=0) be its actual
reduced nonproperness curve. If D is empty take d=1. Factor d into distinct
irreducibles d_i. Let W=D_A be the polynomial Weyl algebra in p,q. For
each component put H_i=A[1/d_i]/A, and let L_i be its unique simple
intersection-cohomology W-submodule. View H_i inside H=A[1/d]/A and set
L_D=sum_i L_i (a direct sum). Write pi:A[1/d]->H.

The proposed theorem is

    Tr_(L/K)(R) = pi^-1(L_D)
                = A + sum_i W(d_i,p/d_i) + W(d_i,q/d_i).       (T)

Zero generators are ignored. The sums in (T) are ADDITIVE differential
modules, not algebras or fractional ideals. In particular (T) does NOT say
that all traces are polynomial or that they fill A[1/d]. It has no degree,
support, one-dicritical, geometric-degree, nodal-only or boundary-defect
hypothesis. The theorem uses the standard characteristic-zero curve-module
result specified below. All deductions and the reducible extension are
given here. Different-model hostile review is required before promotion.

## 2. Charged standard input and scope

The specialized curve-module input is Yekutieli, *Residues
and Differential Operators on Schemes*, arXiv:alg-geom/9602011v2, Section7,
printed pp27--33. For an integral curve in a smooth surface, Corollary7.7
gives the simple submodule L_i and its quotient:

    0 -> L_i -> H_i -> direct_sum_z delta_z^(r_i,z-1) -> 0.    (Y)

Here r_i,z counts normalization branches, and delta_z=H^2_z(A). Theorem7.10
places the fundamental class dd_i/d_i in L_i tensor Omega^1, so its nonzero
coefficients generate L_i. The paper's setting is INTEGRAL; Section5 below
proves the needed reducible statement using Mayer--Vietoris. We do not
ascribe that extension verbatim to the paper. Point-module simplicity and
classification are also used explicitly in the source's proof of7.5.

Primary PDF https://arxiv.org/pdf/alg-geom/9602011v2, retained at
box/keller-trace-image-root-20260911/yekutieli-9602011v2.pdf,
SHA25621fb0150c5c16fbb2d02e9eae0f69aefb5e3d3e3e998d4ea21878107b025470b.
ROOT read all of Section7, including the proofs, from these pinned bytes.
The numerical residue in Example7.13 is NOT a premise or imported constant.
Other background: finite normalization over a complex affine algebra,
normality, nondegenerate separable field trace, and elementary Weyl-module
and local-cohomology facts proved or described below. No theorem asserting
holonomicity implies simplicity is used, and no D-module direct-image
theorem for the Keller map is needed.

The standard fact that the actual nonproperness locus is empty or a curve,
finite etale complement understood, is the introductory nonproperness
interface in Chau, arXiv:math/0305088v1, pp1--2 (selected read only).
Primary https://arxiv.org/pdf/math/0305088v1; retained PDF
box/keller-trace-image-root-20260911/chau-0305088v1.pdf,
SHA2568e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f.
Its stronger polynomial parametrization theorem is not needed for (T).

## 3. Trace stability and top-degree exactness

The Jacobian condition gives algebraic independence of P,Q and a finite
separable function-field extension L/K. Its two lifted derivations are

    delta_p=(Q_y partial_x-Q_x partial_y)/c,
    delta_q=(-P_y partial_x+P_x partial_y)/c.

They preserve R, restrict to partial_p,partial_q on A, and commute. Field
trace commutes with these derivations: use its sum over embeddings into an
algebraic closure, and uniqueness of derivation extension across separable
algebraic extensions. Consequently M=Tr(R) is an A-submodule stable under W.
It contains A because Tr(a/N)=a. Off the actual D the source is finite
etale, hence traces there are regular and M lies in A[1/d].

For a W-module E use the unshifted coordinate de Rham complex

    E -> E dp + E dq -> E dp wedge dq.

Its top cohomology is H2(E)=E/(partial_p E+partial_q E). This functor is
RIGHT EXACT: for a surjection E->T, choose representatives of top forms to
obtain H2(E)->H2(T) surjective. No analogous assertion in lower degree is
being made.

H2(R)=0 in the lifted frame. Indeed h dp wedge dq = c h dx wedge dy has a
polynomial one-form primitive by polynomial integration in x. Since the
inverse Jacobian is polynomial, write that primitive alpha dp+beta dq with
alpha,beta in R. Thus h=delta_p(beta)-delta_q(alpha). Applying trace gives

    M=partial_p M+partial_q M,              H2(M)=0.           (1)

This is a top-degree quotient argument, not an unsupported assertion that
surjective trace maps are surjective on every de Rham cohomology group.

## 4. Height-one trace saturation without cancellation assumptions

Let eta be the generic point of a component of the ACTUAL D. Put O=A_eta,
a DVR with fraction field K and uniformizer t, and C the integral closure
of O in L. C is finite torsion-free over O. It is contained in R_eta:
elements integral over O are integral over the normal ring R_eta. Define

    C^vee={z in L: Tr(z C) subset O}.

Nondegenerate trace makes C^vee a finite O-lattice. R_eta is not finite over
O: if it were, finiteness of the finite-type algebra would spread to a
neighborhood of eta, contrary to eta belonging to the nonproperness locus.

Suppose the O-submodule Tr(R_eta) of K had valuations bounded below by -b.
For every r in R_eta and a in C, ar lies in R_eta, so
Tr(t^b r a) lies in O. Therefore t^b R_eta is contained in C^vee. An
O-submodule of this finite lattice is finite, contradicting the preceding
nonfiniteness. Trace valuations are thus unbounded below. Any O-submodule
of K with that property is K itself: a member of valuation -m generates
t^-m O. Hence

    M_eta=Tr(R_eta)=K.                                      (2)

Trace localization equals the localized image by flatness. The argument
does not assume the trace of each power of a pole has a pole, nor does it
confuse trace products with products of traces. No ramification index or
explicit local covering decomposition was required.

## 5. Reducible boundary module and point quotients

First justify the point-module facts needed below. At z=(a,b),

    delta_z = W/(W(p-a)+W(q-b))

is simple. As a vector space it is C[partial_p,partial_q]; p-a,q-b act as
minus the corresponding polynomial derivatives. Its top de Rham quotient
by multiplication by partial_p,partial_q is C. Finite sums of these modules
are semisimple and every nonzero submodule or quotient has nonzero H2.
Finite extensions of point modules split: the free Koszul resolution of
W/(W(p-a)+W(q-b)), using right multiplication by p-a,q-b, computes Ext^1
as degree-one polynomial de Rham cohomology, which vanishes. For different
points a shifted coordinate operator is invertible on one polynomial model,
so the cross-support Koszul complex is contractible. Thus all the finite
extensions appearing in the following induction are semisimple.

For two curves D' and C with no common component and finite intersection Z,
the local-cohomology Mayer--Vietoris sequence is

    0 -> H1_D'(A) direct_sum H1_C(A)
      -> H1_(D' union C)(A) -> H2_Z(A) -> 0.                 (3)

The zero terms follow since individual divisors are principal, and
H1_Z(A)=0 on the regular surface. These are the usual two-function Cech
localization complexes; multiplicity of intersection does not thicken the
support of H2_Z. In particular H2_Z=direct_sum_(z in Z) delta_z, one copy
per intersection point.

Apply (Y) to the irreducible components and induct with (3). The direct sum
L_D embeds in H and

    H/L_D = direct_sum_z delta_z^(r_z-1),                    (4)

where r_z is the total analytic branch count of D at z. At an intersection
of the old union and the new component, the counts add as
(r_old-1)+(r_new-1)+1=r_total-1; other points keep their old counts. The
finite point extensions split by the preceding paragraph. Thus (4) is an
actual reducible extension of the charged integral statement, independent
of genus, affine-line normalization, or the topology of the complement.

## 6. The short global argument

Compose M->H->H/L_D. Its image E is a W-submodule of the finite semisimple
point module (4). If E were nonzero, H2(E) would be nonzero. But M->E is
surjective and (1), with right exactness of H2, forces H2(E)=0. Hence E=0:

    M/A subset L_D.                                        (5)

Conversely, each L_i maps to H/(M/A). If this map were nonzero, simplicity
would make it injective. Localizing at the generic point eta_i is exact;
(2) makes (H/(M/A))_eta_i zero, whereas (L_i)_eta_i is nonzero. This is
impossible. Thus L_i subset M/A for every i. Together with (5) this gives
M/A=L_D, proving the first equality in (T). The fundamental-class
coefficients in Section2 give its second, explicit equality.

This proof needs neither a comparison of total Betti numbers nor the
normalization-A1 theorem, and does not assume regular holonomicity of R.
An independently assigned Astra task is checking a longer global
dimension-comparison route; its live report is not a premise here.

## 7. Node specialization, controls, and exact limits

At an ordinary node use S=widehat(A_z)=C[[u,v]] and d a unit times uv.
After ordinary flat tensor base change, the two smooth-branch modules in
(4) give

    M tensor_A S = S[1/u]+S[1/v],
    (A[1/d]/M) tensor_A S
      = S[1/(uv)]/(S[1/u]+S[1/v]) = H2_(u,v)(S).             (6)

For an explicit verification, S tensor_A W is the continuous formal Weyl
algebra with finite derivative order. The invertible coordinate Jacobian
changes the two derivatives to partial_u,partial_v. If the two local
branches belong to one global component, dd_i/d_i equals
du/u+dv/v plus a regular one-form; if they belong to different components,
the two logarithmic forms separate already. Their coefficients generate
1/u and1/v modulo S. Formal differentiation generates every higher pure
pole and never a mixed pole. This proves (6) directly from the explicit
generators in (T). This is tensor base change, not adic completion of the
non-finite source.
The coefficient u^-1 v^-1 is zero in every element of the sum and one in
1/(uv). Hence traces at an actual ordinary node cannot supply mixed poles.
This conclusion has no zero-defect or two-transposition assumption.

Controls, all manual:

- For d=uv in a polynomial plane, M0=A[1/u]+A[1/v] has H2=0: integrate
  each summand in the variable not inverted. It is full at height one but
  not an algebra: 1/u,1/v belong, their product does not.
- The genuine etale open immersion (C*)2->A2 has trace image A[1/(uv)]
  and H2=C, generated by du/u wedge dv/v. It is not an A2 source, so fails
  exactly the top-exactness input. Full localization is therefore not
  forbidden for arbitrary etale affine surfaces.
- The genuine open immersion A1 x Gm->A2 has M=A[1/u], H2=0 and d=u.
  It satisfies (T), but is not a Keller selfmap of A2. Thus the trace
  condition alone cannot characterize the desired source or properness.
- The non-etale polynomial map (x,y)->(p=x,q=xy) has field trace the
  identity and R=C[p,q/p]. Its image is not stable under partial_q since
  partial_q(q/p)=1/p is absent. The Jacobian condition is indispensable.
- Identity F has actual d=1 and M=A. An artificial divisor for the
  identity is not its nonproperness locus and invalidates (2).

The mixed-pole obstruction is compatible with separately escaping local
sheets. It does not bound N, exclude nodes, compute any campaign defect,
or prove that a specified local model globalizes. The elementary ring
control needs no unreviewed node-cover report as an input. When all local
singularities are unibranch, (4) has no point part and (T) gives full
localization; that alone supplies no contradiction.

## 8. History comparison and next decisive test

Targeted history searches located no exact field-trace-image statement in
the current avenue/claim ledgers; that is not an exhaustive novelty search.
The separate20260830 Chau/Jelonek scope audit already guards the dangerous
Euler-positivity misreading. ROOT reread correct Jelonek2011.03472v3,
Theorems1.1--1.2 and proofs: its no-self-intersections exclusion uses curve
topology and line injectivity, not (T); the connected Euler clause assumes
smoothness. The current arXiv v6 explicitly withdraws v4/v5. No general
connectedness exclusion is imported here. Chau's polynomial parametrization
does give A1 normalizations, but this theorem does not need it.

QUANTITY: the exact field-trace image for an arbitrary actual complex
Keller map. CHEAPEST DISCRIMINATOR completed manually is the right-exact
top-de-Rham map onto the point quotient, plus the DVR trace-dual argument.
The remaining gate is hostile review of those deductions, (Y)'s exact
scope, reducible Mayer--Vietoris extension and formal node specialization.
If confirmed, (T) is a source-attached necessary-condition interface.
The genuinely unsolved step is to force a trace violating it, or prove
its compatibility with a polynomial A2 source impossible. Merely counting
branches, reasserting height-one fullness, or treating M as an algebra
cannot do that. No claim here resolves JC2, constructs a polynomial pair,
or establishes a new global degree bound. No new OPEN identifier is added.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13707`.
- Body SHA-256:
  `dae022b6cbf0c4fd110f3a905a02875fb4268c5c5940d0105079ee5f7ff4b8b1`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
