# q1 post-D9 proper-divisor square defect survives D11

Date: 2026-08-28  
Author: Sol Ultra  
Status: **EXACT PROVISIONAL PRODUCER / SIGNIFICANT NEWS / NEXT-ROUND INPUT**

## Verdict

The natural hope that D10/D11 immediately repair the square defect left by
the q1 D9 theorem is false.  On the proper-divisor component there is an
exact rational raw-window point with `W=B`, hence `A` does not divide `W`,
which satisfies every determinant row through D11.

Continue from the c2-zero D9 normal form

```text
A=C B,       V0=C v,       gcd(B,v)=1,
T=A u,
F4=V0*u/16+Z^2/64+A W,
W=B r.
```

Put

```text
J=64F5-uZ-16rv,
Q=64F5-uZ-32rv.
```

An independent replay of the complete characteristic recurrence, with all
ten scheduled modes retained, gives

```text
D9:   C | rJ,

P10 = 3Q^2 + 96B^2 r(256C F6-Cu^2-16rZ),
D10:  C^2 B^2 | P10,

D11:  C^3 B^4 | P11.
```

The exact useful relation is

```text
P11+vP10 =
 49152 B^4 C^2 F7 r -1536 B^4 C r^2 u
+16384 B^3 C^3 c10 v
+49152 B^2 C F5 F6 -192 B^2 C F5 u^2
-768 B^2 C F6 u Z +3 B^2 C u^3 Z
-96 B^2 r Z J.
```

At a root of `B`, D10 forces `Q/B` to exist.  After choosing `F6` so that
`P10=0`, the root value of the D11 bracket is

```text
-3 v (Q/B)^2 / C.
```

Thus D11 forces the next Hermite condition `B^2|Q`; it does not force
`A|W`.  This is the alternating divisor cascade one row deeper.

## Exact rational survivor

Use coefficient lists in increasing powers of `X`:

```text
A  = X^4-1,
C  = X-1,
B  = 1+X+X^2+X^3,
R0 = C,
V0 = A'R0+2AR0' = -2-4X^3+6X^4 = C(2+2X+2X^2+6X^3),
u  = -27/16,
T  = A*u,
Z  = 9/2,
W  = B,
c2=c6=c10=0,

F4 = V0*u/16+Z^2/64+A*W,

F5 = [1421/2048, 5/8, 7/16, 9/4, -9/16, -3/8, -3/16],
F6 = [-16551/65536, -117/512, -45/256,
      -27/256, -27/512, -9/512],
F7 = [117/8192, -27/2048, -135/4096, -27/2048, -27/8192],
F8=F9=F10=F11=0.
```

With all characteristic modes specialized to zero, reconstruct

```text
G=F^(3/2).
```

Exact division in `Q[X]` succeeds through coefficient 11.  Every `F_n` and
`G_n` lies in the literal generic raw slot window pinned from `RAW_INPUT`,
and a direct recomputation of

```text
D_n=sum_(i+j=n) ((12-j)F_i'G_j+(i-8)F_iG_j')
```

gives `D0=...=D11=0`.  Meanwhile division of `W=B` by `A` has quotient zero
and remainder `B`, so the survivor is genuinely outside the old `A|W`
slice.  The checker also evaluates the displayed factorizations and obtains
literal polynomial identities `P10=0` and `P11=0`.

## Provenance and mutations

The frozen D7--D9 compiler is reloaded by hash and independently extended to
weights 10 and 11.  The complete symbolic rows contain respectively 57 and
79 Laurent monomials before taking their polar parts.  The generic D3 raw
input is pinned by hash and supplies every literal lower/upper coefficient
window through weight 22.  It is not used as a leading-row fixture.

Live mutations catch the load-bearing choices:

- omitting the `A*H` Hermite adjustment in `F5` first makes coefficient 11
  nonpolynomial;
- dropping `F6` first makes coefficient 10 nonpolynomial;
- setting `c10=1` contributes `V0/(4A)=V1/(4B)` to `G11`, detecting failure
  to retain the born mode.

## Scope firewall

This proves only existence of an exact characteristic/raw-window prefix
through D11 on one proper-divisor q1 stratum.  It does not construct a lift
through D12--D22, satisfy the endpoint row, land in the complete GGV
reduction, construct a Keller map, disprove JC2, or prove JC2.  The q1 locus
itself still depends on the reviewed D23 licensing theorem.  The correct
successor is a sequential all-mode continuation of this single frozen prefix
through the remaining raw windows.

## Replay

```bash
cd cases/ggv_8_28_upper_endpoint_q1_post_d9_d11_survivor_20260828
python3 -B verify_q1_post_d9_d11.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```
