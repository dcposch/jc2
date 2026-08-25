# Hostile audit — B9 normalized common cubic at `3^11`

Date: 2026-08-25  
Auditor: Codex, independent AWS reconstruction  
Verdict: **V2 UNSAT INVALID; INTENDED FINITE GATE SAT**

## Bottom line

The V2 Boolector/Z3 agreement and one-clause CNF do not certify the claimed
common-cubic exclusion.  V2 emitted a different, trivially inconsistent
formula: the function that reduces residue literals modulo `177147` was also
used to emit the modulus itself.  It therefore wrote zero as every modular
divisor and wrote `h_i < 0` for each common-cubic coordinate bound.

More strongly, the intended fixed-parent finite gate is nonempty.  A new
integer staged/Kuranishi compiler that never reads the V2 or V3 SMT produced
a literal mod-`177147` point.  A second source-independent polynomial replay
confirmed the fixed B9 parent modulo 243, exact degree pair `(9,12)`, all 276
determinant positions, both leading units, and all 23 common-cubic top-form
positions.

Accordingly, V2 licenses no UNSAT or all-depth exclusion.  The corrected
finite statement is SAT.  This finite SAT point does not itself license an
all-depth lift.

## 1. Smallest decisive V2 defect

Charged source:

```text
cases/as_b9_9_12_common_cubic_3p11_20260825/emit_common_cubic.py
SHA-256 ab85df4824042f9919e535ad9b2d9c4213deb1aa2ed953ae6fa6aed4c66a7556
```

At lines 48--49 it defines

```python
def bv(value):
    return f"(_ bv{value % MODULUS} {WIDTH})"
```

Line 57 uses `bv(MODULUS)` as the `bvurem` divisor, and line 111 uses it as
the strict upper bound for `h1,h2,h3`.  Since
`MODULUS % MODULUS == 0`, the frozen emitted SMT

```text
SHA-256 182bc9f7302ba852b32d04899e6b7a86b38d0eaf0cb2faaa280717d4b9c70604
```

contains, beginning at line 586,

```smt2
(assert (bvult h1 (_ bv0 64)))
```

and identical impossible bounds for `h2,h3`.  Its alleged modular gates are
`bvurem(..., (_ bv0 64))`, not reduction modulo 177147.  Thus the instant
Boolector/Z3 verdict is forced by `h1 < 0` in unsigned bitvector order.

The frozen V2 bit-blast is literally

```text
p cnf 0 1
0
```

at SHA-256
`69ee12c3118a428a28f674ec24e362b721e0611c800f65afbcb8a48e778c1394`.
CaDiCaL/DRAT can perfectly certify that empty clause while saying nothing
about the intended arithmetic gate.  The quarantined V2 custody is correctly
separate at
`cases/as_b9_9_12_common_cubic_v2_zero_divisor_erratum_20260825/`.

## 2. Domains, support, and equation meaning

Apart from the V2 modulus literal, the charged inventory has the intended
shape:

- 55 coefficients for `P` on the complete total-degree-9 simplex;
- 91 coefficients for `Q` on the complete total-degree-12 simplex;
- 145 predecessor trits and 146 fresh trits inherited from the pinned
  complete determinant family;
- 276 determinant rows, one for every monomial of total degree `0..22`;
- three common-cubic coordinates; and
- 10+13 top-form equalities.

The intended domains are `s_i,w_i in {0,1,2}` and
`0 <= h_i < 177147`, `h_i = 0 mod 3`.  V2 encoded the trit domains correctly
but not the `h_i` upper bounds or any remainder by the target modulus.

The 23 top rows mean, coefficientwise modulo `3^11`,

```text
P9  = P_(0,9)  H^3,
Q12 = Q_(0,12) H^4,
H   = y^3 + h1*x*y^2 + h2*x^2*y + h3*x^3.
```

Two leading rows are tautological because the coefficient of `y^3` in `H`
is one; retaining all 23 is nevertheless a faithful full coefficient
inventory.  Requiring `P_(0,9)` and `Q_(0,12)` nonzero modulo three is the
correct leading-unit condition.

The monic normalization loses no charged common cubic.  Reduction of the
fixed parent has top forms `-y^9,y^12`, so any shared homogeneous cubic
reduces to a unit multiple of `y^3`.  Dividing the cubic by that unit makes it
monic and absorbs its third and fourth powers into the two leading scalars;
no extraction of a root is required.  The other three normalized
coefficients are then divisible by three.

## 3. Independent complete reconstruction

Custody source:

```text
cases/as_b9_9_12_common_cubic_hostile_audit_20260825/independent_common_core.py
SHA-256 460199584e128bc2c5f3196871a34437ebdfd7d674ccf0bcc2f52b9db8ace6b8
```

This compiler does not parse or read either producer SMT.  It consumes the
pinned linear-window parent source at SHA-256
`fb4f16d808dfba754582fb1b5fe10dfa0e69bca0888b38f92586e1f5534724e2`
and starts directly from the displayed B9 pair modulo 243.  At every digit it
introduces all 146 map-coefficient coordinates and all three `H` coordinates.
It forms 299 exact integer rows: 276 determinant rows plus all 23 top rows.
This bypasses the emitter's 145-coordinate serialization, so a missing or
misread predecessor coordinate cannot explain the SAT result.

The complete linear stages gave the following finite digit-coordinate
dimensions:

| modulus | dimension |
|---|---:|
| `3^6` | 55 |
| `3^7` | 81 |
| `3^8` | 99 |
| `3^9` | 116 |
| `3^10` | 133 |

Every base and basis direction was replayed with exact integer rows at its
stated modulus.  At `3^10 -> 3^11`, the independently compiled first
quadratic gate had:

- 17 predecessor coordinates visible quadratically;
- 116 three-divisible linear spectators;
- fresh rank/kernel/cokernel `94/55/205`;
- spectator rank 38 in the fresh cokernel; and
- **zero residual equations** after exact coefficient-image containment.

The result JSON is SHA-256
`fad73f36b609363f0ee8cde84f9ffd89233913ec9e036b00441ee11de5e8307f`.
The emitted empty residual ANF is SHA-256
`2a65d00367451476f31941426f086de0fef53bc0b73478e4eb9fa87fb2cf913e`.
The ranks imply a Kuranishi coordinate exponent
`17 + (116-38) + 55 = 150`; the load-bearing conclusion here is the literal
point below, not a promoted scheme-dimension claim.

## 4. Literal SAT witness and separate replay

The witness payload is

```text
cases/as_b9_9_12_common_cubic_hostile_audit_20260825/evidence/box02/independent_witness.json
SHA-256 a39bc9185a21df92173b356c027a00650ced4b92cfc15d587a91b39c8aca299a
```

Its normalized cubic is

```text
H = y^3 + 119880*x*y^2 + 40581*x^2*y  (mod 177147).
```

Both nonleading coefficients are divisible by three.  The witness has
`P_(0,9)=2 mod 3`, `Q_(0,12)=1 mod 3` and exact total degrees `(9,12)`.

The separate verifier

```text
cases/as_b9_9_12_common_cubic_hostile_audit_20260825/independent_witness_verify.py
SHA-256 eba7d223b88fd61da246fd766a3c5f4f73163e9b0261263d64406779671d6689
```

reads only the pinned witness.  It uses its own polynomial arithmetic and a
hardcoded copy of the displayed integer B9 parent.  It confirmed:

- exact reduction to that parent modulo 243;
- no coefficient outside `P<=9,Q<=12`;
- exact total degrees `(9,12)`;
- `det J(P,Q)=1 mod 177147` (142 nonzero integer determinant positions before
  reduction);
- both leading units; and
- all 23 normalized top-form rows.

Verifier result SHA-256:
`2008726f5791b86b3c4f6e5b296cbbf4cdfa91766290c1d32aeec81e4a52c67a`.

## 5. Corrected-emission diagnostic

For diagnosis only, changing the two uses of the target modulus to the raw
64-bit literal produces canonical SMT SHA-256
`5af9efbe4b138f1cb0408099c90283842b4ef0b0fef9d7d33447d51a29d53563`
and Boolector-form SHA-256
`2eb69355a0b85b6928899a619840ecb7856ee6e6cc2ef050ab76067e44c835f7`.
Those files now contain the positive divisor and bounds
`(_ bv177147 64)`.  Generic solver runs on them were stopped once the literal
independent witness made them unnecessary; no interrupted solver output is
evidence for this verdict.

## 6. Exact scope and refusals

What is established is finite and narrow: the normalized determinant-one
common-cubic incidence modulo `3^11` is nonempty inside the complete
`P<=9,Q<=12` coefficient box over one displayed B9 mod-243 parent.

This audit does **not** establish:

- an all-depth compatible chain or inverse-limit point;
- survival to `3^12`;
- coverage of every earlier mod-243 parent;
- uniqueness or a scheme dimension for the common-cubic incidence;
- algebraization or a characteristic-zero Keller map;
- a polynomial counterexample, maximum-twelve theorem, TD6 landing, or JC2.

Conversely, the claimed V2 UNSAT cannot exclude any all-depth lift, because
its formula is invalid and the intended finite gate is in fact SAT.  Any
all-depth conclusion needs a genuine successor or recurrence theorem beyond
this one finite parent.

## 7. Custody

All substantive work ran on AWS Box02 in
`/home/ubuntu/jobs/as_b9_common_cubic_hostile_audit_20260825T1725Z`.
The independent reconstruction used 28,920 KiB maximum RSS and completed in
4.96 seconds; the separate replay used 14,592 KiB and completed in 0.03
seconds.  The frozen local case contains the full audit sources, corrected
diagnostic formula, parent replays, ranks/ANF, literal witness, independent
replay, timing logs, source closure, manifest, and freeze pins.
