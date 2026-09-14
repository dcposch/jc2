# Zero-defect node: trace image and localization

MANUAL / UNREVIEWED conditional co-research. First action 2026-09-11 19:53:25.708431496 UTC; original publication reserve 20:10 UTC, hard stop 20:13 UTC. No mathematical computation or external source access.

This report uses only ROOT TASK and the pinned, explicitly unreviewed one-dicritical report. Its ordinary-node source model is conditional, not a promoted existence theorem or Keller example.

## 1. Verdict and exact source conditions

The proposed trace-image calculation is correct for the stipulated open-source model. Its tensor-base-change attachment also follows from the full actual-node hypotheses below, using finite normalization and the ordinary-node covering comparison. It does NOT follow merely from two abstract disjoint transpositions. The resulting cokernel is nonzero although the stipulated local defect K_p is zero. This refutes height-one trace saturation as a sufficient gluing argument; it proves neither existence nor exclusion of a global Keller map.

Write A=C[P,Q], R=C[x,y], K=Frac(A), L=Frac(R), and N=[L:K]. For an actual Keller map with Jacobian c in C*, P,Q are algebraically independent, the extension is finite separable, and the morphism Spec(R)->Spec(A) is etale and quasi-finite. Let Z be the finite normalization of Spec(A) in L; finiteness holds for this finitely generated complex algebra. Its coordinate ring embeds in R: an element integral over A is integral over R and belongs to the normal domain R. The induced quasi-finite birational map Spec(R)->Z is an open immersion by the normal-target form of Zariski's Main Theorem. Denote its closed complement by E.

At the chosen node, put S=widehat(A_p)=C[[u,v]], with reduced d a unit times uv. The required local data are:

1. The actual N-sheet finite etale cover off D has, on a sufficiently small nodal neighborhood, meridian orbits of types (2,1), (1,2), and N-4 trivial orbits: the two transpositions have disjoint supports.
2. Exactly two sheets are absent over a general point of EACH smooth branch. This is the charged generic affine-fibre count N-2, not merely an inertia statement.
3. Exactly N-4 affine points lie over the node, as stipulated by K_p=0 and N-a_p=2r_p=4. There are no omitted sheets off D.

Here and below N>=4. The charged report stipulates these actual local covering/fibre data; it has not established that any global Keller map realizes them.

The finite normalization after base change has factors

    O(Z) tensor_A S = B1 x B2 x S^(N-4),
    B1=C[[a,v]], u=a^2;  B2=C[[u,b]], v=b^2.

The local comparison used here is explicit. The complement of a node in a small bidisc has fundamental group Z^2. Each two-sheet orbit is the unique connected double cover with sign character on just its indicated meridian, hence is the restriction of u=a^2 or v=b^2. Trivial orbits give trivial covers. The finite normal extension across the divisor is uniquely determined by that cover; its two smooth normal extensions are the displayed power-series rings after completion. This uses the finite complex-analytic covering/normalization comparison, not a claim that a monodromy permutation alone specifies an arbitrary open source. Equivalently one can stipulate this completed finite-normalization factorization directly. Excellence of the finite complex normalization ensures its local completions are normal.

Now the OPEN inside those factors is forced by conditions 2–3. Every ramified point a=0 or b=0 is excluded because the actual source map is etale. Every trivial-factor closed point is retained: all N-4 affine node points must be these unramified points. An open subset of a local spectrum containing its closed point is the whole spectrum, so each trivial factor is entirely retained. On B1, E is contained in V(av), contains V(a), and does not contain the generic point of V(v): excluding that unramified contribution would exceed the two absent sheets over the v branch. The only remaining closed subset of V(v) not containing its generic point is its closed point, already in V(a). Thus E on B1 is exactly V(a) set-theoretically; similarly E on B2 is V(b). Consequently

    R tensor_A S = B1[1/a] x B2[1/b] x S^(N-4).              (1)

Open complements use reduced supports, so no extra scheme structure on E changes this conclusion. Without the finite-normalization comparison or the stated generic/closed fibre membership, (1) is only a conditional algebra model: extra deleted unramified divisors can preserve branch monodromy while changing the trace image. This identifies exactly the source information that must not be silently discarded.

## 2. Global trace, flat base change, and completion

The lifted derivations on R are

    delta_P=(Q_y partial_x-Q_x partial_y)/c,
    delta_Q=(-P_y partial_x+P_x partial_y)/c.

They preserve R, extend the coordinate derivations of K, and commute with field trace. For the last assertion use separability and the sum over K-embeddings, with the unique extensions of a derivation to algebraic extensions. Thus M=Tr_(L/K)(R) is an A-submodule stable under both derivations, and contains A since Tr(a/N)=a. Off D the source is finite etale, so M lies in A[1/d]. None of this says that M is an algebra or a finite A-module.

Completion S of the localized base A_p is flat over A. Tensoring the kernel/image sequence for R->A[1/d] therefore identifies M tensor_A S with the IMAGE of the base-changed trace in S[1/(uv)]. Generic trace also commutes with scalar extension: L tensor_K Frac(S) is a product of separable field factors, and its trace is their sum. With (1), this is precisely the trace calculation in the next section, not an asserted completion of R.

Indeed, ordinary (u,v)-adic completion of the right side of (1) kills both escaping factors: u is already invertible in B1[1/a], and v in B2[1/b]. It leaves only S^(N-4). Tensor base change and adic completion of this non-finite module/algebra are different operations. In particular the escaping trace cannot be recovered by first completing the source and then taking the trace of only its retained factors.

## 3. Exact image and the missing mixed poles

Grouping even and odd powers of a gives B1=S direct-sum aS as an S-module. Since a^-1=a/u,

    B1[1/a]=S[1/u] direct-sum a S[1/u].

The two embeddings send a to a and -a, hence Tr(f+a g)=2f. Thus the first factor's trace image is exactly S[1/u], not merely a submodule of it. The second image is exactly S[1/v]; each trivial factor has image S. The sum of component traces consequently has image

    M_S = S[1/u] + S[1/v]  inside  S[1/(uv)].                (2)

This also covers N=4: the absent trivial factors are unnecessary, since 2 is a unit. Equation (2) is an additive S-module sum, not a product of rings and not an algebra. Both 1/u and 1/v belong to it, while their product does not.

For a direct proof, each element of S[1/(uv)] has a unique formal Laurent expansion with both exponents bounded below. In S[1/u], every v exponent is nonnegative; in S[1/v], every u exponent is nonnegative. Therefore every mixed coefficient with BOTH exponents negative vanishes on their sum, whereas 1/(uv) has mixed coefficient 1. Conversely, subtracting the terms with nonnegative u or nonnegative v leaves a finite sum of mixed negative monomials. The quotient is precisely

    Q = S[1/(uv)] / (S[1/u]+S[1/v])
      = direct-sum_(i,j>=1) C [u^-i v^-j]
      = H^2_(u,v)(S).                                      (3)

The last identification is the top cokernel of the two-generator Cech complex. Multiplication by u or v shifts a basis monomial toward exponent zero, at which point its class vanishes. The module is supported only at the closed point, but is infinite-dimensional over C and not a finite-length error counted by an integer defect.

Both coordinate derivations preserve each summand of (2). At any height-one prime of S at least one of u,v is a unit; after localization the OTHER summand supplies the entire localized target S[1/(uv)]. Thus every height-one stalk of Q vanishes, although Q itself is nonzero. If (1) is attached to a stipulated actual source, flat base change makes (3) the base change of its actual trace cokernel near p. Its nonvanishing then rules out global trace saturation for that conditional source. It is not just a comparison of unspecified local modules.

## 4. Controls and the meaning of zero defect

* One branch: B1[1/a] together with retained S factors has trace image S[1/u], exactly the full complement localization for d=u. The mixed obstruction needs two separately escaping branch factors.
* Add a factor missing BOTH branches: adjoining an unramified S[1/(uv)] factor to (1) makes its component trace the identity on the full localization, so the obstruction disappears. Off the divisor it only adds a trivial monodromy orbit. This is why meridians alone do not determine open-source membership. It changes the stipulated missing-sheet counts and is not a counterexample within the original source conditions.
* Identity map: N=1, R=A and the actual nonproperness divisor is empty, so d=1 and trace image equals A. Choosing an artificial nodal divisor for the identity map would not be its nonproperness data.
* Completion control: at N=4 the (u,v)-adic completion of (1) is zero, yet its ordinary tensor-base-changed trace image contains 1. Thus replacing tensor base change by source completion loses the entire phenomenon, not just a small correction.

At the charged node r_p=2 and N-a_p=4, hence K_p=(N-a_p)-2r_p=0. Equations (2)–(3) impose no extra escaping sheet or local ramification excess. The new trace cokernel instead records that poles on the two disjoint escaping components cannot be multiplied inside a trace IMAGE. It is an intersection/gluing obstruction at the node, invisible to those generic counts. No inequality equating K_p with the length or dimension of this trace cokernel is valid here. Global return-path transport and existence of the source remain separate issues.

## 5. The formal top de Rham class, without a contradiction

Use the coordinate de Rham complex with formal derivations partial_u, partial_v and forms du,dv: this is the localized continuous formal differential complex, not an assertion about unrestricted algebraic Kahler differentials of an abstract power-series field. The double residue

    Res(f du wedge dv) = coefficient_(u^-1 v^-1)(f)

annihilates partial_u(f) and partial_v(f), because a derivative could produce exponent -1 only from exponent 0, whose multiplier is zero. Every other Laurent monomial has a formal antiderivative in at least one variable. Consequently the top class of S[1/(uv)] is generated by du/u wedge dv/v. On M_S every summand integrates in the variable that is not inverted, so its top coordinate de Rham cohomology vanishes. On Q all mixed basis elements except [u^-1v^-1] are derivatives, leaving a one-dimensional top class represented by that same residue.

A naive trace-surjectivity argument loses exactly this mixed residue: it cannot express 1/(uv) as a trace from (1). Nor does surjectivity of a trace map in each degree, if hypothesized elsewhere, automatically imply surjectivity on de Rham cohomology; a kernel/connecting-map argument would still be needed. No global de Rham contradiction, Keller realization, source exclusion or JC2 conclusion follows here.

## 6. Quantity, remaining condition, and closeout

QUANTITY: the exact actual-node trace-image equality after ordinary flat base change, conditional on the charged node covering and fibre counts. Result: (1) yields (2), with nonzero cokernel (3). CHEAPEST TEST completed manually is the coefficient of u^-1v^-1; it is zero on every allowed trace and one on the proposed missing element. No scientific runtime is needed or estimated, and no code, fixture, network, new gate, descendant or canonical OPEN identifier is authorized.

The indispensable source bridge is finite normalization with its actual open subset, the small-node finite-cover comparison, the generic N-2 source membership and the node's N-4 retained points. The report explains how those hypotheses force the displayed algebra; it does not promote the unreviewed parent or infer such a node from abstract monodromy alone. All two inputs are freshly hash-checked and WHOLE-read, seals included; no linked premises are consumed. Own WHOLE readback, input postpins, scope/quantity/OPEN and collision checks precede the unique completion marker. Standard transactional publication and final custody follow, then ALL WRITERS IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12577`.
- Body SHA-256:
  `4f1185341b38bac14eca9c370844bb857724f71fb2fd85cb1af243ec143cfbe9`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
