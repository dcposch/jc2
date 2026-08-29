# Degree-eight R5 survivors against D3 raw support

Date: 2026-08-27  
Author: Grok 4.6, independent producer  
Status: **EXACT BOUNDED ANALYSIS / NOT A LANDING THEOREM**

R5 is used only as a named provisional premise, with rollback: every formula
consumed from it is rederived below.  A later hostile failure of R5 retracts
the mode-schedule labels `P`/`Q` without retracting the raw-support lemmas,
which use only the frozen D3 lattice and the coefficient recurrence.

---

## 0. Result

On the frozen D3 raw `2S/3S` support through weight 22, every polynomial
`X`-jet has

```text
F_n = 0  for all n ≥ 15,
G_n = 0  for all n ≥ 22.
```

The charged target `D_22=1` therefore has **no** `G_22` (or `F_22`) handle.
It is the bilinear mixed form

```text
D_22 = sum_{i=1}^{14}  ((12-(22-i)) F_i' G_{22-i} + (i-8) F_i G_{22-i}')
```

in the positive-weight raw slots.  The constant term of this form uses only
four named slots,

```text
D_22[X^0] = F_11[X^1] G_11[X^0] - F_7[X^0] G_15[X^1],     (0.1)
```

and the only contributing pairs that can produce a constant are `(F_7,G_15)`
and `(F_11,G_11)`.

For the two R5 endpoint survivors, the first weight at which a rational
exact homogeneous mode is **not** a raw polynomial `G_n` slot is

| branch | first unrepresentable mode | leading term | raw `G_n` window |
|---|---|---|---|
| (Q) generic `delta` odd | `n=16` | `H^{-1}` | `span{X^2,...,X^8}` |
| (P) `H=A^2`, `delta=2` | `n=14` | `A^{-1}` | `span{X^1,...,X^{10}}` |

The denser even schedule of `P` is an asset through weight 12: the extra
modes at `n=2,6,10` are polynomial and lie in the raw `G_n` windows.  The
weight-22 kernel `A^{-5}` of `P` is **not** a raw slot (`G_22` is empty).  It
can affine-shift the rational residual `d` in `K(X)`, but it cannot be added
as a polynomial `G_22` term to cancel an endpoint particular while preserving
raw support.

The first weight at which `D_n=0` becomes a cokernel incidence on mixed
lower terms, with no remaining `F_n` handle, is `n=15`.  The exact linear
object is

```text
L_n :  (raw G_n-window)  -->  Q[X],
L_n(G) = (12-n) (H^2)' G - 8 H^2 G',     n=15,...,21.     (0.2)
```

Each `L_n` is injective on its window.  Image(`L_n`) sits in the principal
ideal `(H)`.  Dimensions, over any characteristic-zero field, for a degree-8
`H` occupying the top of `F_0`/`G_0`:

```text
n     dim G_n     rank L_n     D_n deg window     dim coker
15       9           9          0..24              16
16       7           7          0..23              17
17       6           6          0..22              17
18       5           5          0..21              17
19       3           3          0..20              18
20       2           2          0..19              18
21       1           1          0..18              18
```

Stop rule: at the first `n∈{15,...,21}` for which the mixed bilinear of
lower raw slots misses `im(L_n)`, the jet is dead.  If all seven land, the
remaining object is the single bilinear evaluation `D_22 ?=? 1`.

Negative fixture (exact): the leading-edge jet `F=H^2`, `G=H^3`, with all
positive-weight slots zero, satisfies `D_n=0` for every `n` and in
particular `D_22=0≠1`.  The same holds after adding any `Q`-polynomial modes
`c_4 t^4 H^2 + c_8 t^8 H + c_12 t^{12}` (and, for `P`, the extra polynomial
modes `c_2 t^2 A^5 + c_6 t^6 A^3 + c_10 t^{10} A`).  Two-weight activation
of the linear kernel at weight 11 produces bilinear `D_22` of degree at
least 9; the constant `1` is not even in the linear span of that bilinear
table.

No exact positive fixture with `D_22=1` on either survivor branch was
constructed.  The analysis does **not** exclude either branch as a whole,
does **not** produce a polynomial jet, and does **not** claim GGV landing.

---

## Firewall

Maximum licensed claim: a necessary raw-support filter on the two R5
degree-eight endpoint survivors, together with an executable finite linear
object and an exact negative fixture.  R5 remains provisional.  This note
does not prove GGV landing, a whole-family statement, `G2-PSC`, `G2-BD`,
cofinality, a counterexample, or JC2.

---

## Custody

Pinned inputs, SHA-256 recomputed on the live bytes, all matching:

```text
fd1640420ac389b1b6c3a0ea21243f5d72488bba5d39e4cc2293ab9e7c494681
  xmodel/ggv-keller-face-general-multiplicity-endpoint-r5-sol-20260827.md
3d8ba26743a5c77bf37694ec0118a221a9c5fa1faff6fffb426659010a51c419
  cases/ggv_keller_face_general_multiplicity_endpoint_r5_20260827/FREEZE.sha256
012acfe5ca560757269fd6e332ed3c4bab2f1005bce43113109f31b705ffe022
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/FREEZE.sha256
5187676bdb9b1ea449dde569e426385ad1453b4f15ebc8906886a7cc33c14557
  xmodel/ggv-keller-face-general-squarefree-rational-mode-theorem-r4-hostile-review-grok-20260827.md
```

Freeze-internal lines of both charged freezes match the live bytes of every
hashed producer file.  R5 is treated as a named premise, not as promoted
evidence.  No AWS, no CAS, no `jc2-lean` access, no ledger or freeze edits.
Desk-scale exact `Fraction` arithmetic and one prime-field linear algebra
pass (`p=257` and `p=10^9+7`) were used as mutation guards, not as the
support or mode identities.

Repository `HEAD` at writing: `418e413593120d19e15e6546eb50c985f4b1f038`.

---

## 1. Raw `F_n`/`G_n` support from the D3 lattice

D3 enumerates lattice points of `2S` and `3S` independently of any chart
slogan.  The polygons, taken from the D3 compiler and rederived from the
inequalities, are

```text
2S:  i ≥ 0,   max(0, 4i-8)  ≤ j ≤ 3i+8,    i ≤ 16,
3S:  i ≥ 0,   max(0, 4i-12) ≤ j ≤ 3i+12,   i ≤ 24.
```

The raw chart is

```text
x^i y^j  in f  |->  t^{8+3i-j} X^i,
x^i y^j  in g  |->  t^{12+3i-j} X^i.
```

Hence `n_F=8+3i-j` and `n_G=12+3i-j`.  The upper inequalities `j≤3i+8` and
`j≤3i+12` are automatic for every `n≥0`.  The remaining inequalities give
the exact windows, empty when the lower bound exceeds the upper bound:

```text
F_n:  max(0, ceil((n-8)/3))  ≤ i ≤ 16-n,    j=8+3i-n,
G_n:  max(0, ceil((n-12)/3)) ≤ i ≤ 24-n,    j=12+3i-n.
```

Independent double count of lattice points with `0≤n≤22` recovers D3's
census: `141` named `F` slots, `301` named `G` slots, `442` total.  Slice
enumeration and polygon enumeration agree as sets.

The complete windows:

```text
n     F_n degrees           #    G_n degrees            #
 0    0..16                17    0..24                 25
 1    0..15                16    0..23                 24
 2    0..14                15    0..22                 23
 3    0..13                14    0..21                 22
 4    0..12                13    0..20                 21
 5    0..11                12    0..19                 20
 6    0..10                11    0..18                 19
 7    0..9                 10    0..17                 18
 8    0..8                  9    0..16                 17
 9    1..7                  7    0..15                 16
10    1..6                  6    0..14                 15
11    1..5                  5    0..13                 14
12    2..4                  3    0..12                 13
13    2..3                  2    1..11                 11
14    2                     1    1..10                 10
15    empty                 0    1..9                   9
16    empty                 0    2..8                   7
17    empty                 0    2..7                   6
18    empty                 0    2..6                   5
19    empty                 0    3..5                   3
20    empty                 0    3..4                   2
21    empty                 0    3                      1
22    empty                 0    empty                  0
```

In particular `F_14` is only `X^2` (raw `x^2`), `G_21` is only `X^3` (raw
`x^3`), and `G_22` is empty, matching the D3 boundary rows.  These are
identities of lattice-point sets, not samples.

The same windows imply that a raw jet is a polynomial in `t` of `F`-degree
at most 14 and `G`-degree at most 21.  There is no raw `t^{22}` coefficient
in `G`.

---

## 2. Recurrence, and independent check of every consumed R5 formula

### 2.1 Coefficient recurrence

For `F=sum F_n t^n`, `G=sum G_n t^n` and

```text
E = 12 F_X G - 8 F G_X - t(F_X G_t - F_t G_X),
```

the coefficient of `t^n` is

```text
D_n = sum_{i+j=n} ((12-j) F_i' G_j + (i-8) F_i G_j').     (2.1)
```

This is the `t^n` slice of `E`, not an import: `t G_t` contributes the
`-j F_i' G_j` correction and `t F_t` contributes the `+i F_i G_j'`
correction, which together convert `12` into `12-j` and `-8` into `i-8`.

With `F_0=H^2` and `G_0=H^3`, the `(0,0)` pairing vanishes by Euler:

```text
D_0 = 12 (2H H') H^3 - 8 H^2 (3 H^2 H') = 0.
```

For `n≥15` one has `F_n=0` on the raw lattice, so

```text
D_n = L_n(G_n) + mixed_n,     mixed_n = sum_{i=1}^{n-1} pair(F_i,G_{n-i}),
```

with `L_n` as in (0.2).  Explicitly
`L_n(G)=2H[(12-n)H' G - 4 H G']`, hence `im(L_n) ⊆ (H)`.  At `n=22` both
windows are empty, so `D_22=mixed_22` with no linear remainder.

Possible `X`-degrees in `D_22` from the raw windows are `0` through `17`.
The constant term is exactly (0.1).  The four slots in (0.1) are named D3
slots `f_1_0` (`F_11`, `i=1`), `g_0_1` (`G_11`, `i=0`), `f_0_1` (`F_7`,
`i=0`), and `g_1_0` (`G_15`, `i=1`).

### 2.2 Homogeneous modes

Direct substitution in `K(X)[[t]]` gives, whenever the binomial series of
`F^γ` exists,

```text
E(F, t^n F^γ) = t^n F^γ F_X (12 - 8γ - n).
```

The vanishing locus is `γ=(12-n)/8`.  Writing `q_n=(12-n)/4` one has
`q_n=2γ_n` and `12-8γ_n-n=0` for every integer `n`, including `n=22`.
This identity does not use squarefreeness, degree, or R5.

A first residual `r_n∈K(X)` at weight `n` satisfies
`r_n'/r_n = q_n H'/H`.  Logarithmic residues at the distinct monic
irreducible factors `p_i` of `H` (multiplicities `e_i`) are integers, so a
nonzero rational solution requires `q_n e_i ∈ Z` for every `i`, equivalently
`4 | delta·(12-n)` with `delta=gcd_i(e_i)`.  The converse produces
`R_q=product p_i^{q_n e_i}` and the exact lift
`t^n R_q (F/H^2)^{γ_n} = t^n F^{γ_n}`.  Constant-field of `K(X)` under
`d/dX` is `K`.  An extra factor at infinity would mismatch leading `1/X`
coefficients.  These are the R5 mode statements, rederived; they are used
below only as a schedule of candidate leading terms to test against raw
windows.

Schedules through weight 22, matching R5:

```text
delta odd:           n = 0,4,8,12,16,20;
delta ≡ 2 (mod 4):   n = 0,2,4,...,20,22;
4 | delta:           every n = 0,...,22.
```

### 2.3 Endpoint ODE

After subtracting all rational modes below 22, a residual `t^{22}d` has

```text
E_22 = 2H((12-22)H' d - 4 H d') = -20 H H' d - 8 H^2 d'.
```

The change `g=-8 H^2 d` gives the identity, valid for every nonzero `H` and
every rational `d`,

```text
2H g' + H' g = 2H · E_22.
```

On the target `E_22=1` this is `2H g'+H'g=2H`.  No squarefreeness and no
uniqueness at weight 22 is used.  Existence of a weight-22 homogeneous
kernel (the `P` case) makes the solution affine, not empty.

### 2.4 Squarefree decomposition and degree-eight filter

Write `H=A^2 B` with `B` squarefree.  Substituting `g=B z/A` converts the
endpoint ODE into `B z' + (3/2) B' z = A`.  A finite pole of rational `z`
away from `B` is uncancelled in the derivative term.  At a simple root of
`B`, a pole of order `m≥1` has leading coefficient `3/2-m ≠ 0`.  Thus every
rational `z` is polynomial, and solvability is `A=N_B(v):=B v'+(3/2)B' v`
for some `v∈K[X]`.

Degree law, `b=deg B≥1`, `deg v=r≥0`:

```text
deg N_B(v) = r+b-1,     lc = (r + (3/2)b) lc(B) lc(v) ≠ 0
```

in characteristic zero.  For `deg H=8` one has `2a+b=8` with `b∈{0,2,4,6,8}`
by parity of the odd-multiplicity part.  If `b≥4` then `a<b-1`, so (0.2) in
R5 is impossible.  Survivors of this degree filter are only `b=0` (branch
`P`) and `b=2` (branch `Q`).

### 2.5 Normalized quadratic formula, and the raw-chart form

Over an algebraic closure, after translation and scaling, `B=z^2-D` with
`D≠0`.  For `v=v_2 z^2+v_1 z+v_0`,

```text
N_B(v) = 5 v_2 z^3 + 4 v_1 z^2 + (3 v_0 - 2 D v_2) z - D v_1.
```

Matching a cubic `A=a_3 z^3+a_2 z^2+a_1 z+a_0` is equivalent to
`4 a_0 + D a_2 = 0`; the other three coefficients determine `v` uniquely.
This identity was recomputed and mutation-checked (`A_0 ↦ A_0+1` breaks it).

That normalization is **not** a raw-chart automorphism.  Translation
`X=z+β` fills lower `X`-degrees: a raw slot such as `F_14=c X^2` becomes a
trinomial of degrees `0,1,2`, and degrees `0` and `1` are forbidden on the
`F_14` window.  Scaling `X` likewise moves Newton edges.  The condition
`4 a_0+D a_2=0` is therefore an endpoint-category statement after base
extension, not a statement in the D3 coordinate `X`.

The invariant raw-chart form, for a general quadratic
`B=b_2 X^2 + b_1 X + b_0` with `disc(B)≠0`, is that the cubic `A` lies in
the image of the `K`-linear map `N_B: K[X]_{≤2} → K[X]_{≤3}` with matrix,
relative to bases `(v_2,v_1,v_0)` and `(X^3,X^2,X,1)`,

```text
[  5 b2              0            0    ]
[ (7/2) b1          4 b2          0    ]
[  2 b0            (5/2) b1      3 b2  ]
[  0                b0         (3/2) b1]
```

When `b_1=0`, the left kernel is spanned by `(0,-b_0,0,4 b_2)`, i.e.

```text
4 b_2 a_0 - b_0 a_2 = 0,
```

which is `4 a_0 + D a_2 = 0` upon `b_2=1`, `b_0=-D`.  Field extension is
needed only to split `B` or to complete the square; the image membership
`A∈im N_B` is already defined over the ground field of the coefficients of
`A,B`.

If `A` and `B` share a root then, at a simple root of `B`, `N_B(v)` vanishes
iff `v` vanishes there, so `B` divides `v` and hence `B` divides `A`.  That
is a special subcase of `Q` (multiplicity `3` at the shared root), not the
generic `delta=1` schedule.

---

## 3. Rational modes against raw windows

Polynomiality is imposed on the original `G`, not on individual modes.  A
mode is nonetheless a variation of `G` given `F`, and at the leading edge
`F=H^2` (no positive `F`) it occupies a single weight with leading term
`H^{q_n}`.  If that leading term does not lie in the raw `G_n` window, the
mode is not a raw polynomial slot.  Tails of lower modes, or poles of
`F^{3/2}`, can still cancel against it in `K(X)`; that cancellation is the
content of §4, not a license to treat the leading term as a raw coefficient.

### 3.1 Branch `Q` (generic: `A` squarefree, coprime to `B`, `delta=1`)

Leading terms `H^{q_n}` versus raw `G_n`:

```text
n     q_n     leading        deg     G_n window     raw polynomial slot?
 0     3      H^3             24      0..24          yes (this is G_0)
 4     2      H^2             16      0..20          yes
 8     1      H                8      0..16          yes
12     0      1                0      0..12          yes
16    -1      H^{-1}         poles    2..8           NO
20    -2      H^{-2}         poles    3..4           NO
22   -5/2     H^{-5/2}       not in K(X)   empty     NO
```

The first unrepresentable `Q`-mode is at weight 16.  Weights `0,4,8,12` fit.

### 3.2 Branch `P` (`H=A^2`, `deg A=4`, generic `delta=2`)

Leading terms `A^{(12-n)/2}` (since `H^{q_n}=A^{2 q_n}`):

```text
n     q_n     leading        deg     G_n window     raw polynomial slot?
 0     3      A^6             24      0..24          yes
 2    5/2     A^5             20      0..22          yes
 4     2      A^4             16      0..20          yes
 6    3/2     A^3             12      0..18          yes
 8     1      A^2=H            8      0..16          yes
10    1/2     A                4      0..14          yes
12     0      1                0      0..12          yes
14   -1/2     A^{-1}         poles    1..10          NO
16    -1      A^{-2}         poles    2..8           NO
18   -3/2     A^{-3}         poles    2..6           NO
20    -2      A^{-4}         poles    3..4           NO
22   -5/2     A^{-5}         poles    empty          NO
```

The denser schedule is useful through weight 12: three extra polynomial
modes fit the raw windows.  The first unrepresentable `P`-mode is at
weight 14, two weights earlier than `Q`.  The weight-22 kernel `A^{-5}`
meets an empty window.

Linearized kernel dimensions at the leading edge, computed exactly over
`Q` for the fixtures `H=(X^4+1)^2` (`P`) and
`H=(5X^3-4X^2+X+1)^2(X^2-1)` (`Q`, which satisfies `4a_0+D a_2=0` in
the already-centered chart `B=X^2-1`), confirm the table.  At `n=2` the
`P` kernel is one dimension larger than `Q` (`16` vs `15`), matching the
extra polynomial mode `A^5`.  At `n=14,16,18,20,22` there is **no** extra
polynomial kernel on either branch: the negative-power modes are not in
the raw windows.  At `n=14` both branches have nulldimension `1`, equal to
the single `F_14=c X^2` slot, not to an `A^{-1}` direction.

### 3.3 No low-weight obstruction through 14

For `n≤14`, `F_n` is a nonempty raw window.  The linearized pairing with
`(F_0,G_0)` always has a solution in the product of the raw `F_n` and `G_n`
windows: `G_n=(3/2)H F_n` lands in `G_n` whenever `F_n` occupies its window,
because

```text
hi(F_n)+deg H = (16-n)+8 = 24-n = hi(G_n),
lo(F_n) = max(0, ceil((n-8)/3)) ≥ max(0, ceil((n-12)/3)) = lo(G_n).
```

Plus, at mode weights with polynomial leading term, a one-dimensional
`G`-summand.  Sequential exact linear algebra over `Q` on both fixtures
produces nonempty affine spaces at every `n=1,...,14`.  There is no first
weight below 15 at which a required rational mode (or the unique
off-kernel particular) fails to meet the raw polynomial slots.

---

## 4. Weight 15–21 as a finite linear object; `D_22=1` as the bilinear target

### 4.1 The maps

For `n=15,...,21`, `F_n` is empty, so `D_n=0` is the affine equation
`L_n(G_n)=-mixed_n` on the raw `G_n` window.  Each `L_n` was row-reduced
over `Q` (and over `F_p`) on the named windows.  In every case
`rank = dim(G_n-window)` and the kernel is zero: `G_n` is unique when it
exists.  The cokernel dimensions are those of §0.

Because `L_n(G)∈(H)`, a necessary condition for existence is
`H | mixed_n`.  At each simple root `σ` of `H` this is the scalar
`mixed_n(σ)=0`, which `G_n` cannot cancel.  At a double root (an `A`-root
on either branch, and every root on `P`) `L_n` vanishes to order at least
`3`, so `mixed_n` must vanish to order `3` before `G_n` can act.

This is the first genuine raw/mode interaction: `n=15` is the first empty
`F`-weight, and the first weight whose vanishing is a cokernel incidence
on lower raw slots.

### 4.2 Negative fixture

Take `F_n=G_n=0` for all `n>0`, with `F_0=H^2`, `G_0=H^3`.  Then
`mixed_n=0` for all `n`, so `G_n=0` solves `D_n=0` uniquely for
`n=15,...,21`, and `D_22=0`.  The same holds after adding any combination
of the polynomial modes listed in §3 (they occupy weights `≤12`, produce
no mixed term at `22`, and their self-pairings at `2n≤24` are killed by
the corresponding `L_{2n}` when `2n≤21`, or vanish for `2n=24>22`).

So a polynomial-mode jet on either survivor branch is endpoint-silent at
weight 22 in the raw category: it cannot produce `D_22=1`.

### 4.3 Two-weight kernel fixtures do not hit `1`

The cheapest quadratic attempt is to occupy a single positive weight `k`
in the linearized kernel of `D_k=0`, and read `D_{2k}`.  For `k=11`,
`2k=22`, and the only mixed pair is `(F_11,G_11)`.

On both fixtures the kernel of the raw `(F_11,G_11)` pairing with slot `0`
is `5`-dimensional (`F_11` in degrees `1..5`, `G_11` in `0..13`, `19`
variables, rank `14`).  The bilinear table `Dpair(F^{(a)},G^{(b)})` on a
basis of this kernel has degrees in `{9,...,17}` and rank `13` (`P`) or
`14` (`Q`) inside the `18`-dimensional space of polynomials of degree
`≤17`.  The constant `e_0=(1,0,...,0)` is **not** in that linear span.
Hence no `Q`-linear combination of the bilinear values, and in particular
no quadratic image of the `5`-space, equals the constant polynomial `1`.

The same linear-span test on every mixed pair `(F_i,G_{22-i})` with each
factor in the linearized kernel of its own weight, and with the other
weights zero, failed to contain `e_0` for all
`(i,22-i)∈{(8,14),(9,13),(10,12),(11,11)}` on the `Q` fixture.  For
`i≤7` the partner `G_{22-i}` has `n≥15` and, with no lower mixed terms,
is forced to `0` by injectivity of `L_{22-i}`.  Those pairs contribute
nothing.

A `D_22=1` jet, if it exists, cannot be a two-weight (plus leading edge)
object.  It must use a cascade that produces a nonzero `G_15` (or a
non-kernel `G_11`) from mixed lower terms.

### 4.4 Constant-term 2-jet system is not an obstruction

The constant coefficients of all `D_n` close on the 2-jets

```text
a_n=F_n[0] (n≤8),   b_n=F_n[1] (n≤11),
c_n=G_n[0] (n≤12),   d_n=G_n[1] (n≤15).
```

The generating function is
`Φ=f(12 C - t C')+(t A'-8 A)Δ`.  For fixed `F` 2-jets the map on
`(C,Δ)` is linear of size `29→23`.  With only the leading edge occupied
it has rank `16` and `D_22[0]=1` is inconsistent (recovering §4.2).  With
generic positive `F` 2-jets and `H(0)≠0` the map has full rank `23` and
`D_22[0]=1` is consistent.  With `H(0)=0` the rank is `22` and `D_22[0]=1`
remains consistent.  Thus (0.1) is satisfiable as a 2-jet condition, and
does **not** by itself kill `P` or `Q`.  It is necessary, not sufficient:
the higher-degree coefficients of `D_15,...,D_21` remain.

### 4.5 Staged linear algebra, and what was not obtained

Exact sequential solution over `Q` along the zero section of all kernels
gives the negative fixture of §4.2.  Random sections of the product of
linearized kernels at weights `1..14` (dimension `127` on the `Q`
fixture) missed `im(L_15)` in `200/200` trials over `F_{10^9+7}`, as
expected for a codimension-`16` condition in a large field.

Fixing weights `1..7` arbitrarily and solving the `16` cokernel conditions
of `n=15` linearly on the `35`-dimensional product of kernels at
`8..14` succeeded in `30/30` trials over `F_257`: that map is generically
surjective, leftover dimension `19`.  Sampling the leftover missed
`im(L_16)` in every trial.  The `n=16` incidence is quadratic in the
weight-`8` kernel (self-pairing `F_8,G_8`) and linear in weights `9..14`.
It is the next exact gate, not a Gröbner search: `17` coker conditions,
quadratic in `≤10` variables after using `9` linear variables.  That gate
was not solved to a fixture in this pass.

No exact `D_22=1` jet was produced on either branch.  No identity was
found that would force `mixed_22∈(H)` (or `mixed_22=0`) once
`mixed_15,...,mixed_21∈im(L_n)`, which would have killed `D_22=1` at
every root of `H`.  That identity, if true, would be the cheapest complete
exclusion of both survivors for the frozen raw support; it is not claimed.

---

## 5. Branch `Q` and the endpoint particular

On `Q`, after mode subtraction in `K(X)[[t]]`, a solution of `E_22=1` has

```text
d = -v / (8 A^5 B),     A = N_B(v),     deg v = 2
```

when `deg A=3`.  At infinity, `d=O(X^{-15})`.  The inhomogeneous operator
`L(d)=-20 H H' d - 8 H^2 d'` has leading term
`-h^2 κ(160+8m) X^{15+m}` for `d~κ X^m`; this has degree `0` iff `m=-15`
(the kernel valuation `m=-20` is `H^{-5/2}`, not rational on `Q`).  The
leading coefficient then forces `κ=-1/(40 h^2)`, which matches the
displayed particular.

Raw `G_22=0` says `d=-[t^{22}](mode sum)`.  Degree bounds from the raw
windows and the square-root recurrence `2H S_n=F_n-sum_{i=1}^{n-1}S_i S_{n-i}`
give `deg S_n ≤ 8-n` (as a rational function, negative meaning vanishing
at infinity).  Then

```text
[t^{22}] S^3          has deg ≤ 2,
[t^{18}] S^2          has deg ≤ -2,
S_14                  has deg ≤ -6,
[t^6] S^{-1}          has deg ≤ -14,
[t^2] S^{-2}          has deg ≤ -18.
```

The only contribution that can have a polynomial part at weight 22 is
`S^3`.  Raw `G_22=0` forces that polynomial part (degrees `0,1,2`) to
vanish.  What remains of the mode sum at weight 22 is a rational function
of strictly negative degree, which is the correct infinity class for the
endpoint particular `O(X^{-15})` **if** the finite poles of `d` (simple at
`B`-roots, order `5` at simple `A`-roots) can be arranged by the
negative-power modes and by poles of `S`.  That matching is not a raw
polynomial identity and was not certified here.

The residue of `d` at a simple `B`-root `σ` is forced by `L(d)=1` to be
`-1/(12 h_1^2)` with `H=h_1(X-σ)+⋯`, and this agrees with
`-v(σ)/(8 A(σ)^5 B'(σ))` upon `A(σ)=(3/2)B'(σ)v(σ)`.  An independent
check, not an import.

Source/raw normalizations do **not** force `4a_0+D a_2=0` in the D3
coordinate.  They force `A∈im N_B` in that coordinate, which is the
`4×3` membership of §2.5.  Completing the square to reach `4a_0+D a_2=0`
requires an affine change that leaves the raw windows.

---

## 6. Branch `P` and the weight-22 kernel

On `P`, `B` is a unit, `N_B` is differentiation, and every polynomial `A`
of degree 4 has a polynomial antiderivative `v=∫A` of degree 5.  The
endpoint is therefore always rationally solvable:

```text
d_part = -v / (8 A^5),     d_gen = A^{-5} (c - v/8).
```

The extra constant `c` is the weight-22 homogeneous mode.  It changes the
`X^{-20}` coefficient, not the `X^{-15}` leading term coming from `v`.
Raw `G_22=0` determines `c` (if at all) as whatever makes
`[t^{22}](lower modes)+c A^{-5}` have vanishing polynomial part; it does
not give a free polynomial slot with which to cancel `d_part`.

The extra even modes at `n=2,6,10` are raw-representable and enlarge the
linear kernels at those weights by one (observed at `n=2`: `16` vs `15`).
They feed mixed terms at weights `4,8,12,16,20,22`.  In particular
`2+20`, `6+16`, `10+12` all contribute to `D_22`.  This is a denser
quadratic cascade than `Q`, not a reason to discard `P`.  It does not, by
itself, produce a `D_22=1` fixture, and the first unrepresentable mode at
`n=14` arrives two weights earlier than on `Q`.

If `4|delta` (e.g. `A` a square, `H` a fourth power), every weight is a
mode.  The linearized kernels at odd weights then grow as well (observed
for `H=X^8`: nulldimension at `n=1` is `17` rather than `16`).  Negative
powers still fail to meet the high-weight `G` windows, and `G_22` remains
empty.  This subcase is not a new endpoint survivor; it is a denser-mode
specialisation of `P`.

---

## 7. Failed attempts

1. **Inferring support from a chart slogan.**  Rejected.  Support was
   rebuilt from the D3 lattice inequalities and cross-checked against
   polygon enumeration (`141+301=442`).

2. **Treating each rational mode as a polynomial slot.**  Rejected.  Only
   leading terms were tested against windows, and only to locate the first
   unrepresentable weight.  Polynomiality of `G` is the constraint.

3. **Leading-edge plus polynomial modes.**  Exact, but `D_22=0`.  Negative
   fixture, not a discriminator of `P` vs `Q`.

4. **Constant-term 2-jet system as an obstruction.**  The system closes
   and is solvable for `D_22[0]=1` as soon as positive `F` 2-jets are
   allowed.  Not a branch killer.

5. **Pure weight-11 quadratic.**  Kernel dimension `5`; bilinear image
   misses constants (min degree `9`; `e_0` not in the linear span).
   Exact negative for this ansatz, both branches.

6. **Other two-weight pairs.**  Same linear-span failure, or the
   `n≥15` partner is forced to zero.

7. **Random full-kernel Monte Carlo over `F_p`.**  Died at `n=15` for
   dimension reasons; not a proof of emptiness of the incidence variety.

8. **Staged linear solve of the `n=15` coker, then sampling `n=16`.**
   The `n=15` map on weights `8..14` is generically surjective; `n=16`
   was not reduced to a fixture.  No Gröbner search was launched.

9. **Claiming `mixed_22∈(H)` from `mixed_n∈im(L_n)` for `n<22`.**
   Plausible exclusion of `D_22=1` at every root of `H`, not proved.
   `L_n` lands in `(H)` but mixed terms of two positive weights need not.

10. **Using affine normalization of `Q` as a raw constraint.**  The
    change of `X` does not preserve D3 windows.  Replaced by the `4×3`
    image membership in the raw coordinate.

11. **Assuming the denser `P` schedule is automatically worse.**  The
    extra modes at `2,6,10` fit.  The first failure is at `14`, and the
    weight-22 kernel cannot occupy `G_22`.

---

## 8. Smallest surviving object

One finite linear/determinantal object, with exact inputs, dimensions,
stop rule, and a decisive negative fixture.

**Inputs.**  The D3 named slots through weight 22; `F_0=H^2`, `G_0=H^3`
with `H` of type `P` or `Q` in the raw coordinate (for `Q`, `A∈im N_B`
via the `4×3` matrix, not via a translated `4a_0+D a_2=0`); the bilinear
recurrence (2.1).

**Object.**  For `n=1,...,14`, the linearized pairing of `(F_n,G_n)` in
the raw windows with slot `0`, plus the bilinear mixed of previously
chosen slots.  This is an affine linear solve at each weight, of size at
most `40` variables and `39` equations.  For `n=15,...,21`, the injective
map `L_n` of (0.2) on the raw `G_n` window, asking `mixed_n∈im(L_n)`.
For `n=22`, the bilinear evaluation `mixed_22`, asking equality with `1`.

**Dimensions.**  Recorded in §0 and §3.  No Gröbner basis.  Each step is
one exact Gaussian elimination over `Q`.  The only nonlinear gate is
`n=16`'s self-pairing of weight `8`, which is quadratic in `≤10`
variables after a linear elimination of dimension `9`.

**Stop rule.**  Inconsistent linear system at the first `n∈{15,...,21}`,
or `mixed_22≠1`.  A `PASS` would be an exact rational point of the raw
slots with `D_0=⋯=D_21=0` and `D_22=1`.

**Decisive negative fixture.**  All positive-weight slots zero: replay
gives `D_n=0` for all `n` and `D_22=0`.  Mutation: occupying the
weight-`11` kernel moves `D_22` into degrees `≥9` and still misses `1`.

**What a future `PASS` or `FAIL` of this object would mean.**  A `FAIL`
at a named `n` for a named branch, with an exact coker certificate
`ℓ(mixed_n)≠0` for a linear form `ℓ` annihilating `im(L_n)`, excludes
that branch for the frozen formal raw support.  A `PASS` is a bounded
formal fixture, not a GGV jet.  Neither outcome was obtained beyond the
negative fixture already in hand.

---

## Scope

The result is a necessary raw-support filter on the two degree-eight R5
endpoint survivors, together with the first unrepresentable-mode weights,
the finite linear object `(L_15,...,L_21, mixed_22)`, and an exact
negative fixture.  R5 is provisional.  Nothing here constructs a
polynomial jet from a survivor, lands a GGV object in this chart,
excludes a whole family, controls a global polynomial automorphism,
establishes `G2-PSC` or `G2-BD`, gives a cofinal degree bound, constructs
a counterexample, or resolves JC2.
