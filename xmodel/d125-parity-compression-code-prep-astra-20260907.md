# D125 parity compression: construction/cost precursor

2026-09-07, PREP ONLY. **The original-lambda3 22-coordinate slice constructor and literal-row replay library are implemented; no production construction, full-source read, AWS action or solver occurred.** No expansion-size or runtime advantage is claimed. Root relayed acceptance of the restricted-source/T2[s] mathematical gate during preparation (`3940ba00aca8033bd8206250dc007881b9b50113061dc85588e06d1ccbe7c47d`); its body was not read here. This new implementation remains ungated. Its conservative provisional output label is intentional.

## Exact source and coordinates

The client is the complete unequal/rational receiver with A/B polygons `(0,0),(0,15),(9,6),(2,1)` and `(0,0),(0,25),(15,10),(1,0)`. Write H=p²(p³+g³). Entire outer faces are H³/H⁵; entire inner faces are g²p+g⁹p⁶ and 5g/9+5g⁸p⁵/3+g¹⁵p¹⁰, including prescribed zeros. Both constants remain zero. The scalar is exactly −5/9, so the target is `[A,B]+5g²/9`, with `[A,B]=A_g B_p−A_p B_g`. Fixed unit guards remain traced.

Restrict only to μ2: λ2=0, all even-total-degree A/B free coefficients zero, λ3 unrestricted. The lift is `g=v^-1, p=v^4*u-lambda3*v-v^-1`. This is a sufficient symmetry-fixed source client, not a normalization covering every counterexample. Actual source degrees are75/125, not receiver15/25. No lambda3=1, moving-face variant, B-Hermite subtraction or additional gauge is introduced.

The production metadata function filters the frozen actual coefficient maps: 33 A+94 B+λ3=128 baseline variables. The output records that complete name vector and every one of the original269 variable maps. It checks13 A pivots and20 retained A coordinates. The metadata function itself was **not invoked locally**; counts originate in the sealed actual-slot witness and are enforced when a future authorized construction runs.

The reduced variable order is the20 retained A names in original source order, `beta5_slice`, then λ3:22 variables. Full mode inserts `shear_s` immediately before λ3:23. These are presentation generator counts, not dimensions. All coefficient arithmetic is Q with sorted repeated-index monomials; `dp` is merely declared for a possible later exporter, not used in any solve.

## Implemented reconstruction

First descend the odd A levels13,11,…,1. At level s the pivot points are `(i,s-i)`, `0<=i<ceil(s/5)`. The exact Hermite matrix is

`M[t,i]=(-1)^(s-i-t)*binom(s-i,t)`.

The literal negative-v row at `(t,5t-s)` is evaluated with current pivots zero; its solution is minus the constant inverse times that forcing vector. All13 graph values are retained. No parameter division occurs.

Next build B in the gauge slice with `[p^15]B=0` and `[p^5]B=beta5_slice`, descending odd degrees23,…,1. The matrix of `[H³,B_d]` has rows indexed by g-exponent r and columns by g-exponent i:

`L[r,i]=((r+1-i)*d-15*i)*h[r+1-i]`, where `h[0,3,6,9]=(1,3,3,1)`.

The actual free slots supply the columns, in descending i order; omit only i=0 at d=5,15, the two kernel coordinates. Deterministic constant row reduction selects independent *original* Jacobian rows. Each block stores its selected row labels, pivot points and exact rational inverse. All92 pivots must be obtained, and their original rows are recomputed after reconstruction and required to vanish. Fixed inner coefficients are included in the forcing, not treated as variables.

Full mode then adds **sA at every B coefficient**, not only sH³. In particular original beta5 equals `beta5_slice+s*[p^5]A`, and original beta15 equals s. The inverse subtracts the whole sA. Every fixed coefficient is checked after this operation. A-negative rows are imposed before this shear; the implementation does not use B-negative invariance without them.

## Complete rows and replay

`construct.py` emits one exclusive canonical JSONL file: header;269 indexed original-variable maps; graph records; **803 original-row traces**; and a complete digest/count footer. The row order matches the frozen exporter:31 fixed assignments, all660 safe-envelope Jacobian slots, all30 A-negative slots, all75 B-negative slots, six vertex guards and the scalar guard. The660 envelope is retained despite its known nonminimality. No low Jacobian equation, including the target, is dropped.

Every trace retains its original index and label. Exact-zero rows have null residual index and empty terms; every nonzero row receives the next residual index. All A-negative rows and selected graph rows must evaluate exactly to zero. All other residuals remain, regardless of dependence. Residual counts, terms, unused coordinates, maximum intermediate terms/degree/coefficient bits, map terms, elapsed time and process RSS are reported, not guessed.

`replay.py` supplies a host-context-only callback for a future pinned caller. It first verifies frozen source JSONL hash `b8db27661d1bfd3dcc5dfe1d1271b78c3f6375e06201654977a51380cd6ebcac`, then substitutes the269 maps into **every literal803 original equation**, checking each trace, residual index and both stream footers. It reuses exact multiplication but not the constructor's Jacobian/lift forcing formulas. Original fixed coefficients are not substitution variables, so their support/face data stay those of the pinned original stream. This is an exact substitution replay, **not an independent certificate of graph invertibility**; that still needs code review against the accepted graph theorem. The full callback has not run.

## Controls, cost ceiling and remaining gate

The final suite passed13 methods normally and under `-O`, combined0.413 seconds, with CPU24 seconds/AS512MiB/combined wall30 seconds enforced by the tiny runner. It exercised an actual d=5 B block and H kernel, d=1 pivot, a2×2 Hermite orientation, a small complete A-lift graph, whole lower-coefficient shear inverse, source-row zeros/duplicates, omitted or changed residuals, changed fixed nonzero/zero faces, wrong target/guard, invalid wire/footer, exclusive creation, pre-multiplication/pre-wire limits and absent production context. Actual mutations were rejected; zero AST Assert nodes. No full degree15/25 constructor or complete matrix census ran locally.

Future production fails absent explicit construction-only root GREEN, accepted symmetry gate pin, nonempty job/registration, exact Linux/Amazon EC2 instance DMI/boot/cwd and source/code pins. Internal ceilings:300 wall/CPU seconds,4GiB address space,128MiB single-artifact bytes,100,000 terms per polynomial,1,000,000 multiplication pairs and retained graph terms,4,096 coefficient bits. Term/pair bounds precede arithmetic; a conservative byte bound precedes rational wire allocation/serialization. Output creation is exclusive; no complete footer is written after a failed graph/count check. Ordinary failures expose partial cost telemetry; hard caps require the future external runner's terminal receipt.

These are ceiling preparations, **not an authorized experiment**. A future root-reviewed capped caller should combine construction and literal replay within one chosen budget, pin the replay library, enforce exact-group RSS/cleanup, separately cap logs and preserve partial output. Internal FSIZE is per regular file, not an aggregate log quota. Neither that caller nor a solver adapter is added here. First measure expansion and replay cost on one slice; stop on any cap/failure without retry. No worker restart is authorized.

All source/code/evidence pins are in `box/d125-parity-compression-code-prep-20260907/pins.json`; terminal custody is beside it. The main constructor hash is `22173cc6a9217a90a8537081a1229b01e58017990b728291285e8cfc01a332a2`; replay hash `2dbb7464fd7b59e361f34b5a705cc7359b98001bf570a80fc77f441e029c2a17`; final control receipt `a5dc380f372d452212a657fe412570f0d93d54c9a969fe593a67a65038a99d64`. The baseline and exact-arithmetic copies remain byte-identical to reviewed predecessors. Only named sealed reports/scripts were read; no live review, normalized-variant artifact, shared ledger or protected project was accessed. All owned subprocesses returned/reaped; all writers are terminal on publication. **No point, exclusion, ideal decision or source-count change follows.**

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8255`.
- Body SHA-256:
  `4a63a6e7d5000ebc3b543e4dcd88401258aea8637a120cea9df94c21b29f1b92`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
