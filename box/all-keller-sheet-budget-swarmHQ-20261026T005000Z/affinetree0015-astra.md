# AFFINETREE0015 — all-Keller applicability of the global sheet budget
Status: CONFIRM_ALL_KELLER_EXTENSION / INTERNAL / MANUAL / UNREVIEWED.
Primary co-research of ROOT's proposal, not an independent hostile review or a novelty claim.
Launch/report3271d021f9f89db8972a8d090768ea3e1013d03f; selection1634f38ef8bd4d5b395d5020912fd5bbfc386aa2.
Frozen public47cbe1093ea6ee7b4ec6d32a7eda4a79e567c061.
No proof/counterexample of JC2, public promotion, or automatic successor.

## Conclusion and exact scope
Let F:U=A2_s→A2_t be ANY complex polynomial Keller map, and let h:X→A2_t be the
normalization of its target in C(U), of finite degree e. The WHOLE U embeds openly in X.
The omitted locus is a finite disjoint union of curves E_i, each with a finite bijective
normalization nu_i:A1→E_i. Smoothness of E_i or rational singularities of X are not assumed.
The normalization of D_i=h(E_i) is A1. Let delta_i be the degree A1→normalization(D_i)
and r_i≥1 the generic transverse ramification index of h along E_i.
For each closed x∈E_i let m_x be its local fibre-algebra length and t_x the local degree
at the UNIQUE point of nu_i^-1(x) for that polynomial normalization map. Then
    e-1-sum_i r_i delta_i = sum_i sum_(x∈E_i)(m_x-r_i t_x) ≥ 0.     (SB-all)
The sum has finite support. This extends the published sheet budget as a necessary condition
to every Keller finite normalization, without divisorial or eigenvaluation assumptions.
It does not extend the logarithmic thickening identity or settle any dynamical reduction.

## Standalone affine-enlargement lemma: purity
First let X be any normal affine complex surface containing a dense open U≅A2.
Its missing closed set has finitely many curve components and possibly isolated components.
If p is an isolated missing point outside their union E, choose f∈I_E with f(p)≠0
(and f=1 if E is empty). V=D_X(f) is affine normal and avoids all missing curves.
V∩U=D_U(f|U) is affine; V minus (V∩U) is a nonempty finite set.
Normal Hartogs gives Gamma(V,O)=Gamma(V∩U,O). The affine open immersion is therefore
an isomorphism on spectra of these rings, contradicting the missing point.
Thus X minus U is pure of dimension one when nonempty. No rational-singularity input occurs.

## Compactification and the connected infinity subtree
Embed affine X in affine space and normalize its projective closure, obtaining barX.
The normalization is an isomorphism over X. The pullback of the hyperplane at infinity is
an effective ample Cartier divisor H with support exactly barX minus X.
Resolve the birational map P2_s⇢barX by point blowups away from U.
This gives a smooth projective Z and a proper birational pi:Z→barX, isomorphic over U.
The boundary D=Z minus U is an SNC tree of P1 curves: initially it is the line at infinity;
blowing up a smooth boundary point adds a leaf, and blowing up a node subdivides an edge.
The resolution is relative to U; alternatively normal-target connected fibres exclude any
extra component over a point where the restriction on U is already an isomorphism.

Put C_inf=Z minus pi^-1(X), the support of the nef and big divisor P=pi*H.
This support is connected. Indeed if P=A+B has nonzero disjoint effective supports,
then A.B=0, A²=P.A≥0 and B²=P.B≥0, while A²+B²=P²>0.
One has positive square; Hodge index makes its orthogonal complement negative definite
modulo numerical equivalence. The other nonzero effective divisor is not numerically zero,
since it meets an ample divisor positively. This contradicts its nonnegative square.
Therefore C_inf is a connected subtree of D. No special compact target or distinguished cusp is used.

## Surviving curves and normalization fibres
Let L_i⊂Z be the strict transform of the closure of a missing curve E_i.
It is a component of D, isomorphic to P1, and is not contained in C_inf.
It meets C_inf: otherwise its nonconstant proper image would be a complete curve in affine X.
It meets C_inf at exactly one point, since two attachments to a connected subtree create a cycle.
Every other component of D outside C_inf is pi-exceptional: a noncontracted component
would map to a missing curve and be its unique strict transform.
Each connected component of the graph D minus C_inf contains at most one L_i.
Indeed two such vertices would each attach to connected C_inf and create a cycle.

Proper birational pi has connected fibres because barX is normal (Stein factorization).
For x∈X minus U, its fibre lies wholly in D minus C_inf. If two E_i met at x,
the fibre would join their strict transforms in the same graph component, a contradiction.
If two DISTINCT points of one L_i mapped to x, a connected exceptional fibre would join
them outside L_i, creating a cycle with L_i; a zero-dimensional connected fibre cannot contain two points.
More explicitly a nontrivial connected fibre is a union of exceptional curves; any additional
isolated fibre point would disconnect it. Its path between the two points, together with L_i,
violates the boundary-tree property, also if one component would meet L_i twice.
Hence the missing curves are disjoint and each restricted map L_i minus C_inf→E_i is bijective.
It is proper by base change from L_i→barX, and quasi-finite since a nonconstant curve map
has finite fibres. Thus it is finite, birational, with normal source P1 minus one point=A1.
It is precisely the normalization of E_i. A finite bijective complex map is a homeomorphism
on analytic spaces (it is proper and closed), so chi_c(E_i)=1.
This proves only finite-bijective normalization; cuspidal nonnormal E_i are allowed.

## Any Keller map supplies this affine enlargement
Write A=C[P,Q]⊂R=C[x,y], K=Frac(R). The Keller condition makes F étale and quasi-finite.
Let B be the integral closure of A in K; it is finite over A. Since R is integrally closed,
B⊂R. The induced U→Spec B is birational and quasi-finite: its fibres lie in fibres of F.
Zariski Main over the normal target makes this morphism an OPEN IMMERSION.
Thus X=Spec B is exactly a normal affine enlargement of the WHOLE U, and h is finite of degree e.
This uses no assertion that A⊂R is integral, no properness of F, and no classification of X.

For each omitted E_i, h|E_i is finite onto an affine curve D_i; it cannot contract a curve.
The composite A1→E_i→D_i is finite and factors through the normalization Dtilde_i.
The induced A1→Dtilde_i remains finite (its coordinate ring is an intermediate integral ring).
Completing gives a nonconstant finite map P1→Dbar_i. Riemann–Hurwitz forces genus(Dbar_i)=0.
Every point at infinity of Dtilde_i has a preimage, and all such preimages lie at the single
source infinity. That source infinity cannot map inside Dtilde_i, or all P1 would map into an
affine curve nonconstantly. Hence Dtilde_i=P1 minus one point=A1.
The induced map is a polynomial of degree delta_i; its local degrees t sum to the usual
finite ramification total sum(t-1)=delta_i-1. No smoothness of D_i at its singular points is needed.

## The published length/Euler proof at these weaker boundary hypotheses
A normal surface is Cohen–Macaulay. Finite dominance over smooth A2_t therefore makes h
flat of constant rank e. For every y, sum_(x over y)m_x=e.
The constructible length function m is 1 on U, since h|U is étale, and generically r_i on E_i.
Only finitely many exceptions occur: exclude singular points of X, E_i or D_i, critical points of
its normalization map, and intersections with the other components of h^-1(D_i).

To prove m_x≥r_i t_x, index x by its unique normalization preimage a∈A1.
Choose the analytic disc through the point g_i(a) in the NORMALIZED target image branch.
Base-change the finite flat map h to this disc. Its algebra is locally free of rank e.
After shrinking, the summand supported near x has constant rank m_x: the finitely many
central-fibre points separate into disjoint neighbourhoods, or equivalently into lifted idempotent summands.
At a general nearby disc point, exactly t_x normalized source points near a occur on E_i.
Finite-bijective normalization puts all of them near x; away from the finite exceptional set
they are distinct smooth curve points, each with local fibre length r_i.
Their contribution is r_i t_x; all other points in the same summand contribute nonnegative lengths.
This proves the inequality even if x is a cusp of E_i, X is singular at x, or D_i has several branches.
It does not compare different target branches or assume an affine unramified sheet over y.

Disjointness and chi_c(E_i)=1 give chi_c(X)=1+s. More directly Euler-integrate the length
identity over target A2_t to obtain integral_X m dchi_c=e, and partition X=U disjoint-union E_i:
    e-1=sum_i r_i + sum_i sum_(x∈E_i)(m_x-r_i).
The finite-bijective parametrizations identify this point sum with the sum on their A1 normalizations.
Subtract sum_i r_i(delta_i-1) and apply the local inequality to obtain (SB-all), including its slack.
This sums over the whole SOURCE; distinct omitted curves may have the same image.
No separate per-image bounds were added, and no singularity delta-invariant was silently discarded.

## Dependencies, historical scope and limits
Named classical dependencies are surface elimination of indeterminacy by point blowups,
normal Hartogs, finite normalization/Zariski Main, connected fibres over a normal target,
Hodge index, normalization and Riemann–Hurwitz for curves, finite-flat analytic length conservation,
and additivity/pushforward of compact-support Euler characteristic. Their uses are explicit above.
No theorem about rational singularities, source rulings, or the classification of affine enlargements is used.
Frozen notes51559–51570 retain a MESSAGE-ONLY BGV Section11 intake; its classification is not imported.
Archive12789–12798 and Oct19journal996–1031 already record this boundary structure and old
NO_NEW_MECHANISM/SNC-crossing stops. This proof audits it for the NEW sheet-budget consumer only.
The exact public sheet-budget113LF and mandatory custody clarification56LF were read whole.
The old reviewer’s corrected coverage is not borrowed as my own reading evidence.

Confirmed scope is one necessary numerical condition for every Keller finite normalization.
The logarithmic identity and its missing thickening estimate remain at their separately admitted scope;
there is no new global closing implication, independent-review claim, or automatic successor.
Fixed39 inputs,11 selection archive blobs,3 public report blobs and the exact frozen notes blob
were gated before mathematics; STATE332 was personally read whole by00:17:21 UTC.
Initial partial00:18:39 and checked partial00:21:56 preserve the actual audit progression.
Exact windows, errors, canonical custody, postpins and terminal collision outputs accompany this report.
OPEN(S) RAISED
None. Independent review/promotion is ROOT-owned and is not automatically commissioned here.
## COLLISIONS
Original terminal scan retained separately against this verified report and frozen public basis.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11049`.
- Body SHA-256:
  `7e5383ddfac0af238d2668a077af1aed32f6199d1ccfc5e7eb63754284380f35`.
- Frozen basis: `3271d021f9f89db8972a8d090768ea3e1013d03f`.
