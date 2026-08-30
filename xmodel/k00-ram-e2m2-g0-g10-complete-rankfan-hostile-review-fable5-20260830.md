# Hostile review: generic K00 `e=2,m=2` complete rank/transition fan through G10

Date: 2026-08-30
Reviewer: Fable 5 (different model from the Sol 5.6 Ultra producer)
Review basis: `0d7544ebd5cb12def6bac892646010301098be3c` (contains the producer's
frozen basis `0f7ee003be45ee40d51d4048897cdacf63821172`)
Target: `xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-sol56-20260829.md`
(body 14580 / `510f81b8...`) and its replay
`xmodel/k00-ram-e2m2-g0-g10-complete-rankfan-replay-sol56-20260829.py`.

## Verdict summary

**CONFIRMED.** Every displayed equation, every rank chart, every terminal,
the retention claims, the K10 cancellation, the odd-branch strictness claim,
and the point-set-emptiness conclusion (0.2) were independently reconstructed
from the frozen tails and survived. Several steps the producer argued by
census I closed computationally with strictly larger retained slot sets, and
two sufficiency-only steps I upgraded to necessity. Two minor errata (a stale
byte count in prose, one vacuous-by-construction mutation control) and two
scope notes; nothing touches soundness. Itemized verdict in section 10.

## 1. Custody and seal (attack 1)

All hashes verified at the review basis before any mathematics:

- Target report `fa5a4ef6...` and replay `efd2f4fe...`: match; both tracked
  at commit `0d7544eb`.
- Body seal: bytes 0..14580 of the report hash to
  `510f81b84a4d965962f8c07ee261beaa8912e5a05baf206b80ffe88a7e67f637`; the
  `<!-- BODY-END -->` line is unique and standalone at byte 14562; the seal
  footer sits outside the body as declared.
- All nine charged source hashes match (`tails.json d72f774c...`, compiler
  `2ac7653c...`, engine `2c918d5b...`, the three m=1 regression packets, my
  prior Fable review `0ee84a0b...`, and the e3m1 pair `22e97527...` /
  `bcd4004e...`).
- Additional pins I verified beyond the charge: the Singular prelude
  `serialized_replay_prelude_Q.sing` matches the compiler's expectation
  `5b0a77e6...`; the canonical (semantic) tails digest equals the compiler's
  `EXPECTED_CANONICAL_TAILS = 6eed03d4...`; the V21 input manifest matches
  `38c6dd45...` and its `load_K10/K6/K2.txt` entries match their listed
  hashes.

## 2. Reviewer engine and independence (attack 7)

I wrote a from-scratch exact engine (`/tmp/e2m2rev/`, five scripts, pure
Python stdlib, `Fraction`-pair Gaussian rationals, own sparse polynomial and
tau-series arithmetic, own tails parser, own chart constructors). It imports
no producer code. Script hashes for the record: `revlib.py 89cd3505...`,
`stage12.py 9671dcc4...`, `stage34.py 3b693374...`, `stage56.py c83d4c82...`,
`stage4b.py 4d62773e...`; combined run log `609f9ef6...`, 60 lines, all
green, total runtime under 6 seconds.

Shared-code exposure and how it is closed. The producer replay imports the
charged r=2 engine for `reconstruct_rows` and all ring arithmetic, so a
coordinate-map or parsing defect there would cohere across both producer
artifacts. My engine rebuilds the seven unloaded rows and the three load
ideals from `tails.json` independently and cross-checks them against two
artifacts produced by a different toolchain in a different lane: the
Singular prelude rows `r1..r7` (my own `ast`-based parser; exact dictionary
equality) and the V21 `load_K10/K6/K2.txt` serializations (exact equality).
A deliberately perturbed row is caught by the prelude comparison (control).
Residual trust is confined to the frozen 569-monomial `tails.json` itself,
which is charged as frozen upstream input and is outside this review's
scope.

Positive controls and real source mutations run in my engine: the exact
surface identity breaks under `16T^2 -> 15T^2` and under a one-coefficient
in-memory bump of row 1; the odd fixture breaks at G8 (rows 1,2,3,5,7) under
`-128 -> -127`; the rank-one G10 terminal has no `k10[0]`-free part, so
deleting the K10 open removes the kill.

## 3. Source reconstruction and honest calendar (attack 2)

Census: 569 tails, per-row counts (36,54,58,81,89,120,131); every monomial
has 10 slots, weight `12+ell` under weights `(8,7,6,5,4,3,2|2,6,10)`, load
slots in `{0,1}` with at most one active. Reconstructed unloaded rows have
term counts (16,23,27,36,40,42,57) and minimum degrees (2,2,2,2,2,3,2) —
row six starts cubic, which is why it is the recurring decisive cokernel
row. `Q6 = hom_2(R_6) = 0` confirmed.

Shift convention: the compiler applies Lambda-shifts 2/6/10 to k10/k6/k2 and
14/16/18/19 to mu2/mu4/mu6/Jdet; at `Lambda=tau^2` this is
`tau^4 k10, tau^12 k6, tau^20 k2` and targets from `tau^28`, exactly (1.1)
and consistent with the `tau-shift = e x Lambda-table` convention pinned in
the e3m1 review. Calendar, independently recomputed:

- K10 globally: `A10` rows all have quadratic bottom (min degree 2), so
  first possible load grade is `4+2*2 = G8`.
- K10 on the exact surface: `A10_r(D(S,T))` has minimum `(S,T)`-degree
  `[3,3,3,none,3,4,3]`, i.e. G10 for rows 1,2,3,5,7, G12 for row 6,
  identically zero for row 4. Matches the producer table and (1.2).
- K6 per-row first grades on the positive faces: `[15,15,15,17,15,17,15]`;
  K2: all 23; mu2/mu4/mu6/Jdet: 29/33/37/38. Matches the table exactly.
- Stronger than claimed: the shifts alone (`tau^12`, `tau^20`, `tau^28+`)
  already exceed G10, so no K6/K2/target coefficient can reach G10 on ANY
  face, including order-zero faces outside the declared cell. The claimed
  positive-face uniformity is therefore trivially exceeded through G10.

Retained-slot audit: my charts carry, at every decisive grade, strictly more
slots than the producer's (surface `S4,T4,S5,T5`, kernel coordinates at all
normal levels, full `N7` and `N8` blocks at the G10 gate, `k10[0..6]`), and
prove the extras absent rather than omitting them; details in sections 5-6.

## 4. Exact surface, gradient lemma, recentering (attack 3)

Verified in `Q[S,T]`: `D(S,T) = ell(S,T) + mu(S,T)` exactly, all seven
`R_r(D(S,T)) = 0`, and all 42 gradients `(dR_r/dd_j)(D(S,T)) = 0` — the
gradient lemma from my 20260829 review (`R_r` in `J^2`), now exercised
directly. In addition I proved the sharper radical fact that powers the
whole fan: **for every row, `DQ_r(x)[ell(alpha,beta)] = 0 identically in
x`** — the tangent plane lies in the radical of every leading quadric. (The
analogous statement is false for the K10 quadrics `M4_r`: I checked, the
plane is not in the radical of `M4`; only `M4_r(ell) = 0` and the polar of
`ell` against `V(A,B)` vectors vanish. This is exactly why the `mu`-part
survives into the `W_r` cubics while the plane and cone directions do not.)

Recentering soundness. The decomposition `d = D(S,T) + N` is
non-canonical; at each rank-zero transition the plane component of the next
`N` coefficient is moved into `(S,T)`. This is a triangular change of
variables on the jet space (later coefficients shift by amounts determined
by earlier data and remain free), hence a bijection on solution sets; and
every G-equation is invariant under it because `Q(x - ell) = Q(x)` and
`DQ(x)[ell] = 0` by the radical fact. The direct sum
`V(A,B) = plane(a,b) + ray(p,q)` with `ray = (2p,0,0,q,-p,4q)` was verified
(trivial intersection), so absorption leaves exactly the ray coefficient:
no odd column is deleted, matching (2.3). The fixture and the forced
`N5 != 0` on the odd branch (section 7) independently witness that odd
columns are alive in the compiled system.

## 5. Cone geometry and rank-fan structure (attacks 3-4)

All verified independently, over `Q(i)`:

- `V(Q1..Q7)` contains `plane + ray = V(A,B)` (`A = v5+16v1-4v3`,
  `B = v0-4v2+2v4`), and conversely on the section `vab(A,B,y)`:
  `Q_4 = (3/2^19)(B^2-64A^2)` and `Q_3+(1/8)Q_1 = (3/16384)AB`, both free of
  the kernel coordinates `y`. `AB=0` and `B^2=64A^2` force `A=B=0`, so
  **`V(Q)_red = V(A,B)` set-theoretically** — the two-line reduced-cone
  proof, reconfirmed on this compiled source.
- The DQ factorization on the cone: all 42 identities
  `dQ_r/dx_c(plane+ray) = avec_c*alpha_r + bvec_c*beta_r` with exactly the
  producer's alpha/beta lists; alpha,beta depend only on `(u,v)=(p,q)`, so
  the rank is a function of the ray part alone. Exactly four nonzero 2x2
  minors, each a constant times `Delta = p^2+64q^2`: rank two iff
  `Delta != 0`, rank one iff `Delta = 0, (p,q) != 0` (then `p = eps*8i*q`,
  `q != 0`), rank zero iff `p=q=0`. On the rank-one chart the single
  surviving functional (row 2: `(3q/16384)(64A + eps*8i*B)`) has kernel
  exactly `B = eps*8i*A` — necessity, not just sufficiency.
- Fresh cone/tangent (2.4) for `n = 2,3,4`: with fully general 6-vector
  residual and tangent and with `alpha,beta,S4,T4,k10[0..2]` retained, all
  grades below `2n` vanish, `G(2n) = Q(N_n)`, `G(2n+1) = DQ(N_n)[N_{n+1}]`,
  and the retained extras are absent. This proves the K10 sector cannot
  touch `G(2n)` or `G(2n+1)` for these `n`, licensing the producer's
  `k10 = 0` shortcut inside the n=3 G8 computation.

## 6. The complete fan and its terminals (attack 4)

Every chart below was rebuilt literally in my engine (own construction,
extra retained slots) and every displayed constant matched.

**n=2, rank two (dead G6).** G0..G5 vanish on the chart; G6 is free of
`alpha,beta,S4,T4`, the tau^4 kernel coordinates, and all k-slots (proved,
not assumed). Row six `= p(192q^2-p^2)/65536` (3.1). The five cokernel
combinations are homogeneous cubics in `(s,t,p,q)` only, which licenses the
`q=1` slice on each branch. Branch `p=0` (`q != 0`): row four
`= (3/512)s q^2` forces `s=0`; then (3.2) demands `t=-8q/3` and `t=-4q`
simultaneously — empty. Branch `p^2=192q^2` (`q != 0` forced): in
`Q[t,r]/(r^2-192)` row four is exactly `(-3/256)(s + r(t+2))` — a unit times
the substitution, so `s=-r(t+2)` is **forced** (my stage-4b closes this
necessity step, which the producer only exhibited as a vanishing
substitution); then (3.3) evaluates to the units `1/8` and `-1/64` — empty.
Since `192` is not a rational square the quotient argument covers both
square roots over the closure.

**n=2, rank one (dead G6).** On both `eps` charts, G0..G5 vanish and
`G6_6 = eps*i*q^3/32` (3.4), nonzero on `q != 0`. Consistency check: (3.1)
at `p = eps*8iq` equals `eps*i*q^3/32` — the two displays agree.

**n=2, rank zero.** `d_2 = ell(s,t)`, the open becomes `(s,t) != (0,0)`,
G5 is vacuous (plane radical), recenter to `n>=3`. Correct.

**n=3, rank two (dead G8).** G0..G7 vanish; G8 is free of
`alpha,beta,S4,T4,S5,T5`, the tau^5 kernel coordinates, and all k-slots.
The augmented determinant of rows 1,2,3 equals `(27/2^35)*Delta*C` and row
four equals `(3/2^15)*E` with (4.1) exactly; `det(C,E)` as a linear system
in `(s,t)` is `-Delta^2` (desk-checked: `256p^2q^2+(64q^2-p^2)^2 =
(p^2+64q^2)^2`), so `s=t=0` on `D(Delta)`, contradicting the open. The
y-terms entering through image directions cancel in the determinant by
column operations, which the assertion itself certifies.

**n=3, rank one: the odd G8 survivor (dead G9).** F3, F4 match (4.3); the
wall combination forces `s = eps*8i*t` and the root then forces
`X = A(N4) = 0` (4.5). For (4.6) I added a necessity variable `w` measuring
the deviation `B(N5) - eps*8i*A(N5) + 128tq`: on the survivor chart every
G8 row is an **exact multiple of `w`**, with at least one row's coefficient
a nonzero constant times `q` — so (4.6) is necessary on `q != 0`, not
merely a sufficient parameterization. With `w=0`, G0..G8 vanish identically
with `alpha,beta,S4,T4,S5,T5`, the N4 kernel, the five-dimensional N5
fiber, the full N6 block, and `k10[0..5]` all retained; and
`G9_6 = eps*i*q^3/32` while the K10 row-six load has zero tau-coefficients
through grade 5, so no `k10[0..5]` value can rescue row six. Dead at G9 on
`q != 0`. The survivor is a genuine constructible G8 component for each
sign — see section 8.

**n=4 final fan (all ranks dead G10).** One chart, truncation 11, with
surface slots through tau^5, `ray(p,q)` at tau^4, general `N5`, `N6`, and —
beyond the producer — **full free `N7` and `N8` blocks** and `k10[0..6]`.
Results: G0..G8 vanish; `G9 = alpha(p,q)A(N5) + beta(p,q)B(N5)` exactly;
G10 is free of `alpha,beta,S4,T4,S5,T5`, every `N7` and `N8` coordinate,
and `k10[1..6]` — the deviation-grade census of the producer's section 6 is
now a computation, closing the only place where the producer relied on an
argument instead of a retained slot. The K10 load series vanishes
identically through tau-grade 5 on the chart (grades 0-3 by order, grade 4
by `M4(ell)=0`, grade 5 by the polar identity), so only `k10[0]` reaches
G10, as claimed.

- Rank two: after `A(N5)=B(N5)=0`, the augmented determinant and row four
  are *again* `(27/2^35)Delta*C` and `(3/2^15)E` — the `k10[0]` load
  cancels from both (verified: the identities hold with `k0` symbolic) —
  so `s=t=0`, contradicting the open.
- Rank one: compat3/compat4 are exactly (4.3) and are `k0`-free (this is
  `W_4 = 0` and `W_3+(1/8)W_1 = 0` in action); `s = eps*8i*t` and `X=0`
  forced; the terminal `G10_2+(eps*i/2)G10_1 = -eps*(5i/16)*k10[0]*t^3`
  (5.3), with no `k10[0]`-free part, nonzero on `k10[0] != 0, t != 0`
  (`t=0` would force `s=0` against the open). Dead.
- Rank zero (`p=q=0`, covering `ord(N)=5,6,...,infinity`): row four
  `= (3/2^19)(B^2-64A^2)` with no load (that is `W_4=0`); on each branch
  `B = delta*8A` the combination is `(3delta/2048)A^2`, so `A=B=0`; then
  **every one of the seven** G10 rows equals `k10[0]*W_r(s,t)` with `W_r`
  the degree-three part of `A10_r(D(S,T))` (I verified all seven, not just
  rows 1,2), and `W_1 = (5/4096)t(3s^2-64t^2)`, `W_2 =
  (5/65536)s(s^2-192t^2)` have common zero only `(s,t)=(0,0)`
  (`3*192=576 != 64`). Dead, including the pure-surface branch.

The transition tree of the producer's section 0 is therefore complete and
each of its nine rows is exact: emptiness (0.2) holds over any
algebraically closed characteristic-zero field. The Gaussian charts use
`i`; the `r^2=192` branch needs no extension (unit ideal in the quotient).

## 7. K10 arrival cancellation and face uniformity (attack 5)

The claimed mechanism is fully verified: `M4_r(ell(s,t)) = 0` for all seven
rows (the tangent identity (1.2)); the polar of `M4` between `ell` and any
`V(A,B)` vector vanishes; hence on every branch that survives to G8 (all of
which have pure-plane `d_2 = ell(s,t)`, since the n=2 branches die at G6
before K10 exists), the global G8 arrival is deleted, and the G9 arrival
dies by the same polar identity. On the n=3 rank-one branch the decisive
row-six load is zero through grade 5 with `k10[0..5]` retained. At G10 only
`k10[0]` survives literal extraction (grade-by-grade: `k_j` multiplies load
grade `6-j`, zero for `j>=1`), and the load enters the kills only through
`W_r`, where it either cancels (rank two, rank one compat, `W_4`,
`W_3+W_1/8`) or is itself the terminal (rank one (5.3), rank zero (5.7)) on
the open `k10[0] != 0`. No K6/K2/target coefficient can reach G10 on any
face because their shifts alone are `tau^12` or later (section 3) — the
uniformity claim holds with margin. `Jdet[0] != 0` is carried in the cell
normalization but unused through G10 (first possible Jdet grade 38);
harmless, since extra opens only shrink the set claimed empty.

## 8. `m=2` strictly exceeds the `tau^2` pullback of `m=1` (attack 6)

Confirmed, and strengthened. Any `tau^2` pullback of an `m=1` datum has
only even tau-coefficients in `d` and the boundary series. The odd G8
survivor of section 6 satisfies `B(N5) - eps*8i*A(N5) = -128tq` with
`t != 0` (from `s = eps*8i*t` plus the open) and `q != 0` (rank one), so
`N5 != 0` is **forced on the entire component**, and `N3 = ray(eps*8iq, q)
!= 0` likewise: every point of the survivor has nonzero tau^3 and tau^5
data. The G8 jet variety of the `m=2` cell therefore strictly contains the
even locus — not merely at the fixture point but on a whole constructible
component per sign — so no coefficient-blind induction or `tau^2`
substitution from the `e=2,m=1` or `e=3,m=1` fans can produce this theorem.
The fixture (4.8) was reconstructed exactly in my engine: all seven rows
vanish through G8, `G9_6 = i/32`, and `-128 -> -127` breaks G8 in rows
1,2,3,5,7 (precisely the rows with nonzero beta). Types kept distinct
throughout: the survivor and fixture are finite G8 prefixes (jets), not
formal arcs (they die at G9), and no attained-source or polynomial-map
claim is made or needed; the producer's section 4/6 wording respects this,
and the `k10=Jdet=1` in the fixture is decoration (Jdet cannot appear
through G10).

## 9. From G10 point-set emptiness to no formal arc in the cell (attack 8)

Sound as stated. A formal solution in the exact normalized cell (0.1) —
`Lambda=tau^2`, `C6=1`, `ord_tau(d)=2` exactly (so `d_2 != 0`, which is the
open `union_i D(d_i[2])`), `k10[0] != 0`, later boundary faces positive or
infinite — would satisfy every graded equation; its coefficients through
the relevant orders give a field-valued point of
`V(G0,...,G10) ∩ D(k10[0]) ∩ {d_2 != 0}`. G0..G3 vanish identically at
`ord(d)=2` (rows start quadratic), and every coefficient capable of
touching G4..G10 is either retained in some chart of the fan or proved
absent by my extended-retention runs (including `N7`, `N8`, `S5`, `T5`,
`k10[1..6]`) — so the truncation really is a point of the analyzed variety,
and the fan kills it. The deduction uses truncation only; no converse
lifting, reachability, algebraization, map, other support, `K10=0`, `C6=0`,
or JC2 statement is used or implied, and the producer's nonclaims list
matches. One scope note: the replay's family takes `k10,k6,k2` as free
series in `tau`, a superset of the `Lambda=tau^2` pullback convention
(which would zero the odd slots); emptiness over the superset implies
emptiness over the subfamily, so whichever convention defines the cell the
theorem stands — but a promoted statement should fix the convention (the
producer's "no exact order is imposed on any late boundary series" leans
the right way).

## 10. Producer replay, controls, and itemized verdict (attacks 7, 9)

`python3 -B` and `python3 -B -O` produce byte-identical output matching the
report's banner block exactly, PASS, ~5.7 s; certificate SHA-256
`486bb644...` matches the pinned expectation; neither file contains bare
`assert` statements, so `-O` disables nothing. The engine-level mutation
controls (custody, surface 16->15, `-128 -> -127`, Delta 64->63, k10-open)
all bind. My independent verdict per attacked item:

| item | verdict |
|---|---|
| custody, seal, prelude/V21/canonical-tails pins | CONFIRMED |
| source reconstruction, census, coordinate map, shifts | CONFIRMED (triple-pinned) |
| honest calendar incl. K10 surface minima, K6/K2/target grades | CONFIRMED; uniformity holds on all faces, exceeding the claim |
| gradient lemma, `D = ell+mu`, recentering exactness | CONFIRMED; plane-in-radical-of-`Q` proved, plane not in radical of `M4` noted |
| reduced cone `V(Q)=V(A,B)`, DQ factorization, rank trichotomy | CONFIRMED with necessity |
| n=2 fan (3.1)-(3.4) | CONFIRMED; `s=-r(t+2)` upgraded to forced |
| n=3 rank two (4.1)-(4.2), `det(C,E)=-Delta^2` | CONFIRMED |
| n=3 rank one survivor, (4.3)-(4.6), G9 kill, K10 row-six zeros | CONFIRMED; (4.6) upgraded to necessity |
| odd fixture (4.8)-(4.9) | CONFIRMED; breaks at G8 rows 1,2,3,5,7 under `-127` |
| n=4 G10 fan, (5.1)-(5.7), all three ranks, `ord(N)>4` | CONFIRMED; all seven rank-zero rows equal `k10[0]W_r` |
| K10 cancellation on every surviving branch; only `k10[0]` at G10 | CONFIRMED |
| retention: `alpha,beta,k10[1..6]` absent; `S4,T4,S5,T5,N7,N8` absent | CONFIRMED computationally (extended beyond producer) |
| `m=2` strictly larger than `tau^2` pullback | CONFIRMED; odd data forced on the whole survivor component |
| emptiness (0.2) and the no-formal-arc corollary in-cell | CONFIRMED |
| replay determinism, certificate, mutation controls | CONFIRMED |

Defects (none affecting soundness):

1. **Erratum.** Section 1 prose says "5,958-byte canonical JSON
   certificate"; the certificate is 6036 bytes (the banner and the pinned
   SHA are correct). Stale figure; fix on next touch.
2. **Weak control.** The `W2 192->191` "mutation" (replay lines 881-886)
   compares two syntactically distinct expected polynomials and can never
   fire; unlike the `-128/-127` and `16/15` controls it does not
   re-exercise the pipeline. Same pattern previously flagged in the e3m1
   review. The in-memory custody control (appending a newline) is likewise
   trivially true. Cosmetic.
3. **Fragility note.** The n=3 G8 rank charts drop `k10` at the call site
   (`kseries=(0,)`), justified by `M4(ell)=0` plus the order census but not
   demonstrated there; my charts retain `k10[0..2]` at G8 and prove
   freeness, so the shortcut is sound on this source.
4. **Scope note.** The `k10(tau)` superset convention of section 9 above
   should be fixed in any promoted statement.

## 11. Maximum exact theorem safe for promotion

Over an algebraically closed field of characteristic zero, on the
normalized generic-ray cell `Lambda=tau^2`, `C6=1`, `ord_tau(d)=2`,
`k10[0] != 0` (with `Jdet[0] != 0` carried but unused), and with
`k10,k6,k2,mu2,mu4,mu6` arbitrary later series (any orders for K6/K2/
targets — positive-face restriction not even needed through G10):

```text
V(G0,...,G10) ∩ D(k10[0]) ∩ {d[2] != 0} = empty,
```

hence no formal solution with these normalizations exists in the cell
(truncation argument only). Additionally promotable: the odd G8-survivor
theorem — for each sign `eps`, the G8-consistent locus at first normal
order three contains a nonempty constructible component on which
`N3 != 0` and `N5 != 0` are forced (nonzero odd columns), and this
component dies at G9 by the raw row-six unit `eps*i*q^3/32`; consequently
the `e=2,m=2` jet space strictly exceeds the `tau^2`-composed `m=1` locus
at G8. No scheme equality, multiplicity, lifting, reachability, map,
other-cell, or JC2 statement is licensed.

## 12. Cheapest next residue

The `k10[0] = 0` face of the same normalized ray (K10 order positive or
infinite). Everything through the n=4 rank-two kill and the rank-one
compat rows carries over verbatim (those steps are `k10[0]`-free), but the
two loaded terminals (5.3) and (5.7) vanish, so the fan survives to G11,
where the same `W_r` cubics reappear multiplied by `k10[1]` (grade
`4+1+6`), plus a fresh `Q(N6)`-type quadratic. The marginal cost is one
more grade on the existing charts — hours, not a new mechanism. Second
residue: the `ord_tau(d)=3` cell of the same ray, which is genuinely open
because every kill above G6 consumed the open `(s,t) != (0,0)`; that cell
needs its own fan seeded at `G6 = Q(d_3)` and is the cheapest place where
this theorem's method could fail to transfer.

<!-- BODY-END -->
