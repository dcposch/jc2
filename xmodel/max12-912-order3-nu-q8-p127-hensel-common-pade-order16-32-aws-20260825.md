# Selected-Q8 simultaneous common-denominator gate at orders 16 and 32

Date: 2026-08-25  
Status: **PRODUCER-EXACT BOUNDED NEGATIVE; review required**

## Result

The exact moving-v Hensel outputs at orders 16 and 32 contain seven lifted
series, each represented in the basis `1,v,...,v^189`. An AWS Box03 replay
parsed all `7*190=1330` scalar `s=w-25` sequences and proved that every
order-16 coefficient is byte-mathematically identical to the corresponding
prefix of the independently computed order-32 lift.

For a scalar common denominator

```text
D(s)=1+d1*s+...+dd*s^d,
```

the replay solved all simultaneous Padé equations requiring every
`D(s)*Y_i(s,v)` coefficient above numerator degree `m` to vanish. It found:

```text
order 16: no unique solution for any 1<=d<=15 and 0<=m<=14
order 32: no unique solution for any 1<=d<=31 and 0<=m<=30.
```

Thus there is no uniquely determined scalar common denominator in either
complete tested rectangle. In particular, order 16 supplies no candidate
that survives the order-32 holdout. This is the expected bounded negative
after the earlier 123-fibre alias ceiling; it directs reconstruction to order
64 and above rather than licensing a low-degree formula.

The checker includes a synthetic rational family with known denominator
`1+2s+3s^2`, recovers it exactly, and rejects a one-coefficient holdout
perturbation. A separate perturbation proves that the cross-order prefix
comparison fails closed.

## AWS custody

Box03 completed rc zero in under one second. Pinned hashes are:

```text
common_pade.py       acc005c798d966297bb3b1a5a9fa64f3e83d71a164f6c2b4d7806473f841e3b5
run_remote.sh        3f5ed92c22c8721e49fb474b8c5619bef14be1307af4696c60e584431ec299f8
order16 series       d4a00d5f5922022fa6de0e2e32398e923128b297100a37e1b688f067b4bfc1cb
order32 series       a2934a4f02f8e5fad42154dcd69a80cb953db8666761945b9282f45326c92eaa
reconstruction.json  63f7fbb230117bd68f1b7ad7af99cf079377428055910b67344efebfac5b44af
result.out           c373d3c38586abd2ec467aabeff083553e0ab99242475c171a01c1b926789088
run.meta             7b09e67f51342e7fa7a16e37bf0c8fd42556ef982f2e313760c0f5c5591cd0d0
stderr.log           79f478fd8a4f834b50d9f41dcab44db946c03a5feb6b95fc6bd5512957ae2083
```

## Exact scope

The negative is only for a denominator regular at `s=0` (normalized by
`D(0)=1`) with `d<=31` and coordinate numerator degree `m<=30`, shared across
all 1,330 sequences. This is the correct local form for a rational graph
regular at the selected base fibre, but higher degrees remain completely
open. A rank-deficient family of fits is deliberately not called a
reconstruction; only a unique denominator was admissible.

No recurrence, quotient component, rational graph, original-row identity,
characteristic-zero component, or trajectory conclusion is obtained.
Order-64 and higher outputs must be searched afresh; any future recurrence
must be validated on a strict higher-order holdout and then substituted
exactly modulo `H` in every original quotient row.
