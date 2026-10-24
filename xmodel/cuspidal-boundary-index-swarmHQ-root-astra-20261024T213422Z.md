# Cuspidal boundary, source projection, and a conditional ramification-index bound

Producer: swarmHQ coordinator (requested gpt-6-astra), with Astra co-research.
Date: 2026-10-24. Basis: `83e557483fbaf6eb9cb0588881bb4615a700164a`.
Evidence: MANUAL, conditional proofs with named standard dependencies.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED; frozen public-artifact review pending.

## Hypotheses and conclusions

For the first two conclusions, assume **all** hypotheses of the
[conditional finite-factor theorem](finite-stein-factor-boundary-swarmHQ-root-20261024T202659Z.md).
In particular, \(X\) is smooth projective rational, \(U=\mathbb A^2\), and
\(\rho:X\to Y\) is proper birational analytic with \(Y\) normal compact and \(Y\setminus B=U\).
The reduced boundary \(B\) is irreducible and the meromorphic standard volume satisfies
\(\operatorname{div}\Omega=-B\), identifying the genuine dualizing ideal \(\omega_Y=\mathcal O_Y(-B)\).
An actual volume-preserving polynomial Keller iterate is resolved by \(\pi:Z\to X\), isomorphic over all \(U\).
Write \(c=\rho\pi\) and \(H=\rho G=hr\) for its analytic Stein factorization \(Z\xrightarrow r W\xrightarrow hY\).
Retain the unique boundary extension represented by the source divisor, with index \(e=N>1\) and residue degree one.
Put \(C=(h^{-1}B)_{\rm red}\). The preceding theorem gives rational singularities on \(W\),
an isomorphism \(h|_C:C\to B\), arithmetic genera one, and \(\operatorname{div}(h^*\Omega)=R-C\) with \(R\ge0\).

1. Both \(B\) and \(C\) have rational normalization and exactly one ordinary cusp, intrinsically as curves.
2. There is a proper birational **source-direction** map \(k:W\to Y\) with \(c=kr\), identity on \(U\).
   Its restriction to \(C\) is an isomorphism; every exceptional curve meets \(C\) at exactly one set-theoretic point.
3. **Add** that the target surface is smooth at the cusp, with local equation \(g=y^2-x^3\) for \(B\).
   If \(m\) is the local Cartier index of \(C\) above that point, then \(m\mid e\) and \(e\le5m\).

The intrinsic cusp does not establish the extra ambient-smoothness premise. The index \(m\) is not bounded here.
These compactification hypotheses are not attached to every Keller map; none of the conclusions proves JC2.

## 1. The intrinsic cusp

Smooth projective rationality gives \(H^1(X,\mathbb Q)=0\). The proper birational map \(\rho\) has connected fibres.
Proper base change identifies \(\rho_*\mathbb Q_X=\mathbb Q_Y\), and low-degree Leray injects
\(H^1(Y,\mathbb Q)\) into \(H^1(X,\mathbb Q)\). Thus \(H^1(Y,\mathbb Q)=0\).
The compact-support exact sequence for \(U=Y\setminus B\) contains
\[
H_c^1(U,\mathbb Q)\longrightarrow H^1(Y,\mathbb Q)\longrightarrow H^1(B,\mathbb Q)
\longrightarrow H_c^2(U,\mathbb Q).
\]
The outer groups vanish because \(U\) is real four-space. Hence \(H^1(B,\mathbb Q)=0\).
The constant-sheaf normalization sequence gives
\(b_1(B)=2g(\widetilde B)+\sum_p(r_p-1)\), where \(r_p\) is the number of analytic branches.
Consequently the normalization is rational and every germ is unibranch.
The holomorphic normalization sequence and \(p_a(B)=1\) give \(\sum_p\delta_p=1\).
There is exactly one singular germ, whose local ring \(A\subset\mathbb C\{t\}\) has normalization colength one.
An element of order one would have an analytic inverse and put \(t\) in \(A\), making the germ normal.
Therefore \(A\subset\mathbb C+t^2\mathbb C\{t\}\); equal colength one makes this equality.
This is the ordinary cusp ring \(\mathbb C\{t^2,t^3\}\). The isomorphic curve \(C\) has the same description.

## 2. The source-direction projection

No \(r\)-exceptional curve meets \(U\), by local quasi-finiteness of the actual Keller map.
The strict transform of the source boundary divisor is not \(r\)-exceptional: \(H\) maps it onto \(B\).
Every other curve in \(Z\setminus U\) is contracted by the proper birational map \(c\), whose target has sole boundary prime \(B\).
Each connected \(r\)-fibre therefore has a one-point image under \(c\).
The reduced image graph of \((r,c):Z\to W\times Y\) is proper over \(W\), with one-point fibres, hence finite.
It is birational over normal \(W\), so is isomorphic to \(W\). This produces the proper birational map \(k\).
Since \(c^{-1}(U)=U\), we have \(k^{-1}(U)=U\), and \(k\) is the identity there.
The restriction \(k|_C\) is finite birational onto \(B\). Equal arithmetic genera kill its finite-length cokernel,
so it is an isomorphism. The reduced complement of \(U\) is \(C\) together with the exceptional curves of \(k\).
Every such curve \(D\) meets \(C\): otherwise finite \(h\) would send it to a complete positive-dimensional curve in \(\mathbb A^2\).
It meets \(C\) at only one set point because \(k(D)\) is a point and \(k|_C\) is injective.
This supplies no assertion about intersection multiplicities or Cartier properties.

Both \(k^*\Omega\) and \(h^*\Omega\) restrict to \(dx\wedge dy\) on the actual source \(U\), so they are equal meromorphically.
Thus \(R\) is supported on \(k\)-exceptional curves, though some of those curves can have coefficient zero.
Descent \(H=Fc\) would imply \(h=Fk\). A finite map cannot contract an exceptional curve of \(k\),
so such descent requires \(k\) to be an isomorphism. Conversely an isomorphism \(k\) supplies \(F=hk^{-1}\).
The construction of \(k\) does not establish this required isomorphism.

## 3. The additional smooth-target cusp case

Assume the extra local coordinates in conclusion 3. The unique point \(p\in C\) above the cusp is the whole fibre over it.
Since \(\operatorname{div}(h^*g)=eC\), the reduced Weil divisor \(C\) has finite local Cartier index \(m\mid e\).
Put \(d=e/m\). A local equation \(t\) for the effective Cartier divisor \(mC\) satisfies \(h^*g=u t^d\),
where normality makes \(u\) a holomorphic unit. Take its analytic \(d\)-th root and absorb it into \(t\).
There is then an intermediate ring
\[
T_d=\mathbb C\{x,y,z\}/(z^d-(y^2-x^3))\ \subset\ \mathcal O_{W,p}.
\]
It is irreducible by the cusp-prime Eisenstein valuation, and normal by the hypersurface \(S_2\) property and isolated singular locus.
The actual local ring is finite over \(T_d\), of generic degree \(m\). No cyclicity of the original \(h\) is assumed.
If \(m=1\), finite birational normality identifies the local ring with \(T_e\).

Here is the needed finite-trace argument. For a normal proper modification \(\beta:T'\to T_d\),
normalize the dominant component of \(W\times_{T_d}T'\). It gives finite \(\phi':W'\to T'\) and a normal modification \(\beta':W'\to W\).
Rationality of \(W\) gives \(R^1\beta'_*\mathcal O_{W'}=0\): resolve \(W'\) and use the Leray injection into the zero \(R^1\) of the composite resolution.
Normalized finite trace splits \(\mathcal O_{T'}\to\phi'_*\mathcal O_{W'}\), since \(T'\) is normal and the characteristic is zero.
Exact finite direct images then imply \(R^1\beta_*\mathcal O_{T'}=0\). Other branch curves do not invalidate this splitting.

If \(d\ge6\), take the weighted blowup of \(T_d\) with weights \((2,3,1)\) on \((x,y,z)\).
Its \(z\)-chart is \(b^2-a^3=z^{d-6}\), with \(x=z^2a,y=z^3b\): it is smooth for \(d=6,7\), and has only an isolated hypersurface singularity otherwise.
The \(x\)-chart is a finite \(\mu_2\)-quotient of \(v^2-1=u^{d-6}w^d\); the \(y\)-chart is a \(\mu_3\)-quotient of \(1-v^3=u^{d-6}w^d\).
These covers are smooth near the exceptional curve, including \(d=6\). The entire strict transform \(T'\) is therefore normal.
Its reduced exceptional curve \(E\subset\mathbb P(2,3,1)\) is the smooth elliptic curve \(y^2=x^3+z^6\) for \(d=6\).
For \(d>6\) it is \(y^2=x^3\), with normalization \([s:t]\mapsto[s^2:s^3:t]\), one ordinary cusp, and no other singularity.
In both cases \(H^1(E,\mathcal O_E)\) has dimension one.
But the ideal sequence of \(E\), the vanishing \(R^1\beta_*\mathcal O_{T'}=0\), and
\(R^2\beta_*I_E=0\) for a proper map with fibres of dimension at most one force \(H^1(E,\mathcal O_E)=0\).
This contradiction gives \(d\le5\), hence \(e\le5m\), without ADE classification.

## 4. Why the index remains a genuine extra input

An exact local diagnostic preserves the cusp and rationality while allowing unbounded index.
Take the weighted blowup of smooth \((x,y)\)-space with weights \((1,n)\), \(n\ge3\), and boundary \(y^2=x^3\).
Its \(y\)-chart is \(yz=x^n\). The strict boundary has ideal \((y^2-x^3,z-x^{n-3}y)\), with quotient exactly \(\mathbb C\{x,y\}/(y^2-x^3)\).
For the exceptional prime \(D=(x,y)\), \(\operatorname{div}(y)=nD\) and \(\operatorname{div}(y^2-x^3)=C+3D\).
The chart is the finite smooth quotient \(x=uv,y=u^n,z=v^n\) by \(\mu_n\) of weights \((1,-1)\), and is rational by the same trace argument.
The exact index of \(D\) is \(n\): pulling a principal \(aD\) to the cover gives \(u^a\) times a unit,
and invariance of the unit's nonzero constant forces \(n\mid a\); the function \(y\) realizes \(nD\).
Hence the index of \(C\) is \(n/\gcd(n,3)\).
On \(z\ne0\), the pulled-back volume is
\(-x^{n-3}(x^{2n-3}-z^2)^{-1}dx\wedge dz\), with divisor \((n-3)D-C\).
This example has **no required finite map \(h\)** and no global Keller source.
It only prevents bounding the index from rationality, the reduced cusp, and the source modification alone.

## Dependencies, scope, and replay

The arguments use the cited conditional finite-factor theorem and standard complex-analytic
proper mapping/base change, finite normalization and trace, coherent direct images, birational normality,
compact-support cohomology, and curve normalization facts, with hypotheses given above.
These are named imports; no external paper proof, formal certificate, or novelty claim is supplied.
Desk-only replay checks the graph direction, intrinsic versus ambient cusp, the intermediate cyclic ring,
the trace diagram, weighted charts, and the diagnostic's missing finite-map hypothesis. No numerical experiment is involved.
ROOT supplied the projection, topological cusp argument, cyclic/weighted lead, and index diagnostic;
Astra checked and extended the index argument using finite trace and exceptional-curve cohomology.
The frozen mathematical candidates received configured Sol5.6 critique, with prior baseline-reading qualifications retained;
this public formatting still requires its own delta review before promotion.

For actual iterates the conditional inequality is only \(N^j\le5m_j\) when the target is smooth at the cusp.
Ambient singularity control and a uniform bound on \(m_j\) using the **same finite maps and Keller compatibility** remain missing.
No vanishing of \(R\), equality \(W=Y\), properness, descent, all-Keller attachment, or infinitely singular case is settled.

## OPENS RAISED

None. These results sharpen the existing normalization/descent question without introducing a new named test.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `83e557483fbaf6eb9cb0588881bb4615a700164a` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10960`.
- Body SHA-256:
  `eac461829dbd8df9908c7401373e64140bdd41c172ef734deb4def769b20677f`.
- Frozen basis: `83e557483fbaf6eb9cb0588881bb4615a700164a`.
