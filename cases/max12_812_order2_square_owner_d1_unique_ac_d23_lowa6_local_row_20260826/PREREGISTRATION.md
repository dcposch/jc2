# Preregistration: D1 unique-`AC` `d=2,3`, low-`a` local-row batch

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS EXACT-SOURCE PRODUCER.**

## Literal scope

Compile the twelve strict-cell baselines

```text
1<=a<=6, d=c-a in {2,3},
s_min=1 if a<=d and 0 otherwise, r>=a+s_min.
```

The intended positive set is the eleven baselines other than
`E=(a,d,s_min)=(1,3,1)`.  `E` is a mandatory negative control, not a
predicted nonempty cell.  The source uses arbitrary `R` jets without
inverting their leading coefficient, so each baseline is the closed tail
`r>=a+s_min`.

## Why this is a separate batch

For every `a<=6`, unloaded `AC/L` is the unique first polar primitive.
Hence its two numerator equations allocate the nonzero leading linear
forms `A0,C0` to opposite roots of squarefree
`L0=z^2+p/2` on `D(p)`.  This ceases to be the literal source statement at
`a=7`, where `k6*C/L` ties `AC/L`; at `a=8,9` that load precedes `AC`.
Those six high-threshold `(a,d)` blocks are excluded from this producer.

## Exact invariant

Mechanically enumerate and aggregate all four binomial source summands
through

```text
G=10+2*a+d, T=10+2*a+2*d.
```

Derive every normal, load, moving-`p`, and target jet ceiling from that
inventory.  Rebuild all seven frozen literal Faber source rows and compare
them coefficientwise, modulo `sigma^(T+1)`, with an independently emitted
analytic Laurent source.

For each positive block the complete source has global pole ceiling two.
If `h1,...,h7` are its Laurent rows and `p(sigma)` is the moving quadratic
coefficient, reconstruct

```text
N = h1*z^3+h2*z^2+(h3+p*h1)*z+(h4+p*h2),
H = N/L^2.
```

For either Hensel root `lambda(sigma)^2=-p(sigma)/2`, verify the exact
moving-root identity

```text
N(lambda)=Phi4+lambda*(Phi3+(p/4)*Phi1).             (*)
```

Rows 1,3,4 carry no target through these positive ceilings (`T<=28`, and
the sole grade-28 target is `mu2` in row 2).  Under the two opposite-root
allocations, the grade-`T` coefficient of (*) must reduce, modulo every
Hensel-root equation, to

```text
(3/2)*lambda^2*gamma^2
```

in both orientations.  It is a unit on `D(p*gamma)`, contradicting the
three full source rows.  This is an exact local-row syzygy, not a support
upper bound or radical calculation.

At `E`, require global pole ceiling three and independently reconstruct its
`L^3` numerator.  The actual local double-pole coefficient must contain
the second correction of `-(3/8)R*A^2/L^2`; the producer must refuse the
pure-`C^2` endpoint.

## Acceptance and controls

1. Exactly twelve baselines, eleven positive and one `E` control.
2. All source/freeze ancestry rehashes before compilation.
3. Cost-derived atom bounds agree after one-count padding.
4. Complete seven-row literal/analytic bridge and denominator recurrences
   pass at every block.
5. Both root orientations and every moving-root coefficient through the
   target are retained.
6. The positive coefficient is exact over `Q`; `F_65521` is only a second
   host/software control.
7. Deleting a row-connection term, the `C^2` primitive, or the `RA^2`
   control contribution must trip a sentinel.
8. AWS only, fresh tags, fail-closed validator, resource telemetry, and
   zero swap.

## Firewall

A PASS closes only the eleven named `a<=6` strict unique-`AC` baseline
tails after the registered upstream gates.  It does not decide `E`, any
`a=7,8,9` block, an equality face, a positive-order leading load, another
D1 face, `p=0`, `k0=0`, a terminal/global landing chart, the square
component, order two, `(8,12)`, maximum twelve, or JC2.
