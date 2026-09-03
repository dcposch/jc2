# Generic-`t` coefficient-family notes (K=16 ray)

Scope: generic-family derivation only.  This note is not the lane report and
does not promote theorem (T) beyond a fixed-`t` certificate.  It uses only the
verified frozen charged inputs and the new fixed-`t` drivers under
`box/k16t3-20260903/`; neither prohibited in-progress report was opened.

## 1. Custody and cross-checks

**MEASURED.**  The receipt
`xmodel/k16-t3-uniform-sol56-20260903.run.v2` was parsed mechanically with
`awk`: its `charged_input_<i>_sha256` and `charged_input_<i>_basename` fields
were paired under its own `lane_inputs_dir`.  `sha256sum -c` returned `OK` for
all 10 files.

`generic_order_system.py` reproduces the frozen gauged `t=2` driver exactly:
the parameter list, all 37 tagged equations, and equation order compare equal
as Sympy objects.  Its `t=3` and `t=4` parameter lists and tagged equations
also compare string-for-string with, respectively,
`box/k16t3-20260903/t3/t_order_system.py` and
`box/k16t3-20260903/t4/t4_order_system.py` after the generic gauge-index
correction described below.

## 2. Denominator-free family

Put

```text
e=3t+1, q=2t+1,
z=pi-gamma,
B=pi*z+b1*pi+b2,
A=pi*B+b3,
h=pi*A+b4.
```

For `1 <= i <= e`, let

```text
S_i(t) = <1>                    (1 <= i <= t),
         <1,A>                  (t < i <= 2t),
         <1,A,B>                (2t < i <= 3t),
         <1,gamma,A,B,z>        (i=3t+1).
```

The gauged family is

```text
P = h^e + sum_(i=1)^e alpha_i h^(e-i),  alpha_i in S_i(t),
Q = h^q + sum_(j=2)^q beta_j  h^(q-j),  beta_j  in S_j(t),

const(beta_q)=0, alpha_t=0, const(alpha_e)=0.
```

The middle gauge is `alpha_(e-q)=alpha_t`, not `alpha_2` uniformly; `alpha_2`
was only its `t=2` specialization.  It comes from `P <- P-alpha_t Q`.
The endpoint gauges are the scalar target translations used in the charged
`t=2` proof.  All three maps are triangular and introduce no denominator.

The ungauged counts are

```text
alpha: t+2t+3t+5 = 6t+5,
beta:  (t-1)+2t+3 = 3t+2,
b_i and c: 5,
total: 9t+12.
```

Thus the three-gauge chart has `9t+9` unknowns including `c`: 27, 36, 45
for `t=2,3,4`.

For a compact equation schema set `alpha_0=beta_0=1`, `beta_1=0`, and use
`i=0,...,e`, `j in {0,2,...,q}`.  Before monic `h`-division, the coefficient
at level `k` is

```text
R_k = sum_(e+q-i-j=k) J(beta_j,alpha_i)
    + sum_(e+q-i-j-1=k)
        [(e-i) alpha_i J(beta_j,h) + (q-j) beta_j J(h,alpha_i)].
```

The exact carry recurrence is

```text
C_0=0,
F_k=R_k+C_k,
F_k = h*C_(k+1) + N_k,       deg_pi N_k < 4,
coeff(N_0-c*gamma)=0, coeff(N_k)=0 (k>0).
```

Division is by monic `h` in `pi`; this is a fixed linear operation and never
branches on a parameter leader.

### Coefficient dependence on `t`

In deficit indexing, every numeric coefficient is in `Z[t]`, of degree at
most one: the only `t`-bearing multipliers are
`e-i=3t+1-i` and `q-j=2t+1-j`.  The `J(beta,alpha)` terms, the polynomials
`z,B,A,h`, the monic carry operation, the target `c*gamma`, and the
Rabinowitsch equation `T*c-1` are `t`-independent.  The changing ranges and
the four regimes of `S_i(t)` are a separate, combinatorial dependence on
`t`.  In particular, the generated ideal itself has no `1/(3t+1)` or other
rational function of `t`; no denominator saturation is needed merely to
state it.

**MEASURED (`t=2,3,4`).**  The coefficient-equation counts are 37, 51, 65,
matching `14t+9`, and the exact level histograms match

```text
h=0:                 7
h=1,...,t:           6 each
h=t+1,...,2t:        5 each
h=2t+1,...,3t+1:     2 each
h=3t+2,...,4t+1:     1 each.
```

This measured affine pattern is useful organization; the scripts, rather
than an extrapolated count, remain the authority at each fixed `t`.

## 3. Two useful indexings

### Low `h`-tail (literally stable)

Rename the bottom coefficients by their `h` powers:

```text
p_s = alpha_(e-s),       r_u = beta_(q-u).
```

Ignoring the distant leading monomials until they enter the chosen level,
the raw tail equation becomes

```text
R_k^tail = sum_(u+s=k) J(r_u,p_s)
         + sum_(u+s=k+1)
             [s p_s J(r_u,h) + u r_u J(h,p_s)].
```

This formula and the monic carry are entirely `t`-independent.  A final
level `H` uses tail coefficients only through power `H+1`.  Their coefficient
spaces have stabilized when `t >= H+1`; consequently the canonically renamed
level-`H` generators are then identical, not merely specializations of a
rational formula.

`tail_band_analysis.py` verifies:

```text
t=2 versus t=3: levels 0,1 identical; first difference H=2;
t=3 versus t=4: levels 0,1,2 identical; first difference H=3.
```

At the first difference between `t` and `t+1`, the later chart has precisely
the newly allowed boundary coordinates

```text
p_(t+1),B   and   r_(t+1),A.
```

Thus for `t=2` versus `t=3` the first differing low band is `h=2`, through
`p_3`'s `B` coordinate and `r_3`'s `A` coordinate.  This is a statement about
the generated systems.  It is not yet a statement about which generators
occur in a unit-ideal lift (none was supplied).

### High side (affine recurrence)

The highest equation is at `h^(4t+1)`.  If `a_1` and `b_1` denote the `A`
coordinates of `alpha_(t+1)` and `beta_(t+1)`, its sole equation is

```text
(2t+1)*a_1 - (3t+1)*b_1 = 0.
```

Writing `a_2,b_2` for the next `A` coordinates and `u_1` for the scalar
coordinate of `alpha_1`, the next high equation is

```text
(2t+1)*a_2 - (3t+1)*b_2 - 3t*u_1*b_1
- b4*((2t+1)*a_1-(3t+1)*b_1) = 0.
```

These display the possible recurrence and its affine `t` dependence.  Over
`Q(t)`, either `2t+1` or `3t+1` can be used as a pivot; neither vanishes at a
positive integral `t`.  But this only eliminates high coefficients.  It is
not a unit certificate, and the number of bands connecting the high side to
the Jacobian tail grows with `t`.

There is one high-side scalar remainder equation at each normalized offset
`L=0,...,t-1` from `4t+1`; a second coordinate appears at `L=t`.  Hence the
first structural difference between the `t=2` and `t=3` high systems is the
third band (`L=2`): at `t=2` it has two equations, while at `t=3` it is still
the one-equation `A` recurrence.  The measured counts are

```text
t=2: [1,1,2]       for L=0,1,2,
t=3: [1,1,1,2]     for L=0,1,2,3,
t=4: [1,1,1,1,2]   for L=0,1,2,3,4.
```

## 4. Exact consistency witness for every fixed low subsystem

The requested two-/three-band symbolic obstruction does not occur.  There is
a stronger exact witness.  Set

```text
b1=b2=b3=b4=0,
h=pi^3(pi-gamma), B=pi(pi-gamma), z=pi-gamma,
Q=h^q+B,
P=h^e+gamma+2z = h^e+2pi-gamma,
c=-1,
```

and set every other chart coordinate to zero.  This obeys all three gauges
and all displayed coefficient spaces.  Direct differentiation gives

```text
J(B,2pi-gamma) = -gamma,
J(h,2pi-gamma) = pi^2(2pi-3gamma),
J(B,h) = -2h,

J(Q,P) = -gamma
       + q*pi^2(2pi-3gamma)*h^(q-1)
       - 2e*h^e.
```

Therefore the `h=0` target equation is satisfied and every level
`1,...,q-2=2t-1` vanishes.  The only residual tagged equations at the tested
values are

```text
t=2: h=4: (-3q)*gamma*pi^2 + (2q)*pi^3; h=7: -2e,
t=3: h=6: (-3q)*gamma*pi^2 + (2q)*pi^3; h=10: -2e,
t=4: h=8: (-3q)*gamma*pi^2 + (2q)*pi^3; h=13: -2e.
```

So the bottom two or three bands are consistent, and indeed no fixed finite
low-tail cutoff can be uniformly inconsistent: for any fixed `H`, the same
point satisfies levels `0,...,H` once `2t-1 >= H`.

The same point also defeats any proposed test consisting of `h=0` plus a
fixed number `K` of highest bands for all sufficiently large `t`; its only
defects are at the moving middle levels `2t` and `3t+1`.  In particular it
satisfies `h=0` plus the highest three bands over `Q(t)` in the stable range
`t>=3`.  Thus a fixed two-/three-top-band unit ideal is impossible.  This is
only a subsystem point, not a polynomial pair with `J=-gamma`.

## 5. Certificate trace and the `pi^-1` tail

**MEASURED LIMIT.**  The charged `t=2` certificate records the input order,
37 equations plus `T*c-1`, and reduced basis `[1]`, but no Singular protocol,
lift matrix, or unit representation.  A reduced basis `[1]` does not reveal
which original band generators its reductions used.  Consequently the
literal first generator used by the `t=2` (or `t=3`) certificate remains
`OPEN[CERTIFICATE-SUPPORT]`.  What is established is the first band at which
the systems can differ: low level `H=2`; independently, the first differing
normalized high offset is also `L=2`, for `t=2` versus `t=3`.

The present order chart is polynomial by construction.  It contains no
separate `pi^-1`-tail cancellation equations.  The charged report explicitly
types the Laurent ring map needed for the tuple coefficient as
`OPEN[DESCENT-ANCHOR]` and gives a future constant-pivot series-reversion
recipe (charged report lines 542-602).  The other charged report describes
`pi^-1` cancellation as additional Appendix-II data, not as a proved generic
recurrence (its lines 520-556).  Importing the printed cancellation identities
from a different row would be an analogy, not a proof for this family.

Accordingly, the exact banded identity supplies a uniform local recurrence,
but neither it nor the unavailable Laurent tail bridge currently supplies a
uniform unit certificate.

## 6. Typed conclusion

- **PROVED-HERE:** the denominator-free gauged family schema; the critical
  generic gauge `alpha_t=0`; literal low-band stabilization; the explicit
  subsystem witness; and failure of every fixed low-tail or fixed-high-band
  obstruction for sufficiently large `t`.
- **MEASURED:** exact agreement with the frozen `t=2` generator and the new
  `t=3,t=4` drivers; counts and band comparisons listed above.
- **PARTIAL:** the high equations form an affine-in-`t` elimination recurrence,
  but it has not been closed across the growing middle interval.
- **OPEN[T-UNIFORM-COEFFICIENT]:** no uniform-in-`t` unit certificate is in
  hand from these bands.
- **OPEN[CERTIFICATE-SUPPORT]:** no trace/lift identifies the first original
  generator used in either fixed-`t` unit representation.
- No representative, actual-pair, attainment, exit-price, or uniform theorem
  claim is made.  No `charge_basis` line is due.

## Reproduction

```bash
python3 box/k16t3-20260903/generic/generic_order_system.py --t 2
python3 box/k16t3-20260903/generic/generic_order_system.py --t 3
python3 box/k16t3-20260903/generic/generic_order_system.py --t 4
python3 box/k16t3-20260903/generic/tail_band_analysis.py
```
