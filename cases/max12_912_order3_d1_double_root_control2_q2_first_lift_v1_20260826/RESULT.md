# First omitted `q2` layer: transported-multiplier result

Date: 2026-08-26 UTC

Status: **EXACT NEGATIVE CONTROL FOR THE OLD MULTIPLIERS.**  The old witness
does not transport unchanged to the first later-`q2` layer.  This is not a
surviving branch and not a no-lift theorem for corrected syzygies.

## Dual AWS custody

- Box03 A/global-`dp`: tag
  `max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826T031500Z_box03_A`,
  worker PID `147189`, compiled input SHA
  `0c3e782a70251e9203dcf6f19c7e773611e77c6b0005bbb5394bba627bfda559`,
  stdout SHA
  `359fbf5abb3f203f3bd96512ca2270d4654c349df1f7902aba7c1bffd29c71af`.
- r6d B/`(lp(2),dp(8))`: tag
  `max12_912_order3_d1_double_root_control2_q2_first_lift_v1_20260826T031500Z_r6d_B`,
  worker PID `214973`, compiled input SHA
  `e8b72e82daa9f09a433b114e4f1730c5d9808956a49ed27827bdd8a73a3ac4a5`,
  stdout SHA
  `6a5a9a8ca8686a9bca7cc6e54d8c22ef66c702869e96e3b5031925f4c0d89a60`.

Both jobs returned rc 0 with empty compiler stderr, CAS stderr, and stdout
diagnostics; each used about 10 MiB RSS with zero swap.  All eight full rows
specialize at `q2=0` to the dehomogenized pinned expanded-B rows.  Both exact
orders verify the same canonical correction SHA

```text
6479de2923b83bcf77ddd756bcb9e3ff2ca7422cc5d7bbd434bdb6abf98abc69
```

and the same full lifted-polynomial SHA

```text
3dddd347d6e8b6e888f802e7fd62a5d61c2b7c8ab8e02aa3e599024ab72b839e.
```

## Exact result

With the reviewed old multipliers `F_i`, both jobs check literally

```text
W_q2 := sum_i F_i E_i(full q2) = W + q2*C,
```

where `C` has 37 terms and is printed in full in both stdout files.  At the
first omitted integral layer

```text
(L,T,H;D;beta*L;alpha*L)=(4,1,1;23;22;30),
```

the target `la^20` has weight 80, but `q2*C` has five terms of weight 75:

```text
q2/81 * (
    4*q0*r1 - 3*q0*r2
  + 4*q1*r0 - 3*q1*r1 + 12*q1*r2
).
```

Their general weight is

```text
D + beta*L + (15/2)*L.
```

Thus the transported polynomial does not have `la^20` as its least-weight
term when `D=23`; the old fixed-support witness alone cannot exclude this
later-`q2` support.

## Immediate graded-lift observation

Using the already frozen q2=0 special-fibre basis

```text
GH3 = 2*q0*r1 + 2*q1*r0 + 3*q0*r0,
GH5 = q0*r2 + q1*r1,
GH6 = 2*q1*r2 - q0*r0,
```

the parenthesized weight-52 coefficient divided by 81 is exactly

```text
(2/81)*GH3 - (1/27)*GH5 + (2/27)*GH6.
```

Hence the first bad coefficient is zero in the q2=0 graded quotient.  This
does not yet provide preimages in the original eight rows, but it makes the
next proof-discriminating test a sparse first-order module lift, not a full
new saturation: find `G_i` such that replacing

```text
F_i -> F_i + q2*G_i
```

cancels every term below weight 80 modulo `q2^2`.  A solution licenses the
next layer; a dual cokernel vector would prove this support obstruction at
first order.

## Firewall

This package proves only failure of the unchanged multipliers at one added
support layer.  It does not refute existence of a corrected witness, assert a
formal arc, or speak about moving axis/cusp, loads, the full fan, D1, or JC2.
