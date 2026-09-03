# FIXED-N6 first-page driver notes

Status: **PROVED-HERE / UNREVIEWED** for the elementary count, determinant,
and frontier algebra; **WITNESS-ONLY** for every matrix using the extra
non-proper completion below.

## What can and cannot be emitted

The frozen `GLOBAL-INTERPOLATION/1.0` input schema requires all `n` branch
series, all first contacts, the complete Galois action, coefficient sharing,
tail support, and a precision guard.  The FIXED-N6 charge supplies a numerical
skeleton, one orbit of rigid proper bottom stars, and only the *number* of
non-proper roots.  It does not supply the remaining required data.  Therefore
there is no family-intrinsic associated-graded matrix, rank, Schur complement,
or tropical basis to emit.

The frozen emitter also trusts `orbits.O.verified=true`; it ignores an
`expected_size` and a supplied generator.  In particular,
`custody-partial-orbit.json` has two displayed members but `expected_size=3`
and is accepted with exit status zero.  This violates the requested custody
control.  The preflight in `fixedn6_driver.py` checks the `(10),V2=1` packet
type, the exact rigid bottom star, size, bijectivity, and single-cycle closure
before reducing orbit equations.  It refuses
`L5-k12-partial-orbit.json` with

```text
REFUSED[ORBIT-SIZE]: L=5 has (10)-orbit size A2=18; requested k=12
```

The compact records in `witness-decorations.json` pass only
`ACCEPTED[PROPER-PACKET-CUSTODY-ONLY]`.  They deliberately say
`full_globalinterp_decoration=false`; no non-proper Galois action or tail
sharing has been invented.

## Exact packet and block counts

For a single nonzero `(10)` orbit,

```text
k=A2=3(5L-1)/4,                 N=k/2,
proper roots=3k,
major residual roots=15L-3k=3(5L-k),
top minor roots=21L-15L=6L,
total non-proper=21L-3k=3(7L-k).
```

| L | k | N | proper | major residual | top minor | non-proper | DEG vanish rows |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 18 | 9 | 54 | 21 | 30 | 51 | 34 |
| 13 | 48 | 24 | 144 | 51 | 78 | 129 | 90 |
| 21 | 78 | 39 | 234 | 81 | 126 | 207 | 146 |
| 29 | 108 | 54 | 324 | 111 | 174 | 285 | 202 |

The minimal skeleton uniformizer denominators are respectively
`R=36,48,156,108`; `(q_delta2,q_delta1,gap)` are
`(14,21,7)`, `(19,28,9)`, `(62,91,29)`, `(43,63,20)`.

## Resource-cap refusal for the frozen quadratic lift

In Moh total-degree mode a top-minor branch has valuation `-R`.  Already at
`qmax>=0`, `globalinterp.py` sets `desired_power[r]>=R*m` for each
`r=2,...,m`.  Thus the number of branch-power variables from top-minor roots
alone is at least

```text
top_minor * (m-1) * (R*m+1).
```

For the four cases this lower bound is `5,218,470`, `123,348,966`,
`1,693,244,070`, and `3,090,039,030`, before product, inverse, time, and
evaluation variables.  A conservative preflight therefore refuses the full
frozen lift as not credibly fitting the 6 GB desk cap; this is not an observed
out-of-memory event or a formal byte lower bound.  The scalable computation
uses the exact GRS determinant projection requested in the charged reading.

## WITNESS-ONLY valuation completion and frontier check

To exercise the scalable code, `fixedn6_driver.py` makes these extra choices:

- the `k` proper discs are distinct at `delta2` and have three normalized
  jets at `delta1=7/12` with `p_g=pi^3-pi`;
- all `r=3(5L-k)` residual-major roots have pair contact
  `rho=delta2+1/(6k)`;
- all `6L` top-minor roots have pair contact `rho_top=2`;
- cross contacts are `delta2` inside the major `D2` and `-1` across the top
  major/minor split.

These contact choices pass the non-proper frontier inequalities.  For a
residual-major root,

```text
ord D_i=(r-1)rho+3k delta2-6L < -1
```

because the equality threshold is exactly `rho=2/5` and
`delta2<rho<2/5`.  For a top-minor root,

```text
ord D_i=(6L-1)*2-15L=-3L-2 < -1.
```

This is only a valuation-tree surrogate.  Its residual coefficients and
their complete Galois permutation are not supplied, so it is not promoted to
a polynomial or even to a full decorated input for the frozen emitter.

## Conditional first-page ranks

There are two inequivalent meanings of “unknown”, and the charged data do not
select between them.

1. **Raw leaf-coordinate page.**  Give each of the three separated leaves per
   rigid star its own coefficient channel.  The proper matrix is confluent
   Vandermonde of size `(7L-1) x 3k`.  It has exact row rank `7L-1` over Q.
   A square pivot uses two jets from `(7L-1)-k=(13L-1)/4` discs and one jet
   from the other `(L-1)/2` discs.  Its determinant is
   `prod_(i<j)(j-i)^(a_i*a_j)`, nonzero over Q.  Ranks and nonzero determinant
   residues agree over `1009,1013,1019`.  Cokernel is zero and the non-proper
   Schur increment is zero for all four L.

2. **One rigid-star amplitude per disc.**  The proper block is a Vandermonde
   of rank `k`, with growing cokernel
   `(7L-1)-k=(13L-1)/4 = 16,42,68,94`.  In the explicit valuation surrogate,
   the residual-major split occurs before `delta1`, giving
   `3(5L-k)` active residual channels, while the top-minor block contributes
   one unresolved aggregate.  The non-proper Schur ranks are exactly
   `16,42,68,94`, the combined ranks are `34,90,146,202`, and the combined
   cokernels are zero.  Thus this surrogate is **repaired by the non-proper
   interface**, but that conclusion depends on its coefficient-sharing model.

The exact modular ranks and pivot residues are in `witness-results.json`.

## Tropical sensitivity

For the raw scaled GRS matrix,

```text
val det(P_S) = sum_{i<j in S} c_ij - sum_{i in S,j!=i} c_ij
             = -C_all + sum_{i<j in T} c_ij,
```

where `T` is the complement of the basis.  The driver minimizes the last sum
exactly by dynamic programming over the declared laminar tree.

With `rho_top=2`, minimum-basis compositions `(proper,major residual,top
minor)` are `(27,0,7)`, `(70,0,20)`, `(114,0,32)`, `(158,0,44)`.  Changing
only the still non-proper top-minor contact to `rho_top=5/2` changes them to
`(24,0,10)`, `(64,0,26)`, `(104,0,42)`, `(144,0,58)`.  Both choices satisfy
`ord D_i<-1`.  Hence neither the minimum-weight bases nor their valuations are
determined by the pinned family data.

## Commands

```text
python3 fixedn6_driver.py validate L5-k12-partial-orbit.json
python3 fixedn6_driver.py certificate 5
python3 fixedn6_driver.py all
python3 fixedn6_driver.py controls
python3 ../../globalinterp-drivers-20260902/globalinterp.py controls
```

The wrapper `controls` command exercises the same scalable consecutive-moment
projection used by the rank audit, at exact rational specializations of the
universal monic-root identity.  For `(y,x+y^3)` and `(y,x+y^5)` it emits all
homogeneous moment values as zero and the following monic moment as one;
for `g=y^2-x^2-x` it emits the expected NO-RESIDUE failure at `t^1` with
residues `+1/2,-1/2`.  This closes the raw-projection regression only.  A full
decorated family initial-form emitter is still not determined by the inputs.
