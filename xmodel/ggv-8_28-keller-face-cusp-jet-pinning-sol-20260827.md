# GGV `8_28`: Keller-face cusp jets pin the generic pole label

Date: 2026-08-27  
Author lane: Sol, `actual_total_g20`  
Verdict: **EXACT BOUNDED JET/PINNING CONTROL; GLOBAL `E_22=1` LIFT OPEN;
NOT A KELLER PAIR; NOT `G2-PSC`**

## 0. Answer

The previous `8_28` mutation cannot be promoted into the Keller subclass by
merely squaring/cubing its `y`-infinity edge.  The exact reason appears one
jet later.  With

\[
 x=t^3X,\qquad y=t^{-1},\qquad f=t^{-8}F,\qquad g=t^{-12}G,
\]

write

\[
 E=12F_XG-8FG_X-t(F_XG_t-F_tG_X).
\]

Then `[f,g]=1` is exactly `E=t^22`.  If

\[
 F_0=H^2,\qquad G_0=H^3,
\]

with `H` squarefree, `E_1=0` forces

\[
 G_1=\frac32HF_1,
\]

and `E_2=0` forces `H|F_1`.  Thus a tempting mutation with
`F_1(c) != 0` at a root of `H` is nonextendable even though it passes the
leading and first bracket cancellations.

There is a sharper fail-closed control at the cusp/tree level.  Two exact,
same-`(t,X)`-support root-sign packets below have `E_0=...=E_21=0` and
different tagged-fibre degeneracy patterns.  They still have `E_22=0`, and
their forced `G_16` corrections contain negative-`y` source monomials.  Thus
they are formal local mutations that a source-honest compiler must reject,
not polynomial pre-counterexamples.

For an actual Keller jet the fibre differential identity

\[
 \frac{d}{dt}(t^{-12}G)=-\frac{t^9}{F_X}
 \quad\text{on }F=a t^8                                      \tag{0.1}
\]

pins `g` finite on every generic branch of this square edge.  Therefore no
generic pole-order mutation of the requested kind exists.  The correct
`G2-PSC`-adjacent carrier here is the fibre/deck-tagged cusp packet
`(U,V,W)`, including its finite residues and source provenance.

## 1. History check and additive boundary

A targeted history and text search found the conceptual approximate-root
proposal already recorded in `xmodel/sol-connections.md` (commit
`11329d236d53a5b466f4b7076857174d557a3f3d`, current SHA256
`3fe165e55704e0a4b5dba3b5968ea995846a81f58b65968fa89521ef8595895c`).
That file proposes enriching a GGV flag by the cusp remainder and paired
residual tower, but it does not contain this edge recurrence, the `E_2`
divisibility obstruction, the fibre ODE, or an executable `(U,V,W)` map.

The prior one-chain control and freeze are pinned at

```text
7647f2f118d4fe9fdd060b9e3e9450b58a62e287a80e942cad6de752a3f34ae8
  xmodel/ggv-8_28-fibre-tagged-newton-eggers-wall-prototype-sol-20260827.md
676bdd3ce960221072f037e7160d457a9d1d64c8e7353891f69e9931ae71149b
  cases/ggv_8_28_fibre_tagged_newton_eggers_wall_prototype_20260827/FREEZE.sha256
```

The transport and global-scope authorities are also pinned by the verifier.
Every artifact here is additive; no earlier control or canonical ledger is
rewritten.  The observed committed HEAD was
`418e413593120d19e15e6546eb50c985f4b1f038`.

## 2. The repaired leading edge retains the native GGV face

Retain the old key

\[
 z=xy^4,\qquad B=x(z-1)^7,
\]

but replace the old non-square/non-cube `y` edge by

\[
 \begin{aligned}
 f_{\rm face}&=B^2-2x^8y^{32}+y^8,\\
 g_{\rm face}&=B^3-3x^{16}y^{60}+3x^8y^{36}-y^{12}.
 \end{aligned}                                           \tag{2.1}
\]

For the maximum-weight convention, the added `f` terms have `(4,-1)`
weights `0,-8`, below the native weight `8`; the added `g` terms have weights
`4,-4,-12`, below the native weight `12`.  Hence

\[
 \operatorname{in}_{4,-1}(f_{\rm face})=B^2,\qquad
 \operatorname{in}_{4,-1}(g_{\rm face})=B^3.             \tag{2.2}
\]

At `y=infinity`, put `H=X^8-1`.  Multiplication by `t^8,t^12`
respectively gives

\[
 F_0=H^2,\qquad G_0=H^3.                                \tag{2.3}
\]

Thus

\[
 3F_0'G_0-2F_0G_0'=0,
\]

which is exactly the leading constant-J cancellation.  The desk verifier
expands (2.1), checks every monomial of both native faces, and recovers (2.3)
without using a copied support list.

## 3. Exact Jacobian recurrence and the first obstruction

The coordinate determinant is

\[
 \det\frac{\partial(x,y)}{\partial(X,t)}=-t.
\]

Direct substitution therefore gives

\[
 [f,g]=t^{-22}E,
 \qquad
 E=12F_XG-8FG_X-t(F_XG_t-F_tG_X).                       \tag{3.1}
\]

For `F=sum_i F_i t^i`, `G=sum_j G_j t^j`, its exact coefficient
recurrence is

\[
 E_n=\sum_{i+j=n}
 \bigl((12-j)F_i'G_j+(i-8)F_iG_j'\bigr).                \tag{3.2}
\]

Let `A=F_1`, `B=G_1`, and set
`D=B-(3/2)HA`.  Exact expansion gives

\[
 E_1=2H(11H'D-4HD').                                    \tag{3.3}
\]

At each simple root of squarefree `H`, a nonzero polynomial solution would
have root multiplicity `11/4`, which is impossible.  Hence `D=0`.

After substituting `G_1=(3/2)HF_1`, the next coefficient is

\[
 \begin{aligned}
 E_2={}&20HH'G_2-8H^2G_2'+6HF_1F_1'
       -\frac{21}{2}H'F_1^2\\
      &+12H^3F_2'-18H^2H'F_2.                           \tag{3.4}
 \end{aligned}
\]

Therefore

\[
 E_2\equiv-\frac{21}{2}H'F_1^2\pmod H.                 \tag{3.5}
\]

Since `gcd(H,H')=1`, `E_2=0` implies `H|F_1`.  Writing
`F_1=Ha`, the unique polynomial second coefficient is

\[
 G_2=\frac32HF_2+\frac38Ha^2.                           \tag{3.6}
\]

This is exactly the second coefficient of the approximate-root expansion
`F^(3/2)`.  The verifier proves (3.3)--(3.6) as identities in a free symbolic
polynomial ring, not at sample values.

### 3.1 Rejected pole mutation

For the native first face coefficient, a tempting same-support mutation is

\[
 F_{1,\lambda}=-14X^{15}+\lambda,\qquad
 G_{1,\lambda}=\frac32H F_{1,\lambda}.                  \tag{3.7}
\]

Both `lambda=13` and `lambda=14` pass `E_1=0`; the latter makes
`F_1(1)=0` and would change the local splitting/pole count if one ignored the
next Jacobian coefficient.  But their exact `E_2 mod H` remainders are
nonzero.  Thus this is a useful fail-closed negative mutation, not a stronger
fidelity witness.

## 4. Two formally extendable cusp packets, rejected by source provenance

The first genuinely useful replacement is root/deck-tagged.  Define

\[
 \begin{aligned}
 S_+&=\tfrac14(3+X-X^2+X^3-X^4+X^5-X^6+X^7),\\
 S_-&=\tfrac14(-1+X-X^2+X^3+3X^4+X^5-X^6+X^7).
 \end{aligned}                                          \tag{4.1}
\]

Both have all eight coefficients nonzero and satisfy

\[
 S_+^2\equiv S_-^2\equiv1\pmod{H}.                     \tag{4.2}
\]

Put

\[
 Q_S=\frac38\frac{S^2-1}{H},\qquad
 F_S=H^2+t^8S,\qquad
 G_S=H^3+\frac32t^8HS+t^{16}Q_S.                        \tag{4.3}
\]

Both `Q_S` are polynomials in `(t,X)` with nonzero coefficients in every
degree `0..6`.  Consequently the two truncated formal pairs have identical
`(t,X)` support:

```text
F: t^0 X^(0..16), t^8 X^(0..7)
G: t^0 X^(0..24), t^8 X^(0..15), t^16 X^(0..6).
```

Exact expansion gives

\[
 E_0=E_1=\cdots=E_{21}=0,
 \qquad E_{22}=0                                       \tag{4.4}
\]

for both packets.  They satisfy every vanishing coefficient required before
the constant-J slot, but do **not** supply that slot.

Their root signs differ.  With

\[
 H=(X-1)(X+1)(X^2+1)(X^4+1),
\]

`S_+` has signs `(+,-,+,+)` and `S_-` has signs `(+,-,+,-)` on the four
rational factors.  On the tagged fibre `a=1`, the degrees of the root sets
where the leading equation degenerates are therefore `7` and `3`.  On the
generic tagged fibre `a=2`, if `q^2=2-S(c)`, then

\[
 \left(q^3+\frac32S(c)q\right)^2=
 \begin{cases}
 25/4,&S(c)=+1,\\
 27/4,&S(c)=-1.
 \end{cases}                                            \tag{4.5}
\]

As formal local packets, identical support and the same coarse `H^2/H^3`
face do not determine the fibre tree or finite residual labels even after all
pre-unit Jacobian coefficients vanish.  The deck-orbit-valued class of
`S mod H` is therefore a necessary local packet field.

But polynomial provenance rejects both examples.  A term `t^16 X^i` in `G`
pulls back to

\[
 x^i y^{3i-4}.
\]

The nonzero `i=0,1` coefficients of both `Q_S` are therefore the forbidden
Laurent terms `y^-4` and `x y^-1`.  This failure is not an accident of the
two displayed sign choices.  Write `S=sum s_iX^i` and
`S^2-1=(X^8-1)q`.  Polynomial source support would require `q_0=q_1=0`,
hence

\[
 s_0^2=1,\qquad 2s_0s_1=0.                              \tag{4.6}
\]

If `S(c)` is `+/-1` at all eight roots, `s_0` is their average.  The equality
`s_0=+/-1` forces every root sign to be the same.  Thus no nonconstant
root-sign mutation survives this bounded polynomial-source window.  The
two packets are valuable mutation tests precisely because a local-only
compiler accepts them while the source-provenance layer must fail closed.

## 5. Why the generic pole order is pinned

On a branch of the fibre `F=a t^8`, implicit differentiation gives

\[
 X'=\frac{8at^7-F_t}{F_X}.
\]

Substituting this and (3.1) into the derivative of `t^-12 G` yields the exact
identity

\[
 t^{13}F_X\frac{d}{dt}(t^{-12}G)=-E.                   \tag{5.1}
\]

For a Keller jet, `E=t^22`, proving (0.1).  At a simple root `c` of `H`, the
local cusp form on a generic tagged fibre has

\[
 H(X(t))=q t^4+O(t^5),\qquad q\ne0,
\]

so `ord_t(F_X)=4`.  Equation (0.1) gives

\[
 \frac{dg}{dt}=O(t^5),\qquad g=g(0)+O(t^6).             \tag{5.2}
\]

Hence every such branch is finite for `g`.  Special fibres where the cusp
discriminant vanishes can change the tree, but they do not license a generic
pole mutation.  This is the requested pinning alternative.

## 6. Minimal `(U,V,W)` provenance map

At every simple root `c`, use the étale local coordinate

\[
 u=H(X).
\]

Formal Morse cleanup and division by the quadratic `F` put the pair in the
bounded cusp interface

\[
 F=u^2+U(t),\qquad G=u^3+V(t)u+W(t),                    \tag{6.1}
\]

with every coefficient still tagged by `(chart,fibre,c,deck orbit,source
monomial)`.  Before cleanup, the first exact map is

\[
 U_1(c)=F_1(c),\qquad
 V_1(c)=\frac32F_1(c),\qquad
 W_1(c)=0.                                               \tag{6.2}
\]

Equation (3.5) forces `U_1(c)=0`.  The weight-eight coefficient is resonant:
`U_8` and `V_8` become independently meaningful cusp data, while weight
twelve supplies the `W` resonance.

The first rootwise coefficient capable of carrying the Jacobian unit in this
support window is

\[
 6H'(c)V_8(c)U_{14}(c)=1.                               \tag{6.3}
\]

For `H=X^8-1`, the exact choice

\[
 U_{14}=X,\qquad V_8=1/48                               \tag{6.4}
\]

passes (6.3) at all eight roots because `XH'=8X^8=8 mod H`.  It does not yet
solve the global coefficient identity: direct expansion gives

\[
 E_{22}=1+\frac{13}{12}H.                               \tag{6.5}
\]

The remaining `H`-multiple is the exact next gap: a higher-`u`/global
polynomial correction must remove it while preserving all earlier
coefficients and the native support walls.  Rootwise residue agreement alone
is not a global Keller lift.

This gives a concrete compiler interface:

```text
exact source pair + chart + fibre + H-factor/deck orbit + F_i/G_i provenance
    -> (U_i(c),V_i(c),W_i(c), discriminant, finite residue, E_i contribution)
```

It is the kind of typed map needed for certificate-sized source pullback and
for the approximate-root proposal already in `sol-connections.md`.  A global
`G2-PSC` theorem would additionally have to construct it on every selected
GGV chain, glue all root/deck packets across both infinity charts, and prove
complete landing.  None of those global steps is asserted here.

## 7. Replay and exact scope

Case directory:

`cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/`

Replay:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_keller_face_cusp_jet_pinning_20260827/verify.py
```

The verifier is standard-library-only and desk scale.  It pins all consumed
sources, expands the two original-coordinate faces, proves the universal
`E_1/E_2` identities in a free symbolic ring, checks the rejected mutation,
constructs both exact formal root-sign packets, verifies every `E_0..E_22`
coefficient stated above, rejects their negative-`y` source pullbacks, and
checks (6.3)--(6.5).

Final status: **the generic pole label is pinned finite; formal paired
cusp/tree residues vary but the displayed mutations fail polynomial
provenance; the global polynomial `E_22=1` lift is open.**  No Keller pair,
counterexample, GGV-to-tree functor, `G2-PSC`, `G2-BD`, or JC2 conclusion is
claimed.
