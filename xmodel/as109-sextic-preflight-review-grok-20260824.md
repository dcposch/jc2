# Hostile different-model review — AS109 SEXTIC FRONTIER PREFLIGHT

| Field | Value |
|---|---|
| Claim under review | Characteristic-zero preflight: after target `GL_2` and divisible-degree shears, the only new actual `y`-degree pairs with maximum degree six are the imprimitive `(4,6)` split and the coprime `(5,6)` Pfaffian; neither is closed here; no `y`-degree-`<=6` theorem, no raised AS109 floor, no lift, no JC2 inference |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking precisions: algebraic closure is used to write `H=h^2` on the `(4,6)` nonzero-`kappa` branch; a polynomial primitive of `omega` modulo `dI_3` exists and is recorded below as successor input, not as a producer theorem) |
| Evidence tier | independent exact expansion over a generic characteristic-zero coefficient ring (hand Jacobian by `y`-degree for the pair sweep and the `(4,6)` `[y^8]` row, Wronskian / logarithmic derivative in `K(x)`, UFD valuations in `K[x]` and `Kbar[x]`, chain-rule Jacobian of the depressed `(5,6)` form, direct differentiation of `I_3,I_2`, exterior derivative of `omega`); a second sparse engine over `Q` with `Fraction` coefficients that does not import the producer replay; unmodified rerun of `verify_sextic_preflight.py` as regression control; confirmed quartic theorem consumed only as scoped input for pairs with both `y`-degrees `<=4`; quintic work recorded as independently landed and **not consumed** |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T10:53:00Z – 2026-08-24T11:07:35Z |
| Python | 3.14.6; stdlib only (`fractions.Fraction`, integer dicts) |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-sextic-frontier-preflight-20260824.md` (SHA-256 `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4`)
- `cases/as109_sextic_frontier_preflight_20260824/verify_sextic_preflight.py` (SHA-256 `21bc494f552587ee0b64c01c735b2f1243eafce9599f1e05bc526d23e38f73ad`)
- `cases/as109_sextic_frontier_preflight_20260824/FREEZE.sha256` (SHA-256 `2890f3dd5d09b45e4f047cbb509b42430c3c9a677412cccef0b18fd66b44c4ab`)
- quartic producer `xmodel/as109-quartic-discriminator-gate-20260824.md` (SHA-256 `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276`) and its different-model review `xmodel/as109-quartic-review-grok-20260824.md` (SHA-256 `3f9e763c07aa019a766b267774f92df857aadd94750cb8c3c9431671318d930e`); landed `CONFIRMED`; consumed only for pairs whose two `y`-degrees are at most four
- quintic producer `xmodel/quintic-y-frontier-preflight-independent-20260824.md` (SHA-256 `598cdf3799d4abf40ec761f1fd2b0a5a6457ee2b578371bd864c296259d2a978`) and, landed during this window, `xmodel/quintic-y-review-grok-20260824.md` (SHA-256 `ab5ce55c1d71628e16800bc9ff9985da9f4ae90fe521849fa2060e97ff552e0e`); overall `CONFIRMED` on the quintic lane; **not consumed** by this preflight or by this review
- Hensel context only: `xmodel/as109-support-gate-20260824.md` (SHA-256 `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5`) and `xmodel/as109-support-review-grok-20260824.md` (SHA-256 `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8`); no new Hensel inference

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No enumerator was written or run. The `(4,6)` lower rows and a monic `(5,6)` eliminant were not pursued. No AWS call was made.

Write `K` for an arbitrary characteristic-zero field, `Kbar` for an algebraic closure, `J(f,g)=f_x g_y-f_y g_x`, and `p=109`. Actual `y`-degrees are used throughout.

---

## Promotion

**Accept `SEXTIC-Y-PREFLIGHT-SURVIVING-PFAFFIAN-GATE` at the stated scope.**

- After constant target operations and divisible-degree shears, the only new actual pairs with maximum `y`-degree six are `(4,6)` and `(5,6)`. Both remain. Neither branch of `(4,6)` is empty. The coprime pair `(5,6)` reduces to the displayed Pfaffian (7.4) and does not presently yield a monic eliminant or a polynomiality theorem.
- The confirmed quartic conclusion is unchanged: an exact AS109 lift must have correction `y`-degree at least five in one coordinate. This file does **not** raise that floor to six or seven.

**Do not promote this to:** a `y`-degree-`<=6` field theorem; a strengthened AS109 exclusion; nonexistence or existence of an arbitrary finite-support AS109 lift; a found lift; a characteristic-zero point; a JC2 counterexample or disproof; `HEIGHT-CERT`; cap widening; an exponent rectangle; a finite Witt-level inference; or a novelty / priority claim.

**Do not consume the independently landed quintic theorem here.** Even if a later coordinator consumes that `CONFIRMED` quintic review, the two sextic patterns below still block a degree-`<=6` theorem. Divisible shears `(1,6),(2,6),(3,6)` would then reduce into the quintic range, but that reduction is not used in this preflight and is not used in this review.

**Smallest valid successors.**

- `(4,6)`: a lower-row compiler for both branches of (3.4) — the `kappa=0` common quadratic generator, without treating top-coefficient compatibility as a full normal form, and the `kappa!=0` constant depression mismatch `lambda/12`, which is not target-sheared away.
- `(5,6)`: start from the polynomial primitive `I_1` recorded in the successor-input section below (`dI_1=omega-(2A/5)\,dI_3`), together with a weighted-projective pole analysis of the remaining `h\,eta(X')=jbar` equation and both polynomial boundary identities (8.1). Do not search blindly for an ambient integrating factor of `omega`. Do not treat the rational trajectory (8.3) as a Keller pair.

---

## Quarantine

No result here proves or disproves JC2. Producer JSON strings `SEXTIC-Y-PREFLIGHT-SURVIVING-PFAFFIAN-GATE` and `ODE-ALONE-DOES-NOT-CLOSE` were not used as evidence; the identities below were re-derived. The quartic parent is recorded as landed `CONFIRMED` and is consumed only in its stated `y`-degree-`<=4` scope. The quintic parent/review are recorded as independently `CONFIRMED` and are **not** used to close any sextic pair, to raise the AS109 floor, or to infer that divisible sextic shears are automorphisms. Finite-support search, Hensel, and Witt data are unused. Priority is quarantined from the mathematical verdict.

The rational path (8.3) is a negative control: it solves the Pfaffian ODE with a nonzero last row and fails the second polynomial boundary. It is not a lift and is not evidence that a lift exists.

---

## Scope (not enlarged)

One prime `p=109`, one seed `(x-x^{109},y)`, and a characteristic-zero field calculation over `K` (temporarily over `Kbar`). The object of the file is a preflight classification and an exact `(5,6)` normal form, not a theorem that every sextic-`y` Keller pair is an automorphism. Arbitrary finite `x`-degree is in scope *inside* the displayed identities. Target `GL_2`, translations, and polynomial target shears are automorphy tests over `K` (or `Kbar`); they need not preserve the integral AS109 seed chart. Quintic identities, generic exponent search, exponent rectangles, finite-Witt inference, and AWS are out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | For actual degrees `m<=n=6`, equal-degree `GL_2` kills `(6,6)`; divisible-degree shears kill `(1,6),(2,6),(3,6)`; the `m=0` branch is triangular and incompatible with actual degree six; both `(4,6)` and `(5,6)` genuinely remain. No quintic theorem is used | **CONFIRMED** | a leftover `y^{11}` term from lower coefficients; `2=0` or `3=0`; kernel of `d/dx` on `K(x)` larger than `K`; `n/m` integral for `(4,6)`; a missed actual pattern; a silent appeal to emptiness of `(2,5),(3,5)`, or `(4,5)` |
| 2 | In genuine `(4,6)`, after constant scaling one has `a_4=H^2`, `b_6=H^3`. The next row is `[y^8]J=H(2H N'-5 N H')` with `N=3 a_3 H-2 b_5`. This implies `(N^2/H^5)'=0` and `N^2=kappa H^5`, including `N=0`, `H` constant, and UFD valuations | **CONFIRMED** | a missed `y^8` summand from `(4,5)` or `(3,6)`; sign error in `N`; hidden division by `H` at a zero of `H`; `2 v(N)=5 v(H)` failing to force even `v(H)` when `kappa!=0`; `ker(d/dx)` larger than constants |
| 3 | `kappa=0` gives the top coefficients of a common quadratic generator `z=H y^2+r y+s` without a lower-row normal form. `kappa!=0` gives `H=h^2`, `N=lambda h^5` over `Kbar` and a constant depression mismatch `lambda/12` that allowable target operations do not remove. Neither branch is claimed empty | **CONFIRMED** | `N=0` failing to match `a_3=2 H r`, `b_5=3 H^2 r`; a polynomial target shear killing the degree-five coefficient of `g`; a claimed emptiness of either branch |
| 4 | Genuine `(5,6)` has `a_5=h^5`, `b_6=h^6` after scaling; the depression invariant `6 a_4/h^4-5 b_5/h^5` shifts by `-5 lambda` under `g\to g+lambda f` and can be aligned. `J_(x,y)=h J_(x,z)`. All nine rows (5.1) and the five integrals (5.2) are exact, including every integration constant and the translations that kill `delta,epsilon` but not `alpha,beta,gamma` | **CONFIRMED** | chain-rule factor not equal to `h`; a leftover `z^9` or missing summand in (5.1); a non-integrated residue in `E8`–`E4`; translating `f` failing to absorb `delta`; a hidden division by `h` in (5.2) |
| 5 | After (5.2), `E3=I_3'` and `E2=I_2'`. Every coefficient of `omega` and `eta` matches (7.2)–(7.3). At `A=B=C=0`, `D=1` and zero constants, `det(dI_3,dI_2,omega,eta)=(6/5)^4`. The displayed exterior component is nonzero, so `omega` is not exact by the immediate quartic mechanism. Absence of a rational first integral on the level surface is not claimed | **CONFIRMED** | a leftover non-integrated `z^3` or `z^2` residue; a sign error in `omega` or `eta`; vanishing of (7.6); rank dropping at the control point; a claim that no first integral exists on `I_2,I_3` level sets |
| 6 | The two `y=0` identities (8.1) plus `I_3,I_2` are four algebraic equations for five initially rational quantities; the raw row `omega(X')=0` is not a total derivative, so no monic eliminant is produced. The path `A=B=C=0`, `D=x^{-5}`, `h=x^{11}`, `r=-x^{-1}` solves the Pfaffian with `h eta=-6`, makes `f(x,0)=0`, and leaves `g(x,0)=-x^{-6}/5`. It is a negative control, not a Keller pair | **CONFIRMED** | a fifth algebraic relation derived as a raw total derivative of `omega`; the trajectory failing `I_2'=I_3'=omega=0` or `h eta=-6`; `g(x,0)` becoming polynomial; the path being promoted to a lift |
| 7 | Frozen hashes match; the unmodified replay returns the expected scoped flags; exact tame shears and the `(5,6)` rejection hold; the outcome is a survivor only | **CONFIRMED** | hash mismatch against the freeze; `full_sextic_theorem_proved=true`; an enumeration or AWS call; a raised AS109 floor; a JC2 inference |

All remarks below are non-blocking unless marked otherwise. None changes a coefficient or a numbered verdict. The polynomial primitive `I_1` of Section “Successor input” answers the producer’s own next-gate question; it does not close `(5,6)` and does not flip claim 5 or 6.

---

## Replay and hashes

Frozen producer hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-sextic-frontier-preflight-20260824.md` | `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4` | prompt and `FREEZE.sha256` |
| `cases/as109_sextic_frontier_preflight_20260824/verify_sextic_preflight.py` | `21bc494f552587ee0b64c01c735b2f1243eafce9599f1e05bc526d23e38f73ad` | prompt and `FREEZE.sha256` |
| `cases/as109_sextic_frontier_preflight_20260824/FREEZE.sha256` | `2890f3dd5d09b45e4f047cbb509b42430c3c9a677412cccef0b18fd66b44c4ab` | prompt |
| `xmodel/as109-quartic-discriminator-gate-20260824.md` | `8c8e3151ce63e4e43d8c91c56a3b801e2bb0e0fcbb9b16dc459dc8eccf7b0276` | producer provenance table; confirmed theorem consumed |
| `xmodel/as109-quartic-review-grok-20260824.md` | `3f9e763c07aa019a766b267774f92df857aadd94750cb8c3c9431671318d930e` | producer provenance table; landed `CONFIRMED` |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | producer provenance table; context only |
| `xmodel/as109-support-review-grok-20260824.md` | `1448985c259d2adb9b7e982fee233e802100fa8a0fd2eb32822b617e0a4632e8` | producer provenance table; context only |
| `xmodel/quintic-y-frontier-preflight-independent-20260824.md` | `598cdf3799d4abf40ec761f1fd2b0a5a6457ee2b578371bd864c296259d2a978` | independent pending-or-landed status only |
| `xmodel/quintic-y-review-grok-20260824.md` | `ab5ce55c1d71628e16800bc9ff9985da9f4ae90fe521849fa2060e97ff552e0e` | landed `CONFIRMED` during this window; **not consumed** |

The case directory contains only `FREEZE.sha256` and `verify_sextic_preflight.py`. Registered command, rerun unmodified:

```sh
python3 cases/as109_sextic_frontier_preflight_20260824/verify_sextic_preflight.py
```

Exit code 0. Top-level fields:

```text
verdict = SEXTIC-Y-PREFLIGHT-SURVIVING-PFAFFIAN-GATE
full_sextic_theorem_proved = false
enumeration_run = false
lift_found = false
jc2_inference = false
field_characteristic = 0
```

The replay is a finite exact regression control (formal differential algebra on named coefficients, plus integer bivariate Jacobians). The coefficient derivations below are the proofs for arbitrary `x`-degree.

A second sparse engine, written for this review over `Q` with `Fraction` coefficients and not importing the producer, checked: the complete `n=6` pair partition; the `(4,6)` identities `da_4=2H\,dH`, `db_6=3H^2\,dH`, vanishing of `[y^9]J` on `a_4=H^2,b_6=H^3`, and the factorization `[y^8]J=H(2H N'-5 N H')`; the cross-multiplied numerator of `(N^2/H^5)'`; the `kappa=0` identities `a_3=2Hr`, `b_5=3H^2 r`; the mismatch identity `12 h^5(r_f-r_g)=N`; the `(5,6)` vanishing of `[y^{10}]J` on `a_5=h^5,b_6=h^6`, the `[y^9]` factorization, and the exact numerator shift `-5 lambda h^5`; all nine depressed rows (5.1) by expanding `F_x G_z-F_z G_x` in `z`; vanishing of `E8`–`E4` after (5.2), including an independent check that the displayed `T` satisfies the integrated `E4` identity; `E3=dI_3` and `E2=dI_2`; all eight coefficients of `omega,eta`; the exterior component (7.6) and the other five `d omega` components; the rank matrix `diag(6/5)` and determinant `(6/5)^4`; the Laurent trajectory `h eta=-6`, `f(x,0)=0`, `g(x,0)=-x^{-6}/5`; the three divisible shears and the rejection `J(x+y^5,y+y^6)=1+6y^5`; a concrete chain-rule sample `J(x^5 y^5+x,\,x^6 y^6+(6/5)x^2 y)=(6/5)x^2=h\cdot(6x/5)`; a sparse `(4,6)` numerical `[y^8]` sample `H=x,a_3=x^2,b_5=x` matching `3x^4+6x^2`; and the `kappa=0` sample with vanishing `[y^8]`. After correcting two expected-value bugs in the tester (the `m=0` Jacobian is `1+6y^5`, not `6y^5`; the chain-rule sample includes the factor `h`), every identity held.

Hostile extras, not claimed by the producer and not used to flip a verdict: `d omega` has nonzero ambient components `(A,B)`, `(A,C)`, `(A,D)` and vanishing `(B,C)`, `(B,D)`, `(C,D)`; the 4-form `d omega\wedge dI_2\wedge dI_3` is identically zero, so `omega` is closed on every `I_2,I_3` level surface; a polynomial `I_1` of weight nine satisfies `dI_1=omega-(2A/5)\,dI_3` identically (successor input below). Gradients of `(I_1,I_2,I_3)` have rank three at a generic test point; the control-point determinant with `eta` remains `(6/5)^4`, so there is no fourth independent first integral.

---

## Claim 1 — exhaustive max-`y`-degree-six pair sweep

**CONFIRMED.**

Write actual degrees `m=deg_y f<=n=deg_y g`. The contribution of a pair of terms `(a_i y^i, b_j y^j)` to the coefficient of `y^{i+j-1}` in `J(f,g)` is `j a_i' b_j-i a_i b_j'`. Lower `y`-coefficients cannot produce a given top degree. For `n=6` the top identity is

```text
6 a_m' b_6 - m a_m b_6' = 0.                                 (1.1)
```

Characteristic zero gives `6\neq 0`. If `m=n=6`, this is a Wronskian: `(a_6/b_6)'=0` in `K(x)`, hence the ratio lies in `K` (kernel of `d/dx` on `K(x)` is `K`: write `r=p/q` in lowest terms in the Euclidean domain `K[x]`; `r'=0` forces `q` to divide `q'`, hence `q` constant in characteristic zero). Constant target `GL_2` kills one leading coefficient and drops to `m<6`, `n=6`.

If `m=0`, then `J=a_0' g_y`. A nonzero constant cannot have a `y^5` term, so `deg_y g=1`, contrary to actual degree six. Independently, `J(x,y+y^6)=1+6y^5`. No `(0,6)` Keller pair exists.

If `m>0` and `m` divides `6`, unique factorization of (1.1) gives `b_6=k a_m^{6/m}` with `k in K^*` after absorbing units of `K[x]`. The polynomial target shear `g\mapsto g-k f^{6/m}` preserves `J` up to the same constant and lowers `n`. The three cases are

```text
(1,6):  g \mapsto g-k f^6,
(2,6):  g \mapsto g-k f^3,
(3,6):  g \mapsto g-k f^2.
```

Exact tame controls: `J(x+y,y+(x+y)^6)=1`, `J(x+y^2,y+(x+y^2)^3)=1`, `J(x+y^3,y+(x+y^3)^2)=1`. These shears may land in degree `<=5`. The preflight does not claim that the reduced pairs are automorphisms, and it does not invoke a quintic theorem. The independently landed quintic review is recorded above and is not used.

The remaining pairs with `1<m<6` and `n=6` are exactly

```text
(4,6)  gcd=2, 6/4 not an integer,
(5,6)  gcd=1, 6/5 not an integer.
```

No other bucket exists: the seven pairs `(0,6),...,(6,6)` partition into triangular, three shears, equal-degree `GL_2`, one imprimitive survivor, and one coprime survivor. Swapping coordinates is constant `GL_2` and reduces to `m<=n`. A full `y`-degree-at-most-six theorem would still have to close both survivors (and, separately, the quintic range). This preflight claims neither closure.

---

## Claim 2 — `(4,6)` leading normalization and `N^2=kappa H^5`

**CONFIRMED.**

On a genuine `(4,6)` pair, (1.1) is `3 a_4' b_6=2 a_4 b_6'`, equivalently `(a_4^3/b_6^2)'=0`, so `a_4^3=c\,b_6^2` with `c in K^*`. For every prime of `K[x]`, `3 v(a_4)=2 v(b_6)`. Thus `v(a_4)` is even and `v(b_6)` is divisible by 3. Write `a_4=u H^2`, `b_6=w H^3` with `u,w in K^*` and `H in K[x]`, `H\neq 0`. Constant target scaling `f\mapsto mu f`, `g\mapsto nu g` with `mu nu in K^*` absorbs `u,w` and yields

```text
a_4=H^2,     b_6=H^3.                                       (2.1)
```

Algebraic closure is not required for (2.1). Directly, `a_4'=2H H'` and `b_6'=3H^2 H'`, so the top row vanishes identically.

The next degree is `y^8`. The only contributing pairs are `(4,5)` and `(3,6)`:

```text
[y^8]J = 5 a_4' b_5 - 4 a_4 b_5' + 6 a_3' b_6 - 3 a_3 b_6'.  (2.2)
```

(Pairs `(4,4)`, `(3,5)`, `(2,6)` produce `y^7`.) Substitute (2.1) and the definition `N=3 a_3 H-2 b_5`. Then `N'=3 a_3' H+3 a_3 H'-2 b_5'` and

```text
2H N'-5 N H'
  = 6 a_3' H^2 - 4 H b_5' - 9 a_3 H H' + 10 b_5 H',
H(2H N'-5 N H')
  = 6 a_3' H^3 - 4 H^2 b_5' - 9 a_3 H^2 H' + 10 H H' b_5,
```

which is exactly (2.2). The second engine checked this as an identity in the 1-jet ring of `(H,a_3,b_5)`, and on the sparse sample `H=x`, `a_3=x^2`, `b_5=x` obtained `[y^9]J=0` and `[y^8]J=3x^4+6x^2`, matching the closed form.

Since `K[x]` is a domain and `H\neq 0`, the vanishing of (2.2) gives `2H N'-5 N H'=0` as polynomials, with no localization at zeros of `H`. As rational functions,

```text
(N^2/H^5)' = N(2H N'-5 N H')/H^6.                           (2.3)
```

The right-hand side vanishes identically in `K(x)`. The kernel of `d/dx` on `K(x)` is `K`, so `N^2/H^5=kappa in K`, hence

```text
N^2 = kappa H^5                                             (2.4)
```

in `K[x]`. Zero cases:

- `H=0` is excluded by genuine `(4,6)`.
- `N=0` is the branch `kappa=0`. Then (2.4) holds, and (2.3) holds without dividing by `N`.
- If `H` is a nonzero constant then `N'=0`, so `N` is constant and `kappa=N^2/H^5` is a constant.

No hidden division remains in (2.4).

---

## Claim 3 — both `(4,6)` branches remain

**CONFIRMED.**

*Zero branch.* If `kappa=0` then `N=0`, so `b_5=(3/2) a_3 H`. Setting `r=a_3/(2H)` in `K(x)` gives the top coefficients of a common quadratic

```text
z = H y^2 + r y + s,     a_3=2 H r,     b_5=3 H^2 r.        (3.1)
```

Directly `3(2Hr)H-2(3H^2 r)=0`. The second engine checked this in the jet ring of `(H,r)`, and the sparse sample `H=x`, `r=x` had vanishing `[y^8]` and `[y^9]`. The quantity `r` is a priori rational; `s` is not constrained by the top two rows. The preflight does not derive a full even/odd residual normal form and does not claim this branch empty. That is the correct scope.

*Nonzero branch.* If `kappa\neq 0`, then `2 v_p(N)=5 v_p(H)` at every prime. Since `gcd(2,5)=1`, `v_p(H)` is even and `v_p(N)` is divisible by 5. Over `Kbar` one may absorb the unit of `H` into a square root and write `H=h^2`, `N=lambda h^5` with `h in Kbar[x]`, `lambda in Kbar^*`. (Over `K` one has only `H=u h^2` with `u in K^*`; passing to `Kbar` is a convenience for the displayed mismatch, not a closure of the branch.) Leading terms are then `h^4 y^4` and `h^6 y^6`. The two linear depression shifts are `r_f=a_3/(4 h^3)` and `r_g=b_5/(6 h^5)`, and

```text
12 h^5 (r_f-r_g) = 3 a_3 h^2 - 2 b_5 = N = lambda h^5,
```

so `r_f-r_g=lambda/12`. Independently: `a_3=0`, `b_5=-h^5/2` gives `N=h^5` and `r_f-r_g=1/12`.

Allowable target operations do not remove the mismatch. The addition `g\mapsto g+mu f` changes coefficients of `g` of `y`-degree at most `deg_y f=4`, so `[y^5]g=b_5` is invariant. Translations of `f` or `g` do not touch `a_3,b_5`. A further linear combination that mixed `g` into `f` would raise `deg_y f` to six. A shear `g-k f^{3/2}` is not polynomial. Unlike consecutive `(5,6)`, there is no target operation that aligns the two degree-five / degree-three shifts.

Neither branch is claimed empty. Equation (2.4) is a discriminator, not a closure theorem. Both statements match the calculation.

---

## Claim 4 — `(5,6)` leading form, nine rows, and (5.2)

**CONFIRMED.**

The top row is `[y^{10}]J=6 a_5' b_6-5 a_5 b_6'=0`, equivalently `(a_5^6/b_6^5)'=0`. Unique factorization and constant scaling give `a_5=h^5`, `b_6=h^6` with `h in K[x]`, `h\neq 0` (units of `K[x]` absorbed as in claim 2; algebraic closure is unnecessary here). The next row receives only `(5,5)` and `(4,6)`:

```text
[y^9]J = 5 a_5' b_5 - 5 a_5 b_5' + 6 a_4' b_6 - 4 a_4 b_6'.
```

With `N_56=6 a_4 h-5 b_5`, this equals `h^4(h N_56'-5 N_56 h')=h^{10}(6(a_4/h^4)'-5(b_5/h^5)')`. Hence

```text
6 a_4/h^4 - 5 b_5/h^5 = constant = 30(r_f-r_g),              (4.1)
```

where `r_f=a_4/(5 h^4)` and `r_g=b_5/(6 h^5)`. The target addition `g\mapsto g+lambda f` replaces `b_5` by `b_5+lambda h^5` and shifts the left-hand side of (4.1) by exactly `-5 lambda`. One may therefore align the two depressions and set `z=h y+r` with a common `r`. This is an identity in `Kbar(x)[y]`, not a polynomial source automorphism.

The depressed forms are (4.5) of the producer. Write `F,G` for those polynomials in the independent variables `(x,z)`. Then `z=hy+r` gives `f_y=F_z h`, `g_y=G_z h`, and the `z_x` terms in `f_x,g_x` cancel, so `J_(x,y)=h J_(x,z)`. Independently, `h=x`, `A=B=C=0`, `D=x`, `S=6x/5` produces `J=(6/5)x^2=h\cdot(6x/5)`. A second sample `A=x`, `B=C=D=0`, `h=1` produces `J=(36/125) x^3 y^2`, matching `I_2'=36 x^3/125` as the sole surviving `z^2` row.

Expanding `F_x G_z-F_z G_x` in `z` gives degrees `8` through `0` only (leading `1,1` contribute nothing after depression). Every coefficient matches (5.1), including the absence of `A` from `E1`, the absence of `P D'` from `E2`, and `E0=-C T'+S D'`. Substituting (5.2) makes `E8=E7=E6=E5=E4=0` identically. The displayed `T` was re-checked by integrating `E4=0`: `5 T'` equals the rest of `E4`, so the cubic and mixed terms `-4A^3/125`, `-2 alpha A^2/25`, `6AC/25`, `3B^2/25` are forced. Weights `(A,B,C,D,alpha,beta,gamma,delta,epsilon)=(2,3,4,5,2,3,4,5,6)` make `P,Q,R,S,T` homogeneous of weights `2,3,4,5,6`.

Integration constants: `alpha,beta,gamma,delta,epsilon in Kbar`. Target translation of `g` absorbs `epsilon` into `T`. Target translation of `f` shifts `D` and absorbs `delta` into the combination `6D/5+delta` (visible in `S`, in `I_3`, in `omega_C`, and in `eta_D`). The constants `alpha,beta,gamma` cannot be killed after depression: `g\mapsto g+lambda f` would reintroduce `z^5`. Retaining `delta,epsilon` is optional covariance, not a gap. Characteristic zero inverts `5`; for AS109 one works over `Q_{109}` with `109\neq 5`.

---

## Claim 5 — first integrals, `omega`/`eta`, rank, and exactness

**CONFIRMED.**

Direct differentiation of the displayed polynomials (6.1) and (6.2), after substituting (5.2), recovers `E3` and `E2` identically as `1`-forms in `(dA,dB,dC,dD)`. No division and no rank hypothesis enter. Thus every Keller path has `I_3=k_3` and `I_2=k_2` with constants in `Kbar`. Both polynomials are weighted-homogeneous (`I_3` of weight `7`, `I_2` of weight `8`). The constant `epsilon` is absent from both, as it is from `omega` and `eta`.

Collecting coefficients of `A',B',C',D'` in `E1` and `E0` after (5.2) recovers every summand of (7.2) and (7.3), including

```text
omega_C = -6AB/25 - 4 alpha B/5 + 3 beta A/5 + 6D/5 + delta,
eta_D   =  6AB/25 + 4 alpha B/5 + 3 beta A/5 + 6D/5 + delta.
```

At `A=B=C=0`, `D=1` and all integration constants zero, the four covectors are diagonal with diagonal `6/5`:

```text
dI_3=(6/5,0,0,0),  dI_2=(0,6/5,0,0),
omega=(0,0,6/5,0), eta=(0,0,0,6/5).
```

The determinant is `(6/5)^4\neq 0`. Generically the system (7.4) is therefore a rank-one algebraic foliation on a Zariski-open part of an `I_2,I_3` level surface, with `eta` fixing the parametrization. The last row of `J_(x,y)` is `h\,eta(X')`, so `jbar\neq 0` forces `eta(X')\neq 0` wherever `h` is finite and nonzero.

The displayed exterior component is

```text
partial_B(omega_A)-partial_A(omega_B)
  = 24 A^2/125 + 8 alpha A/25 - 12 C/25 - 4 gamma/5,         (5.1)
```

which is not the zero polynomial (already the `-12C/25` term). Independently, the remaining components of `d omega` are

```text
d omega_{AC} = 12B/25 + 6 beta/5,
d omega_{AD} = 12A/25 + 8 alpha/5,
d omega_{BC}=d omega_{BD}=d omega_{CD}=0.
```

So `omega` is not closed in ambient `(A,B,C,D)`-space, and is not the differential of a polynomial or rational function of `(A,B,C,D)` by the immediate quartic mechanism (a Jacobian row equal to `I'` before any restriction). That is exactly the distinction required: the calculation does **not** prove that no integrating factor or first integral exists on the `I_2,I_3` surfaces.

*Non-blocking successor input, not a flipped claim.* The 4-form `d omega\wedge dI_2\wedge dI_3` vanishes identically, so the restriction of `omega` to every level surface is closed. A polynomial primitive modulo `dI_3` exists and is recorded in the next section. The producer’s Section 7 already names “finding one, or proving none can support a rational Keller trajectory” as the next exact gate. The existence of `I_1` answers that question in the affirmative for a polynomial primitive; it does not make `omega` itself exact, does not produce a fourth independent integral (the control-point determinant with `eta` forbids that), and does not close `(5,6)`. The headline sentence that “no third polynomial first integral … follows from the present calculation” is therefore an overstatement of completeness, not a false closedness claim: the objects needed to write `I_1` are already on the page, but the preflight correctly refuses to treat the `(5,6)` pattern as empty.

---

## Successor input for `(5,6)` (not a producer claim)

On the full coefficient ring, including `alpha,beta,gamma,delta`, the weight-nine polynomial

```text
I_1 = 24 A^3 B/125 + 8 alpha A^2 B/25 + 4 beta A^3/25
      - 4 B^3/25 - 4 alpha B C/5 - 3 beta B^2/5
      - 18 A B C/25 - 3 beta A C/5 - 4 gamma A B/5
      - 6 A^2 D/25 - delta A^2/5
      + 6 C D/5 + 2 gamma D + delta C
```

satisfies the 1-form identity

```text
dI_1 = omega - (2A/5) dI_3.                                  (S.1)
```

Verified by matching all four components after substituting (5.2). Along any path with `I_3'=0` and `omega(X')=0` one has `I_1'=0`, so `I_1=k_1` is a polynomial first integral of the Pfaffian system (7.4). It is *not* an integral of the raw row `E1` in ambient space: `I_1'=E1-(2A/5)E3`. The gradients of `(I_1,I_2,I_3)` have rank three at the sample point `(A,B,C,D)=(1,2,3,4)`. On the rational trajectory of claim 6 one has `I_1\equiv 0`, so `I_1` does not kill that negative control.

A valid `(5,6)` successor should start from `(I_1,I_2,I_3)` and the remaining speed equation `h eta(X')=jbar`, together with both boundaries (8.1). It should not reopen an ambient integrating-factor search for `omega`. This review does not carry that successor out.

---

## Claim 6 — algebraic count, polynomiality gap, rational trajectory

**CONFIRMED.**

At `y=0` one has `z=r`, so

```text
f(x,0)=r^5+A r^3+B r^2+C r+D,
g(x,0)=r^6+P r^4+Q r^3+R r^2+S r+T,                          (6.1)
```

with `P,\ldots,T` determined by (5.2). The left-hand sides lie in `Kbar[x]` if `(f,g)` is a polynomial pair. Together with `I_3=k_3` and `I_2=k_2` these are four algebraic equations in `Kbar(x)` for the five initially rational quantities `r,A,B,C,D` (`h` is already in `Kbar[x]` by the UFD step). In the quartic gate the remaining Jacobian row was itself a total derivative and supplied a fifth algebraic equation, after which a monic eliminant for `r` existed. Here the remaining row is the non-closed ambient 1-form `omega`; it is not `I'` for an ambient polynomial `I`. No monic eliminant is produced in the file, and none is claimed.

(The successor object `I_1=k_1` would add a third integral in `(A,B,C,D)` and change the naive count to five algebraic equations for five rationals, plus the still-differential speed law `h eta=jbar`. That does not, by itself, exhibit a monic in `r`, and `I_1` vanishes on the negative control below. The producer’s “presently” is therefore still accurate as a statement about what the file derives. Constructing an eliminant from `I_1,I_2,I_3` and (6.1) is successor work and was not done here.)

Without polynomiality of `r,A,B,C,D`, poles may cancel against `h` in `h eta(X')=jbar`, so the polynomial-unit contradiction used at degrees three and four is unavailable. The three closure routes listed in producer Section 8 remain the right menu.

*Negative control.* With all integration constants zero, the rational path

```text
A=B=C=0,     D=x^{-5},     h=x^{11},     r=-x^{-1}            (6.2)
```

has `P=Q=R=T=0` and `S=(6/5)x^{-5}`. Then `I_3=I_2=0` identically on `A=B=C=0`, so `I_2'=I_3'=0`. Next `omega_D=0` on this line and `C'=0`, so `omega(X')=0`. Finally `eta_D=(6/5)D` and `D'=-5 x^{-6}`, hence

```text
eta(X') = (6/5) x^{-5} \cdot (-5 x^{-6}) = -6 x^{-11},
h eta(X') = -6.
```

The first boundary is `r^5+D=-x^{-5}+x^{-5}=0`, a polynomial. The second is

```text
r^6 + S r = x^{-6} + (6/5)x^{-5}(-x^{-1}) = -x^{-6}/5,
```

still with a pole. The functions `z=x^{11} y-x^{-1}` and `f=z^5+x^{-5}` are not polynomials. This is an exact obstruction-gap witness: the ODE (even together with `I_1=0`) admits a rational trajectory with nonzero last row, and the second polynomial boundary is the missing gate. It is not a Keller pair, not an AS109 lift, and not evidence that a lift exists.

Every Pfaffian row, the value `h eta=-6`, the first boundary polynomial, and the residual `-x^{-6}/5` were recomputed from Laurent monomials and from the substituted 1-forms, independently of the producer’s trajectory function (which asserts `I_2,I_3,omega` only in a comment, and checks `eta` and the two boundaries). The identities fill the comment.

---

## Claim 7 — hashes, controls, and scope

**CONFIRMED.**

The three frozen hashes in the prompt match the files on the charged tree, including the hash of `FREEZE.sha256` itself. The unmodified replay returns the four scoped booleans `full_sextic_theorem_proved=false`, `enumeration_run=false`, `lift_found=false`, `jc2_inference=false`, and the verdict string of a surviving Pfaffian gate. No finite formal support in the replay is used as a search cap.

Exact controls, independently recomputed:

```text
J(x+y,     y+(x+y)^6)     = 1,
J(x+y^2,   y+(x+y^2)^3)   = 1,
J(x+y^3,   y+(x+y^3)^2)   = 1,
J(x+y^5,   y+y^6)         = 1+6 y^5,
J(x+y^6,   y)             = 1.
```

The last is the equal-degree unipotent reduction. The rejection `1+6y^5` shows that a superficial `(5,6)` shape is not enough.

*Dependency status.* The confirmed quartic theorem is used only as the statement that every Keller pair with both `y`-degrees at most four is a polynomial automorphism. It is not used to close `(4,6)` or `(5,6)`. The quintic lane independently landed `CONFIRMED` during this review window; this preflight was written without it, and this review does not consume it. In particular, no identity from the quintic `(2,5)`, `(3,5)`, or `(4,5)` arguments is cited, and the unresolved-at-production `(4,5)` infinity discussion is not a blocker for the two sextic survivors.

*Scope exclusions, audited.*

- In scope: the `n=6` pair classification; the `(4,6)` leading discriminator (3.4); the depressed `(5,6)` Pfaffian (7.4) and the polynomiality gap of Section 8; exact characteristic-zero identities with arbitrary finite `x`-degree.
- Out of scope, and not claimed: a theorem that every Keller pair with both `y`-degrees `<=6` is an automorphism; emptiness of either `(4,6)` branch; a monic eliminant for `r` in `(5,6)`; a raised AS109 floor of seven (or six); finite-support existence or nonexistence; a found lift; a JC2 decision.
- Not used: marked collisions, support caps, `x`-degree bounds, coefficient height, finite Witt layers, exponent/support search, AWS.

The confirmed quartic floor stands: any exact AS109 lift must have correction `y`-degree at least five in one coordinate. Raising that floor to six would require consuming the independently landed quintic theorem, which this file does not do. Raising it to seven would additionally require closing both sextic survivors, which this file also does not do.

---

## Non-blocking precisions

None of the following changes a coefficient or a numbered verdict.

- Algebraic closure is a convenience on the `(4,6)` nonzero-`kappa` branch (`H=h^2` after taking a square root of a unit). The identities `a_4=H^2`, `b_6=H^3`, `N^2=kappa H^5`, and `12 h^5(r_f-r_g)=N` can be written over `K` with a unit factor in `H`. The preflight does not close the branch, so the detour is not load-bearing.
- Characteristic zero is load-bearing for the global factors `2,3,4,5,6`, for `deg pi'=deg pi-1` on nonconstant polynomials, and for invertibility of `5` in (5.2). All are stated.
- The auxiliary `z=hy+r` is used only to expand a Jacobian in `Kbar(x)[y]`. The pair `(f,g)` is never replaced by the source change `y\mapsto(z-r)/h`.
- Producer Section 9’s trajectory function checks `eta` and the two boundaries and comments that `I_2=I_3=omega=0`. The 1-form identities of claims 5–6 fill that comment; the replay is still a correct regression control.
- The headline overstatement that “no third polynomial first integral follows from the present calculation” is a completeness defect relative to `I_1`, already scoped as successor input. It is not a claim that `(5,6)` is empty, and it is not a claim that `omega` is closed.
- Jung–van der Kulk is not a dependency.

---

## Promotion advice (repeated)

Accept the file as a sharply specified survivor: two remaining sextic patterns, an exact `(5,6)` Pfaffian, a documented polynomiality gap, and no theorem. Do not raise the AS109 floor. Do not launch a support search from this gate. Do not treat (8.3) as a lift.

The fastest honest next exact work is parallel: a lower-row compiler for both `(4,6)` branches, and a `(5,6)` attack that starts from `I_1` together with both polynomial boundaries and the remaining `eta` speed law. Neither should block on, or silently consume, the quintic theorem.
