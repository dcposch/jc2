# msolve allocation/import repair: bounded instrument result

2026-09-06; owner `/root/model_productivity`; basis
`0d39df3c9fd69c939a8420c54d03228b9077777d`.

## Outcome and scope

**Two concrete 32-bit overflow sites are repaired in a fresh, pinned build:**
the shared-shape exponent allocations on both Q/Fp file-parser paths, and
the subsequent shared neogb exponent-import offset. The final build passes
64/64 upstream tests, allocation-free boundary controls, explicit NULL
allocation controls, and five tiny Q/Fp ideal controls. This is a reusable
instrument candidate, **not a general memory-safety certification**, a
giant-input replay, a mathematical result, or permission to resume the
degree-99 computation. Different-model review remains required; the
coordinator separately placed that frontier on hold.

Only root-owned `172.30.0.56`, fresh directory
`/home/ubuntu/msolve-allocation-repair-20260906`, was written remotely.
No existing build/shared installation, packages, adapter, instance state,
other worker, shared ledger, or giant input was changed. No complete giant
parser/F4 job ran. Tiny known-ideal solver controls are the only new solves.

## Exact defects and repair

Pinned upstream is msolve v0.10.1, commit
`185e7b92fa0687f4db68b0f2f453a835668ac132`, from
`https://github.com/algebraic-solving/msolve.git`. Both historical patches
were applied and their intermediate source hashes checked before the new
patch. Here `nelts_t = len_t = uint32_t`, while `nvars` and many positions
are `int32_t`.

1. Both old calls `calloc(all_nterms * gens->nvars, sizeof(int32_t))`
   multiply in uint32 arithmetic **before** conversion to size_t. With
   11,299,180 terms and 600 variables, 6,779,508,000 entries wrap to
   2,484,540,704: 9,938,162,816 allocated bytes instead of 27,118,032,000.
   The historical signed-offset patch did not repair these allocations.
2. `src/neogb/io.c:set_exponent_vector` independently used
   `iev + (nv * idx)` with uint32 `nv` and int32 `idx`. For `nv=600`,
   `idx=7,158,279`, the true offset is 4,294,967,400 but the old expression
   gives 104. Fixing allocation alone would still import wrong monomials.

New `checked-input-size.h` checks multiplication against `SIZE_MAX / a`,
then object bytes against `PTRDIFF_MAX`, before allocating. Every changed
allocation checks NULL and exits explicitly; zero-sized arrays get a
one-byte allocation without depending on `malloc(0)`. Both exponent layouts
are preflighted before their large coefficient allocations. Shared import
now obtains a checked size_t offset, rejecting negative indices/invalid
dimensions. No monomial order, coefficient, variable, generator or inverse
equation is rewritten by this patch.

## Count/offset/allocation audit

The file-input path and immediate importer were inspected before finalizing
the patch; adjacent output/API/genericity code was sampled to mark limits.
References below use the frozen final source under
`box/msolve-allocation-repair-20260906/evidence/source/`.

| Path or arithmetic | Disposition |
|---|---|
| Variable/generator counts and per-row sign-count increments | Reject before int32 overflow; reject invalid negative dimensions before count-sized allocation. |
| Total terms; `lens[i]`, `gens->nterms` narrowing | Checked addition before narrowing. Fp total at most `INT32_MAX`; Q total at most `INT32_MAX/2`. These are deliberate interface limits, not enlarged support. |
| Fp `pos+j`, final `pos+=lens[i]` | Safe for valid, unchanged rows under the checked total bound. Largest accessed position is total−1. |
| Q `2*nterms`, `pos+j+1`, `pos+=2*lens[i]` | Safe under the Q bound: doubled total at most 2,147,483,646. `mpz_cfs` count/loop now explicitly size_t. |
| Parser exponent storage | Historical int64 offset retained; dimension/byte preflight now bounds its corresponding array. |
| Exponents, coefficient arrays, mpz pointer array and each mpz object, `lens`, variable-pointer array, fixed first-line buffer | New checked array allocation and NULL guards. |
| Shared importer `nv*idx` | Replaced by checked promoted offset in both elimination-block loops. `off`, `init_off`, `off+lens[i]`, and Q `2*j+1` remain bounded for valid file input under the new total restrictions. |
| Temporary term/name/rational-coefficient strings; `getline/getdelim`; adjacent importer/solver arrays | Inspected, **not comprehensively hardened**; details below. |

The count arguments assume syntactically valid, unchanged input between the
parser's counting and reading passes. This patch does not establish that
the existing permissive parser validates those assumptions.

## Tests, negative controls and correction custody

`boundary.c` compiles with `-std=c11 -O2 -Wall -Wextra -Werror
-fsanitize=undefined -fno-sanitize-recover=all`. It directly includes the
actual final helper header. Its allocator shims reject any request over
24 bytes with a distinct error, so no giant allocation is needed or hidden.

The positive test checks zero and near-SIZE_MAX products; failed predicates
leave output arguments unchanged; Fp/Q count limits accept their boundary
and reject the next term; the exact large count/byte calculation and the
first wrapped/last-term import offsets agree with integer constants. It
also reproduces both old uint32 expressions as negative controls. Separate
processes require exit 1 with the exact intended diagnostic for size_t
overflow, exponent byte overflow, PTRDIFF_MAX violation, negative dimension,
negative import index, NULL malloc and NULL calloc. All eight modes pass;
UBSan reports no error in this tiny helper harness. **The whole solver was
not built with sanitizers.**

Both allocation-only and final import-repaired builds pass all 64 upstream
`make check -j8` tests. Final tiny controls, `-g 2 -t 1 -v 2
--random-seed 0`, use Q and p=1,073,741,827:

- Unit: `(x+y,x-y,x-1)` gives `[1]`; independently
  `1=((x+y)+(x-y))/2-(x-1)`.
- Proper: `(xy-1,y^2-x)` gives the exact reduced basis
  `{y^2-x,xy-1,x^2-y}`; `(1,1)` is an independent point.
- Q coefficient control: `(x/2+y/3,3x/4-y/5)` gives `{x,y}`;
  its coefficient determinant is `-7/20`.

The first test driver wrongly compared modular output strings to Q-style
negative-coefficient spellings. All five engine calls had exited 0, but
the final modular-proper string check failed. The original source, bases,
stderr and terminal telemetry are retained. A separate corrected replay
compares exact exponent/coefficient dictionaries (modulo the stated prime),
requires a terminal reduced-basis delimiter, and includes a wrong-sign
negative control. It passes. This is a test-reader correction, not a hidden
solver retry or a new source patch. Q-header `[1]` is **not** used as a
general rational certificate; the independent identity above licenses only
the tiny known-unit control.

## Explicit remaining risks

Do not infer unrestricted parser/import/solver safety from these tests.

- `iofiles.c` still has unchecked temporary `malloc/realloc` in
  `store_exponent`, variable-name handling, 50,000-byte term buffers and Q
  coefficient strings. String-index narrowing, permissive token/strtol
  handling, signed exponents, failed/truncated `getline/getdelim`, file
  mutation between passes, and GMP-internal allocation failures are not
  repaired. Parameter-file readers later in the same file are separate,
  untouched paths. This is not an OOM-safe parser as a whole.
- Immediate importer row arrays and `invalid_gens` allocation still have
  unchecked NULL returns. Their leading unsigned-long casts avoid the
  identified 32-bit product on this LP64 worker, but there is no global
  checked-byte/OOM proof. Extreme counts retain other hazards, e.g.
  `st->init_bs_sz = 2 * nr_gens` and `hm[j-off+OFFSET]` can overflow signed
  intermediates near their limits. API callers bypass file-parser bounds.
- `msolve.c` genericity variable-order changes retain int32 `len` and
  `j*nvars`; linear-form additions and the Julia API retain separate
  allocation/count code. F4/hash growth, exponent-degree representation,
  output/export arrays and arbitrary library entry points are not covered.
- The new header is delivered by this source patch; distribution/install
  packaging was not changed or tested. No shared installation was made.
  A successful small build is not a large end-to-end scalability test.

The previous giant-job SIGSEGV is compatible with the proved underallocation,
but there is no new stack trace or giant replay here establishing its unique
cause or confirming that every later problem is removed.

## Custody, reproducibility and terminal state

All artifacts are in `box/msolve-allocation-repair-20260906/`; compact source,
raw terminal transcripts, inputs and bases are retained in `evidence/`.
Remote source/binaries remain in the fresh worker subtree. Original build
and source elsewhere were never edited. Apply, in order, the two historical
patches and **the v2 patch**, not v1 plus v2. `make_patch.py` reconstructs v2
from the frozen twice-patched source; `worker-v2.py` records the exact
build/rebuild commands; `worker-v3.py` the corrected small test driver.
Build uses `./autogen.sh`, task-local-prefix `./configure
CFLAGS='-O3 -march=native'`, `make -j8`, `make check -j8`.

Key SHA-256 values:

```text
historical heap patch c49a9fb322c3c6518ff2234a7e521de3aa6a372efbe27dc4c9aa9360db3b2242
historical offset patch 4f2e723575ff2acbfcee4144d4c2e47cd314f6f25d1241bd1286c202c3863055
new final v2 patch 452565bfc1f1a7450f08bfe71e8d130f7ea7e5cc27c3f8055f474c38df62117b
final iofiles.c 536ab7ab87ec175242d4f949db7e16a4ad999ae8d2a6979a867969cac173f7d7
final checked-input-size.h 870592b22426f274a601e21620c45728d91e7c3127a5e75c31432fa2f9cd32b1
final neogb/io.c f901d3775c28a813f65527a2bbd65d927eafd9ef3335805a6562932415553a8d
final ELF .libs/msolve 175575870bf76a3c3a21c1660e1f6c7b8604a256fc4123643ce9711589326434
final libmsolve a569a80d81852f031be0d7c1950d68e5d35f04b1a4f85c57a353baf95829c47e
final libneogb 12197d33ce3075fd41c9874cf1379c1937fc5666e25887ae1ec22a30b271edbb
boundary.c 5fcad34ed60fc879f689b30086fba4efab1dbda6851a741eb63b88b40421fdc2
corrected worker 88db3e1b5ae5bc7eb0956cbe293a3a917530d4d8d0ca5abd447503d0ddffcde9
tests-retry.json 2f568acdb8e89e574d72e1200f150d21cc7a3e6c30173e95bcc1a5f16688e3ca
custody.json 68f754ef0d7a0bccb7f791a607b5aaa8f9f3f6761f912902a16f1645f98b671c
local-verification-v2.json fdf2fd52f3ad4f0701fdd2d4c0ac8aaafe7aa260f0d6b7c39253a90d22efc100
```

The reviewed `run_capped.py` SHA is
`4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2`.
The new launcher passed an exact-PGID dummy: leader exited, descendant held
64 MiB and ignored TERM; telemetry observed 77,877,248 bytes, validated
identity before TERM/KILL, and finished with no live descendant. Registered
PGIDs are 84690 (dummy), 84869 (first build), 102640 (rebuild), 113666
(first tests), 114071 (corrected tests). All are terminal; final custody
found **zero live registered group members**. Actual aggregate build/test
elapsed time is 93.119 s, maximum sampled group RSS 815,259,648 bytes,
well within 1,200 s / 16 GiB. Caps, actual identities, UTC times and output
hashes are in each telemetry record. No remote payload writer remains;
root retains the instance and sealed instrument for review.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11304`.
- Body SHA-256:
  `2b17cba5230b6731fd498b41bb0244754db74756040c1b8ea9f104e191a7ca84`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
