# Coordinator integration: F5 local different splits `8=5+3`

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `1efd7a76538e3fcdf51b999563262afc40d58947`  
Lifecycle: **BINDING INTEGRATION / SMOOTH F5 LOCAL SCOPE**

## 0. Disposition and custody

Opus 5 independently reconstructed the sealed producer

```text
8a1c3c50281a9c55b4dcf21c7c5a33ef574b4bfc59d10eb18456528171bbbb72
  xmodel/bd-a2-f5-local-different-two-branch-producer-sol56-20260830.md
  body 9253 / 61931ec73f0b6bd13cfef1d75e9c6c4bdd6d36a2364631b898131f66b19aa897
```

and returned `CONFIRM_WITH_CORRECTIONS`. Its sandbox-attested raw review body
is

```text
5a77b09861b3e53c480715399d777db58290ce60466cb4485f5c25f1c4f5b035
  xmodel/bd-a2-f5-local-different-two-branch-hostile-review-opus5-20260830.md
```

and its sealed full-file SHA-256 is
`7e335e1a1636d1b4342cf0f163fd7051c33b38b3c16766f8c7d94f92e5beea0c`.
The clean schema-v2 receipt has exit code zero and pins unchanged prompt,
adapter, launcher, Seatbelt profile, validator, fallacy appendix, and composed
model-prompt hashes.

Nothing is refuted and no gap remains. The material correction is notational:
the producer's displayed equations `z=v` and `3z=v` are tangent lines, not the
actual Hensel branches. This integration reserves `T_tan,T_tr` for those
lines and `D_tan,D_tr` for the analytic branches. It also makes the initial
unit division, no-common-branch check, boundary-graph monotonicity, and full
global hypotheses explicit.

## 1. Exact F5 normal form

Let `H` be a reduced class-`(2,3)` divisor on `P1 x P1` of type

```text
F5=(0,1)+(1,1)+(1,1).
```

Its three smooth rational components meet only at one point `p`; the two
`(1,1)` components have contact two and each meets the `(0,1)` component
transversely. There is no hidden modulus. After allowable projective changes,
local coordinates `(v,z)` at `p` put the three branches in the exact form

```text
H_0: z=0,
Q_1: z-v=0,
Q_2: (1+v)z-v=0,

h(v,z)=z(z-v)((1+v)z-v).                            (1.1)
```

The nonzero common derivative of `Q_1,Q_2` follows from their Mobius graph
structure and transversality to `H_0`; contact two gives equality of those
derivatives. Conjugating the first graph to the identity leaves the second as
`v/(1+gamma v)`, `gamma!=0`, and a common scaling sets `gamma=1`.

Let `X` be smooth near `p`, let `u=0` be the target infinity line, and let
`pi:X->P2` be the degree-three projection. First divide the local defining
equation by the unit multiplying its restriction to `u=0`. On `X`, this
multiplies the relative derivative only by a unit. The equation is then

```text
f(u,v,z)=h(v,z)+u*g(u,v,z),             g(0,0,0)!=0. (1.2)
```

Smoothness forces the displayed unit condition because every first derivative
of `h` vanishes at the triple point.

## 2. Two coefficient-independent different branches

Solving (1.2) gives `Ohat_{X,p}=C[[v,z]]` and `u=U(v,z)` of order exactly
three. The source Cartier ramification/different is

```text
R_pi=div(f_z|X),
r(v,z)=h_z(v,z)+U(v,z)g_z(U(v,z),v,z).
```

Since the second term has order at least three,

```text
in_2(r)=3z^2-4vz+v^2=(z-v)(3z-v).                  (2.1)
```

Write

```text
T_tan: z=v,                  T_tr: 3z=v
```

for these distinct tangent lines. Weierstrass preparation and the quadratic
formula over `C[[v]]` factor `r` uniquely up to units as

```text
r=unit*(z-xi_tan(v))*(z-xi_tr(v)),
xi_tan=v+O(v^2),             xi_tr=v/3+O(v^2).
```

Thus `D_tan,D_tr`, defined by those two factors, are exactly two reduced
smooth analytic branches, transverse to each other, for every unit `g`.
The local different is reduced at `p`; neither tangent line itself is being
substituted for its Hensel branch.

## 3. Exact intersection split

The ideal of `H` in `C[[v,z]]` is `(U)=(h)`, and `r=h_z mod h`. Hence

```text
I_p(H,R_pi)=length C[[v,z]]/(h,h_z).                (3.1)
```

As a cubic in `z`, `h` has leading coefficient `1+v` and roots
`0,v,v/(1+v)`. Therefore

```text
disc_z(h)=v^8                                      (3.2)
```

exactly, while the resultant differs by a unit. The monic
resultant/length identity gives `I_p(H,R_pi)=8`.

There is no common branch: direct restriction gives orders

```text
ord_v(r|H_0)=2,      ord_v(r|Q_1)=3,
ord_v(r|Q_2)=3.
```

Thus intersection additivity is licensed. `D_tr` has tangent distinct from
all three tangents of `H`, so its three contributions are exactly
`(1,1,1)`. `D_tan` is transverse to `H_0` and tangent to both `Q_i`, so its
contributions are at least `(1,2,2)`. The exact total eight forces equality:

```text
                  H_0   Q_1   Q_2   total
D_tan              1     2     2      5
D_tr               1     1     1      3
                                      ---
                                       8.           (3.3)
```

This is an exact floor-plus-complement argument: it is sound because the
`D_tr` side and total are equalities, not because two lower bounds attain.

The restriction of the target trace discriminant is `v^8` up to a unit by
the norm formula. That is a consistency restatement of the same different
calculation, not independent evidence and not an identification of target
and source branches. Source different, its reduced support, target
discriminant, reduced branch, normalization index, and conductor remain
distinct.

## 4. Binding global consequence

Now assume `X` is smooth and irreducible of class `2A+3B`, `pi` is finite on
a neighborhood of the reduced `H`, and the promoted dominant `A2->U`
first-leg hypotheses hold. The promoted attachment theorem supplies
nonempty reduced affine ramification and excludes irreducible ramification
in `F1,F2,F4,F7`; finiteness excludes `F3,F6`, while `F8,F9` have no forest
refinement.

In F5, neither local different branch lies in `H`, and (3.1)--(3.3) exhaust
the global intersection `H.R_pi=8`, so no additional boundary attachment
exists. If `D_tan,D_tr` belong to one global irreducible `Rbar`, they give
two normalization points over `p`; the attachment-cycle lemma produces a
cycle already in `H union Rbar`. Any resolution of the full boundary
contains a subdivision of that graph, and subsequent subdivision or
vertex/edge addition cannot lower its first Betti number. If the germs lie
on distinct global components, both meet the affine part and `R_red` is
reducible.

Consequently the maximum promoted composition is

```text
smooth irreducible class-(2A+3B) incidence,
pi finite near reduced squarefree infinity,
dominant promoted A2 first leg
    => R_red is nonempty and has at least two components.       (4.1)
```

The next finite gate is the actual conic-bundle component lattice with
boundary degrees five and three. Equation (4.1) does not eliminate reducible
ramification or F5, realize any coefficient tuple, or assert occurrence.

No nonreduced/singular/basepoint/degree-drop stratum, general quadratic or
cubic block, primitivity statement, map, counterexample, or JC2 conclusion is
promoted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6988`.
- Body SHA-256:
  `2d14c7fa9675d41eaaf208e10c2dc4e72e596fa6fbf9503350dd18295abe0787`.
- Frozen basis: `1efd7a76538e3fcdf51b999563262afc40d58947`.
