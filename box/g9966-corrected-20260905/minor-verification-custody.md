# Independent verifier custody

All `minor_*verify.json` results produced from the mutable lane-root verifier
before the immutable snapshots are logical controls. Their source engine,
source derivation and phase files were checked by hashes, and their exact
algebraic conclusions remain useful. They are not the authoritative final
verifier-code custody certificate: some long-running Python processes had
already imported a version while the development file was subsequently
edited. In particular, an end-of-run hash of the development file must not
be attributed to the previously loaded implementation.

`minor-verification-code-v1/` is the first immutable verifier snapshot.
`minor-verification-code-v2/` adds the independent direct FLINT backend and
explicit certificate relocation roots. `minor-verification-code-v3/` adds
recursive batch-resume ancestry, backend custody, band-sequence checks, and
independent materialization of the weak wrapper's actual source images in a
fresh subprocess. Their SHA-256 manifests sit beside
the directories. The frozen core captures its file hash at import; the
merged verifier captures its own and the core's hashes at startup. The
FLINT helper captures its hash at import. These snapshots will not be edited
in place; any further change requires a new numbered snapshot.

The authoritative runs launched around19:20UTC use v2 from the worker directory
`/home/ubuntu/g9966-corrected-jacobian-flint/minor-verification-code-v2/`, with
python-flint0.9.0. They take frozen copies of the selected merged result as
`minor-independent-controls/authoritative-delta{2,52}-input.json`. Every phase
referenced by either antecedent and by the continuation retains its recorded
SHA-256; relocating a file by its basename is permitted only inside an
explicit relocation root, with a unique match and the recorded content hash
checked afterward. The actual source chart and both coefficient-ring maps
are reconstructed independently.

The direct FLINT backend builds complete normalized F and G, differentiates
those polynomials, and applies z=w-1 AFTER extracting the requested Jacobian
coefficient. It does not share the production factored approximate-root
bracket formula. Its t0..6 controls compare every resulting coefficient with
the independently constructed SymPy F/G derivative, including rational
coefficients and the zero-outer pure-power case. The backend declares the
ordered native QQ generators, verifies each generator's monomial image, and
records the exact python-flint version and helper hash. Full-band verification
also regenerates every k coefficient omitted as zero by the native emitter.

An authoritative unit or full-chart survivor verdict requires the frozen
result corresponding to the actual final endpoint, not an earlier successful
checkpoint. A checkpoint verification is reported with its exact ending band.

## Frozen v6 arithmetic and the complete quotient prefixes

`minor-verification-code-v6/` keeps the v4 mathematical checks but parses
expanded rational monomials with Python `Fraction` and composes complete QQ*
coordinate maps with exact `fmpq_mpoly` arithmetic. Source and target native
rings contain every declared remaining generator, in recorded order; each
source variable receives either its recorded QQ* polynomial image or its
identity image. Every cumulative coordinate image is compared exactly in
that ring. No quotient relation is used in the map-composition proof. The
native map helper's import hash and the explicit generator map are recorded
per phase. This avoids repeated SymPy expansion without changing any ideal.
`minor-v6-controls.json` rejects changed images, hidden variables, inversions,
floating exponents and non-polynomial calls, and checks rational arithmetic
against expanded SymPy polynomials.

The v6 replay passed δ2 through J66 plus the equivalent quotient transition
(dimension230), and δ52 through J89 plus that transition (dimension44).
These use exact immutable v4 input snapshots and the earlier hash-bound v2
prefix receipts; the newly reached phases and the actual ideal-inclusion
transition are independently replayed. Final verification of the later
unreduced batch snapshots J70/J93 was launched separately and must not be
called complete unless its terminal coefficient regeneration finishes.

The independent direct full-F/G quotient oracles have also completed at δ2
J67 (75 nonzero coefficients) and δ52 J90 (55 coefficients). Their core and
coefficient-helper hashes are captured at import from immutable v4 files.
The thin `minor_v4_firstband.py` launcher was copied once before execution
and never edited; its output field named `driver_sha256_at_start` is actually
computed when the result is written. We treat that field only as the unchanged
copied-launcher content hash, rather than claiming an import-time hash. The
executed immutable helper, exact parent input hash, complete map and full
coefficient support are preserved. The separate frozen oracle-phase verifier
binds these data to the corresponding ordinary reduction phases.

The reordered δ2 J66-plus-physical-corner check was independently verified by
`minor-verification-code-corner-v2/`: full first Taylor F/G products in the
proved monic coefficient quotient produce the same combined row, the saved
phase preserves its exact parent map/free/residual boundary, and fresh
Singular gives dimension229, nonunit. This corner is an additional necessary
row on the J66 prefix, not an assertion that intervening global bands were
exhausted. Generic direct SymPy first-Taylor controls agree with the independent
native quotient calculation for both linear and higher powers of d.
