# Hostile review: reduced finite normal-quadratic F5 bridge

Verdict: `CONFIRM_WITH_CORRECTIONS`.

Custody note.  The working `HEAD` is the requested frozen basis
`06d8f99967ffb3ce34145d30f1e27e23dd07331b`.  The reviewed packet is not in
that commit tree, but the worktree file matches the charged full SHA-256
`413489b037be9533337f53e6bd104549c2ef663c4afd27927230d469ac1b1128`,
body length `12123`, and body SHA-256
`7b5ab1f2cc6c2419f9325882f080d22d0cf53e55ae4fd250dfd5aafe80f424f7`.
The five Section 0 integrations match their printed SHA-256 values.

## 1. Local ramification at normal singular points

Verdict: `CONFIRM_WITH_CORRECTIONS`.

The local calculation is correct.  In a fibre chart of
`P2 times P1`, with `L_infinity={u=0}` and fibre coordinate `z`, the
hypersurface equation `f(u,v,z)=0` gives

```text
O_H = C[[v,z]]/(h),       h(v,z)=f(0,v,z).
```

On the smooth locus of `X`, the kernel of `d pi` is the vertical tangent, so
the Jacobian determinant is represented by `f_z`.  The normal-singular
integration already promotes the determinant section as a global section of
`omega_X tensor pi^*omega_P2^(-1)=O_X(2A+B)`, with zero divisor the effective
Cartier divisor `R_X` (`bd-a2-normal-singular-quadratic-incidence-coordinator-integration-sol56-20260830.md:207-227`).
Restricting the local Cartier equation to `u=0` gives

```text
H cap R_X = V(h,h_z)
```

scheme-theoretically, including singular points of `H`.

The common-component argument is also correct after spelling out its generic
component scope.  If an irreducible reduced factor `q` of `h` is a component
of `R_X|_H`, then `q | h_z`.  Writing `h=qs` with `(q,s)=1` gives
`q | q_z`; in characteristic zero this forces `q_z=0`, so the component is
target-vertical, i.e. a `(1,0)` component of the bidegree `(2,3)` infinity
curve.  That is incompatible with finiteness of `pi` on a neighbourhood of
`H`, as in the smooth attachment integration
(`bd-a2-quadratic-ramification-attachment-coordinator-integration-sol56-20260830.md:68-71`,
`:97-102`).

Repair required.  Replace the packet's wording "normality extends that
section" (`...f5-bridge-sol56-20260830.md:83-85`) by the stronger statement:
the determinant is a section of the reflexive determinant line, the
normal-singular integration identifies that line with `O_X(2A+B)`, and in the
chosen hypersurface frame its local equation is `f_z`.  This avoids making
normality alone carry the extension.  No smoothness of `X` at the point,
flatness of `pi`, or purity of a branch divisor is being used; the real
inputs are normal Cartier hypersurface, characteristic zero, generically
finite separability, reduced `H`, and finiteness near `H`.

## 2. Connected transforms and one support site

Verdict: `CONFIRM_WITH_CORRECTIONS`.

The graph step is valid, but only in the precise reduced SNC boundary graph
of the first-leg open surface.  The first-leg integration applies to a smooth
quasi-projective `U` dominated by `A2` and gives rational components and a
forest dual multigraph for any strict SNC completion
(`bd-a2-rational-forest-coordinator-integration-sol56-20260830.md:40-72`).
Here `U` must be stated explicitly as the first-leg open obtained from the
normal surface by deleting `H`, the reduced ramification support, and the
charged boundary loci.  Since `R_X` contains every singular point of `X`
(`bd-a2-normal-singular-quadratic-incidence-coordinator-integration-sol56-20260830.md:236-240`),
this open is smooth after those deletions.

In that forest, the reduced total transform of `H` is connected by the
reduced `(2,3)` theorem (`bd-a2-bidegree23-rational-forest-classification-coordinator-integration-sol56-20260830.md:51-65`),
and the reduced total transform of `Supp(R_X)` is connected by ampleness of
`2A+B` on the normal projective surface
(`bd-a2-normal-singular-quadratic-incidence-coordinator-integration-sol56-20260830.md:214-240`).
Two connected subgraphs of a forest cannot have two disconnected intersection
or joining loci.  Thus two separated physical points of `H cap Supp(R_X)`
would create a cycle: the path inside the `H` transform and the path inside
the `R` transform give two routes between the sites.

This remains true for reducible ramification and affine singular trees.  If
the two sites are singular points of `X`, the corresponding ADE exceptional
trees are disjoint shared subtrees, impossible as the intersection of two
connected subtrees of a tree.  If one or both sites are smooth contacts, the
same argument gives parallel connections after contracting internal trees.
Shared exceptional trunks at a single physical point are one site, not many.
Multiple ramification branches at that one site are not excluded; the
promoted connector rule explicitly allows a star when different outside
carriers are connected only through the local contact tree
(`bd-a2-ade-decorated-threat-map-coordinator-integration-sol56-20260830.md:171-183`).

Repair required.  State the graph lemma as a connected-subtree lemma in the
full reduced SNC boundary.  Also replace "common strict carrier would be the
only escape" (`...f5-bridge-sol56-20260830.md:120-122`) by: a common
nonexceptional `H/R` carrier is excluded by the `h_z` factor argument; shared
exceptional ADE components are allowed only as part of the unique physical
site.

## 3. F1--F9 projection-critical typing

Verdict: `CONFIRMED`.

The intrinsic projection-critical counts survive the passage from smooth
`X` to a normal Du Val surface because they are counts on the reduced
bidegree `(2,3)` curve `H`, not on the ambient surface.

`F8,F9` never have rational-forest refinements
(`bd-a2-bidegree23-rational-forest-classification-coordinator-integration-sol56-20260830.md:71-104`).
`F3,F6` contain a target-vertical `(1,0)` component and are therefore outside
the finite-near-`H` scope, not killed inside it
(`bd-a2-bidegree23-rational-forest-classification-coordinator-integration-sol56-20260830.md:132-143`;
`bd-a2-quadratic-ramification-attachment-coordinator-integration-sol56-20260830.md:68-71`).

For `F1`, the normalization is `P1` and its projection to `L_infinity` has
degree three.  Riemann-Hurwitz gives total ramification four, while a single
point in a degree-three map contributes at most two.  Hence there are at
least two normalization-critical points, and in the classified `F1` rows
they are not one physical point.  For `F2,F4,F7`, the imported smooth
attachment calculation gives two distinct physical critical sites
(`bd-a2-quadratic-ramification-attachment-coordinator-integration-sol56-20260830.md:112-118`).
The new connected-transform argument above removes the old need for
irreducible `R_red`; the smooth integration's final theorem had only proved
the narrower irreducible-ramification dichotomy
(`bd-a2-quadratic-ramification-attachment-coordinator-integration-sol56-20260830.md:120-147`).

`F5` has exactly one projection-critical support site.  In the local form
`h=z(z-v)((1+v)z-v)`, the three smooth branches have pairwise intersection
lengths `1,1,2`, so `delta=4`, `r=3`, and `delta-r+1=2`.  The discriminant
order, equivalently `length C[[v,z]]/(h,h_z)`, is
`2(1+1+2)=8`; this is the global intersection
`H.R_X=A.(2A+B)=8`.  Therefore all eight boundary ramification units are
supported at the unique F5 triple/tangency point.

## 4. Singular F5 point and local Cartier rows

Verdict: `CONFIRM_WITH_CORRECTIONS`.

Assume the F5 point `p0` is Du Val.  On the minimal resolution write
`r^*H=H'+Z`, `Z=sum h_iE_i`, and `a_i=H'.E_i`.  Because the Cartier pullback
is orthogonal to the exceptional curves, `a=Ch`.  The positivity
`h_i>0` is a consequence of `a nonzero` and positivity of the inverse Cartan
matrix, not an independent starting hypothesis.

For a generic target line `M` through `pi(p0)` distinct from `L_infinity`,
`r^*M=M'+sum ell_iE_i` with `ell_i>=1`.  Since `M` meets `L_infinity` only at
`pi(p0)` and the F5 fibre over that point is the triple root at `p0`,

```text
3 = A.H = M'.H' + ell^t a.
```

All terms are nonnegative.  Each of the three analytic branches of `H`
through the singular surface point has strict transform meeting the
exceptional fibre, contributing at least one to `sum a_i`.  Thus
`sum a_i>=3`, while `ell_i>=1` gives `sum a_i<=3`; hence `sum a_i=3`.
The same equality forces saturation: `M'.H'=0` and `ell_i=1` on the support
of `a`.  A branch through an exceptional node or tangent to an exceptional
component would contribute more than one and is excluded by this equality.

The delta identity is correct.  Crepancy and orthogonality give

```text
p_a(H)-p_a(H') = -Z^2/2 = h^t C h/2 = h^t a/2.
```

Since `H` and `H'` have the same irreducible components and normalizations,
and `p0` is the only singular point of `H` in the F5 finite scope,

```text
delta_p0(H) = h^t a/2 + sum_{q over p0} delta_q(H').
```

With `delta_p0(H)=4`, this gives `h^t a<=8`.

The finite exact enumeration agrees with the packet.  For connected local
ADE trees, with `sum a=3`, `h=C^{-1}a in Z_{>0}^r`, and `h^t a<=8`, the
complete list modulo diagram automorphism is:

| type | local vector `a` | `h^t a` |
|---|---:|---:|
| `A_r`, `2<=r<=8` | `2e_1+e_(r-1)` and reversal | `6` |
| `A_r`, `4<=r<=8` | `e_1+e_2+e_(r-2)` and reversal | `8` |
| `D_4` | `e_1+e_3+e_4` | `6` |
| `D_5` | `e_1+2e_4` and spin reversal | `8` |
| `D_6` | `e_1+e_5+e_6` | `8` |

Specializations are as printed: for `A_2`, the first row is `3e_1` up to
reversal; for `A_4`, the second row is `e_1+2e_2` up to reversal.  `A_3`
has the same local Cartan row in both global `D9` embedding tags, balanced
`B_4` and unbalanced `U_3`; these tags are carrier/effectivity data, not
extra local vectors.  `A_1` fails integrality, and the minimum `D_r` value
for `r>=7` is already at least ten.  The packet correctly excludes `A1` and
`D7,D8,D9` only at the singular F5 boundary point, not at affine
ramification singularities.

Repair required.  Section 3 should explicitly derive `h_i>0` from
`a=Ch` and the inverse Cartan matrix, and it should mark the target-line
identity as local at `p0` plus global only because the F5 fibre over
`pi(p0)` is supported at `p0`.  This prevents a hidden generic-line or
attainment assumption.

## 5. Correction and maximum theorem

Verdict: `CONFIRMED`.

The packet correctly enforces the recent correction: ADE trees on affine
ramification remain live.  The theorem does not close the normal-singular
stratum, does not assert that the F5 point is singular, and does not import
the old smooth global F5 lattice when `X` has singularities elsewhere
(`...f5-bridge-sol56-20260830.md:35-39`, `:165-167`, `:290-313`).
This is consistent with the normal-singular firewall: local Cartan vectors
and caps are necessary data, not occurrence or effectivity certificates
(`bd-a2-ade-decorated-threat-map-coordinator-integration-sol56-20260830.md:124-133`,
`:167-214`).

Promotion-ready maximum theorem:

Let `X subset P2 times P1` be an irreducible normal Cartier hypersurface of
class `2A+3B` over `C`, in the charged proper cubic-block first-leg scope.
Assume `pi:X->P2` is generically finite and finite on a neighbourhood of
`H=pi^*(L_infinity)`, that `H` is reduced of bidegree `(2,3)`, and that the
first-leg open obtained by deleting `H`, `Supp(R_X)`, and the charged
boundary loci admits the dominant rational `A2` first leg.  Then `R_X` is the
effective Cartier ramification divisor of class `2A+B`, locally represented
by `f_z`; `H cap R_X` is `V(h,h_z)`; `H` and `R_X` have no common component;
and the projection-critical support of `H->L_infinity` has exactly one
physical site.  Consequently the reduced rational-forest infinity type is
exactly

```text
F5 = (0,1)+(1,1)+(1,1),
```

and the full length `H.R_X=8` is supported at its unique triple/tangency
point.

If that F5 point is Du Val, then its connected local infinity Cartier vector
satisfies `sum a=3`, `h=C^{-1}a in Z_{>0}`, and `h^t a<=8`, and the only
local rows are the `A_2`-`A_8`, `D_4`-`D_6` rows listed above, with the two
global `A_3` embedding tags retained.  No listed row is asserted to be
analytically or globally realized.

Exact next carrier/effectivity problem:

Keep every affine ADE tree and its ramification Cartier vector.  If `p0` is
smooth, keep the local F5 `3+5` different split only as a local smooth-point
input.  If `p0` is singular, use the table above and account for the remaining
`0` or `1` unit of strict-boundary delta upstairs.  Then place all exceptional
trees in the actual nine-blowup ruled marking with root lattice inside
`D9(-1)`, decompose the strict carriers of `R~2A+B` and the three F5 infinity
carriers, impose effectivity, irreducibility, unit/class-group independence,
proper intersections, and the physical forest connector rule.  That global
carrier/effectivity problem is the surviving finite client.

No `FALLACY-v2` violation is needed to rescue the proof: no representative is
used as an attained full exit, no capped row is promoted to occurrence, and
no affine ADE tree is silently deleted.  No new exit-price assertion is made.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13050`.
- Body SHA-256:
  `78dc60c0b08e900b57b47c2f153b9f7443755ff3b69472ce417a0d3216964aa7`.
- Frozen basis: `06d8f99967ffb3ce34145d30f1e27e23dd07331b`.
