# Hostile producer-side pre-review: wild one-cusp valuation/completion structure

Status: **UNCHARGED advisory only**. This report neither promotes the packet nor satisfies any different-model gate. I did not inspect any other review or `jc2-lean`.

## Frozen-input verification

The four frozen inputs reproduce the requested SHA-256 values exactly:

```text
2710e90fdcbf1c2c9f61d6a606cf1e6553de5de65e4899367005433bc4f4e5f5  block-descent-a1-one-cusp-wild-valuation-structure-sol56-20260831.md
cd27b7f6687103fae0fc4e5fe19772e0f8e62939d73a655ebf04e57905ddba05  block-descent-a1-one-cusp-poisson-locally-finite-obstruction-sol56-20260831.md
2531a89d6c939aee6e0d402408f15d28a228927dc15d82c10d430e67164cb190  block-descent-a1-quartic-cycle1-function-pair-coordinator-integration-sol56-20260830.md
0a6272060a03c0071ad8b4c71aef00f3c724284d9590dcab61a2e75169a8713f  block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md
```

The announced 2026-08-31 promotion of the Poisson parent is treated only as a status relabel: every use below is rechecked on its merits.

## 1. Intrinsic completion and bracket

**CONFIRMED — (1.1), with a notation qualification.** Completing `C[A,U,Z]` along `(A,U)` gives `C[Z][[A,U]]`. Since `q_A=-1-2AZ` is a unit, the formal implicit-function theorem eliminates `A` uniquely. Direct substitution gives

```text
a(u,Z)=u^2-Zu^4+2Z^2u^6-5Z^3u^8+...
      =(sqrt(1+4Zu^2)-1)/(2Z) in C[Z][[u]].
```

Thus the completion of `R` *along the whole divisor* is `C[Z][[u]]`, whereas the completion of the local ring at its generic point is `C(Z)[[u]]`. Standard notation `widehat(R_P)` normally means only the latter, so the first object should be denoted explicitly as the `P`-adic completion.

**CONFIRMED — the orders.** Since `a=u^2(1-Zu^2+...)`, the normalized divisorial orders are `ord_P(U)=1`, `ord_P(A)=2`, `ord_P(Z)=0`. The last is a generic-`P` statement, not the maximal-ideal order at a closed point.

**CONFIRMED — (1.3).** The identity `1+2Za=sqrt(1+4Zu^2)` yields `B=2+4Za`. Hence `{u,Z}=B` and

```text
{F,G}=B(F_u G_Z-F_Z G_u),
X_H=B(H_u partial_Z-H_Z partial_u).
```

As cross-checks, `B a_u=4u` and `-B a_Z=2a^2`, recovering `{A,Z}=4U` and `{A,U}=2A^2`. The weakest hypothesis for this section is just the displayed hypersurface and Poisson bracket over a characteristic-zero coefficient field; the cyclic chart is unnecessary.

## 2. Associated graded and charged first jets

**CONFIRMED, with a typing correction — (1.4)--(1.6).** For `F=hu^m+...`, `G=ku^n+...`, direct differentiation gives degree `m+n-1` component

```text
2(m h k'-n h' k)u^(m+n-1).
```

This proves the floor and its iterated version by induction. If the coefficient vanishes, it is a degree component, not an “initial form.” In particular, when `m=n=0`, the asserted degree `-1` component is simply zero; negative graded pieces do not exist. State `H!=0` in (1.6), with `H=0` separate. These are notation/edge-case repairs only and do not alter a valuation bound.

**CONFIRMED — (1.9).** The `u^0` coefficient of `{f,g}` is exactly `2(f_1g_0'-f_0'g_1)=kappa`; consequently `f_0'` and `g_0'` have no common zero (indeed they generate the unit ideal in `C[Z]`).

**CONFIRMED — `deg f_0,deg g_0>=2`, under the cited distinct-point collision.** A degree-one coordinate separates the two normalization parameters `z!=z'`. If, say, `f_0` is constant, (1.9) forces `f_1g_0'` to be a nonzero constant, so `g_0` is affine and again separates them. The symmetric argument handles constant `g_0`. Thus the claimed degree bound follows from `kappa!=0` and the collision; singularity of `C_0` is not additionally needed.

**CONFIRMED with ring qualification — (1.10).** On `gr_P(Rhat)=C[Z,ubar]`, the degree `-1` symbols are `-2f_0'(Z) partial_ubar` and `-2g_0'(Z) partial_ubar`, and they are locally nilpotent because they lower polynomial `ubar`-degree. They are not locally nilpotent on the completed power-series ring itself. The safe conclusion is that the leading associated-graded derivations do not witness global wildness; an unqualified “do not detect wildness” is too broad.

## 3. Cusp-companion rectification and jets

**CONFIRMED — (1.11).** At the interior companion, etaleness makes `p=f-f(u_c), q=g-g(u_c)` a regular parameter pair, so the completion is `C[[p,q]]`. The bracket gives exactly `X_f=kappa partial_q` and `X_g=-kappa partial_p`.

**REFUTED as a blanket statement — “no local invariant at `u_c` can detect wildness.”** What is proved is narrower: the *unmarked formal conjugacy class of the differential germ*, and hence any fixed finite jet of that germ, cannot distinguish this pair from the tame translations on `A2`. The packet's next paragraph itself supplies marked local data that can detect wildness: the full formal expansions of the distinguished global generators. Safe replacement:

> No invariant of the unmarked formal vector-field germ, nor any fixed finite jet of it, detects global non-local-finiteness; marked infinite jets of global functions may do so.

This correction affects the prose in §1.2 and any summary using the broader phrase, but not (1.11).

**CONFIRMED — the marked infinite-jet criterion.** A derivation of a finitely generated algebra is locally finite iff the orbit span of every member of one finite generating set is finite-dimensional. Injectivity into the completed local domain preserves polynomial recurrences. The solutions of `P(kappa partial_q)F=0` are precisely finite sums `sum a_(lambda,j)(p)q^j exp(lambda q/kappa)` with the usual multiplicity bound. For `X_g=-kappa partial_p`, the corresponding exponent has the sign dictated by that operator. The pulled-back cusp equation is polynomial in `p,q`, so each translation orbit is finite, exactly as claimed.

## 4. Genuine generic boundary

**CONFIRMED — (1.12)--(1.14).** At the generic point of the unique ramified factor, characteristic-zero tame ramification and strict henselization give `b=s^2` after absorbing a unit square. Neither `b_f` nor `b_g` vanishes generically on irreducible `B`: otherwise irreducibility and the degree drop of a partial derivative force `b` to define a coordinate line, contrary to the singular branch packet. Thus `D(b)` is a unit for each charged field and `D(s)=D(b)/(2s)`. Its normal symbol is `cbar s^(-1)partial_s`, of valuation degree `-2`, and iteration gives `v(D^j s)=1-2j` with nonzero factors `1,-1,-3,...`.

**CONFIRMED — existence of a negative-valuation global function.** Let `W=O_(Y,eta_R)` be the boundary DVR. If `O(S)` were contained in `W`, `W` would have a center on affine `S`; composing with `S->Y` and using separatedness would identify that center with `eta_R`, which is not in `S`. Hence some `h in O(S)` has `k=v(h)<0`.

**CONFIRMED — (1.15) and the redundant non-local-finiteness proof.** The omitted technical bound is `D(W) subset s^(-1)W`, supplied by the tame inverse different. Writing `h=s^k u` with `u` a unit, the differentiated power term has valuation `k-2`, while `s^kD(u)` has valuation at least `k-1`. Inductively,

```text
v(D^j h)=k-2j,
lc(D^j h)=ubar*cbar^j product_(i=0)^(j-1)(k-2i).
```

Every product factor is a nonzero negative integer. In any finite linear relation, the largest iterate has the unique smallest valuation, so cancellation is impossible. This is genuinely independent of the automorphism/LND classification. Weakest hypotheses: a normal separated common model, a deleted tame index-two boundary divisor, generic nonvanishing of `D(b)`, and stability of `O(S)` under `D`. The inverse-different bound should be inserted; its omission is a proof-detail gap, not a false claim.

## 5. Completed coordinate fibres and flow divisor

**CONFIRMED componentwise — (2.1) and (2.4), including attainment.** At a finite deleted point choose `z` with `g-g(p)=z^e`; then exactly `D=(kappa/e)z^(1-e)partial_z`. At infinity choose `g=z^(-e)`; then exactly `D=-(kappa/e)z^(e+1)partial_z`. These give every divisor coefficient and both iterate products. For finite `e>=2`, no factor `1-ie` vanishes.

**GAP as stated — (2.5) silently needs connectedness/geometric irreducibility of the general coordinate fibre.** The promoted parent supplies a surjective etale map of total degree four but does not explicitly prove this connectedness. If the fibre has `delta` connected components with total genus `G=sum gamma_i`, the actual totals are

```text
deg Zero(D)=4+r_infty,
deg Pole(D)=2G+4-2delta+r_infty,
deg div(D)=2delta-2G.
```

The displayed (2.5) is the `delta=1` specialization. Without it, finite ramification can even vanish in the fully split case `delta=4, G=0, r_infty=4`; degree four alone therefore does not produce the ramified point used next.

This is not a merely formal objection. The disconnected curve control `C=C* disjoint_union C*` with maps `z |-> z^2` and `w |-> 1+w^2` is surjective, etale, and of total generic degree four: the two images omit `0` and `1` respectively. Its completion has `delta=2`, `G=0`, `r_infty=2`, and two finite deleted index-two points, so `d=2`, directly defeating `d>=3` under the literal curve hypotheses. It is a countercontrol, not a claimed surface realization.

**CONFIRMED conditionally — (2.6).** Once a finite deleted point `p` of index `e` exists, Riemann--Roch supplies a function with sole pole `p`, and direct iteration gives `ord_p(D^j h)=-M-je`; its coefficient contains `product_(i=0)^(j-1)(-M-ie)`, which never vanishes. Distinct orders prove independence. The later transverse-boundary argument itself supplies index-two points, so (2.6) can be recovered from the full boundary packet, but the claim that it follows from “degree-four fibre structure itself” is overstated.

A repair is either to assume connected general fibres or to prove the missing lemma. A plausible proof must show that a nontrivial relative algebraic closure of `C(f)` in `Frac(R)` would ramify over a finite value; smoothness would push that ramified sheet out of `S`, and finiteness of `Y->A2` would create a boundary divisor mapping to a vertical line, contradicting the sole irreducible nonvertical boundary image `B`. Until those steps are written, (2.5) and its provenance remain `GAP`. Local formulas (2.1), (2.4), and (2.6) are unaffected.

## 6. Necessary tuples and genericity

**CONFIRMED — the generic transversality construction and (3.1).** A normal surface has finite singular locus, and a plane curve has finitely many singular points. Since `B` is irreducible and not vertical, `f o beta_B` is nonconstant and has finitely many critical values. A target value can therefore avoid the images of `Sing(Y)`, `c,n`, every singular point of `B`, and every tangency. At each remaining intersection the ramified sheet and `B` are smooth and the tame completed map is `b->s^2`. Restricting to the transverse line makes `g-g(p)` a unit times `b`, hence a unit times `s^2`; every finite deleted place has `e_p=2`. Because `S=Y-R_bd` and the omitted value `n` is avoided, there are no additional finite missing points. Consequently `s_fin=d_f=deg(f o beta_B)`. No fibre through `Sing(Y)` and no forced tangency survives the finite exceptional-value choice.

**GAP — (3.2) and the four-row table inherit the unproved connectedness from (2.5).** With `delta_f` components and `G_f` the sum of their genera, the correct equality is

```text
d_f=2G_f+4+r_f-2delta_f.
```

Only when `delta_f=1` does this become `d_f=2gamma_f+2+r_f`. The listed positive partitions of total degree four are arithmetically complete, but their pairing with a single nonnegative genus and the exclusions `d_h<=2`, parity, Euler formula (3.4), and puncture bound all need connectedness. The same defect applies after interchanging `f,g`.

**REFUTED as an exact list for the full tuple — (3.6) is incomplete even after connectedness is added.** Section 3.3 treats `(d_h,gamma_h,r_h,lambda_h)` as the tuple, but (3.6) never excludes a supplied `gamma_h` inconsistent with (3.2). For example `(d,r,gamma,lambda)=(5,1,17,(4))` passes the three literal tests in (3.6) but violates the table. Add

```text
d_h != 2gamma_h+2+r_h
```

to (3.6), or declare `gamma_h=(d_h-r_h-2)/2` to be derived rather than independently recorded. Under connectedness and that repair, the four partition rows themselves are `CONFIRMED` as necessary, never sufficient.

Weakest hypotheses for this section are: connected general coordinate fibre (or the corrected componentwise ledger), finite normal `Y->A2` with `S=Y-R_bd`, irreducible noncoordinate `B` with normalization `A1`, and generic `(2,1,1)` tame residue-degree-one ramification.

## 7. Inverse-Kummer collision

**CONFIRMED conditionally — (3.7)--(3.9).** The equality `mu=d1=2` uses both the exact `(mu,r_pp)=(2,2)` model and the minimal-counterexample cyclic replacement; it is not an identity for an arbitrary nonminimal first leg. Given the cited inverse-Kummer identities, the second effective divisor represents the inverse of `[Phi]`, not an independent Kummer class, and the selected sheet difference is `J_t=u^2-v^2`.

**CONFIRMED — (3.10).** For a rank-one valuation with `alpha=w(u), beta=w(v)>0`, unequal values give `w(u^2-v^2)=2min(alpha,beta)`. Equal values give at least `2alpha`, with equality precisely unless the initial squares cancel. In the transverse case `(u,v)` is a regular parameter pair and the compact Newton edge joins `(2,0)` to `(0,2)`; in the tangent case no regular-parameter Newton polygon is determined.

**CONFIRMED — order-index only, not a flow place or ramification change.** Off `B`, the chosen difference contributes `2w(J_t)` to the polynomial discriminant; the normalized etale algebra has unit discriminant, so this lies in the square of the order index. At a `(2,1,1)` value, the colliding points are the two retained unramified companions, while the length-two boundary point is distinct. Thus neither collision point enters `Sigma_fin`, and no `e_p` in (2.1) changes. This conclusion keeps the monogenic order divisor, physical boundary place, and coordinate-fibre series separate.

In `L1` the collision *target value* does lie under the pre-existing boundary place. Accordingly, the packet's phrase “not one of the places” is safe only when it refers to the two interior collision points; the exact statement is that the collision creates no additional place and changes no index.

There is one wording **GAP**: if “ordinary point of `B`” means a smooth point of the plane curve, the cited census does not exclude some other singular point of `B`; §3.1 itself allows and avoids such points. What is safely forced is `z_0 outside B` or `z_0 in B\{c,n}` with the `(2,1,1)` companion configuration. If “ordinary” means only that fibre type, the dichotomy is confirmed. This does not affect the order-index conclusion.

**CONFIRMED — (3.12) and the incidence bounds.** At `mu=2`, the cited cyclic ledger specializes to `e(D_B)=-6-N` and deficit sum `N+3`. The cusp contributes `epsilon_c` to `N`; an `L1` collision contributes two further distinct points because its target differs from the cusp, whereas `L0` contributes none. These counts concern `D_B` and cannot be transferred into the coordinate-fibre divisor (2.1).

## 8. Status typing and maximum-safe conclusion

The packet's labels attached solely to conclusions of the now-promoted Poisson parent are stale status metadata: its Hamiltonian non-local-finiteness and degree-four generic-fibre conclusions may be relabeled as promoted conditional inputs. “Conditional” remains essential because the whole discussion assumes a hypothetical charged pair. Promotion does not manufacture the connectedness statement missing from the cited theorem. The inverse-Kummer successor's provisional labels are separate and should remain.

Unresolved alternatives should be typed more precisely than `PROVISIONAL`: `u_c in Phi` versus not, `L0` versus `L1`, and transverse versus tangent are exact exhaustive dichotomies whose selected alternatives are **OPEN**. The value of `kappa_B`, the numbers `(d_h,r_h)`, and the special cusp-boundary expansion remain **OPEN**. Add two omitted open issues: connectedness of each general coordinate fibre, and smoothness of `B` at an `L1` collision if “ordinary” is intended geometrically.

The existing **OPEN** typings for the length-three boundary completion, actual cusp Puiseux/Newton data, special-boundary leading terms, and any transport from monogenic index to a dicritical jump are all **CONFIRMED**. The cubic discriminant control is not an equation for the charged cusp completion.

Per maximum-safe item:

| Item | Verdict | Required correction |
|---:|---|---|
| 1 | **CONFIRMED** | Interpret local nilpotence only on the associated graded; narrow “detect wildness” as in §3 above. |
| 2 | **CONFIRMED** | The interior companion is rectified; the length-three boundary germ remains open. |
| 3 | **CONFIRMED** | Insert the inverse-different estimate before (1.15). The independent non-LF proof is valid. |
| 4 | **GAP** | (2.1)/(2.4) are exact componentwise, but (2.5), the single-genus table, and closures need connectedness; (3.6) also needs the genus-mismatch clause. |
| 5 | **CONFIRMED conditionally** | Say “no additional flow place”; retain the inverse-Kummer status and do not assert `z_0 in B_reg` without proof. |

## 9. Corrections, blast radius, and best falsification test

Overall verdict: **GAP**, not because the central boundary computation fails, but because a hidden connectedness premise supports the claimed fibre classification.

The principal correction is to prove geometric connectedness for both general coordinate fibres or replace every single-genus formula by the componentwise ledger. Its blast radius is (2.5)'s positivity inference, the claim that (2.6) follows from degree four alone, (3.2)--(3.5), the four-row table as a full necessary table, `Theta_h`, (3.6), and maximum-safe item 4. It does **not** affect the completion/bracket calculations, the generic-boundary proof (1.15), the local flow formulas, or the order-index analysis. Boundary transversality independently supplies finite index-two places, so non-local-finiteness remains proved even while the tuple table is open.

The other repairs have narrow blast radius: replace the blanket local-detectability claim; type zero/negative associated-graded components correctly; add the missing genus check to (3.6); and distinguish an `L1` target value from its two interior companions and its separate boundary place.

**Best next falsification test.** Determine

```text
C(f)^alg intersect Frac(R)  and  C(g)^alg intersect Frac(R)
```

inside `Frac(R)`, equivalently test transitivity of the geometric monodromy on a general vertical and horizontal slice. A nontrivial relative algebraic closure immediately forces the multi-component correction and falsifies the four-row closure. Equality with `C(f)` and `C(g)`, proved together with geometric connectedness, supplies the missing premise before any expenditure on `(d_h,r_h)` or an SNC pole expansion.

<!-- BODY-END -->
