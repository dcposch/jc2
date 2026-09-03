# Independent charged-input/control audit

Current-lane custody: the 17 `(basename,sha256)` pairs were generated directly
from `xmodel/k16-terminal-determinant-sol56-20260903.run.v2` with `awk` and piped
to `sha256sum -c`; all 17 frozen files returned `OK`.  Separately, all 106 files
listed by the charged `artifact_summary.json` match its hashes, and
`validate_claim_artifacts.py` returns `CLAIM_ARTIFACT_VALIDATION_PASS`.

## Declared algebra, map, and sign

The terminal report fixes

```text
q=2t+1, e=3t+1,
H_t=12q^2 y^2-12q(t+1)y+(t+1)(3t+2),
A_t=Q[y]/(H_t), d=2qy-(t+1),
A_t=Q[d]/(3d^2-(t+1)),
g=te(3d+2(t+1))/(6q^3), c=-yg.
```

See `xmodel/k16-terminal-proof-sol56-20260903.md:35-56`.  The original chart
map is `x=q_(t+1),1 -> 1`, `y=q_(2t+1),1 -> y`, and after the proved spine the
residual variables are `b3,b4,u_2,...,u_(t-1)`, with `u_i=q_(i,0)`.
The records contain `R=-E_t`, while the question uses
`T_(t,k)=[X^k]sigma_t(E_t)=-[X^k]sigma_t(R)`; see lines 58-65.

The algebra is a field unless `t=3s^2-1`; at those infinitely many split
indices it is `Q x Q`, evaluated at `d=+s` and `d=-s`.  Componentwise treatment
is mandatory.

## Closed recurrence

With `L=X-b4`,

```text
U=X^q+sum_(i=2)^(2t) u_i X^(q-i),
C=X^(t-1)+sum_(j=1)^(t-1)c_j X^(t-1-j),
B_0=0,
B_(m+1)=g(3m+5)C_m/(2y(m+1)),
S_m={3g(m+1)U_(m+1)
     +sum_(a+b=m-1)(3+2a-b)C_aB_b
     +(gb3/2)(5m+7)C_m}/{y(2m+1)}.
```

Then `V=L^2C-yb3`, `Y=LS-b3B-gb2`, `Z=LB-gb3`,
`N=-VY'+V'Y+2U'Z`, `P0'=(N-N(0))/(2yL)`, and
`R=VP0'-U'Y-yg`.  The coefficient convolution is displayed at terminal-report
lines 146-161.  The high variables are ordered
`c_1,...,c_(t-1),u_t,...,u_(2t),b2` and solved by
`z_j=-rho_j/p_j`; the closed `p_C,p_Q,p_b2` are at lines 185-211.  Finally

```text
T_(t,k)=-sum_(m>=k) binom(m,k)(-b4)^(m-k) R_m.
```

The symbolic derivation of the high diagonals, which the hostile gate had
identified as missing, is supplied by the charged pivot report, especially
`xmodel/k16-pivot-forms-grok46-20260903.md:58-120`; its exact specializations
match all 32 available nonlinear pivots at `t=2,3,4,5` (lines 122-135).

## Denominator ledger

Algebra elements inverted are `y`, the class of `g`, `L_C`, `L_Q`, and
`3qd+(t+1)` (the last `b2` pivot).  Their unit tests are the resultants at
terminal-report lines 265-338.  Rational/indexed factors are

```text
2,3,6,q,q^2,q^3,t,e,t+1,3t+2,4t+1,
m+1 (0<=m<t), 2m+1 (0<=m<=2t),
4t-2j+1 (in the p_C,p_Q ranges),
q-j (t<=j<=2t), F_C, F_Q.
```

Expanded symbolic binomials additionally have only constant factorial
denominators.  The `b3`-axis adds `3t-1`.  The `u2` coefficient-pair recurrence
also exposes `t-2r` and `4t-4r+1`, plus the same pivot denominators.  Its final
accumulated `D(t)` is not known in the charged report, so no complete
denominator audit exists for that axis coefficient yet.  Likewise no
denominator or specialization audit exists for a uniform top-tail basis or
determinant.

The split set is not a denominator exception.  The norm formula
`Res_y(H_t,ad+b)=4q^2(3b^2-a^2(t+1))` must be applied before any inverse.

## Exact and modular controls

| t | recurrence/records | top tail | residual chart |
|---|---|---|---|
| 2 | exact, both rational factors, banked rows match | exact unit on both factors | `RESIDUAL-ZERO` false; band zero a unit on both factors |
| 3 | exact banked-row match | exact unit | exact powers `b3^3,u2^6` |
| 4 | exact banked-row match | exact unit | exact powers `b3^4,u2^8,u3^6` |
| 5 | exact banked-row match | exact `modStd(I,1)` gives `1` | exact powers `b3^5,u2^13,u3^9,u4^7` |
| 6 | 12 exact rows emitted; both mod-1009 banked rows match coefficientwise | exact run timed out, no verdict | exact powers `b3^5,u2^16,u3^11,u4^8,u5^7` |

The pure-power data are terminal-report lines 553-575 and prove the fixed
characteristic-zero radicals for `t=3,4,5,6`.  The exact top `t=5` and timeout
at `t=6` are lines 426-453.  The separate convolution evaluator checks three
points on each of two mod-1009 fibres for `t=2,...,6`; those are pointwise
controls, while the full Singular driver supplies the stated coefficientwise
record comparisons.

At `t=2`, stored `R=-E` on `b4=0` has branch rows

```text
y=1/5,d=-1: (-7/625,0,0,0),
y=2/5,d=+1: (-42/625,0,0,28b3^2/625).
```

Thus the older middle-spine sentence saying all positive rows vanish at `t=2`
is false globally and is superseded by terminal-report lines 577-587.

At `t=11`, `H_11=12(23y-5)(23y-7)`.  The exact factors are
`d=+2,y=7/23` and `d=-2,y=5/23`, reducing to `y=439,746` mod 1009.  The
charged control has all 23 high pivots nonzero and five `PASS_FORMULA` points
per fibre, but no independent terminal-record comparison, no top-prefix
finiteness/determinant computation, and no residual radical result.  The first
residual `dp/std` run timed out at 600 seconds; the second was not run.

## Split t=2 determinant control and correction to the target

For `F_r=T_(2,2+r)|_(b4=1)` and `J_2=<F_1>`, the two components are:

```text
d=-1:
 F0=7(16b3-35)/640,
 F1=-7(88b3-295)/640,
 basis (1), det(mu_F0)=287/1408.

d=+1:
 F0=-18(287156086b3^2-27046560b3+106639425)/74352915125,
 F1=-14(1189646642b3^2+304374720b3-1207034325)/371764575625,
 basis (1,b3),
 det(mu_F0)=2762023282304080896/297558232675799463481.
```

Both determinants are nonzero, but the component ranks are `1` and `2`.
Consequently `B_2` is finite but is not free over `A_2=Q x Q`; the requested
uniform "indexed A_t-basis" formulation is literally false at the base case.
Use componentwise bases/determinants (equivalently a finite-projective module
with locally varying rank) at every split index.  Finite over `A_t` is enough:
for each field factor `K_epsilon`, `B_epsilon` is finite dimensional and
`(J,F0)=[1]` iff `B_epsilon/F0B_epsilon=0` iff `mu_F0` is bijective iff its
determinant is nonzero.  The exact reproduction is
`python3 box/k16det-20260903/audit/t2_component_determinant.py`.

## Logical gaps and safe verdict

The modular lengths `8,44,224` for `J_t` at `t=3,4,5` prove neither uniform
finiteness nor a recurrence.  The apparent fit is expressly unproved.

The `b3` calculation proves only the image of `I_(t,+)` on the coordinate
axis has radical `(b3)`.  It does not prove `b3^N in I_(t,+)`.  The `u2`
calculation is the final triangular quotient modulo
`(b3,u_(t-1),...,u3)`, conditional on all earlier containments.  Even a
complete factorization of its denominator and norm would leave the actual
containment `b3^N in I_(t,+)` and the intermediate `u_j` containments for
`j=t-1,...,3` open.  Coordinate-axis tests alone can miss off-axis components.

Therefore the charged inputs support only `PARTIAL`: theorem (T) is exact for
`t=1,...,5`, the residual half is exact also at `t=6`, and the all-`t`
top-tail and residual statements remain open unless the present lane supplies
new indexed proofs.  No exit-price assertion occurs, so no `charge_basis`
line applies.

## Audit of the symbolic two-solve `u_(t-c)` sector

The post-charge driver `residual_sector_m2_symbolic.py` and output
`residual_sector_m2_tc.out` have SHA-256 hashes
`b4e9683b5f236b96db56d4deaf1717649c32ac4b60ac66e1080a333a0a4bd54b`
and `a5a1d41ad782ed8441f8e74d8359f377b1a355a7c8ebbfbc863c55b6fed6c619`.
Put `c=t-j`.  For integers `c>=1,t>=3c+2`, equivalently
`ceil((2t+2)/3)<=j<t`, one has `2j<q<3j`.  Hence the axis recursion has
exactly the two solves `chi_1` (the weight-`j` C-variable) and `upsilon_2`
(the weight-`2j` U-variable), no `b2` solve, and its first surviving term is
`rho_3`.  It occurs in terminal band

```text
4t+1-3j=t+3c+1 <= 2t-1.
```

Write

```text
G=c^2+2ct+4c+t^2+t+1,
F=3c^4+24c^3t+42c^3+66c^2t^2+146c^2t+119c^2
  +72ct^3+238ct^2+234ct+104c
  +27t^4+134t^3+223t^2+136t+32,
Q=c^2-10ct-14c+25t^2+22t+1.
```

The output's two coordinates of `lambda=rho_3` have common reduced
denominator `q^3 G F^3`, and its quadratic norm factors exactly as

```text
3 lambda_b^2-(t+1)lambda_a^2
=9 t^2(t-c)^6(t+1)(3t+1)^2(4t+1)(t+c+1)^6 Q
 /(q^6 G F^3).
```

This identity was independently re-expanded to zero.  If `t=3c+2+r`, then

```text
Q=196c^2+140cr+332c+25r^2+122r+145 > 0.
```

Also `F,G>0` termwise.  Thus the norm is strictly positive on the entire
integer sector, including both factors at every split index.

All transient divisors in the displayed recurrence are covered by

```text
2,3,6,q,t,c,e,t+1,3t+2,2c+1,F,G,
4t+1, 2t+2c+1, 4c+1, 6c-2t+1.
```

Here `F` is the C-pivot primitive norm, while the Q-pivot primitive norm is
`4G`; `2c+1=q-2j`.  The four final factors are the Euler divisors for series
degrees `0,1,2,3`.  In the sector the first three are positive and
`6c-2t+1<=-3`; all other listed factors are positive.  The reduced
intermediate denominators are `qF` for `chi_1` and
`2(2c+1)qGF^2` for `upsilon_2`.

Substitution `c=1` and `c=2` reproduces the two separately generated symbolic
outputs coefficientwise.  Exact comparison with the independent fixed-pair
evaluator passed at `(t,c)=(5,1),(6,1),(8,2),(9,2),(11,1),(11,2),(14,4),
(26,8)`, including two sector boundaries and the split case `t=11`; the
first two also reproduce the charged exact `t=5,6` rows.

The safe conclusion is axis-only:

```text
sqrt(image(I_(t,+) in A_t[u_j]))=(u_j)
```

after setting `b3=0` and every `u_i` with `i!=j` to zero.  Equivalently the
image contains a unit times `u_j^3`.  This is not a proof of a power of
`u_j` modulo `(b3,u_(t-1),...,u_(j+1))`, because the computation additionally
kills every lower axis variable.  It therefore does not close any of the
triangular containments required for uniform `RESIDUAL-ZERO`.
