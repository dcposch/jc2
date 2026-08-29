# V82QSF nested CURRENT-denominator identity — producer report

## Verdict

Dual exact AWS replay confirms that the three V82QSD foreign factors form a
nested algebraic chain.  In `Q[C,V,U]`, with

```text
F = C U - V^2 + U^3,
```

the exact identities are

```text
G = V^4 + 4 F^2,

L = 4 U^3 G^2
    + V^4 (V^2+4U^3) (V^2+2F)^2.
```

The two independently run hosts emit identical expression digests:

- `G`: `9b3db39ea758ae5b5728fe292a7f521ed0ddd7ba8d96a4c989b2f73bcf29ffd2`;
- `L` and the nested right-hand side:
  `f1dc497af30151f2a6c13c74371e34b407e8e3f0323fa78e1ff9522db820de3a`.

On `D(U)`, put `x=V^2/U^3`, `s=F/U^3`, and `g=x^2+4s^2`.  Exact replay also
confirms

```text
L/U^15 = 64s^4 + 4x^2(x+12)s^2 + 4x^3(x+4)s + x^4(x+8)
       = 4g^2 + x^2(x+4)(x+2s)^2.
```

The normalized expression digest is
`aace451b632deb946ad37d9ff1d2ca59a1d025943901af0a3e372d6365c71779`.

## Exact divisor consequences

These are consequences for the denominator divisor only, not source-fibre
theorems.

- On `F=0`, exact principal-ideal division gives
  `L=V^8(V^2+8U^3)`.  The quotient certificate has SHA-256
  `07f66e75d21e96bba1bea174c540b78817cd71736b3a814a04b5ad0ba7cd4676`.
- On `G=0`, `L=V^4(V^2+4U^3)(V^2+2F)^2`.
- The apparent last branch collapses set-theoretically: for
  `A=V^2+2F`, exact replay proves
  `G-A^2+2AV^2=2V^4`.  Hence `G=A=0` forces `V=0`, then `F=0` in
  characteristic zero.
- Equivalently on `D(U)`, for `a=x+2s`,
  `g-a^2+2ax=2x^2`.  Thus the radical of the normalized intersection
  `g=L/U^15=0` is covered by the two finite branches `x=0` and `x=-4`.

This turns the presentation debt from three unrelated factors into a recursive
finite divisor tree.  The next proof-grade step is still an original-source
CURRENT rebuild on the corresponding raw branches (including their
intersections), or a denominator-free source identity with explicit glue.

## Scope firewall

V82QSF checks polynomial identities and their denominator stratification only.
It does not establish that any q2..q10 CURRENT coefficient survives or
vanishes, that a raw fibre is empty, or that the presentation opens cover the
source scheme.  No family, TD6, SP-2, landing, or JC2 inference follows.
