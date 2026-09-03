# Hostile gate: is the 7,161-coefficient joint chart a necessary superset for `(99,66)`?

Lane `g9966-design-gate-grok46-20260903`.  Charged:
`g9966-global-design-sol56-20260903.md` with the listed drivers, Moh/Xu PDFs,
skeleton, FALLACY-v2, and the four prior gates/reviews.  No ledger, `jc2-lean`,
`ideation-*`, or named in-progress lane reports were read or edited.

## Verdict first

`MECHANICAL-CHECK`: PASS.  Manifest generated with `awk` from the
`charged_input_<i>_sha256=` / `charged_input_<i>_basename=` lines of
`xmodel/g9966-design-gate-grok46-20260903.run.v2`, checked with `sha256sum -c`.
All **21/21** frozen inputs `OK`.  No digest was retyped.
Manifest: `box/g9966dgate-20260903/inputs.sha256`.

| item | charged claim | verdict | scope |
|---|---|---|---|
| (1) label reversal | `F` deg 99 is Moh/Xu `g`; `G` deg 66 is Moh/Xu `f`; `u_s m/d_s=18` on `f` | **CONFIRMED** | Moh p.194/p.202, Xu §7.3 p.10 and §8 p.13; chart puts the *minor* line at `y=0` (Moh (8) puts the *major* line at `y=0`) — a gauge, not a degree swap |
| (2) major `516→120` | simultaneous `h3`-`D2` / `h2`-`D2` / first `h2`-`D1` band; every row necessary | **CONFIRMED** as a necessary *prefix* of Thm 1.2 on `h3⊂h2`; **not** 17(rr) | outer `A,B` `D1`/`D2` order rows are not in the 516; `u_3=3` is the *second* point |
| (3) minor leaders | `δ=2 [2,1]` common-`h3` and `δ=5/2` leader + reduced `T3` ODE vs N6/N8/N9 | **CONFIRMED** as necessary leaders of the promoted split classification | reduced ODE is not `T3∈k(x)[F,G]`; `s^{28}` not re-executed |
| (4) Jacobian prefix | 15 independent pivots; deg `162=99+66-3` after the top | **CONFIRMED** | `J≤163`; top `J(P^9,P^6)≡0`; `[x^{135}y^{27}]` is the next deg-162 monomial |
| (5) controls | `(64,48)→(16,12)` kill; automorphism survives | **CONFIRMED** | `(16,12)` replayed over `GF(32003)` (77 rows, both c5 readings `[1]`); automorphism over `Q` |

**Overall: `GAP[COMPLETE-JOINT-SYSTEM]`.**  Chart (2.1) **is** a necessary
coordinate chart for the gauged two-point locus (not a 17(rr) slice).  The
displayed rows are a necessary *relaxation*.  They do not include the outer
`F,G` `D1` Thm-1.2 bands, the effective-root bridge, or the unranked remainder
of `IJ`.  The next-band computation is the right *kill-or-bound* test of that
relaxation, not a complete decider for `(99,66)`.

`(99,66)` remains `OPEN`.  Nothing here is a Keller witness.  No new
exit-price assertion.

## 0. Pages opened

Printed Moh page `p` is PDF page `p-139`.  Xu printed page `p` is PDF page `p`.
Images under `box/g9966dgate-20260903/pages/`; text extracts under
`box/g9966dgate-20260903/text/`.

```text
moh_pdf-10.png   p.149  Theorem 1.2
moh_pdf-12.png   p.151  Lemma 2.1
moh_pdf-51.png   p.190  minor/major dichotomy
moh_pdf-55.png   p.194  two-point top; (8)(9)(10)
moh_pdf-56.png   p.195  Proposition 6.2
moh_pdf-63.png   p.202  table (99,66; M2=77,M3=97; V3=V2=8; δ2=1/3, δ1=4/9)
moh_pdf-68.png   p.207  Appendix II; u_s=1 for the first three descents
moh_pdf-69.png   p.208  (16,12) 17-coefficient ansatz
xu_p-10.png      p.10   §7.3, Prop. 7.3, multiplicity m u_s/d_s
xu_p-13.png      p.13   §8, data (8.1), (8.2), δ=5/2 open
```

## 1. The essential label reversal

`SOURCE-READ`, Moh p.149: `deg_y f=m`, `deg_y g=n`.  `SOURCE-READ`, Moh p.202
and Xu p.13 (8.1): `n=99`, `m=66`, `M_2=77`, `M_3=97`, `V_3=V_2=8`,
`δ_2=1/3`, `δ_1=4/9`.  Skeleton `M=(−66,77,97)` is `M_1=−m`, `M_s=n−2`.
The gcd chain is `d=(99,33,11,1)`; `u_3=d_3−V_3=11−8=3`.  These data are
attached to **Moh/Xu `g`**, the degree-99 polynomial.

`SOURCE-READ`, Xu p.10 §7.3: `(f,g)` monic in `y`, `deg f=m`, `deg g=n`,
`T_0=g`, `T_1=f`, and the principal-minor multiplicity of **`f`** is
`m u_s/d_s`.  At this row that is `66·3/11=18`.  The same formula on `g`
gives `99·3/11=27`.  Last effective root: `((−μ_s−2)u_s/d_s)+1`; Xu p.13
has `−μ_3=145`, hence `(143·3/11)+1=40` on `T_3`.

The design's identification is therefore forced:

```text
chart F = prompt f = Moh/Xu g,   deg 99,  minor 27, major 72
chart G = prompt g = Moh/Xu f,   deg 66,  minor 18, major 48
```

so `(F,G)=(g_Moh,f_Moh)` and `J(F,G)=1` is `J(g,f)=1= −J(f,g)` in Moh's
ordered pair.  The `t^{18}F` and `t^{12}G` clearings in (2.4) are
`|ord g(σ)|=18` and `|ord f(σ)|=12` at `δ=2` (Xu p.13; Moh p.209 `t^{-18}`
on `g`), **not** the multiplicity 18.

`SOURCE-READ`, Moh p.194: for `M_s=n−2` the top of **`g`** is
`[(y−ax)^{v_s}(y−bx)^{u_s}]^{n/d_s}` with `a≠b`.  After (8) Moh sets the
**major** residue `a=0`; the minor is (9)–(10), `z=y−bx−e`.  The chart
fixes `P=y^3(y−x)^8`, so `in F=y^{27}(y−x)^{72}`: **minor** at `y=0`,
**major** at `y=x`.  That is a linear gauge of the two p.194 lines, not a
swap of degrees.  `u_s·m/d_s=18` is the multiplicity of **Xu/Moh `f` =
chart `G`** at the second (principal-minor) point `y=0`.

Tower radii `δ=(4/9,1/3,−1)` are the major-disc radii of this same `g`
(Def. 5.1 / p.202).  They are not the principal-minor split order.
`FALLACY-v2 / flag-place-series`: not identified.

## 2. Major tower rows `516→120`

`SOURCE-READ`, Moh p.149 Theorem 1.2: if `f=h^d+∑_{j=1}^d h_j h^{d−j}` with
`deg h_j<deg h=(deg f)/d` and `h` a `d`-th quasi-approximate root of accuracy
`λ`, then `ord h_j(σ_i)≥(λ/d)j`.  Along the major tower one has
`ord h=λ/d`, so this is the design's `ord Q_j≥j·ord h`.  The table

```text
ord h3(D2)=−1/3,  ord h2(D2)=−1,  ord F(D2)=−3,  ord G(D2)=−2
ord h2(D1)=−1/9,  ord A2≥−2/9, ord A3≥−1/3, ord B1≥−1/9, ord B2≥−2/9
```

is that identity applied to `h3` of `y`-degree 11 inside `h2` of `y`-degree
33 inside **`F`** of degree 99 (the AM tower of Moh's `g`, not Xu's `T_i`).
No `h3` row at `D1`: the `F`-multiplicity 24 is not divisible by 9.

Independent support count (driver): `H` has 66 lower coefficients; 43 lie
strictly below `3r+4q=32`; equality sites `(r,q)=(4,5),(8,2)`; 21 remain
with `3r+4q≥33`.  After the 45 `h3` rows the simultaneous ambient is
`21+187+308=516`.  Of 392 projected `h2` `D2` slots, three are identities
`(1,23),(1,22),(2,22)`; 389 unit-triangular `C2/C3` pivots (275+114);
seven `D1` rows below `e^{296}` with binomial minors `det=59049` and
`−3`.  Dimension `516−389−7=120`, and the 21 `h3` coordinates remain free.
This matches the charged `major_tower_structure.json`.

**Necessity.**  Face equalities and strict vanishings are the condition that
the `D2` leading form is exactly `w^3(w−1)^8` (resp. `(π^3−1)^8` for `K2`),
which is the two-point top plus Galois filling of denominator 3 at
`δ_2=1/3`.  Tschirnhausen (`no h3^2`, `no h2^2` in `F`) is a characteristic-zero
AM normalisation, not a discarded component.  The torus slice `a=1` in
`P_a=y^3(y−ax)^8` is a gauge.  No remaining gauge kills a pair that has this
skeleton.

**Fixed top at the first point, and 17(rr).**  The first (major) point is
the factor `(y−x)^8` in `h3`, multiplicity `v_s=8`, **one** residue.
`u_3=3` is the complementary factor at the *second* point, not a partition
of the first.  Moh p.194 with `M_s=n−2` forces exactly two linear factors;
it does not license a further original split of the major packet at radius
`−1`.  The topface-license 17(rr) partition-strata are about *descended*
`u'>1` after inverse Prop. 6.3, for original `u_s=1` rows.  This row has
original `u_s=3` and is not a descent.  `NOT-APPLICABLE[17(rr)]`.

`u_s=1` *does* hold for the `(64,48)` parent (Moh p.207), which is why
Prop. 6.4 applies there and not here.  That is
`OPEN[PRINCIPAL-MINOR-RADIUS]` on the second point (p.193: only `δ*≥1`),
not a first-point partition.

**Missing necessary rows in the 516.**  Section 2.1 *states* the outer
`D1` bounds on `A2,A3,B1,B2` and the `h3`-adic `D2` bounds on `F_j,G_j`.
The 516-count uses only `H,C2,C3`.  The 6600 outer coordinates are
untouched.  Numerical Moh (12)/(13) at `r=2` already hold for this skeleton
(`n*=3`, `m*=2`, `V_2=8`, `A_1=3`; (12) is true, (13) false; driver).
They are arithmetic filters that put `(99,66)` in the p.202 table, not extra
coefficient rows.  The missing *geometric* `D1` content is the outer Thm-1.2
vanishings on `A,B`.  Those are necessary and not yet imposed.

## 3. Minor incidence vs N6/N8/N9

Review-gate / source-review §7, charged here: N6 `δ∈{2,5/2}`; N8
`δ=2` only `[2,1]` with `(25,14)`; N9 `δ=5/2` only Galois `[1,1,1]`,
`p=π(π^2−c)`.  (Audit labels 17(nnn)/(rrr)/(sss).)

`δ=2`.  Chart (2.4): `σ=ut+zt^2`, `p_2=z^2(z+3ρ)`, packets `18+9` on `F`
(Moh `g`) and `12+6` on `G` (Moh `f`).  Leader
`R=z^{25}(z+3ρ)^{14}(z−2ρ)` is N8's family.  Driver: the face ODE
`2 p_2 R'−25 p_2' R=k p_2^{14}` (`'=d/dz`) holds identically with `k=5`,
matching the `δ=2` reduction of Xu (7.1).  Common-`h3` substitution
`w=ut^2+t^3 z` and the W3/W6 tails match the charged `joint_probe`.  On
`ρ≠0` this is the N8 face, not a slice of a larger Galois-allowed cubic.

`δ=5/2`.  Chart (2.6): `t=s^2`, `σ=us^2+vs^4+πs^5`, `p=π(π^2−c)`, packets
`9+9+9` / `6+6+6`.  This is exactly N9's `μ_2`-stable cubic (n5-gate:
`π↦−π`).  Monic `q_1` of (2.7) satisfies
`(−1/5)q_1'+2p^3=0`; the driver's `q_1` is that rescaling.  Xu p.13 prints
`q=p^{10}q_1` and `q_1=−2∫p^3`, and leaves the case open.  Equation (3.5)
is a necessary reduced ODE, not `T_3∈k(x)[F,G]`.  Through-`s^{28}`
consistency is the charged `xu_joint_extension.json` (`dimension 3` at
`c=1` with `b0`; `n=1` cokernel `−(2/5)c_{11,0}π`); this desk did not
re-run the 191 s extension.

Raw leader row counts 1,647 / 1,910 are equation *labels*, as the design
says; they are not ranks.

## 4. Direct Jacobian prefix

Generic `deg J(F,G)≤99+66−2=163`.  In the chart `F_{99}=P^9`, `G_{66}=P^6`
with `P=y^3(y−x)^8`, and `J(P^9,P^6)≡0` (driver).  So the first possible
nonzero homogeneous piece is degree `162=99+66−3`.  The complete `J=1`
system in this chart is the `1+2+⋯+163=13,366` coefficients of degrees
`0` through `162` (constant target `1`).  Scheme (2.8)'s `IJ` *is* that
full set; only ten contiguous degree-162 rows are ranked.

Those ten start at `[x^{145}y^{17}]` because `P^6` has `y`-order 18, so
`G_y` has `y`-order 17, and the first `J(F_{98},P^6)` monomial is `y^{17}`.
Coefficient `1764=98·18` on `A3_{(98,0)}`.  The last of the ten,
`[x^{136}y^{26}]`, is the first that meets `B2_{(65,0)}` and, after
reduction, pivots `1170 A2_{(65,0)}`.  Next monomial on the same face is
`[x^{135}y^{27}]` (`135+27=162`).

Replay of the charged `first_global_band.py` is byte-identical to the
charged `results.json` (`sha256 f4a6f39c…`): six unit pole pivots, Jacobian
row 1 dependent, rows 2–10 nine new pivots, rank **15**, residual 0, all
pivots in the outer `A/B` block.  Truncation of `F_{98}` to `y`-degrees
`0..9` and of `G_{65}` to `x^{65}` is exact on this `y^{17}…y^{26}` band
(any other `G_{65}` term contributes at `y`-degree `≥26` only through
`j=0`; `3P^6·(h_2)_{32}` starts at `y`-degree `≥35`).

## 5. Controls

**(16,12).**  `SOURCE-READ`, Moh p.208: `h=y^3(y−x)+b_1 y^3+b_2 y^2+b_3 y+b_4`,
`ḡ=h^4+α_1 h^3+α_2 h^2+α_3 h+α_4`, `f̄=h^3+β_2 h+β_3`, with the five
printed support rules, 17 coefficients.  Both readings of the repeated
`c_5` (printed: `α_3=c_5 A+c_5 B+c_7`; compiler: distinct `c_6`, `α_1=0`)
were built in the same ring: 17 coefficients, Jacobian scalar `kappa`,
wrapper `T·kappa−1`, **77** coefficient rows of `J−kappa`.  Groebner over
`GF(32003)`, grevlex, is `[1]` for both; `<kappa, T kappa−1>=[1]` and
`<kappa−1, T kappa−1>≠[1]` in `Q[kappa,T]`.  The order-spine unit identity
`(20z−10/3)(27/10−27z/5)−1=−2(54z^2−36z+5)` holds over `Q`.  Ring,
wrapper, and both controls are declared.  This is
`SATURATED-EMPTY[P208-ANSATZ / GF(32003)]`, a calibration of the method,
not a `(99,66)` emptiness.  A `Q`-Groebner of the 77-row ideal was not
replayed (no Singular in PATH).

**Automorphism.**  `F=ax+y`, `G=(a−1)x+y` has `J≡1` and inverse
`x=F−G`, `y=aG−(a−1)F` identically over `Q`.  Shared ansatz `Ax+y`,
`Cx+y` reduces to the single row `A−C−1`; slice `A=2` is the witness
`(2x+y,x+y)`.  The plumbing does not falsely kill it.
`NOT-APPLICABLE[s=3 tower; degrees (1,1)]`.

## 6. What the next band would and would not mean

The planned continuation — `[x^{135}y^{27}]J`, pole rows `F_{(95,*)}/G_{(62,*)}`,
and the matching outer-`F,G` `D1` Thm-1.2 band — adds necessary rows that
the 516-count omitted.  Typed consequences:

* **Empty** localized ideal: a valid finite necessary-condition **kill of
  that branch** inside chart (2.1).  It would not kill the other split,
  would not speak to pairs outside this skeleton, and would not require a
  `charge_basis` line unless promoted as a new exit price.
* **Nonempty:** `COUNTING-BOUND` of a still-incomplete relaxation.  Not a
  Keller pair; not `FULL_ACTUAL_EXIT`; not attainment of `J=1`.  Does not
  close `OPEN[EFFECTIVE-T2-T3-BRIDGE]` or the unranked remainder of `IJ`.
* The separate straight-centre dimension 59 remains a different ring.  It
  is not a joint-global count.

Band computation is the right *next* test.  It is not the complete
decider.  That is the GAP.

## 7. FALLACY-v2

Flag/place/series: major radii `(4/9,1/3,−1)`, split order `δ`, and
combined `δ*` are not identified; first-point `v_s=8` is not identified
with second-point `u_s=3`.  Carrier/attainment: dimension 120 / 6689 is a
relaxation floor, never a pair.  Floor/attainment: Thm 1.2 is `≥`; the
face equalities are exact because the leading form is fixed, not because a
lower bound was promoted.  `sat()`: `(16,12)` declares `GF(32003)` and
both wrapper controls; the `(99,66)` prefix uses `Q*` pivots with a
perturbed duplicate.  Prime marks: `p',R'` are `d/dz`; Xu `p'` is
`d/dπ`.  Variable/ring map: `F=Moh g`, `G=Moh f`, `P=y^3(y−x)^8`,
`K3=t^{11}h3(t^{-1},w/t)` are stated; matching names were not treated as
proof.  Numerical (12)/(13) were not identified with outer `D1` coefficient
rows.  No new exit-price assertion, so no `charge_basis` line.

## 8. Reproduction

```text
python3 box/g9966dgate-20260903/g9966dgate_driver.py
python3 box/g9966dgate-20260903/g9966dgate_1612.py
python3 /tmp/jc2-lane.LRGaUp/inputs/first_global_band.py \
  > box/g9966dgate-20260903/first_global_band_replay.json
```

Python 3, SymPy 1.12.  Jacobian replay ~10 s (byte-identical to the charged
`results.json`).  Arithmetic driver <2 s.  `(16,12)` ~98 s.
Artifacts: `box/g9966dgate-20260903/{g9966dgate_driver.py,g9966dgate_1612.py,results.json,results_1612.json,first_global_band_replay.json,inputs.sha256,artifacts.sha256,pages/,text/}`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14646`.
- Body SHA-256:
  `bb3ff016992d066691154e8f87e03dd624e4bb71d69cd8b7708457e0ee86172f`.
- Frozen basis: `523302dfe5b6b62adb6950ea8e801dde93d17d0f`.
