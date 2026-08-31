# Hostile review: corrected missing-multiplicity identity (2.3')

## 0. Integrity and review boundary

The three frozen inputs reproduce the charged SHA-256 values exactly:

```text
634940bb13bb0ad28a7bfa51f76abd987acc2b6382e3d5688262fcdb747ab23a  block-descent-a1-rank4-missing-multiplicity-identity-opus5-r2-20260831.md
eeb4670511f35b7c52f03fa03d334eadff9eb3b7f3b6e18011beb7de4e73c54b  block-descent-a1-rank4-dicritical-typing-d1-d4-grok46-20260831.md
ed0d288bec800bc1cfb59506a60ac76243aa47378692330f54f9d0860d754fb9  block-descent-a1-rank4-reducible-component-tree-ledger-hostile-review-sol56-20260831.md
```

I treated the first packet as the object under review, the second only as its declared provisional source interface for Orevkov/Chau, and the third only as the promotion-status hierarchy. I did not inspect `jc2-lean`, alter a charged input or canonical ledger, or promote any statement. All computations below are exact desk computations.

For citations below, **Opus**, **Typing**, and **Hierarchy** mean respectively the first, second, and third frozen inputs, with the cited numbers denoting their frozen line numbers.

## 1. Executive verdicts

**Overall: the packet cannot carry status `COMPLETE`.** Its corrected generic fibre formula is sound in the charged plane setting and repairable at the stated generality, and its short Orevkov inequality is mathematically decisive under one explicit inertia hypothesis. But K3 does not refute the Keller-scoped ledger identity, inertia alone does not force all `s_l=1`, the budget proof has an admitted special-point gap, and the frozen promotion hierarchy does not certify the universal inertia premise needed to kill every row.

| exact claim checked | verdict | hostile result |
|---|---|---|
| Boundary curves satisfy the three-way typing, and only appropriate dicriticals meet a generic `B_i`-fibre | **CONFIRMED** | No fourth curve type or generic evasion exists; the type-(C) witness needs one more blowup. |
| K3 refutes ledger (2.3) for the Keller map itself | **REFUTED** | K3 is run on `C^2` with Jacobian `4x^2y^3`; it is non-étale and outside the ledger hypotheses. |
| K3 refutes the old formula for general smooth-affine étale maps after restricting its domain | **CONFIRMED** | On `S=(C*)^2`, `A_F=V(uv)` and the `u=0` component has `(s,mu,f)=(2,2,0)`. This is a different, broader claim. |
| (2.3') is proved unconditionally for every dominant étale smooth-affine map | **GAP** | The proof constructs only the `C^2` compactification. A standard graph-resolution repairs it; the plane/Keller instance is confirmed. |
| Generic intrinsic `mu_l` is the Orevkov base multiplicity | **CONFIRMED** | Typing supports generic local degree; positivity is from multiplicity/divisor order, not `deg f_phi>0`. |
| `bracket_l>=mu_l s_l` and Corollary 5.5 | **GAP** | The proof applies a finite-germ degree at all special points and relies on admitted, unsourced comparison C3. |
| Proposition 5.3's cycle type | **CONFIRMED** | The local model gives one `mu_l`-cycle at each of the `s_l` generic boundary points. |
| Promoted inertia alone forces every `s_l=1` | **REFUTED** | A transposition is compatible with an extra `(mu,s)=(1,2)` line and `f=0`. Inertia plus `f(B_i)>=1` repairs the claim. |
| Theorem 10.1's inequality under universal componentwise nontrivial inertia | **CONFIRMED** | Distinct selected lines each cost at least two in Orevkov's sourced sum, so `2m<=3`; neither fibre identity nor C3 is used. |
| Every reducible charged row is already dead from genuinely promoted inputs | **GAP** | Hierarchy §9.1 omits the universal inertia premise from its precise unconditional tier. An exact promoted citation would close the sole remaining provenance gap. |
| Genericity claims | **CONFIRMED** generically / **GAP** at special points | The exceptional sets are finite; numerical boundary mass is not defined when the compactified fibre is positive-dimensional. |
| K1–K4 desk arithmetic | **CONFIRMED** | All degrees, substitutions, local multiplicities, and local cycle patterns recompute; none is a global étale control on `C^2`. |

## 2. Compactification and boundary typing

**Verdict: CONFIRMED for the plane-map compactification; GAP at V1's advertised arbitrary-surface scope.**

For the construction actually made in Opus 154–237, no boundary curve escapes the trichotomy. If `E` is an irreducible complete boundary curve, the closed irreducible set `Phi(E)` has dimension zero or one. In dimension one it is either the target line at infinity or a different projective curve with nonempty affine part; in dimension zero its image point is either infinite or finite. These are exactly polar, dicritical, and finite-contracted. A corner is not a fourth type: it lies on component curves, and its one image is exceptional rather than generic.

The generic-fibre exclusion is also correct. There are finitely many boundary components. A finite-contracted component supplies one target point; a polar component supplies none in `A^2`; two distinct irreducible image curves meet in finitely many points; corners, branch values of `Phi|_l`, and nongeneric local-degree points also have finite image. After deleting those points from `B_i`, every boundary preimage lies on a unique dicritical whose image is `closure(B_i)` (Opus 214–237).

The type-(C) witness needs one correction. For `F=(x,x^2y)` and `x=s`, `y=1/(s tau)`, the displayed extension is `(s,s/tau)`, which is not a morphism at `(s,tau)=(0,0)`; “for every `tau`” in Opus 189–193 is false. Blowing up with `s=tau*b` gives `(tau*b,b)`: the new exceptional `tau=0` is dicritical, while the strict transform `b=0` is genuinely contracted to `(0,0)`. Thus finite-contracted boundary really occurs, but the packet skipped the resolving blowup.

The scope defect is explicit. V1 starts with an arbitrary smooth affine surface (Opus 26–40, 458–465), but Section 2 says “start from `S=C^2 subset P^2`” and then uses that the boundary is a connected rational tree (Opus 156–167, 299–300). Neither construction nor tree assertion proves the stated generality. The identity is repairable: compactify an arbitrary smooth irreducible quasi-projective surface, close the graph of `F`, and resolve the graph and boundary outside `S` to obtain a smooth projective `X`, a morphism `Phi:X->P^2`, and a divisorial boundary. The dimension trichotomy and generic-fibre argument then go through without connectedness, rationality, or affineness. As written, however, the claimed unconditional proof at arbitrary `S` has a compactification gap.

## 3. The V2 hand control and the scope of the refutation

**Verdict on V2's advertised refutation of the ledger identity: REFUTED.**

The packet runs K3 as the polynomial map on `S=C^2`: it labels all four controls non-Keller, computes `F(C^2)`, and invokes the “non-etale form” of the fibre formula (Opus 647–655, 676–695). Directly,

```text
F(x,y)=(x,x^2 y^4),             det JF=4x^2 y^3,
```

so the Jacobian vanishes on `V(xy)`. Thus K3 satisfies neither V1's étale hypothesis nor the ledger's plane-Keller/rank-four hypothesis. Its chart calculation is correct: for `t=xy`, `w=xy^2`, one has `(u,v)=(t^2/w,w^2)`, hence `s=2`, `mu=2`, `f(0,b)=0`, and the multiplicity-weighted generic boundary mass is `2*2=4`. This proves that an `s`-blind formula fails for this broader non-étale map. It does not refute (2.3) as the ledger stated it for the Keller map itself. Indeed Opus's own OPEN-1 concedes that no Keller example with `s_l>=2` was produced (Opus 890–897).

There is a precise repair, but it changes the claim. Restrict the source to

```text
S=D(xy)=(C*)^2.
```

The same formula is then a dominant étale morphism of degree four. It is finite étale over the target torus, its nonproper set in `A^2` is `V(uv)`, and `B_i=V(u)` is one irreducible component. At generic `(0,b)`, the same boundary line has `(s,mu)=(2,2)` and `f=0`. This honestly refutes the generalized étale-surface version of the old `s`-blind identity. It still does not touch the Keller `C^2` statement; its generic inertia at `V(u)` is `(2,2)`, not a charged transposition or three-cycle.

## 4. Local multiplicity and the Orevkov base term

**Verdict: CONFIRMED for the generic base term; GAP for Proposition 4.3's special-point comparison.**

At a generic smooth point of a dicritical `l`, choose `l={t=0}`, a parameter `U` along its image, and a transverse equation `V` of that image. If

```text
V o Phi=t^mu*unit,       U o Phi=w+terms divisible by t,
```

then the isolated local degree is `mu`. Thus `mult_l(Phi^*Gamma)` equals the generic algebraic/topological local degree (Opus 303–346). The Typing source interface defines Orevkov's `mu_l` as the generic collision multiplicity on the surviving line and Chau's restatement calls it generic `deg_u f*` (Typing 111–131, 151–157). At a generic point, where no contraction intervenes, these are the same integer.

The positivity route must be kept typed. Typing 224–234 derives `mu_l>=1` from Orevkov's point-multiplicity definition: `k=1` always works. It expressly rejects an inference from `deg f_phi>0`, which measures the degree of a curve parametrization, not the transverse surface multiplicity. Opus avoids that fallacy: its positivity follows from the positive divisor coefficient, and it invokes `f_phi` only for normalization of the image (Opus 303–307, 421–426). Calling this the “Orevkov base term” is nevertheless licensed only in the Keller/Orevkov setting supplied by Typing, not for every arbitrary étale surface in V1.

The stronger bound

```text
bracket_l >= mu_l*s_l
```

is not established by the declared interface. Proposition 4.1(b) assumes that the original `Phi`-fibre is finite near the point (Opus 313–316), but Proposition 4.3 applies it at every affine ramification point and replaces Orevkov's special-point `deg_u f*` after contraction by `mult_u(Phi)` before contraction (Opus 428–445). At an attachment to a finite-contracted/`L_C` curve, the latter finite-germ degree is not even defined. Opus labels this comparison (C3) and admits that it was asserted rather than proved. Typing sources only generic `mu_l` and nonnegativity of the Orevkov corrections; it does not source the needed special-point comparison (Typing 119–131, 236–244). A proof directly in Orevkov's collapsed local model could repair the bound. Until then Proposition 4.3 and the budget-only Corollary 5.5 are GAP. This gap is irrelevant to the shorter Theorem 10.1 chain, which uses only `bracket_l>=mu_l` from the sourced nonnegative corrections.

## 5. Corrected identity, cycle types, and charged-row corollaries

**Verdict on (2.3'): CONFIRMED in the plane-Keller scope and whenever the required compactification is supplied; GAP as an unconditional proof for every smooth affine `S`. Verdict on Proposition 5.3: CONFIRMED. Verdict that inertia alone recovers (2.3): REFUTED; it needs one additional charged input.**

For a generic `z in B_i`, Section 2 leaves only dicritical points over `B_i`. Conservation of degree for the finite compactified fibre gives

```text
N = sum_{p in F^{-1}(z)} mult_p(F)
    + sum_{p in Phi^{-1}(z) cap D} mult_p(Phi).
```

Étaleness makes the first sum the set count `f(z)`. A line `l` of curve-map degree `s_l` has `s_l` unramified points over generic `z`, each of generic local degree `mu_l`, proving `N=f(z)+sum s_l mu_l` (Opus 246–286, 385–395, 458–474). No Orevkov or Chau theorem is needed for this fibre identity. The only defect is the arbitrary-`S` compactification gap identified in Section 2 of this review.

The cycle-type calculation is exact. At a finite source point, étaleness supplies a fixed sheet. At a generic boundary point the local map is analytically `U=w+...`, `V=t^{mu_l}*unit`; one transverse meridian cyclically permutes the `mu_l` roots of `t` and gives one `mu_l`-cycle. There are `s_l` such boundary points on `l`. Hence the inertia type is

```text
{mu_l repeated s_l times, for l over B_i} union {1^f(z)}.
```

This proves Proposition 5.3 (Opus 485–519). A transposition therefore produces a distinguished `(mu,s)=(2,1)` line; a three-cycle produces `(3,1)`; every other line over that component has `mu=1`.

But inertia alone does **not** force `s=1` for every line. In the transposition case the abstract data

```text
(mu,s)=(2,1) and (1,2),     f=0
```

have degree `2+2=4` and exactly the same permutation type `(2,1,1)`. A `mu=1` dicritical is invisible as anything but fixed cycles. The charged recovery is valid if one also spends the companion-sheet floor `f(B_i)>=1`: the transposition identity gives `2=f+sum_other s_l`, so every extra line has `s=1`; the three-cycle gives `1=f+sum_other s_l`, so there are no extras. The exact companion equality `f=2` or `1` is stronger and removes every extra line, as Corollary 5.4(3) says. The alternative budget proof in Corollary 5.5 depends on the gapped Proposition 4.3. Moreover Opus 558 calls `(2,1,2)` the census while 559–560 immediately admits a transposition alternative with an extra `(1,1)` line and `f=1`; the first wording is not unconditional.

Accordingly, recovery of (2.3) on charged rows is CONFIRMED conditional on the universal inertia premise plus the companion floor (or exact census). It is not a consequence of inertia alone, and the frozen promotion hierarchy does not itself certify those two premises at the universal scope claimed; Section 8 addresses that provenance defect.

## 6. Genericity and special branch points

**Verdict: CONFIRMED generically; GAP in two special-point overstatements.**

The exceptional locus listed in Opus 580–601 is finite on each curve `B_i`: images of contracted curves, finite-contracted boundary components, corners, singular/intersection points of target curves, branch values of the finite curve maps, and zeros of the generic transverse unit. Removing it gives a genuine Zariski-open dense subset, and (2.3') and Proposition 5.3 are statements only there.

At a special point `z'`, étaleness gives disjoint local inverse branches around every finite preimage, so nearby fibres have at least `f(z')` points. Thus `f(z')` is no larger than the generic value along any `B_i` through it. If `Phi^{-1}(z')` is finite, conservation of degree yields the safe one-sided statement

```text
N-f(z') = total boundary multiplicity at z'
          >= sum_{l over B_i} s_l*mu_l.
```

That is Proposition 6.1 (Opus 620–635). However “at every point” in Opus 637–638 drops its own finite-fibre qualification: when a compactified fibre contains a contracted curve, there is no finite sum of isolated local degrees. Also the exact leakage formula (6.1) comes from the smooth-image chart (4.2); at a singular image point Proposition 4.1(b) gives only an inequality. Special points may therefore add contracted components, corners, curve-map ramification, singular-image effects, or positive-dimensional fibres. None changes the generic identity, but the packet's exact special-point narrative is too broad.

## 7. Independent recomputation of the hand controls

**Verdict on the arithmetic: CONFIRMED. Verdict on K3's claimed Keller-scope consequence: REFUTED.**

| control | `N` | generic boundary data over `u=0` | finite count | check |
|---|---:|---|---:|---|
| `K1=(x,xy)` | 1 | `s=1, mu=1` | 0 | with `t=x,w=xy`, `Phi=(t,w)` |
| `K2=(x,xy^2)` | 2 | `s=1, mu=2` | 0 | `Phi=(t^2/w,w)`; one 2-cycle |
| `K3=(x,x^2y^4)` | 4 | `s=2, mu=2` | 0 | `Phi=(t^2/w,w^2)`; two 2-cycles |
| `K4=(x,xy^2+y)` | 2 | `s=1, mu=1` | 1 | after `w=-1+t xi`, `Phi=(t,-xi+t xi^2)`; trivial inertia |

For K1–K3 use `t=xy,w=xy^2` where indicated; solving the monomials gives exactly the substitutions in Opus 657–706. For K4, `(w^2+w)/t` becomes `-xi+t xi^2`, and the bounded solution at `x=0` is `y=b`, so `2=1+1` (Opus 708–730). The Jacobians are respectively `x`, `2xy`, `4x^2y^3`, and `2xy+1`; none is a Keller map. Their cycle descriptions are therefore local analogies to Proposition 5.3, not controls satisfying its global étale-cover hypotheses. The controls correctly test the multiplicity bookkeeping, and K3 genuinely displays why `s_l` belongs in the general formula. Only the inference from K3 to the ledger's Keller-scoped (2.3) fails, as detailed in Section 3.

## 8. Theorem 10.1 and the reducible rank-four branch

**Mathematical verdict: CONFIRMED under its explicit inertia hypothesis. Advertised “promoted, hence unconditional” application: GAP.**

The decisive chain itself survives every mathematical attack:

1. By Proposition 5.3, a nontrivial generic inertia cycle on `B_i` must come from a boundary point, not a finite étale preimage. A transposition or three-cycle therefore supplies an Orevkov dicritical `l_i` over `B_i` with `mu_{l_i}=2` or `3`.
2. The `l_i` are distinct. The image of one irreducible nonconstant line is one irreducible curve (Typing 198–203), so one line cannot map onto two distinct `B_i`.
3. Orevkov's sourced formula is `bracket_l=mu_l+corr_l`, with every correction nonnegative (Typing 119–131, 236–244). Thus every selected bracket is at least `mu_{l_i}>=2`. Every omitted bracket is nonnegative; in fact Typing's correctly typed D3 gives `mu_l>=1`.
4. Extra dicriticals over components of `A_F` outside `B` only increase the full sum. Hence, at `N=4`,

```text
2m <= sum_i bracket_{l_i}
   <= sum_{l in L_F} bracket_l
    = N-1 = 3.
```

For a nonempty branch this gives `m=1`; a reducible branch (`m>=2`) gives the immediate contradiction `4<=3`. This uses neither (2.3), (2.3'), Proposition 4.3, the companion census/floor, nor special-point comparison (C3). Opus 854–857 wrongly includes C3 among the residual risks for this row-emptying argument; C3 affects Corollary 5.5, not Theorem 10.1.

What is not established by the frozen promotion record is the universal premise. Hierarchy §9.1 calls its list “the precise hierarchy” and its unconditional promoted tier does **not** include “the generic divisorial inertia at every `B_i` is a transposition or a three-cycle” (Hierarchy 247–255). Hierarchy §3.1 says more loosely that a promoted producer pins a fibre census (44–48), and the provisional Typing packet interprets that as generic `T211/T31` on every component (Typing 287–305), but the charge authorizes Typing as the Orevkov/Chau source interface, not as a canonical promotion ledger. It does not provide the exact promoted theorem and quantifiers needed to resolve the conflict.

The weakest theorem needs only the explicit hypothesis:

```text
(H_inertia) For every irreducible B_i, a generic meridian has at least
            one cycle of length >=2.
```

Under `H_inertia`, the row death is CONFIRMED and is stronger than the erroneous 16-row bookkeeping. Without an exact promoted citation proving `H_inertia` for every actual charged component, the claim that all reducible rank-four rows are already unconditionally dead is GAP, not a permissible promotion.

## 9. Scope, weakest hypotheses, corrections, and blast radius

The weakest safe statements are these.

- **Generic fibre identity.** Let `S` be a smooth irreducible complex quasi-projective surface, let `F:S->A^2` admit a smooth proper graph-resolution `Phi:X->P^2` that is dominant generically finite of degree `N`, and let `B_i` be an irreducible curve component of `Phi(X-S) cap A^2`. For generic `z in B_i` with finite compactified fibre,

  ```text
  N = sum_{p in F^{-1}(z)} mult_p(F) + sum_{l over B_i} s_l*mu_l.
  ```

  It is enough that `F` be unramified at the finite points in those generic fibres to replace the first sum by `f(z)`; global étaleness is stronger than necessary. No Keller condition, `N=4`, `d1=1`, irreducibility of `A_F`, or scheme-theoretic reducedness is needed. “Component of `A_F`” means a component of its reduced support. Without the graph-resolution hypothesis/construction, Opus has proved this only for `S=C^2`.

- **Cycle type.** Add étaleness in a neighbourhood of the finite sheets and choose the meridian ball away from every other nonproper/branch component. Then Proposition 5.3 holds. The charged `(2,1)` and `(3,1)` distinguished lines follow.

- **Orevkov statements.** The names `L_F`, `mu_l`, `bracket_l`, and the equality `sum bracket_l=N-1` are sourced here only for plane Keller maps in Orevkov's reduction. They must not be exported to arbitrary étale surfaces merely because the generic compactification multiplicity has an analogous definition. Proposition 4.3 additionally needs a proof of the special-point comparison in the collapsed model.

- **Rank-four irreducibility.** It suffices that `F:C^2->C^2` be a degree-four Keller map, each charged `B_i` be an actual component of `A_F`, Orevkov's sourced formula apply, and `H_inertia` hold at every `B_i`. The exact companion census and both fibre identities are unnecessary for `m=1`.

The correction and blast radius are correspondingly sharp:

1. K3 must be demoted from a refutation of the Keller ledger identity to a non-étale control; its restriction to `(C*)^2` is the valid counterexample only to the generalized étale-surface reading. The Keller-scoped (2.3) remains GAP, not refuted.
2. Add the graph-compactification argument to V1. This repairs (2.3') without changing its formula. Correct the type-(C) witness by the extra blowup.
3. Mark Proposition 4.3 and Corollary 5.5 GAP pending C3/a collapsed-model proof. Charged recovery of (2.3) can instead use inertia plus the companion floor, if that floor is genuinely promoted.
4. Theorem 10.1's mathematical implication survives intact and is independent of C3 and (2.3). Its claimed unconditional campaign use, and hence the present assertion that every reducible row is already dead, remains GAP only because the frozen precise hierarchy does not certify universal `H_inertia`.

The claims that `N` may be arbitrary and that reducedness/irreducibility of the whole `A_F` is unnecessary are correct for the generic identity. The claims that the written proof already covers arbitrary smooth affine or quasi-projective `S`, and that its intrinsic `mu_l` is automatically an “Orevkov” term at that scope, overreach.

## 10. Best next falsification test

Demand the exact promoted theorem text supporting `H_inertia` and test its quantifiers against one arbitrary actual component `B_i`: it must say **every** charged `B_i` (not merely some component or all components of a different curve), must identify `B_i` with an actual `A_F` component at `d1=1,N=4`, and must make `T211/T31` a generic meridian cycle type rather than only a fibre-cardinality label. If any clause fails, the unconditional row death fails at its sole remaining input. If all clauses pass, Theorem 10.1 applies and every reducible rank-four row is indeed dead, regardless of the flawed 16-row ledger.

<!-- BODY-END -->
