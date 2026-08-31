# Hostile Review: Dicritical Typing Packet (D1)--(D4)

## Inputs And Hash Check

I first rehashed the two frozen inputs named in the charge:

```text
eeb4670511f35b7c52f03fa03d334eadff9eb3b7f3b6e18011beb7de4e73c54b  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.x8eTmL/inputs/block-descent-a1-rank4-dicritical-typing-d1-d4-grok46-20260831.md
ed0d288bec800bc1cfb59506a60ac76243aa47378692330f54f9d0860d754fb9  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.x8eTmL/inputs/block-descent-a1-rank4-reducible-component-tree-ledger-hostile-review-sol56-20260831.md
```

Both match. Stop condition not triggered. I did not inspect `jc2-lean`, did not run CAS/Singular/msolve, and edited no charged or canonical file. This report is the only workspace file written.

## Primary Sources Refetched

Fresh source record:

| source | URL(s) checked | SHA-256 / limitation |
|---|---|---|
| Orevkov 1987 | `https://www.mathnet.ru/eng/im1571`; Math-Net English PDF link `...getFT.phtml?...what=fullteng`; Geodesic page `https://geodesic.mathdoc.fr/item/IM2_1987_29_3_a4/` | Math-Net and Geodesic confirm Math. USSR-Izv. 29 (1987), 587--596, DOI `10.1070/IM1987v029n03ABEH000984`. Direct shell PDF hashing failed: author mirror gave 504; Math-Net PDF blocked/throttled. Browser-extracted Math-Net PDF text was used, cross-checked against cached `refs/jc86.pdf` hash `f80d4a7d7e04987ce7dece58f33cff20ea9210183ca3ffd4488f39a2147532db`. Fresh PDF byte-hash completeness is therefore `GAP`, not silently cured. |
| Chau 1999 | EUDML `https://eudml.org/doc/262821`; PDF `http://matwbn.icm.edu.pl/ksiazki/apm/apm71/apm7135.pdf` | EUDML page hash `22948fc66a3b4ec41b5adaf8b6acc0ca4e69e7a69a202dd43d8a45043b66bec4`; fresh PDF hash `febddbecb4c54d354fefca1a7e7730fcc18c0e2807fe3e03b5af8017b1d59d39`. The local cached PDF has different bytes but same extracted article. |
| Chau 2004 | arXiv `https://arxiv.org/abs/math/0305088`; PDF `https://arxiv.org/pdf/math/0305088`; e-print `https://arxiv.org/e-print/math/0305088`; EUDML `https://eudml.org/doc/281080` | PDF hash `8e70c57a798c14688c724334e0a004cf666e22faec1f31eb77141f8f3a1ce28f`; e-print hash `c35bdf31aac73c0f5f08cc947490586e3308e1827158734e7dd7f064727fc40d`; EUDML page hash `79a2aa0b36956732679ef8626bd819d3d6160a30301b93f600a37d623757eef7`. Official IMPAN PDF URL was visible but shell download did not complete. |
| Chau 2011 | arXiv `https://arxiv.org/abs/0905.3939`; PDF `https://arxiv.org/pdf/0905.3939`; HTML `https://arxiv.org/html/0905.3939v3`; IMPAN volume/article pages | arXiv PDF hash `c7eee42dfb8cc18b07598748457763d5cf54fdbcb7b574bbf295d26fafed079c`; e-print hash `98f4444db5280b8454bf5291d4786b9b19338b1cfb1a9b24bbb4c7d30d4fcb91`; HTML hash `7c6a2790e4820578e32250e22d761ca316af799e04295659944cf8a751b9acd5`; arXiv abs hash `02759c06f559e4813183a4339b22c3a6887f11d7ed23ca0cbee262aa9d2346b4`. IMPAN page confirms Ann. Polon. Math. 101 (2011), 47--53, DOI `10.4064/ap101-1-5`; shell access to its PDF returned 502. |

## Bibliographic And Quote Audit

Bibliographic identification is `CONFIRMED` for Orevkov 1987, Chau 1999, Chau 2004, and Chau 2011. The only bibliographic caveat is not identity but byte acquisition: the Orevkov and IMPAN 2011 PDFs were readable through browser extraction/indexing but not hashable through direct shell streams during this review.

Strict verbatim-quote audit is `REFUTED` as a property of the Grok packet. The cited statements exist with the needed hypotheses, but the block quotes are normalized mathematical transcriptions, not byte-for-byte source text. Examples: Orevkov's author/cache extraction uses `Xe`, `Ce2`, `LF C`, `neighbourhood`, and printed TeX symbols; the packet rewrites these as Markdown code, Unicode subscripts/superscripts, and cleaned notation. Chau 1999 Theorem 4.4's E2 is rendered as "image germ", while the source says the singular point is on `(P_phi,Q_phi)(D)` for every neighbourhood of zero. Chau 1999 Remark 4.9 is partly paraphrased inside a quoted block, including the bracketed explanation of formula (4.10). Chau 2004's proof quote also normalizes grammar and notation and uses ellipses.

Content audit:

| packet block | source location checked | verdict |
|---|---|---|
| Orevkov boundary definitions and Lemma 2.1 | cached extraction lines 64--96; Math-Net PDF browser text agrees on bibliographic source | `CONFIRMED` content; strict quote `REFUTED` for byte exactness. |
| Orevkov multiplicity, Lemma 4.2, Corollary 4.3 | cached extraction lines 281--371; Math-Net PDF browser extraction independently exposed the same paper | `CONFIRMED` content, including the exact Lemma number and the outer sum over `L_F`; strict quote normalized. |
| Chau 1999 Definition 3.4, function-level correspondence, Theorem 4.4, Remark 4.9 | fresh PDF extraction lines 414--419, 220--229, 798--821, 978--999 | `CONFIRMED` content. The correspondence is for a single polynomial `g`; Remark 4.9 claims a rewrite but does not prove a numbered bijection. |
| Chau 2004 dicritical series, Lemma 1, Phi-chart proof, Corollary 2 | fresh arXiv PDF extraction lines 99--165 and 76--82 | `CONFIRMED` content. Lemma 1 is series-level, not line-level. |
| Chau 2011 dicritical components and union formula | fresh arXiv PDF extraction lines 91--202; IMPAN article page confirms publication | `CONFIRMED` content. Hypothesis is finite fibres. |

## D1 Irreducibility And Dicritical Typing

Verdict: `CONFIRMED`, with a correction to the packet's quote status.

The source generations use different objects:

| source | object |
|---|---|
| Orevkov 1987 | `L_F`: irreducible components of the finite-value boundary on which the regularized map is nonconstant. Orevkov does not use the word dicritical. |
| Chau 1999 | `pi`-series for the map, plus a separate function-level correspondence between `Pi_g` and horizontal components for one polynomial `g`. |
| Chau 2004 | dicritical series `phi(x,xi)` satisfying `deg f_phi > 0`; Lemma 1 covers `A_f` by their polynomial images. |
| Chau 2011 | dicritical component: an irreducible component of `D_infty` on which `(p_l,q_l)` is nonconstant. |

For Orevkov, Lemma 2.1 says a component `K` of `L_FC` meets `L_infty` at one point and that its nonconstant endpoint is in `L_F`; away from that point the image lies in affine `C2`. Thus for `ell subset L_F`,

```text
alpha(ell) = closure_C2 f(ell minus infinity point)
```

is the closure of the image of an irreducible curve under a nonconstant regular map. The image closure is irreducible and one-dimensional. Therefore one Orevkov line cannot realize two distinct irreducible components of `A_F`. This is a desk-scale irreducibility argument, not a direct Chau 2004 Lemma 1 statement.

## D2 Surjectivity

Verdict: `CONFIRMED`, with scope.

Line-level surjectivity is supplied by Chau 2011. Under finite fibres, `A_F` is the union of affine images of dicritical components. A Keller map has finite fibres: a positive-dimensional fibre would force both coordinate functions to be constant along a curve, contradicting nonzero Jacobian at a smooth point of that curve. Since `A_F` is a finite union of irreducible curves and each dicritical-component image has irreducible closure, every irreducible component of `A_F` is the image closure of at least one line.

Series-level surjectivity is supplied by Chau 2004 Lemma 1. Its proof has both directions: a dicritical series gives a nonconstant polynomial image in `A_f`, and every irreducible component of `A_f` gives a unique such series in the construction.

The series-to-line bridge through `Phi` is `CONFIRMED` only as an existence derivation. In the chart

```text
Phi(t,xi) = (t^(-m), phi(t^(-m),xi)),
```

the divisor `t=0` is a source-infinity divisor and `f o Phi` is regular and nonconstant along it when `deg f_phi > 0`. After resolving to Orevkov's regular compactification, the nonconstant strict transform component is in `L_F` and has the same affine image closure. This closes the surjectivity needed for `#Irr(A_F) <= #L_F`.

What is not confirmed is a numbered bijection `Pi_f <-> L_F` in Orevkov 1987, Chau 1999, or Chau 2004, or any termwise transfer of correction terms. Chau 1999's explicit one-to-one correspondence is for a single polynomial function `g`, not the two-coordinate map `F`.

## D3 Positivity

Verdict: `CONFIRMED`.

Orevkov defines `mu_x` as a local multiplicity of the map at a point of the domain, then defines `mu_l f*` as the generic value of `mu_x f*` along `pi(l)`. For any domain point, `k=1` works in the definition, even if distinctness of the listed points is read implicitly. Hence `mu_x f* >= 1`, and therefore `mu_l f* >= 1` for every `ell subset L_F`.

The packet is right that this positivity is not derived from `deg f_phi > 0`. `deg f_phi` is the degree of a polynomial parametrization of a target curve. `mu_l f*` is Orevkov's generic local multiplicity of the surface map at the source boundary component. The earlier ledger's deduction `deg f_phi > 0` implies `mu_l >= 1` is a false identification of different quantities. The conclusion survives only because Orevkov's multiplicity itself is positive on the domain of `f*`.

Chau 1999 also speaks of a natural number `mu_phi` for generic local degrees of `F_phi`, but that supports a chart-level positivity statement, not the ledger's direct replacement of target parametrization degree by Orevkov line multiplicity.

## D4 Identity And Corrections

Verdict: `CONFIRMED`.

Orevkov's actual numbered statement is Lemma 4.2. In the notation of this review it is

```text
sum_{ell subset L_F} (mu_ell f* +
  sum_{x in pi(ell)-{infty}} (mu_x f* - mu_ell f*)) = N - 1.
```

The source immediately says only finitely many inner summands are nonzero, and semicontinuity makes each inner summand nonnegative. Corollary 4.3 is the displayed inequality

```text
sum_{ell subset L_F} mu_ell f* <= N - 1.
```

The outer sum ranges exactly over irreducible components of `L_F`. Constant finite-value components `L_C` and target-infinity components `L_infty` are not in this sum; `L_C` is contracted in the construction of `f*`.

## Mu-Zero Attack Closure And Typed Bound

Verdict: `CONFIRMED`.

The hostile `mu_l = 0` attack is closed by Orevkov's definition of multiplicity, not by Chau's `deg f_phi > 0`. A realizing line is a component of the domain of `f*`; its generic multiplicity cannot be zero because every point has local multiplicity at least one.

The resulting typed theorem is:

```text
#Irr(A_F) <= #L_F <= sum_{ell subset L_F} mu_ell f* <= N - 1.
```

The first inequality is Chau 2011 line-level covering plus irreducibility of images. The second is D3. The third is Orevkov Corollary 4.3. For `N=4`, this gives `#Irr(A_F) <= 3`, hence any reduced branch subcurve `B subset A_F` has `m <= 3`.

## Companion-Floor Sourcing

Verdict: `CONFIRMED` as a consumed promoted campaign interface, not an Orevkov/Chau fact.

The packet's Section 6 points to the right promoted rank-four sources. The producer `xmodel/block-descent-a1-quartic-branch-topology-acyclic-obstruction-sol56-20260830.md` has hash `768cf08fe2be7a72e9e17cd15acd56976b6743cefa293bf11472a4fb4e701805` and states the four rank-four partitions with

```text
T211: u=2;  T31: u=1;  S22,S4: finite loci.
```

The coordinator integration `xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md` has hash `5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de`; its Section 6 states that the generic numbers of unramified sheets on the irreducible branch components are `u_j=2` or `1`. Current `AUDIT.md` promotes the rank-four branch-cycle theorem and also records the conditional use of `f(B_i)>=1` in the reducible ledger review.

Thus the floor

```text
f(B_i) := #(pi^{-1}(z) cap U) >= 1
```

for generic `z in B_i` is genuinely promoted where the packet says it is. It should remain explicit in Lemma 2.3 consumers; it is a floor, not an attainment statement.

## Weakest Hypotheses, Corrections, Blast Radius

Weakest hypotheses for the confirmed typed bound:

```text
F:C2 -> C2 is Keller, with geometric degree N;
Orevkov's regularization/collapse f* is formed;
L_F is the nonconstant finite-value boundary;
A_F is the nonproper-value curve;
alpha(ell) is the affine image closure of ell subset L_F;
Chau 2011 finite-fibre component covering applies.
```

For the rank-four reducible application add the promoted block input `B subset A_F` componentwise and the companion floor `f(B_i)>=1`. For Lemma 2.3 also add its separate missing multiplicity identity `(2.3)`, which this lane does not prove.

Corrections:

1. Replace every citation `deg f_phi > 0 => mu_l >= 1` by the Orevkov domain-multiplicity argument.
2. Replace the silent "dicritical series = Orevkov line" step by either Chau 2011's component covering or an explicit Phi-chart existence derivation.
3. Do not promote the Grok packet as a byte-exact quotation packet. Its mathematical transcriptions are mostly correct, but strict verbatim status is refuted.
4. Do not use Chau 1999 Remark 4.9 to transfer individual correction terms from lines to series without an added theorem.

Blast radius: Lemma 2.2's conclusion `m<=3` survives after the citation repair. The written proof in the reducible ledger remains defective as written. Any successor needing termwise `mu_phi = mu_l` or a series-indexed correction identity remains open. Lemma 2.3 remains conditional on `(2.3)` plus the explicit companion floor.

## Best Next Falsification Test

Force a local proof, or find a counterexample, for the strongest remaining series-to-line use: start with a Chau 2004 dicritical series, resolve the Phi-chart divisor `t=0` into Orevkov's compactification, and verify whether the nonconstant `L_F` component carrying the same affine image also carries the claimed individual multiplicity/correction term. A failure would not break Chau 2011 surjectivity, but it would kill any future termwise series-indexed Orevkov budget.

## Per-Claim Verdicts

| claim | verdict | attack shown |
|---|---|---|
| frozen input integrity | `CONFIRMED` | Both charged SHA-256 hashes reproduced exactly. |
| complete fresh source byte hashes | `GAP` | Chau 1999/2004/2011 arXiv or PDF hashes were obtained; Orevkov PDF and IMPAN 2011 PDF direct byte hashing failed under 504/403/502/throttling. |
| bibliographic IDs | `CONFIRMED` | Math-Net/Geodesic/EUDML/arXiv/IMPAN pages identify the cited papers, years, pages, and DOIs. |
| packet's verbatim quote claim | `REFUTED` | Block quotes are normalized and sometimes paraphrastic; they do not occur byte-for-byte as written. |
| D1 image irreducibility | `CONFIRMED` | Orevkov `L_F` gives a nonconstant map from one irreducible boundary curve; image closure is one irreducible curve. |
| dicritical line versus series separation | `CONFIRMED` | Orevkov/Chau 2011 are line/component sources; Chau 1999/2004 are series sources; the packet mostly states this correctly. |
| D2 line-level surjectivity | `CONFIRMED` | Chau 2011 gives the component union under finite fibres. |
| D2 series-level surjectivity | `CONFIRMED` | Chau 2004 Lemma 1 gives the series union and converse construction. |
| D2 Phi series-to-line bridge | `CONFIRMED` for existence, `GAP` for termwise budgets | The chart gives a nonconstant source-infinity divisor after resolution; no source proves a full numbered bijection or correction-term identity. |
| D3 `mu_l>=1` | `CONFIRMED` | It follows from Orevkov multiplicity at domain points. |
| ledger's old `deg f_phi` to `mu_l` deduction | `REFUTED` | Target parametrization degree and Orevkov surface multiplicity are different typed quantities. |
| D4 identity and nonnegative corrections | `CONFIRMED` | Orevkov Lemma 4.2, the semicontinuity sentence, and Corollary 4.3 give exactly the needed identity/inequality over `L_F`. |
| `mu_l=0` realizing-line attack | `CONFIRMED` closed | A realizing line is in the domain of `f*`; generic multiplicity cannot vanish. |
| `#Irr(A_F) <= N-1` | `CONFIRMED` | Combine D1, D2 line covering, D3, and D4. |
| rank-four `m<=3` for branch subcurves | `CONFIRMED` conditional on `B subset A_F` | Since `N=4`, `#Irr(A_F)<=3`; any reduced subcurve has no more components. |
| companion floor `f(B_i)>=1` | `CONFIRMED` | Promoted rank-four packet and integration state generic unramified sheets `u_j=2` or `1`; `AUDIT.md` records the conditional consumer. |
| Lemma 2.3 missing identity `(2.3)` | `GAP` | Not part of this lane and still unproved here. |

<!-- BODY-END -->
