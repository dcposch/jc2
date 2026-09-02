# Flagship successor: DISC-COUPLING — do the k rigid bottom stars of one Moh skeleton fit together? The first counting obstruction in the exact-form endgame

The charged TIME-FUNCTION ENDGAME report (PROPOSAL; its review runs in
parallel — re-derive what you use) established: at every bottom-major
disc the leading-order interpolation conditions are the one-variable
Keller equation d·p_f·p_g′ − e·p_g·p_f′ = κ (BOTTOM-ODE), whose
solutions are ABC-extremal pairs (STAR-ABC) that always exist (15/15
triples realisable); at the selected D = 105 skeleton (n = 105, m = 70,
(d,e) = (2,3), M = (−70,−63,103), V = (1,4,1), δ = (3/4, 71/95, −1),
u = 20, N = 6, twenty bottom discs each a (2,3,1)-star p_g ∝ π(π² + b),
star {0, ±s}) the higher orders are governed by a linear operator L_ε
with resonances at ε ∈ μZ_{>0}, μ = −λ_g/a₁ = 1/20: non-resonant orders
are free (7 unknowns, 5 conditions), each resonant order imposes ONE
scalar condition per disc. OPEN[DISC-COUPLING] (bounded): the local
count gives 2 free parameters per non-resonant order at ONE disc, but
the outer-scalar half of those parameters is SHARED by all k = 20 discs
(they are coefficients of g at the level of D₂, seen by every bottom
disc). So at each resonant order: 20 conditions against 3·20 + 2
parameters (per the report's count) — but the conditions across discs
are NOT independent of the shared scalars, and the resonant orders
recur (μZ = {1/20, 2/20, ...} up to the order where the next tower
level enters, ε = δ₂ − δ₁ = 71/95 − 3/4 = 59/380 = 11.2μ, i.e. eleven
resonant orders before the junction with D₂).
YOUR TASK (flagship effort; direct):
(1) SET UP the coupled system exactly for the selected D = 105 skeleton:
    the twenty bottom discs are the twenty conjugates (under which
    group? determine from the d_j chain (105, 35, 7, 1) and the head
    exponents) of one disc, so Galois symmetry relates their local
    parameters; write the local parameters of disc j as the conjugates
    of those of disc 1 where the symmetry forces it, and as independent
    where it does not (this IS OPEN[BRANCH-ORBITS] at this skeleton:
    state how many independent discs there are).
(2) IMPOSE the resonant conditions at ε = μ, 2μ, ..., 11μ jointly across
    the independent discs with the shared outer scalars, order by order:
    at each order report unknowns / conditions / rank / solution-set
    dimension; say whether the accumulated conditions (eleven resonant
    orders before the junction) leave a solution — (a) INCONSISTENT:
    the skeleton DIES (the first exact-form Appendix-II kill; state the
    order and the killing scalar); (b) positive-dimensional through the
    junction: report the dimension entering D₂ and set up the junction
    condition (the level-2 star is a (d,e,V₂)... no: at D₂ the a₂ = 60
    roots split into the twenty bottom discs; the junction imposes that
    the twenty local expansions glue into one Puiseux expansion of the
    D₂-level root with the correct characteristic exponent); (c)
    determined: print the solution and evaluate the junction.
(3) UNIFORM READING: for a general skeleton with k bottom discs, s
    levels, and resonances μ_j Z at each level, write the counting
    function (parameters − conditions) accumulated to the top of the
    tower as a function of the skeleton data; state the sign condition
    under which the count alone forbids realisation (a candidate
    skeleton condition (17)); evaluate it over the census at D ≤ 120
    through box/d1sub-drivers-20260902/d1floor.py and report kills per
    degree, typing every number as "counting bound, not a proof" unless
    the linear system is actually solved.
(4) Controls: (y, x + y^k) (k discs? no — one disc; check the count
    gives free parameters matching the automorphism family); the
    (y + x², x + (y + x²)²) control; a non-Keller two-tower row must
    fail at the first resonant order.
Discipline: desk-scale CAS (< 30 min, < 4 GB); PROVED-HERE/UNREVIEWED
typing; state the bounded quantity of every OPEN you raise; do not edit
canonical ledgers; do not inspect jc2-lean; do not read the parallel
review of the endgame report.
Report: xmodel/disc-coupling-opus5-20260902.md
Seal-at-completion (standard <!-- BODY-END --> marker); bounded writes;
target 30-45KB.
charged_input=xmodel/time-function-endgame-opus5-20260902.md
charged_input=xmodel/integration17-coordinator-fable51-20260902.md
charged_input=xmodel/d1-subtree-opus5-20260902.md
charged_input=box/tfe-drivers-20260902/bottomode.py
charged_input=box/d1sub-drivers-20260902/d1floor.py
charged_input=box/moh_skeleton_N.py

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
9f47a25fb7ceb0174add0f0c245d1e9bca914cadb108053bb02abf714bf685c1  {{LANE_INPUTS}}/time-function-endgame-opus5-20260902.md
126d9c84b7ee373891e4e40f8a60b25495a4e0ed89da9c6febe5224a461686f5  {{LANE_INPUTS}}/integration17-coordinator-fable51-20260902.md
26479b06b0f1ef526fe37bd34bccb61f50f207a509fcb0b0c1ae6fc5751858c0  {{LANE_INPUTS}}/d1-subtree-opus5-20260902.md
69ff5bdea265adc37c9518f381eccfe6a6162c430a51075b6c2069f709894473  {{LANE_INPUTS}}/bottomode.py
cf0780cc0b3ef0f2de630e6901f836596c1dd58e3ff1dc0917e9c8d363baebe6  {{LANE_INPUTS}}/d1floor.py
3022020435c86b62ecd28df8d28d1bdf9ab4e361828c028b913ba8aae3f11a39  {{LANE_INPUTS}}/moh_skeleton_N.py
```
