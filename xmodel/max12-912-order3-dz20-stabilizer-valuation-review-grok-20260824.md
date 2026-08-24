# Hostile different-model review — `(9,12)` order-three DZ20 stabilizer/valuation exclusion

| Field | Value |
|---|---|
| Claim under review | Frozen producer: conditional on the coprime spectral input `deg_z(g^3-f^4)=16`, the nontrivial order-three Kummer branch with `k=mu=nu=0` has no rational trajectory. Source stabilizers `e in {1,2,4}` are classified, the scaling parameter is descended, and the terminal ODE plus divisor congruences force `h` to be a cube |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking: the order-three fibre compiler has no completed different-model review; the spectral degree `16` used here is re-derived from the reviewed Faber landing, the order-three character filter, `k=0`, and the elementary tail identity, and is not imported as a fibre theorem. The fibre’s Kuranishi/component analysis is not consumed) |
| Evidence tier | independent hand derivations of the tail identity, coprimality from a `z`-constant Jacobian, the Wronskian/passport/Riemann–Hurwitz ledger, Hurwitz finiteness of three-point covers (no unitree list), affine normalization, coefficient-exponent gcd in every tested support shape, exact Kummer covariance `sigma(eta)=zeta^(-e) eta`, the stabilizer table, and both local and infinity Laurent balances through the first post-cancellation term on the descent-constrained branches; unmodified registered replay as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Charged ancestor | `1144839652c6a4750b9b0cd43e21d80cc9a755eb` (matches the launch prompt) |
| Git HEAD at close | `a04affb7247fb5e87cad4e87f5926ab440254b24` (descendant; mid-session commit `Promote max12 preflight and corrected carry audit` names this case; producer hashes below are unchanged) |
| Review window (UTC) | 2026-08-24T18:56:59Z – 2026-08-24T19:25:00Z |
| Python | CPython 3.14.6, stdlib only (registered replay and independent reconstruction) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, case, named predecessors, and the Pinchuk/Pakovich–Zvonkin scope warning reread in full before any verdict:

- `xmodel/max12-912-order3-dz20-stabilizer-valuation-20260824.md`
- `cases/max12_912_order3_dz20_stabilizer_valuation_20260824/{REGISTRATION.md,README.md,replay.py,replay.json,MANIFEST.sha256,FREEZE.txt}`
- `xmodel/max12-partial-y-kummer-preflight-20260824.md` and `xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md`
- `xmodel/max12-partial-y-shared-faber-probe-20260824.md` and `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md`
- `cases/max12_912_order3_fibre_20260824/order3_fibre.py` (fibre compiler; no completed fibre review exists in-tree)
- `xmodel/pinchuk-quasipolynomial-reduction-source-audit-grok-20260824.md` (scope warning only)

The charged ancestor named by the prompt is `1144839652c6a4750b9b0cd43e21d80cc9a755eb`. Named producer artifacts are newer than that ancestor. No producer, case, canonical, ladder, coordination, prompt, log, run, or erratum file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp`.

Pakovich–Zvonkin unitrees are not a complete list of equality pairs. That overread is not used. Finiteness is taken from transitive permutation triples of a fixed three-point passport, after the unique index-20 point and depression have cut source `PGL2` down to scaling.

---

## Promotion

**Accept `CONDITIONAL ON THE COPRIME SPECTRAL INPUT deg_z(g^3-f^4)=16, THE NONTRIVIAL ORDER-THREE KUMMER BRANCH WITH k=mu=nu=0 HAS NO RATIONAL TRAJECTORY. THE ARGUMENT IS STABILIZER-AWARE AND INDEPENDENT OF TAYLOR ENUMERATION` at the stated scopes.**

- On the order-three leaf the character filter and the three legal target gauges leave only the Faber constant `k`. At `k=mu=nu=0` one has `H(T)=T^{12}` and `T=r8 w^{-8}+...` with `r8≠0` forced by `9 r8'=j/u`. The tail identity then gives `deg_z(g^3-f^4)=16` exactly. A nonzero `z`-constant differential Jacobian forces `gcd(f,g)=1` in `L[z]`.
- `B=3 g_z f-4 g f_z` is a nonzero element of `L`. Every zero of `f` and of `g` is simple, `W` has sixteen distinct simple finite roots, all unramified over `1`, and infinity is the unique index-20 point. The passport is `3^{12}`, `4^9`, `(20,1^{16})`, and Riemann–Hurwitz is exact.
- Over `C` there are finitely many source-`PGL2` orbits of this passport, by finiteness of Hurwitz triples in `S_{36}`. Over `C(x)` the family of three-point covers is isotrivial. Factorization of `beta` recovers the monic pair uniquely. Residual source ambiguity after fixing the index-20 point and depressing is a cyclic scaling group of order `e|gcd(36,20)`, hence `e in {1,2,4}`.
- `eta=lambda^e` lies in `L`. Galois covariance is `sigma(eta)=zeta^{-e} eta` exactly. The eigenspace decomposition `eta=u^a v` with `a=-e mod 3` produces the table `(e,N,a,S)=(1,20,2,14),(2,10,1,4),(4,5,2,4)` and `R=C h^{-S} v^{-N}`.
- Every finite zero of `h` uses the noncancelled balance `r=1-m` and satisfies `m=3 mod N`. The residue `m=3` is integral for all three `e` and is killed only after cancellation: the order-zero coefficient vanishes and every surviving term has order at least `1`. No cancelled branch (`9r+6m=0`) survives. `v` has no divisor where `h` is regular.
- Summing orders and expanding at infinity forces `s=1`. Then `3|D` and algebraically closed constants make `h` a cube, contradicting exact Kummer order three.

**Do not promote this to:** a common-factor/noncoprime spectral stratum; any nonzero `k`, `mu`, or `nu`; the order-one polynomial core; emptiness of all `(9,12)`; maximum-twelve automorphy; a counterexample; or JC2.

**Smallest valid successor.** A separate gate for nonzero invariant loads, and a separate gate for the common-factor/noncoprime spectral stratum. Do not open a generic coefficient rectangle or AWS. Do not treat a unitree census as a `C(x)` classification.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a characteristic-zero Keller pair of type `(9,12)`, empties the loaded fibres, empties the common-cubic locus, or closes maximum twelve. Producer replay output was not used as evidence; the tail identity, Wronskian, Hurwitz finiteness, stabilizer orders, Kummer covariance, local Laurent series, and infinity coefficient were re-derived. The reviewed preflight is consumed only for the order-three leaf, `delta=0`, depression `z=uy+A/9`, covariance `sigma(z)=zeta z`, history residue `3|deg h`, and charged Taylor boundaries (which are retained and unused). The reviewed Faber theorem is consumed only for the high-row landing, the three gauges `(h_9,h_0,h_3)`, and `9 r8'=j/u`. The fibre compiler is not a reviewed theorem; only the `k=mu=nu=0` spectral degree, re-derived below, is used. Pakovich–Zvonkin 2014 is not an input.

---

## Scope (not enlarged)

Emptiness of the coprime `k=mu=nu=0` nontrivial order-three trajectory, conditional on `deg_z W=16`. Common-factor strata, nonzero loads, the order-one core, `(8,12)`, all `(9,12)`, maximum-twelve coverage, a counterexample, and JC2 remain out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | At `k=mu=nu=0` on the order-three leaf, `H=w^{12}` and nonzero terminal `r8` give `deg_z(g^3-f^4)=16`. A nonzero `z`-constant Jacobian forces `gcd(f,g)=1`. The registered claim is not conditional on a hidden extra hypothesis | **CONFIRMED** | a surviving Faber constant of weight `0` other than `k`; `r8=0` compatible with `j≠0`; leading tail cancellation from `T^2` or `T^3`; a common factor not dividing `D`; an unstated dependence on Taylor boundaries or on a fibre component classification |
| 2 | `B` is a nonzero `z`-constant; zeros of `f` and `g` are simple; `W` has sixteen simple finite roots, all unramified over `1`; infinity is the unique index-20 point; passport `(3^{12},4^9,(20,1^{16}))` and Riemann–Hurwitz `70=70`. No repeated-root or cancellation counterexample | **CONFIRMED** | `deg B≥1` with `deg W=16`; a multiple root of `f`, `g`, or `W`; a second index-20 point; an unrecorded branch value; a coprime monic depressed pair of degrees `(9,12)` with `deg W=16` and a repeated root |
| 3 | Finiteness of transitive Hurwitz triples of this passport, without a Pakovich–Zvonkin list, gives finitely many constant source-`PGL2` orbits. Over `C(x)` the pair is isotrivial. Factorization of `beta` recovers the monic `(f,g)` uniquely. Twists are exactly the residual scalings | **CONFIRMED** | a positive-dimensional Hurwitz component; a non-isotrivial three-point family; a second monic pair with the same `beta`; a descent obstruction that is not a scaling; a unitree list used as a complete classification of equality pairs |
| 4 | The unique index-20 point fixes infinity; depression kills translation in characteristic zero; residual ambiguity is `mu_e` with `e|gcd(36,20)`, so `e in {1,2,4}`. No wild/nonfaithful extra action, no extra target roots of unity, no scalar `(f,g)` freedom past monicity | **CONFIRMED** | a translation preserving both depressed polynomials; a non-cyclic finite scaling group; `e` not dividing `20` or `36`; a Möbius swapping `0` and `∞`; a monicity-compatible root-of-unity rescaling of `(f,g)` preserving `beta` |
| 5 | `eta=lambda^e in L` by the coefficient-exponent gcd, including sparse and symmetric templates and vanishing nonleading coefficients. `sigma(eta)=zeta^{-e} eta` exactly, not up to an uncontrolled constant | **CONFIRMED** | a support gcd strictly larger than the true stabilizer on a pair of this passport; Bezout producing only `c eta` with `c` not in `C`; an extension of `sigma` changing `sigma(eta)` by a non-root-of-unity constant |
| 6 | Table `(e,N,a,S)=(1,20,2,14),(2,10,1,4),(4,5,2,4)` and `R=C h^{-S} v^{-N}` from `[z^{16}]W ∝ lambda^{-20}` and `r8=u^2 R`. Signs, powers, eigenspaces, and constants reconstruct | **CONFIRMED** | `a N+2` not divisible by `3`; a second eigenspace for `eta`; leading power of `W` other than `lambda^{-20}`; `r8` of weight other than `2` |
| 7 | Noncancelled balance `r=1-m` forces `m=3 mod N`; `m=3` is integral for all three `e` and dies after cancellation; no cancelled branch survives; `v` has no divisor where `h` is regular. Explicit Laurent series through the first post-cancellation term | **CONFIRMED** | a second residue class; `m=3` producing a nonzero constant term; a cancelled series whose first surviving order is `≤0`; a regular place with `ord(R)=1` |
| 8 | `sum ord_p(R)=s-D`, `ord_∞(R)=D-s`, top coefficient `3(3s-D)≠0` because `D>3s`, hence `s=1`; `3|D` and `C` algebraically closed make `h` a cube. All three stabilizers and the terminal positive control independently confirm | **CONFIRMED** | opposite sum-of-orders sign; vanishing of `3(3s-D)` on `D>3s`; `s=1` with `h` not a cube in `C(x)`; the control `(h,R)=(x^2(x-1)^4, C/(x(x-1)^3))` failing the ODE or satisfying some stabilizer congruence |
| 9 | Strongest licensed conclusion is emptiness of this one fibre. Not common-factor strata, not nonzero loads, not the order-one core, not all `(9,12)`, not maximum twelve, not a counterexample, not JC2 | **CONFIRMED** | a hidden promotion in the report, registration, or replay payload |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Hashes and replay (regression only)

Recomputed SHA-256 on the working-tree bytes match the launch prompt, `MANIFEST.sha256`, and `FREEZE.txt`:

| Artifact | SHA-256 | Cross-check |
|---|---|---|
| `xmodel/max12-912-order3-dz20-stabilizer-valuation-20260824.md` | `4a5ec8b08aab7a9ba5d7c22593efeb67621fea720128dd7051972f52cc9191e5` | prompt, `MANIFEST`, `FREEZE` |
| `cases/…/REGISTRATION.md` | `801295a8f622fe711527613c942166c9f1e768b24aeea2485b85de92bc66e476` | prompt, `MANIFEST`, `FREEZE` |
| `cases/…/README.md` | `7d0faaf0ec6427e1585e54ed807f62d96288603b68d1c2618325c234f099be28` | prompt, `MANIFEST`, `FREEZE` |
| `cases/…/replay.py` | `da97811fe6292c7de7caabbbb8a9159e00b3dfd9b551155607d904b35dfa6173` | prompt, `MANIFEST`, `FREEZE` |
| `cases/…/replay.json` | `bc11592d197be05d5360f0294b2f111e8382558d071291af4810856a8d75dca6` | prompt, `MANIFEST`, `FREEZE` |
| `cases/…/MANIFEST.sha256` | `78719e904cac78806752b4d8b895b9a319e9422d5803aff468075607bcdd3695` | prompt, `FREEZE` |
| `cases/…/FREEZE.txt` | `f1ee7e72a0e7a097141a95fbb888103b3456619316c4bf903e668f666b40082a` | prompt only |

Predecessor hashes recomputed, not used as mathematical evidence:

| Artifact | SHA-256 |
|---|---|
| `xmodel/max12-partial-y-kummer-preflight-20260824.md` | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` |
| `xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md` | `2951856cabe309fe07f564693a6b48a38cd7108616ffe41305d9583611da90fe` |
| `xmodel/max12-partial-y-shared-faber-probe-20260824.md` | `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036` |
| `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md` | `e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c` |
| `xmodel/pinchuk-quasipolynomial-reduction-source-audit-grok-20260824.md` | `bbc8c1df4993301babed4fff5717f89bcae7fd849448e1c221884ab345ca9774` |

`python3 cases/max12_912_order3_dz20_stabilizer_valuation_20260824/replay.py | diff -u cases/max12_912_order3_dz20_stabilizer_valuation_20260824/replay.json -` exits `0`. The replay checks integer congruences, the `m=3` leading coefficient, sample cancelled balances, the regular-point obstruction `1` not divisible by `N`, the infinity coefficient formula, and the terminal positive control. It does not prove isotriviality, does not expand a Laurent series, and does not construct a Belyi map. It is regression only.

The case directory contains exactly the six freeze/manifest/readme/registration/replay files. No enumerator or AWS helper is present.

---

## Claim 1 — spectral input and coprimality

**CONFIRMED.**

The reviewed Faber theorem supplies, over the Kummer root field `L=C(x)(u)`, a unique expansion `g=sum_{j=0}^{12} h_j F_j` with all `h_j` differential constants, and the remaining system `r_1'=⋯=r_7'=0`, `9 r_8'=j/u`. The three legal gauges on `(9,12)` kill `h_9`, `h_0`, and `h_3`. On the order-three leaf, constants must have weight `0 mod 3`, so the only surviving Faber constant is `h_6=k`. At `k=0` one has `H(T)=T^{12}` and `g=[w^{12}]_+`.

The constants `r_1,…,r_7` have weights `ℓ mod 3`. Weight-nonzero constants of `L` vanish because the constant field is `C`. Thus `r_1=r_2=r_4=r_5=r_7=0` automatically, and `r_3=mu`, `r_6=nu` are the only possible nonzero constants. The specialization `mu=nu=0` is exactly the named fibre.

Terminal nonvanishing: `9 r_8'=j/u≠0`, so `r_8` is nonconstant, hence nonzero. Independently, `r_8` has weight `8≡2 mod 3` (also visible from `wt(j/u)≡-1≡2`), so `r_8=u^2 R` with `R in K=C(x)`. Differentiating with `3 u^2 u'=h'` yields

```text
r8' = (2/3)(h'/u) R + u^2 R',
9 r8' = 6 (h'/u) R + 9 u^2 R' = j/u,
9 h R' + 6 h' R = j.
```

The sign is the Faber plus sign on the tail, already confirmed in the Faber review.

Elementary tail identity, independent of the fibre compiler: `f=w^9`, `g=w^{12}-T`, so

```text
W = g^3 - f^4 = -3 w^{24} T + 3 w^{12} T^2 - T^3.
```

With `T=r8 w^{-8}+r9 w^{-9}+…` the leading term is `-3 r8 w^{16}`. The `T^2` contribution starts at `w^{-4}` and `T^3` at `w^{-24}`. Independent expansion with several `(r8,r9,r10)` confirms `deg_w W=16` and `[w^{16}]W=-3 r8`. Since `w=z+O(z^{-1})`, `deg_z W=16`.

Coprimality. Write `D=f_x g_z-f_z g_x`. Keller plus the chain rule gives `u D=j`, so `D=j/u` is a nonzero element of `L`, of `z`-degree `0`. If `d=gcd(f,g)` in `L[z]` has positive degree, the expansion

```text
f=d f1,  g=d g1
```

makes every term of `D` divisible by `d`. A nonunit `d` cannot divide a nonzero `z`-constant. Direct check on `(z-t)(z^2+1)` and `(z-t)(z^3+z+1)`: `D` vanishes at `z=t`. Thus `gcd(f,g)=1` on the whole Keller locus, not only on the spectral branch. The common-power family `f=K^3`, `g=K^4` has `W≡0` and `r8=0`, so it is already excluded by `j≠0`. The producer’s “coprime spectral branch” is therefore conservative, not an extra hidden hypothesis.

Conditionality. The registered sentence is conditional on `deg_z W=16`, the nontrivial order-three class, and `k=mu=nu=0`. Those are exactly the hypotheses used. Taylor boundaries are retained and unused. The fibre compiler’s Kuranishi ranks, quadrics, and discriminant lift are unused. The claim is not conditional on more than it says.

---

## Claim 2 — passport

**CONFIRMED.**

Let `W=g^3-f^4`, `beta=g^3/f^4`, `B=3 g_z f-4 g f_z`. Direct differentiation:

```text
beta_z = g^2 B / f^5.
```

Both `f` and `g` are monic of degrees `9,12` (and depressed: `delta=0` kills the `z^{11}` term of `g`). Hence `beta-1=W/f^4` has order `36-16=20` at infinity. The derivative of `c z^{-20}+…` has order `21`. On the other side, `g^2/f^5` has order `24-45=-21`. Comparing forces `deg_z B=0`. If `B=0` then `beta` is constant, so `W=0`, contradicting (1.1). Thus `B in L^*`.

Simple zeros of `f` and `g`. A multiple root of `g` kills both `g` and `g_z`, hence kills `B`. A multiple root of `f` kills `B` likewise. So every zero is simple.

Finite points over `1`. A root of `W` cannot be a root of `f` or `g` (coprime). The identity `W` divides `f W_z - g^2 B` holds as polynomials (checked by division on a mixed-degree sample, and by the substitution `g_z=(B+4 g f_z)/(3 f)` at `W=0`, which collapses `W_z` to `g^2 B/f`). Thus `W_z=0` at a root of `W` would force `B=0`. All sixteen finite roots of `W` are simple, and `beta_z=g^2 B/f^5≠0` there, so they are unramified over `1`.

Unique index-20 point. Source infinity is the unique pole of `z`. The expansion `beta-1 ~ c z^{-20}` gives ramification index `20` over `1`. Counting `16+20=36` accounts for the whole fibre of `beta`, so there is no second ramified point over `1`.

Passport and Riemann–Hurwitz:

```text
0:        3^{12}     (simple zeros of g, triple zeros of beta),
infinity: 4^9        (simple zeros of f, quadruple poles of beta),
1:        (20, 1^{16}).
12*(3-1)+9*(4-1)+(20-1)=24+27+19=70=2*36-2.
```

No unrecorded branch value.

Repeated-root / cancellation search. The identities above are polynomial and do not assume genericity. A coprime monic pair with `B` a nonzero constant cannot have a multiple root of `f`, `g`, or `W`. Generic monic pairs have `B` of positive degree (explicitly `z^{11}` and `z^8` terms for `f=z^9+2`, `g=z^{12}+3`). No counterexample was found, and the identities leave no room for one on this locus.

---

## Claim 3 — isotriviality without the classification overread

**CONFIRMED.**

A Belyi map of degree `36` with passport (2.2) is a transitive triple `(σ0,σ1,σ∞)` in `S_{36}` of cycle types `3^{12}`, `(20,1^{16})`, `4^9` with `σ0 σ1 σ∞=1`. The symmetric group is finite, so there are finitely many conjugacy classes. Riemann’s existence theorem realises each class by a cover `P^1→P^1` branched at `{0,1,∞}`, unique up to source Möbius transformation. This is Hurwitz finiteness of a three-point passport. It does not use Pakovich–Zvonkin, it does not claim that unitrees list all equality pairs, and it does not require the Hurwitz number to be positive: if the number is zero there is no complex pair and the fibre is empty a fortiori.

The source of `beta` is `P^1`, hence connected, so monodromy is transitive.

Over `L=C(x)(u)`, `beta in L(z)` is a family of such covers, branched at the three constant points `0,1,∞`. The Hurwitz space of a fixed passport is zero-dimensional. A family of three-point covers over a connected base is therefore isotrivial: after a source Möbius transformation defined over a finite extension of `L`, `beta` is a constant Belyi map. Specialisation at a generic `x0` with `h(x0)≠0` preserves degrees, coprimeness, and `deg W=16` (open conditions).

Factorization. Zeros of `beta` are the simple zeros of `g`, with multiplicity `3`. Poles are the simple zeros of `f`, with multiplicity `4`. The monic polynomials with those roots are uniquely `g` and `f`. Extra scalar freedom `(λ g, μ f)` with `λ^3=μ^4` would preserve `beta`, but monicity forces `λ=μ=1` by comparing leading coefficients. The prompt’s “common scaling” therefore dies at the monic normalisation. Recovery is unique, not merely up to an unidentified scalar.

Twists. After the unique index-20 point is placed at infinity (it is `L`-rational) and the coordinate is depressed, the residual source forms of a constant pair `(F,G)` are exactly the scalings (3.1). There is no further `PGL2`-twist: a Möbius swapping `0` and `∞` would move the unique index-20 point, and the labelled ramification types at `0,1,∞` are pairwise distinct, so no nontrivial target automorphism preserves the labelled branch points.

The producer never consults a unitree list. The Pinchuk-audit overread is not committed.

---

## Claim 4 — affine normalization and stabilizer

**CONFIRMED.**

The unique index-20 point is source infinity in the depressed coordinate. Source automorphisms preserving `beta` must fix that point, hence are affine: `z ↦ λ z + τ`.

Depression. For a monic degree-`9` polynomial, the coefficient of `z^8` in `F(z+τ)` is `9τ`. Characteristic zero forces `τ=0`. The same translation coefficient for `G` is `12τ`. Both vanishings are compatible. No special pair retains a nontrivial translation: `9τ=0` has only `τ=0`.

Residual group. Finite subgroups of `G_m=C^*` are cyclic, so the scaling stabilizer is `μ_e` for some `e`. A generic fibre of `beta` has `36` points. The action `z ↦ λ z` on `C^*` has orbits of size `e`, so `e|36`. Equivalently, `beta` becomes a rational function of `z^e` of degree `36/e`. The local expansion `beta-1=c z^{-20}+…` and `beta(λ z)=beta(z)` force `λ^{-20}=1`, so `e|20`. Thus

```text
e | gcd(36,20)=4,    e in {1,2,4}.
```

The deck action of a nontrivial scaling on a generic fibre is free: a nontrivial element of `μ_e` fixes only `0` and `∞`. Characteristic zero, so no wild ramification. The action is faithful by definition of `e` as the actual stabilizer order.

Scalar changes of `f,g` are killed by monicity, as in Claim 3. Extra target roots of unity would have to preserve the labelled set `{0,1,∞}` with three distinct ramification types, hence are trivial. A putative stabilizer `μ_8` coming from a sparse support such as `F=z^9+A_1 z` is incompatible with index `20`: a primitive eighth root satisfies `ω^{-20}=-1≠1`, so it cannot lie in the stabilizer of a pair with this passport. The gcd of appearing exponent differences on any pair that does occur is therefore `1`, `2`, or `4`.

---

## Claim 5 — descent parameter

**CONFIRMED.**

From (3.1),

```text
a_i = A_i λ^{i-9},     b_j = B_j λ^{j-12},
```

with `A_i,B_j in C`. The appearing exponents `k=9-i` and `k=12-j` for nonzero nonleading coefficients are all multiples of the stabilizer order `e`, and their gcd is exactly `e`: a strictly larger gcd would enlarge the scaling stabilizer. Independent support checks:

| template | support | gcd |
|---|---|---|
| generic | all admissible degrees | `1` |
| even / odd | `F` odd powers, `G` even powers | `2` |
| `e=4` | `F` powers `≡1 mod 4`, `G` powers `≡0 mod 4` | `4` |
| sparse | `{9,1}` and `{12,0}` | `4` |
| palindromic-looking mixed | `{9,5,0}` and `{12,7}` | `1` |
| monomial | `{9}` and `{12}` | empty, excluded by `r8≠0` |
| repeated equal exponents | `{4,4}` | `4` |

Vanishing of some nonleading coefficients only removes generators of the exponent lattice; the gcd on the remaining support is still the true `e`. Ratios of coefficients lie in `L`, constants `A_i/A_j` lie in `C subset L`, and a Bézout combination of the exponents produces `λ^{±e}` up to a factor in `C^*`. Hence `eta=λ^e in L`.

Kummer covariance. The preflight gives `wt(A)=1`, so `sigma(z)=zeta z` and `sigma(f)(z)=f(zeta^{-1} z)` (and likewise for `g`). Comparing (3.1) before and after `sigma`, two scalings define the same monic pair iff they differ by a stabilizer element `μ` with `μ^e=1`. Thus `sigma(λ)=zeta^{-1} λ μ`. Then

```text
sigma(eta)=sigma(λ)^e = zeta^{-e} λ^e μ^e = zeta^{-e} eta.
```

The factor `μ^e=1` kills any uncontrolled constant. This identity lives in `L` and does not depend on a choice of extension of `sigma` to `L(λ)`. Direct check for every `e in {1,2,4}` and every `μ in μ_e` in `C` confirms `sigma(λ)^e = zeta^{-e} eta` with no extra constant.

---

## Claim 6 — exact table

**CONFIRMED.**

`N=20/e`. The character `sigma(eta)=zeta^{-e} eta` and the eigenspace decomposition of the cyclic cubic `L/K` force `eta=u^a v` with `v in K^*` and `a=-e mod 3`:

```text
e=1 => a=2,     e=2 => a=1,     e=4 => a=2.
```

Leading coefficient of `W`: `W_{f,g}(z)=λ^{-36} W_{F,G}(λ z)`, and `W_{F,G}=C_F Z^{16}+…` with `C_F in C^*`, so

```text
[z^{16}] W = C_F λ^{-20} = C_F eta^{-N}.
```

The tail identity gives `[z^{16}]W=-3 r8`. Thus `r8=C eta^{-N}` with `C=-C_F/3 in C^*`. Combined with `r8=u^2 R`,

```text
R = C u^{-a N-2} v^{-N} = C h^{-S} v^{-N},     S=(a N+2)/3.
```

The three rows are `(1,20,2,14)`, `(2,10,1,4)`, `(4,5,2,4)`, and `a N+2` is divisible by `3` in each. Signs are absorbed into `C in C^*`. Valuations are independent of the choice of `C`. The naive form `R=C h^6 a^{20}` is not used; all three twists are retained.

---

## Claim 7 — finite valuations

**CONFIRMED.**

Let `m=ord_p(h)>0`, `r=ord_p(R)`, `n=ord_p(v)`, with uniformiser `t=x-p` and unit expansions `h=c t^m(1+α t+…)`, `R=d t^r(1+γ t+…)`. Then

```text
9 h R' + 6 h' R = c d t^{m+r-1} { (9r+6m) + t(6α+9γ + (9r+6m)(…)) + … }.
```

Noncancelled branch. If `9r+6m≠0` the order is `m+r-1`. Equality to the nonzero constant `j` forces `r=1-m`. Substituting `r=-S m-N n` gives `N n=-(S-1)m-1`, so `(S-1)m+1≡0 mod N`. The unique residue in `{0,…,N-1}` is `m=3` for each of `N=20,10,5`. Independently: `13m+1≡0 mod 20`, `3m+1≡0 mod 10`, `3m+1≡0 mod 5`.

The residue `m=3` is integral for all three stabilizers (`n=-2,-1,-2` respectively) and is not killed by the congruence. It is killed by the ODE. At `m=3`, `r=-2`, one has `9r+6m=0` and `m+r-1=0`: the constant term itself cancels. The next coefficient is `3(2α+3γ)`. Explicit series:

- pure monomials `h=c t^3`, `v` a pure power, on each descent `R=C h^{-S} v^{-N}`: the left-hand side vanishes identically (the case `R^9 h^6` constant, hence `j=0`);
- generic units: constant term `0`, first surviving order `1`;
- tuned `2α+3γ=0`: order `1` may vanish, order `2` is nonzero.

In every descent-constrained specialisation the surviving order is at least `m+r=1>0`, so the left-hand side cannot equal `j`.

Cancelled branch from the outset. `9r+6m=0` forces `r=-2m/3` and `3|m`. After cancellation the next possible order is at least `m+r=m/3`. For `m≥3` this is at least `1`. Independent series at `m=3,6,9,12` confirm a vanishing leading coefficient and a first surviving order equal to `m/3` on a generic unit, strictly larger when further coefficients vanish. The identically cancelled law `9 (log R)'+6 (log h)'=0` gives left-hand side zero, not `j`.

Therefore every finite zero of `h` uses the noncancelled balance with `m>3`. The first admissible multiplicities are `23,13,8` for `e=1,2,4`.

No hidden divisor of `v`. If `h(p)≠0` and `n=ord_p(v)≠0`, then `r=-N n` is a nonzero multiple of `N in {20,10,5}`. Here `ord(h R')=r-1` strictly, while `ord(h' R)≥r`, so there is no cancellation. Equality to a constant would require `r=1`, impossible. (If `h'(p)=0` as well, the inequality is stricter.) Linear `h` with unit `R` (`m=1`, `r=0`) is a locally possible noncancelled order-zero balance, and is excluded by the congruence: `m=1` is not `3 mod N`.

---

## Claim 8 — infinity and conclusion

**CONFIRMED.**

`R` is a rational function. Orders at places where `h` is regular vanish, so

```text
sum_{p|h} ord_p(R) = sum (1-m_p) = s-D,
ord_∞(R) = D-s.
```

The sum-of-orders sign is the standard one on `P^1`. At infinity, `h ~ c x^D` and `R ~ d x^{s-D}` with `d≠0`. The left-hand side has top degree `s-1` and top coefficient

```text
9(s-D)+6 D = 3(3s-D).
```

Every finite multiplicity is `>3`, so `D>3s` and the coefficient is nonzero. Equality to a degree-zero constant forces `s=1`. The reviewed history residue supplies `3|D`. A polynomial with a single finite root, of degree divisible by three, over an algebraically closed constant field, is a cube: `h=c(x-b)^D=(c^{1/3}(x-b)^{D/3})^3 in K^{*3}`, contradicting exact Kummer order three.

The argument after `m>3` is uniform in `e`. For `s=1` the pair is monomial in `X=x-b`,

```text
9 h R' + 6 h' R = 3 c d (3-D),
```

a genuine nonzero constant when `D>3`, which can match `j`; the only contradiction is that `h` is a cube. Vacuous `s=0` (constant `h`) is the trivial Kummer class, already excluded, and also gives left-hand side zero if `R` is constant.

Positive control, independently. For `h=x^2(x-1)^4` and `R=C/(x(x-1)^3)`, clearing the denominator of `9 h R'+6 h' R` produces the polynomial identity with right-hand side `-3 C den^2`, hence

```text
9 h R' + 6 h' R = -3 C.
```

The Kummer class of this `h` has order three (`2,4,-6`). Finite multiplicities `2,4` satisfy neither `m=3 mod N` nor `m>3`, for every `e in {1,2,4}`. Logarithmic differences `ord R-6 ord h` are `-13,-27,40` at `0,1,∞`. The ODE alone is therefore noncontradictory; the control is rejected only by the DZ/stabilizer descent. It does not revive a false terminal-valuation inference.

---

## Claim 9 — scope

**CONFIRMED.**

The report, registration, README, freeze, and replay payload all refuse the same promotions. The replay’s conclusion string says “conditional only on the passport and stabilizer-aware isotrivial descent”, which is the same condition as `deg_z W=16` plus coprimeness plus the descent proved in the report; it is not a silent enlargement. Taylor boundaries are explicitly unused. The common-cubic family is named and excluded by `r8'=0`. Nonzero `k,mu,nu`, the order-one core, `(8,12)`, all `(9,12)`, maximum-twelve automorphy, a counterexample, and JC2 are out of scope.

---

## Independent reconstruction (not the producer replay)

Scratch lived in `/tmp` and is not in the bank. It re-derived, without importing `replay.py` or `order3_fibre.py`:

- the tail identity `W=-3 w^{24} T+3 w^{12} T^2-T^3` and `deg=16` for several `(r8,r9,r10)`;
- divisibility of `D` by a common factor;
- the polynomial identity that `W` divides `f W_z-g^2 B`;
- Riemann–Hurwitz `70=70`, orders `-20` and `-21`, fibre count `16+20=36`;
- `gcd(36,20)=4` and the three stabilizer rows, including `a N+2=3S`;
- Kummer covariance for every `e` and every `μ in μ_e`;
- coefficient-exponent gcds on generic, even, `e=4`, sparse, mixed, and monomial templates, and `ω_8^{-20}=-1`;
- unique congruence residues `m=3`;
- Laurent series of `9 h R'+6 h' R` on descent-constrained branches: `m=3` for all three `e` (identically zero on pure monomials; order `≥1` otherwise), cancelled `m=6`, noncancelled `m=23` with leading coefficient `9r+6m=-60`, and a regular place of order `r-1=-21`;
- the infinity coefficient identity on several `(s,D)`;
- the positive-control polynomial identity and the failure of `m=2,4` at every `N`.

Ninety-four targeted identities passed; none failed.

---

## Non-blocking remarks

1. There is no completed different-model review of `cases/max12_912_order3_fibre_20260824/order3_fibre.py`. This review does not bank that compiler’s Kuranishi ranks, quadrics, or discriminant lift. The spectral degree `16` at `k=mu=nu=0` is re-derived from reviewed Faber+character inputs and the elementary tail identity.
2. The mid-session commit `a04affb` names this case. Charged hashes are unchanged from the launch table. The fibre compiler remains untracked. A concurrent untracked `cases/max12_912_order3_nu1_probe_20260824/` was not read.
3. `m=3` solves the integrality condition for every stabilizer. A reader who stops at the congruence table will miss the only argument that kills it, namely the post-cancellation Laurent series. The producer does supply that argument; the slogans “next order is `m+r`” and “next order is `m/3`” are lower bounds, and explicit first surviving coefficients can vanish, pushing the order higher but never back to `0` unless the left-hand side is identically zero.
4. The replay is an integer regression. Isotriviality, Bézout recovery of `eta`, and the Laurent series are not in the payload.

---

## Verdict

**Accept `CONDITIONAL ON THE COPRIME SPECTRAL INPUT deg_z(g^3-f^4)=16, THE NONTRIVIAL ORDER-THREE KUMMER BRANCH WITH k=mu=nu=0 HAS NO RATIONAL TRAJECTORY` at the stated scopes.**

Overall: **CONFIRMED**. Claims 1–9: **CONFIRMED**. Smallest failing identity: none. Smallest missing hypothesis: none that breaks a numbered claim.

Do not promote this to a common-factor stratum, a nonzero-load fibre, the order-one core, emptiness of `(9,12)`, maximum-twelve automorphy, a counterexample, or JC2.
