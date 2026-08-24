# TD6-TWO-CHART-FIRST-BAND — exact shared-coefficient control

Date: 2026-08-24  
Charged clean basis: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`  
Status: **PROVISIONAL PRODUCER / NONEMPTY-WITNESS / STOP**

## Verdict

The smallest fixed-rectangle, two-ended SP-2/r9-M2 control tested here is
**nonempty over `Q`**.  One common pair of global coefficient vectors in the
unchanged rectangles

\[
  f:\ 0\leq i\leq15,\ 0\leq j\leq60,
  \qquad
  g:\ 0\leq i\leq25,\ 0\leq j\leq100
\]

simultaneously has the selected centered x-side boundary, the selected
F1 and r9/M2 leading patterns, and the first required Jacobian coefficient
at both ends.  The exact joint system has rank `3508` in `3602` variables,
hence nullity `94`.

This is only a **finite chart-pattern control**.  The deterministic witness
fails the very next un-imposed Jacobian row in both charts.  It is not a
Keller pair, not a realization of a terminal class, not a full pairing of
Eggers trees, and not evidence for a counterexample.  Its exact conclusion is
negative but useful: this source-typed first-band specialization supplies no
global polynomial obstruction.

## 1. Frozen source-typed specialization

The canonical SP-2 ledger gives

\[
 F_0=(3,6,5,2,8)\longrightarrow
 F_1=(15,60,5,4,4)\longrightarrow(0,y),
\]

with type `(3,5)`, fixed degree rectangles `(15,60)/(25,100)`, a single
x-cluster, `R=4`, and the case-II(a) reduced F1 pattern
`(eta^5-c^5)^2 Pi_2`.  The r9/M2 entry family is, up to units,

\[
 p_0=\zeta(\zeta^5-A),\qquad
 q_0=B\left(\zeta^{10}-{5\over3}A\zeta^5+{5\over9}A^2\right),
 \qquad A B\ne0.
\]

We make the following one-point specialization inside those source types.

### Common x-side centering

Use

\[
 y=s^{-1},\qquad
 x=s+s^2+s^3+t s^4,
 \tag{1}
\]

so the actual centered coordinate is the global polynomial

\[
 T=xy^4-y^3-y^2-y=t.
\]

Thus `(c1,c2,c3)=(1,1,1)` are actual, shared centering coefficients—not a
zero-centering shortcut.  This choice is licensed because SP-2/LR2 requires
all x-side branches to have one common truncation and no split or
characteristic exponent below height four; it does not prescribe the three
common integral-power coefficients.  Nonzero rational choices at levels
one, two, and three remain common to every branch and create neither a split
nor a new characteristic exponent.  The same three constants are used for
both `f` and `g`.  The boundary targets are

\[
 [s^0]f=t^{15},\qquad [s^0]g=t+t^{25}.
 \tag{2}
\]

This licenses the chosen centering; it does **not** prove that every SP-2
realization can or must be normalized to it.

### F1 side and the selected r9 refinement

Put

\[
 x=q^{-5},\qquad y=\eta q,
\]

and choose the case-II(a) reduced polynomial

\[
 P(\eta)=(\eta^5-1)^2(\eta^5-2)
                 \left(\eta^5-{28\over25}\right).
 \tag{3}
\]

The three fifth-power orbit values are nonzero and distinct, the chain orbit
is the squared one, and `deg(P^3)=60`, `deg(P^5)=100`.  We impose

\[
 q^{15}f=P^3+O(q),\qquad q^{25}g=P^5+O(q).
 \tag{4}
\]

Refine the chain orbit by `q=r^5`,

\[
 x=r^{-25},\qquad y=r^5+\zeta r^{17}
 \tag{5}
\]

(the permitted common dead-stretch coefficients at the intervening levels
are specialized to zero).  At `eta=1+zeta r^12`, the first Taylor factor of
`P` is

\[
 L=25(1-2)\left(1-{28\over25}\right)=3.
\]

Choose `A=1/9`, with the transported top scales `L^3=27` and `L^5=243`:

\[
\begin{aligned}
 p(\zeta)&=27\zeta\left(\zeta^5-{1\over9}\right)
           =27\zeta^6-3\zeta,\\
 q_0(\zeta)&=243\left(\zeta^{10}-{5\over27}\zeta^5
                              +{5\over729}\right).
\end{aligned}
\tag{6}
\]

These are a member of the cited r9/M2 family and satisfy exactly

\[
 3p q_0'-5p' q_0=25.                 \tag{7}
\]

The choices `1,2,28/25`, the zero dead stretch, and `A=1/9` are fixed
licensed control parameters.  They are not claimed to be forced by the
terminal ledger.

## 2. Three layers that must not be conflated

### A. Sparse transport spaces

Write

\[
 f=\sum_{i=0}^{15}\sum_{j=0}^{60}a_{ij}x^iy^j,
 \qquad
 g=\sum_{i=0}^{25}\sum_{j=0}^{100}b_{ij}x^iy^j.
\]

The replay compiles exact affine linear equations over `Q` for:

1. holomorphy of `f,g` through `s=0` and the boundary values (2);
2. absence of terms below `q^-15,q^-25` and the exact leading values (4);
3. absence of terms below `r^-3,r^-5` and the exact leading values (6).

The two transport systems separately have

| polynomial | variables | rank | nullity |
|---|---:|---:|---:|
| `f` | 976 | 946 | 30 |
| `g` | 2626 | 2524 | 102 |

Thus both sparse transport spaces are nonempty.  This statement by itself
contains no cross-polynomial Jacobian information.

### B. The shared first Jacobian system

All chart equations use the **same** `a_ij,b_ij`; no local coefficient copy
is introduced.  In chart (1), if

\[
 F=t^{15}+s f_1(t)+O(s^2),\qquad
 G=t+t^{25}+s g_1(t)+O(s^2),
\]

then `dx wedge dy=s^2 ds wedge dt`.  The first possible pole of the global
Jacobian is therefore killed exactly by the 40 coefficient equations in

\[
 f_1(t)(1+25t^{24})-15t^{14}g_1(t)=0,
 \tag{8}
\]

equivalently `[s^-2]J(f,g)=0`.  Thirty-eight of these equations are
independent modulo transport.  The combined rank is

\[
 (946+2524)+38=3508,
 \qquad 3602-3508=94.
\]

At the pole end,

\[
 \det {\partial(x,y)\over\partial(r,\zeta)}=-25r^{-9}.
\]

Equations (6)--(7) make the leading local wedge `-25r^-9`, so transport of
those exact patterns gives `[r^0]J=1` and no negative `r`-powers.  Hence the
nonempty rank computation and the pole ODE together are precisely the
first-Jacobian-band compatibility test; the pole condition is built into the
transport targets rather than counted as 38 additional linear rows.

### C. What is not tied or imposed

There are no untied copies of the 3602 global polynomial coefficients: they
are common to all three substitutions.  What remains outside the test is:

- the 94 free directions of the joint affine space (the frozen witness sets
  every free variable to zero);
- the centering, orbit, dead-stretch, and pole parameters, which were selected
  before the solve rather than quantified or derived from one complete global
  Eggers tree;
- every local coefficient beyond the prescribed boundary/leading patterns;
- every Jacobian coefficient after `[s^-2]` at the x end and after `[r^0]`
  at the pole end;
- other points at infinity, finite-fiber data, mapping degree, landing, and
  all global branch-count conditions required of a counterexample.

Consequently “transport nonempty,” “first Jacobian band compatible,” and
“terminal class realized” are three different assertions.  Only the first
two, for this one specialization, are proved here.

## 3. Exact witness certificate and fail-closed stop

The replay uses `fractions.Fraction`, least-index sparse pivots, and the
deterministic specialization “all free variables = 0.”  It replays every
compiled row exactly, reconstructs the resulting global polynomials, and then
uses a separate sparse polynomial differentiation/substitution path to assert:

\[
\begin{array}{ll}
\text{x chart:}& f,g\text{ have no negative }s\text{-powers, (2) holds,}\
               & J\text{ has no term below }s^{-2},\ [s^{-2}]J=0;\\
\text{F1 chart:}& \text{no term below }q^{-15},q^{-25},\text{ and (4) holds;}\\
\text{pole chart:}& \text{no term below }r^{-3},r^{-5},\text{ (6) holds,}\
               & J\text{ has no negative }r\text{-power,}\ [r^0]J=1.
\end{array}
\]

The reconstructed witness has `441` nonzero terms in `f` and `1160` in
`g`.  Its canonical rational serialization is `44200` bytes with SHA-256

`65ae46524727904e636561c6314d1bf65bc3cb31990de89fccacb007953ddf52`.

The first rows not imposed are already nonzero for this witness:

| next row | result | terms | canonical row SHA-256 |
|---|---|---:|---|
| x side `[s^-1]J` | nonzero | 35 | `93545adb834f9a3a24bf7a30d7bbb0e30f4cfeea7632d7f3ab82944db36db751` |
| pole side `[r^1](J-1)` | nonzero | 2 | `91b086a32d5b268591935b632ce4699d1132f89efd4abc8bbdcb9d5e39346af7` |

Thus the witness proves every claimed finite equation exactly and proves its
own failure to be Keller.  No inference is made from a one-sided formal germ.

## 4. Smallest missing implication and next gate

The immediate missing implication is simultaneous solvability, in the same
fixed rectangles and with the same global coefficients, of the next two
conditions

\[
 [s^{-1}]J=0,
 \qquad [r^1](J-1)=0.                 \tag{9}
\]

Unlike (8), the next x row contains bilinear terms from the first transverse
coefficients.  A successor therefore has to parameterize the 94-dimensional
exact affine transport/first-band space and solve the resulting exact
polynomial system; it must not merely append linear rows.  If that gate is
nonempty, successive paired rows must continue until the full polynomial
identity `J=1` is reached or a contradiction is certified.  Compatibility at
all displayed rows would still need the omitted global Eggers and landing
conditions before it represented a terminal class.

## 5. Reproducibility and JC2 scope

Run:

```text
python3 cases/td6_two_chart_first_band_20260824/replay.py
```

The replay exits zero only after all exact assertions above pass.  Frozen
replay SHA-256:

`c55e213672ebd22cf3e9e8f378ffa857f85c3a54be7ed39e5c956df36ff6e735`.

Canonical stdout SHA-256 (including its final newline):

`06f92eb5cdee0d4b654ab6a27a5e79f4edcd77bcae2ce0cd04b55206e6587a14`.

Charged input bytes at freeze time:

| artifact | SHA-256 |
|---|---|
| `ladder/SHEET6.md` | `fbec069198310c286193be92adbb05eae2a3b7bdf3d317496e4fb4d262358661` |
| `ladder/SHEET6-CAMPAIGN.md` | `fca34f4cad606c9097cdb87c4e9e51609ab5c73d16a03efd764a7c06cdc4ccbb` |
| `ladder/SHEET6-LROOT.md` | `3eb95441c10f375274f8642f2005550e5487477e1b844f9712ea1a48bf220661` |
| `ladder/SHEET6-LT-REVIEW.md` | `82d94e1a43ae9ec315189b4892faafa840027f4f1696dba6a394866331aa22c6` |
| `ladder/SHEET6-AF3.md` | `555363fde61291a0c689bbf9d789c01f73734e0c403d350d85ae2fd0ddab8099` |
| centering-escape producer | `b53064c877a4f0b741f23f036b2323195bef825ccc72b6722b98f1fc2d2eec17` |
| its typography erratum | `efbf05ca2e9f1e13cdc2f6dd67a5510176d6e3e0ce5eb6a0c263046f2ce812dd` |

**JC2 scope:** this report neither proves nor disproves the plane Jacobian
conjecture.  It eliminates one proposed first-band polynomial-compatibility
obstruction for one licensed SP-2/r9-M2 chart-pattern specialization and
isolates the next exact two-ended coefficient gate.  No canonical campaign
file was edited and no AWS work was launched.
