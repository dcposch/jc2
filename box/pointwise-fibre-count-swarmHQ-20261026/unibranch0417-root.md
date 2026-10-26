# Fibre counts from the all-Keller sheet budget

Status: ROOT derivation, UNREVIEWED and UNPROMOTED; no novelty claim.
Basis: HQ cb1b0c16f6b0c350a71dabbe60ae81c14d9d7d7d; public 90cd180f8053240bcdced2bcb530a12ac8b07d58.
Dependency: the accepted all-Keller sheet-budget theorem, xmodel/all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md.
Its full hash is 5c4baaef7e6d5d1ab6edc68a1eb249b02732f001f5846e294557ee701eee5907.

Let F:U=A2_C -> A2_C be a polynomial Keller map, and h:X -> A2 its finite normalization of degree e.
Use the accepted omitted curves E_i, images D_i, indices r_i, polynomial normalization degrees delta_i, local fibre lengths m_x and local normalization degrees t_x.
Write w_i=r_i*delta_i, R=sum_i w_i, s_x=m_x-r_i*t_x>=0, and S=sum_(i,x) s_x=e-1-R.
For a target point y, let b_i(y) be the number of points over y in the normalization of D_i; put b_i(y)=0 when y is not in D_i.
Thus b_i counts analytic branches of the individual irreducible D_i, and repeated images D_i remain indexed by their distinct E_i.
Put n_y=#F^-1(y) and S_off(y)=sum_(i,x:h(x)!=y) s_x.

Claim, conditional only on the accepted dependency:

    n_y = 1 + sum_i w_i*(1-b_i(y)) + S_off(y).                 (1)

In particular, if every D_i through y is unibranch at y, then

    n_y >= 1 + sum_(i:y not in D_i) w_i >= 1.                 (2)

Proof. Finite flatness of h gives e=n_y+sum_(i,x:h(x)=y) m_x, since h is etale on U and the E_i are disjoint.
For each i, factor h on the finite bijective normalization A1 -> E_i through the normalization A1 -> D_i.
The intervening map g_i:A1 -> A1 is a polynomial of degree delta_i.
For each of the b_i(y) target normalization points, the sum of local degrees in its g_i-fibre is delta_i.
Bijectivity of A1 -> E_i therefore gives sum_(x in E_i:h(x)=y) r_i*t_x=w_i*b_i(y).
Consequently e-n_y=sum_i w_i*b_i(y)+S-S_off(y). Substitute S=e-1-R to obtain (1); nonnegativity of S_off gives (2).

Consumer. Every omitted target point must be a multibranch point of at least one individual irreducible nonproper-value curve.
A crossing between distinct unibranch components alone is insufficient. If every individual component is everywhere unibranch, F is surjective.
This does not prove surjectivity for arbitrary F: nonproper-value curves may have self-intersections, and no exclusion of those points is supplied.
It also does not turn surjectivity into properness, injectivity, or a solution of JC2.
This is a direct consequence of the existing global identity, not an independent inequality or a new geometric premise.

Screening. Two frozen-history corpora were searched; selected previews have not established an exact collision or novelty.
A bounded arXiv discovery search returned no source admitted for this implication; no external theorem is used here.
Review target: audit the sum over normalized target branches, repeated image components, local fibre-length decomposition, and exact surjectivity scope; identify prior exact evidence before publication.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3030`.
- Body SHA-256:
  `a8449483308d489db1430e0f532b1dac7d3d90fff9ad6b80ab07dcc46e4d0c35`.
- Frozen basis: `cb1b0c16f6b0c350a71dabbe60ae81c14d9d7d7d`.
