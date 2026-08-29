# HENS-CT rank-one control R0 — preregistration

Frozen UTC date: 2026-08-28

## Scope and exact input

This lane is a proof-of-method computation for the reviewed rank-one control

```text
H=X^4, p=X,
F(X,t)=X^8+(X^7+X^4+1)t,
t=sP,
P^8=X^8+s(X^7+X^4+1)P,
Q=P^2.
```

Equivalently, on the Hensel branch `y(0)=1`,

```text
h=1+X^-3+X^-7,
y^8=1+s h y,
Q=X^2 y^2.
```

The charged algebraic field is

```text
E=Q(s,X)[y]/(y^8-1-s h y).
```

The computation must produce a nonzero operator `L` in `Q(s)<Ds>` and a
certificate operator `C` such that, acting on `Q=X^2 y^2`,

```text
L(Q) = d_X(C(Q))                                      (CT)
```

holds identically in `E`.  Printing only the reviewed scalar residue
recurrence is failure.  A coefficientwise formal Laurent primitive is not an
algebraic certificate and is failure.

## Frozen tool route

Use `ore_algebra` commit

```text
18680180c884fac869a064db99f29a221aad9dfe
```

through its algebraic-composition annihilator and `Ideal.ct(DX,
certificates=True)`.  The independent replay does not trust a package banner:
it explicitly differentiates the returned `B=C(Q)` in `E` and tests (CT).

### Frozen installation amendment after the first exact failure

The unmodified pinned source fails while compiling the optional analytic
extension `analytic/dac_sum_c.c` against the PassageMath/FLINT headers on
`r6c` (`unknown type name 'slong'`).  This happened before any annihilator or
CT computation.  One and only one installation retry is authorized from the
same commit, with the checked-in patch `ore_disable_analytic_extensions.patch`.
It replaces the computed `ext_modules` list by `[]`; it does not alter
`ideal.py`, Ore arithmetic, algebraic composition, or creative telescoping.
The patched `setup.py`, commit, and patch hashes must be captured.  Failure of
the patched pure-Python install or of the algebraic composition/CT API closes
this lane as `FAIL_*`; no further dependency chase is authorized.

The patched install succeeded, but the first emitter invocation stopped at
import because modular PassageMath intentionally provides distribution
aggregators such as `sage.all__sagemath_symbolics`, not monolithic `sage.all`.
A fresh-process smoke test established that importing `ZZ` and
`PolynomialRing` from `sage.all__sagemath_symbolics` initializes the installed
stack and then imports `OreAlgebra`.  One source-only retry from a fresh job
namespace may reuse that frozen venv after checking its commit and patched
`setup.py` hashes.  This changes no tool package and is not a dependency retry.
Any later field/composition/CT exception closes the tool route.

## Host, ownership, and caps

- Authorized host: AWS `r6c`, instance `i-040b7a1c2ed72d4cc` only.
- Ownership audit at `2026-08-28T00:41:24Z`: idle, 527231848448 bytes
  available, zero swap; transferred by the upper-endpoint monitor for this
  one lane.
- Recheck Linux, Amazon EC2 DMI, no competing heavy user process, available
  memory at least 450 GiB, and zero swap immediately before launch.
- Fresh namespace: `/home/ubuntu/jobs/ggv_hens_ct_rank_one_r0_20260828T*/`.
- Tool installation cap: 1800 seconds.
- Algebraic annihilator plus CT cap: 14400 seconds.
- Address-space cap: 400 GiB (`ulimit -v 419430400`).
- One CT process; no local CAS and no use of `r6d`.

## Success, failure, and terminal evidence

`PASS` requires all of:

1. the exact modulus and branch seed are printed;
2. a nonzero `L` and nonzero certificate operator `C` are serialized;
3. Ore-ideal membership `(L-DX*C) mod J = 0` is exact;
4. `B=C(X^2 y^2)` is serialized as an element of `E`;
5. direct algebraic replay gives `L(Q)-d_X B=0`;
6. every monomial of `L` preserves one residue class modulo four, so it can
   be sectioned, or the run explicitly returns `FAIL_NONSECTIONABLE`;
7. source hash, tool commit/version, host, timestamps, rc, wall time, and peak
   RSS are captured.

Terminal markers are exactly one of `PASS`, `FAIL_*`, `TIMEOUT`, or
`RESOURCE_STOP`.  Timeout, OOM, install failure, iteration-limit exhaustion,
an empty/zero certificate, or a replay mismatch is no mathematical verdict.

## Required mutations and desk controls

The lightweight replay must reject:

1. omitted `+22` in the fixed-receiver normalization while retaining the
   actual row receiver;
2. the literal/double `H^k` weighting in place of the R8 fixed gauge;
3. the wrong fourth-root projector phase;
4. the false assertion that the `b=0` section is even (the true free parity
   invariant is for `b=2`).

It must also print the correct receiver `V_(b+22)`, the basis
`X^(-(b+23))dX`, and all three index conventions: section index `k`, physical
coefficient `n=b+4k`, and row `m=n+22`.

## Scope firewall

Success proves only that the R8 algebraic creative-telescoping method can be
instantiated on this fixed rank-one control.  This point already fails row
23.  It says nothing about branch P/Q, a survivor cell, polynomial `G`, raw
determinants, an endpoint fibre, a GGV family, landing, or JC2.
