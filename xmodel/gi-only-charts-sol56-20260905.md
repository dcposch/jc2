# G-only Moh-support charts for the residual with Moh bound at most 100

**Verdict: 0 DEAD, 0 BASIS FOUND, 6 COMPUTE-BOUND.** All twelve fibres were
emitted as six class-uniform full-G charts and every exact-\(\mathbb Q\) run
reached its 600 s watchdog without a UNIT or completed basis. Thus this lane
does not kill the Moh \(\le100\) residual, and it does not exhibit a point.

## 1. Scope and result boundary

This lane replaces the source-complete chart

\[
S_i(V)=D_i(V)\cup G_i
\]

by the smallest support chart proved by the frozen source-support theorem,

\[
G_i=\{(b,a):0\le a<K,\ 0\le b\le
\lfloor d(iK-a)\rfloor\},\qquad d=-\delta_{s'}>0.
\]

The coordinate is always \(\phi=(x,y+\eta(x))\). The chart is

\[
\begin{aligned}
h&=y^K+\sum_{(b,a)\in G_1}h_{b,a}x^by^a,\\
P&=h^e+\sum_{i=1}^{e}\alpha_i h^{e-i},\\
Q&=h^q+\sum_{i=2}^{q}\beta_i h^{q-i},
\end{aligned}
\]

where \(\alpha_i\) and \(\beta_i\) have support in \(G_i\),
\(\beta_1=0\), and the constant coefficients of \(\alpha_e\) and
\(\beta_q\) are gauged to zero. The production ideal is literally

\[
I_G=\operatorname{coeff}_{x,y,h}
   \bigl(J_{x,y}(P,Q)-c x^\ell\bigr)+(Tc-1)
\]

over exact \(\mathbb Q\). No total-degree cap, raw-only subchart, or support
smaller than \(G_i\) is consumed.

There is one executable production chart per class, not one per fibre. This is
not representative-fibre reasoning: \(G_i\) depends only on the class data and
is identical for every \(V\)-label in a class. Each of the twelve fibres has a
separate alias and specialization receipt, while the six canonical charts are
the only solve targets. The theorem supplies the coverage map; see
`xmodel/source-support-closeout-opus5-20260905.md:195-225` and the six-class
consumption statement at
`xmodel/moh-hsupport-gate-astra-20260905.md:188-199`.

The only promotable negative verdict is **DEAD** from an exact-characteristic-
zero UNIT result on this full chart with complete controls. A modular UNIT is a
screen only. A completed non-unit basis is reported as **BASIS FOUND** only with
its dimension and a full exact rational point checked against every generator
and \(Tc-1\). All other outcomes are **COMPUTE-BOUND**; that is the outcome for
each of the six charts below.

## 2. Frozen-input custody

The lane receipt is `xmodel/gi-only-charts-sol56-20260905.run.v2`. Before using
any charged source, its `charged_input_<i>_basename` and
`charged_input_<i>_sha256` fields were paired mechanically with `awk` to form a
`sha256sum -c` manifest rooted at `/tmp/jc2-lane.ymMTCq/inputs`. All eight
entries returned `OK`. The machine-readable duplicate receipt is
`box/gi-only-20260905/input-custody.json`, whose status is `PASS` and whose
`frozen_copy` field is true for every entry.

| charged frozen input | SHA-256 |
|---|---|
| `source-support-closeout-opus5-20260905.md` | `a67ffe4ab454e4350a1512a4f85e81f914d6e26b13654fef4aa680b948e13e9c` |
| `moh-hsupport-gate-astra-20260905.md` | `4437b1f2f8ed8058fc8900e3cdfcbbc67ec5f5c98eee9c0f04d78a0fb8370354` |
| `sprime3_compiler.py` | `7e6cfeedcee999a0163df9a23fd03fea695ca55a5de64e2e85b883a2fd4e1833` |
| `builder_fix.py` | `d6662abfec114a443712600f87e3e7b7064071f445d9b177d2f0ea13c9d3836b` |
| `guided_gb.py` | `501f3b1fed8ad0d26c7535a3c79d6ca74c448a4555f94570a4835d9f740781f3` |
| `fleet.sh` | `ab5ce23a113fc80b05e8261c0199d3513a7956aed3db3d033e0efb39bfe5a46d` |
| `dispatch.sh` | `dd1e148c9a0bdf2f7de0bd80a249c743d985a26f982245a375824ca89e4bc599` |
| `FALLACY-v2.md` | `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5` |

No mismatch was waived. The emitter imports the three charged Python modules
from the frozen directory and records their paths in
`box/gi-only-20260905/verification.json`. No ledger, `jc2-lean`, or
`ideation-*` artifact is modified by this lane.

## 3. The source-support theorem actually used

The cited theorem is conditional on exactly the following hypotheses:

- **(H1), licensed descendant:** the pair is a Proposition 6.3 descendant of a
  minimal Jacobian source with effective characteristic data, hence
  \(M'_{s'}\le n'-2\).
- **(H2), root replacement:** \(Q=T_1^\psi(P)\), equivalently the printed-row
  normalization \(M_1=-m'\).
- **(H3), terminal radius:**
  \(d=-\delta_{s'}=(\ell+1)/(n'-M'_{s'}-1)>0\).

These are the frozen statement at
`xmodel/source-support-closeout-opus5-20260905.md:197-208`. Its conclusion is
the support formula, the absence of \(\beta_1\), and the two allowed constant
gauges (`:210-216`). The proof uses the polynomial shear by the mean of the
\(Q\)-roots, approximate-root extraction, and monic division; the construction
and its specialization compatibility are recorded at
`xmodel/moh-hsupport-gate-astra-20260905.md:100-136`. In particular, monicity
prevents a hidden coefficient-field denominator or a branch on a leading
coefficient.

The theorem says that \(G_i\) receives every actual source pair satisfying
(H1)--(H3). It is a necessary over-approximation, not an existence theorem.
Therefore exact-Q UNIT on \(I_G\) is a valid source-support kill; NONUNIT alone
does not establish an actual source, an attained bound, or a Jacobian
counterexample. The present report makes no new exit-price assertion and hence
declares no `charge_basis` line.

## 4. Emission and exact chart inventory

The emitter is `box/gi-only-20260905/gi_only_emit.py`. It computes \(G_i\) with
the frozen compiler, applies only the terminal constant gauges, and refuses an
unexpected scalar shear (`gi_only_emit.py:194-205`). It asserts six classes and
twelve fibres (`:384-390`), audits every fibre, and emits one canonical chart
per class (`:393-415`). The P and Q term lists are deliberately placed in
P-first order before calling the inherited native builder (`:428-450`), so the
production target is literally \(J(P,Q)-cx^\ell\), rather than merely a
same-named native orientation.

`builder_fix` places all coefficients and `c` in the polynomial ring. Every
production builder has the form

```text
ring R=0,(y,x,<all G coordinates>,c),(lp(1),dp(N+1));
```

where the first block contains only `y`; `x`, all chart coordinates, and `c`
are in the second block. Thus `lead(h)=y^K` independently of the permitted
`x`-degrees. Here “unknowns without T” means the coefficient coordinates plus
`c`; it excludes the structural variables `y,x`. The solve ring removes
`y,x` after coefficient extraction and adjoins one further polynomial unknown
`T`. Ring and extraction requirements are the frozen design at
`xmodel/moh-hsupport-gate-astra-20260905.md:165-173`.

The exact class-uniform inventories are:

| class ID | fibres | \(K\) | \(e,q\) | \(d\) | \(\ell\) | \(|G_1(h)|\) | \(|G_i(\alpha_i)|\) | \(|G_i(\beta_i)|\) | unknowns without/with `T` |
|---|---:|---:|---:|---:|---:|---:|---|---|---:|
| `C_n24m16_Mm12_m2_5_ell1_s4` | 1 | 8 | 3,2 | 1/9 | 1 | 8 | 8,16,22 | 15 | 70 / 71 |
| `C_n18m12_M2_9_ell2_s3` | 2 | 6 | 3,2 | 3/8 | 2 | 11 | 11,25,37 | 24 | 109 / 110 |
| `C_n24m18_Mm15_14_ell1_s3` | 1 | 6 | 4,3 | 2/9 | 1 | 8 | 8,16,24,31 | 16,23 | 127 / 128 |
| `C_n24m16_M12_17_ell1_s3` | 3 | 8 | 3,2 | 1/3 | 1 | 17 | 17,39,59 | 38 | 171 / 172 |
| `C_n24m18_M9_20_ell1_s3` | 2 | 6 | 4,3 | 2/3 | 1 | 18 | 18,42,66,89 | 42,65 | 341 / 342 |
| `C_n16m12_M6_13_ell3_s3` | 3 | 4 | 4,3 | 2 | 3 | 24 | 24,56,88,119 | 56,87 | 455 / 456 |

Each total is the displayed block sum plus one for `c`; the terminal constants
have already been removed. Independent review recomputed every monomial from
the floor formula and matched the metadata exactly. It also checked that
`A<e>_0_0`, `B<q>_0_0`, and every `BB1` symbol are absent, that `c` occurs once
and last in the parameter list, and that each builder contains exactly one
`H0 = H0 - c*x^ell` target. The emitted metadata and verification logic perform
the corresponding checks at `gi_only_emit.py:457-529` and `:827-876`.

Generator counts are counts of nonzero extracted coefficient rows, not support
dimensions. In the displayed solve order they are
`66,150,173,247,560,756`, hence `67,151,174,248,561,757` after adjoining
\(Tc-1\). The same count applies to every fibre alias in its class: one
class-uniform G chart is sufficient for the theorem-backed kill attempt.

## 5. Twelve-fibre and class-union size accounting

All figures below are post-gauge intrinsic unknown counts including `c` and
excluding `T`. `D` is the raw Theorem-1.2 inventory, `S=D\cup G` is the frozen
source-complete inventory, and `zeroed` is exactly \(|S\setminus G|\). Because
\(S=D\cup G\), the audited equality
\(S\setminus G=D\setminus G\) holds blockwise.

| class / fibre | raw `D` | source-complete `S` | proved `G` | zeroed `S -> G` | coeff./total generators |
|---|---:|---:|---:|---:|---:|
| Mm12/m2/5 s4, `V1_1_6` | 77 | 77 | 70 | 7 | 66/67 |
| M2/9 s3, `V1_8` | 123 | 136 | 109 | 27 | 150/151 |
| M2/9 s3, `V3_8` | 88 | 111 | 109 | 2 | 150/151 |
| Mm15/14 s3, `V1_9` | 126 | 129 | 127 | 2 | 173/174 |
| M12/17 s3, `V2_1` | 162 | 218 | 171 | 47 | 247/248 |
| M12/17 s3, `V1_2` | 270 | 292 | 171 | 121 | 247/248 |
| M12/17 s3, `V3_2` | 120 | 185 | 171 | 14 | 247/248 |
| M9/20 s3, `V1_9` | 346 | 376 | 341 | 35 | 560/561 |
| M9/20 s3, `V4_9` | 248 | 343 | 341 | 2 | 560/561 |
| M6/13 s3, `V1_1` | 351 | 487 | 455 | 32 | 756/757 |
| M6/13 s3, `V1_3` | 393 | 473 | 455 | 18 | 756/757 |
| M6/13 s3, `V4_3` | 160 | 455 | 455 | 0 | 756/757 |

The corresponding class-union comparison is:

| class, solve order | `D` union | prior `S` union | `G` | `S-G` | coeff./total gens | `G` vs `D` |
|---|---:|---:|---:|---:|---:|---|
| Mm12/m2/5 s4 | 77 | 77 | 70 | 7 | 66/67 | smaller 7 |
| M2/9 s3 | 125 | 136 | 109 | 27 | 150/151 | smaller 16 |
| Mm15/14 s3 | 126 | 129 | 127 | 2 | 173/174 | larger 1 |
| M12/17 s3 | 270 | 292 | 171 | 121 | 247/248 | smaller 99 |
| M9/20 s3 | 346 | 376 | 341 | 35 | 560/561 | smaller 5 |
| M6/13 s3 | 407 | 487 | 455 | 32 | 756/757 | larger 48 |

This separates two statements that must not be conflated. The proved
\(h\)-support \(G_1\) has size `8,11,8,17,18,24`, while the raw class-union
`D1` h-support has size `11,18,8,47,26,33`; hence \(G_1\) is strictly smaller
on five classes and equal on Mm15. For the **whole parameter chart**, however,
G is smaller than D on only four classes and is larger for Mm15 and M6. The
first comparison is the source report's “five of six” statement; the second is
the honest computational-size comparison. The source-complete `S` chart is
larger than G on eleven fibres and equal on M6/`V4_3`.

Per-fibre block inventories, including the literal names of all zeroed
coordinates, are in the twelve files under
`box/gi-only-20260905/classes/*/fibres/`. Class totals and canonical builder
paths are in `box/gi-only-20260905/classes_manifest.json` and each
`classes/<class>/class.json`.

## 6. Strict specialization and orientation custody

The frozen source-complete builders are Q-first and compute
\(J(Q,P)-c_{\rm native}x^\ell\). Their separate custody chain uses

\[
c_{\rm native}\mapsto-c_{P,Q},\qquad
T_{\rm native}\mapsto-T_{P,Q},
\]

which maps the target to the negative of \(J(P,Q)-c_{P,Q}x^\ell\) and fixes
\(Tc-1\). A symbolic control and one retained Q-first G companion per class
verify this chain (`gi_only_emit.py:339-381`); it is not called the requested
coordinate-only map.

For that literal requirement the emitter instead creates one **P-first
source-complete S presentation for each of the twelve fibres** under
`classes/<class>/specialization-sources/`, using the frozen
`coeff_inventory_source_complete` and the production orientation. It checks
the S ring/setup, derivative orientation, byte-identical executable tails,
the exact zero list \(S\setminus G=D\setminus G\), termwise recovery of every
G setup polynomial, and identity on all retained coordinates, `c`, and `T`
(`gi_only_emit.py:547-623,703-823`). The top receipt
`verification.json` is PASS for six classes/twelve fibres, with every
blockwise subset and P-first coordinate-only specialization true.

As a concrete control, for s4/`V1_1_6` the P-first source presentation has 77
unknowns and the production G chart has 70. The coordinate-only map sets

```text
h_1_5, h_1_6, h_1_7,
A1_1_5, A1_1_6, A1_1_7,
A3_2_7
```

to zero and changes nothing else. The S/G builders both contain the P-first
`AA3,BB2` derivative probe and the target `H0 = H0 - c*x^1`; their executable
tails from `ideal HDIV = h;` are byte-identical. The receipt records this map
at `verification.json:53-60`.

The emitter also imports the frozen verifier's independent inventory arithmetic
(`verify_source_complete.py:23-26`). For every h/alpha/beta block it compares
compiler S, raw D, and G after the two permitted gauges and proves both
\(G_i\subseteq S_i\) and \(S_i\setminus G_i=D_i\setminus G_i\)
(`gi_only_emit.py:242-334`).

## 7. Generator extraction, exact-Q solver, and controls

Each canonical builder specifies every nonzero coefficient of
\(J(P,Q)-cx^\ell\) after monic h-adic reduction as a TSV row. The three
smallest builders completed natively. Generic Singular division became the
extraction bottleneck on the other three, so
`experiments/fast-extract/sparse_hadic_extract.py` performed the same
determinate division over the exact integer coefficient ring. It parsed the
unchanged builder-fixed ring and P/Q setup, kept every G coordinate, introduced
no auxiliary variable, and made no specialization. Its identity

\[
J(ah^r,bh^s)=h^{r+s}J(a,b)+h^{r+s-1}
\{s bJ(a,h)+r aJ(h,b)\}
\]

followed by top-down division by monic \(h=y^K+h_{<K}\) gives the same h-adic
remainder coefficients. On the three completed native controls the expanded
coefficient dictionaries agree exactly, row for row: 66/66, 150/150, and
173/173. For each large class the activation gate additionally recomposed the
rows at two full exact-integer assignments and matched literal
\(J(P,Q)-cx^\ell\), while reversed orientation and a one-term perturbation
failed as required and \(Tc-1\) passed. The activated results were 247 rows in
19.021 s/377,868 KiB, 560 in 50.886 s/1,345,180 KiB, and 756 in
155.771 s/2,767,076 KiB. Full custody is
`sparse-extraction-custody.json` (SHA-256
`90267fe5888b80e7cd8f9eba61c05d40c78d0c3ad0538e39a96760320d70d3c9`);
the independent audit is `experiments/fast-extract/independent-audit.md`
(SHA-256 `473d3293e8959ddfa1f257f1cc6db00a5b4dddc2460ad9649a993be90c1f1350`).

The guided emitter reads those rows and constructs a characteristic-zero
Singular ring on the chart variables, `c`, and `T`, adding exactly `T*c-1`.
Metadata records both generator counts; `gi_only_emit.py:915-953` is the
count-update path.

The production driver is `box/gi-only-20260905/solve_class.py`. Before solving,
it refuses metadata lacking the G-only, blockwise-subset, strict-specialization,
literal-orientation, and top verification receipts
(`solve_class.py:225-280`). It verifies that variables are distinct, that `c`
occurs exactly once, that `T` was not smuggled into the chart count, and that
the extracted and declared generator counts agree (`:697-799`). The exact-Q
watchdog is constrained to at most 600 seconds (`:660-692`, `:823-830`).

The battery requires the exact-Q ring and `T*c-1`; passing ring, known-empty,
and known-nonempty controls; the declared generator count; one zero normal form
per input generator; complete guided markers; one completion marker; no
Singular error; and clean exit (`solve_class.py:486-521`). DEAD requires this
complete run plus UNIT. BASIS FOUND additionally requires an exact rational
assignment with `c!=0` annihilating every row and `T*c-1`; otherwise the result
is COMPUTE-BOUND (`:533-645,850-879`).

The optional msolve run is over the declared prime 1073741827 and is labelled
`MODULAR SCREEN ONLY — NEVER A CHARACTERISTIC-ZERO KILL`. Its result is never
consulted by exact classification; see `solve_class.py:334-483` and
`:763-785`.

## 8. Production solve results

The order is smallest chart first. RSS is peak process-group KiB. `pre PASS`
means the characteristic-zero ring, known-empty, known-nonempty, and declared
generator-count controls printed before `std`; no run printed the later
basis/NF/completion markers. A dash for dimension/sample means none was found,
not dimension zero.

| order | class | unknowns `c`/`+T` | coeff./total gens | modular screen only | exact-Q (`wall s`; RSS KiB) | controls; dim/sample | verdict |
|---:|---|---:|---:|---|---|---|---|
| 1 | `C_n24m16_Mm12_m2_5_ell1_s4` | 70/71 | 66/67 | timeout 600.121; 9,143,032 | 600.010; 923,888 | pre PASS; incomplete; -/- | **COMPUTE-BOUND** |
| 2 | `C_n18m12_M2_9_ell2_s3` | 109/110 | 150/151 | timeout 600.010; 8,125,312 | 600.010; 1,907,700 | pre PASS; incomplete; -/- | **COMPUTE-BOUND** |
| 3 | `C_n24m18_Mm15_14_ell1_s3` | 127/128 | 173/174 | timeout 600.009; 9,594,044 | 600.010; 667,436 | pre PASS; incomplete; -/- | **COMPUTE-BOUND** |
| 4 | `C_n24m16_M12_17_ell1_s3` | 171/172 | 247/248 | timeout 600.010; 17,619,012 | 600.009; 5,219,564 | pre PASS; incomplete; -/- | **COMPUTE-BOUND** |
| 5 | `C_n24m18_M9_20_ell1_s3` | 341/342 | 560/561 | unavailable: exact-size guard | 600.010; 20,692,452 | pre PASS; incomplete; -/- | **COMPUTE-BOUND** |
| 6 | `C_n16m12_M6_13_ell3_s3` | 455/456 | 756/757 | emitter timeout 180.073; 958,040 | 600.009; 48,355,992 | pre PASS; incomplete; -/- | **COMPUTE-BOUND** |

Every exact process returned `-15` from the watchdog. Accordingly `unit=null`,
dimension is absent, and no sample verification was attempted. M9's modular
emitter refused because `10,537,074 * 342 = 3,603,679,308` exceeds msolve
0.10.1's `2,147,483,647` size limit; M6's emitter timed out. The four completed
modular runs also timed out and none is promoted.

The strict aggregation is `box/gi-only-20260905/final-solve-summary.json`
(SHA-256 `906af3a63e4cbb4f16345c9934848a45c4c21353e76ec5daf36d720471026084`).
It re-counted every row, re-parsed the exact controls, re-derived all verdicts,
and checked immutable fleet/canonical replicas. Its selected result hashes are:

```text
c9f102e850f9d88ebb6f633137159df0bbdf17ba2802114e58764d05fee83ba1
f0ff29eba04bebf3ec134153d7dc5619307427df53926214499b36648e69168c
03c12c1d9b41daba3e292769a4814ab8da11d9ec11dc991b49c24f576e3aae58
648ada007281261ee88dd7b0cc9c25fbd62268a5fcec4bd74860c75f464c7bcb
db964ce2da1d1aed8732ae4dbfe6d1629f461bb4708faad49cbc62ddf1edc693
f9d4a19749135789ba62661666982b13c687e0b7137fb945069ac1eb00a68eec
```

Each adjacent dispatch log is byte-identical to its result. Exact stdout,
stderr, rows, guided input, metadata, and hashes are indexed under `custody`;
only superseded prebuild class/meta hashes and the non-promotional worker
msolve binary are declared-only exceptions.

Before sparse activation, native extraction timed out for M12 and M9
(1,800.010 s; 3,331,876 and 3,421,004 KiB). Later M12 and M6 attempts were
stopped after the exact sparse rows passed, at 1,040.170 s/3,166,696 KiB and
1,237.321 s/6,069,248 KiB. They remain historical extraction attempts, not
exact-`std` results.

## 9. Fleet custody and termination

The lane wrapper `box/gi-only-20260905/fleet_lane.sh` restricts every mutable
operation to four explicit ID/IP pairs (`fleet_lane.sh:1-24`) and refuses an
unknown worker or class (`:26-42`). It rechecks the charged fleet, dispatch,
compiler, builder-fix, and guided-GB hashes before synchronization (`:44-65`).
The outer guard covers extraction/screen setup while retaining the 600-second
exact-Q watchdog (`:68-78`). Collection pulls a complete named-class snapshot
and dispatch log; termination accepts only explicit allow-listed IDs. Exactly
four on-demand, owner-tagged workers were launched:

| instance | running IP | type | launch UTC | final classes | termination UTC/state |
|---|---|---|---|---|---|
| `i-0889ee47ceb889561` | 172.30.0.236 | c7i.8xlarge | 14:38:20 | order 1 | 15:20:13, terminated |
| `i-0d8bf8dd339a2e161` | 172.30.0.238 | c7i.8xlarge | 14:38:20 | order 2 | 15:21:32, terminated |
| `i-0fe012c4207c7a220` | 172.30.0.235 | r7i.8xlarge | 14:38:22 | orders 3,4,5 | 16:24:40, terminated |
| `i-0a067499279342f0c` | 172.30.0.75 | r7i.8xlarge | 14:38:22 | order 6 | 16:24:40, terminated |

Dates are 2026-09-05 UTC. The first wave used a 3,900 s outer guard; resumed
large-chart jobs used 5,200 s. Collection preceded reuse or termination. The
last two IDs were terminated explicitly and AWS then reported both
`terminated`; the two c7 IDs had already reached that state. Machine custody
is `box/gi-only-20260905/fleet-custody.json` (SHA-256
`5a0726376f1aa02c542b33baf3bc3657ff144002f1b3199aebc05f435b6415cd`).
No pre-existing or non-lane worker was mutated or terminated.

## 10. FALLACY-v2 audit and final interpretation boundary

The following boundaries governed promotion:

- The chart is the full proved \(G_i\) envelope in every block. Any chart that
  drops even one \(G_i\) coordinate is not a theorem-backed kill, regardless
  of how quickly it returns UNIT.
- `D_i` is decorative for source coverage, but this does not license an
  arbitrary subchart or a total-degree cap. The precise zero map is from
  `S_i=D_i union G_i` to the whole `G_i` chart.
- The physical shear coordinate, root/cover labels, and valuation data are not
  identified with one another. The specialization only changes declared
  coefficient coordinates.
- The terminal translations of P and Q remove exactly the constants of
  \(\alpha_e\) and \(\beta_q\); they do not authorize any additional gauge.
- The saturation equation is explicitly `T*c-1` in a polynomial ring. No
  fraction-field nonvanishing assumption substitutes for it.
- The Q-first frozen custody chain and the P-first production specialization
  are distinct maps. Matching parameter names is not an orientation proof.
- A finite-field UNIT is never a kill. It may be reported only as a modular
  screen beside the mandatory exact-Q outcome.
- An exact-Q NONUNIT without a verified full sample point remains
  COMPUTE-BOUND. Even a verified point is a point of the necessary
  over-approximation; it is not by itself an actual source or counterexample.
- No lower-bound statement is promoted to attainment, and no missing solve
  field is filled by analogy with an older S-chart allocation failure.

The support/emission side is complete: all twelve fibres map to six exact
G-only charts, and all inventories, gauges, rings, orientations, counts, and
coordinate-only specializations pass the frozen and independent checks. The
solve side remains honestly open: six watchdog expiries establish neither
UNIT nor nonemptiness. Therefore no theorem-backed kill and no basis-found
claim is made.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `22571`.
- Body SHA-256:
  `1d08e82474c9a7c46f12c77ca28b5d0ed82a1a14463bdb029fb7eb836bc73003`.
- Frozen basis: `ff1ada61ed0436f3d5993fbbbfe41baef6e91bd4`.
