# Deep lambda-zero tail: the complete fixed `Q=X` even prefix has zero endpoint

Date: 2026-08-28

Status: **exact fixed-even-prefix exclusion theorem; not a universal
`lambda=0` exclusion**

## Statement

Let `K` have characteristic zero and put

```text
A=X^4-1,  Q=X,  r=e=F8=F10=F12=F14=0,
F1=F3=F5=0,
F2=-A^3 Q/8,  F4=A^2 Q^2/256,  F6=0.
```

Assume the reviewed `lambda=0`, exact-tail branch and impose the exact odd
gates `q7,q9,q11,q13,q15`, with all literal raw floors on
`f,F9,F11,F13`.  Let the complete characteristic have arbitrary scalar modes
(in particular arbitrary `c2,c4,c6,c8`; `c2` may be nonzero).  If `G13` lies
in its literal raw window and `G15` is polynomial, then

```text
F11[X^1] G11[X^0] - F7[X^0] G15[X^1] = 0.          (T)
```

Consequently this entire fixed even prefix cannot satisfy the authoritative
endpoint target, whose left side must equal `1`.

Only `G13`'s lower floor and one residue coordinate of `G15` are needed.
No `G17,...,G21` window, four-root resultant, or later determinant row is
used in the exclusion.

## Exact five-dimensional odd fiber

An independent rational RREF of the five gates has 55 variables, rank 50,
and free primitive coordinates

```text
a0=d15[X^4], a1=d15[X^5], a2=d15[X^6],
a3=d15[X^8], a4=d15[X^9].
```

The origin coefficient of `f` is

```text
f0 = -(2^29/75)a1 + (2^28/225)a4.                 (1)
```

Since `F7=A f` and `A(0)=-1`, `F7[X^0]=-f0`.

## The two receiver equations

Reconstructing each characteristic trajectory separately gives

```text
G13[X^0] = (3/4)c6 f0.                            (2)
```

The base trajectory and the `c2,c4,c8` trajectories have zero load in this
slot.  Thus the literal `G13` floor gives `(2)=0`.

At weight 15, take the numerator of the possible `A^-1` pole, reduce it
modulo `A`, and read its `X^1` coefficient.  Polynomiality gives

```text
R15 = -(7*2^19/3)c6 a4 + (2^29/15)c8 a2 = 0.      (3)
```

The base, `c2`, and `c4` trajectories have zero load in this residue
coordinate.

## Exact endpoint identity

The `c4` contribution cancels identically between the two terms of the
endpoint.  Indeed `G11[X^0]=-c4 f0` and the `c4` load in `G15[X^1]` is
`c4 F11[X^1]`.  The remainder is

```text
E = f0 H,
H = c6(-2^21 a1/5 - 2^19 a4/3) + c8(2^29 a2/75).
```

It satisfies the polynomial identity

```text
E = (f0/5) R15
    + (4/3)(-2^21 a1/5 + 2^20 a4/15) G13[X^0].    (4)
```

Equations `(2)`--`(4)` prove `(T)` without a case split and for arbitrary
values of the displayed scalar modes.  The `c10` mode first could couple to
an odd coefficient through `F5`, but `F5=0`; modes born after weight 10 have
not entered by `G15`.

## Scope firewall

This is stronger than the earlier one-point failure: every odd primitive
choice over this fixed even prefix is excluded.  It does **not** exclude the
full `lambda=0` branch.  The smallest remaining releases are the even data
`Q` (first, as an arbitrary quadratic), then `e` and `F8`; later even raw
slots may also matter.  The four-root endpoint system should be appended only
after those local characteristic conditions pass.

## Replay

```bash
python3 cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_qx_fixed_even_endpoint_zero_20260828/verify_qx_fixed_even_endpoint_zero.py
```

The exact standard-library replay derives the five-dimensional fiber from
the frozen all-row `q` formulas, reconstructs local jets and global Laurent
residues independently, verifies every coefficient in `(1)`--`(4)`, and pins
the preceding q15 and `G13` packets.
