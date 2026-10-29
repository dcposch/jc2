# Residue maps at simple-pole divisors

swarmHQ ROOT proof, independently reviewed through the Sol adapter. Status: **PROVISIONAL / MANUAL / PASS_CONDITIONAL** on the standard surface-extraction facts stated below. This is not a formal proof or a novelty claim. The [independent review](simple-pole-review-sol56-20261029T2125Z.md) and [original evidence](../box/simple-pole-residue-swarmHQ-20261029/CUSTODY.md) preserve the exact scope.

Let $K=\mathbf C(x,y)$, with its standard affine volume form $Ω=dx\wedge dy$. Normalize a divisorial valuation to value group $\mathbf Z$, and write $A(D)=\operatorname{ord}_D(Ω)+1$. Thus $A(D)=0$ means a simple pole of the two-form.

**Lemma.** If $A(D)=0$, the residue curve is $\mathbf P^1$ and admits a rational coordinate $s$ such that

$$
\operatorname{Res}_D(Ω)=\gamma\,ds,\qquad \gamma\in\mathbf C^*.
$$

Its rational primitive has degree exactly one; its residue form has one double pole and no zeros.

We use the standard surface facts that a divisorial valuation of $K$ can be extracted by a finite sequence of point blowups from $\mathbf P^2$, following its infinitely near centres, and that later blowups preserve the generic point and rational residue field of an extracted divisor. These are the named imported foundations; the calculation below does not require a further classification theorem.

On $\mathbf P^2$, the line at infinity has label $-2$, since $\operatorname{div}(Ω)=-3L_\infty$. Divisors with affine centres have positive labels: affine prime divisors have label $1$, the exceptional divisor over a smooth affine point has label $2$, and subsequent blowups preserve positivity. Hence a zero-label divisor lies over infinity, where the total boundary remains a simple-normal-crossing tree of rational curves.

At a smooth point of a boundary component labelled $a$, the new exceptional label is $a+1$. At a node labelled $a,b$, it is $a+b$. Inductively, no boundary edge joins labels of opposite strict sign, and no edge joins two zero labels. Both properties hold initially. Smooth-centre blowups preserve them; at a permitted node the sum has the same strict sign as the nonzero labels. Therefore a zero divisor is never born at a node. It is born by blowing up a smooth point on a component labelled $-1$.

At that point choose regular parameters $u,z$, with the component $u=0$ and the centre $z=z_0$. Because the divisor of the form is supported on the boundary, locally

$$
Ω=u^{-2}b(u,z)\,du\wedge dz,\qquad b(0,z_0)\ne0.
$$

In the blowup chart $u=t, z=z_0+ts$, the form becomes $t^{-1}b(t,z_0+ts)\,dt\wedge ds$. Its exceptional residue is $b(0,z_0)ds$. The coordinate $s$ parametrizes a dense affine chart of the exceptional $\mathbf P^1$, so this is an identity of rational one-forms on the whole curve. Later blowups leave that rational form unchanged. This proves the lemma at the stated foundation scope.

**Consequence for rational maps.** Let $H$ be a dominant rational map between two such plane fields, with $H^*Ω_t=cΩ_s$, $c\in\mathbf C^*$. Suppose a source divisorial valuation restricts to $e$ times a target divisorial valuation, both with raw label zero. Let $h:D_s\to D_t$ be the induced residue map and let $f=\deg h$. Then **$f=1$**.

Indeed, a target uniformizer pulls back to $u^e$ times a unit. Taking residues at the generic divisors gives $e h^*\operatorname{Res}(Ω_t)=c\operatorname{Res}(Ω_s)$; units and regular transverse terms contribute no residue. For the degree-one primitives $R_s,R_t$ supplied by the lemma, characteristic zero gives

$$
cR_s=e(R_t\circ h)+\text{constant}.
$$

Comparing degrees gives $1=f$. No periodicity or finite invariant divisor set is needed. The residue map is affine in these primitive coordinates and carries the unique residue pole to the unique residue pole.

**Remaining gap.** The normal index $e$ is unrestricted by this argument. Residue degree one does not establish total field degree one or the weak local-homeomorphism property. The result uses the standard affine volume form, not an arbitrary exact rational two-form. It applies to divisorial simple poles, whereas the [necessary fold witness for a normalized hypothetical Keller counterexample](double-pole-residue-witness-normalization-swarmHQ-root-astra-sol56-20261029.md) has raw label $A=-1$, and the specified inverse ends are infinitely singular. Excluding that negative-pole fold for the whole polynomial source remains open. JC2 remains unresolved.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4482`.
- Body SHA-256:
  `f68441b52a2210c4169090e56c7354de2c03b7565cefd582c7c7b1ba0ffd094d`.
- Frozen basis: `26efb4f4ca452199c6d4bdab4210602071d6abcf`.
