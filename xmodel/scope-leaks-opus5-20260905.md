# SCOPE leaks (ii) U-NEGATIVE and (iii) s'>2 DEPTH — enumerated, typed, routed

Lane `scope-leaks-opus5-20260905`; adapter opus. Drivers
`box/scopeleaks-20260905/`. Frozen inputs under `/tmp/jc2-lane.TfnlJh/inputs`.

## 0. Verdict first

```text
HEADLINE: leak (ii) U-NEGATIVE is NOT a third configuration.  It is a
DEGENERATE descended datum: V'_2 > K' = gcd(n',m') asks a degree-K' form to
carry multiplicity V'_2 > K'.  Family (a) CLOSED-conditionally (one named
licence).  Family (b) s'>=3 is CHARACTERIZED, not closed: Phi_eff already
emits the receiver at every height -- it does NOT need to iterate -- the
wall is compute; a second DESCENT is licensed by Moh only on 31/1420 rows.

(a) U-NEGATIVE, 16<=n<=200:  2,999 of 24,063 (1)-(13) census rows;
    90 of the 1,420 operative (C_FULL_TREE_POLYNOMIAL_ODE) rows.
    - ZERO of them are s'=2.  The classical Appendix-II shape never meets
      the leak; all 90 sit inside the s'>=3 family (leaks (ii) c (iii)).
    - 84/90 have u_s=1 => Prop 6.4 (p.198, read) discharges Prop 6.3's
      radius hypothesis => the descent is FORCED => the datum is
      contradictory => the skeleton is EMPTY.
    - 6/90 have u_s=2 => Prop 6.3 radius dichotomy: 2 have an EMPTY split
      window {delta in (1,v_s/u_s) : den <= u_s} => (R) forced => same kill;
      4 leave exactly one candidate radius delta*=3/2 to exclude.
    - No SECOND descent is needed and none is available: delta'_{s'} != -1
      on 90/90.  Astra's avenue 5 is not the route for this family.

(b) s'>=3 DEPTH, 16<=n<=200: 1,353 of 1,420 operative rows (95.3%);
    by height s' = 3:426, 4:791, 5:136.  s'=2 (Appendix II) is 67 rows.
    - Phi_eff is a SINGLE-STEP closed form in s'; it emits an s'=4 and an
      s'=5 receiver as readily as s'=3.  "Does Phi_eff iterate?" is the
      wrong question: it does not have to.
    - A second Prop 6.3 descent needs delta'_{s'} = -1 on the child: true
      on 157/1420; of those only 31 also have ell=0, i.e. are Moh's own
      Cor 6.1 (p.199) genuine smaller Keller pairs.  The other 126 need
      the monomial-Jacobian category to be closed under descent (avenue 5,
      unproved).
    - Priced with the charged inventories: 1,026 chartable u_s=1 receivers,
      unknown-count quantiles (s'>=3) 78 / 149 / 221 / 405 / 906 / 1636 /
      4952.  The cheapest s'>=3 chart in the whole residual is 78 unknowns
      and is exactly the class the s'=3 compiler already failed to kill.

KILLED INLINE by Groebner: 0.  Nothing in the residual is a <20 min std.
The kills claimed here are STRUCTURAL (degenerate descended datum), with
their single licence named in Sec. 3.3 and typed OPEN.
```

No new exit-price assertion is made, so no `charge_basis` line is licensed.

---

## 1. Frozen-input gate

Manifest built with `awk` from the `charged_input_<i>_basename=` /
`charged_input_<i>_sha256=` lines of
`xmodel/scope-leaks-opus5-20260905.run.v2`, checked with `sha256sum -c`:
**8/8 `OK`**, no digest retyped. Banked at
`box/scopeleaks-20260905/inputs.sha256`.

Workspace `box/moh_skeleton_full.py` and
`box/centre-gate-20260903/moh_skeleton_full_frozen.py` are both byte-identical
to the charged copy (`d20bf084…c506c2`), so the enumerator used by every
driver below is the frozen one.

Page images read at 200–300 dpi (the pdftotext layer drops the display math on
all four): **p.190** (`box/centre-gate-20260903/moh_p190.png`), **p.197**,
**p.198** (`box/prop63gate-20260905/`), **p.207** (ibid.), and **p.208**
rendered here from the charged PDF
(`box/scopeleaks-20260905/moh_p208-69.png`, pdf page 69).

---

## 2. What was enumerated, and against what screens

`box/scopeleaks-20260905/scope_enum.py`, `depth.py`, `uneg.py`, `sizes.py`,
`controls.py`. Two populations, both over `16 <= n <= 200`, `Kmin=2` (Moh's
own space, not the 17(ll) `Kmin=16` slice):

| population | rows |
|---|---:|
| Moh `(1)–(13)` census | **24,063** |
| PROMOTED operative screen `C_FULL_TREE_POLYNOMIAL_ODE` (17(r)/(hh)/(ll)) | **1,420** |

The operative count, its `u_s` histogram `{1:1110, 2:265, 3:34, 4:9, 5:2}` and
its 70 degree pairs reproduce the banked 17(ll) figure exactly — and they do so
from `Kmin=2, n>=16`, which independently shows the `Kmin=16, n>=48` convention
loses nothing at `n <= 200`.

Descent, per row (banked closed form, validated 5/5 against Moh p.207 by
`box/moh14-20260905/descend14.py` and re-validated here in CONTROL P):

```text
u_s = d_s - V_s,  v_s = V_s,  ell = v_s - u_s - 1
(n',m') = (n u_s/d_s, m u_s/d_s),  M'_i = M_i u_s/d_s (i=1..s-1),
V'_i = V_i,  s' = s-1,  d'_r = u_s d_r/d_s,  d'_{s'+1} = u_s,
K' = d'_2 = gcd(n',m'),  u' = K' - V'_2,
delta'_i = (ell+1) * Def 5.1(3)(n',M',d',V',s',i)      [Phi_eff]
```

with Moh's p.174 drop of a terminal `M'_h = n'-1` applied before `Phi_eff`
(90 of the 1,420 operative rows drop exactly one level; without the drop
`delta'` is a 1/0 division on those).

`delta_s = -1` holds on all 24,063 census rows, so Prop 6.3's first hypothesis
is never the obstruction.

---

## 3. Family (a): U-NEGATIVE

### 3.1 The enumeration

`U-NEGATIVE` is `V'_2 > d'_2`, i.e. `u' = K' - V'_2 < 0`
(`box/appendix2-k16-20260903/shape.py:146`, the `reason="U-NEGATIVE"` early
return). Arithmetically it is `V_2/d_2 > u_s/d_s`.

| slice | census | operative |
|---|---:|---:|
| `u' < 0` (U-NEGATIVE) | 2,999 | **90** |
| `u' = 0` | 117 | 2 |
| `u' > 0` | 20,947 | 1,328 |

Operative U-NEGATIVE, cross-tabbed (`uneg.log`):

```text
by u_s : {1: 84, 2: 6}          by s' : {3: 9, 4: 63, 5: 18}   (s'=2: ZERO)
by ell : {0:2, 1:61, 2:15, 3:6, 5:3, 6:2, 7:1}
delta'_2 == -1 : 1 of 90        delta'_{s'} == -1 : 0 of 90
V'_2/K' ranges over 17/16 .. 4  (one row wants multiplicity 4K')
16 degree pairs: (108,72) (120,72) (128,96) (144,96) (144,108) (160,64)
(160,120) (160,128) (162,108) (180,120) (192,128) (192,144) (192,160)
(200,80) (200,120) (200,160)
```

Two facts settle the shape of the leak before any theory:

1. **No operative U-NEGATIVE row has `s'=2`.** All 600 census `s'=2`
   U-NEGATIVE rows die under the promoted whole-tree screen. So leak (ii)
   never touches the covered Appendix-II shape; it is a strict sub-family of
   leak (iii).
2. **No U-NEGATIVE row has `delta'_{s'} = -1`**, so a second Prop 6.3 descent
   is unavailable for every one of them. Avenue 5 ("closure of the marked
   monomial-Jacobian category under a second descent") is *not* the route for
   this family, whatever its status elsewhere.

### 3.2 What Moh's theory says — is `V'_2 > d'_2` genuine?

It is not excluded by conditions (1)–(13) on the **parent**: p.201 (7) is
`V_{r+1}(d_r/d_{r+1}) >= V_r > d_r/(n-M_r)`, and p.190 shows why the left half
holds — it is not a search condition but the identity

> `deg p(pi) = V_{r+1} d_r/d_{r+1} >= V_r > d_r/(n - M_r)`
> — Moh 1983 p.190, §6 opening, with `(pi - C_r)` a factor of `p(pi)` of
> multiplicity `V_r`

i.e. *multiplicity <= degree*. Downward induction from the top convention
`V_{s+1} = d_{s+1}` gives `V_2 <= d_2 = gcd(n,m)` for the parent, which every
census row satisfies by construction. **`V_2 <= u_s d_2/d_s` is strictly
stronger and is nowhere imposed on the parent.** So U-NEGATIVE rows are
genuinely present in Moh's own search space — as the audit's leak (ii) said.

The exclusion is on the **child**. Moh's own two tables settle the descended
datum: p.202 (parent skeletons) -> p.207 (Appendix II descended table) is,
column for column,

| parent p.202 `(n,m); M_2,M_3; V_2,V_3` | `d_s` | `u_s` | child p.207 `(n',m'); M'_2; V'_2` |
|---|---:|---:|---|
| `(64,48); 52,62; V_2=3, V_3=3` | 4 | 1 | `(16,12); 13; 3` |
| `(84,56); 64,82; V_2=2, V_3=3` | 4 | 1 | `(21,14); 16; 2` |
| `(84,56); 72,82; V_2=5, V_3=3` | 4 | 1 | `(21,14); 18; 5` |
| `(75,50); 55,73; V_2=3, V_3=4` | 5 | 1 | `(15,10); 11; 3` |
| `(75,50); 55,73; V_2=2, V_3=4` | 5 | 1 | `(15,10); 11; 2` |

`M'_2 = M_2 u_s/d_s` and **`V'_2 = V_2` unchanged** — Moh writes the parent's
`V_2` as the child's `V_2`. Then on p.208, for the first of those rows, he
writes the descended approximate root explicitly:

> `h(x,y) = y^3(y-x) + b_1 y^3 + b_2 y^2 + b_3 y + b_4`,
> `h(y) =` the fourth approximate root of `f-bar(y)` — Moh 1983 p.208 (1)

`deg h = 4 = gcd(16,12) = K'` and its leading form is `y^{V'_2}(y-x)^{u'}` with
`V'_2 = 3`, `u' = 1`. So on the child, `V'_2` is a **multiplicity inside a form
of degree `K'`**, and `u' = K' - V'_2 >= 0` is forced.

**Conclusion.** When the Prop 6.3 descent applies, `V_2 > gcd(n',m')` is
contradictory: the descended datum assigns the level-2 disc more branches than
the descended approximate root has. The skeleton is EMPTY — a kill, not a
configuration.

`u_s = 1` makes "the descent applies" unconditional. Moh p.198, read from the
image:

> **Proposition 6.4.** Suppose that `g(x,y)` is monic in `y` with
> `deg g = deg_y g = n > 1`, `delta_s = -1` and **`u_s = 1`**. Then the
> logarithmic radius `delta*_{s-1}` of the minor disc `D*_{s-1} >= v_s/u_s = v_s`.

That is exactly Prop 6.3's hypothesis. **84 of the 90 operative U-NEGATIVE rows
are killed with no further input.**

### 3.3 The single licence, typed

The load-bearing hypothesis is *not* `V'_2 = V_2` (that is Moh's own
p.202->p.207 transformation, 5/5 columns, re-checked in CONTROL P) and *not*
`d'_2 = gcd(n',m')` (arithmetic from Prop 6.3(2) p.197 and (5)). It is:

```text
OPEN[UNEG-SHAPE-LICENCE]  (typed, not filled)
  "V'_2 is a multiplicity among the K' = gcd(n',m') branches of the descended
   approximate root h', hence u' = K' - V'_2 >= 0."
  Status: charged campaign convention (box/appendix2-k16-20260903/shape.py
  docstring, 'PROVED-HERE as the unique D1 bound reproducing Moh pp.208,
  210-211'); printed by Moh at p.208(1) for the (16,12) child; Lemma 5.3's
  two-point leading form is licensed only at delta'_2 = -1, which holds on
  1 of the 90 rows.
  Cheapest test (minutes-to-hours, NOT run here): derive deg_x h' for the
  descended pair from Prop 6.2 / Theorem 1.2 directly, or exhibit one
  descended pair with V'_2 > gcd(n',m').
```

Two independent controls that the reading does not over-kill
(`controls.log`, both pass):

* **CONTROL P** — Moh's own six p.202 rows: the five with `u_s = 1` all give
  `u' >= 0` (1, 5, 2, 2, 3); `(99,66)` has `u_s = 3` and Prop 6.4 does not
  apply, exactly as Moh skips it on p.207.
* **CONTROL Q** — every operative row at `n <= 100`: `{u'>0: 18, u'=0: 1,
  u_s>=2: 1}`; **no `u' < 0`**. The moh100 residue and Moh's six printed rows
  are untouched by this kill.

### 3.4 The 6 rows with `u_s >= 2`: the radius dichotomy

At `u_s >= 2` Prop 6.4 is silent and Prop 6.3's `delta*_{s-1} >= v_s/u_s` is a
hypothesis. The banked dichotomy (17, `prop63-radius-dichotomy`, re-derived
from the p.199 proof) says: either `(R)` holds — and then §3.2 kills the row —
or the minor cluster splits at some `delta* in (1, v_s/u_s)` with
`den(delta*) <= u_s`. That window is a finite list:

| row (n,m; M; V) | `d_s` | `u_s` | `v_s` | window |
|---|---:|---:|---:|---|
| `160,120; (-100,-50,55,158); V_2=23` | 5 | 2 | 3 | **empty** |
| `200,80; (-60,-10,95,198); V_2=18` | 5 | 2 | 3 | **empty** |
| `192,144; (-120,-12,18,190); V_2=23` | 6 | 2 | 4 | `{3/2}` |
| `192,144; (-72,12,78,190); V_2=22` | 6 | 2 | 4 | `{3/2}` |
| `192,144; (-72,12,78,190); V_2=31` | 6 | 2 | 4 | `{3/2}` |
| `192,144; (-24,132,174,190); V_2=23` | 6 | 2 | 4 | `{3/2}` |

Empty window ⟹ `(R)` is forced ⟹ §3.2 applies. **86 of 90 are unconditional**
(modulo `OPEN[UNEG-SHAPE-LICENCE]`); the residue of family (a) is **four rows
at `(192,144)` needing the single radius `delta* = 3/2` excluded** by the
split-face screen (G)+(L). That is a minutes-scale desk test on a banked
instrument; it was not run here for time and is typed
`OPEN[UNEG-192-144-SPLIT-3/2]`.

### 3.5 What I deliberately did NOT promote

The same child-tower reading, pushed to the child's *top* level, gives

```text
(C-TOP)   V_{s-1} <= u_s d_{s-1}/d_s   ( = d'_{s'} )
```

— exactly the `V'_{s'} <= d'_{s'}` you get from the p.190 display plus the top
convention `V'_{s'+1} = d'_{s'+1} = u_s`. It is a **strictly stronger** screen
and it is spectacular: it fails on 20,518 of 24,063 census rows and on
**1,195 of the 1,420 operative rows** (970 of them `u_s = 1`), leaving 225
operative survivors in 58 degree pairs. U-NEGATIVE is a corollary of it
(`U-NEG & C-TOP = 0` on all 24,063 rows, as the parent chain
`V_2 <= V_{s-1} d_2/d_{s-1}` predicts).

**It is not promoted, and it should not be used.** The parent's top convention
`V_{s+1} = d_{s+1}` is licensed by p.190 — "the minimal disc `D_s` which
contains all roots of `g(y) prod T_i^psi(y)` is a tower of one major disc" —
together with `M_s = n-2` / `delta_s = -1`. The child has **neither**:
`M'_{s'} = n'-2` on 31 of 1,420 rows and `delta'_{s'} = -1` on 157 of 1,420, so
the child's own tower may extend above `M'_{s'}` and `deg p'(pi)` at level `s'`
is then not `d'_{s'}`. Moh's p.207 table does **not** test the convention
either: at `s'=2` the value `V'_3` never enters `Def 5.1(3)`. Promoting
(C-TOP) would kill 6 of the 12 charged `moh100` receiver rows and the
compiler's `u'=0` row — a claim with no source.

```text
OPEN[CHILD-TOP-CONVENTION]  (typed)
  Is V'_{s'+1} = d'_{s'+1} legitimate for the descended pair, i.e. is
  D'_{s'} the minimal disc containing all roots of the descended pair?
  If YES, 1,195/1,420 operative rows die at once and the (H1)&(H2) residual
  at n<=200 collapses to 225 rows / 58 degree pairs.
  Cheapest test: compute the child's own characteristic data for ONE row
  where delta'_{s'} != -1 (e.g. parent (96,72) M=(36,78,94) V=(4,3,5),
  child (16,12) M'=(-12,6,13), V'_3=3 vs d'_3=2) and check whether its
  tower closes at M'_{s'} or continues to n'-2.
  Distinct from the compiler's OPEN[CHILD-SEARCH-CONDITIONS] (which is
  about (10)/(11)/(12)/(13)); this one is about (7)'s LEFT half only.
```

---

## 4. Family (b): the `s' >= 3` DEPTH residual

### 4.1 The enumeration, by height

Operative residue by descended height (after the p.174 drop) —
`depth.log`:

| `s'` | rows | share |
|---:|---:|---:|
| 2 (Moh Appendix II) | 67 | 4.7% |
| 3 | 426 | 30.0% |
| 4 | 791 | 55.7% |
| 5 | 136 | 9.6% |

`s' >= 3`: **1,353 rows**, 48 degree pairs, 96 distinct `(n',m',ell)`;
`s' >= 4`: 927 rows. By `(s', u_s)`:
`{(3,1):330, (3,2):74, (3,3):14, (3,4):7, (3,5):1, (4,1):596, (4,2):181,
(4,3):14, (5,1):136}`. By `ell`:
`{0:142, 1:739, 2:329, 3:82, 4:11, 5:37, 6:7, 7:6}` — the residual is
overwhelmingly `ell in {1,2}`, confirming 17 `us1-rows-dominate-operative-residue`
at the full `n<=200` scale.

The `n<=100` residue (moh100's 12–14 rows) is the small-`n` shadow of this: at
`n<=100` there are only 20 operative rows in total.

### 4.2 Does `Phi_eff` iterate? — the question does not arise

`Phi_eff` is `delta'_i = (ell+1) * Def 5.1(3)(n',M',d',V',s',i)`. `Def 5.1(3)`
takes the tower height `s'` as a parameter; there is nothing in the formula
that is special to `s'=2` or `s'=3`. The charged compiler already emits an
`s'=4` class (`C_n24m16_Mm12_m2_5_ell1_s4`), and `sizes.py` here evaluates the
same charged pipeline (`descend_once` -> `drop_p174` -> `phi_eff` ->
`closed_form_sprime` -> `h_inventory_necessary` / `coeff_inventory_necessary`)
on all 1,110 operative `u_s=1` rows including the `s'=5` ones, without
modification. **`Phi_eff` does not need to iterate and no new chart type is
needed at `s'>=4`.** What is needed is compute.

Pricing (unknown counts after the charged translation gauges, `B_safe`
threshold, necessary inventories — no sub-slice):

| population | rows | unknown-count quantiles (min/10/25/50/75/90/max) |
|---|---:|---|
| `u_s=1`, `s'>=3`, chartable | 978 | 78 / 149 / 221 / 405 / 906 / 1636 / **4952** |
| `u_s=1`, `s'=2` | 48 | cheapest six: 44, 54, 64, 66, 72, 72 |

The cheapest `s'>=3` chart in the entire `n<=200` residual is **78 unknowns**,
`(n',m') = (24,16)`, `s'=4`, `ell=1`, parent `(96,64) M=(-48,-8,20,94)
V=(1,1,6,3)` — which is precisely the class the s'=3 compiler emitted as
`C_n24m16_Mm12_m2_5_ell1_s4` (77 unknowns after gauges, 425 generators, 97 MB
of extracted rows) and could **not** kill. The median is 405 unknowns. So:
there is no cheap kill anywhere in family (b) at `n <= 200`, and this lane
produces none — reported as a negative, not papered over.

### 4.3 Is a SECOND descent available? (avenue 5, priced)

Prop 6.3's input hypothesis is `delta_s = -1`. On the child,
`delta'_{s'} = -(ell+1)/(n' - M'_{s'} - 1)`, so `delta'_{s'} = -1` iff
`M'_{s'} = n' - ell - 2`. Measured over the 1,420 operative rows:

| condition | rows |
|---|---:|
| `delta'_{s'} = -1` (Prop 6.3's first hypothesis on the child) | **157** |
| `ell = 0` (child is a genuine Keller pair, `J = c`) | 142 |
| `ell = 0` **and** `M'_{s'} = n'-2` — Moh's own **Cor 6.1** (p.199) | **31** |
| `delta'_{s'} = -1` but `ell >= 1` (needs avenue 5) | 126 |

The 157 include Moh's own `(64,48)`, `(75,50)`, `(84,56) V_2=5`, `(99,66)` and
`(108,72)`. So:

* A second descent **as printed mathematics** (Cor 6.1, `d_s = 3`, `ell = 0`,
  smaller Keller pair) is available on **31 of 1,420** rows — 2.2%. Those, and
  only those, route to a strictly smaller instance of the same problem.
* On 126 further rows the radius hypothesis is met but `ell >= 1`, so the child
  is a *monomial*-Jacobian pair; iterating needs Astra's avenue 5 (closure of
  the marked monomial-Jacobian category under a second descent). Unproved; it
  would buy at most 126/1,420 = 8.9% even if proved.
* On the remaining 1,263 rows `delta'_{s'} != -1` and no second descent exists
  at all, avenue 5 or not.

**So the depth residual is not reachable by iterating the descent.** Any route
for family (b) has to go through the `s'>=3` receiver itself.

---

## 5. Kills

Attempted and honest:

* **Structural (Sec. 3):** 84 operative rows (`u_s=1`, U-NEGATIVE) plus 2
  (`u_s=2`, empty split window) = **86 rows across 16 degree pairs**, killed
  by the degenerate descended datum, conditional on
  `OPEN[UNEG-SHAPE-LICENCE]` alone. On the `(1)–(13)` census (Moh's full
  space) the same argument reaches 2,346 `u_s=1` U-NEGATIVE rows.
* **Groebner:** none run to a marker. The cheapest chart in either residual
  family is the 78-unknown `(24,16)` `s'=4` class whose extraction is 97 MB and
  which the charged compiler already left unkilled at 180 s; nothing in the
  lane budget changes that. `k killed inline = 0`. No `UNIT_IDEAL`, no
  `POSDIM`, no new exit price.
* **Not attempted:** the fleet. With no chart under ~78 unknowns there was no
  job whose success probability justified the dispatch inside 150 min.

---

## 6. The exact residual scope obligation

Partition of all 1,420 operative rows, `16 <= n <= 200` (`controls.log`,
totals check `1420`):

| class | rows | status |
|---|---:|---|
| **A** `u_s=1`, U-NEGATIVE | 84 | **KILLED** (Sec. 3.2/3.3), one named licence |
| **B** `u_s>=2`, U-NEGATIVE | 6 | 2 killed; 4 need `delta*=3/2` excluded at `(192,144)` |
| **C** `u_s=1`, `s'>=3`, chartable | 978 | receiver EMITTABLE by `Phi_eff`; **compute-bound** |
| **D** `u_s=1`, `s'=2` | 48 | covered — Moh Appendix II shape |
| **E** `u_s>=2`, not U-NEGATIVE | 304 | radius dichotomy first: split-or-descend, unresolved |

Read against the audit's four leaks:

* leak (ii) **U-NEGATIVE — CLOSED conditionally.** Not a third configuration;
  a degenerate descended datum. Residue: `OPEN[UNEG-SHAPE-LICENCE]` (one
  statement) + 4 rows at `(192,144)`.
* leak (iii) **`s'>2` DEPTH — CHARACTERIZED.** Exact rows: class C above,
  978 chartable `u_s=1` rows (plus the `u_s>=2` part of E once its dichotomy
  is resolved). Missing instrument is **not** an iterated `Phi_eff` — it is
  a Groebner engine that finishes a 78–5,000-unknown exact-`Q` `std`. Naming
  it correctly matters: "s'>=4 needs an iterated `Phi_eff`" would have been
  the wrong obligation.
* leak (iv) **routing maps** — class E (304 rows) is where it bites; not this
  lane's charge, but the U-NEGATIVE dichotomy (Sec. 3.4) is the template: the
  radius window is finite and enumerable per row.

---

## 7. FALLACY-v2 ledger

| clause | where it bit |
|---|---|
| Floor/attainment | `B_safe = V'_2 delta'_1 + u' delta'_{s'}` used throughout `sizes.py` (the charged compiler's own function); `B_tight` never used. At `u' < 0` `B_safe` moves the threshold the *wrong* way (shrinks the inventory), which is an independent signal that a U-NEGATIVE row has no honest chart, and is why no U-NEGATIVE chart was emitted. |
| Prime label/derivative | every prime mark here is a descended-datum label; `delta'`, `V'`, `M'`, `s'` are never derivatives. |
| Target/arrival index | the child's top index `s' = s-1` is kept strictly distinct from the parent's `s`; the whole of Sec. 3.5 is about refusing to import the parent's top convention into the child's arrival index. |
| Carrier/attainment | Moh p.208(1) is one printed *instance* of the descended leading form, not a general theorem; it is cited as evidence for `OPEN[UNEG-SHAPE-LICENCE]`, never as its proof. |
| Merge-free / M-descent | (C-TOP) is exactly a "regular step that changes the top datum"; not promoted (Sec. 3.5). |
| Pole/interior | `Phi_eff`'s `Def 5.1(3)` denominators are guarded (`def51` returns `None`); the p.174 terminal-`M'_h = n'-1` drop is applied before evaluation, not after. |
| positive/negative controls | CONTROL P (Moh's 5 descended rows) and CONTROL Q (all 20 operative rows at `n<=100`) both confirm the U-NEGATIVE reading kills nothing Moh or the campaign has charted. |

Corrections to earlier campaign statements, stated once:

* 17(qqqqq)(5)/(eeeeee) call U-NEGATIVE "a genuine THIRD configuration". On the
  evidence here it is not a configuration at all — it is an inconsistent
  descended datum — and it is contained in leak (iii), not parallel to it.
* Prop 6.3's `delta*_{s-1} >= v_s/u_s` is printed with `v_s/u_s`, and Prop 6.4
  (p.198) discharges it *only* at `u_s = 1`, stating the bound as
  `>= v_s/u_s = v_s`. Both read from the images, not the text layer.

---

## OPENS RAISED

```text
OPEN[UNEG-SHAPE-LICENCE]
  QUANTITY: u' = gcd(n',m') - V'_2 >= 0 for every descended pair.
  STATUS: charged convention + one printed instance (Moh p.208(1)).
  CHEAPEST TEST: derive deg_x h' from Prop 6.2 / Theorem 1.2 on the
  descended pair, at one row with delta'_2 != -1.
  BLOCKS: 86 of the 90 operative U-NEGATIVE kills, and 2,346 census rows.

OPEN[CHILD-TOP-CONVENTION]
  QUANTITY: V'_{s'+1} = d'_{s'+1} for the descended tower, equivalently
  deg p'(pi) = d'_{s'} at the child's top level.
  STATUS: assumed by the charged descend()/shape.py; untested by Moh p.207
  (V'_3 does not enter Def 5.1(3) at s'=2); refused here.
  CHEAPEST TEST: compute the child's own characteristic data for parent
  (96,72) M=(36,78,94) V=(4,3,5) -> child (16,12) M'=(-12,6,13), and see
  whether the tower closes at M'_{s'}=13 or continues to n'-2=14.
  PRIZE: 1,195 of 1,420 operative rows at n<=200 (residual -> 225 rows /
  58 degree pairs).

OPEN[UNEG-192-144-SPLIT-3/2]
  QUANTITY: exclusion of delta* = 3/2 for the four u_s=2 U-NEGATIVE rows at
  (192,144) (M=(-120,-12,18,190) V_2=23; M=(-72,12,78,190) V_2=22 and 31;
  M=(-24,132,174,190) V_2=23).
  CHEAPEST TEST: the banked split-face screen (G)+(L), minutes.

OPEN[DEPTH-ENGINE]
  QUANTITY: an exact-Q std that finishes a 78-unknown / 425-generator
  s'=4 receiver.  This, not an iterated Phi_eff, is the missing instrument
  for the 978-row s'>=3 residual.  Median chart is 405 unknowns.
```

---

## 8. Artifacts

```text
box/scopeleaks-20260905/
  inputs.sha256          8/8 charged inputs, verified with sha256sum -c
  artifacts.sha256       driver + JSON digests
  scope_enum.py/.log/.json   census + operative enumeration, U-NEG and u'=0 slices
  depth.py/.log/.json        heights after the p.174 drop, second-descent census
  uneg.py/.log/.json         the 90 operative U-NEGATIVE rows + split windows
  sizes.py/.log/.json        chart pricing with the charged inventories
  ctop.py/.log/.json         the (C-TOP) measurement -- NOT promoted (Sec. 3.5)
  controls.py/.log           CONTROL P, CONTROL Q, residual partition
  moh_p208-69.png            rendered here (200 dpi) from the charged PDF
```

Replay: `python3 box/scopeleaks-20260905/<driver>.py 16 200` from the repo
root (all drivers use absolute paths and the frozen enumerator; total wall
under 2 minutes each).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `24429`.
- Body SHA-256:
  `cc0a4230ad43be3afdbe0d671a9f3e38f63c50e97c60b1347f1fd6f5d48bfa7d`.
- Frozen basis: `e079aa59cb7c7c9f8af02de76aaeff5d9a86af43`.
