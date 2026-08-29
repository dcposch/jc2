# GGV `8_28` lower-face `S1`: native control, artificial completion, family pin, and `LF40` compiler contract

Date: 2026-08-27  
Author lane: Sol Ultra / `lower_facepin_s1`  
Repository basis: `418e413593120d19e15e6546eb50c985f4b1f038`

## Verdict

**A family-covering lower determinant compiler is licensed, with a precise
scope repair.**  Two different statements must not be conflated:

1. The raw `2S/3S` support and the constant-Jacobian equation license an
   unconditional 442-slot regrading and the complete equations
   `Dtil_0,...,Dtil_40`, without pinning any face polynomial.
2. The specialization

   ```text
   F_0 = a K_rho^2,  G_0 = b K_rho^3,
   K_rho = xi (xi-rho)^7,  a*b*rho != 0,
   ```

   is **not** licensed by D3's raw lattice, by either explicit control, or by
   `lib/families.py` alone.  It *is* licensed for the actual GGV `8_28`
   complete-chain family by the coefficient theorem used in GGV22 Proposition
   4.3: before the reduction transforms, the relevant edge is
   `y(x^4 y-alpha)^7` in flipped coordinates, hence
   `x(x y^4-alpha)^7` after unflipping.  The primary-source and local custody
   pins are given below.

Thus the honest object is a **family-wide necessary raw system**, not an exact
parameterization of every GGV chain operation.  Its emptiness would exclude the
raw pre-final `8_28` family, conditional on the already load-bearing
GGV/Horruitiner reduction.  A surviving point must be reconstructed and checked
as a literal polynomial pair; neither one explicit control nor one row is a
family conclusion.

The previous NU17 review was right to refuse pinning from `RAW_INPUT.json` and
from the controls.  Its unresolved Card B is closed only after adding the
primary GGV22 coefficient statement.  The artificial upper face
`H=X^8-1` is not consumed anywhere in the compiler specified here.

## 1. Authority and custody

### 1.1 Primary sources

The following are the exact gzip bytes returned on 2026-08-27 by the arXiv v1
source endpoints.

```text
2afcbe3e6f97eb0d584b097be6ac467b225cbbfd79a4c65c404c40a46d24065e
  https://export.arxiv.org/e-print/1708.07936
cac83f92efca63de3da6ca811b9837061e1a343a44b8039c8748d1b72423cba7
  https://export.arxiv.org/e-print/2204.14178
```

The relevant exact source locations are:

- GGV5, arXiv:1708.07936v1, TeX lines 505--528: for a regular corner,
  the face polynomial is written in a one-variable edge coordinate and the
  distinguished nonzero root has multiplicity `m_lambda`; lines 594--598
  define `gamma=m_lambda/m`; lines 743--765 identify the generated corner with
  that exact multiplicity.
- GGV22, arXiv:2204.14178v1, TeX lines 1000--1018: Proposition 4.3 and its
  pre-reduction polygon `S` multiplied by `(m,n)=(3,2)`, with `q=4`;
  lines 1132--1140: in all three internal branches, before the final
  transformations, the edge is exactly
  `y(x^4 y-alpha)^7` in flipped coordinates.

These citations do more than record the final corner `(11/4,7)`: they carry
the nonzero characteristic root and its seventh power.  This is the missing
coefficient content that the bare lattice record does not serialize.

### 1.2 Local family and transformation custody

```text
729a5ee7dd235ccca2138fd80035e08e3fed87fabf98a8fc4a0c7f9da089bd3e
  lib/families.py
845d42a2d410234f889d5d846f22f7152354896c67ab3d49152469260e892c0d
  tests/test_families.py
1394871719df5a9ae7726268c1ad760af3bc89e7f8e707af550e6155e9114d88
  lib/FAMILIES.md
836e3c4a8ef491799cd258a26cd0b7ae04a1309b0eefcedcc3964f5288c71427
  jc72108/SECTION4-AUTOMATION.md
```

The live record is exact at `lib/families.py:440-476,478-496` and
`tests/test_families.py:216-235`:

```text
A0=(8,1,28), A0p=(1,1,0),
chain=(((8,1,28),(1,1,0)),),
final=(11,4,7), step=(4,-1,3,4),
mn=(3,2), degs=(108,72),
S=((0,0),(1,0),(8,28),(0,4)),
SuppP=3S, SuppQ=2S.
```

`jc72108/SECTION4-AUTOMATION.md:38-74,85-104` separates the raw standard
pair, whose bracket is constant, from the final `psi_4` output, whose bracket
is `x^2`.  Its `:140-150,208-225` also records that the coefficient-bearing
edge certificate and the root-multiplicity branch are part of the reduction,
not consequences of a support hull.  Therefore the lower compiler below acts
on the **raw pre-final `2S/3S` pair**.  The reduced systems
`open_8_28_c1/c2` in `cases/emit.py:40-48` are different coordinates and are
not valid inputs to this compiler.

### 1.3 Raw lattice and reviewed lower identity

```text
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
012acfe5ca560757269fd6e332ed3c4bab2f1005bce43113109f31b705ffe022
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/FREEZE.sha256
c7ea900bdf0552c50d2a61c5a8f0f41a7b06e24eccedf5e5ab9cef3946c53556
  xmodel/ggv-8_28-raw-to-global-M-cokernel-interface-d3-sol-20260827.md
72f10ad7b42fd15d24bfc578ba1f8f9722ba695341307ae61642f614fe34a1ab
  xmodel/ggv-second-newton-face-nu17-opus5-hostile-review-grok-20260827.md
```

D3 supplies every raw exponent but stores the *upper* weight.  `LF40` must
read only `raw_exponents`, then independently recompute the lower weight.  The
reviewed lower identity and recurrence are at the NU17 hostile review
`:116-172`; the exact windows, census, and tail are at `:176-245`; the warning
against treating one row as a fixture and the required `0..40` tail are at
`:587-627`.

## 2. Three objects, kept disjoint

Put `z=xy^4` and `B=x(z-1)^7`.

| Object | Literal polynomials / constraints | `(4,-1)` lower face | Upper `(-3,1)` face | What it licenses |
|---|---|---|---|---|
| Fibre-tagged native control | `f=B^2-x-y^8`; `g=B^3-2x^2y^2+y^12+lambda*x*y^15` | `B^2`, `B^3` | for `f`, `X^16-1`, not a square | One reviewed non-Keller realization of the chain ledger and a fibre-tagged mutation control; no Keller or family inference |
| D3/R0 artificial completion | `f=B^2-2x^8y^32+y^8`; `g=B^3-3x^16y^60+3x^8y^36-y^12` | the same `B^2`, `B^3` | `(X^8-1)^2`, `(X^8-1)^3` | An artificial upper-face fixture and raw-slot custody; no claim that this upper completion occurs in the GGV family |
| Actual GGV `8_28` raw family | unknown coefficients on exact `2S/3S`, constant Jacobian, complete chain `(8,28)->(11/4,7)` | `a[x(xy^4-rho)^7]^2`, `b[x(xy^4-rho)^7]^3`, with nonzero parameters | not determined or consumed by this report | A family-covering lower `FACEPIN` specialization, conditional on the GGV reduction theorem |

Native-control custody:

```text
7647f2f118d4fe9fdd060b9e3e9450b58a62e287a80e942cad6de752a3f34ae8
  xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-sol-20260827.md
971147c5c8a6d3f26c103b0a2da1095ca7c302a2cfd1e812556eaddf6d21a316
  xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-hostile-review-grok-20260827.md
676bdd3ce960221072f037e7160d457a9d1d64c8e7353891f69e9931ae71149b
  cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/FREEZE.sha256
```

Artificial-completion custody:

```text
3e4e608d32c44b1b0208bd5472257ba1dbe4cadf4ef5efb2ace49d3d47d756be
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-sol-20260827.md
171ff47c844331da8971a731c1ffaf20c31ed5b2ba86fdee2d0d81219eb002b0
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-hostile-review-grok-20260827.md
6928428f9cc46641a80275e2bbfa62e784c4290ff041f5089ae789507fa8804f
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/FREEZE.sha256
```

The native control and artificial completion agree on the lower face because
every added term has strictly smaller `(4,-1)` weight.  This agreement is a
useful checksum, not the proof of family pinning.  Conversely, their upper
faces differ, so transporting the artificial `H=X^8-1` into the family would
be an actual mathematical error.

## 3. Exact family pinning derivation

Work over an algebraically closed characteristic-zero field after the usual
base extension.  Orient the raw pair as

```text
f in 2S,  g in 3S,  J(f,g)=1.
```

If the GGV pair is presented as `(P,Q)` with `P in 3S`, `Q in 2S` and
`[P,Q]=1`, take `(f,g)=(Q,-P)`; this preserves `J(f,g)=1` and absorbs the sign
in the leading scalar.  No unrecorded orientation swap is needed.

The lower edges of the raw polygons are

```text
2S: (2,0) -- (16,56),
3S: (3,0) -- (24,84).
```

Consequently, with `z=xy^4`, their general forms are

```text
in_(4,-1)(f) = x^2 A(z),  deg A=14,
in_(4,-1)(g) = x^3 C(z),  deg C=21,
```

with both endpoint coefficients nonzero when the listed Newton vertices are
attained.

Use the lower chart

```text
x=tau^-4 xi,  y=tau,
F=tau^8 f,    G=tau^12 g.
```

Then the leading rows are `F_0=xi^2 A(xi)` and `G_0=xi^3 C(xi)`.  The
constant-Jacobian equation at weight zero is

```text
Dtil_0 = 12 F_0' G_0 - 8 F_0 G_0' = 0.
```

Unique factorization gives

```text
F_0=a K^2,  G_0=b K^3.
```

The exact endpoints force `ord_xi(K)=1` and `deg K=8`; thus
`K=xi*h(xi)`, `deg h=7`, `h(0)!=0`.  This is all the raw lattice plus
`Dtil_0` proves.  In particular it still permits several nonzero roots.

The chain coefficient theorem supplies the remaining step.  GGV22's
pre-transformation base edge is `y(x^4y-alpha)^7` after the paper's initial
coordinate flip.  Undoing that flip gives

```text
x(xy^4-alpha)^7.
```

Since `alpha` is the nonzero characteristic root whose normalized
multiplicity is the final-chain entry `gamma=7`, it exhausts the seven
non-axis residual degrees.  Therefore

```text
K_rho(xi)=xi(xi-rho)^7,  rho!=0,
F_0=a K_rho^2,           G_0=b K_rho^3.
```

This pins the **shape**, not the normalization: the controls use `rho=1` and
`a=b=1`, while the family compiler must retain `a,b,rho` as nonzero
parameters unless a separately audited torus normalization is supplied.

## 4. Frozen compiler specification `GGV-8_28-LF40-v1`

This section is a fail-closed implementation contract.  It is the only
compiler specification licensed by this report.

### 4.1 Input and source pins

Required inputs:

1. the exact D3 `RAW_INPUT.json` blob at SHA
   `28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876`;
2. the family-record blob `lib/families.py` at SHA
   `729a5ee7dd235ccca2138fd80035e08e3fed87fabf98a8fc4a0c7f9da089bd3e`;
3. the two primary-source gzip digests in section 1.1; and
4. a literal serialized `FACEPIN` derivation containing the flip/unflip map,
   the edge polynomial, `rho!=0`, and all 37 leading-slot equalities below.

The compiler must reject a changed pin.  It must not read D3's stored `weight`
or `chart_image` as the lower grading; those fields belong to the upper chart.

### 4.2 Raw slots and lower regrading

Read all 141 `f_i_j` slots of `2S` and all 301 `g_i_j` slots of `3S` from
their `raw_exponents`.  Recompute

```text
nu_F(i,j)=8-4i+j,
nu_G(i,j)=12-4i+j.
```

Equivalently, for every integer `nu`,

```text
F_nu: max(0,ceil((8-nu)/4)) <= i <= 16-nu,
      j=nu-8+4i,
G_nu: max(0,ceil((12-nu)/4)) <= i <= 24-nu,
      j=nu-12+4i.
```

The compiler must independently assert exact set equality between these
formulae and the regraded raw exponents.  Required census:

```text
F: 141 total = 15 at nu=0 + 126 at positive nu; max nu=16,
G: 301 total = 22 at nu=0 + 279 at positive nu; max nu=24,
total: 442, with 405 positive-weight slots.
```

The live tail must be present:

```text
F_17 = empty,
G_17,...,G_24 have 8,7,6,5,4,3,2,1 slots respectively.
```

### 4.3 `FACEPIN` equations and saturation

Introduce coefficient parameters `a,b,rho` and

```text
K=xi(xi-rho)^7.
```

Retain the original names in the custody representation and emit the 37 exact
relations

```text
f_(i,4i-8)  = coefficient of xi^i in a*K^2,  i=2,...,16,
g_(i,4i-12) = coefficient of xi^i in b*K^3,  i=3,...,24.
```

The compute representation may substitute these relations, leaving 405 raw
slots plus `a,b,rho`, but it must serialize and hash both forms and prove their
equality after substitution.

At minimum saturate by

```text
a*b*rho*f_0_8*g_0_12.
```

Here the first three factors attain both lower-edge endpoints, and the last
two attain the nonorigin axis vertices `(0,8)` and `(0,12)`.  Under the
campaign convention, `(0,0)` is a hull anchor and need not be saturated; a
separate strict-origin control may additionally saturate the two constant
slots.  No normalization `rho=1`, `a=1`, or `b=1` is allowed without a typed
torus/scalar ledger that also tracks the Jacobian target.

### 4.4 Determinant rows

Construct

```text
F=sum_(r=0)^16 F_r(xi) tau^r,
G=sum_(s=0)^24 G_s(xi) tau^s
```

and emit, for every `0<=n<=40`,

```text
Dtil_n = sum_(r+s=n)
  ((12-s) F_r'(xi) G_s(xi) + (r-8) F_r(xi) G_s'(xi)).
```

The target is exactly

```text
Dtil_17=-1,
Dtil_n=0 for every n!=17 in 0,...,40.
```

Reason: direct differentiation gives

```text
12 F_xi G - 8 F G_xi
 - tau(F_xi G_tau-F_tau G_xi)
 = -tau^17 J_(x,y)(f,g).
```

The target sign is therefore tied to the chosen `J(f,g)=1` orientation.
`Dtil_0` must reduce identically to zero after `FACEPIN`.  `Dtil_40` must also
be emitted as a structural-zero control: its only possible pair is the
constant-in-`xi` rows `F_16` and `G_24`, so both derivative terms vanish.
`Dtil_39` is the last potentially nonzero row.  Stopping at row 17 or row 24
is forbidden.

For each `n`, serialize:

- every pre-combination contribution, with source slot names, raw exponents,
  lower weights, derivative side, and output `xi` degree;
- the combined sparse polynomial over the coefficient ring;
- every coefficient generator of `Dtil_n+delta_(n,17)`; and
- row and cumulative digests.

### 4.5 Independent direct-coordinate engine

The second engine must not call the recurrence implementation.  Reconstruct

```text
f=sum f_i_j x^i y^j,  g=sum g_i_j x^i y^j
```

in the original coordinates, calculate `J=f_x g_y-f_y g_x`, and map each
Jacobian monomial `c*x^p*y^q` to

```text
-c * xi^p * tau^(17-4p+q).
```

Its complete coefficient-ring output must equal the recurrence engine term
for term for rows `0..40`, both before and after `FACEPIN`.  This is a
same-source consistency check, not an independent-model review.

### 4.6 Required controls

The frozen run must fail closed on all of the following mutations:

1. replace `-4i` by `-3i` in either lower weight;
2. change the target sign at row 17;
3. truncate after row 17 or row 24;
4. delete the live slot `g_0_12=G_24`;
5. change the exponent `7` in `K_rho` to `6` while retaining the chain pin;
6. set `rho=0` or omit its saturation factor;
7. import `H=X^8-1` or any D3 upper-face equation; and
8. swap `(f,g)` without changing the target sign.

Two negative controls must be replayed in the lower grading:

- the native pair at mutation parameter `lambda=1` has nonzero rows beginning
  at `Dtil_4` and no row-17 target;
- the D3 artificial completion has nonzero rows beginning at `Dtil_8` and no
  row-17 target.

These facts were independently recomputed from the literal sparse
polynomials.  They prevent either control from being silently accepted as a
Keller-family point while retaining both as exact face-pin checks.

### 4.7 Verdict semantics

Allowed compiler verdict:

```text
PASS-LF40-COMPILER-CUSTODY
```

It means only that the complete raw determinant ideal and the GGV lower
`FACEPIN` equations were compiled exactly.  It is not a solver verdict.

The separately solved, saturated ideal is

```text
I_LF40 = <FACEPIN relations,
          coefficients of Dtil_n+delta_(n,17), 0<=n<=40>
         : (a*b*rho*f_0_8*g_0_12)^infinity.
```

- A characteristic-zero unit-ideal certificate for `I_LF40` excludes the raw
  pre-final `8_28` GGV family, conditional on the cited GGV reduction and the
  orientation bridge.
- A survivor is not licensed as a chain point merely because it satisfies a
  prefix.  A full algebraic point must be reconstructed in `f,g`, replay
  `J(f,g)=1` literally, attain the required degree vertices, and pass an
  independent noninvertibility/counterexample audit.
- Neither outcome proves GGV landing for arbitrary hypothetical
  counterexamples, `G2-PSC`, `G2-BD`, a cofinal degree bound, or JC2.

## 5. Attack in both directions

### 5.1 Strongest case against license

The negative case is real but narrower than previously stated:

- D3's `RAW_INPUT.json` is explicitly tagged
  `R0_ARTIFICIAL_CUSP_CONTROL`; it supplies a lattice, not a family theorem.
- `lib/families.py` serializes `(11/4,7)` but not the characteristic-root
  polynomial.  Reading `K=xi(xi-rho)^7` from that Python tuple alone is an
  unjustified semantic leap.
- The native control is non-Keller, and the artificial completion is an
  upper-face proxy.  Neither can transfer its coefficient values to all
  family members.
- GGV22's emitted Proposition 4.3 systems have bracket `x^2`, whereas `LF40`
  targets a constant Jacobian.  Applying `LF40` directly to those reduced
  supports would be wrong.

Without the primary-source pre-transformation edge statement and the explicit
raw/reduced coordinate split, a family-specialized compiler is **not**
licensed.

### 5.2 Why the attack does not defeat `LF40-v1`

The primary source supplies exactly the missing semantic field: one nonzero
root, exponent seven, on the pre-transformation edge, for all internal
Proposition 4.3 branches.  The local transformation ledger explains why the
raw pair still has constant Jacobian and why `x^2` appears only after
`psi_4`.  The chart sends that base polynomial directly to
`K_rho=xi(xi-rho)^7`.  Retaining `a,b,rho` rather than borrowing the controls'
unit normalization removes the last normalization ambiguity.

No proof that the artificial upper face occurs in the family is needed.
No inference from one control is used.

## 6. Smallest next proof/falsification experiment

Before any Groebner solve, build the desk-scale `FACEPIN` custody gate:

1. reconstruct the live `8_28` record from `get_pllc`,
   `get_starting_edges`, `get_complete_chains`, and `get_mn_families`, not from
   a copied target tuple;
2. assert the unique path, step `(4,-1,3,4)`, and final `gamma=7`;
3. serialize the primary-source flip
   `y(x^4y-rho)^7 -> x(xy^4-rho)^7`;
4. expand its square and cube and compare all 37 coefficients with the raw
   lower-face slots; and
5. run the `gamma=6`, `rho=0`, native-control, and artificial-completion
   mutations above.

This is the smallest internal bridge because it turns the currently external
semantic sentence into a typed, replayable coefficient map.  It is desk-scale.
After it passes and receives different-model hostile review, compile `LF40`
as specified.  Any Groebner, saturation, or elimination of `I_LF40` is heavy
algebra and belongs on AWS.

## Scope firewall

This report closes the three-object disambiguation and licenses one exact
family-covering lower compiler contract.  It does **not** implement or solve
that compiler, promote either non-Keller control, identify the artificial
upper face with a GGV face, prove an exact parameterization of all chain
operations, prove GGV landing, or resolve JC2.
