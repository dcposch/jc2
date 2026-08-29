# `(8,12)` order-two square fan: three smallest `AC` face discriminators

Date: 2026-08-26

Status: **CORRECTED HAND ROOT-RESIDUE DISCRIMINATOR.  THE WHOLE `c=a+1`
UNIQUE-`AC` SUBCONE HAS A CONDITIONAL DOUBLE-POLE ELIMINATION; THE OTHER TWO
SMALLEST CHARTS DO NOT.  NO BRANCH VERDICT.**

## Setup

Work on the generic unit-load square chart `D(p*k0)`.  After the reviewed
vertical gates and contact raise, let

```text
a=ord(A)>=1,  c=ord(C)>=3,  r=ord(R)>=2.
```

The lower-hull weights and pole types are those in the frozen horizontal
design and the companion lower-hull reduction.  The first three new
root-allocation tests are

```text
(a,c)=(1,3), (1,4), (2,3).
```

In each case `AC/L` is the unique first negative-tail term.  Over the etale
root algebra write `L=u*v`.  Its vanishing with nonzero linear `A,C` forces,
up to the deck swap,

```text
A=A_u*u,  C=C_v*v,  A_u*C_v!=0.                    (1)
```

The following argument concerns the first subsequent pole grade.  It assumes
the complete-source replay confirms that the listed nonzero scalar
coefficients and absolute timings are unchanged by the retained correction
terms.  A crucial correction is that the `j`-th connection term obtained by
moving `L` in the already polynomial quotient `AC/L` can have pole order
`j`.  It is therefore safe to compare a double pole with connection terms
only when that double pole arrives one grade after the first `AC` face.

## `(a,c)=(1,3)`: no hand endpoint

The first face has relative weight four.  At relative weight six, `C2` and
`A2` occur; when `r=2`, `RA2,R3,RC` join the same grade.  Although

```text
C^2/L^2 = C_v^2/u^2.
```

has a double pole at `u=0`, it arrives **two** grades after the first `AC`
term.  Second-order motion of `L`, together with second corrections to
`A,C`, can also contribute an `L^-2` principal part at that grade.  The
intermediate grade can constrain those corrections without forcing them all
to vanish.  Consequently pole order alone does not eliminate this face; the
full grades-five-and-six source client is required.

## The `c=a+1` unique-`AC` subcone

The integer points of this subcone are

```text
a>=2,  c=a+1,  r>=a.
```

The inequalities in the companion lower-hull lemma show that `AC` is unique
there.  Its weight is `2a+1`, while `C2` has weight `2a+2`, exactly one grade
later.  The term `RC` joins that grade only when `r=a`; `R3` also joins only
at the smallest point `(a,c,r)=(2,3,2)`.  Every other registered lower-hull
term is later.  The display

```text
C^2/L^2=C_v^2/u^2
```

has an unmatched double pole at `u=0`, while `R3,RC` and every first
connection correction to `AC/L` have at most simple poles.  Subject to the
complete-source timing, nonzero-coefficient replay, and a symbolic translation
identity in `a`, this entire oriented subcone and its deck conjugate are
empty.  Sampling finitely many values of `a,r` is not a substitute for that
translation identity.

## `(a,c)=(1,4)`: no hand endpoint

The first face has relative weight five.  If `r>2`, the next nominal term is
the unique `A2=A^2/L=u/v`.  Its pole is only simple, so a first connection
correction to `AC/L` can cancel it.  No hand elimination follows.

If `r=2`, the relative-weight-six face is exactly

```text
RA2, R3, A2.
```

Without corrections, a two-root argument would first constrain `R` and then
expose the double pole

```text
RA2=R*A^2/L^2=R/v^2
```

at the opposite root.  However, first connection corrections can cancel the
simple `R3/A2` equations and invalidate the intermediate conclusion about
`R`.  The complete correction-aware grade-six source client is required.

## Exact client acceptance test

The `c=a+1` source client need not compute a radical.  For each orientation it
should:

1. reproduce the complete source-to-Faber rows through the first subsequent
   pole grade, retaining moving `p,k0` and all corrections that can arrive by
   that grade;
2. verify the first `AC/L` numerator is polynomial exactly when the two
   leading linear factors occupy opposite roots;
3. extract the order-two local principal part at the nominated root and
   verify its coefficient is the stated nonzero scalar times `C_v^2`;
4. verify every competing same-grade term and every connection correction
   has pole order at most one there;
5. prove that increasing `a,c` together, and increasing `r` within the cone,
   changes only the common extracted power and cannot introduce a same-grade
   order-two pole;
6. repeat after the deck swap and on exact `Q`, with one good-prime software
   control.

For `(1,3)` the client must include both intervening grades and second
connection corrections.  For `(1,4)` it must retain all first connection
corrections in the same-grade simple-pole system.  Neither may be replaced by
the pole-order shortcut above.

## Scope firewall

The corrected hand argument conditionally eliminates only the `c=a+1`
unique-`AC` subcone.  It leaves `(1,3)` and `(1,4)` as exact source clients
and does not cover
the rest of the `AC` cell,
unique or tied `RC` faces, the `RA2=A2=R3` boundary outside the displayed
orientation analysis, positive-order or ramified loads, `p=0`, the
exact-square zero section, terminal/Taylor conditions, fan exhaustiveness,
order two, maximum twelve, or JC2.
