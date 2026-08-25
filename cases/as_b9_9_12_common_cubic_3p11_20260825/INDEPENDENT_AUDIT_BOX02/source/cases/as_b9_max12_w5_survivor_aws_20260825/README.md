# AS B9 fixed-D12 survivor through `Z/243`

Status: **producer-exact finite-depth theorem; hostile review pending**.

Put `u=x+y^3`.  Starting from the frozen `Z/27` point, define

```text
P4 = u-u^3+18*u*y,
Q4 = y+u^4+3*u^2*y+72*y^2.
```

Exact expansion gives

```text
det J(P4,Q4)=1+81*(-u^4+2*y-6*u^2*y+32*y^2),
```

so this is a `Z/81` lift.  Its divided residual modulo three is
`2*(u^4+y+y^2)`.  For

```text
D(R,S)=R_x-u^3*R_y+S_y
```

the two exact mod-three primitives

```text
D(2*u*y,y^2)=u^4+y,
D(x*y^2,x^4*y^2+x*y^11)=y^2
```

give the registered next digit.  Therefore

```text
P5 = P4 + 81*(2*u*y+x*y^2),
Q5 = Q4 + 81*(y^2+x^4*y^2+x*y^11)
```

has determinant one modulo `243`.  Both its actual total degrees and actual
partial `y`-degrees are `(9,12)`.  The replay checks all 33 exact integer
determinant terms, both linearized identities, source reduction, and a
negative control omitting the full new digit.

## AWS custody

The identical source ran under a 1 GiB cap and 120-second timeout with tag
`as_b9_max12_w5_20260825T1617Z`:

| host | remote path | UTC end | rc | max RSS | stdout SHA-256 |
|---|---|---|---:|---:|---|
| Box02 `34.203.207.55` | `/home/ubuntu/runs/as_b9_max12_w5_20260825T1617Z` | `2026-08-25T16:10:57Z` | 0 | 14,616 KiB | `86afa339d260ac31d09a1ec59cd189c5adaa02212acd3d7c40bcd4c07678a853` |
| Box03 `98.80.65.144` | `/home/ubuntu/runs/as_b9_max12_w5_20260825T1617Z` | `2026-08-25T16:11:01Z` | 0 | 14,772 KiB | `86afa339d260ac31d09a1ec59cd189c5adaa02212acd3d7c40bcd4c07678a853` |

Both source checks and stdout files agree byte for byte.  The payload SHA is
`04ccf4367c5e321625e41f39faa37c69afdebdcbdc65af4ca66f14094b668850`.

## Replay

Run only on AWS:

```sh
cd cases/as_b9_max12_w5_survivor_aws_20260825
sha256sum -c SOURCE.sha256
ulimit -v 1048576
timeout 120 /usr/bin/time -v python3 replay.py
```

## Scope firewall

This is one explicit fixed-support branch through `Z/243`.  It is not the
complete W2 fibre, a compatible all-depth tower, a `Z_3` or characteristic-
zero polynomial map, a counterexample, a maximum-twelve theorem, TD6, or
JC2.  The next exact task is the divided `Z/243 -> Z/729` residual and its
complete degree-twelve linear correction equation; later promotion requires
hostile review independent of these producer replays.
