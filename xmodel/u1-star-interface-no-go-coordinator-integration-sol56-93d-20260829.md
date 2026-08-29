# U1 pole-inflation interface no-go and td12 selector reset — binding integration

Date: 2026-08-29 UTC  
Coordinator: Sol 5.6  
Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`  
Lifecycle: `PROMOTED_INTERFACE_THEOREM / PCB_DERIVATION_REJECTED`

## 0. Binding disposition

Three independent whole-portfolio attacks agree on the quantified global
spine:

```text
JC2 false
  -> some globally GGV-minimal standard pair
  -> a Sigray normalization of that same pair, preserving td
  -> td >= 6
  -> a finite entry menu at each fixed td.
```

No promoted arrow bounds `td` above, selects `td=12`, selects type `(2,3)`,
selects the three-pole off-axis entry, selects a U1 merge, or produces a named
B25/S17 occurrence.  GGV minimality minimizes the global degree gcd/base
scale among counterexamples; it does not minimize topological degree.

The strongest new negative theorem is now different-model reviewed: the
promoted configuration-level interface itself admits pole-inflated abstract
U1 stars at arbitrarily large topological degree.  Therefore further
configuration arithmetic using only that interface cannot prove a `td`
ceiling or select `td=12`.

This is an interface no-go, not a counterexample to JC2 and not a claim that
any abstract configuration below is realized by a polynomial pair.

## 1. Reviewed abstract family `U1*(R)`

For every odd star arity `R>=3`, take type `(alpha,beta)=(2,3)` and `R`
identical pole entries

```text
(a,b,nu_P)=(1,2,3),  Lambda=4,  M_P=2,  w_P=3/2.
```

Then `td=4R`.  Join the pole-adjacent arrivals in one U1 equality star with
`mu=2`, `eps=k=lex=0`.  The reviewed U1 laws give, for admissible merge
indices `n>=5` with `n` congruent to `1` or `5` modulo `6`, a constant trunk state

```text
(w,M)=(3R/2,2).
```

This explicitly supersedes the producer's unqualified `n=+-1 mod 6`, which
accidentally included `n=1` from the separate U2 regime.  All recorded entry,
tree, merge, arithmetic, and source-mass axioms are satisfied.  In particular
the source-mass floor is saturated:

```text
td = 4R = R*max(beta,2*alpha).
```

At the reduced arithmetic/P1/lower-floor tier, the complete one-step dirty
terminal family is indexed by

```text
k | (3R-1),  k <= R-1,
```

and has

```text
nu_F = 3R + 2(3R-1)/k,
M_F = k+2,
w_F = (k+1)/(k+2),
psi = k+1,
lambda_floor = 3R-1,
budget = 4R-k-2,
slack = R-k-1.
```

The always-present `k=1` cell has

```text
(nu_F,kbar_F,X_F,M_F,w_F)=(9R-2,6R-1,9R-2,3,2/3),
slack=R-2,
B/A=3R/(3R-1)
```

in its nondegenerate vertex-local Proposition 8.1(iv) solution.  This `k=1`
member is sufficient for the no-go at every odd `R`.  Uniform local T1 for
arbitrary `k>1` is not asserted; `k=2` at `R=3` is separately reviewed prior
work.  The displayed floor fit is non-exclusion only, because actual dirty
weights may exceed their AF2 floors.  At that tier the budget becomes looser,
not tighter, as `td=4R` grows.  At `R=3`, `k=1` recovers B25 and `k=2`
recovers S17.  The familiar td12 sharpness is the smallest member of an
unbounded interface family.

The family is an abstract admissible configuration.  It asserts no actual
fibre, occurrence, source gluing, Keller map, degree attainment,
counterexample, or JC2 conclusion.

## 2. Pole-count budget disposition

The proposed inequality

```text
td >= s + sum_F wt(F)
```

(`PCB`) is not promoted.  Its proposed proof is false as a reading of the
reviewed Section 7 integration:

- the constant in the exact Euler integration is
  `chi_c(A^2)=1`, giving `td-1=sum_i integral_(U_i) w_i`;
- pole clusters of `g` are not points of the finite-value quotient lines
  `U_i` and do not replace that constant by their count `s`;
- the component-aware fibrewise Riemann--Hurwitz identity
  `sum_(non-pole infinity)(e_F-1)=2G-2c+td+s`, for `c` normalized fibre
  components of total genus `G`, concerns places at infinity, not the
  finite-value cv flags whose weights enter Corollary 7.1 (the familiar
  `2g-2+td+s` formula is the connected case);
- identifying those quantities would violate the campaign's
  flag/place/series firewall and gives incompatible magnitudes already on
  `U1*(R)`.

Accordingly:

```text
proposed RH/pole-cluster derivation of PCB: REFUTED;
PCB as a corollary of promoted Section 7: REFUTED;
PCB as a bare new inequality on actual Keller maps: UNSUPPORTED.
```

Do not continue PCB merely because it would kill the abstract family.  A
future extra-`s` theorem would require a genuinely new source-typed excess
or cluster-separation invariant and its own proof.

## 3. Strategy consequence

The global proof primary is no longer the compressed arrow

```text
minimal counterexample -> td12/U1 -> B25 or S17.
```

It splits into independent problems:

1. obtain an actual global degree/type/topological-degree ceiling or another
   realizability constraint not contained in the present configuration
   interface;
2. classify or exclude actual source-typed entries and merge skeletons across
   all remaining `td`, without assuming U1;
3. use td12/U1/B25/S17 only as a conditional laboratory after its antecedents
   are explicitly named.

The conditional td12 laboratory remains useful: it contains reviewed source
bridges and unusually tight budget fixtures.  It is not a universal bridge.
This reset supersedes prior live text that described
`TD12-U1-ACTUAL-LANDING` as merely a narrower spelling of the global gap.

## 4. Custody

```text
acd21ced9c2569b46b9f2123e9a7e106c552e62983eebb4408e4ddce32581f5c
  xmodel/td12-occurrence-coverage-attack-opus5-93d-20260829.md
19d15346303d23f10fdf3bae0fc153396434e4e8835585d063e98e3d6c95947d
  Opus producer body through BODY-END
444c309ef73968271ba0a0ae5d17396079fb24c25b5d72617bce05a19fa46177
  xmodel/u1-star-pcb-hostile-review-grok46-93d-20260829.md
36986889dd6f80ed5ed167b8e0ecdaa457fb0a580252f1edad4846c0e74d77a8
  Grok hostile-review body through BODY-END
1d79eeeed18949085e9adb7078b4a6f534e9474de6c83ed113aef4e659857f52
  xmodel/td12-occurrence-coverage-attack-grok46-93d-20260829.md
fc1c709d9defe5d9f89080f5fe24ec02d7f73c951e5eb0f4bb19edcbca6a7f14
  xmodel/td12-occurrence-coverage-attack-fable5-93d-20260829.md
2d30bbf12a4c2bbaff135cfc490d51b6f1521369a892d9876fb087edb5bec732
  xmodel/u1-star-pcb-independent-audit-sol56-93d-20260829.md
4073cc92bf44057018a42440de72b8865105a4c9f3d8825a20ec4de300013d09
  internal-audit body through its sealed-body marker
```

No actual occurrence, exit-price attainment, `PairRef`, source value,
degree ceiling, map, or counterexample is asserted.  No canonical file, case
source, AWS resource, or `jc2-lean` object was touched in preparing this
integration.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6622`.
- Body SHA-256: `0943feb5a4b44f778085978adea168b983ba66cffcc67a32f77ba1e5b3a4a924`.
- Frozen basis: `93db679d3160c957b0610297afccc1f2fad53125`.
