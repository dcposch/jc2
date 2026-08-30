# Binding integration: `A1` ruling and Euler boundary cap

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen integration basis: `00b2fb0c682c5ca2a056af588a29b2421c1b7ce4`  
Lifecycle: **BINDING SURFACE-THEORETIC FILTER / QUADRATIC EFFECTIVITY OPEN**

## 0. Evidence and disposition

This integration binds the sealed producer

```text
a2d4a7eef07700983c039d12763d9730efde0f373840e5909a7b6e276f620016
  xmodel/bd-a2-a1-ruling-euler-boundary-cap-sol56-20260830.md
  body 3cb1243350658fc146671cf7723b96c65c6836f8852582e72cd0781546df596d
  manifest a7ad639036f4fe9c286c4d622282505f9df4d68afb10a7cd6a5b9e6df1610bd1
```

to the independently reconstructed GPT-5.5 xhigh hostile review

```text
dddf3463e840845edceca49860b18404ef842fc12931529456bceb0762da1568
  xmodel/bd-a2-a1-ruling-euler-boundary-cap-hostile-review-gpt55-20260830.md
  body 11922 / f6de61b9940677436f5303538c028ebda6c97b7ae56ce77da480cfeba4703941
  receipt 79d0d0161ce15ca7eaa855a6b5a99e8653f454d913ac885e46d0564db86c9ee6
  verdict CONFIRM_WITH_CORRECTIONS
```

The receipt pins unchanged prompt, adapter, launcher, charge validator,
fallacy appendix, composed model prompt, and raw report/log hashes, with
`exit_code=0`, `final_status=DONE`, and launch basis
`b0f4d09cf8b9aa3524247cb746a2610a6e49542f`.  Root independently checked
those hashes before reading the complete 236-line report and then appended
the canonical seal.

The reviewer independently checked the charged first-leg input, affineness,
smoothness, rationality, units, logarithmic Kodaira dimension, the
Miyanishi--Sugie surface theorem and modern formulations, the adapted ruling
class, Noether/Euler calculation, fibre Euler formula, and both sharp
controls.  It found no mathematical gap.  This integration adopts its four
wording repairs: the actual dominant `A2 -> U` morphism is a charged input;
the external theorem is cited in its surface fibration form; ruling-class
equations live only on an adapted completion; and all Euler counts use
distinct reduced support components.

## 1. Binding `A1`-ruling theorem

Let

```text
X subset P2 times P1,       [X]=2A+3B,
H~A,                        R_X~2A+B
```

be a normal irreducible quadratic incidence in the promoted proper cubic-
block first-leg scope.  Define the maximal safe open

```text
U=X minus Supp(H+R_X).                                  (1.1)
```

The proper-block package supplies an **actual charged dominant morphism**

```text
g_1:A2 -> U.                                            (1.2)
```

It is not reconstructed from the compactification and must not be replaced
by its image or by a smaller open.  The following facts hold.

1. `H+R_X~3A+B` is effective ample, hence `U` is affine.
2. `Sing(X) subset Supp(R_X)`, hence `U` is smooth.
3. The resolved conic fibration makes `X`, and therefore `U`, rational.
4. Pullback along (1.2) gives `O(U)^*=C^*`.
5. Pullback of logarithmic pluricanonical forms along the dominant
   generically finite map gives `bar-kappa(U)=-infinity`.

The Miyanishi--Sugie theorem, in the standard surface extension-to-fibration
form recorded for example by Dubouloz--Kishimoto, therefore supplies a
surjective morphism

```text
rho:U -> C                                               (1.3)
```

with general fibre `A1`.  No finite base change is involved.  Rationality
of `U` makes `C` rational.  Pullback injects `O(C)^*` into `O(U)^*`, so the
only possible smooth bases are

```text
C=A1  or  C=P1.                                         (1.4)
```

The complete-base branch is genuine at this level and must not be silently
discarded.

## 2. Adapted completion, not the raw `D9` marking

Resolve boundary base points of the rational extension of (1.3).  On a
resulting smooth strict-SNC completion `(V,D)`, the fibration extends to a
`P1`-fibration.  Its general completed fibre class `L` is primitive, nef,
effective, and basepoint-free and satisfies

```text
L^2=0,          K_V.L=-2,          D.L=1.              (2.1)
```

Exactly one boundary component is horizontal and meets `L` once; every
other boundary component is vertical.  If `C=A1`, the boundary also contains
a complete fibre over the missing point of the completed base, with its
primitive positive multiplicity vector spanning the fibre-intersection
kernel.  If `C=P1`, no complete boundary fibre is forced.

These equations are not licensed on the present minimal `D9` resolution.
Boundary base-point adaptation can be arbitrarily long, as polynomial
rulings `x+y^n` on `A2` already show.  Once an adapted completion is fixed,
the orthogonal boundary lattice is negative definite and the numerical
candidate set is finite, but primitivity, nefness, effectivity, and
semiampleness remain separate tests.  No raw-`D9` ruling enumeration may be
promoted without an adaptation theorem.

## 3. Completion-invariant Euler identity

Let

```text
r = total rank of all Du Val exceptional trees;
c = number of distinct nonexceptional strict components of Supp(H+R_X);
b = number of later point blowups used to make the boundary strict SNC.
```

On the minimal Du Val resolution, adjunction gives `K=-A+B`, hence
`K^2=-1`; rationality and Noether give `e=13` and Picard rank eleven.  The
resolved support of `H+R_X` is a connected rational tree.  After the `b`
boundary blowups,

```text
e(V)=13+b,
N=#Irr(D)=r+c+b,
e(D)=N+1.
```

Thus every later boundary blowup cancels and

```text
e(U)=12-r-c.                                            (3.1)
```

Here `c` counts distinct components of the **reduced support**.  Divisor
multiplicities never enter.  A strict component shared by `H` and `R_X`
would be counted once.  In the separately reviewed reduced, finite-near-
infinity `F5` scope, the local `(h,h_z)` argument excludes common
nonexceptional components.  There

```text
c=3+k,                                                  (3.2)
```

where `k>=1` is the number of distinct nonexceptional irreducible components
of `Supp(R_X)`.  This reduced-support count includes affine ramification
carriers contracted by the Stein map and is independent of their Cartier
multiplicities.

## 4. Fibre Euler formula and exact caps

Every reduced fibre of (1.3) is a disjoint union of affine lines.  If `q_t`
is the number of irreducible components of its reduced support at a
degenerate value, Euler stratification gives

```text
e(U)=e(C)+sum_t(q_t-1).                                 (4.1)
```

All correction terms are nonnegative.  Combining (1.4), (3.1), and (4.1)
gives the binding caps

```text
r+c<=11,                                                (4.2)
C=P1  =>  r+c<=10.                                     (4.3)
```

If `r+c=11`, then `e(U)=1`; necessarily `C=A1`, and every fibre has
irreducible reduced support.  A multiple irreducible fibre is not excluded.
The weak cap (4.2) duplicates the unit/Picard boundary-class injection.  The
new content is the `A1`-fibration, the complete-base sharpening (4.3), the
equality classification, and the adapted second ruling.

In the reviewed `F5` scope, (3.2) turns the cap into

```text
r+k<=8,                                                 (4.4)
C=P1  =>  r+k<=7.                                      (4.5)
```

Consequently `r<=7`; if `k>=2`, then `r<=6`.

## 5. Immediate intersection with the promoted singular-`F5` table

Let `r_0` be the rank of the possible Du Val tree at the unique `F5`
triple/tangency point and let `r_aff` be the total rank of all affine Du Val
trees.  Thus `r=r_0+r_aff`.  Combining (4.4) with the already promoted local
Cartier table gives the exact residual budget

```text
r_aff+k<=8-r_0,                                        (5.1)
```

and, in the complete-base branch,

```text
r_aff+k<=7-r_0.                                        (5.2)
```

The consequences by local type are:

| `p_0` type | `r_0` | general residual `r_aff+k` | exact consequence |
|---|---:|---:|---|
| smooth | 0 | at most 8 | no local-rank kill |
| `A2` | 2 | at most 6 | affine rank plus carriers costs the remaining six |
| `A3` | 3 | at most 5 | same with residual five |
| `A4` or `D4` | 4 | at most 4 | same with residual four |
| `A5` or `D5` | 5 | at most 3 | same with residual three |
| `A6` or `D6` | 6 | at most 2 | `k=2` forces `r_aff=0`; `k=1` leaves at most rank one |
| `A7` | 7 | exactly 1 | `k=1`, `r_aff=0`, base `A1`, every ruling fibre reduced-irreducible |
| `A8` | 8 | impossible | killed because `k>=1` |

For a `P1` base, subtract one more from every residual column.  In
particular `A7` is impossible in that branch, while `A6/D6` force
`k=1,r_aff=0`.  These statements eliminate all promoted `A8` attachment
rows, regardless of their local Cartier vector or exceptional genus
contribution.  They do not eliminate `A7`: its surviving equality cell is
highly rigid but still requires a geometric contradiction.

This table uses only the reviewed local singular-`F5` types.  It does not
charge or pre-promote any still-live carrier/effectivity producer.

## 6. Controls, scope, and next gates

The numerical cap is sharp as a completion invariant: `A2` with nine
boundary blowups has `e(V)=13` and eleven rational boundary components.  The
complete-base branch is also real: for a smooth ample section `S` on a
Hirzebruch surface, `F_n minus S` is a smooth rational affine surface with
constant units and an `A1`-fibration over `P1`, and contains a dense open
`A2`.  That inclusion has generic degree one.  It therefore does not decide
whether the charged proper-block condition `d1>=2` supplies an additional
obstruction.

Promoted here:

```text
direct A1 ruling on U;             base A1 or P1;
e(U)=12-r-c;                       r+c<=11;
P1 base => r+c<=10;                equality classification;
F5 cap r+k<=8;                     A8 local rows eliminated;
A7 equality cell exactly typed;   adapted-completion ruling equations.
```

Not proved: a bounded boundary-adaptation theorem; a ruling class on the raw
`D9` marking; reducedness of the projective ramification Cartier divisor;
effectivity or occurrence of any remaining carrier row; exclusion of the
`P1` base from `d1>=2`; exclusion of all quadratic presentations; existence
of an intermediate block; a polynomial map; a counterexample; or JC2.

The immediate nonblocking successors are:

1. charge (5.1) to every frozen carrier/effectivity row and isolate the
   equality cells without confusing support count with multiplicity;
2. attack the `A7` equality cell via the reduced-fibre structure of the
   second ruling, keeping it distinct from the original conic ruling;
3. seek either a block-specific `d1>=2` obstruction or a degree-at-least-two
   control for the complete-base branch;
4. seek an exact adaptation bound before any raw-`D9` second-ruling lattice
   enumeration.

Review continues asynchronously; none of these successor searches is a
research barrier for the others.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10866`.
- Body SHA-256:
  `a8aa57dc9f1208491b4512321a4bdd2d83e6ce496707299e25a8179916fdf261`.
- Frozen basis: `00b2fb0c682c5ca2a056af588a29b2421c1b7ce4`.
