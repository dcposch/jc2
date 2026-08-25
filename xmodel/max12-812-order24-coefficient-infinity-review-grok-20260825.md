# Hostile review — `(8,12)` order-four/order-two coefficient infinity

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md` |
| Target SHA-256 | `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e` |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Charged reviews were opened only to obey the inspection clause; no producer `PASS` string and no charged `CONFIRMED` string is evidence |
| Method | source reading and hand derivation only; no CAS, solver, substantive Python, Lean, or other heavy local computation |
| Git HEAD | `24184c989634b40b00da1bbc3328bcc6ab92fa9b` (target uncommitted) |
| Required repairs | identity `(7.2)` and the sentence that the three order-two Faber-load directions have zero tails |
| Overall verdict | **REPAIR** |

Independently recomputed SHA-256 of the target is `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e`, matching the immutable pin.

## Verdict

**REPAIR.**

The source typing of the nontrivial Kummer coefficient-infinity fibre is correct, and the reduced exceptional support is the common quartic. Starting from `a_8=h^2`, `b_12=h^3`, `u^4=h` and monic-core class order `e=4` or `e=2`, the next-row character kills the depression mismatch, the source shear makes `R_0` regular at infinity, the universal high-row identity is `r_1'=\cdots=r_6'=0` and `8r_7'=j/u`, and the three target gauges at indices `8,0,4` leave

```text
e=4:  g=F_12(f),
e=2:  g=F_12(f)+k_10 F_10(f)+k_6 F_6(f)+k_2 F_2(f),
```

with complete tail targets `(0,0,0,mu_4,0,0,R_7)` and `(0,mu_2,0,mu_4,0,mu_6,R_7)` respectively. Both minimal Kummer extensions are unramified at `q=1/x=0`; `t=q^U u` is a unit on a selected sheet; `dR_7/dq=-(j/8)q^{U-2}t^{-1}` follows by the chain rule; its residue excludes every nontrivial `H=4` client; finite multiplicity four is the only finite logarithmic place of `dx/u`; and for `U>=2` every target load is regular at infinity. After the charged Rees scaling the exceptional rows on the selected sheet are exactly the ordinary unloaded seven tails, independently of a concrete `(8,12)` compiler. Mason–Stothers then gives reduced support `f=K^2`, `g=K^3` with `K=z^4+p z^2+c z+r`, projectively `P(2,3,4)`. The bounded-pole degrees are exactly `(8(U+1),12(U+1))` with gcd `4(U+1)`; under the classical Heitmann necessary bound `gcd>=16` this closes only `U<=2`, and the `U>=3` bounded lane remains live. The strict-Rees gate, the `P(2,3,4)` charts, and the denominator list `(6.4)` are correct, with Kummer order `e` independent of the Rees denominator `n`.

The smallest failing identity is `(7.2)`:

```text
F_10(K^2)=K^5,    F_6(K^2)=K^3,    F_2(K^2)=K.
```

These equalities are degree-false (`deg F_j=j`, while `deg K^{j/2}=2j`). The surrounding claim that the three order-two Faber-load directions have zero tails is likewise false on a generic common quartic: `w=f^{1/8}=K^{1/4}`, so `w^j=K^{j/4}` is a polynomial if and only if `K` is a square. The binomial first variation `(7.1)` in the coefficient directions survives, as does the qualitative warning that reduced support is not linear transversality, finite determinacy, or an exclusion of a strict arc. Repair `(7.2)` and that one sentence; do not otherwise reopen §§0–6.

## Smallest failing identity

```text
(7.2)   F_10(K^2)=K^5,  F_6(K^2)=K^3,  F_2(K^2)=K.
```

This is the `(9,12)` identity `F_6(K^3)=K^2` copied onto the wrong root. For `(8,12)` one has `w=K^{1/4}`, not `w=K^{1/2}`.

No load-bearing identity in §§0–6 failed. No hypothesis is missing from the reduced-support identification of the exceptional fibre.

## Strongest exact theorem that survives

Let `L` be a characteristic-zero field, after a harmless finite constant extension containing the needed roots of unity. Let `(P,Q)` be a Keller pair of actual `y`-degrees `(8,12)` with monic common core `h\in L[x]` of degree `H=4U>=4`, written `a_8=h^2`, `b_12=h^3`, `u^4=h`, and with the class of `h` in `L(x)^*/L(x)^{*4}` of order `e=4` or `e=2`. After the source shear that makes the depression `R_0` regular at infinity, the reviewed target gauges, and the character filter:

1. `f` is monic depressed of degree eight, `z=u(y+R_0)`, `R_0` is Kummer-invariant, and
   ```text
   e=4:  g=F_12(f),
   e=2:  g=F_12(f)+k_10 F_10(f)+k_6 F_6(f)+k_2 F_2(f),
   ```
   with `k_j\in L` and complete tail targets `(2.5)`. Always `8r_7'=j/u` with `j\neq 0`.
2. Every place of the minimal Kummer extension above `q=1/x=0` is unramified. On a selected sheet `t=q^U u` is a unit with `t(0)=1`, and `dR_7/dq=-(j/8)q^{U-2}t^{-1}`. For `U=1` the residue is nonzero, so both nontrivial `H=4` clients are empty. For `U>=2`, `R_7` and every other target load are regular at infinity.
3. If `d_i:=\max(0,-\mathrm{ord}_q(a_i))\le(U+1)(8-i)` for all `i`, the sheared pair has exact ordinary total degrees `(8(U+1),12(U+1))` and gcd `4(U+1)`, including the fully loaded order-two partner. Under the classical necessary bound `gcd(\deg P,\deg Q)\ge 16` this sector is counterexample-closed for `U\le 2` and not classically closed for `U\ge 3`.
4. On a selected unramified sheet the descended exceptional rows of the charged Rees scaling are the ordinary unloaded system `r_1(f,F_12(f))=\cdots=r_7(f,F_12(f))=0`. The other sheets are its weighted `mu_e` orbit. The reduced support is
   ```text
   K=z^4+p z^2+c z+r,    f=K^2,    g=K^3,
   ```
   a prime copy of `A^3`, projectively `P(2,3,4)`.
5. The strict chart `Lambda=q^{U+1}rho` together with sequential saturation by `q` and `rho`, then the irrelevant ideal `(B_0,\ldots,B_6)`, is fail-closed for strict formal/Puiseux (hence rational) coefficient-infinity branches of that fixed source. The converse is only algebraic boundary accessibility.

This is a reduced-support and source-typing theorem, plus a bounded-degree split and a residue exclusion of `H=4`. It is not a saturation verdict.

## Required repairs

Replace `(7.2)` and the sentence that the derivatives in the three order-two load directions have zero tails by the following, which is the identity the displayed formula was trying to copy.

At `f=K^2` one has `w=K^{1/4}`. The first variation of `g=F_12(f)+k_{10}F_{10}(f)+k_6 F_6(f)+k_2 F_2(f)` in a `k_j`-direction, with `f` held fixed, is the negative `w`-part of `w^j=K^{j/4}`. For `j\in\{2,6,10\}` this vanishes if and only if `K^{1/2}` is a polynomial, if and only if the depressed quartic `K` is a square. That is a proper closed subscheme of the common-quartic locus. On a generic point of `(0.2)` the three load derivatives are nonzero. The coefficient-direction vanishing from `(7.1)` is unchanged, and it is already enough to keep both clients from being linearly transverse.

No other numbered identity requires repair. A non-blocking citation note, not a mathematical repair: the bound `gcd\ge 16` is the classical Heitmann necessary condition (also stated by Guccione–Guccione–Valqui), not a theorem of the charged history stop, which only licenses prime gcd and gcd `2p`. The arithmetic `4(U+1)<16\Leftrightarrow U\le 2` is exact once Heitmann is granted, and prime/`2p` never apply to these bounded degrees.

## Strict scope firewall

This review licenses the source typing of the coefficient-infinity exceptional equations, their reduced common-quartic support, the exact bounded-pole degree formula, the `U\le 2` portion of that sector under Heitmann, the residue exclusion of nontrivial `H=4`, and the design of the strict saturation. It does **not**:

- prove that the seven-tail ideal is reduced, or determine embedded or nilpotent structure;
- exclude a strict arc for `U\ge 2`, or solve the bounded sector for `U\ge 3`;
- classify the global exactness condition on `dx/u` beyond the logarithmic places treated in Finding 2;
- discharge either original Taylor-boundary family, turn a Puiseux arc into a rational constant-field section, or emit an `(8,12)` compiler;
- close the order-one leaf, the whole `(8,12)` cell, maximum twelve, or JC2;
- promote reduced support to finite determinacy, lifting, Taylor realization, or cell closure.

The target's own firewall matches this boundary except for the false load-direction sentence in §7, which is the repair.

---

## Sources actually used

Read in full before any verdict. Used as definitions, residual routing, high-row identities, character tables, and the statement of Mason–Stothers, never as a conclusion or `PASS` string.

| Artifact | Independently recomputed SHA-256 |
|---|---|
| `xmodel/max12-812-order24-coefficient-infinity-source-audit-20260825.md` | `092dfb6d7de3e57ae153dcf3365fa2884ce289710b6c80c3193a2bc7f7d7853e` |
| `xmodel/as109-partial-y-history-stop-20260824.md` | `6994dd6bc1642122ba549be474d2465203faf554d93da5146ecb212dbaaf89fe` |
| `xmodel/max12-partial-y-kummer-preflight-20260824.md` | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` |
| `xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md` | `2951856cabe309fe07f564693a6b48a38cd7108616ffe41305d9583611da90fe` |
| `xmodel/max12-partial-y-shared-faber-probe-20260824.md` | `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036` |
| `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md` | `e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c` |
| `xmodel/max12-general-faber-exceptional-support-mason-20260825.md` | `7d5271e8caf6d6d071819e8b2a670ac79d2063882a90d4916060b3e4deb95919` |
| `xmodel/max12-general-faber-exceptional-support-mason-review-20260825.md` | `c95524a0a63ea4ab5cfa69eb26799279f330575c0b16f836a46180ebb826c292` |
| `xmodel/max12-general-faber-exceptional-support-mason-review-grok-20260825.md` | `29bd2184a1ec81a7c8f5de69c8b5485a8d8618749f4a357d83ad927e6403fa93` |

The target inventory hashes of the first seven of these (except the history stop, which the target does not list, and the grok Mason review, which the target cites only by inner target hash) match the recomputed values. No D1 compiler, no `(9,12)` degree-split, and no producer replay was consumed as evidence. Mason–Stothers for seven tails is rederived in Finding 6, not imported from a review verdict.

---

## Finding 1 — depression, characters, gauges, complete loads, `8r_7'=j/u`

**Severity: none.**

Let `m=8`, `n=12`, `(d,r,s)=(4,2,3)`, and after harmless nonzero target scalings `a_8=h^2=u^8`, `b_12=h^3=u^{12}`, `u^4=h`, with `h` monic. The Jacobian coefficient of `y^{18}` receives only the pairs `(8,11)` and `(7,12)`. Writing `A=a_7/u^7` and `B=b_{11}/u^{11}`, the four terms are

```text
T1 = 11 a_8' b_11 = 8·11 u^{18} u' B,
T2 = 12 a_7' b_12 = 12·7 u^{18} u' A + 12 u^{19} A',
T3 = -8 a_8 b_11' = -8·11 u^{18} u' B - 8 u^{19} B',
T4 = -7 a_7 b_12' = -12·7 u^{18} u' A.
```

The logarithmic pairs cancel, leaving `u^{19}(12A'-8B')=4u^{19}(3A-2B)'`. Characteristic zero and `u\neq 0` force `delta:=3A-2B` to be a `d/dx`-constant. Depression `z=uy+A/8` kills `[z^7]f` and puts `[z^{11}]g=B-(12/8)A=-delta/2`.

Let `e` be the order of monic `h` in `L(x)^*/L(x)^{*4}`. The minimal extension has degree `e`; a generator sends `u\mapsto zeta u` with `zeta` primitive of order `e`. Then `wt(A)\equiv wt(B)\equiv 1\pmod{e}`, so `wt(delta)\equiv 1`. The constant field of `L(x)(u)` equals `L` for monic `h` (valuations persist under constant extension, so a constant-field growth would raise the class order). A weight-one constant vanishes for `e>1`. This includes the genuine quadratic leaf `e=2`, where `h=v^2` with `v` monic and not a square: `X^4-h=(X^2-v)(X^2+v)` is reducible, the extension is quadratic, and only parity weights exist. The monic-core qualification is load-bearing (a non-monic example produces a nonzero weight-one `delta` while the `y^{18}` row still vanishes) and is supplied by the target's own scalings.

Thus `R_0:=A/8` is the depression, and `sigma(R_0)=R_0` because `sigma(A/u)=(zeta A)/(zeta u)=A/u`. Write `z=u(y+R_0)`. Then

```text
[y^7]P = 8 u^8 R_0 = 8 h^2 R_0.
```

Taylor polynomiality puts this in `L[x]`, so `R_0\in L(x)` with finite poles only over zeros of `h`. Subtracting the polynomial part `q(x)` of `R_0` at infinity by the source automorphism `(x,y)\mapsto(x,y-q(x))` replaces `R_0` by a function regular at infinity, does not change `f` as a polynomial in `z`, does not change any `a_i`, does not change the Kummer class of `h`, and preserves both the constant Jacobian and automorphy versus non-automorphy. Henceforth `R_0` is regular at infinity.

The generator sends `z\mapsto zeta z`. Invariance of `P` as a function of `y` forces `sigma(a_i)=zeta^{-i}a_i`. The monic eighth root `w=f^{1/8}=z+O(z^{-1})` therefore transforms as `w\mapsto zeta w`. Expanding `g=\sum_{j=0}^{12}h_j F_j` with `F_j=[w^j]_+` and `H_F(T)=\sum h_j T^j`, the identity `H_F(w)-g(z(w))=\sum_{\ell\ge 1}r_\ell w^{-\ell}` is invariant, so `r_\ell` has character `zeta^\ell`. Independently, `h_j` has character `zeta^{-j}` and can be a nonzero constant only for `e\mid j`.

Over a characteristic-zero differential field, if `deg_z(f_x g_z-f_z g_x)\le m-2`, descending triangularity of `[f_z w^j]_+` (leading term `m z^{m-1+j}`) forces every `h_j'` to vanish. The remaining identity is `D=\sum_{\ell=1}^{m-1} r_\ell' A_\ell` with `A_\ell=[f_z w^{-\ell}]_+`, leading term `m z^{m-1-\ell}` for `1\le\ell\le m-1`, and `A_{m-1}=m`. The matrix on `(r_1',\ldots,r_7')` is triangular of determinant `8^7`. The chain rule `J_{(x,y)}(P,Q)=u D=j` gives the positive terminal system

```text
r_1'=\cdots=r_6'=0,     8 r_7'=j/u.
```

(The opposite sign on the tail in `D` is incompatible with `H(w)-g=\sum r_\ell w^{-\ell}`.) Differential constants of character not `1` vanish. Hence the complete allowed tail pattern is exactly `(2.5)`:

```text
e=4: (r_1,\ldots,r_7)=(0,0,0,mu_4,0,0,R_7),
e=2: (r_1,\ldots,r_7)=(0,mu_2,0,mu_4,0,mu_6,R_7),
```

with `R_7'=j/(8u)` and character `7\bmod e`. No mod-four filter may be imposed on the order-two leaf: `r_2,r_6` are legal constants there.

Because `n<2m`, the translation `P\mapsto P+q` acts finitely by `h_{k,\mathrm{new}}=h_k-((k+m)/m)h_{k+m}q` on `0\le k\le n-m` and slices `h_{n-m}=h_4`. The automorphisms `Q\mapsto Q-h_8 P` and `Q\mapsto Q-h_0` slice `h_8` and `h_0`. The three indices `8,0,4` are distinct and `0\bmod e` for every `e\mid 4`. Remaining constant indices:

```text
e=4: allowed {0,4,8}, all gauged, H_F(w)=w^{12}, g=F_12(f);
e=2: allowed {0,2,4,6,8,10}, gauges kill {0,4,8},
     H_F(w)=w^{12}+k_10 w^{10}+k_6 w^6+k_2 w^2.
```

This is the complete target-load list. There is no residual `h_{11}`: that slot is the already-killed mismatch. The first seven tails have weights `12+\ell=13,\ldots,19` by the homogeneity in Finding 5. All of this is source typing, not a fibre classification.

Attacks that failed: a surviving logarithmic term in the `y^{18}` row (the four coefficients cancel in pairs); a nonzero forced `delta` on a nontrivial monic-core leaf; treating the order-two leaf as a degenerate quartic; absorbing `mu_4` into a remaining gauge (the three gauges are already spent on `h_0,h_4,h_8`); a leftover odd Faber constant; `8r_7'=-j/u` (the plus sign is forced by the series convention, and the `H=4` residue obstruction of Finding 2 would in any case survive a global sign flip).

---

## Finding 2 — ramification at infinity, `(3.2)`, residue, multiplicity four, regularity for `U>=2`

**Severity: none.**

Put `q=1/x` and `H=4U` with `U\ge 1` an integer (the residual condition `4\mid H` for nontrivial class order; `U=0` is the trivial leaf `e=1`, out of scope). For a Kummer extension of class order `e`, the ramification index at a place `v` is `e/\gcd(e,v(\mathrm{radicand}))`.

- Order four: radicand `h`, `v_\infty(h)=-4U`, index `4/\gcd(4,4U)=1`.
- Order two: radicand `v` with `h=v^2` and `v` monic of degree `2U`, `v_\infty(v)=-2U`, index `2/\gcd(2,2U)=1`.

Every place above `q=0` is unramified, so `q` is a uniformizer on each such place. No fractional valuation is hidden.

On a selected sheet set `t=q^U u`. For `e=4`,

```text
t^4 = q^{4U} h(q^{-1}).
```

Monicity of `h` gives `q^{4U}h(q^{-1})=1+O(q)`, a unit congruent to one. For `e=2`, `t^2=q^{2U}v(q^{-1})` is likewise a unit congruent to one. The condition `t(0)=1` selects a sheet after the licensed roots of unity; the others are `t\mapsto zeta t`. Thus `t` is a unit on every selected sheet.

From `dR_7/dx=j/(8u)` and `dx/dq=-q^{-2}`,

```text
dR_7/dq = -q^{-2}·j/(8u).
```

Substitute `u=t q^{-U}`:

```text
dR_7/dq = -(j/8) q^{U-2} t^{-1}.
```

This is `(3.2)`, including the sign.

For `U=1` the right-hand side is `-(j/8)q^{-1}t^{-1}`. On the selected sheet the residue is `-(j/8)t(0)^{-1}=-j/8\neq 0`; on any other sheet it is `-(j/8)zeta^{-1}\neq 0`. A meromorphic differential of a rational function on a smooth curve has residue zero at every place: if `R_7=\sum a_k \pi^k` locally, then `dR_7=\sum k a_k \pi^{k-1}d\pi`, and the coefficient of `\pi^{-1}d\pi` is zero. But `R_7` lies in the Kummer function field (the Faber tail of a pair of polynomials in `z` with coefficients in `L(x)(u)`). Contradiction. Both nontrivial `H=4` clients are empty, before any Rees calculation.

Finite multiplicity four. Let `v_a(h)=4`. Then `4/\gcd(4,4)=1`, so the place is unramified and `\pi=x-a` remains a uniformizer. Locally `h=\pi^4 c` with `c(a)\neq 0`, and `t:=u/\pi` is a unit. Then `dx/u=t^{-1}d\pi/\pi` has residue `t(0)^{-1}\neq 0`, and `dR_7=(j/8)dx/u` has nonzero residue. The same holds for `e=2`: multiplicity four of `h` is multiplicity two of `v`, the quadratic Kummer extension is unramified, and `u` still satisfies `u^4=h`. This is sharp. If `v(h)=4k` with `k\neq 1` and the place unramified, then `dx/u=t^{-1}\pi^{-k}d\pi` has residue zero. At ramified places (which must exist for `e=4`) a local calculation in the uniformizer `tau` gives a holomorphic form: for `v(h)=1,2,3` one obtains `dx/u` regular. Vanishing of residues is only necessary; the full condition is exactness of `dx/u` on the Kummer curve, as the target states.

Regular loads for `U\ge 2`. The right-hand side of `(3.2)` is holomorphic (`U-2\ge 0`, `t` a unit). A pole of `R_7` of order `k\ge 1` would produce a pole of `dR_7` of order `k+1\ge 2`. Hence `R_7` is regular up to a constant; the constant has character `7\bmod e\neq 0` and vanishes. The remaining targets are scalars (`mu_{2k}` and the `k_j`), hence regular. This is regularity at the place `q=0`, not holomorphy of `R_7` on the whole curve.

Attacks that failed: a hidden ramification index `>1` at infinity (the valuation of the radicand is divisible by `e`); `t(0)` a non-unit (the displayed right-hand side is `1+O(q)`); a residue obstruction at every finite zero of `h` (only multiplicity four); treating `U=2` as logarithmic (`q^{0}t^{-1}` is holomorphic); promoting residue vanishing to a global classification of exact `dx/u`.

---

## Finding 3 — bounded-pole degrees, gcd, GGV/Heitmann split

**Severity: none** for the degree identities. Citation precision recorded, not a break.

The unit `t` does not change pole orders of the `a_i`, because `(4.1)` multiplies by a unit. Let `d_i=\max(0,-\mathrm{ord}_q(a_i))` and assume `(3.4)`: `d_i\le(U+1)(8-i)` for `0\le i\le 6`. Since `R_0` is regular, a summand indexed by `i\ge\ell` in `[y^\ell]P` has pole order at most

```text
d_i + U i \le (U+1)(8-i)+U i = 8(U+1)-i \le 8(U+1)-\ell.
```

Taylor membership puts each coefficient in `L[x]`, so `\deg P\le 8(U+1)`. The top term `[y^8]P=h^2` is monic of `x`-degree `2H=8U`, hence of ordinary total degree `8(U+1)`, and cannot cancel. Exactness of `\deg P=8(U+1)` holds even if every `d_i=0`.

For `Q`, assign `wt(z)=1`, `wt(a_i)=8-i`, `wt(k_j)=12-j`. Then `F_j` is homogeneous of weight `j`, and every monomial of the fully loaded `(2.6)` has weight twelve (including the three order-two summands, and with at most one `k_j` per monomial because `g` is linear in the `k`'s). A monomial contributing to the `z^s` coefficient therefore satisfies `\sum e_i(8-i)+\sum e_j(12-j)+s=12`. After `z=u(y+R_0)`, with `k_j` finite scalars, its pole order is at most

```text
(U+1)\sum e_i(8-i) + U s
 = 12(U+1)-s-(U+1)\sum e_j(12-j)
 \le 12(U+1)-s.
```

Thus `\deg Q\le 12(U+1)`. The top term `[y^{12}]Q=h^3` has `x`-degree `12U` and total degree `12(U+1)`. This is `(0.3)`:

```text
(\deg P,\deg Q)=(8(U+1),12(U+1)),    gcd=4(U+1).
```

The estimate uses the full order-two-loaded `Q`; deleting the `k_j` only removes a nonpositive term and recovers the order-four case. No `(9,12)` identity was used: the weight of `a_i` is `8-i`, the pole of `u` is `U`, and the top degrees are `2H` and `3H`.

Heitmann's necessary condition: a characteristic-zero Jacobian counterexample has `gcd(\deg P,\deg Q)\ge 16`. Then `4(U+1)<16\Leftrightarrow U\le 2`. Combined with Finding 2, the bounded sector is empty for `U=1` already by residue, and counterexample-closed for `U=2`. For `U\ge 3` one has `gcd\ge 16`, so this obstruction does not fire; both the bounded lane of exact degrees `(8(U+1),12(U+1))` and the strict lane `alpha>U+1` remain live. One must not copy the D1 inference that every client is strict: that inference used a single source with bounded gcd `9<16`. For `U=2` every counterexample client must satisfy `alpha:=\max_i d_i/(8-i)>3`.

The charged history stop licenses only: prime total gcd (Nagata's repair of Appelgate–Onishi) and total gcd `2p` (GGV 2017). For `U\ge 1`, `4(U+1)` is never prime and never `2p` (`4(U+1)=2p` forces `p=2(U+1)` even). Those two arrows therefore close none of the bounded `(8,12)` degrees. The `U\le 2` closure uses Heitmann, which is a classical theorem and is stated by GGV, but is not a numbered identity of any charged source. The arithmetic of `(3.7)` is nevertheless exact once that bound is granted, and the target's two-lane split for `U\ge 3` is the correct consequence.

Attacks that failed: a cancellation of `h^2 y^8` (unique top `y`-degree, monic in `x`); the `k_j` inflating poles (they are scalars); the unit `t` changing `d_i`; treating `(3.4)` as raising the top degrees (it only controls lower rows; the top degrees are present even at `d_i=0`); closing `U\ge 3` by prime or `2p`; copying D1's “all clients are strict”.

---

## Finding 4 — character descent, étale-sheet equivalence, deck action, compiler

**Severity: none.**

Let `[a]_e` be the least nonnegative residue of `a` modulo `e`. The deck generator sends `t\mapsto zeta t` and `z\mapsto zeta z`. Set `a_i=t^{[-i]_e}A_i(q)`. Then `t^{[-i]_e}` has character `zeta^{-i}`, matching `a_i`, so every `A_i` is invariant. For `e=2` this is the even/odd splitting (`[-i]_2=0` or `1`). Define

```text
D_\ell(q,A,k)=t^{[-ell]_e} r_\ell(t^{[-i]_e}A_i,\,k).
```

The prefactor has character `zeta^{-ell}` and `r_\ell` has character `zeta^{ell}`, so `D_\ell` is invariant. Powers `t^e` are the displayed base unit (`q^{4U}h(q^{-1})` or `q^{2U}v(q^{-1})`), a polynomial congruent to `1` at `q=0`. The raw tails `r_\ell` are polynomials in the `a_i` and `k_j` by the finite binomial construction of `F_j` and the triangular reversion of `z(w)`. The exponents `[-i]_e` and `[-ell]_e` are nonnegative, so after reducing `t^e` one obtains a polynomial in the `A_i,k_j` over `L[q]`. Set `delta_\ell=t^{[-ell]_e}gamma_\ell`. Nonzero constant targets occur only at multiples of `e`, where `[-ell]_e=0` and the twist is one. For the terminal row, `[-7]_4=1` and `[-7]_2=1`; `R_7` has character `zeta^7=zeta^{-1}`, so `delta_7` is invariant, and it is regular for `U\ge 2` by Finding 2.

Equivalently `C_i=t^{[-i]_e}A_i` (so `C_i=a_i`). Then `D_\ell-delta_\ell=t^{[-ell]_e}(r_\ell(C,k)-gamma_\ell)`. The prefactor is a unit in the local ring at `q=0` (`t(0)\in mu_e`). Vanishing of the descended rows is therefore equivalent to vanishing of the ordinary rows, by an invertible étale/unit change of coordinates, with no reference to a D1 compiler. At `q=0` on the selected sheet `t(0)=1` one has `C_i=A_i`. On another sheet the equations are carried to the first by the weighted action on coefficients.

Induced action on the common-quartic parameters. Write `K=z^4+p z^2+c z+r`. Weights `(2,3,4)` under `z\mapsto zeta z` give

```text
e=4: (p,c,r)\mapsto(zeta^2 p,\,zeta^3 c,\,r),
e=2: (p,c,r)\mapsto(p,\,-c,\,r),
```

which is `(4.5)`. Directly: `K_sigma(Z)=Z^4+(zeta^2 p)Z^2+(zeta^3 c)Z+r` satisfies `K_sigma(zeta z)=zeta^4 K(z)=K(z)` since `zeta^4=1` in both live orders, so `f=K^2` and `g=K^3` remain invariant as functions of `y`.

Theoretical source typing is sufficient for the reduced-support identification of the exceptional fibre: the polynomials `D_\ell` exist, the unit equivalence identifies their vanishing with ordinary vanishing, and Finding 5 specialises them to the unloaded system `(0.1)`. It is not sufficient for a computational saturation verdict. The target does not claim one, and correctly records that no `(8,12)` full-fibre/Rees compiler exists in the repository.

Attacks that failed: exponent `[+ell]_e` instead of `[-ell]_e` (character `zeta^{2ell}`, not invariant); `r` picking up a factor `zeta^4\neq 1` (both live `e` divide `4`); needing explicit tail monomials to know that `D_\ell` is a polynomial (nonnegative `t`-exponents plus `t^e` a polynomial unit); a missing sheet in the `mu_e` orbit.

---

## Finding 5 — tail weights, Rees equations, `Lambda=q^{U+1}rho`, saturations, unit-ideal strength

**Severity: none.**

Scale `z\mapsto lambda z`, `a_i\mapsto lambda^{8-i}a_i`, `k_j\mapsto lambda^{12-j}k_j`. Then `f_{\mathrm{new}}(z)=lambda^8 f_{\mathrm{old}}(z/lambda)`, so `w_{\mathrm{new}}=lambda w_{\mathrm{old}}`, and `H_{\mathrm{new}}(lambda w)=lambda^{12}H_{\mathrm{old}}(w)`. The tail identity becomes `r_\ell^{\mathrm{new}}lambda^{-ell}=lambda^{12}r_\ell^{\mathrm{old}}`, i.e.

```text
r_\ell(lambda^{8-i}a_i,\,lambda^2 k_10,\,lambda^6 k_6,\,lambda^{10} k_2)
 =lambda^{12+ell} r_\ell(a,k).
```

The tail weights are `13,\ldots,19`; the lower-load weights are `2,6,10`. All displayed exponents are strictly positive. The order-four client omits the `k` arguments.

Normalize coefficient infinity by `B_i=Lambda^{8-i}A_i`. The descended Rees equations are

```text
Phi_\ell
 = D_\ell(q,B,Lambda^2 k_10,Lambda^6 k_6,Lambda^{10} k_2)
   - Lambda^{12+ell} delta_\ell(q)
 =0,    1\le\ell\le 7.
```

On a selected sheet `t=1+O(q)`. Setting `q=Lambda=0` kills every `k` argument and every target (regular `delta_\ell` times a positive power of `Lambda`), and yields `r_\ell(B,0)=0`. This is `(0.1)`, not an analogy with `(9,12)`. The constant targets `mu_{2k}` are scaled by `Lambda^{12+2k}` and die; they are not retained as `r_{2k}=mu_{2k}` on the exceptional divisor. That last point is load-bearing for Mason: a surviving `r_4=mu_4` would destroy the seven-tail vanishing.

For a rational pole of slope `alpha=m/n>U+1` in lowest terms, the chart `q=epsilon^n`, `Lambda=epsilon^m` has `rho:=Lambda/q^{U+1}=epsilon^{m-(U+1)n}\to 0`. Substituting `Lambda=q^{U+1}rho` into `(5.3)` produces exactly `(5.5)`, including

```text
q^{2(U+1)}rho^2 k_10,\;
q^{6(U+1)}rho^6 k_6,\;
q^{10(U+1)}rho^{10} k_2,\;
q^{(U+1)(12+ell)}rho^{12+ell}delta_\ell(q).
```

Put `I=(Psi_1,\ldots,Psi_7)`, `K_{\mathrm{strict}}=I:(q rho)^\infty`, and `H_{\mathrm{strict}}=(K_{\mathrm{strict}}+(q,rho)):(B_0,\ldots,B_6)^\infty`. In a polynomial ring, saturation by a product is independent of order: `I:(qr)^\infty=(I:q^\infty):rho^\infty`. Both must be saturated before the boundary `(q,rho)=0` is taken. A `rho`-unit branch has slope exactly `U+1` and is the bounded wall, not the strict sector. A `q`-unit branch is finite coefficient. Saturating by `(B_0,\ldots,B_6)` removes only the irrelevant origin, which is not a projective leading point.

The implication `H_{\mathrm{strict}}=(1)\Rightarrow` no strict formal/Puiseux (hence no rational) coefficient-infinity branch for that fixed source is fail-closed. The converse `H_{\mathrm{strict}}\neq(1)` is only algebraic boundary accessibility: it does not produce a rational constant-field section and does not satisfy the Taylor boundaries. A slope-`U+1` negative control belongs in any later compiler, as the target says.

Attacks that failed: weight `12-\ell` instead of `12+\ell` (the `w^{-\ell}` Jacobian of the scaling); retaining `r_4=mu_4` on the exceptional fibre; saturating only by `q` (admits the bounded wall); saturating by `pcr` in place of the `B_i` (Finding 6); reading a nonempty `H_{\mathrm{strict}}` as a rational trajectory.

---

## Finding 6 — common-quartic graph, `P(2,3,4)`, denominators, `e` versus `n`

**Severity: none.**

On the exceptional fibre the equations are the ordinary unloaded tails `r_1=\cdots=r_7=0` for `g=F_{12}(f)`, independently of `e`. Let `d=\gcd(8,12)=4`, `a=2`, `b=3`, `N=24`. Vanishing of the first seven tails is `T=O(w^{-8})`, so

```text
W(z(w)):=(g^2-f^3)(z(w))
 =(w^{12}-T)^2-w^{24}
 = -2 w^{12}T + T^2
 = O(w^{4}).
```

Substitution `z(w)=w+O(w^{-1})` preserves degree and leading coefficient of a nonzero polynomial, hence `deg_z W\le D:=N-m-n=4`. (Six tails would give bound `5` and Mason equality; all seven are load-bearing.) If `W\neq 0` and `D_0=\gcd(g^2,f^3)` has degree `e\le 4<24`, the pairwise-coprime triple `A=g^2/D_0`, `B=-f^3/D_0`, `C=-W/D_0` has `deg A=deg B=24-e` and `deg C\le 4-e`. Mason–Stothers in characteristic zero yields

```text
24-e \le deg rad(ABC)-1 \le (8+12)+(4-e)-1 = 23-e,
```

a contradiction, including the constant-`W` edge `e=0`. Thus `g^2=f^3`. Unique factorization in `L[z]` with `gcd(2,3)=1` and monicity produce a unique monic `K` of degree `4` with `f=K^2`, `g=K^3`; the missing `z^7` coefficient is `2c_3`, so `K` is depressed. Conversely `K(z(w))=w^4` by uniqueness of the monic fourth root, so `F_{12}(K^2)=K^3` and every tail vanishes. The power map on depressed coefficients is triangular with invertible diagonal `2`, hence an isomorphism onto a closed prime image `A^3`. Geometric equality of zero sets plus contraction gives that the radical of `(r_1,\ldots,r_7)` is the ideal of this image. Weights of the depressed coefficients of `K` are `2,3,4`, so the weighted `Proj` is `P(2,3,4)`.

Expanding the square:

```text
(z^4+p z^2+c z+r)^2
 = z^8 + 2p z^6 + 2c z^5 + (p^2+2r)z^4 + 2pc z^3
   + (c^2+2pr)z^2 + 2cr z + r^2.
```

This is `(6.1)`. The triangular normals `(6.2)` invert it. The reduced boundary is `x_3=x_2=x_1=x_0=0`; the irrelevant ideal is `(p,c,r)`. The normals must remain in any deformation calculation: setting them to zero prematurely would assert reducedness of the tail ideal, which is not proved.

Projective coverage after the interior saturation of Finding 5 uses the three charts `p\neq 0`, `c\neq 0`, `r\neq 0`. These cover `P(2,3,4)`: every point has at least one coordinate nonzero. Saturating by `pcr` alone loses every coordinate boundary (the axes `K=z^4+p z^2`, `K=z^4+c z`, `K=z^4+r`, and the mixed walls). No fourth chart is missing. The discriminant-zero locus (multiple roots of `K`) is included, correctly: Mason does not squarefree `K`.

Denominator classification. A rational strict slope `m/n` in lowest terms, via `q=epsilon^n` and `Lambda=epsilon^m`, scales `(p,c,r)` by `(omega^{2m},omega^{3m},omega^{4m})` under `epsilon\mapsto omega_n epsilon`. For the affine parameters to have limits in `L` one needs `n\mid 2` if `p\neq 0`, `n\mid 3` if `c\neq 0`, `n\mid 4` if `r\neq 0`. Hence `(6.4)`:

```text
p c \neq 0 or c r \neq 0:                 n=1;
c=0, p\neq 0 (r arbitrary):              n\mid 2;
p=r=0, c\neq 0:                          n\mid 3;
p=c=0, r\neq 0:                          n\mid 4.
```

Every nonzero `(p,c,r)` appears exactly once. In lowest terms, `n=2` forces `m` odd, `n=3` forces `gcd(m,3)=1`, and `n=4` forces `m` odd. The numerator `m` is unbounded. Extra vanishing of some `B_i` (e.g. `B_4=p^2+2r=0` with `p,r\neq 0`, or `B_0=r^2` of weight `8`) only adds `B`-constraints or is redundant with `n\mid 4`; it does not create a new stratum of `(p,c,r)` and does not enlarge the possible `n` beyond four.

Kummer order `e` and Rees denominator `n` are independent. The unit `t(q)` is unramified at `q=0` and becomes `t(epsilon^n)`, introducing no new fractional valuation. On the strata of `(6.4)` the two actions are compatible: the `n=2` wall has `c=0`, so the `e=2` deck `(p,-c,r)` is the identity there; the `n=4` wall has `p=c=0`, so the `e=4` deck is the identity there. The composite local degree may exceed both `e` and `n`; the Kummer sheets remain related by `(4.5)`.

Attacks that failed: six tails sufficing for Mason (equality `24-e\le 24-e`); a missing axis of `P(2,3,4)`; `n\mid 8` from `B_0` enlarging the `p=c=0` wall (gcd with weight `4` is still `4`); a forced identification of `e` with `n`; promoting reduced support to reducedness of `(r_1,\ldots,r_7)`.

---

## Finding 7 — first differential of the tail map; the failing identity `(7.2)`

**Severity: repair.** The coefficient-direction vanishing and the qualitative non-promotion survive. The load-direction identity does not.

Write `f=K^2+E` with `E` of degree at most `6`, at zero scaled Faber loads. The binomial expansion of the monic branch of `f^{3/2}` is

```text
(K^2+E)^{3/2}
 = K^3 + (3/2)K E + (3/8)K^{-1}E^2 - (1/16)K^{-3}E^3+\cdots,
```

which is `(7.1)`: the coefficient of `x^2` in `(1+x)^{3/2}` is `(3/2)(1/2)/2=3/8`, and the coefficient of `x^3` is `(3/2)(1/2)(-1/2)/6=-1/16`. The constant term `K^3` and the linear term `(3/2)KE` are polynomials in `z` (`deg(KE)\le 10`). They are absorbed into `F_{12}(f)` at first order, so they do not contribute to the negative `w`-series. The first differential of the seven-tail map therefore vanishes in every coefficient direction along the whole common-quartic locus. (The quadratic term already involves `K^{-1}` and may contribute to tails; this is vanishing of `d\tau`, not finite determinacy. Along the three tangent directions to `(p,c,r)` the tails vanish identically, which is the weaker statement.)

The load directions are a different variation: `f` is held fixed, so `z(w)` is held fixed, and `g` changes by `F_j(f)` while `H` changes by `k_j w^j`. The first variation of the tail is the negative `w`-part of `w^j`. At `f=K^2` one has `w=K^{1/4}`, not `w=K^{1/2}`, and

```text
w^2=K^{1/2},    w^6=K^{3/2},    w^{10}=K^{5/2}.
```

Displayed `(7.2)` asserts `F_{10}(K^2)=K^5`, `F_6(K^2)=K^3`, `F_2(K^2)=K`. These are the equalities `F_j(K^2)=K^{j/2}`. They are false for two independent reasons:

1. Degree: `F_j` is monic of degree `j`, while `K^{j/2}` has degree `2j`. In particular `deg K^5=20\neq 10`.
2. Polynomiality: `K^{j/4}` is a polynomial if and only if `4\mid j`, except on the locus where `K` itself is a square. None of `2,6,10` is divisible by `4`.

The three negative parts vanish simultaneously if and only if `K^{1/2}` is a polynomial, if and only if the depressed quartic `K` is a square of a depressed quadratic. That is a proper closed subscheme of `(0.2)` (the more degenerate fourth-power locus). On a generic common quartic the three order-two load derivatives are nonzero.

The copied `(9,12)` fact `F_6(K^3)=K^2` is true because there `w=K^{1/3}` and `3\mid 6`. It does not transfer.

What survives of §7. The `e=4` client has only the seven coefficient directions, along which `d\tau=0` by `(7.1)`; it is not linearly transverse. The `e=2` client is not linearly transverse either, because the same seven directions still lie in the kernel, even though the three `k_j`-directions generally do not. A fixed jet cannot replace the exact saturation without a separate finite-determinacy theorem. Scheme thickness, normal Kuranishi equations, and the charged Taylor boundaries remain the actual next obstruction. Reduced support is not reducedness, not an exclusion of a strict arc, not Taylor realization, not cell closure, and not JC2.

The required textual repair is local to `(7.2)` and the one sentence that names it. It does not reopen Findings 1–6.

---

## Attacks that did not land on §§0–6

- A surviving depression mismatch on a nontrivial monic-core leaf.
- A mod-four filter on the order-two Faber constants or on `r_2,r_6`.
- Ramification of the Kummer cover at `x=\infty`.
- A zero residue of `(3.2)` at `U=1`.
- A residue obstruction at every finite zero of `h`, or at ramified places.
- Inexact bounded degrees, or the `k_j` spoiling the `Q` bound.
- Closure of the `U\ge 3` bounded lane by prime gcd or gcd `2p`.
- Character exponents of the opposite sign in `(4.1)`–`(4.3)`.
- A missing chart of `P(2,3,4)`, or `n` forced equal to `e`.
- A surviving `mu_4` or `k_j` on the exceptional divisor.
- Sufficiency of six tails for Mason.
- Promotion of this review, or of the target after the `(7.2)` repair, to a saturation verdict, a Taylor realization, or JC2.

---

## Model identity and evidence boundary

Reviewer: Grok 4.6, released by xAI. Independent hostile rederivation of the charged source audit. Every charged review was opened only because the launch listed it; its verdict string was not used. No prior stdout, no CAS, no solver, and no Python reconstruction was used as evidence. The load-bearing chain is the monic-core Kummer split, the universal high-row identity with positive terminal row `8r_7'=j/u`, the three character-compatible target gauges, the unramified unit `t=q^U u`, the chain rule for `dR_7/dq`, exactness of residues, the Faber grading of the fully loaded partner, Heitmann's necessary gcd bound as a classical input, the unit descent `(4.2)`, Rees homogeneity of weights `12+\ell` and `12-j`, Mason–Stothers on seven tails, and the binomial first variation `(7.1)`.

REPAIR
