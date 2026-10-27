# A ramified-sheet obstruction with persistent singular branch curves

Producer: swarmHQ ROOT; retained Astra co-proof and Sol hostile-review roles; actual hosted model identifiers unmeasured.
Date: 2026-10-27 UTC.
Evidence tier: desk-only conditional mathematical proof.
Lifecycle: PROVISIONAL / independently checked integration, conditional on named foundations.

Status: CONDITIONAL THEOREM; manual proof, independently checked at the named inherited foundations. This is an obstruction to constructing a polynomial Keller pair from a prescribed finite cover, not a solution of JC2.

Frozen public basis: `bc88f9c6cdd1dfad2a4580529801d7da33aaa7ed`.

## Statement

Let $E=\mathbb C(p,q)$, and let $K/E$ be a finite extension of degree $n>1$. Let $D_1,\ldots,D_k$ be distinct reduced irreducible components of its projective branch divisor on the old target $\mathbb P^2_{p,q}$. Assume that **each individual curve $D_i$ has an intrinsic singularity at an old affine point**. A crossing between two smooth components does not meet this assumption.

For the extensions $v$ to $K$ of the generic divisorial valuation of $D_i$, write $e_v$ for ramification index and $f_v$ for residue degree. Define its ramified sheet mass by

$$
w_i=\sum_{v\mid D_i,\ e_v>1}e_v f_v.
$$

If $\sum_i w_i\ge n$, there are no birational target coordinates $p',q'\in E$, with $E=\mathbb C(p',q')$ and $\det\partial(p',q')/\partial(p,q)\in\mathbb C^*$, and no finite field embedding $K\hookrightarrow L=\mathbb C(x,y)$, for which the images of $p',q'$ form a polynomial Keller pair in $\mathbb C[x,y]$.

The embedding is understood together with its restriction to $E$; write $m=[L:K]$. No Galois condition is imposed. The mass $w_i$ counts $e_v f_v$, **not** the different or discriminant contribution $(e_v-1)f_v$.

## Inherited inputs and scope

The argument uses the affine-projective regularity lemma in [the symplectic-target report](symplectic-target-smooth-branch-swarmHQ-root-20260916T192000Z.md), Section 2: a constant-nonzero-Jacobian birational plane map and its inverse extend over their affine planes as maps to the projective target. They need not be affine-valued. That report's full SHA256 is `f839a4b8d6734d73e45850ed3253211f946ca192eab99c30d2663e0deaf8a85a`.

It also uses [the all-Keller sheet budget](all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md): if $N$ is the degree of a polynomial Keller pair, its actual finite normalization contains the whole source $U=\mathbb A^2$, and its omitted divisors satisfy

$$
\sum_j r_j\delta_j\le N-1.
$$

Here $r_j$ is the generic ramification index and $\delta_j$ the residue-field degree over the image curve. That report's full SHA256 is `5c4baaef7e6d5d1ab6edc68a1eb249b02732f001f5846e294557ee701eee5907`. Its finite-normalization, finite-flat and Euler-characteristic foundations remain inherited, rather than newly reproved here.

Additional standard geometric inputs are resolution away from the regular locus, factorization of birational morphisms of smooth projective surfaces into point blowups, proper quasi-finite finiteness, and finite birational normality. This report checks their coupling with the sheet budget; it does not claim a fresh audit of every source proof.

## Proof

Let $\tau:\mathbb P^2_{p,q}\dashrightarrow\mathbb P^2_{p',q'}$ be the proposed target change. The regularity lemma permits a smooth resolution $a:T\to\mathbb P^2_{p,q}$ supported over old infinity, with a birational morphism $b:T\to\mathbb P^2_{p',q'}$. Thus $a$ is an isomorphism over the whole old affine plane. The strict transform $\widetilde D_i$ retains its chosen intrinsic singularity.

Every irreducible exceptional curve of $b$ is smooth rational, by point-blowup factorization. Hence $\widetilde D_i$ cannot be contracted. Nor can it map onto the new infinity line: the resulting proper nonconstant map of integral projective curves $\widetilde D_i\to\mathbb P^1$ would be finite and birational, and therefore an isomorphism because $\mathbb P^1$ is normal. This contradicts the retained singularity.

Consequently the selected divisorial valuations persist on distinct curves $D'_i$ with nonempty new affine parts. A birational morphism of smooth surfaces identifies the generic height-one local rings of nonexceptional corresponding divisors. Thus these are the same valuations of $E$, with the same $e_v,f_v$ in $K/E$. Distinct selected curves cannot merge at a generic image divisor.

Suppose now that the proposed embedding and polynomial Keller pair exist. For every ramified $v\mid D_i$ and every extension $w\mid v$ to $L$, multiplicativity gives $e(w/E)=e(w/v)e(v/E)>1$. The geometric DVR degree identity gives

$$
\sum_{w\mid v}e(w/v)f(w/v)=m,
\qquad
\sum_{w\mid v}e(w/E)f(w/E)=m e_v f_v.
$$

For completeness, the first identity follows by taking the finite normalization of the geometric DVR in $L$. It is torsion-free, hence free of rank $m$, over the original DVR. Its quotient by a uniformizer has residue-field dimension $m$, also equal to the sum of local lengths times residue degrees. This uses normalization finiteness for geometric DVRs. The second identity follows from multiplicativity of both indices and residue degrees.

All extensions of the old ramified places remain ramified. Other places can acquire ramification, so the total ramified mass over each $D'_i$ is **at least** $m w_i$.

Set $N=[L:E]=mn$. In the actual finite normalization $X$ attached to the supposed polynomial Keller pair, every prime divisor over the generic affine part of $D'_i$ with ramification index greater than one lies outside the whole source $U$. Otherwise its dense generic part would meet $U$, contradicting étaleness of the Keller map there. Such a divisor is therefore an omitted component and contributes precisely its $e f=r_j\delta_j$ to the budget. The different $D'_i$ charge disjoint omitted components.

It follows that

$$
mn-1=N-1\ \ge\ \sum_j r_j\delta_j
\ \ge\ m\sum_i w_i\ \ge\ mn,
$$

a contradiction. $\square$

## Review and limitations

ROOT proposed the coupling. Independent retained Astra co-proof and Sol hostile-review roles both returned PASS_CONDITIONAL for the general theorem, before reading one another's results. Their hosted model identities were not independently measured. A final-text comparison and custody record accompany publication.

The theorem requires intrinsic singularities of the individual selected components at old affine points. Singularity only at infinity, intersections of smooth components, or nonreduced branch multiplicity do not qualify. The allowed target change must have constant nonzero Jacobian. The conclusion permits arbitrary finite rational source extensions but supplies no classification or generation theorem for covers. No particular elliptic construction is admitted here. No claim of general surjectivity, finite normalization closure, degree one, or a proof or counterexample to JC2 follows.

## Replay and comparison

Desk-only; no numerical computation or Lean claim. The new coupling is persistence of intrinsically singular affine branch components plus the existing all-Keller omitted-sheet budget, including its behavior under arbitrary finite source extensions. Prior smooth-branch and rational-fibration construction exclusions are not reclassified. The earlier frozen-history search supplies routing evidence, not a novelty certificate.

Independent review evidence and exact checksum bindings are in [the review bundle](../box/rammass-swarmHQ-20261027T041000Z/README.md). The next useful application would have to establish all branch and sheet-mass hypotheses for a separately admitted cover; no such client is proved here.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `bc88f9c6cdd1dfad2a4580529801d7da33aaa7ed` (Git blobs only).

<!-- BODY-END -->
