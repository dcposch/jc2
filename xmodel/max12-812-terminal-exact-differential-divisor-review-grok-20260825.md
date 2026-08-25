# Hostile review — `(8,12)` terminal exact-differential and divisor-profile theorem

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-terminal-exact-differential-divisor-theorem-20260825.md` |
| Target SHA-256 | `1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer (OpenAI Codex, GPT-5 family). The charged Faber review is same-model and is not used as a PASS/CONFIRMED certificate; the terminal row and tail sign are re-derived below from the identities in that source |
| Method | source reading and hand derivation only; SHA-256 of the three named files; no CAS, solver, substantive Python, Lean, or other heavy local computation |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `24184c989634b40b00da1bbc3328bcc6ab92fa9b` (named producer artifact uncommitted) |
| Date | 2026-08-25 |

Independently recomputed SHA-256 of the target is `1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b`, matching the launch pin. The two charged sources match the hashes printed in the target. Producer verdict language, the target's own status line, and any PASS string were not used as evidence. No file other than this review was written.

---

## Verdict

The charged theorem is correct as a terminal necessary condition on a nontrivial Kummer client of the reviewed partial-`y` `(8,12)` high-row reduction, and as a complete first-degree classification of the order-two divisor profile. Independently: the Faber tail definition, the Jacobian factor `u`, and `A_{m-1}=m` give `8 r_7'=j/u`; the Kummer generator forces `r_7` into the inverse-character line `u^3 L(x)` or `u L(x)`; the two displayed rational ODEs are equivalent to that row, with unique rational solutions on each nontrivial class; every place above infinity is unramified and `dx/u=-q^{U-2}t^{-1}dq`, so `U=1` is killed sheetwise by a nonzero residue and `U>=2` is regular at infinity; finite orders are exactly `(4-k)/gcd(4,k)-1` and `(2-k)/gcd(2,k)-1`; multiplicity four in `h` is a simple pole of nonzero residue on every branch; exact holomorphic differentials on a complete smooth curve vanish, so some finite multiplicity is at least five in order four and at least six in order two; at `U=2`, `e=2` the only surviving partition is `[3,1]`/`[6,2]`, and the displayed primitive `T` makes the terminal differential exact with the exact constant `j/(4(b-a))`. Passing that identity does not solve the other six tails, produce Taylor polynomiality, close either Kummer client, or touch JC2.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-terminal-exact-differential-divisor-theorem-20260825.md` | `1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b` | target (matches required pin) |
| `xmodel/max12-partial-y-kummer-preflight-20260824.md` | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` | residual `4\|H`, Kummer orders `4,2,1`, depression `z=uy+A/8`, `delta=0` on `e>1`, Galois `z↦ζ z`, charged Taylor jets |
| `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md` | `e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c` | tail definition, fixed-`w` identity, `A_{m-1}=m`, chain rule `J_{(x,y)}=uD` (same-model; unused as a verdict) |

Both hashes match the target's parent table. The preflight is consumed only for residual degree, the live Kummer orders, depression, the Galois action on `z`, and the fact that both original `y=0` Taylor families remain charged. The Faber source is consumed only for the tail series, the triangular terminal system, and the Jacobian factor `u`. Neither source's scope-firewall sentence, nor the preflight replay, is an input.

---

## Strongest exact theorem that survives

Let `L` be a characteristic-zero field enlarged to contain the roots of unity needed below. Let `h∈L[x]` be monic of degree `H=4U` with `U≥1`, let `u^4=h`, and let the class of `h` in `L(x)^*/L(x)^{*4}` have order `e=4` or `e=2`. Let `j∈L^*`. On a monic depressed `(8,12)` client of the partial-`y` high-row reduction, write

```text
H_F(w)-g(z(w))=sum_{ℓ≥1} r_ℓ w^{-ℓ}.
```

Then `8 r_7'=j/u`. If the Kummer generator sends `u↦ζ u`, then `r_7` lies in the inverse-character line: uniquely `r_7=u^3 A` with `A∈L(x)` if `e=4`, and uniquely `r_7=u A` with `A∈L(x)` if `e=2` (after the choice `u^2=v` with `v` monic, `h=v^2`, `v` not a square). These forms convert the terminal row into the equivalent rational ODEs

```text
e=4:  8h A'+6h'A=j,
e=2:  8v A'+4v'A=j,
```

each of which has at most one rational solution. A terminal primitive exists in the Kummer function field if and only if the corresponding ODE has a solution in `L(x)`.

On the smooth projective normalization of the Kummer cover, `dx/u` is exact (up to the nonzero constant `j/8`) whenever such a primitive exists. Every place above `x=∞` is unramified; with `q=1/x` and `t=q^U u` one has `dx/u=-q^{U-2}t^{-1}dq`. Thus `U=1` is impossible, and for `U≥2` the form is regular at infinity. At a finite root of multiplicity `k` the orders are `(4-k)/gcd(4,k)-1` in order four and `(2-k)/gcd(2,k)-1` in order two. Multiplicity four in `h` is a simple pole of nonzero residue on every branch, hence impossible. For `U≥2`, exactness forces a finite root of multiplicity at least five in order four, and a root of `v` of multiplicity at least three (equivalently multiplicity at least six in `h`) in order two.

At `U=2`, `e=2` the only partition of `deg v=4` compatible with those constraints is `mult(v)=[3,1]`, `mult(h)=[6,2]`. For distinct `a,b∈L` that profile is not merely necessary: with `T=u/(x-a)^2` one has `T^2=(x-b)/(x-a)`, `dx/u=(2/(b-a))dT`, and `r_7=j T/(4(b-a))`. The two finite branch points of the normalized quadratic cover are `a` and `b`; `dx/u` has a double pole and zero residue at `a`, is regular at `b`, and is regular at both points above infinity.

This is only the terminal equation. It does not produce the other six tails, Taylor polynomiality, a Keller pair, order-two or order-four closure, `(8,12)`, maximum twelve, or JC2.

---

## Attack 1 — terminal row, inverse character, and both base ODEs

**CONFIRMED.** Existence, uniqueness, the constant-field step, and both implications survive.

**Terminal identity.** The charged Faber source writes the negative tail by `H_F(w)-g(z(w))=sum_{ℓ≥1} r_ℓ w^{-ℓ}` and differentiates at fixed `w`. The chain rule on `g` along `f(z)=w^m` gives `D=-f_z(∂_x g)|_w`, and substitution of the tail produces the plus sign on `f_z sum r_ℓ' w^{-ℓ}`. After the high-row vanishing `h_j'=0`,

```text
D=f_z sum_{ℓ≥1} r_ℓ' w^{-ℓ}.
```

The polynomial parts `A_ℓ=[f_z w^{-ℓ}]_+` vanish for `ℓ≥m`. For `ℓ=m-1`, depression gives `f_z=m z^{m-1}+O(z^{m-3})` and `w^{-(m-1)}=z^{-(m-1)}+O(z^{-(m+1)})`, so `A_{m-1}=m`. The original Jacobian is `J_{(x,y)}=u D` because `z=uy+A/m` has `∂z/∂y=u` and the `z_x` cross terms cancel, hence `D=j/u` with the original constant `j`. The constant row is therefore `m r_{m-1}'=j/u`. Specializing to the `(8,12)` first coordinate, `m=8`, yields exactly `(0.1)`:

```text
8 r_7'=j/u.
```

The opposite tail sign would produce `-8 r_7'=j/u` and is incompatible with the definition `H_F-g=sum r_ℓ w^{-ℓ}`. Characteristic zero is used to have `m≠0` and the binomial root `w=z+O(z^{-1})`.

**Galois action and inverse character.** Preflight: `z=uy+A/8` with `A=a_7/u^7`. The class order `e` divides `4`, hence divides `8`, and `wt(A)≡-(8-1)≡1 mod e`. The generator `σ(u)=ζ u` therefore sends `A↦ζ A` and `z↦ζ z`. Depression `δ=0` is forced on `e>1` by the preflight weight of `δ`, so `f` is monic depressed of degree eight and the unique monic root `w=f^{1/8}=z+O(z^{-1})` satisfies `σ(w)=ζ w`. Faber constants `h_j` survive only for `j≡0 mod e`, so `H_F(ζ w)=H_F(w)`. The original second coordinate is Galois-invariant as a function of `(x,y)`. The tail is therefore an invariant series in `w`:

```text
sum σ(r_ℓ) (ζ w)^{-ℓ} = sum r_ℓ w^{-ℓ},
```

hence `σ(r_ℓ)=ζ^ℓ r_ℓ`. For `ℓ=7` and `ζ^e=1` with `e∣8`, one has `ζ^7=ζ^{-1}`. Thus `r_7` lies in the inverse-character eigenspace.

In a degree-four Kummer field the basis is `1,u,u^2,u^3`, and character `ζ^{-1}=ζ^3` is the line `u^3 L(x)`. In the genuine quadratic field the basis is `1,u`, and character `-1` is the line `u L(x)`. This is the asserted unique shape of `r_7`. (The integer grading `wt(r_ℓ)=12+ℓ` is not required: `12+7=19≡-1 mod 4` and `≡1≡-1 mod 2`, but the Galois computation above uses only the tail definition and `σ(w)=ζ w`.)

**Base ODEs, both directions.** Logarithmic differentiation of `u^4=h` gives `u'/u=h'/(4h)`. Substituting `r_7=u^3 A`,

```text
r_7'=u^3(A'+3 h'A/(4h)).
```

The identity `j/(8u)=j u^3/(8h)` is the rewriting `u^4=h`. Division by `u^3` and multiplication by `8h` (neither zero in the function field) convert `8 r_7'=j/u` into `8h A'+6h'A=j`. Conversely, the same multiplications reverse, so `(0.1)` and `(0.2)` are equivalent.

For `e=2`, write `h=v^2` with `v` monic not a square, and choose the sheet `u^2=v` (the opposite identification `u^2=-v` would replace `j` by `-j` in `(0.3)`; the theorem fixes the sheet). Then `u'/u=v'/(2v)`. With `r_7=u A`,

```text
r_7'=u(A'+v'A/(2v)),     j/(8u)=j u/(8v),
```

and division by `u` followed by multiplication by `8v` yields `8v A'+4v'A=j`. The steps reverse. Equivalence, not mere necessity.

**Uniqueness of the rational solution.** The homogeneous equation `8h A'+6h'A=0` integrates to `A=C h^{-3/4}`. If this were a nonzero element of `L(x)`, then `h^3` would be a fourth power in `L(x)`. Unique factorization in `L[x]` and `gcd(3,4)=1` force every multiplicity of `h` to be divisible by four; `h` is monic, so `h` is a fourth power in `L[x]`, contradicting `e=4`. Likewise `8v A'+4v'A=0` integrates to `A=C v^{-1/2}`, rational only if `v` is a square, contradicting `e=2`. A difference of two solutions of `8 r_7'=j/u` in the full function field is a constant of the function field; after the licensed scalar extension the constants are scalars of `L`, which have trivial character, not inverse character. An uncharged integration constant is therefore excluded on both the rational line and the full Kummer field.

**Existence is the ODE, nothing more.** A primitive in the Kummer field with the forced character is exactly a rational `A` solving `(0.2)` or `(0.3)`. The theorem claims this equivalence and, later, existence for the single profile `[3,1]`. It does not claim that a rational solution exists for an arbitrary divisor class of order four or two. The first-order linear ODE always has a local solution `A=h^{-3/4}(C+(j/8)∫ h^{-1/4} dx)` in a Liouville extension; rationality of that integral is the global exactness condition and is not automatic.

**Constant field.** A finitely generated algebraic extension of `L(x)` in characteristic zero has constant field equal to the algebraic closure of `L` in that extension. After the licensed enlargement (roots of unity, and the finitely many constants needed to split the displayed roots), that constant field is the scalar field. Monicity of `h` is used only to kill a leading-constant Kummer factor in `L^*/L^{*4}` that would otherwise look like order four while being geometric order one; the uniqueness argument above is valuation-theoretic and does not need algebraic closure of `L`.

---

## Attack 2 — infinity, `H=4U`

**CONFIRMED.** Unramified, the displayed local form, sheetwise residue, exclusion of `U=1`, and regularity for `U≥2` all survive. No cancellation between sheets is possible.

Because `h` is monic of degree `4U`,

```text
h(q^{-1})=q^{-4U} η(q),     η(0)=1.
```

For `e=4`, `t=q^U u` satisfies `t^4=η(q)`. The fibre `T^4-1=0` is separable in characteristic zero (`4T^3≠0` at every fourth root of unity), so Hensel lifts four unramified branches of the complete local field `L((q))`, and `q` is a uniformizer at each place above infinity. For `e=2`, `v` is monic of degree `2U` and `t^2=q^{2U}v(q^{-1})` has the same unit value `1` at `q=0`; two unramified places, `q` still a uniformizer. On either client `dx=-q^{-2}dq` and `u=q^{-U}t`, hence

```text
dx/u=-q^{U-2} t^{-1} dq.
```

The coefficient `t^{-1}` is a unit on every sheet because `t(0)^e=1`. The order of `dx/u` at each infinite place is therefore exactly `U-2`.

At `U=1` the form is `-t(0)^{-1} dq`, a simple pole of residue `-t(0)^{-1}≠0` on every sheet. Residues of exact differentials vanish place by place: if `ω=dR` for `R` in the function field, the Laurent coefficient of `τ^{-1}dτ` is zero at each individual place of the smooth projective model. Summing residues over the four (or two) sheets above infinity can give zero by the global residue theorem — for `e=4` the residues are the negatives of the four fourth roots of unity, summing to zero — but that cancellation is irrelevant. Exactness is already impossible at a single infinite place. This kills every order-four or order-two profile of degree `H=4`, including the preflight control `h=x^2(x-1)^2`.

For `U≥2` the order `U-2` is nonnegative, so `dx/u` is regular at every infinite place. There are no further places above infinity: the degree of the extension equals the number of unramified places (residue degree one after roots of unity). No infinite place was missed.

---

## Attack 3 — finite roots, residues, holomorphic-exact obstruction

**CONFIRMED.** Both order formulae, every small multiplicity, the nonzero residues at `mult_h=4`, and the global contradiction survive. Branch-cancellation and missed infinite places do not furnish a loophole.

**Order four.** Let `h=(x-a)^k c(x)` with `c(a)≠0`, `g=gcd(4,k)`, `E=4/g`. The cyclic extension of `L((x-a))` has ramification index `E` and `g` geometric places (degree formula `g·E=4`). A uniformizer `τ` may be chosen so that `x-a=τ^E` and, after Hensel on the unit `c(a+τ^E)`, `u=τ^{k/g} ε(τ)` with `ε(0)≠0`. Then

```text
dx=E τ^{E-1} dτ,     dx/u=E ε^{-1} τ^{E-1-k/g} dτ.
```

The exponent is `E-1-k/g=(4-k)/g-1`, which is `(0.5)`. Independently for each small `k`:

| `k` | `g` | `E` | `ord(dx/u)` | local shape |
|---:|---:|---:|---:|---|
| 1 | 1 | 4 | 2 | zero of order two |
| 2 | 2 | 2 | 0 | regular, ramified |
| 3 | 1 | 4 | 0 | regular, totally ramified |
| 4 | 4 | 1 | `-1` | unramified simple pole |
| 5 | 1 | 4 | `-2` | |
| 6 | 2 | 2 | `-2` | |
| 7 | 1 | 4 | `-4` | |
| 8 | 4 | 1 | `-2` | |

At `k=4` the coefficient of `τ^{-1}dτ` is `E ε(0)^{-1}=ε(0)^{-1}`, and `ε(0)^4=c(a)≠0`. The residue is nonzero on every branch. For `k≥5`, `g` divides `4-k`, so `(4-k)/g` is a negative integer `≤-1` and the order is at most `-2`.

**Order two.** Let `v=(x-a)^k c(x)` with `c(a)≠0`, so the multiplicity in `h` is `2k`. Put `g=gcd(2,k)` and `x-a=τ^{2/g}`, `u=τ^{k/g}ε(τ)`. The identical computation gives `ord(dx/u)=(2-k)/g-1`. At `k=1` the order is `0`; at `k=2` (multiplicity four in `h`) it is `-1` with residue `ε(0)^{-1}≠0`; at `k≥3` it is at most `-2`.

**No branch-cancellation at a finite simple pole.** Each place above `a` has its own residue, a nonzero element of its residue field. Exactness forbids a simple pole at any one of them. Tracing the differential to `P^1_x` can cancel residues; that is a pushforward identity, not exactness on the cover.

**Holomorphic-exact contradiction.** Assume `U≥2`, so infinity is regular by Attack 2. Off the roots of `h`, the cover is unramified over the affine line and `dx/u` is regular of order zero. If every finite multiplicity is at most three in order four, every finite order is `2` or `0`, and `dx/u` is a holomorphic differential on the smooth projective normalization. It is not the zero form (`dx≠0`). If it were `dR` for `R` in the function field, then `R` could have no pole: in characteristic zero, `d(τ^{-m})=-m τ^{-m-1}dτ` with `m≠0`, so a pole of `R` of order `m≥1` produces a pole of `dR` of order `m+1`. A rational function without poles on a complete smooth curve is constant, and `dR=0`, a contradiction. Therefore some finite multiplicity is at least four. Multiplicity exactly four is already excluded by its residue, so some multiplicity is at least five. In particular every profile with all multiplicities at most three is impossible.

In order two, if every root of `v` is simple then every finite order is zero. For `U≥2` the same holomorphic-exact argument applies. A multiple root is required; multiplicity two is the simple-pole case already forbidden; hence some root of `v` has multiplicity at least three, equivalently some root of `h` has multiplicity at least six.

Genus is not needed. On a genus-zero normalization there are in any case no nonzero holomorphic differentials, which is a stronger obstruction to the all-`k≤3` (resp. all-simple) profiles and is compatible with the exactness argument. Places with residue-field extension do not change orders. Affine singularities of `u^4=h` or `u^2=v` are resolved by the normalization on which the orders were computed. No infinite place was used as a hidden pole: for `U≥2` there is none.

Vanishing of residues at poles of order at least two is still necessary for exactness and is not implied by the order formula. The theorem correctly treats those as local filters and retains `(0.2)`/`(0.3)` as the exact global test.

---

## Attack 4 — `U=2`, `e=2`: partition census and the primitive `T`

**CONFIRMED.** `[3,1]`/`[6,2]` is the unique nontrivial candidate, and every identity in `(0.8)` holds on the smooth normalization, including both finite branch points and both infinite places.

Here `deg v=2U=4`. Exactness requires a part at least three and forbids a part equal to two. The integer partitions of four are

```text
[4],     [3,1],     [2,2],     [2,1,1],     [1,1,1,1].
```

`[2,2]` and `[2,1,1]` have a double root of `v`, hence a simple pole of nonzero residue. `[1,1,1,1]` is the all-simple holomorphic case, impossible for `U=2`. The polynomial `v=(x-a)^4` is a square (a fourth power) over an algebraically closed constant extension, so the Kummer class of `h=v^2` is trivial, contrary to `e=2`. The only remaining partition is `[3,1]`. For this partition `h=(x-a)^6(x-b)^2` is a square and, because `v=(x-a)^3(x-b)` has an odd multiplicity, not a fourth power, so the class has order exactly two. Distinctness `a≠b` is required; the coincident case collapses to `[4]`.

**Identities.** Monicity gives `v=(x-a)^3(x-b)`. Set `T=u/(x-a)^2`. Then

```text
T^2=u^2/(x-a)^4=v/(x-a)^4=(x-b)/(x-a).
```

Differentiate: `2T T'=(b-a)/(x-a)^2`. Hence `T'=(b-a)/(2T(x-a)^2)`, and

```text
(2/(b-a)) T' = 1/(T(x-a)^2)=1/u,
```

so `dx/u=(2/(b-a)) dT`. The terminal row then reads `r_7'=(j/8)(1/u)=(j/(4(b-a))) T'`. Integrating, `r_7=j T/(4(b-a))+C`. The constant has trivial character, so `C=0`, and `T=u/(x-a)^2` recovers the displayed formula `r_7=j u/(4(b-a)(x-a)^2)`.

**Independent ODE check of the constant.** Put `A=c(x-a)^{-2}` with `c=j/(4(b-a))`. Then `A'=-2c(x-a)^{-3}` and `v'=(x-a)^2(4x-a-3b)`, so

```text
8v A' = -16c(x-b),     4v'A=4c(4x-a-3b),
8v A'+4v'A = 4c(b-a)=j.
```

The constant in `(0.8)` is therefore exact for `(0.3)`, not merely for the `T`-parametrization.

**Places of the normalized cover.** The substitution `Y=u/(x-a)` gives `Y^2=(x-a)(x-b)`, a smooth conic for `a≠b`, which is the normalization of the singular affine model `u^2=(x-a)^3(x-b)`. Finite branch points are exactly `a` and `b`. At infinity, `Y^2∼x^2` splits into two unramified points, matching Attack 2 for `e=2`.

- At `a`: `k=3`, `g=1`, `x-a=τ^2`, `ord_τ(u)=3`, `ord(dx/u)=-2`. The primitive `T=ε/τ` has a simple pole, so `dT` has pole order two and residue zero (leading term `-ε(0)τ^{-2}dτ`).
- At `b`: `k=1`, `g=1`, `ord_τ(u)=1`, `ord(dx/u)=0`. Regular. Equivalently `T^2=(x-b)/(x-a)` has a simple zero in `x`, hence a simple zero in `τ`, so `T` is a local uniformizer times a unit.
- At both infinite places: `U=2` gives order `0` by `(0.4)`. Directly, `T=u/(x-a)^2=t/(1-aq)^2` is a unit at `q=0`, so `T` and `dT` are regular.

Riemann–Hurwitz on the double cover of `P^1` branched at two points gives genus zero, so a rational primitive is unsurprising; the construction exhibits it. Affine translation and reciprocal scaling in `(x,y)` of Jacobian one send `(a,b)` to `(0,1)` without changing `j`, yielding the compiler profile `h=x^6(x-1)^2`, `T=u/x^2`, `r_7=(j/4)T`. That gauge is not used as existence evidence; `(0.8)` already is.

---

## Attack 5 — firewall

**CONFIRMED.** The theorem does not smuggle a closure.

Faber supplies seven tail equations `r_1'=⋯=r_6'=0` and `8 r_7'=j/u`. Exactness of `dx/u` is the last of these, and only that. The constants `r_1,…,r_6`, the remaining Faber coefficients, both original Taylor jets `u^ℓ ∂_z^ℓ f(A/8)/ℓ!∈L[x]` and the companion family for `g`, polynomiality of any reconstructed pair, and the existence of a Keller pair are unforced. The identity `(0.8)` is existence of a terminal primitive on one divisor profile, not existence of the other six tails on that profile. Order-two and order-four clients remain open. The residual criterion `4∣H` is still the history theorem; this document does not empty `(8,12)`, does not bound maximum twelve, and does not speak to JC2.

The prioritized-consequence paragraph correctly discards the degree-four preflight control `h=x^2(x-1)^2` as an infinity-residue corpse, and correctly refuses to treat `(5.1)` as a closed Rees client. That paragraph is advice, not a hidden existence theorem.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | `8 r_7'=j/u` on every actual monic depressed `(8,12)` client; `r_7` occupies `u^3 L(x)` if `e=4` and `u L(x)` if `e=2`; `(0.1)` is equivalent to `(0.2)` resp. `(0.3)` with unique rational `A` | **CONFIRMED** | opposite tail sign; `A_{m-1}≠m`; Jacobian factor not `u`; `ζ^7≠ζ^{-1}`; a rational homogeneous solution on a nontrivial class; one-way implication only |
| 2 | Every infinite place is unramified; `dx/u=-q^{U-2}t^{-1}dq`; `U=1` has nonzero sheetwise residue; `U≥2` is regular at infinity | **CONFIRMED** | ramification at infinity for monic `h`; residue `0` on some sheet at `U=1`; a missed infinite place of negative order for `U≥2` |
| 3 | Finite orders `(4-k)/gcd(4,k)-1` and `(2-k)/gcd(2,k)-1`; `mult_h=4` is a simple pole of nonzero residue on every branch; for `U≥2` exactness forces `mult_h≥5` in order four and `mult_h≥6` in order two | **CONFIRMED** | a wrong ramification index; residue `0` at `k=4`; cancellation of residues between branches licensing a simple pole; a holomorphic exact nonzero form; an unaccounted pole at infinity |
| 4 | At `U=2`, `e=2` the unique compatible partition is `[3,1]`/`[6,2]`; `T=u/(x-a)^2` satisfies `(0.8)` with exact constant `j/(4(b-a))`; double pole / zero residue at `a`, regular at `b` and at both infinities | **CONFIRMED** | a surviving partition among `[4]`, `[2,2]`, `[2,1,1]`, `[1^4]`; a different constant in `r_7`; nonzero residue at `a`; a pole of `dx/u` at `b` or at infinity |
| 5 | Passing the terminal equation is necessary only. No other tail, Taylor polynomiality, existence of a pair, order-two or order-four closure, `(8,12)`, maximum twelve, or JC2 is licensed | **CONFIRMED** | a hidden promotion in the theorem, the prioritized-consequence paragraph, or the scope firewall |

---

## Remarks (non-blocking)

1. The phrase “uniquely up to the harmless sign `h=v^2`” is slightly loose: monicity of `v` already fixes that sign. The genuine choice is the sheet `u^2=v` rather than `u^2=-v`, which would replace `j` by `-j` in `(0.3)`. The theorem makes that choice explicitly. Not a numbered failure.
2. The integer grading `wt(r_7)=19` is consistent with the inverse character but is not a numbered statement of the charged Faber parent. The Galois argument in Attack 1 does not use it.
3. Partitions and roots are taken after a harmless constant extension containing the needed roots of unity and the displayed `a,b`. Over a non-closed `L`, an irreducible quartic is not a fifth partition: after splitting it is one of the five listed types. The `[4]` exclusion is correctly stated over an algebraically closed constant extension.
4. Characteristic zero is essential and present: `8≠0`, `4T^3≠0` in Hensel, and `d(τ^{-m})` does not drop order. The theorem's opening sentence supplies it.
5. The holomorphic-exact argument is strictly weaker than a genus computation. It is also strictly local-to-global: residue-zero at poles of order `≥2` remains an extra local filter, correctly not folded into the order table.

None of these remarks changes a numbered verdict.

---

## Strict scope firewall

This review confirms an exact terminal necessary condition on nontrivial `(8,12)` Kummer clients with `H=4U`, together with a complete first-degree classification of the order-two profile `[6,2]`. It does **not**:

- solve `r_1'=⋯=r_6'=0` or determine the algebraic fibres of those constants;
- produce the remaining Faber coefficient functions, a rational or polynomial trajectory, or either original Taylor-boundary family;
- classify order-four divisor profiles beyond the local constraints `U≥2`, no multiplicity four, some multiplicity at least five;
- close the order-two client, the order-four client, the cell `(8,12)`, maximum twelve, or JC2;
- assert that the preflight control `h=x^2(x-1)^2` was ever a legal terminal profile (Attack 2 excludes it), or that the compiler profile `(5.1)` is more than a terminal source.

The target's own firewall matches this boundary. No creep was found.

---

## Terminal boundary (accepted, not enlarged)

```text
terminal_row_8_r7=j/u=PROVED
inverse_character_eigenspaces=PROVED
base_ODEs_equivalent_unique_rational_A=PROVED
infinity_U=1_excluded_U>=2_regular=PROVED
finite_orders_and_mult4_residue=PROVED
U>=2_forces_mult_h>=5_e4_and_mult_h>=6_e2=PROVED
U=2_e=2_unique_partition_[3,1]_terminal_exact=PROVED
other_six_tails=NOT_SOLVED
Taylor_polynomiality=NOT_CLAIMED
order_two_client_closed=false
order_four_client_closed=false
(8,12)_empty=false
maximum_twelve=NOT_CLAIMED
JC2=NOT_CLAIMED
```
