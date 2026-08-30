# Q6 affine-ADE threat map: `U3/A3` and the full `B3/A2` modulus

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra sublane `/root/u_rows_global_lattice`  
Frozen basis: `54df5b64b5ea8355cd8c13aa790dcf0f703c5bb7`  
Lifecycle: **EXACT CONDITIONAL PRODUCER / DIFFERENT-MODEL REVIEW REQUIRED**

## 0. Verdict

On the exact `F_2/D_9` marking, the q=6 affine-ADE escape set is empty in
every locally classified `U3/A3` and `B3/A2` cell.  This includes all of the
following, separately rather than by an unweighted surrogate:

1. the two coefficient-one `U3` primes of degrees `4+4`;
2. the generic `B3` partition `4+2+2`;
3. the nonzero-modulus double-site block in each of its split, irreducible,
   and doubled-prime analytic forms;
4. the corrected `tau=0` total in each of its distinct-root, split
   double-site, irreducible, and doubled-prime forms;
5. every Euler-allowed affine root rank, every exceptional Cartier
   coefficient pattern, no contracted carrier or the sole possible simple
   carrier, and both possible bases of the adapted `A1` ruling.

The exact standard-library replay finds

```text
affine cells:                    0 necessary lattice survivors;
rank-zero / carrier controls:    0 necessary lattice survivors;
pair-condition matches before the carrier-forest filter: 0.
```

Thus no conclusion depends on treating an unlabelled positive intersection
as a cycle, on the contact depth of a split double site, or on a questionable
carrier triple point.  The weighted and tangent cells are joined exactly.

The maximum conditional theorem is:

> Assume the binding quadratic-F5 marking, Euler cap, horizontal-prime and
> contracted-carrier classifications, and rational-forest theorem.  Assume
> also the sealed q=6 local contact audit, including its analytic
> discriminant classification.  Then neither `U3/A3` nor any `B3/A2`
> modulus admits the necessary global boundary configuration.  Consequently
> no quadratic F5 first leg, and hence no Keller map in this presentation
> cell, can realize either row.

The `tau=0` and exact discriminant/contact-depth parts of the local audit are
still review-gated.  They are therefore conditional inputs here, not silently
promoted facts.  Combining this packet with the previously reviewed local
deaths of the other q=6 singular tags would conditionally empty the remaining
q=6 singular-F5 list.  It does not prove the quadratic frame occurs for a
minimal counterexample, does not treat nonquadratic presentations, and does
not prove JC2.

## 1. Custody, charged inputs, and object types

Root verified the completed local producer before this packet charged it:

```text
48717ce3d8b3c5ef6926e3b5ebcf2a0d94ad7bee42ea4ea1c253fb4fd9463649
  xmodel/bd-a2-q6-local-contact-audit-sol56-20260830.md
body 941d4e27b95bee2483b98fa62c4e1b9c9b94e7dff7aa200848ab03977461522d
manifest 222d1bffbd05d08103712f922e8baf5710fcf58dc23d144503c4ec94a4cbda83
```

The binding global inputs are

```text
f092a7152dea8bdee387825fa8181dffeb8145fc99cf65973d74f528491f57a0
  xmodel/bd-a2-a1-ruling-euler-boundary-cap-coordinator-integration-sol56-20260830.md

6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08
  xmodel/bd-a2-rational-forest-coordinator-integration-sol56-20260830.md

a5bf78c8ab8704884e9bb3c084c88059e01ec7690c1d6f645a9e87a0aa70a884
  xmodel/bd-a2-normal-f5-decorated-carrier-effectivity-reduction-coordinator-integration-sol56-20260830.md.
```

The q=8 lattice packet, full SHA
`5a31a2ab48746828f08cc0b7e2d349b2c2dc773a2faa59fa23a51cb667bbaecc`,
was used only as a checked algebraic precedent; every q=6 class and bound
below was rederived.

Three levels must remain separate.

- A **root allocation** is an integral class and coefficient pattern in the
  `D9` lattice.
- A **necessary strict decomposition** is a tuple of integral physical-prime
  classes satisfying all displayed numerical tests.  A doubled Cartier
  prime is one physical curve carrying weight two.
- An **effective configuration**, incidence surface, or polynomial map needs
  chronology, effectivity, analytic realization, and the upstream quadratic
  frame.  The replay never promotes a numerical tuple to one of these.

No active sibling report or external-model log was read.  There was no web
search, no heavy local computation, and no access to `jc2-lean` or
`pilot-local.log`.

## 2. Exact marking and strict totals

Use the orthogonal total-transform basis

```text
S0^2=-2,       S0.F=1,       F^2=0,
P_i.P_j=-delta_ij,

A=2S0+5F-sum_i P_i,         B=F,
K=-2S0-4F+sum_i P_i,
r^*R_X=4S0+11F-2sum_i P_i.                         (2.1)
```

Relabel the nine exceptional coordinates as

```text
l=0,          O={1,2},          I={3,4,5,6,7,8},
L=P_l,        T=S0+3F-sum_(i in I)P_i.              (2.2)
```

For `U3`, and for `B3,tau!=0`, the marked local exceptional different is

```text
M_R=2F-2P_l-P_o1-P_o2.
```

Therefore

```text
C0=4S0+9F-sum_i c_iP_i,
c=(0,1,1,2,2,2,2,2,2),
sum c_i=14,                 sum c_i^2=26.            (2.3)
```

For `B3,tau=0`, chronological orientation matters and the corrected class is

```text
M_R=2F-2P_l-2P_o2,
c_tau0=(0,2,0,2,2,2,2,2,2),
sum c_i=14,                 sum c_i^2=28.            (2.4)
```

Both totals have `C0.S0=C0.T=1`, `C0.L=0`, `A.C0=8`, and `B.C0=4`.

The sole possible q=6 contracted class is

```text
Z_J=S0+2F-sum_(j in J)P_j,
J=O union K,                K subset I, |K|=3.       (2.5)
```

Subtracting one `Z_J` from (2.3) leaves `3S0+7F-sum c_i^ZP_i`, with

```text
sum c_i^Z=9,                 sum (c_i^Z)^2=15.       (2.6)
```

Every `Z_J` contains both outside coordinates.  Hence two carriers or one
with coefficient at least two makes (2.3) negative.  Every `Z_J` also
contains the zero `o2` coordinate of (2.4), so no carrier coexists with the
`tau=0` total.

## 3. Local cells and complete Euler budgets

Here `k` counts distinct reduced physical ramification primes; Cartier
multiplicity does not create another support component.  The binding cap is

```text
r_0+r_aff+k+(one if Z is present)<=8.                (3.1)
```

The complete cells are:

| local cell | physical degrees / weights | `r_0` | `k` | `r_aff` cap | cap with `Z` |
|---|---|---:|---:|---:|---:|
| `U3/A3` | `(4,4)/(1,1)` | 3 | 2 | 3 | 2 |
| `B3`, `tau!=0,Delta!=0` | `(4,2,2)/(1,1,1)` | 2 | 3 | 3 | 2 |
| `B3`, `Delta=0`, split block | `(4,2,2)/(1,1,1)` | 2 | 3 | 3 | 2 |
| same, odd discriminant | `(4,4)/(1,1)` | 2 | 2 | 4 | 3 |
| same, doubled block | `(4,2)/(1,2)` | 2 | 2 | 4 | 3 |
| `B3,tau=0`, distinct/split residual | `(4,2,1,1)/(1,1,1,1)` | 2 | 4 | 2 | impossible |
| same, odd residual | `(4,2,2)/(1,1,1)` | 2 | 3 | 3 | impossible |
| same, doubled residual | `(4,2,1)/(1,1,2)` | 2 | 3 | 3 | impossible |

An allocation at the displayed maximum makes equality in (3.1), so the
adapted ruling base must be `A1`.  Every smaller rank permits either `A1` or
`P1`.  The replay includes the maximum, so it does not discard the affine
base branch; the complete-base sharpening is automatically a subset.

## 4. All affine exceptional root systems and coefficients

Write a square-minus-two class orthogonal to `A,B,K` as

```text
Q=aS0+bF-sum_i x_iP_i.
```

`B.Q=0` gives `a=0`; `A.Q=K.Q=0` gives `sum x_i=2b`; and `Q^2=-2` gives
`sum x_i^2=2`.  Up to sign the possibilities are

```text
P_i-P_j,                    F-P_i-P_j.                (4.1)
```

An affine singularity exceptional tree is disjoint from `H`; in particular
`S0.Q=L.Q=T.Q=0`.  This removes the second family, removes `l`, and forces
the two indices of a difference root to lie both in `I` or both in `O`.
The abstract root lattice is therefore

```text
A5(I) direct-sum A1(O).                               (4.2)
```

Every connected root subsystem of (4.2) is type `A`; no `D` or `E` embedding
exists.  Disconnected systems are products of disjoint `A` chains.  In the
fixed local chronology, the positive `O` root `P_o1-P_o2` is already the
local `R2` (`B3`) or `E3` (`U3`), while its reverse is anti-effective.  Thus
an actual *additional* affine tree uses `I`.  For safety, the symmetric
`tau!=0` replay nevertheless includes the formal `O` orbit and still finds
zero; in (2.4) its positive orientation already makes the total negative.

For a directed `A_s` chain with Cartier vector
`m=(m_1,...,m_s)>0`, put

```text
delta=(m_1,m_2-m_1,...,m_s-m_(s-1),-m_s),
n=C_As*m=(delta_0-delta_1,...,delta_(s-1)-delta_s).
                                                               (4.3)
```

The residual total coordinates are `base+delta`.  Positivity of strict
contact makes `delta` nonincreasing; its entries sum to zero.  Effectivity
gives `delta_i>=-base`, hence `delta_0<=s*base`.  This is a proof of finite
completeness, not an arbitrary coefficient cutoff.

With no `Z`, a connected affine tree can attach the already connected local
support at only one root vertex.  For an `I` block (`base=2`) every allowed
coefficient vector is exactly:

| type | all `m` with one-vertex strict support |
|---|---|
| `A1` | `(1)`, `(2)` |
| `A2` | `(1,2)`, `(2,1)`, `(4,2)` |
| `A3` | `(1,2,1)`, `(2,4,2)`, `(3,2,1)`, `(6,4,2)` |
| `A4` | `(3,6,4,2)`, `(4,3,2,1)`, `(8,6,4,2)` |

The formal `O/A1` block has only `m=(1)`.  With one `Z`, a connected affine
tree may have one carrier contact and one residual-strict contact.  The
complete two-support lists needed through rank three are:

| type | all `I`-block `m` with at most two contact vertices |
|---|---|
| `A1` | `(1)`, `(2)` |
| `A2` | `(1,1)`, `(1,2)`, `(2,1)`, `(2,2)`, `(3,2)`, `(4,2)` |
| `A3` | `(1,1,1)`, `(1,2,1)`, `(1,2,2)`, `(2,2,1)`, `(2,2,2)`, `(2,4,2)`, `(3,2,1)`, `(3,4,2)`, `(4,3,2)`, `(4,4,2)`, `(5,4,2)`, `(6,4,2)` |

The replay forms every multiset of these disjoint blocks using at most the
six `I` coordinates, optionally adds the formal `O/A1`, and imposes the
Euler rank cap.  Carrier triples are then quotiented only by the stabilizer
of the full oriented, coefficient-labelled root allocation.

## 5. Weighted prime classes, proximity, and the contact-labelled forest

For each reduced physical prime write

```text
C_j=a_jS0+(2a_j+epsilon_j)F-sum_i x_(ji)P_i,
a_j>0,                 epsilon_j>=0.                 (5.1)
```

Horizontality `a_j=B.C_j>0` follows because a vertical curve would be a
component of the already complete marked local fibre, whereas the polar germ
is not.  If `w_j` is its Cartier weight and `A0=4` (or `3` after `Z`), then

```text
sum_j w_j a_j=A0,
sum_j w_j epsilon_j=1,
sum_j w_j t_j=1,
sum_j w_j x_(ji)=c_i,                                (5.2)

t_j=3a_j+epsilon_j-sum_(i in I)x_(ji)>=0,
d_j=5a_j+2epsilon_j-sum_i x_(ji),                    (5.3)

delta(C_j)
 =1+(2a_j^2+2a_j epsilon_j-sum_i x_(ji)^2+a_j-d_j)/2
 >=0,                                                  (5.4)

C_j.C_k
 =2a_ja_k+a_j epsilon_k+a_k epsilon_j
  -sum_i x_(ji)x_(ki).                                (5.5)
```

Because the weighted sums in (5.2) equal one, the `S0` and `T` contacts are
owned by coefficient-one primes.  On a root chain,
`C_j.(P_p-P_q)=x_jp-x_jq>=0`; this is the required local proximity
inequality.  A residual root contact can be assigned to a weight-`w_j`
prime only if it is divisible by `w_j`, after which the prime receives the
quotient.  All other proximity inequalities are deliberately omitted: that
only enlarges the necessary-lattice set, so an empty relaxed set is safe.

The local audit supplies the exact correction

```text
C_i.C_j=lambda_ij,                                   (5.6)
```

where `lambda_ij=0` for distinct marked sites and
`lambda_ij=ord(discriminant)/2>=1` for the two branches of a split double
site.  In a doubled-prime cell there is one reduced vertex with weight two,
not two vertices.  Accordingly the replay uses:

- pairwise zero for `U3`, generic `B3`, and every irreducible/doubled block
  against its distinct-site companions;
- zero for all cross pairs and an arbitrary positive integer for the two
  split-block branches;
- weighted total equality for every doubled prime.

For a carrier, the code labels root contacts separately as `Z` and strict
contacts.  Each may use at most one vertex of a connected root tree.  Two
distinct direct strict owners, two disconnected affine bridges, or a direct
and bridge path with distinct owners are rejected as genuinely distinct
paths.  A same-owner direct/bridge triple is retained as unresolved rather
than guessed away.  In fact no tuple reaches this filter: every cell has
zero pair-condition matches before carrier processing.  Thus even this
conservative carrier rule is non-load-bearing.

## 6. Conceptual lower bounds

For coefficient-one decompositions in which every physical pair must be
disjoint after the local correction, integrality gives

```text
sum_(j<k) C_j.C_k
 >=2sum_(j<k)a_ja_k+A0-a_e
   -(sum_i(c_i^2-c_i))/2,                             (6.1)
```

where `a_e` is the `a` value of the unique `epsilon=1` prime.  This uses only
`x^2>=x` for nonnegative integers.  It is applied only where the local audit
proves that every `lambda_ij` is zero.

There is a weighted replacement for every split or doubled block.  Partition
the total Cartier divisor into the block `D_G` and its distinct-site
complement `D_H`.  With weighted aggregate data `a_G,epsilon_G` and
`a_H,epsilon_H`, every cross physical pair has local correction zero, while

```text
D_G.D_H
 >=2a_Ga_H+a_G epsilon_H+a_H epsilon_G
   -(sum_i(c_i^2-c_i))/2.                             (6.2)
```

The positive intersection internal to a split block is entirely inside
`D_G` and never enters (6.2).  This is the clean reason arbitrary contact
depth does not escape.

For the `tau=0` four-prime rows, positivity forces every `a_j=1`.  Substituting
`a=1` into (5.3)--(5.4) gives

```text
delta(C_j)=(sum_i x_ji-sum_i x_ji^2)/2.
```

Hence every adjunction-valid multiplicity is zero-one.  But a nonzero
support-one `I` root allocation of rank at most two demands contact at least
two.  No branch can own it.  This proves the replay's `no-meta` result for
both distinct and split four-prime affine cells without a join search.

## 7. Exact enumeration results

The diagnostic bound below is (6.1) for coefficient-one zero-pair cells and
(6.2) for split/doubled cells, minimized after degree, unit-contact,
adjunction, root-contact, and chronological `O` filtering.  `No meta` means
one of those branch lists was already empty.  Candidate records are the sum
of individual branch-candidate list sizes across exact-join metadata; they
are not a claimed count of geometric configurations.

| affine cell | allocation orbits | feasible allocations | feasible/join metas | candidate records | diagnostic minimum | pair matches | survivors |
|---|---:|---:|---:|---:|---:|---:|---:|
| `U3` | 31 | 7 | 40 | 656 | 1 | 0 | 0 |
| `U3+Z` | 26 | 8 | 28 | 176 | 2 | 0 | 0 |
| `B3 tau!=0, Delta!=0` | 31 | 4 | 16 | 454 | 4 | 0 | 0 |
| same `+Z` | 26 | 4 | 18 | 186 | 5 | 0 | 0 |
| `Delta=0`, split | 31 | 4 | 16 | 454 | 2 | 0 | 0 |
| same `+Z` | 26 | 4 | 18 | 186 | 3 | 0 | 0 |
| `Delta=0`, odd | 62 | 8 | 42 | 660 | 1 | 0 | 0 |
| same `+Z` | 70 | 16 | 58 | 262 | 2 | 0 | 0 |
| `Delta=0`, doubled | 62 | 10 | 16 | 163 | 1 | 0 | 0 |
| same `+Z` | 70 | 6 | 6 | 19 | 1 | 0 | 0 |
| `tau=0`, distinct residual | 8 | 0 | 0 | 0 | no meta | 0 | 0 |
| `tau=0`, split residual | 8 | 0 | 0 | 0 | no meta | 0 | 0 |
| `tau=0`, odd residual | 22 | 1 | 7 | 123 | 4 | 0 | 0 |
| `tau=0`, doubled residual | 22 | 2 | 2 | 32 | 1 | 0 | 0 |

The formal no-affine and carrier-only cells were replayed independently, not
assumed from the older unweighted table:

| rank-zero control | feasible/join metas | candidate records | diagnostic minimum | pair matches | survivors |
|---|---:|---:|---:|---:|---:|
| `U3` | 6 | 972 | 3 | 0 | 0 |
| `U3+Z` | 2 | 72 | 3 | 0 | 0 |
| generic `B3` | 11 | 1355 | 6 | 0 | 0 |
| generic `B3+Z` | 1 | 60 | 5 | 0 | 0 |
| split `Delta=0` block | 11 | 1355 | 3 | 0 | 0 |
| same `+Z` | 1 | 60 | 3 | 0 | 0 |
| odd `Delta=0` block | 6 | 972 | 3 | 0 | 0 |
| same `+Z` | 2 | 72 | 3 | 0 | 0 |
| doubled `Delta=0` block | 1 | 141 | 4 | 0 | 0 |
| same `+Z` | 1 | 21 | 3 | 0 | 0 |
| `tau=0`, distinct residual | 1 | 80 | 8 | 0 | 0 |
| `tau=0`, split residual | 1 | 80 | 3 | 0 | 0 |
| `tau=0`, odd residual | 9 | 679 | 5 | 0 | 0 |
| `tau=0`, doubled residual | 1 | 60 | 3 | 0 | 0 |

No energy diagnostic prunes a metadata row in the executable.  Every
feasible row is passed to the exact weighted coordinate join.  Thus the
zero result is independently visible even if one distrusts (6.1) or (6.2).

The root-inventory digests are:

| orbit family | inventory SHA-256 |
|---|---|
| ordinary total, rank cap 3 | `4e584d96f2e8312388d1576d549473ac628ad74aced2fef09e50379fdf4e6ff0` |
| ordinary total plus `Z`, rank cap 2 | `f46c9543e7ec0935347a71bfdd57ac54f02cabb06633de8401b085833bc7104c` |
| ordinary total, rank cap 4 | `4932df18ae6e297686b495698ebda75e481c82de758cf4e5aa35c82ad173bf13` |
| ordinary total plus `Z`, rank cap 3 | `428206d838650d097d7816e090189971057013115cdad17219ca421a4f68518d` |
| `tau=0`, rank cap 2 | `5b5969b7bc521f5ddd3717cefd142c071c14bebb635c6c075b3588bf02b80f80` |
| `tau=0`, rank cap 3 | `31e66e9e8be4f7083bf848c4727bf3fc30c842fb3f63d45fd7b7065aabd0d5db` |
| rank-zero, no `Z` | `ae2f1f8555d22ebc2d0e35b417bc6ec05e7c45d1ad3e90d3f907b934a15eafeb` |
| rank-zero, one `Z` | `07d3ff8e578ed5256e58703cf3aaecc618535dac6b23de8a8c09884b479848d4` |

Counts are canonical root/coefficient or carrier-relative orbits.  Physical
branches remain labelled by their local role; split twins are not divided by
an extra factor of two.  The empty survivor serialization is 830 bytes with
SHA-256
`ab2fc3c6c5d47160fa947542dd5d33e375c9221a43df05c10cd99cfb6926b46d`.

## 8. Replay and negative controls

The standard-library certificate is

```text
ops/q6_f5_affine_ade_threat_replay.py
SHA-256 b892cd1520f13f10093fc51f547672cb8145ad4949c92a86a6ecb9055f3bdd46
```

Run:

```bash
q6_tmp=$(mktemp -d)
python3 ops/q6_f5_affine_ade_threat_replay.py > "$q6_tmp/ordinary.json"
python3 -O ops/q6_f5_affine_ade_threat_replay.py > "$q6_tmp/O.json"
python3 -OO ops/q6_f5_affine_ade_threat_replay.py > "$q6_tmp/OO.json"
cmp "$q6_tmp/ordinary.json" "$q6_tmp/O.json"
cmp "$q6_tmp/ordinary.json" "$q6_tmp/OO.json"
shasum -a 256 "$q6_tmp/ordinary.json" "$q6_tmp/O.json" "$q6_tmp/OO.json"
```

All three outputs are byte-identical, 33,979 bytes, with SHA-256

```text
293f2aee078dbcb0448c57ce4720646503719e2596a9454e709736baa041d602.
```

An AST walk finds zero `assert` nodes.  The executable uses explicit
`require(...)/RuntimeError` checks.  In each of ordinary, `-O`, and `-OO`
modes,

```bash
python3 [MODE] ops/q6_f5_affine_ade_threat_replay.py --mutate-contact
```

exits nonzero with the exact diagnostic

```text
FAIL:q6 baseline multiplicity sum must be fourteen
```

The ordinary replay used about one second and 22 MB resident memory on the
coordinator host.  It is a desk calculation; AWS and a heavy CAS are neither
needed nor used.

## 9. Remaining review and falsification targets

1. Independently replay the local analytic discriminant classification,
   especially the arbitrarily deep split contact and the literal doubled
   prime in `tau=0`.
2. Independently rederive the `O` chronology and the assertion that every
   additional affine ADE exceptional tree is disjoint from `H`.
3. Reimplement the finite join from the displayed formulas without importing
   the producer script; mutate one Cartier weight, one root orientation, and
   one local `lambda` rule.
4. If all three pass, integrate the theorem as the q=6 closure of the
   singular quadratic-F5 lane.  Do not promote it as a theorem about
   nonquadratic incidences or JC2 itself.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `19673`.
- Body SHA-256:
  `ef8e80f4744e382d98bbfbfe4c335d1c7feac217e7ffc689ae3d8e4fe1ce9a7e`.
- Frozen basis: `54df5b64b5ea8355cd8c13aa790dcf0f703c5bb7`.
