# Hostile review: Opus5 new `q`-gate sharpenings (branch-Q `q1`, weight-3, transversality, `q2`, cascade)

Reviewer: Grok 4.6 (different-model hostile referee)
Date: 2026-08-27
Pinned model ID: `grok-4.6`
CLI/version: `grok 1.0.5 (5115b46bc909)` (`/Users/dc/.grok/bin/grok`)
Host: Python 3.14.6, Darwin 23.6.0 arm64
Charged source:
`xmodel/ggv-survivor-q1-q2-de-rham-gates-fable5-hostile-review-opus5-20260827.md`

## Overall verdict

The five new Opus5 sharpenings survive as desk-tier mathematics after independent rederivation, with one load-bearing hypothesis missing from the boxed branch-Q `q1` statement and with the usual degeneration-stratum caveats made explicit. Nothing charged is REFUTED. No face, landing, Keller, or JC2 conclusion is drawn.

| # | Charged new claim | Verdict |
|--:|---|---|
| 1 | Branch-Q `q1`: `T_Q(Q)=4ABQ'-(6A'B+AB')Q`, `deg Q<=11`, injective, rank 12 / codim 4, genus 3 | **CONFIRMED** on squarefree coprime `(A,B)`. **GAP/REPAIR:** boxed theorem omits `A` squarefree, which is load-bearing; degenerate strata drop the codimension |
| 2 | Branch-P weight-3: poly `D1=D2=D3=0` iff `A^2\|F1` (conditioned on squarefree `A`) | **CONFIRMED** as a *row-3* gate, both directions, with `ker L_2` tracked. Not a claim about rows `>=4` |
| 3 | Intersections `9`, `5`, `7` and the displayed bases | **CONFIRMED**, uniform on the squarefree (coprime) loci, not fixture-only |
| 4 | `q2` trace descent; residue-map surjectivity; linear codim 4 (P) / 5 (Q) on `F2`; affine solvable for every `F1` | **CONFIRMED**. Linear-image codimension is not an `F1` cut |
| 5 | `R_n=G_n-(3/2)HF_n`, `D_n=L_n(R_n)+mixed_n(F_<n,R_<n)`, poly kernels even `n<=12` on P and `n=4,8,12` on Q | **CONFIRMED**. Does *not* linearise or eliminate the accumulated nonlinear system |

Dependence on the already-promoted Fable branch-P squarefree `q1` theorem is used only in item 3 (for `dim im T_A=13`) and is labelled there. That theorem was not re-reviewed.

---

## Custody and execution disclosure

Full-file SHA-256 of the charged source, recomputed on live bytes:

```text
46736edc8aa391e50d3c6a1604937bcad85361c25c25f9e3b4c184e19f8afed1  xmodel/ggv-survivor-q1-q2-de-rham-gates-fable5-hostile-review-opus5-20260827.md
```

This matches the pin exactly.

This session had a shell. I wrote and ran only my own pure-Python exact (`fractions.Fraction`) desk scripts in `/tmp/g46q`; no producer or Opus code was executed, no `sympy`/`flint`/Gröbner engine was used, no AWS was launched, no canonical ledger was edited, and `jc2-lean` was not read, touched, or status-inspected. I did not perform a git/status scan. Script manifest (desk-scale, seconds each):

```text
33dc753baac187fc75464d56ba42cc2884b40d0bbbee3ce5ebb040459ec2c16e  /tmp/g46q/poly.py         exact Q[X] + rref/nullspace
edc9439539f6337ec139b87c6c89a2c4b53dc8ac16f7da8f8288cb98ec001023  /tmp/g46q/replay_key.py   key-number replay
```

Replay: `PYTHONPATH=/tmp/g46q python3 /tmp/g46q/replay_key.py`. Scripts are supporting evidence only; every identity quoted below has a hand derivation. Producer and Opus `[desk-checked]` tags were treated as claims, not evidence.

Consumed formulas, rederived rather than trusted: the D3 raw windows
`F_n: max(0,ceil((n-8)/3)) <= i <= 16-n` (so the `F1` window is `deg<=15`, dimension 16, and the `F2` window is `deg<=14`, dimension 15) and
`G_n: max(0,ceil((n-12)/3)) <= i <= 24-n`;
the chart row
`D_n = sum_{i+j=n} [(12-j) F_i' G_j + (i-8) F_i G_j']`
with `F_0=H^2`, `G_0=H^3`;
and `L_n(G)=2H[(12-n)H'G-4HG']` (the `(0,n)` summand). R7R1 remains PROVISIONAL; `q1`/`q2` statements are licensed only when `D23`/`D24` are imposed. The weight-3 and cascade claims need only `D1..D3` and the row formula.

Firewall: no face exclusion, landing, Keller pair, counterexample, or JC2 conclusion is inferred. The 16-dimensional `F1` window is the frozen D3 fixture window.

---

## Item 1 — Branch-Q `q1` operator

**Verdict: CONFIRMED** on `char K=0`, `deg A=3`, `deg B=2`, **both squarefree**, `gcd(A,B)=1`. **GAP/REPAIR** on the boxed statement, which lists `B` squarefree and coprime but not `A` squarefree; that omission is load-bearing. Degenerate strata drop the codimension (table below). Genus 3 is CONFIRMED under the same hypotheses, as an interpretation of the cover, not as a second complete count of the four cut functionals.

### 1.1 Setup and the displayed operator

`H=A^2 B`, `p^4=H`, `q1=F1/(4p^5)`. Since `p^{-5}=p^3/H^2`,

```text
q1 = F1 p^3 / (4 H^2).
```

This is the `i=3` component in the `K(X)`-basis `1,p,p^2,p^3` of `L`, which is a basis once `[L:K(X)]=4`. For `x^4-H` over `K(X)` in characteristic not 2, irreducibility is the standard criterion: `H` is not a square and `-4H` is not a fourth power. Squarefree coprime `(A,B)` gives both: `A^2 B` is a square iff `B` is a square, and the valuation of `-4A^2 B` at a simple root of `B` is `1`, not divisible by 4. **CONFIRMED** as a hypothesis, not a tautology of `deg A=3`, `deg B=2`.

With `p'=H'p/(4H)`,

```text
d(f_i p^i) = p^i [ f_i' + (i/4)(H'/H) f_i ] dX,
```

so `[q1 dX]=0` is the rational ODE

```text
(*)   f_3' + (3/4)(H'/H) f_3 = F1/(4 H^2).
```

**Primitive completeness, squarefree coprime locus.** At a place off `H`, a pole of `f_3` of order `m<0` makes `ord(f_3')=m-1` strictly worse than `ord((H'/H)f_3)`, so the left-hand side of `(*)` has a pole while the right-hand side is regular. At a root of multiplicity `e`, the indicial coefficient is `m+3e/4`. For `e in {1,2}` this never vanishes at integer `m`; combined with `ord(RHS)>=-2e` one gets `m>=-3` at simple roots of `A` (`e=2`) and `m>=-1` at simple roots of `B` (`e=1`). Thus `A^3 B f_3` is regular at finite places: `f_3=Q/(A^3 B)` with `Q in K[X]`. Substituting and clearing (hand) produces exactly the displayed operator

```text
F1 = T_Q(Q) := 4AB Q' - (6 A' B + A B') Q.
```

**CONFIRMED**, including the sign of the `AB'` term.

Higher-pole ansatze `f_3=Q/(A^a B^b)` with `(a,b)` in `{(3,2),(4,1),(4,2),(5,2),(6,3)}` produce no additional polynomial `F1` of degree `<=15` on the squarefree coprime locus (remainder-kernel computation, two fixtures). The `(2,1)` ansatz is the subspace `A\|Q` and has rank 9. Completeness of `(3,1)` is therefore not an artefact of truncation.

**Degree bound, forced.** Let `deg Q=d`. The four displayed summands of `T_Q` all have degree `d+4`, with leading coefficient `4(d-5)\,lc(A)lc(B)lc(Q)`. Resonance at `d=5` drops the degree (on the R5 pair, `T_Q(X^5)` has degree 7, not 9) but does not produce a kernel. For `d\neq 5`, `deg T_Q=d+4`, so `deg F1<=15` forces `d<=11`; `d=5` is already inside that range. Domain dimension 12.

**Injectivity.** `T_Q(Q)=0` rearranges to `Q'/Q=(3/2)A'/A+(1/4)B'/B`, i.e. `Q^4 \sim A^6 B`. On squarefree coprime `(A,B)` the valuations 6 (at `A`-roots) and 1 (at `B`-roots) are not divisible by 4, so the kernel is empty over any characteristic-zero field. Exact criterion, slightly sharper than "empty": `A^6 B` is not a fourth power in `K(X)`. At these degrees that is equivalent to the squarefree-coprime package. Nullspace of the `12\times 16` matrix is trivial on five fixtures, and remains trivial for `deg Q<=20`.

**Rank 12, codimension 4.** Injective linear map `K[X]_{<=11} \to K[X]_{<=15}` has rank 12; the target has dimension 16. **CONFIRMED**, uniform on the locus, not fixture-only. Independently reproduced for

`A=X^3-(2/5)X`, `B=X^2-1` (R5 pair);
`A=5X^3-4X^2+X+1`, `B=X^2-1`;
`A=X^3+X+1`, `B=X^2+X+3`;
`A=X^3-2`, `B=X^2-3`;
`A=X^3-X`, `B=X^2-2`.

### 1.2 Genus 3

`K(X)(p^2)=K(X)(\sqrt{B})` is the conic `C_0: y^2=B`, smooth of genus 0 iff `B` is squarefree, with two points at infinity (`deg B` even). Then `L=C_0(\sqrt{Ay})`. On `C_0`, `Ay` has odd order at the six points over the three simple roots of `A` (unramified double cover of `P^1` there) and at the two zeros of `y`, and even order `-4` at each infinity. Hurwitz for the double cover: `2g_L-2=2(-2)+8=4`, so `g_L=3`. **CONFIRMED**, and the coprime-squarefree package is used twice: three distinct `A`-roots, two distinct `B`-roots, no collisions. This identifies the curve on which the row lives. It is *not* a second proof that the window-codimension is 4: `dim H^1_{dR}=6`, and the algebraic count 4 is smaller because `ω=q1 dX` is a single Kummer component with constrained poles. Opus did not claim `2g+residues=4`. I do not either.

### 1.3 Missing hypotheses and exceptional strata — GAP/REPAIR

The boxed theorem in the charged source lists `deg B=2` squarefree and coprime, `[L:K(X)]=4`, genus 3. It does **not** list `A` squarefree. That is load-bearing:

- If `A` has a double root and `B` does not vanish there, `H` has a root of multiplicity `e=4`, indicial `m+3=0` at `m=-3`, and the `(3,1)` ansatz undercounts.
- If `gcd(A,B)\neq 1`, `e=3` at the shared root; `ord(RHS)>=-6` so `m>=-5`, while `A^3 B` supplies only order 4, so `Q/(A^3 B)` undercounts. Genus also drops (six odd-order points rather than eight; `g=2`).
- If `B` is a square, `C_0` is singular and extra primitives appear.

Complete-pole dimensions in the 16-dimensional `F1` window (supporting script; each row is a remainder-kernel computation, not a truncated projection):

| `(A,B)` | squarefree coprime? | dim exact `F1` | **codim** |
|---|---|--:|--:|
| R5 pair / generic cubics | yes | 12 | **4** |
| `A=X(X^2-1)`, `B=X(X-3)` (shared root) | no | 13 | 3 |
| `A=X^2(X-1)`, `B=X^2-2` (`A` double) | no | 13 | 3 |
| `A=X^3`, `B=X^2-1` (`A` a cube) | no | 14 | 2 |
| `A=X^3+1`, `B=X^2` (`B` a square) | no | 13 | 3 |

On every degeneration the `(3,1)` operator `T_Q` still has rank 12 (the map on `deg Q<=11` does not see the extra poles); the *true* exact-`F1` dimension is strictly larger. Promoting "codimension exactly 4" off the squarefree coprime locus would be a false statement. This is the same species of repair Opus correctly supplied for branch P, and did not supply here.

Char 0 is used for the indicial arithmetic (`3e/4`) and for `4(d-5)`.

### 1.4 Fills

R5 pair `A=X^3-(2/5)X`, `B=X^2-1`, `AB=(2/5)X-(7/5)X^3+X^5`.

| fill | in `im T_Q` | `AB\|F1` | role |
|---|---|---|---|
| `F1=T_Q(1)= -(6A'B+AB') = -12/5 + (106/5)X^2 - 20 X^4` | yes | no | **positive** for `q1`; separates from weight-2 |
| `F1=T_Q(AB)` | yes | yes | positive for both |
| `F1=1` | **no** | no | **negative** for `q1` |
| `F1=AB` | **no** | yes | **load-bearing separator**: weight-2 gate `AB\|F1` does not imply `q1` |
| `F1=AB\cdot X^{10}` | no | yes | same separator at the top of the window |

The same pattern holds on `A=X^3+X+1`, `B=X^2+X+3`: `T_Q(1)` in, `F1=1` out, `F1=AB` out, `T_Q(AB)` in. Not fixture-only.

---

## Item 2 — Branch-P weight-3 gate `A^2 | F1`

**Verdict: CONFIRMED** as a statement about polynomial solutions of `D1=D2=D3=0` on branch P with `A` squarefree of degree 4. Necessity is a hand proof; sufficiency is exact linear algebra on the windows, uniform on four squarefree quartics, not only `A=X^4-1`. Every displayed coefficient checks. This is a **row-3 gate**. It is not a claim about rows 4–14, and I did not test those rows.

**Premise (rederived, not consumed).** `L_n((3/2)HF)=-3H^2[4HF'+(n-8)H'F]`, which is minus the `(n,0)` summand of `D_n`. Hence `R_n:=G_n-(3/2)HF_n` absorbs `F_n` from its own row. `ker L_n=<H^{(12-n)/4}>`. On `H=A^2` this is polynomial precisely for even `n<=12`, equal to `A^{(12-n)/2}`, and lies in the `G_n` window (`deg=24-2n<=24-n`). In particular `ker L_1` has no polynomial mode, so `D1=0` forces `G_1=(3/2)HF_1` uniquely. Then

```text
mixed_2 = 11 F1' G1 - 7 F1 G1' = 6 H F1 F1' - (21/2) H' F1^2,
L_2((3/8) F1^2 / H) = - mixed_2,
ker L_2 = <A^5>,
```

so `R_2=(3/8)F1^2/H + c_2 A^5` is polynomial iff `H\|F1^2`. Squarefree `A` upgrades this to `A\|F1`. Write `F1=AR`. Then `R_2=(3/8)R^2+c_2 A^5`. All of this is inside the `G_2` window (`deg<=22`). Independently verified on random data.

### 2.1 Displayed weight-3 coefficients

Pairs with `i+j=3` and `i,j>=1`:

```text
mixed_3 = 10 F1' G2 - 7 F1 G2' + 11 F2' G1 - 6 F2 G1'.
```

**CONFIRMED** by expanding the chart row. With `F1=AR`, `G1=(3/2)A^3 R`, `G2=(3/8)R^2+c_2 A^5+(3/2)A^2 F2`, reduction modulo `A` kills every term except `10 F1' G2`, and `F1'\equiv A'R`, `G2\equiv(3/8)R^2`, so

```text
mixed_3 ≡ (15/4) A' R^3   (mod A).
```

**CONFIRMED**, and independent of `F2` and of `c_2` (the `c_2 A^5` piece is `0 mod A^5`). So `ker L_2` cannot cancel the row-3 obstruction.

On `H=A^2`,

```text
L_3(G) = 4 A^3 (9 A' G - 2 A G').
```

**CONFIRMED** (expand `L_3=2H[9H'G-4HG']` with `H'=2AA'`). Hence `im L_3 \subseteq A^3 K[X]` among polynomials. `ker L_3=<H^{9/4}>=A^{9/2}\sqrt{A}` is not polynomial for squarefree `A`, so `L_3` is injective on the `G_3` window `deg<=21`. Resonance of the leading coefficient of `9A'G-2AG'` is at `deg G=18` (degree drops from 33 to 29 on `A=X^4-1`); it does not create a kernel.

### 2.2 Necessity

`D3=0` requires `mixed_3 in im L_3 \subseteq A^3 K[X]`, hence `A\|mixed_3`. Then `A\|A'R^3`; squarefree `A` gives `gcd(A,A')=1`, so `A\|R`, so `A^2\|F1`. **CONFIRMED**. Squarefreeness is the whole upgrade, as in the `q1` theorem on this branch.

If only `A\|F1` and not `A^2\|F1`, then `mixed_3\equiv(15/4)A'R^3\not\equiv 0 mod A`, so `D3` is unsolvable for any polynomial `(F2,c_2,G_3)`.

### 2.3 Sufficiency, kernels, nonuniqueness

Conversely, if `A^2\|F1` write `F1=A^2 S`. Then every summand of `mixed_3` has `A`-adic valuation at least 3 (the `(1,2)` terms contribute valuation `>=3` from `F1'` of valuation 1 against `G2` of valuation 2; the `(2,1)` terms have `G1=(3/2)A^4 S` of valuation 4). So `A^3\|mixed_3` is automatic, and the only remaining question is membership in `im L_3` inside the windows.

Exact linear algebra on unknowns `(F2, c_2, G_3)` of dimensions `15+1+22=38`, target coefficients through degree 36: for every tested `F1` with `A^2\|F1`, including generic degree-7 multipliers and the top-window monomial `A^2 X^7`, the inhomogeneous system is solvable. When it is solvable, the map `(F2,c_2,G_3)\mapsto mixed_3+L_3(G_3)` has rank 22 (equal to `dim` of the `G_3` window) and nullity 16 `=15+1`. So:

- `F2` remains **free** in its 15-dimensional window (row 3 does not spend `F2`);
- `c_2` remains **free** (`ker L_2` is not killed at row 3);
- `R_3` (equivalently `G_3` at `F3=0`) is **unique**;
- `F3` is gauge in its own row, as in item 5.

This was reproduced for `A=X^4-1`, `A=X^4+X^3+X+3`, `A=X^4+7`, and `A=X^4+2X^3-X^2+5X-2`. I do not have a closed-form particular `R_3`; sufficiency is the linear-algebra fact above, not a generating-function identity. Opus's table is a special case.

### 2.4 Fills (Opus table replayed, plus separators)

On `A=X^4-1`. Here `in im T_A` uses the promoted branch-P `q1` theorem as a labelled premise.

| `F1` | `A\|F1` | `A^2\|F1` | in `im T_A` | weight-3 solvable |
|---|---|---|---|---|
| `A=X^4-1` | yes | no | no | **no** |
| `A X=X^5-X` | yes | no | **yes** | **no** |
| `A^2` | yes | yes | no | **yes** |
| `A^2(X+2)` | yes | yes | no | **yes** |
| `A^3` | yes | yes | no | **yes** |
| `A^2 X^7` | yes | yes | yes | yes |
| `0` | yes | yes | yes | yes |
| `T_A(A)=-A A'` | yes | no | yes | **no** |
| `T_A(A^2)=A^2 A'` | yes | yes | yes | yes |
| `T_A(1)=-3A'=-12X^3` | no | no | yes | `D2` already fails |

The two boxed disagreements are the point, and they survive on generic `A` in the form `F1=A^2` (weight-3 yes, `q1` no: `A^2` is not in `im T_A` on any of five squarefree quartics) and `F1=T_A(A)=-AA'` (`q1` yes, `A\|F1` yes, `A^2\|F1` no, weight-3 no). `F1=A X` being in `im T_A` is fixture-dependent (true for `A=X^4-1`, false for `A=X^4+X^3+X+3`); the dimension counts in item 3 are not.

**Row-3 versus later rows.** Nothing here constrains `D4..D14`. Whether the cascade eventually implies `im T_A` is open. I do not promote a "weights 1–3 plus `q1` cut the window to 5 dimensions" slogan beyond the linear intersections of item 3 plus this row-3 gate.

---

## Item 3 — Linear intersections / transversality

**Verdict: CONFIRMED**, and **uniform** on the squarefree (coprime) loci, not fixture-only. Closed-form bases exhaust the intersections, by an algebraic argument that does not mention `A=X^4-1`.

**Labelled premise (not re-reviewed):** for squarefree `A` of degree 4, `T_A(Q)=2AQ'-3A'Q` is injective on `deg Q<=12` with `dim im=13` inside the 16-dimensional window.

### 3.1 Branch P, `im T_A ∩ A\cdot K[X]_{<=11}`

`A\cdot K[X]_{<=11}` has dimension 12. If `T_A(Q)` is divisible by `A`, then `-3A'Q\equiv 0 mod A`; squarefree `A` gives `A\|Q`, so `Q=AR` with `deg R<=8`. Direct expansion

```text
T_A(A R) = A (2 A R' - A' R)
```

shows the reverse inclusion. The map `R\mapsto T_A(AR)` is injective (`T_A` is), so the intersection has dimension 9. Equivalently `12+13-16=9`: the sum of the two spaces is the whole window (transverse). Reproduced on five squarefree quartics, all giving intersection 9 and sum 16.

### 3.2 Branch P, `im T_A ∩ A^2\cdot K[X]_{<=7}`

If `A^2\|T_A(Q)` then already `A\|Q`, `Q=AS`, and `A\|(2AS'-A'S)` forces `A\|S`. So `Q=A^2 R` with `deg R<=4`. Expansion

```text
T_A(A^2 R) = A^2 (2 A R' + A' R)
```

gives dimension 5, matching `8+13-16=5`. Same five quartics, all transverse.

### 3.3 Branch Q, `im T_Q ∩ AB\cdot K[X]_{<=10}`

No appeal to the P theorem. `AB\cdot K[X]_{<=10}` has dimension 11; `im T_Q` has dimension 12. If `T_Q(Q)` is divisible by `AB`, then `(6A'B+AB')Q\equiv 0 mod AB`. Mod `A`: `6A'B Q\equiv 0`, and squarefree coprime gives `A\|Q`. Mod `B`: `A B' Q\equiv 0`, so `B\|Q`. Thus `Q=ABR` with `deg R<=6`. Expansion

```text
T_Q(AB R) = AB ( 4 AB R' + (-2 A' B + 3 A B') R )
```

is injective, dimension 7, matching `11+12-16=7`. Reproduced on five coprime squarefree pairs, including the R5 pair and `A=5X^3-4X^2+X+1`, `B=X^2-1`.

### 3.4 Fills

Already in items 1–2, reused as intersection controls.

Branch P, `A=X^4-1`:

- **positive for `q1` and weight-2, not weight-3:** `F1=T_A(A)=-AA'`;
- **positive for all three:** `F1=T_A(A^2)=A^2 A'`, and `F1=T_A(A^2 X^4)`;
- **weight-2 not `q1`:** `F1=A` (also the load-bearing mutation from the charged source: passes `A\|F1`, fails only on the genus-one period);
- **weight-3 not `q1`:** `F1=A^2`;
- **`q1` not weight-2:** `F1=T_A(1)=-12X^3`.

Branch Q, R5 pair: `F1=T_Q(AB)` in both; `F1=AB` in `AB\cdot K[X]` not in `im T_Q`; `F1=T_Q(1)` in `im T_Q` not in `AB\cdot K[X]`.

---

## Item 4 — `q2`: trace descent, residues, linear versus affine

**Verdict: CONFIRMED.** Trace descent does not need `μ_4`. The linear image of exact `F2` has codimension 4 on squarefree branch P and 5 on squarefree coprime branch Q, equal to the number of distinct roots of `H`. The residue map on the 15-dimensional `F2` window is surjective onto those finite residues, so the affine translate is solvable for **every** `F1`: codimension zero on the `F1` window. Degenerate strata drop the linear codimension to the number of distinct roots; on `H=c(X-a)^8` the fill `F2=const` is exact.

### 4.1 Trace descent

`q2=F2/(4H)-F1^2/(16H^3)` lies in `K(X)`. If `df=q2 dX` for some `f in L`, and `L/K(X)` is finite separable (automatic in char 0), the trace `g=Tr_{L/K(X)}(f)/[L:K(X)]` is in `K(X)` and `dg=[L:K(X)]^{-1} Tr(df)=q2 dX`, because every `K(X)`-embedding fixes `X` and commutes with `d`. No roots of unity, no Galois hypothesis, and the argument is available on branch P where `p\mapsto i p` is not a `K(X)`-automorphism. **CONFIRMED**, with the justification weaker than the producer's `μ_4` averaging.

`K(X)` is genus 0, so a rational differential is exact iff all residues vanish (including infinity). The `q2` row is residue calculus on `P^1` on both branches.

### 4.2 Linear image, windows, and residues

`F2` window: degrees `0..14`, dimension 15. **CONFIRMED** from the lattice.

**Branch P, `A` squarefree.** Locally `F2/(4A^2)` has poles of order at most 2 at the four simple roots of `A`, so a rational primitive has poles of order at most 1 there: `g=R/A`. Then `F2=4(AR'-A'R)`. Leading coefficient `4(d-4)lc(A)lc(R)`, resonance at `d=4` equal to the kernel `R=cA`, and `d+3<=14` forces `deg R<=11`. Domain 12, kernel 1, image 11, **codimension 4**. Completeness of `g=R/A` is confirmed by the uniform cleared ansatz `F2 H^K=4(HR'-K H'R)`: dimensions for `K=1,2,3` all return 11; `K=4` over-clears and undercounts.

The four finite residue functionals of `F2 dX/(4A^2)` therefore have rank `15-11=4` (residue theorem makes infinity dependent). Explicitly, at a simple root `α`,

```text
res_α(c dX/(4A^2)) = -c A''(α) / (4 A'(α)^3).
```

For `A=X^4-1`, `α=1`: `A''(1)=12`, `A'(1)=4`, residue `-3/64`. **CONFIRMED**. On the rational-root quartic `A=X(X-1)(X-2)(X-3)` the `4\times 15` residue matrix has rank 4, `F2=1` has all four residues nonzero, and every generator of `4(AR'-A'R)` has vanishing residues.

**Branch Q, squarefree coprime.** Distinct roots of `H`: 3+2=5. At simple `B`-roots the linear differential has pole order 1, so vanishing residue is equivalent to `B\|F2`. The primitive is `g=R/A` (poles only at `A`-roots), giving `F2=4B(AR'-A'R)`. Degree `d+4<=14` forces `deg R<=10`, kernel `R=cA`, image 10, **codimension 5**. Stabilised under the `H^K` ansatz for `K=1,2,3,4`. On `A=X(X-2)(X-3)`, `B=(X-4)(X-5)` the `5\times 15` residue matrix has rank 5.

Opus's table of linear dimensions is confirmed, including the degenerate rows I recomputed with the `K`-ansatz:

| `H` | # distinct roots | dim exact `F2` | linear codim in 15 |
|---|--:|--:|--:|
| `(X^4-1)^2` / generic squarefree `A^2` | 4 | 11 | **4** |
| `(X^2-1)^4` | 2 | 13 | 2 |
| `(X^2(X-1)(X-2))^2` | 3 | 12 | 3 |
| `X^8` | 1 | 14 | 1 |
| R5 / generic `A^2 B` squarefree coprime | 5 | 10 | **5** |
| Q with a shared root, or `B` a square | 4 | 11 | 4 |

So linear `q2` codimension equals the number of distinct roots of `H` on these tests. The squarefree-coprime (resp. squarefree `A`) hypothesis is load-bearing for the numbers 5 and 4.

On `H=X^8`, `F2=1` is exact: `1/(4X^8)\,dX = d(-1/(28 X^7))`, residues at 0 and infinity both vanish. The operator `4(AR'-A'R)` with `A=X^4` is *not* complete on this stratum (it reports a fake codimension 4). Completeness must be re-derived per stratum, as Opus stated for `q1`.

### 4.3 Affine translate versus linear image

The `F1`-dependence of `q2` is the fixed rational differential `-F1^2 dX/(16 H^3)`. Exactness is still vanishing of all residues. The linear residue map on the `F2` window is surjective onto the finite residue space (rank = number of distinct roots = linear cokernel dimension), so for every `F1` there is an `F2` of degree `<=14` cancelling those residues; infinity then vanishes by the residue theorem. Direct solve of the residue equations on the rational-root fixtures succeeds for `F1` in `{0, 1, A, A^2, X^9, X^{15},` generic degree 15`}`. **CONFIRMED**: the affine `q2` row is solvable in `F2` for every `F1` in the window. It imposes **no** condition on `F1`.

A pole-order ansatz `g=Q/A^a` with `a<=4` *fails* for generic `F1` (the inhomogeneous term has poles of order 6, needing `a>=5`). That is an incomplete particular, not a counterexample to affine solvability. Residue matching in the window is the right test.

### 4.4 Fills

- **Linear positive, branch P:** `F2=4(A\cdot 0-A'\cdot 1)=-4A'`. For `A=X^4-1` this is `-16X^3`, in the image.
- **Linear negative, load-bearing:** `F1=0`, `F2=1`. Residues `-3/64` at `X=1` on `A=X^4-1`; not in the linear image on any squarefree `A` tested. This excludes a constant `F2` at `F1=0` on the whole squarefree branch-P locus, not only the fixture, because `A''` cannot vanish at all four roots (`deg A''=2<4`).
- **Affine positive:** on `A=X(X-1)(X-2)(X-3)`, `F1=1` (and `F1=X^{15}`) admits an `F2` in the 15-dimensional window with all four residues of `q2 dX` zero. Same on the rational-root branch-Q pair for five residues.
- **Degenerate exception:** `H=X^8`, `F2=1` *is* exact. The exclusion of `F2=const` is not uniform on all of branch P.

Do not read "row two cuts more" as an `F1` statement. Linear codimension 4 (P) / 5 (Q) is an `F2`-window number. The `F1` cut is 0.

---

## Item 5 — Repaired lower-row architecture

**Verdict: CONFIRMED**, including signs, the factor `3/2`, window containment, the branch-P even-`n` kernel schedule, and the branch-Q schedule `n=4,8,12`. The rewrite does **not** eliminate the nonlinear accumulated problem in earlier `F` and kernel constants, does **not** make G-completion unique below weight 15, and does **not** substitute for `q`-gates or decide a face.

### 5.1 Identities

The `(n,0)` summand of `D_n` is `3H^2[4H F_n'+(n-8)H' F_n]`. The `(0,n)` summand is `L_n(G_n)`. Direct expansion:

```text
L_n((3/2) H F) = 3H^2[(8-n)H'F - 4 H F'] = -3H^2[4H F'+(n-8)H'F].
```

**CONFIRMED** as a polynomial identity for every `n`, independently of the branch. Hence with `R_n:=G_n-(3/2)HF_n` for `n>=1`,

```text
D_n = L_n(R_n) + sum_{i+j=n,\, i>=1,\, j>=1} [(12-j)F_i' G_j + (i-8)F_i G_j'].
```

(The sum skips both `(0,n)` and `(n,0)`.) Substituting `G_j=R_j+(3/2)HF_j` for `1<=j<n` puts the remainder in `F_0,\ldots,F_{n-1}`, `G_0`, and `R_1,\ldots,R_{n-1}`. That is Opus's `mixed_n(F_<n,R_<n)`, with leading data `(F_0,G_0)=(H^2,H^3)` *not* rewritten (`G_0-(3/2)HF_0=-(1/2)H^3`). Verified on random jets for `n=1..14`, and for `n=15..21` with `F_n=0` (so `R_n=G_n`). **CONFIRMED**.

The raw `F_n` slot is gauge **inside its own row**: `D_n` is independent of `F_n` once `G_n=R_n+(3/2)HF_n`. Verified explicitly at `n=5`. It is **not** gauge for later rows: `D_{n+1}` still sees `F_n` through both the `F`-slots in mixed and through `G_n`. Verified: `D_6` depends on `F_5`.

### 5.2 Kernels and windows

`ker L_n` as rational functions is spanned by `H^{(12-n)/4}`. Polynomial kernel:

- **Branch P** (`H=A^2`, `A` squarefree degree 4): polynomial iff `n` even and `n<=12`, equal to `A^{(12-n)/2}`, degrees 20,16,12,8,4,0. Each lies in the `G_n` window. Six free constants `c_2,c_4,c_6,c_8,c_{10},c_{12}`. Direct nullspaces of `L_n` on `K[X]_{<=24}` match, and `L_n(A^{(12-n)/2})=0` as a polynomial identity.
- **Branch Q** (`H=A^2 B` not a square): polynomial iff `4\|(12-n)` and `n<=12`, i.e. `n=4,8,12`, equal to `H^2`, `H`, `1`, degrees 16,8,0, all inside the corresponding `G_n` windows. Nullspaces confirm no polynomial kernel at `n=2,6,10`. Three free constants.

`(3/2)HF_n` lands in the `G_n` window for every `n=1..14`: max degree is exactly `24-n`, min degree of `HF_n` is at least the `G_n` minimum. For `n>=15` the `F_n` window is empty and `R_n=G_n`. **CONFIRMED**.

On a Q-stratum where `B` is a square, extra even-`n` kernels appear; the schedule `n=4,8,12` is for `H` not a square.

### 5.3 What this does and does not eliminate

Does: convert every row `n=1..21` into a first-order linear condition `L_n(R_n)=-mixed_n` on the new `R_n`, with `F_n` absorbed in that row, and with an explicit polynomial kernel schedule. Solvability of each single row, *given earlier data*, is exact linear algebra in the new window.

Does not:

- eliminate `D1..D14` as equations, or replace them by `q`-gates;
- make the accumulated map from earlier `F` and kernel constants linear — `mixed_n` is bilinear in earlier `(F,R)` and quadratic in `F` after substituting the particular `R_2` piece, so the existential problem in the prefix remains nonlinear;
- make G-completion unique for even `n<=12` on P, or for `n=4,8,12` on Q;
- constrain `F2` at row 3 once `A^2\|F1` (item 2);
- license `q1`/`q2` (those still need `D23`/`D24`);
- decide a face, produce a landing, or exclude a Keller pair.

The producer's "unique G-completion for `n=15..21`" remains correct in that range (`ker L_n` is a negative power of `H` there). Extending uniqueness to `n<=14` is the claim this architecture refutes.

---

## Maximum promotable scope

Promotable at **desk tier**, after different-model replay of this review. The `q1`/`q2` atoms remain conditional on R7R1 (PROVISIONAL) and on imposing `D23`/`D24`. The weight-3 gate and the cascade identities are chart-row statements and need only `D1..D3` (any truncation `N>=4`).

> **Theorem (branch-Q `q1` gate).** Let `char K=0`, `A,B in K[X]` with `deg A=3`, `deg B=2`, **both squarefree**, `gcd(A,B)=1`, `H=A^2 B`, `L=K(X)(p)` with `p^4=H` (so `[L:K(X)]=4` and `X^4-H` is irreducible). On the frozen D3 window `F1 in K[X]_{<=15}` (dimension 16), the R7R1 row-one condition `[q1 dX]=0` in `L` holds iff `F1 in im T_Q`, `T_Q(Q)=4AB Q'-(6A'B+AB')Q`, `deg Q<=11`. `T_Q` is injective (a kernel would require `A^6 B` to be a fourth power in `K(X)`), the image is 12-dimensional, and the gate has **codimension exactly 4**. The ansatz `f_3=Q/(A^3 B)` is complete for polynomial `F1` in the window. `L` has genus 3. Off this locus the `(3,1)` ansatz undercounts and the codimension drops.

> **Theorem (branch-P weight-3 gate).** Let `char K=0`, `A` monic squarefree of degree 4, `H=A^2`. Polynomial solutions of `D1=D2=0` are `G_1=(3/2)HF_1` (unique) and `F1=AR`, `R_2=(3/8)R^2+c_2 A^5` with `c_2` free in `ker L_2=<A^5>`. Given that, polynomial `D3=0` is solvable in `(F2,c_2,G_3)` **if and only if** `A^2\|F1`. Then `F2` and `c_2` remain free, `R_3` is unique (`ker L_3` has no polynomial mode), and `F3` is gauge. This is a row-3 statement.

> **Theorem (transversality).** On squarefree branch P, using the promoted `q1` theorem for `dim im T_A=13`: `dim(im T_A ∩ A K[X]_{<=11})=9` with basis `T_A(AR)=A(2AR'-A'R)`, `deg R<=8`; `dim(im T_A ∩ A^2 K[X]_{<=7})=5` with basis `T_A(A^2 R)=A^2(2AR'+A'R)`, `deg R<=4`. On squarefree coprime branch Q: `dim(im T_Q ∩ AB K[X]_{<=10})=7` with basis `T_Q(ABR)`, `deg R<=6`. All three intersections are the whole of those spans (not proper subspaces), and the pairs of spaces are transverse in the 16-dimensional window. Uniform, not fixture-only.

> **Theorem (`q2` row).** Trace descent to `K(X)` holds on both branches without `μ_4`. On squarefree branch P the linear exact-`F2` space has dimension 11 and codimension 4 in the 15-dimensional `F2` window; on squarefree coprime branch Q, dimension 10 and codimension 5. The residue map on that window is surjective, so for every `F1` there exists `F2` in the window making `q2 dX` exact: **codimension 0 on `F1`**. Linear-image codimension is not an `F1` cut. Degenerate exception: `H=c(X-a)^8` has linear codimension 1 and `F2=const` is exact.

> **Theorem (cascade rewrite).** For `n=1..21`, `R_n=G_n-(3/2)HF_n` (`R_n=G_n` for `n>=15`) satisfies `D_n=L_n(R_n)+mixed_n(F_<n,R_<n)`. Polynomial `ker L_n` is `A^{(12-n)/2}` for even `n<=12` on branch P (six constants, all inside the `G_n` windows) and `H^{(12-n)/4}` for `n=4,8,12` on branch Q (three constants). The rewrite is a per-row linear change of variables; it does not linearise the accumulated system and does not uniquely determine `G` at those kernel weights.

Explicitly **not** promotable: any branch-Q `q1` codimension-4 statement off the squarefree coprime locus; any weight-3 claim for non-squarefree `A`, or about rows `>=4`; any `q2` statement that cuts `F1`; any claim that the face decision decouples; any landing, exclusion, Keller pair, or JC2 conclusion.

The 16- and 15-dimensional windows remain D3 fixture windows.

---

## Cleanest exact successor

**S0 (cheap repair, already computed here):** attach the branch-Q degeneration table of §1.3 to the boxed `q1` theorem, and add `A` squarefree to its hypothesis list. That is the only GAP/REPAIR that touches a promotable atom.

**S1 (recommended, same as the charged source):** lower cascade compiler at weights 4–6 on both branches, carrying the kernel constants symbolically. This is strictly cheaper than any `q_n` row (no `D23`) and is the only way to find out whether the cascade eventually implies `im T_A` / `im T_Q`. Desk/exact, no Gröbner, no AWS. I did not run it.

Do not fund a `q2` client as an `F1`-cutting instrument: item 4 settles that it is not one.

---

## Ledger

*What I proved by hand:* the operator `T_Q` from the `i=3` ODE; indicial `m+3e/4`; leading coefficient `4(d-5)`; kernel criterion `Q^4\sim A^6 B`; Hurwitz genus 3; irreducibility of `X^4-H` on the squarefree coprime locus; `L_n((3/2)HF)` and the `(n,0)` cancellation; `mixed_3\equiv(15/4)A'R^3 (mod A)`; `L_3=4A^3(9A'G-2AG')`; necessity of `A^2\|F1` from `A\|mixed_3`; the three intersection bases and their exhaustiveness; trace descent; the residue closed form `-c A''/(4A'^3)`; linear `q2` operators `4(AR'-A'R)` and `4B(AR'-A'R)` with their kernels and degree bounds; affine solvability from residue-map rank; `ker L_n=<H^{(12-n)/4}>` and the two polynomial schedules.

*What is script-only (exact rational arithmetic, no floating point):* the branch-Q degeneration table of §1.3; the weight-3 sufficiency linear systems and the rank/nullity `22/16` on four quartics; the five-plus-five intersection dimension checks; the `q2` `K`-ansatz dimensions and the rational-root residue matrices.

*What I did not do:* weights 4–14 of the cascade; a closed-form particular `R_3`; geometric identification of the four branch-Q `q1` functionals; any statement about whether a face is alive or dead. No canonical ledger was edited; no AWS was launched; no file inside `jc2-lean` was read, touched, or status-inspected; this review is the only repository file written.

---

**Review verdict: all five charged new claims CONFIRMED on the squarefree (coprime) loci, with one GAP/REPAIR — the boxed branch-Q `q1` theorem must list `A` squarefree, and its codimension 4 is exactly that locus. Weight-3 is a row-3 gate, transverse to `q1`. The `q2` row cuts `F2` and not `F1`. The cascade rewrite is an identity, not an elimination of the nonlinear prefix. No face/landing/Keller/JC2 inference.**

---

## Report SHA-256

Self-referential stamps cannot hash themselves, so this is the SHA-256 of the
report **body**: the first 428 lines (through the review-verdict paragraph),
i.e. the file as written before this stamp block was appended.

```text
3c07c0564b4b0ef7a8e46f3752fc3b859440da986e59d334b8a192479f2e21d9
```

Reproduce with:

```bash
head -n 428 xmodel/ggv-qgate-opus-new-claims-hostile-review-grok46-20260827.md \
  | shasum -a 256
```

**Review verdict (restated for the ledger): five new Opus5 claims CONFIRMED
on the squarefree (coprime) loci; GAP/REPAIR that boxed branch-Q `q1` must
list `A` squarefree; no REFUTED atom; no face/landing/Keller/JC2 inference.**
