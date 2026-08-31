# HF-DOSSIER: first attainment test at `Delta_aff=6`

**Lane.** Grok 4.6 primary research, round `20260831T1033Z`.
**Target.** Smallest colourable `Delta_aff=6` survivor; conductor-12 census rows `(6,4,9)` and `(9,6,4)`; first candidate only.
**Status.** DONE. First candidate enumerated. Verdict `OPEN`.

## 0. Charge, hashes, and protocol

Frozen-input SHA-256 (computed this lane; all four match the charge):

```text
9f70069c88730b2010cd22a72c276e32f71511715e8e0e7f30116242fad5e3f2  ideation-20260831T1033Z-fable5.md
7bf7502e43a6bdd344b1c177cf3c2e83afd9ca464b7aeab451b96e6db7528b46  ideation-20260831T1033Z-sol56.md
1500eeb24e1a9f4b2d27daeca85f6ed735a962ae2f7d26e8f923f38ea7d1de7a  block-descent-a1-genus-ladder-conductor12-14-18-20-22-28-s4-census-sol56-20260831.md
2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef  ideation-20260831T1033Z-synthesis.md
```

Protocol followed: one complete projective dossier for the first census survivor; candidate-kill only; stop after the first candidate; desk-scale exact arithmetic; no Singular, msolve, CAS, or `jc2-lean`. Citation lists in the submissions were not treated as typed. Primary sources were fetched and hashed at execution (Section 6). No `charge_basis` line: this report asserts no new exit price.

## 1. Frozen interface: what the census actually licences

The census theorem (frozen §0) is scoped to a reduced irreducible affine plane curve `B` in the charged one-place packet, with `normalization(B)=A1` and a transitive `pi1(A2-B) -> S4` sending every positive generic meridian to a transposition. Its frozen interfaces (census §1, displayed as (1.1)) supply, and only supply,

```text
g_3(K_infinity)=Delta_aff(B),
K_infinity is an iterated cable and is prime or trivial,
pi1(S3-K_infinity) ->> pi1(A2-B), preserving meridians.
```

The cited total-delta interface (hash `03865aae...`, census §1) defines `Delta_aff(B)=sum_p delta_p` as a sum over **every affine singular point**, and states that this strictly extends the sole-ordinary-node theorem: affine singularities may be arbitrary provided the sum is controlled. It also records that the normalization is a polynomial parametrization `nu(t)=(p(t),q(t))`, so `K_infinity` is the large-sphere link of that parametrization (Rudolph / Neumann), not a priori the local link of the germ of the projective closure at the point at infinity.

The census classifies **reduced Assi–García-Sánchez delta-sequences** of the embedding at infinity. It does **not** assert:

- a unique affine singular point,
- that every affine singularity is unibranch,
- that the displayed sequence is a local Puiseux semigroup of an affine germ.

Fable’s card A interpolates “sole affine singularity unibranch with semigroup `S_a`”. The merged synthesis forbids that interpolation: the charged-class interface is to be carried verbatim from the census, not by assumption. Carried verbatim, the interface is one place at infinity, `A1` normalization, total affine delta, and an iterated-cable knot at infinity. Flag, place, and series remain distinct: the AG-S sequence is an embedding invariant of the affine curve; the local germ of `C-bar` at `P_infty` is a different singularity; `K_infinity` is the large-sphere link.

## 2. Candidate selection: first conductor-12 survivor

Census conductor-12 display (frozen §4):

```text
C=12:  (5,4), (6,4,9)*72, (7,3), (9,6,4)*72, (10,4,5), (13,2)
```

Survivors: `(6,4,9)` and `(9,6,4)`, each with labelled full-`S4` count 72. First candidate: `(6,4,9)`. The twin row is not touched.

Reduced-sequence checks (Assi–García-Sánchez, arXiv:1407.0490v1, definition before Proposition 13, and Proposition 2). Write `r=(r_0,r_1,r_2)=(6,4,9)`.

```text
d1=r0=6
d2=gcd(6,4)=2
d3=gcd(2,9)=1
e1=d1/d2=3
e2=d2/d3=2
```

Free/telescopic: `e1 r1=12=2*6` lies in `<6>`; `e2 r2=18=3*6` lies in `<6,4>`. Inequality `r1 d1 > r2 d2`: `24>18`. Strict drops `r0>r1>d2>d3`: `6>4>2>1`. Frobenius and conductor, Proposition 2(iv):

```text
F = (e1-1)r1 + (e2-1)r2 - r0 = 2*4 + 1*9 - 6 = 11
C = F+1 = 12
genus of Gamma(f) = C/2 = 6 = Delta_aff.
```

The Abhyankar semigroup is `Gamma=<6,4,9>`. The census braid compiler (frozen §2) reads the same sequence as the cable `K(R)=C_(2,9)(T(2,3))`. Seifert genus: `g(T(2,3))=1` and `g(C_(2,q)(K))=2 g(K)+(2-1)(q-1)/2` gives `2*1+4=6`, matching `g_3(K_infinity)=Delta_aff`.

## 3. Projective degree and `delta_infty` dictionary

Assi–García-Sánchez Proposition 13: a reduced delta-sequence has `rdeg(f)=r_0=deg_y r(f)`. For `(6,4,9)` this is 6. After an affine automorphism that puts the equation in reduced Weierstrass form, the total degree equals the `y`-degree (their reduction arranges this). The projective closure in those coordinates is a degree-`d=6` curve.

Genus split for a rational plane curve:

```text
(d-1)(d-2)/2 = Delta_aff + delta_infty
5*4/2 = 10 = 6 + delta_infty
delta_infty = 4 >= 0.
```

This is the unique reduced-embedding pair attached to the row. Automorphisms of `A2` of unbounded degree can raise the equation degree and change the germ at the new line at infinity; Fable’s claim that the set of `(d, S_infty)` is finite is unproved (synthesis: “no cofinal degree bound exists”). This lane enumerates only the reduced pair `(d, S_infty)=(6, <2,9>)` constructed in Section 5. No row-exhaustion claim.

## 4. Affine singularity records (typed)

**Row-level dictionary (absent).** The census supplies the sum `Delta_aff=6` and the infinity delta-sequence. It does not supply a partition of that sum into records of type `UNIBRANCH_SEMIGROUP`, `TRANSVERSE_NODE`, or `UNLICENSED_MULTIBRANCH`. Polynomial parametrizations of one-place rational curves may ramify (cusps) or fail injectivity (nodes or worse); the charged interface explicitly allows arbitrary affine singularities. The missing dictionary is named:

```text
OPEN dictionary: affine_singularity_records
  domain  = charged census row (6,4,9)
  needed  = finite list of typed records summing in delta to 6
  supplied = only the sum Delta_aff=6
```

**First geometric curve (AG-S associated equation).** To produce one concrete projective curve rather than a slogan, take the Assi–García-Sánchez associated curve of the sequence (their Section 4 construction; prefix `(3,2)` gives `g=y^3-x^2`, then `d_h=2` and the unique theta with `r_2 d_h=18` is `(theta_0,theta_1)=(3,0)`):

```text
f = (y^3 - x^2)^2 - x^3 = y^6 - 2 x^2 y^3 + x^4 - x^3.
```

(Coefficient `c=-1` of the distinguished monomial `x^3` is nonzero, else the sequence is not `(6,4,9)`.) A polynomial parametrization of this curve is

```text
x(t) = (t^3 - 1)^2 ,     y(t) = t^4 - t.
```

Check: `deg x=6`, `deg y=4`, and `(y^3-x^2)^2 = (t^3-1)^6 = x^3`. Derivatives:

```text
x'(t) = 6 t^2 (t^3 - 1)
y'(t) = 4 t^3 - 1.
```

At the three cube roots of unity, `x'=0` and `y'=3 ≠ 0`: the parametrization is an immersion there. All three roots map to `(0,0)`, with velocity `(0,3)`, hence the same tangent line `x=0`. There are no other affine points with `x'=y'=0` (`y'=0` forces `t^3=1/4`, not a root of `x'=0` except possibly `t=0`, where `y'=-1 ≠ 0`). So this curve has **exactly one affine singular point**, a triple point of three smooth branches with a common tangent.

Typed record:

```text
record_0:
  type            = UNLICENSED_MULTIBRANCH
  place           = affine origin of the AG-S associated curve
  branches        = 3, all smooth, common tangent x=0
  local_delta     = 6   (genus split: pa=10, delta_infty=4)
  licensed_variant = none
    BL 2014 / BHL 2017 require every singularity unibranch
    BLZ 2024 Theorem 6.4 licences, among noncuspidal points,
    only links T(2,2n) (A_{2n-1}; the node is n=1, the Hopf link)
    a 3-component coincident-tangent germ is not T(2,2n)
```

This representative is **not** a row-exhaustion and is not `FULL_ACTUAL_EXIT` of the census row. Other AG-S moduli (the lower terms of Section 4 with `fint<18`) may split or change the affine germ. It is used only as the first explicit charged curve of the first survivor sequence.

## 5. Infinity semigroup from the delta-sequence

The Abhyankar semigroup `Gamma=<6,4,9>` (genus 6) is **not** the local value semigroup of `(C-bar, P_infty)` (needed delta 4). Those are different objects: flag / place / series.

Local equation of the projective closure of `f` at infinity. Homogenise

```text
F = Y^6 - 2 X^2 Y^3 Z + X^4 Z^2 - X^3 Z^3.
```

At `Z=0`, `Y^6=0`, unique point `P_infty=[1:0:0]`. Chart `X=1`:

```text
g(Y,Z) = Y^6 - 2 Y^3 Z + Z^2 - Z^3 = (Y^3 - Z)^2 - Z^3.
```

The extra AG-S terms allowed by `fint<18` and `deg_y<3` homogenise to weight `>9` in the weighting `wt(Y)=1`, `wt(Z)=3`, while the distinguished monomial `c X^3 Z^3` is weight 9 and `c ≠ 0` on this row. The Newton face is therefore `(Y^3-Z)^2` with first perturbation `c Z^3` for every reduced `(6,4,9)` equation, not only the associated curve. Puiseux:

```text
(Y^3 - Z)^2 = c Z^3 + (weight > 9)
Z = Y^3 ± sqrt(-c) Y^{9/2} + higher
Y = t^2 ,   Z = t^6 + alpha t^9 + higher,   alpha ≠ 0.
```

One branch. Orders: `v(Y)=2`, `v(Z)=6 ∈ <2>`, `v(Z-Y^3)=9`. Local semigroup `S_infty=<2,9>`. Gaps `{1,3,5,7}`, four gaps, `delta_infty=4`, link `T(2,9)`. Typed record:

```text
record_infty:
  type             = UNIBRANCH_SEMIGROUP
  place            = P_infty of the reduced degree-6 closure
  semigroup        = <2,9>
  conductor        = 8
  delta            = 4
  link             = T(2,9)
  licensed_variant = Borodzik–Livingston 2014, Theorem 5.4 / 6.5
                     (only if every other singularity is also unibranch)
```

The large-sphere knot `K_infinity=C_(2,9)(T(2,3))` is a different knot (genus 6). It is not a singularity of `C-bar`.

## 6. Literature pins (executed, not inherited)

Fetched this lane; SHA-256 of the PDFs:

| Source | Venue (executed) | arXiv PDF SHA-256 |
|---|---|---|
| Assi–García-Sánchez, *On curves with one place at infinity* | arXiv:1407.0490v1 | `05081acd04a51c85d231ff288c8522b83e79d75b28af7f99868c2f5149683bf9` (matches the census pin) |
| Borodzik–Livingston | **Forum Math. Sigma 2 (2014) e28**, DOI 10.1017/fms.2014.28; arXiv:1304.1062 | `9a65787ab3ba6be6ec3c3d5eb71538c79b1e43feeb7c10c8fc52e6186453861a` |
| Borodzik–Hedden–Livingston | Comment. Math. Helv. 92 (2017) 215–256, DOI 10.4171/CMH/411; arXiv:1409.2111 | `9329d9d9aa1fbe770576e711874947dd5349cd26741c3524248cfa0a77bd97e0` |
| Borodzik–Liu–Zemke | Algebr. Geom. Topol. 24 (2024) 4837–4889, DOI 10.2140/agt.2024.24.4837; arXiv:2104.13709v2 | `ac64acd8f728bc9c920f4063fb6e9699ee13d79cb7fd586b11bc31a9edf84803` |
| Fernández de Bobadilla–Luengo–Melle-Hernández–Némethi | Proc. LMS 92 (2006) 99–138; arXiv:math/0410611 | `e5cdd757e96e2b40508c5a975073fd5ff0b1bf3a2559aaf4019c34ee4500ea9b` |

Fable’s “JEMS 2014” for Borodzik–Livingston is false; the journal is Forum of Mathematics, Sigma. Sol’s citation is the correct one.

**BL 2014, Theorem 5.4** (main theorem; rational cuspidal, i.e. every singularity unibranch, geometric genus 0). Let `I_i` be the gap functions of the local semigroups. With infimal convolution `I ⋄ I'(s) = min_m I(m)+I'(s-m)`,

```text
I1 ⋄ ... ⋄ In (j d + 1) = (j-d+1)(j-d+2)/2
for all j in {-1, 0, ..., d-2}.
```

`j=-1` is the genus identity (Remark 5.5); `j=d-2` is `0=0`.

**BL 2014, Theorem 6.5** (semigroup-counting form). `R_i(m) = #{ s in S_i : 0 ≤ s < m }`, same convolution:

```text
R1 ⋄ ... ⋄ Rn (j d + 1) = (j+1)(j+2)/2
for all j in {-1, ..., d-2}.
```

For `n=1` this is the equality case of the FLMN distribution, sampled at the arguments `jd+1`.

**BHL 2017, Theorem 1.** Cuspidal of genus `g` (still every singularity unibranch): for `j=1,...,d-2` and `b=0,...,g`,

```text
0 ≤ R(j d - 2b + 1) - (j+1)(j+2)/2 + b ≤ g,
```

with `R` the infimal convolution of the local counting functions. At `g=0` this collapses to BL 6.5. Our `C-bar` has geometric genus 0, so BHL is not the first applicable variant; it is recorded because the protocol names it. It still requires a cuspidal (unibranch) hypothesis.

**BLZ 2024, Theorem 6.4.** Reduced curve of degree `d` and genus `g`, cuspidal points with counting functions `R_i`, and, apart from those, only singularities whose links are `T(2,2n)` (`A_{2n-1}`; a transverse node is `n=1`). Then a two-sided bound on the infimal convolution `R` in terms of `d`, `g`, `η_+=sum m_n`, `κ_+=sum n m_n`. The paper’s abstract and §6.2 state that the focus is the transverse double point. It does not licence a three-branch coincident-tangent germ.

**FLMN 2006.** Conjecture (`∗_l`): if unibranch germs with `2δ=(d-1)(d-2)` are realised on a degree-`d` rational cuspidal curve, then `c_l ≤ (l+1)(l+2)/2` for `l=0,...,d-3`. For `ν=1` the conjecture is equivalent to equality, equivalently `# (Gamma ∩ I_l) = min{l+1, d}` on the intervals `I_l = ((l-1)d, l d]`. Their Theorem 1 proves the conjecture when `κ-bar(P^2 \ C) ≤ 1`. BL 2014 Theorem 1.1 / 6.5 proves the `n=1` equality (and the multi-cusp convolution equality) unconditionally for rational cuspidal curves, without a Kodaira-dimension hypothesis. FLMN therefore applies to our candidate **only if** the projective curve is cuspidal, which the associated curve is not.

## 7. Genus identity check

For the enumerated pair `(d, S_infty)=(6, <2,9>)` on the associated curve:

```text
(d-1)(d-2)/2 = 10
delta(S_infty) = #gaps(<2,9>) = 4
Delta_aff = 6
10 = 6 + 4.
```

Identity holds. Compact-core identity from the total-delta interface: `g(F_epsilon)=Delta_aff=6=g_3(K_infinity)`. Arithmetic genus of a degree-6 plane curve is 10; geometric genus 0. No gap in the numerical genus split.

This identity does **not** type the affine germ.

## 8. First nontrivial semigroup-counting / correction-term inequality

Licensed first nontrivial equality, once a complete unibranch (or unibranch-plus-nodes) dossier exists: **BL 2014 Theorem 6.5 at `j=1`**

```text
R1 ⋄ ... ⋄ Rn (d+1) = 3.
```

(The cases `j=-1` and, for a single semigroup containing `0`, `j=0` with `R(1)=1`, are tautological relative to the genus formula.)

On the enumerated candidate this equality is **not evaluated**. The affine record is `UNLICENSED_MULTIBRANCH`. BL 2014 and BHL 2017 require every singularity unibranch. BLZ 2024 Theorem 6.4 requires every noncuspidal singularity to be of type `T(2,2n)`. No licensed theorem has a hypothesis matching the associated curve, and the census row does not supply a substitute unibranch partition. Evaluating the convolution on a fictional affine semigroup would fill the missing dictionary by analogy, which the protocol forbids.

## 9. Controls: one pass, one fail

Both controls are on **named rational cuspidal curves / mutated counting functions**, not on the candidate. They check that Theorem 6.5 is being read correctly.

**Pass: the unicuspidal quartic `X^4 + Y^3 Z = 0`.** Unique singular point `[0:0:1]`, type `(3,4)`, semigroup `S=<3,4>={0,3,4,6,7,8,...}`, gaps `{1,2,5}`, `delta=3`. Degree `d=4`, `(d-1)(d-2)/2=3`. Rational unicuspidal, so BL 2014 Theorem 6.5 applies with `n=1`. First nontrivial slot `j=1`:

```text
R(d+1) = R(5) = #({0,3,4,6,...} ∩ [0,5)) = #{0,3,4} = 3
(j+1)(j+2)/2 = 2*3/2 = 3.
```

Equal. (Replay of the remaining slots: `j=0`, `R(1)=#{0}=1`; `j=2=d-2`, `R(9)=#{0,3,4,6,7,8}=6=(3)(4)/2`. All hold.)

**Fail: hand-mutated gap set of the same cardinality.** Replace gaps `{1,2,5}` by `{1,2,4}`, still three gaps, and keep `d=4`. The mutated set `S~={0,3,5,6,7,...}` is not a plane-branch semigroup (Frobenius would be 4, and `4` is a gap while `1=5-4` is also a gap, so it is not symmetric). Theorem 6.5 at `j=1`:

```text
R~(5) = #({0,3,5,...} ∩ [0,5)) = #{0,3} = 2
(j+1)(j+2)/2 = 3
2 ≠ 3.
```

The mutated count fails. (A same-genus mutation that preserves `R(5)`, such as `<2,7>` with gaps `{1,3,5}` and `R(5)=#{0,2,4}=3`, still passes `j=1`; the fail control is the counting-function mutation, not an arbitrary genus-3 semigroup.)

## 10. Verdict

Enumerated pair: `(d, S_infty) = (6, <2,9>)`, first candidate row `(6,4,9)`.

**OPEN**, for two independently named absences, either of which is sufficient:

1. **Missing dictionary `affine_singularity_records`** on the census row. The charged interface does not pin a typed partition of `Delta_aff=6`. Row-level KILLED or PASS_NECESSARY_ONLY is prohibited without that dictionary and without a proved degree cap.
2. **Missing lemma for `UNLICENSED_MULTIBRANCH`.** On the first AG-S associated curve the unique affine germ is a three-smooth-branch coincident-tangent point, which is not in the hypothesis class of BL 2014, BHL 2017, or BLZ 2024 Theorem 6.4.

Not KILLED: no licensed inequality was evaluated on the candidate, so none can have been violated. Not PASS_NECESSARY_ONLY: that tag is reserved for a complete licensed dossier whose counting identity holds, producing an honest construction target. This pair is not such a target.

The twin row `(9,6,4)` is untouched (stop after the first candidate). No exhaustiveness claim on conductor 12.

## 11. Replay-certificate arithmetic

All integers below are elementary; a verifier needs no code.

**(i) Reduced sequence and conductor.**
`r=(6,4,9)`, `d=(6,2,1)`, `e=(3,2)`.
`2*4 + 1*9 - 6 = 11`, conductor `12`, semigroup genus `6`.

**(ii) Cable genus.**
`g(T(2,3))=(2-1)(3-1)/2=1`.
`g(C_(2,9)(T(2,3)))=2*1+(9-1)/2=6`.

**(iii) Degree and split.**
`r_0=6=d`. `(5)(4)/2=10`. `10-6=4=delta_infty`.

**(iv) Local semigroup `<2,9>`.**
Parametrization `(Y,Z)=(t^2, t^6 + alpha t^9)`, `alpha≠0`.
Generators `2` and `9`. Gaps: odds `1,3,5,7` (next odd is `9∈S`). Count `4`.

**(v) Parametrization of the associated affine curve.**
`x=(t^3-1)^2`, `y=t^4-t`.
`x(1)=x(ω)=x(ω^2)=0`, `y(1)=y(ω)=y(ω^2)=0`.
`y'(1)=4-1=3≠0`; likewise at `ω,ω^2`. Three immersions, one point, common tangent.

**(vi) Control pass.**
`S=<3,4>`. Elements `<5`: `0,3,4`. Count `3`. Right-hand side of BL 6.5 at `j=1`, `d=4`: `3`.

**(vii) Control fail.**
Mutated elements `<5`: `0,3`. Count `2≠3`.

## 12. OPEN dictionary (if any)

```text
OPEN affine_singularity_records
  what is missing: a function from the charged row (6,4,9)
                   to a list of records each typed
                   UNIBRANCH_SEMIGROUP | TRANSVERSE_NODE | UNLICENSED_MULTIBRANCH
                   with local semigroups / link types, summing in delta to 6
  why it is missing: census (1.1) and the total-delta interface give only
                     the sum Delta_aff and K_infinity; they do not type
                     the affine germs
  safe replacement: none; a representative AG-S curve is not the row

OPEN lemma_multibranch_HF
  what is missing: a Borodzik–Liu–Zemke-style correction-term statement
                   whose hypotheses include a 3-branch coincident-tangent
                   (or general unlicensed multibranch) affine germ
  why it is missing: BLZ 2024 Theorem 6.4 licences T(2,2n) among
                     noncuspidal singularities and no others
  safe replacement: none

OPEN degree_cap
  what is missing: a theorem bounding projective degree of a charged
                   one-place curve in terms of promoted block invariants
  why it is missing: Fable’s finiteness of (d, S_infty) is unproved
                     (synthesis: no cofinal degree bound)
  consequence: only the reduced pair (6, <2,9>) was enumerated
```

## 13. FALLACY-v2 checklist

- **Flag / place / series.** AG-S sequence = embedding invariant of `B`. `K_infinity` = large-sphere knot. `(C-bar, P_infty)` = local germ, semigroup `<2,9>`. Not identified.
- **Per-ray / exit-set charge.** No exit-price assertion; no `charge_basis` line.
- **Carrier / attainment.** The AG-S associated curve is a representative, not `FULL_ACTUAL_EXIT` of the census row. A pass of a necessary inequality would still not be attainment; here there was no pass.
- **Pole / interior.** No pole identity used.
- **Floor / attainment.** Genus split is an identity, not a floor promoted to equality by omission. The BL equality was not applied to the candidate.
- **`sat()` wrapping.** No ideal computation.
- **Raw remainder degree.** No normal-form remainder.
- **Variable / ring map.** AG-S reduced coordinates declared: monic in `y` of degree `6`, chart `X=1` at `[1:0:0]`. Matching names were not treated as a map.
- **Prime label / derivative.** `x', y'` are ordinary derivatives of the parametrization; no prime-as-label ambiguity.
- **Merge-free / M-descent.** Not used.
- **Target / arrival index.** Census conductor `12` and `Delta_aff=6` kept distinct from the local conductor `8` of `<2,9>`.

No gap was filled by cap or analogy. Typed `OPEN`.

<!-- BODY-END -->
