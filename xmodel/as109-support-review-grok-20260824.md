# Hostile different-model review — AS109 specification gate

| Field | Value |
|---|---|
| Claim under review | Frozen AS109 support-cancellation specification gate: `NO-FROZEN-GRAMMAR`; parametric two-slot obstruction; Hensel nonautomorphy; closed-support contraction; no enumerated core |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (precisions in §8; none is an overclaim of existence, nonexistence, or a found lift) |
| Evidence tier | independent exact arithmetic over `Z` and `F_109` (producer replay plus a second sparse engine that does not import it); hand binomial composition modulo `109^3`; multivariate Hensel plus Lefschetz embedding on a finitely generated characteristic-zero field |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family, root S) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `c17bd2542b40f3178ec619ae4a73501550555336` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T08:35:00Z – 2026-08-24T08:55:00Z |
| Python | 3.14.6; stdlib only (`math.comb`, integer dicts) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer inputs reread in full before any verdict:

- `xmodel/as109-support-gate-20260824.md` (SHA-256 `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`, matches the launch prompt)
- `cases/as109_support_20260824/PREREGISTRATION.md`
- `cases/as109_support_20260824/manifest.json`
- `cases/as109_support_20260824/FREEZE.sha256`
- `cases/as109_support_20260824/verify_spec_obstruction.py`
- `cases/as109_support_20260824/spec_obstruction.json`

The committed basis is exactly `c17bd2542b40f3178ec619ae4a73501550555336`. All six producer paths above are uncommitted on top of that basis. No producer, canonical, ledger, or case file was edited. No grammar was invented, no cap was widened, and no exponent rectangle was enumerated.

---

## Promotion — negative grammar verdict (`NO-FROZEN-GRAMMAR`)

**Accept as the registered stop for this freeze, at this scope only.** The cap-eight literal-exponent graph, with the frozen first-order gauge and no exponent bound, is not yet a finite exhaustive mathematical object. Successor support is not a gauge invariant without an explicit `mod 109^3` transport, and that transport is not itself a finite normal form.

Do **not** promote this verdict to any of: nonexistence of a cap-eight lift; `HEIGHT-CERT`; `NO-CYCLE-AT-8`; `SUPPORT-ONLY`; `FEASIBLE-CYCLE`; a statement about a larger cap; a statement after a degree rectangle; a characteristic-zero nonexistence theorem. Do not answer it by widening eight, by sampling exponents, or by writing a motif compiler during the stopped run.

## Promotion — Hensel nonautomorphy and closed-support contraction

**Keep as conditional lemmas / resurrection targets. Promote neither to existence.**

- The Hensel lemma is a one-way implication: *if* an exact polynomial lift over `Z_109` with `det J=1` exists, *then* it is noninjective over `Q_109` and, after embedding a finitely generated coefficient-and-preimage field into `C`, is a genuine complex Keller nonautomorphism.
- The contraction criterion is a one-way implication: *if* a finite gauge-fixed coefficient module is nonlinearly closed and `L` is a `Z_109`-unit isomorphism onto its residual module, *then* Banach iteration produces such a lift, and the Hensel lemma applies.

No module in this run meets the contraction hypotheses. No support core was enumerated. These lemmas do not repair the failed grammar, do not license adding slots until closure, and do not produce a characteristic-zero counterexample from the artifacts in hand.

**Quarantine.** No result here proves or disproves JC2. The frozen marked-section collision remains in force for this run; it is not required for the Hensel implication. Do not treat `PASS-SPEC-OBSTRUCTION-CONTROL` as a height certificate for all cap-eight supports.

---

## Scope (not enlarged)

One prime `p=109`, one seed `(x-x^{109},y)` over `F_109`, two marked source sections `(0,0)` and `(1,0)`, at most eight distinct correction slots counted across layers once, and the first nonlinear successor only. Literal exponents range over all of `N^2`. No rectangle, total-degree bound, second seed, AWS, cap widening, or modular-to-characteristic-zero inference is in scope. Characteristic-zero language below is purely conditional on an exact integral polynomial lift that this run did not produce.

Write `L(A,B)=A_x+B_y` and `s=x^{108}`.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Preregistration and manifest hashes were frozen before enumeration; no enumerator was run | **CONFIRMED** | a transition enumerator in the case tree or a hash mismatch against `FREEZE.sha256`; `enumeration_run=true`; freeze listing an enumerator |
| 2 | Displayed `E1`, `E2`, monomial bracket, and `N` are the exact expansion modulo `109^3` | **CONFIRMED** | a `p^2` term in `det J-1` not equal to `L(A_1,B_1)+N(A_0,B_0)`; bracket coefficient not `ad-bc`; packed remainder not `[A,B]-x^{108} B_y` |
| 3 | For every integer `m>=1`, `A_0=y^m`, `B_0=x^{108} y` is a two-slot collision-preserving `E1` solution, arising from `G_m=(x+109 y^m,y)` | **CONFIRMED** | `A_{0x}+B_{0y}≠x^{108}`; a marked-section failure for some `m>=1`; precomposition `F_{\mathrm{can}}∘G_m` not recovering this pair modulo `109^2`; `G_m` not determinant one |
| 4 | Nonlinear residual and transported successor are exact; transport adds three slots, remains collision-preserving, and is not a same-slot cycle | **CONFIRMED** | `N≠-x^{216}+(m \bmod 109)x^{107} y^m`; binomial composition disagreeing with (4.2); a same-slot overlap for some `m>=1`; a vanishing successor coefficient modulo 109 |
| 5 | The monomial-count cap does not make literal exponent enumeration finite; the current gauge quotient does not define an invariant finite graph; `NO-FROZEN-GRAMMAR` is exactly this stop, not nonexistence of cap-eight lifts | **CONFIRMED** | a proved finite gauge-normal-form grammar with successor transport already in the freeze; the gate asserting absence of cap-eight lifts |
| 6 | Hensel nonautomorphy: an exact `Z_109` polynomial lift of the seed with `det J=1` is bijective on each residue ball, hence 109-to-1 onto balls over `(0,b)`, noninjective over `Q_109`, and a complex Keller counterexample after finite-type embedding into `C` | **CONFIRMED** | `J(\overline F)≠I` over `F_109`; Hensel uniqueness failing for a unit Jacobian over a complete DVR; a finitely generated characteristic-zero field with no embedding in `C`; the lemma asserting that such an `F` exists |
| 7 | Closed-support contraction: if a finite gauge-fixed module has `N(U')` in its residual module and `L` a unit inverse/right inverse onto that module, `T(u)=R(s-109 N(u))` is a strict 109-adic contraction and yields an exact lift; combined with 6 this would be a JC2 counterexample | **CONFIRMED** | `det J=1` not equivalent to `L(u)-s+109 N(u)=0`; `N` not 1-Lipschitz on the integral Gauss ball; `R` failing to have `Z_109` entries; the criterion asserting a closed module was found |
| 8 | Canonical and five-slot controls fail closure at `x^{216}` / `x^{324}`; no support core, exact lift, or characteristic-zero counterexample was found or inferred | **CONFIRMED** | `x^{216}` already in `L` of the canonical slot; `x^{324}` in `L` of the five-slot union; a hidden enumerated core; an inferred nonexistence statement |

All remarks below are non-blocking unless marked otherwise. None changes a coefficient, a slot count, or a verdict.

---

## Replay and hashes

Registered command, rerun unmodified from the charged tree:

```sh
python3 cases/as109_support_20260824/verify_spec_obstruction.py
```

Exit code 0. Top-level fields:

```text
verdict = PASS-SPEC-OBSTRUCTION-CONTROL
enumeration_run = false
```

Recomputed SHA-256 (all match the gate tables and `FREEZE.sha256`):

| Artifact | SHA-256 |
|---|---|
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` |
| `cases/as109_support_20260824/PREREGISTRATION.md` | `be9138a90b661f069197a4c22235ee1caa4e03fcecd2dab8c980e8934f2d6301` |
| `cases/as109_support_20260824/manifest.json` | `c69d70805bdba5793f385fca9c289f9a12a8c58c45e1625e1c2f69a9632f0364` |
| `cases/as109_support_20260824/FREEZE.sha256` | `0a535ca2877ec3672044faa5c5f20878c4b95adddf4087b89f772d030d6e140e` |
| `cases/as109_support_20260824/verify_spec_obstruction.py` | `1bb8f86596b75bd43e467dc84b569e8fb2bb2744c198c40f5244f0b054634165` |
| `cases/as109_support_20260824/spec_obstruction.json` | `b95ad244da3ea75100c61143dc9c0026ac567c8acfc2398a86ce1623a101131e` |

The freeze file records only the two pre-enumerator inputs. The verify script and JSON report are post-freeze, as the gate states. The registered program is not a transition enumerator: it recomputes the two frozen hashes and checks the closed-form triangular family at the seven sample exponents `m=1,2,3,108,109,110,1000`. Arithmetic is exact `F_109` sparse polynomials. No CAS, no floating point, no AWS.

Process remark, non-blocking: `spec_obstruction.json` is a curated summary, not byte-identical to the script's stdout (the script emits `sample_replays`; the JSON emits `all_sample_assertions`). Both carry the same identities, and those identities were recomputed independently below.

A second engine, written for this review and not imported from the registered script, used integer (not `F_109`) sparse polynomials and binomial expansion modulo `109^3`. It recorded zero failures on: the `mod 109^3` Jacobian expansion and the packed exact identity, on a spread of supports including the transported family; composition `F_{\mathrm{can}}∘G_m` extracting layers (4.2) for nineteen values of `m` including `109,218,324,1000`; `E1`, `N`, `E2`, and marked collision on that spread; `G_m` determinant, inverse, and fixed points; the monomial bracket on a grid; Fermat `a-a^{109}=0` for every residue `a`; union-slot disjointness for every `m=1..400`; and the two closure probes plus a `{0,±1,2}^5` cube of the five-slot module at `m=1`.

---

## Independent recomputation

### 1. Freeze-before-enumeration — CONFIRMED

The case directory contains exactly five files: `PREREGISTRATION.md`, `manifest.json`, `FREEZE.sha256`, `verify_spec_obstruction.py`, `spec_obstruction.json`. There is no `enumerate_dfs.py`, `enumerate_ilp.py`, or other transition generator. The preregistration header is `SPECIFICATION GATE; NO ENUMERATION RUN`. The manifest `status_at_freeze` is `SPECIFICATION_GATE_NO_ENUMERATION`. The verify script's docstring states it is not a transition enumerator. Git status on the charged basis shows the whole case directory untracked; no enumerator was committed later.

Sampling seven exponents of a closed-form identity is not cap-eight graph enumeration. The finite-grammar gate in preregistration §4 is therefore unentered, and the registered stop `NO-FROZEN-GRAMMAR` is the one that fires.

### 2. Exact expansion modulo `109^3` — CONFIRMED

Let `p=109` and

```text
P = x - x^p + p A_0 + p^2 A_1,
Q = y      + p B_0 + p^2 B_1.
```

Then, exactly over `Z[x,y]` before reducing modulo `p^3`,

```text
P_x = 1 - p x^{p-1} + p A_{0x} + p^2 A_{1x},
P_y = p A_{0y} + p^2 A_{1y},
Q_x = p B_{0x} + p^2 B_{1x},
Q_y = 1 + p B_{0y} + p^2 B_{1y}.
```

The product `P_x Q_y` contributes

```text
1 + p(B_{0y} - x^{p-1} + A_{0x})
  + p^2(B_{1y} - x^{p-1} B_{0y} + A_{0x} B_{0y} + A_{1x})
```

and `P_y Q_x` contributes `p^2 A_{0y} B_{0x}`, with all other terms in `p^3`. Hence

```text
det J(P,Q) = 1
  + p  (A_{0x}+B_{0y}-x^{p-1})
  + p^2(A_{1x}+B_{1y}+(A_{0x}-x^{p-1})B_{0y}-A_{0y} B_{0x})
  + O(p^3).
```

Setting the determinant equal to 1 forces the displayed `E1` and `E2` over `F_p`, with

```text
N(A,B) = (A_x - x^{p-1}) B_y - A_y B_x.
```

The same `N` is `[A,B]-x^{108} B_y`. For monomials,

```text
[x^a y^b, x^c y^d] = (ad-bc) x^{a+c-1} y^{b+d-1},
```

checked identically on a spread of exponents; the coefficient is reduced modulo 109 in the frozen graph, and a zero coefficient is not an edge.

The two-layer expansion is the truncation used by `E1`/`E2`. Packing all corrections into a single pair `(A,B)` over `Z_{109}` gives an identity with no remainder: for `F=(x-x^p+p A,\, y+p B)`,

```text
det J_F - 1 = p(L(A,B)-s) + p^2 N(A,B)
```

exactly in `Z_{109}[x,y]`, because the `2\times 2` determinant produces no `p^3` term. This is the `N` of gate §5.1, not a third formula. The second engine checked both identities, truncated and packed, on the transported family and on mixed supports.

### 3. Parametric two-slot family and triangular gauge — CONFIRMED

Over `Z` already, `A_0=y^m` (`m>=1`) has vanishing `x`-derivative and `B_0=x^{108} y` has `y`-derivative `x^{108}`, so `E1` holds over `F_{109}` and over `Z`. Both polynomials vanish on `y=0`, hence at `(0,0)` and `(1,0)`, so the frozen collision differences are zero. The literal slots are exactly `(P,(0,m))` and `(Q,(108,1))`.

`G_m=(x+109 y^m,\, y)` is triangular with Jacobian `[[1,\, 109 m y^{m-1}],[0,1]]`, determinant one, inverse `(x-109 y^m,\, y)`, and fixes both marked points as polynomial maps over `Z`. Its first-order data `U=y^m`, `V=0` satisfy the frozen gauge equations `U_x+V_y=0` and vanishing at the marked sections.

Canonical first lift modulo `p^2`: `F_{\mathrm{can}}=(x-x^p,\, y+p x^{p-1} y)`. Precomposition:

```text
(x+p y^m)^p ≡ x^p  (mod p^2),
```

because the `k=1` binomial term is `p\cdot p\, x^{p-1} y^m`. Thus

```text
F_{\mathrm{can}}∘G_m ≡ (x - x^p + p y^m,\, y + p x^{p-1} y)  (mod p^2),
```

which is the displayed `(A_0,B_0)`. The family is inside the frozen source-gauge relation, not a formal tangent with no automorphism lift. The lower bound `m>=1` is required for `U(0,0)=U(1,0)=0`; it is not a hidden rectangle.

### 4. Residual, transport, three new slots — CONFIRMED

Directly over `Z`:

```text
N(y^m,\, x^{108} y)
  = (0-x^{108}) x^{108} - (m y^{m-1})(108 x^{107} y)
  = -x^{216} - 108 m x^{107} y^m.
```

Reduce modulo 109: `-108≡1`, so `N=-x^{216}+(m \bmod 109)\, x^{107} y^m`. When `109` divides `m` the second term vanishes; the coefficient of `x^{216}` remains `-1` for every `m>=1`. This is (4.1).

Transport through `mod p^3` is composition, not an `E2` guess. Take the canonical Witt ray

```text
F_{\mathrm{can}} = (x-x^p,\, y + p x^{p-1} y + p^2 x^{2p-2} y)
```

and substitute `X=x+p y^m`, `Y=y`. Binomial terms with `k>=3` lie in `p^3`. The `k=2` term in `X^p` is `p^3(p-1)/2` times a monomial and also vanishes modulo `p^3`. One gets, exactly modulo `p^3`,

```text
P = x - x^p + p y^m - p^2 x^{p-1} y^m,
Q = y + p x^{p-1} y + p^2 x^{2p-2} y + p^2 (p-1) x^{p-2} y^{m+1}.
```

With `p=109` this is (4.2):

```text
A_1 = -x^{108} y^m,
B_1 = x^{216} y + 108 x^{107} y^{m+1}.
```

`L(A_1,B_1)=-N(A_0,B_0)` holds over `F_{109}` for every tested `m`, including multiples of 109 (the extra `B_1` term then cancels `A_{1x}` in the residual, but its coefficient 108 stays nonzero, so the slot remains). Collision holds: every displayed successor monomial has positive `y`-degree.

Slot sets, for every integer `m>=1`:

```text
layer 0:   (P,(0,m)), (Q,(108,1))
successor: (P,(108,m)), (Q,(216,1)), (Q,(107,m+1)).
```

These five labels are pairwise distinct: `0≠108`, `108≠216`, `108≠107`, and `P≠Q`. No successor coefficient vanishes modulo 109. The union through `E2` has five slots, below the cap eight, and is not a same-slot cycle in the preregistration sense (an `E2` solution using no slot outside the layer-zero set). The second engine found no union anomaly for `m=1..400`; the closed forms prove it for every `m>=1`.

### 5. `NO-FROZEN-GRAMMAR` at exactly this scope — CONFIRMED

The registered vertices are literal exponent slots in `N^2`. Already at layer zero the family of claim 3 supplies infinitely many two-slot, collision-preserving `E1` solutions with unbounded exponent `m`. A cap on the *number* of monomials therefore does not yield a finite vertex set. That is the preregistration §4 trigger, and it fires before any enumerator exists.

Precision, not a gap: this family is a *single* first-order gauge orbit of the canonical ray `A_0=0`, `B_0=x^{108} y`. The producer does not claim infinitely many quotient classes at layer zero. The grammar still fails, for the three reasons recorded in gate §4:

1. An SCC on literal exponents depends on the representative.
2. Quotienting by the `mod p^2` gauge without transporting through `mod p^3` can create or delete `N`-support.
3. Exact transport, computed in §4 above, introduces three new slots whose exponents are again unbounded in `m`, so transport is not a finite support normal form.

The property “this displayed representative uses at most eight slots” is therefore not a gauge-invariant finite transition graph. Preregistration §3 required a proved finite normal-form grammar exhaustive for every literal 8-slot support *and* successor invariance or an explicit `mod p^3` gauge lift. Neither proof is in the freeze. The registered verdict is `NO-FROZEN-GRAMMAR`.

Gate §7 states, and this review repeats: that verdict is not a theorem that no cap-eight bounded-support lift exists, not a height certificate, and not a characteristic-zero inference. A symbolic-motif redesign would be a new dependency, not this experiment.

### 6. Hensel nonautomorphy — CONFIRMED

Let `F∈Z_{109}[x,y]^2` reduce to `\overline F=(x-x^{109},y)` and satisfy `det J_F=1` as a polynomial identity. Over `F_{109}`,

```text
d(x^{109}) = 109 x^{108} = 0, \qquad J(\overline F) = I
```

as a matrix of polynomials, hence at every residue point. Also `a^{109}=a` for all `a∈F_{109}`, so `\overline F(a,b)=(0,b)`.

`Z_{109}` is a complete DVR. For any residue `c∈F_{109}^2` and any lift `\hat c`, `det J_F(\hat c)≡1\pmod{109}` is a unit. Multivariate Hensel therefore gives: for every target `t` in the residue ball `\overline F(c)+109 Z_{109}^2`, the equation `F(z)=t` has exactly one solution in the source ball `c+109 Z_{109}^2`. So `F` maps each residue ball bijectively onto its target residue ball.

Fix `b∈F_{109}`. The 109 source balls `(a,b)+109 Z_{109}^2`, `a∈F_{109}`, all map onto the same target ball `(0,b)+109 Z_{109}^2`. Every integral target in that ball, including the origin when `b=0`, therefore has 109 distinct preimages in `Z_{109}^2`. Those points lie in `Q_{109}^2`, so `F` is not injective over `Q_{109}` and is not a polynomial automorphism of `A^2_{Q_{109}}`.

Complex scope. `F` has finitely many coefficients in `Z_{109}`. Adjoin those coefficients and two distinct Hensel preimages (four coordinates) to `Q`. The result `K` is a finitely generated field of characteristic zero. Any such field embeds in `C`: it is a finite extension of a purely transcendental extension `Q(t_1,\ldots,t_r)`, `C` has infinite transcendence degree over `Q`, and `C` is algebraically closed of characteristic zero. Field embeddings are injective, so the two preimages remain distinct. The identities `det J_F=1` and `F(z_1)=F(z_2)` are polynomial and survive. The image is a pair of polynomials in `C[x,y]` with Jacobian determinant 1 that is not injective, hence not an automorphism: a complex plane Keller counterexample.

Hypotheses actually used: `F` is a *polynomial* (finite support) with *integral* `Z_{109}` coefficients; the reduction is this seed, so `J(\overline F)=I` everywhere; `det J_F=1` exactly; completeness of `Z_{109}`; finite generation of `K`. A valuation-preserving embedding `Q_{109}\to C` is not required and is not claimed. A 109-adic *series* lift is excluded.

The lemma does not use the frozen marked-section equations. The collision that embeds is a pair of Hensel preimages of a common target (for `b=0`, one may take the origin), not necessarily the lattice points `(0,0)` and `(1,0)` as integral values of `F`. Those two lattice points both reduce to `(0,0)` but need not be equal as `Z_{109}`-points unless collision holds at every Witt layer. The producer does not assert existence of `F` and does not repair the grammar. The witness family of claims 3–4 satisfies the frozen two-layer collision anyway.

### 7. Closed-support contraction — CONFIRMED

Pack the lift as `F=(x-x^{109}+109 A,\, y+109 B)` with `(A,B)` in a coefficient module. By the packed identity of §2, `det J_F=1` if and only if

```text
E(u) = L(u) - s + 109 N(u) = 0, \qquad N(A,B)=[A,B]-x^{108} B_y.
```

Hypotheses, all stated or immediate from “finite free” / “unit inverse” / “unit coefficient ball”:

1. `U'` is a finite free `Z_{109}`-module of coefficients on a finite, already gauge-fixed monomial support.
2. `W` is a finite free residual module, spanned by finitely many residual monomials, with `s∈W`, `L(U')⊂W`, and `N(U')⊂W` as polynomial maps (no truncation: every pairwise bracket lands in `W`).
3. `L:U'\to W` admits a `Z_{109}`-unit inverse, or a right inverse `R` with `U'=\mathrm{im}\, R`. Then `L` is an isomorphism `U'\cong W`. The adjugate of an integral exponent matrix, divided by a unit determinant, has entries in `Z_{109}`, so `|R|_p\le 1` in the Gauss max-norm.
4. The ball is the integral Gauss ball `Z_{109}^{\mathrm{rk}}`, not the group of units and not `Q_{109}^{\mathrm{rk}}`. On that ball, polynomial maps with `Z_{109}` coefficients are 1-Lipschitz: integer exponents satisfy `|a|_{109}\le 1`, and products satisfy `|u_i v_j-u_i' v_j'|_{109}\le |u-u'|_{109}`.

Then `T(u)=R(s-109 N(u))` maps the ball to itself. The factor 109 multiplies the Lipschitz constant of `N` by `|109|_{109}=1/109<1`, so `T` is a strict contraction of a complete metric space. Banach supplies a unique fixed point. Applying `L` recovers `E(u)=0`. Finite support plus `Z_{109}` coefficients means `F` is a polynomial over `Z_{109}` reducing to the seed with `det J_F=1`. Claim 6 then yields a complex Keller counterexample.

`UNIT-L` over `F_{109}` (determinant not divisible by 109) is equivalent, by completeness, to a `Z_{109}`-unit inverse. If some allowed exponents vanish modulo 109, `L` may drop rank; those supports are simply excluded by the unit hypothesis. The criterion does not include the frozen marked-section linear conditions; combined with claim 6 they are unnecessary for nonautomorphy. It does *not* assert that any enumerated module satisfies the hypotheses. Gate §5.1 records it only as a resurrection target.

### 8. Controls fail closure; nothing found or inferred — CONFIRMED

Canonical slot `B=x^{108} y`: `L(U)` is supported at `x^{108}`, while `N=-x^{216}` is not. Failure at `x^{216}`.

Five-slot union of (4.2), for every `m>=1`:

```text
L(U') spanned by x^{108}, x^{216}, x^{107} y^m.
```

The allowed vector `A=0`, `B=x^{216} y` lies in the module and produces `N=-x^{324}`, which is outside that span. Failure at `x^{324}`. This is a module-closure probe, not a check of the single transported solution (that solution satisfies `E2` by construction, so its `N` does land in `L(U')`). The second engine's `{0,±1,2}^5` cube at `m=1` produced additional escaping residual monomials `x^{106} y^2`, `x^{215} y`, and `x^{323} y`. Enlarging `W` to contain `x^{324}` would break `UNIT-L`, because `L(U')` still does not cover it.

The run did not enumerate, so no candidate was tested against `CLOSED-SUPPORT+UNIT-L`. No exact lift was produced. No characteristic-zero counterexample was inferred. The canonical escaping ray `B_0=x^{108} y \to B_1=x^{216} y \to\cdots` is a control, not a height certificate for all cap-eight supports.

---

## Smallest missing hypothesis or overclaim

None of the eight claims is an existence theorem, a nonexistence theorem for cap-eight lifts, or a characteristic-zero decision.

The smallest precision a reader could miss, and that this review therefore isolates, is:

- Claim 5 fails *literal* finiteness and *invariant-graph* well-definedness. It does not prove that the first-order gauge *quotient* of 8-slot supports is an infinite set of classes. The displayed family is one orbit. The registered stop is still correct, because the freeze demanded a finite normal form with successor transport and did not supply one.
- Claim 6’s embedded “collision” is a pair of Hensel preimages, not `F(0,0)=F(1,0)` as integral lattice-point values.
- Claim 7’s “unit coefficient ball” is the integral Gauss ball `Z_{109}^{k}`. The combination with claim 6 requires finite support (already built into a finite free monomial module). A series solution of the contraction on an infinite monomial module would not be a polynomial, and claim 6 would not apply.

Those are scope reminders, not missing hypotheses in the written lemmas.

---

## Stop conditions that remain in force

No cap, degree, or prime may be changed in response to this review. A request to choose a large exponent box is not a resurrection trigger. The only resurrection trigger remains a separately reviewed theorem giving either a finite gauge-normal-form grammar with exact successor transport, or a terminating symbolic-motif classification exhaustive for all exponent supports of size at most eight, or an explicit finite module that meets `CLOSED-SUPPORT+UNIT-L`.

No result here proves or disproves JC2.
