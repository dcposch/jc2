# f10 mixed import qualification: different-model static FIRST

Status: **CONDITIONALLY STATIC CONFIRMED**. This source-only finding grants no execution, worker, actual-host, import-closure, or scientific authority.

First action was the initial finalizer lease creation at `2026-09-12T23:03:58Z`; the first retained explicit clock read was `2026-09-12T23:04:07.715638168Z`. All four charged SHA-256 values matched before the four bodies were read WHOLE. I reused the exact-pinned immutable coordination snapshot and did not read mutable canonical coordination state.

An administrative tool-output capture error lost the first random lease token. Before recovery, the exact owned lease was 639 bytes, mode 0400, SHA-256 `c22b8d55375b5e2b70068005c975e6e4af631a2a3737cd6655161423d8e00169`; its partial was initially observed empty, then received this report body and was 3,130 bytes, mode 0600, SHA-256 `bc845386cd6a8c35a250c8c4f9bbb5bb78fd7ba3561c579398dbfd1caccc1b82`. Final and manifest were absent. With ROOT's explicit instruction, only those two owned lifecycle files were moved intact to `box/f10-mixed-import-qualification-gate-sol-20260912/recovery-b04a21127e8adcb5dff4879202fad938/`, and a fresh unchanged finalizer transaction was begun. No evidence was deleted or lease content altered.

## Source ordering and bounds

The observer checks EC2 vendor and the still-disabled exact instance placeholder before importing SymPy or mpmath. Only `sys` and `pathlib` startup occurs before those physical guards. It then requires the exact metadata-script startup path vector and all four `-E -s -S -B` flags before appending the private library path.

The assembled manifest read is bounded to 1,048,577 bytes and rejects anything above 1,048,576. Every currently loaded file-backed module is required to appear in the trusted manifest and is read with a 67,108,865-byte bound, rejecting above 67,108,864 and requiring the recorded SHA-256. Manifest size, the finite loaded-module mapping, external service resource envelope, and preparation tmpfs additionally bound this narrowly trusted use. This is not a generic hostile-input read-before-length theorem.

Package origins must resolve beneath the distinct private `lib/sympy` and `lib/mpmath` trees, `GROUND_TYPES` must equal `python`, and output is one sorted JSON metadata record. Ordinary science/runtime directory prefixes are deliberately not claimed from this metadata-script startup.

## Literal API coverage

Against both charged clients, the observer covers every directly required SymPy module callable: `symbols`, `Rational`, `Integer`, `Poly`, `expand`, and `cancel`. It covers the used `Poly` methods `terms`, `degree`, `gcdex`, `mul_ground`, `LC`, `all_coeffs`, `as_expr`, `lcm`, `from_dict`, `nth`, and `factor_list`, plus the used `Poly.is_zero` property and `QQ.frac_field` callable. The clients' other imports are Python standard-library facilities, while `sp.__version__` and mpmath's version are observed metadata rather than callable API requirements.

These presence/callability checks do not establish algebraic semantics. Hashing the modules loaded by this one observer does not prove future dynamic-import closure, complete package closure, native no-escape, or that later producer/checker imports and behavior will be identical.

## Verdict

**CONDITIONALLY STATIC CONFIRMED.** Within the four charged files, the observer supplies the stated missing private-package path, loaded-file pin, backend, and literal API metadata channel. The exact instance-bound copy, execution envelope, assembler provenance, actual output bounds and pins, full native inspection, and future producer/checker qualification remain mandatory ROOT observations. Any mismatch is STOP; this report is not launch authority.

No source was executed, imported, parsed, tested, or edited.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3860`.
- Body SHA-256:
  `2bccd5471279ce9d9d98952501533b9f716fa5898957934fb3ea2cf25478f603`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
