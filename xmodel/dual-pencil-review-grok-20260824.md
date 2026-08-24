# Hostile different-model review — dual-pencil definition gate

| Field | Value |
|---|---|
| Claim under review | Frozen dual-pencil infinity-defect definition gate: intrinsic Suzuki defect of each `H=aP+bQ` is well-defined; it does not define the proposed finite effective divisor on the dual target line; corrected verdict `PRIOR-ART / JUMP-ONLY / TYPE-FAIL`; no GRR descendant |
| Overall verdict | **CONFIRMED** |
| Smallest failing theorem / sign / hypothesis | none |
| Evidence tier | independent topology over `C`; primary-source read of Suzuki 1974 (J-STAGE PDF), Fourrier 1996 (NUMDAM PDF), Siersma–Tibăr arXiv:math/0207076 (Moscow Math. J. 3 (2003)), Joiţa–Tibăr arXiv:1512.07499, Jelonek–Tibăr arXiv:1401.6544, Nguyen Van Chau arXiv:math/0305088; elementary Jacobian and Euler identities |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) and from the internal hostile audit |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `c17bd2542b40f3178ec619ae4a73501550555336` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T08:35:00Z – 2026-08-24T09:05:00Z |
| Host | Darwin arm64 |

Producer inputs reread in full before any verdict. Frozen hashes recomputed on disk:

| Artifact | Charged SHA-256 | On-disk result |
|---|---|---|
| corrected producer `xmodel/dual-pencil-definition-gate-20260824.md` | `b96a6564f4f1f494c6c86c3fa69f0131e9c772d5823558fae6b0ee9d0a34e1ec` | match |
| internal hostile audit `xmodel/dual-pencil-hostile-audit-20260824.md` | `f65de557bfec85eb7ef407b6cf4f087ab1b5f458abf3d3b9386ef88f5b9037db` | match |

The original producer before correction, charged as
`9b84cbd2e217ba8847899e787c5ae8adf8ed36c39da1f4a5f27a7e34b6891e5b`,
is not present as a separate on-disk file. The review attacks the corrected
producer. The internal audit was read and then ignored as evidence.

No producer, audit, or canonical file was edited.

**Promotion.** None. No claim, lemma, divisor, GRR class, client book, ledger
row, AWS job, or wording may be promoted off this record.

**Quarantine / explicit exclusions.** This gate yields no global obstruction,
no positivity theorem, no automorphy criterion beyond the classical coordinate
endpoint, no generic vanishing of defect, and neither a proof nor a
counterexample of JC2. Do not treat the jump cycle as a degree-zero GRR
input. Do not identify `δ(H_ℓ)` with `L·A(F)`. Do not treat Siersma–Tibăr
Example 8.4 as a Keller-pencil sign. Do not delete or change sign of the
possible degree-drop coefficient.

The internal audit is not evidence. Agreement with it is not a confidence
multiplier.

---

## Headline and subclaim table

Let `F=(P,Q):A^2_C → A^2_C` satisfy `J(P,Q)=1`, write `B=P(V*)` for the dual
target line, and `H_ℓ=aP+bQ` for a generator of `ℓ=[a:b]`. Let `G_H` be a
generic fiber of `H=H_ℓ`, and

```text
ε_c(H) = χ(H^{-1}(c)) - χ(G_H),
δ(H)   = sum_c ε_c(H).
```

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | For every nonzero `(a,b)`, `H=aP+bQ` is a polynomial submersion; primitive factorization / Suzuki give a connected generic fiber and `δ(H)=1-χ(G_H)=b_1(G_H)≥0` with the report's definitions | **CONFIRMED** | a point of `A^2` where `dH=0`; a composite `H=φ∘g` with `deg φ>1` compatible with submersivity; `ε_c` of opposite sign matching Suzuki's `d_i+a_i`; disconnected generic fiber of a primitive polynomial |
| 2 | `δ(H)=0` iff the generic fiber is an embedded `A^1`; Suzuki Theorem 5 / AMS makes `H` a coordinate; one coordinate pencil direction plus a Jacobian mate triangularizes `F` to an automorphism | **CONFIRMED** | a smooth simply-connected affine plane curve not Aut-equivalent to an axis; `J(x,K)≠K_y`; a non-polynomial triangular correction |
| 3 | A hypothetical nonautomorphic Keller pair has `δ(H_ℓ)≥1` for every `ℓ`, so the raw universal defect has horizontal support dominating `B` and is not a finite divisor there | **CONFIRMED** | a nonautomorphic Keller pair with some coordinate projection; a constructible function that is `≥1` everywhere yet is a Weil divisor on `P^1` |
| 4 | Off at most one degree-drop direction, Siersma–Tibăr Proposition 5.1 gives `δ(H_{ℓ_0})-δ_gen≤0`; the possible degree-drop coefficient is uncontrolled by that constant-degree theorem | **CONFIRMED** | Prop. 5.1 having the opposite inequality; the family failing to be a constant-degree FISI deformation off `E_deg`; `#E_deg≥2`; a cited constant-degree sign at the degree-drop point |
| 5 | Subtracting generic defect yields only a signed / anti-effective jump cycle and removes the proposed zero-degree endpoint; no resolution-independent finite effective divisor or GRR client survives | **CONFIRMED** | a theorem that `deg J_F=0`; effectivity of `J_F` including `E_deg`; a blowup-invariant coefficientwise divisor on `B` extracting only the horizontal-free part |
| 6 | The ingredients are prior art; the corrected combined verdict `PRIOR-ART / JUMP-ONLY / TYPE-FAIL` follows | **CONFIRMED** | a primary theorem already producing a finite effective dual-pencil divisor for Keller pairs; a new identity not in Suzuki / AMS / Hà–Lê / Siersma–Tibăr |
| 7 | Scope: no global obstruction, positivity theorem, automorphy result, or JC2 proof/counterexample may be inferred | **CONFIRMED** | the producer claiming generic vanishing of `δ`, a new positivity law, or a JC2 decision |

All remarks below are non-blocking unless marked otherwise. None changes a
sign, a support statement, or a verdict.

---

## 1. Submersion, primitivity, connected generic fiber, defect formula — CONFIRMED

**Submersion.** Differentiating `H=aP+bQ` gives

```text
dH = (a P_x + b Q_x) dx + (a P_y + b Q_y) dy = (a,b) · DF.
```

`DF` is invertible because `det DF=J(P,Q)=1`, and `(a,b)≠0`, so `dH` has no
zero in `A^2`. Every fiber of `H` is smooth. All bifurcations are at infinity.

**Primitivity / connected generic fiber.** Suzuki, p. 242: a nonconstant plane
polynomial factors as `f=φ(F)` with `F` primitive, and a polynomial is
primitive when some characteristic surface is irreducible of order one; ordinary
fibers of a primitive polynomial are then of a single type `(g,n)` with `n≥1`.
If `H=φ(g)` with `deg φ>1`, then `φ'` has a root `u∈C` (characteristic zero),
the fiber `g^{-1}(u)` is nonempty (nonconstant polynomial `C^2→C` is
surjective), and `dH=φ'(g) dg` vanishes along that fiber, contradicting
submersivity. Thus `H` is primitive, and a generic fiber `G_H` is a smooth
connected affine curve.

**Euler defects.** For a value `c` not in the (empty) affine critical-value set,
Hà–Lê as quoted in Joiţa–Tibăr, introduction, says `c` is atypical if and only
if `χ` of nearby fibers is not constant. Suzuki, p. 245, sets

```text
a_i = b^2(Ŝ_i) - b^2(Ŝ) ≥ 0,
d_i = b^1(Ŝ) - b^1(Ŝ_i) ≥ 0,
d_i + a_i = χ(Ŝ_i) - χ(Ŝ) = λ_i + μ_i + ν_i,
```

and notes that `d_i+a_i=0` implies `c_i` is not critical. The one-point
compactifications `Ŝ` differ from the affine fibers by one point, so the affine
Euler jump equals `d_i+a_i`. The report's

```text
ε_c(H) = χ(H^{-1}(c)) - χ(G_H)
```

is therefore nonnegative, and `c∈B_∞(H)` if and only if `ε_c(H)>0`. This is
the same sign as Suzuki, not the opposite local-Milnor convention.

**Total formula.** Suzuki Theorem 2, pp. 246–247: a primitive polynomial of
type `(g,n)` satisfies `∑(d_i+a_i)=2g+n-1`. A smooth connected affine curve of
compactification genus `g` with `r≥1` punctures has

```text
χ(G) = 2 - 2g - r,     b_1(G) = 2g + r - 1,     1 - χ(G) = b_1(G).
```

Affine curves in `A^2` are noncompact, so `r≥1` and `b_1≥0`. Hence

```text
δ(H) := ∑_c ε_c(H) = 1 - χ(G_H) = b_1(G_H) = 2g_H + r_H - 1 ≥ 0.
```

In the submersion case Suzuki's affine indices `λ_i` vanish, so every summand
is an infinity defect. Siersma–Tibăr (2.1) writes the same total as
`b_{n-1}(G)=μ+λ`; here `n=2` and `μ=0`, so `δ=λ`. The identification is of
totals, not of local `ε_c` with local Milnor–Lê numbers `λ_{p,t}`. Totals
suffice for every later claim.

Target rescaling of the generator of `ℓ` rescales values but does not change
fiber topology, `ε_c`, or `δ`. The Tot(`O_B(1)`) typing is correct and is not
load-bearing for the type failure.

---

## 2. Zero-defect endpoint and one coordinate direction — CONFIRMED

**Topology.** `δ(H)=0` forces `g_H=0` and `r_H=1`. A smooth connected affine
curve of that type is algebraically isomorphic to `A^1` (compactification `P^1`
minus one point). Every fiber of a submersion is already nonsingular, so the
generic fiber is a nonsingular embedded affine line.

**Embedding theorem.** Suzuki Theorem 5, p. 252, solves the problem stated on
p. 251: an irreducible, nonsingular, simply-connected affine curve in `C^2` is
the image of a coordinate axis under an algebraic automorphism of `C^2`. This
is the Abhyankar–Moh–Suzuki embedding theorem. After that automorphism the
image is `{x=0}`, whose ideal is `(x)`. The fiber `{H=c}` is irreducible of
order one, so `(H-c)∘φ^{-1}=λ x` with `λ∈C^*`. Thus `H` itself is a
coordinate.

Hypotheses actually used: characteristic zero (here `C`); primitivity / order
one; smoothness from the submersion; simple connectivity of `A^1`. Jung–van
der Kulk is not used.

**Keller mate.** If `H_ℓ=aP+bQ` is a coordinate, choose `(c,d)` with
`ad-bc=1` and set `K_ℓ=cP+dQ`. Then `J(H_ℓ,K_ℓ)=ad-bc=1`. In source
coordinates with `H_ℓ=x` one has `K_y=1`, hence `K_ℓ=y+r(x)` with `r`
polynomial. The triangular map `(x,y+r(x))` is an automorphism by the explicit
inverse `(x,y-r(x))`. Since `(H_ℓ,K_ℓ)=M∘F` with `M∈SL_2(C)`, `F` is an
automorphism.

The implication is sharp: a single coordinate direction already finishes the
map. Generic vanishing of `δ` on `B` is therefore equivalent to JC2, as the
report states. That equivalence is a scope warning, not a theorem proved here.

---

## 3. Hypothetical nonautomorphism ⇒ positive defect in every direction — CONFIRMED

The boxed implication is the contrapositive of §2: if some `δ(H_ℓ)=0`, then
`F` is an automorphism. A hypothetical nonautomorphic Keller pair therefore
has `δ(H_ℓ)≥1` (an integer) for every `ℓ∈B`.

The universal incidence

```text
Z_∞ = ∑_{(ℓ,c)} ε_c(H_ℓ) [(ℓ,c)]  ⊂ Tot(O_B(1))
```

then meets every fiber of Tot(`O_B(1)`)→`B`. Fiberwise pushforward is the
constructible function `ℓ↦δ(H_ℓ)`, constant on a nonempty Zariski-open of the
curve `B` by algebraicity of polynomial-map bifurcation loci (Joiţa–Tibăr,
introduction, citing the standard constructibility of `B(f)`). A Weil divisor
on `B≅P^1` is a finite formal sum of points and vanishes at the generic point.
A constructible function that is a positive integer generically is not a Weil
divisor on `B`. That is exactly `TYPE-FAIL` of the proposed coefficient

```text
coefficient at ell = total infinity defect of H_ell
```

in the only regime in which a new obstruction could exist. If instead `F` is
an automorphism then `δ≡0`, which is the zero divisor and supplies no
obstruction.

The Jelonek / Nguyen Van Chau picture is compatible and is not used more
strongly than the sources permit. Jelonek: the nonproperness set of a dominant
generically finite polynomial map is empty or a hypersurface. Nguyen Van Chau:
for a nonsingular polynomial map `C^2→C^2`, if nonempty it is a curve with one
point at infinity. A generic *line* meets the projective closure of `A(F)`
transversely, but as the direction `ℓ` varies the critical values of the
projection `A(F)→A^1` sweep a horizontal curve in `(ℓ,c)`-space. The report
correctly refuses to identify `L·A(F)` with `δ(H_ℓ)` and does not treat
“directions tangent to `A(F)`” as a finite set. The positive baseline is the
Suzuki endpoint, not this picture.

---

## 4. Siersma–Tibăr sign, `#E_deg≤1`, uncontrolled degree-drop — CONFIRMED

**Constant-degree locus.** Let `D=max(deg P, deg Q)`. The degree-`D` part of
`H_ℓ` is the linear form `ℓ↦a P_D+b Q_D` on `(a,b)`, not identically zero.
Its vanishing locus in `P^1` is empty or one point, so `#E_deg≤1`.

**FISI hypotheses.** Siersma–Tibăr work throughout with constant-degree
deformations. Definition 2.1 / Example 3.2: a constant-degree deformation of
plane polynomials with isolated affine singularities is a FISI deformation.
Off `E_deg` the family `H_s=P+sQ` (and the symmetric chart) has constant
degree; every member is a submersion, hence has empty affine singular locus,
and is primitive, hence reduced. In two variables, `dim W_s≤0` is automatic
at constant degree. Proposition 5.1 therefore applies to a local 1-parameter
slice through any `ℓ_0∉E_deg`.

**The inequality and every sign.** Proposition 5.1: for a FISI deformation,

```text
γ(s) := μ(s)+λ(s) ≥ μ(0)+λ(0).
```

The proof is the lower semi-continuity of the local Milnor numbers in (5.1),

```text
γ(s) = (d-1)^n - ∑_{p_i∈W_s} (μ_{p_i,gen}(s)+μ_{p_i}^∞(s)),
```

which uses the same `d` on both sides. Taking `s` nearby general and `0` as
`ℓ_0`, and using `μ=0` together with `δ=λ` from §1,

```text
δ_gen ≥ δ(H_{ℓ_0}),     i.e.     δ(H_{ℓ_0}) - δ_gen ≤ 0.
```

Exceptional directions on `B` are finite, so nearby general members of the
slice have the generic value `δ_gen` of the dual line. The jump-cycle
coefficients are therefore `≤0` off `E_deg`: `J_F` is anti-effective away
from at most one point.

The inequality is the opposite of ordinary local-Milnor conservation, which
is the point of Siersma–Tibăr's paragraph before Proposition 5.1. The original
producer's claim that no sign was available is the statement the correction
replaces; it is not reused.

**Uncontrolled coefficient.** Proposition 5.1 is a constant-degree theorem. It
does not apply on `E_deg`. Discussion after Corollary 5.2 records that `λ`
alone may rise or fall when `μ` is allowed to compensate; that freedom is
killed here by `μ≡0`, but only inside the constant-degree locus. Example 8.3
is FISI and shows `λ(0)=2>λ(s)=0` with `γ` still nondecreasing, the expected
direction. Example 8.4 is explicitly non-FISI (`f_s=x+s x^2 y+z^3` in three
variables) and is not a Keller-pencil sign theorem. No cited result controls
the coefficient at `E_deg`.

Deleting that term would be a noncanonical compactification correction, as
the report says.

---

## 5. Jump cycle, lost degree-zero endpoint, no GRR client — CONFIRMED

Algebraic stratification makes `δ(H_ℓ)` constant on a Zariski-open of `B`.
The residual

```text
J_F = ∑_{ℓ∈B} (δ(H_ℓ) - δ_gen) [ℓ]
```

is a finite formal cycle by construction (`JUMP-ONLY`). The generic horizontal
mass `δ_gen` has been subtracted by definition, not cancelled by `J=1`. Off
`E_deg` the coefficients are `≤0`; at `E_deg` they are uncontrolled. There is
no theorem that `deg J_F=0`.

An effective divisor of degree zero on `P^1` is the zero divisor. Recovering
degree zero after discarding the horizontal baseline would already be the
missing generic-vanishing theorem, i.e. JC2 in this language. Taking positive
parts would manufacture effectivity and destroy additivity. Either operation
is `COSTUME` relative to the proposed card.

**Resolution independence of the aggregate, not of a base divisor.** `B_∞(H)`,
each `ε_c(H)`, and `δ(H)` are topological invariants of the polynomial map.
Fourrier, Theorem 1, p. 647: dual resolution trees are equivalent under
blowups and contractions. Fourrier, theorem p. 660: regularity at infinity is
topological triviality of `f` outside a large ball. Fourrier, Corollary 2,
p. 661: the finite set of affine critical values together with irregular
values at infinity is the minimal global bifurcation set. Extra blowups
redistribute local vanishing-cycle terms; only the aggregated Euler defect is
invariant. A common resolution of the universal pencil can represent `Z_∞`,
including its horizontal components. Deleting those components to obtain a
divisor on `B` is an additional noncanonical operation. It does not produce a
GRR class.

`J_F` is itself a resolution-independent finite formal cycle. That does not
save a GRR client: it is not the proposed object, it is not effective, and it
has no degree-zero formula.

---

## 6. Priority and the combined verdict — CONFIRMED

Every load-bearing identity is classical.

- Suzuki 1974, J. Math. Soc. Japan 26: primitive factorization p. 242;
  Theorem 2 pp. 246–247; Theorem 5 p. 252.
- Abhyankar–Moh 1975 is the same embedding theorem; the working citation
  here is Suzuki Theorem 5, which was read.
- Hà–Lê Euler criterion, as stated in Joiţa–Tibăr 2015, introduction, and
  recovered in Fourrier, Remarque 4, p. 660.
- Siersma–Tibăr, Moscow Math. J. 3 (2003), Proposition 5.1, discussion after
  Corollary 5.2, Examples 8.3–8.4.
- Fourrier 1996 for resolution equivalence and the minimal bifurcation set.

There is no new coefficient, no new vanishing, and no new divisor. The
intrinsic coefficients and the zero-defect coordinate endpoint are `PRIOR-ART`.
Over the dual line only finitely many deviations from a generic baseline
remain, which is `JUMP-ONLY`. In the hypothetical counterexample regime the
baseline is at least one in every direction, so the raw defect is not an
effective divisor on `B`, which is `TYPE-FAIL`. The combined verdict follows
and is the allowed first-gate stop.

---

## 7. Scope — CONFIRMED

Generic vanishing of `δ(H_ℓ)` is equivalent to JC2 by §2. The gate does not
prove it. Automorphism controls (identity, triangular, two-shear, Hénon
tower) have `δ=0` because they *are* automorphisms; they do not test a
positive baseline. Broughton `h=x+x^2 y` is a single polynomial, not a Keller
pair. Direct check: for `t≠0` one has `x≠0` and `y=(t-x)/x^2`, so the fiber
is `C^*` and `χ=0`; at `t=0` the fiber is `{x=0}⊔{xy=-1}≅A^1 ⊔ C^*` and
`χ=1`. Thus `B_∞={0}` and `ε_0=δ=1`, matching Jelonek–Tibăr Remark 1.3. It
shows that critical-point-freeness alone permits positive defect. It does not
supply a nonautomorphic Keller pair.

No-log / different identities for Keller maps remain valid and do not force
`δ=0`. Treating their cancellation as `deg J_F=0` would again omit the
horizontal baseline.

Nothing in this gate is a global obstruction, a positivity theorem, an
automorphy criterion beyond AMS, a proof of JC2, or a counterexample.

---

## Independent identities (no CAS)

- `J(x,y)=1`; `J(x,y+x^n)=1`; inverse of `(x,y+r(x))` is `(x,y-r(x))`.
- `J(aP+bQ,cP+dQ)=(ad-bc)J(P,Q)`.
- Linear algebra of leading forms: `#E_deg≤1`.
- Euler: `χ(A^1)=1`, `χ(C^*)=0`, Broughton jump `1-0=1`.
- Homotopy: smooth connected affine curve of type `(g,r)` has
  `b_1=2g+r-1=1-χ`.

All match the report.

---

## Source caveats

Read in full, or in the cited pages, from primary text:

1. Masakazu Suzuki, *Propriétés topologiques des polynômes de deux variables
   complexes, et automorphismes algébriques de l'espace C²*, J. Math. Soc.
   Japan 26 (1974), 241–257. Official J-STAGE PDF.
2. Laurence Fourrier, *Topologie d'un polynôme de deux variables complexes au
   voisinage de l'infini*, Ann. Inst. Fourier 46 (1996), 645–687. NUMDAM PDF,
   including pp. 647–648, 660–661.
3. Dirk Siersma and Mihai Tibăr, *Deformations of polynomials, boundary
   singularities and monodromy*, arXiv:math/0207076, corresponding to Moscow
   Math. J. 3 (2003), no. 2, 661–679. Proposition 5.1, Corollary 5.2 and the
   following paragraph, Examples 8.3–8.4. Journal pagination was not compared
   line-by-line to a publisher PDF; the stated Proposition 5.1 is unambiguous
   on the arXiv text.
4. Cezar Joiţa and Mihai Tibăr, *Bifurcation set of multi-parameter families
   of complex curves*, arXiv:1512.07499. Introduction's Hà–Lê statement and
   algebraicity of bifurcation loci.
5. Zbigniew Jelonek and Mihai Tibăr, arXiv:1401.6544, Remark 1.3 (Broughton).
6. Nguyen Van Chau, arXiv:math/0305088, Theorem 1 / Corollary 2.

Not read as PDFs, and not used as load-bearing steps of the decisive chain:

- Abhyankar–Moh, J. reine angew. Math. 276 (1975). The embedding theorem
  actually applied is Suzuki Theorem 5.
- S. A. Broughton, Invent. Math. 92 (1988). The Euler computation is
  elementary and was redone directly.
- Zbigniew Jelonek, Ann. Polon. Math. 58 (1993). Used only for the
  non-decisive nonproperness picture.
- Hà–Lê, Acta Math. Vietnam. 9 (1984). Quoted from Joiţa–Tibăr and Fourrier,
  which state the Euler criterion in the form used.

ArXiv versions are unauthenticated relative to the journal of record except
where noted. None of these caveats moves a sign or a support statement.

---

## Promotion advice

Do not promote. Do not open a GRR sequel, a second compactification, a client
book, an AWS job, or a ledger row. The definition gate has stopped: the
proposed raw defect is the wrong type of object on the dual line, and the
only residual finite cycle is jump-only, signed, and without a degree formula.
A later dual-pencil object would have to be a genuinely new typed construction,
not a resuscitation of `ℓ↦δ(H_ℓ)` or of `J_F`.
