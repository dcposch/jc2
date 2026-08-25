# TD6 generic three-center q2-beta dual adjoint

Frozen status: **producer-exact first-order theorem; hostile review pending.**

The source-typed normalized section is

```text
y=s^-1,
x=C s+V s^2+U s^3+t s^4,
p=t^15,
q_beta=t+beta*t^2+t^25,
```

with the frozen F1 orbit, zero dead stretch, and frozen pole/p-boundary
data.  This producer works exactly over
`E(C,V,U)[eps]/(eps^2)` at `beta=eps` on the open

```text
D(U * H * B3),  H=C-3U^2,
B3=4C^2U^2-4CV^2U+24CU^4+V^4-20V^2U^3+20U^6.
```

## Exact first-order result

The transport matrix is beta-independent but its affine right side is not.
The replay retains that derivative and the direct
`q_beta'=1+2 beta t+25t^24` term.  It gives transport rank `3470/3602` and
first rank `38/132`, with exact dual original-row replay.

The genuine P12 compiler has 2,893 base terms and two beta terms.  Reduction
through the varying echelon gives

```text
P12 mod first rows = -k/50 + eps*r,
k=252-342S+144S^2-36S^3.
```

Because the base value `-k/50` is a unit, the full dual remainder is a unit
exactly.  The lifted source certificate has 28 nonzero base rows and 14
nonzero lambda-prime rows.  Both differentiated contributions are retained:

```text
lambda0 * b'   : 3330 terms,
lambda' * b0   : 3330 terms.
```

The producer asserts the derivative source identity against original rows.
Omitting lambda-prime fails an explicit negative control; a separate direct
q-prime omission control also changes the exact first system.

All 71,664 termwise source-product slots pass polynomial denominator
clearing.  The complete denominator radical is contained in `U*H*B3`.
The corrected structural sentinel records 1,489 base multiplier terms,
1,248 beta-support terms, and 1,515 terms in their union; it does not impose
the base support cardinality on the differentiated support.

Consequently the generic fixed three-center open is first-order rigid
against this licensed q2 direction.  This is a dual-number statement only.
The certificate is not beta-independent, so it proves neither a finite beta
neighborhood nor the full beta line.

## AWS custody and replay

Host/tag:

```text
r6d / 100.26.198.153
td6_v32_beta_dual_r6d_20260825T0513Z
```

The source archive `archives/td6-aws-handoff-20260825-v32.tar.gz` has SHA256

```text
eab8f94c1b70a983ca71d380accf76394946d883ef13a19284318d6cb21bdf41
```

Its `SOURCE.sha256` has SHA256
`a6e4469dc67d8a001768b310ed51be4f546af9d681d48226e246f40eef959c77`;
the corrected producer source has SHA256
`dcc7003def824c0d2a88998cbf22a66f022a32714f05754c505e8d825bd91742`.
The recursive source check passed on AWS with empty stderr.

The theorem stdout SHA256 is
`13ced1e7392be3ff00c39069370b4e63e9c8ac4ffd966139e7b2ae21619f0a92`.
The job exited zero in 20:02.36 with maximum RSS 550516 KB.  Its time stderr
has SHA256
`60c6495ed5a42d2af6e05524d0313620f267ca650b8d6daa2e3add169802cdcf`
and ends in `Exit status: 0`.

After extracting on AWS with python-flint 0.9.0:

```sh
sha256sum -c SOURCE.sha256
python3 jc2/cases/td6_c1_c2_c3_q2_beta_dual_20260825/replay.py
```

## Scope quarantine

This is first-order rigidity only on `D(U H B3)` in the fixed normalized
section.  It is not a full beta-family, four-parameter-family,
neighborhood, whole-TD6, SP-2, landing, or JC2 theorem.
