# Hostile different-model review — AS109 sextic `(5,6)` exclusion

| Field | Value |
|---|---|
| Claim under review | Characteristic-zero exclusion of actual `y`-degree pair `(5,6)`: a Keller pair cannot have actual degrees `(5,6)`. Both `y=0` boundaries, the third integral `dI_1=omega-(2A/5)\,dI_3`, the weighted binary Jacobian, the common-factor lemma, finite-pole polynomiality, and polynomial infinity are in scope. Full `y`-degree-`<=6` theorem, `(4,6)` closure, raised AS109 floor, lift, and JC2 inference are out of scope |
| Overall verdict | **CONFIRMED** |
| Smallest missing hypothesis | none that breaks a numbered claim (non-blocking: the Cayley–Hamilton / filtered-finiteness paragraph is a valid algebraic counterpart of the valuation argument and is not load-bearing for the exclusion; the bounded Darboux search is not used in the closure) |
| Evidence tier | independent exact 1-jet expansion of the depressed pair over `Q(alpha,beta,gamma,delta,epsilon)` with `Fraction` sparse polynomials (does not import the producer replay); independent sparse expansion of the homogeneous binary Jacobian in `(t,z,A,B,C,D)`; Euler identity and `(F^6/G^5)_z` numerator by hand and by machine; UFD / monic / depressed-coefficient argument for the common-factor lemma over `k(t)[z]`; valuation filtration by variable weight, including the `A=0` slice of `(K_1,K_2,K_3)`; independent Singular Groebner bases in orders `dp` and `Dp`, with `radical.lib` support; unmodified rerun of both producer replays as regression control; landed preflight review consumed only as licensed `(5,6)` normal form |
| Reviewer / model | Grok 4.6 (xAI). Different model family from the producer (OpenAI Codex, GPT-5 family) |
| Repo | `/Users/dc/code/math/jc2` |
| Git HEAD | `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54` (matches the charged basis) |
| Review window (UTC) | 2026-08-24T11:41:00Z – 2026-08-24T11:47:00Z |
| Python | 3.14.6; stdlib only (`fractions.Fraction`, integer dicts) |
| Singular | 4.4.1, `primdec.lib` / `radical.lib`; orders `dp` and `Dp` |
| Host | `dc-mbp-m2.local`, Darwin arm64 |

Producer and provenance inputs reread in full before any verdict:

- `xmodel/as109-sextic-56-exclusion-20260824.md` (SHA-256 `31420c0cd667640f340f4d127f185edd4515aac7df3733560e6d1fda5ec6c7a4`)
- `cases/as109_sextic_56_next_gate_20260824/verify_sextic_56_gate.py` (SHA-256 `cab6e8597403f5c19d03fcf2da42c37ee3523ce7de2e825812ba1a5cbc47d5d0`)
- `cases/as109_sextic_56_next_gate_20260824/verify_weighted_finiteness.sing` (SHA-256 `0b0c36722f64365ddb0e1c891569124a658c86a77a967c415a5f41da631f61ca`)
- `cases/as109_sextic_56_next_gate_20260824/FREEZE.sha256` (SHA-256 `4c3fa8e19b2e5c9a2c8abb962d5c13427db4e7c45922a06b3081782c77920f9b`)
- parent preflight `xmodel/as109-sextic-frontier-preflight-20260824.md` (SHA-256 `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4`) and its landed different-model review `xmodel/as109-sextic-preflight-review-grok-20260824.md` (SHA-256 `5bf1a677a59975defb33a58da74d7c7c1381535d84f91e7f1584d21624a385ff`); overall `CONFIRMED`; consumed only as the licensed `(5,6)` normal form, Jacobian rows (5.1), substitutions (5.2), 1-forms `omega,eta`, and successor identity (0.1)
- parent replay `cases/as109_sextic_frontier_preflight_20260824/verify_sextic_preflight.py` (SHA-256 `21bc494f552587ee0b64c01c735b2f1243eafce9599f1e05bc526d23e38f73ad`) and `FREEZE.sha256` (SHA-256 `2890f3dd5d09b45e4f047cbb509b42430c3c9a677412cccef0b18fd66b44c4ab`)

The committed basis is exactly `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`. Named producer artifacts remain uncommitted on top of that basis. No producer, canonical, ledger, freeze, or case file was edited. No enumerator was written or run. No AWS call was made. The independent `(4,6)` local-normalization artifacts present in the same working tree were not read as input and are not consumed.

Write `k` for an arbitrary characteristic-zero field, `kbar` for an algebraic closure (the producer works after base change to `kbar`), `J(f,g)=f_x g_y-f_y g_x`. Actual `y`-degrees throughout.

---

## Promotion

**Accept `EXACT (5,6) EXCLUSION` at the stated scope.**

- Over any algebraically closed characteristic-zero field, no Keller pair has actual `y`-degrees `(5,6)`.
- The argument uses both polynomial `y=0` boundaries, the third integral `I_1`, a weighted binary common-factor lemma, and a polynomial-infinity last-row contradiction. It does not use support enumeration.

**Do not promote this to:** a theorem that every Keller pair with both `y`-degrees `<=6` is an automorphism; emptiness of either `(4,6)` branch; a raised AS109 correction floor of seven (or six); nonexistence or existence of an arbitrary finite-support AS109 lift; a found lift; a characteristic-zero point; a JC2 counterexample or disproof; `HEIGHT-CERT`; cap widening; an exponent rectangle; a finite Witt-level inference; or a novelty / priority claim.

**Smallest valid successor.** Close the imprimitive `(4,6)` family independently. Do not treat this file as chain coverage for divisible sextic shears, and do not silently consume the quintic theorem to write a `<=6` theorem.

---

## Quarantine

No result here proves or disproves JC2. Producer JSON strings `EXACT-(5,6)-EXCLUSION` and `EXACT-WEIGHTED-(5,6)-CERTIFICATE` were not used as evidence; the identities below were re-derived. The sextic preflight and its landed `CONFIRMED` review are consumed only for the licensed `(5,6)` normal form named in claim 1. The quartic theorem is not used. The independently landed quintic theorem is recorded in the parent review and is **not** consumed. Finite-support search, Hensel, and Witt data are unused. Priority is quarantined from the mathematical verdict.

The rational one-boundary paths (5.4) are negative controls: each solves the Pfaffian with a nonzero last row and fails the missing boundary. They are not lifts.

---

## Scope (not enlarged)

One characteristic-zero field calculation, after base change to an algebraic closure, of actual `y`-degree pair `(5,6)`. Arbitrary finite `x`-degree is in scope inside the displayed identities. Target operations inherited from the preflight are automorphy tests; they need not preserve the integral AS109 seed chart. The full sextic pair list, `(4,6)`, quintic identities, generic exponent search, exponent rectangles, finite-Witt inference, and AWS are out of scope.

---

## Headline and subclaim table

| # | Exact subclaim | Verdict | What would have flipped it |
|---|---|---|---|
| 1 | Genuine `(5,6)` has `a_5=h^5`, `b_6=h^6` with `h in k[x]`, `h!=0`; after aligning depressions, `z=h y+r` and (1.1) hold with `r,A,B,C,D` initially in `k(x)` and `P,...,T` the exact polynomials (5.2); `J_(x,y)=h J_(x,z)`; all nine rows and both polynomial boundaries `u=f(x,0)`, `v=g(x,0)` are as displayed | **CONFIRMED** | chain-rule factor not equal to `h`; leftover `z^9` or missing summand in (5.1); `h` merely rational; `r` smuggled into `k[x]` at the start; a hidden division by `h` in (5.2) |
| 2 | The displayed weight-nine polynomial satisfies `dI_1=omega-(2A/5)\,dI_3` identically, including every parameter; along (1.2) one has `I_1=k_1`; the identity is undivided, hence valid at rank-drop of the characteristic minors; constants of integration are handled | **CONFIRMED** | a leftover 1-form component; `epsilon` silently required in `I_1`; identity using a determinant in the denominator; `I_1'=0` in `k(x)` failing to force a constant; a rank-drop trajectory exempted from (2.2) |
| 3 | Identity (3.4) holds as polynomials; Euler gives `t J=5 F G_z-6 G F_z`; on `K_1=K_2=K_3=H_{10}=0` one has `F^6=G^5` in `k(t)[z]`, hence `F=L_0^5`, `G=L_0^6` by UFD and `gcd(5,6)=1`; the missing `z^4` coefficient forces `L_0=z`, hence `A=B=C=D=0`; a shared finite linear factor plus the three `K_i=0` forces `H_{10}=0` and then `r=0` | **CONFIRMED** | sign error in (3.4) or Euler; `F^6=c(t)G^5` with `c!=1`; a common factor associated to `t`; characteristic dividing `5` or `6`; a non-monic linear form surviving depression |
| 4 | If `q>0` at a finite place, both boundaries and all three integrals have vanishing highest variable-weight parts, giving (5.2); parameters are constants, so they cannot cancel the leading polar parts; the lemma contradicts a nonzero initial tuple; both boundaries are essential; no fractional-valuation or zero-leading case is lost | **CONFIRMED** | a parameter term of the same variable weight as `I_1^{top}`, `F`, or `G`; one boundary implying the other on `A=B=C=0`; ramification failing to produce a nonzero initial tuple; a finite common root at `t=0` not covered by the lemma |
| 5 | The five leading forms are zero-dimensional of length `126`, with `r^{21}` in the ideal; `(K_1,K_2,K_3,H_{10})` is zero-dimensional of length `42`; both radicals are the origin; filtered-finiteness is valid as an algebraic counterpart and is **not necessary** for the valuation exclusion | **CONFIRMED** | `dim>0`; length not `126` or `42`; `r^{21}` not in the ideal; a nonzero geometric point on either leading scheme; the exclusion resting on an unproved Cayley–Hamilton step |
| 6 | For nonconstant polynomial `(A,B,C,D)`, the leading tuple lies on `K_1=K_2=K_3=0` with `H_{10}!=0`; the degree-`10q-1` coefficient of `eta(X')` is `(6q/125)H_{10}!=0`; lower parameter terms cannot cancel it; `10q-1>0`; the constant-coefficient case has `eta(X')=0`; both contradict `h\,eta(X')=jbar in k^*` | **CONFIRMED** | `H_{10}=0` at a nonzero leading tuple; leading coefficient of `eta(X')` not equal to `(6q/125)H_{10}`; parameter cancellation at degree `10q-1`; `10q-1<=0` on a nonconstant path; nonconstant `r` with constant `X` producing nonzero Jacobian |
| 7 | Frozen hashes match; both unmodified replays return the expected scoped flags; the admissible result is exclusion of actual `(5,6)` only | **CONFIRMED** | hash mismatch; `full_sextic_theorem_proved=true`; an enumeration or AWS call; a raised AS109 floor; a JC2 inference; an implicit `(4,6)` or quintic consumption |

All remarks below are non-blocking unless marked otherwise. None changes a coefficient or a numbered verdict.

---

## Replay and hashes

Frozen child hashes, recomputed on the charged tree:

| Artifact | SHA-256 | Match |
|---|---|---|
| `xmodel/as109-sextic-56-exclusion-20260824.md` | `31420c0cd667640f340f4d127f185edd4515aac7df3733560e6d1fda5ec6c7a4` | prompt and `FREEZE.sha256` |
| `cases/as109_sextic_56_next_gate_20260824/verify_sextic_56_gate.py` | `cab6e8597403f5c19d03fcf2da42c37ee3523ce7de2e825812ba1a5cbc47d5d0` | prompt and `FREEZE.sha256` |
| `cases/as109_sextic_56_next_gate_20260824/verify_weighted_finiteness.sing` | `0b0c36722f64365ddb0e1c891569124a658c86a77a967c415a5f41da631f61ca` | prompt and `FREEZE.sha256` |
| `cases/as109_sextic_56_next_gate_20260824/FREEZE.sha256` | `4c3fa8e19b2e5c9a2c8abb962d5c13427db4e7c45922a06b3081782c77920f9b` | prompt |
| `xmodel/as109-sextic-frontier-preflight-20260824.md` | `bbe95d911077baa1c32fedc062807ce754c68ddd58c26a4b209d56333678f9a4` | producer provenance; parent freeze |
| `xmodel/as109-sextic-preflight-review-grok-20260824.md` | `5bf1a677a59975defb33a58da74d7c7c1381535d84f91e7f1584d21624a385ff` | producer provenance; landed `CONFIRMED` |
| `cases/as109_sextic_frontier_preflight_20260824/verify_sextic_preflight.py` | `21bc494f552587ee0b64c01c735b2f1243eafce9599f1e05bc526d23e38f73ad` | parent freeze |
| `cases/as109_sextic_frontier_preflight_20260824/FREEZE.sha256` | `2890f3dd5d09b45e4f047cbb509b42430c3c9a677412cccef0b18fd66b44c4ab` | parent freeze |

The child case directory contains only `FREEZE.sha256`, `verify_sextic_56_gate.py`, and `verify_weighted_finiteness.sing`. Registered commands, rerun unmodified, no network:

```sh
python3 cases/as109_sextic_56_next_gate_20260824/verify_sextic_56_gate.py
Singular -q cases/as109_sextic_56_next_gate_20260824/verify_weighted_finiteness.sing
```

Both exit 0. Python top-level fields:

```text
verdict = EXACT-(5,6)-EXCLUSION
actual_degree_pair_5_6_exists = false
full_sextic_theorem_proved = false
as109_floor_raised = false
support_enumeration = false
aws_used = false
lift_found = false
jc2_inference = false
primitive_search rank = 26, solution H=I1, mu=-2A/5
bounded_zero_cofactor_darboux_nullities = 0,0,0,0,0,0,1,1,2
```

Singular top-level fields:

```text
verdict = EXACT-WEIGHTED-(5,6)-CERTIFICATE
boundary_top_dim = 0
boundary_top_quotient_length = 126
r_power_certificate = r^21 in boundary_top
eta_top_dim = 0
eta_top_quotient_length = 42
both_y0_boundaries_used = true
enumeration_run = false
jc2_inference = false
```

The Python replay is a finite exact regression control: it reconstructs the weight-nine primitive by linear solve rather than checking a copied polynomial, derives the characteristic minors, and expands the binary Jacobian. The exclusion itself is the prose in claims 3–6. Those identities were re-derived in a second sparse engine that does not import the producer, and the two zero-dimensional certificates were recomputed in Singular with a second monomial order and with radicals.

---

## Claim 1 — `(5,6)` normal form, `k(x)` coefficients, polynomial `h`, rows, both boundaries

**CONFIRMED.**

On a genuine pair of actual degrees `(5,6)` the top Jacobian coefficient is

```text
[y^{10}] J = 6 a_5' b_6 - 5 a_5 b_6' = 0,
```

equivalently `(a_5^6/b_6^5)'=0` in `k(x)`. The kernel of `d/dx` on `k(x)` is `k`, so `a_5^6 = c\, b_6^5` with `c in k^*`. Unique factorization in `k[x]` gives `6 v_p(a_5)=5 v_p(b_6)` at every prime. Since `gcd(5,6)=1`, `v_p(a_5)` is divisible by `5` and `v_p(b_6)` by `6`. After absorbing units by constant target scaling one has

```text
a_5 = h^5,     b_6 = h^6,     h in k[x],     h != 0.
```

Algebraic closure is not required for this step. Genuine degree five forbids `h=0`. The next row is the displayed depression invariant; `g |-> g+lambda f` shifts it by `-5 lambda`, so the two linear depressions may be aligned and a common `z=h y+r` introduced. This is an identity in `k(x)[y]`, not a polynomial source automorphism. The functions `r,A,B,C,D` are a priori in `k(x)` (lower `y`-coefficients of `f` divided by powers of `h`, after the translation `y |-> y + r/h` in the coefficient field). The five functions `P,...,T` are the exact polynomials (5.2) in those quantities and constants `alpha,...,epsilon in k`. So `P,...,T` initially lie in `k(x)` as well, but they are not independent.

Chain rule: `z=h y+r` gives `f_y=F_z h`, `g_y=G_z h`, and the `z_x` terms in `f_x,g_x` cancel, so `J_(x,y)=h J_(x,z)`. The auxiliary `z` is used only to expand a Jacobian; the pair is never replaced by the source change `y |-> (z-r)/h`. Independently, the second engine expanded `F_x G_z - F_z G_x` in `z` after substituting (5.2) and obtained degrees `{0,1,2,3}` only: `E_8=...=E_4=0` identically, `E_3=dI_3`, `E_2=dI_2`, and `E_1,E_0` equal to the displayed `omega,eta` including every parameter. The constant `epsilon` occurs in `T` and in no 1-form used later; target translation of `g` absorbs it.

Both constant-term boundaries belong to `k[x]`:

```text
u = f(x,0) = r^5 + A r^3 + B r^2 + C r + D,
v = g(x,0) = r^6 + P r^4 + Q r^3 + R r^2 + S r + T.
```

No `x`-degree bound is used. The Jacobian rows remaining after (5.2) are exactly (1.2). This is the licensed preflight output; the identities just named were re-expanded rather than trusted as strings.

---

## Claim 2 — third-integral identity, rank-drop, constants of integration

**CONFIRMED.**

Direct differentiation of the displayed polynomial (2.1) in the 1-jet ring of `(A,B,C,D)` with parameters `alpha,beta,gamma,delta` produces

```text
dI_1 - omega + (2A/5) dI_3 = 0
```

as a 4-tuple of polynomials. Every summand of (2.1) is required; omitting any of `24 A^3 B/125`, `-4 B^3/25`, `-18 A B C/25`, `-6 A^2 D/25`, `6 C D/5`, or the eight parameter terms breaks a component. The second engine checked the identity with `epsilon` present in the ambient ring: `I_1,I_2,I_3,omega,eta` are independent of `epsilon`. Consequently the identity is a polynomial 1-form equation on the whole coefficient space. No minor, determinant, or rank hypothesis enters.

Along any path satisfying (1.2) one therefore has `I_1'=0` in `k(x)`. The kernel of `d/dx` on `k(x)` is `k`, so `I_1=k_1 in k`. The same holds for `I_2,I_3`. An additive constant in `I_1` is absorbed into `k_1`. The integration constants `alpha,beta,gamma,delta` already sit inside the polynomial; they are not forgotten. On the line `A=B=C=0` one has the exact specializations

```text
I_1 = 2 gamma D,     I_2 = 3 beta D,     I_3 = 4 alpha D,
```

so with all parameters zero that line lies on all three levels, matching the one-boundary controls. If a parameter is nonzero, the line is *more* constrained, not less.

Rank-drop of the characteristic minors (2.3) is irrelevant to (2.2). Those minors define a vector `V` with `dI_1(V)=dI_2(V)=dI_3(V)=omega(V)=0` on the nose (Laplace expansion, plus the 1-form identity for `omega`), and the second engine confirmed `eta(V)` is not the zero polynomial (374 terms; at `(A,B,C,D)=(0,0,0,1)` one has `eta(V)=1296/625`). On the rank-three locus `X'=lambda V` and the speed law is (2.5). At rank-drop, `V=0` and `X'` need only lie in the common kernel of `dI_1,dI_2,dI_3`. The pole and infinity arguments never divide by a minor and never use `X' || V`; they use the undivided rows (1.2) and the three scalar equations (2.2). A rank-drop trajectory that remained Keller would still have polynomial boundaries and constant integrals, and would still be forbidden by claims 4 and 6. (At the origin, `X'=0` and `eta(X')=0`, which already contradicts `jbar != 0`.)

The bounded searches (2.7)–(2.9) are correctly scoped as negative results through weight nine. They are not used in the closure. The linear solve reconstructing `H=I_1`, `mu=-2A/5` unique modulo `alpha I_3` is consistent with the 1-form identity, which is the stronger statement.

---

## Claim 3 — binary Jacobian, characteristic minors, common-factor lemma

**CONFIRMED.**

The homogeneous binary forms (3.1) are the variable-weight leading parts of `F,G` at `t` of weight `1`. The scaled integrals (3.2) satisfy `I_3^{top}=6 K_3/25`, `I_2^{top}=3 K_2/125`, `I_1^{top}=2 K_1/125` as polynomials (independent check, all parameters dropped). Independent expansion of `J_{(t,z)}(F,G)=F_t G_z - F_z G_t` recovers (3.4) identically, including the mixed term `(84/125) A K_3 t^8 z`. In particular, on `K_1=K_2=K_3=0`,

```text
J_{(t,z)}(F,G) = (6/125) H_{10} t^9.
```

Euler: `t F_t + z F_z = 5 F` and `t G_t + z G_z = 6 G` give `t J = 5 F G_z - 6 G F_z`, checked as a polynomial identity. The `z`-derivative of `F^6/G^5` has numerator proportional to `6 G F_z - 5 F G_z = -t J`. Thus `J=0` implies `(F^6/G^5)_z=0` in `k(t)(z)`. Both `F` and `G` are monic in `z` of degrees `5` and `6`, so `F^6` and `G^5` are monic of degree `30` and the `z`-independent ratio equals `1`. Hence `F^6=G^5` in `k(t)[z]`. (Neither form is the zero polynomial: both are monic.)

Unique factorization in the Euclidean domain `k(t)[z]`, together with `gcd(5,6)=1` and monicity, yields `F=L_0^5` and `G=L_0^6` for a monic linear `L_0=z-rho` with `rho in k(t)`. The coefficient of `z^4` in `L_0^5` is `-5 rho`. The depressed form `F` has no `z^4` term (independent check: that coefficient polynomial is empty), so `rho=0` in characteristic zero. Thus `L_0=z`, `F=z^5`, `G=z^6`, and `A=B=C=D=0`. No genericity, smoothness, or division by a coefficient variable enters. Units in `k(t)` are excluded by monicity of both `F` and `G`: a leading coefficient `c in k(t)` would have to satisfy `c^5=c^6=1`, hence `c=1`.

First statement of the lemma: a common finite root `z=r t` means `L=z-r t` divides `F` and `G`, hence divides `J`. On `K_1=K_2=K_3=0` this is `(6/125) H_{10} t^9`. The form `L` is not associate to `t` (`L` has `z`-coefficient `1`). Therefore `H_{10}=0`. The second statement then applies, and `F(1,r)=r^5=0` forces `r=0`.

The conceptual derivation via the weighted radial vector `W=(2A,3B,4C,5D)` is consistent: the second engine computed `eta^{top}(W)=6 H_{10}/125`, matching the `t^9` coefficient of (3.4) after Euler. Characteristic minors of `(I_1,I_2,I_3)` are not required for the lemma; they only produce the Darboux vector `V` of claim 2.

Hostile extras that did not flip the lemma: `F(0,z)=z^5` and `G(0,z)=z^6` have no common root with `t=0` except the illegal origin `(t,z)=(0,0)`, so there is no “infinite” common binary root to lose. If `G` vanished identically one could not form `F^6/G^5`; that does not occur.

---

## Claim 4 — finite-pole elimination

**CONFIRMED.**

At a finite place let `q` be (5.1). If `q=0` there is no pole at that place. If `q>0`, a finite ramified extension makes the weighted initial coefficients `(r_0,A_0,B_0,C_0,D_0)` defined, with at least one nonzero by maximality of `q`. (Residue fields remain `k` because `k` is algebraically closed.) Variable weights of `(r,A,B,C,D)` are `(1,2,3,4,5)`, so

```text
f(x,0) = pi^{-5q} F(1,r_0) + (strictly less polar),
g(x,0) = pi^{-6q} G(1,r_0) + (strictly less polar).
```

Both left-hand sides are polynomials, hence have valuation `>=0`. For `q>0` the polar leading coefficients vanish: `F(1,r_0)=G(1,r_0)=0`. The three integrals are constants, valuation `>=0`. Each is weighted-homogeneous of weights `9,8,7` in the eight variables `(A,B,C,D; alpha,beta,gamma,delta)`. Parameters lie in `k`, so `v(alpha)>=0` and likewise for the others; every term containing a parameter therefore has *strictly lower variable weight* and a strictly less polar leading part. Independently checked: every monomial in `I_1,I_2,I_3` has the expected total weight, and every monomial that involves a parameter has variable weight strictly below `9,8,7` respectively. The same holds for `eta` and for the top parts of `P,...,T`. Thus the highest polar parts of the integrals are exactly `K_1,K_2,K_3` at the initial tuple, and (5.2) holds.

The common-factor lemma then forces the initial tuple to vanish, a contradiction. Therefore `q=0` at every finite place, i.e. `r,A,B,C,D in k[x]`.

Fractional valuations are not lost: `q` is a maximum of rationals with denominators in `{1,2,3,4,5}`; ramification of index dividing `60` clears them, and the initial-form argument is unchanged. A zero leading tuple cannot occur by construction of `q`. Poles of `h` cannot occur: `h` is already in `k[x]`.

Both boundaries are essential. With all parameters zero, `A=B=C=0` lies on `I_1=I_2=I_3=0` and `omega(X')=0` for any `D`. The two specializations (5.4) were recomputed:

```text
D = -r^5      =>  F(1,r)=0,   G(1,r)=-r^6/5,
D = -5 r^5/6  =>  G(1,r)=0,   F(1,r)= r^5/6.
```

On the Laurent path `r=-x^{-1}`, `D=c x^{-5}`, `h=x^{11}`, one has `eta=(6/5) D D'` and `h eta=-6 c^2 != 0`. Each missing boundary retains a pole (`-x^{-6}/5` or `x^{-5}/6`). These are exact Pfaffian solutions, not Keller pairs. Dropping either boundary would leave a rational pole.

---

## Claim 5 — Singular certificates, lengths 126 and 42, `r^{21}`, filtered-finiteness

**CONFIRMED.**

Producer Singular, rerun unmodified, reports `dim=0`, `vdim=126`, `r^{21}` in the boundary ideal, and `dim=0`, `vdim=42` for `(K_1,K_2,K_3,H_{10})`. An independent Singular session with the same generators, in both `dp` and `Dp`, reproduced those four numbers. Additional independent facts, not claimed by the producer and not needed to confirm the claim:

- `r^{20}` does **not** lie in the boundary ideal, so the nilpotency certificate is sharp.
- `radical` of the boundary ideal is `(r,A,B,C,D)` (quotient length `1`). The only geometric point is the origin.
- `radical` of `(K_1,K_2,K_3,H_{10})` is `(A,B,C,D)` (quotient length `1`).
- `V(K_1,K_2,K_3)` has dimension `1`. Its intersection with `A=0` has radical `(A,B,C)`: on the cone, `A=0` implies `B=C=0` with `D` free (the `D`-axis). This is the input used in claim 6 to see that `10q` is an integer.
- Over `Q` the scaled generator `125 G(1,r)` generates the same ideal as `G(1,r)`, since `125 in Q^*`.

The length `126=5*6*7*8*9/(1*2*3*4*5)` is the weighted complete-intersection number for degrees `(5,6,7,8,9)` in weights `(1,2,3,4,5)`. The length `42=7*8*9*10/(2*3*4*5)` is the analogous number for `(K_1,K_2,K_3,H_{10})`. Matching lengths plus reduced support at the origin are consistent with weighted complete intersections concentrated at `0`; the lemma already supplies the geometric statement.

**Filtered-finiteness prose.** Section 5.1 is valid and is not necessary to the valuation exclusion.

- Valid: the associated-graded map is the leading fivefold whose only common zero is the origin. A basis of the length-`126` quotient of the associated graded lifts to at most `126` module generators of `k[r,A,B,C,D]` over the subalgebra generated by the five displayed polynomials (filtered Nakayama). Cayley–Hamilton then supplies a monic of degree at most `126` for each of `r,A,B,C,D`. Specializing the five values to the polynomial data `f(x,0)`, `g(x,0)`, `k_1,k_2,k_3` and using that `k[x]` is integrally closed puts `r,A,B,C,D` in `k[x]`. Independently, the five polynomials with generic integer parameters `(alpha,...,epsilon)=(1,1,1,1,1)` remain zero-dimensional of length `126`, so restoring lower-weight terms does not create a positive-dimensional fibre in that sample.
- Unnecessary to the exclusion: claim 4 is a self-contained valuation contradiction at any finite place with `q>0`. It never invokes a monic eliminant, filtered division, or Cayley–Hamilton. The producer correctly calls 5.1 the “algebraic counterpart” of (5.3) and does not rest the pole step on an expanded eliminant.

This is a packaging remark, not a gap.

---

## Claim 6 — polynomial infinity

**CONFIRMED.**

After (5.3), `A,B,C,D` are polynomials. If at least one is nonconstant, `q` as in (6.1) is positive. The weighted leading tuple `(a,b,c,d)` is nonzero. Constancy of the three integrals forces `K_1=K_2=K_3=0` at that tuple (parameters have `x`-degree `0`, hence strictly lower `x`-degree than the variable-weight tops when `q>0`). The second part of the lemma forbids `H_{10}(a,b,c,d)=0`. Equation (3.6) gives `eta^{top}(W)=6 H_{10}/125`.

Leading derivatives: if `A=a x^{2q}+...` then `A'=(2q)a x^{2q-1}+...`, and likewise for `B,C,D`. So the leading of `X'` is `q W(a,b,c,d)` in the weighted sense. Each pairing `eta_A A'`, ..., `eta_D D'` has weighted degree `10q-1` (`eta` components have variable weights `8,7,6,5`). The leading coefficient of `eta(X')` is therefore

```text
q * (6/125) H_{10}(a,b,c,d) = (6q/125) H_{10}(a,b,c,d) != 0.
```

Independent samples:

- `D`-axis, `A=B=C=0`, `D=x^n`, `q=n/5`, `H_{10}=125`. Directly `eta=(6/5) D D'` has degree `2n-1=10q-1` and leading coefficient `(6/5)n=(6q/125)*125`. Holds for `n=1,...,5`.
- Point `(A,B,C,D)=(5,0,5,0)` on `K_1=K_2=K_3=0` with `H_{10}=-1250`. The path `A=5x^2`, `C=5x^4`, `B=D=0` has `q=1` and `eta(X')=-60 x^9`, matching `(6q/125)H_{10}=-60`.

Lower parameter terms cannot cancel this coefficient: the variable-weight gap in every `eta` component is at least `2`, so parameter contributions have `x`-degree at most `8q-1 < 10q-1` once `q>0`. Independently checked monomial by monomial.

The inequality `10q-1>0`: a nonconstant polynomial among variables of weights at most five has degree at least `1`, so `q>=1/5` and `10q-1>=1`. On the cone `K_1=K_2=K_3=0` the slice `A=0` is the `D`-axis (claim 5), so either `A!=0` and `2q in Z` (hence `10q in Z`), or the path is along `D` and `5q in Z`. In all cases `10q-1` is a positive integer equal to the actual degree of the polynomial `eta(X')`. No half-integer-degree phantom occurs.

If `A,B,C,D` are all constant then `X'=0` and `eta(X')=0`. Nonconstant polynomial `r` or `h` does not restore the Jacobian: `z_x` cancels in the chain rule, and `eta` does not involve `r`. Direct contradiction to `h eta(X')=jbar in k^*`.

These alternatives exhaust the case. The product of the nonzero polynomial `h` with a nonconstant polynomial `eta(X')` (or with `0`) cannot be a nonzero constant, because `k[x]` is a domain. Therefore no characteristic-zero Keller pair has actual `y`-degrees `(5,6)`.

---

## Claim 7 — hashes, deterministic replay, dependencies, exact scope

**CONFIRMED.**

The four frozen child hashes in the prompt match the files on the charged tree, including the hash of `FREEZE.sha256` itself. Parent preflight hashes match both the child provenance table and the parent freeze. Both unmodified replays return the scoped booleans listed above, with no enumeration flag, no AWS flag, no raised floor, and no JC2 inference. The Python replay uses only the standard library. The Singular replay is exact over `Q`.

*Dependency status.* The landed preflight review is consumed as the licensed `(5,6)` normal form, rows (5.1), substitutions (5.2), and the successor 1-form (0.1). Those objects were re-expanded in this review. The quartic theorem is not used. The independently landed quintic theorem is not used. No identity from `(2,5)`, `(3,5)`, `(4,5)`, or `(4,6)` is cited. Jung–van der Kulk is not a dependency.

*Scope exclusions, audited.*

- In scope, and proved: there is no characteristic-zero Keller pair of actual `y`-degrees `(5,6)`.
- Out of scope, and not claimed: a theorem that every Keller pair with both `y`-degrees `<=6` is an automorphism; emptiness of either `(4,6)` branch; a raised AS109 floor of seven or six; finite-support existence or nonexistence; a found lift; a JC2 decision.
- Not used: marked collisions, support caps, `x`-degree bounds, coefficient height, finite Witt layers, exponent/support search, AWS.

Producer Section 8’s campaign sentence that, conditional on the landed quintic theorem, the only remaining maximum-`y`-degree-six blocker is `(4,6)` is commentary, not a theorem of this file. This review does not confirm that commentary and does not write a `<=6` theorem. The coprime sextic branch is closed; the imprimitive branch is not.

---

## Non-blocking precisions

None of the following changes a coefficient or a numbered verdict.

- Algebraic closure is used to take residue fields of finite places of `k(x)` equal to `k` and to write a linear factor `z-r t` over `k`. The UFD step for `h` and the monic-linear step `rho=0` in `k(t)[z]` do not need it.
- Characteristic zero is load-bearing for the global factors `2,3,4,5,6`, for `deg pi'=deg pi-1` on nonconstant polynomials, for invertibility of `5` in (5.2) and in `mu=-2A/5`, and for `(F^6/G^5)_z`. All are stated. For AS109 one works over `Q_{109}` with `109 != 5`.
- The bounded zero-cofactor Darboux search through weight nine finds no fourth low-weight integral. That is correctly scoped; the closure does not use it and does not claim anything about nonzero-cofactor Darboux polynomials.
- `r^{20}` not lying in the boundary ideal is an extra sharpness statement. The producer’s `r^{21}` certificate is correct and sufficient.
- Section 5.1 is valid equivalent packaging of claim 4, not a second independent proof, and not a hidden gap.
- The characteristic vector field `V` is used only to organize the Darboux search and to record that `eta(V)` is not the zero polynomial. Exclusion does not travel along `V`.
- Producer (6.3) refers to the last row of `J_(x,z)`, i.e. to `eta(X')`, not to `h eta(X')`. The subsequent sentence is unambiguous. Leading-coefficient cancellation between `h` and `eta(X')` cannot occur: `h != 0` in the domain `k[x]` and `eta(X')` has a nonzero leading coefficient of positive degree.

---

## Promotion advice (repeated)

Accept the file as an exact characteristic-zero exclusion of actual `y`-degrees `(5,6)`. Do not raise the AS109 floor. Do not launch a support search from this gate. Do not treat a one-boundary Laurent path as a lift. Do not infer a `y`-degree-at-most-six theorem: `(4,6)` remains, and chain coverage of divisible sextic shears plus the quintic range is a separate consumption step that this review does not perform.
