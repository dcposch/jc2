# DRAFT GitHub issue for algebraic-solving/msolve (HOLD: needs user approval to file)

Title: Silent mis-parse of parenthesized constant subexpressions (0.10.1)

Body:
msolve 0.10.1 silently mis-parses polynomial input containing parenthesized
subexpressions, producing a wrong Groebner basis with exit code 0.

Minimal reproduction (char 0, 1 variable):
  x
  0
  x-(3+1)
Expected: GB [x-4]. Actual: GB [x+1].

The parser appears to drop the parenthesized group's operator context
(related failure class to #354, silent x/2 mis-parse; PR #320's parser
hardening may cover it — unmerged as of 2026-08-10).

Impact: any pipeline emitting parenthesized .ms input gets silently wrong
verdicts. Workaround we adopted: emit fully expanded monomial sums only,
plus an input round-trip guard through an independent parser.

Found during a large verification campaign (systems with ~100 vars over Q);
happy to provide more cases.

---

# DRAFT issue 2 for algebraic-solving/msolve — FILED as PR 2026-08-23

**PR: https://github.com/algebraic-solving/msolve/pull/355**
branch `dcposch:fix-int32-exp-overflow` (commit afb576d)

## What was wrong
Not an F4 hash-table overflow. File parser in `src/msolve/iofiles.c`
computes exponent-vector offsets as `(pos+j)*gens->nvars` in **32-bit
signed** arithmetic (`int32_t pos`, `int32_t nvars`). When
`nterms * nvars > INT32_MAX`, `store_exponent()` is called with a
negative `pos` and writes off the `gens->exps` buffer → SIGSEGV.

Same class of overflow also in:
- `calloc(all_nterms * nvars, ...)` (`nelts_t`/`uint32_t` wrap at 2^32,
  hit by the full ~31M-term × 172-var input);
- `set_exponent_vector()` F4 import (`nv*idx` as 32-bit);
- variable-order swap in `msolve.c` (`j * nvars`, `len` as `int32_t`).

## Bracket on the original input (172 vars, F_105337)
| file | gens | terms | terms×vars | vs INT32_MAX | result |
| --- | --- | --- | --- | --- | --- |
| `d43split_p105337_upto38.ms` (325 MB) | 75 | 10,516,643 | 1,808,862,596 | under | computes |
| `d43split_p105337_upto40.ms` (600 MB) | 81 | 18,949,882 | 3,259,379,704 | over | SIGSEGV |
| `d43fam_p105337_a00pp_verdict.ms` (1.05 GB) | 86 | ~31M | ~5.3e9 | over uint32 too | SIGSEGV |

## gdb (unpatched 0.10.1, minimized reproducer)
```
Program received signal SIGSEGV, Segmentation fault.
store_exponent (term="+x0", gens=..., pos=-2147477296) at src/msolve/iofiles.c:58
    ((gens->exps) + pos)[k] = strtol(ev, NULL, 10);
#1  get_coefficient_ff_and_term_from_line (...) at src/msolve/iofiles.c:799
        store_exponent(term, gens, (pos+j)*gens->nvars);
#2  get_coeffs_and_exponents_ff32 (...) at src/msolve/iofiles.c:928
#3  get_data_from_file (...) at src/msolve/iofiles.c:1054
#4  main (...) at src/msolve/main.c:541
```
`pos=-2147477296` is `214749*10000` wrapped as int32 (`2147490000 - 2^32`).

## Minimized reproducer (~700 KB)
10000 variables, 214750 terms of `x0` over F_105337 (last index × nvars
just exceeds INT32_MAX). Unpatched: SIGSEGV as above. Patched: exit 0,
GB `[1*x0^1]` in ~31 s.

```python
nvars, nterms = 10000, 214750
open("repro.ms","w").write(
    ",".join(f"x{i}" for i in range(nvars)) + "\n105337\n"
    + "+".join(["x0"] * nterms) + "\n")
```

## Fix
64-bit (`int64_t` / `size_t`) indexing for exponent offsets and
allocations in `iofiles.c`, `set_exponent_vector` (`io.c`), and the
variable-order swap (`msolve.c`). 34 insertions / 32 deletions.

## Verification
- `./configure CFLAGS=-g && make -j`; `make check` **64/64 PASS**
- minimized reproducer: unpatched SIGSEGV, patched computes
- original upto40 / 1.05 GB file: same parser path; patched parse in flight
  (crash is during parse, before F4)
