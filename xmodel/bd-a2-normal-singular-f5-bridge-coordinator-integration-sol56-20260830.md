# Binding integration: reduced finite normal-singular infinity is `F5`

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen integration basis: `7e72f3422017511b400003733807c52d4fbf267a`  
Lifecycle: **BINDING F5 REDUCTION / NORMAL-SINGULAR EFFECTIVITY OPEN**

## 0. Evidence and disposition

This integration binds the transactional producer

```text
413489b037be9533337f53e6bd104549c2ef663c4afd27927230d469ac1b1128
  xmodel/bd-a2-normal-singular-reduced-finite-f5-bridge-sol56-20260830.md
  body 12123 / 7b5ab1f2cc6c2419f9325882f080d22d0cf53e55ae4fd250dfd5aafe80f424f7
  manifest 46028e2beaf995df1988c33cfa137bb485d7da5d003cd63ca844f2ebea377b5e
```

to the independent GPT-5.5 xhigh hostile review

```text
10196c685be7d54b035bc22008efbb225fb7ecaf56ef7dd986d3928e1f8e8e4f
  xmodel/bd-a2-normal-singular-reduced-finite-f5-bridge-hostile-review-gpt55-20260830.md
  body 13050 / 78dc60c0b08e900b57b47c2f153b9f7443755ff3b69472ce417a0d3216964aa7
  receipt 130774ebd11cedf4c40bf0b9a1280af0920351e3f895dbd779a8f99bef370e60
  verdict CONFIRM_WITH_CORRECTIONS
```

The reviewer independently reconstructed the local determinant equation,
common-component exclusion, connected-subtree graph lemma, all `F1`--`F9`
critical-site counts, F5 local invariants, target-line saturation, crepant
delta identity, and complete connected `A/D` Cartier enumeration.  It found
no mathematical gap.  This integration incorporates the requested line-
bundle, graph, positivity, and localization repairs.

The exact setting is a normal irreducible Cartier hypersurface

```text
X subset P2 times P1,      [X]=2A+3B,
pi:X->P2,                  H=pi^*(L_infinity)~A,
R_X~2A+B,
```

inside the promoted proper cubic-block first-leg scope.  Assume `pi` is
generically finite and finite on a neighbourhood of `H`, and `H` is reduced.
Affine ADE singularities are allowed and remain part of the final frontier.

## 1. The boundary critical scheme at normal points

Choose target coordinates `(u,v)` with `L_infinity={u=0}` and a fibre
coordinate `z`.  In a hypersurface frame,

```text
X: f(u,v,z)=0,             H: h(v,z)=f(0,v,z)=0.
```

The normal-singular incidence theorem identifies the reflexive determinant
line with the actual line bundle `O_X(2A+B)` and its determinant section with
the effective Cartier divisor `R_X`.  In this local hypersurface frame the
section is represented by `f_z`.  Therefore, without assuming smoothness at
the point,

```text
H cap R_X = V(h,h_z)                                     (1.1)
```

scheme-theoretically.  This uses the promoted determinant-line
identification; normality alone is not being asked to extend an arbitrary
section.

There is no common nonexceptional component of reduced `H` and `R_X`.  If a
reduced irreducible factor `q` of `h` also divides `h_z`, writing `h=qs`
with `(q,s)=1` gives `q|q_z`.  In characteristic zero, `q_z=0`, so that
component is target-vertical of type `(1,0)`.  Such a component contradicts
finiteness near `H`.  Thus (1.1) is a zero-dimensional critical scheme, and
its support is exactly the physical projection-critical support of

```text
H -> L_infinity.                                       (1.2)
```

## 2. Connected subtrees force one physical site

Let `U` be the charged smooth first-leg open obtained by deleting `H`, the
reduced support of `R_X`, and every other named boundary locus.  It is smooth
because `R_X` contains every singular point of `X`.  Resolve the surface and
the reduced boundary to a strict SNC completion.  The promoted dominant
`A2` first leg forces its full dual multigraph to be a rational forest.

Inside that forest, the reduced total transform of `H` is connected because
reduced bidegree-`(2,3)` infinity is connected.  The reduced total transform
of `Supp(R_X)` is connected because `2A+B` is ample and its support is
connected on the normal projective surface.  The intersection of two
connected subtrees of a tree is connected: two separated joining loci would
give two routes between them and hence a cycle.

Consequently (1.1) has exactly one physical support site.  Shared exceptional
ADE trunks are allowed, but only inside this unique site.  Several distinct
ramification branches may also form a star there.  What is excluded is a
second separated joining site, not reducibility of ramification and not more
than one analytic branch at the unique point.

## 3. The reduced infinity curve is exactly `F5`

Apply the promoted nine-type rational-forest classification of reduced
bidegree-`(2,3)` curves.

* `F8,F9` admit no rational-forest refinement.
* `F3,F6` contain a target-vertical `(1,0)` component and lie outside the
  finite-near-`H` hypothesis.
* The degree-three normalization map in `F1` has total ramification four but
  at most two at one point, hence at least two physical critical sites.
* The exact curve-theoretic patterns `F2,F4,F7` also have two distinct
  projection-critical sites.
* `F5` has one site: a `(0,1)` component and two `(1,1)` components meet
  there, with the latter tangent to order two.

The connected-subtree lemma eliminates every in-scope row except

```text
F5=(0,1)+(1,1)+(1,1).                                 (3.1)
```

At its unique point `p_0`, projective changes give

```text
h(v,z)=z(z-v)((1+v)z-v).                              (3.2)
```

The three smooth branches have pairwise intersection lengths `1,1,2`, so

```text
r_p0(H)=3,       delta_p0(H)=4,
delta_p0-r_p0+1=2.                                    (3.3)
```

As a cubic in `z`, (3.2) has discriminant `v^8`.  Equivalently,

```text
length C[[v,z]]/(h,h_z)=8=H.R_X.                      (3.4)
```

Thus the entire global infinity/ramification intersection is supported at
`p_0`.  This is one critical support site, not one ramification branch or one
global ramification component.

## 4. Exact singular-`F5` Cartier filter

Assume additionally that `p_0` is a Du Val singularity of `X`.  On its
minimal resolution write

```text
r^*H=H'+sum_i h_iE_i,        a_i=H'.E_i,       a=Ch.
```

Because `a` is nonzero and `C^(-1)` is strictly positive on a connected
`A/D` tree, `h=C^(-1)a` is componentwise positive.  Positivity is derived,
not an additional occurrence hypothesis.

Take a generic target line `M` through `pi(p_0)` distinct from infinity.  Its
total transform has exceptional multiplicities `ell_i>=1`.  The identity

```text
3=A.H=M'.H'+ell^t a                                  (4.1)
```

is local at `p_0`; it exhausts the global target-line intersection because
the F5 fibre over `pi(p_0)` is supported at `p_0`.  Every one of the three
analytic branches in (3.2) meets the exceptional fibre, hence
`sum a_i>=3`.  Equation (4.1) gives the reverse inequality, so

```text
sum_i a_i=3.                                          (4.2)
```

The equality is saturated: `M'.H'=0` there and `ell_i=1` on `Supp(a)`.
Each strict boundary branch meets a smooth exceptional point transversely;
an exceptional-node contact or tangency would cost more than one unit.

Crepancy and orthogonality give

```text
delta_p0(H)
  = h^t a/2 + sum_(q over p0) delta_q(H'),
h^t a<=8.                                             (4.3)
```

For a connected tree, imposing (4.2), the exact `A/D` Cartier congruences,
positive integral `h=C^(-1)a`, and (4.3) gives, modulo diagram automorphism,
the complete list:

| type | attachment vector `a` | `h^t a` |
|---|---:|---:|
| `A_r`, `2<=r<=8` | `2e_1+e_(r-1)` and reversal | `6` |
| `A_r`, `4<=r<=8` | `e_1+e_2+e_(r-2)` and reversal | `8` |
| `D_4` | `e_1+e_3+e_4` | `6` |
| `D_5` | `e_1+2e_4` up to spin reversal | `8` |
| `D_6` | `e_1+e_5+e_6` | `8` |

For `A_2`, the first row reads `3e_1` up to reversal; for `A_4`, the second
reads `e_1+2e_2`.  `A_3` retains the two distinct global embedding tags
`B_4` and `U_3`, although its local Cartan row is the same.  `A_1` and
`D_7,D_8,D_9` are excluded only at the singular F5 point.  They remain
available at affine ramification singularities.

When `h^t a=8`, the minimal surface resolution already separates and
smooths the three strict infinity branches above `p_0`.  When it is six, one
unit of curve delta remains upstairs for the later embedded resolution.  The
table is a list of necessary local Cartier rows, not analytic occurrence.

## 5. Maximum promoted theorem and remaining frontier

In the charged normal exact-quadratic presentation, reduced infinity plus
finiteness near infinity forces the unique F5 pattern (3.1), and all eight
infinity/different units occur at its one triple/tangency point.  This
strengthens the older smooth irreducible-ramification dichotomy: reducible
ramification and affine ADE singularities do not evade the one-site graph
argument.

It does **not** close the normal-singular quadratic stratum.  The F5 point may
be smooth; if so, only the separately promoted smooth local `5+3` different
split applies there.  If it is Du Val, the table in Section 4 applies, while
all affine ADE trees and their ramification vectors remain live.  No row is
asserted to occur.

The next finite client is global carrier/effectivity:

1. retain every affine ADE tree and its `(m,n)` ramification data;
2. distinguish smooth and singular `p_0`, carrying the exact local F5 data;
3. place the three F5 strict carriers and every exceptional tree in the
   actual nine-blowup ruled marking inside `D9(-1)`;
4. decompose the strict support of `R~2A+B`, preserving multiplicities,
   physical contacts, target images, fibre weights, and common-carrier flags;
5. impose effectivity, irreducibility, unit/class-group independence, exact
   intersections, and the full rational-forest connector rule.

The reviewed 115-signature global fibre theorem supplies the abstract
vertical skeleton for this client.  It remains distinct from an effective
configuration.  Nothing here proves quadratic-basis existence, excludes
higher coefficient degree or higher block degree, constructs an etale first
leg or a polynomial map, gives a counterexample, or proves JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9993`.
- Body SHA-256:
  `9cef2390e268239432520b79ccfe868f38cb384d3f2d995ddc3f55ca5208b05d`.
- Frozen basis: `7e72f3422017511b400003733807c52d4fbf267a`.
