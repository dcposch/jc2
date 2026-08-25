# TD6 q2-beta rational raw-line closures

Frozen status: **producer-exact whole-line closures; hostile review pending.**

This package concerns only the fixed source-typed normalized A3 center
section with `q_beta=t+beta*t^2+t^25`.  It directly rebuilds three rational
lines left by the raw `H=0` and `B3=0` denominator atlases:

```text
V=0, C= 3U^2       (the V=0 branch inside H=0),
V=0, C=-U^2,
V=0, C=-5U^2       (the two non-U branches of B3|_(V=0)).
```

The last two arise from the executable exact factorization

```text
B3|_(V=0)=4U^2(C+U^2)(C+5U^2).
```

## Exact results

On `V=0,C=3U^2` and `V=0,C=-5U^2`, V45 gives transport rank
`3470/3602`, first rank `38/132`, and exact genuine-P12/original-first-row
identities.  In both cases the P12 remainder is a three-term affine-beta
polynomial with constant part `-k/50`; its two-term beta tail is cancelled
by the exact staged `N13=(k/25)beta` contribution without dividing by beta.
The resulting residual is the constant unit `-k/50`.  All raw, first-row,
relation, and termwise-source denominators are powers of `U`; the two source
slot audits check 29,097 and 28,570 products respectively.

The line `V=0,C=-U^2` is stronger and lower-rank.  The original V45 harness
failed closed because it expected first rank 38 but obtained rank 37 and one
dependent row.  V46 preserves that output as a negative harness control and
adjudicates the dependency exactly.  The row is `('X-2',12)`, its residual
has beta-degree zero, and its 13-row original-source combination has monic
compatibility gcd one with an exact Bezout replay.  The entire certificate
denominator is `U^6`, with no beta root or other factor.

Thus every line is empty on `D(U)` for all beta.  Its `U=0` endpoint lies in
the separately frozen whole raw `U=0` divisor, already empty for every beta
with a unit compatibility ideal.  Consequently all three whole
set-theoretic rational lines are empty in this fixed source scope.

## AWS custody

The source archives and manifests are:

| version | archive SHA256 | source-manifest SHA256 | producer SHA256 |
|---|---|---|---|
| V45 | `e9dd234d861e9aa64a3087f2307186f20468e8a14296407ed01908ad34787164` | `1a286d49e53710100ea7f79549c28c230103b3f710f5a9b14cfabbab7feb4580` | `7e1370834460e2bc3123631825f04cb04a0b457a14449985635f3d0af86f8dd1` |
| V46 | `c3fab24308e36ffad4addf13c9b56e026e1eb96ac43ccad79aa01132adaa7487` | `2fb26fcb1bf32fbb6d3b1e0212fef066b2ada2ed483dfca11a3e6812a005b10f` | `9b1670abf55a20f26f02abcc593083ce07dd2b1e4afa0571ac8b9a0f890203c7` |

All runs used r6d, Python 3.12.3, python-flint 0.9.0,
`PYTHONHASHSEED=0`, and passed their source checks.

| line | version/rc | stdout SHA256 |
|---|---:|---|
| `V=0,C=3U^2` | V45/0 | `61bb5fedba625711115ed7665a6ed23f37a54b0cff44356ecac0be717668ed4e` |
| `V=0,C=-U^2` harness control | V45/1 | `f45da292c81b2793978eaf45183cb01f883d3d3681767ffa4edb52360ca4c3ad` |
| `V=0,C=-U^2` unit incompatibility | V46/0 | `01fa0f2ef212f1280f7b1cc4530da867df331b0892053c44f3edf89e1bbf6706` |
| `V=0,C=-5U^2` | V45/0 | `0be0c4093c27d21778853908afc90a3021831cb75a926a60981cffa4e166e8e2` |

## Scope quarantine

This package closes only these three rational center lines for the fixed
q2-beta source.  It does not by itself close generic `H=0` or `B3=0`, vary
other center/boundary/dead-stretch/F1/pole moduli, kill whole TD6 or SP-2,
prove a landing theorem, or resolve JC2.
