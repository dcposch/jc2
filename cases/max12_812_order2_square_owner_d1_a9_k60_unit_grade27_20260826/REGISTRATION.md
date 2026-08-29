# Registration: D1 `a=9`, `D(k60)` grade-27 obstruction

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS EXACT-SOURCE PRODUCER; NO RESULT YET.**

## Question

On the already registered fixed-contact D1 chart

```text
ord_sigma(A)=9,  ord_sigma(C)=10,  ord_sigma(R)>=9,
```

with `p*k0 != 0`, does the corrected, literal-Faber, complete-source `a=9`
census already exclude the additional open `k60 != 0`?

The leading coefficient of

```text
C=sigma^10 ((c1 z+c0)+O(sigma))
```

is required to be nonzero, so the exact-contact chart is the complement of
`V(c1,c0)`.

## Frozen ancestry

This client imports and reruns the parenthesized-load V3 compiler.  It pins:

- V3 compiler SHA-256
  `0f7b9482f214347858f61181119f52fc434de8223ae7a3c4099049bd737897ef`;
- V3 registration SHA-256
  `a88cc145baaa6612b73e0d44df0e012fcc99d531d50bbe8879a081449eb51b3b`;
- V3 result SHA-256
  `88609fdfc50b89625f79e7dcee3b8ceb47d61c3b6668e86ee80da67ad4129e24`;
- V3 freeze SHA-256
  `7016cdba48152e5e44b285a56812f2b2e077f110cc6e5baa5adbbe9d184d2432`;
- V3 evidence SHA-256
  `d2e5d59f94d3489fd8bd3509fd0ece0dc2456c234173f5023ebad2f201bb3c06`.

The quarantined V2 census is transitive negative custody only and is not a
mathematical input.

## Acceptance tests

The generated Singular client must verify, directly from the corrected full
source, all seven grade-27 identities

```text
g27 = ((3/4)c1*k60, (3/4)c0*k60, -(3/16)p*c1*k60, 0,
       -(3/128)p^2*c1*k60, 0, -(3/512)p^3*c1*k60).
```

It must also retain and verify:

- the grade-28 moving-connection term in row 3 and the complete `k60_1`
  terms in rows 1--3;
- the grade-28 `mu20` target;
- the grade-31 `k20` and `k0_1` coefficients;
- the literal later targets `mu4`, `mu6`, and `J/4` in the unreduced full
  source;
- zero source rows below grade 27 and exact recursive division.

In a fresh compact ring, adjoining inverses of `p,k0,k60` and Bezout
coordinates for `(c1,c0) != (0,0)` must make the two leading equations the
unit ideal.  A Chebyshev/Pell identity for `Q=z^4-1` is a positive control
against accidental blanket square forcing.

## Placement

Run exact Q on Box03 and `F_65521` on r6d, each with a 16-GiB virtual-memory
cap, 600-second compiler cap, and 1800-second Singular cap.  Reject any
diagnostic, timeout, missing/nonunique sentinel, nonzero engine exit, or swap.

## Firewall

A PASS excludes only this fixed-contact `a=9` chart on
`D(p*k0*k60)`.  It says nothing about `V(k60)`, moving/raised contact, any
other D1 valuation, the whole square component, order two, `(8,12)`,
maximum-twelve, or JC2.

