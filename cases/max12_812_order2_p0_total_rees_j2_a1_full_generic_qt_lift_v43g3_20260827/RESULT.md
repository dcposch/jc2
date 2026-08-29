# V43G3 tracked generic multiplier result

Date: 2026-08-27

Status: **PASS; exact 58-row Bezout identity over `Q(t)` replayed.**

The frozen r6a compiler independently regenerated all 59 literal total rows,
rechecked the exact `Tg19_2 : (3/8)t*a1*ez9` pivot, and byte-compared the
64-variable ring declaration and every one of the 58 reduced ideal entries to
the frozen V43G2 decision script.  All comparisons passed.

Singular then returned a one-element basis and passed both exact matrix
identities

`matrix(J)*T = matrix(G)` and `matrix(J)*C = [1]`

over `Q(t)`.  Eleven of the 58 saved multipliers are nonzero, on rows

`Tg11_2, Tg11_7, Tg12_2, Tg12_7, Tg13_5, Tg13_7, Tg14_5, Tg14_7,
 Tg15_3, Tg15_5, Tg15_7`.

The other 47 reduced-row multipliers and the original pivot-row multiplier
are exactly zero.  The raw nonzero multiplier files show only monomial
denominators in `t`; their common `t`-valuation is at most six.  Denominator
clearing, minimal-support tests, and total rehomogeneous replay are successor
gates and are not promoted by this report alone.

## Custody and resources

- frozen source-manifest SHA-256:
  `d9ac8ba653be384740b4b313cab99196bd174716a36056a8ada04b41355aef14`;
- compiler-result SHA-256:
  `1c00aef261a3d674cb1b63f4fad18cf0121b9bcb6711a2103e893bab7a83758e`;
- generated Singular SHA-256:
  `0bca5e57db93e620c8f1f9ad52ea50b3f16ab4d01ad0326cab96009bbe803893`;
- remote evidence-manifest SHA-256:
  `1cdccc0e004efaf600cefbefd31482111a38972176c54a59613a2c4cd1ede401`;
- local harvest-manifest SHA-256:
  `dfe68abf0ba646b89e51b9c9ec8375af0a51f2918143dedfc9b5b39ee973450a`.

Source reconstruction used 230.22 seconds and 147,168 KiB peak RSS.  The
exact `liftstd`/replay used 0.13 seconds and 25,820 KiB peak RSS.  Both exited
zero with no swap and no diagnostic marker.

The matrix text files emitted directly by Singular are not used as evidence:
Singular serializes these matrix objects as `0` under this `write` call.  The
58 individually written polynomial multipliers are the authoritative saved
coefficients, while the in-process exact matrix product and terminal markers
certify their common origin.  The successor independently reparses those 58
files and replays their full product.

This is still a generic-fibre identity.  It is not an unrestricted total
certificate until the polynomial-denominator, sigma projection,
rehomogenization, and special-converter stages pass.
