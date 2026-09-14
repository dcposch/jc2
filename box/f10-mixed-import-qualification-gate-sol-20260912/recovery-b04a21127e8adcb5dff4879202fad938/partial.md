# f10 mixed import qualification: different-model static FIRST

Status: **CONDITIONALLY STATIC CONFIRMED**. This source-only finding grants no execution, worker, actual-host, import-closure, or scientific authority.

First action was the finalizer lease creation at `2026-09-12T23:03:58Z`; the first retained explicit clock read was `2026-09-12T23:04:07.715638168Z`. All four charged SHA-256 values matched before the four bodies were read WHOLE. I reused the exact-pinned immutable coordination snapshot and did not read mutable canonical coordination state.

## Source ordering and bounds

The observer checks EC2 vendor and the still-disabled exact instance placeholder before importing SymPy or mpmath. Only `sys` and `pathlib` startup occurs before those physical guards. It then requires the exact metadata-script startup path vector and all four `-E -s -S -B` flags before appending the private library path.

The assembled manifest read is bounded to 1,048,577 bytes and rejects anything above 1,048,576. Every currently loaded file-backed module is required to appear in the trusted manifest and is read with a 67,108,865-byte bound, rejecting above 67,108,864 and requiring the recorded SHA-256. Manifest size, the finite loaded-module mapping, the external service resource envelope, and the preparation tmpfs additionally bound this narrowly trusted use. This is not a generic hostile-input read-before-length theorem.

Package origins must resolve beneath the distinct private `lib/sympy` and `lib/mpmath` trees, `GROUND_TYPES` must equal `python`, and output is one sorted JSON metadata record. Ordinary science/runtime directory prefixes are deliberately not claimed from this metadata-script startup.

## Literal API coverage

Against both charged clients, the observer covers every directly required SymPy module callable: `symbols`, `Rational`, `Integer`, `Poly`, `expand`, and `cancel`. It covers the used `Poly` methods `terms`, `degree`, `gcdex`, `mul_ground`, `LC`, `all_coeffs`, `as_expr`, `lcm`, `from_dict`, `nth`, and `factor_list`, plus the used `Poly.is_zero` property and `QQ.frac_field` callable. The clients' other imports are Python standard-library facilities, while `sp.__version__` and mpmath's version are observed metadata rather than callable API requirements.

These presence/callability checks do not establish algebraic semantics. Hashing the modules loaded by this one observer does not prove future dynamic-import closure, complete package closure, native no-escape, or that later producer/checker imports and behavior will be identical.

## Verdict

**CONDITIONALLY STATIC CONFIRMED.** Within the four charged files, the observer supplies the stated missing private-package path, loaded-file pin, backend, and literal API metadata channel. The exact instance-bound copy, execution envelope, assembler provenance, actual output bounds and pins, full native inspection, and future producer/checker qualification remain mandatory ROOT observations. Any mismatch is STOP; this report is not launch authority.

No source was executed, imported, parsed, tested, or edited.

<!-- BODY-END -->
