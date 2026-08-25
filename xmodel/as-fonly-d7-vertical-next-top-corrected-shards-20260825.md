# AS F-only `D=7`: source-corrected degree-eleven carry census

**Status: PRODUCER EXACT; PROVISIONAL PENDING INDEPENDENT SOURCE/RESULT
REVIEW.**

## Headline

The source-corrected degree-eleven row still leaves a large finite branch.
A source-frozen 27-way exact F3 census on AWS gives

```text
visible predecessor states                       1,085,103
states satisfying N12={C7,D7}=0                    629,115
states also satisfying corrected Q11=0             260,847
degree-six current-digit spectator completions  190,157,463.       (1)
```

The last number is exactly `729*260847`.  This replaces the source-incomplete
old value `602343` for the degree-eleven row.  The old count omitted a
divided single-Frobenius cross term and is quarantined; its independently
reproduced `N12=629115` control remains valid.

## 1. Source-corrected row

Write the first digit as

```text
U=U0+UF,  V=V0+VF,
```

where `UF,VF` are the homogeneous degree-six Frobenius parts.  The exact
integer Jacobian expansion shows that the degree-eleven coefficient row of
the next residual is

```text
Q11 = {C7,D6}+{C6,D7}
      + ({UF,D7}+{C7,VF})/3                       (2)
```

over F3.  The divided numerator has integral coefficients because every
derivative of `UF,VF` is divisible by three.  Formula (2), including its
orientation and nonzero controls, was frozen separately in
`as-fonly-d7-next-top-carry-frobenius-erratum-20260825.md`.  The present
runner pins that source closure, constructs all twelve coefficients of (2),
and asserts that the six degree-six Frobenius directions of the *current*
digit remain absent.  They therefore contribute exactly `3^6=729`
spectator completions per visible survivor.

The runner reconstructs every solution of the frozen predecessor affine
system.  It first tests all five coefficients of the valid degree-twelve
row `N12={C7,D7}`, then all twelve coefficients of (2).  There is no random
sampling or reduced-component extrapolation.

## 2. Exact partition and certificate

The 2,187 structural bases are ordered lexicographically and partitioned
into 27 contiguous intervals of 81.  The aggregate histograms are

```text
N12 survivors per base:
  0^1804, 3^116, 6^24, 9^32, 18^4, 27^32, 54^62, 81^12,
  108^22, 162^14, 243^48, 486^2, 2187^10, 6561^2,
  19683^2, 531441^1;

corrected-Q11 survivors per base:
  0^1916, 3^132, 9^4, 27^114, 81^6, 243^4,
  2187^6, 6561^2, 19683^2, 190269^1.              (3)
```

The unique large fibre shrinks from `531441` after `N12` to `190269` after
the corrected row.  The ordered 27-leaf binary Merkle certificate is

```text
7a28180435e4e4c86e9dfb054e628bbd9070949e045a2d7b73ac30609daa2df7. (4)
```

Every leaf-output SHA-256 is printed in the frozen aggregate.  The aggregate
output itself has SHA-256

```text
e30d6af3d37b94027a7aef9aa2d39a9bba696185eb65d9c062d66055a2ae1528. (5)
```

## 3. Remote provenance

The source archive was frozen locally, transmitted as files, and checked
byte-for-byte before launch:

```text
transported source archive SHA-256
  ad285e6e6ed438d615f9360f896a1ae4be8ff17dc14328acddeadf92b525437f
runner manifest SHA-256
  9791d00f8f7862dc86d9b9b095aa5519b509ac77d864850f2d12fee0ed1f8e26
source-closure manifest SHA-256
  c2a82d548040cd303c0a33be2410e21c202b86d6a14d126e2d5749659235d84b
source FREEZE SHA-256
  4ef3449d55077db59a487a18b04a8ebd60e8484ca980acbe616b8a20d7bda1d3.
```

Execution metadata:

```text
host: Box02, ip-172-30-0-186 (34.203.207.55)
tag: as_d7_corrected_q11_20260825T003952Z
UTC: 2026-08-25T00:40:38Z--00:42:51Z
overall/aggregate rc: 0/0
per-shard cap: one CPU, 8 GiB VM, 12 hours
observed peak RSS: about 21 MB
longest shard: 2:13.68; other shards: about 12--15 seconds.       (6)
```

The source and runner checks passed and aggregate stderr is empty.  The
transported remote-results archive has SHA-256

```text
0ffaf046f8f3ac29b598cdbffe847eaa4679a2a482f1aa0d9e8879d9ef526a4d. (7)
```

## 4. Evidence tier and refusal scope

This is an exact aggregate-count/Merkle producer.  The shards are parallel
partitions of one implementation, not independent mathematical reviews.
Promotion requires independent source/result review.

Survival means only that this finite branch passes degrees twelve and
eleven of the source-corrected next residual.  The source-corrected
degree-ten row remains live and must include both divided single-Frobenius
terms and the divided double-Frobenius bracket.  Lower rows, the quotient
residual, and later Cartier tests also remain open.  There is no recurrence,
all-depth lift/no-lift, characteristic-zero, counterexample, or JC2
conclusion.
