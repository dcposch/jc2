# td=8 affine family — parametric Prop. 8.1(iv)

Exact-arithmetic packet for the local reduced ODE on the equal-join merge
cell `nu=4+3t`, `(dp,dq,M)=(24+18t, 9+6t, 3)`.  Every integer `t>=0`
admits an explicit admissible solution over `Q`, unique up to scale:
the two reduced orbits are opposite, `p=(eta^{2 nu}-1)^3`,
`q=eta(eta^{2 nu}-1)`.

This is a vertex-local formal survival of Prop. 8.1(iv).  It is not an
exact-lambda, landing, realizability, degree-bound, or JC2 theorem.

Run:

```sh
python3 test_prop81iv_td8_affine.py
python3 -O test_prop81iv_td8_affine.py
python3 prop81iv_td8_affine.py
```
