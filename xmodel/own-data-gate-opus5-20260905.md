# HOSTILE GATE on Astra's `child-own-v` — the 1,355-row emptiness claim

Lane `own-data-gate-opus5-20260905`; adapter opus. Notes and drivers in
`box/own-data-gate-20260905/`. Frozen basis `b1966334d0a6f0c2f6a5f77e56c3be467de617ea`.

## 0. Verdict first

```text
VERDICT: CONFIRMED-WITH-FIX.

  The partition is right in structure and almost right in count.  Every
  emptiness step but ONE is backed by a line I read off the charged PDF, and
  I reproduce Astra's numbers with independent code written from the print.

  THE OVER-STRICT STEP.  own_v_routes.py:66,74
      if z>0 and P==Q*z: continue     # "PropA.3 resonance exclusion"
      if      P==Q*r  : continue
  Since P = V_{j+1} d_j/d_{j+1} and Q = V_{j+1}(n-M_j)/d_{j+1}, the predicate
  `P == Q*mult` is exactly `mult = d_j/(n-M_j)`.  The printed line it is meant
  to implement is Prop 4.6(5) p.170, "p(pi) is not a power of q(pi)".  That
  forbids p = q^w, which needs ALL multiplicities equal to P/Q AND
  #distinct-roots(p) = deg q.  A SINGLE factor of multiplicity P/Q is not
  excluded by the print.  The filter as coded is necessary-not-sufficient
  turned into a kill.

  CORRECTED COUNTS:   1,354 empty  /  66 singleton  (46 at u=1, 20 at u>1).
  Delta: exactly ONE row moves from "empty" to "singleton",
      source (168,112), M=(-112,140,160,166), V=(3,21,3), u_s=1
      -> child (42,28), M'=(-28,35,40), OWN V'=(3,7)   (copied V was (3,21)).
  Its level-2 witness is p = xi^2 (xi^10-c_1)^3 (xi^10-c_2)^1: P=42, Q=21,
  21 distinct roots = deg q, multiplicities {2,3,1} NOT all equal, so
  p != q^w and Prop 4.6(5) is satisfied.  Nothing else changes: relaxing the
  filter creates no new set-valued row and does not widen any of the 65.

  EVERYTHING ELSE HOLDS.  The 1,354 are genuine contradictions among necessary
  conditions, each traced to a printed line (table in Sec. 4).  The operative
  residual at n <= 200 is 66 necessary rows, not 65 and not 1,420.

  NOT REFUTED.  I could not exhibit a row whose empty set is nonempty by my
  computation, and I could not manufacture one: the margins are enormous
  (typical failure is b*V = 3255 > P = 36, Sec. 3.2).

  SCOPE, stated up front.  This is a residual of NECESSARY TOWER
  CONFIGURATIONS, not of pairs, and it is conditional on the reduced-source
  hypothesis printed on p.200 ((1) deg f = deg_y f = m < deg g = deg_y g = n,
  (2) m /| n and M_s = n-2, (3) J = 1 and the degrees cannot be reduced
  simultaneously).  A code predicate is not a theorem; Sec. 4 supplies the
  theorem for each predicate, or says it could not.
```

No new exit-price assertion is made, so no `charge_basis` line is licensed.

---

## 1. Frozen-input gate

Manifest built mechanically with `awk` from the paired
`charged_input_<i>_basename=` / `charged_input_<i>_sha256=` lines of
`xmodel/own-data-gate-opus5-20260905.run.v2`, then `sha256sum -c`:
**7/7 `OK`**, no digest retyped by hand. Banked at
`box/own-data-gate-20260905/inputs.sha256` (+ `inputs.check.log`); this lane's
own artifacts at `artifacts.sha256`.

p.200 was rendered fresh at 150 dpi from the charged PDF
(`box/own-data-gate-20260905/pg61-61.png`, PDF page 61 = printed 200); p.170,
p.174, p.179, p.188, p.197 were read from images already banked in
`box/child-own-v-20260905/`. Every quotation is read off an image, not off the
PDF text layer.

---

## 2. What I built, and what it agrees with

Two independent instruments, neither importing `box/lib/descend_own.py`:

* **`box/own-data-gate-20260905/mygate.py`** — the first-support arithmetic,
  written from Def 5.1(1)-(4) p.179 and Prop 4.6(1) p.170 only. On all 1,420
  operative rows its set of admissible first-nonzero indices is **identical**
  to Astra's `outer_routes` (1,420/1,420, zero disagreements).
* **`box/own-data-gate-20260905/routes_probe.py`** — a switchboarded copy of
  the source-tree engine, one flag per condition, so each condition's load is
  measurable by turning it off. With all flags on it reproduces Astra's
  `full_source_routes` exactly: **90 rows, identical `j`-sets**, and after the
  finite-pole removal the same **65**.

So the numbers are not in dispute; only their licences are. The route states
are `EMPTY_NECESSARY_FIRST_SUPPORT` 1,051, `EMPTY_NECESSARY_WHOLE_SOURCE_TREE`
214, `EMPTY_PROP6.3_FINITE_POLE` 90, `NONEMPTY` 65.

### 2.1 My own reduction, and what it can and cannot do here

My frozen child-top lane proved (validated 8/8) that the child's own p.150
expansion is the parent's **x-side** p.150 datum, `pi <-> y`, `gamma <-> x`.
That is an independent route to the child's data, but say up front what it does
**not** give: for a census ROW (a tower datum, not a pair) the parent's x-side
`V` is a free invariant, not a function of the y-side row, so the reduction
cannot alone print `V'` for a hypothetical row.

What it does supply, and I use all three:

1. **An independent necessary check Astra deliberately does not run.** Under
   the reduction the child is a legitimate Def 5.1 tower in its own right, so
   the child's own Def 5.1(2) (`V'_{i+1}d'_i/d'_{i+1} >= V'_i > d'_i/(n'-M'_i)`,
   `V'_{s'+1}=d'_{s'+1}`) and its own root count (`V'_2 <= d'_2`, i.e. U-NEG)
   are necessary. On the 65 singletons: **65/65 PASS** — none is refuted by its
   own child-side data and no extra kill appears. On the outer vectors of the
   214 tree-rejected rows: **0 of 214** corroborated, so those 214 rest
   entirely on the source-tree layer.
2. **An independent derivation of the finite-pole obstruction** (Sec. 3.4),
   which comes out cleaner than Astra's and does not need the normalization
   step Astra's version leans on.
3. Confirmation of `n' = deg_x g`, `m' = deg_x f`, `M'_i = M_i u_s/d_s`, and
   of the `u_s > 1` prefix-only typing — all matching `descend_own`'s
   `raw_M`/`characteristic_scope`.

---

## 3. Part (2) of the charge: the controls. All pass.

### 3.1 Moh's own printed rows must be NONEMPTY — they are

Moh's five p.207 descended rows are census rows with the terminal `M_s = n-2`
appended (Moh prints only the level-2 column). All five, plus `(99,66)`, run
through `descend_own` as **NONEMPTY singletons**, and my `mygate.py` gives the
same first-support index:

| source `(n,m)`, `M`, `V` | state | own `V'_2` | Moh's printed child |
|---|---|---:|---|
| `(64,48)`, `(-48,52,62)`, `(3,3)` | NONEMPTY | **3** | `(16,12);13;3` |
| `(84,56)`, `(-56,64,82)`, `(2,3)` | NONEMPTY | **2** | `(21,14);16;2` |
| `(84,56)`, `(-56,72,82)`, `(5,3)` | NONEMPTY | **5** | `(21,14);18;5` |
| `(75,50)`, `(-50,55,73)`, `(3,4)` | NONEMPTY | **3** | `(15,10);11;3` |
| `(75,50)`, `(-50,55,73)`, `(2,4)` | NONEMPTY | **2** | `(15,10);11;2` |
| `(99,66)`, `(-66,77,97)`, `(8,8)` | NONEMPTY | **8** | not printed by Moh; prefix `(27,18)`, `M'=(-18,21)`, `u_s=3` |

The child `M'` and the child radii also reproduce (`(16,12)`, `M'=(-12,13)`,
`delta' = (1/4,-1)`). **The tool is not universally over-strict.**

### 3.2 The sharper control Astra did not state, and it is decisive

Restrict to `n <= 100`, where Moh's own theorem says there is no
counterexample. Of the 65 singletons, **exactly six have source `n <= 100`, and
they are exactly Moh's five p.207 rows plus `(99,66)`** — i.e. precisely the
data Moh himself carries forward. *Every other* operative row with `n <= 100`
prints empty. That is the right shape for both directions at once: the tool
keeps Moh's survivors and kills what Moh's theorem says must die.

In particular the **12 Moh `<=100` residual fibres (the `s'=3/4` classes of the
h-support gate) are ALL EMPTY** — 9 on the pure Prop 4.6 degree arithmetic, 3
on the source tree:

| child class | source | state | decisive line |
|---|---|---|---|
| `6_13/V1_1` | `(96,72)` `(-72,36,78,94)` `V=(1,1,5)` | tree | outer `j=3` rejected |
| `6_13/V1_3` | same, `V=(1,3,5)` | arith | `i=2`: `b=7,V=1,P=6`, `7>6` and `7 /| 5` |
| `6_13/V4_3` | same, `V=(4,3,5)` | arith | `i=2`: `b=7,V=4,P=6`, `28>6` and `7 /| 2` |
| `2_9/V1_8` | `(90,60)` `(-60,10,45,88)` `V=(1,8,4)` | tree | outer `j=2` rejected |
| `2_9/V3_8` | same, `V=(3,8,4)` | arith | `i=2`: `b=21,V=3,P=24`, `63>24`; zero route ends at level 2 (Prop 5.6) |
| `12_17/V1_2` | `(96,64)` `(-64,48,68,94)` `V=(1,2,3)` | arith | `i=2`: `b=5,V=1,P=4`, `5>4` and `5 /| 3` |
| `12_17/V2_1` | same, `V=(2,1,3)` | tree | outer `j=3` rejected |
| `12_17/V3_2` | same, `V=(3,2,3)` | arith | `i=2`: `b=5,V=3,P=4`, `15>4` and `5 /| 1` |
| `m12_m2_5/V1_1_6` | `(96,64)` `(-64,-48,-8,20,94)` | arith | `i=3`: `b=77,V=1,P=12`, `77>12` and `77 /| 11` |
| `9_20/V1_9` | `(96,72)` `(-72,36,80,94)` `V=(1,9,3)` | arith | `i=2`: `b=22,V=1,P=18`, `22>18` and `22 /| 17` |
| `9_20/V4_9` | same, `V=(4,9,3)` | arith | `i=2`: `b=22,V=4,P=18`, `88>18` and `22 /| 14` |
| `m15_14/V1_9` | `(96,72)` `(-72,-60,56,94)` `V=(1,9,3)` | arith | `i=2`: `b=58,V=1,P=18`, `58>18` and `58 /| 17` |

This is corroboration, not alarm: these twelve are exactly the classes the
campaign had not yet retired but Moh's `<=100` theorem already covers. It is
**not** a licence to discard the source-complete charts, which prove a
different statement under different hypotheses.

### 3.3 Sampled empties: 45 drawn at seed 20260905

33 arithmetic, 10 source-tree, 2 finite-pole; each row's decisive line is
printed in the run log. The arithmetic failures are not marginal. Examples,
verbatim from my independent engine:

```text
(192,128) M=(-128,-96,-48,24,76,190) V=(36,24,12,6)  u=1
   i=5: b=43  V=6  P=6   -> bV=258  > P ;  43 | (6-6)   ok, keep descending
   i=4: b=125 V=12 P=12  -> bV=1500 > P ;  125 | 0      ok
   i=3: b=179 V=24 P=24  -> bV=4296 > P ;  179 | 0      ok
   i=2: b=215 V=36 P=48  -> bV=7740 > P ;  215 /| 12    BOTH FAIL -> empty
(144,96) M=(-96,-72,12,112,142) V=(17,18,9)  u=1
   i=2: b=161 V=17 P=36  -> bV=2737 > P ;  161 /| 19    BOTH FAIL -> empty
```

A degree-`P` polynomial cannot contain a Galois orbit of length `b*V`. There is
no slack anywhere near these numbers.

### 3.4 The 90 dropped tails, re-derived through my reduction

Astra's finite-pole argument is correct, and my reduction gives a shorter,
normalization-free version. All 90 hypotheses check exactly (`u_s=1`,
`n-M_{s-1}=d_s`, `delta_{s-1}=0`, `deg Q = V_s in [3,7]`, `A in [13,341]`
integral). `delta_{s-1}=0` is forced, not assumed: with `M_s=n-2` and
`n-M_{s-1}=d_s`, Def 5.1(3) gives `delta_{s-1}=1-(2V_s-d_s)/(V_s-1)=0` exactly
when `V_s=d_s-1`, i.e. `u_s=1`; and the 90 rows carrying some `delta_i=0` for
`2<=i<=s-1` are **precisely** the 90 dropped rows.

The argument, my version:

* At the `delta_{s-1}=0` disc the general point is `sigma = pi` (a constant),
  so Prop 4.6(2) p.170's leading form of `T^psi_{s-1}` in `pi` **is** the
  leading `x`-coefficient `a_D(y)` of `T_{s-1} = sum_k a_k(y)x^k`, `D = deg_x`.
* Prop 4.6(2),(3): that leading form is `p^A q` with `q` of degree
  `V_s (n-M_{s-1})/d_s = V_s >= 3` and **all roots distinct**. So `a_D(y)` has
  at least three distinct roots, at least two of them nonzero.
* Prop 6.3 substitutes `y = gamma^{-u_s}` and `x = [y-e-A(gamma)-pi gamma^{v_s}]/b`,
  so the leading `pi`-coefficient of the transform is
  `a_D(gamma^{-u_s}) * (-gamma^{v_s}/b)^D`. This is a nonzero constant iff
  `a_D` is a **monomial** in `y`. It is not.
* **p.197 Prop 6.3(2), verbatim:** "`gbar(sigma), Tbar_1^psi(sigma), ...,
  Tbar_{s-1}^psi(sigma)` are **monic in `pi`** with `pi`-degree
  `u_s n/d_s, u_s(-mu_1)/d_s, ..., u_s(-mu_{s-1})/d_s` respectively."
  Contradiction.

This needs no constant normalization and no "pole above finite gamma"
language: three distinct residues alone kill monicity. It is the same
obstruction Astra states, obtained from the other side of my `pi <-> y`
identification, which is the independence the charge asked for. The p.174
**Definition–Remark** ("if `M_h = n-1`, then we should drop it ... The last
effective characteristic pair is denoted by `M_s`") licenses the drop for the
child, since Prop 5.1's only hypothesis (`g` monic in `y`, `deg_y g = n > 1`)
is supplied for `g'` by Prop 6.3(2). Astra does **not** use the invalid
rescaled post-drop radius formula for these kills — `descend_own.py:230`
asserts formula/metric agreement only on non-dropped rows. That is correct
practice and I confirm it.

---

## 4. Part (1): necessity, step by step, with the printed line

Each row of the table was measured by switching the condition off in
`routes_probe.py` and recounting; "rows carried" is the number of rows that
become nonempty when that single condition is dropped.

| step, as coded | printed line that makes it necessary for a realized pair | rows carried |
|---|---|---:|
| centre support of a Galois-stable disc lies only at recorded radii and at exponent 0 | Def 5.1(4) p.179 (general point `sigma_i = sum a_j t^j + pi t^{delta_i}`) + conjugation in `k((t^{1/N}))/k((t))`: a common coefficient at a non-integral exponent is scaled by a nontrivial root of unity, hence 0. `deg g = deg_y g = n` (Prop 6.3 hyp., p.197) forces `ord(y) >= -1`, and the only integer in `(-1,1)` is 0, absorbed by `e` in `z = y - bx - e` | all |
| `P_i = V_{i+1} d_i/d_{i+1}` is `deg p` | Prop 4.6 conclusion (1) p.170 ("powers of a common polynomial `p(pi)` of degree `v`") with Def 5.1(4)'s `v = V_{i+1}(d_i/d_{i+1})` | all |
| `p = xi^z prod (xi^{b_i}-c_nu)^{r_nu}`, `b_i = den(delta_i)` | same conjugation; `g_sigma = c p^{n/d_i}`, so the `t^{delta_i}`-coefficients of the roots of `g` in `D_i` are the roots of `p` | all |
| nonzero selection needs `b_i V_i <= P_i` | the selected subdisc is a root of `p` of multiplicity `V_i` (Def 5.1(1) root count); a nonzero root drags its whole orbit, contributing `b_i V_i <= deg p` | **1,051** |
| zero selection needs `b_i | (P_i - V_i)` | same factorisation with `z = V_i` | (same block) |
| all-zero route excluded | **Prop 5.6 p.188 verbatim**: if the `pi`-root `sigma_1` in `D_1` is `sigma_1 = pi t^{delta_1}` then either `k[x,y]=k[f,g]` or there is an automorphism reducing `deg f, deg g, deg T_1^psi` simultaneously — both excluded by p.200 search condition (3) | 12 (arith.), 0 (tree) |
| `delta_j > 0` at the first nonzero | vacuous here: **no operative row has `delta_i < 0` for `2<=i<=s-1`** (measured, 0/1,420). The only `delta_i <= 0` in range is `delta_i = 0` on the 90 dropped rows, where the coefficient is the exponent-0 constant absorbed by the `e` gauge | **0** |
| every *major* sibling factor must extend to a full tower | **p.200 Theorem (4) verbatim**: "if the number of roots of `g(y)` in `E_i` is `> n/(n-M_r)` then the tower of major discs `D_s ⊋ ... ⊋ D_r` can be extended to `D_s ⊋ ... ⊋ E_i`". Multiplicity `>` `d_r/(n-M_r)` is exactly the code's `lo`. Since every such tower is a Def 5.1 tower, Prop 5.5/5.6 and the p.188 relation apply to it too | **95** |
| at least one major factor must exist | **p.200 Theorem (7)** verbatim | (inside the above) |
| number of subdiscs `<= (n-M_r) V_{r+1}/d_{r+1}` | **p.200 Theorem (6)** verbatim; equivalently Prop 4.6(3),(4) (`q` has distinct roots, all roots of `p` are roots of `q`) | 0 |
| bottom: `A | n*V_2` and `A | m*V_2 - 1`, or the swap | **p.188 verbatim**: "`A|n*V_2 and A/|m*V_2 or A/|n*V_2 and A|m*V_2`", together with the same page's "we always have from the very definition of `A` the following: `A | (n*+m*)V_2 - 1`". Astra's correction — `A = den(L*delta_1)` with `L` the **actual** centre stabilizer, not an accumulation of radius denominators — is a *relaxation* and is the right generalisation of Moh's `A` (a zero coefficient adds no ramification) | **88** |
| `d_s > V_s > d_s/2` at the top | Def 5.1(2) p.179 + the p.179 note on Prop 5.2 (a subdisc is usable if it holds more than the average number of roots) | 0 |
| **`P == Q*z` / `P == Q*r`** ("PropA.3 resonance") | **NOT CONFIRMED.** The intended line is Prop 4.6(5) p.170, "`p(pi)` is not a power of `q(pi)`". `P == Q*mult` is `mult = d_j/(n-M_j)`, which is necessary but not sufficient for `p = q^w` | **1** |
| finite pole on the 90 dropped tails | Prop 6.3(2) p.197 (monic in `pi`) + Prop 4.6(2),(3) p.170 + p.174 Definition–Remark. Independently re-derived in Sec. 3.4 | **90** |

### 4.1 The one fix, in full

The surviving witness for `(168,112)`, `M=(-112,140,160,166)`, `V=(3,21,3)`,
first nonzero at `j=2`:

```text
   j=3  delta=1/5   A=5   P=21  Q=6   z=21  orbits=()        mode=zero
   j=2  delta=3/10  A=10  P=42  Q=21  z=2   orbits=(3,1)     mode=nonzero
        p = xi^2 (xi^10 - c_1)^3 (xi^10 - c_2)^1
        distinct roots of p = 1 + 10 + 10 = 21 = deg q       (Prop 4.6(3),(4) ok)
        multiplicities {2,3,1} are NOT all equal  =>  p is not a power of q
        Prop 4.6(5) SATISFIED; the code kills it only because 2 = P/Q = 42/21.
   bottom:  delta_1 = 3/4, centre_L = 10, A_1 = 2, V_2 = 3    (p.188 ok)
```

Own child data: `(42,28)`, `M' = (-28,35,40)`, `d' = (42,14,7,1)`, `u_s=1`,
`ell=1`, **own `V' = (3,7)`** against copied `V = (3,21)`. It passes the
child's own Def 5.1(2) and U-NEG (Sec. 2.1). Note it also illustrates Astra's
central point: the old frozen tier kills this row by (C-TOP) using the copied
`V_3 = 21 > d'_3 = 7`, whereas its *own* `V'_3 = 7 <= 7` passes. So the fix
adds a row that the *old* accounting had killed for the wrong reason.

Relaxing the filter creates no new set-valued row and widens none of the 65:
the first-support index set determines the `V`-vector, and the measured
`rows made multivalued` is 0.

### 4.2 Candidates the charge named that I checked and cleared

* **"centre stabilizer".** Correct, and Astra's version is *looser* than the
  frozen Tree's: `L` stays `L` on a zero selection, `L -> lcm(L, den(delta))`
  on a nonzero one, relative orbit length `A = den(L*delta_next)`. A zero
  coefficient genuinely adds no ramification denominator. Under the campaign's
  shear `z = y - bx - e` the level-`s` coefficient is gauged to 0 while
  `delta_s = -1` is *integral*, so `D_{s-1}` is Galois-stable and `L = 1` at
  the top even though Prop 6.3 needs `b != 0` — the code's `removable` branch
  gets this right.
* **"compulsory major branches".** p.200(4)/(7), verbatim, quoted above.
  Necessary. Carries 95 rows — the single heaviest tree condition, so it is
  the one to re-audit if any of this is ever promoted.
* **"finite-pole obstruction".** Sec. 3.4. Necessary, independently derived.
* **set-valued/multivalued data.** `descend_own` stores whole correlated
  vectors per first-nonzero index, never a coordinatewise product, and keeps an
  empty set empty. I re-derived the marginals: no product artifact. The two
  preliminary set-valued outer rows are emptied by the source tree, not by a
  marginal collapse.
* **the p.174 drop.** Printed, and available to the child (Sec. 3.4). Astra's
  refusal to rescale the post-drop radius formula on dropped rows is right and
  is enforced by the code, not just asserted.
* **rejection completeness.** A "no route" verdict is not a greedy-search
  artifact: `_ok` exhausts every `z` in its residue class and every mode before
  returning `None`, and recursive results are memoised. Only successes
  short-circuit.

---

## 5. What the 66 are, and what they are not

| bucket | rows | type |
|---|---:|---|
| own U-NEG, `u=1` | 84 | licensed necessary contradiction (Def 5.1(1) root count) |
| own U-NEG predicate, `u=2` | 6 | radius-conditional; source tree independently empty |
| dropped tail (disjoint from U-NEG — verified, overlap 0) | 90 | licensed finite-pole contradiction |
| other empty necessary source trees | 1,174 | empty own-data set |
| **singleton own data, `u=1`** | **46** | necessary data; own C-TOP passes |
| **singleton retained own data, `u>1`** | **20** | prefix values only; terminal scope conditional |
| total | 1,420 | necessary source rows, never a count of pairs |

I confirm the disjointness Astra asserts: the 90 U-NEG rows (84 at `u=1`,
6 at `u=2`) and the 90 dropped rows (all `u=1`) do not overlap at all.

The `u>1` block of 20 is **prefix-only**, exactly as my frozen child-top lane
requires: at `u_s >= 2` the chain does not close (`d'_{s'+1} = u_s > 1`) and
p.150 admits `M'_{s'+1} = infinity` as well as `< n'-1`, so
`OPEN[CTOP-EXTRA-CONDITION-E]` stays live and Astra correctly does not consume
it. Astra's "C-TOP contributes zero exclusions" is consistent with my lane; I
checked that no singleton's own data violates the child's own C-TOP bound.

Effective heights of the 65 as banked: `u=1` gives `{2:24, 3:20, 4:1}` and
`u>1` gives `{2:19, 3:1}`; the fix adds one `u=1` row at `s'=3`.

---

## 6. FALLACY-v2 ledger

| clause | where it bit |
|---|---|
| Floor/attainment | `b_i V_i <= P_i` is a budget inside a degree-`P_i` polynomial, used in the safe direction only (violation kills). The surviving 66 are never read as attained. |
| Carrier/attainment | Moh's p.207 five and `(99,66)` are printed admissible data, used only as a control that the tool does not kill survivors — never as realized pairs. |
| Pole/interior | The finite-pole step is used only after checking every source hypothesis on all 90 rows (`u=1`, `n-M_{s-1}=d_s`, `delta_{s-1}=0` *derived* not assumed, `deg q = V_s >= 3`, `A` integral) and after checking Prop 6.3(2)'s monicity is actually printed rather than inferred. |
| Prime label/derivative | `M', d', V', delta'` are child labels, `M~` the parent's x-side label; Sec. 2.1 says my lane *proves* they coincide. No prime here means differentiation. |
| Variable/ring map | Sec. 3.4 declares the substitution (`y = gamma^{-u_s}`, `x = [y-e-A(gamma)-pi gamma^{v_s}]/b`), the direction of the identification (`pi <-> y`, `gamma <-> x`), and checks the image degrees against Prop 6.3(2) before concluding anything about leading coefficients. |
| Merge-free / M-descent | The `u>1` block stays prefix data; no terminal index is invented at `n'-2` or inferred from a finite gcd list. |
| Target/arrival index | Source level `i`, first-nonzero `j`, source `s`, child depth `s'` and child raw last index stay distinct; `V_{s+1}=d_{s+1}` is the source's convention and is not transported. |
| Per-ray/exit-set charge | Each emptiness is charged to exactly one first separation — the level at which both tests fail — and each condition's load was measured by single-flag ablation so that 95/88/1 are not double counted (they are per-condition marginals, not a partition; the three overlap on the 214). |
| `sat()`, raw remainder degree | No Groebner or saturation run in this lane; `k killed inline = 0`. |
| positive/negative controls | Positive: Moh's six `n<=100` survivors stay nonempty with the printed `V'_2` values. Negative: every other `n<=100` operative row, including all 12 residual fibres, prints empty — the direction Moh's own theorem requires. Independent-code control: 1,420/1,420 agreement on outer sets and 90/90 on full routes from engines written off the print. |

**Correction to the charged report, stated once.** `child-own-v-astra-20260905.md`
types the finite-set census as "**DETERMINED** ... 65 rows have singleton
necessary own-data sets; 1,355 have empty sets". One of its 1,355 is carried
by a filter that is stricter than the printed Prop 4.6(5); the correct counts
are **1,354 / 66**. Nothing else in the report's arithmetic, its partition
structure, its D1 identity `V'_2 = V_2`, its zero-C-TOP-exclusion finding, or
its `OPEN[MINOR-RADIUS-BOUNDARY-ONE]` typing is affected.

---

## OPENS RAISED

```text
OPEN[RESONANCE-FILTER-EXACT-FORM]
  QUANTITY: the exact necessary form of Prop 4.6(5) p.170, "p(pi) is not a
    power of q(pi)", as a predicate on (z, {r_nu}, A, P, Q).  The correct
    predicate is  NOT( all multiplicities equal w  AND  [z>0]+A*#orbits = Q
    AND P = Q*w ); the code uses the strictly stronger per-factor test
    mult != P/Q.
  STATUS: the code's test is REFUTED as necessary on one explicit witness
    (Sec. 4.1).  The corrected predicate is stated but not swept.
  CHEAPEST TEST: replace the two `continue` guards at own_v_routes.py:66,74
    with the conjunctive predicate and rerun the 1,420-row sweep; ~2 minutes.
  BLAST RADIUS: 1 row at n <= 200 (source (168,112), V=(3,21,3)); the
    operative residual is 66, not 65.  No other count moves.

OPEN[SIBLING-EXTENSION-DEPTH]
  QUANTITY: p.200 Theorem (4) licenses extending the tower THROUGH any major
    subdisc E_i; own_v_routes additionally demands that the resulting tower
    reach a valid bottom at level 2 satisfying the p.188 divisibility.  The
    step "every major sibling reaches a p.188-valid bottom" is the composition
    of p.200(4) with Prop 5.5's proof, and I confirmed each link separately
    but did not verify that Prop 5.5's proof needs no further hypothesis on a
    NON-selected tower.
  STATUS: believed necessary; the individual printed lines are quoted in
    Sec. 4.  Not independently re-derived.
  CHEAPEST TEST: read pp.185-188 (the full proof of Prop 5.5) and check that
    its hypotheses are exactly Def 5.1 for the tower it is applied to.
  BLAST RADIUS: 95 rows of the 1,354, including 3 of the 12 Moh <=100
    residual fibres (6_13/V1_1, 2_9/V1_8, 12_17/V2_1).  If it fails, the
    residual is at most 66+95 = 161, still far below 1,420.
```

## OPENS RETAINED

```text
OPEN[MINOR-RADIUS-BOUNDARY-ONE]   -- unchanged; the six u=2 U-NEG rows are
  independently empty, so it does not move the 66.
OPEN[CTOP-EXTRA-CONDITION-E]      -- unchanged; the 20 u>1 singletons are
  prefix-only and Astra does not consume it.
OPEN[PROP6.3-RADIUS-US>1]         -- unchanged.
OPEN[CHILD-TERMINAL-SUPPORT-US>1] -- unchanged.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `25512`.
- Body SHA-256:
  `f62e51981d48653043a32daba24dcb821dfedac0fef5d5dee02ab3fc1fd1e4ef`.
- Frozen basis: `b1966334d0a6f0c2f6a5f77e56c3be467de617ea`.
