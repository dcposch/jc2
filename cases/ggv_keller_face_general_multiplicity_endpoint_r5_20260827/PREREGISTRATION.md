# R5 preregistration: general multiplicities and the rational endpoint

Date: 2026-08-27

## Charged theorem

Let `K` have characteristic zero, let `H in K[X]` be nonzero and
nonconstant, and let `F,G in K[X][[t]]` satisfy `F0=H^2`, `G0=H^3`.  For

```text
E=12F_XG-8FG_X-t(F_XG_t-F_tG_X),
```

classify every rational homogeneous mode below weight 22 using the
multiplicities of the irreducible factors of `H`.  After exact mode
subtraction, reduce a prospective `E=t^22+O(t^23)` endpoint to the audited
rational ODE and combine it with the squarefree decomposition `H=A^2B`.

The maximum result is a necessary exclusion criterion for this formal
`H^2/H^3` edge.  It is not a sufficient construction, raw-source landing,
GGV-family theorem, `G2-PSC`, `G2-BD`, cofinal statement, or JC2 result.

## Preregistered checks

1. At weight `n`, with `q=(12-n)/4`, a rational kernel exists exactly when
   `q*e_p` is integral for every irreducible-factor multiplicity `e_p`.
2. The leading kernel lifts to an exact mode using
   `t^n R_q (F/H^2)^((12-n)/8)`, where
   `R_q=product p^(q e_p)`.
3. At weight 22, with `g=-8H^2d`, the inhomogeneous endpoint is
   `2Hg'+H'g=2H`.
4. If `H=A^2B`, `B` squarefree, rational solvability is equivalent to
   `A=Bv'+(3/2)B'v` for a polynomial `v`.
5. For `deg H=8`, squarefree-part degree `b>=4` is excluded by degree;
   only `b=0,2` survive the degree-only filter.  In the normalized quadratic
   case `B=z^2-D`, `A=a3 z^3+a2 z^2+a1 z+a0`, the remaining condition is
   `4a0+D*a2=0`.

## Stop rules

- Stop at any failure of exact mode lifting, especially a scalar-root or
  infinity issue.
- Keep perfect-square `B=1` as endpoint-silent, not excluded.
- Do not infer a polynomial jet from a rational endpoint solution.
- Do not consume the provisional R4 producer as promoted evidence.

