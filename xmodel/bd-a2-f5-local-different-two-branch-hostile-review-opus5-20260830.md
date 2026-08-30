# Hostile review: F5 local different and the `3+5` attachment split

Reviewer: Opus 5 (independent, different model from producer Sol 5.6).
Date: 2026-08-30 UTC.
Review basis: `1efd7a76538e3fcdf51b999563262afc40d58947` (verified;
producer basis `1c665e1f...` verified as ancestor).

## 0. Custody and execution disclosure

Re-hashed on the review basis, all four declared inputs match:

```text
8a1c3c50...  f5-local-different producer      body 9253 / 61931ec7...  MATCH
255bd0ba...  ramification-attachment integ.                            MATCH
e3dc96f0...  bidegree-(2,3) forest integ.                              MATCH
410de2f5...  discriminant/conductor integ.                             MATCH
```

I recomputed the producer body independently: 9253 bytes through the unique
standalone `<!-- BODY-END -->` line, SHA-256 `61931ec7...`. Seal is honest.

Execution: I had a shell. I used it for hashing plus one light `sympy`
polynomial check (expansion, `discriminant`, `resultant`, three branch
restrictions, two truncated Hensel series). No Singular, no heavy CAS, no
`jc2-lean` access, no input/canonical file touched. Everything in §§1-5
below was first derived by hand; the CAS only confirmed it.

`FALLACY-v2` `charge_basis` line: **not applicable**. This packet asserts no
cv exit price; all charges here are plane-germ intersection multiplicities.

## 1. Item 1 — F5 local normal form: `CONFIRM_WITH_CORRECTIONS`

Reconstructed from the forest classification, not from the producer.
With `S=P1_v x P1_z`, `(1,0)=[{pt}xP1_z]`, `(a,b).(c,d)=ad+bc`: the `(0,1)`
component `H_0` and each `(1,1)` component `Q_i` have degree one over
`L_infinity`, and `Q_i` is the graph of a Mobius `phi_i`. Global numbers
`H_0.Q_i=1`, `Q_1.Q_2=2`.

Budget consistency (my check, not in the producer): all components are
smooth rational, so `delta_p = 1+1+2 = 4`, `r_p = 3`,
`K = delta_p-r_p+1 = 2`. This saturates `K(C)=2`, so **`p` is the only
singular point of `H`** and every listed intersection is concentrated there.
The F5 row is therefore self-consistent and the "all three at one point,
contact two" data is forced, not assumed.

Normal form. Normalize `H_0={z=0}`, `phi_i(0)=0`. Apply the fibre Mobius
`z |-> phi_1^{-1}(z)` (fixes `z=0`): `Q_1` becomes `z=v`, and `Q_2` becomes
the graph of `psi = phi_1^{-1} o phi_2` with `psi(0)=0`, `psi'(0)=1`
(contact two), `psi != id`. Hence `psi(v)=v/(1+gamma v)`, `gamma != 0`.
The common scaling `(v,z) |-> (v/gamma, z/gamma)` sends `psi` to
`v/(1+v)`. So exactly

```text
H_0: z=0,   Q_1: z-v=0,   Q_2: (1+v)z-v=0,
h = z(z-v)((1+v)z-v).
```

**No hidden moduli.** I verified this by orbit count as well: the F5 family
has dimension `1+3+3-2 = 5`; `dim(PGL2 x PGL2) = 6`; the stabilizer of the
standard configuration is exactly the 1-dimensional parabolic
`v |-> v/(1+tv)`, `z |-> z/(1+tz)` (the subgroup commuting with `psi`).
Orbit dimension `5` = family dimension, so the F5 configuration is a single
orbit. `CONFIRMED`.

Coordinate hypothesis audit. The reduction uses one Mobius in `z` and one
scaling in `v`. The `z`-change is unconditionally free: `pi` forgets `z`, so
any fibre-preserving change multiplies `f_z` by a unit on `X`. The
`v`-change is a linear automorphism of the target fixing `L_infinity`, hence
compatible with `u`. So the normal form is legitimate as a **local-analytic**
statement at `p`, which is all the different computation needs.

Corrections:

* **C1** (§0). "smooth projectively finite *cubic* incidence" mis-scopes the
  packet. The surface is *quadratic* (`X` of class `2A+3B`); only the
  projection `pi` has degree three. Read as written, §0 claims a scope the
  body never establishes.
* **C2** (§2). "Their contact order two says that the two transformations
  have the same nonzero first derivative" attributes too much to contact.
  Contact two gives only `phi_1'(0)=phi_2'(0)`. Nonvanishing is separate and
  doubly forced: a Mobius map has nowhere-zero derivative, and
  `H_0.Q_i=1` forces transversality to `z=0`.
* **C3** (§2). The reduction recipe should be stated as "one projective
  change in `z`, then one common scaling", not "independent projective
  changes in `v,z` followed by a common scaling" — no independent
  `v`-Mobius is used or needed.

## 2. Item 2 — `f=h+ug`, unit, `U`, tangent cone, two branches: `CONFIRM_WITH_CORRECTIONS`

`f(0,v,z) = w.h` with `w` a unit germ. Replacing `f` by `f/w` is legitimate:
`(f/w)_z = f_z/w - f w_z/w^2`, which equals `f_z/w` **on** `X`, so the
divisor `{f_z|X}` is unchanged. Only after this division is (2.2) exact.

`h_v(0)=h_z(0)=0` since `ord h = 3`; smoothness of `X` at `p` then forces
`f_u(0)=g(0) != 0`, so `g` is a unit, `u=U(v,z)` by the implicit function
theorem, and `Ohat_{X,p}=C[[v,z]]`. From `U = -h/g(U,v,z)` with
`g(U,v,z)` a unit, `ord U = 3` **exactly** (the producer states only `>=3`;
the exact value is what makes `(U)=(h)` in §3 below).

Different: `Omega_{X/P2} = O_X/(f_z)` for the hypersurface
`X subset P2 x P1`, so `R_pi = div(f_z|X)`. Class check (mine):
`R_pi in |(-2B)-(-2A-3B)| = |2A+B|`, and
`H.R_pi = A.(2A+B).(2A+3B) = 8 A^2 B = 8`. Both promoted values reproduce.

Tangent cone. Expanding exactly,
`h = (1+v)z^3 - (2v+v^2)z^2 + v^2 z`, so

```text
h_z = 3(1+v)z^2 - (4v+2v^2)z + v^2 = (z-v)(3z-v) + 3vz^2 - 2v^2z.
```

Since `r = h_z + U g_z` with `ord(U g_z) >= 3`,
`in_2(r) = (z-v)(3z-v)`. `CONFIRMED`.

Two smooth branches, rigorously and coefficient-independently: `in_2(r)` has
`z^2`-coefficient `3 != 0`, so `r` is `z`-regular of order two and
Weierstrass preparation gives `r = unit.(z^2 + a_1(v)z + a_0(v))` with
`ord a_1 >= 1`, `ord a_0 >= 2`. Distinctness of the two tangent lines makes
`a_1^2-4a_0 = v^2.(unit)`; a unit in `C[[v]]` has a square root, so the
quadratic formula splits it over `C[[v]]`:

```text
r = unit . (z - xi_tan(v)) . (z - xi_tr(v)),
xi_tan = v + O(v^2),   xi_tr = v/3 + O(v^2).
```

Two reduced smooth branches, transverse, for **every** unit `g`. The germ of
`R_pi` at `p` is therefore reduced, and cannot be one branch of any
multiplicity. `CONFIRMED`. (CAS confirmation: solving for the two branches
of `h_z` to order `v^4` returns `v - v^2/2 + 5v^3/8 - 11v^4/16` and
`v/3 - v^2/6 + v^3/24 + v^4/48`.)

* **C4** (§2/§3). Make the unit division `f |-> f/w` an explicit step before
  (2.2), and record `ord U = 3` exactly.

## 3. Item 3 — length, discriminant, `3+5`: `CONFIRM_WITH_CORRECTIONS`

Ideal of `H` in `C[[v,z]]`: `H = X cap {u=0}`, ideal `(U)`, and
`U = h.(unit)` so `(U)=(h)`. Then `r = h_z + h.(unit).g_z ≡ h_z (mod h)`,
giving `I_p(H,R_pi) = length C[[v,z]]/(h,h_z)`. `CONFIRMED`.

Discriminant. Roots `0, v, v/(1+v)`, leading coefficient `(1+v)`:

```text
disc_z(h) = (1+v)^4 . v^2 . (v/(1+v))^2 . (v^2/(1+v))^2 = v^8,
```

**exactly**, not merely up to a unit. CAS confirms `disc_z(h) = v^8` and
`Res_z(h,h_z) = -v^8(1+v)`.

Resultant/length passage. The clean route: `h = (1+v).W_0` with `W_0` monic
of degree three in `z` over `C[[v]]`, `C[[v]][z]/(W_0)` free of rank three,
`det(mult by h_z) = Res_z(W_0,h_z) = -v^8/(1+v)`, so
`length = ord_v = 8`. `I_p(H,R_pi)=8`. `CONFIRMED`, and equal to the global
`H.R_pi=8`, so as a set `R_pi cap H = {p}`.

Branchwise split. Direct restriction (hand, CAS-confirmed):

```text
r|_{z=0}       = v^2                 ord 2
r|_{z=v}       = v^3                 ord 3
r|_{z=v/(1+v)} = -v^3/(1+v)          ord 3        total 8   OK
```

(valid for `r`, not just `h_z`, because `U` vanishes on each branch of `H`.)
None is zero, so `r` and `h` share no branch: **all intersection numbers are
finite and additivity is legitimate.** The producer never checks this.

`D_tr` (tangent `3z=v`) is transverse to all three branches of `H` (whose
tangents are `z=0`, `z=v`, `z=v`), so `I_p(H,D_tr) = 1+1+1 = 3`, **exact**.
`D_tan` (tangent `z=v`) is transverse to `H_0` (exactly 1) and tangent to
both `Q_i` (each `>= 2`), so `I_p(H,D_tan) >= 5`. Additivity plus the exact
total `8` and the exact `3` forces `I_p(H,D_tan) = 5` and the branchwise
table

```text
                H_0   Q_1   Q_2   total
    D_tan        1     2     2      5
    D_tr         1     1     1      3
    total        2     3     3      8
```

which reproduces the three restriction orders above independently.
`8 = 3+5` `CONFIRMED`, for arbitrary unit `g`.

`FALLACY-v2` floor/attainment note: this is a floor-plus-exact-complement
argument. It is sound **only** because the `D_tr` side is exact, not a
bound, and because the total is exact. Two floors would not suffice. The
producer does not flag this; the load-bearing exactness is (4.4).

* **C5 (MATERIAL)** (3.4). Display (3.4) introduces `D_tan: z=v`,
  `D_tr: 3z=v` as *tangent lines*, and §4 then uses the same symbols as the
  *Hensel branches*. Under the literal reading (4.5) is false and
  meaningless: `z-v` divides `h`, so `I_p(H,{z=v}) = infinity`. The
  displayed lines must be renamed (e.g. `T_tan`, `T_tr`) and `D_tan`,
  `D_tr` reserved for the branches `z=xi_tan(v)`, `z=xi_tr(v)`. The
  underlying mathematics is correct; the symbol is not.
* **C6** (§4). Add the "no common branch" check before invoking additivity.

## 4. Item 4 — object typing: `CONFIRM_WITH_CORRECTIONS`

The four-object firewall (source Cartier different `R_pi = div(f_z|X)`;
its reduced support `Rbar`; target trace discriminant; reduced target
branch) is stated correctly in §1 and respected throughout. No conductor and
no normalization-index/Fitting divisor is used anywhere — correct, and
required, since `bd-fix3` §2 exhibits `index != conductor` (`SH-2`:
index 2, conductor 1) and §3 shows normalization does not commute with
slicing. The packet also never slices a normalization, so `bd-fix3` §3 is
not engaged. Reducedness is asserted only *at `p`*, not globally — correct
typing of Cartier versus reduced support.

Target-discriminant claim. With `f/w = unit . W` (Weierstrass, degree three
in `z`), the local target discriminant is `disc_z(W)(u,v)`, and
`disc_z(W)|_{u=0} = disc_z(W_0) = v^8/(1+v)^4 = v^8 . (unit)`. So "the
restriction of the target trace discriminant, up to a nonzero unit" is
`CONFIRMED`, and the producer's refusal to identify branches is correct:
the discriminant multiplicities are norms of different exponents
(`bd-fix3` §1), not the reduced source ramification.

* **C7**. §4 calls (4.2) an "independent numerical check". It is **not
  logically independent**. `pi_*R_pi = D` and `H = pi^* L_infinity`, so
  `H.R_pi = L_infinity.D` by the projection formula; and (4.1) already
  reduces `I_p` to `ord_v disc_z(h)`. It is the *same* computation read on
  the target. Downgrade to "consistency restatement". This matters: a
  reader could otherwise treat `8` as doubly certified when it is certified
  once.

## 5. Item 5 — global inference: `CONFIRM_WITH_CORRECTIONS`

Hypotheses I verified rather than assumed:

* *No boundary component.* Verified **directly in this chart**: `r` is
  nonzero on each of `H_0,Q_1,Q_2` (orders `2,3,3`). Neither branch lies in
  `H`; the promoted lemma is not needed here.
* *Attachment is only at `p`.* `H.R_pi = 8 = I_p(H,R_pi)`, so
  `Rbar cap H = {p}`. No unclassified attachment elsewhere on `H`.
* *`H` resolves to a connected tree.* Connected by `H^1(S,O(-2,-3))=0`;
  tree by `K(C)=2`, saturated at `p` (§1). `CONFIRMED`.
* *Two normalization points.* Two distinct analytic branches of an
  irreducible `Rbar` at `p` give two distinct points of its normalization.
  `CONFIRMED`.
* *Reducibility in case 2.* Each of the two distinct global components
  through `p` is not contained in `H`, so each meets `Y`; `R_red` then has
  at least two components. `CONFIRMED`.
* *Exhaustiveness.* Each branch lies on exactly one irreducible component of
  `Rbar`; same or different is exhaustive. `CONFIRMED`.
* *Nonemptiness.* Cited from the attachment integration §2 (needed so that
  "reducible" is not vacuous).

* **C8** (§5, case 1). The cycle lemma is applied to `H union Q`, but the
  first-leg theorem constrains the resolved boundary of `U`, which is
  `H union Rbar` plus further blowups. Add the (easy but omitted) monotonicity
  step: the dual graph of any embedded resolution of `H union Rbar` contains
  a subdivision of a resolution graph of `H union Q`, and subdivision plus
  vertex/edge addition cannot decrease `b_1`. Without this, (5.1) is a
  non-sequitur about a different graph.
* **C9** (5.2). The displayed hypothesis list is incomplete. It must read:
  `X` smooth **irreducible** of class `2A+3B` in `P2 x P1`; `pi` finite on a
  **neighbourhood of `H`**; `H` reduced; promoted dominant `A2 -> U`
  first-leg hypotheses. And `R_red != empty` must be cited.

## 6. Maximum exact theorem safe to promote

**Theorem (F5 local different).** Let `H subset P1 x P1` be reduced of class
`(2,3)` and type `F5=(0,1)+(1,1)+(1,1)`, with `p` its unique singular point.
Let `X subset P2 x P1` be smooth near `p` with
`X cap (L_infinity x P1) = H`, and `pi = pr_1`. Then there are local
analytic coordinates `(u,v,z)` at `p`, `L_infinity={u=0}`, in which:

1. `H` is cut by a unit times `h = z(z-v)((1+v)z-v)`, and the F5
   configuration is a **single** `PGL2 x PGL2` orbit (stabilizer the
   1-dimensional parabolic `v|->v/(1+tv)`, `z|->z/(1+tz)`): no moduli.
2. After dividing by that unit, `f = h + u g` with `g(0) != 0`;
   `Ohat_{X,p} = C[[v,z]]`; the ideal of `H` is `(h)`; `ord U = 3`.
3. `R_pi = div(f_z|X)` has `in_2 = (z-v)(3z-v)` and hence **exactly two
   reduced smooth transverse branches** `D_tan`, `D_tr` at `p`, with tangent
   lines `z=v` and `3z=v`.
4. `disc_z(h) = v^8` exactly; `I_p(H,R_pi) = 8`; and the split is exactly

   `I_p(H,D_tan) = 5`, `I_p(H,D_tr) = 3`, branchwise `(1,2,2)` / `(1,1,1)`
   against `(H_0,Q_1,Q_2)`, per-component totals `(2,3,3)`.
5. Neither branch is contained in `H`, and `R_pi cap H = {p}`.

Items 1-5 hold for every unit `g`, i.e. independently of all higher
coefficients.

**Corollary (maximum safe composition).** Let `X subset P2 x P1` be smooth
and irreducible of class `2A+3B`, `pi` finite on a neighbourhood of the
reduced `H`, and assume the promoted dominant `A2 -> U` first-leg
hypotheses. Then `H in {F1,F2,F4,F5,F7}` (`F8,F9` by the forest
classification; `F3,F6` by finiteness near `H`), and `R_red` is nonempty
with **at least two irreducible components**.

This promotes no occurrence, no coefficient realization, no map, no block
closure, and no JC2 statement. It does not show `F5` occurs, does not
eliminate reducible ramification, and identifies no target-discriminant
branch.

## 7. Cheapest next finite component-lattice control

The producer proposes enumerating splittings of `R_pi = 2A+B`. The new
local data makes this sharper and cheaper than proposed, because `A|_X` is
nef and `A.C = 0` exactly when `pi` contracts `C`:

Write `C_tan`, `C_tr` for the distinct global components carrying the two
germs (case 2, the only surviving case). Then
`A.C_tan >= 5` and `A.C_tr >= 3`, while
`A.R_pi = 8 = sum m_i (A.C_i)`. Hence **forced**:

```text
m_tan = m_tr = 1,   A.C_tan = 5,   A.C_tr = 3,
every other component of R_pi satisfies A.C = 0.
```

An effective `C` with `A.C=0` is a contracted fibre `{x}xP1 subset X`, i.e.
a common zero of the four coefficient sections — exactly the separate
"affine coefficient zero" client already named in the forest integration
§3. With `K_X = (B-A)|_X` (which reproduces `K_X^2=-1`) and
`R_pi.B = 4`, the residual satisfies `sum n_j = 4 - B.C_tan - B.C_tr`.

So the cheapest gate is: **enumerate pairs of classes
`(gamma_tan, gamma_tr)` in the rank-11 conic-bundle lattice
`<A,B,e_1..e_9>` subject to `A.gamma_tan=5`, `A.gamma_tr=3`,
`gamma_tan+gamma_tr+ (contracted residual) = 2A+B`,
`B.gamma_tan+B.gamma_tr <= 4`, effectivity, irreducibility,
`p_a(gamma) = delta(gamma)` from first-leg rationality via
`p_a = 1 + (gamma^2 + (B-A).gamma)/2`, and independence in the promoted
`Cl(Y)` injection.** This is a bounded integer search with no coefficient
elimination and no CAS; it should be run before any realization test. If it
returns empty, `F5` closes outright; if it returns a short list, each entry
carries a fixed `(5,3)` boundary profile that a later attachment/adjunction
gate can attack individually.

Secondary, also cheap: decide whether `pi` can be globally finite. If yes,
`R_pi = C_tan + C_tr` exactly and `R_red` has exactly two components with
`(A.C, B.C)` summing to `(8,4)` — an even smaller lattice.

## 8. Verdict summary

```text
Item 1  F5 local normal form                CONFIRM_WITH_CORRECTIONS  (C1,C2,C3)
Item 2  f=h+ug, unit, U, two branches       CONFIRM_WITH_CORRECTIONS  (C4)
Item 3  length, disc v^8, split 3+5         CONFIRM_WITH_CORRECTIONS  (C5 material, C6)
Item 4  object typing / norm control        CONFIRM_WITH_CORRECTIONS  (C7)
Item 5  global inference (5.1),(5.2)        CONFIRM_WITH_CORRECTIONS  (C8,C9)
Overall                                     CONFIRM_WITH_CORRECTIONS
```

Nothing is refuted. No `GAP` is opened: every step I could not read off the
producer I was able to close myself (orbit rigidity, `z`-regularity,
finiteness of the intersection numbers, `b_1` monotonicity), and I record
those as required additions rather than as gaps. The one material defect is
**C5**: as displayed, (3.4) names tangent lines and (4.5) then computes with
them, which is false as written. With C5 and C6 applied the `3+5` split is
exact and coefficient-free.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `17425`.
- Body SHA-256:
  `5a77b09861b3e53c480715399d777db58290ce60466cb4485f5c25f1c4f5b035`.
- Frozen basis: `1efd7a76538e3fcdf51b999563262afc40d58947`.
