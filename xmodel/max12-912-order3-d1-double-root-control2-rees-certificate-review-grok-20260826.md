# Hostile text-only review — control-2 Rees monomial certificate

| Field | Value |
|---|---|
| Claim under review | Source-identical follow-up that prints the special-fibre basis of frozen encoding B and certifies a monomial in the full minimum-weight initial ideal |
| Overall verdict | **REES_CERT_CONFIRMED**. Encoding-B special fibre contains `la^20` after exact `s!=0` contraction and `s=0`. That monomial is in `in_w(I)`, not an initial form of a submitted generator. Dual encoding A is not a result |
| Smallest failing identity | none in the frozen certificate sources or in the r6d certificate stream |
| Smallest missing hypothesis for a dual theorem | encoding A torus basis, and a cross-encoding comparison of the two emitted `Htor` bases, as already firewalled by v2 |
| Evidence tier | byte comparison of `base_B.sing` against the frozen v2 r6d B input; hand reading of the nine Rees-transformed generators, the contraction/`s=0` order, the certificate insertion, and the emitted 35-element basis; SHA-256 of frozen text and already-emitted AWS files. No local Python, Singular, Sage, msolve, Lean, Gfan, or other substantive symbolic computation |
| Reviewer / model | Grok 4.6 (xAI). Text-only tropical / commutative-algebra referee |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `4fe628a133ae62e16b1bec5e4ed6fcee420dd880` (this package uncommitted) |
| Host | Darwin. Certificate compiler, v2 compiler, charged reconstruct, and Singular were not run |

No local substantive computation was run. Hashes were checked with `shasum -a 256`. File identity was checked with `cmp`. Git identity was read with `git rev-parse` / `git status --porcelain`. AWS streams were read as already-emitted text.

Frozen hashes charged in the prompt, recomputed and matched:

```text
48c7a6f9144b6b83fb57b2c80decb48208a7d3ff8fe880c77abb10631a09ef5d  FREEZE.sha256
abb769de9d9cf7fd1af43f96d32fcc148f79ba51844b1995e539baab7b84ebee  RESULT.md
d5317aacf229d85b7b550c40e85d2b7294cae99ba0dedf2e56c2064d4d9ec088  aws_r6d/singular.stdout
c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b  base_B.sing
```

Nested hashes used below also match, including `SOURCE_CLOSURE` `6a577a40…`, `AWS_REGISTRATION` `f03265fa…`, `compile_certificate.py` `1a1f6ef1…`, `remote_worker.sh` `3e58dff8…`, empty compiler/CAS stderr `e3b0c442…`, both rc files `9a271f2a…` (`"0\n"`), compiled input `255a8bd3…`, v2 B input identical at `c905f1b5…`, charged reconstruct `67343b56…`, v2 compiler `dd25bb5b…`, v2 B stdout `77c933be…`, and the v2 freeze chain `SOURCE_CLOSURE → PRECOMPILE_FREEZE → PRESOLVE_FREEZE`.

Read in full before the verdict: the certificate `PREREGISTRATION.md`, `compile_certificate.py`, `remote_worker.sh`, `AWS_REGISTRATION.md`, `base_B.sing`, `RESULT.md`, every file under `aws_r6d/`, the complete v2 package (`PREREGISTRATION.md`, `compile_control2_rees_v2.py`, `remote_worker_v2.sh`, `AWS_REGISTRATION.md`, `COMPILE_CUSTODY.md`, freeze files, every r6d B artifact), v1 `SOFTWARE_CONTROL.md` with the v1 worker as a negative custody control, and the already written v2 source review as a prior algebraic identity of the same B input. Encoding A was not read as a result.

---

## Promotion

**Accept `IN ENCODING B, AFTER EXACT CONTRACTION OF THE REES-TRANSFORMED FINITE IDEAL FROM s!=0 AND THEN s=0, THE REDUCED STANDARD BASIS OF THE SPECIAL FIBRE CONTAINS THE MONOMIAL la^20. THAT MONOMIAL LIES IN THE FULL MINIMUM-WEIGHT INITIAL IDEAL in_w(I), INCLUDING ALL S-POLYNOMIAL CONSEQUENCES. IT IS NOT AN INITIAL FORM OF A SUBMITTED GENERATOR. ON THE TORUS WHERE la IS REQUIRED NONZERO, la^20 IS ALREADY A CANONICAL MONOMIAL OBSTRUCTION TO THIS WEIGHT. INDEPENDENTLY, TORUS ITSELF LIES IN THE SPECIAL FIBRE AT SATURATION EXPONENT ONE, AND THE ORIGINAL INVERSE-VARIABLE LOCALIZATION RETURNS (1). THIS EXCLUDES ONLY THE FROZEN SUPPORT a=1, h=q2=k=nu=0, mu=2/3, WEIGHT (4,1,1,22,22,30,30,30), WITH ALL EIGHT DISPLAYED COORDINATES NONZERO. ENCODING A IS NOT A RESULT. THIS IS NOT A MOVING-AXIS STATEMENT, NOT A q2 STATEMENT, NOT WHOLE-RAY/FAN COVERAGE, NOT D1, AND NOT JC2.`**

Do not promote this to: a dual-encoding theorem; emptiness of coordinate-hyperplane loci of the special fibre; later moving-axis or `q2` corrections; other supports, weights, residues, or loads; the whole correction ray or double-root fan; D1; or JC2.

---

## Charge 1 — `base_B.sing` is the frozen expanded Rees-v2 source; compiler delta is tag plus printing plus a source-identical saturation cross-check

**CONFIRMED**

`cmp` reports `base_B.sing` byte-identical to

```text
cases/max12_912_order3_d1_double_root_control2_rees_v2_20260826/aws_r6d_B/control2_rees_v2_B_expanded_inverse_lpdp.sing
```

Both hash to the charged identity `c905f1b5…`, which is also the r6d B output recorded in v2 `COMPILE_CUSTODY.md` and in the r6d compiler payload. The certificate does not re-expand from the charged reconstruct. It consumes the already-compiled expanded inverse-elimination source.

Anchor counts, read from the 66-line file, are exactly those the compiler demands:

| anchor | required count | observed |
|---|---|---|
| `OLD_TAG = max12_912_order3_d1_double_root_control2_rees_v2_20260826T005028Z_r6d_B` | 1 | line 24, the `AWS_TAG=` print, and nowhere else |
| `poly TORUS=la*tau*rho*q1*q0*r2*r1*r0;\n` | 1 | line 34, and nowhere else |

`compile_certificate.py` is AWS-only (`REFUSE_NON_LINUX`, `REFUSE_NON_AWS_EC2`), refuses any tag not prefixed `max12_912_order3_d1_double_root_control2_rees_certificate_`, refuses a `base_B.sing` hash other than `c905f1b5…`, and refuses a wrong anchor count. The only mutations of the frozen source are:

1. replace that one embedded v2 r6d B tag by the certificate job tag;
2. keep the `poly TORUS=…` line and insert, immediately after it, basis printing, `sat_with_exp(GH,⟨TORUS⟩)`, a unit-saturation gate, a direct `reduce(TORUS^e, GH)` gate, and `PASS_CONTROL2_REES_MONOMIAL_CERTIFICATE`.

No equation, weight, load, support mask, residue, ring, order, contraction, or `H=C,s` line is touched. The original inverse-variable block `JT=GH,v*TORUS-1` still runs after the insertion. The emitted stdout order is exactly that splice: special-fibre count, full basis, saturation exponent, monomial witness, certificate PASS, then the original torus-special-fibre block with the new tag.

```text
AWS_TAG=max12_912_order3_d1_double_root_control2_rees_certificate_20260826T010154Z_r6d
ENCODING=B_EXPANDED_REES_INVERSE_ELIM_LPDP_V2
B_CONTRACTION_GENERATORS=403
B_SPECIAL_FIBRE_GENERATORS=35
```

Those two generator counts are the same numbers as the v2 r6d B stream. The compiler stdout hash of the spliced file is `255a8bd3…`, matching `input.sha256`.

`sat_with_exp` is the source-identical saturation in the sense of the prompt: it saturates the same special fibre `GH` already computed by the frozen B source, by the same eight-factor `TORUS` already defined there, using `elim.lib` which the frozen source already loads. It is not a change of ideal. It is an independent algorithm from B's Rabinowitsch inverse `v`, and it is the same colon as encoding A's `sat(GH,⟨TORUS⟩)`, with the exponent returned.

---

## Charge 2 — construction order, and whether `GH[34]=la^20` is in the full minimum-weight initial ideal

**CONFIRMED. `la^20` is in `in_w(I)`, including every polynomial consequence. It is not an artifact of taking initial forms of the nine submitted generators.**

Frozen B construction, in order, with no intervening specialization:

```text
J  = ⟨E1,…,E8, LT, u s − 1⟩
GJ = std(J)
C  = eliminate(GJ, u)          # contraction from s≠0
H  = C + ⟨s⟩                   # then s=0
GH = std(H)                    # standard basis of the special fibre
```

Let `I ⊂ Q[X]` be the exact finite ideal in `X=(la,tau,rho,q1,q0,r2,r1,r0)`, generated by the eight specialized D1 rows minus targets together with `la−tau^3 rho`. Let `φ_s` be the Rees substitution `X_i ↦ s^{w_i} X_i` for

```text
w = (4, 1, 1, 22, 22, 30, 30, 30).
```

Then `C = φ_s(I) : s^∞`, computed by the Rabinowitsch inverse of `s`. For any `f∈I` of lowest weight `d`,

```text
φ_s(f) = s^d in_w(f) + s^{d+1}(⋯),
```

so `in_w(f)+s·(⋯)∈C` and `in_w(f)∈H`. Conversely, the lowest `s`-piece of a contraction identity is a `Q[X]`-linear combination of initial forms of elements of `I`. Hence `H` modulo `s` is the full initial ideal `in_w(I)`, not the ideal of submitted generator initials `{in_w(g_i)}`.

The certificate prints `GH` after `std(H)` and before any torus localization. The emitted reduced basis, under `option(redSB)`, has 35 elements, matching `B_SPECIAL_FIBRE_GENERATORS=35`. Its last two are

```text
GH[34]=la^20
GH[35]=s
```

A reduced standard-basis element that is the monomial `la^20` is the polynomial `la^20`, hence `la^20 ∈ H`. It does not involve `s`, so `la^20 ∈ in_w(I)`.

It is not `in_w(E8)`. Every term of submitted `E8` carries a positive power of `s`; the `la^20` terms are

```text
− s^80 la^20 − s^81 la^20 tau,
```

while the lowest `s`-power in `E8` is `52`, on the five `(q,r)` binomials. The ordinary-tail target `Lambda^{20}(1+tau)` sits 28 weights above `in_w(E8)`. Likewise `in_w(E3)` is the weight-52 `(q,r)` piece; the row-3 target `−(2/3) s^{60} la^{15}` is 8 weights higher. Direct inspection of all nine generators: none has a lowest `s`-piece equal to a power of `la`. The monomial `la^20` is therefore a consequence, obtained only after the contraction has used higher-weight terms to cancel lower-weight layers. That is the S-polynomial / Buchberger content of `in_w(I)`.

The same r6d host already computed this `H` in the v2 B stream (403 contraction generators, 35 special-fibre generators, wall 5.21 s, RSS ≈ 32 MiB). The certificate is a rerun of that Gröbner basis with extra printing and a cheap membership test, not a different ideal.

---

## Charge 3 — dehomogenization, weight reversal, block order, elimination, hidden localization; why `s=0` after contracting

**No defect found that could create `la^20` spuriously.**

**Why `s=0` after contracting, not before.** Every submitted generator is divisible by a positive power of `s` (`E1…E8` at least `s^{52}`, `LT` by `s^4`). Two wrong orders:

- Add `s=0` to the generators and do not invert `s`. Then every `E_i` and `LT` vanish identically, and the “special fibre” is the zero ideal in the coordinates. No `la^20`, and no condition at all. That is naive substitution, i.e. not even the generator-initial prevariety (the prevariety requires dividing out the lowest `s`-power of each generator separately).
- Add `s=0` together with `u s−1`. Then `⟨s, u s−1⟩=(1)`. The computation collapses to the unit ideal for a trivial reason.

Contraction first inverts `s` and intersects back. That is the Rees closure of the graph of the `G_m`-action. Only then does `s=0` cut the special fibre, which is `in_w(I)`. Adding `s` after contracting is the entire difference between the tropical variety and a meaningless substitution.

**Dehomogenization.** There is none. The source never sets `s=1`, never calls `subst`, `homog`, `imap`, or a dehomogenizing `s−1` except the Rabinowitsch inverse `u s−1`, which is localization at `s`, the opposite of setting `s=1`. The certificate prints the special fibre `s=0`, not a dehomogenized affine chart.

**Minimum versus maximum weight.** The Rees map attaches `s^{∑ w_i α_i}` to the monomial of exponent `α`. Lowest weight produces lowest `s`-power and is what survives `s=0` after saturation. Direct evidence against reversal, read from the frozen generators without rerunning a compiler:

| generator | `s`-powers present | recorded / visible minimum |
|---|---|---|
| `E1` | `{52}` | 52 |
| `E2` | `{52,60}` | 52 |
| `E3` | `{52,60,66}` | 52 |
| `E6` | `{60,66,74}` | 60, not the maximum 74 |
| `E8` | `{52,60,66,74,80,81,82,88}` | 52; `la^20` lives at 80 |
| `LT` | `{4}` | 4, homogeneous |

The v2 compiler's `initial_data` uses `min`, and the r6d payload records those minima. This certificate does not recompute them; it inherits the same polynomials.

**Block order.** Ring

```text
R=0,(u,v,s,la,tau,rho,q1,q0,r2,r1,r0),(lp(3),dp(8)).
```

The lex block `(u,v,s)` is an elimination block for the two inverses and the Rees parameter. The `dp(8)` block is a tie-breaker on the eight finite coordinates after `s` is set to zero. It is not a weight order on `X`, and it does not reverse `w`. A Gröbner basis of `in_w(I)` may be taken with respect to any monomial order on `X`; a polynomial that is the monomial `la^20` is in the ideal independently of that tie-breaker. `option(redSB)` makes that polynomial the reduced basis element, not a leading-term abbreviation of a longer polynomial.

**Elimination.** `eliminate(GJ,u)` is the first Rabinowitsch step. `u` is the largest lex variable, and Singular `eliminate` additionally builds its own elimination order. The synthetic controls of the same inverse-elimination, still present and still passing,

```text
⟨s, u s−1⟩ ∩ Q[s,X] = (1),
⟨s(q1−1), u s−1⟩ ∩ Q[s,X] = ⟨q1−1⟩,
```

are exactly the contraction identities. `v` is idle during this first basis; it does not appear in `J`. That is ring hygiene inherited from v2, not a change of ideal.

**Hidden localization.** The certificate prints `GH` before `v·TORUS−1` is adjoined. `la^20` is therefore a polynomial-ring member of the special fibre, not an element of a localized ring that could have inverted `la`. The later torus localization is a separate check, not the source of the monomial.

---

## Charge 4 — `GH[35]=s`, `sat_with_exp=1`, direct reduction of `TORUS^1`, inverse-variable localization

**CONFIRMED as four mutually consistent exact checks. `la^20` alone is already the canonical monomial obstruction on this torus, because `la` is required nonzero.**

Emitted certificate block:

```text
GH[34]=la^20
GH[35]=s
TORUS_SATURATION_EXPONENT=1
MONOMIAL_WITNESS=TORUS^1
PASS_CONTROL2_REES_MONOMIAL_CERTIFICATE
B_TORUS_SPECIAL_FIBRE_GENERATORS=1
TORUS_SPECIAL_FIBRE_IS_UNIT=1
GHT[1]=1
```

No `FAIL_CERTIFICATE_*` line exists. The worker would have died on any `FAIL_` line, on a missing certificate PASS, or on a missing v2 B PASS.

Interpretation, independently:

1. **`GH[35]=s`.** `H=C+⟨s⟩` contains `s` by construction. With `s` lex-larger than the eight coordinates, a reduced basis of `H` is `{s}` union a reduced `dp`-basis of `in_w(I)`. The last element being `s` is the expected elimination signature, not a hidden relation among coordinates, and not a localization.

2. **`sat_with_exp(GH,⟨TORUS⟩)=(1)` at exponent 1.** In `elim.lib`, `sat_with_exp` returns the saturation `GH : TORUS^∞` and the least `e` such that `GH : TORUS^e` equals that saturation. Exponent 1 and unit saturation together mean `TORUS ∈ GH` as a polynomial, and therefore `GH : TORUS^∞ = (1)`.

3. **Direct reduction of `TORUS^1`.** The inserted gate is `reduce(TORUS^SATEXP, GH)==0` with `SATEXP=1`. This is polynomial division against the already computed special-fibre basis. It does not invert any variable. It is the same membership as (2), viewed without the saturation API.

4. **Inverse-variable torus localization.** The frozen tail still forms `⟨GH, v·TORUS−1⟩` and eliminates `v`. If `TORUS∈GH`, this ideal contains both `TORUS` and `v·TORUS−1`, hence `1`. The emitted `GHT[1]=1` with size 1 and `TORUS_SPECIAL_FIBRE_IS_UNIT=1` is that independent Rabinowitsch check. It is the same check that the v2 B stream already printed, now run on the tag-replaced source.

These four are consistent. (1) describes the `s`-direction. (2) and (3) are the same polynomial membership `TORUS∈GH`. (4) is an independent algorithm for the same colon. None of them is the source of `la^20`; they confirm that the torus special fibre is the unit ideal.

**Is `la^20` already enough?** Yes. The residue torus is the open set where all eight displayed coordinates are nonzero. In particular `la≠0`, which is the condition that `Lambda` has exact valuation `4` rather than strictly larger. A monomial `la^{20}` in `in_w(I)` is already a monomial in the Laurent sense after inverting `la`, so this weight vector does not lie in `trop(I ∩ (G_m)^8)`. Saturating only by `la` would already yield `(1)`. The eight-factor product is a stronger, independently verified membership, not a necessary crutch for the obstruction.

`la^20 ∈ in_w(I)` does not, by itself, imply `TORUS∈GH` in the polynomial ring: `dp`-leading term `la^{20}` has degree 20 and does not divide `TORUS` of degree 8. The two memberships are therefore genuinely separate facts about `GH`, both reported, both consistent with a unit torus fibre.

---

## Charge 5 — generator initials vanish at the residue, yet the full initial ideal contains `la^20`

**CONFIRMED. This is the tropical-prevariety versus tropical-variety / S-polynomial distinction. The code does not conflate them.**

The v2 compiler, whose nine generator-initial records this certificate inherits, refused to compile unless the *minimum*-weight form of every submitted generator vanished at

```text
(la,tau,rho,q1,q0,r2,r1,r0) = (1,1,1,1,−1,1,1,−2).
```

Hand evaluation of the lowest `s`-piece of each frozen B polynomial at that residue, already recorded in the v2 source review and re-read here against `base_B.sing`, is zero on all nine. Supports match the payload `2,3,4,5,5,5,5,5,2`. That is membership of the residue in the tropical *prevariety* of the presented generators: each `in_w(g_i)` is a non-monomial that dies at the residue.

It is not tropical membership of `w` for the ideal `I`. Tropical membership of a weight for `I ∩ (G_m)^8` is the condition that `in_w(I)` contain no monomial. The certificate exhibits the monomial `la^20`.

Concrete leftover, not used by the generator-initial check. The weight-60 piece of submitted `E3` at the same residue is

```text
(−2/3) la^{15} + (4/9) r2 r1  ↦  −2/3 + 4/9 = −2/9 ≠ 0.
```

That leftover is strictly higher than `in_w(E3)`. An S-polynomial (or any contraction combination) that cancels the weight-52 layer of several rows can promote such a higher piece, or a combination of several rows including the weight-80 target of `E8`, to a lowest-weight monomial. The contraction is designed to see that monomial. Setting `s=0` in the generators alone would never see it.

The code path does not equate the two:

1. compiler (v2, inherited): residue misses a generator initial → compile failure, a negative control that the residue is on the prevariety;
2. solver: contract, then `s=0`, then print `GH`;
3. certificate: `la^20` is read from that basis, *before* torus localization;
4. `CONTROL2_REES_RESIDUE_SURVIVES` is still set from `Htor + m_residue`, never from step 1.

This is why a truncated Newton jet through `t^{60}` can match the D1 targets at this residue while the exact eight-variable initial ideal still contains `la^20`: the jet is a coefficient identity in a series; the Rees special fibre asks whether any arc in this finite ring has this leading weight on the torus.

---

## Charge 6 — exact promotion scope

**CONFIRMED. `RESULT.md` already states the legal exclusion and no more.**

What this encoding-B monomial certificate excludes:

- frozen support mask `a=1`, `h=q2=k=nu=0`, `mu=2/3`;
- weight `(4,1,1,22,22,30,30,30)`;
- the open torus of the eight displayed coordinates, i.e. all of them nonzero.

In particular it excludes the displayed residue `(1,1,1,1,−1,1,1,−2)`, and every other nonzero residue at this same weight. `la^20` is stronger than a residue-specific maximal-ideal test: it empties the whole torus fibre of this weight.

What it does not exclude, and what must not be written as excluded:

- moving axis (`a`, `h` unfrozen);
- later `q2` directions;
- other supports;
- other weights, including the same ray with some coordinate of strictly higher valuation (that coordinate's residue `0`, i.e. an axis of this torus);
- other residues on those axes;
- other loads `(k,mu,nu)`;
- the whole correction ray, or the rest of the double-root Newton fan;
- D1 as a global statement;
- JC2.

The later coefficient `−t^{38}/2` of `r0` is not a ninth finite-ring variable. Rees closure in these eight coordinates is exactly the question whether some higher terms of these same eight coordinates exist. The monomial `la^20` says they do not, for this leading weight, on the torus.

`RESULT.md` matches this scope, including the firewall sentence on moving-axis / `q2` / other supports / other weights / fan / D1 / JC2. It still labels the consequence provisional pending encoding A. That dual-endpoint firewall is correct and is not weakened by this review. Encoding A was not read as a result and is not inferred.

---

## Charge 7 — AWS custody, and the v1 software-control firewall

**CONFIRMED**

**Source hashes.** Certificate `SOURCE_CLOSURE.sha256` matches the four local source files. AWS `source.check` reports all four OK before compile. Compiler then re-hashes `base_B.sing` against the pinned `c905f1b5…` and exits `REFUSE_BASE_HASH` on mismatch. `FREEZE.sha256` covers `SOURCE_CLOSURE` and `AWS_REGISTRATION`. `RESULT_FREEZE.sha256` covers `FREEZE`, `RESULT.md`, stdout, empty stderr, and rc; all five recomputed values match.

**Compiler.** rc `0`, stderr empty (0 bytes, `e3b0c442…`), unique marker `PASS_CONTROL2_REES_CERTIFICATE_COMPILER` once, no `FAIL_`. Caps: 16 GiB / 600 s, nice 10.

**Solver.** rc `0`, stderr empty, `/usr/bin/time -v` isolated in `singular.time` (wall `0:05.21`, user `5.19`, max RSS `32296` kB, `Exit status: 0`, command the compiled certificate). Unique markers, each once:

```text
PASS_B_SYNTHETIC_CONTROLS
PASS_CONTROL2_REES_MONOMIAL_CERTIFICATE
PASS_D1_DOUBLE_ROOT_CONTROL2_REES_V2_B
```

No `FAIL_` line. Worker requires both certificate and v2-B PASS counts equal to 1, nonempty-stderr rejection, and `FAIL_` rejection. Caps: 64 GiB / 1800 s, nice 10. Metadata: PID `194858`, tag `…T010154Z_r6d`, `WAITING_GO` then `PASS_REMOTE_WORKER`, matching `AWS_REGISTRATION.md`. Timing is comparable to the v2 B run on the same host (5.20 s user, 32340 kB), as expected for a reprint of the same Gröbner basis.

**Fail-closed AWS gate.** Linux, Amazon EC2, certificate tag prefix, source-hash, compiler PASS, solver rc, empty CAS stderr, both PASS markers, no `FAIL_`. Local Darwin cannot run the compiler.

**V1 software-control firewall.** V1 directed `/usr/bin/time -v` into `singular.stderr` while requiring that file empty. `SOFTWARE_CONTROL.md` records that every completed v1 solve failed its own custody contract; Box02 A was stopped; r6d B's underlying Singular rc `0` still produced wrapper `SOLVE_FAILED`. Those streams are not evidence. V2 and this certificate separate `singular.time` from `singular.stderr`. The certificate worker accepts only the certificate tag prefix and compiles `compile_certificate.py`, not the v1 compiler. V1 cannot support this monomial.

**V2 B identity.** Contraction 403, special fibre 35, torus fibre unit, `GHT[1]=1`, residue unit, `CONTROL2_REES_RESIDUE_SURVIVES=0`, firewall string, v2-B PASS: all identical between the v2 B stream and this certificate stream, up to the inserted basis and the replaced tag. The monomial `la^20` is the missing explicit generator of that already-emitted unit.

Local artifact gap, non-blocking: the remote tarball hash `ae2e7e72…` from `AWS_REGISTRATION.md` is not present as a file in the local case directory, so it was not recomputed. The four source files that tarball is supposed to contain are the files whose hashes are in `SOURCE_CLOSURE` and that `source.check` accepted.

---

## Directed defect search

| hunted defect | finding |
|---|---|
| `base_B.sing` silently rewritten | Byte-identical to frozen v2 r6d B input `c905f1b5…`. Compiler hash-pins that identity |
| Compiler changes equations, weights, or order | Only the AWS tag and a post-`TORUS` print/saturation block. Ring, `(lp(3),dp(8))`, nine generators, `u s−1`, `H=C,s` untouched |
| `la^20` is `in_w(E8)` | False. `E8`'s `la^20` terms are `s^{80}` and `s^{81}`; `in_w(E8)` is the `s^{52}` `(q,r)` piece |
| `s=0` before contraction | Not what the source does. That wrong order is either `⟨s⟩` with no coordinate relations, or `(1)` with `u s−1` |
| Dehomogenization `s=1` | Absent. `u s−1` is inversion of `s`, not setting `s=1` |
| Min/max weight reversal | Lowest `s`-power is the minimum weight. Row 6 and row 8 display higher leftover powers. `la^20` is a leftover, not a minimum of a submitted generator |
| Block order used as a hidden weight | `dp(8)` is a tie-breaker on `in_w(I)`. A reduced monomial basis element is order-independent membership |
| Malformed elimination of `u` or `v` | First block is `(u,v,s)`. Synthetic inverse-elimination controls passed. `v` idle until torus localization, after `GH` is printed |
| Hidden localization producing `la^20` | `GH` is printed before `v·TORUS−1`. `la^20` is a polynomial-ring member of `H` |
| `sat_with_exp` a different ideal | Same `GH`, same `TORUS`, library already loaded. Exponent 1 matches direct `reduce(TORUS,GH)` |
| Prevariety sold as tropical membership | Compiler residue check is the prevariety control. Result is `GH` after contraction. They disagree, and the code reports both |
| Overstrong promotion | `RESULT.md` and the printed firewall stay inside frozen axis, fixed load, this weight, torus. Dual A not claimed |
| V1 telemetry contamination | Certificate isolates `singular.time`. V1 is quarantined by `SOFTWARE_CONTROL.md` |
| Resource kill disguised as a unit | rc 0, 5.21 s, 32 MiB, no timeout, both PASS markers present |

Non-blocking notes, not repairs: (i) `v` is idle in the first Gröbner basis, inherited from v2; (ii) the remote source-archive blob `ae2e7e72…` is not in the local tree; (iii) encoding A is live and is not a result; (iv) `RESULT.md` still awaits A, which is the correct dual firewall rather than a defect.

---

## Sharpest non-claim

One-encoding, one-host, one-order monomial certificate: `la^20 ∈ in_w(I)` for the frozen-axis, fixed-load, weight-`(4,1,1,22,22,30,30,30)` degeneration of the exact eight-row D1 coefficient ideal, hence empty torus special fibre in encoding B. Not dual-encoding emptiness. Not emptiness of the axes. Not a statement about any other ray, residue, load, moving axis, or `q2` chart. Not a classification of the double-root fan. Not D1. Not JC2. The already certified control-2 finite successor through `t^{60}` remains a truncated identity; this certificate says that leading torus residue is not a point of the exact initial degeneration, because the full initial ideal contains `la^20`.

---

## Evidence layers (do not collapse)

1. Byte identity of `base_B.sing` with the frozen v2 r6d expanded B source, and a line-by-line reading of the certificate compiler's two substitutions.
2. Hand reading of the nine Rees-transformed generators: lowest `s`-powers versus the `la^{15}` and `la^{20}` target terms; residue vanishing of those lowest pieces; leftover `−2/9` on the weight-60 piece of `E3`.
3. Algebra of contraction, why `s=0` must follow inversion of `s`, initial ideals, and torus saturation, against the frozen B source and the inserted certificate block.
4. Reading of the emitted 35-element special-fibre basis, the four torus checks, and the v2 B stream as a prior custody-clean computation of the same `H`.
5. SHA-256 of the certificate freeze chain, AWS streams, v2 B input/stdout, charged reconstruct, and v1 `SOFTWARE_CONTROL.md` as a negative custody control.

Encoding A is not among these layers.

REES_CERT_CONFIRMED
