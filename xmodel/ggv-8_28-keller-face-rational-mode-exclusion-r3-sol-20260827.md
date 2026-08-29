# `8_28` Keller-face R3: rational-mode normal form excludes the squarefree replacement edge

Date: 2026-08-27  
Author lane: Sol, `actual_total_g20`  
Status: **EXACT PRODUCER THEOREM / PROVISIONAL PENDING HOSTILE REVIEW /
EXCLUDES ONLY THE CHARGED `H^2/H^3` REPLACEMENT EDGE**

## 0. Decisive result

Let `K` be a characteristic-zero field, put `H=X^8-1`, and suppose

\[
 F,G\in K[X][[t]],\qquad F_0=H^2,\quad G_0=H^3.        \tag{0.1}
\]

There is no such polynomial-`X` formal jet satisfying

\[
 E:=12F_XG-8FG_X-t(F_XG_t-F_tG_X)
   =t^{22}+O(t^{23}).                                  \tag{0.2}
\]

The proof supplies the typed-normal-form completeness missing from R1, but
in the rational differential field `K(X)[[t]]`, where it is simplest and
strongest.  Define the branch `F^(1/2)=H+O(t)` and subtract `F^(3/2)` from
`G`.  All homogeneous solutions below weight 22 are exactly

\[
 c_4t^4F+c_8t^8F^{1/2}+c_{12}t^{12}
 +c_{16}t^{16}F^{-1/2}+c_{20}t^{20}F^{-1}.            \tag{0.3}
\]

After subtracting them, the first residual is `t^22 d(X)`.  Equation (0.2)
then becomes

\[
 -20HH'd-8H^2d'=1.                                    \tag{0.4}
\]

Regularity of the right side and squarefreeness of `H` force `d` to have at
most simple `H`-poles.  Hence `d=-Y/(2H)` for a polynomial `Y`, and (0.4) is
exactly

\[
 4HY'+6H'Y=1.                                         \tag{0.5}
\]

No nonzero polynomial `Y` satisfies (0.5): if `deg Y=d`, its left side has
degree `d+7` and leading coefficient `(4d+48)lc(Y)`.  This turns R1's
two-ansatz operator into a complete rational-mode obstruction for this exact
squarefree edge.

This does **not** exclude the original non-Keller `8_28` witness, the entire
GGV `8_28` family, or any other leading-edge type.

## 1. Custody, history, and novelty boundary

The additive exact case is

```text
cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/
```

It pins the frozen R2 rootwise carrier package, the frozen R1 type repair,
and the completed R0 hostile review.  In particular:

```text
453f7821f88add5d97b65cee41fe3a4df225db5768526746cf4ff1431aa73aa6
  cases/ggv_8_28_keller_face_cusp_unit_carrier_classification_r2_20260827/FREEZE.sha256
0f8f3833c8fa16349d52c6d68829e5c86200ab064f84e4172b0ba4039314b733
  xmodel/ggv-8_28-keller-face-cusp-unit-carrier-classification-r2-sol-20260827.md
05cbb5c046f9aa4b89e1104448e77fd38ec3a146d2422bf84773f81d668bfe3c
  cases/ggv_8_28_keller_face_cusp_jet_pinning_r1_20260827/FREEZE.sha256
171ff47c844331da8971a731c1ffaf20c31ed5b2ba86fdee2d0d81219eb002b0
  xmodel/ggv-8_28-keller-face-cusp-jet-pinning-hostile-review-grok-20260827.md
```

R0 proved a rootwise carrier and exposed the global remainder `13H/12`.
R1 corrected the local/raw interpretation and proved the image obstruction
inside two displayed polynomial ansatzes.  R2 proved that arbitrary local
higher-`u` sidecars cannot produce a third rootwise scalar carrier, while
leaving their global `H`-multiple unclassified.

The negative-power modes at weights 16 and 20 are precisely the sidecars
that those polynomial ansatzes did not classify.  R3 includes them, without
pretending they are polynomial source transformations: they are exact
rational identities used inside the proof.  Repository search found no prior
artifact containing this complete six-mode differential-field normal form or
the endpoint pole-order argument.  All earlier artifacts remain immutable.

## 2. Exact linearization

Work in `K(X)[[t]]` and choose the unique formal square root

\[
 S=F^{1/2}=H+O(t).                                     \tag{2.1}
\]

It exists because `F/H^2=1+O(t)` in this differential field.  Put

\[
 R=G-F^{3/2}.                                          \tag{2.2}
\]

Since `F^(3/2)` is a function of `F`, both its weighted derivative and its
Jacobian with `F` vanish.  Thus

\[
 E(F,G)=E(F,R)
 =12F_XR-8FR_X-t(F_XR_t-F_tR_X).                      \tag{2.3}
\]

For every integer `n` and rational exponent `alpha`, direct differentiation
gives

\[
 E(F,t^nF^\alpha)
 =t^nF^\alpha F_X(12-8\alpha-n).                      \tag{2.4}
\]

Consequently

\[
 Z_n:=t^nF^{(12-n)/8}                                  \tag{2.5}
\]

is an exact homogeneous solution whenever its formal coefficients lie in
`K(X)`.  At `t=0`, its leading `X`-coefficient is

\[
 H^{(12-n)/4}.                                         \tag{2.6}
\]

For `0<=n<22`, this exponent is an integer exactly at

\[
 n=0,4,8,12,16,20.                                    \tag{2.7}
\]

The `n=0` mode is the already-subtracted `F^(3/2)`.  The remaining five are
exactly (0.3).  Notice that `n=16,20` give `F^(-1/2),F^(-1)`; excluding them
merely because they lack direct polynomial-source provenance would be
invalid.  They must be retained in the rational normal form.

## 3. Completeness through weight 21

The list (2.7) is exhaustive, not just a supply of examples.  Suppose a
residual `D` has vanished below weight `n`.  Because (2.3) is linear in its
second entry, the coefficient `r_n=[t^n]D` satisfies

\[
 2H\big((12-n)H'r_n-4Hr_n'\big)=0.                    \tag{3.1}
\]

For nonzero `r_n in K(X)`, this is

\[
 \frac{r_n'}{r_n}=\frac{12-n}{4}\frac{H'}H.           \tag{3.2}
\]

Hence `r_n=cH^((12-n)/4)`, with `c` in the constant field.  Since `H` is
squarefree, the valuation of a rational function at each root of `H` is an
integer.  Therefore (3.2) has a nonzero rational solution only when
`(12-n)/4` is integral, exactly the weights in (2.7).

Inductively, at each of those five positive weights choose `c_n` to remove
the leading coefficient by subtracting the exact mode (2.5).  That mode has
no lower `t` terms, while all its higher terms are carried forward exactly.
At every other weight the residual coefficient is forced to zero.  Thus

\[
 \begin{split}
 G={}&F^{3/2}+c_4t^4F+c_8t^8F^{1/2}+c_{12}t^{12}\\
    &+c_{16}t^{16}F^{-1/2}+c_{20}t^{20}F^{-1}
      +t^{22}d+O(t^{23}).                              \tag{3.3}
 \end{split}

This is a differential-field identity, not an allowed source/target cleanup
and not a claim that the individual summands are polynomial.  The original
`F,G` remain polynomial in `X`; the decomposition is used only to expose the
complete kernel of (2.3).

## 4. Endpoint pole lemma

Every term displayed before `d` is an exact zero of (2.3), and the new
residual has no coefficient below 22.  Therefore only `F_0=H^2` enters its
weight-22 equation:

\[
 E_{22}=-20HH'd-8H^2d'.                               \tag{4.1}

The coefficient `d` belongs to `K(X)`.  Moreover all its possible finite
denominators divide a power of `H`: `G_22` is polynomial, and coefficients of
the formal powers in (3.3) are built from polynomial `F_i` by dividing only
by powers of the leading unit denominator `H`.

Let `c` be a simple root of `H`, and suppose

\[
 d=aH^{-m}+O(H^{1-m}),\qquad a(c)\ne0.                \tag{4.2}
\]

The leading term of (4.1) is

\[
 (8m-20)aH' H^{1-m}.                                  \tag{4.3}

For every integer `m>=2`, `8m-20` is nonzero, so (4.1) would have a pole.
Since its charged value is the regular polynomial one, `m<=1` at every
root.  Squarefreeness now gives

\[
 d=-\frac{Y}{2H},\qquad Y\in K[X].                    \tag{4.4}

Substitution into (4.1) yields exactly

\[
 E_{22}=4HY'+6H'Y=:\mathcal M(Y).                     \tag{4.5}

This also explains why the earlier rootwise fixture `Y=X/48` produced

\[
 \mathcal M(X/48)=1+\frac{13}{12}H.                   \tag{4.6}

The target weight is load-bearing: at target 20 the analogous double-pole
coefficient is zero, reflecting the exact `t^20F^-1` homogeneous mode.  At
the charged target 22 it is `-4`, so no such pole survives.  The verifier
includes this mutation.

## 5. No polynomial endpoint

Let `Y` be nonzero of degree `d`.  For `H=X^8-1`, the leading term of
`M(Y)` has degree `d+7` and coefficient

\[
 (4d+48)\operatorname{lc}(Y),                         \tag{5.1}

which is nonzero in characteristic zero.  Thus `M(Y)` cannot be the constant
one.  The zero polynomial maps to zero.  Equation (0.5) has no polynomial
solution, contradicting (0.2).

The theorem actually uses no later `2S/3S` support detail: polynomiality of
the `X`-coefficients, the leading square/cube edge, squarefreeness, and the
charged weight 22 suffice.  In particular, adding more raw coefficients
cannot repair this exact edge.

## 6. Exact scope

Pending hostile review, R3 excludes a polynomial Keller lift whose rescaled
leading edge is exactly

```text
F0=(X^8-1)^2,  G0=(X^8-1)^3,  E=t^22+O(t^23).
```

It strengthens the artificial Keller-compatible replacement used for the
`8_28` fidelity control.  It does not apply to the original non-Keller
witness with `F_0=X^16-1`, does not exclude the whole GGV `8_28` family, and
does not supply the missing general GGV-to-Eggers-Wall typed functor.  It is
not `G2-PSC`, `G2-BD`, a counterexample, or JC2.

## 7. Replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/verify_r3.py
```

The standard-library verifier rehashes all dependencies, enumerates every
rational homogeneous weight through 21, checks the exact mode identity,
replays the endpoint pole coefficients and target-weight mutation, derives
`M`, and tests its leading-degree formula on `Y=X^d` for `0<=d<=64` plus
dense exact polynomials.
