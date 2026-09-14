# Complete factored-J solver discriminator: timeout, modular crash, and a new allocation overflow

2026-09-06. Owner `/root/model_productivity`; basis
`0d39df3c9fd69c939a8420c54d03228b9077777d`.

**VERDICT: NO UNIT OR PROPERNESS RESULT.** The complete exact-Q Singular run reached its original 600-second cap without a basis. The pinned, twice-patched msolve build crashed before reporting an F4 result. A further unsigned-32-bit allocation overflow is proved in the pinned source and reproduced without allocating a large array. Its responsibility for this SIGSEGV is a strong inference, not a debugger-confirmed claim. There was one complete-input attempt per engine, no retry, no enlarged solve, and no dropped row or variable.

## 1. Authority, frozen target, and custody

Root sent explicit GREEN at 11:12Z after its exact and scalar full-J replays completed. No Groebner invocation preceded that authorization. Only root-owned `i-0da0cebfc97c9fd54`, `172.30.0.56`, hostname `ip-172-30-0-56`, r7i.8xlarge, was used. No instance was launched, terminated, stopped, retagged, or otherwise adopted. Task artifacts live in the fresh worker subtree

```text
/home/ubuntu/full-j-solver-pilot-20260906
```

The actual total degrees are F=99, G=66; the mechanical frontier gate returns `NOT_CLOSED_BY_THIS_GATE` since gcd=33. The scope remains the frozen delta2, gauged stage-8 physical-polynomial family, not all degree-(99,66) maps. Its necessity for a hypothetical counterexample remains unproved.

The complete ideal is over Q, global dp, with the literal 600-coordinate order: 439 source coordinates, 160 Hfact coordinates, then Zj. All 1,629 rows and 11,299,180 literal terms remain: 160 monic graph definitions, 1,468 positive physical-J coefficients, and the genuine `Zj*J0-1`. No C elimination, rowless-variable removal, J0=1 gauge, or positive-high-band-only ideal was substituted. The positive-only proposal is not the authorized target; the inverse row is essential.

Frozen inputs, independently hashed before use:

| artifact | SHA-256 |
|---|---|
| completed Fable gate `xmodel/factored-jacobian-gate-fable5-20260906.md` | `c01996800fbb4084a640770f1edd21092fe2b23ae1e3b50281477767e5488535` |
| producer `complete_checked.sing` | `50792efed4a5ed47cf2da5bf1f0d3b65e4f68efcba8e528b7dc29a541b72e091` |
| producer `complete_export.generators.jsonl` | `39ea3365c8c83916c5f813be0b7719374dcad131cdd4b10ed24d25516bfae75f` |
| producer custody | `f9000c9fb461b052b076d2cc60649b4bd312e36d2d59ebb91c364e12ac7c26d0` |

The full completed gate was read. Its literal-stream and physical-map conclusions are consumed as stated; no source-necessity or T2/T3-equivalence claim is added. After both jobs terminated, **all 54 artifacts listed in the producer custody rehashed unchanged**. No original path was used as an output.

## 2. Complete input transformations and their checks

`worker.py prepare` checks the source whole-file hashes, header, coordinate order, all labels and sequential indices, the complete footer and generator-stream hash. For every row, its safely parenthesized rational expression is compared byte-for-byte with the corresponding checked Singular row. The Singular input changes only the parse-only footer, retaining the entire Q/dp ideal. Its new footer requests `slimgb`, interreduces a completed result, checks `reduce(1,G)` and `reduce(I,G)`, writes the basis, and prints unambiguous terminal markers. All these operations remain inside the single 600-second cap, including parsing.

For msolve, coefficientwise reduction Q -> F_1073741827 preserves the same 600 names, their order, and every monomial in every generator. Every rational denominator is checked invertible; a zero reduced coefficient would cause a fail-closed stop rather than silently dropping a term. All encountered denominators have only factors 2 and 3; the largest is 1944.

The first preparation rejected whitespace-bearing rational terms before completing either input; both rejected partials and `worker.v1.py` are retained. The repair removes whitespace before coefficient-token conversion. This was preparation, not a solver retry. The repaired preparation completed in 28.189 seconds.

Two complementary checks cover the modular conversion:

- Native FLINT Q/Fp micro-controls independently verify rational coefficient values while retaining variable subscripts and exponents. They reject the old whitespace handling, a coefficient-sign mutation, a denominator divisible by p, and a term becoming zero modulo p.
- `audit_modular.py` independently splits source and modular rows into signed terms, compares every monomial spelling and every coefficient value modulo p, and checks all row/term counts plus the original literal generator-stream digest. It completed in 19.789 seconds: **1,629/1,629 rows and 11,299,180/11,299,180 terms PASS; none removed**. This audit consumed the already frozen executed modular input after its failed run; it was not another solve.

Executed input hashes:

```text
complete.slimgb.sing:
f87c0718b7df56c2b421a9d145e0e30d4e337ac2dca4a4c73d036033a55487cb
complete.p1073741827.ms:
5a7f674325e9e8cb483234bd8b510f54bff387032498ed49ba76e084748517e2
```

The complete coordinate/ring map and row labels are in `evidence/map.json`. The independent term-pair audit is `evidence/modular.audit.json` (SHA `4b17d12672986d7a394e388a9750d9334df00161dd42c5f3c3cd99a4561bc7ec`), with the full compact row manifest `evidence/modular.rows.tsv` (SHA `14faa213a132ca85018b50974b1c8eeb27c4bf0bf1729d8a82e60f253ea9132e`).

## 3. Reviewed runner, build provenance, and controls

The unchanged `ops/run_capped.py` has SHA
`4435279df8f987c667ebc2fae8e4bd987916032561cb3faf1e07a57789d196c2`.
The COORDINATION operational rules and AUDIT's hostile-review/17-regression record were read, together with the runner's exact-PGID implementation. The new payload fails closed unless Linux, the exact EC2 hostname/DMI, fresh cwd, and registered job environment match. The runner starts the payload in its own process group; exec retains the registered PID for the CAS. No unrecorded inner timeout group is introduced.

A new no-CAS dummy let its leader exit while a same-PGID child held 64 MiB and ignored TERM. The runner observed 77,873,152 bytes aggregate RSS, validated the same start identity before TERM and KILL, and ended with complete cleanup and no live descendant. This exercises the actual launcher path rather than merely trusting a supervisor exit.

The Singular binary is 4.3.2, SHA
`90ab699b7a28486944a167e797d7c8dd38f8f949960b93ee7a6d08ff1c7c46f4`.
It used one thread, exact Q/global dp, 600 seconds and 64 GiB aggregate PGID RSS.

No previously reviewed patched msolve binary was available locally or on this worker. The source was cloned from `https://github.com/algebraic-solving/msolve.git`, pinned exactly to commit `185e7b92fa0687f4db68b0f2f453a835668ac132` (v0.10.1). Both existing patches received forward/reverse dry-runs and `git diff --check`:

```text
heap-sort-permutation.patch:
c49a9fb322c3c6518ff2234a7e521de3aa6a372efbe27dc4c9aa9360db3b2242
int64-input-offset.patch:
4f2e723575ff2acbfcee4144d4c2e47cd314f6f25d1241bd1286c202c3863055
```

The resulting `iofiles.c` and `neogb/io.c` hashes exactly match the completed class-A build provenance, respectively `e0107ae05994a3480ca95d0f289529b9fe4537826702458fe467b68652bae874` and `71077383a1b2c1bdb2c01cffd0956593879fe627ae13766fa3342a40247ef3e6`.

The first build stopped at missing autoreconf. Root subsequently authorized missing build prerequisites only. A recorded apt simulation showed **0 upgraded, 12 newly installed, 0 removed**. Installation and the before/after package census confirmed no existing package-version changes. The exact additions/versions are in `evidence/apt.custody.json`; they comprise autoconf/automake/libtool/pkg-config, their small dependencies, and matching FLINT/MPFR development headers. No shared msolve installation or existing runtime replacement occurred.

The resumed task-local build used `-O3 -march=native`, make -j8, and completed **64/64 upstream tests**; unit and proper-basis controls at p1073741827 also passed. Build elapsed 54.721 seconds, peak RSS 814,694,400 bytes. The executed launcher and its complete binary/library hashes are in `evidence/binary.json`; the ELF SHA is `1c9e48776d3dcef846149df1e55fb375ac280653c89408e5c0ae590eaa599ff1`, and patched libneogb SHA `4fd482dc7964dfca213c521136fc445c2e16b9727036c6de6e509f69d7768079` matches the prior terminal build. The new failure below demonstrates why passing these small controls does not certify large-input safety.

The modular launch used `-g 2 -t 8 -v 2 --random-seed 0`, the explicitly modular input, 600 seconds and 96 GiB aggregate PGID RSS. Both engine caps sum to 160 GiB; build/preparation did not overlap their joint execution. RSS is sampled with disclosed possible overshoot, not mislabeled as an address-space cap. The worker had no swap.

## 4. Terminal measured results

| complete-input engine | UTC interval | PID=PGID | terminal outcome | wall including parsing/cleanup | peak observed RSS |
|---|---|---:|---|---:|---:|
| Singular exact-Q slimgb | 11:19:26.025–11:29:26.984 | 54368 | WALL_TIMEOUT | 600.959 s | 35,739,922,432 bytes, 33.29 GiB |
| patched msolve, p1073741827 | 11:22:57.251–11:23:24.068 | 76287 | SIGNAL 11 | 26.817 s | 11,062,775,808 bytes, 10.30 GiB |

Singular printed `ALL_ROWS_PARSED`, `GENERATORS=1629`, `VARIABLES=600`, and `BEGIN_SLIMGB`; its diagnostic stream advanced through `4M...`. It never printed `END_SLIMGB`, any result block, `REDUCE_ONE`, or a dimension/basis size. There is no completed basis. TERM at the original deadline cleaned the exact registered group, with cleanup_complete=true and no live member. The extra 0.959 seconds is bounded termination/observation time, not an enlarged solve.

msolve printed only the seed message to stderr, no stdout, and produced a zero-byte basis file. It died of SIGSEGV, not the wall/RSS cap. No F4 completion, parser-success conclusion, unit, nonunit, dimension, or properness is inferred. The runner observed the group quiet and authoritatively reaped the signaled child. Its normal signal-exit telemetry leaves the termination-only cleanup fields null/false; that is not a live-process finding. A separate terminal process census confirms both registered groups empty.

Strict harvest rejects missing/duplicate terminal markers and incomplete output. **Neither outcome establishes a unit ideal or a proper ideal.** In particular there is no characteristic-zero-header msolve claim; the attempted characteristic is explicitly p. The exact-Q engine would need a completed reduced basis before any properness claim could even be considered. No result here is a JC2 proof or counterexample.

## 5. New proved allocation defect; crash attribution remains an inference

In the pinned, already twice-patched source,

```c
/* neogb/data.h */
typedef uint32_t len_t;
/* msolve-data.h */
typedef len_t nelts_t;
typedef int32_t nvars_t;
/* iofiles.c, both finite-field and rational input paths */
gens->exps = (int32_t *)calloc(all_nterms * gens->nvars, sizeof(int32_t));
```

The product is evaluated in unsigned 32-bit arithmetic **before** conversion to calloc's size_t parameter. Here

```text
required entries = 11,299,180 * 600 = 6,779,508,000
actual entries   = required mod 2^32 = 2,484,540,704
required bytes   = 27,118,032,000
allocated bytes  =  9,938,162,816
```

The earlier input-offset patch widens `store_exponent`'s argument and four call-site products. It does not widen these two allocation products. Thus the strengthened store offsets can write beyond the undersized buffer. The source files/types are retained in the compact evidence and remain hash-identical to the reviewed patch build.

`allocation_control.c` reproduces the original call-argument conversion using the actual typedefs, prints the values above, and allocates no array. Its negative control uses the former 6,448,959-term, 449-variable input, whose product stays below 2^32 and does not overflow this allocation. The check passed under the worker compiler. Source SHA:
`2275174b550d327baa7ed93939448061b4c6232de73ed02540d6e326f0317f8f`.

The undersized allocation is a proved source defect. Its agreement with an early SIGSEGV around 10.30 GiB is a **strong causal inference**, not a stack trace: core dumps were disabled and no crash debugger was run. No claim that these are the only remaining large-input hazards is made.

The next modular step, if separately authorized, should first widen and overflow-check both allocation paths and review the remaining count products, then validate the large-input parser. Merely raising memory/wall caps or reusing the two-patch binary would not address this proved defect. No third patch or second full-input attempt was made here. Until that repair is reviewed, this is not a fair F4-versus-slimgb throughput comparison and supplies no solver-speedup claim.

## 6. Terminal handoff

Worker remains running under root custody. All task arithmetic processes are terminal; both registered full-solver groups are empty. Dense inputs and any full build tree remain on the worker. Compact code, terminal transcripts, exact maps, all-row manifest, package additions, controls, source excerpts and telemetry occupy about 0.76 MB on the coordinator host, below the 10 MB limit.

Local evidence directory: `box/full-j-solver-pilot-20260906/evidence/`.

```text
custody.json SHA256:
89f877a6f26db5f563b0dd5d55d911f8462fc78137efb225fddac442e0351d0a
results.json SHA256:
f923f35a5782439c7c0df7608af2939b8c8f89556a9d8d5e5c7baa4a46d8830f
```

Custody contains every charged worker artifact path/hash, all 54 unchanged original hashes, exact launch argv/start identities, caps, terminal states, and the package-change record. Source/gate originals, shared ledgers, and sealed reports were not edited. No other worker, `jc2-lean`, live foreign report body, or ideation submission was used. No assertion of properness, chart necessity, all-degree exclusion, or JC2 resolution is promoted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14102`.
- Body SHA-256:
  `e0b0fd63466b6773161791f78c6ff00f64d8ce3013debae18682ac21b4301dd0`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
