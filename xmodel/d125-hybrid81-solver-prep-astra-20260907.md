# Hybrid81 exact-Q solver adapter: local preparation

2026-09-07. Author `/root/model_productivity`. **PREP ONLY: no solver, source
construction/import, worker access, deployment or authority file.** All code and
25 normal plus25 optimized tiny tests are terminal. Own box:
`box/d125-hybrid81-solver-prep-20260907/` (below, `B/`).

## Minimal interface result

**JC2CERT version1 needs no schema change.** Its existing source digest now binds
the frozen hybrid construction; the ring digest still bindsQ, globaldp and the
displayed variable order. The complete indexed engine-I/G/T blocks and the
rational cofactor/Buchberger checker are unchanged. Old `exact.read_source`
cannot consume the hybrid schema directly, so a separate83-line `hybrid.py`
adapts that input instead of weakening the reviewed old parser.

`exact.py` is byte-identical to the accepted two-check repair,
SHA `7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9`.
Strict empty stderr, exact I_SIZE/nonzero-entry count, zero/duplicate equality
mapping, rational arithmetic, dp comparison, all S-pairs and all-row reductions
are preserved. The reviewed footer function is unchanged, including short=0,
one slimgb(I), complete I/G printing and conditional lift in the same cap.

`driver-delta.patch` lists only the hybrid import/read call, new source/cwd/
registration pins, distinct authority schema, construction-bound result digest,
and single-input post-hash changes. No algorithm, result parser, certificate
arithmetic, order, limits or engine-control fixture changed. Its SHA is
`9a7665f89ccf41d1b334b8e8796fc303652049fa565a6dfcef39de6fa8e0db63`.
The authority format changes to `jc2.d125-hybrid81-solver-authority/v1`, not
the mathematical certificate format. Engineering and solver modes remain separate.

## Literal input and source interpretation

Production parsing requires the frozen construction SHA
`4ea526b2680ef41154332be3059ae5543c2678fdf8fb6a95d02176e8eb929272`,
canonical JSONL bytes, complete prefix/footer hash, literal row indices, unique
names/labels, rational canonical coefficients and correct dimensions/counts.
Field/order/target areQ/dp/`J+5*k^3*g^2/9`. Nonzero golden components are rejected,
not split into extra equations. Original source binding remains
`b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac`.

All804 rows, including578 zero original rows and all original guards plus
UNIT/kz, are serialized as ordinary explicit rational polynomials with their
labels. The adapter re-parses each serialized expression and checks exact equality
before returning the Singular prefix. It neither drops zeros nor assumes
Singular's cofactor index equals a literal index. Production requires81 names,
804 rows,298 coefficient maps,19 graphs and the exact kz−1 final guard.
Every map/graph and cover trace remains in the unchanged hash-bound input;
they are not reinterpreted as additional independent polynomial variables.

For a unit, complete engine equality mapping and cofactor expansion against the
full804-row vector must give literal1. For properness, exactQ Buchberger,
NF(1) nonzero and zero NF for every804 input equation certify containment in a
proper superideal. Neither a parser success, [1] display, nonunit printed list,
dimension nor a modular calculation is a certificate. The result format also
retains raw engine cofactors for later exact replay; no cofactor is inferred.

Those are certificates about the constructed81-coordinate ideal. The already
accepted affine-graph/normalization/faithful-cover chain is still required for
any source conclusion. The client is the restricted parity/gauge slice, not all
JC2 maps. Physical total75/125 is not replaced by receiver degree15/25. No actual
basis, certificate, point or nonemptiness claim was produced by this preparation.

## Actual tiny controls

All17 prior producer methods pass, with only the synthetic authority's schema
literal updated to the new caller. Eight new methods use declared4-variable,
at-most7-row toy hybrid streams; none imports the actual2.24MB stream.
New checks include:

- Complete ordinary-expression roundtrip with all zero/duplicate slots and unit
  guard; a genuine unit cofactor vector lifts to every literal position.
- Corrupted cofactor and omitted guard rejection; a genuine proper superideal;
  rejection of `(x²,xy−1,kz−1)` as a false proper certificate by its S-pair.
- Actual changed target, field/order/source pin, row index, golden component,
  missing low row, final guard, footer count, duplicate JSON key and trailing
  record mutations, with resynchronized footer hashes where applicable.
- Resynchronized changed zero/fixed-map objects cannot reuse the unchanged
  construction-bound certificate; whitespace stderr and false I_SIZE remain
  rejected. Code AST checks find no removable language-assert enforcement.

Both modes passed25 methods:0.575290 seconds combined wall,0.577203 child CPU,
29536KiB peak child RSS, within30wall/25CPU/512MiB. Results are preserved in
`B/test-results.json`, SHA
`b67368ce5173593d233344813062fb1ff5cac2b038920965bc1ae51c094df0c7`.
Replay: `python3 -B B/run_tests.py` (read-only stdout mode). These are synthetic
stream/identity controls, not fabricated actual Singular observations.

## Prospective attempt and specifically missing evidence

The disabled `B/REGISTRATION.md`, SHA
`38bc496f9f2eb7f7519c70bbabe0eab8586c56264b7e20c0078fc71cb818cd6d`,
describes one conditional300-second import/serialization+slimgb+unit-lift attempt,
with120-second exact verification only after normal complete output and450 total.
The reviewed16GiB AS/sampledRSS and64MiB FSIZE per output stream/core0 remain.
The existing **2MiB generated-input cap, including suffix, is unchanged**.
Actual ordinary-input size is unmeasured; JSONL size does not determine it.
Hitting that cap ends the attempt INCONCLUSIVE, without automatic enlargement.
All future phases need fresh root physical authority, pins, boot/custody and
exclusive paths; this preparation creates none. The worker remains root-stopped.

The genuinely new untested interface is hybrid serialization/import and its
caller/source binding. It needs different-model code review and a later explicitly
authorized tiny actual-engine hybrid fixture, including complete zero/duplicate
I/T correspondence. Current code's historical `full_stream_gate_*` authority
field can record root's accepted adapter/source-interface gate; it does not
require inventing a third full algebraic implementation or replay.

**No concrete unresolved algebraic claim warrants another complete cover replay
by convention.** Sol14k already reviewed construct.py and the separate literal
original-row cover replayer, and their actual all803-row run succeeded. Root's
accepted harvest `e4c659f7e324651757c2d52fe1fc3fda52acd25b5dbbbbe4be24f3db30062d8c`
is sufficient at that stated scope. The former report's generic “next gate”
wording is not an additional standing dependency. Prior accepted engine, FSIZE
and CAPRUN evidence is retained; fresh checks should address the new path/boot
and adapter, not automatically repeat every historical control.

## Pins and custody

- hybrid.py: `c9755a7172eaa7f1393860931d55c38a0b9d79b5b170eadbf14baff0203c35a3`.
- driver.py: `faf7a1e08fa7fafac09160b57587eb325ef4542da30a7defbf5165bc329569d9`.
- test_hybrid.py: `b1e35d3935b8e808dcbd935567b77cea7457029e2968c2a3fd32e58ff4c71118`.
- `B/custody.json`: `319fe354fd46e5aef2d17ff8ca0c54782a6ec6f277de6122d2d9df0c64967d87`,
  containing all9 artifact pins and exact dependencies/pending evidence.

Read perimeter: terminal D125 exact-solver/strict-repair reports and code,
known versioned D125 instrument filenames, the sealed hybrid constructor's
format definitions and own terminal compact custody. No live peer material,
protected tree, AWS/SSH, source rows, CAS or full-system arithmetic was accessed.
All earlier bytes remain untouched. Report transactional publication and local
test writers are terminal. **STOP/IDLE; no solver authority.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8046`.
- Body SHA-256:
  `0e0f5d8963e7670ccd7259942da9e369d20ea9cf2177a06792665264c0391c7c`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
