# Result: small-`a` unique-`AC` `d=2,3` support/local-pole census

Date: 2026-08-26

Status: **DUAL-AWS EXACT-Q SUPPORT CENSUS PASS; NO EMPTINESS VERDICT.**

## Exact result

The cost-bounded binomial enumerator independently expanded all four source
summands through the first `C^2` target in each of the eighteen strict-cell
baselines

```text
1<=a<=9, d in {2,3},
s_min(a,2)=1 for a<=2 and 0 otherwise,
s_min(a,3)=1 for a<=3 and 0 otherwise.
```

The canonical structural inventory has SHA-256

```text
373552623cf15658efbef868be26f54dadea7712d417f884ab9c39d5475f45ce.
```

For a primitive `P/L^q` with `e_A` copies of `A`, first grade `g`, and target
`T=10+2*a+2*d`, the miner used the exact correction-depth upper bound

```text
local pole at the allocated A0 root
  <= q-max(e_A-(T-g),0).
```

All eighteen blocks contain the target

```text
(3/8)*C^2/L^2
```

as a possible local double pole at `T`.  Exactly seventeen blocks contain no
other primitive whose correction can have local pole order at least two.
The sole negative control is

```text
(a,d,s)=(1,3,1), equivalently (a,c,r)=(1,4,2),
```

where

```text
-(3/8)*R*A^2/L^2
```

starts two grades before the target and can lose both allocated `A0` factors
by its second correction.  No additional lower-load or higher-binomial
family crosses the local double-pole wall in any baseline.  The largest
target grade is 34.

The atom multiplicity bounds were derived separately from each positive
effective grade cost.  Repeating every enumeration with one extra count in
all four atom directions produced exactly the same retained signatures, so
the result does not depend on a handwritten binomial-degree cutoff.

## Dual-AWS custody

Exact rational arithmetic on Box03 and the independent `F_65521`
coefficient control on r6d both returned rc zero and the fail-closed validator
`PASS_D1_D23_SMALL_A_SUPPORT_CENSUS`.  The inventory and stdout hashes agree;
both runs used 19 MiB or less and recorded zero swap.  Source freeze SHA is

```text
aeb01ce491aeb6596d031ba9a5cd7dccfa2b3cc97d85a012b6ae151f3eb66d7f,
```

and the 30-row evidence manifest SHA is

```text
e3925672a81fea7e9403b85a46aa5651e8f196acf657d1a9dfcf85f2d824a85b.
```

## Next exact client

The census licenses one complete-source/local-row-syzygy batch with seventeen
putatively safe blocks and `(1,4,2)` as a required fail-closed negative
control.  That successor must still rebuild and bridge all seven literal
Faber rows, prove the first root allocation, retain every moving/load/target
jet, and compute the actual local `u^-2` coefficient.  The upper-bound census
alone cannot prove that cancellation is impossible.

## Firewall

This result is exact support and local-pole navigation only.  It does not
promote the hand simple-block argument, prove a source/Faber identity, close
any `d=2,3` cell, decide `(1,4,2)`, handle equality faces, or establish a fan
cover, D1, the square component, order two, maximum twelve, or JC2.
