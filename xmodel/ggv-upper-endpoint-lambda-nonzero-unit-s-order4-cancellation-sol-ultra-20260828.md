# Lambda-nonzero unit-S face: the D12 lifts cancel every order-four pole

Date: 2026-08-28  
Lane: Sol Ultra coordinator, exact desk theorem  
Status: **PROVISIONAL; INDEPENDENT HOSTILE REVIEW REQUIRED**

## Verdict

On the reviewed active-`c2`, exact-`D=0` successor, the two D12 root lifts
strengthen the earlier first-correction lemma enough to cancel every
potential face pole at relative epsilon order four.  Thus the unit-`S`
fractional-pole test is regular through order four, not merely through order
three.  The first possible discriminator must occur later or use raw windows
rather than face polynomiality alone.

This is a local characteristic theorem.  It does not prove the existence of a
raw pair, any higher-order polynomiality, endpoint emptiness, a Keller theorem,
or JC2.

## 1. Abstract order-four identity

At a simple root `alpha` of `A`, put `epsilon=X-alpha`, `t=epsilon*tau`, and

```text
L=A'(alpha)+S(alpha)*tau/4.
```

Write the normalized local expansion initially in the weaker form

```text
epsilon^-4 F = L^4 + epsilon*L^2*K
                       + epsilon^2*B
                       + epsilon^3*C
                       + epsilon^4*D + O(epsilon^5).
```

In the complete characteristic

```text
G=F^(3/2)+sum_(m=2,4,...,20) c_m t^m F^((12-m)/8),
```

only the modes `m=0,2,4,6,8` can enter relative order four.  Exact binomial
expansion gives that coefficient as

```text
(3/2)L^2 D + (3/4)K C
+ (3/128)L^-2 (4B-K^2)^2
+ c2*tau^2[(5/4)L C
            +(5/128)L^-1 K(8B-K^2)]
+ c4*tau^4 B
+ (3/4)c6*tau^6 L K
+ c8*tau^8 L^2.                                      (1)
```

This exhibits the entire possible polar part, including cancellation between
the partitions of the pure and `c2` modes.  In the weaker abstract setting,
regularity would force `L|K` and `L|B`.

## 2. The reviewed D12 lifts make both conditions automatic

Use the exact prefix formulas

```text
F0=A^4,
F1=A^3 S,
F2=(3/8)A^2 S^2-(1/8)A^3 Q,
F3=A S^3/16+A^2(U-SQ/2)/8,
F4=(S^2-AQ)^2/256+A S U/16,
F5=(A P1+2S^2 U)/256,
```

which follow from `S^2-2Z=AQ`, exact `D=R-4SU=0`, and `P=A P1`.  The
reviewed paired D11/D12 repair also gives, at every root,

```text
QS+4U=0,
2048F6-2SP1-4QSU-8U^2=0.                             (2)
```

Expand

```text
A=epsilon(a+b*epsilon+...),
S=s+h*epsilon+...,
Q=q+r*epsilon+...,
U=u+v*epsilon+...,
P1=p+...,
F6=w+....
```

The first equation in (2) says `u=-s*q/4`.  Direct substitution in the
literal `F0,...,F5` formulas gives

```text
[epsilon^1](epsilon^-4 F)
 = L^3(4(b+h*tau/4)-q*tau^2/8).                       (3)
```

Thus the first correction is in `L^3`, one power stronger than the already
reviewed `L^2` statement.

For the second correction, evaluation at the unique face root
`tau0=-4a/s` cancels every derivative term and leaves

```text
B(tau0)=(a^6/s^6)(s^2 q^2-4s p+4096w).                (4)
```

The second equation in (2), together with `u=-s*q/4`, is exactly

```text
4096w=4s p-s^2 q^2.                                   (5)
```

Hence `B(tau0)=0`, so `L|B`.  Put the two strengthened corrections in the
form

```text
epsilon^-4 F=L^4+epsilon*L^3 J+epsilon^2*L H+O(epsilon^3).
```

Substitution in (1) leaves no negative power of `L` in any mode.  Therefore
the complete relative-order-four characteristic coefficient is regular.

The assumptions `S(alpha)!=0` and `A'(alpha)!=0` make `tau0` well defined;
they hold on the lambda-nonzero q1 branch because
`S(alpha)=3lambda*A'(alpha)` and `A` is squarefree.

## 3. Reproduction and controls

Run

```text
python3 cases/ggv_8_28_upper_endpoint_lambda_nonzero_unit_s_order4_cancellation_20260828/verify_unit_s_order4_cancellation.py
```

Expected marker:

```text
PASS_EXACT_UNIT_S_ORDER4_CANCELLATION
```

The checker is a standard-library exact sparse Laurent calculation.  It
reconstructs (1), verifies (3), verifies the zero remainder (4)--(5), and
then expands every mode born by order four.  Mutating either root lift leaves
a detected nonzero remainder.  It imports no producer code and performs no
heavy local algebra.

## 4. Scope and next discriminator

The theorem consumes the reviewed D12 lifts; it is not a statement on the
earlier unit-`S` face before those rows.  It also does not say that arbitrary
higher coefficients are polynomial or satisfy their raw degree windows.

The clean successor is to recompute the mode census with the stronger
divisibilities `f1 in (L^3)` and `f2 in (L)`, then isolate the first remaining
polar residue (provisionally relative order five) before launching another
large raw compiler.
