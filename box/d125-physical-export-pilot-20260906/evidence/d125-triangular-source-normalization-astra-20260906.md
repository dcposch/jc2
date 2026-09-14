# Degree-125 triangular normalization preserves the exact source chart

2026-09-06. Producer `/root/nonemptiness_certificate`; bounded child of the root-suggested normalization and the two frozen inputs below. **PROVISIONAL COMPOSITION, pending independent gates.** This is a field-point/nonemptiness theorem, not a scheme isomorphism, nilpotent coefficient-support theorem, source witness, solver result, or global degree-125 coverage theorem. No AWS, full source/ideal build, solver, or live gate body/log read.

## Result and exact dependencies

The proposed normalization survives the source-preservation check. Every characteristic-zero **field point of the complete guarded source ideal** can be changed by

`u -> u-s*v-r`, `v -> v`

to another point of the **same** original source chart with

`deg_u P<=15`, `deg_v P<=60`, `[v^60]P=alpha*u^15`,

`deg_u Q<=25`, `deg_v Q<=100`, `[v^100]Q=beta*u^25`.

The two degree guards, all terminal jets, all five fixed terminal coefficients, and the entire Jacobian equation are preserved. Both parameters lie in the original field, with no new localization. Consequently the original full ideal is proper exactly when the full normalized-subchart ideal is proper. The conclusion is conditional on the exact source contract and the polynomial Euler theorem retained below; no outcome of a live gate is assumed.

Frozen inputs:

- `xmodel/d125-client-interface-astra-20260906.md`, SHA `0c5270a432a6336c17c4693034e36cb496f139c3267843e3ac06628ec8c4b255`.
- Whole `xmodel/d108-upper-envelope-euler-astra-20260906.md`, SHA `08d3fa09506b412dcbddeabb24d70da0f266b90174615cf39013a4311ecabd75`; only its general polynomial Euler envelope/top-face lemmas are used, not its D108 case composition.
- Primary GGV, [On the shape of possible counterexamples to the Jacobian Conjecture, arXiv:1401.1784v3](https://arxiv.org/pdf/1401.1784v3), Theorem 2.6, polynomial clause (1), and endpoint clause (2). Local text `box/census-coverage-20260905/core-ggv-layout.txt`, SHA `e3694dde3f83c2ab6ed8d957fc6b53472e6a6dd55486af1dff345eade39e37b1`. Read the introduction and Sections 1–2 through the entire theorem/proof, including the direction and endpoint conventions. The existence theorem and its cited upstream lemma are retained at EXTERNAL-THEOREM trust, not re-proved. It is stated over an arbitrary characteristic-zero field; algebraic closure is introduced only later in the paper. No minimality assumption occurs here.

## 1. Literal source assumptions

Let K be a characteristic-zero field and let P,Q be a field point of the complete guarded contract. Thus

`P,Q in K[u,v]`, `J(P,Q)=P_u Q_v-P_v Q_u=1/5`,

`Supp(P) subset {i,j>=0: i+j<=75, 5i-j<=15}`,

`Supp(Q) subset {i,j>=0: i+j<=125, 5i-j<=25}`,

with `alpha=[u^15 v^60]P !=0`, `beta=[u^25 v^100]Q !=0` and retained inverse `Z alpha beta=1`.

Under the fixed source embedding

`Phi(u)=X^5`, `Phi(v)=Y+X^(-1)`,

the entire terminal halfspaces are `v_(5,-17)(Phi(P))<=3` and `v_(5,-17)(Phi(Q))<=5`. The fixed coefficients are

| Side | Monomial in X,Y | Fixed coefficient | Terminal weight |
|---|---|---:|---:|
| P | `X^4 Y` | 1 | 3 |
| P | `X^21 Y^6` | 1 | 3 |
| Q | `X` | -1 | 5 |
| Q | `X^18 Y^5` | -3 | 5 |
| Q | `X^35 Y^10` | -9/5 | 5 |

These are the original source constraints, not a free Laurent support box. All polynomial Jacobian coefficients and the inverse row remain present throughout.

The source bounds alone already imply `deg_u P<=15` and `deg_u Q<=25`: adding the total and weight inequalities gives `6i<=90` or `150`. Moreover the only permitted source monomials at i=15 or 25 are respectively `u^15 v^60` and `u^25 v^100`. What is **not** initially true is the vertical rectangle bound or a unique total leading monomial: for example `v^75` remains permitted in P.

## 2. First normalization: the homogeneous total tops

The total degree-75 part is `P_75=v^60 f_15(u,v)`, where f is homogeneous of degree 15 and `[u^15]f=alpha`. The exact v-order is60. At direction `(1,1)`, GGV Theorem 2.6 supplies a homogeneous polynomial

`E=A*u^2+B*u*v+C*v^2`, with `[E,P_75]=P_75`.

The coefficient of `u^16 v^59` on the left is `120 A alpha`, while the right has v-order 60. Hence A=0. Next the `u^15 v^60` coefficient gives `45 B alpha=alpha`, so

`B=1/45`, `s=C/B`, `E=(u+s*v)*v/45`.

These divisions are legitimate because K has characteristic zero and alpha is nonzero. In coordinates `U=u+s*v`, v, the Euler bracket acts on `U^k v^(75-k)` by the scalar `(75-2k)/45`. Its eigenvalue is 1 only for k=15. Therefore

`P_75=alpha*(u+s*v)^15*v^60`.

The highest total part of the Keller bracket vanishes: `[P_75,Q_125]=0`. Expand Q_125 in U,v. The coefficient contributed by `c_k U^k v^(125-k)` is

`75*(25-k)*alpha*c_k * U^(k+14) v^(184-k)`.

Distinct k give distinct monomials, so every coefficient except k=25 vanishes. The top guard fixes the remaining coefficient:

`Q_125=beta*(u+s*v)^25*v^100`.

Thus the **same** shear parameter works for both components. The automorphism `tau_s(u)=u-s*v`, `tau_s(v)=v` has Jacobian 1 and makes the two total leaders the single monomials `alpha*u^15*v^60` and `beta*u^25*v^100`. The minus sign is required.

No root extraction is concealed here:

`s=[u^14 v^61]P/(15 alpha)=[u^24 v^101]Q/(25 beta)`.

## 3. Euler envelope and the second normalization

For clarity, the general Euler-envelope reasoning was independently checked. If a polynomial Keller component has unique total leader `c u^a v^b`, a,b>0, and a support point has v-exponent above b, maximize `(j-b)/(a-i)`. This produces an exposed nonmonomial face with start `(a,b)` and primitive normal `0<rho<sigma`. A polynomial Euler element of weight rho+sigma has support only at `(1,1)` and possibly `(1+sigma/rho,0)`. If monomial, GGV Remark 2.5 forces the leading face to be monomial, a contradiction. If not, its start is the latter point, which is not parallel to `(a,b)` and is not `(1,1)`, contrary to Theorem 2.6(2). Thus `deg_v=b`; swapping variables gives `deg_u=a`. This uses the primary counterclockwise start convention, not the opposite endpoint.

Apply this lemma after tau_s. We obtain the rectangles 15 by 60 and25 by 100. Write the vertical tops as `p(u)v^60` and `q(u)v^100`, with degrees 15 and 25 and leading coefficients alpha and beta.

At `(0,1)`, Theorem 2.6 is applicable because `rho+sigma=1>0` and the component has positive vertical degree. Its polynomial Euler element is `e(u)v`, giving

`60 e' p-e p'=p`.

If `deg e=d>=2`, the highest coefficient on the left has degree `15+d-1` and nonzero multiplier `60d-15`, impossible. A constant e also cannot work. Thus `e=(u+r)/45`, and the identity becomes `(u+r)p'=15p`. Consequently

`p=alpha*(u+r)^15`.

The v-weight 159 part of the common bracket vanishes, giving `100 p' q-60 p q'=0`. Canceling a nonzero power of u+r gives `(u+r)q'=25q`, so

`q=beta*(u+r)^25`.

The second automorphism `tau_r(u)=u-r`, `tau_r(v)=v` makes both vertical tops pure. It preserves the rectangles and the already normalized total leaders. Both transformations commute.

The parameter is in K and uses no new inverse:

`r=[u^14 v^60](tau_s P)/(15 alpha)=[u^14 v^60]P/(15 alpha)`.

The last equality is literal: the only additional source monomial that could contribute under tau_s is `u^15 v^59`, and it is forbidden by `5i-j<=15`. Similarly `r=[u^24 v^100]Q/(25 beta)`. In public variable names,

`alpha=P_15_15`, `beta=Q_25_25`, `s=P_9_14/(15 alpha)`, `r=P_10_14/(15 alpha)`.

Since `alpha^(-1)=Z beta` and `beta^(-1)=Z alpha`, the existing guard already controls these denominators. No alpha=0 or beta=0 stratum is discarded beyond the original explicitly guarded chart.

## 4. The load-bearing check: preservation of the entire chart

For fixed s,r in K, source substitution by either shift preserves polynomiality and the total-degree bounds. Each replacement of u by v lowers ordinary `(5,-1)` weight by 6, while replacement by a constant lowers it by 5. Hence the full original weight bounds and their entire top faces are unchanged. In particular alpha, beta and Z may be kept unchanged.

It remains to check the **translated terminal** bounds and all five pins. The lift of the source derivation `partial_u` is

`D=(X^(-4)*partial_X+X^(-6)*partial_Y)/5`.

Indeed, `D Phi(u)=1` and `D Phi(v)=0`. Thus `D Phi(R)=Phi(partial_u R)` for every source polynomial R. Likewise `Phi(v)D` conjugates `v partial_u`. These are locally nilpotent **on the polynomial-source image**, not on the whole Laurent ring: D repeatedly applied to X need not vanish. This distinction is essential.

With terminal weight `(5,-17)`, the two terms of D lower weight by 25 and 13. Multiplication by `Phi(v)=Y+X^(-1)` gives four terms lowering weight by 42, 30, 30, 18. All drops are strictly positive. Therefore on any polynomial-source image,

`Phi(tau_s R)=exp(-s Phi(v)D) Phi(R)`,

`Phi(tau_r R)=exp(-r D) Phi(R)`.

These exponentials are **finite sums**, because they are conjugates of source-polynomial shifts; no formal infinite lift or growing support is assumed. Every nonidentity term has strictly smaller terminal weight than its input. Accordingly the complete terminal leading faces of weights 3 and 5 remain literally unchanged. Since every pin in the table lies on exactly that face, all five fixed coefficients are preserved, as are all forbidden-above-face coefficients, equivalently every source binomial-jet relation.

Finally both source shifts have Jacobian 1, so `J(P,Q)=1/5` is preserved. The fixed Phi then gives the same `X^4` target automatically. This proves preservation of simultaneous satisfaction of **every** row of the complete source contract, not just the listed linear equations. It does not assert preservation of additional optional carrier/root/pivot gauges absent from that contract.

## 5. Precisely what the reduction licenses

Let I be the complete guarded original-source ideal. Let I_norm be obtained by retaining every generator of I and imposing the additional source coefficient zeros

`[u^i v^j]P=0` for j>60; `[u^i v^j]Q=0` for j>100;

`[u^i v^60]P=0` for i<15; `[u^i v^100]Q=0` for i<25.

No new inverse variable is needed. For each characteristic-zero field K, every I-point has the explicit same-field normalized I_norm-point constructed above, with alpha, beta and Z unchanged. Conversely every I_norm-point is an I-point. Hence geometric nonemptiness is equivalent. In particular, by weak Nullstellensatz over Qbar,

`I is proper over Q  <=>  I_norm is proper over Q`.

This is **not** equality of I and I_norm in their common ambient ring, not equality of their point sets in fixed coordinates, and not a scheme isomorphism or a statement about nilpotent coefficient supports. The argument uses field specializations and a point-dependent normalization. It does not provide an original-generator unit certificate, a properness witness, or a runtime improvement.

The exact raw support counts are:

| Side | Original source | Rectangle plus original weight | Also pure vertical top |
|---|---:|---:|---:|
| P | 706 | 586 | 571 |
| Q | 1901 | 1576 | 1551 |

These are monomial-coordinate counts **before** terminal jet ranks and scalar pins, not affine dimensions. The pure-top column removes 15 and 25 further coefficients. The ordinary Jacobian's rectangular envelope is

`0<=I<=39`, `0<=J<=159`, `5I-J<=36`,

so the row-index upper bound is `sum_(I=0)^39(160-max(0,5I-36))=3792`, compared with the unnormalized bound 4572. The bound can include identically zero rows and is not an emitted row count. No terms, nodes, wall-time advantage, dense elimination, or solver behavior were measured.

## 6. Exact controls, read scope, and custody

Owned `box/d125-triangular-source-normalization-20260906/check.py` uses only standard-library Fraction arithmetic and finite polynomial dictionaries, under 30s/512MiB per process. It tests the actual exponents 15/60 and 25/100, Euler signs and constants, both normalization signs, a common versus mismatched Q-root, the lifted derivation, source-only nilpotence, terminal weight drops, and the raw support/index counts.

A small **non-Keller** fixture satisfies the actual linear source chart, all five pins and both degree guards. Direct substitution and complete terminal-face extraction verify preservation under a nonzero shear and translation, and inverse substitution recovers the original fixture. It is deliberately verified not to have constant Jacobian; it is not a source solution. Genuine wrong-Euler, u-squared Euler, wrong-shear-sign, mismatched-root and wrong-lift-sign mutations are rejected by the actual equality checks; the chart checker also rejects a zero-alpha boundary mutation. Checks use explicit exceptions rather than erasable assertions, and normal/optimized Python runs are retained separately.

The input manifest records the three frozen source hashes and exact control hashes. Both prior producer reports were read whole; the primary theorem and its surrounding preliminaries/proof were read directly. No live D108/D125/Euler gate body or log was consulted. All local writers finish before terminal handoff; root retains promotion decisions. **STOP:** no dependent trimming is implemented in any active source or builder, and no next computation is authorized by this packet.

Post-cutoff coordination notice: after this proof and its controls were written, root reported promotion of the underlying Euler lemma and exact D125 source contract/ideal equality, and completion of a separate 153-control normalization check. Those gate bodies and root control code were not read in producing this packet; the current normalization composition still requires its own independent review. No live 14:35 blind-round submission was read.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13711`.
- Body SHA-256:
  `0369c0bb2db2927b92523a66b0940e347727511bbd31333fd2203e1b98221cc7`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
