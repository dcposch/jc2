# NA-SHARPNESS: `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]` at equality

Lane: Grok 4.6. Card II of ideation `20260902T0022Z`, adopted by synthesis.
Method: desk literature + countermodel search. No CAS, no Groebner, no
canonical edit. Stop rule of the charge: one sourced YES, one witness that
strictness is essential, or one named missing hypothesis.

## Verdict in one line

**Typed `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]`**, with one named missing
hypothesis: Nori WLT ampleness `O_U(H)|H` ample, i.e.
`H^2 = C^2 - 2 r(C) > 0` after embedded resolution of the unique infinite
place (equivalently Neumann–Norbury `d > 1`). Nori’s treatment *at infinity
is typed*; the numerical hypothesis of 3.27 is false at equality, and no
sourced replacement covers this vertex class. Not a YES. Not a
strictness-essential witness. Rows `(9,6,4)`, `(6,4)`, `(8,4)` are not
killed.

## 0. Custody

Charged frozen inputs, hashed with `shasum -a 256` **before any reading**;
3/3 match the boxed values:

```text
83319c5e0ddbdb2bfa43b983aae28c57474703205e244cda6e1460942e5809b9  ideation-20260902T0022Z-grok46.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc  block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  rep-96-inner-opus5-20260901.md
```

Primary literature, hashed before consumption:

```text
1b848c19dcaaa016ff8070a7843cfd89db70cbbec3ce13cd9de080074739cc45  nori_ens1983.pdf
        (Numdam ASENS 1983, 4 546 575 bytes; banked N-A packet copy)
7c3ba931d9cf2152a18c2a1b2c0f62c2cddec73e61927751813b449fe4b6d726  refs/orevkov1990_sb65_fundamental_group_complement.pdf
        (Math. USSR Sb. 65 (1990); matches the charge)
9754547840d422d86bfc36a418fb360b970f75709751a08ccb676f9b03b447e8  orevkov_invar.pdf
```

Wait: the Neumann–Norbury hash actually computed in this lane is
`9754547840d422d86bfc36a418fb360b970f75709751a08ccb676f9f03b447e8`
(banked acquisition ledger, `/tmp/jc2-pi1-lit/orevkov_invar.pdf`, arXiv
math/0110286). The line above is the live `shasum` value; it matches the
acquisition ledger of `b0-pi1-acquisition-grok46-20260831.md` §6.

Nori statements below are from the hashed PDF (journal pagination),
cross-checked against the banked N-A packet
(`nori-bc-extension-opus5-20260831.md`, hostile review, verification arm).
Orevkov 1990 is quoted from the hashed IOP scan (journal pp. 267–277).
Campaign documents cited by file and section: the three charged inputs;
`nori-bc-extension-opus5-20260831.md` §§1, 3.3, 3.5, 4.3; fold-reduction
`pi1s4-64-fold-reduction-opus5-20260831.md` §4.2 and its hostile review
§§5–6; `b0-pi1-acquisition-grok46-20260831.md` §§1.3, 2–3. No other
`20260902` lane report was opened.

Firewall: flag ≠ place ≠ cover series; `REPRESENTATIVE` is not
`FULL_ACTUAL_EXIT`; no gap filled by cap or analogy; bitangent-conic
countermodels consumed only as the promoted `T_x` sharpness datum
(`T_x ≠ 0`, two components); the residual `(6,4)` family is not used as a
π₁-countermodel.

## 1. The question, exactly

Promoted Theorem N-A (Nori 3.27 extended to `A_{2k-1}` by blowing up
tangencies, N-A packet §3.3): if every irreducible `C ⊂ D` satisfies the
**strict** inequality

```text
C^2  >  2 r_1(C) + 4 T(C) + T_x(C) ,
```

then `ker(π₁(X-(D∪E)) → π₁(X-E))` is finitely generated abelian with
finite-index centraliser. For irreducible nodal `C` with `T = T_x = 0` this
is Nori 3.27: `C^2 > 2 r(C)`.

Card II asks: for `C` irreducible, nodal, `T = T_x = 0`, with the only
non-nodal point of the original plane curve the resolved place at infinity,
**may the conclusion still hold at equality** `C^2 = 2 r_1`? A sourced YES
would kill `(9,6,4)` by the fold identity `C̃^2 = d^2 - 2 δ_∞ - M_∞`, and
the downstairs `(6,4)` / `(8,4)` rows, with no Box03. A witness that
strictness is essential (same vertex class, nonabelian kernel) would close
the OPEN negative. If Nori at infinity is untyped, return the exact missing
hypothesis.

Do not relax `>` to `≥` by analogy. Do not iterate
`OPEN[NA-AGGREGATE-REDUCIBLE]`.

## 2. Arithmetic of equality (identities, not π₁)

Charged Lemma 4.3, independently re-derived from
`C̃^2 = d^2 - Σ m_i^2`, `2 δ_∞ = Σ m_i(m_i-1)`, `M_∞ = Σ m_i`, and
`δ_aff + δ_∞ = (d-1)(d-2)/2`:

```text
C̃^2 - 2 δ_aff  =  3d - 2 - M_∞ .
```

On this vertex class `δ_aff = r_1` and `T_x = 0`, so

```text
C̃^2 > 2 r_1   ⇔   M_∞ ≤ 3d - 3
```

integrally: the promoted `(M-INF)` gate. Equality is the next integer,

```text
C̃^2 = 2 r_1   ⇔   M_∞ = 3d - 2 .
```

The three residual rows sit exactly here. Numbers from charged REP-96 §1
and fold-reduction §4.2, re-checked as identities:

| type | `d` | `δ_aff` | `M_∞` | `3d-2` | `C̃^2 - 2 r_1` |
|---|---:|---:|---:|---:|---:|
| `(6,4)` | 6 | 3 | 16 | 16 | `0` |
| `(8,4)` | downstairs via `Aut(A^2)` of `(6,4)` |  |  |  | `0` |
| `(9,6,4)` | 9 | 6 | 25 | 25 | `0` |
| `(9,6,2)` | 9 | 4 | 27 | 25 | `-2` |

`(9,6,2)` has deficit 2 and is out of reach of any relaxation of `r_1`.
Upstairs, the fold of `(6,4)` trades deficit 1 for two components each
missing N-A by 3 (`C_i^2 = 3` against `2 r_1 = 6`); that is a route-failure
already closed, not this question.

Adjunction on the infinity-resolved surface `X`, for a rational curve
(geometric genus 0) with `r` nodes, is Neumann–Norbury Lemma 5.4’s
identity

```text
C̃^2 - 2 r(C̃)  =  -K·C̃ - 2  =  d_NN - 1 ,
```

where `d_NN := -K·C̃ - 1` is their splice-diagram number. Equality
`C̃^2 = 2 r` is exactly `d_NN = 1`. This is the same numerical point as
`M_∞ = 3d-2`, written in canonical-class language.

## 3. Nori 3.27 is typed at infinity, and fails only the strict bound

**3.1 What 3.27 actually requires** (journal p. 331, hashed PDF). `X`
smooth projective; `D, E` curves intersecting transversally; `D` nodal;
`C^2 > 2 r(C)` for every irreducible `C ⊂ D`. Then
`N = ker(π₁(X-(D∪E)) → π₁(X-E))` is finitely generated abelian and its
centraliser has finite index. Here `r(C)` is the number of singular points
*of `C` itself* (p. 306).

The proof spends the numerical bound in two places, both load-bearing:

1. **WLT ampleness.** Nori takes `H =` normalisation of `C` and a tubular
   neighbourhood `(U,i,q)` of `h: H → X`. WLT (pp. 305–306) requires
   `O_U(H)|H` ample, i.e. `H^2 > 0`. For nodal `C` the 3.26 computation
   (p. 330) gives `H^2 = B(C) = C^2 - 2 r(C)`. WLT(C) on p. 330 then
   bounds the index by `(Div h)^2 / H^2 = B^2 / (B^2 - 2 r(B))`. At
   equality the denominator **vanishes**.
2. **Lemma 5.1 via Lemma 5.2** (pp. 332–333). The abelianness half of
   3.27 invokes Lemma 5.2 (`φ` unramified off `E`). Lemma 5.1
   *hypothesises* `B` nodal with `B^2 > 2 r(B)`, and its proof uses
   transversality to get `(A.R) = 2 r(B) - 2 r(A)`. At equality this
   gateway is untyped.

Fact 1.4 B (centrality of a meridian in a tubular neighbourhood, p. 310)
needs only: `H` smooth and `q^{-1}(R)` normal-crossings along `H`. That
half **does not use** `H^2 > 0`. Centrality in a neighbourhood is not
centrality in `π₁(X')`, and without WLT one does not even get finite index
of the centraliser.

**3.2 The infinity-resolution is typed.** This is Neumann–Norbury Theorem
2.1 (arXiv math/0110286, hashed), quoting Nori 3.27: let `Σ ⊂ C^2` be
nodal, `X` the blow-up of `P^2` resolving the singularities of `Σ` *at
infinity*, `D = X - C^2`. If each proper transform satisfies
`C̄_i · C̄_i > 2 r(Σ_i)` and meets `D` transversally, then
`π₁(C^2-Σ)` is abelian, because `X-D = C^2` is simply connected, so `N`
is the whole group.

On Card II’s vertex class the resolution hypotheses hold:

- The unique infinite place is unibranch. Embedded resolution produces a
  chain of exceptionals; the proper transform `C̃` meets only the last
  exceptional, transversally, at a smooth point of `C̃`.
- Affine singularities are ordinary nodes, disjoint from the divisor `E`
  at infinity. So `C̃` is nodal, `E ∩ Sing(C̃) = ∅`, and `D ∪ E` is
  normal-crossings along `D - Sing D`.
- `X - E = C^2`.
- `T = T_x = 0` after separation at infinity (irreducible `D`, no
  cross-component tangency).

Nori 3.27 therefore applies *as a typed statement* on this surface. The
numerical hypothesis is `C̃^2 > 2 r_1`, which is false: it is equality.
The configuration is **not** an untyped infinity. The missing piece is
exactly the strict bound.

Nori with `X = P^2`, `D = D̄`, `E = L_∞` is a different, failed typing:
`D̄` is not nodal (the infinite place is a high-contact unibranch
singularity) and `D̄` does not meet `L_∞` transversally. That is why one
resolves. After the resolution, transversality is discharged; ampleness is
not.

**3.3 Nori 6.5 is a different inequality.** Remark 6.6: for a node,
`s = 4` (the printed `s = 2` is the banked erratum E2), so 6.5 needs
`C^2 > 4 r(C)`, and “example 3.19 (C) shows that this is false when
`C^2 = 4 r(C)`”. That is sharpness of the *coarser* bound, at a point
where 3.27’s `C^2 > 2 r` still holds (`4 r > 2 r` for `r > 0`). It is not
a witness for 3.27 at `C^2 = 2 r`, and it is not consumed as one.

## 4. Orevkov 1990 does not fire, and is not a YES

**Theorem A** (p. 267, hashed scan). Let `K ⊂ CP^2` satisfy the
**negativity condition at infinity** (NC, §1) and assume all singularities
lying in `C^2` are nodes. Then to each irreducible component of `K` one
can attach an element of `π₁(C^2-K)` generating the whole group, and
elements of intersecting components commute. For irreducible `K` the group
is therefore cyclic.

**NC** (p. 268). In coordinates `(z,w)`, expand the multivalued function
`F(z) = {w | (z,w) ∈ K}` at infinity as `f_j(z) = g_j(τ(z))`,
`τ = z^{-1/d}`. NC: if `k ≠ l` then `g_k(τ) - g_l(τ)` does not vanish at
`τ = 0` (pole or finite limit). Equivalently: the braid of a sufficiently
large circle is positive.

What NC covers, and what it does not:

- Example 2: the *generic* curve parametrized by two polynomials of given
  degrees satisfies NC. The residual rows are not generic
  (Abhyankar–Moh / fold form, large `β_1`).
- Example 4: NC holds if each infinite singularity is a cusp `u^m = v^n`
  tangent to `L_∞`, or a transverse meeting of smooth branches. This is
  the quasihomogeneous Newton-polygon case (leading terms already
  separate the branches). It does **not** include the high-`β_1`
  residual germs: if it did, Orevkov’s own §6 curve would satisfy NC.
- Example 5: analytically irreducible at infinity, with all
  *characteristic* Puiseux exponents negative. The residual
  `(2;15)` / `(3;23)` germs have a separating exponent that vanishes at
  infinity (`k_* = 2d - a - β_1 < 0`).

**§6 is the residual vertex class, and it fails NC.** Orevkov computes

```text
z = t^4 + 2 t^2 + 2 t + 1 ,
w = 2 t^6 + 6 t^4 + 6 t^3 + 6 t^2 + 6 t + 5
```

and states these are “polynomials of least degrees such that the curve
parametrized by them cannot satisfy the negativity condition at infinity”.
The curve has three nodes; the Puiseux expansion at infinity is
`z = t^{-4}`, `w = 2 t^{-6} + 3 t^2 - t^3 + ⋯`. Leading terms of the
branches `t` and `-t` agree, and their difference is `-2 t^3 + ⋯ → 0` as
`t → 0`. NC fails by the definition on p. 268. Numerically this is a
degree-6 polynomial curve with `δ_aff = 3`, i.e. the `(6,4)` equality
type (`M_∞ = 16 = 3d-2`). Theorem A therefore does **not** apply to Card
II’s configuration.

**Orevkov’s computation and conjecture are not a sourced YES.** He
reports (PDP-11/70, single precision, Puiseux to the 40th term) that
`π₁` of this one curve “turned out to be abelian”, readable from Figure 1
plus Lemma 3.1. On p. 268 he conjectures that Theorem A holds *without*
NC. A conjecture is not a theorem. A numerical experiment on one member
of one moduli space is not a theorem that every irreducible nodal `C` with
`C^2 = 2 r_1` has abelian kernel. FALLACY-v2 (floor/attainment; no gap by
analogy): neither item is consumed as a YES, and neither is a
nonabelian witness.

## 5. Neumann–Norbury uses the same strict bound

Lemma 5.4: for an immersion `Σ = ⊔ Σ_i → C^2`, if
`2 g(Σ_i) - 2 > K · Σ̄_i` on each component, then `π₁(C^2-Σ)` is abelian.
The proof is “a simple application of Nori’s theorem”. For a nodal
rational component (`g = 0`) this is `C̃^2 - 2 r > 0`, i.e.
`d_NN > 1`. Theorem 2 / Theorem 5.2 then need
`d_n ≥ p_1 q_2 ⋯ q_n - 1`, and they record that `d > 1` follows from that
inequality. At Card II equality one has `d_NN = 1`; Lemma 5.4 does not
fire.

Their Figure 3 (degree 6, splice `• —2/3— k/2 —>`): `d_2 = k - 2` wait,
the recursion is `d_1 = p_1+q_1 = 5`, `Δ_2 = k - 2·3·2 = k-12`,
`d_2 = 2·5 + (k-12) = k-2`. For `k = 3`, `d_2 = 1`. They state
explicitly: “when the degree is 6 only `k = 3` is not covered” by Theorem
2. That is the `(6,4)` equality type, excluded from the Nori application
by the same missing hypothesis.

They then write that MAPLE showed, for those degree `< 12` types not
covered by Theorem 2, that each moduli space is connected and the Orevkov
invariant is abelian. For a nodal curve the Orevkov invariant equals
`π₁`. This is a computer claim in a 2001 paper, not reproduced here, not
a proof, and it does not list degree 9. It is not a sourced YES for Card
II, and it does not export onto `(9,6,4)`.

Oka’s Theorem 2.2 in the same paper (`π₁(C^2-Σ) = Z` if `Σ` is a generic
fibre of a polynomial) *does* give abelianness at the `r = 0` equality
`C̃^2 = 0` (Russell bad field generators; Kaliman `C^*` fibres), by a
van Kampen argument that never uses Nori. That vertex class is a smooth
generic fibre, typically several places at infinity, not “only non-nodal
point the resolved infinity place” plus affine nodes. It is not consumed
by analogy.

## 6. Rejected countermodels and rejected YES-routes

| Candidate | Why it is not a Card II witness / not a YES |
|---|---|
| Two bitangent conics (`C_i^2 = 4`, `T_x = 4`, `π₁ ≅ Z * Z/2`) | Promoted sharpness of the **`T_x` coefficient**. Two components, `T_x ≠ 0`. Charge: do not consume beyond that. |
| Zariski sextic `f^2 = g^3` (`B = 36 > 0`, `π₁ ≅ Z/2 * Z/3`) | Unibranch cusps, not nodes. Refutes unrestricted `B(C)>0`, not 3.27 at nodal equality. |
| Nori 6.5 at `C^2 = 4 r` (Ex. 3.19(C)) | Different inequality; 3.27 still holds there. |
| Oka generic fibre, including `C̃^2 = 0` | `r = 0`, wrong places at infinity. |
| Zariski–Oka flex (`G(d,1) ≅ Z`) | Smooth infinite place, consecutive degrees. Residual `a ≥ 2` is singular at infinity. |
| Deligne–Fulton | `D̄ ∪ L_∞` is not nodal for `d ≥ 2` with one place at infinity. |
| Residual `(6,4)` family as nonabelian kernel | Circular: that is the residual question. FALLACY floor/attainment. |
| Orevkov no-NC conjecture; §6 abelian computation; NN MAPLE | Not theorems. Computational abelianness, if trusted, would lean YES, which is the opposite of a strictness-essential witness, and still does not kill `(9,6,4)`. |

No sourced irreducible `C` with `C^2 = 2 r_1`, nodal, `T = T_x = 0`,
resolved infinity place, and nonabelian `π₁(C^2-C)` was found. Absence of
a countermodel is not a proof that the conclusion holds.

## 7. Named missing hypothesis

Nori’s infinity-resolution typing is complete on this configuration
(§3.2). The statement of 3.27 is therefore available, and it does not
conclude, because the numerical hypothesis is false.

**Named missing hypothesis (the unique stop of this lane):**

> **`O_U(H)|H` ample**, for `H` the normalisation of `C̃` in Nori’s
> tubular neighbourhood of 3.27 / WLT. Equivalently
> `H^2 = C̃^2 - 2 r(C̃) > 0`, equivalently Neumann–Norbury `d_NN > 1`,
> equivalently the strict gate `M_∞ ≤ 3d-3`.

At Card II equality this is `H^2 = 0` (`d_NN = 1`, `M_∞ = 3d-2`). Degree
0 on a rational curve is the trivial bundle, never ample. WLT does not
start (Prop. 3.10 of Nori needs the conormal ample to deform `mH`).
WLT(C) divides by zero. Lemma 5.1 is untyped. No sourced theorem
replaces this hypothesis on the vertex class “irreducible, nodal,
`T = T_x = 0`, unique non-nodal point the resolved infinite place”:

- Orevkov Theorem A requires NC, which this germ fails (§4).
- NN Lemma 5.4 / Theorem 2 require the same `d_NN > 1` (§5).
- Oka 2.2 and Zariski–Oka flex are different vertex classes (§6).

Until this hypothesis is supplied by a new theorem, or a nonabelian
witness in class is exhibited, `OPEN[NA-R1-SHARPNESS-IRREDUCIBLE]` stays
OPEN and the three equality rows live. Do not relax N-A.

Secondary, not the stop: the missing hypothesis for the Orevkov route is
**NC at infinity**, which is false here rather than untyped. Naming it
does not create a YES.

## 8. What this lane does not claim

- It does not kill `(9,6,4)`, `(6,4)`, or `(8,4)`.
- It does not assert that `π₁(C^2-D)` is nonabelian on those rows
  (failure of a strict inequality is a floor, not attainment).
- It does not assert that equality ever produces a nonabelian kernel.
- It does not promote Orevkov’s conjecture, the §6 computation, or NN’s
  MAPLE sentence.
- It does not touch `(9,6,2)` (deficit 2) or `OPEN[NA-AGGREGATE-REDUCIBLE]`.
- No new exit price. No `charge_basis` line.

## 9. FALLACY-v2 audit

- **Flag/place/series.** Four objects at `P_∞` kept apart: contact
  `(D̄ · L_∞) = d`, multiplicity `a = d-n`, characteristic numerator
  `β_1`, and `k_* = 2d-a-β_1`. `d_NN` is a canonical-class number on the
  resolved surface, not a cv-flag and not a cover series. The infinite
  place is not identified with a dicritical.
- **Floor/attainment.** `C̃^2 = 2 r_1` is an identity. Failure of
  `C̃^2 > 2 r_1` is not `π₁ ≠ Z`. Orevkov’s abelian computation and NN
  MAPLE are not promoted to attainment of abelianness.
- **Carrier/attainment.** `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`.
  No homomorphism `π₁ ↠ S_4` is produced or denied.
- **Pole/interior.** Characteristic pairs are used only after the vertex
  class (one place, one pair, polynomial curve) is named. No pole identity
  is applied off that class.
- **Per-ray/exit-set.** No exit-price assertion; no `charge_basis`.
- **`sat()` / remainder degree / variable-ring map.** Not in play.
- **Prime label/derivative.** `C̃` is the proper transform; `q'` in
  fold-reduction is a derivative and is not used here.
- **Not filled by cap or analogy.** `≥` is not substituted for `>`.
  Bitangent conics stay at `T_x ≠ 0`. Oka’s `r = 0` equality is not
  transported. Orevkov’s no-NC conjecture is not consumed. NN MAPLE is
  not consumed. Family-3 / Shirane / INF-TRIVIAL are not imported.

## 10. Sources

Charged inputs: hashes in §0, all matching. Banked N-A packet (Nori 3.27
via `nori-bc-extension` §1, Theorem N-A §3.3, N-A-RES §3.5, bitangent
sharpness §4.3) consumed as the promoted inequality and as the `T_x`
negative control. Orevkov 1990 hashed and read (Theorem A, NC, Examples
1–5, §6, the no-NC conjecture). Neumann–Norbury hashed and read (Thm
2.1, Lemma 5.4, Thm 5.2, Figure 3 `k=3`, MAPLE sentence not consumed).
Nori re-checked on the banked Numdam PDF (WLT, 3.26, 3.27, 1.4 B, 5.1,
6.5–6.6). No CAS.

No `charge_basis` line: this report asserts no new exit price.

<!-- BODY-END -->
