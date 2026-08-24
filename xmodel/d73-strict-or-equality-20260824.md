# D73-STRICT-OR-EQUALITY — local direction-collision gate

Date: 2026-08-24  
Scope: the LR2 x-side critical-value vertex only; no D-series, new book
cell, coefficient search, or global landing claim.  Primary source:
`refs/sigray_full.pdf`, SHA-256
`9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae`.

## Verdict

**EQUALITY-CONTROL.**  The proposed strict upgrade

\[
  \operatorname{mult}(p_G-a_*,c)\geq2,\quad \kappa_G=1
  \quad\Longrightarrow\quad
  \sum_{P\in R^*_{a_*}}\Lambda(P)\geq \pi(G)
\]

is false in the local analytic/Puiseux category used by Proposition 7.3.
There is an exact Jacobian-one germ matching the sharp SP-2 x-side data

\[
 (k_f,l_f)=(60,15),\qquad (k_g,l_g)=(100,25),\qquad
 \pi(G)=4,\qquad \kappa_G=1,
\]

with a direction of multiplicity \(15\), but

\[
  \sum_{P\in R^*_0}\Lambda(P)=3=\pi(G)-1.
\]

Thus direction multiplicity alone does not buy an extra delta unit.  This
does **not** construct a global polynomial Keller pair: the remaining possible
obstruction is precisely globalization/polynomial realizability together with
the pinned opposite-side data.  It closes only the named *local* strictness
gate.

## 1. Source and hypothesis map

The source notation is \(F\); below \(F=G\), the campaign's LR2 vertex.

| Required datum | Exact source / campaign location | Control below |
|---|---|---|
| \(G\in T_{a,cv}\), hence \(d_{f-a,G}=d_{g,G}=0\) and \(\pi(G)>1\) | Sigray, Notation 7.1 and Statement 7.1, printed p. 35 | \(d_{f,G}=d_{g,G}=0\), \(\pi(G)=4\) |
| Proposition 7.3 direction \(c\), set \(R^*_{a_*}\), and lower bound \(\sum\Lambda\geq\kappa_G(\pi(G)-1)\) | Sigray, Proposition 7.3, statement printed pp. 36--37 and geometric proof pp. 37--38 | \(a_*=c=0\); all three normalized ends are in \(R^*_0\) |
| Equality is asserted by the source only when the direction is simple | Sigray, Proposition 7.3, printed p. 37; correctly summarized in `ladder/SHEET6-LT-REVIEW.md:90-95` | the control shows the converse fails locally |
| LR2: one x-cluster, \(\kappa_G=1\), no characteristic exponent below \(\pi(G)\); at slack zero \(\pi(G)=R\) | `ladder/SHEET6-LROOT.md:136-153` | three ends stay together through height \(4\), first separating at \(21/5\) |
| Sharp SP-2 numerical row | `ladder/SHEET6-LROOT.md:184-195` | exactly \(l_f=15,l_g=25,R=4\), and x-mass \(3\) |
| Collision is a genuine, nonvacuous LR2 question | `ladder/SHEET6-LT-REVIEW.md:102-110` | \(\deg p_G=15\) and \(p_G=t^{15}\) has the critical value \(0\) |
| Global sheet arguments remain book-relative and owe landing/compatibility where invoked | `AUDIT.md:947-961`, `AUDIT.md:1430-1440`, and `APPROACHES.md:76-79` | no global or JC2 inference is made |

One wording correction follows immediately.  The sentence at
`ladder/SHEET6-LROOT.md:254-255` says equality holds "iff mult = 1".  The
primary source says only **if** the multiplicity is one; the reviewed wording
at `ladder/SHEET6-LT-REVIEW.md:90-94` is accurate.  The present control makes
the stronger "only if" false locally.

## 2. Exact Jacobian-one germ

Work in the x-side chart near \(y=\infty\), with

\[
  s=y^{-1},\qquad t=xy^4,qquad x=t s^4,qquad y=s^{-1}.
\]

Then

\[
  dx\wedge dy=s^2\,ds\wedge dt.
\]

Put

\[
 q(t)=t+t^{25},\qquad q'(t)=1+25t^{24},
\]
and, on a sufficiently small bidisc around \((s,t)=(0,0)\), define

\[
  g=q(t),\qquad
  f=t^{15}+\frac{s^3}{3q'(t)}.
  \tag{1}
\]

The denominator is a holomorphic unit there.  Directly,

\[
  df\wedge dg
   =\frac{s^2}{q'(t)}ds\wedge q'(t)dt
   =s^2ds\wedge dt
   =dx\wedge dy.
\]

Hence \(J_{x,y}(f,g)=1\) exactly, not merely to leading order.  At height
\(G=I_P(4)\), the Eggers variable is

\[
  \eta_G=y^4x=t.
\]

Equation (1) therefore gives

\[
 d_{f,G}=d_{g,G}=0,\qquad
 p_G(t)=t^{15},\qquad p_{g,G}(t)=t+t^{25}.
\]

In particular

\[
  \deg p_G=15=l_f,\quad \deg p_{g,G}=25=l_g,
  \quad \operatorname{mult}(p_G-0,0)=15.
\]

The dominant monomials below the critical height have the sharp SP-2
slopes \(k_f/l_f=60/15=4\) and \(k_g/l_g=100/25=4\).  More importantly for
the local gate, the normalized Puiseux ends computed next have no split or
characteristic exponent below \(4\).

## 3. Exact normalization and the Lambda sum

On the special fiber \(f=0\),

\[
  s^3=-3q'(t)t^{15}.
  \tag{2}
\]

Because \(q'(0)=1\), choose a holomorphic unit \(U(t)\) with
\(U(t)^3=-3q'(t)\), and set \(S=s/U(t)\).  Equation (2) becomes exactly

\[
  S^3=t^{15}.
\]

It has \(d=\gcd(3,15)=3\) normalized branches.  On each branch one may use
\(z=t\) as local parameter and write

\[
  S=\omega z^5,qquad s=U(z)\omega z^5,qquad
  \omega^3=1.
\]

Consequently

\[
  y=s^{-1}\sim C_\omega z^{-5},qquad
  x=t s^4\sim C'_\omega z^{21}
             \sim C''_\omega y^{-21/5}.
\]

Thus each end has \(y\)-pole order \(5\), its first characteristic exponent
is \(21/5>4\), and all three series have zero truncation below height \(4\).
At \(G=I_P(4)\), Sigray's definition on printed p. 12 gives

\[
  \kappa_G=\frac{5}{e_0}=\frac55=1.
\]

The three branches first separate at contact \(21/5\); hence they form the
single LR2 cluster through \(G\).  With suitable denominator \(5\), the
direction \(c=0\) gives \(G*0=I_P(4+1/5)\), and the endpoint convention
\(u\leq O(P,P')\) in Definition 3.3 (printed p. 11) puts all three normalized
points in \(R^*_0\).

Finally, on every normalized branch

\[
  g=q(z)=z(1+z^{24}),
\]

so Sigray's multiplicity \(\Lambda(P)\) (Notation 1.5, printed p. 6) equals
one.  Therefore

\[
  \sum_{P\in R^*_0}\Lambda(P)=1+1+1=3
   =\kappa_G\pi(G)-\kappa_G=4-1,
\]

while \(\operatorname{mult}(p_G,0)=15\ge2\).  This is the required equality
control.

## 4. Audit of all fifteen generic split roots

It is tempting to strengthen Proposition 7.3's one-\(Q\) argument as follows:
split the multiplicity-\(15\) root into fifteen simple roots, apply the simple
case to all of them, and add. In this control, the proposed transport,
distinctness, \(A\)-membership, and local-degree steps all hold. The addition
is the type error.

Take a sufficiently small generic \(a\ne0\). On the compactifying divisor
\(s=0\), the equation \(f=a\) has the fifteen distinct roots

\[
  t_i^{15}=a.
\]

They give fifteen distinct punctures \(Q_i\) in the same chosen local
bidisc \(A\). Since \(q'(0)=1\), after shrinking the bidisc the values

\[
  b_i=g(Q_i)=q(t_i)
\]

are also pairwise distinct. Near \(Q_i\), the implicit equation gives

\[
  t-t_i=C_i s^3+O(s^6),\qquad C_i\ne0,
\]

and hence

\[
  g-b_i=q'(t_i)(t-t_i)+O((t-t_i)^2)
       =C'_i s^3+O(s^6).
\]

Thus every one of the fifteen simple-root punctures has
\(\Lambda(Q_i)=3=\kappa_G(\pi(G)-1)\), exactly as Proposition 7.3 says.
They are distinct, they all remain in \(A\), and local tree transport does
not fail.

What fails is summing these fifteen multiplicities as though they lay over
one value of \(g\). They lie over the fifteen different values \(b_i\).
Indeed \(g:A_a\to B\) has degree exactly three: for a generic target
\(b\in B\), local invertibility of \(q\) determines one \(t=q^{-1}(b)\),
and then

\[
  s^3=3q'(t)(a-t^{15})
\]

has three solutions counted with multiplicity. At \(b=b_i\), those three
solutions coalesce into the single point \(Q_i\) of local degree three.
This can happen at each of fifteen *different* target values without raising
the degree of the cover. At \(a=0,b=0\), the three normalized special-fiber
points each have degree one, again totaling three.

Therefore the one-\(Q\) wording in the printed proof is not concealing a
missing factor of \(15\). All split roots may be followed, but their
\(\Lambda\)'s belong to different fibers of \(g\). A theorem equating their
sum with the multiplicity over the single collided value would be false for
this exact Jacobian-one germ.

## 5. Why multiplicity does not force strictness

The mechanism is stable and transparent.  For arbitrary integers
\(R\ge2\), \(L\ge2\), and any polynomial \(q\) with \(q'(0)\ne0\), set

\[
  g=q(t),\qquad
  f=t^L+\frac{s^{R-1}}{(R-1)q'(t)},qquad
  x=t s^R,\quad y=s^{-1}.
\]

Again \(J_{x,y}(f,g)=1\).  On \(f=0\), after an analytic unit change, the
normal form is

\[
  S^{R-1}=t^L.
\]

Writing \(d=\gcd(R-1,L)\), there are \(d\) normalized branches and \(g\)
has multiplicity \((R-1)/d\) on each.  Their total is always

\[
  d\frac{R-1}{d}=R-1,
\]

independent of the collision multiplicity \(L\).  The multiplicity of
\(p_G-a_*\) records tangency of the boundary value map; normalization can
absorb that tangency into fewer branches with compensating ramification.
It need not create another sheet of the \(g\)-map.

## 6. Smallest missing implication and scope boundary

The smallest implication needed for a strict kill is therefore not a local
Puiseux inequality.  One would have to prove that a **global normalized
polynomial** Keller pair with the pinned LR2 and opposite-side data cannot
realize the local unit-corrected germ (1), or else prove a global balance law
forcing an additional \(g\)-zero/branch elsewhere on the same compactified
fiber.  Neither follows from

\[
  \kappa_G=1,\quad \pi(G)=R,\quad
  \operatorname{mult}(p_G-a_*,c)\ge2,\quad
  J=1
\]

locally.  This returns the campaign to the already named
`x-side realizability vs. templates` surface
(`ladder/SHEET6-LROOT.md:260-264`); it does not alter the eight-class book,
prove a global equality case, or prove/disprove JC2.
