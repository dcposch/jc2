# Hostile review — `(8,12)` terminal-power/Belyi theorem and the order-one pure-power core

| Field | Value |
|---|---|
| Target | `xmodel/max12-812-terminal-power-belyi-order1-theorem-20260825.md` |
| Target SHA-256 | `a4d7d6a1173b5a0b785aa61a4c80ad5f46e4ea83f1d73103917c425608666633` |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim |
| Reviewer / model | Grok 4.6 (xAI). Independent hostile rederivation. Different model family from the producer (OpenAI Codex, GPT-5 family). The charged Faber review and the charged terminal-divisor review are same-model and are not used as PASS/CONFIRMED certificates; the terminal row, the inverse character of `r_7`, and the radicand `d` are re-derived below from the identities in those sources |
| Method | source reading and hand derivation only; SHA-256 of the target and the six named parents; no CAS, solver, substantive Python, Lean, or other heavy local computation |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `4fe628a133ae62e16b1bec5e4ed6fcee420dd880` (named producer artifact uncommitted) |
| Date | 2026-08-25 |

Independently recomputed SHA-256 of the target is `a4d7d6a1173b5a0b785aa61a4c80ad5f46e4ea83f1d73103917c425608666633`, matching the launch pin. All six charged sources match the hashes printed in the target's Section 1. Producer verdict language, the target's own status line, and any prior PASS/CONFIRMED token were not used as evidence. No file other than this review was written.

---

## Verdict

The charged theorem is correct as a terminal necessary condition on every `(8,12)` Kummer leaf. Independently: the Faber tail `H(w)-g(z(w))=sum r_ℓ w^{-ℓ}` together with `A_7=8` and `J_{(x,y)}=u D` give `8 r_7'=j/u`; the Kummer generator `u↦ζ u` forces `r_7↦ζ^7 r_7=ζ^{-1} r_7` on both `e=4` and `e=2`, so `T=r_7^e` descends to the exact fixed field `L(x)`; the identity is `d(T')^e=(e j/8)^e T^{e-1}` with `d=h` in order four and `d=v` (not `h=v^2`) in order two, and the two displayed constants are `j^2/16` and `j^4/16`; the finite dictionary is `k=e-n` on zeros and poles of `T`, `k=e` is impossible, uncharged zeros have order exactly `e`, and no finite critical point of `T` lies off the fibres `T=0,∞`; at infinity the prime is `d/dx=-q^2 d/dq`, `T` has no pole, the two local forms are `ord_∞(T-λ)=U-1` and `ord_∞(T)=e(U-1)`, `U=1` is empty, and every branch value lies in `{0,∞,λ}` with `λ` omitted when `T(∞)=0` and unbranched when `U=2` and `T(∞)∈L^*`; on the order-one leaf, a polynomial `q` admitting a rational primitive of `1/q` is a nonzero constant or a single-root pure power of degree `U≥2`, there is no solution for `U=1`, the unique root descends, and both converses hold with the displayed constants. Passing these identities does not solve the other six tails, produce Taylor polynomiality, close any Kummer leaf, or touch JC2.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-812-terminal-power-belyi-order1-theorem-20260825.md` | `a4d7d6a1173b5a0b785aa61a4c80ad5f46e4ea83f1d73103917c425608666633` | target (matches required pin) |
| `xmodel/max12-partial-y-kummer-preflight-20260824.md` | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` | residual `4\|H`, Kummer orders `4,2,1`, `u^4=h`, order-two `h=v^2` with `v` not a square, order-one `h=c q^4`, depression `z=uy+A/8`, `δ=0` on `e>1`, Galois `z↦ζ z` |
| `xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md` | `2951856cabe309fe07f564693a6b48a38cd7108616ffe41305d9583611da90fe` | different-model preflight audit (read; unused as a verdict) |
| `xmodel/max12-partial-y-shared-faber-probe-20260824.md` | `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036` | tail definition, fixed-`w` identity, `A_{m-1}=m`, `m r_{m-1}'=j/u`, character filter on `h_j` |
| `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md` | `e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c` | same-model Faber audit (read; unused as a verdict) |
| `xmodel/max12-812-terminal-exact-differential-divisor-theorem-20260825.md` | `1cd824c9553a800ddf390bc972a29656e1286699406b1ca46bbc94bdfe18084b` | inverse-character eigenspace, base ODEs, residue exclusion of multiplicity `e` |
| `xmodel/max12-812-terminal-exact-differential-divisor-review-grok-20260825.md` | `db67f16dbda759b8481fcbf32491fe77c37483bb5fe70830eb42e95541767251` | same-model divisor audit (read; unused as a verdict) |

All six hashes match the target's parent table. The preflight is consumed only for residual degree `H=4U`, the three live Kummer orders, the identification of the order-two radicand `v`, the polynomial core `u=q`, depression, and the Galois action on `z`. Faber is consumed only for the tail series, the triangular terminal system, the Jacobian factor `u`, and the character filter on the constants `h_j`. The divisor theorem is consumed only as an independent `(8,12)` source of the inverse-character convention and the residue exclusion that the rational-map dictionary recovers; its `[3,1]` existence statement is not an input. No scope-firewall sentence of any parent is an input.

---

## Strongest exact theorem that survives

Let `L` be a characteristic-zero field enlarged by the already licensed finite constant extension so that the required roots of unity and leading scalar roots are present. Let `j∈L^*`. Let `h∈L[x]` be monic of degree `H=4U` with `U≥1` on a nontrivial Kummer leaf, or `h=q^4` with `q∈L[x]` of degree `U≥0` on the trivial leaf, as in the preflight.

On a monic depressed `(8,12)` client, the Faber tail

```text
H(w)-g(z(w))=sum_{ℓ≥1} r_ℓ w^{-ℓ}
```

satisfies `8 r_7'=j/u`. If the Kummer generator sends `u↦ζ u`, then `r_7` occupies the inverse-character line: `σ(r_7)=ζ^7 r_7=ζ^{-1} r_7`. For `e∈{2,4}`, the power `T=r_7^e` is therefore Galois-invariant and lies in the exact fixed field `L(x)`, and is nonconstant. Writing `C: u^e=d(x)` for the smooth projective normalization of the minimal Kummer extension (`d=h` if `e=4`; `h=v^2` and `d=v` if `e=2`, with `deg d=eU`), one has

```text
d (T')^e = (e j/8)^e T^{e-1},
```

equivalently `v(S')^2=(j^2/16)S` if `e=2` and `h(T')^4=(j^4/16)T^3` if `e=4`. Over an algebraic closure, at every finite point `a` with `k=ord_a(d)`,

```text
1≤k<e  <=>  T has a zero of order e-k at a;
k=e            is impossible;
k>e       <=>  T has a pole of order k-e at a.
```

A zero of `T` of order exactly `e` is allowed at a point with `k=0`. Away from `T=0,∞`, the map `T:P^1_x→P^1` has no finite critical point. At `x=∞`, `T` has no pole, and the only local forms are `T(∞)=λ∈L^*` with `ord_∞(T-λ)=U-1`, or `T(∞)=0` with `ord_∞(T)=e(U-1)`. In particular `U=1` is impossible. For `U≥2` every branch value of `T` lies in `{0,∞,λ}`, the third value omitted when `T(∞)=0` and unbranched when `U=2` and `T(∞)∈L^*`. Formula `(0.2)` reconstructs `d=(e j/8)^e T^{e-1}/(T')^e`.

On the order-one leaf, `h=q^4`, `u=q∈L[x]`, `U=deg q`, a rational solution of `8 r_7'=j/q` exists if and only if `U=0` with `q=c∈L^*`, or `U≥2` with `q=c(x-a)^U` for `c∈L^*` and `a∈L`. There is no solution for `U=1`. Conversely every such polynomial has the rational primitive displayed in `(0.10)`.

This is only the terminal equation. It does not produce the other six tails, Taylor polynomiality, a Keller pair, order-four or order-two or order-one closure, `(8,12)`, maximum twelve, or JC2.

---

## Attack 1 — inverse character of `r_7`, fixed-field descent, and the constant in `(0.2)`

**CONFIRMED.** The character is inverse, `T` lies in `L(x)`, `d=v` rather than `h=v^2` in order two, and both displayed constants are exact.

**Terminal row, from Faber, not from a verdict.** The charged Faber source defines the negative tail by `H(w)-g(z(w))=sum_{ℓ≥1} r_ℓ w^{-ℓ}` and differentiates at fixed `w`. Fixed `w` is fixed `f`, so `D=-f_z(∂_x g)|_w`. Substituting the tail produces a plus sign on `f_z sum r_ℓ' w^{-ℓ}`. After high-row vanishing `h_j'=0`,

```text
D = f_z sum_{ℓ≥1} r_ℓ' w^{-ℓ}.
```

The polynomial parts `A_ℓ=[f_z w^{-ℓ}]_+` vanish for `ℓ≥m`. For `ℓ=m-1`, depression gives `f_z=m z^{m-1}+O(z^{m-3})` and `w^{-(m-1)}=z^{-(m-1)}+O(z^{-(m+1)})`, so `A_{m-1}=m`. The original Jacobian is `J_{(x,y)}=u D` because `z=uy+A/m` has `∂z/∂y=u` and the `z_x` cross terms cancel, hence `D=j/u`. The constant row is `m r_{m-1}'=j/u`. Specializing to the `(8,12)` first coordinate, `m=8`, yields exactly `(0.1)`:

```text
8 r_7' = j/u.
```

The opposite tail sign would produce `-8 r_7'=j/u` and is incompatible with the definition `H-g=sum r_ℓ w^{-ℓ}`. Characteristic zero is used to have `m≠0` and the binomial root `w=z+O(z^{-1})`. The right-hand side is nonzero, so `r_7` is nonconstant.

**Galois action and inverse character.** Preflight: `z=uy+A/8` with `A=a_7/u^7` and `wt(A)≡-(8-1)≡1 mod e`. The generator `σ(u)=ζ u` therefore sends `A↦ζ A` and `z↦ζ z`. Depression `δ=0` is forced on `e>1` by the preflight weight of `δ`, so `f` is monic depressed of degree eight and the unique monic root `w=f^{1/8}=z+O(z^{-1})` satisfies `σ(w)=ζ w`. Faber retains `h_j` only for `j≡0 mod e`, so `H(ζ w)=H(w)`. The original second coordinate is Galois-invariant as a function of `(x,y)`. The tail is therefore an invariant series in `w`:

```text
sum σ(r_ℓ) (ζ w)^{-ℓ} = sum r_ℓ w^{-ℓ},
```

hence `σ(r_ℓ)=ζ^ℓ r_ℓ`. For `ℓ=7` and `ζ^e=1` with `e∣4∣8`, one has `ζ^8=1`, so `ζ^7=ζ^{-1}`. This holds for both live nontrivial orders:

```text
e=4:  ζ^7=ζ^3=ζ^{-1},
e=2:  ζ=-1,  (-1)^7=-1=ζ^{-1}.
```

Thus `r_7` lies in the inverse-character eigenspace, as the target's “charged tail convention” states. In a degree-four Kummer field the basis is `1,u,u^2,u^3` and character `ζ^{-1}=ζ^3` is the line `u^3 L(x)`. In the genuine quadratic field the basis is `1,u` and character `-1` is the line `u L(x)`.

**Fixed-field descent of `T=r_7^e`.** Apply `σ`:

```text
σ(T) = σ(r_7)^e = (ζ^{-1} r_7)^e = ζ^{-e} T = T.
```

The extension `L(x)(u)/L(x)` is cyclic Kummer of exact degree `e` (preflight: class order equals extension degree after roots of unity are in `L`; the order-two leaf is the genuine quadratic `L(x)(√v)`, not a degenerate quartic). The Galois group is the full deck group. An element fixed by every deck transformation therefore lies in the exact fixed field `L(x)`, not in a larger intermediate field. Exactness of the class is load-bearing: if the class had smaller order, the displayed power would still be invariant but would live in a proper subextension already named by a different leaf.

Explicitly: `e=4` gives `r_7=u^3 A` and `T=u^{12} A^4=h^3 A^4∈L(x)`; `e=2` gives `r_7=u A` and `T=u^2 A^2=v A^2∈L(x)`.

**The identity `(0.2)`, with the order-two radicand challenged.** Let `r=r_7` and `T=r^e`. Differentiate in `x` and use `(0.1)`:

```text
T' = e r^{e-1} r' = e r^{e-1} (j/(8u)) = (e j/8) r^{e-1}/u.
```

Raise to the `e`-th power and use the *minimal* equation `u^e=d`:

```text
(T')^e = (e j/8)^e r^{e(e-1)} / u^e = (e j/8)^e T^{e-1} / d,
```

which rearranges to `(0.2)`. The radicand is `d`, not `h`, on every leaf.

- Order four: the minimal cover is `u^4=h`, so `d=h`. Then `(4j/8)^4=(j/2)^4=j^4/16`, and `T^{e-1}=T^3`, which is `(0.4)`.
- Order two: the class of `h` in `L(x)^*/L(x)^{*4}` has order two, so `h=v^2` with `v` monic and not a square, and the *minimal* cover is `u^2=v`. Thus `d=v` and `deg d=2U=eU`. Substituting `d=h=v^2` would produce `h(S')^2=v·(v(S')^2)=(j^2/16) v S`, which is not `(0.3)`. The target's explicit sentence “in the order-two leaf `h=v^2` and `d=v`” is therefore necessary and correct. The constant is `(2j/8)^2=(j/4)^2=j^2/16`, and `T^{e-1}=S`, which is `(0.3)`.

**Nonconstancy of `T`.** If `T` were constant then `T'=e r^{e-1} r'=0`. Characteristic zero gives `e≠0`. If `r=0` then `8 r'=j/u≠0` is already false, so `r^{e-1}≠0` and `r'=0`, contradicting `(0.1)`. Thus `T` is nonconstant as claimed.

**Reconstruction `(0.8)`** is the same identity solved for `d`. It is a formula, not a minimality proof: exact order `e` of the class of `d` remains a standing hypothesis.

---

## Attack 2 — finite dictionary, all three values of `T`, and omitted critical points

**CONFIRMED.** The dictionary `(0.5)` holds at every finite place; `k=e` is empty; uncharged zeros have order exactly `e`; no finite critical point off `{T=0,∞}` was omitted.

Work over an algebraic closure, at a finite point `a`, with uniformizer `t=x-a`. Characteristic zero is used throughout: if `n=ord_a(T)≠0` then `ord_a(T')=n-1` exactly, because the leading coefficient is multiplied by the nonzero integer `n`. Write `k=ord_a(d)`. Polynomiality of `d` forces `k≥0` at every finite place. Take orders in `(0.2)`, whose constant `(e j/8)^e` is a unit.

**Case `T(a)=0` or `T(a)=∞`, i.e. `n≠0`.** Then

```text
k + e(n-1) = (e-1)n,
```

so `k=e-n`. This is the target's `(3.1)`, and it covers poles as well as zeros: a pole of order `m>0` is `n=-m`, whence `k=e+m`.

- If `n>0` (a zero of `T`), then `k=e-n`. Polynomiality `k≥0` forces `n≤e`. Combined with `n≥1` one has `1≤n≤e`. A charged root `k>0` forces `n=e-k` with `1≤k<e`. The endpoint `n=e` is `k=0`, an uncharged zero of `T` of order exactly `e`. A zero of any other order at an uncharged point is impossible: `k=0` and `n≠0` plug into `(3.1)` to give `n=e` and nothing else.
- If `n=-m<0` (a pole of `T`), then `k=e+m>e`. A pole of order `m` is precisely a root of `d` of multiplicity `e+m`. There are no uncharged poles: `k=0` and `n=-m` would give `m=-e<0`.

**Case `T(a)` finite and nonzero.** Write `T-T(a)=c t^s+⋯` with `c≠0` and `s≥1` (nonconstancy of `T`). Then `ord_a(T')=s-1`, while `ord_a(T)=0`, so `(0.2)` gives

```text
k = -e(s-1).
```

Polynomiality forces `k≥0`, hence `s-1≤0`. Combined with `s≥1` one has `s=1` and `k=0`. Local degree one, unramified, and `d` is a unit at `a`. In particular `T'` cannot vanish at any finite point where `T` is finite and nonzero.

**The three clauses of `(0.5)`, as equivalences under `(0.2)`.**

- If `1≤k<e`, the finite-nonzero case is excluded (`k=0`) and the pole case is excluded (`k>e`), so `T` has a zero, of order `n=e-k`. Conversely a zero of that order forces `k=e-n` in `{1,…,e-1}`.
- If `k=e`, then `n≠0` would give `n=0` from `k=e-n`, a contradiction; the finite-nonzero case would give `e=-e(s-1)`, hence `s=0`, which is not a local expansion of a nonconstant function. All three cases fail. This recovers, on the base `P^1_x`, the divisor theorem's residue exclusion of multiplicity `e` (multiplicity four in `h` if `e=4`; a double root of `v` if `e=2`) without importing that residue computation.
- If `k>e`, the zero and finite-nonzero cases are excluded, so `T` has a pole of order `k-e`. Conversely a pole of order `m` forces `k=e+m`.

**Uncharged zeros.** Allowed, of order exactly `e`, at points with `k=0`. They are ramified over the value `0` whenever `e≥2`, which both live orders satisfy. They do not violate `(0.5)`; they sit outside its first line, as the target states.

**No omitted finite critical point.** Critical points of a rational map `T:P^1→P^1` in the affine line are: zeros of `T'` at which `T` is holomorphic, and poles of order at least two.

- A zero of `T'` at which `T` is finite and nonzero is the case `s≥2` already excluded.
- A zero of `T'` at which `T=0` lies on the fibre `T=0`.
- A pole of `T` of order `m` has local degree `m`; it is ramified precisely when `m≥2`, and in any case lies on the fibre `T=∞`. (If `T` is holomorphic at a finite point then so is `T'`, so there is no hidden pole of `T'` off the pole fibre of `T`.)

Thus every finite critical point lies on `T=0` or `T=∞`. The claim “away from `T=0,∞`, the rational map `T` has no finite critical point” is exact. Infinity is not a finite point and is treated in Attack 3.

**What would have broken the dictionary.** Characteristic `p` dividing a local order `n`; a non-polynomial radicand allowing `k<0` and thereby `s>1` off `{0,∞}`; using `k=ord_a(h)` rather than `k=ord_a(d)` on the order-two leaf (a double root of `h` would then be mislabelled `k=2` rather than `k=1` in `v`). None of these occurs.

---

## Attack 3 — infinity, the prime `-q^2 d/dq`, `U=1`, `λ=0`, `U=2`, and unramified cases

**CONFIRMED.** `T` has no pole at infinity; the two local forms in `(0.6)` are exact; `U=1` is empty; branch values lie in `{0,∞,λ}` as claimed.

Put `q=1/x`. The derivative in `(0.2)` is the `x`-derivative. The chain rule is

```text
d/dx = (dq/dx) d/dq = -q^2 d/dq,
```

not `d/dq`. Forgetting the factor `-q^2` would replace every infinite order below by the wrong integer and is the first thing this attack is designed to catch. Since `deg d=eU` with nonzero leading coefficient, `d(q^{-1})=c q^{-eU}+⋯` with `c≠0`, so `ord_q(d)=-eU`.

**Finite nonzero value, `T(∞)=λ∈L^*`.** Write `T-λ=c q^s+⋯` with `c≠0` and `s≥1` (this is the definition of `T(∞)=λ` for a nonconstant rational function). Then `dT/dq` has order `s-1`, and

```text
ord_q(T') = ord_q(-q^2 dT/dq) = 2+(s-1) = s+1.
```

The right-hand side of `(0.2)` has order `(e-1)·ord_q(T)=0`. The left-hand side has order `-eU+e(s+1)`. Thus `s+1=U`, so `s=U-1`. This requires `s≥1`, hence `U≥2`.

**Zero, `T(∞)=0`.** Write `T=c q^n+⋯` with `n>0`. Then `ord_q(T')=n+1`, and `(0.2)` gives

```text
-eU + e(n+1) = (e-1)n,
```

so `n=e(U-1)`. For `U=1` this is `n=0`, not a zero. For `U≥2` it is a genuine zero of order `e(U-1)≥e≥2`.

**Pole, `T(∞)=∞`.** Write `T=c q^{-m}+⋯` with `m>0`. Then `ord_q(dT/dq)=-m-1` and `ord_q(T')=2+(-m-1)=1-m`. The same calculation gives

```text
-eU + e(1-m) = (e-1)(-m),
```

so `m=e(1-U)`. For `U≥1` this is `≤0`, contradicting `m>0`. Thus `T` has no pole at infinity. (In particular `λ=∞` is not a third local form.)

**Exclusion of `U=1`.** The finite-nonzero case would require `s=0`, which is not a nonconstant local expansion of `T-λ`. The zero case would require `n=0`. The pole case would require `m=0`. No nonconstant germ at infinity is compatible with `(0.2)` when `U=1`. Combined with Attack 1 (nonconstancy of `T` on `P^1`), there is no terminal solution at `U=1`. This is independent of the divisor theorem's sheetwise residue of `dx/u` at `U=1`; the two killings are compatible and neither is used as input to the other here.

**Challenge `λ=0`.** The two finite-value cases are disjoint. Substituting `λ=0` into the first line of `(0.6)` would predict order `U-1`, whereas a genuine zero at infinity has order `e(U-1)`. For `e=4` and `U=2` these are `1` versus `4`. The target states `λ∈L^*` in the first line and treats `T(∞)=0` separately. No silent identification of `λ` with `0` occurs.

**Challenge `U=2` and unramified cases.** If `T(∞)=λ∈L^*` and `U=2`, the local degree at infinity is `s=U-1=1`, so infinity is unramified. Moreover every finite preimage of `λ` is unramified by Attack 2 (`s=1` off `{0,∞}`). Therefore `λ` is *never* a branch value when `U=2` and `T(∞)∈L^*`. The target's phrase “may be unbranched when `U=2`” is true (and, on this subcase, is always unbranched rather than only possibly so). If instead `T(∞)=0` and `U=2`, the local degree at infinity is `n=e≥2`, so infinity *is* ramified, with critical value `0` already in the set; there is no third value. For `U≥3` and `T(∞)=λ`, one has `s=U-1≥2`, so `λ` is genuinely a branch value.

**At most three branch values.** By Attack 2 every finite critical value lies in `{0,∞}`. The only remaining domain point is `x=∞`, whose value is either `0` or a single constant `λ∈L^*`. This is `(0.6)`–`(0.7)`. After a constant target Möbius sending `{0,∞,λ}` to `{0,1,∞}` when all three occur, `T` is a Belyi-type rational map in the weak sense that its branch locus is contained in three points. When `T(∞)=0`, or when `U=2` and `T(∞)=λ`, the branch locus has at most two points (and in the degree-one case, which occurs, it is empty; the inclusion `(0.7)` remains valid). No assertion that every abstract passport is realized is made, and none is used.

The local analysis lives on the base `P^1_x`. Smoothness of the affine model `u^e=d` is irrelevant: the normalization is invoked only to name the cover through which `T` descended.

---

## Attack 4 — order one: rational primitives of `1/q`

**CONFIRMED.** A polynomial `q` admitting a rational `R` with `R'=1/q` is a nonzero constant, or a single-root pure power of degree at least two. There is no solution of degree one. The unique root descends. Both converses hold, with the constants in `(0.10)` exact.

On the trivial Kummer leaf the preflight writes `h=c q^4` and, after the licensed leading-scalar extension, `h=q^4` with `u=q∈L[x]`. Put `R=(8/j) r_7`. Then `(0.1)` is exactly `R'=1/q`. Characteristic zero, `j∈L^*`, and `8≠0` make this equivalent to rationality of `r_7`. The argument below does not use Kummer theory.

**Constants.** If `U=deg q=0` then `q=c∈L^*`, `R'=1/c`, and `R=(1/c)x+C`. Thus

```text
r_7 = (j/(8c)) x + C',     C'∈L,
```

which is `(0.10)` for `U=0`. Conversely every nonzero constant has this rational primitive.

**Simple roots are impossible.** Suppose `q` has a simple root at `a`. Then `1/q` has a simple pole. A rational function's derivative never has a simple pole: if `R` has a pole of order `m≥1` then `R'` has a pole of order `m+1≥2`; if `R` is regular then `R'` is regular. Equivalently, the residue of `dR` at every place vanishes, while the residue of `dx/q` at a simple root is `1/q'(a)≠0`. Thus every root of `q` has multiplicity at least two.

**Degree one is empty.** If `U=1` then `q` is linear, hence has a unique simple root, already forbidden. There is no rational primitive. The formal integral is logarithmic.

**Exact finite pole orders, `U≥2`.** Work over an algebraic closure. Let the distinct roots have multiplicities `m_1,…,m_N` with `sum m_i=U` and each `m_i≥2`. At the `i`-th root, `1/q=c_i t^{-m_i}(1+O(t))` with `c_i≠0`. A rational primitive must therefore have a pole of order exactly `m_i-1`: a more negative pole would make `R'` too polar, a milder pole (or regularity) not polar enough, and the leading coefficient matches by `α=-c_i/(m_i-1)` with `m_i-1≠0`. There are no other finite poles of `R`: an extra finite pole of `R` would produce a pole of `R'` off the roots of `q`.

**Infinity.** Let `s=1/x`. Then `dR/dx=1/q=x^{-U}(lc(q)^{-1}+O(x^{-1}))` has exact order `U` in `s`. The chain rule `dR/dx=-s^2 dR/ds` gives `ord_s(dR/ds)=U-2` exactly. A pole of `R` of order `m>0` at infinity would give `ord_s(dR/ds)=-m-1`, hence `1-m=U≥2`, so `m≤-1`, a contradiction. Thus `R` is finite at infinity. Writing `R-R(∞)=α s^k+⋯` with `k≥1` and `α≠0`, one has `k-1=U-2`, so

```text
ord_∞(R-R(∞)) = U-1
```

exactly. This is `(5.2)`. For `U≥2` the order is at least one, a genuine vanishing.

**Global degree versus local degree.** As a rational map `R:P^1→P^1` regular at infinity, the degree equals the total finite pole degree:

```text
deg R = sum_i (m_i-1) = U-N.
```

The local mapping degree at infinity is `U-1` by `(5.2)`. A local degree cannot exceed the global degree (the sum of local degrees over any fibre equals `deg R`). Hence `U-1≤U-N`, so `N≤1`. A nonconstant polynomial over an algebraic closure has a root, so `N≥1`. Therefore `N=1` and `q=c(x-a)^U`.

Equality in the degree comparison then says that infinity is the unique preimage of `R(∞)`, consistent with a single finite pole of order `U-1` and with the explicit shape `R=c'(x-a)^{1-U}+C`.

**Descent of the unique root.** The polynomial `q` already lies in `L[x]`. Expanding `c(x-a)^U`, the ratio of the two leading coefficients is `-U a`, and `U≠0`, so `a∈L` by arithmetic in the coefficient field. Equivalently the unique root is Galois-stable over `L` and therefore lies in `L` after the stated constant extension (which was needed for leading scalar roots of `h=q^4`, not for `a` itself). No further extension is required.

**Converse for `U≥2`.** Direct integration:

```text
R' = 1/(c(x-a)^U),     R = (x-a)^{1-U}/(c(1-U)) + C,
```

and `1-U≠0`. Multiplying by `j/8` yields exactly `(0.10)`. The function is rational. A difference of two primitives of `1/q` is a constant, so this is the full rational solution space.

**No other polynomials.** A power of an irreducible of degree `≥2` over `L` would split into `N≥2` distinct roots over the algebraic closure and is already excluded by `N=1`. Constants were handled as `U=0`.

---

## Attack 5 — firewall

**CONFIRMED.** The theorem does not smuggle a closure.

Faber supplies seven tail equations `r_1'=⋯=r_6'=0` and `8 r_7'=j/u`. The present document uses only the last of these. The constants `r_1,…,r_6`, the remaining Faber coefficients, both original Taylor jets, polynomiality of any reconstructed pair, a strict Rees boundary, rational coefficient reconstruction, and the existence of a Keller pair are unforced.

On the nontrivial leaves, three-value geometry of `T` is a necessary constraint on any terminal-power map satisfying `(0.2)`. It is not a census of passports, not a lift to the lower Faber fibre, and not existence of such a `T` for an arbitrary divisor class. The divisor theorem's existence statement for the single profile `[3,1]` at `U=2`, `e=2` is not consumed and is not repeated as a conclusion here.

On the order-one leaf, `(0.9)`–`(0.10)` collapse the *terminal* profile space of `q` to constants and single-root powers. That is existence of a rational primitive of `1/q`, not existence of the other six tails on those profiles, and not polynomiality of a Keller pair with that core.

No complete Kummer leaf is closed. The residual criterion `4∣H` is still the history theorem. The document does not empty `(8,12)`, does not bound maximum twelve, and does not speak to JC2. The target's Section 6 matches this boundary.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | `8 r_7'=j/u`; inverse character `ζ^7=ζ^{-1}` on both `e=4` and `e=2`; `T=r_7^e∈L(x)` by exact-class descent; `d(T')^e=(e j/8)^e T^{e-1}` with `d=v` not `h=v^2` in order two; constants `j^2/16` and `j^4/16`; `T` nonconstant | **CONFIRMED** | opposite tail sign; `A_7≠8`; Jacobian factor not `u`; `ζ^7≠ζ^{-1}`; `T` living in a proper subfield of a non-minimal cover; identity written with radicand `h` on `e=2`; `(4j/8)^4≠j^4/16`; constant `T` compatible with `(0.1)` |
| 2 | Finite dictionary `(0.5)`; `k=e` impossible; uncharged zeros of order exactly `e` at `k=0`; no finite critical point off `{T=0,∞}` | **CONFIRMED** | `ord(T')≠n-1` at a finite place with `n≠0`; a finite point with `T` finite nonzero and `s≥2`; a pole of `T'` off the pole fibre of `T`; `k=e` realized; an uncharged zero of order other than `e` |
| 3 | Prime `d/dx=-q^2 d/dq`; no pole of `T` at `∞`; exact orders `(0.6)`; `U=1` empty; branch values in `{0,∞,λ}`; `λ=0` not silently used; `U=2` with `T(∞)∈L^*` unramified at `λ` | **CONFIRMED** | infinite orders computed with `d/dq` in place of `d/dx`; a pole of `T` at `∞`; `s=U+1` or `n=U-1` at a zero of `T`; a terminal germ at `U=1`; `λ=0` inserted into the first line of `(0.6)`; a finite critical value off `{0,∞,λ}` |
| 4 | Order one: `R'=1/q` with `R` rational forces `U=0` or `q=c(x-a)^U` with `U≥2`; `U=1` empty; simple roots impossible; `deg R=U-N`; local degree `U-1` at `∞`; unique root in `L`; converses `(0.10)` | **CONFIRMED** | a rational primitive of `1/(x-a)`; a simple pole of a rational derivative; `U-1>U-N`; a second distinct root surviving the degree comparison; `a∉L` for `q∈L[x]`; a wrong constant `1-U` or `8c` |
| 5 | Terminal necessity only. No other tail, Taylor polynomiality, existence of a pair, leaf closure, `(8,12)`, maximum twelve, or JC2 is licensed | **CONFIRMED** | a hidden promotion in the theorem statement, Section 6, or the order-one converse |

---

## Remarks (non-blocking)

1. For `U=2` and `T(∞)∈L^*`, the third value `λ` is always unbranched, not only possibly: every preimage, finite or infinite, has local degree one. The target's “may be unbranched” is correct and slightly weak. When additionally `deg T=1` (as in the divisor theorem's `[3,1]` profile, which is *not* an input here), the branch locus is empty and `(0.7)` holds vacuously. Not a numbered failure.
2. The notation `d(T')^e` is `d·(T')^e`. The specializations `(0.3)`, `(0.4)` and the reconstruction `(0.8)` make the parsing unambiguous.
3. Descent of the order-one root does not need Galois stability as a separate step: `a=-q_{U-1}/(U q_U)` is already in `L`. The target's Galois sentence is redundant and correct.
4. Characteristic zero is essential and present: `8≠0`, `e≠0`, `ord(T')=n-1`, `m_i-1≠0`, and `d(τ^{-m})` does not drop order.
5. The integer grading `wt(r_7)=12+7=19≡-1 mod 4` is consistent with the inverse character but is not a numbered statement of the charged Faber parent. Attack 1 does not use it.
6. Places with residue-field extension do not change orders. Affine singularities of `u^e=d` are irrelevant because the dictionary is on the base.

None of these remarks changes a numbered verdict.

---

## Strict scope firewall

This review confirms a terminal necessary condition: on nontrivial `(8,12)` Kummer clients a rational three-value (at most) terminal-power map satisfying `(0.2)`, and on the order-one leaf a collapse of the polynomial core to constants and single-root powers of degree `U≥2`. It does **not**:

- solve `r_1'=⋯=r_6'=0` or determine the algebraic fibres of those constants;
- produce the remaining Faber coefficient functions, a rational or polynomial trajectory, either original Taylor-boundary family, a strict Rees boundary, or a Keller pair;
- classify three-value passports, realize any passport, or lift a passport to the lower Faber fibre;
- consume or restate the divisor theorem's existence of a terminal primitive on `[3,1]` at `U=2`, `e=2`;
- close the order-four client, the order-two client, the order-one client, the cell `(8,12)`, maximum twelve, or JC2.

The target's own firewall matches this boundary. No creep was found.

---

## Terminal boundary (accepted, not enlarged)

```text
terminal_row_8_r7=j/u=PROVED
inverse_character_and_T_in_L(x)=PROVED
identity_d(T')^e=(e_j/8)^e_T^(e-1)=PROVED
order_two_radicand_d=v_not_h=PROVED
finite_dictionary_and_k=e_impossible=PROVED
uncharged_zeros_order_exactly_e=PROVED
no_finite_critical_point_off_zero_pole_fibres=PROVED
infinity_prime_-q^2_d/dq_orders_0.6_U=1_empty=PROVED
at_most_three_branch_values=PROVED
order_one_constant_or_single_root_U>=2=PROVED
order_one_U=1_empty_converses_0.10=PROVED
other_six_tails=NOT_SOLVED
Taylor_polynomiality=NOT_CLAIMED
passport_census_or_lift=NOT_CLAIMED
any_Kummer_leaf_closed=false
(8,12)_empty=false
maximum_twelve=NOT_CLAIMED
JC2=NOT_CLAIMED
```
