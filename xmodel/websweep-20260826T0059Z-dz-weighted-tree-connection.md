# JC2 web sweep — 2026-08-26T00:59Z

Status: **no new disclosed proof or counterexample to the complex plane
Jacobian conjecture was found; one high-value terminal-classification
connection and two directly useful 2026 enumeration results were found.**

This sweep was pulled forward from the 24-hour backstop by significant
campaign news: the reviewed `(8,12)` terminal equation had just become an
extremal polynomial-abc problem.  The searches also rechecked recent
`Jacobian conjecture`, plane/two-variable, proof/counterexample, arXiv, and
August-2026 results.  The public counterexamples remain in dimensions at
least three; the real degree-six theorem is not the complex constant-Jacobian
problem.  Search indexing and private work are incomplete, so “none found”
is not an exhaustiveness theorem.

## 1. Exact match with Davenport--Zannier weighted plane trees

Let a reviewed nontrivial terminal map be written

```text
T=A/B,  deg A=deg B=D,
pi_0=(alpha_1,...,alpha_r),
pi_infinity=(beta_1,...,beta_s),
U=r+s,
pi_1=(U-1,1^(D-U+1)).
```

Here `A,B` are coprime monic polynomials, `A-B` is squarefree, and infinity
is the point of local degree `U-1` above `1`.  This is precisely a
Davenport--Zannier pair, represented by a weighted bicolored plane tree:
black vertex weights are the `alpha_i`, white vertex weights are the
`beta_j`, and total edge weight is `D`.

[Pakovich--Zvonkin Part I](https://arxiv.org/abs/1306.4141) proves that such
trees represent coprime equal-degree polynomial pairs whose root
multiplicities are the black/white vertex degrees and whose difference has
the minimum possible degree.  The campaign identity
`deg(A-B)=D-U+1` is exactly that minimum.  Equivalently, the associated
three-point cover has the third passport above.

This is not merely an analogy.  For `U>=3`, the part `U-1>1` marks the
unique ramified point over `1`; moving it to infinity turns source Möbius
equivalence into the affine equivalence used in the terminal theorem.  The
degenerate `U=2` clients should remain in their already explicit direct
classification rather than be inferred from a theorem stated for genuine
three-branch covers.

## 2. New finite enumeration front end

Two recent primary sources make the connection algorithmic.

- [Lu--Song, *Enumeration of weighted plane trees by a permutation model*
  (January 2026)](https://arxiv.org/abs/2601.07544) gives a constructive
  permutation/tree bijection for full passports.  It also records the
  Boccara--Zannier existence criterion for an integer passport:

  ```text
  (U-1) * gcd(alpha_i,beta_j) <= D.
  ```

  Thus many integer terminal profiles can be rejected before any coefficient
  ideal is compiled.  In the nondecomposable fully labelled case the rooted
  tree count is controlled by the explicit permutation model; decomposable
  passports are handled recursively.

- [Lu--Song, *Counting Weighted Bi-Colored Plane Trees and Their Geometric
  Applications*, v2 July 2026](https://arxiv.org/abs/2606.21074) gives a
  unified exact count for arbitrary repeated vertex weights (Theorem 3.13)
  and a counting algorithm based on divided passports, modified Kochetkov
  counts, and Möbius inversion.  Its Theorem 4.2 proves, for arbitrary
  partitions `pi_0,pi_infinity` of `D>2`, a bijection between weighted
  bicolored plane trees and strong equivalence classes of genus-zero covers
  with

  ```text
  pi_1=(1^(D-U+1),(U-1)^1).
  ```

  That is exactly the reviewed terminal passport, with no inferred change of
  variables or heuristic matching.

[Zvonkin's 2014 enumeration paper](https://arxiv.org/abs/1404.4836) provides
coarser checks by total weight and number of edges.  [Pakovich--Zvonkin Part
II](https://arxiv.org/abs/1509.07973) computes the unitree pairs, but unitrees
are only the rational-coefficient subset: the campaign must retain
non-unitrees and the algebraic number fields of their Belyi maps.

## 3. Consequences for the `(8,12)` campaign

This replaces blind terminal moment-variety enumeration with the following
count-certified finite pipeline at each `(m,U,D)`:

1. enumerate signed integer passports with `1<=alpha_i<=m`, `beta_j>=1`,
   equal total `D`, `U-1<=D<=m(U-1)`, exact-order condition
   `gcd(m,alpha_i,beta_j)=1`, and the stronger weighted-tree existence
   inequality;
2. compute the exact number of tree/cover classes from the 2026 trivial-
   passport algorithm;
3. construct all full-labelled trees via the permutation model, quotient by
   repeated-label automorphisms, and require the constructed census to equal
   the independent exact count;
4. realize each tree as a Belyi/Davenport--Zannier pair over its actual
   algebraic number field, with exact reconstruction and source replay;
5. shard the remaining Faber tails and both Taylor boundaries by tree class
   across AWS; run hostile review in parallel with descendants once a result
   is provisionally credible.

The count is a completeness checksum, not a lower-tail theorem.  A tree
realizes only the terminal differential equation.  It supplies neither the
other six tails, the nine Faber constants, Taylor polynomiality, a Keller
pair, nor JC2.

There is also a possible uniform route beyond fixed-`U` enumeration.  The
terminal logarithmic derivative

```text
T'/T = sum_i n_i/(x-c_i)
```

is the meromorphic differential attached to the weighted tree, with its
unique zero of order `U-2`.  Rather than expand every Belyi polynomial, one
can try to express the first unresolved lower-tail obstruction as a local
sum over weighted edges or tree paths.  A sign/positivity, leaf-removal, or
cut identity valid for every weighted tree would close all `U` at once.  The
finite census should therefore serve both as a direct search and as a
conjecture generator for such a tree-local obstruction.

## 4. Allocation decision

- Promote the weighted-tree correspondence as a **terminal frontend**, not
  as a new proof avenue detached from maximum twelve.
- Add a small independent count oracle first; it can invalidate a faulty
  constructive census cheaply.
- Run all substantive enumeration, Belyi reconstruction, Gröbner
  elimination, and exact lower-tail tests on AWS.  The Mac remains restricted
  to coordination, text edits, hashes, and SSH.
- Do not restrict to unitrees or rational coefficients.
- Preserve the separate direct treatment of `U=2` and the terminal/lower-tail
  firewall.

The full web-sweep clock resets at this event; the next quiet backstop is
2026-08-27T00:59Z, with immediate resweep on significant external news.
