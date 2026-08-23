# The filtered differential Newton lemma

## Verdict

**THEOREM (proved below).** Route B works. Euler terms do not require a
nonlinear conjugation: a fixed-linearization contraction proves the required
Hensel statement over an arbitrary field, including characteristic \(p\). The
quantity that enters the sharp inequality is the loss of an exact causal right
section of the Euler/Ore linearization. If that loss is \(e\), a residual of
global \(t\)-order \(D\) lifts whenever

\[
                     \boxed{D\geq 2e+1}.                 \tag{N}
\]

The resulting root agrees with the approximate point modulo \(F^{D-e}\), not
necessarily modulo \(F^D\).

This closes **CONJECTURE E-HENSEL as an abstract theorem**. It does not, by
itself, promote any current repository value of \(e^+\). Four
repository-specific gates remain unproved:

1. **CONJECTURE CYCLIC-30:** the full, all-depth equation, including the
   \(t^{42+}\) x-side terms, has exactly the asserted 30 output streams;
2. **CONJECTURE BRIDGE-30:** those streams generate the full pristine equation
   ideal, universally and level by level, and every emitted presentation is
   connected by certified localized-unit transformations;
3. **CONJECTURE PARAM-30 at a proposed live point:** the corrected
   \(30\times30\) operator has an exact all-depth causal right section with the
   claimed loss, including every characteristic-\(p\) resonance; and
4. **CONJECTURE FILTER-30:** the universal all-depth normalization on the
   Newton ball is an integral filtered Euler-differential expression, with no
   hidden negative \(t\)-shift and with every localized denominator a unit.

The abstract quadratic-remainder theorem is proved here. `FILTER-30` is only
the repository-specific audit that its hypotheses apply to the as-yet
unbanked full x-side formula. The old \(29\times29\) index \(295\) is
irrelevant to the corrected object.

## 1. The corrected object and its filtration

Let \(k\) be any field, \(R=k[[t]]\), \(u=t^6\), and

\[
 \theta=t\frac d{dt},\qquad \Theta=u\frac d{du}.
\]

The coefficient field may be \(\mathbf F_p\), a finite extension, or its
algebraic closure. This is a \(t\)-adic lifting theorem over that same field;
it is not a lift from characteristic \(p\) to characteristic zero.

The six allowed tail families split into the following 30 \(u\)-streams:

- residues \(0,1,2,3,4,5\) for each of
  `tf1, tf2, tg1, tg2`;
- residues \(0,2,4\) for each of `tg01, tg02`.

Fix the deterministic column order by family first and then increasing
allowed residue:

\[
\begin{array}{c|c|c}
q&\text{family}&\text{residues in order}\\ \hline
1\!:\!6&\mathrm{tf1}&0,1,2,3,4,5\\
7\!:\!12&\mathrm{tf2}&0,1,2,3,4,5\\
13\!:\!18&\mathrm{tg1}&0,1,2,3,4,5\\
19\!:\!24&\mathrm{tg2}&0,1,2,3,4,5\\
25\!:\!27&\mathrm{tg01}&0,2,4\\
28\!:\!30&\mathrm{tg02}&0,2,4.
\end{array}                                                \tag{1.0}
\]

For a stream of residue \(\rho\), its global \(t\)-shift is

\[
 r_\rho=6+\rho\quad(\rho\ne4),\qquad r_4=16,              \tag{1.1}
\]

where \(r_4=16\), rather than \(10\), records `PIN42`. Thus

\[
 X=\bigoplus_{q=1}^{30}t^{r_q}k[[u]],\qquad \sum_qr_q=288. \tag{1.2}
\]

The corrected target is

\[
 Y^+=\bigoplus_{a=0}^{29}t^{s_a}k[[u]]e_a,               \tag{1.3}
\]

where

\[
 s_a=6+2((a+1)\bmod3)\quad(0\le a\le28),\qquad
 s_{28}=16,\qquad s_{29}=36,                             \tag{1.4}
\]

and \(\sum_as_a=276\). Every direct sum here is a finite direct sum of
formal-series spaces, hence a product in the coefficient direction.

Embed these spaces in their global \(t\)-series ambient spaces and put

\[
 F^nM=M\cap t^nM_{\rm amb}.
\]

Equivalently, for
\(x=(t^{r_q}x_q(u))_q\) and \(y=(t^{s_a}y_a(u))_a\), define

\[
\begin{aligned}
 \nu_X(x)&=\min_q\{r_q+6\operatorname{ord}_u x_q\},\\
 \nu_Y(y)&=\min_a\{s_a+6\operatorname{ord}_u y_a\},
\end{aligned}                                             \tag{1.5}
\]

with \(\nu(0)=\infty\). Then \(F^nX=\{x:\nu_X(x)\ge n\}\), and
similarly for \(Y^+\). These filtrations are decreasing, separated, and
complete, with finite-dimensional graded pieces.

At a fully specified allowed source point \(s\), use the actual all-depth
normalized orbit products in the map

\[
 \mathcal E(x)=(\theta\Phi-12\Phi)\Gamma_\eta
       -\Phi_\eta(\theta\Gamma-18\Gamma)+42t^{20}.        \tag{1.6}
\]

Equation (1.6) uses the chosen gauge \(c_fc_g=1\); without it the last scalar
coefficient is \(42/(c_fc_g)\). The B-orbits, finite \(u_f/v_f\) data, pole
scales, chart units, and `PIN42` are held fixed. Thus the tangent mode is
`tails`, never `tailsW`.

For a tail variation \(h\), put
\(\delta\Phi=D\Phi_s(h)\) and \(\delta\Gamma=D\Gamma_s(h)\), computed from
that same source-dependent orbit-product map. The series-valued derivative is

\[
\begin{aligned}
D\mathcal E_s(h)={}&(\theta\delta\Phi-12\delta\Phi)\Gamma_\eta
 +(\theta\Phi-12\Phi)(\delta\Gamma)_\eta\\
&-(\delta\Phi)_\eta(\theta\Gamma-18\Gamma)
 -\Phi_\eta(\theta\delta\Gamma-18\delta\Gamma).          \tag{1.6a}
\end{aligned}
\]

Thus differentiating already-emitted scalar coefficient rows is not a
substitute for differentiating the all-depth map: \(\theta\) acts on the
unknown variation itself.

Under the required all-depth gate `CYCLIC-30`, write universally on the
admissible source ball

\[
 \mathcal E(x)=\sum_{a=0}^{29}t^{s_a}H_a(x;u)\eta^a       \tag{1.7}
\]

and define the shifted nonlinear map

\[
 \mathcal H(x)=\bigl(t^{s_a}H_a(x;u)\bigr)_{a=0}^{29}\in Y^+.
                                                                  \tag{1.8}
\]

If literal `CYCLIC-30` is replaced by the weaker direct-bridge route, (1.8)
instead denotes the first 30 selected component streams and `BRIDGE-30` must
give universal ideal-membership identities for every further component. The
Newton argument solves (1.8); those identities then force the remaining
components to vanish.

Its derivative at \(s\) is the corrected operator

\[
 L_s^+=D\mathcal H_s\in
 \operatorname{Mat}_{30}\bigl(k[[u]]\langle\Theta\rangle\bigr),
 \qquad \Theta u=u(\Theta+1).                            \tag{1.9}
\]

There is one \(30\times30\) operator. There is no free input stream and no
minimization over 29-column minors.

A depth-\(D\) solution means, in this global filtration,

\[
 \mathcal H(s)\in F^DY^+;                                \tag{1.10}
\]

equivalently,

\[
 [u^j]H_a(s)=0\quad\text{whenever }s_a+6j<D.              \tag{1.11}
\]

For a finite jet, (1.10) is independent of unspecified higher source
coefficients by causality. The derivative and its all-depth inverse are not:
the certificate must name a legal full completion \(s\) and build \(L_s^+\)
from that same completion, including the actual x-side correction rather than
silently deleting it.

## 2. Delayed surjectivity and a causal right section

The Round-6 delayed loss is the correct linear invariant:

\[
 \ell(L)=\min\left\{e\ge0:
 F^{n+e}Y\subseteq L(F^nX)\ \text{for every }n\ge0\right\}. \tag{2.1}
\]

If the displayed set is empty, define \(\ell(L)=\infty\).

It is useful to make explicit what (2.1) supplies.

### Lemma 2.1 (delayed inclusion is equivalent to a bounded section)

Let \(X,Y\) be finite sums of shifted one-variable formal-series spaces with
the global-order filtration, and let \(L:X\to Y\) be continuous and
\(k\)-linear. For an integer \(e\ge0\), the following are equivalent.

1. \(F^{n+e}Y\subseteq L(F^nX)\) for every \(n\ge0\).
2. There is a continuous \(k\)-linear map

   \[
   S:F^eY\longrightarrow X                              \tag{2.2}
   \]

   such that

   \[
   LS=\operatorname{id}_{F^eY},\qquad
   S(F^{n+e}Y)\subseteq F^nX\quad(n\ge0).                \tag{2.3}
   \]

#### Proof

The implication \(2\Rightarrow1\) is immediate. Conversely, split \(Y\) by
exact global \(t\)-degree:

\[
 F^eY=\prod_{m\ge e}Y[m],
\]

where every \(Y[m]\) is finite-dimensional and is zero when degree \(m\) is
not one of the allowed congruence classes. For a basis vector
\(v\in Y[m]\), hypothesis 1 with \(n=m-e\) gives an
\(x_v\in F^{m-e}X\) satisfying \(Lx_v=v\). Choose these preimages basis by
basis and extend to a linear map \(S_m:Y[m]\to F^{m-e}X\).

For \(y=\sum_{m\ge e}y_m\), set

\[
 Sy=\sum_{m\ge e}S_my_m.                                \tag{2.4}
\]

The sum converges because its \(m\)-th term lies in \(F^{m-e}X\).
Continuity of \(L\) gives \(LSy=\sum_my_m=y\), and (2.3) follows degree by
degree. \(\square\)

Thus an all-depth proof of (2.1) is mathematically enough. For a machine
certificate, however, the choices in (2.4) must be replaced by an exact Ore
identity or a finite-state causal recurrence whose initial transient and
all-index identities prove (2.3) for every degree; any claimed periodic part
must itself be proved, including its boundary identities. A finite rank
profile does not prove (2.1).

We call any \(e\) for which (2.2)--(2.3) has been proved a **certified inverse
loss**. It need not be minimal.

### Remark 2.2 (relation to the ordinary DEPTH-STAB minor)

For an \(R\)-linear square matrix \(A\) with
\(\det A=t^e\varepsilon\), \(\varepsilon\in R^\times\), the adjugate formula

\[
 S=(\det A)^{-1}\operatorname{adj}(A):t^eR^r\longrightarrow R^r
                                                                  \tag{2.5}
\]

is a causal right section of loss at most \(e\). Corollary 3.2 therefore
recovers the usual \(2e+1\) minor criterion. In the present problem,
\(L_s^+\) is only \(k\)-linear: \(\Theta u=u(\Theta+1)\), so an \(R\)-matrix
adjugate does not apply. Equations (2.2)--(2.3) are the exact replacement,
not an analogy based only on an Ore index.

## 3. Filtered Newton with loss

The next theorem is dimension-free and does not assume that \(L\) is
\(k[[t]]\)-linear.

### Theorem 3.1 (filtered fixed-linearization Newton theorem)

Let \(X,Y\) be complete separated filtered \(k\)-vector spaces, with linear
topologies defined by \(F^nX,F^nY\). Let \(\mathcal H\) be a continuous map on
the affine space \(s+F^1X\), and put

\[
 A=\mathcal H(s),\qquad L=D\mathcal H_s,\qquad
 N(h)=\mathcal H(s+h)-A-Lh.                              \tag{3.1}
\]

Assume:

1. \(A\in F^DY\);
2. \(L\) has a causal right section \(S:F^eY\to X\) satisfying
   (2.3); and
3. for some fixed integer \(\sigma\ge0\), the nonlinear remainder satisfies

   \[
   N(F^aX)\subseteq F^{2a-\sigma}Y                       \tag{3.2}
   \]

   and, whenever \(h,h'\in F^aX\) and
   \(h-h'\in F^mX\), \(m\ge a\),

   \[
   N(h)-N(h')\in F^{a+m-\sigma}Y.                        \tag{3.3}
   \]

If

\[
                       D\ge2e+\sigma+1,                  \tag{3.4}
\]

then there is an \(h_\infty\in F^{D-e}X\) such that

\[
                       \mathcal H(s+h_\infty)=0.         \tag{3.5}
\]

Only the fixed derivative \(D\mathcal H_s\) is used.

#### Proof

Put

\[
 q=D-e,
\]

so (3.4) gives \(q-e-\sigma=D-2e-\sigma\ge1\). On the
complete ball \(B=F^qX\), define

\[
 T(h)=-S\bigl(A+N(h)\bigr).                              \tag{3.6}
\]

This is defined because \(A\in F^DY=F^{q+e}Y\subseteq F^eY\), while

\[
 N(h)\in F^{2q-\sigma}Y\subseteq F^{q+e}Y                \tag{3.7}
\]

by \(q\ge e+\sigma\). The section bound now gives \(T(h)\in F^qX\), so
\(T\) maps \(B\) to itself.

If \(h,h'\in B\) and \(h-h'\in F^mX\), \(m\ge q\), then (3.3) and
(2.3) give

\[
\begin{aligned}
 T(h)-T(h')
 &=-S\bigl(N(h)-N(h')\bigr)\\
 &\in F^{q+m-\sigma-e}X\\
 &=F^{m+c}X,
 \qquad c:=D-2e-\sigma\ge1.                             \tag{3.8}
\end{aligned}
\]

Start with \(h_0=0\) and set \(h_{j+1}=T(h_j)\). Both \(h_0,h_1\) lie in
\(F^qX\), and (3.8) inductively yields

\[
 h_{j+1}-h_j\in F^{q+jc}X.                              \tag{3.9}
\]

Hence \((h_j)\) is Cauchy and converges, by completeness, to some
\(h_\infty\in F^qX\). The same estimates make \(T\) continuous on \(B\),
so \(h_\infty=T(h_\infty)\). Applying \(L\) and using \(LS=1\) gives

\[
 Lh_\infty=-A-N(h_\infty).
\]

Together with (3.1), this is (3.5). \(\square\)

### Corollary 3.2 (zero quadratic loss)

When \(\sigma=0\), the exact integer-depth gate is

\[
                  \boxed{D\ge2e+1}
       \quad\Longleftrightarrow\quad
                  \boxed{e\le\left\lfloor\frac{D-1}{2}\right\rfloor}. \tag{3.10}
\]

More sharply, if the actual residual order is
\(\nu=\nu_Y(\mathcal H(s))\), it is enough that

\[
                            \boxed{\nu>2e}.               \tag{3.11}
\]

The correction has order at least \(\nu-e\). In particular, this theorem
does **not** promise a formal root with the entire depth-\(D\) jet fixed. To
obtain congruence modulo \(F^A\), and hence preserve all coefficients of order
strictly below \(A\), one needs \(\nu\ge A+e\), in addition to (3.11). To
preserve the coefficient of \(t^A\) as well, one needs
\(\nu\ge A+e+1\). If \(\nu=\infty\), the starting point is already a root
and no correction is needed.

### Proposition 3.3 (the \(+1\) is sharp)

For every \(e\ge1\), the bound \(D=2e\) is insufficient, even for an
ordinary polynomial map. Over \(k[[t]]\), take

\[
 \mathcal F(x_1,x_2)=
 \bigl(t^ex_1+t^{2e},\ t^ex_2+x_1x_2-t^{2e}\bigr)        \tag{3.12}
\]

at \(s=(0,0)\). Its derivative is \(L=t^eI_2\), which has inverse loss
\(e\), and \(\mathcal F(s)\in F^{2e}\). The first equation of a root forces
\(x_1=-t^e\); the second then becomes \(-t^{2e}=0\), a contradiction.
Thus \(2e+1\), rather than \(2e\), is the sharp uniform threshold.

## 4. Why the Euler terms have zero quadratic loss

### Lemma 4.1 (Euler operators preserve order)

For every field \(k\) and every \(n\ge0\),

\[
 \theta(t^nR)\subseteq t^nR.                             \tag{4.1}
\]

Indeed, if \(f\in R\),

\[
 \theta(t^nf)=t^n(nf+\theta f).                          \tag{4.2}
\]

After the residue split,

\[
 \theta\bigl(t^rZ(u)\bigr)=t^r(r+6\Theta)Z(u).           \tag{4.3}
\]

These formulas remain true in characteristic \(p\). A scalar such as
\(n\), \(r+6j\), or \(j\) may vanish modulo \(p\), but that can only raise
order; it cannot lower it.

### Lemma 4.2 (Euler-differential polynomials have \(\sigma=0\))

Let \(\mathcal P\) be a finite polynomial expression, with coefficients of
nonnegative \(t\)-order, in finitely many series \(x_i\) and their Euler
derivatives \(\theta^jx_i\). Localizations at fixed chart units are allowed.
Then the remainder of \(\mathcal P\) about any fixed point satisfies
(3.2)--(3.3) with \(\sigma=0\).

#### Proof

Expand each monomial after \(x\mapsto x+h\). Subtracting its constant and
linear parts leaves only terms with at least two factors among
\(\theta^jh_i\). If \(h\in F^aX\), Lemma 4.1 puts every such factor in
\(F^a\), while multiplication adds orders. This proves (3.2).

For (3.3), subtract the corresponding remainder at \(h'\) and telescope
each product. Every resulting term has one factor
\(\theta^j(h_i-h_i')\in F^m\) and, because the original variation degree
was at least two, at least one further factor coming from \(h\) or \(h'\),
of order at least \(a\). All background factors and coefficients have
nonnegative order. Hence every term has order at least \(a+m\). No
Taylor factorial or division by the characteristic was used. \(\square\)

Here **restricted on an \(F^1\)-ball** means that, modulo every \(F^N\), only
finitely many monomials contribute, uniformly for the value, its linear part,
and the two-point remainder. Such an expression is a filtration limit of
finite differential polynomials. The estimates just proved pass to the limit
because every \(F^N\) is closed. This proves the same result for restricted
differential power series; it is not merely a formal use of the word
“convergent.”

A source-dependent inverse is covered only with a filtered unit audit. Assume
first that \(U\) itself is a restricted integral expression covered by Lemma
4.2, or directly that its own linearization remainder satisfies
(3.2)--(3.3) with \(\sigma=0\). If \(U(s)\) is an order-zero unit and

\[
 U(s+h)-U(s)\in F^a,
 \quad
 (U(s+h)-U(s))-(U(s+h')-U(s))\in F^m                 \tag{4.4}
\]

whenever \(a\ge1\), \(m\ge a\), \(h,h'\in F^a\), and
\(h-h'\in F^m\), then
\(U(s+h)^{-1}\) has the convergent geometric expansion in
\(U(s)^{-1}(U(s+h)-U(s))\). After subtracting the constant and linear
parts, the first geometric term contributes the already quadratic remainder
of \(U\), and all later terms have variation degree at least two. Thus the
same proof applies. Being a unit at each point, without both the filtered
difference estimates and the quadratic audit of \(U\), is not enough. What
is also not allowed without accounting for it is an unrecorded negative power
of \(t\); a normalization losing \(\sigma\) orders must use Theorem 3.1 with
that \(\sigma\).

The full expression (1.6) is built from products, \(\eta\)-differentiation,
and \(\theta\). Therefore, once `CYCLIC-30` identifies the all-depth streams
and `FILTER-30` exhibits the source-dependent normalized products on the
whole Newton ball as integral filtered expressions, Lemma 4.2 proves the
required quadratic estimate with \(\sigma=0\). The Euler terms themselves
cause no additional Hensel loss; \(\eta\)-differentiation changes only the
finite component label and does not change \(t\)-order.

Characteristic-\(p\) resonance is instead a **linear inverse** issue. For
example, on \(k[[u]]\) in characteristic \(p\),

\[
 (\Theta+1)u^j=(j+1)u^j.                                 \tag{4.5}
\]

Every truncation ending before \(u^{p-1}\) is invertible, but the operator
misses \(u^{p-1},u^{2p-1},\ldots\). Its all-depth delayed loss is infinite.
This is a direct counterexample to promoting a low-window rank profile or an
apparently stable defect without closing the full \(p\)-periodic recurrence.

## 5. The completed-ideal bridge

There are two different bridge obligations: a filtered finite-depth bridge
for the initial residual, and a full completed-ideal bridge for the final
solution. Both live **before numerical evaluation**. After specialization to
a point the coefficients are scalars, so a “coefficient ideal over \(k\)” is
not the needed statement.

Fix an admissible witness cylinder \(\mathscr B\), for example the Newton
ball \(s+F^1X\), with its named base relations and chart units. For each
global depth \(N\), let \(C_N\) be the localized finite-jet coordinate ring
representing the allowed \(N\)-jets in \(\mathscr B\). It contains exactly
the source coefficient variables that causality permits to affect raw
coefficients of order \(<N\), modulo the named base and pin relations, and it
inverts only the named chart units. Jet truncation is contravariant on
coordinate rings: for \(M\ge N\) it gives a pullback \(C_N\to C_M\). Write

\[
 C_{\rm alg}=\varinjlim_N C_N,
 \qquad
 \widehat C=\varprojlim_\lambda C_{\rm alg}/\mathfrak a_\lambda,       \tag{5.1}
\]

where \((\mathfrak a_\lambda)\) is an explicitly declared defining filtration
and \(\widehat C\) is required to be separated. Thus \(C_{\rm alg}\) is the
ring of causal polynomial functions on finite jets, and \(\widehat C\) is a
chosen completion—not an inverse limit of the jet coordinate rings. Require
all pullbacks and universal coefficient functions to be compatible. Every
formal point \(x\in\mathscr B\) gives evaluation maps, compatible under
pullback,

\[
                         \operatorname{ev}_{x,N}:C_N\to k.             \tag{5.2}
\]

### Proposition 5.1 (universal coefficient bridge under CYCLIC-30)

Let \(A\) be a commutative ring. Suppose the universal identity

\[
 \mathcal E=\sum_{a=0}^{29}t^{s_a}H_a(u)\eta^a,
 \qquad H_a(u)=\sum_{j\ge0}h_{a,j}u^j,                  \tag{5.3}
\]

holds in \(A[[t]][\eta]\), with every higher \(\eta\)-component identically
zero. Then

\[
 [t^n\eta^a]\mathcal E=
 \begin{cases}
 h_{a,j},&0\le a\le29,\ n=s_a+6j,\ j\ge0,\\
 0,&\text{otherwise}.
 \end{cases}                                             \tag{5.4}
\]

Consequently, in \(A\), the pristine coefficient ideal is

\[
 I_E^+=\bigl(h_{a,j}:0\le a\le29,\ j\ge0\bigr),          \tag{5.5}
\]

and its part below depth \(D\) is

\[
 I_{E,<D}^+=\bigl(h_{a,j}:s_a+6j<D\bigr).                \tag{5.6}
\]

#### Proof

Substitute the \(u\)-expansions into (5.3) and use \(u=t^6\). Uniqueness of
coefficients in \(A[[t]][\eta]\) gives (5.4), hence (5.5)--(5.6).
\(\square\)

The relevant instances are the truncated statement over \(A=C_N\) and the
all-depth statement over \(A=C_{\rm alg}\) or its declared completion, not the
already evaluated field. Under literal `CYCLIC-30`, Proposition 5.1 supplies
the raw coefficient bridge. If `CYCLIC-30` is weakened, `BRIDGE-30` must
additionally supply universal membership identities for every higher
\(\eta\)-component.

### Lemma 5.2 (levelwise ideal equality gives completed equality)

Let \(C\) be a separated complete linearly topologized ring with defining
ideals \(\mathfrak a_N\), and let \(I,J\subseteq C\). If

\[
 (I+\mathfrak a_N)/\mathfrak a_N
   =(J+\mathfrak a_N)/\mathfrak a_N\quad\text{for every }N, \tag{5.7}
\]

then

\[
                         \overline I=\overline J.         \tag{5.8}
\]

#### Proof

For a linear topology,

\[
 \overline I=\bigcap_N(I+\mathfrak a_N),\qquad
 \overline J=\bigcap_N(J+\mathfrak a_N).
\]

Equation (5.7) says \(I+\mathfrak a_N=J+\mathfrak a_N\) for each \(N\), so
the intersections agree. \(\square\)

Completeness is used to realize \(C\) as the intended inverse-limit
coefficient algebra; the displayed closure formula itself only needs the
stated linear topology.

For a direct, evaluation-safe bridge, let \(h_N\) be the finite vector of
the universal selected coefficients \(h_{a,j}\) of order \(<N\), and let
\(g_N\) be the finite vector of all pristine raw equations of order \(<N\),
both in \(C_N\). `BRIDGE-30` must give rectangular matrices over \(C_N\)

\[
                 g_N=U_Nh_N,\qquad h_N=V_Ng_N,           \tag{5.9}
\]

compatible after pullback to every deeper jet ring, with every denominator a
named chart unit. The
first identity is the implication needed after Newton; the second proves
equality of ideals in each \(C_N\), hence in \(C_{\rm alg}\); their closures
then agree in every declared separated completion. The same two-sided
identities must connect any emitted Schur/pivot row vector to the pristine
one. Exact reconstruction and direct pristine-row replay are an alternative.

### Proposition 5.3 (the levelwise bridge transfers a formal zero)

Assume the first identity in (5.9) for every \(N\). If a formal point
\(x\in\mathscr B\) satisfies every selected coefficient \(h_{a,j}(x)=0\),
then every pristine equation vanishes at \(x\).

#### Proof

For each \(N\), evaluate the identity \(g_N=U_Nh_N\) using (5.2). Its
right-hand side is zero, so every pristine coefficient of order \(<N\) is
zero. Since \(N\) is arbitrary, all pristine coefficients vanish.
\(\square\)

This finite-level proof, not closure equality alone, is the safe vanishing
argument: evaluation at an infinite tail point need not have closed kernel
for an arbitrary tail topology. Lemma 5.2 records the completed-ideal equality
that (5.9) also proves inside the declared completion \(\widehat C\) of (5.1).

The initial residual must likewise be recomputed directly by (1.11), or from
a filtration-triangular identity; an arbitrary presentation change can mix
levels. Equality of radicals, equality of point sets, or one-way reduction is
insufficient. Radical, saturation, Rabinowitsch, pivot-definition, and
`W`-pin equations are fixed base-chart conditions, not extra tail-function
rows; reconstruction must show that they remain satisfied on \(\mathscr B\).

## 6. Conditional Euler/Ore lifting theorem for this campaign

### Theorem 6.1 (corrected 30-stream germ certificate)

Fix a coefficient field \(k\), a named radical/chart branch, `PIN42`, and all
other held-fixed base data. Let \(s_D\) be a depth-\(D\) point. Suppose a
certificate supplies:

1. a legal full source completion \(s\) of \(s_D\);
2. the source-dependent all-depth map on \(s+F^1X\), together with
   `CYCLIC-30`, or the surplus-membership alternative in `BRIDGE-30`, as
   universal identities on that whole ball;
3. the exact residual check \(\mathcal H(s)\in F^DY^+\);
4. the exact derivative \(L_s^+=D\mathcal H_s\), independently replayed from
   (1.6);
5. a causal right section

   \[
   S:F^eY^+\to X,\qquad L_s^+S=1,\qquad
   S(F^{n+e}Y^+)\subseteq F^nX\quad(n\ge0);              \tag{6.1}
   \]

6. `FILTER-30` on \(s+F^1X\), including unit control for every localization;
7. the levelwise pristine/emitted identities (5.9) of `BRIDGE-30` throughout
   that ball; and
8. \(D\ge2e+1\).

Then there is an allowed formal tail tuple

\[
 s_\infty\in s+F^{D-e}X                               \tag{6.2}
\]

over \(k[[t]]\) satisfying the full pristine formal equation system on the
named chart. It agrees with the supplied finite point only below depth
\(D-e\); “lifts” here means lifting that shorter truncation. Hence a scoped
mod-\(p\) formal germ exists, but not necessarily one with the entire
depth-\(D\) jet \(s_D\).

#### Proof

`FILTER-30` and Lemma 4.2 give (3.2)--(3.3) with \(\sigma=0\). Theorem 3.1 applied to
\(\mathcal H\), \(L_s^+\), and (6.1) produces
\(s_\infty=s+h_\infty\) with all 30 \(H_a\) zero and with (6.2).
The point \(s_\infty\) remains in \(s+F^1X\). Proposition 5.3, applied to the
universal `BRIDGE-30` identities, makes every pristine formal equation vanish.
The corrections lie only in \(X\), so all held-fixed chart conditions and pins
remain fixed, and the certified chart denominators remain units. \(\square\)

The proof uses the one operator \(L_s^+\) throughout. There is no additional
requirement that right inverses at the Newton iterates be stable.

## 7. Exact certificate contract

An implementation should report the following, with exact identities rather
than only hashes or finite samples.

### 7.1 Scope and completion

- coefficient field, prime/extension, \(t=x^{-1/42}\), and \(u=t^6\);
- depth \(D\), branch, chart units, frozen data, pins, witness, and
  reconstruction provenance;
- every coefficient of the chosen full completion in a finite symbolic,
  rational, recurrent, or otherwise exactly evaluable representation;
- the universal source-dependent rule for the actual \(t^{42+}\) x-side
  factors under every tail variation in \(s+F^1X\), not merely their values
  and first derivatives at \(s\).

For D23/D25 reconstruction, the banked DEEPMAP true-name registry is part of
that provenance and must be replayed canonically:

```text
x74=tg02_54  x75=tg01_54  x76=tg2_54   x77=tg2_49
x78=tg1_54   x79=tg1_49   x80=tf2_54   x81=tf2_49
x82=tf1_54   x83=tf1_49
```

The old swapped names are import-only aliases, not matrix labels.

An arbitrary zero completion of genuinely free source coordinates is allowed
only if it is named and the **full** equation and derivative are recomputed
there. Zeroing the omitted x-side correction in the pure-y constructor is not
such a completion.

### 7.2 Source and residual

- all 30 input and 30 output labels, their order, and shifts (1.0)--(1.4);
- an all-depth `CYCLIC-30` proof, or the universal levelwise
  surplus-membership alternative of `BRIDGE-30` for every additional output;
- the raw label bijection

  \[
  (n,a)\longleftrightarrow
  \left(a,\frac{n-s_a}{6}\right);
  \]

  here \(0\le a\le29\), \(n\ge s_a\), and
  \(n\equiv s_a\pmod 6\);

- exact replay of every raw coefficient below \(D\), giving

  \[
  \nu:=\nu_Y(\mathcal H(s))\ge D.                        \tag{7.1}
  \]

  If the starting point was certified only in emitted rows, a direct replay
  or filtration-triangular finite-level bridge must establish (7.1).

### 7.3 Linear certificate

- the exact all-depth Ore coefficients of \(L_s^+\), with the operator tied to
  the same completion as the residual;
- causality in the global \(t\)-filtration;
- an exact description of \(S\) and proofs, on every target basis stream, of

  \[
  L_s^+S=I,\qquad
  \nu_X(Sy)\ge\nu_Y(y)-e\quad(\nu_Y(y)\ge e);             \tag{7.2}
  \]

- for a recurrence certificate: a finite symbolic rule parameterized by the
  target basis index \(j\), its memory and initial transient, an invariant
  state space, and identities proving (7.2) for all \(j\). A finite period may
  replace the all-\(j\) proof only after the certificate proves that the full
  operator coefficients and transition data—not merely the scalar \(j\)
  occurring in \(\Theta u^j=ju^j\)—are periodic or finite-state, and verifies
  every boundary state.

Neither bounded \(\delta^+(N)\) nor its apparent stabilization proves (7.2).

### 7.4 Presentation and final inequality

- one finite symbolic rule producing the compatible two-sided identities
  (5.9) for arbitrary \(N\), or direct universal reconstruction/replay; a
  finite list of unrelated sampled matrices is not a proof for every level;
- the `FILTER-30` syntax/unit audit invoking Lemma 4.2; and
- the sharp decisive check

  \[
                         \boxed{\nu-2e\ge1}.              \tag{7.3}
  \]

  If the advertised certificate records only a guaranteed depth \(D\le\nu\),
  the directly checkable sufficient form is

  \[
             \boxed{\nu\ge D\quad\text{and}\quad 2e+1\le D}. \tag{7.4}
  \]

If a normalization audit finds a loss \(\sigma>0\), replace (7.3) by
\(\nu-2e-\sigma\ge1\), or the second inequality in (7.4) by
\(2e+\sigma+1\le D\).

## 8. What \(e^+\) should mean

First define the Round-6 diagnostics without importing conventions from
another file. Strip the shifts from an input as
\(x_q=t^{r_q}\sum_{j\ge0}x_{q,j}u^j\), and likewise strip \(t^{s_a}\) from
the output. Causality makes the first \(N\) normalized output coefficients
depend only on the first \(N\) normalized input coefficients. In the ordered
bases \((q,j)\), \((a,j)\), \(0\le j<N\), let

\[
 M^+(N):(k[u]/u^N)^{30}\longrightarrow(k[u]/u^N)^{30}   \tag{8.1}
\]

be the resulting \(30N\times30N\) matrix of \(L_s^+\), and put

\[
                  \delta^+(N)=30N-\operatorname{rank}M^+(N).          \tag{8.2}
\]

The symbol \(d^+\) may be recorded only when an exact all-depth recurrence or
Ore normal form proves that some integer \(N_0\) satisfies

\[
                  \delta^+(N)=d^+\quad\text{for every }N\ge N_0.     \tag{8.3}
\]

A long constant sample is not (8.3). Even (8.3) does not itself construct a
section.

The Newton theorem does not use this defect/index diagnostic. Let
\(\ell^+=\ell(L_s^+)\) be the minimal loss (2.1), and let

\[
 e^+_{\rm cert}:=\text{any proved upper bound on \(\ell^+\) realized by
 a section satisfying (7.2)}.                              \tag{8.4}
\]

It is safest to retain two separate fields:

```text
E_LOSS_CERT     = e_cert_plus
E_INDEX         = 6*d_plus - 12       # diagnostic only
```

If (8.3) is proved, the corrected index diagnostic is

\[
 (e^+)^{\rm idx}=6d^++\sum_as_a-\sum_qr_q=6d^+-12.       \tag{8.5}
\]

The legacy convention may call this number \(e^+\), but it becomes a
conservative Newton certificate only when the same exact normal form also
proves a section with

\[
 0\le\ell^+\le(e^+)^{\rm idx}.                           \tag{8.6}
\]

Merely proving (8.3), computing (8.5), and checking a weighted pivot sum is
not sufficient. Conversely, a direct section of loss \(e\) proves a lift
using (7.3) even when the index is larger or unavailable.

For a residual known only to depth \(D\), the nominal thresholds are:

| guaranteed depth | theorem gate using minimal loss | implementer check | conservative index route |
|---:|---:|---:|---:|
| \(23\) | \(\ell^+\le11\) | \(e^+_{\rm cert}\le11\) | \(\ell^+\le(e^+)^{\rm idx}\le11\) |
| \(25\) | \(\ell^+\le12\) | \(e^+_{\rm cert}\le12\) | \(\ell^+\le(e^+)^{\rm idx}\le12\) |
| \(D\) | \(\ell^+\le\lfloor(D-1)/2\rfloor\) | \(e^+_{\rm cert}\le\lfloor(D-1)/2\rfloor\) | same with the proved index upper bound |

At the boundary values, the D23 correction lies in \(F^{12}X\), while the
D25 correction lies in \(F^{13}X\). Smaller losses preserve correspondingly
more of the supplied point; neither boundary case preserves the whole D23 or
D25 jet.

Since \((e^+)^{\rm idx}=6d^+-12\), the conservative D25 route permits only
\(d^+=2,3,4\), giving indices \(0,6,12\); D23 permits only \(d^+=2,3\).
Those integer restrictions do not replace PARAM-30.

These table entries use only the advertised depth. The exact, sharper
implementation is always (7.3): extra residual vanishing \(\nu>D\) permits a
larger certified loss up to \(\lfloor(\nu-1)/2\rfloor\).

Round 6's finite-window rank computation, together with its causality check
that inputs above band 40 cannot affect degree 36, puts the degree-36 target
\(t^{36}e_{29}\) outside the full image \(L_s^+(X)\) at 36 sampled operators.
Taking \(n=6\) in (2.1) gives its stated valid bound \(\ell^+\ge31\). With the
literal \(n\ge0\) convention in (2.1), the same fact gives the following
**new strengthening** of that banked bound:

\[
                              \boxed{\ell^+\ge37}:        \tag{8.7}
\]

for every \(e\le36\), that target lies in \(F^eY^+\) but not in \(L_s^+(X)\).
This concerns exactly six witnesses times three deep draws times two primes
on the single `a00pp` radical fiber—not 36 atlas fibers, and not unsampled
D25 completions.

Thus those sampled operators fail the nominal D23/D25 depth-only gate. They
could pass (7.3) only at a completion with actual residual order at least 75,
which would itself be a depth-75 point. A certificate using only that depth-75
guarantee would require \(e^+_{\rm cert}\le37\); for \(\nu>75\), the exact
allowance is instead \(e^+_{\rm cert}\le\lfloor(\nu-1)/2\rfloor\). In every
case all other gates are still required, and the lower bound (8.7) supplies
neither a section nor a germ.

At D25:

- family-wide EMPTY kills the scoped formal germ without any Newton lemma;
- one named NONEMPTY survivor with one legal full completion at which the
  residual, derivative, `CYCLIC-30` (or its bridge alternative), `BRIDGE-30`,
  `FILTER-30`, `PARAM-30` of loss at most \(12\), and (7.4) are all certified
  proves a scoped mod-\(p\) formal germ by Theorem 6.1;
- NONEMPTY without those certificates is only finite-depth survival.

## 9. Minimal remaining lemma list

Everything below is an application gate, not a gap in Theorem 3.1.

### CONJECTURE CYCLIC-30 (literal all-depth support/source generation)

Universally on the admissible source ball, the full orbit products, including
every normalized x-side term beginning at \(t^{42}\), satisfy

\[
 \mathcal E=\sum_{a=0}^{29}t^{s_a}H_a(u)\eta^a             \tag{9.1}
\]

identically, with the asserted congruence classes and with every
\(\eta^a\)-component for \(a\ge30\) identically zero. This is Round 6's
`CYCLIC-30` gate. The current band-41 regression does not prove it. The
discovery of \(H_{29}\) after the old 29-stream assertion is the concrete
warning against extrapolating the regression.

Literal `CYCLIC-30` is stronger than the lifting theorem needs. Its weakest
sufficient replacement is the universal **surplus part of `BRIDGE-30`**:
retain the first 30 streams as \(\mathcal H\), and provide a finite symbolic
rule expressing every higher component coefficient in their levelwise ideal.
That replacement must not be reported as `CYCLIC-30`.

### CONJECTURE BRIDGE-30 (pristine/emitted ideal bridge)

In the universal finite jet rings \(C_N\) on the whole Newton ball, the ideal
of the full pristine depth tower equals the levelwise ideal generated by the
30 \(H_a\), through the compatible two-sided identities (5.9). If literal
`CYCLIC-30` fails, these identities also include every surplus \(\eta\)-row.
Every emitted Schur/pivot presentation is connected to the pristine vector by
the same kind of identities over named chart units. Set-theoretic equality,
radical equality, and identities only after evaluation at \(s\) are
insufficient.

`CYCLIC-30` proves the raw coefficient part through Proposition 5.1. The
reconstruction/presentation part still needs its own certificate.

### CONJECTURE FILTER-30 (zero nonlinear filtration loss)

On \(s+F^1X\), the actual source-dependent all-depth normalized orbit
products—including the \(t^{42+}\) x-side terms—are restricted
Euler-differential power series with coefficients of nonnegative global
\(t\)-order in the precise restricted sense following Lemma 4.2. Every
localized denominator is a named order-zero unit and satisfies the filtered
variation estimates (4.4), and its defining expression has its own
zero-loss quadratic remainder as required in the inverse paragraph after
Lemma 4.2. Equivalently, the certificate may directly prove (3.2)--(3.3) with
\(\sigma=0\). Lemma 4.2 then discharges the nonlinear estimate; this gate is
an audit of the repository formula, not a missing Newton argument. If the
audit instead finds loss \(\sigma\), use \(\nu>2e+\sigma\).

### CONJECTURE PARAM-30 (pointwise all-depth Ore section)

For any point advertised as `LIVE`, its fully specified corrected operator
\(L_s^+\) admits an exact causal right section satisfying (7.2) with the
advertised finite loss. A proof must close the initial transient and every
\(p\)-periodic resonance. No current `valuation_e2.py` artifact does this for
the corrected square object; its primary computation remains the obsolete
29-column blocks with an appended \(H_{29}\) diagnostic.

### Required data, not a conjecture: legal completion

A finite D25 point does not specify the all-depth operator. The certificate
must give a legal full completion, a sufficiently long compatible lift plus a
proved finite-determinacy bound, or a uniform parametrix over the quantified
completion variables. Silent zero-fill is not a proof.

Once these four conjectural gates and the completion data are supplied at a
point, no further differential-Hensel lemma is missing: Theorem 6.1 promotes
the point exactly under (7.3), with (7.4) as its depth-only implementation.
