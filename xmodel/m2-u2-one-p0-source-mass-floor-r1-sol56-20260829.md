# Nested U2 source-mass floor: the one-P0 ray cannot land below `td=15`

Date: 2026-08-29  
Producer: Sol 5.6 coordinator, exact desk proof  
Lifecycle: `PRODUCER_CHECKED`; independent hostile review required  
Scope: an **actual typed pole-tree landing** of the labelled
`U2--P0--U2` route; no claim that any landing exists at or above the bound

## 0. Result

The repaired semilinear one-P0 family is a genuine infinite family at its
declared formal-local tier, but it is not a threat to any current
`td<=12` panel.

The useful input is a more general arrival-subtree estimate.  Fix a global
type `(alpha,beta)`, with `1<alpha<beta`, and let an actual merge arrival
have reduced multiplicity `mu`.  The total pole mass in the arrival subtree
is at least

```text
min(2*beta, mu*alpha).                              (ASM)
```

For the displayed route, the inner U2 has two arrivals of multiplicity
`mu=3`, while the outer U2 has a second arrival subtree disjoint from the
one containing the inner U2.  Therefore

```text
td >= 2*min(2*beta,3*alpha) + beta >= 2*6+3 = 15.   (U2F)
```

Consequently **no member of the repaired `t==5 (mod 6)`, `K==1 (mod 6)`
family, and in fact no local member with the same inner/outer merge
arities and inner multiplicity, can land in an actual pole tree at
`td<=12`**.  This is a source-landing exclusion, independent of `K`, `t`,
N1/L6, the U2 ODE recurrence, coefficient gluing, absolute sheet index,
or a numerical enumeration.

The conclusion does not kill the formal family at `td>=15`, prove global
U2 finiteness, cover other positive inter-merge segments, or imply a degree
ceiling, `G2-PSC`, `G2-BD`, or JC2.

## 1. Pinned basis and typing

Full-file SHA-256 values recomputed before this proof:

- `ladder/SHEET6-MULTIPOLE.md`:
  `93adb7acedf4cf0fd56ffc68e4571649a04eab12e1271431449a79465a964bcb`;
- `ladder/BOOK-OFFAXIS.md`:
  `40104334b5e21d6495f9857a6c13a2877ad0e31a67529c5f23243e7170cfaaaa`;
- `ladder/SHEET6-TDUNIFORM.md`:
  `9034a987330f55c00e06689e35d6aac397da74fc129c3685437a155afe2f805d`;
- sealed family producer:
  `19fcd0133c72eba01dc4a554638111760a8813231a3b983a752d7d7528f58f82`;
- sealed `dq_0=3` correction:
  `4dde1c471b04d88db466293bc197c78529bc16743cc7ccde176e594bceb622dc`.

The exact promoted clauses used are:

1. MP0: the relevant set `U` is a finite rooted tree whose leaves are
   exactly the pole vertices.
2. MP1: non-merge vertices are exactly the regular vertices; distinct
   incoming subtrees at a merge are disjoint.
3. St 8.4: an arrival multiplicity satisfies `mu | M_H` at its incoming
   vertex `H`.
4. St 8.5 in the reviewed merge-free scope (`BOOK-OFFAXIS` section 2(a)):
   down a merge-free pole segment, the successive `M` values divide the
   pole entry value `M_P=b_P`.
5. Pole data (`TDUNIFORM` R1--R4 and MP4):

   ```text
   M_P=b,
   Lambda(P)=a*b*alpha*beta/nu,
   a,b in N*,
   nu | alpha  or  nu | beta,
   Lambda(P)>=beta,
   1<alpha<beta.
   ```

6. The corrected family has an inner binary U2 merge with arrival
   multiplicities `(3,3)`, followed rootward by one regular P0 vertex and
   then an outer binary U2 merge.  The displayed `dq_0` correction changes
   no arity or multiplicity.

No statement about reduced-pattern realization is promoted into a tree
statement silently: the theorem below is conditional on the labelled route
being instantiated by actual vertices of the MP0 tree.  This is precisely
the source-landing consumer left open by the family record.

## 2. Arrival-subtree mass lemma

Let `G` be an actual merge vertex and `H=G+c` one of its incoming vertices.
Write

```text
mu = mult(p_G^red,c).
```

Let `U_H` be the component above that incoming edge, and let `L_H` be its
set of pole leaves.  Then

```text
sum_(P in L_H) Lambda(P) >= min(2*beta,mu*alpha).   (ASM)
```

Proof.  MP0 makes `L_H` nonempty.

If `|L_H|>=2`, the pole lower bound gives

```text
sum_(P in L_H) Lambda(P) >= |L_H|*beta >= 2*beta.
```

If `|L_H|=1`, call its unique pole `P`.  A finite rooted subtree with one
leaf contains no merge: any vertex of in-degree at least two has at least
two descendant leaves.  Thus the path from `P` to `H` is merge-free.
Statement 8.4 and the reviewed Statement-8.5 chain give

```text
mu | M_H | M_P=b_P,
```

so `b_P>=mu`.  If `nu_P|alpha`, then

```text
Lambda(P)=a*b_P*(alpha/nu_P)*beta >= b_P*beta
                                             >= mu*beta > mu*alpha.
```

If `nu_P|beta`, then

```text
Lambda(P)=a*b_P*alpha*(beta/nu_P) >= b_P*alpha
                                             >= mu*alpha.
```

Hence the one-leaf subtree has mass at least `mu*alpha`.  Combining the two
cases proves (ASM).  QED.

The proof also covers the zero-length chain case `H=P`: then St 8.4 alone
gives `mu|b_P`, and no use of St 8.5 is needed.

### 2.1 General nested-merge corollary

Suppose an inner actual merge with arrival multiplicities
`mu_1,...,mu_r` lies anywhere inside one incoming subtree of an outer
actual merge of arity `R`.  No assumption on the length or local labels of
the intervening merge-free segment is needed.  The `r` subtrees entering
the inner merge and the `R-1` other subtrees entering the outer merge have
pairwise disjoint pole-leaf sets.  Applying (ASM) to the former and the
ordinary pole lower bound to the latter gives

```text
td >= sum_(e=1)^r min(2*beta,mu_e*alpha) + (R-1)*beta.  (NM)
```

Thus (ASM) is not specific to P0 or U2.  It is a cap-free source consumer
for every nested-merge skeleton, including a direct adjacent merge edge.
The one-P0 theorem below is the specialization
`r=R=2`, `mu_1=mu_2=3`.

## 3. Application to the one-P0 nested-U2 route

Assume the corrected labelled route lands in `U`.  Let `G_in` be its inner
U2 merge, `G_out` its outer U2 merge, and let the regular P0 chain lie on
one incoming branch of `G_out`.  At `G_in` there are two distinct incoming
subtrees, each with `mu=3`.  By (ASM), each carries pole mass at least

```text
c = min(2*beta,3*alpha).
```

Because `G_out` is binary, it has one other incoming subtree besides the
subtree containing `G_in`.  MP0 gives that other subtree at least one pole,
so its mass is at least `beta`.  The three pole sets are pairwise disjoint.
Using `td=sum_P Lambda(P)` gives

```text
td >= 2*c+beta = 2*min(2*beta,3*alpha)+beta.
```

Finally `alpha>=2` and `beta>=3`, so both `2*beta` and `3*alpha` are at
least six.  This proves `td>=15`.

Notice that no assumption about the outer unused sibling matching the
displayed P0 state was used.  Requiring two symmetric **full-route** copies
would only strengthen the floor.  The result therefore discharges the
record's unused-sibling debt at `td<=12` without assuming sibling
synchronization.

## 4. Sharpness of the argument and campaign consequence

For type `(2,3)`, the numerical bound produced by these inputs is exactly
`2*min(6,6)+3=15`; neither MP0/MP1 nor the pole formula alone improves it.
The proof asserts no configuration at equality.  Extra congruence,
coefficient, tower, root, or landing conditions may raise the floor or make
the route empty.

At current campaign scope this has two immediate consequences:

1. the repaired one-P0 semilinear ray is removed from every `td=8` and
   `td=12` source panel, even though it remains locally legal;
2. low-degree U2 work should concentrate on direct adjacent U2 edges,
   other intervening-segment types, and the row-to-actual-edge coverage
   map, rather than coefficient-gluing this particular ray.

A reusable compiler consumer should attach (ASM) to every actual merge
arrival and sum the disjoint subtree floors before expanding local pattern
families.  It is cap-free, exact, and can prune before any ODE or
coefficient computation.

## 5. Hostile-review checklist

The reviewer should attack, in order:

1. whether every actual U2 arrival in the family is an MP0-tree edge to
   which St 8.4 applies;
2. whether a one-leaf incoming subtree is necessarily merge-free in the
   exact orientation used by `F -> F^o`;
3. whether reviewed St 8.5 really composes to `M_H|b_P` on that segment,
   including a possible pole-adjacent zero-length case;
4. the two `nu|alpha` / `nu|beta` lower bounds for a pole with `mu|b`;
5. disjointness of the two inner-arrival pole sets and the outer unused
   sibling pole set;
6. whether the formal record actually fixes inner `(r,mu)=(2,3)` and outer
   `R=2` after applying the `dq_0=3` correction;
7. a counterexample tree with `td<=14`, if any premise above has been
   over-typed.

No web, AWS, heavy computation, canonical edit, commit, push, or access of
any kind to `jc2-lean` was used.

*End of sealed report body.*

---

## Seal

- Body byte count: `8611`.
- Body SHA-256:
  `42993a409e5ed4d2f4c4bb253e05e6ebf1b0e2f22dbd2eaf80bf71aa076d7f71`.
