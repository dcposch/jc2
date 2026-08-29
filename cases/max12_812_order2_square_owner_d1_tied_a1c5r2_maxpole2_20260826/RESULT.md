# Result: tied `(a,c,r)=(1,5,2)` maximal-pole face

Date: 2026-08-26

Status: **PRODUCER PASS ON EXACT `Q`, WITH TWO INDEPENDENT GOOD-PRIME
CONTROLS.  HOSTILE REVIEW REQUIRED BEFORE PROMOTION.**

## Narrow theorem

On the frozen generic square/D1 unit-load chart `D(p*k0)`, the exact contact
cell

```text
ord(A)=1, ord(C)=5, ord(R)=2
```

is empty.  This statement concerns only the grade-16 source obstruction on
that named chart.

## Complete grade-16 source

An independent enumeration of all four frozen binomial summands, using
cost-derived atom bounds and a padded-bound replay, found exactly four
primitive families through grade 16:

```text
(3/4) A*C/L,
(5/32) k0*A^2/L,
(5/16) k0*R^3/L,
-(3/8) R*A^2/L^2.
```

All four first occur in grade 16.  The last is the unique pole-two family;
the other three have pole one.  Because the ceiling equals the first grade,
the mechanical jet maxima are zero beyond the seven leading source
coefficients, and every target/load family other than the unit `k0` is
absent.  The complete seven literal rows, all recursive source quotients,
and the lower-unitriangular analytic/Faber bridge passed exactly.

## Iterated maximal-pole obstruction

Let `L=z^2+p/2`.  After clearing `L^2`, the full rational numerator is

```text
N2_full=(3/4)A*C*L+(5/32)k0*A^2*L
       +(5/16)k0*R^3*L-(3/8)R*A^2.                (1)
```

The Laurent/Faber receiver reconstructs the canonical remainder of (1)
modulo `L^2`; the discarded ordinary quotient was retained and its exact
division identity passed.  The pole-two recurrence and both root identities

```text
N2(+-lambda)=Phi4+-lambda*(Phi3+(p/4)Phi1),
lambda^2+p/2=0,
```

passed.  Modulo `L`, these are exactly

```text
-(3/8)R(+-lambda)A(+-lambda)^2.                   (2)
```

The four products obtained by choosing a nonzero root value of each nonzero
linear form `A,R` were compiled separately.  The two same-root charts are
unit ideals already from (2).  The two residual charts allocate `A` and `R`
to opposite roots.  For example,

```text
A=au*(z-lambda), R=bu*(z+lambda).
```

There `N2=L*Q1` exactly, and at the `A` root

```text
Q1(lambda)=(5/2)k0*lambda^3*bu^3.                (3)
```

The deck conjugate gives `-(5/2)k0*lambda^3*bu^3`.  Equivalently, the
derivative syzygies in the literal rows give the common unit multiple

```text
N2'(+-lambda)=5*k0*lambda^4*bu^3.                 (4)
```

The two opposite-root ideals containing the pole-two equations and the
appropriate derivative functional are unit ideals after inverting only
`lambda`, `k0`, and the named nonzero root value of `R`.  Thus the cover is
scheme-theoretically empty.  The determinant of the two-root evaluation map
is `2*lambda`, a unit in every registered characteristic, so the four charts
cover every nonzero linear `A,R` pair.  Faithfully flat descent from the
finite etale root cover gives the stated base-chart emptiness.

The omitted-`R3` negative control makes (3) zero.  Stopping after (2) leaves
the two opposite allocations and therefore does not yield a false endpoint.

## V1 quarantine and V2 repair

Triple-AWS V1 passed every substantive identity above but failed a sentinel
which demanded literal equality `N2=N2_full`.  The negative Laurent tail is
only the remainder modulo `L^2`; a separate exact-Q diagnostic certified both
the mod-`L^2` identity and the exact discarded quotient.  V1 is preserved as
no-verdict evidence.  V2 changes only that normalization sentinel and retains
the ordinary quotient explicitly.

## Exact producer custody

The V2 source archive SHA is

```text
4b903ffcb76b3d584f64105b821372d82580ad851415e1538d7dc84bd8a5367d.
```

The exact-Q and two good-prime runs all returned engine `rc=0`, validator
`PASS_D1_TIED_A1C5R2_MAXPOLE2_EMPTY`, and the identical structural stdout
SHA

```text
40614e986b5a5958069fb36992478ea717ae1220dbb7f44485072ed09421abbe.
```

Each used about 20 MiB maximum RSS and zero swap.  Full paths and hashes are
in `AWS_LAUNCH_METADATA.md` and `EVIDENCE.sha256`.

## Consequence for the hand triage

The prior hand triage left `(1,5,2)` open because it allowed `AC` to cancel
the post-allocation `R^3` pole.  The exact quotient shows these poles occur at
opposite roots: at the root where `A` vanishes, the `AC`, `A^2`, and divided
`RA^2` terms vanish, while `R^3` is the unit (3).  Any correction of that memo
must wait for hostile review of this producer.

## Firewall

This result does not cover another lower-hull face, a positive-order or
ramified load, `p=0`, `k0=0`, the exact-square zero section, terminal/Taylor
receivers, fan exhaustiveness, order two, `(8,12)`, maximum twelve, or JC2.
