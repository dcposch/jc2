# Hostile review — squarefree cubic Poisson/fractional-power recurrence

| Field | Value |
|---|---|
| Producer | `xmodel/sol-max12-912-squarefree-poisson-recurrence-20260825.md` (SHA-256 `ff082a2c6607d33b0d117ca5e745dd8b88f267752670b364a1c434eb6d125e88`) |
| Pinned bytes | match; no custody failure |
| Overall verdict | **CONFIRMED** |
| Mathematics | **CONFIRMED** as a reduced-point / UFD derivation of homogeneous bands 18–12 on the squarefree `K` stratum, including (FT1)–(FT2) and (1)–(19) |
| Software | **NOT APPLICABLE** to the producer note (hand derivation). No local CAS or original-bracket replay was launched. The separate AWS package `xmodel/max12-912-order1-squarefree-poisson-recurrence-rows18-12-aws-20260825.md` was not consumed |
| Custody | **CONFIRMED** of the pinned producer bytes. Historical hashes `e46d3204…`, `c0753a6f…`, `ec0eb0a2…` are cited consistently by the note and by the AWS preregistrations; this review does not reconstruct those older file bytes |
| Wording / scope | **CONFIRMED.** Set-theoretic / UFD statements are not silently promoted to scheme or radical equalities. The license paragraph below is the maximum claim |
| Mathematical defects | none |
| Software defects | none (no executable is under review) |
| Custody defects | none |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer |
| Evidence | independent rederivation of the homogeneous ODE centralizer; Leibniz reconstruction of Jacobian rows 18–16; independent `R P` / binomial expansion of `P^{4/3}` through `Q8`; schoolbook expansion of the triangular identities (11) and (18) and of the Cardano remainder (13)–(16); two homogeneous specializations of `R^4` at degree 5 for the extra `Q5` monomials; binary-form parameter counts. No Singular, Sage, Groebner, rref, or local exact replay |
| Git HEAD | `f96845eecaa073110d1526e0b08117205a4dcf30` (producer uncommitted) |
| Review window | 2026-08-25 |

## Verdict

**CONFIRMED**

Over an algebraically closed field of characteristic zero, with `K` a squarefree binary cubic and leading forms `P9=K^3`, `Q12=K^4`, the homogeneous polynomial and rational centralizer lemmas are correct, including at infinity, in the localization at `K`, and in negative degree. There is a unique formal cube root `R=P^{1/3}` in the decreasing-degree completion of that localization with leading term `K`. The identity `[R,Q-R^4]=c/(3R^2)` has leading degree `-6`, forces commuting leading remainders of degree `d>-7` to be resonant exactly at `d\in\{9,6,3,0\}` among nonnegative degrees, and yields

```text
Q = [ R^4 + (lambda/3) R^3 + mu R^2 + nu R + delta ]_>=0.
```

Equations (1)–(19) rederive with the displayed signs, coefficients, and target-shear terms. The squarefree reduced-family dimensions `16+6=22`, `19+5=24`, `21+5=26`, and `23+3=26` are honest parameter counts of the displayed triangular charts, not Krull dimensions of possibly nonreduced incidence schemes. Under `K\mid CW`, polynomiality of the displayed degree-6 poles is equivalent to `K\mid C` and `K\mid W` as a UFD/reduced-point statement, and imposes no hidden condition on `U`. The eight root-allocation pieces at degrees 14 and 12 are set-theoretic unions, not scheme decompositions and not disjoint partitions.

The old degree-14 formula containing `(lambda/3)V` is dimensionally invalid and is treated only as the disclosed negative control `e46d3204…`.

## Strongest exact claim

On the squarefree homogeneous stratum `P9=K^3`, `Q12=K^4`, the reduced geometric points of the first four lower Jacobian bands are given by the displayed divisibility parameterizations (1)–(19), with reduced dimensions

| after row | reduced old base | fresh | full | reduced obstruction |
|---|---:|---:|---:|---|
| 17 | 6 (`P8=K R_5`) | 8 (`P7`) | 14 | `K\mid P8` |
| 16 | 11 (`A2,P7`) | 8 (`P6,lambda`) | 19 | `R_5=K A2` |
| 15 | 16 (`A2,B4,P6,lambda`) | 6 (`P5`) | 22 | `P7=K B4` |
| 14 | 19 | 5 (`P4`) | 24 | `K\mid C4 W6`, eight allocation branches |
| 13 | 21 | 5 (`P3,mu`) | 26 | `K\mid C4` and `K\mid W6` |
| 12 | 23 | 3 (`P2`) | 26 | `K\mid N3 R5`, eight allocation branches |

Here `R_5` in the degree-17 row is the old degree-five cofactor of `P8`, not the later degree-five combination in (17). Each “full” number is the number of free binary-form coefficients on the displayed reduced chart, including the licensed target shear `lambda` and the degree-six recurrence resonance `mu`. Mixed allocation branches remain live at rows 14 and 12 and are killed, as reduced points, at row 13.

## Sharpest non-claim

A reduced-point recurrence for homogeneous Jacobian degrees 18 through 12 on one squarefree leading-form stratum of the strict total-degree `(9,12)` box. Not a scheme-theoretic or radical identification with any Groebner incidence ideal, not polynomiality of a complete cube root of `P`, not vanishing or survival of bands 11 through 0, not a polynomial target automorphism for `mu` or `nu`, not a transfer to weighted or partial-`y` filtrations, not a maximum-twelve theorem, not a counterexample, and not JC2.

---

## Custody of the pinned note

**CONFIRMED**

```text
ff082a2c6607d33b0d117ca5e745dd8b88f267752670b364a1c434eb6d125e88  xmodel/sol-max12-912-squarefree-poisson-recurrence-20260825.md
```

matches the prompt pin. The review is of those bytes. No producer file was modified.

The disclosed ancestor hashes

```text
e46d3204b1c7048a56b54624ec73b3ca7c1f80ea685d01205496eb8c9e2630be   first degree-14 formula, invalid (lambda/3)V
c0753a6f1b29601e08a71ae7b88682bae568d489f4d4cb7b82acad2760e10eba   corrected degree-14 parent of the degree-13 subsection
ec0eb0a2a004622d742652664f9db96de8ba9999141a85b1c796b8e5a0f1acb9   parent of the degree-12 subsection
```

are the same strings recorded in the AWS preregistrations under

```text
cases/max12_912_order1_binary_cubic_squarefree_degree14_poisson_aws_20260825/
cases/max12_912_order1_binary_cubic_squarefree_degree13_poisson_aws_20260825/
cases/max12_912_order1_binary_cubic_squarefree_degree12_poisson_aws_20260825/
```

Those cases and the wrap-up `xmodel/max12-912-order1-squarefree-poisson-recurrence-rows18-12-aws-20260825.md` are a separate original-bracket producer. They were not read as evidence for the identities below.

---

## Charge 1 — polynomial and rational homogeneous centralizer of squarefree `K`

**CONFIRMED**

Work over an algebraically closed field of characteristic zero. Write `[A,B]=A_x B_y-A_y B_x`. Let `K` be a squarefree binary cubic and `W` a homogeneous rational function of degree `d`. In any affine chart `z=x/y` one has `K=y^3 k(z)` and `W=y^d w(z)` with `w\in k(z)`, and the bracket identity is

```text
[K,W] = y^{d+1} ( d k'(z) w(z) - 3 k(z) w'(z) ).
```

Vanishing is the ODE `3\,d\log w = d\,d\log k` in the function field of the line, hence `w^3=c\,k^d`. Squarefreeness of `k` (or of `K` after a chart change) forces `3\mid d`, otherwise a simple root of `k` has valuation not divisible by 3. Then `w=\lambda k^{d/3}` and `W=\lambda K^{d/3}`. Cube roots of unity are absorbed into the scalar.

Attacks, and why they do not land.

- **Root at infinity.** If the chart `z=x/y` places a root of `K` at `y=0`, then `deg k<3`. The ODE is unchanged. The degree identity `3\deg_{\mathrm{rat}}(w)=d\deg k` together with unique factorization still forces `3\mid d` and `W=\lambda K^{d/3}` (checked on the representative `K=xy(x-y)`, where `k(z)=z(z-1)`). The producer’s instruction to choose a chart avoiding the three roots is available by `PGL2` over an algebraically closed field and is a convenience, not a missing chart.
- **Polynomial case.** If `W` is a polynomial then `w` is a polynomial, and the same conclusion holds in `k[x,y]`. Constants (`d=0`) commute; so do all `K^{d/3}` with `d\ge 0` and `3\mid d`.
- **Negative degrees.** For `d=-3m<0` one obtains `W=\lambda/K^m`, which is homogeneous of degree `d` and lies in the localization at `K`. Directly, `[K,K^{-m}]=-m K^{-m-1}[K,K]=0`.
- **Localization at `K` versus the full fraction field.** Homogeneous elements of `k[x,y]_K` are ratios `F/K^m`. The rational lemma is strictly stronger and implies the localized statement. A homogeneous rational centralizer with poles off `K=0` would still have to equal `\lambda K^{d/3}`, whose only poles lie along `K`. There are no extra localized centralizers.
- **Algebraic closure.** Used to split `K=\ell_1\ell_2\ell_3` in later charges. The centralizer lemma itself needs only that `K` be squarefree in a UFD of characteristic zero (an irreducible cubic, or a linear times an irreducible quadratic, still forces `3\mid d`).
- **Characteristic.** Characteristic zero is the right global hypothesis. In characteristic 3 the ODE collapses to `d k' w=0` and the triple-root analysis changes; every later coefficient `1/3,1/9,1/27,1/81,1/243` is undefined. Characteristic 2 would additionally break the collapse `-2C^3=0\Rightarrow C=0` at row 13. Characteristic not 2 or 3 would suffice for the lemma plus (14)–(15), but the note correctly states characteristic zero.
- **Non-squarefree `K`.** For `K=y^3` one has `[y^3,x^a y^b]=-3a x^{a-1}y^{b+2}`, so every `W=\lambda y^d` commutes and `3\mid d` fails. Squarefreeness is essential for the stated form. (The double-root form `K=xy^2` happens to obey the same homogeneous conclusion, but that is outside the squarefree stratum and is not used.)

The producer’s sentence that this elementary homogeneous lemma is the only centralizer input is accurate for everything through (19).

---

## Charge 2 — unique cube root, (FT1), (FT2), degree bookkeeping

**CONFIRMED**

**Existence and uniqueness of `R`.** Filter the localization `k[x,y]_K` by homogeneous degree and complete in the decreasing direction. Write `P=K^3+P_8+\cdots+P_0` and seek `R=\sum_{j\le 3} R_j` with `R_3=K` and `R^3=P` as formal series. The degree-`n` piece of `R^3` is `3K^2 R_{n-6}` plus products of already determined higher terms. Characteristic zero inverts 3; localization inverts `K`. So each `R_{n-6}` is uniquely determined. Negative-degree pieces of `R^3` are arranged to vanish because `P_n=0` for `n<0`. Cube roots of unity are excluded by the leading-term normalization `R_3=K`. The resulting `R` is a formal series of homogeneous rational functions with poles only along `K=0`, of the shape `K` plus terms of degree at most 2, as stated. It is not claimed to be a polynomial, nor a single rational function.

**From `[P,Q]=c` to (FT1).** Set `T=Q-R^4`. Then `[R,R^4]=0` and `[R^3,Q]=3R^2[R,Q]=c`, so

```text
[R,T] = c/(3R^2).                                   (FT1)
```

The right-hand side has leading term `c/(3K^2)` of degree `-6`.

**Leading-term bookkeeping.** If the leading term of `T` has degree `d`, the leading term of `[R,T]` is `[K,T_d]` of degree `d+1`. For this to lie strictly above the right-hand side one needs `d+1>-6`, i.e. `d>-7`. For every integer `d\ge-6` one therefore has `[K,T_d]=0`. The rational centralizer lemma forces `T_d=0` unless `3\mid d`, in which case `T_d=a K^{d/3}`. Subtracting `a R^{d/3}` cancels that leading piece without changing (FT1), because `R^{d/3}` commutes with `R`.

**Nonnegative resonances.** `Q_{12}=K^4=(R^4)_{12}`, so `T` has degree at most 11. The nonnegative degrees with `3\mid d` and `d\le 11` are exactly `9,6,3,0`. They produce constants `lambda,mu,nu,delta` and the normalization `lambda/3` matches the target shear `Q\mapsto Q-(lambda/3)P` in (5). After these subtractions, every nonnegative homogeneous piece of `T` vanishes as a rational function, which is (FT2). The operator `[\;]_{\ge 0}` is the sum of nonnegative homogeneous pieces in the localized completion; equality with the polynomial `Q` is the assertion that those pieces are polynomials and coincide with `Q`.

**Negative commuting resonances and the constant Jacobian.** The same argument at `d=-3` and `d=-6` produces formal terms in `R^{-1}` and `R^{-2}`. They are invisible in `[\;]_{\ge 0}` and are not needed for (FT2). After they too are removed, the first degree at which `[K,T_d]` need not vanish is `d=-7`. Then `[K,T_{-7}]` has degree `-6` and can match `c/(3K^2)`, while

```text
[P_9, T_{-7}] = [K^3, T_{-7}]
```

has degree `9-7-2=0`. That is the first place a constant Jacobian can enter. The producer’s degree list is therefore complete: right-hand side starts in degree `-6`; a degree-`d` remainder brackets to degree `d+1`; nonnegative resonances are `9,6,3,0`; first noncommuting remainder that can source a degree-zero Jacobian is `-7`.

**Missing premises, all of which the note already carries in looser language.**

- Ambient ring: decreasing-degree completion of `k[x,y]_K`, characteristic zero.
- `P=R^3` as formal series, leading term of `R` equal to `K`.
- (FT2) generates positive-band equations only after demanding that the nonnegative pieces be polynomials. That is stated.
- `mu R^2` and `nu R` are recurrence resonances, not polynomial target automorphisms `Q\mapsto Q+f(P)`. Inside total degree 12 the only polynomial shears are `delta` and `(lambda/3)P`. The note says this for `mu`.
- (FT2) does not by itself make the negative parts of `R^4` vanish, prove `P` a polynomial cube, or obstruct the constant row.

No completeness, domain, or centralizer hypothesis required for (FT2) through degree 12 is missing. The empty duplicate heading “Why this may accelerate the lane” before the degree-14 subsection is editorial, not mathematical.

---

## Charge 3 — equations (1)–(9) and dimension `16+6=22`

**CONFIRMED**

The homogeneous Jacobian of degree `n` is `\sum_{i+j=n+2}[P_i,Q_j]`. Independent Leibniz reconstruction, with the derivation identities `[K^n,B]=n K^{n-1}[K,B]` and `[A,K^n]=n K^{n-1}[A,K]`:

**Degree 18.**

```text
[K^3,Q11]+[P8,K^4] = K^2 [K, 3 Q11 - 4 K P8] = 0.
```

The inner polynomial has degree 11, not divisible by 3, so vanishes, which is (1).

**Degree 17.** Direct expansion equals

```text
[K, K^2(3 Q10 - 4 K P7) - (2/3) P8^2 ].
```

The inner polynomial has degree 16, hence is zero: (2). Thus `K^2\mid P8^2`. In the UFD `k[x,y]`, squarefreeness of `K` gives `K\mid P8`, so `P8=K R_5` and (3). This is polynomial divisibility on each geometric coefficient point. It is not a scheme-theoretic identification with the frozen first-two-band ideal, which the first-two-band review correctly reports as nonreduced of Singular dimension 6. The reduced parameter count is six coefficients of a binary quintic, matching that geometric dimension; eight fresh `P7` coefficients remain.

**Degree 16.** With `S=P7` and `T=P6`, the original row equals the producer’s (4). The inner polynomial has degree 15, hence equals `lambda K^5`. Reduction modulo `K` yields `K\mid R_5^3`, hence `R_5=K A_2` on reduced points, and (5) follows by dividing the resulting identity by `K^2`. Signs: the `(4/27)R_5^3` term produces `-(4/81)K A_2^3` in `Q9`; the centralizer produces `+(lambda/3)K^3`. Parameters: `A_2` has 3 coefficients, `S` has 8, total 11; fresh `T` has 7 plus `lambda` gives 8; full 19. That is the reduced-family count the note writes as `11+8=19`. Agreement with any Groebner “degree-16 endpoint” is not re-verified here and is not required for the charge.

The scalar is target-shear gauge: `Q\mapsto Q-(lambda/3)P` removes the displayed `Q9` term and, coherently, the lower pieces `(lambda/3)P8`, `(lambda/3)P7`, `\ldots` appearing in (9), (10), (13), and (17). Retaining it until an explicit quotient is taken is correct.

**Degree 15, independently from `Q=[RP+(lambda/3)P]_{\ge 0}`.** With `R_2=A_2/3` and `R_1=(S-K A_2^2/3)/(3K^2)`, the degree-8 piece expands to

```text
Q8 = (4/3) K U + (4/9) A T + (2/9) S^2/K^2 - (4/27) A^2 S/K
     + (5/243) A^4 + (lambda/3) K^2 A.
```

Clearing denominators reconstructs (6)–(7) with the producer’s `F14`, including `-(5/81)K^2 A_2^4` and `-lambda K^4 A_2`. Degree 14 is not divisible by 3, so the inner polynomial vanishes and `K^2\mid F14`. Reduction modulo `K` gives `K\mid S^2`, hence (8). Substituting `S=K B_4` produces (9) with every displayed coefficient, including `+(lambda/3)K^2 A_2=(lambda/3)P8`.

**Dimension `16+6=22`.** After (8)–(9) the reduced base is `A_2:3`, `B_4:5`, `T:7`, `lambda:1`, total 16; fresh `P5` has six coefficients; full 22. This is a parameter count of the reduced chart, not a scheme dimension and not an identification with any double-root numerical family. The parenthetical coincidence with double-root numbers is not load-bearing and is not confirmed here.

The hash `e46d3204…` and the term `(lambda/3)V` are a disclosed negative control: `V=P4` has degree 4, while the degree-seven shear is `(lambda/3)P7=(lambda/3)K B_4`. They are not part of the current formula.

---

## Charge 4 — corrected degree-14 formulas (10)–(12), eight-way union, `19+5=24`

**CONFIRMED**

Put `C=B-A^2/3` and `W=T-AB/3+2A^3/27`. These are a polynomial automorphism of `(B,T)` with inverse `B=C+A^2/3`, `T=W+AB/3-2A^3/27`, so they do not change parameter counts. In the cube-root chart they are the depressed remainders `R_1=C/(3K)` and `R_0=(W-AC/3)/(3K^2)`.

**Identity (11).** Expanding `(4/9)CW` by hand yields exactly the displayed five-term numerator

```text
(4/9) B T - (4/27) A^2 T - (4/27) A B^2 + (20/243) A^3 B - (8/729) A^5.
```

**Formula (10).** Substituting the cube-root components into `(RP)_7+(lambda/3)P7` and eliminating `R_{-1},R_{-2}` from `P=R^3` produces

```text
Q7 = (4/3) K V + (4/9) A U + (4/9) C W / K + (lambda/3) K B,
```

after cancellation of every extra `1/K` monomial against the triangular substitution for `T`. The difference between a polynomial `Q7` and the pole-free part of (10) has degree 7, not divisible by 3, so the homogeneous centralizer lemma makes it zero. Polynomiality is therefore equivalent to `K\mid CW`, which is (12).

**Eight root-allocation pieces.** Over an algebraically closed field, `K=\ell_1\ell_2\ell_3` with distinct linear factors. As a UFD statement, `K\mid CW` means each `\ell_i` divides `C` or `W`. Indexing by `S\subset\{1,2,3\}` and writing

```text
C = (prod_{i in S} ell_i) C_{4-|S|},
W = (prod_{i not in S} ell_i) W_{3+|S|}
```

gives eight polynomial charts. This is a set-theoretic union, not a disjoint partition: a point at which extra factors vanish lies on more than one chart. It is not a scheme-theoretic decomposition, not a primary decomposition, and not a radical equality with the coefficient ideal of `K\mid CW`. The all-`C` branch `C=K L_1` is the next polynomial approximate-cube-root condition; the other seven branches remain live at this row.

**Dimension `19+5=24`.** Binary forms of remaining degrees `4-|S|` and `3+|S|` have `(5-|S|)+(4+|S|)=9` coefficients, independent of `S`. Plus `A_2:3`, `U:6`, `lambda:1` gives obstructed old base 19; fresh `V=P4` has 5 coefficients; full 24 on every branch. Overlaps of branches have strictly smaller generic dimension and do not inflate the union. These are reduced-chart parameter counts, not Krull dimensions.

---

## Charge 5 — degree-13 formulas (13)–(16), collapse of mixed branches, `21+5=26`

**CONFIRMED**

**Formula (13).** The binomial expansion of `K^4(1+Y)^{4/3}` at degree 6, with `Y=(P-K^3)/K^3` and binomial coefficients

```text
C(4/3,1)=4/3,  C(4/3,2)=2/9,  C(4/3,3)=-4/81,
C(4/3,4)=5/243, C(4/3,5)=-8/729, C(4/3,6)=44/6561,
```

plus `(lambda/3)P_6=(lambda/3)T` and the degree-six piece `mu K^2` of `mu R^2`, yields exactly (13). In particular:

- polynomial part `(4/3)KZ+(4/9)AV`;
- simple pole `(4/9)BU/K-(4/27)A^2 U/K=(4/9)CU/K`;
- double pole equal to `(2/81)(9W^2-6ACW-2C^3)/K^2`, verified by expanding the Cardano combination and matching the seven monomials `T^2`, `ABT`, `A^3 T`, `B^3`, `A^2 B^2`, `A^4 B`, `A^6` coefficientwise.

Degree 5 is not divisible by 3, so no new centralizer resonance occurs at this degree; `mu` is inherited from degree 6.

**Polynomiality under `K\mid CW`.** Clearing the common denominator `K^2` gives polynomiality of (13) if and only if

```text
K^2  divides  (4/9) K C U + (2/81) Gamma,     Gamma := 9W^2 - 6 A C W - 2 C^3.
```

Modulo `K` this is `K\mid Gamma`, which is (14). For each linear factor `\ell_i`, the quotient `k[x,y]/(\ell_i)` is an integral domain, and `CW\equiv 0` splits into `C\equiv 0` or `W\equiv 0`. If `C\equiv 0` then `Gamma\equiv 9W^2`, so `W\equiv 0` in characteristic not 3. If `W\equiv 0` then `Gamma\equiv -2C^3`, so `C\equiv 0` in characteristic not 2. Hence every `\ell_i` divides both `C` and `W`, i.e. `K\mid C` and `K\mid W` as polynomials, which is (15). Conversely (15) implies (14) and `K\mid CW`.

This equivalence is a reduced-point / UFD statement. It is not a radical equality of coefficient ideals: `C^3\in(K)` is scheme-theoretically weaker than `C\in(K)`. Mixed degree-14 branches do not survive as reduced points; they are not hereby shown to vanish as nonreduced scheme structure.

**No hidden condition on `U`.** Under (15), write `C=K L_1` and `W=K M_3`. Then `Gamma=K^2(9M^2-6 A L M-2 K L^3)` is divisible by `K^2`, and `(4/9)CU/K=(4/9)L U` is polynomial. The complete numerator is therefore divisible by `K^2` with no condition on `U`.

**Polynomial formula (16).** Substituting into (13) produces exactly

```text
Q6 = (4/3) K Z + (4/9) A V + (4/9) L U
     + (2/9) M^2 - (4/27) A L M - (4/81) K L^3
     + (lambda/3) T + mu K^2.
```

**Dimension `21+5=26`.** After the collapse, `A_2:3`, `L_1:2`, `M_3:4`, `U:6`, `V:5`, `lambda:1` total 21; fresh `Z=P3` has 4 coefficients plus `mu` gives 5; full 26. Honest reduced-chart arithmetic: the previous full family of dimension 24 had 9 parameters in `(C,W)` which become 2+4=6, losing 3, and `V` is now old, so `24-3=21` old plus 5 fresh.

---

## Charge 6 — degree-12 formulas (17)–(19), `23+3=26`

**CONFIRMED**

Put `N=M-AL/3` and `R5=9U-A^2 L-3 A N-3 K L^2`. The change `(M,U)\leftrightarrow(N,R5)` is triangular with leading coefficients `1` and `9`, hence an isomorphism of parameter spaces. In the cube-root chart, `R_0=N/(3K)` and `27 K^2 R_{-1}=R5-3AN`.

**Shear terms in (17).** Degree 5 of `(lambda/3)P` is `(lambda/3)U`. Degree 5 of `mu R^2` is `mu\cdot 2K\cdot(A/3)=(2 mu/3) K A`. No homogeneous centralizer of `K` in degree 5.

**Leading polynomial terms.** The binomial at degree 5 gives `(4/3)K Y+(4/9)A Z`. The quadratic `B V/K` term is `(4/9)LV+(4/27)A^2 V/K`, and the cubic `Y_{-1}^2 Y_{-5}` contribution `-(4/27)A^2 V/K` cancels the pole, leaving `(4/9)L V`.

**Identity (18).** Expanding `3 N R5-A K L^3` with the definition of `R5` is tautological and equals the displayed left-hand side. Scaling by `4/243` converts that identity into

```text
(4/243)(3 N R5 - A K L^3)/K = (4/81) N R5 / K - (4/243) A L^3.
```

The term `A K L^3` is already divisible by `K`, so it contributes the polynomial `-(4/243)A L^3` rather than a new divisibility. Independently, the specialization `A=L=0` of `R^4` at degree 5 yields the pole `(4/9) N U/K`, which is `(4/81)N\cdot(9U)/K`; the specialization `N=U=V=Z=Y=0` yields the polynomial `-(4/243)A L^3` after summing the five contributions `rho^4`, `4 rho^3_6 R_{-1}`, `4 rho^3_7 R_{-2}`, `4 rho^3_8 R_{-3}`, and `4 rho^3_9 R_{-4}`. Those two monomials together with (18) fix the displayed extra terms in (17). Polynomiality of `Q5` is therefore equivalent to `K\mid N R5`, which is (19).

**Eight-way allocation and dimension.** As at degree 14, `K\mid N R5` is the set-theoretic union of eight overlapping charts, not a scheme decomposition. Remaining coefficients of `(N,R5)` total `(4-|S|)+(3+|S|)=7` on every branch. The degree-13 full family had dimension 26; imposing three reduced divisibility conditions drops the old base to 23; fresh `Y=P2` has 3 coefficients; full 26 on every branch. The all-`N` branch `K\mid N` is the next polynomial approximate-cube-root condition (`R_0` becomes polynomial). The seven mixed branches remain live at this row.

Notation collision, non-blocking: the symbol `R5` in (17) is not the degree-17 cofactor of `P8`. The two objects never appear in the same formula.

---

## Charge 7 — license for the squarefree order-one fixed-D12 `(9,12)` stratum

**CONFIRMED** at the following strength, and no higher.

What the derivation licenses, once (FT2) and (1)–(19) are accepted:

1. On the squarefree leading-form stratum `P9=K^3`, `Q12=K^4` of the strict total-degree `(9,12)` coefficient box, the reduced geometric points of homogeneous Jacobian rows 18 through 12 are parametrized by the displayed triangular charts, with the reduced dimensions of the strongest-claim table.
2. Target shear `lambda` is the unique polynomial automorphism of this degree window besides adding a constant to `Q`. The quantity `mu` is a recurrence resonance of `R^2` and is not licensed as `Q\mapsto Q+f(P)`.
3. A transparent replacement of separate Groebner derivations for those four upper bands, at reduced-point scope, by expansion of `P^{4/3}` plus the two resonances that have already appeared.
4. A concrete prediction that the next mixed-allocation collapse, if it occurs, is the degree-11 row, analogous to the degree-13 collapse of `K\mid CW` to `K\mid C` and `K\mid W`.

What it does not license:

- any Jacobian row of degree `\le 11`, including the constant row sourced by `T_{-7}`;
- polynomiality of the complete formal cube root of `P`, or of `R_0`, `R_{-1}`, `\ldots`;
- elimination of the seven mixed `K\mid N R5` branches;
- scheme or radical equality with the compiler’s incidence ideals, including the already reviewed nonreduced first-two-band ideal;
- transfer to a weighted or partial-`y` filtration (that would need its own homogeneity, cube-root existence, and rational centralizer theorem);
- a maximum-twelve theorem, a Keller map, a counterexample, or JC2.

The classical remark that `gcd(9,12)=3` is below Heitmann’s bound 16 is a routing fact about this total-degree box and is not inferred from (1)–(19). It is not used above.

---

## Set-theoretic statements versus scheme statements

| statement | scope |
|---|---|
| `K\mid P8`, `P8=K R_5`, `R_5=K A_2`, `P7=K B_4` | UFD / reduced points of the squarefree stratum |
| first-two-band Singular dimension 6 with `s9^2` in the standard basis | scheme; not identified with the reduced chart |
| `K\mid C W` and `K\mid N R5` | UFD divisibility; set-theoretic union of eight overlapping charts |
| eight-way parameter counts `19+5=24` and `23+3=26` | reduced-chart dimensions, constant across branches |
| `K\mid C` and `K\mid W` from (14) plus `K\mid CW` | reduced points, using that `k[x,y]/(\ell_i)` is a domain and `char\ne 2,3` |
| mixed branches “collapse” at row 13 | reduced points; no claim about nilpotents |
| all dimensions `16+6=22`, `21+5=26`, `\ldots` | parameter counts of displayed charts, not Krull dimensions |

No scheme or radical assertion in the producer note is load-bearing, and none is added here.

---

## Exact defects

**Mathematical:** none.

**Software:** none in the object under review.

**Custody:** none for the pinned producer bytes. The ancestor hashes are consistent citations, not independently reconstructed files.

**Non-blocking editorial notes, not defects.** Duplicate empty heading before the degree-14 subsection; reuse of the name `R5` for two different degree-five forms; parenthetical coincidence with double-root numerical dimensions is unused.

---

## Cleanest next row, and the general induction

**Next row.** Degree 11, the degree-four piece of (FT2). After substituting (15)–(19), expand `Q4` from `R^4+(lambda/3)R^3+mu R^2`. The expected shape is a polynomial part `(4/3)K P_1+(4/9)A Y+(4/9)L Z+\cdots` plus a simple pole whose numerator is a product of `N` with the next depressed remainder of `R5` (and possibly a cubic remainder in `(N,R5)` over `K^2`). Two outcomes, to be distinguished by an original-bracket identity, not by pattern matching:

- analogue of row 13: under `K\mid N R5`, polynomiality forces `K\mid N` and `K\mid R5` as reduced points, collapsing the eight branches and making `R_0` polynomial;
- analogue of row 14/12: the eight mixed allocations survive and a further pair of remainders is allocated.

The first outcome is the higher-value test: it is exactly the next coefficient of a polynomial approximate cube root. Resonance `nu` does not yet appear (degree 3). Do not discard mixed branches until the identity forces it.

**General induction, at reduced-point scope only.** Let `R^{(s)}` be the truncation of `R` through a given pole order, with two consecutive depressed remainders `(\Gamma,\Delta)` encoding the failure of the next coefficients to be polynomial. Then the next nonnegative piece of `R^4` has pole numerator proportional to `\Gamma\Delta` (or a fixed cubic form in `(\Gamma,\Delta)` over one extra power of `K`). Squarefreeness of `K` converts `K\mid\Gamma\Delta` into an eight-way allocation, and the following row’s cubic remainder vanishes on each line `\ell_i` only if both remainders vanish there. Resonances are admitted only at Q-degrees in `{9,6,3,0}`, and only `lambda` and `delta` are polynomial target automorphisms. The induction still has to reach `T_{-7}` and the constant Jacobian; four confirmed bands do not finish it.

Any transfer off the homogeneous total-degree filtration must re-prove bracket homogeneity, existence of the completed cube root, and the appropriate rational centralizer theorem. None of those is supplied by (1)–(19).
