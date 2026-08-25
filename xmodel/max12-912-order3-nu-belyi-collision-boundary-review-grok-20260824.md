# Hostile different-model review — `(9,12)` order-three `nu!=0` full B/W absorption boundary

| Field | Value |
|---|---|
| Claim under review | Frozen producer: on the reviewed order-three `k=mu=0`, `nu!=0` landing, no actual Keller trajectory survives when the complete ramification divisor of the quadratic spectral Wronskian `B` is absorbed by `W=g^3-f^4=0`. This is exactly the two passports `(18,2,2,1^{14})` and `(18,3,1^{15})` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking: the order-three fibre compiler and the spectral Wronskian-ladder producer have no completed different-model review; neither is consumed. The quadratic `B` and the leading term `[z^{18}]W=-3 nu` are re-derived from the reviewed Faber form, the order-three character filter, and elementary tail calculus) |
| Evidence tier | independent hand derivations of the tail identity, the centered quadratic Wronskian, coprimality and squarefreeness from a `z`-constant Jacobian, the identity `f W_z-g^2 B=4 f_z W`, exact local multiplicities two and three, both Riemann–Hurwitz ledgers, Hurwitz finiteness of three-point covers (no unitree list), affine normalization, the scaling exponent `-18`, and the splitting of `X^{18}-c` in a function field over algebraically closed constants; unmodified registered replay as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (`Promote max12 DZ20 exclusion and source audits`). Named producer artifacts for this case are untracked on top of that HEAD; charged hashes below are unchanged |
| Review window (UTC) | 2026-08-24T20:08:00Z – 2026-08-24T20:26:00Z |
| Python | CPython 3.14.6, stdlib only (registered replay and independent reconstruction) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, case, named reviewed predecessors, and the charged coprimality firewall reread in full before any verdict:

- `xmodel/max12-912-order3-nu-belyi-collision-boundary-20260824.md`
- `cases/max12_912_order3_nu_belyi_collision_20260824/{REGISTRATION.md,README.md,replay.py,replay.json,MANIFEST.sha256,FREEZE.txt}`
- `xmodel/max12-partial-y-kummer-preflight-20260824.md` and `xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md`
- `xmodel/max12-partial-y-shared-faber-probe-20260824.md` and `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md`
- `xmodel/max12-912-order3-dz20-stabilizer-valuation-review-grok-20260824.md` (coprimality/squarefreeness firewall only)

No producer, case, canonical, ladder, coordination, prompt, log, run, or other review file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp`.

Pakovich–Zvonkin unitrees are not a complete list of equality pairs. That overread is not used. Finiteness is taken from transitive permutation triples of a fixed three-point passport, after the unique index-18 point and depression have cut source `PGL2` down to scaling.

---

## Promotion

**Accept `ON THE REVIEWED ORDER-THREE k=mu=0, nu!=0 LANDING, NO ACTUAL KELLER TRAJECTORY SURVIVES WHEN THE COMPLETE RAMIFICATION DIVISOR OF THE QUADRATIC SPECTRAL WRONSKIAN B IS ABSORBED BY W=0` at the stated scopes.**

- The reviewed Faber landing and the order-three character filter give `f=w^9`, `g=w^{12}-T`, `T=nu w^{-6}+r8 w^{-8}+...` with `nu in C*` and `9 r8'=j/u !=0`. The elementary tail identity then yields `deg_z W=18` and `[z^{18}]W=-3 nu`, with no hidden leading cancellation. The same tail calculus produces the centered quadratic `B=54 nu z^2+18 nu p+60 r8` of discriminant `-1296 nu(3 nu p+10 r8)`.
- A nonzero `z`-constant Jacobian `D=j/u` forces `gcd(f,g)=1` and squarefreeness of both factors. Consequently `B` cannot vanish at a root of `f` or of `g`.
- Full absorption has exactly two strata. Distinct simple roots of `B` in `W` give ramification indices exactly two over `1`, passport `(18,2,2,1^{14})`. A double root of `B` in `W` gives index exactly three, passport `(18,3,1^{15})`. In both cases every other finite root of `W` is simple, the three labelled ramification types are pairwise distinct, and Riemann–Hurwitz is sharp at `70=70`. There is no fourth branch value.
- Fixed-passport Hurwitz finiteness makes the three-point family isotrivial over `L`. The unique index-18 point and depression cut source identifications to scaling. Factorization of `beta` recovers the monic pair uniquely. Residual stabilizer twists preserve `lambda^{18}`.
- `[z^{18}]W=C18 lambda^{-18}=-3 nu` forces `lambda^{18} in C*`. Because `C` is algebraically closed and sits inside every finite extension of `L`, `X^{18}-c` splits into linear factors and `lambda in C*`. Every coefficient of `f,g`, and the Laurent tail `r8`, is therefore differential-constant, contradicting `9 r8'=j/u !=0`.

**Do not promote this to:** the generic quadratic-Wronskian fibre; a single `B`--`W` collision; a double root of `B` away from `W`; collision of the two non-`1` critical values; any Taylor boundary; the order-one core; all `(9,12)`; maximum-twelve automorphy; a counterexample; or JC2.

**Smallest valid successor.** Separate gates for (i) no `B` root in `W`, (ii) exactly one simple `B` root in `W`, (iii) a double `B` root off `W`, and (iv) equal non-`1` critical values. Do not open a generic coefficient rectangle or AWS. Do not treat a unitree census as a `C(x)` classification. Do not fold a four-point leftover into this three-point exclusion.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a characteristic-zero Keller pair of type `(9,12)`, empties the generic `nu`-loaded fibre, empties a one-root collision, or closes maximum twelve. Producer replay output was not used as evidence; the tail identity, the centered quadratic, the local multiplicities, Hurwitz finiteness, the scaling exponent, and the constant-field splitting were re-derived. The reviewed preflight is consumed only for the order-three leaf, `delta=0`, depression `z=uy+A/9`, and covariance `sigma(z)=zeta z`. The reviewed Faber theorem is consumed only for the high-row landing, the three gauges `(h_9,h_0,h_3)`, and `9 r8'=j/u`. The DZ20 review is consumed only for the already-confirmed coprimality/squarefreeness firewall, which is also re-derived below. Taylor boundaries remain charged and unused.

---

## Scope (not enlarged)

Emptiness of the two full-absorption passports `(18,2,2,1^{14})` and `(18,3,1^{15})` on the reviewed order-three `k=mu=0`, `nu!=0` landing. The generic quadratic fibre, one-root collision, double-`B` four-point family, equal non-`1` critical values, Taylor boundaries, the order-one core, all `(9,12)`, maximum-twelve coverage, a counterexample, and JC2 remain out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | On this leaf, `[z^{18}](g^3-f^4)=-3 nu` with no leading cancellation, and `B=54 nu z^2+18 nu p+60 r8` is the exact centered quadratic of discriminant `-1296 nu(3 nu p+10 r8)` | **CONFIRMED** | a surviving Faber constant of weight `0` other than `k`; a nonzero `r_l` for `l in {1,2,3,4,5,7}` compatible with the character filter; `T^2` or `T^3` reaching degree `18`; a linear term in `B`; `disc` other than `-4ac` |
| 2 | The actual Keller equation `D=j/u in L*` forces `gcd(f,g)=1` and squarefreeness of `f` and of `g`. Hence `B` cannot vanish at a root of `f` or of `g` | **CONFIRMED** | a common factor not dividing `D`; a square factor of `f` or `g` leaving `f_x` or `f_z` (resp. `g`) not divisible by `d`; a Keller Jacobian of positive `z`-degree |
| 3 | Distinct simple `B` roots in `W` give `beta-1` of multiplicity exactly two at each, passport `(18,2,2,1^{14})`. A double `B` root in `W` gives multiplicity exactly three, passport `(18,3,1^{15})`. No higher `W` multiplicity, and no `B` root at `f g=0` | **CONFIRMED** | `W_{zz}=0` at a simple `B` root in `W`; valuation of `W` other than `3` at a double `B` root in `W`; a `B` root on `f g=0` compatible with (2.1) |
| 4 | Both Riemann–Hurwitz ledgers equal `70`. Every other finite root of `W` is simple. The labelled types `3^{12}`, `(18,2,2,1^{14})` or `(18,3,1^{15})`, and `4^9` are pairwise distinct, so there is no fourth branch value and no hidden target automorphism | **CONFIRMED** | a leftover ramification unit; a repeated finite `W` root off `B`; a Möbius of the target permuting `{0,1,infty}` while preserving types; coincident labels `1=0` or `1=infty` |
| 5 | Fixed-passport Hurwitz finiteness (no unitree list) gives isotriviality over `L`. The index-18 point is unique, so source identifications are affine; depression kills translation. Factorization of `beta` recovers the monic pair uniquely | **CONFIRMED** | a positive-dimensional Hurwitz component; a second index-18 point; a translation preserving both depressed polynomials; a second monic pair with the same `beta`; a unitree list used as a complete classification |
| 6 | `W(z)=lambda^{-36} W0(lambda z)` yields `[z^{18}]W=C18 lambda^{-18}`. Every finite source-stabilizer twist satisfies `mu^{18}=1`, so (4.3) is invariant. The exponent is `-18`, not `+18` or `-20` | **CONFIRMED** | a Jacobian factor `lambda^{-36}` of the wrong weight; `[Z^{18}]W0` scaling as `lambda^{18}` rather than `lambda^{18-36}`; a stabilizer element with `mu^{18}!=1`; a residual translation |
| 7 | `lambda^{18} in C*` forces `lambda in C*` by splitting of `X^{18}-c` in any field containing `C`. Every coefficient of `f,g` and the tail `r8` is therefore a differential constant of `L`, contradicting `9 r8'=j/u !=0`. Nonconstant algebraic roots of constants do not exist over algebraically closed `C` | **CONFIRMED** | a nonconstant `lambda` in a finite extension of `L` with `lambda^{18} in C*`; constant field of `L` larger than `C`; `r8` moving while `f,g in C[z]`; the terminal row allowing `r8'=0` |
| 8 | Strongest licensed conclusion is emptiness of the two full-absorption passports on this leaf. Not the generic fibre, not a single collision, not a double `B` root off `W`, not equal non-`1` critical values, not Taylor, not all `(9,12)`, not maximum twelve, not a counterexample, not JC2 | **CONFIRMED** | a hidden promotion in the report, registration, README, freeze, or replay payload; a four-point leftover treated as three-point |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Hashes and replay (regression only)

Recomputed SHA-256 on the working-tree bytes match the launch prompt, `MANIFEST.sha256`, and `FREEZE.txt`:

| Artifact | SHA-256 | Cross-check |
|---|---|---|
| `xmodel/max12-912-order3-nu-belyi-collision-boundary-20260824.md` | `9b717712e59b70a6b06303f745a9c70b2152e3f624d03162741e3338ef1168b7` | prompt, `MANIFEST`, `FREEZE` |
| `cases/…/REGISTRATION.md` | `a5e16635593c19dea316b1b14a059ceef6f5b4391e302fbe89940383b60a5082` | `MANIFEST`, `FREEZE` |
| `cases/…/README.md` | `8ae1a375b1896ee76a598a4c32aab1e81c53d2d031afd0bf6e41a56950957d69` | `MANIFEST`, `FREEZE` |
| `cases/…/replay.py` | `16e0c18882152229d04ca68f91925b70ea90c3c245ee382f69b3b3bece13c42d` | `MANIFEST`, `FREEZE` |
| `cases/…/replay.json` | `28ea8dfd9859a09f6be75823c8a4ed2ecf7cf32da3eecf05307aa7730622fa9c` | `MANIFEST`, `FREEZE` |
| `cases/…/MANIFEST.sha256` | `7f24f78f494f54eb4ae9a974ebb2ebec59f6ab0f098cbb6e1a495dc3d48a5592` | prompt, `FREEZE` |
| `cases/…/FREEZE.txt` | `7fd777af0507d06407baf360f613f1841d7e5fb4f18999ba198ff852fc28935b` | prompt only |

Predecessor hashes recomputed, not used as mathematical evidence beyond the licensed inputs named above:

| Artifact | SHA-256 |
|---|---|
| `xmodel/max12-partial-y-kummer-preflight-20260824.md` | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` |
| `xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md` | `2951856cabe309fe07f564693a6b48a38cd7108616ffe41305d9583611da90fe` |
| `xmodel/max12-partial-y-shared-faber-probe-20260824.md` | `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036` |
| `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md` | `e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c` |
| `xmodel/max12-912-order3-dz20-stabilizer-valuation-review-grok-20260824.md` | `a8d7282ff98a0dfd998c52bfc60eed7e9f64ff89e6a988682ef8e80202229300` |

`python3 cases/max12_912_order3_nu_belyi_collision_20260824/replay.py | diff -u cases/max12_912_order3_nu_belyi_collision_20260824/replay.json -` exits `0`. `shasum -a 256 -c cases/max12_912_order3_nu_belyi_collision_20260824/MANIFEST.sha256` is `OK` on every named path. The replay checks the three top exponents of `W`, the discriminant scalar `-1296`, both fibre partitions, both Riemann–Hurwitz sums, and the scaling exponent `18-36=-18`. It does not prove isotriviality, does not expand a Laurent series, does not construct a Belyi map, and does not force `lambda in C*`. It is regression only.

The case directory contains exactly the six freeze/manifest/readme/registration/replay files. No enumerator or AWS helper is present.

---

## Claim 1 — leading term of `W` and the centered quadratic `B`

**CONFIRMED.**

The reviewed Faber theorem supplies, over `L=C(x)(u)`, a unique expansion `g=sum_{j=0}^{12} h_j F_j` with all `h_j` differential constants, and the remaining system `r_1'=...=r_7'=0`, `9 r_8'=j/u`. The three legal gauges on `(9,12)` kill `h_9`, `h_0`, and `h_3`. On the order-three leaf, constants have weight `0 mod 3`, so the only surviving Faber constant is `h_6=k`. At `k=0` one has `H(T)=T^{12}` and `g=[w^{12}]_+`.

The Laurent coefficients `r_ell` of `T=w^{12}-g` have Kummer weight `12+ell equiv ell mod 3`. Weight-nonzero differential constants of `L` vanish because the constant field is `C` (a weight-one candidate `c u` has derivative `c h'/(3 u^2)`, which vanishes only if `c=0` or `h` is constant, the trivial class). Thus `r_1=r_2=r_4=r_5=r_7=0`, and `r_3=mu`, `r_6=nu` are the only possible nonzero constants among `r_1,...,r_7`. The specialization `mu=0`, `nu in C*` is exactly the named leaf. The terminal row forces `r_8` nonconstant, hence nonzero.

Elementary tail identity, independent of any fibre compiler:

```text
W = g^3 - f^4 = -3 w^{24} T + 3 w^{12} T^2 - T^3.
```

With `T=nu w^{-6}+r8 w^{-8}+...` the three displayed terms have top exponents `18`, `0`, `-18`. The `z^{18}` coefficient is `-3 nu`. Depression gives `w=z+O(z^{-1})`, so `w^{18}=z^{18}+O(z^{16})` and `[z^{18}]W=[w^{18}]W=-3 nu`. No hidden leading cancellation: `nu!=0` prevents the first term from vanishing, and the other two cannot reach degree `18`.

Wronskian. Directly, `beta=g^3/f^4` and `X=T w^{-12}` give `beta=(1-X)^3` and `g^2/f^5=w^{-21}(1-X)^2`. Comparing with `beta_z=g^2 B/f^5` cancels `(1-X)^2` identically (on this leaf `X` starts at `w^{-18}`, so `1-X` is a unit in the Laurent series) and yields

```text
B = -3 w^{21} X_z = 3 sum_{l>=1} (l+12) r_l w^{8-l} w_z.
```

For `l>=9` the series has no polynomial part. For `1<=l<=8` one has `[w^{8-l} w_z]_+=F_{9-l}'/(9-l)`, because the negative tail of `w^{9-l}` starts at `z^{-1}` or lower and its `z`-derivative does not contribute to the polynomial part. The finite exact ladder is therefore

```text
B = sum_{l=1}^8 3(l+12)/(9-l) r_l F_{9-l}'.
```

On the leaf only `l=6` and `l=8` survive, with coefficients `18` and `60`. A monic depressed degree-nine core has `F_3=[w^3]_+=z^3+p z+q` with `p=a_7/3`, and the tail of `w^3` starts at `z^{-1}`, so `[3 w^2 w_z]_+=F_3'`. Thus

```text
B = 18 nu F_3' + 60 r8 = 54 nu z^2 + 18 nu p + 60 r8.
```

There is no `z` term. Independent truncated-Laurent reconstruction on a generic `k=0` pair (all eight `r_l` live) matched this ladder coefficient-for-coefficient; the leaf is the specialization. Discriminant of `a z^2+c` with `a=54 nu` and `c=18 nu p+60 r8` is `-4ac=-1296 nu(3 nu p+10 r8)`, and `-4*54*6=-1296`. When the discriminant vanishes the double root is at `z=0`.

The identity does not consume a component decomposition or either Taylor boundary.

---

## Claim 2 — coprime and squarefree firewall

**CONFIRMED.** Independently re-derived; agrees with the already-confirmed DZ20 firewall.

Keller plus the chain rule is `u D=j` with `D=f_x g_z-f_z g_x`, so `D=j/u in L^*` is a nonzero element of `L`, of `z`-degree `0`.

If a nonunit `d in L[z]` divides both `f` and `g`, write `f=d f_1`, `g=d g_1`. Then `f_x=d_x f_1+d f_{1,x}` and `f_z=d_z f_1+d f_{1,z}`, and likewise for `g`. Expanding the Jacobian shows that `d` divides every term of `D`. A nonunit cannot divide a nonzero `z`-constant. Equivalently: at a common root `alpha` in an algebraic extension, differentiating `f(alpha)=g(alpha)=0` along `x` yields `D(alpha)=0`; since `D` is independent of `z`, `D=0`.

If `d^2` divides `f`, then `f=d^2 f_1` gives `f_x=2 d d_x f_1+d^2 f_{1,x}` and `f_z=2 d d_z f_1+d^2 f_{1,z}`, so `d` divides both `f_x` and `f_z`, hence divides `D`. The same applies to `g`. Thus on every actual trajectory

```text
gcd(f,g)=1,     f and g are squarefree.
```

In particular `B` cannot vanish at a root of `f` or of `g`. At a root of `f` one has `B=-4 g f_z`, with `g!=0` by coprimeness and `f_z!=0` by squarefreeness. At a root of `g`, `B=3 f g_z!=0`. Coefficient-fibre components violating this are algebraic artifacts and cannot be imported into a trajectory claim. The common-power family `f=K^3`, `g=K^4` has `W=0` and `B=0`, already excluded by `nu!=0` and by `j!=0`.

The double root of the centered quadratic, when it exists, is at `z=0`. If `f(0)=0` or `g(0)=0` then `B(0)=0` would place a `B` root on `f g=0`, contradicting the firewall. So on the double-root stratum both `f(0)` and `g(0)` are nonzero.

---

## Claim 3 — local multiplicities and exact passports

**CONFIRMED.**

By (1.2), `beta-1=W/f^4 ~ -3 nu z^{-18}` at infinity, so infinity is a point of ramification index `18` over `beta=1`. Simple roots of `g` give `3^{12}` over `0`. Simple roots of `f` give `4^9` over infinity.

The polynomial identity

```text
f W_z - g^2 B = 4 f_z W
```

holds on every monic pair of degrees `(9,12)` (checked by expansion on eight random depressed samples, and by substituting the definition of `B`). At a root of `W` away from `f g=0` one therefore has `W_z=g^2 B/f`. A repeated finite root of `W` is exactly a root of `B`.

Distinct simple `B` roots in `W`. At such a root `rho`, `B'(rho)!=0` and `f(rho) g(rho)!=0`. Differentiating the identity and evaluating gives `W_z(rho)=0` and

```text
W_{zz}(rho) = g(rho)^2 B'(rho) / f(rho) != 0.
```

Thus `W` has multiplicity exactly two, not higher, and `beta-1=W/f^4` has multiplicity exactly two. This matches a simple zero of `beta_z=g^2 B/f^5`. Two such points and the index-18 point at infinity leave `36-18-2-2=14` unramified finite points over `1`. The fibre is `(18,2,2,1^{14})`. Independent local constructions forcing `W(0)=B(0)=0` with `B'(0)!=0` produced valuation `(val B, val W)=(1,2)` in every coprime sample, with the displayed second-derivative identity.

Double `B` root in `W`. Discriminant zero makes `B=54 nu z^2`. The condition that the double root lie in `W` is `W(0)=0`. Let `k=v_0(W)>=1`. Comparing valuations in `W_z=(g^2 B+4 f_z W)/f`:

- `k=1` is impossible (`W_z(0)` would be a unit, while the right-hand side vanishes);
- `k=2` gives `val(W_z)=1` against right-hand side valuation `2`;
- `k>2` forces the right-hand side to have valuation `2`, hence `k=3`.

At `k=3` the leading coefficients match by `3 W[3]=g(0)^2 B[2]/f(0)!=0`. Thus the multiplicity is exactly three, not higher, and `beta-1` has multiplicity exactly three. The fibre is `(18,3,1^{15})`. Independent local constructions forcing `W(0)=B(0)=B'(0)=0` with `B''(0)!=0` produced valuation `(2,3)` in every coprime sample, with the displayed leading-coefficient identity.

A `B` root at `f g=0` is excluded by Claim 2. Higher multiplicity of `W` is excluded by the nonzero leading coefficients above. The two simple `B` roots cannot collide with infinity (they are finite). They collide with each other precisely on the discriminant-zero stratum.

---

## Claim 4 — Riemann–Hurwitz and no fourth branch value

**CONFIRMED.**

A degree-`36` map `P^1 -> P^1` has total ramification `2*36-2=70`. The two full-absorption ledgers are

```text
12*(3-1)+9*(4-1)+[(18-1)+2*(2-1)] = 24+27+19 = 70,
12*(3-1)+9*(4-1)+[(18-1)+(3-1)]   = 24+27+19 = 70.
```

Both are sharp. There is no leftover ramification unit, so there is no fourth branch value.

Every other finite root of `W` is simple, because a repeated root off `f g=0` is a root of `B`, and both roots of `B` (counted with multiplicity) have already been placed in `W`. Zeros of `beta_z=g^2 B/f^5` occur only at zeros of `g` (already counted as index `3` over `0`) and at zeros of `B` (already placed over `1`). Poles occur only at zeros of `f` (index `4` over infinity). No unrecorded branch value.

The labelled ramification types over `{0,1,infty}` are pairwise distinct: `3^{12}` versus either `(18,2,2,1^{14})` or `(18,3,1^{15})` versus `4^9`. No nontrivial target automorphism in `PGL_2` preserves the labelled triple, and none even preserves it unlabelled. Coincident labels `1=0` or `1=infty` would require a common root of `W` and `g`, or of `W` and `f`, contradicting coprimeness.

Full absorption versus a single collision is a different passport. One simple `B` root in `W` gives fibre `(18,2,1^{16})` over `1`, Riemann–Hurwitz contribution `18` rather than `19`, and a leftover unit carried by the other simple `B` root over a value `c not in {0,1,infty}`. That is a four-point family, retained by the producer. Collision of the two distinct non-`1` critical values likewise remains four-point unless both critical points themselves lie over `1`, which is case (3.2). A double `B` root off `W` contributes index `3` over a fourth value and is likewise retained. None of these is smuggled into the three-point exclusion.

Existence of a complex pair of either full-absorption passport is not required. If the Hurwitz number vanishes the boundary is empty a fortiori.

---

## Claim 5 — isotriviality, unique index-18 point, depression, monic recovery

**CONFIRMED.**

A Belyi map of degree `36` with either passport is a transitive triple in `S_{36}` of the displayed cycle types with product one. The symmetric group is finite, so there are finitely many conjugacy classes. Riemann’s existence theorem realises each class by a cover `P^1 -> P^1` branched at `{0,1,infty}`, unique up to source Möbius transformation. This is Hurwitz finiteness of a three-point passport. It does not use Pakovich–Zvonkin, it does not claim that unitrees list all equality pairs, and it does not require the Hurwitz number to be positive.

The source of `beta` is `P^1`, hence connected, so monodromy is transitive. Over `L`, `beta in L(z)` is a family of such covers, branched at the three constant points `0,1,infty`. The Hurwitz space of a fixed passport is zero-dimensional. A family of three-point covers over a connected base is therefore isotrivial: after a source Möbius defined over a finite extension of `L`, `beta` is a constant Belyi map.

The fibre over `1` contains a unique part equal to `18`. Source infinity realises it, by `beta-1 ~ c z^{-18}`. A second index-18 point would be a finite root of `W` of multiplicity `18`, incompatible with the exact multiplicities two or three of Claim 3. Source identifications preserving the labelled covering therefore fix infinity and are affine: `z |-> lambda z + tau`.

Depression. For a monic degree-`9` polynomial, the coefficient of `z^8` in `F(z+tau)` is `9 tau`. Characteristic zero forces `tau=0`. The same translation coefficient for `G` is `12 tau`. No special pair retains a nontrivial translation.

Factorization. Zeros of `beta` are the simple zeros of `g`, with multiplicity `3`. Poles are the simple zeros of `f`, with multiplicity `4`. The monic polynomials with those roots are uniquely `g` and `f`. Extra scalar freedom `(lambda g, mu f)` with `lambda^3=mu^4` would preserve `beta`, but monicity forces `lambda=mu=1` by comparing leading coefficients. Recovery is unique.

After a finite extension of `L`, a constant template `(F,G)` therefore yields the normal form (4.1). There is no further `PGL_2` twist: a Möbius swapping `0` and `infty` would move the unique index-18 point, and the labelled ramification types are pairwise distinct.

---

## Claim 6 — scaling exponent and stabilizer twists

**CONFIRMED.**

From (4.1),

```text
W(z) = g^3-f^4 = lambda^{-36} (G(lambda z)^3 - F(lambda z)^4) = lambda^{-36} W0(lambda z).
```

If `W0=C18 Z^{18}+...` with `C18 in C^*` (the constant template has the same spectral degree `18`, because scaling does not change polynomial degree and `[z^{18}]W=-3 nu !=0`), then

```text
W0(lambda z) = C18 lambda^{18} z^{18}+...,
[z^{18}]W = C18 lambda^{18-36} = C18 lambda^{-18}.
```

Independent substitution on a sample pair with `lambda=2` matched both the leading-coefficient identity and the full polynomial identity `W(z)=lambda^{-36} W0(lambda z)`. Combining with (1.2) gives `C18 lambda^{-18}=-3 nu`, hence `lambda^{18}=-C18/(3 nu) in C^*`. The exponent is `-18`, not `+18`. It is also not the tail weight `-20` of `r8` (see Claim 7).

Residual source stabilizer. After fixing infinity and depressing, finite subgroups of `G_m` are cyclic of order `e`. A generic fibre has `36` points, so `e | 36`. The local expansion `beta-1=c z^{-18}+...` together with `beta(mu z)=beta(z)` forces `mu^{-18}=1`, so `e | 18`. Thus `e | gcd(36,18)=18`. Every stabilizer element therefore satisfies `mu^{18}=1`, and replacing `lambda` by `lambda mu` leaves both `C18` and `lambda^{18}` unchanged:

```text
(lambda mu)^{18} = lambda^{18} mu^{18} = lambda^{18},
[Z^{18}](mu^{-36} W0(mu Z)) = C18 mu^{-18} = C18.
```

The equation (4.3) is insensitive to every finite source-stabilizer twist, including the large cyclic groups of order `3,6,9,18` that the index-18 expansion permits (in contrast to the index-20 coprime fibre, where `e | 4`). No residual translation survives depression. Target roots of unity are killed by Claim 4. Monicity kills scalar `(f,g)` freedom.

Kummer covariance is compatible: `sigma(z)=zeta z` acts as `lambda |-> lambda/zeta` up to stabilizer, and `zeta^{18}=1`, so `lambda^{18}` remains fixed. If `lambda in C^*` then `zeta^{-1}` itself lies in the stabilizer, which forces the constant template to be a polynomial in `z^3`; that is a restriction on which constant pairs can appear, not an escape from constancy.

---

## Claim 7 — `lambda^{18} in C^*` forces differential-constant coefficients and `r8`

**CONFIRMED.** This is the load-bearing step, and the naive shortcut that does not pass through `lambda in C^*` is false.

Let `M` be a finite extension of `L` containing `lambda`, as supplied by isotriviality. Then `C subset L subset M` and `lambda^{18}=c in C^*`, so `lambda` is a root of `X^{18}-c in C[X]`. Because `C` is algebraically closed this polynomial splits as `prod (X-zeta_i)` with every `zeta_i in C subset M`. An integral domain cannot contain a product of nonzero factors equal to zero, so `lambda=zeta_i` for some `i`. Hence `lambda in C^*`.

Nonconstant algebraic roots of constants do not exist in a function field over an algebraically closed constant field. A putative unit `phi in M^*` with `phi^{18}=1` would be a root of `X^{18}-1`, hence likewise constant. An element of weight one such as `u v` with `v in C(x)` would have eighteenth power `h^6 v^{18}`, which lies in `C^*` only if `h` is a cube in `C(x)` up to a constant, contradicting exact Kummer order three — but this branch is already excluded by the splitting argument, which never produces a nonconstant `lambda`.

Coefficients. From (4.1), `a_i=A_i lambda^{i-9}` with `A_i in C`. Now `lambda in C^*`, so every `a_i` lies in `C`. The same holds for the coefficients of `g`. The constant field of `L` under `d/dx` is `C`, so these coefficients are differential-constant.

The tail `r8`. This is not itself a coefficient of `f` or `g`. It is the coefficient of `w^{-8}` in `w^{12}-g`. Under (4.1) one has `w_f(z)=lambda^{-1} w_F(lambda z)` and `T(z)=lambda^{-12} T_0(lambda z)`, so the raw `z^{-8}` term of the tail scales as `lambda^{-20}`. If one knew only `lambda^{18} in C^*` and not `lambda in C^*`, this would not force `r8` constant: `-20` is not a multiple of `18`. The splitting step is therefore necessary for `r8`, not ornamental. Once `lambda in C^*`, the whole series `T` has constant coefficients, so `r8 in C` and `r8'=0`.

This contradicts the terminal Faber row `9 r8'=j/u !=0`. Therefore neither full-absorption passport supports an actual Keller trajectory.

The same conclusion can be read off the coefficients of `f` alone, without naming `r8`: a pair in `C[z]` cannot satisfy a nonzero `z`-constant Jacobian whose right-hand side `j/u` involves a nonconstant Kummer radical. The producer’s route through `r8` is the one licensed by the Faber landing.

---

## Claim 8 — scope

**CONFIRMED.**

The report, registration, README, freeze, and replay payload all refuse the same promotions. The exact excluded strata are the two full-absorption passports. Explicitly retained: no `B` root in `W`; exactly one simple `B` root in `W`; a double `B` root off `W`; equal non-`1` critical values at two distinct `B` roots; both Taylor boundaries; other invariant loads; the order-one core. No `(9,12)` emptiness, maximum-twelve automorphy, counterexample, or JC2 sentence is present. Collision of the two non-`1` critical values is correctly distinguished from (3.2).

---

## Independent reconstruction (not the producer replay)

Scratch lived in `/tmp` and is not in the bank. It re-derived, without importing `replay.py` or any fibre compiler:

- `F_3=z^3+(a_7/3)z+a_6/3` from the binomial expansion of `w=f^{1/9}`;
- the general ladder `B=sum_{l=1}^8 3(l+12)/(9-l) r_l F_{9-l}'` by truncated Laurent series on a generic `k=0` pair, matching `3 f g_z-4 g f_z` coefficient-for-coefficient, then the leaf specialization `18 nu F_3'+60 r8`;
- top exponents `[18,0,-18]` of `-3 w^{24} T+3 w^{12} T^2-T^3` and the conversion `[z^{18}]=[w^{18}]` under depression;
- `disc=-4ac=-1296 nu(3 nu p+10 r8)`;
- the polynomial identity `f W_z-g^2 B=4 f_z W` on eight random depressed `(9,12)` pairs;
- local valuations `(val B, val W)=(1,2)` with `W_{zz}=g^2 B'/f` at a simple common root, in seventeen coprime samples;
- local valuations `(2,3)` with `3 W[3]=g^2 B[2]/f` at a double common root, in thirty coprime samples;
- both Riemann–Hurwitz sums `70=70`, the one-collision leftover `69`, and the no-collision leftover `68`;
- `W(z)=lambda^{-36} W0(lambda z)` and `[z^{18}]W=C18 lambda^{-18}` by exact substitution at `lambda=2`;
- `e | gcd(36,18)=18` and invariance of `lambda^{18}` under `mu_e`;
- splitting of `X^{18}-c` in any integral domain containing `C`.

Targeted identities passed; none failed.

---

## Non-blocking remarks

1. There is no completed different-model review of the order-three fibre compiler, nor of the spectral Wronskian-ladder producer that first wrote (1.3) as a portable identity. This review does not bank either. The quadratic `B` and `[z^{18}]W=-3 nu` are re-derived from reviewed Faber+character inputs and elementary tail calculus.
2. Named producer artifacts for this case are untracked on `2e6104a`. Charged hashes match the launch table. A concurrent untracked `cases/max12_912_order3_nu1_probe_20260824/` was not consumed.
3. The scaling weight of `r8` is `-20`, not `-18`. A reader who infers constancy of `r8` from `lambda^{18} in C*` without passing through `lambda in C*` has a false implication. The producer does supply the missing step, via algebraic closure of `C`. The splitting argument above is the explicit form of that step in a function field.
4. The residual stabilizer may be as large as `mu_{18}`. That does not enlarge the constant-field conclusion: every such twist preserves `lambda^{18}`, and `lambda` itself still lies in `C^*`.
5. The replay is an integer regression. Isotriviality, local multiplicities, and the splitting of `X^{18}-c` are not in the payload.

---

## Verdict

**Accept `ON THE REVIEWED ORDER-THREE k=mu=0, nu!=0 LANDING, NO ACTUAL KELLER TRAJECTORY SURVIVES WHEN THE COMPLETE RAMIFICATION DIVISOR OF THE QUADRATIC SPECTRAL WRONSKIAN B IS ABSORBED BY W=0` at the stated scopes.**

Overall: **CONFIRMED**. Claims 1–8: **CONFIRMED**. Smallest failing identity: none. Smallest missing hypothesis: none that breaks a numbered claim.

Do not promote this to the generic `nu`-loaded fibre, a single `B`--`W` collision, a double `B` root off `W`, equal non-`1` critical values, a Taylor boundary, the order-one core, emptiness of `(9,12)`, maximum-twelve automorphy, a counterexample, or JC2.
