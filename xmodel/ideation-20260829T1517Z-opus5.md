# Blind whole-portfolio ideation — Opus 5 — round `20260829T1517Z`

Frozen basis `40c1ab3448209e3d87173feb947a733f6fe54f7f`. Written blind: no peer
submission, no other `ideation-20260829T1517Z-*` file, no file created after
this lane started, no web, no `jc2-lean` access of any kind.

## 0. Binary disposition

```text
JC2_RESOLVED            = NO
NEW_TYPED_EXIT_PRICE    = NO          (charge_basis therefore ABSENT)
AVENUE_RANK_CHANGES     = 1 lower (Avenue 36, conditional), 45 unchanged
NEW_MECHANISM           = K00-SHIFT-LADDER (block-shift covariance)   [NEW]
NEW_CONNECTION          = Avenue 36 <-> Avenue 4, and Avenue 36 -> Avenue 2/3
                          via row-proportionality compatibility        [NEW]
DECISIVE_EXPERIMENT     = RUN, not merely proposed (Section 3)
EVIDENCE_TIER           = EXACT / PRODUCER-INTERNAL-UNREVIEWED
LIFECYCLE               = DRAFT (not provisional; no different-model review)
```

The one substantive new result is a desk-exact, Groebner-free determination of
the **literal grade-five compatible point set over the promoted K00 rank-zero
plane**. Under the source-open condition `k10_0 != 0` it collapses the whole
two-plane to its origin `d*_1 = 0`. This is producer-side evidence from an
ideation lane, not a promotion, and Section 3.7 states exactly what it is not.

## 1. Custody and charged inputs

Round inputs, independently rehashed here:

```text
648acf8ba6d8cd2b498d7a0825fc0e239044a4270e0a928009811550806d3449
  xmodel/ideation-20260829T1517Z-state.md        (body 10551 B,
  body sha256 a2ed4405151dc5acac0441694604484d29e4e6f7fee9181ed758aa09f1035f92
  — recomputed here and matching its own seal)
72284172888e3c8ed38d9a619ac195c5060bd0b7dd5abf1b728634e0aa4cfdad
  xmodel/roundview-20260829T1517Z-40c1ab34.md
```

Canonical files, all matching the packet's declared values:

```text
f781077840a8405b4ef100b718bc6eeef17a9d07948aaadda2eb2d51aecf27ab  APPROACHES.md
3f35e3a8a5d204a8c24d96821077117e6efe263a4e2765da7a527d0c13686877  AUDIT.md
d7e833c890c6fdc11a646c5feb5125665b9c298e7fb93a6a706e1afdc63102bc  COORDINATION.md
d45f1db6117f67e21065c29e0ff65ff7c1f8304f3ecc37fa796c5cd4b93b4e65  PROGRESS.md
805152bf2e68edad1a5d55b9fff7092e7a19f40171406050c9d9b50e994de608
  xmodel/ideation-20260829T1224Z-synthesis.md
319212fbf03feb1dfe7ce1f4255a021b5e7931815af5f46a1f890027ddf9797a  notes.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
```

Mathematical inputs charged by Section 3:

```text
d7ec6d18d58265421ff315fa00e38cd32992ac12f7d8166cf6c436e23bf06501
  cases/max12_812_order2_u2_62_k00_grade7_fitting_atlas_v26_20260827/
  aws_box02_r2_held_compile/output/ATLAS_EXACT_POLYNOMIALS.json   (62,072,089 B)
d453b9563d8f6cc23319d6bc0d8edce8a83f657b9e3a60cb244b00f181459860
  xmodel/k00-rank5-rankle1-coordinator-integration-sol56-20260829.md
e0947368509714aa96376789914a4dbfd7141b1f77832016bf4dbe7c3caa45e4
  xmodel/k00-grade3-rankle1-primary-grok46-92e-20260829.md
0d2a9861126c8857e04a9170c8586b6b4eabe67d2e65d3b4d3b7e991774b614f
  xmodel/k00-grade4-rank0-plane-primary-opus5-92e-20260829.md   (my own,
  sealed producer evidence, explicitly NOT promoted; used only for its
  independently reproduced grade-four closed form, re-derived from scratch
  in Section 3.2 rather than consumed on trust)
```

Read for portfolio context, not charged as premises for any claim:
`xmodel/td12-global-source-bridge-b-coordinator-integration-sol56-20260829.md`
(`c6c1d5fe...`) and
`xmodel/finite-pole-full-actual-scope-coordinator-integration-sol56-20260829.md`
(`bf51df72...`).

**Concurrency disclosure.** From a directory listing only — I did not open the
files — two lanes are running on this same basis:
`k00-grade5-rank0-plane-twoinput-primary-fable5-40c-20260829` and
`k00-grade4-rank0-plane-opus5-hostile-review-grok46-40c-20260829`. Both were
created at `08:21–08:22`, after this lane's prompt at `08:20`, and are
therefore outside my read scope. My Section 3 is consequently an
**independent concurrent** computation, not a lane takeover and not a
substitute for the owned grade-five gate. If it agrees with that lane it is a
free different-model cross-check; if it disagrees, the owned lane's sealed
report and this one must both be reviewed and the disagreement adjudicated.
Agreement between them would be evidence about the computation, never proof.

No canonical, ladder, case, guardrail or operations file was edited. No
commit, push, AWS, remote shell, or web. Scratch lived only in `/tmp/op5id/`.
The only repository file created is this report.

## 2. What I actually verified before reasoning

Three cheap consistency checks on the promoted ledger, all passing, run
before any new work (Section 3 script, steps `[custody]` and `[1]`):

1. all 49 literal atlas rows through grade six rebuild from `exact_terms`
   with exact `Fraction` arithmetic and reproduce the stored producer digest
   and term count: `49/49`;
2. the seven literal grade-two rows and the seven literal grade-three rows
   vanish **identically** on the promoted rank-zero plane
   `(d0_1,...,d5_1) = (2s, t/8, s, t, s, 2t)` with the whole `d*_2` block
   free — an independent reproduction of the promoted grade-three incidence
   theorem `V(B,P3_1..P3_7) = Pi x A^6_u` restricted to its rank-zero
   stratum;
3. the grade-four closed form `phi(Lambda_{4,r}) = Q_r(u - mu(s,t))`,
   `mu = (s^2, st/8, 16t^2, 0,0,0)`, holds as a polynomial identity for all
   seven rows.

Check 2 is the load-bearing one: it is a from-scratch re-derivation of the
promoted result from the frozen atlas bytes, so Section 3 does not stand on a
prose citation.

## 3. New result — the K00 grade-five point set over the rank-zero plane

Script `/tmp/op5id/K00G5.py`, sha256
`028b4218478020602d85649de6e91a269d10fdf4fc31597798a8cd6d2ab8f376`; stdout
sha256 `059ef07986eb5eb3df2152328657e8b67954b6c181a6e23482a2884a9d98f725`.
One process, `1.51 s` wall / `1.44 s` user, `618,856,448 B` peak RSS — inside
the 60 CPU-second and 1 GiB desk caps. Pure Python exact rational sparse
polynomial arithmetic; **no Groebner basis, no CAS, no localizer ideal**.

### 3.1 Setup and declared ring map

`phi` sends `d*_1` to the plane `(2s, t/8, s, t, s, 2t)`, `d*_2 -> u`,
`d*_3 -> v`, `d*_4 -> x`, `k10_0 -> k0`, `k10_1 -> k1`, over `Q`. Generator
order and coefficient field are those of the atlas `ring_variables`. Write
`w := u - mu(s,t)`.

### 3.2 Two structural identities

* **(S1) Grade four is grade two at a shifted argument.**
  `phi(Lambda_{4,r}) = Q_r(w)` for all seven `r`, `Q_r := Lambda_{2,r}`.
  Reproduced here from the atlas bytes.
* **(S2) Grade five is affine-linear in the newest data, and two blocks
  disappear.** On the plane, `phi(Lambda_{5,r})` has degree `0` in the whole
  `d*_4` block and in `k10_1`, and total degree `1` in the seven unknowns
  `(v_0,...,v_5, k10_0)` jointly. So grade five is an inhomogeneous *linear*
  system, not a fresh nonlinear gate.

Additionally, the `v`-linear coefficient of `phi(Lambda_{5,r})` equals
`C_r(w)`, where `C = A[:,1..6]` is exactly the grade-three `d*_2`-coefficient
matrix — grade five is grade three at the shifted argument in its
load-bearing part (7/7 rows, 6/6 slots each). This is the mechanism named in
Section 5.

### 3.3 Reduction on the reduced grade-four locus

Set-theoretically over an algebraic closure, `V(I4) = V(sqrt I4)`, so the
exact grade-four point set is `w in W4 := {16w1-4w3+w5 = 0,
w0-4w2+2w4 = 0}`. This is the honest input for a *point-existence* question;
the non-reduced scheme input governs ideal-level statements only, and I make
none. All seven literal grade-four rows vanish identically on `W4`, confirming
these are genuine scheme points and not merely radical points.

On `W4`, with `X := 8w1 - w3` and `Y := w2 - w4`:

* row 6 is identically zero;
* row 4 contains **no unknown at all**;
* rows 3, 5, 7 have `(v,k10_0)`-linear parts exactly `-1/8`, `-1/128`,
  `-1/1024` times row 1's — exact constant proportionality, not a
  numerical near-miss.

Hence the necessary base conditions are exactly two:

```text
Phi4 = (3/32768) * ( 64 s X^2 + 128 t X Y - s Y^2 )      = 0
Phi3 = (3/2048)  * ( 64 t X^2 -   2 s X Y - t Y^2 )      = 0
```

with `Phi5 = (-1/8) Phi3` and `Phi7 = (-1/128) Phi3`, both exact.

### 3.4 Complete branch decomposition

Verified identities: `t*Phi4' - s*Phi3' = 2(s^2 + 64 t^2) X Y`, and at
`s = 8 i t`, `Phi3' = -t (Y + 8 i X)^2` while `Phi4' = 8 i * Phi3'`. Case
analysis on `(s^2+64t^2) X Y = 0` is then exhaustive and gives

```text
V(Phi3,Phi4) = {X = Y = 0}  u  {s = t = 0}
             u  {s = +8it, Y = -8iX}  u  {s = -8it, Y = +8iX}.
```

The last two are exchanged by the `Q`-conjugation of `Q(i)`, under which all
atlas coefficients are fixed, so one settles both.

**`{X = Y = 0}` inside `W4` is exactly the plane `Pi` again**, with
`(s',t') = (w2, 8w1)`. That is: the grade-four shifted argument `w` lies on
the *same* two-plane. This is the self-similar branch — the natural formal-arc
continuation.

### 3.5 Every branch except the origin dies under `k10_0 != 0`

* **Self-similar branch `w in Pi`.** The `v`-part vanishes identically and
  the seven rows collapse to
  `k10_0 * (5/4096) * t (3s^2 - 64 t^2) = 0` and
  `k10_0 * (5/65536) * s (s^2 - 192 t^2) = 0`.
  With `k10_0 != 0`: `t = 0` forces `s^3 = 0`; `t != 0` forces
  `3s^2 = 64t^2` and then `s = 0` or `s^2 = 192t^2`, both contradictory.
  So `s = t = 0`.
* **Branch `s = 8it`, `Y = -8iX`, `t != 0`.** Symbolically over
  `Q(i)[t,w1,w2,w3]`: the `2 x 6` matrix of `v`-coefficients of rows 1 and 2
  has rank one (all fifteen `2x2` minors vanish identically), the
  `k10_0`-free residue after eliminating `v` is **identically zero**, and the
  surviving `k10_0` coefficient is
  `-(15/16384) i t^3 X`. With `t != 0` and `k10_0 != 0` this forces `X = 0`,
  hence `Y = -8iX = 0`, hence the previous bullet, hence `s = t = 0` —
  contradicting `t != 0`. The branch is empty.
* **Branch `s = t = 0`.** Survives. Explicit witness, verified against the
  literal atlas rows of grades 0 through 5 simultaneously:
  `d*_1 = 0`, `d*_2 = (4,1,1,0,0,-16)`, `d*_3 = 0`,
  `d*_4 = d*_5 = 0`, `k10_0 = 1 != 0`, `k10_1 = k10_2 = 0`.

### 3.6 Verdict

> **(G5-COLLAPSE, EXACT, UNREVIEWED.)** Set-theoretically over an
> algebraically closed field, with `d*_1` on the promoted rank-zero plane,
> the reduced grade-four input, and the source-open condition
> `k10_0 != 0`, the literal grade-five compatible locus is exactly
> `{s = t = 0}`, i.e. `d*_1 = 0`. Every point of the plane other than its
> origin is excluded at grade five.

Grade four had left a 13-dimensional survivor with the full two-plane free.
Grade five removes the plane's two parameters entirely.

### 3.7 What this is not

It is not a JC2 theorem, a counterexample, a Keller pair, a polynomial map, a
degree bound, an exit price, or an occurrence statement. It is not an
ideal-theoretic (scheme) statement: I computed a point set, and the
non-reduced grade-four input is a different question that this lane did not
touch — a `REPRESENTATIVE` reduced input is not the scheme. It is not
promoted, not provisional, and not different-model reviewed. It does not
license relabelling any capped historical job. It says nothing about grade six
or beyond, about the `d*_4`/`k10_1` blocks at their own first grade, or about
any other K00 stratum. Model agreement, if it later occurs, is not proof.

### 3.8 The single question that decides its importance

Whether `d*_1 = 0` is **admissible** in the source problem. The campaign
record I can see names exactly one source-open condition, `k10_0 != 0`
(`k00-grade3-rankle1-primary-grok46-92e-20260829.md` §8), and no
nondegeneracy condition on `d*_1`. I refuse to guess the source semantics.

* If `d*_1 = 0` is excluded upstream, `(G5-COLLAPSE)` is a **full grade-five
  kill** of the bounded characteristic-zero K00 counterexample seed.
* If it is admissible, the seed survives as a single point of the plane and
  grade six — whose literal rows are already in the frozen atlas — decides.

This is Idea Card B and it is the cheapest decisive step in the whole
counterexample portfolio right now.

## 4. Disposition over all 46 avenues

`unchanged` unless stated. One change, explained.

| # | Disposition | Note |
|--:|---|---|
| 1 GGV corner families | unchanged | No new degree/td ceiling. Bezout deficit stays family-local per the 1224Z close. |
| 2 Sheet ladder / Sigray–Orevkov | unchanged | Still the principal proof avenue. Bottleneck re-ranked in §5, mechanism added in §6. |
| 3 Vertex-gap / strip ODEs | unchanged | Mechanism supply; still no source-provenanced td12 PairPack client. |
| 4 Formal-germ certification (D-series) | unchanged rank, **new live sub-question** | The block-shift covariance of §3.2 is a concrete prolongation mechanism the D-series lane has never tested. Rank unchanged because I have no D-series theorem — only a cheap test (Card A tail). |
| 5 Jung–van der Kulk descent | unchanged | |
| 6 Abhyankar–Moh | unchanged | |
| 7 Jelonek asymptotic variety | unchanged | |
| 8 Formal-inverse combinatorics | unchanged | |
| 9 Lee–Li Conjecture E | unchanged | |
| 10 HC4 => JC2 | unchanged | `NO LEVERAGE` stands. |
| 11 Mathieu/GMC/Zhao | unchanged | refuted. |
| 12 Face isolation / p-adic multinomials | unchanged | |
| 13 Dixmier DC(2) | unchanged | |
| 14 End(A_1) / Zheglov | unchanged | |
| 15 Spectral surfaces | unchanged | |
| 16 D-module holonomic index | unchanged | |
| 17 BCW/Druzkowski/Yagzhev | unchanged | |
| 18 Graded / GIT | unchanged | closed. |
| 19 Char-p + Witt lifting | unchanged | LL1-R4 closed software debt only; no occurrence theorem. |
| 20 p-curvature formalism | unchanged | |
| 21 p-adic injectivity / Hensel | unchanged | degree-twelve frontier unmoved. |
| 22 Diophantine/heights | unchanged | |
| 23 Analytic global inverse | unchanged | |
| 24 Real JC / Pinchuk | unchanged | |
| 25 Monodromy / passports | unchanged | |
| 26 Primitive monodromy bound | unchanged | still the cheapest untried group-theoretic test; no new evidence either way. |
| 27 Links / splice diagrams | unchanged | no splice-scope reopen; §3 gives it nothing. |
| 28 Log surfaces / BMY | unchanged | |
| 29 LND / commuting frames | unchanged | |
| 30 Affine-surface classification | unchanged | |
| 31 Integrality / ZMT | unchanged | |
| 32 Off-diagonal collision ideal | unchanged | `OFF-DIM2` still has no complete-map client. |
| 33 Symplectic exactness / residues | unchanged | |
| 34 2D sweep / pole removal | unchanged | |
| 35 Descent of dim>=3 CEs | unchanged | |
| 36 Guided CE search (**K00 lives here**) | **lower (conditional)** | See below. |
| 37 Finite-field census | unchanged | |
| 38 Tropical | unchanged | |
| 39 Cohomological cluster | unchanged | |
| 40 Free-associative lift | unchanged | |
| 41 Naive scaling deformation | unchanged | falsified. |
| 42 Markus–Yamabe | unchanged | |
| 43 Ritt decomposition | unchanged | |
| 44 Moskowicz "no prime td" | unchanged | closed as proof input. |
| 45 Differential Galois | unchanged | |
| 46 Lean / AI certification | unchanged | |

**Avenue 36, lower (conditional).** The packet calls K00 "the protected
bounded characteristic-zero counterexample seed" and puts the whole
falsification bottleneck at literal grade five. Section 3 decides that
question set-theoretically on the reduced input: the surviving locus over the
promoted rank-zero plane is the single point `d*_1 = 0`. A seed whose
surviving stratum is one point, rather than a two-parameter family, is
materially weaker. The lowering is **conditional on two things** and must be
reverted if either fails: (a) different-model reproduction of §3; (b) the
`d*_1 = 0` admissibility question of §3.8. If `d*_1 = 0` turns out excluded,
Avenue 36 should be lowered **hard**, not conditionally. I deliberately do
not lower it further now: an unreviewed producer computation from an ideation
lane is not grounds for closing the campaign's only protected
counterexample-side seed, and the packet's own instruction to keep
counterexample-side research time funded still binds.

## 5. Reranked bottlenecks

**Proof side** (change from the packet is at rank 4, which is new):

1. Derive a named B25 or S17 **occurrence** from an arbitrary hypothetical
   minimal counterexample. Unchanged as #1; nothing this round touches it.
2. Serialize a route-separated actual `PairRef`/completion and source values.
3. Prove a finite support/degree cap or an invariant of the missing values.
4. **(new framing)** Find a *nonabsorbed distant inhomogeneous constraint
   that needs no source values at all*, by row-proportionality compatibility
   (§6.2). This was previously fused into #2/#3 as "get the source data
   first"; §3 shows the two can be decoupled, which is why it now ranks above
   the tower transgression.
5. Construct the original-to-terminal tower transgression.

**Counterexample / falsification side** (materially re-ranked):

1. **`d*_1 = 0` admissibility** (§3.8). Was not on the list at all; it is now
   the single cheapest decisive question on this side.
2. Different-model reproduction of `(G5-COLLAPSE)` and reconciliation with
   the concurrently owned grade-five lane.
3. Literal **grade six** on whatever survives, using the atlas rows that are
   already frozen (`131..457` terms each). Previously this looked like the
   next AWS-scale gate; §3.2 shows the newest block enters linearly, so it is
   very likely another desk-scale linear-solvability question.
4. The scheme (non-reduced) grade-four input as an ideal-level question,
   separate from the point set. Demoted below (3): it cannot create points
   that the reduced input excludes.
5. Everything else on the falsification side (char-p lifts, dim>=3 descent,
   sparse search) is unchanged and remains behind these.

## 6. New mechanism and new connection

### 6.1 `K00-SHIFT-LADDER` — block-shift covariance — `NEW`

History search: `grep -ril` over `xmodel/`, `APPROACHES.md`, `AUDIT.md`,
`PROGRESS.md`, `notes.md` (excluding all `*1517Z*`) for `shift ladder`,
`GRADE-SHIFT`, `shift-covarian`, `iterated plane`, `shifted argument`, and
`grade-two rows at` returns **zero** hits. `u-mu`/`Q_r(u` hit only my own
grade-four report and prompts derived from it. The grade-four instance is
therefore `KNOWN` (it is the promoted-adjacent closed form (S1)); the
*ladder* reading, its grade-five instance, and its use as a proof mechanism
are `NEW`.

**Statement.** In the K00 atlas the grade tower is not a sequence of
independent gates. On the rank-zero plane, grade `g+2` is grade `g` evaluated
at a **shifted block argument**, plus an explicit `k10` correction:

```text
g = 2 :  phi(Lambda_{4,r}) = Lambda_{2,r}( w ),          w = u - mu(s,t)
g = 3 :  v-linear part of phi(Lambda_{5,r}) = C_r( w ),  C = grade-three
                                                         d*_2-coefficient
```

both verified 7/7 on the frozen bytes. The consequence that matters is
structural, not cosmetic: because the newest block enters linearly, **each
grade is an inhomogeneous linear solvability problem whose obstruction is a
compatibility condition on the previous grade's data**, and the obstruction is
computable by elimination rather than by a Groebner basis. That is precisely
what let §3 replace a registered heavy gate with a 1.5-second desk run.

The mechanism is falsifiable: if grade six is *not* grade four at a shifted
argument, the ladder is a grade-4/5 accident. Card A tests exactly that, on
rows that are already frozen in the atlas.

### 6.2 New connection A — Avenue 36 -> Avenues 2 and 3 — `NEW`

The grade-five kill in §3 did **not** come from solvability of the rows in
the unknown block. It came from four rows whose coefficient vectors in the
unknown block are exact constant multiples of one another
(`-1/8, -1/128, -1/1024`), which forces their *inhomogeneous* parts into the
same ratio — conditions carrying **zero new unknowns**.

Transport this as a method, not a result, to the td12 cascade. The packet's
own diagnosis is that the homogeneous rows are all absorbed (`J = 0` through
`s <= r = 3i/2`) and that "genuine Keller content remains at the distant
inhomogeneous row", while the blocker is that source values are unavailable.
Row-proportionality compatibility is exactly a constraint that survives that
blocker: if two cascade rows have proportional coefficient vectors in the
unknown source jets, their right-hand sides must be in the same ratio,
whatever the jets are. Card C tests it. This is the first mechanism I have
seen in the campaign record that attacks bottleneck #4 without first solving
bottleneck #2.

### 6.3 New connection B — Avenue 36 <-> Avenue 4 — `NEW`

Avenue 4's D-series is the campaign's other graded prolongation tower, and its
recorded wall is that "modular nonempty != germ != char-0 != polynomial" with
depth prolonged one window at a time. The K00 ladder shows a prolongation
tower can be *shift-covariant*, in which case all depths are governed by one
recursion. Whether the D-series has the same covariance is a bounded desk
question on frozen rows and has never been asked. I attach it as the tail of
Card A rather than as a separate card, because it is worth an hour only if
Card A's grade-six test succeeds.

### 6.4 A pattern I explicitly refuse to call a connection

Gaussian integers keep surfacing across unrelated lanes: `(4+3i)/5` in
`TWIN-ORDER`, `(9 +/- 3i)/8` in the td12 U1 sibling charge, and now
`s = +/- 8it` in K00 grade five. These live in different problems with
different rings and no exhibited map between them. Under FALLACY-v2
"Variable/ring map", matching arithmetic shapes prove nothing. I record the
observation so a later lane does not rediscover it as a lead, and I assign it
no weight.

## 7. Strongest attacks

### 7.1 Strongest proof attack

`TD12-ROW-PROPORTIONALITY` (Card C). Reason it is the strongest available:
every other proof-side move in the current portfolio is blocked behind the
occurrence theorem or behind absent source values, and has been for several
rounds; this one is blocked behind neither. It consumes only the already
promoted route-separated cascade structure and asks a question about
coefficient vectors, which are known. Its expected value is high precisely
because a negative answer is also informative and cheap — it would say the
cascade's rows are in general position in the unknown block, which is itself a
fact the campaign has never recorded.

Keep B and S routes strictly separate throughout; the two S sibling
evaluations share one parent family and are not independent generic
coefficients.

### 7.2 Strongest counterexample / falsification attack

Resolve `d*_1 = 0` (Card B), then run grade six on the survivor. This is the
strongest because §3 has already reduced the falsification frontier from a
13-dimensional survivor to a single point, and a single point either dies for
a stated reason or is a genuinely sharp object. The historical failure mode
here — treating a finite formal jet as a polynomial map — is guarded by the
packet's own binding stop, which I endorse: even a jet surviving every grade
is not a counterexample, and algebraization remains Avenue 4's unsolved wall.

## 8. Mathematical-software acceleration / decisive experiment

**Already executed, not proposed:** the exact sparse-polynomial desk kernel of
`/tmp/op5id/K00G5.py`. Dependency-free Python, `Fraction` coefficients,
tuple-monomial dictionaries, plus a two-element `Q(i)` layer by reduction
modulo `I^2+1`. It settled the grade-five point set in `1.51 s` / `619 MB`.

The generalizable acceleration is a **linear-in-the-newest-block prescreen**
to be run *before* any heavy gate is registered:

1. rebuild the literal rows and re-verify producer digests (fail closed);
2. apply the declared specialization;
3. measure the total degree in the newest unknown block;
4. **if that degree is 1**, do not register a Groebner job at all — split each
   row into linear part and constant, find exact proportionalities among the
   linear parts, and emit the compatibility conditions and their branch
   decomposition directly.

Measured benefit on the one case where both routes are known: K00 grade five,
prescreen `1.5 s` desk versus a registered heavy gate (the comparable capped
K00 chart in the record consumed 21,000 s and returned
`RESOURCE_CAP_NO_VERDICT`). The prescreen is not a replacement for Groebner
work when the degree exceeds 1; it is a router. Its own negative control is
mandatory: on a row set that is genuinely nonlinear in the newest block, it
must decline rather than emit conditions.

I ran the FALLACY-v2 controls this requires: six independent perturbations of
`mu`, one generic off-plane shift, and six single-coordinate perturbations of
the plane itself, all of which break the collapse; plus the positive controls
that the ansatz solves grade four exactly and that the origin is a genuine
witness through grade five.

## 9. Campaign-systems card

`UPGRADE` — endorse the packet's named candidate, with one measured
refinement and a concrete smallest test.

**Endorsement.** The repo-owned wait-authoritative capped-process helper
should be built as specified: closed stdin or explicit `quit;`, wall/CPU/RSS
caps, PID/PGID/start telemetry, exact-PGID TERM, bounded grace, exact-PGID
KILL, one reap; prohibit unscoped `pgrep`/`pkill` and indefinite `kill -0`
loops; migrate the nine bare loops afterwards as a separate bounded task.

**Measured refinement (new, from this session).** Telemetry must go to a
**separate file descriptor, not stderr**. Evidence: in this session
`/usr/bin/time -l python3 K00G5.py ... > out 2> timing` produced an
**empty stdout and a normal-looking timing block**, while the actual
`FileNotFoundError` was buried inside the timing file. A caller checking
"stdout produced, resource block present" would have scored a hard failure as
a quiet success. This is the same failure class as the packet's incident —
a supervisor treating a non-authoritative signal as authoritative — one layer
up, and it costs one design line to prevent.

**Smallest measurable test** — a six-case fixture matrix, each asserting exit
status, stdout bytes, telemetry-fd bytes, and that no process survives:

```text
1 clean exit 0, output on stdout            -> status 0, telemetry on fd 3 only
2 nonzero exit, empty stdout                -> status != 0 and NOT reported clean
3 child writes to stderr then exits 0       -> stderr preserved, not merged with telemetry
4 child ignores TERM                        -> TERM to exact PGID, bounded grace, then KILL
5 child forks a grandchild that outlives it -> whole PGID reaped, none survives
6 child exceeds the wall cap mid-output     -> capped, partial stdout retained, status distinguishable from 1
```

Retain only if cases 1–6 pass deterministically and the nine call sites keep
byte-identical behaviour on their existing fixtures. No mathematical
scheduling penalty: this runs beside research and blocks nothing.

**Secondary, not proposed for this window.** The `ROUNDVIEW/v1` body is
45,683 B, of which the older-overlay index is roughly 19 KB of hashes of
superseded text that no lane can act on. A v2 that emits the index to a
separate hash-referenced file would cut the charged prompt slice by about 40%
with zero information loss and a trivial determinism test (v2 + index
concatenates back to v1 byte-for-byte). I rank it below the process helper
because context cost is an efficiency issue and the helper is a correctness
issue.

## 10. Idea cards

### Card A — `K00-SHIFT-LADDER/v1` — `NEW`

**Claim to test.** Grade six on the rank-zero plane is grade four at a shifted
block argument plus an explicit `k10` correction, i.e. the covariance of §6.1
is a ladder and not a grade-4/5 accident.

**Dependencies.** The frozen atlas only (grade-six rows are already present,
`131..457` terms). No AWS, no promotion, no source semantics.

**Cheapest discriminator.** One desk run, well under a minute: substitute the
plane, check whether the `d*_4`-linear coefficient of `phi(Lambda_{6,r})`
equals the grade-four `d*_3`-coefficient at the shifted argument, for all
seven rows and six slots.

**Interpretation of every outcome.**
* *Holds 7/7.* The ladder is real. Then the whole tower is governed by one
  recursion; state and prove it, and the K00 gate stops being a per-grade AWS
  question forever. Run the Avenue-4 D-series analogue next (§6.3).
* *Holds for some rows only.* Not a ladder but a partial covariance; report
  exactly which rows and stop — a partial pattern must not be extrapolated.
* *Fails.* Grade four and five are an accident of the plane's specific
  quadratic `mu`; the mechanism claim in §6.1 is withdrawn and each grade
  keeps needing its own gate. §3's verdict is unaffected either way, since it
  never used the ladder as a premise.

**Stop condition.** One grade tested. Do not iterate to grade seven: grade
seven rows are outside the frozen atlas.

**Expected information gain.** High and symmetric. It either converts an
open-ended grade march into a closed form or kills a mechanism claim before
anyone builds on it.

### Card B — `K00-G5-DSTAR1-ADMISSIBILITY` — `NEW`

**Question.** Is `d*_1 = 0` admissible in the source problem underlying the
K00 atlas?

**Dependencies.** `SOURCE_COLUMNS.json` and `compile_fitting_atlas_v26.py`
source semantics; §3's verdict; the concurrently owned grade-five lane's
sealed report once it exists. Not blocked by review of §3 — the question is
worth answering whichever way §3 is adjudicated.

**Cheapest discriminator.** Read the recorded `kind`/`first_Lambda_grade`/
`boundary_status` for the `d*_1` columns and determine, from the source
construction rather than by analogy, whether a vanishing leading block is a
legal jet or a degenerate one.

**Interpretation of every outcome.**
* *Excluded upstream.* `(G5-COLLAPSE)` becomes a full grade-five kill of the
  bounded characteristic-zero seed. Lower Avenue 36 hard; do not call it a
  JC2 result — it kills one seed, not the conjecture's counterexample side.
* *Admissible.* The seed survives as one point. Go to grade six on that point.
* *Underdetermined by the recorded source.* Return typed `OPEN` and say so.
  Do not fill the gap by cap or analogy; a guessed admissibility rule would
  silently decide the campaign's protected falsification lane.

**Stop condition.** One file read plus one derivation. If the source does not
determine it, stop and report `OPEN` rather than escalating.

**Expected information gain.** Highest per unit time on the falsification
side: it is the difference between "a seed collapsed to a point" and "a seed
is dead".

### Card C — `TD12-ROW-PROPORTIONALITY/v1` — `NEW`

**Claim to test.** Some pair of td12 cascade rows have coefficient vectors in
the unknown source jets that are exactly proportional, so their inhomogeneous
parts must be in the same ratio — a Keller constraint requiring no source
values.

**Dependencies.** The promoted route-separated cascade structure and the
promoted B-bridge landing row. Explicitly **not** dependent on a `PairRef`, an
occurrence theorem, source values, `c_g`, or a support cap — that is the whole
point. Keep B and S separate; do not treat the two S sibling evaluations as
independent generic coefficients.

**Cheapest discriminator.** Form the coefficient vectors of the cascade rows in
the unknown block over the declared ring and test all pairwise `2x2` minors
for identical vanishing. Desk-scale exact rational arithmetic; no CAS.

**Interpretation of every outcome.**
* *A proportional pair exists.* Emit the ratio condition on the inhomogeneous
  parts and check whether it is absorbed by the known `J = 0` response. If it
  is not absorbed, that is a genuine nonabsorbed distant constraint —
  bottleneck #4 — obtained without source data. Enqueue hostile review before
  any descendant.
* *A pair is proportional but the condition is absorbed.* Record it; the
  absorption itself sharpens the description of what the response can reach.
* *No proportional pair.* Record `NO HIT` and the fact that the cascade rows
  are in general position in the unknown block, which the campaign has never
  established either way. Do not retry with a looser notion of "nearly
  proportional" — approximate proportionality carries no theorem.

**Stop condition.** One pass over the promoted rows. Two non-informative
attempts on the same representation force a redesign per COORDINATION.

**Expected information gain.** Moderate-to-high, and it is the only proof-side
card in this report that is not blocked behind the occurrence theorem.

## 11. `continue / redesign / stop` for the live lanes

* **`TD12-GLOBAL-SOURCE-BRIDGE/v1` (B and S, separate)** — **continue**, with
  a **redesign of the attack order**: try Card C's row-proportionality
  compatibility *before* spending more capacity on obtaining source values.
  The bridge itself is fine; what is stalled is the assumption that source
  data must come first.
* **K00 grade five** — **continue** under its existing owner. My §3 is an
  independent concurrent computation; treat it as cross-check input after that
  lane seals, never as a replacement, and adjudicate any disagreement rather
  than counting agreement as evidence.
* **K00 grade four different-model replay** — **continue**; it is in flight and
  is now higher priority than before, because §3 consumes the grade-four
  survivor's description.
* **Finite-pole full-actual carrier** — **stop** expanding; stays banked. No
  `s >= 3` typed consumer exists and §3 supplies none. Agrees with the packet.
* **`TWIN-ORDER`** — **stop**. It closed `OPEN`; §6.4 explicitly declines to
  revive it on a Gaussian-integer resemblance.
* **B25 `RESROW` `j=17` vacuity / `j=42` frontier** — **continue at review
  only**; no descendant, no `j=42` work without a source-bearing client.
* **LL1-R4 equality profiles** — **stop/defer**, unchanged; no occurrence,
  attainment, or EN-decoration client exists.
* **Systems: capped-process helper** — **continue**, with §9's fd-separation
  refinement and six-case fixture matrix.

## 12. Binding non-claims

Nothing here proves or disproves JC2, exhibits a Keller pair or a polynomial
counterexample, bounds a degree or a covering degree, establishes an
occurrence or a route exclusion, asserts attainment of any floor, or declares
an exit price. Section 3 is a **point-set** statement on the **reduced**
grade-four input with `k10_0 != 0`; it is not a scheme statement, not a
later-grade statement, and not promoted. A surviving formal jet is not a
polynomial map. `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`. A lower floor is
not attainment. The proportionality constants `-1/8, -1/128, -1/1024` are
exact identities on the frozen bytes, not numerical observations. I did not
run, and do not license, any heavy or AWS computation; I did not relabel any
capped historical job; and I did not read, list the contents of, or modify
`jc2-lean`, any peer report, or any file created after this lane started.

No new typed exit price is asserted, so no `charge_basis` line appears.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `35263`.
- Body SHA-256: `ce6be25440230d89cac05ac5cb6717199120a9fd4ab6bf822e6297d152b56aed`.
- Frozen basis: `40c1ab3448209e3d87173feb947a733f6fe54f7f`.
