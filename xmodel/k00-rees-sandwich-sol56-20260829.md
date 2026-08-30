# K00-REES-SANDWICH: exact nilpotence exponent five, valuation sandwich, and the full-initial-ideal correction

UTC: 2026-08-30  
Author: Sol 5.6 / independent AWS producer  
Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`  
Lifecycle: `EXACT INDEPENDENT PRODUCER / FRESH REPLAY COMPLETE / REVIEW REQUIRED / INTEGRATION READY`

## 1. Charge and frozen inputs

Let

```text
A = Q[d0,d1,d2,d3,d4,d5],        I=(r1,...,r7),
f0=d0-2d4-d4^2,                  f1=8d1-(1+d4)d3,
f2=d2-d4-16d3^2,                 f5=d5-2d3,
J=(f0,f1,f2,f5).
```

The literal rows are reconstructed from the frozen unloaded prelude, SHA-256
`5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a`.
The reviewed radical/fifth-power chain is:

```text
producer full     96d88f49fd8e2dab1b05d18ac7912d7c1e3374fc474dcfafce29a08558edb62b
review full       6f300d9890bb624e7c1023763271e409cc106c3f68e94436809b0ca18cf5a178
review body       17402 / 1300566c9b862a1c4624b893e91e426ac7295d004667ea247cab9883005b8c01
integration full  e3e84ac9a9aba58fcff731c0b75a279b8f7d62ce252e91253a708234bebcab08
integration body  5312 / d5294dab7f1a8c6c6c311fed667920f7e45385ea621299cebed362595f494d64
```

It proves `sqrt(I)=J`, `A/J = Q[d3,d4]`, and supplies 28 exact multiplier
polynomials replaying

```text
f0^5, f1^5, f2^5, f5^5 in I,       while fa^k notin I for 1<=k<=4.
```

The separate literal normal-coordinate replay has full hash
`0e7f98d165bf60531f675bae948315211fd08fd466f21f98aa399cd5fb12457b`
and checks all seven rows, not selected rows.  The AWS runs below independently
reconfirm `I subset J^2` and `I not subset J^3`.

The Opus blind report was seal-verified before Section 1 was read:

```text
full  d8e7328479232094b1a77ec8560d85e0a70e4288b18e49d506602bd746d6aa36
body  34609 / 2b9e2f08f4e58252d984944a34e9d78fa5b596bfe1a350aadc073ed39d393b30
```

Only its exact coordinate definitions and the seven-row leading-system claim
were in charge.  Its quartic elimination is not recomputed or promoted here,
and the separate Fable review is deliberately not consumed.

## 2. Analytic upper bound and exact least exponent

The reviewed fifth-power identities already prove the proposed bound

```text
J^17 subset I.                                             (2.1)
```

Indeed, a degree-17 monomial in four generators has some exponent at least
five, since `17>4*(5-1)`, and is therefore a multiple of one reviewed fifth
power.  This proof is an exact identity argument; it uses no modular screen or
`msolve` characteristic-zero `[1]` inference.

The bound 17 is true but very far from least.  Two fresh exact-Q computations
prove

```text
J^5 subset I,             f5^4 notin I.                    (2.2)
```

Consequently:

> **Theorem K00-REES-SANDWICH.** The least positive integer `N` satisfying
> `J^N subset I` is exactly **5**.

For the upper endpoint, AWS V2 recomputed an ordinary exact standard basis of
`I` (114 elements).  At total degree five it reduced to zero all 52 monomials
whose four exponents are at most four; the four omitted degree-five monomials
are exactly the four replayed pure fifth powers.  Thus all 56 canonical
generators of `J^5` lie in `I`.  It then found the degree-four witness

```text
f5^4=(d5-2d3)^4
    =16d3^4-32d3^3d5+24d3^2d5^2-8d3d5^3+d5^4,
```

whose V2 normal form is that same nonzero polynomial.  If any `J^m` with
`m<=4` were contained in `I`, multiplication by `J^(4-m)` would put `J^4` in
`I`, contradicting this witness.  Hence 5 is least.

The independent replay used the exact triangular automorphism

```text
d0=e0+2S+S^2,                 d1=(e1+(1+S)T)/8,
d2=e2+S+16T^2,                d3=T, d4=S, d5=e5+2T.
```

It carried all four `f` generators and all seven rows through the map,
required the first four images to be exactly `(e0,e1,e2,e5)`, detected the
`16 -> 15` mutation, built an 80-element `liftstd` basis, and replayed every
basis column into the seven transformed rows.  All 56 generators of
`(e0,e1,e2,e5)^5` reduced to zero.  Independently, `e5^4` had nonzero normal
form

```text
(1/40)e5^2 S^2 -(32/5)e5^3 T -(48/5)e5^2 T^2 -(1/80)e0 e5^2
+(3/10)e2 e5^2 -(1/10)e1 e5 S -(1/4)e5^2 S -(1/20)e0 e5 T
+(4/5)e2 e5 T +(1/10)e1^2 +(1/320)e0 e2 -(1/80)e2^2
+(3/10)e1 e5 +(1/8)e5^2.
```

This replay does not consume the V2 basis, reductions, or witness file.

## 3. Sharp power sandwich and valuation conventions

Combining the separate lower containment with (2.2) gives the exact power
sandwich

```text
J^5 subset I subset J^2,                                  (3.1)
J^(5n) subset I^n subset J^(2n)       for every n>=1.      (3.2)
```

For a Krull valuation `v` of `Frac(A)` centered on `A`, set `v(0)=infinity`
and, for a finitely generated nonzero ideal `L=(g1,...,gs)`, set

```text
v(L)=min_i v(gi).
```

Centeredness makes this equal to the infimum over all elements of `L`;
inclusion reverses ideal value, products add, and `v(L^n)=n v(L)`.  Therefore
(3.1) gives

```text
2 v(J) <= v(I) <= 5 v(J) <= 17 v(J).                     (3.3)
```

This proves the requested `2v(J)<=v(I)<=17v(J)` and sharpens its
power-containment upper constant from 17 to 5.  For a centered semivaluation
that may kill every generator, use the extended convention `n*infinity =
infinity`; `I subset J^2` then forces `v(I)=infinity` when `v(J)=infinity`, so
the same inequalities remain valid.  Minimality of the ideal-power exponent
does not assert that some valuation attains ratio 5, and no integral-closure
or Rees-valuation classification is claimed.

## 4. Full initial ideal versus seven generator initials

Write the exact normal coordinates as `(e0,e1,e2,e5)` and tangential
coordinates as `(S,T)`.  Because `I subset J^2`, each chosen row has a
well-defined degree-two `J`-initial form `Qi`.  Let

```text
K2=(Q1,...,Q7) subset gr_J(A)=Q[S,T,e0,e1,e2,e5].
```

This is only the ideal generated by the seven chosen row initials.  The full
initial ideal is

```text
in_J(I)=direct_sum_n ((I intersect J^n)+J^(n+1))/J^(n+1),
```

and it contains initial forms of every element of `I`, including cancellations
and higher consequences.  From `J^5 subset I`, it contains the entire
degree-five ideal `(e0,e1,e2,e5)^5`, not merely four pure fifth powers.

V2 and the fresh replay independently carry the seven literal rows and
`f0^5` together across the source/target ring change.  At `S=T=0`, on

```text
P0: e0=4e2, e5=-2e1,
```

the scaled image of every row is divisible by `l^3`; hence every `Qi`
vanishes identically on `P0`.  But the full-initial-ideal element `e0^5`
restricts to `4^5 e2^5`, which is nonzero.  Therefore

```text
(Q1,...,Q7) is strictly contained in in_J(I).              (4.1)
```

This exactly refutes the possibility that the seven quadratic generator
initials generate the full `J`-adic initial ideal.

## 5. The actual normal cone

Put `B=A/I` and `K=J/I`.  The theorem gives

```text
K^5=0,                 K^4 != 0.                           (5.1)
```

The second assertion is witnessed by the class of `f5^4`.  Thus the positive
ideal of

```text
gr_K(B)=direct_sum_(n>=0) K^n/K^(n+1)
```

is nilpotent of exact index five.  Every homogeneous prime contains that
nilpotent irrelevant ideal, so

```text
Proj(gr_K(B)) = empty                                     (5.2)
```

everywhere over `Spec(A/J)`, and after every base change.  The affine normal
cone `Spec(gr_K(B))` need not be empty: it is a nilpotent thickening supported
on the zero section.  Its projectivization is nevertheless empty.

Accordingly, the literal Opus phrase identifying nonzero solutions of the
seven quadrics with points of the actual projectivized normal cone is false.
If separately reviewed, its quartic can govern only degeneracy of the
**seven-generator quadratic leading system**, not nonemptiness of (5.2).
This report neither verifies nor promotes that quartic, its geometry, or its
other proposed clients.

## 6. AWS evidence, fail-closed incidents, and custody

All evidence runs used exact characteristic zero in Singular 4.3.2 on
campaign r6b, `i-0f089e64c378f5da3`, boot
`3dca2ad4-9cbb-48f9-9c62-02d37a90bd19`.  No modular result or `msolve` output
is used.

Clean V2:

```text
packet manifest   1f9d20032efe7713ab18cd8ec742d0d658220a9b8389b57cfecc17b436bba720
payload manifest  214df908cf7de2466e0f35f35ed8324574e88ea0057b022d6da37b919b5778eb
runner             4e1c20b7af2e31b8ebf55cfcbbf0383735e3802c3e6085fd3878e8b7762bdc75
results manifest  b4ecb6c3f02c4167610398b2b51e89e5d978121a7d37b4a282a87d8aeb9eb72e
search stdout      d9a688b1c2bc35021d2b7e6b24b0313c09bea78aff30016808febc139ba8d36f
search telemetry   4e8aaed19a31675d824c9f1af161e3c4332786735aadf8fb7116b808ecfda634
initial stdout     003406453e28fa6dcd580f5c1329d1d38506b5f9bd3362493d77556f24caf4b6
```

V2 Singular PID/PGID 40181 ran 517.001612087 seconds with maximum observed
aggregate RSS 28,372,992 bytes.  The separate initial check ran as PID/PGID
45566 in 0.114348951 seconds.  Both were normal zero exits, with empty stderr,
no TERM/KILL, unique expected endpoints, and no generic Singular diagnostic.

Clean triangular replay B:

```text
packet manifest   7ac2b7b8a101fc3c06d7ed3490aa79d2f546cf6a9a8d25972a99d34bdbd206a3
payload manifest  1e4dd78bea3f9ba987920a3b5ce1a6dd2c4ae3bdd7ad026981649da992fb7ee3
runner             3d214809dc0dddd84f894f3485ce6c5dd44ec148bc6d831480d98d8fa62cf85f
results manifest  a87bd33d12e7f4c16732a29e664f924f7414d411a985a6304e914b9d7c8c3b80
replay stdout      35221f5fc0fa96fa8c4d7c43fa6ddfbd7f76e10c83b8c9132c039dddb8fee5d4
replay telemetry   f2e598e0e584d043834802376639deff529c33f7416ef18842d59bcf4a961818
witness / NF       506906933fa5edea812e03a30ea0338b7331160aa5d98ac008ecc9aab2da60d1
                   7170a65f260c1db33d9a9ad12037e0458e94207999bb303f7575bd2838431260
```

Replay PID/PGID 47764 ran 0.434013231 seconds with maximum observed aggregate
RSS 25,501,696 bytes; its separate initial replay ran as PID/PGID 47792.  All
registered descendants were absent after completion.

Both clean routes first ran a planted undefined-symbol script that returned
zero and printed a fake PASS.  The same validator used for evidence rejected
it with the preregistered diagnostic status 41.  Two real defects were also
kept fail-closed:

- V1 referenced an out-of-scope `f0` after a ring switch; Singular continued
  to PASS, exposing a missing generic-diagnostic check.  Every V1 line is
  quarantined.  Sealed receipt full
  `e241964c2714a71b721ad57c260f01aa2fe281032f86cb571490cac6a7df3d7f`,
  body 2417 / `8b8f5cbcb79f550b82e759662da1ccd747b693c136d9ce1c2f4d1bae0053e711`.
- Replay A used reserved identifier `IN`; the repaired validator rejected 28
  diagnostic matches despite downstream PASS text.  Sealed receipt full
  `58d8aa187ed98c4c47cc377afbdeda5ed850709b4d360c9693c0cb20843e1179`,
  body 1606 / `fd2db8d702a1cf82d8a6027a8b1f6247f36536614c98c72ee6dea76088d8d796`.

Neither rejected process is used as calibration or evidence.  The 25-entry
evidence manifest is
`cases/max12_812_order2_u2_62_k00_rees_sandwich_20260829/EVIDENCE_CUSTODY.sha256`,
SHA-256
`a623fea9b7f806049703f0d7c5b6dbc43a00579c1982d20c9974a6952f9fc198`.

After preservation, r6b was audited at zero CAS processes and zero sessions,
then tagged `ActiveJob=IDLE`, `OwnerTask=unclaimed`; the running instance was
not stopped.  No other AWS host was touched.

## 7. Maximum safe theorem and firewalls

The integration-ready maximum is exactly:

```text
sqrt(I)=J,  I subset J^2,  I not subset J^3,
J^5 subset I,  J^4 not subset I (witness f5^4),
least N with J^N subset I is 5,
2v(J) <= v(I) <= 5v(J) for centered valuations,
(Q1,...,Q7) proper-subset in_J(I),
Proj(gr_(J/I)(A/I)) is empty and its positive ideal has index 5.
```

This is a theorem about one frozen unloaded ideal.  It does not compute the
full set of generators of `in_J(I)`, the Rees valuations, integral closures,
or a filtered standard basis.  It does not set the literal loaded source to
zero, identify a quadratic direction with an attained scheme point, prove a
cell or formal arc, establish closure incidence or all-order lifting,
algebraize a trajectory, construct a polynomial map, or decide JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12138`.
- Body SHA-256:
  `20f8ed14cec710fa6f389bc75e75ed565eef408fcf9d8f0930ef885cb9f00d1f`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
