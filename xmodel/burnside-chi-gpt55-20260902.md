# BURNSIDE-CHI: S4 subgroup-lattice chi_c table at the N=4 profile

Lane: BURNSIDE-CHI  
Date: 2026-09-02 UTC  
Agent: GPT-5.5 / Codex  
Disposition: **COLLAPSE CONFIRMED AT THE PINNED N=4 PROFILE**  

## 0. Custody and answer

The frozen inputs were hashed before reading. The stop condition did not fire.

```text
2ad20b4c37128533ef23e956c2921aeb70d830bd6166a11b95a6ef6637cc5eff  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.hELKJd/inputs/ideation-20260902T0022Z-fable5.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.hELKJd/inputs/rep-96-inner-opus5-20260901.md
bdd857c9d8c55fa000fcffee05f9f3084c5d073fb4d06285edf2af0d3c369339  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.hELKJd/inputs/reducible-all-n-r2-opus5-20260901.md
```

Question: does the full eleven-row `S_4` subgroup-lattice `chi_c` system at
the pinned profile produce an integer relation on `(s_1, sigma_2, j)` beyond
the already collapsed `chi_2 + sigma_2 = 1`?

Answer: **no**.  After the local fixed-locus census is assembled in the Galois
closure, every subgroup row is a function only of the already pinned `D_1`
node count `s_1`.  The companion variables `(chi_2, sigma_2, j)` cancel from
`chi_c(X^e)` and never appear in `chi_c(X^g)` for `g != e`, because `D_2` is
the trivial-dicritical component and has identity generic inertia.  The
point-stabilizer/source-hull row, computed with the typed
`a_i = N - W_i` deficit bookkeeping, gives exactly

```text
chi_2 + sigma_2 = 1.
```

No integrality row adds a congruence or equality.  With the realized
`(9,6,2)` curve, `s_1 = 4`, and the eleven row values are

```text
36, 15, 22, 12, 11, 15, 8, 3, 6, 5, 1
```

in the subgroup order listed in SS3 below.

Typed outcome: **retire BURNSIDE-CHI as a "more Euler identities" gate for
this N=4 residual profile.**  The sign row and the `S_3` resolvent row remain
valid controls, not new gates.

No exit-price assertion is made here, so no `charge_basis=` line is declared.

## 1. Inputs consumed

Card A defines the mechanism: for `G <= S_N`, the Galois closure `Xhat`
has intermediate quotients `Y_H = Xhat/H`, the target row `Y_G` has
`chi_c = 1`, the point-stabilizer row is the finite hull of the source, and
the source row must consume the typed `a_i = N - W_i` and `a_p` census rather
than a `#Fix` substitution
(`ideation-20260902T0022Z-fable5.md:80-90`).  The fixed-locus vector
`chi_c(Xhat^g)` is then assembled over branch strata, and

```text
chi_c(Xhat/H) = (1/|H|) sum_{h in H} chi_c(Xhat^h)
```

is the row formula (`ideation...:92-108`).  Card A asks for the eleven-row
`S_4` table at the profile `core (2,1,0), W=(1,2), D_1=(9,6,2), D_2` unknown
(`ideation...:255-276`).

The realized `D_1` census is exact.  The `(9,6,2)` curve has normalization
`A^1`, affine semigroup `<2,9>`, `delta_aff = 4`, and four affine nodes
(`rep-96-inner-opus5-20260901.md:72-84`).  The node verification is direct:
the four node images come from the four `{t,-t}` pairs with `p(t)=0`, and
there are no other affine singularities (`rep-96...:109-125`).  The same
report records the complete vertical factorization census, but the Euler
calculation below needs only the ordinary-node count and the local cluster
types (`rep-96...:127-141`, `600-616`).

The reducible profile data are the binding source-row data.  The N=4 residual
profile is a single row: core `(2,1,0)`, `W=(1,2)`, one branched component
`D_1` of weight `2`, and one trivial-dicritical component of weight `1`
(`rep-96...:661-670`; `reducible-all-n-r2-opus5-20260901.md:424-429`).
The profile gives `a^(1)=2`, `a^(2)=3`, and the local point census

```text
D_1 node:          clusters 2 + 2,     a_p = 0
D_1 cap D_2 point: clusters 2 + 1,     a_p = 1
D_2 node:          clusters 1 + 1,     a_p = 2
```

with `D_1` having `s_1` nodes and normalization `A^1`, `D_2` having
`sigma_2` nodes and `chi_c(D_2)=chi_2`, and `j` transverse intersection
points (`rep-96...:688-708`).  The older natural-action identity collapses
there to `chi_2 + sigma_2 = 1`, with `s_1` cancelling identically
(`rep-96...:700-705`).

I used the r2 label hygiene: the cycle-type law includes trivial carriers
as `1`-cycles, while `a_i=N-W_i` is not the same object as the fixed-letter
count in a coarse label (`reducible-all-n-r2...:270-280`).  This is the
separation used below: source/hull Euler uses typed deficits; Galois
fixed-locus multiplicities use inertia stabilizers.

## 2. Local strata and inertia

Let the element classes of `S_4` be ordered as

```text
1, T=(2,1,1), V=(2,2), C3=(3,1), C4=(4).
```

Their class sizes are

```text
|1|=1, |T|=6, |V|=3, |C3|=8, |C4|=6.
```

Write `s=s_1`.  Before pinning the realized curve, keep `s` symbolic; the
realized curve later sets `s=4`.

The target stratification is:

| target stratum | `chi_c` | local inertia in `S_4` |
|---|---:|---|
| `U = C^2 - (D_1 cup D_2)` | `s - chi_2 + j` | `1` |
| smooth open part of `D_1` | `1 - 2s - j` | `<(12)>` |
| smooth open part of `D_2` | `chi_2 - sigma_2 - j` | `1` |
| node of `D_1` | `s` points | `<(12),(34)>` |
| transverse `D_1 cap D_2` point | `j` points | `<(12)>` |
| node of `D_2` | `sigma_2` points | `1` |

The entries need a short check:

* `chi_c(D_1)=1-s`, because the normalization is `A^1` and each node
  identifies two preimages to one point.
* Therefore `chi_c(D_1^sm open)=chi_c(D_1)-s-j=1-2s-j`.
* `chi_c(C^2-(D_1 cup D_2))=1-chi_c(D_1 cup D_2)
  =1-((1-s)+chi_2-j)=s-chi_2+j`.
* `D_2` is the trivial-dicritical component at the generic point, hence
  identity inertia.  Its typed deficit is still `a^(2)=3`; that is source
  bookkeeping and is not substituted into the Galois fixed-locus count.

For a stratum with inertia subgroup `I`, the number of points in the fibre of
`Xhat^g` over that stratum is the number of fixed cosets of `g` on `S_4/I`:

```text
m_I(g) = #{aI : g aI = aI}
       = |C_{S_4}(g)| * |I cap Cl(g)| / |I|.
```

For the three inertia groups occurring above:

| inertia `I` | `m_I(T)` | `m_I(V)` | `m_I(C3)` | `m_I(C4)` |
|---|---:|---:|---:|---:|
| `1` | 0 | 0 | 0 | 0 |
| `<(12)>` | 2 | 0 | 0 | 0 |
| `<(12),(34)>` | 2 | 2 | 0 | 0 |

Thus the nonidentity fixed-locus vector is

```text
f_T = chi_c(Xhat^T) = 2(1 - 2s - j) + 2j + 2s = 2(1-s),
f_V = chi_c(Xhat^V) = 2s,
f_C3 = 0,
f_C4 = 0.
```

The identity entry can either be read from the same stratum table or from the
target row.  The direct stratum assembly is:

```text
f_1 =
  24(s - chi_2 + j)
+ 12(1 - 2s - j)
+ 24(chi_2 - sigma_2 - j)
+  6s
+ 12j
+ 24 sigma_2
= 12 + 6s.
```

This is the first visible degeneracy: `chi_2`, `sigma_2`, and `j` cancel before
any subgroup row is formed.  The fixed-locus class function is therefore

```text
(f_1, f_T, f_V, f_C3, f_C4)
  = (12+6s, 2(1-s), 2s, 0, 0).
```

At the realized `D_1`, `s=4`, so

```text
(f_1, f_T, f_V, f_C3, f_C4) = (36, -6, 8, 0, 0).
```

Negative compactly supported Euler characteristic for `Xhat^T` is not an
error: the fixed curve over the open part of `D_1` has
`chi_c=2(1-s)` after the node identifications are included.

## 3. Eleven subgroup rows

For a subgroup `H <= S_4`, put

```text
chi_H = chi_c(Xhat/H)
      = (1/|H|) (f_1 + n_T(H) f_T + n_V(H) f_V),
```

since the `C3` and `C4` fixed-locus entries vanish.  Here `n_T(H)` and
`n_V(H)` are the numbers of transpositions and double transpositions inside
`H`.

A short exact enumeration of `S_4` as tuples produced all 30 subgroups and
the 11 conjugacy classes.  It also computed the subgroup-class row matrix
over `QQ`.  The full subgroup-average matrix has rank `5` on all element
classes and rank `3` on the actually supported columns `(1,T,V)`.  Those
rank figures are audit data only; the row formulas below are the load-bearing
calculation.

| row | subgroup class `H` | `|H|` | `n_T` | `n_V` | `chi_c(Xhat/H)` | at `s=4` |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `1` | 1 | 0 | 0 | `12 + 6s` | 36 |
| 2 | `C2_T = <(12)>` | 2 | 1 | 0 | `7 + 2s` | 15 |
| 3 | `C2_V = <(12)(34)>` | 2 | 0 | 1 | `6 + 4s` | 22 |
| 4 | `C3` | 3 | 0 | 0 | `4 + 2s` | 12 |
| 5 | `C4` | 4 | 0 | 1 | `3 + 2s` | 11 |
| 6 | `V4_norm = {1,V,V,V}` | 4 | 0 | 3 | `3 + 3s` | 15 |
| 7 | `V4_split = <(12),(34)>` | 4 | 2 | 1 | `4 + s` | 8 |
| 8 | `S3` point stabilizer | 6 | 3 | 0 | `3` | 3 |
| 9 | `D8` Sylow 2 / pair-partition stabilizer | 8 | 2 | 3 | `2 + s` | 6 |
| 10 | `A4` | 12 | 0 | 3 | `1 + s` | 5 |
| 11 | `S4` | 24 | 6 | 3 | `1` | 1 |

Every row is integral for every integer `s`.  In particular, after pinning
`s=4`, integrality imposes no congruence at all.

The two pinned rows are visible in the table:

* `H=S4` gives `chi_c(Y_G)=1`, the target `C^2`.
* `H=S3` gives `chi_c(Y_{H_1})=3`, the point-stabilizer finite hull row.

The target row also checks the class-function arithmetic:

```text
(1/24) ((12+6s) + 6*2(1-s) + 3*2s) = 1.
```

## 4. Point-stabilizer/source-hull comparison

The point-stabilizer row must be compared to the source hull, not to a
generic fixed-letter count.  The finite hull is the source `C^2` plus the
boundary curve over the escaping sheets.  The boundary count is obtained from
the typed deficits and cluster decomposition.

At a generic point of `D_1`, two sheets escape as one size-2 boundary cluster;
at a generic point of `D_2`, one sheet escapes as one size-1 boundary cluster.
At special points the boundary cluster counts are:

```text
D_1 node:          2 boundary points   (two size-2 clusters, a_p=0)
D_1 cap D_2 point: 2 boundary points   (one size-2 and one size-1 cluster, a_p=1)
D_2 node:          2 boundary points   (two size-1 clusters, a_p=2)
```

Therefore

```text
chi_c(C_boundary)
  = (1 - 2s - j)
  + (chi_2 - sigma_2 - j)
  + 2s
  + 2j
  + 2 sigma_2
  = 1 + chi_2 + sigma_2.
```

The source-hull value is

```text
chi_c(Y_{H_1}) = chi_c(C^2_source) + chi_c(C_boundary)
               = 1 + (1 + chi_2 + sigma_2)
               = 2 + chi_2 + sigma_2.
```

The quotient table gives the same row as `3`.  Equating the two gives

```text
2 + chi_2 + sigma_2 = 3
chi_2 + sigma_2 = 1.
```

This is exactly the collapsed relation already recorded in the source note.
It contains no `s` and no `j`.  The cancellation is structural:

* the two `D_1` node effects cancel between the open part of `D_1` and the
  two boundary points at each `D_1` node;
* the two intersections with `D_1` and `D_2` cancel the removals of those
  points from the two open curves;
* the two `D_2` node boundary points convert
  `chi_2 - sigma_2` into `chi_2 + sigma_2`.

No row other than the point-stabilizer row even contains the companion
topology after the fixed-locus vector has been assembled.

## 5. Independent controls

### 5.1 Sign row

The sign row is `H=A4`, the kernel of `sgn:S_4 -> C_2`.  The table gives

```text
chi_c(Xhat/A4) = 1 + s.
```

Independently, this quotient is the double cover of the target branched over
the odd-meridian part.  Here the odd generic meridian is the `D_1`
transposition; the trivial-dicritical component `D_2` is even/identity at the
generic point.  Thus the branch curve for the sign cover is just `D_1`.

For a degree-2 cover branched over `D_1`,

```text
chi_c(Y_sgn)
  = 2 chi_c(C^2 - D_1) + chi_c(D_1)
  = 2(1 - (1-s)) + (1-s)
  = 1 + s.
```

At the realized `D_1`, this is `5`, matching the `A4` row.

The node behavior is also consistent.  At a `D_1` node the two local
transposition meridians are disjoint in `S_4`, but both are odd, so the sign
cover has branch around both local branches.  The stratum formula above
already counts the node as one branch-set point, not two unrelated smooth
points.

### 5.2 S3 resolvent / TB-GERM row

The `S_3` resolvent triple cover is the action of `S_4` on the three pair
partitions of `{1,2,3,4}`.  Its point stabilizer is a Sylow-2 `D8`, so the
Burnside row is `H=D8`, not the normal `V4` quotient row.  The table gives

```text
chi_c(Xhat/D8) = 2 + s.
```

Independently, a transposition in `S_4` acts on the three pair partitions as a
transposition in `S_3`: it fixes the pairing containing that transposed pair
and swaps the other two pairings.  At a `D_1` node the two disjoint local
transpositions have the same image in this `S_3` action, because their product
is in the normal `V4`.  Thus the triple cover is simply ramified over `D_1`
and unbranched over the trivial `D_2` component.

Therefore

```text
chi_c(Y_res)
  = 3 chi_c(C^2 - D_1) + 2 chi_c(D_1)
  = 3s + 2(1-s)
  = 2 + s.
```

At `s=4`, this is `6`, matching the `D8` row.  This is the TB-GERM row as a
control, not an additional identity.

## 6. Degeneracy proof

The full calculation collapses for three independent reasons.

First, the only nontrivial generic inertia is the transposition inertia along
`D_1`.  The generic `D_2` inertia is identity because `D_2` is the
trivial-dicritical component.  Identity-inertia strata contribute to
`Xhat^e` only; they do not contribute to `Xhat^g` for `g != e`.

Second, the identity entry `chi_c(Xhat)` is insensitive to the companion
variables after the strata are assembled:

```text
24(s - chi_2 + j)
+ 12(1 - 2s - j)
+ 24(chi_2 - sigma_2 - j)
+ 6s
+ 12j
+ 24 sigma_2
= 12 + 6s.
```

This is not an integrality accident.  It is the statement that the Galois
closure has the expected finite fibres over the target strata: `24` over
identity-inertia strata, `12` over transposition-inertia strata, and `6` over
the `V4_split` node strata.  The companion variables appear only in
identity-inertia strata, and their Euler contributions cancel against the
target-complement term.

Third, every subgroup average uses only `(f_1,f_T,f_V)`.  Once the vector is

```text
(12+6s, 2(1-s), 2s),
```

there is no remaining slot in the subgroup table where `chi_2`, `sigma_2`, or
`j` could enter.  The subgroup lattice can reweight `f_T` against `f_V`; it
can see the already known `D_1` node count.  It cannot see the companion curve
except through the one source-hull comparison, and that comparison is exactly
`chi_2 + sigma_2 = 1`.

Consequently, after imposing the known realized value `s=4`, the quotient
rows become fixed integers.  Before imposing `s=4`, they are integral
polynomials in the integer `s`; no row imposes even a parity condition.

## 7. General-N rank statement

Here is the promotion-safe rank statement extracted from the computation.

Let `G` be the pinned monodromy group of a decorated RED-N cage profile, and
let `A_G` be the subgroup-average matrix

```text
(A_G)_{H,C} = |H cap C| / |H|,
```

with rows indexed by conjugacy classes of subgroups `H <= G` and columns by
element conjugacy classes `C` of `G`.  Let `B_profile` be the matrix whose
columns are the local-inertia class functions contributed by the decorated
strata of the profile.  Then the rational row rank available from the
Burnside-Euler system on that decorated profile is exactly

```text
rank_Q(A_G B_profile).
```

This rank is a property of the **decorated local inertia columns**, not of the
coarse moved-cycle label.  That distinction is forced by r2: the survivor unit
is the carrier multiset with owner partition and physical places, not just a
label `[lambda^(k)]` (`reducible-all-n-r2...:493-504`), and the label loses
fixed-letter and placement data (`reducible-all-n-r2...:270-289`).

For the pinned N=4 profile computed here,

```text
rank_Q(A_{S4} B_profile) = 3
```

on the supported columns `1,T,V`, while the projection to the residual
companion variables has rank `1`, generated by `chi_2 + sigma_2`.  The extra
subgroup rows increase the rank on the **already known D_1 inertia columns**,
not on the live companion residual.

The all-N consequence is therefore negative in the sense Card A needs:
for every decorated RED-N profile whose companion components are trivial
dicriticals with identity generic inertia and whose only nontrivial local
inertia lies on already pinned branched components, the subgroup-lattice
Burnside rows have zero projection to companion variables except for the
typed source-hull row.  On that class, the residual-variable rank is the same
as the natural-action pair: one source/hull Euler relation.

This covers the transposition/trivial spine represented by the N=4 row and
the analogous restored `[2]` residuals in the r2 ledger.  It does **not**
assert a rank theorem for off-spine imprimitive profiles such as the live
`[22...]`, `[3...]`, `[4...]`, or mixed rows through `N=8`.  R2 explicitly
keeps block-system descent open off the pinned all-transposition classes
(`reducible-all-n-r2...:206-232`, `483-523`).  For those rows, a Burnside rank
claim requires the missing decorated local-inertia matrix `B_profile`; the
coarse cage label alone is insufficient.

Thus the general-N rank statement is:

```text
RANK-N-LOCAL-COLUMN:
  Burnside rank on RED-N residual classes is rank_Q(A_G B_profile).
  At label level there is no promotion-safe rank excess claim.
  On the transposition/trivial companion spine, the companion-variable rank is
  1, not larger than the natural-action source/hull relation.
```

## 8. Final verdict

No subgroup-class row yields an integer relation on `(s_1, sigma_2, j)` beyond
`chi_2 + sigma_2 = 1`.

The full eleven-row `S_4` table at the pinned `N=4` profile is internally
consistent, integral, and matched by the sign and `S_3` resolvent controls.
Its only new-looking information is dependence on `s_1`, but `s_1=4` is
already fixed by the realized `(9,6,2)` curve's exact census.  The live
companion data remain untouched:

```text
sigma_2: unconstrained by Burnside rows after chi_2 + sigma_2 = 1
j:       unconstrained by Burnside rows
s_1:     pinned externally to 4 by the D_1 census, not by a new row
```

Permanent retirement recommended for this direction as charged:
**do not spend further on "more Euler identities" from the subgroup lattice
at the N=4 residual profile.**  Future off-spine use would need new local
inertia data, not another replay of this table.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17945`.
- Body SHA-256:
  `8f6ba20101ba309392bb0b29c929d1f5b89ea605238769a3c1344ad820dd3bbf`.
- Frozen basis: `f35adc89bec33c1e1a2df50ac3d8bcd99f762218`.
