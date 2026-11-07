# HAMREVIEW1815 — independent hostile review of uniform cusp-filtration rigidity

Verdict: CONFIRM_UNIFORM_CUSP_THEOREM
Status: COMPLETED REVIEW at the exact scope below; no promotion action is taken here.
Review UTC observed before final write: 2026-11-07T18:17:44.258976290Z
Required useful draft UTC retained: 2026-11-07T18:14:18.573558574Z
Configured model: gpt-5.6-sol / ultra; hosted identity UNVERIFIED.

## Custody and reading

The copied packet reader has SHA-256 `47e3aea5fd494d0966aad35312aa3eea689a000b05289bd03646b9e5d577fbe4`.
Preflight verified the pinned manifest, its 17 inputs, physical nonsymlink ancestry, modes, hashes, LF counts, and both report seals.
The manifest itself is the eighteenth frozen packet file.
PROPOSAL.md has SHA-256 `136603ace7abb1279bed04341f7cf42e89de52af7c2bfbb16d1299767033af9e` and its seal verified at basis `9d7fdb904649ea282731e1455e749779c0f32751`.
PRIOR_THEOREM.md has SHA-256 `888a9ecffd43e02090168c1f8ba57563d7fdc04d8a16ed4b002cfa845dc926f7` and its seal verified at basis `a636e88e7cfc086340c87f66ff149e48f0120d63`.

Startup ACK was written mode 0444 at 2026-11-07T18:08:07.433002+00:00.
ACK immutable0444; it proves neither hosted identity nor mathematics.
No narrow command-format correction was used.

Whole-reading charge was 2043/3500 non-STATE LF and 122/180 STATE LF.
The non-STATE total is 269 MANIFEST + 1342 governors + 50 ADMISSION + 4 METHOD + 164 PROPOSAL + 214 PRIOR_THEOREM.
Historical reading was 378/400 LF, namely all 164 proposal LF and all 214 prior-theorem LF.
Repeat, help, and own-report-preview charge was 29/100 LF: 29 help, 0 repeat, 0 preview.
All required body windows reached `next_start=null`; no truncated display receives credit.

## Exact confirmed scope

Fix coprime integers p,q>=2, put s=pq-p-q, B=C[x,y], and w=x^p-y^q.
Give the unique normal monomials x^i y^a w^b, 0<=i<p, weights qi+pa+sb, and let δ be their maximum weight.
Let F*:B->B send x to P and y to Q, with Jac(P,Q)=J in C*.
Assume the full-filtration equality

    δ(F*f)=e δ(f)

for every nonzero f in B and an integer e>=1.
Then e=1, P=αx, Q=βy, αβ!=0, and α^p=β^q.
If J=1, also αβ=1 and α^(p+q)=1.
Conversely every such diagonal map preserves δ exactly.

The full homogeneous Rees consumer is also valid for every such p,q under exactly the hypotheses in PROPOSAL.md lines 114-131.
In particular, homogeneous U,V,H of weights qe,pe,se satisfying the full relation and whose reductions define an injective Poisson map admit only e=1.
This is a theorem about the displayed cusp filtration and the stated full polynomial lift, not arbitrary Keller maps or arbitrary filtrations.

## 1. General Poisson and divergence rigidity

Let A=gr_δ(B) be a domain and suppose the induced degree-zero bracket on Frac(A) has center C.
The scalar-center hypothesis implies that the bracket is nonzero.
Choose homogeneous leading forms fbar,gbar with nonzero bracket and lift them to f,g.
Then δ({f,g})=δ(f)+δ(g).

For L=a partial_x+b partial_y preserving the filtration, direct differentiation gives

    L{f,g}={Lf,g}+{f,Lg}-(a_x+b_y){f,g}.

The first three terms have degree at most δ(f)+δ(g).
Multiplicativity and the equality for {f,g} therefore give δ(div L)<=0 whenever div L is nonzero.
Since δ vanishes exactly on nonzero constants, div L is constant.

If div L=0, the polynomial one-form b dx-a dy is closed.
Termwise integration gives a polynomial H with H_x=b and H_y=-a, so L={H,-}.
If L is nonzero, then H is nonconstant and its leading form Hbar is not scalar.
The fraction-field center condition supplies a homogeneous fbar with {Hbar,fbar} nonzero.
For a lift f this forces

    δ(Lf)=δ(H)+δ(f)>δ(f),

contradicting preservation.
Thus the divergence kernel is zero and the preserving derivation space has dimension at most one.
If it contains a derivation of nonzero divergence, every preserving derivation is its scalar multiple.
This argument uses polynomial Hamiltonian integration only; it assumes no normality, smooth symplectic locus, boundary extension, or complete flow.

## 2. Every coprime-cusp hypothesis

Here s=(p-1)(q-1)-1>=1 because p,q>=2 are coprime.
The monic equation x^p=y^q+w gives the complete and unique C[y,w]-basis 1,x,...,x^(p-1).
Taking highest weights gives

    A=C[X,Y,W]/(X^p-Y^q),  deg(X,Y,W)=(q,p,s).

Coprimality makes X^p-Y^q prime, for example through X=z^q and Y=z^p.
Hence A is a domain, δ is multiplicative, all filtration pieces are finite dimensional, and only constants have degree zero.
Bezout gives z in Frac(A), so the actual fraction field is C(z,W), not a larger auxiliary field.

The source brackets are

    {x,y}=1,
    {y,w}=-p x^(p-1),
    {x,w}=-q y^(q-1).

Their degrees are bounded by the sums of generator degrees, with equality for the last two.
The normal basis and Leibniz rule therefore prove the bracket filtration for every pair of polynomials.
The induced brackets are

    {X,Y}=0,
    {Y,W}=-p X^(p-1),
    {X,W}=-q Y^(q-1).

Using X=z^q gives

    {z,W}=-z^(pq-p-q+1)=-z^(s+1).

A rational function commuting with z has zero W derivative and lies in C(z).
Commuting also with W then gives zero z derivative, hence a scalar.
Thus the fraction-field Poisson center is exactly C even though the bracket degenerates at z=0.
No normality or everywhere-symplectic assertion is needed.

The actual polynomial derivation

    E=q x partial_x+p y partial_y

preserves δ because E(w)=pq w and every normal monomial is an eigenvector.
Its divergence is p+q, so the general lemma makes every δ-preserving polynomial derivation a scalar multiple of E.
The Euler eigenvalue pq on w is correctly kept distinct from the filtration degree s.

## 3. Full-image Euler transport

The constant Jacobian defines polynomial derivations D_P and D_Q with
D_P(P)=1, D_P(Q)=0, D_Q(P)=0, and D_Q(Q)=1.
For

    D=qP D_P+pQ D_Q

one has D(F*f)=F*(Ef) for every f.
The exact scaling hypothesis induces an injective graded map φ:A->A multiplying degrees by e.

Every polynomial derivation L has finite filtered order

    r=max(δ(Lx)-q, δ(Ly)-p, δ(Lw)-s),

with δ(0)=-infinity.
The normal basis and Leibniz rule give δ(Lf)<=δ(f)+r, and a generator attains r when L is nonzero.
Therefore a positive r for D would produce a nonzero degree-r derivation Dbar of A.
The transport identity has degree at most eδ(f), so Dbar annihilates the full graded image φ(A), not merely its generators.

Put K=Frac(A) and K0=Frac(φ(A)).
Both have transcendence degree two and K is finitely generated over K0, hence K/K0 is finite algebraic.
Characteristic zero makes it separable.
Differentiating the minimal polynomial of any element shows that a K0-linear derivation of K is zero.
Thus Dbar would be zero, a contradiction, and D has filtered order at most zero.

The rigidity lemma gives D=μE.
Both D_P and D_Q have zero divergence, while

    div(D)=qD_P(P)+pD_Q(Q)=p+q=div(E).

Hence μ=1.
It follows that E(P)=qP and E(Q)=pQ.
Coprimality and p,q>=2 make x the sole monomial of Euler weight q and y the sole monomial of Euler weight p.
Thus P=αx and Q=βy.
Exact scaling on y gives e=1.
Exact scaling on w forces α^p=β^q because otherwise the y^q term has degree pq>s.
This transport uses only the finite separable extension of graded fraction fields, not integrality or finiteness of B over F*B.

## 4. All-(p,q) full Rees consumer

The ring

    S=C[X,Y,W,T]/(X^p-Y^q-WT^(p+q))

with weights q,p,s,1 embeds as X=xt^q, Y=yt^p, W=wt^s, T=t in B[t].
It is a graded domain, S/(T)=A is a domain, T is prime, and S_0=C.
The displayed bracket is homogeneous of degree zero.

Bracket the full relation U^p-V^q=T^((p+q)e)H with V.
This gives

    -p U^(p-1){U,V}=T^((p+q)e){V,H}.

Injectivity of the reduced map makes Ubar nonzero, so T does not divide U.
Primality, cancellation in the domain, and induction on the T exponent show that T^((p+q)e) divides {U,V}.
Homogeneity then gives {U,V}=cT^((p+q)e) with c in C.
After cancellation, {V,H}=-pcU^(p-1).
Reduction modulo T and the prescribed Poisson identity give c=1.
Specializing T=1 therefore yields an ordinary polynomial Keller pair with Jacobian one.

For completeness, the terse scaling step in PROPOSAL.md line 128 is valid as follows.
Define the graded endomorphism Θ of S by X->U, Y->V, W->H, T->T^e.
The full relation makes Θ well defined, and its reduction is the injective map ψ:A->A.
For nonzero f of δ-degree d, apply Θ to its homogeneous Rees lift.
The result has degree ed, specializes to F*f, and reduces to ψ(fbar), which is nonzero.
It is therefore not divisible by T, so δ(F*f)=ed.
The confirmed theorem applies and forces e=1.
No finite jet, rational lift, or completed-local lift is excluded.

## Limitations and disposition

The proof establishes no suitable filtration for an arbitrary Keller map.
It establishes no filtration-preserving Liouville derivation outside the explicit cusp filtration.
It does not settle the general finite-normalization, properness, omitted-boundary, or whole-source realization gaps.
It makes no JC2 conclusion, source-integrality claim, novelty claim, downstream generalization, promotion, or automatic successor.
No source or web access, repository or history search, CAS, native or secondary model, control-family farm, or retry was used.
PRIOR_THEOREM supplies only the old p=2,q=5 comparison; the uniform proof above was checked independently from the general hypotheses.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9422`.
- Body SHA-256:
  `59c940df94f33db2eac2315d16f245ba68d13ca433409baf8b7f8f16708d5382`.
- Frozen basis: `f8c3ebfc4fe785cba1414e8ec3e1b3b9ef923886`.
