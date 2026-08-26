# Hostile text-only review — control-2 beta=5 dual equality-face certificate

| Field | Value |
|---|---|
| Claim under review | Dual AWS contractions of the expanded nine-generator control-2 source at the sampled beta=5 weight `(4,1,1,20,20,30,30,30)` produce the same 41-generator special fibre, containing `la^20`, with empty eight-coordinate torus |
| Overall verdict | **BETA5_DUAL_CONFIRMED** for this exact frozen cubic, fixed loads, five-coefficient support, and this sampled integral weight. It is a dual contraction/order certificate of one equality-face special fibre, not a new derivation of the eight rows, not a whole-cone statement, and not a replacement of the already-reviewed strict `beta>5` witness region |
| Smallest failing identity | none in the frozen dual package, either AWS stream, the expanded-source provenance, or the hand face-weight arithmetic |
| Smallest missing hypothesis for a stronger theorem | every positive split `(T,H)` with `L=3T+H`; neighbouring equality faces; later `q2`; moving axis/loads; another support; a Gröbner cone or Newton fan; the whole double-root locus; D1; JC2 |
| Evidence tier | SHA-256 of the dual freeze and every nested path; `cmp`/`diff`/sed identity of the nine expanded bodies and of the 41 special-fibre generators; inspection of compiler, worker, both compiled sources, both AWS streams, the pinned base compiler, the charged ordinary-tail source, and the frozen reviewed expanded B. No local Singular, Sage, msolve, gfan, Lean, or Python algebra |
| Reviewer / model | Grok 4.6 (xAI). Text-only tropical / commutative-algebra / CAS-custody referee. Independent of the producer status line and of the slope-uniform reviews except as independently re-audited source |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Host | Darwin. Singular, Sage, msolve, gfan, Lean, and every solver were not run |

## What was and was not run

No local substantive computation was run. In particular this review did **not** execute Singular, Sage, msolve, gfan, Lean, or Python algebra. Hashes were recomputed with SHA-256 over file bytes. Polynomial bodies and special-fibre generators were compared as text. Git identity was read with `git rev-parse`. AWS streams were read as already-emitted text. Hand arithmetic is recorded under charges 4–5.

The producer status line (“HOSTILE SOURCE REVIEW PENDING”) was ignored as a verdict. The slope-uniform obstruction note and its grok review were read as scope explanation and independently re-checked on the face-weight arithmetic; their `beta>5` theorem is not inherited as a premise of this dual certificate.

Charged dual freeze and provisional report, recomputed and matched:

```text
c8c541b2a098b396b32bd3e905189ca54f2dd11c44ecc7b74c0cf98ed5570a34
  cases/max12_912_order3_d1_double_root_control2_beta5_face_v1_20260826/DUAL_FREEZE.sha256
c42f8d470de0692f7f7eead4887702a91e70c0505453cea6843469303b837503
  cases/max12_912_order3_d1_double_root_control2_beta5_face_v1_20260826/DUAL_RESULT_PROVISIONAL.md
```

Every path listed in `DUAL_FREEZE.sha256` recomputed and matched (24/24). Nested `SOURCE_CLOSURE.sha256`, both `result.sha256`, both `compiled.sha256`, and both `solve_source.sha256` likewise recomputed and matched. Empty compiler/CAS stderr and stdout diagnostics are the empty-string digest `e3b0c442…`. All four rc files are the two-byte string `"0\n"`, digest `9a271f2a…`.

Read in full before the verdict: every file at the dual-package root; every artifact under `aws_box02_A/` and `aws_r6d_B/` (except AppleDouble `._*` harvest sidecars, which are not in the freeze); the pinned base compiler `compile_control2_rees.py`; the charged ordinary-tail source `independent_reconstruct.py`; the control-2 Rees preregistration; the frozen reviewed expanded B at SHA `c905f1b5…`; the slope-uniform obstruction note and its grok review.

---

## Promotion

**Accept `FOR THE FROZEN DOUBLE-ROOT CUBIC K=(z-1)^2(z+2) WITH a=1, h=q2=k=nu=0, mu=2/3 AND SUPPORT Q=q1 z+q0, R=r2 z^2+r1 z+r0, LET J BE THE EXACT UNHOMOGENIZED NINE-GENERATOR IDEAL WHOSE EXPANDED BODIES E1,...,E8,LT MATCH THE REVIEWED CONTROL-2 ENCODING B BYTE-FOR-BYTE AFTER STRIPPING REES s-POWERS. AT THE SINGLE INTEGRAL WEIGHT w(la,tau,rho,q1,q0,r2,r1,r0)=(4,1,1,20,20,30,30,30), THE SAMPLED RAMIFICATION OF THE SIMULTANEOUS EQUALITY FACE alpha=15/2, beta=5 WITH SPLIT (L,T,H)=(4,1,1), TWO INDEPENDENT EXPANDED CONTRACTIONS — DIRECT sat(I,<s>) IN GLOBAL dp, AND DOUBLE-INVERSE ELIMINATION IN (lp(3),dp(8)) — COMPUTE THE SAME 41-GENERATOR SPECIAL FIBRE UP TO THE POSITION OF s. THAT IDEAL CONTAINS la^20 AS A REDUCED STANDARD-BASIS GENERATOR, CONTAINS THE SEVEN-TERM WITNESS FACE WFACE, KILLS THE FORMERLY DISPLAYED RESIDUE, AND AFTER EIGHT-COORDINATE TORUS SATURATION IS THE UNIT IDEAL. THEREFORE THIS EXACT FIXED-WEIGHT, FIXED-SUPPORT TORUS SPECIAL FIBRE IS EMPTY: NO k[[t]]-POINT OF V(J) REALIZES THESE EXACT VALUATIONS WITH ALL EIGHT LEADING COEFFICIENTS NONZERO. THIS CLOSES THE SAMPLED beta=5 FACE AT THIS WEIGHT. IT DOES NOT CERTIFY EVERY POSITIVE SPLIT (T,H), DOES NOT REPLACE THE ALREADY-REVIEWED STRICT beta>5 WITNESS REGION, AND IS NOT A MOVING-AXIS, LATER-q2, OTHER-SUPPORT/LOAD, WHOLE-CONE, WHOLE-FAN, WHOLE-DOUBLE-ROOT, D1, OR JC2 THEOREM.`**

Do not promote this to: a new derivation of the eight charged rows; Gröbner-basis continuity; emptiness of coordinate hyperplanes; every positive split `L=3T+H`; neighbouring equality faces; the already-reviewed open interval `5<beta<6`; `beta=6` or `beta>6` as control-2 geometry; moving axis or loads; nonzero `q2`; another support; a full Newton fan; D1; or JC2.

Smallest repair / counterexample: none for the licensed theorem.

---

## Charge 1 — freeze hashes, AWS custody, compile/solve separation

**CONFIRMED.**

`DUAL_FREEZE.sha256` and `DUAL_RESULT_PROVISIONAL.md` match the required digests. All 24 freeze entries match the files they name. Nested closures:

```text
9d586158dfcb587db02e6c18d442c9299fb66d680ff24eb5d79e421f25965623  SOURCE_CLOSURE.sha256
015d66b8d9b569855cfe761445b2327a13d58cfe686b0cf5f0c19c0d7f97a7d4  compile_control2_rees.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  independent_reconstruct.py
8c0909e9e57c3c0f170e1c1eb5f7426cbae3ba7fd1e256ad59980444b36f5aea  compile_beta5_face.py
b7b1da1cc515413975369f6bedc2337f0df6715d68571650e40df22a8099b06a  remote_worker.sh
b4832a2b50b3469cedb91b02f32a4a5edce0f622780726ec7918dec8578f141d  PREREGISTRATION.md
c591eff8daeb96991fe146e11f93b123b4dcc687dbc75470ed11631b810cfaf8  AWS_REGISTRATION.md
```

Both compiler stdout files reprint those two source pins and `PASS_CONTROL2_BETA5_FACE_COMPILER` once. Both `source.check` / `source.prelaunch.check` streams are six `OK` lines against `SOURCE_CLOSURE.sha256`. Both `solve_source.check` streams are one `OK` line against the encoding-specific compiled input.

| | A | B |
|---|---|---|
| host/tag | Box02 `34.203.207.55`, `…20260826T025500Z_box02_A` | r6d `100.26.198.153`, `…20260826T025500Z_r6d_B` |
| hostname / uname | `ip-172-30-0-186`, Linux `7.0.0-1010-aws` | `ip-172-30-0-45`, Linux `6.17.0-1019-aws` |
| worker PID | `268278` | `212593` |
| encoding | A | B |
| solver cap / timeout | `268435456` KiB (256 GiB), 21600 s | `201326592` KiB (192 GiB), 21600 s |
| compiler cap / timeout | `2097152` KiB, 300 s | same |
| nproc | 128 | 64 |
| host RAM / swap | 2.0 Ti, swap `0B` | 495 Gi, swap `0B` |
| worker start | `2026-08-26T02:54:44Z` | `2026-08-26T02:54:45Z` |
| solve start / finish | `02:55:27Z` / `03:00:05Z` | `02:55:33Z` / `02:55:36Z` |
| compiled input SHA | `cb767f1fe4162a1d992cac145cd744c6d720751b4737e5434f79402bb218ef8a` | `023dc47323a3511a2457048166e50dadc05333b1ae9a9280003d1cb30f43d6eb` |
| stdout SHA | `cc5a80afce386ff9915d932c2d08ff66e9f3e1661d3ed00c87dc6d1a82952038` | `069a3428c77231a7bb079b7e161055f76a061784c218fc19663e3d199d0abf63` |
| elapsed / max RSS / swaps | `4:37.93`, `516588` KiB, `0` | `2.80 s`, `25676` KiB, `0` |
| Singular | 4.3.2 (4330), `/usr/bin/Singular -q` | same binary series |
| compiler rc / solver rc | `0` / `0` | `0` / `0` |
| compiler stderr, CAS stderr, stdout diagnostics | empty | empty |

Compile and solve are distinct gates: `WAITING_COMPILE` until `GO_COMPILE`, source-hash check, compile under a 2 GiB/`300 s` ulimit, `COMPILE_DONE`, then `WAITING_SOLVE` until `GO_SOLVE`, compiled-input hash check, one `nice -n 10` Singular process, `SOLVE_DONE`. The worker refuses non-Linux, non-EC2, and unregistered tags; the compiler repeats those checks and additionally refuses a mutated base-compiler hash, a mutated charged-source pin, and a mutated weight tuple. Existing registered jobs were not stopped: both hosts already had ~166–169 GiB in use.

Worker accept conditions fired exactly once on each host: `PASS_WITNESS_FACE_MEMBERSHIP`, `TORUS_FACE_IS_UNIT=0|1`, and the encoding-specific final `PASS_CONTROL2_BETA5_FACE_{A,B}`. No `FAIL_` line. Nested `result.sha256` entries match the files they name, including the empty diagnostics files.

The two compiled inputs differ only by baked-in `AWS_TAG` (seven versus five characters in the suffix `box02_A` / `r6d_B`, a two-byte size gap). Polynomial bodies of `E1,…,E8,LT` are identical across all four compiled sources (A’s A, A’s unused B, B’s unused A, B’s B). Each host solved only its registered encoding.

Harvest nit, not a defect: AppleDouble `._*` sidecars sit in both AWS directories and are absent from the freeze.

---

## Charge 2 — compiler provenance, encodings, E8 compact error

**CONFIRMED. Both encodings consume the same expanded nine generators. This package does not call the historical factored-A renderer.**

The beta=5 compiler hash-pins the reviewed control-2 base compiler and that compiler’s charged ordinary-tail pin, then mutates only the in-memory weight tuple to

```text
WEIGHTS = (4, 1, 1, 20, 20, 30, 30, 30).
```

It loads `independent_reconstruct.py` through the base compiler, builds the eight ordinary tails, substitutes the unweighted coefficient images of `a0,…,a7,k` for `K=z^3-3z+2`, `q2=k=0`, subtracts the charged targets, and emits both encodings from `expanded_poly_string(..., rees=True)`. `compact_row_string` and `COEFFICIENT_REES_STRINGS` are never called. The historical E8 compact error is exactly that unused renderer: factored A differed from expanded B by the nonzero constant `-25134148616192/43046721`. This package cannot consume it.

Targets and Rees relation, from the pinned base compiler and visible in both compiled sources:

- row 3: `(2/3) la^{15}` appears as `(-2/3)*s^60*la^15`;
- row 8: `la^{20} + la^{20} tau` appears as `-1*s^81*la^20*tau-1*s^80*la^20`;
- other rows: no `la`/`tau`/`rho`;
- `LT = s^4 la - s^4 tau^3 rho`.

Support mask and loads are those of the charged control-2 Rees preregistration: `a=1`, `h=q2=k=nu=0`, `mu=2/3`, `Q=q1 z+q0`, `R=r2 z^2+r1 z+r0`. The compiler-side residue evaluation of submitted initials is **not** used as a refuse gate here (correct: that residue was for `beta=11/2`, not this face). The compiler only refuses an empty initial. Both hosts report the same eight initial SHA-256 values, with minimum weights `50` on rows 1–5,7,8 and `60` on row 6.

Encoding A, as compiled and solved:

```text
ring R=0,(s,la,tau,rho,q1,q0,r2,r1,r0),dp;
ideal I=E1,E2,E3,E4,E5,E6,E7,E8,LT;
ideal C=sat(I,CS);          // CS=<s>
ideal H=C,s;  ideal GH=std(H);
ideal GHT=std(sat(GH,CT));  // CT=<la*tau*rho*q1*q0*r2*r1*r0>
```

Encoding B, as compiled and solved:

```text
ring R=0,(u,v,s,la,tau,rho,q1,q0,r2,r1,r0),(lp(3),dp(8));
ideal I=E1,E2,E3,E4,E5,E6,E7,E8,LT,u*s-1;
ideal C=eliminate(std(I),u);
ideal H=C,s;  ideal GH=std(H);
ideal GHT=std(eliminate(std(GH, v*TORUS-1), v));
```

Both use `option(redSB)`. A is expanded direct saturation with global `dp`. B is expanded double-inverse elimination with `lp,dp`. The nine finite generators are the same strings.

s-stripped bodies of `E1,…,E8,LT` are byte-identical to frozen reviewed expanded B

```text
c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b  base_B.sing
```

Every s-power in the beta=5 sources equals the face weighted degree; every s-power in frozen B equals the discovery-weight degree `(4,1,1,22,22,30,30,30)`. The only differences are `2` per q-factor, as required by `22→20`. Terms without q (pure `la`, `r`, `tau`, `rho`) keep the same s-powers, including `s^80 la^20`, `s^81 la^20 tau`, and `s^4` on both sides of `LT`. This is the same finite ideal `J`, re-homogenized at the face weight. It is not a second derivation of the eight D1 rows.

In the nine expanded generators, `tau` occurs only as the higher row-8 target `la^20 tau` and in `LT` as `tau^3 rho`; `rho` occurs only in `LT`.

Nit, not a defect: encoding A assigns `sat` directly to an `ideal`, rather than unwrapping a Singular list. The campaign already recorded that coercion as semantically complete. Empty diagnostics and the matching 41-generator special fibre with encoding B corroborate it here.

---

## Charge 3 — contraction versus special fibre; 41-polynomial comparison

**CONFIRMED. Different contraction counts are allowed. The displayed special-fibre bases are literally the same 41 polynomials up to the position of `s`.**

`C` is a generating set of the contraction of the Rees ideal from `s≠0`:

- A: `I : s^∞` via `sat(I,<s>)` in global `dp`, 420 generators;
- B: elimination of `u` from `⟨E1,…,E8,LT, u s-1⟩` in `(lp(3),dp(8))`, 319 generators.

These are independent presentations of the same algebraic operation, computed by different algorithms in different ambient rings. Generator counts of `C` are not invariants. The special fibre is `H=C+(s)` after a reduced standard basis. That is the object compared.

Both streams report `SPECIAL_FIBRE_GENERATORS=41` and print `GH[1]` through `GH[41]` with no gap. Writing `s` for the Rees parameter:

- A has `GH[1]=s` and `GH[41]=la^20`;
- B has `GH[40]=la^20` and `GH[41]=s`.

Deleting `s` from each printed list leaves the same 40 polynomials in the same order. Equivalently, `A.GH[i+1] = B.GH[i]` for `i=1,…,40`, and `A.GH[1] = B.GH[41] = s`. The two 41-element multisets are equal. The claim in `DUAL_RESULT_PROVISIONAL.md` is therefore literal, not merely “same ideal up to reduction”.

The 40 non-`s` polynomials begin

```text
2*q0*r1+2*q1*r0+3*q0*r0
q0*r2+q1*r1
2*q1*r2-q0*r0
q1*r1*r0
…
tau^3*rho-la
r0^5
…
la^20
```

and contain `tau`/`rho` only in the homogeneous relation `tau^3*rho-la`. Position of `s` is the only order artifact (global `dp` with `s` first versus an `lp` block still containing `s`).

---

## Charge 4 — `la^20` in the full specialized initial ideal; residue versus torus

**CONFIRMED. `la^20` is a reduced generator of both special fibres. It is not a submitted-row initial and not a dehomogenization leftover.**

Both reduced bases contain the monomial `la^20` as a generator (`A.GH[41]`, `B.GH[40]`). `option(redSB)` is on, so this is a reduced standard-basis element of `std(C+(s))`, i.e. of the specialized initial ideal `in_w(J)` at the compiled weight, together with the fibre equation `s=0`.

It is not the initial of submitted `E8`. Compiler stdout on both hosts has `row_8_minimum_weight=50`. In the expanded `E8`, that weight-50 piece is the `q r` terms; `la^20` sits at weight `80` and `la^20 tau` at `81`. The same phenomenon as the reviewed discovery-weight certificate: `la^20` is an S-polynomial / full-initial consequence, not `in_w(E8)`.

It is not a dehomogenized artifact. The printed generator is the monomial `la^20` with no leftover `s`-power. The membership check

```text
poly WFACE=la^20+1/243*q1*q0^3+1/54*q1*r2*r1+7/108*q1*r1^2
           +1/54*q1*r2*r0-1/54*q0*r1*r0+1/108*q1*r0^2;
reduce(WFACE,GH)==0
```

is against `GH=std(C+(s))`, and both streams print `PASS_WITNESS_FACE_MEMBERSHIP` once. `WFACE` is the seven-term face of the already-reviewed witness `W` (namely `W` minus the strictly higher `la^20 tau`). Membership of `WFACE` in `GH` is weaker than a reduced generator `la^20`; both are present.

`DISPLAYED_RESIDUE_SURVIVES=0` means: adjoining the formerly displayed leading residue

```text
(la,tau,rho,q1,q0,r2,r1,r0)=(1,1,1,1,-1,1,1,-2)
```

to `GH` produces the unit ideal. Because `la^20 ∈ GH`, already `la-1` forces `1`. The flag is therefore a correct but non-independent corollary of `la^20`. It is **not** a statement that some other torus point survives.

`GHT[1]=1` with `TORUS_FACE_IS_UNIT=1` is the independent torus check the preregistration asked for. Encoding A saturates `GH` by the product of all eight finite coordinates; encoding B inverts that product by `v·TORUS-1` and eliminates `v`. Both print a one-element basis `GHT[1]=1`. Over `Q`, `la^20 ∈ GH` already forces this for any saturation that inverts `la`. The dual constructions still independently compute the localization, and both get `(1)`. Coordinate hyperplanes of `V(GH)` are not classified.

Valued-arc reading, scoped to this ring and weight: a `k[[t]]`-point of `V(J)` with exact valuations `w` and nonzero leading coefficients would be a point of `V(in_w(J)) ∩ (k*)^8`. That intersection is empty.

---

## Charge 5 — beta=5 face of `W`; sampled split versus all positive splits

**CONFIRMED for the seven-term face of `W`, uniformly in `T>0`. The computed 41-generator initial ideal is licensed only at the sampled split `(L,T,H)=(4,1,1)` and its positive ray.**

The already-reviewed element of `J` is

```text
W = la^20*tau + la^20
  + (1/243)*q1*q0^3
  + (1/54)*q1*r2*r1 + (7/108)*q1*r1^2 + (1/54)*q1*r2*r0
  - (1/54)*q0*r1*r0 + (1/108)*q1*r0^2.
```

All eight coefficients are nonzero in `Q`. Under `w(la,tau,rho)=(L,T,H)`, `w(q1)=w(q0)=beta L`, `w(r_i)=(15/2) L`, and `L=3T+H`:

| term | weight |
|---|---|
| `la^20*tau` | `20L+T` |
| `la^20` | `20L` |
| `q1*q0^3` | `4 beta L` |
| each of the five `q r r` terms | `(beta+15) L` |

At `beta=5` the last three classes equal `20L`. For `T>0`, `la^20 tau` is strictly higher. The least-weight face of `W` is exactly the seven-term `WFACE` compiled into both sources. No displayed term of `W` contains `rho`, so `H` does not enter the face. Positive rescaling of `(L,T,H)` does not change the least-weight monomials. This arithmetic is independent of the AWS special fibre.

The AWS computation is not that arithmetic. It computes `in_w(J)` at the single integral vector `(4,1,1,20,20,30,30,30)`. Positive multiples of this vector stay on the same ray: `beta=20/4=5`, `alpha=30/4=15/2`, `L=3T+H`. Other interior splits such as `(L,T,H)=(5,1,2)` are different rays. A Gröbner cone certificate for those rays is not in the package.

Structural support for expecting the same special fibre for every `T>0` is real and is not a certificate: in the nine expanded generators the only explicit `tau` is the strictly higher row-8 target, `rho` occurs only in the already-homogeneous relation, and the computed `GH` itself contains `tau`/`rho` only in `tau^3*rho-la`. Syzygies that used the higher `tau` term before `s=0` could in principle depend on `T`. This run does not bound that. The dual report does not claim it. The licensed emptiness statement is the sampled weight.

Submitted-row initials among `(la,q,r)` terms likewise depend only on `L` (and the charged `alpha,beta`), not on `(T:H)`, because those rows contain no `tau`/`rho` except the higher `E8` target. That is a statement about submitted generators, not about `in_w(J)`.

---

## Charge 6 — strongest exact theorem and firewall

**CONFIRMED. The dual report’s scope matches the licensed theorem. It is not the `beta>5` theorem.**

Distinguish three statements:

1. **Already reviewed, not this package.** For every rational `L>0`, `T>0`, `H>0` with `L=3T+H` and every rational `beta>5`, the unique least-weight term of `W` is `la^20`, hence `la^20 ∈ in_w(J)` and the eight-coordinate torus is empty. That is finite-support arithmetic on a frozen membership identity. It includes the strict control-2 interval `alpha=15/2`, `5<beta<6`, and does **not** need this dual run.

2. **This dual certificate.** At the single weight `(4,1,1,20,20,30,30,30)`, the full special fibre of the expanded nine-generator Rees ideal has a 41-element reduced basis containing `la^20`, and the eight-coordinate torus localization is `(1)`, in two independent contractions. The seven-term equality face of `W` is a member of that fibre, but torus emptiness uses the full fibre, not `WFACE` alone: `WFACE` can vanish with `la≠0`.

3. **Not licensed.** Other weights on the hyperplane `beta=5`; other splits `(T,H)`; `beta=6` as a control-2 endpoint; `beta>6` as control-2 geometry; moving `a,h`; nonzero or later `q2`; moving `k,mu,nu`; another support mask; the tied chart `alpha=2 beta`; control-1; a Gröbner cone; the double-root Newton fan; D1; JC2.

The dual report’s firewall string, printed by both solvers, is

```text
FIREWALL=EXACT_BETA5_EQUALITY_FACE_FIXED_SOURCE_LOAD_SUPPORT_ONLY
```

Its prose closes “the beta=5 endpoint for this finite source package” at the fixed weight in its scope block, and explicitly refuses omitted tails, moving loads, neighbouring equality faces, and the entire double-root fan. That is the correct promotion discipline.

The equality face is the Newton collision `3 beta = 2 alpha = 15`. Closing it at one sampled ramification does not consume the strict `beta>5` region and does not enlarge that region.

---

## Nits, not defects

1. Producer status still says hostile review pending. Timestamp.
2. `DISPLAYED_RESIDUE_SURVIVES=0` is implied by `la^20 ∈ GH`. Independently informative content is `GHT[1]=1`, which is also implied over `Q` once `la` is inverted, but is the preregistered dual localization.
3. Encoding A omits the synthetic toy saturation controls of the original Rees A. Not required by this preregistration; encoding B’s inverse-elimination path is the second construction.
4. In-memory mutation of `base.WEIGHTS` is the intended reweighting; the on-disk base compiler hash is checked before that assignment.
5. AppleDouble `._*` files in the harvested AWS directories. Not frozen.
6. Evidence uses `la`; some notes use `Lambda`. Same coordinate.

No source, certificate, or theorem repair is required. No AWS replay is required: both encodings already completed on registered hosts with empty diagnostics, matching special fibres, and matching nested hashes.

BETA5_DUAL_CONFIRMED
