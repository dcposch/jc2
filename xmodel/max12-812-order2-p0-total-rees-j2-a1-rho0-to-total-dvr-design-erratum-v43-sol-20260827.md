# V43 erratum: literal-total alphabet, corpus map, and Singular preamble

Date: 2026-08-27  
Author: Sol total-lift design lane  
Status: **EXACT CORRECTION; ORIGINAL PRODUCER AND FABLE5 REVIEW PRESERVED**

## Custody

This is an additive erratum.  The reviewed producer remains byte-immutable:

```text
e3d263d5c0006bc4f05c5b7ff17bfcbd68bab52f7c1d3ccb5d323facd94448f7
  xmodel/max12-812-order2-p0-total-rees-j2-a1-rho0-to-total-dvr-design-sol-20260827.md
a836a978a6b9f05370322fb39c2cf1c45fa6907c337f10ef3ee9456d2e2f0f6d
  xmodel/max12-812-order2-p0-total-rees-j2-a1-rho0-to-total-dvr-design-hostile-review-fable5-20260827.md
```

The original report's ring/map theorem and the Fable5 verification of it
remain correct after replacing the mistaken 65-variable total-support census
by the typed census below.  The discovered variable has positive sigma
weight, so it does not change the load-bearing assertion that `rho` is the
only weight-zero variable.

## 1. Correct ambient ring and specialization map

There are two support alphabets:

```text
X19^tot = X19^0 union {ez9},       |X19^tot|=66, |X19^0|=65,
S       = Q[rho,X19^tot],
sp      : S -> S0=Q[X19^tot],      rho |-> 0.
```

`X19^0` is the support of the frozen rho-zero rows consumed by V37/V42.
The specialized ideal `J0=sp(J)` is the scalar extension of that frozen
65-variable ideal along

```text
Q[X19^0] -> Q[X19^tot].
```

Thus `ez9` is a faithful polynomial-extension spectator in `J0`; V42's
rho-zero saturation/radical conclusion extends unchanged.  It is inaccurate
to call `ez9` itself rho-torsion.  Rather, its only source-row coefficient is
divisible by `rho^2`, so its support disappears under `sp`.

## 2. Literal discrepancy and exact adjudication

Regenerating the actual-total rows through grade 19 from the V35 source-series
emitter, applying only

```text
rs=cs=c0=c1=a0=0
```

and then converting `t=rho^2`, gives exactly one monomial containing the
general-only variable:

```text
Tg19_2 contains (3/8)*t*a1*ez9
         =       (3/8)*rho^2*a1*ez9.
```

The canonical one-record inventory has SHA-256
`6cae87a2c5440057750e03a43d558d0f08c93decb35db12520d27454bd15e114`.
The canonical total-`t` polynomial hash of `Tg19_2` is
`cc8957b85398036791e8193bc5864897412bdec6e30f2c363cce7bb345e31209`.
Its rho-zero frozen file hash is
`c0e3e218aad73bf01373edceed7d83c4e9b0820ea0d9f0b8ab15f903018429dc`.
All 70 regenerated rows still bridge exactly to their frozen images after
`rho=0`.

Fable5's claimed "full frozen general-rho corpus" was actually the corpus
addressed by the V37 loader.  That is sufficient for V37/V42, but it is not a
literal-total corpus at grades 16--19: each of the V28, V30, V33, and V35
producer programs explicitly defines

```text
killed = parser.J1 | {a0,rho}.
```

Consequently the stored `Tg19_2_q.poly` is already specialized at `rho=0`,
and loading it "without an additional rho kill" cannot recover the discarded
`rho^2*a1*ez9` term.  V43 instead regenerates from `build_source_series_19`
and `build_row` before killing rho, then separately checks the rho-zero
bridge.  This fully explains the apparent conflict.

## 3. Corrected preflight dimensions

The first compiler failed closed when it compared total support 66 to the
frozen support 65.  The corrected compiler derives all complementary
monomials from `X19^tot` and proves `X19^0 subset X19^tot`.  Registered r6d
preflight returned:

```text
nonzero total rows                         59
all weight-30 products                460485
all total support monomials          1370353
total target component products       224938
total target component monomials      687758
total target component incidences    8567907
rho=0 target component products        26200
rho=0 target component monomials       66076
rho=0 target component incidences      616679
maximum t-degree in a source row            4
```

These sizes disqualify V37's rank-squared dense Flint route as the primary
exact solver.  V43 therefore prioritizes a sparse rho-zero dual and a small
direct `a1=1` unit/lift computation on the union of the cascade rows.  The
complete fixed-weight module above remains the definition; no support is
truncated.

## 4. Fable5's fail-closed syntax finding and repair

Fable5 correctly found that Singular does not accept `syz(module,vector)`.
The generated toy controls are repaired additively by forming augmented
modules first:

```text
module NE=NEG,NT; module NZ=syz(NE);
module PE=POS,PT; module PZ=syz(PE);
```

The live module already used the valid augmented form `E=M,T; Z=syz(E)`.
The defect could only stop a run before a verdict; it could not create a false
certificate.  No V43 decision solve is promoted until the repaired source is
frozen and replayed.

