# AWS result — `(8,12)` order-two `U=2,[6,2]` exact tail compiler

Date: 2026-08-25  
Status: **EXACT SEVEN-TAIL COMPILATION PASS; STRICT SATURATION EMITTED AND
RUNNING SEPARATELY; TAYLOR FAMILIES NOT COMPILED**

## Result

The frozen compiler for the canonical source

```text
h=x^6(x-1)^2,       u^2=x^3(x-1),       T=u/x^2,
T^2=(x-1)/x,        r_7=(j/4)T
```

completed on registered AWS host `r6d`:

```text
tag:       max12_812_order2_u2_62_compile_v1_20260825T223800Z_r6d
host:      ip-172-30-0-45
job dir:   /home/ubuntu/jobs/max12_812_order2_u2_62_compile_v1_20260825T223800Z_r6d
start:     2026-08-25T22:38:35Z
end:       2026-08-25T22:38:37Z
rc:        0
elapsed:   2.16 s
max RSS:   23,448 KiB
Python:    3.12.3
```

The result token is

```text
PASS-MAX12-812-ORDER2-U2-62-TAIL-COMPILER.
```

The compiler reconstructed the reviewed Faber polynomials
`F_12,F_10,F_6,F_2`, then all seven exact sparse tails, verified the inverse
root through the required range and every tail/load Rees weight, and emitted
the complete global strict-Rees Singular input.  It did not execute that
saturation.

## Frozen sources and custody

```text
840a12e29386d37801f986e39273c3fb34f5542019cc1da7043ee1730dcb31f2
  cases/max12_812_order2_u2_62_strict_rees_20260825/compile_rees.py
f0630c6ce8131494e2c9df66927c747186358032aba8fcf2a60abd88ae2f6c72
  cases/max12_812_order2_u2_62_strict_rees_20260825/run_compile_aws.sh
```

and the exact client source is

```text
e5e3472f052b2ae932daefc9dec7a17106ca4c13f8b920ba59da627d0653fec7
  xmodel/max12-812-order2-u2-62-strict-rees-client-20260825.md
```

The shipped source archive has SHA-256
`20a5a5f3d36e5a369301b867860429c0d4eb9c61a23a139f4b88f06aeb764844`.
The retrieved evidence is frozen by

```text
cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v1/MANIFEST.sha256
```

and verifies in full.

## Exact outputs

```text
all seven tails:
6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8

result.json:
d5a3bc080900a244d8fc8e04b48da76bcc9fe8defc19ad7a61534d6aa8335105

tails.json:
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848

strict_rees.sing:
e3cbb667cdd390bac3981ed4aaeaa032bf1de6c83061c6890512758179ca70a7
```

Tail support sizes and individual hashes are:

| tail | support | SHA-256 |
|---:|---:|---|
| 1 | 36 | `a85e9b2c45a70eecc38028402cf617183475371025f5d75ab57b39442fdb6a54` |
| 2 | 54 | `86dd2a853424343bfea8a5e26138697dcbcef150fcc2189182c06758045e38a8` |
| 3 | 58 | `3e5d0ef0c680c50f87a0200bad1f5b9e18259cdae10310647bb9cefdf93cfcb3` |
| 4 | 81 | `fc073a8a1cdf981c5991a3922080d7544b481f559636f0a152c5d715946c0167` |
| 5 | 89 | `b325e0bc938d1c38f02649fa01365b86b4141bc04e33542a694f98b7e6a6c604` |
| 6 | 120 | `adef4cb0141051f1dd6e695c63f925b7d0b923c8a415febbbd796399923e36f7` |
| 7 | 131 | `fdc5af9ea401da3bb6f872175702a082b1d61fc644f9870f29fd78915816bc4e` |

## Next gate and scope firewall

The emitted exact input is now running on registered AWS `r6d` as

```text
max12_812_order2_u2_62_strict_rees_sat_v1_20260825T225334Z_r6d
```

under a 14,400-second timeout and 256-GiB virtual-memory cap.  Its input hash
is the exact `strict_rees.sing` hash above.  That lane is a separate result
and is not anticipated here.

This compilation pass proves only that the exact source-typed seven tails
and strict-Rees input were reconstructed and emitted with their licensed
weights and targets.  It is not a saturation verdict, does not compile
either finite Taylor family, does not construct a rational section or a
Keller pair, does not close the order-two client or `(8,12)`, and proves
nothing about maximum twelve or JC2.
