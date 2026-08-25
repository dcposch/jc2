# Hostile different-model review — maximum-12 `(9,12)` order-three unordered critical-value norm

| Field | Value |
|---|---|
| Claim under review | Frozen producer: on the reviewed `k=mu=0`, `nu=1` landing, `B/54=z^2-s` and `C(T)=Norm(g^3-T f^4)` has `disc_T C=4 s E^2`. After localizing at `s*Norm(F)!=0` the four leaves (full absorption, exactly one absorption, equal non-`1` values, unequal unabsorbed values) are disjoint and exhaustive. The double-`B` and `B`-meets-`f` strata are retained. No leaf is excluded |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking: `nu=1` is legal only as a constant source scaling `lambda^{18}=1/nu` over algebraically closed `C`, equivalently as the affine chart `r6=1` of the weighted cone; characteristic not `2` or `3` is the ambient Faber setting. The order-three fibre compiler has no completed different-model review and is not consumed as a theorem) |
| Evidence tier | independent binomial `F_12`; independent quadratic-algebra reduction and pair powers; hand expansion of `disc_T C=4 s E^2`; exact rational specializations on and off the seven-row fibre comparing `C(T)` to `Res_z(z^2-s, g^3-T f^4)` and to `Res_z(B, g^3-T f^4)`; actual Wronskian `3 f g_z-4 g f_z` versus the leaf quadratic; Laurent tails from `f(z(w))=w^9`; scaling weights of `nu`, `r8`, and `B`; parity substitution; unmodified registered replay as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Charged ancestor | none named by the launch prompt |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (`Promote max12 DZ20 exclusion and source audits`). Named producer artifacts for this case are untracked on top of that HEAD; charged hashes below are unchanged |
| Review window (UTC) | `2026-08-24T21:12:00Z` – `2026-08-24T21:28:00Z` |
| Python | CPython 3.14.6, stdlib only (registered replay and independent reconstruction) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, case, exact order-three parent compiler, and the pinned full-absorption and parity producer/review pairs reread in full before any verdict:

- `xmodel/max12-912-order3-critical-value-norm-20260824.md`
- `cases/max12_912_order3_critical_value_norm_20260824/{REGISTRATION.md,README.md,replay.py,replay.json,MANIFEST.sha256,FREEZE.txt}`
- `cases/max12_912_order3_fibre_20260824/order3_fibre.py` (exact parent compiler; no completed fibre review exists in-tree; unused as a theorem)
- `xmodel/max12-912-order3-nu-belyi-collision-boundary-20260824.md` and `xmodel/max12-912-order3-nu-belyi-collision-boundary-review-grok-20260824.md`
- `xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md` and `xmodel/max12-912-order3-nu-parity-genus5-review-grok-20260824.md`

No producer, case, canonical, coordination, prompt, log, run, or other review file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp`.

---

## Promotion

**Accept `ON THE NORMALIZED ORDER-THREE k=mu=0, nu=1 COEFFICIENT FIBRE, THE UNORDERED PAIR-NORM C(T)=Norm(g^3-T f^4) IS AN EXACT ROOT-FREE STRATIFIER WITH disc_T C=4 s E^2` at the stated scopes.**

- Normalizing the nonzero constant load `nu` to one is a constant source scaling `z |-> lambda z` with `lambda^{18}=1/nu`. The 18th root exists in `C*` because the constant field of `L` is algebraically closed. Equivalently, the identities are those of the affine chart `r6=1` of the weighted cone. Weights: `nu` has weight `18`, `r8` has weight `20`, `a7` has weight `2`, `B` has weight `20`.
- On the seven-row leaf `r1=r2=r3=r4=r5=r7=0`, `r6=nu`, `r8=rho`, one has `p=a7/3` and `B=54 nu z^2+18 nu p+60 rho`. At `nu=1` this is `B=54(z^2-s)` with `s=-(a7+10 rho)/9`. Off the fibre the actual Wronskian has degree greater than two and does not equal this quadratic.
- Source `f` is the generic monic depressed degree-nine polynomial and `g=F_12` at `k=0`. Neither is reduced by the fibre ideal. Reducing modulo `z^2=s` produces the charged even/odd remainders, including all eight pair hashes.
- In the quadratic algebra, `C(T)=Norm(G-T F)=C0+C1 T+C2 T^2` with the displayed coefficients, `E=G0 F1-G1 F0`, and `disc_T C=4 s E^2`, `C(1)=Norm(W)`. These are polynomial identities in `(G0,G1,F0,F1,s)` and do not use the fibre.
- `C(T)` equals `Res_z(z^2-s, g^3-T f^4)` exactly. `Res_z(B, g^3-T f^4)` equals `54^{deg Q} C(T)` with the actual `z`-degree of `Q`. No leading factor is lost in the pair form.
- After localizing at `s*Norm(F)!=0`, the four leaves are the Boolean partition of whether `W=0` as a pair, whether `Norm(W)=0` with `W!=0`, and whether `E=0` with `Norm(W)!=0`. The loci `s=0` and `Norm(F)=0` are excluded from that open set and retained separately. The actual-Keller coprimality firewall is not applied.
- Parity is a positive control that `E=0`. It is not claimed to be the whole equal-value leaf, and no residual leaf is excluded.

**Do not promote this to:** emptiness of any of the four leaves; emptiness of the double-root or `B`-meets-`f` strata; a Taylor boundary; the terminal ODE; other loads; the order-one core; `(8,12)`; all `(9,12)`; maximum-twelve automorphy; a counterexample; or JC2.

**Smallest valid successor.** Attach the original seven fibre rows and both Taylor families to each leaf, then use cube-divisor or four-point Hurwitz genus before any broad primary decomposition. Do not open a generic coefficient rectangle or AWS. Do not apply the coprimality firewall without its reviewed hypotheses.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a characteristic-zero Keller pair of type `(9,12)`, empties a residual leaf, transports a Taylor boundary, or closes maximum twelve. Producer replay output was not used as evidence; the Faber binomial, the quadratic pair algebra, the discriminant expansion, the resultant comparisons, the actual Wronskian, the tails, and the scaling weights were re-derived. The reviewed full-absorption theorem is consumed only for the leaf quadratic `B=54 nu z^2+18 nu p+60 r8`, the leading term `[z^{18}]W=-3 nu`, and the already-confirmed coprimality/squarefreeness firewall (which is *not* applied here). The reviewed parity theorem is consumed only as a positive control that odd `f` and even `g` force `E=0`, and as a source of exact fibre points. The fibre compiler is not a reviewed theorem; `F_12` and `z(w)` used as evidence were rebuilt from the reviewed binomial and `f(z(w))=w^9`.

---

## Scope (not enlarged)

Exact coefficient-field case split of the two unordered critical values of `beta=g^3/f^4` at the roots of the leaf quadratic `B`, after `nu=1`. Residual-leaf emptiness, Taylor reconstruction, terminal dynamics, other loads, the order-one core, all `(9,12)`, maximum-twelve coverage, a counterexample, and JC2 remain out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Normalizing `nu in C*` to one is a legal constant source scaling `lambda^{18}=1/nu`, equivalently the chart `r6=1`. Covariance: `nu |-> lambda^{18} nu`, `r8 |-> lambda^{20} r8`, `a7 |-> lambda^2 a7`, `B_new(Z)=lambda^{20} B_old(Z/lambda)` | **CONFIRMED** | a nonconstant `lambda` required; weight of `nu` other than `18`; `B` of weight other than `20`; the `nu=1` quadratic used as if it equalled the Wronskian at general `nu` without scaling |
| 2 | On the actual seven-row fibre with `r8=rho`, `p=a7/3` and `B=54 nu z^2+18 nu p+60 rho`; at `nu=1` one has `B=54(z^2-s)` with `s=-(a7+10 rho)/9`. Off the fibre the actual Wronskian is not this quadratic | **CONFIRMED** | a linear term in `B` on the leaf; `p!=a7/3`; on-fibre mismatch of `3 f g_z-4 g f_z` with the displayed quadratic; off-fibre accidental identity |
| 3 | Source `f,g` are the generic `k=0` Faber pair, not reduced by the fibre. Even/odd remainders modulo `z^2=s` match all charged hashes and term counts `10/11`, `44/27`, `1437/1272`, `3799/3301` | **CONFIRMED** | independent `F_12` disagreeing with the parent binomial; a pair hash mismatch; fibre relations smuggled into `f` or `g` (e.g. independence of `a0`) |
| 4 | `C0=G0^2-s G1^2`, `C1=-2(G0 F0-s G1 F1)`, `C2=F0^2-s F1^2`, `E=G0 F1-G1 F0`, `disc_T C=4 s E^2`, `C(1)=Norm(W)` as polynomial identities | **CONFIRMED** | a different expansion of `C1^2-4 C0 C2`; `C(1)` not equal to `Norm(G-F)` |
| 5 | Up to the declared leading scalar, `C(T)=Res_z(z^2-s, g^3-T f^4)` exactly, and `Res_z(B, g^3-T f^4)=54^{deg Q} C(T)`, on exact rational controls both on and off the fibre | **CONFIRMED** | a missing or extra power of `54`; pair-norm disagreeing with the monic-quadratic resultant; a hidden content factor changing the vanishing locus |
| 6 | On `s*Norm(F)!=0` the four leaves are disjoint and exhaustive. `s=0` (split by `W0`) and `Norm(F)=0` are separate. `Norm(F)=Norm(f)^4`, so `B`-meets-`f` is the same locus as `Norm(f)=0`. One-root versus two-root absorption is `Norm(W)=0` with `W!=0` versus `W=0` | **CONFIRMED** | a fifth Boolean case on the open set; `W=0` not implying `E=0`; `s=0` or `Norm(F)=0` folded into a leaf; the firewall used to empty `Norm(F)=0` |
| 7 | On parity, `f` even remainder and `g` odd remainder vanish, hence `F1=G1=E=0`. Parity is a positive control, not the whole equal-value leaf. No residual leaf is excluded | **CONFIRMED** | a nonzero parity even-`f` or odd-`g` remainder; `E` not vanishing on parity; a hidden emptiness claim in the report, registration, FREEZE, README, or replay payload |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Hashes and replay (regression only)

Recomputed SHA-256 on the working-tree bytes match the launch prompt, `MANIFEST.sha256`, and `FREEZE.txt`:

| Artifact | SHA-256 | Cross-check |
|---|---|---|
| `xmodel/max12-912-order3-critical-value-norm-20260824.md` | `7339478798e00894c7b975c60aca821ec7ff2da383ffe5165a93cfa361bb6cb6` | prompt, `MANIFEST`, `FREEZE` |
| `cases/…/REGISTRATION.md` | `1027142326e68f2014625869d5707af58ba651ca07e8a1b3560907438c2cf615` | `MANIFEST` |
| `cases/…/README.md` | `2ad3c94a4570c2bd97568958a7d04a12c60340b4380e7644f74d21371f1aad91` | `MANIFEST` |
| `cases/…/replay.py` | `88f4e2145defe8b548cd5794d171ee7919da77257811a51271df7dbb68e7e4df` | `MANIFEST` |
| `cases/…/replay.json` | `98967e2ea85c47cdb96f7406edaf9a76c5eb8b932a65fa72c9460936f342a4d6` | `MANIFEST` |
| `cases/…/MANIFEST.sha256` | `73b55970e600fe65664a089a03642291fbbbd5e6d9480515517011f1f2745e0a` | prompt, `FREEZE` |
| `cases/…/FREEZE.txt` | `258fea426d71f524de180b84d6633f0e163f6d837f665f094ab484c22b5283d6` | prompt only |

Predecessor hashes recomputed, not used as mathematical evidence beyond the licensed inputs named above:

| Artifact | SHA-256 |
|---|---|
| `cases/max12_912_order3_fibre_20260824/order3_fibre.py` | `a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf` |
| `xmodel/max12-912-order3-nu-belyi-collision-boundary-20260824.md` | `9b717712e59b70a6b06303f745a9c70b2152e3f624d03162741e3338ef1168b7` |
| `xmodel/max12-912-order3-nu-belyi-collision-boundary-review-grok-20260824.md` | `6d34908cbd2ead9769e4090fcab903ec5d5b7bd9db485db1d681708c5d36946e` |
| `xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md` | `f37376c96ab7e3c6ed7aa554dd04e2c72c9b2f5092ba6df03f524ea44765515d` |
| `xmodel/max12-912-order3-nu-parity-genus5-review-grok-20260824.md` | `903a973ac4975dfdeea77d143ebaa33cdc504d0f75d31dfe5327dad2d9be8528` |

`python3 cases/max12_912_order3_critical_value_norm_20260824/replay.py | diff -u cases/max12_912_order3_critical_value_norm_20260824/replay.json -` exits `0`. `shasum -a 256 -c cases/max12_912_order3_critical_value_norm_20260824/MANIFEST.sha256` is `OK` on every named path. Canonical `payload_sha256` of the replay JSON is `a96165d3c673ddca777f08834d788abca1b3e9a0fd14347dea3f2e6bee1b4f57`, matching `FREEZE.txt`. The replay checks the pair hashes, the abstract discriminant and `C(1)` identities, and the parity remainders. It does not compute a Sylvester resultant, does not evaluate the actual Wronskian, does not impose the seven fibre rows on `f,g`, and does not differentiate `r8`. It is regression only.

The case directory contains exactly the six freeze/manifest/readme/registration/replay files. No enumerator or AWS helper is present.

---

## Claim 1 — legality and covariance of `nu=1`

**CONFIRMED.** Needed hypothesis, stated: the constant field of `L` is `C`, algebraically closed, so `lambda^{18}=1/nu` has a solution `lambda in C*`; equivalently, one works on the affine chart `r6=1` of the weighted cone. Characteristic not `2` or `3`.

Write `f(z)=lambda^{-9} F(lambda z)` and `g(z)=lambda^{-12} G(lambda z)`. Then `a7` has weight `2`, the load `nu=[w^{-6}]T` has weight `18`, the tail `r8` has weight `20`, and the Wronskian `B=3 f g_z-4 g f_z` has weight `20`:

```text
B_new(Z) = lambda^{20} B_old(Z/lambda).
```

Independent exact substitution at `lambda=2` on `f=z^9+3 z^7+2 z^3+1` matched all three weights coefficient-for-coefficient (`nu: -3022/81 |-> -792199168/81`, `r8: 15980/729 |-> 16756244480/729`).

On the leaf the un-normalized quadratic is `B=54 nu z^2+18 nu p+60 r8=54 nu(z^2-s_gen)` with `s_gen=-(nu a7+10 r8)/(9 nu)`. Setting `nu_new=lambda^{18} nu=1` produces `B_new=54(Z^2-s_new)` with `s_new=-(a7_new+10 r8_new)/9`. Exact control: `f=z^9-1` lies on the seven-row fibre with `nu=2/9`, `r8=0`, `p=0`, and `B=12 z^2`. After `lambda^{18}=9/2` one has `B_new(Z)=12 lambda^{18} Z^2=54 Z^2`, which is the normalized formula at `s=0`.

Without this hypothesis the producer quadratic `54(z^2-s)` is the Wronskian only on the slice `r6=1`, not at a general point of `r6=nu in C*`. The report’s first sentence and the pinned absorption paper both name that slice. The independent on-fibre samples with `nu!=1` confirm the distinction: `3 f g_z-4 g f_z` equals `54 nu z^2+18 nu p+60 r8` and does *not* equal `54 z^2+18 p+60 r8`.

---

## Claim 2 — `p=a7/3`, `B=54(z^2-s)`, fibre versus ambient

**CONFIRMED.**

Depression of a monic degree-nine polynomial gives `w=z+(a7/9) z^{-1}+O(z^{-3})` and `F_3=[w^3]_+=z^3+(a7/3) z+q`. Thus `p=a7/3` on every depressed pair, fibre or not.

The leaf ladder, already confirmed in the pinned full-absorption review and re-used here only as that quadratic, is `B=18 nu F_3'+60 r8=54 nu z^2+18 nu p+60 r8`. At `nu=1`,

```text
B = 54 z^2 + 6 a7 + 60 rho = 54(z^2-s),     s=-(a7+10 rho)/9.
```

The two writings are identical as polynomials in `(z,a7,rho)`.

Exact on-fibre controls, tails rebuilt from `f(z(w))=w^9` and `T=w^{12}-g(z(w))`, not from the producer replay:

| point | fibre rows | `nu` | `r8` | `deg B` | `B` equals leaf formula | `B` equals `nu=1` formula |
|---|---|---|---|---|---|---|
| parity `p=0`, `x5=-36`, `x3=36`, `x1=432`, `rho=r8` | `r1=r2=r3=r4=r5=r7=0` | `25344` | `124416` | `2` | yes | no |
| parity `p=1`, `v=1`, `rho=r8` | same | `-292400640` | `4364672256` | `2` | yes | no |
| `f=z^9-1`, `rho=r8=0` | same | `2/9` | `0` | `2` | yes (`B=12 z^2`) | no |
| `f=z^9+z^7+1`, `rho=1` | off | `353062/1594323` | `5852/43046721` | `7` | no | no |
| `f=z^9+z^2-2`, `rho=-9/10` | off | `8/9` | `0` | `6` | no | no |

The `p=0` parity tails independently match the reviewed identities `nu=-(11/729) x3 x5^3` and `r8=-x5^5/486`. Off the fibre, `deg B in {4,6,7}`: the producer quadratic is then a fibre-specialized polynomial in `(z,a7,rho)`, not the Wronskian. The report labels this as the landing `r1=r2=r3=r4=r5=r7=0`, `r6=1`, `r8=rho`. It does not claim the quadratic off that landing.

`rho` is a free coordinate of the ambient ring `Q[a0,...,a7,rho]`. The fibre equation `r8-rho=0` is documented and not imposed on the pair hashes. Substituting a wrong `rho` on an otherwise-fibre point moves `s` and can change the named leaf (the `p=0` parity point at `rho=0` is the producer’s `s=0` locus, while the true `r8` is `124416`). That is ambient geometry, not a hidden reduction.

---

## Claim 3 — source `f,g`, remainders, charged hashes

**CONFIRMED.**

Independent binomial `F_12=z^{12}[sum_q binom(12/9,q) U^q]_+` with `U=sum_{i=0}^7 a_i z^{i-9}` agrees coefficient-for-coefficient with the parent `faber`. Specializing `k=0` produces `g`. Reducing modulo `z^2=s=-(a7+10 rho)/9` and powering in the quadratic algebra produces the eight charged digests:

| pair | even terms / sha256 | odd terms / sha256 |
|---|---|---|
| `f` | `10` / `622d86c93d6a1e81…d6fa` | `11` / `6ea2d9048df27d18…ab00` |
| `g` | `44` / `c42c2b43e051c296…b50e` | `27` / `41bdcdbaebbbf27c…0bbc` |
| `F=f^4` | `1437` / `c4eaab9cf463d6bf…115f` | `1272` / `38399a4461ca588e…6cd4` |
| `G=g^3` | `3799` / `1e82542f0df8ad22…b53a` | `3301` / `e4b1f6e9a6c02fc9…6e76` |

The even remainder of `f` depends on `a0` (the constant term of `a0 + a2 s + a4 s^2 + a6 s^3`). The fibre ideal is not used. Term counts `10/11` match the expansion of that remainder against `s=-(a7+10 rho)/9` after like terms in `a7,rho` combine; they would collapse if `r1=...=0` had been imposed.

---

## Claim 4 — norm coefficients and `disc_T C=4 s E^2`

**CONFIRMED.** Purely in the quadratic algebra, no fibre.

`G-T F=(G0-T F0)+(G1-T F1) z` with `z^2=s`, so

```text
C(T)=Norm(G-T F)=(G0-T F0)^2-s(G1-T F1)^2
    = C0 + C1 T + C2 T^2,
C0=G0^2-s G1^2,   C1=-2(G0 F0-s G1 F1),   C2=F0^2-s F1^2.
```

Hand expansion:

```text
C1^2-4 C0 C2
  = 4(G0 F0-s G1 F1)^2 - 4(G0^2-s G1^2)(F0^2-s F1^2)
  = 4s(G0 F1-G1 F0)^2
  = 4 s E^2.
```

`C(1)=(G0-F0)^2-s(G1-F1)^2=Norm(W)`. Both identities hold as elements of `Q[G0,G1,F0,F1,s]` (computer reconstruction of the same polynomials) and on every rational sample below.

Geometrically, at the two roots `±alpha` of `z^2-s` one has `C(T)=Norm(F)(beta(alpha)-T)(beta(-alpha)-T)` and `beta(alpha)-beta(-alpha)=-2 alpha E / Norm(F)`. The discriminant identity is `(beta1-beta2)^2 C2^2=4 s E^2`.

---

## Claim 5 — pair-norm versus `Res_z(B, g^3-T f^4)`

**CONFIRMED.** The declared leading scalar is `1` against the monic quadratic `z^2-s` and `54^{deg_z Q}` against `B=54(z^2-s)`.

Euclidean resultant over `Q`, actual degrees, on every listed sample, at `T in {0,1,2,-3,5/7}`:

```text
Res_z(z^2-s, Q) = C(T),
Res_z(B, Q)     = 54^{deg Q} C(T),
Q = g^3 - T f^4.
```

No mismatch. In particular:

- Generic `T!=1`: `deg Q=36`, factor `54^{36}`.
- On the loaded leaf at `T=1`, `deg W=18` (leading cancellation `[z^{36}](g^3-f^4)=0` and `[z^{18}]W=-3 nu!=0`). For `f=z^9-1` one has `C(1)=1` and `Res_z(B,W)=54^{18}`. The pair form still equals the monic-quadratic resultant.
- Off fibre at `T=1` the degree of `W` need not be `18` (samples gave `20` and `22`). The identity uses the actual degree; a Sylvester matrix of declared size `36` would carry a different power of `54` when the leading coefficient `1-T` vanishes. The producer never expands that Sylvester matrix. The pair form is `Res_z(z^2-s,·)` and does not lose a factor.

`Norm(F)=Norm(f)^4` held on every sample. The zero loci of `Norm(F)` and `Norm(f)` agree in an integral domain. The leading coefficient `C2` is a fourth power; vanishing of `C` is unaffected.

---

## Claim 6 — four leaves, double root, `B`-meets-`f`

**CONFIRMED.**

On the open set `U={s*Norm(F)!=0}` the two roots of `B` are distinct and `beta` is finite at both. In the quadratic algebra:

- `W=0` as a pair implies `Norm(W)=0` and `E=0` (because `E=G0 F1-G1 F0` becomes `G0 G1-G1 G0`).
- Therefore the four Boolean cells
  1. `W0=W1=0`,
  2. `Norm(W)=0` and `(W0,W1)!=(0,0)`,
  3. `Norm(W)!=0` and `E=0`,
  4. `Norm(W)*E!=0`
  partition `U`. They are the named leaves: both critical points over `1`; exactly one over `1`; two distinct points with the same non-`1` finite value; two distinct unabsorbed unequal values.

`s=0` is excluded from `U`. Then `C(T)=(G0-T F0)^2`, the two critical points collide at `z=0`, and the remaining split is `W0=0` (double root over `1`, passport `(18,3,1^{15})` of the pinned absorption paper) versus `W0!=0` (double root off `W`). Sample: `f=z^9-1`, `rho=r8=0` gives `s=0`, `W0=-1`, `Norm(F)=1`, the retained double-root-off-`W` stratum.

`Norm(F)=0` is excluded from `U`. It is `B`-meets-`f`. Sample: `f=z^9+z^2-2` (off fibre, `f(1)=0`) with `s=1` lands on this stratum; `Res_z(z^2-s,Q)=C(T)` continues to hold with `C2=0`. The actual-Keller firewall `gcd(f,g)=1` plus squarefreeness, already confirmed in the pinned absorption review, would forbid this on a trajectory. It is *not* applied here. The report’s sentence “the actual-Keller coprimality firewall may be applied only with its reviewed hypotheses” is the correct refusal.

Equal values equal to `0`, `1`, or infinity:

- Both equal to `1`: `W=0`, leaf 1, not leaf 3.
- Both equal to infinity: `F=0` as a pair, inside `Norm(F)=0`, not in `U`.
- Both equal to `0`: `G=0` as a pair, hence `E=0` and `Norm(W)=Norm(F)!=0` on `U`, so leaf 3. This is `B`-meets-`g`. The firewall would forbid it on a trajectory; the coefficient stratifier correctly leaves it inside the equal-value leaf rather than emptying it. One value `0` and one not is leaf 4 (or leaf 2 if the other is `1`).

One-root versus two-root absorption is the distinction between leaf 2 and leaf 1. Exact ambient samples `ai=(-3,-3,0,...,0)` and `ai=(-1,-1,0,...,0)` with `s=1` give `Norm(W)=0`, `(W0,W1)!=(0,0)`, leaf 2. Over a field in which `s` is not a square, `k[z]/(z^2-s)` is a field, so `Norm(W)=0` as an *element* of the function field implies `W=0`; as a *locus* in coefficient space, `Norm(W)=0` forces `s` to be a square and cuts out exactly the geometric one-root set. The producer writes loci, not function-field element identities.

---

## Claim 7 — parity positive control and non-exclusion

**CONFIRMED.**

The substitution `a0=a2=a4=a6=0`, `a7=3p`, `a5=3p^2+x5`, `a3=p^3+x3`, `a1=x1` makes the even remainder of `f` and the odd remainder of `g` identically zero, hence `F1=G1=0` and `E=0`. The odd remainder of `F=f^4` and of `G=g^3` likewise vanish. This is the registered control.

`W0=G0-F0` is *not* the zero polynomial on this slice (`432` terms). On `U`, parity therefore lies in leaf 1 union leaf 3, not in leaf 3 alone. The two exact fibre parity points above land in leaf 3 (`s*Norm(F)*Norm(W)!=0`, `E=0`). The report’s sentence “placing parity in the equal-value leaf without claiming that it is the whole leaf” is the positive control `E=0` plus the refusal to empty leaf 3; it does not assert that every parity point with `s*Norm(F)!=0` has `Norm(W)!=0`. The replay string is the accurate one: `f_even=0 and g_odd=0, hence E=0`.

The report, registration, README, FREEZE refusal block, and replay `scope` string all refuse residual-leaf exclusion, Taylor transport, other loads, order one, `(8,12)`, maximum twelve, a counterexample, and JC2. The pinned full-absorption emptiness of leaf 1 on actual trajectories is a different theorem and is not imported as an exclusion in this checkpoint.

---

## Attacks that do not land

- **Hidden use of the fibre equations.** `f` and `g` are the generic `k=0` Faber pair; `a0` survives in the even remainder of `f`; term counts match the unreduced expansion. The quadratic `B=54(z^2-s)` *is* fibre-specialized and is labelled as such. `rho` is free; `r8-rho` is a documented later equation, not a silent rewrite of `g`.
- **Loss of a resultant leading factor.** Against `z^2-s` there is no factor. Against `B` the factor is `54^{deg Q}`, with `deg Q` jumping from `36` to `18` at `T=1` on the leaf. The pair form is the monic-quadratic resultant. Vanishing loci agree.
- **`Norm(f)` versus `Norm(f^4)`.** `Norm(F)=Norm(f)^4`. Zero loci coincide. `C2` being a fourth power does not change `disc_T C=4 s E^2`.
- **One-root versus two-root.** Leaf 1 is `W=0` as a pair. Leaf 2 is the hypersurface `Norm(W)=0` minus that pair-origin. Samples of leaf 2 exist over `Q`. The function-field/locus distinction is observed.
- **Equal values `0`, `1`, infinity.** Split correctly across leaf 1, leaf 3, and `Norm(F)=0`. Value `0` is not smuggled into a pole stratum.
- **Firewall applied too early.** `Norm(F)=0` is retained. The firewall is named and deferred.

---

## Independent reconstruction (not the producer replay)

Scratch lived in `/tmp` and is not in the bank. It re-derived, without importing `replay.py` as a theorem:

- binomial `F_12` agreeing with the parent `faber`;
- quadratic reduction and pair powers reproducing all eight charged hashes;
- hand and machine expansion of `disc_T C=4 s E^2` and `C(1)=Norm(W)`;
- Euclidean `Res_z` versus `C(T)` on on-fibre and off-fibre rational points, including `T=1` degree drop;
- actual Wronskian versus the leaf quadratic, matching if and only if the seven rows vanish and `(nu,r8)` are the true tails;
- `f(z(w))=w^9` tails on the `p=0` parity point matching `nu=-(11/729) x3 x5^3`, `r8=-x5^5/486`;
- scaling weights at `lambda=2`, and the exact `nu=2/9 -> 1` transport `B=12 z^2 -> 54 Z^2` for `f=z^9-1`;
- `Norm(f^4)=Norm(f)^4`;
- parity remainders and a `432`-term nonzero `W0`;
- leaf samples of types 2, 3, 4, `s=0` with `W0!=0`, and `Norm(F)=0`.

Targeted identities passed; none failed.

---

## Non-blocking remarks

1. The fibre compiler has no completed different-model review. Tails used as evidence were rebuilt from the reviewed binomial and `f(z(w))=w^9`. A post-hoc comparison with the pinned parent matches and is not evidence.
2. On `U`, parity is contained in leaf 1 union leaf 3, not in leaf 3 alone. The registered control is `E=0`, which holds. No numbered claim asserted a stricter containment.
3. `B`-meets-`g` (`Norm(G)=0`) is not split out as a fifth closed stratum. On `U` it sits in leaf 3 or leaf 4 according as `E` vanishes. The firewall would forbid it on a trajectory; this checkpoint does not empty it.
4. The `nu=1` chart over `Q` need not contain a given `Q`-point of `r6=nu` (the `p=0` parity point has `nu=25344`, not an 18th power in `Q`). Over `C` the scaling exists. The coefficient scheme of this case is the ambient ring of that chart.
5. The replay is a correct regression of hashes, abstract identities, and the parity remainders. Absence of a Sylvester check in-replay is not a mathematical gap: the resultant comparison was re-derived independently.

---

## What this does not license

This review does not license: emptiness of any residual leaf; application of the coprimality firewall; Taylor-boundary reconstruction; terminal dynamics; other invariant loads; the order-one core; all `(9,12)`; maximum-twelve automorphy; a counterexample; or JC2.

---

**Verdict.** `CONFIRMED`
