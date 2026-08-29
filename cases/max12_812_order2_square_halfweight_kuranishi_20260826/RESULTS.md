# Generic-square correction-aware half-weight receiver

Date: 2026-08-26

Status: **DUAL-AWS PRODUCER ENDPOINT; EXACT-Q PASS; ONE NORMALIZED RAY;
NO SQUARE-BRANCH OR ORDER-TWO VERDICT.**

## 1. Endpoint

The complete frozen seven-row source was compiled independently over `Q`
and `F_65521` after

```text
Lambda=sigma^2,
M=sigma^3*(a1*z+a0),
S=sigma*(c1*z+c0)/2.
```

Both lanes passed every source hash, exact `sigma^10` divisibility,
quotient-identity, forbidden-variable, localization, and per-generator
radical-containment sentinel:

| field | host | tag | time | peak RSS | verdict |
|---|---|---|---:|---:|---|
| `Q` | Box03 | `max12_812_order2_square_halfweight_q_20260826T071955Z_box03` | 0.06 s | 14,636 KiB | PASS |
| `F_65521` | r6d | `max12_812_order2_square_halfweight_p65521_20260826T071955Z_r6d` | 0.06 s | 14,992 KiB | PASS |

Both used zero swap.  Exact-Q stdout SHA is
`54bf5d295b4533298708963465ada6def98b4277b308f5ef22e3ce07c47ec5e2`;
the good-prime stdout SHA is
`53517a5900e702e63682bd1409d0dd80f39cc40d7cef761d55fdf2136077b981`.

## 2. Exact divided source rows

The seven exact-Q grade-ten rows are

```text
-(5/32)*p*cs^3*k10+(15/256)*cs*rs^2*k10
 +(3/8)*a1*c0+(3/8)*a0*c1,

-(15/128)*p*cs^2*rs*k10+(5/1024)*rs^3*k10
 -(3/16)*p*a1*c1+(3/8)*a0*c0+(3/32)*c1^2,

(5/128)*p^2*cs^3*k10-(15/1024)*p*cs*rs^2*k10
 -(3/32)*p*a1*c0-(3/32)*p*a0*c1+(3/16)*c0*c1,

-(3/64)*p*c1^2+(3/32)*c0^2,

(5/1024)*p^3*cs^3*k10-(15/8192)*p^2*cs*rs^2*k10
 -(3/256)*p^2*a1*c0-(3/256)*p^2*a0*c1
 -(3/64)*p*c0*c1,

0,

(5/4096)*p^4*cs^3*k10-(15/32768)*p^3*cs*rs^2*k10
 -(3/1024)*p^3*a1*c0-(3/1024)*p^3*a0*c1
 -(3/512)*p^2*c0*c1.
```

They contain none of `k6,k2,mu2,mu4,mu6,J`, exactly as their frozen source
weights require.

## 3. Raw scheme and radical

The complete nonreduced standard basis is frozen in both stdout artifacts.
It retains the mixed `A*C`, quadratic `C`, and cubic `k10*R` scheme
structure.  On `D(p*k10)`, the exact radical is

```text
(c1,c0,rs,cs).                                       (3.1)
```

Both ideal containments in (3.1) were checked generator-by-generator over
`Q` and independently over `F_65521`.

The hand interpretation is transparent.  With

```text
L=z^2+p/2,
R=cs*z+rs/4,
A=a1*z+a0,
C=(c1*z+c0)/2,
D=L*A+C,
```

the divided source rows are the charged unitriangular coordinates of

```text
[(3/8)*D^2/L^2+(5/16)*k10*R^3/L]_- .                 (3.2)
```

Polynomiality of (3.2) gives `L^2 | 6D^2+5k10 R^3 L`.  Reduction modulo the
squarefree `L` first forces `C=0`, then forces `R=0`; `A` is free at this
grade.  The complete source and the hand UFD argument therefore agree.

## 4. Exact scope and successor

This is correction-aware for the primitive tie

```text
wt(Lambda,M,S,R)=(2,3,1,0)
```

and includes its coordinate faces.  It repairs the principal omission in
the ordinary fifth-grade zero-correction slice: the possible `A*C/L`
cross-term is present in every row.

It is not yet a proof that this ray exhausts the generic-square Newton fan.
Smaller/larger valuations must be routed by a lowest-weight argument, and
the surviving `A` direction must be prolonged with all new corrections.  In
the zero-new-correction subchart its next `k10` term is proportional to
`A^2/L`, but that observation is not a correction-aware verdict.

The degenerate core `p=0`, square/discriminant intersection, terminal row,
and both Taylor receivers remain outside this endpoint.  No strict arc,
square-component exclusion, order-two closure, `(8,12)` closure,
maximum-twelve theorem, or JC2 result follows.
