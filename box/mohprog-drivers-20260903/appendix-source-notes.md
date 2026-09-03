# Moh 1983 source-only notes: minor discs and Appendix II

Scope discipline: these notes were made directly from the 300-dpi page images
`/tmp/moh-pages-sol56/moh-51.png` through `moh-73.png`.  I did not read any
charged Markdown report.  Journal-page numbering is used below.

## Exact appendix boundary

- Appendix I starts on p.202, below the degree table, under the heading
  “Appendix I. The polynomial solutions of some ordinary differential
  equations.”  It continues through Proposition A.5 at the top of p.207.
- Appendix II starts in the middle of p.207, immediately after Proposition
  A.5, under the heading “Appendix II. Some special cases.”
- Appendix II ends with the last paragraph of p.211 (“All other cases can be
  computed directly as above. There is no counter-example ...”).
- p.212 is References.  Thus Appendix II is pp.207–211, not pp.203–212.

## Section 6: what is and is not an extra numerical restriction

### The major/minor multiplicity dichotomy (p.190)

At the opening of section 6 (p.190, first two paragraphs after the heading),
Moh fixes a factor `pi-c_r` of the bottom polynomial `p(pi)`, of multiplicity
`V_r`.  He states the two alternatives

```
deg p(pi) = V_{r+1} d_r/d_{r+1} >= V_r > d_r/(n-M_r)  (major extension),
d_r/(n-M_r) >= V_r                                  (minor disc).
```

The first displayed chain is precisely the local numerical content of printed
search condition (7).  Proposition 6.1 (pp.190–193) proves facts about the
minor alternative: its radius `delta^*_{r-1}` is at least 1, and suitable
pi-roots are distribution detectors.  Those conclusions depend on actual
root discs/leading polynomials and do not yield another scalar inequality in
the recorded tuple `(n,M_i,d_i,V_i,delta_i)`.

The summary theorem on p.200 makes the same point in root-count language.  For
subdiscs `E_i` inside `D_r`, more than `n/(n-M_r)` roots of `g` gives a major
extension; at most that number gives a minor disc (items (4),(5)); the number
of subdiscs is bounded by `(n-M_r)V_{r+1}/d_{r+1}` (item (6)); and at least one
subdisc is major (item (7)).  Item (7) of this theorem supplies existence of a
chosen major factor, not a new lower bound beyond printed search (7).

There is, however, a **global completion datum** which a path-only numerical
tuple forgets: the multiplicities of all factors of `p(pi)` must add to its
displayed total degree, and at least one is in the major range.  The theorem
does not state a nontrivial scalar obstruction on one selected path from that
completion alone.  It is nevertheless a legitimate candidate if the program
kept the whole factor-multiplicity partition rather than only the selected
`V_r`.

A sharper version combines this with the orbit calculation printed on p.201.
For each level, nonzero roots occur in the `A_{r-1}`-orbits behind condition
(10), while the fixed root `pi=0` has the residue-class multiplicity in (11).
At the top, p.194 additionally requires at least one positive-multiplicity
minor sibling.  Thus a defensible executable candidate is:

```
FULL-FACTOR-PARTITION:
  partition P_r=V_{r+1}d_r/d_{r+1} into a fixed-zero factor and complete
  nonzero A_{r-1}-orbits; mark at least one factor major, and at the top at
  least one factor minor; require every factor's multiplicity to satisfy its
  (10)/(11) branch and the appropriate major/minor threshold.
```

This is existential and strictly stronger than checking (10) or (11) only on
the selected tower factor.  Moh does not spell out this algorithm, so it must
be reported as a candidate rather than PROVED-IN-SOURCE equivalence to his
program.  Every printed row preserves it in principle because p.194 asserts
the required actual major/minor pair; a numerical witness partition still
has to be generated for a fail-closed implementation.

### Two source-proved top-level consequences (p.194)

On p.194, in the paragraph beginning “We shall apply Proposition 6.1,” Moh is
in the special top configuration `M_s=n-2`.  He says explicitly that the
top major disc `D_s` contains **both** a major disc `D_{s-1}` and a minor disc
`D^*_{s-1}` (citing Propositions 5.3 and 6.1).  The indexing matters:
extending `D_r` to `D_{r-1}` uses a factor of multiplicity `V_r` (p.190).
At `r=s`, the total bottom-polynomial degree is
`V_{s+1}d_s/d_{s+1}=d_s`, by Definition 5.1's
`V_{s+1}=d_{s+1}`.  Consequently the positive minor sibling forces
`V_s<d_s`.  It does **not** force
`V_{s-1}<V_s d_{s-1}/d_s`; that would require a minor sibling one level
lower, which p.194 does not assert.

The same p.194 paragraph computes

```
delta_{s-1}
 = 1 - (n-M_{s-1})[v_s(n-M_s)-d_s]
       / ((n-M_s)[v_s(n-M_{s-1})-d_s])
 = [u_s(n-M_{s-1})-d_s]
       / [v_s(n-M_{s-1})-d_s],
```

using `u_s=d_s-v_s`, and concludes `delta_{s-1} >= 0`.  Lemma 6.1 immediately
below restates: if `delta_s=-1`, then `delta_{s-1}>=0`.  Hence a second
source-proved candidate is

```
TOP-RADIUS: u_s(n-M_{s-1}) >= d_s,
```

provided the displayed denominator is positive, as it is in Moh's setup.
This preserves every printed row: their p.202 top next-radii are `1/4`,
`2/7 [1/4]`, `1/5`, and `1/3`, all nonnegative.  This may be logically
automatic from the complete Definition 5.1 hypotheses, but it is not a
consequence of the bare weak inequality in printed (7), so it deserves a
separate implementation test.

The same paragraph writes the highest homogeneous form explicitly as

```
[(y-a x)^(v_s) (y-b x)^(u_s)]^(n/d_s),  a != b,
u_s=d_s-v_s.
```

Thus this is the source's `H=L_1^v L_2^u` / two-points-at-infinity split.
Numerically it requires `u_s+v_s=d_s` with both parts positive.  In fact
Definition 5.1(2) on p.179 sets `V_{s+1}=d_{s+1}`; its `i=s` instance and
`M_s=n-2` give only the printed weak chain `d_s>=V_s>d_s/2`.  The genuine
two-factor split strengthens its upper end to

```
TOP-SPLIT-STRICT: d_s > V_s > d_s/2,
```

because `u_s=d_s-v_s` is positive.  Corollary 6.1's proof writes exactly
`d_s>v_s>d_s/2` on p.200.  The lower bound is printed (7), but the strict
upper bound is an additional scalar condition unless another listed premise
already encodes the two nonzero linear factors.  All six rows have the
required split: `(d_s,v_s,u_s)=(4,3,1)`, `(4,3,1)`, `(5,4,1)`, or `(11,8,3)`.

Adjacent-source cross-check: Lemma 5.3 at the bottom of p.185 states the
two-root homogeneous-form criterion with `d_s>v_s>d_s/2`.  Its proof on
p.186 first derives `d_s>V_s>d_s/2`, then says the degree-two bottom
construction (`deg q(pi)=n-M_s=2`) has `p(pi)` with two roots, one of
multiplicity `V_s`; the stated homogeneous form follows.  This identifies
lowercase `v_s` with tower
`V_s` and makes TOP-SPLIT-STRICT **PROVED-IN-SOURCE**, not merely an inference
from p.194.

After Lemma 6.1, p.194 gives forms (8)–(10) for roots in the major and minor
discs.  The minor radius is at least 1; after a coordinate choice the roots
in the minor disc have common initial terms.  These are geometric/root-series
facts, not further integer-tuple tests.

### Propositions 6.2–6.4 and Corollary 6.1 (pp.195–200)

- Proposition 6.2 (pp.195–196, items (1)–(4)) gives bidegrees after
  `z=y-bx-e`:
  `deg_y gbar=v_s n/d_s`, `deg_z gbar=u_s n/d_s`, and analogously
  `v_s(-mu_i/d_s)`, `u_s(-mu_i/d_s)` for approximate roots.  The apparent
  divisibilities are already furnished by the characteristic gcd data; Moh
  does not use them as an extra census filter.
- Proposition 6.3 (pp.197–198) is conditional on the unrecorded minor radius
  `delta^*_{s-1} >= v_s/u_s`.  It constructs a transformed polynomial pair,
  monic in `pi`, and gives
  `J_{gamma,pi}(gbar,Tbar_1)=-(u_s/b) gamma^(v_s-u_s-1)` (p.197 item (3),
  completed on p.198).  This is a reduction theorem, not an admissibility
  condition on a skeleton.
- Proposition 6.4 (pp.198–199) says `u_s=1` is a sufficient condition for
  `delta^*_{s-1} >= v_s/u_s=v_s`.  It is not a necessary condition.  Treating
  `u_s=1` as a global filter would be fail-open/incorrect: the printed
  `(99,66)` class has `d_s=11`, `v_s=8`, hence `u_s=3`, and Moh retains it.
- Corollary 6.1 (p.199 statement; p.200 proof) treats `d_s=3`.  The proof uses
  `3=d_s>v_s>d_s/2` and `v_s+u_s=3` to force `(v_s,u_s)=(2,1)`, then
  Propositions 6.4 and 6.3 transform to a smaller constant-Jacobian pair with
  degrees divided by `d_s`.  For a least-degree counterexample this excludes
  `d_s=3`; p.201 explicitly records `d_s>=4` in search condition (6).  Thus
  Corollary 6.1 supplies no *unprinted* scalar restriction beyond the list.

Bottom line for the minor-disc lane: the clean scalar candidates not already
visibly identical to printed (6)/(7) are TOP-SPLIT-STRICT and TOP-RADIUS.
The other potentially missing datum is a levelwise completion of *all* factor
multiplicities/root discs, not a scalar condition stated by Propositions
6.1–6.4.

## The p.202 output claim and six printed rows

The first paragraph of p.202 says: “The above discussion can be easily put
into a computer program. The computer program produces only the following
exceptions which satisfy the necessary numerical restrictions.”  The table
then contains six rows when bracket alternatives are expanded:

1. `(64,48; M2=52,M3=62,M4=63; V3=3,V2=3; delta2=1/4,delta1=9/16)`.
2. `(84,56; M2=64,M3=82,M4=83; V3=3,V2=2; delta2=2/7,delta1=16/21)`.
3. `(84,56; M2=72,M3=82,M4=83; V3=3,V2=5; delta2=1/4,delta1=7/12)`.
4. `(75,50; M2=55,M3=73; V3=4,V2=3; delta2=1/5,delta1=1/2)`.
5. `(75,50; M2=55,M3=73; V3=4,V2=2; delta2=1/5,delta1=1/3)` as printed on
   p.202; Appendix II's transformed bracket is `4/3` after the section-6
   transformation.
6. `(99,66; M2=77,M3=97; V3=8,V2=8; delta2=1/3,delta1=4/9)`.

No extra algorithm or pseudocode is printed between the list on p.201 and
this assertion.  Appendix II begins five pages later and takes these cases as
already selected.

## Appendix I facts adjacent to, but not used as a table filter

Appendix I is worth separating from Appendix II because it contains genuinely
general multiplicity theorems, yet Moh does not say that the pre-table program
ran them as additional tests.

- Proposition A.1 (pp.202–203): `D(a,b,p,q)=0` forces the degree weights and
  makes powers of `p,q` proportional.
- Proposition A.2 (pp.203–204): under the stated special degree relation and
  `epsilon>-1`, the differential equation forces `p,q` to be powers of a
  common linear polynomial.  Its proof compares root multiplicities and peels
  common factors.
- Proposition A.3 (p.205, items (1)–(4)): for
  `D(m,n,p,q)=c p`, every root of `p` is a root of `q`; `q` is squarefree;
  `p` is not a power of `q`; and at least one root of `p` has multiplicity
  `>m/n`.  This is a source-proved **whole multiplicity-partition** condition.
  The last inequality is the same kind of “large factor” used to grow the
  major tower.  A possible hidden-program candidate is that Moh retained the
  complete compatible multiplicity partition at every level, rather than
  merely one orbit size.  A mapping from A.3's `(m,n,p,q)` to each census
  level is required before implementation; the proposition alone does not
  justify an extra scalar test on `V_{r-1}`.
- Proposition A.4 (p.206) peels `p^l` from `q^*` and lowers the second degree
  in the differential equation.  Proposition A.5 (top p.207) says
  `D(m,n,p,q)=c!=0` forces `p q` to have only simple roots.  These could constrain
  a fully realized bottom polynomial, but Appendix II never turns them into
  a new numerical restriction on `(M_i,V_i)`.

Candidate ranking from these pages alone:

1. TOP-SPLIT-STRICT (`V_s<d_s`) — explicit in the p.194 two-factor form and
   written as `d_s>v_s` on p.200; all six printed rows preserved.
2. TOP-RADIUS (`delta_{s-1}>=0`) — explicit, scalar, source-proved, all six
   printed rows preserved.
3. LEVELWISE-MULTIPLICITY-COMPLETION — source-motivated by pp.190, 200, and
   Proposition A.3, but requires a typed map of the bottom ODE at each level;
   not yet a safe scalar theorem.
4. `u_s=1` — rejected as a global filter because it kills the printed `(99,66)`
   class; it is only a sufficient hypothesis for a reduction.

## Appendix II: every displayed reduction/elimination

### Entry and first transformation (p.207)

Appendix II opens by repeating that a “simple computer program” has already
left the four degree classes `(64,48)`, `(84,56)`, `(75,50)`, `(99,66)` with
special data.  It does not re-run or refine that program.

For the first three degree classes Moh observes `u_3=d_3-v_3=1` and applies
Propositions 6.4 and 6.3.  The transformed table on p.207 is:

```
n=16,m=12,M2=13,V2=3,      delta2=-1,   delta1=1/4,       J=X;
n=21,m=14,M2=16[18],V2=2[5],delta2=-1/2[-1],delta1=7/6[1/3],J=X;
n=15,m=10,M2=11,V2=3[2],  delta2=-1,   delta1=1/2[4/3],  J=X^2.
```

This carries all five bracket-expanded rows from the first three degree
classes forward; it eliminates none.  The `u_3=1` split is therefore a method
selector, not a pre-table filter.  Coefficient counts fall to 244, 373, and
202 respectively.

### `(64,48)` / transformed `(16,12)` (pp.207–209)

Moh uses this as the worked example for coefficient reduction:

- p.207 bottom chooses a major-disc root `sigma=pi t^(1/4)` and a minor-disc
  root `sigma^*=t^-1+a0+a1 t+a2 t^2+pi t^3`.
- p.208 defines a truncation `barsigma` ending in `pi t^(11/4)` and invokes
  Theorem 1.2 to expand `gbar` quartically and `fbar` cubically in the fourth
  approximate root `h`, with degree and order bounds.  Equations (1)–(5) on
  p.208 force special forms for `h,alpha_i,beta_i`, reducing to 17
  coefficients.
- p.208 bottom–p.209 top performs polynomial/Tschirnhausen replacements of
  `(f,g)` and expands in `h`.  The displayed identities for
  `beta_2 beta_3=gamma h+gamma^*` and `beta_2^3=delta h^2+delta^*`, with
  `deg_y gamma^*<4`, `deg_y delta^*<8`, reduce to 10 coefficients (p.209,
  paragraph after those displays).

These are invertible normalizations and case-specific approximate-root
constraints.  They reduce the coefficient search but do not eliminate this
numerical row on the page.  Its eventual impossibility is only covered by the
blanket assertion at the end of p.211.

### `(84,56)` bracket pair / transformed `(21,14)` (p.208)

After the first worked reduction, p.208 says only: “Similar arguments can be
applied to the second case to show the impossibility directly.”  Both bracket
alternatives are present in the transformed table, but no equations proving
their separate elimination are printed.  Therefore the source gives a
case-by-case assertion, not a general numerical condition extractable from
Appendix II.

### `(75,50)` bracket pair / transformed `(15,10)` (pp.208–211)

Pages 208–209 first state coefficient reductions for the third degree class:
22 `[15 or 13]`, then 12 `[10 or 7]`.  The detailed contradiction on
pp.210–211 explicitly handles only
`n=15,m=10,M2=11,V2=3` (p.210, second paragraph):

1. Normalize `f=h^2+2 beta=eta^-10` and write `g` as a Laurent/ fractional
   power expansion with constants `a,b,c,d`, where `b,c` are nonzero
   (p.210 before equation (1)).
2. Because `g` is a polynomial in `y`, all negative powers in `y^-1` must
   cancel.  Equations (2)–(4) on p.210 result, including
   `beta^2=alpha h+gamma`, a degree bound `deg_y gamma<5`, and two stronger
   cancellation identities.
3. The inverse section-6 transformation guarantees a minor disc.  Moh states
   that the major disc `D_2` has **precisely three subdiscs containing 2,2,6
   roots of `f`**, and `delta_1=1/2` forces the displayed forms of `h` and
   `beta` (p.210 last paragraph through p.211 equations (5),(6)).
4. Equation (3) yields `deg_y gamma<=2` (p.211 equation (7)).  Substitution
   gives three scalar coefficient equations.  Splitting `a_9=0` and
   `a_9!=0`, Moh obtains a contradiction to equation (3) in each case
   (p.211, Case 1 and Case 2).

This is the only fully displayed elimination in Appendix II.  The `2,2,6`
root partition is a genuine extra realization datum for this one transformed
row, but Moh derives it after fixing that row and after an inverse
transformation.  No theorem on these pages promotes it to a uniform numerical
condition for all skeletons.  The bracketed `V2=2` variant is not proved in
detail; it falls under the p.211 assertion that all other cases can be
computed directly.

### `(99,66)` (pp.209–211)

Moh says this fourth degree class has “complications.”  From the distribution
of roots of `g` in `D^*_2`, the leading polynomial `g_sigma(pi)` is either
(i) a power of a linear polynomial, or (ii) the ninth power of a cubic with
precisely two roots (p.209, paragraph beginning “In the fourth case”).

- In alternative (i), he transforms the data to
  `(n,m,M2,V2,delta2,delta1;J)=(27,18,21,8,-1,0;X^4)` and says the earlier
  method reduces to 10 coefficients (p.209 table and following sentence).
- In alternative (ii), p.209 gives a Laurent transformation
  `Omega: x->x^-1, y->a0+a1 x+a2 x^2+y x^3`, the leading monomials of the
  transformed `f,g,T_2,T_3`, and Jacobian `x`.  Page 210 says that examining
  solutions of `Omega(g)=0` in both Laurent fields `k<<x^-1>>` and
  `k<<y^-1>>` reduces the direct computation to 11 variables.

Neither alternative is actually contradicted in a displayed calculation;
both are swept into the p.211 final assertion.  The two-root cubic is a
case-specific leading-polynomial datum, not a uniform filter on `M_i,V_i`.

### Final assertion and what Appendix II does not contain

The last paragraph of p.211 says all other cases “can be computed directly as
above” and concludes no counterexample through degree 100.  There is no
printed computation for five of the six expanded p.202 rows, and no general
numerical theorem is stated that eliminates them simultaneously.

In particular, Appendix II contains:

- no expression `H=L_1^u L_2^v` and no `L_1,L_2` split;
- no new condition of the form `m | (...)`;
- no new sign or ordering restriction on the `M_i` beyond using the listed
  data and `m=-M_1`;
- no all-level root-count rule.  The only explicit count partition is `2,2,6`
  for the single transformed `(15,10,V2=3)` case;
- no independent “second point at infinity” filter.  Section 6 identifies
  `delta_s=-1` with more than one point at infinity in Corollary 6.1 (p.199),
  and the Appendix uses the resulting minor-disc geometry, but does not turn
  it into another pre-table scalar test;
- no pre-table elimination of excess numerical rows.  Its opening premise is
  already the p.202 table.

## Source-only verdict for OPEN[MOH-PROGRAM]

**Appendix II does not close OPEN[MOH-PROGRAM].**  It performs transformations,
coefficient-count reductions, and one detailed case-specific contradiction
*after* Moh's unexplained program has selected the six rows.  It cannot explain
how the program discarded other tuples.

The minor-disc pages expose two safe candidates to test against the census:
TOP-SPLIT-STRICT and TOP-RADIUS.  If neither accounts for the discrepancy, the
remaining source-motivated candidate from these pages is a full, levelwise
factor/root-multiplicity completion (rather than the selected-path orbit size
alone).  Appendix I's Proposition A.3 supports that direction, but a precise
level map is still OPEN; Appendix II provides none.
