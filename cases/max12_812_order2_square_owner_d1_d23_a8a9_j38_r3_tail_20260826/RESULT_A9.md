# Producer result: D1 `a=9`, `d=2,3` grade-38 tails

Date: 2026-08-26

Status: **PRODUCER PASS IN EXACT `Q`; TWO INDEPENDENT GOOD-PRIME SOFTWARE
CONTROLS PASS.  A SEPARATE HOSTILE REVIEW IS REQUIRED BEFORE PROMOTION.**

## Exact result

After the frozen generic-square and D1 source gates, the complete seven
literal Faber equations generate the unit ideal on `D(J)` in each of the
two preregistered source cells

```text
ord(A)=9, ord(C)=11, ord(R)>=9;   (d=2)
ord(A)=9, ord(C)=12, ord(R)>=9.   (d=3)
```

Together with the registered `p,k0` units, the producer's exact open is
`D(p*k0*J)`.  It does not assert exact contact for `R`: the independent
homogeneous factor `eta` is never inverted, and `eta=sigma^s` covers every
closed tail `ord(R)>=9`.

For both cells an independent cost-bounded census finds exactly thirteen
primitive source families through grade 38, maximal pole order three, and
the first pole-four family only at grade 42 (`d=2`) or 43 (`d=3`).  It
mechanically derives every source/load/moving-`p`/target ceiling, verifies
that the maximal licensed jet of every source family enters at grade 38,
and bridges all seven literal rows coefficientwise to the independent
Laurent source modulo `sigma^39`.

The already reviewed universal pole-three identity gives

```text
Phi7+(p(sigma)/4)*Phi5+(3*p(sigma)^2/32)*Phi3
    +(5*p(sigma)^3/128)*Phi1 = -sigma^38*J/4 mod sigma^39.
```

Rows 1,3,5 have no target in the licensed window; row 7 contributes the
sole odd target `J/4`.  Dividing by `sigma^38` and adjoining `iJ*J-1`
produces `1` before radicals.  All row-2, row-4, and row-6 targets and all
licensed load jets remain in the complete seven-row bridge even though the
odd functional does not use those rows.

## Independent executions

| cell | exact-Q AWS endpoint | `F_65519` control | `F_65521` control | common engine output |
|---|---|---|---|---|
| `a9,d2` | Box02, rc 0, 21:34, 107,644,548 KiB, swap 0 | Box03, rc 0, 17:50, 98,951,104 KiB, swap 0 | r6d, rc 0, 17:22, 98,951,420 KiB, swap 0 | `386c1ace212de6764884f34bd699a0639bf430c5044d7493c34031fce0a55eb0` |
| `a9,d3` | Box02, rc 0, 14:04, 62,252,144 KiB, swap 0 | Box03, rc 0, 11:04, 56,589,900 KiB, swap 0 | r6d, rc 0, 10:36, 56,589,548 KiB, swap 0 | `8c2e9f50247bf33f4018a83807af8439ac21daf63411f189037dd90994e6b165` |

Exact `Q` is the characteristic-zero endpoint.  The primes are independent
software/host controls only.  All six validators returned their named PASS
endpoint, every engine returned rc 0, and every run recorded zero swap.
The generated Singular programs use ordinary polynomial rings plus
explicit truncation ideals and `reduce`; no Singular `qring` is present.

## Custody and firewall

The source archive presented independently on all hosts had SHA256

```text
01cca2d13adfd6685dd628b89f7eace7344b5c778b828d29563f8b8279040f53
```

and every host passed the frozen source manifest before compilation.
`EVIDENCE_A9.sha256`, `AWS_LAUNCH_METADATA_A9.md`, and
`PRODUCER_FREEZE_A9.sha256` pin the retrieved evidence and this result.

This producer says nothing about the neighboring `(a,d)=(8,3)` cell.  Its
unchanged complete V2 source is running separately at higher memory after
the original 128-GiB attempts ended with resource rc 14 and no mathematical
verdict.  This result also does not cover an equality face, another leading
face, positive-order leading load, `p=0`, `k0=0`, `J=0`, a terminal/global
chart, the whole square component, order two, `(8,12)`, maximum twelve, or
JC2.
