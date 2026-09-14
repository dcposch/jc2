# Independent t = 8 generator-image checks

PASS: fixed indexed signed minor map and W1..W7 match at every validation sample.

`check_t8_images.py` imports only Python standard-library modules and calls no CAS or subprocess. It reads `box/k16rank-20260903/terminal_t8_exact_none.out` directly (not `gen.py`), asserts the recurrence/done sentinels and all 16 row labels, and selects rows T15 down through T8. A strict shunting-yard parser evaluates integer literals, variable names, parentheses, and +,-,*,/,^ in F_p; division uses `pow(denominator,-1,p)`, asserts nonzero denominator, and never uses floats. Eight parser sanity expressions check precedence, unary minus, rational division, exponentiation, and coefficient/variable products.

The source ring map is `yy -> 11288` over F_32003, `yy -> 23825` over F_32027, `b4 -> 1`, and `qj_0 -> qj` in the declared ordered target ring `F_p[q2,q3,q4,q5,q6,q7]`. H8(yy)=0 is asserted. Both `.ms` headers and the exact set of variable names are asserted. The sample points list coordinate values in that target order.

For each top row T_r, direct evaluations at b3=0,1,-1 recover `c=T(0)`, `b=(T(1)-T(-1))/2`, `a=(T(1)+T(-1)-2T(0))/2`. A fourth independent evaluation at b3=2 checks the recovered quadratic. This is repeated for all eight top rows at every sample. Then the script recomputes `B_r=a0*b_r-a_r*b0`, `C_r=a0*c_r-a_r*c0`, every two-row determinant of the declared matrix with rows `(C_r,B_r)`, and `W_r=a0*C_r^2-b0*B_r*C_r+c0*B_r^2`, all modulo p. The recomputed a0 is nonzero throughout (the JSON records it).

To make generator order explicit, one calibration sample at p=32003, `(2,3,5,7,11,13)`, uniquely identifies every signed minor and checks bijectivity across all 21 row pairs. That indexed signed map is then frozen. The remaining five samples at p=32003 and all six at p=32027 are compared entry by entry using the same map, with no rematching or multiset comparison. Thus there are 308 holdout image-value comparisons (11 samples times 28 generators), in addition to 28 calibration values.

For each pair (r,s) in the following ordered list, the corresponding `.ms` generator is sampled against `C_s B_r - C_r B_s` (the negative of the determinant in row order `(C_r,B_r),(C_s,B_s)`):

```text
(1,6) (1,5) (1,4) (1,3) (1,2) (1,7) (2,5) (2,4) (2,3) (2,6) (2,7) (3,4) (3,5) (3,6) (3,7) (4,5) (4,6) (4,7) (5,6) (5,7) (6,7)
```

Generators 22 through 28 are W1 through W7, with positive sign in that order.

The five holdout points, reused at both primes, are:

```text
(17, 19, 23, 29, 31, 37)
(41, 43, 47, 53, 59, 61)
(67, 71, 73, 79, 83, 89)
(97, 101, 103, 107, 109, 113)
(127, 131, 137, 139, 149, 151)
```

All 28 images matched at every sample at both primes. Total wall time was 11.875 seconds. `t8_images.json` preserves all exact expected/observed residue vectors, roots, points, index maps, and hashes. `check_t8_images.log` is the execution transcript.

These are deterministic sample checks that can detect ring/map/export corruption. They are not claimed to prove formal polynomial identity, and do not replace the CAS identity assertions in the generator prefix or the Groebner computation.

```text
8f41559606bbf9f2c592f5569ee0feef596d7196d39d2290941bdf889990f767  box/k16rank-20260903/terminal_t8_exact_none.out
ccfdaf9771a7113155dd3f6ed55dd7d66351c5c411f6b917b255746867181ab3  check_t8_images.py
d6401d43c62af47b17b67a1fd91221e31b9bbfbb775f092bda1d839057749e6c  box/k16t8-20260905/msolve_t8_affinew_p32003_b0.ms
8be78590cbd8ab8edba4097372f3978986c18e9aa8c0b17da8066ed8f796a8d4  box/k16-t8-gate-20260905/affinew_p32027.ms
8384df2e680a208f36a006b219dc465d7588e4f54c20375ea5defb6092db5a97  t8_images.json
c5813a676c5856e8b1e0211322443d1909d36ade8d7367452a871c0ec34b3592  check_t8_images.log
```
