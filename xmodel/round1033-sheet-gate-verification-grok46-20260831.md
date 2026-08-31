# SHEET-GATE verification — countermodel hunt

**Lane.** Independent verification (countermodels and sanity stress-tests).
**Charged inputs (hashes verified).**
- `6d8f6667fc7d52d1e46fc4ac55f2aa2049603f06c1764ae4ac51b078435d90eb` `round1033-sheet-gate-opus5-20260831.md`
- `2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef` `ideation-20260831T1033Z-synthesis.md`
**Date.** 2026-08-31

## 0. Hash check and charged claims

Both charged SHA-256 digests match (`shasum -a 256`). No CAS. No inspection of `jc2-lean`. No edits to charged files or canonical ledgers.

Standing notation as in the charged report. `F=(F_1,F_2):\mathbb{A}^2\to\mathbb{A}^2` over `\mathbb{C}`; `d=[ \mathbb{C}(x,y):\mathrm{Frac}\,\mathbb{C}[F_1,F_2] ]`; `D=A_F`; `D_0=D\setminus\mathrm{Sing}\,D`; `a=\#F^{-1}(p)` for generic `p\in D_0`; `a_p=\#F^{-1}(p)`; `e_j=\mathrm{ord}_{B_j}(q^*h)`; `b=\sum_{e_j=1}\delta_j`. Compactly supported Euler characteristic `\chi_c` with `\chi_c(\mathbb{A}^n)=1`, `\chi_c(\mathrm{pt})=1`, `\chi_c(\emptyset)=0`, and closed-closed additivity.

No known non-automorphism Keller map exists (that is JC), so every genuine Keller test is an automorphism (`A_F=\emptyset`, `d=1`). Non-Keller maps are used as one-hypothesis-at-a-time controls. A lemma that still holds after its stated hypothesis is dropped is recorded as using less than claimed.

**Charged claims under test.** (M′) `a(\nu+s-1)-\sum_p a_p=d\nu-1` with `1\le a\le d-2`; covering `F^{-1}(D_0)\to D_0` of degree `a`; `a_p=s_p-b_p`; `e_j=1+v_j(dx\wedge dy)` for dicriticals of Keller maps; (E) `1=d\bigl(1-\chi_c(A_F)\bigr)+\chi_c(F^{-1}(A_F))`; (B-w) `\sum_j \delta_j e_j\le d-1` with some `e_j\ge 2`.


## 1. Non-Keller controls (hypotheses fail one at a time)

### 1.1 `F=(x,xy)` — étale fails on a curve; not quasi-finite; `d=1`

Jacobian matrix: `\partial(x,xy)/\partial(x,y)`, `Jac=x`, zero locus the `y`-axis. Inverse on `{u\neq 0}` is `(u,v/u)`, so `d=1` (birational). Not quasi-finite: `F(\{x=0\})=\{(0,0)\}`.

**`A_F`.** Sequence `(1/n,\,cn)\to\infty` has `F=(1/n,\,c)\to(0,c)`. For `u\neq 0` the inverse is a morphism, so `F` is proper over `{u\neq 0}`. Thus `A_F=\{u=0\}\cong\mathbb{A}^1`. (This is the `v`-axis in `(u,v)`-coordinates.) Irreducible, normalisation `\mathbb{A}^1`: (H2)+(H3) hold; Keller fails.

**Fibres.** Generic `p=(0,c)`, `c\neq 0`: empty, so `a=0`. At `(0,0)`: the whole `y`-axis. `F^{-1}(A_F)=\{x=0\}\cong\mathbb{A}^1`.

**Covering lemma.** `D` is smooth, `D_0=D`, and `F^{-1}(D_0)=\{x=0\}` collapses to `\{(0,0)\}`. Not a covering. Failure traces to quasi-finiteness (used for `q` finite and for `a\ge 1` via density of `F(E_i)`). **BROKEN**, correctly, off Keller.

**Ceiling `1\le a\le d-2`.** Here `a=0`, `d-2=-1`. The proof of `a\ge 1` uses quasi-finiteness; the proof of `a\le d-2` uses purity of the branch locus plus étaleness on `U` to force some `e_j\ge 2`. Both fail. **BROKEN**, correctly.

**(B-w).** No finite `q` of degree `1` with a ramified dicritical in the report's sense. If one counts the dicritical computed in §3 (`e=1`, `\delta=1`) then `\sum\delta e=1\not\le d-1=0`. **BROKEN**, correctly, off `a\ge 1`.

**Step 0 / Lemmas 2.1–2.3.** `A=\mathbb{C}[x,xy]\cong\mathbb{C}[u,v]` is integrally closed in `K`, so `B=A`, `Y\cong\mathbb{A}^2`, and `j` is `F` itself, not an open immersion. Lemma 2.1 (`A\subseteq B\subseteq\mathbb{C}[x,y]`) **HOLDS** without Keller. Lemmas 2.2–2.3 (purity of `B_Y`, `A_F=q(B_Y)` via ZMT) **BROKEN**, correctly: ZMT needs quasi-finite.

**(E) and (M′) are computed in §2.**

### 1.2 `F=(x,y^2)` — degree 2, non-étale, proper, `A_F` empty

`Jac=2y`. Finite: `\mathbb{C}[x,y]` is a rank-2 module over `\mathbb{C}[x,y^2]`, so proper and `A_F=\emptyset`, `d=2`. Generic fibre two points; over `{v=0}` one point (ramified).

**(E).** Left side `1`. Right side `2(1-0)+0=2`. **BROKEN.** Failure traces exactly to “`F^{-1}(V)\to V` is an unramified covering”: here `V=\mathbb{A}^2`, and `F` is branched. Multiplicativity `1=\chi_c(\mathbb{A}^2)\neq 2\cdot 1` is the same break.

**Covering lemma / (M′) / (B-w) over `D`.** Vacuous (`D` empty). The automorphism case `F=\mathrm{id}` (Keller, `A_F=\emptyset`, `d=1`) makes (E) hold: `1=1(1-0)+0`. So emptiness of `A_F` is not itself the obstruction; ramification on `V` is.

**Purity “some `e_j\ge 2` over `A_F`”.** No affine-image dicritical. The argument that the branch locus must meet `B_Y` uses étaleness on `A^2\setminus D` *and* on `U`. Here the branch locus `{y=0}` lies in `U=Y`. **Correctly inapplicable.**

### 1.3 `F=(x^2,y)` — étale off a line, still proper

`Jac=2x`, `d=2`, finite hence `A_F=\emptyset`. Restriction `U=\mathbb{A}^2\setminus\{x=0\}\to\mathbb{A}^2\setminus\{u=0\}` is étale of degree 2, non-injective (punctured-surface control). Polynomial (E) still reads `1=2`, **BROKEN** for the same reason as §1.2: ramification lives on `{x=0}\not\subset F^{-1}(A_F)=\emptyset`.

If one instead computes non-properness *of the restriction* `U\to\mathbb{A}^2`, sequences `x=1/n` give `A_F(U)=\{u=0\}=q(B_Y)` with `Y=\mathbb{A}^2`, `B_Y=\{x=0\}`. Then `a=0`, one boundary point of ramification index `2` over generic `(0,c)`, and `\chi_c(U)=0=2\cdot\chi_c(\mathbb{G}_m\times\mathbb{A}^1)+0`. The identity (E) with left-hand side `1` is an `\mathbb{A}^2`-source statement; on a punctured source the same covering arithmetic holds with `\chi_c(U)` in place of `1`. **Finding:** (E) uses `source=\mathbb{A}^2` for the constant `1`, not merely étaleness.

### 1.4 `F=(x,\,y+xy^2)` — quasi-finite, non-proper, Keller fails only off `V` in a weaker sense

`Jac=1+2xy`. Fibres: `u=x`, `v=y+xy^2` rearranges to `u\,T^2+T-v=0`, at most two roots, so quasi-finite. Degree `2`.

**`A_F`.** Set `x_n=(b-y_n)/y_n^2` with `y_n\to\infty`: then `u_n\to 0` and `v_n\to b`. For `u` bounded away from `0` the quadratic inverse stays finite on compacts. Thus `A_F=\{u=0\}\cong\mathbb{A}^1`, (H2)+(H3) hold.

**Fibres over `D`.** `{x=0\}\xrightarrow{\sim}\{u=0\}`: `a=1=a_p` for all `p\in D`. Interior ramification remains: discriminant `{1+4uv=0\}\subset V=\mathbb{A}^2\setminus D`. So `F` is *not* étale on all of `V`, hence not Keller, but it *is* quasi-finite and `A_F` is a line.

**Covering lemma.** `F^{-1}(D_0)\to D_0` is an isomorphism, degree `a=1`. **HOLDS** without Keller.

**Ceiling `a\le d-2`.** `a=1=d-1\not\le 0`. **BROKEN.** This is the essential use of Keller: purity plus étaleness on `V` forces some `e_j\ge 2`, hence `a\le d-2`. Sol-xpoll's `a=d-1` is realised here; it is compatible with quasi-finiteness and (H2)+(H3), and is killed only by Keller.

**(B-w) “some `e_j\ge 2`”.** Over `D` one has `e=1`, `b=1`, `d=a+b=2`, no ramified dicritical. Branch locus is the discriminant, not `A_F`. **BROKEN**, correctly, off Keller. The inequality `\sum\delta_j e_j=1\le d-1=1` still holds.

**(M′) with `\nu=s=0`.** `-a=-1`, so `a=1`. Holds numerically (see §2). The smooth-`A_F` law `a=1` therefore **HOLDS** on a non-Keller quasi-finite map.

### 1.5 Automorphisms (Keller, `A_F` empty) and proper maps with `A_F` empty

`F=\mathrm{id}`: Keller, `d=1`, `A_F=\emptyset`. (E) holds. (M′)/(H2) inapplicable. Prop. 2.5 (`d\ge 3`) uses a branch component of `A_F`; correctly silent.

`F=(x^2,y^2)`: `Jac=4xy`, finite, `d=4`, `A_F=\emptyset`. (E) says `1=4`, **BROKEN**. Same mechanism as §1.2.

### 1.6 One-at-a-time summary

| Control | Hypothesis dropped | Covering | `a\le d-2` | some `e\ge 2` | (E) | (M′) |
|---|---|---|---|---|---|---|
| `(x,xy)` | Keller + quasi-finite | BROKEN | BROKEN (`a=0`) | n/a | HOLDS (§2) | BROKEN (`-a=-1`) |
| `(x,y^2)` | Keller on `V` | vacuous | n/a | n/a | BROKEN | n/a |
| `(x^2,y)` on `U` | source not `\mathbb{A}^2` | n/a | `a=0` | `e=2` on `B_Y` | (E) as written BROKEN; covering form HOLDS with `\chi_c(U)` | BROKEN |
| `(x,y+xy^2)` | Keller on `V` (disc.) | HOLDS | BROKEN (`a=d-1`) | BROKEN | HOLDS | HOLDS (`a=1`) |
| `\mathrm{id}` | (H2) (`D` empty) | vacuous | n/a | n/a | HOLDS | n/a |

**Findings.** (i) The covering lemma and the smooth-`A_F` evaluation of (M′) use quasi-finiteness plus the topology of `D_0`, not the full Keller package. (ii) The ceiling `a\le d-2` and “some `e_j\ge 2`” use Keller on `V` essentially; `F=(x,y+xy^2)` is the explicit `a=d-1` control. (iii) (E) as written uses étaleness on `V` *or* else `\chi_c(V)=0` (accidental vanishing); the latter is why (E) survives on `(x,xy)` and `(x,y+xy^2)`.


## 2. Euler identity (E): direct `chi_c` computation

Theorem 5.2 claims `1=d\bigl(1-\chi_c(A_F)\bigr)+\chi_c(F^{-1}(A_F))` for Keller maps, via `F^{-1}(V)\to V` a degree-`d` covering and 5.1(a)–(b).

### 2.1 `F=(x,xy)`

`A_F\cong\mathbb{A}^1`, `\chi_c=1`. `F^{-1}(A_F)\cong\mathbb{A}^1`, `\chi_c=1`. `d=1`. RHS `=1(1-1)+1=1`. **HOLDS.**

Covering check: `V=\{u\neq 0\}\cong\mathbb{G}_m\times\mathbb{A}^1`, `\chi_c(\mathbb{G}_m)\chi_c(\mathbb{A}^1)=0`. `F^{-1}(V)=\{x\neq 0\}` likewise, `\chi_c=0`. The map is an isomorphism (degree `d=1`). Multiplicativity holds. Keller fails on `{x=0\}=F^{-1}(D)`, which is *not* used.

**(M′).** `a=0`, `s=0`, `\nu=0`, empty sum: `0\cdot(-1)-0=0-1`, i.e. `0=-1`. **BROKEN**, matching `a=0` rather than a `\chi_c` error. Assembly of (M′) used `a=\deg(F^{-1}(D_0)\to D_0)`, which is not a covering here.

### 2.2 `F=(x,y^2)`

`A_F=\emptyset`, `\chi_c=0`. `F^{-1}(\emptyset)=\emptyset`, `\chi_c=0`. `d=2`. RHS `=2`. **BROKEN** (`1\neq 2`). Directly: `\chi_c(\mathbb{A}^2)=1\neq 2\cdot\chi_c(\mathbb{A}^2)`. Hypothesis that fails: unramified covering over `V=\mathbb{A}^2`.

### 2.3 `F=(x,y+xy^2)` (extra, `\chi_c(V)=0` again)

`A_F\cong\mathbb{A}^1`, `\chi_c=1`. `F^{-1}(A_F)\cong\mathbb{A}^1`, `\chi_c=1`. `d=2`. RHS `=2\cdot 0+1=1`. **HOLDS.**

Here `F^{-1}(V)\to V` is *ramified* (discriminant `{1+4uv=0\}`). Multiplicativity is not licensed, yet both sides of `\chi_c(F^{-1}(V))=d\,\chi_c(V)` are `0=2\cdot 0`. **Finding:** (E) is not probed by any control with `\chi_c(A_F)=1`, because the coefficient of `d` vanishes. The only desk control with `\chi_c(A_F)\neq 1` is `A_F=\emptyset` (`\chi_c=0`), where (E) *does* break off Keller.

An affine nodal cubic would give `\chi_c(D)=0` by 5.1(c) (`D^\sim\cong\mathbb{A}^1`, one node, `r_p=2`, `\chi_c=1-1=0`), hence (E) would read `\chi_c(F^{-1}(D))=1-d`. No explicit polynomial `F` with `A_F` a nodal cubic was constructed at desk. **UNTESTABLE-AT-DESK** for singular `A_F` with `\chi_c\neq 1`.

### 2.4 Toolkit 5.1(c) on two elementary curves

Two lines `{xy=0\}`: normalisation `\mathbb{A}^1\sqcup\mathbb{A}^1`, `\chi_c=2`, one point with `r_p=2`, so 5.1(c) gives `2-1=1`. Additivity: `\chi_c(L_1)+\chi_c(L_2\setminus\{0\})=1+0=1`. **HOLDS.**

Node of `y^2=x^2(x+1)` (affine nodal cubic, one infinite place): `D^\sim\cong\mathbb{A}^1`, `r_p=2`, `\chi_c=0`, matching `\chi_c(\mathbb{G}_m)=0`. **HOLDS** as a formula, independently of (E).

### 2.5 Verdict on (E)

On Keller automorphisms: **HOLDS** (both sides `1`). On the two non-Keller controls with `A_F\cong\mathbb{A}^1`: **HOLDS**, because étaleness is used only over `V` *or* `\chi_c(V)=0`. On proper ramified maps with `A_F=\emptyset`: **BROKEN**, and this is the only desk probe of the factor `d`. The proof uses less than “Keller on all of `\mathbb{A}^2`”: it uses a degree-`d` unramified covering over `V=\mathbb{A}^2\setminus A_F` plus `\chi_c(\mathrm{source})=1`.


## 3. Lemma 4.2: valuation formula `v(dx\wedge dy)`

On `\mathbb{P}^2` with `x=X/Z`, `y=Y/Z`,
`dx\wedge dy = Z^{-3}\bigl(Z\,dX\wedge dY - Y\,dX\wedge dZ + X\,dY\wedge dZ\bigr)`,
so `v_{L_\infty}(dx\wedge dy)=-3`. After a blowup at `P`, a rational 2-form pulls back with
`\mathrm{div}(\pi^*\omega)=\pi^*(\mathrm{div}\,\omega)+E`.

### 3.1 Four divisorial valuations at infinity

**(i) Line at infinity.** `v=-3`. Matches the report.

**(ii) One blowup, `P_1\in L_\infty`.** `\pi^*L_\infty=\widetilde L_\infty+E_1`, so
`\mathrm{div}=-3\widetilde L_\infty-3E_1+E_1=-3\widetilde L_\infty-2E_1`. Thus `v_{E_1}=-2`. Matches.

**(iii) Two blowups, free.** `P_2\in E_1\setminus\widetilde L_\infty`. Then `\pi_2^*\widetilde L_\infty=\widetilde{\widetilde L}_\infty`, `\pi_2^*E_1=\widetilde E_1+E_2`,
`\mathrm{div}=-3\widetilde{\widetilde L}_\infty-2(\widetilde E_1+E_2)+E_2=-3L-2\widetilde E_1-E_2`. Thus `v_{E_2}=-1`.

**(iv) Two blowups, satellite.** `P_2=E_1\cap\widetilde L_\infty`. Then `\pi_2^*\widetilde L_\infty=\widetilde{\widetilde L}_\infty+E_2`, `\pi_2^*E_1=\widetilde E_1+E_2`,
`\mathrm{div}=-3(L+E_2)-2(\widetilde E_1+E_2)+E_2=-3L-2\widetilde E_1-4E_2`. Thus `v_{E_2}=-4`.

**Existence of `v` with `v(dx\wedge dy)=0`.** Three free blowups, only `P_1` on `L_\infty`: each free step contributes `c_i=1`, `\sum c_i=3`, only `P_1` meets `L_\infty`, so the report's formula `v=\sum c_i-3\sum_{P_i\in L_\infty}c_i=3-3=0`. Recursively: after the free pair, `v_{E_2}=-1`; blow `P_3\in E_2` off `\widetilde E_1` and off `L_\infty`:
`\mathrm{div}=-3L-2\widetilde E_1-(\widetilde E_2+E_3)+E_3=-3L-2\widetilde E_1-\widetilde E_2`, and `v_{E_3}=0`. **HOLDS.** (All-satellite chain of length `N` gives `v=-2N`; length-3 satellite gives `-6`, not zero.)

### 3.2 `e=1+v(dx\wedge dy)` on `F=(x,xy)`

Indeterminacy of `[XZ:XY:Z^2]` at `[0:1:0]`. Chart `Y=1`, coordinates `(X,Z)`, `x=X/Z`, `y=1/Z`, `dx\wedge dy=-dX\wedge dZ/Z^3`.

First blowup, chart `Z=t`, `X=st` (directions not along `L_\infty`): `dx\wedge dy=-ds\wedge dt/t^2`, so `v_{E_1}=-2`. The map remains indeterminate at `s=t=0`, the free point `E_1\cap\{X=0\}` (strict transform of the `y`-axis).

Second blowup `s=\alpha`, `t=\alpha\beta`: `F` becomes `[\alpha\beta:1:\beta]` in the first chart of §1.1's homogeneous form, i.e. affine `(u,v)=(\alpha,1/\beta)` for `\beta\neq 0,\infty`. Restriction to `E_2=\{\alpha=0\}` is non-constant onto `{u=0\}=\overline{A_F}`: this is the dicritical. Also `dx\wedge dy=-d\alpha\wedge d\beta/(\alpha\beta^2)`, so `v_{E_2}=-1`, matching the free two-blowup.

Local equation of `D=\{u=0\}` pulls back as `u\circ F=\alpha`, so `e=\mathrm{ord}_{E_2}(\alpha)=1`.

Keller form of Lemma 4.2: `1+v(dx\wedge dy)=1-1=0\neq e=1`. **BROKEN** as a Keller formula, correctly: `Jac=x` and `v(x)=1` on this valuation (in the chart, `x=X/Z=s= \alpha`), so the general identity from the report's own local computation is
`e-1=v(Jac)+v(dx\wedge dy)=1-1=0`.
The charged report already records this as a non-Keller sanity (`\mathrm{ord}(Jac)+v=0=e-1`). The lemma as stated for Keller maps is not claimed here; the control confirms the missing `v(Jac)` term.

### 3.3 Second resolvable map: `F=(x,\,y+xy^2)`

From §1.4, `A_F=\{u=0\}`, `e=1` (isomorphism over `D`), `Jac=1+2xy`. Escaping sequences have `x\sim -1/y`, so `1+2xy\to -1` and `v(Jac)=0` along the dicritical.

Resolution at `[0:1:0]`, coordinates `(x'=x/y,\,z'=1/y)`: three blowups, free chain (the third infinitely-near point is the direction `xy=-1`, off `E_1` and off `L_\infty`). By §3.1 this is exactly the `v=0` valuation. Thus `1+v(dx\wedge dy)=1=e`. **HOLDS** even though `F` is not Keller, because `v(Jac)=0` on this divisor.

**Finding.** Lemma 4.2's local proof gives `e=1+v(Jac)+v(dx\wedge dy)` without Keller; Keller is used only to set `v(Jac)=0` (a nonzero constant has valuation `0` at every place). The formula can hold off Keller (`F=(x,y+xy^2)`) and can fail off Keller (`F=(x,xy)`). The existence of a valuation at infinity with `v(dx\wedge dy)=0` is not merely abstract: it is realised as a dicritical of an explicit quasi-finite polynomial map. Closing box `(Y\setminus U,\,e=1)` therefore cannot be a purely valuative prohibition; the report's OPEN at `d=4` transposition class is consistent with this control.

### 3.4 Local proof, checked

At generic `p\in D`, coordinates `(w,t)` with `D=\{t=0\}`; at generic point of `L_j`, `( \xi,z)` with `L_j=\{z=0\}`, `w\circ F=W(\xi,z)` with `W_\xi(\xi,0)\neq 0`, `t\circ F=z^{e}T` with `T(\xi,0)\neq 0`. Then
`d(w\circ F)\wedge d(t\circ F)=e z^{e-1} W_\xi T\,d\xi\wedge dz+O(z^e)`,
so `v(F^*(du\wedge dv))=e-1`. And `F^*(du\wedge dv)=Jac\cdot dx\wedge dy`. No gap at desk in this local algebra. **HOLDS** as a local identity; the Keller specialisation is the only extra step.


## 4. The `d=4` enumeration (Thm 4.4)

Constraints, from the box audit and (H2): `1\le a\le 2`, integers `\delta_j\ge 1`, `e_j\ge 1`, `\sum_j \delta_j e_j=4-a`, some `e_j\ge 2`. (Under (H2) every component of `B_Y` dominates the unique curve `D`, so there are no vertical components to miss.)

Write `N=4-a\in\{2,3\}`.

**`a=2`, `N=2`.** Integer pairs `(\delta,e)` with `\delta e` summing to 2, some `e\ge 2`:
- `(1,2)`: one dicritical, `b=0`.
- `(2,1)`: all `e=1`, forbidden.
- `(1,1)+(1,1)`: all `e=1`, forbidden.

Only `(1,2)`. Cycle type of `g`: fibre points with multiplicities `(e=1,e=1,e=2)` = transposition. `\sigma=a+b=2`.

**`a=1`, `N=3`.**
- One dicritical: `(1,3)` (`e=3\ge 2`, `b=0`); `(3,1)` forbidden.
- Two dicriticals: `(1,2)+(1,1)` (has `e=2`, `b=1`); `(2,1)+(1,1)` all `e=1`, forbidden.
- Three: `(1,1)^3` forbidden.
- `\delta=2` with `e\ge 2`: `2\cdot 2=4>3`, impossible.
- `\delta=2`, `e=1` plus a ramified term: leftover `1`, which forces another `(1,1)`, already listed and forbidden.

So exactly two further profiles: `(1,3)` with `b=0`, `\sigma=1`, cycle type a 3-cycle; and `(1,2)+(1,1)` with `b=1`, `\sigma=2`, cycle type a transposition.

**No missed profile.** In particular no admissible `\delta_j=2` row: the only `\delta=2` partitions of `N\in\{2,3\}` have all `e_j=1`, excluded by purity. A hypothetical `(\delta,e)=(2,2)` needs `N=4`, hence `a=0`, contradicting `a\ge 1`.

**Group-theoretic admissibility of the three.** Cycle types with `\sigma=a+b\ge 1` cannot be a 4-cycle or a double transposition (both fix nothing). That excludes `C_4` and `V_4` as monodromy groups generated by `g`, independently of the generation argument in §5.

The three rows of Theorem 4.4 are complete. **HOLDS.** The residual bit `a\in\{1,2\}` in the transposition class is exactly the `(1,2)` versus `(1,2)+(1,1)` alternative; no further numerical split exists.


## 5. Group theory claims

`G\le S_4` is the monodromy group, transitive (one Galois closure / one field extension of degree 4), and generated by the images of meridians. Under (H2) all meridians are conjugate in `\pi_1(\mathbb{A}^2\setminus D)`, so `G=\langle g^G\rangle`.

Transitive subgroups of `S_4`, up to conjugacy: `C_4`, `V_4`, `D_4` (order 8), `A_4`, `S_4`. (No transitive `S_3`: order would have to be a multiple of 4.)

### 5.1 `g` a transposition `\Rightarrow G=S_4`

`A_4`, `V_4`, `C_4` contain no transpositions.

`D_4` (square `1234`) contains transpositions: vertex reflections `(24)` and `(13)`. The `D_4`-class of `(24)` is `\{(24),(13)\}`, generating `\langle(13),(24)\rangle\cong C_2\times C_2`, not all of `D_4` and not transitive. So `D_4\neq\langle\tau^{D_4}\rangle` for a transposition `\tau`. Hence `G` cannot be `D_4`.

`S_4` is generated by its transpositions, and the conjugacy class of a transposition is all six transpositions. **HOLDS:** a transitive `G=\langle g^G\rangle` with `g` a transposition is `S_4`.

(The coarser slogan “transitive, generated by transpositions `\Rightarrow S_n`” is true because the transpositions define a connected graph on `n` letters; the conjugacy-class refinement is what excludes `D_4`.)

### 5.2 `g` a 3-cycle `\Rightarrow G=A_4`

Only `A_4` and `S_4` contain 3-cycles. The `S_4`-class of a 3-cycle is all eight 3-cycles, generating `A_4`, not `S_4`. So `G=\langle g^G\rangle` cannot be `S_4`.

Inside `A_4` the 3-cycles split into two classes of size 4, and a 3-cycle is not conjugate in `A_4` to its inverse. One class still generates `A_4`: the subgroup generated by a conjugacy class is normal, and the only proper normal subgroup of `A_4` is `V_4`, which has no 3-cycles. **HOLDS:** `G=A_4`.

### 5.3 Local groups `H_p` (§6 item 4)

`H_p` is generated by (images of) local branch meridians, each conjugate to `g`.

**`#\mathrm{Fix}(H_p)=2`.** A subgroup of `S_4` with exactly two fixed points acts on the remaining two letters, so is `1` or `C_2`. Nontrivial `\Rightarrow H_p\cong\mathbb{Z}/2` generated by a transposition. **HOLDS**, with no extra input from the class of `g`. (This cycle type occurs only in the transposition class anyway.)

**`#\mathrm{Fix}(H_p)=1`, no class specified.** Subgroups with exactly one fixed point: the copy of `S_3` (or `A_3`) on the other three letters. `S_3` is generated by transpositions; `\mathbb{Z}/3` is generated by a 3-cycle. Both occur, in different classes. Sol-xpoll's `{ \mathbb{Z}/3,\,S_3 }` **HOLDS** as a class-blind statement. `A_4` itself is transitive, so `#\mathrm{Fix}(A_4)=0` and is not in this list.

**Transposition class (`G=S_4`).** Generators are transpositions, so `H_p\le S_3` on the unfixed triple when there is a global fixed sheet. Then `#\mathrm{Fix}=1` forces `H_p\cong S_3`, not `\mathbb{Z}/3`. The report does not claim otherwise inside this class.

**`A_4` class.** Generators are 3-cycles, so `H_p\in\{\mathbb{Z}/3,\,A_4\}` (no other 3-cycle-generated subgroups: `V_4` has none). **HOLDS.** Filtering by `#\mathrm{Fix}=1` kills `A_4` and leaves `H_p\cong\mathbb{Z}/3`, which is the report's later `nu=0` corollary, not the class-blind item 4.

No desk countermodel to these subgroup lists. **HOLDS.**


## 6. Corollary 3.2 (`a_p = s_p - b_p`) and disk family

Cor. 3.2: `a_p=s_p-b_p` with `b_p=\#\{y\in B_Y\cap q^{-1}(p): e_y=1\}`. Lemma 3.3: `q^{-1}(D_0)\to D_0` is an unbranched covering of degree `c=\#\mathrm{cycles}(g)`, and `B_Y\cap q^{-1}(D_0)` and `F^{-1}(D_0)` are unions of connected components (so no mixed component over a smooth point of `D`).

### 6.1 Disk models (the round's `q:\Delta\to\Delta` family)

**(I) Identity, punctured.** `Y=\Delta`, `q=\mathrm{id}`, `U=\Delta^*`, `p=0`. Then `q^{-1}(0)=\{0\}\subset B_Y`, `e=1`. The covering of `\Delta^*` is 1-sheeted, monodromy trivial, `s_p=\#\mathrm{Fix}=1`. Affine preimages: none, `a_p=0`. And `b_p=1`. Thus `0=1-1`. **Confirms** Cor. 3.2; this is exactly Sol-xpoll's sheet-on-the-boundary, now accounted for by `b_p`.

**(II) Ramified disk.** `q(z)=z^e`, `U=\Delta^*`. One point over `0`, multiplicity `e`. For `e\ge 2` the punctured covering is an `e`-cycle, `#\mathrm{Fix}=0`, `b_p=0` (the unique boundary point has `e>1`), `a_p=0`. Thus `0=0-0`. **Confirms.**

**(III) Product, affine image a disk.** `Y=\Delta_w\times\Delta_t`, `q(w,t)=(w,t^e)`, `D=\{t=0\}`, `U=\{t\neq 0\}`. Over generic `p\in D_0` one point, on `B_Y`. The covering `q^{-1}(D_0)\to D_0` is the `w`-disk, entirely in `B_Y`. Lemma 3.3's "boundary points over `D_0` are whole covering components" **HOLDS**. Affine part empty, `a=0`.

**(IV) Mixed analytic cut (attempted break).** Take the same product but set `U` to omit only `{t=0,\,|w|\ge 1/2\}`, so `B_Y` is a closed half-disk in `{t=0\}`. Then a single analytic arc over `D_0` would be partly in `U` and partly in `B_Y`, mixing components. This `B_Y` is not a closed pure-dimension-1 analytic (let alone algebraic) subset of `Y`. It violates Lemma 2.2, hence leaves the category in which Lemma 3.3 is stated. **Not a countermodel.**

### 6.2 Algebraic mixed-component hunt

The openness argument: if `y\in B_Y\cap q^{-1}(D_0)`, then `B_Y` is a curve through `y` (purity), `B_Y\subset q^{-1}(D)` (because `q(B_Y)=D`), and `q|_{B_Y}` is finite onto `D`, so a neighbourhood of `y` in `B_Y` covers a neighbourhood of `p` in `D_0`. Thus `B_Y\cap V_y` is 1-dimensional inside the irreducible arc `q^{-1}(D)\cap V_y` (`Y` normal `\Rightarrow` analytically irreducible germ over `\mathbb{C}`), hence equals it. Closed+open `\Rightarrow` whole components.

On `F=(x,y+xy^2)` this is visible: `q^{-1}(D)` has two components over `D\cong\mathbb{A}^1` (simply connected, covering trivial), one in `U` (the line `{x=0\}`) and one in `B_Y` (the `v=0` dicritical of §3.3), neither mixed. The affine line `{x=0\}` is already closed in `U`; its compactification meets the dicritical, but that meeting is at infinity of `Y`, not over `D_0`. **Confirms** Lemma 3.3.

On `F=(x,xy)` the `y`-axis *does* escape to the dicritical over the origin, a smooth point of `D`. Mixed/escaping over `D_0`. But `q` is not finite, `j` is not an open immersion (§1.1). **BROKEN only off the hypotheses.**

### 6.3 Identification `s_p=\#\{y:e_y=1\}`

Lemma 3.1 (for `p\in D_0`): orbits of `\langle g\rangle` biject with `q^{-1}(p)`, orbit size `e_y`. Then `e_y=1` iff a 1-cycle iff a fixed sheet of `H_p=\langle g\rangle`. Combined with Keller (`e_y=1` for every point of `U`) this is `a_p=s_p-b_p` tautologically. The disk models in 6.1 are the case `U` misses some `e=1` points.

At singular `p`, `H_p` is larger. A 1-orbit of the full local group still corresponds to an unramified point of `q^{-1}(p)`. Connectedness of `V_y\setminus q^{-1}(D)`: a ball in a normal surface minus a curve remains connected. No desk countermodel. **UNTESTABLE-AT-DESK** for a singular `p` on an actual Keller map (none known); **HOLDS** on the smooth-`D` models above.

### 6.4 Verdict

Cor. 3.2 and the component claim of Lemma 3.3 **HOLDS** on the disk family and on the quasi-finite algebraic model `F=(x,y+xy^2)`. The family confirms the `b_p` correction rather than breaking it. A mixed component over `D_0` was not produced inside the algebraic category with finite `q`.


## 7. Verdict table

| Target | Verdict | Witness / reason |
|---|---|---|
| (E) as a Keller theorem | **HOLDS** on automorphisms; **BROKEN** off Keller when `\chi_c(V)\neq 0` (`F=(x,y^2)`, `1\neq 2`); **HOLDS** off Keller when `\chi_c(A_F)=1` (`(x,xy)`, `(x,y+xy^2)`) | Factor `d` untested except on `A_F=\emptyset`. Singular `A_F` with `\chi_c\neq 1`: **UNTESTABLE-AT-DESK**. Proof uses a covering over `V` plus `\chi_c(\mathbb{A}^2)=1`, less than global Keller. |
| Covering `F^{-1}(D_0)\to D_0` of degree `a` | **HOLDS** on `F=(x,y+xy^2)` (`a=1`); **BROKEN** on `F=(x,xy)` (collapses to a point, `a=0`) | Failure traces to quasi-finite / finite `q`. Uses less than Keller (quasi-finite + (H2) suffice). |
| (M′) | **UNTESTABLE-AT-DESK** on Keller+(H2)+(H3) (no non-automorphism Keller map). **BROKEN** on `(x,xy)` (`0=-1`). **HOLDS** on `(x,y+xy^2)` with `\nu=s=0` (`-a=-1\Rightarrow a=1`) | Arithmetic assembly from (E)+covering is correct. Ceiling `1\le a\le d-2` is *not* tested on a Keller example. |
| Ceiling `1\le a\le d-2` | **BROKEN** off Keller: `a=0` on `(x,xy)`; `a=d-1` on `(x,y+xy^2)` | Keller on `V` (purity) is essential. Sol-xpoll's `a=d-1` is realised. |
| `a_p=s_p-b_p` (Cor. 3.2) | **HOLDS** on the disk family and on `F=(x,y+xy^2)` | Confirms `b_p`, does not break it. Mixed `U` cuts leave the algebraic category. |
| Lemma 3.3 component claim | **HOLDS** on disk products and on `F=(x,y+xy^2)` (two separate components over `\mathbb{A}^1`). **BROKEN** on `(x,xy)` off finite `q` | Boundary points over `D_0` are whole components when `q` is finite. |
| Lemma 4.2, `e=1+v(dx\wedge dy)` | **HOLDS** as local algebra with the Jac term. Keller form: **BROKEN** on `(x,xy)` (`1+v=0\neq e=1`); **HOLDS** on `(x,y+xy^2)` (`v=0=e-1`) | `v=-3,-2,-1,-4` as computed; `v=0` exists (three free blowups) and is dicritical for a quasi-finite map. OPEN at `d=4` is consistent. |
| Thm 4.4 three profiles | **HOLDS** | Re-enumeration complete; no `\delta_j=2` row is admissible. |
| `G=\langle\mathrm{transpositions}\rangle` transitive `=S_4` | **HOLDS** | `D_4` is not generated by the conjugacy class of one of its transpositions. |
| `G=\langle\mathrm{3-cycles}\rangle` transitive `=A_4` | **HOLDS** | One `A_4`-class of 3-cycles already generates `A_4`; cannot generate `S_4`. |
| `H_p` lists, §6 item 4 | **HOLDS** | `#\mathrm{Fix}=2\Rightarrow\mathbb{Z}/2`; `#\mathrm{Fix}=1\Rightarrow\{\mathbb{Z}/3,S_3\}` class-blind; `A_4` class `\Rightarrow\{\mathbb{Z}/3,A_4\}`. |
| (B-w) `\sum\delta_j e_j\le d-1`, some `e_j\ge 2` | Inequality **HOLDS** whenever `a\ge 1` (tautology `d=a+\sum\delta e`). “Some `e\ge 2`” **BROKEN** on `(x,y+xy^2)` | Keller/purity essential for the ramified-dicritical clause, not for the numerical inequality. |
| One-node exclusion (arithmetic) | **HOLDS** as arithmetic from (M′)+ceiling | `a-a_p=d-1>a` if `a\le d-2`. Not realised on a map; depends on the ceiling, which is untested on Keller examples. |
| Step 0, `A\subseteq B\subseteq\mathbb{C}[x,y]` | **HOLDS** without Keller (integrally closed) | ZMT / purity of `B_Y` need quasi-finite; **BROKEN** on `(x,xy)`. |

**Global.** No desk countermodel kills (M′), the covering lemma, Cor. 3.2, Lemma 4.2, Thm 4.4, or the group theory *inside* the stated Keller+(H2)+(H3) envelope, because that envelope has no explicit non-automorphism inhabitant. Several lemmas hold after dropping Keller, so they use less than claimed; the ceiling `a\le d-2` and “some `e_j\ge 2`” do not. The sheet-location bit `b=0` remains **OPEN** and is consistent with the existence of `v(dx\wedge dy)=0` dicriticals off Keller.

## 8. Sources

Desk computations only, plus the following primary sources. The 1993 Jelonek paper was not retrieved (IMPAN 502); its statement is recorded from the 2019 sequel which cites it as Theorem 4.1 / [8].

- Z. Jelonek, *The set of points at which a polynomial map is not proper*, Ann. Polon. Math. **58** (1993) 259–266. Content-level: `S_f` empty or a uniruled hypersurface. Not byte-hashed this lane.
- Z. Jelonek–M. Lasoń, arXiv:1906.06160v1 (12 Jun 2019), SHA-256 `8ebd09c3d04381e636b54172bd40fa6f9d6485b5f5522a483c819fc6f0928b83`. Re-states Jelonek's hypersurface theorem (Thm 1.2 / Thm 4.1 of [8]).
- V. Cossart–M. Matusinski, arXiv:1103.0707v2 (4 May 2011), SHA-256 `abdd75c2d4cd99b58521998c952d8105067befa77addf985287dfe3e4ba8b5f5`. Dicritical = exceptional with non-constant map to `\mathbb{P}^1`.
- Transitive subgroups of `S_4`: standard list `C_4,V_4,D_4,A_4,S_4` (e.g. the degree-4 line of the transitive-subgroup tables). `A_4` 3-cycle class split: conjugacy class `1131` of size 8 in `S_4` splits in `A_4` (centraliser `C_3` contains no odd element).

Charged inputs (verified):
- `6d8f6667fc7d52d1e46fc4ac55f2aa2049603f06c1764ae4ac51b078435d90eb` round1033-sheet-gate-opus5-20260831.md
- `2793104bcf746eab690ca75a2aaf2ef105b64e7be0c1826eb1fa9ed51ba992ef` ideation-20260831T1033Z-synthesis.md

<!-- BODY-END -->
