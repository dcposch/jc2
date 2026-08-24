# Hostile different-model review — `SECANT-IDEMPOTENT` × AS109

| Field | Value |
|---|---|
| Claim under review | Frozen cross-connection gate: the characteristic-109 secant idempotent recovers the Hensel sheet split and adds rank zero to a collision-aware coefficient compiler; trichotomy `COSTUME / NEED-GLOBAL-BOUNDED-ALGEBRAIC-OFF-DATUM` |
| Overall verdict | **CONFIRMED** |
| Requested trichotomy | **`COSTUME`** (not `CONTRADICTION`, not `NEW-FINITE-CONSTRAINT`) |
| Smallest failing identity | none (algebra holds) |
| Smallest overclaim | JSON `constraint_rank_added_on_off_sectors = 0` is a hardcoded label, and the all-Witt marked-projector Boolean is the tautology `0 * (1+109+…)=0`. Neither disturbs the identities. The verdict sentence that the secant row cannot constrain a cubic-or-higher compiler is true only under the compiler hypothesis of §4 below; the body already has it |
| Evidence tier | independent polynomial identities over `F_109` and `Q`; Newton Teichmüller lifts (not the producer brute-force search); scheme-theoretic differential of the adjugate identity, including product terms; coefficient Jacobian rank on a `p=5` packed analog; Singular `sat`/`quotient` of the seed collision ideal; actual Jacobians and marked secants of `G_7`, the tame automorphism, and `F_n` for `n=1..6` |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, provisional cross-connection child) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T09:57:00Z – 2026-08-24T10:20:00Z |
| Python | host 3.14.6; attack interpreter 3.11.11 with `sympy==1.14.0` |
| Singular | 4.4.1 (`elim.lib` `sat` / `quotient`) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer inputs reread in full before any verdict:

- `xmodel/secant-as109-cross-gate-20260824.md` (SHA-256 `f4bd8ff7708469dd4ca1a6a6880634fb60ea2975fa1c7aa9fb3ecf5d61ba80cf`, matches the launch prompt)
- `cases/secant_as109_20260824/secant_as109.py` (SHA-256 `8024f629060624d86c88029452c8c4df85c0728a1e5388ae789965311c0ef98c`)
- `xmodel/fresh-connection-gate-20260824.md` (SHA-256 `666bde51ea8bb78bd2c031122183148708b2b7de08547dc407191e633a712c4b`)
- `xmodel/secant-idempotent-review-grok-20260824.md` (SHA-256 `6b0cb25dd3d1769f9f6c15116b6869b37c6cb1c89f17d9831ff19c67f20f09e9`)

Banked Hensel / carry inputs reread against the same charged basis:

- `xmodel/as109-support-gate-20260824.md` (SHA-256 `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`)
- `xmodel/as109-support-gate-20260824-erratum.md` (SHA-256 `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb`)

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer and parent-review artifacts are frozen uncommitted on top of that basis. No producer, canonical, ledger, or case file was edited. No support grammar, exponent rectangle, AWS search, new Witt level, or counterexample claim was opened. Producer JSON strings (`verdict`, `constraint_rank_added_on_off_sectors`, section name labels) are not evidence.

The secant parent is independently **CONFIRMED** (this reviewer, same day) as a software/theory accelerator, not as a JC2 decision. This child neither needed nor supplies a parent promotion: the decisive off-sector identity is the universal adjugate relation `adj(A)A=(det A)I_2`, which holds in any commutative ring.

**Promotion.** Accept `COSTUME / NEED-GLOBAL-BOUNDED-ALGEBRAIC-OFF-DATUM` at this exact scope. Do **not** feed the raw secant row to a collision-aware AS109 compiler. Do **not** promote a contradiction, a finite coefficient equation, a bounded polynomial factorization of the 108 off sectors, a lift, or JC2.

**Quarantine.** An exact determinant-one lift is assumed only hypothetically, via the banked Hensel nonautomorphy lemma. Existence is not inferred. Local analytic idempotents are not global polynomial factors. Trace `109 ≡ 0 (mod 109)` is a rank, not a vanishing. No statement here proves or disproves JC2.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | After `t=x-u`, the seed collision ideal is `(t(1-t^{108}), y-v)`; `e_0=1-t^{108}` is the Fermat diagonal indicator; the off algebra splits as `∏_{r∈F_{109}^×} F_{109}[u,y]`; ordered-pair / rank counts are `108`, `109`, `109^2=11881`, `109·108=11772`; the displayed CRT projectors are the Lagrange idempotents and sum to one (`11664/11664`) | **CONFIRMED** | `(x-u)^{108} ≠ ∑_{i=0}^{108} x^{108-i}u^i` in `F_{109}[x,u]`; a multiple root of `t^{108}-1`; a projector evaluation `≠ δ_{r,s}`; product failing to split because `gcd(t,1-t^{108})≠1` |
| 2 | For a hypothetical exact lift, multivariate Hensel supplies analytic collision graphs and analytic idempotents on the 109 residue balls, not bounded polynomial factors of `det A`. Trace/norm record already-split ranks (`1` / `108` on a second-source ball; diagonal trace `109` on the target fibre) and yield no coefficient identity | **CONFIRMED** | `J(F̄)≠I` at a residue point; a polynomial factorization of the deformed off algebra already in the artifacts; a trace/norm identity in the correction coefficients not in the localized collision ideal; the report claiming finite polynomial sector representatives |
| 3 | On every off sector, `x-u` is a `109`-adic unit, so `(f_1,f_2,e)_{x-u}=(f_1,f_2)_{x-u}` as ideals. Differentiating the adjugate identity at `e=f_1=f_2=0` gives `de=(x-u)^{-1}(a_{22} df_1-a_{12} df_2)` after product terms vanish; the `de` row has tangent/coefficient rank zero, including nilpotents | **CONFIRMED** | `e(x-u)-a_{22}f_1+a_{12}f_2 ≠ 0` as a polynomial; a leftover 1-form at a collision not in `span{df_1,df_2}`; `e` not in the localized ideal after inverting `x-u`; a positive-rank coefficient Jacobian for `e` at an off pair after quotienting by `f_1,f_2` |
| 4 | Packed expansion `e=c+109(α+cδ)+109^2(αδ-βγ)` is exact. Every digit of `e=0` on an off collision, including base-109 carries, is a digit of the adjugate identity and is not an independent successor, **provided** the compiler already includes the collision equations at matching precision (or is restricted to the exact-lift locus) | **CONFIRMED** (with the compiler hypothesis stated in §4) | a `p^2` term missing from the `2×2` expansion; a carry digit of `e=0` independent of the carried collision digits at the same precision; the claim that `e=0` cuts truncated non-exact maps that omit collisions entirely, presented as a cut of the exact-lift locus |
| 5 | Triangular `G_7=(x+109 y^7,y)` has secant determinant `1`; the two-step tame automorphism has the nine-term nonconstant determinant and off Gröbner basis `[1]`; `F_n` has `det J=1-109^n x^{108 n}`, marked projector `0`, and `Q`-support `n` for `n=1..6`. Degree, support, factor count, trace, and norm give no overlooked global bounded coefficient equation | **CONFIRMED** | tame off basis not `[1]`; actual `F_n` Jacobian not the telescope; actual marked `det A` nonzero; a finite polynomial factorization, Vieta identity, or discriminant equation on the correction coefficients outside the localized collision ideal |
| 6 | At exact scope the trichotomy is `COSTUME`. Raw local secant-row redundancy is not a global bounded off-datum. No lift, characteristic-zero point, or JC2 decision is produced | **CONFIRMED** | a coefficient row of positive generic rank after quotienting by determinant and collision; a proved bounded polynomial realization of the 108 lifted sectors; the report inferring existence, emptiness, or a complex Keller map |

All remarks below are non-blocking unless marked otherwise. None changes an identity, a rank, or the trichotomy.

---

## Replay and hashes

Frozen artifact SHA-256 values match the launch prompt:

| Artifact | SHA-256 |
|---|---|
| `xmodel/secant-as109-cross-gate-20260824.md` | `f4bd8ff7708469dd4ca1a6a6880634fb60ea2975fa1c7aa9fb3ecf5d61ba80cf` |
| `cases/secant_as109_20260824/secant_as109.py` | `8024f629060624d86c88029452c8c4df85c0728a1e5388ae789965311c0ef98c` |
| `xmodel/fresh-connection-gate-20260824.md` | `666bde51ea8bb78bd2c031122183148708b2b7de08547dc407191e633a712c4b` |
| `xmodel/secant-idempotent-review-grok-20260824.md` | `6b0cb25dd3d1769f9f6c15116b6869b37c6cb1c89f17d9831ff19c67f20f09e9` |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` |

Independent rerun of the frozen engine, locale `C`:

```text
uv run --no-project --with sympy==1.14.0 \
  python3 cases/secant_as109_20260824/secant_as109.py
```

Stdout SHA-256 `3f9edfc6327d2859c32c8bfcd2e9aaff1d9fe39308a55989aa9c63a9655263e6`, identical to the producer report. Exit 0. The script reports `29/29` Boolean checks and `11664/11664` CRT evaluations. Those Booleans were then discarded as evidence; every numbered claim below is re-derived or re-reduced independently.

Independent payloads, computed from the Lagrange/Newton formulae with no producer imports, match the script’s own hashes:

| Payload | SHA-256 |
|---|---|
| CRT projector coefficient table | `d5e5d670b63c543627447e0f06251f22f5c5079ccfaf7a22e2adc29c76b1ab74` |
| Teichmüller roots modulo `109^3` | `e5873b38de0c57e446c34f1f62c4628bc509ca8f787a9e7883398b8a06d7e67f` |

The field `constraint_rank_added_on_off_sectors` is the integer literal `0` in `main()`, not a matrix rank. It is ignored. Rank zero is re-proved in §3.

---

## 1. Seed algebra, counts, CRT projectors

Let `P_0=x-x^{109}`, `Q_0=y` over `F_{109}`. The `x`-then-`y` secant is diagonal, with

```text
a_11 = 1 - ∑_{i=0}^{108} x^{108-i} u^i,
a_12 = 0,     a_21 = 0,     a_22 = 1.
```

Two polynomial identities in `F_{109}[x,u]`, checked as `Poly(..., modulus=109)` and not merely on `F_{109}^2`:

```text
x^{109}-u^{109} = (x-u)^{109},
∑_{i=0}^{108} x^{108-i} u^i = (x-u)^{108}.
```

The second is the first divided by `x-u`, equivalently Lucas: `C(108,k)≡(-1)^k (mod 109)`, so the binomial expansion of `(x-u)^{108}` has all coefficients `1`. Hence `e_0=det A_0=1-(x-u)^{108}` and

```text
P_0(x)-P_0(u)=(x-u)(1-(x-u)^{108}),     Q_0(y)-Q_0(v)=y-v.
```

After `t=x-u` and killing `y-v`,

```text
C_0 = F_{109}[u,y,t] / (t(1-t^{108})).
```

`gcd(t,1-t^{108})=1` because `1-t^{108}` evaluates to `1` at `t=0`. Chinese remainder gives the product in the report. Further, `t^{108}-1=∏_{r∈F_{109}^×}(t-r)` as polynomials (verified by expanding the product in characteristic 109). Every root is simple: `108 r^{107}≠0` for `r≠0`. So the off factor is etale of rank `108` over `F_{109}[u,y]`, a product of `108` copies of `F_{109}[u,y]`. Including the diagonal `t=0` gives `109` sheets relative to a fixed second source.

Pointwise: `e_0(0)=1` and `e_0(r)=0` for all `r∈F_{109}^×`. It is the Fermat indicator of the diagonal, not a sum of the `108` off projectors.

**Counts, not JSON.** `109^2=11881` ordered residue pairs over a fixed target residue `(0,b)`, because every source residue `(a,b)` maps to `(0,b)`. Off-diagonal ordered pairs: `109·108=11772`. Relative to one second-source residue: `108` off graphs plus the diagonal. Independently: `108·108=11664` CRT evaluations; `108^{-1}≡108 (mod 109)` because `108^2=11664=107·109+1`.

**CRT projectors.** In `F_{109}[t]/(t^{108}-1)`,

```text
ε_r(t) = 108^{-1} ∑_{k=0}^{107} (t/r)^k
       = ∑_{k=0}^{107} 108^{-1} r^{-k} t^k.
```

This is the standard cyclotomic Lagrange interpolant: at `t=r` the sum is `108`, times `108^{-1}` gives `1`; at `t=s≠r` in `F_{109}^×` the ratio `s/r` is a nontrivial `108`-th root of unity and the geometric sum vanishes. Independent evaluation on all `108×108` pairs: `11664` matches, `0` failures. Sampled agreement with the product formula `∏_{s≠r}(t-s)/(r-s)`. Sum of the `108` projectors is `1` (coefficient vector `(1,0,…,0)`). These are seed algebra projectors in `t` alone. They are not claimed, and are not, factors of a deformed `det A`.

**Teichmüller.** `f(t)=t^{108}-1` has `f'(r)=108 r^{107}` a unit at every nonzero residue, so each root lifts uniquely through every `109^n`. Independent Newton lifts through `109^3` are valid, pairwise distinct, and reduce to `1,…,108`. Brute-force uniqueness at the first step was spot-checked for `r=1,2,108` (one lift each). The Newton payload hash matches the producer brute-force payload, so the two procedures computed the same unique roots. This is a seed control on `t^{108}-1`, not a factorization of a lifted secant determinant.

---

## 2. What Hensel actually supplies

Assume hypothetically `F=(P,Q)∈Z_{109}[x,y]^2` with `F ≡ (x-x^{109},y) (mod 109)` and `det J_F=1`. The reduction has Jacobian the identity at every residue point (`P_x=1-109 x^{108}≡1`, `Q_y=1`). Multivariate Hensel therefore realises each source ball

```text
B_{(a,b)} = (a,b) + 109 Z_{109}^2
```

as an analytic isomorphism onto the target ball `T_b=(0,b)+109 Z_{109}^2`. This is the banked nonautomorphy lemma, used only hypothetically; the carry erratum correctly isolates it from digit bookkeeping. Existence of such an `F` is not an output of this gate.

**Second-source decomposition.** Fix a second-source ball `B_{(a',b)}`. For each of the `109` first-source balls `B_{(a,b)}` there is a unique analytic graph of pairs with the same image. One of them is the diagonal graph `a=a'`; the other `108` are off. The completed self-fibre product over that second-source ball is the product of these `109` graphs. The polynomial `e=det A` equals `1` on the diagonal (because `A` restricts to `J_F` and `det J_F=1`) and equals `0` on every off graph (claim 3: `x-u` is a unit there, and `e(x-u)` lies in `(f_1,f_2)`). As an element of the product ring it is the tuple `(1,0,…,0)`.

**Target-fibre decomposition.** Over `T_b` there is one analytic graph for each ordered pair of source balls, `109^2=11881` of them. The diagonal projector is the sum of the `109` components with equal source residues.

**Trace and norm.** On the second-source product of rank `109` over the analytic functions on the second-source ball:

```text
tr(e)=1,     tr(1-e)=108,     N(e)=0,     N(1-e)=0.
```

On the target-fibre product of rank `109^2`, the diagonal projector has trace `109` and norm `0`. These are ranks of already-split factors. They are not polynomial identities in the correction coefficients of `A,B`.

The congruence `109≡0 (mod 109)` does not kill the diagonal. Over `Z_{109}` the trace is the integer `109`, which remains nonzero in `Z_{109}` as a rank; its reduction in `F_{109}` being `0` only says that the rank is divisible by the residue characteristic. There is no contradiction, and no coefficient equation.

**Polynomial versus analytic.** Idempotents lift uniquely through nilpotent kernels `Z/109^n → Z/109^{n-1}` and in the `109`-adic completion (standard for etale algebras / lifting idempotents through nil ideals). Persistence of the *decomposition* is not persistence of *bounded polynomial representatives*. The sector projectors of a hypothetical lift are analytic functions of the second source — equivalently, power series on each ball — and may have unbounded degree, unbounded support, and unbounded coefficient height. Hensel does not produce a finite factorization of `det A` in `Z_{109}[x,y,u,v]`.

The seed algebra `F_{109}[t]/(t^{109}-t)` is finite etale of rank `109`, so its traces are the point-counts of §1 (`e_0` has values `(1,0,…,0)` on `F_{109}`, trace `1`). A characteristic-zero or `Z_{109}` polynomial lift need not be a finite morphism at all: etale polynomial maps `A^2→A^2` that are not automorphisms fail to be proper, hence fail to be finite. The global collision algebra `k[x,y,u,v]/(f_1,f_2)` is then not finite over `k[u,v]`, and “trace of `e`” as a polynomial is not defined. That is exactly the parent’s held finite-sheet card: one would need a finite normalization `R` before traces become coefficient matrices. Hensel does not supply `R`.

---

## 3. Localized redundancy and the `de` row

In any commutative ring, `adj(A)A=(det A)I_2`. Substituting `A δ=(f_1,f_2)^T` gives the polynomial identities

```text
e(x-u)=a_{22} f_1 - a_{12} f_2,
e(y-v)=-a_{21} f_1 + a_{11} f_2.
```

Independent expansion in free symbols `a_{ij}, t, w` is the zero polynomial (no Keller hypothesis). The same identities hold for the telescoping secant of every control below, and for a packed low-degree deformation over `Z`.

**Ideal membership after inverting `x-u`.** In `S[(x-u)^{-1}]`,

```text
e = (x-u)^{-1}(a_{22} f_1 - a_{12} f_2) ∈ (f_1,f_2).
```

Hence `(f_1,f_2,e)=(f_1,f_2)` as ideals of the localized ring. This is localization at the element `x-u`, not at a prime. On an AS109 off sector of a hypothetical lift one has `x-u ≡ r ≠ 0 (mod 109)`, so `x-u` is a `109`-adic unit and the same equality holds in the completed local ring. The companion identity in `y-v` is not required: seed collisions have `y=v` identically, and deformed collisions still lie in matching `b`-balls, so `y-v` need not be a unit.

This is scheme-theoretic, not merely set-theoretic. Equality of ideals after inverting `x-u` identifies the closed subschemes `V(f_1,f_2)` and `V(f_1,f_2,e)` on `D(x-u)`, nilpotents included. Independently, over `F_{109}`:

```text
h_1 = (x-u) e_0,     h_2 = y-v,
```

so `e_0` is not in `(h_1,h_2)` (it is `1` at `t=0`), but `(x-u)e_0` is. Singular `sat((h_1,h_2),(x-u,y-v))` and the first colon `quotient((h_1,h_2),(x-u,y-v))` both return `(y-v, ∑_{i=0}^{108} x^{108-i}u^i - 1)`, which is `(y-v,e_0)` in characteristic 109. That is the parent saturation identity on this seed, and it confirms that adjoining `e` cuts away the diagonal rather than cutting the off scheme.

**Product terms in the differential.** Write `Φ=e·t-a_{22}f_1+a_{12}f_2`, the zero function on the ambient space of `(a_{ij},t,w)` (and of coefficients, via the same identity). Then `dΦ=0` identically:

```text
de·t + e dt - da_{22} f_1 - a_{22} df_1 + da_{12} f_2 + a_{12} df_2 = 0.
```

Rearranged,

```text
de·t - (a_{22} df_1 - a_{12} df_2)
  = -e dt + da_{22} f_1 - da_{12} f_2.
```

The right-hand side is the product-error combination; it lies in the ideal `(e,f_1,f_2)` in the ring of 1-forms. At a collision `e=f_1=f_2=0` it vanishes, leaving

```text
de = (x-u)^{-1}(a_{22} df_1 - a_{12} df_2)
```

whenever `x-u` is a unit. This is an identity of cotangent vectors on whatever ambient space the differentials are taken in (points, coefficients, or both). In particular the `de` row is in the span of the `df_1,df_2` rows: algebraic rank zero.

A concrete coefficient Jacobian, not using producer code. Packed `p=5` analog `P=x-x^5+5A`, `Q=y+5B` with eight affine coefficients, evaluated at the fixed off pair `(x,u,y,v)=(1,0,0,0)` (`x-u=1`). At the seed coefficient origin the `3×8` Jacobian of `(f_1,f_2,e)` has rank `2`, equal to the rank of `(f_1,f_2)`. At the still-colliding point `A=y` the `de` row is exactly `df_1-5\,df_2`. In the coefficient ring, `e` at that pair lies in the ideal `(f_1,f_2)=(A_1,B_1)`.

**Nilpotents.** Because membership is exact in the localized ideal, `e` does not cut embedded structure on `D(x-u)`. Seed off roots are simple, so the seed off scheme is reduced; Hensel preserves etaleness for a determinant-one lift. Even if a non-reduced off point were present, the localized ideal equality would still make the `e` equation redundant.

**Global versus local.** Globally, adjoining `e` is exactly off-diagonal saturation (parent theorem). That is how one *removes the diagonal*, not how one constrains off-sector coefficients. On the off locus the extra generator is already in the ideal. A compiler that presents `(f_1,f_2,e)` at an off pair therefore enlarges the presentation and does not enlarge the rank.

---

## 4. Packed expansion, carries, compiler hypothesis

Linearity of divided differences gives, for `P=x-x^{109}+109A` and `Q=y+109B`,

```text
a_11 = c + 109 α,     a_12 = 109 β,
a_21 = 109 γ,         a_22 = 1 + 109 δ,
```

with `c` the integral seed secant `1-∑ x^{108-i}u^i` and `α,β,γ,δ` the secant entries of `(A,B)`. The `2×2` determinant expands over `Z` to

```text
e = c + 109(α + c δ) + 109^2(α δ - β γ).
```

Independent check on a packed map with seed `(x,y)` (so `c=1`) and affine `(A,B)`: the actual telescoping determinant equals that expansion as polynomials over `Z`. The same expansion is the free-symbol identity in the producer script; that check is valid as algebra (it does not compute a rank).

**Carries.** The adjugate identity holds over `Z`, before any base-109 reduction. Consequently every base-109 digit of `e(x-u)`, including carries, equals the corresponding digit of `a_{22}f_1-a_{12}f_2`. If `f_1=f_2=0` integrally on an off pair, then `e=0` integrally. If `f_1=f_2=0` only modulo `109^n` and `x-u` is a unit modulo `109^n`, then `e=0` modulo `109^n`. There is no carry digit of `e=0` that is independent of the collision digits at the same precision.

This is the same bookkeeping lesson as the AS109 carry erratum, with the opposite sign: the erratum exhibits a *missing* carry in an uncarried `E2`; here the identity is already packed, so extracting digits of `e=0` cannot outrun the collision carries. Uncarried `e`-digits would be as misleading as uncarried `E2`, and are not what the identity produces.

**Compiler hypothesis (precise).** Let `U` be a coefficient module for packed corrections `(A,B)`, at whatever finite support. Consider a compiler that imposes, at a common `109`-adic precision, including evaluation and determinant carries:

1. the packed Jacobian equation `det J(x-x^{109}+109A,\, y+109B)=1`;
2. the packed collision equations `f_1=f_2=0` at one or more pairs with `x-u` a `109`-adic unit (marked, sampled, or existential off points).

Then every digit of `e=0` at those pairs lies in the ideal generated by (2) after inverting `x-u`. It is not an independent successor row for a coupled cubic-or-higher compiler. If the pair is a constant off residue pair, `x-u` is a unit *constant* and membership holds in the coefficient polynomial ring itself.

If the compiler omits (2) and keeps only (1), then on the *exact-lift locus* Hensel still supplies the collisions, so imposing `e=0` at those collisions does not cut that locus. It can cut a truncated space of maps that satisfy `det J≡1 (mod 109^n)` and do not collide; that truncated space is outside the gate’s exact-lift question, and the apparent cut is a collision digit in disguise rather than a new family of equations.

The producer body (§3, “same point holds if the compiler omits marked collisions”) is this second case, restricted to exact lifts. The headline sentence that the secant row “adds no independent coefficient constraint to a cubic or higher coupled AS109 compiler” is true under the hypothesis above and is not a claim about arbitrary truncated presentations that drop collisions and then compare digits at mismatched precision. That is the precisification, not a refutation.

Feeding `e` to the compiler therefore fails the producer’s own success test: after quotienting by determinant and collision, the new row has generic rank zero.

---

## 5. Controls; no overlooked global bounded equation

**Triangular gauge.** `G_7=(x+109 y^7,y)` has Jacobian `1`. Its secant is `a_{11}=1`, `a_{21}=0`, `a_{22}=1`, and `a_{12}=109(y^7-v^7)/(y-v)≠0`. Determinant identically `1`, off ideal `(1)`. Source-gauge representatives are automorphisms; they are not AS collision sectors. Independently recomputed, not read from JSON.

**Tame two-step.** `F=(x+(y+x^2)^2,\, y+x^2)` has Jacobian `1` and nine-term secant determinant

```text
-u^3 - u^2 x - u v + u x^2 + u y - v x + x^3 + x y + 1,
```

matching the parent polynomial as an element of `Q[x,y,u,v]`. Sympy grevlex off Gröbner basis `[1]`; Singular `dp` standard basis `[1]`; `sat` and first colon likewise `(1)`. The test is not “`det A` happened to be the constant `1`”. The mechanism is the parent saturation identity on an automorphism, not a special feature of triangular projectors.

**All-Witt, actual maps.** For `n=1,…,6`,

```text
F_n = (x-x^{109},\; y ∑_{j=0}^{n-1} (109 x^{108})^j)  (mod 109^n).
```

The producer script checks only the scalar telescope `(1-109z)∑(109z)^j=1-(109z)^n`. Independently, the actual Jacobian of the displayed polynomials equals that telescope: `P_y=0`, `Q_y=S(x)`, so `det J=(1-109 x^{108})S(x)=1-109^n x^{108 n}`. Residual `p`-adic order `n`; reduction `1` modulo `109^n`. The `Q`-polynomial has exactly `n` monomials. The tower is compatible: `Q_n-Q_{n-1}=y(109 x^{108})^{n-1}`.

Marked pair `(0,0),(1,0)`: both coordinates collide at every level. The producer Boolean is `marked_seed_secant * ∑ 109^j == 0` with `marked_seed_secant=0`, a tautology. The actual secant of `F_n` at that pair is independently zero: `a_{12}=0` and `a_{11}=1-∑ x^{108-i}u^i` evaluates to `0` at `(x,u)=(0,1)`, so `e=a_{11}S(u)=0` regardless of the geometric sum `S(1)=(109^n-1)/108`. Finite-level off projectors therefore coexist with linearly growing support. The inverse limit is the nonpolynomial series `Q=y/(1-109 x^{108})`. Idempotent persistence at finite levels does not select a fixed-support polynomial lift.

**Degree and support.** If `deg P=d` and `deg Q=q`, each secant entry has degree at most `d-1` or `q-1`, so `deg e ≤ d+q-2`. For the seed this is `108`, and `e_0` attains it: the bound is sharp and is forced by the reduction `e≡1-(x-u)^{108} (mod 109)`. For fixed supports of `P,Q`, the support of `e` lies in explicit Minkowski sums of divided-difference supports. Both are derived closures of the input support, not new restrictions on the correction coefficients.

**Factor count.** The integer `108` counts etale seed sectors, equivalently local analytic graphs of a hypothetical lift. It is not a theorem that `det A` factors into `108` polynomials of bounded degree in `Z_{109}[u,v][t]`. Weierstrass preparation realises each local graph as `t-φ_r` with `φ_r` analytic, not polynomial. Vieta on those analytic roots tautologically recovers the coefficients of `e` and does not constrain them.

**Discriminant / etaleness.** The discriminant of a degree-`108` polynomial in `t` being a unit is an inequality (simple roots), already guaranteed locally by etaleness of a determinant-one lift. It is not an equation on the correction coefficients.

**Rigid-analytic identity theorem, considered and rejected.** A polynomial vanishing on a nonempty `109`-adic polydisc of full dimension is identically zero, but `e` vanishes only along `2`-dimensional graphs in `4`-space. Vanishing along a thin analytic subset does not force `e≡0` as a polynomial; it is the local redundancy of claim 3. There is no interpolation constraint beyond membership in the localized collision ideal.

**Trace and norm** are the ranks of §2. None of the five quantities (degree, support, factor count, trace, norm) produces a finite coefficient equation not already in `(f_1,f_2)_{x-u}`.

---

## 6. Trichotomy at exact scope

**Not `CONTRADICTION`.** The local picture is consistent: `109` analytic preimages over each target ball is the banked Hensel nonautomorphy of any hypothetical exact lift, restated in secant language. Finite-level maps `F_n` carry compatible off projectors. Trace `109` is a rank. Nothing in the secant identities contradicts existence of a lift, and nothing proves nonexistence.

**Not `NEW-FINITE-CONSTRAINT`.** After quotienting by determinant and collision, the secant row has generic rank zero (claim 3). Degree/support bounds are derived. Seed factorizations and CRT projectors do not survive as bounded polynomial factorizations of a deformed `det A`. Trace and norm are ranks of a split algebra that Hensel realises only analytically.

**`COSTUME`.** The construction exactly recovers the already-known Hensel sheet decomposition in the language of the secant idempotent, and adds no independent coefficient constraint under the compiler hypothesis of §4. The missing object is a *global bounded algebraic realization of the off sectors*: a finite normalization or polynomial branch algebra with a proved degree/support bound; a bounded polynomial factorization of the off algebra whose relations survive localization and are not generated by `f_1,f_2`; or an elimination theorem that compatibility of all `108` analytic graphs forces a nonzero ideal in the fixed-support correction coefficients. Hensel does not supply that object, and fixed support of `P,Q` alone does not supply it.

Distinguish the two uses of `e`:

- *Raw local secant row.* On each off sector, `e` is already in the localized collision ideal. Costume.
- *Global normalization / factorization.* If an independently constructed finite `R` (parent Card C) or a bounded factorization of the off algebra were in hand, traces, multiplication matrices, or Vieta could in principle produce coefficient equations outside `(f_1,f_2)_{x-u}`. No such datum is in the artifacts. That use remains the resurrection condition, not a result.

No exact lift, characteristic-zero point, proof, or counterexample is produced. The cubic-`y` no-go was not consumed. Canonical campaign state is unchanged.

---

## Scope exclusions

- One prime `p=109`, one seed `(x-x^{109},y)`, hypothetical exact `det J=1` lifts only.
- No exponent rectangle, cap widening, AWS, new Witt level, or generic sparse search.
- No inference from finite-level `F_n` to a polynomial inverse limit.
- No inference from residue-ball analytic graphs to global polynomial factors.
- No literature-novelty claim; the adjugate identity is classical, the Hensel split is the banked lemma.
- Characteristic-zero language is purely conditional on an exact integral polynomial lift that this run did not produce.
- `I+(det A)=(1)` for every complex Keller map remains the injectivity endpoint (JC2). This gate does not touch it.

---

## Promotion advice

**Accept the costume.** Record that `SECANT-IDEMPOTENT` applied to AS109 is an exact change of language for the Hensel sheet split, with a proved rank-zero warning against feeding `e` to a collision-aware coefficient compiler.

**Do not promote** any of: a contradiction for AS109 lifts; a new finite constraint on cubic-or-higher corrections; a bounded polynomial factorization of the `108` off sectors; persistence of seed CRT projectors as factors of a deformed `det A`; a closed-support core; a lift; a complex Keller nonautomorphism; a JC2 decision.

**Do not resume this route** by enlarging a compiler with the raw `e` row, by treating Teichmüller roots of `t^{108}-1` as a lifted factorization, or by reading `tr=109` as a vanishing. Resume only with an object that couples the local off sectors globally and algebraically, meeting one of the producer’s three resurrection tests, and whose new row has positive generic rank after quotienting by determinant and collision.

No statement in the producer report, and no statement in this review, proves or disproves JC2.
