# JC2 significant-connection round packet — `20260824T1820Z`

Cutoff: `2026-08-24T18:20:00Z`  
Clean charged basis: `7832fb73ac887041968f9cec2dc6cba7aa0d0bcf`  
Previous full round: `20260824T1633Z`, closed `2026-08-24T17:14Z`  
Round trigger: a newly discovered primary-source reduction by Pinchuk, its
exact generalized Davenport--Zannier connection to the new maximum-12
spectral invariant, an approximate-cubic Kuranishi simplification, and a
provisional generic TD6 `c1`-line exclusion.

This packet is immutable. Events after the cutoff belong to synthesis or a
follow-on round. Ideators must not read one another's reports before freezing
their own submissions. Ongoing exact computations and hostile reviews remain
nonblocking.

## Canonical snapshot

Read all 46 numbered avenues in `APPROACHES.md`, plus `AUDIT.md`,
`PROGRESS.md`, the newest `LIVE STATE` in `notes.md`, `COORDINATION.md`, and
`ladder/REDUCTION.md`. At cutoff their SHA-256 hashes were:

```text
da001ad6da24b66bf8f9d710c5b4bcdf14d5f5420927315d7d5b91d25a3d9794  APPROACHES.md
2debde002e49b0d2d45d5862112fba5c2b5da0b6e4a2b954a7939b53e296eac7  AUDIT.md
63ff1eafd836d0f04ee3e4321a97965a11a3d316f07c54e9337b042e1cb1e4a5  PROGRESS.md
93ebb398a0d951e625e565235dbf725ffdada707aeb75665b0d5986574ab528e  notes.md
2bed8117d2137bd9f93d558d7b9aca98a02a21c5b42688fc181e99d683f537cd  COORDINATION.md
f0fca49811349483c437d674ab819065eb09500330516d161978868c71bf6371  ladder/REDUCTION.md
```

The newest canonical state is `2026-08-24 17:54Z LIVE STATE`. The only policy
delta afterward is commit `7832fb73...`, which requires every `p`-adic
successor residual to be derived as an exact integral quotient before
reduction, with divided carries and an independent exact-source control.

## Reviewed theorem delta

Different-model hostile review and fail-closed composition now prove:

> No characteristic-zero Keller pair has actual partial `y`-degrees `(6,9)`
> with `3|H`; consequently every characteristic-zero Keller pair with maximum
> actual partial `y`-degree at most 11 is a polynomial automorphism.

The proof has no `x`-degree bound. This is not JC2. The first maximum-12
primitive cells are exactly `(8,12)` and `(9,12)`.

## Provisional maximum-12 delta

The frozen preflight and shared high-row compiler are under different-model
hostile review:

```text
30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07  xmodel/max12-partial-y-kummer-preflight-20260824.md
d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036  xmodel/max12-partial-y-shared-faber-probe-20260824.md
```

Producer-exact facts, not yet promoted:

- For monic depressed `f,g` of degrees `(m,n)`, `w=f^(1/m)` and the Faber
  expansion give constants `h_j` and the complete lower system
  `r1'=...=r_(m-2)'=0`, `m*r_(m-1)'=j/u`.
- Aggregate mandatory-route width selects `(9,12)` for speed. Its order-three
  branch has `H(w)=w^12+k*w^6`,
  `r1=r2=r4=r5=r7=0`, `r3=mu`, `r6=nu`, and
  `9*r8'=j/u`. The terminal descent is `r8=u^2 R` and
  `9hR'+6h'R=j`; the exact control
  `h=x^2(x-1)^4`, `R=C/[x(x-1)^3]` gives `-3C`, so the ODE alone is not an
  exclusion.
- In triangular approximate-cubic coordinates
  `K=z^3+pz+q`, `f=K^3+sum_(0..5) x_i z^i`, the common-cubic locus is
  `x_i=0`. On `k!=0` the normal linearization has rank three and kernel
  `phi=K*(A+Bz+C(z^2-p))`. The four exact restricted Kuranishi quadrics are

  ```text
  Q4=k*(-2AC-B^2+3pC^2)/9
  Q5=k*(-2AB+4pBC+qC^2)/9
  Q6=k*(-3A^2+10pAC+2pB^2+6qBC-9p^2C^2)/27
  Q7=k*(2pAB+4qAC+2qB^2-4p^2BC-7pqC^2)/27.
  ```

  Projectively `Q4=Q5=Q7=0` gives `[1:0:0]` and, for every root `B` of
  `B^3+pB+q`, the direction `C=1,A=(3p-B^2)/2`. There `Q6` is respectively
  `-k/9` and `-k(3B^2+p)^2/36`. Thus fixed `mu=nu=0` has no transverse first
  direction when `k!=0` and `K` is squarefree; `k=0`, `disc(K)=0`, nonzero
  invariant loads, Taylor boundaries, and the order-one core remain open.
- Exact elimination of a dummy cubic parameter gives the spectral polynomial

  ```text
  W=g^3-f^4-3*k*f^2*g-k^3*f^2.
  ```

  It vanishes on `f=K^3,g=K^4+kK^2`. If
  `g=H(w)-T`, then
  `W=-3*(H^2-k*w^18)*T+3*H*T^2-T^3`, and
  `J(f,W)=3*(g^2-k*f^2)J(f,g)`. The first possible `z`-degrees from
  `r3,r6,r8` are `21,18,16`. On `k=mu=nu=0`, a coprime pair has
  `deg_z(g^3-f^4)=16`, exactly the polynomial-abc lower bound. This spectral
  connection is coordinator-derived and must be independently checked before
  promotion.

The exact fibre compiler is active; raw global Gröbner calculations are
cross-checks, not the only strategy.

## Newly discovered primary source

S. I. Pinchuk, *Quasi-polynomial mappings with constant Jacobian*,
Izvestiya: Mathematics 85:3 (2021), 506--517,
DOI `10.1070/IM9017`:

- authoritative landing page: `https://www.mathnet.ru/eng/im9017`;
- English primary text:
  `https://www.mathnet.ru/php/getFT.phtml?jrnid=im&option_lang=eng&paperid=9017&what=fullteng`.

This source was absent from the campaign history at cutoff. Treat it as
`SOURCE-FOUND / CLAIMS-UNREVIEWED`, not as a theorem input. Its Theorem 3.4
claims that any noninvertible plane Keller map is equivalent, through
polynomial and rational-power quasi-elementary source changes, to a reduced
quasi-polynomial map whose leading weighted pair already has constant
Jacobian. Its Theorem 4.1 states, for coprime positive `k,r`, polynomials
`p,q` of degrees `kd,rd`, and `m=k+r+1`, the equivalence of

```text
r*p'*q-k*p*q' in k*,
deg(p^r-q^k)=d*(k*r-k-r)+1,
J(x^-k p(x^m y), x^-r q(x^m y)) in k*.
```

Theorem 4.1's displayed degree identity is elementary and directly relevant
to the `k=0` maximum-12 spectral boundary with exponents `(4,3),d=3`, whose
minimum is 16. The much broader Theorem 3.4 has only a short reduction proof
and needs a hostile source audit, including equivalence directions,
termination, rational-power field changes, and whether invertibility or
polynomial recovery is preserved. Do not confuse this author/topic with the
real Pinchuk counterexample avenue.

## Corrected AS/Witt delta

The earlier 29-row deep-branch gate is quarantined: it omitted the divided
integer carry. The frozen source-honest replacement is

```text
cbcd8851200f2ab15c29a7b9414c1d720c7aee0aa852b2cd522dcd7d699ae194  xmodel/as-fonly-first-residual-divided-carry-deep-d7-erratum-20260824.md
e1e8bd61077354d3523c9b655980fe6118164fdbb67e7ff1930db064df0643f6  cases/as_fonly_first_residual_divided_carry_deep_d7_erratum_20260824/FREEZE.txt
```

Over the integers,
`det J(P0+3U,Q0+3V)-1=3L+9K`, and the true next residual is
`L/3+K+div(C,D)`, adding `u5_3+v5_2=0`. The corrected 40-variable/30-row
ideal has producer GB size 269, dimension 18, is nonradical, and has an exact
nonreduced three-piece cover; none of the pieces is claimed primary or
minimal. Hostile review is active. Degree-ten accepted-digit/mixed-carry work
continues from the original nonreduced ideal.

## Provisional TD6 delta

The frozen common-centering tangent gate remains under independent
3,602-column reconstruction. The exact nonlinear `c1` base-line pencil has
now completed at producer level:

```text
transport 3470/3602; first 38/132; previous+pole 38/94; current 25/56.
```

There are nine nonzero generic current compatibilities and their canonical
numerator gcd is one; one residual is already a nonzero constant. Therefore
the generic pivot open of the `c1` line is empty. This is not whole-line or
family coverage: later pivot factors of degree up to 16 have exceptional
strata that require denominator-cleared certificates or exact rebuilds. The
`c3` dual thickening and Fitting data remain active.

## Active allocation and review debt

- Internal research: `(9,12)` order-three exact fibre/Kuranishi; corrected AS
  degree-ten successor; TD6 `c1,c3` atlas and exceptional strata.
- External hostile review: maximum-12 preflight, shared Faber theorem, TD6
  tangent reconstruction, and corrected AS carry scheme.
- Local exact computation: original and approximate-cubic fibre Gröbner
  cross-checks plus TD6 base/dual arithmetic.
- AWS remains stopped: current gates are exact symbolic/certificate
  bottlenecks, not memory-capacity bottlenecks.
- Broad sweep #9 was due at `21:25Z`; the Pinchuk discovery starts early
  intake. Absence from prior searches is not novelty evidence.

## Campaign-wide questions for this round

1. Can the generalized Davenport--Zannier equality cases at `(4,3),d=3` turn
   the `k=mu=nu=0` maximum-12 boundary into a finite rigid list, and can its
   affine/scaling trajectories plus original Taylor boundaries be excluded?
   Is there a comparable spectral/curve argument for `k!=0` or nonzero
   `mu,nu`?
2. Does Pinchuk Theorem 3.4 genuinely create a new global reduction client,
   merely rename existing Newton/q-polynomial work, or contain a scope gap?
   Give its cheapest decisive source audit and any exact connection to
   `G2-PSC`, `G2-BD`, partial-`y` coverage, or counterexample construction.
3. What is the cheapest exhaustive split of the `(9,12)` order-three fibre:
   generic squarefree `K`, discriminant `K`, `k=0`, invariant loads, and
   Taylor boundaries? Can the spectral invariant bypass full primary
   decomposition?
4. After the AS carry correction and generic TD6 `c1` exclusion, which exact
   successor has the highest information gain? Can their certificate engines
   be simplified without losing nonreduced or exceptional strata?
5. What genuinely new proof, disproof, software, or cross-avenue mechanism is
   still missing? Search the repository before calling it new.

## Required blind submission contract

Give: (1) a compact `unchanged/raise/lower/reopen` disposition for all 46
numbered avenues, explaining every change; (2) reranked principal proof and
disproof bottlenecks; (3) at least one genuinely new mechanism and one new
cross-avenue connection; (4) strongest proof attack and strongest
counterexample/falsification attack; (5) one software accelerator or decisive
experiment; (6) no more than three detailed idea cards, each with explicit
dependencies, cheapest discriminator, interpretation of every outcome, stop
condition, and expected information gain; and (7) `continue/redesign/stop`
for every current major lane. Mark speculation, run the canonical
history/priority checksum, and do not overread provisional facts. Do not read
other ideation submissions before freezing your own report.
