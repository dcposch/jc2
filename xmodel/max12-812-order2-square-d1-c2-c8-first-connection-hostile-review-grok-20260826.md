# Hostile review — D1 primary-C2 `c=8` first-connection split

| Field | Value |
|---|---|
| Target | `cases/max12_812_order2_square_owner_d1_c2_c8_k6_connection_split_20260826/` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Earliest missing source family | none |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Producer PASS markers, compile-time print strings, and the support miner are not authority |
| Method | SHA-256 of every named pin and evidence file; compiled-script inspection; independent four-summand atom census with pad `0,1,2`; independent expansion of the analytic generating function through grade 26; exact univariate extraction of the seven frozen `SourcePhi` rows at specialized points; hand reconstruction of both exact-`C` unit ideals, both root terminals, etale descent, and the closed `A,R` tail. No Singular, Sage, msolve, Lean, or package compiler was executed by the reviewer |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `418e413593120d19e15e6546eb50c985f4b1f038` |
| Date | 2026-08-26 |

Independently recomputed SHA-256 of every required primary pin matches. Every path named in `PRODUCER_FREEZE.sha256` (7 rows), source `FREEZE.sha256` (22 rows), and the 48 digest rows of `EVIDENCE.sha256` rehashes to the printed digest. All three nested `compiled.sha256` files rehash to the retrieved local compiled scripts and inventories once the AWS absolute prefixes are stripped. The `/tmp` source archive rehashes to the claimed digest, and every member rehashes to the corresponding workspace file. The quarantined V2 manifests rehash as well; they license no emptiness claim. No file other than this review was written.

---

## Verdict

**CONFIRMED.**

After the frozen generic-square and D1 unit-load source gates, in characteristic zero on `D(p*k0)`, the complete seven literal Faber equations have no point on

```text
ord(C)=8,  ord(A)>=8,  ord(R)>=7.
```

The independent padded census of the four binomial summands at the exact-contact boundary `(ord(A),ord(C),ord(R))=(8,8,7)` has exactly four polar primitive families through grade 26, with unique pole-two family unloaded `C^2`. The unique grade-25 family is `(3/4)k60 C/L`. After clearing `L^2`, the complete grade-26 numerator is

```text
N2 = (3/4) A C L + (3/8) C^2 + (5/8) k0 R C L
   + (3/4) (k60_1 C + k60 Cnext) L
   - (3/4) ell1 k60 C
```

modulo `L^2`. The last summand is the first moving-connection correction for `p(sigma)=p+2 sigma ell1+...`. Both next-`C` coefficients, `k60_1`, and `ell1` enter; omitting the connection breaks the numerator identity. All targets begin at grade 28 or later. Ordinary (non-polar) families, including `k6*A` at grade 25 and bare `k2` at grade 20, do not enter the seven polar rows through grade 26. The first polar `k2` family is `k2*R` at grade 29.

The scheme split `D(k60) union V(k60)` is exhaustive. On `D(k60)`, the grade-25 seven-row ideal contains `1` before radicals on each exact-`C` chart `D(c1)` and `V(c1) intersect D(c0)`. The inverses introduced there are `k60^{-1}`, `c1^{-1}` or `c0^{-1}`, and the ambient `p^{-1}`, `k0^{-1}`. No leading coefficient of `A` or `R` is inverted. On `V(k60)`, every contribution proportional to `k60` vanishes, including the moving connection and `k60 Cnext`, while the free `k60_1 C/L` term remains pole one and dies at the roots. On the finite etale cover `lambda^2=-p/2` the exact pole-two pair is `(3/8)(lambda c1+c0)^2` and `(3/8)(-lambda c1+c0)^2`. Both exact-`C` chart ideals contain `1` before radicals; descent from `D(lambda)` to `D(p)` is finite etale of degree two, hence faithfully flat. The Faber/root bridge is true only after adjoining `k60=0`; the unconditional moving-root gap is nonzero.

Raising `ord(A)` or `ord(R)` can only delay a family with positive `A` or `R` exponent. It cannot add a lower-grade polar family, change the pole ceiling through grade 26, or advance a target through grade 26. The four localized unit ideals therefore empty exactly the displayed closed tail on `D(p*k0)`, after the stated frozen gates, excluding the exact-square zero section `c1=c0=0`.

The statement does not cover `c>=9`, another primary or tied face, a positive-order leading load, `p=0`, `k0=0`, the exact-square zero section, a terminal/global chart, fan exhaustiveness, order two, maximum twelve, or JC2.

**CONFIRMED**

---

## Verdict table

| Issue | Charge | Finding |
|---|---|---|
| 1. Primary pins | seven claimed SHA-256 including producer-freeze `a44cfc00…` | **holds** |
| 1. Named manifests | `PRODUCER_FREEZE` 7/7, `FREEZE` 22/22, `EVIDENCE` 48/48 digest rows | **holds**; no locale-warning prefix |
| 1. Nested compiled manifests | three hosts, two rows each; source archive `5830f73c…` | **holds** against retrieved local files and `/tmp` tarball |
| 2. Exact `Q` vs two good primes; zero swap; validator; ordinary rings | separate hosts/rings; fail-closed; ordinary `ring`, no `qring` | **holds**; exact `Q` is the endpoint |
| 3. Singular 4.3.2 quotient-ring hazard | ordinary polynomial rings; explicit `std`/`reduce`; no noncanonical `qring` `==0`/`subst`/`diff` | **holds** |
| 4. Polar census at `(8,8,7)` through grade 26, padded | independently from four binomials, pad `0,1,2` | exactly four families; unique pole-two is `C^2`; no omitted polar source/load/`p`/target through 26 |
| 5. Grade-25 source and complete `N2`; seven-row bridges; targets | from analytic `H` and from literal `SourcePhi`, not PASS strings | **holds**; connection coefficient `-3/4`; jets enter; targets at 28,32,36,38 |
| 6. `D(k60)` unit ideals on both exact-`C` charts | `1` before radicals; list the inverses; no `A`/`R` inverse | **holds** |
| 7. `V(k60)` vanishing, etale pair, descent, unconditional gap | pole-two squares; unit ideals; gap nonzero before the split | **holds** |
| 8. Frozen V2 failure; omit-connection and omit-`C^2` controls | over-strong pre-split `ROOT_FABER`; V3 repairs placement | **holds**; V2 is no-verdict, not a hidden refutation |
| 9. Closed tail `ord(A)>=8`, `ord(R)>=7` | exponent/cost, not density; four unit ideals empty exactly the displayed cell | **holds** |
| Firewall | `c>=9`, other faces, loads, `p=0`, `k0=0`, zero section, charts, fan, order two, max twelve, JC2 | **holds**; kept out of the verdict |

---

## 1. Custody

Recomputed SHA-256 of the required primary pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `.../RESULT.md` | `e97f250d4889d4e134d095df3e047a7b3066b5f0b2e99baeefc7c0024ba252d8` | producer report |
| `.../EVIDENCE.sha256` | `7c87430fa3d69ddcd7b56148be9cca376623f112a9f09dcd2ef84911b7021fb7` | V3 evidence freeze |
| `.../FREEZE.sha256` | `2792fe768e383039d771ddf40a048931ff27852b5f7359a6a7d142a05e3a5736` | source freeze |
| `.../AWS_LAUNCH_METADATA.md` | `55e49b2d38740ff0bcf83aae3d3a75e7c061ecea56295f1b05b6c4da0fae7ffd` | launch/resource custody |
| `.../PREREGISTRATION.md` | `bd1bed04c66792061ad2985de3c99c6a5feed5e4d31f03c5e5e71d129c7abef6` | preregistration |
| `.../compile_c2_c8_connection.py` | `fc1ac06f6898e302a8def6f7b025423de277f54c3d444b9450a7d0a43f50ee84` | V3 compiler |
| `.../PRODUCER_FREEZE.sha256` | `a44cfc000e3f5156ceed2aff58fbaae24ca78316c6eeb405e8a7a800dd0a2d2b` | producer-level freeze (matches the charged digest) |
| `/tmp/jc2_d1_c2_c8_connection_v3_20260826.tgz` | `5830f73cc677c7765b6114c798f003004b49c7842b0ba5430655c7c33021c081` | source archive on all three V3 hosts |

`PRODUCER_FREEZE.sha256` names seven files, all matching: `RESULT.md`, `EVIDENCE.sha256`, `FREEZE.sha256`, `AWS_LAUNCH_METADATA.md`, and the three V2-quarantine pins `RESULT_V2_FAILED.md` `43868154…`, `EVIDENCE_V2_FAILED.sha256` `05532438…`, `FREEZE_V2_FAILED.sha256` `a4dbe723…`.

Source `FREEZE.sha256` names twenty-two files, all matching. Direct producer pins: preregistration `bd1bed04…`, compiler `fc1ac06f…`, `run_aws.sh` `5776dd81…`, `launch_host.sh` `c70de8a8…`. Ancestry consumed by that chain also rehashes: target-free `c=3..7` compiler `fdd28139…` and promotion `eaff1eaa…`; r1/d1 freeze `34b0f325…` and compiler `e024a13d…`; CGE3 freeze `a5efc70c…` and compiler `352ad4f2…`; frozen tails `d72f774c…`; load-ladder compiler `77f25216…`; first-normal Padé promotion `40790378…`; halfweight results `eb2cd803…` and hostile review `49744ab9…`; `A`-prolongation validator result `74551fe8…`; low-contact v4 result `b8ae74e5…`; small-AC residue lemma `3a81fe72…`; fan lower-hull reduction `c9ecfe40…`; contact-raising closure criterion `3c0a33ce…`; maximal-pole miner specification `c4eba2d7…`; `ops/aws_exact_lane.sh` `ebe06a10…`.

`EVIDENCE.sha256` is 48 digest rows with no locale-warning prefix. All 48 rehash. Nested `compiled.sha256` rows, which record AWS absolute paths, match the retrieved local compiled objects:

| Lane | `source_inventory.json` | `.sing` |
|---|---|---|
| exact `Q` / Box03 | `8ca9fc6b…` | `f1aa985e…` |
| `F_65519` / Box02 | `ad9af29b…` | `3d6a2012…` |
| `F_65521` / r6d | `9df44a67…` | `eb7be703…` |

The three compiled scripts differ by exactly the ring-characteristic token (`RC28=0` / `65519` / `65521`). Substitutions, recurrences, charts, terminals, and sentinels are otherwise byte-identical. All three inventories report `primitive_count=4`, `maximum_grade=26`, and scope `C_EQ_8_A_GE_8_R_GE_7_ON_D_P_K0_ONLY`. All three `archive.sha256` files record the same source-archive digest `5830f73c…`. The local tarball rehashes to that digest and contains the twenty-two frozen source files; every member rehashes to the workspace pin. A passing manifest is not a mathematical verdict. The algebra below is independent of those sentinels.

The print strings `C2C8_SOURCE_HASHES=PASS`, `C2C8_PADDED_CENSUS_IDENTICAL=1`, `C2C8_MONOTONE_A_R_CLOSED_TAIL=1`, and `C2C8_EXACT_C_CHART_COVER=1` are compile-time constants. They are not mathematical evidence. The corresponding identities are reconstructed in §§4–9.

---

## 2. Exact `Q`, two good-prime controls, swap, validator

Exact `Q` is the theorem endpoint. `F_65519` and `F_65521` are software/support controls only. They are three distinct registered AWS executions of the same frozen source archive.

| Charge | Exact `Q` (Box03) | `F_65519` (Box02) | `F_65521` (r6d) |
|---|---|---|---|
| Host | `ip-172-30-0-249` | `ip-172-30-0-186` | `ip-172-30-0-45` |
| Tag | `…_q_box03_v3_20260826T2148Z` | `…_p65519_box02_v3_20260826T2148Z` | `…_p65521_r6d_v3_20260826T2148Z` |
| Characteristic | `0` | `65519` | `65521` |
| Compiled script SHA | `f1aa985e…` | `3d6a2012…` | `eb7be703…` |
| Engine `rc` | `0` | `0` | `0` |
| Validator | `PASS_D1_C2_C8_CONNECTION_SPLIT_CLOSED_TAIL` | same | same |
| Stdout SHA | `a59389d2…` | same | same |
| Peak RSS / swaps | 20,396 KiB / 0 | 19,692 KiB / 0 | 20,424 KiB / 0 |
| Wall | 0.10 s | 0.09 s | 0.09 s |
| Source archive in registration | `5830f73c…` | same | same |
| Launcher PID | 278318 | 341548 | 353317 |
| On-host freeze check | 22/22 `OK`, SHA `ff450563…` | same | same |
| Compiler stderr | empty-file digest `e3b0c442…` | same | same |

Both control primes are prime. Neither divides `2,3,5,8`, and both are odd, so the denominators `2,4,8` and the numerators `3,5` remain units. The three validation files are byte-identical (`engine_rc=0` plus the same validator line), hash `32e2a539…`; that common payload is not evidence that the runs were copied. Identical stdout is expected: on success the script prints only `0/1` markers and fixed diagnostic strings. All three metas record `argv` as `timeout 1800` wrapping the lane-local compiler then `Singular -q` on the emitted script, return code 0, and stdout hashes matching `EVIDENCE.sha256`. Caps were 64 GiB virtual (`67108864` KiB) and 1800 s engine. Launcher PIDs match the registration files. Compiler stdout on each lane is exactly the corresponding `source_inventory.json`. Outer stdout/stderr are empty. Neither mathematical stdout nor stderr contains `=FAIL`, `// **`, a leading `?`, `error occurred`, or `Swaps: [1-9]`. Zero swap is recorded on every stderr.

The fail-closed validator requires each listed marker exactly once, including `C2C8_ENDPOINT=PASS_EMPTY_PRIMARY_C2_C8_CLOSED_A_R_TAIL`, and rejects the diagnostic patterns above. On-host `sha256sum -c FREEZE.sha256` ran before compilation on every lane.

---

## 3. Singular 4.3.2 quotient-ring hazard

Each generated program begins

```text
ring RC28=<char>,(z,t,sigma,p,ell1,a1,a0,c1,c0,cc1,cc0,b1,b0,k0,k60,k60_1,k20,mu2,mu4,mu6,J,lam,ic1,ic0,ik60,ilam,ip,ik0),dp;
```

There is no `qring`, no `sat(`, no `radical`, no `primdec`, and no `LIB`. The eight `std(ideal(…))` constructions and twenty-nine `reduce` calls run in this ordinary polynomial ring. Localization is the Rabinowitsch adjunction `ik60*k60-1` and its siblings, not a quotient-ring assignment.

Coefficient extraction uses exact division `SourcePhi/sigma^25` together with the identity `sigma^25*Q-SourcePhi==0`, then `subst(Q,sigma,0)`. Taylor coefficients of the analytic series use `diff` in `t` followed by `subst(t,0)` divided by `n!`. Root evaluation uses `subst` of the ordinary polynomials `N2` and the Faber combinations. Raw `==0`, `subst`, and `diff` therefore run on canonically represented polynomials, not on Singular 4.3.2 quotient-ring assignments. Membership `reduce(1,I)==0` is the ordinary-ring test that `1` lies in `I`.

---

## 4. Independent polar census through grade 26

The frozen square source is `f=K^2+σ^5 D` with `K=L^2+σ^2 R` and `D=LA+C`. Factoring `f=L^4(1+x)` gives the four atoms

```text
x = 2 σ^2 R/L^2 + σ^4 R^2/L^4 + σ^5 A/L^3 + σ^5 C/L^4
```

of `σ`-costs `(2,4,5,5)` and denominators `(2,4,3,4)`, with scalars `(2,1,1,1)`. The four binomial summands are

```text
f^{3/2},   σ^4 k10 f^{5/4},   σ^{12} k6 f^{3/4},   σ^{20} k2 f^{1/4},
```

i.e. alphas `3/2, 5/4, 3/4, 1/4`. Pole order is `denominator-4α`. The unit-load chart names `k10` as `k0` and `k6` as `k60+σ k60_1`. At the boundary `(8,8,7)` the atom costs are `(9,18,13,13)`, all at least 9.

Independent expansion through grade `T=26`, with atom bounds `budget // cost` and with one and two extra counts in every atom direction, produces identical retained polar signatures. Every positive atom cost is at least 9, so a count exceeding `budget // cost` already overshoots the ceiling by itself. There is no cutoff hole. No cancelled key appears at this contact through grade 26.

The nonzero polar inventory is exactly the claimed list:

| Family | Summand | Coefficient | Pole | First grade |
|---|---|---|---:|---:|
| `k6*C` | `k6` | `3/4` | 1 | 25 |
| `AC` | unloaded | `3/4` | 1 | 26 |
| `C^2` | unloaded | `3/8` | 2 | 26 |
| `RC` | `k10` | `5/8` | 1 | 26 |

Coefficients reconstruct from binomials. Loaded `k6*C` is `binom(3/4,1)=3/4`, grade `12+5+8=25`. Unloaded `AC` is `binom(3/2,2)·2=3/4`, grade `5+5+8+8=26`. Unloaded `C^2` is `binom(3/2,2)=3/8`, grade `10+16=26`. Loaded `RC` is `binom(5/4,2)·2·2=5/8`, grade `4+2+5+7+8=26`. The unique pole-two family is `C^2`.

The first polar `k2` monomial is `k2*R` at grade `21+c=29`, coefficient `1/2`. Bare `k2` is ordinary (pole `-1`) at weight 20. Ordinary families through grade 26 include `k6*A` (pole 0, grade 25) and unloaded `A^2` (pole 0, grade 26). Specialized exact evaluation of all seven frozen `SourcePhi` rows at `(k60,a1)=(1,1)` with every other load/jet/contact coefficient zero yields the zero polynomial through grade 30; likewise bare `k20=1`. Those ordinary families do not enter the polar rows. Specialized evaluation at `(k20,b1)=(1,1)` first appears at grade 29 with row-1 coefficient `1/2`, matching the census.

Targets are the explicit subtractions `σ^{28} μ2`, `σ^{32} μ4`, `σ^{36} μ6`, `σ^{38}(J/4)` on rows 2,4,6,7, i.e. the frozen `2(12+row)` timing. They begin after grade 26. The compiled check `reduce(FullPhi-SourcePhi, (σ^{27}))==0` is slightly loose (it would allow a hypothetical grade-27 target) but the actual target monomials sit at 28 and later, and the four `FullPhi` tails contain exactly those four displayed powers.

Jet ceilings are mechanical from the grade-25 family `k6*C`. The substitutions retained through grade 26 are `k6=k60+σ k60_1`, `C=σ^8(C_0+σ C_1)`, and `p(σ)=p+2σ ell1`. Next-`A`, next-`R`, `k60_2`, and `ell2` first affect polar source at grade 27. `AC`, `C^2`, and `RC` themselves first appear at grade 26, so their own next jets are at 27 or later. The compiled numerator sentinels `diff(N2, k60_1)`, `diff(N2, cc1)`, `diff(N2, cc0)`, `diff(N2, ell1)` are therefore the complete in-window jet list; all four are nonzero.

---

## 5. Grade-25 source, complete `N2`, bridges, targets

The analytic generating function is the universal polar `hshift` of unloaded plus `k10`, plus the first `k6*C` family, with moving modulus `sp=p/2+σ ell1` in the inverse series `Inv1=1/(1+sp t^2)` and `Inv2=1/(1+sp t^2)^2` truncated through `t^8`:

```text
H = (3/4) σ^{10} t A C Inv1
  + (3/8) σ^{10} t^3 C^2 Inv2
  + (5/8) σ^{11} t k0 R C Inv1
  + (3/4) σ^{17} t^2 (k60+σ k60_1) C Inv1
  + (terms of grade >=30 at this contact).
```

Independent expansion through `(σ,t)=(26,8)` gives Taylor coefficients `h25_i=[t^{i+1}]H_{25}` and `h26_i=[t^{i+1}]H_{26}`. The grade-25 row is exactly

```text
h25_1 = (3/4) k60 c1,   h25_2 = (3/4) k60 c0,
```

with the pole-one recurrences `h25_{i+2}+(p/2) h25_i=0` for `i=1..5`. Thus

```text
N1 = h25_1 z + h25_2 = (3/4) k60 C.
```

The cubic representative

```text
N2 = h26_1 z^3 + h26_2 z^2 + (h26_3 + p h26_1) z + (h26_4 + p h26_2)
```

satisfies `N2 ≡ N2Expected (mod L^2)` identically, where `N2Expected` is the displayed five-summand numerator, together with the pole-two recurrences `h26_{i+4}+p h26_{i+2}+(p^2/4) h26_i=0` for `i=1,2,3`. The six unreduced degree-four monomials in `AC L` and `RC L` are exactly the content of `L^2`. Differentiating the cubic gives

```text
∂N2/∂ell1 + (3/4) k60 C = 0,
```

so the moving-connection coefficient is `-3/4` with that sign. Omitting the connection (comparing `N2` to `N2Expected+(3/4)ell1 k60 C`) leaves a nonzero remainder modulo `L^2`. All four jet derivatives of `N2` are nonzero.

The sign of the connection is the first correction of `1/L` along `L=L_0+σ ell1`:

```text
1/L = L_0^{-1} - σ ell1 L_0^{-2} + ⋯,
```

so the grade-26 correction of `(3/4)k60 C/L` is `-(3/4)ell1 k60 C/L^2`, numerator `-(3/4)ell1 k60 C`. Equivalently, `p(σ)=p+2σ ell1` is the unique lift of that `L`-jet through `L=z^2+p/2`.

The frozen seven-row tails, after the coefficient substitution of exact orders `A ↦ σ^8(a1 z+a0)`, `C ↦ σ^8((c1 z+c0)+σ(cc1 z+cc0))`, `R ↦ σ^7(b1 z+b0)` and `p ↦ p+2σ ell1`, are the literal `SourcePhi` rows. The offset-zero Faber transform `T^{(0)}` of the CGE3 dictionary is unitriangular in the even-step basis, with `g_i = h_i` on rows 1 and 2. Exact univariate evaluation of all seven frozen `SourcePhi` polynomials at `p=2`, with `(k60,c1)=(1,0-rest)` and separately `(k60,c0)=(1,0-rest)`, reproduces the predicted `T^{(0)}(h25)` coefficient vectors

```text
c1-chart:  (3/4, 0, -3/8, 0, -3/32, 0, -3/64),
c0-chart:  (0, 3/4, 0, 0, 0, 0, 0)
```

at grade 25 and no earlier polar term. The same extraction shows `k60_1 C` and `k60 Cnext` entering at grade 26 with the same row-1 coefficient `3/4`, the connection entering as an extra grade-26 column once `ell1=1`, `C^2` entering at grade 26 with row-2 coefficient `3/8`, and `AC`,`RC` entering at grade 26 and not before. The analytic/literal bridge at both grades is the CGE3 transform including the offset-one mixing `T^{(1)}(h25)` into `g26`; that mixing is proportional to `ell1 k60 C` and is the source of the unconditional moving-root gap in §7.

---

## 6. `D(k60)` unit ideals

On `D(k60)` the grade-25 equations are the seven Faber rows of `(3/4)k60 C/L`. Because `g25_1=h25_1=(3/4)k60 c1` and `g25_2=h25_2=(3/4)k60 c0`, the seven-row ideal contains both of those linear forms. In characteristic zero, `3/4` is a unit.

- Chart `D(c1)`. The compiled ideal is
  ```text
  (g25_1,…,g25_7,  ik60·k60-1,  ic1·c1-1,  ip·p-1,  ik0·k0-1).
  ```
  The inverses introduced are `k60^{-1}`, `c1^{-1}`, and the ambient `p^{-1}`, `k0^{-1}`. Then `(4/3) ik60 ic1 · g25_1 = 1`. The ideal contains `1` before radicals.
- Chart `V(c1) ∩ D(c0)`. The compiled ideal is
  ```text
  (g25_1,…,g25_7,  c1,  ik60·k60-1,  ic0·c0-1,  ip·p-1,  ik0·k0-1).
  ```
  The inverses introduced are `k60^{-1}`, `c0^{-1}`, and the ambient `p^{-1}`, `k0^{-1}`. Then `(4/3) ik60 ic0 · g25_2 = 1`. The ideal contains `1` before radicals.

The two charts cover exact nonzero linear `C`. Neither chart inverts `a1`, `a0`, `b1`, or `b0`. Inverting `p` and `k0` on this branch is the ambient gate `D(p*k0)`, not an extra load inverse: grade 25 does not use `k0` or a leading `A`/`R` coefficient. Extra generators among `g25_3,…,g25_7` can only enlarge the ideal.

---

## 7. `V(k60)`, etale pair, descent, moving-root gap

Adjoin `k60=0`. Every numerator term proportional to `k60` vanishes, including `(3/4)k60 Cnext L` and `-(3/4)ell1 k60 C`. What remains is

```text
N2|_{k60=0} = (3/4) A C L + (3/8) C^2 + (5/8) k0 R C L + (3/4) k60_1 C L.
```

The free `k60_1 C/L` term is pole one: after clearing, it still carries a factor `L`, so it vanishes at both roots of `L`. On the finite etale cover `λ^2=-p/2` one has `L(±λ)=0`, and the only surviving terminals are

```text
N2(z=λ)  = (3/8)(λ c1 + c0)^2,
N2(z=-λ) = (3/8)(-λ c1 + c0)^2.
```

The compiled Faber combinations `PsiPlus`, `PsiMinus` equal these terminals after `k60=0` (the offset-zero transform of `h26`), which is the repaired `ROOT_FABER` assertion. Before the split, `Psi-N` is nonzero: the offset-one mixing `T^{(1)}(h25)` contributes a multiple of the grade-25 `k60 C` column, and `N2` itself retains `-(3/4)ell1 k60 C` at the frozen root. Independent evaluation of `N2` at the roots with `k60` free leaves a two-term gap against the pure squares; after `k60=0` the gap is identically zero.

On `D(c1) ∩ D(λ) ∩ D(k0) ∩ V(k60)` the two squares `u^2=(λ c1+c0)^2` and `v^2=(-λ c1+c0)^2` satisfy `u-v=2λ c1`, a unit. Then `v^2-u^2=-2λ c1(u+v)` produces `u` after using `u^2`, hence produces `1`, before radicals. On `V(c1) ∩ D(c0) ∩ D(λ) ∩ D(k0) ∩ V(k60)` both terminals collapse to `(3/8)c0^2`, a unit. The compiled ideals are

```text
(k60, PsiPlus, PsiMinus, ic1·c1-1, ilam·λ-1, ik0·k0-1),
(k60, c1, PsiPlus, PsiMinus, ic0·c0-1, ilam·λ-1, ik0·k0-1).
```

The inverses introduced on this branch are `λ^{-1}`, `c1^{-1}` or `c0^{-1}`, and ambient `k0^{-1}`. No leading `A` or `R` coefficient is inverted. Inverting `λ` in place of `p` is the cover coordinate: `p=-2λ^2` is a unit on `D(λ)`.

Descent: the map `D(λ) → D(p)`, `p=-2λ^2`, is finite etale of degree two (`d(p)/dλ=-4λ ≠ 0` on `D(λ)`, and `λ=0` is `p=0`, already excluded). Every geometric point of `D(p)` lifts. If the pulled-back seven-row ideal contains `1` on the cover, the cover of the putative point-set is empty, so the base is empty. Faithful flatness of a finite etale cover gives the same conclusion scheme-theoretically. The two root combinations lie in the seven-row ideal, so unit-ness of those combinations is sufficient.

Omitting `C^2` from the numerator makes both root evaluations identically zero after `k60=0`, because every remaining summand carries a factor `L`.

---

## 8. Frozen V2 failure and controls

V2 is three distinct registered executions of a different frozen archive `d860cd90…` (`/tmp/jc2_d1_c2_c8_connection_v2_20260826.tgz`) on the same three hosts, tags `…_v2_20260826T2142Z`, engine `rc` 0, zero swap, empty compiler stderr. Mathematical stdout is byte-identical across the three characteristics. The fail-closed validator rejected the endpoint as `FAIL_MISSING_OR_NONUNIQUE:C2C8_ROOT_FABER=1`. The printed line is `C2C8_ROOT_FABER=0`, followed by `C2C8_FAIL=SOURCE_CONNECTION_OR_CHART`. Every other listed V2 marker is `1`, including `G25_K60_C_EXACT`, `CONNECTION_MINUS3_OVER4`, both chart-unit flags, `V_K60_ROOT_SQUARES`, and `OMIT_C2_ROOTS_ZERO`.

The V2 compiled predicate is the unconditional equality `PsiPlus=NPlus` and `PsiMinus=NMinus` *before* adjoining `k60=0`. That is exactly the over-strong pre-split fixed-root bridge described by `RESULT_V2_FAILED.md`. V3 differs from V2, in the compiled programs, only by inserting the gap polynomials, requiring `RootGap ≠ 0` unconditionally, and moving `ROOT_FABER` onto the substitutions `subst(Psi,k60,0)` and `subst(N,k60,0)`. No other identity is weakened, deleted, or redirected. That is a logical-placement repair, not a hidden mathematical failure. V2 remains no-verdict; its evidence tree is pinned and is not used for the cell.

The two negative controls hold independently of PASS strings: deleting the moving-connection term leaves a nonzero remainder of `N2` modulo `L^2`, and deleting `C^2` kills both root terminals after `k60=0`.

---

## 9. Closed tail `ord(A)>=8`, `ord(R)>=7`

Every polar monomial's grade is `fixed_σ + (c-1)·e_R + c·e_A + c·e_C` at exact contact, and strictly larger as soon as a contact with positive exponent is raised. Families with `e_A=e_R=0` are `k6*C` (grade 25) and `C^2` (grade 26); they persist under raising `A` or `R`. Families with `e_A>0` or `e_R>0` (`AC`, `RC`, and every later polar including `k2*R` at 29) are delayed. No census key has a negative `A` or `R` exponent, so raising cannot create a new lower-grade primitive family. The in-window pole ceiling remains 2, from persistent `C^2`. Targets are contact-independent at grades 28, 32, 36, 38 and cannot advance through 26. The `D(k60)` unit ideals use only `k60 C`, independent of `A` and `R`. The `V(k60)` root terminals use only `C^2`, independent of `A` and `R`. Specializing `a1=a0=0` or `b1=b0=0` (the jet-level shadow of a higher contact) preserves a unit ideal.

The four localized unit ideals therefore establish scheme-theoretic emptiness of exactly

```text
D(p*k0),  ord(C)=8,  ord(A)>=8,  ord(R)>=7
```

after the frozen generic-square and D1 unit-load source gates, on the exact nonzero linear `C` cover. They do not empty the zero section `c1=c0=0`.

---

## Firewall

This confirmation is a narrow cell. It does not extrapolate to `c>=9` (further connection and load jets enter), another primary or tied face, a positive-order leading load, `p=0`, `k0=0`, the exact-square zero section, a terminal or global chart, fan exhaustiveness, order two, maximum twelve, or JC2. It is not composed with the promoted target-free `3<=c<=7` theorem, nor with any other D1 statement.

**CONFIRMED**
