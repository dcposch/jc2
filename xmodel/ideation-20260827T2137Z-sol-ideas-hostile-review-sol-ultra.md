# Hostile review of Sol ideas `EXIT-DIFF` and `BI-FACE-SRC`

**Reviewer lane:** Sol Ultra  
**Date:** 2026-08-27  
**Scope:** the two proposal cards in
`ideation-20260827T2137Z-sol.md`, judged against the post-seal truth delta,
the reviewed `C74-PLACE` / `EXIT-RPMC(C)` correction, and the reviewed
finite-end identity.  This is a proposal review, not a JC2 proof or
counterexample.

## 0. Custody

The assigned sealed target matches its required SHA-256 exactly:

```text
2112a0ad5fbc4fcc5d1a26efd725c01500186f6299b5b591e2849eb0a865ac32
  xmodel/ideation-20260827T2137Z-sol.md
```

The load-bearing review inputs also match the hashes recorded in the truth
delta:

```text
968b42ced94bd6c59b33bfdab30677e2ad6ad91a349fc978a271c01083d11e7d
  xmodel/g2-c74-place-exit-rpmc-hostile-review-opus5-20260827.md
0f201502716ca9c9bf33718412739e0254981c2eb7204657dc78ee7fbcd653c1
  xmodel/g2-finite-end-asymptotic-monodromy-connection-sol-ultra-20260827.md
```

No heavy computation or external job was used.  No `jc2-lean` path was
inspected, listed, searched, or modified.

## 1. Executive verdict

### `EXIT-DIFF`: **REFUTE the claimed bridge; REFILE a narrower conjecture**

The current card does not survive the post-seal correction as written.

1. Its dependence on the monolithic `C74-PLACE` corridor must be deleted.
   Native face-power custody and multiplicity conversion are available, but
   truncation compatibility and the deck/leaf-place bijection remain open;
   chart coverage belongs to the independent exact-pair constructor.  No VGG
   Corollary-7.4 object supplies the missing physical chart.
2. `EXIT-RPMC(C)` is equivalent to `RPMC(C)` once its clause 1 is assumed.
   Renaming discrepancy subtrees by their first exits localizes the hard
   inequality but does not weaken it.
3. The proposed `E_xi` is not presently an invariant module and
   `(Omega_(Cbar/P^1))_xi` is not typed: `xi` is a center in a surface
   resolution, whereas the differential stalk is indexed by a point of the
   completed fibre curve.
4. Even granting every typing and injection claim, summation yields only

   ```text
   total exit mismatch <= C * (2g - 2 + 2td),
   ```

   whose right side already grows linearly with `td` and with the unbounded
   genus.  This is not `RPMC(C)` and gives no noncircular `td` bound.

There is a defensible residual idea: on the minimal exact-pair resolution,
define an invariant *numerical* exit energy for each essential exit subtree
and compare it with the sum of local different exponents at its boundary
leaves.  That would be a useful support/falsification lemma, but its global
consequence is only an a posteriori topology-dependent estimate.

### `BI-FACE-SRC`: **KEEP as a provenance/separation audit, not yet a client**

The coefficient-source comparison is useful and correctly refuses transpose
as a same-pair identification.  It is not yet a new simultaneous
shared-source fixture.  A commuting coefficient table can prove a separation
or clear a type gate; consistency of its linear rows does not prove that the
two nonlinear compiler loci have a common raw point.  Moreover, the displayed
quotient has unresolved variance: for the usual compiler-to-source maps the
simultaneous object is a fibre product, not a sum of naively pulled-back or
contracted ideals in `R_raw`.

The right label now is **NEW campaign provenance audit**.  Promote it to a
shared-source client only after exact source morphisms, private compiler
variables, normalizer choices, localizers, and the full scheme-theoretic fibre
product are written down.

## 2. What the `C74` / exit correction deletes

The proposal's composition

```text
intrinsic two-chart forest
  -> C74-PLACE
  -> E_xi -> different
  -> EXIT-RPMC(C)
```

cannot be repaired by changing the chart label.  The reviewed decomposition
is:

```text
L1  native face-power custody       available
L2  multiplicity conversion         available after naming the convention
L3  fibre-truncation compatibility  open
L4  chart coverage                   exact-pair constructor, not VGG
L5  deck/leaf-place bijection        open
```

Thus an exit/different statement must start directly from a
coefficient-complete fixed pair and an exact simultaneous resolution.  It may
not use a Corollary-7.4 corridor to obtain a chart, and it must not use
`C74-PLACE` as a black box hiding L3--L5.  In addition, because

```text
EXIT-RPMC(C) <=> RPMC(C)     (under EXIT-RPMC clause 1),
```

an exit reformulation earns no cheaper proof target merely by identifying the
first nonzero center.

## 3. The narrow intrinsic version of `EXIT-DIFF`

An intrinsic statement is possible, but it is not the module statement in the
proposal.  The minimum defensible setup is:

1. Fix the **ordered** Keller pair `(f,g)` with
   `deg f=B*alpha`, `deg g=B*beta`, and retain the corrected component sort
   `(P,Q)=(g,f)` and `(m,n)=(beta,alpha)`.  Do not identify another pair by
   signed transpose.
2. Take a minimal common principalization of the two homogenized pencils at
   infinity, or equivalently their canonical weighted base-point clusters.
   Record the full proximity relation, not just parent edges.  At every
   essential center `p`, put

   ```text
   delta_p = R_p/alpha - S_p/beta.
   ```

3. Contract subdivisions caused only by superfluous blowups.  A zero corridor
   is then a maximal proximity-closed connected set with `delta_p=0`; an exit
   is an adjacent essential valuation with nonzero discrepancy.  This makes
   “first exit” independent of a chosen blowup presentation, conditional on
   invariance of the canonical cluster construction.
4. Resolve the generic fibre and prove a leaf/place map.  For an exit subtree
   `T_xi`, let `B_xi` be its set of boundary places and require the `B_xi` to
   be disjoint in the energy decomposition.  Put

   ```text
   M_xi = (1/2) * sum_(p in T_xi) delta_p^2,
   d_S  = length Omega_(Cbar_a/P^1),S.
   ```

   Here `d_S=e_S-1` at a finite end and `d_S=lambda_S-1` at a pole, using a
   local coordinate at infinity on the target.

Only after these choices is the scalar conjecture

```text
EXIT-DIFF-intr(C):
  M_xi <= C * sum_(S in B_xi) d_S
```

well typed.  It is intrinsic to the fixed pair if the minimal-cluster and
leaf/place invariance assertions are proved.  It does not depend on the
refuted other-chart reading and does not require the name `C74-PLACE`.

This is the narrowest salvage.  Calling `M_xi` the length of a module adds no
content and currently creates errors: `M_xi` is generally rational, while
the length of a finite module is integral.  Multiplying by
`2 alpha^2 beta^2` makes an integer but does not canonically manufacture a
module or a morphism.

## 4. Why `E_xi` is not invariant or typed

The card leaves six independent gaps.

1. **Different ambient local rings.**  Point-basis data live at infinitely
   near surface centers.  `Omega_(Cbar_a/P^1),S` lives over the DVR
   `O_(Cbar_a,S)`.  Until an exit subtree is mapped to one or more boundary
   points, `(T_q)_xi` is meaningless.
2. **No canonical module operation.**  A difference of two normalized
   multiplicity vectors is numerical data.  It supplies neither an inclusion
   of ideals nor a kernel/cokernel whose length is the squared discrepancy.
3. **Integrality.**  `R_p/alpha-S_p/beta` and half its square need not be
   integers.  Fitting length cannot equal the proposed energy without an
   explicit scaling convention and a reason that the scaled object is
   functorial.
4. **Presentation dependence.**  “Last common power” and “first
   nonproportional transform” change under insertion of redundant blowups,
   translations, unit rescalings, and changes of a primitive common root.
   Essential valuations or canonical complete ideals must replace those
   phrases.
5. **Descent and double counting.**  Kummer presentations can represent one
   place several times, several exits can feed one place, and a satellite
   center sees more than its parent.  A full deck quotient, reduced
   denominator law, proximity closure, and disjoint energy partition are
   prerequisites, not consequences of a different comparison.
6. **Fitting ideals do not solve the map.**  On a curve DVR,
   `Fitt_0 Omega=(t^d_S)` is intrinsic.  Comparing it with a surface-side
   Fitting ideal still requires transporting both ideals to the same DVR and
   proving the appropriate containment.  A numerical length inequality is
   not a natural injection.

The quickest invariant test is therefore not a large local-algebra
calculation.  On one coefficient-complete control, record the essential
cluster, insert one superfluous blowup, and apply one permitted coordinate/unit
change.  The exit classes, their total scaled energies, their leaf sets, and
their `d_S` values must be unchanged.  Any failure stops the module proposal.
Among the resulting rows, an exit with nonzero mismatch landing only at
`d_S=0` is an immediate decisive falsifier.

## 5. The Riemann--Hurwitz step is circular as a degree budget

For the same connected generic fibre, the reviewed exact identities are

```text
deg Diff(q) = 2g - 2 + 2td,
sum_(S in N) e_S = td + b1(C_a) - 1,
b1(C_a) = 2g + s - 1,
deg Diff(q) = td + sum_(S in N) e_S - s,
```

where `s` is the total number of punctures.  The last display is a change of
variables, not an independent upper budget.

Suppose every missing definition is supplied and the local inequalities sum
without duplication.  They give only

```text
M_exit <= C * deg Diff(q)
       = C * (2g - 2 + 2td).
```

Even under the most optimistic identification
`M_exit=E_MR=td/(alpha*beta)`, the result is

```text
(1/(alpha*beta) - 2C) * td <= 2C * (g-1).
```

For `C >= 1/(2 alpha beta)` it has no upper-degree content at all.  For a
smaller constant it still needs an independent genus bound and a favorable
sign; neither is supplied.  The scalable reviewed control
`q(z)=z^d-dz` on `P^1` has `deg Diff=2d-2` and satisfies the finite-end
identity for every `d`, illustrating exactly why Riemann--Hurwitz alone does
not cap the degree.  It is a topology countermodel to the inference, not a
claimed Keller surface counterexample.

The per-root gap is sharper.  To derive

```text
M_i <= constant * mu_i/B
```

from a different comparison, one would also need

```text
sum_(S assigned to root i) d_S <= K * mu_i/B.
```

Summing that missing inequality bounds the *assigned* different by `K`.  If,
as the proposed global-budget rhetoric requires, the assignment covers the
different, Riemann--Hurwitz already gives `td <= (K+2)/2`; the added estimate
itself contains the desired ceiling.  If the assignment does not cover the
different, Riemann--Hurwitz gives no bound of that selected subsum by
`mu_i/B`.  Either way, nothing in the finite-end identity supplies the
missing per-root estimate.

The only honest promoted consequence of `EXIT-DIFF-intr(C)` would therefore
be a topology-dependent mismatch estimate and the local support rule
“nonzero mismatch requires positive ramification charge.”  Delete every
claim that summing it gives `EXIT-RPMC(C)`, `RPMC(C)`, or a cofinal `td`
bound.

## 6. `BI-FACE-SRC`: audit versus actual shared-source scheme

The proposed source firewall is directionally correct: the upper branch-P
fixture and lower LF40 fixture must not be identified by transpose, common
`(8,28)` numerology, or matching slot names.  Exact coefficient provenance is
the cheapest way to catch that error.

However, a common ring can always be manufactured formally, so existence of
some `R_raw` is not evidence.  What matters is whether both compilers are
derived from one universal ordered polynomial pair with their actual chart
maps, normalizers, gauges, omitted coefficients, auxiliary root variables,
and nonvanishing guards retained.

There are two different variances:

* If a raw pair **deterministically compiles** to both fixtures, there are ring
  maps from the compiler coordinate rings into `R_raw`; only then does
  extending the two compiler ideals to `R_raw` and summing them have the form
  displayed in the proposal.  Such deterministic maps are not currently
  given and may fail because root/chart and gauge choices require auxiliary
  variables or covers.
* In the usual situation, the upper and lower parameter schemes have source
  maps to the raw-pair scheme.  Write their localized coordinate algebras as

  ```text
  U = (A_U/I_U)_[s_U^-1],
  L = (A_L/I_L)_[s_L^-1]
  ```

  over `R_raw`.  The simultaneous object is then

  ```text
  X_bi = Spec(U tensor_(R_raw) L),
  ```

  followed, if desired, by exact elimination to its scheme-theoretic image in
  the raw source.  Adding contractions of `I_U` and `I_L` inside `R_raw`
  loses private lifts and is not equivalent to this fibre product.

This produces three distinct gates:

```text
G0  coefficient provenance and commuting-square audit
G1  consistency of fixed/linear face equations with every guard retained
G2  nonemptiness of the full localized upper/lower fibre product
```

`G0` or `G1` failure is a useful, exact separation.  Passing them only
licenses construction of `G2`; it is not a nonempty common-source locus.
Only `G2` is a genuinely new shared-source finite client, and even a point of
`G2` is merely a common finite fixture until prolongation and receiver/source
completeness are separately proved.

## 7. Cheapest exact provenance table

The cheapest adequate artifact is one sparse table, `BI-FACE-PROV-R0`, over a
frozen canonical raw coefficient ring.  Its global header must record the
ordered components, degree/support convention, both chart substitutions,
homogenization/dehomogenization, component sort, normalizer/gauge variables,
and all unit/localizer assumptions.  Then include one row for every compiler
slot that is live, fixed, or forced to zero in the fixed/linear layer:

| field | required content |
|---|---|
| side / source row | upper or lower, compiler slot, and originating equation |
| raw key | ordered component and raw monomial coefficient(s) |
| exact pullback | the full expression in raw coefficients and normalizer variables; not merely a monomial label |
| state | live, fixed value, forced zero, derived, absent, or omitted-with-proof |
| chart/orientation | exponent map, sign/scalar, and component sort used for this slot |
| guard | denominator, saturation factor, root/deck choice, and required nonvanishing |
| cross-verdict | identical expression, compatible equation, collision, or genuinely unrelated |

The “exact pullback” column is essential because translations and gauge
changes mix raw coefficients; a table containing only original monomial names
can falsely report agreement.  “Absent” must never be treated as “zero.”  It
is enough to enumerate slots touched by the fixed/linear equations provided
all other raw coefficients are explicitly declared free and unused; there is
no need to import either nonlinear determinant ideal at this stage.

From the table, generate the two sparse exact linear systems and row-reduce
their union over the declared exact base field, with separate checks that no
guard is forced to zero.  The first contradictory raw coefficient, component
swap, sign, exponent, or normalization is a decisive separation.  A
consistent system is only `G1 PASS`; the next artifact must be the localized
fibre product above.

## 8. Final disposition

| proposal | disposition | narrowest promotable result | cheapest next test |
|---|---|---|---|
| `EXIT-DIFF` | **REFUTE as an `RPMC/td` bridge; REFILE** | an intrinsic scalar exit-energy versus local-different conjecture on a minimal exact-pair resolution | redundant-blowup/coordinate invariance table, then test all zero-different leaves first |
| `BI-FACE-SRC` | **KEEP as audit; not yet a client** | exact proof of coefficient-level separation or compatibility without transpose | `BI-FACE-PROV-R0` plus exact linear consistency and guard replay |

No allocation raise for a degree-ceiling lane is justified by `EXIT-DIFF`.
`BI-FACE-SRC` deserves desk-scale audit time because a failure prevents a
false composition; nonlinear shared-source algebra should wait until the
provenance gate and the variance of the source maps are settled.
