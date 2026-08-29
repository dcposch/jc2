# Registration: generic-square `r=1` and symbolic `d=1` AC receivers

Date: 2026-08-26

Status: **PREREGISTERED EXACT-SOURCE DUAL-AWS CLIENT.  NO SQUARE-BRANCH OR
ORDER-TWO VERDICT.**

Work on the generic unit-load square chart `D(p*k0)` after the reviewed
first-normal and half-weight gates and the producer-tier `c=1,2`
contact-raising gate.  Write

```text
Lambda=sigma^2,
K=L(sigma)^2+sigma^2 R(sigma),
D=L(sigma) A(sigma)+C(sigma),
L(sigma)=z^2+p(sigma)/2.
```

This package has two independent receivers.

1.  The `r=1` receiver puts `ord(A)>=1`, `ord(C)>=3`, and
    `R=sigma*R0+...`.  The unique absolute grade-13 negative term must be

    ```text
    (5/16) k0 R0^3/L0.
    ```

    The exact source rows are compared to this Laurent principal part.  A
    tiny localized support calculation on `D(p*k0)` must show that its seven
    zero rows force the two coefficients of the nonzero linear `R0` to
    vanish.

2.  The symbolic `d=1` receiver begins at `(a,c,r)=(2,3,2)` but introduces
    independent markers `theta,eta`:

    ```text
    A=sigma^2*theta*(A0+sigma*A1),
    C=sigma^3*theta*(C0+sigma*C1),
    R=sigma^2*theta*eta*R0.
    ```

    Substitution `theta=sigma^n`, `eta=sigma^s` represents the entire
    subcone

    ```text
    a=2+n, c=a+1, r=a+s,  n,s>=0.
    ```

    The compiler must certify the exact bidegree decomposition through the
    first successor grade.  It therefore distinguishes exactly the three
    modules: `(n,s)=(0,0)` with `C2,RC,R3`; `n>=1,s=0` with `C2,RC`; and
    `s>0` with `C2`, always together with the first moving-`L` connection.
    This is a symbolic translation certificate, not finite sampling.

    On the oriented etale root chart

    ```text
    p=-2*lambda^2,
    A0=au*(z-lambda), C0=cv*(z+lambda)
    ```

    the grade-15 `AC/L` row is polynomial.  After reconstructing the full
    grade-16 proper numerator over `L^2`, evaluation at `z=lambda` must be

    ```text
    (3/2)*lambda^2*cv^2*theta^2.
    ```

    All source corrections, the moving `p` term, `RC`, and the exceptional
    `R3` term are retained.  The deck-conjugate orientation is checked
    separately.  On `D(p*au*cv)` this is a nonzero unmatched double-pole
    coefficient.

The compiler reconstructs all seven frozen loaded Faber rows and verifies
the exact lower-unitriangular `w^2=z^2+p(sigma)/2` coordinate change.  It
fails closed on any later load/target contamination, source/analytic row
mismatch, recurrence failure, nonproper localization, or residue mismatch.

The exact-Q Box03 lane is proof-producing.  The independent `F_65521` r6d
lane is a software control.  Each gets a 24 GiB virtual-memory cap,
10-minute compiler cap, and one-hour engine cap.  Any timeout, diagnostic,
missing/nonunique sentinel, or nonzero exit is no verdict.

Scope is only `r=1` and the unique-`AC` subcone `a>=2,c=a+1,r>=a` on
`D(p*k0)`, conditional on the prior square first-normal/half-weight and
`c=1,2` gates.  The `(1,3)` and `(1,4)` AC charts, all other fan faces,
positive-order loads, `p=0`, `k0=0`, the exact-square zero section,
terminal/Taylor receivers, the square branch, order two, maximum twelve,
and JC2 remain outside scope.

