# Hostile different-model review — AS109 HENSEL TO GLOBAL DEGREE

| Field | Value |
|---|---|
| Claim under review | Frozen Hensel-to-global-degree / monodromy cross-gate: under a conditional exact AS109 lift, `d=[Q_109(x,y):Q_109(P,Q)]>=109`, the generic algebra splits as `E^{109} x A_infinity` over a formal target tube, and local residue-ball data supply neither a congruence, a deck group, nor a lift obstruction |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (precisions below; the missing bridges `A_infinity=0` and descent of the formal `C_109` relabelling are correctly *not* claimed) |
| Evidence tier | independent field theory over `Q_109` and `Frac(Z_109[[S,T]])` (Kähler independence, kernel-height, Hom-bound without algebraic closure, finite-locally-free scalar extension); a second sparse engine that does not import the producer replay; unmodified rerun of `cases/as109_degree_cross_20260824/check.py` as regression control; banked Hensel lemma as previously dual-confirmed, rechecked as complete-ring parameter Hensel rather than DVR pointwise noninjectivity |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T10:48:00Z – 2026-08-24T11:05:00Z |
| Python | 3.14.6; stdlib only (`math.comb`, integer dicts) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-hensel-global-degree-cross-gate-20260824.md` (SHA-256 `7a7185c27fe245233173a173f9f0851326f18d83585ffb743970b2189f703133`, matches the launch prompt)
- `cases/as109_degree_cross_20260824/check.py` (SHA-256 `c0587c220cc9ca0e92bf8cd57fab466787ca6caa88fb61c8aceb7affb806f7b7`)
- `cases/as109_degree_cross_20260824/FREEZE.sha256` (SHA-256 `75b04b7c55748da5025d274582d007b593e9d0cd35a2af10694038fbb3a3adbf`)

Dual-confirmed AS109 Hensel / carry, reread against the same charged basis:

- `xmodel/as109-support-gate-20260824.md` (SHA-256 `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`) and different-model review `xmodel/as109-support-review-grok-20260824.md` (SHA-256 `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8`)
- carry erratum `xmodel/as109-support-gate-20260824-erratum.md` (SHA-256 `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb`) and `xmodel/as109-carry-erratum-review-grok-20260824.md` (SHA-256 `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212`), only to confirm that Hensel consumes the packed exact identity `det J=1`, not truncated digit equations

Cited secant / sheet-ledger statements, consumed only where the producer uses them:

- `xmodel/secant-idempotent-review-grok-20260824.md` (SHA-256 `6b0cb25dd3d1769f9f6c15116b6869b37c6cb1c89f17d9831ff19c67f20f09e9`)
- `xmodel/secant-as109-review-grok-20260824.md` (SHA-256 `16d052ae483fe5c829fb6416202a77c1707e7acc85b65bee249e794b16c51029`) and parent `xmodel/secant-as109-cross-gate-20260824.md` (SHA-256 `f4bd8ff7708469dd4ca1a6a6880634fb60ea2975fa1c7aa9fb3ecf5d61ba80cf`)
- `ladder/SHEET6.md` canonical checksum (eight terminal classes; Moskowicz prime-degree claim flagged unvetted)
- `ladder/SHEET6-TDUNIFORM.md` promoted Theorem TDU (single-pole entry exclusion at every prime `td`)
- `PROGRESS.md` line that TDU is promoted; `APPROACHES.md` avenue 44 (Moskowicz unvetted)

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer and parent-review artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No enumerator was written or run. No infinity-gate successor was attempted. No AWS call was made.

Write `p=109`, `K=Q_109`, `M=K(P,Q)`, `L=K(x,y)`, `d=[L:M]`, `R=Z_109[[S,T]]`, `E=Frac(R)`. The exact-lift hypothesis is the existence of `F=(P,Q) in Z_109[x,y]^2` with `F mod 109=(x-x^{109},y)` and `det J_F=1` as a polynomial identity. Existence is not inferred.

---

## Promotion

**Accept `EXACT SCOPED THEOREM / NO NEW CONTRADICTION` at the stated scope.**

Under the conditional exact-lift hypothesis:

- `P,Q` are algebraically independent over `K`, `L/M` is finite separable of some degree `d`, and `d` is the generic (algebraic mapping) degree.
- Parameter Hensel over `R` supplies 109 distinct `M`-embeddings `L -> E`, hence `d>=109`, and the finite étale algebra splits as `L tensor_M E ~= E^{109} x A_infinity` with `dim_E A_infinity=d-109`.
- After descent to a finitely generated coefficient field and an abstract embedding into `C`, the complex Keller map has the same generic degree, still with constant Jacobian one.
- Local formal monodromy fixes the 109 displayed sheets. No inertia element, no rational `C_109` deck group, no divisibility `109|d`, and no congruence for `d` follow. The triangular controls `G_N` realize every integer degree `N>=109` with the same residue-ball mechanism once constant Jacobian one is dropped.

**Do not promote this to:** existence of a lift; a new AS109 nonexistence result; a degree congruence or `109|d`; elimination of `A_infinity`; a properness or finiteness theorem; a global monodromy element of order 109; a landing in or kill of the `td=6` book; a TDU statement at `td=109`; Moskowicz prime-sheet exclusion; or any JC2 decision.

**Keep `CLOSED-SUPPORT + UNIT-L` as a conditional resurrection target.** This file does not enlarge or shrink that target. The quantitative lower bound `d>=109` is a necessary condition on any exact lift, not an obstruction to one.

---

## Quarantine

No result here proves or disproves JC2. Producer string `32/32 checks pass` was not used as evidence; the identities and field maps below were re-derived. Generic uncarried two-layer digit equations remain as in the carry erratum: they are not the packed exact identity that Hensel consumes. Moskowicz's unpublished prime-degree claim (arXiv:2407.13795, `ladder/SHEET6.md`, `APPROACHES.md` avenue 44) is not consumed. The independent `deg_y<=5` frontier is not consumed: the producer marked it pending, and this review does not re-audit that sibling. Secant ranks are a restatement of `d>=109`. Bounded-`y` no-gos already confirmed at `y`-degree `<=4` (and affine / cubic / quartic) are recovered only as the tautology `d=1` versus `d>=109`.

---

## Scope (not enlarged)

One prime `p=109`, one seed `(x-x^{109},y)`, exact coefficient ring `Z_109` for a hypothetical polynomial lift, function fields over `K=Q_109`, and one formal target tube `R=Z_109[[S,T]]`. Characteristic-zero language is purely conditional on an exact integral polynomial lift that this run did not produce. No construction, no support grammar, no exponent rectangle, no AWS, and no modular-to-characteristic-zero existence inference are in scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Under the exact-lift hypothesis, `P,Q` are algebraically independent over `K`; `L/M` is finite separable; `d` is the generic mapping degree of `A^2 --> A^2` | **CONFIRMED** | `det J_F=1` compatible with a nonzero relation `R(P,Q)=0` in char 0; `tr.deg_K L != 2`; a purely inseparable `L/M`; `d` identified with a Brouwer degree of large spheres that the gate then fed to the sheet ledger |
| 2 | Parameter Hensel over the 109-adically complete ring `R` produces, at each of the `109^2` residue points `(a,b)`, a unique integral branch; for fixed `b`, evaluation gives 109 distinct `M`-embeddings of the *field* `L` into `E`, not merely maps of a polynomial ring. Kernel-height and denominators survive | **CONFIRMED** | `R` failing 109-adic completeness or `(R,109R)` failing to be Henselian; `F(a,b)-(109S,b+109T)` not in `109 R^2`; `det J_F(a,b)` a nonunit; a nonzero `G in K[x,y]` with `G(x_a,y_a)=0`; a vanished denominator in `Frac(K[x,y])`; two distinct `a` with `x_a=x_{a'}` in `E`; the 109 embeddings collapsing after inverting `K[P,Q]\{0}` |
| 3 | Separability gives `d>=109` with no algebraic closure of `E`. Then `L tensor_M E ~= E^{109} x A_infinity` as finite étale `E`-algebras, `dim_E A_infinity=d-109`. Further `E` factors or a non-field product decomposition of `A_infinity` do not disturb the wording | **CONFIRMED** | a separable degree-`d` extension with more than `d` maps into an overfield; nilpotents in `L tensor_M E`; the 109 maps failing to split off as direct `E` factors; the report claiming `A_infinity` is a field, or that there are *exactly* 109 split factors, or that `A_infinity=0` |
| 4 | Degree over a finitely generated `k_0 subset Q_109` equals `d`; it does not drop or split under scalar extension to `Q_109` or `C`. An abstract embedding `k_0 -> C` yields a complex Keller map of the same generic degree with constant Jacobian one | **CONFIRMED** | a geometrically disconnected source after `k_0 -> Q_109`; finite-locally-free rank jumping under scalar extension; `det J` acquiring nonconstant terms after a coefficient embedding; a finitely generated char-0 field with no embedding in `C`; residue-mod-109 distinctness used as if a valuation-preserving embedding `Q_109 -> C` existed |
| 5 | Local Galois/decomposition action fixes the 109 `E`-rational sheets (`e=f=1`). Automorphisms of `E^{109}` are not `M`-automorphisms of `L`. Conditionals `deck C_109 => 109|d` and `A_infinity=0` plus descent `=>` cyclic Galois of degree 109 are correct and unearned. No inertia, divisibility, congruence, or global monodromy element is smuggled | **CONFIRMED** | Hensel producing a nontrivial permutation of the displayed sheets; the cyclic relabelling already lying in `Aut_M(L)`; Artin's theorem failing for a faithful `C_109 <= Aut_M(L)`; the report asserting `109|d` or a global element of order 109 as an unconditional theorem |
| 6 | For every integer `N>=109`, `G_N=(x-x^{109}+109 x^N,y)` has the same residue-ball Hensel data, integral unit Jacobian, nonconstant Jacobian, and generic degree exactly `N`. This disproves that local splitting alone forces a congruence or `109|d`. It says nothing under the Keller hypothesis `J=1` | **CONFIRMED** | `G_N mod 109 != (x-x^{109},y)` for some `N>=109`; `det J_{G_N}` a nonunit on an integral ball; `det J_{G_N}` the constant polynomial 1; `[K(x):K(g_N)] != N`; the report presenting some `G_N` as a Keller example |
| 7 | Interactions with `td=6`/TDU, secant ranks, Bézout/leading degree, and bounded-`y` no-gos are restatements or correct non-consumptions. Unreviewed prime-degree claims stay quarantined. The smallest global missing bridges are elimination of `A_infinity` or descent of the formal deck permutation | **CONFIRMED** | the gate landing AS109 in the sheet-six book; TDU applied at `td=109` without `d=109`; Moskowicz consumed; secant idempotent used as a new coefficient rank; a current AS109 support with a proved `d<=108`; `A_infinity=0` or deck descent treated as a lemma of residue-ball Hensel |
| 8 | The gate is conditional on a lift, constructs none, and at most proves a degree lower bound and a formal split. It is not a lift obstruction, degree congruence, properness theorem, or JC2 decision | **CONFIRMED** | a constructed lift in the artifacts; an inferred nonexistence statement; `d>=109` sold as incompatible with existence of a counterexample; a properness or congruence theorem derived from Hensel alone |

All remarks below are non-blocking unless marked otherwise. None changes a residue, a rank, or a numbered verdict.

---

## Replay and hashes

Frozen producer hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-hensel-global-degree-cross-gate-20260824.md` | `7a7185c27fe245233173a173f9f0851326f18d83585ffb743970b2189f703133` | prompt and `FREEZE.sha256` |
| `cases/as109_degree_cross_20260824/check.py` | `c0587c220cc9ca0e92bf8cd57fab466787ca6caa88fb61c8aceb7affb806f7b7` | prompt and `FREEZE.sha256` |
| `cases/as109_degree_cross_20260824/FREEZE.sha256` | `75b04b7c55748da5025d274582d007b593e9d0cd35a2af10694038fbb3a3adbf` | self-hash of the freeze listing |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | banked Hensel producer |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` | banked Hensel review |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` | carry erratum |
| `xmodel/as109-carry-erratum-review-grok-20260824.md` | `1b10eba84500d008548926e2c9dba9dd70a77331b4b670104f164d6119cf7212` | carry review |
| `xmodel/secant-idempotent-review-grok-20260824.md` | `6b0cb25dd3d1769f9f6c15116b6869b37c6cb1c89f17d9831ff19c67f20f09e9` | cited where used |
| `xmodel/secant-as109-cross-gate-20260824.md` | `f4bd8ff7708469dd4ca1a6a6880634fb60ea2975fa1c7aa9fb3ecf5d61ba80cf` | cited where used |
| `xmodel/secant-as109-review-grok-20260824.md` | `16d052ae483fe5c829fb6416202a77c1707e7acc85b65bee249e794b16c51029` | cited where used |

Registered command, rerun unmodified from the charged tree:

```sh
python3 cases/as109_degree_cross_20260824/check.py
```

Exit code 0. Final line `32/32 arithmetic checks passed`. Stdout SHA-256 `f66826c5ed6ce1fd9157357a3430b74ecc4d3a3d353c14475fdf9643251f9c9e`. Locale warnings from the host `shasum` wrapper are not part of that digest.

The registered program is a finite arithmetic control suite, not a checker of Hensel, of `Hom_M(L,E)`, or of scalar extension. It samples five degrees `N in {109,110,111,218,219}` and four residual ranks. Those Booleans were discarded as evidence for the field-theoretic claims; every numbered claim below is re-derived independently.

A second engine, written for this review and not imported from the registered script, used only integer dictionaries and `math.comb`. It recorded zero failures on: Fermat as functions on `F_109` and as the polynomial identity `x^{109}-x=prod_{a}(x-a)` on `F_109`; `J(x-x^{109},y)≡I_2 mod 109`; injectivity of `(U,V)|->(109S, b+109T)` on thirty random sparse polynomials over `Z` plus the zero polynomial; `G_N` for every `N=109..138` and for `N in {217,218,219,327,334,549,1000,268}` (degree `N`, derivative `1 mod 109` as a polynomial, residue collapse on all 109 source residues, extra derivative terms `109`-divisible and not identically zero); the closed-form derivative `1-109 x^{108}+109 N x^{N-1}` at five values including `N=109` (leading coefficient of `G_{109}` equal to `108`); all residue classes modulo 109 realized by `N=109..217`; `d(d-1)>=109*108` for `d=1..249` if and only if `d=1` is excluded and `d>=109`; the counts `109^2=11881`, `109*108=11772`; unit class of the `x^{109}` coefficient of any integral lift; and `det J_{G_N}` coprime to 109 at every residue representative `a=0..108`.

Process remark, non-blocking: `check.py` tests “generic degree is `N`” by taking the largest exponent in a sparse support. That is the polynomial degree of the first coordinate, which equals the function-field degree only by the elementary triangular argument of claim 6, not by the script.

---

## Independent recomputation

### 1. Algebraic independence, finiteness, separability, generic degree — CONFIRMED

Assume `F=(P,Q)` as in the exact-lift hypothesis. Then `det J_F=1` in `Z_109[x,y]`, hence in `K[x,y]`. Let `Ω_{L/K}` be Kähler differentials of the rational function field `L=K(x,y)`. The identity

```text
dP ∧ dQ = det(J_F) dx ∧ dy = dx ∧ dy ≠ 0
```

says that `dP,dQ` are linearly independent over `L`.

If `P,Q` satisfied a nonzero relation `R(U,V)=0` over `K`, take one of minimal total degree. Characteristic zero implies that some partial, say `R_U`, is not the zero polynomial, and has strictly smaller degree. Minimality forces `R_U(P,Q)≠0`. Differentiating the relation then yields a nontrivial linear dependence `R_U(P,Q) dP + R_V(P,Q) dQ = 0`, a contradiction. Thus `P,Q` are algebraically independent over `K`, `tr.deg_K M=2`, and `M ≅ K(U,V)` is purely transcendental.

Both `L` and `M` have transcendence degree two over `K`, so `L/M` is algebraic. It is finitely generated (`L=M(x,y)`), hence finite. Characteristic zero implies separable. Write `d=[L:M]`.

This `d` is the generic mapping degree of the dominant morphism `A^2_K -> A^2_K`: it is the separable degree of the function-field extension, equivalently the number of geometric points of a generic fibre after extending scalars to an algebraic closure of `M`. Campaign language (`td`, sheet number, Żołądek topological degree) uses this invariant, not the Brouwer degree of large real 4-spheres. For a nonproper étale map the latter need not stabilize; the gate never feeds a sphere-degree to the sheet ledger. Precision, not a gap: wherever this review writes “topological degree”, it means the algebraic mapping degree.

The original dual-confirmed DVR lemma already gives 109 distinct points in some *special* fibres, hence noninjectivity. Special-fibre cardinality does not by itself yield `d>=109` for a non-finite morphism (points can accumulate where an integral equation degenerates). The upgrade `d>=109` is the content of claims 2–3, not a restatement of noninjectivity.

### 2. Parameter Hensel, field embeddings, kernel-height, denominators — CONFIRMED

`Z_109` is a complete DVR. The ring `R=Z_109[[S,T]]` is local with maximal ideal `(109,S,T)`, equal to the Jacobson radical. The principal ideal `109R` is contained in that radical. A 109-adic Cauchy sequence in `R` is Cauchy coefficientwise in `Z_109`, uniformly across monomials because membership in `109^k R` constrains every coefficient; completeness of `Z_109` therefore makes `R` 109-adically complete. The pair `(R,109R)` is Henselian.

Fix `b in {0,...,108} subset Z_109` and independent parameters `S,T`. The target

```text
(U,V) = (109 S, b+109 T)
```

reduces to `(0,b)` modulo 109. For each residue `a in F_109`, Fermat gives `F_bar(a,b)=(0,b)`, and `J(F_bar)=I_2` as a matrix of polynomials over `F_109` (because `d(x^{109})=109 x^{108}=0`). Thus

```text
F(a,b) - (109 S, b+109 T)  in  109 R^2.
```

The Jacobian of the system in `(X,Y)` is `J_F`. At the constant point `(a,b)` one has `det J_F(a,b) ≡ 1 (mod 109)` in `Z_109`, hence a unit of `R`. (Under the Keller hypothesis the determinant is the constant polynomial 1, so invertibility is even global; the reduction-unit is what Hensel consumes, and is what the controls of claim 6 share.)

The standard multivariate Hensel lemma for a Henselian pair therefore produces a unique pair

```text
(x_a, y_a) in R^2,     x_a ≡ a,  y_a ≡ b  (mod 109),
```

with `F(x_a,y_a)=(109 S, b+109 T)` exactly. Uniqueness is inside the residue class `(a,b)+109 R^2`, not among all of `R^2`. Nonconstant solutions in `F_109[[S,T]]` could exist and lift; they would be additional branches, not collisions among these 109. The report does not claim otherwise.

Dependency precision, not a gap. The dual-confirmed lemma is the *pointwise* statement over the complete DVR `Z_109`. The gate uses the *parameter* version over `R`. That is the standard complete-ring inverse-function theorem, whose reduction hypotheses (`Fermat`, `J(F_bar)=I`) are exactly those of the banked lemma. Carry-erratum independence is used: Hensel consumes `det J_F=1` as a packed polynomial identity, not `E1`/`E2` residue digits.

The elements `109S` and `b+109T` are algebraically independent over `K`. The substitution `(U,V) |-> (109S, b+109T)` is translation in `V` (an automorphism of `K[S,T]`) composed with scaling by `109≠0`. Explicitly, `G(109S,109T)=sum g_{ij} 109^{i+j} S^i T^j` vanishes as a polynomial only if every `g_{ij}` vanishes. The second engine checked this on random sparse supports.

Evaluation at `(x_a,y_a)` therefore defines a `K`-algebra map `φ_a: K[x,y] -> E` sending `P |-> 109S` and `Q |-> b+109T`. The image is a domain (subring of a field) containing two algebraically independent elements, so has transcendence degree two. For an affine domain over a field, transcendence degree equals Krull dimension, hence `ker φ_a` is a prime of height zero in the two-dimensional domain `K[x,y]`, hence `ker φ_a=0`. Equivalently: a nonzero kernel would force `dim K[x,y]/ker <= 1`, contradicting transcendence degree two of the image.

Thus `φ_a` is injective on the polynomial ring and extends uniquely to a field embedding `σ_a: L=Frac(K[x,y]) -> E`. No denominator vanishes: a rational function `f/g` with `g≠0` has `g(x_a,y_a)≠0` because `g` is not in the kernel.

This is an *`M`-embedding*. Identify `M=K(P,Q)` with its image `K(109S, b+109T) subset E` via the structure map `P |-> 109S`, `Q |-> b+109T`, which is well-defined by algebraic independence. Every `σ_a` restricts to that same structure map, so the 109 embeddings are homomorphisms in one and the same set `Hom_M(L,E)`. They are distinct because `σ_a(x)=x_a` have pairwise distinct residues modulo 109, hence are distinct in the domain `R` and in `E`.

The 109 choices of `b` produce 109 disjoint *target* balls. Generic degree counts sheets over one target neighbourhood, so the lower bound is 109, not `109^2`. Completeness of the `109^2` source-ball table is a Hensel-hypothesis audit, not a degree-count.

### 3. Hom-bound without algebraic closure; étale splitting — CONFIRMED

A finite separable extension of degree `d` admits at most `d` homomorphisms into any overfield, algebraically closed or not. Proof without a primitive element: `L tensor_M E` is an `E`-vector space of rank `d`, and a commutative étale algebra over a field is a finite product of finite separable field extensions of that field (characteristic zero: finite reduced). Each `M`-homomorphism `L -> E` is an `E`-algebra projection onto a factor isomorphic to `E`, and distinct homs give distinct (hence orthogonal) idempotents, so there are at most `d` of them.

With a primitive element, which exists in characteristic zero: `L=M[α]≅M[T]/(Φ)` with `Φ` separable of degree `d`, and `Hom_M(L,E)` is the set of roots of `Φ` in `E`, at most `d`. The 109 embeddings differ on `x`, hence on `α`, hence give 109 distinct roots. Consequently `d>=109`. Algebraic closure of `E` is never used; `E=Frac(Z_109[[S,T]])` is not algebraically closed.

Write `Φ=(T-r_1)...(T-r_{109}) Ψ` with the `r_i` the 109 distinct roots and `Ψ` coprime to that product (`Φ` separable, so no repeated roots). Chinese remainder over the field `E` yields

```text
L tensor_M E  ≅  E^{109} × E[T]/(Ψ),
```

and `dim_E E[T]/(Ψ)=d-109`. This is (0.1), with `A_infinity := E[T]/(Ψ)` an étale `E`-algebra. Each displayed `E` factor is a clopen, degree-one, unramified formal branch in the étale topology of the generic fibre.

Wording audit, requested explicitly:

- `A_infinity` is not claimed to be a field. It is an étale algebra of known rank. Over a field of characteristic zero it is a product of fields. Non-field (nilpotent) factors cannot occur.
- The report states there may be further `E` factors *inside* `A_infinity`. That is correct: (0.1) splits off only the 109 *integral* Hensel sections. Additional `E`-rational solutions of `F(X,Y)=(109S,b+109T)` that do not reduce to constant residues would enlarge the split part of `A_infinity` and would only improve the lower bound. Nothing in the wording is disturbed by more than 109 split factors.
- The adjective “equivalently” between `d>=109` and (0.1) is accurate in the étale sense: 109 maps `L -> E` produce `E^{109}` as a direct factor of the rank-`d` étale algebra, which is exactly rank remainder `d-109`.

### 4. Descent to `k_0`; scalar extension; complex Jacobian one — CONFIRMED

Let `k_0` be the subfield of `Q_109` generated over `Q` by the finitely many coefficients of `F`. It is finitely generated of characteristic zero. The morphism `f: A^2_{k_0} -> A^2_{k_0}` is dominant (claim 1 over `k_0` the same way). The coordinates `x,y` are algebraic over `k_0(P,Q)`, so after inverting a single nonzero element of `k_0[P,Q]` they become integral; generic freeness on a regular base of dimension two then supplies a nonempty Zariski open `U` of the target, defined over `k_0`, over which `f` is finite locally free of some rank `d_0`. Locally-free rank survives arbitrary scalar extension. The source `A^2` is geometrically integral, so after `k_0 -> K` or `k_0 -> C` the source remains integral: the generic fibre of a dominant morphism from an integral scheme is the spectrum of a *field*, and that field's degree over the generic target is the locally-free rank. Hence there is no degree drop and no tensor-product splitting of the function field.

In particular `[K(x,y):K(P,Q)]=d_0=d`. (The naive fear that a minimal polynomial over `k_0(P,Q)` could factor after constants in `k_0` become powers in `Q_109` is incompatible with `k_0` being algebraically closed in `k_0(x,y)`, which it is, as a purely transcendental extension, and is independently killed by the locally-free rank.)

Any finitely generated characteristic-zero field embeds in `C`: it is a finite extension of a purely transcendental extension `Q(t_1,...,t_r)`, `C` has infinite transcendence degree over `Q`, and `C` is algebraically closed. Applying a field embedding `σ: k_0 -> C` coefficientwise produces a complex polynomial map `F^σ` whose Jacobian determinant is `σ(1)=1`, the constant polynomial one: `det J` is the polynomial `1` with coefficients in `Z`, and forming the Jacobian commutes with coefficient homomorphisms. The function-field degree is again `d` by the same scalar-extension argument. This is the complex mapping/`td` of (3.1).

A valuation-preserving embedding `Q_109 -> C` is not required and is not used. Distinctness of Hensel preimages after an abstract embedding is injectivity of field maps, not preservation of the 109-adic residue.

The alternative — adjoin the finitely many coordinates of 109 integral preimages of one numerical target, still finitely generated, and embed — produces 109 distinct unramified points of one complex fibre (`det J=1` everywhere, local degree one). Because the morphism is étale, a fibre cannot have more geometric points than `d`; this again yields `d>=109`, but the function-field argument of claims 2–3 identifies the generic degree more cleanly, as the report says.

### 5. Monodromy, Artin conditionals, no smuggled congruence — CONFIRMED

The 109 sections are `E`-rational (coordinates in `R subset E`). The absolute Galois group `Gal(E^{sep}/E)` therefore fixes each corresponding geometric sheet of `Hom_M(L, E^{sep})`. In étale language, each displayed factor of `E^{109}` has ramification index 1 and residue degree 1. The inequality `sum e_i f_i <= d` on these 109 branches is the Hom-bound of claim 3, not a one-dimensional Dedekind fundamental inequality smuggled across dimension two. Precision: *all* factors of the étale algebra `L tensor_M E`, including those inside `A_infinity`, are unramified over `E`. The residual factor records sheets not captured by the *integral constant-residue* balls, not ramified points at infinity.

The algebra `E^{109}` has automorphism group `S_{109}` over `E`, which contains the translations `a |-> a+c` of `F_109`. An automorphism of a split *base-changed* algebra is not an element of `Aut_M(L)`. Descent would additionally require that the 109 images `σ_a(L) subset E` coincide (or are conjugated inside a single copy of `L` over `M`) and that the permutation preserves `A_infinity` as an `M`-structure. Hensel gives neither. In particular it does not produce a global monodromy element of order 109, a rational `C_109` deck group, or the divisibility `109|d`. Transitivity of the Galois group of a Galois closure on `d` sheets is compatible with a decomposition group that fixes 109 displayed sheets: other paths, around infinity, may mix those sheets with the residual ones.

Conditional 1. If a cyclic factor permutation of order 109 descends *faithfully* to `Aut_M(L)`, Artin's theorem gives `[L : L^{C_109}]=109` with `M subset L^{C_109}`, hence `109|d`. Faithfulness is needed: the geometric permutation has order 109, so a descended automorphism would too.

Conditional 2. If independently `A_infinity=0`, then `d=109` and `L tensor_M E ≅ E^{109}`. That is complete splitting over `E`, not yet Galois over `M`: the `d` embeddings into `E` need not have the same image. If the cyclic action also descends, then `|Aut_M(L)|>=109=d`, so `L/M` is Galois of degree 109, and cyclic because 109 is prime. A classical Galois-Keller theorem (a Keller map whose function-field extension is Galois is an automorphism) would then contradict nonautomorphy (`d=109≠1`). That classical pointer is not proved in the gate and is not load-bearing: both missing hypotheses remain missing. Residue-ball Hensel supplies neither.

No inertia element is constructed. No congruence for `d` is claimed. Claim 6 is the mechanism that would have to fail for a silent congruence to be legitimate.

### 6. Controls `G_N` — CONFIRMED

For every integer `N>=109` put `G_N=(g_N, y)` with `g_N=x-x^{109}+109 x^N`. Then `G_N mod 109=(x-x^{109},y)` as polynomials. The Jacobian determinant is the polynomial

```text
det J_{G_N} = 1 - 109 x^{108} + 109 N x^{N-1}.
```

Every nonconstant term is divisible by 109, so `det J_{G_N} ≡ 1 (mod 109)` in `Z[x]`, hence on every integral residue ball. Evaluated at `x in Z_109` one has `|det J-1|_{109}<=1/109`, so `det J` is a 109-adic unit. It is not the constant polynomial 1: for `N>109` the terms `x^{108}` and `x^{N-1}` have distinct degrees; for `N=109` one has `g_{109}=x+108 x^{109}` and `det J=1+108·109 x^{108}≠1`. These maps are deliberately non-Keller.

Reduction and unit Jacobian on balls are the same Hensel input as in claim 2, so each target ball `(0,b)+109 Z_109^2` has 109 integral inverse branches.

Generic degree. `Q=y`, so `[K(x,y):K(g_N,y)]=[K(x):K(g_N)]`. For a polynomial `g in K[x]` of degree `N>=1`, `K[x]` is free of rank `N` as a `K[g]`-module on `{1,x,...,x^{N-1}}`. Characteristic zero, `109≠0`, and `108≠0` keep the leading coefficient nonzero: for `N>109` it is `109`; for `N=109` it is `108`. Thus the generic degree is exactly `N`. The second engine checked the sparse degree, the derivative identity, residue collapse, and nonconstancy for every `N=109..138` and a spread of larger `N` including `1000`. Every residue class modulo 109 is realized by some `N>=109` (already by `N=109..217`).

What this disproves: that the local residue-ball splitting data (same reduction, 109 integral branches, Jacobian a unit on those balls) impose a divisibility `109|d` or any congruence on the global degree.

What this does not say under the Keller hypothesis: it does not produce a map with `det J` the constant polynomial 1 and degree not divisible by 109, and it does not forbid a future global argument that *constant* Jacobian one forces extra constraints on `d`. Any such argument needs genuinely new constant-Jacobian or infinity input, as the report states.

### 7. Campaign interactions and missing bridges — CONFIRMED

Sheet-number ledger. The active `td=6` book (`ladder/SHEET6.md` canonical checksum; `APPROACHES.md` / `PROGRESS.md`) has eight terminal classes, four single-pole and four two-pole. Claim 4 places a hypothetical AS109 lift at `td>=109`, so it cannot land in that book. This is a lane separation, not a closure of either lane.

TDU. Promoted Theorem TDU (`ladder/SHEET6-TDUNIFORM.md`, review `SHEET6-TDU-REVIEW.md`) excludes *single-pole* configurations at every prime `td`, on an AF3/H1-tier perimeter, and leaves multi-pole configurations. Applying it at 109 requires a separate theorem `d=109` (i.e. `A_infinity=0`), which the gate does not have, and would still leave multi-pole. The gate does not apply TDU. Correct non-consumption.

Unreviewed prime-degree claims. Moskowicz arXiv:2407.13795 is flagged unvetted in `ladder/SHEET6.md` and as avenue 44 in `APPROACHES.md`. It is not consumed.

Secant. On one formal tube the 109 sections give `109^2=11881` ordered source pairs and `109*108=11772` ordered off-diagonal pairs; over one source branch, 108 off branches. The inequalities `d(d-1)>=109*108` and `d-1>=108` are exactly `d>=109`. The secant idempotent records the clopen split of the localized collision algebra and, as already reviewed (`COSTUME` / rank zero on off sectors), adds no coefficient rank. Restatement, not a new constraint.

Bézout / leading degree. A dominant generically finite plane map satisfies `d <= deg(P) deg(Q)`. Any integral lift of the seed has `deg(P)>=109`, because the coefficient of `x^{109}` is `-1+109 a_{109,0}`, a 109-adic unit. Bézout therefore only says `d` is at most something already at least 109, which does not constrain `d>=109`. No current named AS109 support carries an independently proved generic-degree *upper* bound below 109; a family that did would be excluded immediately by (2.2). Leading-form divisibility does not see the residual rank `d-109`. Correct and inert.

Bounded-`y`. Any characteristic-zero theorem that every Keller pair in a bounded `y`-degree range is an automorphism forces `d=1`, contradicting `d>=109`. That is the already-known noninjectivity contradiction rewritten in degree language. It recovers the confirmed affine / quadratic / cubic / quartic AS109 exclusions as restatements. The producer marks the independent `deg_y<=5` frontier as pending and does not consume it; this review follows that quarantine and does not re-audit the sibling quintic file.

Smallest missing global bridge. Eliminating `A_infinity` is a global boundedness / properness / finite-flat-across-109 statement: every generic sheet over the tube is integral, or a support-specific upper bound `d<=109` exists. That is the known nonproperness wall for a Keller counterexample, not a cheap residue-ball lemma. Separately, turning `a |-> a+c` into an element of `Aut_M(L)` is an algebraization/descent theorem for local inverse branches, and is the smallest bridge to `109|d`. Neither follows from Hensel, the secant idempotent, fixed finite support alone, or the present sheet ledger.

### 8. Scope firewall — CONFIRMED

The report assumes an exact finite polynomial lift and does not construct one. It proves a conditional lower bound `d>=109` and a formal split over one tube. Noninjectivity of such a lift was already in the dual-confirmed Hensel lemma; the new quantitative content is generic degree and the displayed étale splitting, still compatible with existence of a counterexample. Nothing here is a lift obstruction, a degree congruence, a properness theorem, a global monodromy theorem, or a JC2 decision. No web-priority claim is used, no AWS computation is invoked, and no canonical file is edited.

---

## Dependency and scalar-extension caveats

- Logical dependency for claims 1–6 and 8 is the exact-lift hypothesis plus standard commutative algebra (Henselian pairs, finite separable extensions, generic freeness) together with the reduction hypotheses of the dual-confirmed AS109 Hensel lemma (`F_bar=(x-x^{109},y)`, `J(F_bar)=I`, Fermat). Parameter Hensel over `R` is the standard complete-ring theorem, not a new arithmetic identity and not a silent upgrade of the DVR lemma's *conclusion* (that conclusion is pointwise noninjectivity; field embeddings into `E` need parameters).
- Digit carries are irrelevant. The carry erratum quarantines uncarried `E1`/`E2`; this gate never uses them.
- Scalar extension `k_0 -> Q_109 -> C` preserves degree because a finite-locally-free open exists over `k_0` and `A^2` is geometrically integral. It preserves `det J=1` because that identity is the constant polynomial 1. Complex `td` is the algebraic mapping degree.
- Secant, TDU, the `td=6` book, Bézout, and bounded-`y` theorems are interaction remarks. None is an input to `d>=109`.

---

## Exact scope exclusions

Do not read this file, or the producer, as any of the following:

- a construction of an exact lift, series lift, or complex point;
- a proof that no exact lift exists;
- `109|d`, `d=109`, `d ≡ r (mod m)`, or any other congruence;
- `A_infinity=0`, properness, or finiteness of `A^2 -> A^2`;
- a rational `C_109` deck transformation, a global monodromy element of order 109, or a Galois-Keller contradiction;
- a landing in or exclusion of the sheet-six book, a TDU statement at `td=109`, or Moskowicz prime-sheet exclusion;
- a coefficient rank from the secant idempotent;
- a larger `y`-degree cutoff than those already confirmed as automorphy theorems;
- a JC2 proof or counterexample.

---

## Smallest missing hypothesis or overclaim

None of the eight claims is an existence theorem, a nonexistence theorem, a congruence theorem, or a JC2 decision.

The smallest precision a reader could miss, and that this review therefore isolates, is that `d>=109` is *not* a corollary of “109 points in a special fibre” alone. The load-bearing chain is: complete-ring parameter Hensel produces integral branches in `R`; kernel-height promotes evaluation to `M`-embeddings of the field `L` into `E`; the Hom-bound for a separable extension, with no algebraic closure, gives `d>=109` and the étale splitting (0.1). The DVR lemma remains the noninjectivity engine; this gate is its generic-degree companion.

The smallest genuinely global missing objects remain exactly those named in producer §7: a theorem that kills `A_infinity`, or a descent theorem for the formal factor permutation. Either would be a new paper. Residue-ball Hensel does not supply them.

---

## Promotion advice

Accept internally as an exact, hostile-confirmed packaging of the conditional implication

```text
exact AS109 lift  =>  d >= 109 and L tensor_M E ≅ E^{109} × A_infinity.
```

Record it as quantitatively stronger than two-point collision, and as a lane separator from the active `td=6` book. Do **not** promote it into `APPROACHES.md` as a kill of avenue 19, as a degree congruence, as a properness theorem, as a TDU-at-109 statement, or as any JC2 implication. Successor work that wants `A_infinity=0` or `109|d` must bring a global boundedness or algebraization hypothesis that this gate correctly refuses to invent.
