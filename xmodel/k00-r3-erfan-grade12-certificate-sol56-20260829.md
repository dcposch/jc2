# Normalized V20R2 valuation three: remaining-fan grade-12 certificate

Date: 2026-08-29  
Author/engine: Sol 5.6 Ultra  
Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`  
Status: **exact provisional finite-jet theorem; hostile review required before promotion**

## Result

The three cells left by the independently reconstructed grade-11 effective
rank fan are all empty at the next sequential grade:

| residual cell | required open | exact endpoint |
|---|---|---|
| `R3-00-ER1(+)` | `D(kappa*t*V)` | empty at grade 12 by a two-row unit identity |
| `R3-00-ER1(-)` | `D(kappa*t*V)` | empty at grade 12 by its independently replayed conjugate identity |
| `R3-00-ER2` | `D(kappa*Delta)` and `D(s) union D(t)` | empty at grade 12 by a binary-quadratic resultant and two ray certificates |

Consequently there is no residual case to send to grades 13 through 19.
Those grades are **unreached after a certified empty prefix**, not evaluated
as zero and not declared empty by missing output.  No AWS elimination was
needed or launched.

This closes the normalized V20R2 valuation-three finite-jet stratum, subject
to review of the preceding branch-completeness packet.  It does not prove the
Plane Jacobian Conjecture, exclude another valuation, change the V20R2 source
model, or infer any periodicity from valuation two, four, or five.

## Frozen literal source and normalization

The replay reconstructs all seven rows directly from the frozen 569 tails.
Its byte-pinned inputs are:

| input | SHA-256 |
|---|---|
| frozen `tails.json` | `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848` |
| V20R2 source compiler | `2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b` |
| sparse exact arithmetic/tail parser | `2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4` |
| this remaining-fan replay | `02fb368a054c781e8846e07a2948a5bdbe9e879abebc4e9b8e34be008f4e2053` |

The last file is imported only as a byte-pinned standard-library sparse
arithmetic library and tail parser.  No valuation-two conclusion is imported.
The literal coordinate map remains

```text
C0=(1+d0)/256, C1=d1, C2=(1+d2)/16, C3=d3,
C4=(3+d4)/8, C5=d5, C6=1,

Phi_l = R_l(d) + Lambda^2 K10 A10_l(d)
                 + Lambda^6 K6 A6_l(d)
                 + Lambda^10 K2 A2_l(d)
                 - Lambda^(12+l) delta_l.
```

The replay uses every literal column able to reach grades 6 through 12:

```text
d_j[n], j=0,...,5 and n=3,...,7                  30
k10[0],...,k10[4]                                 5
k6[1],...,k6[3]                                   3
                                                   --
total                                             38
```

It fixes `k6[0]=k2[0]=0` before expansion.  No free `K2` or target
coefficient can reach grade 12.  Thus the grade-12 certificate is
source-complete to its stopping grade; later source columns are not silently
specialized because no branch reaches their grades.

## Common grade-11 input

Write

```text
ell(s,t)=(2s,t/8,s,t,s,2t),
x=ell(s,t),
y=ell(a,b),
z=(2d+2u,c,d,8c+v,d-u,16c+4v),
U=u+(5/6)kappa*s,
V=v-(5/6)kappa*t,
Delta=U^2+64V^2.
```

Here `kappa=k10[0]` is a unit and `(s,t)!=(0,0)`.  The effective grade-11
normal matrix, using `A(w)=WA` and `B(w)=WB`, is

```text
             [ U   -V ]
             [64V   U ],        determinant Delta,
```

up to the row scalars `3/1024` and `3/16384`.  This is the shifted matrix
controlled by `(U,V)`, not the unshifted derivative at `(u,v)`.

The previously sealed source/threat packet proves that the effective
rank-zero cell is already empty and that the only residuals are
`ER1(+/-)` and `ER2`.  The new replay independently expands the literal rows
again on each of those three residual inputs and verifies all rows at grades
6 through 10 before solving grade 11.

## ER1(+/-): exact localized unit certificate

Put `j=epsilon*i`, where `epsilon=+1` or `-1`.  The effective rank-one and
grade-11 compatibility equations give

```text
U=8*j*V,       V!=0,
s=-8*j*t,      t!=0.
```

Let `qV*V=1`.  The freshly reconstructed first-row inhomogeneity is

```text
h1=-(5/16)t^3*kappa-(3/4)t^2*V.
```

For `T=A(w)`, set

```text
L=8*j*A(w)-B(w)=-(1024/3)qV*h1,
A(w)=T,
B(w)=8*j*T-L.
```

Direct substitution makes every grade-11 row zero modulo `qV*V-1`.  Project
the grade-12 vector to the six-dimensional cokernel of the rank-one normal
map.  Number the first five projections as

```text
C1=G12_4,
C2=G12_6,
C3=G12_3+G12_1/8,
C4=G12_5+G12_1/128,
C5=G12_7+G12_1/1024,
```

and take `C6=G12_2+(j/2)G12_1`.  The two rows needed for the obstruction are

```text
C1 = 25/384 t^6 kappa^2 qV^2
     +5/32 t^5 kappa qV +3/16 t^4
     -5j/512 t^3 T kappa qV -3j/128 t^2 T -3/4096 T^2,

C3 = -5j/16 t^5 kappa qV -3j/8 t^4
     -5/256 t^3 T kappa qV -3/64 t^2 T +3j/2048 T^2.
```

The replay also obtains `C2=0`, `C4=-C3/8`, and `C5=-C3/128`.  Exact sparse
arithmetic verifies the decisive identity

```text
12288*C1 - 6144*j*C3 = 800*t^6*kappa^2*qV^2.       (ER1-UNIT)
```

The right side is a unit on `D(kappa*t*V)`.  For a literal Bezout
certificate, adjoin `eta*kappa*t*V=1` and set

```text
A=eta*kappa*t*V,
B=qV*V,
M=eta^6*kappa^4*V^8/800,
P=12288*C1-6144*j*C3.
```

Then `M*P=A^6*B^2`, and the replay checks the polynomial identity

```text
1 = M*P
    -(A-1)(1+A+A^2+A^3+A^4+A^5)B^2
    -(B-1)(B+1).
```

This is an explicit unit-ideal certificate for each sign.  The two signs are
expanded and serialized independently; neither is inferred from the other.

## ER2: exact resultant and ray certificates

On `D(Delta)`, let `qD*Delta=1`.  With the grade-11 inhomogeneous first two
rows denoted by `h1,h2`, put

```text
r1=-(1024/3)h1,
r2=-(16384/3)h2,
A(w)=qD*(U*r1+V*r2),
B(w)=qD*(-64V*r1+U*r2).
```

All seven original grade-11 rows reduce to zero modulo
`qD*(U^2+64V^2)-1`.  At grade 12, the same five universal cokernel rows apply.
The second is zero and the fourth and fifth are `-1/8` and `-1/128` times the
third.  Thus only the first and third can be needed.

Clear the verified denominator without dropping a branch:

```text
N1=Delta^2*C1(qD=1/Delta),
N3=Delta^2*C3(qD=1/Delta).
```

They are binary quadratics in `(U,V)`:

```text
N1=kappa^2*(A U^2+B UV+C V^2),
N3=kappa^2*(D U^2+E UV+F V^2),
```

where

```text
A= 25s^6/25165824 -125s^4t^2/131072
   +125s^2t^4/2048 -25t^6/96,

B=-25s^5t/32768 +125s^3t^3/768 -25st^5/8,

C=-25s^6/393216 +125s^4t^2/2048
   -125s^2t^4/32 +50t^6/3,

D= 25s^5t/262144 -125s^3t^3/6144 +25st^5/64,

E= 25s^6/786432 -125s^4t^2/4096
   +125s^2t^4/64 -25t^6/3,

F=-25s^5t/4096 +125s^3t^3/96 -25st^5.
```

For binary quadratics, the exact Sylvester resultant used by the checker is

```text
Res=(A*F-C*D)^2-(A*E-B*D)*(B*F-C*E),
```

including the displayed common `kappa^2` factors in each quadratic.  Fresh
exact expansion gives

```text
Res = -5^8/(2^76*3^4)
      *kappa^8*(s^2+64t^2)^12.                    (ER2-RES)
```

A point of `ER2` has `(U,V)!=(0,0)` because `Delta!=0`; hence two vanishing
binary quadratics force their resultant to vanish.  Since `kappa!=0`,
`ER2-RES` forces `s^2+64t^2=0`.  Over the algebraically closed
characteristic-zero ground field, and with `(s,t)!=(0,0)`, this is one of

```text
s=rho*8*i*t,       rho=+1 or -1,       t!=0.
```

Both specializations are checked directly from the literal rows:

```text
N1|rho = -(25/3)t^6*kappa^2*(U+rho*8*i*V)^2,
N3|rho = rho*(50i/3)t^6*kappa^2*(U+rho*8*i*V)^2.
```

Thus `N1=0` forces `U+rho*8*i*V=0`.  But

```text
Delta=(U+8iV)(U-8iV),
```

contradicting the defining open `Delta!=0`.  Therefore `ER2` is empty at
grade 12.

## Sequential grade ledger

| grade | ER1(+/-) | ER2 | interpretation |
|---:|---|---|---|
| 6--10 | all seven rows replay to zero | all seven rows replay to zero | exact prefix replay |
| 11 | normal image solved; six coker rows respected | two normal coordinates solved; five coker rows respected | exact branch initialization |
| 12 | `ER1-UNIT` makes the localized ideal the unit ideal | `ER2-RES` plus both ray certificates contradict `D(Delta)` | all residuals empty |
| 13 | unreachable | unreachable | no residual input exists |
| 14 | unreachable | unreachable | no residual input exists |
| 15 | unreachable | unreachable | no residual input exists, including first `mu2` target grade |
| 16 | unreachable | unreachable | no residual input exists |
| 17 | unreachable | unreachable | no residual input exists, including first `mu4` target grade |
| 18 | unreachable | unreachable | no residual input exists |
| 19 | unreachable | unreachable | no residual input exists, including first `mu6` and `Jdet` target grade |

This is sequential early termination, not a jump from grade 12 to grade 19.

## Replay and public canonical certificate hashes

Run from the repository root:

```bash
python3 -m py_compile xmodel/k00-r3-erfan-grade12-replay-sol56-20260829.py
python3 xmodel/k00-r3-erfan-grade12-replay-sol56-20260829.py
python3 -O xmodel/k00-r3-erfan-grade12-replay-sol56-20260829.py
```

Both ordinary and optimized replays pass in about five seconds on the local
coordinator host.  The deterministic sparse serialization includes the ring
variable order, every exponent vector, and Gaussian-rational numerator and
denominator for every charged certificate polynomial.  Current hashes are:

```text
ER1_PLUS_CANONICAL_SHA256 = 215a9fd7334a6bc4854f24eb2060dcc2f5a9d0da33d6ef77e3da60787142c7e2
ER1_MINUS_CANONICAL_SHA256= 42a4c87abb02d60fcce71f8ed76d9fea0574800407225dc1ecddd55b75dc8992
ER2_CANONICAL_SHA256      = c5400833a19e81f68f4fe083d8c68867874b09954bbc75338172e70a0a9e387c
COMBINED_CERTIFICATE_SHA256=e6f05a903eaa0c31876a5729f41a706cd071bf4aecb1292fd58c04631aa943e2
```

The replay fails closed on source-byte drift, the `6144 -> 6143` ER1 unit
combination mutation, the `64 -> 63` ER2 inverse-matrix mutation, a newline
custody mutation, or a collision between the independently serialized
conjugate branches.  It uses explicit runtime checks rather than Python
`assert`, so `python3 -O` exercises the same gates.

## Threat audit and scope boundary

1. **Branch completeness.**  This report charges the previously sealed
   valuation-three source/threat packet for the elimination of leading ranks,
   the twice-old-plane reduction, and the grade-11 effective fan.  The new
   replay does independently rebuild the literal rows on every residual cell,
   but it is not a replacement review of that earlier fan.
2. **Field semantics.**  The ER2 ray step is a characteristic-zero,
   algebraically closed field-point argument.  It is appropriate for emptiness
   of the constructible finite-jet locus; no reducedness claim is needed.
3. **Localization honesty.**  ER1 carries both inverse relations and an
   explicit Bezout identity.  ER2 clears only powers of the defining unit
   `Delta` and then uses the defining open again at the final contradiction.
4. **No false empty output.**  Every branch has a displayed obstruction.
   Grades 13--19 are marked unreachable, not silently emitted as empty files.
5. **No cross-valuation periodicity.**  No formula or conclusion from
   valuation two, four, or five enters the proof.
6. **Finite-jet scope.**  The endpoint is the emptiness of this normalized
   V20R2 valuation-three stratum.  Any theorem connecting the complete
   normalized valuation atlas to JC2 remains a separate campaign obligation.

## Recommended independent review

The cheapest hostile review should independently reconstruct the 569 tails,
then check four load-bearing points:

1. the `5/6` effective shift and the grade-11 inverse matrices;
2. `ER1-UNIT` for each sign plus the explicit Bezout identity;
3. the denominator-cleared `N1,N3` coefficient table and `ER2-RES`;
4. both source-ray specializations and the final `Delta` contradiction.

No Gröbner basis or AWS machine is required unless that independent
reconstruction disagrees with one of these exact identities.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11923`.
- Body SHA-256:
  `0dca07ecf7538acd065fedbc60bd3f417400b86fa3ddf29f049a4dcf30a06c1e`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
