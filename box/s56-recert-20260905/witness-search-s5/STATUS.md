# S5 `[2]` full-chart witness search status

Outcome: **no exact rational sample point found**.  Nothing in this directory
is a survivor certificate or a verdict on the full 115-parameter, 261-row
chart.  All specializations below were used only for witness search; a unit on
one of them does not kill the parent chart.

## Exact reductions searched

For `h=y^3`, write

```
Q = y^6 + b2(x)y^2 + b1(x)y + b0(x),
P = y^9 + sum_{i=0}^8 p_i(x)y^i.
```

The rows of `J(Q,P)` in `y^13,...,y^5` determine the `p_i` successively,
up to nine integration constants (two are Jacobian-invisible).  The five
remaining coefficient forms are emitted by `emit_h_y3_system.py`.  The x
caps are the full completed-chart caps: `deg b2<=6`, `deg b1<=7`, and
`b0 in x*Q[x]`, `deg b0<=9`.  Thus this is the entire `h=y^3`
specialization, not a weight-floor deletion inside it.

At characteristic 32003 its 33-variable/90-generator Rabinowitsch system was
a unit:

```
msolve 0.10.1: [-1], basis size 1
wall 8.07 s; maximum RSS 455544 KiB; exit 0
```

The exact-Q Singular replay ran for 150 seconds without a basis marker and was
terminated by its watchdog.  The modular unit is therefore not promoted.

For the centered even/odd specialization

```
Q = y^6 + A(x)y^4 + B(x)y^2 + C(x),
P = y*(y^8 + g3(x)y^6 + g2(x)y^4 + g1(x)y^2 + g0(x)),
```

the high rows eliminate `g3,...,g0` exactly.  The full completed support has
caps `(deg A,deg B,deg C)=(3,6,9)` and gives 26 variables/55 generators after
saturation.  Modular unit subcharts were obtained at the following successive
caps:

| caps | p=32003 wall | peak RSS | result |
|---|---:|---:|---|
| `(1,3,5)` | 0.05 s | 4480 KiB | `[1]` |
| `(2,4,6)` | 1.19 s | 54756 KiB | `[1]` |
| `(2,5,7)` | 3.80 s | 129216 KiB | `[1]` |
| `(3,5,7)` | 45.44 s | 1058152 KiB | `[1]` |
| `(3,5,8)` | 113.97 s | 1456736 KiB | `[1]` |

The full `(3,6,9)` computation hit its 300-second watchdog without a result.
Only `(1,3,5)` was confirmed exactly over Q: Singular returned `G[1]=1`,
`DIM=-1`, `UNIT=1` in 0.03 s at 12456 KiB.  Larger exact-Q attempts did not
finish within their watchdogs.

## Sparse and numerical searches

`search_monomial.py` screened 44280 monomial paths in the exact `h=y^3`
distribution.  `search_even_odd_monomial.py` screened 62976 monomial paths in
the exact even/odd distribution.  Both used p=32003 only as a filter and would
have reconstructed and checked every hit over Q; neither produced a hit.

`numeric_even_odd.py` used the exact 54 coefficient equations with `c=1`.
It found no finite zero.  Its best residuals are an escaping degeneration
`C=epsilon*x^9`, `k0` proportional to `1/epsilon`; the omitted residual is
proportional to `epsilon^2`.  This is not a point and was not rationally
reconstructed.

Key custody hashes:

```
d3071dd2a854d084e19f06567f71bda898c1878f10e9cde5877b13fd8bc249e4  h_y3_full_p32003.ms
0333251e6ebb3890ef547f522ec55f27f0cef9a860998757e31f3e1b819e7490  h_y3_full_msolve.out
8dd5c6f3a8165e45f1cf65a8f1276cfbf788077f81012e332367528277a5be29  even_odd_d1_3_5_p0.sing
4e476b3991570356e8cea31948cbe4ce724628b17b9b9f72ac60f18cbff770a9  even_odd_d1_3_5_Q.out
45296d07cbec184ee9e9776c7359afbe25a0ff9c7e04d8094ba1e44e71f85654  search_monomial.out
4098e71649019d5ff0aa5cacfc062ab84610b1c108ea20f1b55d550e4b350dea  search_even_odd_monomial.out
```
