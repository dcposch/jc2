# Registration: exact-square seven-tail Pell/Chebyshev classification

Date: 2026-08-26

Status: **V2 PREREGISTERED DUAL-AWS EXACT/GOOD-PRIME PRODUCER; V1 IS
FAIL-CLOSED NEGATIVE CUSTODY.**

This client tests the reduced solution set of the first seven negative
Laurent coefficients of

```text
sqrt(Q)*(Q^2+beta*Q+gamma),
Q=z^4+p*z^2+c*z+r.
```

The predicted support is the union of:

```text
square:       c=0, Delta=p^2-4*r=0;
Chebyshev:    c=0, 16*beta=5*Delta, 256*gamma=5*Delta^2.
```

The Chebyshev family obeys the exact identity

```text
A^2-Q*P(Q)^2=Delta^5/262144,
T=z^2+p/2,
P(Q)=Q^2+(5*Delta/16)Q+5*Delta^2/256,
A=T^5-(5*Delta/16)T^3+(5*Delta^2/256)T.
```

Registered lanes:

```text
exact Q: Box02, one core, 24 GiB VM cap, 1800 s
good prime 65521: Box03, one core, 16 GiB VM cap, 1800 s
```

The modular result is navigation only.  Even exact agreement classifies only
this seven-tail Laurent system.  Mapping it into the total Rees source,
terminal `[6,2]` row, Taylor receivers, order two, `(8,12)`, maximum twelve,
and JC2 are all separate obligations.
