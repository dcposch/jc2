# V43G5 generic-certificate circuit and pole minimizer

Date: 2026-08-27  
Status: **PREREGISTERED; exact AWS-only descendant of frozen V43G3/V43G4.**

## Frozen question

Let `R` be the eleven literal dehomogenized total rows supporting the V43G4
identity, in `Q[t,X]`, `t=rho^2`:

```text
Tg11_2 Tg11_7 Tg12_2 Tg12_7 Tg13_5 Tg13_7
Tg14_5 Tg14_7 Tg15_3 Tg15_5 Tg15_7.
```

1. Exhaustively test all `2^11` subsets over `Q(t)` and report every
   inclusion-minimal unit support.  Unitness is exact complete-basis
   `std`/`reduce(1,G)` semantics; finite-prime or specialized fibres are not
   verdicts.
2. Over the polynomial ring `Q[t,X]`, find the least `0<=s<=6` such that
   `t^s` lies in the full eleven-row ideal.  V43G4 is the positive control at
   `s=6`; absence through 6 is a fail-closed contradiction.
3. For every inclusion-minimal `Q(t)`-unit support, find its least pole
   `0<=s<=6` when one exists, use `liftstd` to serialize every individual
   multiplier, and replay the exact product against the original selected
   row entries.  A minimal support need not share the full ideal's minimum
   pole; report both quantities separately.
4. Mutate one literal row coefficient and require the chosen certificate
   replay to fail.  Do not mutate only the target or a status token.

The compiler must pin the immutable V43G3 and V43G4 freezes, the exact G3
58-row script and row-name map, and the V43G4 eleven-row support.  It may
remove variables absent from all eleven rows, but it must prove byte equality
of each selected row expression before doing so.  All heavy Gröbner/lift work
runs on AWS, with at most two one-core processes, a 128-GiB cap per process,
and a six-hour wall cap.

## Outcome semantics

- An exhaustive unit table determines the inclusion-minimal unit circuits
  inside this fixed eleven-row set.
- The full-support polynomial scan determines the actual minimum `t` pole
  within this eleven-row ideal, not globally over all 59 rows.
- These are certificate-compression theorems only.  They do not replace the
  explicit special-fibre input when the minimum pole is positive and do not
  enlarge V43G4's ordered-chart scope.
