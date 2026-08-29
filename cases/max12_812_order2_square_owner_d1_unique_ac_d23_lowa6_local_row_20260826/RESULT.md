# Result: eleven low-`a` D1 unique-`AC` `d=2,3` tails

Date: 2026-08-26

Status: **DUAL-AWS EXACT-Q PRODUCER PASS; AWAITING HOSTILE REVIEW.**

## Exact producer theorem

After the registered square/D1 source gates, over characteristic zero on
`D(p*k0)`, the seven literal Faber equations have no point in each of the
following eleven strict unique-`AC` contact tails:

| `a=ord(A)` | `d=ord(C)-a` | `ord(R)` | first `AC/L` grade `G` | checked through `T` |
|---:|---:|---:|---:|---:|
| 1 | 2 | `>=2` | 14 | 16 |
| 2 | 2 | `>=3` | 16 | 18 |
| 2 | 3 | `>=3` | 17 | 20 |
| 3 | 2 | `>=3` | 18 | 20 |
| 3 | 3 | `>=4` | 19 | 22 |
| 4 | 2 | `>=4` | 20 | 22 |
| 4 | 3 | `>=4` | 21 | 24 |
| 5 | 2 | `>=5` | 22 | 24 |
| 5 | 3 | `>=5` | 23 | 26 |
| 6 | 2 | `>=6` | 24 | 26 |
| 6 | 3 | `>=6` | 25 | 28 |

Here `ord(C)=a+d` is exact.  The coefficient denoted `gamma` below is
therefore nonzero after the first-row allocation.  The source leaves the
leading `R` coefficient uninverted, so each listed baseline represents the
entire closed tail in the third column, not only its boundary order.

## Local-row obstruction

For every listed block, `AC/L` is the unique first polar primitive, at

```text
G = 10+2*a+d.
```

Its two proper-numerator coefficients allocate the leading linear forms of
`A` and `C` to opposite roots of the squarefree moving quadratic

```text
L(z,sigma)=z^2+p(sigma)/2
```

after the finite etale root cover of `D(p)`.  The complete source through

```text
T = 10+2*a+2*d
```

has global pole order at most two.  If `h1,...,h7` are the independently
emitted Laurent rows, its numerator is reconstructed exactly as

```text
N = h1*z^3+h2*z^2+(h3+p*h1)*z+(h4+p*h2),
H = N/L^2.
```

At either Hensel root `lambda(sigma)^2=-p(sigma)/2`, the frozen Faber
connection gives the exact identity

```text
N(lambda)=Phi4+lambda*(Phi3+(p/4)*Phi1).            (1)
```

Rows 1, 3, and 4 carry no target through any listed ceiling.  The only
target at grade 28 is `mu2` in row 2, which is absent from (1).  Under each
of the two exhaustive opposite-root allocations, the compiler reduces all
coefficients of (1) below `T` to zero and its grade-`T` coefficient to

```text
(3/2)*lambda^2*gamma^2.
```

This is a unit on the exact-contact root chart.  Thus the three full rows in
(1) cannot vanish.  Both orientations are checked separately.  Because the
root cover is finite etale and surjective on `D(p)`, emptiness descends to
the unsplit chart.

## Complete source and correction custody

For all twelve compiled baselines (the eleven positive blocks and the
control below), the producer:

1. independently enumerates all four binomial source summands;
2. derives every `A,C,R`, load, moving-`p`, and target jet ceiling from the
   cost-bounded primitive inventory;
3. emits all seven literal Faber source rows with delayed `k10`, `k6`, `k2`
   and every licensed target;
4. bridges those rows modulo `sigma^(T+1)` to an independent analytic
   Laurent emitter;
5. certifies every recursive sigma quotient, the moving-root equations, the
   pole-two recurrence, both orientations, and the unit ideal.

The exact-Q and `F_65521` runs print byte-identical result streams.  Exact Q
is the characteristic-zero endpoint; the finite-field run is only an
independent host/software control.

## Mandatory routed control `E=(a,d,s)=(1,3,1)`

No emptiness or nonemptiness verdict is made for

```text
ord(A)=1, ord(C)=4, ord(R)>=2.
```

Its complete source has global pole ceiling three.  Besides `C^2/L^2`, it
contains `-(3/8)R*A^2/L^2`.  At the `A`-allocated moving root, the latter's
first two local-numerator coefficients vanish, while the exact grade-18
second correction is, modulo the Hensel-root equations,

```text
-(3/8)*(b1*lambda+b0)
       *(lambda*a1_1+a0_1+au*rho1)^2.
```

Both exact engines reconstruct this coefficient and require it to pass.
Consequently the pure-`C^2` pole-two endpoint is deliberately refused and
`E` is routed to a dedicated pole-three/local-collision successor.

## AWS custody

Box03 exact Q and r6d `F_65521` each return engine rc zero and
`PASS_D1_D23_LOWA6_LOCAL_ROW_ELEVEN_EMPTY`.  Compiler stderr is empty,
there are no Singular diagnostics, and both engines record zero swap.  Full
launch/resource custody is in `AWS_LAUNCH_METADATA.md`; all retrieved bytes,
including the quarantined V3 failed preflight, are pinned by
`EVIDENCE.sha256`.

## Firewall

This producer closes exactly the eleven rows in the table, after its cited
upstream gates.  It does not decide `E`; the `a=7` tie
`k6*C/L + AC/L`; the `a=8,9` load-first cells; the grade-32/34 row-4 target
shadows; an equality face; a positive-order leading load; `p=0`; `k0=0`;
another D1 face; a terminal/global chart; the whole square component; order
two; `(8,12)`; maximum twelve; or JC2.  In particular, nothing here may be
extrapolated through the six `a=7,8,9`, `d=2,3` timing exceptions.
