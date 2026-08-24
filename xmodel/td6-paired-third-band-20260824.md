# TD6-PAIRED-THIRD-BAND — exact pointwise obstruction

Date: 2026-08-24  
Charged clean basis: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`  
Status: **PROVISIONAL PRODUCER / K-EMPTY / STOP**

## Verdict

At the explicit complex moduli-zero point isolated by the uniformity gate,
the next centered Jacobian band is impossible.  Let

\[
 K=\mathbb Q[S]/(10S^2-35S+37),
\]

and specialize

\[
 C=1,\qquad D=S-{22\over25},
 \qquad L=3,\qquad A={1\over9}.        \tag{1}
\]

The complete 56-dimensional paired-next-row family from the preceding gate
forces

\[
 \boxed{[s^0t^0]J(f,g)={81\over15625}},               \tag{2}
\]

with zero coefficient on every one of the 56 free parameters.  Exact
Jacobian one would require this coefficient to equal `1`; the residual is

\[
 {81\over15625}-1=-{15544\over15625}\ne0.             \tag{3}
\]

Therefore the third paired-band system is **empty over `K` at (1)**.  The
opposite pole row was also compiled exactly and independently replayed, but
is unnecessary for the emptiness certificate.

This is a pointwise result.  It kills neither the one-dimensional complex
moduli-zero locus nor SP-2, any terminal class, or JC2.

## 1. Input family and exact field

The replay retains without change:

- the SP-2 rectangles `(15,60)/(25,100)`;
- centered chart `y=s^-1`, `x=s+s^2+s^3+t s^4`;
- x boundary `f_0=t^15`, `g_0=t+t^25`;
- zero r9 dead stretch;
- F1 pattern
  \[
    R(z)=(z-1)^2(z^2-Sz+D),
  \]
  with leading values `R(eta^5)^3,R(eta^5)^5`;
- r9 patterns with `L=3,A=1/9`.

The minimal polynomial has discriminant `-255`, so `K` is a genuine
quadratic field.  The source conditions remain exact:

\[
 1-S+D={3\over25}\ne0,
 \qquad 3^8(1/9)^3=9.
\]

As proved in the moduli-uniformity report, `D != 0`, the two roots `U,V` of
`z^2-Sz+D` are distinct, and neither is `1`.  No numerical embedding of `K`
is used.  Elements are stored as exact pairs `a+bS` with rational `a,b` and
reduced by

\[
 S^2={7\over2}S-{37\over10}.
\]

## 2. Previously imposed rows

The replay rebuilds the full shared-coefficient system rather than importing
a local witness:

1. all `6547` first-band transport/Jacobian rows have rank `3508` in `3602`
   global polynomial coefficients and give a 94-dimensional affine family;
2. the complete rows `[s^-1]J=0` and `[r^1](J-1)=0` add rank `38`, leaving the
   exact 56-dimensional affine family used here.

Every original row is replayed coefficientwise over `K`.  The 56 parameters
are then composed back into the same 3602 global coefficients before either
new chart band is compiled.

## 3. The next centered band

Write

\[
\begin{aligned}
 F&=p+s f_1+s^2f_2+s^3f_3+\cdots,\\
 G&=q+s g_1+s^2g_2+s^3g_3+\cdots,
\end{aligned}
\]

where `p=t^15`, `q=t+t^25`.  Since
`dx wedge dy=s^2 ds wedge dt`, the newly tested coefficient is

\[
\begin{aligned}
 [s^0]J={}&f_1g_2'+2f_2g_1'+3f_3q'\\
           &-3p'g_3-2f_1'g_2-f_2'g_1.                \tag{4}
\end{aligned}
\]

The earlier rows already fix `f_1,g_1`, so (4) is affine-linear—not
quadratic—in the 56 survivor parameters.  The exact audit is:

| item | result |
|---|---:|
| possible `t` slots | 40 |
| nonzero affine rows | 35 |
| parameter degree | 1 |
| homogeneous/tangent rank | 25 |
| homogeneous nullity | 31 |

The very first row, degree `t^0`, has no homogeneous part at all and is (3).
Thus the affine system is empty before a pivot is introduced.  Rank `25` and
nullity `31` describe only the homogeneous linear part; the inconsistent
affine system itself has no solution space or nullity.

For an independent certificate, the replay specializes all 56 free
parameters to zero, reconstructs `f,g` in `K[x,y]`, differentiates globally,
and substitutes the centered chart.  It rechecks the two prior negative bands
and recovers (2) directly, without using formula (4).

## 4. The simultaneously compiled pole band

The next pole condition is `[r^2](J-1)=0`.  Write

\[
\begin{aligned}
 F&=r^{-3}p+r^{-2}p_1+r^{-1}p_2+\cdots,\\
 G&=r^{-5}q+r^{-4}q_1+r^{-3}q_2+\cdots.
\end{aligned}
\]

Before division by the exact chart-determinant coefficient `-25`, its local
wedge numerator is

\[
 -3p q_2'-2p_1q_1'-p_2q'
 +3p'q_2+4p_1'q_1+5p_2'q.             \tag{5}
\]

Here the only induced coefficient supports are

\[
 p_1:\{4\},\quad p_2:\{2\},
 \qquad q_1:\{3,8\},\quad q_2:\{1,6\}.
\]

Consequently the actual pole-J row has only the `zeta^1,zeta^6` slots
nonzero.  Its audit is:

| item | result |
|---|---:|
| possible slots retained | 40 |
| nonzero rows | 2 |
| parameter degree | 2 |
| distinct quadratic monomials | 78 |
| tangent rank at the deterministic origin | 2 |

Together with the centered-band derivatives, the tangent rank at that origin
is `26/56`.  These tangent figures do not affect the exact empty verdict,
which comes from the parameter-free row (3).  Independent global
differentiation also reproduces the complete pole `r^2` band and rechecks
`[r^0]J=1`, `[r^1](J-1)=0`.

## 5. Smallest remaining implication

The point (1) is dead, so appending another band there would add no
information.  The smallest meaningful successor is a **moduli-uniform third
band** on

\[
 -2S^2+2S+5D-3=0:
\]

derive `[s^0t^0]J-1` as an exact function on that curve and determine its
remaining zero locus before handling the quadratic pole row.  A nonzero
formula on the whole source-open curve would eliminate this normalized
boundary-pattern control; a new zero would provide the next algebraic point.

Even uniform elimination of this curve would not yet kill SP-2 without
quantifying broader licensed x-boundary data and restoring all omitted global
Eggers, infinity, mapping-degree, and landing conditions.

## 6. Reproducibility and scope

Run:

```text
python3 cases/td6_paired_third_band_20260824/replay.py
```

The replay uses exact rational/quadratic-field arithmetic only.  No modular
probe, floating point, AWS, extra coefficient band, or protected legacy
process is used.

| artifact | SHA-256 |
|---|---|
| third-band replay | `5d05a6de17e3959ad221527ab74c7da77ba1e1980e8a7d86d0fd8cdca10d468a` |
| canonical replay stdout | `3ef256cb1a1afc9d0da1aa4617c4999734e2c05dd6e54da9cbba086b4d4ec8b8` |
| compiled current equations | `c31a6eb89d34985028ddddb4e789941164980618b7fc2dc618e3243afe066103` |
| one-row certificate payload | `e07f7b476308fb5a411835bfa9b739b8ded26c36bbbe1ea4015e8d4d488640e4` |
| imported moduli report | `499e95763759fe195ab1eba5fbf97bfb9d255bbf6fb2b090add938d92f1f3a06` |
| imported moduli freeze manifest | `8d28ce7bc0ca31b51887457e9f5e33537f0ec86d950a6e0e21c78813a78994af` |

**JC2 scope:** `K-EMPTY` applies only to the single algebraic point (1) inside
the fixed normalized SP-2 chart-pattern control.  No uniform curve, terminal
class, or Jacobian-conjecture conclusion is claimed.  No canonical file was
edited.
