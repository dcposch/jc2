# Promotion: generic-square high-contact `A`-prolongation and first moving-`p` tangent

Date: 2026-08-26

Status: **HOSTILE-REVIEW CONFIRMED AT THE STATED HIGH-CONTACT SCOPE.**

## Promoted statement

On the generic square open `D(p*k0)`, start after the reviewed half-weight
receiver `C=R=0` with `A` free and restrict to the high-contact cone

```text
Lambda=sigma^2,
ord_sigma(R)>=2,
ord_sigma(C)>=4.
```

For fixed `p`, the complete grade-fourteen and grade-fifteen negative
receivers have the reviewed form `h14,h15`.  The grade-fourteen equation
retains genuine root-allocation and correction faces, but after it is imposed
the grade-fifteen cleared numerator satisfies

```text
Num15 == -A0^3  (mod L),       L=z^2+p/2.
```

Since `L` is squarefree of degree two on `D(p)` and `deg(A0)<=1`, every
geometric point of this localized source scheme has `A0=0`.

The first base tangent

```text
p -> p+2*sigma*ell,
L(sigma)=z^2+p/2+sigma*ell
```

does not alter that separator.  Its complete extra grade-fifteen cleared
numerator `Delta` obeys

```text
Num14 == -12*B0*A0^2       (mod L),
Delta ==  12*ell*B0*A0^2   (mod L),
Delta == -ell*Num14         (mod L).
```

Thus `Delta` vanishes modulo `L` after the grade-fourteen equation, and
`Num15moving == -A0^3 (mod L,Num14)`.  The ordinary source rows and the
moving Faber transform agree exactly:

```text
g14 = T(p) h14,
g15 = T(p) h15moving + 2*ell*(dT/dp)(p) h14.
```

## Evidence and review

- Fixed-`p` root source/result freezes:
  `36dfff6b0cd7234c4e4e32a0a6bb82496fbdf543ebdfc4aa649cda519e6b8e51`,
  `13b1189088853c9781bec87dba16978f1342c818b34ff07bd8025c5ea24275d4`,
  `a00eeaa475eac943d67ad8fa9d954762572f2657fc791ab2ec0dc9688efdedfa`.
- Independent fixed-`p` owner result/freezes:
  `eba4640a9c7da51e4297e7e0b3c236f73f2eb2f70770de0634e1d0fea652d13f`,
  `6dbf5b6118aac14c38facdd977e221b0e4648a9e875fe03867172c646e322f64`,
  `3f3d729ed046431e92a6cbd1f5e373526525f39422a495fe9d66def8476a6e80`.
- Fixed-`p` hostile review:
  `00640cd4b80b079aa2123a686aad351ae3801ee0f4203aac2f7451c8c6d16c6d`
  (`CONFIRMED`).
- Moving-`p` V5 result/source/evidence freezes:
  `74551fe8b2ed1e4b9b1fd1594cee54e3bd3d87e6acee8b8c29d9384f5317d5ea`,
  `a2a665a4771f2941a8b64babb9fed35ddc877ce81af2e3fcf75f8a56b5ea1e94`,
  `380245162296ae04a2cdcc677b04d4617bd415e09665c999090bfab1741839a6`.
- Moving-`p` hostile review:
  `a3bbee7bb523bd1d049a4c4654e5843a8f37f372f362e69da514c18c52044f06`
  (`CONFIRMED`).

The exact-Q and `F_65521` lanes were distinct registered AWS executions on
Box03 and r6d with zero swap.  Characteristic zero carries the theorem; the
good-prime runs are software controls.  The quarantined V1 factor-two error,
V3 pre-engine wrapper-anchor failure, and V4 validator-prefix failure remain
preserved and contribute no endpoint.

## Scope firewall and successor

This eliminates the leading `A` direction only in the displayed high-contact
cone and for the displayed first `p` tangent.  It does not prove a full
Newton-fan exhaustion, cover `ord_sigma(R)=1` or `ord_sigma(C)<=3`, establish
higher `p`-jet stability, treat `p=0` or the square/discriminant intersection,
or impose later terminal/Taylor receivers.  It does not close the square
branch, order two, `(8,12)`, maximum twelve, or JC2.

The immediate successor is the exact low-contact fan: route `c=1,2`, then
use the complete grade-fifteen denominator filtration for `c>=3` rather than
proliferating separate rays.
