# Hostile theorem review: D43 coefficient algebra `K0`

**UTC:** 2026-08-29
**Role:** Grok 4.6, different-model mathematical referee
**Charge:** `xmodel/d43-k0-field-theorem-hostile-review-grok46-prompt-20260829.md`
**Object:** Opus 5 primary research
`xmodel/d43-k0-splitting-primary-research-opus5-20260828.md`

No `jc2-lean`, no AWS, no PARI/GP, no heavy CAS.  All executed checks below
are bounded stdlib Python (exact `int`/`Fraction` polynomial arithmetic, a
separate cyclotomic engine for Theorem A, cubic-residue characters, `F_p`
frame/Hensel/root counts, and the committed `RadicalCoefficient` normalizer
for the displayed quotient).  Coordinator paper-proof adjudication is treated
as non-evidence.

---

## Overall

The coefficient-algebra theorem survives a first-principles attack.  A
product-algebra countermodel, a missed Kummer relation, a Galois-stability
gap, a ramification counterexample at 5, a nonmaximal-order collapse of the
`Z[1/42]` claim, and a sign/branch error in `q0` were attempted and failed.

The 432-frame counts are **not** a proof of fieldness; they are a consistency
check, and the charged report already says so.  Theorem F is **conditional**
on the hashed displayed `E`.  The §9 GP script is an unexecuted recipe.

| # | claim | verdict |
|---|---|---|
| 1 | free rank 432 of the quotient; free rank 48 of the pre-cubic base | **CONFIRMED** |
| 2 | `B ≅ Q(zeta_168)`, both maps, degree 48, every cyclotomic exponent identity | **CONFIRMED** |
| 3 | abelian descent L2, and/or `[3±sqrt3]` span `(Z/3)^2`; characters at 673 and a second prime | **CONFIRMED** |
| 4 | `K0` is one field of degree 432, Galois, nonabelian, idempotents `{0,1}` | **CONFIRMED** |
| 5 | finite étale `Z[1/42]` model; ramified rational primes exactly `{2,3,7}` | **CONFIRMED** |
| 6 | both registered frames; complete split/count 432; unique registered `p^2` lift | **CONFIRMED** |
| 7 | conditional on literal `E`: `u^3=2-sqrt3`, `c=-u^10`, `q0`, `q0^4=c`, four branches, four-term form, both bank regressions | **CONFIRMED** (conditional) |
| 8 | solve-graph consequences (component deletion, NF inversion, maximal ideal, remaining Fitting/chart/claim debt) | **CONFIRMED** as coefficient-algebra consequences, with the residual obligations below |

Maximum promotion of the charged report, after this review: an exact
structural theorem about the `Q`-algebra `K0` and its `Z[1/42]` model, plus
one theorem about the displayed `E`-ratio **conditional** on the hashed
bridge polynomial.  It is not a row certificate, not a characteristic-zero
point, not raw-J existence, not template survival, not a Fitting solve, and
not JC2.

---

## 0. Custody (independently recomputed)

| file | SHA-256 | match |
|---|---|---|
| `xmodel/d43-k0-splitting-primary-research-opus5-20260828.md` | `6d3d53c20387d324766daaf40eb502df42d9e2776c6ab6053041bc1f3dee1430` | charge |
| `cases/d43_common_integral_emitter.py` | `5420b5c0b4164c719e98316cade96c094c2945a6fed8bad3ac0926771855984d` | charged report §0 |
| `xmodel/d43-e5-e6-elimination-bridge-gpt56-20260828.md` | `e1b99600b01f91f7b95df4f7f969481efa1e7b1ee377e83156f3f6b6a8e3c863` | full hash of the `e1b99600...` pin |
| `cases/d43_exact_sparse_rows_v2_20260828/selected_rows_v2.py` | `9fc9bd7a365827ddba2c1ba45cbb34870d6f2d71c9d3eecb6b242d46e00990b2` | charged report §0 |
| `xmodel/d43-seven-w-elimination-algorithm-grok46-20260828.md` | `8b748f388c53868ccfe856135db2f4251a066db01115641d299f08939f3dcc26` | charged report §0 |
| `xmodel/d43-a00pp-tail-elimination-independent-audit-gpt56-r1-20260828.md` | `e19a3d0eaad79ea47fc08fb7c406a9045818671776b535950a285c9813f7f0f8` | charged report §0 |
| `xmodel/d43-direct-exact-sparse-source-preflight-gpt56-20260828-v2.md` | `e7000a748782e579f2108a8aa913684765d82bba8639613b6f6e4864e6fb2202` | charged report §0 |
| `cases/d43_full_pointbank_p105337.pkl` | `bb0f13b61616c486116027e284483a4fb0f529f8df2dca7f728d56584d98fcbb` | charged report §8.3 |
| `cases/d43_full_pointbank_p105673.pkl` | `b933cdb5b72bd4073da0cb82150db768f6b4607d5cd29d3d4aec0fe22ce5bcc3` | charged report §8.3 |

Displayed relations in the emitter (`PHI42`, `BASIS_SHAPE=(12,2,3,3,2)`,
`BASIS_RANK=432`, `r3^2=3`, `A1^3=3+r3`, `A2^3=3-r3`, `2h^2=3`) are the
literal relations of
`selected_rows_v2.py:59-72` (`field_claim: null`).  The rewriting in
`RadicalCoefficient._normalize` is exactly those five leading-term rules.

Displayed `E` in the hashed bridge, used verbatim as the conditional input:

```text
E := (9+5*r)*A1*W1^4 + (9-5*r)*A2*W2^4 = 0.
```

Non-load-bearing prose defect, recorded so it cannot be recycled as a source
pin: the emitter comment at `d43_common_integral_emitter.py:33-35` says `PHI42`
is **not** `z^42-1`.  The charged report's §3.1 sentence that the file's
comment “claims” `x^42-1` is a misread.  The polynomial tuple is nevertheless
the genuine `Phi_42`.

---

## 1. Free ranks 432 and 48 — CONFIRMED

**Lemma L1, as charged.**  Over `Q`, iterate “`R[t]/(f)` is free of rank
`deg f` for monic `f`”:

- `Q[z]/(Phi_42)` free of rank 12 (`Phi_42` monic of degree 12);
- adjoin `r` by `r^2-3` (monic, rank 2);
- adjoin `A1` by `A1^3-(3+r)` (monic over the previous ring, rank 3);
- adjoin `A2` by `A2^3-(3-r)` (monic, rank 3);
- adjoin `h` by `2h^2-3`.  Over `Q`, `2` is a unit, so the ideal equals
  `(h^2-3/2)` with monic generator (rank 2).

Product `12*2*3*3*2=432`.  The pre-cubic base `B` stops before `A1,A2`, rank
`12*2*2=48`.  Reducibility of any layer polynomial does not drop the vector-
space rank: it would only drop reducedness/fieldness, which is the content of
items 2–4, not of L1.

**Attack: extra relations / non-confluence.**  The leading-term monomials
`z^{12}, r^2, A1^3, A2^3, h^2` are a triangular regular sequence in separate
variables, with tails of the two cubics linear in `r`.  The associated graded
is `Q[z,r,A1,A2,h]/(z^{12},r^2,A1^3,A2^3,h^2)` of dimension 432, so the
rewriting spans and does not collapse.  Tails involving `r` are reduced by
`r^2-3` and do not create a further syzygy among the monomials of the
claimed shape.  This is the same reduction the emitter implements.

L1 is a statement about the presented `Q`-algebra, before irreducibility.

---

## 2. `B ≅ Q(zeta_168)` — CONFIRMED

Independently rebuilt `Phi_n` by exact monic division of `x^n-1` by
`∏_{d|n, d<n} Phi_d`, working in `Z[x]`.

```text
Phi_42  = (1,1,0,-1,-1,0,1,0,-1,-1,0,1,1)   MATCH source PHI42
deg Phi_168 = 48 = phi(168)
Phi_168(x) == Phi_42(x^4)                    True
Res(Phi_42, Phi_42') = 205924456521
                     = 3^6 * 7^10            True, and odd
```

The identity `Phi_n(x^k)=Phi_{nk}(x)` when every prime dividing `k` already
divides `n` gives `Phi_42(x^4)=Phi_168(x)` independently of the division
check; both were run.

**Forward map**, executed in a separate engine `Q[x]/(Phi_168)`, not in
`RadicalCoefficient`:

```text
zeta42 |-> z^4
r3     |-> z^14 + z^154
h      |-> (z^21 + z^147)*(z^14 + z^154)/2
```

```text
Phi_42(z^4) == 0                         True
ord(z^4) == 42                           True  (z^168==1, z^84==-1, z^56!=1)
(z^14+z^154)^2 == 3                      True
(z^21+z^147)^2 == 2                      True
2 h^2 == 3                               True
```

These are the three defining relations of `B`, so the map is a well-defined
`Q`-algebra homomorphism `B -> Q(zeta_168)`.  (Fieldness of the target uses
the standard theorem that cyclotomic polynomials are irreducible over `Q`.
That is a named theorem, not an unexecuted factorisation of this tower.)

**Inverse / generation.**  Put `zeta3 = (z^4)^{14} = z^{56}` and
`i = r3*(1+2*zeta3)/3`.  Executed:

```text
i^2 == -1                                True
zeta8 := (1+i)*h*r3/3  ==  z^21          True
zeta8^5 * (z^4)^16     ==  z             True
```

The exponents are CRT, and they are elementary:

```text
21*5 + 56*2 + 24*5 = 337 = 2*168 + 1
zeta8^5 * zeta3^2 * zeta7^5 = z^{105+112+120} = z^{337} = z
zeta3 = zeta42^{14}, zeta7 = zeta42^6
zeta3^2 zeta7^5 = zeta42^{28+30} = zeta42^{58} = zeta42^{16}
zeta8^5 * zeta42^{16} = z^{105} * z^{64} = z^{169} = z
```

The load-bearing computational identity is `zeta8 == z^{21}`; the rest is
exponent arithmetic in the cyclic group of order 168.  Both were checked.

**Injectivity.**  L1 gives `dim_Q B = 48 = [Q(zeta_168):Q]`.  A surjective
linear map between finite-dimensional vector spaces of equal dimension is
bijective.  Hence an isomorphism of `Q`-algebras, and `B` is a field.

**Conductor tower**, generation rather than a second irreducibility test:

```text
Q(zeta42) = Q(zeta21)                 degree 12, conductor 21
Q(zeta42, r3) = Q(zeta84)             degree 24, conductor 84
Q(zeta42, r3, h) = Q(zeta168)         degree 48, conductor 168
```

Cross-check, independent of generation: `disc(Q(sqrt3))=12`, so 2 ramifies
there, while `disc(Phi_42)` is odd, so 2 is unramified in `Q(zeta42)`, hence
`sqrt3 ∉ Q(zeta42)`.  Conductors: `12 ∤ 42`, `24 ∤ 84`, while `12|168` and
`24|168`.

No collapse at the `r3` or `h` layer.

---

## 3. Kummer classes span `(Z/3)^2` — CONFIRMED

`mu_3 ⊂ B` because `3|168`.  The eight nontrivial classes in
`<alpha1,alpha2> ⊂ B^*/(B^*)^3` are inverse-pairs of the four representatives
`alpha1=3+sqrt3`, `alpha2=3-sqrt3`, `alpha1 alpha2=6`,
`alpha1/alpha2 = 2+sqrt3`.  The last identity is elementary:

```text
(3+sqrt3)/(3-sqrt3) = (3+sqrt3)^2 / 6 = (12+6 sqrt3)/6 = 2+sqrt3.
```

### 3.1 Lemma L2 (abelian descent)

The charged proof is correct.  If `x^3 = beta ∈ Q(sqrt3)^*` with `x ∈ F` and
`t^3-beta` irreducible over `Q(sqrt3)`, then `E=Q(sqrt3)(x)` has degree 6
over `Q`.  Abelian `F/Q` forces every subextension Galois over `Q`, so `E/Q`
is Galois, so `E/Q(sqrt3)` is Galois of degree 3, so `t^3-beta` splits in `E`,
so `zeta3 ∈ E`, so `Q(zeta_12)=Q(zeta3,sqrt3) ⊆ E`, so `4|6`.

Cubics over a field are irreducible iff they have no root, so there is no
hidden reducible-without-root case.  Characteristic is 0.  The degree-6
conclusion cannot drop to 3: `Q(cbrt beta)` cannot contain `Q(sqrt3)`
because 2 does not divide 3.

**Attack: cyclotomic twist.**  A relation `[alpha1^i alpha2^j]=0` in
`B^*/(B^*)^3` is precisely the statement that a fixed element of `Q(sqrt3)^*`
is a cube in `B`.  L2 applies to that element.  Twisting by a cyclotomic
unit does not create a new relation among these two classes: if
`alpha1/alpha2 = zeta * y^3` with `y ∈ B`, then `eps` is a cube in `B` after
absorbing `zeta` only if `[eps]=0`, which L2 reduces to `Q(sqrt3)` and
refutes.

### 3.2 The four non-cubes in `Q(sqrt3)`

Norms for `Q(sqrt3)/Q`:

- `N(3±sqrt3)=6`, and `v_2(6)=v_3(6)=1` are not divisible by 3, so 6 is not
  a cube in `Q^*`.  A cube in `Q(sqrt3)^*` has cube norm.
- `N(6)=36=2^2 3^2`, same obstruction.  Equivalently `[Q(cbrt 6):Q]=3` does
  not divide 2.
- `eps=2+sqrt3` has norm 1, so the norm test is blind.  `O=Z[sqrt3]` is the
  ring of integers (`d=3≡3 mod 4`).  The negative Pell equation
  `a^2-3b^2=-1` is impossible because squares mod 3 are `{0,1}` and
  `-1≡2 mod 3`; the fundamental unit is therefore the smallest solution of
  `a^2-3b^2=+1` with `b=1`, namely `a=2`.  Unit group `{± eps^n}`.

  If `eps=y^3` with `y ∈ Q(sqrt3)^*`, then for every finite prime ideal
  `3 v_p(y)=v_p(eps)=0`, so `v_p(y)=0`, so `y ∈ O^*`.  (The charged phrasing
  “`(y)^3=(1)` as fractional ideals, so `y∈O^*`” is this valuation argument;
  it does not need class number 1.)  Then `y=±eps^n` and `±eps^{3n}=eps`.
  Both real embeddings of `eps` are positive, so the sign is `+` and `3n=1`.

L2 plus these four facts give Theorem B: `Delta ≅ (Z/3)^2`.

### 3.3 Cubic characters, recomputed

This proof does not use L2.  It does use that algebra maps `B -> F_p` exist
for `p≡1 (mod 168)`, which they do at the level of the presented algebra
(`Phi_42` splits, `3` and `3/2` are squares because `p≡1 (mod 168)` forces
`p≡1 (mod 8)` and `p≡1 (mod 12)`).  The value `chi(3±r)` depends only on `r`.
If `alpha1^i alpha2^j` is a cube in `B`, it is a cube in every `F_p` image.

Executed, `chi(x)=x^{(p-1)/3} ∈ mu_3(F_p)`, discrete log in a fixed order-3
generator:

```text
p=673 = 4*168+1, prime, 3 is square with roots {26,647}
  r=26  :  (a,b)=(2,0)     chi(3+r)=255, chi(3-r)=1
  r=647 :  (a,b)=(0,2)     chi(3+r)=1,   chi(3-r)=255
  det = 2*2-0*0 = 4 ≡ 1 (mod 3) ≠ 0

p=1009 = 6*168+1, prime, roots {149,860}
  r=149 :  (a,b)=(0,1)
  r=860 :  (a,b)=(1,0)
  det ≡ 2 (mod 3) ≠ 0
```

The 673 vectors match the charged display.  The 1009 vectors were not fully
printed there; they are the standard basis of `F_3^2` and are a strictly
cleaner certificate.  Either pair kills every nontrivial `(i,j)`.

**Hidden denominators / specialisation.**  `p ∤ 6`, so `3±r ≠ 0`.  No
division by a vanishing `alpha_k`.  The character is a power in `F_p`, not a
ratio of algebraic integers with hidden content.  The argument never
inverts 3 in `F_p` beyond the already-available `(p-1)/3`.  Both square
roots of 3 occur as residue values of the presented generator `r3`, without
needing Galois-ness of `B` in advance.

**Attack: silent primes.**  Not every `p≡1 (mod 168)` is a certificate.
Executed counterexample to a naive “any such `p` works”:

```text
p=337 = 2*168+1, prime
  both frames: (a,b)=(0,0), det=0
```

Among primes that split completely in `Q(zeta_168)`, Frobenius lands in
`Gal(K0/B)≅(Z/3)^2` of order 9, so density `1/9` are complete-split in `K0`
and give the zero character.  The registered primes `105337` and `105673`
are of this kind (item 6).  That is why the charged refusal to read
independence off the two campaign frames is correct, and why a second
non-split prime is load-bearing.  1009 is such a prime.  337 is not.

No missed relation among the two classes exists.

---

## 4. `K0` is one field of degree 432 — CONFIRMED

`K0 = B[A1,A2]/(A1^3-alpha1, A2^3-alpha2)` is free of rank 9 over the field
`B` (L1 + item 2).  Kummer theory: `B` contains `mu_3`, `Delta` has order 9,
so `L = B(cbrt alpha1, cbrt alpha2)` has `[L:B]=9`.  The tautological
`B`-algebra map `K0 -> L` is a surjection of 9-dimensional `B`-vector spaces,
hence an isomorphism.  Thus `K0` is a field, `[K0:Q]=48*9=432`.

**Product-algebra countermodel, attempted.**  If `Delta` had order 3, the
same presentation would be free of rank 9 over `B` mapping onto a degree-3
extension, and the kernel would realise a product (typically three copies of
a degree-144 field).  Item 3 forbids every such collapse: neither cubic
splits, and they are linearly independent over `F_3`.  If `B` itself split,
`K0` would split; item 2 forbids that.  There is no remaining product
decomposition over `Q`.

**Idempotents.**  A field has only `0,1`.  These are the idempotents of `K0`
as a `Q`-algebra.  (After base change to `Q-bar` one has 432 geometric
points; that is Galois splitting, not a product over `Q`.)

**Galois.**  Any `Q`-embedding of `K0` into `Q-bar` preserves `B` (cyclotomic,
Galois), sends `r3` to `±r3`, and sends `A1` to a cube root of `3±r3`.  Those
cube roots are `zeta3^k A1` or `zeta3^k A2`, all already in `K0` because
`mu_3 ⊂ B`.  Same for `A2` and for `h |-> ±h`.  Equivalently, `Delta` is
`Gal(B/Q)`-stable because the nontrivial action on `Q(sqrt3)` swaps
`alpha1 ↔ alpha2`.

**Nonabelian.**  `(A1 A2)^3 = (3+r3)(3-r3)=6`, so `Q(cbrt 6) ⊆ K0` is a
non-normal cubic over `Q`.  Subfields of abelian extensions are Galois over
the base.  In particular `K0` lies in no cyclotomic field.

**Second generators.**  `<6, eps>` is the image of `Delta` under the
`F_3`-matrix `[[1,1],[1,-1]]` of determinant `-2≡1 (mod 3)`.  So
`K0 = B(cbrt 6, cbrt(2+sqrt3))` as well.

The fibre-product description of `Gal(K0/Q)` in the charged §5.2 is
bookkeeping, not used by the fieldness proof.  The degree count it relies on
does check: L2 applies with `F=Q(zeta_12)` in place of `B`, so the same
`Delta` is independent over `Q(zeta_12)`, the field
`Q(zeta_12, cbrt alpha1, cbrt alpha2)` has degree 36, and
`432=48*36/[B∩F:Q]` forces `[B∩F:Q]=4= [Q(zeta_12):Q]`.

---

## 5. Finite étaleness and ramified set `{2,3,7}` — CONFIRMED

**Reducedness / étaleness over `Q`.**  Immediate from item 4.

**The model**
`A = Z[1/42][z,r,A1,A2,h]/(Phi_42, r^2-3, A1^3-alpha1, A2^3-alpha2, 2h^2-3)`.

Over `Z[1/42]`, `2` is a unit, so `(2h^2-3)=(h^2-3/2)` and the last generator
may be taken monic.  Also `h=sqrt6/2` is not an algebraic integer, but after
inverting 2 one has `Z[1/42][h]=Z[1/42][sqrt6]`.  That is the only
nonmaximal-order / non-integral-generator subtlety, and inverting `42`
removes it.

Successive criterion: `R -> R[t]/(f)` is étale when `f` is monic and
`disc(f)` is a unit.

| layer | monic model over the previous ring | disc | inverted |
|---|---|---|---|
| `zeta42` | `Phi_42` | `3^6 7^{10}` (item 2) | 3,7 |
| `r3` | `r^2-3` | 12 | 2,3 |
| `A1` | `A1^3-alpha1` | `-27 alpha1^2` | 3, and `alpha1` a unit |
| `A2` | `A2^3-alpha2` | `-27 alpha2^2` | 3, and `alpha2` a unit |
| `h` | `h^2-3/2` | 6 | 2,3 |

`alpha1 alpha2=6` is a unit of `Z[1/42]`, hence of every later ring, and in
any commutative ring a factor of a unit is a unit.  So both cubic
discriminants are units.  Inverting `42=2*3*7` is necessary and sufficient
for this presentation.  Composite of étale maps is étale, and each step is
finite free, so `A` is finite étale of rank 432 over `Z[1/42]`.

**Attack: nonmaximal order at 5.**  No layer discriminant is divisible by 5,
so the composite remains étale at 5.  An étale `Z_{(5)}`-order is maximal
and unramified.  The Kummer layer cannot reintroduce 5: `N(alpha1)=6` is not
divisible by 5, `eps` is a unit, and `n=3≠5`, so the Kummer extension of `B`
is tame and unramified at 5.  Independently, `disc(x^3-6)=-27*36` is
supported on `{2,3}`, and `5` does not divide 168.

**Attack: Kummer ramification above 2 invalidating the upper bound.**  For a
prime `q` of `B` not dividing 3, `K0/B` ramifies iff some `v_q(alpha)` is not
divisible by 3.  In `Q(sqrt3)`, `(1+sqrt3)^2 = 2 eps` with `eps` a unit, so
the unique prime above 2 is `(1+sqrt3)` and `v(alpha1)=1` there.  Extending
to `B`, `e_2(B)/e_2(Q(sqrt3))=4/2=2`, so `v_q(alpha1)=2` above 2, and
`2 ≢ 0 (mod 3)`.  Above 3, `alpha1=sqrt3(1+sqrt3)` has `v=1` and
`e_3(B)=e_3(Q(sqrt3))=2`, so `v_q(alpha1)=1`.  Above 7, `v_q(alpha1)=0`.
The cubic layer ramifies at 2 and 3 and not at 7; all 7-ramification is
cyclotomic.  None of this lets a prime outside `{2,3,7}` ramify, and it does
not break étaleness over `Z[1/42]`.

**Exact ramified set.**  Upper bound from étaleness of `A`: only 2,3,7.
Lower bound: 3 and 7 ramify in `Q(zeta42)⊂K0`; 2 ramifies in `Q(sqrt3)⊂K0`.
So exactly `{2,3,7}`.

The emitter constant `ETALE_LOCALIZATION_PRIMES=(2,3,5,7)` is a safe
superset.  5 is a Newton/source-denominator prime, not a ramified prime.
A derivation of “ramified at 2,3,5,7” from that constant would be wrong;
the charged report does not make that derivation.

---

## 6. Frames, complete splitting, unique `p^2` lift — CONFIRMED

Executed on the literal registered frames
`(p, z, r, A1, A2, h)`:

```text
105337 = 627*168+1,  frame (2779, 795, 50630, 10114, 50267)
105673 = 629*168+1,  frame (13862, 14686, 38664, 46664, 35053)
```

Both satisfy the five relations, `zeta42` has exact order 42, and the five
gate quantities `Phi_42', 2r, 3 A1^2, 3 A2^2, 4h` are units.  At 105337 those
derivatives are exactly the charged tuple `(72846, 1590, 63015, 32307, 95731)`.

A registered frame is a `Z[1/42]`-algebra map `A -> F_p`, hence a degree-1
prime of the unique factor `K0` (item 4), unramified because `p ∤ 42`
(item 5).  Galois of degree 432 plus one degree-1 prime implies complete
splitting: 432 primes, all degree 1.

**Count 432, executed, and what it is not.**  Direct `F_p` census:

```text
p=105337 : #Phi_42 roots=12, #h=2, both r in {795,104542} have
           (3±r) cubic residues, #A1=#A2=3, sum_r #A1 #A2=18, TOTAL=432
p=105673 : #Phi_42 roots=12, #h=2, both r in {14686,90987} have
           (3±r) cubic residues, TOTAL=432
```

This is the same number a split `L^3` with `[L:Q]=144` would produce.  It is
a consistency check of items 4–5, not a proof of fieldness.  The charged
report already makes that distinction; this review does not upgrade it.

**Jacobian / unique Hensel lift.**  The five defining maps
`(z,r,A1,A2,h) -> (Phi_42(z), r^2-3, A1^3-(3+r), A2^3-(3-r), 2h^2-3)` have
Jacobian that is **not** diagonal: `∂(A1^3-3-r)/∂r=-1` and
`∂(A2^3-3+r)/∂r=+1`.  The determinant is nevertheless

```text
det J = Phi_42'(z) * 2r * 3 A1^2 * 3 A2^2 * 4h
```

up to the unit `1` in the `3×3` block `(r,A1,A2)`.  The frame gate therefore
does certify `det J ∈ F_p^*`, so the registered `p`-point has a unique lift
to `Z/p^2`.  Executed on `REGISTERED_P2_FRAME_105337`:

```text
reduces mod 105337 to the registered p-frame     True
all five relations vanish mod 105337^2           True
```

Uniqueness is étale Hensel (item 5 + Jacobian units), not “a lift was
found”.  It is uniqueness over the registered `p`-frame, not uniqueness of
`p^2`-points of `A` (there are 432 such lifts, one per `p`-frame).

The 432 frames over one `p` are a single `Gal(K0/Q)`-torsor.  Agreement of
the two campaign primes is conjugate evidence, not two components.

---

## 7. Conditional `q0` theorem — CONFIRMED (conditional on hashed `E`)

### 7.1 The polynomial `E` is the literal hashed input

The bridge `e1b99600b01f91f7b95df4f7f969481efa1e7b1ee377e83156f3f6b6a8e3c863`
displays `E=(9+5r)A1 W1^4+(9-5r)A2 W2^4`.  The E5-to-`E` coefficient
identities in that file are correct over `Q(sqrt3)` with `a1=3+r`, `a2=3-r`,
`b=4`:

```text
a1^2 (a2-b) = -6(5+3r)
a2^2 (a1-b) =  6(3r-5)
```

Equating the two E5 formulae for `HM` and multiplying by the unit `r`
produces `E`.  Conversely `E` reconstructs those formulae.  This review does
**not** re-derive E5 from a template packet; Theorem F is conditional on
that displayed form.

From `E` and `q=W1/W2`, using `(9+5r)(9-5r)=6`:

```text
c = (15 r3 - 26) * A2/A1.
```

### 7.2 Identities F1–F5, attacked for signs

Hand identities in `Q(sqrt3)` and `Q(i,sqrt3)`, then replayed in the
committed 432-basis:

```text
(F1) u^3 = (3-r3)/(3+r3) = (3-r3)^2/6 = 2-r3           True
(F2) (2-r3)^3 = 26-15 r3,  so 15 r3-26 = -(2-r3)^3     True
(F3) c = (15 r3-26) u = -u^{10}                        True
(F4) s=(1+i)(r3-1)/2,  s^2 = i(2-r3)                   True
     because (1+i)^2=2i and (r3-1)^2=4-2r3
(F5) q0=u s,  q0^2 = i u^5,  q0^4 = -u^{10} = c        True
```

`i` is the charged element `r3(1+2 zeta42^{14})/3`; `i^2=-1` holds in both
engines (item 2 and the 432-basis).  Replacing `i` by `-i` still yields a
fourth root of `c`; the four roots are `q0 mu_4`, and `mu_4 ⊂ K0`.

**Direct substitution, not routed through `c=-u^{10}`:**
`E(i^k q0, 1)=0` for `k=0,1,2,3`, all four branches pairwise distinct.
`q0` is a unit (`q0 * (-sigma(q0)) = 1` with the charged involution
`r3 |-> -r3`, `A1 ↔ A2`).

**Sign/branch attack, failed.**  The factor `(r3-1)` rather than `(1-r3)`
is the choice of one fourth root; the opposite sign is `-q0`, already among
the four branches.  Direct `E(q0,1)=0` would have failed on a wrong `i` or a
wrong linear form of `s`.  It did not.

### 7.3 Four-term normal form

Executed normal form, denominators in `{2,3}` only:

```text
q0 = A1^2 A2 * ( -5/6 + (1/2) r3 + (2/3) zeta42^7 - (1/3) zeta42^7 r3 )
```

This is not an independent generator choice: `zeta42^{14}` reduces through
`Phi_42` into lower degree, and `zeta42^7=zeta_6=(1+i r3)/2` converts the
`zeta3`-form

```text
(r3 - 1 + 4 zeta3 - 2 r3 zeta3)/6
```

into the displayed `zeta42^7`-form by an identity in `Q(i,sqrt3)`.  Both
expressions were matched.  The four-term vector is therefore a corollary of
F1–F5 plus `Phi_42`-reduction, not an extra numerical accident.

### 7.4 Pointbank regressions — evidence, not proof

Pickle status on both banks is `INTERNAL / UNREVIEWED / MOD-p`.  Reading
only `cell_values['W1','W2','uW1','uW2']` and specialising the exact `q0`
at the registered frames:

```text
p=105337: W1=31931, W2=9457,  W1 uW1≡1, W2 uW2≡1
          W1/W2 ≡ 7210
          q0-branches = [73053, 98127, 32284, 7210]   match at k=3
          E(W1,W2)≡0
p=105673: W1=8021,  W2=20111, W1 uW1≡1, W2 uW2≡1
          W1/W2 ≡ 14755
          q0-branches = [14755, 101655, 90918, 4018]  match at k=0
          E(W1,W2)≡0
```

Both banked ratios lie on a `q0`-branch.  Branch indices are
frame-dependent and are not portable.  This confirms that Theorem F names
the right object for these two modular points; it does not construct a
characteristic-zero point and does not prove E5.

If the hashed `E` is later corrected, F1–F5 must be recomputed.  The method
(reduce `c` to a power of `u`) will often survive coefficient perturbation;
the conclusion `q ∈ K0` will not automatically.

---

## 8. Solve-graph consequences — CONFIRMED, with residual obligations

These are consequences of items 4 and 7, not independent theorems.

**Component splitting that may be deleted.**  Over `Q`, `c=1`: there is no
product decomposition of `K0`, no per-factor `K_i`, no G5 (“components that
miss the registered frames”).  `K0-SPLIT` as a product-decomposition job is
vacuous and may be replaced by a replay of the fieldness certificate.  The
§9 GP script is **not** that replay (item 9 below).  Reissuing `FITTING-A`
once per coefficient factor is also vacuous.  Tower factorisation aimed at
splitting `K0` (charged D2) is unnecessary.

**When a nonzero normal form may be inverted.**  In the field `K0`, the
432-term monomial support of L1 is a `Q`-basis, so `a ∈ K0` is a unit if and
only if that normal form is the nonzero vector.  No annihilator computation
and no Bézout search is required **for elements of `K0`**.  Nonvanishing at
the two modular frames remains insufficient: those frames are two of 432
degree-1 primes, and a nonzero `a` may lie in either.  The Gal(`K0/B`)
inversion recipe (nine conjugates, norm in `Q(zeta_168)`) is a correct
algorithm for field inversion; it is not needed to know that inversion is
legal.

This invertibility statement is about `K0` as a `Q`-algebra.  It is not a
statement about `A` as a `Z[1/42]`-algebra, and it is not a statement about
zero-divisors in `K0[W1,W2,...]`.

**Five relations as a maximal ideal.**  Item 4 is exactly the statement that

```text
(Phi_42, r^2-3, A1^3-(3+r), A2^3-(3-r), 2h^2-3)
```

is a maximal ideal of `Q[z,r,A1,A2,h]`.  Adjoining those five generators
alongside the `W`-equations therefore introduces no extra coefficient
components.  That is a genuine gift to engines that cannot work in a
degree-432 number field.  It does not make the `W`-side ideal maximal, prime,
or zero-dimensional.

**Fitting / chart / claim obligations that remain.**  Being a field deletes
a coefficient-algebra hazard only.  Still required, and still unproved by
the charged report:

- Fitting/determinantal chart retention and `V(Delta)` for every inverted
  minor;
- the tail-Jacobian drop locus, `W1=0`, `W2=0`, and Rail J / Rail E
  separation;
- G1 (`29-22=7` is not an elimination ideal), G2, G3, G4, G6, G7, G8, G9,
  G10;
- a sealed 184-row exact packet;
- reconstruction replay of literal E5/E6/unit from the bridge, if that
  bridge is used as a solver contract;
- all four `q0`-branches retained, with `sigma=0` excluded by localisation;
- no transport of modular identities to characteristic zero;
- nothing on Q0, `H_F`, NF equivalence, all-depth compatibility, Keller, or
  JC2.

Rail E collapsing to four explicit `K0`-rational branches with a single
remaining scale is a valid **conditional** rewrite, given item 7.  The
`+42` inhomogeneity at `(eta,slot)=(0,20)` remains the only scale pin, as
in the charged design memo.

The involution `sigma: r3 |-> -r3, A1 ↔ A2` is a ring automorphism of `K0`
and satisfies `sigma(q0) q0 = -1`.  Stability of the 29 live rows under
`(sigma, W1 ↔ W2)` is **open**: the exact rows do not exist yet.  That is
a proposed test, not a result.

---

## Theorem / conditional / evidence / recipe

**Theorems, independent of the 184-row packet, of both modular frames, and
of the seven-condition story:** L1, A (`B ≅ Q(zeta_168)`), L2, B (Kummer
independence), C (fieldness, Galois, nonabelian, idempotents `{0,1}`), D
(étale `Z[1/42]` model, ramified set `{2,3,7}`), and E(1)–(3) as
structural facts about the two registered primes (the complete-split
count as a Galois consequence; the brute-force 432 as a consistency check).

**Conditional theorem:** F, on the hashed displayed `E` only.

**Evidence, not proof:** 432-frame counts; both pointbank ratio regressions;
the `p^2` residue check (consistent with, not a proof of, étaleness); source
hash matches.

**Recipe, not a result:** `k0_split_cert.gp` in the charged §9.2.  It was
not executed by the producer (`which gp` is not PARI).  It was not executed
here.  Layers L0, L1, L3, L4, L5 of that script overlap checks this review
did run in stdlib Python; layer L2 (`nffactor` over `Q(sqrt3)` and over
`Q(zeta_168)`) is unnecessary for the theorem (L2 + characters already
prove B) and remains unreplayed.  The optional `rnfequation` absolute
primitive element was not produced.  Mutation-battery items that this
review did exercise independently: source `PHI42` pin, generation identity
`zeta8^5 z42^{16}=z`, character rank at 673 and 1009, degeneracy at 337 and
at the registered primes, frame relations and Jacobian units, `q0`
four-term coefficients, and direct `E(q0,1)=0`.

---

## Maximum promotion allowed, and remaining debt

**Allowed.**  Cite `K0` as a number field of degree 432, Galois and
nonabelian over `Q`, equal to
`Q(zeta_168, cbrt(3+sqrt3), cbrt(3-sqrt3))`, with integral model finite
étale of rank 432 over `Z[1/42]` and ramified rational primes `{2,3,7}`.
Cite the displayed `E`-ratio as splitting completely over `K0` on four
explicit branches, **conditional** on the hashed bridge polynomial.

**Forbidden.**  Deriving fieldness from the two frames; deriving any
`W`-side emptiness, rank, or scale polynomial from fieldness; treating the
unexecuted GP script as a certificate; promoting this review, or the charged
report, to a D43 row/point/template/Keller/JC2 result.

**Artifact / replay debt (not theorem defects):**

1. PARI/GP replay of the charged §9.2, on a host that actually has PARI.
   Syntactic/API risk in `znlog` / `znprimroot` wrapping is untested.
2. A sealed different-engine certificate packet with fail-closed mutations.
   A producer prompt for such a packet exists
   (`xmodel/d43-k0-field-certificate-r1-opus5-prompt-20260828.md`) and is
   outside this write set; it is not a substitute for replay.
3. Optional absolute primitive element and inverse maps in `Q[t]/(m)`.
   Unnecessary for the theorem; still absent as an artifact.
4. Exact 29-row / 184-row packet, still unsealed.  `sigma`-stability of the
   live rows is untestable until those rows exist.
5. Fitting-A, determinantal charts, `V(Delta)`, tail-Jacobian drop, rail
   separation, and G1–G4, G6–G10, unchanged.
6. Literal E5/E6 reconstruction replay, if the bridge is used operationally.
7. Pointbanks remain `INTERNAL / UNREVIEWED / MOD-p`.
8. No AWS job is authorised or required for the coefficient-algebra theorem.
   An AWS PARI replay of debt (1) is optional corroboration, not a
   promotion gate for items 1–5.

No canonical ledger was edited.

The SHA-256 of this review file is the digest of the on-disk bytes of

```text
xmodel/d43-k0-field-theorem-hostile-review-grok46-20260829.md
```

computed after the final write, recorded immediately below.
<!-- self-hash -->
877e451f33b24b7714c712404401f11b35b6621e80400e791c4b54cfbe5078fd  report body above this delimiter
