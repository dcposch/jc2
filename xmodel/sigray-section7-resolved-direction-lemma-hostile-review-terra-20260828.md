# Hostile review: Sigray Section 7 resolved-direction lemma

Date: 2026-08-28  
Reviewer: GPT-5.6-terra / Codex  
Verdict: **FAIL AS FILED; CONDITIONALLY REPAIRABLE.**

## Scope and custody

Reviewed producer file (hash verified):

```text
3e44aba9ae890028b5d64084a635df7060b87765635f2f5f47eb2f8728549ae9
  xmodel/sigray-section7-resolved-direction-lemma-producer-gpt5-20260828.md
```

Cross-checks used only the printed Section 7 (pp. 35--39) in
`refs/sigray_full.pdf`, the cited independent audit
`0159cdf18f9ad1c986677d4631916dbbef0b5310829958f6dac192eab2795a31`,
and its hostile review
`af1ce600bff775bacee122bea3cd5a098ef6a457616273d8a0147c16438a0afe`.
The corrected inputs permitted for the local part are EW1--EW4 as the
producer states them.  In particular, this review does not restore the
printed per-puncture `delta_a`, the printed boolean `a ->_i b`, or the
printed claim that a value curve is biholomorphic to `C`.

The producer correctly targets the cluster ledger rather than the false
per-puncture ledger.  Its failure is one of licensing, not an exhibited
geometric counterexample: the crucial global chart/descent theorem remains
an asserted enlargement of EW1--EW4, and the final Euler step silently uses
the separately repaired every-fibre Proposition 5.8.

## Clause ledger

| clause | verdict | hostile finding and minimal clean repair |
|---|---|---|
| Custody and avoidance of the literal Section 7 defect | **PASS** | The producer hash is exact.  It charges one baseline per direction cluster, counts parameter points rather than punctures, and does not use the printed `delta_a` inference. |
| Common graph resolution | **CONDITIONAL** | G1 is the standard characteristic-zero surface elimination theorem, provided `X_0` is a smooth projective compactification and the rational extension of `(f,g)` to `X_0 --> P^1 x P^1` is specified.  It should be cited in that form (or proved by the point-blowup algorithm).  G1 alone says nothing about Eggers--Wall flags or their coefficient lines. |
| Divisorial realization of every `F_i` on that same graph resolution | **CONDITIONAL** | G2 states this as an input but gives neither a citation nor the needed compatibility statement.  Ordinary realization of a rational rank-one surface valuation gives an exceptional divisor; it does not by itself identify the Eggers--Wall residual coefficient chart, its finite stabilizer, and the restriction of every residual polynomial after all graph-resolving blowups.  Add a precisely stated divisorial Eggers--Wall chart lemma (below), with its hypotheses and proof/citation. |
| `E_i=P^1`, and the direction domain is exactly `U_i=E_i\{infinity_i} ~= A^1` | **CONDITIONAL** | This is plausible after the chart lemma, but G2's phrase “supplies an affine chart” is too weak to prove that it is the whole strict transform minus exactly one point on the final common model.  The assertion that every finite collision/intersection point remains a direction is also not derived.  Prove that later point blowups restrict to an isomorphism on the strict transform of `E_i`, identify its coefficient chart with the complement of the one incoming point, and show that `f,g` are finite there.  The unnecessary sentence that an infinity branch has “a different zero-order flag” should be deleted; for the ledger it is enough to prove that no finite `f=a` direction is represented at that removed point. |
| Cyclic quotient `A^1_eta/mu_m = A^1_z` and no cyclic overcount | **CONDITIONAL** | The invariant-ring calculation is correct *after* one has an effective scalar cyclic action on the actual residual chart.  EW1--EW4 as stated do not establish the global stabilizer, its scalar action on the chosen chart, or its compatibility with `E_i`.  Add these as parts of the chart lemma.  Then `z=eta^m` and the single fixed orbit over zero give the claimed no-overcount. |
| Invariance and polynomial descent of `p_(f-a0,F_i)` and `p_(g,F_i)` | **CONDITIONAL** | The conclusion follows from a **zero-order cyclic residual descent lemma**, but that lemma is not among EW1--EW4 or G1--G3.  Section 4 assumes a deck expansion and then says that order zero kills the character.  This needs the precise assertion: on a tame residual cover the deck action sends `p_(h,F)(eta)` to `chi_h(zeta)p_(h,F)(eta)`; if `d_(h,F)=0`, then `chi_h=1`.  Apply it to `h=f-a0,g`, then use `C[eta]^{mu_m}=C[eta^m]`.  Without that lemma, (4.1)--(4.3), including the claim that the graph morphism has no finite-chart poles, is unproved. |
| `P_i` nonconstant and finite direction fibres | **PASS, once descent is supplied** | A realized root of the nonzero residual polynomial rules out a constant first coordinate.  A nonconstant complex polynomial is surjective with finite fibres.  The producer's monic-equation argument also correctly proves that `A^1 -> Spec C[P_i,Q_i]` is finite. |
| Twisted Statement 3.14 transport | **CONDITIONAL** | The producer correctly avoids literal named-`eta` equality and keeps the common twist.  But EW3 is a tree transport; it does not alone prove that the transported flag/direction is the same point of one fixed global `E_i`, nor that the quotient coordinate and both value functions transport together.  Those are additional conclusions of the missing chart lemma.  Once supplied, the common twist is harmless because it acts simultaneously on both descended functions. |
| Bijection `disjoint_union_i U_i(C)` to finite-value direction clusters | **CONDITIONAL** | Given the chart/descent lemma, the producer's proof is sound: EW1 gives the unique flag, EW2 gives the root-orbit cluster, and EW3 gives the unique reference family.  It rightly maps one parameter point to one cluster, not to one puncture.  Without the lemma, the key phrase “one residue point on `U_i`” is only asserted, so (5.3) has not been proved. |
| No cross-vertex or cyclic duplication | **CONDITIONAL** | Under the preceding bijection, the injectivity argument is correct: a common nonempty cluster has one EW1 flag, and an orbit has one quotient point.  It cannot independently prove either the common-model identification or the orbit quotient, so the producer's unqualified “proved” status is too strong. |
| Boundary collisions versus coefficient infinity | **CONDITIONAL** | Retaining finite collision points is the right Euler convention; deleting every boundary intersection would give the wrong characteristic.  The proof must nevertheless establish that these points are in the residual `A^1` chart on the *final* graph resolution and are assigned once.  This is not a consequence of merely saying “strict-transform identification after a blowup.” |
| Constructible multiplicity pushforward and Euler integral | **PASS, conditional on the constructed `phi_i`** | For `phi_i(z)=(P_i(z),Q_i(z))` with nonconstant `P_i`, the geometric fibre count `n_i` is constructible and Euler-Fubini gives `integral n_i dchi_c=chi_c(A^1)=1`.  This correctly tolerates ramification, self-intersection, and common image curves.  G3 should specify complex algebraic finite-type maps and compactly supported Euler characteristic; with those hypotheses it is exactly applicable. |
| Pointwise cluster deficit | **CONDITIONAL** | Grouping by the asserted bijection gives `d-N=B+E` with `E>=0` from EW4/Proposition 7.3.  This has no dependence on the disputed printed (22).  It additionally requires the every-fibre degree identity in the next row. |
| Use of the every-fibre fibre-divisor identity | **FAIL** | Equation (8.1) is not a consequence of Keller étaleness, EW1--EW4, or G1--G3.  It uses the repaired Proposition 5.8: on **every** normalized fibre `f=a`, the meromorphic degree of `g` is `td(f,g)`.  The independent audit explicitly records printed Proposition 5.8 as a source gap with a separately promoted replacement.  Cite that replacement by exact file/hash and state its polynomial-Keller/normalization hypotheses, or include it as an additional canonical input. |
| Global licence for `(22-cl)` for a polynomial Keller map | **FAIL** | The final integration from (8.2) is algebraically correct after (i) the resolved-direction/chart/descent/bijection lemma and (ii) repaired every-fibre Proposition 5.8 are supplied.  As filed it establishes neither from EW1--EW4+G1--G3, so “PROVED FROM EW1--EW4 + G1--G3” is false.  With both additions, étaleness gives quasi-finiteness, `N=Phi_!1` has Euler integral `chi_c(A^2)=1`, and the displayed `(22-cl)` follows globally. |
| Circular dependence on disputed Section 7 formula | **PASS** | No circular use of printed Notation 7.3, Proposition 7.4, or (22) was found.  The missing inputs are antecedent geometry/Proposition 5.8, not a disguised appeal to the disputed formula. |

## Required replacement lemma

The smallest clean addition is a single lemma, not a reassertion of G2.
For a polynomial Keller pair over `C`, a reference critical-value flag
`F_i`, and the corrected EW1--EW3 transport, prove or cite:

```text
Divisorial resolved-direction chart lemma.
There is one smooth projective point-blowup resolution X of the graph of
(f,g) and a distinct divisor E_i for every reference flag F_i such that:

(a) E_i is the divisorial valuation of F_i.  Its strict transform is P^1,
    and a residual-coordinate cover A^1_eta -> U_i=E_i\{infinity_i} is
    the quotient by a specified effective scalar finite cyclic group mu_m.
(b) Further graph-resolving blowups preserve this chart on the strict
    transform.  All finite coefficient/collision points lie in U_i, and
    f,g are finite on U_i.
(c) For every polynomial h with d_(h,F_i)=0, its residual polynomial is
    mu_m-invariant (state the tame deck/semi-invariance calculation).
    Hence it is the pullback of a unique regular function on U_i; for
    h=f-a0,g these functions are polynomials in z=eta^m.
(d) Under corrected Statement 3.14, z is in bijection with the geometric
    outgoing direction at the transported F_i(a), and the zero set of the
    descended f-value function over a is exactly the finite-value direction
    clusters, with no identifications between distinct i.
```

Parts (a)--(d) are precisely the five obligations isolated by the earlier
hostile review.  Surface elimination alone proves neither (c) nor (d).
The source of the deck step should be named with its hypotheses; the
campaign's cyclic residual lemma is the relevant form, rather than an
unstated assertion that all residual polynomials descend.

Add, separately, the repaired every-fibre Proposition 5.8 as an explicit
input, for example the independent audited replacement
`xmodel/sigray-prop58-every-fiber-independent-audit-sol-ultra-20260828.md`
(and its cited coordinator integration), rather than treating (8.1) as a
formal divisor identity.  Then replace the final verdict by:

```text
(22-cl) is proved for polynomial Keller maps conditional on
the divisorial resolved-direction chart lemma and repaired Proposition 5.8.
```

No stronger repair is necessary.  In particular, do not return to a
per-puncture excess, a boolean value-curve relation, or an injectivity claim
for `phi_i`.
