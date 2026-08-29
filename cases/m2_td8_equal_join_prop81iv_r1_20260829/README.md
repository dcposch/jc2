# td=8 equal-join Prop. 8.1(iv), R1

Status: `SOURCE_READY_FOR_DIFFERENT_MODEL_REVIEW`.

This packet gives an exact local formal solution of Proposition 8.1(iv) for
every member of the reviewed affine merge family `nu=4+3t`, `t>=0`:

```text
p(eta) = (eta^(2nu)+1)^3
q(eta) = eta*(eta^(2nu)+1)
delta = X = 4nu
1-u = kbar = 2(2nu+1)/3
delta*p*q' - (1-u)*p'*q = delta*p.
```

The two roots of `T^2+1` give two distinct nonzero `nu`-orbits, each of
arrival multiplicity three. The common `q` multiplicity is one and `eta` is
the forced simple q-root. Degrees are `(6nu,2nu+1)`, with gcd three because
`nu=1 mod 3`.

The packet also verifies the two fixed local consumers on the same formal
route:

```text
incoming (21,15): p=(T-2)^2(T-3), q=eta(T-2)(T-3),
                  (delta,1-u)=(7,5), RHS=42p;
trunk (85,35):    p=(T-3)^3(T-4)^2, q=eta(T-3)(T-4),
                  (delta,1-u)=(17,7), RHS=204p.
```

Thus both identical incoming steps, every affine merge, and the fixed trunk
survive the vertex-local ODE test. No cross-vertex coefficient gluing follows.

Replay:

```sh
python3 td8_equal_join_prop81iv_r1.py --scan 1000
python3 test_td8_equal_join_prop81iv_r1.py
python3 -O test_td8_equal_join_prop81iv_r1.py
```

The scan is regression evidence; the proof is the displayed polynomial
identity. This certifies only local formal ODE survival. It does not certify
exact lambda, source landing, geometric realizability, a degree ceiling, or
JC2. No canonical consumer may use it before different-model hostile review.
