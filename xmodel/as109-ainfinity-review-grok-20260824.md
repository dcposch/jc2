# Hostile different-model review — AS109 `A_infinity` / DECK DESCENT

| Field | Value |
|---|---|
| Claim under review | Frozen AS109 `A_infinity` / deck-descent gate: residual rank equals the exact negative-weight valued multiplicity of a simple fibre; finiteness of the formal fibre algebra forces `d=p`; abstract étale/Zariski-Main data do not; Newton controls realize every residual rank with trivial rational deck group; self-fibre `L`-factors are exactly `Aut_M(L)`, and a descended `p`-cycle plus `A_infinity=0` is a two-key obstruction, not an automatic kill |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (precisions below; the missing keys `A_infinity=0` from `det J=1` and descent of the formal `p`-cycle are correctly *not* claimed) |
| Evidence tier | independent commutative algebra over `R=Z_p[[S,T]]` and the height-one DVR of `(p)`; Newton polygon and binomial deck expansion over `Z` (second engine, no producer imports); Jacobian criterion for étaleness; tropical fundamental theorem with exact initial-ideal multiplicity, not mixed volume; unmodified rerun of `cases/as109_ainfinity_20260824/check.py` as regression control only |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T11:07:00Z – 2026-08-24T11:20:00Z |
| Python | 3.14.6; stdlib only (`fractions.Fraction`, `math.comb`, integer dicts) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-ainfinity-deck-descent-gate-20260824.md` (SHA-256 `f1cf4991e92e502459ca6c61a3cb4d0e346a65e6221890c8c64a808ec2e3b64b`, matches the launch prompt)
- `cases/as109_ainfinity_20260824/check.py` (SHA-256 `84941b672e04fab735b5de31f39de28487672167d233caeffa08870a57665b7f`)
- `cases/as109_ainfinity_20260824/FREEZE.sha256` (SHA-256 `78f727709a3812b8052b641be575d5bfa18cd75b4accc4a3860fec96a4fa22a9`)

Predecessor Hensel-to-global-degree producer and its completed different-model review, same charged basis:

- `xmodel/as109-hensel-global-degree-cross-gate-20260824.md` (SHA-256 `7a7185c27fe245233173a173f9f0851326f18d83585ffb743970b2189f703133`)
- `xmodel/as109-degree-cross-review-grok-20260824.md` (SHA-256 `fb260d5ce622f05e5869bfc64d0497f54e219e9afe04308aa7f3355312af19c6`), overall **CONFIRMED**

Dual-confirmed AS109 Hensel / carry, reread against the same charged basis:

- `xmodel/as109-support-gate-20260824.md` (SHA-256 `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`) and different-model review `xmodel/as109-support-review-grok-20260824.md` (SHA-256 `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8`)
- carry erratum `xmodel/as109-support-gate-20260824-erratum.md` (SHA-256 `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb`) and `xmodel/as109-carry-erratum-review-grok-20260824.md` (SHA-256 `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212`), only to confirm that Hensel consumes the packed exact identity `det J=1`, not truncated digit equations

Dual-confirmed secant-idempotent materials, consumed only where the producer uses them as no-leverage:

- `xmodel/secant-idempotent-review-grok-20260824.md` (SHA-256 `6b0cb25dd3d1769f9f6c15116b6869b37c6cb1c89f17d9831ff19c67f20f09e9`)
- `xmodel/secant-as109-review-grok-20260824.md` (SHA-256 `16d052ae483fe5c829fb6416202a77c1707e7acc85b65bee249e794b16c51029`) and parent `xmodel/secant-as109-cross-gate-20260824.md` (SHA-256 `f4bd8ff7708469dd4ca1a6a6880634fb60ea2975fa1c7aa9fb3ecf5d61ba80cf`)

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer and parent-review artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No support compiler was implemented. No AWS call was made.

Write `p=109`, `K=Q_p`, `M=K(P,Q)`, `L=K(x,y)`, `d=[L:M]`, `R=Z_p[[S,T]]`. The exact-lift hypothesis is the existence of `F=(P,Q)` in `Z_p[x,y]^2` with `F mod p=(x-x^p,y)` and `det J_F=1` as a polynomial identity. Existence is not inferred. The predecessor theorem (confirmed) supplies

```text
L tensor_M E  ~=  E^p x A_infinity,       dim_E A_infinity = d-p,
```

over `E=Frac(R)`. This gate's new content is the valued description of the residual factor, the finiteness implication, the exact deck test, and the negative controls.

---

## Promotion

**Accept `EXACT REDUCTION + FINITE DISCRIMINATORS / NO AUTOMATIC KILL` at the stated scope.**

Under the conditional exact-lift hypothesis and the predecessor splitting:

- The formal fibre algebra `B=R[X,Y]/(P-pS, Q-pT)` is étale, finitely presented, and quasi-finite over `R`. Its special fibre splits as `p` reduced copies of `F_p[[S,T]]`. After height-one localization at `(p)` and completion, the `p` integral geometric generic roots are exactly the Hensel lifts of `(a,0)`, and every residual geometric root has a negative source valuation.
- Consequently `dim A_infinity = d-p` equals the number of geometric residual roots, equivalently the sum of exact valued-initial multiplicities at negative (extended) source weights, not a mixed volume. A named finite support therefore has a finite emptiness test for `A_infinity`.
- Finiteness of `B` over `R` forces rank `p` and `d=p`. Abstract étale models `R^p x (R[1/p])^r` show that Zariski Main, special splitting, and étaleness alone do not bound `r`. They are not polynomial Keller models.
- The family `G_N=(x-x^p+p x^N, y)` for `N>=p+2` has residual rank `N-p` and trivial rational deck group, so local Hensel/Newton/trace/secant data cannot force descent or a degree congruence.
- An `L`-factor of `L tensor_M L` is exactly an element of `Aut_M(L)`. One off factor, or one completed match `0 -> 1`, is not a `p`-cycle. A descended `p`-cycle gives `p|d`; with `A_infinity=0` it gives a Galois degree-`p` extension, and the classical Galois Keller theorem then contradicts Hensel noninjectivity. That two-key implication is conditional, not a lift obstruction.

**Do not promote this to:** `A_infinity=0` from `det J=1`; a bound or congruence on `d-p`; descent of a formal permutation; a complex projective-boundary identification of `A_infinity`; nonexistence of an exact lift; a support-compiler implementation; TDU at `td=109`; Moskowicz prime-sheet exclusion; or any JC2 decision.

**Keep the two bridges as resurrection targets, not theorems:** (i) exclude all common negative weights, or prove integral finiteness of `B`; (ii) factor the off self-fibre algebra and prove that a rational deck map acts as the displayed `p`-cycle. The second key may be weakened to “any off `L`-factor” *after* `A_infinity=0` is known, because `p` is prime (precision in claim 6, not a producer error).

---

## Quarantine

No result here proves or disproves JC2. Producer string `48/48 controls pass` was not used as evidence for étaleness, tropical multiplicity, or the Möbius comparison; those were re-derived. Generic uncarried two-layer digit equations remain as in the carry erratum: they are not the packed exact identity that Hensel consumes. Moskowicz's unpublished prime-degree claim is not consumed. The independent `deg_y<=5` frontier is not consumed. Secant ranks remain a restatement of `d>=p`. The classical Galois Keller theorem is a known-theorem input to the last sentence of (5.3) only (Campbell/Razar/Wright/Bass–Connell–Wright; already the knownness citation for the rank-two gate in `AUDIT.md`); it is not re-proved here and is not load-bearing until both keys are supplied.

---

## Scope (not enlarged)

One prime `p=109`, one seed `(x-x^{109},y)`, exact coefficient ring `Z_{109}` for a hypothetical polynomial lift, function fields over `K=Q_{109}`, one formal target tube `R=Z_{109}[[S,T]]`, and the height-one DVR obtained by localizing at `(p)` and completing. Characteristic-zero language is purely conditional on an exact integral polynomial lift that this run did not produce. No construction, no support grammar, no exponent rectangle, no AWS, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | `B=R[X,Y]/(P-pS,Q-pT)` is étale, finitely presented, and quasi-finite over `R`. Special fibre is the reduced split algebra `prod_{a in F_p} F_p[[S,T]]`. After height-one localization/completion, the integral geometric generic roots are exactly the Hensel lifts of `(a,0)`, and every residual root has `min(val X, val Y)<0` | **CONFIRMED** | Jacobian criterion failing with `det J=1` a unit in `B`; `X-X^p` multiple over `F_p`; an extra integral `O_Ω`-point not reducing to some `(a,0)`; a residual geometric root with both source valuations nonnegative; idempotents of `B/pB` lifted inside `B` itself and used to conclude `B ~= R^p` unconditionally |
| 2 | `dim A_infinity=d-p` equals the number of geometric residual roots, hence the sum of exact valued-initial multiplicities at negative source weights of the *fixed* simple system (axes included). The finite-support emptiness test is finite and exact. Mixed volume / generic stable intersection is not this count | **CONFIRMED** | mixed volume of the Newton polytopes used as `d-p`; torus `Trop(I)` without an axis correction in the discriminator; `in(f),in(g)` emptiness treated as insufficient for the vanishing direction; infinitely many candidate weights on a finite support; residue-field rational points counted without residue degree |
| 3 | `B` finite over `R` implies finite étale of constant rank `p`, hence `d=p` and `A_infinity=0`. The control `B_r=R^p x (R[1/p])^r` is finitely presented and étale, with special rank `p` and generic rank `p+r`. It rules out a bound from general étale/ZMT data, and is not a polynomial Keller model | **CONFIRMED** | finite étale rank jumping on a connected base; `R[1/p]/p R[1/p] != 0`; `B_r` not finitely presented; the producer presenting `B_r` as an irreducible Keller fibre; the converse `d=p => B` finite asserted |
| 4 | Newton polygon of `g_N(X)-pS` has lengths `1,p-1,N-p` with valuations `1,0,-1/(N-p)`. Residual rank of `G_N` is `N-p`; Jacobian is not the constant `1`. For `N>=p+2` the rational deck group of `K(x)/K(g_N)` (hence of `G_N`) is trivial, by unique pole, affine Möbius, and uncontaminated coefficient comparison | **CONFIRMED** | a different lower hull for some `N>p`; residual mass not `N-p`; `det J_{G_N}` the constant polynomial `1`; a nontrivial Möbius with `g_N(αx+β)=g_N(x)` at `N>=p+2`; `N=p+1` included in the uncontaminated `x^{N-1}` row |
| 5 | `L`-factors of `C_L=L tensor_M L` are exactly `Aut_M(L)`. One off factor or one completed `0->1` match is not a `p`-cycle. A descended `p`-cycle implies `p\|d`; with `A_infinity=0` one gets a Galois degree-`p` extension; classical Galois Keller plus Hensel then forbids an exact lift. The implication (5.3) is two-key and unearned | **CONFIRMED** | an `L`-algebra map `L->L` over `M` that is not an automorphism; the report treating one off factor as a `p`-cycle when `d>p`; `|Aut|` not dividing `d`; (5.3) stated unconditionally; Galois Keller applied to a non-Galois residual extension |
| 6 | Formal permutations of `E^p`, the projector `e_int` of trace `p`, the secant diagonal idempotent, and abstract monodromy/normalizer language do not descend the `p`-cycle. Components of `C_L` are `H`-orbits; rational deck maps are `N_G(H)/H`. No smaller *trace/secant* criterion was missed; a smaller *Aut* criterion exists after `A_infinity=0` (precision, not a refutation) | **CONFIRMED** | `S_p` of the split algebra already in `Aut_M(L)`; `e_int` an idempotent of the field `L` for `0<p<d`; the `p` Hensel labels already singleton `H`-orbits; a trace identity in the correction coefficients outside the localized collision ideal |
| 7 | Campaign utility is a fixed-support negative-weight discriminator and a separate finite graph-factor/`p`-cycle test, not an automatic lift obstruction. Scope exclusions and predecessor dependence are exact. Prime sheet number after `A_infinity=0` may consume only already-reviewed prime-degree theorems | **CONFIRMED** | the gate concluding `CONTRADICTION`; `A_infinity=0` from `det J=1`; TDU or Moskowicz consumed at `td=109`; a compiler written as a theorem of this freeze; (0.1) used without the predecessor; a complex-projective identification of `A_infinity` treated as proved |

All remarks below are non-blocking unless marked otherwise. None changes a Newton length, a rank, or a numbered verdict.

---

## Replay and hashes

Frozen producer hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-ainfinity-deck-descent-gate-20260824.md` | `f1cf4991e92e502459ca6c61a3cb4d0e346a65e6221890c8c64a808ec2e3b64b` | prompt and `FREEZE.sha256` |
| `cases/as109_ainfinity_20260824/check.py` | `84941b672e04fab735b5de31f39de28487672167d233caeffa08870a57665b7f` | prompt and `FREEZE.sha256` |
| `cases/as109_ainfinity_20260824/FREEZE.sha256` | `78f727709a3812b8052b641be575d5bfa18cd75b4accc4a3860fec96a4fa22a9` | self-hash of the freeze listing |
| `xmodel/as109-hensel-global-degree-cross-gate-20260824.md` | `7a7185c27fe245233173a173f9f0851326f18d83585ffb743970b2189f703133` | predecessor producer |
| `xmodel/as109-degree-cross-review-grok-20260824.md` | `fb260d5ce622f05e5869bfc64d0497f54e219e9afe04308aa7f3355312af19c6` | predecessor review |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | banked Hensel producer |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` | banked Hensel review |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` | carry erratum |
| `xmodel/as109-carry-erratum-review-grok-20260824.md` | `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212` | carry review |
| `xmodel/secant-idempotent-review-grok-20260824.md` | `6b0cb25dd3d1769f9f6c15116b6869b37c6cb1c89f17d9831ff19c67f20f09e9` | cited where used |
| `xmodel/secant-as109-cross-gate-20260824.md` | `f4bd8ff7708469dd4ca1a6a6880634fb60ea2975fa1c7aa9fb3ecf5d61ba80cf` | cited where used |
| `xmodel/secant-as109-review-grok-20260824.md` | `16d052ae483fe5c829fb6416202a77c1707e7acc85b65bee249e794b16c51029` | cited where used |

Registered command, rerun unmodified from the charged tree:

```sh
python3 cases/as109_ainfinity_20260824/check.py
```

Exit code 0. Final line `48/48 exact controls passed`. Stdout SHA-256 `f275413172e7c95031764436d3ecdf367c94241e2d75c72d159396ec027ecb23`. Locale warnings from the host `shasum` wrapper are not part of that digest.

The registered program is a finite arithmetic control suite, not a checker of étaleness, of `Trop(I)`, or of `Aut_M(L)`. It samples four degrees `N in {111,137,218,219}`, five residual ranks `r`, and four values of `d`. The Newton-hull block is a genuine lower-convex-hull computation. The Fermat block is a genuine residue computation. The Zariski-Main block is the tautology `special_rank=p`, `generic_rank=p+r`. The deck block is the Boolean pair `N-1>p` and `p*N != 0`, not a polynomial expansion. The secant block is `1+(d-1)=d`. Those Booleans were discarded as evidence for the field-theoretic claims; every numbered claim below is re-derived independently.

A second engine, written for this review and not imported from the registered script, used only `fractions.Fraction`, `math.comb`, and integer dictionaries. It recorded zero failures on: Fermat as functions on `F_{109}` and simplicity of `X-X^p`; the lower Newton hull and mass partition for every `N=110..124` and for `N in {217,218,219,327,334,552,1000,10000}` (trapezoid vertices, strictly increasing slopes `-1, 0, 1/(N-p)`, integral mass `p`, residual mass `N-p`); nonconstancy of `det J_{G_N}` at `N in {109,110,111,137,218,219,1000}`; binomial expansion of `g_N(αx+β)-g_N(x)` with `[x^N]=p(α^N-1)`, uncontaminated `[x^{N-1}]=p N α^{N-1} β` for `N>=p+2`, and `[x^1]=α-1-p α β^{p-1}+p N α β^{N-1}`; contamination of the `x^p` row at `N=p+1`; seed-only emptiness of residual initial forms on the torus and on both axes; the `G_N` tying weight `w_x=-1/(N-p)` strictly below the weights of `X` and `pS`; Zariski-Main ranks for `r` up to `1000`; and `d-1>=108` for `d=109..229`.

Process remark, non-blocking: `check.py` tests “affine deck comparison forces identity” by the separation Boolean, which is the *reason* the `x^{N-1}` row is uncontaminated, not the comparison itself. The comparison is the binomial expansion in claim 4.

---

## Independent recomputation

### 1. Formal fibre algebra, special split, integral vs residual roots — CONFIRMED

Assume the exact-lift hypothesis. Set `R=Z_p[[S,T]]` and

```text
B = R[X,Y] / (P(X,Y)-p S, Q(X,Y)-p T).
```

Finite presentation is immediate: polynomial ring in two variables, quotient by two elements.

Étaleness is the Jacobian criterion. The relative Kähler differentials of `B/R` are presented by `d(P-pS)=P_X dX+P_Y dY` and `d(Q-pT)=Q_X dX+Q_Y dY`. The determinant of this Jacobian is the constant polynomial `1`, a unit of `R` and therefore of `B`. Hence `Ω_{B/R}=0` and `B` is étale over `R` (standard étale / Jacobian criterion). Étale morphisms are finitely presented, flat, unramified, and locally quasi-finite. Quasi-finiteness of `Spec B -> Spec R` is therefore not an extra geometric input.

Special fibre. Reduction modulo `p` uses the seed `P ≡ X-X^p`, `Q ≡ Y`:

```text
B / pB  ~=  F_p[[S,T]][X,Y] / (X-X^p, Y)
        ~=  F_p[[S,T]][X] / (X-X^p).
```

Fermat gives `X^p-X = prod_{a in F_p}(X-a)` as polynomials over `F_p`. The factors `X-a` are pairwise coprime. The derivative of `X-X^p` is `1-p X^{p-1} ≡ 1 (mod p)`, so every geometric root is simple and the quotient is reduced. Chinese remainder yields

```text
B / pB  ~=  prod_{a in F_p} F_p[[S,T]].
```

The parameters `S,T` do not appear in the special equations. Geometric special points are exactly the `p` points `(X,Y)=(a,0)`.

Idempotent-lifting caveat, requested as a completion attack. The pair `(R,pR)` is Henselian (`R` is `p`-adically complete). Idempotents of `B/pB` therefore lift to the *`p`-adic completion* of `B`. They need not lift to `B` itself, because `B` is only quasi-finite, not a finite `R`-module, and need not be `p`-adically complete. Lifting inside `B` would split `B ~= R^p` and force `d=p` unconditionally; the producer does not do this. The sentence “the `p`-adic completion sees these sections; a component living only after inverting `p` has zero `p`-adic completion” is exactly the correct location of the `p` sections. (Independently, parameter Hensel over `R`, as in the predecessor, already produces `p` actual `R`-points of `Spec B`, i.e. sections over the full tube; that is stronger than DVR Hensel and is used below.)

Height-one localization and completion. The ideal `(p)` is prime because `R/(p)=F_p[[S,T]]` is a domain, and it has height one by Krull. The localization `R_{(p)}` is a regular local ring of dimension one, hence a DVR, with uniformizer `p` and residue field `Frac(F_p[[S,T]])`. Completing along `p` yields a complete DVR `O` with the same residue field `κ` and fraction field `E_0`. Every element of `R \ (p)`, in particular `S` and `T`, becomes a unit, so the Gauss valuation satisfies `val(S)=val(T)=0` and `val(pS)=val(pT)=1`. This is the vertical `p`-adic Gauss valuation on the tube, not an `(S,T)`-adic order and not a complex compactification at infinity.

Generic fibre. Let `Ω` be an algebraic closure of `E_0` (completion of that closure is harmless for valuations). The morphism `A^2 -> A^2` given by `F` is étale, hence the scheme-theoretic fibre over the point `(pS,pT)` — which has transcendence degree two over `K`, so is generic — consists of `d` simple geometric points. Rank of `B tensor_R E_0` equals `d` by scalar extension from `K(S,T)` to `E_0`, using predecessor (0.1). Simplicity is `det J_F=1`.

Integral points are precisely the Hensel lifts of `(a,0)`. An `Ω`-point of the generic fibre with both source coordinates in the valuation ring of `Ω` is an `O_Ω`-point of `A^2` satisfying the two equations, hence an `O_Ω`-point of `Spec B`. It reduces to a geometric point of the special fibre, therefore to some `(a,0)`. Each of those `p` special points is simple, so Hensel supplies a unique unramified lift, already defined over `O` (in fact the predecessor supplies it over `R`). Étaleness forbids extra ramified integral lifts: a ramified integral point would still reduce to some `(a,0)` and would have to coincide with the unique lift. There are no other geometric special points, even after extending `κ`, because `X^p-X=0`, `Y=0` has only the `p` solutions in any extension of `F_p`.

Every residual geometric root therefore fails integrality of both coordinates, i.e. `min(val(X),val(Y))<0`. Conversely the `p` Hensel points are integral. This is the integral meaning of predecessor (0.1): `A_infinity` records sheets that escape the chosen integral model in the vertical `p`-adic direction. The producer correctly refuses to identify this with a component of a complex projective compactification; that comparison is an additional infinity theorem, not this gate.

### 2. Exact tropical ledger; axes, saturation, residue degree; finite test — CONFIRMED

Write `I=(P-pS, Q-pT)` in `Ω[X,Y]`. The scheme `V(I)` is zero-dimensional of length `d`, reduced (every geometric root simple). Partition the `d` geometric points according to `w(z)=(val(u),val(v))` in the extended value group `Q ∪ {+∞}`, with `val(0)=+∞`. Claim 1 gives

```text
d-p  =  number of geometric roots with min(val(u),val(v)) < 0.     (0.2)
```

This equality does not use tropical geometry. It is the content of claim 1 plus simplicity.

Tropical packaging. The fundamental theorem of tropical geometry, for a zero-dimensional ideal over a complete algebraically closed valued field, identifies the valuation vectors of the *torus* points `V(I) ∩ (Ω*)^2` with `Trop(I) ⊂ R^2`, and identifies the tropical multiplicity `mult_w(I)` with the length of the initial ideal `in_w(I)` in the Laurent polynomial ring over the residue field (equivalently, the number of geometric torus points of that valuation, counted with scheme multiplicity). Because every geometric root is simple, scheme multiplicity on the valued side is geometric multiplicity one; several simple roots may share a valuation vector, in which case `mult_w(I)` is their number, possibly realized as a nonreduced initial scheme, and the “usual valued lifting check” is the Newton–Puiseux refinement. This is the exact valued-Groebner multiplicity of the *fixed* coefficient system. It is not the stable intersection number of two bare Newton polygons, and it is not the mixed volume of those polygons. Mixed volume would count torus solutions of a *generic* coefficient system with the same supports, would include the nonnegative-weight mixed cells (the integral torus roots), and can strictly overcount the special-seed system. The producer’s refusal is load-bearing and correct.

Axes / extended Trop, the tropical error that was available. Classical `Trop(I) ⊂ R^2` sees only finite valuations. A residual axis point — `Y=0` and `val(X)<0`, or `X=0` and `val(Y)<0` — has an infinite coordinate and is invisible to torus tropicalization. For the AS109 shape `Q=Y+p Q_1`, the axis `Y=0` becomes `Q_1(X,0)=T`, which can have negative-valuation roots whenever `Q_1` has an `X`-only part. Formula (2.2) as a subset of `R^2` therefore equals the residual *torus* mass, not automatically `d-p`. Headline (0.2) remains exact. The algorithm in producer §2 step 3 (“saturating by the relevant torus coordinates and handling axes separately”) restores completeness: substitute `X=0` or `Y=0` and run a univariate Newton polygon. Interpreting `Trop(I)` in the extended space `(R ∪ {+∞})^2`, with `mult_w` the corresponding initial multiplicity, makes (2.2) identical to (0.2). This is a wording precision, not a wrong count: the discriminator the gate actually proposes is the complete one, and (0.2) is the equality used for `A_infinity=0`.

Torus saturation and generators versus the ideal. A weight `w` lies in the torus tropicalization of a hypersurface `{f=0}` if and only if at least two terms of `f` achieve the minimum weight (a single monomial never vanishes on the torus). Enumerating pairwise term-tying hyperplanes is therefore complete for torus residual roots. The two initial forms satisfy `(in_w(P-pS), in_w(Q-pT)) ⊂ in_w(I)`, so `V(in_w(I)) ⊂ V(in_w P, in_w Q)`. Emptiness of the two-form initial system implies emptiness of `Trop` at that weight. This direction is one-sided safe and is exactly the vanishing test “every retained initial system empty ⇒ `A_infinity=0`”. The converse, when the two-form system is nonempty, may overcount: extra generators of `in_w(I)` can cut the locus, and a one-dimensional two-form locus is not a tropical 0-cell of `I`. The producer’s “exact residual rank after the usual valued lifting check” and the phrase “valued-Groebner multiplicity of the fixed coefficient system” name `in_w(I)`, not mixed volume and not the naive complete intersection of two initial forms. Non-blocking wording tension only on the nonempty-multiplicity side.

Geometric versus residue degree. The integer `dim_E A_infinity=d-p` is an `E`-rank. A residual closed point of residue degree `f` contributes `f`. Tropical multiplicity as the length of `\bar κ[X^{±},Y^{±}]/in_w(I)` counts geometric initial points over an algebraic closure of the residue field; the completed algebraic closure of `E_0` has algebraically closed residue field, so this length is the contribution to geometric rank, matching `d-p`. Counting only `κ`-rational initial points would undercount. Headline (0.2) says “generic roots” and is the geometric count.

Finiteness and exactness of the support test. A named finite support has finitely many monomials, hence finitely many pairwise tying hyperplanes in `R^2`, hence finitely many candidate 0-cells, with rational coordinates determined by integer coefficient valuations. Axes add two univariate Newton polygons, also finite. For each retained negative weight, emptiness of the saturated initial system is a finite Gröbner computation over a finitely generated coefficient ring (after including `det J=1` if desired). Exact for the vanishing direction. If some initial system survives, its `in_w(I)`-length plus lifting is the exact residual contribution, not an existence proof of a global lift. The producer states both.

Coefficient-valuation caveat, non-blocking. For a fully specified coefficient candidate the valuations are known. For a support family, extra coefficients of `P_1,Q_1` in `Z_p` may have valuation `0` or `>0`. The one-sided filter “incapable of tying the seed leading terms at any negative weight” is safest at unit extra valuation: higher valuation only makes extra terms less visible. Seed-only (no correction) was checked independently: at every `w` with `min(w_x,w_y)<0` some seed initial form is a torus-nonvanishing monomial or a unit (`pS` or `pT` with residue a unit), and both axes are empty because `P(0,Y)-pS=-pS` and `Q(X,0)-pT=-pT`. A correction support that cannot tie at negative weight therefore cannot carry an `A_infinity` sheet. A surviving negative initial system is a candidate mechanism, not a lift.

The test does not contradict a lift when it returns `A_infinity=0`: it proves `d=p` for that support. A stronger contradiction still needs a reviewed degree-`p` obstruction or the deck bridge (5.3). The producer says this. Correct.

### 3. Finiteness implies `d=p`; Zariski-Main control does not bound `r` — CONFIRMED

If `B` is finite as an `R`-module, then finite + étale implies finite étale, hence finite locally free. The base `Spec R` is connected (`R` is a domain), so the rank is constant and equals the special-fibre rank `p`. Scalar extension to `Frac(R)` or to `E_0` preserves that rank, and the generic fibre rank is `d` by claim 1. Thus

```text
B finite over R  ==>  d=p  ==>  A_infinity=0.
```

The converse is not used and is not true on general quasi-finite grounds: Zariski’s Main Theorem embeds `Spec B` as an open subscheme of a finite `R`-scheme, and the open immersion need not be surjective. Generic components can miss the special fibre by meeting the omitted boundary over `p=0`. Equality `d=p` does not, without more work, restore finiteness of the original model over every locus of `Spec R`.

Negative control. For `r>=0` set

```text
B_r  =  R^p  ×  (R[1/p])^r.
```

Each factor `R[1/p] ≅ R[U]/(pU-1)` is finitely presented. A finite product of finitely presented `R`-algebras is finitely presented (explicitly: orthogonal idempotents `e_1,...,e_p,f_1,...,f_r` summing to `1`, together with `p u_j = f_j`). Jacobian criterion for `pU-1`: the derivative in `U` is `p`, invertible in `R[1/p]` because `pU=1`. Localization at an element is étale. A product of étale algebras is étale. Special fibre:

```text
R[1/p] / p R[1/p]  =  0,
```

because `p` is a unit, so `(R/p)[U]/(-1)=0`. Thus `B_r / p B_r ≅ (R/p)^p`. Generic fibre: `R[1/p] tensor_R Frac(R) = Frac(R)`, so the generic rank is `p+r`. Quasi-finite: fibres are empty or a point.

This rules out precisely the claim that special splitting, étaleness, quasi-finiteness, and Zariski Main bound `dim A_infinity`. It does not model a polynomial Keller fibre: `det(pU-1)/dU=p` is a unit in the localization, not a unit already in `R`, and `B_r` is split rather than a relative complete intersection `R[X,Y]/(P-pS,Q-pT)` with Jacobian the constant polynomial `1`. A residual Keller factor could be a field of degree `r` rather than `E^r`; that does not disturb the negative rank statement. A bound under the full polynomial `det J=1` hypotheses would be new global input, as the producer says.

Finiteness of a characteristic-zero Keller map over the whole target is essentially properness and would settle that map. Finiteness only over the AS109 formal tube is weaker, a legitimate special-seed target, and still would not make the global map proper. Correct.

### 4. Newton polygon, residual rank `N-p`, trivial deck group — CONFIRMED

Let `g_N(X)=X-X^p+p X^N` and solve `g_N(X)=pS` over the DVR of claim 1, with `S` a unit. Coefficient valuation points of `g_N(X)-pS`:

```text
(0,1), (1,0), (p,0), (N,1).
```

For every integer `N>p` these four points form a trapezoid whose lower-edge slopes

```text
-1,     0,     1/(N-p)
```

are strictly increasing. The lower convex hull therefore uses all four vertices. Horizontal lengths and root valuations (valuation `=` minus slope):

```text
length 1:      valuation 1,
length p-1:    valuation 0,
length N-p:    valuation -1/(N-p).
```

The three lengths sum to `N`, so every root of the degree-`N` polynomial is accounted for. Integral mass (`val>=0`) is `p`; residual mass is `N-p`. Geometric meaning of the edges, independently of the registered hull code: the first edge is the tie `X` versus `-pS`, one root `X ~ pS` of valuation `1` (the Hensel lift of `a=0`); the middle edge is the tie `X` versus `-X^p`, initial form `X-X^p`, giving the `p-1` unit roots (Hensel lifts of `a in F_p^x`); the last edge is the tie `-X^p` versus `p X^N` at `w_x=-1/(N-p)`, initial torus equation `p U^{N-p}=1`. The residual initial is separable for `N>=p+2` (`N-p>=2`, `U≠0`, derivative `(N-p)U^{N-p-1}≠0`), so those `N-p` roots are simple.

For `G_N=(g_N(x),y)` the second coordinate is `Y=pT` of valuation `1`, hence integral. Generic degree is `[K(x,y):K(g_N,y)]=[K(x):K(g_N)]=N`, because `K[x]` is free of rank `N` over `K[g_N]` on `{1,x,...,x^{N-1}}` and the leading coefficient is `p≠0`. Thus `A_infinity` has rank `N-p`. The Jacobian

```text
1 - p x^{p-1} + p N x^{N-1}
```

is not the constant polynomial `1`: for `N≠p` the two extra degrees `p-1` and `N-1` are distinct and both coefficients are nonzero in characteristic zero; for `N=p` it is `1+p(p-1)x^{p-1}`. Mechanism control, not a Keller example. It realizes every nonnegative residual rank while preserving the AS109 special fibre and its simple Hensel sections.

Deck group of `K(x)/K(g_N)`, `N>=p+2`. Every `K`-automorphism of `K(x)` is Möbius. The polynomial `g_N` has a unique pole, at infinity, of order `N`. An automorphism `φ` satisfying `g_N(φ(x))=g_N(x)` as rational functions must send that unique pole to itself, so `φ(∞)=∞` and `φ(x)=αx+β`. Independent binomial expansion of `g_N(αx+β)-g_N(x)` in `Z[α,β][x]`:

```text
[x^N]      = p(α^N - 1),
[x^{N-1}]  = p N α^{N-1} β,
[x^1]      = α - 1 - p α β^{p-1} + p N α β^{N-1}.
```

The `x^{N-1}` row receives no contribution from `-(αx+β)^p` because `N-1>p`. Characteristic zero, `p≠0`, `N≠0`, and `α^N=1` (so `α≠0`) force `β=0` from the middle row. Then `[x^1]=α-1`, so `α=1`. The automorphism is the identity. At `N=p+1` the `x^p` row *is* contaminated (`-(αx+β)^p` contributes `-α^p`, and `p(αx+β)^{p+1}` contributes `p(p+1)α^p β`); the exclusion `N>=p+2` is necessary for the written comparison, and the producer does not claim deck triviality at `N=p` or `N=p+1`.

Two-variable deck group of `G_N`. An `M`-automorphism of `L=K(x,y)` over `M=K(g_N,y)` has graph `(R,S)` in `L^2` with `g_N(R)=g_N(x)` and `S=y` (the second coordinate of `G_N` is already in the base). Then `R` is a root of the univariate polynomial `U-U^p+p U^N-g_N(x)` over `K(x)`. The algebraic closure of `K(x)` inside `K(x,y)` is `K(x)` itself (`K(x,y)/K(x)` is purely transcendental). Hence `R∈K(x)`, and the one-variable computation applies. The producer’s sentence that `y` is already in the base field is this standard observation, slightly compressed; the missing word is that `R` cannot involve `y`. Non-blocking.

These controls simultaneously have `p` formal integral branches, all formal factor permutations of `E^p`, arbitrary residual rank, and no rational deck map. They stop any argument that uses only the local Hensel split, Newton count, trace, or abstract secant idempotents. They do not stop an argument that uses the exact constant-Jacobian equations globally.

### 5. Self-fibre graph equivalence, no fake `p`-cycle, two-key obstruction — CONFIRMED

The generic self-fibre algebra

```text
C_L = L tensor_M L  ~=  L[X,Y] / (P(X,Y)-P(x,y), Q(X,Y)-Q(x,y))
```

is finite étale of rank `d` over `L`. An `L`-algebra projection `C_L -> L` is an `M`-homomorphism `L -> L`. Because `L` is a field and `[L:M]<∞`, any such homomorphism is injective and surjective, hence an automorphism. Conversely every element of `Aut_M(L)` is such a projection, with graph `X=R(x,y)`, `Y=S(x,y)` in `L` and `F(R,S)=F(x,y)`. Multiplication gives the diagonal factor (the identity). Factorization of `C_L`, or a search for a rational graph, is therefore an exact finite descent test.

The producer’s correction is mandatory when `d>p`. An off-diagonal `L`-factor is one nonidentity deck automorphism, of unspecified order; it need not preserve the set of `p` integral Hensel factors (it may mix them with `E`-factors inside `A_infinity`), and if it does, the induced permutation need not contain the cycle `a |-> a+1`. A completed match of the `a=0` branch to the `a=1` branch is one ordered pair. Continuation around the remaining labels is global monodromy information, not a formal consequence of one pair. A transposition-like action sending `0` to `1` and `1` to `0` matches that pair and is not a `p`-cycle.

If the induced permutation of the `p` integral factors *does* contain the cycle `a |-> a+1`, the acting element has order divisible by `p` (the permutation order is a multiple of `p`; Cauchy’s theorem is slightly overquoted here — the cyclic subgroup generated by a suitable power already has order `p` — non-blocking). For a finite separable extension, `|Aut_M(L)|` divides `d`: if `N/M` is a Galois closure with `H=Gal(N/L)`, then `Aut_M(L) ≅ N_G(H)/H` and `|N_G(H)|` divides `|G|`, so `|Aut|` divides `[G:H]=d`. Thus `p|d`.

If also `A_infinity=0`, then `d=p`. Combined with `p` dividing `|Aut|` and `|Aut|` dividing `p`, one has `|Aut|=d`, so `L/M` is Galois of prime degree, hence cyclic. The classical Galois case of the Jacobian conjecture (Campbell, Razar, Wright, Bass–Connell–Wright: a Keller map whose function-field extension is Galois is an automorphism) then forces `F` to be an automorphism. Hensel already supplies `p` distinct points of `Z_p^2` over the target `(0,0)`, contradicting injectivity. After Lefschetz embedding of a finitely generated coefficient field into `C` (predecessor claim 4, confirmed) the same contradiction is the complex Galois-Keller theorem plus `d=p≠1`.

This known-theorem step is a dependency of the last sentence of (5.3), not a lemma of this freeze, and is not load-bearing until both keys are supplied. It is the same classical pointer already used as knownness for the rank-two gate. The two-key implication

```text
A_infinity=0  +  rational descent of the p-cycle  ==>  no exact lift
```

is correctly conditional. Neither key is supplied by residue-ball Hensel, by Newton, or by this gate.

### 6. Trace, idempotent, secant, monodromy: no leverage; smaller Aut criterion — CONFIRMED

After base change, `E^p` admits all `p!` permutations as `E`-algebra automorphisms. These are automorphisms of a split scalar extension, not elements of `Aut_M(L)`. Descent would additionally require that the `p` images `σ_a(L) ⊂ E` coincide and that the permutation preserve the residual factor as an `M`-structure. Hensel gives neither. This is the predecessor’s monodromy firewall, re-used correctly.

The projector `e_int=(1,...,1,0)` in `E^p × A_infinity` has multiplication trace `p`. Trace does not make it descend. The only idempotents of the field `L` are `0` and `1`. For `0<p<d` the element `e_int` is neither. For `d=p`, `e_int=1` is the unit of `L` and carries no cyclic symmetry. Descent of an idempotent of the étale algebra requires invariance under the full monodromy action; a numerical trace is not such an invariance. The dual-confirmed secant-AS109 review already recorded that trace `109` on the target fibre is a rank, not a coefficient identity; this gate does not reopen that costume.

The secant diagonal idempotent of `C_L` splits the diagonal from the off algebra of rank `d-1`. Over one completed source branch the other integral Hensel sections account for `p-1=108` off branches, and `d-1>=108` is exactly `d>=p`. Splitting the aggregate off algebra does not split each formal branch as an `L`-factor. A polynomial factorization of those `108` sectors is the missing global bounded off-datum of the secant cross-gate, not a corollary of the idempotent.

Group language. Let `G` be the geometric monodromy group of a Galois closure acting transitively on the `d` sheets, and let `H` be a sheet stabilizer. The primitive idempotents of `C_L` correspond to `H`-orbits on `H\G`. The factors isomorphic to `L` as `L`-algebras are the singleton `H`-orbits, i.e. the elements of `N_G(H)/H ≅ Aut_M(L)`. Labelling `p` sheets after the formal base change `E` gives no assertion that those labels are singleton `H`-orbits; they split over `E`, not over `L`. That missing orbit statement is the deck-descent problem. Correct.

Smaller descent criterion the producer did not write, and did not contradict. Because `p` is prime, `|Aut_M(L)|` divides `d`, and `A_infinity=0` forces `d=p`, any single off-diagonal `L`-factor already implies `|Aut|=p=d`. The extension is then Galois of degree `p` without a separate `p`-cycle check: a nontrivial automorphism of a degree-`p` extension generates, and the regular action on the `p` embeddings is a `p`-cycle automatically. Thus, *after* `A_infinity=0`,

```text
A_infinity=0  +  any one off L-factor  ==>  no exact lift,
```

via the same classical Galois Keller plus Hensel. When `d>p` the producer’s distinction stands: one off factor is not a `p`-cycle and does not give `p|d` without inspecting the induced permutation. The written two-key test (5.3) is sufficient in all cases and redundant on the cycle side only once residual rank vanishes. This is an enhancement of the descent bridge, not a missed trace, secant, or tropical kill, and it does not produce an automatic obstruction (the first key is still missing).

No smaller *trace/idempotent/secant/monodromy* criterion was found. Projectors onto proper subsets of the `p` branches are still idempotents that cannot live in the field `L`. A resolvent factorization of the self-fibre is exactly the graph test of claim 5.

### 7. Campaign utility, scope firewall, predecessor dependence — CONFIRMED

The predecessor bound remains `d>=p`. Formula (0.2) upgrades the slack `d-p` to an exact nonnegative integer ledger. Success of the infinity bridge sets `d=p=109` and does not land in the active `td=6` book. Prime sheet number then may invoke only those prime-degree results whose hypotheses have already been reviewed (promoted TDU excludes *single-pole* configurations at prime `td`, and still leaves multi-pole). It is not permission to consume Moskowicz. The producer does not consume either. Correct.

Fixed-support compiler order in §8.2 — impose reduction and `det J=1`, enumerate negative common tropical weights, test saturated initial systems (axes included), and only then run full coefficient elimination — is the cheapest exact discriminator for a named support, and is not a generic sparse search. It can reject a support incapable of carrying residual sheets, or certify `d=109` for that support. It is not a lift obstruction.

Self-fibre factorization in §8.3 is the corresponding exact deck discriminator. Dividing out the diagonal first, searching the off algebra for an `L`-linear graph, and computing the action on all `p` completed Hensel branches is the right procedure. Merely finding an off idempotent or matching one ordered pair is insufficient, except for the prime-degree collapse recorded in claim 6 after `A_infinity=0`.

Scope firewall, reread against the body. The report does not prove `A_infinity=0` from `det J=1`; a general bound or congruence on `d-p`; descent of a formal branch permutation; that `A_infinity` is a complex projective-boundary component; or nonexistence of an AS109 exact lift. Those exclusions match the algebra. Resurrection conditions (named support, a finiteness theorem for (1.1), a factorization exhibiting the `109`-cycle, or a reviewed degree-`109` obstruction) are exactly the inputs that would make one of the two bridges fire. Until then the output is a finite two-gate architecture, not a contradiction.

Predecessor dependence is clean. The splitting (0.1) is the confirmed Hensel-to-degree theorem. The present gate identifies the residual factor with negative-valuation sheets (new), gives a finite test for its vanishing on a named support (new), and gives an exact Aut-test for descent (new). It does not silently upgrade (0.1) to `A_infinity=0` or to a deck group.

---

## Dependency and valued-field caveats

- Logical dependency for claims 1–7 is the exact-lift hypothesis, the confirmed predecessor splitting (0.1), and standard commutative algebra (Jacobian criterion, Henselian pairs, Zariski Main, finite separable extensions) together with the reduction hypotheses of the dual-confirmed AS109 Hensel lemma (`F_bar=(x-x^p,y)`, `J(F_bar)=I`, Fermat). Parameter Hensel over `R` is the complete-ring inverse-function theorem, not a silent upgrade of the DVR lemma’s *conclusion*.
- Digit carries are irrelevant. The carry erratum quarantines uncarried `E1`/`E2`; this gate never uses them. Hensel consumes packed `det J=1`.
- The valuation is the vertical `p`-adic Gauss valuation after localizing `R` at the height-one prime `(p)`: `val(S)=val(T)=0`, `val(pS)=val(pT)=1`, residue field `Frac(F_p[[S,T]])`, value group `Z` on `E_0` and `Q` on an algebraic closure. It is not the `(S,T)`-adic order, not an archimedean size, and not the order of vanishing at a complex divisor at infinity.
- Tropical multiplicities are lengths of initial ideals of the fixed system, including axes as `val=∞` or as separate univariate Newton polygons, and including residue degree. They are not mixed volumes.
- Classical Galois Keller is a known-theorem input to the last step of (5.3) only. Secant parent reviews are no-leverage restatements.

---

## Exact scope exclusions

Do not read this file, or the producer, as any of the following:

- a construction of an exact lift, series lift, or complex point;
- a proof that no exact lift exists;
- `A_infinity=0` from `det J=1`, or any bound/congruence on `d-p`;
- descent of a formal branch permutation, a rational `C_{109}` deck transformation, or a global monodromy element of order `109`;
- an identification of `A_infinity` with a complex projective-boundary component;
- a proof that `B` is finite over `R`;
- a support-compiler implementation, an enumerated core, or an AWS search;
- a landing in or exclusion of the sheet-six book, a TDU statement at `td=109`, or Moskowicz prime-sheet exclusion;
- a coefficient rank from the secant idempotent or from `tr(e_int)=p`;
- a JC2 proof or counterexample.

---

## Smallest missing hypothesis or overclaim

None of the seven claims is an existence theorem, a nonexistence theorem, a degree congruence, or a JC2 decision.

The smallest precision a reader could miss, and that this review therefore isolates, is that formula (2.2) with classical torus `Trop(I) ⊂ R^2` is the residual *torus* mass. Headline (0.2) and the algorithm (axes separate, torus saturation, exact `in_w(I)` after lifting) are the complete exact count. No mixed-volume substitution occurs.

The smallest genuinely missing objects remain the two keys named by the producer: a theorem that kills `A_infinity` (finiteness of `B`, or empty negative initial systems on a named support, or a support-specific upper bound `d<=p`), and a descent of a rational deck map that acts as the displayed `p`-cycle (or, after `A_infinity=0`, any single off `L`-factor). Either would be a new paper. Residue-ball Hensel, Newton, trace, secant, and Zariski Main do not supply them.

A completion error that was available — lifting the special-fibre idempotents inside `B` rather than in the `p`-adic completion, and concluding `B ~= R^p` for every étale quasi-finite model — is not committed. The control `B_r` exists precisely to block that error.

---

## Promotion advice

Accept internally as an exact, hostile-confirmed packaging of the conditional architecture

```text
exact AS109 lift
  =>  d-p = exact negative-weight residual multiplicity,
      B finite over R => d=p,
      L-factor of C_L  <=>  Aut_M(L),
      (A_infinity=0 and descended p-cycle) => no lift,
      and none of these keys is supplied by Hensel, ZMT, trace, or secant.
```

Record it as two independent finite discriminators (negative-weight support filter; self-fibre graph/`p`-cycle test), and as a lane that does **not** close AS109. Do **not** promote it into `APPROACHES.md` as a kill of avenue 19, as `A_infinity=0`, as `109|d`, as a properness theorem, as a TDU-at-109 statement, or as any JC2 implication. Do **not** answer it by writing the support compiler or by launching AWS. Successor work that wants a contradiction must bring one of the four resurrection inputs in producer §9; this gate correctly refuses to invent them.
