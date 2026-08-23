# Algebraization kill audit for the residue-A window

Date: 2026-08-16.  Exact checkers:
`cases/sol_algkill.py`, `cases/sol_algkill_q2.py`.

## Executive verdict

The global question is **not decided**: no point of the D23 window has yet
been proved to exist, and neither an algebraizing Keller pair nor a unit-ideal
certificate for the whole window is known.

Three sharper conclusions are proved here.

1. **Bounded algebraicity cannot kill D23.**  Every allowed D23 pole prefix
   extends to a polynomial relation in the full residue-A support rectangle
   $(\deg_x,\deg_y)=(42,126)$, and the recorded g-orbits simultaneously extend
   to one in $(63,189)$.  Primitive exact-degree versions preserve every
   coefficient through level 54.  Thus the forced low tails, the six no-log
   pins, and the $-42$ Row-20 inhomogeneity impose no Hermite--Padé
   obstruction at this depth.
2. **Row 24 is not a new principal resonance.**  Its exact first-occurrence
   symbol on the ten effective frontier tails has rank 4, just as in the
   stable post-Row-12 regime.  The $b_2$ information can only enter the
   nonlinear compatibility residual.  No Row-24 kill has been proved.
3. **The literal banked B-zero window is disjoint from the Q2-l12 tier.**
   On leaf 11, four Q2 quotient rows have an exact characteristic-zero
   combination equal to a nonzero multiple of the saturated variable
   `s1F`; hence that ordinary ideal is the unit ideal.  Leaves 12 and 13
   are already domain-disjoint from $B=0$, and the origin is the banked
   empty l13 stratum.  This is a genuine cross-family elimination, but its
   scope is $V_{\rm bank}\cap Q2_{l12}$, not all residue A.

The useful next junction is therefore mixed, not algebraicity alone: finish
the finite Row-24--41 compatibility ladder, add the x-side at Row 42, and
intersect the remaining Q2 strata.  For the canonical orbit completions
below, the first separate support equations occur naturally at root levels
$81/82$ (formal Rows 49/50), but that threshold is not uniform over the still
unconstructed B-side partitions.

## 1. Scope and the membership-direction correction

The object actually banked in `SHEET6-DIRECTIONB.md` section 6 is

\[
 V_{\rm bank}=V_{J,D23}\cap\{B_{D21}=0\},
\]

where `B_D21=0` means the 100 B-side registry coefficients through level 52.
The six live level-42 no-log variables are also zero.  This is a finite
formal window; its nonemptiness was explicitly left open in section 6.V.
Restoring B-side variables gives a larger object and can only make a
row-growth kill harder.

There is also an orientation error in the proposed $\eta^0$ membership test.
Let

\[
 e_0=\operatorname{Row}_{20}[\eta^0]+42.
\]

Then $e_0$ is itself a generator of the J-window ideal.  Thus
$e_0\in I_J$ with the one-term certificate $e_0=1\cdot e_0$; the exact
unit-pivot compression does not change that fact after pullback/localization.
This membership says nothing new.

For set-theoretic novelty the correct tests are:

- whether $e_0\in\sqrt{I_{Q2}}$ on a Q2 chart, if asking whether the J row
  cuts that Q2 chart; or
- whether a Q2 generator belongs to $\sqrt{I_J}$, if asking whether Q2 cuts
  the J-window.

Ordinary nonmembership alone is insufficient: $x\notin(x^2)$, although
adding $(x)$ does not change the zero set.  Section 4 avoids this distinction
entirely by proving that the relevant saturated ordinary ideal is already
the unit ideal.

## 2. Bounded algebraicity is invisible at D23

Put $R=K[[T]]$, with $v(T)=1$, over a characteristic-zero field containing
the template radicals and a primitive 42nd root of unity.  The following
elementary form of clustered Hensel lifting is the main tool.

### Lemma 2.1 (clustered truncation/Hensel lemma)

Let $a_1,\ldots,a_n\in TR$ be pairwise distinct and

\[
 H(T,Y)=\prod_{j=1}^n(Y-a_j).
\]

For a fixed $i$, set

\[
 \lambda_{ij}=v(a_i-a_j),\qquad
 d_i=\sum_{j\ne i}\lambda_{ij},\qquad
 L_i=\max_{j\ne i}\lambda_{ij}.
\]

Suppose that $P\in R[Y]$ is monic of degree $n$ and
$P-H\in T^eR[Y]$.  If $e>d_i+L_i$, then $P$ has a unique root
$b_i\in a_i+T^{e-d_i}R$.  The roots obtained for different $i$ are
distinct.  If a finite group fixes $P$ and permutes the $a_i$, it
permutes the $b_i$ with the same labels.

#### Proof

Write

\[
 a_i-a_j=T^{\lambda_{ij}}u_{ij},\qquad u_{ij}\in R^\times,
 \quad q_i=e-d_i>L_i.
\]

After putting $Y=a_i+T^{q_i}Z$,

\[
\begin{aligned}
H(T,a_i+T^{q_i}Z)
 &=T^{q_i}Z\prod_{j\ne i}
   \left(T^{\lambda_{ij}}u_{ij}+T^{q_i}Z\right)\\
 &=T^e ZU_i(T,Z),
\end{aligned}
\]

where

\[
 U_i(T,Z)=\prod_{j\ne i}
 \left(u_{ij}+T^{q_i-\lambda_{ij}}Z\right)
 \equiv \prod_{j\ne i}\bar u_{ij}=:u_i\ne0\pmod T.
\]

Write $P-H=T^eQ(T,Y)$.  Dividing the root equation by $T^e$ gives

\[
 \Psi_i(T,Z)=ZU_i(T,Z)+Q(T,a_i+T^{q_i}Z)=0.
\]

Modulo $T$, this is $u_iZ+Q(0,0)$, with one simple root.  Ordinary
Hensel lifting supplies a unique $z_i\in R$, and
$b_i=a_i+T^{q_i}z_i$ is the required root.  Since both corrections have
valuation strictly larger than $\lambda_{ij}$,
$v(b_i-b_j)=\lambda_{ij}$; hence the roots remain distinct.  Equivariance
follows from uniqueness in each ball.  In particular, a 21-orbit with even
support remains a 21-orbit.  $\square$

### Theorem 2.2 (D23 surjectivity of the bounded-relation incidence)

Every assignment of the allowed P1/P2 residue-A coefficients through level
54 extends to 126 series satisfying a nonzero polynomial relation supported
in

\[
 0\le i\le42,\qquad 0\le j\le126.
\]

The analogous assertion holds simultaneously for the recorded 189 g-series
and support $0\le i\le63$, $0\le j\le189$.  The relations can be chosen
Gauss-primitive in $K[x][Y]$, of exact bidegrees $(42,126)$ and $(63,189)$,
while preserving every series coefficient through level 54.

Consequently, the separate $f$- and $g$-Hermite--Padé rank-drop incidences
project surjectively onto the D23 coefficient space.  In particular they
impose no polynomial equation on $V_{\rm bank}$.

#### Proof: the f-side

Extend the prescribed P1/P2 series arbitrarily through level 80.  Choose the
same classical-ledger-compatible B completion used in
`SOL-ALGEBRAIZATION.md`,

\[
 Y_B=\beta T^{12}+T^{56}+T^{57},\qquad \beta^7=3/2.
\]

For the three 42-orbits form

\[
 H_f(T,Y)=\prod_{r\in\{P1,P2,B\}}\prod_{k=0}^{41}
       \bigl(Y-Y_r(\zeta^kT)\bigr).
\]

The substitution $T\mapsto\zeta T$ permutes its roots, so, with
$S=T^{42}$,

\[
 H_f(T,Y)=\widehat H_f(S,Y).
\]

Let $P_f$ be the truncation of $\widehat H_f$ modulo $S^{43}$.  Then
$P_f(T^{42},Y)-H_f(T,Y)\in T^{1806}R[Y]$.  The contact multisets,
computed only from the pinned levels, are

| root type | contacts with the other 125 roots | $d$ | $L$ | $1806-d$ |
|---|---:|---:|---:|---:|
| P1 or P2 | $114@12,10@32,1@37$ | 1725 | 37 | 81 |
| B | $120@12,4@56,1@57$ | 1721 | 57 | 85 |

For a P root, the 114 first contacts are the other A-directions together
with all B roots; inside its $T$-level-12 direction, ten roots separate at the
two $\alpha$ directions and its final pole twin separates at level 37.  For a
B root, level 56 gives the order-three split and level 57 the remaining
twin.  Lemma 2.1 therefore produces all 126 roots of $P_f(T^{42},Y)$,
preserving the P prefixes through level 80 and the B prefixes through level 84.

Now set

\[
 F(x,Y)=x^{42}P_f(x^{-1},Y).
\]

This is a polynomial with the required support, and
$F(T^{-42},b_i(T))=0$.  The monomial $x^{42}Y^{126}$ is present.  If a
primitive exact-degree representative is desired, add a generic allowed
term $\lambda S^{42}Y^2$ before substituting $S=x^{-1}$.  It supplies a
nonzero $x^0Y^2$ coefficient, so the $K[x]$-content is one while the
terms $x^{42}Y^{126}$ and $x^0Y^2$ force the exact bidegrees.  At a root
of valuation 12, this perturbation has valuation $42\cdot42+24=1788$.
The first corrections therefore occur at levels

\[
 1788-1725=63\quad(P1/P2),\qquad
 1788-1721=67\quad(B),
\]

both beyond D23.  The same rescaled proof as Lemma 2.1 applies because these
corrections still lie beyond every contact radius.

#### Proof: the g-side

Use the registry orbit sizes

\[
 42,42,21,21,42,21
\]

for `Gp1,Gp2,G0p1,G0p2,GB42,GB21`.  Complete the two frozen B-generators
after the window by

\[
 Z_{B42}=\beta T^{12}+cT^{55},\qquad
 Z_{B21}=\beta T^{12}+dT^{56},\qquad cd\ne0;
\]

the second series has even support.  Form the 189-root invariant product and
truncate it modulo $S^{64}$, so $e=2688$.  The exact contact table is

| root type | contacts with the other 188 roots | $d$ | $L$ | $2688-d$ |
|---|---:|---:|---:|---:|
| any A-side g root | $171@12,15@32,2@37$ | 2606 | 37 | 82 |
| GB42 | $180@12,8@55$ | 2600 | 55 | 88 |
| GB21 | $180@12,6@55,2@56$ | 2602 | 56 | 86 |

Indeed a fixed A level-12 direction contains 18 roots; the other two roots
in its alpha cell split at 37, the other 15 at 32, and the remaining 171 at
12.  A fixed B direction contains six GB42 and three GB21 roots, giving the
last two rows.  Lemma 2.1 gives the desired algebraic g-series.  With

\[
 G(x,Y)=x^{63}(\widehat H_g\bmod S^{64})(x^{-1},Y),
\]

the support is $(63,189)$.  Adding a generic $S^{63}Y^2$ makes it
primitive and exact-degree.  Its value at a seed root starts at level 2670,
so the corrections start at levels $(64,70,68)$, respectively, again all
beyond D23.  This proves the theorem.  $\square$

### 2.3 What the theorem does and does not say

This explains the promoted fixed-completion full-rank experiment.  That
experiment evaluated the uncorrected series with nearly every later tail
set to zero.  The algebraic completion constructed above begins changing
the P roots at level 81 and the B roots at level 85, so it lies outside that
fixed completion while having exactly the same low prefix.

The theorem is stronger than a dimension heuristic: it gives an extension
for every D23 prefix.  It also shows why the $-42$ cannot be an algebraicity
obstruction at this tier.  The $-42$ is a joint f/g differential condition;
each joint prefix satisfying it still has both separate algebraic lifts.

It does **not** construct a Keller pair.  The two relations need not be
irreducible or smooth and need not satisfy the later tower equations or
$J(F,G)=1$.  There is also no arithmetic coefficient-height bound over
the complex numbers beyond the proved degree/support bounds.  Finally, the
B-side post-prefix tree is unconstructed; the levels 81/82 are the natural
first support junctions for the completions just used, not a universal
threshold for every possible B partition.

## 3. Higher rows: exact law, Row 24, and the ceiling

### Proposition 3.1 (the $C_6$ grading law)

For every pure-y J row, a nonzero coefficient
$\operatorname{Row}_k[\eta^q]$ satisfies

\[
 k\equiv 2(q+1)\pmod 6. \tag{3.1}
\]

In particular every odd row vanishes identically.

#### Proof

Let $\omega=\zeta^7$, of order six.  In a through-direction size-42
block, an $\eta^n$ coefficient selects $r=6-n$ root-series terms.  If
their total relative slot is $s$, cycling the six roots multiplies the
term by

\[
 \omega^{\sum_a(32+s_a)}.
\]

The selector sum is nonzero only when $2r+s\equiv0\pmod 6$, equivalently
$s\equiv2n\pmod 6$.  A size-21 block has three roots and even levels; its
order-three selector gives the same congruence.  In an off-direction $\Delta$
block, the Newton power sums retain slots divisible by six, while each
$\eta t^{20}$ insertion contributes $20\equiv2\pmod 6$.  Products
preserve the weight.  Finally, $\eta$ differentiation in the J operator lowers
the $\eta$ degree by one, yielding (3.1).  $\square$

The registry adds four ordinary `tf/tg` tails at every absolute level and
two `tg0` tails at every even level.  Thus every six new levels add exactly

\[
 6\cdot4+3\cdot2=30
\]

P/G variables.  For even $12\le k<42$, the effective first-occurrence block
has ten variables: four odd tails at level $k+27$, first seen by pairing
with the fixed pole slot 5, and six even tails at level $k+32$, seen
directly at jet slot $k$.

This is not, by itself, a proved 29-equation periodicity law.  Off-direction
$\eta t^{20}$ insertions can raise the $\eta$-degree later in the pure-y
window; the exact congruence (3.1) survives, but a uniform top-degree
cancellation for every nonlinear frozen-B row has not been proved.  The
banked rows through 22 show the $(9,10,10)$ component cycle, and the exact
Row-24 frontier has nine components, but extrapolating that count forever
would be a conjecture.

As a guarded computational census, two primes and three generic seeds agree
that Rows 24,26,...,40 have respectively

\[
 9,10,10,9,10,10,10,10,10
\]

components: 88 equations against 90 first-occurrence variables.  The no-log
pins remove the otherwise present Row-30 $\eta^{29}$ term, while an
$\eta^{29}$ term returns at Row 36 through unpinned level-48 discrepancies.
This is evidence against an equation-growth kill in the remaining pure-$y$
window, not a characteristic-zero theorem and not an existence proof.

### Proposition 3.2 (exact Row-24 first-occurrence symbol)

On the B-frozen chart, the Row-24 frontier is

\[
\begin{split}
&\mathit{tf1}_{51},\mathit{tf2}_{51},\mathit{tg1}_{51},\mathit{tg2}_{51},\\
&\mathit{tf1}_{56},\mathit{tf2}_{56},\mathit{tg1}_{56},\mathit{tg2}_{56},
 \mathit{tg01}_{56},\mathit{tg02}_{56}.
\end{split}
\]

Its exact nine-by-ten symbol, on $\eta$ powers $2,5,\ldots,26$, has rank four
over the étale coefficient algebra, uniformly on all $h$-sign branches and
all nonzero pole-scale fibers.  It factors polewise as

\[
 A_i^{\rm odd}(\eta)
 \left(w_i\,\mathit{tf}_{i,51}-{2\over3}\mathit{hw}_i\,\mathit{tg}_{i,51}\right)
 +A_i^{\rm even}(\eta)
 \left(\mathit{tf}_{i,56}-{2\over3}\mathit{tg}_{i,56}
       -{1\over3}\mathit{tg0}_{i,56}\right),
 \tag{3.2}
\]

for $i=1,2$, with the four displayed $A$-vectors independent.  Unit
pivots may be taken in `tf1_51,tf1_56,tf2_51,tf2_56`.

#### Proof

Pin every older free coefficient to zero, retaining only the ten variables
above, and build the depth-25 products with the full exact variable-degree
cap 25.  This computes the true first-occurrence symbol, not a differential
approximation: a level-56 tail can pair only with slot zero, while a
level-51 tail first appears with the fixed slot-5 pole coefficient; no older
free can enter either coefficient.  Direct raw-ring comparison gives the
ratios in (3.2).  Exact unit-pivot elimination gives rank four and no
leftover on all four sign branches and at pole scales $(1,1)$, $(2,3)$, and
$(1/5,7)$; the factorization shows the scale-uniform statement.  The
canonical 90-entry symbol has SHA-256
`ab5ee038b118ba6d0b6303c6b2b55b110dc9872c203e1c6b2d60044458e69d29`.
$\square$

For a fixed D23 point, the four level-51 values are already recorded dummy
coordinates, so only the six new level-56 variables remain adjustable and
their sub-symbol has rank two.  Row 24 can therefore impose as many as seven
compatibility conditions on that fixed point.  For the existential problem
over all of $V$, the level-51 controls participate and the nine-component
symbol leaves at most five compatibility residuals.  **No computation here
shows that those residuals vanish or are inconsistent.**

Nor is 24 a resonance of the lead operator from `xmodel/sol-thmB.md`:

\[
 L_k(h)=-2p\left(6ph'+(k-18)p'h\right).
\]

A polynomial homogeneous solution has $h\propto p^{(18-k)/6}$, so the
polynomial resonant indices are $(0,6,12,18)$.  At $k=24$ the exponent is
$-1$.  The template's $h_2/b_2$ datum may occur in the nonlinear Row-24
source after lower-row reduction, but it does not create a principal-symbol
rank drop.

The no-log pins do not change this conclusion: they concern only the six
level-42 variables.  Also, the current pure-y identity stops at Row 41;
Rows 42 and above require the x-side factors.  Therefore the present builder
cannot support a claim about conditions “forever.”

### Proposition 3.3 (an all-orders scheme kill is finite)

Let $I_\infty$ be the ideal generated by every row coefficient, pin, and
template relation in the polynomial ring on all formal coefficients,
including Rabinowitsch variables for required units.  If
$1\in I_\infty$, then $1\in I_N$ for some finite depth $N$.

#### Proof

An ideal-membership identity

\[
 1=\sum_j a_jf_j

\]

is, by definition, a finite sum.  Only finitely many row generators occur,
so they all lie below one finite depth.  Conversely, if every finite-depth
ideal is proper, their increasing union is proper and is contained in a
prime ideal, giving a compatible formal point over the prime's residue-field
extension.  $\square$

Thus “infinite codimension” is not an emptiness proof: the ideal
$(u_1,u_2,\ldots)$ has infinite codimension and still has the origin.  For
bounded-support polynomial pairs the ambient coefficient ring is finite
type, making finite detection still more direct.  A higher-row attack must
produce a concrete finite inconsistency; asymptotic growth alone cannot kill
$V$.

## 4. The Q2-l12/B-zero certificate

This section uses the correctly oriented cross-family question and yields
an actual, though sector-limited, kill.

On Q2 leaf 11 let $Q_n$, for $n=2,9,16,23$, denote the quotient rows

\[
 Q_n=W_F(n,60)-s_{1F}c_n,
\]

where

\[
 \sum_m c_{7m+2}U^m=(U-1)^{16}(U-3/2)^8.
\]

### Theorem 4.1 (the literal B-zero l12 tier is empty)

After setting exactly the 100 D21 B coordinates to zero, the exact
characteristic-zero Q2 fold satisfies

\[
 148342W_F(2,60)+9435W_F(9,60)
 +408W_F(16,60)+9W_F(23,60)=0. \tag{4.1}
\]

Moreover,

\[
 148342c_2+9435c_9+408c_{16}+9c_{23}
 ={76022307\over128}. \tag{4.2}
\]

Consequently

\[
 148342Q_2+9435Q_9+408Q_{16}+9Q_{23}
 =-{76022307\over128}s_{1F}. \tag{4.3}
\]

Together with the leaf saturation $s_{1F}t_{\rm SAT}-1=0$, equation (4.3)
puts $1$ in the ordinary specialized leaf ideal.  Hence leaf 11 has no point,
even before imposing $\eta^0$ or the other J rows.

#### Proof

The checker reconstructs the exact lcut-12 UU/reduction back-map over the
repository's radical ring, substitutes the entire D21 B block before orbit
folding, and retains all coefficients that can reach slot 60.  A fresh tail
has relative slot at least 41, so its complementary slot is at most 19; on
this slice only complements `0,12,18` occur.  Thus fresh levels 72, 60, and
54 are exhaustive.  Since every free has relative slot at least 12,
variable-degree cap five is exact; absence of the loss sentinel is asserted.

The four exact $W_F$ rows then satisfy (4.1) coefficient by coefficient.
An independent polynomial multiplication gives (4.2), hence (4.3).  If
$c=76022307/128$ and $L$ is the left side of (4.3), the explicit unit
certificate is

\[
 1=-{t_{\rm SAT}\over c}L-(s_{1F}t_{\rm SAT}-1).
\]

This proves ordinary, and therefore radical, emptiness.  Independent
reductions of the full shipped leaf equations give the same identity at
both primes:

| prime | coefficient of $s_{1F}$ in the four-row combination |
|---:|---:|
| 105337 | 33983 |
| 105673 | 49195 |

Both are nonzero.  $\square$

Leaves 12 and 13 require respectively $\mathtt{bg42\_24}\ne0$ and
$\mathtt{bg21\_24}\ne0$,
contradicting the literal B-zero domain.  The remaining origin chart is the
already banked characteristic-zero-empty l13 stratum.  Therefore

\[
 V_{\rm bank}\cap Q2_{l12}=\varnothing.
\]

This closes the seven Q2 rows left open by `xmodel/sol-l12map.md`; $\eta^0$ is
not needed.  It does **not** close Q2 directions opened before l12, nor does
it prove that every algebraizing point of $V$ must lie in the l12 tier.  It is
also tied to the literal B-zero window; an unfrozen-B construction requires
a new intersection map.

## 5. What remains

The answer to “does any point of $V$ algebraize?” remains **open**, for two
independent reasons: $V$ itself has no certified point, and separate bounded
relations are much weaker than a joint Keller pair.

The finite next tasks are:

1. Compute the full nonlinear Row-24 compatibility residual on the D23
   locus.  Proposition 3.2 reduces its new symbol to four pivots, but does
   not decide its remaining five-to-seven conditions.
2. Continue Rows 26--40 without assuming an unproved $(9,10,10)$ top-degree
   law, then introduce the x-side at Row 42.
3. Extend Theorem 4.1 to the earlier Q2 l8/l4 directions, or prove a
   structural theorem forcing every algebraizing B-zero point into l12.
4. Build the unfrozen-B J-window.  The current bank cannot decide actual
   B-tail directions that it omitted.
5. At a low-dimensional surviving component, construct the completed
   orbit relations and impose the mixed polynomial identity
   $J(F,G)=1$.  For the canonical completions in Theorem 2.2, Rows 49/50
   are the natural first separate support junctions.

**Conjecture (generic prolongability; unproved).**  The rank-four frontier
symbols continue to leave a nonempty formal prolongation on a dense part of
the D23 window.  Balanced variable counts and Rows 14--24 support this, but
they do not exclude a finite nonlinear incompatibility.

No other conjectural assertion is used in the proved results above.

## 6. Reproduction

Fast exact contact, primitive-margin, grading, and bank replay:

```text
python3 cases/sol_algkill.py
```

Add the exact targeted D25/Row-24 rebuild (about 25 seconds):

```text
python3 cases/sol_algkill.py --row24
```

Fast two-prime Q2 identity guard:

```text
python3 cases/sol_algkill_q2.py --mod-only
```

Full characteristic-zero Q2 fold and cross-engine replay:

```text
python3 cases/sol_algkill_q2.py
```

If the transient UU/reduction states are absent, add `--rebuild-state`.
The checkers write no repository files.
