# Producer result: `r=1` and symbolic unique-`AC` `d=1` receivers

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER PASS; HOSTILE REVIEW REQUIRED BEFORE PROMOTION.**

## Endpoint

The frozen V12 package passed independently over exact Q and `F_65521`.
Both isolated `r=1` and D1 Singular processes returned `rc=0` on both hosts;
both fail-closed validators printed
`PASS_R1_D1_AC_SYMBOLIC_V12_RECURRENCE_PRODUCTS`.  No stdout contains a
Singular diagnostic or `=FAIL` marker.

The exact-Q compiled `r=1` / D1 input SHAs are
`e253681e155c0cbbc2c2984ecd6eeb7b5edfcb3e75b7b0c5649ec1051be7e5b3`
and
`9ea31841e78ffdf927509b4e15aa4505c7c31c0acfe39a32cb3f3040007f9845`.
The `F_65521` inputs are
`e388c06b366dbcf083529861ad94de0184105125c90d8e4a595eb75c9d184bc3`
and
`73fd282452e7f4a1b8bcb708b8678ed7d1729246a88ea0641f34473c124dced5`.
Marker-only `r=1` and D1 stdout SHAs are respectively
`8adb20f408c987d72d346224d92bfcbb2af441a2ee82107434d1caf3f0b1ef25`
and
`c56b388cfc8f3b4cee41c9976d55012662529b885693d9c1b83f7593db154044`
on both fields.

## Producer theorem 1: the normalized `r=1` receiver

On the reviewed generic-square first-normal chart `D(p*k0)`, after the
half-weight support gate, assume

```text
ord(A)>=1,   ord(C)>=3,   R=sigma*R0+... .
```

The complete seven source rows at absolute grade 13 are the exact
lower-unitriangular Faber image of the Laurent receiver

```text
(5/16)*k0*R0^3/L0,        L0=z^2+p/2.
```

Their vanishing forces the proper numerator remainder of `R0^3` modulo
`L0` to vanish.  The localized exact-Q radical on `D(p*k0)` is supported at
both coefficients of the linear polynomial `R0` equal to zero.  Hence no
finite-order arc in this normalized receiver has a nonzero leading `R0`.

## Producer theorem 2: the symbolic unique-`AC`, `d=1` subcone

On the same open, the symbolic substitution

```text
A=sigma^2*theta*(A0+sigma*A1),
C=sigma^3*theta*(C0+sigma*C1),
R=sigma^2*theta*eta*R0
```

with `theta=sigma^n`, `eta=sigma^s` covers exactly

```text
a=2+n,   c=a+1,   r=a+s,    n,s>=0.
```

All seven complete source rows at absolute grades 15 and 16 agree with the
analytic Laurent rows.  The certified symbolic decomposition retains the
three successor modules: `(n,s)=(0,0)` with `C2,RC,R3`, `n>=1,s=0` with
`C2,RC`, and `s>0` with `C2`, in every case including the moving-`L`
connection.

Over the etale splitting of `L0`, the first `AC/L` equation allocates `A0`
and `C0` to opposite roots.  Four explicit source-to-target ring maps check
both deck orientations.  At the allocated root the grade-16 proper numerator
has the unmatched value

```text
(3/2)*lambda^2*cv^2*theta^2,
```

nonzero on the registered chart.  Therefore the entire unique-`AC` subcone
`a>=2,c=a+1,r>=a` is empty, subject to the stated first-normal hypotheses.

## Software-control history

V1--V7 failed closed at the terminal root block after all source/row/scaling
sentinels passed.  V8 isolated `r=1` and D1 into separate processes; V9 used
direct substitutions; V10 introduced four ring maps and was mathematically
producer-positive; V11 changed the next print sentinel.  These controls show
that a Singular exponent diagnostic was delayed from the N16/recurrence
syntax rather than caused by the root evaluator.  V12 changes only one
`z^3`, one `z^2`, and three `p^2` spellings to equal explicit products.  The
diagnostic disappears and all maps/validators pass on both fields.  Earlier
versions remain immutable negative/presentation controls and supply no
theorem by themselves.

## Firewall

This is producer-tier arcwise/set-theoretic elimination only for the
normalized `r=1` receiver and the unique-`AC` subcone
`a>=2,c=a+1,r>=a` on `D(p*k0)`.  It awaits hostile review.  It does not
cover the `(1,3)` or `(1,4)` AC charts, other unique/tied AC or RC faces,
the RA2 exception, positive-order/ramified loads, `p=0`, `k0=0`,
zero/infinity sections, fan exhaustiveness, scheme structure, the whole
square branch, exact order two, maximum twelve, or JC2.  Exact Q carries the
characteristic-zero producer claim; `F_65521` is a software control.
