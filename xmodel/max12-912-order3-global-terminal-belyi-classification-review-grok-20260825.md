# Hostile different-model review — whole-order-three terminal Belyi classification

| Field | Value |
|---|---|
| Claim under review | Scope-promotion audit: every actual characteristic-zero `(9,12)` partial-`y` trajectory on the nontrivial order-three Kummer branch has `9 r8'=j/u` and `sigma(r8)=zeta^2 r8`, hence `T:=r8^3 in C(x)` nonconstant with `h=(j^3/27) T^2/(T')^3`; writing reduced `T=A/B` and `W=A'B-AB'` gives the selected-branch Wronskian/passport classification with no selected-Q8, `k=mu=0`, or `nu!=0` input |
| Overall verdict | **CONFIRMED** |
| Smallest failing identity | none |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking: the integer grading `wt(r_l)=12+l` is derived here from the Faber tail definition plus monic `g` of degree 12, not a numbered theorem of the charged Faber parent; only the character `20≡2 mod 3` is used. Over `C` the preflight monic-core lemma is automatic. The terminal nondegeneracy erratum is not load-bearing for the direct-cube identity, which already excludes `T=0` by `9 r8'=j/u≠0`) |
| Evidence tier | independent hand re-derivation of the Galois character of `r8`, the identities `T=r8^3=h^2 R^3`, `T'=(j/3) h R^2`, and `(1.1)`, the Wronskian orders and polynomiality criterion, both unequal-degree killings, the balanced passport, `r+s=e+1`, `deg h=3(e+1)`, and Riemann–Hurwitz saturation; full read of the target, the same-model AS scope audit (context only), and every charged parent; repository search for a prior branch-wide promotion; no CAS, solver, or substantial Python |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the composition producer. The charged Faber review is same-model and is not used as evidence for the covariance or `(1.1)`; those are re-derived below. The charged preflight and selected-terminal reviews are Claude |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD at close | `f96845eecaa073110d1526e0b08117205a4dcf30` |
| Date | 2026-08-25 |
| Execution constraint | Mathematical/provenance audit only. SHA-256 of the target, the AS cross-check, and all seven charged parents were recomputed. No CAS, solver, fibre compiler, or replay was run |

The target, the independent same-model scope cross-check (context, not evidence), and every charged parent were read in full before any verdict. No producer, case, canonical, coordination, prompt, run, or log file was edited. The only file written is this review.

---

## Verdict in one paragraph

The composition is exact. Universal Faber supplies the terminal row `9 r8'=j/u` on every actual monic depressed `(9,12)` Keller trajectory, with no selected-Q8, `k`, `mu`, or `nu` input. The preflight Galois action `sigma(z)=zeta z` together with the Faber tail `H(w)-g(z(w))=sum r_l w^{-l}` and the reviewed character filter on the constants `h_j` force `sigma(r8)=zeta^2 r8`, hence `r8=u^2 R` with `R in C(x)`, before any coefficient-component choice. The cube `T=r8^3` is then Galois-invariant and equals `h^2 R^3 in C(x)`; differentiating the original row produces `T'=(j/3) h R^2` and the scalar identity `(1.1)` with constant `j^3/27` rather than the selected `nu^{10}` constant. Zero, constant, ramified, and scalar edge cases all fail to produce a loophole: `j/u≠0` kills `r8=0` and `T` constant, ramification of `L/K` never leaves `T` or `R` as functions of `x`, and the scalar is exact. After `T=A/B` is reduced, the Wronskian criterion, both unequal-degree killings, the balanced passport, `r+s=e+1`, `deg h=3(e+1)`, and Riemann–Hurwitz saturation are the selected classifier's Sections 3–4 verbatim, and those sections use no Q8 coordinate, no `nu`, no selected component, no parity, and no contact theorem. The Kummer hypotheses `h in C[x]`, `3|deg h`, and `h` noncube are licensed on every actual nontrivial-Kummer residual `(9,12)` trajectory and are exactly the two inputs that empty the unequal strata. Repository search found no earlier branch-wide promotion: the ninth-power identity is old algebra (leaf-4 Claim 5, selected `(1.1)`), while the branch-wide reuse of the Belyi passport is new as a composition/scope theorem. The cyclic `D=1,2` controls, lower fibre, original-terminal converse, both Taylor families, removed boundaries, order-one/B8 leaves, maximum twelve, and JC2 remain unclaimed.

**CONFIRMED**

---

## Hashes and charged parents

Recomputed SHA-256, matching the target's parent table and the launch pins:

| Artifact | SHA-256 | Role |
|---|---|---|
| `xmodel/max12-912-order3-global-terminal-belyi-classification-audit-20260825.md` | `28f33b993726b4bd7441a79a8f4208983dbbd0c5e4113d839a78af1b8cc7b6c6` | target (matches required pin) |
| `xmodel/max12-912-order3-universal-terminal-belyi-scope-audit-as-20260825.md` | `4518ee123fe422e6ee287ea43e865943059455dfcaa6a7f863717d3626e20117` | same-model scope cross-check; context only |
| `xmodel/max12-partial-y-kummer-preflight-20260824.md` | `30cb45ccb64bc3666a8f1c6b223d89654a69b31bd5e96eb8915718b0f2de7b07` | `h in C[x]`, order-three class, `3\|deg h`, noncube, `sigma(z)=zeta z` |
| `xmodel/max12-partial-y-kummer-preflight-review-claude-20260824.md` | `2951856cabe309fe07f564693a6b48a38cd7108616ffe41305d9583611da90fe` | CONFIRMED source/Kummer audit |
| `xmodel/max12-partial-y-shared-faber-probe-20260824.md` | `d303bf76853a286c9fedf6dedcce430b4575f2c0040c050d57b954e599dc0036` | terminal row, tail definition, `h_j` character filter |
| `xmodel/max12-partial-y-shared-faber-probe-review-grok-20260824.md` | `e2ddc5b50506e4ba7a933265c640f2abd77ab51a077c3672b7ef9d90f77aa47c` | CONFIRMED formal-Laurent verification (same-model; unused as evidence below) |
| `xmodel/max12-912-order3-terminal-belyi-classification-20260824.md` | `5d8806db54eb2056dd7aafe6fb7dc342c68be1bef7cba06b96beeeaa765273fc` | divisor/Wronskian/infinity/passport |
| `xmodel/max12-912-order3-terminal-belyi-classification-review-claude-20260824.md` | `713e41def64d0fc313d254cae5d660e412f5ba9b69bd4d7c0e6c212a4688c52b` | CONFIRMED audit of every classification step |
| `xmodel/max12-912-order3-terminal-belyi-classification-erratum-20260825.md` | `0221a683fc88daeb162d84096e94200989dd3853d3f319455bf13f4e1dd93b1f` | `Z≠0` on the selected ninth-power form |

Read in full before deciding, in addition to the table: the selected classifier's residual Section 5, the Faber terminal system `(0.1)` and character/target quotient, and the preflight Kummer split including the monic-core constant-field lemma.

---

## Attack 1 — covariance `sigma(r8)=zeta^2 r8` before any selected load

**CONFIRMED.** No selected-Q8 chart, no `k=mu=0`, and no `nu≠0` enters.

**Constant field.** Work after the licensed scalar extension containing `mu_3`. The target takes `K=C(x)` with `C` algebraically closed of characteristic zero, `L=K(u)`, `u^3=h` not a cube. The preflight review's monic-core lemma says the constant field of `k(x)(u)` equals `k` for monic nonconstant `h`. Here `k=C` is algebraically closed, every leading constant is a cube, and the class of `h` in `C(x)^*/C(x)^{*3}` is the divisor class, so the constant field of `L` is `C` whether or not `h` is written monic. Constants of `L` are therefore scalars in `C`.

**Galois action on `z`.** Preflight: `z=uy+A/m` with `m=9`, `wt(A)=-(m-1)≡1 mod 3`, `sigma(u)=zeta u`. Hence `sigma(z)=zeta z`. Depression `delta=0` is forced on the nontrivial class, so `f` is monic depressed of degree 9 in `z` and the unique monic root `w=f^{1/9}=z+O(z^{-1})` satisfies `sigma(w)=zeta w`.

**Weight convention.** Faber defines the tail by `H(w)-g(z(w))=sum_{l≥1} r_l w^{-l}` with `H(T)=sum h_j T^j` and `g` monic of degree `n=12`. Under the geometric `C^*` grading `z↦λz`, `w↦λw`, each term of `H(w)` and of `g` has weight 12 (the constants `h_j` carry weight `12-j`), so `r_l` has integer weight `12+l`. The Kummer generator is the case `λ=zeta`, and the character is weight mod 3:

```text
wt(r8)=12+8=20≡2 mod 3,     sigma(r8)=zeta^2 r8.
```

An equivalent Galois-only computation, using only numbered Faber statements, reaches the same eigenspace without the integer grading. Faber forces every `h_j` to be a differential constant, and the character filter (Faber §4) retains `h_j` only for `j≡0 mod e`. On `e=3` one has `H(zeta w)=H(w)`. The value of `g` is the original second coordinate, Galois-invariant as a function of `(x,y)`. The tail is therefore invariant as a series in `w`, which forces `sigma(r_l) zeta^{-l}=r_l`, i.e. character `+l`. For `l=8` this is again `8≡2 mod 3`. The three target gauges `(h_9,h_0,h_3)` are not needed: they also have `j≡0 mod 3`, so they do not mix characters.

**Eigenspace.** `L=K⊕u K⊕u^2 K` as `K`-vector spaces. Character two is exactly the line `u^2 K`. Thus `r8=u^2 R` with `R in K=C(x)`, on every actual trajectory in the nontrivial order-three class, with no coefficient-component restriction. (The same character argument applied to *constant* tails would force `r1=r2=r4=r5=r7=0` and allow `r3=mu`, `r6=nu`; the target correctly leaves that fibre charged and does not use it.)

**Faber landing is universal.** For an actual Keller pair, `J_{(x,y)}=j=u D` with `j in C^*`, so `D=j/u` is independent of `z` and `deg_z D≤m-2` holds. The remaining system is `r1'=⋯=r7'=0`, `9 r8'=j/u`, on the whole cell, not on a selected Q8 component.

The target's attribution of “order-three covariance” to the Faber theorem is slightly loose: the charged Faber parent states the tail *definition*, the terminal row, and the `h_j` filter, not a numbered theorem `wt(r_l)=12+l`. The derivation above is one paragraph from those ingredients plus the preflight Galois action, and it is given in the target's “Direct universal derivation” section. Non-blocking.

---

## Attack 2 — the identities `T=r8^3`, `T'=(j/3)h R^2`, and `(1.1)`

**CONFIRMED.** Starting from `9 r8'=j/u`, `r8=u^2 R`, `u^3=h`, `j in C^*`:

```text
T := r8^3 = u^6 R^3 = h^2 R^3 in K=C(x).
```

Character: `sigma(T)=zeta^6 T=T`, so invariance is equivalent. Differentiation in `L`, using `r8'=j/(9u)`:

```text
T' = 3 r8^2 r8' = 3 r8^2 · j/(9u) = (j/3) r8^2 / u.
```

Then `r8^2/u = u^4 R^2 / u = u^3 R^2 = h R^2`, hence `T'=(j/3) h R^2`. Squaring and cubing:

```text
T^2 = h^4 R^6,
(T')^3 = (j/3)^3 h^3 R^6 = (j^3/27) h^3 R^6,
T^2/(T')^3 = (27/j^3) h,
```

which is `(1.1)`. The same calculation in the descended coordinates `9 h R'+6 h' R=j` (the chain-rule form of the terminal row) gives `T=h^2 R^3` and `T'=h R^2 (2 h' R + 3 h R')=(j/3) h R^2`, so the identity does not depend on computing the derivative in `L` versus `K`.

**Zero.** `r8≡0` would give `9 r8'=0=j/u`, contradicting `j in C^*` and `u≠0`. Thus `T≢0`. This is strictly stronger than the selected erratum's `Z≠0`: the ninth-power form is satisfied by `Z=0`, while `(1.1)` is undefined at `T=0`. The zero-solution defect is absent without a Q8 contact or a `nu≠0` load, as claimed.

**Constant.** If `T` were constant then `T'=0`, so `h R^2=0`. Noncube forces `h≠0` (`0=0^3`). `R=0` is `r8=0`, already excluded. Characteristic zero and `T` nonconstant also give `T'≠0` directly. So `(1.1)` is a genuine identity of rational functions, not `0/0`.

**Ramified.** `R=r8/u^2` is Galois-invariant, hence lies in `K` as a rational function even at places where `v(h)` is not divisible by 3. `T=h^2 R^3` is an element of `K` before any local uniformizer is chosen. Differentiation of `T in C(x)` is ordinary rational differentiation; ramification of `L/K` does not create extra zeros or poles of `T` beyond those of `h` and `R`.

**Scalar.** The constant `j^3/27` is exact for this `T=r8^3`. The selected formula `C^3=j^9/(3^9 nu^{10})` is the same identity after the rescaling `S=r8^9=nu^{10} T_{\mathrm{sel}}^3`, which forces `T_{\mathrm{direct}}=c\,T_{\mathrm{sel}}` and changes only the leading scalar. Divisors, polynomiality, infinity, and passport are invariant under `T↦c T`. Setting `nu=1` in the selected formula recovers `C=j^3/27` on the nose. No `nu` is required, so the identity survives the `nu=0` components of the order-three cell, which the selected-Q8 statement does not cover.

The ninth-power rewrite `h^3 (S')^9=j^9 S^8` with `S=T^3` is equivalent after taking cube roots of constants in `C`, and is strictly weaker as a derivation: it requires the valuation-theoretic divisor cube. The direct cube is correctly described as stronger.

---

## Attack 3 — Wronskian polynomiality, and Q8/nu/parity/contact contamination

**CONFIRMED.** Re-derived from `(1.1)` and reduced `T=A/B`, `gcd(A,B)=1`, `W=A'B-AB'`, `C=j^3/27≠0`. Then `T'=W/B^2` and

```text
h = C A^2 B^4 / W^3.
```

Characteristic zero and coprimality:

- At an `A`-root of multiplicity `alpha≥1`, `B` is a unit, `ord(A'B)=alpha-1` exactly, `ord(AB')≥alpha`, so `ord(W)=alpha-1` and `ord(h)=2alpha-3(alpha-1)=3-alpha`.
- At a `B`-root of multiplicity `beta≥1`, symmetrically `ord(W)=beta-1` and `ord(h)=4beta-3(beta-1)=beta+3≥4`.
- Off `supp(A B)`, `ord(h)=-3 ord(W)`, so a finite zero of `W` is a pole of `h` of order a positive multiple of three.

`W` is a polynomial. A rational function regular on all of `A^1` is a polynomial. Therefore `h in C[x]` if and only if every finite zero of `W` lies in `supp(A B)` and every `alpha_i≤3`. There is no finite restriction on the `beta_j`. Under those conditions the displayed orders are exhaustive and

```text
W = c · product_i (x-a_i)^{alpha_i-1} · product_j (x-b_j)^{beta_j-1}.
```

Cube class: `(T')^{-3}` is a cube and `C in C^*` is a cube over `C`, so `[h]=[T^2]` in `C(x)^*/C(x)^{*3}`, trivial if and only if `T` is a cube. This is the selected `(3.3)`–`(3.5)` with the constant specialized to `j^3/27`.

**Contamination audit of the selected classifier after the terminal identity.** Read in full:

| Selected step | Inputs actually used | Q8 / `nu` / component / parity / contact |
|---|---|---|
| §2 divisor cube `Z=T^3` | ninth-power `(1.1)`, char 0, `C` alg closed, `Z≠0` | none after the scalar equation; `nu^{10}` is a constant |
| §2 cancellation to `h=C T^2/(T')^3` | `Z'=3 T^2 T'`, cube roots of constants in `C` | `nu` only inside `C` |
| §3 Wronskian orders | reduced `T=A/B`, char 0, coprimality | none |
| §4.1 unequal degrees | leading coefficient `(a-b)A0 B0`, `3\|deg h`, noncube | none |
| §4.2 balanced passport | `lambda=T(∞)`, `e=ord_∞(T-lambda)`, `d/dx=-s^2 d/ds` | none |
| §4.6 Riemann–Hurwitz | listed ramification units, char 0 | none |
| §5 residual list | Q8 quotient, scale `p`, Taylor, boundaries | charged as *remaining* work, not used |

No step of §§2–4 names a Q8 coordinate, a contact index, an even/odd parity involution, a selected coefficient component, or a value of `k,mu,nu` other than the constant `nu^{10}` in the scalar `C`. The target does not even import §2: it supplies `T=r8^3 in C(x)` directly and consumes only the Wronskian/infinity/passport argument. The selected positive-genus, infinity-contact, and eight-contact documents are not parents and are not used.

---

## Attack 4 — `h in C[x]`, `3|deg h`, noncube, unequal strata, passport, RH

**CONFIRMED**, licensed on every actual nontrivial-Kummer residual `(9,12)` trajectory.

**`h in C[x]`.** Preflight: after harmless target scalings, `a_9=h^3`, `b_12=h^4` with `a_9,b_12 in C[x]`. `C[x]` is integrally closed in `C(x)`, so `h^3 in C[x]` forces `h in C[x]`. This is the leading UFD of every actual polynomial pair of type `(9,12)`, not a selected-component construction.

**`3|deg h`.** Residual history criterion `gcd(H,3)=3`, equivalently `3|H`, including `H=0`. Every actual trajectory that remains on the `(9,12)` cell after the reviewed shear/UFD history lies in this class. The pair-level `H=0`, all-`x`-degrees-`≤1` corner closed by GGV is the trivial Kummer class and is already excluded by noncube.

**Noncube.** This *is* the nontrivial order-three class: preflight orders `{3,1}`, with `e=1` the polynomial core `h=c q^3`. The target's “nontrivial order-three Kummer branch” is exactly `h` not a cube in `C(x)`. Over `C`, Gauss/UFD makes this equivalent to `h` not a cube in `C[x]`.

**Unequal degrees empty.** If `deg A≠deg B`, the Wronskian leading coefficient `(a-b)A0 B0≠0`, so `deg W=a+b-1`. Comparison with `deg W=a+b-r-s` gives `r+s=1`: one of `A,B` is constant and the other is `c(x-c0)^D`.

- `a>b`: `B` constant, `D≤3`, `deg h=3-D`. Then `3|deg h` leaves only `D=3`, for which `h` is a nonzero constant, hence a cube over `C`.
- `b>a`: `A` constant, `deg h=D+3` with no upper bound on `D`. Then `3|deg h` forces `3|D`, so the unique multiplicity `D+3` is `0 mod 3` and `h` is a cube.

Both strata are nonempty for the bare identity `(1.1)` without the two Kummer hypotheses (the selected control tables exhibit exactly those failure modes) and are empty on the actual residual nontrivial branch. Hence `deg A=deg B=D`.

**Balanced passport.** `lambda=T(∞)=A0/B0 in C^*` (neither `0` nor `∞`). Set `G=A-lambda B≠0`, `e=D-deg G`, so `1≤e≤D`. Then `W=G'B-G B'` has leading coefficient `-e G0 B0≠0` and `deg W=2D-e-1`. Comparison with `(3.4)` gives `r+s=e+1`. Local orders give the same degree independently:

```text
deg h = sum_i (3-alpha_i) + sum_j (beta_j+3) = 3r - D + D + 3s = 3(r+s)=3(e+1).
```

Ramification data of `T:P^1_x→P^1_T`:

```text
over 0:         (alpha_1,…,alpha_r),  alpha_i≤3,  sum = D,
over ∞:         (beta_1,…,beta_s),                 sum = D,
over lambda:    (e, 1^(D-e)).
```

Finite critical points off `{0,∞}` are finite zeros of `W` off `supp(A B)`, forbidden by polynomiality. In particular every finite `lambda`-preimage is simple. After scaling `lambda` to `1` by `z↦z/lambda` (a Möbius transformation fixing `0` and `∞`, which changes the constant in `(1.1)` but not the passport), this is a three-value Belyi map.

**Riemann–Hurwitz saturates:**

```text
sum (alpha_i-1) + sum (beta_j-1) + (e-1)
  = (D-r)+(D-s)+(e-1)
  = 2D - (e+1) + e - 1
  = 2D-2.
```

In characteristic zero this is the entire ramification total of a degree-`D` map `P^1→P^1`. No unlisted branch value can carry ramification. The three values `0,lambda,∞` are distinct because `lambda in C^*`.

**Cyclic controls remain positive.** For `e=1` one has `r=s=1` and `T=C((x-a0)/(x-b0))^D` with `D≤3`. Multiplicities `(2,4)` and `(1,5)` at `D=1,2` are noncube of degree 6; `D=3` is a cube. These are exact rational solutions of `(1.1)` at the charged Kummer scope, so the classification excludes no trajectory.

---

## Attack 5 — earlier branch-wide promotion versus duplicate algebra

**CONFIRMED as a new composition/scope theorem; the divisor algebra is duplicate.**

Repository search for `whole-order-three`, `branch-wide`, `entire nontrivial`, `T=r8^3`, and `terminal Belyi` across `xmodel/`, `AUDIT.md`, `notes.md`, and `APPROACHES.md` produced exactly three documents that state a *branch-wide* reuse of the selected passport:

- the target under review;
- the same-day AS scope audit, charged as context not evidence;
- this review's launch prompt.

The selected classifier and its Claude review, the erratum, and `AUDIT.md`'s “MAX12 SELECTED-`Q8` TERMINAL BELYI CLASSIFICATION” entry all remain at `k=mu=0`, `nu≠0`, `Z≠0` selected-Q8 scope. Leaf-4 Claim 5 (CONFIRMED) is the ninth-power identity `h^3(S')^9=j^9 S^8` from `9 r8'=j/u`, `r8=u^2 R`, `u^3=h`; that is the same algebra as the target's `(1.1)` after `S=T^3`, but it is scoped as a formal-local Q8-contact identity and does not run Sections 3–4 of the Belyi classifier. The FT2/Faber deduplication note records that rewriting the terminal row through `R=w^3` is not a new high row, and asks for a lower-fibre classification as the first fibre-level successor; it does not itself promote a branch-wide Belyi theorem.

Distinction, stated exactly:

- **Duplicate algebra:** Wronskian orders, polynomiality criterion, unequal-degree killing by `3|deg h` plus noncube, balanced passport, `r+s=e+1`, `deg h=3(e+1)`, Riemann–Hurwitz saturation. All of this is the selected classifier §§3–4, independently CONFIRMED by Claude, and re-derived here without change.
- **New composition/scope:** the terminal identity `(1.1)` with constant `j^3/27` is obtained from universal Faber plus Kummer covariance on the *entire* nontrivial order-three `(9,12)` cell, including components with `k≠0` or `nu=0`, without Q8 coordinates. That is the first statement in the repository that the selected passport is a necessary target on every actual order-three trajectory.

The AS cross-check reaches the same scope theorem by the ninth-power path (`S=r8^9`, then the selected divisor cube). It is same-model and was not used as evidence. Agreement is recorded: both documents refuse a fibre classification, a realization, and an exclusion. The target's direct cube is the cleaner of the two derivations and does not need to set `nu=1` formally in the selected formula.

The phrase “first nonduplicate consequence of the FT2/Faber audit” is campaign language for this scope lemma. It does not classify a coefficient fibre and does not contradict the deduplication note's demand that a fibre-level successor still be done.

---

## Attack 6 — firewall

**CONFIRMED; nothing listed below is claimed.**

| Charged unclaim | Where the target keeps it open |
|---|---|
| Cyclic `D=1,2` terminal controls | Stated as exact noncube positive controls; “the theorem by itself excludes no trajectory” |
| Lower `(k,mu,nu)` fibre | Residual item 1: still must realize `r1=r2=r4=r5=r7=0`, `r3=mu`, `r6=nu` with Faber constant `k` |
| Original terminal converse | Residual item 2: `(1.1)` is necessary, not a reconstruction of `9 r8'=j/u`; cube roots of `T` in `L` are three-valued |
| Both Taylor families | Residual item 3; preflight/Faber keep `(1.1)` of the Faber parent charged |
| Removed finite/projective boundaries and coprimality | Residual item 4 |
| Order-one `(9,12)` leaf | Firewall: the `e=1` polynomial core, where `h` is a cube and unequal strata need not die |
| Either `(8,12)` Kummer leaf | Firewall: different cell, `m=8`, terminal unknown `r7`, weights mod 4 or 2 |
| Maximum twelve | Firewall: no coverage or automorphy statement |
| JC2, counterexample, emptiness, realization | Firewall: “proves no passport is realized, no passport is impossible, no Taylor family is polynomial, no trajectory exists or is excluded, no maximum-12 theorem, no counterexample, and no JC2 result” |

Formal coefficient-fibre points are excluded by the opening quantification “actual … Keller trajectory”: the row `9 r8'=j/u` is a differential equation along a trajectory, not an algebraic equation of the fibre. Positive characteristic is excluded by the opening “characteristic-zero”. No computation is claimed, and none was run here.

---

## Promotable sentence

On every actual characteristic-zero `(9,12)` partial-`y` Keller trajectory in the nontrivial order-three Kummer class — `u^3=h in C[x]`, `h` not a cube in `C(x)`, `3|deg h`, `j in C^*` — the reviewed universal Faber terminal row and the order-three tail character give `9 r8'=j/u` and `sigma(r8)=zeta^2 r8`, hence `r8=u^2 R` with `R in C(x)` and `T:=r8^3=h^2 R^3` a nonconstant element of `C(x)` satisfying `h=(j^3/27) T^2/(T')^3=(j^3/27) A^2 B^4/W^3` for reduced `T=A/B` and `W=A'B-AB'`; polynomiality of `h` is equivalent to every finite zero of `W` lying in `supp(A B)` with every `A`-root of multiplicity at most three; the same two Kummer hypotheses empty both unequal-degree strata and force `deg A=deg B=D`, so after scaling `lambda=T(∞)` to one, `T` is a three-value Belyi map of passport `(alpha_i≤3)` over `0`, `(beta_j)` over `∞`, `(e,1^(D-e))` over `1`, with `r+s=e+1`, `deg h=3(e+1)`, saturating Riemann–Hurwitz `2D-2`. This is a necessary classification only. The cyclic rows `D=1,2` remain exact noncube terminal positive controls, and the theorem excludes no trajectory.

---

## Residual obligations

An actual trajectory with a balanced passport must still, independently of this classification:

1. realize the complete lower Faber fibre `r1=r2=r4=r5=r7=0`, `r3=mu`, `r6=nu` with its constant `k`;
2. satisfy the original terminal row `9 r8'=j/u`, not only the Belyi consequence `(1.1)`;
3. reconstruct every coefficient function and both complete Taylor polynomiality families at the true center `r=A/9`;
4. retain coprimality of `A,B` and every finite/projective boundary removed by gauges or charts.

The next honest gate is a passport-versus-Taylor realization test on the full order-three lower fibre, split by `(k,mu,nu)`. The selected-Q8 positive-genus theorem remains one component only.

---

## Non-blocking remarks

None of the following changes the verdict.

1. The integer grading `wt(r_l)=12+l` is the standard geometric convention (matching the leaf-4 and global-quotient ledgers) but is not a numbered Faber theorem. Only the character `2` is used, and that character is a one-line consequence of the charged tail definition, the `h_j` filter, and `sigma(z)=zeta z`.
2. Over `C` the preflight monic-core precision is automatic: every constant is a cube, so class order equals divisor order and the constant field of `L` is `C`. The target's omission of the word “monic” does not open the preflight's `h=2x^4` failure shape, which required a non-algebraically-closed constant field.
3. The erratum parent is the confirmed scope of the *imported* selected classification (`Z≠0` on the ninth-power form). The direct-cube identity never admits `T=0`. Listing the erratum is honest provenance, not a load-bearing step.
4. Scaling `lambda` to one changes the constant in `(1.1)` from `j^3/27` to `(j^3/27)/lambda`. The passport claim is after that scaling; the identity `(1.1)` is for the unscaled `T=r8^3`.
5. `h≠0` is used and follows from noncube. `1≤e≤D` uses `A-lambda B≠0`, i.e. `T` nonconstant, already forced.
6. Same-model caveat: the charged Faber review is Grok 4.6. Covariance and `(1.1)` were re-derived here from the producer bytes and the Claude preflight, not from that review.

---

## Quarantine

No result here proves or disproves JC2, constructs or excludes a characteristic-zero Keller pair of type `(9,12)`, realizes or forbids a passport, classifies a `(k,mu,nu)` fibre, polynomializes a Taylor jet, empties the order-one or `(8,12)` leaves, or yields a maximum-twelve theorem. The cyclic `D=1,2` rows are terminal-identity controls, not constructed trajectories. The AS scope audit was not used as evidence.

CONFIRMED
