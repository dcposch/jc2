# Bounded-`y` degree six chain audit

**Verdict: `CONDITIONAL COMPLETE COVERAGE; TWO UNREVIEWED LEAVES`.**

- Snapshot: `2026-08-24T11:38:17Z`
- Charged bank: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`
- Field statement audited: characteristic-zero Keller pairs with both actual
  `y`-degrees at most six
- Reviewed theorem currently available: every pair with both degrees at most
  five is an automorphism
- Confirmed sextic reduction skeleton: yes
- Unreviewed fundamental leaves: `(4,6)` and `(5,6)` only
- Generic support search, coefficient enumeration, AWS: none
- AS109 lift or JC2 inference: none

## 1. Answer

Yes.  If the two newest frozen exclusions

```text
xmodel/as109-sextic-46-local-normalization-gate-20260824.md
xmodel/as109-sextic-56-exclusion-20260824.md
```

are each confirmed at their exact stated scopes, then every
characteristic-zero Keller pair whose two actual `y`-degrees are at most six
is a polynomial automorphism.

There is no missing degree pair.  The only subtle bucket is `(6,6)`: a
constant target `GL_2` operation lowers one coordinate but leaves the other
at degree six, so it produces `(r,6)` for some `r<=5`.  It therefore depends
on the same two leaves `(4,6)` and `(5,6)`; it is not independently closed by
the quintic theorem.

At the current trust state the degree-at-most-six theorem is **not yet
promoted**.  The `(4,6)` local-normalization closure and the `(5,6)` weighted
exclusion have exact passing replays but no hostile different-model review.

## 2. Trust-state matrix

All named producers and hostile reviews below were read for this audit.

| Layer | Producer SHA-256 | Hostile review SHA-256 | Current state | Logical use here |
|---|---|---|---|---|
| quadratic `<=2` | `10ee0b91d4be7ced8d6c053ba66e6d677d7c4cc83af89fc481d215f145e38ea1` | `4ee7793d352d130d79b5efb1f555c8a241ed5ed59335426238505da5dcae48f2` | `CONFIRMED` | historical base; subsumed by quintic theorem |
| cubic `<=3` | `198f0b2ff39f91a7815b9be15f7fc3c3afdd00c00b1c4c0ada6b9f6438d62820` | `2fdb8ae2beffb766b38d8e7de4bdff353bc354c4dba84d026225f88376f95cef` | `CONFIRMED` | closes genuine `(2,3)` |
| quartic `<=4` | `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276` | `3f9e763c07aa019a766b267774f92df857aadd94750cb8c3c9431671318d930e` | `CONFIRMED` | closes genuine `(3,4)`; input to quintic |
| quintic `<=5` | `598cdf3799d4abf40ec761f1fd2b0a5a6457ee2b578371bd864c296259d2a978` | `ab5ce55c1d71628e16800bc9ff9985da9f4ae90fe521849fa2060e97ff552e0e` | `CONFIRMED` | reviewed base for every pair of maximum degree `<=5` |
| sextic pair sweep / normal forms | `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4` | `5bf1a677a59975defb33a58da74d7c7c1381535d84f91e7f1584d21624a385ff` | `CONFIRMED` | proves that only `(4,6),(5,6)` are fundamental sextic leaves |
| `(4,6)` discriminator | `b2f6a16eb8399d4de408c41070c666000b324409a5332fa211eff011b5624552` | `4f2c8b6cd1a165ed73dedb0a3fc92256199927961a6c5126afc6689408106c59` | `CONFIRMED` as survivor normal form | exact input to newest `(4,6)` closure |
| `(4,6)` local closure | `587a142a09ac70805264f56ed408545fa6dd0b771d4712459fad6eddcf9902ac` | none landed | **PROVISIONAL** | would make genuine `(4,6)` empty |
| `(5,6)` weighted exclusion | `31420c0cd667640f340f4d127f185edd4515aac7df3733560e6d1fda5ec6c7a4` | none landed | **PROVISIONAL** | would make genuine `(5,6)` empty |

The `(4,6)` closure froze while its parent review was still being treated
conservatively.  That parent review has now landed `CONFIRMED`; its normal
form dependency is therefore discharged.  This does not review the new
local Puiseux argument itself.

The sextic-preflight review found the additional identity

```text
dI_1=omega-(2A/5)dI_3.
```

The `(5,6)` exclusion correctly starts from this reviewed successor input.
Thus the preflight's headline statement that no third integral followed was
a completeness overstatement, not a blocker inherited by the successor.

## 3. Universal target reductions

Let the actual degrees be ordered `0<=m<=n`, with leading coefficients
`a_m(x),b_n(x)`.  The top Jacobian row is

```text
n a_m' b_n-m a_m b_n'=0.                              (3.1)
```

The following reductions are exact over a characteristic-zero field.

1. If `m=n>0`, (3.1) makes `a_m/b_n` constant.  A constant target `GL_2`
   operation strictly lowers one coordinate's actual degree.
2. If `0<m<n` and `m` divides `n`, unique factorization gives
   `b_n=k a_m^(n/m)`.  The polynomial target shear
   `g -> g-k f^(n/m)` strictly lowers the maximum degree.
3. If `m=0`, then `J=a_0'(x)g_y`.  A nonzero constant forces `n=1`, and
   the pair is triangular; `(0,0)` and `(0,n>=2)` are impossible.
4. If `m=1`, the affine-in-`y` argument successively removes all higher
   powers of the affine coordinate and gives a triangular automorphism.

All target operations are polynomial automorphisms of the target, so they
preserve both the Keller property and whether the original pair is an
automorphism.  The reductions terminate by lexicographic induction on
`(max(m,n),m+n)`.

## 4. Every unordered actual degree pair

Swapping the two target coordinates handles the opposite ordering.  The 28
unordered pairs are:

| Pair | Exact route | Trust/result |
|---|---|---|
| `(0,0)` | Jacobian is zero | impossible |
| `(0,1)` | degree-zero/affine triangular form | automorphism |
| `(1,1)` | equal-degree `GL_2 -> (0,1)` | automorphism |
| `(0,2)` | `a_0'g_y` constant forces degree one | impossible |
| `(1,2)` | affine-in-`y` reduction | automorphism |
| `(2,2)` | equal-degree `GL_2 -> (r,2)`, `r<2` | automorphism |
| `(0,3)` | degree-zero obstruction | impossible |
| `(1,3)` | affine-in-`y` reduction | automorphism |
| `(2,3)` | genuine coprime cusp | empty, cubic `CONFIRMED` |
| `(3,3)` | equal-degree `GL_2 -> (r,3)`, `r<3` | reduces to prior rows |
| `(0,4)` | degree-zero obstruction | impossible |
| `(1,4)` | affine-in-`y` reduction | automorphism |
| `(2,4)` | shear `g-kf^2` | maximum degree drops below four |
| `(3,4)` | genuine coprime pattern | empty, quartic `CONFIRMED` |
| `(4,4)` | equal-degree `GL_2 -> (r,4)`, `r<4` | reduces to prior rows |
| `(0,5)` | degree-zero obstruction | impossible |
| `(1,5)` | affine-in-`y` reduction | automorphism |
| `(2,5)` | genuine coprime pattern | empty, quintic `CONFIRMED` |
| `(3,5)` | genuine coprime pattern | empty, quintic `CONFIRMED` |
| `(4,5)` | genuine coprime pattern | empty, quintic `CONFIRMED` |
| `(5,5)` | equal-degree `GL_2 -> (r,5)`, `r<5` | reduces to confirmed rows |
| `(0,6)` | degree-zero obstruction | impossible |
| `(1,6)` | shear `g-kf^6`, or affine reduction | maximum degree at most five |
| `(2,6)` | shear `g-kf^3` | maximum degree at most five |
| `(3,6)` | shear `g-kf^2` | maximum degree at most five |
| `(4,6)` | genuine imprimitive pattern | empty only if newest closure is confirmed |
| `(5,6)` | genuine coprime pattern | empty only if newest closure is confirmed |
| `(6,6)` | equal-degree `GL_2 -> (r,6)`, `0<=r<=5` | depends exactly on the two preceding leaves |

This table also explains why `gcd(4,6)=2` does not help: `6/4` is not an
integer, so no polynomial power of the degree-four coordinate cancels the
degree-six top.  Conversely `(2,6)` and `(3,6)` are removed by honest
polynomial shears.

## 5. Dependency proof of the conditional theorem

Let `(f,g)` be a characteristic-zero Keller pair with both actual degrees at
most six.

- If the maximum is at most five, the hostile-confirmed quintic theorem
  makes the pair an automorphism.
- If the ordered pair is `(m,6)` with `m=0,1,2,3`, Section 3 either rejects
  it or reduces it to maximum degree at most five.
- The two cases `m=4,5` are exactly the two newest exclusion claims.
- If the pair is `(6,6)`, a constant target operation produces `(r,6)` with
  `r<=5`, so one of the preceding bullets applies.

Therefore hostile confirmation of both newest exclusions implies the full
degree-at-most-six theorem.  No compatibility condition between the two
closures is needed: they concern disjoint actual leading-degree strata.

Over a non-algebraically-closed ground field, the exclusions may be checked
after base change to an algebraic closure.  Nonexistence there implies
nonexistence over the original field.  For the reducible strata, automorphy
over the algebraic closure descends by uniqueness of the polynomial inverse
or faithful flatness.  Hence the conditional conclusion is genuinely over
every characteristic-zero field, not only over `Kbar`.

## 6. What is proved now, and what is not

Current reviewed theorem:

```text
deg_y(f),deg_y(g)<=5  =>  (f,g) is an automorphism.     (6.1)
```

Current reviewed sextic skeleton:

```text
fundamental blockers = {(4,6),(5,6)}.                  (6.2)
```

Current provisional synthesis:

```text
CONFIRM(4,6 exclusion) and CONFIRM(5,6 exclusion)
  => deg_y(f),deg_y(g)<=6 implies automorphism.         (6.3)
```

The pair `(6,6)` is unresolved under confirmed inputs alone, but only
derivatively: its possible `GL_2` reductions include the two unreviewed
leaves.  There is no third fundamental blocker.

The two pending hostile reviews should focus on different load-bearing
points:

- `(4,6)`: fractional Newton-valuation exhaustiveness, the nonsquare Galois
  parity descent, and the polynomial-degree cone classification for `eta`;
- `(5,6)`: the binary common-factor lemma, restoration of lower-weight
  parameter terms in the finite-map argument, and noncancellation of the
  degree-`10q-1` `eta` term.

Passing replays are evidence for the identities, not substitutes for those
reviews.

## 7. Conditional AS109 corollary, quarantined

If (6.3) is promoted, an exact AS109 lift whose two correction polynomials
have `y`-degree at most six has coordinate `y`-degrees at most six over
`Q_109`.  The field theorem would make it an automorphism and hence
injective.  The already reviewed residue-ball Hensel lemma makes every exact
lift of the seed `(x-x^109,y)` noninjective over `Q_109`.  Therefore the
reviewed AS109 correction-degree floor would conditionally rise from six to
seven.

That corollary is **not promoted here** because both sextic leaves remain
unreviewed.  It is not an arbitrary-support no-go, a lift, or a JC2
inference.

## 8. Deterministic replay

Run:

```text
python3 cases/as109_bounded_y6_chain_audit_20260824/verify_degree_pair_coverage.py
```

Expected output:

```text
PASS-BOUNDED-Y6-DEGREE-PAIR-COVERAGE
unordered_pairs=28
ordered_pairs=49
confirmed_genuine_leaves=(2, 3),(3, 4),(2, 5),(3, 5),(4, 5)
provisional_genuine_leaves=(4, 6),(5, 6)
confirmed_only_unresolved_pairs=(4, 6),(5, 6),(6, 6)
fundamental_unreviewed_blockers=(4, 6),(5, 6)
conditional_on_both_closures=ALL_49_ORDERED_PAIRS_COVERED
```

The replay recursively enumerates every possible lowered actual degree after
an equal-degree `GL_2` operation or divisible-degree shear.  It is a 28-pair
finite logic audit, not a support or coefficient search.

For this synthesis the registered producer replays were also rerun
unmodified: quadratic, cubic, quartic, quintic, sextic preflight, the
confirmed `(4,6)` discriminator, both newest closures, and both `(5,6)`
Python/Singular certificates all pass.  The newest passing verdicts remain
provisional until hostile review.

Hashes are frozen in
`cases/as109_bounded_y6_chain_audit_20260824/FREEZE.sha256`.  No producer,
review, canonical top-level file, ledger, or AWS resource was edited.
