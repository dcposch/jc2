# Global-source stop gate (Fable 5.1, independent structural co-researcher), 2026-09-14

Lane: `global-source-stop-gate-fable5-20260914`. Started 06:12:53 UTC. Substantive deadline 06:32 UTC, HARD 06:36.
Tier: MANUAL, UNPROMOTED, no computation. Charged inputs (read whole, bounded chunks, hashed before and after):

- `COORDINATION.md` sha256 `a14b2ebcb3841f175b52ef0a96835a5724aee06a6008442eb3d25f98194a99bc` (840 lines, 50885 bytes; 14 reads of <=60 lines, no clipping)
- `APPROACHES.md` sha256 `d4984049c6742aa45495a91198a96a8fdb22c0c37479a64dbc6ad059078a4ac6` (618 lines, 92879 bytes; 31 reads of <=20 lines, no clipping)

Authoring: `apply_patch` only (skeleton first, sections appended). No links followed, no live ledgers, no CAS, no network.

## 1. Scope verdict on the stopping rules

**Verdict: NO_SCOPE_ERROR.** I checked every stop in APPROACHES sections 5 to 9 against
the question "does it forbid a mechanism that a full polynomial Keller source
`C[x,y]` could actually feed?" Each stop names one exact missing premise, and in every
case the premise is one that full-plane data (UFD, `R^x = C^*`, `Pic = 0`, simple
connectivity, finite etale `A2 \ F^{-1}(D) -> A2 \ D`) does not supply on its own:

- TRACE-CUTOFF stop: the missing premise is invertibility of `uv` in a nonzero factor.
  Normality of `T` lifts idempotents but a factor of a normal ring containing `u,v`
  with `uv` a unit would have to be a localization, and no source datum forces it.
  Correctly scoped.
- Collision/unit stop ("arbitrary connected off-component units are not proved
  constant"): a genuine GAP, not an over-broad stop; Section 2 attacks it with a
  changed hypothesis and reaches the same wall from a different side.
- Conductor division / radial descent stops: the recorded controls (pinching control,
  Euler-descent control) are full-A2 counterobjects to the RELAXED criteria, so those
  stops are minimal.
- Ramification-under-base-change: the prompt's own clarification is right; the residual
  cover `W` below is finite over the source plane but ramified along `p_2^{-1}(Ram pi)`,
  and nothing in the full pullback removes that ramification.
- Generic-fibre genus and involution linearization: the recorded endpoints (Chau
  Theorem 2 duplicate; central-inversion conjugacy without pole control) are primary-
  text facts, not campaign policy; a stop cannot be "too broad" about a theorem.

The one thing I would NOT relabel as harmless: the map's sentence "abstract collision
geometry, even with that polynomial-difference property, does not recover full-plane
source origin" is an essential hypothesis statement. Section 2 keeps full-plane origin
as the hypothesis and tests whether it is enough. It is not, yet.

## 2. Selected attempt: units and ramification on the relative finite compactification of the off-square

**Literal objects.** `A = C[f,g] <= R = C[x,y]`, `J(f,g) = 1`, `F: Spec R -> Spec A`.
`L = Frac A`, `K = Frac R`, `N = [K:L] >= 6` (accepted Zoladek tier). `B` = integral
closure of `A` in `K`; `B` is finite over `A` (finite type, `K/L` finite separable).
`B <= R` because `R` is normal and integral-over-`A` implies integral-over-`R`.
`Y = Spec B`, normal affine surface; `pi: Y -> A2_target` finite of degree `N`, flat
(normal surface is CM, target regular).

**Step 1 (open immersion; standard, rederived for literalness).** `C := R (x)_A B` is
etale over `B` (base change of the etale `A -> R`), hence normal. Its generic fibre
`K (x)_L K = K x K'` with `K'` of left-`K`-rank `N-1`. The diagonal idempotent `e` lies
in the total quotient ring of the normal ring `C`, hence `e` is in `C`. `eC` is a finite
left-`R`-algebra, a domain with fraction field `K`, so `eC = R` (`R` normal). The
multiplication map `mu: C -> K`, `r(x)b -> rb`, is a ring map with `mu(e) = 1`, so
`mu(C) = RB = R`. The `B`-structure on the factor `eC = R` is the inclusion `B -> R`,
etale as an open-closed piece of `C -> B`; etale + birational + normal target gives an
open immersion (Zariski main theorem). So `A2_source = Spec R` is open in `Y`,
`E := Y \ A2_source` is a curve (complement of an affine open in a normal variety is
pure codimension one), and `D := pi(E)` is the nonproperness curve.

**Step 2 (the relative finite compactification).** `C = R x C'`, `W := Spec C'`.
`p_1: W -> A2_source` is finite of degree `N-1`; `p_2: W -> Y` is etale. Because an
open immersion is a monomorphism, `R (x)_A R = C (x)_B R = (R (x)_B R) x (C' (x)_B R)
= R x (C' (x)_B R)`. Hence the off-square `W' := Spec R'` equals `p_2^{-1}(A2_source)
= W \ Delta_W`, `Delta_W := p_2^{-1}(E)` a reduced curve, with `p_1(Delta_W) =
F^{-1}(pi(E)) = F^{-1}(D)`. So the off-square, whose two projections are etale and
nonfinite, is the complement of a reduced curve inside a scheme FINITE over the full
source plane. This is the prompt's "residual degree `N-1` cover"; I claim no novelty
for the object, only for the use below.

**Step 3 (ramification transfer).** `F p_1 = pi p_2`. Since `F` is etale, `p_1` is
etale at `w` iff `F p_1` is etale at `w` iff `pi p_2` is etale at `w` iff `pi` is etale
at `p_2(w)` (etale cancellation, `p_2` etale). Zariski-Nagata purity (`Y` normal,
target regular, `pi` finite): the non-etale locus `Ram(pi)` is pure of codimension one
in `Y`, contained in `E`, and nonempty (else `pi` is finite etale onto the simply
connected target plane and `N = 1`). Therefore `p_1` is a finite normal cover of the
FULL plane, branched exactly along `Delta := p_1(p_2^{-1}(Ram pi)) <= F^{-1}(D)`,
with local monodromy around a component of `F^{-1}(D_1)` equal to the local monodromy
of `pi` around `D_1` with the base sheet deleted. Over `A2_source \ F^{-1}(D)` the
monodromy of `p_1` is the point stabilizer `G_1 <= G <= S_N` on the other `N-1`
sheets, because `A2_source \ F^{-1}(D) -> A2_target \ D` is finite etale of degree `N`.
Components of `W` correspond to `G_1`-orbits, i.e. to the map's blocks. KNOWN.

**Step 4 (claimed implication, attacked).** Target statement U: for every connected
component `W'_0` of the off-square, `O(W'_0)^x = C^*`. By the map (Section 8, collision
priority identification) U would exclude every regular scalar pair on the pseudo-plane
`S`, because such a pair keeps the unit-carrying `L` as a component of its off square.
Changed hypothesis relative to the recorded GAP: instead of abstract collision geometry,
use `W'_0 = W_0 \ Delta_{W_0}` with `W_0 -> A2_source` FINITE, plus `R` a UFD and
`R^x = C^*`.

Derivation. Let `u` be a unit of `O(W'_0)`. On the normal surface `W_0`,
`div(u) = sum_k a_k Delta_k`, the `Delta_k` being the components of
`Delta_{W_0} = p_2^{-1}(E) ∩ W_0`. The norm `N_1(u) := Nm_{W_0/A2}(u)` lies in `K` with
divisor `p_{1*} div(u)` supported on `F^{-1}(D) = V(h_1 ... h_s)`, `h_i` irreducible in
the UFD `R`. Hence

`N_1(u) = c h_1^{m_1} ... h_s^{m_s}`, `c` in `C^*`, `m_i = sum_{Delta_k over V(h_i)} a_k f_k`,

where only sheets lying in `Delta_{W_0}` contribute (sheets in `W'_0` over a generic
point of `V(h_i)` carry neither zero nor pole of `u`), and `f_k` is the residue degree of
`Delta_k -> V(h_i)`. The same holds for `u^{-1}` with negated exponents, and for the
finite second projection `q_2: Z_0 -> Y` on the normalized closure `Z_0` of `W'_0` in
`Y x_{A2} Y`, with divisor on `Y` supported on `E ∪ q_2(q_1^{-1}(E))`, whose restriction
to `A2_source` is again `F^{-1}(D)`. Full-plane data therefore constrain every norm to
the group `C^* x Z^s` and nothing more.

**First unresolved step (GAP-U1).** Show that `sum_k a_k [Delta_k] = 0` in `Cl(W_0)`
forces every `a_k = 0`. Equivalently, by the localization sequence
`0 -> O(W_0)^x -> O(W'_0)^x -> (+)_k Z Delta_k -> Cl(W_0) -> Cl(W'_0) -> 0`,
GAP-U1 is exactly `O(W'_0)^x = O(W_0)^x`. What full-plane data DO give is the same
statement one level down: for `Y` itself the sequence reads
`0 -> O(Y)^x -> R^x -> (+)_j Z E_j -> Cl(Y) -> 0`, and `R^x = C^*` forces the
boundary classes `[E_j]` to be `Z`-independent in `Cl(Y)` (a small exact fact I did
not find stated in the map; it is not new mathematics, but it is the correct form of
the full-plane input here). It does NOT transfer to `W_0`: `p_2` is etale but not
finite, so there is no pushforward `Cl(W_0) -> Cl(Y)`, and a nonfinite etale map onto
the plane can carry nonconstant units (the punctured plane is such a map). I could not
exclude a nonconstant unit on `W'_0` this way.

**Second unresolved step (GAP-U2).** Even with all `a_k = 0`, `u` is a unit of the finite
normal `R`-algebra `O(W_0)` with constant norm, and such units need not be constant:
`t^2 = x^2 + 1` over `C[x,y]` has the unit `x + t` of norm `-1`. Any proof of U must use
that `W_0 -> Y` is etale and that `Delta_{W_0}` is the pullback of `E`; the norm
bookkeeping above does not see either. This is the same wall the map records from the
collision side ("even constant norms have a nontrivial kernel in the localized
control"), now reached from the finite side. No new closing mechanism.

**Dependency path to JC2.** U (proved) -> no regular scalar pair on `S` (map's own
attachment) -> closes the S/T construction front only; it is NOT a proof route, and
its failure (a nonconstant unit on some `W'_0`) is not a counterexample. The unit `x+t`
control shows a proof of U cannot be a pure finiteness/UFD argument; it needs GAP-U1
and GAP-U2 with the etale-over-`Y` structure, which is exactly the block/normality data
the map already lists as open.

## 3. Cheapest changed decisive test

**Verdict: NO_NEW_MECHANISM for a runnable full-source test.** The discriminator for U
is exact but needs `B`, which no actual source supplies. Stated so a future source can
be tested without reinterpretation:

- Test T1 (GAP-U1): on each component `W_0` of `Spec (R (x)_A B)'`, decide whether the
  boundary classes `[Delta_k]`, `Delta_k <= p_2^{-1}(E)`, are `Z`-independent in
  `Cl(W_0)`. A relation gives a nonconstant unit on `W'_0` and kills U; independence
  is necessary for U but not sufficient.
- Test T2 (GAP-U2): decide `O(W_0)^x = C^*`. Failure kills U; success with T1 gives U
  and, through the map's collision attachment, excludes all regular `S` scalar pairs.

Neither outcome decides JC2. The only cheap manual control I can offer without a
source is the recorded punctured-plane control: its off square `L` is `C^* x A1`, the
first projection `L -> {x != 0}` is an isomorphism, so the unit `x` has NONCONSTANT
norm `x`, and the norm filter of Section 2 correctly attributes it to a source unit.
On a full plane that attribution is unavailable, which is why T1/T2 are the remaining
content. No instrument, worker, or CAS run is selected.

## 4. Reopening evidence and deviations

**No automatic successor.** Reopen the unit question only if one of these appears:
(a) a proof or counterexample to T1 on ANY finite normal `Y >= A2` with `A2` open,
`pi` finite, and `W_0 -> Y` etale, i.e. on the abstract shape without a Keller pair;
(b) an actual source `B` (a Keller counterexample candidate at the accepted degree
scope), in which case run T1/T2 by hand on its components before any Grobner work;
(c) a theorem giving `O(W'_0)^x = O(W_0)^x` whenever `W_0` is finite over the plane
and etale over such a `Y`, which would discharge GAP-U1 outright (the `Cl(Y)`
independence of the `[E_j]` is already forced by `R^x = C^*` and is not enough).

**Deviations disclosed.** None on tooling: two charged reads only, bounded chunks
(60/20 lines), no clipping recovered because none occurred, `apply_patch` for every
write, no network, CAS, or ledger access. Content deviation: the selected attempt does
not reach a decisive test; it converts a recorded GAP into two exact sub-gaps
(GAP-U1, GAP-U2) and shows finiteness plus UFD data cannot close them. Sections 1 and 2
were written after the whole of both inputs was read; no personal inherited-read
claim is made.

Post-authoring hashes (recomputed after all content, before the marker):
COORDINATION.md `a14b2ebcb3841f175b52ef0a96835a5724aee06a6008442eb3d25f98194a99bc`,
APPROACHES.md `d4984049c6742aa45495a91198a96a8fdb22c0c37479a64dbc6ad059078a4ac6`
(verified in the readback step; if the recomputation had differed, this line would
say so).

<!-- BODY-END -->
