# GCD3 `(6,9)` mixed-cube-factor adversarial control

**Producer-internal verdict: `h=x^3(x^3-1)` IS NONCUBE IN `k(x)`;
THE FACTOR `x^3` DOES NOT CREATE A THIRD KUMMER BRANCH; THE EXACT TOP ROW
DERIVES `delta=0`; BOTH ORIGINAL BOUNDARY VALUES REMAIN CHARGED; AND THE
DATA LAND IN THE REVIEWED ALIGNED LOWER-PFAFFIAN INPUT.`**

- Date: 2026-08-24
- Status: bounded producer-internal control, pending independent review
- Field for the calculation: algebraically closed `k`, characteristic zero,
  with a primitive cube root `omega`
- Frozen or canonical files edited: none
- New theorem claimed: none; the reviewed first-gate and lower-Pfaffian
  theorems are consumed at their exact scopes

This is an adversarial specialization of the noncube handoff in the frozen
coverage composition.  It targets the proposed “hybrid” failure mode in
which a polynomial cube factor might conceal a third branch.

## 1. Exact divisor and Kummer class

Put

```text
F=k(x),
h=x^3(x^3-1)=x^6-x^3,
q=x^3-1=(x-1)(x-omega)(x-omega^2).
```

The complete divisor data on `P^1_k` are

```text
v_0(h)=3,
v_1(h)=v_omega(h)=v_(omega^2)(h)=1,
v_infinity(h)=-6.                                   (1.1)
```

Indeed, at a cube root `a` of one,

```text
h'(a)=3a^2(2a^3-1)=3a^2 != 0.
```

Every valuation of a rational cube is divisible by three.  The simple
valuation at `x=1` already proves

```text
h notin F^3.                                         (1.2)
```

Moreover

```text
[h]=[q] in F*/F*^3                                  (1.3)
```

because `h=x^3q`.  If `t^3=q` and `s=xt`, then

```text
s^3=h,
F(s)=F(t),                 t=s/x.                    (1.4)
```

Thus `T^3-q` and `T^3-h` define the same nontrivial cyclic cubic Kummer
extension.  The cube factor changes only the generator.  In particular it
creates no extra field, component, or third case between “cube” and
“noncube.”  More generally, `h=g^3q` always gives
`F(h^(1/3))=F(q^(1/3))` by the same two inclusions.

At `x=0`, the order-three zero is Kummer-class neutral and causes no new
global branch; the genuine ramification is detected by the simple zeros of
`q`.  The historical input is also exact:

```text
H=deg(h)=6,                  3|H.                    (1.5)
```

## 2. The top row derives `delta=0`

Start with the reviewed actual-degree leading data

```text
a6=h^2=s^6,             b9=h^3=s^9,
a5=s^5 A,               b8=s^8 B.
```

Writing `u=s'/s`, the four contributions to the `y^13` Jacobian row, after
factoring `s^14`, are

```text
 8a6'b8     ->  48uB,
 9a5'b9     ->   9A'+45uA,
-6a6b8'     ->  -6B'-48uB,
-5a5b9'     ->       -45uA.
```

All logarithmic-derivative terms cancel, leaving exactly

```text
s^14(9A'-6B')=0.
```

Therefore

```text
delta=3A-2B
```

has zero derivative.  The constant field of the algebraic function field
`L=F(t)` is `k`: constants are algebraic over the algebraically closed
constant field `k`.  Hence `delta in k`.

Let `sigma(t)=omega t`.  Since `s=xt` and `x in F` is fixed,
`sigma(s)=omega s`.  Consequently

```text
sigma(A)=omega^(-5)A=omega A,
sigma(B)=omega^(-8)B=omega B,
sigma(delta)=omega delta.                             (2.1)
```

But `delta in k` is fixed by `sigma`.  Thus

```text
(omega-1)delta=0.
```

There is no zero-divisor or hidden localization:

```text
(omega-1)^(-1)=-(omega+2)/3
```

in `Q[omega]/(omega^2+omega+1)`.  It follows that

```text
delta=0.                                             (2.2)
```

This is derived from the top row and weight one; it is not assumed from the
presence of the cube factor.

## 3. Exact aligned high-row landing

Set `r=A/6` and `z=sy+r`.  Equation (2.2) makes the two depressions align:
the `z^5` row of the first coordinate and `z^8` row of the second both
vanish.  The reviewed eight-row integration gives

```text
f=z^6+a4z^4+a3z^3+a2z^2+a1z+a0,
g=g0(a0,...,a4)+kappa(z^3+(a4/2)z+a3/2).
```

The Kummer weight of a `z^j` integration constant is `-j mod 3`.  Therefore

```text
c7=c5=c4=c2=c1=0,                                   (3.1)
```

while `c6,c3,c0` have weight zero.  The legal target operations remove
`c6` by `Q -> Q-c6P` and `c0` by second-target translation.  The remaining
`c3=kappa` may be retained in the explicitly pinned first-target-constant
chart used by the reviewed lower-Pfaffian theorem.  Equivalently, the
reviewed erratum gauges it to zero by `P -> P+2kappa/3`; the invariant
`C=kappa^2+mu` and the lower exclusion are unchanged.  No cube-core
weight-unforced constant is imported.

The input is now exactly

```text
F=k(x),
L=F(s), s^3=h in k[x],
L/F nontrivial cubic Kummer,
3|deg(h),
aligned f,g as above,
J_(x,y)=s(f_x g_z-f_z g_x),
terminal row [z^0]D=j/s.
```

These are precisely the hypotheses named by the confirmed aligned
lower-Pfaffian review.

## 4. Both boundary values remain charged

The rational depression is not treated as a polynomial source
automorphism.  At the original section `y=0`, one has `z=r` and the exact
provenance identities

```text
f(x,r)=P(x,0) in k[x],
g(x,r)=Q(x,0) in k[x].                               (4.1)
```

They need not vanish.  The target gauges used above transform the pair to

```text
P(x,0),
Q(x,0)-c6 P(x,0)-c0,
```

and an optional first-target translation changes the first value to
`P(x,0)+q0`.  Both remain polynomials, actual degrees stay `(6,9)`, and the
Jacobian is unchanged.  Thus neither boundary is dropped.  The aligned
lower-Pfaffian proof happens not to use a boundary reduction; carrying (4.1)
inertly is therefore sufficient and avoids the reviewed full-cubic
`TYPE-FAIL`.

## 5. Result and residual scope

No mixed-factor gap was found.  The factor `x^3` is invisible in the Kummer
class and generator field, while the cube-free factor supplies simple
valuations that force the noncube route.  All required aligned inputs are
present, and both original boundary values remain charged.

The smallest remaining dependency is not a new branch: this control consumes
the already reviewed eight-high-row integration and aligned lower-Pfaffian
exclusion rather than reproving them.  It is one exact specialization plus a
general field identity, not an independent hostile review of the frozen
composition and not a generic primary-decomposition theorem.

Run:

```sh
python3 cases/gcd3_69_mixed_cube_factor_control_20260824/replay.py
```

Expected terminal markers:

```text
PASS-GCD3-69-MIXED-CUBE-FACTOR-CONTROL
h_noncube=valuation_at_each_root_of_x3_minus_1_is_1
cube_factor=KUMMER-CLASS-NEUTRAL
delta=DERIVED-ZERO-BY-WEIGHT-ONE
boundaries=BOTH-CHARGED
landing=REVIEWED-ALIGNED-LOWER-PFAFFIAN-INPUT
payload_sha256=81852acbee47204e6ade03852a7f1ace57d0a217a3c5d0f846498776db219b32
```
