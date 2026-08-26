# Preregistration: independent factored/saturation A-fast race

This auxiliary exact race consumes the pinned factored Rees-v2 A source and
changes only:

- the embedded registered AWS tag;
- the ring order from global `dp` to `(lp(1),dp(8))`, placing the Rees
  parameter in its own elimination block;
- diagnostic printing of the full special-fibre basis;
- a unique A-fast PASS marker.

The eight charged equations, toric relation, `s` contraction by Singular
`sat`, special-fibre torus saturation, fixed support/load/weight/residue, and
verdict semantics remain byte-derived from the pinned source

```text
2b416cb8209dd9d220d8f57ec78044bddb7d83d5ea4899d59ab7b4b6b4f49e52  base_A.sing
```

This races the original Box02 `dp` A solve; it does not replace or modify it.
Any disagreement is fail-closed.

