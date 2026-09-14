# Carrier degeneration at the degree-(75,125) frontier of the plane Jacobian problem

## Exact root-jet obstructions, an uncomposed reduction lemma, and reproducible data

Will Strinz

Draft of 22 August 2026

## Abstract

We give a reproducible exact-computation study of the degree pair `(75,125)`
in the two-dimensional Jacobian problem. The mathematical center is an exact
obstruction theory inside an explicit normalized Family-F2 carrier model. We
classify the K3/K4 root jets and the first K5 post-root-jet obstruction. K5
eliminates the generic K4 roots and confines
survivors to explicit deeper-contact strata; those strata are nonempty and
positive-dimensional. Corrected K6/K7 equations impose only partial further
conditions, and the tested K8 Chang--Wang selector cancels identically under
its stated pins.

Separately, we extract from published standard-pair and complete-chain
machinery a fixed-degree reduction: over a characteristic-zero field, a
hypothetical Keller pair of degrees `(75,125)` can be carried over the
algebraic closure to the Family-F2, `j=1`, standard configuration with initial
corner `(5,20)`. This unconditional front end is chiefly a specialization and
proof extraction from published results. The carrier theory is the new part,
but it is conditional on a normalized model that has not been attached to the
actual standardized pair. A characteristic-zero Gate-B census closing 26 of
32 support cells is provided as a reproducible data appendix; the six open
cells are precisely the largest support cells.

The actual-pair-to-carrier source theorem is not proved, and six
Gate-B cells remain open. Consequently this work neither excludes nor
constructs a degree-`(75,125)` counterexample. Its contribution is an exact,
auditable classification of where the present carrier obstruction ceases to
force a contradiction, together with a careful front-end reduction and a
reproducible finite-algebra dataset. A narrow local K5
criterion is additionally formalized in Lean and replayed through Comparator,
Lean's kernel, and NanoDa.

## 1. Status and scope

For polynomials `P,Q` in two variables over a characteristic-zero field, the
Keller condition is that the Jacobian determinant `[P,Q]` is a nonzero
constant. The plane Jacobian conjecture predicts that every such pair defines
a polynomial automorphism. The present note concerns the fixed degree pair

```text
(deg P, deg Q) = (75,125).
```

The overall case remains open. Two distinctions are load-bearing throughout:

1. The fixed-degree reduction concerns an actual Keller pair after a
   polynomial automorphism over an algebraic closure.
2. The carrier theorems concern coefficients satisfying a separately
   constructed normalized F2 carrier model.

The source theorem that would attach the output of the first theorem to the
literal inputs of the second has not been constructed. It requires
approximate-root, Puiseux/Laurent-support, and nonmonomial coordinate-transport
control at specific coefficients; it is not merely a bookkeeping dictionary.
We therefore do not compose the two results and do not claim an exclusion of
`(75,125)`.

All computational claims are graded individually as written proof, exact
checked arithmetic, kernel checked, or modular reconnaissance. Modular solver
output is never promoted to a characteristic-zero theorem.

## 2. Front-end reduction lemma to Family F2

The published GGV standard-pair machinery associates to a counterexample a
reduced ratio `(m,n)` and a complete Newton chain. For degrees `(75,125)`, the
ratio is `(3,5)` and the original degree gcd is `25`. The proof extraction used
here has two steps.

First, the subrectangular normalization argument is read without the
minimality upgrade: one retains the weaker transformed-gcd bound `g <= 25`
instead of forcing an equality at the normalization stage. The existence of a
normalizing automorphism over an algebraic closure of an arbitrary
characteristic-zero base field is obtained by transferring a finite
polynomial witness. Coefficients of the automorphism and its inverse,
composition identities, finite support vanishings, and the nonvanishing
corner coefficient form a finite polynomial system. A complex solution and
the weak Nullstellensatz produce a solution over the algebraic closure of the
original coefficient field. This transfers existence; it is not descent of a
chosen complex automorphism and produces no automorphism over the base field.

Second, the complete GGV family census through `g <= 25` is replayed. In the
`(3,5)` ratio the unique admissible row is Family `F2`, `j=1`, with

```text
A0 = (5,20),    transformed gcd = 25.
```

Thus every hypothetical characteristic-zero Keller pair of degrees
`(75,125)` becomes, after an automorphism over the algebraic closure, a
standard `(3,5)` pair in that F2 row. This is an existential,
automorphism-relative theorem. It does not say that the original coordinates
already exhibit the F2 corner.

The family census and Newton-polygon inputs are cited published results. The
minimality-free proof extraction and finite-witness transfer are written and
exactly custodied here, but are not presently formalized in a proof kernel.

## 3. The normalized F2 carrier model

The carrier calculation organizes successive coefficient constraints into a
filtration K1, K2, and so on. The first three levels force enhanced common-root
divisibility. At K4 the global polynomial problem splits into finite local
root-jet conditions on the three classified residual branches: one
squarefree branch `S0` and two repeated-root branches `S+` and `S-`.

On the squarefree branch, the K4 statement includes the global condition

```text
S0(w) divides P13(w).
```

This is forced by K4 polynomiality inside the normalized model, not imported as
a second hypothesis: modulo `S0`, the squarefree-branch K4 numerator is
`27*lambdaP^2*P13^2`; the scalar guard and squarefreeness give exactly
`S0 | P13`. Omitting the condition would overstate the local classification.
Subject to the stated guards and this derived global condition, the K4
root-jet equations are necessary and sufficient. On a regular K4 stratum,
a regularized local value `Z` satisfies

```text
27 Z^2 - 9 Z + 1 = 0,
```

and the remaining equation uniquely pins its derivative jet. On a
deeper-contact stratum the value collapses to `Z=0` and the derivative
direction remains free.

The three-branch classification is proved by exact symbolic reduction and
Chinese-remainder/local-jet calculations. Independent Poisson/cokernel
replays at pinned witnesses reproduce the same equations on all three
branches. These witness batteries are strong hostile controls, but they are
not represented as a second all-parameter proof.

## 4. The first post-root-jet obstruction

At a guarded double root `rho`, write

```text
m = ord_rho(G),        k = ord_rho(P13).
```

The corrected K5 valuation calculation eliminates every generic K4 root. Its
deeper-contact classification is:

- if `k >= 2`, the stratum survives K5;
- if `(m,k)=(1,1)`, it fails K5;
- if `(m,k)=(2,1)`, it survives exactly after one explicit affine tuning of
  `P12(rho)`;
- if `m >= 3` and `k=1`, it survives exactly when `P12(rho)=0`.

The last clause is important. An earlier audit had silently fixed
`P12(rho) != 0` and consequently overstated the exclusion. Exact positive and
hostile fixtures now lock the corrected statement.

On the tuned `(2,1)` locus, the order-twenty coefficient does not impose an
additional survival equation. Its nonvanishing gives exact order twenty; its
vanishing gives still deeper order. The result therefore classifies a genuine
survivor locus rather than leaving a generic computer-algebra problem
unresolved.

### 4.1 Kernel-checked local criterion

One especially transparent branch is formalized independently in Lean. Let
`X` be a local parameter and let `N5` be the displayed denominator-cleared K5
numerator. Assume

```text
r   = X^2 r0,   r0(0) != 0,
P14 = X^6 a,
P13 = X b,      b(0) != 0,
lambdaP != 0,   lambdaQ != 0.
```

Then

```text
X^20 divides N5    if and only if    X divides P12.
```

After the factorizations are substituted, every term is visibly divisible by
`X^20` except a nonzero scalar multiple of

```text
X^19 b P12 r0^9.
```

The theorem is stated using only ordinary Mathlib polynomial definitions. The
Challenge file exposes the complete numerator and every hypothesis. Comparator
confirms that the Solution proves exactly that declaration; the exported proof
is accepted by Lean's kernel and the independent NanoDa kernel. This formal
result certifies only the local polynomial criterion, not the carrier
derivation or the `(75,125)` reduction.

## 5. Independent F2 overlap and the unresolved filtration crosswalk

The polynomial `27T^2-9T+1` also occurs in Roy van Rijn's independent public
F2 programme. There it constrains a descent-eight relative coefficient `T=y`;
here it constrains a regularized K4 local root jet `T=Z`. The shared formula is
not, by itself, an identification of variables or theorems.

The next-stage behavior makes the missing crosswalk mathematically important.
This carrier model eliminates both generic `Z` roots at K5, with resultant
`63`, while Roy's tested return packet retains both `y` roots through `v^10`.
These statements are not presently contradictory because no exact map relates
the variables, branch guards, normalization choices, or filtration levels.
There are three live possibilities: the parameters are different; they are the
same and one computation exposes an error; or they encode the same local datum
but are subjected to different later obstructions. Resolving that trichotomy
is the highest-value comparison left by this release.

## 6. Where the carrier continuation stops

A corrected depth-five support dictionary preserves the K5 divisibility
geometry while retracting an earlier false conclusion that a shear parameter
must vanish. Corrected K6 and K7 equations constrain portions of the K5
survivor locus but leave explicit higher-degeneracy families.

At K8, under the stated `kappaEdge=2` and top-row pins, the proposed
Chang--Wang coefficient selector cancels exactly:

```text
f_-115 = 0.
```

This is a negative structural result, not an exclusion theorem. It explains
why continuing the same selector search is not presently justified. Higher
coefficient marching would require a new global relation capable of acting on
the surviving contact invariants.

## Appendix A. Complementary finite-algebra dataset: Gate B

An independent finite-algebra programme studies a 32-cell support atlas. Exact
characteristic-zero ideal identities close 26 cells. The six open cells are
the five support-size-four faces and the support-size-five face.

Custody is reported cell by cell:

- 23 closures have portable exact payloads;
- two large one-slice identities are retained under digest-backed custody;
- one three-cell result is deterministically regenerable, but its full
  historical Gröbner/cofactor payload is not retained;
- six cells are open.

The public custody matrix records each statement, artifact, checker, hostile
control, formal consumer, and replay command. The mixed custody distinction is
intentional: a historical exact result is not silently promoted to a portable
certificate merely because the theorem count is convenient.

The cell count is a census, not a progress percentage: the six unresolved
cells are the five size-four supports and the size-five support. Gate B is
complementary to the carrier programme. It does not repair the
actual-pair-to-carrier attachment, and the carrier results do not close the six
remaining support cells.

## Appendix B. Reproducibility and proof custody

The release is organized by theorem rather than campaign chronology. Each
headline bundle contains a statement, hypotheses, exact checker or written
proof, retained receipt, hostile controls where applicable, and a dependency
record. A generated release manifest states the overall theorem status as
`OPEN` and the Gate-B count as `26/32`.

The quick release battery replays the five headline bundles, the Gate-B census,
and the claim/supersession ledgers. The formalization subtree pins Lean,
Mathlib, Comparator, Lean4Export, and NanoDa revisions. A fresh Linux replay
passes Comparator and both kernels. SHA-256 digests cover the retained release
artifacts.

The source campaign used extensive AI assistance for symbolic discovery,
formalization, adversarial scope review, code generation, and orchestration.
The human maintainer selected the claims, required exact or kernel-checked
receipts, directed corrections, and is responsible for the release. The AI
role, model families, review status, and known gaps are disclosed in the
Palomar metadata and release files.

## 7. What is and is not established

The work establishes, without composing the first two items:

1. an exact K3/K4 root-jet theorem and corrected K5 survivor theorem inside the
   normalized carrier model;
2. a precise positive-dimensional locus on which the present carrier mechanism
   stops;
3. a fixed-degree reduction of a hypothetical `(75,125)` pair to the standard
   F2 row, chiefly as a written specialization/proof extraction from cited
   inputs;
4. an exact 26/32 finite-algebra dataset with explicit mixed custody;
5. a kernel-checked short local K5 polynomial criterion.

It does not establish:

1. the source/support attachment from an actual standardized pair to the
   carrier model;
2. an exclusion or construction of a degree-`(75,125)` counterexample;
3. closure of the six remaining Gate-B cells;
4. literature-wide novelty for the carrier formulas;
5. external peer review of the written reduction or carrier model.

## 8. Open problems

The most useful continuation questions are now narrow.

1. Construct or refuse an exact crosswalk between this work's `Z` and Roy's
   `y`, including the K5/return-filtration comparison.
2. Construct the literal source/support theorem from the standardized F2 pair
   to the carrier inputs, without replacing it by an abstract premise.
3. Lift one tuned `(m,k)=(2,1)` model survivor toward an actual standard pair
   and record the first exact failed or missing source condition.
4. Find a global mate, contact, or intersection relation that acts on the
   surviving `(m,k)` strata.
5. Produce compact original-generator certificates for any of the six open
   Gate-B cells.
6. Regenerate the three non-portable Gate-B custody entries into a uniform
   public receipt format.

Routine K9/K10 marching, another generic high-memory Gröbner run, or another
search for the cancelled selector is not supported by the present evidence.

## 9. Availability

The public repository is
<https://github.com/wstrinz/plane-jacobian-75-125>. Reproduction instructions
are in `REPRODUCE.md`; precise theorem boundaries are in `THEOREMS.md`; the
active mathematical seams are in `OPEN_FRONTIER.md`. The Palomar candidate is
under `formalization/` and is intended to be submitted at a pinned public
commit. A versioned archival release is planned through Zenodo.

## References

The full bounded bibliography and theorem anchors are maintained in
`literature/REFERENCES.md`. The claim-by-claim comparison with the cited GGV
and GGHV literature and Roy van Rijn's public F2 programme is in
`literature/NOVELTY_MATRIX.md`. Classifications there are deliberately bounded:
“apparently new” means only that no matching statement was found in the named
comparison set.
