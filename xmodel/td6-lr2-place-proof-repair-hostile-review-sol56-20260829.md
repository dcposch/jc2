# Hostile review: td6 LR2 place-versus-series proof repair

Date: 2026-08-29  
Reviewer: Sol 5.6  
Target: `xmodel/flag-place-series-consumer-audit-sol56-20260829.md`, §3.3  
Verdict: **PASS WITH ONE REQUIRED EXPLICIT BRIDGE AND ENDPOINT NARROWING**  
Scope: the promoted td6/LR2 local x-side consequence only

## 0. Verdict

The proposed two-mode repair is mathematically sound at the current LR2
scope.  Once the actual-weight budget has independently established one
x-side critical-value vertex `G` and `kappa_G=1`, exact Eggers--Wall
definitions prove:

1. every distinct x-side place has the same cv vertex `G`, hence any two
   such place rays agree through height `pi(G)`; and
2. every conjugate Puiseux representative of each one place agrees through
   that height, because `kappa_G=1` excludes a characteristic exponent at
   or below `pi(G)` under Notation 3.5's post-characteristic convention.

Thus the advertised common x-side truncation and no-characteristic-through-
`G` conclusion survives.  No LR2 descendant named in the target changes
verdict.

One sentence in the proposed repair is too compressed to be accepted
literally:

> “Definition 3.3 makes their flags at G's height distinct.”

A point of a place ray at a chosen height is not automatically a cv flag.
The missing bridge is nevertheless already available and exact for every
filed td6 carrier: its recorded y-side pole vertices exhaust the full
Proposition 5.8 pole mass `td=6`; hence no x-side place is a `g`-pole.
Proposition 7.2 then gives a cv vertex on every x-side place ray, and the
already-proved uniqueness of the x-side cv set forces every one of those
vertices to equal `G`.  Only after this bridge may Definition 3.3 be used.

The endpoint must also be stated precisely.  The proof gives agreement
**through and including** height `pi(G)`.  Two distinct places with contact
exactly `pi(G)` may split immediately above `G`; and a first characteristic
exponent may occur strictly above `G`.  LR2 neither excludes nor needs to
exclude either event.

## 1. Exact custody

Hashes recomputed in this session:

```text
ae3b561ef8e70f527391291bece8b5df308ed2acd4bb0e714f0f32f014510f3a  xmodel/flag-place-series-consumer-audit-sol56-20260829.md
0a1a649289dc48715b93c34df3c93337ab42a6fce5e923b4cd1dabd81239890c  ladder/SHEET6-LROOT.md
26b9bbf69a581885c62926cf0a8411463e70ea64f2c0e3b6f717f8a920eb4702  ladder/SHEET6-LT-REVIEW.md
59a2fa489f7f999b24aabc4c707254b7e54f8db02d69690226754e3224f9bdda  ladder/SHEET6-III.md
c253bd12d205eed7c01e42a21204c5735d0f5cba70dce1d962fb8744dbd95eb6  xmodel/sigray-section7-weighted-euler-inequality-repair-sol-ultra-20260828.md
727f58506af4ff36f6a8c39bb83420c5077c2e4872e6e48bd42ec165c2323aa8  xmodel/sigray-section7-weighted-euler-inequality-hostile-review-terra-20260828.md
c31a611d793533dce55159d9e2cb219f802e4a755bfd03f50c3547db101ea381  xmodel/sigray-section7-weighted-euler-canonical-integration-map-terra-20260828.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
```

The target's sealed body hash is
`300a0efff1960a15335c2e61a8f42bcd2d9ea27dab99b4694480f0fa572b9444`.

Exact source clauses checked directly in `refs/sigray_full.pdf`:

- Definition 3.1, printed p. 10: characteristic indices
  `e_0=kappa`, `beta_j`, `e_j=gcd(e_(j-1),beta_j)`, with every genuine
  characteristic step strictly decreasing `e`;
- Definition 3.2 and Statement 3.2, pp. 10--11: contact and the selected
  place-series representatives;
- Definition 3.3 and Notation 3.1, p. 11: two place rays agree at height
  `u` exactly when `u<=O(P,Q)`;
- Notations 3.4--3.5, p. 12: at a characteristic endpoint
  `alpha_j<=u<alpha_(j+1)`, so `kappa_F=kappa/e_j` uses the
  **post-jump** denominator at equality;
- Proposition 3.1, pp. 14--15: reduced-pattern degrees and root
  multiplicities count cover-level Puiseux series, not cv flags;
- Statement 3.13, p. 16: a unique `d_f=0` height on each place ray;
- Proposition 5.5 and Proposition 5.8, printed pp. 26--28: `g`-poles are
  exactly rays meeting `T_(a,pole)`, and their positive pole masses sum to
  `td(f,g)` on every fibre;
- Proposition 7.2, p. 36: `g(P)` is finite iff the ray of `P` contains a
  cv vertex;
- Corollary 7.1, p. 39, used only through its reviewed actual-weight
  replacement `(C7.1*)` for pairwise distinct cv vertices;
- Statement 9.4's x-side slope/psi argument, p. 49, with its numerical
  inequality now sourced through `(C7.1*)`, not the invalid printed
  equation `(22)`.

The relevant campaign text is `SHEET6-LROOT.md:156-182,210-225,251-258`,
its review `SHEET6-LT-REVIEW.md:70-98,356-361`, and the Section 7 integration
map `:397-450`.

## 2. What LR2 establishes before any place/series argument

For every filed td6 survivor carrier,

```text
td-1=5,          sum(lambda)=2,
R in {3,4},      psi=R-1 in {2,3},
slack=5-2-psi in {1,0}.
```

Every x-side cv vertex `H` has `pi(H)>=R`: at `(0,x)`, the `f`-order is
`k_f`, the pattern degree is at most `l_f`, and a ray cannot reach order
zero before height `k_f/l_f=R`.  Its positive integral `(C7.1*)` cost is

```text
kappa_H*(pi(H)-1) >= kappa_H*(R-1).
```

There is at least one x-side cv vertex.  The already filed y-pole data have
positive Proposition 5.8 masses `6` in the single-pole carriers and `3+3`
in the two-pole carriers.  They exhaust `td=6`, so Proposition 5.8 permits
no x-side `g`-pole.  Every x-side place is therefore `g`-finite, and
Proposition 7.2 supplies a cv vertex on its ray.

Apply `(C7.1*)` to the two already-distinct y exit flags together with the
set of distinct x-side cv vertices.  Two x-side cv vertices would spend at
least

```text
2*psi > psi+slack = 5-sum(lambda),
```

and one x-side vertex with `kappa>=2` would spend the same impossible
amount.  Consequently, without any clustering premise,

```text
T_(a,cv) intersect T_(a,x) = {G},
kappa_G=1,
R <= pi(G) <= R+slack.
```

This is exactly the portion that the weighted Section 7 integration map
records as surviving.  It uses a set of distinct cv vertices, never a count
of cover-level Puiseux series.

## 3. Distinct places: the exact Definition 3.3 argument

Let `P` be any x-side place.  By the pole-exhaustion argument above,
`g(P)` is finite.  Proposition 7.2 gives a cv vertex `H_P` on `I_P`.
The x-side cv set is `{G}`, hence

```text
H_P=G                                                    (3.1)
```

for every x-side place `P`.

Now take two distinct x-side places `P,Q`.  Equation (3.1) says

```text
G=I_P(pi(G))=I_Q(pi(G)).
```

By Definition 3.3 this equality is equivalent to

```text
pi(G) <= O(P,Q).                                        (3.2)
```

Thus their selected place-series representatives agree through height
`pi(G)`.  This is stronger and cleaner than saying that a split “would make
two flags at G's height”: it proves that `G` lies on every x-ray before it
invokes contact.

Endpoint control is exact.  If `O(P,Q)=pi(G)`, Definition 3.3 identifies
the two rays at `G` and separates them for every larger height.  Such a
split immediately above `G` is allowed.  A split at any smaller contact
would contradict (3.2).

No statement here applies no-remerging to conjugate representatives of one
place.  They are handled separately below.

## 4. One place and its conjugate Puiseux representatives

Fix an x-side place `P` whose Puiseux characteristics are

```text
(kappa,beta_1,...,beta_s),
e_0=kappa, e_j=gcd(e_(j-1),beta_j), alpha_j=beta_j/kappa.
```

Write `G=I_P(u)` with `u=pi(G)`.  Notation 3.5 chooses the unique `j`
such that

```text
alpha_j <= u < alpha_(j+1)
```

and defines

```text
kappa_G=kappa/e_j.                                     (4.1)
```

Every genuine characteristic step is strict: Definition 3.1 chooses
`beta_j` not divisible by `e_(j-1)`, hence
`e_j<e_(j-1)`.  Since `kappa_G=1`, (4.1) gives `e_j=kappa=e_0`, so
necessarily `j=0`.  Therefore

```text
u < alpha_1.                                           (4.2)
```

In particular a first characteristic exponent exactly at `u` is excluded:
Notation 3.5 would use `j=1` at equality and would give `kappa_G>1`.

Equivalently, every nonzero series coefficient of index at most `kappa*u`
has index divisible by `kappa`.  The deck transformations of the common
Puiseux cover therefore fix all coefficients through height `u`; all
conjugate representatives of `P` have the same truncation through `G`.

Combining this with (3.2), all x-side places and all cover conjugates of
each place form one common Puiseux-series cluster through and including
height `pi(G)`.  This does **not** say they are one place or one global
series, and it says nothing above `G`.

## 5. Exact replacement wording

Replace the last three sentences of the LR2 proof beginning with “A split
of the x-side f-tree...” and qualify the “equivalently” clause by the
following text:

> The preceding budget argument establishes
> `T_(a,cv) intersect T_(a,x)={G}` and `kappa_G=1` without any
> no-splitting premise.  For each filed carrier, the recorded y-side pole
> vertices already contribute all of `td=6` in Proposition 5.8, so no
> x-side place is a `g`-pole.  Proposition 7.2 therefore assigns a cv
> vertex `H_P` to every x-side place `P`; uniqueness forces `H_P=G`.
> Hence for any two x-side places `P,Q`,
> `G=I_P(pi(G))=I_Q(pi(G))`, and Definition 3.3 gives
> `O(P,Q)>=pi(G)`.  Distinct place rays thus agree through `G` (they may
> split immediately above it if equality holds).
>
> Fix one such place with characteristics
> `(kappa,beta_1,...,beta_s)` and denominator sequence `e_j`.  If
> `alpha_j<=pi(G)<alpha_(j+1)`, Notation 3.5 gives
> `kappa_G=kappa/e_j`.  Since every characteristic step strictly lowers
> `e_j` and `kappa_G=1`, one has `j=0` and
> `pi(G)<alpha_1`.  Thus no conjugate shedding occurs at or below `G`,
> and all conjugate Puiseux representatives of each place agree through
> `G`.  Together, all x-side Puiseux representatives have one common
> truncation through height `pi(G)`.
>
> In a slack-zero carrier the separate slope-equality argument gives
> `pi(G)=R` and retains full `f`- and `g`-pattern degrees below `G`.
> That degree statement is not inferred merely from the existence of one
> flag.

The LR2 statement itself should read:

> The x-component has exactly one cv vertex `G`, with `kappa_G=1` and
> `R<=pi(G)<=R+slack`.  Every x-side place ray and every conjugate
> Puiseux representative has the same truncation through `G`; equivalently,
> pairwise place contact is at least `pi(G)` and no characteristic exponent
> occurs at or below `pi(G)`.  Splitting or a first characteristic exponent
> strictly above `G` is not excluded.  In the slack-zero case,
> `pi(G)=R`, and the independent slope equality retains the full `f`- and
> `g`-pattern degrees below `G`.

This wording is source-exact and avoids claiming either one place or one
global Puiseux series.

## 6. The separate line-224 wording

The target's proposed repair of `SHEET6-LROOT.md:223-225` is also sound,
with one useful precision.  Replace

```text
single-orbit pattern, NO series leave (all conjugates), no new cv mass
```

by

```text
the single cyclic direction-orbit creates no distinct place/direction-orbit
exit at this node, hence contributes no new first-separation cv flag here;
this alone does not exclude conjugate shedding within the continuing place.
```

Statement 3.18 licenses the orbit-level formulation: among the cyclic roots
of one nonzero `nu`-orbit, exactly one covered representative defines the
tree continuation.  A denominator jump may still occur without a second
tree direction.  Because the superseded literal `(22)` ledger is no longer
used, this wording proves only “no new exit flag here,” not zero change in
the eventual actual weight of the continuing flag.

## 7. Hostile controls

Three near-models delimit the conclusion.

1. **One place, several conjugate series, first characteristic above `G`.**
   Here `kappa_G=1` and there is one flag, yet there are several global
   conjugate Puiseux series.  They agree through `G` and split later.  This
   is allowed and refutes any wording “one flag means one series/place.”
2. **First characteristic exactly at `G`.**  Notation 3.5 uses the
   post-jump `e_1`, so `kappa_G=kappa/e_1>=2`.  The budget excludes this
   case.  This tests the inclusive endpoint in the repaired theorem.
3. **Two places with `O(P,Q)=pi(G)`.**  Definition 3.3 makes both rays
   contain `G` but separates them at every larger height.  This is allowed
   and tests that LR2 proves agreement through `G`, not beyond it.

A fourth dependency control is structural: if the filed pole data did not
exhaust Proposition 5.8, an x-side `g`-pole could lack a cv vertex and the
argument “every x-ray contains `G`” would fail.  Pole-mass saturation is
therefore a required td6-carrier hypothesis, not disposable exposition.

## 8. Remaining scope limits

- The result proves a common truncation, not a unique puncture, place,
  cover sheet, or global Puiseux series.
- It controls only heights at or below `pi(G)`; distinct-place separation
  and characteristic shedding may occur strictly above `G`.
- `kappa_G=1` is a local denominator decoration at `G`, not a claim that
  every place has global pole multiplicity one.
- The full `f`/`g` pattern-degree conclusion in slack-zero carriers remains
  the separate slope-equality corollary.  The place/series repair does not
  strengthen it and supplies no slack equality in the slack-one carriers.
- The proof uses reviewed `(C7.1*)`, not printed Proposition 7.5 `(22)`,
  literal `delta_a`, or a transported fixed `kappa`.
- It assumes the filed td6 survivor carrier and its pole/exit data; it is not
  an exhaustive root-aware book theorem or a source-landing theorem.
- No coefficient gluing, centering, two-chart compatibility, polynomial
  realization, degree ceiling, `G2`, or JC2 conclusion follows.

No canonical file, engine, round artifact, or source was edited.  No web,
AWS, or heavy computation was used.

---

Report-body SHA-256 (all bytes strictly before the final separator):
`a68ea0c29b7af39c63d9b2216855b8854483eb962f39ec8b007d27c0d81edaa8`.
