# Verification lane: THEOREM EXHAUST — computation arm

**Lane.** Independent computation arm of the paired review of
`row-nf-exhaustiveness-opus5-20260901.md`, with coordinator integration
`block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md`
as secondary charged input.

**Scope.** Desk-scale exact reasoning only. No CAS. No `jc2-lean`.
No edits to charged files or canonical ledgers.

**Date.** 2026-09-01
**Agent.** grok-4.6

## 0. Hash verification of charged inputs

Frozen copies were hashed with `shasum -a 256` **before any was read**. Both reproduce the boxed manifest byte-for-byte. The stop condition did not fire.

```text
30eb230dca026da6d59cbc7dd733cdb4ca63af443d5069ee83f7713b83a357f3
  .../inputs/row-nf-exhaustiveness-opus5-20260901.md
46e08515b12d21780b727c9035872fdb3a9bfb01c4c8ebc74d0efc950b6258fc
  .../inputs/block-descent-a1-rowkill-coordinator-integration-fable5-20260901.md
```

Primary literature was re-fetched on this host and re-hashed:

```text
637acfd15d3d73b47f2ddc75b713063ee6e236ff6fef271417d96d5846d5a4c9
  241372 bytes,  https://arxiv.org/pdf/0910.2613v2
  C. Galindo, F. Monserrat, "The Abhyankar-Moh theorem for plane valuations
  at infinity", arXiv:0910.2613v2.
```

This is the custody value recorded in the charged exhaust report §0 / §8. A parallel HTML rendering (`https://ar5iv.labs.arxiv.org/html/0910.2613v2`) was used only to read Theorem 2.1, Remark 2.1, Definition 2.2, and Proposition 2.1 without OCR; it is not a second byte-source.

**Execution disclosure.** No Groebner basis, no SAT, no job of uncertain duration, no `jc2-lean`. Finite expansions over `Q` of polynomials of degree at most 12 (addition, multiplication, and linear algebra on coefficient vectors) were used as a calculator for the identities in §§1–3; every identity is displayed with its coefficients. No canonical ledger or charged file was edited. One output file only.

**FALLACY-v2 posture.** This report asserts no new exit price and carries no `charge_basis` line. The rules that bite are *floor/attainment* (a gap census is exact because the semigroup is exhibited, not because a lower bound was capped) and *variable/ring map* (every automorphism is written with coordinate images, generator order, coefficient field, and Jacobian).

## 1. Semigroup arithmetic: gaps of ⟨Δ⟩ and affine/∞ defect counts

**Claim under test.** For Δ = (6,4,3) and Δ = (8,4,6,3), the numerical semigroup ⟨Δ⟩ equals ⟨3,4⟩, has exactly three gaps, and the genus split with the cluster identity gives δ_aff = 3 at both rows, with δ_∞ = 7 and 18 respectively.

### 1.1 Gaps of ⟨Δ⟩, by hand

⟨6,4,3⟩ contains 3 and 4, hence contains ⟨3,4⟩. Conversely 6 = 2·3, so ⟨6,4,3⟩ = ⟨3,4⟩. Direct listing: 3,4 ∈ ⟨3,4⟩, then 6=2·3, 7=3+4, and every n ≥ 3 except 5. Explicitly:

```text
  in:  0, 3, 4, 6, 7, 8, 9, …     (Frobenius number 3·4−3−4 = 5)
  out: 1, 2, 5
```

So N \ ⟨3,4⟩ = {1,2,5}, cardinality 3.

⟨8,4,6,3⟩ likewise contains 3 and 4, and 8 = 2·4, 6 = 2·3, so ⟨8,4,6,3⟩ = ⟨3,4⟩ with the same three gaps.

Thus #gaps⟨Δ⟩ = 3 at both rows. Under the identification δ_aff(D) = dim_C C[t]/A_D = #(N \ S_D) of charged (4.1) (birational normalisation, degree-filtration basis), this is δ_aff = 3 **as soon as** S_D = ⟨Δ⟩. That last equality is GM Theorem 2.1, checked as a statement in §4 of this report; the gap count itself does not use GM.

**Cross-check of charged (C1).** The genus-3 numerical semigroups containing {4,6} are exactly three, not one:

| semigroup | gaps | genus |
|---|---|---|
| ⟨3,4⟩ | {1,2,5} | 3 |
| ⟨4,5,6,7⟩ | {1,2,3} | 3 |
| ⟨2,7⟩ | {1,3,5} | 3 |

(The auxiliary ⟨4,6,5⟩ has genus 4; ⟨4,6,7⟩ has genus 5; ⟨4,6⟩ itself is not numerical, gcd 2.) Charged (C1) is **CONFIRMED** as a correction: “δ_aff = 3 at (6,4) forces S_D = ⟨3,4⟩” is false as a semigroup-theoretic sentence and is true for row members only through GM (among the five admissible Δ of charged §2.1, only (6,4,3) has genus 3). The argument of charged §4 Step 2 does **not** use uniqueness: it uses 3,4 ∈ S_D (so S_D ⊇ ⟨3,4⟩) together with #gaps = 3, so a strictly larger semigroup would have fewer gaps.

### 1.2 Admissible axioms, re-run from GM 2.1

Indexing as in GM: d_i = gcd(δ_0,…,δ_{i−1}) (so d_1 = δ_0), n_i = d_i/d_{i+1}.

**(6,4,c).** d_1 = 6, d_2 = gcd(6,4) = 2, n_1 = 3. Axiom (2) at i=1: n_1 δ_1 = 12 ∈ ⟨6⟩. For δ_2 = c, d_3 = gcd(2,c) must be 1 (axiom (1) forbids n_2 = 1), so c is odd and the sequence stops at g=2. Axiom (2) at i=2: 2c ∈ ⟨6,4⟩ = {0,4,6,8,10,…}, which fails only at c=1. Axiom (3): c < n_1 δ_1 = 12. Hence c ∈ {3,5,7,9,11}. No four-term sequence. **CONFIRMED.**

**(8,4,6,3).** d_1=8, d_2=4, d_3=gcd(4,6)=2, d_4=1, n_1=n_2=n_3=2, all >1. Axiom (2): 2·4=8 ∈ ⟨8⟩; 2·6=12 ∈ ⟨8,4⟩; 2·3=6 ∈ ⟨8,4,6⟩. Axiom (3): 8>4, 6 < n_1·4 = 8, 3 < n_2·6 = 12. **CONFIRMED.**

### 1.3 Cluster identity and δ_∞

The Euclidean formula used by the reviewed sweep (and independently the classical plane-branch formula) is

```text
  2 δ_∞ = Σ_i (e_{i−1} − e_i) β_i − a + 1,     e_0 = a = d−n,   e_i = gcd(e_{i−1}, β_i),
```

with β_i the characteristic numerators of the germ at infinity, **not** the maximal-contact values. Conversion Δ → maximal contact is GM Proposition 2.1, dividing case (a | d at both rows): β̄_0 = δ_0−δ_1 and β̄_{i−1} = δ_0²/d_i − δ_i for i>1. Characteristic numerators then satisfy β̄_0 = a, β̄_1 = β_1, and β̄_{i+1} = n_i^{char} β̄_i + β_{i+1} − β_i with n_i^{char} = e_{i−1}/e_i.

**(6,4,3).** a=2. β̄_0=2, β̄_1 = 36/2 − 3 = 15. One pair (2; 15), gcd(2,15)=1. Then 2δ_∞ = (2−1)·15 − 2 + 1 = 14, so δ_∞ = 7. Cluster of ⟨2,15⟩: 15 = 7·2+1 gives (2^7, 1, 1). Cluster formula Σ m(m−1)/2 = 7·1 = 7, matching. p_a = (6−1)(6−2)/2 = 10, hence δ_aff = 10−7 = 3, matching #gaps.

**(8,4,6,3).** a=4. β̄_0=4, β̄_1 = 64/4 − 6 = 10, β̄_2 = 64/2 − 3 = 29. Then n_1^{char} = 4/gcd(4,10) = 2, and 29 = 2·10 + β_2 − 10 ⇒ β_2 = 19. Characteristic (4; 10, 19), e-chain (4,2,1). Then 2δ_∞ = (4−2)·10 + (2−1)·19 − 4 + 1 = 36, so δ_∞ = 18. The listed cluster (4^2, 2^6, 1^2) has Σ m(m−1)/2 = 2·6 + 6·1 = 18 and total multiplicity 8+12+2 = 22 = a+β_h−1, internally consistent with the Euclidean value; p_a = (8−1)(8−2)/2 = 21, hence δ_aff = 21−18 = 3, matching #gaps.

(The Enriques listing of six 2-centres is not re-derived from a blowup tableau in this arm; δ_∞ itself is obtained from GM Prop. 2.1 plus the Euclidean formula, independently of that listing.)

**Verdict, target (1): HOLDS.** Both rows have ⟨Δ⟩ = ⟨3,4⟩, three gaps, δ_aff = 3, and δ_∞ = 7 resp. 18, by two agreeing routes (gaps vs genus split). The uniqueness sentence corrected as (C1) is false and is not used by the exhaust argument.

## 2. Section 4 dimension count: two explicit one-place (6,4) examples

**Claim under test.** For a one-place (6,4) curve with 3 ∈ S_D, the degree filtration of A_D = C[P,Q] has a unique degree-6 basis monomial, namely the square of a degree-3 element, forcing P = α R² + β Q + γ R + ε (charged (4.2)); after the displayed T_1 and the affine normalisation, the image is a D_{b,c} with c ≠ 0. Two examples: a ROW-NF member, and a synthetic (6,4) parametrisation not in obvious fold form.

Map declaration used throughout this section. Coefficient field C (computations in Q). Source ring C[t], target C[x,y], parametrisation ν(t) = (P(t), Q(t)). Automorphisms are written as T(x,y) = (…, …) with Jacobian in C^*.

### 2.1 ROW-NF member: D_{1,1}

```text
  r = t^3 + t + 1,
  q = t^4 + (2/3) t^2 + (4/3) t,
  P = r^2 = t^6 + 2 t^4 + 2 t^3 + t^2 + 2 t + 1,
  Q = q.
```

This is the charged family at (b,c)=(1,1), already in fold form. The identity recorded in the sweep (and inverted here) is a polynomial identity in t:

```text
  (8/27) r  =  P^2 − Q^3 − 2 P Q + (2/3) Q^2 − (16/27) P + (1/9) Q − 1/9.
```

Coefficient-wise the two sides agree in degrees 0 through 12 (all terms of degree ≥ 4 cancel). Equivalently

```text
  r = (27/8) P^2 − (27/8) Q^3 − (27/4) P Q + (9/4) Q^2 − 2 P + (3/8) Q − 3/8.
```

Thus R := r lies in C[P,Q] and deg_t R = 3, so 3 ∈ S_D independently of quoting GM. The monomials R^i Q^j, 0 ≤ j ≤ 2, have pairwise distinct degrees 3i+4j (j is recovered as the residue of the degree mod 3, since 4 ≡ 1 mod 3). Those of degree ≤ 6 are exactly {1, R, Q, R²} (degrees 0, 3, 4, 6). Expanding P in this basis:

```text
  P = 1 · R² + 0 · Q + 0 · R + 0,
```

which is (4.2) with α=1, β=γ=ε=0. The unique degree-6 basis element is R², and it equals P: the fold is the filtration. T_1 is the identity. The cubic is already depressed and monic, q already matches (4.6) with (b,c)=(1,1) and c ≠ 0. Lands on D_{1,1}.

A second integer check, (b,c)=(0,3): r = t^3+3, q = t^4+4t, P=r², and P² − Q³ − 6P − 3 = 8r identically, so again R ∈ C[P,Q] of degree 3 and P = R².

### 2.2 Synthetic member, not in obvious fold form

Start from the integer family member (b,c)=(3,3),

```text
  r_0 = t^3 + 3 t + 3,     q_0 = t^4 + 2 t^2 + 4 t,
```

reparametrise the source by t ↦ t+1 (so the cubic is *not* depressed and q acquires a t³ term), then apply the triangular automorphism T_0^{-1}(x,y) = (2x + 3y + 5, y) of Jacobian 2. The resulting parametrisation, expanded, is

```text
  r = t^3 + 3 t^2 + 6 t + 7,
  q = t^4 + 4 t^3 + 8 t^2 + 12 t + 7,
  P = 2 r^2 + 3 q + 5
    = 2 t^6 + 12 t^5 + 45 t^4 + 112 t^3 + 180 t^2 + 204 t + 124,
  Q = q.
```

P is not a square (it has a degree-4 term from 3q, and lc(P)=2). Q has a t³ term. This is not ROW-NF form.

**Degree-3 element in C[P,Q].** The (3,3)-identity

```text
  r_0 = (1/8) p_0² − (1/8) q_0³ − (3/4) p_0 q_0 + (3/4) q_0² − (1/2) p_0 − (3/8) q_0 − 21/8
```

is a polynomial identity, hence survives the source shift: the same F satisfies F(r², q) = r. Substituting r² = (P − 3Q − 5)/2 (which holds in C[P,Q] by construction of T_0) yields an explicit element

```text
  R = F( (P − 3Q − 5)/2 , Q )  ∈ C[P,Q],     deg_t R = 3,
```

and R equals the shifted cubic t³+3t²+6t+7. So 3 ∈ S_D by exhibition, not by quoting Δ.

**Filtration.** The monomials R^i Q^j for 0 ≤ j ≤ 2 have distinct degrees 3i+4j, as in charged Step 3; those of degree ≤ 6 are {1, R, Q, R²}. Linear algebra on coefficients of degree ≤ 6 gives

```text
  P = 2 R² + 3 Q + 5,
```

i.e. (4.2) with α=2, β=3, γ=0, ε=5. To exercise completing the square, replace R by R_1 := R+1 (still degree 3, still in A_D). Then

```text
  P = 2 R_1² − 4 R_1 + 3 Q + 7.
```

So α=2, β=3, γ=−4, ε=7, α ≠ 0, and the square of the degree-3 element is the unique degree-6 basis monomial, as claimed.

**Step 5, T_1.** R̃ := R_1 + γ/(2α) = R_1 − 1 = R, and ε' = ε − γ²/(4α) = 5. Set

```text
  T_1(x,y) = ( (x − 3 y − 5)/2 , y ),     T_1^{-1}(x,y) = (2x + 3y + 5, y),
  Jac T_1 = 1/2 ∈ C^*.
```

Then T_1 ∘ ν = (R̃², Q) identically (coefficient check through degree 6). Combined with T_0 this is the triangular automorphism predicted by charged Step 5.

**Step 6, normalisation.** R̃ = t³ + 3t² + 6t + 7. The Tschirnhausen shift that kills t² is t ↦ t − a_2/(3a_3) = t−1, recovering (r_0, q_0). (The charged parenthetical “replace t by t+β_0 with β_0 = a_2/(3a_3)” has the wrong sign under the usual reading of substitution; the existence of an affine source change killing t² is unaffected. Recorded as a formula slip, not a break.) Scaling x by a_3^{-2}=1 and y by e_4^{-1}=1, and translating the constant term of q (already 0 after the shift), yields

```text
  r = t^3 + 3 t + 3,     q = t^4 + 2 t^2 + 4 t,
```

which is D_{3,3}: q_3=0, q_2=2b/3=2, q_1=4c/3=4, and c=3 ≠ 0. Lands in the family.

### 2.3 The quartic N, as a coefficient check of Step 8

Charged (4.5) is an algebraic identity in (e_1, b, c, q_3, q_2, q_1), independent of the examples. Substituting e_2 = (e_1²+b)/3 + 2c/(3e_1) into Dq and multiplying by −3 e_1 expands, with no remainder, to

```text
  N(e_1) = −e_1^4 − 2 q_3 e_1^3 + (2b−3 q_2) e_1² + (q_3 b + 4c − 3 q_1) e_1 + 2 c q_3.
```

On the coefficient locus (4.6) this collapses to N ≡ −e_1^4, which has no nonzero root. The three geometric cases of charged Step 8 (t≠s with r(t)≠0; t≠s with r(t)=r(s)=0; t=s at a root of r with q'(τ)=0) are not re-proved here — they are the geometric content of the forward bridge, not a computation — but the quartic they feed is the displayed polynomial.

**Verdict, target (2): HOLDS.** Both examples: the filtration forces (4.2); the square of a constructed degree-3 element of A_D is the unique degree-6 basis monomial; the constructed T_1 is triangular with constant Jacobian; the synthetic curve, which was not in fold form, lands on D_{3,3} after T_1 and the (correctly signed) Tschirnhausen shift. The β_0 sign in charged Step 6 is a local formula slip.

## 3. Section 5: explicit (8,4) member landing on a D_{b,c}

**Claim under test.** An explicit row-(8,4) member with Δ=(8,4,6,3) expands in the charged basis as (5.1) with c_{11}=0 and c_{20}≠0, so δ_2=6; the triangular T_1 of charged Step 5′ lands on a fold, and Steps 6–9 then land on a D_{b,c}.

### 3.1 Direct octic: D'_{3,3}

Take the integer family (b,c)=(3,3) and the charged octic construction P = r² + q², Q = q:

```text
  r = t^3 + 3 t + 3,
  q = t^4 + 2 t^2 + 4 t,
  P = r² + q² = t^8 + 5 t^6 + 8 t^5 + 10 t^4 + 22 t^3 + 25 t^2 + 18 t + 9,
  Q = q,     deg(P,Q) = (8,4).
```

The same identity as in §2.2 puts R := r in C[r², q] = C[P−Q², Q] ⊆ C[P,Q], degree 3. Basis monomials of C[R,Q] of degree ≤ 8, with their degrees:

```text
  1, R, Q, R², R Q, Q²     at     0, 3, 4, 6, 7, 8.
```

Expansion of P in this basis (coefficient match through degree 8):

```text
  P = 1 · Q² + 0 · R Q + 1 · R² + 0 · Q + 0 · R + 0.
```

So c_{02}=1 ≠ 0, **c_{11}=0**, c_{20}=1 ≠ 0. Charged Step 4′ then gives δ_2 = 6 iff c_{11}=0 and c_{20}≠0, and equivalently deg(P − c_{02} Q²) = 6. Directly: P − Q² = r² has degree 6. This is the third proof of ROW-84 on this member.

T_1 of Step 5′ is Φ(x,y) = (x − y², y), Jacobian 1, and T_1 ∘ ν = (r², q), i.e. D_{3,3}. Steps 6–9 are then the already-normal family member, c=3 ≠ 0.

### 3.2 Hidden octic, still Δ-type (8,4,6,3)

Shear further, still triangular:

```text
  P_h = 3 q² + 2 r² + 5 q + 7
      = 3 t^8 + 14 t^6 + 24 t^5 + 29 t^4 + 60 t^3 + 76 t^2 + 56 t + 25,
  Q_h = q.
```

Same basis expansion:

```text
  P_h = 3 Q² + 0 · R Q + 2 R² + 5 Q + 0 · R + 7.
```

Thus c_{02}=3, **c_{11}=0**, c_{20}=2 ≠ 0, c_{01}=5, c_{10}=0, c_{00}=7, so δ_2=6. Completing the square is vacuous (c_{10}=0). Set

```text
  T_1(x,y) = ( (x − 3 y² − 5 y − 7)/2 , y ),
  T_1^{-1}(x,y) = (2x + 3 y² + 5 y + 7, y),     Jac T_1 = 1/2 ∈ C^*.
```

This is (scaling) ∘ (x,y) ↦ (x − 5y − 7, y) ∘ Φ_3, with Φ_λ(x,y)=(x−λ y², y), matching the charged factorisation of T_1. Coefficient check: T_1 ∘ ν = (r², q) identically. Lands on D_{3,3}.

If c_{11} were nonzero the degree-7 monomial R Q would survive every subtraction of a polynomial in Q, giving δ_2=7, off the row. The vanishing that the row's Δ supplies is exactly the vanishing that lets T_1 be a fold.

**Verdict, target (3): HOLDS.** Both (8,4) members expand with c_{11}=0, c_{20}≠0; the constructed T_1 is triangular with constant Jacobian and lands on D_{3,3} directly, without consuming Φ-transport of the kill.

## 4. GM Theorem 2.1: fetch, hash, statement check

**Claim under test.** The charged citation of Galindo–Monserrat Theorem 2.1 (δ-sequence generates S_{C,∞}, axioms (1)–(3)), together with Definition 2.2 and Remark 2.1, matches the primary source at hash `637acfd1…`.

**Fetch.** `https://arxiv.org/pdf/0910.2613v2` downloaded on this host: 241372 bytes, SHA-256

```text
637acfd15d3d73b47f2ddc75b713063ee6e236ff6fef271417d96d5846d5a4c9
```

byte-identical to the charged custody value. Statement below is from the PDF / ar5iv HTML of that version, pp. 2–5.

**Definition 2.2 (semigroup at infinity).** For a curve C with only one place at infinity at p,

```text
  S_{C,∞} := { −ν_{C,p}(h) | h ∈ T },     T = O_C(C \ {p}).
```

This is the charged translation (for a polynomial parametrisation, −ν_{C,p}(h) = deg_t h(P,Q)). **Matches.**

**Theorem 2.1.** Let C be a curve having only one place at infinity and assume that char(k) does not divide gcd(−ν_{C,p}(x), −ν_{C,p}(y)). Then there exists a finite sequence of positive integers Δ = {δ_0, δ_1, …, δ_g} that **generates** the semigroup S_{C,∞} and satisfies:

1. If d_i = gcd(δ_0, δ_1, …, δ_{i−1}) for 1 ≤ i ≤ g+1, and n_i = d_i/d_{i+1} for 1 ≤ i ≤ g, then d_{g+1}=1 and n_i > 1 for 1 ≤ i ≤ g.
2. For 1 ≤ i ≤ g, n_i δ_i belongs to ⟨δ_0, …, δ_{i−1}⟩.
3. δ_0 > δ_1 and δ_i < δ_{i−1} n_{i−1} for i = 2, 3, …, g.

Charged §1 and §2.1 quote generation plus (1)–(3) with this indexing (d_1=δ_0, n_i = d_i/d_{i+1}). The (6,4) and (8,4,6,3) axiom checks in this report §1.2 are exactly those three conditions. Over C the characteristic hypothesis is vacuous. **Matches.**

**Remark 2.1.** The hypotheses of Definition 2.3 on f can be attained by a change of variables, producing an isomorphic curve C′ with S_{C′,∞} = S_{C,∞}; the generators in Theorem 2.1 are the approximate-root values of C′; δ_0 = deg(C′). Charged §6 item 1 cites this caveat and the equality of semigroups. **Matches.** The charged report's further restriction “only Δ ⊆ S_D is used; S_D ⊆ ⟨Δ⟩ is never invoked” is a consumption choice, not a misquote: each δ_i is a value by Definition 2.3, so Δ ⊆ S_D holds for the AM sequence of a row member even before generation is used. Generation is what identifies S_D with ⟨Δ⟩ when that is invoked (the cross-check ⟨6,4,3⟩=⟨3,4⟩, and the (8,4) analogue).

**Proposition 2.1 (consumed for the cluster conversion in this arm, not re-derived).** Dividing case ν(u) | ν(v): s = g+1, β̄_0 = δ_0−δ_1, and β̄_{i−1} = (δ_0)²/d_i − δ_i for 1 < i ≤ g+1. This is the conversion used in §1.3. Charged exhaust §8 says “Proposition 2.1 not re-derived; the cluster conversions are taken from SWEEP/SWREV”; this arm used Prop. 2.1 plus the Euclidean δ-formula, not the Enriques tableau.

**What the theorem is not.** It does not by itself force S_D = ⟨3,4⟩ among all genus-3 oversemigroups of ⟨4,6⟩; that uses the specific Δ. It does not supply nodality. The converse (every δ-sequence is realised by some one-place curve) is stated in the paper's introduction and is **not** consumed by EXHAUST.

**Verdict, target (4): HOLDS.** Hash matches; Definition 2.2, Theorem 2.1 (1)–(3) with generation, and Remark 2.1 match the charged quotation.

## 5. Transport composition on an explicit triangular automorphism

**Claim under test.** Charged §3: if T ∈ Aut(A²) carries D_1 onto D_{b,c}, then a hypothetical surjection Ψ: π_1(C² \ D_1) ↠ S_4 sending meridians of D_1 to transpositions pushes to a surjection π_1(C² \ D_{b,c}) ↠ S_4 sending meridians of D_{b,c} to transpositions.

### 5.1 An explicit T, with the ring map declared

Work over C, coordinates (x,y) in that order. Set

```text
  T(x,y)  = ( x − y² + 3 y + 1 ,  2 y − 5 ),
  dT      = [ 1 , −2y+3 ]
            [ 0 ,  2     ],     det dT = 2 ∈ C^*.
```

Inverse, polynomial:

```text
  y = (Y + 5)/2,
  x = X − 3 y − 1 + y²
    = X − 3(Y+5)/2 − 1 + ((Y+5)/2)².
```

So T ∈ Aut(A²), triangular of Jung type (affine in y, polynomial in y added to x). This is strictly more than the shear Φ(x,y)=(x−y²,y) of the charged families: it has a y-scaling and a translation. Image check: T is dominant (Jacobian nowhere zero) and has a polynomial inverse, hence bijective on A².

Let D_1 be any irreducible affine curve, D' := T(D_1). Then T restricts to a biregular isomorphism C² \ D_1 → C² \ D', because it is biregular on A² and carries the closed set D_1 onto D'.

### 5.2 Meridians, on this T

A meridian of an irreducible affine curve D at a smooth point p is the class in π_1(C² \ D, *) of the positively oriented boundary of a small complex disc Δ transverse to D at p. Here “positive” means the complex orientation of Δ.

T is holomorphic with dT invertible at every point, in particular at every smooth point of D_1. C-linear automorphisms of C² send complex lines to complex lines and preserve the complex orientation of every complex 1-disc (the induced real map on a complex line has Jacobian |λ|² > 0 for the C-multiplier λ ≠ 0). Thus T(Δ) is a small complex disc transverse to D' at T(p), with the same complex orientation. Smooth points go to smooth points (dT invertible, and the tangent line to D_1 is sent to the tangent line to D'). Therefore T_* sends meridians of D_1 to meridians of D', not to inverse meridians.

Both curves being irreducible with connected smooth locus, meridians form a single conjugacy class, and T_* carries that class onto the target class. Base-point change is inner, and “image is a transposition” is conjugation-invariant in S_4.

### 5.3 The pushed representation

Suppose Ψ: π_1(C² \ D_1, *) ↠ S_4 exists and sends every meridian of D_1 to a transposition. Define

```text
  Ψ'  :=  Ψ ∘ (T_*)^{-1}  :  π_1(C² \ D', T(*)) ↠ S_4.
```

Surjective because T_* is an isomorphism and Ψ is surjective. For a meridian m' of D', the class (T_*)^{-1}(m') is a meridian of D_1 (by §5.2, inverted), hence Ψ of it is a transposition, hence Ψ'(m') is a transposition.

Specialising to D' = D_{b,c} with c ≠ 0 (the landing of §§2–3), this is exactly the object forbidden by the promoted row-kill (charged coordinator §1) for every c ≠ 0. Hence no such Ψ exists on D_1.

The argument consumes only the pair (A², D) up to isomorphism and the meridian conjugacy class. It does not consume projective degree, the germ at infinity, β_1, M_∞, a braid basis, or γ_∞ — the charged list of non-transporting data. Direction: a non-existence statement is pulled back, so nothing about D_1's infinity data needs to be re-established.

**Negative control.** If T were antiholomorphic, meridians would go to inverse meridians, and a transposition-valued representation would still push (transpositions equal their inverses in S_4). That accident is not used: the T written here is holomorphic. If the target group were such that meridians and inverse meridians were distinguished, holomorphicity would be load-bearing; it is, and it holds.

**Verdict, target (5): HOLDS.** The explicit T is in Aut(A²) with constant nonzero Jacobian; meridians go to meridians with orientation; a hypothetical transposition-valued S_4 quotient on D_1 pushes to one on T(D_1).

## 6. Verdict table

| # | Target | Verdict | What was actually checked |
|---|---|---|---|
| 1 | Semigroup arithmetic: ⟨Δ⟩, gaps, δ_aff=3, δ_∞=7/18 | **HOLDS** | ⟨6,4,3⟩=⟨8,4,6,3⟩=⟨3,4⟩, gaps {1,2,5}; GM axioms re-run; Euclidean δ_∞ from Prop. 2.1; genus split agrees. (C1) uniqueness is false and unused. |
| 2 | §4 filtration at two (6,4) examples | **HOLDS** | D_{1,1}: identity puts R∈C[P,Q], P=R². Synthetic (shifted, sheared, not a square): explicit R∈C[P,Q] of degree 3, (4.2) with γ≠0 after R↦R+1, T_1 triangular, lands on D_{3,3}. N(e_1) expands as displayed. Sign slip in β_0, not load-bearing. |
| 3 | §5 (8,4) direct landing | **HOLDS** | D'_{3,3} and a hidden octic both expand with c_{11}=0, c_{20}≠0; T_1 lands on D_{3,3}. ROW-84 on these members is the vanishing of c_{11}. |
| 4 | GM Thm 2.1, hash `637acfd1…` | **HOLDS** | 241372 bytes, hash match; Def. 2.2, Thm 2.1 (1)–(3) with generation, Remark 2.1 match the charged quotation. |
| 5 | Transport through an explicit T | **HOLDS** | T(x,y)=(x−y²+3y+1, 2y−5), Jac=2; meridians → meridians; hypothetical transposition S_4 quotient pushes. |

No target is BROKEN. No target is UNTESTABLE. The single formula slip (Tschirnhausen sign in charged Step 6) does not change any verdict.

This arm does **not** re-prove the three geometric cases of charged Step 8, does **not** re-derive the Enriques tableau giving six 2-centres, and does **not** promote THEOREM EXHAUST (different-model hostile gate still required, as the charged report itself types PROVED-HERE / REVIEW-PENDING). Those are out of the computation charge.

## 7. Notes, OPEN items, and FALLACY-v2 flags

**Formula slip, not a break.** Charged §4 Step 6 writes “replace t by t+β_0 with β_0 = a_2/(3 a_3)” to kill the t² term of R̃ = a_3 t³ + a_2 t² + ⋯. Under the usual reading (substitute t ↦ t+β_0) the t² coefficient becomes 3 a_3 β_0 + a_2, so the working value is β_0 = −a_2/(3 a_3). On the synthetic cubic t³+3t²+6t+7 the charged sign inflates t²; the opposite sign recovers the family. Existence of an affine source change killing t² is true either way.

**What this arm did not test.** (i) The three geometric cases of the forward bridge (charged Step 8: minus pair with r≠0, both roots of r, and t=s at a critical point of q) — those are geometry, not a coefficient identity; N(e_1) as a polynomial was checked, the implication “δ_aff=3 ⇒ N≡−e_1⁴” was not re-proved. (ii) Birationality of a generic (6,4) map, beyond the family identity r ∈ C[r²,q] and the c=0 even/odd factorisation. (iii) The Enriques blowup sequence (4², 2⁶, 1²) as a tableau; δ_∞=18 was obtained from GM Prop. 2.1 plus the Euclidean formula, with the listed cluster only as a δ- and M-consistent check.

**FALLACY-v2.** No new exit-price assertion, so no `charge_basis` line (and the charge forbade one). Floor/attainment: #gaps = 3 is an exact listing of {1,2,5}, not a lower bound capped at 3. Variable/ring map: every T is declared with images, Jacobian, and an image check; matching degree pairs were never used as identifications. Pole/interior: the infinity germ was used only after a = d−n and the GM dividing-case hypothesis a | d were checked at both rows. Carrier/attainment: the two explicit members are representatives, not a proof that every row member is attained; the computation arm tests the algorithm on witnesses, not the universal quantifier of THEOREM EXHAUST. Prime labels: q' in Step 8 is an actual derivative of the polynomial q; no ambiguous prime marks were copied.

**OPEN, typed.** The computation arm has nothing to type OPEN on the five charged targets. Residual obligations of the exhaust report that this arm was not asked to touch remain as the producer left them: different-model hostile review of Steps 1–4, Step 8, and Step 4′ before promotion; the six (8,6)/(9,6) types; nodality of those types.

**Sources.** Charged frozen inputs, hashes in §0. Primary: Galindo–Monserrat arXiv:0910.2613v2, hash `637acfd1…`, Def. 2.2, Thm 2.1, Rem. 2.1, Prop. 2.1. Classical facts used without a hashed citation: p_a=(d−1)(d−2)/2; δ=Σ m(m−1)/2 on a cluster; Aut(A²) over C has constant nonzero Jacobian; Tschirnhausen for a cubic; power-sum divided differences.

<!-- BODY-END -->

