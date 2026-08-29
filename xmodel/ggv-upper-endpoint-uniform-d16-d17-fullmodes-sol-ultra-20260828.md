# Uniform full-fixture D16/D17 continuation (independent Sol Ultra desk)

## Result

The frozen D14/D15 characteristic cascade continues exactly through D17,
but D16 does **not** kill the newly born negative mode.  Instead it uniquely
forces `c16`, which can be nonzero.  The next row produces a clean
gauge-invariant successor congruence.

Write

\[
B=F_8-\frac{Y}{2}-\frac{TZ}{8}-\frac{QV}{16}-\frac{R^2}{4},
\qquad
C=F_9-\frac{QR}{2}-\frac{TV}{16}-\frac{YZ}{8}.
\]

The exact D16 Laurent numerator is

\[
g_{16}^{\rm polar}=\frac{\frac38B^2+\frac12c_8B+c_{16}}{A^2}.
\]

Because raw `G16` is polynomial, its numerator must be in `(A^2)`.  Defining
the quotient `M` gives

\[
3B^2+4c_8B+8c_{16}=8A^2M. \tag{D16}
\]

A nonzero scalar cannot lie in `(A^2)`, so this determines `c16` uniquely if
the relation exists.  It does not imply `c16=0`: literal determinant-zero
fixtures give both `c16=3/8` and `c16=-3/8`.

This causal order matters.  The `c16/A^2` term is the weight-16 indicial
kernel, so differentiating D16 cannot determine its constant numerator.  If
one formally carries a free `c16`, its D17 predecessor-mixed contribution is
`+6*c16*A'/A`, while the linked same-row contribution is
`-6*c16*A'/A`; they cancel exactly.  Hence D17 does not independently kill
`c16`.  The raw `G16` polynomial window fixes it through (D16).

The additive `F8` gauge acts by

\[
B\mapsto B+\lambda,\quad
c_8\mapsto c_8-\frac32\lambda,\quad
c_{16}\mapsto c_{16}-\frac12c_8\lambda+\frac38\lambda^2.
\]

In the complete nine-mode coordinates one also has
`c12 -> c12-c4*lambda`.  That mandatory bookkeeping shift has no D16/D17
tail because `F^0` has no positive-weight coefficients; it is nevertheless
retained in the machine result.

Consequently

\[
\widehat B=B+\frac23c_8,
\qquad
J_{16}=c_{16}-\frac16c_8^2
\]

are fixed, and (D16) becomes

\[
\frac38\widehat B^2+J_{16}=A^2M. \tag{D16-centered}
\]

The previously exposed scalar `H0=c8/2+3F8(0)/4` is also fixed and remains
live; no gauge is normalized.

Before using (D16), the entire negative part at D17 factors as

\[
-\frac{\frac38B^2+\frac12c_8B+c_{16}}{2A^4}
+\frac{(\frac34B+\frac12c_8)C}{A^2}.
\]

This explicitly retains the linked `c16` successor and guards against the
kind of dropped-predecessor error that can occur for a forced mode.  Applying
(D16) converts the full `A^{-4}` block to `-M/(2A^2)`, so polynomiality at
D17 is exactly

\[
(3B+2c_8)C-2M=4A^2N. \tag{D17}
\]

Thus the new invariant is

\[
K_{17}^{\rm uniform}=(3B+2c_8)C-2M.
\]

In centered coordinates the rootwise core is

\[
\widehat B(\alpha)^2=-\frac83J_{16},
\qquad
3\widehat B(\alpha)C(\alpha)=2M(\alpha)
\quad(A(\alpha)=0).
\]

This displays the two-valued square-root cover without selecting a root or a
sign pattern; the cover coalesces when `J16=0`.

## Lower polynomial windows

The raw windows `G16[X^2..X^8]` and `G17[X^2..X^7]` omit constants and linear
terms.  The checker therefore extracts four additional exact live equations.
Their constant equations are

\[
\begin{aligned}
C_{16,0}:\quad M_0={}&\frac3{16}Q_0^2T_0+\frac38Q_0R_0Y_0
+\frac3{16}R_0T_0^2+\frac3{64}T_0V_0Y_0
+\frac3{64}Y_0^2Z_0,\\
C_{17,0}:\quad N_0={}&\frac3{16}Q_0^2Y_0+\frac3{16}Q_0T_0^2
+\frac38R_0T_0Y_0+\frac3{128}V_0Y_0^2.
\end{aligned}
\]

The exact linear equations `C16,1` and `C17,1`, including every allowed raw
`F9..F14` jet, are serialized in `RESULT.json`.  All four equations remain
live.  They are not eliminated, normalized, or claimed to exhaust later-row
information.  The earlier `C13,C14,C15` equations and `H0` are carried in the
same result.

## Literal-source custody

The checker pins the authoritative 303-variable/513-generator raw source and
recursively replays the frozen D14/D15 packet.  It records:

- full-rank literal maps for all seven `G16` and six `G17` raw slots;
- a D16 first-failure mutation with quadratic scaling;
- a D17 first-failure mutation with linear scaling after an exact nonzero
  `c16` continuation;
- a second-lift D17 mutation with `K=A*L` but `A` not dividing `L`, proving
  that the full `(A^2)` condition is live rather than an artifact of the
  first reduction modulo `A`;
- two all-row-zero fixtures with `c16=3/8` and `c16=-3/8`;
- three all-row-zero additive-`F8` gauge mutations preserving `Bhat,J16`;
- per-row and per-generator hashes/provenance, with every mutation checked
  against an independent ordinary-polynomial determinant recurrence for all
  513 serialized generators.

## Scope firewall

This packet proves necessary characteristic/polynomial-window consequences at
field points.  It does not prove endpoint emptiness, choose a square-root or
gauge branch, normalize a carrier or unit, or assert that the displayed
uniform invariant specializes to the cutoff-three `K` relation.  That
transport remains a candidate requiring a separate literal map.  Modes
`c18,c20` are retained as mandatory and unconstrained.  No CAS, AWS, or Lean
state was used.
