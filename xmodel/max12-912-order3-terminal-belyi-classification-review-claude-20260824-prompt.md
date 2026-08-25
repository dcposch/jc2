# Hostile review — selected-Q8 terminal Belyi classification

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`. Treat every existing producer, case, canonical,
coordination, prompt, log, run, and review byte as immutable. Do not use Bash
or run any local computation. Read in full:

- `xmodel/max12-912-order3-terminal-belyi-classification-20260824.md`;
- every file in
  `cases/max12_912_order3_terminal_belyi_classification_20260824/`;
- the reviewed global-quotient parent cited by its registration, only as
  needed to audit the imported hypotheses.

Charged hashes:

```text
report       5d8806db54eb2056dd7aafe6fb7dc342c68be1bef7cba06b96beeeaa765273fc
manifest     ff7e065845f064cf1cb25b35dea053dee5c72ee0540bf46a8f901d131b582b33
freeze       0c5b862fd4f784e3e258881c39a16dbd14d3c53f9aafe9426cfec8102f5018d9
replay       495844f1d51c0f230223d143f36b54679865244581fb60974c268da4c756a4bb
AWS output   4697899b8ba8e4780db56a7318911e4e463d9f0db4cea00392098a4f530c894e
```

The replay was independently run on AWS r6d with exit zero and empty stderr;
do not rerun it locally. Inspect the source and frozen output rather than
trusting PASS. Independently attack:

1. The valuation argument from
   `nu^10 h^3 (Z')^9 = j^9 Z^8` to `3 | ord_a(Z)` at every finite point,
   including the `ord_a(Z)=0` case, and the transfer to infinity/divisor
   degree. Check that algebraic closedness really yields `Z=T^3` in `C(x)`.
2. The cancellation leading to `h=C*T^2/(T')^3`. Look for lost zero or pole
   cases, constant `T`, or an illicit cube-root choice.
3. For reduced `T=A/B`, derive `W=A'B-AB'`, all local orders at roots of
   `A` and `B`, the exact finite polynomiality criterion, and the cube-class
   assertion `[h]=[T^2]`. Check every use of coprimality and characteristic
   zero.
4. Both infinity strata. In the unequal-degree case verify
   `deg W=a+b-1`, `r+s=1`, the pure-power classification, and that
   `3|deg(h)` plus noncube really excludes every such case. In the balanced
   case verify the definition/range of `e`, `deg W=2D-e-1`,
   `r+s=e+1`, and `deg h=3(e+1)`.
5. The claimed three-value Belyi passport and complete Riemann--Hurwitz
   count. Search for hidden ramification over `lambda=T(infinity)`, missing
   finite critical points, inseparability, cancellation at infinity, or an
   omitted fourth branch value.
6. The positive controls and strict logical scope. This is only a necessary
   classification on the selected corrected-Q8 `k=mu=0, nu!=0` branch. It
   must not claim coefficient-fibre realization, Taylor integrality, global
   trajectory existence/nonexistence, maximum-twelve exclusion, or JC2.

State the smallest false identity or missing hypothesis if one exists. Give
the exact promotable sentence and its strict scope. Write exactly
`xmodel/max12-912-order3-terminal-belyi-classification-review-claude-20260824.md`.
Do not edit any other file. End with exactly one verdict: `CONFIRMED`, `GAP`,
or `REFUTED`.
