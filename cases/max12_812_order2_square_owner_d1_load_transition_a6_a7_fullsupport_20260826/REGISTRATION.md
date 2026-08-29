# Registration: D1 first lower-load transition `a=6,7`

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS PRODUCER; NO ENDPOINT YET.**

## Objective

Source-type the first two generic-square D1 contacts at which the `k6`
lower load enters the decisive two-grade window.  On `D(p*k10)` set

```text
ord(A)=a,  ord(C)=a+1,  ord(R)>=a,  a in {6,7},
k6=k60+sigma*k61+... .
```

The exact expected proper parts are:

```text
a=6, grades 23,24:
  U0 ; U1 + KRC + S0

a=7, grades 25,26:
  U0 + S0 ; U1 + KRC + S1,
```

where

```text
U0  = [(3/4) A0*C0/L]_-,
U1  = [(3/4)((A1*C0+A0*C1)/L-ell1*A0*C0/L^2)
       +(3/8)C0^2/L^2]_-,
KRC = [(5/8)k10*R0*C0/L]_-,
S0  = [(3/4)k60*C0/L]_-,
S1  = [(3/4)((k61*C0+k60*C1)/L-ell1*k60*C0/L^2)]_-.
```

For `a=6`, the leading allocation remains `A0*C0`; `S0` is only a simple
pole at the next grade.  For `a=7`, the leading numerator is
`C0*(A0+k60)`, so the two root allocations use the shifted factor
`A0+k60`.  At the allocated shifted-A root, the two moving-L connection
terms `-ell1*A0*C0` and `-ell1*k60*C0` must cancel exactly, leaving the same
nonzero `C0^2` residue.

## Acceptance contract

Compile all seven frozen Faber tails with all three load summands and all
four targets.  Check exact quotient extraction and the moving `T0+T1` row
transform at both grades.  Require the exact `L` and `L^2` recurrences and
both root orientations.  Include fail-closed negative controls showing:

- deleting `k6*C` changes the source rows at `a=6` grade 24 and `a=7`
  grade 25;
- the first moving row-basis connection is generically nonzero;
- the `k10*RC` module is present when the grade-a `R` section is nonzero.

Run exact Q and `F_65521` independently on Box03/r6d, with 24-GiB virtual
memory, 600-second compile, and 1800-second engine caps.  Timeout, nonzero
return, missing/duplicate marker, `=FAIL`, `// **`, leading `?`, or
`error occurred` is no verdict.

## Firewall

This is only the fixed `a=6,7` transition on `D(p*k10)` after the reviewed
first-normal/half-weight/M=0 gates.  It does not cover `a>=8`, any other
face, p=0/k10=0, positive-order k10, zero/infinity sections, scheme
structure, the whole square branch, order two, `(8,12)`, maximum twelve, or
JC2.  It proves no blanket all-load square forcing: combined-load
Chebyshev/Pell solutions are expected controls for later strata.

