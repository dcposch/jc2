# Erratum R1 — edgewise non-`V_{2,a}` certificate

Date: 2026-08-29  
Coordinator: Sol 5.6  
Frozen source review:
`f9dd2035bbe5a47561cce263ba1288a9245526dec748c3ef031545e443bf510f`
(body `1ca3948f97114d56e1c5aae916fa086d459d036550f2e218bcf31923710c3e12`)

## Correction

The fourth item under “Maximum safe promotion” in the frozen Fable5 review
contains one missing negation.  Its phrase

```text
edgewise-V_{2,a}
```

must read

```text
edgewise-notin-V_{2,a}.
```

The review's controlling compiler audit A9 already states the correct
hypothesis: every child on the relevant segment must carry an edgewise
`notin V_{2,a}` certificate.  This is also the hypothesis used by the
canonical `AUDIT.md` compiler rule.  A dirty `V_{2,a}` edge is precisely why
merge-free M-descent failed, so the unnegated phrase cannot be a valid
alternative reading.

No formula, floor, route verdict, downstream computation, or canonical
mathematical conclusion changes.  The frozen review remains immutable; this
erratum resolves only its internally contradictory summary phrase.

## Scope

This erratum does not promote strong ASM for an uncertified arrival.  The
strong consumer remains attachable only with a pole-adjacent arrival, an
edgewise-`notin V_{2,a}` certificate for every child on the segment, or a
directly certified `M_H | b_P`.

## Seal

- Body length: `1335` bytes (all bytes before this heading).
- Body SHA-256: `26631d03b002cc47e709e5a71d03d7467ea3547be2f1cef661af97abdb1cd882`.
