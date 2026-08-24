# Preregistration: `D-STATE-GATE`

Frozen: 2026-08-24T02:59:31Z, before executing the gate.

## Premise and source object

The only mathematical premise consumed from the new D work is the reviewed
source-defined `X27 -> X25` transition in
`xmodel/review-dtransition-grok.md`.  The full-cell D2 result is used only to
justify provisional scheduling; no compatibility function, fitted row, or
cell conclusion is consumed here.

The source is the unreduced equation

\[
\mathcal E=(\theta\Phi-12\Phi)\Gamma_\eta
 -\Phi_\eta(\theta\Gamma-18\Gamma)+42t^{20},
\qquad \theta=t\,d/dt,
\]

with the cyclic orbit products defined by `cases/r1_experiment.py` and
implemented on the pure-`y` window by `cases/valuation_e2.py`.  No reduced,
Schur, normal-form, D43, or fitted recurrence is an input.

## Candidate six-band state (frozen before the test)

Put `u=t^6`.  The only repository-registered candidate is the corrected
30-input / 30-output state in `xmodel/sol-newton-lemma.md`:

- input streams `(family,rho)`: residues `0,...,5` for each of
  `tf1,tf2,tg1,tg2`, and residues `0,2,4` for each of `tg01,tg02`;
- input starts `r_rho=6+rho`, except `r_4=16` because `r=10` is `PIN42`;
- output streams `H_a`, `0<=a<=29`, with starts
  `s_a=6+2*((a+1) mod 3)` for `a<=28`, except `s_28=16`, and
  `s_29=36`.

The proposed relabeling is

\[
T_X(f,r)=(f,r+6),\qquad T_Y(a,n)=(a,n+6).
\]

On a stream `t^r Z(u)`, the written Euler rule gives

\[
\theta(t^r Z)=t^r(r+6\Theta)Z,
\quad \Theta=u\,d/du,
\]

so simultaneous relabeling must use the Ore conjugacy
`r+6 Theta -> r+6+6 Theta`, not literal equality of scalar matrices.

For a cutoff `b`, let `P_b^X` forget source coordinates whose first source
occurrence is above `b`, and let `P_b^Y` forget residual coefficients above
band `b`.  The required square is

```text
source through b+6  --E_(b+6)-->  residuals through b+6
       | P_b^X                         | P_b^Y
       v                               v
source through b    ----E_b---->  residuals through b.
```

It must commute coefficientwise by source causality.  After the registered
transient (including `H_29` at band 36), the relative layer maps must also be
closed under `T_X,T_Y` with the displayed Ore correction and with no new
unclassified source or target type.

## Frozen checks

1. Derive the two 30-stream registries from the written start formulas, not
   from observed matrices.
2. At one banked witness for each registered prime, rebuild the unreduced
   pure-`y` source through band 40.  Check the input ladder partition,
   output support, first-occurrence layers at bands 26, 32, and 38, and the
   projection square by exact finite differences.  No equation is solved.
3. Derive the simultaneous-shift law twice: once from the dual source product
   and once from the separately grouped written product rule.  On the banked
   rows require the corresponding second Ore difference to vanish.
4. Audit the first source term omitted by the pure-`y` window directly from
   the unreduced polynomial factors
   `U_f=1+alpha_1*t^42+...`, `U_g=1+beta_1*t^42+...`.  Derive its row-42
   dependence by two independent coefficient expansions.  This is an
   algebraic typing audit, not a band-42 sample or solve.
5. Require an already sourced classification and shift/projection map for
   every coordinate appearing in step 4.  Do not invent one.

## Verdicts and stop

- `SOURCE-MISMATCH`: either source derivation, a banked row, or a projection
  square contradicts the frozen relabeling.
- `UNBOUNDED-STATE`: the unreduced derivation proves that new state types are
  required without a finite bound.
- `STATIONARY-SOURCE-SIGNAL`: both derivations, both primes, and the full
  source typing close exactly under the frozen state and commuting square.
  This would license only a future first source-defined syzygy obstruction.
- `NO-TYPED-STATIONARITY`: the finite pure-`y` regressions pass, but the full
  source reaches a coordinate whose held/derived/independent status or shift
  map is absent from the repository.  Per coordinator instruction, stop
  instead of inventing a state map.

Stop at the first applicable verdict.  In particular, do not compute the
first syzygy obstruction, emit/solve/sample band 28, specialize the row-42
sidecar at a D43 point, use D43 or integral artifacts, form an inverse limit,
or infer a germ or characteristic-zero object.

## Cost

At most two existing banked zero-completed witnesses (one per prime), source
bands at most 40, three registered relative layers (26/32/38), and two small
exact polynomial expansions of the symbolic row-42 interface.  No heavy CAS,
network, new depth solve, or shared-ledger edit.

