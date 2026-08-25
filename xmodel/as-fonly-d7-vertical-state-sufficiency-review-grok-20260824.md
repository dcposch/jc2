# Hostile different-model review — AS F-only vertical D8 state sufficiency

| Field | Value |
|---|---|
| Claim under review | Frozen producer: the displayed corrected vertical D8 `7 x 5` system is the coefficient map `M(X,Y)=(-A X+B Y, -H X-A Y)` with `H=h^3`, `deg X<=2`, `deg Y<=1`. Over any field, `Msharp M=M Msharp=(A^2+H B)I`. On `Delta!=0` a capped solution exists iff both adjugate numerators are divisible by `Delta` and the quotients obey those degree caps; the two `Delta=0` strata have the stated one-line criteria. Geometric ranks are exactly `5,3,2,0`. A literal-F3 replay against the frozen corrected column matches all `1594323` assignments, all `314127` compatible assignments, the fibre histogram, both stream hashes, and a no-cap negative control of exactly `202176` false positives. This is a state-compression theorem for the displayed matrix, not a next carry, all-depth, lift, or JC2 claim. Interpretation of the column as the exact AS successor remains review-gated |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking remarks below; the corrected census package's different-model review is still active, so the AS-successor reading of the column is correctly *not* claimed as reviewed; next divided carry, algebraic-closure classification, all-depth lift/no-lift, characteristic zero, a counterexample, and JC2 are correctly *not* claimed) |
| Evidence tier | independent `2 x 2` multiplication over `Z[A,B,H]` for both products, including sign-flip attacks; kernel-dimension argument for ranks `5,3,2,0` over an arbitrary field; regeneration of the frozen `7 x 5` core and affine column from `generate_corrected.py`, matched termwise to the displayed Sylvester form with polynomial entries `-h^3` not `-h`; independent F3 Gaussian rank versus an independently coded state test on all `1594323` points; multi-prime random-target checks; explicit reconstructed solutions in every stratum and one no-cap false positive; registered `./replay_all.sh` as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD at launch | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (the charged freeze basis) |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (unchanged) |
| Review window (UTC) | 2026-08-24T21:05:27Z – 2026-08-24T21:18:58Z |
| Python | host CPython 3.14.6 (hashes, integer identities, independent F3 census, multi-prime attacks, registered replay) |
| Singular | 4.4.1 (present; not used as mathematical evidence) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, freeze, and named payloads reread in full before any verdict:

- `xmodel/as-fonly-d7-vertical-state-sufficiency-20260824.md` (SHA-256 `410235081a54470a377d8d107a1982d34d507040718b945d11ee99dc4d1e5fe4`)
- `cases/as_fonly_d7_vertical_state_sufficiency_20260824/FREEZE.txt` (SHA-256 `b842a03e35bab622939dc22f69c5eafbcd59e6ea2c4aba227c49df9db99b9aee`)
- `cases/as_fonly_d7_vertical_state_sufficiency_20260824/MANIFEST.sha256` (SHA-256 `ba28e9132b30a9cb7a794dc3da1a55c518c1b9c1253817ffde5fdbb90f539e36`)
- `cases/as_fonly_d7_vertical_state_sufficiency_20260824/README.md` (SHA-256 `3e932ae902ab2de6baddf77e3b4353791d099a07814070e0abc400dc60a13938`)
- `cases/as_fonly_d7_vertical_state_sufficiency_20260824/check_matrix_identity.py` (SHA-256 `147cb423eb02f303974196ba06a7eb0a7bb632af417c7dab75c1410b4bd354ab`)
- `cases/as_fonly_d7_vertical_state_sufficiency_20260824/check_vertical_state.py` (SHA-256 `66b42abdf3c1d2174b77d609936e4b3f79e59ea302aeccdc660b157d08ac27de`)
- `cases/as_fonly_d7_vertical_state_sufficiency_20260824/replay_all.sh` (SHA-256 `c547669f9d2409635e1e13afec149d6f3ff2c473e27fb2472abe51fa8a3b3d22`)

Frozen corrected post-D10 D9/D8 producer, consumed as the integer-source emitter of the displayed matrix and column, never as a reviewed AS-successor theorem:

- `xmodel/as-fonly-d7-postd10-d98-f3-corrected-20260824.md` (SHA-256 `9cc39af35e1d52c9673755b79392e62bb265f78dc38bd9110cd37a992115c2d8`)
- `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/generate_corrected.py` (SHA-256 `a71daa0cb525bac229afb91c76987c8f25c1e2d63683caa10ff45d3364c658e5`)
- `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/audit_corrected_frobenius_rows.py` (SHA-256 `77485e9d583dd621c8ae412fa70bab3c2aa5b7605bebe03e0b74a3c4dc87689c`)
- `cases/as_fonly_d7_postd10_d98_f3_corrected_20260824/FREEZE.txt` (SHA-256 `bf7ce39ae1cf7cc6338c006cd2cd59d11a387d8644d740e6faee2cb63229a264`)

Confirmed omitted-Frobenius erratum, consumed only for the preservation/retraction boundary and to refuse reuse of quarantined columns/counts:

- `xmodel/as-fonly-d7-postd10-d98-f3-erratum-20260824.md` (SHA-256 `26dd0908295bfbcc36ad2f0efe59b645ce1dd11411fd88ab8e37337a74fc0d7d`)
- `xmodel/as-fonly-d7-postd10-d98-f3-erratum-review-grok-20260824.md` (SHA-256 `c97330558a53ad3caa82d1bf53f642f68139d453edbe96f541a55eece331ad8a`), overall **CONFIRMED**

The currently active different-model review of the corrected census package has **not** completed (`xmodel/as-fonly-d7-postd10-d98-f3-corrected-review-claude-20260824.md` is absent; its log is a two-line launcher stub). It was not consumed.

The charged freeze basis is `2e6104a417cfe15a93a901aa0a9129094a2ae11b`. Review started and closed there. Named producer artifacts remain uncommitted. Recomputed producer hashes at close match the launch table. No producer, case, canonical, prompt, log, run, coordination, erratum, or other review file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp/as_d7_vertical_state_review/` and in ephemeral interpreters. `check_matrix_identity.py` and `check_vertical_state.py` were not imported as mathematical evidence. `generate_corrected.py` was used only as the frozen integer-source emitter of the `7 x 5` core and affine column.

Tried hard, and failed, to flip a sign in `M` or `Msharp` and still obtain `Delta I`; to cancel `Delta` in the truncated coefficient module `k[z]_{<=3} ⊕ k[z]_{<=2}` rather than in the domain `k[z]`; to replace polynomial `H=h^3` by `H=h` over a field where those functions differ; to find `A^2=0` with `A≠0` in `k[z]_{<=1}`; to produce a specialized rank one or four; to make divisibility without quotient caps equivalent to capped solvability; to confine the no-cap false positives to characteristic three; to change table (11) by declaring `deg 0 = -1`; to leak an all-depth, lift/no-lift, characteristic-zero, counterexample, or JC2 inference out of the stated scope; and to treat the regenerated column as a different-model-confirmed AS successor.

---

## Promotion

**Accept `THE DISPLAYED CORRECTED VERTICAL D8 7 BY 5 SYSTEM IS THE COEFFICIENT MAP M(X,Y)=(-A X + B Y, -H X - A Y) WITH H=h^3 AND SOURCE CAPS DEG X<=2, DEG Y<=1. OVER ANY FIELD, MSHARP M = M MSHARP = (A^2+H B)I. ON DELTA!=0 A CAPPED SOLUTION EXISTS IF AND ONLY IF DELTA DIVIDES BOTH ADJUGATE NUMERATORS AND THE QUOTIENTS OBEY THOSE CAPS; THE TWO DELTA=0 STRATA HAVE THE STATED ONE-LINE CRITERIA, INCLUDING A=0 WHEN H=0 AND THE B=0 SUBCASE. THE ONLY GEOMETRIC RANKS ARE 5,3,2,0. AGAINST THE FROZEN CORRECTED COLUMN, THE CRITERION MATCHES ALL 1594323 LITERAL F3 ASSIGNMENTS AND ALL 314127 COMPATIBLE ASSIGNMENTS, WITH THE STATED STRATUM TOTALS, FIBRE HISTOGRAM, AND STREAM HASHES. DIVISIBILITY WITHOUT THE QUOTIENT CAPS ACCEPTS EXACTLY 202176 INCOMPATIBLE POINTS, WITH THE STATED DEGREE-PATTERN TABLE. THIS IS UNCONDITIONAL FOR THE DISPLAYED MATRIX AND AN EXACT LITERAL-F3 COMPARISON FOR THE REGENERATED COLUMN. IT IS NOT A REVIEWED AS-SUCCESSOR THEOREM, A NEXT DIVIDED CARRY, AN ALGEBRAIC-CLOSURE CLASSIFICATION, AN ALL-DEPTH LIFT OR NO-LIFT, A CHARACTERISTIC-ZERO STATEMENT, A COUNTEREXAMPLE, OR JC2.`**

On the displayed matrix, after the triangular coordinates `(P,Q,R,T)` of the frozen corrected producer:

- Direct expansion over `Z[A,B,H]` gives both
  `Msharp M = Delta I` and `M Msharp = Delta I`
  with `M=[[-A,B],[-H,-A]]`, `Msharp=[[-A,-B],[H,-A]]`, and `Delta=A^2+H B`. Every one-sign flip of the `(1,2)` or `(2,1)` entry of either factor destroys at least one of those identities.
- If `Delta≠0` in the domain `k[z]`, a pair `(X,Y)` of the source degrees solves `M(X,Y)=(u,v)` if and only if `Delta` divides `NX=-A u-B v` and `NY=H u-A v` and the unique quotients satisfy `deg(NX/Delta)<=2`, `deg(NY/Delta)<=1`. Necessity is `Msharp M=Delta I`. Sufficiency multiplies `Msharp(u,v)=Delta(X,Y)` on the left by `M` and cancels the non-zero-divisor `Delta` in `k[z]`, not in a truncated coefficient space. The quotient bounds are exactly the source caps.
- If `Delta=0` and `H≠0`, then `H` is a unit of `k` and `B=-H^{-1} A^2`. The single relation `H u-A v=0` is necessary, and `Y=0`, `X=-H^{-1} v` is a capped solution; `deg v<=2` makes the cap on `X` automatic. The identity `NX=-H^{-1} A·NY` shows that this one relation is the full row syzygy.
- If `Delta=H=0`, then `A^2=0` in the domain `k[z]`, hence `A=0`. The map becomes `(X,Y)↦(B Y, 0)`. If `B≠0` the image criterion is `v=0` and `u=B Y` for some `deg Y<=1`. If `B=0` it is `u=v=0`.
- These four strata are disjoint and exhaustive. Rank-nullity on the five-dimensional domain gives ranks `5,3,2,0` respectively, and forbids ranks one and four.
- Regenerating the frozen vertical core from `generate_corrected.py` produces remaining labels `M_0_9,M_3_6,M_6_3,M_9_0,M_0_8,M_3_5,M_6_2` in unknowns `(d7_1,d7_4,d7_7,d6_1,d6_4)`, and the `7 x 5` coefficient matrix equals the displayed Sylvester form, including polynomial entries `2 h h h = -h^3` in characteristic three. The affine system is `M(X,Y)+b=0`, so the theorem is applied to `(u,v)=-b`.
- An independently coded F3 census of all `3^{13}=1594323` regenerated assignments has zero theorem/direct-rank mismatches, stratum totals (8), fibre histogram (9), both stream hashes (10), no-cap count `202176`, and degree-pattern table (11). All `202176` no-cap false positives have `deg Delta ∈ {0,1}`; when `deg Delta=2` the caps are automatic.

**Do not promote this to:** a different-model confirmation that the regenerated column is the exact AS successor (that review is still active); a next divided carry; an algebraic-closure or Fitting classification of the inhomogeneous family; emptiness or nonemptiness of `FONLY_(3,7)(D=7)`; all-depth lifting or nonlifting; a characteristic-zero lift or no-lift theorem; a counterexample to JC; or any JC2 inference. Do not replace `H=h^3` by `H=h` outside literal F3 points. Do not cancel `Delta` in a truncated polynomial ring. Do not read divisibility of the adjugate numerators, without the two quotient caps, as the bounded state. Do not reuse the quarantined post-D10 columns or the counts `50939/177147`.

**Smallest honest successor.** Wait for the corrected census package's different-model review to close before treating the regenerated column as the exact AS successor. Independently of that, the two capped adjugate quotients are the complete D8 state for the displayed matrix; the next honest arithmetic step is to impose the following divided carry on those two polynomials, not to enlarge this gate into a tower statement.

---

## Quarantine

The following readings are refused and must not be reused as live mathematics:

- this gate as a reviewed proof that the frozen corrected column is the exact AS successor;
- this gate as a next divided carry, a complete D8-to-D7 classification, or emptiness/nonemptiness of `D=7`;
- this gate as all-depth lifting or nonlifting, a characteristic-zero statement, a counterexample, or JC2;
- cancellation of `Delta` in `k[z]/(z^4) ⊕ k[z]/(z^3)`, or in `F_3^7`, in place of cancellation in the domain `k[z]`;
- replacement of polynomial `H=h^3` by `H=h` in the displayed matrix or in the algebraic criterion, except as an F3-pointwise coincidence `a^3=a`;
- divisibility `Delta | NX, NY` without the quotient caps (4) as a state description;
- the four geometric ranks as a scheme-theoretic Fitting classification of a family over an algebraic closure (they are ranks of the specialized capped map);
- the quarantined post-D10 inhomogeneous column, the counts `50939/177147`, or the four-variable Frobenius fibre `(f_a,f_b,f_c,f_d)` as complete.

Producer strings `PASS-FORMAL-ADJUGATE-IDENTITY`, `PASS-VERTICAL-STATE-SUFFICIENCY`, and `PASS-AS-D7-VERTICAL-STATE-SUFFICIENCY-ALL` were not used as evidence. Independent reconstruction, not the producer scripts, is the evidence for every numbered claim. The registered replay was rerun unmodified as a regression only.

---

## Scope (not enlarged)

One prime `p=3` in the census; one total-degree cap seven; the displayed vertical D8 `7 x 5` after the frozen triangular coordinates; an algebraic state theorem for that matrix over an arbitrary field; an exact literal-F3 comparison against the regenerated corrected column. No rectangular support, no enumerator, no AWS, no gauge cap, no next carry, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | `Msharp M = M Msharp = (A^2+H B)I` over `Z[A,B,H]`, with the displayed signs `M=[[-A,B],[-H,-A]]` and `Msharp=[[-A,-B],[H,-A]]` | **CONFIRMED** | a leftover sign on `B` or `H`; one product holding and the other failing; the identity requiring characteristic three |
| 2 | On `Delta≠0`, capped solvability is equivalent to `Delta | NX, NY` together with `deg(NX/Delta)<=2` and `deg(NY/Delta)<=1`. Cancellation is in the domain `k[z]` | **CONFIRMED** | a capped solution with a nonzero remainder; a pair of legal quotients whose `M`-image is not `(u,v)`; cancellation used in a truncated ring; uniqueness failing while `Delta≠0` |
| 3 | On `Delta=0`, `H≠0` the criterion is `H u-A v=0`, and `Y=0`, `X=-H^{-1} v` is a capped solution. On `Delta=H=0` one has `A=0`; if `B≠0` then `v=0` and `u=B Y` for some `deg Y<=1`; if `B=0` then `u=v=0` | **CONFIRMED** | a rank-3 point with `NY≠0` in the image; `A≠0` on `H=0`; a nonzero `B Y` of `deg Y<=1` missing from the image; the `B=0` zero map accepting a nonzero target |
| 4 | The four strata have geometric ranks `5,3,2,0`. Ranks one and four do not occur | **CONFIRMED** | a specialized `7 x 5` of rank 1 or 4 over any field; kernel dimension other than `0,2,3,5` on the four strata |
| 5 | The frozen generator's reduced core is the displayed Sylvester matrix and the theorem is applied to `(u,v)=-b`. Rows were regenerated, not copied | **CONFIRMED** | a termwise mismatch against the displayed `7 x 5`; second-block entries equal to `-h` as polynomials rather than `-h^3`; affine convention `M x = b` rather than `M x + b = 0` |
| 6 | Literal F3 exhaustion: `1594323` assignments, `314127` compatible, stratum totals (8), fibre histogram (9), rank stream `e86fd1ec…b23d`, state stream `98b9395a…1f77`, zero mismatches | **CONFIRMED** | any theorem/direct-rank mismatch; a stratum total off by one; a fibre count off by one; either stream hash different |
| 7 | Omitting the quotient caps on `Delta≠0` accepts exactly `202176` incompatible points, with degree-pattern table (11) and the convention `deg 0 = -1` | **CONFIRMED** | a different false-positive count; a missing or extra `(deg X, deg Y)` row; degree of the zero polynomial recorded as `0` rather than `-1` |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Replay and hashes

Registered commands, rerun unmodified from the case directory:

```sh
cd cases/as_fonly_d7_vertical_state_sufficiency_20260824
./replay_all.sh
```

Exited 0 in 87.73s. Printed `PASS-FORMAL-ADJUGATE-IDENTITY`, the four stratum totals, fibre histogram `{0:12, 3:36, 9:16, 81:1904, 729:219}`, `residue_without_cap_false_positive 202176`, table (11), both stream hashes, `mismatch_count_prefix 0`, `PASS-VERTICAL-STATE-SUFFICIENCY`, manifest OK, and `PASS-AS-D7-VERTICAL-STATE-SUFFICIENCY-ALL`. These runs were regressions only.

Recomputed SHA-256 (all match the launch prompt and `FREEZE.txt`):

| Artifact | SHA-256 |
|---|---|
| `xmodel/as-fonly-d7-vertical-state-sufficiency-20260824.md` | `410235081a54470a377d8d107a1982d34d507040718b945d11ee99dc4d1e5fe4` |
| `cases/as_fonly_d7_vertical_state_sufficiency_20260824/MANIFEST.sha256` | `ba28e9132b30a9cb7a794dc3da1a55c518c1b9c1253817ffde5fdbb90f539e36` |
| `cases/as_fonly_d7_vertical_state_sufficiency_20260824/FREEZE.txt` | `b842a03e35bab622939dc22f69c5eafbcd59e6ea2c4aba227c49df9db99b9aee` |
| `README.md` | `3e932ae902ab2de6baddf77e3b4353791d099a07814070e0abc400dc60a13938` |
| `check_matrix_identity.py` | `147cb423eb02f303974196ba06a7eb0a7bb632af417c7dab75c1410b4bd354ab` |
| `check_vertical_state.py` | `66b42abdf3c1d2174b77d609936e4b3f79e59ea302aeccdc660b157d08ac27de` |
| `replay_all.sh` | `c547669f9d2409635e1e13afec149d6f3ff2c473e27fb2472abe51fa8a3b3d22` |

Consumed corrected-package hashes, unchanged:

| Artifact | SHA-256 |
|---|---|
| corrected report | `9cc39af35e1d52c9673755b79392e62bb265f78dc38bd9110cd37a992115c2d8` |
| `generate_corrected.py` | `a71daa0cb525bac229afb91c76987c8f25c1e2d63683caa10ff45d3364c658e5` |
| `audit_corrected_frobenius_rows.py` | `77485e9d583dd621c8ae412fa70bab3c2aa5b7605bebe03e0b74a3c4dc87689c` |
| erratum review | `c97330558a53ad3caa82d1bf53f642f68139d453edbe96f541a55eece331ad8a` |

---

## Independent recomputation

### 1. Both adjugate products, including signs — CONFIRMED

Write, in the commutative polynomial ring `Z[A,B,H][X,Y]`,

```text
M(X,Y) = (u,v) = (-A X + B Y, -H X - A Y),
Msharp(u,v) = (-A u - B v, H u - A v).
```

Then

```text
-A u - B v = (A^2 + H B) X,
 H u - A v = (A^2 + H B) Y,
```

and, on abstract targets `(U,V)`,

```text
M(Msharp(U,V)) = (A^2 + H B) (U,V).
```

Both identities are coefficient-free over `Z` and therefore hold after every specialization to a field. The registered formal checker asserts only the first product. The second is the identity actually invoked in the sufficiency argument; it holds independently.

Sign-flip attacks, all failing at least one factor:

| Wrong operator | `NX = Delta X` | `NY = Delta Y` |
|---|---|---|
| `Msharp` with `+B` in `(1,2)` | no | yes |
| `Msharp` with `-H` in `(2,1)` | yes | no |
| `M` with `-B` in `(1,2)` | yes | no |
| `M` with `+H` in `(2,1)` | no | yes |

The pair `(M, Msharp)` is the ordinary `2 x 2` adjugate of `[[-A, B], [-H, -A]]`, whose determinant is `A^2 + H B`. That is the source of both products and of every displayed sign.

### 2. `Delta≠0`: divisibility plus quotient caps — CONFIRMED

Necessity. A capped solution satisfies `Msharp(u,v)=Delta(X,Y)` by (7), so both divisions are exact and the quotients *are* the unique capped solution.

Sufficiency. Let `X=NX/Delta` and `Y=NY/Delta` be polynomials of degrees at most `2` and `1`. Then `Msharp(u,v)=Delta(X,Y)`. Left-multiplying by `M` and using `M Msharp=Delta I` gives `Delta·M(X,Y)=Delta·(u,v)`. The hypothesis `Delta≠0` means `Delta` is a non-zero-divisor in the domain `k[z]`, so `M(X,Y)=(u,v)`. Because the quotient degrees are the source caps, this equality holds in the capped spaces, not merely in `k(z)`.

Cancellation in the truncated module `k[z]_{<=3} ⊕ k[z]_{<=2}` is the wrong hypothesis: `z^2` annihilates `z^2` in `k[z]/(z^4)`. The proof does not do that. The no-cap negative control in §7 is the explicit witness that the uncapped polynomial identity is strictly larger than the capped linear map.

Uniqueness on this stratum is the kernel of `M`. If `M(X,Y)=0` then `Delta(X,Y)=0`, hence `X=Y=0`. Rank is therefore `5`.

Degree arithmetic: `deg u<=3`, `deg v<=2`, `deg A<=1`, `deg B<=2` give `deg NX<=4` and `deg NY<=3`. If `deg Delta=2` the quotients automatically satisfy the caps. Independent F3 exhaustion of the regenerated column found that every one of the `202176` cap failures has `deg Delta ∈ {0,1}` (`155520` constant, `46656` linear), matching this bound.

### 3. Both `Delta=0` criteria — CONFIRMED

`H≠0`. Then `H∈k^x` and `B=-H^{-1} A^2`. The identity `NX=-H^{-1} A·NY` makes `NY=0` equivalent to the full vanishing of `Msharp(u,v)` except on the sub-locus `A=0`, where `B=0` as well and `NY=H u`, so `NY=0` is still exactly the image condition `u=0`. Conversely `Y=0`, `X=-H^{-1} v` satisfies the second coordinate of `M` identically and the first coordinate once `H u=A v`. The cap on `X` is free because `deg v<=2`. Kernel: `X=-H^{-1} A Y` with `Y` free of degree `<=1` is two-dimensional (the `Y`-component is injective, and `deg(A Y)<=2`), so rank is `3`.

Independently reconstructed rank-3 witness on the regenerated column:

```text
(P,Q,R,T,s,w,h)=(1,0,1,0,2,0,1),  (fua,...,fvb)=(0,0,0,0,1,0),
A=1, B=2, H=1, Delta=0,
(u,v)=(z,z),  NY=NX=0,
X=-H^{-1} v=2z, Y=0,
M(X,0)=(z,z),  rank(M)=rank[M|-b]=3.
```

`H=0`. Then `Delta=A^2=0` in `k[z]`. A field is an integral domain, so `A=0`. The map is `(X,Y)↦(B Y, 0)`. If `B≠0` then `k[z]` has no zero-divisors, so `B Y=0` forces `Y=0` on `deg Y<=1`; the image is exactly `{ (B Y, 0) : deg Y<=1 }` and the rank is `2`. If `B=0` the map is zero and the criterion is `u=v=0`.

The four cases are disjoint (`Delta` zero or not; then `H` zero or not; then `B` zero or not) and cover every specialization.

### 4. Ranks `5,3,2,0`; absence of one and four — CONFIRMED

The kernel-dimension argument of §3 is characteristic-free and uses only that `k[z]` is a domain and that `H∈k`. It does not pass through Fitting ideals or radicals.

Independent rank census of the displayed `7 x 5` on all `2187` F3 bases:

```text
rank 0: 17 bases, rank 2: 64, rank 3: 66, rank 5: 2040.
```

These are exactly the counts of structural bases with `(H=B=A=0)`, `(H=A=0, B≠0)`, `(Delta=0, H≠0)`, and `(Delta≠0)`. Every one of the `2187` bases obeys the four-stratum rank prediction. No rank `1` or `4` occurs.

The same rank set `{0,2,3,5}` is the only set seen in `40000` random specializations over each of `F_5`, `F_7`, and `F_11`. Regenerated `core_matrix` ranks agree with the displayed Sylvester form on all `2187` F3 bases.

The F3 affine census rank pairs of the regenerated column are

```text
(0,0) 873, (0,1) 11520, (2,2) 1404, (2,3) 45252,
(3,3) 6642, (3,4) 41472, (5,5) 305208, (5,6) 1181952,
```

which match both the corrected producer's display (13) and the four compatible-stratum totals. Compatible rank `5,3,2,0` counts are exactly the compatible counts of the four state strata.

This is a statement about the specialized capped map, not a scheme-theoretic radical-of-minors classification of a family over an algebraic closure. No embedded component of a base scheme can change the rank of `M` at a field point: that rank is constant on each of the four polynomial strata.

### 5. Regenerated matrix and column, not copied rows — CONFIRMED

Loading the frozen generator with `BRANCH=vertical` and no census flags emits remaining variables `(d7_1, d7_4, d7_7, d6_1, d6_4)` and remaining source labels `(M_0_9, M_3_6, M_6_3, M_9_0, M_0_8, M_3_5, M_6_2)`. The reduced core, after the generator's triangular substitution, is termwise

```text
[ 2 Pp,   0,    0,   Rr s,           0         ]
[ 2 Qq,  2 Pp,  0,   Rr w + Tt s,    Rr s      ]
[ 0,     2 Qq, 2 Pp, Tt w,           Rr w+Tt s ]
[ 0,      0,   2 Qq, 0,              Tt w      ]
[ 2 hhh,  0,    0,   2 Pp,           0         ]
[ 0,     2 hhh, 0,   2 Qq,           2 Pp      ]
[ 0,      0,   2 hhh,0,              2 Qq      ]
```

in `F_3`. This is the displayed Sylvester matrix of `(-A X+B Y, -h^3 X-A Y)` with `X=x0+x1 z+x2 z^2` and `Y=y0+y1 z`. The second-block diagonal is the polynomial `-h^3`, not the polynomial `-h`: as expressions, `h` and `h^3` are unequal even in characteristic three.

The affine convention in the generator is `M x + b = 0`. The state theorem must be applied to `(u,v)=-b`. That is what the producer does.

The six-variable affine column is the generator's `core_rhs`. Its interpretation as the exact AS successor is the content of the still-active corrected-package review and is **not** confirmed here. The F3 comparison below is a comparison against that regenerated column, as a displayed input.

Attack: over `F_5`, on the `1978` sampled points of a `5000`-point draw at which `h^3≠h` as field elements, the criterion written with `H=h` disagrees with the displayed `h^3`-matrix at `142` targets, while the criterion written with `H=h^3` agrees in every sample. The cube is load-bearing over a general field. On literal F3 points `a^3=a`, so the census cannot see this distinction; the regenerated *polynomial* matrix still carries `h^3`.

### 6. Exhaustive literal-F3 agreement — CONFIRMED

An independently coded enumerator (own `F_3` Gaussian elimination, own polynomial arithmetic, own stratum classifier; matrix and column taken from the frozen generator, not from copied markdown rows; `check_vertical_state.py` not imported) returned

```text
total                              1594323
compatible                          314127
Delta!=0                    1487160 / 305208
Delta=0, H!=0                 48114 /   6642
Delta=0, H=0, B!=0            46656 /   1404
Delta=0, H=0, B=0             12393 /    873
fibre histogram     {0:12, 3:36, 9:16, 81:1904, 729:219}
mismatches                             0
rank stream   e86fd1ec2724b5089039378c07e1a19a089042eeb4172b0342474f85d4d8b23d
state stream  98b9395a186f04acd1db001fe5457fa5dca8c5bd8d5c2c3d6e52df79f8981f77
```

These are exactly (8), (9), and (10). The fibre arithmetic `36·3+16·9+1904·81+219·729=314127` closes. Structural base counts `2040+66+64+17=2187` close. Rank-pair totals reproduce the corrected producer's display (13).

Random-target checks of the *displayed* matrix, `8000` samples each, against independently solved `7 x 5` systems, gave zero mismatches over `F_3, F_5, F_7, F_11, F_13, F_17, F_31, F_101`. The algebraic criterion is not an F3-only cancellation accident.

Reconstructed capped solutions, each matching both the polynomial map and the numeric `7 x 5`:

| Stratum | Base `(P,Q,R,T,s,w,h)` | Frobenius | Rank | Witness |
|---|---|---|---|---|
| `Delta≠0` compatible | `(0,0,0,1,0,1,1)` | `0` | `5=5` | `Delta=z^2`, `X=z^2`, `Y=z` |
| `Delta=0,H≠0` | `(1,0,1,0,2,0,1)` | `(0,0,0,0,1,0)` | `3=3` | `X=2z`, `Y=0` |
| `Delta=H=0,B≠0` | `(0,0,0,1,0,1,0)` | `0` | `2=2` | `B=z^2`, `Y=z`, `v=0` |
| `B=0` | `(0,0,0,0,0,0,0)` | `0` | `0=0` | `u=v=0` |

Incompatible points exist in every stratum (ranks `(5,6)`, `(3,4)`, `(2,3)`, `(0,1)`), so the criteria are not vacuously true.

### 7. No-cap negative control — CONFIRMED

Independent census: `residue_only and not exact` occurs at exactly `202176` points, all on `Delta≠0`. Degree patterns, with `deg 0 = -1`:

```text
(deg X, deg Y)   count
(-1, 2)           1968
( 0, 2)           2208
( 1, 2)           9648
( 2, 2)          28944
( 3,-1)           4320
( 3, 0)           3456
( 3, 1)          15552
( 3, 2)          54432
( 3, 3)          23328
( 4, 2)          34992
( 4, 3)          23328
```

The eleven rows sum to `202176`. This is table (11).

Explicit no-cap false positive on the regenerated column:

```text
(P,Q,R,T,s,w,h)=(0,0,0,1,1,0,1),  (fua,...,fvb)=(0,0,0,0,2,0),
Delta=z (degree 1),  X of degree 2,  Y of degree 2,
rank(M)=5, rank[M|-b]=6  (incompatible for the 7 x 5),
M(X,Y)=(u,v) as unbounded polynomials.
```

The adjugate division classes alone are not the bounded state. The two endpoint caps are load-bearing. The same phenomenon appears in the multi-prime random-target samples (false positives in every field tested), so it is not a characteristic-three artefact.

On the small `Delta=H=0, B≠0` stratum, exact division `u=B Y` with `deg Y>1` occurs at `120` further incompatible points. The stated criterion already includes `deg Y<=1` there. Those `120` points are not part of the registered `202176`, which is the `Delta≠0` control named in the producer.

---

## Non-blocking remarks

1. The registered formal checker asserts `Msharp M=Delta I` and not `M Msharp=Delta I`. Both hold over `Z`. Sufficiency uses the second product. Not a hole in (7).

2. The registered F3 enumerator asserts total, compatible count, fibre histogram, rank-stream hash, and zero mismatches. It *prints* but does not `assert` the state-stream hash, the four stratum totals, the `202176` count, or table (11). Those printed values match the report and the independent reconstruction. A successor package should pin them.

3. On literal F3 points, `h^3=h` as functions, so the F3 census is blind to `H=h` versus `H=h^3`. The regenerated polynomial matrix and the algebraic theorem use `h^3`. Over `F_5` the distinction is visible and the cube is required. The producer already states that Section 2 is a field-theoretic claim about the displayed matrix and that Sections 3–4 classify literal F3 points only.

4. The triangular coordinate change in the generator is written with `F_3` coefficients (`escale(2,·)` for a minus sign). The algebraic theorem is about the *displayed* matrix over an arbitrary field, not about a characteristic-zero lift of that coordinate change from `(p,q,r,s,t,w)`.

5. `A^2=0 ⇒ A=0` uses that `k[z]` is a domain. The producer states that `k` is a field. The implication fails on non-reduced coefficient rings; those are outside the claim.

6. The currently active review of `xmodel/as-fonly-d7-postd10-d98-f3-corrected-20260824.md` has not completed. Nothing here upgrades the regenerated column from “displayed frozen input” to “different-model-confirmed AS successor.”

None of these remarks breaks a numbered claim.

---

## Radicalization, truncation, finite-field-only cancellation, endpoint degrees, all-depth

- **Radicalization.** The rank statement is rank-nullity for a specialized linear map of finite-dimensional vector spaces. No Fitting ideal, no radical, and no minAss prime is used. Replacing the four polynomial strata by their radicals would not change the field-valued ranks, and is not how the proof proceeds.
- **Lost embedded structure.** The `7 x 5` is the coefficient matrix of a two-polynomial map in one auxiliary variable, with source labels the vertical bidegree steps of total degrees nine and eight. That embedding is used only to identify the displayed matrix. The F3 census is pointwise. No scheme-theoretic multiplicity of a base locus is claimed, and none is needed for the specialized rank.
- **Truncation.** Cancellation is in `k[z]`. The no-cap control is exactly the set of points at which an unbounded polynomial solution exists and the capped `7 x 5` is incompatible.
- **Finite-field-only cancellation.** Both adjugate products hold over `Z`. Random-target agreement holds on eight primes. `A^2=0` with `A≠0` does not occur for `deg A<=1` over `F_3, F_5, F_7`.
- **Endpoint degree conventions.** The zero polynomial has degree `-1` in table (11), matching `len(trim(a))-1` on the empty coefficient list. The inequality `deg X<=2` includes that case. Re-binning the zero polynomial as degree `0` would destroy the `(-1,2)` and `(3,-1)` rows and the total `202176`.
- **All-depth / lift.** The producer refuses a next carry, an algebraic-closure classification, a lift or no-lift, characteristic zero, a counterexample, and JC2. Nothing in the algebra enlarges that refusal.

---

CONFIRMED
