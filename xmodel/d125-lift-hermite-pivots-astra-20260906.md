# D125 polynomiality: 97 unimodular Hermite pivots

Root/Astra, September6 2026. DESK theorem, PRODUCER-CHECKED, awaiting
different-model review. No production source expansion, CAS, AWS allocation,
solver, point or properness. This is a cheaper presentation of the reviewed
sufficient source client, not an all-degree JC2 theorem.

## 1. Charged inputs and exact claim

Terminal frozen inputs:

- `xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md`,
  SHA `7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413`.
- Its different-model gate `xmodel/d125-minimal-receiver-gate-fable5-20260906.md`,
  SHA `cd69c23885de119e4bd910992dad5ef695e7b12013168ec1c401546d8aa6ed8d`.
- `xmodel/d125-small-polynomial-lift-gate-fable5-20260906.md`,
  SHA `4295593a57a65e4d31630aecdef0b54e9d6078935e07cfb5e64acfd83fae4122`.

All rehashed MATCH before this report. This task does not consume the live
engineering review/exporter or the separate B-reconstruction theorem.

Work over K=Q or K=Q[rho]/(rho²-3rho+1), retaining both conjugates in the
second presentation. For each of the three normalized polygon cases, fix
the COMPLETE reviewed outer/inner faces, including every zero coefficient,
and both target constants0. Keep lambda2,lambda3 as unrestricted indeterminates.
Use the full receiver polynomials A15,B25 and their exact lift

    g=v^-1, p=v^4*u-lambda2*v²-lambda3*v-v^-1.

THEOREM. The ideal of ALL105 negative-v lift rows in the receiver coefficient
ring is an affine polynomial graph eliminating exactly27 A coefficients and
70 B coefficients. Every diagonal block has determinant ±1. Thus this is a
coordinate-ring isomorphism over K[lambda2,lambda3], without a parameter
localization, rational-point loss, generic-rank assumption or changed field.
Any other equations, including the complete Jacobian and nonzero-c guard,
must be carried through this graph substitution. Then the complete source
quotient is isomorphic to its substituted quotient, not merely equinumerous
at geometric points.

Counts INCLUDING both lambdas and the common-case c,z variables would be
172/198/274 instead of269/295/371. No substituted production residual has
been constructed; fewer variables is NOT a measured solver advantage.

## 2. Exact triangular filtration of all negative rows

Write one member of total degree D, D=15 or25, as

    C(g,p)=sum_{s=0}^D C_s(g,p),
    C_s(g,gz)=g^s f_s(z),
    f_s(z)=sum_{i+j=s} c_ij*z^j.

Index each negative row by (s,t), where

    1<=s<=D, 0<=t<=floor((s-1)/5),
    R_s,t = [u^t*v^(5t-s)] C(v^-1,v4*u-lambda2*v²-lambda3*v-v^-1).

This is a bijection with the complete negative-row envelope in the charged
gate: for fixed t, s ranges5t+1..D. Put r_s=ceil(s/5).
The explicit multinomial in that gate shows

    R_s,t = f_s^(t)(-1)/t! + F_s,t,

where F_s,t depends ONLY on coefficients of total degree strictly greater
than s, and on the lambdas. Indeed a summand with b lambda2 factors and d
lambda3 factors has row exponent

    e=5t+3b+2d-(i+j).

For e=5t-s this requires i+j=s+3b+2d. If b=d=0 we get precisely
(-1)^(j-t)*binom(j,t)c_ij, the displayed derivative functional. Every other
summand has i+j>s. There are no same-level lambda terms and no infinite
series. Descending s therefore supplies a finite triangular system.

At s=D every F_D,t is zero. The fixed top is H³ for A and H5 for B,
where h(z)=H(1,z) is z²(z³+1) or z²(z+1)(z+1-rho)². Thus f_D=h³ or h5
vanishes at z=-1 to order at least3 or5. Exactly the r_D=3 or5 top negative
rows are identically zero. They impose no extra conditions on lambdas or
the lower coefficients. This accounts for all eight automatic top rows.

## 3. Literal free pivot slots

For each1<=s<D, choose the r_s coefficients

    c_{i,s-i}, i=0,...,r_s-1.

They are not fixed face coefficients in ANY of the three polygon cases.
Here is a direct check, independently supplemented by finite exact polygon
census in the checker. Since i<=floor((s-1)/5), s>=5i+1, and j=s-i>=4i+1.
The pivot is non-origin, has nonnegative coordinates, and i+j=s<D so is not
on the outer face. All polygons have the left p-axis boundary i=0.

- Unequal A additionally has 5i-7j<=3 and j>=i/2. Unequal B has
  5i-7j<=5 and j>=0. For a chosen pivot, 5i-7j=12i-7s<=-23i-7,
  strictly below both fixed inner faces, and the other inequality holds.
- Common3 has i-j<=3 for A or<=5 for B, besides j>=0. Here
  i-j=2i-s<=-3i-1, strictly below the fixed inner face.
- Common4 has i<=9 for A or<=15 for B, besides j>=0. Chosen i<=2
  for A or<=4 for B is strictly below that inner face.

These are the remaining sides of the literal four-vertex polygons. Hence
every selected pivot is an allowed free coefficient, including when a full
inner face fixes other coefficients of the same total degree to zero.
This argument is identical for rational and golden top faces: the slot and
fixed-face index sets are the same, while their coefficient values differ.

## 4. Unimodularity, not generic rank

At fixed s, the coefficient matrix of the selected columns in R_s,t is

    M_{t,i}=(-1)^(s-i-t)*binom(s-i,t),  0<=t,i<r_s.

Its determinant is (-1)^(r_s*s+r_s*(r_s-1)/2), hence ±1. To prove this,
factor (-1)^(s-i) out of column i and (-1)^t out of row t; the combined
sign is (-1)^(r_s*s). The remaining matrix evaluates binomial polynomials
binom(x,t), with leading coefficient1/t!, on the consecutive descending
nodes x_i=s-i. Its Vandermonde determinant is

    product_{i<j}(x_j-x_i) / product_{t=0}^{r_s-1} t!
      = (-1)^(r_s*(r_s-1)/2).

This is an integer identity, not a specialization or a numerical rank test.
The inverse matrix has integer entries by the adjugate formula. Its size is
at most3 for A and5 for B.

After higher levels have been solved, all r_s rows therefore solve the chosen
coefficients as POLYNOMIALS in the unselected coefficients and lambdas.
Substitution creates no nonconstant denominators. Iterating s=D-1 down to1
expresses all chosen coordinates as polynomials in the retained coordinates.
Conversely, assigning the retained coordinates and those polynomial graph
values satisfies every row. Elementary invertible block row operations plus
the triangular coordinate changes identify the negative-row ideal with the
97 graph equations. This proof works as a ring identity, including nonreduced
base quotients. An arbitrary extra ideal J is handled by the induced quotient
isomorphism: every generator of J is substituted, with none discarded.

There are sum_{s=1}^{14}ceil(s/5)=27 A pivots and
sum_{s=1}^{24}ceil(s/5)=70 B pivots. Together with the eight top zero rows,
these exhaust all105 rows, so no unexplained compatibility row is lost.
The remaining A counts are44/50/71; B counts126/144/199. Common cases addc,z,
all cases addlambda2,lambda3, yielding172/198/274. Golden encoding as a
rational polynomial ring adds rho and its quadratic relation, not a split
of any field-valued equation into coefficient parts.

## 5. Exact controls and scope of computation

`box/d125-lift-hermite-pivots-20260906/check.py`, SHA
`d68b5ee59fc161abf5196606095b8384c0ac535de6ec45bae581ea79d100ea8f`.
Standard-library-only code, fully read by its author, no Assert nodes: every
load-bearing check calls require and explicitly raises RuntimeError. No file
writes, CAS imports, worker controls or production entry point.

Controls:238 PASS in normal mode and238 PASS under python -O. All114 small
blocks (three polygons times14+24 lower levels) have their selected free
slots checked against the literal polygon and fixed-face lines, and their
determinants computed by exact Fraction elimination. Two toy degree6 fixtures
with lambda=(0,0),(2,-3) use repeated Laurent multiplication, a top
z³(z+1)³, arbitrary lower nonpivot coefficients, and the descending pivots.
Every negative coefficient vanishes. Changing the actual p coefficient by1
leaves exactly the nonzero row [u0*v^-1]=-1. This is a polynomiality control,
not a Keller/source point or a full degree15/25 expansion.

`--mutate-matrix` replaces one actual matrix row by another and loses its
unit determinant. `--mutate-drop-row` deletes the actual failed negative row
from the bad fixture. Both controls exit1 in normal AND optimized modes;
the unmodified checks exit0. The positive replay shell was rerun with
`set -e -o pipefail`, so an early failed pipeline could not be hidden by a
later successful command. Complete six-run batch took1.254s, under the
declared30wall/25CPU/512MiB limits. No long computation was run locally.

Replay each mode under these limits:

    timeout 30 bash -c 'ulimit -t 25 -v 524288; python3 box/d125-lift-hermite-pivots-20260906/check.py'
    timeout 30 bash -c 'ulimit -t 25 -v 524288; python3 -O box/d125-lift-hermite-pivots-20260906/check.py'

The two mutation flags above must each return1 in each mode. Script and all
three source hashes were checked unchanged after replay; the final report
uses the standard begin/close/finalize/verify transaction.

## 6. Decision and limits

This is a scoped new application of triangular coefficient extraction and
consecutive-node Hermite/Vandermonde matrices, not a claim of new general
mathematics. The root found it during the theorem-interface composition pass
for the now-reviewed105-row lift. It does not depend on the unreviewed
separate B reconstruction, and does not assert that their variable savings
can be added. The optional two-lambda graph from the prior gate is another
pivot choice; its two reductions must not be counted again after blindly
changing pivot sets. The baseline exporter remains unchanged while this desk
theorem is reviewed.

Next cheapest discriminator AFTER different-model review: prepare a circuit
representation of these affine-in-coefficient graph substitutions, then measure
one capped AWS construction and compare terms/memory against the explicit
lambda/full-row baseline. Stop or reorder if fill worsens. No such construction
or commitment is authorized by this report. Full Jacobian rows and c guard
remain the hard existence/exclusion problem, and no point, properness, unit,
source coverage for arbitrary counterexamples, or JC2 resolution follows.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10150`.
- Body SHA-256:
  `7db2c8564fd8e07ba2afcaaf65425532b6968a22937d0c9b9958fb29b1c07afe`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
