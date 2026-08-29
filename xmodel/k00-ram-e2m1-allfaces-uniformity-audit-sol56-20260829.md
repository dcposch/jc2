# Generic-K00 ramified all-face theorem and uniformity audit

Date: 2026-08-29  
Author: Sol 5.6 Ultra  
Frozen campaign basis: `9b64db896b65e100839f6d75fbeea661cd818b9c`  
Status: **EXACT PRODUCER COROLLARY / CORE DIFFERENT-MODEL CONFIRMED / COROLLARY REVIEW-GATED; STRONGER INDUCTION REFUTED**

## 0. Endpoint

### Theorem: every `e=2,m=1` load-order face is empty

Work on the normalized generic K00 ray over a characteristic-zero field,
after the licensed finite field/Kummer extensions, with

```text
Lambda=tau^2,       ord_tau(d)=1,
C6,k10,Jdet units,
k6,k2,mu2,mu4,mu6 in tau*K[[tau]].                 (0.1)
```

No exact order is imposed on the last five series: each may have any finite
positive order or be the zero series.  Then the seven literal source rows
have no field-valued formal solution.  More sharply, their grades G0--G7
already have no geometric point on

```text
D(k10[0]) intersect (D(s) union D(t)).              (0.2)
```

Thus the corrected G7 certificate closes **all** boundary load-order faces at
`e=2,m=1`, not only its originally labelled `B11111` face.  It uses no
coefficient, equation, or open from K6, K2, `mu2`, `mu4`, `mu6`, or `Jdet`.

This is the maximum exact producer statement in this packet.

### Failed stronger reading

The tempting extension

```text
all integer e>=2 at m=1 by repeating the same unloaded recentering fan
```

is **not proved**, and the coefficient-blind induction proposed for it is
**refuted**.  There is an exact `e=3,m=1` rank-one full-source jet through G8
which disappears if one incorrectly sets the second surface coefficient to
zero.  G9 is the first undecided equation on that branch.  This is a finite
jet, not an arc.

## 1. Frozen source and replay

The charged bytes are

```text
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  frozen tails.json (569 monomials)
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  compile_contracted_source_v20r2.py
d453b9563d8f6cc23319d6bc0d8edce8a83f657b9e3a60cb244b00f181459860
  promoted G3 incidence theorem
66b4f59e16f9f8f26a42e5305e5906ff495c9d00c15d96a291f91baa9efbeff4
  corrected e=2,m=1 G7 report
981b39f91afd4e449193077bc00d02937701618cee9bc3ae53547edaaa11dac6
  corrected e=2,m=1 G7 replay
07c4ad13091c15dd39a5a703e266343323de40a3352d6d9449adb9c26473d736
  Opus 5 hostile review of the corrected G7 certificate
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  exact sparse-rational engine
0e7f98d165bf60531f675bae948315211fd08fd466f21f98aa399cd5fb12457b
  xmodel/k00-ram-m1-uniform-rankfan-replay-sol56-20260829.py
```

Opus returned `CONFIRM_WITH_CORRECTIONS`: it independently rebuilt the 569
tails, rederived the G3 reduction, and confirmed both complete fans and the
G7-to-G38 implication.  Its material documentation repairs are incorporated
below: the missing grade-2 center `mu`, the identification of the post-G3
open, and the distinction between a retained labelled row and a load-bearing
control.  The review also directly confirmed that deleting A6 and A2 leaves
the proof unchanged.  The all-load-order-face statement is the new corollary
of those reviewed facts and remains review-gated in its enlarged scope.

Run

```text
python3 -B xmodel/k00-ram-e2m1-g7-rankfan-replay-sol56-20260829.py
python3 -B xmodel/k00-ram-m1-uniform-rankfan-replay-sol56-20260829.py
python3 -B -O xmodel/k00-ram-m1-uniform-rankfan-replay-sol56-20260829.py
```

The new replay prints, identically in ordinary and optimized Python,

```text
K00_RAM_M1_UNIFORM_RANKFAN_REPLAY=PASS
TAIL_TERMS=569
UNLOADED_SURFACE=EXACT;UNLOADED_IDEAL_SUBSET_SURFACE_SQUARE=EXACT
SURFACE_LOAD_ORDERS=K10:3,K6:2,K2:1
STABLE_RANK2=EMPTY_AT_2N+1;STABLE_RANK1_NAIVE_KILL=REFUTED_BY_SURFACE_COEFFICIENT
E3_M1_RANK1_PREFIX=SURVIVES_FULL_SOURCE_THROUGH_G8;G9_UNDECIDED
FRESH_RANKZERO_FINAL_K10_FAN=SHIFT_INDEPENDENT_FOR_N_GE3
E2M1_LOAD_ORDER_FACES=ALL_POSITIVE_OR_INFINITE_BOUNDARY_ORDERS
THEOREM=EMPTY_FOR_E2_M1_ALL_LOAD_ORDER_FACES_ON_GENERIC_K00_RAY
CERTIFICATE_BYTES=3910
CERTIFICATE_SHA256=afd1bf5242adae7f300818ae1ae85c8c18b0cdb95a09bf03d7df430a2749c62a
MUTATIONS=CUSTODY,SURFACE_16_TO_15,K10_CUBIC,STABLE_640_TO_639,E3_SURFACE_COEFF,FINAL_SHIFT
```

The 3,910-byte canonical JSON object is rebuilt in memory and not written.

## 2. Proof of the all-face theorem

The literal normalized source is

```text
R(d)+tau^4*k10*A10(d)+tau^12*k6*A6(d)
    +tau^20*k2*A2(d)-targets                       (2.1)
```

at `e=2`.  The frozen exact stencil gives

```text
ord_d(A6_r)>=1,  ord_d(A2_r)>=1,
ord_tau(k6),ord_tau(k2)>=1.
```

Consequently K6 cannot occur before G14 and K2 cannot occur before G22.
The four target lower bounds are

```text
mu2 >= G29,  mu4 >= G33,  mu6 >= G37,  Jdet >= G38. (2.2)
```

These are lower bounds, not exact-order assumptions.  Raising any boundary
order or setting the series to zero only delays or deletes its sector.

Therefore every face in (0.1) has literally the same G0--G7 equations as the
corrected certificate.  That certificate retains all seven labelled rows and
proves, by two exhaustive reduced-support rank fans,

```text
G5 rank 2 -> empty at G5;
G5 rank 1 -> empty at G6;
G5 rank 0 -> fresh G6 cone;
G6 ranks 2,1,0 -> empty at G7 on k10[0] != 0.       (2.3)
```

The corrected G7 load is

```text
DM4(ell)[u]+A10^[3](ell)=DM4(ell)[u-mu/2],         (2.4)
```

where the required grade-2 center, omitted from the producer prose but
reconstructed in both replays and the hostile review, is

```text
mu=(s^2,s*t/8,16*t^2,0,0,0),   w=d[2]-mu.          (2.4a)
```

so the omitted cubic from the older prefix is retained.  In particular the
rank-one terminal is

```text
G7_2+(epsilon*i/2)G7_1
   =-epsilon*(5i/16)*k10[0]*t^3,                   (2.5)
```

and the rank-zero terminal contains

```text
W1=(5/4096)T(3S^2-64T^2),
W2=(5/65536)S(S^2-192T^2),                         (2.6)
```

whose only common zero is `(S,T)=(0,0)`.  Equations (2.3)--(2.6) use only
`k10[0]`, the transverse-order-one open, and the unloaded rows.  This proves
the theorem after dropping every late exactness open from `B11111`.
On the promoted G3 reduction, `(s,t)!=(0,0)` is exactly the original cell open
`union_i D(d_i[1])`; no pre-reduction coordinate is used in the cell statement.

## 3. Exact surface normal form

The seven unloaded rows vanish identically on

```text
D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T).          (3.1)
```

The literal surface ideal is

```text
J=(d0-2d4-d4^2,
   8d1-(1+d4)d3,
   d2-d4-16d3^2,
   d5-2d3).                                        (3.2)
```

Fresh expansion of all 569 tails in the four normal coordinates of (3.2)
shows generator by generator

```text
R_r in J^2,   r=1,...,7.                           (3.3)
```

This is an exact polynomial containment detected syntactically: after the
substitution `d=D(S,T)+normal`, every unloaded monomial has normal degree at
least two.  It explains why a rank-zero residual can be absorbed by extending
`S(tau),T(tau)`.

It does **not** say that mixed loaded equations set `R_r=0` termwise, and it
does not license replacing a finite loaded prefix by the reduced surface.
The nonreduced transverse cone and its rank-one arcs must still be retained.

## 4. Counterexample to the uniform recentering induction

Let a first transverse residual occur at order `n>=3`.  The grade `2n+1`
rank fan is the same exact fan as G5/G7.  On a rank-one chart write

```text
p=epsilon*8i*q,  s=epsilon*8i*t,  tq != 0,
mathcalB(v)-epsilon*8i*mathcalA(v)=-128*t*q,
X=mathcalA(v),
S=s*tau+alpha*tau^2+...,
T=t*tau+beta*tau^2+....                            (4.1)
```

The second surface coefficients cannot be discarded.  Two exact cokernel
equations at grade `2n+2` are

```text
C3 = epsilon*(3i/2048) *
  [X^2-epsilon*48i*t*q*X-512*t^2*q^2
       +16*alpha*q^2-epsilon*128i*beta*q^2],

C4 = -(3/4096) *
  [X^2-epsilon*48i*t*q*X-640*t^2*q^2
       -16*alpha*q^2+epsilon*128i*beta*q^2].        (4.2)
```

If one sets `alpha=beta=0`, the two bracketed forms differ by the apparent
fatal `128*t^2*q^2`.  That is the false induction.  In the actual source,

```text
X=epsilon*24i*t*q,  alpha=-4*t^2,  beta=0          (4.3)
```

makes both forms vanish.

The replay goes beyond compatibility and supplies a complete exact fixture.
Over `Q(i)`, put

```text
Lambda=tau^3,  k10=1,  Jdet=1,
k6=k2=mu2=mu4=mu6=0,

S=8i*tau-4*tau^2,       T=tau,
d=D(S,T)+tau^3*w+tau^4*v+tau^5*z,
w=(16i,0,0,1,-8i,4),
v=(-320,0,0,0,0,24i),
z=(-1088i,0,0,0,0,0).                              (4.4)
```

Direct evaluation of every frozen tail gives all seven full source rows zero
in grades G0--G8.  Here `ord_tau(d)=1`, `k10` and `Jdet` are units, and all
boundary conditions hold.  K10 first reaches this fixture at G9.  Changing
the coefficient `-4` in `S` to `-3` makes G8 nonzero.

Thus (4.4) is an exact counterexample to the proposed prefix induction.  It
is not a point of the infinite source, because G9 and all later equations are
unassigned.

## 5. Surface-restricted sector calendar and resonances

The exact load restrictions to (3.1) begin in `(S,T)`-degree

```text
A10|D: degree 3,
A6 |D: degree 2,
A2 |D: degree 1.                                   (5.1)
```

The first two rows are

```text
A10_1|D = (5/4096)T(3S^2-64T^2),
A10_2|D = (5/65536)S(S^2-192T^2) + terms of degree 4,

A6_1 |D = (3/64)S*T,
A6_2 |D = (3/2048)(S^2-64T^2),

A2_1 |D = T/2,
A2_2 |D = S/32.                                    (5.2)
```

Each displayed leading pair has only the origin as a common zero.  All three
load sectors vanish identically on row 4:
`A10_4|D=A6_4|D=A2_4|D=0`, as the hostile review independently checked.
On an already recentered surface branch with `ord(S,T)=m`, write positive boundary
orders as `h6,h2,hmu2,hmu4,hmu6`, allowing `infinity`.  The restricted first
grades are

```text
nu10  = 2e + 3m,
nu6   = 6e + h6   + 2m,
nu2   = 10e+h2   + m,
numu2 = 14e+hmu2,
numu4 = 16e+hmu4,
numu6 = 18e+hmu6,
nuJ   = 19e.                                       (5.3)
```

This table is conditional on the surface/rank-zero branch.  Normal terms can
arrive earlier on a transverse branch, so (5.3) is not a global arc calendar.

The K10 resonance walls in this restricted calendar are

```text
h6   = m-4e,
h2   = 2m-8e,
hmu2 = 3m-12e,
hmu4 = 3m-14e,
hmu6 = 3m-16e,
3m   = 17e                         (K10/Jdet).       (5.4)
```

Whenever a right side is not a positive integer, that face does not occur.
At a tie, vectors from K6/K2 or a target coordinate axis may cancel a K10
cokernel class; the isolated common-zero calculation (5.2) does not decide
the combined fan.  In particular, target series are free source variables
until their exact-order opens are imposed and must not be treated as fixed
nonzero obstructions.

There is an earlier, representation-level wall: the generic K10 quadratic
grade `2e+2m` meets the unloaded cubic grade `3m` when

```text
m=2e.                                               (5.5)
```

At and beyond (5.5), even the promoted unloaded G3 leading-plane reduction
cannot be imported without a new mixed fan.

## 6. Ranked next exact cells

1. **`e=3,m=1,G9` rank-one carry.**  Retain `alpha,beta,X`, the four free
   directions in `v`, and the five-dimensional G8 lift fiber.  Add the
   corrected K10 cubic and eliminate only the newest coefficient block.  The
   fixture (4.4) is a mandatory old-pass control; `alpha=0` is a forbidden
   simplification.
2. **`e=2,m=2` all faces.**  This is the lexicographically first unclosed
   transverse valuation.  Its intermediate odd coefficients prevent a
   simple `tau^2` reparameterization.  Freeze the literal rows through the
   first K10 surface grade G10 and split the transverse cone without deleting
   odd columns.
3. **Mixed leading wall `e=2,m=4`.**  Here (5.5) is reached; solve the K10
   quadratic and unloaded cubic together at the first compatibility grade.
4. **First surface load-tie family `e=2,m=9`.**  For example `h6=1` gives
   `nu6=nu10=31`; `h2=2` and `hmu2=3` can join the same grade.  This is the
   first small integer cell requiring a genuinely coupled K10/K6/K2/target
   cokernel fan rather than an isolated load argument.

All four are desk-scale source-emission/rank-design tasks initially.  Any
uncertain elimination must be frozen and moved to registered AWS.

## 7. Scope firewall

The theorem is a geometric, field-valued emptiness statement for the exact
`e=2,m=1` generic-K00 formal source cell.  It excludes a formal arc in that
cell because every arc would restrict to its impossible G7 jet.  It does not
assert an explicit Bezout identity for the localized jet ideal.

The G8 object (4.4) is only a finite jet and proves no G9 lift, formal arc,
algebraic arc, source-closure point, Taylor trajectory, rational or polynomial
map, Keller pair, counterexample, or attainment.  No conclusion here covers
`m>=2`, the `C6=0` tip, `k10=0`, `Jdet=0`, another K00 support/load ray, Gate
T, order two, maximum twelve, or JC2.  Floors, infima, and attained valuations
are not interchanged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13029`.
- Body SHA-256: `5925efef3638ba5a0dcc8b855933fbc7c557ea82f8015edd5564496384c99c06`.
- Frozen basis: `9b64db896b65e100839f6d75fbeea661cd818b9c`.
