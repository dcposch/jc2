# V18 design failure: factored-prelude parser

The first registered modular preflight
`max12_812_order2_u2_62_k00_filtered_load_v18_p65521_20260827T111333Z_r6a`
failed closed before emitting a matrix or rank.  All six freeze entries
verified.  The emitter then rejected the exact frozen V14R1 row prelude
because it contains safe factored expressions such as
`(21/512)*(d5)*(1)^5`, while the V18 parser accepted only expanded monomials.

This is an implementation/type failure and carries no mathematical outcome.
The harvested packet is `aws_p65521_r6a_failed_parser/`.  Its emitter-stderr
SHA-256 is
`0f01afd2eaf18b29216ab418ae315bc777c996fb7bb26d4f36fe2685c4f73f6a`;
the failed compiler SHA is
`a26149ce209c57491fa7f6610160e750fb280873429ab22bd6dda6cc6b6b7a88`.
V18R1 changes only polynomial parsing, using a whitelisted arithmetic AST;
the invariant, source rows, ideals, matrix maps, field, and rank engine remain
unchanged.
