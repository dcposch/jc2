# Hostile review case: deep upper endpoint licensed q1/q3 composition

Independent different-model (Fable 5) audit of

```text
xmodel/ggv-upper-endpoint-deep-q1-q3-composition-sol-ultra-20260828.md
sha256 6958c3986022e28484ea1a0a15a0b09a562dbd94cc2154ade4fe6dbc35000715
```

Verdict: **REPAIR** — all displayed identities (1)–(5), (8)–(14)
CONFIRMED by full symbolic recomputation over exact rationals; defects:

- **D1** (normalization REPAIR): "primitive `p*c/512`, rescaling
  `C=256c`" is off by exactly 512 against ODE (11); correct primitive is
  `pC/256`.  No downstream impact.
- **D2** (localization REPAIR): (11) starts from `C in K[X,1/A]`
  unjustified; poles away from `A` must first be excluded via the
  `-2m*A(beta)` leading coefficient.  One-line repair, no impact.
- **D3** (hypothesis note): the deep condition also uses `A|T` (`T=AU`),
  embedded in the displayed prefix (6) but not named in §1.

Full findings: see
`xmodel/ggv-upper-endpoint-deep-q1-q3-composition-hostile-review-fable5-20260828.md`.

## Replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  xmodel/ggv-upper-endpoint-deep-q1-q3-composition-hostile-review-fable5-20260828-check.py
```

Expected tail:

```text
OVERALL: ALL 32 CHECKS PASS (6 mutations detected; squarefree and D12 load-bearing controls held)
```

The checker is standard-library only (Fraction sparse multivariate
polynomials, exact truncated series), imports no producer checker, and
includes mutation controls for: two q3 binomial coefficients
(`11/512 -> 12/512`, `-3/32 -> -1/8`), the ODE normalization
(factor-512 detection), D12 omission (`r` unresolved; `U=48A'` q3-passing
counterexample), and the final `U`/`L` constants (`9lam^3/2 -> 9lam^3/4`,
`6lam^2 -> 3lam^2`).  Load-bearing controls: non-squarefree `A=X^4`
admits the rational ODE solution `C=1/X`, and the q1 kernel jumps from
dimension 1 to 4.

`check_output.log` is the frozen full output of the replay command above.
The same-model downstream addendum
`ggv-upper-endpoint-deep-q1-composition-addendum-r1-sol-ultra-20260828.md`
was not read; `jc2-lean` was not entered; no frozen input byte modified.

## Manifests

- `SOURCE.sha256` — frozen inputs (target + four reviewed upstream atoms
  + upstream checker), repo-root-relative.
- `EVIDENCE.sha256` — final produced bytes (review, checker, this README,
  RESULT.json, check_output.log, SOURCE.sha256), repo-root-relative,
  non-self-referential.
