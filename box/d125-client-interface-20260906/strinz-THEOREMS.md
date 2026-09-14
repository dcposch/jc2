# Theorem statements and trust boundaries

The overall degree-`(75,125)` case remains **open**.

## Theorem A — fixed-degree reduction to Family F2

Let `K` be a characteristic-zero field, let `Kbar` be an algebraic closure,
and let `(P,Q) in K[x,y]^2` have nonzero constant Jacobian and degrees
`(75,125)`. Then there is an automorphism `Psi in Aut(Kbar[x,y])` such that
`(Psi(P),Psi(Q))` is a standard `(3,5)` pair generating the admissible GGV
Family `F2`, `j=1`, with `A0=(5,20)` and transformed gcd `25`.

The result is existential and automorphism-relative. It does not assert that
the original coordinates already display the F2 corner. The field argument
transfers a finite polynomial witness and may construct a different
automorphism over `Kbar`; it is not descent of a selected complex
automorphism, and it produces no automorphism over `K`.

Evidence: written proof extraction and finite-witness transfer, with exact
custody checks. The published Newton-polygon census remains a cited input.

## Theorem B — K3/K4 carrier root-jet classification

Inside the exact normalized F2 carrier model, K3 imposes enhanced root
divisibility. K4 is equivalent to finite root-jet conditions on all three
classified residual branches. On the squarefree branch the statement includes
the global condition `S0(w) | P13(w)`. This is not an additional imported
hypothesis: under the carrier guards, reduction of the K4 numerator modulo
`S0` is `27*lambdaP^2*P13^2`, so squarefreeness makes the condition equivalent
to the squarefree-branch K4 polynomiality requirement. On the regular K4
stratum a normalized
local parameter `Z` satisfies

```text
27 Z^2 - 9 Z + 1 = 0,
```

with the derivative jet pinned by the remaining equations. Deeper-zero strata
have `Z=0` and retain a free derivative direction.

Evidence: exact symbolic necessary-and-sufficient classifier, plus independent
Poisson/cokernel witness batteries at pinned specializations. The latter are
not a second all-parameter proof.

## Theorem C — K5 obstruction and survivor classification

At a guarded double root `rho`, write

```text
m = ord_rho(G),   k = ord_rho(P13).
```

Then K5 eliminates every generic K4 root and has the following deeper-contact
classification:

- `k >= 2`: survives K5;
- `(m,k)=(1,1)`: fails K5;
- `(m,k)=(2,1)`: survives exactly on the explicit affine tuning of
  `P12(rho)`;
- `m >= 3, k=1`: survives exactly when `P12(rho)=0`.

On the tuned `(2,1)` locus, the order-20 coefficient stratifies exact order 20
from deeper order; it imposes no additional survival condition.

Evidence: exact valuation proof, exact positive and hostile fixtures, and
branch-local symbolic replay.

## Proposition D — current limit of the carrier continuation

Under the stated `kappaEdge=2` and top-row pins, corrected K6/K7 impose partial
conditions on the K5 survivor locus. The honest corrected K8 row makes the
candidate Chang–Wang coefficient cancel exactly:

```text
f_-115 = 0.
```

This is a limit theorem, not an exclusion theorem.

## Proposition E — complementary Gate-B frontier

The characteristic-zero Gate-B support atlas closes exactly 26 of 32 cells.
The six support-size-four/five top cells remain open. Custody is mixed: most
closed cells have retained portable cofactors; two large one-slice identities
are digest-pinned; one trio is deterministically regenerable without its full
historical GB/cofactor payload.

The six open cells are precisely the five size-four supports and the size-five
support, so `26/32` is a census, not a percentage estimate of proof completion.

## Non-composition statement

Theorem A concerns an actual pair after automorphic standardization. Theorems B
and C concern data satisfying the normalized F2 carrier-model hypotheses. The
map from Theorem A's output to those literal carrier data is not constructed.
Constructing it is a substantive source theorem involving approximate-root,
Puiseux/Laurent, and coordinate-transport control—not a bookkeeping dictionary.
Therefore these results do not compose to an exclusion of `(75,125)`.
