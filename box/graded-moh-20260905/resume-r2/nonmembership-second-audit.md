Independent second audit of all four N=1 obstructions

All four exact-Q nonmembership claims pass a second computation from the FULL direct coefficient files. The independent driver audit_nonmembership.py records hashes, total ring maps, generator counts, and checks in nonmembership-second-audit.json. It uses exact Fraction arithmetic and no Gröbner solver. The retained direct source hashes match math-audit.json and the instrument custody.

For the 111 and 136 fibres let R be the original full parameter ring and B its first grading, with B(c)=3. Let S be the polynomial ring in the declared retained positive-B coordinates and c, in the declared receiver order. Extend the receiver's projection to a TOTAL homomorphism phi:R→S by sending every retained coordinate to itself and every other coordinate to zero. This includes the zero-charge coordinates, coordinates of charge>3, and the two unused positive coordinates omitted from the 136 receiver. The extension fixes c and preserves both gradings, since every eliminated coordinate maps to zero.

Let G be the saved rational basis and M the monomial ideal of all monomials of B-degree>3. Define the finite-dimensional witness algebra A=S/(G+M). The second audit reads every full source row and verifies its original bidegree term by term. Rows with B≤3 project to polynomials that divide to zero by G; rows with B>3 project into M. Thus every full coefficient generator maps to zero in A, yielding a homomorphism R/I→A.

The audit verifies homogeneity of every basis element and exact reduction to zero of every S-pair whose leading-monomial lcm has B-degree≤3. The bounded Buchberger criterion therefore gives a standard basis through degree3. The overflow ideal has no component in degree3, and every critical pair involving an overflow generator has degree>3. In consequence the computed normal form c is nonzero in A. Since the image of c under R/I→A is nonzero, c is NOT in the full ideal I. No reverse basis-containment assertion G⊆phi(I) is needed: it is enough that the full source ideal vanishes in this larger quotient and c survives.

| Fibre | All source rows/terms | B≤3 rows/nonzero images | Basis elements | Required exact S-pairs | NF(c) |
|---|---|---|---:|---:|---|
| 111 | 167 / 74,878 | 78 / 67 | 60 | 466 | c |
| 136 | 348 / 371,224 | 87 / 76 | 68 | 574 | c |

The 77 and 129 fibres use a different total map, also preserving BOTH gradings: every B=0 coordinate z maps to t^w(z), every retained positive-B coordinate maps to itself, and every omitted positive-B coordinate maps to zero. The new variable has degree (0,1). The second audit independently expands the full source rows under this map, checks each resulting bidegree, and verifies both gradings of every saved basis element. No finite value is assigned to t.

Use the positive single grading H=w+LB, with L=40 for the 77 fibre and L=42 for the 129 fibre. The exact target degrees are respectively H(c)=39+40·2=119 and H(c)=41+42·2=125. These cutoffs include the target; a smaller cutoff would not decide this target by the stated bounded-basis criterion. Because L=D+1, every omitted row of B≥3 has H-degree≥3L+1>2L+D. The actual smallest omitted-row degrees are 123 (77 fibre) and 139 (129 fibre), both strictly above their target cutoffs. Hence ALL omitted full source generators vanish in the corresponding overflow quotient M_(H>119) or M_(H>125), and no omitted full row can affect the target.

| Fibre | All source rows/terms | B≤2 rows/nonzero images | Basis elements | Required exact S-pairs | NF(c) |
|---|---|---|---:|---:|---|
| 77 | 150 / 33,030 | 77 / 77 | 382 | 775 | c |
| 129 | 177 / 239,501 | 70 / 70 | 67 | 256 | 21 terms, nonzero |

The same witness-algebra proof applies with the declared positive H-degree replacing B-degree. All full generators vanish, while c has the independently verified nonzero normal form. The 129 normal form need not equal c for the argument: it is nonzero, of target bidegree (2,41), and agrees exactly with the saved rational expression. The c² image vanishes in both witness algebras by the degree overflow, at H-degrees238 and250. Thus all four N=1 failures are certified, while possible N≥2 membership remains open.

For all four fibres, an input basis row plus c has the same nonzero normal form as c, while 1 remains nonzero; every stored c normal form agrees exactly. These controls accompany the complete checks rather than replacing them.

These are ideal-NONmembership certificates only. In each explicit witness algebra c²=0 automatically by its positive-degree overflow. They therefore provide no point with c≠0, no radical-nonmembership conclusion, and no failure of a possible higher-power certificate in the original ring. They do not kill any Moh class. Their use of specialization is valid in the negative direction: membership in the original ideal would persist under every ring map, so a single nonzero quotient image disproves that membership. A UNIT after an arbitrary specialization would have the opposite logical direction and would not kill the full chart.
