# Preregistration: residual D1 `a=8,9`, `d=2,3` grade-38 tail

Date: 2026-08-26

Status: **PREREGISTERED SHARDED EXACT-Q AWS PRODUCER WITH TWO FRESH PRIME CONTROLS PER CELL.**

## Exact cells

Compile independently, with no support-miner emptiness import,

```text
(a,d,c,r_floor) = (8,3,11,8), (9,2,11,9), (9,3,12,9).
```

Here `ord(A)=a`, `ord(C)=c` is exact, and `ord(R)>=r_floor`.  The already
separate `a=8,d=2` producer is not composed into this theorem.

## Controlling invariant

For each cell, independently expand all four binomial source summands
through absolute grade 38 with cost-derived atom bounds and padded-cutoff
sentinels.  The preregistered primitive counts, pole ceilings, and first
later pole-four grades are

| cell | primitive families through 38 | max pole | first pole >=4 |
|---|---:|---:|---:|
| `a8d3` | 17 | 3 | 41 |
| `a9d2` | 13 | 3 | 42 |
| `a9d3` | 13 | 3 | 43 |

Every normal, moving-`p`, load, and target jet ceiling must be derived from
that complete inventory.  All seven frozen literal source rows must bridge
modulo `sigma^39` to an independently emitted Laurent source.

The already promoted universal odd-pole theorem then licenses, separately
for each certified pole-three source,

```text
Phi7+(p(sigma)/4)*Phi5+(3*p(sigma)^2/32)*Phi3
    +(5*p(sigma)^3/128)*Phi1 = 0 mod sigma^39.
```

Rows 1,3,5 have no targets.  The only odd target is `J/4` in row 7 at
grade 38, so the same combination of full equations must be exactly
`-sigma^38*J/4 mod sigma^39`.  Adjoining `iJ*J-1` must give the unit ideal
before radicals.

## Closed `R` tails and target shadows

Compile at `ord(R)=a` with an independent homogeneous factor `eta` on every
`R`.  Verify the recurrence polynomially in `eta`; substitution
`eta=sigma^s`, `s>=0`, covers every `ord(R)>=a` and only delays source
families.  Do not invert `eta` or either leading `R` coefficient.

Retain row-2 targets through grades 28--38, row-4 targets through 32--38,
row-6 targets through 36--38, and row-7 `J/4` at 38.  The order-three odd
functional must bypass, not delete, the row-2/row-4 load and target shadows.

## Execution and firewall

Shard each cell.  Compile/run exact Q and independently `F_65521` and
`F_65519` on AWS, with fresh tags, caps, timeouts, source freezes, rc and
diagnostic sentinels, and zero swap.  Exact Q alone is the characteristic-zero
endpoint; primes are software/host controls.

A PASS closes only the three listed strict `A,C` cells and their closed
`R` tails, after the cited square/D1 gates on `D(p*k0*J)`.  It does not
cover `E=(a,d,r)=(1,3,2)`, an equality face, another `(a,c)` cell, positive
order outside the licensed load series, `p=0`, `k0=0`, another D1 face, a
terminal/global chart, the whole square component, maximum twelve, or JC2.
