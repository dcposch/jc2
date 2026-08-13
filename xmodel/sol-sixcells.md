# Next-tier attack on the six \(td=7\) survivor cells

## Executive summary — five lines

1. I selected **transport** and **budget-equality rigidity**; for the smallest cell, transport gives a **PROVEN next-step survival**, not a kill.
2. The cell \((9,15,7,3)@\mu _0=2\) has exactly two deduplicated completions, both budget-equality, and an explicit minimum-cost parent chain satisfies every filed handshake and every displayed local Prop. 8.1(iv) equation.
3. Its direct completion passes case IV at \((w,M,\psi)=(2/3,3,2)\); its other completion passes the next trunk cell \((35,15,7,5)\) and case IV at \((2/5,5,1)\).
4. Equality does force every **integerized** AF2 summand sharp, but both routes have a zero-defect scalar ledger; the extra unit needed from a repeated direction is **CONJECTURE**, not a consequence of current Prop. 7.3.
5. Replaying this transport/T1 tier on the remaining five costs about \(1.5\)–\(2\) person-days; a reusable honest coefficient-gluing emitter is a separate \(3\)–\(5\)-day build, with solve time not yet bounded.

## 1. Scope and notation

The promoted local law leaves the six cells listed in
`BOOK-OFFAXIS.md:648-681`; they carry 53 deduplicated routes, 35 at budget
equality (`xmodel/sol-td7-law.md:285-312`). The smallest cell has the forced
local solution

\[
 p=\eta ^2(t-A),\qquad
 q=\eta(t-A)(t-\tfrac23A),\qquad t=\eta^7,\qquad
 \widetilde C=-\frac{14}{15}A^2,\quad A\ne0,
\]

and all its root guards pass (`xmodel/sol-td7-law.md:264-283`). A hostile
replay independently verifies all six solutions and the route split: the
\((10,15)\) cell has \(47\) routes, \(29\) equality, while the other five have
\(2+1+1+1+1\) routes, all equality
(`xmodel/grok-td7-law-review.md:40-76`).

Two ratios must not be conflated:

\[
 \rho_F:=\frac{D_F}{\deg p_F},\qquad
 \theta_F:=\frac{d_p}{d_q}.
\]

The frame invariant is \(w_F=(\bar\kappa_F-\rho_F)/\nu_F\), as defined in
`SHEET6-DEPTH.md:67-77`. The reduced local equation is

\[
             \theta p q'-p'q=Cp,\qquad C\ne0,                 \tag{T1}
\]

after division by \(1-u\); its normalization, top cancellation, and root
conditions are proved in `xmodel/sol-td7-law.md:95-113,172-188`.

## 2. Transport: a fully worked next-step survivor

### Proposition (proved survival at the filed transport tier)

**PROPOSITION.** The cell \((9,15,7,3)@2\) survives all currently filed
numerical \(Q\)-transport equations on both of its priced completions. On one
explicit minimum-cost parent chain, every charged/neutral vertex has an
admissible solution of (T1). The nonterminal completion also has an
admissible (T1) solution at its next trunk vertex. Thus the cell is a
**demonstrated survivor at the Prop. 9.3 transport + vertex-local T1 tier**.

This proposition does **not** assert a simultaneous Puiseux/Keller lift.

### 2.1 The parent chain

The unique \(td=7\) off-axis entry consists of pole data
\((a,b,\nu)=(1,1,2)\oplus(1,2,3)\), with initial states
\((w,M)=(2,1)\oplus(3/2,2)\) (`BOOK-OFFAXIS.md:75-85`). For a dirty or clean
case-II edge, the calculation uses

\[
 \frac{\rho_{\rm par}+n}{\bar\kappa_{\rm par}+n}
       =\frac{d_p}{l\,d_q},
 \qquad
 \bar\kappa_{\rm child}
       =\frac{\bar\kappa_{\rm par}+n}{\nu_{\rm par}},          \tag{2.1}
\]

together with the clean and dirty \(w\)-laws proved in
`BOOK-OFFAXIS.md:239-256,273-283`. The full priced pattern menu and its
AF2 charge are `BOOK-OFFAXIS.md:455-475`; the exact implementation is
`cases/scratch_offaxis_pricing/px2.py:35-151`.

Write a frame as

\[
        \mathcal F=(\rho,\bar\kappa,\nu;\,w,M).
\]

A predecessor replay of that exact transition graph gives the following
minimum-cost chain-2 witness:

| target | reduced shape data | \((d_p,d_q)\) | edge \(n\) | target frame \(\mathcal F\) | \(\Delta\lambda\) |
|---|---|---:|---:|---|---:|
| entry \(H_0\) | pole \((a,b,\nu)=(1,2,3)\) | — | — | \((1/2,5,3;3/2,2)\) | 0 |
| \(F_1\) | \(l=2,\epsilon=0,k=2,(m_j)=(1,1),\nu=5\) | \((20,16)\) | 7 | \((1/4,4,5;3/4,4)\) | 2 |
| \(F_2\) | \(l=4,\epsilon=0,k=1,(m_j)=(3),\nu=17\) | \((119,35)\) | 21 | \((1/7,5,17;2/7,7)\) | 1 |
| \(F_3\) | pure-\(b\): \(l=7,\epsilon=3,\nu=5\) | \((38,6)\) | 46 | \((1/2,3,5;1/2,2)\) | 1 |
| \(H_2\) | neutral: \(l=2,n_q=1,\nu=7\) | \((14,8)\) | 17 | \((1/2,4,7;1/2,2)\) | 0 |

For example, the first row of (2.1) is
\((1/2+7)/(5+7)=20/(2\cdot16)\), and the target has
\(\bar\kappa=12/3=4\) and \(w=(4-1/4)/5=3/4\). The other rows verify
identically. The last state is a legal \(\mu _0=2,\nu_H=7\) arrival:
\(2\mid M=2\) and \(\nu_H\equiv-1\pmod2\), exactly the arrival law in
`BOOK-OFFAXIS.md:510-519`. The Dijkstra closure retaining these minimum
state costs is `cases/scratch_offaxis_pricing/px5.py:63-87`.

### 2.2 Both merge handshakes close

Chain 1 is frozen with frame

\[
       (\rho_1,\bar\kappa_1,\nu_1;w_1,M_1)=(1,5,2;2,1),
\]

as proved in `BOOK-OFFAXIS.md:521-529`. Its case-II edge has \(n_1=5\),
so

\[
 \bar\kappa_G=\frac{5+5}{2}=5,\qquad
 X_G=\frac{1+5}{2}=3.                                      \tag{2.2}
\]

The chain-2 zero edge is case III. With the last frame in the table and
\(n'_2=1\), it gives

\[
 \bar\kappa_G=4+1=5,\qquad
 X_G=\mu_0(\rho_2+n'_2)=2(\tfrac12+1)=3.                   \tag{2.3}
\]

Equivalently, the two general-\(\mu\) handshakes are
\(X_G=1(5-2)=3\) and \(X_G=2(5-7/2)=3\). These are precisely R2.1's
case-II/case-III laws (`BOOK-OFFAXIS.md:293-315`), specialized in the
class-C formula at `BOOK-OFFAXIS.md:541-549`. Finally,

\[
 \frac{X_G}{\bar\kappa_G}=\frac35=\frac9{15},\qquad
 \rho_G=\frac{X_G}{d_p}=\frac13,\qquad
 w_G=\frac{5-1/3}{7}=\frac23,\qquad M_G=3.                 \tag{2.4}
\]

Thus there is no handshake or \(w\)-conservation mismatch.

### 2.3 Coefficient witness at every displayed vertex

Give each vertex its own nonzero scale \(A_v\). Direct substitution into
(T1) yields:

| vertex/cell | \(p,q\), with \(t=\eta^\nu\) | forced relation | \(C\) |
|---|---|---|---:|
| \(F_1:(20,16),\nu=5\) | \(p=(t-A)^2(t-B)(t-D)\), \(q=\eta(t-A)(t-B)(t-D)\) | \(B+D=3A,\ BD=3A^2\) | \(-15A^3/4\) |
| \(F_2:(119,35),\nu=17\) | \(p=(t-A)^4(t-B)^3\), \(q=\eta(t-A)(t-B)\) | \(B=3A/2\) | \(51A^2/10\) |
| \(F_3:(38,6),\nu=5\) | \(p=\eta^3(t-A)^7\), \(q=\eta(t-A)\) | — | \(-10A/3\) |
| \(H_2:(14,8),\nu=7\) | \(p=(t-A)^2\), \(q=\eta(t-A)\) | — | \(-7A/4\) |
| \(G:(9,15),\nu=7\) | \(p=\eta^2(t-A)\), \(q=\eta(t-A)(t-B)\) | \(B=2A/3\) | \(-14A^2/15\) |

All constants are nonzero. In the first row, \(B,D\) are the roots of
\(z^2-3Az+3A^2\), whose discriminant is \(-3A^2\ne0\); neither root is
\(0\) or \(A\). Every other distinctness and squarefreeness guard is
immediate from the displayed nonunit ratios. Hence every root of \(p\)
appears simply in \(q\), and every \(q\)-only root is simple, as required by
the general root law (`BOOK-OFFAXIS.md:209-224`).

For the requested cell itself, cancellation of \(p\) makes the entire solve
visible in one line:

\[
 \frac{\theta pq'-p'q}{p}
   =\frac{-14A+21B}{5}\,t-\frac75AB,\qquad \theta=\frac35.  \tag{2.5}
\]

Thus \(B=2A/3\) and \(C=-14A^2/15\ne0\), agreeing with the promoted
solution table (`xmodel/sol-td7-law.md:270-283`).

### 2.4 Both next vertices pass

There are exactly two deduplicated routes through this cell, obtained by the
documented route deduplication
`cases/scratch_offaxis_pricing/px5.py:254-262`:

1. **Direct case-IV terminal.** From (2.4),
   \(j=M(1-w)=3(1/3)=1\) and
   \(\psi=\lceil M/j\rceil-1=2\). The parent-chain cost is
   \(2+1+1=4=6-\psi\).

2. **One nonterminal trunk step.** Take the legal \(l=3\) cell
   \((d_p,d_q,\nu,M)=(35,15,7,5)\). Equation (2.1) gives
   \((1/3+n)/(5+n)=35/(3\cdot15)\), hence \(n=16\), and therefore

   \[
   (\rho,\bar\kappa,\nu;w,M)
       =(1/5,3,7;2/5,5).                                  \tag{2.6}
   \]

   Its local equation has

   \[
    p=(t-A)^3(t-B)^2,\quad q=\eta(t-A)(t-B),\quad
    \frac{\theta pq'-p'q}{p}
       =\frac73\bigl((B-2A)t+AB\bigr),\quad\theta=\frac73.
   \]

   Hence \(B=2A\), \(C=14A^2/3\ne0\), and all root guards pass. Now
   \(j=5(1-2/5)=3\), \(\psi=\lceil5/3\rceil-1=1\), and the total cost is
   \(4+1=5=6-\psi\).

The terminal formulas and the shared \(td=7\) budget are proved in
`BOOK-OFFAXIS.md:486-500`; merge/trunk accounting starts from only
\((w,M)\) at `BOOK-OFFAXIS.md:502-519`.

This proves the proposition. It also explains why the merge ratio
\(B/A=2/3\) does not contradict the next-cell ratio \(B/A=2\): these are
different pattern variables at different characteristic levels. The filed
coefficient transport pins leading Taylor coefficients but explicitly does
not pin subleading pattern coefficients across edges
(`SHEET6-TEMPLATE.md:140-154`), and the depth theorem explicitly excludes
the coefficient layer and \(M\ge2\) suffixes
(`SHEET6-DEPTH.md:403-422`).

**CONJECTURE.** The independent local scales and coefficients in this
witness extend simultaneously to full Puiseux data. Nothing above proves
that statement; it records exactly where an honest St. 3.9/tower/Jacobian
gluing system must begin.

## 3. Budget equality: what is rigid, and the precise escape

### Proposition (integerized termwise rigidity)

**PROPOSITION.** Let an actual carrier realize a priced \(td=7\) route.
For each charged noncontinuation direction \(c\) at \(F\), let
\(a(F,c)\in\mathbb N_{>0}\) be its recorded AF2 lower summand
\(\max(1,\lceil\mathrm{gap}\rceil)\), with the \(\nu_F\)-normalized version
at zero. Put \(L=\sum_{F,c}a(F,c)\). If \(L=6-\psi\), then:

1. every \(\lambda_F\) equals the sum of its recorded integerized summands;
2. every selected cv vertex has exactly its recorded integer mass and no
   additional vertex occurs in any \(Y(F)\);
3. under the standing E9/H2 Euler-ledger reading used by the off-axis book,
   the x-side mass is exactly \(\psi\), every other unrecorded cv row is empty,
   and every \(\delta_a=0\).

**Proof.** AF2 proves that distinct directions give distinct cv vertices,
each mass is a positive integer, and
\(\lambda_F\ge\sum_c a(F,c)\)
(`SHEET6-AF2.md:94-115`). The shared bound is
\(\sum_F\lambda_F\le6-\psi\) (`BOOK-OFFAXIS.md:486-500`). When
\(L=6-\psi\),

\[
 0\le \sum_F\left(\lambda_F-\sum_c a(F,c)\right)
    \le (6-\psi)-L=0,
\]

so every nonnegative integer difference vanishes, proving 1–2. The exact
Euler identity is \(td-1=\sum_{cv}\kappa(\pi-1)+\sum_a\delta_a\), with
all \(\delta_a\ge0\), and its chain/x/pole itemization is
`SHEET6-LROOT.md:33-98`. A case-IV terminal has
\(\lambda_{(0,y)}=0\), and its \(\psi\) lower bound is sharp-capable
(`SHEET6-LROOT.md:100-126`). The already forced y-mass \(6-\psi\) plus
x-mass at least \(\psi\) exhausts \(td-1=6\); all remaining nonnegative
terms vanish. This proves 3. \(\square\)

The word **integerized** is load-bearing: equality forces the rounded AF2
mass, not equality in the underlying rational gap.

### 3.1 Application to \((9,15,7,3)@2\)

The common positive-cost signatures of the two routes are:

| vertex | \((\bar\kappa,X)\) | charged local multiplicity | raw AF2 bound | integer mass |
|---|---:|---:|---:|---:|
| \((20,16),\nu=5\) | \((4,5)\) | \(1,1\) | \(1,1\) | \(1+1\) |
| \((119,35),\nu=17\) | \((5,17)\) | \(3\) | \(17/3-5=2/3\) | \(1\) |
| \((38,6),\nu=5\) | \((3,19)\) | zero root \(\epsilon=3\) | \((19/3-3)/5=2/3\) | \(1\) |

The second route adds:

| vertex | \((\bar\kappa,X)\) | charged local multiplicity | raw AF2 bound | integer mass |
|---|---:|---:|---:|---:|
| \((35,15),\nu=7\) | \((3,7)\) | \(2\) | \(7/2-3=1/2\) | \(1\) |

These are direct substitutions into P0's formula
(`BOOK-OFFAXIS.md:455-475`). The merge costs zero because its zero root is
an arriving chain and its \(q\)-extra is not a \(p\)-direction; this is the
P2 accounting in `BOOK-OFFAXIS.md:502-509`.

Consequently the two formal exact ledgers are

\[
 \begin{array}{c|c|c|c}
   \text{route}&\text{recorded y-mass}&\text{x-mass}&\text{total}\\
   \hline
   \text{direct}&(1+1)+1+1=4&2&6\\
   \text{one trunk step}&4+1=5&1&6.
 \end{array}                                                   \tag{3.1}
\]

Thus budget equality supplies real rigidity but no contradiction. In
particular, the \(2/3,2/3\) (and \(1/2\)) raw gaps can legitimately round to
mass \(1\). The later hostile reread is decisive here: Prop. 7.3 proves
equality in the special eventual-fibre multiplicity-one case, but provides
neither the converse nor a strict excess theorem at multiplicity at least
two (`SHEET6-LT-REVIEW.md:84-118`).

### 3.2 The strongest precise kill target

The following implication is already proved by the equality proposition:

> **PROVEN conditional kill.** If the cv subtree belonging to either the
> multiplicity-\(3\) direction at \((119,35)\) or the zero direction of
> multiplicity \(3\) at \((38,6)\) has total integer mass at least \(2\), then
> both routes through \((9,15,7,3)@2\) overrun their budget by one and die.

A predecessor replay of the minimum state graph shows that zero-cost neutral
loops/\(M\)-drops are the only minimum-path variants; every positive-cost
minimum path contains those two signatures. This replay uses exactly the
transition enumeration `cases/scratch_offaxis_pricing/px2.py:35-151` and the
minimum-state closure `cases/scratch_offaxis_pricing/px5.py:63-87`.

What is missing is precisely:

**CONJECTURE (transported multiple-direction excess).** At one of those two
signatures, the local reduced multiplicity \(3\) transports either to
eventual fibre multiplicity at least \(2\), or to at least two cv vertices,
and the corresponding subtree has integer mass at least \(2\) rather than
the AF2 floor \(1\).

Both clauses are unproved: the route book does not retain eventual-fibre
multiplicity, and the required strict local excess formula is exactly the
gap isolated in `SHEET6-LT-REVIEW.md:84-111`. The proposed provenance tuple
for measuring it was already specified in `xmodel/sol-avenues2.md:174-183`.
The \((10,15)\) direct equality route is the necessary negative control: its
only charged A-step has a simple NE orbit, its \(\mu_0=3\) zero direction is
an arrival, and its merge costs zero (`xmodel/sol-avenues2.md:160-170`).
Hence no honest theorem should assert “every \(\mu_0\ge2\) merge costs one.”

## 4. Cost to process the remaining five

The route distribution matters: \((10,15,7,5)\) accounts for \(47/53\)
routes (29 equality and 18 slack), while each of the other four cells has
one equality route (`xmodel/grok-td7-law-review.md:40-58`). Therefore:

| work item | estimated cost | deliverable |
|---|---:|---|
| Retain exact predecessor/provenance data instead of only \((w,M,\lambda)\) minima | \(0.5\) day | one explicit path for every deduplicated survivor route |
| Generate (T1) from each distinct charged/neutral/trunk shape and check \(C\ne0\), root separation, and squarefreeness | \(0.5\)–\(1\) day | transport + local-T1 verdict on all remaining five |
| Independent exact audit of handshakes, terminals, and route deduplication | \(0.5\) day | proof-grade tables; **total \(1.5\)–\(2\) days at the tier of §2** |
| Emit equality provenance signatures | \(<0.5\) day | at most \(35\cdot5=175\) equality-route charge records, before hashing |
| Prove the multiple-direction excess conjecture | \(3\)–\(7\) research days, high uncertainty | one reusable theorem; mechanical application then takes hours |
| Build the first honest St. 3.9/\(h_j\)-tower/Jacobian coefficient-gluing emitter | \(3\)–\(5\) engineering days, solve time unknown | simultaneous rather than vertex-local obstruction system |

The \(175\)-record bound uses “every positive step costs at least one”
(`BOOK-OFFAXIS.md:464-478`) and the \(td=7\) maximum total charge \(5\)
(`BOOK-OFFAXIS.md:486-500`). Equality rigidity can cheaply attack the four
singleton cells, but it cannot by itself close the 18 slack routes of the
\((10,15)\) cell. That cell is therefore the dominant remaining cost and the
right coefficient-gluing pilot after the provenance pass.

## 5. Reproduction and honest perimeter

The route totals and the two smallest-cell completions are regenerated by

```sh
cd /Users/dc/code/math/jc72108
python3 cases/scratch_offaxis_pricing/px5.py \
  | rg 'cell\((9,15|10,15|15,25|18,27|39,65)\)|total routes'
```

The generator, class-C construction, trunk enumeration, and dedup key are at
`cases/scratch_offaxis_pricing/px5.py:97-150,208-262`; the promoted report's
independent reproduction recipe is `xmodel/sol-td7-law.md:353-376`.

The proved result in this report is a survival witness for the finite
Prop. 9.3 frame transport, every displayed local Prop. 8.1(iv) solve, and
the next case-IV arithmetic. It is not P-realizability and not a global
Keller pair: the book itself warns that its state/arrival construction is a
conservative superset (`BOOK-OFFAXIS.md:632-646`), and depth closure makes no
realizability claim (`SHEET6-DEPTH.md:429-432`). Every stronger extension in
this report is explicitly labeled **CONJECTURE**.
