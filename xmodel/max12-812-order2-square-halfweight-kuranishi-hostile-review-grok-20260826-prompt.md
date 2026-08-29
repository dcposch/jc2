You are the independent hostile referee for a correction-aware normalized-ray
calculation in the `jc2` repository. Work text-only. Do not run Singular,
Sage, msolve, Lean, the package compiler, or any other substantive algebra
program. You may read files, recompute SHA-256 hashes, inspect already-emitted
records, and check the displayed small identities by hand. Do not edit any
existing file.

Primary targets, with required byte hashes:

```text
37a7234cee998a0069f33b7a36bb945123b305acd01485a771d8e6ed7dac65fd
  xmodel/max12-812-order2-generic-square-halfweight-kuranishi-design-20260826.md
eb2cd8036a0fbf87a1ff7a58c116346b11973efc47f35f9cb76105a6ccd485af
  cases/max12_812_order2_square_halfweight_kuranishi_20260826/RESULTS.md
ee4718fc24ae451f8f86c05e9c4eeae83215835e7cff5fdc8eccc54b9f881677
  cases/max12_812_order2_square_halfweight_kuranishi_20260826/FREEZE.sha256
a41a704b44cd4a3e456edd1e214d4d872f9d151bb43336f46a22a19b1a8c7d37
  cases/max12_812_order2_square_halfweight_kuranishi_20260826/RESULTS.sha256
```

Read both prose targets in full. Verify both manifests and every evidence
file they name. Also read these scope predecessors completely:

```text
xmodel/max12-812-order2-square-third-tail-divisibility-theorem-20260826.md
xmodel/max12-812-order2-generic-square-load-ladder-design-20260826.md
cases/max12_812_order2_square_load_ladder_20260826/RESULTS.md
xmodel/cross-pollination-order2-square-normalized-rees-20260826T0640Z.md
```

Attack the following issues independently and identify the smallest broken
implication or missing hypothesis if any:

1. Custody. Recompute all four primary hashes, validate both manifests, and
   check that exact-Q and F_65521 records are genuinely separate frozen runs.
   Charge source hash, compiler hash, compiled script hash, run tag, field,
   return code, validation, and stdout identity. A passing manifest is not
   itself a mathematical verdict.
2. Scaling. Starting only from
   `L=z^2+p/2`, `K=L^2+Lambda R`, `N=L M+Lambda S`, and
   `f=K^2+Lambda N`, independently substitute
   `Lambda=sigma^2`, `M=sigma^3 A`, `S=sigma C`. Check exactly that
   `f=(L^2+sigma^2 R)^2+sigma^5(LA+C)` and that this is the primitive
   correction tie being claimed. Check every coefficient substitution in the
   compiler against this identity, including `n3,n2,n1,n0`.
3. First nonpolynomial receiver. Independently expand `f^(3/2)` and the
   charged `k10*f^(5/4)` through total sigma grade ten. Decide whether the
   complete grade-ten negative part is exactly
   `[(3/8)D^2/L^2+(5/16)k10 R^3/L]_-`, `D=LA+C`.
   Attack omitted cross terms from K, D, lower grades, k6, k2, targets,
   terminal data, and both Taylor families. Distinguish terms proved
   polynomial from terms merely dropped by weight assertions.
4. Frozen-source bridge. Inspect the seven complete-source quotient
   identities already emitted. Check that all rows are divisible by
   `sigma^10`, agree with the claimed Laurent/Faber receiver before
   specialization, and are independent of exactly the variables stated.
   Charge whether a lower charged row can mix into this grade through the
   unitriangular convention. Check the claim that seven frozen tails suffice:
   after multiplying by `L^2`, compare numerator/denominator degrees rather
   than accepting a row-count slogan.
5. UFD interpretation. From
   `L^2 | 6D^2+5k10 R^3 L` on `D(p*k10)`, verify carefully that squarefreeness
   of `L`, `deg C<deg L`, and characteristic zero force C=0 and then R=0.
   Check the exact coefficient conventions
   `R=cs*z+rs/4`, `C=(c1*z+c0)/2`. Decide whether the raw nonreduced ideal and
   its localized radical are reported correctly and whether any embedded
   structure is improperly discarded.
6. Good-prime role. Treat F_65521 only as an independent software/control
   lane, not a characteristic-zero proof. Check that no bad denominator or
   localization factor vanishes there.
7. Correction awareness and scope. Decide whether the calculation genuinely
   repairs the omitted A*C/L tie in the earlier zero-higher-correction slice.
   Then attack every stronger inference: it is one normalized ray with
   coordinate faces, not a proof of Newton-fan exhaustiveness; A survives;
   p=0, the square/discriminant intersection, terminal/Taylor receivers at
   later valuations, and higher-contact corrections remain open. Do not allow
   a square-branch, order-two, (8,12), maximum-twelve, or JC2 conclusion.

Output exactly one new report and no other file:

`xmodel/max12-812-order2-square-halfweight-kuranishi-hostile-review-grok-20260826.md`

Include a verdict table, independent derivation of the grade-ten receiver,
custody findings, strongest surviving theorem, exact scope, and sharpest
non-claim. If the endpoint survives unchanged, end with exactly
`ORDER2_SQUARE_HALFWEIGHT_RAY_CONFIRMED`; otherwise end with exactly one of
`ORDER2_SQUARE_HALFWEIGHT_RAY_REPAIRED` or
`ORDER2_SQUARE_HALFWEIGHT_RAY_QUARANTINED` and state the smallest repair.
