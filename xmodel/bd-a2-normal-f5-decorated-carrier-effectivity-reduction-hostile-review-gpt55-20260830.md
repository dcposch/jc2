# Hostile review: corrected normal-F5 carrier/effectivity reduction

Date: 2026-08-30  
Reviewer: GPT-5.5 xhigh  
Review basis: `c4d65fedd9f9a135ab32a3ead7beb045fd2f873f`  
Overall verdict: **CONFIRM_WITH_CORRECTIONS**

## 0. Custody, scope, and verdict ledger

The producer and mandatory corrigendum were reviewed as one packet.  Their
full-file, body, and manifest hashes all reproduce exactly:

```text
producer full  f942e743dc206d958f31892e838d7517fe23eacbc863b56c9441b60152bc0cb4
producer body  28064 / e4823537bbaa3bb6142790456c11814d9be32c8b3f4c93f2563a2a13eb2a641d
producer manifest baf2b42a73fa5615b70e9544caaa4fdfa1f7fce4b79a4917ee17d0064e496324

corrigendum full 94f5bc5ce509809b951f5189bb6d3f863c09133dfda77522965d791a7419ee2e
corrigendum body 7659 / 488da252288cd9cc14ea797529d49b2d9db3c0a74bcab4308965ac07205182b6
corrigendum manifest 315a12543266d43784b005956e4cce08f1d9e280e443b0be549e2f493a2ff226
```

The four supplied binding inputs also reproduce their stated full hashes, and
all six reviewed blobs at the stated commit are byte-identical to the files
read.  The checkout itself was later than the review basis, so no theorem from
that later checkout is used except the four inputs expressly bound by the
prompt.  The directly charged normal-surface, F5 bridge, D9 fibre, fixed-sheet,
rational-forest, ramification-attachment, and smooth-local-different sources
were checked where load-bearing.

For citations below, `P` is
`xmodel/bd-a2-normal-f5-decorated-carrier-effectivity-reduction-sol56-20260830.md`,
`C` is its contracted-carrier corrigendum, `FB` is the supplied singular-F5
bridge integration, `D9` is the supplied global fibre integration, `EU` is
the supplied A1-ruling/Euler integration, and `LD` is the supplied smooth-F5
local-different integration.

| item | verdict | disposition |
|---:|---|---|
| 1 | **CONFIRMED** | F5 degrees, adjunction, fibre saturation, crepant delta, and `S.T` are exact. |
| 2 | **CONFIRMED** | The `S`-adapted contraction ends at `F_2`, uses nine blowdowns, and is valid with infinitely-near centres. |
| 3 | **CONFIRM_WITH_CORRECTIONS** | The ruled classes are exact; one physical-point sentence must be corrected and proximity/effectivity must remain separate. |
| 4 | **CONFIRMED** | The exact nine local necessary marked tags and the two advertised deaths are correct. |
| 5 | **CONFIRMED** | The reduced-`H` energy is unconditionally `q-4`, and no other ADE point lies on `H`. |
| 6 | **CONFIRM_WITH_CORRECTIONS** | The corrigendum restores raw clique number two in every marked state; effective attainment is not proved. |
| 7 | **CONFIRMED** | The ramification class/degree system and smooth `3+5` decomposition are correct, with `nu_k` uncontrolled. |
| 8 | **CONFIRM_WITH_CORRECTIONS** | The fibre residual identity is correct, but the raw target-image cap fails over `pi(Z_k)` and must be residualized. |
| 9 | **CONFIRM_WITH_CORRECTIONS** | Discrete finiteness survives, by a repaired proof; the binding Euler interface kills `B9/A8`. |
| 10 | **CONFIRMED** | Only a finite necessary-state theorem is promotable; there is no effectivity, occurrence, map, or JC2 theorem. |

There is no `GAP` after the repairs in Sections 3, 6, 8, and 9 below.  The
target-cap repair is mathematical, not cosmetic, but it is local and does not
invalidate the carrier table, the corrected maximum-two upper bound, the
class system, or the Euler eliminations.

## 1. F5 degrees, adjunction, and the singular fibre

The bidegree labels give

```text
B.L=0,                 B.S=B.T=1.
```

The three positive `A`-degrees sum to `A.H=A^2=3`, hence

```text
A.L=A.S=A.T=1.
```

With `K=-A+B` and all three strict components smooth rational, adjunction
then gives

```text
L^2=-1,                S^2=T^2=-2.
```

This confirms `P:97-119` directly from the binding numerical surface data
`FB:36-46` and the nine-blowup reduction
`xmodel/bd-a2-normal-singular-quadratic-incidence-reduction-sol56-20260830.md:173-205`.

Now suppose `p_0` is singular.  The target-line saturation theorem says that
each of the three boundary branches meets a smooth point of the exceptional
divisor transversely with one unit; a contact at an exceptional node or a
tangency would consume more than one unit (`FB:160-178`).  If

```text
F_0=sum_v beta_v C_v
```

is the actual scheme fibre, the section equation

```text
1=F_0.S=sum_v beta_v(C_v.S)
```

has nonnegative integral summands.  The known exceptional contact already
contributes at least one.  It therefore occurs on a `beta=1` component and
exhausts the equation.  In particular `L.S=0`; the identical argument for
`T` gives `L.T=0`.  This is not inferred merely from distinct normalization
points, and there is no hidden tangency or exceptional-node assumption.

For `r^*H=H'+hE`, `a=Ch`, and `q=h^t a`, crepancy gives

```text
delta_p0(H)=q/2+sum_(x over p0) delta_x(H').
```

The F5 germ has delta four.  Each strict branch is smooth, and the fibre
argument has removed the `L/S` and `L/T` intersections.  Thus the residual
delta is exactly the intersection length `S.T`:

```text
q=6:  S.T=4-3=1;       q=8:  S.T=4-4=0.
```

The first case is one transverse physical intersection of the two strict
sections.  It is not two vertices, two branch flags, or the coefficient two
of an attachment vector.  This confirms `P:121-163` against `FB:180-209`.

## 2. The `S`-adapted contraction and the nine-blowup marking

The binding fibre diagrams are the `B_s` chain and the `U_s` weighted fork,
including `U_2=A1+A1` and `U_3=A3` (`D9:108-149`).  A section has total
fibre intersection one, so it meets exactly one weight-one component.

In a `B_s` fibre, contract an endpoint `(-1)` not met by `S` and peel the
chain, switching sides if necessary so that the component met by `S` is
retained.  In a `U_s` fibre, first contract the weight-two nonexceptional
`(-1)` component, then peel the long arm and the unused spin.  In `U_2`,
contracting the middle weight-two curve makes the two leaves `(-1)` curves;
the leaf not met by `S` is then contracted.  At each stage the contracted
curve is disjoint from the current transform of `S`.  Repeating fibre by
fibre leaves a relatively minimal ruled surface and preserves `S^2=-2`.

If the endpoint is `F_e`, an irreducible section is `S_e+kF`.  The equation
`(S_e+kF)^2=-2` gives `e=2k+2`.  If `k>0`, then
`(S_e+kF).S_e=k-e<0`, forcing `S_e` as a component.  Hence irreducibility
forces `k=0,e=2`; the endpoint is exactly `F_2` and `S=S_0`.

The minimal resolution has `K^2=-1`, while every Hirzebruch surface has
`K^2=8`.  Thus exactly nine `(-1)` contractions occur.  Reversing them gives
nine, possibly infinitely-near, blowups away from `S_0`.  In the orthogonal
total-transform basis,

```text
S=S_0,       B=F,
K=-2S_0-4F+sum_i E_i=-A+F,
A=2S_0+5F-sum_(i=1)^9 E_i.
```

This supplies the explicit nine-step justification compressed at `P:193-207`;
the general total-transform proof is at
`xmodel/bd-a2-normal-singular-quadratic-incidence-reduction-sol56-20260830.md:210-258`.

In the singular row, `L` is a `(-1)` curve disjoint from `S`, so it may be
contracted first.  In the inverse sequence it is created last and has no
descendant, hence its actual class is `L=E_l`.  In the smooth row, `S` meets
`L`; the other `(-1)` member of the `B_1` fibre is contracted and
`L=F-E_l`.  A larger root block on this fibre would put an ADE point on `H`
or a positive-dimensional `pi`-fibre through `H`, contradicting respectively
smoothness at `p_0`, Section 5 below, or finiteness near `H`.  Orthogonal
total-transform identities are unchanged by infinitely-near centres.  Thus
`P:209-228,253-264` is confirmed.

## 3. Ruled classes, retained root, proximity, and physical contacts

Because a strict section has multiplicity zero or one at every successive
centre,

```text
T=S_0+bF-sum_(i in I)E_i,       T^2=-2,
|I|=2b.                                                    (3.1)
```

The binary statement remains valid for successive infinitely-near centres;
it is not a claim that all centres were initially distinct.  In the smooth
row, intersection with `L=F-E_l` and the F5 intersections give

```text
b=4,       l notin I,       |I|=8.
```

In a singular row retain the weight-one exceptional component `C_S` met by
`S`.  Its coefficient `h_S` in the exceptional cycle is the coefficient of
the surviving fibre after pushdown to `F_2`.  Comparing

```text
A=L+S+T+Z_H
```

with `L=E_l` and (3.1) yields

```text
b=5-h_S,       l notin I,       |I|=2(5-h_S),
Z_H=h_S F-2E_l-sum_(i notin I, i!=l)E_i.                 (3.2)
```

Since the centres avoid `S_0`, `S.T=b-2=3-h_S`.  Section 1 therefore gives

```text
q=6: h_S=2, T=S_0+3F-sum_(I_6)E_i, |I_6|=6,
     Z_H=2F-2E_l-E_j-E_k;

q=8: h_S=3, T=S_0+2F-sum_(I_4)E_i, |I_4|=4,
     Z_H=3F-2E_l-E_j-E_k-E_u-E_v.                        (3.3)
```

The retained fibre component is a smooth `(-2)` curve and has binary centre
multiplicities.  Its pushdown is `F`, so its class is `F` minus exactly two
centre classes:

```text
C_S=F-E_i-E_j.
```

The two centres may be successive.  Consequently

```text
T.C_S=1-1_(i in I)-1_(j in I).
```

Nonnegativity excludes both indices in `I`; `T` meets `C_S` exactly when
neither lies in `I`, and misses it exactly when one lies in `I`.  These
calculations confirm `P:230-335`.

They do not prove effectivity.  Chronological proximity inequalities, the
marked fibre history, and physical contact partitions remain additional
necessary data.  In particular the class equation `T.C_S=1` does not by
itself say which analytic point is used.

There is one literal error at `P:364-366`.  The phrase “three prescribed
smooth attachment points” is false for `q=6`: there are three unit branch
attachments partitioned into only two physical points, one for `L` and one
shared by `S,T`.  The exact replacement is:

> the three unit branch attachments, partitioned into two physical smooth
> points for `q=6` and three physical smooth points for `q=8`.

This repair preserves every class and tag.

## 4. Marked local table and actual fibre diagrams

An independent exact rational-arithmetic replay enumerated every nonnegative
vector `a` with `sum a_i=3`, positive integral `C^{-1}a`, and
`a^t C^{-1}a<=8` in the allowed `A/D` ranks.  Up to diagram reversal it
reproduced precisely

```text
A_r: 2e_1+e_(r-1), q=6;       e_1+e_2+e_(r-2), q=8;
D_4: e_1+e_3+e_4, q=6;
D_5: e_1+2e_4, q=8;           D_6: e_1+e_5+e_6, q=8.
```

The global `D9` embedding restricts the `A` rows to the ranks in `FB:188-204`.
Putting the actual nonexceptional fibre component `L` back into the diagrams,
rather than quotienting by an abstract Dynkin automorphism, gives:

* In a `B_(r+1)` fibre, `L` meets an endpoint of `A_r`.  In the `q=6`
  row the singleton unit is internal for every `r>=3`; hence `B_4/A_3`
  and all higher balanced `q=6` rows die.  For `r=2`, the row is `3e_1`,
  and `B_3/A_2` survives as a necessary tag.
* In `U_3=A_3`, `L` meets the central vertex and the two sections share a
  point on a spin.  Thus `U_3/A_3` survives although `B_4/A_3` does not.
* In `U_4/D_4`, `L` meets vertex `1` and the section units lie on the two
  distinct weight-one spins.  That gives `S.T=0`, contradicting the required
  `q=6` intersection one; `U_4/D_4` dies.
* For `q=8`, the balanced rows are exactly `B_5/A_4` through `B_9/A_8`.
  In `A_4`, coefficient two means two distinct physical points on vertex
  `2`, not a tangent branch or one doubled germ.
* The unbalanced survivors are exactly `U_5/D_5` and `U_6/D_6`.  The
  coefficient two in `D_5` again represents two distinct section contacts
  on one spin.  `D_4` triality is unavailable because the actual `U_4`
  fibre weights mark the long arm.

The exact local necessary list is therefore

```text
q=6: B3/A2, U3/A3;
q=8: B5/A4, B6/A5, B7/A6, B8/A7, B9/A8, U5/D5, U6/D6.
```

`U_2` is two physical `A1` points in one actual fibre, not one `A1+A1`
singularity; `A1` also fails the local Cartier filter.  Repeated contacts on
one exceptional component have been retained as distinct physical points.
No hidden nonexceptional `(-2)` vertex occurs at `p_0`: connectedness of the
fibre root block would join it to the F5 component, while `A.C=0` would make
its image a positive-dimensional `pi`-fibre through `H`, contrary to local
finiteness.  Thus `P:337-382` is correct after the physical-point wording
repair in Section 3.  None of these tags is an occurrence theorem.

## 5. Unconditional reduced-infinity energy

At any ADE point of reduced `H`, the local crepant identity is

```text
delta_p(H)=h^t a/2+sum delta(H').
```

The right side is positive because `a` is nonzero and `C^{-1}` is positive.
Every point of the F5 curve away from `p_0` is smooth, with delta zero.
Therefore no ADE point lies on `H` away from `p_0`, as asserted at
`P:384-395`.

Let

```text
D_H=Supp(r^*H),       W_H=r^*H-D_H=sum(h_i-1)E_i.
```

The reduced divisor `D_H` is connected.  Since `p_a(r^*H)=p_a(A)=2` and
`A,K` are orthogonal to the exceptional trees,

```text
p_a(D_H)=2-(1/2)sum_trees (h-1)^t C(h-1)>=0.
```

Hence the total energy is at most four.  At the unique connected F5 tree,
`sum a_i=3` and `1^t C 1=2`, so

```text
(h-1)^t C(h-1)=h^t a-2sum a_i+2=q-4.
```

Thus a `q=6` row uses two energy units and a `q=8` row all four.  This is a
global reduced-`H` budget, not a fresh per-point budget.  `P:396-423` is
confirmed without a ramification-multiplicity hypothesis.

## 6. Contracted carriers and the mandatory corrigendum

For a nonexceptional prime `Z` contracted by `pi` to an affine target point,
the incidence fibre is the unique source line over that point.  Thus
`A.Z=0`, `B.Z=1`, `Z` is rational, and adjunction gives `Z^2=-3`.  Finiteness
near `H` makes it disjoint from `S_0`.  Writing its total-transform class as
`S_0+bF-sum mu_iE_i`, one obtains

```text
b=2,       sum mu_i=5,       sum mu_i^2=5.
```

The integral multiplicities are therefore binary, giving exactly the
necessary class

```text
Z_J=S_0+2F-sum_(j in J)E_j,       |J|=5.                (6.1)
```

Infinitely-near centres introduce proximity constraints but do not alter
(6.1).  Disjointness from `L,T` gives the corrected raw candidate table:

| state | marked form | candidates |
|---|---|---:|
| smooth | `J={l} union K`, `K in binom(U_8,4)` | 70 |
| `q=6` | `J=O union K`, `|O|=2`, `K in binom(I_6,3)` | 20 |
| `q=8` | `J=K union N`, `K in binom(I_4,2)`, `N in binom(O_4,3)` | 24 |

For distinct classes

```text
Z_J.Z_K=2-|J cap K|.
```

Distinct contracted primes lie over distinct target points and are disjoint,
so coexistence requires `|J cap K|=2`.  This is necessary numerical
compatibility, not a converse effectivity test.

The producer's unrestricted sentence at `P:462-463` is false.  The
corrigendum's explicit three-subset counterexample has pairwise intersection
two, empty triple intersection, and union nine.  The corrected marked proofs
are sound:

* Smooth: every `J` contains `l`.  Three compatible sets would have triple
  intersection size `t>=1`, so inclusion-exclusion gives union size
  `15-6+t>=10`, impossible in a nine-set.  The pair count is
  `70*(4*4)/2=560`.
* `q=6`: every candidate contains the fixed two-set `O`; compatibility means
  the two three-subsets of `I_6` are disjoint, hence complementary.  There
  are `20/2=10` pairs, and three disjoint three-subsets cannot fit in six.
* `q=8`: two three-subsets of `O_4` have intersection two exactly when they
  are distinct.  Compatibility additionally makes the two two-subsets of
  `I_4` complementary.  The pair count is `3*(4*3)=36`, and three pairwise
  disjoint two-subsets cannot fit in four.

A standard-library replay over all five-subsets returned

```text
state       vertices   edges   compatible triangles   clique number
smooth         70       560             0                   2
q=6            20        10             0                   2
q=8            24        36             0                   2
```

Accordingly the safe statement is:

> each raw marked numerical compatibility graph has clique number exactly
> two; therefore every effective family has at most two contracted carriers.

It is not safe to say that two effective contracted carriers are attained.
The counts ignore chronological proximity and simultaneous effectivity.

A targeted search on the frozen basis found the false unrestricted principle
only in `P:462-463` and its explicit retraction in `C:19-46`.  Sections 7 and
8 of `P` sum over arbitrary `Z_k` and do not use it.  Section 9 item 3 is the
only downstream cardinality consumer and is restored by the marked proofs.
Even without the sharp result, `sum nu_k<=4` gives coarse finiteness
(`C:179-208`).  The supplied Euler theorem uses lower bounds on `k`, not this
upper bound.  Thus no downstream conclusion retains the false unrestricted
assertion.

## 7. Ramification class, divisorial coefficients, and smooth `3+5`

The ramification class in the `F_2` marking is

```text
r^*R_X=2A+B=4S_0+11F-2sum_iE_i.                         (7.1)
```

Separate noncontracted primes `C_j`, contracted primes `Z_k`, and the actual
exceptional cycle `M=sum m_alpha E_alpha`.  The binding fixed-sheet theorem
(`xmodel/block-descent-galois-coordinator-integration-sol56-20260830.md:47-64`)
says that a divisorial target branch has an unramified sheet.  In degree
three, the remaining ramified sheets must form one tame transposition.  Thus
every noncontracted ramification prime has `e=2`, residue degree one, and
different coefficient `e-1=1`.

This argument applies only at a target divisor.  It does not control a
`Z_k`, whose image has codimension two, or an exceptional curve.  Write its
unknown coefficient as `nu_k>=1`.  The exact divisor/class and degree system
is

```text
sum_j C_j+sum_k nu_k Z_k+M
   =4S_0+11F-2sum_iE_i,

sum_j A.C_j=8,
sum_j B.C_j+sum_k nu_k=4.                               (7.2)
```

At an ADE tree, `n=Cm>=0` with `m>0`.  The total-basis class of `M` must be
computed from the actual roots; it cannot be replaced by formal orthogonal
symbols.  For a horizontal rational carrier

```text
C=dS_0+bF-sum mu_iE_i,       d=B.C>=1,
a=A.C=d+2b-sum mu_i,
C^2=-2d^2+2db-sum mu_i^2,
delta(C)=1+(C^2-a+d)/2 in Z_{>=0}.                    (7.3)
```

These formulas confirm `P:473-527`.  One useful constraint should be made
explicit in a promoted state: distinct `C_j` have distinct target branch
divisors, and each `C_j` maps generically birationally to its image.  Otherwise
the cubic degree plus the fixed sheet would be exceeded.

If `p_0` is smooth, `LD:77-151` gives exactly two reduced local different
branches with boundary totals three and five.  They cannot be branches of one
global prime, because two normalization points attached to the connected F5
boundary produce a forest cycle (`LD:160-190`).  Since all eight boundary
contacts occur at `p_0`, their global `A`-degrees are exactly three and five,
and they exhaust (7.2):

```text
r^*R_X=C_3+C_5+sum_k nu_kZ_k+M.
```

For singular `p_0`, only a positive partition of eight among the `A.C_j` is
known.  No singular `3+5` analogue is licensed.  `P:529-551` keeps this
firewall correctly.

## 8. Proper residual caps, class groups, and support genus

### 8.1 Actual-fibre cap: confirmed

Let

```text
F_t=Gamma+sum_i beta_iE_i
```

be an actual scheme fibre, with `Gamma` already scheme-weighted.  Let `V_t`
be the actual Cartier-weighted sum of every nonexceptional fibre component
common with the strict ramification, put `v_i=V_t.E_i`, and set
`R_o=R_str-V_t`.  In the present noncontracted fibre case fixed-sheet gives
coefficient one, but the Cartier-weighted definition is the safe one.  Since
`F_t.V_t=F_t.M=0`, removal of all common carriers gives

```text
4=Gamma.R_o+beta^t(n-v),       beta^t(n-v)<=4.           (8.1)
```

Every `beta` remains present, including the weight-two part of a `U_s`
fibre.  The subtraction is `n-v`, not raw `n`, and not an unweighted
per-singularity budget.  This confirms `P:553-574`.

At the F5 fibre, subtracting the unique common component `L` gives

```text
2=Gamma.(S+T)+beta^t(a-ell).                            (8.2)
```

For singular `p_0`, the first term is zero and the two section contacts have
weight one.  For smooth `p_0`, there is no exceptional term and the two
intersections with `L` give the whole value.  `P:576-587` is exact.

### 8.2 Target-image cap: correction required

The raw equation at `P:589-609` is an algebraic total-transform identity, but
its claimed nonnegative proper term and resulting bound on raw `n` are false
when `q=pi(Z_k)`.  Every target line through that point pulls back with
`Z_k` as a component.  Generic choice cannot remove a curve contracted to
the chosen point.

The exact repair is parallel to (8.1).  Define

```text
V_q=sum_(pi(Z_k)=q) nu_k Z_k,
v_i^(p)=V_q.E_i,
R_(o,q)=R_str-V_q.
```

Choose a generic target line through `q` avoiding the divisorial images of
all `C_j` and the finitely many other contracted target points.  If `G_q` is
the nonexceptional part of its resolved pullback and `ell^(p)` its positive
exceptional valuation vector, then `A.V_q=0`, total pullbacks are orthogonal
to exceptional curves, and all remaining strict intersections are proper.
Therefore

```text
8=G_q.R_(o,q)
  +sum_(p over q) (ell^(p))^t(n^(p)-v^(p)),              (8.3)

sum_(p over q) sum_i(n_i^(p)-v_i^(p))<=8.               (8.4)
```

The producer's raw bound on `sum n_i` is recovered only in the subcell
`V_q=0`.  This is required by the common-carrier firewall in `D9:201-214`.
The corrigendum did not create this issue, but its broad statement at
`C:42-46` that no cap changes cannot be used to promote the uncorrected target
cap.

### 8.3 Units, class group, and support genus: confirmed

For `Y=X-H` and `U=Y-Supp(R_X)`, dominance of the affine first leg gives
`O(U)^*=C^*`; restriction then gives `O(Y)^*=C^*`.  The divisor localization
sequence injects the free group on all reduced nonexceptional ramification
primes into `Cl(Y)`.  A relation

```text
sum q_jC_j+sum q_kZ_k ~ cA+(exceptional)
```

pushes down and restricts to a relation among those primes, while `A~H`
becomes trivial on `Y`; hence all coefficients must vanish.  The `nu_k` do
not enter this reduced-prime independence test.  This confirms `P:611-628`
against
`xmodel/bd-a2-quadratic-ramification-attachment-coordinator-integration-sol56-20260830.md:149-160`.

Let `D_R=Supp(r^*R_X)` and

```text
W_R=r^*R_X-D_R
   =sum_k(nu_k-1)Z_k+sum_alpha(m_alpha-1)E_alpha.
```

The support is connected and `p_a(r^*R_X)=9`.  Since
`r^*R_X.Z_k=K.Z_k=1` and both classes are orthogonal to exceptional curves,
adjunction gives exactly

```text
p_a(D_R)=9+(W_R^2-3sum_k(nu_k-1))/2>=0.                 (8.5)
```

Only if every `nu_k=1` is `W_R` purely exceptional, in which case (8.5)
becomes

```text
sum_trees (m-1)^tC(m-1)<=18.
```

Thus `P:630-661` is correct: the ramification-energy cap eighteen is
conditional and fixed-sheet inertia does not make it unconditional.

## 9. Finiteness and the binding Euler interface

The discrete necessary state is finite, but `P:689-692` gives one wrong
reason: raw target bound (8.5) does not bound every `n` over a contracted
carrier image.  Replace that sentence by the following argument.

There are nine blowup coordinates and finitely many combinatorial proximity
graphs and marked `D9` root subsystems.  Equation (7.2) bounds every
`d=B.C_j`, the number of horizontal carriers, and every `nu_k` by four.
Pushing the effective decomposition to `F_2` bounds each nonnegative fibre
coefficient `b` by eleven.  With `1<=a=A.C<=8`, equation (7.3) bounds
`sum mu_i=d+2b-a`, hence all centre multiplicities.  Vertical strict carriers
come from the finite marked fibre diagrams.  Once these strict classes and
root classes are selected, `n_i=R_str.E_i` is determined and
`m=C^{-1}n` is unique; alternatively, (8.4) bounds `n-v`, while the finite
carrier classes and `nu_k<=4` bound `v`.  Integrality, positivity, proximity,
and physical-cluster rules are filters on this finite list.

“Finite” here means discrete numerical classes, equality partitions of target
labels, proximity graphs, and physical contact partitions.  It does not mean
finitely many target coordinates, blowup locations, analytic germs, or
moduli.

Now charge the supplied binding Euler theorem, not the producer's formerly
out-of-basis proposal.  Put `rho=r_0+r_aff`, where `r_0` is the local rank at
`p_0`, and let `k` count distinct reduced nonexceptional ramification primes,
including every `Z_k` once regardless of `nu_k`.  From `EU:188-235`,

```text
rho+k<=8,
P1 base for the new A1-ruling  =>  rho+k<=7.             (9.1)
```

The exact residual table is:

| marked state | `r_0` | general `r_aff+k` | new-ruling `P1` base |
|---|---:|---:|---:|
| smooth `B_1` | 0 | `<=8`, with `k>=2` | `<=7` |
| `B_3/A_2` | 2 | `<=6` | `<=5` |
| `U_3/A_3` | 3 | `<=5` | `<=4` |
| `B_5/A_4` | 4 | `<=4` | `<=3` |
| `B_6/A_5`, `U_5/D_5` | 5 | `<=3` | `<=2` |
| `B_7/A_6`, `U_6/D_6` | 6 | `<=2` | `<=1` |
| `B_8/A_7` | 7 | exactly `1` | impossible |
| `B_9/A_8` | 8 | impossible | impossible |

The last row dies because every singular F5 state has at least one
nonexceptional strict ramification prime, so `k>=1`.  In the `B_8/A_7` row,
`(r_aff,k)=(0,1)` is forced.  Its one prime is noncontracted, since strict
ramification must attach at `p_0`; it has `A`-degree eight.  Equality
`rho+k=8` forces base `A1` for the new ruling and every one of its fibres to
have irreducible reduced support, though a multiple irreducible fibre is not
excluded.

For any other row with residual ceiling `R=8-r_0`, the formal equality cells
are

```text
(r_aff,k)=(R-k,k),       1<=k<=min(4,R),
```

with `k>=2` in the smooth row; they remain necessary numerical cells, not
attained configurations.  Equality forces the same reduced-fibre conclusion
and the `A1` base.  In the `P1`-base branch replace `R` by `7-r_0`.
Equality there also makes every reduced fibre irreducible because all Euler
correction terms vanish.  In particular `A7` dies in that branch, while the
`A6/D6` rows force `(r_aff,k)=(0,1)`.

These fibre conclusions concern the new `A1`-ruling on an adapted completion
of `U`.  They do not concern the original conic fibration with fibre class
`B`, do not make a `B_s/U_s` fibre irreducible, and do not license a second
ruling class in the raw `D9` marking (`EU:97-120,264-273`).

## 10. Exact repairs, maximum theorem, and successor

### 10.1 Required promotion repairs

1. Treat `P:462-463` as retracted.  Splice in the three marked proofs of
   `C:78-177`; state raw clique number two and effective cardinality **at
   most** two, never effective attainment.
2. At `P:364-366`, replace “three prescribed smooth attachment points” by
   the branch-attachment/physical-point sentence in Section 3 above.
3. Replace `P:589-609` by the residual target identity (8.3)-(8.4).  A generic
   line cannot exclude a `Z_k` over the point through which it is chosen.
4. Replace the raw-`n` finiteness sentence at `P:689-692` by the finite-class
   argument in Section 9.
5. In the target-label state, impose that distinct noncontracted `C_j` have
   distinct divisorial target images and are generically birational to them.
6. Keep every chronological proximity history and physical contact partition.
   A subset signature, root embedding, or zero intersection is not an
   effectivity or coexistence theorem.

### 10.2 Promotion-ready maximum theorem

In the charged normal irreducible class-`2A+3B`, reduced-infinity,
finite-near-`H`, dominant-first-leg scope, the boundary is F5.  After choosing
one section `S`, the minimal resolution admits an `S`-adapted nine-blowup
marking over `F_2` with

```text
S=S_0,       B=F,       A=2S_0+5F-sum E_i.
```

The smooth state has `L=F-E_l` and the exact smooth `3+5` different.  Before
the Euler filter the singular local possibilities are exactly the nine
necessary marked tags in Section 4, with `L=E_l`, the classes (3.2)-(3.3),
and the physical/proximity data retained.  After the binding Euler filter,
`B_9/A_8` is eliminated, leaving eight singular tags plus the smooth state,
subject to the residual table in Section 9.

Every affine coefficient-basepoint carrier has one of the raw classes (6.1).
The three marked compatibility graphs have `(vertices,edges)` equal to
`(70,560)`, `(20,10)`, and `(24,36)`, each with clique number two; hence an
effective configuration contains at most two such carriers.  No pair is
asserted effective.

Ramification obeys the exact class/degree system (7.2), coefficient one on
noncontracted divisorial primes, and uncontrolled positive coefficients
`nu_k` on Stein-contracted primes.  The actual-fibre cap is (8.1), the correct
target-image cap is the residual formula (8.3)-(8.4), reduced prime classes
are independent on `Y`, support genus is (8.5), and ramification energy at
most eighteen is available only when every `nu_k=1`.  These data define a
finite **necessary numerical/combinatorial threat state**.

This theorem does not assert that any marked tag, subset, proximity history,
attachment partition, or equality cell is effective.  It gives no moduli or
analytic-incidence classification, finite algebra, first-leg realization,
polynomial map, counterexample, or JC2 conclusion.  It must not identify a
branch flag with a physical place or a divisor series, and it makes no
floor-to-attainment inference.

### 10.3 Cheapest exact successor

The cheapest exact successor is local and valuative, not a heavy global
enumeration:

1. For each surviving singular-`p_0` marked tag, factor the completed local
   Cartier different on the ADE germ.  Output its strict primes and
   coefficients, exceptional attachment vector, physical contact partition,
   and global `A`-degree partition of eight.  The smooth Hensel `3+5` result
   must not be transferred by analogy.
2. At the generic DVR of each candidate `Z_J`, compute
   `nu_J=ord_(Z_J) Fitt^0 Omega_(X/P2)` from the two pulled-back target
   parameters and their leading tangential terms.  This is a codimension-two
   contraction calculation, not divisorial inertia.
3. Only then run the finite proximity/effectivity and connector filters using
   the residual target cap.  Analytic realization remains a later gate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `30296`.
- Body SHA-256:
  `93fd7e936fc2f14add9d893130d37e64dc20e3fc7eb66cb741221d0da75fe63a`.
- Frozen basis: `c4d65fedd9f9a135ab32a3ead7beb045fd2f873f`.
