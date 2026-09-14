# Hostile audit of the first-support reconstruction

Scope: read-only review of `box/lib/descend_own.py` and
`theory-independent.md`, plus the frozen print. No library changes. The
metric comparison below records library SHA-256
`ca6932be023a84b5ac7e67e3a13efa93b54c211a3554a39d0aeda63119f75019`.

## 1. Material error found: dropped-tail child radii

The proposed geometric inverse radii and the library's child `def51_radii`
are inconsistent precisely in part of the p.174-dropped-tail case. The
independent driver `hostile_metric_audit.py` takes the frozen operative rows,
obtains the proposed candidate routes, and compares at every child level:

```text
before/at first nonzero index j: delta'_i = v-u/delta_i, i>=j;
after that coefficient: delta'_i = v-u-(u/delta_j)(1-delta_i), i<j.
```

These are physical contact formulas from inversion. Comparison with the
library's effective-chain Def5.1 product gives the following
**DETERMINED arithmetic counts**:

| u_s=1 candidate routes | Routes | Metric vs. formula |
|---|---:|---|
| No dropped n'-1 tail | 178 | Every radius agrees |
| Dropped tail | 42 | At least one radius disagrees |
| Dropped tail | 4 | Every radius agrees |

There are 224 candidate routes (two source rows have two routes), 692
individual radius comparisons, and 104 mismatching values. No non-dropped
route mismatches. `hostile-metric-audit.json` records every comparison.
These are counts of proposed routes and arithmetic tests, not realized pairs.

First failure: source `(108,72)`, M=(-72,84,104,106), V=(8,8,3).
It proposes j=2 and child n'=27,m'=18, raw M'=(-18,21,26), then drops
26=n'-1. On the remaining indices the physical formulas give
`(delta'_1,delta'_2)=(1/3,0)`, whereas `def51_radii` gives `(0,-2/5)`.
Consequently the earlier output field `child_radii` cannot be called the
child's established own radii on these dropped rows. Nor does installing
the terminal boundary V=d fix the discrepancy.

The p.174 Definition–Remark is explicit for the printed constant-Jacobian
theory. Extending its drop and terminal-radius mechanism to the descended
monomial-Jacobian situation requires a compatible argument. The usual
negative terminal-radius formula cannot just overwrite a zero or positive
physical contact computed by inversion. The independent fixed-chart obstruction in section5 now proves these
source rows incompatible; it does not license the unsupported dropped
formula as an own-data identification. Do not impose the desired negative radius as a
filter that manufactures different own V.

## 2. Full denominator before first support: no gap identified

The Galois argument is valid under its stated zero-centre hypothesis and
the actual Prop5.3 minimal-disc construction, rather than for an abstract
list of radius denominators alone.

At a zero-selected split of radius delta_r, the selected multiset consists
of roots of `g*T1*...*Tr` satisfying `ord(y)>delta_r`. All these polynomials
have coefficients in k((t)); this selection is invariant under the full
Galois group. Proposition5.3 p.180 defines D_(r-1) to be the minimal disc
containing this selected multiset. If its common centre first had a
nonzero term c*t^e with delta_r<e<delta_(r-1), Galois invariance of the
multiset would force invariance of that common coefficient. A noninteger
e would give a distinct conjugate coefficient, separating roots already
at e, contradicting the claimed minimal radius. Thus any such common
term is at an integer exponent.

After the source's allowable linear and constant normalization, the
relevant gap lies in (0,1), which contains no integer. Zero coefficients at
previous radii do not impose a ramified coefficient field. Hence at the
first nonzero support the orbit length is the full denominator of the
current radius. Replacing it with an incremental denominator from earlier
zero splits would admit spurious first coefficients.

This argument requires the selected **whole root multiset** of the
relevant g and quasi-approximate roots. Galois invariance of a numerical
V list or of one chosen Puiseux series would not suffice. The note does use
the whole selected multiset, so this distinction is satisfied in its proof.
At a source radius exactly zero the chosen constant can be normalized;
the argument then applies to subsequent positive gaps. This source-side
claim does not itself settle the dropped child's radius issue in section1.

Thus the empty route set is a necessary source-configuration obstruction
in the reduced source scope if the first-support alternatives are stated
as such. It is not an assignment of an arbitrary child's V by ex falso.
The observed 1,095 empty outer sets remain a different predicate from
U-NEGATIVE or C-TOP. This audit independently reviewed the implication,
but did not exhibit any pair realizing a nonempty route.

## 3. Why a first nonzero coefficient must occur

Prop5.6 pp.188–190 concerns a tower reaching D1 with general point
`sigma_1=pi*t^delta_1`. It concludes either a coordinate pair or simultaneous
degree reduction by an automorphism. Therefore an all-zero centre is
excluded for a reduced minimal counterexample source. It is not excluded
for arbitrary polynomial pairs merely satisfying the numerical row.

The current library is explicit about this `reduced_source` condition.
It should be included in every promoted obstruction or level-2 statement.
The proposition is not a theorem that all-zero towers cannot exist
without the reduced/non-coordinate scope.

## 4. Level2 identity is now geometric, subject to scope

If j is the first selected nonzero source coefficient, fix one inverse
initial coefficient. Local inversion has a nonzero derivative and maps
each deeper selected disc to a disc with the same root count, separately
for g and every retained quasi-approximate root. It preserves the per-disc
count, not the aggregate count over all conjugate inverse coefficients.
The metric transformation identifies the deeper disc radii; the exact
agreement on all 178 non-dropped u_s=1 candidate routes is an independent
check of that indexing.

Since j>=2, D1 lies after the first selected nonzero coefficient, so
`#roots(g' in transported D'_1)=#roots(g in source D1)`. Only after that
geometric identification may one use n'/d'_2=n/d_2 to conclude
`V'_2=V_2`. This is materially stronger than the old normalizer-equality
argument. Subject to a licensed descendant and the stated transported
disc identification, the elementary U-NEG count contradiction is valid.

The phrase “own V” needs one further clarification: Definition5.1 data
belong to a **chosen major-disc tower**, not uniquely to the underlying
polynomial pair. The reconstructed vector here is the vector of the
tower transported from the source row's selected tower. It does not
classify every other possible child major-disc tower. This limitation
does not spoil a contradiction for the transported disc, which would
still have to exist with its counted roots.

## 5. Fixed-chart finite-pole obstruction: the translation control is resolved

The refined argument uses the squarefree factor in the **retained**
T_(s-1), and only one licensed monic chart. It does not apply the monicity
assertion anew after every arbitrary source translation. This resolves
this audit's earlier single-residue translation concern for the 90 rows.

Write r=s-1. On a dropped row, u_s=1 and n-M_r=d_s, so the source radius
is delta_r=0. Proposition4.6 p.170(2) gives the leading polynomial

```text
T_(r,sigma)(xi) = p(xi)^A q_0(xi),
A=(-mu_r+M_r-n)/d_r,
deg(q_0)=V_s(n-M_r)/d_s=V_s.
```

Conclusion(3) states that q_0 has distinct roots. I independently checked
this display from the fresh `hostile-p170.png` render and recomputed the
arithmetic on all 90 rows. **DETERMINED:** A is an integer between 13 and
341; all are positive, so q_0 actually divides the leading polynomial
and no cancellation can delete its roots. The q_0-degree histogram is
`{3:61, 4:21, 5:5, 6:2, 7:1}`. All 90 have u_s=1 and delta_r=0. The
records are in `finite-pole-audit.json`.

Consequently the retained polynomial T_r has source branches with at
least three distinct finite constant residues y->C as x->infinity.
Whichever single constant normalization is used for the licensed chart,
at most one of these residues can become zero. Choose a branch with
C!=0. For the **fixed** Prop6.3 substitution,

```text
gamma=y^(-1/u_s),
pi=(y-beta*x-e-A(gamma))/gamma^v_s,
```

gamma tends to a finite nonzero value C^(-1/u_s). The denominator
and A(gamma) are regular there, while beta*x has a pole and beta!=0.
Thus pi has a pole. But Prop6.3(1),(2) supplies T_r(sigma) as a polynomial
in gamma that is monic in pi. Every pi-root is integral over k[gamma];
its extension to the local valuation ring at any finite gamma value has
nonnegative valuation. A root with a pi pole is impossible. If y is
identically constant along the source branch, the same contradiction
follows directly: a monic polynomial specialized at finite gamma cannot
vanish on a pole-valued pi series.

Prop6.4 licenses the descent for u_s=1, as holds on all 90 rows. This is
therefore a separate necessary-source contradiction using the full
printed Prop6.3 polynomiality and monicity conclusions. It does **not**
repair or justify the invalid dropped-tail radius formula in section1.
It says that these necessary source rows cannot produce such an actual
licensed descendant. Their abstract inverse-count tuples and failed
formula checks may be retained diagnostically; they should not be
presented as data of realized children.

The previous translation concern remains a reason to avoid the stronger
claim that the z-leading coefficient must be a power centred at every
possible translated origin. That stronger claim is unnecessary here.
Multiple distinct residues cannot all be removed by the one affine
constant normalization in a fixed licensed chart. No additional global
normalization assumption is used in the finite-pole argument.

## 6. API details to keep explicit

The finite vectors are a **necessary outer set**, with correlations across
levels retained. Orbit capacity is not an existence theorem for the full
differential-equation tree or a polynomial pair. A singleton nonempty set
is conditionally DETERMINED for a compatible actual source. An empty set
is not a scalar datum. Local forced-top calculations may survive as local
implications even when the complete source route is incompatible.

The library's zero orbit check should explicitly require P>=V_i as well
as divisibility if the public API accepts arbitrary Skel-like inputs.
For the already screened operative rows this inequality follows from
the parent's necessary data, so its omission changes none of the audited
campaign counts.

No new exit-price assertion is made here.
