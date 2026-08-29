# Registration: sharpened square third tail V2

Date: 2026-08-26

V1 is preserved as a four-lane deployment negative: its generated Singular
used an unavailable `coeff(poly,var,degree)` API, every validator failed, and
it has no mathematical endpoint.

V2 changes only coefficient extraction.  It uses iterated differentiation,
specialization at zero, and division by the exact factorial.  A known sparse
polynomial self-control checks degrees zero through three before any source
row identity is accepted.  All source substitutions, Laurent reversal,
Faber transform, configurations, fields, and mathematical sentinels are those
of V1.

Run `generic` and `p0moving` over exact `Q` and independently over
`F_65521` on registered AWS hosts.  No modular endpoint carries a
characteristic-zero conclusion.
