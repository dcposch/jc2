# Negative result: raw direct-unit cone `15<H<18` is false

Date: 2026-08-26

Status: **DUAL-AWS FAIL-CLOSED MATHEMATICAL NEGATIVE.  NO EXCLUSION
THEOREM.**

Both frozen lanes (`Box03`, exact-Q coefficients; `r6d`, F65521 exponent
control) returned `engine_rc=1` at the preregistered unsafe-support gate.
The exponent sequences agree, and the same list of graph-relative support
terms violates the proposed endpoint inequalities.

At

```text
alpha=H/3,       q=21-H,       complements=2q,
```

the term

```text
-(3/8)*X^2*a*lambda^2*M^2
```

has weight difference from the intrinsic cubic

```text
(2H+2q+alpha)-3H = 42-(8/3)H.
```

It therefore crosses at `H=63/4`, strictly inside the proposed open band.
Other exact violators include `K10*X^3`, complement/kernel terms, and the
first transverse graph deviations.  Thus imposing only the leading
grade-42 affine graph does not make the intrinsic cubic the next universal
unit for every `q>21-H`.

This negative does not exhibit a surviving source arc.  The offending terms
belong to later predecessor faces.  The correction-aware successor must
iterate:

```text
q<21-H:  unloaded quadratic block before grade 42;
q=21-H:  combined affine-graph/quadratic grade-42 block;
q>21-H:  next graph-deviation or quadratic face, with its raw predecessor,
          before applying the cubic functional.
```

The two AWS stderr files are the controlling outputs; stdout is empty
because the analyzer deliberately raises on the first false conjecture.
No local CAS was run.
