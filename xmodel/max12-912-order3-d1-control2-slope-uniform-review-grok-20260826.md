# Hostile text-only review — control-2 slope-uniform tropical obstruction

| Field | Value |
|---|---|
| Claim under review | After `s=1`, the frozen eight-term `W` lies in the exact unhomogenized nine-generator control-2 ideal `J`, and least-weight reweighting of this same `W` yields `Lambda^20 ∈ in_w(J)` uniformly on the strict face `alpha=15/2`, `5<beta<6`, for every positive split `L=3T+H` |
| Overall verdict | **CONFIRMED** for the exact fixed-cubic, fixed-load, five-coefficient-support theorem. Membership of `W` is a certificate replay of a frozen LPDP identity, not a new derivation of `W` or of the eight rows. The slope-uniform step is elementary finite-support arithmetic on that fixed polynomial |
| Smallest failing identity | none in the frozen target, the literal r6d replay, or the hand weight/mapping arithmetic |
| Smallest missing hypothesis for a stronger theorem | equality face `beta=5`; endpoints; `beta>6` as a control-2 statement; moving axis; nonzero `q2`; moving `k,mu,nu`; another support; the tied `alpha=2 beta` chart; control-1 / other Newton branches; a full Gröbner cone or double-root fan; D1; JC2 |
| Evidence tier | SHA-256 of the charged target and four freezes; nested freeze verification; text identity of the nine replay generators against frozen encoding B; hand dehomogenization of printed `TAIL`; hand weights, halfspace collapse, and control-2 window arithmetic. No local Singular, Lean, Sage, Python algebra, or other computational replay |
| Reviewer / model | Grok 4.6 (xAI). Text-only tropical / commutative-algebra referee. Independent of the producer status line and of any prior mapping-review attempt |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `574e873d4753b57dbaeb0fb83e320fbef3694724` |
| Host | Darwin. Singular, Lean, Sage, and every solver were not run |

## What was and was not run

No local substantive computation was run. In particular this review did **not** execute Singular, Lean, Sage, msolve, Gfan, or Python algebra. Hashes were checked with `shasum -a 256` and `shasum -a 256 -c`. Git identity was read with `git rev-parse`. The nine `poly E1,…,E8,LT` bodies in the harvested replay source were compared as text to frozen encoding B; they are identical. AWS streams were read as already-emitted text. Hand arithmetic is recorded under charges 1–5.

The producer status line (“focused hostile mapping/firewall review pending”) was ignored as a verdict. A prior Claude lane produced no mathematical finding; nothing is inherited from it.

Charged target and evidence SHA-256, recomputed and matched:

```text
b6349549a115a44ac8534d7801a15fa7e3f8c7a8211cce69ce723cd019301a49
  xmodel/max12-912-order3-d1-double-root-control2-slope-uniform-obstruction-20260826.md
04cd09886ed78e1af48a6387ee2c67996856d2b6f59791963450e7e4380e32a3
  cases/max12_912_order3_d1_double_root_control2_la20_syzygy_v2_20260826/WITNESS_FREEZE.sha256
616628e959c6b458948bcf72102c46118e5e6c4c95165f0133e5324579a120ee
  cases/max12_912_order3_d1_double_root_control2_la20_witness_replay_v1_20260826/FREEZE.sha256
e4cc300ad4317a7a3807a67cf3d2e671ff9eefaf11a5cecd98b0b5e1f9f1abf5
  cases/max12_912_order3_d1_double_root_control2_la20_witness_replay_v1_20260826/RESULT.md
1fdddc051d8a7cdad2b6e250e4d9332897568cb9da436bfcb3c954dd2f35b297
  cases/max12_912_order3_d1_double_root_control2_la20_witness_replay_v1_20260826/aws_r6d/singular.stdout
```

Every path listed in both freeze files recomputed and matched from the respective case root. Nested identities used below also match, including harvested replay source `cba367e6c5aff8d199ef52f21a60152ee689d1fd5ca962fc8a349526f751b6a1`, frozen encoding B `c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b`, LPDP source `e9b2c1594460cc8a6053654f0fcd810522044c6b1ef89d6e92ec2fb0038fd894`, LPDP stdout `a0611ede0e667d45f569a954fdaa73818f0ebea328212b8c46d4ccb0aa29fe08`, `WITNESS_RESULT.md` `c4a2207bd5a67f819963eee1b579413372a1953c21bb24e31b72547d9be51bcd`, and the Newton-fan correction firewall `466736cdd1a76607e6475c98d9da4b55096e88813d911722954549bdcba702c0`. Empty compiler/CAS stderr and the hardened replay diagnostics file are the empty-string digest `e3b0c442…`. Both replay rc files are the two-byte string `"0\n"`, digest `9a271f2a…`.

Read in full before the verdict: the 124-line target; both freeze files and every nested path they list; replay `RESULT.md`, `compile_witness_replay.py`, `aws_r6d/witness_replay.sing`, and `aws_r6d/singular.stdout`; LPDP `WITNESS_RESULT.md`, `CONE_PREMISES_PROVISIONAL.md`, and the printed `FINAL`/`TAIL`/`DEHOMOGENIZED_WITNESS` block of `aws_r6d_LPDP/singular.stdout`; frozen `base_B.sing`; the Newton-fan correction firewall. No other xmodel review was used as a premise.

---

## Promotion

**Accept `FOR THE FROZEN DOUBLE-ROOT CUBIC K=(z-1)^2(z+2) WITH a=1, h=q2=k=nu=0, mu=2/3 AND SUPPORT Q=q1 z+q0, R=r2 z^2+r1 z+r0, LET J BE THE EXACT UNHOMOGENIZED NINE-GENERATOR IDEAL OBTAINED BY SETTING s=1 IN THE CHARGED EXPANDED CONTROL-2 REES GENERATORS (E1,…,E8, Lambda-tau^3 rho). THE LITERAL r6d REPLAY OF THE FROZEN LPDP CERTIFICATE PROVES THAT THE DISPLAYED EIGHT-TERM POLYNOMIAL W LIES IN J, WITH LEADING TARGET COEFFICIENT +1 ON Lambda^20. THIS IS CERTIFICATE REPLAY, NOT A NEW DERIVATION OF W OR OF THE EIGHT ROWS. FOR ANY RATIONAL L>0, T>0, H>0 AND RATIONAL beta>5, WITH L=3T+H AND WEIGHTS w(Lambda,tau,rho)=(L,T,H), w(q1)=w(q0)=beta L, w(r2)=w(r1)=w(r0)=(15/2) L, THE UNIQUE LEAST-WEIGHT TERM OF W IS Lambda^20. HENCE Lambda^20 LIES IN THE LEAST-WEIGHT INITIAL IDEAL in_w(J), THE AFFINE VARIETY V(in_w(J)) LIES IN {Lambda=0}, AND THE EIGHT-COORDINATE TORUS LOCALIZATION IS (1). BY THE VALUED-ARC LEMMA BELOW, THERE IS NO k[[t]]-POINT OF V(J) REALIZING THESE EXACT VALUATIONS WITH ALL EIGHT LEADING COEFFICIENTS NONZERO. IN PARTICULAR THE ENTIRE STRICT CONTROL-2 FACE alpha=15/2, 5<beta<6 IS EXCLUDED FOR THIS FIXED CUBIC, FIXED LOADS, AND DISPLAYED FIVE-COEFFICIENT SUPPORT, UNIFORMLY IN THE NONZERO LEADING RESIDUE AND IN THE POSITIVE SPLIT (T,H). THE SAMPLED RAMIFICATION (L,T,H; beta L; alpha L)=(4,1,1;22;30) IS THE SPECIAL CASE beta=11/2. NO EQUALITY FACE, ENDPOINT, MOVING AXIS, q2, OTHER SUPPORT, OTHER BRANCH, D1, OR JC2 STATEMENT IS LICENSED.`**

Do not promote this to: a new independent construction of `W`; Gröbner-basis continuity; a claim that `96` is minimal; emptiness of coordinate hyperplanes of `V(in_w(J))`; the face `beta=5`; `beta=6` or `beta>6` as control-2 geometry; moving axis or loads; nonzero `q2`; the tied chart `alpha=2 beta`; control-1; a full Newton fan; D1; or JC2.

Smallest repair / counterexample: none for the licensed theorem.

---

## Charge 1 — `W ∈ J`, coefficients, and `Lambda^20`; replay versus derivation

**CONFIRMED as certificate replay of a frozen polynomial identity. Not a new derivation of `W` or of the eight charged rows.**

The harvested replay source contains the nine expanded encoding-B generators, text-identical to frozen

```text
c905f1b507fda84f62950198bd9528718798c0498ee31e8cc7679479d677693b  base_B.sing
```

and hard-wires the LPDP multipliers and tail. The identity checked on r6d is

```text
s^96*la^20 - s^97*TAIL - sum_{i=1}^9 FINAL[i]*I[i] = 0
```

in `Q[s,la,tau,rho,q1,q0,r2,r1,r0]`, with `I=(E1,…,E8,LT)` those nine generators. The AWS stream prints `PASS_LITERAL_REES_IDENTITY` once, empty stderr, empty diagnostics, rc `0`. Printed `FINAL` matches the compiler source, including `FINAL[3]=FINAL[9]=0`. Printed `TAIL` is

```text
-1/243*s^7*q1*q0^3
-1/54*s*q1*r2*r1
-7/108*s*q1*r1^2
-1/54*s*q1*r2*r0
+1/54*s*q0*r1*r0
-1/108*s*q1*r0^2
-la^20*tau.
```

All `s`-exponents in `FINAL` and `TAIL` are nonnegative; no `s`-denominator is inverted. The ring homomorphism `s ↦ 1` therefore sends a combination of the nine Rees generators to a combination of the nine dehomogenized generators. The factor `s^96` becomes `1` and is not a leftover saturation condition on `J`.

Hand substitution: `la^20 - s*TAIL` expands to

```text
la^20
+ (1/243)*s^8*q1*q0^3
+ (1/54)*s^2*q1*r2*r1
+ (7/108)*s^2*q1*r1^2
+ (1/54)*s^2*q1*r2*r0
- (1/54)*s^2*q0*r1*r0
+ (1/108)*s^2*q1*r0^2
+ s*la^20*tau.
```

At `s=1` this is exactly the displayed `W` (and the AWS `WITNESS_BEGIN`/`DEHOMOGENIZED_WITNESS` line), including the minus on `q0*r1*r0` and coefficient `+1` on both `la^20*tau` and `la^20`. The exponent on `Lambda` is `20`, not a different target power. Clearing denominators `{1,243,54,108}` uses `lcm=2^2·3^5=972` and recovers the primitive integral representative printed in `WITNESS_RESULT.md`.

`J` in the target is this unhomogenized nine-generator ideal. Encoding B is the Rees expansion `φ_s` of the exact eight-row D1 coefficient system plus `Lambda-tau^3 rho`; `φ_{s=1}` is the identity, so `I|_{s=1}` is the exact unhomogenized finite ideal charged by the control-2 Rees package, not a proper initial-piece truncation.

Distinction the target blurs only stylistically, and which this review will not blur: the LPDP V2 run *discovered* the combination by saturation and lift. The r6d replay *checks* that printed combination by literal polynomial arithmetic, without recomputing `sat` or a Gröbner basis. The slope-uniform note consumes membership. It does not re-derive `W`, does not re-expand the eight D1 rows, and does not replace the certificate. Replay `RESULT.md` states this correctly; the membership claim is licensed by that PASS, not by a new independent syzygy.

---

## Charge 2 — term weights, least-versus-greatest, rational rescaling

**CONFIRMED. Unique least-weight term of `W` is `Lambda^20` exactly on the claimed open set, under the campaign’s least-weight convention.**

Write `w(Lambda,tau,rho)=(L,T,H)` and impose the control-2 ansatz `w(q1)=w(q0)=beta L`, `w(r_i)=(15/2) L`. The eight displayed monomials have weights

| term | coefficient | weight |
|---|---|---|
| `Lambda^20*tau` | `+1` | `20 L + T` |
| `Lambda^20` | `+1` | `20 L` |
| `q1*q0^3` | `1/243` | `4 beta L` |
| `q1*r2*r1` | `1/54` | `(beta+15) L` |
| `q1*r1^2` | `7/108` | `(beta+15) L` |
| `q1*r2*r0` | `1/54` | `(beta+15) L` |
| `q0*r1*r0` | `-1/54` | `(beta+15) L` |
| `q1*r0^2` | `1/108` | `(beta+15) L` |

All eight coefficients are nonzero in `Q`, so none is optional on the full support of `W`. No displayed term contains `rho`, so `H` does not enter the uniqueness inequalities. With `L>0` the non-target classes are strictly above `20 L` if and only if

```text
T > 0,
4 beta L > 20 L    ⇔    beta > 5,
(beta+15) L > 20 L ⇔    beta > 5.
```

Thus, given `L>0` and `T>0`, unique least-weight term `Lambda^20` if and only if `beta>5`. Both of the target’s “non-target classes” really do collapse to the same strict inequality. `H>0` is not used for uniqueness; it is used only to place the split in the interior of `Lambda=tau^3 rho` (charge 5).

The seven general halfspaces in `CONE_PREMISES_PROVISIONAL.md` specialize to exactly those inequalities under the equal-weight ansatz, and `H` remains unrestricted by this witness.

**Least versus greatest.** For a valued arc `x_i = a_i t^{w_i} + ⋯`, substitution into a polynomial sees the *lowest* power of `t`. The campaign `in_w` is that least-weight initial ideal. It is the same convention as the Rees construction `X_i ↦ s^{w_i} X_i`, then `s=0`. A Gröbner weight order that prefers *greatest* weight would pick `q1 q0^3` or `Lambda^20 tau` off this support, not `Lambda^20`; that is the wrong convention for the obstruction and is not used. The replay’s registered-weight enumeration

```text
WEIGHT_MULTISET=80x1,81x1,82x5,88x1
```

with unique weight-`80` monomial `la^20` is the least-weight check at the sample, not a `dp` leading-term claim.

**Sample and homogeneity.** At `(L,T,H)=(4,1,1)` and `beta=11/2`,

```text
20 L = 80,
20 L + T = 81,
4 beta L = 88,
(beta+15) L = 82,
```

margins `1,8,2,2,2,2,2`, matching the replay and the cone file. Positive rational rescaling of `(L,T,H)` multiplies every term weight by the same positive constant and does not change the least-weight monomial or the inequality `beta>5`. Any rational point of the open cone is a positive rational multiple of an integral weight, so the ramification `(4,1,1;22;30)` is representative, not an extra hypothesis.

At `beta=5` seven terms reach weight `20 L` (`Lambda^20`, `q1 q0^3`, and the five `q r r` terms); `Lambda^20 tau` stays strictly above if `T>0`. The witness is nonmonomial on that face. Agreed, and not claimed.

---

## Charge 3 — `W ∈ J ⇒ Lambda^20 ∈ in_w(J)`, torus localization, valued-arc lemma

**CONFIRMED for the least-weight initial ideal, as a witness-obstruction region, not as a Gröbner cone.**

One-polynomial lemma: if `W = A·Lambda^20 + ∑_{e ∈ S} B_e x^e ∈ J` with `A=1 ≠ 0` and `e·w > 20 L` for every other term of `W`, then the least-weight initial form of `W` is `Lambda^20`, hence `Lambda^20 ∈ in_w(J)`. Other elements of `J` may contribute further initial generators, including terms of weight below `20 L`; that cannot remove `in_w(W)` from `in_w(J)`. Constancy of a full reduced initial basis is not used.

Set-theoretically, `V(in_w(J)) ⊆ V(Lambda^20) = V(Lambda)` over a field. If `Lambda` is invertible, `Lambda^20` is a unit and the localization of `in_w(J)` is `(1)`. In particular the eight-coordinate torus

```text
(Lambda, tau, rho, q1, q0, r2, r1, r0) ∈ (k*)^8
```

is empty in `V(in_w(J))`. The relation `Lambda - tau^3 rho` is homogeneous of weight `L` on both sides once `L=3T+H`, so it does not cancel `Lambda^20`.

**Valued-arc / leading-coefficient lemma (the exact missing sentence).** Let `k` be a field of characteristic `0` and `φ: k[x]/J → k[[t]]` a `k`-algebra map. Write `v` for the `t`-adic valuation. If `v(φ(x_i)) = w_i` for each of the eight coordinates, with nonzero leading coefficients `a_i ∈ k`, then `a = (a_i)` lies in `V(in_w(J)) ∩ (k*)^8`. Proof: for every `f ∈ J` one has `f(φ)=0`, hence infinite valuation; if the least-weight form `in_w(f)` did not vanish at `a`, then `v(f(φ))` would equal that finite least weight. Applying this to `W` (or to any preimage of `Lambda^20` in `in_w(J)`) forces `a_Lambda^20 = 0`, hence `a_Lambda = 0`, a contradiction.

This is the only lemma needed to pass from `Lambda^20 ∈ in_w(J)` to exclusion of a control-2 arc in this finite-variable ring: a D1 arc of the displayed support is a `k[[t]]-point` of `V(J)`, and a control-2 leading jet with exact valuations `w` and all eight leading coefficients nonzero would be such a torus point. Higher `t`-terms of the same eight coordinates are invisible to `in_w` and cannot rescue a bad leading jet. The target’s “consequently the interval is excluded” is this lemma plus charge 5, scoped to the stated support. It is not a Gröbner-cone or Newton-fan completeness theorem.

---

## Charge 4 — `s=1` and reweighting at every rational slope

**CONFIRMED. No leftover saturation, homogenization, denominator, or discovery-order artifact.**

The Rees computation at `w=(4,1,1,22,22,30,30,30)` is used only to *find* a preimage. The checked identity is a polynomial identity in the nine original generators. After `s=1`:

- `φ_{s=1}` is the identity on the coefficient ring, so the generators of `J` are the exact unhomogenized eight rows plus `Lambda-tau^3 rho`, independent of the discovery weight;
- `s^96` and `s^97` become `1`, so the colon exponent is not a relation in `J`;
- `FINAL[i]` remain in `Q[X]`, with no inverted nonunit;
- the monomial order used to compute `sat`/`lift` is irrelevant once the identity is the zero polynomial.

Therefore `W ∈ J` as an element of a fixed finitely generated ideal in `Q[Lambda,tau,rho,q1,q0,r2,r1,r0]`. Least-weight initial forms of this same polynomial may be taken with respect to any rational weight vector on those eight variables. No continuity of a Gröbner basis, no parametric neighbourhood of the source, and no re-homogenization of `W` is invoked: only the explicit eight-term support.

What would have been a defect, and is not present: (i) treating `W` as an element of `I : s^∞` without dehomogenizing; (ii) retaining discovery-weight `s`-powers in the generators and then changing `w` as if those powers were part of `J`; (iii) inverting a coordinate other than the dummy `s`; (iv) claiming the seven halfspaces are a Gröbner cone. The target avoids all four.

---

## Charge 5 — control-2 mapping: `alpha=15/2`, `5<beta<6`, positivity, `Lambda=tau^3 rho`

**CONFIRMED for the charged face and this fixed support. No firewall-allowed leading layer is missing from the five-coefficient torus.**

D1 row `ell` carries target `Lambda^{12+ell} γ_ell`. Row 3 is `Lambda^15 μ` with `μ=2/3`; weight `15` in the normalization `v(Lambda)=1`. The control-2 face is the Newton ray on which the first ordinary `R^2/K^2` layer lands on that row, i.e. `2 alpha = 15`, hence `alpha=15/2`, hence `w(r_i)=(15/2) L`.

The previously charged window `5<beta<6` is exactly the open in which that face has the control-2 layer order

```text
beta < alpha < 3 beta/2 < 2 beta.
```

- `alpha < 3 beta/2` ⇔ `15/2 < 3 beta/2` ⇔ `beta>5`, which is the same strict inequality that makes `Lambda^20` the unique least-weight term of `W`;
- `beta < alpha` ⇔ `beta < 15/2`, and the low-fan window `beta<6` is stricter, as previously charged;
- first `QR/K` weight `beta+alpha ∈ (12,15)` sits strictly below row 3; `Q^3` weight `3 beta ∈ (15,18)` sits strictly above.

So the witness wall `beta=5` is the Newton collision `3 beta = 2 alpha = 15`, not an accident of the certificate.

**Positivity and the relation.** `Lambda = tau^3 rho` forces `L=3T+H` on leading terms. `T>0` is required for uniqueness (`Lambda^20 tau` strictly heavier). `H>0` places the split in the interior of the strict chart, off the equal-slope wall `H=0` (`v(Lambda)=3 v(tau)`, `rho` a unit) and off the `tau`-unit wall `T=0`. Every positive rational split is allowed; the sample `T=H=1`, `L=4` is one interior point. Uniformity in `(T,H)` is therefore correct for the open chart, and is not a hidden extra ramification hypothesis.

**Leading jet versus this support.** The charged control-2 successor is

```text
Q = t^beta L = t^beta (z-1),
R = t^{15/2} N - (1/2) t^{15-beta} + higher,
```

with `N=(z-1)(z+2)=z^2+z-2`. Leading coefficients `(q1,q0) ∝ (1,-1)` and `(r2,r1,r0) ∝ (1,1,-2)` all lie in the eight-coordinate torus. The correction exponent `15-beta` is strictly larger than `alpha=15/2` on `5<beta<6`, so `-1/2` is a later coefficient of the *same* coordinate `r0`, not a ninth finite-ring variable, not `q2`, and not a moving-axis parameter. Relative valuation at the sample is `38-30=8`. Killing the leading torus already kills this jet; the higher term is not needed and is not missing.

**Layers allowed by the correction firewall but absent here.**

| firewall object | in this `J`? | status |
|---|---|---|
| control-2 leading five-coefficient torus, `q2≡0` | yes | excluded for `beta>5` |
| control-2 higher `r0` coefficient `-1/2 t^{15-beta}` | same `r0`, higher valuation | invisible to `in_w`; does not rescue the leading jet |
| control-1 jet `Q=t^beta N` (quadratic, `q2≠0`) | no | different support; firewalled |
| tied ray `alpha=2 beta` | no | different chart; firewalled |
| moving axis `a,h` | no, frozen `a=1,h=0` | firewalled |
| later activation of `q2` at valuation `>beta` | `q2` is identically `0` in this ring | different family; firewalled |
| moving `k,mu,nu` | no, `k=nu=0`, `mu=2/3` | firewalled |

No coefficient or Newton layer that the correction firewall licenses *as a control-2 leading jet on this support* is absent from the eight-coordinate torus that `Lambda^20` kills. What the finite ring cannot see is a later `q2` (or axis) direction; that is a scope limit, not a hole in the charged face.

---

## Charge 6 — equality face, endpoints, `beta>6`, and the stated firewalls

**CONFIRMED. The target does not infer beyond the exact fixed cubic/load/support theorem.**

| locus / inference | licensed? | reason |
|---|---|---|
| open face `alpha=15/2`, `5<beta<6`, this support | yes | charges 1–5 |
| equality `beta=5` | no | seven-term nonmonomial `in_w(W)`; needs a full face initial ideal and torus saturation |
| `beta=6` as a control-2 endpoint | no | not a wall of this witness; Newton-window boundary, not claimed |
| algebraic uniqueness for `beta>6` | true as weight arithmetic, **not promoted** as control-2 geometry | layer order / low-fan interpretation was only charged for `beta<6` |
| moving axis, nonzero `q2`, moving `k,mu,nu` | no | different ideal |
| another support mask | no | `W` and `J` are this five-coefficient slice |
| tied `alpha=2 beta` chart | no | different covering; `alpha/beta=15/11≠2` on the sample |
| other strict branch (control-1) | no | quadratic `Q`, different support |
| whole double-root fan, D1, JC2 | no | correctly firewalled |
| sampled ramification `(4,1,1;22;30)` | yes, as a special case | `beta=11/2 ∈ (5,6)`, `alpha=15/2` |

The sentence “although the inequality remains true for `beta>6`, this theorem only promotes `5<beta<6`” is the correct promotion discipline. Broadening it would be a defect; the target does not.

---

## Nits, not defects

1. The producer status line still says the mapping review is pending. Timestamp, not a contradiction of the identities.
2. The target says “frozen LPDP certificate and its literal r6d replay prove `W ∈ J`” without the word “replay not derivation.” Mathematically accurate; Charge 1 records the distinction.
3. The valued-arc lemma is used (“excluded”, “leading-coefficient torus”) but not written. It is standard and is recorded above; it is not a missing hypothesis of the algebraic initial-ideal statement.
4. `H>0` is a chart hypothesis, not a uniqueness hypothesis. Harmless.
5. Evidence uses `la`; the target uses `Lambda`. Same coordinate.

No source, certificate, or theorem repair is required. No AWS computation is required: the identity is already replayed on r6d, and the slope-uniform step is finite-support arithmetic.

CONFIRMED
