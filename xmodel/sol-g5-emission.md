# G5 via the merged-emission law: exact audit, obstruction, and missing lemma

Date: 2026-08-19

## Status

**BLOCKED. No upper bound on `td` is proved by FC5, the `M=1` depth
closure, and NF-M as presently stated.** More sharply, their explicitly
extracted scalar bookkeeping consequences do not force

\[
  \sum_{P\in T_{a,\mathrm{pole}}}\frac{a_Pb_P}{\nu_P}\le 1,
\]

and they do not force any weaker finite bound on that sum, even with the
global Sigray type fixed to \((\alpha,\beta)=(2,3)\), when their displayed
local consequences are treated as the bookkeeping system. This is not a
logical-independence claim about the full hypotheses “actual Keller pair”
and “actual Eggers--Wall tree”; it identifies the global content that any
proof must still use.

This is not merely failure to find the right manipulation. There is an
explicit infinite **formal arithmetic-schema family** below. Its sheet
numbers are `td = 4A -> infinity`; it satisfies the pole laws, N1, all
displayed numerical equations of a Proposition 9.3 case-IIa schema, FC5,
separately solvable local coefficient identities, the numerical case-IV
terminal conditions, and non-conflict between the proved charge lower bound
and the global ceiling. The family stays entirely on
`M=2 -> M=3`, outside the scope of the `M=1` depth theorem. NF-M sees one
coefficient type for each member. What is not proved is a compatible local
chart transition, global Eggers--Wall gluing, or realization by one
polynomial Keller pair.

Accordingly:

- **PROVED:** the exact pole-mass potential carried by an entry state is
  \(\Phi_s(w,M)=wM^2/(sM-1)\), where \(s=\alpha+\beta\).
- **PROVED:** FC5 is a local frame identity. It has no incoming-mass term.
- **PROVED:** the natural potential \(\Phi_s\) changes with both signs on
  coefficient-solvable local merge charts, so it is not a monotone
  one-step telescope.
- **PROVED:** nonsaturated all-\(\mu=1\) IIa merges are locally
  \(\Phi_s\)-dissipative. This is genuine positive structure, but it points
  in the wrong direction for an upper bound on leaf mass.
- **PROVED:** depth closure gives a finite cumulative jump-cell menu and
  NF-M gives finite isolated coefficient-type counts after fixing their
  respective inputs; neither is coercive in `td`.
- **CONJECTURE:** the sharp target is the normalized mismatch-energy bound
  on a common resolution. A proof needs new global Keller/proximity
  information, not another emission identity.
- **CORRECTION TO THE STATED PAYOFF:** even the sharp mass bound gives only
  `td <= alpha*beta`. The repository has no absolute finite GGV type list.
  Thus TD-BOUND alone does not make the ladder cofinal.

There is a second, elementary correction of principle: a universal absolute
bound `td <= N` for *every* plane Keller counterexample would already prove
the two-dimensional Jacobian conjecture, because iterating one counterexample
would give sheet numbers `td^k`. A finite bound useful as an intermediate
book theorem must therefore be restricted to a class not closed under
iteration. Bounding a specially selected globally minimal counterexample is
the reduction-relevant option; bounding primitive/indecomposable
representatives would be another possible quantifier.

All gaps below are explicitly labelled **CONJECTURE**. A “formal family” is
never asserted to be a Keller counterexample.

---

## 1. Notation and the exact content of FC5

Use \((\alpha,\beta)\), with \(2\le\alpha<\beta\) and
\(\gcd(\alpha,\beta)=1\), for the Sigray type. Put

\[
  s:=\alpha+\beta.
\]

The letter `r` below denotes the number of arrivals at a merge, never the
first component of the type. At a nonterminal chart \(G\), write

\[
 X_G:=D_G/i_G,\qquad P_G=i_Gd_p,\qquad
 \rho_G:=D_G/P_G,\qquad
 w_G:=\frac{\bar\kappa_G-\rho_G}{\nu_G}.
\]

The full-degree normalization is recorded in
[`xmodel/sol-normalform.md:100-120`](sol-normalform.md). The general merge
handshake and ratio law are in
[`BOOK-OFFAXIS.md:293-331`](../BOOK-OFFAXIS.md).

### Proposition 1 (FC5 reconstructed)

**PROVED.** The equal-quotient/Proposition 9.3 ratio equation is

\[
  \frac{X_G}{\bar\kappa_G}=\frac{d_p}{d_q}.
\]

Since \(P_G=i_Gd_p\),

\[
 \rho_G=\frac{D_G}{P_G}=\frac{X_G}{d_p}
       =\frac{\bar\kappa_G}{d_q}.
\]

Consequently

\[
 \boxed{
 w_G=\frac{\bar\kappa_G(d_q-1)}{\nu_Gd_q}},
 \qquad
 \boxed{M_G=\gcd(d_p,d_q)}.                         \tag{1.1}
\]

This is exactly FC5 as certified in
[`TOWER-TD11.md:695-719`](../TOWER-TD11.md) and implemented at
[`cases/td11_census.py:1064-1120`](../cases/td11_census.py).

For an NF-M schema,

\[
 d_p=\epsilon+\nu\sum_i p_if_i,
 \qquad d_q=1+\nu\widehat Q,
\]

so (1.1) becomes

\[
 w_G=\frac{\bar\kappa_G\widehat Q}{d_q},\qquad
 M_G=\gcd\!\left(\epsilon+\nu\sum_i p_if_i,
                  1+\nu\widehat Q\right).            \tag{1.2}
\]

The orbit locations and coefficient type do not occur. That is useful for
state emission, but it is also the loss of information that prevents FC5
from being a conservation law.

### Exact scope

Equation (1.1) says what state a chart emits after its frame is already
known. It contains:

- no number of incoming pole leaves;
- no incoming \((a,b,\nu)\)-mass;
- no charge accumulated above the chart;
- no proximity multiplicity or intersection defect;
- no coefficient/root positions; and
- no relation between distinct charts.

Also, only \(M_G=\gcd(d_p,d_q)\) is unconditional. The frequently used
divisibility \(M_G\mid\sum\mu_e\) has the restricted
`epsilon=0=k` scope described in `BOOK-OFFAXIS.md:317-331`.

Thus FC5 is **PROVED as an identity**, not as a conservation or monotonicity
statement.

---

## 2. The exact natural interface with pole mass

At a pole \(P\), the promoted entry equations give

\[
 (D,D_g)=a(\alpha,\beta),\qquad
 (P,P_g)=b(\alpha,\beta),
\]

\[
 M=b,\qquad \bar\kappa=as,\qquad \rho=a/b,\qquad
 \Lambda=\frac{\alpha\beta ab}{\nu}.
\]

See [`SHEET6-TDUNIFORM.md:36-74`](../SHEET6-TDUNIFORM.md) and
[`SHEET6-MULTIPOLE.md:48-61`](../SHEET6-MULTIPOLE.md). Therefore

\[
 w=\frac{as-a/b}{\nu}
   =\frac{a(sb-1)}{b\nu}.
\]

Solving for the normalized pole mass gives the exact formula

\[
 \boxed{
   \frac{ab}{\nu}=\Phi_s(w,M)
   :=\frac{wM^2}{sM-1}.}                              \tag{2.1}
\]

Proposition 5.8 then gives

\[
 \boxed{
   \frac{td}{\alpha\beta}
    =\sum_{P\ \mathrm{pole}}\frac{a_Pb_P}{\nu_P}
    =\sum_{P\ \mathrm{pole}}\Phi_s(w_P,M_P).}         \tag{2.2}
\]

This is an exact memoryless scalar bridge from pole data to the FC5 state.
It is exact **at poles**. At an internal chart,
\(\Phi_s(w_G,M_G)\) is only a candidate potential; it is not a geometric
mass supplied by any cited theorem.

Any direct FC5 proof of TD-BOUND would therefore need, at minimum, a global
telescope controlling the sum of the pole values in (2.2). The next two
sections show exactly why the obvious telescope fails.

---

## 3. What FC5 does at an all-`mu=1` merge

Suppose an all-\(\mu=1\), nonzero-edge merge receives the common depth-state
value \(w\). The depth handshake gives

\[
 \bar\kappa_G=w\frac{d_q}{\Delta},\qquad
 X_G=w\frac{d_p}{\Delta},\qquad
 \Delta:=d_q-d_p.
\]

Combining this with FC5 yields

\[
 \boxed{
 w_{\rm out}=w\frac{d_q-1}{\nu\Delta}.}                \tag{3.1}
\]

For the three MP6 families this specializes to

\[
\begin{array}{c|c|c}
\text{family}&(d_p,d_q)&w_{\rm out}/w\\ \hline
\mathrm{IIa}&(r\nu,(r+l)\nu+1)&(r+l)/(l\nu+1)\\
\mathrm{ZCH}&((r-1)\nu+1,(r-1+l)\nu+1)&(r-1+l)/(l\nu)\\
\mathrm{I}&(r,r+l)&(r+l-1)/l.
\end{array}                                             \tag{3.2}
\]

Every factor is at most \(r\), but the factors occur on both sides of one.
Along a fixed hierarchy this supplies only a finite growth estimate, roughly
at most a product of arrival counts. The number of leaves, the initial
\(w\), and the hierarchy itself are already `td`-dependent. Equation (3.2)
therefore has no reverse leverage on the entry mass.

### Proposition 2 (a real but wrong-way IIa inequality)

**PROVED.** For an all-\(\mu=1\) IIa merge, put

\[
 \Delta=l\nu+1,\qquad g=\gcd(r,\Delta)=M_{\rm out}.
\]

Compare the potential of \(r\) equal incoming `M=1` states with the
potential of the emitted state:

\[
 \frac{\delta}{w}
 :=\frac{r}{s-1}
   -\frac{(r+l)g^2}{\Delta(sg-1)}.                     \tag{3.3}
\]

If the cell is nonsaturated, \(\Delta\nmid r\), then \(\delta>0\).

Indeed write \(r=gR\), \(\Delta=gD\). Nonsaturation gives \(D\ge2\),
and \(\nu\ge2\) gives \(l\le(gD-1)/2\). After clearing positive
denominators, (3.3) is positive exactly when

\[
 RD(sg-1)>(gR+l)(s-1).                                 \tag{3.4}
\]

The coefficient of \(R\) in the left-minus-right side is

\[
 A_R=D(sg-1)-g(s-1).
\]

For \(g=1\), \(A_R=(s-1)(D-1)>0\). For \(g\ge2,D\ge2\), it is
minimized at \(D=2\), where \(A_R=g(s+1)-2>0\). The difference is
therefore increasing in \(R\), so it suffices to take \(R=1\). Twice
the resulting difference is bounded below by

\[
 gs(D-2)+D(g-2)+2g+s-1>0,                              \tag{3.5}
\]

with the displayed lower bound in the `g=1` case reducing to
\((s-1)(D-1)>0\).

Thus every nonsaturated IIa cell dissipates the natural potential.

The general saturated-IIa coefficient kill is currently recorded only at
the quarantined A3 tier in
[`SHEET6-MULTIPOLE.md:145-151`](../SHEET6-MULTIPOLE.md).
Treating that general kill as promoted is therefore **CONJECTURE** in this
note. Even if it is granted, Proposition 2 gives

\[
 \sum \Phi_s(\text{incoming})
   \;\ge\;\Phi_s(\text{outgoing}),                     \tag{3.6}
\]

which is the wrong direction. A terminal lower bound would yield another
lower bound on leaf mass. TD-BOUND needs an upper bound on the accumulated
dissipation plus the terminal contribution, and no such budget occurs in
FC5.

---

## 4. The natural potential is nonmonotone even after local coefficient solving

Two exact controls dispose of a simple monotonicity proof.

### 4.1 Decrease: residue A

For \(s=5\), the two residue-A pole states are \((w,M)=(2,1)\), so their
total pole mass is

\[
 2\Phi_5(2,1)=1.
\]

The coefficient-solvable local IIa chart
\((r,\nu,l)=(2,3,1)\) emits

\[
 (w',M')=(3/2,2),\qquad \Phi_5(3/2,2)=2/3.             \tag{4.1}
\]

The potential decreases by \(1/3\).

### 4.2 Increase: the NF-M BB2 cylinder

The type-\((2,3)\) `11-C` packet has two B inputs
\((w,M)=(3/2,2)\); see
[`TOWER-TD11.md:104-115`](../TOWER-TD11.md). Their total is

\[
 2\Phi_5(3/2,2)=4/3.
\]

For every \(N\ge2\), NF-M's coefficient-solvable BB2 cylinder has

\[
 (\bar\kappa,d_p,d_q)=(6N+3,4N+1,2N+1),\qquad M'=1.
\]

FC5 gives

\[
 w'=\frac{(6N+3)(2N)}{N(2N+1)}=6,\qquad
 \Phi_5(6,1)=3/2.                                      \tag{4.2}
\]

The potential increases by \(1/6\). This arithmetic schema has a solved
local coefficient fiber: NF-M finds the unique type `b=-a` for every \(N\); see
[`NF-M.md:170-188`](../NF-M.md). The chart later dies by a separate
denominator criterion. That later death does not turn FC5 into a monotone
law.

Equations (4.1)--(4.2) prove:

> **PROVED NO-TELESCOPE STATEMENT.** The pole-mass extension
> \(\Phi_s(w,M)\) obeys neither one-step inequality
> \(\Phi_{\rm out}\le\sum\Phi_{\rm in}\) nor its reverse uniformly
> across coefficient-solvable local merge charts.

All three state values used here satisfy the type-`(2,3)` pole laws:
`(2,1)` comes from `(a,b,nu)=(1,1,2)`, `(3/2,2)` from
`(1,2,3)`, and `(6,1)` from `(3,1,2)`. Hence the same controls rule
out any universal memoryless state potential `V(w,M)` that must equal pole
mass on every pole-law state and obey one fixed local inequality on every
coefficient-solvable chart in this relaxation.

This does not rule out a signed cancellation over globally admissible
histories, a global restriction eliminating one sign, or a richer internal
state. It rules out the direct one-step monotonicity interpretation of FC5's
emitted pair.

---

## 5. An unbounded fixed-type formal arithmetic-schema family

This is the decisive obstruction to *any* numerical `td` bound from the
listed local consequences alone.

### Proposition 3 (unbounded local arithmetic schemas)

**PROVED AS AN ARITHMETIC-SCHEMA STATEMENT; COMPATIBLE TREE/CHART AND GLOBAL
REALIZATION ARE CONJECTURE/UNKNOWN.** Let

\[
 A=30t+5\quad(t\ge0),\qquad N:=9A-2,\qquad n:=13A-3.
\]

There is a one-pole type-\((2,3)\) record and one case-IIa numerical schema
satisfying all identities listed below, with

\[
 td=4A\longrightarrow\infty,\qquad
 \frac{ab}{\nu_0}=\frac{2A}{3}\longrightarrow\infty,  \tag{5.1}
\]

but with constant FC5 output

\[
 (w_1,M_1)=(2/3,3).                                    \tag{5.2}
\]

#### 5.1 Pole and entry laws

Take

\[
 (\alpha,\beta)=(2,3),\qquad (a,b,\nu_0)=(A,2,3).
\]

The pole equations give

\[
 (D_0,D_{g,0})=(2A,3A),\qquad (P_0,P_{g,0})=(4,6),
\]

\[
 \Lambda_0=td=\frac{6\cdot A\cdot2}{3}=4A,\qquad
 M_0=b=2.                                               \tag{5.3}
\]

The Sigray entry menu is also satisfied:

\[
 \nu_0=3\mid\beta,\qquad
 \nu_0\mid(b\alpha-1)=3.                             \tag{5.3a}
\]

The entry frame is

\[
 Q_0=(2A,4,3,2,5A),\qquad
 \rho_0=A/2,\qquad w_0=3A/2.                          \tag{5.4}
\]

N1 holds because \(A\equiv2\pmod3\), so
\(\gcd(\bar\kappa_0,\nu_0)=\gcd(5A,3)=1\).

#### 5.2 Exact displayed Proposition 9.3 arithmetic

Take a case-IIa step with

\[
 \mu=2,\qquad k=1,\qquad l=0,
\]

where \(\mu=2\mid M_0=2\); this is the required `k>0 => l=0` IIa
pattern. With child pattern parameter \(\nu_1=N\), the reduced child degrees
are

\[
 d_p=(k+\mu)N=3N=27A-6,\qquad
 d_q=(k+l+1)N+1=2N+1=18A-3.                           \tag{5.5}
\]

Since \(i=P_0/\mu=2\), the exact case-I/II ratio is

\[
 \frac{d_p}{d_q}
 =\frac{2(\rho_0+n)}{\bar\kappa_0+n}
 =\frac{A+2(13A-3)}{5A+13A-3}
 =\frac{27A-6}{18A-3}.                                \tag{5.6}
\]

Also \(\bar\kappa_0+n=18A-3\) is divisible by \(\nu_0=3\). The
transport equations therefore give

\[
 D_1=\frac{D_0+nP_0}{3}=2N,\qquad P_1=i d_p=6N,
\]

\[
 \rho_1=1/3,\qquad \nu_1=N,\qquad
 \bar\kappa_1=\frac{\bar\kappa_0+n}{3}=6A-1.          \tag{5.7}
\]

Moreover

\[
 M_1=\gcd(3N,2N+1)=3,\qquad
 \gcd(N,6A-1)=1,                                      \tag{5.8}
\]

the second identity following from
\(2N-3(6A-1)=-1\). Thus child N1 also holds.

The case-I/II equations used here are the H1-tier Proposition 9.3
arithmetic (Sigray, pp. 50--51), summarized in
[`SHEET6-CAMPAIGN.md:27-46`](../SHEET6-CAMPAIGN.md). The campaign explicitly
records that trust perimeter at `SHEET6-CAMPAIGN.md:69-75`; no stronger
incidence claim is imported here.

#### 5.3 The arithmetic relaxation lets FC5 erase the scale

Since \(d_q=3(6A-1)\),

\[
 \rho_1=\frac{\bar\kappa_1}{d_q}=\frac13,
\]

and FC5 gives

\[
 w_1
 =\frac{\bar\kappa_1(d_q-1)}{N d_q}
 =\frac{6A-1}{18A-3}\frac{2N}{N}
 =\frac23.                                             \tag{5.9}
\]

Thus the displayed arithmetic-schema relaxation maps (5.1) to the constant
state (5.2). No inverse estimate from `(w_1,M_1)` to the pole mass can follow
within that relaxation. A realized Keller chart could still carry additional
global constraints not represented by this state.

#### 5.4 Necessary characteristic-denominator arithmetic

To check more than the ratio equation, choose

\[
 \kappa_0=3N,\qquad
 \pi_0=\frac{22A-6}{3N},
\]

\[
 \kappa_1=N,\qquad
 \pi_1=\frac{3A-1}{N}.
\]

Then \(\bar\kappa_j=\kappa_j(1-\pi_j)\), and

\[
 \pi_0-\pi_1=\frac{n}{3N}.                             \tag{5.10}
\]

For \(A=30t+5\),

\[
 \gcd(3N,22A-6)=1,\qquad
 \gcd(3N,9A-3)=3.                                     \tag{5.11}
\]

Hence the two reduced denominators are exactly \(3N\) and \(N\), the
expected possible factor-three characteristic gcd chain. This is necessary
Puiseux-lattice arithmetic; it proves neither that the two coefficient
patterns occur on one compatible local chart transition nor that these are
consecutive vertices in a globally realized tree.

#### 5.5 Charge and terminal numerical gates

The `k=1` extra orbit has positive gap

\[
 \frac{D_1}{i}-\bar\kappa_1
 =N-(6A-1)=3A-1.
\]

The proved positive-gap part of AF2 therefore gives

\[
 \lambda_1\ge3A-1.                                    \tag{5.12}
\]

See [`SHEET6-AF2.md:73-119`](../SHEET6-AF2.md). At the child,
\(\kappa_1=\nu_1=N\) and \(\bar\kappa_1<N\), and every displayed
case-IV numerical condition holds:

\[
 d_{\rm root}
 =\frac{D_1+(N-\bar\kappa_1)P_1}{N}
 =2N,
\]

\[
 2N<P_1=6N,\qquad
 \frac{d_{\rm root}M_1}{P_1}=1.                       \tag{5.13}
\]

Thus \(R=P_1/d_{\rm root}=3\) and \(\psi=2\). The budget ceiling is

\[
 td-1-\psi=4A-3,
\]

and the proved lower charge is compatible with it:

\[
 3A-1\le4A-3.                                         \tag{5.14}
\]

A consistent numerical root rectangle is

\[
 (k_f,l_f)=(6N,2N),\qquad (k_g,l_g)=(9N,3N).
\]

The one-pole `M` condition is numerically compatible as well: Proposition
8.4 requires \(M_{\rm root}\ne1\), while the case-IV/St. 8.5 divisibility
requires \(M_{\rm root}\mid M_1=3\), so assign

\[
 M_{\rm root}=3.                                       \tag{5.14a}
\]

The case-IV equations and sharp \(\psi\)-budget are derived at
[`SHEET6-H3.md:129-150`](../SHEET6-H3.md) and
[`SHEET6-H3.md:177-210`](../SHEET6-H3.md); the root-`M` compatibility is
the same check used at [`SHEET6-AF3.md:129-139`](../SHEET6-AF3.md).

**CONJECTURE/UNKNOWN:** the actual charge need not equal its AF2 lower bound.
There may be additional globally forced `Y(F)` contributions. Equation
(5.14) proves compatibility of the known charge, not existence of a full
budget-realizing tree.

#### 5.6 The local coefficient equations are nonempty

At the pole, for \(U_0\ne0\), put

\[
 p_0(\eta)=\eta(\eta^3-U_0),
\]

\[
 q_0(\eta)=\eta^6-\frac32U_0\eta^3+\frac38U_0^2.
\]

Direct differentiation gives

\[
 2p_0q_0'-3p_0'q_0=\frac98U_0^3\ne0.                 \tag{5.15}
\]

Both polynomials are squarefree and coprime.

At the child set \(x=\eta^N\) and take

\[
 p=(x-U_1)^2(x-V_1),\qquad
 q=\eta(x-U_1)(x-V_1).
\]

NF-M's reduction is

\[
 F(x)=N\big((N-1)V_1-(N+2)U_1\big)x+3NU_1V_1.         \tag{5.16}
\]

Choosing

\[
 \frac{V_1}{U_1}=\frac{N+2}{N-1}                      \tag{5.17}
\]

makes `F` constant, with

\[
 C=\frac{3NU_1V_1}{2N+1}\ne0.
\]

The roots are nonzero and distinct. Here \(\widehat Q=2\), so the NF-M
Bézout bound is

\[
 (\widehat Q-1)!=1                                    \tag{5.18}
\]

for **every fixed** \(A\). The symbols \(U_0\) and \((U_1,V_1)\) are
deliberately independent: no coefficient transport between the two solved
local equations is claimed. This is the exact quantifier failure: one type
per schema does not bound the parameter indexing the schemas.

#### 5.7 What Proposition 3 proves and does not prove

It proves that the following local numerical/coefficient package is
noncoercive in `td`:

- Sigray pole equations and the `M=b` pin;
- N1 at the pole and child;
- the complete displayed case-II ratio, integrality, and frame transport;
- FC5;
- non-conflict between the AF2 lower charge and the St 9.4 ceiling after
  assigning the charge its permitted lower-bound value;
- all displayed case-IV numerical gates;
- the pole and child local ODE/Fuchs equations; and
- the necessary characteristic-denominator drop.

It does **not** prove:

- that the case-II child is the actual immediately preceding vertex in a
  globally glued Eggers--Wall tree;
- that no extra curve vertices raise \(\lambda\) above the budget;
- that the root carries all required \(h_j\)-patterns;
- coefficient substitution/gluing between the two local levels;
- algebraization by polynomials; or
- the Keller condition for a global map.

Those missing statements are all realization data. Consequently the family
is not a Jacobian counterexample, nor yet a compatible local Eggers--Wall
transition. It shows that the explicitly displayed scalar relaxation is
noncoercive after assigning \(\lambda\) its permitted lower-bound value.

---

## 6. Scale loss occurs in an MP6 multi-arrival schema too

The preceding family is single-pole, which is already fatal to an
emission-only proof: a theorem meant for every configuration cannot omit the
sector in which no multi-leaf merge occurs. For completeness, FC5 also loses
unbounded mass in a two-arrival MP6 arithmetic schema with a solved local
coefficient equation, still without a claimed globally compatible tree.

Let \(A\ge3\) be odd. Take two type-\((2,3)\) poles

\[
 (a,b,\nu_0)=(A,1,2).
\]

Each has \(M=1\), \(w=2A\), pole mass \(A/2\), and
\(\Lambda=3A\). Hence

\[
 td=6A,\qquad \sum\frac{ab}{\nu_0}=A.                 \tag{6.1}
\]

Merge the two `mu=1` arrivals in an IIa cell with

\[
 r=2,\qquad l=1,\qquad \nu_G=2A-1=:N.
\]

Then

\[
 (d_p,d_q)=(2N,3N+1)=(4A-2,6A-2),\qquad \Delta=2A.
\]

For each edge, \(n=7A-4\) gives

\[
 \frac{\rho_0+n}{\bar\kappa_0+n}
 =\frac{A+7A-4}{5A+7A-4}
 =\frac{d_p}{d_q},                                    \tag{6.2}
\]

and the mod-two integrality condition holds. The handshake yields

\[
 \bar\kappa_G=d_q,\qquad X_G=d_p,\qquad \rho_G=1.
\]

Therefore

\[
 M_G=\gcd(d_p,d_q)=2,\qquad
 w_G=\frac{d_q-1}{N}=3,                               \tag{6.3}
\]

independent of \(A\).

The local coefficient equation is also nonempty for every \(N>1\). With
\(t=\eta^N\), \(\widetilde p=(t-u_1)(t-u_2)\), and one extra root
\(b\), the unique scale class is

\[
 u_1+u_2=\sigma\ne0,\qquad
 u_1u_2=\frac{\sigma^2(N-1)}{4N},\qquad
 b=\frac{\sigma(N+1)}{2N}.                            \tag{6.4}
\]

All local side conditions hold. This is the general formula proved in
[`SHEET6-L1.md:259-284`](../SHEET6-L1.md) and independently audited in
[`SHEET6-A3L1-REVIEW.md:198-219`](../SHEET6-A3L1-REVIEW.md).

Again, (6.1)--(6.4) are a **formal locally solved merge-schema family**, not
a completed suffix or polynomial realization. They prove that even a
coefficient-solvable multi-arrival merge schema can map unbounded incoming
pole mass to one constant emitted pair.

---

## 7. Why the depth theorem cannot restore coercivity

The depth theorem is strong in its stated direction:

\[
 w_{j+1}=w_j\frac{n}{(n-1)\nu+1}.                     \tag{7.1}
\]

Neutral steps preserve `w`; resonant steps contract it; the cumulative jump
menu is finite for each fixed entry. See
[`SHEET6-DEPTH.md:28-51`](../SHEET6-DEPTH.md) and
[`SHEET6-DEPTH.md:142-205`](../SHEET6-DEPTH.md).

It cannot supply a cross-rung bound for four independent reasons.

1. Its scope is the `M=1` axis. `M>=2` suffix chains and mixed merges are
   explicitly out of scope at
   [`SHEET6-DEPTH.md:403-422`](../SHEET6-DEPTH.md). Proposition 3 lives on
   `M=2 -> 3`.
2. Its finite set \(W(w_0)\) is constructed after fixing the entry. For an
   `M=1` pole entry, the numerator bound in
   `SHEET6-DEPTH.md:200-203` already uses the fixed `td`; for an
   `M=1`-emitting merge child, finiteness is inherited only after the prior
   entry and hierarchy records have been fixed. Neither direction supplies
   cross-rung coercivity.
3. It explicitly proves no segment-depth bound from the global discrete
   pair: the Puiseux denominator \(\kappa_i\) is uncontrolled
   (`SHEET6-DEPTH.md:128-138`).
4. The safe representative bound is
   \(d_0\le2\operatorname{gen}(W)+2\), and only for the cumulative
   jump-cell menu. It does not truncate endpoint frames, degree products,
   E5F data, or tower histories; see
   [`SHEET6-DEPTH-REVIEW.md:183-218`](../SHEET6-DEPTH-REVIEW.md) and
   [`xmodel/sol-normalform.md:385-399`](sol-normalform.md).

In slogan form, depth closure proves a **finite cumulative jump-cell menu per
fixed `M=1` entry**, not equal full frames and not **finitely many
entries**.

---

## 8. Why NF-M cannot restore coercivity

NF-M proves that, for every fixed discrete \(\nu\ge2\) schema whose
coefficient scheme is zero-dimensional modulo scaling, the number of types
is at most

\[
 (\widehat Q-1)!.                                      \tag{8.1}
\]

Positive-dimensional components are retained, not bounded. The total schema
menu and \(\widehat Q\) are bounded only after fixing the entry and budget.
See [`NF-M.md:95-129`](../NF-M.md) and
[`NF-M.md:257-272`](../NF-M.md).

For a fixed finite labelled hierarchy, one fixed schema at each merge, and
zero-dimensional coefficient fibers at every merge, the strongest safe
conditional product is

\[
 \#\{\text{coefficient decorations of fixed schemas}\}
 \le\prod_G(\widehat Q_G-1)!,                          \tag{8.2}
\]

Compatibility can only reduce the right side. Equation (8.2) is not a
product over symbolic schema parameters or retained positive-dimensional
components. It counts decorations of already fixed schemas; it does not
count sheets.

The BB2 cylinder makes the quantifiers exact. For every \(N\ge2\), it has
one NF-M type and the constant FC5 pair `(w,M)=(6,1)`, while its full frame

\[
 (\bar\kappa,d_p,d_q)=(6N+3,4N+1,2N+1)               \tag{8.3}
\]

still varies with \(N\). NF-M's locality theorem requires the same type
**and the same emitted frame**; later consumers can see degrees, `C`, and
orbit values. Therefore

\[
 \forall N\quad \#\mathrm{Types}_N=1,
 \qquad
 \#\coprod_{N\ge2}
   \{N\}\times\mathrm{Types}_N\times\{\mathrm{Frame}_N\}
   =\infty.                                             \tag{8.4}
\]

The schema-relative type may literally have the same symbolic name
`b=-a` for every \(N\); the tagged schema/type/frame triples are distinct.

Proposition 3 is the same phenomenon with `td` itself as the unbounded
parameter.

---

## 9. What the 21-of-22 census does and does not say

Let \(q\) be the number of pole vertices. The pole laws give

\[
 td=\sum_i\Lambda_i,\qquad \Lambda_i\ge\beta.
\]

Writing \(e_i:=\Lambda_i-\beta\ge0\),

\[
 td\le\alpha\beta
 \quad\Longleftrightarrow\quad
 q\le\alpha\ \text{ and }\
 \sum_i e_i\le(\alpha-q)\beta.                        \tag{9.1}
\]

Hence every row with \(q>\alpha\) violates TD-BOUND before any tower is
built. If \(q=\alpha\), equality would require every pole to be
\(\beta\)-minimal; MP4 then forces every `b_i=1`. Thus an off-axis row with
`q=alpha` also violates automatically.

This explains 21 of the 22 violating rows in the filed off-axis sample. The
derivation and row audit are at
[`xmodel/sol-tdbound-review.md:211-257`](sol-tdbound-review.md).
The sample remains useful as a census, but the violation frequency is mostly
a construction effect, not evidence for a conservation law.

The current local books also retain a type-\((2,3)\), `td=9`, three-pole
residue packet of total pole mass `3/2`; after the two bash rounds the panel
is reduced to the residue template rather than killed
([`BOOK-BASH-R2.md:199-232`](../BOOK-BASH-R2.md),
[`BOOK-BASH-R2.md:253-269`](../BOOK-BASH-R2.md)). This is another formal
warning that a global realizability theorem, rather than another local
state count, is required.

---

## 10. The exact global coordinate: mismatch energy

The existing resolved-pencil calculation identifies precisely where new
mathematics must enter.

Let

\[
 \deg f=B\alpha,\qquad \deg g=B\beta.
\]

Resolve the two projective pencils simultaneously. For each proper or
infinitely-near base center \(p\), let \(R_p,S_p\) be the multiplicities of
generic members of the two pencils, using zero when a center belongs only to
one. In the orthogonal total-transform basis,

\[
 C=B\alpha H-\sum_pR_pE_p^*,\qquad
 D=B\beta H-\sum_pS_pE_p^*.
\]

Because general pencil fibers have square zero and meet in the affine plane
in `td` points,

\[
 \sum_pR_p^2=B^2\alpha^2,\qquad
 \sum_pS_p^2=B^2\beta^2,\qquad
 \sum_pR_pS_p=B^2\alpha\beta-td.
\]

Expanding the square gives the **PROVED** identity

\[
 \boxed{
 \frac{td}{\alpha\beta}
 =\frac12\sum_p
 \left(\frac{R_p}{\alpha}-\frac{S_p}{\beta}\right)^2.} \tag{10.1}
\]

Combining with the pole formula gives

\[
 \boxed{
 \sum_P\frac{a_Pb_P}{\nu_P}
 =\frac12\sum_p
 \left(\frac{R_p}{\alpha}-\frac{S_p}{\beta}\right)^2.} \tag{10.2}
\]

Equivalently, for

\[
 \Delta:=C/\alpha-D/\beta,
\]

\[
 \Delta^2=-\frac{2td}{\alpha\beta}.                   \tag{10.3}
\]

The derivation is recorded in
[`xmodel/sol-tdbound-review.md:349-427`](sol-tdbound-review.md). No local
identification of an individual pole summand with an individual resolution
center is currently proved.

### Exact equivalent global reformulation

> **CONJECTURE KME-2 (Keller mismatch-energy bound).** For every
> Sigray-normalized polynomial Keller pair of type \((\alpha,\beta)\), on a
> common resolution of its two projective pencils,
> \[
>   \sum_p\left(\frac{R_p}{\alpha}
>                    -\frac{S_p}{\beta}\right)^2\le2. \tag{KME-2}
> \]

By (10.1)--(10.3), KME-2 is exactly equivalent to

\[
 \sum_P\frac{a_Pb_P}{\nu_P}\le1,\qquad
 td\le\alpha\beta,\qquad \Delta^2\ge-2.              \tag{10.4}
\]

KME-2 is not an independent mechanism lemma: by (10.1), it is TD-BOUND
rewritten in exact global coordinates. Its value is diagnostic. It proves
that the missing mechanism must control normalized divergence energy, but it
does not by itself advance the inequality.

**Hardness: 9/10.** The exceptional lattice alone does not imply KME-2.
Even support on an ADE configuration is insufficient: multiples of a root
have arbitrarily negative square. The theorem must constrain the
coefficients of the normalized difference divisor, using the constant
Jacobian and proximity relations at the centers where normalized
multiplicities diverge.

### A more structural sufficient target

The following statement is stronger than KME-2 but gives a concrete bridge
from common-power contacts to the required global inequality.

> **CONJECTURE PCC (proportional-center coverage).** At every resolved base
> center put
> \[
> h_p:=\min\!\left(
>       \left\lfloor\frac{R_p}{\alpha}\right\rfloor,
>       \left\lfloor\frac{S_p}{\beta}\right\rfloor
>       \right).
> \]
> Then
> \[
> \sum_ph_p^2\ge B^2-1.                               \tag{PCC}
> \]

If PCC holds, then

\[
 I_\infty=\sum_pR_pS_p
 \ge\alpha\beta\sum_ph_p^2
 \ge\alpha\beta(B^2-1),
\]

and hence `td <= alpha*beta`. Corollary 7.4's common powers are plausible
sources of the \(h_p\), but the needed weighted/Laurent-to-projective
transport, proximity accounting, distinct-center coverage, and no-double-
counting theorem do not exist in the repository.

**Hardness: 8.5/10.** This is the most concrete proof lane found. FC5 could
participate only after an emission-to-proximity theorem says which base
centers and which source increments a chart represents. Its current pair
`(w,M)` does not contain that information.

### The smallest sector lemma an emission proof must import

> **CONJECTURE SP (single-pole cap).** If a one-pole Sigray configuration is
> globally realizable by a polynomial Keller pair, then
> \[
>   ab\le\nu.                                           \tag{SP}
> \]

SP is exactly TD-BOUND in the one-pole sector. It is necessary for any
merge-based proof, because there is no multi-leaf merge in that sector. The
family in Proposition 3 satisfies the current local rules while violating SP
by an unbounded factor.

KME-2 already implies SP as its one-pole specialization; SP is not an
additional hypothesis if KME-2 is assumed. It is isolated because it is the
smallest necessary sector test for any proposed emission-based mechanism.

**Hardness: 8/10.** A proof must use global gluing/algebraization or force
unbooked charge. Refining FC5 cannot prove SP because FC5 has no incoming
merge to compare.

### Relaxed finite typewise target

Even a nonsharp finite bound would require:

> **CONJECTURE KME-finite.** For each fixed \((\alpha,\beta)\), there is an
> effective constant \(C_{\alpha,\beta}<\infty\), independent of the degree
> scale and tree, such that
> \[
>   \sum_p\left(\frac{R_p}{\alpha}
>                    -\frac{S_p}{\beta}\right)^2
>       \le C_{\alpha,\beta}.                          \tag{KME-finite}
> \]

Then

\[
 td\le\frac{\alpha\beta}{2}C_{\alpha,\beta}.          \tag{10.5}
\]

Proposition 3 shows that KME-finite is not encoded in the current local
laws even for type `(2,3)`. Its proof would already be new global geometry.

---

## 11. Why a universal absolute `td` bound is not an intermediate theorem

### Proposition 4 (iteration obstruction)

**PROVED.** Let \(F:\mathbb A^2\to\mathbb A^2\) be a nonautomorphic Keller
map with \(td(F)=d>1\). Then for every \(k\ge1\), \(F^k\) is a
nonautomorphic Keller map and

\[
 td(F^k)=d^k.                                          \tag{11.1}
\]

The Jacobian determinant follows from the chain rule. For topological
degree, the pullback \(F^*\) embeds the rational function field into itself,
and

\[
 [K:(F^k)^*K]
 =\prod_{j=0}^{k-1}[(F^j)^*K:(F^{j+1})^*K]
 =d^k.                                                 \tag{11.2}
\]

Every factor is \(d\), because \((F^j)^*:K\to(F^j)^*K\) is a field
isomorphism carrying \(F^*K\) to \((F^{j+1})^*K\). The identification
`td(F)=[K:F^*K]` is recorded at
[`REDUCTION.md:65-81`](../REDUCTION.md).

Finally, an automorphism has topological degree one, whereas (11.1) gives
\(td(F^k)=d^k>1\). Hence every iterate remains nonautomorphic.

Consequently:

> **PROVED LOGICAL COROLLARY.** For any fixed finite \(N\), the statement
> “every plane Keller counterexample has `td <= N`” implies that there are no
> plane Keller counterexamples. Conversely, if the Jacobian conjecture is
> true, that bound is vacuously true. Thus existence of a universal absolute
> bound is logically equivalent to JC2, not a weaker intermediate rung.

The premise \(d>1\) covers every counterexample here: the published bound
in [`REDUCTION.md:340-351`](../REDUCTION.md) gives in fact \(td\ge6\).

This does not obstruct a bound on a *selected globally minimal*
counterexample. Iteration is precisely why that quantifier must be stated.

---

## 12. TD-BOUND alone does not make the book ladder cofinal

The sharp conjecture gives only

\[
 td\le\alpha\beta.                                    \tag{12.1}
\]

The current GGV Algorithm 8 catalog is finite only after an explicit input
degree/valuation bound. It is not an absolute finite list of possible types.
This is stated in
[`REDUCTION.md:225-267`](../REDUCTION.md) and
[`REDUCTION.md:887-904`](../REDUCTION.md), and reiterated in
[`xmodel/sol-tdbound-review.md:279-325`](sol-tdbound-review.md).

Therefore the cofinality sentence in `TDBOUND.md:97-103` is not currently a
theorem. A second global compactness statement is required:

> **CONJECTURE SC (selected-counterexample type cap).** There exists an
> a priori explicitly computable integer \(B_0\), fixed independently of
> any unknown counterexample and independently of its unknown GGV minimum,
> such that: if a plane Keller counterexample exists, some globally minimal
> GGV pair selected for the reduction has transported Sigray type satisfying
> \[
>   \alpha\beta\le B_0                              \tag{SC}
> \]

KME-2 plus SC would give `td <= B_0` for that selected pair and would avoid
the iteration obstruction, because it does not claim a bound for every
iterate. A direct selected-pair `td` bound would serve the same purpose.

**Hardness: 10/10.** No current GGV or sheet theorem supplies an upper type
or degree bound. In addition, cofinal enumeration still needs a
completeness-preserving fixed-rung symbolic quotient: NF-Z, NF-P, generalized
NF-M, off-axis `b>=2` termination, and all full-route landing sectors.
These obligations are recorded at
[`xmodel/sol-normalform.md:401-486`](sol-normalform.md) and
[`REDUCTION.md:851-904`](../REDUCTION.md); they include post-jump `M>=2`
suffixes and mixed later merges.

---

## 13. Final dependency ledger

| desired conclusion | what the present inputs prove | exact missing item | rating |
|---|---|---|---:|
| FC5 state after a chart | equation (1.1), type- and coefficient-independent | none | proved |
| finite depth quotient at fixed entry | finite `w`/jump menu on `M=1` ancestry | `M>=2` and full-history closure | existing perimeter |
| finite coefficient quotient at fixed schema | at most `(Qhat-1)!` isolated types | zero-dimensionality and cross-schema properness | existing perimeter |
| single-pole mass `<=1` | no bound; Proposition 3 is locally unbounded | **CONJECTURE SP** | 8/10 |
| full pole mass `<=1` | exact reformulation as mismatch energy | **CONJECTURE PCC** or another global Keller/proximity mechanism proving KME-2 | 9/10 |
| any finite bound for fixed type | no bound from local laws | **CONJECTURE KME-finite** | 9/10 |
| absolute cofinal book ladder | not supplied by TD-BOUND or GGV catalog | **CONJECTURE SC** plus full landing | 10/10 |
| universal absolute bound on every counterexample | would contradict iterates of any one counterexample | equivalent to JC2 | 10/10 |

## Conclusion

The merged-emission law is valuable as a deterministic transition rule, but
it is not the missing global accountant. Its exact pole-mass interface is
\(\Phi_s\); that potential is nonmonotone on coefficient-solvable local
charts. More decisively, the extracted arithmetic relaxation admits an
arbitrarily large fixed-type scale with constant FC5 output. Depth closure
and NF-M then quotient what remains only after the unbounded entry/schema
parameters have been fixed.

The exact sharp target is KME-2, and the relaxed target is KME-finite; both
require a new global Keller/proximity mechanism at divergence centers. PCC is
the most concrete sufficient mechanism found. SP is the smallest necessary
sector test for an emission-based route, not an extra assumption beyond
KME-2. Absolute book cofinality additionally requires a selected-
counterexample type cap and full-configuration landing.

No `td` upper bound, sharp or weak, is proved here. The new proved output is
the obstruction: **the present FC5 + depth + NF-M bookkeeping is
noncoercive, even at fixed type, and the precise missing information is the
global normalized mismatch/proximity energy.**
