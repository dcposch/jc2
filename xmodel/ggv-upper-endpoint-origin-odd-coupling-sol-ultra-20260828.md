# Upper endpoint origin equation: the exact odd-fiber coupling

Date: 2026-08-28  
Author: Sol Ultra / coordinator  
Status: **EXACT PROVISIONAL LEMMA; INDEPENDENT COMPOSITION RUNNING**

## 1. Result

For the authoritative `8_28` upper-chart raw windows, the constant-in-`X`
coefficient of the endpoint row is exactly

```text
D22[X0]=F11[X1]*G11[X0]-F7[X0]*G15[X1].               (1)
```

Since the target is `D22=1`, every endpoint point must satisfy

```text
F11[X1]*G11[X0]-F7[X0]*G15[X1]=1.                    (2)
```

These four slots are precisely the original-coordinate linear coefficients:

```text
P_x(0)=f_1_0=F11[X1],     P_y(0)=f_0_1=F7[X0],
Q_x(0)=g_1_0=G15[X1],     Q_y(0)=g_0_1=G11[X0].
```

Thus `(2)` is literally `J(P,Q)(0)=1`.

In particular, the all-odd-weight section is empty at the raw endpoint.  It
is not a survivor merely because every odd de Rham gate vanishes there.
This supplies the smallest exact coupling between the reviewed q5--q15 odd
fiber and the endpoint target.

## 2. Literal-window derivation

The raw recurrence is

```text
D_n=sum_(i+j=n) ((12-j)F_i'G_j+(i-8)F_iG_j').         (3)
```

To contribute to `[X0]`, the differentiated polynomial must use its `X1`
slot and the other polynomial its `X0` slot.  At `i+j=22`, the authoritative
floors leave only:

```text
(i,j)=(11,11): (12-j)F11'G11 = +F11[X1]G11[X0],
(i,j)=(7,15):  (i-8)F7G15'  = -F7[X0]G15[X1].
```

The apparent neighbouring pairs are structural zeros: `(10,12)` has
`12-j=0`, while `(8,14)` has `i-8=0`.  All other pairs lack one of the
required literal `X0/X1` slots.  This proves `(1)` without a specialization,
division, radical step, or q-gate.

## 3. Parity interpretation

In the upper chart `X=x*y^3`, `t=1/y`, a weight-`w` first-component slot
`X^i` represents

```text
x^i y^(8+3i-w),
```

and a second-component slot represents `x^i y^(12+3i-w)`.  Its ordinary
total-degree parity is therefore `w mod 2`.  If all odd weights vanish, both
`P` and `Q` contain only even-total-degree monomials, are invariant under
`(x,y)->(-x,-y)`, and have zero gradients at the origin.  Equation `(1)`
then gives `D22[X0]=0`, contradicting the target.

This corrects the tempting but false inference from the reviewed q15 packet
that the all-odd-zero section remains available after the raw endpoint is
restored.  The q15 dimension theorem itself is unchanged: it concerns the
q-gate fiber before `(2)` is imposed.

## 4. Reproducibility

Checker:

```text
cases/ggv_8_28_upper_endpoint_origin_odd_coupling_20260828/
  verify_origin_odd_coupling.py
```

SHA-256:

```text
f23a6d959dc9a8854f051c16a1fe287dea91d5b66b01a63198a64715c08c04c8
```

Replay marker:

```text
PASS_EXACT_UPPER_ENDPOINT_ORIGIN_ODD_COUPLING
```

The checker pins the authoritative raw-slot input at SHA-256
`28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876`,
verifies the chart exponent/parity formula for every raw slot, enumerates
all possible D22 constant-term contributions, and checks the ordinary linear
Jacobian sign.

## 5. Next exact target and scope

On the `lambda=0`, `c2!=0`, exact-`D=0` branch, reconstruct `G11[X0]` and
`G15[X1]` from the complete ten-mode characteristic and intersect `(2)`
with the reviewed q5--q15 fiber.  This is smaller and sharper than either a
q17-only calculation or the 15-coordinate even four-root resultant.

The lemma alone does not show that the intersection is empty.  It proves no
endpoint exclusion, other-branch result, Keller theorem, or JC2.
