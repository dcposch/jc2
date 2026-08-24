# EXACT-COFRAME-GATE-20260824

Status: **FROZEN / PRIOR-ART-CORRECTED / EXACT SCOPED NEGATIVE / ROOT STOPPED**

- Producer: OpenAI Codex, GPT-5 family, root E
- Basis: dd11599b07eb05591b5c006791005eef19457d8e
- Frozen synthesis: xmodel/ideation-20260824T0453Z-synthesis.md
- Synthesis SHA-256: 76d9b7685771f65138fcb3c3dba1cfdd1ab104a9a5b21a7e3262c971f96ff790
- Preregistration freeze: 2026-08-24T06:37:51Z
- Preregistration SHA-256: d0d629c6231f814d2cd3ac0fdf76baef4240cbb6271b2271ae9a9f95e6d54658
- Computation discipline: one frozen one-shear orbit, one frozen three-parameter slice, no support or degree widening, and no elimination after the tangent gate failed.
- External discipline: primary-source lookup only; no public contact and no shared-ledger edit.

## Exact verdict

The conditional bridge is valid, but it is not a new reformulation. Wright's 1978 weak Jacobian theorem gives the stronger exact-coframe dichotomy: for a full determinant-one polynomial Jacobian, membership in \(E_2\) is equivalent to polynomial invertibility. Thus the implication below is a known side of that dichotomy:

\[
\begin{gathered}
M\in {\rm SL}_2(\mathbb C[x,y]),\\
a_y=b_x,\quad c_y=d_x,\quad
M\notin E_2(\mathbb C[x,y])
\end{gathered}
\quad\Longrightarrow\quad
M=J(P,Q)
\]

for a determinant-one plane Keller map \((P,Q)\) which is not a polynomial automorphism.

The proof uses literal nonmembership only. It does not form or multiply classes in an alleged quotient \({\rm SL}_2/E_2\), and it does not assume that \(E_2\) is normal in \({\rm SL}_2(\mathbb C[x,y])\).

The Cohn witness and its non-\(E_2\) lineage pass the source and certificate gate. The preregistered Broughton/Cohn orbit does not contain an exact coframe:

- the frozen bounded tangent target is outside the image, with matrix rank \(3\) and augmented rank \(4\);
- the coefficient ideal is the unit ideal by an explicit rational linear combination;
- no exact elimination was licensed;
- more strongly, no polynomial left shear at any degree completes the fixed Broughton row;
- there is no survivor to integrate into a full Keller pair.

The distinct scoped result produced by this gate is the fixed-row Broughton/Cohn no-go, not the exact-coframe reformulation itself. No claim of literature novelty is made for the scoped no-go.

Overall return:

**BRIDGE-VALID-BUT-WRIGHT-PRIOR-ART / COHN-CERTIFIED / EMPTY-TANGENT / ONE-SHEAR-NO-POLYNOMIAL / STOP.**

This is a scoped negative result for every determinant-one completion of one fixed exact Cohn row. It is not a result on the full double elementary orbit and not a result on JC2.

## 1. Protocol and freeze

The frozen synthesis was read in full. Before any symbolic curl or coefficient computation, the theorem premise, nonmembership standard, family, support, tangent license, and stop conditions were frozen in

cases/exact_coframe_gate_20260824/00_preregistration.md.

The frozen matrix family was

\[
M(h)=L(h)C_B,\qquad
L(h)=
\begin{pmatrix}1&0\\h&1\end{pmatrix},
\]

with the bounded replay restricted to

\[
h=c_0y^2+c_1xy^3+c_2x^2y^4.
\]

The preregistration separately licensed a proof for arbitrary polynomial \(h\) in this same one-left-shear family. It did not license a right factor, another left factor, a coordinate change, a generic sparse family, or a second elimination.

The first replay attempted to import SymPy and stopped immediately because SymPy is not installed. No equation or elimination ran in that attempt. The replay engine was replaced by a standard-library sparse polynomial ring over \(\mathbb Q\); the mathematical family and gate were unchanged.

## 2. Primary-source and certificate audit

### 2.1 Cohn

[Cohn's 1966 primary paper](https://www.numdam.org/item/PMIHES_1966__30__5_0/) proves in section 8 that a two-variable polynomial ring need not be GE2. The standard determinant-one witness used here is

\[
C=
\begin{pmatrix}
1+xy&x^2\\
-y^2&1-xy
\end{pmatrix}.
\]

Its determinant is one.

### 2.2 Park's executable nonmembership certificate

[Park's 1995 primary dissertation and Berkeley memorandum](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1995/ERL-95-39.pdf), Theorem 5.2.1 and its Cohn replay on printed pages 52–53, gives a directly usable necessary condition for elementary factorization. If an \({\rm SL}_2\) polynomial matrix has a rank-one leading-term matrix, then one leading row must be a monomial multiple of the other. Park's later [SIAM realization algorithm](https://doi.org/10.1137/S0895479897331096) decides elementary realizability over its stated polynomial rings.

For \(C\), the total-degree leading-form matrix is

\[
\operatorname{LF}(C)=
\begin{pmatrix}
xy&x^2\\
-y^2&-xy
\end{pmatrix}.
\]

Its rows are

\[
x(y,x),\qquad -y(y,x).
\]

The matrix has rank one, but neither row is a polynomial or monomial multiple of the other: the required multiplier would be \(-x/y\) or \(-y/x\). Park's necessary condition therefore gives the finite certificate

\[
C\notin E_2(\mathbb C[x,y]).
\]

The same argument works directly over \(\mathbb Q\) or \(\mathbb C\). No Mennicke-symbol computation is needed.

### 2.3 Cross-check of the alternate Cohn form

The current primary preprint [Chapovskyi–Kozachok–Petravchuk, arXiv:2412.03688](https://arxiv.org/abs/2412.03688) records

\[
C_{\rm alt}=
\begin{pmatrix}
x^2&xy-1\\
xy+1&y^2
\end{pmatrix}
\]

as the Cohn counterexample. It is exactly related to the chosen form by

\[
C(x,-y)
\begin{pmatrix}0&-1\\1&0\end{pmatrix}
=C_{\rm alt},
\]

and the constant rotation has the explicit elementary factorization

\[
\begin{pmatrix}0&-1\\1&0\end{pmatrix}
=U(-1)L(1)U(-1).
\]

Thus the two forms have the same literal nonmembership lineage.

### 2.4 Jung–van der Kulk

Van der Kulk's 1953 primary theorem says that every plane polynomial automorphism is tame. A modern primary proof, [Nguyen Van Chau, A Simple Proof of Jung's Theorem](https://arxiv.org/abs/math/0408077), states the precise generation form used below: over \(\mathbb C\), every plane polynomial automorphism is a finite product of linear automorphisms and shears

\[
(x,y)\longmapsto(x+p(y),y).
\]

Translations are included by constant \(p\), and conjugation by a linear swap gives the other orientation.

### 2.5 Wright priority and a necessary hostile control

[Wright's 1978 primary paper](https://www.sciencedirect.com/science/article/pii/0022404987900041), “The amalgamated free product structure of \({\rm GL}_2(k[X_1,\ldots,X_n])\) and the weak Jacobian theorem for two variables,” is the priority source. Its weak Jacobian theorem says that if the full Jacobian of two plane polynomials lies in \({\rm GE}_2\), then the polynomials generate the plane polynomial algebra. The precise statement is also printed with attribution to Wright's Theorem 6, page 250, in Shpilrain–Yu's primary article [“Polynomial Automorphisms and Gröbner Reductions”](https://shpilrain.ccny.cuny.edu/paperyu.pdf), printed page 6.

For determinant-one matrices over \(\mathbb C[x,y]\), \({\rm GE}_2\)-membership is the same as \(E_2\)-membership. Indeed, constant diagonal matrices normalize the elementary subgroup, and the remaining determinant-one diagonal factor is elementary; explicitly, for \(u\ne0\),

\[
\operatorname{diag}(u,u^{-1})
=\bigl(U(u)L(-u^{-1})U(u)\bigr)
 \bigl(U(-1)L(1)U(-1)\bigr).
\]

Combining Wright with Jung–van der Kulk therefore gives, for any full determinant-one polynomial Jacobian,

\[
J(P,Q)\in E_2(\mathbb C[x,y])
\quad\Longleftrightarrow\quad
(P,Q)\text{ is a polynomial automorphism}.
\]

This makes the exact-coframe reformulation prior art. The self-contained bridge proof in Section 3 is retained because it verifies the direction required by this gate without importing a stronger theorem.

There is also a source trap. Shpilrain–Yu Proposition 2.4 prints a strengthening which says that an arbitrary second row under a gradient first row in \({\rm GE}_2\) must itself be a gradient. The elementary matrix

\[
L(y)=\begin{pmatrix}1&0\\y&1\end{pmatrix}
\]

is an immediate counterexample to that extra assertion: its first row is \(d x=(1,0)\), while its second row has curl \(1\). This does not contradict Wright, whose hypothesis is a full Jacobian. Proposition 2.4's arbitrary-row conclusion is not used anywhere in this report.

### 2.6 Broughton control

The exact row below integrates to \(P=x+x^2y\), the standard example associated with [Broughton's 1988 primary paper](https://doi.org/10.1007/BF01404452). No topological theorem from that paper is needed here. Directly,

\[
P_x=1+2xy,\qquad P_y=x^2
\]

have no common zero, so \(P\) has no affine critical point. Also

\[
P^{-1}(0)=\{x=0\}\cup\{1+xy=0\}
\]

is reducible, so \(P\) is not a coordinate polynomial.

The full source record, URLs, and exact claims are frozen in

cases/exact_coframe_gate_20260824/01_source_audit.md.

## 3. The bridge theorem (self-contained replay of the required direction)

### Theorem

Let

\[
M=
\begin{pmatrix}a&b\\c&d\end{pmatrix}
\in {\rm SL}_2(\mathbb C[x,y]).
\]

Assume

\[
a_y=b_x,\qquad c_y=d_x.
\]

Then there are \(P,Q\in\mathbb C[x,y]\) with

\[
J(P,Q)=M.
\]

If \(M\notin E_2(\mathbb C[x,y])\), then \((P,Q)\) is a determinant-one Keller map which is not a polynomial automorphism.

### Proof: polynomial integration

For the first row define

\[
P(x,y)=\int_0^x a(t,y)\,dt+\int_0^y b(0,s)\,ds.
\]

Characteristic zero makes this a polynomial. Plain differentiation gives

\[
P_x=a(x,y)
\]

and, using \(a_y=b_x\),

\[
\begin{aligned}
P_y
&=\int_0^x a_y(t,y)\,dt+b(0,y)\\
&=\int_0^x b_x(t,y)\,dt+b(0,y)\\
&=b(x,y).
\end{aligned}
\]

The same formula with \(c,d\) produces \(Q\). Hence \(J(P,Q)=M\), and

\[
\det J(P,Q)=\det M=1.
\]

### Proof: tame automorphism Jacobians are elementary

Let \(S=\mathbb C[x,y]\).

First, substitution by any polynomial endomorphism of \(S\) preserves elementary matrices:

\[
U(f)\longmapsto U(f\circ\Phi),\qquad
L(f)\longmapsto L(f\circ\Phi).
\]

Second, every constant \(K\in{\rm GL}_2(\mathbb C)\) normalizes \(E_2(S)\), and this requires no normality in the full polynomial special linear group. Write

\[
K=\operatorname{diag}(\det K,1)\,K_0,
\qquad K_0\in{\rm SL}_2(\mathbb C).
\]

Gaussian elimination gives \(K_0\in E_2(\mathbb C)\). Conjugation by an element of \(E_2\) stays inside the subgroup. For \(\lambda\ne0\), direct multiplication gives

\[
\operatorname{diag}(\lambda,1)U(f)
\operatorname{diag}(\lambda^{-1},1)=U(\lambda f),
\]

\[
\operatorname{diag}(\lambda,1)L(f)
\operatorname{diag}(\lambda^{-1},1)=L(\lambda^{-1}f).
\]

Thus constant \({\rm GL}_2(\mathbb C)\) normalizes \(E_2(S)\) by explicit formulas.

Now use Jung–van der Kulk. A shear \((x+p(y),y)\) has Jacobian \(U(p'(y))\), which is elementary. A linear generator has a constant Jacobian. The chain rule is

\[
J(\Phi\circ\Psi)=(J\Phi\circ\Psi)J\Psi.
\]

Substitution leaves each elementary factor elementary. Repeatedly moving an elementary factor past the next constant factor, using only the constant normalizer just proved, writes the Jacobian of any plane automorphism as

\[
J\Phi=K E
\]

with \(K\in{\rm GL}_2(\mathbb C)\) constant and \(E\in E_2(S)\).

If \(\det J\Phi=1\), then \(\det K=1\), so

\[
K\in{\rm SL}_2(\mathbb C)=E_2(\mathbb C)\subset E_2(S).
\]

Consequently \(J\Phi\in E_2(S)\).

Returning to the integrated map, if \((P,Q)\) were a polynomial automorphism, its determinant-one Jacobian \(M\) would belong to \(E_2(S)\), contrary to the hypothesis. Therefore \((P,Q)\) is a Keller nonautomorphism. This proves the bridge. \(\square\)

## 4. Frozen Broughton/Cohn completion family

Apply the ring automorphism

\[
\theta(x)=x,\qquad\theta(y)=2y
\]

to \(C\). This gives

\[
C_B=
\begin{pmatrix}
1+2xy&x^2\\
-4y^2&1-2xy
\end{pmatrix}.
\]

The automorphism \(\theta\) and its inverse send elementary generators to elementary generators. Therefore

\[
C_B\notin E_2(\mathbb C[x,y]).
\]

Its first row is closed:

\[
(1+2xy)_y=(x^2)_x=2x,
\]

and it is exactly \(dP\) for \(P=x+x^2y\). Its second-row curl, with the convention

\[
\operatorname{curl}(r,s)=r_y-s_x,
\]

is

\[
(-4y^2)_y-(1-2xy)_x=-8y+2y=-6y.
\]

The first row \((a,b)=(1+2xy,x^2)\) is unimodular, with the explicit identity

\[
(1-2xy)a+4y^2b=1.
\]

Let \(M'\) be any determinant-one matrix with this same first row. Subtracting the second row of \(C_B\), write the difference as \((p,q)\). Equality of determinants gives

\[
aq-bp=0.
\]

Since \(a,b\) are coprime, \(p=ha\) and \(q=hb\) for a unique polynomial \(h\). Thus every determinant-one completion of the fixed row is

\[
M(h)=L(h)C_B.
\]

This is not merely an ansatz within the fixed-row problem; it is the complete fixed-row completion family. It remains non-elementary: if \(M(h)\) were elementary, then

\[
L(-h)M(h)=C_B
\]

would be elementary.

The second row of \(M(h)\) is

\[
(-4y^2+h(1+2xy),\;1-2xy+hx^2).
\]

Because the first row is closed, its curl is

\[
-6y+(1+2xy)h_y-x^2h_x.
\]

Define

\[
\delta=(1+2xy)\partial_y-x^2\partial_x.
\]

The exact-coframe condition in the complete fixed-row family is therefore the single linear equation

\[
\delta h=6y.
\]

## 5. Frozen bounded tangent replay

The preregistered support was

\[
H_2=\operatorname{span}_{\mathbb Q}
\{y^2,xy^3,x^2y^4\}.
\]

Exact replay gives

\[
\begin{aligned}
\delta(y^2)&=2y+4xy^2,\\
\delta(xy^3)&=3xy^2+5x^2y^3,\\
\delta(x^2y^4)&=4x^2y^3+6x^3y^4.
\end{aligned}
\]

In the output basis

\[
(y,xy^2,x^2y^3,x^3y^4)
\]

the linearized map has matrix

\[
A=
\begin{pmatrix}
2&0&0\\
4&3&0\\
0&5&4\\
0&0&6
\end{pmatrix},
\qquad
t=
\begin{pmatrix}6\\0\\0\\0\end{pmatrix}.
\]

The exact ranks are

\[
\operatorname{rank}A=3,\qquad
\operatorname{rank}[A\mid t]=4.
\]

Thus \(6y\notin\delta(H_2)\): **EMPTY-TANGENT**.

Equivalently, coefficient comparison gives

\[
\begin{aligned}
e_0&=2c_0-6,\\
e_1&=4c_0+3c_1,\\
e_2&=5c_1+4c_2,\\
e_3&=6c_2.
\end{aligned}
\]

The explicit unit-ideal certificate is

\[
-\frac16e_0+\frac1{12}e_1-\frac1{20}e_2+\frac1{30}e_3=1.
\]

The family is already affine-linear in \(h\), so its tangent equations are its exact equations. The preregistered tangent gate therefore forbade a Gröbner or other elimination run. None was run.

## 6. Complete one-shear no-go

The bounded failure is the first three steps of an exact infinite-chain obstruction.

Give a monomial the integer weight

\[
w(x^iy^j)=i-j.
\]

For every monomial,

\[
\delta(x^iy^j)
=j x^iy^{j-1}+(2j-i)x^{i+1}y^j.
\]

Both terms have weight \(w+1\). Since \(6y\) has weight \(-1\), the weight-\(-1\) component of \(\delta h\) comes only from the weight-\(-2\) component of \(h\). If a polynomial solution existed, write that finite component as

\[
h_{-2}=\sum_{n=0}^{N}c_nx^ny^{n+2}.
\]

The coefficient of \(y\) in \(\delta h_{-2}\) gives

\[
2c_0=6,\qquad c_0=3.
\]

For \(n\ge1\), the coefficient of \(x^ny^{n+1}\) gives

\[
(n+2)c_n+(n+3)c_{n-1}=0.
\]

Hence

\[
c_n=(-1)^n(n+3).
\]

In particular every \(c_n\) is nonzero. The last term in a finite truncation contributes the uncancelled terminal monomial

\[
(N+4)c_Nx^{N+1}y^{N+2}.
\]

This is nonzero in characteristic zero, a contradiction. Therefore

\[
\delta h=6y
\]

has no polynomial solution in \(\mathbb C[x,y]\).

The replay also verifies the rational control

\[
h_{\rm rat}
=\frac{y^2(3+2xy)}{(1+xy)^2},
\qquad
\delta h_{\rm rat}=6y.
\]

Its expansion in \(z=xy\) is

\[
y^2\sum_{n\ge0}(-1)^n(n+3)z^n,
\]

exactly the nonterminating recurrence above. The pole or infinite support is the obstruction; the rational solution is not a survivor.

### Scoped theorem

There is no polynomial \(h\) for which \(L(h)C_B\) has both rows closed. Equivalently, the exact Broughton row

\[
d(x+x^2y)=(1+2xy,x^2)
\]

has no determinant-one closed polynomial completion in the Cohn non-\(E_2\) lineage obtained by fixing that row.

This closes the complete one-left-shear, fixed-first-row family. It does not close \(E_2 C E_2\) with a changed first row.

## 7. Survivor and stop audit

There was no bounded or unbounded polynomial survivor. Therefore:

- the first row was integrated and replayed exactly as \(P=x+x^2y\);
- no second polynomial potential \(Q\) exists in the frozen family;
- no full Keller pair was produced;
- no collision or injectivity test was applicable;
- no elimination was licensed;
- no degree, support, elementary-word length, or family was widened.

The stop was triggered first by **EMPTY-TANGENT** in the frozen bounded slice. The global recurrence, explicitly preregistered for this same one-shear family, then supplied the stronger **ONE-SHEAR-NO-POLYNOMIAL** certificate.

Post-freeze coordinator observations about the family \(x+x^m y\) and length-two left elementary words were not computed, source-checked, or used in this verdict. They remain an unverified queue for a separately frozen micro-gate.

## 8. Artifact record

| Artifact | SHA-256 |
|---|---|
| cases/exact_coframe_gate_20260824/00_preregistration.md | d0d629c6231f814d2cd3ac0fdf76baef4240cbb6271b2271ae9a9f95e6d54658 |
| cases/exact_coframe_gate_20260824/01_source_audit.md | 52e39a480dfd52f1d95d8daf33a9f62695c3fe5f3635319005bc240031b27ce8 |
| cases/exact_coframe_gate_20260824/replay_exact.py | e02ae9da94b01ac337fabd65b8733557503963fa19ba9963548b6e2059a30920 |
| cases/exact_coframe_gate_20260824/replay_exact.txt | 8bce91b8495a4b163640af0b5936837758ed0fb9660385cf37e73667745bc751 |

The report hash is recorded after this file is frozen.

## 9. Final interpretation

The exact-coframe mechanism survives its theorem gate: a closed, determinant-one, literally non-elementary polynomial matrix would be a direct characteristic-zero Keller nonautomorphism. This conceptual equivalence is not new: Wright's weak Jacobian theorem supplies the reverse implication and establishes the full exact-coframe \(E_2\)/automorphism dichotomy.

The separate, gate-specific result is that the first high-value Cohn deformation does not survive its orbit gate. Scaling the Cohn witness exposes a connection to Broughton's critical-point-free noncoordinate polynomial, but the missing second primitive is measured by a nontrivial cokernel class of its Hamiltonian derivation. The required correction exists rationally and formally, while its weight recurrence cannot terminate polynomially.

That is decisive negative information about the frozen family, not evidence against exact coframes in larger elementary double orbits. Root E stops here under its preregistration.

Frozen. No claim was promoted and no shared ledger was edited.
