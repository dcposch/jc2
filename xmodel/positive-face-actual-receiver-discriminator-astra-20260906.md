# Positive-face discriminator on the actual Moh (25,15) receiver

2026-09-06. `/root/model_productivity`. **PROVISIONAL SOURCE COMPOSITION / FINITE NECESSARY RESIDUE SCREEN; NO RECEIVER EXCLUSION.** One actual-source client, no farm, solver or chart mutation. The newly reviewed positive-face Euler theorem restricts two previously free outer-face slope strata. Every resulting face still admits its required Euler element. This is not a polynomial receiver point or a new equation proved independent of the full Jacobian ideal.

## 1. Exact source-to-polynomial-pair hypotheses

The client is not an arbitrary pair bearing degrees 25 and 15. Start with the licensed Moh `(n,m)=(125,75)` parent having

`M=(-75,105,123), d=(125,25,5,1), (V2,V3)=(2,4)`.

Thus `u_s=d_s-v_s=1`. Moh Proposition 6.4 supplies the minor-radius hypothesis of Proposition 6.3. In the proposition's actual coordinates `(gamma,pi)`, its high component and transformed first characteristic polynomial give **both**

`P,Q in K[gamma,pi], deg_pi(P,Q)=(25,15), monic in pi,`

`[P,Q]_(gamma,pi)=c gamma^2, c=-1/b_source !=0`.

Here P is the high-degree component; some native chart files reverse P and Q and correspondingly negate c. Nothing below depends on that nonzero scalar. Work after extension to an algebraically closed characteristic-zero field K. Polynomiality, not merely a Laurent face, is supplied by Proposition 6.3(1). Its conclusion is a **pi-degree** statement, not a total-degree assertion.

The accepted effective child datum is `(25,15; M2'=21,V2'=2;k=2)`, `d2'=5`, with major radii `delta2'=-1`, `delta1'=7/5`. This is the charged descent accepted in `row2515-order-gate` §2, not a fresh claim to prove the entire characteristic-data transport. The gate rejects the later sparse order-basis chart as exhaustive; none of its coefficient restrictions or scalar shear is used here.

Primary anchors: Moh printed pp.197–199, Propositions 6.3–6.4; pp.170–171, Proposition 4.6 and its monomial-J extension; pp.173–175, Proposition 5.1 and the effective-last-entry convention; p.179 Definition 5.1(1)–(4), p.180 Proposition 5.3. These give polynomiality/Jacobian, the common outer disc, root counts and the selected major packet. The accepted top-face license §3 and its `(25,15)` row keep all three partitions of the remaining mass 3:

`H=pi^2 S(gamma,pi),  deg S=3,  P_top=H^5, Q_top=H^3`,

`S=(pi-gamma)^3`, or `(pi-gamma)^2(pi-a gamma)`, or

`S=(pi-gamma)(pi-a gamma)(pi-b gamma)`.

The one nonzero slope is normalized to 1 by the licensed coordinate/scalar changes preserving monicity and the form `c gamma^2`. In the second stratum `a!=0,1`; in the third `a,b!=0,1`, `a!=b`. Those distinctness conditions express the **actual factorization stratum**, not genericity imposed on all sources. No assertion is made that any stratum is attained by an actual parent.

## 2. Exhausting positive directions without the rejected D1-centering claim

The following explicit shared centering is a source-packet argument, not an inference from a D1 order inequality or from the old h-width cap.

Put `t=gamma^(-1)`. The common outer-disc radius is

`delta2'=-(k+1)/(25-21-1)=-1`.

Use the polynomial mean of the Q roots,

`eta(gamma)=-[pi^14]Q/15`,

and substitute `pi -> pi+eta(gamma)` in **both** components. The common-disc ultrametric argument places every translated P/Q root at order at least -1. This is the elementary outer-disc normalization proved in terminal `moh-hsupport-gate` §4. Monicity and elementary symmetric functions therefore give total degrees at most 25/15; they are exactly those degrees since the pi leaders remain. The substitution has determinant one and fixes gamma, so the same monomial-J equation is retained.

Next move the selected outer slope to zero by a shared linear shear in pi. The outer homogeneous forms are the H powers above. The **entire** zero-slope outer packet comprises 10 roots of P and 6 of Q, by `V2'=2` and the degree scalings 5 and 3. Proposition 5.3 shrinks that very packet to the common D1 disc of radius 7/5; it is not a selected proper subpacket with other zero-slope roots left outside. Consequently every pair of roots in this combined P/Q packet has contact at least 7/5.

The P zero-slope packet is Galois-stable over K((t)): it is exactly the set of P roots with `ord_t rho>-1`, equivalently outer slope zero. Its mean `eta0(t)` belongs to K((t)), rather than merely a fractional Puiseux field. Each of its roots has order greater than -1, so the mean also does; its integral Laurent exponents imply

`eta0(t)=b0+O(t), b0 in K`.

For **each P or Q root** rho in the common zero packet,

`rho-eta0 = (1/10) sum_(P zero roots rho_i) (rho-rho_i)`

has order at least 7/5. Hence the same constant b0 works for both components. The shared polynomial translation `pi -> pi+b0` puts all 10/6 selected roots at order at least 1. All remaining 15/9 roots still have order exactly -1, with the nonzero outer slopes. No full D1 center has been set equal to zero: the possible positive-t tail of eta0 is left untouched.

Each elementary symmetric product can contain at most 15 or 9 order-minus-one roots; all remaining factors have nonnegative order. Since each coefficient is polynomial in gamma, this proves

`deg_gamma P<=15, deg_gamma Q<=9`.

The product of all nonzero-slope roots forces the nonzero endpoints `(15,10)` and `(9,6)`; equivalently these coefficients are visible directly in H^5 and H^3. Together with the total-degree bounds, this exhausts every positive direction:

| Positive direction `(r,s)` | P face | Q face |
|---|---|---|
| `r<s` | `pi^25` | `pi^15` |
| `r=s` (primitive `(1,1)`) | `H^5` | `H^3` |
| `r>s` | nonzero multiple of `gamma^15 pi^10` | nonzero multiple of `gamma^9 pi^6` |

For example, `ri+sj <= sN+(r-s)i` on the total-degree bound; when r>s, `i<=15/9` gives equality only at the displayed endpoint. When r<s, equality is only at the pure-pi leader. Thus there is only one positive nonmonomial edge. In particular the advertised two-root weight `(1,3)` is monomial on this client. The mixed-sign direction associated with the inner radius 7/5 is outside the positive theorem and is not tested here.

## 3. The outer-face Euler equation gives an actual residue screen

The reviewed theorem applies to the **full** polynomial pair above, with k=2 and l=3. At `(1,1)` it supplies a polynomial homogeneous degree-four E satisfying

`[E,H^5]=gamma^2 H^5`, or `5[E,H]=gamma^2 H`.

The loose root bound is four nonzero roots. H already has only one to three, so **the count alone has no gain**. Retaining the actual Euler identity is stronger.

Write `z=pi/gamma`, `H=gamma^5 h(z)`, `E=gamma^4 e(z)`. Polynomiality gives `deg e<=4`, and direct differentiation gives

`5(4e h'-5e' h)=h`.                                      (E)

The pi^0 term of E would create a nonzero pi^9 term in `[E,H^5]`, while the right side has pi-order 10; hence `pi|E`, or `z|e`. Also every distinct nonzero root of h divides e: otherwise `4e h'` has order one less than h at that root and cannot cancel against `5e'h`. This is also the transported GGV Proposition 2.11(1) divisibility. Repeated roots of h are handled with their actual multiplicities, never counted as distinct roots.

**Partition [3].** With `h=z^2(z-1)^3`, (E) admits

`e=z(z-1)(-25z^2+35z-7)/105`.

There is no free normalized nonzero slope here and no obstruction.

**Partition [2,1].** Here `h=z^2(z-1)^2(z-a)`, `a!=0,1`. Divisibility and degree imply

`e=z(z-1)(z-a)(Az+B)`.

Equation (E) gives exactly

`5B+(3-a)A=0`, `-(2+6a)B-2aA=0`, `3aB=1/5`.

Thus `a=3` is impossible and elimination gives the necessary condition

`a^2-a-1=0`.

Conversely, **at Euler-face level**, either root of this quadratic admits

`e=z(z-1)(z-a)((3-a)-5z)/(15a(3-a))`.

The denominator is nonzero on the two roots; it does not discard an additional possible solution branch. The exact undivided identity is

`5(4N h'-5N' h)-15a(3-a)h = 30z(a^2-a-1)h`,

where `N=z(z-1)(z-a)((3-a)-5z)`.

**Partition [1,1,1].** Write the monic cubic as `s(z)=z^3+A z^2+B z+C`, with three distinct nonzero roots. Divisibility and degree force `e=lambda z s`, `lambda!=0`. Equation (E) reduces to

`5 lambda (A z^2+2B z+3C)=1`.

Therefore A=B=0. Since one slope is 1, C=-1. Equivalently

`S(gamma,pi)=pi^3-gamma^3`,

`1+a+b=0`, `a+b+ab=0`.

The remaining slopes are the two primitive cube roots, distinct and nonzero in characteristic zero. The compatible Euler element is `e=-z(z^3-1)/15`. This does **not** assert an actual arbitrary-three-root stratum existed before the screen, or that this specialized face extends to a polynomial pair.

For Q_top=H^3 the Euler element is `(5/3)E`, so it gives exactly the same slope conditions, not an additional equation. On the monomial positive faces, `E=gamma^3 pi/(3B-A)` works for a face `gamma^A pi^B`; the four denominators are 15,75,9,45, all nonzero. Every surviving positive-face alternative is therefore explicitly Euler-compatible. **No partition or source receiver is excluded.**

## 4. Gain, redundancy, and read perimeter

The concrete delta is a finite necessary slope restriction inside the source-safe `[2,1]` and `[1,1,1]` outer strata. The read top-face license and row2515 gate retain those slopes as free, subject only to noncollision factors; neither displays these two residue equations. This can be a useful preprocessing target after an independent gate of this source composition, but no chart or source generator was changed here.

There is **no claim of nonredundancy on the full necessary source ideal**. The theorem is a consequence of the full polynomial monomial-J equation; the equations vanish on the applicable characteristic-zero field points, and no ideal-membership or scheme statement is established. Moh Proposition 4.6 retains a stronger boundary differential equation beyond its root-count corollary. This task does not prove that the finite slope restrictions are absent from that primary system; rediscovery there is plausible. Root separately noted algebraic coincidences with F2 cubic data and the change `b=a+1`, which turns `a^2-a-1` into `b^2-3b+1`. That is not a coefficientwise Moh/F2 attachment or a source-identification theorem.

Read whole: the charged positive-face root composition and Fable gate; row2515-order gate. Read relevant source/support sections: top-face license §§1–5,7–8; Moh h-support gate §§1–4; terminal twopoint gate source/ring discussion. Primary Moh passages listed in §1 and GGV definitions, Theorem 2.6 with proof, Remark 2.8, Proposition 2.11(1)–(3) with proof were inspected in pinned local text. GGV's upstream existence lemma remains external, exactly as in the accepted gate.

Focused history searches checked these terminal Moh source reports and terminal Markdown matches for cubic/golden-ratio slope equations; no matching explicit row2515 screen was found. A preliminary filename-glob search also returned historical Moh log snippets; these were not used as mathematical evidence. No live 14:35 submission or live D125 full-stream/published-chain body, code, log or receipt was read. The unrelated F2 degree30/50 polygons and normalized D125 rectangles were not re-derived. No AWS, classifier, CAS, solver, negative-weight extension, K7 cut, shared-ledger edit or Lean access occurred.

Pinned full-file SHA-256:

- Euler composition `41a2efed83a6f928e8a2f9fe5c8e7d2e8aa5faf691212b31334177b0e9bccf7b`.
- Euler gate `3eb7a6e5e3a390646cd6e77ac95a0042f3015fb0dcfefbf446568d40af870e70`.
- Row2515 gate `f1766b7c59c03387447fa0b599d79ef05935a0a5c373ff17c8e4020592bd67fb`.
- Top-face license `53c13d48eebd135841150fc36e2cd6a378d33cfe182be811046d3233b0f355ae`.
- Moh h-support report `4437b1f2f8ed8058fc8900e3cdfcbbc67ec5f5c98eee9c0f04d78a0fb8370354`.
- `box/census-coverage-20260905/moh-layout.txt`: `f203d7892753011ac21e8f01d29d73f5d777cad36310d2c16aa49d4a335072a0`.
- `box/recvatlas-20260905/moh-p197-199.txt`: `241f7c96259dd78efac7bc0b62eda8d44c98acfa770893bd09336564b2ff2f46`.
- GGV `core-ggv-layout.txt`: `e3694dde3f83c2ab6ed8d957fc6b53472e6a6dd55486af1dff345eade39e37b1`.

The one small replay artifact is `box/positive-face-actual-receiver-20260906/check.py`, SHA `e85416c7d94c72e7c627264fbb22ef0dc0499ca56432f53342d9df72022dbe9b`. Standard-library rational polynomial arithmetic checks all three exact identities, wrong-sign and unforced-slope controls, both component scalings, all monomial endpoints and a genuine polynomial monomial-J control `(P,Q)=(gamma*pi,gamma^2)`. Normal and optimized runs each passed 15 checks in under 0.003 seconds under 30-wall/25-CPU/512MiB limits. These are algebra controls, not substitutes for the source-packet proof or an actual receiver witness.

All owned writers are terminal at publication. STOP: bank this source-specific residue screen for independent review; no solver or further client follows from it.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12896`.
- Body SHA-256:
  `b6cb34fe6cae11161ac27ddf905aca0009724332ee174407ef89e0c7e0174b0c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
