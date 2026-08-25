# Max12 `(9,12)` selected-Q8 candidate at the corrected-Q8 boundary

Date: 2026-08-25  
Status: **producer-exact projection theorem; lifted-component consequence pending**

## 1. Exact statement

Let `H(w,v)` be the pinned monic degree-190 candidate over `F_127`
reconstructed from the 123 primitive nonzero selected-Q8 fibres.  Let
`Q8bar(v)` be the monic reduction modulo 127 of the corrected Q8 contact
octic.  Exact dense polynomial arithmetic gives

```text
H(0,v) = Q8bar(v) C(v),        deg C = 182,
gcd(Q8bar,C) = 1,              gcd(Q8bar,Q8bar') = 1.       (1.1)
```

The second division has nonzero remainder of degree seven, so `Q8bar`
occurs with multiplicity exactly one.  Equivalently,

```text
gcd(Q8bar, (partial H / partial v)(0,v)) = 1.              (1.2)
```

Thus, over the algebraic closure of `F_127`, the plane hypersurface `H=0`
contains all eight corrected-Q8 `(w,v)` projection points `(0,alpha)`, and
it is smooth in the `v` direction at every one.  In particular each point
has a unique formal `H=0` branch with `w` as a local parameter.

## 2. Why this is strategically useful

The reviewed contact-grouping theorem says that the eight corrected-Q8
contacts lie either on one selected geometric component or on eight
singleton components.  A separately certified rational reconstruction of
the other seven quotient coordinates, followed by direct substitution in
the original eight rows modulo `H`, would turn `H=0` into an actual
irreducible quotient-curve component.  If its coordinate functions have
the corrected finite limits at all eight roots of `Q8bar`, (1.1)--(1.2)
would put all eight contacts on that one component.  The reviewed infinity
passport theorem already excludes an actual trajectory on such an
eight-contact component.

This route may therefore avoid proving that the degree-190 component is the
*entire* generic quotient.  It still requires all of the italicized lifted
component and coordinate-limit statements; the present projection result
does not supply them.

## 3. Exact provenance

AWS Box02 lane `q8_p127_candidate_q8_boundary_v1` on
`ip-172-30-0-186` returned `rc=0` with empty stderr.  The returned result is

```text
result.json  181cabca21843cb0263b840ce3d11f10bbfb502e4db6dfa1fea62303f9e58e6e
stderr.log   e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
replay.py    a8a967ae64aa173980aeb54d47d27c4b9f9e194bb1260295d5d00faac630385f
runner       7193b16b1f01256ac1b44e3191ad18ea2deca80bf30066ea1d1604aac6e1ea8e
candidate    9061726295086f58f74f3751b2f7c2d59c5cb86de5e53ecd636687fd54daa7ce
```

The monic corrected octic modulo 127 has low-to-high coefficients

```text
[106,122,106,126,72,61,60,29,1].                       (3.1)
```

The dense hashes of `H(0,v)` and `C(v)` are respectively
`44355245fae62592de0b209ad9d4b6353d1adff0ba81c3d1138ac2909ca47491`
and `c9ff012798ff6b168464e223a4021f190fe27836323315b38e8093ca65797433`.

## 4. Scope firewall

This report proves an exact statement only in the `(w,v)` projection modulo
127.  It does not prove generic ideal membership, construct the other seven
coordinates, control their limits at `w=0`, prove that `H=0` is a component
of the selected-Q8 quotient, lift a component to characteristic zero,
exclude a `(9,12)` trajectory, close maximum twelve, or prove JC2.

