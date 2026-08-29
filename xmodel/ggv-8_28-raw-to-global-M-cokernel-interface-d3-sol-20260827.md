# D3: first raw-to-global `8_28` / `M`-cokernel interface prototype

Date: 2026-08-27  
Lane: `a1_total_lift_design` / Sol2

## Verdict

**`STOP-FIRST-MISSING-PROVENANCE` (exact, fail closed).**

The frozen artificial-control run does not license a global polynomial
`E22` as a descendant of the raw `2S/3S` source.  The first missing typed
field is

```text
local_carrier_fixture.raw_to_morse.cleanup_DAG
```

whose required type is an exact serialized derivation from named raw
coefficient slots through the formal Morse/approximate-root cleanup.  The
smallest concrete witness is R1's boundary:

```text
raw F14 = Q * X^2,
artificial local fixture U14 = X.
```

Thus `U14=X` is not a direct raw coefficient.  It could only be justified by
a nonlinear, source-pinned cleanup calculation including the sidecars, and
no reviewed R0/R1/R2 artifact contains that calculation.  R0's literal raw
face and its hand-specified local cusp fixture are therefore retained as
separate objects.  The compiler emits neither a typed `E22` nor a typed
seven-vector.

This is the intended useful negative interface outcome, not an `8_28` face
exclusion.

## 1. Frozen raw source

The exact ambient source is the polynomial ring over `Q` on named raw slots
`f_i_j` and `g_i_j`.  The chart is `Q[t,X]`, with

```text
x^i y^j in f |-> t^(8+3i-j) X^i,
x^i y^j in g |-> t^(12+3i-j) X^i.
```

The compiler independently enumerates every lattice point of `2S` and `3S`
and checks it against the slice formulas.  Through weight 22 the exact
census is:

| source | named slots |
|---|---:|
| `F` / `2S` | 141 |
| `G` / `3S` | 301 |
| total | 442 |

The boundary rows replay as

```text
F14: t^14 X^2       (raw monomial x^2)
G21: t^21 X^3       (raw monomial x^3)
G22: empty.
```

The frozen input also reconstructs R0's literal artificial face assignment

```text
B = x (x y^4 - 1)^7,
f = B^2 - 2 x^8 y^32 + y^8,
g = B^3 - 3 x^16 y^60 + 3 x^8 y^36 - y^12,
```

as 17 nonzero `F` slots and 25 nonzero `G` slots.  Every one maps to a named
raw slot at a weight at most 22.  There is no serialized map joining that
raw assignment to R0's separate `V8=1/48`, `U14=X` cusp fixture.

## 2. Rings, local charts, and retained tags

The required pipeline is explicitly typed as

```text
Q[f_i_j,g_i_j]
  --raw chart--> Q[t,X]
  --formal cleanup at p--> kappa_p[[t,u]]
  --factor/deck gluing--> Q[X] containing literal E22
  --linear remainder--> Q[X]_{<=6}.
```

Here `p` runs over the four rational irreducible factors

```text
X-1, X+1, X^2+1, X^4+1.
```

Every factor has its own identifier and degree.  The orientation is
`u=H mod t`, the determinant tag is `u_X(c,0)=H'(c)`, and the deck tag is
`ORIENTED_PLUS_H`.  R0's two formal root-sign packets retain separate
factor-sign and deck tags and remain marked `polynomial_source_status =
REJECTED`, exactly as in R0.  The first-run cusp fixture uses the R2
`V8 != 0` carrier label on each factor, but that label is not treated as
raw provenance.

No alias is consumed as a map.

## 3. Exact seven-coordinate reducer

For

```text
H=X^8-1,
M(Y)=4 H Y' + 6 H' Y,
```

the endpoint is a vector-space quotient, not a quotient ring.  For a leading
term `p_m X^m`, `m>=7`, the replay subtracts

```text
p_m / (4*(m+5)) * M(X^(m-7)).
```

At each step it serializes the cancelled degree and coefficient, and finally
checks the exact identity `P=M(Y)+r(P)` with `deg r<=6`.

The hand-specified R0/R1 global polynomial is quarantined from raw
compilation, but it is a valid reducer positive control:

```text
1 + (13/12) H = M(X/48),
r(1 + (13/12)H) = (0,0,0,0,0,0,0).
```

The negative control gives

```text
r(1) = (1,0,0,0,0,0,0).
```

Changing `13/12` to `1` is detected with remainder
`(1/13,0,0,0,0,0,0)`.

Most importantly, the compiler replays

```text
r(H X^i) = -12/(i+13) X^i,  0<=i<=6.
```

Hence `r o (H*)` on `Q[X]_{<=6}` has diagonal

```text
(-12/13, -6/7, -4/5, -3/4, -12/17, -2/3, -12/19),
```

all entries nonzero.  The global `H`-multiple can therefore move every one
of the seven coordinates.  The 16 possible factorwise carrier patterns do
not determine `E22` or its seven-vector.

## 4. Fail-closed controls

All registered controls pass:

- inserting the nonexistent raw `F14` term `X` is rejected (its pullback
  would be `x*y^-3`, outside `2S`);
- deleting the orientation tag is rejected;
- deleting one factor tag is rejected;
- deleting the cleanup DAG produces the registered first-field stop; and
- mutating the quarantined `13/12` coefficient produces a nonzero remainder.

The full frozen source and result reproduce byte-for-byte under:

```bash
python3 cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/compile_d3.py \
  --check \
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json \
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RESULT.json
```

The replay prints `PASS D3 exact source/result replay` and uses only exact
`Fraction` arithmetic at desk scale.

## 5. Smallest honest successor

The next object is not a search over branch bits.  It is a serialized
raw-to-Morse cleanup DAG through weight 22 with, for every derived
`V8/U11/U14` and sidecar term:

1. the named raw coefficient inputs;
2. every coordinate substitution and nonlinear operation;
3. its factor, chart, deck, orientation, and determinant tags;
4. the gluing rule producing one polynomial in `Q[X]`; and
5. the literal resulting `E22`, including its `H`-multiple.

Only after those checks does the seven-coordinate reducer become a verdict
engine.  A proof that `U14=X` cannot arise under all allowed cleanups would
also be an honest successor, but the direct raw-row mismatch alone is not
that proof.

## Scope firewall

The reviewed R3 squarefree replacement-edge theorem is pinned only as an
artificial-scope firewall and is not consumed as a source pair.  This D3
result proves no face/family exclusion, no source/landing coverage, no
`G2-PSC`, no `G2-BD`, no Keller pair, no counterexample, and no JC2 result.

## Frozen artifacts

```text
87fd708fa0e6d1a554724489d3b3b6065e2c6f89c1c1a11414a2ac0b147d4541
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/PREREGISTRATION.md
f3c758e052d95252438fb9665ac2f2b27705019e91a41c2aa851dd41e9463bf4
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/compile_d3.py
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RAW_INPUT.json
a1d83f3f0ec1635844a3d8c67b59ce437c8d846617ae1250f2cf2e3db4a64b3f
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/RESULT.json
9f63f2d01d9ffccc44bedf8d318496336419a51fa3a1e7557f0d74f9c9b33fff
  cases/ggv_8_28_raw_to_global_m_cokernel_interface_d3_20260827/README.md
```
