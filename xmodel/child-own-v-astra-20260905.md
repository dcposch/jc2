INSTRUMENT — own characteristic data under Moh descent.
Lane `child-own-v-astra-20260905`; Astra/Codex.
Frozen basis: `1e5bfa910708e7ec25634f85c11fc2924ecd830d`.

**The copied upper V labels are not the child's data. The bottom label can be
identified, with a proof that uses the selected source disc.** In the reduced
source regime of the operative census, the transported child's own `V'_2=V_2`.
Higher values come from inversion and depend initially on where the selected
source centre first becomes nonzero. `descend_own()` now computes these values
with exact rationals and correlated finite sets, keeping an empty set empty.

There are three different results, which must not be conflated:

* **DETERMINED:** the own-D1 U-NEG predicate has 90 rows. Proposition 6.4
  licenses 84 directly. The remaining six have a separate unresolved minor
  radius boundary; their U-NEG application remains conditional, although the
  source compatibility test below excludes their necessary configurations.
* **DETERMINED:** C-TOP contributes **zero exclusions**. Local inversion
  forces its inequality on all 1,020 nondropped `u_s=1` rows; 45 have nonempty
  complete necessary sets. The 20 retained `u_s>1` rows have only confirmed
  prefix data, so their terminal C-TOP remains OPEN.
  An empty own-data set is not counted as a C-TOP pass or failure.
* **DETERMINED finite-set census:** after checking the source's actual centre
  stabilizers and compulsory major branches, and the separate finite-pole
  obstruction on the 90 dropped-tail rows, **65 rows have singleton necessary
  own-data sets; 1,355 have empty sets**. There are no surviving nonempty
  multivalued sets. These are necessary configurations, not realized pairs.

The old `936 / 174 / 310` partition is reproduced and replaced below. The new
source inconsistencies are not credited to C-TOP. No ledger, `jc2-lean`, or
`ideation-*` file was edited.

**1. Custody, population and meaning of a datum.** The first substantive
operation built the manifest from the receipt, mechanically:

```sh
awk -F= '
/^charged_input_[0-9]+_sha256=/ {
 k=$1; sub(/_sha256$/, "", k); hash[k]=$2
}
/^charged_input_[0-9]+_basename=/ {
 k=$1; sub(/_basename$/, "", k); name[k]=$2
}
END {for (k in hash)
 print hash[k] "  /tmp/jc2-lane.wwyG4k/inputs/" name[k]}
' xmodel/child-own-v-astra-20260905.run.v2 > /tmp/child-own-v-astra-20260905.sha256
sha256sum -c /tmp/child-own-v-astra-20260905.sha256
```

Result: **DETERMINED, 7/7 OK**; manifest at
`box/child-own-v-20260905/inputs.sha256`. Charged contents were read from the
frozen copies. Primary formulas were read from fresh images of the checked PDF.

`sweep.py` freshly imports the checked enumerator as
`moh_skeleton_full_frozen`, verifies that the operative Tree imports that same
module, and enumerates `16<=n<=200`, `Kmin=2`, `full=True`. Tree settings remain
`gate=False, ode=True, capacity=False, passport=False, recenter=True`.
**DETERMINED:** 24,063 enumerator rows, 1,420 operative rows. Complete source
keys match the frozen gate replay and operative inventory. The multiset of
`(class_id,parent_n,parent_m)` matches all 1,420 `hard-rows.jsonl` records.
Every regenerated child M/d label matches the frozen partition arithmetic.
The stronger source check is applied afterwards.

Definition 5.1(1), p.179, attaches V to a chosen tower of discs. Its meaning is

```
V'_i = #{roots of G in D'_(i-1)} / (n'/d'_i).
```

Roots include multiplicity. A pair can have several major towers. Here `D'`
is the tower transported from the source row's selected tower. Its root
count is not a coefficient of h or a characteristic label.

**2. Own M and d, and the places involved.** Write
`q=d_s`, `v=V_s`, `u=q-v`, `c=u/q`, and `ell=v-u-1`. The coordinate map in
Proposition 6.3 is, after the stated source normalization,

```
y=gamma^(-u),  z=y-beta*x-e=A(gamma)+pi*gamma^v,
x=(gamma^(-u)-e-A(gamma)-pi*gamma^v)/beta,
beta != 0, deg A < v.
```

The ring is `k[gamma,pi]`, with algebraically closed characteristic-zero k;
gamma is the coefficient variable, pi the polynomial/root variable. Its
infinity is `gamma->infinity`. The minor disc used to polynomialize this map
is at `gamma->0`. Source roots were expanded at `t=1/x->0`. These are three
different descriptions, not interchangeable places.

Proposition 6.3(2) gives exact pi-degrees `n'=cn`, `m'=cm` and
`deg_pi T'_j=c(-mu_j)`, for `j<s`. The recurrence obtained directly from
p.150 is

```
mu_1=M_1;
mu_j=(d_(j-1)/d_j) mu_(j-1)+M_j-M_(j-1).
```

Use the child's own `eta=G^(-1/n')`, not the parent's fixed-x eta. Canonical
approximate-root relations retain their strict lower-weight terms under the
map. Successive Hensel steps in this own eta expansion force the first term
outside each preceding gcd lattice at `cM_i`: the relevant approximate root
has its exact prescribed degree, its leading derivative is nonzero, and all
lower canonical terms have later derivative order. Thus the retained data are

```
M'_i=cM_i  (1<=i<s),
d'_1=n',  d'_(i+1)=gcd(n',M'_1,...,M'_i)=c d_(i+1).
```

Nonzero constant coefficients count in p.150's definition. The implementation
checks the mu recurrence and degree scalings independently. On the gate's
180/120 row the own quasi-root degrees are 20,18,87.

The raw last retained gcd is u. For u=1 the raw chain closes. For u>1 these
are confirmed **prefix** data: the later nondivisible coefficients, effective
terminal characteristic index, and its complete tower have not been supplied
by the source numbers. We do not invent an extra pair at `n'-2` or infer an
effective top merely from a finite gcd list.

Exactly **DETERMINED 90 rows** have the raw terminal `M'=n'-1`, all with u=1.
Their post-drop gcd exceeds one. Raw data and historical p.174 indexing are
retained separately; section 6 disposes of these rows by another contradiction.

There are two source-reading corrections. The Jacobian exponent comes from
the p.197 statement and the coordinate chain rule: `J=constant*gamma^ell`.
The denominator/exponent display in the p.198 proof is inconsistent with
them. Also, p.202's source75/50 bracket `delta_1=1/3` should be `2/3` by
Definition 5.1; p.207's child bracket `delta'_1=4/3` agrees with physical inversion.
Neither printed slip is propagated into the code.

**3. The finite inversion recipe.** Initially the major source disc contains
`(n/q)v>n/2` roots of g. Distinct equal-radius conjugate discs are disjoint,
so this disc is Galois invariant. Normalize its slope and the selected common
constant to zero. Every relevant source radius is below 1; the first retained
radius is nonnegative. Before a nonzero coefficient has been selected, a
source disc has zero centre.

This last statement needs minimality, not a lattice guessed from radius labels.
Proposition 5.3, p.180, constructs the next disc as the minimal disc containing
the entire indicated selected root multiset. If this set is invariant and had
a shared first coefficient at a nonintegral exponent between the recorded
radii, conjugation would separate its roots there. That contradicts the next
minimal radius. An integral common constant is removable, and there is no
positive integer below 1. Thus first nonzero support occurs at an actual
positive recorded radius `delta_j`, with `2<=j<s`. Proposition 5.6 excludes
the all-zero D1 route in the reduced non-coordinate source regime. Its
alternative is a coordinate pair or degree reduction; it is not a theorem
excluding arbitrary polynomial pairs without that source hypothesis.

At a zero-centred node i put

```
P_i=V_(i+1) d_i/d_(i+1),  delta_i=a_i/b_i in lowest terms.
p(xi)=xi^z product_nu (xi^b_i-c_nu)^r_nu,
z+b_i sum r_nu=P_i,  c_nu distinct and nonzero.
```

Proposition 4.6, p.170, gives the corresponding initial g as `p^(n/d_i)`.
A nonzero source orbit has initial equation `y^b_i*x^a_i=c_nu`; inversion
gives `x^a_i=c_nu*gamma^(u b_i)`. It produces **a_i distinct inverse
coefficient discs**, each with `r_nu(n/d_i)` roots. A denominator change counts
conjugate discs; it does not multiply the roots inside one such disc. In
particular no extra factor u belongs in this root count.

At the raw top, writing `h=d_(s-1)/q`, the zero inverse coefficient has

```
W_zero=u h-a sum r_nu
      =u h-delta_(s-1)(v h-z),
```

and each nonzero inverse coefficient has normalized count `r_nu`. This gives
the general version of the gate's 15+15 calculation.

For the whole selected route, enumerate the first nonzero index j. For every
i>j the selected source factor is zero, so `z=V_i`; at j it is nonzero with
multiplicity `V_j`. The immediate necessary tests are

```
i>j: b_i divides P_i-V_i;
i=j: delta_j>0 and b_j V_j<=P_j.
```

Start `W_s=u` and descend through the zero selections:

```
W_i=(d_i/d_(i+1)) W_(i+1)-delta_i(P_i-V_i),  i>j;
W_i=V_i,                                                   i<=j.
```

The subtraction is an exact projection count: the source roots leaving at
that order contribute `delta_i*(n/d_i)*(P_i-V_i)` inverse roots. Finite-x
points above y=0 remain in the zero remainder, whose total is determined by
the exact degree n'. After removing the common A shift their pi orders are
at least v, whereas the mapped source radii are below v. Their unrecorded
coefficients cannot split one of the relevant earlier discs.

At the first nonzero coefficient and below it, formal local inversion has a
nonzero leading derivative. It identifies the chosen source subdisc and an
inverse coefficient subdisc with the same number of roots of g and each
retained approximate root. This supplies the missing geometric identification
for `W_2=V_2`; the numerical equality `n'/d'_2=n/d_2` is only its normalization.

The disc identification includes its metric. If `e=delta_j`, the radii are

```
delta'_i=v-u/delta_i                       for i>=j;
delta'_i=v-u-(u/e)(1-delta_i)               for i<j.
```

Both expressions agree at j. For every nondropped u=1 candidate these equal
the radius formula computed from own W and confirmed terminal M.

**4. Which coefficients remain free, and what “finite set” means.** The
constants `c_nu`, their finer terms, and unselected multiplicities are not
realized coefficients in a census row. The only way they can change this
transported V vector is through a different compatible first nonzero index.
The recipe stores the entire vector for each such index, preserving
correlations; it never takes an arbitrary product of coordinate sets.

The first-support arithmetic alone gives **DETERMINED set cardinalities**:
1,095 empty sets, 323 singleton sets, two sets of size two. The complete list
of nonempty multivalued alternatives at this preliminary stage is

| Source necessary row | Preliminary child V alternatives |
|---|---|
| `(168,112), M=(-112,84,156,166), V=(1,5,3)` | **SET-VALUED** `{(1,3),(1,5)}` |
| `(192,128), M=(-128,160,172,190), V=(3,3,3)` | **SET-VALUED** `{(3,2),(3,3)}` |

Both outer sets fail the compulsory source-branch continuation check below.

For completeness, a shared off-radius coefficient cannot enlarge an already
nontrivial centre denominator L either: minimality makes it fixed by the
subgroup fixing the current centre. Therefore the exact stabilizer update is

```
selected zero: L stays L;
selected nonzero at delta: L becomes lcm(L,den(delta));
relative orbit length at the next radius: A=den(L*delta_next).
```

`own_v_routes.py` checks the entire necessary source tree with this state,
including every unselected major factor that p.200 requires to extend. It
retains the operative polynomial ODE resonance check and squarefree-q orbit
capacity; it adds no passport or numerical child cap. At the bottom the
p.188 divisibilities use this actual L. The old Tree instead accumulated the
denominators of radius labels even when the corresponding coefficients were
zero. A zero coefficient has no ramification denominator.

Exhausting this necessary source model leaves **DETERMINED 90 singleton
routes and 1,330 empty sets**. Both preliminary multivalued rows become empty;
not every arithmetic first-support option can coexist with its compulsory
siblings. An independent validator, which does not import the route engine,
checks 90 root witnesses, 442 node occurrences and 244 bottom occurrences:
all pass the metric, stabilizer, mass, resonance and continuation conditions.
Singleton means a forced conditional value, without solving the p/q equations;
empty means incompatibility with these necessary conditions.

**5. Worked and printed controls.** Every numerical entry in this paragraph
and table is **DETERMINED**, conditional on the specified licensed source.
For `(180,120), M=(-120,132,150,178), V=(2,4,5)` the top radius is `1/6` and
`p=xi^4(xi^6-a)`. The nonzero orbit has 90 source roots and gives 15 inverse
roots. G has degree 30, leaving 15 at the zero inverse coefficient. Thus
`W_3=15/(30/2)=1`, and local inversion below the first nonzero source
coefficient gives `W_2=2`. The alternate source `V_2=3` gives `(W_2,W_3)=(3,1)`.
Both complete necessary source witnesses survive the corrected stabilizer
check. Neither is a realized Keller pair.

For `(96,72), M=(-72,36,78,94), V=(4,3,5)` the top radius is `1/7`, with
`p=xi^3(xi^7-a)`. The inverse split is 8+8, so its conditional own top is
again 1, with raw `M'=(-12,6,13)` and `d'=(16,4,2,1)`. The next all-zero
source node has `P_2=6`, full denominator 7, selected multiplicity 4:
neither `7*4<=6` nor `7|(6-4)` holds. Its complete set is empty. The API
retains the forced local top 1 and independent D1 identity 4 as diagnostics;
it does not fabricate a completed child vector for this inconsistent row.

Moh's five p.207 rows are reproduced in every printed child column:

| Source `(n,m); M_2; V_2` | Child `(n',m'); M'_2; V'_2` | `delta'_2, delta'_1; ell` |
|---|---|---|
| `(64,48);52;3` | `(16,12);13;3` | `-1,1/4;1` |
| `(84,56);64;2` | `(21,14);16;2` | `-1/2,7/6;1` |
| `(84,56);72;5` | `(21,14);18;5` | `-1,1/3;1` |
| `(75,50);55;3` | `(15,10);11;3` | `-1,1/2;2` |
| `(75,50);55;2` | `(15,10);11;2` | `-1,4/3;2` |

The second row's source radius `2/7` produces two separate inverse coefficient
discs per orbit, tested explicitly. The `(99,66)` row on p.202 retains labels
`M=(-66,77,97)` exactly. Moh does not print it as a p.207 descendant. Its
conditional Prop.6.3 prefix is `(27,18), M'=(-18,21), d'=(27,9,3)`; it is
never mislabeled as a printed child with degree pair `(99,66)`.

**6. The 90 dropped tails have a different obstruction.** Rescaling the
post-drop Definition 5.1 radius formula is not justified by p.174 alone for
a monomial-Jacobian child. Example: source `(108,72), M=(-72,84,104,106),
V=(8,8,3)` has raw child `(27,18), M'=(-18,21,26)`. After dropping 26 the
old formula gives `delta'_2=-2/5, delta'_1=0`; physical inversion gives
`0,1/3`. Across the preliminary u=1 routes, all 104 radius discrepancies
occur on 42 dropped routes; nondropped routes have no discrepancies.

There is a separate source obstruction that avoids this invalid formula.
For a dropped row, `u=1`, `n-M_(s-1)=q`, and source `delta_(s-1)=0`.
Definition 5.1(4) licenses Proposition 4.6 at this actual source disc. Its
squarefree factor Q has degree

```
deg Q=V_s*(n-M_(s-1))/q=V_s>=3,
T_(s-1),initial = p^A Q,
A=(-mu_(s-1)+M_(s-1)-n)/d_(s-1).
```

On all 90 rows A is an integer between 13 and 341. Thus there is no
cancellation: the **retained** T_(s-1) has at least three distinct constant
residues at this source radius. After any one constant normalization at
least one residue C remains nonzero. Along that branch `x` has a pole,
`y->C`, and the fixed licensed coordinate map gives a finite nonzero
`gamma_0`, with `gamma_0^u=C^(-1)`, but pi has a pole.

Proposition 6.3(1),(2) makes the transformed T_(s-1) a monic polynomial in
pi over `k[gamma]`. A root of such a polynomial cannot have a pole above a
finite gamma: the highest pi power would have uniquely smallest valuation
in its equation. This contradiction uses one fixed licensed chart and
survives every choice of its constant normalization. It does not assume
monicity in every arbitrarily translated chart. All 90 have u=1, so
Proposition 6.4 supplies the licence.

**DETERMINED:** 25 of these 90 rows survived the corrected necessary source
tree, and 65 already failed it. Removing the 25 new failures leaves
**65 singleton own-data sets: 45 at u=1 and 20 at u>1**. This is not a
90-row C-TOP exclusion, and the invalid effective radius formula is not used.

**7. Typed counts and corrected partition.** On all 1,420 rows the independent
D1 identity is conditionally DETERMINED: `W_2=V_2`. It gives exactly 90
instances of `W_2>K'=d'_2`. The U-NEG proof is simply that the identified
disc would contain `(n'/K')W_2>n'` roots. It uses no h cap and no top convention.
Of these, 84 have the automatic u=1 licence.

The other six have `(u,v)=(2,3)` or `(2,4)`. The frozen strict-window argument
eliminates radii in `(1,v/u)`, but p.193–194 only gives `delta*>=1`. The
boundary 1 cannot be omitted. At that boundary the displayed face identity
reduces to

```
p Q_dot-W Q p_dot=p^(W+1),
Q=(pi+C)p^W.
```

Here dot means differentiation in pi, and Q is the face polynomial.
Taking `p=pi(pi-1)`, `C=2`, `W=2` gives an exact polynomial split-face
solution, passing the stated Galois and local multiplicity tests. The driver
checks the polynomial identity exactly. It is a face control, not a source
pair. Therefore the six U-NEG applications remain
`OPEN[MINOR-RADIUS-BOUNDARY-ONE]`. All six independently have empty necessary
source trees, so retaining this licence distinction does not change the
65-row finite-set remainder.

Here is the own-versus-copy comparison after all audited necessary source
conditions, with historical effective levels used to align the frozen row
list. The numbers of rows in every column are **DETERMINED**; the final
column describes **SET-VALUED empty data**, not a numerical V comparison.

| Level i | Own V determined equal to copy | Own V determined different | Nonempty multivalued | Empty own-data set |
|---|---:|---:|---:|---:|
| 2 | 65 | 0 | 0 | 1,355 |
| 3 | 15 | 7 | 0 | 1,331 |
| 4 | 1 | 0 | 0 | 926 |
| 5 | 0 | 0 | 0 | 136 |

Rows without that level are absent. Raw-level empty counts are
`1355,1355,962,166`; nonempty comparisons are unchanged. An empty set has no
scalar V comparison. Partial implications are banked in `local_V` and `route_steps`.

To expose the effect of completing the source constraints, the preliminary
first-support outer sets at levels 2–5 respectively have determined different
counts `0,74,38,0`; level 3 also has the two listed multivalued cases.
Those are **outer-set diagnostics**, superseded by the complete table above.
The seven final changed rows are enumerated in the machine-readable output;
six have u=1 and one has u=2. For example the source144/96 row with
`M=(-96,112,132,142), V=(8,8,3)` has own retained `(8,3)`, not `(8,8)`.

**C-TOP, DETERMINED predicate accounting:** local top alternatives satisfy
the bound on all 1,020 nondropped u=1 rows, including 13 with SET-VALUED local
top V. Of these, 45 have a nonempty complete set and 975 fail elsewhere.
Zero top failures occur. All 310 u>1 local prefix comparisons also satisfy
the bound, but terminal C-TOP is unlicensed. Empty complete sets are not
counted as completed child passes; the 90 dropped rows have the separate
finite-pole obstruction. The old 936-row C-TOP kill is not recovered.

The disjoint corrected partition, with every count **DETERMINED**, is:

| Bucket | Rows | Mathematical type |
|---|---:|---|
| Own U-NEG, u=1 | 84 | Licensed necessary contradiction |
| Own U-NEG predicate, u=2 | 6 | Radius-conditional U-NEG; source tree independently empty |
| Dropped tail, disjoint from U-NEG | 90 | Licensed finite-pole contradiction |
| Other empty necessary source trees, u=1 | 891 | SET-VALUED empty own-data set |
| Other empty necessary source trees, u>1 | 284 | SET-VALUED empty own-data set |
| Singleton own data, u=1 | 45 | DETERMINED necessary data; own C-TOP passes |
| Singleton retained own data, u>1 | 20 | DETERMINED prefix values; descent/terminal scope conditional |
| Total | 1,420 | Necessary source rows, never a count of pairs |

For direct reconciliation with the frozen tiers:

| Old tier | U-NEG | Finite pole | Other empty source tree | Nonempty own data |
|---|---:|---:|---:|---:|
| `ctop_killed` 936 | 84 | 56 | 790 | 6 |
| `live_us1` 174 | 0 | 34 | 101 | 39 |
| `us_ge2` 310 | 6 | 0 | 284 | 20 |

All entries are **DETERMINED** set arithmetic with the stated radius qualification.
The remainder is 65 necessary rows. The 45 u=1 rows have effective
heights `{2:24,3:20,4:1}`; the 20 u>1 rows have `{2:19,3:1}`.

**8. Implementation, validation and downstream use.** New reusable code is
`box/lib/descend_own.py` and `box/lib/own_v_routes.py`. The API takes a source
Skel and returns raw/effective M,d, exact degree data, correlated `V_vectors`,
per-level finite marginals, source-tree witnesses, explicit obstructions,
physical inverse radii and separate local diagnostics. It refuses nonreduced
source scope and nonintegral characteristic data; it never truncates a
rational. The radius flag for u>1 must be supplied by an independent licence.
The old scalar `descend()` remains a historical copied-label API; replacing
its return value in existing consumers with a set would silently break them.
This lane's entire new sweep uses `descend_own()`.

Reproduction commands, run from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 box/child-own-v-20260905/test_descend_own.py
PYTHONDONTWRITEBYTECODE=1 python3 box/child-own-v-20260905/test_own_v_routes.py
PYTHONDONTWRITEBYTECODE=1 python3 box/child-own-v-20260905/sweep.py
```

**DETERMINED validation:** eight own-descent and six source-route test methods
pass. Fresh enumeration and frozen row comparisons pass. The independent
`audit_route_witnesses.py` and `audit_receiver_support.py` also pass.
`own-rows.jsonl` contains every row; summary, witness and radius-control JSON
files preserve all qualifications.

The copy error's receiver effects are narrower than its accounting effects.
At fixed confirmed terminal characteristic data the source-support theorem's
`G_i` uses the terminal radius
`d=(ell+1)/(n'-M_last'-1)` and block degree. Within a fixed degree class it
is independent of V. Of course the block degree also uses the already fixed
`K=gcd(n',m')`. The s'=3/4 source-complete compiler takes `D_i union G_i`,
gives each included monomial a free coefficient, and saturates by c alone.
Changing V changes the decorative D_i part, not the included G_i family.

The direct audit checks **DETERMINED 18 saved charts in six classes, all
108 coefficient blocks**, constructing G without V. All blocks contain G,
with free coefficients and c saturation. An exact UNIT still excludes the
G-supported class: specialize decorative coordinates outside G to zero.
The actual terminal M and the support theorem's other hypotheses remain
necessary; a u>1 prefix is not automatically terminal.

`receiver-audit.md` traces the copies in `census_sweep.py`,
`sprime3_compiler.py`, `descend14.py` and `scope_enum.py`, through lower radii,
B values, raw D_i inventories, sizing, fibre keys, tiers and routing.
Some G-complete emitters skip on V-dependent B before building G and need
repair. Old s'=2 receivers use V in actual h faces, partitions, x-width caps
and saturation. Their UNIT results need a necessary-family proof or a correct
enlargement; their V dependence is substantive.

No saved chart or solver certificate was rewritten. The audit establishes
coverage, without making a new solver exclusion claim.

**9. Remaining scope and FALLACY-v2.** `OPEN[CHILD-LEVEL2-IDENTIFICATION]` is
closed for the reduced source's transported D1 under a licensed descent,
not for an arbitrary all-zero or unchosen tower. The live open scopes are
`OPEN[MINOR-RADIUS-BOUNDARY-ONE]` for the six conditional U-NEG applications,
`OPEN[PROP6.3-RADIUS-US>1]` where no radius proof is supplied, and
`OPEN[CHILD-TERMINAL-SUPPORT-US>1]` for a prefix's subsequent characteristic
data. Realization of every nonempty necessary set remains unasserted.

Floors, attained counts, cover series, places and disc labels remain distinct.
No empty set supplies an arbitrary datum. No new exit-price assertion,
quotient/saturation computation, ledger promotion or Lean claim is made;
no new `charge_basis` declaration is appropriate.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `24444`.
- Body SHA-256:
  `83e5bf7b5bb620ccda071ce616fa82007069cebccf3a445829519d767cb97f32`.
- Frozen basis: `1e5bfa910708e7ec25634f85c11fc2924ecd830d`.
