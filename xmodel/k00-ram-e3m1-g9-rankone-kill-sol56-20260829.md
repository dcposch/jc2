# Exact G9 kill of the banked `e=3,m=1` stable-rank-one family

Date: 2026-08-29  
Author: Sol 5.6 Ultra  
Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`  
Lifecycle: **EXACT PRODUCER / PROVISIONAL / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Endpoint

The banked `e=3,m=1` full-source fixture does not lift through G9.  More
strongly, both Gaussian signs of the reduced stable-rank-one G8-compatible
family containing that fixture are empty at literal source grade G9.

On the rank-one open `t*q != 0`, write `epsilon in {+1,-1}`.  The two exact
G8 cokernel equations force, on field-valued points,

```text
X = epsilon*24*i*t*q,
alpha - epsilon*8*i*beta = -4*t^2.                 (0.1)
```

After retaining `beta`, all four free grade-four kernel coordinates, the
full five-dimensional grade-five lift fiber, arbitrary coefficients
`d[6],d[7],d[8]`, and arbitrary displayed K10 coefficients, the literal raw
row-six coefficient is

```text
G9_6 = epsilon*i*q^3/32.                           (0.2)
```

It is a unit on `D(q)`.  Thus this reduced rank-one chart has no G9 point.
For the banked fixture `epsilon=+1,t=q=1`, (0.2) is `i/32`.

This is the first decisive G9 gate.  It shows that the earlier fixture is a
genuine finite jet through G8 and a one-grade delay of the obstruction, not
an arc.  It does not restore the false coefficient-blind claim that the
branch dies at G8.

The G0--G8 premise and its enlarged all-face parent remain review-gated at
this cutoff.  This report independently reconstructs their literal source
coefficients, but it is produced by the same model and therefore cannot
promote them.

## 1. Frozen source and custody

The replay charges the following exact bytes:

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  frozen tails.json (569 monomials)
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  compile_contracted_source_v20r2.py
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  exact sparse-rational engine
64eaafe3fe5aaa9238a338f2da045e302d9a239ac9c29312e39d5c545893d42c
  all-face uniformity producer carrying the G8 fixture
0e7f98d165bf60531f675bae948315211fd08fd466f21f98aa399cd5fb12457b
  all-face/uniformity replay
0eb501b414f2162d14a73725a46410b7e799adc70932cdfb8a05f4196ff0bb1a
  promoted corrected-G7 binding integration
3ef20945b4a009bba4dccbbf7a43461718feb8155e84f513f14c736ce45182e2
  xmodel/k00-ram-e3m1-g9-rankone-kill-replay-sol56-20260829.py
```

The new replay reconstructs all seven unloaded and K10 rows directly from
the 569 tails.  It does not substitute the promoted unloaded radical or set
the unloaded rows to zero inside the mixed source.

The normalized `e=3` source through G9 is literally

```text
R(d) + tau^6*k10(tau)*A10(d).                      (1.1)
```

K6 first has lower bound G20, K2 G32, `mu2` G43, `mu4` G49, `mu6` G55,
and `Jdet` G57 when the boundary series have positive order; zero series
delete their sectors.  Hence none can occur in this gate.  The normalization
is `Lambda=tau^3`, `C6=1`; no higher coefficient of `Lambda` is introduced.

## 2. Typed rank-one coordinates

Work over `Q(i)` or a characteristic-zero extension containing `i`.  Define

```text
A(x)=x5+16*x1-4*x3,
B(x)=x0-4*x2+2*x4.                                 (2.1)
```

Use the exact surface

```text
D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T),          (2.2)

S=epsilon*8*i*t*tau + alpha*tau^2,
T=t*tau + beta*tau^2.                             (2.3)
```

The first transverse normal is

```text
w_epsilon=(epsilon*16*i*q,0,0,q,-epsilon*8*i*q,4*q).
                                                               (2.4)
```

At grade four write

```text
v=V(X,Bv;y1,y2,y3,y4)
 =(Bv+4y2-2y4, y1, y2, y3, y4, X-16y1+4y3),       (2.5)

Bv=epsilon*8*i*X-128*t*q.                         (2.6)
```

Then

```text
d=D(S,T)+tau^3*w_epsilon+tau^4*v+tau^5*z
       +tau^6*u+tau^7*r+tau^8*h+... .             (2.7)
```

Here `y1,...,y4`, all six coordinates of `z,u,r,h`, and the K10 series
coefficients are retained as algebraically independent variables.  The
letters `r,h` in (2.7) are coefficient vectors only and are unrelated to
the seven source-row labels.

The banked fixture is the specialization

```text
epsilon=+1, t=q=1, beta=0, alpha=-4, X=24*i,
y1=y2=y3=y4=0,
z=(-1088*i,0,0,0,0,0),
u=r=h=0, k10=1.                                    (2.8)
```

This reproduces exactly

```text
S=8*i*tau-4*tau^2, T=tau,
w=(16*i,0,0,1,-8*i,4),
v=(-320,0,0,0,0,24*i),
z=(-1088*i,0,0,0,0,0).
```

## 3. G8 compatibility and its reduced support

Before imposing (0.1), the replay reconstructs the two literal G8 cokernel
forms

```text
F512 = X^2-epsilon*48*i*t*q*X-512*t^2*q^2
       +16*alpha*q^2-epsilon*128*i*beta*q^2,

F640 = X^2-epsilon*48*i*t*q*X-640*t^2*q^2
       -16*alpha*q^2+epsilon*128*i*beta*q^2.       (3.1)
```

They occur as

```text
G8_3+(1/8)G8_1 = epsilon*(3*i/2048)*F512,
G8_4             = -(3/4096)*F640.                 (3.2)
```

Exact factorization gives

```text
F512-F640 = 32*q^2*(4*t^2+alpha-epsilon*8*i*beta),
F512+F640 = 2*(X-epsilon*24*i*t*q)^2.              (3.3)
```

On a characteristic-zero field and `D(q)`, (3.3) gives precisely (0.1).
This is a reduced/field-valued inference.  The square in the second line is
not silently replaced by a linear generator at the nonreduced scheme level.

After substituting (0.1), put

```text
Az=z5+16*z1-4*z3,
Bz=z0-4*z2+2*z4,

H_epsilon = Bz-epsilon*8*i*Az +128*q*beta
            +epsilon*1088*i*t^2*q
            -512*t*y1-epsilon*8*i*t*y2
            +64*t*y3+epsilon*8*i*t*y4.             (3.4)
```

The seven full source G8 rows are exactly

```text
(-3/1024, epsilon*3*i/2048, 3/8192, 0,
  3/131072, 0, 3/1048576) * q*H_epsilon.           (3.5)
```

Thus G8 is equivalent to `H_epsilon=0` on `D(q)`.  Formula (3.4) is monic in
`z0`: the four `y` directions remain free and, over each choice of them and
the older parameters, the `z` lift fiber has dimension five.  Specialization
(2.8) gives `H_+=z0+1088*i=0`, confirming that the banked fixture lies in
this exact family.

## 4. Literal G9 terminal

The replay now evaluates every source row at G9 before any surface-ideal or
cokernel quotient.  On both signs it obtains

```text
G9_6 = epsilon*i*q^3/32.                           (4.1)
```

There is no dependence on `beta`, `y`, `z`, `u`, the grade-seven or
grade-eight coefficient blocks, or `k10[0..3]`.  The K10 row-six series has
zero coefficients in degrees zero through three, so K10 contributes nothing
to (4.1); this is an unloaded raw row-six obstruction.  All later loads are
excluded by the literal calendar in §1.

Since `q` is a unit on the rank-one chart, (4.1) is impossible.  This proves
field-valued point-set emptiness of the reduced G8-compatible family at G9.
It also proves the exact banked fixture has no one-step G9 lift, even after
all coefficients which can possibly enter through that grade are freed.

## 5. Controls and replay

The replay includes four independent control classes.

1. Every charged hash and the 569-term census are fail-closed.
2. Replacing the essential surface relation coefficient `-4*t^2` by
   `-3*t^2` leaves the G8 compatibility wall `t^2`, so the old prefix fails
   on `D(t)`.
3. Mutating K10 row six by a forbidden `d3^3` term changes the G9 terminal by
   exactly `k10[0]*t^3`; this verifies that the asserted K10 absence is seen,
   not assumed by dropping the sector.
4. Setting `q=0` kills (4.1), confirming that the rank-one open is
   load-bearing and that this proof does not cover the rank-zero boundary.

Run

```text
python3 -B xmodel/k00-ram-e3m1-g9-rankone-kill-replay-sol56-20260829.py
python3 -B -O xmodel/k00-ram-e3m1-g9-rankone-kill-replay-sol56-20260829.py
```

Both modes print identically:

```text
K00_RAM_E3M1_G9_RANKONE_REPLAY=PASS
TAIL_TERMS=569
PREMISE_G0_G8=PRODUCER_EXACT_REVIEW_GATED
SIGNS=PLUS,MINUS;OPEN=t*q!=0
G8_FIELD_COMPAT=X=EPS*24*i*t*q;alpha-EPS*8*i*beta=-4*t^2
G8_LIFT=H_EPS=0;Y_DIRECTIONS=4;Z_FIBER_DIM=5
G9_ROW6=EPS*i*q^3/32
K10_ROW6_G9=ZERO;LATE_LOADS=ABSENT
VERDICT=REDUCED_STABLE_RANKONE_G8_FAMILY_EMPTY_AT_G9_ON_D(q)
CERTIFICATE_BYTES=4675
CERTIFICATE_SHA256=53cb17004c510c34de96c64838c9707d10400aa83b36d5b9cb56bf4c01630ed9
MUTATIONS=CUSTODY,SURFACE_-4_TO_-3,K10_ROW6_D3_CUBED,Q_OPEN
```

Runtime is about 6.5 seconds per mode using Python stdlib exact
`fractions.Fraction` arithmetic.  No CAS, AWS task, or local heavy process is
used.

## 6. Lifecycle, stop condition, and next cells

This packet is `EXACT PRODUCER / PROVISIONAL`.  It may be explored cheaply,
but promotion requires a different-model hostile reconstruction of the
literal source, both signs, the G8 factorization, the five-dimensional lift
fiber, the raw G9 row-six coefficient, and all mutations.

Stop or narrow this result immediately if review changes any frozen source
hash, the `Lambda=tau^3` normalization, the K10 shift, the rank-one open, or
the G8 compatibility parameterization.  A point with `q=0`, a different
leading/normal-rank stratum, or a source point not reaching coordinates
(2.3)--(2.7) is outside the theorem and must not be absorbed by closure.

The exact next ramified work is therefore not G10 on this dead branch.  It is
to classify the other `e=3,m=1` rank strata and rank-zero recenterings, then
place them in the honest load/resonance calendar.  The G8 fixture remains a
mandatory old-pass control for any such compiler because it refutes death at
G8 even though its reduced rank-one family dies one grade later.

This report does not close the whole `e=3,m=1` cell, another `(e,m)`, another
support/open, the ramified source atlas, source completeness, all-order
lifting, reachability, or algebraization.  A finite-jet exclusion is not a
formal arc theorem outside its exact source cell and is not an attained
source point, polynomial map, counterexample, or JC2 result.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9880`.
- Body SHA-256:
  `0fe19184da754151933294aa7377273d03e07f4b7830ee430d20984c53827b36`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
