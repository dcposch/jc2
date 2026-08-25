# Hostile different-model review — B9 fixed-D12 leading shear/order-one/Q8 interface V2

| Field | Value |
|---|---|
| Producer | `xmodel/as-b9-max12-leading-shear-q8-interface-audit-v2-20260825.md` (SHA-256 `82c701474a9d1605097910f7947deb99d70908934fa93d26a73103b4b2440e40`) |
| V1 negative control only | `xmodel/as-b9-max12-leading-shear-q8-interface-audit-20260825.md` (SHA-256 `9f7eb4bfd61aa5ecd61a9f53939327c2ec268956e45eac2885d78b82832ce56a`) |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED** |
| Source typing | **CONFIRMED** |
| Wording / scope | **CONFIRMED.** No sentence is stronger than the eight charged items once the `(9,12)` / nonautomorphic quantifiers already in §§2–3 are read onto the later summary sentences |
| Mathematical defects | none |
| Reviewer / model | Grok 4.6 (xAI) |
| Evidence | source reading and hand algebra: Jacobian dehomogenization of equal-degree binary forms; B9/B8 residue expansions; frozen mod-`3^11` face coefficients from the already-reviewed quadratic witness; history-stop G-route of `(10,12)`/`(11,12)`; Kummer-preflight identities; selected-Q8 `p=1` divided-row compiler. No local CAS, solver, Lean, Jacobian replay, or AWS job |
| Git HEAD | `d0f6edfbfcd8fbe4c77ffadcd336df349c11eb7e` |
| Review window | 2026-08-25 |

V1 was read only as a negative scope control. Its degree-three `h_one`/`h_three` pair is not used below and is not repaired.

## Verdict

**CONFIRMED**

An exact fixed-total-D12 Keller pair over a finite extension of `Q_3`, reducing to B9, is a strictly stronger object than any finite congruence family. For such a pair the degree-22 row is `J(P12,Q12)=0`; in characteristic zero two nonzero binary forms of degree 12 are then proportional, the unique scalar is the unit `y^12` ratio and lies in `3O`, and the target shear `(P-cQ,Q)` is integral, determinant-preserving, the identity modulo three, and kills the whole degree-12 face of `P`. The displayed mod-`3^11` witness has that ratio `c=27702` and a nonzero `(x^3 y^9)` residual `59049`, so that one point is not an exact-lift representative; the complete `3^183` family is untouched. After the shear, conditional on a nonautomorphic exact lift, the reviewed partial-`y` maximum-12 routing retains only the broad cell `(9,12)` and does not choose the strict total-degree box. On that cell the identities `a9=h^3`, `b12=h^4` plus `deg_total(Q)<=12` force `h` constant, hence Kummer order one after the licensed scalar extension; the B8 analogue is the same cap on `a8=h^2`, `b12=h^3`. The selected corrected-Q8 source is an order-three `p=1` divided-row chart that refuses the order-one core; neither the `p=q=0` degeneration nor denominator clearing licenses a B9 specialization into it. The only claimed bridge is complete-family leading-face incidence, the integral shear, and an original-row order-one common-core compiler.

## Strongest exact claim

Conditional on an exact algebraized fixed-D12 B9 lift, the leading-face target shear exists, is integral, and routes every nonautomorphic such lift onto the broad partial-`y` `(9,12)` cell with trivial partial-`y` Kummer class. The selected order-three corrected-Q8 source is then a scope conflict. No all-depth point, common-cubic solution, maximum-twelve theorem, or JC2 conclusion is included.

## Sharpest non-claim

A conditional routing theorem about an exact lift that the frozen congruence families do not supply. Not emptiness or nonemptiness of the `3^183` leading-face incidence, not a `Z_3` point, not exclusion of the order-one core, not a common-cubic or common-quartic classification, not a B8 settlement, not Taylor/terminal, not maximum twelve, not a counterexample, and not JC2.

---

## Charge 1 — Conditional scope

**CONFIRMED**

Section 1 writes the hypothesis as an exact pair

```text
P,Q in O[x,y],                    det J(P,Q)=1,
deg_total(P),deg_total(Q) <= 12,
(P,Q) mod 3 = (u-u^3, y+u^4),     u=x+y^3,
```

with `O` the valuation ring of a finite extension of `Q_3`. The next sentence is the firewall: this is a statement about an exact lift, and the frozen finite congruence families do not supply one.

That typing is correct and load-bearing. The producer-exact `3^183` family at modulus `3^11` is a finite `F_3`-digit parameterization over one B9 mod-243 parent (quadratic review SHA `19198646…`, cardinality as a digit count, honest degree pairs `(12,12)`). A point of that family is not an element of `O[x,y]` with Jacobian identically 1. The V2 note never treats it as one, except as the negative control in Charge 4.

V1’s weaker opening (no explicit `deg_total <= 12` in the displayed hypothesis, though the prose is a D12 shear) is superseded. Nothing in V2 repairs or consumes V1’s later order-one/order-three ambiguity.

No missing hypothesis. The finite families are correctly excluded.

## Charge 2 — Equal-degree proportionality

**CONFIRMED**

If both top faces have exact total degree 12, the degree-22 summand of `det J(P,Q)-1=0` is the homogeneous identity `J(P12,Q12)=0`. Write `P12=y^{12}a(x/y)`, `Q12=y^{12}b(x/y)`. Direct expansion:

```text
P_x = y^{11} a',     P_y = y^{11}(12 a - t a'),
Q_x = y^{11} b',     Q_y = y^{11}(12 b - t b'),
```

hence

```text
J(P12,Q12) = 12 y^{22}(a'b - a b').
```

The displayed “nonzero scalar multiple” is this factor `12`. Over `Frac(O)` one has characteristic zero, so `12≠0`. The polynomial ring is a domain, so `J=0` forces the univariate Wronskian `a'b-ab'=0`. In characteristic zero, `W(a,b)=0` with `b≠0` implies `a/b` constant as a rational function, hence `P12=c Q12` as forms.

Attacks:

- **Zero faces.** If `Q12=0`, the unit `y^{12}` coefficient of Charge 3 is false, so this case is excluded by the B9 residue. If `P12=0`, then `c=0` still satisfies (2.2) and the shear is the identity; the note’s “two nonzero” clause is the interesting case, not a gap. If both vanish, the unit `y^{12}` coefficient of `Q` again forbids it.
- **Characteristic.** In characteristic 2 or 3 the prefactor `12=4·3` vanishes and `J=0` does not force `W=0`. That is exactly why a mod-3 (or even mod-`3^{11}`) solution can have a non-proportional degree-12 face; see Charge 4. The hypothesis is a characteristic-zero pair, so the implication holds. The note does not display the `12`, but it does not need a further characteristic hypothesis beyond §1.
- **Dehomogenization / the line `y=0`.** The identity `J=12 y^{22} W(a,b)(x/y)` is a polynomial identity in `x,y`, not a statement on the chart `y≠0`. Setting `y=1` recovers `W` as a univariate polynomial. Homogeneous proportionality on `A^2` is equivalent to proportionality of the dehomogenized binary forms. The opposite chart `P12(x,0)=p_{12}x^{12}`, `Q12(x,0)=q_{12}x^{12}` is included: a unit `y^{12}` coefficient is `b(0)` a unit, so `Q12` is not supported only at `y=0`.
- **Characteristic-`p` Wronskian kernel.** In characteristic `p` one has `W=0` iff `a/b` lies in the subfield of `p`-th powers, not necessarily in the constants. That kernel is absent in characteristic zero.

Thus (2.2) holds for a unique `c∈Frac(O)` whenever both faces are nonzero of degree 12. No counterexample.

## Charge 3 — Unique integral scalar and target shear

**CONFIRMED**

B9 residue, expanded in characteristic three:

```text
u = x+y^3,
P ≡ u-u^3 ≡ x+y^3-x^3-y^9,
Q ≡ y+u^4 ≡ y+x^4+x^3 y^3+x y^9+y^{12},
```

using `C(4,1)≡1`, `C(4,2)≡0`, `C(4,3)≡1` and `u^3≡x^3+y^9`. So:

- the `y^{12}` coefficient of `Q` is `1` modulo three, hence a unit of `O` for any exact lift;
- every total-degree-12 coefficient of `P` vanishes modulo three, because `P` has total degree nine on the special fibre.

The unique `c` of (2.2) is the ratio of the `y^{12}` coefficients. The denominator is a unit and the numerator lies in `3O`, so `c∈3O`. Uniqueness in `Frac(O)` is the ratio; uniqueness in `3O` is the same ratio plus the unit denominator.

The target operation `(P,Q)↦(P-cQ,Q)` is the elementary automorphism of the target with matrix `[[1,-c],[0,1]]`. It therefore:

- preserves `O[x,y]` because `c∈O`;
- preserves `det J=1`;
- is the identity modulo three because `c∈3O`;
- kills the whole degree-12 face of `P` by (2.2);
- is invertible on the target, so it preserves any actual injectivity or noninjectivity of the map.

The note’s restriction of current evidence to a special-fibre collision is correct and is not a characteristic-zero collision claim.

The same unit `y^9` coefficient of `P` survives the shear: `P_{(0,9)}≡-1` and `c∈3O`, so `[y^9](P-cQ)` remains a unit modulo three, independently of `[y^9]Q`.

## Charge 4 — Exact displayed-witness failure

**CONFIRMED**

The frozen quadratic witness is the zero-active point of `cases/as_b9_max12_full_fibre_quadratic_3p11_20260825/AWS_BOX02_V4/result.json`, already independently degree-read in the quadratic review. Homogeneous degree-12 faces, reduced modulo `177147=3^{11}`:

| monomial | `P` | `Q` |
|---|---:|---:|
| `y^{12}` | `27702` | `156736` |
| `x y^{11}` | `118098` | `18063` |
| `x^2 y^{10}` | `0` | `8505` |
| `x^3 y^9` | `59049` | `10692` |
| `x^4 y^8` | `0` | `118098` |

`Q_{(0,12)}=156736≢1`, but `156736-1=156735=3^6·215` and `v_3(27702)=6`, so

```text
27702 · 156736 ≡ 27702  (mod 3^{11}).
```

The unit-coefficient ratio is therefore `c=27702` modulo `177147`, even though the `Q` leading coefficient is not 1. Independently, `v_3(10692)=5`, hence `c·Q_{(3,9)}` has valuation `11` and vanishes modulo `3^{11}`, and the residual is

```text
P_{(3,9)} - c Q_{(3,9)} ≡ 59049  (mod 177147).
```

`59049=3^{10}≠0` modulo `3^{11}`. The same valuation arithmetic makes the `(0,12)`, `(1,11)`, `(2,10)`, and `(4,8)` residuals vanish, so the only surviving degree-12 obstruction on this point is the charged `(x^3 y^9)` slot. That is enough: this representative does not satisfy (2.2), so it is not the reduction of an exact all-depth pair of total degrees `(12,12)`.

It is one digit tuple in a displayed parameterization of cardinality `3^{183}`. A single failed point is not a family incidence theorem. The note states this and does not promote it.

No Jacobian of the 276-row determinant was recomputed; the face table is a reading of stored supports plus schoolbook 3-adic valuations.

## Charge 5 — Broad-cell-only landing

**CONFIRMED**

After (2.4), `P` has total degree at most 11 and a unit `y^9` coefficient, while `Q` is unchanged and retains partial `y`-degree 12. Actual partial-`y` pairs compatible with those bounds are `(9,12)`, `(10,12)`, and `(11,12)`. Extra `y^{10}`/`y^{11}` terms of `P` may be nonzero in characteristic zero and still vanish modulo three.

The imported routing is the reviewed partial-`y` history stop (`xmodel/as109-partial-y-history-stop-20260824.md`, SHA `6994dd6b…`), as restated by the Kummer preflight (SHA `30cb45cc…`) on the maximum-12 row:

| pair | route |
|---|---|
| `(11,12)` | `G`, gcd one, every `H` |
| `(10,12)` | `G`, gcd two: `gcd(H,2)∈{1,2}` for every `H` |
| `(9,12)` | primitive, residual exactly `3|H` including `H=0` |

The `G` arrow is the large triangular source shear `σ_L(x,y)=(x,y+x^L)` followed by Nagata’s repaired prime-total-gcd theorem (`g=1`) or the Guccione–Guccione–Valqui `2p` theorem (`g=2`). Those theorems conclude automorphy. The note therefore correctly conditions on a **nonautomorphic** exact lift before discarding `(10,12)` and `(11,12)`. It does not import the `(6,9)` maximum-eleven composition as a closer of those pairs (that composition concerns `max(deg_y)≤11`, which `(10,12)` and `(11,12)` violate). It does not claim a maximum-twelve automorphy theorem.

The surviving cell is the **broad partial-`y` cell** `(9,12)`: `deg_y P=9`, `deg_y Q=12`, with `deg_total P≤11` still allowed. The note’s next sentence is the required firewall: this does not choose a Kummer class and does not choose the stricter total-degree-`(9,12)` normalized box (55+91 variables, `deg_total P≤9`). Section 5 later names that stricter box only as a successor compiler stratum, honestly, not as a consequence of the routing.

No silent inference to the strict box. No missing hypothesis beyond the nonautomorphic exact-lift condition already written.

## Charge 6 — Fixed-D12 Kummer collapse

**CONFIRMED**

On actual `y`-degrees `(9,12)`, history (1.1)–(1.2) and the preflight table give, after harmless nonzero constant scalings,

```text
a9(x)=h(x)^3,       b12(x)=h(x)^4,
```

with `h∈k[x]` and Kummer class in `k(x)^*/k(x)^{*3}`. The leading-row identity `12 a9' b12 - 9 a9 b12'=0` is all that is used.

`Q` still has total degree at most 12, so the coefficient of `y^{12}` cannot involve a positive power of `x`. Combined with the unit `y^{12}` coefficient, `b12` is a nonzero constant. Then `h^4` is a nonzero constant. Unique factorization in `k[x]` (or valuation of a reduced rational function) forces `h` itself to be a nonzero constant. The Kummer preflight already licenses a finite scalar extension containing roots of unity and, on the trivial class, absorption of constants; adjoining a cube root of that constant makes

```text
[h]=1 in k(x)^*/k(x)^{*3}.
```

So `H=deg_x h=0`. The residual `3|H` still holds because `gcd(0,3)=3`, and it does not make the class nontrivial. On `e=1` the depression mismatch `delta` is weight-unforced, matching the preflight table.

Even without writing perfect powers: `b12` constant implies `b12'=0`, hence `a9'=0` from the leading row, so `a9` is constant as well. The common-core language is then only a packaging of two constants.

V1’s pair `h_one=-(1+3x)^3` and `h_three=-(1+3x^3)` both have `deg_x h=3`. Then `b12=h^4` would have `x`-degree 12 and `Q` would contain `x^{12} y^{12}`, total degree 24, contradicting D12. Those controls are correctly declared inapplicable. They are not used.

**B8 analogue.** The residue `G8=(y+u^2,u^3-u)`, `u=x+y^4`, has actual partial-`y` degrees `(8,12)` and unit leading `y` coefficients `(1,1)`. On that cell the preflight writes `a8=h^2`, `b12=h^3`. The same total-degree cap makes `b12` a nonzero constant, hence `h` constant, hence order one in `k(x)^*/k(x)^{*4}` after the same licensed scalar extension (now a fourth root of the constant, or absorption into a monic core `h=1`). Order-two and order-four leaves are therefore empty for any exact fixed-D12 lift that actually occupies the `(8,12)` identities. The note does not claim that every B8 lift is already on `(8,12)` after a shear, and Section 6 explicitly refuses to settle B8. That is the right strength.

**Partial-`y` `h` versus homogeneous `K`.** On the *strict* total-degree `(9,12)` stratum the top faces satisfy `P9=a K^3`, `Q12=b K^4` for a homogeneous binary cubic `K`. The coefficient of `y^9` in `a K^3` is `a` times the cube of the `y^3` coefficient of `K`, hence a constant whenever `h` is constant, even if `K` has `x`-terms. Those `x`-terms live in lower `y`-degree coefficients. The B8 homogeneous quartic is analogous. Fixed-cap Kummer order one does not solve that incidence and does not kill any lower determinant row. The note states this and does not conflate the two cores.

No missing hypothesis. The collapse uses only the reviewed leading-coefficient identities plus the total-degree cap already in §1.

## Charge 7 — Selected-Q8 scope conflict

**CONFIRMED**

The selected corrected-Q8 source, as compiled in the global-quotient gate (SHA `2102e5d7…`) and consumed by the selected-contact theorem, is:

- the **order-three** `(9,12)` leaf, not the polynomial core;
- the geometric chart `p=1`, `K=z^3+z+q`;
- loads `k=mu=0`, `nu≠0`;
- the six divided rows `r1/t, r3/t, r5/t, r7/t, r2, r4` in `(w,c,d2,d4,x1,x3,x5)`, with `t=x0`, `w=t^2`.

The selected-contact theorem’s refusal list includes the order-one / polynomial core; that source does not contain the leaf Charge 6 lands on. This is already a scope conflict, independent of reduction type.

**`p=q=0` degeneration.** The B9 special-fibre leading pair is `(-y^9,y^{12})=(-(y^3)^3,(y^3)^4)`, the monomial cubic `K=y^3`. In depressed approximate-cubic coordinates that is `p=q=0`. An exact lift may fatten `p` into `3O`, but the residue forces `p≡0 (mod 3)`, so `p` is never a 3-adic unit. Normalizing a nonzero `p` to 1 uses `λ^2=p` and divides remaining coefficients by powers of `λ`. At `v_3(p)>0` this is ramified and nonintegral; at `p=0` it is impossible. So there is no integral horizontal map from the B9 coefficient scheme onto the `p=1` open, even if one ignores the Kummer-class mismatch.

(The varying homogeneous cubic of Charge 6 does not repair this: its `p` still reduces to 0.)

**Denominator clearing.** The source-honest undivided rows are `r1,r3,r5,r7,r2,r4`. Restoring them multiplies each odd quotient row by `t`. On `t=0` those products acquire the whole `t=0` divisor and do not imply the divided equations. Clearing powers of 3, Kummer roots, or source scalings that are units only in the characteristic-zero normalized chart likewise enlarges the special fibre past the selected `p=1` scheme. None of these operations is a specialization into the selected source.

B9 reduction also does not force the exact loads `k=mu=0`, `nu≠0`, either Taylor family, or the terminal row. Congruence modulo three would not replace those equalities.

The boxed verdict

```text
integral degree-12 target shear:                     PASS;
conditional broad partial-y (9,12) landing:          PASS;
fixed-D12 Kummer landing:                            ORDER ONE;
selected order-three corrected-Q8 landing:           SCOPE-CONFLICT.
```

is therefore not a euphemism for “order unknown”. It is the correct interface statement.

## Charge 8 — Successor honesty and refusal scope

**CONFIRMED**

Section 5 proposes exactly two family-level stages:

1. On the complete broad B9 family, impose every coefficient of `P12-cQ12=0` with `c` solved from the unit `y^{12}` coefficient. Only a complete incidence result may replace the failed displayed witness.
2. Apply the target shear familywise. On the *strict* total-degree-`(9,12)` stratum, impose the homogeneous common-cubic equations and compile the order-one polynomial-core lower system from the original, denominator-free determinant rows, splitting the cubic by the three binary root-multiplicity types `L^3`, `L^2 M`, `LMN` before large elimination.

The B8 analogue is the same order-one logic with the common homogeneous quartic and its cross-ratio / multiplicity strata. No generic order-three Q8 substitution is licensed.

This is the charged bridge and nothing else. Section 5 does not run a divided generic substitution, a Taylor reconstruction, a terminal row, an all-depth existence argument, a counterexample, a maximum-twelve theorem, or JC2.

Section 6’s refusal list matches: the note does not show the complete B9 leading-face incidence empty or nonempty, construct an all-depth `Z_3` point, exclude the order-one core, solve the common cubic, settle B8, land any Taylor/terminal system, prove maximum twelve, construct a counterexample, or resolve JC2.

## Sentences checked against the eight items

Read against the eight charges, the following sentences look strongest and are still in bounds.

| Sentence | Why it is not stronger |
|---|---|
| Status: “ORDER-ONE LANDING” | Kummer class of the partial-`y` core on the cell of Charges 5–6, not a Q8 or compiler landing |
| “every exact fixed-D12 B9 candidate lies on the order-one polynomial-core leaf” | Quantified by §2’s nonautomorphic condition and by §3’s opening “on the reviewed `(9,12)` partial-`y` route”; automorphic `(10,12)`/`(11,12)` lifts are G-closed and are not counterexample candidates |
| “the selected corrected-Q8 source cannot contain it” | Charge 7, not emptiness of that source on its own leaf |
| “the B8 seed cannot occupy its order-two or order-four Kummer leaves” | Charge 6 analogue on the `(8,12)` identities; §6 refuses to settle B8 |
| “preserves any actual injectivity or noninjectivity already known” | Invertible target operation; the note immediately denies a characteristic-zero collision |
| §5 “on the strict total-degree-`(9,12)` stratum” | Named successor compiler, not a routing inference; Charge 5’s firewall in §2 is intact |
| Boxed `SCOPE-CONFLICT` | Interface typing, not a selected-Q8 trajectory theorem |

No sentence asserts an all-depth point, a family-empty incidence, a solved common cubic, Taylor/terminal landing, maximum twelve, a counterexample, or JC2.

V1’s ambiguity claim is named, confined to the unbounded-total `(9,12)` cell, and forbidden as a B9-interface input. This review does not repair it.

## Mathematical defects

None.

## Non-blocking exposition notes

1. Charge 2’s scalar is `12`, not an unspecified unit. Displaying it would make the characteristic attack visible on the page. The hypothesis already supplies characteristic zero, so this is not a missing implication.
2. `Q_{(0,12)}≡156736` on the frozen witness, not `1`. The ratio `c=27702` is still correct by the valuation identity of Charge 4; a parenthetical `Q_{(0,12)}≡1 (mod 3^6)` would have blocked a false “they forgot to invert” objection.
3. The B8 paragraph is thinner than the B9 shear (no separate equal-degree face analysis). It is correctly scoped to the reviewed `(8,12)` identities plus the total-degree cap.
4. “Reviewed maximum-12 degree routing” does not repeat the history-stop SHA. The content used is the G-route of `(10,12)` and `(11,12)`, which is the right object.

None of these changes an identity or licenses a broader claim.

## Promotion

**Accept `CONDITIONAL ON AN EXACT FIXED-TOTAL-D12 KELLER PAIR OVER A FINITE EXTENSION OF Q_3 REDUCING TO B9: THE DEGREE-22 ROW FORCES P12=c Q12 WITH UNIQUE c IN 3O; THE TARGET SHEAR (P-cQ,Q) IS INTEGRAL, DETERMINANT-PRESERVING, THE IDENTITY MODULO THREE, AND REMOVES THE DEGREE-12 FACE OF P. THE DISPLAYED MOD-3^11 WITNESS HAS c=27702 AND (x^3 y^9) RESIDUAL 59049≠0, SO THAT POINT IS NOT AN EXACT-LIFT REPRESENTATIVE; THE COMPLETE 3^183 FAMILY IS NOT KILLED. AFTER THE SHEAR, A NONAUTOMORPHIC EXACT LIFT LANDS IN THE BROAD PARTIAL-y CELL (9,12) AND NOT IN THE STRICT TOTAL-DEGREE BOX. THERE a9=h^3, b12=h^4 TOGETHER WITH deg_total(Q)≤12 FORCE h CONSTANT AND KUMMER ORDER ONE AFTER THE LICENSED SCALAR EXTENSION; THE B8 ANALOGUE ON a8=h^2, b12=h^3 IS THE SAME CAP. THE SELECTED ORDER-THREE p=1 DIVIDED-ROW CORRECTED-Q8 SOURCE CANNOT RECEIVE THIS LIFT. THE ONLY LICENSED SUCCESSOR IS COMPLETE-FAMILY LEADING-FACE INCIDENCE, THE INTEGRAL SHEAR, AND AN ORIGINAL-ROW ORDER-ONE COMMON-CORE COMPILER.`**

**Refuse `FINITE CONGRUENCE FAMILY AS AN EXACT LIFT`, `FAMILY-EMPTY LEADING-FACE INCIDENCE`, `V1 ORDER-ONE/ORDER-THREE AMBIGUITY AS A B9 INTERFACE INPUT`, `STRICT TOTAL-DEGREE (9,12) BOX AS A ROUTING CONCLUSION`, `CONFLATION OF PARTIAL-y h WITH THE HOMOGENEOUS CUBIC/QUARTIC K`, `INTEGRAL OR DIVIDED SPECIALIZATION INTO SELECTED Q8`, `TAYLOR/TERMINAL`, `ALL-DEPTH / Z_3`, `MAXIMUM TWELVE`, `COUNTEREXAMPLE`, and `JC2`.**
