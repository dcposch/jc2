# Pointwise fibre counts and localization of missing values

Producer: swarmHQ coordinator; independent retained Sol 5.6 review seat (native hosted identities unmeasured).
Date: 2026-10-26 UTC.
Basis: 90cd180f8053240bcdced2bcb530a12ac8b07d58.
Evidence tier: MANUAL, independently reviewed. Lifecycle: PROMOTED at the scope below.

## Statement and scope

Let F:U=A2_C -> A2_C be a polynomial Keller map and h:X -> A2 its finite target normalization, of degree e.
Use the omitted curves E_i, their irreducible images D_i, and r_i,delta_i,m_x,t_x from the accepted [all-Keller sheet budget](all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md).
Put w_i=r_i*delta_i, s_x=m_x-r_i*t_x>=0, and S_off(y)=sum_(i,x:h(x)!=y) s_x.
For each target point y, let b_i(y) count the points over y in the normalization of D_i; set b_i(y)=0 off D_i.
Repeated images D_i are counted separately for their distinct source curves E_i. Then

    #F^-1(y) = 1 + sum_i w_i*(1-b_i(y)) + S_off(y).             (1)

If every individual D_i through y is unibranch at y, this yields

    #F^-1(y) >= 1 + sum_(i:y not in D_i) w_i >= 1.              (2)

Thus every missing target value is a multibranch point of at least one INDIVIDUAL irreducible nonproper-value curve.
Crossings between distinct unibranch components alone cannot cause omission. If every individual component is everywhere unibranch, F is surjective.

## Dependencies and proof

This is a direct corollary of the accepted sheet-budget identity, not a new independent inequality. No novelty or priority is claimed.
Finite flatness of h and etaleness on the whole source give e=#F^-1(y)+sum_(i,x:h(x)=y) m_x.
The finite bijective normalization A1 -> E_i factors over normalized D_i through a polynomial g_i:A1 -> A1 of degree delta_i.
Each of the b_i(y) target normalization points has a g_i-fibre whose local degrees sum to delta_i.
Therefore sum_(x in E_i:h(x)=y) r_i*t_x=w_i*b_i(y), even for repeated images or singular E_i.
Writing S=sum_(i,x)s_x=e-1-sum_i w_i, the omitted fibre length is sum_i w_i*b_i(y)+S-S_off(y).
Substitution proves (1); nonnegativity of S_off proves (2).

## Evidence and limitations

Desk-only. The [evidence package](../box/pointwise-fibre-count-swarmHQ-20261026/README.md) preserves the original derivation and [independent review](../box/pointwise-fibre-count-swarmHQ-20261026/unibranch0420-sol56.md) byte-identically, with custody receipts and checksums.
The review checks repeated images, normalized branch multiplicities, empty fibres and the zero-boundary case. No external theorem is imported beyond the accepted dependency.
The general multibranch case remains unresolved. The result does not imply properness, injectivity, or JC2, and does not exclude self-intersections of nonproper-value curves.
History/source screening was bounded; the collision check below concerns explicitly raised OPEN entries only and is not a novelty test.

## OPENS RAISED

None. The existing general surjectivity gap is localized, not closed.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `90cd180f8053240bcdced2bcb530a12ac8b07d58` (Git blobs only).
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3211`.
- Body SHA-256:
  `77f1694f8db39a97b4e90f9868144647235175dcf60030a9a12f3edd26f7d7fe`.
- Frozen basis: `90cd180f8053240bcdced2bcb530a12ac8b07d58`.
