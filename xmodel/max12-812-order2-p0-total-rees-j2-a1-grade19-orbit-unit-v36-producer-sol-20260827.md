# Producer report: the V34 degree-five orbit dies at grade 19

Date: 2026-08-27 06:00Z  
Author: Sol (coordinator)  
Status: **PROVISIONAL PASS; independent hostile review live**

## Narrow claim

Inside the V32 six-coordinate ordered-`a1`, `rho=0` support, the normalized
degree-five scheme surviving all rows through grade 18 has no grade-19
prolongation.  This is not a closure of the ordered `T-a1` chart: other
supports/components remain open.

## Grade-18 scheme

V34 adjoins the only nonzero restricted grade-18 row to the V32 grade-17
ideal.  Exact Q and F65521 Singular runs both return a proper
zero-dimensional scheme of vector-space dimension five.  The Q standard
basis is

```text
600*cs1-11*ec3,
192*ell2-7*ee1,
ec3^2+3750*aa0,
ee1*ec3-21600,
7*aa0*ec3-2880*rs2,
24*rs2*ec3+875*ee1,
35*ee1^2+20736*rs2,
25*aa0*ee1+144*ec3,
2*rs2*ee1-105*aa0,
aa0^2-4*ee1,
rs2*aa0-210,
96*rs2^2-49*ec3.
```

Putting `t=ec3` gives

```text
t^5=1215000000000,
cs1=11*t/600,
ee1=21600/t,
ell2=1575/(2*t),
aa0=-t^2/3750,
rs2=-7*t^3/10800000,
a1=48.
```

The constant is `2^9*3^5*5^10`; in characteristic zero this scheme is
reduced because `t` is nonzero and the derivative is `5*t^4`.  With sigma
weights `(a1,ell2,cs1,rs2,aa0,ee1,ec3)=(5,2,3,4,6,7,8)`, scaling by
`lambda=t^3/13500000` has `lambda^5=4` and sends every geometric point to
the same rational representative

```text
a1=192, ell2=21/4, cs1=11, rs2=-35,
aa0=-96, ee1=576, ec3=2400.
```

V34 result/evidence SHAs are Q `7796c99a...` / `d175a8b2...` and F65521
`f293aaa2...` / `cf2589b5...`.

## Literal grade-19 reconstruction

V35 reconstructs the actual-total source through grade 19 with the exact
endpoint depths `ell19`, `cs17/rs17`, `az14/ac14/ez14/ec14`, `k10_15`, and
`k6_7`.  It byte-bridges the 42 V23 rows and seven rows at each of grades
16, 17, and 18, for 63 old rows total.  At the rational representative it
finds

```text
Tg19_1=...=Tg19_6=0,
Tg19_7=-7077888,
```

and the modular shadow is `63901 mod 65521`.  Both 18-file evidence
manifests replay locally.  V35 result/evidence SHAs are Q `bec0cf93...` /
`e4d45324...` and F65521 `56fc7b0b...` / `720f7e58...`.

V35 is discovery evidence, not the promotion boundary.  Its F65521 path
shares the rational reconstruction and reduces it modulo the prime, and its
validator does not independently derive every outcome field.  V36 was
created specifically to remove reliance on those weak points.

## Scheme-theoretic grade-19 obstruction

V36 freezes and parses all seven Q and F65521 V35 rows.  It verifies exact
Q-to-F65521 coefficient shadow, sigma weight 19 term-by-term, and the
absence of every sigma-weight-19 variable in every row.  Because sigma
weight need not equal first-occurrence grade, a follow-up exact census also
checks the honest newcomers: nine occur in rows 1--3 (`ell8,cs7,rs7,k10_6,
ac8,az8,ez8,k6_1,ec9`), while rows 4--7 have none.  In particular the sole
obstructing row `Tg19_7` is jet-free, so no new grade-19 coordinate can
cancel it.  The terminology correction is recorded in
`FIRST_OCCURRENCE_AMENDMENT.md`.

It then substitutes `a1=48`, restricts `Tg19_7` to the six V34 coordinates,
and sends the independently serialized Q and F65521 rows and corresponding
V34 bases to ordinary Singular.  Both runs return a nonzero normal form and
the unit ideal after adjoining the row.  Over Q the exact normal form is

```text
(110592/35)*rs2.
```

The V34 basis already contains `rs2*aa0-210`.  Hence `rs2` is a unit on the
V34 scheme; the displayed normal form is a unit in characteristic zero.
Equivalently, adjoining `Tg19_7` gives standard basis `1`.  The F65521
normal form is `18136*rs2`, also a unit, and its final basis is likewise
`1`.

The V36 Q result/evidence/normal-form SHAs are `d332ee24...` /
`d6efd436...` / `543d2b81...`; the F65521 SHAs are `06aa3a1a...` /
`882b7efe...` / `3e752b3a...`.  Both evidence manifests replay 17/17 with
zero mismatches.  Q and F65521 compiler-result SHAs are `b7e8d549...` and
`2cf20054...`.

## Scope and next action

The V32/V34 sparse orbit is eliminated, not the full ordered `T-a1` chart.
The next discriminating work must enlarge support or obtain a chart-wide
terminal/radical certificate; merely prolonging this six-coordinate orbit
is now forbidden.  Independent Fable5 hostile review is running in the
background, and Opus5 is independently attacking the terminal receiver and
support-enlargement design.
