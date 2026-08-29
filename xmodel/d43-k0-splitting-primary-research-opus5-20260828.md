# D43 coefficient algebra `K0`: exact splitting, primary research

**UTC:** 2026-08-28
**Role:** Opus 5, primary research (independent; not a review of the charged reports)
**Verdict:** **`K0` IS A FIELD.** It is a *number field of degree exactly 432*,
Galois but **not** abelian over `Q`, equal to

```text
K0  =  Q(zeta_168, cbrt(3+sqrt3), cbrt(3-sqrt3))
    =  Q(zeta_168, cbrt(6), cbrt(2+sqrt3)).
```

There is **one** factor, hence exactly two idempotents, `0` and `1`. The
degree-48 base generated before `A1,A2` is **cyclotomic and is exactly
`Q(zeta_168)`** — the cyclotomic description is *verified*, with explicit maps
in both directions. The two Kummer cubic classes are **independent** in
`B^*/(B^*)^3`: they span a full `(Z/3)^2`, so no relation of any kind exists
among them. `K0` is finite etale over `Z[1/42]`; the ramified rational primes
are **exactly `{2,3,7}`** (`5` is unramified). Both registered frames map to
the unique factor, and both primes split completely: each carries exactly
**432** frames, which was computed and matches.

Bonus theorem, obtained on the way and directly load-bearing for Rail E:
**the E-relation fourth-root ratio is `K0`-rational.** `W1/W2` needs no field
extension at all; the four branches are `q0 * i^k` with an explicit four-term
`q0 ∈ K0`, and both banked modular points sit on one of those four branches.

No AWS, no web, no `jc2-lean`, no heavy computation. Everything reported as
executed below ran in seconds of stdlib Python on the local host. No
repository object other than this report was written.

---

## 0. Custody

Charged inputs, read completely, as they exist on this host now:

| file | SHA-256 |
|---|---|
| `xmodel/d43-seven-w-elimination-algorithm-grok46-20260828.md` | `8b748f388c53868ccfe856135db2f4251a066db01115641d299f08939f3dcc26` |
| `xmodel/d43-a00pp-tail-elimination-independent-audit-gpt56-r1-20260828.md` | `e19a3d0eaad79ea47fc08fb7c406a9045818671776b535950a285c9813f7f0f8` |
| `xmodel/d43-direct-exact-sparse-source-preflight-gpt56-20260828-v2.md` | `e7000a748782e579f2108a8aa913684765d82bba8639613b6f6e4864e6fb2202` |
| `cases/d43_exact_sparse_rows_v2_20260828/selected_rows_v2.py` | `9fc9bd7a365827ddba2c1ba45cbb34870d6f2d71c9d3eecb6b242d46e00990b2` |
| `cases/d43_common_integral_emitter.py` | `5420b5c0b4164c719e98316cade96c094c2945a6fed8bad3ac0926771855984d` |

The emitter hash matches the one both charged reports pin, so the algebra I
analyse is the algebra they analyse. Ancillary reads (pointbanks) are hashed in
§7.

The object of study is the literal `COEFFICIENT_ALGEBRA` block of
`cases/d43_exact_sparse_rows_v2_20260828/selected_rows_v2.py:59-72`
(`basis_generators`, `basis_shape [12,2,3,3,2]`, `basis_rank 432`,
`field_claim: null`), realised by `RadicalCoefficient` in
`cases/d43_common_integral_emitter.py:73-232`:

```text
K0 = Q[zeta42, r3, A1, A2, h] /
     (Phi42(zeta42), r3^2-3, A1^3-(3+r3), A2^3-(3-r3), 2h^2-3).
```

Throughout write

```text
alpha1 = 3 + r3,  alpha2 = 3 - r3,  eps = 2 + r3,
B      = Q[zeta42, r3, h]/(Phi42, r3^2-3, 2h^2-3)      (the pre-cubic base)
u      = A2/A1,   i = r3*(1 + 2*zeta42^14)/3.
```

---

## 1. Results, with claim type attached to each

| # | statement | type |
|---|---|---|
| L1 | `K0` is **free** of rank 432 over `Q` on the displayed monomial basis; `B` is free of rank 48 | THEOREM (proved §2) |
| A | `B ≅ Q(zeta_168)`, a field, degree 48, abelian; conductor tower `21 → 84 → 168` | THEOREM (proved §3, machine-checked) |
| L2 | for `beta ∈ Q(sqrt3)^*`: `beta` is a cube in `B` **iff** it is a cube in `Q(sqrt3)` | THEOREM (proved §4) |
| B | `<[alpha1],[alpha2]> ≅ (Z/3)^2` inside `B^*/(B^*)^3`; **no** relation exists | THEOREM (two independent proofs, §4, §5) |
| C | `K0` is a **field**, `[K0:Q] = 432`, Galois over `Q`, non-abelian; idempotents `{0,1}` | THEOREM (proved §5) |
| D | `K0` is finite etale over `Z[1/42]`; ramified rational primes **exactly `{2,3,7}`**; `5` unramified | THEOREM (proved §6) |
| E | both registered frames are degree-1 primes of the unique factor; `105337 ≡ 105673 ≡ 1 (mod 168)`; each prime carries exactly 432 frames; the `p^2` frame is the unique Hensel lift | THEOREM + executed check (§7) |
| F | `W1/W2` is `K0`-rational: `q0 = u*(1+i)*(r3-1)/2 ∈ K0` satisfies the E-ratio equation; all four branches are `q0*i^k ∈ K0` | THEOREM **conditional** on the charged form of `E` (§8) |
| G | both banked points lie on a `q0`-branch (indices 3 and 0 respectively) | executed regression, evidence only (§8.3) |
| H | the involution `sigma: r3↦-r3, A1↔A2, W1↔W2` fixes `E`; whether it fixes the 29-row set is **open** | CONDITIONAL / test proposed (§10.8) |

Nothing here touches Tier 2–7 language. This report is entirely about the
coefficient algebra; it says nothing about the 184-row packet's correctness,
about raw-J existence, or about JC2.

---

## 2. Lemma L1 — the rank is exactly 432, before any irreducibility

Both charged reports say "rank at most 432" and "432 is not `[K0:Q]` for a
field". The first is an understatement and the second is a non sequitur; the
rank is exactly 432 unconditionally, and (§5) it *is* `[K0:Q]`.

**Lemma L1.** `K0` is a free `Q`-module of rank 432 with basis
`{ zeta42^a r3^b A1^c A2^d h^e : a<12, b<2, c<3, d<3, e<2 }`. Likewise
`B` is free of rank 48 on `{zeta42^a r3^b h^e}`.

*Proof.* Iterate the elementary fact that `R[t]/(f)` is free of rank `deg f`
over `R` for monic `f`. `Q[z]/(Phi42)` is free of rank 12 (`Phi42` monic of
degree 12; computed and matched against the source tuple in §3.1). Adjoin `r`
with the monic `r^2-3` (rank 2), `A1` with the monic `A1^3-(3+r)` (rank 3),
`A2` with the monic `A2^3-(3-r)` (rank 3), and finally `h`: `2h^2-3` is not
monic, but `2` is a unit in every `Q`-algebra, so `(2h^2-3) = (h^2-3/2)` with
`h^2-3/2` monic (rank 2). The five quotients commute, so the order of
adjunction is irrelevant. `12*2*3*3*2 = 432`. ∎

This is exactly the reduction system implemented in
`RadicalCoefficient._normalize` (`d43_common_integral_emitter.py:102-136`);
L1 is the statement that that rewriting is confluent and loses nothing, which
the leading-term shape `z^12, r^2, A1^3, A2^3, h^2` guarantees.

---

## 3. Item 1 — the degree-48 base is `Q(zeta_168)`: verified, not refuted

### 3.1 The pins

Executed locally (stdlib Python, exact integer/`Fraction` arithmetic):

```text
Phi42 computed from x^42-1 by exact division : (1,1,0,-1,-1,0,1,0,-1,-1,0,1,1)
PHI42 in d43_common_integral_emitter.py:36   : (1,1,0,-1,-1,0,1,0,-1,-1,0,1,1)
MATCH                                        : True
deg Phi_168                                  : 48
Phi_168(x) == Phi_42(x^4)                    : True
disc(Phi42) = Res(Phi42,Phi42')              : 205924456521 = 3^6 * 7^10
```

So the source's `PHI42` is the genuine 42nd cyclotomic polynomial (not
`x^42-1`, as the file's own comment claims and I confirm), and
`disc(Phi42) = 3^6*7^10` is **prime to 2**. That single fact is what makes the
tower not collapse at the `r3` layer.

### 3.2 Theorem A

**Theorem A.** Let `zeta = zeta_168`. The assignment

```text
zeta42 |--> zeta^4
r3     |--> zeta^14 + zeta^-14   ( = zeta_12 + zeta_12^-1 = sqrt3 )
h      |--> (zeta^21 + zeta^-21)*(zeta^14 + zeta^-14)/2   ( = sqrt2*sqrt3/2 = sqrt6/2 )
```

is an isomorphism of `Q`-algebras `B --> Q(zeta_168)`. In particular `B` is a
field of degree 48, abelian over `Q`, and the "pre-cubic base" is **exactly the
168th cyclotomic field**.

*Proof.* (a) *Well defined.* The three relations hold at the images. Executed
in `Z[x]/(Phi_168)` with exact integer arithmetic:

```text
Phi42(zeta^4) == 0      : True        ord(zeta^4) == 42 : True
(zeta^14+zeta^154)^2 == 3            : True
(zeta^21+zeta^147)^2 == 2            : True
2*h^2 == 3                            : True
```

(b) *Surjective.* Put `zeta3 = (zeta^4)^14` and `i = r3*(1+2*zeta3)/3`. Then
`i^2 = -1` (executed: `True`), and

```text
zeta8 := (1+i)*h*r3/3  ==  zeta^21          (executed: True)
zeta   =  zeta8^5 * (zeta^4)^16              (executed: True)
```

The exponents come from CRT: `21a + 56b + 24c ≡ 1 (mod 168)` has the solution
`(a,b,c) = (5,2,5)` (`105+112+120 = 337 = 2*168 + 1`), so
`zeta = zeta8^5 * zeta3^2 * zeta7^5`; and `zeta3 = zeta42^14`,
`zeta7 = zeta42^6` collapse `zeta3^2 zeta7^5 = zeta42^{28+30} = zeta42^{16}`.
Hence `zeta_168` lies in the image, so the image is all of `Q(zeta_168)`.

(c) *Injective.* By L1, `dim_Q B = 48 = [Q(zeta_168):Q]`; a surjective
`Q`-linear map between spaces of equal finite dimension is bijective. ∎

Note what this proof does **not** need: no irreducibility test, no CAS, no
factorisation of any tower. It is checkable by any engine that can multiply
integer polynomials modulo `Phi_168`.

### 3.3 The conductor tower, and why nothing collapses

Theorem A retroactively proves the two non-collapse facts that both charged
reports could only call "expected" / "likely":

```text
Q(zeta42)                          degree 12   conductor 21    (= Q(zeta21))
Q(zeta42, r3)  = Q(zeta_84)        degree 24   conductor 84    ==> sqrt3 ∉ Q(zeta42)
Q(zeta42, r3, h) = Q(zeta_168)     degree 48   conductor 168   ==> sqrt6 ∉ Q(zeta_84)
```

The middle identification is again by generation, not by irreducibility:
`sqrt3 = zeta_84^7 + zeta_84^-7 ∈ Q(zeta_84)` gives `⊆`, and conversely
`i = r3*(1+2*zeta3)/3 ∈ Q(zeta42, r3)` gives
`Q(zeta42,r3) ⊇ Q(zeta21, i) = Q(zeta_84)`. Same pattern at the top:
`sqrt6 = (zeta_168^21+zeta_168^-21)(zeta_168^14+zeta_168^-14) ∈ Q(zeta_168)`
gives `⊆`, and `sqrt2 = sqrt6/sqrt3 ∈ Q(zeta_84,h)` gives
`zeta8 = (1+i)/sqrt2 ∈ Q(zeta_84,h)`, hence `Q(zeta_84,h) ⊇ Q(zeta_168)`.

Cross-check by ramification (independent of the above): `Q(sqrt3)` has
discriminant 12 so 2 ramifies in it, while `disc(Phi42) = 3^6 7^10` is odd, so
2 is unramified in `Q(zeta42)` — therefore `sqrt3 ∉ Q(zeta42)`. Second
cross-check by conductor-discriminant: `f(Q(sqrt3)) = 12 ∤ 42` and
`f(Q(sqrt6)) = 24 ∤ 84`, while `12 | 168` and `24 | 168`.

**Correction to a phrase in the charged design memo.** grok46 §3.1 writes
"`2h^2-3` adjoins a form of `sqrt2`". As a description of the *relative* step
that is right — over `Q(zeta_84)`, which already contains `sqrt3`, adjoining
`h = sqrt6/2` is the same as adjoining `sqrt2` — but the *absolute* generator
is `sqrt6`, and the resulting field is `Q(zeta_168)`, not "a form of". The
distinction matters in §4: the Kummer classes must be tested over
`Q(zeta_168)`, not over `Q(zeta_84)`.

---

## 4. Item 2 — the two Kummer cubic classes, and every possible relation

`B = Q(zeta_168)` contains `mu_3` (`zeta3 = zeta42^14`, i.e. `3 | 168`), so
Kummer theory of exponent 3 applies verbatim over `B`.

`B^*/(B^*)^3` is an infinite group, so "every possible relation" can only mean:
every relation among the two classes actually present, i.e. every
`(i,j) ∈ (Z/3)^2` with `alpha1^i alpha2^j ∈ (B^*)^3`. There are 8 nontrivial
candidates. They fall into 4 inverse-pairs, and a class is trivial iff its
inverse is, so 4 representatives decide everything:

| `(i,j)` | representative modulo cubes | value | inverse pair |
|---|---|---|---|
| `(1,0)` | `alpha1` | `3 + sqrt3` | `(2,0)` |
| `(0,1)` | `alpha2` | `3 - sqrt3` | `(0,2)` |
| `(1,1)` | `alpha1*alpha2` | `6` | `(2,2)` |
| `(1,2)` | `alpha1*alpha2^2 ≡ alpha1/alpha2` | `2 + sqrt3 = eps` | `(2,1)` |

(The last line uses `alpha1 alpha2^2 = (alpha1/alpha2) * alpha2^3` and
`(3+sqrt3)/(3-sqrt3) = (3+sqrt3)^2/6 = 2+sqrt3`. All four representatives lie
in `Q(sqrt3)^*`, which is the whole point.)

### 4.1 Lemma L2 (abelian descent) — the classes may be decided in `Q(sqrt3)`

**Lemma L2.** Let `F/Q` be **abelian** with `sqrt3 ∈ F`, and let
`beta ∈ Q(sqrt3)^*`. If `beta ∈ (F^*)^3` then `beta ∈ (Q(sqrt3)^*)^3`.

*Proof.* Suppose `x ∈ F`, `x^3 = beta`, and `beta` is not a cube in `Q(sqrt3)`.
Then `t^3 - beta` has no root in `Q(sqrt3)`, hence (being a cubic) is
irreducible there, so `[Q(sqrt3)(x):Q(sqrt3)] = 3` and
`E := Q(sqrt3)(x)` has `[E:Q] = 6`. `E ⊆ F` and `F/Q` abelian, so every
subfield of `F` is Galois over `Q`; in particular `E/Q` is Galois, hence
`E/Q(sqrt3)` is normal, hence `E` contains the other roots `zeta3*x`,
`zeta3^2*x` of `t^3-beta`, hence `zeta3 = (zeta3 x)/x ∈ E`. Then
`Q(zeta3, sqrt3) = Q(zeta_12) ⊆ E`, so `4 | [E:Q] = 6` — false. ∎

`B = Q(zeta_168)` is abelian and contains `sqrt3`, so L2 applies.

### 4.2 The four non-cube facts in `Q(sqrt3)`

Norms are for `Q(sqrt3)/Q`; a cube has cube norm.

1. `N(3+sqrt3) = 9-3 = 6`, and 6 is not a rational cube ⟹ `alpha1 ∉ (Q(sqrt3)^*)^3`.
2. `N(3-sqrt3) = 6` ⟹ `alpha2 ∉ (Q(sqrt3)^*)^3`.
3. `N(6) = 36`, not a rational cube ⟹ `6 ∉ (Q(sqrt3)^*)^3`.
   (Equivalently: a cube root of 6 generates a non-normal cubic field, which
   cannot sit inside the quadratic `Q(sqrt3)`.)
4. `eps = 2+sqrt3` has norm 1, so the norm test is blind; use units. `O = Z[sqrt3]`
   is the ring of integers (disc 12) and its unit group is `{±eps^n}` with `eps`
   fundamental (`b=1` forces `a^2 = 3±1`, so `a=2`; and `a^2-3b^2 = -1` is
   impossible mod 3). If `eps = y^3` with `y ∈ Q(sqrt3)^*`, then `(y)^3 = (1)`
   as fractional ideals, so `y ∈ O^*`, so `y = ±eps^n` and
   `±eps^{3n} = eps`. Both real embeddings of `eps` are positive
   (`2+sqrt3 > 0`, `2-sqrt3 > 0`), so the sign is `+` and `3n = 1` — false.
   ⟹ `eps ∉ (Q(sqrt3)^*)^3`.

**Theorem B (first proof).** By L2 and 1–4, all 8 nontrivial classes are
nontrivial in `B^*/(B^*)^3`; i.e.
`Delta := <alpha1, alpha2>(B^*)^3/(B^*)^3 ≅ (Z/3)^2`, of order 9. ∎

---

## 5. Item 2, second proof (engine-free) — and the core question

### 5.1 A cubic-residue-character certificate, provable in twenty lines

This proof uses no Galois theory of `B`, no unit group, no CAS. Let `p ≡ 1
(mod 168)` be prime. Then `F_p` contains all 168th roots of unity, so
`B = Q(zeta_168)` has a degree-1 prime over `p` and there exist ring maps
`phi: B -> F_p`; the restriction `phi|Q(sqrt3)` sends `sqrt3` to one of the two
square roots of 3 in `F_p`, and **both** occur (the map
`Gal(B/Q) -> Gal(Q(sqrt3)/Q)` is onto). Let `chi(x) = x^((p-1)/3) ∈ mu_3(F_p)`,
a homomorphism killing cubes. If `alpha1^i alpha2^j ∈ (B^*)^3`, then for every
such `phi` (with `p ∤ 6`, automatic here, so both `alpha_k` are units)

```text
a*i + b*j ≡ 0 (mod 3),   where  chi(phi(alpha1)) = w^a,  chi(phi(alpha2)) = w^b.
```

Two frames whose `(a,b)` span `F_3^2` therefore force `(i,j) = (0,0)`.

Executed locally:

```text
p = 673   (prime, 673 = 4*168 + 1, so p ≡ 1 mod 168)
sqrt3 mod p = 26 and 647
  frame r = 26 :  chi(3+r) = w^2 , chi(3-r) = w^0    ==>  2i + 0j ≡ 0  ==> i ≡ 0
  frame r = 647:  chi(3+r) = w^0 , chi(3-r) = w^2    ==>  0i + 2j ≡ 0  ==> j ≡ 0
  det = 2*2 - 0*0 = 4 ≡ 1 (mod 3)  ≠ 0
```

**Theorem B (second proof).** `Delta ≅ (Z/3)^2`. ∎

(The two frames at `p = 673` are Galois-conjugate — they differ by
`sqrt3 ↦ -sqrt3`, which swaps `alpha1 ↔ alpha2`, hence swaps `(a,b) ↦ (b,a)`.
That is legitimate: they are genuinely two distinct primes of `B`, and the
relation would have to hold at both. Other independent pairs exist, e.g.
`p = 1009` with `r = 149` and `r = 860`; the certificate should record two
primes anyway, as a mutation guard.)

Note the *scan itself* also confirms that the registered primes are silent
witnesses: at `105337` and `105673` both `alpha_k` are cubes, so their character
vectors are `(0,0)`, which imposes no condition at all. That is precisely why
the two registered frames could never have settled this question, and why
grok46 §3.1's refusal to guess was correct.

### 5.2 Theorem C

**Theorem C.** `K0` is a field, `[K0:Q] = 432`, and `K0/Q` is Galois and
non-abelian. Explicitly `K0 ≅ Q(zeta_168)(cbrt(alpha1), cbrt(alpha2))` for any
choice of cube roots, and equally `K0 ≅ Q(zeta_168)(cbrt 6, cbrt(2+sqrt3))`.
Its only idempotents are `0` and `1`; there is **no** product decomposition and
there are no nontrivial primitive idempotents to exhibit.

*Proof.* By Theorem A, `K0 = B[A1,A2]/(A1^3-alpha1, A2^3-alpha2)` with `B` a
field containing `mu_3`, and by L1 it is free of rank 9 over `B`. Fix cube
roots in an algebraic closure and let `L = B(cbrt alpha1, cbrt alpha2)`. By
Kummer theory `[L:B] = |Delta| = 9` (Theorem B). The evident `B`-algebra
surjection `K0 --> L` is a surjection between `B`-spaces of equal dimension 9,
hence an isomorphism. Thus `K0 ≅ L` is a field of degree `48*9 = 432`.

*Galois.* Let `sigma: K0 -> Q-bar` fix `Q`. `sigma(B) = B` since `B/Q` is
Galois. `sigma(cbrt alpha1)^3 = sigma(alpha1) ∈ {alpha1, alpha2}` according to
`sigma(sqrt3) = ±sqrt3`; in either case `sigma(cbrt alpha1)` is
`zeta3^k * cbrt(alpha_m) ∈ K0`. Same for `alpha2`. So `sigma(K0) = K0`.
Equivalently: `Delta` is `Gal(B/Q)`-stable because the nontrivial action on
`Q(sqrt3)` swaps `alpha1 ↔ alpha2`.

*Non-abelian.* `cbrt 6 = A1*A2 ∈ K0` (since `alpha1 alpha2 = 6`), so
`Q(cbrt 6) ⊆ K0` is a cubic field that is not normal over `Q`. A subfield of an
abelian extension is normal, so `K0/Q` is not abelian. In particular `K0` is
**not** contained in any cyclotomic field: only the degree-48 base is
cyclotomic.

*Second generator set.* `A1 A2` and `A1/A2` cube to `6` and `eps`; the
base change `[[1,1],[1,-1]]` over `F_3` has determinant `-2 ≡ 1 ≠ 0`, so
`<6, eps> = Delta` and `B(cbrt 6, cbrt eps) = K0`. ∎

**Structure remark (bookkeeping only).** With
`F = Q(zeta_12, cbrt alpha1, cbrt alpha2)` one has `[F:Q] = 36`, `F/Q` Galois,
`B ∩ F = Q(zeta_12)` (forced by `432 = 48*36/[B∩F:Q]`), so
`Gal(K0/Q) ≅ Gal(B/Q) ×_{(Z/12)^*} Gal(F/Q)` of order 432, with
`Gal(K0/B) ≅ (Z/3)^2`. The nine elements of `Gal(K0/B)` are trivial to
implement in the committed 432-basis: `A1 ↦ zeta3^a A1`, `A2 ↦ zeta3^b A2`,
i.e. multiply the basis monomial `... A1^c A2^d ...` by `zeta3^(ac+bd)` with
`zeta3 = zeta42^14`. §10.2 uses this for exact inversion.

### 5.3 What is thereby refuted

* "`K0` is a rank-432 quotient algebra, not automatically a field; decompose it
  componentwise" (gpt56 §1, §4.2) — the decomposition is trivial: `c = 1`.
* "Degrees 48, 144, 432, or a product, are all still legal" (grok46 §3.1) — only
  432 is legal, and it is a field.
* grok46 §2.2's "every primitive idempotent factor of `K0`", §3.2's
  `K0-SPLIT` product, §3.3's Bezout/annihilator pivot protocol, §3.4's
  `∏ K_i[W1,W2,...]`, and gap **G5** ("`K0` components that miss the registered
  frames are invisible") are all **vacuous**: there are no such components.
* grok46's own refusal list keeps the entry "`K0` called a field w/o
  `K0SPLIT` ⟹ REFUSE the packet". That refusal is now satisfiable: this report
  *is* the `K0SPLIT` output, with `c = 1`, and §9 gives its replay.

What is **not** refuted, and remains exactly as those reports state it:
everything about determinantal charts, Fitting strata, `V(Delta)` retention,
the tail-Jacobian drop locus, rail separation, and tier discipline. Being a
field removes a *coefficient-algebra* hazard only. See §10.5.

---

## 6. Item 3 — reducedness, finite etaleness, ramified primes

**Theorem D.**
1. `K0` is reduced (it is a field), and `K0/Q` is finite separable, hence
   finite etale. There are no nilpotents in the coefficient algebra.
2. The standard model `A = Z[1/42][z,r,A1,A2,h]/(same five relations)` is
   **finite etale of rank 432 over `Z[1/42]`**.
3. The rational primes ramifying in `K0` are **exactly `{2, 3, 7}`**. `5` is
   unramified, and so is every prime outside `{2,3,7}`.

*Proof.* (1) is immediate from Theorem C.

(2) Use `R -> R[t]/(f)` is etale when `f` is monic with `disc(f) ∈ R^*`, and
compose:

| layer | monic model | discriminant | needs inverted |
|---|---|---|---|
| `zeta42` | `Phi42` | `3^6 * 7^10` (computed §3.1) | `3, 7` |
| `r3` | `r^2-3` | `12` | `2, 3` |
| `A1` | `A1^3-alpha1` | `-27 alpha1^2` | `3`, and `alpha1 ∈ A^*` |
| `A2` | `A2^3-alpha2` | `-27 alpha2^2` | `3`, and `alpha2 ∈ A^*` |
| `h` | `h^2-3/2` | `6` | `2, 3` |

`alpha1 alpha2 = 6` is invertible in `Z[1/42]`, hence each `alpha_k` is a unit,
so the two cubic discriminants are units. Inverting `42 = 2*3*7` suffices.
(The frame gate in `d43_common_integral_emitter.py:328-334` computes exactly
these derivatives `Phi42', 2r3, 3A1^2, 3A2^2, 4h`; executed at the `105337`
frame they are `72846, 1590, 63015, 32307, 95731`, all nonzero, as étaleness
predicts.)

(3) Upper bound from (2): only `2,3,7` can ramify. Lower bound: `3` and `7`
ramify in `Q(zeta42) ⊆ K0` (indices 2 and 6), and `2` ramifies in
`Q(sqrt3) ⊆ K0` (disc 12). ∎

**Finer location (not needed above, recorded for the artifact).** In the
Kummer layer `K0/B`, a prime `q` of `B` with `q ∤ 3` ramifies iff
`3 ∤ v_q(alpha)`. In `Q(sqrt3)`, `alpha1 = sqrt3*(1+sqrt3)` has valuation 1 at
the ramified prime over 3 and valuation 1 at the ramified prime over 2
(`N(1+sqrt3) = -2`). Since `e_2(B) = 4` and `e_2(Q(sqrt3)) = 2`, `v_q(alpha1)
= 2` above 2 and `= 1` above 3: neither is `≡ 0 (mod 3)`, so the cubic layer
ramifies above **2 and 3**, and is unramified above 7. All 7-ramification is
cyclotomic.

**Consequence for the source's constants.** `ETALE_LOCALIZATION_PRIMES =
(2,3,5,7)` (`d43_common_integral_emitter.py:42`) is a *safe superset*: 5 is not
needed for étaleness and does not ramify. 5 enters only through
`SOURCE_DENOMINATOR_PRIMES = (2,3,5)`, i.e. Newton denominators of coefficients,
a different object. Nothing is wrong with the constant; but a report that
derives "ramified at 2,3,5,7" from it would be wrong.

---

## 7. Item 4 — mapping both registered frames to the factor(s)

There is one factor, so the map is a single arrow — but the content is in
*which* prime of `K0` each frame is, and in the splitting behaviour.

**Theorem E.** Let `p ∈ {105337, 105673}`.
1. `p ≡ 1 (mod 168)` (executed: `105337 = 627*168 + 1`, `105673 = 629*168 + 1`).
2. A registered frame is precisely a `Z[1/42]`-algebra homomorphism
   `phi_p : A --> F_p`; its kernel `P_p = ker(phi_p)` is a maximal ideal of `A`
   with residue field `F_p`, i.e. a **degree-1 prime of the unique factor `K0`**
   above `p`. `p ∤ 42`, so `p` is unramified.
3. Because `K0/Q` is Galois (Theorem C) and admits a degree-1 prime over `p`,
   `p` **splits completely**: there are exactly 432 primes above `p`, all of
   degree 1, permuted simply transitively by `Gal(K0/Q)`. Equivalently
   `A ⊗ F_p ≅ F_p^432`, i.e. exactly 432 frames.

*Executed check of (3)* — a brute-force count of solutions
`(z,r,a1,a2,h) ∈ F_p^5` of the five defining equations:

```text
p = 105337 : #roots(Phi42) = 12 , #h = 2 , sum_r #a1*#a2 = 18   TOTAL = 432
p = 105673 : #roots(Phi42) = 12 , #h = 2 , sum_r #a1*#a2 = 18   TOTAL = 432
```

with, at both primes and for both square roots of 3, `#a1 = #a2 = 3` (both
`alpha_k` are cubes mod `p`). Both registered frames pass
`validate_specialization` at their prime.

**Honesty note on what this check can and cannot do.** The count 432 is a
*consistency* check, not a proof of Theorem C: a hypothetical split
`K0 ≅ L × L × L` with `[L:Q] = 144` totally split would produce the same 432.
The proof of fieldness is §4–§5 and nothing else. Conversely, a count `≠ 432`
would have refuted Theorem C outright; it did not.

*The `p^2` frame.* `REGISTERED_P2_FRAME_105337` satisfies all five relations
modulo `105337^2` (executed: all five residues 0) and reduces mod `p` to the
registered `p`-frame (executed: `True`). Étaleness (Theorem D) says this lift is
**unique**: the Hensel frame is not a choice, it is determined, and any second
`p^2` frame over the same `p`-frame would be a defect.

*Practical corollaries for the campaign.*
* The 432 frames over one `p` form a single `Gal(K0/Q)`-torsor. So "two
  registered frames" is **one Galois orbit per prime**, not two probes of two
  components. Agreement between them is much weaker evidence than it looks: they
  are conjugate objects.
* A modular result computed at one frame transports to all 432 by the group
  action; it does **not** transport to characteristic zero. The existing
  CRT-refusal stands unchanged.
* Frame-dependent labels are *not* portable: §8.3 shows the two banked points
  sit on **different** E-branch indices (3 and 0) purely because of the frame's
  root choices. Never carry a branch index across frames.

---

## 8. Theorem F — the E-relation ratio is `K0`-rational (Rail E collapse)

### 8.1 Setting (conditional input)

Both charged reports carry, from the reviewed bridge `e1b99600...`, the
existential projection of the displayed E5/E6 subsystem on `W1*W2 ≠ 0`:

```text
E := (9 + 5*r3)*A1*W1^4 + (9 - 5*r3)*A2*W2^4  =  0.
```

I did not re-derive `E`; everything in §8 is **conditional** on that displayed
form. With `q = W1/W2` this is `q^4 = c` where (both reports agree, and I
re-derived it: `(9+5r3)^-1 = (9-5r3)/6`, then
`-(9-5r3)^2/6 = -(156-90 r3)/6 = 15 r3 - 26`)

```text
c = (15*r3 - 26) * A2/A1.
```

### 8.2 The theorem

**Theorem F.** Let `u = A2/A1 ∈ K0^*` and
`i = r3*(1+2*zeta42^14)/3 ∈ K0` (`i^2 = -1`). Then

```text
(F1)  u^3      = (3-r3)/(3+r3) = 2 - r3 = eps^-1
(F2)  15*r3-26 = -(2-r3)^3     = -eps^-3
(F3)  c        = -u^10
(F4)  s := (1+i)*(r3-1)/2  satisfies  s^2 = i*(2-r3) = i*eps^-1
(F5)  q0 := u*s  satisfies  q0^2 = i*u^5   and   q0^4 = -u^10 = c.
```

Hence `q0 ∈ K0`, and the four solutions of `q^4 = c` are `q0, i*q0, -q0, -i*q0`,
**all in `K0`**. No field extension of `K0` is needed to impose `E`; the
polynomial `t^4 - c` splits completely over `K0`.

*Proof.* (F1) `u^3 = alpha2/alpha1 = (3-sqrt3)^2/6 = 2-sqrt3`. (F2)
`(2-sqrt3)^3 = 26-15 sqrt3`. (F3) `c = -eps^-3 u = -(u^3)^3 u = -u^10`. (F4)
`(1+i)^2 = 2i` and `(r3-1)^2 = 4-2r3`, so `s^2 = 2i(4-2r3)/4 = i(2-r3)`. (F5)
`q0^2 = u^2 s^2 = u^2 i (2-r3) = u^2 i u^3 = i u^5`, so
`q0^4 = (i u^5)^2 = -u^10 = c`. The four fourth roots differ by `mu_4 ⊂ K0`. ∎

Every step is a two-line identity over `Q(sqrt3)` or `Q(i,sqrt3)`; the only
input from the cubic layer is `u^3 = eps^-1`, which is immediate from the two
defining relations. The theorem therefore does **not** depend on Theorem C —
but Theorem C is what makes the conclusion useful (in a non-field `K0`, `q0`
could have been a zero divisor; here it is a unit, with explicit inverse
`q0^-1 = -sigma(q0)`, see §10.8).

*Executed in the committed algebra* (`RadicalCoefficient`, exact `Fraction`
arithmetic over the 432-basis, `d43_common_integral_emitter.py`):

```text
r3^2 == 3 / A1^3 == 3+r3 / A2^3 == 3-r3 / 2h^2 == 3      : True (all)
I^2 == -1                                                : True
u^3 * (3+r3) == (3-r3)                                   : True
eps^3 == 26 + 15 r3 ;  eps*(2-r3) == 1                   : True
c == -u^10                                               : True
q0^2 == I*u^5 ;  q0^4 == c                               : True
E(q0,1) == 0     (direct substitution, not via the u-identity) : True
E(I^k * q0, 1) == 0 for k = 0,1,2,3                      : True (four branches)
the four branches are pairwise distinct                  : True
```

`q0` has **four** terms in the 432-basis, with denominators in `{2,3}` only —
inside `SOURCE_DENOMINATOR_PRIMES`:

```text
q0 = A1^2*A2 * ( -5/6 + (1/2)*r3 + (2/3)*zeta42^7 - (1/3)*zeta42^7*r3 )

exponent (zeta42, r3, A1, A2, h) : coefficient
  (0,0,2,1,0) : -5/6
  (0,1,2,1,0) :  1/2
  (7,0,2,1,0) :  2/3
  (7,1,2,1,0) : -1/3
```

### 8.3 Regression against both banked pointbanks (evidence, not proof)

```text
bb0f13b61616c486116027e284483a4fb0f529f8df2dca7f728d56584d98fcbb  cases/d43_full_pointbank_p105337.pkl
b933cdb5b72bd4073da0cb82150db768f6b4607d5cd29d3d4aec0fe22ce5bcc3  cases/d43_full_pointbank_p105673.pkl
```
(both hashes recomputed on this host; they match the values sealed in the
gpt56 audit's §7 frozen-input list.)

Reading only `cell_values['W1','W2','uW1','uW2']` and specialising `q0` at the
registered frame:

```text
p = 105337 : W1/W2 = 7210    q0-branches = [73053, 98127, 32284, 7210]   match at k=3
p = 105673 : W1/W2 = 14755   q0-branches = [14755, 101655, 90918, 4018]  match at k=0
both       : uW1*W1 ≡ 1, uW2*W2 ≡ 1, and E(W1,W2) ≡ 0 at the frame
```

Both banked ratios are `q0`-branches, at different branch indices. This is a
regression, not a construction: it confirms Theorem F is the right object and
that the banked points are E-conformal, and it warns that the branch index is
frame-dependent.

### 8.4 What this changes in the charged designs

* grok46 §4 Rail E step 2: "This is a degree-≤4 cover of each `K_i`" — there is
  **no** cover. `rho^4 ∈ K_i` is fixed *and* `rho ∈ K0`.
* gpt56 §4.3: "Work in the whole squarefree quotient for `q`, or factor it and
  retain every factor; selecting only the modularly banked fourth root would be
  circular." The retention requirement is right and stays; the factorisation is
  now **complete and explicit**: `t^4 - c = (t-q0)(t-i q0)(t+q0)(t+i q0)` over
  `K0`. Retaining every factor now costs four scalar substitutions instead of a
  quartic field extension.
* Consequently Rail E after `E` is a **one-unknown** problem over `K0`: set
  `W1 = i^k q0 sigma`, `W2 = sigma`, `k = 0..3`, and every row becomes a
  polynomial in the single scale `sigma` over `K0`. The `+42` inhomogeneity at
  `(eta,slot) = (0,20)` is the only thing that can pin `sigma`, exactly as
  grok46 §6/G8 says — but now the "degree-6 scale polynomial" has a well-posed
  exact analogue: a univariate element of `K0[sigma]` per branch, not a modular
  rumour.

---

## 9. Item 5 — a small exact certificate, replayable on AWS

### 9.1 Design principles

* Every layer is checkable by an engine that does **not** know why it is being
  asked (no "we ran it and it printed 0").
* The critical path is six cheap layers (L0-L5); the expensive absolute-degree
  construction is optional and capped, and no result depends on it.
* Irreducibility of a degree-432 polynomial is **never** needed. The theorem
  supplies it; the certificate only needs well-definedness + surjectivity +
  a dimension count. (Charged reports asked for factorisation of the tower;
  this is strictly cheaper and strictly stronger.)

**Status of §9.2: RECIPE, NOT EXECUTED.** There is no `gp` on this host
(`which gp` finds only a shell alias for `git push`), and PARI is not installed.
The script below was written and hand-reviewed but **not run**. Its layers L0,
L1, L3, L4, L5 were independently executed here in stdlib Python (outputs quoted
in §3, §5.1, §7, §8); only layers L2 (`nffactor`) are unexecuted anywhere.

### 9.2 `k0_split_cert.gp`

```gp
\\ D43 K0 splitting certificate.  Replay:  gp -q k0_split_cert.gp
\\ Prints one line per test; final line must read  ALL_PASS 1.
ok = 1;
chk(lab, val) = {ok = ok && (val != 0); printf("%-52s %d\n", lab, val != 0); val;}

\\ ---- L0: source pins ---------------------------------------------------
PHI42SRC = [1,1,0,-1,-1,0,1,0,-1,-1,0,1,1];   \\ d43_common_integral_emitter.py:36
P42  = polcyclo(42, 'x);
P168 = polcyclo(168,'x);
chk("PHI42 source tuple == polcyclo(42)", Vecrev(P42) == PHI42SRC);
chk("deg polcyclo(168) == 48",            poldegree(P168) == 48);
chk("Phi168(x) == Phi42(x^4)",            P168 == subst(P42,'x,'x^4));
chk("disc(Phi42) == 3^6*7^10",            poldisc(P42) == 3^6*7^10);
chk("2 does not divide disc(Phi42)",      poldisc(P42) % 2 != 0);

\\ ---- L1: Theorem A, base = Q(zeta168) ----------------------------------
z = Mod('x, P168); z42 = z^4; r3 = z^14 + z^154; s2 = z^21 + z^147; h = s2*r3/2;
chk("Phi42(z42) == 0",           subst(P42,'x,z42) == 0);
chk("ord(z42) == 42",            z42^42 == 1 && z42^21 != 1 && z42^14 != 1);
chk("r3^2 == 3",                 r3^2 == Mod(3,P168));
chk("s2^2 == 2",                 s2^2 == Mod(2,P168));
chk("2*h^2 == 3",                2*h^2 == Mod(3,P168));
i0 = r3*(1 + 2*z42^14)/3;
chk("i^2 == -1",                 i0^2 == Mod(-1,P168));
z8 = (1+i0)*h*r3/3;
chk("zeta8 == x^21",             z8 == z^21);
chk("GENERATION z8^5*z42^16 == x", z8^5*z42^16 == z);
\\ dim_Q B = 48 (monomial freeness, Lemma L1) + surjection ==> B = Q(zeta168).

\\ ---- L2: Kummer classes, two independent layers ------------------------
\\ (a) cheap layer in Q(sqrt3); rigorous given Lemma L2 (abelian descent).
nf3 = nfinit('y^2 - 3);
CL  = ['y + 3, 3 - 'y, 6, 2 + 'y];         \\ alpha1, alpha2, alpha1*alpha2, alpha1/alpha2
for(k = 1, 4,
    f = nffactor(nf3, 'x^3 - CL[k]);
    chk(Str("Q(sqrt3): x^3 - class",k," irreducible"),
        matsize(f)[1] == 1 && f[1,2] == 1));
\\ (b) engine layer directly over B; needs no lemma at all.
QB  = polcyclo(168,'y);
nfB = nfinit(QB);
R3B = Mod('y^14 + 'y^154, QB);
CLB = [3 + R3B, 3 - R3B, Mod(6,QB), 2 + R3B];
chk("R3B^2 == 3 in B", R3B^2 == Mod(3,QB));
for(k = 1, 4,
    f = nffactor(nfB, 'x^3 - CLB[k]);
    chk(Str("Q(zeta168): x^3 - class",k," irreducible"),
        matsize(f)[1] == 1 && f[1,2] == 1));
\\ Kummer: all four (hence all eight) classes nontrivial ==> [K0:B] = 9.

\\ ---- L3: engine-free character certificate -----------------------------
charvec(p) = {my(w, v = [], r0);
  if(!isprime(p) || p % 168 != 1, error("bad certificate prime"));
  w = Mod(znprimroot(p), p)^((p-1)/3);
  r0 = lift(sqrt(Mod(3,p)));
  for(s = 1, 2, my(r = if(s == 1, r0, p - r0),
                  a = znlog(Mod(3+r,p)^((p-1)/3), w, 3),
                  b = znlog(Mod(3-r,p)^((p-1)/3), w, 3));
      v = concat(v, [[r,a,b]]));
  v};
V = charvec(673);
chk("p=673 two frames give independent F_3 forms",
    (V[1][2]*V[2][3] - V[2][2]*V[1][3]) % 3 != 0);
V2 = charvec(1009);
chk("p=1009 independent as well (mutation guard)",
    (V2[1][2]*V2[2][3] - V2[2][2]*V2[1][3]) % 3 != 0);

\\ ---- L4: frames ---------------------------------------------------------
FR = [[105337, 2779, 795, 50630, 10114, 50267],
      [105673, 13862, 14686, 38664, 46664, 35053]];
for(k = 1, 2, my(p = FR[k][1], zz = FR[k][2], rr = FR[k][3],
                 a1 = FR[k][4], a2 = FR[k][5], hh = FR[k][6], nz, nh, tot, r0);
  chk(Str("frame ",p,": p == 1 mod 168"), p % 168 == 1);
  chk(Str("frame ",p,": five relations"),
      Mod(subst(P42,'x,zz),p) == 0 && Mod(rr^2-3,p) == 0 &&
      Mod(a1^3-3-rr,p) == 0 && Mod(a2^3-3+rr,p) == 0 && Mod(2*hh^2-3,p) == 0);
  chk(Str("frame ",p,": etale (jacobian units)"),
      Mod(subst(P42',  'x, zz), p) != 0 && Mod(2*rr,p) != 0 &&
      Mod(3*a1^2,p) != 0 && Mod(3*a2^2,p) != 0 && Mod(4*hh,p) != 0);
  nz  = #polrootsmod(P42, p);
  nh  = if(issquare(Mod(3,p)/2), 2, 0);
  r0  = lift(sqrt(Mod(3,p)));  tot = 0;
  for(s = 1, 2, my(r = if(s == 1, r0, p-r0),
                   c1 = if(Mod(3+r,p)^((p-1)/3) == Mod(1,p), 3, 0),
                   c2 = if(Mod(3-r,p)^((p-1)/3) == Mod(1,p), 3, 0));
      tot += c1*c2);
  chk(Str("frame ",p,": exactly 432 F_p points"), nz*nh*tot == 432));

\\ ---- L5: Theorem F, all at base level ----------------------------------
epsq = Mod(2 + 'y, 'y^2-3);
chk("F2: -(2-r3)^3 == 15 r3 - 26",  -(Mod(2-'y,'y^2-3))^3 == Mod(15*'y-26,'y^2-3));
chk("F1: (3-r3)/(3+r3) == 2-r3",    Mod(3-'y,'y^2-3)/Mod(3+'y,'y^2-3) == Mod(2-'y,'y^2-3));
sB = (1 + i0)*(r3 - 1)/2;            \\ inside B = Q(zeta168)
chk("F4: s^2 == i*(2-r3)",          sB^2 == i0*(2 - r3));
\\ F3/F5 then follow from u^3 = 2-r3, which is A1^3, A2^3 and nothing else.

\\ ---- OPTIONAL, capped: absolute primitive element ----------------------
\\ Only for producing the downstream inverse-map artifact; NOT needed for the
\\ theorem.  Cap: alarm(1800).
\\ rel = 'x^3 - (3 + R3B);  [pol,a,k] = rnfequation(nfB, rel, 1);
\\ chk("[B(A1):Q] == 144", poldegree(pol) == 144);

printf("ALL_PASS %d\n", ok);
```

### 9.3 Independent (non-PARI) checker

The checker must be a *different engine*. The one used here is stdlib Python
over the producer's own `RadicalCoefficient`, which has the useful property of
exercising the emitter's arithmetic at the same time:

1. **Base layer.** Integer polynomial arithmetic in `Z[x]/(Phi_168)`; verify the
   five identities of §3.2(a) and the two generation identities of §3.2(b). This
   alone certifies Theorem A, since dimension is Lemma L1.
2. **Class layer.** The twenty-line character computation of §5.1, at two
   primes. Pure `pow`; no algebraic number theory.
3. **Frame layer.** The 432-count and the frame/Hensel checks of §7.
4. **Theorem F layer.** The `RadicalCoefficient` identities of §8.2, including
   the *direct* substitution `E(q0,1) == 0` (not routed through `c = -u^10`).
5. **Inverse-map checks** (these are the "divide legally" primitives; all
   executed here and all `True`):

```text
r3   * (r3/3)               == 1
h    * (2h/3)               == 1
(3+r3)*((3-r3)/6)           == 1
(3-r3)*((3+r3)/6)           == 1
A1   * (A1^2*(3-r3)/6)      == 1
A2   * (A2^2*(3+r3)/6)      == 1
zeta42 * (-zeta42^20)       == 1
q0   * (-sigma(q0))         == 1        (sigma as in §10.8)
```

6. **Optional primitive-element artifact.** If `L2/optional` produces an
   absolute `m(t)` of degree 432 together with polynomials
   `Z(t),R(t),A1(t),A2(t),H(t)` of degree `< 432`, the checker verifies only:
   (i) the five relations hold in `Q[t]/(m)`; (ii) the chosen primitive
   expression `Theta(Z,R,A1,A2,H) ≡ t (mod m)`. Then the induced map
   `K0 -> Q[t]/(m)` is a surjection of 432-dimensional `Q`-spaces, hence an
   isomorphism, and **irreducibility of `m` is a corollary of Theorem C**,
   not an input. This is the "factor / minimal-polynomial / inverse-map" triple
   the charge asks for, with the expensive direction deleted.

### 9.4 Mutation battery (a certificate that cannot fail is not a certificate)

| mutation | expected result |
|---|---|
| `PHI42SRC` last entry `1 -> -1` | L0 fails |
| `r3` set to `z^12 + z^156` (i.e. `zeta_14 + conj`) | L1 `r3^2 == 3` fails |
| `h` set to `s2*r3/3` | L1 `2h^2 == 3` fails |
| drop the `z8^5*z42^16 == x` line | surjectivity unproved: **must** be treated as a failed certificate, not a passed one (this is the load-bearing line) |
| class list `[y+3, 3-y, 6, 2+y] -> [y+3, 3-y, 6, 7+4*y]` | `7+4y = eps^2` is still a non-cube, so L2 still passes: **this mutation must NOT fail**, and a battery that reports it as a failure is miscoded |
| class list `-> [y+3, 3-y, 6, (1+y)^3]` | L2 must fail (a cube) |
| character prime `673 -> 105337` | L3 must fail (vector `(0,0)`; degenerate certificate) |
| frame `A1 50630 -> 50631` | L4 relations fail |
| `q0` coefficient `-5/6 -> -5/7` | Theorem F direct substitution fails |
| replace `E(q0,1)` check by `c == -u^10` only | tautological-pass hole: the direct substitution must be retained |

### 9.5 Cost

`nfinit(polcyclo(168))` plus four cubic `nffactor` calls is seconds on any host;
the character certificate is microseconds; the 432-count is one pass over `F_p`.
**No AWS host is required for `K0-SPLIT` at all.** The job that grok46's DAG puts
on the critical path next to `FITTING-A` costs less than a second and can be
replayed by hand.

---

## 10. Item 6 — exactly how this changes the component-safe Fitting solve

### 10.1 The component bookkeeping disappears

`c = 1`. Concretely, delete from the solve DAG:

* `K0-SPLIT` as a product-decomposition job (replace by the ~1s certificate of
  §9, still hash-pinned, still a prerequisite);
* the "reissue `FITTING-A` per `K_i`" instruction (grok46, DAG §Parallelism);
* D2 ("tower factorization ... if this times out, D5-split on pivots") and D5's
  dynamic-evaluation machinery;
* the `K_i`-id field of every worker receipt (keep the field, write `K0`);
* the `∏ K_i` language in §3.4, and gap **G5** entirely.

Keep the receipt schema otherwise unchanged: the chart/minor/complement
bookkeeping is orthogonal to this result.

### 10.2 The legal pivot rule becomes decidable and cheap

Old rule (grok46 §3.3): "A pivot is legal only after a Bezout identity `ab=1` in
`K0`, or after splitting at the annihilator `Ann(a)`."

New rule, complete and sufficient:

> **A coefficient `a ∈ K0` is invertible iff its 432-term normal form is
> nonzero.** No annihilators, no splitting, no Bezout search.

The prohibition that survives intact — and it is the one that actually bites —
is: *nonzero at two modular frames does not imply nonzero*. Both `105337` and
`105673` frames can kill a nonzero `a` (`a` may lie in either of those two
degree-1 primes). What is now available is that the *exact* test is a normal-form
comparison, i.e. free.

Explicit inversion, no linear algebra of size 432:

```text
Gal(K0/B) = { s_(a,b) : A1 |-> zeta3^a A1 , A2 |-> zeta3^b A2 },  zeta3 = zeta42^14
N(x) := prod_{(a,b) in (Z/3)^2} s_(a,b)(x)  ∈  B            (8 monomial-relabel
                                                              multiplications)
x^-1 = ( prod_{(a,b) != (0,0)} s_(a,b)(x) ) * N(x)^-1
```

and `N(x)^-1` is an inverse in the cyclotomic field `Q(zeta_168)` (48-dimensional
solve, or the standard cyclotomic norm trick). Each `s_(a,b)` is a relabelling of
basis exponents with a `zeta3` twist — trivial to add to `RadicalCoefficient`.

### 10.3 The five relations generate a maximal ideal — a free algorithmic gift

Theorem C says `(Phi42, r3^2-3, A1^3-alpha1, A2^3-alpha2, 2h^2-3)` is a
**maximal** ideal of `Q[z,r,A1,A2,h]`. Therefore a Groebner/msolve computation
that simply *adjoins those five polynomials as generators*, with `z,r,A1,A2,h`
as five ordinary variables alongside `W1,W2,L,M,H`, is sound: the coefficient
part contributes no spurious components, no extra primary components, and no
splitting of the answer. Before this theorem that was a genuine hazard and would
have required post-hoc decomposition of every output component. This is likely
the single most useful practical consequence: it lets engines that cannot work
over a degree-432 number field (msolve, most `F4` front ends) run correctly by
adding five variables and five equations.

Recommended presentations, in order of preference:

1. `Q(zeta_168)` (native cyclotomic arithmetic, fast in Singular/Magma) plus the
   two relative cubics — 9-dimensional relative work.
2. Five extra variables + five relations over `Q` (§10.3) — for engines with no
   number-field support.
3. An absolute degree-432 primitive element — **not recommended**; the
   coefficient blow-up is severe and nothing needs it.

### 10.4 Rail E becomes a one-unknown problem, four times

From Theorem F: run four branches `k = 0,1,2,3` with

```text
W1 = i^k * q0 * sigma ,    W2 = sigma ,    q0 as in §8.2 (four basis terms).
```

Then band 20 is `A(sigma) L = b(sigma)` over `K0[sigma]`, the `+42` at
`(eta,slot)=(0,20)` is the only inhomogeneity, and the residual is univariate.
The rank stratification of grok46 §1.2 still applies but over a *line*, not a
plane: `Z_k(A) ⊂ A^1_{K0}` is a finite set of `sigma`-values plus possibly all
of `A^1`, which is much cheaper to decide exactly. The mod-`p` "degree-6 scale
polynomial" now has a well-defined exact target to be compared against, per
branch.

Retention discipline is unchanged: all four branches must be carried, `V(Delta)`
for every inverted minor must be retained, and `sigma = 0` is excluded by
localisation and not by neglect.

### 10.5 What does *not* change

* Fitting/determinantal chart retention (grok46 §2) — untouched. Being a field
  says nothing about `W`-plane strata.
* `I_22(J_T)` drop locus, `W1=0`, `W2=0`, Rail J/Rail E separation, and the
  entire tier ladder — untouched.
* G1 ("`29-22 = 7` is not an elimination ideal"), G2, G3, G4, G6, G7, G8, G9,
  G10 — untouched. Only G5 dies.
* The row packet remains unsealed. This report gives no reason to launch
  anything on the 184-row problem; it removes a prerequisite, it does not
  supply one.
* Nothing here bears on Q0, `H_F`, NF equivalence, all-depth compatibility,
  Keller, or JC2.

### 10.6 Correct language for future reports

Permitted after this report: "`K0` is a number field of degree 432" with a
pointer to the §9 certificate. Still forbidden: deriving that from the two
frames (§7 shows why the count 432 is not a proof), and deriving any
`W`-side statement from it.

### 10.7 One dependency to re-check in the emitter

`RadicalCoefficient.assert_source_denominators` allows `{2,3,5}`. `q0`, `i`, and
the inverse formulas of §9.3 introduce denominators in `{2,3}` only, so the
E-branch substitution stays inside the registered denominator set. The
étale-localisation set `{2,3,5,7}` is a superset of the true `{2,3,7}` (§6); if
any solve step ever needs a *new* prime in a denominator, the halt rule in
grok46 §3.3 stands.

### 10.8 A symmetry worth testing before the solve (conditional)

Define `sigma` on the 432-basis by `r3 ↦ -r3`, `A1 ↔ A2`, `zeta42 ↦ zeta42`,
`h ↦ h`. It preserves the five relations, so it is a ring automorphism of `K0`
(verified: 40 random product/sum pairs, exact, all consistent), and it fixes
`Q(zeta42)` and `h` while sending `sqrt2 ↦ -sqrt2`. Executed facts:

```text
sigma(E(W1,W2)) = E(W2,W1)          E is sigma-symmetric under W1 <-> W2
sigma(q0) * q0  = -1                so q0^-1 = -sigma(q0), and the branch set
                                    {i^k q0} is stable under sigma composed with
                                    inversion
```

**Open, and cheap to settle from the exact rows when they exist:** whether the
29-row live set (and the 155 zero rows) is stable under
`(sigma, W1 ↔ W2)`. If it is, the solve halves and every candidate comes in a
`sigma`-pair, and the two banked frames' different branch indices (§8.3) get a
structural explanation. If it is not, that asymmetry is itself informative about
the `a00pp` specialisation. I did not test it: the exact rows do not exist yet.
This is a **conditional claim + proposed test**, not a result.

---

## 11. Separation of theorem, conditional claim, and computational recipe

**THEOREMS proved in this report** (independent of every unreviewed packet, and
of both modular frames): L1, A, L2, B, C, D, and E(1)-(3). The proofs use only
the printed defining relations. They stand even if the 184-row emitter is
wrong, if the pointbanks are wrong, and if the seven-condition story is wrong.

**Theorem F is conditional** on one input I did not re-derive: the displayed
`E = (9+5r3)A1 W1^4 + (9-5r3)A2 W2^4` from the reviewed bridge `e1b99600...`,
as quoted identically by both charged reports. Given that `E`, F is a theorem
(its proof is the five two-line identities F1-F5). If the bridge's `E` is later corrected,
F must be recomputed; the method (reduce `c` to a power of `u = A2/A1` using
`u^3 = eps^-1`) will survive most perturbations of the numerical coefficients,
but the conclusion `q ∈ K0` will not automatically.

**Evidence, not proof:** the 432-frame counts (§7 — a split `L^3` would give the
same number), the banked-ratio regression (§8.3), the `p^2` Hensel check
(§7 — consistent with, not a proof of, étaleness), and the source-hash matches
(§0).

**Recipes, not results:** the `gp` script of §9.2 (**not executed**: no PARI on
this host), the checker plan §9.3 items not marked executed, the optional
primitive-element artifact §9.3(6), and every DAG edit proposed in §10.

**Executed locally, exact, stdlib Python only:** §3.1 (cyclotomic pins and
`disc(Phi42)`), §3.2 (all base identities in `Z[x]/(Phi_168)`), §5.1 (character
certificate at 673 and the scan through 2857), §6 (frame Jacobians), §7 (frame
validation, 432-counts at both primes, `p^2` Hensel), §8.2 (all
`RadicalCoefficient` identities including the direct `E(q0,1)=0`), §8.3 (banked
regression), §9.3(5) (inverse maps), §10.8 (`sigma` automorphism spot-check).
No AWS, no network, no `jc2-lean`, no CAS.

---

## 12. Answers, in the order asked

1. **Degree-48 base.** `B = Q[zeta42,r3,h]/(Phi42, r3^2-3, 2h^2-3) ≅ Q(zeta_168)`,
   a field of degree 48, abelian over `Q`. The cyclotomic description is
   **verified**, with explicit forward map (`zeta42 ↦ zeta^4`,
   `r3 ↦ zeta^14+zeta^-14`, `h ↦ (zeta^21+zeta^-21)(zeta^14+zeta^-14)/2`) and
   explicit inverse (`zeta_168 = zeta8^5 zeta42^16`,
   `zeta8 = (1+i)h r3/3`, `i = r3(1+2 zeta42^14)/3`), both machine-checked. The
   conductor tower is `21 → 84 → 168`. (For the *full* algebra the cyclotomic
   description is **refuted**: `K0` contains the non-normal cubic `Q(cbrt 6)`,
   so `K0/Q` is not abelian and `K0` lies inside no cyclotomic field.)
2. **The two Kummer classes.** `[alpha1]` and `[alpha2]` are independent in
   `B^*/(B^*)^3`: they span `(Z/3)^2`. Every one of the eight nontrivial
   `alpha1^i alpha2^j` is a non-cube; the four inverse-pair representatives are
   `3+sqrt3` (norm 6), `3-sqrt3` (norm 6), `6` (norm 36), and `2+sqrt3` (the
   fundamental unit of `Z[sqrt3]`). Proved twice: by abelian descent to
   `Q(sqrt3)` plus norm/unit arguments, and by an engine-free cubic-residue
   character certificate at `p = 673`. **No relation of any kind exists.**
3. **Reducedness / étaleness / ramification.** `K0` is a field, hence reduced
   and finite étale over `Q`. The model over `Z[1/42]` is finite étale of rank
   432. The ramified rational primes are exactly `{2,3,7}`; the cubic layer
   ramifies above 2 and 3 only, all 7-ramification is cyclotomic, and `5` is
   unramified.
4. **The two frames.** Both are degree-1 primes of the unique factor `K0`; both
   `105337` and `105673` are `≡ 1 (mod 168)` and split completely, with exactly
   432 frames each (counted). The `105337` `p^2` frame is the unique Hensel lift
   of the `p`-frame. The 432 frames over one prime form a single Galois torsor,
   so the two registered frames are conjugate probes of the same object, not
   independent components.
5. **Certificate.** §9: six cheap layers (L0-L5), mutation battery, independent
   non-PARI checker, and an explicit deletion of the expensive
   degree-432-irreducibility step (it is a corollary, not an input). Total cost
   well under a second; **no AWS host is needed for `K0-SPLIT`**.
6. **Effect on the solve.** §10: the component machinery is deleted (`c = 1`);
   the pivot rule becomes "nonzero normal form ⟹ unit", with an 8-conjugate
   inversion recipe; the five relations generate a *maximal* ideal, which
   legalises the five-extra-variables presentation for engines without
   number-field support; and Rail E collapses from "adjoin a fourth root" to
   four explicit `K0`-rational branches with a single remaining scale unknown.
   The chart/stratum retention discipline, the rail separation, and the tier
   ladder are unchanged.

**Maximum promotion of this report:** an exact structural theorem about the
coefficient algebra `K0` and its integral model, plus one conditional theorem
about the displayed `E`-ratio. It is not a row certificate, not a point, not
raw-J existence, and not any tier above 0.
