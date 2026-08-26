# TD6 V83 — exact generic FIRST principal open

Status: **dual-AWS producer PASS; proof-grade selected-minor certificate;
hostile review pending.**

The source-replayed packed FIRST map has a certified `38x38` selected minor.
After removing constant field units, its principal-open factorization is

```text
U^4 * (C-3U^2)^2 * B3 * R38,

R38 = C*V^2*U + 8*C*U^4 - (1/2)*V^4
      - 7*V^2*U^3 + 8*U^6.
```

The full packed-matrix denominator uses only `U` and `C-3U^2`.  Consequently
FIRST is certainly surjective on

```text
D(U * (C-3U^2) * B3 * R38).
```

The extra divisor `R38=0` is an exact raw-fibre/alternate-minor debt.  This
selected minor does **not** prove that rank drops everywhere on `R38=0`; a
different minor may cover part or all of it.  In particular, the earlier
generic-rank corollary must not be silently identified with `D(U*H*B3)`.

Both registered AWS hosts returned rc zero from the same source archive.  The
three exact ledgers are byte-identical.  Mathematical stdout is byte-identical
after deleting only `aws_hostname` and `aws_run_tag`; timing stderr is retained
separately.  `verify.py` checks archive/source closure, custody hashes, this
normalization, the principal factor ledger, controls, and PASS marker without
rerunning the algebra.

`V83A_STALE_LOCAL_LAUNCHER_NEGATIVE.txt` records an unrelated malformed local
SSH launcher that reached no producer computation.  V83B is the only
mathematical evidence consumed here.

Scope is the fixed source-typed A3 presentation and its symbolic center field.
No statement is made on the unresolved `R38=0` fibre, at quadratic order, for
a nonlinear family, for full TD6/SP-2, or for JC2.

