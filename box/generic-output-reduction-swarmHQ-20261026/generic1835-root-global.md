# Generic output coordinates: global reduction conditional on the local lemma

Tier: INTERNAL/UNREVIEWED. Complete conditional argument; local premise L is not proved here.
For a nonlinear complex polynomial Keller map F with det DF=1, a nonempty Zariski-open set of determinant-one linear output changes gives a map H whose Favre–Jonsson eigenvaluation is centered at a regular attracting point of the line at infinity, with the germ below.
Conditional on L and the named FJ inputs, that eigenvaluation is infinitely singular. This is a reduction, not a proof of JC2.

## Exact local premise L
For d>=2 and 1<=p<d, let G(u,v)=(u^d a(u,v),u^p b(u,v)) be holomorphic at0, with a(0)b(0)!=0, preserving u^(-3)du wedge dv.
L asserts: there is no divisorial valuation centered at0 satisfying G_*nu=d nu. No classification or proof of L is supplied by this global report.

## 1. A nonempty generic set of output changes
Put d=max(deg F_1,deg F_2)>1. Choose S in SL2(C) so (P,Q)=S F has degP=d>degQ=q>=1.
If both initial degrees equal d, the degree-(2d-2) Jacobian part vanishes. For binary homogeneous forms P_d=x^d p(y/x), Q_d=x^d q(y/x), this says p q'-p' q=0, hence the forms are proportional; a determinant-one row operation lowers one degree.
If the degrees differ, a determinant-one interchange suffices. Neither component can become constant because the Jacobian remains1.
Let B=[[a,b],[c,e]] in SL2, w=(a,c), and require a!=0, P_d(w)!=0, Q_q(w)!=0.
These conditions define a nonempty Zariski-open set: choose w=(1,s) outside the finitely many roots of P_d(1,s)Q_q(1,s), then complete w to a determinant-one matrix.
Set H=B(P,Q), s=c/a, and p_infty=[a:c:0]. Its leading map is H_d=w P_d, so H_d(w)!=0; every iterated leading homogeneous composition is nonzero.
Consequently deg H^n=d^n, and lambda_1(H)=d. The same is true for the degree of the first component of H^n, since a!=0.
The generic field degree N is unchanged by S and B. Bézout applied to a generic fibre of (P,Q) gives N<=dq<d^2.
Generic finiteness follows from the nonzero Jacobian; the two generic fibre curves have no common projective component, so the Bézout application is valid.
No dynamical lower bound lambda>=N, minimization, or assumed properness is used. Since S is fixed, the allowed total changes B S also form a nonempty open subset of SL2.

## 2. The eigenvaluation has the required local centre
Use u=1/x, v=y/x-s near p_infty. Define nu_n=d^(-n)(-deg) composed with H^n, the normalized forward orbit of the degree valuation.
For every n>=1, nu_n(u)=1. The determinant-one identity gives v composed H=Q/(a H_1).
Since Q_q(w)!=0, deg(Q composed H^(n-1))=q d^(n-1), including n=1. Thus nu_n(v)=1-q/d=(d-q)/d>0 for every n>=1.
FJ Proposition2.3 supplies nu_* in V1 with H_*nu_*=d nu_*. Since N<d^2, Theorem2.4(b) gives nu_n -> nu_*; the degree valuation has skewness1>0.
Pointwise convergence on polynomials also gives convergence on these rational coordinates: x has value-1 throughout, and y-sx has value-q/d throughout.
Hence nu_*(u)=1 and nu_*(v)=(d-q)/d>0. It is centered at p_infty, not merely somewhere on the boundary. Theorem2.4(a) also supplies uniqueness in its stated nonnegative-skewness scope.
As d is integral and N<d^2, FJ Proposition2.5 says this eigenvaluation is divisorial or infinitely singular.

## 3. The actual local germ and use of L
In x=1/u, y=(s+v)/u write P=u^(-d) Ptilde(u,v), Q=u^(-q) Qtilde(u,v).
The generic conditions give Ptilde(0,0)Qtilde(0,0)!=0. Direct substitution gives
u'=u^d/[a Ptilde+b u^(d-q)Qtilde],
v'=u^(d-q)Qtilde/[a(a Ptilde+b u^(d-q)Qtilde)].
Both bracketed factors are units at0, so this is the germ of L with p=d-q. Its differential is nilpotent; it is holomorphic at p_infty.
Moreover dx wedge dy=-u^(-3)du wedge dv and det DH=1, so the meromorphic form in L is preserved exactly.
If nu_* were divisorial, its restriction at this centre would satisfy L's forbidden equality. The equality on rational functions extends to local analytic/formal functions by positive valuation of the maximal ideal and polynomial truncation.
Thus L excludes the divisorial case, leaving the infinitely singular case under the named FJ classification.
Any hypothetical noninvertible Keller map is nonlinear; determinant-one output changes preserve noninvertibility. Therefore excluding all such infinitely singular representatives would suffice for JC2. This does not exclude those representatives.

## Sources, review obligations, and limits
FJ is Favre–Jonsson, Dynamical compactifications of C2, Annals173(2011),211–249, DOI10.4007/annals.2011.173.1.6; official PDF https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n1-p06-p.pdf .
The exact cached PDF is box/dynamical-minimization-gate-20260914/favre-jonsson-annals2011.pdf in jc2, SHA e85b214ae52e6d04a42807f5e4234d945b17bcdd12e2939efbb7fa7c41ae2381.
Cached text SHA30400b3a1e1df8e99b8a4461546d9a32cd5aec4715038125ef7f9443e17ea874. ROOT read375-430 (56 LF): Proposition2.3 statement; Theorem2.4 statement/printed proof; Proposition2.5 statement/printed proof. The partial Proposition2.6 at424-430 is NOT used.
Underlying references[8],[28],[30] and AppendixA foundations remain named imports, not newly audited proofs. Bézout and the valuative topology are standard named facts. No stopped Favre2010 source was accessed.
The exact local lemma, its analytic coordinate changes and its completed-DVR argument require separate checking. A hostile review must also check the global centre argument and the scope of the imported FJ results.
This does not preserve the original F's eigenvaluation or dynamical degree. It gives no properness, surjectivity, N=1, boundary-weight bound, or exclusion of infinitely singular valuations. Hénon automorphisms are compatible with the reduction.
History scope: briefs/generic1827-selection.json and history-screen.json; exact earlier minimization report119LF personally covered. The two lexical screens are not novelty certificates. No degree/control-family successor is implied.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6025`.
- Body SHA-256:
  `7a1d798a3aa14e55917e62a6690f11406292cb90d06ab86753408c09abb11902`.
- Frozen basis: `89c9da0f2ec8c2941a78c518ecbb195d21ceb6de`.
