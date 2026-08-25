# B9 normalized common-cubic global next-layer reduction

This portable case starts from the reviewed complete common-cubic family at
modulus `3^11` above one fixed B9 mod-243 parent.  It freezes three distinct
scopes:

1. the earlier 557-point `[x^2 y^2]` diagnostic (`AWS_BOX02_V1`);
2. 447 deterministic predecessor controls with the complete final fresh55
   fibre retained (`AWS_BOX02_FRESH_ELIM_V2`), all diagnostic UNSAT;
3. the exact global reduction: a constant `205 x 55` block of rank 29,
   followed by an exact 176-coordinate modular Kuranishi circuit on all 95
   predecessor parameters (`AWS_BOX02_FRESH_BLOCK`,
   `AWS_KURANISHI_MAP`, `AWS_BOX02_AGGREGATE`).

The exact theorem is the reduction, not an emptiness or survival statement.
The full 176-row formula is hash-pinned, while solver endpoints are kept
outside this freeze until they terminate and are independently certified or
directly replayed.

Heavy replay is AWS-only.  `compile_fresh_block.py`,
`emit_kuranishi_map.py`, and `aggregate_kuranishi_map.py` refuse non-Linux
execution and require registered AWS job tags.
