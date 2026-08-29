# Registration: independent `p=0` cusp grade-12 unit replay

Date: 2026-08-26

Independently reconstruct the complete normalized primitive coefficient
series and all seven canonical loaded tail rows through absolute grade twelve.
The client imports neither the terminal DAG nor the grade-10/11 Singular
emitter.  It must form every grade-11 and grade-12 source row before applying
only the two unit pivots `ell1=e0=0`, and then prove

```text
row(6,12)=(18144/125)*k^5*tau^8
          =-(21/1024)*rs^3*u^2.
```

This is a unit on `D(k*tau)=D(rs*k0)`.  The same replay must specialize to
`rs=u=1`, `s=a1=0`, `k0=-96/5` and recover `-21/1024` from exactly the four
contributing frozen-tail monomials.  Run on two registered AWS hosts.  Exact
Q carries the theorem; modular coefficients are controls only.
