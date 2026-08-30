# Blind whole-portfolio ideation — Opus 5 — round `20260829T2254Z`

Researcher: Opus 5 (equal-standing whole-portfolio lane)
Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`
Lifecycle: `BLIND_SUBMISSION / PRODUCER_UNREVIEWED / NO PROMOTION CLAIMED`

## 0. Custody and boundary compliance

Recomputed before use, all matching the packet:

```text
d1cc6a649b120253675c1694a2afc4b0c929393cd11f66c99f2635b49185236a  state packet
91e9790dd409103e7f77ebf7ad5fed3e2edf2180a91d3f35b40e62bb816e1d0c  APPROACHES.md
4a96be4e1cd43ee805a0e34cade96bd5c321c5bbeef78568d7b35e96e3f0f62a  AUDIT.md
f947045b4d747efe89a8dadc37ab46e13985ce6099e3bbd40dbd93e3b2489083  COORDINATION.md
b8e57d444f17028ed806bfb0f8831dcbcd0501abacb3b0375a80e3e55c42cff2  PROGRESS.md
7f901db6c8e6fbc80c85581a331c247d5c219e23bf286136f77fbc0182ebbe1b  ladder/REDUCTION.md
87c3821ad161bdd00477f5397138e4e3cd8bf3af7f1c965fb81e9a4aab67d13c  notes.md
76f068f879e658a5588669da329bb6773fcd1c9abc6bb9bda70f150fabd7ae82  xmodel/ideation-20260829T1808Z-synthesis.md
64eaafe3fe5aaa9238a338f2da045e302d9a239ac9c29312e39d5c545893d42c  k00-ram-e2m1-allfaces-uniformity-audit-sol56-20260829.md
96d88f49fd8e2dab1b05d18ac7912d7c1e3374fc474dcfafce29a08558edb62b  k00-unloaded-surface-global-radical-sol56-20260829.md
```

I read no other `ideation-20260829T2254Z-*` artifact, no peer submission, no
prompt, no log, and no run record from this round. No web. No `jc2-lean`
access of any kind. All computation below is local desk-scale exact
characteristic-zero algebra in Singular 4.4.1 (44105) under a 60 s per-process
timeout; every run finished well inside it except one explicitly reported
budget failure (§1.6). No AWS launch was made and none is made by this
report. No exit-price assertion is made, so no `charge_basis` line appears.

## 1. New exact result: the unloaded normal cone and its degeneracy quartic

### 1.1 What was computed and from what

Input is the frozen unloaded prelude
`cases/max12_812_order2_u2_62_k00_unloaded_surface_local_v1_20260829/aws_r6b_global_power_v4/prelude_Q.sing`,
recomputed SHA-256
`5b0a77e6d16df30de2df344862fc4316aedcc8aeabf1ec81e23d7881ce67ee7a`,
which is byte-identical to the value declared in §2 of the charged producer
`96d88f49...`. It defines `I=(r1,...,r7)` in `Q[d0,...,d5]`.

Consuming from the producer only its stated first containment structure, put

```text
f0 = d0-2*d4-d4^2,  f1 = 8*d1-(1+d4)*d3,
f2 = d2-d4-16*d3^2, f5 = d5-2*d3,      J=(f0,f1,f2,f5).
```

`(f0,f1,f2,f5,d3,d4)` is a polynomial coordinate system on `A^6`: the map
`d |-> (f(d),d4,d3)` is a triangular automorphism. So writing `e=(e0,e1,e2,e5)`
for the normal coordinates and `(S,T)=(d4,d3)` for the tangential ones is an
exact change of variables, not a truncation. Under it the reduced surface is
the producer's `D(S,T)=(2S+S^2,(1+S)T/8,S+16T^2,T,S,2T)` and `e=0`.

### 1.2 Confirmations of already-filed claims

Exact reduction gives

```text
I subset J     CONFIRMED
I subset J^2   CONFIRMED     (the separate `I subset J^2` claim, which the
I not subset J^3               integration note `e3e84ac9...` explicitly keeps
                               at its own lifecycle)
```

Therefore the seven rows have zero constant and zero linear part in `e`, and
their degree-2 part in `e` is nonzero for every row. Because `D` is smooth and
`I subset J^2`, the image of `I` in `J^2/J^3 = Sym^2(J/J^2)` is well defined
and independent of the choice of generators of `J`. Explicitly this is a
seven-tuple

```text
Q = (Q_1,...,Q_7),  Q_i in Q[S,T][e0,e1,e2,e5], homogeneous of degree 2 in e,
```

machine-checked homogeneous by `Q_i(lam*e)=lam^2*Q_i(e)`. This is the
intrinsic leading normal form of the unloaded rows along their own reduced
support.

### 1.3 The new object: the degeneracy quartic

Over the function field `Q(S,T)` the ideal `(Q_1,...,Q_7)` has

```text
dim = 0,  vdim = 16,  socle degree 4,  h-vector (1,4,6,4,1).
```

So for generic `(S,T)` the seven quadrics have only the trivial common zero,
and the graded Artinian quotient has the length of a regular sequence of four
quadrics. Saturating by the irrelevant ideal `(e0,e1,e2,e5)` and eliminating
`e` gives a **principal** elimination ideal:

```text
Delta(S,T) = S^3 + S^2 + 72*S*T^2 + 64*T^2 - 432*T^4.
```

**Theorem (K00-NORMAL-CONE-QUARTIC, exact, producer-unreviewed).** For the
frozen unloaded rows, and for every field `K` of characteristic zero and every
`(S_0,T_0) in K^2`, there exists a nonzero `nu in Kbar^4` with
`Q_i(nu;S_0,T_0)=0` for all `i` **iff** `Delta(S_0,T_0)=0`. Equivalently, the
projectivised normal cone of `V(I)` along its reduced support `D` is empty
over exactly the complement of the plane quartic `Delta=0`.

### 1.4 Structure of `Delta`

Machine-verified:

- `Delta` is **irreducible over `Q`** (`factorize` returns the unit and
  `Delta` itself), of total degree 4.
- Its singular scheme has `dim 0`, `vdim 5`, with exactly two minimal primes:
  `(S,T)` and `(3S+4, 27T^2+1)`.
- Local types: at `(0,0)`, `milnor = tjurina = 1`, an **ordinary node**; at
  `(-4/3, ±i*sqrt(3)/9)`, `milnor = tjurina = 2`, a **cusp**. The two cusps
  are conjugate over `Q(sqrt(-3))`.
- `genus(Delta) = 0`. Arithmetic genus 3 minus delta-invariant `1+1+1`
  confirms it: `Delta=0` is a **rational** plane quartic.
- Exact rational parametrisation (verified to reduce `Delta` to zero
  identically):

```text
S(lam) = (lam^4 + 24*lam^2 - 432)/432,
T(lam) = lam*(lam^2 + 36)/432.
```

  `lam=0 |-> (-1,0)`; `lam=±6i |-> (0,0)`, the node, conjugate over `Q(i)`;
  `lam=±2i*sqrt(3) |-> (-4/3, ±i*sqrt(3)/9)`, the cusps; `lam=infinity` is
  the smooth point at infinity `[1:0:0]`, where the line at infinity is a
  four-fold tangent.

- Degenerate-cone dimension in `A^4_e`, machine-checked pointwise:
  `2` at the node `(0,0)`; `1` at the smooth `Delta`-points `(-1,0)` and
  `(4,1)`; `0` at each of `(1,0),(2,1),(3,-2),(-1,1),(5,3)`, all of which have
  `Delta != 0`.
- At the node the degenerate cone is supported on the **linear 2-plane**

```text
P_0 = { e0 = 4*e2,  e5 = -2*e1 },
```

  and `Q` vanishes **identically** on `P_0`, not merely set-theoretically
  (checked row by row).
- Both branches of `Delta` at the node, tangent cone `(S+8iT)(S-8iT)`:

```text
S = +8i*T - 4*T^2 + 4i*T^3 + O(T^4)      and its complex conjugate.
```

  They are conjugate and defined over `Q(i)`, not over `Q`.

### 1.5 Exact reconciliation with already-promoted campaign objects

This is where the new object earns its keep, and where one trap must be
called out explicitly.

**Confirmed identifications (all exact, machine-checked).**

1. The linear parts of the two forms cutting `P_0` are, verbatim, the
   campaign's leading-cone forms:

```text
lin( f0 - 4*f2 ) = d0 - 4*d2 + 2*d4 = B(q)
lin( f5 + 2*f1 ) = 16*d1 - 4*d3 + d5 = A(q)
```

   with full nonlinear completions `f0-4f2 = B(q) - d4^2 + 64*d3^2` and
   `f5+2f1 = A(q) - 2*d3*d4`. So the campaign's leading four-plane `A=B=0`
   is the preimage of `P_0` under the (surjective, 2-dimensional kernel)
   linearised normal projection.

2. The campaign's rank-zero parametrisation is, verbatim, the tangent plane
   of the unloaded surface at the base point:

```text
d/dS D |_(0,0) = (2,0,1,0,1,0),  d/dT D |_(0,0) = (0,1/8,0,1,0,2)
  =>  s*(...) + t*(...) = (2s, t/8, s, t, s, 2t) = ell(s,t).
```

3. The campaign's rank fan is recovered from `Q` alone. Because `Q(.;0,0)`
   vanishes identically on `P_0`, its polar form kills `P_0` and descends to
   `A^4/P_0`. Evaluating the polar map at `nu_x = (4u,-v,u,2v) in P_0` gives a
   `7x4` matrix whose rows 4 and 6 are identically zero — matching the
   published `alpha_4=beta_4=alpha_6=beta_6=0` — whose row 1 is
   `(-3/1024 v, 3/512 u, 3/256 v, 3/1024 u)`, matching the published
   `alpha_1=(3/1024)u`, `beta_1=-(3/1024)v`, and whose ideal of `2x2` minors
   is **exactly**

```text
( u^2 + 64*v^2 ).
```

   That is the campaign's `Delta` rank fan, derived rather than posited.

**The trap, stated so peers do not fall into it.** My tangential quartic has
tangent cone `S^2 + 64*T^2` at the node, and the campaign's rank fan is
`u^2 + 64*v^2`. **These are different objects and must not be identified.**
On the campaign's cone parametrisation
`x=(2b+2u, a, b, 8a+v, b-u, 16a+4v)` the normal part is
`(f0,f1,f2,f5)=(4u,-v,u,2v) in P_0` while the tangential part is
`(S,T)=(b-u, 8a+v)`. So `(u,v)` are coordinates on the **normal** degenerate
plane and `(S,T)` are **tangential**; the shared `64` is a coefficient
coincidence unless someone proves otherwise. I initially matched them and
the check above is what refuted the match. Flag/place/series discipline
applies here exactly as `FALLACY-v2` requires.

### 1.6 Controls, and one honest budget failure

- Positive/negative point controls: seven `(S,T)` samples, listed in §1.4,
  all agreeing with `Delta`.
- Mutation control: replacing `r4` by `r4 + (1/1024)*d4^2*d5^2` changes the
  degenerate-cone dimension at the on-`Delta` point `(-1,0)` from `1` to `0`
  and leaves the off-`Delta` point `(1,0)` at `0`. So the degeneracy is a
  property of the frozen rows, not of the pipeline.
- **Budget failure, reported not hidden:** the full saturate-and-eliminate on
  the *mutated* rows did not finish within 180 s and was killed. I therefore
  do **not** claim a mutation control at the level of the eliminated
  polynomial, only the pointwise control above. The original system's
  elimination finishing in seconds while a one-monomial perturbation does not
  is itself a (weak, uncorroborated) structure signal, and I do not build on
  it.

### 1.7 What this is and is not

It is an exact statement about one frozen unloaded polynomial ideal and its
reduced support. It is **not** a statement about the loaded source
`R(d)+K10*A10(d)+K6*A6(d)+K2*A2(d)-targets=0`, which does not set `I=0`. It is
not a formal arc, an attained source point, ramified coverage, closure
incidence, all-order lifting, algebraization, a polynomial map, a
counterexample, or JC2. Set equality is not scheme equality: `V(I)` is
visibly non-reduced (`I subset J^2`) and nothing here claims otherwise. It
depends on the producer's first containment only, not on its fifth-power
certificates, so it is not blocked by the live Fable review of `96d88f49...`;
if that review overturns `sqrt(I)=J`, §1.3 survives verbatim as a statement
about `J` and its normal cone, while §1.5's interpretation would need
re-typing.

### 1.8 Why this matters for the campaign, stated at the right strength

Two consequences are immediate and one is conjectural.

**(a) It bounds the recentering programme the campaign just licensed
(strong).** The `22:44Z` overlay licenses "exact graph recentering whenever an
unloaded coefficient block vanishes in a reduced ring" and names as the next
theorem target "a graded induction that isolates precisely when the unloaded
block vanishes and records resonant load collisions". §1.3 answers the second
half in closed form: after any such recentering to a surface point
`(S_0,T_0)`, the leading normal analysis is **trivially empty** unless
`Delta(S_0,T_0)=0`. The admissible recentering targets are therefore one
explicit irreducible rational quartic — a single `P^1` of data via §1.4's
parametrisation — plus its one node and two cusps, rather than an
unstructured two-parameter search.

**(b) It explains, rather than re-derives, why the base point is hard
(strong).** The campaign's base point `d=0` sits at `(S,T)=(0,0)`, which is
the **node** of `Delta` — the unique point of the whole surface where the
degenerate cone is 2-dimensional instead of 1-dimensional, and the only
`Q`-rational singular point. Every per-valuation `r in {1,...,5}` and every
per-`(e,m)` cell re-derives the leading four-plane and the rank fan at that
same fixed point, because the tangential centre never moves. The tangential
axis has never been varied in this campaign; `Delta` is that axis.

**(c) A conjectural mechanism with a cheap test (weak, explicitly not a
theorem).** At low grades the loads are absent, so the system is
approximately `R(d)=0` and pushes the normal deviation into the degenerate
cone at each order — which is exactly the "old plane" that every valuation
cell reports. Iterating that heuristic predicts that the tangential
trajectory `gamma(t)=(d4(t),d3(t))` of a deep survivor should have high
contact with `Delta`, hence should satisfy, as formal series,

```text
d4 = ±8i*d3 - 4*d3^2 ± 4i*d3^3 + O(d3^4).
```

That prediction is checkable in minutes against the already-computed
`e=3,m=1` fixture over `Q(i)` that survives `G0--G8`. Note the field: the
branches exist only over `Q(i)`, and the surviving fixture is over `Q(i)`.
I flag that as suggestive, **not** as evidence; a coincidence of quadratic
fields is exactly the kind of thing that must be tested, and §5 gives the
test with both outcomes typed.

## 2. Disposition over all 46 numbered avenues

Default is `unchanged`: this round produced no proof-side arrow and no
attainment, so no avenue's tier moves on proof grounds. Changes below are all
mechanism-level and are argued individually.

| # | Disposition | Reason |
|--:|---|---|
| 1 | unchanged | No new corner/degree-ceiling input. |
| 2 | unchanged (principal) | The selector and ceiling gaps are untouched by this round. |
| 3 | unchanged | Scope limits and Zoladek A.7 priority stand. |
| 4 | **raise (mechanism only)** | §1 supplies the first closed-form obstruction for the formal-germ recentering/algebraization sub-lane: admissible recentering targets are one explicit rational quartic. Tier unchanged; execution priority up. |
| 5–13 | unchanged | No new input. |
| 14 | unchanged | Defensive recon only, as before. |
| 15–18 | unchanged | No new input. |
| 19 | unchanged | Degree-twelve frontier untouched this round. |
| 20 | unchanged | Bridge still consumes false statements. |
| 21 | unchanged | No new Hensel input. |
| 22–26 | unchanged | No new input. |
| 27 | **lower (one sub-lane only)** | The labelled degree-six PALF / `A2`-filling comparison is stopped upstream: the packet records the genus-two `A4` vs genus-one passport mismatch, and a Keller `f` is a submersion, so that filling category is empty. The splice/plumbing avenue itself is unchanged; only the PALF sub-lane drops. |
| 28 | unchanged | BMY still `NEEDS-DATA`. |
| 29–30 | unchanged | No new input. |
| 31 | **reopen (as tool, not as JC2 route)** | The master table records "no direct attempt" and the integration note keeps "Rees-valuation sharpenings" at an open lifecycle. §1 is precisely a Rees/normal-cone invariant of `I` along `J`, executed. Reopen Avenue 31 as the technique owner for the K00 resonance calendar. It is **not** reopened as an integrality proof of JC2. |
| 32 | unchanged | Three-generator presentation is still injectivity. |
| 33–35 | unchanged | No new input. |
| 36 | unchanged (tier), **raise execution** | The campaign files K00/V20R2 here. §1 does not narrow the atlas, so no tier change; it changes how the remaining cells should be attacked (§5). |
| 37–45 | unchanged | No new input. |
| 46 | unchanged, out of scope | Formalization is user-owned and was not inspected. |

## 3. Reranked gaps

### 3.1 Global proof gaps

1. **Global actual-map selector / source completeness.** No arrow from an
   arbitrary minimal Keller counterexample to a bounded td/type/entry/U1
   client. Unchanged at #1; nothing this round touches it.
2. **Absolute or cofinal `td` ceiling.** Without it the finite entry menu at
   each fixed `td` is not a reduction, however complete each book becomes.
3. **Full-configuration landing/coverage** for `b>=2` entries and `M>=2`
   continuations.
4. **`STRICT-COLLIDE-POLY`.** With `Xi = d - s - sum_i b_i` exact and
   atypicality forcing collision but not excess, the live positive input is
   polynomial/rational origin forcing strict quotient weight. Separately the
   global `#atypical >= s-1` bound is still owed.
5. **`G2-PSC`** packet/sheet compatibility (hybrid architectures only).
6. **QCS boundary-complex bridge.** Lowered relative to #4: the pole-incidence
   plus suspension formulation survives, the PALF/`A2` route does not.
7. **`G2-BD`** bounded delay/carrier.

### 3.2 Counterexample and falsification gaps

1. **Reachability/occurrence — raised to #1.** Every K00 result, including
   §1, is a statement about a normalized finite source datum. Nothing sends
   an actual polynomial Keller map to such a datum. §1 makes the jet-side
   geometry cheaper, which sharpens rather than softens this: the binding
   constraint is now clearly on the far side.
2. **Source completeness** of the normalized V20R2 support: `C6=0`, other
   load faces, other supports.
3. **Ramified/valuative coverage** over all `(e,m)`. The `e=3,m=1` fixture
   refutes coefficient-blind induction; §1.8(c) proposes the replacement
   axis.
4. **`R4-00` closure** — the single literal integer cell, with R1+/R1-/R2 unit
   packets `PRODUCER_UNREVIEWED` under active Opus review.
5. **All-order lifting.** A surviving finite jet is not a formal arc.
6. **Algebraization.** An arc is not a germ is not a polynomial map.
7. **char-p / Witt** bounded-degree frontier at maximum twelve.

## 4. New avenue, and new connection between existing avenues

### 4.1 New mechanism: `NORMAL-CONE-ATLAS`

**Novelty: `NEW`.** Repository search over `xmodel/`, `APPROACHES.md`,
`notes.md`, `PROGRESS.md`, `AUDIT.md` finds no occurrence of the polynomial
`432T^4-S^3-72ST^2-S^2-64T^2` or any equivalent, no "projectivised normal
cone" of `V(I)` along `D`, and no statement that `ell(s,t)` is the tangent
plane of the unloaded surface. `I subset J^2` exists as a separate filed
claim and is here `CONFIRMED`, not claimed new; `sqrt(I)=J`, the four-plane
`A=B=0`, the rank fan `u^2+64v^2` and `ell(s,t)` are all `KNOWN` and are
re-derived here from one object rather than posited.

**Content.** Stop stratifying the K00 source by the `Lambda`-valuation `r`
and the ramification pair `(e,m)`. Stratify instead by the pair

```text
( tangential centre/trajectory gamma(t) = (d4(t), d3(t)) in the (S,T) plane,
  normal order rho = ord_t (f0,f1,f2,f5)(d(t)) ),
```

and use `Delta` as the single global discriminant of the leading normal form.
The valuation and ramification indices then enter only through grade
arithmetic against the load calendar, not through a separate geometry each
time.

### 4.2 New connection: Avenue 36/4 (K00 jet atlas) `<->` Avenue 31 (Rees valuations)

**Novelty: `NEW` as an executed link; `KNOWN` as a wish.** The master table
scores Avenue 31 at S:6 for "Rees valuations of one complete boundary book"
and marks it "no direct attempt"; the unloaded-surface integration note
separately keeps "Rees-valuation sharpenings" at an open lifecycle. §1 is
exactly that computation, executed, on the K00 object rather than on a
boundary book: `Delta` is the locus over `D` where the fibre of
`Proj(gr_J(Q[d]/I))` is nonempty, i.e. a Rees-algebra invariant of `I` along
`J`. The campaign's "resonance calendar" is, on this reading, the order-of-
contact data of the trajectory against `Delta`. This gives Avenue 31 its
first concrete client and gives Avenue 36's K00 lane a coordinate-free
language. It does not make Avenue 31 a proof route for JC2.

## 5. Strongest next K00 attack: explicit comparison

Ranked, with the packet's seven named options compared directly.

1. **`R4-00` closure.** *Highest expected value per unit cost, lowest
   information gain.* The rank-zero cell is independently reproduced empty at
   grade 18 by three reconstructions; R1+/R1-/R2 have sealed exact grade-19
   unit packets in review. Finishing it costs review, not new mathematics,
   and closes the literal integer section functor only. **Do not reallocate
   away from it, but do not treat it as the frontier.**
2. **`e=3,m=1` `G9` carry, attacked along the `Delta` branches.** *Best
   information gain per unit cost.* The naive coefficient-blind induction is
   already refuted, so `G9` needs a structural input. §1.8(c) supplies a
   candidate one that is testable before any `G9` computation is launched
   (§7 Card A). Both outcomes are informative.
3. **General ramification/load calendars.** Currently the campaign's most
   expensive axis, because each `(e,m)` re-derives the same fixed-point
   geometry. §4.1 predicts that the geometry is `(e,m)`-independent and only
   the grade arithmetic varies. If Card B confirms the load/`Delta`
   relation, this axis collapses from a family of computations to one
   divisibility statement plus arithmetic. **Highest leverage, medium risk.**
4. **Source completeness.** `C6=0`, other load faces, other supports. This is
   gap 3.2/#2 and is the real blocker on the counterexample side after
   `R4-00`. It is also the axis on which §1 says nothing.
5. **Reachability.** Gap 3.2/#1, the dominant gap. Nothing in this round or
   the last several rounds moves it, and no cheap discriminator is known to
   me. It should keep a named owner precisely because the cheap work is
   elsewhere.
6. **All-order lifting.** Premature: a lifting theorem for cells that are
   being emptied is wasted; revisit only if a cell survives.
7. **Algebraization.** Premature for the same reason, one step further out.

**Recommendation.** Keep `R4-00` review running to completion; put the new
capacity on (2)+(3) via Cards A and B, which share one preregistration and
one compute class; keep one owner on (4); keep (5) named but unfunded this
round; do not start (6) or (7).

## 6. Mathematical-software acceleration

**`K00-SPLIT-COORDINATE-PREPASS`.** Every K00 jet fan to date is compiled and
solved in the raw `d`-coordinates. Because `I subset J^2` (§1.2), each such
solve rediscovers, at every valuation and every `(e,m)`, that the rows carry
no constant and no linear normal part — an order-2 redundancy that is
structural, not arithmetic. Running the same fans in the exact split
coordinates `(e0,e1,e2,e5,S,T)` of §1.1 makes that redundancy a change of
variables instead of a Groebner discovery, and makes the leading rank fan a
`7x4` polar matrix (§1.5.3) instead of a `7x6` differential.

This is a preprocessing change with no mathematical content and therefore no
promotion risk: the coordinate change is a triangular polynomial automorphism,
so the emptiness verdicts are invariant by construction. Acceptance is a
byte-equal verdict on one already-closed cell (valuation two is the cheapest)
plus a recorded wall-clock and peak-RSS comparison. If the verdict differs on
a closed cell, the prepass is wrong and must be discarded, not debugged into
agreement.

## 7. Research cards

### Card A — `K00-DELTA-BRANCH-DISCRIMINATOR`

- **Novelty:** `NEW`. No repository artifact contains `Delta`, its branches,
  or a tangential-contact stratification.
- **Dependencies:** §1.3/§1.4 only (this report). Independent of the live
  Fable review of `96d88f49...` (see §1.7) and of the Opus R1/R2 review.
- **Exact experiment:** take the frozen `e=3,m=1` rank-one fixture over
  `Q(i)` that solves the literal source through `G8`, read off its tangential
  series `d4(t)`, `d3(t)`, and test the two exact conditions
  `d4 = ±8i*d3 - 4*d3^2 ± 4i*d3^3 + O(d3^4)` and `ord_t Delta(d4(t),d3(t))`.
- **Cheapest discriminator:** the single integer `ord_t Delta(d4(t),d3(t))`
  computed from the already-frozen fixture coefficients. Minutes of desk
  arithmetic; no CAS, no AWS, no recompilation.
- **Outcome meanings.** *High or infinite contact:* the ramified survivors
  are the `Delta`-branch arcs; `G9` should then be attacked by substituting
  the branch rather than by a fresh fan, and the `Q(i)` field of the fixture
  is explained rather than coincidental. *Low contact (`ord = 2m`):* the
  tangential axis does not control the ramified survivors; §1.8(c) is
  falsified, §1.8(a)/(b) are untouched, and the ramified atlas keeps its
  current shape. *Contact strictly between:* the survivor is on a nodal
  tangent but off the branch, which localises exactly which order of the
  branch expansion first fails — the most informative outcome of the three.
- **Stop condition:** report the integer and stop. Do not launch `G9` from
  this card; do not extrapolate in `e`.
- **Expected information gain:** high. Every outcome changes the ramified
  plan, and one of them collapses an open-ended family of computations.
- **Compute class:** desk, seconds.
- **Ownership:** prove — the branch-substitution `G9` route; falsify — an
  explicit low-contact reading of the fixture; bypass — `R4-00` closure
  continues regardless.

### Card B — `K00-LOAD-ON-SURFACE-vs-DELTA`

- **Novelty:** `NEW` as posed. The state packet already records the surface
  load degrees "K10 cubic / K6 quadratic / K2 linear" and says they "explain
  the resonance calendar"; no artifact relates any load block to a
  degeneracy locus, because no degeneracy locus existed before §1.3.
- **Dependencies:** §1.3; the frozen loaded compiler
  `compile_contracted_source_v20r2.py` for the three load blocks
  `A10, A6, A2`.
- **Exact experiment:** restrict each load block to the unloaded surface,
  i.e. compute `A10(D(S,T))`, `A6(D(S,T))`, `A2(D(S,T))` in `Q[S,T]^7`, and
  test (i) whether any component is divisible by `Delta`, (ii) whether the
  common zero locus of the seven components of `A10|_D` meets `Delta=0`, and
  (iii) the same for `A6|_D`, `A2|_D`.
- **Cheapest discriminator:** step (i) alone — seven exact divisibility tests
  of small polynomials in two variables. If (i) is negative, run (ii) for
  `A10` only and stop.
- **Outcome meanings.** *Divisibility holds:* the resonance calendar has a
  closed-form cause and the per-`(e,m)` calendar collapses to one divisibility
  statement plus grade arithmetic — this is the single highest-leverage
  outcome available on the counterexample side. *Zero loci meet `Delta` but no
  divisibility:* there is a finite set of genuinely resonant surface points;
  enumerate them and treat them as the only hard centres. *No relation:* the
  load and the unloaded normal geometry are independent, §1.8(a)/(b) stand
  unchanged, and the calendar must keep being computed per cell — a real
  negative result that stops a tempting unification.
- **Stop condition:** stop at the first negative among (i),(ii); do not
  escalate to a full loaded normal-cone computation from this card.
- **Expected information gain:** high on the positive branch, moderate on the
  negative branch (it closes a plausible-looking unification).
- **Compute class:** desk if the load blocks restrict cheaply; **preregister
  AWS** if the restriction exceeds the desk cap, since the state packet
  reserves heavy or uncertain CAS to AWS. Do not launch during a blind round.
- **Ownership:** prove — the divisibility identity; falsify — an explicit
  non-vanishing evaluation at one `Delta`-point; bypass — the per-cell
  calendar continues meanwhile.

### Card C — `QCS-RATIONALITY-OF-COLLISION-PARTNERS`

- **Novelty:** `KNOWN` direction, `NEW` mechanism. The packet already
  isolates "polynomial/rational origin" as the next strictness input and
  records that the type-`(2,3)` analytic surrogate's forced square root is
  nonrational. What is new is proposing a **field-of-definition / Galois
  descent** argument rather than a further case analysis.
- **Dependencies:** the promoted `Xi = E_gen-(s-1) = d - s - sum_i b_i` and
  the reviewed Section-7 quotient package; the reviewed type-`(2,3)`
  surrogate as the negative control. **It does not depend on any residue-A
  template**, which is `UNDERDETERMINED(first_absent=PairRef)` and must not
  be used as a source.
- **Exact statement to attempt:** for an actual polynomial pair and an
  atypical value `c in C`, the quotient-line data at `c` is defined over the
  residue field at a `C`-point of the base, hence over `C` itself; show that
  a zero-excess collision forces the two colliding quotient lines to be
  conjugate under a nontrivial quadratic extension of the field generated by
  the profile data. Contradiction gives `STRICT-COLLIDE-POLY`.
- **Cheapest discriminator:** exhibit, or prove impossible, one
  source-compatible **polynomial-origin** germ realising a zero-excess
  collision with all profile data rational over the base field. One witness
  falsifies; a proof of impossibility proves.
- **Outcome meanings.** *Witness found:* `STRICT-COLLIDE-POLY` is false and
  QCS must be reached through the boundary-complex route or abandoned.
  *Impossibility proved:* `E_gen >= #atypical` follows, and the separate
  global `#atypical >= s-1` bound becomes the sole remaining QCS obligation —
  which must be stated as still open, not absorbed. *Neither within budget:*
  return typed `OPEN`; do not fill by analogy with the analytic surrogate,
  which is a control and not a source.
- **Stop condition:** stop at a witness, or at a bounded search over the
  reviewed germ family; do not start an unrestricted mapping-class or Kirby
  search — the packet forbids it and the PALF comparison is already stopped.
- **Expected information gain:** moderate-to-high, and it is the cheapest
  live proof-side card I can construct that does not require the missing
  global selector.
- **Compute class:** desk plus literature-free symbolic work; no AWS.
- **Ownership:** prove — the descent argument; falsify — the germ witness;
  bypass — the pole-incidence/suspension boundary-complex formulation, which
  remains a separate live route and is not owned by this card.

## 8. Global selector and QCS portfolio

**Selector — prove.** The only reviewed chain remains `JC2 false -> some
globally GGV-minimal standard pair -> Sigray-normalized, td preserved ->
td>=6 -> finite entry menu at each fixed td`. The missing arrow is a bound,
and GGV minimality minimizes a base-scale invariant rather than `td`. The
honest prove-side target is therefore a **second minimisation** inside the
Sigray frame with a well-order that the book machinery controls, not a
re-derivation from GGV data.

**Selector — falsify.** The `U1*(R)` family for every odd `R>=3` already
shows that the reduced merge/trunk/budget interface admits type `(2,3)`,
`R` poles, `td=4R`, U1, and a T1-compatible P1 continuation. That is a
standing refutation of any selector built from that interface alone, and it
should be cited as such rather than re-tested.

**Selector — bypass.** The strongest bypass available is to abandon the
`td`-indexed architecture for a `td`-free invariant. I have no such invariant
to offer and I decline to name a candidate I cannot type; this stays `OPEN`.

**QCS — prove / falsify / bypass.** Card C owns prove and falsify. The bypass
is the pole-incidence boundary complex with a suspension of its cycle space
onto `H1(F)`, which would give QCS by rank-nullity. Its precondition is one
**common labelled** surface/boundary packet; bare positive filling data cannot
force the incidence or suspension maps, and the degree-six PALF comparison is
stopped upstream. Note also that a `PASS` on Card C yields only
`E_gen >= #atypical`; `#atypical >= s-1` remains separately owed, and no card
in this report addresses it.

## 9. Campaign-systems card

**`UPGRADE` — `ADAPTER-PREFLIGHT`.**

**Evidence of the gap.** `ops/adapters/{claude,codex,grok,opus}.sh` total 44
lines and contain no status, exit-code, credit, or health handling — verified
by inspection. This round's packet records that Grok returned HTTP 402 with
its balance exhausted *before* the all-face review began, costing a full
blind lane, and separately that a long Fable attempt hit a 64,000-output-token
ceiling with no report, an operational non-verdict. Neither failure was
detectable before the prompt was dispatched. `grep` over `ops/` finds no
preflight or health check, so this is not a duplicate.

**Change.** Add `ops/adapters/preflight.sh`: for each configured adapter,
issue the cheapest authenticated request under a hard timeout, and emit one
line per provider of the form
`provider=<name> status=<code> latency_ms=<n> verdict=<AVAILABLE |
UNAVAILABLE_NO_MODEL_WORK | DEGRADED>`. Round dispatch consults it and
reallocates an unavailable lane before charging any prompt. Separately, make
each lane declare its output-token budget and checkpoint at 80% of it, so a
ceiling produces a partial typed report rather than nothing.

**Smallest measurable acceptance test.** On synthetic fixtures only, never
against a live provider or the fenced formalization tree: (1) a stubbed
adapter returning 402 yields `UNAVAILABLE_NO_MODEL_WORK` and **zero prompt
bytes written**, asserted by byte count; (2) a stubbed healthy adapter yields
`AVAILABLE`; (3) a stubbed hang is classified `DEGRADED` by timeout, not left
pending; (4) total preflight wall time under 10 s for all four adapters; (5)
a stubbed lane driven past its declared budget emits a checkpoint artifact
whose body ends in a well-formed marker. Five assertions, all offline.

**Non-goals.** No change to `ops/lane.sh`, no automatic top-up, no
mathematical claim depends on it, and it must stay opt-in until the diff has
ordinary software review.

## 10. Provisional descendants that may start without waiting for review

- Card A (§7) depends only on this report's §1.3/§1.4 and frozen fixture
  coefficients. It may start immediately.
- The §6 split-coordinate prepass may be built and validated against an
  already-closed cell immediately, since its correctness is a change of
  variables.
- Card B's step (i) may start as soon as the load blocks are extracted; its
  escalation to AWS may not be launched from a blind report and must be
  preregistered.
- Promotion of anything in §1 still requires different-model hostile review.
  Nothing here is promoted by this submission.

## 11. Nonclaims

This report does not prove or disprove JC2, does not close `R4-00`, does not
close any ramification or load face, and does not rerank any avenue's tier on
proof grounds. §1 concerns one frozen **unloaded** ideal; it says nothing
about the loaded source, which does not set that ideal to zero. A finite jet
is not a formal arc, an algebraic germ, a polynomial map, a counterexample, or
a JC2 result; a surviving prefix is not attainment; equality of sets is not
equality of schemes; `Delta` is a locus on the tangential plane and is **not**
the campaign's normal-plane rank fan `u^2+64v^2` (§1.5). One mutation control
failed to complete inside budget and is reported as such (§1.6). No exit price
is derived or asserted. No formalization evidence was inspected or consumed.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `34609`.
- Body SHA-256:
  `2b9e2f08f4e58252d984944a34e9d78fa5b596bfe1a350aadc073ed39d393b30`.
- Frozen basis: `0f7ee003be45ee40d51d4048897cdacf63821172`.
