# `8_28` Keller-face R2: rootwise cusp unit-carrier classification with sidecar

Date: 2026-08-27  
Author lane: Sol, `actual_total_g20`  
Status: **EXACT ROOTWISE/FORMAL CLASSIFICATION THROUGH WEIGHT 22;
RAW-PROVENANCE AND GLOBAL SIDECAR IMAGE OPEN; PROVISIONAL PENDING HOSTILE
REVIEW**

## 0. Decisive delta

R1 left one specific completeness question: can arbitrary higher-`u` terms in
the local cusp expansion introduce a third way to carry the constant
Jacobian at weight 22?  They cannot.

At each simple root `c` of `H=X^8-1`, parametric formal Morse normalization
puts the first coordinate in the form

\[
 F=u^2+U(t),\qquad u\equiv H(X)\pmod t,
\]

while the second has the unrestricted expansion

\[
 G=W(t)+V(t)u+Q(t)u^2+\Gamma(t)u^3+O(u^4),
 \qquad \Gamma(0)=1.                                  \tag{0.1}
\]

The exact constant-in-`u` channel is

\[
 C(t)=V(t)(tU'(t)-8U(t)),                              \tag{0.2}
\]

independent of every higher-`u` coefficient.  Its companion `u^2` channel
is enough to prove that the first weight-22 unit carrier is exactly one of

\[
 6V_8U_{14},\qquad \frac92U_{11}^2.                   \tag{0.3}
\]

After restoring the source-coordinate determinant, the rootwise conditions
are

\[
 6H'(c)V_8(c)U_{14}(c)=1                              \tag{0.4a}
\]

when `V_8(c) != 0`, and

\[
 \frac92H'(c)U_{11}(c)^2=1                            \tag{0.4b}
\]

when `V_8(c)=0`.

This closes **rootwise scalar-carrier completeness**, including arbitrary
local higher-`u` sidecars.  It does not classify the global polynomial
`H`-multiple at `E_22`; therefore it does not turn R1's two-ansatz
`M(Y)` obstruction into an `8_28` face exclusion.

## 1. Custody and history check

The additive case is

```text
cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/
```

and pins:

```text
05cbb5c046f9aa4b89e1104448e77fd38ec3a146d2422bf84773f81d668bfe3c
  cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/FREEZE.sha256
66121bddbe0b004ad1b8960f896d3691c4dd3963068fbfddb6ad3ba15dda7027
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-r1-sol-20260827.md
171ff47c844331da8971a731c1ffaf20c31ed5b2ba86fdee2d0d81219eb002b0
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-hostile-review-grok-20260827.md
```

The R0 hostile review confirmed the local determinant carrier and its explicit
global `13H/12` remainder.  R1 then repaired the interpretation of local
`U_14=X`: it is not a direct raw `F_14` source coefficient, and R1 excluded
`E_22=1` only inside two named polynomial ansatzes.  The subsequent
`20260827T1308Z` interface microround routed the still-open work to a typed
quotient-plus-sidecar compiler; it supplied no proof artifact.

Repository search found no prior artifact proving that the two carriers stay
exhaustive in the presence of unrestricted `Q`, `Gamma-1`, and `u^4+` terms.
R2 is precisely that missing local theorem.  R0 and R1 bytes are unchanged.

## 2. Coordinate naturality and determinant unit

Recall the rescaled Keller equation

\[
 E=12F_XG-8FG_X-t(F_XG_t-F_tG_X)=t^{22}.              \tag{2.1}
\]

Fix a simple root `c` and work in the completed local ring over its residue
field.  Since `F_0=H^2` and `H'(c)` is a unit, the parametric formal Morse
lemma gives a formal source coordinate `u` with

\[
 F=u^2+U(t),\qquad u=H(X)+O(t).                        \tag{2.2}
\]

This is root-local and formal.  No global polynomial source automorphism, no
support preservation, and no raw coefficientwise lift is asserted.

Although `u` depends on `t`, its `u_t` terms cancel from the determinant:

\[
 E=u_X L,qquad
 L=12F_uG-8FG_u-t(F_uG_t-F_tG_u),                     \tag{2.3}
\]

where the `t` derivatives in `L` hold `u` fixed.  Since `u_X` is a unit,
`E_0=...=E_{21}=0` implies `L_0=...=L_{21}=0`.  At weight 22,
evaluation at `u=0` gives

\[
 1=u_X(c,0)[t^{22}u^0]L
  =H'(c)[t^{22}u^0]L.                                 \tag{2.4}
\]

The convention `u=H mod t` fixes the local/deck orientation and hence the
sign in (2.4).

## 3. Exact low-`u` channels with unrestricted sidecar

Insert (0.1) into (2.3).  Direct expansion gives

\[
 [u^0]L=V(t)(tU'-8U),                                  \tag{3.1}
\]

\[
 [u^1]L=24W-2tW'+2Q(tU'-8U),                           \tag{3.2}
\]

and

\[
 [u^2]L=16V-2tV'+3\Gamma(tU'-8U).                     \tag{3.3}
\]

Thus, coefficientwise,

\[
 C_n=\sum_{i+j=n}V_i(j-8)U_j,                          \tag{3.4}
\]

\[
 D_n=2(8-n)V_n+3\sum_{i+j=n}\Gamma_i(j-8)U_j.         \tag{3.5}
\]

The quadratic sidecar `Q` affects only (3.2).  `Gamma-1` affects (3.5), but
not the constant channel.  Every coefficient of `u^4` or higher in `G`
misses all three displayed channels.  The exact verifier derives (3.1)--(3.5)
from a generic sparse polynomial ring through `t^22`, rather than checking a
numerical specialization.

## 4. Exhaustion of the first carrier

All assertions in this section are over one geometric simple-root residue
field, so a nonzero coefficient is a unit and has no square-zero escape.

First suppose `U_k` is the earliest nonzero positive-weight coefficient with
`k<8`.  Equation (3.5) first gives

\[
 V_k=\frac32U_k.
\]

Then (3.4) has its first nonzero term at weight `2k`, with coefficient

\[
 \frac32(k-8)U_k^2.
\]

It is nonzero and occurs before weight 22, a contradiction.  Hence
`U_1=...=U_7=0`, and then (3.5) also gives `V_1=...=V_7=0`.

At weight eight, both `U_8` and `V_8` are resonant.  Crucially, `U_8` is
annihilated by `t d/dt-8`; it never enters (3.4) or any convolution in
(3.5).

Let `k>8` be the first index with `U_k != 0`.  Such a `k` must exist because
(2.4) makes `C_22` nonzero.  All earlier nonresonant `V` coefficients vanish,
and (3.5) at the first index gives

\[
 V_k=\frac32U_k.                                      \tag{4.1}
\]

No coefficient of `Gamma-1` can change (4.1): its only possible earlier
partner is `U_8`, whose factor `(8-8)` is zero.

There are now exactly two cases.

1. If `V_8 != 0`, the first constant-channel term occurs at weight `8+k`
   and equals `(k-8)V_8U_k`.  Vanishing below 22 and nonvanishing at 22 force
   `k=14`, giving `C_22=6V_8U_14`.
2. If `V_8=0`, the first constant-channel term occurs at weight `2k` and,
   by (4.1), equals `3(k-8)U_k^2/2`.  The endpoint forces `k=11`, giving
   `C_22=9U_11^2/2`.

Combining with (2.4) proves (0.4a)--(0.4b).  This argument allows arbitrary
`Q`, arbitrary `Gamma=1+O(t)`, arbitrary `u^4+` coefficients, and arbitrary
`U_8`; none produces a third rootwise constant carrier.

## 5. Factor, deck, and conjugation tags

The dichotomy is rootwise, not necessarily global.  In the finite etale
algebra `K[X]/(H)`, `V_8` can vanish on some factors and be a unit on others.
The verifier pins the explicit mixed example

\[
 H=(X^4+1)(X^4-1),\qquad V_8=X^4+1.                   \tag{5.1}
\]

On `X^4+1`, `V_8=0` and the `U_11^2` case applies.  On `X^4-1`, `V_8=2` and
the `V_8U_14` case applies.  A compiler must therefore split by
`gcd(H,V_8)` or equivalent idempotents and retain the root/factor, conjugation,
deck orientation `u=H mod t`, chart, and determinant `H'(c)` in every packet.

## 6. What remains open

R2 proves the local quotient statement needed by the proposed
GGV-to-cusp bridge: once a root-local Morse chart is selected, the packet has
only the two unit-carrier types in (0.4).  It does **not** prove that the
global coefficient at `E_22` is exhausted by R1's operator

\[
 \mathcal M(Y)=4HY'+6H'Y.                              \tag{6.1}
\]

Arbitrary raw `2S/3S` jets can contribute higher-`u` terms whose local
constant channel is already controlled by R2 but whose global multiple of
`H` need not lie in either of R1's two-slot images.  The remaining compiler
must:

```text
raw 2S/3S jets through weight 21
  -> formal Morse cleanup with every raw source coefficient pinned
  -> factor/root/deck-tagged (U,V,Q,Gamma,W,higher-u) packet
  -> one of the two R2 rootwise carrier types
  -> complete global H-multiple / E22 image test.
```

Therefore this artifact proves neither a global typed-normal-form/image
theorem nor an `8_28` face/family exclusion.  It is not a Keller pair, a
counterexample, `G2-PSC`, `G2-BD`, or JC2.

## 7. Replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/verify_r2.py
```

The standard-library verifier rehashes the frozen dependencies, verifies
coordinate-change naturality, derives the generic low-`u` channels through
weight 22, enumerates every possible first carrier order, and checks the
mixed etale-factor fixture exactly.
