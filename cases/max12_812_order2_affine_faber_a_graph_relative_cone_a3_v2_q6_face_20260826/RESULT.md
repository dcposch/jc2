# Result: repaired graph-relative `a=3` cone and `q=6` face

Date: 2026-08-26

Status: **DUAL-AWS PASS; SUPPORT SPLIT CERTIFIED.**

The exact-Q Box03 lane and characteristic-65521 r6d software lane analyzed
the independently frozen 365-term graph-relative support and agreed on the
following sharp split:

- the intrinsic cubic is the unique least term for `a=3,q>6`;
- by center-order monotonicity it is also unique for `a>3,q>=6`;
- the sole equality wall is `a=3,q=6`, at base weight 45.

At that wall there are exactly six minima: the intrinsic cubic, the two
nonstrict kernel competitors

```text
-(3/8)*X^2*a*lambda^2*M^2,
 (3/2)*Y^2*a*lambda^2*E,
```

and the three strict graph-deviation ties

```text
-(9/128)*d6*a*E^5,
 (1/8)*d2*a*E^3,
-dm*a*E.
```

There is no central `K10` term at or below weight 45.  The two lanes emitted
byte-identical summary stdout with SHA-256
`f80a40ef985e9a8fef553afb8a88e09d7fb8987b8bb49e204678d77491ecbea9`;
their validations are byte-identical with SHA-256
`4aabc91b3840a883ccb58d6646bb38a0328723af77413ff17d0479b1566a7007`.

This certifies the support split only.  The equality face still requires its
separate predecessor reduction, and this result makes no source/Rees,
order-two, maximum-twelve, or JC2 claim.
