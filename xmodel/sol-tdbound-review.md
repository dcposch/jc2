VERDICT: COINCIDENCE-RISK — `td <= m*n` is not falsified, and it has a clean exact intersection-theoretic reformulation, but the advertised `dead <-> violates` evidence is mostly forced by the off-axis census construction; the scan does not replay kill certificates, its 23 rows are formal Sigray entry data without matched GGV provenance or polynomial realizations, and it overstates corpus coverage.

# Independent adversarial review of CONJECTURE TD-BOUND

Date: 2026-08-17.  I ran the supplied gate, independently rebuilt its entry
data from the sheet equations, independently recomputed the residue-A
intersection number, and audited the current kill/status sources.  No claim
below treats a machine `PASS` as a proof of its prose label.

## 1. Bottom line

There are three different conclusions, and they should not be merged.

1. **Arithmetic replay: confirmed.**  `python3 cases/tdbound_scan.py` exits
   zero with 6/6 checks.  An independent enumeration gives exactly the same 23
   L6-surviving off-axis entries and their Sigray types.  The residue-A formal
   genome gives `I_infinity = 42330` exactly.
2. **Empirical kill correlation: not confirmed.**  The program assigns
   `DEAD` from `td` inside the scan rather than reading a kill artifact.  Only
   10 of its 23 off-axis rows are even labelled dead; 12 of the 22 violating
   rows are labelled unadjudicated.  Current repository audits further make
   the td-11 result conditional and td-13 globally open.
3. **Mathematical conjecture: still open, with a good proof coordinate.**  In
   the Sigray degree frame the proposed bound is exactly

   ```text
   sum_F a_F*b_F/nu_F <= 1,
   ```

   and also exactly a square-norm bound for the difference of the two resolved
   pencil fibers.  This is substantive: it identifies the missing lemma.  It
   is not evidence that the missing lemma is already contained in L6, N1, or
   the current budget filters.

As written, the scan still computes in the Sigray entry language.  A
concurrent new artifact, `TRANSPORT.md`, now supplies an explicit pre-Laurent
normalization theorem for the **selected genuine GGV-minimal pair**: after
determinant-one source/target rotations its sorted GGV multipliers equal its
Sigray type.  I ran `cases/transport_check.py` and audited the core
coordinate-cusp/degree-minimality argument; this materially repairs the old
blanket type objection.  It does not match any of the 23 formal entries to a
GGV chain or realize one as a polynomial pair.  Thus the directly tested
candidate remains

```text
Sigray TD-BOUND:  td <= alpha*beta
```

for a realizable Sigray-normalized Keller configuration.  `TRANSPORT.md`
makes this the same numerical bound for the selected pre-Laurent GGV pair if
such a counterexample exists; the scan itself supplies no GGV provenance for
its 23 abstract rows.

## 2. Independent replay of the 23 entries

I did not use `book_offaxis.census()` to generate the comparison side.  I
rebuilt the leaf menu from Statement 5.2 and Propositions 5.6--5.8:

```text
(D,D_g) = a(alpha,beta),       (P,P_g) = b(alpha,beta),
Lambda = alpha*beta*a*b/nu,    td = sum Lambda,
```

with the two `nu` divisibility/congruence alternatives, then enumerated
partitions of `td`, required one `b >= 2`, and finally imposed

```text
L6: gcd(a(alpha+beta),nu)=1  <=>  gcd(a,nu)=1.
```

This independently gives 27 raw off-axis multisets and kills exactly four at
L6, leaving 23.  The four L6 removals are all violating type-`(2,3)` rows, so
L6 did not manufacture the single passing row.  Comparing the independent
objects with `cases/book_offaxis.py` was exact, including pole order.

Here is the full type audit.  A pole is written `(Lambda,a,b,nu)` and `r` is
the number of poles; it is not a GGV parameter.

| # | td | r | independently inferred Sigray type | pole multiset | `td <= alpha*beta` |
|---:|---:|---:|---|---|---|
| 1 | 7 | 2 | `(2,3)` | `(3,1,1,2) + (4,1,2,3)` | no |
| 2 | 8 | 2 | `(2,3)` | `2 x (4,1,2,3)` | no |
| 3 | 10 | 2 | `(2,3)` | `(4,1,2,3) + (6,1,1,1)` | no |
| 4 | 10 | 3 | `(2,3)` | `2 x (3,1,1,2) + (4,1,2,3)` | no |
| 5 | 11 | 2 | `(2,3)` | `(3,1,1,2) + (8,2,2,3)` | no |
| 6 | 11 | 2 | `(2,5)` | `(5,1,1,2) + (6,1,3,5)` | no |
| 7 | 11 | 3 | `(2,3)` | `(3,1,1,2) + 2 x (4,1,2,3)` | no |
| 8 | 12 | 2 | `(2,3)` | `(3,1,1,2) + (9,1,3,2)` | no |
| 9 | 12 | 2 | `(2,3)` | `(4,1,2,3) + (8,2,2,3)` | no |
| 10 | 12 | 2 | `(2,5)` | `2 x (6,1,3,5)` | no |
| 11 | 12 | 2 | `(3,5)` | `2 x (6,1,2,5)` | **yes** |
| 12 | 12 | 3 | `(2,3)` | `3 x (4,1,2,3)` | no |
| 13 | 13 | 2 | `(2,3)` | `(3,1,1,2) + (10,1,5,3)` | no |
| 14 | 13 | 2 | `(2,3)` | `(4,1,2,3) + (9,1,3,2)` | no |
| 15 | 13 | 2 | `(2,3)` | `(4,1,2,3) + (9,3,1,2)` | no |
| 16 | 13 | 2 | `(3,4)` | `(4,1,1,3) + (9,1,3,4)` | no |
| 17 | 13 | 3 | `(2,3)` | `(3,1,1,2) + (4,1,2,3) + (6,1,1,1)` | no |
| 18 | 13 | 4 | `(2,3)` | `3 x (3,1,1,2) + (4,1,2,3)` | no |
| 19 | 14 | 2 | `(2,3)` | `(4,1,2,3) + (10,1,5,3)` | no |
| 20 | 14 | 2 | `(2,3)` | `(6,1,1,1) + (8,2,2,3)` | no |
| 21 | 14 | 3 | `(2,3)` | `2 x (3,1,1,2) + (8,2,2,3)` | no |
| 22 | 14 | 3 | `(2,3)` | `2 x (4,1,2,3) + (6,1,1,1)` | no |
| 23 | 14 | 4 | `(2,3)` | `2 x (3,1,1,2) + 2 x (4,1,2,3)` | no |

Counts are `(2,3): 19`, `(2,5): 2`, `(3,4): 1`, `(3,5): 1`; by
rung they are `1,1,2,3,5,6,5` at td `7,8,10,11,12,13,14`.  For
every stored pole multiset, the equation
`Lambda*nu = a*b*alpha*beta` together with the A/B congruence menu uniquely
recovers the displayed type in the admissible menu.  Thus the 22/23 arithmetic
pattern is not caused by a mistyped row.

Relevant implementation/specification locations are
`SHEET6-TDUNIFORM.md:38-58`, `cases/book_enum.py:104-124`, and
`cases/book_offaxis.py:35-55`.

## 3. Residue-A: independent `I_infinity` calculation

The rectangular corners in `SHEET6-TEMPLATE.md:61-64` give

```text
(k_f,l_f)=(126,42),  deg f=168;
(k_g,l_g)=(189,63),  deg g=252;
B=gcd(168,252)=84,   (alpha,beta)=(2,3).
```

For generic levels, the two projective points at infinity contribute as
follows.

```text
Y=[1:0:0]:  I_Y = 126*252 + 84*(-1/14)
                  = 31752 - 6 = 31746.

X=[0:1:0]:  I_X = 42*252 = 10584.

I_infinity = I_Y + I_X = 42330.
td         = 168*252 - 42330 = 6.
```

The `-1/14` pole order is independently recovered from the product of the
recorded branch contacts (`cases/classical_tests.py:100-107`); the complete
calculation is encoded at `cases/classical_tests.py:180-189` and printed in
`SHEET6-CLASSICAL.md:278-285`.  Numerically,

```text
I_infinity/(deg f*deg g) = 42330/42336
                         = 7055/7056
                         = 99.9858277...%,
I_infinity = (B^2-1)*alpha*beta = (84^2-1)*6.
```

This is an exact consistency check **conditional on the formal Puiseux/Newton
genome**.  It is not an observation from a realized polynomial Keller map.
`SHEET6-TEMPLATE.md:4-12` calls the object `FORMAL-CANDIDATE`, and
`BOOK-ENUM.md:149-154` explicitly leaves polynomial realizability untracked.
Consequently `TDBOUND.md` should not call residue-A “the one realized record.”

## 4. What the 6/6 scan actually proves

The six green checks are real program outcomes, but several descriptions are
stronger than their predicates.

- At `cases/tdbound_scan.py:60-63`, status is assigned solely from `td`:
  td 7, 11, and 13 are labelled `DEAD`; no tower/book certificate is loaded.
- T1 checks only `len(ROWS)==24` and `len(off)==23`.  The displayed 17 and 411
  counts are prose constants, not replayed artifacts.
- T2 checks only that 22 arithmetic rows violate the inequality and residue-A
  is at equality.  It does not test a single kill status.
- T3 checks the singleton arithmetic row and the status string that this same
  file assigned.
- T4 compares a set of `(td,alpha,beta)` triples, thereby deduplicating
  distinct entries.  Its prose calls td-8 killed although the table calls it
  unadjudicated.
- T5 compares a hard-coded `42330` and the deliberately off-axis type set; it
  does not recompute either local intersection contribution.
- T6 filters the status strings created at lines 60--63.  It is circular as a
  corpus-provenance check.

Therefore 6/6 means “this hand-built table is internally arithmetically
consistent,” not “the corpus adjudications were independently replayed.”

### The claimed kill equivalence fails in both directions

Within the scan's own 23 rows:

```text
violates bound:                         22
labelled DEAD by the scan:              10  (td7:1, td11:3, td13:6)
violating but labelled UNADJUDICATED:   12
```

Thus even the hand labels establish at most `labelled-dead => violates`, not
`dead <-> violates`.  The current mathematical status is weaker still:

- The 17 td-7 cells all inherit one entry type.  They are dependent cells,
  not 17 independent tests of the inequality.
- `cases/td11_census.py` does run 24/24 and stamps all 411 quotient rows, but
  its header calls the object an **instrument-uniform death quotient**, not a
  literal extension census (`:13-40`).  Its certificate is explicitly
  conditional on two remaining possibly-live classes, FC1-R and FC3
  (`:1146-1169`).  The 411 rows inherit only three entry types.
- The current corrected scope files td-11 and td-13 as `UNKNOWN`
  (`xmodel/sol-td11-13-scope.md:21-24`).  Five td-13 entries have only an
  entry-local max-X empty window, explicitly “not yet a global tower theorem”
  (`:382-418`), while 13-2b has a genuinely nonempty local window.
  `REDUCTION.md:1039-1043` likewise says that full td-11/13 exclusion is
  false in current campaign status.

The tower work may eventually kill these rows.  It cannot currently be used
as independent evidence that all 22 violators were killed.

## 5. Why 21 of the 22 violations are selected in advance

Let `r` be the number of pole vertices.  The promoted leaf identities give

```text
td = sum_i Lambda_i,       Lambda_i >= beta.
```

Moreover MP4 says `Lambda_i=beta` forces `b_i=1`.  Hence:

- if `r > alpha`, then `td >= r*beta > alpha*beta`;
- if `r = alpha`, then `td >= alpha*beta`, and equality would force every
  pole to be beta-minimal and hence every `b_i=1`;
- therefore an **off-axis** row (some `b_i>=2`) with `r>=alpha` satisfies
  `td > alpha*beta` before L6, a budget, or a tower is consulted.

This applies to 21 of the 23 rows: all 19 type-`(2,3)` rows and both
type-`(2,5)` rows have `alpha=2` and `r>=2`.  It explains 21 of the 22
violations by construction.  The effective nonautomatic sample has only two
rows:

```text
td13, type (3,4), r=2, Lambda=(4,9):  excess 5 > capacity 4  -> violates;
td12, type (3,5), r=2, Lambda=(6,6):  excess 2 <= capacity 5 -> holds.
```

More generally, put `e_i=Lambda_i-beta >= 0`.  Then

```text
td <= alpha*beta
    <=> r <= alpha and sum_i e_i <= (alpha-r)*beta
    <=> sum_i a_i*b_i/nu_i <= 1.
```

This is useful as a proof reduction, but it makes the 22/23 frequency weak
evidence.  The off-axis selector has preloaded almost the whole answer.

The other entry filters do not secretly prove the remaining inequality:

- L6/N1 is only `gcd(a,nu)=1` here.
- Fixed-type N1-valid arithmetic progressions have unbounded `td`
  (`SHEET6-TDUNIFORM.md:99-122`).
- The printed shared budget has right side `td-1-psi`, which loosens as `td`
  grows, and the pure `M=1` forest is budget-transparent
  (`SHEET6-MULTIPOLE.md:61-64`).

So this is selection bias, not yet a theorem disguised as L6 or the budget.

### “Entire filed corpus” is also too broad

Repeating the same `book_enum.entries` enumeration through L6 **before** the
off-axis filter gives 43 entries: 23 off-axis plus 20 all-`b=1` entries.  The
scan manually reinstates residue-A but omits the other 19 on-axis entries.
Among all 20 all-`b=1` entries, 12 satisfy the bound and 8 violate it; all 20
have at least one inline `BOOK-ENUM` survivor.  Their types include

```text
(2,3), (2,5), (2,7), (3,4), (3,7), (4,5), (5,6), (6,7),
```

so the complete L6 entry set has nine types after adding off-axis `(3,5)` and
has maximum `alpha*beta=42`, not 15.  `BOOK-ENUM.md:60-81` records the relevant
on-axis panels, while `cases/book_offaxis.py:49-51` deliberately drops them.

It is legitimate to study “the off-axis census plus residue-A,” but that scope
must be named.  It does not support “single below-bound filed entry” or “caps
the entire filed ladder at 15.”

## 6. Normalization transport update and the remaining notation break

### GGV `(m,n)` now transports to Sigray `(alpha,beta)` for the selected pair

The scan reads `(al,be)` from the Sigray entry generator and stores them in
fields called `m,n` (`cases/tdbound_scan.py:55-66`).  The older promoted
reduction correctly recorded that no dictionary had then been proved
(`REDUCTION.md:315-336`, `:813-824`).  During this review, `TRANSPORT.md` was
added with a stronger pre-Laurent theorem.  Its argument is:

1. a coordinate polynomial cannot have weighted initial form divisible by
   the coprime cusp binomial `d^r U^s-c^s V^r` (Theorem 1.1, via the
   Hamiltonian locally nilpotent derivation);
2. therefore no target coordinate can cancel the common cusp peak of the two
   rectangular components, giving an exact target-degree formula and
   orbitwise lexicographic minimality (Theorem 2.1); and
3. determinant-one target sorting and the source rotation `(x,y)->(y,-x)`
   carry the genuine selected GGV pair to a Sigray-normalized representative
   of type

   ```text
   (alpha,beta)=(min(m,n),max(m,n)),
   ```

   with the same `td` and an exactly recoverable pre-Laurent GGV ledger
   (Theorem 3.1 and Section 4).

I independently checked the algebraic steps above and ran
`python3 cases/transport_check.py`; its actual `(8,28)` GGV fixture transports
from degree pair `(108,72)` to Sigray degree pair `(72,108)` and type `(2,3)`.
This removes the blanket claim that the numerical types are unrelated for the
selected polynomial counterexample.

It does **not** give GGV provenance to the 23 rows in this review.  The
transport checker has one actual GGV fixture; residue-A and td-7 are explicitly
independent Sigray frame-schema controls, not transports of that fixture.  No
off-axis entry is matched to a GGV admissible chain, and polynomial
realizability remains untracked.  `TRANSPORT.md` also disclaims a
corner-to-tree functor.  The right conclusion is therefore:

- for a genuine selected GGV counterexample, the proposed law (i) and its
  Sigray version use the same sorted numerical type;
- the 23-row scan remains evidence only about abstract Sigray entry data, not
  23 realized or GGV-certified configurations; and
- the advertised finite-ladder payoff still fails: the GGV enumeration is
  complete only under an input degree bound, not an all-degree finite catalog
  (`REDUCTION.md:225-244`, `:690-697`; `TRANSPORT.md` Section 6).

### Sigray `b_i=M_i` is not GGV `q_h`

Sigray MP4 defines the pole multiplier by

```text
(deg p_i,deg p_{g,i}) = b_i(alpha,beta),   M_i=b_i
```

(`SHEET6-TDUNIFORM.md:68-74`, `SHEET6-MULTIPOLE.md:48-50`).  GGV instead
defines

```text
q_h = v_{rho_h,sigma_h}(A_h)
      / gcd(rho_h+sigma_h, v_{rho_h,sigma_h}(A_h))
```

(`SECTION4-AUTOMATION.md:23-27`).  No theorem identifies them.  The scan is
internally inconsistent as well: residue-A's actual Sigray pole multipliers
are `(1,1)`, but the scan inserts `(84,)`; off-axis rows use their actual
`b_i` values.  Accordingly law (ii), `td | mn*product(q_h)`, has not been
replayed and should receive no evidentiary weight from this table.

## 7. Proof path: exact infinity accounting

The following is the first real lemma I would promote.  It is independent of
the entry census and makes the missing geometry explicit.

### Resolved-pencil mismatch-energy lemma

Let `f,g in C[x,y]` define a generically finite map, let

```text
d=deg f=B*m,   e=deg g=B*n,   gcd(m,n)=1,
```

and resolve simultaneously the projective pencils
`<F_d,Z^d>` and `<G_e,Z^e>` by point blowups.  For every proper or
infinitely-near base center `p`, let `r_p` and `s_p` be the multiplicities of
a general member of the two pencils, putting zero when `p` belongs only to the
other pencil.  Then

```text
I_infinity = sum_p r_p*s_p = d*e-td,

td/(m*n) = (1/2) * sum_p (r_p/m - s_p/n)^2.       (ME)
```

**Proof.**  In the orthogonal total-transform exceptional basis on the common
resolution, the two general fibers have classes

```text
C = d*H - sum_p r_p*E_p^*,
D = e*H - sum_p s_p*E_p^*.
```

Each is a fiber of a morphism to `P^1`, so `C^2=D^2=0`; hence
`sum r_p^2=d^2` and `sum s_p^2=e^2`.  A finite union of boundary curves cannot
dominate `P^1 x P^1`, so for generic levels the resolved fibers meet only in
the affine plane and `C.D=td`.  Therefore `sum r_p*s_p=d*e-td`.  Divide by
`m*n` and expand the square:

```text
sum (r_p/m-s_p/n)^2
 = B^2+B^2-2(B^2-td/(m*n))
 = 2*td/(m*n).
```

No Keller hypothesis is needed for this numerical identity beyond generic
finiteness/separability; the Keller condition makes the generic affine
intersections reduced.

Equivalently, the normalized difference divisor

```text
Delta = C/m - D/n
```

has no `H` part and satisfies

```text
Delta^2 = -2*td/(m*n).
```

Thus TD-BOUND is exactly `Delta^2 >= -2`, or equivalently raw normalized
mismatch energy at most 2.  The exceptional lattice alone does not imply this;
the Jacobian condition must constrain which divergence vectors occur.

### Combination with the Sigray pole identity

In the Sigray degree frame set `(m,n)=(alpha,beta)`.  Proposition 5.8 gives
`td=sum_F Lambda_F` and `Lambda_F=alpha*beta*a_F*b_F/nu_F`.  Combining it
with (ME) gives the exact scalar identity

```text
td/(alpha*beta)
  = sum_F a_F*b_F/nu_F
  = (1/2) * sum_p (r_p/alpha-s_p/beta)^2,

I_infinity
  = alpha*beta * (B^2 - sum_F a_F*b_F/nu_F).
```

This does **not** identify individual pole summands with individual resolution
centers.  For the selected pre-Laurent GGV pair, `TRANSPORT.md` now makes the
global type/degree substitution theorem-level; the unresolved transport is
the local corner/edge-to-tree/base-cluster identification.
Residue-A has two `(a,b,nu)=(1,1,2)` poles, mass `1`, and raw mismatch energy
`2`; the td-12 `(3,5)` row has two `(1,2,5)` poles, mass `4/5`, and raw
mismatch energy `8/5`.

### What Corollary 7.4 contributes, and what it does not

Under Corollary 7.4's actual direction and Laurent-frame hypotheses, its proof
simultaneously produces common-power leading forms of the shape

```text
ell(P)=lambda*R_tilde^(q*m),
ell(Q)=mu*R_tilde^(q*n).
```

If a separate weighted/Laurent-to-projective transport theorem shows that
such an edge is the lowest local initial pair at a resolved base center, after
removing exceptional monomials, and `ord(R_tilde)=h`, then

```text
r_p=q*m*h,   s_p=q*n*h,
```

so `r_p/m=s_p/n`: that center contributes zero mismatch energy and a large
proportional term to `I_infinity`.  The proof problem is thereby localized to
the **divergence centers**, where the two normalized multiplicity clusters
stop agreeing.

Power structure alone is not enough.  For example, local expressions
`u^(qm)+x` and `u^(qn)+2x` have the advertised boundary initials while their
ordinary multiplicities and local intersection are controlled by the lower
`x` terms.  One must transport the weighted blowup chain, exceptional
monomials, eligible direction interval, and proximity relations.  The new
pre-Laurent normalization theorem carries leading faces, valuations, and the
GGV `(p_h,q_h)` tag through the linear rotations, so that gross coordinate
gap is repaired.  It does not convert a transported GGV edge into an ordinary
projective base center or a Sigray pole decoration; replacing GGV `q_h` by
Sigray `b_i` still does not do this.

A useful rigorous sufficient criterion is now immediate: if distinct resolved
centers carry nonnegative integers `h_p` with

```text
r_p >= alpha*h_p,   s_p >= beta*h_p,
sum_p h_p^2 >= B^2-1,
```

then `I_infinity >= alpha*beta*(B^2-1)` and TD-BOUND follows.  Corollary 7.4
could supply `h_p=q_p*ord(R_p)` at the centers for which the missing transport
is proved.  This separates the real obligations: proportional multiplicity
transport, cluster-energy/proximity accounting without double counting, and
coverage of enough centers.

### First new realizability lemma worth attacking

The census analysis suggests a strictly weaker first target than full
TD-BOUND:

> **Maximal-pole rigidity.**  Every realizable Sigray type-`(alpha,beta)`
> Keller configuration has at most `alpha` pole vertices.  If it has exactly
> `alpha`, every pole is beta-minimal, necessarily
> `(Lambda,a,b,nu)=(beta,1,1,alpha)`.

This lemma would eliminate the 21 construction-forced off-axis rows without
assuming the full excess bound.  The remaining step for `r<alpha` is

```text
sum_i (Lambda_i-beta) <= (alpha-r)*beta.
```

In resolution language the natural target is: after deleting the
Corollary-7.4-certified proportional centers, the Keller Jacobian divisor and
proximity inequalities force the remaining normalized difference divisor to
have square at least `-2`.  That is the first point at which `J(f,g)=1`, rather
than census arithmetic, must do real work.

## 8. Size of the td-12 type-`(3,5)` book

The entry is

```text
td=12, r=2, (alpha,beta)=(3,5),
poles: 2 x (Lambda,a,b,nu)=(6,1,2,5),
M=b=2,
w0=a*(b*(alpha+beta)-1)/(b*nu)=3/2,
L6: gcd(8,5)=1.
```

There is one labelled two-leaf hierarchy.  The exact entry-level
`merge_cells([2,2])` skeleton has 14 cells:

| ordered arrivals `(mu_1,mu_2)` | cells after emitted-`M` and root/interior choices |
|---|---:|
| `(1,1)` | 3 |
| `(1,2)` | 3 |
| `(2,1)` | 3 |
| `(2,2)` | 5 |
| **total** | **14** |

Equivalently these are 9 root and 5 interior cells, or 9 MP6-anatomy and 5
all-`mu>=2` mixed cells.  Swapping the two identical poles leaves 11 skeleton
orbits.  The current `stage_rp_census` correctly reports

```text
DEAD 0 / ALIVE 0 / OPEN 14, capped=True.
```

So “no book was ever built” is too literal: the entry and 14-cell structural
skeleton exist.  What does not exist is a completeness-certified priced
chain/tower/realization book.

The full book is much larger than 14.  Its nominal shared chain/merge budget
is `td-2=10` when the terminal `psi` is minimal.  The current
`close_p` implementation hard-caps every request at budget 5
(`cases/book_offaxis.py:598-609`); from the pole seed `(w,M)=(3/2,2)` it returns
69 states, 25 distinct `w` values, maximum `M=25`, and marks the result capped.
An independent cap-lift sizing run reached 162 one-chain states, 48 `w` values,
and maximum `M=49` already at budget 6 (about 27 seconds); budget 7 did not
finish within two minutes.  At budget 6 alone, the naive two-chain product is
26,244 ordered state pairs, or 13,203 modulo swapping, before imposing the
shared cost, arrival, merge, trunk, and tower constraints.  These are sizing
figures, not a claimed final cardinality.

A complete build requires:

1. cap-free closure of both `(3/2,2)` arrival languages through shared cost
   10;
2. pairing under the one global St 9.4 budget and the identical-pole symmetry;
3. choosing arrivals with `mu | M_current` at the actual post-jump state, not
   merely `mu | b_entry`;
4. root/interior and zero/nonzero merge arrangements with merge pricing;
5. trunk closure and the terminal `psi` charge; and
6. N1, E5/H5a, T1/ODE, tower composition, and finally polynomial
   realizability.

The honest size today is therefore: **14 exact skeleton cells; full priced
cardinality unknown and beyond the current budget-5 engine**.  This row is a
good next target precisely because it is the only nonautomatic discriminator
inside the selected 23-row off-axis sample.

## 9. Final assessment

I do not have a counterexample to the inequality, so `REFUTED` would be too
strong.  `SUPPORTED` would also be too strong: there is no realized positive
example, the formal scan rows have no entrywise GGV provenance, the kill
equivalence is false, and 21/22 violations are forced by how the off-axis
sample is selected.  The new normalization theorem makes the GGV and Sigray
type numbers agree on the selected genuine pair, but does not change those
data-quality conclusions.

What survives the adversarial review is worthwhile:

- the complete 23-entry arithmetic and residue-A `42330` calculation are
  correct at their stated formal tiers;
- the conjecture becomes the exact pole-mass inequality
  `sum a*b/nu <= 1` in the Sigray frame;
- the resolved-pencil lemma turns it into the geometric bound
  `Delta^2 >= -2`; and
- Corollary 7.4 plausibly removes proportional zero-mismatch centers, leaving
  a sharply stated Jacobian/proximity problem at divergence centers.

That is a credible proof program.  It is not yet an empirical law established
by the current census.
