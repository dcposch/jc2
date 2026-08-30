# Source and utility audit: `AF-PI1-NODAL-SQUEEZE`

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `a8c8c1dd27c2cdd1d7ffb5f5c1eeada4eeeb60c5`  
Lifecycle: **TARGETED SOURCE AUDIT / MAXIMUM-SAFE COROLLARY / NO AVENUE RAISE**

## 0. Verdict

Fable's two exact implications are sound after a substantial repricing.

> **Maximum safe corollary.** If `F:A2_C->A2_C` is a hypothetical
> noninvertible Keller map and `A=A(F)`, then
>
> ```text
> pi_1(A2-A) is nonabelian,
> D=closure(A)+L_infinity subset P2 is not a nodal curve.
> ```

The first statement is an immediate composition of the promoted connected
complement cover with Campbell's classical Galois-case theorem.  The Kummer
normalization argument is unnecessary.  The second is the contrapositive of
the Fulton--Deligne nodal-complement theorem.

This is useful infrastructure and a clean necessary-condition filter, but it
does not presently raise Avenue 7.  The first implication is classical in
substance, and the nodal failure at infinity is often already forced by the
one-place polynomial parametrizations of components.  A stronger Nori-type
numerical application remains an open new client, not a consequence of this
audit.

No broad web sweep and no computation were performed.

## 1. Charged campaign inputs

```text
4cda89526079cfeee51fab005fa108986f09ef8408c5d67f7efc81e3748d539a
  xmodel/ideation-20260830T1015Z-fable5.md
54fd5073a5d1447ab344ebfcc9c5019bdc19ccdbbd41c6b8cd11f417f17b692e
  xmodel/acs-tdic-hostile-review-grok46-20260829.md
```

The promoted ACS theorem supplies a connected finite etale cover

```text
V=A2-F^{-1}(A)  -->  W=A2-A
```

of degree equal to the geometric degree `d=[C(x,y):C(P,Q)]`.  It also says a
counterexample's `A(F)` must be reducible or singular, but that latter fact is
not used in the group argument.

## 2. Abelian complement group forces the classical Galois case

Assume `pi_1(W)` is abelian.  Connectedness of `V` makes its monodromy action
on a geometric fibre transitive.  The image is abelian.  A faithful transitive
action of an abelian group is regular: all point stabilizers are conjugate,
hence equal, and the kernel of the action is their intersection, so every
stabilizer is trivial.  Equivalently, the subgroup of `pi_1(W)` defining the
cover is normal.  Thus `V->W` is a Galois cover and

```text
C(x,y)/C(P,Q)
```

is a Galois field extension.

Campbell proved that a complex Keller map whose induced rational-function
extension is Galois is a polynomial automorphism.  The original source is:

```text
L. A. Campbell,
"A condition for a polynomial map to be invertible",
Mathematische Annalen 205 (1973), 243--248,
doi:10.1007/BF01349234.
```

Razar's later algebraic treatment is:

```text
M. J. Razar,
"Polynomial maps with constant Jacobian",
Israel Journal of Mathematics 32 (1979), 97--106,
doi:10.1007/BF02764906.
```

Therefore an assumed counterexample cannot have abelian `pi_1(W)`.

This proof is stronger in custody and shorter than the proposed Kummer-unit
sketch.  The sketch would have to choose cyclic layers, normalize the affine
target in each layer, control divisors with exponents divisible by the layer
degree, and prove that both a representative and its inverse restrict
regularly to the source open.  None of that adds content once the classical
Galois case is cited.

## 3. Nodal projective arrangement is impossible

Let

```text
D=closure(A) union L_infinity.
```

Then `P2-D=A2-A=W`.  Fulton proved that the algebraic fundamental group of
the complement of a projective plane curve with only ordinary nodes is
abelian; Deligne proved the corresponding topological statement.  The primary
references are:

```text
W. Fulton,
"On the fundamental group of the complement of a node curve",
Annals of Mathematics 111 (1980), 407--409,
doi:10.2307/1971204,
https://annals.math.princeton.edu/1980/111-2/p08

P. Deligne,
"Le groupe fondamental du complement d'une courbe plane n'ayant que des
points doubles ordinaires est abelien (d'apres W. Fulton)",
Seminaire Bourbaki, Exp. 543 (1979/80).
```

If `D` were nodal, `pi_1(W)` would be abelian, contradicting Section 2.
Hence `D` has at least one worse-than-node singularity, nontransverse
component intersection, or nontransverse contact with `L_infinity`.

## 4. Utility limit and exact successor

The projective nodal corollary is weaker than its wording initially suggests.
An irreducible polynomially parametrized component has one place at infinity.
If its projective degree is greater than one, its entire intersection number
with `L_infinity` can be concentrated at that place, and nontransverse
infinity contact is typical or forced.  If components are lines, repeated
directions or several components through one infinity point already make the
arrangement nonnodal.  Thus `D` failing nodality need not sharpen the existing
one-place geometry.

Nori's generalization can be genuinely stronger only after an exact resolved
arrangement and its self-intersection/node inequalities are supplied:

```text
M. V. Nori,
"Zariski's conjecture and related problems",
Annales scientifiques de l'Ecole Normale Superieure 16 (1983), 305--344,
https://www.numdam.org/item/10.24033/asens.1450.pdf
```

The cheapest successor is therefore not another proof of nonabelianity.  It
is one component-labelled `A(F)` packet on a resolved compactification:

1. compute the exact singularities and infinity intersections of
   `closure(A)+L_infinity`;
2. test the literal Nori inequalities on those strict transforms; and
3. stop if the hypotheses fail automatically for every one-place component.

A success would impose a quantitative worse-singularity/tangency floor.  A
failure records that the pi1 route adds no leverage beyond the classical
Galois theorem and one-place infinity geometry.  Neither outcome constructs
`A(F)`, bounds `d`, supplies a selector, or proves JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5898`.
- Body SHA-256:
  `e1864f1ce59ae3f6cbe6a01d32c339e67a230c7ded38793fd5b1bc858997d6a0`.
- Frozen basis: `a8c8c1dd27c2cdd1d7ffb5f5c1eeada4eeeb60c5`.
