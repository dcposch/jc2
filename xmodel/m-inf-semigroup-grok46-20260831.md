# M-INF: last-exponent bound by semigroup gap counts

**Lane.** OPEN[M-INF], integration §3.2.
**Date.** 2026-08-31.
**Agent.** grok-4.6.
**Scope.** Two named pieces from the charged residual report §4 / §6.3:
(1) the embedded-resolution identity used as (4.2);
(2) the last-exponent inequality `beta_h <= 2d + n - 2` for places at infinity of polynomial curves.

**Convention lock (preview).** Characteristic data, semigroup generators, and the last exponent `beta_h` are typed in §1; every later formula uses that lock.

---

## 0. Hash verification, sources, and reading order

Charged inputs were hashed with `shasum -a 256` **before any reading**. Both match the prompt:

```text
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696  pi1s4-close-residual-r2-opus5-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

No mismatch; work proceeded.

**Reading order.** Residual r2 §§1.2, 4.1–4.4, 6.0, 6.3 (the identity (4.2), the reduction of (M-INF) to `β_h ≤ 2d+n-2`, and the gap-count mechanism). Integration §3 item 2 (the two named pieces). Then primary literature, hashed below.

**Primary literature fetched and hashed in this lane.**

```text
f9af327748bbc4f3f4d31934510ec0fcbf3c547dc39f79d61278962cab69cc15
   E. R. García Barroso, A. Płoski, "An approach to plane algebroid branches",
   arXiv:1208.0913v1 (2012); Rev. Mat. Complut. 28 (2015) 227–252.
   442536 bytes. Consumed: §1.1 (n-characteristic sequences, conductor
   formula Prop. 1.5); Theorem 6.4 (Abhyankar–Moh inequality, p. 22 of the
   arXiv text); Corollary 6.5; Theorem 6.6 (embedding-line form).
```

The original Abhyankar–Moh 1975 PDF (Crelle 276, 148–166) was **not obtained** from an official free source (De Gruyter paywall; GDZ/eudml full text not retrieved). The inequality used below is GB-P Theorem 6.4, which attributes the semigroup form to [A-M] and to Kang / Russell; no step cites a page of the 1975 text that I have not seen.

Supporting surveys, not used as a substitute for a missing inequality:

- Barrolleta–García Barroso–Płoski, arXiv:1407.0176, AM semigroups and conductor `c ≤ (n-1)(n-2)`.
- García Barroso–Gwoździewicz–Płoski, arXiv:1407.0514, AM characteristic sequences of coordinate lines.
- García Barroso–et al., arXiv:2209.04232, conductors of AM semigroups.
- Zhang, arXiv:1907.06281, Theorem 2.8 (Enriques–Chisini Euclidean chain for the multiplicity sequence of the standard embedded resolution), citing Enriques–Chisini 1924 and Casas-Alvero, *Singularities of Plane Curves*, CUP 2000, Thm. 5.5.1 / Cor. 5.5.3.
- Galindo–Monserrat, arXiv:0910.02613, Theorem 2.1 (δ-sequence of the semigroup at infinity).

No CAS. No `jc2-lean`, no canonical ledger, no charged file was edited. This report is the only file written.

**Status preview.** Piece 1 (identity (4.2)) is proved, with the requested one-pair and two-pair checks. Piece 2 is **not proved**: the Abhyankar–Moh inequality bounds the last *d*-minimal generator of the local semigroup at infinity, which is not the residual’s transverse last Puiseux exponent `β_h`; the gap-count mechanism is correctly named but does not, on the estimates I can source, cut `β_h` down to `2d+n-2` in general. No explicit countermodel family is exhibited. (M-INF) therefore stays typed OPEN except on the residual’s already-checked small degrees.

## 1. Conventions: Puiseux vs Newton, semigroup, `M_emb`, `beta_h`

**Lock.** All later formulae use this lock. No Newton-pair `(p_i,q_i)` is used as a primary invariant; conversion is recorded only to name the Euclidean input.

**Puiseux / Zariski characteristic of a plane branch** (transverse coordinate). Let `C` be an irreducible plane germ, not smooth. Choose local coordinates `(v,u)` so that `{v=0}` is **transverse** to `C` (equivalently: `C` is not tangent to the `v`-axis). There is a primitive parametrization

```text
v = s^a ,    u = Σ_{k ≥ a} c_k s^k ,     a = mult(C) ≥ 2,
```

with `c_k = 0` for non-characteristic terms as needed. Set `e_0 := a` and, inductively,

```text
β_{i+1} := min{ k : c_k ≠ 0 and e_i does not divide k } ,
e_{i+1} := gcd(e_i, β_{i+1}) ,
```

until `e_h = 1`. The sequence `(β_0, β_1, …, β_h)` with `β_0 := a` is the **Zariski–Puiseux characteristic**. Always `a = β_0 < β_1 < … < β_h` and `e_i > e_{i+1}`. Write `n_i := e_{i-1}/e_i` (`n_i ≥ 2`). This is Zhang’s characteristic sequence `(n; m_1, …, m_g)` with `n = β_0`, `m_i = β_i`, and Casas-Alvero’s characteristic exponents of a Puiseux series whose `v`-axis is non-tangent.

The residual r2 §4.2 uses exactly this: “characteristic exponents of `C` with respect to a transverse coordinate”. So **`β_h` in (4.2) is this last Zariski–Puiseux exponent**, an integer, not a Newton pair and not the last *d*-minimal generator of the semigroup at infinity (that generator is `b_h` in §3).

**Zariski generators of the local semigroup.** The value semigroup of the germ is `G(C) = ⟨ β̄_0, …, β̄_h ⟩` with `β̄_0 = a`, `β̄_1 = β_1`, and `β̄_{i+1} = n_i β̄_i + β_{i+1} − β_i`. It is symmetric of conductor `c = 2δ = Σ_{i=1}^h (n_i−1) β̄_i − a + 1` (GB-P Prop. 1.5(4), classical for plane branches).

**Multiplicity sequence of the standard embedded resolution.** Following Zhang Def. 2.6 / Casas-Alvero: the *standard resolution* of `C` is the shortest sequence of point blow-ups such that the total transform of `C` has normal-crossings support. Equivalently: the strict transform is smooth and meets the total exceptional divisor transversely at a smooth point of that divisor. Let `M_1, …, M_k` be the multiplicities of the strict transform at the successive centres. This is the residual’s cluster for `M_emb(C)`: **`C` alone**, not the pair `(C, L_∞)`. (The pair is residual (4.1): `M_∞ = max(M_emb(C), d)` up to one trailing multiplicity-1 point.)

**Enriques–Chisini (Zhang Thm 2.8; Casas-Alvero Thm 5.5.1).** The multiplicity sequence is the concatenation of the Euclidean algorithms

```text
β_1 = h_{1,0} a + r_{1,1} ,
a   = h_{1,1} r_{1,1} + r_{1,2} ,
…
```

and, for each subsequent pair `i = 2, …, h`,

```text
β_i − β_{i−1} = h_{i,0} r_{i−1, k_{i−1}} + r_{i,1} ,
```

continuing until the last remainder is `1`. In the concatenated sequence, remainder `r_{i,j}` appears `h_{i,j}` times, except that the last remainder of pair `i` is identified with the first of pair `i+1` and appears `h_{i,k_i} + h_{i+1,0}` times. The last remainder of pair `h` is `1` and appears `h_{h, k_h}` times. This **includes** the trailing `1`s of the embedded resolution (the residual’s `m_{r−1}` further multiplicity-1 blow-ups after the strict transform is smooth).

**Euclidean block `M(p,q)`.** For `p, q > 0` write the Euclidean algorithm of `(p,q)` as above and let `M(p,q)` be the corresponding (uncombined) multiplicity list, last remainder `d = gcd(p,q)` appearing with its own last quotient. Then `sum M(p,q) = p + q − gcd(p,q)`: if `q = λ p + r`, `0 ≤ r < p`, the list is `p` repeated `λ` times followed by `M(r,p)` (or just `p` repeated `λ` times if `r = 0`), and the identity follows by induction on `p+q`.

The Enriques–Chisini sequence is the concatenation `M(β_0, β_1) ⌢ M(e_1, β_2−β_1) ⌢ ⋯ ⌢ M(e_{h−1}, β_h − β_{h−1})`, with the adjacent gcd-blocks sequential (not identified twice in the sum: they occupy distinct positions).

**Two semigroups, never conflated.**

1. `G(C)` — local value semigroup of the germ at `Q` (intersection numbers against other germs). Genus `δ_∞`. For a place at infinity of a degree-`d` curve, GB-P takes the **`d`-minimal generating sequence** `(b_0, …, b_g)` of `G(C)`: `b_0 = I(C, L_∞) = d`, `b_1 = min(G \ dℕ) = a` (since `a = d−n < d`), and `G(C) = ⟨ b_0, …, b_g ⟩`. This is a Seidenberg *n*-characteristic sequence in GB-P §1.1 with `n = d`.
2. `S_aff = { deg_t h(p,q) : h ∈ ℂ[X,Y] } ⊆ ℕ` — the affine degree semigroup of a polynomial parametrization `(p,q)` with `deg p = d > n = deg q`. Numerical (gcd `1` by birationality), `S_aff ⊇ ⟨ d, n ⟩`, and `δ_aff = #(ℕ \ S_aff)` (residual (4.3)). This is the Galindo–Monserrat semigroup at infinity, generated by a *δ-sequence* `(δ_0, …, δ_g)` with `δ_0 = d`, `δ_1 = n`.

Genus-0 of the projective closure is `δ_aff + δ_∞ = (d−1)(d−2)/2`. The two semigroups are not equal: for the residual’s rigid `(d,n)=(4,2)` curve one has `G = ⟨2,5⟩` (genus 2) and `S_aff = ⟨2,3⟩` (genus 1).

**Polynomial curve.** Irreducible affine plane curve whose normalisation is `𝔸^1` (equivalently: rational projective closure, one place at infinity). Residual normalisation: unique point `Q = [1:0:0]` of `C̄ ∩ L_∞`, chart `(v,u) = (Y/X, Z/X)`, `s = 1/t`,

```text
v = s^{d−n} · unit ,   u = s^d · unit ,
a := mult_Q(C̄) = d−n ,   b := I(C̄, L_∞; Q) = d .
```

Here `{v=0}` is transverse (`I = a = mult`) and `{u=0}` is `L_∞`. So the residual’s `β_h` is the last Zariski–Puiseux exponent of `u` as a series in `v^{1/a}`.

**What (4.2) is not.** It is not an identity for the pair `(C, L_∞)`. Residual (4.1) compares the two clusters separately. Coprime check: if `gcd(a,d)=1` then `h=1`, `β_h = d`, and `M_emb = a+d−1`, recovering charged Lemma 4.4. If `a=1` the germ is already smooth, `h=0`, and `M_emb = 0` (no characteristic; the formula is for singular germs).

## 2. Piece 1 — the embedded-resolution identity

### 2.1 Statement

> **Theorem (4.2).** Let `C` be a singular irreducible plane germ with Zariski–Puiseux characteristic `(β_0, …, β_h)` in a transverse coordinate, `β_0 = a = mult(C)`. Let `M_emb(C)` be the sum of the multiplicities of the strict transform at the centres of the standard embedded resolution (normal-crossings total transform; §1). Then
>
> ```text
> M_emb(C) = a + β_h − 1 .
> ```

The residual’s recursion `M_emb = Σ_{j < r} m_j + m_{r−1}` (length-`r` non-embedded resolution, then `m_{r−1}` further `1`s) is already proved in residual §4.2; it is the same cluster as Enriques–Chisini’s sequence, which includes those trailing `1`s. What is proved here is the closed evaluation of that sum.

### 2.2 Proof

**Lemma (Euclidean sum).** For integers `p, q > 0`, `sum M(p,q) = p + q − gcd(p,q)`.

*Proof.* Induction on `p+q`. If `q = λ p` then `d = p` and `M(p,q)` is `p` repeated `λ` times, sum `λ p = q = p+q−p`. If `q = λ p + r` with `0 < r < p`, then `M(p,q)` is `p` repeated `λ` times followed by `M(r,p)`, and `gcd(r,p) = gcd(p,q)`, so the sum is `λ p + (r + p − d) = q + p − d`. `[]`

**Lemma (telescoping).** Write `e_0 = β_0 = a`, `e_i = gcd(β_0, …, β_i)`, `e_h = 1`. Then

```text
sum M(β_0, β_1) + sum M(e_1, β_2−β_1) + ⋯ + sum M(e_{h−1}, β_h−β_{h−1})
  = a + β_h − 1 .
```

*Proof.* The Euclidean-sum lemma gives
`sum M(β_0, β_1) = a + β_1 − e_1`,
`sum M(e_{i−1}, β_i − β_{i−1}) = e_{i−1} + (β_i − β_{i−1}) − e_i` for `i ≥ 2`.
The last remainder of the last block is `e_h = 1`. Adding:

```text
(a + β_1 − e_1) + Σ_{i=2}^h ( e_{i−1} + β_i − β_{i−1} − e_i )
  = a + β_h − e_h = a + β_h − 1 .
```

The intermediate `e_i` and `β_i` for `1 ≤ i ≤ h−1` cancel. `[]`

Enriques–Chisini (Zhang Thm 2.8) says the multiplicity sequence of the standard resolution **is** that concatenation. (Adjacent gcd-blocks occupy distinct positions in the concatenated list, so the sums add without a double-count correction; the last block ends with `1` appearing `h_{h,k_h}` times, which are the residual’s extra multiplicity-`1` blow-ups.) Therefore `M_emb(C)` equals the telescoping sum. `[]`

**Remarks.** (i) For `h = 1`, `gcd(a, β_1) = 1`, this is `M_emb = a + β_1 − 1`, the coprime `(a,b)`-cusp (charged Lemma 4.4). (ii) The identity is local to `C` and independent of `L_∞`. (iii) The crude conductor estimate `β_h ≤ 2δ + a − 1` (residual §4.3, from `n_h ≥ 2` and `c = 2δ`) is **not** used.

### 2.3 One-pair checks: `(a,b) = (2,5), (3,4), (4,5)`

Each is a coprime cusp, `h = 1`, `β_h = b`, Euclidean of `(a,b)` plus trailing `1`s.

| germ | Euclidean | multiplicity sequence | `M_emb` | `a+β_h−1` | `2δ = Σ m(m−1)` |
|---|---|---|---|---|---|
| `(2,5)` | `5 = 2·2 + 1`, `2 = 2·1` | `2, 2, 1, 1` | `6` | `2+5−1 = 6` | `2+2 = 4`, `δ = 2 = (2−1)(5−1)/2` |
| `(3,4)` | `4 = 1·3 + 1`, `3 = 3·1` | `3, 1, 1, 1` | `6` | `3+4−1 = 6` | `6`, `δ = 3 = (3−1)(4−1)/2` |
| `(4,5)` | `5 = 1·4 + 1`, `4 = 4·1` | `4, 1, 1, 1, 1` | `8` | `4+5−1 = 8` | `12`, `δ = 6 = (4−1)(5−1)/2` |

Residual table rows `(2,3)` and `(3,7)` are the same pattern (`4` and `9`). Recursion check: after the non-embedded resolution the last multiplicity `≥ 2` is `m_{r−1}`, and one adds `m_{r−1}` ones. For `(2,5)`: two points of multiplicity `2`, then two `1`s. For `(3,4)` and `(4,5)`: the strict transform is already smooth after one blow-up, `I(C_1, E_1) = a`, and one adds `a` ones.

### 2.4 Two-pair checks: `(4;6,7)`-type and `(4;6,9)`-type germs

**`(s^4, s^6+s^7)`.** Characteristic: `β_0 = 4`, `β_1 = 6` (`4 ∤ 6`), `e_1 = 2`; `β_2 = 7` (`2 ∤ 7`), `e_2 = 1`. So `h = 2`.

- `M(4,6)`: `6 = 1·4 + 2`, `4 = 2·2`. List `4, 2, 2`. Sum `8 = 4+6−2`.
- `M(2, 7−6) = M(2,1)`: `2 = 2·1`. List `1, 1`. Sum `2 = 2+1−1`.
- Concatenation `4, 2, 2, 1, 1`. Sum `10 = 4+7−1`.

Blow-up check (cluster algorithm, no CAS). Origin multiplicity `4`, tangent `{u=0}`, `I = 6`. Chart `u = v u_1`: `(s^4, s^2+s^3)`, multiplicity `2`, tangent to `E_1`. Next chart `v = u_1 v_2`: after the coordinate `W = v_2 − u_1` one has `(U, W) = (s^2·unit, s^3·unit)`, a `(2,3)`-cusp, sequence `2, 1, 1`. Total `4, 2, 2, 1, 1`. Semigroup `⟨4, 6, 13⟩` (`β̄_2 = 2·6 + 7 − 6 = 13`). Conductor `2δ = (n_1−1)β̄_1 + (n_2−1)β̄_2 − 4 + 1 = 6 + 13 − 3 = 16`, so `δ = 8`; equivalently `Σ m(m−1)/2 = (4·3 + 2·1 + 2·1)/2 = 8`. Matches residual table.

**`(s^4, s^6+s^9)`.** Characteristic: `β_0 = 4`, `β_1 = 6`, `e_1 = 2`; `β_2 = 9` (`2 ∤ 9`). 

- `M(4,6) = 4, 2, 2` as above.
- `M(2, 9−6) = M(2,3)`: `3 = 1·2 + 1`, `2 = 2·1`. List `2, 1, 1`. Sum `4 = 2+3−1`.
- Concatenation `4, 2, 2, 2, 1, 1`. Sum `12 = 4+9−1`.

Blow-up: same first two steps, then `(U, W) = (s^2·unit, s^5·unit)`, a `(2,5)`-cusp (`2, 2, 1, 1`). Total `4, 2, 2, 2, 1, 1`. Semigroup `⟨4, 6, 15⟩` (`β̄_2 = 2·6 + 9 − 6 = 15`). Conductor `2δ = 6 + 15 − 3 = 18`, so `δ = 9`; equivalently `Σ m(m−1)/2 = (4·3 + 2·1 + 2·1 + 2·1)/2 = 9`. Matches.

(The residual’s extra row `(s^6, s^8+s^9)` is the same algorithm: `M(6,8) = 6, 2, 2, 2`, `M(2,1) = 1, 1`, sum `14 = 6+9−1`.)

**Verdict on piece 1.** Identity (4.2) is proved, not merely checked. The residual’s seven-row table is recovered as instances. The recursion of residual §4.2 is the Enriques–Chisini cluster; the closed form is the telescoping Euclidean sum.

## 3. Piece 2 — the last-exponent bound `beta_h <= 2d + n - 2`

### 3.1 Mechanism named by the charged report

Residual §4.3, given (4.1)–(4.2):

```text
(M-INF)  ⟺  a + β_h − 1 ≤ 3d − 3  ⟺  β_h ≤ 2d + n − 2 ,
```

using `a = d − n`. Piece 1 supplies the left-hand identity. The remaining claim is the scalar inequality on the last transverse Puiseux exponent of the place at infinity of a polynomial curve.

Residual §4.4 names the mechanism, and it is correct as far as it goes:

- `S_aff ⊇ ⟨d, n⟩` and `δ_aff = #(ℕ \ S_aff)` (birationality ⇒ gcd of `S_aff` is `1`);
- genus 0 ⇒ `δ_aff + δ_∞ = (d−1)(d−2)/2`;
- a lower bound on `#(ℕ \ S_aff)` is an upper bound on `δ_∞`;
- the crude local estimate `β_h ≤ 2δ_∞ + a − 1` (from `c(G) = 2δ_∞` and `n_h ≥ 2`) then bounds `β_h`.

This is load-bearing at `(d,n) = (6,4)` (residual §4.4: `S ⊇ ⟨4,6⟩` forces `δ_aff ≥ 5`, hence `β_1 ≤ 11`). It is **not** strong enough at `(8,4)` and `(8,6)` if one only uses `δ_aff ≥ 1` and the crude `β_h`-estimate (residual §6.0). The named missing ingredient is Abhyankar–Moh admissibility of `S_aff` (a *δ*-sequence) and/or of `G(C)` (an AM semigroup of degree `d`).

### 3.2 Abhyankar–Moh characteristic sequence (acquired statement)

The following is GB-P Theorem 6.4, attributed there to Abhyankar–Moh, *J. Reine Angew. Math.* **276** (1975), 148–166, and recorded in the semigroup form used by Kang and Russell. I have not seen the 1975 PDF; I consume GB-P’s statement (hashed `f9af3277`, arXiv text p. 22).

> **Theorem (Abhyankar–Moh inequality).** Let `C` be an affine irreducible curve of degree `n > 1` with one branch at infinity, permissible (`gcd(deg C, mult_O C̄) ≢ 0 (mod char K)`; automatic in characteristic 0). Let `(b_0, …, b_h)` be the *n*-minimal system of generators of the semigroup `Γ_O` of the branch at infinity. Then `e_{h−1} b_h < n^2`, where `e_k = gcd(b_0, …, b_k)`.

In residual coordinates `n` here is `d`, and `b_0 = I(C, L_∞) = d`, `b_1 = min(Γ_O \ {0}) = mult_Q = a` (GB-P proof of 6.4: `b_1 = n'`). So `(b_0, …, b_h)` is a Seidenberg *d*-characteristic sequence in the sense of GB-P §1.1: `e_h = 1`, `n_i := e_{i−1}/e_i > 1`, and `n_{i−1} b_{i−1} < b_i` for `i ≥ 2`. GB-P Corollary 6.5 then gives the conductor bound

```text
c(Γ_O) ≤ (d−1)^2 − (d/gcd(d,a) − 1)(d − a) .
```

The embedding-line theorem (GB-P 6.6 / AM Main Theorem (1.1)) is the special case of a rational curve whose unique singularity is the point at infinity: then `c = (d−1)(d−2)` and one concludes `d − a` divides `d`. That case is **not** the residual: `D_1` is singular in the affine plane (`δ_aff ≥ 1`).

**δ-sequence of `S_aff`** (Galindo–Monserrat Thm 2.1, citing AM and Sathaye–Stenerson). For a one-place-at-infinity curve, `S_aff` is generated by a sequence `(δ_0, …, δ_g)` with `δ_0 = d`, `δ_1 = n` (after ordering `δ_0 > δ_1`), `d_{i} = gcd(δ_0, …, δ_{i−1})`, `n_i = d_i/d_{i+1} > 1`, `d_{g+1} = 1`, `n_i δ_i ∈ ⟨δ_0, …, δ_{i−1}⟩`, and `δ_i < n_{i−1} δ_{i−1}` for `i ≥ 2`.

**What AM does not identify with `β_h`.** The sequence `(b_0, …, b_h)` is the characteristic of the Puiseux series of the *transverse* coordinate as a function of a local equation of `L_∞` (GB-P: `char_x f` with `{x=0} = L_∞`). The residual’s `β_h` is the last characteristic of `u` as a series in `v^{1/a}` (`{v=0}` transverse). These are inverse characteristics in Zariski’s sense; they determine the same `G(C)` but are not termwise equal. For a one-pair germ they satisfy `{a, d} = {b_0, b_1}` and `β_h = d` or `a` according to the axis. For two pairs they diverge: the germ `(s^4, s^6+s^7)` has transverse `β_h = 7` and `d`-minimal sequence `(6, 4, 13)` if one takes the tangent as axis with `I = 6`, last generator `13 ≠ 7`.

### 3.3 The bound is not obtained; no countermodel is exhibited

**Attempt A — crude conductor + AM Cor. 6.5.** From `β_h ≤ 2δ_∞ + a − 1` and `2δ_∞ = c(Γ_O) ≤ (d−1)^2 − (d/g − 1)(d−a)` with `g = gcd(d,a) = gcd(d,n)`, one gets an explicit upper bound. At `(d,n) = (8,6)`: `a = 2`, `g = 2`, `c ≤ 49 − 3·6 = 31`, so `β_h ≤ 31` for a `(2, β)`-germ (where the crude estimate is sharp: `β = 2δ+1`). The requirement is `β_h ≤ 2·8+6−2 = 20`. The AM conductor bound does **not** close the gap. At `(8,4)`: `a = 4`, `g = 4`, Cor. 6.5 gives `c ≤ 49 − (2−1)·4 = 45`, still far from forcing `β_h ≤ 18`.

**Attempt B — `S_aff ⊇ ⟨d,n⟩` plus δ-sequence, minimum genus.** This is the residual’s `(6,4)` argument, and it is valid whenever one can minimise `#(ℕ \ S)` over AM δ-sequences with `δ_0 = d`, `δ_1 = n`. For `(8,6)`: `⟨8,6⟩ = 2⟨4,3⟩`, an odd extra generator `c` is required, and `2c ∈ ⟨8,6⟩` forces `c ∈ ⟨3,4⟩`. The candidate `(8,6,3)` satisfies Galindo’s three axioms (`n_1 = 4`, `n_2 = 2`, `4·6 = 24 ∈ ⟨8⟩`, `2·3 = 6 ∈ ⟨8,6⟩`, `3 < 24`). The semigroup `⟨3,8⟩` has genus `8`, hence `δ_aff ≥ 8`, `δ_∞ ≤ 21−8 = 13`, and for a `(2,β)`-germ `β ≤ 27`, still above `20`. I do **not** claim `(8,6,3)` is realised by a polynomial parametrization with `deg(p,q) = (8,6)`: a degree-`3` value in `S_aff` requires leading-term cancellation in `H(p,q)` that may be incompatible with `deg p = 8 ≠ 6 = deg q`. Without a realisation or a prohibition, this is not a proof and not a countermodel.

**Attempt C — inversion identity `a + β_h = d + b_h`.** True for one pair, false for two (the `(4;6,7)` numbers above). No substitution of `b_h` for `β_h` is licensed.

**Attempt D — Newton polygon of `F(1,v,u)` in the triangle `i+j ≤ d`.** The term `v^d` and `u^a` lie on the Newton polygon, but Tschirnhausen (`u ↦ u − c v^{d/a}` when `a | d`) leaves the degree-`d` triangle, so one cannot bound `β_h` by `d`. No bound.

**No countermodel family.** An explicit polynomial map `(p,q)` of type `(d,n)` with `β_h > 2d+n−2` would refute the claim. The one-parameter perturbations `p = t^d`, `q = t^n + t^k` (`k` odd, `k < n`) for `a = 2` give, after reparametrisation, `β_h = d + n − k` at most `d+n−1` (at `k=1`), and `d+n−1 ≤ 2d+n−2` holds. Cancelling further odd exponents by extra coefficients of `p` and `q` might raise `β_h`; that is a finite interpolation problem, not executed (no CAS), and not an exhibited family. AM existence of a one-place curve with local semigroup `⟨8,2,31⟩` (the sequence `(8,2,31)` satisfies GB-P 6.4: `2·31 = 62 < 64`) produces `β_h = 31 > 20` **if** that curve can be taken rational of type `(d,n)=(8,6)`. Existence of an AM semigroup does not by itself give genus 0 with prescribed `(d,n)`; the complementary `δ_aff = 21−15 = 6` would have to be realised affinely. Not constructed.

Per FALLACY-v2 (no cap, no analogy): the inequality `β_h ≤ 2d+n−2` is **OPEN**. The exact break is the identification of the residual’s transverse `β_h` with an AM-constrained generator, plus a minimum-genus theorem for `S_aff` at given `(d,n)` strong enough to feed the crude (or a sharper) local estimate.

### 3.4 Gap-count / genus-0 accounting (what is proved)

The following are proved, without the missing identification.

1. `δ_aff = #(ℕ \ S_aff)` and `S_aff ⊇ ⟨d,n⟩` (residual (4.3), standard).
2. `δ_aff + δ_∞ = (d−1)(d−2)/2` for a polynomial curve (Noether; residual §1).
3. `c(G(C)) = 2δ_∞`, and `β_h ≤ 2δ_∞ + a − 1` with equality on every `(2, β)`-germ (conductor formula + `n_h ≥ 2`; residual §4.3).
4. AM inequality on `(b_0, …, b_h)` and Cor. 6.5 on `c(Γ_O)`, as quoted in §3.2.
5. The residual’s small-degree verifications that do **not** need a general bound: `(4,2)` is rigid of type `(2,5)`, `β_h = 5 ≤ 8`; `(6,4)` uses (4.3) only, `β_1 ≤ 11 ≤ 14`; coprime stratum `β_h = d ≤ 2d+n−2`. These stand.

What is not proved: a general upper bound `β_h ≤ 2d+n−2`. The first degree at which the sourced estimates fail to conclude is `d = 8` (residual §6.0), and AM as quoted does not repair those two rows.

## 4. Verdict on (M-INF) and the nodal noncoprime closure

**Piece 1: HOLDS.** Identity (4.2) is proved for every singular plane branch, in the Zariski–Puiseux normalisation of §1. The residual’s reduction

```text
(M-INF)  ⟺  β_h ≤ 2d + n − 2
```

is therefore an equivalence, not a one-way implication through an unchecked formula. Coprime and two-pair checks match the residual table; the two-pair Euclidean/cluster computations are independent of that table.

**Piece 2: OPEN.** The inequality `β_h ≤ 2d + n − 2` is not proved for a general place at infinity of a polynomial curve, and is not refuted by an exhibited family. Abhyankar–Moh is acquired (GB-P Thm 6.4) and does constrain `Γ_O`, but it constrains the last *d*-minimal generator, not `β_h`. The gap-count mechanism is correctly named and is sufficient in the residual’s small cases; it is not sufficient, on the sourced conductor estimates, at `d = 8`.

**Consequences for the nodal noncoprime closure.** Residual Theorem B-noncoprime and §5.2 row 4 close the residual **when** `(M-INF)` is verified **and** `D_1` is nodal, via hashed Nori Prop. 3.27. That route fires on every instance where piece 2 is known by a separate check:

- the whole coprime stratum (nodal): `β_h = d`, (M-INF) holds identically, Nori applies (residual §5.2 row 1; integration has promoted this);
- `(d,n) = (4,2)`: rigid `(2,5)`, nodal, two independent kills (braid and Nori);
- `(6,4)` and the other `d ≤ 7` noncoprime rows of residual §6.0, **except** `(6,2)` which used (4.2) as CHECKED — that row is now covered by piece 1, so `(6,2)` nodal is closed on the same footing as the others.

What does **not** fire: a general nodal noncoprime closure at `d ≥ 8`. Integration §3 item 1 remains the highest-leverage gap (`OPEN[PI1S4-D1-DEGREE]`). The present lane does not promote `(M-INF)` and does not declare the nodal noncoprime residual closed in general.

No `charge_basis` line: this report asserts no new exit price.

**FALLACY-v2 checks.** No cv-flag/place/series identification. No `REPRESENTATIVE`/`FULL_ACTUAL_EXIT` confusion. Pole identities unused. Floor/attainment: AM Cor. 6.5 is an upper bound on `c`, not an evaluation of `β_h`; not treated as exact. No `sat()`, no remainder degree, no ring-map claim, no prime-as-derivative. Merge-free/M-descent and target/arrival indices do not arise. Where a step would have required an un-sourced conversion of `b_h` into `β_h`, the claim is typed OPEN.

## 5. OPEN items, failed substitutions, and source list

**OPEN[M-INF-BOUND].** Prove or refute `β_h ≤ 2d+n−2` for places at infinity of polynomial curves. Exact break: convert the transverse last Puiseux exponent into AM-constrained data (`b_h` of `Γ_O`, or the last δ-generator of `S_aff`) by a sourced inversion formula that survives `h ≥ 2`, then minimise `#(ℕ \ S_aff)` over δ-sequences with `(δ_0, δ_1) = (d, n)` strongly enough to feed a local estimate of `β_h`. Alternative: exhibit one polynomial parametrization with `β_h > 2d+n−2`.

**Failed substitutions (not used).** (i) `β_h = b_h`. (ii) `a + β_h = d + b_h` (false at two pairs). (iii) AM Cor. 6.5 as a proof of the residual’s scalar at `d = 8`. (iv) Existence of the AM semigroup `⟨8, 2, 31⟩` as a genus-0 curve of type `(8,6)`. (v) Newton-polygon support in `i+j ≤ d` after Tschirnhausen.

**What this lane does promote.** Identity (4.2), with the convention lock of §1. The residual’s `(6,2)` nodal row, previously leaning on a CHECKED formula, now sits on a proof.

**Sources (consumed).**

| hash / locus | item |
|---|---|
| charged `b9a83b07` | residual r2, §§4, 6.3 |
| charged `bafe5e89` | integration, `OPEN[M-INF]` |
| `f9af327748bbc4f3f4d31934510ec0fcbf3c547dc39f79d61278962cab69cc15` | GB-P arXiv:1208.0913, Thm 6.4, Cor. 6.5, Prop. 1.5 |
| Zhang arXiv:1907.06281 Thm 2.8 | Enriques–Chisini chain (citing EC 1924, Casas-Alvero 2000 Thm 5.5.1) |
| GB-P 1407.0176, 1407.0514; 2209.04232 | AM semigroups, conductors, characteristic sequences |
| Galindo–Monserrat arXiv:0910.02613 Thm 2.1 | δ-sequence of `S_aff` |

**Not consumed.** Abhyankar–Moh 1975 original PDF (no official copy obtained). Orevkov 1990 (carried UNVERIFIED). Nori is not re-used here; nodal closures that need it remain on the residual’s hashed quotation.

**Execution.** Desk-scale only. Euclidean algorithms and two-pair blow-ups by hand. No CAS, no `jc2-lean`, no ledger edits.

**Status line.** Piece 1 proved. Piece 2 OPEN at the conversion `β_h ↔` AM generators / minimum genus of `S_aff`. (M-INF) holds on the coprime stratum and on the residual’s checked noncoprime rows through `d ≤ 7`; the general nodal noncoprime closure does not fire.

<!-- BODY-END -->

