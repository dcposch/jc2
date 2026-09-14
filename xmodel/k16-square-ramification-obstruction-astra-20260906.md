# K16 square/ramification budget: a precise no-gain result

2026-09-06. Desk lane `model_productivity`; basis
`0d39df3c9fd69c939a8420c54d03228b9077777d`.

**Verdict: NO-GAIN for the direct polynomial-abc/critical-fibre mechanism.**
The exact multiplicity budget below is compatible with every target degree.
Its complementary-factor term cannot be deleted, and the differential
identity does not force selected simple roots into the critical divisor:
there are exact compatible formal germs at those places. This is a delimited
failure of a proposed obstruction, not a theorem that all rational-map
methods fail. The polynomial `B*eta!=0` target remains OPEN.

## 1. Scope, frozen sources, and notation

Read completely: `k16-boundary-product-astra-20260906.md` and its Fable gate.
Read ueta classification §§2–7; f3abel §§6–7; Series §3; Xempty §§7.2–7.3.
The six report names and immutable full hashes are in
`box/k16-square-ramification-20260906/sources.sha256`, reproduced here:

| report in `xmodel/` | SHA-256 |
|---|---|
| `k16-boundary-product-astra-20260906.md` | `1c4a1100cc774932f23da27e11bf828a6fa10d5e256ce1528694d356d9031d9c` |
| `k16-boundary-product-gate-fable5-20260906.md` | `d40a0aefde728d22f0b4e38aaef908dd2c59408b3e0fee1631ca17b35d5e1130` |
| `k16-ueta-classification-astra-20260906.md` | `f04c483c94f9c1320e4d630cfd52422ca3730ad396d0d653c3d3ef2a2c49e8ac` |
| `k16-f3abel-astra-20260905.md` | `0d2b27fed00a27a1f21d0997adce38252405506839d74f674327f2ff994b22b4` |
| `k16-universal-series-fable5-20260905.md` | `5ac0ff1ddcfc766dd1d5050c73e08203795f1ecc56be954b388ef0c1eaeb41bb` |
| `k16-xempty-astra-20260905.md` | `1f06694fb58d53c4a4b3c54dad88722cd31a5ccc894679ac52b0620b91e2623f` |

Within these six terminal reports, searched `abc`, `Mason`, `Stothers`,
`ramification`, `rational.map`, `critical.value`, `squarefree`, and the
root-contact/residue passages. The direct degree budget proved below was
not present in this search scope. Earlier RC6/RC8 retain repeated roots;
ueta §7 already explains why simple nonzero W roots are not excluded by
the `B=0` parity argument. Series' infinity residues only recover top
balance. None is represented here as a newly discovered obstruction.

Work over an algebraically closed characteristic-zero field k. On `B*eta!=0`
use the reviewed normalization `B=eta=1`, with the individual leading
coefficient of A moving. Put

```text
n=m-1>=3, q=2n+1, N=4n+1=2q-1,
Z=xA, D=(3/4)Z^2, deg Z=n,
R=(x/3)D^2-D-1,
J=2W'-(W+1)/x+2D,   E=x(WJ-R).
```

The target keeps `deg W=q`, `deg J=q-1`, `W(0)=-1`, `W'(0)=1`.
The review confirmed that its full equation already imposes
`lc W/(lc A)^2=1/[4(2d+1)]` for one of the two roots `3d^2=m`.
Everything below holds separately after either embedding, including both
rational factors when `m=3s^2`; no sign or leading coefficient is fixed
by convenience. There is no coefficient-ring radical assertion here.

Use the reviewed finite-algebra isomorphism

```text
f(t)=3t(t-1),
Q(t)+1 = S(t) = (27/4)t^2(t-1)^3 A(f(t))^2,
k[x]/(R) <-> k[t]/(Q),  t=xZ^2/4, x=f(t).
```

It preserves each local length, hence root multiplicities, even at the
fixed ramification place. Both R and Q have degree N. For any nonzero
polynomial H let `r(H)` count its distinct roots and
`e(H)=deg H-r(H)` its repeated-root excess.

## 2. Exact ramification budget, including repeated roots

**Lemma.** Let `r=r(Z)` and let `delta=1` if `Z(-3/4)=0`, otherwise zero.
Then

```text
r(S)=2r-delta,
e(Q)=e(R) <= 2r-delta-1 <= 2n-1,                       (RB)

(q-r(W))+(q-1-r(J))+h <= 2r-delta-1,                  (RB-WJ)
h = number of distinct common roots of W and J.
```

Proof of the first equality with multiplicities: let `s=ord_0 Z>=1`.
The roots `t=0,1` of S have orders `2s,2s+1`. Each nonzero root of Z,
away from `x=-3/4`, of order a gives two roots of S, each of order `2a`.
If Z has order a at `-3/4`, the sole preimage `t=1/2` has order `4a`.
These account for the entire degree `4n+1`. Thus merging that preimage
subtracts exactly delta from the count, with no squarefree assumption.

For a nonconstant polynomial H in characteristic zero,
`deg gcd(H,H')=deg H-r(H)`, by the local derivative order at each root.
Since `S-Q=1`, the polynomials `gcd(S,S')` and `gcd(Q,Q')` are coprime;
their product divides `S'=Q'`, of degree N-1. Consequently

```text
(N-r(S))+(N-r(Q)) <= N-1.
```

This proves (RB) directly; no outside abc or Riemann–Hurwitz theorem is
being invoked. Finally `r(R)=r(W)+r(J)-h`, since `R=WJ`. Subtracting this
from `deg R=q+(q-1)` proves (RB-WJ), including repeated/common factors.

The exact lost term is visible in the equivalent inequality

```text
r(W) + [r(J)-h] >= N+1-2r+delta.                       (GAP)
```

For `r=n, delta=0` the right side is `q+1`. Replacing the left side by
`r(W)<=q` would create a spurious contradiction by dropping the bracketed
complementary-factor term. The actual degrees allow `r(W)=q`,
`r(J)=q-1`, `h=0`; then `e(R)=0`, fully compatible with (RB). More repeated
roots tighten an upper bound on e(R); the equation has not forced the
positive lower bound needed to contradict it.

## 3. The critical divisor and the exact differential contact

One can see precisely what a stronger ramification argument would need.
Differentiation, writing A' for derivative in x before substituting f,
gives

```text
S'=(27/4)t(t-1)^2 A(f(t)) C(t),
C=(5t-2)A(f(t))+6t(t-1)(2t-1)A'(f(t)),
deg C=2n-1=q-2.                                        (CP)
```

The leading coefficient in C is `N*lc(A)*3^(n-1)`, nonzero. At a Q root,
`t`, `t-1`, and `A(f(t))` are units, and
`Q'=C/[t(t-1)A(f(t))]`. Thus the roots that consume e(Q) are exactly
the Q roots lying in this remaining critical divisor (with derivative
multiplicity). If the degree-q divisor selected by W were forced into
C, there would be a strict degree contradiction. Local contact does not
force it there; proving such a consequence of all global constraints
would be a new, presently missing theorem.

At a W root `alpha!=0`, set

```text
w=W'(alpha), D0=D(alpha), t=alpha*D0/3.
alpha=3t(t-1), D0=1/(t-1),
J(alpha)=2w+(6t-1)/alpha,
(2t-1)D'(alpha)=w*J(alpha)-D0^2/3.                     (DC)
```

These follow by differentiating `R=WJ`. For a simple W root disjoint
from J, the exact derivative relation is

```text
Q'(t)=3(t-1)R'(alpha)=3(t-1)w*J(alpha),
C(t)=3t(t-1)^2 A(alpha) w*J(alpha) != 0.               (NC)
```

The formula for Q' also follows directly from Q, so it remains valid at
`t=1/2`, without cancelling `2t-1`. Thus simple compatible selected roots
are NONcritical, not a source of additional ramification.

**Local realizability to all formal orders, not just a first-jet count.**
Fix `alpha!=0,-3/4`, either root D0 of
`alpha*D0^2/3-D0-1=0`, and any formal germ W with `W(alpha)=0` and
`w!=0`, `2w+(6t-1)/alpha!=0`. The equation for D is

```text
F(D)=(x/3)D^2-(2W+1)D-1-2WW'+W(W+1)/x=0.             (LF)
```

Its D-derivative at the marked place is `2t-1!=0`. Solve successive
coefficients in `k[[x-alpha]]`: at each order the new D coefficient has
that same nonzero pivot, all other terms being already determined.
This constructs a unique formal power series D with initial value D0.
Since D0 and alpha are nonzero, the square-root recursion gives
`Z^2=4D/3`, `A=Z/x`. Thus the full local equation and its square shape
hold to every formal order, while `R'=wJ!=0`. This is a local statement
only: these germs need not be polynomial or satisfy the origin/infinity
markings. It explains why local contact cannot supply the missing
ramification margin; global degree-constrained compatibility is still
required.

At `alpha=-3/4`, a root of R has `D0=-2`, `R'=4/3`, `Q'=-2`.
If selected by W, `3w^2-4w-2=0`, hence w and J are nonzero. For an
explicit formal control at this exception, take D identically -2 near
alpha and choose either slope `w=(2+/-sqrt(10))/3`. At order k>=2 the
new W coefficient has pivot `2(k+1)w-8/3`, nonzero because w is
irrational over Q. Recursive solution of `WJ=R` therefore exists here
too. Its A is locally `sqrt(-8/3)/x`, not a global polynomial.
The double zero of `W(f(t))` at the fixed point is ramification of f;
Q itself is simple. Counting that double zero as e(Q) would be wrong.

## 4. Shape-only negative control and the boundary of the conclusion

For every n>=3 set `A_lambda=lambda*(x^(n-1)+x+1)`, lambda nonzero.
This is nonmonomial, and `L=x^2 A_lambda` has support gcd 1. Put
`S_lambda=lambda^2 S_1`, `Q_lambda=S_lambda-1`. For all but finitely
many lambda, Q_lambda is squarefree: a multiple root requires
`S_1'(t)=0` and `lambda^2 S_1(t)=1`, hence a nonzero critical value in
a fixed finite set. The finite-algebra isomorphism makes R_lambda
squarefree as well. Choose any q of its N roots, normalize their factor
W by `W(0)=-1`, and set J=R_lambda/W. Then

```text
deg W=q, deg J=q-1, W(0)=-1, J(0)=1,
WJ=R_lambda, r(W)=q, r(J)=q-1, h=e(R_lambda)=0.
```

These are controls for the shape/factor/ramification argument ONLY.
They do not assert `W'(0)=1`, the prescribed leading ratio, or J's
differential definition. In particular they are neither target
counterexamples nor the already excluded `B=0` monomial family. The
formal controls in §3 test the extra local differential linkage;
neither set of controls is being glued into a global polynomial pair.

The unclosed obligation is now precise: exploit the simultaneous global
polynomial degree bounds, both markings, and the full differential
identity to prove a root excess beyond (RB), or some other obstruction.
Local ramification and the direct polynomial-abc inequality do not do
this. No finite-m solve, sampled rank, pole-rigidity reproving, infinity
residue promotion, or proposed exhaustive search is substituted for it.

## 5. Exact checks and custody

Owned evidence: `box/k16-square-ramification-20260906/`. The standard-
library `check.py` uses exact rational truncated series at `alpha=28/3`,
with `W=x-alpha`, `D0=3/4`. It verifies the ring map and literal E through
order 10; in particular `D'=1077/1232`, `R'=95/28`, `C(t)=95/21!=0`.
It also checks the fixed-point identities. The degree-uniform proofs
are the coefficient recursions and derivative-divisibility argument
above, not this finite jet. Its explicit exceptions survive `python -O`;
a changed D' is the required failing mutation. Exact run status and
source/checker hashes are retained in custody alongside the checker.

No fleet, CAS package, heavy computation, live lane body, shared-ledger
edit, or `jc2-lean` access. New report publication is transactional.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10574`.
- Body SHA-256:
  `ee7a62c7811ea866c4569161db21f813e76fac26c4d69203e90210af462d0cd4`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
