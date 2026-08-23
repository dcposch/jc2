# End\((A_1)\) disproof / Zheglov DC(1) audit

Date: 2026-08-23  
Lane: `APPROACHES.md` row 14  
Inputs audited: `ZHEGLOV-SCOPE.md`, `ZHEGLOV-LTEST.md`, `DC2-PROGRAM.md`,
`RESIDUE.md`, `CERT-UPGRADE.md`, and `zheglov/v5src/DC5.tex`.

## Verdict up front

1. Over a characteristic-zero field,
   \[
   \mathrm{JC}(2)\Longrightarrow \mathrm{DC}(1).
   \]
   Therefore an actual pair \(P,Q\in A_1\) with \([Q,P]=1\) and
   \(K\langle P,Q\rangle\subsetneq A_1\) refutes JC2. Merely finding a gap in
   Zheglov's proof does not.

2. The deferred T2 calculation has now been replayed at its algebraic core.
   **T2-local verdict: PASS.** The formulas for \(\gamma _1,\gamma _2\), the
   \(\Gamma _1\)-coefficient, all three printed coefficients \(A,B,C\), the
   tail recursion, the orbit average, and the final \(N\)-dependent
   distinguished coefficient agree. I found no sign or offset error in Steps
   4--7. I also give a short rigorous proof of \(A\ne0\), replacing the paper's
   compressed explanation.

3. This is not an end-to-end validation of the claimed DC(1) proof. The
   N-independence lemma, the non-coprime string/spectral correspondence, the
   existence of the specially chosen all-\(p\) head-chopping sequence, and the
   imported normal-form calculus remain outside this replay. Zheglov v5 is
   **not refuted, but not certified**.

4. The residue-A *template* does not transfer to \(A_1\): the normal symbol of
   a Weyl pair satisfies a star-commutator equation, not a commutative Keller
   equation. Its Newton/Puiseux geometry therefore cannot simply be reused.
   The *architecture* does transfer: contraction order is triangular, the
   leading linear block is the same Hamiltonian/Koszul differential, and its
   residue/cokernel functionals become compatibility equations with explicit
   quantum source terms.

5. The exact/modular certificate machinery transfers even more directly.
   There is a finite, exact bounded-degree counterexample scheme using
   Bavula's inverse-degree bound and a dual linear functional. A
   characteristic-zero point of that scheme is already a certified
   non-surjective Weyl endomorphism; an exact Nullstellensatz certificate for
   its emptiness proves DC(1) through that degree. This is a genuinely new
   attack inside this repository, although no claim of literature novelty is
   made. It is bounded, not global: no degree ceiling is known.

---

## 1. The reduction and the required counterexample

Let
\[
A_1(K)=K\langle x,\partial\rangle/([\partial,x]-1),
\qquad \operatorname{char}K=0.
\]
An endomorphism \(\varphi\) is determined by
\[
P=\varphi(x),\qquad Q=\varphi(\partial),\qquad [Q,P]=1.
\]
Since \(A_1\) is simple, every unital endomorphism is injective. Thus a DC(1)
counterexample is not a kernel phenomenon; it is an injective but
non-surjective endomorphism. Equivalently,
\[
[Q,P]=1,\qquad K\langle P,Q\rangle\ne A_1.
\]
In concrete terms, at least one of \(x,\partial\) is not a noncommutative
polynomial in \(P,Q\).

Bavula and Belov-Kanel--Kontsevich prove
\(\mathrm{JC}(2n)\Rightarrow\mathrm{DC}(n)\); setting \(n=1\) gives the
claimed reduction. See
[Bavula](https://arxiv.org/abs/math/0512250) and
[Belov-Kanel--Kontsevich](https://arxiv.org/abs/math/0512171). Hence
\[
\neg\mathrm{DC}(1)\Longrightarrow\neg\mathrm{JC}(2).
\]

There are three different possible outcomes, and they must not be conflated.

- A fatal error in Zheglov v5 would only restore DC(1) to open status.
- A modular or truncated Weyl pair is not a counterexample.
- A genuine counterexample must be a finite pair \(P,Q\in A_1(K)\), satisfy
  \([Q,P]=1\) exactly in characteristic zero, and carry a proof of
  non-surjectivity.

The last requirement is where the bounded inverse-membership certificate in
Section 4 changes the computational problem.

---

## 2. Deferred T2: symbolic replay of v5 Steps 4--7

### 2.1 Local contract and notation

This replay takes as input the two homogeneous-component shapes asserted at
`DC5.tex:3222-3226` and checks every subsequent algebraic transformation. Put
\[
M=\widetilde M_{I-1},\qquad D_N=dN+l,
\qquad p_N=nD_N,
\]
and
\[
q_N=N(M+1)+\frac{Ml}{d}+1.
\]
The needed input components are
\[
(\Phi_{N,1}(P_n))_{p_N-N-1}
 =(dn\Gamma _1+a)\partial^{p_N-N-1},
\]
\[
(Q_{N,I})_{q_N-N-1}
 =\epsilon_I((M+1)\Gamma _1+b)\partial^{q_N-N-1}.
\]
The coefficients \(a,b\) are independent of \(N\). The gaps above these
components are also part of the local contract.

The elementary Schur factor is
\[
\bar S_{-N-1}=1+(\gamma _2\Gamma _2+\gamma _1\Gamma _1+u)
\int^{N+1}.
\]
The replay uses only
\[
D^r\Gamma _1=(\Gamma _1+r)D^r,
\qquad \Gamma _2=\Gamma _1^2,
\]
and the cyclic shift on the vector coefficient \(u\). Because its period is
\(p_N\), the \(u\)-term cancels when normalizing the leading
\(\partial^{p_N}\) term.

### 2.2 Step 4: \(\gamma _1,\gamma _2\) and \(A,B,C\)

The coefficient to cancel in the conjugated \(P\) is
\[
\gamma _2\big((\Gamma _1+p_N)^2-\Gamma _1^2\big)
 +\gamma _1p_N+dn\Gamma _1+a.
\]
Equating its \(\Gamma _1\) and constant parts to zero gives
\[
\gamma _2=-\frac{dn}{2p_N}
 =-\frac{d}{2(dN+l)}
 =-\frac{d_2}{2(d_2N+l_2)},
\]
\[
\gamma _1=-\frac{a}{p_N}+\frac{dn}{2}.
\]
These are exactly `DC5.tex:3237`.

For \(Q_{N,I}\), the relevant coefficient after conjugation is
\[
\begin{aligned}
\epsilon_I\{&\gamma _2((\Gamma _1+q_N)^2-\Gamma _1^2)
 +\gamma _1q_N+(\sigma^{-q_N}u-u)\\
& +(M+1)\Gamma _1+b\}.
\end{aligned}
\]
The elementary identity
\[
dq_N=(M+1)(dN+l)+(d-l)
\]
gives the printed \(\Gamma _1\)-coefficient
\[
2\gamma _2q_N+(M+1)=-\frac{d-l}{dN+l}.
\]

The constant rational term satisfies the exact identity
\[
(dN+l)(\gamma _2q_N^2+\gamma _1q_N)=AN^2+BN+C,
\]
where
\[
A=\frac d2(M+1)(dn-M-1),
\]
\[
B=\frac12\left(
-\frac{2(M+1)(a+lMn)}n+d^2n
+d(2M(ln-1)+ln-2)\right),
\]
\[
C=-\frac{(d+lM)(2a+n(-dln+d+lM))}{2dn}.
\]
I independently expanded both sides over the rational function field and the
difference is identically zero. Thus all of `DC5.tex:3244-3254` replays.

### 2.3 The paper's compressed \(A\ne0\) claim can be repaired

Only the factor \(dn-M-1\) is non-obvious. Let
\(r=\operatorname{ord}(Q_{I-1})\) and let \(M_{I-1}\) retain the paper's
un-tilded meaning. The preceding induction gives
\[
M=rnd-M_{I-1},\qquad r\ge dm,\qquad M_{I-1}<d(n+m).
\]
If \(M+1=dn\), then
\[
M_{I-1}=dn(r-1)+1\ge dn(dm-1)+1.
\]
Since \(1<l<d\), one has \(d\ge3\), and for positive \(m,n\),
\[
dn(dm-1)+1-d(n+m)
=d(dnm-2n-m)+1\ge1.
\]
This contradicts \(M_{I-1}<d(n+m)\). Also \(M+1=\operatorname{ord}(Q_I)>0\).
Consequently \(A\ne0\). This is stronger and clearer than the one-line
explanation at `DC5.tex:3256`.

### 2.4 Steps 5--6: body-tail recursion

Write \(p=dn\), \(\widetilde p=p_N=n(dN+l)\), and
\[
\widetilde d=\operatorname{SeqGCD}_{I-1}
(\Phi_{N,1}(P_n),\Phi_{N,1}(Q_n)).
\]
The base tail in vector form is
\[
\left(-\frac{\Gamma _1}{\widetilde p}
 +(0,1/\widetilde p,\ldots,(\widetilde p-1)/\widetilde p)\right)
\widetilde D^{-\widetilde p}.
\]

At one head-chopping step, the part linear in the tail is the sum of its
\(p\) possible placements among the leading body factors. Commuting the body
powers to the left gives
\[
\sum_{k=0}^{p-1}\left(
-\frac{\Gamma _1+k\operatorname{ord}(Q_{N,i})}{\widetilde p}
+\sigma^{-k\operatorname{ord}(Q_{N,i})}(v_i)\right).
\]
Therefore the scalar shift accumulates
\((p-1)\operatorname{ord}(Q_{N,i})/(2\widetilde p)\), while the vector part
is replaced by its orbit average. Induction yields the printed expression
at `DC5.tex:3343-3349`; the prefactor is
\[
K_I=p^I\prod_{j=1}^{I-1}\epsilon_j^{p-1}.
\]
Matching the already verified \(\Gamma _1\)-coefficient forces
\[
K_I=\epsilon_I(dn-ln)=\epsilon_In(d-l),
\]
exactly as at `DC5.tex:3352`.

Let
\[
L=\frac{\widetilde p}{\widetilde d}=n\widetilde d_1.
\]
The final orbit average is \(\widetilde d\)-periodic and, for
\(0\le i<\widetilde d\), has component
\[
a_i=\frac{L-1}{2L}+\frac{i}{\widetilde p}.
\]
This is exactly the arithmetic mean of
\(i,i+\widetilde d,\ldots,i+(L-1)\widetilde d\), divided by
\(\widetilde p\). The claimed tail and the body obtained by subtracting it
therefore have the printed signs.

### 2.5 Step 7: the final average and \(N\)-dependence

The elementary invariant-conjugation equation is a cyclic coboundary equation
\[
q-s+\sigma^rs=\text{invariant part}.
\]
Its invariant part is the orbit average of \(q\). At the final sequential-GCD
drop to one, this is the average of all vector components. Thus
\[
\operatorname{avg}(\sigma^{-q_N}u-u)=0
\]
and
\[
\begin{aligned}
\operatorname{avg}(\widetilde u)
 &=\frac1{\widetilde d}\sum_{i=0}^{\widetilde d-1}a_i\\
 &=\frac{L-1}{2L}+\frac{\widetilde d-1}{2\widetilde p}
 =\frac12-\frac1{2\widetilde p}
 =\frac12-\frac1{2n(dN+l)}.
\end{aligned}
\]
Substitution gives
\[
\begin{aligned}
c_{N,I;r(I)}=\epsilon_I\bigg[&(-dn+ln)\left(
\frac12-\frac1{2n(dN+l)}
-\Big(\sum_{i=0}^{I-1}\operatorname{ord}Q_i\Big)\frac{p-1}{2p}
\right)\\
&+\frac{AN^2+BN+C}{dN+l}+b\bigg],
\end{aligned}
\]
which is `DC5.tex:3383`. Since \(A\ne0\), this rational function grows as
\((A/d)N\) and is nonconstant on the infinite allowed arithmetic progression
of \(N\)'s.

### 2.6 T2 verdict and remaining proof obligations

**T2-local: DONE, PASS.** Within the stated local contract, Steps 4--7 are
internally consistent. No Zheglov counterexample or fatal endgame arithmetic
error was found.

This pass has sharply limited scope:

- **CONJECTURE / unclosed proof obligation Z-SEQ.** At `DC5.tex:3148` the
  paper chooses a head-chopping sequence with every \(n_i=p=dn\). The main
  induction initially defines the minimal exponent
  \(n_i=p/\gcd(p,\operatorname{ord}Q_i)\), although it notes non-uniqueness
  and explicitly permits \(n_i=p\) in the last-step calculation. It is very
  plausible that every step can be replaced by the corresponding multiple,
  but v5 does not supply a clean lemma proving that the all-\(p\) sequence
  preserves every order, tail, and termination property used here.

- **CONJECTURE / unclosed proof obligation Z-BT.** The unique relevant
  one-tail term and its body-tail provenance are argued informally at
  `DC5.tex:3277-3303`. The highest one-tail recursion replays, but a complete
  operator-level certification would require the T0 HCP/vector-form kernel
  and all imported normal-form identities, not merely the displayed local
  formulas.

- **CONJECTURE / unclosed proof obligation Z-AVG.** The final averaging rule
  follows from the cyclic linear system in the proof of
  `L:invariant_conjugation`; this local consequence checks. What is not
  independently certified is that the particular auxiliary conjugator
  transported through the non-coprime string/commuting correspondence is
  exactly the one to which that final sequential-GCD averaging applies.

- `L:distinguished coefficients` (`DC5.tex:3168-3210`) is the other jaw of
  the contradiction and was not part of this Steps-4--7 replay. Its special
  \(M_{I-1}=d_2=2\) case remains a separate T4 audit.

Accordingly, this computation modestly de-risks R1 but does not justify citing
DC(1) as settled.

---

## 3. What transfers from residue-A to the Weyl algebra?

### 3.1 Exact normal-symbol calculus

Write a Weyl element in normal order and identify it with a commutative
polynomial in \(x,\xi\):
\[
P=\sum p_{ij}x^i\partial^j\longleftrightarrow
p(x,\xi)=\sum p_{ij}x^i\xi^j.
\]
Then the exact normal symbol of the product is
\[
q\star p
=\sum_{s\ge0}\frac1{s!}
(\partial_\xi^s q)(\partial_x^s p),
\]
and hence
\[
\operatorname{sym}([Q,P])
=\sum_{s\ge1}\frac1{s!}\left(
\partial_\xi^s q\,\partial_x^s p
-\partial_\xi^s p\,\partial_x^s q\right).
\tag{W}
\]
This is finite for polynomials and has integer structure constants when
expanded in monomial coefficients. The \(s=1\) term is the Poisson bracket.
Every \(s\)-contraction lowers the exponent sum by \(s(1,1)\).

For a weight \((\rho,\sigma)\) with \(\rho+\sigma>0\), contraction order is
strictly triangular: the \(s\ge2\) terms land below the \(s=1\) term. Weyl
*symmetric* symbols package (W) as the Moyal bracket and retain only odd
contraction orders. That is conceptually cleaner, but normal symbols are
better for modular work because they keep integral coefficients and avoid
powers of \(2\) and factorial denominators.

### 3.2 The precise transfer

The reusable relationship is:

| residue/depth system | Weyl analogue | transfer status |
|---|---|---|
| coefficient equations for \(\{f,g\}=1\) | coefficient equations for \([Q,P]_\star=1\) | exact, with higher-contraction source terms |
| depth/column order | weight order positive on \((1,1)\) | exact triangular filtration |
| linear block \(\operatorname{ad}_{xA}\) | leading Hamiltonian block of \(s=1\) | same associated-graded operator |
| cokernel moment/residue \(\mu\) | compatibility functional on each quantum block | exact after adding the quantum source |
| modular ideal and cofactor certificate | modular Weyl coefficient ideal and cofactor certificate | direct transfer |
| Puiseux branch, boundary divisor, topological degree | no literal Weyl counterpart | does not transfer |
| residue-A cell \((r,\nu,l)=(2,3,1)\) | no canonical \(A_1\) candidate | does not transfer |

In particular, suppose one quantum weight block has unknown correction \(E\)
and leading symbol \(xA(y)\). The coefficient of the current level has the
form
\[
L(E)=G_{\mathrm{classical}}+G_{\mathrm{quantum}},
\qquad
L=A\frac d{dy}-(k+1)A'.
\]
The operator \(L\) and its residue cokernel are the same as in `RESIDUE.md`;
the right side now includes already-known contributions from \(s\ge2\)
contractions. Thus
\[
\mu(G_{\mathrm{classical}}+G_{\mathrm{quantum}})=0
\]
is a valid quantum compatibility equation. The old residue does not vanish
unchanged: it acquires a computable quantum anomaly.

This is the useful transfer. It says that the repository's triangular
elimination and certificate-mining methods can operate on Weyl blocks, and
that the small left kernels should still have residue descriptions.

### 3.3 What emphatically does not transfer

For a Weyl endomorphism, equation (W) says
\[
\{q,p\}=1-\sum_{s\ge2}(\text{higher contractions}).
\]
Therefore \((p,q)\) is generally not a commutative Keller pair. Replacing a
residue-A formal pair by normally ordered operators does not preserve its
Jacobian equation and almost never produces \([Q,P]=1\). The residue-A
Newton polygon, its Puiseux places, and its depth-25 survivor cannot be treated
as an \(A_1\) candidate.

**CONJECTURE (Weyl-residue sparsity).** On GGV subrectangular Weyl shapes, the
quantum compatibility functionals produced above remain uniformly
low-support after head chopping, so modular cofactors reconstruct to a finite
family of residue identities. This is plausible from the one-dimensional
contraction cone and from Zheglov's own final averaging functional, but it is
not proved by the residue-A calculations.

---

## 4. A new exact bounded-degree counterexample/certificate scheme

This is the most promising transfer found in the audit.

### 4.1 Finite inverse membership in \(A_1\)

Let \(F_DA_1\) be the Bernstein filtration and
\[
\mathcal B_D=\{x^i\partial^j:i+j\le D\},
\qquad M_D=\dim F_DA_1=\binom{D+2}{2}.
\]
Let \(\varphi\) have degree at most \(D\), with images \(P,Q\). Bavula's
inverse-degree theorem specializes in rank one to
\[
\deg(\varphi^{-1})\le\deg(\varphi)
\]
whenever \(\varphi\) is an automorphism.

Define the finite image space
\[
W_D(P,Q)=\operatorname{span}_K\{P^iQ^j:i+j\le D\}
\subset F_{D^2}A_1.
\]
Then
\[
\boxed{\quad
\varphi\text{ is an automorphism}
\iff x,\partial\in W_D(P,Q).
\quad}
\tag{I}
\]
The forward implication is the inverse-degree bound. Conversely, if both
generators lie in the image, \(\varphi\) is surjective and hence an
automorphism.

This converts non-surjectivity from an unbounded word problem into finite
linear nonmembership at every fixed \(D\).

### 4.2 Dual-functional counterexample scheme

Introduce coefficient variables for
\(P,Q\in F_DA_1\) and a linear functional
\(\lambda\in(F_{D^2}A_1)^*\). Consider
\[
[Q,P]=1,
\tag{C1}
\]
\[
\lambda(P^iQ^j)=0\quad(i+j\le D),
\tag{C2}
\]
\[
\lambda(x)=1.
\tag{C3x}
\]
There is a second branch with \(\lambda(\partial)=1\). By elementary linear
duality, (C2)--(C3x) hold exactly when \(x\notin W_D(P,Q)\).

Consequently:

**Proposition.** A characteristic-zero point of (C1)--(C3x), or of the
\(\partial\)-branch, is a non-surjective endomorphism of \(A_1\), hence a
counterexample to DC(1) and JC2. Conversely, every DC(1) counterexample of
degree at most \(D\) gives a point on one of these two schemes.

The equations are ordinary commutative polynomial equations over
\(\mathbb Z\): normal-ordered Weyl multiplication contributes only binomial
and falling-factorial structure constants. No p-curvature theorem is needed.
The functional \(\lambda\) is itself a concise proof of nonmembership.

Fourier symmetry exchanges the two branches, so an existence search may work
with the \(x\)-branch up to that symmetry. For a literal exhaustive statement
without quotienting by Fourier, retain both.

The degree-one calibration closes by inspection. If
\[
P=a_0+a_1x+a_2\partial,\qquad
Q=b_0+b_1x+b_2\partial,
\]
then \([Q,P]=1\) says \(a_1b_2-a_2b_1=1\). Relative to the basis
\((1,x,\partial)\), the three columns \((1,P,Q)\) have determinant one.
Hence \(W_1=F_1A_1\), both dual branches are empty, and the criterion recovers
the affine automorphism case with no classification input.

### 4.3 Raw sizes

Before affine/triangular normalization, one dual branch has
\[
2M_D+\dim F_{D^2}A_1
\]
variables. An upper count for its equations is
\(\dim F_{2D-2}A_1+M_D+1\).

| \(D\) | \(M_D\) | \(\dim F_{D^2}\) | raw variables | raw equations |
|---:|---:|---:|---:|---:|
| 2 | 6 | 15 | 27 | 13 |
| 3 | 10 | 55 | 75 | 26 |
| 4 | 15 | 153 | 183 | 44 |
| 5 | 21 | 351 | 393 | 67 |

The apparent underdetermination is misleading: for an automorphism, (C2)
forces \(\lambda(x)=0\), so the fiber in \(\lambda\) is empty. Still, raw F4
will scale poorly. The important reductions are:

- eliminate \(\lambda\) as a sparse linear block, or work with the equivalent
  augmented-rank minors;
- quotient translations and linear symplectic automorphisms;
- impose exact top degree and a normalized GGV leading shape;
- use the contraction/depth filtration before a global Gröbner basis;
- mine a sparse dual functional rather than retaining every coordinate of
  \(F_{D^2}^*\).

### 4.4 Why this makes modular certificates genuinely relevant

There are now two proof-bearing endpoints.

1. **Counterexample endpoint.** Reconstruct an exact characteristic-zero
   solution \((P,Q,\lambda)\). Exact normal-order verification of (C1)--(C3)
   simultaneously proves the CCR and non-surjectivity. There is no subsequent
   geometric or algebraization bridge.

2. **Exclusion endpoint.** Prove the dual scheme empty on a normalized degree
   or Newton-shape chart. An exact identity
   \(1=\sum h_if_i\) proves that chart contains no counterexample. Stable
   small cofactors at several primes can be CRT/rationally reconstructed and
   checked over \(\mathbb Q\), exactly as in `CERT-UPGRADE.md`.

Ordinary modular `[1]` outputs at finitely many primes remain evidence only.
A single bad prime can kill a characteristic-zero point, and prime-dependent
normal forms defeat naive CRT. The final object must be an exact reconstructed
cofactor identity or an exact characteristic-zero point.

For discovery, use primes larger than all active contraction orders (a safe
simple choice is \(p>D^2\)) and avoid pivot divisors. Small characteristic is
especially deceptive: for example
\[
P=x-x^p,\qquad Q=\partial
\]
satisfies \([Q,P]=1\) in characteristic \(p\) for Frobenius reasons and does
not lift to the same characteristic-zero CCR pair.

### 4.5 This is different from the Tsuchimoto center route

In characteristic \(p\), \(A_1\) has the large center
\(K[x^p,\partial^p]\), and a reduced Weyl endomorphism induces a Poisson map
on that center. This is the mechanism behind
\(\mathrm{JC}(2)\Rightarrow\mathrm{DC}(1)\). Using JC2 to prove that the
center map is invertible is circular for the present task.

The dual-functional scheme instead reduces only the finite integer
coefficient equations and lifts/checks the answer back in characteristic
zero. It does not infer characteristic-zero surjectivity from the center of
\(A_{1,\mathbb F_p}\). That distinction is why the certificate method is a
new usable attack rather than a restatement of Bavula/Tsuchimoto.

---

## 5. Feasibility and the right first experiment

### 5.1 Feasibility assessment

- **Direct exact/modular coefficient method: feasible at low degree.** The
  \(D=2\) and \(D=3\) dual schemes are small enough after eliminating the
  linear \(\lambda\)-block and normalizing affine automorphisms. They should
  be calibrated against known automorphism classifications.

- **Residue/cokernel acceleration: plausible and worth testing.** The
  associated-graded block and its residue functional genuinely survive. The
  question is whether quantum source terms preserve the sparse certificates
  seen in `RESIDUE.md`.

- **Unstructured \(D\ge4\): likely expensive.** The ambient inverse-test space
  grows as \(D^4/2\), before the CCR geometry is stratified.

- **Global DC(1): not presently feasible by this alone.** There is no bound on
  \(D\), no finite list of GGV shapes, and no uniform sparse-certificate
  theorem. A degree-by-degree census cannot refute DC(1) without one of those
  bridges.

**CONJECTURE (uniform certificate bridge).** After GGV subrectangular
normalization, the dual nonmembership scheme admits a contraction-ordered
elimination whose terminal cofactors have support bounded by the essential
GCD data rather than by \(D^2\). This would convert bounded computations into
a real DC(1) program. No evidence for uniformity exists yet; the first pilots
must measure support growth rather than assume it.

### 5.2 Pre-registered pilot

1. Implement the integral normal-symbol kernel (W) and verify it against
   direct normal ordering on random \(P,Q\) through \(D=4\).
2. Build the \(x\)-dual systems at \(D=2,3\); eliminate \(\lambda\) by exact
   linear algebra before F4.
3. Normalize translations and the affine \(SL_2\) action. Retain emission
   hashes and exact back-substitution to the unnormalized equations.
4. Run three good primes, with one independent implementation of the Weyl
   coefficient emitter. Treat modular nonempty points as discovery data only.
5. If empty, request modular cofactors, compare supports, reconstruct over
   \(\mathbb Q\), and independently verify \(1=\sum h_if_i\).
6. If nonempty, rationally reconstruct \(P,Q,\lambda\) and verify (C1)--(C3)
   exactly. Failure to reconstruct is not a counterexample.
7. Controls:
   - every affine and triangular automorphism must make the full-\(D\) dual
     system inconsistent;
   - for \(x\mapsto x,\ \partial\mapsto\partial+x^D\), truncating the inverse
     test to \(D-1\) must make the \(\partial\)-dual system nonempty, while the
     correct bound \(D\) makes it empty;
   - a small prime \(p\le D\) should be retained as a labeled Frobenius bad
     control, never as proof evidence.
8. Only after the low-degree engine passes, impose one GGV subrectangular
   top-face chart and compare its terminal left kernel with the residue
   functional predicted in Section 3.

Kill/continue rule: continue beyond \(D=3\) only if either an exact candidate
survives or modular cofactors show small, support-stable motifs. A large
prime-dependent Gröbner basis with no stable certificate is a stop signal.

---

## 6. Bottom line

The defensive Zheglov audit did not produce a disproof. T1 remains 640/640
passed, and the previously deferred local T2 calculation now also passes.
The honest residual audit burden lies in the theorem-chain interfaces, not in
the printed \(A,B,C\) arithmetic.

The positive result of this lane is methodological. Weyl contraction calculus
does preserve the triangular/cokernel skeleton of the residue machinery, but
not the residue-A geometric template. More importantly, Bavula's rank-one
inverse-degree bound turns non-surjectivity into a finite dual linear
certificate at each degree. That makes the repository's modular cofactor
pipeline directly applicable to \(A_1\) counterexample strata, with exact
proof endpoints on both the nonempty and empty sides.

This is a serious bounded attack, not yet a global one. Its missing theorem is
uniformity: a degree ceiling, a finite shape reduction, or a support-stable
certificate law. Until one of those appears, the correct claim is
"new certificate engine for bounded End\((A_1)\) disproof searches," not
"a reduction of DC(1) to a finite computation."
