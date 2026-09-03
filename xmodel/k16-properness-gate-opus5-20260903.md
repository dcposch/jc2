# k16 properness gate: hostile audit of Fable's PROMOTION LEMMA 5.1

**Lane:** `k16-properness-gate-opus5-20260903`.  Date 2026-09-03.
Drivers and artifacts: `box/k16propgate-20260903/`.

## Verdict

```text
(1) THE LEMMA  ....................... CONFIRMED (proof correct; three hypotheses
      were left implicit by the producer and are supplied here; the DVR
      hypothesis is stronger than the proof needs -- R local domain suffices).
(2) THE APPLICATION .................. CONFIRMED, with two corrections: the
      producer's stated sufficient condition on p is not sufficient, and its
      loud-failure argument is a detector, not a fail-stop.  All five
      hypotheses were re-established here from the denominator list and by
      direct comparison of exact and modular rows, not from the absence of an
      error marker.  PROVED thereby (characteristic zero, on the ray, through
      the banked reduction chain): t = 3, 4, 5, 6, 7.
      NOT proved: t = 8, 9, 11, and every t >= 12.
(3) REPLAY ........................... all charged numbers reproduced
      independently: t=5 (both roots), t=6, t=7 dim 0; t=2 controls 1 / 0;
      t=4 exact and modular agree (identical dim AND identical GB size).
(4) RECONCILIATION ................... (V0) <=> "dim I_(t,+) = 0" CONFIRMED as
      the same statement.  Opus's tau-criterion is the exact (necessary and
      sufficient) form of (8.1) and is STRICTLY WEAKER than (V0); the strictness
      is witnessed here, not cited.
SIDE FINDING (new) ................... the producer's MEASURED lead-ideal
      pattern q_(j,0)^(t+7-j) is REFUTED at t=7 (measured 13 and 9, predicted
      12 and 8).  It was typed MEASURED, so nothing is retracted, but the
      "finite evidence" for the uniform target of the producer's section 8 is
      weaker than stated.
```

No exit-price assertion is made in this report, so no `charge_basis` line is
due.  `FALLACY-v2` applies throughout.  No ledger, `jc2-lean`, `ideation-*`
file or in-progress lane report was read or written.

## 0. Custody

The manifest was generated mechanically from
`xmodel/k16-properness-gate-opus5-20260903.run.v2` with `awk` on the paired
`charged_input_<i>_sha256` / `_basename` lines and checked with `sha256sum -c`:
**15/15 OK**, no digit retyped.  `laurent_spine.py` is not charged but is
required by the task; the copy taken from `box/k16terminal-fable5-20260903/`
matches that lane's own `SHA256SUMS.final`, and that box's `analyze_rows.py`
matches the frozen charged copy.  New files are confined to
`box/k16propgate-20260903/` and this report.

Notation as charged: `q=2t+1`, `e=3t+1`, `H_t=12q^2y^2-12q(t+1)y+(t+1)(3t+2)`,
`A_t=Q[y]/(H_t)`, `g=et y/q^2 - et(t+1)/(6q^3)`, `c=-yg`,
`I_(t,+)=<T_(t,1),...,T_(t,2t-1)>`, weights `wt(b3)=t+1`, `wt(b4)=1`,
`wt(q_(j,0))=j`.

## 1. The lemma

### 1.1 The properness input, with its hypotheses

> **Fact P (standard).** Let `R` be a ring and `S` a graded ring with `S_0=R`
> which is generated as an `R`-algebra by finitely many homogeneous elements of
> **positive** degree.  Then `Proj S -> Spec R` is proper.

(EGA II 5.5.3; equivalently, for `d` the lcm of the generator degrees the `d`-th
Veronese `S^(d)` is generated in degree `d`, `Proj S = Proj S^(d)` is a closed
subscheme of a projective space over `R`, and closed immersions and projective
morphisms are proper.)  Two hypotheses of Fact P matter and were **not stated**
by the producer (a third, base change for `Proj`, is used in 1.3):

* *finite generation* -- satisfied: `S = R[x_1..x_n]/J` with `n = t` variables
  `(b3,b4,q_(2,0),...,q_(t-1,0))`;
* *positive degrees, and `S_0 = R` exactly* -- satisfied **because every
  generator of `J` is homogeneous of positive weight**: `T_(t,k)` has weight
  `4t+1-k >= 2t+2 > 0` for `1<=k<=2t-1`.  This is exactly why band zero must be
  excluded, and the exclusion is forced twice over: `T_(t,0)` is inhomogeneous,
  so `R[x]/<T_(t,0),...>` is not a graded ring and `Proj` is not defined at all;
  and its weight-`0` part is the **unit** `-c = yg`, so any graded ideal
  containing it would have `S_0 = 0` and empty `Proj` over *every* fibre,
  making the promotion vacuous.  TYPED: hypothesis check, CONFIRMED.

### 1.2 "Cone = {0}" is the right condition

For a graded ring `S̄ = kappa[x]/J̄` with `deg x_i = a_i > 0` the irrelevant
ideal is `S̄_+ = (x_1,...,x_n)`, and

```text
Proj S̄ = empty  <=>  S̄_+ subset nil(S̄)  <=>  x_i^(N_i) in J̄ for all i
                <=>  V(J̄) = {0} in A^n over kappabar   (Nullstellensatz;
                     "{0}" and not "empty" because J̄ is homogeneous of
                     positive weights, so 0 in V(J̄) always).
```

The middle condition is field-independent and is precisely what a Groebner
computation exhibits: **a pure power of every variable in `lead(J̄)`**.  This
audit reads the certificates that way as well as through Singular's `dim`
(section 3), so the conclusion does not rest on the meaning of `dim` in a `wp`
ring.  TYPED: CONFIRMED.

### 1.3 The proof

**Lemma (promotion).** Let `R` be a local domain with fraction field `K` and
residue field `kappa`, and let `J subset R[x_1..x_n]` be an ideal generated by
polynomials homogeneous for positive integer weights `a_1..a_n`.  If
`V(J.kappa[x]) = {0}` over `kappabar`, then `V(J.K[x]) = {0}` over `Kbar`.

*Proof.*  Put `S = R[x]/J`, graded by the `a_i`; `S_0 = R` and `S` is generated
by `x_1..x_n` in positive degrees, so `X := Proj S -> Spec R` is proper by Fact
P.  Proj commutes with base change on the base, so the fibre over the closed
point is `Proj(S ⊗_R kappa) = Proj(kappa[x]/J.kappa[x])`, empty by 1.2 and the
hypothesis.  Properness makes the image of `X` in `Spec R` closed, and it misses
the closed point `m`; but a closed subset `V(I)` of `Spec R` with
`m not-in V(I)` has `I not-subset m`, hence `I = R` because `R` is local, hence
`V(I) = empty`.  So `X = empty`, in particular the generic fibre
`X_K = Proj(K[x]/J.K[x])` is empty, and by 1.2 over `K` (again using positive
weights) `V(J.K[x]) = {0}` over `Kbar`. `[]`

### 1.4 What the proof uses, and does not

* **No flatness.**  Fact P holds for any graded finite-type `R`-algebra; the
  special fibre is used only through its emptiness.  CONFIRMED (the producer's
  claim on this point is right).
* **The DVR hypothesis is not needed.**  Only two properties of `R` are used:
  local (for "closed subset missing `m` is empty") and a domain (so that a
  generic fibre exists with `K = Frac R`).  This matters for the application:
  the localisation of `Z[y]/(H_t)` at `P=(p,y-r)` is a one-dimensional local
  domain, but it is a DVR only if `P` is a regular point, which would need
  `p` prime to the conductor/discriminant.  **Weakening `DVR` to `local
  domain` removes that check entirely.**  TYPED: PROVED-HERE (strengthening).
* **One direction only.**  Contrapositive: generic fibre nonempty ⇒ special
  fibre nonempty.  So a modular `dim > 0` proves nothing.  CONFIRMED.
* **Homogeneity is where the naive modular argument dies.**  For the
  inhomogeneous unit test `<T_(t,0),...,T_(t,2t-1)> = [1]` the sound direction is
  the reverse one (char-0 unit ⇒ modular unit for almost all `p`); a modular unit
  ideal lifts to nothing.  CONFIRMED.

**Verdict (1): the lemma is CONFIRMED.**  No gap; three implicit hypotheses
supplied (finite generation, positive degrees / `S_0 = R`, base change for
Proj); one hypothesis (DVR) shown to be stronger than necessary.

## 2. The application: hypotheses audited

Write `R` for the localisation of `Z[y]/(H_t)` at `P=(p,y-r)` (non-split `t`),
or `Z_(p)` (split `t`, one rational fibre at a time), `kappa = GF(p)`,
`K = A_t` resp. `Q`, and `J := <T_(t,1),...,T_(t,2t-1)> . R[x]`.  Then
`J.K[x] = I_(t,+)` by construction, and the whole question is whether the
*computed* modular ideal is `J.kappa[x]`.

### 2.1 (H-int) p-integrality, from the denominator list

The producer's argument is that Singular "fails loudly" on a `p`-divisible
denominator and that no marker occurs.  I did it the way the task asks --
from the list -- by reading every division in `laurent_spine.py`:

```text
(D-a) binom():        i, 1<=i<=4t+1
(D-b) integrate_s():  i, 1<=i<=4t+2
(D-c) euler_inverse():yy*(2i-1), so yy and odd integers <= 8t+3
(D-d,e) Bp and Xp:    2*yy
(D-f) rhsD:           2  (the 5/2)
(D-g) g1,g2,g:        q, 2q^2, 6q^3
(D-h) affine_solve(): the 2t+1 high pivots p_C(t,j), p_Q(t,j), p_b2,
                      plus b1coef = y*g and B0coef = q/y.
```

`pintegral_check.py` reduces every one of these at `P`, taking the **exact**
pivot values from the `PIVOT` lines of the charged exact row files.  Result
(`pint_summary.txt`, `pint_t2.txt`):

```text
PINT PASS for (t,p,y) = (5,32009,1821), (5,32009,15639), (6,32003,27617),
                        (7,32059,4425), (4,32029,25378), (4,32029,31563),
                        (2,32003,1/5),  (2,32003,2/5).
```

In each: every fixed integer denominator is a unit because `p > 8t+3`;
`H_t(y) = 0`; `y != 0`; `q, 2q^2, 6q^3, 2` are units; and all `2t+1` exact high
pivots plus `y*g` and `q/y` are nonzero mod `P` (every value printed in the
artifact).  TYPED: **CONFIRMED, established from the list.**

*Correction to the producer.*  Fable states the condition as "a prime `p` not
dividing `12q^2` with a root `r` of `H_t` modulo `p`".  That is necessary but
**not sufficient**: it does not give `p` prime to `6q^3` (the `g` denominator),
nor `r != 0 mod p`, nor -- decisively -- the nonvanishing of the `2t+1` pivots,
which is not implied by any condition on `p` alone.  The producer's operational
procedure ("checked per run") does cover this; the *stated* sufficient condition
does not.  TYPED: statement corrected, application unaffected.

### 2.2 (H-loud) the div-by-0 argument is a detector, not a fail-stop

I re-ran the producer's premise myself (`divzero_probe{,2,3}.sing`).  In
`GF(32003)`, `number a = number(7)/32003;` prints `? div. by 0` **on stdout** --
and then the next statement still executes and the process **exits 0**.  So the
marker is emitted (the grep is sound as a *detector*) but there is no fail-stop:
`SPINE_OK` and `exit=0` are not evidence of a clean run, and the grep is
load-bearing rather than a convenience.  The `affine_solve` guard fires
correctly on a zero pivot (`cf == 0 -> ERROR`), but a top-level Singular `ERROR`
likewise does not terminate the script.  I therefore scanned every run this
audit relies on for `div. by 0` / `div by 0` / `error occurred`: the **only**
files carrying a marker are my two deliberate probes.  TYPED: premise CONFIRMED
as stated (loud), its sufficiency **corrected** (not fail-stop).

### 2.3 (H-gen) the modular ideal is generated by the reductions of the SAME generators

This is the hypothesis the task asks to "resolve exactly", and it has a clean
answer.

> If `J = (f_1,...,f_m).R[x]`, then `J.kappa[x] = (f̄_1,...,f̄_m).kappa[x]`.

*Proof.* `R[x]^m -> J -> 0` is exact; tensoring with `kappa` is right exact, and
the image of `J ⊗ kappa -> kappa[x]` is by definition `J.kappa[x]`. `[]`
So reduction of **any generating set of `J` as an ideal of `R[x]`** is legitimate
-- no Groebner subtlety, and no "reduction of a Groebner basis" is involved.

The trap is a generating set of `J.K[x]` that is **not** one of `J`.  Take
`R = Z_(p)`, `J = (p x, y)`, `wt x = wt y = 1`.  A Groebner basis of
`J.K[x] = (x,y)` scaled into `R[x]` is `{x,y}`, generating `J' strictly-contains
J`; then `V(J'.kappa) = {0}` while `V(J.kappa) = V(y)` is a line.  Reducing a
`K`-Groebner basis can therefore produce a strictly **larger** modular ideal and
a **false** emptiness.  The safe inclusion is the other one: if the computed
`I_kappa subset J.kappa[x]` -- a *possibly larger* cone -- then
`V(I_kappa) = {0} => V(J.kappa[x]) = {0}`, since `V` reverses inclusions and the
cone contains `0`.  So "larger cone is still safe" is correct; the real risk is
the smaller one.

Which case are the runs in?  `analyze_rows.py` (charged) and my `jplus_hom.py`
build the ideal directly from the row generators `T_1..T_(2t-1)` in the rows
file, and the modular rows are produced by re-running the recurrence in `GF(p)`
-- so the identification "modular generators = reductions of exact generators"
is a claim about the recurrence, not about Singular.  I tested it directly:
`exact_vs_modular.py` reduces the **exact** number-field rows at `y -> r` in
`GF(p)` and subtracts the rows produced by `laurent_spine.py --modp`:

```text
ROWMATCH  t=2 (p=32003, y=1/5)      4/4  OK, 0 mismatches
ROWMATCH  t=4 (p=32029, r=25378)    8/8  OK      t=4 (r=31563)   8/8  OK
ROWMATCH  t=5 (p=32009, r=1821)    10/10 OK      t=5 (r=15639)  10/10 OK
ROWMATCH  t=6 (p=32003, r=27617)   12/12 OK
ROWMATCH  t=7 (p=32059, r=4425)    14/14 OK
```

TYPED: **CONFIRMED by direct computation**, not by an argument.

There is also a *self-certifying* form of the argument that does not need the
exact rows (relevant at `t=11` and beyond).  By induction on the spine steps:
if steps `1..j-1` commuted with reduction, the pivot coefficient printed by the
modular run at step `j` is the reduction of the exact pivot; the run's own
`affine_solve` guard asserts it is nonzero; a nonzero element of `kappa` is a
unit, so the exact pivot is a `P`-unit and step `j` commutes.  With the fixed
integer denominators handled by `p > 8t+3` (2.1), a modular run that prints all
`2t+1` pivots nonzero and carries no error marker **proves** its own rows are the
reductions of the exact rows.  TYPED: PROVED-HERE.

### 2.4 (H-hom) weighted homogeneity of `T_(t,k)`, `k >= 1`, and its failure at `k = 0`

Symbolically this is the charged second grading: in the `w`-picture the `w^j`
coefficient has weight `j` under `wt(h)=1, wt(pi)=-t, wt(y)=wt(g)=0`, giving
`wt(b4)=1, wt(q_(j,0))=j, wt(b3)=t+1`; the recurrences (D3),(D2),(D1),(D0) are
weight-homogeneous and `T_(t,k) = -[w^(4t+1-k)]sigma_t(Delta) + yg[k=0]`, whence
weight `4t+1-k` for `k>=1` and a single inhomogeneous term at `k=0`.  I verified
the conclusion mechanically with `homog()` in the declared `wp` ring on every
row of every run:

```text
t=2 (both fibres, exact and mod p), t=3 exact, t=4 exact and mod 32029 (2 roots),
t=5 mod 32009 (2 roots), t=6 mod 32003, t=7 mod 32059:
  for every k in 1..2t-1:  homog(T_k) = 1  and  deg(T_k) = 4t+1-k   EXACTLY;
  in every run: T0_homog = 0 (INHOMOGENEOUS), T0HOM_homog = 1 with deg = 4t+1,
                T0CONST != 0, JPLUS_HOMOG_IDEAL = 1.
```

The constant is `+y*g` in every run, checked against the independently computed
`b1coef = y*g` of 2.1 (`1249` at `t=5,r=1821`; `3531` at `t=7`; exactly
`650/2187*y - 910/19683` at `t=4`).  Since `c = -yg`, the rows as produced by
`laurent_spine.py` satisfy `T_(t,0) = -c + tau_t` (Fable's `-E_t` convention).
Opus's report writes `T_(t,0) = c + tau_t` and reports the weight-`0` part as
`28/625-7y/25 = -yg` at `t=2`: the opposite overall sign for the family, from
the charged `terminal_laurent_t*.json` records rather than from these rows.  The
two conventions differ by an overall `-1` and are each internally consistent;
**both arguments need only that the constant is a unit of `A_t`**, and
`N(yg) != 0` for every `t >= 1`.  TYPED: (H-hom) CONFIRMED; the sign convention
is a labelling difference, not a discrepancy.

### 2.5 (H-split) the split-`t` fibres

`H_t` splits over `Q` exactly when `t = 3s^2-1`; in `2<=t<=11` that is `t=2`
(`y=1/5, 2/5`) and `t=11` (`y=7/23, 5/23`).  Then `A_t = Q x Q` is not a domain
and the lemma cannot be applied to it; the correct move -- which both producers
make -- is to work on each rational fibre with `R = Z_(p)`, `K = Q`,
`kappa = GF(p)`.  Checked here:

* `t=2`, `p=32003`: `2,3,q=5,6q^3,5` are units; `y=1/5 -> 19202`, `2/5 -> 6401`,
  both nonzero; all 5 exact pivots nonzero mod `p`.  `PINT PASS`.  (`t=2` needs
  no promotion -- it is exact in char 0.)
* `t=11`, `p=32003`: here `q = 23` **and** the fibre denominator is `23`;
  `32003 mod 23 = 10 != 0`, so `23`, `6q^3 = 73002 -> 8996`, `2`, `3` are units
  and `p > 8t+3 = 91`.  `H_11(7/23) = H_11(5/23) = 0 mod P`; `y -> 27829` resp.
  `15306` and `y*g -> 16082` resp. `16036`, all nonzero; all `23` pivots of each
  charged modular run are nonzero in `GF(32003)`.  By the self-certifying
  induction of 2.3 the `t=11` modular rows **are** the reductions of the exact
  rows on each fibre.  TYPED: (H-int),(H-gen) CONFIRMED at `t=11`.
  **This buys nothing**: no `t=11` cone test finished (`JPLUS` and `RESZ` on
  both fibres are `INCONCLUSIVE_TIMEOUT`), so there is no certificate to
  promote.  TYPED: `t=11` remains OPEN.

## 3. Replay

Every Singular job ran under `timeout`, in four parallel streams, on a host at
load average ~45; the batch was blocked on to completion inside this turn and
nothing was left running.  `jplus_hom.py` reproduces the ring, weights, minpoly,
variable order and generator list of the charged `analyze_rows.py` verbatim and
adds the homogeneity assertions of 2.4.

| `t` | fibre / prime | `JPLUS dim` | GB size | time (s) | pure powers in `lead` | typing |
|---:|---|---:|---:|---:|---|---|
| 2 | `y=1/5` exact | **1** | 3 | <1 | `b4^7` only, **no `b3` power** | negative control, matches |
| 2 | `y=1/5` mod 32003 | **1** | 3 | <1 | `b4^7` only | negative control, matches |
| 2 | `y=2/5` exact | **0** | 3 | <1 | `b3^2, b4^8` | matches |
| 3 | `Q(sqrt3)` exact | **0** | 15 | <1 | `b3^2, b4^10, q2^8` | matches |
| 4 | `Q(sqrt15)` exact | **0** | 66 | 21 | `b3^2, b4^12, q2^9, q3^8` | matches |
| 4 | mod 32029, `r=25378` | **0** | 66 | <1 | identical to exact | **agreement control** |
| 4 | mod 32029, `r=31563` | **0** | 66 | <1 | identical to exact | **agreement control** |
| 5 | mod 32009, `r=1821` | **0** | 285 | <1 | `b3^2,b4^14,q2^10,q3^9,q4^8` | certificate |
| 5 | mod 32009, `r=15639` | **0** | 285 | <1 | identical | certificate |
| 6 | mod 32003, `r=27617` | **0** | 1224 | 12 | `b3^2,b4^16,q2^11,q3^10,q4^9,q5^8` | certificate |
| 7 | mod 32059, `r=4425` | **0** | 5304 | 1152 | `b3^2,b4^18,q2^13,q3^11,q4^10,q5^9,q6^9` | certificate |

Every certificate line carries a pure power of **every** variable in `lead(G)`,
so the special fibre's `Proj` is empty by the ideal-theoretic criterion of 1.2,
independently of Singular's `dim` in a `wp` ring; at `t=2, y=1/5` `b3` has **no**
pure power, in exact and modular arithmetic alike -- the lemma's contrapositive
behaving correctly.  The `t=4` exact/modular agreement (same dim, same GB size
66, same lead ideal, rows matching term by term) is the positive control for the
whole promotion.  The charged `analyze_rows.py` battery at `t=2` reproduces the
banked table exactly: `y=1/5` -- `dim 1`, `T0HOM power 1`, `RESZ dim 1`,
`TOPT b4^7`, both charts `UNIT`; `y=2/5` -- `dim 0`, `T0HOM power 1`,
`RESZ dim 0`, `TOPT b4^10`, both charts `UNIT`.

**Scope of the promotion.**  With (H-int),(H-gen),(H-hom),(H-loud) confirmed and
the lemma of 1.3, each `dim = 0` line above is a characteristic-zero proof that
`V(I_(t,+)) = {0}` over `Abar_t`, hence of (8.1), hence -- through the banked,
uniformly proved reduction chain -- of (T) at that `t`.  For non-split `t` one
root suffices (the two roots are the two embeddings of the quadratic field
`A_t`; `V(J.K[x]) = {0}` is a statement about `K = A_t` and is
embedding-independent); both roots were run at `t=4,5` as redundancy.
**PROVED: `t = 3, 4, 5, 6, 7`** (`t=2` is exact and needs no promotion; it
satisfies (8.1) on both fibres but (V0) only on `y=2/5`).
**NOT PROVED: `t = 8, 9, 11` (INCONCLUSIVE_TIMEOUT) and every `t >= 12`.**

## 4. Reconciliation with Lemma CONE

* **(V0) `<=>` `dim I_(t,+) = 0`.**  `I_(t,+)` is generated by weighted
  homogeneous polynomials of positive weight, so `Z_+ = V(I_(t,+))` is stable
  under the `G_m`-action and contains `0`; a `G_m`-stable set is finite iff it
  is `{0}`, and `dim` of the affine quotient is `0` iff `Z_+` is finite.  This
  is Opus's (1.1) and Fable's (V0) verbatim.  TYPED: **the two lemmas state the
  same condition**; CONFIRMED.
* **Opus's tau-criterion is the exact statement, and is strictly weaker.**
  Lemma CONE gives `(8.1) <=> tau_t in sqrt(I_(t,+))` (necessary and
  sufficient) with Corollary C1 `dim I_(t,+) = 0 => (8.1)` (sufficient only).
  The strictness is witnessed at `t=2, y=1/5` and was verified here rather than
  cited: `JPLUS dim = 1` (so (V0) FAILS) while `T0HOM_IN_RADICAL power=1` and
  both charts are `UNIT` (so (8.1) HOLDS).  TYPED: CONFIRMED.
* Consequently the promotion lemma proves the **stronger** statement (V0) and
  gets (8.1) as a corollary.  A future `t` with `dim I_(t,+) > 0` would not
  refute (8.1); it would put that `t` outside the reach of this instrument, and
  the fallback would be the radical membership `tau_t in sqrt(I_(t,+))`.  That
  fallback is **not** promotable by the lemma of 1.3, and not for a soft reason:
  radical membership modulo `P` does not lift.  Take `R = Z_(p)`, `n = 2`,
  `wt x = wt y = 1`, `J = (x - p y)`, `tau = x`.  Then `x` vanishes on
  `V(J.kappa[x]) = {x=0}`, so `tau in sqrt(J.kappa[x])`; but on
  `V(J.K[x]) = {x = p y}` one has `x = p != 0`, so `tau not-in sqrt(J.K[x])`.
  The lemma promotes emptiness of a proper special fibre, and the locus
  `V(I_(t,+)) cap D(tau_t)` whose emptiness is at issue is **open**, not
  proper.  TYPED: OPEN, flagged.

## 5. Side finding: the lead-ideal pattern is refuted at `t=7`

The producer records, typed MEASURED, that `lead I_(t,+)` contains `b3^2`,
`b3 b4^(t+2)`, `b4^(2t+4)` and `q_(j,0)^(t+7-j)`, offering the last as the finite
evidence for the uniform target of its section 8.  Measured here: at `t=2..6`
predicted = measured; at `t=7` `b4^18 = b4^(2t+4)` still holds, but the exponents
are `q_2^13` (predicted 12) and `q_6^9` (predicted 8) -- **pattern refuted at
`t=7`**.  Nothing is retracted (it was typed MEASURED, never promoted), but the
stated evidence for a `q_(t-1,0)`-pure-power uniform statement is weaker than the
report suggests.  TYPED: MEASURED, refuting the extrapolation.

## 6. Reproduction

```text
cd box/k16propgate-20260903
python3 pintegral_check.py 7 32059 4425 ../k16terminal-fable5-20260903/t7_rows.txt out.txt
./run_batch.sh                                 # spines, row agreement, JPLUS
Singular -q divzero_probe.sing < /dev/null     # the loud-but-not-fatal probe
```

Artifacts: `pint_summary.txt`, `pint_t2.txt`; `ev_t{2,4,5,6,7}*.out` (row
agreement); `an_t*.out` (homogeneity + JPLUS); `ar_t2f*.out` (charged battery at
`t=2`); `s{1..4}.log`, `batch.log`, `divzero_probe*.out`.

## 7. FALLACY-v2 audit of this report

* *Variable/ring map.*  Every test declares ring, coefficient field, generator
  order `(b3,b4,q_2,...,q_(t-1))` and weights `wp(t+1,1,2,...,t-1)`; the ring
  construction is copied from the charged `analyze_rows.py` and the weights
  actually used are printed (`WEIGHTS=wp,...`) in every run.
* *`sat()` wrapping.*  Not used; radical membership is by explicit powers.
* *Floor vs attainment.*  `dim = 0` is not read as a bound: it is cross-checked
  by the ideal-theoretic criterion (pure power of every variable in `lead`),
  which *is* the definition of the special fibre being empty.
* *Carrier/attainment.*  The promotion is one-directional and is used only in
  that direction; `dim > 0` modulo `p` is never read as evidence.
* No fixed-size certificate is interpolated from finite `t`; section 5 is an
  explicit warning against exactly that.
* No exit-price assertion is made, so no `charge_basis` line is declared.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `23475`.
- Body SHA-256:
  `512cf3a15ff8d1f5470f08fe452eaca1165c9715af97b70b6d370ed172e4bfd1`.
- Frozen basis: `fbcee92f64c15875a96192fe2291d610c31fd6e5`.
