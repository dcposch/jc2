# `OPEN[CHILD-TOP-AT-US-GE-2]` — the child's extra characteristic pair at `u_s >= 2`

Lane `child-top-us2-opus5-20260905`; adapter opus. Drivers
`box/child-top-us2-20260905/`. Frozen inputs `/tmp/jc2-lane.qo8l0p/inputs`.

## 0. Verdict first

```text
(A) THE OPEN'S BINARY FRAMING IS WRONG.  It asks "is M'_{s'+1} = n'-1, or is
    M'_{s'+1} < n'-1?".  Moh p.150 admits a THIRD case, and it occurs:
      (a) M'_{s'+1} = infinity  -- min{i : f'_i != 0, d'_{s'+1} /| i} is EMPTY.
          p.150 sets M_{h+1} = infinity whenever that set is empty; it does NOT
          require d_{h+1} = 1.  The child's chain then ENDS at d'_{h'+1} = u_s.
      (b) M'_{s'+1} = n'-1     -- dropped by the p.174 Definition-Remark.
      (c) M'_{s'+1} < n'-1     -- effective; s' is NOT the child's last pair.
    (a) and (b) both give V'_{s'+1} = d'_{s'+1} and LICENSE (C-TOP);
    (c) REFUTES it.  Existence of M'_{s'+1} < infinity was assumed, not proved.

(B) REDUCTION (proved, Sec. 2).  The child's own p.150 expansion is the parent's
    x-side p.150 datum: with pi <-> y and gamma <-> x,
        M'_j  =  M~_j  :=  the j-th characteristic exponent of (f,g) taken with
                           x as the parameter and k(y) as the base field,
    and n' = deg_x g, m' = deg_x f -- exactly Prop 6.3(2)'s pi-degrees.  This
    turns "the child's own expansion" into a computable invariant OF THE PARENT
    and is what makes (1) executable at all.  Validated 8/8 exactly.

(C) REFUTED AS POSED (Sec. 4).  M'_{s'+1} = n'-1 is NOT a consequence of the
    descent data.  Over 1,199 instances that reproduce EVERY numerical
    prediction Prop 6.3(2) + Moh p.207 make about the child
      (n' = deg_x g, m' = deg_x f, M'_i = M_i u_s/d_s for i <= s-1, d'_{s'+1}=u_s),
    with u_s in {2:425, 3:407, 4:287, 5:80}:
        case (c)  1,188      case (a)  11      case (b)  0.
    Zero instances of the conjectured value.  The 10 instances with s >= 2 (the
    ones whose inherited-level check M'_1 = M_1 u_s/d_s is NOT vacuous) are all
    u_s = 2 and all case (c).

(D) SCOPE LIMIT, STATED UP FRONT.  None of the 1,199 carries delta_s = -1.  By
    Prop 5.1 (p.173-174) delta_s = -1 <=> M_s = n-2, and no random pair meets
    that codimension-heavy condition (0 of ~54,000 generated).  So (C) refutes
    the statement AS A CONSEQUENCE OF THE DESCENT, and does NOT refute it on the
    census locus.  The exact extra condition is typed in Sec. 5.

(E) COUNTERFACTUAL, computed but NOT charged: were (C-TOP) licensed at u_s >= 2
    it would kill 225 of the 310 operative rows and 196 of the 233
    descent-forced ones.  It is not licensed.  Corrected partition in Sec. 5.
```

No new exit-price assertion is made, so no `charge_basis` line is licensed.

---

## 1. Frozen-input gate

Manifest built with `awk` from the `charged_input_<i>_basename=` /
`charged_input_<i>_sha256=` lines of
`xmodel/child-top-us2-opus5-20260905.run.v2` and checked with `sha256sum -c`:
**7/7 `OK`**, no digest retyped. Banked at
`box/child-top-us2-20260905/inputs.sha256` (+ `inputs.check.log`); artifacts at
`artifacts.sha256`.

Page images rendered here at 300 dpi from the charged PDF (its text layer drops
the display math on every one of them): **p.150** `pg11-11.png`, **p.173**
`pg34-34.png`, **p.174** `pg35-35.png`, **p.197** `pg58-58.png`, **p.198**
`pg59-59.png`, **p.201** `pg62-62.png`, **p.207** `pg68-68.png`. Every quotation
below is read off those images.

---

## 2. The reduction: the child's own expansion IS the parent's x-side datum

### 2.1 What Prop 6.3 actually substitutes

**p.197, Prop 6.3**, verbatim: `sigma = sum a_j theta^j + pi theta^{v_s/u_s}`,
`gamma = theta^{1/u_s}`, `y^{-1} = theta`, `z` defined by equation (10); and
**p.198**, verbatim, the inversion
`x = (1/b)[theta^{-1} + sum_{i<v_s/u_s} c_i theta^i + higher]`, `y = theta^{-1}`,
`z = y - bx - e`. So the descent is the substitution

```text
      y = gamma^{-u_s},        x = (y - e - sigma)/b ,
      sigma = (c_0-e) + sum_{0<i<v_s/u_s} c_i gamma^{u_s i} + pi gamma^{v_s} .
```

### 2.2 Which place of the child is `pi = infinity`

Hold `gamma` fixed and let `pi -> infinity`. Then **`y = gamma^{-u_s}` is FIXED**
and `x = -(gamma^{v_s}/b) pi + O(1) -> infinity`. Hence

> the child's place at `pi = infinity` over `k(gamma)` is the parent's place at
> `x = infinity` over `k(y)`.

p.150 assigns the roles by "`g` monic in `y` with `deg_y g = n`"; Prop 6.3(2)
says `gbar(sigma)` is **monic in `pi`** with `pi`-degree `n'`. So `pi <-> y` and
`gamma <-> x`, and the child's p.150 datum is the parent's datum read with `x`
as the parameter. Two immediate consistency checks, both of them Moh's own
numbers:

* `deg_z gbar = deg_x g` (the shear `x = (y-e-z)/b` is degree 1 in `z`, no
  cancellation), and p.197's proof prints `deg_z gbar = u_s n/d_s`. Hence
  **`deg_x g = n'`** and, by the same line, `deg_x f = m'` -- i.e. Prop 6.3(2)'s
  two `pi`-degrees are the parent's two x-degrees, not new quantities.
* The remaining moves are `k(gamma)`-affine in the parameter (`x` is scaled by
  `-gamma^{v_s}/b` -- exactly what makes `g'` monic -- and translated by
  `c(gamma)`), plus `T_1^psi(f,g) = +-f + poly(g)` whose extra terms sit at
  `eta`-exponents divisible by `n` and so can never be an `M_j`. None of these
  changes the branch, hence none changes any `M_j`. The base change
  `k(y) subset k(gamma)`, `y = gamma^{-u_s}`, is a field extension: Puiseux
  characteristic exponents are geometric and do not move under it.

**Consequence.** `M'_j = M~_j` for all `j`, where `M~` is the parent's x-side
p.150 datum. In particular `M'_{s'+1} = M~_s`, and it is computable from any
explicit pair.

### 2.3 Validation

Engine `box/child-top-us2-20260905/chardata.py` implements p.150 verbatim
(`eta = (g/lc)^{-1/n}`; rescaling `eta` by a unit of `k(base)` rescales each
`f_j` and leaves the support, hence every `M_j`, fixed). Hand control, the tame
automorphism `f = x+y^2`, `g = y+(x+y^2)^2`:

```text
   y-side  n=4  m=2  M=(-2, 1)  d=(4,2,1)      -> s=2, d_s=2, deg_x g = 2
   x-side  n'=2 m'=1 M'=(-1)    d'=(2,1)
   u_s = n' d_s / n = 2*2/4 = 1
   banked law M'_1 = M_1 u_s/d_s = -2/2 = -1   MATCHES the x-side  (non-vacuous)
   chain closes: d'_2 = 1 = u_s                MATCHES the frozen closed form
```

Reproduced by hand, by `chardata.py` (sympy, symbolic base) and by
`fastchar.py` (exact Fractions, three independent base points): identical.

**Cross-check against print.** Moh's p.207 descended table gives, for the five
`u_s = 1` rows he descends, `(n', m', M'_2) = (16,12,13), (21,14,16),
(21,14,18), (15,10,11), (15,10,11)`. Under Sec. 2.2 these say the *parent's*
x-side datum equals its y-side datum scaled by `u_s/d_s` at levels `<= s-1`.
Note for later that in all five `M'_{last} < n'-2 < n'-1`: **Moh's own printed
children never carry the terminal `n'-1` pair.**

---

## 3. The trichotomy, and where the OPEN mis-stated the alternatives

**p.150**, verbatim: `M_j = min{i : f_i(x) != 0, d_j /| i}`, `M_{h+1} = infinity`.
The chain stops when that set is **empty**. The charged OPEN reads this as "the
chain closes iff `d = 1`", and therefore concludes that at `u_s >= 2`
(`d'_{s'+1} = u_s > 1`) "at least one further characteristic pair
`M'_{s'+1} < infinity` exists". **That inference is not in the print.** The set
is empty exactly when every nonzero `f'_i(gamma)` has `u_s | i`, which is the
statement that the child's parametrisation `pi |-> (g', f')` over `k(gamma)` has
degree `u_s` rather than 1. p.150 secures degree 1 for the *parent* by an
explicit hypothesis -- "Suppose `y in k(x, f(x,y), g(x,y))`" -- and Prop 6.3
transports no such hypothesis to the child. Concretely, by Sec. 2.2 the child's
terminal gcd is `[k(y,x) : k(y,f,g)]`, i.e. **x-side birationality**, which is
not the parent's hypothesis.

So the three cases, with their effect on Def 5.1(2) at `i = s'`
(`V'_{s'+1} d'_{s'}/d'_{s'+1} >= V'_{s'}`):

| case | child datum | last effective pair | `V'_{s'+1}` | (C-TOP) `V'_{s'} <= d'_{s'}` |
|---|---|---|---|---|
| (a) | `M'_{s'+1} = infinity`, `d'_{h'+1} = u_s` | `M'_{s'}` | `= d'_{s'+1} = u_s` (Def 5.1(2) top convention) | **licensed** |
| (b) | `M'_{s'+1} = n'-1` | `M'_{s'}` (p.174 drop) | `= d'_{s'+1}` | **licensed** |
| (c) | `M'_{s'+1} < n'-1` | `M'_{s'+1}` | not forced | **NOT licensed** |

Both (a) and (b) are observed below; (b) is not.

Two supporting facts, each read off the print, that the case split relies on:

* **Prop 5.1 (p.173) applies to the child verbatim.** Its only hypothesis is
  "`g(x,y)` is monic in `y` with `y`-degree `n > 1`", and Prop 6.3(2) gives
  exactly that for `g'` in `pi`. No Jacobian hypothesis. So the p.174 drop is
  available to the child -- the charged OPEN is right about that -- and,
  combining Prop 5.1(1) and 5.1(2), uniformly
  `delta_{h} = -1/(n - M_{last effective} - 1)`. Applied to the parent this is
  the identity **`delta_s = -1 <=> M_s = n-2`**, which is how Prop 6.3's
  hypothesis `delta_s = -1` is tested numerically in Sec. 4.
* **p.201 (4)**, verbatim: "`{n, M_1,...,M_s}` is the part of characteristic
  data of `(f,g)` which are less than `n-2`". Moh states outright that the
  listed data is a *truncation*: the pair may carry characteristic exponents
  above the cut. The census's `V_{s+1} = d_{s+1}` is therefore a top-of-tower
  convention attached to that truncation, and (C-TOP) is the claim that the
  child's truncation ends at the same place. Nothing in p.201 transports it.

---

## 4. Instances: 1,199 children computed from their own expansion

Driver `scan2.py` (modular engine `modchar.py`), cross-checked exactly by
`exact2.py` (`fastchar.py`, Fractions over Q, three independent base points).
Soundness direction of the modular step is stated in `modchar.py`'s docstring: a
coefficient nonzero in `F_p` **proves** support membership, so a false zero can
only make a computed `M'` LARGER -- it can only manufacture the `n'-1` reading,
never destroy it. Every refuting instance is therefore one-sided-safe, and 8/8
representatives were re-run exactly (`exact.json`): **8/8 agree, stable over Q**.

Retained only pairs where the child reproduces every prediction Prop 6.3(2) and
Moh p.207 make about it: `n' = deg_x g`, `m' = deg_x f`, `u_s = n' d_s/n` a
positive integer `>= 2`, `M'_i = M_i u_s/d_s` for `i <= s-1`, and
`d'_{s'+1} = u_s`. Result (`scan2.json`):

| | count |
|---|---:|
| instances retained | **1,199** |
| by `u_s` | `{2: 425, 3: 407, 4: 287, 5: 80}` |
| case (c) `M'_{s'+1} < n'-1` | **1,188** |
| case (a) `M'_{s'+1} = infinity` | **11** |
| case (b) `M'_{s'+1} = n'-1` | **0** |
| with `s >= 2` (inherited-level check non-vacuous) | 10, all `u_s = 2`, **all case (c)** |
| with `delta_s = -1`, i.e. `M_s = n-2` | **0** of ~54,000 generated |

The richest retained instance, exactly verified:

```text
  f = y^3 + 3x^2 y^3 + 2x^2 y + x - 2x^2
  g = y^6 - 4xy^5 + 6x^2y^4 - 4x^3y^3 + x^4y^2 + 5x^2y^2       (= y^2(y-x)^4 + 5x^2y^2)
  y-side (Moh's own) : n = 6   m = 3   M = (-3, -2)   d = (6, 3, 1)   s = 2, d_s = 3
  x-side (the CHILD) : n' = 4  m' = 2  M' = (-2, -1)  d' = (4, 2, 1)
  u_s = n' d_s/n = 4*3/6 = 2
  banked law   M'_1 = M_1 u_s/d_s = -3*2/3 = -2      MATCHES        (NON-VACUOUS)
  closed form  d'_{s'+1} = d'_2 = 2 = u_s            MATCHES
  EXTRA PAIR   M'_{s'+1} = M'_2 = -1        n'-1 = 3        -1 != 3   -> case (c)
```

and one case-(a) instance (`f = y`, `g = y^4 - 2xy^3 + x^2y^2 + y^3`): the child
is `n' = 2`, `m' = 0`, `M' = (infinity)`, `d' = (2)` -- the chain ends at
`d'_{h'+1} = 2 = u_s`, exactly the possibility Sec. 3 says p.150 permits. 10 of
the 11 case-(a) instances have `m' = 0` (degenerate `f`); one does not, so
case (a) is not purely an artifact, but I do not lean on it.

**What these instances do and do not settle.** They settle that
`M'_{s'+1} = n'-1` is not entailed by the child's degrees, the inherited
exponents, `d'_{s'+1} = u_s`, or Prop 6.3(1)-(3): all of those hold on 1,199
counterexamples. They do **not** settle the census locus, because none carries
`delta_s = -1` (`M_s = n-2`), which is Prop 6.3's second hypothesis. Nor do they
carry `J = const`. I could not realise a census row: those rows are hypothetical
Keller counterexamples and no polynomial pair realises one, and the
generic-branch route needs a pair with `M_s = n-2`, a codimension-heavy
condition that random families in `n <= 6` never meet.

**So parts (1) and (3) of the charge are delivered only in part**: the child's
own expansion is computed at `u_s = 2, 3, 4, 5` (425/407/287/80 instances), but
NOT for the three named `u_s = 2` descent-forced census rows nor for the
`(99,66)` `u_s = 3` row; and (3) is not run, because (2) came back REFUTED.

---

## 5. Verdict, the exact extra condition, and the corrected partition

**VERDICT: REFUTED as posed.** `M'_{s'+1} = n'-1` is not forced. The mechanism
the OPEN proposed -- "the last `u_s` roots of `g'` are the descended images of
the `u_s`-fold minor root family and their mutual contact is what the terminal
pair records" -- fails at the first step: the descended minor family accounts
for the child's `pi`-roots (Prop 6.3's `pi_i = (tau_i - c(theta))/gamma^{v_s}`),
whereas `M'_j` is by p.150 the contact datum of the `n'` **conjugates of `f'`
over `g'`** at `pi = infinity`, a different configuration. Sec. 2.2 identifies
that configuration correctly, and Sec. 4 shows the resulting exponent is
generically well below `n'-1`.

`(C-TOP)` at `u_s >= 2` is therefore **still unlicensed**, and now with a
*negative* instance count rather than an absence of proof. The exact extra
condition that would be needed:

```text
EXTRA CONDITION (E).  For every pair (f,g) satisfying Prop 6.3's hypotheses
  (g monic in y, deg g = deg_y g = n > 1, delta_s = -1  [<=> M_s = n-2, Prop 5.1],
   delta*_{s-1} >= v_s/u_s)  with u_s >= 2, the x-side p.150 datum of (f,g)
  satisfies:  either  min{i : f~_i(y) != 0, u_s /| i}  is empty  (case (a)),
              or      that minimum equals  n' - 1       (case (b)).
Equivalently, in Prop 5.1's language applied to the child:
              delta'_{h'}  =  -1/(n' - M'_{s'} - 1),
  i.e. the child's finest disc radius is already fixed by the INHERITED
  exponent M'_{s'} = M_s-1 u_s/d_s and no finer disc appears.
```

`(E)` is exactly what Moh never has to state, because Prop 6.4 (p.198) restricts
him to `u_s = 1`, where `d'_{s'+1} = 1` closes the chain outright. It is not
implied by `delta_s = -1` alone in any way I can see, and Sec. 4 shows it fails
whenever `delta_s = -1` is dropped.

**Corrected partition (no ledger edit made).** Against the frozen child-data
partition (936 licensed `u_s=1` kills / 174 `u_s=1` live / 310 `u_s>=2`
unlicensed) and the frozen split-window residual of 478:

| block | rows | status after this lane |
|---|---:|---|
| `u_s = 1`, (C-TOP) fails | 936 | licensed kill (unchanged, frozen) |
| `u_s = 1`, (C-TOP) holds | 174 | live (unchanged) |
| `u_s >= 2`, 77 with typed ES leaves | 77 | live (unchanged) |
| `u_s >= 2`, descent-forced, live | **227** | **STILL LIVE** -- (C-TOP) refuted as posed, `OPEN[CTOP-EXTRA-CONDITION-E]` |

Operative residual **unchanged at 478**. The counterfactual (`ctop310.py`,
`ctop310.json`) is recorded for completeness only: were `(E)` proved, (C-TOP)
would kill **225 of the 310** operative `u_s >= 2` rows and **196 of the 233**
descent-forced ones, leaving 85 + 37 respectively. That number is **not**
charged and must not be quoted as a kill.

---

## 6. FALLACY-v2 ledger

| clause | where it bit |
|---|---|
| Floor/attainment | Sec. 4's 1,199 instances are a *refutation* of universality, never a proof that case (c) always holds; the census locus is explicitly excluded in Sec. 0(D) and Sec. 4. |
| Carrier/attainment | Moh's p.207 five rows are a printed control on the transformation law at `u_s = 1`, never the general theorem; the `u_s >= 2` law is derived in Sec. 2.2, not extrapolated from them. |
| Prime label/derivative | `M'`, `d'`, `V'`, `s'`, `delta'` are descended-datum labels; `M~`, `d~` are x-side labels of the PARENT. Sec. 2.2 proves the two coincide -- they are not assumed equal by notation. No derivative is meant anywhere. |
| Variable/ring map | Sec. 2.2 declares the map explicitly (`pi <-> y`, `gamma <-> x`), fixes generator order and base field (`k(gamma) contains k(y)`, `y = gamma^{-u_s}`), and checks the images: `deg_pi g' = n' = deg_x g` and `deg_pi f' = m' = deg_x f`, both against Prop 6.3(2). Matching names prove nothing, so each of the four moves (scale, translate, `T_1^psi`, base change) is separately argued not to move an `M_j`. |
| Target/arrival index | `s` (parent, last effective), `s'` (child inherited depth `= s-1`) and `h'` (child's raw last index) are kept distinct throughout; the trichotomy is stated in terms of `h'` vs `s'`. |
| Merge-free / M-descent | Sec. 3 is precisely the refusal to assume a merge-free child top; the "existence of `M'_{s'+1} < infinity`" step is where the charged OPEN merged. |
| Pole/interior | Prop 5.1 is used only after checking its single hypothesis (`g'` monic in `pi`, degree `> 1`) against Prop 6.3(2); its `delta_s = -1 <=> M_s = n-2` corollary is derived from BOTH conclusions (1) and (2), not one branch. |
| positive/negative controls | Positive: the hand-computed automorphism control reproduced by three independent engines (Sec. 2.3), and the banked law verified non-vacuously on 10 `s >= 2` instances. Negative: 0 case-(b) instances out of 1,199; specialisation-instability discarded (3 base points / 3 primes must agree). One-sidedness of the modular test argued in Sec. 4. |
| `sat()`, raw remainder degree | No Groebner run in this lane; `k killed inline = 0`. |

Correction to an earlier campaign statement, stated once: the frozen child-data
report's `OPEN[CHILD-TOP-AT-US-GE-2]` asserts "`d'_{s'+1} = u_s > 1`, so at
least one further characteristic pair `M'_{s'+1} < infinity` exists". p.150 does
not support that implication (Sec. 3); the correct reading is the trichotomy.
The frozen report's conclusions at `u_s = 1` are untouched -- there
`d'_{s'+1} = 1` and `M'_{s'+1} = infinity` unconditionally.

---

## OPENS RAISED

```text
OPEN[CTOP-EXTRA-CONDITION-E]
  QUANTITY: condition (E) of Sec. 5 -- for pairs meeting Prop 6.3's hypotheses
    with u_s >= 2, the child's extra characteristic pair is either infinity or
    exactly n'-1; equivalently delta'_{h'} = -1/(n' - M'_{s'} - 1).
  STATUS: REFUTED without the hypothesis delta_s = -1 (1,199 instances, 0 in
    case (b)).  UNDECIDED with it: no instance carrying M_s = n-2 and u_s >= 2
    was realised in this lane.
  CHEAPEST TEST: realise ONE pair with deg g = deg_y g = n, M_s = n-2, d_s >= 5
    and u_s = 2 -- the smallest shape is n=10, m=5, M=(-5,8), d=(10,5,1),
    child (4,2) with M'_1 = -2 and M'_2 in {-1,1,3}; then read M'_2 off the
    x-side.  A one-place-at-infinity / approximate-root construction, not a
    random search (0 of ~54,000 random pairs met M_s = n-2).
  BLAST RADIUS: 227 live descent-forced rows; decides 225 of the 310 operative
    u_s >= 2 rows and whether the residual is 478 or 253.

OPEN[CHILD-XSIDE-BIRATIONALITY]
  QUANTITY: is the child's parametrisation pi |-> (g',f') over k(gamma)
    birational, i.e. does the child's chain reach d = 1?
  STATUS: by Sec. 2.2 this is x in k(y,f,g), the x-side analogue of p.150's
    stated hypothesis "y in k(x,f,g)".  Moh states the y-side one and never the
    x-side one.  11 of 1,199 instances fail it (case (a)); 10 of those are
    degenerate (m' = deg_x f = 0), one is not.
  CHEAPEST TEST: for a Keller pair, u_s | deg(f,g) is forced by
    [k(x,y):k(f,g)] = u_s [k(y,f,g):k(f,g)]; check whether the census's
    admissible degrees permit u_s | deg Phi.
  BLAST RADIUS: case (a) LICENSES (C-TOP) just as case (b) does, so a proof
    here in the affirmative direction (chain does NOT close) would recover the
    225 kills by a different route than (E).
```

<!-- BODY-END -->
