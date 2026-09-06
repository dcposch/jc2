# THEOREM [ACTUAL-STABILIZER SCREEN] — Opus 5 — 2026-09-06

```text
VERDICT.  PROVED (necessity), not refuted.
  Moh's L in (8) p.201 is an over-approximation.  His automorphism is only required to
  FIX THE CENTRE of the current disc, and the centre is built one term at a time by
  Prop 5.3 p.180's tau = sum a_j t^j + C_r t^{delta_r}: a selected factor pi (C_r = 0)
  contributes NO term, so it cannot enlarge the denominator lattice.  LEMMA A proves the
  centre's support carries no other fractional exponent, so the modulus is exactly
      Lcal_j = lcm{ den delta_i : j < i <= s, C_i != 0 },   A_j = den(Lcal_j delta_j).
  Every clause -- (10)/(11), the orbit enumeration b == P (mod A), the per-factor ODE
  P != Q v, the Prop 5.6 danger, the bottom (12)/(13) -- is necessary at THIS modulus,
  with a printed line each.  No witness row can exist: the screen is existential over
  branch patterns and a pair supplies its own pattern.
  CALIBRATION (decisive).  ACTUAL survivors at n <= 100 are EXACTLY Moh's six p.202 rows
  (set equality); the COARSE reading leaves 14 excess rows at (90,60),(96,72),(96,64), all
  with 3 <= s <= 5, d_s >= 4 -- inside Moh's search range and contradicting his printed
  p.207 Appendix II.  The coarse reading of (8) is refuted BY MOH'S OWN OUTPUT.
  All five p.207 descended rows survive; (99,66) survives.
  Chain: 24,063 -> 1,420 (coarse) -> 90 (actual) = 65 roster + 25 finite-pole; the
  further 90 -> 64 consumes two OTHER lanes' licences, not proved here.
```

No new exit-price assertion is made, so no `charge_basis=` line applies.

## 0. Custody

Manifest built mechanically with `awk` from the receipt's numbered
`charged_input_<i>_sha256=`/`_basename=` fields, piped to `sha256sum -c` before any
mathematical read: **9/9 OK** (`box/actual-stabilizer-soundness-20260906/charged-inputs.sha256`);
all reads were the frozen copies in `/tmp/jc2-lane.LKbCI2/inputs`. Moh was read as **page
images** (`pdftoppm`, printed = PDF ordinal + 139): pp.170-171, 179-180, 187-190, 200-202,
207. Declared uncharged repo reads: `opus5_probe.py` (coarse
control) and `residual66-20260905/roster.jsonl` (row ids only). No fleet, ledger edit,
`jc2-lean` or `ideation-*`. Writes: this report and the notes dir (2.3 MB). `C_i` is Moh's
selected factor coefficient (p.180, p.190: the factor `pi - C_r`); `Lcal` is the actual
centre modulus, `L` Moh's (8) lcm.

## 1. What the printed argument actually uses

**(8) p.201, verbatim:** "let the l.c.m. of the reduced denominators of `delta_s,...,delta_r`
be `L`. Then `A_{r-1}` is defined to be the reduced denominator of `L delta_{r-1}`. ... Let
`(t-bar)^{L A_{r-1}} = t`. Due to the existence of the following **automorphism of
`k<<t-bar>>` over `k<<t-bar^{A_{r-1}}>>`**: `t-bar -> omega t-bar`, where `omega` is an
`A_{r-1}`-th root of unity, the value of `V_{r-1}` is further restricted by (10) ... (11)."

The base field is `k<<t-bar^{A_{r-1}}>> = k((t^{1/L}))`. **The only role of `L` is to
name a field the automorphism must fix**, and the only thing that must lie in it is the
centre: writing the Def 5.1(4) p.179 general point `sigma_{r-1} = sum alpha_j t^j + pi t^{delta_{r-1}}`,
the automorphism `tau` sends `sigma_{r-1}(pi)` to `tau(sum alpha_j t^j) + omega^a pi t^{delta_{r-1}}`,
and this is `sigma_{r-1}(omega^a pi)` **iff `tau` fixes the centre `sum alpha_j t^j`**.
Moh's own `s = 2` instance says this sharply: p.188, "**The conjugations of `k((t^{1/A}))`
over `k((t))`** show us that if the reduced denominator `A` of `delta_1` is not a factor of
`deg g_sigma(pi) = n* V_2` then `pi` is a factor of `g_sigma(pi)`" -- there `L = 1` and the
base field is `k((t))` because at `s = 2` the centre is integral (`delta_2 = -1`, p.187).
The printed base field is *the field of the centre*; (8) names it by a sufficient recipe.

**The centre is built one selected coefficient at a time.** Prop 5.3 p.180, verbatim: "Let
`pi - C_r` be a factor of `p(pi)` ... with multiplicity `V_r` ... Let `tau` and `delta_{r-1}`
be defined as follows **`tau = sum alpha_j t^j + c_r t^{delta_r} in D_r`**, `delta_{r-1} =
min{ord(tau_i - tau_j) : tau_i, tau_j roots of g(y) prod T_i^psi(y) with ord(tau_i - tau) >
delta_r and ord(tau_j - tau) > delta_r}` = **the logarithmic radius of `D_{r-1}` which is the
minimal disc containing all roots `tau_i` ... with `ord(tau - tau_i) > delta_r`**."

So `delta_r` enters the centre of `D_{r-1}` with coefficient `C_r`; with `C_r = 0` -- Moh's
own p.201 case, "(11) ... if the corresponding factor of `p(pi)` is of the form `pi`" --
**no term is added at all**. That is the whole sharpening.

## 2. LEMMA A (centre support)

**Lemma A.** Let `c_i` be the centre of `D_i` (the common truncation below `delta_i` of the
roots of `G := g prod T_j^psi` in `D_i`; canonical, and Def 5.1(1) p.179 guarantees
`(n/d_{i+1}) V_{i+1} >= 1` such roots). Then every `e in Supp(c_i)` satisfies
`den(e) | Lcal_i := lcm{ den delta_j : i < j <= s, C_j != 0 }`.

*Proof.* Order `Supp(c_i) = {e_1 < e_2 < ...}`; induct on `k`. Put
`Lcal' = lcm{den e_l : l < k}` (`= 1` at `k = 1`); by induction `Lcal' | Lcal_i`. Suppose
`den(e_k) ∤ Lcal'`; let `tau_aut : t^{1/N} -> zeta_N^{Lcal'} t^{1/N}` for a common
denominator `N`. It fixes `k((t))` -- hence permutes the roots of `G in k[x][y] ⊂ k((t))[y]`
-- fixes `c_i|_{<e_k}` pointwise, and scales the `t^{e_k}` coefficient by
`exp(2 pi i Lcal' e_k) != 1`. For a root `xi` of `g` in `D_i`, `xi` and `c_i` agree below
`delta_i > e_k`, so `ord(xi - tau_aut xi) = e_k` exactly. Three cases.

* `e_k < delta_s`: `D_s` is **the minimal disc containing all roots** of `G` (p.179, note
  after Def 5.1, citing Prop 5.1; restated p.190 §6), so `delta_s = min` pairwise `ord`
  difference over roots, contradicting `ord(xi - tau_aut xi) = e_k < delta_s`.
* `e_k = delta_j` for some `j > i`: then the `delta_j`-coefficient of `c_i` is `C_j` (§1),
  and it is nonzero because `e_k in Supp(c_i)`, so `den(delta_j) | Lcal_i`. Done.
* `delta_j < e_k < delta_{j-1}` for some `j in [i+1, s]`: `xi in D_i ⊆ D_{j-1}` gives
  `ord(tau - xi) > delta_r`-type membership, and `ord(tau - tau_aut xi) >= min(>delta_j, e_k) > delta_j`,
  so **both** `xi` and `tau_aut xi` are among the roots whose minimum p.180 defines
  `delta_{j-1}`. Hence `delta_{j-1} <= ord(xi - tau_aut xi) = e_k < delta_{j-1}`. Contradiction.

(Second route for case 3, using no minimality: Prop 4.6(1),(4) p.170 give
`g_sigma = c p(pi)^{n/d_j}`, so the roots of `g` in `D_j` with `delta_j`-coefficient `C_j`
number `(n/d_j) V_j` = the Def 5.1(1) count of `D_{j-1}`, and `tau_aut xi` would be one of
them outside `D_{j-1}`.) Radii increase strictly downwards by p.180's `min`. QED

**Consequence.** `Stab(c_i) = Gal(P / k((t^{1/Lcal_i})))`; `Lcal_i` is exactly the "start at
1; zero factor keeps `L`; nonzero centre `L <- lcm(L, den delta)`" rule of
`descend_own.py:151-152` / `closure_fixed.py:75,89`. Since `Lcal_i | L_i^{Moh(8)}`,
`A_i^{Moh} | A_i^{actual}`: the actual modulus is a **multiple** of the coarse one, so (10)
and (11) are strictly harder and `actual ⊆ coarse` -- a runtime invariant, never violated.

## 3. THEOREM [ACTUAL-STABILIZER SCREEN]

Let `(f,g)` be a non-coordinate Keller pair in Moh's normalized FS presentation, minimal in
degree sum, with tower `D_s ⊋ ... ⊋ D_1`, configuration `(n, M_2..M_s, V_2..V_s)` and selected
coefficients `C_s,...,C_2`; `Lcal_j` as in Lemma A, `A_j = den(Lcal_j delta_j)`. For
`j = s-1, ..., 2`:

1. **Galois action.** `tau := tau_{Lcal_j}` fixes `c_j`, `t`, `g` and every `T_i^psi`, and
   sends `t^{delta_j} -> zeta t^{delta_j}` with `zeta` **primitive** `A_j`-th. Comparing
   leading coefficients in `g(sigma_j(pi))` gives `p_j(zeta pi) = const * p_j(pi)`: the root
   multiset of `p_j` is `zeta`-stable, freely on nonzero roots, `0` fixed.
2. **(10)/(11) at the actual modulus.** With `deg p_j = tri_j A_j + sq_j` (eq. (9) p.201),
   the nonzero mass is a multiple of `A_j`, so `mult(0) = j' A_j + sq_j` -- **(11)** at a
   selected factor `pi` -- and a nonzero root has `A_j V_j <= deg p_j`, hence `V_j <= tri_j`
   -- **(10)** at a selected factor `pi - a`, `a != 0`.
3. **Orbit-multiset enumeration.** `b := mult(0)` runs over `range(P % A, P+1, A)`; nonzero
   multiplicities come in `A_j`-blocks summing to `(P-b)/A_j`; distinct roots number
   `<= Q_j = deg q` (`q` squarefree, roots of `p` among them, Prop 4.6(2),(3),(4) p.170),
   giving `#orbits <= (Q - [b>0])/A_j`.
4. **Per-factor ODE.** Every factor of `p_j` of multiplicity `v` obeys `P_j != Q_j v`
   (Prop A.3 via p.171, "the conclusions (2),(3),(4),(5) follow at once from Propositions
   A.3 and A.4" -- the `r >= 2` citation, not Prop 4.6's `r = 1` sentence). `A`-independent,
   so it transfers verbatim.
5. **Whole-tree / major threshold.** Each major factor (`v > d_j/(n-M_j)`, Def 5.1(2) p.179 /
   Prop 5.3 p.180 / p.200 Thm (4),(7)) must itself extend to a full admissible tower, with
   **its own** modulus `lcm(Lcal_j, den delta_j)` at a nonzero root and `Lcal_j` at the zero
   root: the sharpening is *per-branch*, and is carried separately down every sibling.
6. **Prop 5.6 danger.** A path whose every selected coefficient is zero or sits at integral
   `delta <= 0` transports by `x -> x, y -> y - ax - b` (p.190, taking
   `sigma_1 = a t^{-1} + b + pi t^{delta_1}` to `pi t^{delta_1}`) to Prop 5.6's hypothesis
   p.188 and is excluded. *Coherence:* `den(delta) = 1` is exactly when the term neither
   enlarges the stabilizer nor survives the translation -- the two rules fire on the same
   levels.
7. **Bottom (12)/(13).** At `r = 2`, `A_1 = den(Lcal_1 delta_1)`; the p.188 conjugation
   argument runs unchanged over `k((t^{1/Lcal_1}))`, giving (12) `A_1 | n* V_2`,
   `A_1 | m* V_2 - 1` **or** the swap (13), from `(g_sigma, T^psi_{1,sigma}) = 1` and
   `(d g_sigma/d pi, d T^psi_{1,sigma}/d pi) = 1` (Prop A.5, p.187).

**Necessity.** Each clause is a property of the pair's own `(branch, V)` pattern at that
pattern's own modulus, and the screen accepts a row iff **some** pattern passes. A realizing
pair supplies its own pattern, which passes by 1--7; no realizing pair's row is rejected. QED

**Where Moh over-approximates.** Nowhere in p.201 or p.188 is `L` used other than to name
`tau`'s fixed field; his recipe makes it a function of the configuration alone -- what a
bounded hand search wants -- and is sufficient, not sharp.

## 4. The zero-factor case, explicitly

A selected factor `pi` has `C_j = 0`. Then (i) by p.180 the centre gains no `t^{delta_j}`
term, and by Lemma A no other exponent of denominator `den(delta_j)` sneaks in;
(ii) `Stab(c_{j-1}) = Stab(c_j)`, i.e. `Lcal_{j-1} = Lcal_j` -- the stabilizer does not
grow; (iii) the zero root is fixed by the whole action, which is why (11) constrains
`mult(0)` by a congruence, not a division. Until the first nonzero selected coefficient
`Lcal = 1` and `A = den(delta)` outright.

## 5. Numerics (independent driver, not the charged one)

`verify.py` re-implements the tree from the printed clauses with an explicit `centre_L`
state; `controls*.py` run the tests. 28.6 s.

| population | rows |
|---|---:|
| census (1)-(13), `16 <= n <= 200`, `Kmin=2` | **24,063** |
| coarse `C_FULL_TREE_POLYNOMIAL_ODE` (0 mismatches vs live `opus5_probe`) | **1,420** |
| **actual-stabilizer screen** | **90** (lost 1,330, gained 0) |
| by `s` | 3:43, 4:45, 5:2, 6:0 |
| roster hits / non-roster | **65 / 25**; only **R063** drops |
| residual 64 | **64/64** still actual-operative |

Reproduces the charged DATA report exactly, independently.

**Calibration against the print.**

* `n <= 100` ACTUAL survivors = **Moh's six p.202 rows, set equality** (mechanically checked
  against the charged `MOH_TABLE`). The coarse screen leaves **20**: 14 excess at `(90,60)`,
  `(96,72)`, `(96,64)`, each with `3 <= s <= 5`, `d_s >= 4` -- inside Moh's range (6) p.201
  -- and each contradicting p.207. **His printed output adjudicates the convention.**
* All five **p.207** descended rows survive. The only one where the conventions can differ is
  `(21,14; M_2=16; V_2=2)`, `delta_2 = -1/2, delta_1 = 7/6`: the `C_2 = 0` branch gives
  `A_1 = 6` and fails (12)/(13); the `C_2 != 0` branch gives `A_1 = 3` -- **Moh's own
  `A_1`** -- and passes (12). The actual rule reproduces his number.
* `(99,66)` `M=(77,97)` `V=(8,8)` survives (`A_2 = 3`, `b = 0`, orbit `(8)`, `A_1 = 3`).
* Sandwich control: the over-strong rule `centre_L == 1` always keeps **72**, so
  `72 < 90 < 1,420` -- the actual rule is neither degenerate limit. Of the 90, 12 use a zero
  factor on the kept path; the force is in the 1,330 rejections.

## 6. The chain, and what it does not include

`24,063 -> 1,420 -> 90` is printed at every step (census (1)-(13) p.200-201; the operative
flags, gate-confirmed 2026-09-05; §3 here). `90 -> 64` is **not** proved here: it consumes
(i) the 25 finite-pole rows' `PROP6.3_FINITE_POLE_US1` obstruction and (ii) R001's removal
by Xu Cor. 5.3 with the `u_s = 1` principal floor; quoting "64" requires naming both. Rows
stay `NECESSARY_TOWER_CONFIGURATION_NOT_POLYNOMIAL_PAIR`. **Not claimed:** the 1,330 as dead
pairs; `embed` = printed-closure `N` (they merely coincided here); any exit price; anything
about `u_s >= 2` child data.

## 7. FALLACY-v2

*Flag/place/series.* Label-zero coefficient, old `1/L` lattice exponent and physical packet
stay apart in Lemma A; the increment action is never identified with the full Puiseux Galois
group -- Lemma A uses the latter to bound the support, its restriction to act on `p(pi)`.
*Carrier/attainment.* No pair is asserted; the `n <= 100` match is corroboration, not
realization. *Target/arrival index.* Coarse `A_i^{Moh(8)}`, actual `A_i` and the orbit size
stay three named objects. *Variable/ring map.* `t = 1/x`, `k[x][y] ⊂ k((t))[y]`, `tau_k`'s
generator and fixed field declared first. *Pole/interior.* Major/minor decided by the
p.190 threshold `d_r/(n-M_r)` first. *Floor/attainment.* No `I_M`/`I_m` claim. Controls: positive
(p.202 six, p.207 five, (99,66), roster 65/66, residual 64/64), negative (`centre_L == 1`
sandwich at 72), plus a 0-mismatch coarse replay against the live probe.

## 8. Verdict

```text
PROVED.  THEOREM [ACTUAL-STABILIZER SCREEN] (Sec.3), on LEMMA A (Sec.2).
  Moh (8) p.201's L is sufficient, not sharp: the printed argument requires only that the
  automorphism FIX THE CENTRE (p.201 "over k<<t-bar^{A_{r-1}}>>"; p.188 "conjugations of
  k((t^{1/A})) over k((t))"), and p.180's tau = sum a_j t^j + C_r t^{delta_r} adds a term
  only when C_r != 0.  Lemma A closes the one gap BOTH readings need -- no other fractional
  exponent in the centre -- from p.180's minimal-disc definition and p.179's Prop 5.1 note.
  Zero factor: centre 0, fixed by every conjugation, stabilizer unchanged (Sec.4).  All
  clauses are necessary at the ACTUAL modulus.  NOT REFUTED: the screen is existential over
  branch patterns, so a realizing pair supplies a passing pattern; no witness row exists.
CENSUS.  24,063 -> 1,420 (coarse) -> 90 (actual); 65 roster + 25 finite-pole; residual
  64/64 unaffected; only R063 drops.  90 -> 64 needs two other lanes' licences.
PROMOTE.  The actual-centre stabilizer as the sound reading of Moh (8) at every level,
  including the bottom A_1; the per-branch (not per-row) character of the modulus.
DO NOT PROMOTE.  The 1,330 as dead pairs; "90 = printed N>0" as a theorem; 64 without
  naming the finite-pole and Xu licences.

OPENS RAISED
  1. Moh's coarse (8) leaves 14 rows at n<100 that his own p.207 Appendix II excludes:
     either he computed with the actual stabilizer, or his search had a further unprinted
     clause.  Deciding this fixes whether any further clause is owed at n > 100.
     QUANTITY: replay the 14 excess rows against every printed clause of p.200-203 and
     name the clause, if any, that kills all 14 at the coarse modulus; <= 3 h.
  2. Lemma A is proved for MAJOR discs.  Minor packets (p.190 Prop 6.1) carry their own
     centres and moduli; the I_M/I_m calculus still uses coarse A_i.
     QUANTITY: re-derive the minor-packet orbit size at the actual modulus and re-run the
     exact-contact 924/1,080 counts; <= 4 h.
  3. No configuration here is a witness pair; unchanged.
```

Replay: `sha256sum -c box/actual-stabilizer-soundness-20260906/charged-inputs.sha256`, then
`python3 .../verify.py 200` (24063/1420/90) and `controls{,2,3}.py`; page images alongside.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16433`.
- Body SHA-256:
  `ba4c45f53204bb309f317542ab0aa37f8464c4835d89ac2e0ac816b6681482e0`.
- Frozen basis: `2c5d904617ceeeee055f093d832f0f7988c352da`.
