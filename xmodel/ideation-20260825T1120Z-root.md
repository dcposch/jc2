# JC2 full-spectrum ideation — root coordinator

Date: 2026-08-25T11:20Z  
Packet: `xmodel/ideation-20260825T1120Z-state.md`  
Method: blind whole-portfolio scan.  I did not read another `1120Z`
submission before sealing this report.  Results received after the packet
cutoff are not consumed here.

## 1. Disposition vector over all numbered avenues

Legend: `U` unchanged, `R` raise, `L` lower, `O` reopen.

```text
 1 R   2 R   3 U   4 R   5 U   6 U   7 R   8 U   9 U  10 U
11 U  12 U  13 U  14 U  15 U  16 U  17 U  18 U  19 R  20 U
21 R  22 U  23 U  24 U  25 R  26 R  27 U  28 R  29 U  30 U
31 R  32 U  33 U  34 U  35 U  36 L  37 U  38 R  39 U  40 U
41 U  42 U  43 U  44 U  45 U  46 R
```

Reasons for every change:

- **1, 2 — raise.**  Max12/Q8 and TD6 have both converted vague
  coefficient/boundary work into exact source schemes with finite named
  complements.  This does not supply the missing universal landing or td
  ceiling, but it sharply raises the information yield of the current
  GGV/sheet-number descendants.
- **4 — raise.**  The selected-Q8 problem is now literally an algebraic-curve
  closure/valuation problem.  Formal branch certification at the remaining
  finite boundary and algebraization/proper closure are no longer generic
  slogans; there are exact rows and a finite first discriminator.
- **7 — raise.**  The complement of the affine Q8 fibre is a concrete piece
  of the nonproperness locus.  Computing its valuative/projective boundary is
  now cheaper than attempting `A(F)` globally and may provide a reusable
  construction of one asymptotic component.
- **19, 21 — raise.**  The confirmed residue-ball theorem turns a complete
  fixed-support Witt tower into an actual characteristic-zero collision.
  The bridge is no longer the bottleneck; the bounded-support existence or
  obstruction question is.  The live full-Q5 fibre is exactly the right
  discriminator.
- **25, 26 — raise.**  Q8 primitivity and all-eight/singleton propagation have
  already made monodromy operational inside a source component.  The new
  all-Q8 affine fibre makes coupled component/landing monodromy more valuable,
  though passports alone remain too generous.
- **28 — raise.**  Projective closure before specialization is now a charged
  computation, and any surviving divisor comes with explicit source rows,
  outputs, and valuations.  This is the first credible local client for
  log/adjunction bookkeeping in the present max12 lane.
- **31 — raise.**  Rees valuations are precisely the language of the remaining
  Q8 escape: a horizontal source component whose affine coordinates cease to
  be integral at `w=0`.  This is now a bounded test on a named algebra rather
  than an attempt to prove finiteness of an arbitrary Keller map in one jump.
- **36 — lower.**  Generic sparse search is dominated by the source-typed AS
  fixed-support tower and by exact max12 boundary strata.  Keep structured
  SAT/falsification, but do not spend capacity on untyped map searches.
- **38 — raise.**  Tropical/initial-ideal methods have acquired a precise
  Newton object: the six Q8 quotient rows over `Q[w]`, with boundary opens and
  output/terminal functions retained.  A finite valuative fan can classify
  projective escape rays or expose where ordinary homogenization is too large.
- **46 — raise.**  Not as a discovery route.  The AS UNSAT/SAT boundary and
  TD6 source-lift identities increasingly need independently checkable proof
  DAGs, cores, and row provenance; formal/certificate infrastructure now
  directly reduces review latency on the critical paths.

All `U` entries retain the reasons and ranks in `APPROACHES.md`; the new event
does not repair their named obstruction, refute their mechanism, or supply a
cheaper test than the three cards below.

## 2. Reranked bottlenecks

### Proof side

1. **Q8 landing/coverage complement.**  Prove that every actual selected
   `k=mu=0,nu!=0` trajectory reaches the now-classified affine `w=0` chart, or
   exclude every finite and projective escape using source rows plus terminal
   and Taylor constraints.
2. **Max12 cell coverage.**  Even a complete Q8 complement theorem must be
   placed in the full normalized `(9,12)` leaf partition and then composed
   with the remaining max12 faces.  Component-local genus is not a universal
   landing theorem.
3. **Global complexity ceiling.**  The sheet/degree ladder still has no
   absolute or cofinal td bound.  Max12 can be a landmark without resolving
   JC2 unless the reduction ledger really lands every minimal counterexample
   there.
4. **TD6 source-complete denominator atlas.**  Close every current row and the
   denominator cover before consuming any localized adjoint identity.

### Counterexample side

1. **Fixed-support all-depth AS tower.**  Decide the full unpinned Q5/Q4
   fibre, derive a global obstruction if UNSAT, and continue all omitted rows
   if SAT.  Complete-map status is non-negotiable.
2. **Uniform boundedness versus conductor growth.**  Either find one support
   that stabilizes through all depths or prove a support/degree invariant that
   must grow.  A merely restricted-analytic limit is not a polynomial map.
3. **Characteristic-zero algebraization and collision.**  This bridge is now
   available once a fixed finite support gives a compatible tower; it should
   not be repeatedly re-proved at finite depth.

## 3. New mechanism and cross-avenue connections

The genuinely new mechanism is a **terminally decorated valuative fan** for
the Q8 source.  Rather than compute one enormous projective closure and hope
its components are intelligible, enumerate rational valuation rays

```text
ord_w(c), ord_w(d2), ord_w(d4), ord_w(x1), ord_w(x3), ord_w(x5)
```

whose initial forms satisfy all six divided rows.  Attach `r6`, `r8`, the
true-centre Taylor polynomials, and the trajectory Kummer ODE to every cone.
Source regularity in the original coordinates (`t*c`, `t*d2`, `t*d4`) cuts
the fan further.  Each surviving cone gives a small toric chart and exact
initial ideal; no surviving cone means there is no projective escape.

This connects four previously separate avenues:

- Q8/max12 source geometry (1--2);
- formal-germ certification and algebraization (4);
- Rees valuations/integrality (31);
- tropical compactification (38).

The same certificate shape also connects to TD6: its denominator atlas is a
constructible/Fitting cover, and the Q8 fan can use the same proof-DAG idea to
record exactly which pivot is a unit on each cone.

A second connection is **Cartier obstruction extraction as a solver
preconditioner**.  The pinned AS Q4 obstruction is a left-cokernel coordinate,
not an accidental point evaluation.  Compute the symbolic row module over
the full Q5 predecessor first, split by Fitting ideals, and feed only the
surviving nonlinear fibres to SMT.  This connects the AS disproof route
(19/21) with the TD6 source-lift/Fitting machinery and can turn solver search
into a small certified algebraic decomposition.

## 4. Three detailed idea cards

### Card A — finite Q8 `x5=0` branch versus terminal vanishing order

**Target.**  Exclude or precisely classify transverse non-parity branches
through the finite boundary curve

```text
x5=0, x1=x3=a!=0, c=1/a, d2=d4=0,
r6=-4a^3/81, r8=0.
```

**Dependencies.**  Exact six-row compiler, the displayed boundary identity,
the already reviewed terminal identity
`nu^10 h^3 (Z')^9=j^9 Z^8`, and source-honest Taylor reconstruction.

**Cheapest discriminator.**  Over `Q(a)` (and separately after fixing the
normalization of `r6`), compute the completed local branches only to the first
nonzero coefficient of `r8` and of the two Taylor defects.  Use tangent-cone
and Hensel linear algebra before any full elimination.  Compare the exact
order of `Z=r8^9/r6^10` at a finite trajectory place with the discrete orders
allowed by the Kummer ODE.

**If incompatible.**  The only finite loaded complement of the Q8 chart dies;
combine with `x3-2*x5=0 => r6=0`, leaving projective/p=0 escape only.

**If compatible.**  Freeze the surviving formal passport and immediately ask
whether Taylor polynomiality or positive genus of its global component kills
it; do not continue generic series depth without a named next invariant.

**Stop condition.**  Stop after the first source-verified nonzero terminal or
Taylor coefficient decides every tangent branch, or after two orders reveal a
free parameter with no new invariant; then move to the valuative fan.

**Information gain.**  Very high: a small calculation can remove the only
finite loaded boundary family or identify the exact remaining Taylor leaf.

### Card B — source-derived Q8 valuative fan and toric closure

**Target.**  Exhaust horizontal components that reach `w=0` only with one or
more quotient coordinates divergent.

**Dependencies.**  Six exact rows over `Q[w]`; original-coordinate
regularity bounds from `q_c=t*c,x2=t*d2,x4=t*d4,w=t^2`; saturation performed
before specialization; output and Taylor compilers.

**Cheapest discriminator.**  Compute the common refinement of Newton normal
fans for the six rows, enumerate cones satisfying tropical balance, and test
each initial ideal over two good primes.  Only cones passing modular controls
receive exact characteristic-zero Gröbner or resultant work.  Add inverse
variables for the cone's declared leading coefficients and retain `r6!=0`.

**If no cone survives.**  Every horizontal loaded component has a finite
affine `w=0` point, hence meets Q8 and falls to the reviewed positive-genus
exclusion (subject to the actual-trajectory/component hypotheses already
charged).

**If cones survive.**  Each is a finite named boundary chart with a leading
source scheme and exact `r6/r8` orders; feed it to Card A's terminal/Taylor
test or to a source-derived projective component calculation.

**Stop condition.**  Stop broad fan growth after all cones in the exact
support are classified.  If more than two cones share the same unresolved
initial ideal, replace them by one symbolic Fitting/toric chart instead of
running duplicate CAS.

**Information gain.**  Highest proof-side gain: it converts “escape to
infinity” into a finite auditable atlas and directly tests the present global
coverage wall.

### Card C — AS global Cartier/Fitting compiler before SMT

**Target.**  Decide whether any full-Q5 predecessor survives the first omitted
Q4 Cartier coordinate, and expose a reusable obstruction rather than a list
of dead points.

**Dependencies.**  Frozen full unpinned 198-row formula, exact integer
determinant compiler, predecessor equations, and the confirmed collision
compactness theorem only after all rows are complete.

**Cheapest discriminator.**  Form the Q4 coordinate as a polynomial function
on the Q5 predecessor algebra.  Compute its class in the cokernel of the next
digit Jacobian; stratify the vanishing/nonvanishing of the relevant minors.
Use the resulting linear equations and variable eliminations as certified SMT
preprocessing, with independent bitblast/proof checking for any UNSAT branch
and exact integer replay for SAT.

**If globally nonzero.**  Q5 is dead by one symbolic Cartier obstruction;
extract the pattern across depths and test whether it proves forced conductor
growth for every fixed support.

**If a zero stratum survives.**  Continue Q4 through Q0 immediately on that
stratum, retaining the same support and all source rows.  A complete map then
advances the compatible-tower/collision route.

**Stop condition.**  Stop adding raw solver seeds once two distinct engines
agree or a proof certificate lands.  If no result after the current cap,
spend the next cycle on symbolic row-module reduction, not more duplicate
bitvector search.

**Information gain.**  High on both outcomes: either a global obstruction and
possible all-depth invariant, or the first source-complete deeper survivor.

## 5. Strongest attacks and software acceleration

- **Strongest proof attack:** Cards A then B, nonblocking and parallel.  The
  finite branch should be decided by jets while the valuative fan classifies
  projective escape.
- **Strongest counterexample/falsification attack:** Card C on the full Q5
  fibre, with a cheap different-prime/p=2 seed used only to test whether the
  obstruction mechanism is prime-specific.
- **Strongest software acceleration:** one source-derived
  `initial-ideal/Fitting/proof-DAG` broker shared by Q8 and TD6, plus certified
  linear/cokernel preprocessing for AS SMT.  It should emit immutable inputs,
  exact cover equations, engine-neutral row hashes, and independently
  checkable SAT/UNSAT or lift certificates.

## 6. Continue / redesign / stop

- **Q8/max12: continue, with redesign at the boundary.**  Run finite boundary
  jets and projective valuative charts in parallel; hostile review of the
  affine theorem stays in the background.  Stop generic support-box growth
  and any computation that again assumes the affine chart is proper.
- **AS: continue.**  The full unpinned Q5/Q4 decision is primary.  Redesign
  around symbolic Cartier/Fitting preprocessing if solver diversity does not
  decide it; stop exact duplicate seeds.  Never attach compactness to a
  filtered or incomplete map.
- **TD6: continue to source completeness.**  Harvest one-row shards and the
  proof DAG; require an explicit denominator cover before atlas composition.
  After a third serializer/monolith failure, stop rerunning the same
  representation and keep only the row-wise DAG.
- **Generic untyped search, ordinary action residues, HC4 first observable,
  and refuted stronger-conjecture ladders: stop/defer.**  They currently lose
  to source-typed boundary and bounded-support tests in expected information
  gain per compute dollar.

No card here proves or disproves JC2.  The global landing/coverage and
complexity-ceiling walls remain explicit.
