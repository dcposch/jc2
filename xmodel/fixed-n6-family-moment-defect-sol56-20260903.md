# FIXED-N6 FAMILY — orbit correction, first moment page, and the missing valuated-rank interface

**Lane/date.** FIXED-N6 FAMILY, 2026-09-03.  **Status of new work:**
`PROVED-HERE / UNREVIEWED` unless a narrower type is printed.  Computations
labelled `WITNESS-ONLY` or `CONDITIONAL-MACRO` are not promoted to facts about
an actual Keller pair.  No canonical ledger was edited, no `jc2-lean` file was
inspected, and no uncharged ideation or running-lane report was read.

## 0. Custody, direct verdict, and scope correction

The mandatory custody gate ran before any input was opened.  All eight frozen
copies matched the charged SHA-256 values exactly:

```text
20f290f7e33a3b8a4f97d303751633b9d9b2df50ca8cbd0a46498856be5d5b2f  ideation-20260903T1015Z-sol56.md
20d554a0b19c563093ec35caad58664f800d7517490f530a07f511d7042393b6  global-interpolation-sol56-20260902.md
49ba5a019714e30a952c998fb39a88aff38505a80fcac6df3c5883bb16599588  globalinterp.py
55db4a9ef9021ef28d3a86dbd3e44d5e3a5aa1b72d61ba23043497f78ba94411  branch-orbits-v2-grok46-20260903.md
aaea3c345b1d53f561798f6a3e4352722f56c50a762f141dfe5e59cf35b1f276  knapsack.py
fb137b92d88b2f59f369bbffb2a0591aed69e9294135751c329da9eea58f6948  census-rebase-opus5-20260902.md
d20bf0841a1ba2b229d423bb948e6c4474a4f5a83f55148071cae39cb6c506c2  moh_skeleton_full.py
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  integration17-coordinator-fable51-20260902.md
```

**Direct verdict.**  There are four distinct conclusions.

1. **PROVED-HERE:** after deleting Moh's historical search cap and treating
   existence as a hypothesis, the proposed formulas give an exact unbounded
   family of numerical skeletons satisfying the arithmetic content of
   (1)--(13).  The complete algebra is in section 1.
2. **PROVED-HERE:** branch-orbit closure destroys the advertised fixed
   `N=6`.  The only positive packet made from this `(10)`-only type has
   `k=A_2`, hence

   ```text
   (L,k,N)=(5,18,9),(13,48,24),(21,78,39),(29,108,54).
   ```

   More generally `N=15a+9`; it grows.  Formal `k=12,N=6` is a partial
   orbit for every member and must be refused.
3. **REFUTED:** the frozen `GLOBAL-INTERPOLATION/1.0` driver does not perform
   the promised orbit-custody check.  It trusts `verified:true`, ignores an
   inconsistent expected orbit size and generator, and accepts the supplied
   partial-orbit negative control.  The wrapper delivered here refuses it.
4. **OPEN, finitely typed:** the charge does not determine a decorated
   first-page system.  It supplies the proper disc orbit and the *number* of
   remaining roots, but not their contact tree, branch Galois permutation,
   Puiseux templates, coefficient sharing, active support, or precision guard.
   Consequently there is no family-intrinsic matrix, tropical minimum basis,
   Schur complement, or leading coefficient to emit from these data.

What is invariant can still be settled exactly.  The raw consecutive moment
parity matrix is MDS: its proper-root submatrix already has full row rank
`34,90,146,202`, so its cokernel is identically zero and the non-proper block
adds no raw rank.  Under the additional, unproved rule “one free macro
coordinate per cubic slot,” the proper defect instead grows as
`16,42,68,94`, and the non-proper Schur block repairs it exactly.  This
dichotomy identifies the missing map: the associated-graded evaluation map
from actual tame/root coefficients to branch primitive values.

### 0.1 Literal versus extended `(1)--(13)`

Two qualifications are non-negotiable.

First, Moh's printed (1) says `n<=100`
(`census-rebase-opus5-20260902.md:63-85`).  Here `L>=5` gives `n=21L>=105`.
Thus no member literally satisfies printed condition (1).  “Passes
(1)--(13)” below always means the **degree-unbounded numerical extension** in
which this historical enumeration cutoff is removed.

Second, printed (3) asserts an actual constant-Jacobian pair and simultaneous
degree-minimality, while (4) says that the displayed integers are actual
characteristic data of that pair.  A list of integers cannot prove either
assertion.  What is proved is exactly the arithmetic skeleton tested by
`Skel.windows_ok()` and `Skel.full_ok()`, conditional on hypothetical
realisability.  This is also the qualification made by the charged Sol report
at its lines 303--340.  Calling the family an actual `(1)--(13)` family would
silently assume the main realisability problem.

## 1. Symbolic verification of the extended numerical skeleton

Let `a>=0`, `L=8a+5`, and set

```text
n=21L,                  m=14L,              M_1=-14L,
M_2=7(3L+1)/4,          M_3=21L-2,          s=3,
V_2=1,                  V_3=5.
```

Since `3L+1=24a+16`,

```text
M_2=42a+28 in Z.
```

The sequence is strictly ordered:

```text
M_2-M_1 = 7(11L+1)/4 = 154a+98 > 0,
M_3-M_2 = (63L-15)/4 = 126a+75 > 0.
```

After removing only the printed `n<=100` cutoff, condition (1) has
`m=-M_1=14L<21L=n`.  For (2), `n/m=3/2` is not integral, hence `m` does not
divide `n`, and `M_3=n-2`.

The normalized degree data are

```text
K=gcd(n,m)=7L,          e=n/K=3,            d=m/K=2,
gcd(d,e)=1.
```

These are the numerical shadows used by the enumerator; they do not supply
the pair demanded in printed (3)--(4).

### 1.1 Condition (5): the complete gcd chain

The first gcd is immediate:

```text
d_2=gcd(21L,-14L)=7L.
```

Put `B=(3L+1)/4`.  Since `4B-3L=1`, `gcd(L,B)=1`, and therefore

```text
d_3=gcd(7L,7B)=7.
```

Finally

```text
d_4=gcd(7,21L-2)=gcd(7,2)=1.
```

Thus the exact chain is

```text
(d_1,d_2,d_3,d_4)=(21L,7L,7,1).
```

### 1.2 Conditions (6)--(7): depth and both windows

Condition (6) holds because `s=3` and `d_s=d_3=7>=4`.  The enumerator's
top choice also has `0<V_3=5<d_3=7`, leaving top minor multiplicity two.

At `r=3`, with `V_4=d_4=1`, condition (7) is exactly

```text
d_3/(n-M_3)=7/2 < 5=V_3 <= V_4 d_3/d_4=7.
```

Also

```text
n-M_2=7(9L-1)/4,
```

so the `r=2` window is

```text
4L/(9L-1) < 1=V_2 <= V_3 d_2/d_3=5L.
```

The strict inequality on the left is equivalent to `5L>1` and is automatic.

### 1.3 Condition (8): all radii

The implemented Definition 5.1(3) formula is

```text
delta_i = 1 - (n-M_i)/(n-M_s-1)
                 * product_{j>i}
                   [V_j(n-M_j)-d_j]/[V_j(n-M_{j-1})-d_j].
```

Here

```text
n-M_3-1=1,
V_3(n-M_3)-d_3=10-7=3,
V_3(n-M_2)-d_3=63(5L-1)/4.
```

Consequently

```text
delta_3=1-(n-M_3)=-1,

delta_2
 =1-[7(9L-1)/4]*3/[63(5L-1)/4]
 =2(3L-1)/[3(5L-1)].
```

At the last level,

```text
[V_2(n-M_2)-d_2]/[V_2(n-M_1)-d_2]
  =[7(5L-1)/4]/(28L)
  =(5L-1)/(16L).
```

The product subtracted from one is therefore

```text
35L * (5L-1)/(16L) * 4/[21(5L-1)] = 5/12,
```

and

```text
delta_1=7/12.
```

All denominators used above are positive, and direct subtraction gives

```text
-1=delta_3 < delta_2 < delta_1=7/12.
```

### 1.4 Denominator increments `A_2,A_1`

Because the only preceding radius for `delta_2` is the integral `delta_3`,
`A_2` is the reduced denominator of `delta_2`.  With `L=8a+5`, its raw
numerator and denominator are

```text
2(3L-1)=4(12a+7),
3(5L-1)=4*6(5a+3).
```

Now `gcd(12a+7,6)=1`, and

```text
5(12a+7)-12(5a+3)=-1,
```

so the raw gcd is exactly four.  Hence

```text
A_2=3(5L-1)/4=30a+18=6(5a+3).
```

For the bottom increment the preceding lcm is `A_2`, and

```text
A_1=den(A_2*delta_1)
   =den(7(5a+3)/2)
   ={ 2, a even, L=5 mod 16;
      1, a odd,  L=13 mod 16. }
```

### 1.5 Conditions (9)--(11)

There is only one `(9)--(11)` level, `j=2`.  Its polynomial degree is

```text
Q=V_3 d_2/d_3=5L=40a+25.
```

Since

```text
Q-A_2=10a+7>0,          2A_2-Q=20a+11>0,
```

the division in (9) is exactly

```text
5L = 1*A_2 + (5L+3)/4
   = 1*(30a+18)+(10a+7).
```

Thus `triangle_2=1` and `square_2=10a+7`.  Condition (10) holds with
equality, `V_2=1<=triangle_2`.  Condition (11) fails: one has

```text
0 < square_2-V_2=10a+6 < A_2,
```

so `A_2` does not divide `V_2-square_2`.  The split `D_2 -> D_1` is therefore
**(10)-only**, not a choice between the two branches.

### 1.6 Conditions (12)--(13), and `q,u`

At the bottom `n/d_2=e=3`, `m/d_2=d=2`, and `V_2=1`.
If `A_1=2`, (12) fails while (13) holds because

```text
2 | d V_2=2,            2 | e V_2-1=2.
```

If `A_1=1`, both printed alternatives hold trivially.  This degeneration of
the bottom congruence is not an `(11)` zero-centre choice at `D_2 -> D_1`;
that `(11)` branch was just proved impossible.

Finally the D1-PIN quantities reduce without qualification:

```text
q=(1-delta_1)de/(d+e)=(5/12)*(6/5)=1/2,
u=V_3 K/d_3=5L=40a+25.
```

This completes the symbolic arithmetic verification.  Independent exact
evaluation by the charged `Skel` class returned `windows_ok=True` and
`full_ok=True` at all four requested values, with no floating arithmetic.

## 2. Orbit-admissible packets and the corrected root ledger

Branch-orbits v2 proves, for one orbit of bottom-major discs,

```text
|O|(D_1)=product_{j=2}^{s-1} omega_j,
omega_j=A_j on (10),  omega_j=1 on (11).
```

It also proves that `A_1` governs the internal roots of one `D_1`, not the
number of `D_1` discs, and that at `s=3` the packing
`sum |O|V_2 <= u` is exact at the unique `D_2`
(`branch-orbits-v2-grok46-20260903.md:192-266`).

Here there is one `(10)`-only level, so

```text
|O|=A_2=30a+18.
```

If `t` copies of this one packet type are used, then

```text
k=tA_2,                 N=k V_2 q=tA_2/2,
tA_2<=u.
```

But `A_2<=u` and

```text
2A_2-u=(5L-3)/2>0.
```

Therefore `t=1` is the only positive choice:

```text
k=A_2,                  N=A_2/2=15a+9,
u-k=(5L+3)/4=10a+7=square_2<A_2.
```

The inequality is a packing capacity, not a claim that the unused slots are
attained by a particular minor subtree.

| `L` | `a` | `(n,m)` | `M_2` | `delta_2` | `A_1` | `k=A_2` | bottom branch | `u` | `N` | unused `u-k` |
|---:|---:|---:|---:|---:|---:|---:|:---|---:|---:|---:|
| 5 | 0 | (105,70) | 28 | 7/18 | 2 | 18 | (13) only | 25 | 9 | 7 |
| 13 | 1 | (273,182) | 70 | 19/48 | 1 | 48 | both | 65 | 24 | 17 |
| 21 | 2 | (441,294) | 112 | 31/78 | 2 | 78 | (13) only | 105 | 39 | 27 |
| 29 | 3 | (609,406) | 154 | 43/108 | 1 | 108 | both | 145 | 54 | 37 |

In particular, `k=12` is not in `A_2 Z_{>0}` for any member.  At `L=5`
this corrects the formal group-A packet from `(k,N)=(12,6)` to `(18,9)`, in
agreement with the exact `D=105` orbit calculation in the charged v2 report.
The title “fixed-N6 family” now names the historical proposal, not the
corrected family.

### 2.1 Proper, major-residual, and top-minor roots

Each bottom star has `eV_2=3` roots and is fixed, after discwise
normalization, by

```text
p_g(pi)=pi^3-pi,        p_f(pi)=pi^2-2/3.
```

The unique `D_2` contains `ue=15L` major roots.  Thus the orbit packet
contains `3k` proper bottom roots and leaves `3(5L-k)` roots inside `D_2`.
The top minor child contains

```text
n-ue=21L-15L=6L
```

roots.  The aggregate zero-charge/non-proper count requested in the charge is

```text
3(5L-k)+6L = 3(7L-k)=e(K-sum_B V_2(B)).
```

| `L` | proper `3k` | all roots in `D_2` | residual in `D_2` | top minor | aggregate non-proper | check total |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 54 | 75 | 21 | 30 | 51 | 105 |
| 13 | 144 | 195 | 51 | 78 | 129 | 273 |
| 21 | 234 | 315 | 81 | 126 | 207 | 441 |
| 29 | 324 | 435 | 111 | 174 | 285 | 609 |

These are exact counts.  They do not specify how either residual collection
splits, and `NONPROPER-COUNT` is not a tree.

## 3. Why the requested decorated first page is not determined

The charged global-interpolation theorem defines a decorated skeleton to
order `Q` as a bare skeleton plus all of the following
(`global-interpolation-sol56-20260902.md:459-558`):

1. a rooted cluster tree on all `n` labelled leaves;
2. a cyclic action, with complete branch orbits and stabilizers;
3. a truncated Puiseux series `tau_i(z)` for every leaf;
4. declarations identifying shared tame coefficients;
5. a target order and a guard sufficient for every inverse and primitive;
6. the polynomial coefficient support/gauge.

The present charge fixes the proper disc count, the one disc orbit, the cubic
leading stars, the unique major `D_2`, and two aggregate residual counts.  It
does not fix any of items 1--6 for the non-proper roots.  In particular:

- a Galois orbit of **discs** is not a Galois orbit of the three individual
  roots in each disc;
- the `A_1=1` and `A_1=2` cases have different internal stabilizer behavior;
- the `3(5L-k)` roots left in `D_2` may have several minor subclusters and
  several first-separation radii;
- the `6L` top-minor roots may likewise split in many ways;
- “rigid star” fixes leading polynomials but does not say which deformations,
  primitive constants, or tail coefficients are independent after descent;
- a junction gap is provenance, not automatically the first nonzero
  coefficient order of every moment row.

The minimal common denominators coming only from the three displayed radii
are

| `L` | `R=lcm(den delta_2,12)` | `R delta_2` | `R delta_1` | bottom gap `R(delta_1-delta_2)` |
|---:|---:|---:|---:|---:|
| 5 | 36 | 14 | 21 | 7 |
| 13 | 48 | 19 | 28 | 9 |
| 21 | 156 | 62 | 91 | 29 |
| 29 | 108 | 43 | 63 | 20 |

These four gaps are **PROVED-HERE / UNREVIEWED junction labels only**.  A
non-proper split can activate before or after them, and orbit trace may cancel
the nominal leading coefficient.  They are not four emitted first pages.

There is an additional numerical warning.  If all residual-major roots are
placed in one cluster with mutual contact `rho`, a residual branch has

```text
ord_t D_i=(3(5L-k)-1)rho+3k delta_2-6L.
```

The threshold `ord D_i=-1` simplifies exactly to `rho=2/5`.  Thus strict
zero-charge behavior in this one-cluster completion needs

```text
delta_2 < rho < 2/5.
```

This missing separation occurs *before* `delta_1=7/12` and therefore changes
the alleged first bottom page.  Supplying only the residual root count cannot
determine that page.

Accordingly:

`OPEN[FAMILY-FIRST-PAGE-MATRIX]` — **bounded quantity:** four members, one
graded page, respectively 34, 90, 146 and 202 homogeneous DEG rows.  **Cheapest
test:** at `L=5`, provide the complete non-proper contact tree, generator
permutation on all 105 branches, equivariant templates through the inverse
guard, sharing classes, and the domain filtration; then eliminate auxiliary
variables and compare the direct moment Jacobian with coefficient
interpolation.  Only after that comparison should the construction be scaled.

No safe replacement exists in the frozen data, so this OPEN is not filled by
choosing convenient rational centres.

## 4. Frozen driver audit, custody repair, and resource stop

### 4.1 The upstream partial-orbit control fails

The frozen driver documents `orbits.O.verified=true` as an assertion.  Its
implementation checks only that the named representative belongs to the list
of branches carrying label `O`; it checks neither an expected size, a
generator permutation, nor coefficientwise covariance under `z -> omega z`.

The negative fixture `custody-partial-orbit.json` declares two members, an
expected orbit size three, and a generator of order two.  Nevertheless the
frozen command exits zero and reports

```text
NO-LOG equations: 2 branchwise, 1 effective with verified orbit metadata
```

so the bad group is used for descent.  Therefore:

```text
REFUTED: GLOBAL-INTERPOLATION/1.0 refuses a partial orbit.
```

The delivered preflight verifies the `(10),V2=1` packet type, exact rigid
bottom star, distinct member count, bijectivity, one-cycle closure, the
family-required `(10)` orbit size, and all advertised root-block counts before
any descent.  On the historical `L=5,k=12` fixture it exits 2:

```text
REFUSED[ORBIT-SIZE]: L=5 has (10)-orbit size A2=18; requested k=12
```

This is the requested custody refusal.  It validates only the proper packet;
it deliberately prints `full_globalinterp_decoration=false` until the missing
leaf action and templates are supplied.

### 4.2 The full quadratic lift is outside the desk cap even at `L=5`

The frozen emitter is exact but expands branch powers for all `r=2,...,m`.
For a top-minor branch of `z`-valuation `-R`, in Moh total-degree mode and any
`qmax>=0`, its own recurrence gives

```text
desired_power[r] >= R*m.
```

The number of branch-power variables contributed by top-minor roots alone is
therefore at least

```text
6L*(m-1)*(R*m+1).
```

| `L` | lower bound before products/inverses/times/evaluations |
|---:|---:|
| 5 | 5,218,470 |
| 13 | 123,348,966 |
| 21 | 1,693,244,070 |
| 29 | 3,090,039,030 |

Millions of prospective SymPy variables make even the first lift not credibly
fit the intended 6 GB desk envelope; the later cases are orders of magnitude
larger.  This is a conservative structural preflight rejection, not a formal
byte lower bound or an observed out-of-memory event.  In accordance with the
stop rule, no full lift was launched.  There is no “largest `L` that fit”:
none of the four full quadratic lifts passes the preflight.  The main scalable
direct GRS projection ran in seconds and below 22 MB; the independent audit
remained below 70 MB.

The frozen driver also has no command that emits an initial-form moment
matrix, tropical bases, or a proper/non-proper Schur complement.  Its `rank`
field is the ambient Jacobian rank of a quadratic auxiliary presentation; it
is not any of those three ranks.

## 5. Exact raw moment-parity theorem

This section isolates everything that *is* determined once “unknown” means an
independent branch value `H_i`.

Let `F` be the valued Puiseux field, let the `n` roots be distinct, and put

```text
D_i=product_{j!=i}(tau_i-tau_j),
P_{r i}=tau_i^r/D_i,       0<=r<h,
h=n-m-1=K-1=7L-1.
```

For every set `S` of `h` columns, the ordinary Vandermonde determinant gives

```text
det P_S
 = (+/-) product_{i<j in S}(tau_j-tau_i)
         / product_{i in S}D_i.
```

Every factor is nonzero.  Hence every `h`-subset is a basis and `rank P=h`.
This is an exact characteristic-zero theorem, stronger than three-prime rank
discovery.  There is no left-kernel functional and no cokernel in the raw
branch-value model.

If `c_ij=ord_t(tau_i-tau_j)`, then

```text
val det P_S
 = sum_{pairs in S} c_ij - sum_{i in S,j!=i} c_ij
 = -sum_{pairs in S}c_ij - sum_{i in S,j notin S}c_ij
 = -T + sum_{pairs in S^c}c_ij,
```

where `T=sum_{i<j}c_ij`.  Thus tropical minimization is exactly the problem of
choosing the omitted `n-h=m+1` roots with minimum internal contact sum.  It
requires all non-proper contacts.

### 5.1 The proper roots alone already span every homogeneous DEG row

There are `3k` proper roots, and

```text
3k-h = [9(5L-1)-(28L-4)]/4 = (17L-5)/4 > 0.
```

Any `h` of those distinct roots give a nonzero minor.  Therefore the proper
submatrix has full row rank, before any non-proper coordinate is added.

| `L` | raw proper unknowns `3k` | homogeneous equations `h` | exact rank | kernel | cokernel | raw non-proper Schur increment |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 54 | 34 | 34 | 20 | 0 | 0 |
| 13 | 144 | 90 | 90 | 54 | 0 | 0 |
| 21 | 234 | 146 | 146 | 88 | 0 | 0 |
| 29 | 324 | 202 | 202 | 122 | 0 | 0 |

For the full `n`-column matrix the same rank holds and its kernel has dimension
`n-h=m+1`, exactly the number of coefficients of a degree-`m` interpolant.
This is not a Keller solution: the actual `H_i` are primitives tied together
by Galois descent and root/tail coefficients, not freely assignable branch
values.

The implementation also formed an explicit rational confluent-Vandermonde
pivot, selecting two jets from `h-k=(13L-1)/4` proper discs and one jet from
the remaining `2k-h=(L-1)/2` discs.  Its determinant factors as

```text
product_{i<j}(j-i)^(a_i a_j) != 0,
```

and the exact ranks and pivot nonvanishing agree modulo `1009,1013,1019`.
The determinant factorization, rather than modular agreement, is the
characteristic-zero certificate.

### 5.2 Minimum-weight bases inside the proper submatrix

D1-PIN and the displayed tree give, for every proper root,

```text
ord_t D_i
 =2 delta_1 +(15L-3)delta_2-6L
 =-5/6.
```

Within one bottom disc pair contacts are `delta_1`; between distinct discs in
the `(10)` orbit they are `delta_2`.  Because `delta_1>delta_2` and
`k<h<2k`, a minimum proper-only basis spreads its `h` roots as evenly as
possible: two roots in

```text
h-k=(13L-1)/4
```

discs and one root in

```text
2k-h=(L-1)/2
```

discs.  No disc is empty or tripled.  Every such basis has valuation

```text
w_prop(L)
 = C(h,2) delta_2 +(h-k)(delta_1-delta_2)+5h/6
 = [2352L^3-249L^2-46L+7]/[48(5L-1)].
```

| `L` | doubled discs | single discs | `w_prop` | number of labelled minimum proper bases |
|---:|---:|---:|---:|---:|
| 5 | 16 | 2 | 4493/18 | 59,275,334,817 |
| 13 | 42 | 6 | 26691/16 | 978854863415157927258352871832 |
| 21 | 68 | 10 | 26047/6 | 20665578850909156348064939848892437011632754343545 |
| 29 | 94 | 14 | 893003/108 | 472508698140545962420060358319799587169842614059604644200515196154800 |

The count is `binom(k,h-k)3^k`: choose the doubled discs, then choose one of
three roots or one of three pairs in every disc.  The leading coefficient of
each minor is the nonzero product of the declared leading differences divided
by the corresponding denominator leaders.  Its *nonvanishing* is intrinsic;
its numerical value is not a function of `L`, because the outer and
non-proper leading coefficients have not been fixed.

These are minimum bases **within the proper block**.  They are not asserted to
be the minimum bases of the full matrix.  The latter comparison includes the
missing non-proper contacts in the formula above.

## 6. Conditional cubic-trace macro model and its exact Schur complement

The phrase “rigid cubic star” admits a second, inequivalent linearization:
suppose, as an additional hypothesis, that the trace of each three-root slot
leaves exactly one free macro coordinate.  Then the page has `K=7L` macro
nodes: `k` proper slots and `q_np=K-k` non-proper slots.  This collapse and its
sharing are **not** supplied by the charge, so the whole section is typed
`CONDITIONAL-MACRO / PROVED-HERE algebra`.

Let distinct macro nodes be `a_1,...,a_K`, put

```text
Q(X)=product_i(X-a_i),
B_{r i}=a_i^r/Q'(a_i),       0<=r<=K-2.
```

The same determinant theorem gives `rank B=K-1`.  The proper submatrix has
rank `k`, so its cokernel dimension is

```text
(K-1)-k=(13L-1)/4.
```

| `L` | equations | proper macro unknowns/rank | proper cokernel | non-proper macro columns | Schur rank | combined rank/cokernel |
|---:|---:|---:|---:|---:|---:|---:|
| 5 | 34 | 18 / 18 | 16 | 17 | 16 | 34 / 0 |
| 13 | 90 | 48 / 48 | 42 | 43 | 42 | 90 / 0 |
| 21 | 146 | 78 / 78 | 68 | 69 | 68 | 146 / 0 |
| 29 | 202 | 108 / 108 | 94 | 95 | 94 | 202 / 0 |

The three-prime computations at `211,223,227` give these ranks identically;
the following formula proves them over characteristic zero.

This canonical `K`-node audit is implemented independently in
`independent_mds_audit.py`.  It is not the wrapper certificate's different
`rigid_star_collapsed_surrogate`, which uses one channel for each residual
leaf plus one top-minor aggregate (22, 52, 82, 112 non-proper columns).  The
two models happen to have the same Schur *increment* in these four cases; that
numerical agreement does not identify their domains.

Partition the nodes into proper `P` and non-proper `N`, with `|N|=q_np`, and
write `Q=Q_PQ_N`.  A row functional on `B_P` is represented by a polynomial
of degree at most `K-2`; it kills every proper column precisely when it has
the form

```text
Lambda(X)=Q_P(X) psi(X),       deg psi<=q_np-2.
```

Applying the basis `psi=1,X,...,X^(q_np-2)` to a non-proper column `b` and
cancelling `Q_P(b)` transforms the Schur block, by a unit lower-triangular row
operation, into

```text
S_{s,b}=b^s/Q_N'(b),          0<=s<=q_np-2.
```

This is the canonical `(q_np-1) x q_np` parity matrix.  Its rank is
`q_np-1`, its cokernel is zero, and its one-dimensional right kernel is the
common additive constant.  Hence the growing proper defect is repaired
exactly.

For the full macro matrix, if

```text
Delta=product_{p<q}(a_q-a_p),
```

then deleting column `j` gives

```text
det B_hat(j)=(-1)^[binom(K-1,2)+j-1]/Delta.
```

All `K` bases have the same valuation `-val(Delta)`.  The Schur leave-one-out
minors are analogously `+/-1/Delta_N`.  Their leading coefficients still
depend on the unspecified node leaders, so there is no closed coefficient in
`L` alone.

If the proper disc centres are normalized to one cyclotomic orbit,

```text
Q_P(X)=X^k-c^k,
```

a stable basis of proper left-kernel functionals is

```text
Lambda_s = M_{k+s}-c^k M_s,
0<=s<=K-k-2.
```

On a non-proper node `b`, the reduced functional is

```text
Lambda_s(b)=b^s/Q_N'(b).
```

This is a stable **repair interface**, not a cofinal obstruction.

## 7. Witness-only tropical computations and sensitivity

The delivered scalable driver includes a valuation-only completion so that
the determinant optimizer, count scaling, and frontier inequalities are
exercised.  It chooses all proper contacts as above, gives every
residual-major pair contact

```text
rho=delta_2+1/(6A_2),
```

and gives every top-minor pair contact either `2` or `5/2`.  Both top choices
have `ord D_i<-1`; the residual choice has `delta_2<rho<2/5` and also gives
`ord D_i<-1`.  These facts are exact valuation algebra.

Crucially, the artifact labels this a `WITNESS-ONLY valuation-tree surrogate`:
it does **not** supply residual Puiseux coefficients or a complete Galois
permutation realizing those rational contacts.  It is not fed to the frozen
emitter and is not a branch-packet attainment claim.

The exact dynamic program uses

```text
val det(P_S)=-C_all+sum_{pairs in complement(S)}contact(i,j)
```

on the laminar surrogate.  The minimum compositions change when only the
still-zero-charge top-minor contact changes:

| `L` | basis at top contact `2` `(proper,residual,top)` | weight | basis at top contact `5/2` | weight |
|---:|:---|---:|:---|---:|
| 5 | (27,0,7) | 531/4 | (24,0,10) | 26 |
| 13 | (70,0,20) | 39283/48 | (64,0,26) | 407/6 |
| 21 | (114,0,32) | 54225/26 | (104,0,42) | 329/3 |
| 29 | (158,0,44) | 424997/108 | (144,0,58) | 303/2 |

Thus even at the level of abstract valuation trees, the aggregate count and
proper orbit do not determine the requested global minimum bases or weights.
The large exact labelled-basis counts are retained in `witness-results.json`.
This sensitivity result is evidence for the information obstruction, not a
substitute full decoration.

## 8. Controls

The charged exact controls were rerun from the frozen file:

```text
globalinterp.py controls: 40 checks, 0 failures
globalinterp.py selftest: 50 checks, 0 failures
```

In particular, `(f,g)=(y,x+y^3)` and `(y,x+y^5)` recover the interpolant `y`
and satisfy DEG, POLY, and NO-RESIDUE.  The same proof works for every `k>=2`:
on `g=c_2`, `tau^k=c_2-x`,

```text
d tau/dx=-1/(k tau^(k-1))=-1/g_y(tau),
```

which equals `J/g_y` because `J[y,x+y^k]=-1`; interpolation recovers `y`.
The exponents of `1/g_y` are `-(k-1)/k-j`, `j>=0`, so none is `-1`.

For the target-independent negative control

```text
g=y^2-x^2-x,
```

the two roots give

```text
1/g_y(tau_+)= +(1/2)t + ...,
1/g_y(tau_-) =-(1/2)t + ... .
```

NO-RESIDUE therefore fails at exactly `t`-order 1, as required.

These controls pass the frozen interpolation engine, but no upstream
associated-graded-page emitter exists.  The delivered wrapper therefore
evaluates the same **scalable direct consecutive-moment projection** used in
section 5.  To avoid radicals, it evaluates the universal monic-root identity
at the exact rational nodes `1,...,k`; the displayed proof identifies that
specialization with the tame pair's moment values.  The negative residues are
the exact analytic record independently checked by the frozen control suite.
It emits, exactly,

```text
(y,x+y^3): homogeneous moments [0],       monic moment 1
(y,x+y^5): homogeneous moments [0,0,0],   monic moment 1
bad g:      EXPECTED-FAIL[NO-RESIDUE] at t^1, residues +/-1/2
```

so the raw-page regression passes.  This does not pretend to exercise the
absent full decorated-family initial-form or conditional Schur extractor;
that stronger regression is part of `OPEN[FAMILY-FIRST-PAGE-MATRIX]`.

The wrapper selftest ran 32 checks with no failure in about nine seconds and
21.3 MB maximum resident memory.  It covers the four family counts, rational
and three-prime rank certificates, both tropical witnesses, root accounting,
frontier inequalities, direct-page controls, and partial-orbit refusal.

## 9. Reading: no supported cofinal obstruction on this page

The corrected orbit result changes the proposed asymptotic experiment.  The
proper packet is no longer fixed at 12 discs/36 roots: it has

```text
k=(15L-3)/4,             3k=(45L-9)/4,
```

while the homogeneous parity block has only `7L-1` rows.  Thus raw proper
coordinates grow faster than the rows and already give a full-rank MDS minor.
There is no raw left-kernel functional whose nonzero value could obstruct the
family.

The conditional macro model goes the other way: its proper defect grows as

```text
(13L-1)/4=16,42,68,94,
```

but its exact non-proper Schur matrix is itself MDS and repairs every missing
rank.  The stable functionals `M_{k+s}-c^kM_s` are therefore repair equations,
not obstructions.

The actual differential problem lies between those two models.  Write the
associated-graded evaluation/time map schematically as

```text
gr(E_p):  gr(U_p)  -> branch H-values,
gr(E_np): gr(U_np) -> branch H-values,
P:        branch H-values -> DEG syndromes.
```

The counterexample lane needs the induced non-proper syndrome interface

```text
gr(U_np) --gr(E_np)--> F^n
         --P--> coker(P gr(E_p)).
```

Equivalently it needs the Schur map after quotienting the moment equations by
the image of the proper-star deformation map.  This is the missing datum
hidden by the phrase “rigid star.”  It must include orbit descent, the
Hamiltonian primitive equation, non-proper coefficient sharing, and allowed
polynomial support.

### 9.1 The unproved theorem target that would constitute a cofinal obstruction

There is not enough evidence to conjecture a numerical leading coefficient,
but the exact theorem target can be stated without pretending it is proved:

> **VALUATED-MDS COFINAL-OBSTRUCTION THEOREM TARGET (not conjectured here).**
> For every geometrically realized, Galois-complete decoration of the
> extended family `L=8a+5`, let `b_L` be the forced proper primitive syndrome
> on the first invariant page and let
> `T_L=P_L gr(E_{p,L} direct_sum E_{np,L})` be the actual filtered
> coefficient-to-syndrome map.  There exists a left functional `ell_L` in
> `ker(T_L^T)` with `ell_L(b_L)!=0`, and the valuation and normalized leading
> coefficient of `ell_L(b_L)` obey a closed formula in `L` stable under the
> allowed non-proper templates.

Proving this statement would kill the entire numerical ray.  The present lane
does not supply `ell_L`: the raw map has no left kernel, while the conditional
macro non-proper map is surjective.  A credible proof must use restrictions in
`gr(E)`, not another Vandermonde rank count.

Conversely, if the actual non-proper map always has rank `(13L-1)/4` on the
macro quotient, the interface above is exactly what a counterexample
construction must parameterize and lift.  Passing it at finite order is still
not polynomial attainment.

## 10. Typed OPEN register and FALLACY-v2 audit

`INHERITED-RESIDUE[FAMILY-REALISABILITY]` — the arithmetic skeleton and orbit
knapsack do not construct `f,g`, actual characteristic data, or a branch
packet.  Full geometric realisability is not promoted as a bounded OPEN in
this lane.

`OPEN[FAMILY-REALISABILITY-FIRST-DISCRIMINATOR]` — bounded proxy: the four
requested values and one page, at most 202 homogeneous rows.  Cheapest test:
complete and run the 105-leaf decoration through the direct/lift cross-check
before attempting the other three members.

`OPEN[FAMILY-FIRST-PAGE-MATRIX]` — four full decorations are absent.  Missing
finite data per member: a tree on at most 609 leaves, one permutation of those
leaves, one finite template per leaf through the guard, a finite set of
sharing classes, and a row/column filtration for at most 202 DEG rows.
Cheapest test is the 105-leaf member, followed by agreement of direct moment
and coefficient-interpolation initial forms.

`OPEN[VALUATED-MDS-INTERFACE]` — determine `gr(E_p)` and `gr(E_np)`, then
compute the induced Schur rank and forced syndrome for the same four members.
Bounded quantity: four maps with respectively 34, 90, 146 and 202 target
rows, through one page.  Cheapest test: form the 34-row `L=5` map, quotient by
the exact proper image, and test whether the 51 non-proper root channels span
the forced syndrome.  This becomes finite linear algebra once the previous
OPEN's decoration is supplied.

Guardrail audit:

- **Flag/place/series:** the `D_1` disc orbit, its three cover roots, branch
  orbits, and physical places are never identified.  `A_1` is not multiplied
  into the disc-orbit size.
- **Carrier/attainment:** the exact knapsack packet is numerical
  orbit-admissibility, not `FULL_ACTUAL_EXIT` and not geometric attainment.
- **Floor/attainment:** `u-k` is unused capacity; no omitted factor is declared
  to attain it.
- **Pole/interior:** only the reviewed D1-PIN derivative valuation is used for
  proper roots.  Witness non-proper inequalities are direct contact sums and
  are not promoted to actual places.
- **Raw remainder/ring:** the exact rank theorem is over the declared valued
  Puiseux field.  Modular matrices are diagnostics with determinant
  certificates over characteristic zero.
- **Variable/ring map:** raw leaf values, macro coordinates, and actual tame
  coefficients are three explicitly different domains.  Equal-looking names
  are not used as a map.
- **Prime/derivative:** `Q'(a_i)` denotes the ordinary derivative in the macro
  theorem only.
- **Counting:** equation count, matrix rank, cokernel, auxiliary ambient
  Jacobian rank, and ideal height are never conflated.
- **Custody:** a claimed verified orbit is reduced only after size and cycle
  closure in the wrapper; full coefficient covariance remains required for a
  full decoration.

No new exit-price assertion is made, so no `charge_basis` declaration is due.

## 11. Artifacts and reproduction

All new driver artifacts are under `box/fixedn6-drivers-20260903/`:

```text
fixedn6_driver.py              fail-closed packet preflight, scalable ranks,
                               Schur diagnostics, tropical DP, selftest
independent_mds_audit.py       independent raw/macro determinant audit
witness-decorations.json       proper-packet manifests, explicitly not full
witness-results.json           four witness-only certificates
L5-k12-partial-orbit.json      required family partial-orbit negative fixture
custody-partial-orbit.json     upstream verified-orbit failure fixture
independent_partial_orbit.json independent upstream failure fixture
README.md                      scope, formulas, and commands
```

Reproduction commands:

```text
python3 box/fixedn6-drivers-20260903/fixedn6_driver.py selftest
python3 box/fixedn6-drivers-20260903/fixedn6_driver.py validate \
  box/fixedn6-drivers-20260903/L5-k12-partial-orbit.json
python3 box/fixedn6-drivers-20260903/fixedn6_driver.py all
python3 box/fixedn6-drivers-20260903/fixedn6_driver.py controls
python3 box/fixedn6-drivers-20260903/independent_mds_audit.py
python3 /tmp/jc2-lane.CBLhSa/inputs/globalinterp.py controls
python3 /tmp/jc2-lane.CBLhSa/inputs/globalinterp.py selftest
python3 /tmp/jc2-lane.CBLhSa/inputs/globalinterp.py emit \
  box/fixedn6-drivers-20260903/custody-partial-orbit.json --rank none
```

Expected custody outcomes are exit 2 with `REFUSED[ORBIT-SIZE]` for the first
family fixture, and exit 0 with one falsely reduced verified orbit for the
upstream bug fixture.  The latter is a negative-control success because it
detects the frozen driver's missing check.

Final artifact digests:

```text
df051b71d3c6145d8a0857d3258e4e0fd078258231593ab9d2e5eeaaeba1bd11  fixedn6_driver.py
30255ff5c0dd0b8e2d46ac192a013bb8f17f47fa2682aa8cb0241f30e971952a  independent_mds_audit.py
f9fbae7d3a61a680da9eb710e5e8adb13c302be422144d62067ff2d1ef29da15  witness-results.json
8b23fd56740714acd389635d905863c90e16d7a4cb5e74d1c5cb9933f11653f8  witness-decorations.json
c0bfad20f6722be11b5d64c957dd4b7edaa44e8a30d4aa362e2bd4a1ea3b5a49  L5-k12-partial-orbit.json
1ec03ae9b426fc6b18d81f0609c95967dc7eafc7fa8bf1bd0549beefe307ab58  custody-partial-orbit.json
7a79d5fbdfd635eb0b7d4bfc7d92e7432bc76f344cde3fa86b5d3e64ac5d0ccc  independent_partial_orbit.json
058f25b292c58cb9fa5b1f776a675e54de5e28898e398ba7671630bc050d25bb  README.md
```

## 12. Final typed block

```text
PROVED-HERE / UNREVIEWED
  cap-erased numerical skeleton algebra for every L=8a+5;
  d=(21L,7L,7,1), delta=(-1,2(3L-1)/(3(5L-1)),7/12),
  A2=3(5L-1)/4, A1 in {1,2}, q=1/2, u=5L;
  (10)-only orbit size A2 and unique positive fixed-type packet;
  corrected k=A2 and N=15a+9; exact root-block counts;
  consecutive-row GRS determinant and valuation formula;
  full raw proper rank and proper-only minimum-basis pattern;
  conditional macro Schur theorem and its exact repair formula;
  upstream partial-orbit acceptance and wrapper refusal.

REFUTED
  fixed N=6 after orbit closure;
  literal printed (1)-(13) membership at n>=105;
  inference of actual-pair membership solely from a numerical skeleton;
  frozen-driver partial-orbit refusal.

NOT DETERMINED FROM THE CHARGED DATA
  a family-intrinsic first-page/tropical/Schur table.

WITNESS-ONLY
  valuation completions, their ranks, frontier checks and tropical bases;
  no Galois/polynomial realization claimed.

CONDITIONAL-MACRO
  one free coordinate per cubic slot gives growing proper defect
  16,42,68,94, exactly repaired by the non-proper Schur block.

OPEN
  FAMILY-REALISABILITY-FIRST-DISCRIMINATOR;
  FAMILY-FIRST-PAGE-MATRIX; VALUATED-MDS-INTERFACE.

READING
  The raw parity code is already MDS and supplies no obstruction.  Any
  cofinal defect must live in the filtered evaluation/time map from actual
  tame coefficients to branch primitive values.  That map, and especially
  its non-proper Schur quotient, is the counterexample lane's interface.
```

<!-- BODY-END -->
