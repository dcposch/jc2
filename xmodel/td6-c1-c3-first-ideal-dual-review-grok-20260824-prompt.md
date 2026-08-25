# Hostile review — TD6 c1/c3 first-ideal dual rigidity

Act as a hostile different-model mathematical reviewer in
`/Users/dc/code/math/jc2`. Read in full:

- `xmodel/td6-c1-c3-first-ideal-dual-gate-20260824.md`;
- every file in `cases/td6_c1_c3_first_ideal_dual_20260824/`;
- only the two canonical compiler sources pinned by the manifest.

Charged hashes:

```text
report     6b36c189f1af3188261a91f9122a8f54d08f7a554004cd3f6d9b58bef91a7b1e
manifest   83e21713d8fe0171229341d4166ca99a89a49f5bbf9073b1c28d9ea91d8bc8a6
freeze     83e21713d8fe0171229341d4166ca99a89a49f5bbf9073b1c28d9ea91d8bc8a6
replay.py  0894a5243588bb9ad68804824f378ddbff97ccb7d0cd28692b01b6c41bb103ed
stdout     eb301f65dd41ffbfc9c57b9bf8f364fd633adf7ee02f9c93b4632b9f7925b102
```

Run the registered replay and independently attack:

1. exact dual-number arithmetic for `(c1,c2,c3)=(C,1,1+eps)` over
   `E(C)[eps]/eps^2`;
2. refactorization of all 3,602 transport columns, rank `3470`, and the
   varying 38-row first-band echelon rather than a frozen specialization;
3. provenance of the genuine quadratic-current `P12`, the 28 original source
   rows, 1,489 multiplier slots, and the lifted ideal-membership identity;
4. inclusion of differentiated pivot inverses, row multipliers, and the
   `lambda'` terms;
5. the two omission controls: nonzero raw `dc3(P12)` and 11 varying first
   pivot leads;
6. the final identity with base remainder `-k/50` and zero `dc3` remainder,
   including all ranks and digests;
7. strict scope over generic `E(C)`: first order for one class only, with no
   exceptional-fibre, neighbourhood, projective, SP-2, or JC2 inference.

Try to make the zero derivative disappear by differentiating the original
rows independently, varying the echelon, or restoring an omitted transport
or source term. Identify the smallest false identity or missing hypothesis.

Write exactly `xmodel/td6-c1-c3-first-ideal-dual-review-grok-20260824.md`.
Do not edit producer, case, canonical, coordination, prompt, log, run, or any
other review file. End with exactly one verdict: `CONFIRMED`, `GAP`, or
`REFUTED`.
