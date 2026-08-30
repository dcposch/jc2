# Hostile review: complete-base `A1` controls and the two-sided successor

Date: 2026-08-30 UTC  
Reviewer: Sol 5.6 Ultra (`a1_p1_degree_hostile_review` lane)  
Frozen producer:

```text
xmodel/bd-a2-a1-p1-degree-controls-sol56-20260830.md
full SHA-256     8cb874927c6bdc9a081abaa6e67c8b98adaa583b749453eeb4f5be51ef15de8e
body SHA-256     0fdef779643fd98fe8774ea01138bc35023c79aa063b6749a14249ce9898139c
manifest SHA-256 0fb2d30642be5b1b6595110094759436359eb0b6e23416935e856f0538dc842d
```

Review status: **INDEPENDENT SAME-MODEL HOSTILE REVIEW; NOT A
DIFFERENT-MODEL PROMOTION REVIEW**.

## 0. Verdict

**CONFIRM WITH CORRECTIONS.**  The report's central negative conclusion is
correct:

```text
degree(g_1)>1, even together with codimension-one surjectivity of
g_1:A2 -> X, does not by itself contradict a complete-base A1 ruling.
```

The exact source statements support the advertised Galois equal-multiplicity
controls and the non-Galois divisible-multiplicity controls, and Lemma 2.7
really does state exact degree `m_2`.  The proposed shift from the first arrow
to the full etale sandwich is therefore mathematically sound.

Three repairs should accompany integration.

1. The packet instantiates Lemma 2.7 at `(m_1,m_2)=(2,4)` without separately
   citing or constructing a cyclic `A1`-fiber space with that multiplicity
   pair.  The lemma is conditional on such an `X`.  Add a primary existence
   citation or a standard ruled-boundary construction.  Until that pin is
   supplied, phrase the exact degree-four row as: "for any cyclic
   `A1`-fiber space with multiplicities `(2,4)`, Lemma 2.7 supplies ..."  This
   is a custody/documentation gap, not evidence that the class is empty.
2. In Section 5, purity by itself does not turn the finite normalization of a
   Galois pseudo-covering into an etale cover.  Cite Miyanishi Lemma 2.2(2),
   or say explicitly that Galois uniformity over every height-one target
   point plus almost-surjectivity removes divisorial ramification, after
   which purity applies.  The conclusion is correct; the causal shorthand is
   too loose.
3. On the actual internal block open, `K_U~0` is already forced by the second
   leg (and can also be recovered from the canonical/different classes).
   Therefore the internal computation of `K_U` is a consistency filter on
   proposed adapted boundary rows, not new geometric information about an
   actual row.  Formula (6.1) itself is licensed only when all fibres of the
   chosen `P1`-base `A1`-fibration are irreducible; in the internal Euler
   ledger this is automatic in the equality cell `r+c=10`, not in every
   complete-base row.

None of these repairs revives a `d_1>=2`-only obstruction.

## 1. Custody and source reproduction

Both transactional verifiers pass on the frozen producer.  I independently
retrieved the two primary texts and reproduced the producer's exact receipts:

```text
e35a88d8a33daa64b24b9120bd85aeca0c891869bfa79cdb81ef545a6acfd909
  Oberwolfach Report 19/2005, TIB archival PDF, 493374 bytes

ab4eb0cb74e4051e3fb1f702a253d29cb1a658632f11bc6f4b04a8bb9e7daaa4
  arXiv:1504.07179v1 PDF, 806236 bytes
```

The EMS delivery currently emits a byte-different PDF rendition, but the TIB
archival object reproduces the charged hash and the mathematical text is the
same.  No source claim below rests on a search-result paraphrase.

Primary locations:

```text
https://oa.tib.eu/renate/bitstreams/506cb292-0466-4e6a-9a34-53989f1922e0/download
https://arxiv.org/pdf/1504.07179
https://doi.org/10.1016/j.jalgebra.2005.01.042
```

The Journal of Algebra publisher abstract confirms the definition and the
paper's `A2` source/target scope.  The exact lemma statements charged here are
present verbatim in Miyanishi's authored Oberwolfach summary; this review did
not claim to reconstruct every proof in the paywalled journal article.

## 2. Exact audit of Definition 2.5 and Lemmas 2.6--2.7

The report transcribes the source accurately.

* An affine pseudo-covering is an etale morphism `f:Y->X`, with `Y` affine,
  for which `codim_X(X-f(Y))>=2`.  On a surface this means that the image
  contains the generic point of every prime divisor.  Etaleness also makes
  the morphism quasi-finite and open; almost-surjectivity makes it dominant.
  Neither finiteness nor surjectivity on all closed points follows.
* A cyclic `A1`-fiber space in Definition 2.5(2) has base `P1`, all fibres
  irreducible, and at most two multiple fibres.  The source states Picard
  number one, finite cyclic `Pic(X)_tor`, and, for two fibres of
  multiplicities `m_1,m_2`, fundamental-group order
  `gcd(m_1,m_2)`.
* Lemma 2.6(1)(ii) says exactly that `A2` is a **Galois** affine
  pseudo-covering when the two multiplicities are equal and larger than one.
* Lemma 2.7 says exactly that, if `m_1|m_2` and `m_2/m_1>1`, there is a
  **non-Galois** affine pseudo-covering `A2->X` of degree `m_2`.

Thus, conditional on an `(m_1,m_2)=(2,4)` cyclic target, all seven properties
listed in producer Section 3 follow: actual morphism, everywhere etale,
dominant, open, quasi-finite, codimension-one-surjective, generic degree four,
and non-Galois function-field extension.

The only missing source pin is non-vacuity of the specifically chosen pair.
The Oberwolfach lines state a theorem for every `X` satisfying the
hypotheses; they do not, in those three lines, construct the `(2,4)` target.
The cleanest repair is a one-line construction/citation rather than deleting
the useful exact-degree row.

## 3. The `(2,2)` degree-two crosscheck

The degree-two conclusion is correct, but its clean proof uses the full
Galois pseudo-covering lemma.

Let `q:A2->X` be supplied by Lemma 2.6 for a cyclic space with multiplicities
`(2,2)`, and let `Xtilde` be the normalization of `X` in `C(A2)`.  Miyanishi
Lemma 2.2(2) says that

```text
Xtilde -> X
```

is a connected finite etale Galois cover, with `A2` an open subset of
`Xtilde`.  Definition 2.5 gives `pi_1(X)=Z/2`.  Consequently the finite etale
degree is one or two.  It cannot be one: then `q` is a birational etale
quasi-finite map, hence an open immersion, and almost-surjectivity leaves at
most finitely many points of the smooth complex surface `X`.  Removing a
finite set from a complex manifold of real dimension four does not change
its fundamental group, contradicting `pi_1(A2)=1` and `pi_1(X)=Z/2`.
Therefore the degree is exactly two.

This validates the producer's complementary Galois row.  The phrase
"purity makes the finite normalization etale" should nevertheless be
replaced by the preceding Lemma 2.2(2) argument: in a non-Galois
normalization, ramification can occur on deleted boundary components above a
target divisor even though the `A2` open contains an unramified point over
that divisor.  Galois uniformity is the ingredient that forbids that mixed
behavior.

## 4. Match to the first-leg invariant packet

The invariant checks in producer Section 4 are correct.

1. If `u in O(X)^*`, then `q^*u` is a unit in `C[x,y]`, hence constant;
   dominance of `q` makes `u` the same constant.  Thus `O(X)^*=C^*`.
2. Rationality follows already from an `A1`-fibration over the rational curve
   `P1`.  Miyanishi Lemma 2.2(3) independently transports negative log
   Kodaira dimension from `A2`.
3. Every reduced fibre is `A1`.  Constructible Euler integration (or the
   standard fibration formula) gives `e(X)=2`; scheme multiplicities do not
   alter the topological fibre.  This matches the numerical internal
   complete-base equality cell `e(U)=2`, i.e. `r+c=10`.
4. The report correctly refuses to infer an actual F5/ADE decoration from
   that numerical match.  The control defeats only arguments whose extra
   input is the first-leg degree or image strength; it does not imitate the
   block boundary marking.

The generic-fibre warning is also correct.  A pseudo-covering is not
generally finite, and it need not be a morphism over the identity of `P1`.
A ramified cover of the completed base can be neutralized by multiple-fibre
indices on the total space, leaving the surface morphism etale.  Hence the
absence of connected finite etale covers of a geometric `A1` fibre cannot be
applied before proving ruling compatibility over the same base.

## 5. Canonical formula and `T!=M` inequality

The formula quoted as (6.1) is an exact transcription of the later lecture
notes.  Miyanishi first considers, in general, a smooth affine surface with
an `A1`-fibration over `P1` whose fibres are all irreducible.  On the adapted
completion obtained from `Sigma_n`, he writes

```text
T ~ M+a ell,                 a=0 or a>=n,
[K_X] = I[ell|_X] in Pic(X) tensor Q,
I = 2a-n-2 + sum_i k_i/m_i,
```

and records `k_i>m_i`.  For two multiple fibres,

```text
sum_i k_i/m_i > 2.
```

When the horizontal section is not the chosen minimal section, one is in the
`a>=n` branch (on `Sigma_0` one may choose the minimal section to be `T` in
the `a=0` case).  Therefore

```text
I > 2a-n >= n >= 0.
```

Definition 2.5 gives free Picard rank one for a cyclic space, with the fibre
class spanning the rational Picard group.  Hence `I!=0` really does imply
`K_X` is nontrivial, so no etale `X->A2` can exist in the `T!=M` branch.

If `T=M`, then `a=0` and rational triviality requires exactly

```text
k_1/m_1 + k_2/m_2 = n+2.
```

This kills only the free part.  The producer correctly retains the separate
integral torsion test.  The detailed source's divisibility conditions in the
Platonic proof illustrate why the rational equation must not be promoted to
linear triviality.

Two scope qualifications are mandatory.

* The formula assumes **all fibres irreducible**.  Internally this is known
  from the Euler formula in the complete-base equality cell `r+c=10`; it is
  not known merely from `C=P1` when `r+c<10`.
* For the actual block open, `K_U~0` is already a theorem.  Recomputing it in
  an adapted candidate lattice can reject a falsely assembled row, but it
  cannot provide an additional invariant of a genuine row.

## 6. Reverse-direction source theorems

The producer states the later source scopes correctly.

* Oberwolfach Theorem 2.9 states no etale maps to `A2` for an `ML_0` affine
  pseudo-plane or a Platonic `A1`-fiber space.
* The detailed Theorem 2.5.6 proves the corresponding assertion for a
  `Q`-homology plane with `ML(X)=k` and for Platonic spaces, with the stated
  possible exception `{2,2,m}`, `m>5`.
* Remark 2.5.9 explicitly strengthens that conclusion from target `A2` to
  any affine surface with trivial canonical divisor.
* Theorem 2.5.10 says that an affine pseudo-plane of type `(d,n,r)` admitting
  an etale map to `A2` must have `r=2`.  It is a necessary condition, not an
  existence theorem, exactly as the producer says.

The older three-page summary states the Platonic exclusion without an
exception, whereas the later detailed proof retains the `{2,2,m}`, `m>5`
case.  Campaign use should charge the later, weaker scope.  Neither theorem
covers the cyclic two-fibre targets at issue here.  The firewall against
calling an internal surface cyclic/Platonic without proving the required
irreducible-fibre, multiple-fibre, homology, and fundamental-group hypotheses
is correct.

## 7. Exact decomposable volume and the successor

If `p:X->A2` is etale and `f=p^*u`, `g=p^*v`, then

```text
df wedge dg = p^*(du wedge dv)
```

is nowhere vanishing and

```text
df wedge dg = d(f dg).
```

Since the surface is affine, the global algebraic de Rham complex computes
its algebraic de Rham cohomology; the form therefore has zero class.  If
`O(X)^*=C^*` and `K_X~0`, every nowhere-vanishing canonical form differs by a
scalar, so vanishing of the class is well defined.  The producer is right
that this is stronger than abstract canonical triviality.

The converse is not claimed and must not be introduced later: a zero de
Rham class does not by itself produce two functions `f,g` with
`df wedge dg` nowhere zero.  Even such an etale coordinate pair would still
have to satisfy the fixed rank-three finite-flat extension and F5/different
boundary data to be the internal second leg.

The sharp external successor is consequently well posed:

```text
Find or exclude a cyclic complete-base X with
  A2 -> X an etale pseudo-covering of degree >1
and
  X -> A2 etale.
```

Any affirmative instance composes to an etale endomorphism of `A2` of
generic degree greater than one and is therefore already a JC2
counterexample.  This explains both the power and the difficulty of the
successor.  The efficient sequence is:

1. pin one explicit external cyclic family and compute its adapted
   `(n,a,m_i,k_i)` data;
2. eliminate every `T!=M` row by the verified inequality;
3. in the `T=M` rows impose the rational equation and then the integral
   torsion class;
4. only for survivors test exact/decomposable volume and a genuine reverse
   etale coordinate pair;
5. internally, use `K_U~0` only as a lattice-consistency check and reserve
   the real discriminator for the coordinate pair plus cubic/F5 extension.

## 8. Final disposition

Promotable after a different-model review and the small corrections above:

```text
FIRST-LEG-DEGREE-ONLY P1 EXCLUSION: REFUTED.
```

Not promoted by this report:

```text
existence of a reverse etale map on a cyclic control;
existence of an internal cyclic classification row;
any F5/D9 realization;
any Keller counterexample or JC2 conclusion.
```

The highest-value immediate repair is to pin an explicit `(2,4)` cyclic
target or replace that sentence by its conditional form.  The highest-value
research successor is the full two-sided sandwich, beginning with the
canonical/torsion audit of a concrete cyclic family rather than another
attempt to extract a contradiction from `d_1` alone.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `13739`.
- Body SHA-256:
  `8ece9f575db86110cf2b3b21193ae1b0e6f361742d6dad610a7b857764c1d608`.
- Frozen basis: `0b60124c897778274ab0ce359672089b3f2f91ef`.
