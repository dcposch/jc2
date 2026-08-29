# Hostile review — D1 `a=9`, `d=2,3` grade-38 order-three tail

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_d23_a8a9_j38_r3_tail_20260826/` charged on `RESULT_A9.md` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing source family | none through grade 38. Earliest polar family outside the window is `k6*R*C/L^3` at grade 39 (`d=2`) and `R*A^2/L^2` at grade 39 (`d=3`); first pole-four family is `k6*A*C/L^4` at grade 42 (`d=2`) or 43 (`d=3`) |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, validator strings, and finite-field agreement are not authority |
| Method | SHA-256 of every named pin and nested compiled manifest; independent four-atom expansion of `f=K^2+sigma^5 D` and binomial census of all four summands at `(A,C,R)=(9,11,9)` and `(9,12,9)` with product range larger than the compiler's; generating-function reconstruction of the pole-three odd functional with moving `p(sigma)`; exact match of analytic/literal monomial inventories; compiled-script inspection of the seven-row bridge, targets, unit ideal, and `eta`. No Singular re-execution, Sage, msolve, Lean, low-`a` support miner, or neighboring promotion as proof |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of the five required primary pins match. Every path named in `FREEZE.sha256` (21/21) and `EVIDENCE_A9.sha256` (108/108) rehashes to the printed digest, as does `PRODUCER_FREEZE_A9.sha256` (4/4). Nested `compiled.sha256` on all six retrieved lanes rehashes (3/3 each). Frozen `tails.json` is `d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`; canonical all-tails digest is `6eed03d486e1cd9e8d990eed74a105293d383882bbae77d204eac190cce387e8`. Exact `Q` is the characteristic-zero endpoint; `F_65519` and `F_65521` are separate compiled inputs and separate engine transcripts. The neighboring `(a,d)=(8,3)` cell is outside this verdict. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

After the frozen generic-square and D1 source gates, on the named open `D(p*k0*J)`, write

```text
A = sigma^9 (a1(sigma) + t a0(sigma)),
C = sigma^c (c1(sigma) + t c0(sigma)),     c=11 (d=2) or c=12 (d=3),
R = sigma^9 eta (b1(sigma) + t b0(sigma)),
```

with independent jets of the moving connection `p(sigma)`, of `A,C,R`, of the parenthesized loads `k10,k6,k2`, and of the sparse targets `mu2,mu4,mu6,J/4`. Through absolute grade 38 every source term that enters the seven first-normal rows has pole denominator at most `L^3`. Independently expanding all four binomial summands of `f^alpha` at both exact contacts yields exactly thirteen polar families per cell, padded-cutoff stable, with first pole-four wall at grade 42 (`d=2`) or 43 (`d=3`).

The odd Faber rows of any such source satisfy

```text
Phi7 + (p(sigma)/4) Phi5 + (3 p(sigma)^2/32) Phi3
     + (5 p(sigma)^3/128) Phi1  =  0   mod sigma^39.
```

Rows 1, 3, 5 are target-free. The only odd-row target is `-sigma^38*(J/4)` in row seven, so the same combination of the full rows is `-sigma^38 J/4` modulo `sigma^39`. Vanishing of the seven source equations therefore forces `J=0`. Adjoining `iJ*J-1` yields the unit ideal before radicals, which is emptiness on the named chart `D(J)`. The units `p` and `k0` are inherited from the upstream gates and are not inverted here; the exact open of the producer is `D(p*k0*J)`. This is not a theorem on `V(J)`, `V(p)`, or `V(k0)`.

The identity is polynomial in the independent variable `eta`. Substituting `eta=sigma^s`, `s>=0`, covers every closed tail `ord(R)>=9`. Extra nonnegative powers of the uniformizer only delay `R`-bearing families. Neither `eta` nor either leading `R` coefficient `b1,b0` is inverted. Orders of `A` and `C` are exact, not closed.

The neighboring cell `(a,d)=(8,3)` is a separate source, with seventeen polar families and a first pole-four wall at grade 41. Its 128-GiB failures are resource-only and supply no mathematical verdict here.

No claim is made about an equality face, another `(a,c)` cell, positive-order leading load outside the licensed series, `p=0`, `k0=0`, `J=0`, a terminal/global chart, the whole square component, order two, `(8,12)`, maximum twelve, or JC2.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 0. Five primary pins | hashes | all five match the required bytes |
| 0. Named manifests | every named file | `FREEZE` 21/21, `EVIDENCE_A9` 108/108, `PRODUCER_FREEZE_A9` 4/4, six nested `compiled.sha256` 3/3 |
| 0. Source archive | six AWS lanes | every retrieved `archive.sha256` is `01cca2d13adfd6685dd628b89f7eace7344b5c778b828d29563f8b8279040f53` |
| 1. Exact `Q` vs two primes | separate hosts, scripts, transcripts; rc, diagnostics, swap, no `qring` | **holds**; exact `Q` is characteristic 0; primes are software controls |
| 2. Four binomial summands | thirteen polar families at each of `(9,11,9)` and `(9,12,9)`; coefficients, grades, poles; padded cutoff; first pole four at 42 and 43 | **holds**; generous `product(range(13),repeat=4)` already exhausts grade `<=38` |
| 3. Derived jet ceilings | mechanical maxima enter grade 38; no omitted earlier polar source | **holds**; holomorphic `pole<=0` families do not enter the seven polar rows |
| 4. Seven-row reconstruction | frozen Faber tails, parenthesized loads, moving `p(sigma)`, jets, sparse targets; analytic/literal inventories | **holds**; `d=2` has 16083/10550 monomials, `d=3` has 11557/7551; byte-exact against frozen JSON |
| 5. Laurent-to-Faber `(R3)` | signs, moving `p(sigma)`, `mod sigma^39` | **holds**; combination is `[x^3](1-s x)^{-1/2} Phi(x)` with `s=p(sigma)/2` |
| 6. Full-row combination | exactly `-sigma^38 J/4`; even targets cannot enter; `iJ*J-1` is the unit ideal on `D(J)` | **holds** |
| 7. Homogeneous `eta` coverage | `eta=sigma^s`; no hidden inversion of `eta,b1,b0`; exact `A,C` vs closed `R` | **holds** |
| 8. Firewall | `(8,3)` excluded; equality/other face, load, `p=0`, `k0=0`, `J=0`, global/terminal, order two, maximum twelve, JC2 | **holds** |

---

## 0. Custody

Recomputed SHA-256 of the five required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT_A9.md` | `65ecc9cb8c4a51fb699e8ff86fdd4d5cb4b7dce744f77a77d2f0c4bc346c01db` | producer report |
| `.../PRODUCER_FREEZE_A9.sha256` | `3430b677791372e50b3fc0bc3ad2f504f234832c1f0f1f38f6a891dec64affd1` | producer pin list |
| `.../EVIDENCE_A9.sha256` | `0e953f19aef02184f0dc68e80b0d61deca5c53b5292d7b057744dfd848c20d53` | evidence freeze |
| `.../FREEZE.sha256` | `4a36e6ff0b97800559bbef9b1366ab1e995f2e1deef341b1d009b2d4f7595dc6` | source freeze |
| source archive on all six lanes | `01cca2d13adfd6685dd628b89f7eace7344b5c778b828d29563f8b8279040f53` | presented tarball |

`PRODUCER_FREEZE_A9.sha256` names four files, all matching, including `AWS_LAUNCH_METADATA_A9.md` at `2fe86b2653f2573e06ec2961a980bc678902b69a846031a543e9e92f25799cd8`. `FREEZE.sha256` names twenty-one files, all matching, including this cell's compiler/`run_aws.sh`/`launch_host.sh`, the frozen `a>=10` order-three parent, the `a>=13` order-two parent, the high-contact C2-shadow parent, the universal odd-pole promotion and its hostile review, `ops/aws_exact_lane.sh`, and the unused V1-failed wrapper. `EVIDENCE_A9.sha256` names one hundred eight retrieved files across the six `a=9` lanes; all one hundred eight rehash. Nested `compiled.sha256` files rehash to the retrieved `.sing`, `result.json`, and `source_inventory.json` on each lane.

`EVIDENCE_A9.sha256` begins with a Perl locale warning block. That is custody hygiene, not a hash failure: every 64-hex row after the warning rehashes, and the file digest is the charged pin.

The two inventories are byte-identical within each cell:

```text
a9d2  8d36d3dbcca9f868c64187717fe83183537bbf388af4afab56859342e8be5b5d
a9d3  78a6e51ecfae35bea663ab0fd850348cb186354d02b7b54947700c209b7f955d
```

Exact `Q` and the two primes are genuinely separate frozen runs. Compiled scripts are byte-identical after replacing the single ring-characteristic token `ring R=0,` versus `ring R=65519,` or `ring R=65521,`. Size gap 4 bytes equals the longer prime versus `0` once.

A passing manifest is not a theorem. What follows is the source.

---

## 1. Distinct frozen executions

| Charge | `a9d2` exact `Q` | `a9d2` `F_65519` | `a9d2` `F_65521` | `a9d3` exact `Q` | `a9d3` `F_65519` | `a9d3` `F_65521` |
|---|---|---|---|---|---|---|
| Host | Box02 `ip-172-30-0-186` | Box03 `ip-172-30-0-249` | r6d `ip-172-30-0-45` | Box02 `ip-172-30-0-186` | Box03 `ip-172-30-0-249` | r6d `ip-172-30-0-45` |
| PID | `303783` | `258839` | `324851` | `303831` | `258829` | `324878` |
| Characteristic | `0` | `65519` | `65521` | `0` | `65519` | `65521` |
| Compiled `.sing` SHA | `72d3b303f2988191…` | `f5e41967534355d5…` | `d7a5c0322606749d…` | `57ace535c6bbb2c3…` | `9a949fe9370c275d…` | `1c7cc2a16cc35722…` |
| Engine `rc` | `0` | `0` | `0` | `0` | `0` | `0` |
| Compiler stderr | empty `e3b0c442…` | same | same | same | same | same |
| Stdout SHA | `386c1ace212de6764884f34bd699a0639bf430c5044d7493c34031fce0a55eb0` | same boolean transcript | same | `8c2e9f50247bf33f4018a83807af8439ac21daf63411f189037dd90994e6b165` | same | same |
| Peak RSS KiB / swaps | 107,644,548 / 0 | 98,951,104 / 0 | 98,951,420 / 0 | 62,252,144 / 0 | 56,589,900 / 0 | 56,589,548 / 0 |
| Wall | 21:34 | 17:50 | 17:22 | 14:04 | 11:04 | 10:36 |
| VM cap / timeout | 134,217,728 KiB / 10800 s | same | same | same | same | same |
| Validator | `PASS_D1_A9_D2_J38_R3_TAIL_EMPTY` | same | same | `PASS_D1_A9_D3_J38_R3_TAIL_EMPTY` | same | same |
| `qring` | none | none | none | none | none | none |

Every lane presents the same source archive, passes the frozen `FREEZE.sha256` before compilation, runs `Singular -q` of the unique compiled input whose SHA is in `result.json` and `compiled.sha256`, and records GNU `time -v` with exit status 0, zero swaps, no `?`, no `error occurred`, and no `=FAIL`. Characteristic `0` on Box02 is the endpoint. The primes are second compiled scripts and second engines. They do not divide `2` and they do not kill a displayed denominator; they are still not a coefficient proof. Stdout hashes coincide within each cell because both engines print only the boolean/census sentinels; that agreement is not used below. The validator string is not a mathematical verdict.

Each compiled program is an ordinary polynomial ring `ring R=char,(…),dp;` together with `ideal S38=std(ideal(sigma^38))` and `S39=std(ideal(sigma^39))`, and `reduce` against those truncation ideals. There is no `LIB` line and no `qring`. Division by `sigma^38` is issued only after `reduce(full_rel,S38)==0`. Remainder zero against `std(ideal(sigma^39))` in `dp` is membership in the principal ideal `(sigma^39)` in the polynomial ring.

---

## 2. Independent expansion of the four binomial summands

The frozen square octic is `f=K^2+sigma^5 D` with `K=L^2+sigma^2 R`, `D=LA+C`, and `L=z^2+p(sigma)/2`. This is the substitution encoded by `source_coefficients` in the frozen `r1_d1_ac` parent. Expanding,

```text
f = L^4 + 2 sigma^2 R L^2 + sigma^4 R^2 + sigma^5 A L + sigma^5 C
  = L^4 (1+X),
X = 2 sigma^2 R/L^2 + sigma^4 R^2/L^4 + sigma^5 A/L^3 + sigma^5 C/L^4.
```

Those are the four atoms, scalars `2,1,1,1`. The frozen first-normal tails are polynomials in the octic coefficients `a0..a6` and the three loads `k10,k6,k2` of Lambda-weights `2,6,10`. With `Lambda=sigma^2` the four binomial summands of the source are therefore

```text
unloaded:     f^{3/2}              = L^6 (1+X)^{3/2},     fixed sigma 0,
k10:          sigma^4  k10 f^{5/4} = L^5 k10 (1+X)^{5/4},  fixed sigma 4,
k6:           sigma^{12} k6  f^{3/4} = L^3 k6  (1+X)^{3/4},  fixed sigma 12,
k2:           sigma^{20} k2  f^{1/4} = L   k2  (1+X)^{1/4},  fixed sigma 20.
```

Pole order of a monomial is `denominator - 4 alpha`. Polar families are those with pole `>=1`. Independently enumerating with `product(range(13), repeat=4)` — a strictly larger range than the compiler's cost bound — and also with cost-bounded pads `0,1,2`, yields the same thirteen polar families at each charged cell. Atom costs at both baselines are strictly positive.

### `ord(A)=9`, `ord(C)=11`, `ord(R)=9` (`d=2`)

| grade | pole | summand | `sigma^fixed` | `R` | `A` | `C` | coefficient |
|---:|---:|---|---:|---:|---:|---:|---|
| 28 | 1 | `k6` | 17 | 0 | 0 | 1 | `3/4` |
| 30 | 1 | unloaded | 10 | 0 | 1 | 1 | `3/4` |
| 31 | 1 | `k10` | 11 | 1 | 0 | 1 | `5/8` |
| 31 | 1 | `k2` | 22 | 1 | 0 | 0 | `1/2` |
| 32 | 1 | `k10` | 14 | 0 | 2 | 0 | `5/32` |
| 32 | 2 | unloaded | 10 | 0 | 0 | 2 | `3/8` |
| 34 | 2 | `k10` | 14 | 0 | 1 | 1 | `5/16` |
| 34 | 2 | `k2` | 25 | 0 | 1 | 0 | `1/4` |
| 34 | 1 | `k6` | 16 | 2 | 0 | 0 | `3/8` |
| 36 | 3 | `k10` | 14 | 0 | 0 | 2 | `5/32` |
| 36 | 3 | `k2` | 25 | 0 | 0 | 1 | `1/4` |
| 37 | 1 | `k10` | 10 | 3 | 0 | 0 | `5/16` |
| 37 | 2 | `k6` | 19 | 1 | 1 | 0 | `-3/8` |

Maximal pole through grade 38 is three. First pole-four family is `k6 A C / L^4` at grade 42, coefficient `-3/16`. Earliest polar families above the window: `k6 R C / L^3` and unloaded `R A^2 / L^2`, both at grade 39.

Sample coefficient, first family: `k6 sigma^{12} L^3 * binom(3/4,1) * (sigma^5 C/L^4) = (3/4) k6 sigma^{17} C / L`, grade `17+11=28`. Sample pole-four: `k6 sigma^{12} L^3 * binom(3/4,2)*2 * (sigma^5 A/L^3)(sigma^5 C/L^4) = (-3/16) k6 sigma^{22} A C / L^4`, grade `22+9+11=42`.

### `ord(A)=9`, `ord(C)=12`, `ord(R)=9` (`d=3`)

| grade | pole | summand | `sigma^fixed` | `R` | `A` | `C` | coefficient |
|---:|---:|---|---:|---:|---:|---:|---|
| 29 | 1 | `k6` | 17 | 0 | 0 | 1 | `3/4` |
| 31 | 1 | `k2` | 22 | 1 | 0 | 0 | `1/2` |
| 31 | 1 | unloaded | 10 | 0 | 1 | 1 | `3/4` |
| 32 | 1 | `k10` | 14 | 0 | 2 | 0 | `5/32` |
| 32 | 1 | `k10` | 11 | 1 | 0 | 1 | `5/8` |
| 34 | 2 | `k2` | 25 | 0 | 1 | 0 | `1/4` |
| 34 | 1 | `k6` | 16 | 2 | 0 | 0 | `3/8` |
| 34 | 2 | unloaded | 10 | 0 | 0 | 2 | `3/8` |
| 35 | 2 | `k10` | 14 | 0 | 1 | 1 | `5/16` |
| 37 | 1 | `k10` | 10 | 3 | 0 | 0 | `5/16` |
| 37 | 3 | `k2` | 25 | 0 | 0 | 1 | `1/4` |
| 37 | 2 | `k6` | 19 | 1 | 1 | 0 | `-3/8` |
| 38 | 3 | `k10` | 14 | 0 | 0 | 2 | `5/32` |

Maximal pole through grade 38 is three. First pole-four family is the same `k6 A C / L^4` at grade 43. Earliest polar family above the window: unloaded `R A^2 / L^2` at grade 39.

Both censuses are identical to the frozen `primitive_families` arrays. No fifth load, extra atom, or higher normal appears through grade 38. The low-`a` support miner was not consulted.

---

## 3. Derived jet ceilings and holomorphic families

Mechanical maxima from remaining grade `38 - base_grade` on every polar family that carries the corresponding normal or load, and from every polar family for the moving connection:

| cell | `A` | `C` | `R` | `k10` | `k6` | `k2` | `p` | `mu2` | `mu4` | `mu6` |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `d=2` | 8 | 10 | 7 | 7 | 10 | 7 | 10 | 10 | 6 | 2 |
| `d=3` | 7 | 9 | 7 | 6 | 9 | 7 | 9 | 10 | 6 | 2 |

Target ceilings are `38-28`, `38-32`, `38-36`. Independently recomputing `inventory_monomials` from these primitives and maxima reproduces the frozen JSON byte-for-byte: 16083 analytic / 10550 literal monomials (`d=2`) and 11557 / 7551 (`d=3`). Every licensed source jet occurs in the literal inventory (`d=2`: 94 jets, `d=3`: 87 jets). Every mechanical maximum occurs in a grade-38 literal monomial: `a1_8,c1_10,b1_7,k0_7,k60_10,k20_7,ell10` (`d=2`) and `a1_7,c1_9,b1_7,k0_6,k60_9,k20_7,ell9` (`d=3`).

Fifteen holomorphic (`pole<=0`) binomial families exist through grade 38 at each cell, starting at grade 11. They are excluded from `H`. If they contributed to `Phi_1..Phi_7` they would demand jet ceilings far above the polar maxima (an unloaded `R` family at grade 11 would license `R`-jets through 27). The certificate that they do not contribute is the coefficientwise seven-row bridge of the complete frozen tails against the polar `H`, not the enumerator’s `pole<=0` skip. That bridge is encoded as

```text
reduce(SourcePhi_row - PredPhi_row, S39) == 0,    row=1..7,
```

in an ordinary polynomial ring, and was executed on exact `Q`. Producer PASS strings were not used as a substitute for inspecting this encoding.

No omitted higher normal, moving-`p`, load, connection, or target jet was found inside the window.

---

## 4. Literal source, targets, and the seven-row bridge

The complete source rows are the frozen seven-row Faber tails with `Lambda=sigma^2` and the D1 substitutions of §2, parenthesized load series, and moving `p(sigma)=p+2 sigma ell_1+cdots`. Independently inspected compiled input on exact `Q`:

- Rows 1, 3, 5: `FullPhi = SourcePhi` identically (target-free).
- Row 2: `FullPhi = (SourcePhi) - sigma^{28}(mu20 + … + sigma^{10} mu20_10)`.
- Row 4: `FullPhi = (SourcePhi) - sigma^{32}(mu4 + … + sigma^6 mu4_6)`.
- Row 6: `FullPhi = (SourcePhi) - sigma^{36}(mu6 + … + sigma^2 mu6_2)`.
- Row 7: `FullPhi = (SourcePhi) - sigma^{38}(J/4)`.

That is twenty-two licensed target jets, all retained, none on rows 1, 3, 5. The compiled script differentiates each even-row target and `J` through the corresponding `FullPhi` and reduces the derivative plus the claimed monomial against `S39`. Even-row targets remain in the complete seven-row bridge; the odd functional of §5 does not use those rows.

`PredPhi_row` is the frozen odd Faber transport of the polar generating function `H`, with

```text
T_{i j} = ((j/2)_n / n! / 2^n) p^n,    n=(i-j)/2,
```

for even nonnegative index gap, independently recovered as

```text
Phi1 = h1,
Phi3 = h3 + (p/4) h1,
Phi5 = h5 + (3p/4) h3 + (3p^2/32) h1,
Phi7 = h7 + (5p/4) h5 + (15p^2/32) h3 + (5p^3/128) h1.
```

The inverse series for `1/(1+s t^2)^q` is truncated through `t^8`, which is the last power needed for `h_7`; higher inverse degree only produces `t^{>=10}`. The encoding is the campaign odd generating function `Y_{q,e}=x^e/(1+s x)^q`, not a naive `(t^2+s)^{-q}` expansion about a pole. Matching the complete literal tails is the content of the bridge.

---

## 5. Universal pole-three odd functional

Pack odd Laurent and Faber rows as `Y(x)=sum h_{2m+1} x^m` and `Phi(x)=sum Phi_{2m+1} x^m`. The frozen transport is `Phi(x)=(1-s x)^{-1/2} Y(x/(1-s x))` with `s=p/2`. Proper odd principal parts of pole order at most `q` along `L=z^2+s` are spanned by `Y_{q,e}=x^e/(1+s x)^q` for `0<=e<q`, and map to `x^e (1-s x)^{q-e-1/2}`. For row seven take `M=3` and pole ceiling `r=3`. The functional `W=(1-s x)^{-1/2}` has ordinary coefficients

```text
1,    s/2 = p/4,    3 s^2/8 = 3 p^2/32,    5 s^3/16 = 5 p^3/128,
```

so

```text
[x^3] W Phi  =  Phi7 + (p/4) Phi5 + (3 p^2/32) Phi3 + (5 p^3/128) Phi1.
```

On a basis element this is `[x^3] x^e (1-s x)^{2-e}`, a polynomial of degree `2-e <= 2 < 3` for every `e=0,1,2`. Vanishing is an identity in `Q[s]`, not a grid. Substitution of the moving polynomial `p(sigma)` and truncation at `sigma^{39}` are ring homomorphisms and preserve it.

The compiled `source_rel` is exactly that combination of `SourcePhi_{7,5,3,1}` with `p` replaced by `p+2 sigma ell_1+cdots`. Because every polar family through grade 38 has pole at most three, and because the seven-row bridge identifies the complete source with the polar `H` through `sigma^{38}`, the source combination is zero modulo `sigma^{39}`.

The same combination of full rows receives no contribution from rows 2, 4, 6, and none from rows 1, 3, 5. Row 7 contributes the sole odd target `-sigma^{38} J/4`. Therefore

```text
full_rel  =  - sigma^{38} J/4    mod sigma^{39}.
```

This is encoded as `reduce(full_rel + sigma^{38}*J/4, S39)==0` and as `subst(full_rel/sigma^{38}, sigma, 0) + J/4 == 0`, after the divisibility check `reduce(full_rel, S38)==0`.

---

## 6. Localization and the unit ideal

Division by `sigma^{38}` is polynomial-ring division of an element of `(sigma^{38})`. The grade-38 coefficient is `-J/4`. Adjoining `iJ*J-1` produces the ideal `(-J/4, iJ J-1)` in the polynomial ring over `Q`. Then `J` lies in the ideal because `4` is a unit, and `1 = iJ·J - (iJ J-1)` lies in the ideal. The compiled test is `reduce(1, std(ideal(subst(q38,sigma,0), iJ*J-1)))==0` before radicals.

`J` is a target coefficient, not a source denominator. The argument proves emptiness on the named chart `D(J)` and says nothing on `V(J)`. The units `p` and `k0` are not inverted in this script: `p(sigma)` enters polynomially through `(1+s t^2)^{-q}` and the Faber transport, and `k0` is the leading coefficient of the `k10` load series. Both units are supplied by the cited square/D1 gates. The producer’s exact open is therefore `D(p*k0*J)`, and not a theorem on `p=0` or `k0=0`.

---

## 7. Closed `R` tails and exact `A,C`

`R` carries a free polynomial factor `eta`. The compiled ring contains `eta,b1,b0` as variables. There is no division by `eta`, `b1`, or `b0`, and no negative exponent of those variables, in either exact-`Q` script. The check `reduce(diff(source_rel,eta), S39)==0` is implied by `source_rel in (sigma^{39})`; the mathematical coverage is that the identity is polynomial in `eta`.

Substituting `eta=sigma^s` with `s>=0` raises `ord(R)` from 9 to `9+s`. Families with `R`-exponent zero (`k6 C`, unloaded `A C`, `k10 A^2`, unloaded `C^2`, `k10 A C`, `k2 A`, `k10 C^2`, `k2 C`) are unchanged. Families with positive `R`-exponent are delayed by `s` times that exponent. The contributing set at `ord(R)>=9` is therefore a subset of the `ord(R)=9` window after a nonnegative grade shift. Pole ceiling three and target placement are preserved; the first pole-four wall only moves later. Targets do not depend on `R`.

`A` and `C` have no extra homogeneous factor. The compiled substitutions are exact `ord(A)=9` and exact `ord(C)=11` or `12`. Raising `A` or `C` is a different cell and is not claimed.

---

## 8. Firewall

The compiler also knows the cell `(a,d)=(8,3)`, with seventeen polar families and first pole-four grade 41. That cell is not in `RESULT_A9.md`, not in `EVIDENCE_A9.sha256`, and not in this verdict. On-disk `aws_v2_failed_a8d3_*` directories record resource `rc` 14 at 128 GiB and supply no mathematical identity. A later higher-memory replay is a separate producer.

V1-failed wrapper files are frozen as ancestry and were not used. The charged executions are the six V2 `a=9` lanes.

This review did not import the low-`a` support miner, the `a=8,d=2` producer, the `a>=10` emptiness theorem, or any neighboring promotion as a proof of the `a=9` census or of the seven-row identities. The universal odd-pole identity was reconstructed from the generating function in §5; the pinned promotion is custody, not authority.

Out of scope, and not asserted: an equality face, another leading face, another `(a,c)` pair, positive-order leading load outside the licensed `k10,k6,k2` series, `p=0`, `k0=0`, `J=0`, a terminal or global chart, the whole square component, order two, `(8,12)`, maximum twelve, JC2.

---

CONFIRMED
