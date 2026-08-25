# Hostile different-model review — exact univariate `p`-elimination on the double-`B` leaf

| Field | Value |
|---|---|
| Claim under review | Frozen producer: exact `msolve 0.10.1` ELIM(8) on the corrected nine-variable saturation `J=I+(p*ip-1)` of the normalized `k=mu=0`, `nu=1` order-three double-`B` fibre returns a primitive `P(p)∈Q[p]` of degree 630, support `{0,9,...,630}`, and nonzero constant; hence every field point of `I` has `p` algebraic over `Q`, so an actual trajectory has constant `p` and constant `r8=-3p/10`, contradicting `9 r8'=j/u≠0` |
| Overall verdict | **INCONCLUSIVE** |
| Smallest failing identity | none found |
| Smallest missing certificate | a second characteristic-zero engine's elimination basis, `lift`, or cofactor identity proving `P∈J` over `Q` (equivalently, that the printed one-element list generates `J∩Q[p]`). Reconstructed output plus input replay plus three modular Singular matches do not discharge that certificate |
| Evidence tier | independent parse of all 71 terms; byte-for-byte regeneration from the pinned parent compiler; independent coefficient comparison of the eight source rows against the three Singular scripts; local re-run of all three frozen Singular product-order scripts; inspection of `msolve 0.10.1` `io.c`/`convert.c`/`update.c` for the `homogeneous input?` flag; unmodified frozen verifier only as a regression, not as evidence |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Repo | `/Users/dc/code/math/jc2` |
| Charged ancestor | none named by the launch prompt as a promotion dependency. Sibling `q`-algebraicity package unread as a theorem. Prior same-day research report `xmodel/max12-912-order3-double-b-p-algebraicity-grok-20260824.md` unread as a theorem |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (`Promote max12 DZ20 exclusion and source audits`). Named producer artifacts for this case are untracked on top of that HEAD; charged hashes below are unchanged |
| Review window (UTC) | `2026-08-24T22:40:00Z` – `2026-08-24T23:10:00Z` |
| Python | CPython 3.14.6 |
| Singular | 4.4.1 (local scratch re-run of the three frozen modular scripts only) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Frozen target reread in full before any verdict:

- `xmodel/max12-912-order3-double-b-p-elimination-20260824.md`
- `cases/max12_912_order3_double_b_p_elimination_20260824/` (every listed file)
- `cases/max12_912_order3_nu1_probe_20260824/generate_double_b_msolve.py`
- `cases/max12_912_order3_fibre_20260824/order3_fibre.py`
- `ops/aws_doubleb_run.sh` (invocation only)
- `msolve 0.10.1` sources `src/neogb/io.c`, `convert.c`, `update.c`, `f4.c` (flag and pair-degree path only)

No producer, case, canonical, coordination, prompt, log, run, or other review file was edited. `msolve` was not run locally. Independent reconstruction lived only in `/tmp`.

---

## Promotion

**Do not accept algebraicity of `p` over `Q`, emptiness of actual trajectories on this leaf, or any stronger statement.**

The frozen package is an honest producer-exact reconstruction of one non-unit univariate together with three modular Singular controls. That is not a characteristic-zero membership certificate. The producer already named this trust boundary; this review does not waive it.

Keep, as regression-only facts about the frozen bytes:

- the input is the source-honest normalized double-`B` saturation in `p`-last order;
- the printed `P` has degree 630, content one, 71 terms at exponents `9k`, and `P(0)≠0`;
- reducing `P` modulo `32003`, `100003`, and `104729` and normalizing the lead recovers the three frozen (and locally re-run) Singular product-order first elements, coefficient for coefficient.

**Do not promote this to:** a characteristic-zero Groebner basis of `J`; a Nullstellensatz identity `P=Σ h_i f_i`; emptiness of any other pair-norm leaf; a Taylor boundary; other loads; the order-one core; `(8,12)`; all `(9,12)`; maximum twelve; a counterexample; or JC2.

**Smallest valid successor.** An independent characteristic-zero engine must exhibit either a product-order / elimination Groebner basis over `Q` whose first element is a `Q`-multiple of `P`, or cofactors proving `P∈J`. Until that lands, the leaf remains open.

---

## Quarantine

No result here proves or disproves JC2, empties the double-`B` leaf, or constructs a nonconstant-`p` point. Frozen verifier `PASS` was not used as evidence. The sibling exact DRL basis of `J` (`cases/max12_912_order3_double_b_q_gb_20260824/`) is unread as a theorem: only its input polynomial body was compared byte-for-byte with this input. The earlier same-day research report that stopped at `INCONCLUSIVE` before this reconstruction arrived is not a parent. The fibre compiler is not a reviewed theorem; the eight tails used as evidence were rebuilt by calling `compile_fibre()` at `k=0`. Reviewed norm and terminal-row facts are consumed only for leaf identity and for `9 r8'=j/u≠0`, and only hypothetically, after membership.

---

## Scope (not enlarged)

Producer-exact reconstruction and modular controls on the normalized `k=mu=0`, `nu=1`, order-three double-`B` coefficient leaf `r1=r2=r3=r4=r5=r7=0`, `r6=1`, `3p+10 r8=0`, saturated by `p*ip-1`. No other leaf, all `(9,12)`, maximum-twelve, counterexample, or JC2 conclusion follows. The implication from `P∈J` to a trajectory contradiction is recorded as logic, not as a landed theorem.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Manifest, freeze, and result hashes match the launch prompt. The frozen verifier's checks are the ones it actually performs; an independent parser recovers the same 71 terms. `PASS` is not a membership certificate | **CONFIRMED** | a hash mismatch; a term the independent parser rejects; the verifier asserting `P∈J` |
| 2 | First input line is exactly the nine variables in `p`-last order, second line is characteristic zero, and the body is the eight source-honest normalized double-`B` equations plus `p*ip-1`. Regeneration from the pinned parent compiler matches byte-for-byte. Signs, denominators, and the specializations `k=0`, `r6-1`, `10 r8+3p` are correct | **CONFIRMED** | a tenth variable; `p` not last; a comment on line 1; a missing or extra equation; a sign/denominator mismatch against `compile_fibre()`; regeneration drift |
| 3 | Telemetry is a real `msolve 0.10.1` ELIM(8) reconstruction: nine valid equations, one polynomial lifted, 120 primes, zero bad primes, coefficient height 1828 bits, output characteristic zero, variable order `p`. It is not the malformed one-variable trials and not the characteristic-zero `[1]` short circuit | **CONFIRMED** | `#variables 1`; output `[1]` or `[-1]`; zero primes / no CRT; `#polynomials to lift` other than 1; a unit first modular basis |
| 4 | `homogeneous input? 1` is an ELIM-mode labeling side-effect in `msolve 0.10.1` `io.c`, not a dropped-constant parse and not a mathematical homogenization of `r6-1` or `p*ip-1`. It is a tool-reporting caveat. It does not discharge `P∈J` | **CONFIRMED as caveat, not as a parse error** | constants absent from the parsed generators; DRL sibling of the same body reporting a different polynomial body; modular inhomogeneous Singular minpoly disagreeing with `P` |
| 5 | Exact `P` has degree 630, primitive content one, exactly 71 nonzero terms at exponents `0,9,...,630`, and nonzero constant. Reducing `P` modulo `32003`, `100003`, and `104729` and normalizing the lead matches all 71 coefficients of the frozen Singular outputs. Those scripts are source-equivalent to the parent tails. Local re-run of all three scripts reproduces the frozen outputs | **CONFIRMED** | a missing `9k` exponent; content `>1`; `P(0)=0`; a coefficient mismatch; Singular `r_i` not equal to the parent tail string; local Singular differing from the freeze |
| 6 | *If* `P` generates `J∩Q[p]`, then every field point of `I` has `p` algebraic over `Q`; in a trajectory field with algebraically closed constants `C`, `p` is constant; `3p+10 r8=0` makes `r8` constant; reviewed `9 r8'=j/u≠0` contradicts it. Saturation, nilpotent, embedded-component, constant-field, and differentiation loopholes do not break that implication. The hypothesis `P∈J` is the missing certificate | **INCONCLUSIVE** | a second-engine membership identity (would confirm the implication as a theorem on this leaf); a char-0 component of `I` with nonconstant `p` (would refute the proposed kill); a gap in `9 r8'=j/u` on this landing (would block the last step only) |
| 7 | Reconstructed exact elimination output plus input replay plus three independent modular Singular matches is **not** sufficient to `CONFIRM`. Exact membership/transformation from a second characteristic-zero engine remains mandatory | **INCONCLUSIVE overall, by this claim** | a landed `Q`-basis or cofactor identity for `P∈J`; equivalently, treating engine trust as a theorem, which this review refuses |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Hashes and replay (regression only)

Recomputed SHA-256 on the working-tree bytes match the launch prompt, `MANIFEST.sha256`, and `FREEZE.txt`:

| Artifact | SHA-256 | Cross-check |
|---|---|---|
| `xmodel/max12-912-order3-double-b-p-elimination-20260824.md` | `37667ebaa943b5f1a4a7afc46331ac0cdf3d1ab0bd0ead82047bce0677aead87` | prompt, `MANIFEST`, `FREEZE` |
| `cases/…/MANIFEST.sha256` | `576485096ba84b4fc8b329fb2e3d10c48a2e8b45ed85ce83d4a902238e6bc68d` | prompt, `FREEZE` |
| `cases/…/FREEZE.txt` | `198b9daa41ee299f5720d8024ce06606ec19598539a78edda2bb3c2c32ddb256` | prompt |
| `cases/…/result.out` | `50d71a0b76239db801e5c75ff9497f33d62086c4b8f7b5fd0a3e1bfb67852a75` | prompt, `MANIFEST`, `FREEZE`, `metadata` |
| `cases/…/input.ms` | `1bde828bfe3cddb7342a10436b34913c6cf1adebb4d668f0947b3a1f1ad1f287` | `MANIFEST`, `metadata` |
| `cases/…/verify_result.py` | `058fc2c656445637ae247bf4815c4831cc373e10709a5235527efc9075c76fa1` | `MANIFEST`, `FREEZE` |
| `cases/…/README.md` | `f8d219b32f76d53cd065a9dfdafa0d9493b63368b67651eaa9808ca046e48ebc` | `MANIFEST`, `FREEZE` |
| `cases/…/REGISTRATION.md` | `f6181a4aa9b982779dff304f4d25f77e3359a9f838fb083261be6d20cb286a72` | `MANIFEST`, `FREEZE` |
| `cases/…/replay.out` | `fa5affc39aec0776b2c62c2214392af23b624ca279d915f24b5ba8d5c67e55fa` | `MANIFEST`, `FREEZE` |
| `cases/…/stderr.log` | `162dddcb47c9bb4cf6f9255119ca2f83237ddf8bae23b7e821dd860d9e90644b` | `MANIFEST` |
| `cases/max12_912_order3_fibre_20260824/order3_fibre.py` | `a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf` | `MANIFEST`, generator pin |
| `cases/…/generate_double_b_msolve.py` | `5c1c6e6d6570d58f9c9f6104be151e6da68c90d0e2855af9021f533b92420b01` | `MANIFEST`, generator pin |
| coefficient-list of `P` | `459c4436ddc06c086171baab73a41bd9626e356c5749f445bf82766938431e68` | producer, verifier |

`shasum -a 256 -c cases/max12_912_order3_double_b_p_elimination_20260824/MANIFEST.sha256` is `OK` on every named path. Running the frozen verifier from the repository root prints the advertised `PASS` tail. That program hash-checks the frozen modular outputs, regenerates the input, and parses `P`; it does not recompute a Groebner basis, does not inspect `homogeneous input?`, and does not prove `P∈J`. It is regression only.

The case directory contains exactly the freeze/manifest/readme/registration/input/metadata/result/stderr/replay/verifier files and the three Singular script/output pairs. No enumerator is present. `msolve` is not invoked.

---

## Claim 1 — manifest, verifier, independent parse

**CONFIRMED.**

Every path named in `MANIFEST.sha256` hashes to the listed digest, including the producer report, the result, and the pinned parent compiler. `FREEZE.txt` hashes to the launch-prompt freeze digest. `result.out` is 38,205 bytes and hashes to the launch-prompt result digest.

The verifier's polynomial parser is a sign-splitting regular expression. An independent parser that requires an explicit integer coefficient on every term of the characteristic-zero output, then splits `*p^N` / constant, recovers the same 71 pairs `(coefficient, exponent)`. The two parsers agree on this particular string. The exact polynomial never uses a monic `p^N` token; the modular Singular outputs do, and were parsed by a separate monic-aware reader, not by the verifier's regex.

`PASS` therefore means: hashes, regeneration, support, primitivity, and the three frozen modular coefficient lists match. It does not mean `P` lies in `J`.

---

## Claim 2 — input, regeneration, signs, denominators, specialization

**CONFIRMED.**

The frozen `input.ms` is eleven lines:

```text
x0, x1, x2, x3, x4, x5, q, ip, p
0
<eight primitive integer polynomials, comma-newline separated>
p*ip-1
```

Nine declared variables, `p` last, characteristic zero, nine equations, no in-band comment. This is the opposite of the quarantined one-variable trials, which misread a comment as the variable declaration. The sibling DRL input `cases/max12_912_order3_double_b_q_gb_20260824/input.ms` has the same polynomial body byte-for-byte and declares `p` first; only the variable order changes.

Regeneration

```text
python3 cases/max12_912_order3_nu1_probe_20260824/generate_double_b_msolve.py \
  --characteristic 0 --mode saturated --order p-last
```

reproduces the frozen input exactly (SHA-256 `1bde828bfe3cddb7342a10436b34913c6cf1adebb4d668f0947b3a1f1ad1f287`). The generator pins parent SHA-256 `a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf` before calling `compile_fibre()`.

Independent reconstruction of the transverse tails at `k=0` yields term counts `10,16,20,29,35,48,57,73` for `r1,…,r8`. `r6` has no constant term before the shift. The eight emitted equations are the primitive integer contents of

```text
r1, r2, r3, r4, r5, r6-1, r7, 10*r8+3*p
```

in that order. Clearing denominators (powers of three) and contents:

| eq | denominator | content | terms |
|---|---:|---:|---:|
| 1 | 27 | 4 | 10 |
| 2 | 81 | 2 | 16 |
| 3 | 81 | 4 | 20 |
| 4 | 243 | 1 | 29 |
| 5 | 243 | 4 | 35 |
| 6 | 243 | 1 | 49 |
| 7 | 2187 | 4 | 57 |
| 8 | 6561 | 1 | 74 |

The first monomial of `r1` is `(4/9) x0 x5`; the primitive integer form starts `3 x0 x5`, scale `27/4`. Equation 6 ends in the constant `-243`, which is the primitive image of `-1` after multiplying by denominator `243`. Equation 8 ends in `+19683 p` with `19683=3^9=6561*(3)`, the primitive image of the summand `3p`. Each of the eight primitive strings matches the corresponding frozen input equation exactly. Each of the eight unscaled parent `coeff_string` values matches the corresponding `poly rN=…` line of all three Singular scripts exactly.

The generator's `p1` mode is not this input. Saturated mode adjoins only `p*ip-1` and sets `k=0` in the ring map; `mu` is not a transverse coordinate. Normalization `nu=r6=1` is the constant `-1` shift, not a substitution of a symbol `nu`.

---

## Claim 3 — msolve 0.10.1 telemetry versus the two known failure classes

**CONFIRMED.**

Runner `ops/aws_doubleb_run.sh` backend `msolve-sat-elim-p-last` invokes

```text
msolve -f input.ms -o result.out -t 32 -v 2 -g 2 -e 8 --random-seed 0
```

which matches `metadata.txt` (`msolve=0.10.1`, `command=msolve saturated elimination order=p-last block=8`, `exit_code=0`, `final_status=DONE`, 61 s elapsed on the 128-thread host) and `stderr.log` (seed 0, 32 threads, `ELIM(8)`).

Logged input: 9 variables, 9 equations, 0 invalid, characteristic 0. First modular F4 reports `size of basis 10`, then

```text
[1]
#polynomials to lift              1
```

followed by CRT/rational reconstruction: 120 primes, 0 bad primes, max coefficient bitsize 1828, then a printed non-unit polynomial. Output header:

```text
#field characteristic: 0
#variable order:       p
#monomial order:       graded reverse lexicographical
#length of basis:      1 element
```

This is the non-unit `-g 2` reconstruction path. It is not the unit-ideal short circuit: that path returns after the first modular F4 when the reduced basis is `{1}`, prints `[1]`, and never enters CRT (`xmodel/grok-msolve-erratum.md`, `jc72108/CERT-UPGRADE.md`). The log contains neither `Grobner basis has a single element` nor `[-1]`. The token `[1]` that does appear is the lift-count banner for one remaining-variable polynomial, not the constant `1`.

The malformed one-variable trials are excluded by the first line of the input (nine identifiers, no comment) and by `#variables 9`. They supply no evidence here.

Independent parser: degree 630, 71 terms, exponents `630,621,…,0`, content one, constant term nonzero, leading coefficient 1726 bits. Reported height 1828 bits is therefore some other coefficient, not a contradiction.

---

## Claim 4 — `homogeneous input? 1`

**CONFIRMED as an ELIM-mode labeling caveat. Not a parse error, not a dropped-constant mathematical error, and not a discharge of membership.**

Visible constants exist: equation 6 ends `-243`, equation 9 is `p*ip-1`. The sibling DRL run of the *identical* polynomial body logs `homogeneous input? 0`. So the flag is not a property of the polynomials as written. It tracks the monomial order.

In `msolve 0.10.1` `src/neogb/io.c` `import_input_data`, when `st->nev>0` (elimination block nonempty), the code scans each generator for a later term whose `hd.deg` strictly exceeds the first term's, sets `st->homogeneous=1` on the first such occurrence, stores that maximum as the polynomial `DEG`, and then *skips* the actual equal-degree homogeneity test. In ELIM(8) the leading term is leading for the block order, not for total degree: a later term such as `x0 x2 p` has higher total degree than `x0^2` while losing on the first block. That is exactly the situation of the inhomogeneous rows `r6-1` and `10 r8+3p`. The assignment is a sugar/max-degree side-effect, not a declaration that constants were discarded.

Computational uses of the flag in 0.10.1:

- `meta_data.c`: print only;
- `convert.c`: records `min_deg_in_first_deg_fall` only when `homogeneous==0` (an FGLM statistic, unused by `-g 2 -e 8`);
- `msolve.c`: a different, projective path that *exits* if the input is not homogeneous — not this invocation;
- `sba.c` / `f4sat.c`: signature / saturation engines, both off (`signature-based computation 0`);
- `update.c` pair degrees in elimination mode use the stored `DEG` sugar, not the boolean.

F4 still processes the actual generators, including constant terms, until the pair set is empty. The first modular basis has ten elements, matching the three Singular product-order bases of the inhomogeneous system. The reconstructed `P` has `P(0)≠0`; dropping `p*ip-1` to `p*ip` would have allowed `p=0` into `J` and forced a vanishing constant term.

Load-bearing conservative reading: the flag is a tool-reporting caveat attached to elimination mode. It is not evidence that the engine computed a different ideal. It is also not evidence that the engine's output is a `Q`-basis of `J`. Membership remains Claim 7.

---

## Claim 5 — exact `P`, three modular Singular matches, source equivalence

**CONFIRMED.**

Independent parse of `result.out`:

- 71 nonzero terms, exponents exactly `{630,621,…,9,0}`;
- `gcd` of absolute coefficients is 1;
- constant term nonzero (1484 bits);
- coefficient-list SHA-256 `459c4436ddc06c086171baab73a41bd9626e356c5749f445bf82766938431e68`.

The three Singular scripts differ only by the prime in the ring declaration and the `PRIME=` print. Each is

```text
ring R=<prime>,(x0,x1,x2,x3,x4,x5,q,ip,p),(dp(8),dp(1));
ideal I=r1,r2,r3,r4,r5,r6-1,r7,10*r8+3*p,p*ip-1;
ideal G=slimgb(I);
```

with `r1,…,r8` equal as strings to the parent-compiler tails. That is the same ideal as the msolve input up to units in `Q`. Product order `(dp(8),dp(1))` is the Singular analogue of ELIM(8) with `p` last.

Local re-run, Singular 4.4.1, scratch only, all three scripts: stdout is byte-identical to the frozen `mod_*.out`. Each reports `size=10`, `dim=0`, `deg=1188`, and a monic degree-630 polynomial in `p` with 71 terms at the same exponents.

Reducing the characteristic-zero `P` modulo each prime and multiplying by the inverse of its leading coefficient recovers every modular coefficient, including the three constant terms `-4785`, `-45933`, `25007`. None is zero, so these fibres have `p≠0`, as required of a saturation by `p`.

These matches are independent-engine controls at three primes outside msolve's ~2^30 machine-prime band. They are not a Groebner basis of `J` over `Q`.

---

## Claim 6 — elimination logic and loopholes

**INCONCLUSIVE**, because the hypothesis `P∈J` is the missing certificate. The implication from that hypothesis is sound.

Let `I⊂Q[x0,…,x5,q,p]` be the eight-equation unsaturated ideal, and `J=I+(p*ip-1)` in nine variables. The printed one-element list is claimed as a basis of the *elimination ideal* `J∩Q[p]`, not of `J` itself. If that claim holds, then `P∈J`.

**Field points of `I`.** If `p=0`, then `p` is the constant `0`. No primary decomposition of the `p=0` slice is required for that tautology. If `p≠0` in a field, `ip=p^{-1}` exists in that field and the tuple extends uniquely to a point of `V(J)`, so `P(p)=0`. Thus `p` is algebraic over `Q` at every field point of `I`.

**Saturation.** Adjoining `p*ip-1` is the graph of inversion, not a black-box `sat(I,p)`. Points with `p=0` do not extend; they are already constant. Points with `p≠0` extend uniquely. No extra field points are added, and no nonzero-`p` field points are lost.

**Nilpotents and embedded components.** A field-valued point sees only the reduced support. If `J` is zero-dimensional over `Q`, a component of `I` on which `p` is nonconstant would be dense in `p≠0` and would spread to a positive-dimensional subset of `V(J)`, a contradiction. That zero-dimensionality over `Q` is again the uncertified engine claim. Modular zero-dimensionality at every tested prime, including the three independent Singular primes, is the expected reduction of a `Q`-scheme of dimension zero, and is not a proof that no dim-1 component exists over `Q`. Spreading-out of dimension fails at only finitely many primes; 123 agreeing primes make a modular ghost extraordinarily implausible and still do not replace a `Q`-basis.

**Constant field.** An actual trajectory lives in `L=C(x)(u)` with `u^3=h` and algebraically closed constants `C`. An element of `L` algebraic over `Q` lies in `C`. This is the same constant-field step already used on this landing; it does not need a new identity.

**Differentiation.** On the leaf, `3p+10 r8=0` is a defining equation (source-honest, Claim 2). Constant `p` forces constant `r8`. The reviewed Faber landing identity is `9 r8'=j/u≠0` (collision-boundary review SHA-256 `6d34908cbd2ead9769e4090fcab903ec5d5b7bd9db485db1d681708c5d36946e`, consuming the reviewed high-row landing). Double-`B` is the retained `s=0` stratum of the reviewed unordered pair-norm (critical-value-norm review SHA-256 `b6ae9516430073e177a5174684109b437ab278fa04dd066686c58af57715588e`). That identity is a landing identity for actual Keller trajectories, not an absorption-only identity. If `p` is constant then `r8'=0`, contradiction.

The loopholes do not invent a counterexample. They also do not create a membership proof.

---

## Claim 7 — CAS trust boundary

**INCONCLUSIVE. Second characteristic-zero engine remains mandatory.**

What is inside the independently checked envelope:

- source-honest input, regenerated from the pinned compiler;
- a non-unit 120-prime rational reconstruction, not the `[1]` short circuit;
- a primitive degree-630 univariate whose support and constant term are as advertised;
- three independent Singular product-order minpolys, locally re-run, matching `P` coefficient-for-coefficient after lead normalization.

What remains engine trust, exactly as the producer wrote: identification of that printed polynomial with a generator of `J∩Q[p]`. `msolve 0.10.1` does not emit cofactors (`CERT-UPGRADE.md`). The frozen verifier does not call a second engine over `Q`. The three modular matches prove

```text
(J mod q) ∩ F_q[p] = (P mod q)
```

for `q∈{32003,100003,104729}` up to units. They do not exhibit `h_i∈Q[x0,…,x5,q,ip,p]` with `P=Σ h_i f_i`.

`CERT-UPGRADE.md` correctly refuses to demote a *non-unit* characteristic-zero reconstruction to the `[1]` erratum. That is an engine-trust remark about nonemptiness of the reconstructed list, not a membership theorem. This review does not turn that caveat into invented wrong math, and does not treat it as a substitute for `P∈J`.

A Singular race over `Q` is the named successor. It was not present in the frozen package and was not run here.

---

## Exact promotable sentence, and strict scope

**Promotable, and no more:**

> On the frozen normalized `k=mu=0`, `nu=1`, order-three double-`B` saturation `J=I+(p*ip-1)` in `p`-last order, `msolve 0.10.1` reconstructed a primitive integer polynomial `P(p)` of degree 630 with 71 terms at exponents `9k` and nonzero constant term; that polynomial reduces, after leading-coefficient normalization, to the product-order minpoly of `J` at each of `32003`, `100003`, and `104729`, independently re-run in Singular 4.4.1. Exact membership `P∈J` over `Q` is not certified.

**Not promotable:** `p` is algebraic over `Q` at every point of `I`; every actual trajectory on this leaf is impossible; the double-`B` leaf is empty; any statement about other leaves, `(9,12)`, maximum twelve, a counterexample, or JC2.

---

## Non-blocking remarks

- The printed monomial order `graded reverse lexicographical` on the single remaining variable `p` is the second block of ELIM(8), not a claim that the nine-variable computation was DRL.
- First modular F4 `size of basis 10` agrees with Singular `size=10` at the three small primes. Degree `1188` versus `deg P=630` is compatible with extra `q`-degree (and the auxiliary `ip`) on a zero-dimensional scheme; `1188/630` is not an integer, so `P` is not simply a power of a degree-`1188` minpoly.
- Weighted homogeneity of the unsaturated tails, broken by `r6-1`, explains the support `p^{9k}` as the `nu=1` slice of a relation of weight `18` in `(p,nu)`. That picture is consistent and unused as a proof.
- The verifier does not read `homogeneous input? 1`. That omission is why Claim 4 had to be attacked from `msolve` source and from the DRL sibling, not from `PASS`.
- Local Singular 4.4.1 versus the frozen scripts' AWS Singular 4.3.2 produced identical modular outputs. That is a robustness check, not a characteristic-zero lift.

---

## Quarantine (close)

The reconstructed polynomial is a real object with three independent modular shadows. The trajectory kill is a correct implication from an uncertified membership. Overall `INCONCLUSIVE` until a second characteristic-zero engine writes `P` as an element of `J`.
