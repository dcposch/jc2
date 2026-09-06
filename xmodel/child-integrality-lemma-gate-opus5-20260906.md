# HOSTILE GATE — LEMMA [CHILD-INTEGRALITY] (Astra) — Opus 5 — 2026-09-06

```text
VERDICT: PROMOTABLE.

(1) print-check ......... CONFIRMED-WITH-FIX (one wording fix; substance holds)
(2) R063 = 71/4 ......... CONFIRMED (recomputed independently, end to end)
(3) exhaustion boundary . CONFIRMED-WITH-FIX (certificate stated below; the
                          six-rows fixed list is NOT consumed as exhaustion and
                          does not need to be -- SURVIVES is existential)
(4) u_s >= 2 ............ CONFIRMED (nothing; and a radius proof alone is still
                          not enough -- the child TOP is open too)
(5) promote the conditional lemma and the R063 kill; retain the six-row OPENs.

SINGLE POINT OF FAILURE (unflagged by the producer): the R063 kill rests
ENTIRELY on step 3's "forbidden average multiplicity" exclusion.  Drop it and
z=2 (pi^2(pi^3-c1)^3(pi^3-c2)) survives with sum exactly 9 in Z.  I re-derived
that exclusion from Moh's printed p.169/p.171 equation; it holds, twice over.
```

## 0. Custody

Receipt `charged_input_<i>_sha256=`/`_basename=` fields paired with `awk`, then
`sha256sum -c`: **9/9 OK** before mathematical use. Reads were the frozen copies in
`/tmp/jc2-lane.AqFuif/inputs` only. Moh's decisive displays are OCR-dead, so pp.169-171,
179-182, 197-199 were rendered with `pdftoppm` and read as images. No fleet, ledger edit,
`jc2-lean`, or `ideation-*` input. Artefacts in `box/child-integrality-lemma-gate-20260906/`. No new exit-price assertion is made,
so no `charge_basis=` line applies.

## 1. Print check

**M Prop 6.3, p.197 — CONFIRMED verbatim; the declared map is Moh's, not an analogy.**
The hypothesis is literally "`delta_s = -1` and the logarithmic radius `delta*_{s-1}` of
the minor disc `D*_{s-1} >= v_s/u_s`". Conclusion (1) puts the images in `k[gamma,pi]` — a
**polynomial** ring, so the upgrade of `Phi*: K[x,y] -> K[X,X^-1,Y]` is Moh's own; (2) gives
monicity and pi-degrees `u_s n/d_s, u_s(-mu_i)/d_s`, i.e. `n', m'`; (3) prints
`-(u_s/b) gamma^{v_s-u_s-1}` — the **positive** power. Moh's `u_s,v_s` are the report's
`u,v` (checked three ways). p.198 prints the
inversion `x = (1/b)[theta^-1 + sum c_i theta^i + ...]`, `y = theta^-1`, eq. (10)
`z = y-bx-e`, `sigma = (c_0-e) + sum c_i theta^i + pi theta^{v_s/u_s}`,
`gamma = theta^{1/u_s}`; eliminating gives the report's `Phi*` character for character, and
then `x_pi = -gamma^{v_s}/b`, `y_gamma = -u_s gamma^{-u_s-1}`, `y_pi = 0`, so
`J_{gamma,pi}(x,y) = -(u_s/b)gamma^{v_s-u_s-1}` and `J_{X,Y}(P',Q') = cX^ell` by the chain
rule with the constant parent determinant (the order swap is a sign). Verified
symbolically.

**The p.198 printing-error claim — CONFIRMED, corruption worse than stated (the FIX).**
The report says "the displayed derivatives resolve that printing error". Precisely: (a)
the printed `x_pi` entry is `-1/(b gamma^{v_s})` where the substitution three displays above
forces `-gamma^{v_s}/b`, so one of the two displayed derivatives *is* the corrupt object;
(b) the printed matrix at face value evaluates to `-(u_s/b)gamma^{-v_s-u_s-1}`, which is not
p.198's own printed answer `-u_s/(b gamma^{v_s-u_s-1})` either — corrupt twice, and
internally inconsistent. Only the positive-power reading is self-consistent, and it
reproduces the **statement** p.197(3). Verdict stands; the sentence should read "the
substitution, not the displayed derivatives, resolves it". (The orbit-transport gate found
the same double corruption independently.)

**M Prop 4.6, pp.170-171 — CONFIRMED, and it supplies more than the report claims.**
Hypothesis (2) gives `ord g(sigma) = n lambda`, `ord T_i^psi(sigma) = (-mu_i)lambda` —
where (CI.4) comes from **without** Xu's Keller-only proportional lemma. Conclusions:
`deg p = v`, `deg q = v(n-M_r)/d_r`, `q` squarefree, roots of `p` are roots of `q`, `p` not
a power of `q` — so `P`, `Q` and "at most `Q` distinct factors" are printed, not assumed.
The p.171 **Remark** prints, for `J_{x,y}(f,g) = x^l`, condition
`(3)*: lambda = (-1-l+delta)/(n-m_r) < (-1-l+delta)/(n-m_i)`, i.e. `(delta-H)/(n-M_r)` with
`H = 1+ell`: **the ell-shift of Prop 4.6 is Moh's print.** The Prop 4.4 gap is real and correctly
handled: p.169's Remark shifts Prop 4.4's condition **(6)** only, while p.181 uses its
condition **(3)**, never shifted; the report says so and supplies (CI.6), the exact
`-1 -> -1-ell` analogue of p.170's own display. p.181's chain and p.182's
`epsilon > -1` both shift, and p.182 prints `V = V_r(d_{r-1}/d_r)`, "`r-1` replacing `r`" —
the report's `P_next` and one-step descent are Moh's.

**M Def 5.1 — CONFIRMED.** (1) is the root-count law `(n/d_{i+1})V_{i+1}`,
`(-mu_j/d_{i+1})V_{i+1}` = the report's `rho_Q, rho_P`; (2) prints
`V_{i+1}d_i/d_{i+1} >= V_i > d_i/(n-M_i)`, the **strict** above-average rule; (3) is
`def51_radii` verbatim; (4) licenses Prop 4.6 per level with `v = V_{i+1}(d_i/d_{i+1})`.

**M Prop 5.3, p.180 — CONFIRMED, as an *identity*, not a citation.** It takes *any* factor
with `deg p >= V_r > d_r/(n-M_r)` to a major disc at index `r-1` with the Def 5.1(3) formula
extended one step. Evaluating Moh's printed formula on R063's child symbolically in the free
multiplicity `a = V'_2`, against the report's successor:

```
Moh Prop 5.3 (x H) : (64 - 5a)/(3(5a-1))     report successor : (64 - 5a)/(3(5a-1))
                                  IDENTICAL
```

The report's linearity/intercept construction reproduces Moh's closed form as a rational
function of the free multiplicity — the strongest corroboration here.

**Xu — CONFIRMED.** §2 p.1 defines `I(f,g) = deg_x Res_y(f,g)` for `f,g` **monic in y**,
and Moh 6.3(2) supplies that monicity; `Res_Y(P'-xi,Q')` is monic of degree `n'` in `xi`,
hence nonzero, so `deg_X R` is a genuine non-negative integer — (CI.1) sound. Lemma 4.1 p.4
is stated for **arbitrary** `J(x,y)`; with `J = cX^ell`, `X = t^-1` it gives `-c t^{-ell-2}`,
so (CI.3) is the literal substitution, and Lemma 4.4's proof then yields
`lambda_P + lambda_Q = delta - H` with thresholds `delta < H` / `delta > H`. Thm 5.1 p.7
proves `I(f_xi,g) = (n/(m+n)) sum_{P_M}|D_sigma|(1-delta_sigma)` via
`-lambda^g = n(1-delta)/(n-M_1)`; replacing `1 -> H`, `(n,m,M_1) -> (n',m',-m')` is (CI.5)
exactly (`M'_1 = -28 = -m'` verified). The report is right to refuse Xu's global route:
Lemma 2.1 is stated *for a Jacobian pair* and Lemma 4.2 invokes it, so it does not transfer
at `J = cX^ell`; §3 is explicitly Jacobian-free, so Prop 3.3 does. `I(P'_Y,Q'_Y) = 0` is likewise
correctly refused — Xu gets it from `J in K*`, whereas at `J = cX^ell` common derivative
roots over `X = 0` are allowed; the replacement `Res_Y(P'_Y,Q'_Y) = c_0X^k` is justified
correctly.

**Boundedness / `Q'-eta` — SOUND.** `Q'-eta` is monic of the same `Y`-degree,
`J_{X,Y}(P',Q'-eta) = J_{X,Y}(P',Q')` (a constant dies under `partial`), negative orders
are unchanged, and every bounded value acquires order **exactly** 0 for generic `eta`: all
hypotheses preserved, omitted roots contribute exactly zero. Vacuous on R063 — all 28 roots
sit in the four major packets. **(CI.7) — CONFIRMED**: I redid the ultrametric count
and both term bounds come out as printed, `ell`-independent.

**"Complete sum, never summands" — CORRECT and necessary**: (CI.5) is an equality for the
total only, and R063's summands are `3,3,3,35/4`; a per-summand test is a Floor/attainment
fallacy, and `check.py` carries this as a control. **"Certified empty => dead" — SOUND**:
the empty case is the *same* universally quantified sentence, and the contradiction is with
coverage hypothesis (3), not with evaluating a nonexistent sum, which is how the report
words it. The live risk is an emptiness certificate resting on a non-*necessary* filter;
for R063 that filter (final Galois residues) is not established inside the charged set,
**but the kill does not need it** (§2).

## 2. R063 recomputed independently

All from the printed formulas, not the report's numbers. **Own data.** `n=168, m=112, M=(-112,140,160,166), d=(168,56,28,4,2), V=(3,21,3)`; Def
5.1(3) gives radii `(3/4, 3/10, 1/5, -1)`, with `M_s = n-2`, `delta_s = -1`. `d_s = 4`,
`V_s = 3`, so `u=1, v=3, ell=1, H=2` and Prop 6.4 licenses the descent. `n'=42, m'=28`;
`M' = M/4 = (-28,35,40)` (`166/4` non-integral, prefix stops); `d' = (42,14,7,1)` with
`d'_s = 1 = u`. Route tests at `i=3,2` leave a
**singleton** outer family `V' = (3,7)` (`i=3` zero-only, `i=2` nonzero-only); child radii
`(7/6,-1/3,-2)` reproduced twice — local inverse map, and `def51_radii(child) * H` — with
`delta'_{s'} = -2 = -H`.

**Forced top.** `D'_3`: `P = 7`, `Q = 2`, `A_0 = 1`; multiplicity `7 = P` uses the whole
degree (one factor up to translation) and `rho_P = 28`, `rho_Q = 42`, so the top holds
**all** roots, `L = 1`.

**Forced level-2 pattern.** `D'_2`: `P = 14`, `Q = 7`, `A_0 = den(-1/3) = 3`, average
`P/Q = 2 = d'_2/(n'-M'_2)`. Enumerating all `0 <= z <= 14` with `3 | 14-z` and all
partitions of `(14-z)/3`, under `1_{z>0} + 3k <= Q` and occurrence of the selected
multiplicity `V'_2 = 3`:

```
 z= 2: NONE (the zero factor would have multiplicity 2 = P/Q)
 z= 5: [(3,)]                               <-- unique survivor
 z= 8,11,14: NONE  (remaining degree 2,1,0 < 3)
```

so `p'_2 = pi^5(pi^3-c)^3` is forced; `z in {2,5,8,11,14}` is just `3 | 14-z`. The report's
"8,11,14 cannot hold the nonzero orbit" is loose but true: no multiplicity-**3** orbit fits.

**Why `z = 2` is excluded — re-derived from print, because everything depends on it.**
Moh p.169/p.171 print, with `T_r = p^E q`, `(deg T)T p' - v p T' = c* p^{E+1}`, which
reduces (using `deg T - vE = v(n-M_r)/d_r = Q`, `v = P`) to `Q p'q - P p q' = c* p`, with
`c* != 0` (else `p^{deg T} = const * T^P`, contradicting Prop 4.6(5)). At a root of `p` of
multiplicity `a` — a **simple** root of `q` by Prop 4.6(3)(4) — matching the `t^a`
coefficient gives `u(0)(Qa - P) = c* != 0`, hence `a != P/Q`. Verified symbolically for
`a = 1,2,3,5,7`. The rule is Moh's, and it is strictly stronger than Def 5.1(2), which
constrains only the *selected* `V_i`.

**Sensitivity.** Drop that exclusion and `z = 2` gives `pi^2(pi^3-c_1)^3(pi^3-c_2)`: the
multiplicity-2 factor has `kappa = 0` (exactly average) and the three multiplicity-1 discs
have `kappa < 0` (bounded sinks), so only the three multiplicity-3 discs charge and the sum
is `3*3 = 9 in Z` — **R063 would survive**. The whole kill is that one rule. It is doubly
grounded: `kappa = 0` at `a = P/Q` also degenerates the successor to `delta_fin = H`, which
is neither a final major (`delta < H`) nor a final minor (`delta > H`) disc. But it is a
single point of failure the frozen report does not flag. (The parallel six-rows lane reaches
the same `9` independently — a corroboration, not a novelty for the campaign.)

**Packets and the sum.** `rho_P = 2a`, `rho_Q = 3a` (Def 5.1(1)): `(10,6,6,6)` and
`(15,9,9,9)`, exhausting `28 = m'` and `42 = n'`. The same four `P'`-counts fall out of the
charged `inverse_top(112,4,56,1,3,3/10,12,(3,))` from the parent pattern
`pi^12(pi^10-c)^3`, with `W0 = 5` — an independent confirmation of `z = 5`. All four
multiplicities exceed the threshold 2, so Prop 5.3 carries each to `D'_1`; the reduced final
degrees `2a in {6,10} > 1` meet Xu's finality requirement, and the `r=1` constant `D` makes
the leading polynomials squarefree and disjoint. With `lambda_2 = -1/3`, `W = 70`,
`kappa(a) = 14(a-2)/3`:

```
 zero    a=5: rho=(10,15) kappa=14    delta_fin=13/24  S=35/4  L=1 mod 24 res (10,15) FAIL
 nonzero a=3: rho=(6,9)   kappa=14/3  delta_fin=7/6    S=3     L=3 mod  2 res (0,1) pass (x3)
                        I'_M = 3*3 + 35/4 = 71/4   NOT in Z
```

Both `delta_fin` also come out of Moh's Prop 5.3 formula (§1). The kill is carried by the
**ungated** sum alone: the Galois filter (which would give a certified-empty family) is
redundant, and the result is independent of the coarse-vs-actual stabilizer convention,
since `L = 1` at `D'_2` either way. The charged `check.py`, re-run with the path
redirected to my frozen inputs, passes every internal assertion and returns `{71/4}`,
`{8, 592/29}`, `{8, 146/13}` — matching the report.

**No conflict with orbit transport.** `I'_M = u I_M` is a partial map; the transport gate
itself records that the zero-route sibling has no determined `epsilon`, "exactly where
R063's parent and child values diverge". The transverse suborbit contributes 9 on both
sides (my sensitivity run reproduces that 9) and the parent's own actual-stabilizer value
`1035/59` is likewise non-integral — two independent non-integralities, no contradiction.

## 3. Boundary: what certifies `C(A)`

Hypothesis (3) is met in practice by five artefacts, all present for R063: (i) a finite
(here singleton) own-data family from the correlated first-support routes, with `u_s = 1`
so the child chain is complete, not a prefix; (ii) a finite factor-shape enumeration
bounded by the printed `A_0 | P-z` and `1_{z>0} + A_0k <= Q` (Prop 4.6(3)(4)), plus the
selected-multiplicity and forbidden-average constraints; (iii) forced one-step descent to
index `r-1` at the Prop 5.3 radius, terminating at `r=1`; (iv) **double** root conservation
`sum rho_P = m'`, `sum rho_Q = n'` — the closure certificate, since a further disjoint
packet would exceed a polynomial degree; (v) bounded/order-zero omitted roots, or `Q'-eta`.

**Does the frozen six-rows fixed list meet (3)? It does not need to.** Its verdict is
SURVIVES — the *existential* direction, where one compatible integral member suffices, and
it exhibits several with exact `D(P,Q,p,q) = Cp` witnesses. Exhaustion is required only for
a kill. Where it goes further and calls `I'_M` **forced** (17/22/18) it does supply
(i)-(iv) above, but those rows carry **minor** packets, so (v) — the clause R063 does not
need — is replaced by a minor-floor comparison rather than a boundedness proof. Astra's
`SET-VALUED / OPEN[TRANSPORT-EXHAUSTION]` is therefore more conservative than its own step
7 ("any integral member gives SURVIVES") would give; the reason is legitimate, since those
own records were not charged into its lane, so its step 1 gate cannot run. Both readings leave the rows alive. For the ledger: **the six rows are not
excluded, and no exhaustion claim of theirs is consumed.**

## 4. `u_s >= 2`

**Confirmed: nothing — and a radius proof alone would still not be enough.** Prop 6.4 is
`u_s = 1` by hypothesis and by proof (§1). Hypothesis (2) fails independently: at
`u_s > 1` the retained child chain has `d'_s = u_s > 1`, so a further gcd drop is possible
and the identified prefix has an unidentified terminal part — the frozen instrument returns
`characteristic_scope = "retained prefix only"` and
`top_license = OPEN_CHILD_TERMINAL_IDENTIFICATION` (`descend_own.py:249-258`), and
`def51_radii`'s docstring records that the child version is called only at `u_s = 1`. So `u_s >= 2`
needs **both** a proved `delta*_{s-1} >= v_s/u_s` **and** a certified finite family of full
terminal extensions; the 20 such roster rows are untouched.

## 5. Verdict, FALLACY-v2

Per-step verdicts: header block. **PROMOTABLE**: promote the conditional
LEMMA [CHILD-INTEGRALITY] and the R063 kill; retain `OPEN[TRANSPORT-EXHAUSTION]` on
R025-R028/R057/R058 and the unrestricted final-cover OPEN. No ledger edits made here.

**FALLACY-v2.** *Floor/attainment*: the kill uses the (CI.5) **equality**; (CI.8) and the
minor floor are audited and never substituted. *Carrier/attainment*: `SURVIVES` is never
read as realisation. *Variable/ring map*: declared, and re-derived by me from p.198 rather
than matched by name. *Prime label/derivative*: disambiguated in the report's first line.
*Pole/interior*: Lemma 4.1 / Prop 4.1 applied only after the disc class (final, major,
`delta < H`) is fixed. No `sat()`, no remainder-degree, no exit-price assertion. The
one item I add to the record is §2's single-point-of-failure structure.

<!-- BODY-END -->
