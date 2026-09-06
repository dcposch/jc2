**HOSTILE GATE — ACTUAL-STABILIZER SCREEN — Astra — 2026-09-06**

**VERDICT: CONFIRMED-WITH-FIX.** Lemma A's denominator assertion and the screen's
necessity are proved below. Independent replay gives **24,063 -> 1,420 coarse ->
90 actual**, with **20 -> 6** at n<=100 and exact equality of the six source keys
with p.202. **90 may replace 1,420 as the stronger screen's population**, for
normalized minimal counterexamples. It counts necessary configurations, not pairs.
Fixes concern the printed field notation, an ODE display, prefix versus centre,
and the calibration's interpretation; none changes 90.

**1. Custody and scope.** Before mathematical reads, `awk` joined the receipt's
nine numbered `_basename`/`_sha256` fields into the own box directory's
`inputs.sha256`; `sha256sum -c` returned **9/9 OK**. Reads used the frozen
`/tmp/jc2-lane.rMB50I/inputs`, and the named `.run.v2` receipt. No sub-agents,
ledger edits, jc2-lean, ideation inputs, or uncharged operative implementation.
The frozen skeleton was executed only as a comparison after my own computation.

All requested Moh pages were inspected as images from the frozen PDF; printed
page = PDF ordinal + 139. Additional images: pp.141, 146, 147, 185, 205–206, for notation,
the top window and ODE. Renderings and navigation OCR are temporary files.

The theorem concerns a non-coordinate unit-Jacobian pair, minimal in degree sum,
in Moh's FS presentation: `deg g=deg_y g=n`, `deg f=m<n`, `M_1=-m`, `M_s=n-2`,
`delta_s=-1`. Degree-reduction exclusions require minimality; they are not
transferred to descendants with Jacobian `x^ell`.

**2. The field sentence.** Equation (8), p.201, defines coarse
`L=lcm(den delta_s,...,den delta_r)`, `A_{r-1}=den(L delta_{r-1})`.
Def.5.1(4), p.179, contains no L: its unique general point is
`sigma_i=c_i+pi t^{delta_i}`, invoking Prop.4.6. The coefficient sum does not
declare its indices integral.

The frozen report overlooks a notation defect: p.141 defines `k<<t>>` as the
entire Puiseux field `union_N k((t^{1/N}))`. Thus `k<<bar t>>=k<<bar t^A>>`;
a nonidentity automorphism of the former **over the latter** is impossible.
The report's equality `k<<bar t^A>>=k((t^{1/L}))` is literally false.

Use the finite Laurent extension `k((bar t))/k((bar t^A))`, `bar t^{LA}=t`,
whose base is `K_L=k((t^{1/L}))`; p.188 likewise uses Laurent parentheses.
For `c_j in K_L`, `A=den(L delta_j)`, the integer `a=LA delta_j` satisfies
`gcd(a,A)=1`. The action sends `sigma_j(pi)` to `sigma_j(omega^a pi)` and fixes
t and the coefficients of `g,T_i^psi in k[t^{-1}][y]`.

L supplies the field containing the centre and defines A in (9)–(13). No separate
Def.5.1 requirement inserts radius monomials having zero coefficients. Paragraph 5
proves the bottom at this smaller field. This strengthens (8); it does not change
its literal definition or identify Moh's historical program.

**3. Independent Lemma A: exact denominator lattice.** Write `c_i` for the
canonical common truncation strictly below `delta_i` of roots in `D_i`
(Def.1.3, p.146; p.147 opening paragraph), and put

```
Lcal_i = lcm{den(delta_j): i<j<=s and C_j != 0},     lcm(empty)=1.
```

The support-denominator lcm of c_i is exactly `Lcal_i`. This does not assert that
every fractional exponent occurring is itself a recorded radius.

Proof: take a finite `K_N=k((t^{1/N}))` containing all roots and radius monomials.
Its Galois group acts diagonally on exponents. The note after Def.5.1, p.179,
makes D_s the minimal disc of a Galois-invariant root set, so its common
truncation belongs to `k((t))`: initial lattice 1. In the normalized setting
`c_s=0`: a g-root of order below -1 would make y^n uniquely lowest-order in g.

Inductively assume `c_r in K_L`, with L exactly the accumulated nonzero-radius
lcm. The first display of Prop.5.3, p.180, defines the **prefix**
`tau=c_r+C_r t^{delta_r}`. Set `L'=L` if `C_r=0`, otherwise
`L'=lcm(L,den delta_r)`. The subgroup fixing `K_{L'}` fixes tau. It permutes the
roots of the correct level-dependent polynomial
`G_r=g product_{i=1}^r T_i^psi` and preserves the strict inequality
`ord(xi-tau)>delta_r`. Hence it permutes exactly the packet in Prop.5.3's min
display. That packet's minimal disc has radius `delta_{r-1}`; all packet roots
have the same truncation below this radius. The subgroup therefore fixes that
truncation `c_{r-1}`, proving `c_{r-1} in K_{L'}`.

A new gap denominator would thus produce two roots of this packet parting before
its minimal radius. The argument uses the correct G_r at each step, not an
unchanged product of all higher quasi-roots after they have left the packet.

For equality, every selected nonzero term at `delta_j`, j>i, is an actual term
of c_i: radii strictly increase down the tower and later truncation preserves
earlier coefficients. Thus their denominator lcm divides the support lcm. The
proved containment gives the opposite divisibility. This proves exactness and
identifies the centre stabilizer as `Gal(Puiseux/K_{Lcal_i})`.

**Zero-factor qualification.** `C_r=0` adds no term at `delta_r` and cannot
enlarge the lattice through intervening a_j terms. But tau is only a prefix:
later terms on the old lattice are not excluded. Thus unchanged stabilizer does
not mean unchanged centre. Nor does “no lattice enlargement” mean “affinely
removable”: a nonintegral exponent already on the old lattice fails the latter.
The code correctly keeps these separate.

**4. Internal clauses and printed locators.** At j>=2, write
`P=V_{j+1}d_j/d_{j+1}`, `Q=V_{j+1}(n-M_j)/d_{j+1}`,
and `A=den(Lcal_j delta_j)`. Prop.4.6(1), p.170, gives
`g_sigma=c p(pi)^{n/d_j}`, `deg p=P`. The centre action makes the root multiset
invariant: every nonzero root has orbit size exactly A and constant multiplicity;
zero is fixed.

| Clause | Necessary assertion and printed line |
|---|---|
| (10), nonzero selected root | `A V_j<=P`, or `V_j<=floor(P/A)`; p.201(9),(10), the line specifying `pi-a`, a nonzero. |
| (11), zero selected root | If b is its multiplicity, `b congruent P mod A`, with `0<=b<=P`; p.201(11), the following line specifying the factor pi. No division of b by A is imposed. |
| Orbit enumeration | `b=P mod A, P mod A+A,...,P`; nonzero multiplicities form an arbitrary multiset with sum `(P-b)/A`. This exhausts the root multiset of the preceding action. |
| Root-count cap | `1_{b>0}+A*(number of nonzero orbits)<=Q`; p.170 conclusions (2),(3),(4): q has degree Q, is squarefree, and contains every root of p. Also p.200 Theorem(6). |
| Per-factor ODE | `P != Qv` for every positive multiplicity, including b when b>0; p.171 equation (6) and p.205 A.3, derived explicitly below. |
| Every major sibling extends | `v>d_j/(n-M_j)` invokes Prop.5.3, p.180, first hypothesis and last conclusion; p.200 Theorem(4),(7) supplies extension and at least one major. Each sibling receives its own selected coefficient and L update. |
| Minor sibling handling | `v<=d_j/(n-M_j)` is the minor case, p.190's split and Prop.6.1 hypothesis. It is not subjected to major descent or the major-path danger rejection. |

For the ODE, define derivatives with respect to pi, as in p.203's display
`D(a,b,p,q)=a p q'-b q p'`. Let
`h=(-mu_j+M_j-n)/d_j`, so p.170(2) says `H=T_{j,sigma}=p^h q`.
Substitute `g_sigma=c_0 p^{n/d_j}` in p.171(6) and divide by its nonzero scalar
and common power of p. One obtains

```
p H' - (-mu_j/d_j) p' H = c_1 p^{h+1},
P p q' - Q p' q = c_2 p,                 c_1 c_2 != 0.
```

This uses the r>=2 equation, not Prop.4.6's separate r=1 sentence. There is an
additional printing defect: p.171's “can be simplified” display puts the weights
`P(-mu_j/d_j), P` in the opposite order from the order required by (6) and the
definition of D. The substitution above repairs it without assuming the desired
conclusion. At a p-root a of multiplicity v, q has a simple zero, and division by
the leading term at a gives `(P-Qv)q'(a)=c_2 !=0`. This proves the per-factor
test, including the zero factor; it is independent of the choice of modulus.

**5. Bottom (12)/(13) at the actual field.** Set
`G=g_{sigma_1}`, `F=T_{1,sigma_1}`, with degrees
`a=(n/d_2)V_2`, `b=(m/d_2)V_2`. Def.5.1(4) and the r=1 sentence of Prop.4.6,
p.170, give their nonzero-constant differential equation. The two coprimality
conditions are displayed at the foot of p.187; p.207 A.5 also states that GF has
only simple roots. In particular G,F cannot both vanish at a point, and their
derivatives cannot both vanish there, by their differential equation.

The action at `A_1=den(Lcal_1 delta_1)` makes G and F eigenpolynomials: their
nonzero coefficient degrees are congruent to a and b, respectively, modulo A_1.
For A_1>1, if both residues were nonzero, G(0)=F(0)=0, impossible. If both were
zero, G'(0)=F'(0)=0, impossible. If one residue is zero, its derivative vanishes
at zero; the other derivative must be nonzero, forcing the other residue to be 1.
Therefore `(a,b) mod A_1` is `(0,1)` or `(1,0)`, exactly p.201(12)/(13).
For A_1=1 both divisibility alternatives are automatic.

This proof does not assume the special s=2 formula used on p.188 to derive
`A | (n*+m*)V_2-1`. It supplies the general-level argument directly at the smaller
centre field. In particular there is no hidden demand to restore coarse L at the
bottom, and both alternatives must be retained.

**6. Prop.5.6 and the zero case.** The statement on p.188 excludes
`sigma_1=pi t^{delta_1}` for a minimal non-coordinate pair: it would be a coordinate
pair or admit simultaneous degree reduction. Its p.189 proof uses the unit
Jacobian and the normalized conditions. Its p.190 application explicitly removes
`a t^{-1}+b` by `x->x, y->y-ax-b`.

If every selected coefficient on a path is zero or occurs at an integral
`delta<=0`, then Lcal stays 1. Lemma A makes the final centre integral even in
all gaps. Normalized roots have order >=-1, and Def.5.1 gives `delta_1<1`, so the
centre is precisely of the removable form `a t^{-1}+b`. Conversely an earlier
nonzero nonintegral coefficient persists and cannot be removed by this affine
translation. Thus the Boolean update
`danger_next=danger and (zero or (den(delta)=1 and delta<=0))`
and rejection of a still-dangerous major bottom are necessary. An isolated zero
choice after earlier fractional support is allowed. “Zero factor” does not mean
“zero centre” unless the earlier support has also been accounted for.

**7. Existential patterns.** A realizing pair supplies its root multisets,
zero/nonzero choices, and continuations at **every** major factor. Lemma A gives
each node's modulus. All its data pass the proved conditions, so induction down
the finite tower supplies a passing pattern containing the specified source path.
Rejecting only if **every pattern fails** cannot reject such a pair's row.
Independently allowed coefficient or sibling choices may add false positives;
acceptance does not assert realization. Checking only one path is insufficient.

Also `Lcal_j | L_j(coarse)` implies `A_j(coarse) | A_j(actual)`. Actual orbits
split into smaller coarse orbits without changing root mass; bottom divisibilities
weaken. Thus actual acceptance implies coarse acceptance, licensing the coarse
census as the outer population.

**8. Independent code.** The own box directory contains `replay.py` and
`controls.py`. The census directly chooses increasing exponents, computes radii
by consecutive ratios of Def.5.1, and enforces strict major/top windows and both
bottom alternatives. It uses Kmin=2 and no height cap. Its 16<=n<=200 loop omits
no eligible smaller row: the remaining constraints force n>=24.

The solver carries level, higher multiplicities, centre L, danger, and a required
source-path flag. It enumerates all b and uses unbounded coin sums for nonzero
orbits, retaining the minimum orbit count at fixed total and major/path flags.
Larger counts are dominated for the upper count bound. There is no cap or timeout
acceptance. Each sibling's own multiplicities determine its radii.

Code locators: `replay.py:62` census; `:109` L update; `:115` tree/bottom;
`:128` factors; `:150` patterns. Separately, `controls.py` checks **90 retained
tree certificates**, including 127 represented bottoms, using the full radius
product formula and direct clause checks without calling the dynamic program.
The frozen skeleton comparison is set equality on all 24,063 keys.

| Population | n<=100 | n<=200 | Height counts at n<=200 |
|---|---:|---:|---|
| Coarse census (1)–(13), relaxed bounded-search caps | 658 | 24,063 | no height cap |
| Coarse whole-tree operative | 20 | 1,420 | s=3:43; s=4:414; s=5:797; s=6:166 |
| Actual whole-tree operative | 6 | 90 | s=3:43; s=4:45; s=5:2; s=6:0 |
| Lost / gained by actual | 14 / 0 | 1,330 / 0 | actual is a subset |

Replay took 29.788 seconds. `results.json` contains all actual/coarse keys,
actual certificates, the 14 excess traces and the census-set digest. Roster hits:
**65/66**; only **R063**, `(168,112;M=(140,160,166);V=(3,21,3))`, drops.
The 64 roster rows excluding R001/R063 remain. The other 25 actual keys are in
the JSON; no finite-pole or Xu removal is applied here.

**9. Calibration and all 14 excess rows.** My independent transcription of p.202
gives the following six `(n,m; M_2..M_s; V_2..V_s)` keys:

```
(64,48; 52,62; 3,3)             (75,50; 55,73; 2,4)
(75,50; 55,73; 3,4)             (84,56; 64,82; 2,3)
(84,56; 72,82; 5,3)             (99,66; 77,97; 8,8)
```

Set equality is on source keys, omitting p.202's ineffective n-1 tails.
At `(75,50;55,73;2,4)`, printed delta_1=1/3 is **2/3** by Def.5.1; the other five
entries agree. The p.207 introduction also misprints `(64,68)` for `(64,48)`.

Here is the full coarse-minus-actual set, grouping only identical M sequences:

| n,m | M_2..M_s | V_2..V_s, one row per alternative |
|---|---|---|
| 90,60 | 10,45,88 | (1,8,4); (3,8,4) |
| 90,60 | 45,80,88 | (2,5,4); (3,5,4) |
| 96,64 | -48,-8,20,94 | (1,1,6,3) |
| 96,64 | 48,68,94 | (1,2,3); (2,1,3); (3,2,3) |
| 96,72 | -60,56,94 | (1,9,3) |
| 96,72 | 36,78,94 | (1,1,5); (1,3,5); (4,3,5) |
| 96,72 | 36,80,94 | (1,9,3); (4,9,3) |

All lie within Moh's n<=100, 3<=s<=5, d_s>=4 scope. Direct actual obstructions:

* First family: level 3 has `(P,A)=(8,35)`, hence is all zero. At level 2,
  `(P,A)=(24,21)` forces, for either listed selection, a zero major of multiplicity
  3 and one orbit of multiplicity 1. That zero major remains dangerous at bottom.
* Second family: the selected V_3=5 is forced zero; the next `(P,A)=(10,14)`
  cannot contain either selected multiplicity 2 or 3, by (10)/(11).
* Third family: the level-4 selection is forced zero; at level 3 the actual
  `(P,A)=(12,77)` cannot contain selected V_3=1.
* Fourth family: selected V_3=1 or 2 forces level-3 pattern `b=2`, one 10-orbit
  of multiplicity 1. The zero sibling is major. Its next `(P,A)=(4,5)` forces
  an all-zero continuation and fails Prop.5.6, regardless of the selected sibling.
* Fifth family: V_3=9 is forced zero, and next `(P,A)=(18,58)` excludes V_2=1.
* Sixth family: selected V_3=1 or 3 forces `b=3`, one 7-orbit of multiplicity 1.
  The zero major sibling has next `(P,A)=(6,7)`, hence an excluded all-zero bottom.
* Seventh family: V_3=9 is forced zero; next `(P,A)=(18,22)` excludes V_2=1 or 4.

Three pass actual selected-path-only checks: first family V_2=1, fourth family
`(2,1,3)`, sixth family `(1,1,5)`. The sibling check removes them.

**10. Calibration corrections.** Fourteen extra rows do not refute coarse (8)
as a necessary condition. They show that this coarse screen does not reproduce
Moh's complete reported program output. Whether his program used the sharper
action or other tests is **historically OPEN**. The proof above, not the match,
licenses the sharpening beyond n=100.

The five descended p.207 rows all pass the **bottom-residue control** for some
zero/nonzero reading. At `(21,14;M_2=16;V_2=2)`, C_2=0 gives `(L,A_1)=(1,6)`
and fails; C_2 nonzero gives `(2,3)` and passes. These rows have Jacobian x or x^2,
so calling them survivors of the full parent screen would wrongly apply Prop.5.6.
`controls.json` explicitly types them as bottom-only checks.

The ancillary “centre_L==1 always keeps 72” needs correction: forcing L=1
**including bottom** gives **12**; forcing it only internally, retaining the final
nonzero-centre update, gives **72**. Both are reproduced. These excessive controls
are not necessary screens. No discrepancy affects 24,063/1,420/90 or the six keys.

**11. FALLACY-v2 and promotion.** Centre, root, coefficient orbit and disc remain
distinct; zero coefficient is not zero centre. No exit price, attainment, floor,
quotient-ring calculation or child terminal identification is asserted. Primes
mean d/dpi; `t=1/x` and coefficient fields are explicit. Major/minor status is
checked before recursion; sibling state uses its own multiplicities.

Promote with the field repair, denominator proof, corrected ODE and calibration
scope supplied here. **90 is citable for the actual-stabilizer screen at n<=200**;
1,420 remains the historical coarse count. No `90 -> 64`, minor pricing or pair
existence is promoted. No mathematical OPEN found here blocks this replacement.

Replay from the workspace root:

```
sha256sum -c box/actual-stabilizer-screen-gate-20260906/inputs.sha256
python3 box/actual-stabilizer-screen-gate-20260906/replay.py --limit 200 --compare-charged
python3 box/actual-stabilizer-screen-gate-20260906/controls.py
```

<!-- BODY-END -->
