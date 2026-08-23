# DEPTH-STAB: depth stabilization for the residue-A window system

Status: **BANKED 2026-08-17 (first-lemma tier, both routes; ROUTE B
COMMITTED for the decision statement).** Sources:
`xmodel/grok-lateral2.md` ideas 4 (window-ideal ascending chain) and
5 (Greenberg function); tower structure `SHEET6-DIRECTIONB.md`
§§6–8 (esp. 8.S, the D23-core). Machine gate:
`cases/depthstab_check.py` (14 checks, exit 0). Exact arithmetic
only. No git commit. Consistency with the running data is BUILT IN
(§4): any stabilization at `D* <= 21` is refuted by the banked
12/12 sample deaths, so every statement here carries `D* >= 23`.

## 1. Setup

`A` = the CORE2 coordinate ring localized at the pole scales
(`k[CORE2][1/W1W2]`, 27-variable unsplit / 22-variable fiber chart)
— a finitely generated `k`-algebra, hence **Noetherian**. For each
odd depth `D >= 21`, `V_D` = the residue-A window at depth `D`
(B-frozen, no-log, `W != 0`: algebraic conditions of bounded
degree), `pi_A : V_D -> Spec A` the projection killing the depth-D
tails, `J_D = ker(A -> k[V_D])` the elimination (image) ideal.

**Truncation-compatibility (machine fact, not hypothesis).** The
depth-23 system CONTAINS the depth-21 system on the common
variables: the D23-core's first 38 post-header rows are
byte-identical to the banked D21 CORE2 rows at all three primes
(gate DS1, live re-verification; the build-tier row-for-row
regression is SHEET6-DIRECTIONB §8's 17/18 gate). New depths add
rows (22 pivots + 10 Row_22 at D23), never remove them.

## 2. Theorem DS (depth decision, residue-A window tier)

**(1) Chain (route A, proved at this tier).** Truncation-
compatibility gives `pi_A(V_23) ⊆ pi_A(V_21)`, hence
`J_21 ⊆ J_23 ⊆ J_25 ⊆ ...` — an ascending chain in the Noetherian
ring `A`. It stabilizes at some finite `D*`; equivalently the
closed images `X_D = closure(pi_A(V_D))` descend and stabilize.
Mod `p` the windows are finite sets, so a descending chain of
nonempty images has nonempty inverse limit (König): **all depths
nonempty ⟺ a mod-p formal germ exists.** The mechanism is
exact-verified on a toy tower (gate DS2: `J_1 = (0) ⊊ J_2 ∋ b⁴−a³`).

**(2) Kill direction (depth-free; what the running lanes consume).**
A formal germ truncates to a point of every `V_D`; contrapositive:
`V_D = ∅` at ANY single depth kills the germ (mod-p screening
tier). **The pre-registered "D23 EMPTY at 2+ primes ⇒ residue-A
dead at the window tier" needs no stabilization theorem — only
DS1's compatibility.** (Gate DS3.)

**(3) Live direction (route B, COMMITTED; the effective decision
constant).** Tougeron's implicit function theorem (Greenberg's
effective form for our data): *a depth-`D` point `s` whose Jacobian
minor has t-adic valuation `e(s) <= (D−1)/2` lifts to a true formal
germ agreeing with `s` to depth `D − e(s)`.* Decision constant:
`D*_eff = 2e* + 1`, `e*` = the minimal minor-valuation over the
depth-`D` locus. So if a depth-`D` lane returns NONEMPTY and a
found point has `e <= (D−1)/2`, the LIVE verdict is **final** — the
formal germ exists and the iteration stops. Newton mechanism
demonstrated exactly mod 105337 (gate DS4a/b: `e = 1` point lifted
from depth `3 = 2e+1` to depth 24); the hypothesis is load-bearing
(DS4c: `x² = t³` is solvable mod `t³` with `e = ∞` and truly
unsolvable — no lift is claimed there).

**(4) Combined decision rule.** At the current depth `D`:
`EMPTY (2+ primes)` ⇒ dead, final, by (2). `NONEMPTY` ⇒ compute
`e` on the found points (recipe §3): if `e <= (D−1)/2` ⇒ LIVE,
final, by (3) — at `D = 23` this means **any found point with
`e <= 11` already decides the formal germ question**; else iterate
to `D = 2e + 1` with the stopping rule now e-tracked, not
open-ended. Either way **the depth-`D*` window verdict decides the
formal germ question** with `D* = max(23, 2e* + 1)` on the live
branch and `D* =` the first empty depth on the dead branch.

## 3. The e-recipe (banked, gate DS6)

For a found depth-`D` point `s` of the window system `F_1..F_m`
(87 vars / 77 eqs at D23): `e(s) = min` over maximal minors `M` of
`Jac(F)(s)` of the t-adic valuation of `M`. Cheap per point (rank
computations over `F_p[t]/t^D`). Controls: a unit minor gives
`e = 0`, `D* = 1` (`γ ≡ id` — the ctl0/origin window must behave
this way or the elimination is buggy; DS6b); `e = ∞` (all minors
vanish to depth) means the hypothesis fails and NO verdict is
claimed — fall back to iteration (fail-closed).

## 4. Consistency with the data (the refutation check, gate DS5)

Banked record (SHEET6-DIRECTIONB 8.S, FILTER-REPLAY CLOSURE): the
12 dead D21 sample points are 12/12 INCONSISTENT against the
emitted D23-core. So `im(V_23 → V_21)` omits all 12 samples: the
image **moved** at the 21→23 step. A stabilization at `D* <= 21`
would assert the image already stable at 21 — **refuted**. Every
statement above therefore carries `D* >= 23`; the D21-nonempty /
D23-sample-kill data is consistent with Theorem DS and would have
refuted the naive form. (Machine halves: DS5a/b the implication,
DS5c the 77-row D23-core genuinely extends the 38-row prefix.)

## 5. Route comparison and the commit

Route A gives the chain + abstract `D*` + the kill direction, and
its chain hypothesis is already machine-grounded (DS1) — but its
`D*` is NOT effective from Noetherianity alone: elimination-degree
growth is the named obstruction (**DS-OB1**; no doubly-exponential
generic bound is claimed as useful). Route B gives the explicit
constant `D*_eff = 2e + 1` with `e` a computable valuation on the
actual locus — the constant the lanes can consume TODAY.
**Committed: route B for the decision statement; route A banked as
the structural half.** Idea 4's elimination `J_23` onto CORE2
(three exact outcomes: `(1)` = variety-tier kill upgrading 0/12;
`(0)` = wrong ambient, record honestly; proper = first chain step)
remains the pre-registered NEXT computation if the D23 lanes return
NONEMPTY without a small-`e` point; idea 5's empirical Greenberg
numbers `dim im(V_{n+2} → V_n)` at `n = 21, 23` are the lane
observables for it.

## 6. Reproduction

```bash
python3 cases/depthstab_check.py    # 14 checks, exit 0
```

DS1 truncation-compatibility (38-row byte-identity, 3 primes); DS2
exact toy chain ascent; DS3 kill direction; DS4a–c Tougeron/Newton
demo + failure control; DS5a–c data consistency (`D* >= 23`
forced); DS6a–b e-recipe + ctl0 control; DS7 DS-OB1 record. No git
commit.
