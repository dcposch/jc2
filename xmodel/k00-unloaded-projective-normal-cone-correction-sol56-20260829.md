# Unloaded K00: the true projectivized normal cone is empty; the quartic governs only the seven-quadric leading system

UTC: 2026-08-29  
Author: Sol / coordinator  
Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`  
Lifecycle: `EXACT COMPOSITION / PRODUCER CORRECTION / REVIEW REQUIRED`

## Exact correction

Let

```text
A = Q[d0,...,d5],
I = (r1,...,r7),
J = (f0,f1,f2,f5),
R = A/I,       K = J/I.
```

The reviewed unloaded-radical packet proves `I subset J`, `sqrt(I)=J`, and

```text
f0^5, f1^5, f2^5, f5^5 in I.                         (1.1)
```

Every monomial of total degree 17 in four generators contains a fifth power,
because `17>4*(5-1)`. Hence

```text
J^17 subset I,       equivalently K^17=0 in R.         (1.2)
```

Consider the actual normal cone of the reduced support
`D=Spec(A/J)` inside the nonreduced scheme `X=Spec(A/I)`:

```text
C_D X = Spec(gr_K(R)),
gr_K(R) = direct_sum_(n>=0) K^n/K^(n+1).
```

By (1.2), `gr_K(R)` is concentrated in degrees `0,...,16`; its irrelevant
ideal `gr_K(R)_+` is nilpotent. Every homogeneous prime contains every
nilpotent element, hence every homogeneous prime contains the irrelevant
ideal. Therefore

```text
Proj(gr_K(R)) = empty.                                (1.3)
```

This conclusion holds over every base change and every point of `D`. The
affine cone need not be the zero scheme: it can retain nilpotent normal
structure supported on the zero section. Its projectivization nevertheless
has no points because there is no nonnilpotent positive-degree direction.

## Consequence for the Opus quartic

The sealed Opus blind report

```text
xmodel/ideation-20260829T2254Z-opus5.md
full d8e7328479232094b1a77ec8560d85e0a70e4288b18e49d506602bd746d6aa36
body 34609 / 2b9e2f08f4e58252d984944a34e9d78fa5b596bfe1a350aadc073ed39d393b30
```

extracts the degree-two normal parts `Q1,...,Q7` of the seven chosen row
generators and eliminates their nonzero common directions. It obtains

```text
Delta(S,T)=S^3+S^2+72*S*T^2+64*T^2-432*T^4.           (2.1)
```

Even if every displayed computation of `(Q1,...,Q7)` and `Delta` is correct,
the ideal of those seven initial forms need not equal the full filtered
initial ideal `in_J(I)`: cancellations among row generators and higher
members of `I` can add initial forms.

Here strict inequality is forced without any heavy computation. In the exact
normal coordinates `e0,e1,e2,e5`, (1.1) puts

```text
e0^5, e1^5, e2^5, e5^5 in in_J(I).                   (2.2)
```

At the node `(S,T)=(0,0)`, Opus reports that all seven quadrics vanish
identically on the plane

```text
P0 = {e0=4*e2, e5=-2*e1}.
```

But `e0^5` restricts to `4^5*e2^5`, a nonzero polynomial on `P0`.
Consequently

```text
(Q1,...,Q7) is strictly contained in in_J(I)           (2.3)
```

at that fibre. In particular, a nonzero direction of the seven-quadric
system is not a projective point of the actual normal cone.

The maximum safe interpretation pending hostile reconstruction is therefore:

> `Delta=0` is the parameter locus where the **seven quadratic leading row
> equations** have a nonzero normal solution, if the elimination and
> specialization claims in the producer are confirmed.

It is not the locus where `Proj(gr_K(R))` is nonempty; that Proj is empty by
(1.3). The quartic, its node/cusps, its parametrization, and its recovery of
the first polar rank fan may remain useful as a **quadratic resonance
discriminant** for finite-order loaded deformations. This correction changes
the object and lifecycle, not necessarily those computations.

## Valuation sandwich

The separate exact normal-coordinate replay claims `I subset J^2` and Opus
independently recomputes it. Together with (1.2), for a centered valuation
with

```text
v(L)=min{v(h):h in L}
```

one obtains

```text
2*v(J) <= v(I) <= 17*v(J).                            (3.1)
```

Indeed, inclusion reverses ideal value: `I subset J^2` gives
`v(I)>=v(J^2)=2v(J)`, while `J^17 subset I` gives
`17v(J)=v(J^17)>=v(I)`. This linearly compares the two ideal topologies and
bounds possible transverse slopes. It does not identify integral closures,
compute the actual Rees valuations, license loaded recentering, or prove an
arc or map.

The exponent 17 is the universal pigeonhole bound from four fifth powers,
not a claim of minimality. An independent exact membership lane is testing
the least `N` with `J^N subset I`.

## Evidence and firewalls

The reviewed fifth-power and radical evidence is carried by:

```text
review full 6f300d9890bb624e7c1023763271e409cc106c3f68e94436809b0ca18cf5a178
review body 17402 / 1300566c9b862a1c4624b893e91e426ac7295d004667ea247cab9883005b8c01
integration full e3e84ac9a9aba58fcff731c0b75a279b8f7d62ce252e91253a708234bebcab08
integration body 5312 / d5294dab7f1a8c6c6c311fed667920f7e45385ea621299cebed362595f494d64
```

No loaded source sets `I=0`; no equality of schemes follows from radical
equality; finite-jet survival is not an arc; and a quadratic leading-system
direction is not an attained point of `X`. This report does not decide the
hostile review of the quartic's computations, any load restriction, source
completeness, a Keller map, a counterexample, or JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5183`.
- Body SHA-256:
  `b115f76e36dfeda68d0c08eac1eae981b4feb4f85a8d713f8a9655bc501f4dab`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
