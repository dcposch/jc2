# AS B9 maximum-twelve survivor through `Z/27`

Status: **producer-exact finite-depth theorem; hostile review pending**.

Put `u=x+y^3`.  The two integer polynomials

```text
P=u-u^3+18*u*y,
Q=y+u^4+3*u^2*y+18*y^2
```

have actual partial `y`-degrees `(9,12)`, reduce modulo three to

```text
G9=(u-u^3,y+u^4),
```

and satisfy `det J(P,Q)=1 (mod 27)`.  In the determinant-one source
coordinates `(u,y)`, direct integer expansion is

```text
det J(P,Q)
 = (1-3u^2+18y)(1+3u^2+36y)-18u(4u^3+6uy)
 = 1-81u^4+54y-162u^2y+648y^2.
```

Thus every nonconstant coefficient is divisible by `27`.  At the intermediate
level,

```text
(u-u^3, y+u^4+3u^2y)
```

has determinant `1-9u^4`, hence determinant one modulo nine.  In the W3
calculation the product's `-9u^4` term is cancelled by subtracting the cross
term `72u^4`, which is `+9u^4 (mod 27)`.  The older `+18u^4` shorthand is
incorrect and is not used here.

The special fibre is etale and noninjective: `(0,0)` and `(2,2)` are distinct
`F_3` points mapping to `(0,0)`.  The replay expands in `Z[x,y]`, retains the
mixed integer binomial terms in `(x+y^3)^3`, and checks every determinant
coefficient.  Omitting either `18*u*y` or `18*y^2` is detected.

## AWS custody

The identical source ran under a 1 GiB virtual-memory cap and 120-second
timeout on two hosts with tag `as_b9_max12_w3_20260825T1607Z`:

| host | remote path | UTC end | rc | max RSS | stdout SHA-256 |
|---|---|---|---:|---:|---|
| Box02 `34.203.207.55` | `/home/ubuntu/runs/as_b9_max12_w3_20260825T1607Z` | `2026-08-25T16:05:40Z` | 0 | 14,620 KiB | `f9e55a4f3cfc6c3b85b2d4c9ec724e0d757e083b0e82e0ff0e387d7125ea1aef` |
| Box03 `98.80.65.144` | `/home/ubuntu/runs/as_b9_max12_w3_20260825T1607Z` | `2026-08-25T16:05:44Z` | 0 | 15,192 KiB | `f9e55a4f3cfc6c3b85b2d4c9ec724e0d757e083b0e82e0ff0e387d7125ea1aef` |

Both source checks passed byte-identically, both replay stdout files are
byte-identical, and both terminal markers are
`AS-B9-MAX12-W3-SURVIVOR PASS`.  The stderr hashes differ only because
`/usr/bin/time -v` reports host-specific resource fields.

## Replay

Heavy or uncertain computation is AWS-only.  On an AWS host:

```sh
cd cases/as_b9_max12_w3_survivor_aws_20260825
sha256sum -c SOURCE.sha256
ulimit -v 1048576
timeout 120 /usr/bin/time -v python3 replay.py
```

## Scope firewall

This is one explicit fixed-support lift over `Z/27`.  It does not classify
the whole W2 fibre, produce a `Z/81` or all-depth branch, give a `Z_3` or
characteristic-zero polynomial map, prove nonautomorphy in characteristic
zero, settle either maximum-twelve frontier, enter the TD6 normalization, or
prove or disprove JC2.  Its immediate exact successor is the complete next
digit over this fixed W3 point, followed—if necessary—by the whole W2-fibre
Kuranishi/Fitting gate under a preregistered degree/support cap.
