# Result: complete H17/q7/a3 rows through grade 51

Date: 2026-08-26

Status: **DUAL-AWS PASS; DIAGNOSTIC PRODUCER, NOT YET A REDUCED FACE
THEOREM.**

The exact-Q Box03 lane and independent F65521 Box02 control reconstructed
all seven complete normalized source rows through absolute grade 51.  The
corrected V4 grade-48 block is reproduced exactly; all lower coefficients
vanish.  Row-support sizes at grades 48--51 are

```text
grade48: 2,6,3,4,3,5,3
grade49: 4,11,9,8,10,12,10
grade50: 7,23,19,17,25,29,26
grade51: 13,41,39,29,55,58,61.
```

The exact functionals at grade 51 are

```text
Hseries51=-2*m^3*p^2+(5/4)*kk0*a3^3*p^7,

K51=4*d40*a3-dm0*p*a3+(1/8)*d20*p^3*a3
    -(9/128)*d60*p^5*a3+(3/2)*y0^2*p*a3
    -(3/8)*x0^2*m^2*a3-(1/16)*m^3*p
    -(65/128)*kk0*a3^3*p^6.
```

`Hseries` is identically zero below grade 51 after the complete source
substitution.  The first formula is therefore correction-independent in
this fixed schedule.  It defines the candidate receiver

```text
5*kk0*a3^3*p^5-8*m^3=0
```

on `D(p*m*a3*kk0)`.  Since `kk0` is a campaign/source parameter, this is
rational after solving for `kk0`; over fixed `kk0` it is a cubic Kummer
sheet.

The grade-49--51 raw rows and both functional polynomials are preserved
byte-for-byte in the evidence outputs.  Sequential reduction by the
grade-48 predecessor is the next client; V5 itself does not assert that the
receiver lifts, is accessible from a literal total-Rees chart, or survives
terminal/Taylor conditions.

## Firewall

Scope is the fixed normalized `(H,q,alpha)=(17,7,3)` graph.  This is not a
rational-regrading or source/total-Rees theorem, not an all-orders arc, and
not order-two, `(8,12)`, maximum-twelve, or JC2 closure/counterexample.
