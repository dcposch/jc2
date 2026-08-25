# Erratum and replacement: max12 `(9,12)` parity-normal boundary is `Q8`, not `Q12`

Date: 2026-08-24  
Status: **producer-exact erratum/replacement; hostile review required**

## 1. Rollback and immutable quarantine

The frozen `Q12` checkpoint is refuted.  Its replay substituted

```text
x1_wrong=x5*p^2*(v+1)+x5^2*(1/3)/(9v),                (1.1)
```

where the genuine reviewed parity chart requires

```text
x1=x5*p^2*(v+1)+x5^2*(1+3v)/(9v).                    (1.2)
```

Equation (1.1) does not satisfy `r2=r4=0`.  It nevertheless reproduces the
old `Q12` determinant identity, which explains why the internally consistent
replay passed.

The following are now quarantined and must not be consumed:

- `xmodel/max12-912-order3-nu-parity-normal-q12-20260824.md`;
- its frozen case `cases/max12_912_order3_nu_parity_normal_q12_20260824`;
- the dependent `Q12` formal-branch report and case.

Their bytes are unchanged.  Exact hashes and the hostile refutation are in
the new case's `QUARANTINE.md`.  The reviewed parity genus-five theorem is
unaffected: its replay uses the polynomial numerator `1+3v` in (1.2).

## 2. Source-honest reconstruction

Reconstruct all eight Faber tail rows from the pinned coefficient compiler.
On the parity fixed locus

```text
f=(z^3+p*z)^3+x5*z^5+x3*z^3+x1*z,
```

the odd rows vanish.  The complete first-order normal block remains

```text
J_N=d(r1,r3,r5,r7)/d(a0,a2,a4,a6).                   (2.1)
```

Retain the reviewed reversible chart

```text
A=x3-2*p*x5,   p*x5*A != 0,   v=A/(p*x5),
x3=p*x5*(v+2),
x5=-36*p^2*v^2*(3v^2+3v+1)/(3v^2-2),                (2.2)
```

and use exactly (1.2).  Exact substitution verifies `r2=r4=0` and recovers

```text
r6=-2304*p^9*v^6*(3v^2+3v+1)^3*A5(v)/(3v^2-2)^4,

A5(v)=33v^5+117v^4+131v^3+69v^2+18v+2.              (2.3)
```

## 3. Correct determinant and residual octic

On (1.2)–(2.2), exact rational-function arithmetic gives

```text
det(J_N)=p^20*226492416*v^16*(3v^2+3v+1)^8*Q8(v)
         /(3v^2-2)^10,                                (3.1)

226492416=2^23*3^3,

Q8(v)=-999*v^8-1539*v^7+1782*v^6+6498*v^5
      +7320*v^4+4428*v^3+1548*v^2+296*v+24.          (3.2)
```

The replay contains the required old-pass/new-fail controls:

```text
wrong (1.1): r2,r4 are nonzero; old Q12 identity passes;
right (1.2): r2=r4=0; old Q12 identity fails; (3.1) passes.
```

At the smallest numerical control `p=v=1`, the correct chart has

```text
x5=-252, x3=-756, x1=27720,
det(J_N)=25275425185572323328,
old Q12 RHS=169664962152837939200/243.
```

The two values differ exactly.

Euclidean checks give

```text
gcd(Q8,Q8')=1,
gcd(Q8,v)=gcd(Q8,3v^2+3v+1)=gcd(Q8,3v^2-2)=1,
gcd(Q8,A5)=gcd(Q8,Q12)=1.                             (3.3)
```

The reviewed chart already separates `v=0`, `3v^2+3v+1=0`, and
`3v^2-2=0`.  Therefore the sole residual first-order normal-rank boundary on
the retained chart is

```text
Q8(v)=0.                                               (3.4)
```

Because `Q8` is coprime to the numerator of (2.3), loaded algebraic
coefficient points exist over its roots.  This says nothing yet about formal
lifting or actual trajectories.

## 4. Exact scope

This report replaces only the first-order rank checkpoint.  It does not
transfer the quarantined formal-branch argument from `Q12` to `Q8`.  Both
rank-three minors, transversality to the loaded parity curve, and the
equivariant formal normal form must be recomputed at `Q8` from scratch.

There is no `Q8` trajectory, Taylor-boundary, non-parity exhaustion,
all-`(9,12)`, maximum-twelve, counterexample, or Jacobian-conjecture
conclusion.

## 5. Replay

```sh
shasum -a 256 -c cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/MANIFEST.sha256
python3 cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_parity_normal_q8_erratum_20260824/replay.json -
```

The replay uses only Python's standard library, pins the compiler, reviewed
parity replay, and hostile refutation by hash, and proves every displayed
identity and gcd exactly.
