# Result: corrected H17/q7/a3 grade-48 predecessor

Date: 2026-08-26

Status: **DUAL-AWS PASS; FIXED NORMALIZED PRODUCER.  THE FACE SURVIVES.**

The exact-Q Box03 lane and independent F65521 Box02 collection control
reconstructed all seven rows from the frozen complete tails.  Every row is
zero below absolute grade 48.  At grade 48 the complete block is

```text
C1=-3*r1*m^2/8+3*s0*m/4,
C2=3*d6*p^4/128-3*r0*m^2/8-d2*p^2/8+3*y^2/8-dm
   +15*kk*a^2*p^5/128,
C3=-3*r1*m^2*p/32-3*x*y*m/8+3*s0*m*p/16,
C4=3*x^2*m^2/32-3*r0*m^2*p/16-3*y^2*p/16-d4,
C5=-3*r1*m^2*p^2/256+3*x*y*m*p/32+3*s0*m*p^2/128,
C6=-d6*p^6/512-3*r0*m^2*p^2/64+d2*p^4/128
   +3*y^2*p^2/64-15*kk*a^2*p^7/1024,
C7=3*r1*m^2*p^3/1024-3*x*y*m*p^2/256
   -3*s0*m*p^3/512.
```

Here `a=a3` and `kk=kk0` are the leading center and `K10` coefficients.
The two center/load terms in `C2,C6` are genuine.  Their omission caused
V2 to fail closed in both characteristics; V3 then emitted the complete
block, and V4 validates every displayed coefficient.

The exact odd redundancies are

```text
C5=(3*p^2/32)*C1-(p/4)*C3,
C7=(p^2/32)*C3-(p^3/64)*C1.
```

On `D(p*m)`, the grade-48 face reduces to

```text
s0=r1*m/2,
x*y=0,
d2=d6*p^2/4+6*(r0*m^2-y^2)/p^2+(15/8)*kk*a^2*p^3,
dm=-d6*p^4/128-(9/8)*r0*m^2+(9/8)*y^2
   -(15/128)*kk*a^2*p^5,
d4=3*x^2*m^2/32-3*r0*m^2*p/16-3*y^2*p/16.
```

Thus both projective charts survive.  V4 checks exact zeros with
`p=m=a=kk=1` on each chart:

```text
D(x): x=1,y=0,r0=r1=s0=d6=0,
      d2=15/8, dm=-15/128, d4=3/32;
D(y): y=1,x=0,r0=r1=s0=d6=0,
      d2=-33/8, dm=129/128, d4=-3/16.
```

The next compulsory equation is at grade 51.  Existing exact support
shows that the odd functional has the central two-term tie

```text
-2*m^3*p^2+(5/4)*kk*a^3*p^7,
```

but its reduction together with the complete grade-49--51 rows is a
successor, not part of this result.  In particular V4 does not call the
grade-48 survivor either an arc or a contradiction.

The broad ordinary-Singular V1 replay timed out/no-verdict; the sparse
exact-Q engine is controlling.  V2 is an informative failed-closed
negative, and V3 is diagnostic custody only.

## Firewall

This result is only the fixed integral `(H,q,alpha)=(17,7,3)` predecessor
inside the normalized affine graph, on `D(p*m)`.  It does not prove the
grade-51 reduction, rational-regrading invariance, literal-source or
total-Rees accessibility, another graph/load schedule, order two,
`(8,12)`, maximum twelve, or JC2.
