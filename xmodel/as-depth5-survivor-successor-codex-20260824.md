# AS `p=3` depth-five cap-eight survivor — independent successor

Date: 2026-08-24  
Basis commit: `c327bdc8d02472feba42573760325099f34b8cdf`  
Status: **INDEPENDENT EXACT RESEARCH / NONCANONICAL**  
Strongest result: **the displayed depth-five gauge is exact, but is terminal: it has no symplectic lift to depth six at any cap**

## 1. Scope and verdict

All arithmetic below is over the integers followed by exact reduction. I read the committed wild-symplectic gate and review, bounded-polar gate and review, depth-four growth gate and review, and the depth-four replay and independent checker. I reran the latter two without modification. No producer code was imported into the new checker, no repository case was edited, and no AWS or network service was used.

The supplied checkpoint is correct. It gives a depth-five equal-cap survivor with cap eight, improving the cotangent control's cap nine at that depth. Its mechanism is a filtered boundary-Wronskian cancellation, not a random coefficient coincidence. However, the same gauge has a nonzero Cartier obstruction in its next determinant carry. Consequently it cannot be lifted from `mod 243` to `mod 729`, even with arbitrarily large fresh digit supports. Thus it does not itself start an iterable family.

The true depth-five minimum is narrowed, but not decided:

```text
7 <= min D for B_(3,5)(D,D) <= 8.
```

The lower bound is reduction to the reviewed depth-four minimum seven; the upper bound is the verified survivor here. I obtained no certificate-grade elimination of cap seven and do not claim that eight is minimal.

At depth six the standard cotangent point gives cap eleven. I found no cap-eight, cap-nine, or cap-ten lift of the displayed motif; more strongly, no lift of that exact residue-class gauge exists at any cap. This does not exclude other depth-five points from lifting with cap at most ten.

## 2. Independent exact verification

Put

```text
c = x^5(1-y),
d = x^4(1+y+y^2),
f = x^4(7y+5y^2),
A = x+9c,
B = y+9d+27f.
```

Thus the stated coefficients of `B` are `9+27*7=198` on `x^4 y` and `9+27*5=144` on `x^4 y^2`. With

```text
S5(T)=1+3T^2+9T^4+27T^6+81T^8,
P=A-A^3,
Q=B S5(A),
```

direct integer expansion and coefficientwise reduction modulo `243` gives exactly

```text
P = 27*x^7*y + 216*x^7 + 234*x^5*y + 9*x^5 + 242*x^3 + x,

Q = 81*x^8 + 135*x^6*y^2 + 189*x^6*y + 27*x^6
    + 144*x^4*y^2 + 207*x^4*y + 9*x^4 + 3*x^2*y + y.
```

The reduced total degrees are

```text
deg(A)=deg(B)=6,        deg(P)=deg(Q)=8.
```

The same computation gives

```text
det J(A,B) = 1 (mod 243),
det J(P,Q) = det J(A,B) = 1 (mod 243),
(P,Q) = (x-x^3,y) (mod 3).
```

The equality of determinants also follows invariantly from

```text
d(A-A^3) = (1-3A^2)dA,
d(B S5(A)) = S5(A)dB + B S5'(A)dA
```

and `(1-3A^2)S5(A)=1-243A^10`: the second summand wedges to zero.

## 3. Structural cancellation

Write `u=1-y` and `v=1+y+y^2`, so `c=x^5u` and `d=x^4v`. Modulo three,

```text
v=u^2,             v'=u.
```

This is the organizing identity.

### 3.1 The top `Q` carry

Modulo `243`, expansion at the first active gauge digit gives

```text
S5(x+9c)
 = 1+3x^2+9x^4+27x^6+81x^8
   +54xc+81*4x^3c.
```

The part of `Q` at coefficient `81` that can cross degree eight is

```text
x^8 y + x^4 d + 4x^3 c y
= x^8 (y+v+4uy).
```

In `F_3[y]`, using `4=1` and the definitions of `u,v`,

```text
y+v+uy = y+(1+y+y^2)+y(1-y)=1.
```

Hence all degree-nine boundary terms cancel and the boundary carry reduces to the allowed monomial `x^8`. This explains both the cap drop from nine to eight and the surviving coefficient `81*x^8`. It is a filtered boundary identity: the top cotangent term, the transported `d` term, and the linearized substitution of `c` form one boundary polynomial.

### 3.2 Divisibility of the bracket

For separated weighted forms `x^m u(y)` and `x^(m-1)v(y)`, their Poisson bracket is the boundary Wronskian

```text
{x^m u, x^(m-1)v}
 = x^(2m-2) (m u v'-(m-1)u'v).
```

Here `m=5`, `u'=-1`, `v=u^2`, and `v'=u` modulo three. Therefore

```text
5uv'-4u'v = 2u^2+v = 3v = 0 (mod 3).
```

Equivalently, over the integers,

```text
{c,d} = -3*x^8*(2y^2-3y-3).
```

Thus `{c,d}` is divisible by three for structural Wronskian reasons. This is the Hamiltonian part of the motif.

### 3.3 The correction `f`

The first divergence is not zero, but is divisible by three:

```text
c_x+d_y = 3h,          h=x^4(2-y).
```

Expanding the gauge determinant gives the exact filtered expression

```text
det J(A,B)
 = 1+9(c_x+d_y)+27f_y+81{c,d}+243{c,f}.
```

After division by `27`, the remaining condition modulo nine is

```text
h+f_y+3{c,d} = 0 (mod 9).
```

For `f=x^4(7y+5y^2)`, direct calculation gives

```text
h+f_y+3{c,d}
 = -9*x^4*(2*x^4*y^2-3*x^4*y-3*x^4-y-1).
```

So `f` is precisely a primitive for the residual divided-divergence carry, with the bracket correction included. This supplies an invariant construction recipe at this one stage:

1. choose adjacent weighted boundary forms `x^m u`, `x^(m-1)v` with `v=u^2` in `F_3` so their Wronskian bracket is divisible by three;
2. impose the boundary identity that kills the over-cap composition carry;
3. integrate the remaining divided divergence to the next gauge digit.

The recipe is not indefinitely iterable: its next Cartier class is nonzero, as follows.

## 4. Exact depth-six obstruction for this motif

Every lift of this exact gauge has the form

```text
A' = A+243e,
B' = B+243g
```

modulo `729`, for arbitrary polynomials `e,g` over `F_3` (with no degree restriction needed for the obstruction). Put

```text
R=(det J(A,B)-1)/243.
```

The exact checker obtains

```text
R = -x^4*(32*x^4*y^2-46*x^4*y-38*x^4-y-1),

R mod 3
  = x^8*y^2+x^8*y+2*x^8+x^4*y+x^4.
```

Linearization modulo `729` is

```text
det J(A',B')
 = 1+243(R+e_x+g_y) (mod 729),
```

because the base gauge is the identity modulo three. In characteristic three, the coefficient of every monomial

```text
x^(3a+2)y^(3b+2)
```

in a divergence `e_x+g_y` is zero: its only possible antiderivatives have multipliers `3a+3` or `3b+3`. But `[x^8 y^2]R=1`. Hence

```text
R not in im(partial_x,partial_y),
```

and no `e,g` exist. This is a one-row Cartier-cokernel certificate, proving:

```text
The displayed (A,B) modulo 243 has no determinant-one lift modulo 729,
at cap 8, 9, 10, or any other finite cap.
```

There is also a composition-side warning. If `q5` denotes the canonical reduction of `B*S5(A)` modulo `243`, then

```text
T=(B*S6(A)-q5)/243 mod 3
```

has support

```text
2*x^10*y^3 + 2*x^10*y^2 + x^8*y^2 + x^6*y^2 + 2*x^6*y.
```

Fresh `A` corrections cannot change this digit because `S6'(A)` is divisible by three; fresh `B` corrections contribute `g`. In particular the unmodified motif already has an immutable over-cap term of degree thirteen before imposing the determinant. The determinant Cartier row is stronger: it rules out the lift even when `g` is allowed to reach that degree.

## 5. Minimum and depth-six controls

Reduction from depth five to depth four preserves the equal cap. The reviewed exact depth-four minimum therefore gives `D>=7`. The verified point gives `D<=8`. A cap-seven decision requires eliminating the full nonlinear depth-five base system (or decomposing its depth-four liftable components); testing only the displayed point cannot do that. No such finite solve was completed here, so the exact minimum remains `{7,8}`.

Depth six is nevertheless nonempty at cap eleven via the cotangent truncation

```text
P6 = x-x^3,
Q6 = y+3*x^2*y+9*x^4*y+27*x^6*y+81*x^8*y+243*x^10*y
     (mod 729).
```

Indeed

```text
det J(P6,Q6)=1-729*x^12 = 1 (mod 729),
```

and `deg Q6=11`. This is an exact positive control, not a claim that eleven is minimal. The results established here are therefore

```text
depth 5: minimum is 7 or 8; explicit cap-8 survivor;
depth 6: explicit cap-11 survivor;
displayed depth-5 motif: no depth-6 lift at any cap.
```

## 6. Growth and recurrence assessment

The known upper bounds at depths `2,3,4,5,6` are

```text
3, 5, 7, 8, 11.
```

Only the depth-five entry improves on `2n-1`; it is terminal by Section 4. I found no recurrence, sublinear family, or stepped unbounded family from this motif. The only all-depth construction retained is the cotangent family with cap `2n-1` at `p=3`.

This is consistent with the reviewed polar theorem: every fixed cap eventually fails. A future slower-growth construction must allow the depth-five representative to vary inside its solution space so that its next Cartier class vanishes; extending this fixed point is impossible.

## 7. Reproducibility

The independent script and its captured output are outside the repository:

```text
/tmp/as_depth5_verify.py
sha256 dfe50ab61b3b4233568dfb1e86b5b84598f44cd71421239eba7e2429ae1cab92

/tmp/as_depth5_verify.stdout.txt
sha256 db7bc42f85501248923a4c56126a1830f7c92e832b61ae5870f10bc2daa857c0
```

Reproduce with:

```bash
cd /Users/dc/code/math/jc2
uv run --offline --no-project --with sympy==1.14.0 \
  python /tmp/as_depth5_verify.py | tee /tmp/as_depth5_verify.stdout.txt
sha256sum /tmp/as_depth5_verify.py /tmp/as_depth5_verify.stdout.txt
```

Regression controls were rerun with:

```bash
uv run --offline --no-project --with sympy==1.14.0 \
  python cases/as_gauge_growth_p3_depth4_20260824/replay.py \
  > /tmp/as_depth4_replay.stdout
uv run --offline --no-project --with sympy==1.14.0 \
  python cases/as_gauge_growth_p3_depth4_20260824/independent_check.py \
  > /tmp/as_depth4_checker.stdout
```

Both passed, including the replay's exact depth-four minimum seven and the independent checker's unit obstruction for caps five and six.

## 8. Precise next discriminator

The next certificate-grade discriminator is not another lift attempt on this point. It is the cap-seven depth-five base variety with the next Cartier row attached:

```text
1. solve B_(3,5)(7,7) exactly on total-degree simplices;
2. if nonempty, decompose its solutions by the coefficient of
   x^(3a+2)y^(3b+2) in the divided depth-six Jacobian carry;
3. retain only components on which every such Cartier coefficient vanishes;
4. solve the resulting linear fresh-digit system at caps 8, 9, and 10,
   reconstructing P=A-A^3 and Q=B*S6(A) over the integers modulo 729.
```

An inconsistency certificate in step 1 proves the depth-five minimum is eight. A cap-seven point proves it is seven. A liftable component surviving steps 2–4 is the first evidence that the cap-eight anomaly belongs to a recurrence rather than to an isolated terminal point.

## 9. Firewall

This report proves only finite congruence statements and a terminal obstruction for one exact depth-five residue class. It does not construct a characteristic-zero polynomial lift, does not rule one out, does not settle `A_infinity`, does not provide rational or polynomial deck descent, and does not decide JC2. The exterior polar divisor theorem still forbids any fixed-cap all-depth conclusion; nothing here weakens that theorem.
