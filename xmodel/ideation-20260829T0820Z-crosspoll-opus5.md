# Cross-pollination adversarial review — Opus 5 — round `20260829T0820Z`

Lane: Opus 5 (exact `claude-opus-5`), equal-standing adversarial researcher.
Post-blind cross-pollination pass. Written `2026-08-29` against the sealed
packet, the four blind lane reports, and pre-cutoff canonical/`xmodel`
artifacts only.

## 0. Custody, method, and disclosures

**All five charged files verified byte-exact this session.**

```text
65afb334763023765f701ee9a2140087a47c6ae470877cee0a04b4f4651c0d8f  xmodel/ideation-20260829T0820Z-state-packet.md   MATCHES
cc58a521b92955b8c1e423aacdf60a5b619ba5384c9e05781bafec1ed7647b8c  xmodel/ideation-20260829T0820Z-fable5.md          MATCHES
142d1e3dcd1305dda7397b5cd8f812080c2bf6d6eeb7106203fce9912777e451  xmodel/ideation-20260829T0820Z-opus5.md           MATCHES
ec454b2e958690f396bbd14e901afcb1b5faf9204907911d27b8ab1c972cd98a  xmodel/ideation-20260829T0820Z-grok46.md          MATCHES
ad50d1ada197a3ad424f321707ea62105fafc74a650d8b55e34cc1130c2efa84  xmodel/ideation-20260829T0820Z-sol56.md           MATCHES
```

All seven canonical roots also recomputed and matching the packet
(`COORDINATION.md fc9c69cb`, `APPROACHES.md 27a208c5`, `AUDIT.md 7cb5d4a8`,
`PROGRESS.md 3a6298d3`, `notes.md f34ad60d`, `ladder/REDUCTION.md b0b6c276`,
`0250Z` synthesis `d2e34570`).

**Pre-cutoff read boundary, enforced mechanically.** Independent
reconstruction required the reviewed bodies themselves, not the packet's
summaries of them. To guarantee no post-cutoff leakage I read every
supporting report through `git show eaad172e:<path>` — the basis commit named
in the packet — so every byte I consumed predates the cutoff by construction.
Files read this way, each hash-checked where the packet or a review header
pins a value:

```text
3c2c9a7e…  m2-td8-trunk-exact-charge-r1-sol56-20260829.md              (td8 producer, packet-pinned)
           m2-td8-trunk-exact-charge-r1-hostile-review-opus5-20260829.md (my td8 review, body 51f3ed7c)
2a151eef…  m2-td12-u1-next-trunk-discriminator-r1-sol56-20260829.md    (td12 producer, review-pinned)
           m2-td12-u1-next-trunk-discriminator-r1-hostile-review-fable5-20260829.md
           m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md
           m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
99bbe233…  m2-u2-nested-nu1-boundary-r1-sol56-20260829.md              (U2 producer, packet-pinned)
           m2-u2-first-p2-boundary-finiteness-r1-sol56-20260829.md
           m2-u2-nu1-unbounded-lex-primary-hostile-review-fable5-20260829.md  (absorbed U2 ODE, e156f94c)
```

**Disclosure 1 — post-cutoff artifact deliberately not opened.** My
auto-loaded memory index contains a pointer to a Fable review of the U2
nested `nu=1` boundary that postdates the cutoff. I did not open it and I
use none of its content. Charge 3 below is settled entirely from pre-cutoff
artifacts I re-derived myself. I record this so the coordinator does not read
my charge-3 verdict as either ignorant of, or contaminated by, that review.

**Disclosure 2 — self-attack is the main product.** The two objects I
attack hardest are my own: the closed-form `Lambda` and the
`PLACE-CONSERVATION` alarm. Both fail. Charge 5's week-waster is also mine.

**Disclosure 3 — boundary.** `jc2-lean` was never entered, enumerated,
searched, read, built, statused, modified, or controlled; every `git`
invocation was scoped to `-- xmodel` or to an explicit non-`jc2-lean` path,
and no root tree was listed. No canonical edit, commit, push, web access,
AWS action, or heavy computation. Execution was `shasum`, `git show`, `grep`,
`sed`, and two short exact-`Fraction` scripts reproduced verbatim below.
This report is the only file written.

**Standing typing firewall, used throughout.** Physical **flag** (a vertex of
`T_{a,cv}`), **place** (a point of `Ra_bar \ Ra`, one ray each), **orbit** (a
`mu_nu`-conjugacy block counting as one direction), and **conjugate Puiseux
series** (counted by `deg p`) are four different things. `Alive != existent`;
formal cell `!=` germ `!=` polynomial. `G2-PSC` and `G2-BD` are named in full.
Nothing here proves or disproves JC2.

---

## 1. Charge 1 — the maximum safe statement behind `Lambda`

### 1.1 What the two reviewed proofs actually pin

Independent reconstruction from the pinned axioms, not from the packet
paraphrase. The td8 review's §3.2/§4.3 fixes, at a charged extra-direction
exit with `c_* != 0`:

```text
(A2)  D_F = integral_0^{tau_0} N dtau,  N(0) = m := mult(p_F,c_*),  N <= m
                                                  =>  tau_0 >= D_F/m
(A4)  q := kappa_H/kappa_F in N*,  q | E_+ <= m
(A5)  w_H = kappa_H(pi(H)-1) = q(tau_0 - kbar_F) in N*                (INT)
```

Write the **defect** `delta := D_F/m - kbar_F`. The two reviewed vertices are
`delta = 17/2 - 7 = 3/2` (td8 trunk, `m = 2i`, `D_F = 17i`) and
`delta = 25 - 17 = 8` (td12 B, `m = i`, `D_F = 25i`), with the td8 A-copy at
`delta = 14/2 - 5 = 2`.

Per flag, `(A2)`+`(A5)` give `w_H = q_H x_H` with `x_H >= delta`, `q_H in N*`,
`w_H in N*`. The decisive extra fact, supplied by Lemma R1(b), is that the
`q = 1` branch **pins `x` exactly**: `q = 1` means no characteristic level in
the normalized range (Notation 3.5), conjugate series separate only at
characteristic exponents, so `N == m` throughout and `(A2)` becomes an
equality, `tau_0 = D_F/m`, hence `x = delta` exactly. The `q >= 2` branch has
no such pin: shedding has occurred, so `x > delta` is permitted and only
`w = qx in N*` constrains.

### 1.2 The maximum safe statement

```text
  MAXIMUM SAFE STATEMENT (theorem at the scope of the two reviewed vertices)

      Lambda(F,c_*)  >=   delta            if delta in Z
                     >=   ceil(2*delta)    if delta not in Z
```

Derivation, three exhaustive branches:

- **single flag, `q = 1`** — admissible only if `delta in Z` (else `w = delta`
  violates `(INT)`); cost `delta`;
- **single flag, `q >= 2`** — `w >= ceil(q*delta) >= ceil(2*delta)`;
- **two or more flags** — each `w_j >= ceil(delta)` by `(A2)`+`(INT)`, total
  `>= 2*ceil(delta)`.

### 1.3 The multi-flag branch: does it have the same per-flag descent floor?

**Yes — `PASS`, and it is proved, not conjectural.** This was hypothesis
(H2) in my blind report, which I named "the one I most expect to need
repair." That was wrong, and the correction is load-bearing enough to state
plainly. The floor is `tau_0 >= D_F/m` with `m` the **total** multiplicity at
`c_*`, not a per-flag count, because `(A2)` bounds `N <= m` pointwise for
*every* ray through `F*c_*` whatever its degree profile. Splitting the
multiplicity group across more flags therefore cannot lower any flag's floor.
Both reviews state exactly this, independently and at different numbers:

- td8 review §3.2: "`w_H >= D_F/m - kbar_F = 3/2` for **every** `H in
  E_F(c_*)` … uniform in `t` because `i` cancels";
- td12 review: "`tau_0 >= D_F/i = 25` holds with or without partings" and
  "the bound is `25 - 17 = 8` for **every** cv flag below the B-direction".

A second, structural consequence nobody has recorded: since
`ceil(2*delta) <= 2*ceil(delta)` for all `delta > 0`, **the multi-flag branch
never binds the lower bound.** The `min` in my blind formula is decorative;
all three reviewed values are decided by the single-flag branch alone. That
matters because it means the three calibration points test only the branch
that is wrong.

### 1.4 `Lambda = min(num(delta), 2*ceil(delta))` is REFUTED as a general law

The first term came from "a lone flag must have `q` divisible by `den(delta)`
to make `q*delta` an integer." That silently assumes `x = delta` in the
`q >= 2` branch — i.e. it imports the `q = 1` pin into the branch where the
pin does not hold. The honest `q >= 2` floor is `ceil(2*delta)`, not
`num(delta)`.

```text
$ python3  (exact Fraction, reproduced verbatim)
td8 trunk    delta=3/2   conj=3 safe=3 reviewed=3
td12 B       delta=8     conj=8 safe=8 reviewed=8
td8 A-copy   delta=2     conj=2 safe=2 reviewed=2

divergences (delta, conjecture, safe):  4/3 -> (4,3)   5/4 -> (4,3)
                                        7/3 -> (6,5)   9/4 -> (6,5)
max overprice conj - safe            :  1        (never 0 < safe)
any underprice                       :  False
all divergences have den >= 3        :  True
all divergences have frac(delta)<=1/2:  True
divergence rate over tested delta<=6 :  122 of 276
```

So:

- the conjecture **never underprices**, and **overprices by exactly one
  unit** on a large slice of the parameter space — `den(delta) >= 3`,
  `frac(delta) <= 1/2`, `num(delta) >= 2*floor(delta)+2`;
- all three calibration points have `den(delta) in {1,2}`, and the two laws
  **agree identically on `den <= 2`**. The entire three-for-three calibration
  is insensitive to the only regime where the formula can be wrong. A
  four-point in-sample fit that cannot see its own failure mode is not
  evidence;
- an overprice of exactly one unit is exactly the size of the td8 kill's
  entire margin (`2+2+3+1 = 8` against `7`). This is not an academic defect.

**Verdict: `REFUTED`** for `Lambda = min(num(delta), 2*ceil(delta))`.
**`PASS`** for the safe law of §1.2 as a lower bound at the reviewed scope.

### 1.5 Every hypothesis, with status

| # | Hypothesis | Status |
|---|---|---|
| H1 | Place conservation: every place through `F*c_*` carries exactly one cv flag, so a lone flag carries all `m` | **PROVED** — St 7.3 with its hypothesis discharged by the Notation 6.1 test `D_F/m > kbar_F`, plus St 3.13 uniqueness (see §2) |
| H2 | Per-flag descent floor `tau_0 >= D_F/m`, uniform over flags, `m` total | **PROVED** — `(A2)`, restated for "every ray"/"every cv flag" in both reviews |
| H3 | `(INT)`: `w_H in N*` | **PROVED** — `(A5)` |
| H4 | `q in N*` (and `q | E_+ <= m`, a cap, unused in the lower bound) | **PROVED** — `(A4)`/Theorem A(4) |
| H5 | `c_* != 0` | **SCOPE HYPOTHESIS** — the `c_* = 0` branch of (4.1) carries an extra `1/nu_F`; the law as stated does not transfer. Named by the td8 review; not carried by any blind report |
| H6 | `q = 1 => N == m => tau_0 = D_F/m` exactly | **PROVED**, and it is the step the whole first branch rests on. Requires the normalization `N(0) = m` at `F` |
| H7 | `Lambda` is per charged **direction** `c_*`, not per vertex | **TYPING REPAIR** — my blind report said "per charged vertex"; a vertex with several charged directions pays a sum |
| H8 | All flags usable simultaneously in `(C7.1*)` | **PROVED** — td8 review §3.1, omitted terms positive |

### 1.6 What remains conjectural

1. **Attainment.** §1.2 is a *lower* bound. It is attained at all three
   reviewed vertices, but attainment in general is a realization question and
   is **not** proved. Do not quote `Lambda` as an exact charge.
2. **Transfer beyond the reviewed vertex type.** The derivation is generic in
   the pinned axioms and was independently reproduced at two different
   numeric frames, but it is licensed only for charged extra-direction
   (`T_a^up`/northeast) exits with `c_* != 0` and `gap > 0`. Pole vertices
   (price 0, separately reviewed) and merge vertices (`lambda_G = 0`,
   Theorem B) are outside it.
3. **The sharper per-vertex value.** `(A4)`'s `q | E_+ <= m` can force
   `q_min > 2`, raising the true charge above `ceil(2*delta)`. The safe law
   ignores this, which is the correct direction for a lower bound but means
   the law is not tight.

### 1.7 The reusable consequence nobody stated

The recorded floors in the menus have the form `max(1, ceil(gap))` — the
td12 consumer review quotes `lambda_F >= max(1, ceil(8)) = 8` explicitly.
For **non-integral** `gap` that recorded floor is an **undercount**: the
licensed floor is `ceil(2*gap)`, i.e. roughly double.

```text
recorded floor ceil(delta)   safe floor ceil(2 delta)
delta = 15/2        8                   15
delta = 17/2        9                   17
delta = 31/2       16                   31
```

This is the quantitative content that Fable's "re-derive each edge floor" and
Grok's "run `FLAG-ARITY` on the menu" are reaching for, and it makes their
sweep far more valuable than either argued: every legacy edge whose floor was
recorded as `ceil(gap)` with `gap not in Z` is priced at roughly half its
licensed value. **`PASS`, and it is the single most actionable line in this
report.**

---

## 2. Charge 2 — is `PLACE-CONSERVATION` a real gap?

**Verdict: `REFUTED`. It is a misreading — and the misreading is mine.**

My blind report §6.1 called this "the highest expected-information-per-hour
item on the board" whose downside branch "reverses two headline results." It
does not, because the property is proved on-page in §3.1 of the very review
whose §4 repair I was worried about. I did not connect the two sections when
writing blind. The proof, reconstructed:

1. **Typing.** Notation 6.1 / Statement 6.2 give the parent test
   `D_F/m > kbar_F`. On the td8 trunk that is `17/2 > 7`, so
   `F*c_* in T_a^up`. This is a property of the *child vertex*, hence shared
   by every place through it.
2. **Totality.** Statement 7.3 says: if some `I_P(u) in T_a^up` then some
   `I_P(v) in T_{a,cv}`. By (1) its hypothesis holds for **every** place `P`
   through `F*c_*`. So every such place has a cv flag.
3. **Uniqueness.** Statement 3.13 gives a unique `u` per point with
   `d_{I(u)} = 0`, so the flag sits at that level and there is exactly one
   per place.

Therefore the map `place -> cv flag` is **total**, and `|E_F(c_*)| = 1` forces
that one flag to carry all `m` places. Place conservation holds in exactly the
direction the arity argument needs.

**Keeping the four notions distinct, which is where my alarm went wrong.**
The step that is genuinely load-bearing is not about **places** at all. A lone
flag carrying all `m` places still does not give `tau_0 = D_F/m`: that needs
`N == m`, a statement about **conjugate series**. Series can shed while the
place, its ray, and its flag are unchanged — precisely the fallacy the td8
review exposed in the producer ("Since separated Puiseux series cannot
remerge, all `2i` series agree strictly below the common cv level"). The
repair does **not** re-use a variant of that inference in the opposite
direction, as I suspected blind; it *avoids* the series question by using
`q = 1 => no characteristic level => no shedding` (Notation 3.5). Places are
handled by St 7.3/3.13; series are handled by `q`. The two are never
identified.

**One residue worth carrying, and it is not a gap.** `(C7.1*)` is stated for
*any* subset of pairwise-distinct cv flags because every omitted term is
positive. Using the full set is licensed and gives the **largest** left-hand
side, i.e. the strongest kill. Selection can only weaken a kill, never
manufacture one, so MFE selection is safe in the kill direction.

**Consequence.** My blind card 2 is withdrawn. Its claimed downside branch —
"the `td=8` affine equal-join family is alive again" — does not exist. The
td8 kill's genuine load-bearing dependencies are the ones the review already
records: the `psi = 1` x-side unit (margin exactly one; `psi = 0` reopens the
family at `2+2+3 = 7 <= 7`) and hypothesis H6. Anyone auditing that margin
should audit `psi`, not place conservation.

---

## 3. Charge 3 — Sol's U2 resonant family against the claimed ODE scope

Sol's blind §2 displays, and calls a refutation of the degree argument:

```text
R = T^r - 1,  S = T^r,  L = r,  C = -rR
r R S' - L R' S = -r^2 T^(r-1) = C'
```

**The algebra is correct.** I verified it by hand:
`r(T^r-1)(rT^{r-1}) - r(rT^{r-1})T^r = -r^2 T^{r-1}`, and `R` is squarefree
with roots off `0`, `gcd(R,S) = 1`, both monic of degree `r`. Sol's structural
side conditions all hold.

**It nevertheless refutes nothing, for two independent reasons.**

**(a) `C'` is a nonzero constant, not a derivative — `SCOPE-CONFLICT`.** In
the campaign's absorbed U2 normal form (Fable narrowing `e156f94c…`, which the
producer declares as a dependency), with `p = Rad^mu`, `q = Rad*S`,
`rho = r*mu/(r+L)`:

```text
rho p q' - p' q = p (mu/(r+L)) (r Rad S' - L Rad' S)
Prop 8.1(iv)  <=>  r Rad S' - L Rad' S = C' != 0,   C = mu C'/(r+L)
```

`C'` is a **scalar**. The review computes it as `C' = -2A s_1` (`r = 2`),
`C' = -r A s_1` (`r >= 3`), and `C' = r W(S,Rad)` *constant*; and its free
admissibility lemma — "a shared or double root `xi` gives `0 - 0 = C'` at
`xi`, contradiction" — is only valid because `C'` takes one value everywhere.
The prime in `C'` is a name, not `d/dT`; note `C = mu C'/(r+L)` would force
`C' = 0` if it were literally `C`'s derivative. Sol read `C'` as the
derivative of a polynomial `C`, chose `C := -rR`, and thereby solved a
*different* equation. For `r >= 2` the left side of Sol's family is
`-r^2 T^{r-1}`, a non-constant polynomial, so the family is **not a solution
of the U2 transport equation at all**. Sol's own card-3 outcome (iv) — "the
symbols occupy different mathematical roles … verdict `SCOPE-CONFLICT`,
repair the translation before further algebra" — is the branch that fires.
Credit to the card design; the executive claim built on it is wrong.

**(b) Even taken at face value, the family sits in an already-closed case.**
Sol's family has `L = r`. The same pre-cutoff reviewed narrowing proves
`L = r` is **universally** dead, not merely dead on the power shape:
`C' = r W(S,Rad)` constant forces `S/Rad = (C'/r) integral Rad^{-2}` to be
rational, whose residue at a root `a_i` is proportional to
`Rad''(a_i)/Rad'(a_i)`, and `Rad''` (degree `r-2`, leading coefficient
`r(r-1) != 0`) cannot vanish at all `r` distinct roots. Sol's own family
confirms it: `Rad S' - Rad' S = -r T^{r-1}`, constant only at `r = 1`, while
`r >= 2` is fixed.

**(c) The producer's own lemma is sound.** I checked "universal death for
`R|K`" line by line: with `K = mR`, `(T)` reads `P S' - m P' S = c/R != 0`;
the operator annihilates `P^m`; `T0 = S - (lc S/lc P^m) P^m` is nonzero of
degree `d < mR`; the leading coefficient of `P T0' - m P' T0` is
`lc(P) lc(T0) (d - mR) != 0` at degree `R + d - 1 >= R - 1 >= 1`, so it cannot
be a nonzero constant. Correct, including the `d = 0` case. **`PASS`.**

**Verdict on charge 3: `REFUTED` as a refutation; the family merely exhibits
the already-excluded resonance, in a mistyped equation.** Consequences:

- Sol's executive claim "the U2 advance is less secure than the packet's
  provisional ranking suggests" is **not supported** by the evidence offered;
- Sol's ranked #1 information-gain item ("the U2 resonance substitution …
  can reverse a provisional advance") is now **executed and closed** at desk
  cost, in this report;
- the queued different-model review of `99bbe233…` is still warranted, but
  its aim should move **off** the ODE degree lemma — which survives two
  independent checks — and **onto** equation `(E)`, the edge typing, and the
  producer's own named residues: whether the campaign's intended "first
  nested boundary" really is the direct edge quantified in its §1, and
  whether an unrecorded mandatory chain edge lies between the two states.

---

## 4. Charge 4 — stress tests

### 4.1 `PIC-DISC` (Sol, card 1) — `PASS_WITH_REPAIR`

**The identity is correct.** Re-derived independently: for `phi: X -> Y`
generically finite of degree `d` between smooth projective rational surfaces,
`phi^*` is injective on `NS`, the projection formula gives
`A^T Q_X A = d Q_Y`, so `|disc M| = |det(d Q_Y)| = d^rho(Y)` since `NS(Y)` is
unimodular; index scaling gives `|disc M| = h^2 |disc Mbar|`; and primitivity
of `Mbar` in the unimodular `NS(X)` gives `|disc Mbar| = |disc K|`. Hence
`|disc K| h^2 = d^rho(Y)`. **`PASS` on the mathematics.**

**Repair 1 — the obstruction content is far weaker than advertised.** The
identity is a *consequence* of having the morphism; `K` is *defined* as
`Mbar^perp`, so `|disc K|` is derived, not measured. The only non-tautological
residue is the divisibility `h^2 | d^rho(Y)`, and it bites only if `h` is
computed independently from boundary data. Sol pre-registers this as outcome
(iv), which is good card design, but the report's framing ("can kill a
complete boundary record without enumerating its local M2 coefficient
descendants") oversells a consistency check.

**Repair 2 — quantifier.** `X`, `Y`, and `A` are not free data; they come from
resolving a *hypothetical* counterexample. Any record that genuinely arises
from a morphism passes by construction. `PIC-DISC` can therefore falsify a
*claimed or incomplete* landing record — real value as a landing-output
validator — but it is not an obstruction to JC2, and Sol's own outcome (i)
caveat says as much.

**Repair 3 — strength scales with `rho(Y)`.** If `Y = P^2`, `rho(Y) = 1`, `M`
is rank one generated by `phi^*H`, and the identity degenerates to a
restatement of the degree. The test only acquires teeth on large boundary
graphs — exactly where the unpaid landing dependency lives. So the mechanism
is real, correct, and structurally parked behind the same wall.

**History.** `Picard` appears twice in `APPROACHES.md` (row 35's
`Z/(d-2)` dimensional-descent obstruction, and the `Picard group Z` hyperplane
remark) and `Smith normal`/`saturation index` appear zero times across the
canonical roots. Sol's `NEW` label is **sustained** at campaign scope.

### 4.2 `EXIT-RH` and `ARITY-CEIL` (mine) — `REFUTED`, and partly `DUPLICATE`

I withdraw both. Three independent failures, in increasing severity.

**(i) `DUPLICATE` on the Riemann-Hurwitz half.** `APPROACHES.md` line 4734
already records avenue 25/26's stage-1 experiment: "assume ramification of
`\hat g` supported at `<= N` places at infinity, Riemann-Hurwitz, transitivity,
primitivity; enumerate types for `td = 6,7,8,9`". The RH-on-`\hat g` idea is
`KNOWN` and on record. My blind report labelled it a `NEW` connection; that
label is wrong. The only new part is "let the `q >= 2` exit flags supply the
support bound" — and the recorded experiment already names the support bound
as its missing input, which is a better framing than mine but does not make
the connection new.

**(ii) Typing, as I flagged blind and now resolve against myself.**
`q = kappa_H/kappa_F` is a Puiseux denominator jump along a ray in the
Eggers-Wall tree of the *source curve* `p_F`. Calling it ramification of the
degree-`td` map `\hat g` at infinity is the forbidden local-to-global
identification unless a theorem supplies the map. No such theorem exists.
Grok's row 25 ("local flag torsion is not target-component inertia") reaches
the same place independently. **`SCOPE-CONFLICT` until typed; per my own card
3's stop rule, that means stop.**

**(iii) The fatal one: `ARITY-CEIL` is dead on the desk, no computation
needed.** My blind card 1 step B — price the two banked formal countermodels
under the ledger — was billed as "the single most informative run in the
package". It is answered structurally, and negatively:

- Statement 3.13 gives a **unique** level per point with `d_{I(u)} = 0`, so
  there is **at most one cv flag per place**. The budget's left-hand side
  `sum_{F in U^full} lambda_F^exit` is therefore a sum indexed by *places*,
  not by tree vertices or characteristic levels.
- Banked Lemma 2.2 sends its unbounded parameter to infinity by **inserting
  `r` characteristic vertices** (`q = q' = 2`, `w = 2` preserved) along
  existing rays at fixed `td = 6`, `deg Psi = 36`, `E_MR = 1`, with
  `kappa_i = 42*2^r -> infinity`. Inserting characteristic vertices adds no
  places, hence no cv flags, hence **no ledger cost at all**. The exit-charge
  ledger is structurally blind to exactly the operation the countermodel uses.

So the ledger is *not* strictly stronger than the tree/arithmetic identities
the countermodels satisfy; on Lemma 2.2 it is silent. My blind report's
claimed "genuine bypass of the KJN/RPMC decomposition" is **`REFUTED`**, and
`ARITY-CEIL` collapses onto the recorded, unpaid avenue-26 support bound —
i.e. `DUPLICATE` of a known debt. Lemma 3.1 (`td = 6b -> infinity`) is not
settled by this argument, but the burden now sits with any future proposer.

**Bonus defect in my own blind text, recorded so it is not inherited.** §4
asserted "`Lambda(v) >= 2` at every charged vertex." False: `delta = 1` gives
`Lambda = 1`, and `delta <= 1/2` gives `Lambda = 1`. The td8 ledger's `+1`
term is an `H_x` unit at `psi = 1`, not a `Lambda`-priced extra direction, so
it is not a counterexample — but the asserted floor of `2` was never derived
and must not be reused. `Lambda >= delta` survives.

**Net: my blind report's #2-ranked proof bottleneck (cofinal ceiling promoted
on the strength of `ARITY-CEIL`) reverts to its prior rank with no mechanism.**
Grok's and Fable's blind dispositions (row 26 unchanged, "killing one U1
family does not license a ceiling") were right; my raise was wrong.

### 4.3 The `A(F)` / one-place connections

**Fable C-NEW-1 (pole purity unblocks the banked `A(F)` bridge) —
`PASS_WITH_REPAIR`; and Grok's blanket rejection is too strong.**

Grok's composition table records "pole-purity + ACS: **NO HIT**… poles are
`g = infinity`, `A(F)` is affine. Identifying them is `SCOPE-CONFLICT`."
Adjudicating: Fable never proposes that identification. Fable proposes the
*converse* typing — use `g(P) = infinity` to **exclude** pole rays from the
finite-value census and keep only both-finite cv exits. That is exactly the
right use of the purity theorem and is not a scope conflict. Grok's verdict is
right in its conclusion (the bridge is blocked) and wrong in its reason.

The actual defect is a **quantifier**, and it is the one Fable claims to
bypass. The census gives: every listed both-finite exit orbit is a candidate
carrier of asymptotic values. The conclusion Fable wants ("exactly one
both-finite exit orbit `=>` `A(F)` irreducible") needs the *converse*: every
component of `A(F)` arises from a listed exit flag. `APPROACHES.md` row 7
records `A(F)` as "never constructed from the books" with the raw pencil
defect `JUMP-ONLY / TYPE-FAIL`. So the surjectivity direction **is** the
unpaid component-labelling debt, and "unblocks M7-F without avenue-7's
horizontal packet" fails. Verdict: `GAP` on the bridge, `PASS` on the typing
instrument, and Fable's own step-0 gate (M7-F must first pass its cheap
different-model check) correctly contains it.

**Fable C-NEW-2 (depth-24 "bamboo" as avenue 6's first correctly-typed
client) — `GAP`; the "correctly-typed" label is unearned.**
`APPROACHES.md` row 6 records the documented category error ("fibers are
multi-place; category error documented twice") **and** its resolution:
"Correct one-place objects are `A(F)` components, whose place data are
unpinned." The bamboo is a third object — a one-place branch datum of the
source curve `p_F` to depth 24 — and it is neither a fiber nor an `A(F)`
component. Abhyankar-Moh constrains a curve with one place at infinity
*embedded in the affine plane*; a local branch datum is not that. The
arithmetic Fable offers is correct (`gcd(6n,25) = gcd(n,25)` since
`gcd(6,25) = 1`), but arithmetic is not typing. Fable's zero-allocation,
typing-scope-only reopen is the right containment; the label should be
demoted from "first correctly-typed client" to "third candidate object,
untyped."

**Sol `COVER-MOD` — `PASS` on the algebra, `DUPLICATE` on the mathematics.**
I recomputed the Jacobian from scratch and get Sol's expression exactly:
`J(u,v) = (ad-bc) x^(a+c-1-k(b+d)) (y-h)^(b+d-1)`. Constancy forces
`b+d = 1` and `a+c = k+1`; with `b,d >= 0`, `a-kb >= 0`, `c-kd >= 0` the two
cases give `|det| = a <= 1` and `|det| = c <= 1`. **Correct, and correctly
scoped by Sol** ("says nothing about arbitrary sums, nonmonomial units,
multiple charts, or two modifications"). But the content is the classical fact
that a monomial map with constant Jacobian has unimodular exponent matrix.
History label repair: `NEW` to the campaign record, `KNOWN` externally; it is
a negative control, not evidence.

### 4.4 Sibling versus B-child priority

**Convergence.** Grok card 1, Fable card 1 item 1, and my blind out-of-sample
prediction all target the `(3/4,4)@nu_F=17` sibling; Grok and Fable both rank
it first. Sol's "do not touch the sibling through this card" is a scoping
instruction for its card 2, not a dissent. **3/4 convergence, and I concur.**

**But the reports understate the test, and one of them mis-scopes it.** From
pre-cutoff records: Grok's own primary tabulates the sibling as
`nu_F = 17, k = 2, (3/4,4)`, floor `8`, `psi = 3`, ceiling `td-1-psi = 8`,
**slack 0**; and my earlier trunk-consumer review noted `8 + 3 = 11 > 8` would
kill it — under the `+3` pole price that the packet now records as
**withdrawn** (pole/interior-child typing regression, price exactly 0). So the
sibling currently survives at an exact knife edge, and the recorded floor `8`
was produced by the pre-dichotomy rule `max(1, ceil(gap))`.

Combining with §1.7 gives a **sharper discriminator than any blind report
states**:

```text
   sibling verdict  =  one yes/no question

   delta_sib := X_F/m - kbar_F   (computable from the recorded frame:
                                  kbar = l w_G dq/E,  X = kbar dp/dq)

   delta_sib in Z   ->  Lambda = delta_sib;  survives iff delta_sib <= 8
   delta_sib not in Z -> Lambda >= ceil(2 delta_sib) >= 15 > 8  ->  DEAD
```

Because the recorded floor is `8`, a non-integral defect immediately roughly
doubles the price past a ceiling with zero slack. **Is `delta_sib` an
integer** is the whole test — one line of exact arithmetic from data already
in the menu. Neither Fable's `min(2(tau_0-kbar), q>=2 price)` nor Grok's
"apply `FLAG-ARITY`" states it this sharply.

**Danger, and it is mine.** The sibling has `M_F = 4`. If `den(delta_sib)`
is `3` or `4` with `frac <= 1/2`, my blind closed form and the safe law differ
by exactly one unit — at a target with **zero slack**. See charge 5.

**B-child cards — `DUPLICATE` at the gate level.** Grok card 2, Fable card 2,
and Sol card 2 are the same object: the first B-child coefficient vector and
the level-1 test. Sol's catalecticant/Veronese membership condition is
mathematically **equivalent** to the packet's scalar test — a degree-`i`
univariate `C` is a pure `i`-th power iff `deg gcd(C,C') = i-1` iff its binary
form lies on the rational normal curve iff all `2x2` catalecticant minors
vanish. It is a reformulation, not a second gate. Sol's conormal
"early-failure accelerator" is the only genuinely new part and Sol correctly
hedges that it "certifies only first-order contact." Fable's persistence
framing and Grok's "24 levels are one recurrence, not 24 tests" are the same
observation and are both right.

---

## 5. Charge 5 — deduplicated ranked action list

**Duplicate classes across the four blind lanes.**

| Class | Lanes | Adjudication |
|---|---|---|
| Uniform exit-charge functional (`ARITY-LAW`/`FLAG-ARITY`/`lambda_min`/`EXIT-PARTITION`) | **4/4** | `DUPLICATE`. Best design is Sol's: a typed schema separating flags/places/series/orbits with a fail-closed `UNTYPED/NO_VERDICT`. Best content is the §1.2 safe law. Worst is mine (closed form, `REFUTED`) |
| Sibling repricing | Grok C1, Fable C1, Opus prediction | `DUPLICATE`; sharpen to the integrality test of §4.4 |
| Legacy floor sweep (13-edge menu, MFE/td7/LL-1 verify) | Fable only | **Unique, and now the highest-yield item** (§1.7) |
| B-child level-1 | Grok C2, Fable C2, Sol C2 | `DUPLICATE`; catalecticant equivalent to gcd |
| U2 direct-edge review | Grok C3, Fable priority, Sol C3 | `DUPLICATE`; Sol alone supplied a concrete attack, executed and closed in §3 |
| Anti-fallacy propagation | Opus, Grok, Sol | `DUPLICATE`; see charge 6 |
| Hash-pin resolution linter | Fable only | Unique, different class, partly covered by the 07:24Z recorder |
| `PIC-DISC`, `COVER-MOD` | Sol only | Unique |
| `EXIT-RH`/`ARITY-CEIL` | Opus only | Unique and `REFUTED` (§4.2) |
| Bamboo/AM typing | Fable only | Unique, `GAP` |

**Ranked action list, deduplicated, by expected information per desk-day.**

1. **Sibling integrality test.** Compute `delta_sib = X_F/m - kbar_F` from the
   recorded frame; integral `=>` charge `= delta_sib`, non-integral `=>`
   charge `>= ceil(2 delta_sib)`, which kills a zero-slack terminal. One line.
   **Use the §1.2 safe law, never the blind closed form.**
2. **Legacy floor re-pricing sweep** under §1.7. Every recorded
   `max(1, ceil(gap))` with non-integral `gap` is an undercount by ~`gap`.
   Re-derive the 13-edge menu, then the MFE/td7/LL-1 verify passes. Any floor
   that rises triggers the standard consumer rollback.
3. **Re-aim the U2 different-model review.** The ODE degree lemma survives two
   independent checks (§3); point the review at equation `(E)`, the edge
   typing, and the producer's own two named residues.
4. **B-child level-1** (`deg gcd(C_1,C_1') = 6n-1`), run forward as a
   coefficient generator so it doubles as the counterexample-side seed. All
   three lanes that proposed it agree; nothing here changes it.
5. **Exit-charge evaluator**, built as Sol specified (typed schema, fail-closed
   `UNTYPED`) with the §1.2 law as its core and the three reviewed values plus
   a `den(delta) = 3` divergence case as hard fixtures.
6. **Systems upgrade** — charge 6.
7. **`PIC-DISC`** — park behind landing; re-scope as a landing-output
   validator, not an obstruction.
8. **`EXIT-RH` / `ARITY-CEIL`** — **stop**. Record the §4.2 structural reason
   in the negative-results channel so it is not re-derived.
9. **Bamboo/AM** — one typing paragraph, zero allocation, per Fable.
10. **`COVER-MOD`** — record as a negative control; no successor search.

### The single proposal most likely to waste a week if left unreviewed

**`Lambda = min(num(delta), 2*ceil(delta))` — my own blind closed form.**

Not because it is the weakest idea on the board, but because it is the one
positioned to do damage:

- **it is the object four of four lanes independently converged on**, so it
  will be picked up;
- **its designated first application is a zero-slack target** — three lanes
  rank the sibling first, and its ceiling equals its floor;
- **its error is exactly one unit, in the kill-licensing direction**, and only
  for `den(delta) >= 3` — a regime the sibling's `M_F = 4` makes plausible and
  which the entire three-point calibration cannot see;
- **the failure is silent and self-confirming.** A false sibling kill would
  read as a triumphant out-of-sample confirmation of `Lambda`, would empty the
  first-trunk `P1`-fitting set, and would then be used to argue the depth-24
  gate is family-decisive — or, worse, unnecessary. That contaminates the
  campaign's only live counterexample seed;
- **and it is presented with three-for-three calibration**, which is exactly
  the kind of evidence that stops further checking.

Runner-up: Fable's C-NEW-1 claim that pole purity unblocks the `A(F)` bridge
*without* the horizontal packet (§4.3) — a week of census-building for a
consumer whose surjectivity quantifier is unpaid. It is contained by Fable's
own step-0 gate, which is why it is second and not first.

---

## 6. Charge 6 — one bounded systems upgrade, with the trial half-run

**Comparison of the four cards.** Three lanes (Opus, Grok, Sol) independently
identify the same evidenced failure — the td12 producer repeated the
flag/series shortcut that the td8 reviews had just repaired — and propose
three mechanisms; Fable proposes a different class (hash-pin resolution),
which is real but partly covered by the 07:24Z declared-input recorder.

**I ran the decisive half of the trial this session, and it falsifies the
cheap mechanism — including my own.**

```text
Grok's literal denylist, against its own designated regression seed
(both producers "should hit"):

  phrase                            td12 producer   td8 producer
  "one flag means"                        0               0
  "conjugate series stay together"        0               0
  "no series split"                       0               0
  "pole price unknown"                    0               0

Shape-regex fallback:
  'all .{0,12}series'   td8 = 1   td12 = 0   U2 control = 0
  'series (agree|stay)' td8 = 1   td12 = 0   U2 control = 0

Occurrences of the word "series" in the td12 producer 2a151eef: 0
```

The td8 producer's actual fallacious sentence is "Since separated Puiseux
series cannot remerge, all `2i` series agree strictly below the common cv
level" — a shape-regex catches it. **The td12 producer never uses the word
"series" at all**; its repetition reads "Already with this one flag, Corollary
7.1 gives …". The same invalid inference recurred with **zero lexical
overlap**. No prose lint — Grok's literal denylist, any shape-regex, or my own
`FALLACY.md` prompt appendix, which likewise depends on a producer recognising
the pattern in prose — can catch it. Grok's card fails its own pre-registered
prediction; my card's "at least three of ten" trial measures coverage, not
effect, and would have passed while catching nothing.

This vindicates Sol's diagnosis (a mechanism that "propagates declared hazards
cannot discover an undeclared or synonymously repeated inference") while
showing Sol's full inference-ID taint graph is larger than "smallest useful."

**`UPGRADE` — the declared `charge_basis` field.** Require every promoted
exit-charge claim to carry one machine-checkable structured field:

```text
charge_basis:
  delta        : exact Fraction  (numerator/denominator explicit)
  branch       : one of { q=1-exact | q>=2 | multi-flag }
  flag_count   : single | multi,  with the licensing citation
```

with one rejection rule: **a `q=1-exact` branch is rejected unless
`delta.denominator == 1`.** That single rule is exactly the invalid step in
the td8 producer (single flag, `N == 2i`, `tau_0 = 17/2`, `delta = 3/2`), it
forces the denominator into the open where my own `Lambda` error also lives,
and it is checkable without reading prose.

**Pre-registered pass/fail trial — four fixtures, adopt only on 4/4.**

| # | Fixture | Required outcome |
|---|---|---|
| 1 | td8 producer `3c2c9a7e` | **FIRE** — declares single-flag exact weight with `delta = 3/2 not in Z` |
| 2 | td12 producer `2a151eef` | **FIRE** — single-flag conclusion with no declared `q`-exclusion (weaker fixture; verify at implementation) |
| 3 | repaired td8 review `51f3ed7c` | **GREEN** — declares the `q`-dichotomy branch explicitly |
| 4 | U2 producer `99bbe233` | **GREEN** — carries no exit-charge claim; field absent, must not fire |

**Fail conditions:** any fixture wrong; or the field cannot be filled from the
two reviewed reports without guessing; or the added producer burden exceeds
one field. On failure, record `NO_UPGRADE` and fall back to the one-line
reviewer-contract obligation ("state which listed anti-patterns you checked"),
which is the only surviving cheap option after the trial above.

**Cost/risk.** One declared field, one rejection rule, four fixtures; no run
path, no custody surface, read-only at promotion time. Inside the standing
48-hour systems window (next checkpoint `2026-08-31 07:24Z`). It displaces
Fable's hash-pin linter, which should stay queued — it addresses a real but
lower-frequency class already partly covered.

---

## 7. Consolidated verdicts

| # | Object | Owner | Verdict |
|---|---|---|---|
| 1 | `Lambda = min(num(delta), 2 ceil(delta))` | Opus (blind) | **REFUTED** — overprices by exactly one unit for `den >= 3`, `frac <= 1/2`; calibration blind to its own failure mode |
| 2 | Safe law `Lambda >= delta` (`delta in Z`), `>= ceil(2 delta)` otherwise | this report | **PASS** as a lower bound at the two reviewed vertices' scope |
| 3 | Per-flag descent floor (H2) | Opus (blind) called it weakest | **PASS** — proved from `(A2)`; blind assessment withdrawn |
| 4 | Multi-flag branch binds the minimum | implicit in all four lanes | **REFUTED** — `ceil(2d) <= 2 ceil(d)` always; it never binds |
| 5 | Recorded floors `ceil(gap)` with non-integral `gap` | campaign record | **GAP** — undercount by ~`gap`; re-price |
| 6 | `PLACE-CONSERVATION` as a gap | Opus (blind) | **REFUTED** — proved on-page (St 7.3 + Notation 6.1 + St 3.13) |
| 7 | Sol's U2 resonant family as a refutation | Sol | **REFUTED**; `SCOPE-CONFLICT` on the `C'` reading |
| 8 | Producer lemma "universal death for `R|K`" | Sol producer `99bbe233` | **PASS** — verified line by line |
| 9 | `PIC-DISC` lattice identity | Sol | **PASS_WITH_REPAIR** — identity correct; obstruction content is `h^2 \| d^rho` only; parked behind landing |
| 10 | `EXIT-RH` | Opus (blind) | **REFUTED** / **DUPLICATE** of the recorded avenue-26 stage-1 experiment; untyped |
| 11 | `ARITY-CEIL` | Opus (blind) | **REFUTED** — St 3.13 caps cv flags at one per place; ledger blind to Lemma 2.2 |
| 12 | Pole purity `x` `A(F)` bridge | Fable C-NEW-1 | **PASS_WITH_REPAIR** on typing; **GAP** on the surjectivity quantifier. Grok's blanket `SCOPE-CONFLICT` is too strong |
| 13 | Bamboo as avenue-6 client | Fable C-NEW-2 | **GAP** — "correctly-typed" unearned; correct one-place objects are `A(F)` components |
| 14 | `COVER-MOD` one-modification no-go | Sol | **PASS** on algebra; **DUPLICATE** externally (monomial Keller maps) |
| 15 | Catalecticant vs gcd pure-power test | Sol C2 | **DUPLICATE** — mathematically equivalent |
| 16 | Sibling first, B-child second | Grok C1/Fable C1 vs Sol | **PASS** — 3/4 convergence; sharpened to an integrality test |
| 17 | Uniform exit-charge functional | all four lanes | **DUPLICATE** 4/4; Sol's typed fail-closed design dominates |
| 18 | Literal denylist / prose fallacy lint | Grok, Opus | **REFUTED** by pre-run trial (0 hits on both producers) |
| 19 | Declared `charge_basis` field | this report | `UPGRADE` proposed with a 4-fixture pass/fail trial |

---

## 8. What this report does not claim

- No proof or counterexample to JC2. Nothing here supplies landing,
  `G2-PSC`, `G2-BD`, full family-aware source realization, a corrected-sheet
  global theorem, a type or cofinal degree ceiling, or algebraization.
- The §1.2 safe law is a **lower bound** at the scope of the two reviewed
  vertices, with hypotheses H1-H8 listed and H5 (`c_* != 0`) an explicit
  scope limit. Attainment is not proved; do not quote it as an exact charge.
- §1.7's undercount claim licenses a **re-derivation**, not a kill. No family
  is declared dead here.
- §4.4 does **not** decide the sibling. It states the one-line test and warns
  which law to use. `delta_sib` was not computed: its frame data are not
  derivable from the reports I read without guessing, which is itself the
  first thing the executor should file if it is missing.
- §4.2 refutes `ARITY-CEIL` as a *ceiling mechanism* via Lemma 2.2. Lemma 3.1
  is not settled by that argument.
- §3 closes Sol's specific substitution. It does not certify the U2 producer,
  whose equation `(E)`, edge typing, and two self-declared residues remain
  unreviewed. I did not reconstruct `(E)`.
- The charge-6 trial was run only on fixtures 1-2 and the U2 control;
  fixture 2 is the weaker one and must be re-verified at implementation.
- No canonical file was edited; no commit, push, AWS action, web access, or
  heavy computation occurred; no post-cutoff report was read; `jc2-lean` was
  not entered, enumerated, searched, read, built, statused, modified, or
  controlled.

*Report body ends. The seal below covers everything above this line.*

## Seal

```text
report_body_sha256 = 6e8a9d1947903a45a466d9230fda8bcd24efdbfed5ca4fb16dce6396a0813a9b
report_body_bytes  = 43568
```

The body seal is the SHA-256 of the first 43568 bytes of this file, i.e. up
to and including the line
`*Report body ends. The seal below covers everything above this line.*`
and its trailing newline. Verify with:

```
python3 -c "import hashlib,pathlib; b=pathlib.Path('xmodel/ideation-20260829T0820Z-crosspoll-opus5.md').read_bytes(); print(hashlib.sha256(b[:43568]).hexdigest())"
```

The full-report SHA-256 covers the complete file bytes including this
appendix. Compute with:

```
python3 -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('xmodel/ideation-20260829T0820Z-crosspoll-opus5.md').read_bytes()).hexdigest())"
```

Inputs verified byte-exact this session:

```text
65afb334763023765f701ee9a2140087a47c6ae470877cee0a04b4f4651c0d8f  xmodel/ideation-20260829T0820Z-state-packet.md
cc58a521b92955b8c1e423aacdf60a5b619ba5384c9e05781bafec1ed7647b8c  xmodel/ideation-20260829T0820Z-fable5.md
142d1e3dcd1305dda7397b5cd8f812080c2bf6d6eeb7106203fce9912777e451  xmodel/ideation-20260829T0820Z-opus5.md
ec454b2e958690f396bbd14e901afcb1b5faf9204907911d27b8ab1c972cd98a  xmodel/ideation-20260829T0820Z-grok46.md
ad50d1ada197a3ad424f321707ea62105fafc74a650d8b55e34cc1130c2efa84  xmodel/ideation-20260829T0820Z-sol56.md
```

Basis commit for every supporting read: `eaad172e59742ef8cfd055eace9bc6d3b2da8463`.
