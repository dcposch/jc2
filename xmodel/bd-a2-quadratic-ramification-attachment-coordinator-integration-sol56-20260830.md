# Coordinator integration: quadratic ramification attachments and lattice gate

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `f89cbb02305ee6fef32a79ccb8ff53fc4740a2a1`  
Lifecycle: **BINDING INTEGRATION / SMOOTH PROJECTIVELY FINITE QUADRATIC SCOPE**

## 0. Disposition and custody

Fable 5 independently reconstructed the sealed producer

```text
f3129c3497e265988617f7da66b7cf2da408b5736c1f91338a78fbbd111caff2
  xmodel/bd-a2-quadratic-ramification-attachment-dichotomy-sol56-20260830.md
  body 9399 / c37282a42af45c57e723dddd061ce2681203564df1b76008e8001206b2c69199
```

and returned `CONFIRM_WITH_CORRECTIONS`. Its sandbox-attested raw review body
is

```text
aa4877388dddadfbe2d4b167356c76f35424a440951ef0cc0cab6502c9dcf610
  xmodel/bd-a2-quadratic-ramification-attachment-hostile-review-fable5-20260830.md
```

and its sealed full-file SHA-256 is
`c1ab1258005080cfa58d979820bebff5bb233638e96984aa1b6aae425e37f477`.
The clean schema-v2 receipt has exit code zero and pins unchanged prompt,
adapter, launcher, Seatbelt profile, validator, fallacy appendix, and composed
model-prompt hashes.

The review confirms every attachment and graph calculation. This integration
adds its two missing lemmas: the reduced affine ramification is nonempty, and
the boundary critical set is exactly—not merely contained in—the classified
attachment set. It also deletes the unnecessary and generally false claim
that `Y` is affine. Finally, the reviewer independently computes Picard rank
eleven and invalidates the proposed raw class-group-rank shortcut, agreeing
with the sealed supporting desk packet
`7ee2a8e3e5eaae8b681da4a8b17e410199a4409fecb872dcc6b14d54394adefc`
(body `0ad7e812...`).

## 1. Scope and notation

Let

```text
X subset P2 times P1
```

be a smooth irreducible quadratic Miranda incidence surface of class
`2A+3B`. Let `pi:X->P2` be the degree-three incidence projection, assume it
is finite on a neighborhood of the infinity divisor

```text
H=X intersect ({infinity line} times P1),
```

and assume `H` is reduced. Put `Y=X minus H`, let `R_red` be the reduced
critical support of `pi` in `Y`, let `Rbar` be its closure in `X`, and put
`U=Y minus R_red`. The block-side application additionally assumes the
promoted dominant morphism `A2 -> U`.

The promoted first-leg theorem forces the resolved boundary of `U` to have
only rational components and forest dual multigraph. The promoted reduced
`(2,3)` classification then restricts `H` to `F1`--`F7`; `F8,F9` have no
rational-tree refinement.

Finiteness near `H` excludes a vertical `(1,0)` component of `H`: such a
component is an entire fibre of `pi` over one point of the infinity line.
Thus projective-coefficient-basepoint types `F3,F6` lie outside the present
scope rather than being eliminated inside it.

## 2. Exact attachment lemmas

**Cycle lemma.** Let `T` have connected tree resolution graph and let `Q` be
an irreducible reduced curve not contained in `T`. If the normalization of
`Q` has two distinct branches over `T`, then every embedded resolution of
`T union Q` has a cycle in its dual multigraph. Extra blowups either attach a
pendant vertex or subdivide an edge of the resolved `T` tree. The single
strict-transform vertex of `Q` then has two edges into that tree; distinct
endpoints close the unique path, while equal endpoints form a parallel-edge
cycle. The statement covers two physical points, two analytic branches over
one point, singular `Q`, tangencies, and attachments deep in exceptional
trees.

**Exact boundary critical set.** In a local chart

```text
X: f(u,v,z)=0,                 H: f(0,v,z)=0,
```

the critical divisor of `pi` is `f_z|X=0`. A point of `H` lies on it exactly
when it is a singular point of `H_red` or a smooth point where the relevant
branch is critical for projection `H->L_infinity`; equivalently the vertical
line has intersection multiplicity at least two there.

This Cartier critical divisor has no component contained in `H`. Indeed, if
a reduced factor `h` of `f(0,v,z)` also divides `f_z(0,v,z)`, coprimality with
the residual factor forces `h|h_z`, hence in characteristic zero `h_z=0`.
Then `h=h(v)` defines the excluded vertical `(1,0)` component. Purity of the
Cartier divisor therefore puts every boundary critical point in `Rbar` and
shows that there is no additional, unclassified attachment kind.

**Nonemptiness.** `R_red` is nonempty. A positive-dimensional fibre away
from `H`, if present, lies in the critical locus. If no such fibre exists,
properness makes `pi` finite; an everywhere-etale degree-three map from the
irreducible `X` to the simply connected `P2` is impossible. Since the
critical divisor has no component in `H`, its affine part is nonempty.

## 3. Attachment dichotomy

For a rational component's normalization of degree `b` over the infinity
line, Riemann--Hurwitz gives total ramification `2b-2`, with contribution at
most `b-1` at one point. Thus every degree-three component and every
degree-two component has at least two distinct normalization critical points.
The forest budget prevents their images from identifying in the relevant
`F1,F2,F4` configurations. In `F7`, the two length-two contacts with its two
disjoint sections are distinct double-root points. Therefore:

```text
F1, F2, F4, F7 + irreducible R_red
    => two branches of Rbar over H
    => cycle in the resolved full boundary
    => contradiction.                                 (3.1)
```

In `F5`, every component has projection degree one. The exact boundary
critical set is only its unique triple/contact point `p_0`, so the attachment
argument supplies only one branch and does not eliminate the type. The
ramification Cartier class is

```text
R_pi=(2A+B)|X,                 H.R_pi=8,
```

and all eight intersection units are concentrated at `p_0`.

Combining the cases gives the promoted conclusion:

> In the declared smooth, reduced, projectively finite quadratic block
> scope, every survivor has reducible `R_red` or infinity type `F5`. If
> `R_red` is irreducible, the only surviving infinity type is `F5`, with its
> entire boundary ramification intersection concentrated at the unique
> triple point.

This is a necessary-condition dichotomy. It proves neither that `F5` occurs
nor that reducible ramification is compatible with a first leg.

## 4. Units, class groups, and the failed rank shortcut

The dominant block morphism `A2->U` forces `O(U)^*=C^*`: the pullback of a
unit is constant, and density makes the original unit equal to that constant.
Restriction gives `O(Y)^*=C^*` as well. Since `Y` is smooth and integral and
`R_red` is pure codimension one, localization yields an injection

```text
Z^{components(R_red)} -> Cl(Y).                       (4.1)
```

Affineness of `Y` is neither required nor asserted.

This injection does not make a raw rank bound useful. Projection
`X->P1` is a smooth-total-space conic bundle with nine simple rank-two
singular fibres. Equivalently, adjunction and Noether give

```text
K_X^2=-1,       e(X)=13,       rho(X)=11.
```

If reduced `H` has `s<=3` components, localization from `X` gives

```text
rank Cl(Y) >= 11-s >= 8.                              (4.2)
```

No independence of the component classes is assumed. Since the total class
of `H` is nonzero, `rank Cl(Y)<=10`; the raw class-group rank can therefore
never supply the proposed rank-at-most-one gate. It should be treated as a
diagnostic—an output at most one would reveal an error—not as an elimination
strategy.

The exact numerical controls are

```text
R_pi.B=4,       H.R_pi=8,
p_a(H)=2,       p_a(R_pi)=9,       p_a(H+R_pi)=18.
```

What remains useful in (4.1) is the actual component-class lattice, not its
rank alone.

## 5. Next finite gates and nonclaims

The cheapest positive gate is the `F5` local different at `p_0`: determine
whether a triple-root finite jet can realize one irreducible ramification
branch carrying all eight boundary intersection units, or whether the
different forces multiple branches and hence a cycle.

In parallel, express possible components of `R_pi=2A+B` in the conic-bundle
lattice generated by `A`, `B`, and the nine singular-fibre line classes.
Impose effectivity, adjunction, total class, linear independence from (4.1),
and the exact allowed attachment set for each `F1,F2,F4,F5,F7` type. This is
the honest finite replacement for the dead raw-rank shortcut.

Nonreduced infinity, singular ambient closure, projective coefficient
basepoints, affine coefficient zeros, and target/fibre degree drops remain
separate strata. No general quadratic/cubic block closure, primitivity,
occurrence theorem, first-leg construction, map, counterexample, or JC2
result is promoted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8727`.
- Body SHA-256:
  `f334970e50271ce851c55ec55cfc30ba9f00054b4d81179e437b669350dd878b`.
- Frozen basis: `f89cbb02305ee6fef32a79ccb8ff53fc4740a2a1`.
