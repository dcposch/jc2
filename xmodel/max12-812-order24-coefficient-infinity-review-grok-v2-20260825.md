# Hostile review V2 — `(8,12)` order-four/order-two coefficient infinity

| Field | Value |
|---|---|
| V2 theorem | original source audit with exactly the erratum replacement of §7 `(7.2)` and its adjacent load-direction sentence |
| Original | `xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md` |
| Original SHA-256 | `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e` |
| Erratum V2 | `xmodel/max12-812-order24-coefficient-infinity-source-audit-erratum-v2-20260825.md` |
| Erratum SHA-256 | `aa90155ec8a182f4f451c77fc9548cf8035889efc230afdaea622f84eb18c495` |
| First hostile review (inspection only) | `xmodel/max12-812-order24-coefficient-infinity-review-grok-20260825.md` |
| First-review SHA-256 | `2f0a03a99ba6563034cdaf84ffc06f6d78ddd377144201d40aa4352ac71c6b55` |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Charged reviews were opened only to obey the inspection clause; no producer `PASS`/`EXACT` string and no charged `CONFIRMED`/`REPAIR` string is evidence |
| Method | source reading and hand derivation only; no CAS, solver, substantive Python, Lean, or other heavy local computation |
| Git HEAD | `24184c989634b40b00da1bbc3328bcc6ab92fa9b` (all three charged files uncommitted) |
| Smallest failing identity | none in the V2 theorem |
| Overall verdict | **CONFIRMED** |

Independently recomputed SHA-256 of the three charged files match the immutable pins above.

## Verdict

**CONFIRMED.**

The V2 theorem is the original source audit with the single local replacement advertised by the erratum. Directly from the definition `H_F(w)-g(z(w))`, at `f=K^2` one has monic `w=K^{1/4}`, and the first variation in each order-two load `k_j` (`j=2,6,10`), holding `f` fixed, is exactly the strictly negative Laurent part

```text
w^j - F_j(z(w)) = [K^{j/4}]_- .
```

The sign is that of `H_F-g`, not of `g-H_F`. No variation of `w` is hidden: `w=f^{1/8}` is a function of `f` alone. Vanishing of any one of those three full negative parts is equivalent to `K` being a square in `L[z]`. For the monic depressed quartic `K=z^4+p z^2+c z+r`, including every degenerate case, the square locus is exactly `c=0`, `p^2=4r`. Already the first two seven-tail coordinates of the `k_2` derivative cut out this locus, so the same equivalence holds for the seven-row projection.

The coefficient-direction expansion `(7.1)` is unchanged and correct. Consequently the order-four seven-tail map has zero first differential along the whole common-quartic locus, while the order-two seven-tail map has rank at most three. Neither client is linearly transverse. This does not license finite determinacy, a jet replacement for saturation, reducedness of the tail ideal, or exclusion of a strict arc.

The erratum is genuinely narrow. It does not alter or silently strengthen §§0–6, §8, the raw unloaded exceptional fibre, the bounded-degree split, common-quartic support, Rees equations, chart/denominator audit, or the original scope firewall. The only residual conflict is the superseded sentence in the immutable original §7, which the erratum explicitly replaces and declares not consumed.

The source typing, terminal row, infinity residue, bounded-degree split, ordinary unloaded fibre, Mason reduced support, strict-Rees design, and `P(2,3,4)` charts survive by independent rederivation below. This remains a reduced-support and source-typing theorem, not a saturation verdict.

## Smallest failing identity

None in the V2 theorem. No missing hypothesis breaks the repaired load-direction identity, the square-locus equivalence, the rank bounds, or the identification of the exceptional fibre.

The original displayed equalities

```text
(7.2)   F_10(K^2)=K^5,    F_6(K^2)=K^3,    F_2(K^2)=K
```

are false and, by the erratum, are not consumed. They are not part of V2.

Non-blocking citation precision, inherited from the original and not introduced by the erratum: the bound `gcd(deg P, deg Q)>=16` is the classical Heitmann necessary condition (also stated by Guccione–Guccione–Valqui). The arithmetic `4(U+1)<16\Leftrightarrow U<=2` is exact once that bound is granted. Prime gcd and gcd `2p` never apply to these bounded degrees.

## Strongest exact theorem that survives

Let `L` be a characteristic-zero field, after a harmless finite constant extension containing the needed roots of unity. Let `(P,Q)` be a Keller pair of actual `y`-degrees `(8,12)` with monic common core `h\in L[x]` of degree `H=4U>=4`, written `a_8=h^2`, `b_12=h^3`, `u^4=h`, and with the class of `h` in `L(x)^*/L(x)^{*4}` of order `e=4` or `e=2`. After the source shear that makes the depression `R_0` regular at infinity, the reviewed target gauges, and the character filter:

1. `f` is monic depressed of degree eight, `z=u(y+R_0)`, `R_0` is Kummer-invariant, and
   ```text
   e=4:  g=F_12(f),
   e=2:  g=F_12(f)+k_10 F_10(f)+k_6 F_6(f)+k_2 F_2(f),
   ```
   with `k_j\in L` and complete tail targets `(2.5)`. Always `8r_7'=j/u` with `j\neq 0`.
2. Every place of the minimal Kummer extension above `q=1/x=0` is unramified. On a selected sheet `t=q^U u` is a unit with `t(0)=1`, and `dR_7/dq=-(j/8)q^{U-2}t^{-1}`. For `U=1` the residue is nonzero, so both nontrivial `H=4` clients are empty. For `U>=2`, `R_7` and every other target load are regular at infinity.
3. If `d_i:=max(0,-ord_q(a_i))<=(U+1)(8-i)` for all `i`, the sheared pair has exact ordinary total degrees `(8(U+1),12(U+1))` and gcd `4(U+1)`, including the fully loaded order-two partner. Under the classical necessary bound `gcd>=16` this sector is counterexample-closed for `U<=2` and not classically closed for `U>=3`.
4. On a selected unramified sheet the descended exceptional rows of the charged Rees scaling are the ordinary unloaded system `r_1(f,F_12(f))=...=r_7(f,F_12(f))=0`. The other sheets are its weighted `mu_e` orbit. The reduced support is
   ```text
   K=z^4+p z^2+c z+r,    f=K^2,    g=K^3,
   ```
   a prime copy of `A^3`, projectively `P(2,3,4)`.
5. The strict chart `Lambda=q^{U+1}rho` together with sequential saturation by `q` and `rho`, then the irrelevant ideal `(B_0,...,B_6)`, is fail-closed for strict formal/Puiseux (hence rational) coefficient-infinity branches of that fixed source. The converse is only algebraic boundary accessibility.
6. At a common quartic, holding `f` fixed, the first variation of `H_F(w)-g(z(w))` in each order-two load `k_j`, `j\in{2,6,10}`, is `[K^{j/4}]_-`. Each of these three full negative parts vanishes if and only if `K` is a square in `L[z]`, which for the displayed depressed monic quartic is the proper closed locus `c=0`, `p^2=4r`. The coefficient-direction first variation `(7.1)` vanishes on the whole common-quartic locus. Hence the order-four seven-tail differential is zero, the order-two seven-tail differential has rank at most three, and neither client is linearly transverse. Finite determinacy is not granted.

This is a reduced-support and source-typing theorem, plus a bounded-degree split, a residue exclusion of `H=4`, and a first-differential non-transversality statement. It is not a saturation verdict.

---

## Finding 1 — repaired load derivative, sign, no hidden `w`

**Severity: none.**

Write `F_j=[w^j]_+` for the monic degree-`j` Faber polynomial in `z`, and

```text
H_F(T)=sum_j h_j T^j,     H_F(w)-g(z(w))=sum_{ell>=1} r_ell w^{-ell}.
```

After the three target gauges the order-two high-row form is

```text
H_F(w)=w^{12}+k_10 w^{10}+k_6 w^6+k_2 w^2,
g=F_12(f)+k_10 F_10(f)+k_6 F_6(f)+k_2 F_2(f).
```

The monic eighth root is `w=f^{1/8}=z+O(z^{-1})`. At a common quartic `f=K^2` with `K` monic of degree four, the unique monic square root of `f` is `K` itself, and the unique monic eighth root is the unique monic fourth root of `K`:

```text
w=K^{1/4}.
```

Uniqueness: `K=z^4(1+O(z^{-2}))`, and `1+O(z^{-2})` has a unique binomial fourth root `1+O(z^{-2})` in `L((z^{-1}))`. Any other fourth root differs by a fourth root of unity and would spoil the leading term `z`.

Hold `f` fixed. Then `w` and the inverted series `z(w)` are fixed, and every `F_j` (a polynomial in `z` built from `f` alone) is fixed. Differentiating the tail generating function in the coordinate `k_j` therefore hits only the displayed summands:

```text
\partial/\partial k_j (H_F(w)-g(z(w))) = w^j - F_j(z(w)).
```

By definition of the polynomial part at infinity, `w(z)^j=F_j(z)+[w(z)^j]_{z,-}`. Substituting `z=z(w)` and using `w(z)^j=K^{j/4}` gives

```text
w^j - F_j(z(w)) = [K^{j/4}]_{z,-}(z(w)).
```

The right-hand side is `O(w^{-1})`, because `z=w+O(w^{-1})` converts every strictly negative `z`-power into a strictly negative `w`-series. This is the strictly negative Laurent part `[K^{j/4}]_-` in the sense of the tail identity `(2.3)`. The sign is positive for `H_F-g`; the opposite combination `g-H_F` would flip it. Vanishing is unaffected by a global sign.

No chain-rule term in `w` is present. A hidden variation of `w` would require `k_j` to enter `f`, or the eighth-root construction to depend on `H_F`. Neither occurs. At a point with `k=0` the same partials are the load columns of the first differential of the joint map `(a,k)\mapsto(r_1,...,r_7)`; mixed second derivatives do not enter.

Attacks that failed: interpreting `[K^{j/4}]_-` as the `w`-series of the function `w^j` itself (that series is tautologically `w^j` and has no negative part; the negative part is that of `K^{j/4}` as a `z`-series, re-expanded after subtracting `F_j`); taking `w=K^{1/2}` (that is the monic fourth root of `f`, not the eighth); a product-rule term from `\partial F_j/\partial k_j` (`F_j` does not depend on `k_j`).

## Finding 2 — vanishing of any negative part iff `K` is a square; locus `(E.2)`

**Severity: none.**

`[K^{j/4}]_-=0` if and only if `K^{j/4}` is a polynomial in `z`. The three indices are `j=2,6,10`, each congruent to two modulo four, so

```text
K^{j/4} = K^{1/2},\quad K^{3/2},\quad K^{5/2}
```

respectively.

If `K=Q^2` for some `Q\in L[z]`, then `K` monic of degree four forces `Q` monic of degree two, the monic square root of `K` is `Q`, and `K^{j/4}=Q^{j/2}` equals `Q`, `Q^3`, `Q^5` respectively, all polynomials. All three negative parts vanish.

Conversely, work in the UFD `L[z]`. If `K^{3/2}=P` is a polynomial then `P^2=K^3`, so for every irreducible one has `3 v(K)=2 v(P)`, hence `v(K)` is even, hence `K` is a square. If `K^{5/2}=P` then `P^2=K^5` and `5 v(K)=2 v(P)`, so again `v(K)` is even. The case `K^{1/2}` polynomial is the definition of being a square. Characteristic zero is used only to guarantee that `2` and `3` (resp. `5`) remain nonzero in the valuation identity; the argument does not require squarefreeness of `K`. Thus vanishing of any one of the three full negative parts is equivalent to `K` being a square, and then all three vanish.

Exact locus for `K=z^4+p z^2+c z+r`. A monic degree-four square is `(z^2+a z+b)^2=z^4+2a z^3+(a^2+2b)z^2+2ab z+b^2`. Depression forces `2a=0`, hence `a=0`, hence `K=(z^2+b)^2=z^4+2b z^2+b^2`. Matching coefficients: `c=0`, `p=2b`, `r=b^2`, so `p^2=4r`. Conversely, if `c=0` and `p^2=4r` then `K=(z^2+p/2)^2`. Squares of non-monic quadratics do not enlarge the list: `(-z^2+a z+b)^2=(z^2-a z-b)^2` reduces to the same depressed family. Squares of linear polynomials have degree two, not four.

Degenerate quartics are included and not over-counted.

- `p=c=r=0`: `K=z^4=(z^2)^2`, on the locus.
- Double-double: `K=(z^2-t)^2=z^4-2t z^2+t^2` has `c=0` and `p^2=4t^2=4r`, on the locus.
- Double root at zero, two simple roots: `K=z^4+p z^2` with `p\neq 0` has `c=r=0` and `p^2\neq 0=4r`, off the locus, and is not a square.
- Triple-plus-simple, depressed: `(z-a)^3(z+3a)=z^4-6a^2 z^2+8a^3 z-3a^4` has `c=8a^3` and `p^2=36a^4\neq -12a^4=4r` unless `a=0`, off the locus.
- `K=z^4+r` with `r\neq 0`: `c=p=0`, `4r\neq 0`, off the locus.

The locus is a proper closed copy of `A^1` inside the common-quartic `A^3`, parametrized by `b=p/2`. A generic common quartic is not a square.

Seven-row projection. The full-series equivalence is what the erratum states. For the seven-tail map one still needs that a non-square does not hide its principal part in `O(w^{-8})`. Expand

```text
K=z^4(1+p z^{-2}+c z^{-3}+r z^{-4}),
K^{1/2}=z^2(1+u)^{1/2},\quad u=p z^{-2}+c z^{-3}+r z^{-4}.
```

The binomial `(1+u)^{1/2}=1+u/2-u^2/8+O(z^{-6})` yields

```text
K^{1/2}=z^2 + p/2 + (c/2) z^{-1} + ((4r-p^2)/8) z^{-2} + O(z^{-3}).
```

Thus `F_2(z)=z^2+p/2` and the `z`-principal part begins at `z^{-1}` or `z^{-2}`. Invert `w=z+(p/4)z^{-1}+O(z^{-2})` to `z=w-(p/4)w^{-1}+O(w^{-2})`. Then `z^{-1}=w^{-1}+O(w^{-3})` and `z^{-2}=w^{-2}+O(w^{-4})`, so the `k_2` tail begins

```text
[K^{1/2}]_- = (c/2) w^{-1} + ((4r-p^2)/8) w^{-2} + O(w^{-3}).
```

The seven-row `k_2` derivative therefore has coordinates `r_1=c/2` and `r_2=(4r-p^2)/8` (in the `H_F-g` convention). These two vanish if and only if `c=0` and `p^2=4r`. Hence already the seven-row `k_2` column vanishes if and only if `K` is a square. In particular the three seven-row load columns are not all zero off `(E.2)`, and “nonzero at a generic common quartic” holds for the seven-tail map, not only for the full series.

Attacks that failed: `K^{3/2}` polynomial without `K` a square (UFD, `3v(K)` even implies `v(K)` even); extra square points among multiple-root quartics; `(z^2+a z+b)^2` remaining depressed for `a\neq 0`; a non-square whose `k_2` principal part starts only at `w^{-8}` (the displayed `w^{-1}` or `w^{-2}` term); working with a non-monic fourth root.

## Finding 3 — coefficient variation `(7.1)`, rank, non-transversality without finite determinacy

**Severity: none.**

Write `f=K^2+E` with `E` of degree at most six (depression kills `z^7`; the top coefficient of `f` is `1`). At zero scaled Faber loads, `w^{12}=f^{3/2}` and the unloaded tails are the negative part of `f^{3/2}-F_{12}(z(w))`. The binomial series of the monic branch is

```text
(1+x)^{3/2}=1+(3/2)x+(3/8)x^2-(1/16)x^3+\cdots,
```

because `(3/2)(1/2)/2=3/8` and `(3/2)(1/2)(-1/2)/6=-1/16`. Substituting `x=E/K^2` produces `(7.1)`:

```text
(K^2+E)^{3/2}=K^3+(3/2)K E+(3/8)K^{-1}E^2-(1/16)K^{-3}E^3+\cdots.
```

The constant term `K^3` is a polynomial of degree `12`. The linear term `(3/2)KE` has degree at most `10`, hence is a polynomial in `z`. Both are absorbed into `F_{12}` at first order and contribute nothing to the negative `w`-series. The quadratic term already involves `K^{-1}` and is not claimed to be polynomial. This is vanishing of the first differential in every `f`-coefficient direction along the whole common-quartic locus, not finite determinacy.

Order-four client. The domain of the seven-tail map is the seven depressed coefficients `(a_0,...,a_6)`. Finding 1 has no `k_j` here. By `(7.1)` every partial vanishes on the common-quartic locus, so the first differential is the zero map.

Order-two client. The domain is those seven coefficients plus `(k_10,k_6,k_2)`, mapping to seven tails. At the exceptional point one has `k_j=0`, so the extra summands `k_j(w^j-F_j)` do not contribute to `f`-derivatives: each carries an explicit factor `k_j`. The seven coefficient columns therefore still vanish by `(7.1)`. Only the three load columns of Finding 1 can contribute, and the rank is at most three, strictly less than seven. The erratum does not claim generic rank equal to three, and does not need to: already the `k_2` column is nonzero off `(E.2)` by Finding 2, so generic rank is in `{1,2,3}`. On the square locus all three load columns vanish and the rank drops to zero.

Linear transversality of seven tail equations would require the differential to be surjective onto the tail space. Rank `0` and rank at most `3` both fail that. For the order-four client the three-dimensional common-quartic locus already prevents surjectivity, and `(7.1)` is stronger (rank `0` rather than at most `4`). For the order-two client the same three-dimensional zero locus in a ten-dimensional domain only gives rank at most `7`, which could still be surjective; the load-bearing input is `(7.1)`, which puts all seven coefficient directions in the kernel and drops the bound to `3`.

Finite-determinacy promotion is refused. Vanishing or rank-deficiency of `d\tau` blocks any implicit-function or jet replacement of the exact saturation. Scheme thickness, normal Kuranishi equations, and the charged Taylor boundaries remain open. Reduced support is not reducedness of `(r_1,...,r_7)`, not an exclusion of a strict arc, not Taylor realization, not cell closure, and not JC2.

A competing interpretation — derivatives of the Rees polynomials `Phi_ell` at `Lambda=0` — does not disturb V2. In `(5.3)` the loads enter only as `Lambda^{12-j}k_j`, so `\partial Phi_ell/\partial k_j` vanishes on `Lambda=0` by the prefactor, independently of whether `[K^{j/4}]_-` vanishes. That is a statement about the compactified chart, not about the unscaled tail map that the erratum differentiates while holding `f` fixed. It does not resurrect the false identity `(7.2)`, and it does not restore transversality of `Phi` in the `B_i` directions, which still vanish by `(7.1)`.

Attacks that failed: a linear term `(3/2)KE` of degree `>12` (depression bounds `deg E<=6`); promoting the quadratic `K^{-1}E^2` term to first order; claiming generic rank three as a numbered identity; using only the tangent space of `(p,c,r)` to get order-two non-transversality (that bound is `<=7`, not `<=3`); reading rank deficiency as a license to stop at a finite jet; treating `\partial Phi/\partial k_j|_{Lambda=0}=0` as a repair of original `(7.2)`.

## Finding 4 — erratum is narrow; residual conflict

**Severity: none** for V2. One residual conflict in the immutable original, explicitly superseded.

The erratum rewrites only original §7 from the sentence on order-two load derivatives through the non-transversality paragraph. It leaves `(7.1)` in place, records that original `(7.2)` is false and not consumed, and restates the finite-determinacy refusal. Direct comparison against §§0–6 and §8:

- Raw unloaded fibre `(0.1)`: exceptional rows are the ordinary tails of `g=F_12(f)` after positive Rees weights kill every lower Faber constant and every target load. That is a statement about values on `q=Lambda=0`, not about unscaled `k_j`-derivatives. Unchanged. The repaired derivatives being generically nonzero off `(E.2)` is compatible, because those derivatives are taken before (or without) the `Lambda^{12-j}` scaling.
- Common-quartic support `(0.2)`, triangular graph `(6.1)`, normals `(6.2)`, `P(2,3,4)` charts, denominator list `(6.4)`, independence of Kummer order `e` and Rees ramification `n`: none of these identities mentions `F_j(K^2)=K^{j/2}` or vanishing load derivatives. Unchanged. The converse Mason identity actually used is `F_12(K^2)=K^3`, which is `j=12` and `4\mid 12`, hence true independently of `(7.2)`.
- Bounded-degree split `(0.3)`, `(3.4)`–`(3.8)`: the `k_j` enter only as finite scalars of weights `12-j`. Unchanged.
- Rees equations `(5.3)`, strict chart `(5.5)`, saturation `(5.6)`–`(5.7)`: loads still have strictly positive weight and vanish on the exceptional divisor. Unchanged. Retaining the three `k_j` as polynomial variables, as §8 already requires, is if anything more necessary once their unscaled derivatives are generically nonzero.
- Terminal residue `(0.4)`, `(3.2)`, `H=4` exclusion, character descent `(4.1)`–`(4.5)`, scope firewall, and the four next gates in §8: no dependence on `(7.2)`.

The erratum does not silently strengthen any of those statements. Relative to the original §7 it weakens the order-two differential claim (rank at most three, not rank zero from vanishing load columns) while keeping non-transversality. The square locus `(E.2)` is new content in the replacement paragraph, not a change to the fibre.

Residual conflict, confined to the immutable original: §7 still prints the false equalities `(7.2)` and the sentence that the three load derivatives have zero tails. V2 is defined as original plus the erratum’s replacement of exactly that sentence and identity. A reader of the original file alone still sees the false claim; a reader of the charged pair does not. No other original sentence asserts `F_j(K^2)=K^{j/2}` or zero load derivatives. The original firewall already refused reducedness, strict-arc exclusion, Taylor realization, cell closure, and JC2; the erratum’s firewall matches.

Attacks that failed: the erratum rewriting the exceptional fibre to include a square restriction on `K`; the erratum promoting generic rank three, or finite determinacy, or a saturation verdict; a load-bearing use of `(7.2)` in `(0.1)`, `(5.3)`, or Mason; a conflict between “loads vanish on the exceptional divisor” (values) and “load derivatives are generically nonzero” (unscaled Jacobian).

## Finding 5 — depression, characters, gauges, complete loads, `8r_7'=j/u`

**Severity: none.** Independent of the erratum.

Let `m=8`, `n=12`, and after harmless nonzero target scalings `a_8=h^2=u^8`, `b_12=h^3=u^{12}`, `u^4=h`, with `h` monic. The Jacobian coefficient of `y^{18}` receives only the pairs `(8,11)` and `(7,12)`. Writing `A=a_7/u^7` and `B=b_{11}/u^{11}`,

```text
T1=11 a_8' b_11=88 u^{18} u' B,
T2=12 a_7' b_12=12 u^{19} A'+84 u^{18} u' A,
T3=-8 a_8 b_11'=-8 u^{19} B'-88 u^{18} u' B,
T4=-7 a_7 b_12'=-84 u^{18} u' A.
```

Logarithmic pairs cancel, leaving `4 u^{19}(3A-2B)'`. Characteristic zero and `u\neq 0` force `delta:=3A-2B` to be a `d/dx`-constant. Depression `z=u y+A/8` kills `[z^7]f` and puts `[z^{11}]g=B-(12/8)A=-delta/2`.

Let `e` be the order of monic `h` in `L(x)^*/L(x)^{*4}`. A generator sends `u\mapsto zeta u` with `zeta` primitive of order `e`. Then `wt(A)\equiv wt(B)\equiv 1\pmod{e}`, so `wt(delta)\equiv 1`. The constant field of `L(x)(u)` equals `L` for monic `h`. A weight-one constant vanishes for `e>1`, including the genuine quadratic leaf `e=2` (`h=v^2` with `v` monic and not a square; the extension is quadratic and only parity weights exist). The monic-core qualification is load-bearing and is supplied by the target’s own scalings.

Thus `R_0:=A/8` is Kummer-invariant. Taylor polynomiality of `[y^7]P=8 h^2 R_0` puts `R_0\in L(x)` with finite poles only over zeros of `h`. Subtracting its polynomial part at infinity by `(x,y)\mapsto(x,y-q(x))` makes `R_0` regular at infinity and does not change `f`, the `a_i`, the Kummer class, or the Keller property.

The generator sends `z\mapsto zeta z` and `w\mapsto zeta w`, so `r_ell` has character `zeta^ell` and a Faber constant `h_j` can be a nonzero constant only for `e\mid j`. Over a characteristic-zero differential field, `deg_z(f_x g_z-f_z g_x)<=m-2` plus descending triangularity of `[f_z w^j]_+` forces every `h_j'` to vanish. The remaining identity is triangular of determinant `8^7` on `(r_1',...,r_7')`, with terminal row `A_7=8`. Differentiating `H_F(w)-g(z(w))` at fixed `w` (hence fixed `f`) produces the plus sign on the tail, and `J_{(x,y)}(P,Q)=u D=j` gives

```text
r_1'=\cdots=r_6'=0,     8 r_7'=j/u.
```

Differential constants of character not `1` vanish, so the complete allowed tail pattern is exactly `(2.5)`. No mod-four filter may be imposed on the order-two leaf.

Because `n<2m`, the three gauges `P\mapsto P+q`, `Q\mapsto Q-h_8 P`, and `Q\mapsto Q-h_0` slice `h_4`, `h_8`, and `h_0`. Remaining constant indices:

```text
e=4: allowed {0,4,8}, all gauged, H_F(w)=w^{12};
e=2: allowed {0,2,4,6,8,10}, gauges kill {0,4,8},
     H_F(w)=w^{12}+k_10 w^{10}+k_6 w^6+k_2 w^2.
```

This is source typing, not a fibre classification.

Attacks that failed: a surviving logarithmic term in the `y^{18}` row; a nonzero forced `delta` on a nontrivial monic-core leaf; treating the order-two leaf as a degenerate quartic; absorbing `mu_4` into a remaining gauge; `8r_7'=-j/u` (the plus sign is forced by the series convention; the `H=4` residue obstruction would survive a global sign flip in any case).

## Finding 6 — ramification at infinity, `(3.2)`, residue, regularity for `U>=2`

**Severity: none.**

Put `q=1/x` and `H=4U` with `U>=1` an integer. The ramification index of a Kummer extension of order `e` at a place `v` is `e/\gcd(e,v(\mathrm{radicand}))`.

- Order four: radicand `h`, `v_\infty(h)=-4U`, index `4/\gcd(4,4U)=1`.
- Order two: radicand `v` with `h=v^2` monic of degree `2U`, `v_\infty(v)=-2U`, index `2/\gcd(2,2U)=1`.

Every place above `q=0` is unramified, so `q` is a uniformizer. On a selected sheet `t=q^U u` satisfies `t^4=q^{4U}h(q^{-1})` or `t^2=q^{2U}v(q^{-1})`, a unit congruent to one. From `dR_7/dx=j/(8u)` and `dx/dq=-q^{-2}`, substitute `u=t q^{-U}`:

```text
dR_7/dq=-(j/8) q^{U-2} t^{-1}.
```

For `U=1` the residue on any sheet is `-(j/8)zeta^{-1}\neq 0`. A meromorphic differential of a rational function on a smooth curve has residue zero at every place, and `R_7` lies in the Kummer function field. Both nontrivial `H=4` clients are empty.

Finite multiplicity four is the only finite logarithmic place of `dx/u` on an unramified chart: if `v_a(h)=4` then `dx/u` has residue a unit. Vanishing of residues is only necessary; the full condition is exactness of `dx/u`. For `U>=2` the right-hand side of `(3.2)` is holomorphic, so `R_7` is regular at `q=0` (the residual additive constant has character `7\bmod e\neq 0` and vanishes). Remaining targets are scalars.

Attacks that failed: hidden ramification at infinity; a residue obstruction at every finite zero of `h`; treating `U=2` as logarithmic; promoting residue vanishing to a global classification of exact `dx/u`.

## Finding 7 — bounded-pole degrees, gcd, classical split

**Severity: none** for the degree identities. Citation precision recorded above, not a break.

The unit `t` does not change pole orders of the `a_i`. Under `d_i<=(U+1)(8-i)` and `R_0` regular, a summand indexed by `i>=ell` in `[y^ell]P` has pole order at most `8(U+1)-ell`, so `deg P<=8(U+1)`. The top term `[y^8]P=h^2` has ordinary total degree `8(U+1)` and cannot cancel.

For `Q`, assign `wt(z)=1`, `wt(a_i)=8-i`, `wt(k_j)=12-j`. Every monomial of the fully loaded `(2.6)` has weight twelve. After `z=u(y+R_0)`, with `k_j` finite scalars, the pole order of a `z^s` coefficient is at most `12(U+1)-s`. The top term `[y^{12}]Q=h^3` gives equality. Thus `(deg P, deg Q)=(8(U+1),12(U+1))` with gcd `4(U+1)`, including the order-two partner.

Heitmann’s necessary condition `gcd>=16` yields `U<=2` for classical closure of this sector. Combined with Finding 6, the bounded sector is empty for `U=1` by residue and counterexample-closed for `U=2`. For `U>=3` both the bounded lane and the strict lane `alpha>U+1` remain live. Prime total gcd and total gcd `2p` never fire on `4(U+1)`. One must not copy the D1 inference that every client is strict.

Attacks that failed: cancellation of `h^2 y^8`; the `k_j` inflating poles; the unit `t` changing `d_i`; closing `U>=3` by prime or `2p`.

## Finding 8 — character descent, Rees equations, exceptional fibre is unloaded

**Severity: none.**

With `[a]_e` the least nonnegative residue modulo `e`, set `a_i=t^{[-i]_e}A_i(q)`. Every `A_i` is invariant. Faber equivariance makes `D_ell=t^{[-ell]_e} r_ell(t^{[-i]_e}A_i,k)` invariant, and after reducing `t^e` to the displayed base unit one obtains a polynomial over `L[q]`. Nonzero constant targets occur only at multiples of `e`, where the twist is one; `delta_7` is invariant and regular for `U>=2`. Equivalently `C_i=t^{[-i]_e}A_i`, and vanishing of the descended rows is vanishing of the ordinary rows by an invertible étale/unit change of coordinates at `q=0`. The induced action on `(p,c,r)` is the weight-`(2,3,4)` action reduced modulo `e`, which is `(4.5)`.

Faber homogeneity:

```text
r_ell(lambda^{8-i}a_i, lambda^2 k_10, lambda^6 k_6, lambda^{10} k_2)
 =lambda^{12+ell} r_ell(a,k).
```

All displayed exponents are strictly positive. The descended Rees equations are `(5.3)`. Setting `q=Lambda=0` kills every `k` argument and every regular target times a positive power of `Lambda`, and yields the ordinary unloaded system `(0.1)`. A surviving `r_4=mu_4` on the exceptional divisor would destroy seven-tail vanishing; the scaling prevents that. The strict chart `Lambda=q^{U+1}rho`, sequential saturation by `q` and `rho`, and then by `(B_0,...,B_6)`, is fail-closed in the direction `(5.7)`. A `rho`-unit branch is the bounded wall, not the strict sector. The converse of `(5.7)` is only algebraic boundary accessibility.

Attacks that failed: character exponents of the opposite sign; retaining `mu_4` or the `k_j` as nonzero values on the exceptional divisor; saturating only by `q`; saturating by `pcr` in place of the `B_i`; reading a nonempty `H_strict` as a rational trajectory.

## Finding 9 — Mason reduced support, charts, denominators, `e` versus `n`

**Severity: none.**

On the exceptional fibre the equations are the ordinary unloaded tails `r_1=\cdots=r_7=0` for `g=F_{12}(f)`, independently of `e`. Here `d=\gcd(8,12)=4`, `a=2`, `b=3`, `N=24`. Seven tails give `T=O(w^{-8})`, so

```text
W(z(w)):=(g^2-f^3)(z(w))=(w^{12}-T)^2-w^{24}=-2w^{12}T+T^2=O(w^4).
```

Substitution `z(w)=w+O(w^{-1})` preserves degree and leading coefficient, hence `deg_z W<=D:=4` if `W\neq 0`. Six tails would give bound `5` and Mason equality; all seven are load-bearing. If `W\neq 0` and `D_0=\gcd(g^2,f^3)` has degree `e<=4<24`, the pairwise-coprime triple `A=g^2/D_0`, `B=-f^3/D_0`, `C=-W/D_0` has `deg A=deg B=24-e` and `deg C<=4-e`. Mason–Stothers in characteristic zero yields `24-e<=(8+12)+(4-e)-1=23-e`, a contradiction, including the constant-`W` edge. Thus `g^2=f^3`. Unique factorization with `gcd(2,3)=1` and monicity produce a unique monic `K` of degree `4` with `f=K^2`, `g=K^3`; the missing `z^7` coefficient is `2c_3`, so `K` is depressed. Conversely `K(z(w))=w^4` by uniqueness of the monic fourth root, so `F_{12}(K^2)=K^3` and every tail vanishes. The power map on depressed coefficients is triangular with invertible diagonal `2`, hence an isomorphism onto a closed prime `A^3`. Weights `2,3,4` give `P(2,3,4)`. Expanding the square is `(6.1)`; the normals `(6.2)` invert it. The discriminant-zero locus is included: Mason does not squarefree `K`.

Projective coverage after interior saturation uses the three charts `p\neq 0`, `c\neq 0`, `r\neq 0`. Saturating by `pcr` alone loses every coordinate boundary. For a rational strict slope `m/n` in lowest terms, `n` divides `gcd({2 if p\neq 0},{3 if c\neq 0},{4 if r\neq 0})`, which is `(6.4)`. The numerator `m` is unbounded. Kummer order `e` and Rees denominator `n` are independent: `t(q)` is unramified and becomes `t(epsilon^n)`, introducing no new fractional valuation.

Attacks that failed: six tails sufficing for Mason; a missing axis of `P(2,3,4)`; `n\mid 8` from `B_0` enlarging the `p=c=0` wall; a forced identification of `e` with `n`; promoting reduced support to reducedness of the tail ideal.

## Attacks that did not land on V2

- A hidden `\partial w/\partial k_j` in the load derivative.
- Sign reversal of `H_F-g`.
- Vanishing of `[K^{3/2}]_-` or `[K^{5/2}]_-` without `K` a square.
- Extra or missing points on the square locus among degenerate quartics.
- A non-square whose seven-row `k_2` column is zero.
- Failure of `(7.1)` at first order.
- Order-two transversality from a three-dimensional kernel in a ten-dimensional domain.
- Finite-determinacy promotion from rank at most three.
- The erratum altering §§0–6, the unloaded fibre, Mason support, Rees equations, charts, denominators, or the firewall.
- Resurrection of original `(7.2)` as a statement about `\partial Phi/\partial k_j` at `Lambda=0`.
- A surviving depression mismatch; a mod-four filter on the order-two leaf; ramification at `x=\infty`; a zero residue of `(3.2)` at `U=1`; inexact bounded degrees; closure of the `U>=3` bounded lane by prime gcd or gcd `2p`; a surviving `mu_4` on the exceptional divisor; sufficiency of six tails for Mason.

## Strict scope firewall

This review licenses the V2 theorem: source typing of the coefficient-infinity exceptional equations, their reduced common-quartic support, the exact bounded-pole degree formula, the `U<=2` portion of that sector under Heitmann, the residue exclusion of nontrivial `H=4`, the design of the strict saturation, the repaired load-direction identity `[K^{j/4}]_-`, the exact square locus `(E.2)`, and first-differential non-transversality of both clients (rank `0` for order four, rank at most `3` for order two). It does **not**:

- prove that the seven-tail ideal is reduced, or determine embedded or nilpotent structure;
- exclude a strict arc for `U>=2`, or solve the bounded sector for `U>=3`;
- classify the global exactness condition on `dx/u` beyond the logarithmic places treated in Finding 6;
- discharge either original Taylor-boundary family, turn a Puiseux arc into a rational constant-field section, or emit an `(8,12)` compiler;
- close the order-one leaf, the whole `(8,12)` cell, maximum twelve, or JC2;
- promote reduced support, or rank deficiency of `d\tau`, to finite determinacy, lifting, Taylor realization, or cell closure;
- claim that the three load columns are linearly independent, or that generic rank equals three.

The original firewall, the erratum firewall, and this review agree on that boundary.

---

## Sources actually used

Read in full before any verdict. Used as definitions, residual routing, high-row identities, character tables, and the statement of Mason–Stothers, never as a conclusion or `PASS`/`CONFIRMED`/`REPAIR` string.

| Artifact | Independently recomputed SHA-256 |
|---|---|
| `xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md` | `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e` |
| `xmodel/max12-812-order24-coefficient-infinity-source-audit-erratum-v2-20260825.md` | `aa90155ec8a182f4f451c77fc9548cf8035889efc230afdaea622f84eb18c495` |
| `xmodel/max12-812-order24-coefficient-infinity-review-grok-20260825.md` | `2f0a03a99ba6563034cdaf84ffc06f6d78ddd377144201d40aa4352ac71c6b55` |
| `xmodel/max12-partial-y-kummer-preflight-20260824.md` | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` |
| `xmodel/max12-partial-y-shared-faber-probe-20260824.md` | `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036` |
| `xmodel/max12-general-faber-exceptional-support-mason-20260825.md` | `7d5271e8caf6d6d071819e8b2a670ac79d2063882a90d4916060b3e4deb95919` |

The first review was opened only because the launch listed it. Its verdict string is not evidence. No D1 compiler, no `(9,12)` degree-split, and no producer replay was consumed as evidence. Mason–Stothers for seven tails is rederived in Finding 9. The Faber polynomial is `F_j=[w^j]_+` as in the shared high-row probe; the tail sign is that of `H_F(w)-g(z(w))`.

---

## Model identity and evidence boundary

Reviewer: Grok 4.6, released by xAI. Independent hostile rederivation of the V2 theorem (original source audit plus the narrow erratum). Every charged review was opened only because the launch listed it; its verdict string was not used. No prior stdout, no CAS, no solver, and no Python reconstruction was used as evidence. The load-bearing chain is the monic-core Kummer split, the universal high-row identity with positive terminal row `8r_7'=j/u`, the three character-compatible target gauges, the unramified unit `t=q^U u`, the chain rule for `dR_7/dq`, exactness of residues, the Faber grading of the fully loaded partner, Heitmann’s necessary gcd bound as a classical input, the unit descent `(4.2)`, Rees homogeneity of weights `12+ell` and `12-j`, Mason–Stothers on seven tails, the binomial first variation `(7.1)`, and the unscaled load derivative `w^j-F_j(z(w))=[K^{j/4}]_-` with UFD square-equivalence and explicit `(E.2)`.

CONFIRMED
