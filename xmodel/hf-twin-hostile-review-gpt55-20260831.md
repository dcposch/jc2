# HF-TWIN (9,6,4) Hostile Review

## Input Integrity

Frozen inputs were checked before review. Both SHA-256 sums match the
charge:

```text
7cef355be1af63e71bc24361955ad19755598c3925fa1cb2612e62e186f4a35b  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.L87hQ0/inputs/hf-twin-964-grok46-20260831.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  /private/var/folders/80/jm5p82hn56g0crpvv9xjzrc00000gn/T/jc2-lane.L87hQ0/inputs/block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Primary PDFs were streamed from the public source URLs and hashed without
saving copies into the tree:

```text
05081acd04a51c85d231ff288c8522b83e79d75b28af7f99868c2f5149683bf9  https://arxiv.org/pdf/1407.0490v1
9a65787ab3ba6be6ec3c3d5eb71538c79b1e43feeb7c10c8fc52e6186453861a  https://arxiv.org/pdf/1304.1062
9329d9d9aa1fbe770576e711874947dd5349cd26741c3524248cfa0a77bd97e0  https://arxiv.org/pdf/1409.2111
ac64acd8f728bc9c920f4063fb6e9699ee13d79cb7fd586b11bc31a9edf84803  https://arxiv.org/pdf/2104.13709v2
e5cdd757e96e2b40508c5a975073fd5ff0b1bf3a2559aaf4019c34ee4500ea9b  https://arxiv.org/pdf/math/0410611
```

No CAS or long-running computation was used. No canonical ledger or
charged input was edited, and no `jc2-lean` content was read. This file is
the only written artifact.

## Charge Under Review

The charged HF-TWIN report asks for `PASS_NECESSARY_ONLY` on the
`(9,6,4)` conductor-12 census twin. The substantive claim is not a
row-exhaustion theorem. It is a necessary-inequality pass for an explicit
polynomial representative with degree `9`, affine delta `6`, one cusp at
infinity of semigroup `⟨3,23⟩`, and affine singularities all in the
BLZ-licensed `T(2,2n)` class. The remaining affine delta `2` is not pinned
as either two nodes or one `A_3`, but both possibilities are licensed by
BLZ 2024 Theorem 6.4.

The coordinator input only marks the rowsweep data as provisional pending
this different-model gate. It also contains an unrelated residual
row-sweep numerical type `Δ=(9,6,4)` for a different object; I do not use
that collision as evidence for or against the present affine curve.

## Re-derived Semigroup Data

Let `r=(r_0,r_1,r_2)=(9,6,4)`. With the Assi--Garcia-Sanchez notation,

```text
d_1 = r_0 = 9
d_2 = gcd(9,6) = 3
d_3 = gcd(3,4) = 1
e_1 = d_1/d_2 = 3
e_2 = d_2/d_3 = 3
```

The freeness divisibilities are exact:

```text
e_1 r_1 = 18 = 2*9 in <9>
e_2 r_2 = 12 = 2*6 in <9,6>
```

The reduced inequalities also hold:

```text
r_1 d_1 = 6*9 = 54 > 4*3 = 12 = r_2 d_2
r_0 > r_1 > d_2 > d_3 is 9 > 6 > 3 > 1
```

Thus `(9,6,4)` is a reduced AG-S delta sequence. The numerical
semigroup is

```text
Γ = <9,6,4> = <4,6,9>.
```

Its gaps are

```text
1, 2, 3, 5, 7, 11
```

so the conductor is `12` and the gap genus is `6`. This agrees with
the AG-S Frobenius formula:

```text
F = (e_1-1)r_1 + (e_2-1)r_2 - r_0
  = 2*6 + 2*4 - 9
  = 11,
C = F+1 = 12.
```

For the polynomial representative below, the compact-core genus identity
is `g_3(K_infty)=6`: the large-sphere knot is the `(3,4)` cable of the
trefoil, and

```text
g(C_(3,4)(T(2,3))) = 3*g(T(2,3)) + (3-1)(4-1)/2
                   = 3*1 + 3
                   = 6.
```

This is a semigroup/large-sphere calculation, not a statement about the
local cusp at projective infinity.

## Associated Curve and Delta Budget

For the AG-S recursive construction, the prefix `(9/3,6/3)=(3,2)`
gives `g_1=y^3-x^2`. The condition

```text
r_2 d_2 = 4*3 = 12 = 0*9 + 2*6
```

selects the distinguished monomial `y^2`, hence the associated curve

```text
f = (y^3-x^2)^3 - y^2.
```

This curve is not the charged `A^1`-normalised polynomial
representative. Indeed, putting `v=y^3-x^2` gives `v^3=y^2`; with
`y=s^3`, `v=s^2`, one obtains `x^2=s^2(s^7-1)`, so the normalization is
the hyperelliptic curve `u^2=s^7-1`, of genus `3`.

The affine singularity check is closed. With `g=y^3-x^2`,

```text
f_x = -6x g^2,       f_y = 9y^2 g^2 - 2y.
```

The equations `f=f_x=f_y=0` have only `(0,0)`: if `g=0`, then
`f=-y^2`; if `x=0`, then `f=y^2(y^7-1)` and the `y^7=1` points have
`f_y=7y != 0`. At the origin the Newton edge is `(6,0)--(0,2)`, with
initial form `-(x^6+y^2)`, so there are two smooth branches with
contact `3`: type `A_5`, delta `3`, link `T(2,6)`.

The degree-9 closure has unique infinity point `[1:0:0]`. In chart
`X=1`,

```text
(Y^3-Z)^3 = Y^2 Z^7.
```

Equivalently, after `Z=Y^3+W`, the first face is `W^3 = -Y^23`;
`gcd(3,23)=1`, so the infinity branch has semigroup `⟨3,23⟩`, delta
`(3-1)(23-1)/2=22`. Since `p_a=(9-1)(9-2)/2=28`, the associated curve
has `g_geom=28-3-22=3`, matching the normalization check. The associated
curve is BLZ-eligible in its own right, but it is not the charged
polynomial census representative.

The charged representative is the explicit polynomial parametrisation

```text
x(t) = t^9 + 3t^7 + (21/4)t^5 + (35/8)t^3 + (63/32)t
y(t) = t^6 + 2t^4 + (5/2)t^2 + 3/4.
```

Writing `z=t^2`, direct expansion gives

```text
y^3-x^2 = (27/1024)(8z^2+13z+16),
```

so the degrees of `x`, `y`, and `y^3-x^2` are exactly `9`, `6`, and `4`.
The parametrisation is proper: any nontrivial reparametrisation degree
divides `gcd(9,6)=3`, but then every nonzero polynomial in the parameter
would have `t`-degree divisible by `3`, contradicting the degree `4`
displayed above. Thus the normalization is `A^1`, and the total affine
delta is the gap genus `6` of `⟨4,6,9⟩`.

The map is immersed. Here

```text
y' = t(6z^2+8z+5),        discr(6z^2+8z+5) = -56,
x'(0)=63/32.
```

Modulo `6z^2+8z+5`, one has

```text
x' == -(27/8)z - 117/32.
```

Its zero would be `z=-13/12`, but
`6z^2+8z+5 = 27/8` there. Hence `x'` and `y'` do not vanish together,
so there are no affine cuspidal branches.

The involution `t -> -t` gives four explicit multiple fibres at the
nonzero roots of

```text
q(z)=32z^4+96z^3+168z^2+140z+63 = 32*x(t)/t.
```

The roots are simple: the Euclidean remainders reduce through
`(3/4)(40z^2+56z+49)` and then `(42/25)(4z+1)`, and
`40(-1/4)^2+56(-1/4)+49=75/2 != 0`. They are not paired to the same
plane point through equal `y`-values: if two distinct roots `r,s` of
`q` had `p(r)=p(s)` for
`p(z)=z^3+2z^2+(5/2)z+3/4`, then with `sigma=r+s` the two coefficient
conditions would be

```text
32 sigma^3+152 sigma^2+256 sigma+157 = 0,
 8 sigma^3+ 32 sigma^2+ 46 sigma+ 25 = 0,
```

whose gcd is `1` since their difference gives
`8sigma^2+24sigma+19` and the next remainder gives `sigma+2`, while
`8(-2)^2+24(-2)+19=3`. Therefore these are four distinct ordinary
nodes, contributing delta `4`.

The remaining affine delta is `6-4=2`. Because the parametrisation is
immersed, every remaining branch is smooth; because a three-branch
smooth germ has delta at least `3`, no remaining point has three or more
branches. Thus the unpinned remainder is either two more nodes or one
two-smooth-branch contact-2 germ (`A_3`). In both cases every affine
singularity is of link type `T(2,2n)`.

Finally, the degree-9 projective closure of the charged curve has
geometric genus `0`, so

```text
δ_infty = p_a - Δ_aff = 28 - 6 = 22.
```

The parametrisation has one place at infinity. In the chart `X=1`,
`Y=y/x` has valuation `3` and `Z=1/x` has valuation `9`; since
multiplicity `3` is prime, a unibranch plane semigroup is `⟨3,b⟩`.
The delta equation `(3-1)(b-1)/2=22` gives `b=23`. Hence the infinity
cusp is `⟨3,23⟩`, link `T(3,23)`, local conductor `44` and Frobenius
`43`.

## BLZ 2024 Applicability

BLZ 2024 Theorem 6.4 applies to a reduced degree-`d` curve of genus
`g` with cuspidal singular points carrying semigroup counting functions
`R_i`, and with every other singular point an `A_{2n-1}` point, i.e. a
link `T(2,2n)`. It defines

```text
η_+ = sum_n m_n,        κ_+ = sum_n n m_n,
```

where `m_n` counts `T(2,2n)` points. With `R` the infimal convolution
of the cuspidal semigroup counting functions, for `k=1,...,d-2` the two
required inequalities are

```text
max_{0<=j<=g} min_{0<=i<=κ_+-η_+}
  (R(kd+1-η_+-2i-2j) + i + j)
    <= (k+1)(k+2)/2 + g,

min_{0<=j<=g+κ_+}
  (R(kd+1-2j) + j)
    >= (k+1)(k+2)/2.
```

The charged curve matches the hypotheses exactly:

```text
d = 9,  g = 0,
one cuspidal point: P_infty with semigroup S = <3,23>,
all affine singularities: two smooth branches, link T(2,2n).
```

There are two possible affine splits, both within the theorem:

```text
A: six nodes                 m_1=6,          η_+=6, κ_+=6
B: four nodes plus one A_3   m_1=4, m_2=1,   η_+=5, κ_+=6
```

The second inequality is independent of this split because `κ_+=6` in
both cases. The first inequality must be checked for both values of
`η_+` and `κ_+-η_+`.

## Licensed Inequality Slots

Use the BLZ convention

```text
R(m) = #(S cap [0,m)),        S=<3,23>.
```

The gap list is

```text
1, 2, 4, 5, 7, 8, 10, 11, 13, 14, 16, 17,
19, 20, 22, 25, 28, 31, 34, 37, 40, 43.
```

Thus `R(m)=m-#(gaps < m)`, and `R(m)=m-22` for `m>=44`.

For split A, the first BLZ left side is `R(9k-5)`. For split B, it is
`min(R(9k-4), R(9k-6)+1)`. The second BLZ left side is
`min_{0<=j<=6}(R(9k+1-2j)+j)`.

| k | RHS | first A | first B | second | second argmin |
|---|-----|---------|---------|--------|---------------|
| 1 | 3  | 2  | 2  | 4  | `j=0,1,2` |
| 2 | 6  | 5  | 5  | 7  | `j=0,1,2` |
| 3 | 10 | 8  | 8  | 11 | `j=1,2,3,4,5` |
| 4 | 15 | 14 | 14 | 16 | `j=4,5,6` |
| 5 | 21 | 20 | 20 | 22 | `j=4,5,6` |
| 6 | 28 | 27 | 27 | 28 | `j=5,6` |
| 7 | 36 | 36 | 36 | 36 | `j=6` |

Every first-inequality entry is `<= RHS`; every second-inequality entry
is `>= RHS`. The saturation checks are exact:

```text
k=6 second: min(33,32,31,30,29,28,28) = 28 = RHS
k=7 second: min(42,41,40,39,38,37,36) = 36 = RHS
```

The first inequality also saturates at `k=7` for both split A and split
B. No BLZ inequality slot kills the charged representative.

## Verdict Classification

Verdict: `PASS_NECESSARY_ONLY`.

Not `KILLED`: the only charged theorem with matching hypotheses is BLZ
2024 Theorem 6.4, and all seven `k=1,...,7` slots hold for both licensed
remaining-delta splits. The saturated slots were rechecked explicitly.
BL 2014 and BHL 2017 are cuspidal-curve obstructions; the charged curve
has affine nodes, so their hypotheses fail. FLMN-style rational
cuspidal/local-irreducibility constraints likewise do not apply to the
charged affine singularity package. No licensed inequality gives a
violation.

Not `OPEN`: the possible gap in the charged report is the unlocated
remaining affine delta `2`. That gap is harmless for BLZ applicability.
The parametrisation is proper and immersed, four distinct ordinary nodes
are accounted for, and the total affine delta is exactly `6`; therefore
the residual delta cannot be unibranch and cannot have three or more
smooth branches. It is necessarily a sum of two-smooth-branch
singularities, hence links `T(2,2n)`. Both possible partitions, six nodes
or four nodes plus one `A_3`, were evaluated in the BLZ table.

The pass is necessary-only. BLZ supplies obstructions, not classification
or full attainment. The displayed curve is a representative of the
`(9,6,4)` row, not a `FULL_ACTUAL_EXIT` assertion for every row member or
for an `S_4` packet. The row-level Newton-face claim remains unnecessary:
the projective infinity semigroup for this curve follows from the
parametrisation and the genus/delta identity. No degree cap, pole
identity, or exit-price charge is consumed.

FALLACY-v2 check: the Abhyankar semigroup `Γ=<4,6,9>` with conductor
`12`, the projective-infinity local semigroup `⟨3,23⟩` with conductor
`44`, and the large-sphere cable knot are kept as distinct objects. The
report does not identify a flag, physical place, and cover series. It
uses equality in the delta budget only where the normalization and
singularity accounting supply it. It makes no `sat()` claim, no raw
remainder claim, no variable-name ring-map claim, no M-descent claim, and
no exit-price declaration.

## Promotion Recommendation

Promote the charged HF-TWIN result as:

```text
HF-TWIN (9,6,4): PASS_NECESSARY_ONLY, confirmed.
```

Recommended ledger wording should include the pins:

```text
explicit polynomial representative only;
degree 9, genus 0, Δ_aff=6, P_infty semigroup <3,23>;
affine singularities all T(2,2n);
BLZ 2024 Theorem 6.4 all k=1..7 hold, with second-inequality saturation at k=6,7;
remaining affine delta split unpinned but irrelevant to BLZ because both splits are licensed.
```

Do not promote a stronger classification, row-exhaustion, `FULL_ACTUAL_EXIT`,
or exit-price statement from this pass.

<!-- BODY-END -->
