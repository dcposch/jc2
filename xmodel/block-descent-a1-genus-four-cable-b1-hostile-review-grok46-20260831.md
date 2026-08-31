# Hostile review: conductor-eight genus-four Betti obstruction

Date: 2026-08-31 UTC  
Reviewer: Grok 4.6 (independent different-model audit)  
Packet: `xmodel/block-descent-a1-genus-four-cable-b1-hostile-review-packet-20260831.md`  
Packet SHA-256: `789725ceaae5e7496d1e4e83071c64c33065afc72101aaea1da63852b31e3e80`  
Coordinator basis named in packet: `59f25428`

## Verdict

**CONFIRM**

The claimed non-existence theorem is true at its exact charged scope. The
genus-four prime iterated-knot list, the conductor-eight delta-sequence list,
the labelled full-`S4` and Fox-3 screens, the `(9,6,2)` Weierstrass normal
form, and the four-pair `b1>=4` obstruction all survive independent
re-derivation. No load-bearing gap was found. No downstream promotion is
implied.

## Custody

Every charged SHA-256 was reproduced before the corresponding file was read.

```text
070faa884a26b0c96aaacafa7738cb39746407803d156a5a327d360eabf613e5
  xmodel/block-descent-a1-genus-four-cable-b1-obstruction-sol56-20260831.md
c79b7197d9c84e8a9a161cf153430849ad730b35d950a51afc32d1cd73ffa707
  ops/block_descent_a1_genus_four_cable_b1_replay.py
03865aae3cc11a5f7de264ef7a66d1e3600ccb983ea8f95079c50d8a28b0b5aa
  xmodel/block-descent-a1-total-delta-two-iterated-knot-s4-obstruction-sol56-20260830.md
03b16c2deba48605482963ae7f98f5e74aca26ce0e1761bbeab653a164bec4b4
  xmodel/block-descent-a1-genus-three-cable-b1-obstruction-sol56-20260830.md
5d7df7ce0ad3548e88fd23734917212d6b3fbd3ada4cab81514b12bb76ea64de
  xmodel/block-descent-a1-quartic-branch-topology-coordinator-integration-sol56-20260830.md
be4c287fe56c067208496f39a7388c56592c562a93fe46665e693958ad972a3a
  xmodel/post-ledger-dependency-hash-corrigendum-sol56-20260831.md
```

All six matched. No sibling review, model log, run receipt, mutable lane
output, or excluded workspace was inspected. The Assi--Garcia-Sanchez arXiv
`1407.0490v1` PDF was fetched independently as a primary source; its SHA-256
is `05081acd04a51c85d231ff288c8522b83e79d75b28af7f99868c2f5149683bf9`, which
agrees with the hash recorded in the charged genus-three artifact.

The charged corrigendum records a misbound review hash in the genus-three
artifact. That is a provenance defect only. The three topology interfaces
consumed below are taken from the directly charged total-delta paper, not from
the misbound review.

## Exact theorem

Let `B` be a reduced irreducible complex affine plane curve with
`normalization(B)=A1`, one place at infinity, `Delta_aff(B)=4`, and
`b1(B)=1`. Suppose `pi1(A2-B)` admits a transitive representation to `S4`
sending every positive generic meridian to a transposition. Then no such `B`
exists.

Equivalently, in this packet: of the seven prime iterated-cable knot types of
genus four, the one-place semigroup condition retains exactly the four
conductor-eight delta-sequences `(9,2)`, `(5,3)`, `(6,4,5)`, `(9,6,2)`; the
first three have no labelled full-`S4` meridian-transposition colouring; every
polynomial realisation of the last sequence is equivalent, under affine
parameter change and triangular target automorphisms, to

```text
U=t^6+8 t^2,
V=t^9+12 t^5+24 t,
V^2-U^3-64 U=64 t^2,
```

and that normal form has four disjoint normalisation pairs, hence `b1(B)>=4`,
contradicting `b1(B)=1`. Combined with `Delta_aff=4` and `delta_z >= #nu^{-1}(z)-1`,
one in fact has `b1(B)=4` throughout the `(9,6,2)` row.

This is not an exit-price assertion.

## 1. Prime iterated-knot census

Schubert's formula, after winding-one and unknot-producing steps are deleted,
is `g(C_(p,q)(J))=p g(J)+(p-1)(|q|-1)/2` with `p>=2` and `gcd(p,q)=1`.

Unknot companion and genus four give `(p-1)(|q|-1)=8`. Coprimality and
exchange of torus coordinates leave exactly `T(2,9)` and `T(3,5)`, with
mirrors.

Nontrivial companion forces `p g(J)<=4`.

- `g(J)=1`: `J` is a trefoil or mirror, and the exact solutions are
  `(p,|q|)=(2,5),(3,2),(4,1)`.
- `g(J)=2`: necessarily `p=2` and `|q|=1`. The prime iterated genus-two
  companions, from the charged total-delta census, are `T(2,5)` and
  `C_(2,1)(trefoil)`, with mirrors. Connected sums are excluded already by
  one-place primeness, not by this Diophantine step.
- `g(J)>=3` is impossible.

This is exactly the seven-row list (0.1). Signs and companion chiralities are
retained. No omitted winding-one, mirror, or three-stage row exists inside
the prime iterated-cable category: the only three-stage tower is
`C_(2,+/-1)(C_(2,1)(trefoil) or mirrors)`, already listed.

## 2. Conductor-eight delta-sequence census

Assi--Garcia-Sanchez Proposition 2 gives

```text
mu = sum_{k=1}^h (e_k-1) r_k - r0 + 1,
```

with `e_k=d_k/d_{k+1}` and `d_1=r0`, `d_{k+1}=gcd(d_k,r_k)`. Here
`mu=2g=8`. Their Section 5 records `mu >= 2(2^h-1)`, hence
`h <= floor(log_2(g+1))=2`. In particular a free length-four characteristic
sequence is impossible at conductor eight.

A delta-sequence in their sense is free, satisfies the Newton inequalities
`r_{k-1} d_{k-1} > r_k d_k`, and obeys `r0 > r1 > d2 > ... > 1`. The last
clause forces `b>=2` in the writing `r0=a d`, `r1=b d`.

For `h=1`, `(r0-1)(r1-1)=8` with `r0>r1` and coprimality gives exactly
`(9,2)` and `(5,3)`.

For `h=2`, primitivity is `gcd(d,r2)=1` and freeness is `r2 in <a,b>`, hence
`r2>=b>=2`. The conductor equation is `7=d*((a-1)b-a)+(d-1)r2`. The defect
`(a-1)(b-1)-1` is at least `1`, so `7>=3d-2` and `d<=3`.

- `d=2`: the only solution is `(a,b,r2)=(3,2,5)`, i.e. `(6,4,5)`.
- `d=3`: the only solution is `(a,b,r2)=(3,2,2)`, i.e. `(9,6,2)`.

Both satisfy the Newton inequality (`24>10` and `54>6` respectively) and
`r1>d2`. Independently, every primitive conductor-eight sequence of length at
most four was enumerated in a finite box; the only AGS delta-sequences are
these four. The topological leftovers `(12,8,1)`, `(10,4,1)`, and any
length-four characteristic fail freeness or the height bound, as claimed.
Dropping freeness in the replay legitimately adds exactly `(10,4,1)` and
`(12,8,1)`.

The Puiseux/cabling dictionary matches the first four rows of (0.1):
`(9,2)=T(2,9)`, `(5,3)=T(3,5)`, `(6,4,5)=C_(2,5)(trefoil)`,
`(9,6,2)=C_(3,2)(trefoil)`. Coordinate order `r0>r1` is the AGS convention,
not an extra hypothesis.

## 3. Braid convention, full-`S4` counts, and Fox-3

Consumed meridian and boundary-to-affine interfaces, all from the charged
total-delta paper unless noted:

- `g_3(K_infinity)=Delta_aff(B)` (nearby fibre plus Neumann Theorem 1);
- `K_infinity` is the unknot or a prime iterated cable (Rudolph parametrized
  cabling / Neumann rooted valency one, plus Schubert primeness);
- `pi1(S3-K_infinity) ->> pi1(A2-B)`, meridians preserved (Zariski--van Kampen
  versus the closed-braid total word);
- Artin action `sigma_i:(A,B)|->(A B A^{-1}, A)`, with the inverse
  `(A,B)|->(B, B^{-1} A B)`;
- zero-framed cable word, as in the charged genus-three convention,
  `W_(p,q,epsilon)=X_p^{3 epsilon}(s_1...s_{p-1})^{q-3 epsilon p}`, where
  `X_p` is the positive permutation braid swapping two blocks of `p` strands.

The replay's bubble-sort `block_switch_word` reproduces the charged words
`X_2=s2 s3 s1 s2` and `X_3=s3 s4 s5 s2 s3 s4 s1 s2 s3` on the nose. The
permutation of each of the eight cable closures is a single `2p`-cycle, so
each closure is a knot. Independent reduced-Burau specialisations at
`t=2,3,4` show that `det(I-Burau_red(W))` equals the Seifert--Schubert cable
polynomial

```text
Delta_{C(p,q)(J)}(t) = Delta_{T(p,q)}(t) Delta_J(t^p)
```

up to a Laurent unit, for every sign/chirality of `C(2,+/-5)(trefoil)` and
`C(3,+/-2)(trefoil)`, and likewise for `T(2,9)` and `T(3,5)`. The braid
convention is therefore the geometric cable, not a homonym.

The labelled full-`S4` and Fox-3 counts, including every cable sign/chirality,
are:

| row | det | Fox-3 | full-`S4` |
|---|---:|---:|---:|
| `T(2,9)` | 9 | 9 | 0 |
| `T(3,5)` | 1 | 3 | 0 |
| `C(2,+/-5)(trefoil or mirror)`, all four chiralities | 5 | 3 | 0 |
| `C(3,+/-2)(trefoil or mirror)`, all four chiralities | 9 | 27 | 144 |

The multiply-by-six from a fixed first transposition is legitimate: labelled
counts are not quotiented by conjugacy, and simultaneous conjugation acts
transitively on the six possible first colours. Inverse words have identical
fixed colourings, so the replay's omission of `T(2,-9)` and `T(3,-5)` is
harmless; those two were enumerated separately and match. Determinant `9` does
not kill `T(2,+/-9)` by the double-cover lemma, which is why the colouring
count is load-bearing for that row. Determinant `1` does kill `T(3,+/-5)`.
Fox-3 counts are compatible with the 3-primary part of the determinants
(`3^{1+1}`, `3^{1+0}`, `3^{1+0}`, `3^{1+2}` respectively). No colouring or
determinant claim is used against the `(9,6,2)` row.

## 4. Section 5: approximate-root normal form

This is the highest-risk bridge. It is nonetheless exact.

The charged AGS/reduced-coordinate interface, used in the same way as for
conductor six, supplies coordinates of degrees `deg U=6`, `deg V=9` whose
weighted leading relation is `V^2-U^3`. The monomials of weighted degree
strictly less than eighteen are `1,U,U^2,V,UV`. Completing the square in `V`,
depressing the cubic in `U`, and scaling are affine-triangular target
automorphisms of `A2`. They preserve the partition of `A1` into normalisation
fibres, hence preserve `b1`. The last characteristic value forces the
resulting Weierstrass polynomial `H=V^2-U^3+A U+B` to have parameter degree
exactly two.

There is a unique monic cubic `Z` with `U=Z^2+R` and `deg R<=2`. Translating
the parameter depresses `Z`. The polynomial part `W` of `U^{3/2}` at infinity
is `Z^3+(3/2) Z R+(3/8) Q` after the division `R^2=Z Q+S`. Direct expansion
gives `deg(W^2-U^3)<=8`. If `V` is monic of degree nine then `deg(V-W)<=8`; a
nonzero difference of degree `d>=0` produces a term `2 W(V-W)` of degree
`9+d>=9`, strictly above every term cancellable by `A U+B`. Characteristic
zero therefore forces `V=W`. The identity

```text
W^2-U^3 = -(3/4) Z^2 S + (9/8) Z R Q - R^3 + (9/64) Q^2
```

was re-expanded by hand and is correct. Polynomial division recovers the
stated formulae for `Q` and `S`.

If `a=0` and `b!=0`, the degree-eight coefficient is `-3 b^2/4`, which
constants `A,B` cannot cancel. If `a=b=0`, a unique choice of `A,B` reduces
`H` to zero, of parameter degree zero rather than two. Hence `a!=0`. Then `S`
must be constant, which uniquely solves for `p,q`. After the unique `A`
killing degree six, exact expansion in `C[b,c]` at `a=1` gives

```text
[t^5](W^2-U^3+A U)=3b/8,
[t^4](W^2-U^3+A U)=-(c-b^2)/8,
[t^3](W^2-U^3+A U)=(5/8) b (2c+b^2).
```

(The producer's interpolation grid is a valid certificate of the same
bivariate identities, of `b`-degree at most 18 and `c`-degree at most 6; the
expansion above makes the interpolation unnecessary.) Characteristic zero and
`a!=0` force `b=0`, then `c=0`, then `p=q=0`. Scaling in `t` and the weighted
coordinates over `C` sends every `a!=0` to `a=8`. Conversely the displayed
member has exact parameter degree two, so it realises the last delta entry.

No omitted lower-weight monomial, no residual family, and no cancellation
escape remains. The `a=0` branches are dead. The replay's specialisation grid
and the integer identity `V^2-U^3-64 U=64 t^2` match the closed form.

Birationality: (5.13) puts `t^2` in `C(U,V)`, and (5.14) then puts `t` in
`C(U,V)` because the denominator `t^8+(3/2)a t^4+(3/8)a^2` is a polynomial
in `t^2` and is not identically zero (discriminant `(3/4)a^2!=0`).

## 5. Normalisation pairs and `b1`

For `a=8`, `V=t(w^2+12 w+24)` with `w=t^4`. Discriminant `48` and constant
term `24` give two distinct nonzero `w`-roots. Their eight fourth roots are
distinct and partition into four disjoint unordered pairs `{t,-t}` with
`t!=0`. The coordinate `U` is even and `V` vanishes at every endpoint, so
each pair lies in one fibre of `nu`. Independently, the four image values `U=t^2(w+8)` are four distinct
purely imaginary numbers (two conjugate pairs of distinct moduli), so the
four pairs have four distinct images. The weaker merging argument is
therefore not needed for this specific member, but remains the correct
uniform bound.

Formula (1.1), charged through the genus-three identification of the affine
curve with the quotient of a contractible normalisation by its finite fibres,
gives `b1(B)=sum_z (#nu^{-1}(z)-1)`. Four pairs in at most four fibres, with
at least eight endpoints, yield `b1>=8-4=4`. Merging images or adding extra
preimages only increases the right-hand side. This is a lower bound with a
matching theorem-side upper bound `b1<=Delta_aff=4` from `delta_z >= n_z-1`,
so equality `b1=4` holds throughout the row. Against the charged hypothesis
`b1=1`, the inequality `b1>=4` is already fatal.

The argument never mistakes a count of pair equations for a Betti number, and
never treats a representative fibre as a full actual exit.

## 6. Replay

Interpreter: CPython 3.14.7. The replay contains no `assert` statements.
Ordinary, `python3 -O`, and `python3 -OO` executions are byte-identical:

```text
stdout SHA-256:
1fbb987b3b3a12aef716f5526fea3f539d02843797ded68e4d70eeea66c8438c
payload_sha256:
f36b4480a9163060f438b3ca33465dbe27fb99aa254a937fa2f0a04d2c015689
status=PASS-A1-GENUS-FOUR-CABLE-B1-OBSTRUCTION
```

The three mutations exit nonzero at their intended gates:

- `--mutate-drop-freeness` fails the conductor-eight census (the extra
  sequences are `(10,4,1)` and `(12,8,1)`);
- `--mutate-allow-c32-b1-one` fails the four-pair lower bound;
- `--mutate-promote-zero-s4` fails the winding-two vanishing count.

The replay proves the finite arithmetic, the labelled colouring table, the
coefficient identities on a sufficient interpolation grid, the `a=0`
dead-ends, the integer Weierstrass identity, and the pair-quadratic
discriminant. It does not prove Schubert genus or primeness, Neumann--Rudolph
goodness, the nearby-fibre Euler identity, the infinity-to-affine surjection,
the AGS existence theorem, the normalisation-quotient identification of
`b1`, or (unlike the genus-three predecessor) the cable Alexander polynomials.
Those last polynomials were checked independently in Section 3 and are not a
gap in the written argument.

## Primary-source interfaces actually consumed

- Horst Schubert, *Knoten und Vollringe*, Acta Math. 90 (1953): satellite
  genus, primeness of nontrivial cables, cable Alexander formula.
- Walter D. Neumann, *Invent. Math.* 98 (1989), Theorems 1 and 2(i), together
  with corrected Neumann--Rudolph Lemma 7.1 (1988 corrigendum): nearby fibre
  as minimal Seifert surface; one point at infinity; rooted cabling from the
  unknot.
- Lee Rudolph, arXiv:math/0106058, Sections 4 and 6: polynomial parametrisation
  meets a large bidisk in an iterated torus knot.
- John Milnor, Annals of Mathematics Studies 61: `mu_p=2 delta_p-r_p+1`.
- Assi--Garcia-Sanchez, arXiv:1407.0490v1: Proposition 2 (freeness, conductor),
  the delta-sequence definition before Proposition 13, and Section 5
  (`mu>=2(2^h-1)` and the fixed-genus enumeration).
- The charged total-delta paper for the double-cover determinant lemma and
  the meridian-preserving boundary-to-affine surjection.
- The charged genus-three paper only for the AGS packaging, the
  `b1=sum(n_z-1)` quotient formula, and the cable-braid word convention; not
  for its genus-three existence conclusion.

The charged coordinator integration is not used as a numerical bound. Its
`(2,2)`-fibre count `n22` is a cover-side quantity and is not identified with
the normalisation self-pairs of `B`.

## Remaining assumptions

The following are assumptions, not theorems of the present artifact.

- The charged total-delta interfaces listed above, including goodness of a
  one-place reduced equation and the identification of the compact nearby
  fibre with the minimal Seifert surface.
- Characteristic zero, used for completing the square, depressing the cubic,
  the coefficients `3/2` and `3/8`, and `V=W`.
- Complex algebraic (not merely topological) orientation of the one-place
  branch; extra braid signs are retained only as a stronger screen.
- That every abstract iterated knot need not be polynomially realisable: the
  argument never claims the converse, and uses AGS freeness to discard the
  non-realisable rows.

No `sat()` identity, no pole-class identity, no merge-free `M`-descent, and
no target/arrival-index comparison is used.

## Maximum safe statement and blast radius

**Safe statement.** There is no reduced irreducible complex affine plane
curve `B` with normalisation `A1`, one place at infinity, `Delta_aff(B)=4`,
`b1(B)=1`, and a transitive meridians-to-transpositions representation
`pi1(A2-B)->S4`.

**Blast radius.** This closes the irreducible one-place charged genus-four
`b1=1` horn, including the `m=0` specialisation of that horn, before any
affine Fox or local singular-link computation. It realises the `(9,6,2)` row
by an explicit polynomial curve, and shows that every such realisation has
`b1=4`. It does not:

- exclude genus four with `b1>=2`;
- exclude reducible branches, forests, or more than one place at infinity;
- exclude non-transposition inertia, disconnected covers, or degree other
  than four;
- treat conductor ten / genus five, or any higher iterated cable;
- construct or exclude a finite algebraic cover, a proper rank-four block,
  or a Keller map;
- prove JC2, rank-four emptiness, or anything about primitive packets.

The first remaining irreducible one-place question at this delta is therefore
not a `b1=1` genus-four curve. The smallest honest successor is the
conductor-ten census, with the same order: approximate-root normal form,
then normalisation-pair count, then any affine Fox/local-link kernel.

## Repair

None required. Presentation nits that do not affect the theorem: the replay
does not list negative torus braids (inverse-word invariance supplies them);
determinants in the replay are hardcoded from the cable formula rather than
recomputed from Burau (the formula is independently confirmed); identity
(5.11) is stated by coefficient comparison whose written certificate is the
interpolation grid. None of these is an invalid implication.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `18138`.
- Body SHA-256:
  `55931020c8ce8c5c4c901855e376ea9179a9036df6f0e7a5342f3ca420e20caf`.
- Frozen basis: `14933626fddaa5b0f239e6cefc6aaa9763b29dce`.
