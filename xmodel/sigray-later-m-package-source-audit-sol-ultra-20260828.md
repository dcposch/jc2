# Sigray pp. 39--45: independent source audit of the later `M` package

**Date:** 2026-08-28  
**Mode:** desk/light exact; primary source plus canonical-consumer read  
**Status:** producer report; no canonical promotion is made here

## 0. Custody, scope, and bottom line

Primary source: `refs/sigray_full.pdf`, printed page = PDF page, SHA-256

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
```

The audited block is Notation 8.1, Statement 8.1, Proposition 8.1,
Statements 8.2--8.5, Propositions 8.2--8.4, and Corollary 8.1, printed
pp. 39--45.  Earlier source statements were reread only where this block
actually consumes them, especially Proposition 4.2, Proposition 4.6,
Statements 3.9/3.16/3.17/3.18, Theorem 6.1, Statements 6.1/6.2,
Propositions 6.3/6.6/6.7/6.8, and Corollary 6.1.

Bottom line:

1. **Statement 8.4 survives** after a short UFD/valuation repair.  Its exact
   content is the edge law
   \[
      G=F+c,\quad F,G\in T_a^{\searrow}\cap V_a
      \quad\Longrightarrow\quad
      \operatorname{mult}(p_F^{\rm red},c)\mid M_G.
   \]
   Here `+c` moves from the lower/rootward vertex `F` to its upper child
   `G`, so `F=G^\circ`.  This statement does **not** say that `M_F` divides
   `M_G`, and it is not Proposition 8.4.

2. **Proposition 8.4 survives for nonroot vertices only.**  The clean
   corrected statement is
   \[
   T_{a,\mathrm{pole}}=\{G\}
   \quad\Longrightarrow\quad
   M_F\ne1
   \quad\text{for every }F\in T_a^{\searrow}\cap
       (V_a\setminus\{(0,y)\}).
   \]
   Its printed proof is repairable on that domain.

3. **The printed root clause is a genuine endpoint gap.**  If the starting
   vertex is `F=(0,y)`, the printed descent has length `n=0` and the next
   line `H:=F_{n-1}` is undefined.  The repaired Proposition 8.3 propagates
   `M=1` rootward; it cannot propagate `M_{(0,y)}=1` upward to a nonroot
   vertex.  The singleton-pole hypothesis gives a unique down child but no
   reverse `M` propagation.  Thus the source proves no contradiction from
   `M_{(0,y)}=1`.

4. This audit does **not** claim that the root clause is false for an actual
   Keller counterexample.  The displayed root ODE and normalization data
   permit `M=1` packets, but the simplest such packet fails an additional
   polynomial approximate-root lift test recorded in Section 11.  The
   precise verdict is therefore **UNPROVED / QUARANTINE**, not counterexample.

5. The current high-value canonical uses of Proposition 8.4 at a **pole
   entry** are nonroot and remain valid.  The current uses that force or
   forbid `M_{(0,y)}=1`, or claim a suffix theorem including the root, must
   be rolled back.  `papers/paper2/main.tex` imports Statement 8.4 but not
   Proposition 8.4, so its advertised edge divisibility law is unaffected.

No web, AWS, or remote computation was used.  No canonical file and no file
under `jc2-lean` was edited.

## 1. Orientation and notation (the source is easy to misread here)

Write `T_a^\searrow` for the source's `T_a&`:

\[
 T_a^\searrow=\{F\in T_a^+:d_F<(1-\pi(F))\deg p_F\}.
\]

For a nonroot vertex `U`, `U^\circ` is the next adjacent vertex toward the
root (Notation 3.3).  Proposition 3.2 writes the reverse relation as
`U=U^\circ+c`.  Thus in Statement 8.4, `G=F+c` means

```text
upper child G  ----degree = multiplicity---->  lower parent F=G°
```

whereas Proposition 8.4 starts at an upper vertex and repeatedly applies
`°` until reaching `(0,y)`.

For a vertex where Proposition 4.2's tower is defined, write

\[
 h_0=g,\ h_1,\ldots,h_m=h_F,
\qquad
 (h_{j,F}^+)^{k_j}=s_j(f_F^+)^{l_j}\quad(0\le j<m),
\]

with `gcd(k_j,l_j)=1`.  The correct degree ratio is

\[
 \frac{\deg p_{h_j,F}}{\deg p_F}=\frac{l_j}{k_j};
\]

several displayed computations on pp. 40--43 reverse this ratio.

## 2. Notation 8.1 and Statement 8.1

### 2.1 Exact repaired domain

The source prints `F\in T_a` in Notation 8.1 and `F\in V_a` in Statement
8.1, but `m_F,h_{j,F}` are imported from Proposition 4.2, whose domain is
`T_a^+`.  The typed version is therefore:

> Let `F` lie in the domain of the Proposition 4.2 tower (in this package,
> it is enough to take `F\in T_a^+`).  Put `m=m_F` and `h_j=h_{j,F}`.  Define
> \[
> M_F=\gcd(\deg p_F,\deg p_{h_0,F},\ldots,\deg p_{h_m,F}),
> \]
> \[
> M_F^*=\gcd(\deg p_F,\deg p_{h_0,F},\ldots,
>                     \deg p_{h_{m-1},F}).
> \]

For `m=0`, the second gcd has only `deg p_F`, so `M_F^*=deg p_F`.
The already-promoted Proposition 4.2 constant-corner repair can add a
zero-degree preterminal member; the standard convention `gcd(n,0)=n`
keeps the definitions typed.  That corner does not occur on the down-domain
used below.

Statement 8.1 is then just Bezout for these finite lists of nonnegative
integers: there are integer coefficients representing `M_F` and `M_F^*` as
integer linear combinations of the listed degrees.  Negative coefficients
are allowed and are crucial later.

### 2.2 Trust verdict

**PASS after domain repair.**  No geometric theorem is hidden in Statement
8.1.  Its danger is downstream: an integer Bezout combination of degrees
does not make the corresponding product of polynomials a polynomial when
some coefficients are negative.

## 3. A missing local lemma that repairs Corollary 6.1 and Proposition 8.1

This is the omission suggested in the source audit, and it checks exactly.
Let `F\in T_a^\searrow`, put

\[
 u=\pi(F),\quad p=p_F,\quad q=p_{h_F,F},\quad
 d=d_F,\quad e=d_{h_F,F},\quad \mu=\mu_F.
\]

For a root `c` of `p`, put `a=mult(p,c)` and `b=mult(q,c)`.  Proposition
4.6 says either local cancellation (12) and the ratio (13) hold,

\[
 a+b-1<\mu a,\qquad \frac ab=\frac de,
\]

or the exact order relation (14) holds,

\[
 a+b-1=\mu a.
\]

But Proposition 4.2(iv) gives

\[
 e=(\mu-1)d+1-u,
 \qquad
 \frac ed=\mu-1+\frac{1-u}{d}>\mu-1,
\]

because a down vertex has `u<1`.  Under (12)+(13),

\[
 b=\frac eda>(\mu-1)a.
\]

Equation (11), whose right side is a nonzero scalar times `p^\mu`, implies
`\mu a\in\mathbb Z`; hence `(\mu-1)a\in\mathbb Z`.  Therefore

\[
 b\ge(\mu-1)a+1,
\]

contradicting (12), which says `b<(\mu-1)a+1`.  Consequently, at **every**
root of `p` and for every down vertex,

\[
 \boxed{\operatorname{mult}(q,c)
       =(\mu-1)\operatorname{mult}(p,c)+1.}\tag{L6-root}
\]

This proof does not use Proposition 6.7.

For the printed Corollary 6.1, now assume additionally
`F\in V_a\setminus\{(0,y)\}`.  If the degree ratio were not the order ratio,
the degree alternative in Proposition 4.6 would give

\[
 \deg q=(\mu-1)\deg p+1.
\]

Summing (L6-root) over the `r` distinct roots of `p` gives

\[
 \deg q\ge(\mu-1)\deg p+r.
\]

Thus `r=1`, contradicting Statement 3.16, which gives more than one root at
a nonroot vertex of `V_a`.  Hence

\[
 \boxed{\frac{\deg q}{\deg p}=\frac ed}
 \quad\text{and}\quad F\prec F'
\]

for a sufficiently fine next microstep, exactly as Corollary 6.1 intends.

The printed proof instead cites Proposition 6.7 for (L6-root).  Proposition
6.7 does not state it: it gives a down-child alternative.  This arithmetic
repair is therefore load-bearing.  It is used directly in Proposition 8.1's
polynomiality step and indirectly in the tower comparisons used in
Statements 8.3--8.5 and Proposition 8.4.  Corollary 6.1 itself still excludes
the root; it cannot settle the root endpoint of Proposition 8.4.

## 4. Proposition 8.1: exact statement and complete repair

Let `F\in T_a^\searrow`, `u=\pi(F)`, and

\[
 i=\frac{\deg p_F}{M_F^*}.
\]

Then `i\in\mathbb N^*`, and, up to the source's suppressed nonzero scalars,
there are `p,q\in\mathbb C[\eta]` and `\delta\in\mathbb Q` such that

\[
 (\xi^\delta p)^i=f_F^+,\tag{8.1-i}
\]
\[
 h_F^+=\xi^{1-u}(\xi^\delta p)^kq,
 \qquad k=i(\mu_F-1)\in\mathbb Z,\tag{8.1-ii}
\]
\[
 J(\xi^\delta p,\xi^{1-u}q)=\mathbin{\ominus}\xi^{\delta-u}p,\tag{8.1-iii}
\]
\[
 \delta p q'-(1-u)p'q=\mathbin{\ominus}p,\tag{8.1-iv}
\]
and
\[
 M_F=\gcd(\deg p,\deg q).\tag{8.1-v}
\]

### 4.1 Negative Bezout exponents and the perfect-power conclusion

Let `D=deg p_F` and `D_j=deg p_{h_j,F}` for `j<m`.  From the tower,

\[
 D_j=\frac{l_j}{k_j}D,
\]

not `(k_j/l_j)D`.  Since the fractions are reduced,

\[
 i=\frac{D}{\gcd(D,D_0,\ldots,D_{m-1})}
   =\operatorname{lcm}(k_0,\ldots,k_{m-1}).
\]

For every irreducible factor `r` of `p_F`, the tower equality gives

\[
 k_j v_r(p_{h_j,F})=l_jv_r(p_F),
\]

so `k_j|v_r(p_F)` and hence `i|v_r(p_F)` for every `j`.  UFD factorization
therefore gives `p_F=\mathbin{\ominus}p^i` with a polynomial `p`.

The source instead defines `\xi^\delta p` immediately by a Bezout product

\[
 (f_F^+)^{N^*}\prod_{j<m}(h_{j,F}^+)^{N_j^*}.
\]

Because the Bezout coefficients can be negative, this expression is initially
only a rational/Laurent function.  Its valuation at every irreducible factor
is `v(p_F)/i\ge0`; only **after** this valuation calculation may it be called
a polynomial times a monomial in `\xi`.  That is the missing
negative-exponent/perfect-power justification.

Since every `k_j|i`, the tower formula for `\mu_F` gives `i\mu_F\in\mathbb Z`
and therefore `k=i(\mu_F-1)\in\mathbb Z`.

### 4.2 Polynomiality of `q`

Define `q` first in the rational function field by dividing the terminal
pattern by the factor in (8.1-ii).  If `k\le0`, polynomiality is immediate.
If `k>0`, its only possible finite poles occur at roots of `p`.  Since
`p_F=\mathbin{\ominus}p^i`, (L6-root) gives at every such root

\[
 v(p_{h_F,F})=(\mu_F-1)v(p_F)+1=k\,v(p)+1,
\]

and hence `v(q)=1`.  Thus `q` is a polynomial.  The source's citation of
Proposition 6.3 for this exact root-order formula is wrong; the repaired
local lemma above is what is needed.

The chain rule now proves (iii), its one-variable expansion proves (iv), and

\[
 \deg p_{h_F,F}=k\deg p+\deg q,
 \quad M_F^*=\deg p
\]

proves (v).

### 4.3 Printed slips on pp. 39--41

The proof survives, but the following are real transcription/logic slips:

- the raw Bezout product is called a polynomial before negative exponents
  are controlled;
- “`j=1/i` proves property (ii)” should say property (i);
- `i\mu_G` should be `i\mu_F`;
- `H(\xi,u)` should be `H(\xi,\eta)`;
- the calculation obtains exponent `1-u`, while the next line prints
  `H=\xi^{u-1}q`;
- Proposition 6.3 is the wrong source for the root-order equality;
- the proof of (v) prints `M_F` twice where `M_F^*` is required.

**Verdict:** Proposition 8.1 is valid after these explicit repairs.

## 5. Statements 8.2 and 8.3

### 5.1 Statement 8.2 must exclude the root

With Proposition 8.1's notation, the intended nonroot statement is:

> If
> `F\in(T_a^\searrow\cap(V_a\setminus\{(0,y)\}))\setminus T_{a,pole}`
> and `G=F+c`, then
> \[
>   \deg(q)\operatorname{mult}(p,c)\ne\deg(p),
> \]
> and `G\in T_a^\searrow` exactly when
> \[
>   \deg(q)\operatorname{mult}(p,c)>\deg(p).
> \]

The source includes `(0,y)` but begins the proof with “from Statement 3.16,
`p` has more than one root.”  Statement 3.16 explicitly excludes both roots.
At the root the equality case is compatible with the reduced ODE (Section
11), so this is not merely a missing citation.  **Verdict: valid only after
adding the nonroot restriction.**

### 5.2 Statement 8.3: tower transport

For a sufficiently fine common `\kappa`, the source considers an upper
nonroot down vertex `F=G*c`.  The intended conclusion is that every tower
member through `m_F` is shared and

\[
 h_{j,F}=h_{j,G},\qquad
 \deg p_{h_j,F}=\operatorname{mult}(p_{h_j,G},c)
 \quad(0\le j\le m_F).
\]

The proof needs the repaired Corollary 6.1 and the tower comparison
`F\prec G`.  Every displayed ratio `k_j/l_j` in the proof must be replaced
by `l_j/k_j`.  The same reversal occurs in the terminal `\psi` calculation.
With that correction, the prefix cases follow from the common-power
relations, and the terminal case follows by moving to a sufficiently fine
common microstep and using the repaired degree/order equality.

For later use one needs the adjacent-vertex form, not merely one selected
microstep:

> If `U=L+c` are adjacent down vertices, then `U\prec L`; every tower
> member through `m_U` is shared, and
> \[
> \deg p_{h_j,U}=\operatorname{mult}(p_{h_j,L},c)
> \quad(0\le j\le m_U).
> \]

For `j<m_U` this is the common-power transport.  For the terminal member,
use the corrected terminal ratio at the first sufficiently fine microstep
below `U`, persistence of the common tower along the edge, and Statement
3.17 for `f`.  This makes explicit the hidden tower-comparability step used
in Statements 8.4/8.5 and in the Proposition 8.4 axis computation.

**Verdict:** valid after the systematic ratio correction and the repaired
Corollary 6.1.

## 6. Statement 8.4: multiplicity divides the child's `M`

Let `F,G\in T_a^\searrow\cap V_a`, with `G=F+c`, and let `p` be the reduced
polynomial at the lower vertex `F` from Proposition 8.1.  Then

\[
 \boxed{\operatorname{mult}(p,c)\mid M_G.}
\]

### 6.1 Clean proof (no Bezout product is needed)

Put `m=m_G`.  Strict tower comparison gives `G\prec F`; hence every
`h_{j,G}`, `0\le j\le m`, is the same polynomial as a **nonterminal** tower
member at `F`.  Proposition 8.1's UFD argument at `F` therefore gives

\[
 p_F=\mathbin{\ominus}p^i,
 \qquad
 p_{h_j,F}=\mathbin{\ominus}p^{r_j}\quad(r_j\in\mathbb N^*).
\]

Let `a=mult(p,c)`.  Adjacent transport gives

\[
 \deg p_G=i a,
 \qquad
 \deg p_{h_j,G}=r_j a\quad(0\le j\le m).
\]

Their gcd is `M_G`, so `a|M_G`.

### 6.2 Defects in the printed proof

- The Bezout equation prints `N_m^*` in place of `N_m`.
- The displayed product stops at `h_{m-1,F}` although the very next
  valuation sum uses the coefficient of `h_{m,F}`.  The terminal factor is
  visibly missing.
- Negative Bezout exponents are again ignored, so the product is rational,
  not automatically polynomial.
- Proposition 6.7 is cited for polynomiality/perfect-power structure that it
  does not state.
- The last transported degree has subscript `F` where `G` is required.

One can also repair the source's route: include the `h_m` factor, regard the
product as rational, observe that every factor is a power of `p`, and use its
positive `c`-valuation `M_G` to conclude that it is a positive integral power
of `p`.  The direct gcd proof above is shorter and exposes all typing.

**Verdict:** PASS after repair.  This producer is independent of the root
endpoint defect in Proposition 8.4.

## 7. Statement 8.5, Proposition 8.2, and Corollary 8.1

### 7.1 Statement 8.5

If `F` is an upper down vertex, `G=F^\circ`, and `G\notin V_{2,a}`, the
intended conclusion is

\[
 M_G\mid M_F.
\]

The proof is repairable.  It uses the same strict tower comparison and the
same `l_j/k_j` degree ratios as Statement 8.3.  At a one-orbit lower vertex,
the prefix degrees are `\nu_G` times the transported upper degrees.  The
terminal residual has the form

\[
 p_{h_G,G}(\eta)=\eta^\epsilon r(\eta^{\nu_G}),
 \qquad \epsilon\equiv1\pmod{\nu_G},
\]

so its degree is coprime to the common `\nu_G` factor.  The source's last
line must read

\[
 \gcd(\nu_G,\deg p_{h_G,G})=1,
\]

not `p_{h,F}`.  The systematic `k/l` inversions earlier in the proof must
also be corrected.  At a root direction `c` can be zero; the printed
`c\in\mathbb C^*` is unnecessarily narrow.

**Verdict:** PASS after these corrections.

### 7.2 Proposition 8.2 / Corollary 8.1

Proposition 8.2 starts with a Bezout representation of `M_F` and forms a
product at `G=F^\circ`.  Again, negative exponents make the raw product
rational.  In addition, the source product starts at `j=1` and omits the
`h_0` factor while its Bezout equation contains `N_0`; the product must run
from `j=0` through `m`.

After correction, all prefix factors at `G` are common powers.  The product's
valuation at the distinguished direction is `M_F>0`; hence it is a positive
power of the common reduced polynomial and therefore polynomial.  This is
the missing positivity step before Statement 6.1 is invoked.  The already
repaired Proposition 6.7 supplies positivity of the required microsteps.

Thus Proposition 8.2 and its `M_F=1` specialization Corollary 8.1 survive.
Both already exclude `(0,y)`.

## 8. Proposition 8.3: printed hypothesis impossible; exact repair

The source takes a nonroot down vertex `F`, puts `G=F^\circ`, and then assumes

> for every down nonroot `H`, `G\ne H^\circ`.

Taking `H=F` contradicts the setup.  The only coherent hypothesis, and the
one used by the proof, is unique down-child regularity:

\[
 \boxed{
 \{H\in T_a^\searrow\cap(V_a\setminus\{(0,y)\}):H^\circ=G\}=\{F\}.}
 \tag{Reg}
\]

Under (Reg) and `M_F=1`:

1. `M_G=1`.
2. If `G\ne(0,y)`, then
   \[
   p_G(\eta)=\mathbin{\ominus}(\eta^{\nu_G}-c^{\nu_G})^r,
   \qquad c\in\mathbb C^*,\quad \nu_G\ne1,
   \]
   for some `r\in\mathbb N^*`.
3. If `G=(0,y)`, then `p_G(\eta)=(\eta-c)^r` for some
   `r\in\mathbb N^*`.

For (1), Corollary 8.1 makes every existing child direction at `G` down.
If `G\in V_{2,a}`, the repaired microstep-to-next-vertex bridge from
Propositions 6.7/6.8 produces a second down actual child, violating (Reg).
Hence `G\notin V_{2,a}`, and Statement 8.5 gives `M_G|M_F=1`.

For (2), `G\in V_{1,a}\setminus V_{2,a}` and Statements 3.16/3.18 give the
single-orbit shape.  The capital exponent `M` printed in Proposition 8.3(ii)
is unbound.  The intended exponent is simply

\[
 r=\deg p_G/\nu_G;
\]

it is **not** `M_G` (which equals one).  Proposition 8.3(ii) is not used by
the minimal proof of Proposition 8.4 and can safely be quarantined if this
repair is not adopted.

For (3), the printed citation of Statement 3.16 is outside that statement's
domain.  Instead use the definition of root directions: two distinct roots
would give two down children, contrary to (Reg); at `\nu_G=1` this is exactly
the asserted one-root form.

**Verdict:** the printed proposition is vacuous; repaired (Reg) makes (i)
and (iii) valid.  Only those two clauses belong to the minimal Proposition
8.4 trust set.

## 9. Proposition 8.4: the repaired nonroot theorem

### 9.1 Singleton sibling exclusion

Suppose `T_{a,pole}={G_*}`.  At any rootward vertex on a down chain, two
distinct down upper siblings would lie in disjoint branches.  The repaired
Proposition 6.8 places a pole weakly above each sibling on the **same**
branch.  Those poles are distinct, contradicting the singleton hypothesis.
Thus every rootward step of the chain has the unique-child property (Reg).
This is the hidden use of the singleton hypothesis in the printed proof.

### 9.2 Descent and `M=1` propagation

Let

\[
 F_0=F,\qquad F_{j+1}=F_j^\circ,
\]

until `F_n=(0,y)`.  The source prints `F_{n+1}=F^\circ`; this is an index
typo.  Rootward preservation of the down condition follows from the
monotonicity in Proposition 6.6 (contrapositive) and Statement 6.1; the
repaired Propositions 6.7/6.8 give the needed branch realization.  If the
start `F` is nonroot then `n\ge1`, and `H:=F_{n-1}` is defined.

Assuming `M_F=1`, repaired Proposition 8.3(i), applied at each regular
step, gives `M_H=1`.  Proposition 8.3(iii), at the last step, gives a single
root `c` for `p_{(0,y)}`.

### 9.3 The hidden axis contradiction

Choose Bezout coefficients at `H`:

\[
 1=N\deg p_H+\sum_{j=0}^{m_H}N_j\deg p_{h_j,H}.
\]

Use the same coefficients on the root degree/order vectors:

\[
 (K,L)=N(\deg p_R,d_R)+
       \sum_{j=0}^{m_H}N_j(\deg p_{h_j,R},d_{h_j,R}),
 \qquad R=(0,y).
\]

The strict tower comparisons along the chain make every vector in this sum
proportional to the normalized root axis `(k_f,l_f)`.  This comparability is
not stated at the point of use in the source; it is exactly the repaired
Corollary 6.1 + Proposition 6.3/tower-persistence input.

At the last edge, adjacent transport and the one-root conclusion give

\[
 \deg p_R=\operatorname{mult}(p_R,c)=\deg p_H
\]

and the same equality for every shared `h_j`.  Consequently `K=1`.
Both `K,L` are integers, while `(K,L)=w(k_f,l_f)`; hence

\[
 w=1/k_f,\qquad L=l_f/k_f.
\]

Because `l_f>0`, `L` would be a positive integer.  Theorem 6.1 says
`0<l_f/k_f<1`, contradiction.

This proves:

> **Corrected Proposition 8.4.**  For a normalized counterexample with
> `T_{a,pole}` a singleton, `M_F\ne1` for every
> `F\in T_a^\searrow\cap(V_a\setminus\{(0,y)\})`.

The proof uses ordinary integer Bezout coefficients at `H`; unlike the
polynomial products in Propositions 8.1/8.2 and Statement 8.4, no illegal
negative polynomial exponent occurs in this final axis step.

## 10. Why the root is not an implicit `n=0` case

For `F=(0,y)`, the descent stops immediately: `n=0`.  The source's
`H=F_{n-1}` is undefined, there is no last upper edge, and Proposition 8.3
has no place to manufacture the one-root transport from a nonroot `M=1`
vertex.

The direction of every available `M` law is wrong for a repair:

- Proposition 8.3(i) propagates `M=1` from an upper nonroot vertex to its
  lower parent.
- Statement 8.5 gives `M_{\rm lower}|M_{\rm upper}` at a regular step;
  `M_{(0,y)}=1` is therefore vacuous information about the child.
- Statement 8.4 gives
  `mult(p_{(0,y)}^{red},c)|M_{\rm child}`.  It can force the child `M` to be
  large; it cannot force it to be one.
- The singleton-pole hypothesis excludes a second down child, but supplies
  no reverse divisibility.

Therefore one cannot “first descend” from a root `M=1` to a nonroot `M=1`:
the root is already the terminal object and all propagation is rootward.
Conversely, whenever a canonical calculation finds `M=1` at any **nonroot**
chain vertex, the corrected theorem applies directly and the contradiction
remains valid.

The root must be treated as a separate theorem.  No such theorem has been
proved in the audited source package.

## 11. Root data: what is compatible, and why no full witness is claimed

At `R=(0,y)`, normalization and the chart equalities give

\[
 (\deg p_R,d_R)=(k_f,l_f),\qquad
 (\deg p_{g,R},d_{g,R})=(k_g,l_g),
\]

with

\[
 (k_f,l_f)=(a\alpha,b\alpha),\qquad
 (k_g,l_g)=(a\beta,b\beta),\qquad 0<b<a,
\]

where `(\alpha,\beta)` is the reduced type.  Thus `R\in T_a^\searrow` by
Theorem 6.1; lack of down-typing is **not** the root problem.

Proposition 8.1 reduces the root terminal identity to

\[
 \delta p q'-p'q=\mathbin{\ominus}p,
 \qquad M_R=\gcd(\deg p,\deg q).
\]

If `A=deg p` and `B=deg q`, top-degree comparison gives either `B=1` or
the resonant equality `\delta B=A`.  Neither alternative contradicts
`0<\delta<A` or the type conditions by itself.  For example the reduced
ODE packet

\[
 p=\eta^2,\quad q=\eta,\quad\delta=1
\]

satisfies

\[
 pq'-p'q=-p,\qquad \gcd(2,1)=1.
\]

Together with type `(2,3)` it gives the associated-leading-form packet

\[
 f_R^+=\xi^2\eta^4,\quad g_R^+=\xi^3\eta^6,\quad
 h_R^+=\xi^2\eta^3,
\]

and

\[
 J(f_R^+,h_R^+)=-2\xi^3\eta^6
             =\mathbin{\ominus}(f_R^+)^{3/2}.
\]

This packet demonstrates that the **displayed** root ODE, Jacobian-leading
identity, gcd formula, down inequality, and normalization ratios do not by
themselves yield a contradiction.  It is not, however, a fully typed
polynomial-tower witness.  For the simplest one-step tower, write the most
general primary-variable degree `(2,3)` polynomials as

\[
 F=P^2Y^2+aY+b,\qquad
 G=P^3Y^3+cY^2+dY+e.
\]

Requiring `G^2-F^3` to have degree at most two forces

\[
 c=\frac32Pa,qquad
 d=\frac32Pb+\frac{3a^2}{8P},qquad
 e=\frac{3ab}{4P}-\frac{a^3}{16P^3},
\]

and its `Y^2` coefficient is

\[
 -\frac{3(4P^2b-a^2)^2}{64P^2}.
\]

For `P=X^2`, polynomiality forces enough `X`-divisibility that this
coefficient is divisible by `X^4`; it cannot be the proposed `X^3`.
Accordingly, the tempting packet does **not** prove a polynomial lift
`h_1=g^2-f^3`, and it is not evidence that the theorem is false.

What remains established is narrower and sufficient for source custody:
the printed proof does not cover the root, the repaired pp. 39--45 identities
do not furnish a reverse propagation, and a separate polynomial/global
argument is required.  Until supplied, `M_{(0,y)}\ne1` is quarantined.

## 12. Minimal Proposition 8.4 trust set versus the full pp. 39--45 package

### 12.1 Minimal trust set for the corrected nonroot Proposition 8.4

The proof in Section 9 needs only:

- the typed gcd/Bezout definitions in Notation/Statement 8.1;
- repaired Corollary 6.1 and the tower-comparability/adjacent transport
  consequence of Statement 8.3;
- Proposition 8.2 and Corollary 8.1, with the rational-product repair;
- Statement 8.5, with its ratio/subscript repair;
- corrected Proposition 8.3(i) and (iii) under (Reg);
- the repaired same-branch Propositions 6.7/6.8 for sibling exclusion;
- Statements 3.9/3.17/3.18, Proposition 6.6/Statement 6.1 for descent, and
  Theorem 6.1 for the final axis contradiction.

It does **not** consume:

- Statement 8.2;
- Statement 8.4 (the edge multiplicity divisor);
- Proposition 8.3(ii), including its undefined exponent;
- the root clause of Proposition 8.4.

This separation matters: Statement 8.4 can be promoted as an independent
producer even while the root endpoint remains quarantined.

### 12.2 Full package liabilities

The full pp. 39--45 package additionally carries:

- every negative-Bezout-exponent repair in Propositions 8.1/8.2 and
  Statement 8.4;
- the UFD perfect-power argument and delayed polynomiality of `q`;
- the root exclusion in Statement 8.2;
- all `k_j/l_j` to `l_j/k_j` repairs in Statements 8.3/8.5;
- the unique-child correction to Proposition 8.3;
- quarantine or renaming of the exponent in Proposition 8.3(ii);
- the nonroot restriction in Proposition 8.4.

## 13. Canonical consumer census and precise rollback

The census distinguishes a nonroot `M=1` kill from a root-only assertion.
The decisive rule is:

> **Safe:** if the calculation produces `M=1` first at a pole entry or any
> other nonroot down vertex, apply corrected Proposition 8.4 there.  One may
> then descend in the proof.  
> **Unsafe:** if the only `M=1` datum is at `(0,y)`, there is no way to ascend
> to a nonroot `M=1`; no Proposition 8.4 contradiction is available.

### 13.1 Safe, load-bearing uses

- `ladder/REDUCTION.md` T8/T9 and the prime-`d` single-pole kill use
  Proposition 8.4 at the pole entry.  Pole vertices are nonroot by
  Proposition 5.3(i).  **No rollback.**
- `ladder/SHEET6-TDUNIFORM.md` and its entry-pin uses set
  `M_F=gcd(b\alpha,b\beta)=b` at a pole.  Every `b=1` kill is nonroot.
  **No rollback.**
- `ladder/SHEET6-AF3.md` entry-row kills, and the corresponding
  `SHEET6-CAMPAIGN.md`/`SHEET6-III.md` nonroot-child pruning, remain valid.
- `ladder/SHEET6-L1.md`, `SHEET6-2POLE.md`, and
  `SHEET6-MULTIPOLE.md` uses that kill `M=1` at a nonroot interior merge or
  nonroot suffix vertex remain valid, assuming their separately promoted
  multi-pole regularity hypotheses.
- `ladder/SHEET6-LROOT.md` and `SHEET6-LT-REVIEW.md` use the rootward descent
  of pole chains, not `M_{(0,y)}\ne1`.  That descent survives independently.
- `papers/paper2/main.tex` imports Statement 8.4's edge divisibility and the
  repaired tower transport, but not Proposition 8.4.  Its `mult(p,c)|M_G`
  consumer remains inside the safe Statement 8.4 trust set.
- `ladder/BOOK-OFFAXIS.md`, `BOOK-TD12.md`, `TOWER-25-35.md`,
  `TOWER-ROLLOUT.md`, and `TOWER-UNIFORM.md` consume Statement 8.4 for
  arrival/freeze divisibility.  **No root rollback.**

### 13.2 Root clauses that must be removed or weakened

- `ladder/SHEET6-AF3.md` lines 135--138: the claim that Proposition 8.4
  forbids `M_{(0,y)}=1` and therefore forces the displayed terminal menus is
  unsupported.  Keep `M_{(0,y)}|M_G` from Statement 8.5; allow `1` in the
  terminal menu.  The surrounding text says this was only a satisfiability
  check, so its four survivor verdicts are not killed; their constraint set
  is broadened.
- `ladder/SHEET6-TDU-REVIEW.md` line 190: the assertion that Statement 8.5
  plus Proposition 8.4 forces `M_{(0,y)}=3` is unsupported.  It is again a
  satisfiability remark, not the prime-entry kill.
- `ladder/SHEET6-CAMPAIGN.md` line 44 (“`M_F\ne1` for every `F` in the
  tree”) must say “for every nonroot down vertex.”  Any engine/pruning rule
  that kills a chain solely because its **terminal root** has `M=1` must be
  disabled.  Its pole-entry kills remain valid.
- `ladder/SHEET6-A3L1-REVIEW.md` lines 112--115 and 295--299 correctly
  noticed the root issue but classified it as a harmless down-typing nit.
  Theorem 6.1 actually supplies root down-typing; the real defect is the
  undefined `H=F_{-1}` endpoint.  Upgrade this from cosmetic nit to proof
  gap, while retaining the review's observation that no recorded verdict
  used the terminal constraint.
- `ladder/SHEET6-A2P-REVIEW.md` Front 5's “CONFIRMED line by line” needs the
  explicit qualification `F\ne(0,y)`.  Its merge conclusions based on a
  nonroot starting `M=1` remain intact.
- `ladder/SHEET6-H3.md`, `SHEET6-HIII-REVIEW.md`, and
  `SHEET6-REVIEW.md` treat root `M\ne1` as a satisfiable background
  constraint/free terminal choice.  Remove that constraint.  Their negative
  conclusion (“no additional root kill located”) becomes stronger, not
  weaker.
- `ladder/SHEET6-TEMPLATE.md` already says `M_R=1` needs re-examination and
  no printed statement decides it.  That is the correct posture.

### 13.3 Multi-pole suffix statements

- `ladder/SHEET6-MULTIPOLE.md` MP2 currently says that when the global meet
  `G^*` is nonroot, `M_F\ne1` for every suffix vertex `F\le G^*`.  Since that
  set includes `(0,y)`, MP2 must explicitly exclude the root.  The proof D3
  works for every nonroot suffix vertex: start there, descend to the last
  nonroot `H`, and run the axis contradiction.  It does not work when the
  starting `F` itself is the root.
- The same qualification applies to `SHEET6-2POLE.md` phrases saying an
  `M=1` node is killable “at/below the merge.”  Read this as every nonroot
  node at/below the merge.  Its separate root-merge analysis (case-IV
  handshake/window/log obstruction) does not rely on root Proposition 8.4
  and is unaffected.
- `SHEET6-MP-REVIEW.md` should inherit the same endpoint qualification.
  `BOOK-ENUM.md`/`BOOK-OFFAXIS.md` kill root cells by the separate `w<1`
  handshake, not by root Proposition 8.4; those root verdicts are unaffected.

No canonical edit is made in this producer report.

## 14. Terminal verdict table

| Item | Printed status | Repaired status | Root-sensitive? |
|---|---|---|---|
| Notation 8.1 | domain too broad | tower-domain definition | typing only |
| Statement 8.1 | Bezout | valid after domain repair | no |
| Proposition 8.1 | negative exponents and premature polynomial claims | valid by UFD valuations + (L6-root) | applies at root, but does not kill `M=1` |
| Statement 8.2 | includes root illegally | valid only for nonroot vertices | **yes** |
| Statement 8.3 | reversed ratios / hidden comparability | valid after repair | transport to root is valid when an upper edge exists |
| Statement 8.4 | missing terminal factor / negative exponents | valid by direct power/gcd proof | no |
| Statement 8.5 | reversed ratios / wrong terminal subscript | valid after repair | only gives lower `M` divides upper `M` |
| Proposition 8.2 + Corollary 8.1 | omitted `h_0`, rational product called polynomial | valid after valuation repair | explicitly nonroot |
| Proposition 8.3 | impossible hypothesis, undefined exponent | valid under unique-child (Reg); quarantine (ii) if desired | (iii) handles the final edge |
| Proposition 8.4 | claims all down vertices | valid for nonroot down vertices; root clause unproved | **critical rollback** |

## 15. Promotion recommendation

Promote only the following sharply separated claims after review:

1. the repaired Corollary 6.1 local order lemma (L6-root) and nonroot degree
   corollary;
2. Proposition 8.1 with explicit UFD/valuation polynomiality;
3. the adjacent tower-transport lemma;
4. Statement 8.4 in the direct gcd form;
5. corrected Proposition 8.3(i),(iii) under (Reg);
6. corrected **nonroot** Proposition 8.4.

Quarantine:

- Statement 8.2 at the root;
- Proposition 8.3(ii) unless its exponent is renamed `r=deg p_G/nu_G`;
- every use of `M_{(0,y)}\ne1`;
- any blanket suffix theorem whose quantified set still includes `(0,y)`.

The root question should be opened as a separate producer: prove or refute,
using the actual polynomial approximate-root tower and global Jacobian
constraints, that singleton pole plus `M_{(0,y)}=1` is impossible.  Nothing
in the repaired pp. 39--45 package currently supplies that theorem.
