# Nested U2--P0--U2: repaired semilinear ray and exact family-record boundary

Date: 2026-08-29  
Role: post-review theorem-interface/family-record follow-up  
Verdict: **one repaired ray is an exact one-parameter semilinear formal family; the reviewed `nu=2K` ray is uniformly N1/L6-DEAD**  
Scope: characteristic-zero reduced patterns, local edge arithmetic, P0/U2
ODE verdicts, and normalized full-degree products only; no source landing,
coefficient gluing, polynomial-pair realization, full-book coverage, panel,
degree bound, `G2`, or JC2 conclusion

## 0. Result

The reviewed obstruction contains a repairable but load-bearing omission.
At its P0 vertex it takes

```text
nu_1=2K,                 kbar_1=4K+2.
```

Thus `gcd(kbar_1,nu_1)=2` for every `K`.  A standard `nu>=2` P0 vertex is
a `V_{1,a}` characteristic vertex, so the promoted, case-agnostic N1/L6
law requires `gcd(kbar,nu)=1`.  The old `K==1 (mod 6)` ray is therefore an
infinite family of solutions to the *truncated* arithmetic/ODE list, but it
is uniformly **DEAD** in the current source-licensed local grammar.  The
producer and hostile review checked integrality of `kbar` but not this
primitivity condition.

The obstruction itself survives after the smallest useful rescaling.  Put

```text
K=6q+1, q>=0,             nu_1=5K.
```

Keep all other inner-U2, P0, and outer-U2 labels fixed as in the reviewed
family.  Then N1/L6 holds, every advertised local equation and ODE test
holds, and all integer/rational-pair coordinates are affine in `q`.  This is
one exact linear set, representable by one labelled family record rather
than infinitely many literal cells.

More generally `nu_1=tK` works at this tier for every fixed
`t==5 (mod 6)`.  The simultaneous two-parameter union is **not** being
claimed semilinear: its graph contains the product `nu_1=tK` of two
independent unbounded variables.  The single fixed choice `t=5` is the
smallest semilinear witness needed to preserve the outer-finiteness
obstruction.

Full `i`-synchronization does not kill the repaired family.  It forces the
successive multiplicative index ratios and they hold identically.  What
remains open is whether actual source branches supply the same incoming
index scale and compatible coefficients, not whether adjacent vertex
indices are numerically equal.

## 1. Custody and exact inputs

Full-file SHA-256 values recomputed in this session:

- reviewed producer,
  `xmodel/m2-u2-one-p0-nested-boundary-r1-sol56-20260829.md`:
  `350ec5ceb152524588cbb33e72b09c82d5e0250593583f3b60eda42eba32dc04`
  (sealed body
  `16dcbfcf26259f76cefa42eaced12fff4a334514f113d672f173818ce6a3c31b`);
- Grok hostile review,
  `xmodel/m2-u2-one-p0-nested-boundary-r1-hostile-review-grok46-20260829.md`:
  `2391b96cb131bf6b647c519e37c1423573d95d76917081d7dc31d5b45a5635ed`
  (sealed body
  `b90ece915d174c80ed69e310cca6dfd7552f46f13330ebda3e0de8eec1d5217a`);
- direct-edge/full-degree source audit,
  `xmodel/m2-u2-direct-edge-isync-source-audit-sol56-20260829.md`:
  `59fd30425df7bf4e9138c56b2d4ba4247d0c35f2ddeb409bc09b5cb6c7c45a0f`
  (sealed body
  `6c24091eecb78fe82b664794421fb8e1685c60394d807ed21d2866d16b38f0f2`);
- `ladder/BOOK-OFFAXIS.md`:
  `7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77`;
- `ladder/SHEET6-DEPTH.md`:
  `ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d`;
- `ladder/SHEET6-III.md`:
  `59a2fa489f7f999b24aabc4c707254b7e54f8db02d69690226754e3224f9bdda`;
- `ladder/TEMPLATE-ATTACK.md`:
  `15457f185748249d57558f52f88727ae00efd16a4d485a51160e045a5e490229`;
- `ladder/REDUCTION.md`:
  `b0b6c276b1fe28a9b94556e29a058264201267dfc496b3100c416f027bc7aa0f`;
- `APPROACHES.md`:
  `27a208c58af3eb192bff51b2dc8f58cb9f6efcbd22816f88de6c9d428595a05b`;
- `AUDIT.md`:
  `7cb5d4a8a3a4162a8a204facb79e68a9ef4f353275912d440170ae9898cd41f8`;
- U1 record producer/review,
  `xmodel/m2-equal-join-semilinear-primary-research-opus5-20260829.md` and
  `xmodel/m2-equal-join-semilinear-primary-research-hostile-review-grok46-20260829.md`:
  `7ed65bc22f836230dada03776a1b3c6f9110c955a35b52fa28c21d0811a6c99d`
  and
  `8755bd5d3d1cd2721d32e5956c5b139b2cc6e0e805662d5278ededff896135ba`;
- printed source `refs/sigray_full.pdf`:
  `9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae`.

Load-bearing locations are producer §§3--6; hostile review §§2--8;
`SHEET6-III.md` §3 N1 (lines 123--133); `TEMPLATE-ATTACK.md` §1a
(lines 58--70); `BOOK-OFFAXIS.md` R1.2, R2.1, P0, and the §10 trust
perimeter; direct-edge audit §§3--7; `REDUCTION.md` Critical 4 and
§§5.1--5.2; and the reviewed `EQJOIN-FAMILY/v1` normalization/hash rules.

## 2. Exact local grammar and hypotheses

Work over a characteristic-zero field.  This is a labelled three-vertex
formal route

```text
U0 = inner U2 (nu_0=1)
  -- case II, arrival multiplicity l=3 -->
P1 = one clean neutral P0 (nu_1>=2)
  -- case I, arrival multiplicity h=3 -->
U2 = outer U2 (nu_2=1), with two symmetric P1 arrivals.
```

The fixed inner data are

```text
a=1, r=2, mu=3, L_inner=1,
(dp_0,dq_0,kbar_0,rho_0,w_0,M_0)=(6,4,3,1,2,3).
```

The P0 labels are

```text
l=3, eps=k=lex=Sm=0, s=1, E=3,
p_1=(eta^nu-c^nu)^3, q_1=eta(eta^nu-c^nu), c!=0.
```

The outer U2 labels are

```text
R=2, h=3, L_outer=K,
two equal-weight arrivals w_1=2.
```

The local legality predicate retained here is the one actually used by the
source and reviewed packets: positive edge indices; strict root-multiplicity
and searrow inequalities; St 8.4 divisibility; MP2; `gcd(nu_1,h)=1`;
N1/L6 at the `nu_1>=2` characteristic vertex; the clean P0 ODE; and the two
U2 T1 verdicts.  It does not assert that the labelled route lands from a
source entry or that its coefficient data glue.

## 3. The missed N1 branch and the repaired general scaling

For a neutral P0 step at incoming weight two, with arbitrary `nu>=2`, the
reviewed formulas reduce to

```text
dp_1=3nu, dq_1=nu+1, kbar_1=2nu+2,
rho_1=2, w_1=2, M_1=gcd(3,nu+1),
j=kbar_1-kbar_0=2nu-1.
```

At the outer U2 vertex,

```text
dp_2=6, dq_2=K+2, M_2=gcd(6,K+2),
kbar_2=2(K+2)/K,
n=nu*kbar_2-kbar_1=4nu/K-2.
```

Hence the clean co-scaling branch has `nu=tK`, giving `n=4t-2`.  For
`K==1 (mod 6)`, its remaining arithmetic is exact:

```text
N1/L6: gcd(kbar_1,nu)=gcd(2,nu)=1  iff t is odd;
M_1=3 and h|M_1                         iff t==2 (mod 3);
gcd(nu,h)=1                             iff t!=0 (mod 3);
M_2=3, and outer U2 T1 is alive because K is odd.
```

Thus precisely `t==5 (mod 6)` survives these local filters.  The reviewed
choice `t=2` fails N1 uniformly.  The least positive repaired choice is
`t=5`.

For `t=5`, write `K=6q+1`.  The full repaired data are

```text
nu_1   =5K       =30q+5,
dp_1   =15K      =90q+15,
dq_1   =5K+1     =30q+6,
kbar_1 =10K+2    =60q+12,
rho_1=2, w_1=2, M_1=3, lambda_1=0,
j       =10K-1   =60q+9;

dp_2=6,
dq_2   =K+2      =6q+3,
M_2=3, lambda_2=0,
kbar_2 =(2K+4)/K =(12q+6)/(6q+1),
n=18.
```

Every rational pair displayed for `U2` is in lowest terms because
`K==1 (mod 6)`.  The remaining useful outer frame values are

```text
rho_2=2/K,       X_2=12/K,
w_2=2(K+1)/K.
```

The P0 ODE is the same exact identity as in the reviewed report:

```text
delta=3nu/(nu+1), Z=eta^nu-c^nu,
delta*p*q' - p'*q = -delta*c^nu*p != 0.
```

The inner U2 has quadratic radical degree two and `L_inner=1`; the outer
U2 has the same radical degree and odd `K`.  The reviewed quadratic theorem
therefore gives T1-alive at both ends for every `q>=0`.  No recurrence is
being extrapolated from a finite scan.

For completeness, at fixed `t=5` the local residue classifier on arbitrary
positive `K` has only one live class:

| `K mod 6` | decisive result at this fixed skeleton |
|---:|---|
| 0 | DEAD: P0 `M_1=1`; N1 and outer T1 also fail |
| 1 | ALIVE at the declared local/formal tier |
| 2 | DEAD: P0 `M_1=1`; N1 and outer T1 also fail |
| 3 | DEAD: `M_1=M_2=1` and `gcd(nu,3)!=1` |
| 4 | DEAD: N1 and outer T1 fail |
| 5 | DEAD: `M_1=M_2=1` |

This table is a finite periodic consumer, not a numerical search.

## 4. Smallest safe normalized family record

The following is the smallest safe record shape at this scope.  “Smallest”
means that derived quantities may be recomputed from the displayed laws,
but the labelled route, N1 certificate, rational numerator/denominator
pairs, consumers, and provenance may not be dropped without changing a
known verdict or colliding with a different family.

```text
schema            = "NESTED-U2-P0-U2-RAY/v1"
kind              = "ONE_CLEAN_NEUTRAL_P0"
scope             = "FORMAL_LOCAL_ARITHMETIC_T1_FULL_DEGREE_RATIOS"
realization       = "NOT_ASSERTED"

parameter         = {name:"q", domain:"N0"}
K_law             = {slope:6, intercept:1}
K_period          = 6
K_residues        = [1]
neutral_scale_t   = 5

inner_u2          = {nu:1,r:2,mu:3,L:1,dp:6,dq:4,
                     kbar:"3/1",rho:"1/1",w:"2/1",M:3,lambda:0}
p0_labels         = {l:3,eps:0,k:0,lex:0,Sm:0,s:1,E:3,
                     case_in:"II",coefficient_character:"CLEAN_NEUTRAL"}
p0_affine         = {nu:[30,5],dp:[90,15],dq:[30,6],
                     kbar:[60,12],rho:"2/1",w:"2/1",M:3,
                     lambda:0,edge_index_j:[60,9]}
outer_u2_labels   = {nu:1,R:2,h:3,case_in:"I",dp:6,M:3,lambda:0}
outer_u2_affine   = {dq:[6,3],
                     kbar_num:[12,6],kbar_den:[6,1],
                     rho_num:[0,2],rho_den:[6,1],
                     X_num:[0,12],X_den:[6,1],
                     w_num:[12,4],w_den:[6,1],
                     edge_index_n:[0,18]}

legality          = ["positive_edges","strict_R_NE","St8.4",
                     "MP2","arrival_coprime","N1_L6",
                     "P0_ODE_ALIVE","U2_INNER_T1_ALIVE",
                     "U2_OUTER_QUADRATIC_ODD_T1_ALIVE"]
coefficient_character = {
  inner_u2:"Rad(T)=T^2-A, L=1, A!=0",
  p0:"Z=eta^nu-c^nu; p=Z^3; q=eta*Z; c!=0",
  outer_u2:"quadratic Rad; unique monic S_K; K odd"
}

full_index_primitive = {i0:[0,1], i1:[0,2], i2:[60,10]}
full_degree_affine = {
  degp0:[0,6], D0:[0,6],
  degp1:[180,30], D1:[360,60],
  degp2:[360,60], D2:[0,120]
}

consumers         = ["outer_case_I","full_i_sync","sibling_sync",
                     "Statement3.9_gluing","source_landing",
                     "downstream_trunk_or_terminal"]
coverage_status   = "ONE_EXPLICIT_LOCAL_FAMILY_ONLY"
coverage_debt     = ["all_other_t","generic_nested_U2_grammar",
                     "actual_source_indices","unused_siblings",
                     "coefficient_gluing","landing","realization",
                     "downstream_coverage"]
negative_control = "same record with t=2 is DEAD by gcd(kbar1,nu1)=2"
provenance        = [labelled path plus exact producer/review/source hashes]
```

An affine pair `[slope,intercept]` denotes `slope*q+intercept`.  Fractions
are stored as separate reduced integer numerator/denominator laws; no float
or division operation belongs to the family key.  Canonical equality and
hashing should follow `EQJOIN-FAMILY/v1`: sorted-key canonical JSON,
lowest-term fraction pairs, minimal period, sorted residues, labelled
members, and SHA-256 of the canonical blob.  A member must retain this
family key; it must not be keyed only by `(dp,dq,nu,M,kbar)`.

The integer generator underlying the nonconstant load-bearing fields is
explicitly

```text
(K,nu1,dp1,dq1,kbar1,j,dq2,kbar2_num,kbar2_den,n,
 i2,degp1,D1,degp2,D2)
=
(1,5,15,6,12,9,3,6,1,18,10,30,60,60,120)
+ q*(6,30,90,30,60,60,6,12,6,0,60,180,360,360,0).
```

It is therefore one linear set in the integer encoding.

## 5. Presburger/semilinear boundary

### 5.1 What is Presburger here

For fixed `t=5`, membership, every integer coordinate above, every reduced
rational numerator/denominator pair, positivity, the edge indices, the
primitive index ratios, MP2/St 8.4, N1, arrival coprimality, and the T1
verdict are affine or periodic in `q`.  Their joint graph is Presburger
definable and semilinear.  The exact local validity set is the single
progression `K==1 (mod 6)`.

The P0 polynomial support is also affine (`{0,nu,2nu,3nu}` and shifted
copies), and the P0 ODE is certified by one uniform symbolic identity.  The
outer quadratic U2 recurrence need not be stored coefficient-by-coefficient:
its reviewed verdict compiles exactly to `K` odd, a Presburger predicate.

### 5.2 What is not being called Presburger

Coefficient values such as `c^nu`, the field-valued outer recurrence
coefficients, root choices, and cross-vertex gluing are not Presburger data.
The record stores their exact theorem/character tag and routes realization
consumers to `UNCOVERED`; it does not serialize those coefficients as an
integer semilinear set.

The unrestricted outer coupling

```text
K(n*dq_1+z)=z*nu*s*R
```

contains products of independently varying integer fields and is not a
Presburger transition in the generic nested-U2 grammar.  It becomes affine
on this ray because `t=5`, `nu=5K`, and `n=18` are part of the proved
parametrization.

Likewise, allowing both `K=6q+1` and `t=6u+5` to vary produces
`nu=tK`.  That two-parameter graph is not semilinear.  It is an infinite
collection of fixed-`t` semilinear rays, not one finite semilinear endpoint.
This is coverage debt, and this report does not claim that the entire
nested-U2 leak has been compiled into finitely many records.

Absolute full indices add the same boundary.  If an incoming scale `tau` is
fixed by source context, then

```text
(i0,i1,i2)=tau*(1,2,10K)
```

is affine in `q`.  If `tau` and `q` are independent unbounded variables,
the graph `i2=10K*tau` is not Presburger.  The normalized record therefore
stores the primitive ratio and treats the actual source scale as a typed
consumer, rather than falsely claiming a uniform absolute-index quotient.

## 6. Full `i`-synchronization: compatibility, not a kill

Let `i0,i1,i2` be the full-pattern indices at the inner U2, P0, and outer
U2 vertices.  Statement 3.17(i) plus Proposition 8.1(i), in the exact
orientation audited in the direct-edge report, gives on the first edge

```text
i0*dp_0=i1*l,       so 6*i0=3*i1 and i1=2*i0.
```

On the second edge it gives

```text
i1*dp_1=i2*h,       so i1*(15K)=3*i2 and i2=5K*i1=10K*i0.
```

With primitive normalization `i0=1`, the indices are `(1,2,10K)`.  The
corresponding full degrees and `D` values are

```text
degp=(6,30K,60K),       D=(6,60K,120).
```

They also satisfy both Proposition 9.3(c) transports directly:

```text
D1=(D0+j*degp0)/nu0 = 6+(10K-1)*6 = 60K,
D2=(D1+n*degp1)/nu1 = (60K+18*30K)/(5K) = 120.
```

Thus different adjacent `i` values are required by the degree-product law;
they are not a mismatch.  The hostile review's normalized numbers `2` and
`4K` for the old `t=2` ray were arithmetically correct, but their inequality
does not supply an `i`-sync contradiction.  On the repaired ray the analogous
numbers are `2` and `10K`, again compatibly.

At the outer merge, two genuinely symmetric copies with the same `q` and
incoming scale have the same `i2`.  For actual source branches, equality of
their incoming scales is an additional landing/sibling obligation.  Full
`i`-sync can kill a particular landed pair whose source scales disagree, but
it does not uniformly kill this formal family.  It moves the unresolved
question to source provenance and sibling/gluing coverage.

## 7. Stop rule and negative control

The compiler/consumer stop rule is:

1. Verify every pinned source hash, labelled edge case, fixed multiplicity,
   N1 certificate, and the canonical record hash.  Drift or a missing
   mandatory predicate is a hard failure.
2. Emit the repaired family once; never enumerate `q` to a cap.  A consumer
   expressible in Presburger arithmetic over the exposed affine integer
   fields must return a finite progression refinement plus finite exceptions.
3. A claimed kill must cover every resulting progression by an exact
   certificate.  A surviving progression stays as a family record; it is not
   converted to a finite list or silently dropped.
4. If a consumer reads variable coefficient values, independently variable
   source `i` scale, unused siblings, Statement 3.9 data, landing, generic
   bilinear outer coupling, or an unclassified downstream transition, return
   `UNCOVERED` and stop.  Do not infer DEAD, ALIVE-realizable, or finiteness.
5. A complete nested-U2 endpoint requires a coverage theorem for every
   positive-length inter-merge segment.  This one record is a witness and a
   schema test, not that theorem.

The mandatory negative control is the reviewed `t=2` mutation:

```text
K=6q+1, nu=2K, kbar1=4K+2
=> gcd(kbar1,nu)=2
=> DEAD_N1_L6 for every q>=0.
```

The validator must reject it even though its edge equations, ODEs, MP2,
St 8.4, arrival coprimality, equal weight, and modeled zero price all pass.
This one control detects exactly the omission in both the producer and its
hostile review.

## 8. Maximum safe consequence

At the current local/formal tier, the original `nu=2K` obstruction is
superseded by a uniform N1/L6 kill, but the outer-finiteness obstruction is
not removed: the repaired `nu=5K`, `K==1 (mod 6)` ray is an exact infinite
formal family and one normalized semilinear record represents it without a
numerical cap.

The result neither proves that any member occurs in an actual Sigray source
tree nor that two symmetric branches glue.  It provides no complete family
language for all `t`, no landing, no polynomial pair, no counterexample, no
panel conclusion, no degree bound, no `G2`, and no JC2 conclusion.

No web, AWS, heavy computation, canonical edit, round-artifact edit, commit,
or push was used.

---

Report-body SHA-256 (all bytes strictly before the final separator):
`ce5cf26906d3c736e75c791c3600be201b65279aabbbacbf0b12014d51497c29`.
