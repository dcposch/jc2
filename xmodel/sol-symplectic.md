# Global symplectic primitives and action residues at infinity

**Date:** 2026-08-23  
**Avenue:** APPROACHES.md shortlist 1, row 33  
**Verdict:** **HOLLOW as a new global/landing obstruction.** There is an exact
and useful necessary condition—the placewise no-log residue, already banked as
PIN42—but the canonical polar residues of the global action form vanish for
every Keller pair, including a hypothetical counterexample. The residue-A lead
passes them. The only nontrivial boundary-twisted residue found is exactly the
existing vertex-gap functional \(R_{k,d_2}\), not an independent obstruction.
The avenue does not repair the universal book-landing gap G2.

All assertions below marked **EXACT** are proved algebraically in the text and
checked by the SymPy 1.14.0 transcript in Section 7. Statements not proved are
explicitly labelled **CONJECTURE**. No global three-sheet Keller map is claimed:
Section 4 uses the unique \(\Lambda=3\) *local pole datum* as a negative control,
precisely because Orevkov excludes its global realization.

---

## 1. The exact object

Work over a characteristic-zero field \(K\). Let

\[
 F=(P,Q):\mathbb A^2_{x,y}\longrightarrow\mathbb A^2,
 \qquad [P,Q]=P_xQ_y-P_yQ_x=c\in K^*.
\]

With \(\omega=dx\wedge dy=d(x\,dy)=-d(y\,dx)\), dimension two gives

\[
 F^*\omega=dP\wedge dQ=c\,dx\wedge dy.
\]

Thus \(F\) is conformally symplectic (symplectic after scaling one target
coordinate). Choose the Liouville primitive \(\lambda=x\,dy\). The two polynomial
**action forms** are

\[
 \alpha_P:=P\,dQ-cx\,dy,
 \qquad
 \alpha_Q:=Q\,dP-cy\,dx.                                      \tag{1.1}
\]

They are closed:

\[
 d\alpha_P=dP\wedge dQ-c\,dx\wedge dy=0,
 \qquad
 d\alpha_Q=dQ\wedge dP-c\,dy\wedge dx=0.                    \tag{1.2}
\]

Polynomial Poincare exactness on \(\mathbb A^2\) gives **polynomial** action
primitives \(S_P,S_Q\in K[x,y]\), unique up to constants:

\[
 \alpha_P=dS_P,\qquad \alpha_Q=dS_Q.                         \tag{1.3}
\]

No analytic or invertibility hypothesis enters. One may prove (1.3) directly:
integrate the \(dx\)-coefficient of a closed polynomial one-form term by term;
closedness makes the difference a polynomial in \(y\) alone, which can also be
integrated in characteristic zero. The two choices obey

\[
 S_P+S_Q=PQ-cxy+\text{constant},                             \tag{1.4}
\]

because \(\alpha_P+\alpha_Q=d(PQ-cxy)\). Equivalently, the symmetric action
form

\[
 \tfrac12(P\,dQ-Q\,dP)-\tfrac c2(x\,dy-y\,dx)
   =\tfrac12d(S_P-S_Q)
\]

is exact. Changing the Liouville primitive changes the action only by an exact
polynomial differential, so none of the residue conclusions below changes.

### 1.1 Why this is genuinely dimension-two-specific

For a map of a two-dimensional affine space, the symplectic form is already a
top form, so the determinant identity is exactly the symplectic identity. In
dimension \(n\ge3\), \(\det JF=c\) controls an \(n\)-form; it does not imply
preservation of a two-form and therefore does not produce (1.1). This is real
two-dimensional structure. The experiment below shows that it is nevertheless
too weak: every putative plane counterexample has it automatically.

### 1.2 Poles in the standard compactification

Embed \(\mathbb A^2\subset\mathbb P^2\), with \(L_\infty=\{Z=0\}\). If
\(\deg S_P=d\), then on the \(X\ne0\) chart

\[
 u=Z/X=1/x,\qquad v=Y/X=y/x,
\]

one has

\[
 S_P=u^{-d}\bigl(S_{P,d}(1,v)+uS_{P,d-1}(1,v)+\cdots\bigr). \tag{1.5}
\]

At a generic point of \(L_\infty\), \(S_P\) has pole order \(d\), the normal
component of \(dS_P\) has pole order \(d+1\), and the tangential component has
order at most \(d\). At a zero of the leading homogeneous form these orders can
drop. After any resolution \(\pi:X\to\mathbb P^2\), the pole order along a
boundary component \(E\) is simply the divisorial valuation of the rational
function \(\pi^*S_P\). There is no a priori forbidden order: it is the pole
divisor of a polynomial.

The canonical divisorial residue is fatal to the proposed obstruction. In a
local parameter \(t\) at \(E\), write

\[
 \pi^*S_P=\sum_{m\ge-N}a_m t^m.
\]

The \(dt/t\)-coefficient of \(d(\pi^*S_P)\) is zero, since it could only come
from \(m=0\), whose derivative coefficient is \(m a_m=0\). Hence:

> **EXACT LEMMA 1 (global action residues vanish).** For every prime boundary
> divisor \(E\) on every resolution,
> \[
> \operatorname{Res}_E(\pi^*\alpha_P)
> =\operatorname{Res}_E(\pi^*\alpha_Q)=0.                   \tag{1.6}
> \]
> Every action period also vanishes, because the action is the differential of
> a single-valued rational function.

A higher polar coefficient of \(dS_P\) is not a residue. It changes with the
choice of local parameter/trivialization. Pole order is intrinsic, but there is
no general vanishing law for it.

### 1.3 The nontrivial placewise functional

There is a different, useful residue. Let \(\widetilde C_a\) be the normalization
of the compactified fibre \(P=a\), and \(p\in\widetilde C_a\setminus C_a\) an
infinity place. Pulling back \(\alpha_Q=dS_Q\) to \(P=a\) kills \(dP\):

\[
 -c\,y\,dx=d(S_Q|_{\widetilde C_a}).
\]

Likewise, on a fibre \(Q=b\), \(-c\,x\,dy=d(S_P|_{\widetilde C_b})\). Therefore

\[
 \mathcal R^P_p:=\operatorname{Res}_p(y\,dx)=0,
 \qquad
 \mathcal R^Q_p:=\operatorname{Res}_p(x\,dy)=0.             \tag{1.7}
\]

These are separate equations at every place, stronger than merely saying that
their sum is zero. In the normalized Puiseux chart

\[
 x=t^{-\kappa},\qquad y=\sum_m c_m t^m,
\]

they become the coefficient selector

\[
 \operatorname{Res}_t(y\,dx)=-\kappa c_\kappa,
 \qquad
 \operatorname{Res}_t(x\,dy)=+\kappa c_\kappa.             \tag{1.8}
\]

Thus exactness forces \(c_\kappa=0\). This is exactly the level-\(\kappa\)
no-log lemma already derived and consumed in SHEET6-DIRECTIONB.md Section 7.
For residue A, \(\kappa=42\): nine placewise coefficients vanish, of which the
six live emitted variables are

\[
 tf1_{42},tf2_{42},tg1_{42},tg2_{42},tg01_{42},tg02_{42}.
\]

So (1.7) is a valid necessary condition, but it is not new to the current
repository state and it did not empty the residue-A window.

---

## 2. Positive controls: elementary and tame automorphisms

Normalize \(c=1\).

### 2.1 One elementary automorphism

For

\[
 (P,Q)=(x,y+x^n),
\]

direct calculation gives

\[
 \begin{aligned}
 P\,dQ-x\,dy&=n x^n\,dx
   =d\!\left(\frac n{n+1}x^{n+1}\right),\\
 Q\,dP-y\,dx&=x^n\,dx
   =d\!\left(\frac1{n+1}x^{n+1}\right).
 \end{aligned}                                             \tag{2.1}
\]

In the \(X\ne0\) infinity chart, the first primitive is
\(\frac n{n+1}u^{-(n+1)}\), and its action form is
\(-n u^{-(n+2)}du\). It has a high-order pole but zero residue. The exact
SymPy control used \(n=4\): primitive pole order \(5\), action-form normal
pole order \(6\), residue \(0\).

### 2.2 A tame product with elementary degrees \(3,4\)

Let

\[
 V_3(x,y)=(x,y+x^3),\qquad H_4(x,y)=(x+y^4,y),
\]

and put \(F=H_4\circ V_3\). With \(R=y+x^3\),

\[
 P=x+R^4,\qquad Q=R,\qquad [P,Q]=1.                         \tag{2.2}
\]

Both primitives are explicit:

\[
 S_P=\frac34x^4+\frac15R^5,
 \qquad
 S_Q=\frac14x^4+\frac45R^5.                               \tag{2.3}
\]

Indeed \(dS_P=P\,dQ-x\,dy\), \(dS_Q=Q\,dP-y\,dx\), and
\(S_P+S_Q=PQ-xy=x^4+R^5\). At infinity,

\[
 S_P=\frac{3}{4u^4}+\frac{(1+u^2v)^5}{5u^{15}},
 \qquad \lim_{u\to0}u^{15}S_P=\frac15.                   \tag{2.4}
\]

Thus the primitive has generic pole order \(15\), \(dS_P\) has normal pole
order \(16\), and its divisorial residue is still \(0\). Large action poles are
therefore legal even for tame maps; pole order alone cannot distinguish tame
from counterexample data.

---

## 3. Residue-A leading pair without tails

Use exactly the merge chart of SHEET6-DIRECTIONB.md Section 0, with the
registered gauge \(\sigma=6\):

\[
 x=t^{-42},\qquad y=t^{12}+\eta t^{32},
\]

where setting the registered \(t^{18},t^{24},t^{30}\) prefix freedoms and all
later tails to zero is the requested zero-tail test. Set

\[
 r(\eta)=(\eta^3-(3+\sqrt3))(\eta^3-(3-\sqrt3))
         =\eta^6-6\eta^3+6,
\]

\[
 S_M=\frac{7^{12}}{2^6},\qquad G_M=-\frac{7^{18}}{2^9},
 \qquad C=S_MG_M,
\]

and take the leading pair

\[
 f_0=S_Mt^{-12}r^2,\qquad g_0=G_Mt^{-18}r^3.               \tag{3.1}
\]

The exact wedge calculation is

\[
 dx\wedge dy=-42t^{-11}dt\wedge d\eta,
 \qquad df_0\wedge dg_0=0.                                \tag{3.2}
\]

The second equality is the familiar \(2{:}3\) leading cancellation: both
coordinates are powers of the same \(r\), with matching \(t\)-weights. Moreover

\[
 f_0\,dg_0=d\!\left(\frac35Ct^{-30}r^5\right).             \tag{3.3}
\]

For the truncated action
\(\alpha_0=f_0\,dg_0-x\,dy=A_tdt+A_\eta d\eta\),

\[
 \begin{aligned}
 A_t&=-18Cr^5t^{-31}-12t^{-31}-32\eta t^{-11},\\
 A_\eta&=3Cr^4r't^{-30}-t^{-10},\\
 d\alpha_0&=42t^{-11}dt\wedge d\eta.                     \tag{3.4}
 \end{aligned}
\]

This has three consequences.

1. The zero-tail leading pair has no action primitive, because it is not itself
   Keller. This is not a new contradiction: \(42t^{-11}\) is exactly the
   inhomogeneous slot-20 Jacobian defect. SHEET6-DIRECTIONB.md already proves
   that nonzero tails must cancel it and that the zero-extension locus is dead.
2. Nevertheless its divisorial \(dt/t\) coefficient is \(0\), and on every
   constant-\(\eta\) root of \(r\) the fibre-action residues
   \(\operatorname{Res}(-y\,dx)\) and \(\operatorname{Res}(-x\,dy)\) are both
   \(0\). Thus the proposed leading polar-residue test does **not** kill the
   residue-A lead.
3. Adding a level-42 coefficient \(c_{42}t^{42}\) to \(y\) gives exactly

   \[
   \operatorname{Res}_t(y\,dx)=-42c_{42},\qquad
   \operatorname{Res}_t(x\,dy)=42c_{42},                  \tag{3.5}
   \]

   reproducing PIN42 and nothing stronger.

The primitive polar divisor is therefore not “illegal for the \((2,3)\)
genome.” Before completion there is no primitive because Row 20 is missing;
after any Keller completion, a polynomial primitive exists automatically and
all of its canonical residues vanish automatically.

---

## 4. Orevkov-excluded three-sheet negative control

Orevkov's Theorem 1.1 states that a two- or three-sheeted polynomial map
\(\mathbb C^2\to\mathbb C^2\) cannot have nonzero constant Jacobian. To ask
whether action residues can see that theorem, use the unique \(\Lambda=3\)
row-1 pole datum from Sigray's table, recorded in SHEET6-L1.md:

\[
 (D_F,D_g;\deg p,\deg p_g;\nu,M,\bar\kappa)
 =(2,3;2,3;2,1,5).                                       \tag{4.1}
\]

Taking the same \(\kappa=42\) ramification as residue A makes
\(\pi=37/42\) and realizes \(\bar\kappa=42(1-\pi)=5\). Put

\[
 x=t^{-42},\qquad y=\eta t^{37},
\]

\[
 p=\eta^2-1,\qquad
 q=14\eta\left(\eta^2-\frac32\right),
\]

\[
 f=t^{-2}p,\qquad g=t^{-3}q.                              \tag{4.2}
\]

The pole ODE and both area forms agree exactly:

\[
 2pq'-3p'q=42,
 \qquad
 dx\wedge dy=df\wedge dg=-42t^{-6}dt\wedge d\eta.        \tag{4.3}
\]

Even more strongly, this excluded-degree local datum has an explicit action
primitive:

\[
 f\,dg-x\,dy
 =d\!\left[
 t^{-5}\frac{\eta(42\eta^4-105\eta^2+100)}5
 \right].                                                \tag{4.4}
\]

Its action residue and its two fibre-action residues are all zero. If this were
the sole pole of a global map, its \(\Lambda=3\) would give topological degree
three, which Orevkov excludes. The calculation does **not** construct such a
map; it proves that the action-residue test cannot detect the global obstruction.

This is the decisive negative control. It is also structurally unsurprising:
each residue-A pole \(P_i\) carries this same row-1 \(\Lambda=3\) pattern, and
residue A gets \(td=3+3=6\) by using two of them. A placewise action residue
cannot tell whether the global boundary contains one copy or two.

---

## 5. Relation to the vertex-gap residue

The action residue (1.6) is **not** the paper's nontrivial
\(R_{k,d_2}\). The repository has already isolated the distinction in
RESIDUE.md and cases/residue_check.py.

For the strip equation \([P,Q]=x^k\), the analogous action form

\[
 P\,dQ-\frac{x^{k+1}}{k+1}\,dy                            \tag{5.1}
\]

is again closed and polynomial-exact. On the binomial strip locus
\(A=1+a_2y\), however, solving the *support-restricted column ODE* produces

\[
 \operatorname{Res}_{y=-1/a_2}
 \frac{2BC'-kB'C}{A^{k+2}}\,dy
 =(k+2)(-1)^k a_2^{-2d_2-1}R_{k,d_2}.                    \tag{5.2}
\]

That is a residue of a boundary-twisted reconstruction integrand. Equivalently,
it is an iterated residue of \(dP\wedge dQ\) only after inserting the toric
boundary factors \(x^{k+2}A^{k+2}\). The twist contains exactly the strip,
gap, and chosen-boundary information. Without it, the natural candidate is
exact:

\[
 \frac{dP\wedge dQ}{P^{k+2}}
 =d\!\left(-\frac{P^{-(k+1)}}{k+1}\,dQ\right),            \tag{5.3}
\]

so its total iterated residue is identically zero.

At the vertex-gap cell \((k,d_2)=(2,2)\), write

\[
 A=1+ay,\quad C=y+\frac a2y^2,\quad
 B=b_2y^2+b_3y^3+b_4y^4.
\]

SymPy gives

\[
 \operatorname{Res}_{y=-1/a}
 \frac{2BC'-2B'C}{A^4}\,dy=\frac{4b_4}{a^5},             \tag{5.4}
\]

and \(R_{2,2}=b_4\). The repository's exact Fraction engine was also rerun:
python3 cases/residue_check.py ended ALL OK on its 11 cells, including
the exactness control (5.3).

Hence the comparison is precise:

- The global action residue is identically zero for every Keller pair.
- The placewise fibre residue is the already-banked level-\(\kappa\) no-log pin.
- In the strip block, the nonzero boundary-twisted reconstruction residue is
  exactly the existing vertex-gap functional \(R_{k,d_2}\).
- Residue A is not killed by either canonical action residue; its zero-tail
  failure is exactly the already-known slot-20 Jacobian defect.

The two residue packages share a “no logarithm when integrating a Jacobian
equation” philosophy, but they are not independent constraints. Recovering
\(R_{k,d_2}\) requires reintroducing the Newton/toric boundary data that the
putatively global action route was meant to transcend.

---

## 6. Does this attack the landing gap G2?

No.

The action primitive is universal in the wrong sense: it exists for every
Keller pair before any infinity tree or book is chosen. Its canonical residues
therefore cannot select a finite entry, bound topological degree, type all
downstream branches, or prove that an arbitrary counterexample lands in an
enumerated configuration. The tame and \(\Lambda=3\) controls show that even the
primitive's pole order and complete residue vector do not encode sheet number.

A mixed-coordinate generating function does not repair this. The polynomial
\(S_P(x,y)\) from (1.3) is not automatically a polynomial function of
\((x,Q)\). Passing to \(S(x,Q)\) requires the projection
\((x,y)\mapsto(x,Q)\) to be globally invertible, which is already a substantial
coordinate/injectivity assertion.

> **CONJECTURE (only possible surviving refinement; not established).** On a
> completely specified resolved boundary, the *full principal parts* of all
> local action primitives might obey a nontrivial Cousin/Mittag-Leffler gluing
> condition not implied by the filed local Jacobian rows.

The experiment supplies no positive evidence for this conjecture. A version
using only pole orders or residues is refuted by Sections 2 and 4. A version
using full principal parts requires all boundary components, intersection
charts, and tail coefficients—the compactification/algebraization problem
again—and still would not by itself supply a typed terminating map into the
current books. It should not be advertised as a G2 repair.

### Final classification

| Candidate output of row 33 | Result |
|---|---|
| Polynomial global action primitive | **EXACT**, but automatic for every Keller pair |
| Divisorial action residues on any resolution | **EXACTLY ZERO**, hence hollow |
| Action periods | **EXACTLY ZERO**, hence hollow |
| Per-fibre residues \(\operatorname{Res}(y\,dx),\operatorname{Res}(x\,dy)\) | **EXACT necessary condition**, already PIN42; no residue-A kill |
| Polar order of the primitive | Legal and arbitrarily large on tame maps |
| Residue-A zero-tail failure | Exactly Row 20 / \(J=1\), not a new obstruction |
| Boundary-twisted strip residue | Exactly \(R_{k,d_2}\), the vertex-gap theorem |
| Three-sheet discrimination | Fails on the exact local \(\Lambda=3\) control |
| Universal book landing / G2 | No progress |

**Operational verdict:** retain the level-\(\kappa\) no-log equations as cheap,
depth-independent necessary rows. Do not spend a new campaign on untwisted
global action residues or primitive pole orders. Any future residue work should
be honestly filed as a boundary-twisted Newton/adjoint extension of
\(R_{k,d_2}\), not as a new global symplectic lane.

---

## 7. Exact SymPy reproduction

The default repository python3 did not contain SymPy. The run used the
ephemeral command

~~~bash
UV_CACHE_DIR=/tmp/jc72108-uv-cache PYTHONDONTWRITEBYTECODE=1 \
  uv run --no-project --with sympy python3 - <<'PY'
~~~

with the following body. All arithmetic is symbolic over \(\mathbb Q\); no
floating-point values occur.

~~~python
import sympy as s
x,y,u,v,t,e,c,a,b2,b3,b4 = s.symbols(
    'x y u v t eta c42 a b2 b3 b4')

def W(F,G,z,w):
    return s.factor(s.diff(F,z)*s.diff(G,w)-s.diff(F,w)*s.diff(G,z))
def act(F,G,X,Y,z,w):
    return (s.factor(F*s.diff(G,z)-X*s.diff(Y,z)),
            s.factor(F*s.diff(G,w)-X*s.diff(Y,w)))
def curl(A,B,z,w):
    return s.factor(s.diff(B,z)-s.diff(A,w))
def gradcheck(A,B,S,z,w):
    return (s.factor(A-s.diff(S,z)), s.factor(B-s.diff(S,w)))

# Elementary automorphism.
P=x; Q=y+x**4
T=s.Rational(4,5)*x**5; U=s.Rational(1,5)*x**5
A,B=act(P,Q,x,y,x,y); A2,B2=act(Q,P,y,x,x,y)
assert W(P,Q,x,y)==1 and gradcheck(A,B,T,x,y)==(0,0)
assert gradcheck(A2,B2,U,x,y)==(0,0)
Pc=P.subs({x:1/u,y:v/u}); Qc=Q.subs({x:1/u,y:v/u})
Au,_=act(Pc,Qc,1/u,v/u,u,v)
assert s.residue(Au,u,0)==0

# Alternating tame product of elementary degrees 3 and 4.
R=y+x**3; P=x+R**4; Q=R
T=s.Rational(3,4)*x**4+s.Rational(1,5)*R**5
U=s.Rational(1,4)*x**4+s.Rational(4,5)*R**5
A,B=act(P,Q,x,y,x,y); A2,B2=act(Q,P,y,x,x,y)
assert W(P,Q,x,y)==1 and gradcheck(A,B,T,x,y)==(0,0)
assert gradcheck(A2,B2,U,x,y)==(0,0)
Pc=P.subs({x:1/u,y:v/u}); Qc=Q.subs({x:1/u,y:v/u})
Au,_=act(Pc,Qc,1/u,v/u,u,v)
assert s.residue(Au,u,0)==0
assert s.limit(u**15*T.subs({x:1/u,y:v/u}),u,0)==s.Rational(1,5)

# Residue-A zero-tail merge lead.
r=e**6-6*e**3+6
SM=s.Rational(7**12,2**6); GM=-s.Rational(7**18,2**9); K=SM*GM
X=t**-42; Y=t**12+e*t**32
F=SM*t**-12*r**2; G=GM*t**-18*r**3
A,B=act(F,G,X,Y,t,e)
assert W(X,Y,t,e)==-42*t**-11 and W(F,G,t,e)==0
assert curl(A,B,t,e)==42*t**-11 and s.residue(A,t,0)==0
Sfg=s.Rational(3,5)*K*t**-30*r**5
assert gradcheck(F*s.diff(G,t),F*s.diff(G,e),Sfg,t,e)==(0,0)
assert s.residue(-Y*s.diff(X,t),t,0)==0
assert s.residue(-X*s.diff(Y,t),t,0)==0
Y42=Y+c*t**42
assert s.residue(Y42*s.diff(X,t),t,0)==-42*c
assert s.residue(X*s.diff(Y42,t),t,0)==42*c

# Unique Lambda=3 row-1 pole datum: Orevkov-excluded global degree control.
p=e**2-1; q=14*e*(e**2-s.Rational(3,2))
X=t**-42; Y=e*t**37; F=t**-2*p; G=t**-3*q
A,B=act(F,G,X,Y,t,e)
H=e*(42*e**4-105*e**2+100)/5
assert s.factor(2*p*s.diff(q,e)-3*s.diff(p,e)*q)==42
assert W(X,Y,t,e)==W(F,G,t,e)==-42*t**-6
assert gradcheck(A,B,t**-5*H,t,e)==(0,0)
assert s.residue(A,t,0)==0 and curl(A,B,t,e)==0

# Vertex-gap (2,2): the twisted residue is exactly R_22=b4.
A0=1+a*y; C=(A0**2-1)/(2*a)
B0=b2*y**2+b3*y**3+b4*y**4
G0=s.expand(2*B0*s.diff(C,y)-2*s.diff(B0,y)*C)
rvg=s.factor(s.residue(G0/A0**4,y,-1/a))
assert s.factor(rvg-4*b4/a**5)==0

print('SymPy',s.__version__)
print('elementary: J=1, poles(T,dT)=(5,6), Res=0')
print('tame(3,4): J=1, pole(T)=15, Res=0')
print('residue-A zero-tail: wedges=(-42/t^11,0), d(alpha)=42/t^11, Res=0')
print('PIN42 selector:',-42*c,42*c)
print('td=3 row control: both wedges=-42/t^6, T=t^-5*',H,', Res=0')
print('vertex-gap (2,2): residue=',rvg)
~~~

Executed output:

~~~text
SymPy 1.14.0
elementary: J=1, poles(T,dT)=(5,6), Res=0
tame(3,4): J=1, pole(T)=15, Res=0
residue-A zero-tail: wedges=(-42/t^11,0), d(alpha)=42/t^11, Res=0
PIN42 selector: -42*c42 42*c42
td=3 row control: both wedges=-42/t^6, T=t^-5* eta*(42*eta**4 - 105*eta**2 + 100)/5 , Res=0
vertex-gap (2,2): residue= 4*b4/a**5
~~~

---

## 8. Provenance and literature anchors

- APPROACHES.md row 33 and Section 4 give the experiment specification.
- SHEET6-DIRECTIONB.md Sections 0 and 7 give the residue-A merge chart,
  slot-20 identity, and already-promoted level-42 action residues.
- SHEET6-TEMPLATE.md Sections 1a–1b give the \((2,3)\) genome, scales, and
  pole patterns.
- SHEET6-L1.md records the unique \(\Lambda=3\) row-1 datum
  \((D,D_g)=(2,3)\), pattern degrees \((2,3)\), \(\nu=2\), \(M=1\).
- RESIDUE.md, cases/residue_check.py, and paper1/main.tex Section 6
  identify the boundary-twisted residue with \(R_{k,d_2}\) and prove the
  pure-\(P,Q\) exactness control.
- S. Yu. Orevkov, *On three-sheeted polynomial mappings of
  \(\mathbb C^2\)*, Math. USSR-Izv. 29 (1987), 587–596,
  DOI 10.1070/IM1987v029n03ABEH000984; local source refs/jc86.pdf,
  Theorem 1.1.
