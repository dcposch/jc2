# Magnen v1 tree restriction: independent source countercheck

- Producer: swarmHQ, Astra (`gpt-6-astra`), bounded `magnen_source_check` lane.
- Evidence: **MANUAL** exact rational algebra; lifecycle: **PRODUCER-CHECKED, UNPROMOTED**. This is not different-model FIRST review.
- Basis: `9131f71b35f524751a1182f4f4f7cc7cca6afda9`.
- Charged source: Jacques Magnen, *The Jacobian conjecture*, [arXiv:2311.14723v1](https://arxiv.org/abs/2311.14723v1), dated 19 November 2023; frozen PDF `box/magnen-tree-screen-swarmHQ-20260914/magnen-v1.pdf`.
- Frozen PDF SHA256: `963c7ac5130670869724402b2c12dc5b86df421d39dfbf2ce82a3b785f01ed83` (recomputed before source reading).
- Scope: ordinary characteristic-zero plane Keller automorphisms; source equations (3.1), (3.19), and (4.3)-(4.4) under the source's own edge restriction. No accepted degree bound is under review.

## Disposition

The literal universal identities (3.1), (3.19), and (4.3)-(4.4) are **REFUTED at this report's manual, unpromoted tier** by a quadratic plane automorphism. The discrepancy is already the coefficient of `y1^2` in the first inverse component. This does not refute the Jacobian conjecture or the source's degree-bound conclusion; it breaks the proposed tree-to-determinant factorization on an automorphism.

## Source read scope and hypotheses

I read the frozen nine-page PDF by `pdftotext -layout`, with separate bounded rereads of pages 1-4 and 5-7. The charged statements are (1.1)-(1.7) and Theorem 1.2 on pages 1-2; Definitions 1-4 on pages 3-4; Proposition 1/(3.1), Definition 6/(3.19) on pages 4-6; Definition 7 and Proposition 4.1/(4.3)-(4.4) on pages 6-7. The appendix was inspected only to establish that its relaxed linear-term case is unnecessary here.

The source requires `f(x)=x-V(x)`, `V(0)=DV(0)=0`, and determinant one. Its displayed trace/log condition is equivalent to `det(I-DV)=1` in the formal completion used below. The tensor coefficients in the outgoing indices are symmetric, as in (1.3). Our example even has components symmetric under exchanging `x1,x2`.

The ring is `Q[x1,x2]` for the polynomial map and `Q[[y1,y2]]` for tree sums, formal logarithms and exponentials. Substitution `xj -> Gj(y)` is the unique continuous homomorphism of formal power-series rings when `G(0)=0`. The later coefficient extraction uses the explicit specialization `y1 -> t, y2 -> 0` into `Q[[t]]`.

Root and leaf edges are included: Definition 1 pairs the root index with a vertex incoming index, and pairs outgoing indices with other vertices or the `y` leaves. Definition 3 declares an incoming edge smaller than its outgoing edges. Thus a root edge of index 1 and a leaf edge of index 1 at the same vertex form a forbidden aligned pair in Definition 6. This is essential to the charged interpretation and follows directly from the definitions, rather than an internal-edge-only convention.

Weights are normalized by the recursive inverse expansion (1.5)-(1.7), to which Definition 1 expressly attaches its trees. In particular, the entire one-vertex contribution is `Vi(y)` before restriction. No independent choice of graph symmetry factors is introduced.

No ROOT or other lane report body, mutable external report, third-party mirror/social source, or separate repository was consulted. Administrative policy reads were `README.md`, `AGENTS.md`, `COORDINATION.md`, `team/swarmHQ/README.md`, and `FALLACY-v2.md`. No scientific Python, CAS, enumeration, AST scan, test suite, build, cloud job or model launch was used.

## Exact ordinary plane control

Set `s=x1-x2` and

```text
V(x) = (s^2, s^2),
f(x) = (x1-s^2, x2-s^2),
A(x)=DV(x) = 2s [[1,-1],[1,-1]].
```

Here `A^2=0`, `tr A=0`, and

```text
det Df = (1-2s)(1+2s) - (2s)(-2s) = 1.
```

The difference of the two components of `f(x)` is `s`. Consequently the exact polynomial inverse is

```text
F(y) = (y1+(y1-y2)^2, y2+(y1-y2)^2).
```

Both compositions are the identity by that same difference invariant. The map and its inverse have actual total degree 2 in both components, and actual degree 2 separately in each input variable; no weighted degree is used. This is a finite-degree automorphism method control, with no counterexample/frontier computation.

Let `G=F(|1)` as defined in Definition 6. Since the root edge of `G1` has index 1, every edge below it must have index 2. The only permitted quadratic monomial in its one-vertex term is therefore `y2^2`. For `G2` the root is index 2, and all three one-vertex monomials are permitted: their index-1 leaf edges are siblings, not aligned. Hence, writing `O(3)` for terms of total degree at least 3,

```text
G1 = y1 + y2^2 + O(3),
G2 = y2 + (y1-y2)^2 + O(3).
```

There is also an exact description of the first component. The subtrees below its root use only index 2, so if `z=y2+z^2` is the unique solution with zero constant term, then `G1=y1+z^2`. In particular `G1(t,0)=t` exactly. This exact observation is optional; the degree-two truncation already decides all charged failures.

## Equation (3.1): full determinant factor

As printed in Proposition 1, (3.1) multiplies `Gi` by `exp(-tr log(I-A(G)))`, without a trace restriction. Since `A(G)^2=0` and `tr A(G)=0`, that factor is exactly 1. Its right side in component 1 is `G1`, which has coefficient 0 at `y1^2`. The left side `F1` has coefficient 1. Thus (3.1), literally as printed, fails.

## Equation (3.19): the restricted trace reading also fails

Equation (3.19) restricts the trace to closed index words containing index 1. This is a materially different reading from (3.1), and it must be checked separately.

Write `u=G1-G2`. For each positive integer `m`, `tr(A(G)^m)=0`. The unique closed index word avoiding index 1 is the all-2 word, with weight `A22(G)^m=(-2u)^m`. Therefore the restricted trace sum is `-(-2u)^m`, and its exponential is exactly

```text
E1(G)
 = exp(sum_{m>=1} -(-2u)^m/m)
 = exp(log(1+2u))
 = 1+2u.
```

This calculation uses the same `1/m` trace-log normalization printed in the source. It is coefficientwise valid in the formal power-series ring because `u(0)=0`.

Thus the component-1 right side of (3.19) is

```text
G1 E1(G)
 = (y1+y2^2+O(3)) (1+2(y1-y2)+O(2))
 = y1 + 2y1^2 - 2y1y2 + y2^2 + O(3).
```

Its `y1^2` coefficient is 2, while the exact inverse coefficient is 1. Equivalently, after the explicit specialization `(y1,y2)=(t,0)`, the left side is `t+t^2`, whereas the right side is `t+2t^2+O(t^3)`.

The factor 2 has a concrete combinatorial meaning here: the derivative `d(x1^2)/dx1=2x1` marks either of the two equal-index children, whereas the inverse expansion contains the one quadratic monomial once. The passage from the rooted tree sum to the common multiplicative trace exponential has not preserved that coefficient. This report establishes failure of the resulting identity; it does not attempt a general replacement for the intermediary combinatorics (3.14)-(3.18).

## Equations (4.3)-(4.4): final tree restriction

Let `H=F(|<=2)` under Definition 7: aligned repeated index 1 is forbidden, and repeated index 2 needs an intervening index 1. Root and leaf edges remain included.

For root index 1, a nonlinear term can only have index-2 leaves, and those leaves cannot grow: another 1 would repeat the root index, while another 2 without an intervening 1 is forbidden. Thus `H1=y1+y2^2`.

For root index 2, every child of a nonlinear root must be index 1, since a child of index 2 would immediately repeat index 2 without an intervening 1. Each index-1 child has value `y1+y2^2`; its possible index-2 leaves are separated from the root by index 1. Therefore

```text
H1 = y1+y2^2,
H2 = y2+(y1+y2^2)^2.
```

In particular, `(4.4)` asserts `F1=H1`, although their `y1^2` coefficients are 1 and 0. This is a decisive failure even without computing `H2`.

The final trace partition by minimum index is not the source of this discrepancy. At any common formal argument `X`, the index-1 factor is `1+2(X1-X2)` and the all-2 factor is its reciprocal. Their product is 1, as required by the determinant hypothesis. Thus Lemma 5.1's determinant cancellation works on this example. Reading the common final argument in (4.3) as `H` (the natural `k=n` reading of its printed notation), its right side is `H`, and the same coefficient refutes (4.3). No repair of the determinant cancellation can make the already unequal tree sums equal.

## Negative control and exact limits

For the triangular shear `V=(x2^2,0)`, the inverse is `F=(y1+y2^2,y2)`. Its sole nonlinear tree has root index 1 and leaf indices 2, so both source restrictions retain it, and `G=H=F`. Its derivative matrix has only its `(1,2)` entry nonzero; every closed trace word has zero weight. Thus all three charged identities pass on this control. The failure test therefore does not reject an allowed triangular one-vertex tree or introduce a universal normalization error.

Excluding root or leaf edges from alignment would alter the explicitly charged source definitions. This report does not adjudicate a replacement restriction, and does not assert that every reinterpretation is impossible. The source's own length-one base case in Lemma 5.2 also counts the single external edge, consistent with the reading used here.

The result is a finite coefficient refutation of universal identities, not a finite-family attempt to settle JC2. It requires no literature-bound dependency, no quotient/localization transfer, no probabilistic evidence, and no claimed different-model promotion. There is no claim about later versions or an author's unprovided correction.

## Replay and completion

All mathematics above was recomputed manually from the frozen primary equations. Reproduce the input check and extraction with:

```sh
sha256sum box/magnen-tree-screen-swarmHQ-20260914/magnen-v1.pdf
pdftotext -f 1 -l 7 -layout box/magnen-tree-screen-swarmHQ-20260914/magnen-v1.pdf -
```

Then multiply the displayed two-by-two matrices and compare the three displayed degree-two coefficients. No software verification tier is claimed. This report stops at that decisive countercheck; no proof-repair successor is proposed.

The local artifact uses the assigned administrative transaction `begin -> close -> finalize -> verify`, at the basis stated above. The finalizer manifest accompanies the report. Root must independently verify the published bytes after this lane is terminal; this producer's seal is not a promotion receipt.

## OPENs raised

None. The charged universal formulas have a finite, explicit countercheck; no additional unresolved task is needed for this disposition.

## COLLISIONS

status: EMPTY (manual; no corpus scan)

- NONE: the report raises no named open question. This is not a claim that the result has no historical duplicate.
- The standard collision program was inspected but not executed: its `main` calls `banked_corpus` even when the question list is empty. The lane's explicit ban on reading ROOT or other report bodies takes precedence during independent work. Root may run the standard administrative collision check after all independent lanes are terminal.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `11092`.
- Body SHA-256:
  `507bb49fdd8d5a6e59e2d952b93012c623c2dd013f213836c385a86b959caa30`.
- Frozen basis: `9131f71b35f524751a1182f4f4f7cc7cca6afda9`.
