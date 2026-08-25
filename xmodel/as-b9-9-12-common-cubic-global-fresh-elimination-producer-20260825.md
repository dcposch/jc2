# Producer theorem: exact global fresh elimination for the B9 common-cubic family

Status: **producer-exact, provisional pending hostile source/compiler review**.

## Scope

Fix the reviewed normalized `(P<=9,Q<=12)` B9 mod-243 parent and its complete
common-cubic family through modulus `3^11`.  The reviewed canonical family has

```
17 active + 78 spectator-kernel + 55 final-fresh-kernel = 150 trits.
```

This note concerns only the next `3^11 -> 3^12` transition inside that one
fixed-parent common-cubic chart.  It is not a statement about other mod-243
parents, the broad D12 chart, all-depth lifting, maximum 12, a counterexample,
or JC2.

## Exact elimination theorem

The fresh order-`3^11` output-digit operator on the 299 source rows has shape
`299 x 149`, rank 94, kernel dimension 55, and cokernel dimension 205 over
`F3`.  After projecting the next carry to this 205-dimensional cokernel, the
dependence on the final 55 family parameters is one constant matrix

```
A_fresh : F3^55 -> F3^205,
rank(A_fresh)=29,
dim ker(A_fresh)=26,
dim coker(A_fresh)=176.
```

Its serialized SHA is
`9b1ae5b0f64bb3d7fccd27f7d8a3d2cae141c297fd531fd6fff1c302a48fb7d5`.
The canonical quotient payload has uncompressed SHA
`6b972339a1ad402229fc03b878a8ae80f2620c1441e4103226613ee6241b6946`.

Constancy is source-licensed, not inferred from samples.  Predecessor-family
changes begin at output order `3^5`; final fresh-kernel changes enter at output
order `3^10`.  A predecessor/fresh cross term therefore has order at least
`3^15`, and after division by `3^11` it vanishes modulo 3.  The same valuation
check was applied to determinant rows and to every derivative of the cubic
and quartic common-core rows.

Consequently existence of a `3^12` lift is equivalent to vanishing of one
exact map

```
K : F3^(17+78) = F3^95 -> F3^176.
```

Setting the final 55 kernel coordinates to zero is licensed only after this
176-row quotient; it is not a choice of a representative asserted to lift.

## Exact circuit and independent shard composition

`emit_kuranishi_map.py` reconstructs the literal 276 determinant plus 23
common-core rows modulo `3^12=531441`, with explicit chronological divisions
by `3^10` and `3^11`.  Every modular multiplication widens 20-bit residues to
40 bits before reduction.  It emits the 176 coordinates as a shared 34,555
node QF_BV DAG.  No ordinary F3 ANF degree is assumed across the canonical
carry gates.

Six deterministic overlapping row blocks ran on Box02, Box03, and r6d.  All
consume identical source hashes and report the same all-coordinate structural
hash

`557123112e5c3e4ea5d3a5a95709d816254080e0eeef2d995d028013db468b48`.

The ten overlap coordinates (30--31, 60--61, 90--91, 120--121, 150--151)
match exactly.  The aggregate full formula has 2,024,323 bytes and SHA

`108cfdaae0c897ab66518e18d5e38d0969a1f8f936eeb488fd9144e4fbfe0f4c`.

The aggregate result is
`351f2049b11adc1e4cbe30911f989dd817eba7bac00f0add46af469757790293`.

## Diagnostics kept separate

Across the origin, signed basis, and 256 seeded mixed predecessor controls
(447 total), the complete 55-dimensional fresh fibre was eliminated exactly.
All 447 displayed matrices were byte-identical to `A_fresh`, had rank 29, and
all 447 right sides were inconsistent.  The ordered record stream SHA is
`c066603aca9e2c432a96ff6f0a6f513a11dfd91b326feaaf6491b709fca15dfe`.

This is only a sampled negative diagnostic.  It is not evidence that `K` has
empty zero locus.  Only the exact 95-variable formula (with a replayed SAT
model or a checked UNSAT certificate) can decide that question.

## Solver firewall

The system Boolector 1.5.118 deployment rejects SMT-LIB `define-fun` and is a
parser negative control only.  Z3 4.8 parsed a smoke formula but exhausted a
deliberately small 8 GiB cap.  Current Z3 4.16 solver races are outside this
freeze and do not affect the reduction theorem.

A SAT model will be accepted only after reconstructing the eliminated
fresh-kernel solution, solving the 149 new digits, and replaying all 299
integer source rows modulo `3^12`.  An UNSAT return will not be promoted
without independently checked proof or an independent exact finite-field
certificate.
