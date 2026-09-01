# Hostile review: ROW-84 transport + EDGE-MODULI kills

Lane: `row-64-84-closure-review-grok46-20260901`
Model: Grok 4.6. Started 2026-09-01. Budget 3h hard.
Mode: desk-scale exact reasoning; no CAS; literature fetch permitted with hashes.
Stance: different-model gate; default to refutation.

## 0. Inputs, hashes, and standing constraints

Stop-check: `shasum -a 256` on the five frozen copies, **before any was read**, reproduced the boxed manifest byte-for-byte. The stop condition did not fire.

```text
6bdd164ca89bfd8b8947dbb23222929bfd575c48e65b261f3c085397de42bd64  pi1s4-84-row-kill-opus5-20260901.md
d853764d8eebc2c9d59a72ec2816bbc1122708649dd790307bfb304c659b440c  pi1s4-64-edge-moduli-gpt55-20260901.md
0fb4778e6baa40fa6961e1cae8e7c7faf5dd88e3f5ca4ce2dd0c2ba8f02fba83  pi1s4-64-torus-check-hostile-review-sol56-20260901.md
9b03dad679d5060d2456bff81037feb008c448196dc1ddf8bee3a06d20a0b200  pi1s4-64-torus-check-verification-grok46-20260901.md
126c2d2941dcd5b3f95584d0d2cc371dea270ed30494f773abafd4f9e5c20286  block-descent-a1-na-rowsweep-coordinator-integration-fable5-20260831.md
```

Path abbreviations below: `R84`, `EM`, `GATE`, `VER`, `CI`. Line numbers refer to those frozen copies.

Literature re-fetched as PDFs and re-hashed on this host; both reproduce the receipts already in `GATE`/`VER`/`R84`.

| tag | source | URL | SHA-256 |
|---|---|---|---|
| Sh12 | Shirane, arXiv:1211.2526v1 | `https://arxiv.org/pdf/1211.2526` | `b37e8d45381a299e489516fd479ec896a016f06c402b16ae049d310aa1618153` |
| Oka05 | Oka, arXiv:math/0507051v1 | `https://arxiv.org/pdf/math/0507051` | `2a864cdd2530533c30f45d2cf9e9435e24f6a53b3788094df26a63e7208213e4` |

No CAS, no job of uncertain duration, no canonical ledger, no charged-file edit, no `jc2-lean`. FALLACY-v2 applies as a negative rule only: this report asserts no new exit price and therefore contains no `charge_basis` line. Miranda 1985 was not fetched; Sh12 §1.1 is used only as a displayed statement, and only off the critical path.

**Typing of the charged objects.** `CI` Theorem N-A is promoted and is not re-audited. ROW-SWEEP / ROW-NF / Theorem FOLD remain `PROVISIONAL` (`CI` §2, `GATE` R1, `VER` §7). Charged Theorem ROW-KILL is the object `GATE` already corrected, not the original torus-check text. `R84` Theorem B and `EM` are the two closure chains under review.

Stance: default to refutation. A producer sentence is not inherited because a neighbouring lemma is true.

## 1. Part A — ROW-84 (Opus): derive-check of Delta iff deg(P-Q^2)=6

Let `(P,Q)` be monic of degrees `8` and `4`, birational onto its image `D' ⊂ A²`. The Abhyankar–Moh data `Δ=(8,4,6,3)` is a legal δ-sequence: `d=(8,4,2,1)`, quotients `n_i=2`, and `n_1 δ_1=8∈⟨8⟩`, `n_2 δ_2=12∈⟨8,4⟩`, `n_3 δ_3=6∈⟨8,4,6⟩`, with the two strict inequalities `δ_2=6<8` and `δ_3=3<12`. The affine semigroup is then `⟨8,4,6,3⟩=⟨3,4⟩`, gaps `{1,2,5}`, matching `δ_aff=3`.

In the chart `X=1` at `s=1/t`, `v=s^4 \tilde Q/\tilde P` and `w=s^8/\tilde P`. One place, at `Q_∞=[1:0:0]`, multiplicity `min(4,8)=4`, and `I(C',L_∞;Q_∞)=ord_s w=8`, so Bézout exhausts `C'∩L_∞={Q_∞}` with `L_∞` the tangent. Both `ord v` and `ord w` lie in `4Z`; the first new generator is `w-cv^2`. The identity

```text
w - v^2 = s^8 / \tilde P^2 · (\tilde P - \tilde Q^2),     \tilde P - \tilde Q^2 = s^{8-m}·(unit)
```

with `m=deg_t(P-Q^2)` and `\tilde P(0)=1` gives `ord_s(w-v^2)=16-m`. (Monic leading terms force `m≤7`.) Independently, `δ_2=min{deg(P-φ(Q)): deg φ≤2}`. The choice `φ(y)=ay^2+b y+c` with `a≠1` leaves degree `8`; with `a=1`, subtracting `bQ+c` touches only `t`-degrees `4` and `0`. Thus `δ_2=m` whenever `m≥5`, and `δ_2≤4` whenever `m≤4`. Therefore

```text
δ_2 = 6  ⟺  m = deg(P-Q^2) = 6  ⟺  \bar β_1 = 10.
```

This is an identity, not an analogy. The remaining characteristic data is the genus split `δ_∞=p_a-δ_aff=21-3=18` together with the cluster formula `2δ_∞=(e_0-e_1)β_1+(e_1-e_2)β_2-a+1`, i.e. `36=20+β_2-3`, hence `(4;10,19)`, `\bar β=(4,10,29)`, `Γ_∞=⟨4,10,29⟩`. Gap count: two even gaps `{2,6}` and sixteen odd gaps `{1,3,…,27,31,35}`, total `18` ✓. The semigroup generator `29` is not the exponent `19`; `R84` §1.4 correctly refuses that identification.

**Verdict on (1).** The equivalence is **CONFIRMED**. It uses only the monic `(8,4)` parametrisation, the definition of `δ_2`, and `δ_aff=3`. It does not use ROW-NF, a closed form, or any literature.

## 2. Part A — Theorem A: Phi carries the whole (8,4) row onto the whole (6,4) row

`Φ(x,y)=(x-y^2,y)` is a biregular automorphism of `A^2`, inverse `(x,y)↦(x+y^2,y)`, Jacobian determinant `1`. If `(P,Q)` is an `(8,4)` member in the sense of `R84` §1 (degrees `8,4`, `Δ=(8,4,6,3)`, exactly three ordinary nodes) then `R:=P-Q^2` has degree `6` by §1, and `Φ∘(P,Q)=(R,Q)`. Write `D=im(R,Q)`.

**Why the δ-sequence becomes the sextic row label.** `Φ` identifies `C[P,Q]=C[R,Q]`, so the affine semigroup is unchanged: still `⟨3,4⟩`. The pair `(R,Q)` is a polynomial parametrisation, birational onto `D` because it is `Φ` composed with a birational map, and it has one place at infinity because every polynomial map `A^1→A^2` does. A generic line pulls back with degree `max(6,4)=6`, so `deg \bar D=6`, `p_a=10`, and `δ_∞=10-3=7`. Repeating the chart computation: `ord v=2`, `ord w=6`, unibranch of multiplicity `2`, hence semigroup `⟨2,15⟩` and analytic type `A_{14}`. The AM sequence of `(R,Q)` is then `(6,4,3)` — the unique `ROW-SWEEP` survivor of the `(6,4)` row (`CI` §2). The octic entry `δ_2=6` *is* `deg R`, which becomes the first coordinate degree downstairs. Nothing is inferred by transporting characteristic exponents of the two *infinity* germs: those germs are different, and `R84` §2.3 says so.

**Why nodes are preserved.** `Φ` is an isomorphism of pairs `(A^2,D')≅(A^2,D)`. Analytic type of affine singularities is an invariant of the pair. Ordinary nodes map to ordinary nodes, and there are no extra affine singularities. (Infinity is a compactification-dependent locus and is *not* preserved; that is intended.)

**Why the map is row-onto.** Conversely, if `(R,Q)` is a `(6,4)` member with three ordinary nodes, `P:=R+Q^2` has degree `8` (the square dominates), `P-Q^2=R` has degree `6`, and §1 gives `\bar β_1=10` with the same three nodes, hence `Δ=(8,4,6,3)`. The two three-node classes are inverse images under `Φ^{±1}`.

**What the proof does *not* show, and a false stratum sentence.** The mechanism never uses that the singularities are nodes rather than `D_4` or `A_3+A_1`: whatever affine type `D'` has is copied to `D`. So the same `Φ` is a type-preserving bijection of the whole explicit families, including degenerate moduli. `R84` Theorem A as *written* is only the three-node fragment. Worse, the closed-form commentary (`R84` 227) repeats the original torus-check falsehood “three-ordinary-node stratum `j∉{-27/4,-81/16}`”. `GATE` §2 already replaced that by: three distinct ordinary nodes iff `b≠0` and `j≠-81/16`; `j=-27/4` is still `3A_1`; `j=0` is one ordinary triple point `D_4`. `VER` §1 independently breaks the uniform `3A_1` claim at `(b,c)=(0,1)`. Theorem A’s *mechanism* is not this sentence; the sentence is **REFUTED** and must not be copied into a promotion.

**Onto the campaign rows?** Theorem A is a bijection of the two *numerical* classes as `R84` defined them. That these classes exhaust the coordinator’s `(6,4)` and `(8,4)` nodal survivors still consumes provisional ROW-SWEEP / ROW-NF / FOLD (`CI` §2, `GATE` R1). Lemma FOLD and the closed form `(1.5)` are not used by Theorem B and are not promoted here.

**Verdict on (2).** Mechanism **CONFIRMED** on the three-node numerical classes. The “whole row” slogan is **REPAIR**: it is true for those classes, false as a claim that the three-node stratum equals `j∉{-27/4,-81/16}`, and strictly smaller than the explicit ROW-NF family `c≠0`.

## 3. Part A — Aut(A^2) meridian-preserving pi_1 isomorphism

`Φ` restricts to a biregular isomorphism `C^2 \ D' ≅ C^2 \ D`, hence `Φ_*` is a group isomorphism on `π_1`. A meridian of an irreducible affine curve is the oriented boundary of a small disc transverse to the smooth locus. `dΦ` is invertible (Jacobian `1>0`), so transversality and orientation are preserved, smooth points map to smooth points, and small transverse discs map to small transverse discs. Thus `Φ_*` sends meridians to meridians, not to inverse meridians. The smooth locus of an irreducible curve is connected, so meridians form a single conjugacy class, and `Φ_*` carries that class *onto* the target class.

The `S_4` condition is a property of this pair `(π_1, conjugacy class of meridians)`. It therefore transfers: a transposition-meridional surjection exists on `D'` if and only if one exists on `D`. No braid basis, no line pencil, and no compactification is used. The orientation correction in `GATE` §5 (positive `L_∞`-meridian conjugate to the inverse of the geometric-basis product) is irrelevant here: the objects are affine meridians of the *curve*, and `Φ` does not meet `L_∞`.

**Verdict on (3).** **CONFIRMED.** The meridian-class statement is the standard fact for an orientation-preserving isomorphism of pairs, and the Jacobian check is displayed.

## 4. Part A — inheritance of ROW-KILL at exact scope; adjudication table; TORUS-CHECK trim

`R84` Theorem B: no transposition-meridional `S_4` surjection on any three-node `(8,4)` member, “at the scope of Theorem ROW-KILL”. The proof is Theorem A plus the charged torus-check §8.

**Exact scope, as corrected by `GATE`.** Promote ROW-KILL only for explicit ROW-NF curves with `c≠0` and `j∉{-27/4,-81/16}`, splitting `j≠0` as `3A_1+A_{14}` and `j=0` as `D_4+A_{14}` (`GATE` §10). The value `j=-27/4` is still three ordinary nodes; it was excluded because the *projection* `x=r(t)^2` degenerates, not because the affine type degenerates (`GATE` R2, `VER` §1).

Theorem A therefore sends the three-node `(8,4)` class onto the three-node `(6,4)` class, which **includes** the shear of `D_{-27/4}`. Uncorrected ROW-KILL does not cover that fibre. Theorem B, read as a kill of every three-node `(8,4)` member, is **incomplete** until the `j=-27/4` kill of `EM` is joined. Read as inheriting *exactly* the charged torus-check §8 scope, it kills only those `(8,4)` members whose image has `j∉{-27/4,-81/16}` (and, after `GATE`, includes the `D_4` octic at `j=0`, which Theorem B’s “three ordinary nodes” hypothesis simultaneously excludes). The slogan “exactly ROW-KILL scope and nothing weaker or stronger” is thus **REPAIR**: the written geometric hypothesis (three nodes) and the charged ROW-KILL hypothesis (exclude `j=-27/4`) are not the same set.

**Adjudication table (`R84` §4).** Every “does not transport” line is a compactification- or projection-dependent object: projective degree and germ, `M_∞`, `B_6` vs `B_8` tuples, `γ_∞` in `H_1` (`6g` vs `8g`), the fold `p=r^2`, torus type / `deg Δ_π`. Re-derivation of the fold failure is not needed for Theorem B; Lemma NO-FOLD is a correct optional strengthening on `disc(r)≠0`. The two “does transport” lines — the pair up to `Aut(A^2)`, and `π_1` with its meridian class — are exactly §3.

**Consistency with `GATE`’s trim of the non-transfer note.** `GATE` §9: if “target-equivalent” means an actual `T∈Aut(A^2)`, then `A^2\D ≅ A^2\T(D)` and the transposition-quotient property transfers regardless of degree, pencil, or braid basis; a categorical “does not transfer” cannot be promoted. `R84` takes that fork: Theorem A supplies the automorphism for every three-node member, not merely the ROW-SWEEP witness, and the table refuses to transport the `B_6` tuple. This is consistent, and it is the correct reading of `CI` §2 (“one target-isomorphism class”). What remains non-transferred is INF-TRIVIAL as a statement about a *line* pencil: `Φ` sends vertical lines to parabolas, so `γ_∞^{(8,4)}` is not `γ_∞^{(6,4)}` (`R84` (2.4)–(2.5)). That non-transfer is real and is why the octic projective route stays `OPEN`. It is not an obstruction to Theorem B.

**Verdict on (4).** Table **CONFIRMED**. Inheritance **REPAIR**: Theorem B at charged ROW-KILL scope does not cover the three-node fibre `j=-27/4`; the combined chain of §7 does.

## 5. Part B — EDGE-MODULI: singularity typing at j=-27/4 and j=-81/16

ROW-NF (`EM` from `ZVK:154-163`, not re-proved here): `x=r(t)^2`, `y=q(t)`, `r=t^3+bt+c`, `q=t^4+(2b/3)t^2+(4c/3)t`, `c≠0`, `j=b^3/c^2`. Plus-branch coincidences are the roots of `h(e)=e^3+(4b/3)e-4c/3`, with `p=ts=e^2+b`. The minus branch is empty for `c≠0` (consumed). Discriminants: `disc(r)=0 ⇔ j=-27/4` and `disc(h)=0 ⇔ j=-81/16` are elementary in `j` (`-4b^3-27c^2` and the cubic discriminant of `h`, the latter reducing to `j=-81/16`).

The pair discriminant `(t-s)^2=-3e^2-4b` cannot vanish on `h(e)=0`: `3e^2+4b=0` would make `h(e)=-4c/3≠0`. Every plus solution has two distinct parameters. Image and tangency formulae, re-derived: `t^2=et-(e^2+b)` gives `r(t)=r(s)=-e^3/4` and `q(t)=q(s)=b(e^2+b)/3` after substituting `c=(3/4)e^3+be` from `h=0`. The Wronskian expands, using the same substitution, to

```text
r'(t)q'(s)-r'(s)q'(t) = -(1/3)(t-s)(3e^2+4b)(9e^2+4b).
```

The first two factors are nonzero; coincidence of branch tangents is exactly `9e^2+4b=0`, i.e. `h'(e)=0`. Velocity cannot vanish at a plus preimage: `r=-e^3/4≠0` (`e=0` is `h(0)=-4c/3≠0`), and `r'=0` implies `q'=4c/3≠0`. Both branches of every plus pair are smooth.

**`j=-27/4`.** Write `r=(t-τ)^2(t+2τ)`, `b=-3τ^2`, `c=2τ^3`, `τ≠0`. This is `disc(r)=0`, not `disc(h)=0`. All three `h`-roots are simple, hence three ordinary nodes by the Wronskian. The double root `τ` of `r` is a *smooth* point: `q'(τ)=8τ^3/3≠0`, and locally `x=z^4(3τ+z)^2`, `y-y(τ)=q'(τ)z+O(z^2)`. Projection ramification order four over `x=0`, not a singularity of `D`. The charge’s parenthetical “tacnode stratum” for this modulus is the original torus-check mislabel; `EM` and `GATE` §2 / R2 agree it is still `3A_1`. **Typing CONFIRMED: `Sing_aff=3A_1`.**

**`j=-81/16`.** Here `r` is square-free (`4j+27=27/4≠0`). The cubic `h` has a double root `e_0` with `9e_0^2+4b=0` and `c=(2b/3)e_0`, and a simple root `-2e_0`; `e_0≠0`. Images are distinct: `x=e^6/16` scales by `2^6` between the two roots. The simple root gives an ordinary node. The double root gives two smooth branches with a common tangent.

Infinity is uniform on the whole family: leading terms `x=t^6+…`, `y=t^4+…` give `v=s^2 U`, `w=s^6 V` with `U(0)=V(0)=1`, independently of `(b,c)` (`VER` §1, `GATE` §2). One place, multiplicity `2`, `I=6`, type `A_{14}`, `δ_∞=7`. Arithmetic genus `10` then forces `δ_aff=3` on *every* `c≠0` member, edge moduli included — this is the right derivation, replacing `EM`’s appeal to a ZVK `δ_aff=3` line as an input. Subtracting `δ(A_1)=1` leaves `δ=2` at the tangential double point. Two smooth branches with `δ=I=2` are the ordinary tacnode `A_3` (`A_{2k-1}` with contact `k=2`), not `A_5` (that would need `δ=3` and no leftover node). **Typing CONFIRMED: `Sing_aff=A_3+A_1`.** No affine cusp, no `A_5`, no multiplicity `≥3` point at either edge.

Projective packages: `3A_1+A_{14}` at `j=-27/4` and `A_3+A_1+A_{14}` at `j=-81/16`.

## 6. Part B — modified INF-TRIVIAL relation and Shirane Cor 0.6

**No torus type.** Oka05 pp. 2–3 (fetched): an inner simple point of a `(2,3)`-torus sextic is `A_{3ι-1}` if the cubic is smooth there, or `E_6` if the cubic is singular with `I=2` and the conic reduced; Proposition 2, for torus sextics with only simple singularities, gives `∑_inner ρ(P,5)=6`. `A_1` is not in that list. `A_3` is not: `3ι-1=3` is not integral, and the singular-cubic case is `E_6` only. `D_4` is not (`GATE` §3: an inner torus germ of multiplicity three has cubic cone a triple line, not three distinct lines). All affine singularities at both edges, and at `j=0`, are therefore outer. The only inner-capable point is `A_{14}`, contributing `0` or `5`, never `6`.

This citation is load-bearing at `j=-81/16`. The elementary tangent-cone argument that excludes inner `A_1` does *not* exclude inner `A_3`: a tacnode’s cone is a double line, which is a square, so it is a priori compatible with `G_3,1^2`. Parametric pullback and the conic/Bézout proof likewise fail unless inner `A_3` is already forbidden. `EM`’s use of Oka here is correct and necessary. At `j=-27/4` the type is `3A_1+A_{14}`, so all four NO-TORUS routes of `GATE` §3 apply unchanged.

**Infinity meridian, `j=-81/16`.** `disc(r)≠0`, so three simple folds over `x=0`. The feeds `GATE` §5 actually uses survive: `q'≡-8/3(bt+c) (mod r)` cannot vanish at a root of `r` when `c≠0` and `b≠0`; the `y`-levels `q(τ_i)` are distinct because `q(τ_i)-q(τ_j)=-(τ_i-τ_j)τ_k^3/3` and `r(0)=c≠0`. Geometric basis: `g_1=g_2`, `g_3=g_4`, `g_5=g_6`, product `δ=g_5^2 g_3^2 g_1^2`. Involutions kill it. (Positive `L_∞`-meridian is conjugate to `δ^{-1}`; still killed.)

**Infinity meridian, `j=-27/4`.** Replace `2+2+2` by `4+2`. At the double root `τ`, the local model is `x=az^4+O(z^5)`, `y-y(τ)=bz+O(z^2)` with `ab≠0`. This point is a *smooth* point of `D`, so a small ball complement has `π_1≅Z`, generated by one meridian. A nearby vertical fibre is transverse to `D` at four points (the branch is a graph over `y`), and each local fibre loop is a genuine once-around meridian of that same generator. Transporting along a shared path into a cluster disc gives `g_1=g_2=g_3=g_4` in an adapted geometric basis. The remaining simple root `-2τ` is an ordinary fold: `g_5=g_6`. The two clusters have distinct `y`-levels (`q(τ)=(5/3)τ^4`, `q(-2τ)=(8/3)τ^4`). The large-circle product is `g_5^2 g_1^4` or `g_1^4 g_5^2` according to order along the fibre; either is an even word in involutions, hence `χ(γ_∞)=1`. `EM`’s phrase “the local ZvK relation identifies their four meridians” is the right conclusion, supplied here by the ball-complement argument rather than by analogy with the `n=2` fold. **INF-TRIVIAL at both edges CONFIRMED.**

**Shirane Corollary 0.6.** Fetched PDF, Cor. 0.6 p. 2: a degree-6 divisor `Δ` on `P^2` is `Δ_π` for a normal triple cover iff there exist homogeneous `G_i` with `G_2^3+G_3^2` defining `Δ` plus two local primitivity conditions. The printed “degree `i` for `i=1,2`” is the known typo; the identity names `G_2,G_3` (`GATE` §7, `VER` §0). No genericity, non-cyclic, simple-singularity, or smooth-`X` hypothesis. `A_3+A_1+A_{14}` is in scope. If a transposition-meridional `S_4` surjection exists, the quotient `S_4/V≅S_3` is still onto and still transposition-valued (`GATE` §4). INF-TRIVIAL puts `ψ(γ_∞)=1`, so `ψ` descends to `π_1(P^2\setminus \bar F)`. Generalized Riemann existence plus normality ⇒ Cohen–Macaulay plus miracle flatness over `P^2` produces a normal triple cover with `S_π=\bar F`, `T_π=0`, weighted `Δ_π=\bar F` of degree 6 (`GATE` §7; `EM` cites `TC:434-450` and does not replay the Riemann-existence insertion). Cor. 0.6 then forces torus type, contradicting NO-TORUS. Primitivity is superfluous: already clause (1) contradicts. **Application CONFIRMED**, riding the same descent package as corrected ROW-KILL, including the gate-inserted existence step that `EM` does not rewrite.

## 7. Part B — union of scopes vs ROW-NF with c != 0; ROW-KILL j=0 D_4 split; verification arm

`GATE` §10 promotes ROW-KILL on explicit ROW-NF with `c≠0` and `j∉{-27/4,-81/16}`, with the `j=0` fibre split as `D_4+A_{14}`. `EM` kills the two excluded moduli. The set-theoretic union inside the explicit family is exactly `{c≠0}`, i.e. the whole ROW-NF family.

**`j=0` is not a gap.** `GATE` §2–§5: three plus-pairs collide at `(c^2/9,0)` with three distinct tangents, ordinary triple point `D_4` of `δ=3`; `D_4` cannot be inner in a torus presentation; `disc(r)≠0` so the three disjoint folds over `x=0` survive, and INF-TRIVIAL does not use the false six-value census. `VER` §1 independently computes `F_{(0,1)}` and the cubic cone `(8/81)(2Y^3-9X^3)`; §2.2 kills `A^3-B^2=λF` by leading forms (`F_6=y^6` vs `x^4`) without Lemma 2.2; §4.2 confirms the three disjoint `x=0` half-twists at `(0,1)` even though `|Σ_x|=3` not `6`. `VER`’s leftover `OPEN[STRATUM-J=0]` is conservative relative to its own feeds: the two lemmas ROW-KILL actually consumes at this fibre (inner-`D_4` exclusion and the three folds) are both verified. This review takes the gate’s close, corroborated by `VER`’s HOLDS on those lemmas, and does not keep a typed open at `j=0`.

**Other discriminant collisions are not gaps.** `GATE` §5 records node-value coincidences at `j=-2` and tangency/node meetings at `j=-16/3` and `j=-4±2√3`. None of these changes affine analytic type or the `x=0` folds. INF-TRIVIAL never needed global distinctness of `Σ_x`.

**`c=0` is outside ROW-NF**, not a missing fibre of the family.

**What is *not* closed by the union.** Exhaustiveness of ROW-NF for the campaign `(6,4)` row remains provisional (`GATE` R1, `VER` §7, `CI` §2). `EM` does not prove it. The verification arm did not compute at `j=-27/4` or `j=-81/16`; those fibres are desk-scale in `EM` and in §5–§6 above, not a second-engine numeric check. `FIXED-TUPLE` as the literal frozen node-commutation system is still not the same as a `π_1`-homomorphism (`GATE` §8) and is not killed by this union.

**`(8,4)` side of the union.** `Φ` identifies the explicit families, including degenerate moduli (the mechanism of Theorem A does not use nodality). After `EM`, every explicit `(8,4)` shear `x=r^2+q^2`, `y=q`, `c≠0`, is killed by transport of the `(6,4)` kill. The three-node hole at the shear of `j=-27/4` left by Theorem B alone is filled. Direct octic INF-TRIVIAL and the degree-8 triple-plane classification remain `OPEN` and off the critical path (`R84` §2.4, §3.3).

**Verdict on the union.** Inside explicit ROW-NF, **yes: `c≠0`, no residual modulus**. Against the coordinator’s campaign rows, **no**: ROW-NF exhaustiveness is still provisional, and the literal `FIXED-TUPLE` question is still a different object.

## 8. Combined statement: promotion recommendation and residual provisional inputs

**Promote the following, and no broader formulation.**

Let `r=t^3+bt+c`, `q=t^4+(2b/3)t^2+(4c/3)t` with `c≠0`, and let `j=b^3/c^2` run through all of `C` (including `0`, `-27/4`, `-81/16`). Let `D_{b,c}` be the image of `t↦(r(t)^2,q(t))`, and let `D'_{b,c}` be the image of `t↦(r(t)^2+q(t)^2,q(t))`. Then there is no surjection

```text
π_1(C^2 \ D_{b,c})  ↠  S_4     or     π_1(C^2 \ D'_{b,c})  ↠  S_4
```

sending every curve meridian to a transposition.

Affine types that must appear in the proof, not in a single “three nodes” slogan: `3A_1+A_{14}` for `j∉{0,-81/16}`; `D_4+A_{14}` for `j=0`; `A_3+A_1+A_{14}` for `j=-81/16`; and at `j=-27/4` the projection is `4+2` rather than `2+2+2`, while the affine type remains `3A_1`. The `(8,4)` statement is the `(6,4)` statement transported by `Φ(x,y)=(x-y^2,y)`, which is an orientation-preserving isomorphism of pairs and identifies meridians.

**Do not promote:** “three nodes iff `j∉{-27/4,-81/16}`”; Theorem B as a kill of the whole three-node `(8,4)` class on charged torus-check §8 alone; categorical non-transfer of the complement property; a `FIXED-TUPLE` kill in the frozen literal sense; resolution of `OPEN[PI1S4-(8,4)-INF-TRIVIAL]` or `OPEN[TRIPLE-PLANE-BRANCH-DEGREE-8-ROW-84]`; any statement about rows `(8,6)` or `(9,6)`; an upgrade of ROW-NF / FOLD / ROW-SWEEP from provisional.

**Every provisional or sourced input the combined statement still rides.**

1. **ROW-NF / Theorem FOLD / ROW-SWEEP exhaustiveness** (`CI` §2, `GATE` R1). The kill is unconditional for the displayed parametrisations. That these exhaust every campaign `(6,4)` or `(8,4)` member remains provisional. Numerical identification of the campaign survivors with `Δ=(6,4,3)` and `(4;10,19)` is the same item.

2. **Empty minus-branch for `c≠0`**, consumed from the ROW-NF source that `EM` cites and not re-proved in `EM` or `R84`. Used to know that all affine singularities are plus-pairs. This is load-bearing at the edges: an undetected minus-branch `A_2` would be Oka-inner (`A_{3·1-1}`) and could make the inner `ρ`-sum `5+1=6`.

3. **Shirane Corollary 0.6**, necessary direction, as a published theorem (Sh12, hashed above), including the `i=1,2` typo repaired to degrees `2,3`, and with `T_π` distinguished from the weighted `Δ_π`.

4. **Oka05 inner-simple classification and Proposition 2** (hashed above). Essential at `j=-81/16` for outer `A_3`; used also at `3A_1` and `D_4` as an independent route. Proofs in Oka were not re-verified.

5. **Projective descent package**, including generalized Riemann existence and “finite + normal surface over smooth `P^2` ⇒ flat” (`GATE` §7). `EM` and original torus-check omit the existence step; the combined statement needs it.

6. **Elementary resolvent** `S_4/V≅S_3` carrying transpositions to transpositions (`GATE` §4).

7. **INF-TRIVIAL local models**: three disjoint folds when `disc(r)≠0`, and the ball-complement identification of four meridians when `j=-27/4`. Orientation convention: affine geometric-basis product versus positive `L_∞`-meridian; involution-triviality is insensitive to the inverse.

8. **Theorem A / identity `(1.3)`** for the `(8,4)` half, re-derived in §§1–3 and not provisional as a map of explicit families. Campaign-row exhaustiveness of those families is item 1, not this item.

9. **Inner-point lemma for `D_4`** (`GATE` §3), needed at `j=0`; alternatively `VER` §2.2 leading-form elimination, which does not use Oka.

No `charge_basis` line: no new exit price is asserted. Consuming Shirane and Oka as published theorems is not an exit-price declaration.

## 9. Verdict ledger

| claim | verdict |
|---|---|
| `Δ=(8,4,6,3) ⇔ deg(P-Q^2)=6`; germ `(4;10,19)`, `Γ_∞=⟨4,10,29⟩` | **CONFIRMED** |
| Theorem A mechanism (three-node numerical classes, nodes preserved, row-onto) | **CONFIRMED** |
| Theorem A “whole row” as `j∉{-27/4,-81/16}` three-node stratum | **REFUTED** (false stratum; `j=0` is `D_4`; `j=-27/4` is still `3A_1`) |
| `Φ_*` meridian-class isomorphism | **CONFIRMED** |
| `R84` transport table vs `GATE` Aut-trim | **CONFIRMED** |
| Theorem B as kill of every three-node `(8,4)` member on charged ROW-KILL alone | **REFUTED** (misses shear of `j=-27/4`) |
| `EM` typing `j=-27/4` as `3A_1`, projection `4+2` not a tacnode | **CONFIRMED** |
| `EM` typing `j=-81/16` as `A_3+A_1` | **CONFIRMED** |
| NO-TORUS at both edges (Oka essential for `A_3`) | **CONFIRMED** |
| INF-TRIVIAL at `j=-81/16` (`2+2+2`) and `j=-27/4` (`g_5^2 g_1^4`) | **CONFIRMED** (4-cluster by ball complement) |
| Shirane Cor. 0.6 on both edges | **CONFIRMED** (with gate-inserted Riemann existence) |
| `j=0` `D_4` split of `GATE`, corroborated by `VER` | **CONFIRMED**; `VER`’s `OPEN[STRATUM-J=0]` not kept |
| Union of scopes = explicit ROW-NF, `c≠0`, no modulus gap | **CONFIRMED** |
| Union = campaign `(6,4)`/`(8,4)` rows | **NOT PROMOTED** (ROW-NF exhaustiveness still provisional) |
| Combined `S_4` statement on explicit `D_{b,c}` and `D'_{b,c}`, all `c≠0` | **PROMOTE-AS-CORRECTED** at the dependency list of §8 |
| Literal `FIXED-TUPLE`; octic projective chain; rows `(8,6)`, `(9,6)` | **NOT PROMOTED** |

Headline: both producers are right about the mechanism they actually use and wrong about the three-node stratum they inherited. Joined with the gate’s `j=0` repair, the explicit `(6,4)` and `(8,4)` families are dead for meridian-transposition `S_4` surjections. The N=4 residual cage does not shrink past those two explicit families until ROW-SWEEP is itself promoted.

<!-- BODY-END -->

