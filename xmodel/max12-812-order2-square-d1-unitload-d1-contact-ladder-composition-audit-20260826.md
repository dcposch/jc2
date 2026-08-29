# Audit: unit-load D1 unique-`AC`, `d=1` contact ladder

Date: 2026-08-26

Status: **LITERAL COVERAGE AUDIT PASSES FOR THE NORMALIZED INTEGRAL
`d=1` CELL; FINAL COMPOSITION AWAITS THE `a>=10` HOSTILE REVIEW.**

This is not a whole-D1 theorem and not a promotion. It audits whether the
reviewed fixed bands plus the new producer have a genuine routing gap.

## 1. Exact fan cell

On the generic unit-load horizontal chart, write

```text
q=ord(k10)=0,  a=ord(A)>=1,  r=ord(R)>=2,  c=ord(C)>=3.
```

The five lower-hull weights are

```text
AC=a+c,  C2=2c,  R3=3r,  RC=1+r+c,  A2=4+2a.
```

At an integral point where `AC` is uniquely minimal, put
`d=c-a` and `s=r-a`. Strict comparison gives

```text
1<=d<=3,  s>=0,  a+3s>d.
```

For `d=1`, the last inequality is automatic exactly when `a>=2`. Hence the
entire normalized integral cell audited here is

```text
a>=2,  c=a+1,  r=a+s with s>=0.                    (D1-AC1)
```

There is no missing `c` or `r` boundary inside (D1-AC1): `r=a` is included,
and every `r>a` is the closed leading-section face in the fixed-band clients
or the homogeneous `eta=sigma^s` substitution in the tail. The exceptional
`RA2` lower-hull locus `(a,r)=(1,2),c>=5` is disjoint from (D1-AC1).

All orders in this audit are ordinary `ord_sigma` values of a normalized
DVR arc and hence integral. This file does not enlarge the fixed `a=2..9`
theorems to a separately normalized rational-weight convention.

## 2. Contact partition and custody

The integer interval is partitioned without overlap gaps as follows.

| contact | exact reviewed/producer scope | custody |
|---|---|---|
| `a=2,3,4,5` | fixed `c=a+1,r>=a` on `D(p*k10)` | RESULT `17c3baa2...`; hostile review `e03de4e1...`, **CONFIRMED** |
| `a=6,7` | fixed `c=a+1,r>=a` on `D(p*k10)` | RESULT `f3c987b6...`; hostile review `3e601cf3...`, **CONFIRMED** |
| `a=8` | fixed `c=9,r>=8` on `D(p*k10)` | promotion `3d847561...`; review `b5944e15...`, **CONFIRMED** |
| `a=9` | fixed `c=10,r>=9` on `D(p*k0)` | promotion `dfabe082...`; review `8524bd1e...`, **CONFIRMED** |
| `a>=10` | uniform `c=a+1,r>=a` on `D(J)` | producer RESULT `2ccfdfe9...`; producer freeze `60b2e1d5...`; hostile review live |
| `a>=13` | overlapping order-two functional control | promotion `29e2ac11...`; review `7a067603...`, **CONFIRMED** |

Here `k10` denotes the leading source load and `k0` its leading jet; on the
unit-load chart the two notations describe the same open `D(k0)`. The Keller
campaign works on `D(J)`. Therefore the new `a>=10` statement restricts to
the same `D(p*k0)` chart and fills precisely the old `a=10,11,12` hole. The
`a>=13` theorem is overlap, not an additional routing assumption.

The `a=2..5` and `a=6,7` packages have different-model CONFIRMED reviews,
but no separate `xmodel/*promotion*` artifacts were found in this audit.
That is a lifecycle/ledger action for the coordinator; it is not a
mathematical interval gap.

## 3. Exhaustive load-jet timing

There is no silent split of the lower load `k6` across the interval.

- `a=2..5`: `k6` and all targets occur after the decisive two-grade window;
  the hostile review independently checks that support inequality.
- `a=6`: `k60*C/L` first joins the second grade and is retained with arbitrary
  `k60`; no inversion or section split is used.
- `a=7`: `k60*C/L` joins the first grade and its `k61`/moving-connection
  correction joins the second; both are retained, including `k60=0`.
- `a=8`: the exhaustive split is `D(k60) union V(k60)`. On `V(k60)`,
  `k61,k62` are free and may both vanish; no higher `k6` jet can enter the
  grade-27/28 window.
- `a=9`: the exhaustive scheme-theoretic split is
  `D(k60) union (V(k60) intersect D(k60_1)) union V(k60,k60_1)`.
  Positive-valuation intermediate DVR sections specialize into the already
  empty open pieces. Higher `k6`, delayed `k2/k10_1`, moving connection, and
  terminal targets are retained through grade 30.
- `a>=10`: no load coefficient is inverted. The complete grade-38 inventory
  contains all jets through `k10_6,k6_10,k2_6`; its order-three row identity
  is independent of their values.

Thus there is no remaining `k6`-valuation or delayed-load section inside
(D1-AC1). The positive-order leading-load case `ord(k10)>0` is a different
fan and remains outside.

## 4. `R` and exact-contact faces

For `a=2..8`, the fixed clients put the grade-`a` section of `R` in a free
coefficient `eta`. The face `eta=0` represents every `r>a` because the next
`R` jet occurs after the decisive window; each hostile review checks this
timing explicitly. The `a=9` theorem is stated for all `r>=9`. For `a>=10`,
`eta=sigma^s` is a polynomial homogeneous shift, with no `eta` inversion,
and raising `r` delays every inventoried family. Exact orders of `A,C` are
enforced in the finite bands; the tail theorem is stronger and includes
their closed leading-coefficient faces.

## 5. Narrow composition verdict

Subject to confirmation of the frozen `a>=10` producer, the cited results
literally exhaust every normalized integral contact in (D1-AC1) on
`D(p*k0*J)` after the common first-normal, half-weight, and `M=0` upstream
gates. Since Keller has `J!=0`, this is normally named the `D(p*k0)`
unit-load unique-`AC`, `d=1` cone.

No theorem should be phrased as “D1 is closed.” The composition closes one
fan cell only.

## 6. Residual D1 cells not covered by this composition

At minimum, the following remain outside the ladder and require their own
promoted compositions, even where partial or local results already exist:

1. the other unique-`AC` families from the exact fan:
   `d=2` with `s=0,1,>=2`, and `d=3` with `s=0,>=1`, plus their small-`a`
   equality boundaries;
2. the primary `C2`, `R3`, `RC`, and `A2` lower faces and all their equality
   intersections, including the exceptional `RA2=A2=R3` locus
   `(a,r)=(1,2),c>=5`;
3. the separate `a=1` / `(1,3)` and `(1,4)` `AC` charts. The normalized
   `r=1` receiver itself has a distinct CONFIRMED V15 result, but that does
   not remove these other faces;
4. positive-order leading load `ord(k10)>0`, where `A3` can enter and the
   unit-load five-weight fan is invalid;
5. `p=0`, `k0=0`, the exact-square zero section, zero/infinity receivers,
   terminal/Taylor landing, and other lifecycle charts;
6. global source landing/coverage needed to transport every hypothetical
   counterexample into this local fan.

Beyond D1, the whole square component, nonsquare/Pell receiver, exact order
two, `(8,12)`, maximum twelve, and JC2 remain separate campaign obligations.
