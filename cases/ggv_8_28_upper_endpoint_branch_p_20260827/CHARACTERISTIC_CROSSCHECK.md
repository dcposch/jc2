# Characteristic cross-check firewall

This note is diagnostic only.  The literal raw ideal with SHA-256
`ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0`
remains authoritative.

For `F0=A^4` and a formal coefficient sequence `y=F^alpha`, the safe
weight recurrence is

```text
n A^4 y_n = sum_(1<=i<=min(n,14)) (((alpha+1)i-n) F_i y_(n-i)).
```

The forced rational continuation has

```text
g_n = (F^(3/2))_n
    + sum_(m even, 4<=m<=min(n,20)) k_m
        (F^((12-m)/8))_(n-m).
```

All even rational integration constants through `k20` must be carried by
any characteristic compiler.  Only `k4,k6,k8,k10,k12` give free polynomial
raw modes in the frozen windows.  At `m=14,16,18,20`, the rational kernel
directions are respectively `A^-1,A^-2,A^-3,A^-4`; the restricted
polynomial `G_m` windows have zero kernel, so pole cancellation uniquely
forces those auxiliary constants.  Saying “no polynomial mode after 12”
does not license dropping them from a rational continuation calculation.

For the affine target, the endpoint-transfer diagnostic is

```text
g22 = (X^5/5-X+c)/(8 A^5),
L22(g22)=-1,
D_raw,22=-L22(g22)=1.
```

A characteristic certificate must serialize every cleared recurrence,
every division quotient/remainder enforcing the exact raw window, the four
forced constants `k14,k16,k18,k20`, and a final literal raw replay.  No
active solver lane in this case uses a truncated characteristic schedule.

## Reviewed uniform first defects (2026-08-28)

On characteristic-zero field points of the complete fixed fixture, the
first two polar-numerator identities are

```text
A^2 (F^(3/2))_7 = -(3/1024) T^2                         (mod A),
A^2 (F^(3/2))_8 =  (3/8)(F4-V/16-Z^2/64)^2             (mod A),
```

where the second line is after the first conclusion `T=A*V`.  Available
characteristic modes do not cancel these order-two poles; exactly

```text
(F^(3/4))_2 = 3/(32A) + (3/16)AZ.
```

Hence `D7=0` gives `A|T`, and then `D8=0` gives
`A|(F4-V/16-Z^2/64)`, field-radically.  The corrected operator sign is

```text
L7((F^(3/2))_7) = -(27/256) A A' T^2   (mod A^2),
D7_raw           = +(27/256) A A' T^2   (mod A^2).
```

Producer/audit hashes are `f6950b25...` / `d2ab35e1...`.  The result is not
scheme divisibility or endpoint emptiness.  Every successor defect must
serialize both its Laurent numerator and its literal raw-row image, including
all modes already born.

## Reviewed D8 mode kill and D9 defect (2026-08-28)

Continuing from the two reviewed divisibilities above, the complete born-mode
schedule at weights eight and nine is `c4,c6,c8`.  The same D8 row additionally
has

```text
polar(g8)=3*c6/(32*A),
D8_raw=-(9/4)*c6*A^2*A'                         (mod A^3),
```

so polynomiality forces the scalar `c6=0`.  Only after this mode kill is the
weight-nine negative part

```text
-3*W^2/(16*A^2)+(3*F5*W/4-3*V*W*Z/256)/A,
D9_raw=(21/4)*A*A'*W^2                          (mod A^2),
```

and hence `A|W` on characteristic-zero field points.  Before `c6=0`, the
term `-c6/(128*A^3)` dominates and invalidates a direct D9 argument.  Grok46
review SHA `0a075a73...` passes 189 independent checks.  Modes
`c10,c12,c14,c16,c18,c20` have no causal support yet but remain mandatory in
every successor compiler.

## Reviewed D10--D13 continuation (2026-08-28)

After `W=A*R` and `c6=0`, define

```text
Delta5=F5-R/2-Z*V/64.
```

The reviewed causal sequence is

```text
D10_raw=-9*A*A'*Delta5^2                 (mod A^2),
Delta5=A*S,
D11_raw=(15/4)*A*A'*S^2                  (mod A^2),
S=A*Q,
D11_raw=-3*c10*A^2*A'                    (mod A^3),
c10=0.
```

Thus `F5=R/2+Z*V/64+A^2*Q`.  Next set

```text
Delta6=F6-Q/2-R*Z/8-V^2/256.
```

Then

```text
D12_raw=-6*A*A'*Delta6^2                 (mod A^2),
Delta6=A*S,
D13_raw=(9/4)*A*A'*S^2                   (mod A^2),
S=A*T,
```

so `F6=Q/2+R*Z/8+V^2/256+A^2*T`.  D10 and D12 have no
mode kill; D13 has no second mode consequence; `c12` remains the additive
`G12[X^0]` gauge.  Grok46 review SHA `9363d7cc...` independently passes 499
checks, including each cross-term omission and two nonzero-`c16` gauge
points.  Continue with all nine modes at D14.

## Reviewed D14--D15 continuation (2026-08-28)

Continue from the reviewed D13 prefix and define

```text
Delta7=F7-T/2-Q*Z/8-R*V/16.
```

The complete next coefficient has

```text
polar(g14)=3*Delta7^2/(8*A^2)+c14/A,
D14_raw=-3*A*A'*Delta7^2                 (mod A^2).
```

The order-two square first forces `Delta7=A*U`.  Only then is `c14/A` the
sole pole.  The literal polynomial `G14` window has shape `26x10`, rank 10
and nullity zero, so it cannot realize this rational kernel and `c14=0`.
This is a polynomial-window consequence, not a claim that the differential
operator detects `c14/A`.

If `c14` is provisionally retained, its complete D15 image is

```text
same-row  L15(-c14/(4*A^3)) = -3*c14*A',
mixed     (F1,G14)           = +3*c14*A',
sum                            0.
```

Thus D15 does not independently kill `c14`; the superseded same-row-only
claim is false.  After the D14 conclusion put

```text
Delta8=F8-T*Z/8-Q*V/16-R^2/4.
```

Then

```text
polar(g15)=-3*U^2/(16*A^2)+U*(3*Delta8/4+c8/2)/A,
D15_raw=(3/4)*A*A'*U^2                    (mod A^2),
```

so `U=A*Y` and
`F7=T/2+Q*Z/8+R*V/16+A^2*Y`; `c8` survives.  The lower equations
`C13,C14,C15` remain live through the invariant
`H0=c8/2+3*F8(0)/4`.  Corrected Grok46 review SHA `e4788bb8...` passes
334/334 checks, including all 513 raw generators, gauges and mutations.
Continue with all nine modes at D16.

## Reviewed D16--D17 continuation (2026-08-28)

Define

```text
B=F8-Y/2-T*Z/8-Q*V/16-R^2/4,
C=F9-Q*R/2-T*V/16-Y*Z/8.
```

The complete weight-sixteen relation is

```text
polar(g16)=(3*B^2/8+c8*B/2+c16)/A^2,
3*B^2+4*c8*B+8*c16=8*A^2*M.
```

It uniquely fixes `c16` if continuation exists but does not force zero;
literal exact points realize both `c16=3/8` and `c16=-3/8`.  The additive
`F8` gauge fixes

```text
Bhat=B+2*c8/3,
J16=c16-c8^2/6,
(3/8)*Bhat^2+J16=A^2*M.
```

Before imposing D16, D17's complete predecessor and same-row `c16` pieces
are `+6*c16*A'/A` and `-6*c16*A'/A`; they cancel.  After D16, the exact
next relation is

```text
(3*B+2*c8)*C-2*M=4*A^2*N.
```

Both A-adic lifts are live.  Grok46 review SHA `c2015d74...` passes 361/361
checks, including every raw generator, the literal window ranks, gauges,
both-sign points, lower equations `C13--C17`, and a one-A mutation.  The
displayed D17 invariant is not yet a source-tracked cutoff-three transport.
Continue with all nine modes at D18.

## Reviewed D18--D22 endpoint contradiction (2026-08-28)

Retain all nine modes and the reviewed D16/D17 quotients.  With the exact
cross-term-completed defects `E,H,J,K`, polynomiality gives

```text
D18: c18=0,
     (3*B/4+c8/2)*E+3*C^2/8-N/2=A^2*O,

D19: (3*B/4+c8/2)*H+3*C*E/4-O/2=A^2*P,

D20: c20=0,
     (3*B/4+c8/2)*J+3*C*H/4+3*E^2/8-P/2=A^2*S,

D21: (3*B/4+c8/2)*K+3*C*J/4+3*E*H/4-S/2=A^2*U.
```

The birth-row ordering is load-bearing.  At D19 the complete linked `c18`
pieces are `+9*c18*A'/A^2` and `-9*c18*A'/A^2`; at D21 the `c20` pieces are
`+12*c20*A'/A^3` and `-12*c20*A'/A^3`.  Each pair cancels, so only D18 and
D20 polynomial windows kill the corresponding mode.

After D21, complete `g22` has A-support

```text
{-2,0,2,4,6,8}.
```

There is no raw `G22`, hence

```text
D22_raw=-L22(g22) in (A).
```

The literal target is the full polynomial `D22(X)=1`, a contradiction for
`A=X^4-1`.  Grok46 review SHA `a294cdf7...` passes 289/289 checks, including
all 100 D18--D22 raw coefficients, ranks `5,3,2,1` of `G18..G21`, mutations,
endpoint sign, and the optional annihilated `c22/A^5`.  This closes only the
fixed `V0=1` field-valued endpoint fixture; it does not close general `V0`,
another branch, the endpoint scheme, Keller pairs, or JC2.
