# Hostile different-model review — AS109 `xy` membership gate

| Field | Value |
|---|---|
| Claim under review | Frozen AS109–`xy` membership gate: the 109 Hensel sections on the tube `(P,Q)=(109S,1+109T)` give 109 distinct images of `w=xy`, hence `[M(xy):M]>=109` and `xy` lies in neither the target field nor the target ring, including after a characteristic-zero coefficient embedding into `C`; under the separately reviewed hypothesis `A_infinity=0` one has `L=M(xy)` and the monic minimal polynomial reduces on that tube to `Z^{109}-Z`; trace, norm, and the local discriminant are split-étale tautologies; both displayed controls work; the univariate deck discriminator is unearned; the admissible conclusion is a sharp no-go for the membership bridge, not a lift obstruction |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (precisions below: `μ_w ∈ R[Z]` is the *tube specialization* of the field minimal polynomial, not a global integral equation over `K[P,Q]`; “conjugates” before `A_infinity=0` are the 109 integral-tube images, not a complete Galois orbit) |
| Evidence tier | independent field theory over `Q_{109}` and `Frac(Z_{109}[[S,T]])` (restriction of the reviewed Hensel embeddings, kernel of a monic polynomial with `p` distinct roots in `E`, linear algebra of membership after scalar extension); Newton/binomial Möbius expansion for `G_p` over `Z` and a full `109×109` Vandermonde solve over `F_{109}` (second engine, no producer imports); unmodified rerun of `cases/as109_xy_membership_20260824/check.py` as regression control only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T11:48:17Z – 2026-08-24T12:05:00Z |
| Python | 3.14.6; stdlib only (`math.comb`, integer lists, one `104729`-modular sampling) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-xy-membership-gate-20260824.md` (SHA-256 `09d5654aeeeee55f9c5766e75f1a975db12a5701258efb25b04606fb4fc72729`, matches the launch prompt and `FREEZE.sha256`)
- `cases/as109_xy_membership_20260824/check.py` (SHA-256 `d31f47f0dcee171a2dc4ac60d6aacd098cc55596f7d5a97a0b93574216a6fc01`)
- `cases/as109_xy_membership_20260824/FREEZE.sha256` (SHA-256 `76ce3a7b3f176f9d7aa575850e8011ce1cb70b7f88d46fc706ae0e190b857448`)

Reviewed Hensel degree-cross and `A_infinity` parent gates, same charged basis:

- `xmodel/as109-hensel-global-degree-cross-gate-20260824.md` (SHA-256 `7a7185c27fe245233173a173f9f0851326f18d83585ffb743970b2189f703133`)
- `xmodel/as109-degree-cross-review-grok-20260824.md` (SHA-256 `fb260d5ce622f05e5869bfc64d0497f54e219e9afe04308aa7f3355312af19c6`), overall **CONFIRMED**
- `xmodel/as109-ainfinity-deck-descent-gate-20260824.md` (SHA-256 `f1cf4991e92e502459ca6c61a3cb4d0e346a65e6221890c8c64a808ec2e3b64b`)
- `xmodel/as109-ainfinity-review-grok-20260824.md` (SHA-256 `a86b694364ebaf28a3890b7bd73aafb5057ddae100172db78a9490e7a2b55d76`), overall **CONFIRMED**

Confirmed Moskowicz prime-degree source audit and hostile review, same charged basis:

- `xmodel/moskowicz-prime-degree-source-audit-20260824.md` (SHA-256 `929469d903d156d18e32a3b98e847a07145c72352d3baecf37b50eb10d9d4210`)
- `xmodel/moskowicz-prime-degree-review-grok-20260824.md` (SHA-256 `a32082a89077b17bb9f9df4d2b518d8e7ad6de4e126a35cf0d49b446bb0d5a06`), overall **CONFIRMED**
- `cases/moskowicz_prime_degree_audit_20260824/check.py` (SHA-256 `1a6174fcd8fc1648e283df316c22206ccad6d9bb103224d3704f4d6c4c9408fb`)

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer, parent, and this-review artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No AWS call was made.

Write `p=109`, `K=Q_p`, `M=K(P,Q)`, `L=K(x,y)`, `d=[L:M]`, `w=xy`, `R=Z_p[[S,T]]`, `E=Frac(R)`. The exact-lift hypothesis is the existence of `F=(P,Q)` in `Z_p[x,y]^2` with `F mod p=(x-x^p,y)` and `det J_F=1` as a polynomial identity. Existence is not inferred. The reviewed degree-cross supplies 109 distinct `M`-embeddings `σ_a:L→E` over every target tube `(U,V)=(pS,b+pT)`. The reviewed `A_infinity` gate supplies the split `L⊗_M E ≅ E^p × A_infinity` with `dim_E A_infinity=d-p`, and is consumed only for the conditional `A_infinity=0 ⇒ d=p`. The Moskowicz audit is consumed only for the repaired implication “complex Keller `+ xy∈C(P,Q) ⇒` automorphism”; the printed first case and the headline no-prime theorem stay quarantined.

Tried hard, and failed, to turn the tube residues into a mere special-fibre count, to make `μ_w` acquire a hidden `p`-denominator that would collapse the reduction, to produce a constant-extension membership of `w` in `C(P,Q)`, to read the local discriminant as an obstruction, or to extract a descended `p`-cycle from the symmetric functions of `μ_w`.

---

## Promotion

**Accept `SHARP NO-GO FOR THE MEMBERSHIP BRIDGE / PRIMITIVE-GENERATOR CLIENT UNDER A_infinity=0` at the stated scope.**

Under the conditional exact-lift hypothesis:

- Parameter Hensel on the tube `(P,Q)=(pS,1+pT)` supplies 109 integral sections with `σ_a(x)≡a`, `σ_a(y)≡1 (mod p)`, hence `σ_a(w)≡a (mod p)`. These are pairwise distinct elements of `E`.
- Distinctness in `E`, not in a special fibre, forces `[M(w):M]>=p`. In particular `w∉M` and `w∉K[P,Q]`. The same nonmembership survives every characteristic-zero coefficient-field embedding into `C`. The antecedent of the repaired Moskowicz second case is therefore impossible for an AS109 lift in the displayed coordinates.
- If, separately, `A_infinity=0`, then `d=p`, hence `L=M(w)` and the monic minimal polynomial of `w` over `M` specializes on this tube to `∏_{a∈F_p}(Z-w_a)∈R[Z]`, which reduces to `Z^p-Z`.
- Trace, norm, and `Disc(μ_w)≡-1 (mod p)` are the elementary symmetric functions of that split residue set. The residue `-1` is a square (`33^2≡-1 (mod 109)`). None of these is an obstruction.
- The displayed controls do what they claim: `G_p=(x+(p-1)x^p,y)` is a degree-`p` finite-free non-Keller map with primitive `xy` and trivial rational deck group; the cyclic Kummer extension moves `xy` under every nonidentity deck element.
- Equations (6.3)–(6.4) are a finite univariate test for a *descended* translation of the roots. They are equivalent to supplying the missing permutation, not a corollary of `μ_w`.

**Do not promote this to:** nonexistence of an exact AS109 lift; a proof of `A_infinity=0`; descent of a formal `p`-cycle; a global integral equation for `μ_w` over `K[P,Q]`; a square-discriminant contradiction; TDU at `td=109`; consumption of the Moskowicz first case or headline; or any JC2 decision.

**Close `AS109-XY-MEMBERSHIP` as a route to the repaired theorem (1.4).** Keep the two parent bridges — vanishing of `A_infinity`, and rational descent of a deck automorphism — as the remaining exact clients. After `A_infinity=0`, any single off `L`-factor already closes the lift by the reviewed Galois-Keller implication; that closure does not run through `xy∈M`.

---

## Quarantine

No result here proves or disproves JC2. Producer string `verdict = AS109-XY-MEMBERSHIP-SHARP-NO-GO` and the registered Booleans were not used as evidence for Hensel, for `[M(w):M]>=p`, or for the Möbius comparison; those were re-derived. The registered script is residue arithmetic and two mechanism labels. Moskowicz’s printed first case and headline no-prime theorem remain unusable. The independent `deg_y<=5` frontier is not consumed. Classical Galois Keller is a known-theorem input only to the last sentence of producer §6 (already so recorded in the `A_infinity` review); it is not load-bearing for nonmembership.

---

## Scope (not enlarged)

One prime `p=109`, one seed `(x-x^{109},y)`, exact coefficient ring `Z_{109}` for a hypothetical polynomial lift, function fields over `K=Q_{109}`, and one formal target tube `R=Z_{109}[[S,T]]` centred at `V=1`. Characteristic-zero language is purely conditional on an exact integral polynomial lift that this run did not produce. No construction, no support grammar, no enumerator, no AWS, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | On the tube `(P,Q)=(pS,1+pT)`, parameter Hensel produces 109 sections `(x_a,y_a)∈R^2` with `F(x_a,y_a)=(pS,1+pT)`, `x_a≡a`, `y_a≡1 (mod p)`, hence `σ_a(w)≡a (mod p)`. The 109 product residues are pairwise distinct. The `b=0` tube collapses every product residue and is correctly refused | **CONFIRMED** | `(R,pR)` failing to be Henselian; `F_bar(a,1)≠(0,1)` or `det J_F(a,1)` a nonunit; `y_a` not reducing to `1`; two distinct `a` with `x_a y_a` equal in `E`; the report using the `V=0` tube as the distinguishing locus |
| 2 | The maps `σ_a` are the reviewed `M`-embeddings `L→E`, not evaluations of a special fibre. Distinct images of `w` in `E` force `[M(w):M]>=p`. Separability of `L/M` is characteristic zero. No algebraic closure of `E` is used. Localization/completion maps stay injective on the fields | **CONFIRMED** | a nonzero `G∈K[x,y]` with `G(x_a,y_a)=0`; a vanished denominator in `Frac(K[x,y])`; the `p` embeddings of `L` restricting to fewer than `p` maps of `M(w)`; a degree-`<p` polynomial over `M` acquiring `p` distinct roots after an illegal specialization `E→κ`; the report claiming `[M(w):M]=p` without `A_infinity=0` |
| 3 | Therefore `xy∉K(P,Q)` and `xy∉K[P,Q]`. Membership cannot first appear after extending the finitely generated coefficient field `k_0` to `Ω` or embedding `k_0→C`. The repaired implication (1.4) cannot consume an AS109 lift. No constant-extension or Galois-descent loophole survives | **CONFIRMED** | a nonzero `Ω`-solution of `A(P,Q)-w B(P,Q)=0` whose `k_0`-span had vanishing `B`-part; `P,Q` becoming algebraically dependent after `k_0→C`; Wang converting a non-membership into a membership; a complex map not obtained by a coefficient embedding of the same `F` treated as a counterexample to (3.3) |
| 4 | Under the reviewed hypothesis `A_infinity=0`, `d=p`, hence `L=M(w)`. The field minpoly `μ_w∈M[Z]` specializes along `M→E` to `∏(Z-w_a)∈R[Z]` and reduces to `Z^p-Z`. The identification is local on the tube. Denominators of elements of `M` do not vanish on the embedding. This is not a global integral equation over `K[P,Q]` | **CONFIRMED** | `A_infinity=0` not forcing `d=p`; tower law failing; `μ_w` dropping degree after `M→E`; a pole of a coefficient of `μ_w` at `(pS,1+pT)`; the report claiming `μ_w∈Z_p[P,Q][Z]` as a global identity; `c_1≡-1` read as a congruence in the coordinate ring of the whole target |
| 5 | On the tube, `Tr(w)≡0`, `Nm(w)≡0`, `Disc(μ_w)≡-1 (mod p)`, and `33^2≡-1 (mod 109)`. These are the split-étale elementary symmetric functions of `F_p`. They do not force `w∈M`, constrain `A_infinity`, or descend a deck transformation. The stop is correct | **CONFIRMED** | `Disc(Z^p-Z)≢-1 (mod p)`; `-1` a nonsquare mod `109`; the report presenting (5.1) as a local obstruction; trace/norm used as if they were extra elements of `M` beyond the definition |
| 6 | `G_p=(x+(p-1)x^p,y)` has AS109 reduction, generic degree `p`, finite-free formal fibre of rank `p`, `A_infinity=0`, primitive `w` with the displayed minpoly reducing to `W^p-W` on the tube, nonconstant Jacobian, and trivial rational deck group (affine Möbius, uncontaminated `x^{p-1}` row). The cyclic Kummer control has degree `p`, and every nonidentity deck element moves `xy=s^2+3sv+2v^2` | **CONFIRMED** | `G_p mod p ≠ (x-x^p,y)`; leading coefficient `p-1` not a `p`-adic unit; `[K(x):K(g_p)]≠p`; a nontrivial Möbius with `g_p(αx+β)=g_p(x)`; the displayed minpoly failing the identity `(p-1)w^p+y^{p-1}w-g_p(x)y^p=0`; `3(ζ-1)=0` for some `ζ≠1`; the report presenting `G_p` or the Kummer pair as a Keller example |
| 7 | If a rational `τ∈Aut_M(L)` descends `a↦a+1` and `A_infinity=0`, then `τ(w)=R_τ(w)` with `deg R_τ<p`, the unit Vandermonde puts the interpolant in `R[Z]`, and `R_τ(Z)≡Z+1 (mod (p,μ_w))` with `p`-fold composition the identity. These do not follow from the symmetric coefficients of `μ_w`. No numbered implication silently assumes the unearned deck action. The even `p`-cycle makes `Disc(μ_w)` a square in `M`, compatibly with (5.2) | **CONFIRMED** | interpolation of `w_a↦w_{a+1}` not unique in degree `<p`; Vandermonde of the `w_a` a nonunit of `R`; `R_τ^{[p]}` read as a `p`-th power rather than composition; (6.4) asserted from `μ_w` alone; (6.5) used as a contradiction; a numbered claim of §§2–5 invoking `τ` |
| 8 | The admissible conclusion is a sharp no-go for `xy∈M` plus the conditional primitive-generator statement. The freeze constructs no lift, does not prove `A_infinity=0`, does not descend a cycle, does not exclude an arbitrary-support AS109 lift, and does not decide JC2. Scope strings match the algebra | **CONFIRMED** | a constructed lift in the artifacts; `A_infinity=0` or a deck cycle claimed as a theorem of this freeze; (2.5) sold as incompatible with existence of a counterexample; `jc2_inference` or a headline no-prime consumption |

All remarks below are non-blocking unless marked otherwise. None changes a residue, a rank, or a numbered verdict.

---

## Replay and hashes

Frozen producer hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-xy-membership-gate-20260824.md` | `09d5654aeeeee55f9c5766e75f1a975db12a5701258efb25b04606fb4fc72729` | prompt and `FREEZE.sha256` |
| `cases/as109_xy_membership_20260824/check.py` | `d31f47f0dcee171a2dc4ac60d6aacd098cc55596f7d5a97a0b93574216a6fc01` | prompt and `FREEZE.sha256` |
| `cases/as109_xy_membership_20260824/FREEZE.sha256` | `76ce3a7b3f176f9d7aa575850e8011ce1cb70b7f88d46fc706ae0e190b857448` | self-hash of the freeze listing |
| `xmodel/as109-hensel-global-degree-cross-gate-20260824.md` | `7a7185c27fe245233173a173f9f0851326f18d83585ffb743970b2189f703133` | predecessor producer |
| `xmodel/as109-degree-cross-review-grok-20260824.md` | `fb260d5ce622f05e5869bfc64d0497f54e219e9afe04308aa7f3355312af19c6` | predecessor review |
| `xmodel/as109-ainfinity-deck-descent-gate-20260824.md` | `f1cf4991e92e502459ca6c61a3cb4d0e346a65e6221890c8c64a808ec2e3b64b` | parent gate |
| `xmodel/as109-ainfinity-review-grok-20260824.md` | `a86b694364ebaf28a3890b7bd73aafb5057ddae100172db78a9490e7a2b55d76` | parent review |
| `cases/as109_ainfinity_20260824/check.py` | `84941b672e04fab735b5de31f39de28487672167d233caeffa08870a57665b7f` | parent replay |
| `xmodel/moskowicz-prime-degree-source-audit-20260824.md` | `929469d903d156d18e32a3b98e847a07145c72352d3baecf37b50eb10d9d4210` | repaired second case |
| `xmodel/moskowicz-prime-degree-review-grok-20260824.md` | `a32082a89077b17bb9f9df4d2b518d8e7ad6de4e126a35cf0d49b446bb0d5a06` | Moskowicz review |
| `cases/moskowicz_prime_degree_audit_20260824/check.py` | `1a6174fcd8fc1648e283df316c22206ccad6d9bb103224d3704f4d6c4c9408fb` | source-audit replay |

Registered command, rerun unmodified from the charged tree:

```sh
python3 cases/as109_xy_membership_20260824/check.py
```

Exit code 0. Exact advertised headline:

```text
verdict = AS109-XY-MEMBERSHIP-SHARP-NO-GO
target_field_membership_forced = false
target_ring_membership_forced = false
jc2_inference = false
```

Stdout SHA-256 `ead9fb80403aeea5a301536298ae952681a0b4ed5f3bab09daee1a4b05799352`. Locale warnings from the host `shasum` wrapper are not part of that digest.

The registered program is a finite residue-arithmetic suite, not a checker of Hensel, of `Hom_M(L,E)`, or of scalar extension. It records product residues `(a·b) mod p` on every target residue `b`, multiplies `∏(Z-a)` in `F_p[Z]`, evaluates trace/norm/disc of `{0,…,108}`, and labels two mechanism controls. Those Booleans were discarded as evidence for the field-theoretic claims; every numbered claim below is re-derived independently.

A second engine, written for this review and not imported from the registered script, used only integer lists, `math.comb`, and one `104729`-modular sampling. It recorded zero failures on: Fermat as functions on `F_{109}` and as the polynomial identity `∏_a(Z-a)=Z^{109}-Z` coefficient by coefficient; product residues bijective for every `b∈F_p^×` and collapsed at `b=0`; `b=1` the identity permutation; trace `0`, norm `0`, discriminant `-1` by both `∏_{i<j}(i-j)^2` and `(-1)^{n(n-1)/2}∏ f'(roots)` with `f'= -1` in characteristic `p`; `33^2≡76^2≡-1 (mod 109)` and `p≡1 (mod 4)`; Vandermonde of `F_p` a unit (value `76`); the unique degree-`<p` interpolant of `a↦a+1` equal to `Z+1`, obtained by a full `109×109` Vandermonde solve over `F_{109}`, with translation-order exactly `p`; `G_p` reduction on every residue, leading coefficient a unit, Jacobian extra term `109·108=11772≠0`; the identity `(p-1)w^p + y^{p-1}w - g_p(x) y^p = 0` on a `5×5` grid at `p=3,5` and at 40 random points modulo `104729`; `1/(p-1)≡-1 (mod p)`; the uncontaminated `x^{p-1}` Möbius coefficient `p(p-1)`; Kummer coefficient `3≠0` and evenness of a `p`-cycle.

Process remark, non-blocking: `check.py` tests “deck group trivial” and “every nonidentity deck element moves `xy`” by labels and the Booleans `3≠0`, `(-1)^{p-1}=1`. The Möbius expansion and the UFD/Kummer difference `(ζ^2-1)s^2+3(ζ-1)sv` are the actual comparisons, in claim 6.

---

## Independent recomputation

### 1. Hensel sections on the `V=1` tube; product residues — CONFIRMED

Assume the exact-lift hypothesis. The pair `(R,pR)` is Henselian: `R=Z_p[[S,T]]` is `p`-adically complete and `pR` lies in the Jacobson radical `(p,S,T)`. This is the same complete-ring input already confirmed in the degree-cross review, not a silent upgrade of the DVR lemma’s pointwise conclusion.

Fix the target

```text
(U,V) = (p S, 1 + p T).
```

It reduces to `(0,1)` modulo `p`. For each residue `a∈F_p`, Fermat gives `F_bar(a,1)=(a-a^p,1)=(0,1)`, and `J(F_bar)=I_2` as a matrix of polynomials over `F_p`. The packed identity `det J_F=1` makes `det J_F(a,1)` a unit of `R`. Multivariate Hensel therefore produces a unique pair

```text
(x_a, y_a) ∈ R^2,     x_a ≡ a,     y_a ≡ 1  (mod p),
```

with `F(x_a,y_a)=(pS,1+pT)` exactly. Uniqueness is inside the residue class `(a,1)+p R^2`.

The elements `pS` and `1+pT` are algebraically independent over `K` (translation in `V` composed with scaling by `p≠0`). Evaluation at `(x_a,y_a)` is the reviewed `M`-embedding `σ_a:L→E` of the degree-cross gate, now centred at `b=1` rather than at `b=0`. The parent theorem is stated for every `b∈F_p`; the choice `b=1` is a specialization of a confirmed statement, not a new Hensel lemma.

The product is integral:

```text
σ_a(w) = x_a y_a ∈ R,     x_a y_a ≡ a·1 = a  (mod p).
```

Distinct residues in `R/pR` imply distinct elements of `R` and of `E`. Thus the 109 values `σ_a(w)` are pairwise distinct.

The `b=0` tube is the necessary negative control. There `y_a≡0 (mod p)` and every product residue vanishes, so the 109 sections do not distinguish `w`. Every nonzero `b` makes multiplication-by-`b` a bijection of `F_p`, hence also distinguishes; the report’s choice `b=1` is the cleanest, not the only, distinguishing centre. Essential, and correctly flagged.

Tried to break the sections by evaluating the Jacobian only at `(a,0)`, or by transporting the `A_infinity` parent’s height-one DVR (Gauss valuation centred at `(pS,pT)`) without re-centring. Hensel consumes a unit Jacobian at the *chosen* residue point `(a,1)` and `p`-adic completeness of `R`, both of which hold. The Gauss DVR is not used in this claim.

### 2. Distinct tube images force `[M(w):M]>=p`, not a special-fibre count — CONFIRMED

The specialization attack that was available: look at the scheme-theoretic fibre of `F` over `(0,1)` in characteristic `p`, observe `p` points `(a,1)` with products `a`, and infer that the generic degree of `w` is at least `p`. That inference is illegitimate for a non-finite morphism (special-fibre cardinality can drop, and a function on the special fibre need not be the reduction of a generic minimal polynomial). The producer does not make it.

Load-bearing chain, re-derived:

1. Each `σ_a` is an injective `M`-homomorphism `L→E` (degree-cross review, claim 2: kernel of `K[x,y]→E` has height zero because the image contains two algebraically independent elements, and no denominator of `Frac(K[x,y])` vanishes). The element `w=xy` is a polynomial, so there is no denominator to vanish in any case.
2. Restrict to the subextension `M(w)/M`. The restrictions are `M`-homomorphisms `M(w)→E`. They are pairwise distinct because they send `w` to pairwise distinct elements of `E`.
3. Let `μ_w∈M[Z]` be the monic minimal polynomial of `w` over `M`, of some degree `k=[M(w):M]`. The embedding `M→E` is injective (algebraic independence of `pS` and `1+pT`), so the image polynomial in `E[Z]` still has degree `k`. It has `p` distinct roots `σ_a(w)`. A degree-`k` polynomial cannot have `p>k` roots in a field. Hence `k>=p`.

This uses neither an algebraic closure of `E` nor the full set `Hom_M(L,Ω)`. The producer’s slogan — the number of distinct values of an element under *all* base-field embeddings into an algebraic closure equals the degree of its minimal polynomial — is true, and would give equality after passing to `Ω`. Applied to the 109 embeddings into `E` it yields only a lower bound, which is exactly (2.5). When `A_infinity≠0` there may be further conjugates of `w` living on residual sheets; that can only enlarge the number of distinct values, and the report correctly writes `>=`.

Separability. `L/M` is finite separable because it is finite in characteristic zero (degree-cross review, claim 1: `det J_F=1` implies algebraic independence of `P,Q`, equal transcendence degrees, hence a finite extension). Any subextension `M(w)/M` is therefore separable. Separability is not required for the root-count lower bound: `p` distinct roots already force `deg μ_w>=p` whether or not `μ_w` is separable. It is required for the parent Hom-bound `d>=p` and for the étale splitting that this report inherits.

Localization / completion injections. The structure map `K[P,Q]→R` extends to a field embedding `M→E` because `pS,1+pT` are algebraically independent; no localization of a nonzero element of `K[P,Q]` dies. Completing `R` along `(p,S,T)` or localizing at `(p)` is not used for (2.5). Reduction modulo `p` is applied only to the *integral* elements `x_a y_a∈R`, as a distinctness witness, never to arbitrary elements of `E`. An illegal reduction `E→Frac(F_p[[S,T]])` would send some elements of `E` to infinity; that map is not invoked.

Wording precision, non-blocking. The introduction’s “109 pairwise distinct conjugates of `xy`” is Galois language. Before `A_infinity=0` the extension `L/M` need not be Galois, and these 109 values are the images under the integral Hensel embeddings, not a complete orbit. Body (2.3)–(2.5) states the Hom-count correctly.

### 3. Field and ring nonmembership; no constant-extension loophole — CONFIRMED

If `w∈M` then every `M`-embedding sends `w` to the same element of `E`, contradicting claim 1. Thus `xy∉K(P,Q)`. The polynomial ring sits inside the field, so `xy∉K[P,Q]` as well. Ring membership is the weaker statement; both fail. Wang’s intersection theorem (`K(P,Q)∩K[x,y]=K[P,Q]` for a Keller map) is not needed: it would convert *field* membership of the polynomial `xy` into *ring* membership, and there is no field membership to convert.

Constant extension. Let `k_0⊂Q_p` be the field generated over `Q` by the finitely many coefficients of `F`. It is finitely generated of characteristic zero. Suppose, for a field extension `Ω/k_0`, that

```text
w = A(P,Q)/B(P,Q) ∈ Ω(P,Q),     B ≠ 0.
```

Clear the denominator of the right-hand side (already a ratio of polynomials in two algebraically independent elements) and freeze the finite supports of that particular `A,B`. The identity

```text
A(P,Q) − xy B(P,Q) = 0
```

is an identity in `Ω[x,y]`: `B(P,Q)` cannot vanish as a polynomial in `x,y` without `B=0`, by algebraic independence of `P,Q` over `Ω` (the Jacobian remains `1` after scalar extension). Expanding in the monomial basis of `Ω[x,y]` yields a finite homogeneous linear system in the unknown coefficients of `A,B`. The matrix has entries in `k_0` (the coefficients of the polynomials `P^i Q^j` and `xy P^k Q^l` as elements of `k_0[x,y]`). For a matrix over `k_0`, rank and nullity survive scalar extension to `Ω`, and a `k_0`-basis of the kernel spans the `Ω`-kernel. If some `Ω`-solution has nonzero `B`-part, some `k_0`-basis vector does as well: otherwise the `Ω`-span of the kernel would have vanishing `B`-part. A nonzero kernel vector cannot have `B=0` and `A≠0`, again by algebraic independence. Thus `w∈k_0(P,Q)⊂Q_p(P,Q)`, contradicting claim 2.

The producer’s phrase “matrix entries in `k_0(x,y)`” is slightly loose: after monomial expansion the matrix is over `k_0`. Equivalently, one may view the vanishing as a single `k_0`-linear map from the finite-dimensional space of coefficient pairs of given support into `k_0(x,y)`, and kernels of linear maps commute with scalar extension. Either packaging gives the same conclusion. Not a gap.

Every finitely generated characteristic-zero field embeds in `C`. Applying a field embedding `σ:k_0→C` coefficientwise produces a complex Keller map `F^σ` with `det J=1` still the constant polynomial one (degree-cross review, claim 4). The same linear algebra over `k_0` forbids `xy∈C(P^σ,Q^σ)`. Membership cannot first appear after Lefschetz. A valuation-preserving embedding `Q_p→C` is not used and does not exist as a field map compatible with the 109-adic topology; distinctness of Hensel images is injectivity of field maps, not preservation of residues.

Tried a Galois-descent loophole: if `w` were in `Ω(P,Q)` for a Galois extension `Ω/k_0`, average the coefficients of `A,B`. That also works, and is strictly weaker than the linear-algebra argument, which does not need Galois. Tried `Ω=C` with a different identification of the source, not coming from a coefficient embedding of this `F`; that would be a different map, outside the claim.

The repaired Moskowicz implication (1.4), confirmed as a complex plane statement assuming Wang 41(i) and Gwoździewicz 1.1, therefore cannot consume an AS109 lift: its hypothesis `xy∈C(P,Q)` is false for every complex incarnation obtained from the lift. The implication itself remains valid. The printed first case and the headline no-prime theorem are not used.

### 4. `A_infinity=0` implies `L=M(w)` and the local reduction `Z^p-Z` — CONFIRMED

The reviewed `A_infinity` gate gives `A_infinity=0 ⇒ d=p` (finiteness of the formal fibre algebra is a sufficient condition for this, not a necessary one; the present report assumes the vanishing, it does not prove it). Combined with (2.5) and the tower law

```text
[L:M] = [L:M(w)] [M(w):M],
```

one gets `[M(w):M]=p` and `[L:M(w)]=1`, hence `L=M(w)`. Thus `xy` is a primitive generator of the degree-`p` extension, the opposite of target-field membership.

Let `μ_w(Z)=Z^p + c_{p-1} Z^{p-1} + ⋯ + c_0 ∈ M[Z]` be the monic minimal polynomial over the *field* `M`. Under the tube embedding `M→E`, which is injective, `μ_w` maps to a monic degree-`p` polynomial in `E[Z]`. The `p` distinct images `w_a=σ_a(w)` are roots, hence

```text
image(μ_w) = ∏_{a∈F_p} (Z − w_a).
```

Each `w_a` lies in `R`, so the product lies in `R[Z]` (elementary symmetric functions of integral elements, `R` integrally closed). This is the identification (4.3). It is an identity in `E[Z]` after specialization, not a claim that the unspecialized `μ_w` has coefficients in `K[P,Q]` or in the integral closure of `Z_p[P,Q]`.

Hidden-denominator attack, failed. An arbitrary element of `M` is a ratio `A(P,Q)/B(P,Q)` with `B≠0`. Its image in `E` is `A(pS,1+pT)/B(pS,1+pT)`, and the denominator does not vanish because `B(P,Q)≠0` and `P,Q` remain algebraically independent on the tube. There is therefore no pole on `M→E`. Reducing the *image* of `c_i` modulo `p` is reduction of an element of `R`, which is legitimate. What would be illegitimate — and is not claimed — is a global congruence `c_i ≡ 0 (mod p)` in a coordinate ring of the whole target, or an identity `μ_w ∈ Z_p[P,Q][Z]`. The producer’s “exact local coefficient ledger” and the sentence that this is “a useful univariate representation of the `A_infinity=0` client, not a membership theorem” match the distinction.

Reduction. `w_a ≡ a (mod p)`, so

```text
∏ (Z − w_a) ≡ ∏_{a∈F_p} (Z − a) = Z^p − Z  in  (R/pR)[Z].
```

The polynomial identity `∏(Z-a)=Z^p-Z` over `F_p` was re-multiplied coefficient by coefficient. Expanding `Z^p-Z` gives the ledger

```text
c_1 ≡ −1 (mod p),     c_i ≡ 0 (mod p) for i ≠ 1, p,
```

as congruences of the specialized coefficients in `R`. Field-minpoly versus local integral polynomial: `μ_w` is monic over the field `M` by definition; the specialized polynomial is monic in `R[Z]` because the roots are integral. A non-monic integral equation over `K[P,Q]` is not produced and not needed.

### 5. Trace, norm, discriminant are split-étale tautologies — CONFIRMED

On the tube, the elementary symmetric functions of `{w_a}` reduce to those of `F_p`. Independently:

- `Tr_{L/M}(w) = −c_{p-1} ≡ ∑_{a=0}^{p-1} a = p(p-1)/2 ≡ 0 (mod p)`.
- `Nm_{L/M}(w) = (−1)^p ∏ a`. The product includes `0`, so the norm residue is `0`. (For odd `p` the sign is `−1` and is irrelevant.)
- `Disc(μ_w) = ∏_{i<j}(w_i−w_j)^2`. Reducing, two computations agree: the double product `∏_{i<j}(i-j)^2 ≡ −1 (mod p)`, and the formula `Disc(f)=(−1)^{n(n-1)/2} ∏ f'(roots)` for `f=Z^p−Z`. In characteristic `p` one has `f'=−1`, `n(n-1)/2=109·54` even, and `∏(−1)=(−1)^p=−1`, hence `Disc≡−1`. The second engine recorded both.

Trace and norm of `w` lie in `M` for every finite extension, by definition. Their tube congruences are the first and last symmetric functions of the split residue set. The discriminant congruence is the same split-étale datum: the 109 residues are distinct, so the discriminant is a unit of `R`, and that unit reduces to `-1`.

Square. `-1` is a square modulo `p` if and only if `p=2` or `p≡1 (mod 4)`. Here `109=27·4+1`. Explicitly `33^2=1089=10·109−1` and `76=−33`. A square-discriminant condition in `M`, which would follow from a descended even permutation of the roots, is therefore compatible with the local residue. It is not forced by (5.1), and (5.1) supplies no contradiction.

The stop is sharp: none of (5.1) forces `w∈M`, constrains `A_infinity`, or descends a deck transformation. Claiming an obstruction here would have been a refutation of the report; the report does not claim one.

### 6. Both controls, including every displayed minpoly and deck assertion — CONFIRMED

**Finite-free non-Keller map.** Set `g_p(X)=X+(p-1)X^p` and `G_p=(g_p,y)`. Then

```text
g_p ≡ X − X^p (mod p),
```

because `p-1≡−1`. This is the `N=p` member of the parent family `g_N=X−X^p+p X^N`. Leading coefficient `p-1` is a `p`-adic unit, so `K[x]` is free of rank `p` on `{1,x,…,x^{p-1}}` over `K[g_p]`, and the formal fibre algebra `R[X]/(g_p(X)−U)` is finite free of rank `p` over `R`. In particular `A_infinity=0` and the generic degree is `p`. The Jacobian

```text
det J_{G_p} = 1 + p(p-1) x^{p-1} = 1 + 11772 x^{108}
```

is not the constant polynomial `1`. Mechanism control, not a Keller example.

Primitive generator. `y=V` already lies in `M=K(U,V)`, and `w=x y` gives `x=w/y` in the function field. Thus `L=M(w)`. The identity

```text
(p-1) w^p + y^{p-1} w − g_p(x) y^p = 0
```

is immediate in `Z[x,y]`:

```text
(p-1)(xy)^p + y^{p-1}(xy) − (x+(p-1)x^p) y^p
  = (p-1) x^p y^p + x y^p − x y^p − (p-1) x^p y^p
  = 0.
```

Dividing by the unit `p-1` produces the displayed monic field minpoly

```text
W^p + V^{p-1}/(p-1) W − U V^p/(p-1).
```

The denominators are `p-1∈Z_p^×`, so this monic polynomial in fact has coefficients in `Z_p[U,V]`. On the tube `U≡0`, `V≡1`, the linear coefficient is `1/(p-1)≡−1 (mod p)` and the constant term vanishes, hence `W^p−W`. (The integral non-monic form `(p-1)W^p+V^{p-1}W−U V^p` remains valid at `V=0`, where the substitution `x=w/y` is unavailable; the field minpoly is the monic form, and `y≠0` as an element of `L`.)

Rational deck group. Every `K`-automorphism of `K(x)` is Möbius. The polynomial `g_p` has a unique pole, at infinity, so an automorphism satisfying `g_p(φ(x))=g_p(x)` fixes infinity and has the form `φ(x)=αx+β`. Independent binomial expansion in `Z[α,β][x]`:

```text
[x^p]      = (p-1)(α^p − 1),
[x^{p-1}]  = (p-1)·p·α^{p-1} β,
[x^1]      = α − 1 + (p-1)·p·α β^{p-1}.
```

The `x^{p-1}` row receives no contribution from `αx+β`. Characteristic zero, `p(p-1)≠0`, and `α≠0` force `β=0`. Then `[x^1]=α−1`, so `α=1`. This comparison is *not* inherited from the parent’s `N>=p+2` argument (that argument excluded `N=p` and `N=p+1` because of an `X^p` contamination in `g_N`). It is a separate, cleaner expansion for the combined leading term `(p-1)X^p`. For the two-variable map, `y` is already in the base, so a graph coordinate `R` lies in the algebraic closure of `K(x)` inside `K(x,y)`, which is `K(x)`. Trivial deck group.

Precision, non-blocking: `Q_p` contains no primitive `p`-th root of unity, so `α^p=1` in `Q_p` already forces `α=1`. The `x^{p-1}` row is still the right first step, and it continues to kill `β` after any extension of `K` that does contain `μ_p`. The `x^1` row then kills a nontrivial `α` with `α^p=1`.

**Cyclic Kummer control.** Over a characteristic-zero field containing a primitive `p`-th root `ζ`, set `L=K(s,v)`, `M=K(s^p,v)`, `x=s+v`, `y=s+2v`. This is the degree-`p` member of the family already confirmed in the Moskowicz review: linear inversion `s=2x−y`, `v=y−x`, Jacobian of `(s^p,v)` equal to `p s^{p-1}≠0`, cyclic Galois with generator `s↦ζs`. Then

```text
xy = (s+v)(s+2v) = s^2 + 3 s v + 2 v^2.
```

A nonidentity power sends this to `ζ^{2k} s^2 + 3 ζ^k s v + 2 v^2`. The difference is `(ζ^{2k}−1)s^2 + 3(ζ^k−1)sv`. For `1≤k≤p−1` one has `ζ^k≠1`, and `3≠0` in characteristic zero, so the coefficient of `sv` is nonzero. Every nonidentity deck element moves `xy`. A deck group does not imply membership of a chosen source monomial. The control is not Keller, as required.

### 7. Univariate deck discriminator; no smuggled descent — CONFIRMED

Section 6 of the producer is explicitly conditional on `A_infinity=0` *and* on the existence of a rational `τ∈Aut_M(L)` descending `a↦a+1`. Claims 1–5 do not invoke `τ`. The Galois-Keller sentence at the end of §6 is the already-reviewed two-key implication, and is used only to record that a descended cycle closes the lift without (1.4).

Under those two extra hypotheses, `L=M(w)`, so `τ` is uniquely a polynomial in `w` of degree `<p`:

```text
τ(w) = R_τ(w),     deg R_τ < p,     R_τ ∈ M[Z].
```

On the tube, `τ` permutes the roots by construction as `w_a ↦ w_{a+1}`. The unique degree-`<p` interpolant of `p` points is given by a Vandermonde system. The Vandermonde `∏_{i<j}(w_j−w_i)` reduces modulo `p` to `∏_{i<j}(j−i)`, a unit of `F_p` (second-engine value `76`), hence is a unit of `R`. Interpolation coefficients therefore lie in `R`. Reducing the interpolant is the interpolant of the reductions, which is the unique degree-`<p` polynomial over `F_p` sending `a↦a+1`. A full `109×109` Vandermonde solve over `F_{109}` returns exactly `Z+1`. Thus

```text
R_τ(Z) ≡ Z+1  (mod (p, μ_w)).
```

Because `deg R_τ<p=deg μ_w`, reducing modulo `μ_w` does not change the polynomial: the congruence is `R_τ(Z)≡Z+1 (mod p)` as polynomials of degree `<p`. The iteration condition is `p`-fold *composition*, not a `p`-th power: `(Z+1)^{∘p}=Z+p=Z`. In characteristic `p` one has `(Z+1)^p=Z^p+1≡Z+1 (mod μ_w)`, which is *not* the identity; reading `R_τ^{[p]}` as a power would have been a gap, and is not what the display says.

These congruences do not follow from the symmetric coefficients of `μ_w`. The polynomial `μ_w` knows the set of roots, not the translation labelling. Any interpolant of an unlabelled permutation of `F_p` would be compatible with the same `μ_w`; `Z+1` is specifically the translation. Supplying `R_τ∈M[Z]` is equivalent to supplying the missing root permutation, i.e. to descent. The formal interpolant in `R[Z]` always exists; membership of its coefficients in the image of `M` is the unearned datum.

A descended `p`-cycle makes `L/M` cyclic Galois of prime degree. A `p`-cycle is an even permutation for odd `p` (`sign=(−1)^{p-1}=1`), so it preserves the Vandermonde and `Disc(μ_w)` is a square in `M`. This is a genuine conditional global coefficient constraint. It is compatible with `Disc≡−1` being a square residue, and is not a contradiction. After `A_infinity=0`, any single nonidentity element of `Aut_M(L)` already makes the extension Galois (`p` prime), and the reviewed Galois-Keller plus Hensel noninjectivity closes the lift without (1.4), without trace/norm, and without (6.5). The producer records this. Correct, and unearned.

The cyclic control of claim 6 is the exact negative companion: a descended cyclic group need not fix `xy`.

### 8. Scope firewall — CONFIRMED

The report assumes an exact finite polynomial lift and does not construct one. The theorem is that such a lift would satisfy `[M(xy):M]>=109`, hence would lie outside the hypothesis of the repaired Moskowicz second case. That is a no-go for a proposed bridge, not a no-go for the lift. The residual object `A_infinity` and the descent of a formal permutation remain exactly as in the parent gates. Trace, norm, and the local discriminant are explicit stops. The square-discriminant condition is only a consequence of the still-unearned cycle.

No result here proves `A_infinity=0`, descends a cycle, constructs or rules out an arbitrary-support lift, or proves or disproves JC2. The advertised Booleans `target_field_membership_forced=false`, `target_ring_membership_forced=false`, `exact_lift_found=false`, `support_enumeration=false`, `aws_used=false`, `jc2_inference=false` match the algebra. The freeze listing contains the report and `check.py`, which is the right scope for this client.

---

## Dependency and specialization caveats

- Logical dependency for claims 1–2 and 8 is the exact-lift hypothesis plus the confirmed Hensel-to-degree embeddings `σ_a:L→E`, specialized to the tube centre `b=1`. Parameter Hensel over `R` is the complete-ring inverse-function theorem already reviewed; this gate evaluates `w` on those embeddings.
- Claim 4 additionally consumes the reviewed implication `A_infinity=0 ⇒ d=p`. It does not consume a proof of `A_infinity=0`, a finiteness theorem for the formal fibre algebra, or the tropical ledger.
- Claim 3 consumes the repaired Moskowicz second-case implication only as a *target* of the no-go: (1.4) is a valid theorem whose hypothesis is false for an AS109 lift. The printed first case and the headline no-prime theorem are not inputs.
- Claim 6’s `G_p` is the `N=p` member of the parent `G_N` family, with a separate Möbius comparison. Claim 6’s Kummer control is the degree-`p` member of the family confirmed in the Moskowicz review. Neither is a Keller map.
- Digit carries are irrelevant. Hensel consumes packed `det J=1`.
- Reduction modulo `p` is applied only to elements of `R`. The embedding `M→E` is a field map, so coefficients of `μ_w` have no poles on the tube. Global congruences of those coefficients in `K[P,Q]` are not claimed.

---

## Exact scope exclusions

Do not read this file, or the producer, as any of the following:

- a construction of an exact lift, series lift, or complex point;
- a proof that no exact lift exists, or a bound on support;
- `A_infinity=0`, `d=p` unconditionally, or `109∣d`;
- descent of a formal branch permutation, a rational `C_{109}` deck transformation, or a global monodromy element of order `109`;
- a global integral equation `μ_w∈Z_p[P,Q][Z]`, or a square-discriminant contradiction;
- consumption of Moskowicz’s first case or headline no-prime theorem;
- a landing in or exclusion of the sheet-six book, or TDU at `td=109`;
- a JC2 proof or counterexample.

---

## Smallest missing hypothesis or overclaim

None of the eight claims is an existence theorem, a nonexistence theorem, a descent theorem, or a JC2 decision.

The smallest precision a reader could miss, and that this review therefore isolates, is that (4.3) identifies the *tube specialization* of the field minimal polynomial with an integral polynomial in `R[Z]`. It is not a global monic equation over the target coordinate ring. The lower bound (2.5) does not need that identification; the coefficient ledger (4.4) does, and is correctly scoped as local.

The specialization error that was available — counting distinct products on the characteristic-`p` fibre over `(0,1)` and declaring that the generic degree of `w` — is not committed. The load-bearing chain is the reviewed generic embeddings into `E` plus `p` distinct roots of `μ_w` in `E`.

The smallest genuinely missing objects remain the two parent keys: a theorem that kills `A_infinity`, and a descent of a rational deck map. This gate correctly refuses to invent them, and additionally shows that the membership bridge which would have fed the repaired Moskowicz second case points the wrong way.

---

## Promotion advice

Accept internally as an exact, hostile-confirmed packaging of the conditional implication

```text
exact AS109 lift  =>  [M(xy):M] >= 109, hence xy ∉ K(P,Q) and xy ∉ C(P,Q),
A_infinity=0      =>  L = M(xy) and μ_w ≡ Z^{109}−Z on the tube (P,Q)=(109S,1+109T).
```

Record it as a closed door on `AS109-XY-MEMBERSHIP` as a route to the repaired theorem (1.4), and as a primitive-generator statement available to any future client that independently proves `A_infinity=0`. Do **not** promote it into `APPROACHES.md` as a kill of avenue 19, as `A_infinity=0`, as deck descent, as a prime-degree exclusion, or as any JC2 implication. Successor work that wants a contradiction must still bring one of the two parent keys; evaluating `xy` on the Hensel sections does not supply them.

**Overall: CONFIRMED.**
