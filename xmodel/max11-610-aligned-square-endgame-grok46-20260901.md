# max11 `(6,10)` scale-two aligned-square chamber: structural endgame

**Verdict: PARTIAL**

There is no referee-checkable `False` for the aligned-square chamber from
committed input. The landed packet
`normalized610ScaleTwo_alignedSquare_mixedPairReduction` is a two-limb
hypersurface against the inhomogeneous Keller row
\(p_0'(a)\,q_1(a)-p_1(a)\,q_0'(a)=j\neq 0\). One child on \(w_1(a)=0\)
is already empty (410-style collision \(p_1(a)=q_1(a)=0\)). The three
surviving residuals do not force both Keller cross-products to vanish.

The linear-root bounded tower does **not** instantiate on this face:
the landed source wrapper requires the Backwire peel \(p_5=h_0^5 w_1\)
and \(N=C(\lambda)h_0^9\), and the linear-root closure uses
\(\lambda\neq 0\). On the aligned face \(N=0\) and \(p_5=h_0^4 w_1\).
Substituting that peel into the committed depressed numerators
\(Abar,Bbar,Cbar\) produces strictly worse poles than Backwire
(\(A\) has pole \(2\) on the live \(\mu=0\) limb). A new wrapper and a
new vanishing order would be required; filling either from the
linear-root numbers \(75/69/6\) is forbidden.

A 68-style exact identity in \(k[X]\) is not available: the unreduced
weights \(5/30/65/70\) are tautological at \(a\) on the square jet
\(p_5(a)=p_4(a)=0\), and there is no committed \(\deg_X\) dictionary on
the lower source coefficients.

The exact missing objects are named in §5. No exit-price is claimed.

---

## 0. Sources and verification status

Work over a field \(k\) of characteristic zero, on the normalized
scale-two \((6,10)\) **aligned** face \(N=0\), square chamber
\(H=h_0^2\). Clone used for reading:
`https://github.com/dcposch/jc2-lean` at `16eed1b`
(`origin/master` as of this run; commit message “Land the 610
aligned-square mixed (p1,q1) pair reduction”). The nested worktree
`jc2-lean/` is sandbox-blocked.

### 0.1 What was read on `origin/master` (used below)

| File / theorem | Used for |
|---|---|
| `Grok610AlignedSquareMixedPairScratch.lean`, `normalized610ScaleTwo_alignedSquare_mixedPairReduction` | frozen two-limb packet; peel ladder; Keller row at \(a\); mixed ninth/tenth heads |
| same file, `alignedSquareMixed_kellerCollision610` | \(p_1(a)=q_1(a)=0\Rightarrow 0=j\) |
| same file, `alignedSquareW1Zero_e1_a2_zero610`, `..._complementResidual610` | \(w_1=0\) quadratic collapse and the live complement |
| same file, `alignedSquareMuZeroMixed_comboResidual610`, `..._vZero_yZero610`, `...DeepMixed_tenthHeadKill610` | \(\mu=0\) cube/combo and the \(v(a)=0\) child |
| `Grok610DegreeZeroMixedArmClosureScratch.lean`, `degreeZeroFace610_linearRoot` | linear-root chamber **CLOSED** by pole-six exhaustion |
| `Grok610PoleCeilingLemmaScratch.lean` | \(h_0^M\mid A_0\) and \(\deg A_0<M\Rightarrow\rho=0\); then \(\rho'=Cj/h_0\) is impossible |
| `Grok610DegreeZeroOrder75CeilingScratch.lean` | clearing \(h_0^6\), jet-quotient \(h\)-degree \(\le 6\), ceiling at order \(75\) |
| `Grok610DegreeZeroSourceWrapperScratch.lean`, `degreeZeroPostCollapsePrimitive610_deriv_eq_simplePole_of_source` | wrapper hypotheses: Backwire peel \(p_5=h_0^5 w_1\), \(N=C(\lambda)h_0^9\) |
| `Grok68TerminalBranchClosureScratch.lean`, `fiveToSix_qZero_terminal_dZ_sum_algebra68` | 68 identity \(3dZ+BU-18\gamma B^2+C(C_0)=0\) and two-case degree comparison |
| `LowScale610ScaleTwoSourceFace.lean` | \(N=5p_5 H^2-3q_9\), aligned face \(N=0\) |
| `LowScale610ScaleTwoFifteenthFinalRow.lean`, `fifteenthCoefficientJacobianRow_610` | degree-\(0\) row \(p_0'q_1-p_1 q_0'=Cj\) |
| `derive_610_degree_zero_residual.py` (`Abar`–`Xbar`, clearing \(h^{75}\)) | depressed numerators used for the pole comparison in §2 |
| `Sol410ScaleTwoAlignedSquareClosureScratch.lean` | 410 analog: ninth head \(327680\,p_1(a)^3=0\) against \(p_1(a)\neq 0\) |
| `Grok410ScaleTwoAlignedFaceClosureScratch.lean` | 410 aligned face closed by jet exhaustion plus that unit head, **not** by a pole tower |

Packet tops on this face: \(h_0\neq 0\), \(H=h_0^2\), \(h_0.\mathrm{natDegree}=1\),
\(j\neq 0\), \(N=0\). Differentiation in the source variable \(X\) is the
polynomial derivative. A prime mark on a compact letter (\(w_{1n}\),
\(e_{1n}\), \(v_1\), \(q_{41}'\) in sibling files) is a Taylor label at
the unique root \(a\), not a Lean name.

### 0.2 What the prompt listed as committed, and was not

On `origin/master` the only aligned-square scratch is
`Grok610AlignedSquareMixedPairScratch.lean` (2113 lines, import
`Grok610AlignedSquareNinthLoadsScratch`). The following names are
**absent** from the git tree (raw GitHub 404, `git log --all` empty):

- `Grok610AlignedSquareFinalRowScratch.lean`
- `Grok610AlignedSquareEndgameScratch.lean`
- `Grok610AlignedSquareNinthLoadsScratch.lean`

They exist as untracked working files in the sandbox-blocked nested
worktree. Content quoted from Grok session
`01a05a10-0357-7411-9b87-f3d4dde72e5a` (which read and authored those
files) is labelled **UNVERIFIED** as a git object. MixedPair’s own
header and theorems already record the residuals those files were
written to produce; those MixedPair statements **are** committed.

### 0.3 FALLACY-v2 (read first)

- Pole identities are used only after the vertex class
  (\(H=h_0^2\), \(\deg h_0=1\)) **and** every source hypothesis of the
  wrapper. The linear-root wrapper’s Backwire peel and \(\lambda\neq 0\)
  fail on this face; no pole-six lemma is applied to aligned-square.
- Floor/attainment: \(h^{75}\) is the native clearing of the weight-15
  primitive **before** peel, committed for the linear-root substitution.
  It is not claimed as the aligned vanishing order.
- Prime/derivative: \(w_{1n},e_{1n},e_{1b},a_{2b},v_1,y_1\) are Taylor
  labels of source-coefficient polynomials.
- No flag/place/series identification; no exit-price assertion.

No `charge_basis` line: nothing here is a new exit-price claim.

---

## 1. The frozen packet (committed)

Theorem `normalized610ScaleTwo_alignedSquare_mixedPairReduction`.
On a normalized aligned source with \(H=h_0^2\):

\[
\begin{aligned}
h_0.\mathrm{natDegree}&=1,\qquad h_0(a)=0,\qquad j\neq 0,\\
p_0'q_1-p_1 q_0'&=C(j),\\
p_0'(a)\,q_1(a)-p_1(a)\,q_0'(a)&=j,\\
p_5&=h_0^4 w_1,\qquad
p_4&=h_0^2 f_2,\qquad
3f_2-w_1^2&=h_0 e_1,\\
27p_3-w_1^3&=h_0 e_2,\qquad
e_2&=h_0 e_3,\qquad
w_1(e_2-3e_1 w_1)&=h_0 u_2,\\
2048\,e_1^3 w_1^4-C(\mu)w_1^7&=h_0 s_2,
\end{aligned}
\]

and the three peeled rows of the consumed degree-\(7/6/5\) Jacobian
coefficients are constants times \(h_0^6\):

\[
\begin{aligned}
\texttt{alignedNinthSquarePeeledRow610}&=C(\mu_3)\,h_0^6,\\
\texttt{alignedEighthSquarePeeledRow610}&=C(\kappa_7)\,h_0^6,\\
\texttt{alignedTenthSquarePeeledRow610}&=C(\kappa_9)\,h_0^6.
\end{aligned}
\]

Evaluating the product identity, the eighth combined row, and the ninth
peeled row at \(a\) and applying `alignedNinthSquareResolve_610` gives
the two-limb split

\[
w_1(a)=0\qquad\text{or}\qquad\bigl(\mu=0\land e_1(a)=0\bigr).
\]

### 1.1 Limb \(w_1(a)=0\)

Global divisor \(w_1=h_0 w_{1n}\). Eighth quadratic plus tenth remainder
force \(e_1(a)=p_2(a)=0\) over any characteristic-zero field
(`alignedSquareW1Zero_e1_a2_zero610`: the ray \(135p_2=2e_1^2\) reduces
the quadratic to \(\frac{7}{25}e_1^4\), hence \(e_1=0\) and then
\(p_2=0\)). Next ninth head is \(-5120 e_3(a)^3\), so \(e_3(a)=0\).
After \(e_1=h_0 e_{1b}\), \(p_2=h_0 a_{2b}\), \(e_3=h_0 e_{3b}\), the
mixed pair is

\[
a_{2b}(6p_1-a_{2b}w_{1n})=0,
\qquad
45p_1^2-30p_1 a_{2b}w_{1n}+a_{2b}^2(2\kappa-5e_{1b}+5w_{1n}^2)=0.
\]

- Child \(a_{2b}(a)=0\): ninth then forces \(p_1(a)=0\) and \(q_1(a)=0\).
  `alignedSquareMixed_kellerCollision610` gives \(0=j\). **Empty.**
- Complement \(a_{2b}(a)\neq 0\): live residual
  \[
  6p_1(a)=a_{2b}(a)\,w_{1n}(a),
  \qquad
  20e_{1b}(a)=8\kappa+5w_{1n}(a)^2.
  \]

On this complement \(q_1\) is **not** in the \(h_0^0\) ninth head. It
enters at \(h_0^1\) with unit coefficient \(-1632586752\)
(`alignedSquareW1ZeroMixedNinthLoad610`).

### 1.2 Limb \(\mu=0\), \(w_1(a)\neq 0\)

Then \(e_1=h_0 e_{1n}\), ninth head forces \(u_2(a)=81p_2(a)\), and the
next ninth head is \(135\nu w_1^4\), so \(\nu=0\). Product upgrade
\(u_2=h_0 v+81p_2\), rewrite \(y=e_3-6e_{1n}w_1\). Cube identity

\[
y^3+9v^2 w_1=h_0\rho,
\qquad
y(a)^3+9v(a)^2 w_1(a)=0.
\]

Mixed ninth/tenth heads combine (`alignedSquareMuZeroMixed_headCombo610`)
to

\[
2w_1 N+T=30720\,v y^2-45\nu_2 w_1^3,
\]

hence at \(a\)

\[
2048\,v(a)\,y(a)^2=3\nu_2 w_1(a)^3.
\]

- If \(v(a)=0\): cube and \(w_1(a)\neq 0\) force \(y(a)=0\), then
  \(\nu_2=0\), and the deepened tenth head is
  \(92160(243p_1+v_1 w_1)^2\), so
  \(243p_1(a)+v_1(a)w_1(a)=0\). The deepened ninth head remains linear
  in \(p_1\) **and** \(q_1\) (unit coefficient \(-1632586752\) on
  \(b_1=q_1\) already at \(h_0^0\)).
- If \(v(a)\neq 0\): cube plus combo determine a pair
  \((y(a),\nu_2)\) with \(y(a)\neq 0\) available (e.g. \(w_1(a)=v(a)=1\)
  gives \(y(a)^3=-9\)). Neither Keller cross-product is forced to \(0\).

MixedPair’s header states the chamber is **not** claimed empty. That is
the honest landed status.

---

## 2. Question 1: a bounded \(h\)-adic tower?

### 2.1 What closed the linear-root sibling

On the **nonzero** face \(N=C(\lambda)h_0^9\) with \(\lambda\neq 0\),
after the Backwire peel \(p_5=h_0^5 w_1\), \(p_4=h_0^4 a_{42}\), …:

1. Affine depression \(y=(z-r)/h_0\) sends the Keller identity to
   \(\mathrm{differentialJacobian}(\hat p,\hat q)=C(j/h_0)\).
2. The weight-15 primitive satisfies \(\rho'=C(j)/h_0\)
   (`degreeZeroPostCollapsePrimitive610_deriv_eq_simplePole_of_source`).
3. Native clearing \(h^{75}\) (every depressed coordinate except \(L\)
   has pole/weight ratio \(5\); weight \(15\)). After Backwire,
   \(Q=h_0^{69}\cdot(\text{jet quotient})\), so \(h_0^6\rho\) is
   polynomial. Pole order \(6\); ceiling at order \(75\); at most seven
   frozen heads.
4. Exhaustion of those heads exposes \(\rho\) as a polynomial, which
   cannot have derivative \(Cj/h_0\) with \(j\neq 0\).

That wrapper’s hypotheses include the Backwire identities
\(p_5=h_0^5 w_1\), \(p_4=h_0^4 a_{42}\), \(p_3=h_0^2 p_{32}\),
\(p_2=h_0 p_{21}\) and \(N=C(\lambda)h_0^9\). The linear-root closure
`degreeZeroFace610_linearRoot` additionally takes \(\lambda\neq 0\).

### 2.2 What fails to transfer

| Quantity | Linear-root (landed) | Aligned square (this face) |
|---|---|---|
| Discriminator | \(N=C(\lambda)h_0^9\), \(\lambda\neq 0\) | \(N=0\) identically |
| \(p_5\) peel | \(h_0^5 w_1\) (Backwire) | \(h_0^4 w_1\) (MixedPair) |
| \(p_4\) peel | \(h_0^4 a_{42}\) | \(h_0^2 f_2\) with \(3f_2-w_1^2=h_0 e_1\) |
| Source wrapper | landed | **OPEN**: Backwire hypotheses false |
| Native clearing | \(75\) | same formula **if** the same primitive is used; not instantiated |
| Vanishing order | \(69\) | strictly smaller than \(69\) (computed below) |
| Remaining pole | \(6\) | **OPEN**, larger if the same primitive is used |
| Endgame identity | \(\rho'=Cj/h_0\) vs \(\rho\) polynomial | not landed |

Using pole-six on this face would be a pole identity without the matching
source hypotheses. Typed **OPEN**, not filled by the linear-root numbers.

The *shape* (depression \(\to\) a primitive of the degree-\(0\) row
\(\to\) clearing \(\to\) a finite \(h\)-adic tower whose ceiling is
holomorphic \(\rho\) versus \(Cj/h_0\)) is available as a **future
authoring plan**. It is not a closing argument from committed input.

### 2.3 Pole comparison from committed `Abar,Bbar,Cbar`

`derive_610_degree_zero_residual.py` records, independently of the face,

\[
\begin{aligned}
Abar&=12 a_4 h^6-5a_5^2,&& A=Abar/(12h^{10}),\\
Bbar&=54 a_3 h^{12}-36 a_4 a_5 h^6+10 a_5^3,&& B=Bbar/(54h^{15}),\\
Cbar&=144 a_2 h^{18}-72 a_3 a_5 h^{12}+24 a_4 a_5^2 h^6-5a_5^4,&& C=Cbar/(144h^{20}).
\end{aligned}
\]

Substitute the aligned peel \(a_5=h^4 w_1\), \(a_4=h^2 f_2\),
\(a_3=(w_1^3+h^2 e_3)/27\), then \(3f_2-w_1^2=he_1\):

\[
\begin{aligned}
Abar&=4e_1 h^9-h^8 w_1^2,&&
A=\frac{-w_1^2}{12 h^2}+\frac{e_1}{3h},\\
Bbar&=-12 e_1 w_1 h^{13}+2e_3 h^{14},&&
B=\frac{-2 e_1 w_1}{9 h^2}+\frac{e_3}{27 h}.
\end{aligned}
\]

On the live \(\mu=0\) limb \(e_1=h e_{1n}\) and \(w_1(a)\neq 0\), the
\(h^8 w_1^2\) term in \(Abar\) survives:

\[
Abar=4e_{1n}h^{10}-h^8 w_1^2,
\qquad
\mathrm{pole}(A)=2,
\qquad
\mathrm{pole}(B)=1,
\qquad
\mathrm{pole}(C)=4
\]

(\(Cbar\) still has valuation \(16\) against denominator \(20\), using
\(a_2\) of valuation \(0\) as a worst-case lower bound on vanishing).

Backwire comparison, same numerators: \(a_5=h^5 w_1\), \(a_4=h^4 a_{42}\)
gives \(\mathrm{pole}(A)=0\), \(\mathrm{pole}(B)=1\).

So if the **same** weight-15 primitive were used, the aligned peel would
leave a **longer** jet quotient than the linear-root \(h\)-degree
\(\le 6\), not a shorter one. The \(A^7 L\) summand of
`degreeZeroBaseGroup610` has pole \(14\) from \(A\) alone once
\(\mathrm{pole}(A)=2\). (On aligned one has \(\lambda=0\), and the python
identification \(L=-\lambda/3\) would set \(L=0\) and kill \(A^7 L\);
that identification is part of the un-instantiated wrapper, not a landed
theorem on \(N=0\).)

The \(q\)-side poles were not recomputed: MixedPair does not record a
peel of \(q_8\). If \(b_8\) had valuation \(0\), then with \(\lambda=0\)

\[
Pbar=-5a_5^2+4b_8 h^2=-5h^8 w_1^2+4b_8 h^2
\]

would give \(\mathrm{pole}(P)=8\). That is a warning, not a valuation
theorem.

**Clearing power, pole order, ceiling (aligned):** not computed. The
only committed triple is the linear-root \((75,6,75)\), which does not
apply. A later wrapper must recompute all three from the aligned peel
and, if \(L=0\) is justified, from that specialization.

The peel ladder on this face cannot be said to “run past the ceiling
and force \(\rho\) polynomial”: there is no landed \(\rho\), and the
surviving MixedPair residuals are evaluation identities at \(a\), not
frozen heads of a jet quotient.

---

## 3. Question 2: an exact-identity kill?

The 68 terminal branch closed by an identity **in** \(k[X]\),

\[
3dZ+BU-18\gamma B^2+C(C_0)=0,
\]

whose two degree cases on the wall \(9N=7S\)
(\(\deg B=D\), \(\deg U=N-D\), \(\deg d=V>N>2D\)) are both impossible
at a single coefficient.

### 3.1 The conserved weights are tautological at \(a\)

UNVERIFIED as a git object, but recorded in the Endgame module that
MixedPair imports, theorem
`normalized610ScaleTwo_alignedSquare_endgamePacket`: the unreduced
first integrals of the exhausted tower are

\[
\begin{aligned}
N&=0 &&\text{(weight 5, the aligned hypothesis)},\\
\texttt{alignedTwelfthDefect610}&=C(c)\,H^{30} &&\text{(weight 30)},\\
\texttt{localClearedThirteenthDefect610}&=C(\xi)\,h_0^{65} &&\text{(weight 65)},\\
\texttt{localClearedFourteenthDefect610}&=C(\nu)\,h_0^{70} &&\text{(weight 70)},
\end{aligned}
\]

together with the degree-\(1\) row

\[
p_1' q_1+2p_0' q_2-2p_2 q_0'-p_1 q_1'=0
\]

and the degree-\(0\) Keller row. Endgame’s header states that the
unreduced weight-\(5/30/65/70\) identities are **tautological at \(a\)**
on the square jet \(p_5(a)=p_4(a)=0\). The live constraints sit in the
*cancelled peeled rows* of those integrals — exactly the eighth/ninth/tenth
objects MixedPair already used.

Evaluating a tautology at \(a\) produces \(0=0\), not a 68-style
identity of incompatible degrees.

### 3.2 No degree dictionary

A 68-style comparison needs exact \(\mathrm{natDegree}\) on each letter
of the identity. Committed input supplies \(Y\)-degrees
\(p.\mathrm{natDegree}=6\), \(q.\mathrm{natDegree}=10\) and the leading
identities \(p_6=H^3=h_0^6\), \(q_{10}=H^5=h_0^{10}\). It does **not**
bound \(\deg_X\) of \(p_5,\ldots,p_0,q_9,\ldots,q_0\). Without that
dictionary both degree cases of any candidate combination of the
peeled rows are OPEN. Cap-and-analogy from the 68 wall \(9N=7S\) is
forbidden.

The degree-\(1\) row is homogeneous of Jacobian weight \(1\) and equals
\(0\); it is not an inhomogeneous identity with a constant term playing
the role of \(C(C_0)\). Combined with Keller it is a linear system in
the **derivatives** \(p_0'(a),p_1'(a),q_0'(a),q_1'(a)\), not a
coefficient comparison in \(k[X]\).

**No exact-identity kill from committed input.**

---

## 4. Question 3: do the limbs collapse to \(0=j\)?

### 4.1 Which peeled letters enter the Keller row at \(a\)

The identity is

\[
p_0'(a)\,q_1(a)-p_1(a)\,q_0'(a)=j.
\]

| Letter | Status on the live packet | Enters Keller at \(a\) as |
|---|---|---|
| \(p_1(a)\) | determined on both live children (below) | value, coefficient of \(q_0'(a)\) |
| \(q_1(a)\) | **not** determined on either live child; unit coefficient in the next ninth order | value, coefficient of \(p_0'(a)\) |
| \(p_0'(a)\) | \(X\)-derivative of \(p_0\); the jet controls \(p_0(a)\), not \(p_0'(a)\) | derivative |
| \(q_0'(a)\) | likewise | derivative |
| \(p_0(a)\) | appears in ninth/tenth at \(h_0^{\ge 2}\) (and in the unused eighth integer head, §4.3) | does **not** enter Keller |
| \(q_0(a)\) | tenth, high \(h_0\) | does **not** enter Keller |
| \(q_2(a)\) | eighth integer head | does **not** enter Keller |

`alignedSquareMixed_kellerCollision610` needs **both** values
\(p_1(a)=q_1(a)=0\). Then both products vanish regardless of the
derivatives. One-sided vanishing leaves a single product equal to \(j\),
which is consistent (e.g. \(p_1(a)=0\), \(q_1(a)\neq 0\) gives
\(p_0'(a)q_1(a)=j\)).

### 4.2 Limb \(\mu=0\): \(v(a)=0\) is not forced

Cube \(y^3+9v^2 w_1=0\) with \(w_1(a)\neq 0\) forces \(y(a)=0\) **only
after** \(v(a)=0\). The mixed combo \(2048 v y^2=3\nu_2 w_1^3\)
determines \(\nu_2\) once \(v,y,w_1\) are given; it does not kill \(v\).

Endgame *predicted* a matching eighth head \(1280 v^2\) which would have
forced \(v(a)=0\). NinthLoads’ CAS (session `01a05a10`, **UNVERIFIED** as
git, but the conclusion is compatible with MixedPair not using such a
head) distinguishes two eighth objects after the product substitution
\(w_1(e_3-3e_{1n}w_1)=h_0 v+81p_2\):

- **Plain** eighth head \(1280(81p_2+3e_{1n}w_1^2-e_3 w_1)^2\). At
  \(h_0=0\) the product identity makes the parenthesis \(0\). Tautology.
- **Integer** eighth head after substituting the product, valuation \(4\):
  \[
  \begin{aligned}
  &174960\,p_0 w_1^2-116640\,p_1 e_{1n}w_1+38880\,p_1 e_3\\
  &\quad+46656\,p_1\kappa w_1-944784\,q_2\\
  &\quad-1680 e_{1n}^3 w_1^2+720 e_{1n}^2 e_3 w_1+\cdots-\kappa_5 w_1^2+80 v^2.
  \end{aligned}
  \]
  Linear in \((p_0,p_1,q_2,v^2)\), not a unit times \(v^2\).

MixedPair consumed ninth+tenth on this limb and **did not** consume that
integer eighth head. One more conserved-weight relation of this shape
does **not** force \(v(a)=0\), and therefore does not force the cube to
\(y(a)=0\), and therefore does not reach the deepened pair where
\(243p_1+v_1 w_1=0\).

Even on the child \(v(a)=0\), the deepened ninth is

\[
\begin{aligned}
&-\kappa\cdot 110592\,e_{1n}^3 w_1+\kappa\cdot 26873856\,e_{1n}p_1
+\kappa\cdot 80621568\,w_1 p_0\\
&\quad-\kappa_3\cdot 3359232\,p_1-\kappa_5\cdot 1152\,e_{1n}w_1
-\kappa_7\cdot 36 w_1\\
&\quad+138240 e_{1n}^4 w_1-33592320 e_{1n}^2 p_1
+201553920 e_{1n} w_1 p_0\\
&\quad-46080 w_1 v_1^2-22394880 p_1 v_1-1632586752\,q_1
\end{aligned}
\]

at \(h_0^0\) (`alignedSquareMuZeroDeepMixedNinthLoad610`). After
\(p_1=-v_1 w_1/243\) this is still linear in \(q_1\) **and** \(p_0\).
Setting it to \(0\) solves for one letter, not both Keller values.

### 4.3 Limb \(w_1(a)=0\): the quadratic collapsed; the complement did not

The \((p_2,e_1)\) quadratic **did** collapse (committed). The remaining
complement \(a_{2b}(a)\neq 0\) has \(p_1(a)\) proportional to
\(w_{1n}(a)\). Forcing \(p_1(a)=0\) is equivalent to \(w_{1n}(a)=0\)
(deeper divisor on \(w_1\)), which is a new peel, not a unit head.

The 410 closer was a ninth head \(327680 p_1(a)^3\) against a
same-witness \(p_1(a)\neq 0\). Here the mixed ninth \(h_0^0\) head is
\(a_{2b}(6p_1-a_{2b}w_{1n})\), which is \(0\) on the complement by
construction. The next order has a unit times \(q_1\), so it constrains
\(q_1(a)\) linearly in the other letters; it does not by itself produce
\(q_1(a)=0\) and \(w_{1n}(a)=0\) simultaneously.

Weight \(30/65/70\) unreduced, as in §3.1, do not evaluate to a new
relation at \(a\).

### 4.4 No \(0=j\) on the live children

| Child | \(p_1(a)\) | \(q_1(a)\) | Keller |
|---|---|---|---|
| \(w_1=0\), \(a_{2b}=0\) | \(0\) | \(0\) | \(0=j\), **False** (landed) |
| \(w_1=0\), \(a_{2b}\neq 0\) | \(a_{2b}w_{1n}/6\) | unconstrained at \(h_0^0\) | one free derivative |
| \(\mu=0\), \(v\neq 0\) | in mixed ninth/tenth, not forced \(0\) | in ninth at higher \(h_0\) | both products live |
| \(\mu=0\), \(v=0\) | \(-v_1 w_1/243\) | linear in deepened ninth | both products live unless \(v_1=0\) and the \(q_1\)-coefficient kills |

---

## 5. Missing objects (why PARTIAL, not DERIVED or BLOCKED)

A referee-checkable closure would be one of:

1. two-sided \(p_1(a)=q_1(a)=0\) forced on every live child, then
   `alignedSquareMixed_kellerCollision610`;
2. a 68-style identity in \(k[X]\) of incompatible degrees;
3. a landed aligned wrapper with computed clearing/vanishing/ceiling,
   exhausted through holomorphic \(\rho\) versus \(Cj/h_0\).

(1) is a theorem *if* the vanishings are granted; MixedPair grants them
on one child only. (2) fails for the reason in §3. (3) is the a priori
shape of §2; carrying it out is new authoring, and the pole comparison
says it would be a longer tower than linear-root, not a shortcut.

**Named missing objects**, in the order that actually shortens the
chamber rather than restarting a tower:

- **M1 (next ninth order on the \(w_1=0\) complement).** Cancel the
  remaining \(h_0\) in `alignedSquareW1ZeroMixedNinthLoad610` after
  substituting \(6p_1=a_{2b}w_{1n}\). The \(h_0^1\) coefficient contains
  \(-1632586752\,q_1\). The exact residual is that linear form in
  \((q_1,e_{1b},e_{3b},\kappa,\mu,w_{1n},a_{2b})\) at \(a\). A unit
  times \(q_1(a)\) plus a unit in the remaining letters would force
  \(q_1(a)=0\); one still needs \(w_{1n}(a)=0\) for the collision.
- **M2 (\(\mu=0\) integer eighth head after product).** The valuation-4
  form of §4.2, **UNVERIFIED** as a Lean identity (CAS in session
  `01a05a10`; MixedPair did not land it). Combined with the mixed
  ninth/tenth combo and the degree-\(1\) row, this is the unused
  conserved-weight relation on that limb. It does not by itself force
  \(v(a)=0\).
- **M3 (aligned source wrapper), only if M1–M2 fail.** Instantiate
  `differentialJacobian_affineDepress_sourceToRatFunc68` on a literal
  aligned \((6,10)\) source with the MixedPair peel in place of
  Backwire; produce \(\rho'=C(j)/h_0\) or a typed OPEN if the depressed
  Jacobian is not a simple pole; recompute clearing power and vanishing
  order (do not reuse \(75\) and \(69\)). This is the analog of
  `Grok610DegreeZeroSourceWrapperScratch`, not a copy of it.

A **BLOCKED** verdict would require a consistent polynomial model of the
reduced packet. Evaluation-at-\(a\) of the \(\mu=0\) cube and combo is
easy (e.g. \(w_1(a)=v(a)=1\), \(y(a)^3=-9\), \(\nu_2\) from the combo,
Keller satisfied by a choice of \(p_0'(a),q_1(a)\)), but that is a
pointwise assignment, not a polynomial in \(k[X]\). No such polynomial
model is constructed. Saturation/quotient language is not used.

---

## 6. Computations (aligned peel poles)

From committed `Abar` after the committed MixedPair peel and
\(3f_2-w_1^2=he_1\):

```
Abar = 4*e1*h**9 - h**8*w1**2
Bbar = -12*e1*h**13*w1 + 2*e3*h**14
```

After \(\mu=0\) upgrade \(e_1=h e_{1n}\):

```
Abar = 4*e1n*h**10 - h**8*w1**2     # pole(A)=2 because w1(a)≠0
Bbar = h**14*(-12*e1n*w1 + 2*e3)    # pole(B)=1
```

Backwire, same numerators:

```
Abar valuation 10  => pole(A)=0
Bbar valuation 14  => pole(B)=1
```

Keller collision (committed ring identity):

```
eval_a (p0' * q1 - p1 * q0') = eval_a (C j) = j
p1(a)=0 and q1(a)=0  =>  0 = j.
```

\(w_1=0\) quadratic plus tenth ray (committed):

```
Q8:  e1^4 - 81 e1^2 p2 + 2187 p2^2 = 0
T10 remainder: 55296 e1 (135 p2 - 2 e1^2) = 0 after reducing by Q8
ray 135 p2 = 2 e1^2  =>  25 * Q8 = 7 e1^4  =>  e1=0  =>  p2=0.
```

Mixed combo (committed `ring`):

```
2 w1 * N + T = 30720 v y^2 - 45 ν2 w1^3
N=T=0  =>  15*(2048 v y^2 - 3 ν2 w1^3)=0  =>  2048 v y^2 = 3 ν2 w1^3.
```

---

## 7. FALLACY-v2 recap

- Pole identity: not applied to aligned-square. Linear-root pole-six is
  cited only as the sibling method, with its hypotheses listed and
  shown to fail here.
- Floor/attainment: \(75\) is native clearing of the weight-15 primitive
  under the linear-root substitution; not claimed as aligned vanishing
  order. Pole(\(A\))=2 is an exact identity of the committed `Abar`
  after the committed peel, not a lower bound sold as equality of a
  tower length.
- Prime/derivative: Taylor labels distinguished from Lean primes and
  from \(p_0',q_0'\) in the Keller row.
- Raw remainder: MixedPair heads are taken after `cancel` of explicit
  \(h_0\)-powers, branched on vanished leaders \(w_1,\mu,e_1,v,a_{2b}\),
  with the zero polynomial handled as the closed \(a_{2b}=0\) child.
- No flag/place/series; no `charge_basis`.
