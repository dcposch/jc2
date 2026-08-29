# `8_28` Keller-face R1: raw-slice typing and the `E_22` image obstruction

Date: 2026-08-27  
Author lane: Sol, `actual_total_g20`  
Status: **EXACT ADDITIVE TYPE REPAIR / TWO UNIT-CARRIER ANSATZES EXCLUDED /
TYPED-NORMAL-FORM COMPLETENESS OPEN**

## 0. Decisive delta

The frozen R0 rootwise identity is correct, but its example

\[
 U_{14}=X,\qquad V_8=1/48
\]

is a **local cusp coefficient**, not a raw polynomial-source coefficient.
The exact `2S` source slice at `n=14` contains only `X^2`; a raw `F_14=X`
term would pull back to `x y^-3`.  R0 did not claim a global lift, and its
bytes remain unchanged.  This additive report makes the type wall explicit.

There is also a clean answer to the attempted `13H/12` repair inside the two
minimal unit-carrier ansatzes.  Every polynomial higher-`u` correction enters
through

\[
 \mathcal M(Y)=4HY'+6H'Y,
 \qquad H=X^8-1.                                        \tag{0.1}
\]

The R0 fixture has `Y=X/48`, hence

\[
 \mathcal M(X/48)=1+\frac{13}{12}H.                     \tag{0.2}
\]

No polynomial `Y` can satisfy `M(Y)=1`: if `deg Y=d`, then

\[
 \deg\mathcal M(Y)=d+7,
 \qquad
 \operatorname{lc}\mathcal M(Y)=(4d+48)\operatorname{lc}(Y). \tag{0.3}
\]

Thus the displayed remainder cannot be cancelled within either the
`V_8 U_14` carrier or the `U_11^2` carrier by a polynomial higher-`u`
correction.

This is not yet an exclusion of the face or family.  The remaining theorem
is precisely typed-normal-form completeness: every raw `2S/3S` jet satisfying
`E_0=...=E_21=0` must be transported, with polynomial provenance, to one of
those two carrier cases.  That theorem is not assumed here.

## 1. Custody

R1 pins the frozen R0 package exactly:

```text
6928428f9cc46641a80275e2bbfa62e784c4290ff041f5089ae789507fa8804f
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/FREEZE.sha256
3e4e608d32c44b1b0208bd5472257ba1dbe4cadf4ef5efb2ace49d3d47d756be
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-sol-20260827.md
ef9acfa90935b32e244367dada67ab35d6454f431f6d43dc35d144b3d08fe46c
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/verify.py
46e1b3434badcea007a914ec71bf60d9758ee76d312dc00d252342d52beed76d
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/RESULT.json
```

No R0 artifact or canonical ledger is modified.

## 2. Exact raw-source slices

The polygon used by the one-chain control is

\[
 S=\operatorname{conv}\{(0,0),(1,0),(8,28),(0,4)\}.
\]

For a raw monomial `x^i y^j`, the substitutions

\[
 F=t^8f(t^3X,t^{-1}),\qquad
 G=t^{12}g(t^3X,t^{-1})
\]

give

\[
 n_F=8+3i-j,\qquad n_G=12+3i-j.                         \tag{2.1}
\]

The four edges of `2S` imply

\[
 \max\left(0,\left\lceil\frac{n-8}{3}\right\rceil\right)
 \le i\le16-n,
 \qquad j=8+3i-n,                                      \tag{2.2}
\]

and the four edges of `3S` imply

\[
 \max\left(0,\left\lceil\frac{n-12}{3}\right\rceil\right)
 \le i\le24-n,
 \qquad j=12+3i-n.                                     \tag{2.3}
\]

In particular,

```text
F_14: i=2 only, hence x^2 y^0;
G_21: i=3 only, hence x^3 y^0;
G_22: empty.
```

The local coefficient `U_14=X` would instead correspond through (2.1) to
`x y^-3`.  It is valid modulo `H`, and therefore valid as a rootwise cusp
fixture, but it has no raw source row of that type.

This distinction also explains why a local Morse/Weierstrass cleanup cannot
be treated as coefficientwise support preservation: lower approximate-root
jets can contribute to `U_14`.  A correct compiler must record the whole
source combination that produces the local coefficient.

## 3. The `V_8 U_14` carrier and all its higher-`u` corrections

Retain the exact R0 normalization `F_0=H^2`, `G_0=H^3`.  The general
polynomial solutions in the two charged slots have the form

\[
 \begin{aligned}
 F_8&=P,& G_8&=\frac32HP+CH,\\
 F_{14}&=A,& G_{14}&=\frac32HA,
 \end{aligned}                                         \tag{3.1}
\]

where `C` is constant.  The `CH` term is the weight-eight cusp resonance;
arbitrary factors divisible by `H` in `P,A` include the higher-`u`
corrections that leave the rootwise data unchanged.

Using the general recurrence

\[
 E_n=\sum_{i+j=n}
 ((12-j)F_i'G_j+(i-8)F_iG_j'),                          \tag{3.2}
\]

the complete cross contribution at `n=22` is

\[
 \begin{aligned}
 E_{22}
 &=6H(PA)'+9H'PA+4CH A'+6CH'A\\
 &=\mathcal M\left(A\left(\frac32P+C\right)\right).   \tag{3.3}
 \end{aligned}

Thus **every** polynomial correction inside this two-slot ansatz changes only
the polynomial `Y=A((3/2)P+C)` in (0.1).  Equation (0.3) proves that none can
turn (0.2) into the constant one.

The fixture `P=0`, `C=1/48`, `A=X` gives `Y=X/48`; its rootwise condition is

\[
 \mathcal M(Y)\equiv6H'Y=1\pmod H,
\]

but global equality retains `13H/12`.  Rootwise inversion of `H'` is
therefore necessary but not sufficient.

## 4. The alternative `U_11` self-carrier

If the weight-eight resonance is absent, the first local scalar cusp term
that can hit the unit slot by self-interaction is weight eleven:

\[
 F_{11}=A,\qquad G_{11}=\frac32HA.                       \tag{4.1}
\]

Its exact quadratic contribution is

\[
 E_{22}=6HAA'+\frac92H'A^2
       =\mathcal M\left(\frac34A^2\right).              \tag{4.2}
\]

The same degree obstruction (0.3) therefore excludes a polynomial unit in
this ansatz as well.  Modulo `H`, the necessary root condition is the R0
congruence

\[
 \frac92H'(c)A(c)^2=1,
\]

but no polynomial representative can upgrade it to global equality through
(4.2).

## 5. Why these are the two local scalar carriers

In the local cusp quotient, write

\[
 F=u^2+U(t),\qquad G=u^3+V(t)u+W(t).
\]

The coefficients of `u^2,u,1` in `E/H'` are

\[
 \begin{aligned}
 &(16V-24U-t(2V'-3U'))u^2,\\
 &(24W-2tW')u,\\
 &V(t)(tU'-8U).                                         \tag{5.1}
 \end{aligned}

Hence

\[
 (8-n)(2V_n-3U_n)=0,                                   \tag{5.2}
\]

and `W` has only its weight-twelve resonance.  After the lower common-root
jets and the uniform weight-eight fibre translation are cleaned:

- if the independent `V_8` resonance is nonzero, every `U_9,...,U_13` would
  create a forbidden coefficient before weight 22, so the first unit carrier
  is `V_8U_14`; and
- if `V_8=0`, the first nonzero `U_9` or `U_10` creates a forbidden square at
  weights 18 or 20, while `U_11^2` lands exactly at weight 22.

This is an exact local scalar classification.  It is **not yet** the required
global typed-normal-form theorem: raw polynomial jets may contain higher-`u`
terms, root-dependent cleanups, and deck-gluing data whose transport into
(5.1) must be proved rather than assumed.

## 6. Next theorem/compiler

The highest-leverage next step is a fail-closed finite compiler:

```text
raw F_n/G_n in the exact 2S/3S slices, n<=21
  -> approximate-root cleanup with every source coefficient pinned
  -> per-H-root/deck (U_n,V_n,W_n) plus global polynomial representatives
  -> proof that E_0..E_21=0 lands in V8*U14 or U11^2
  -> E_22 image test under M.
```

A PASS would turn (0.3) into a bounded face exclusion.  A failure must print
the first raw higher-`u` term outside the two cases; that term would be the
missing field in the proposed GGV-to-cusp packet.  Until this compiler or an
equivalent theorem is reviewed, no family exclusion is licensed.

## 7. Replay and scope

Replay:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/verify_r1.py
```

The standard-library verifier rehashes R0, derives every raw slice in
(2.2)--(2.3), replays (0.2), verifies (3.3) and (4.2) on exact dense
polynomials, and checks the leading-term obstruction mechanically.

Exact scope: **raw-source type repair plus exclusion of polynomial correction
inside the two named normalized carrier ansatzes.**  Typed-normal-form
completeness, the full `8_28` face/family, a Keller pair, a counterexample,
`G2-PSC`, `G2-BD`, and JC2 remain open.
