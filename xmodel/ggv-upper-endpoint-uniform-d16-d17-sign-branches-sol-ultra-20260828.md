# Uniform D16/D17 degree and sign-branch classification

## Exact classification

The authoritative raw windows and the preceding cascade give

\[
\deg(Z,V,R,Q,T,Y)\le(6,5,4,3,2,1),
\qquad \deg\widehat B\le8,
\qquad \deg C\le7.
\]

Here `A=X^4-1`, and the frozen D16/D17 equations are

\[
\frac38\widehat B^2+J_{16}=A^2M,
\qquad
3\widehat B C-2M=4A^2N. \tag{1}
\]

### The nonzero-J sheet

Assume `J16!=0` and adjoin a nonzero `rho` satisfying

\[
\rho^2=-\frac83J_{16}.
\]

Then (1) says `(Bhat/rho)^2=1 mod A^2`.  Over the splitting field, each of
the four double local factors at `1,-1,i,-i` has exactly the two square roots
`+1,-1`.  Hence there are exactly 16 unique degree-`<8` Hermite lifts
`E_s`, characterized by

\[
E_s(\alpha)=s_\alpha,\qquad E_s'(\alpha)=0
\quad(\alpha=1,-1,i,-i).
\]

The degree bound then gives

\[
\widehat B=\rho E_s+\lambda A^2. \tag{2}
\]

Put

\[
D_s=\frac{E_s^2-1}{A^2},\qquad
R_s=\operatorname{rem}(E_sD_s,A^2),\qquad
T_s=\frac{E_sR_s-D_s}{A^2}.
\]

Exact substitution into (1), with no division by a carrier, yields

\[
\begin{aligned}
C&=\frac{\rho}{4}R_s+\frac{\lambda}{2},\\
M&=\frac38\rho^2D_s+\frac34\rho\lambda E_s
  +\frac38\lambda^2A^2,\\
N&=\frac3{16}\rho^2T_s+\frac3{16}\rho\lambda R_s
  +\frac3{16}\lambda^2.
\end{aligned} \tag{3}
\]

The displayed `C` is the unique degree-`<8` representative; this uniqueness
uses the source bound `deg C<=7`.  Simultaneous
`E_s -> -E_s, rho -> -rho` leaves (2)--(3) unchanged, leaving eight systems
up to this global-sign bookkeeping.  The machine result records all 16
polynomials over `Q(i)`, rather than discarding a sheet.

### The collision sheet

If `J16=0`, D16 gives `A^2 | Bhat^2`.  Squarefreeness of `A` implies
`Bhat=A*L` and `M=3L^2/8`.  Reducing D17 modulo `A` then gives `A|L^2`, so
again by squarefreeness `A|L`.  The degree bound forces

\[
\widehat B=\lambda A^2,qquad M=\frac38\lambda^2A^2.
\]

D17 now permits arbitrary `deg(C)<=7`, with

\[
N=\frac34\lambda C-\frac3{16}\lambda^2.
\]

Thus the zero-J sheet is not obtained by choosing one of the nonzero square
roots; it is a distinct collision stratum with a freer `C`.

## Lower-window test

For every one of the 16 nonzero-J lifts, the checker substitutes (2)--(3)
into the exact live equations

```text
F9[X0] absence; C13; C14; C15;
G16[X0]; G16[X1]; G17[X0]; G17[X1].
```

Two useful branch-interface identities are

\[
\begin{aligned}
H_0={}&\frac34\left(\rho E_s(0)+\lambda
 +\frac{Y_0}{2}+\frac{T_0Z_0}{8}
 +\frac{Q_0V_0}{16}+\frac{R_0^2}{4}\right),\\
0={}&\frac{\rho}{4}R_s(0)+\frac{\lambda}{2}
 +\frac{Q_0R_0}{2}+\frac{T_0V_0}{16}
 +\frac{Y_0Z_0}{8}.
\end{aligned}
\]

The first carries the gauge-invariant `H0`; the second is the missing
constant slot of raw `F9`.  Exact formulas for `C1,M0,M1,N0,N1` are also
substituted before the four G16/G17 equations are serialized.

No one of the 16 resulting systems contains an immediate nonzero literal
constant, including after remembering `rho!=0`.  Therefore the finite cover
does not itself close a branch.  It has nevertheless replaced two polynomial
congruences by eight explicit small scalar systems suitable for exact
elimination or hand analysis.  A nonunit result would not prove existence.

## Regression controls and scope

Three exact mutations are live:

- using only value interpolation and dropping the Hermite derivative
  conditions passes modulo `A` but fails modulo `A^2`;
- reversing the sign of the `rho*R_s/4` term in `C` leaves a nonzero D17
  residue modulo `A^2`;
- on `J16=0`, stopping at `Bhat=A` passes D16 but gives the nonzero D17
  residue `-3/4 mod A`.

This is a splitting-field classification without a chosen root, gauge,
carrier, or unit.  Global-sign pairing is bookkeeping, not a quotient of the
actual cover.  The lower systems have not undergone a Groebner elimination.
No literal map to the cutoff-three `Q0*(b_bar*Q0+L0^2)` invariant is asserted
here; that comparison requires its own source-tracked transport.  No CAS,
AWS, or Lean state was used.
