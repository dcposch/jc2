# Hostile different-model review — Q8 leaf-4 local quotient and terminal descent

| Field | Value |
|---|---|
| Claim under review | Frozen producer: at every loaded `Q8` contact, the Kummer-fixed quantities `theta=a0^2/p^9`, `pi=p^9`, `q=r8/p^{10}`, `S=r8^9=pi^{10} q^9`, and the root-free Hurwitz pair `tau`, `Delta` are well-defined without a chosen critical root; `Delta`, `tau`, `q`, and `S` are étale local coordinates on the parity-involution quotient of the second formal branch; `dS/dDelta` is a unit; the terminal row descends necessarily to `h^3 (S')^9=j^9 S^8`. The parity formula `r6=p^9 R6(v)` fails by a unit times `t^2` off parity and is not consumed. Formal-local coefficient-fibre descent only |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking: characteristic not `2` or `3` is the ambient involution / Faber / Kummer setting; `j≠0` and `u≠0` are the frozen Keller/Faber nonvanishing used to retain `9 r8'=j/u`; the order-three fibre compiler has no completed different-model review and is consumed only as the engine producing the eight tails; the frozen parent normalization jet remains producer-tier except for the coefficient claims re-derived here) |
| Evidence tier | independent re-solve of the seven-row `3 x 3` tangent plus affine `7 x 7` truncation over `E=Q[v]/(Q8)`; independent pair-norm reconstruction of `C(T)` and of `disc_T C=4 s E^2` on the jet; Euclidean unit certificates for every named denominator and every named `theta`-derivative at all eight contacts; positive and negative controls on `p^9 R6(v)-nu`; integer Kummer/weight and terminal-exponent ledger; unmodified registered replay as regression only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Charged ancestor | reviewed genuine `Q8` seven-row formal branch; reviewed unordered critical-value norm; frozen producer-tier `Q8` normalization/Taylor/terminal jet (arithmetic engine and parent pin only; jet coefficients re-derived). Reviewed genus-five `R6` formula used solely as the negative-control rational function |
| Git HEAD at close | `2e6104a417cfe15a93a901aa0a9129094a2ae11b` (`Promote max12 DZ20 exclusion and source audits`). Named producer artifacts for this case are untracked on top of that HEAD; charged hashes below are unchanged |
| Review window (UTC) | `2026-08-24T22:08:17Z` – `2026-08-24T22:15:00Z` |
| Python | CPython 3.14.6, stdlib only (registered replay and independent reconstruction) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer, case, and only the frozen parents pinned by the case replay (together with the reviewed theorems those parents name) reread in full before any verdict:

- `xmodel/max12-912-order3-nu-q8-leaf4-descent-jet-20260824.md`
- `cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/{REGISTRATION.md,README.md,replay.py,replay.json,MANIFEST.sha256,FREEZE.txt}`
- `xmodel/max12-912-order3-nu-q8-normalization-jet-20260824.md` and `cases/max12_912_order3_nu_q8_normalization_jet_20260824/` (frozen producer parent pinned by SHA-256)
- `xmodel/max12-912-order3-nu-q8-formal-branch-20260824.md` and `xmodel/max12-912-order3-nu-q8-formal-branch-review-grok-20260824.md`
- `xmodel/max12-912-order3-critical-value-norm-20260824.md` and `xmodel/max12-912-order3-critical-value-norm-review-grok-20260824.md`
- `xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md` and `xmodel/max12-912-order3-nu-parity-genus5-review-grok-20260824.md` (licensed only for the parity chart and the rational function `R6(v)`)

No producer, case, canonical, coordination, prompt, log, run, or other review file was edited. No AWS call was made. Independent reconstruction lived only in `/tmp`.

---

## Promotion

**Accept `AT EVERY LOADED Q8 CONTACT THE ROOT-FREE HURWITZ PAIR AND THE INVARIANT TAIL QUOTIENT ARE ETALE LOCAL COORDINATES ON THE PARITY-INVOLUTION QUOTIENT OF THE SECOND FORMAL BRANCH, AND THE TERMINAL ROW DESCENDS NECESSARILY TO h^3 (S')^9 = j^9 S^8` at the stated scopes.**

- On the chart `p≠0`, the integer weights are `wt(a0)=9`, `wt(p)=2`, `wt(r8)=20`. The four quantities `theta=a0^2/p^9`, `pi=p^9`, `q=r8/p^{10}`, `S=r8^9` have order-three Kummer character zero and are free of a ninth or tenth root. The identity `S=pi^{10} q^9` is algebraic on `p≠0` and does not use a parity formula for `pi`.
- Extending the reviewed rational function `R6(v)` along the corrected second branch gives `p^9 R6(v)-nu = c t^2+O(t^4)` with `c` a unit of `E`. The constant term vanishes (parity positive control). The tempting substitution `pi=nu/R6(v)` is therefore false at the first nontrivial order, uniformly over all eight conjugates, and is not used.
- Reducing `F=f^4` and `G=g^3` modulo `z^2-s` without choosing a Wronskian root produces `tau=-C1/C2` and `Delta=disc_T C / C2^2`, which expand to the displayed formulae `(4.1)`. On the jet, `C1^2-4 C0 C2 = 4 s E^2` holds coefficientwise. The denominators `s`, `Norm(F)`, `Norm(W)` and the linear coefficient of `E` are units of `E`.
- In the `p=1` chart one has `theta=t^2+O(t^4)`. The `t^2` coefficients of `Delta`, `tau`, `q`, and `S` are units, as is `S1/D1`. `Delta` vanishes at the node and is even in `t`, so it is an étale local parameter on the parity-involution quotient. The same derivative test makes `tau`, `q`, and `S` étale local coordinates there.
- From `9 r8'=j/u`, `r8=u^2 R`, `u^3=h` one has `S'=j h^5 R^8` and `S=h^6 R^9`, hence `h^3 (S')^9=j^9 S^8`. This is a necessary identity, not a converse reconstruction of `r8`. Because `dS/dDelta` is a unit at each contact, the unknown `S` may be replaced by `Delta` in that necessary identity at the node; `h` remains.

**Do not promote this to:** a global leaf-4 quotient curve; an algebraic relation among `Delta`, `tau`, `S`, and the Taylor center; a closed ODE in `Delta` alone; a Taylor-center determination of `R0=r/u`; algebraization or rationalization of the punctured branch; a finite-place or infinite-place exclusion; all `(9,12)`; maximum twelve; a counterexample; or JC2.

**Smallest valid successor.** Compute the algebraic relation among `Delta`, `tau`, `S`, and the descended Taylor center on the global leaf-4 quotient, then its projective boundary/genus, then `(5.3)`. Do not open a generic coefficient rectangle or AWS. Do not treat the formal quotient coordinates as a trajectory.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a characteristic-zero Keller pair of type `(9,12)`, produces a global leaf-4 quotient, determines the rational center `R0`, empties the punctured branch, or closes maximum twelve. Producer replay output was not used as evidence of the units, the discriminant identity, the `R6` defect, or the terminal exponents. Those were re-derived over `E`. The reviewed formal-branch theorem is consumed only for the existence of the second reduced smooth non-parity formal curve, the genuine chart numerator `1+3v`, and the coprimeness of `Q8` to `v`, `A2`, `D`, `A5`, and `Q8'`. The reviewed critical-value-norm theorem is consumed only for the pair-norm `C(T)` and the identity `disc_T C=4 s E^2`, both of which are re-expanded on this jet. The reviewed genus-five theorem is consumed only for the parity chart at `t=0` and for the rational function `R6(v)` as a negative control. The frozen parent normalization jet is consumed only as the arithmetic engine (`NF`, `Series`, `qseries_*`, fibre compiler) and as a SHA-256 pin; its Taylor families, finite-contact valuation, and `p0`-restoration via `R6(v0)` are not used. The fibre compiler is not a reviewed theorem.

---

## Scope (not enlarged)

Formal-local Kummer and parity-involution descent of the second `Q8` coefficient branch at the eight contacts, together with the necessary terminal identity `(5.3)`. Global quotient geometry, Taylor polynomiality, punctured-trajectory exclusion, all `(9,12)`, maximum twelve, a counterexample, and JC2 remain out of scope. The present confirmation stays inside that scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | `theta=a0^2/p^9`, `pi=p^9`, `q=r8/p^{10}`, `S=r8^9=pi^{10} q^9` have Kummer character zero, avoid a ninth or tenth root, and (along an actual order-three trajectory) lie in `K=C(x)`. `S=pi^{10} q^9` is algebraic off parity | **CONFIRMED** | a hidden ninth or tenth root; character of `r8` or `p` other than `2`; `S` failing to equal `pi^{10} q^9` as series; `pi` replaced by `nu/R6(v)` |
| 2 | On the second branch, `p^9 R6(v)-nu=c t^2+O(t^4)` with `c` a unit of `E`; the identity `r6=p^9 R6(v)` is parity-only and is not used off parity | **CONFIRMED** | vanishing of the `t^2` defect at a `Q8` root; a nonzero constant term (formula already wrong on parity); any later formula substituting `pi=nu/R6(v)` |
| 3 | `tau=2(G0 F0-s G1 F1)/Norm(F)` and `Delta=4 s E^2/Norm(F)^2` are root-free; `s`, `Norm(F)`, `Norm(W)`, and `E/t` are units at every `Q8` contact; `D1`, `T1`, `Q1`, `S0`, `S1` are units | **CONFIRMED** | a chosen square root of `s` in the charged formulae; `Norm(F)` or `s` sharing a root with `Q8`; a named `theta`-derivative sharing a root with `Q8`; `disc_T C ≠ 4 s E^2` on the jet |
| 4 | `Delta` is an étale local coordinate on the parity-involution quotient of the second branch at each `Q8` contact; `dS/dDelta` is a unit there | **CONFIRMED** | `Delta` odd in `t`; `Delta(node)≠0`; `D1` or `S1/D1` not a unit; the quotient map identified with the Kummer cover rather than `t |-> -t` |
| 5 | `9 r8'=j/u`, `r8=u^2 R`, `u^3=h` imply `S'=j h^5 R^8` and `h^3 (S')^9=j^9 S^8` as a necessary identity, not a converse | **CONFIRMED** | a wrong exponent in `r8^8/u=h^5 R^8` or in `S=h^6 R^9`; a hidden reconstruction of `r8` from `(5.3)`; a fibre-level differential identity claimed in place of a trajectory-level necessary condition |
| 6 | Numbered claims stay inside formal-local coefficient-fibre descent. No global quotient, Taylor constraint, algebraization, converse, or punctured-trajectory exclusion is registered | **CONFIRMED** | a charged artifact computing a global leaf-4 curve; a determination of `R0=r/u`; an exclusion of the punctured branch; a JC2 or maximum-twelve sentence in the report, registration, FREEZE, README, or replay payload |
| 7 | The chart uses the genuine numerator `1+3v`; no `Q12` descendant is imported; `R6` appears only as the negative control | **CONFIRMED** | a `1/3` substitution in `x1`; a SHA-256 pin of a quarantined `Q12` artifact; off-parity use of `r6=p^9 R6(v)` as an equation of the second branch |

All remarks below are non-blocking unless marked otherwise. None changes a numbered verdict.

---

## Hashes and replay (regression only)

Recomputed SHA-256 on the working-tree bytes match the launch prompt, `MANIFEST.sha256`, and `FREEZE.txt`:

| Artifact | SHA-256 | Cross-check |
|---|---|---|
| `xmodel/max12-912-order3-nu-q8-leaf4-descent-jet-20260824.md` | `b835aa0370b69e508ed776e1c9e0008f1186c751e537b63506619a7c43e95738` | prompt, `MANIFEST`, `FREEZE` |
| `cases/…/REGISTRATION.md` | `5d589920d43f5599a452aa64df654a4d9d9c1f0684db5339119e3849697da0cc` | `MANIFEST`, `FREEZE` |
| `cases/…/README.md` | `e0e55ae6362deba5a89e081837afacc18ff49d25fabadcff95fdfa9c1c8a5284` | `MANIFEST`, `FREEZE` |
| `cases/…/replay.py` | `5dcb0a67d79859c04d83d2c20ff8518a148a78c1229f42b00169c5842d5e7256` | `MANIFEST`, `FREEZE` |
| `cases/…/replay.json` | `dac9fda20ed7e50e2740b3d87466a11b323e4bf75515c704da6cf01922d8ae5e` | `MANIFEST`, `FREEZE` |
| `cases/…/MANIFEST.sha256` | `0b9b3f7176e337db4d4068b06d96bca60279889561dc654748a4bcfbe8e058d6` | prompt, `FREEZE` |
| `cases/…/FREEZE.txt` | `700ddb29d01de5075de3f5a4f7cc2df00f8b35aa6a59803e778ee3c87edb7de2` | prompt only |

Pinned parent (the normalization jet) recomputed, used as an arithmetic engine and SHA-256 pin, not as mathematical evidence of the new units:

| Artifact | SHA-256 |
|---|---|
| `xmodel/max12-912-order3-nu-q8-normalization-jet-20260824.md` | `739fbad475bc10540756c7a0180168185523f6e3cfe368225e03efa1abe62d65` |
| `cases/max12_912_order3_nu_q8_normalization_jet_20260824/replay.py` | `5536f16ac30da115021835d1a07c3116d7b1cb6675e628726dcfe766533528df` |
| `cases/max12_912_order3_nu_q8_normalization_jet_20260824/replay.json` | `bbb9316eb207305400b141dadd27d94fd8fece766ae5d333190ec9f42da5b313` |
| `cases/max12_912_order3_nu_q8_normalization_jet_20260824/MANIFEST.sha256` | `036b8656ba53dd3b1b212b2bf5bec6d0eed83f8a56023cf3ebf0b689156d8971` |
| `cases/max12_912_order3_nu_q8_normalization_jet_20260824/FREEZE.txt` | `807ad9dacbc477972c3c30b3770d84ca27340b5771ec2aad3efc90d7eb3e5b50` |

Reviewed ancestors recomputed, not used beyond the licensed inputs named above:

| Artifact | SHA-256 |
|---|---|
| `xmodel/max12-912-order3-nu-q8-formal-branch-20260824.md` | `37ce842eece0e79f0768bdfd492be70905bb83ba62af93965b4c4a2a3d6f03a3` |
| `xmodel/max12-912-order3-nu-q8-formal-branch-review-grok-20260824.md` | `32750e4e350919d7d52984feab06d3cd2d801386caec5848f7c5750bf9e8e846` |
| `xmodel/max12-912-order3-critical-value-norm-20260824.md` | `7339478798e00894c7b975c60aca821ec7ff2da383ffe5165a93cfa361bb6cb6` |
| `xmodel/max12-912-order3-critical-value-norm-review-grok-20260824.md` | `b6ae9516430073e177a5174684109b437ab278fa04dd066686c58af57715588e` |
| `xmodel/max12-912-order3-nu-parity-genus5-exclusion-20260824.md` | `f37376c96ab7e3c6ed7aa554dd04e2c72c9b2f5092ba6df03f524ea44765515d` |
| `xmodel/max12-912-order3-nu-parity-genus5-review-grok-20260824.md` | `903a973ac4975dfdeea77d143ebaa33cdc504d0f75d31dfe5327dad2d9be8528` |
| `cases/max12_912_order3_fibre_20260824/order3_fibre.py` | `a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf` |

The five SHA-256 pins inside `replay.py` match the parent-jet hashes above. `shasum -a 256 -c cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/MANIFEST.sha256` exits `0`. `python3 cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/replay.py | diff -u cases/max12_912_order3_nu_q8_leaf4_descent_jet_20260824/replay.json -` exits `0`. The replay re-solves the corrected jet from the original seven rows, checks `S=pi^{10} q^9`, Euclidean-certifies the `t^2` defect of `p^9 R6(v)-nu`, and records unit inverses for `D1`, `T1`, `Q1`, `S1`, and `S1/D1`. It does not impose a global quotient, does not invert `Delta` beyond the node, and does not differentiate `r8` as a function of `x`. It is regression only.

The case directory contains exactly the six freeze/manifest/readme/registration/replay files. No enumerator or AWS helper is present. The replay source contains no `Q12` polynomial, no `Q12` path pin, no square root, and no tenth or ninth root. The two occurrences of `Fraction(1, 3)` are `p=a7/3` and the summand `-p/3` in `s`, not the quarantined `x1` substitution.

---

## Claim 1 — Kummer descent of `theta`, `pi`, `q`, `S`

**CONFIRMED.** Needed hypothesis, stated: characteristic not `3`; along an actual order-three trajectory one has `u^3=h in C(x)` and `sigma(z)=zeta z`, so `sigma(a_i)=zeta^{-i} a_i`.

The geometric weights are `wt(z)=1`, `wt(a_i)=9-i`, hence `wt(a0)=9` and `wt(p)=wt(a7)=2`. The tail `T=w^{12}-g(z(w))` assigns `wt(r8)=20`. The Kummer character of a quantity of weight `w` is `w mod 3`. In particular `p` and `r8` both have character `2`, so `p=u^2 P` and `r8=u^2 R` with `P,R in K` along a trajectory. Then

```text
char(theta) = 2 char(a0) - 9 char(p) = 0 - 18 ≡ 0,
char(pi)    = 9 char(p) = 18 ≡ 0,
char(q)     = char(r8) - 10 char(p) = 2 - 20 ≡ 0,
char(S)     = 9 char(r8) = 18 ≡ 0.
```

No ninth root of `p` and no tenth root of `p` is taken: `pi` raises `p` to the ninth, `q` divides by `p^{10}`, `S` raises `r8` to the ninth. Explicitly `pi=p^9=u^{18} P^9=h^6 P^9 in K` and `S=r8^9=u^{18} R^9=h^6 R^9 in K` along a trajectory, without extracting `u` from `p` or from `r8`. The algebraic identity

```text
pi^{10} q^9 = (p^9)^{10} (r8/p^{10})^9 = r8^9 = S
```

holds on the chart `p≠0`, independently of parity. Independent series substitution on the corrected jet gives coefficientwise equality through `O(t^4)`.

Weight versus character. The producer claims Kummer *character* zero, not geometric weight zero, for all four. The weights are `wt(theta)=0`, `wt(q)=0`, `wt(pi)=18`, `wt(S)=180`. The last two still descend to `K` because the character vanishes. In the `p=1` local normalization, `p=1+P2 t^2+O(t^4)` yields `theta=t^2+O(t^4)` with `t^2`-coefficient `1`, matching `(2.2)`.

The replay payload phrase `"field": "all six coordinates are in K=C(x)"` omits the trajectory qualifier present in §2. On the coefficient fibre the six quantities are elements of `E[[t]]/(t^4)`. They lie in `K` only along an actual order-three trajectory. The report, registration, README, and FREEZE all keep that scope. Non-blocking.

---

## Claim 2 — parity-formula negative control

**CONFIRMED.**

On the parity chart `q=x0=x2=x4=0` with `p x5 A≠0`, the reviewed genus-five calculation gives

```text
R6(v) = -2304 v^6 A2(v)^3 A5(v) / D(v)^4,
A2=3v^2+3v+1,   D=3v^2-2,
A5=33v^5+117v^4+131v^3+69v^2+18v+2,
```

and `r6=p^9 R6(v)`. Independently, `gcd(Q8,v)=gcd(Q8,A2)=gcd(Q8,D)=gcd(Q8,A5)=gcd(Q8,Q8')=1`, so every `Q8` root is a loaded parity contact and `R6(v0)` is a unit of `E`.

The invariant `v=x3/(p x5)-2` is the same rational function off parity. Extending it along the second branch (even series, `v(0)=v0`) and substituting the reviewed `R6` produces a defect `pi R6(v)-nu`. Positive control at the node: the constant term vanishes, so the formula is correct on parity. Odd coefficients vanish by the involution. The `t^2` coefficient is a unit of `E`:

```text
sha256(c) = acbf2d9d456901e47644a63a1ad632fbbc0e50bf7c6ede3fb1ff2167e67e99b0,
gcd(c, Q8)=1,
```

with a recorded Euclidean inverse. Thus `p^9 R6(v)=nu` fails at order `t^2`, uniformly over all eight conjugates. No later formula uses `pi=nu/R6(v)`. Away from parity, `pi=p^9` is retained as its own character-zero coordinate.

Source-level: `R6` occurs in `replay.py` only inside this negative control and its payload description. `R8(v)` is not referenced. The parent jet's restoration `p0^9 R6(v0)=nu` is a parity-node identity and is not imported.

---

## Claim 3 — root-free `tau`, `Delta`; denominators; unit jets

**CONFIRMED.** Needed hypothesis, stated: characteristic not `2`; work on the seven-row landing so that the Wronskian is the quadratic `B=54 nu (z^2-s)` with `s=-p/3-10 r8/(9 nu)`. The charged formulae do *not* scale `nu` to `1`; they use this general-`nu` center. That is the correct covariance: vanishing of `s`, `E`, `Norm(F)`, `Norm(W)` is unchanged by the constant scaling `lambda^{18}=1/nu`.

In the quadratic algebra `z^2=s`, write `F=f^4=F0+F1 z` and `G=g^3=G0+G1 z`. The pair reduction replaces `z^{2k}` by `s^k` and `z^{2k+1}` by `s^k z`; it does not choose a square root of `s`. Then

```text
C(T)=Norm(G-T F)=C0+C1 T+C2 T^2,
C0=G0^2-s G1^2,   C1=-2(G0 F0-s G1 F1),   C2=F0^2-s F1^2=Norm(F),
E=G0 F1-G1 F0.
```

The unordered critical values are the roots of `C(T)=0`, so

```text
tau = beta_+ + beta_- = -C1/C2 = 2(G0 F0-s G1 F1)/Norm(F),
Delta = (beta_+-beta_-)^2 = (C1^2-4 C0 C2)/C2^2 = 4 s E^2 / Norm(F)^2.
```

These are the formulae `(4.1)`. Both have geometric weight zero because `beta=g^3/f^4` does. Independent substitution on the corrected jet gives coefficientwise equality of `C1^2-4 C0 C2` with `4 s E^2`, and of the two writings of `tau` and of `Delta`.

Even/odd typing through `O(t^4)`, forced by the involution and re-checked as identities, not as truncation accidents:

```text
F0, G0, C0, C1, C2, s, Norm(W), tau, Delta, q, S, pi, theta, v, p, r8  even,
F1, G1, E, a0, a2, a4, a6                                               odd.
```

In particular `E=e1 t+O(t^3)` with `e1` a unit, so `Delta` has valuation two in `t` and is a function of `theta`. Denominator and leaf-typing units, all Euclidean `gcd=1` against `Q8`:

| residue | role | `sha256` | unit |
|---|---|---|---|
| `s0` | Wronskian center | `ee22f38eb836c7fbc56a5a7d50aa24503c5a6de323ecfefeced3fa88d2d151cf` | yes |
| `nF0` | `Norm(F)` at the node | `2f3665c3c64380ebe340a52c30bee34a6f1aab1c9cf2ac33786066423b6b3cf9` | yes |
| `nW0` | `Norm(W)` at the node | `0e804599725c3dd5e117a231490df85f1ff8730d537da072471d6b7165c5108f` | yes |
| `e1` | `[t^1]E` | `c289f3c14b0c9402cf78db10e71a4f4ce0e0c42d5f231e1e7e0c7f39726f248d` | yes |

Thus the node is in reviewed leaf 3 (`s Norm(F) Norm(W)≠0`, `E=0`) and the punctured jet is in reviewed leaf 4 (`E/t` a unit). Chart denominators `v0`, `D0`, `A2(v0)`, `x5(v0)` are likewise units; the `x1` formula uses `(3v+1)/(9v)`, which is distinct from the quarantined constant `1/3`.

Because `theta=t^2+O(t^4)` with leading coefficient `1` at `p=1`, the derivative `d/dtheta` at the node equals the `t^2` coefficient. Those coefficients, and `S0`, are units:

```text
sha256(D1)=2c651a6265e650c5d72f409a46bb6fe3c572e2c51518ae9794f3b9b06dc9209e,
sha256(T1)=2011e1ea82ba014d14037329b91f2571f99199215d30314156c6d625614000fe,
sha256(Q1)=87b80678a4a92f8e768bc4cd4f118a425bc797cef61f720392e0ae8a716590cc,
sha256(S1)=30caa5eebba929de017fa52461483c602e14800541c1a308357186f70df4a2a3,
sha256(S0)=7011688d46fa49ae29c6e6bdd4128eb8ea6a5118bdcdf036434ee010e2e8d357,
sha256(S1/D1)=386a59430805c0e74525cd485750c7267761ceef04153848e28b57002b297c15.
```

Each of `D1`, `T1`, `Q1`, `S1`, `S1/D1` has a recorded Euclidean inverse modulo `Q8`. `S0` is certified by `gcd(S0,Q8)=1` (equivalently, `rho0` is a unit and `S0=rho0^9`). `Delta`'s constant term is zero, as required for a local parameter vanishing at the node. Squarefreeness `gcd(Q8,Q8')=1` converts each `gcd=1` certificate into nonvanishing at all eight distinct complex contacts.

The truncation `E[[t]]/(t^4)` cannot see `O(theta^2)=O(t^4)`. The derivative test at the node does not need that term. Non-blocking.

---

## Claim 4 — `Delta` étale on the involution quotient; `dS/dDelta` a unit

**CONFIRMED.**

Two distinct actions are in play. Kummer `Gal(K(u)/K)` of order three is already fixed by Claim 1. The parity involution `f(z) |-> -f(-z)` acts by `t=a0 |-> -t`. The second formal branch is a formal curve in `t` with even invariant functions and odd anti-invariant functions. Its quotient is the formal disc in `theta` (equivalently in `t^2`).

`Delta` is even, vanishes at `t=0`, and has `dDelta/dtheta |_{theta=0}=D1` a unit of `E`. Formal inverse-function theorem over the field `E` (or, after any embedding `E -> C`, at each of the eight contacts) makes `Delta` an étale local parameter on that quotient at the node. The same test, after translating by the unit constants `tau0`, `q0`, `S0`, makes `tau`, `q`, and `S` étale local coordinates there. The chain rule gives `dS/dDelta=S1/D1`, a unit, so `S` and `Delta` are étale-equivalent local coordinates at the node.

This is formal-local étale-ness at the eight `Q8` contacts. It is not étaleness of a global map from a leaf-4 quotient curve to the `Delta`-line, and it is not a statement along the punctured branch away from the node. The report's sentence "this is the precise sense in which the generic leaf-4 motion descends without selecting a critical root" is licensed only in that local sense: the unordered pair `(tau,Delta)` is well-defined on the quotient, and `Delta` is a local parameter there.

---

## Claim 5 — terminal descent `h^3 (S')^9=j^9 S^8`

**CONFIRMED.** Needed hypotheses, stated: the original Faber terminal row `9 r8'=j/u` with `j in C^*` and `u≠0`; Kummer `u^3=h`; character-two descent `r8=u^2 R` with `R in K`, along an actual trajectory. Characteristic not `3`.

Differentiating `S=r8^9` and substituting the terminal row:

```text
S' = 9 r8^8 r8' = j r8^8 / u.
```

Then `r8=u^2 R` gives `r8^8/u = u^{16} R^8 / u = u^{15} R^8 = h^5 R^8`, hence `S'=j h^5 R^8`. Independently `S=u^{18} R^9=h^6 R^9`. Raising the first identity to the ninth power:

```text
(S')^9 = j^9 h^{45} R^{72},
h^3 (S')^9 = j^9 h^{48} R^{72} = j^9 (h^6 R^9)^8 = j^9 S^8.
```

Equivalently `(S')^9 = j^9 S^8 / u^9` and `u^9=h^3`. Every exponent is an integer identity (`8*2-1=15=5*3`, `9*8=72`, `u^9=h^3`, `wt(S)=180≡0 mod 3`). No ninth root is extracted.

The identity is a necessary consequence of `(5.1)` along a trajectory whose jet lies on this formal branch. It is not a coefficient-fibre differential equation (the fibre has no `d/dx`), not a converse reconstructing `r8` from `S`, and not a closed ODE in `Delta` alone: `h` remains as an element of `K`. Because `dS/dDelta` is a unit at each contact, the formal inverse-function theorem lets one rewrite the left-hand side in terms of `Delta'` at the node, with `h` still present. That is the precise content of the report's parenthetical that `(5.3)` is locally a differential equation in `Delta`. Section 6 correctly defers the global relation among `Delta`, `tau`, `S`, and the Taylor center, and then `(5.3)`, as the remaining gate.

---

## Claim 6 — no trajectory / converse / algebraization / Taylor / global-quotient overclaim

**CONFIRMED.**

Charged artifacts were read for promotion language. Report §1 and §6, the registration, the README, and the FREEZE all state that the conclusion is formal-local at the eight `Q8` contacts; that no global leaf-4 quotient is computed; that the high-row fibre does not determine `R0=r/u`; and that nothing here excludes the punctured branch, a disjoint component, all `(9,12)`, maximum twelve, a counterexample, or JC2. The FREEZE verdict is exactly the local étale-ness plus the necessary identity `(5.3)`.

Places where a confusion could have been introduced, and was not in a numbered claim:

- `S=pi^{10} q^9` is an algebraic coefficient identity, not a trajectory.
- `p^9 R6(v)=nu` is a parity-chart identity; its failure off parity is the negative control, not a new equation of the second branch.
- `tau` and `Delta` are functions on the coefficient jet; they become elements of `K` only along a trajectory.
- Étale-ness of `Delta` is at the node of the formal quotient, not a global coordinate on a projective model.
- `(5.3)` is necessary, not converse, and is not used to constrain the Taylor center.
- The parent finite-contact valuation (an actual trajectory cannot meet the node at a finite `x`-place) is not consumed and is not re-proved.

The Taylor families of the parent jet remain charged. The present report correctly records that writing `r=u R0` makes them descend coefficientwise without determining `R0`.

---

## Claim 7 — genuine chart; no `Q12`; no illicit `R6`

**CONFIRMED.**

The node is built from the reviewed genus-five chart with polynomial numerator `1+3v`. Independent comparison: `(3v0+1)/(9v0)` is not the element `1/3` of `E`. The second-branch reconstruction uses the pinned seven-row tails and Gaussian elimination; it does not impose `r6=p^9 R6(v)` off parity. No charged path pin of a quarantined `Q12` artifact exists in this case or in the parent jet's dependency ledger.

---

## Independent reconstruction (not the producer replay)

Scratch lived in `/tmp` and is not in the bank. Using the frozen parent arithmetic engine (`NF`, `Series`, fibre compiler, pair reduction) but not treating `replay.json` as evidence, it re-derived:

- the `3 x 3` odd tangent and the affine `7 x 7` truncation, with exact residual zero (the map in the unknowns is affine inside `E[[t]]/(t^4)`, so the Gaussian solution is an exact jet, not a linear approximation);
- even/odd typing of all displayed series through `t^3`;
- `S=pi^{10} q^9` coefficientwise;
- `C(T)` from the pairs, `disc_T C=4 s E^2` coefficientwise, and both writings of `tau` and `Delta`;
- Euclidean units for `v0`, `D0`, `A2(v0)`, `x5(v0)`, `nu`, `rho0`, `s0`, `nF0`, `nW0`, `e1`, `D1`, `T1`, `Q1`, `S0`, `S1`, `S1/D1`, and the `t^2` `R6`-defect;
- positive control `p^9 R6(v0)=nu` and negative control at order `t^2`;
- genuine `1+3v` versus quarantined `1/3`;
- Kummer/weight and terminal-exponent ledgers;
- exact match of every named SHA-256 in the charged report and in `replay.json`.

Targeted identities passed; none failed. The fibre compiler and `F_12` were not rebuilt from the binomial in this review; they are the same pinned engine already used as a non-theorem in the formal-branch and critical-value-norm reviews.

---

## Non-blocking remarks

1. The frozen parent normalization jet is still producer-tier. This review re-derives the second-branch 2-jet, the leaf-typing units `s0`, `nF0`, `nW0`, `e1`, and the new quotient units. It does not confirm the parent's Taylor-family hashes, the `z=0` negative control, or the finite-place node exclusion.
2. The fibre compiler has no completed different-model review. Tails used as evidence are those of the pinned Faber engine, as in the formal-branch review.
3. Characteristic not `2` or `3` is the ambient involution / Faber inverse-root / Kummer setting. The factors `9` and `2` in the terminal row and in `tau`, `Delta` need it.
4. `pi` and `S` have Kummer character zero but nonzero geometric weight. A reader who converts the user's "weight zero" prompt into a producer claim will misread §2. The producer wrote character zero.
5. The replay payload field `"all six coordinates are in K=C(x)"` is sloppy. The report's qualifier "along any actual order-three trajectory" is the correct statement.
6. `(5.3)` is not a closed ODE in `Delta`: `h in K` remains. The report does not claim otherwise as a numbered identity.
7. `MANIFEST.sha256` does not list `FREEZE.txt`. The freeze file names the five digests it needs. Bookkeeping only.
8. Constants in `replay.json` record `unit_mod_Q8` by gcd, without serializing an inverse polynomial. Existence of the inverse is the Euclidean gcd, which was re-run.

None of these remarks changes a numbered verdict.

---

## What this does not license

This review does not license: a global leaf-4 quotient curve; an algebraic relation among `Delta`, `tau`, `S`, and the Taylor center; a closed differential equation in `Delta` alone; determination of `R0=r/u`; algebraization or rationalization of the punctured branch; a finite-place or infinite-place exclusion; pullback of the parent Taylor families as polynomiality constraints; all `(9,12)`; maximum-twelve automorphy; a counterexample; or JC2. It also does not license substituting `r6=p^9 R6(v)` off parity, choosing a Wronskian root, or extracting a ninth root of `p` or of `r8`.

---

**Verdict.** `CONFIRMED`
