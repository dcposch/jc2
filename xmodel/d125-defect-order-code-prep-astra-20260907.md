# D125 defect-order instrument: versioned code preparation

Status: **IMPLEMENTED PREP ONLY; all local controls PASS.** 2026-09-07. No AWS/SSH, CAS, full-client read/arithmetic, solver, deployment, fleet action or live-review access. No authority file is supplied. The independent mathematical gate remains outside this task's read perimeter.

## Outcome

The fresh code in `box/d125-defect-order-code-prep-20260907/` implements **exactly W1/W2/W3 then dp**, preserving all 269 production variable names and 803 source equations. No W4/W5, gauge, graph expansion, elimination or field change was added. The original source files and reviewed instrument were not edited.

The 87-line `defect_order.py` derives and validates the single production descriptor from the already fixed names. Its descriptor digest must equal `64c212c26a9883d1c0f674b93f0246f67e22a8b742b643c6628fd3c14014db66`; the full ring-line digest must equal `d894d6427d39b774c403165c83bffddbe993b96345ee00d652f5af7a06219bca`. The old dp name/ring digest must equal `ccd93ccf39b0109a36dc89d54f1fd281bcef17b1dc5fab3c65f2988027333d73`. The only other allowed descriptors are declared fixtures with at most eight variables; no production command-line option selects another order.

The exact key prepends the three integer weight sums to the existing total-degree/reverse-lexicographic key. Weights propagate through **every** dividend/divisor leading-term choice, both S-polynomial leading terms, all Buchberger reductions, normal form of 1 and reduction of every original equation. The production driver explicitly supplies the same descriptor to the result parser and its weight rows to properness verification. There is no implicit dp fallback in that path.

## Source and certificate boundary

`read_source` is byte-identical as a function to the repaired instrument. It still checks both frozen source pins, the original dp header, literal row identities and the complete 269/803 client. Polynomial parsing/arithmetic, original-row unit cofactors and zero/duplicate engine mapping are unchanged as functions too; source-segment equality is tested.

After that validation, the adapter changes only the **initial ring-declaration line** of the execution prefix. Everything after its first newline through the ideal's terminal semicolon remains byte-identical. `check_prefix` rejects any changed/omitted ideal row, fixed zero, label/body or appended text relative to the validated original. As in the previous caller, the original import-only tail is replaced by the solver/certificate footer. That footer differs from the old one **only in its result order digest**; its commands and conditional lift are otherwise byte-identical, as tested.

The result parser retains literal-empty stderr, exact `I_SIZE` versus nonzero indexed-I count, complete ordered I/G/T blocks, terminal framing and no trailing text. Weighted and dp headers cannot be interchanged. Unit cofactors are still multiplied against the complete original equations, independently of monomial order. Properness still requires an exact-Q Groebner basis for a proper superideal containing **every original equation**: all S remainders zero, NF(1) nonzero and all original normal forms zero. No modular, timeout or incomplete-output decision is accepted.

## Separate future authority

The prospective remote directory is newly named `/home/ubuntu/d125-defect-order-solver-20260907`; it was **not created or accessed**. The new schema is `jc2.d125-defect-order-solver-authority/v1`. Authority must bind the new caller/checker/helper pins, the fixed order digest, exact instance/boot/cwd, unchanged source/binary/runner pins, caps, job and deadline. Solver mode additionally requires accepted full-stream and defect-order gates plus a named accepted actual-engine order control. The prior authority schema and prior remote cwd are rejected. `PLAN_SHA` now pins the terminal defect-order proposal `9b6f972b2513094fe5fe33cf41721eb971e494a6762915bfda5c31e8a4e77d9b`; this is not itself execution permission.

Engineering control and solver authority remain separated. The retained existing `control` phase is the old tiny dp zero/index/cofactor fixture, without slimgb; it is **not** a claimed test of the new weighted engine order. Later order controls need separate explicit root authorization. No registration/authority falsely says that they have run.

Caps and custody machinery are unchanged: 300 seconds decision plus conditional lift in that same cap; verification at most 120 seconds only after normal completion; 450 seconds total; 16-GiB AS and sampled exact-group RSS; inherited 64-MiB FSIZE per output stream and core size zero. There is no retry/enlargement or hidden process group. The fixed CAPRUN pin remains `4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2` and Singular pin `90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`; neither binary nor runner was executed or altered here.

## Actual tiny tests and reproducible diff

`run_tests.py` ran all **28 methods normally and under -O**, both successfully. The retained replay batch took 0.588034 seconds wall, with aggregate child user/system CPU 0.567/0.022761 seconds and maximum child RSS 30300 KiB. The runner enforces 30-wall/25-CPU-second and 512-MiB AS limits. An earlier identical pre-harvest batch also passed; no failed preparation test or repair retry occurred.

The 17 original methods retain their mathematical/parser/limit controls; only their authority fixture was updated. Eleven new methods verify:

- Actual metadata descriptor/ring/name pins, weight/type/field/tie-break/key drift and production variable-order rejection.
- The real graph basis `x-y^2,z-y^3` passes weighted Buchberger under W1=(3,1,4), but fails under dp and under a changed all-ones first row. Instrumentation also checks that every normal-form call receives the supplied weights.
- Comparisons controlled separately by W1, W2, W3, ordinary degree and reverse lexicographic ties; weighted protocol cannot be parsed as dp or vice versa.
- Changed execution ideal suffixes, dropped original rows, altered zero/coefficients, old-source order drift and certificate-footer preservation.
- Six literal zero/duplicate rows and six cofactor columns, exact original-row unit identity, corrupted cofactor rejection, whitespace stderr rejection and `I_SIZE=0` rejection.
- False properness `(x*y-1,x^2)` fails Buchberger despite NF(1)=1 and input reductions zero; an omitted original equation is rejected.
- New authority rejects the old job/schema/cwd, wrong order pin and missing order gate/control. AST scans find no Python `assert` statements in production or test files, and unchanged function bodies are compared exactly.

Replay without creating an output file:

`python3 -I -B box/d125-defect-order-code-prep-20260907/run_tests.py`

`versioned-delta.patch` is the exact deterministic unified diff of the four copied files against the frozen repaired version. The only two new Python files are `defect_order.py` and `test_order.py`; no generic runner or configurable production-order framework was built.

## Pending actual-engine delta, not executed

After independent code/mathematical acceptance and a separate engineering GREEN, use at most 10 seconds/512 MiB per declared tiny engine fixture. First test three `a(...)` rows on variables x,y,z,t,u with rows `(2,1,2,2,2)`, `(1,0,0,1,0)`, `(1,0,0,0,0)`, then dp. Require global=1 and respective leaders x,x,x,y^2,z for `x+y`, `x+z`, `x+t`, `y^2+z`, `z+u`. This separates all five comparison levels using actual explicit engine printing.

Then, only under authority explicitly permitting a tiny engineering GB, serialize the declared three-variable weighted graph fixture above through the new footer, check actual I/G with the exact weighted verifier, and reject a changed descriptor/header. Retain the existing zero/duplicate, FSIZE and group-cleanup controls or repeat only what root requires after a new boot. These are prospective commands/requirements, not observed results. Any full 269-variable source parse or solver remains a distinct later authorization.

## Pins and terminal custody

Original files remain at `box/d125-small-exact-solver-strict-repair-20260907/`. Their rechecked SHA-256 pins are exact.py `7ca2b24ee5d04ff6d60fd2212a05586c8bba24327a51c7718351434c7eda60e9`, driver.py `7f081576ea72005c2509ef2d575aa63b9fd53416987f3535ed520fd79fdc130d`, test_exact.py `e1f0d6d0c0a930d8f1a2dc17709c98fd1bb37669564c1d09b2be6251a87dd588`, run_tests.py `90f3ae5e24c51a893af232b911d9baafb9b8f60ece1a5349807fa3332b94cd04`.

The only mathematical metadata read here was terminal `box/d125-defect-order-discriminator-20260907/witnesses.json`, SHA `6e8c0102089ca6d046f4e1834ce30917a1dff6b2ad7d8ab29de95e7fc7eb83a1`; no full coefficient stream was loaded. Original source pins remain JSONL `b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac`, Singular `c089c33301e3889e0c20527386719f411907cf2957ecfad3d93c65f7be24e718`, not re-read this task.

All owned artifacts are in the new box:

| file | SHA-256 |
|---|---|
| exact.py | `f452a1f6a3dfcc534a14a0d2b1f162589fc928973aff5a91f7faaa88921039af` |
| driver.py | `944d5a840b6e4a81e89e5bcfa0ce6e6e54684ece70f182499735b9aa8571faec` |
| defect_order.py | `d5031c04fc7fdfec1fc57285b7538747b4d0aae25fae5ac140439d01dbd99ca3` |
| test_exact.py | `a9ee732372e9340c6c0796b2be41c24ad325a7c6653ff517f896d95cde596e20` |
| test_order.py | `4936e892be0cb4eed0f658f210dcb386fe2cc13d2a10c5d0b75f2a84efe57880` |
| run_tests.py | `27633b921bb73dd2f9aab357858f525b683f3383361193345150403b89b5a70a` |
| versioned-delta.patch | `41f1a0931805cabd50e22f5c4a781ad5c2bfbd4cea1e7e0a147b52955a15ea01` |
| replay.json | `31cdd5e7b060e99e1112530f0a7db55893fc662867031bf4e867cb2c8d495dee` |

All local tests and writers are terminal. No live peer artifact, shared ledger or protected project was read/edited. No remote job or worker was touched or retained. **STOP/IDLE: code prepared, no solver result or new execution authority.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10049`.
- Body SHA-256:
  `83a78ec1e7fcd9611b70f012609cd92fdf683e8e2c248f3ea52de389a4fa7e95`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
