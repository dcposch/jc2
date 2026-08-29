# K3 V4 generic-open result

Date: 2026-08-26

Status: **dual-AWS producer PASS; ordinary `rho`-correction chart only.**

Both exact Q and characteristic 32003 passed every source, reduced-support,
`rho^7` divisibility, multiplication-back, forbidden-variable, lower-load,
terminal-target, and fail-closed validation sentinel.  Over the coefficient
field `Q(b,t,C,S)`, eliminating all ten first-correction variables from the
seven affine-linear K3 rows gives

```text
DISC_TRIPLE_K3_ELIM_DIM=-1
DISC_TRIPLE_K3_ELIM_UNIT=1
DISC_TRIPLE_K3_ELIM_BASIS_BEGIN
1
DISC_TRIPLE_K3_ELIM_BASIS_END
```

The good-prime lane gives the same endpoint.  Thus the ordinary next
correction chart through the reduced triple-root K2 survivor is empty at its
generic point on `D(b*t)`.

This does **not** eliminate ramified/weighted corrections.  In particular,
the raw K2 ideal contains the doubled normal `U^2`; a Puiseux ray with
`rho=sigma^2`, `U~sigma`, and the three linear normals of order `sigma^2`
is not represented by the V4 ansatz and remains the decisive successor.
V4 also says nothing about parameter divisors, Taylor realization, or an
order-two verdict.

Exact-Q stdout SHA-256:
`ca31479fee49003d3740b6a19d074c19d5b55c2e37dc492e9c48729bdd24ef65`.
Good-prime stdout SHA-256:
`510eb0c28615e247227d13bc9ef6b9e1b993b115c411f08d701e4e51350785f7`.
Both validation files have SHA-256
`a88f4900464020905a5c3b8cfd0f70e8c6dfa6e0dcb3cd95ae2554dc2eccfa82`.
The complete custody manifest is `RESULTS.sha256`.
