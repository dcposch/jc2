# Opus 5 primary research — exact splitting of the D43 coefficient algebra

Work independently in `/Users/dc/code/math/jc2`. Do not enter, list, search,
read, build, modify, status-check, or control `jc2-lean`. Do not use the web,
AWS, or heavy local computation. Short exact desk calculations and light
shell/source inspection are allowed. Write only the requested report.

Read these charged sources completely:

- `xmodel/d43-seven-w-elimination-algorithm-grok46-20260828.md`
- `xmodel/d43-a00pp-tail-elimination-independent-audit-gpt56-r1-20260828.md`
- `xmodel/d43-direct-exact-sparse-source-preflight-gpt56-20260828-v2.md`
- the coefficient-algebra definitions in
  `cases/d43_exact_sparse_rows_v2_20260828/selected_rows_v2.py`

The exact algebra is

```text
K0 = Q[zeta42,r3,A1,A2,h]/
 (Phi42(zeta42), r3^2-3, A1^3-(3+r3), A2^3-(3-r3), 2h^2-3).
```

Determine, with proof rather than heuristic, whether `K0` is a field. If it
is not, give the complete product decomposition and explicit primitive
idempotents. If it is, give a rigorous irreducibility/linear-disjointness
proof and an explicit primitive element or certified tower. In either case:

1. identify the degree-48 base generated before `A1,A2` (and verify or refute
   its cyclotomic description);
2. decide the two Kummer cubic classes over that base, including every
   possible relation in `B^*/B^{*3}`;
3. prove finite etaleness/reducedness and locate the ramified rational primes;
4. map both registered finite-field frames to the resulting factor(s);
5. design a small exact PARI/GP certificate whose output can be independently
   replayed on AWS, including factor/minimal-polynomial and inverse-map checks;
6. state exactly how the answer changes the component-safe Fitting solve.

Do not call a 432-dimensional presentation a field without proving it. Do
not infer characteristic-zero irreducibility from the two modular frames.
Separate theorem, conditional claim, and computational recipe.

Write exactly:

```text
xmodel/d43-k0-splitting-primary-research-opus5-20260828.md
```

