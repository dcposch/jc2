# Reproduction manifest

Input SHA-256 verification was run first on all eight frozen inputs; every
digest matched the value in the lane request.  No non-frozen source input was
used.  The mathematical source pages inspected in the frozen PDF were Moh
Appendix II, pp.150--151, 173--175, 179--180, 197--198, and 207--211.

Environment: CPython 3, SymPy 1.12, one core per command.  Runs below were
made from `/home/ubuntu/jc2` on 2026-09-03 UTC.

| command | wall time | max RSS | result |
|---|---:|---:|---|
| `python3 box/tladder-drivers-20260903/hadic_identity_check.py` | 1.07 s | 50,940 KB | exit 0 |
| `python3 box/tladder-drivers-20260903/moh_1510_jacobian_control.py` | 9.56 s | 55,548 KB | exit 0 |
| `python3 -u box/tladder-drivers-20260903/moh_1612_reduction_control.py` | 19.79 s | 65,088 KB | exit 0 |
| `python3 box/tladder-drivers-20260903/keller_uniform_counterfamily.py` | 0.72 s | 50,684 KB | exit 0 |
| `python3 -m py_compile box/tladder-drivers-20260903/*.py` | <1 s | not measured | exit 0 |

Main results:

- **PROVED-HERE:** the charged `(2,3)` Jacobian display is false.  The driver
  verifies the corrected identity and gives the concrete witness
  `h=y,beta=x/2,G1=3x/2,G0=0`.
- **SOURCE-READ + PROVED-HERE:** the literal p.208 `(16,12)` display has 17
  parameters and produces 77 coefficient equations for `J=C*x`.  The p.209
  normalized family has ten parameters, five nonconstant canonical H-digits
  of maximum x-degree one, and 36 equations.  An exact coefficient/gcd
  certificate proves its `C!=0` locus empty.
- **SOURCE-READ + PROVED-HERE:** the pp.210--211 `(15,10)` displayed shape has
  twelve parameters, three nonconstant H-digits of x-degree two, and 27
  equations for `J=C*x^2`.  An exact two-branch coefficient certificate proves
  its `C!=0` locus empty.
- **PROVED-HERE:** the uniform family in `keller_uniform_counterfamily.py`
  has `J(P,Q)=x^k`.  At `k=0` it is a polynomial automorphism in every degree;
  its sole nonconstant H-digit has unbounded x-degree.
- **UNREVIEWED / OPEN:** the earlier Moh count `22 [15 or 13]` is stated on
  p.208 but its corresponding ansatz is not printed.  The frozen pp.210--211
  shape is already the later twelve-parameter simplification.  No fabricated
  reconstruction is claimed.

Driver SHA-256 values:

```text
bb16b67fdb035de24ddd86d9d753aba85d4b2d66511e27c771858bc2cfbcd3b7  hadic_identity_check.py
f7d13f4600070f0757179916a353305d41bb9dad8bac0f7024b0ae164479648f  keller_uniform_counterfamily.py
3786e1d5fe734ff703df5b96c7d6e9b347930e44b7c7e2777d3de4d577f1ca56  moh_1510_jacobian_control.py
481a6a43a69fcab86724523bee1812eaeb6ecd9c45509e4cd05d5f1e186d4800  moh_1612_reduction_control.py
33dadb6bb5dd780a5ecede7b84151c59076ecb33b1d5552e9ee583f9d45388e7  README.md
```
