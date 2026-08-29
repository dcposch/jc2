# TD6 V84R2 bounded quadratic pilot — first q-block vanishes

Status: **PRODUCER-EXACT / DUAL-AWS / HOSTILE REVIEW PENDING**.

This package is the smallest source-typed repair of the V84/V84R pilot.  It
tests only the ten unordered quadratic pairs in

```text
Sym^2 span(q2,q3,q4,q5)
```

on the fixed source-typed A3/F1 presentation over the symbolic center field,
through transport, FIRST, and previous/pole.  It does not test current or any
pair involving `q6,...,q24,d10,d15`.

## Exact endpoint

Both registered AWS runs used byte-identical source archive

```text
71934436bf932284f136d7742b398208504ef59bc07f29969bad91e6bf32abc3
```

and independently returned exit zero.  They agree on:

```text
transport_rank=3470/3602;free=132
first_rank=38/132;dependent=0
previous_pole_rank=38/94;dependent=1
quadratic_coordinate_count=0
quadratic_denominator_factor=(1, [])
```

The single previous/pole dependent row has zero coefficient for all ten
registered pairs.  Equivalently, the emitted exact table contains only its
header.  Its bytes agree on both hosts:

```text
b93bed47384146af9d18c44cc51897aa95455094fa55cec51470d2ea3cc737ab
  K2_BLOCK_0_0.exact.tsv
8041f53d2bb2b7e92f9e047d2ca6bad668bac36b5f2a1e0a146cec71be70af43
  K2_BLOCK_0_0.denominator.factor.txt
```

This is not an empty-serializer inference.  Before the expensive source
replay, the runner passes a registered nonzero-slot control, the diagonal
Taylor-coefficient control, the mixed-product control, and the inverse
second-term control.  It then replays all original source combinations and
checks the active q-boundary singleton and per-axis omission controls.

V84R's failed control is retained in `source/`: it incorrectly compared the
authoritative normalized typed `qd.source_rhs(key).value` with a legacy scalar
presentation outside the X boundary.  V84R2 uses the typed value and retains
the exact legacy equality only on X-boundary rows, where it is licensed.

## Custody

- r6d: tag `td6_v84r2_k2_r6d_block_0_0_20260826T0540Z`, PID `233537`,
  run `/home/ubuntu/runs/td6_v84r2_k2_pilot_r6d_20260826T0540Z`, finished
  `2026-08-26T06:03:08Z`, max RSS 431,068 KiB, zero swap.
- Box03: tag `td6_v84r2_k2_box03_block_0_0_20260826T0540Z`, PID `166617`,
  run `/home/ubuntu/runs/td6_v84r2_k2_pilot_box03_20260826T0540Z`, finished
  `2026-08-26T06:03:26Z`, max RSS 431,624 KiB, zero swap.

Raw streams differ only in registered host/tag and timing/custody text around
the common algebraic endpoint.  Their SHAs are:

```text
88470fa31351d82b047f00ed638981d2528878f8d7950148625056875b296b9a  r6d stdout
aa3da7c33d67b7b4c949b5d870e37b2cde10aacfcec740c5fa848c5b79e0fa1d  r6d stderr
c2367b092b951cf20e08b97cb15ede2c2535d82e7c4758cba6ebfa60af68db4c  Box03 stdout
caf52fe3ffb3957337f9dbaced407fa33ca87a75c102b081ecce56b89b949ef4  Box03 stderr
```

The stderr files contain only `/usr/bin/time -v` custody output and report
exit status zero.  The terminal PASS label inherits the shorter historical
string `...V84 PASS`; the producer banner, source archive, run tags, and
preregistration all identify V84R2.  This naming defect changes no source or
table byte and remains charged for hostile review.

## Firewall

The exact conclusion is only that the q2--q5 quadratic block has zero
previous/pole obstruction on the same generic symbolic-center presentation
and principal rank open used by its ancestors.  The raw rank-drop fibres,
including the V83 `R38=0` debt, remain outside this result.  A zero quadratic
block does not prove a nonlinear lift, formal integrability, a neighborhood,
a family, all of K2, current compatibility, TD6, SP-2, landing, or JC2.

