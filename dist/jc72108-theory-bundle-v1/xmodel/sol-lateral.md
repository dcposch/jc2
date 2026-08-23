# Maximally lateral proof/disproof ideas for the plane Jacobian Conjecture

**Date:** 2026-08-14  
**Scope:** ideas not already run in this campaign, ranked by novelty x payoff x one-week tractability

## Executive summary

The campaign has already made the obvious local algebra unusually expensive to revisit. Theorem A is promoted; the strip obstruction is uniform in characteristic zero; `td <= 5` and the corrected `td = 7` panel are closed; residual-32 is now an exact 91-equation/84-variable no-log system with 42 high tails placed first for elimination; and the degree-150 farm has 13 remote EMPTY verdicts awaiting the audit/re-emission protocol before they can become mathematical data. The best new moves therefore change the direction of information flow.

My three strongest disproof bets are: search the *nearby* characteristic-2 collision locus for a vanishing Witt/Bockstein obstruction; continue the deliberately solvable `ctl0` residual fiber into the real residual-32 fiber; and quotient the new three-dimensional counterexample by one carefully chosen lifted \(\mathbb G_a\)-action. The first already has a useful exact pilot result: Mondello's map itself has a nonzero Cartier obstruction and cannot lift modulo 4 with *any* correction support. The strongest proof bets are to mine farm `[1]` outputs into a parametric Nullstellensatz identity and to dualize tower deaths into a Hall-deficiency certificate.

The table uses scores from 1 to 10. The product, not my aesthetic preference, sets the order.

| rank | idea | side | novelty | payoff | tractability | product |
|---:|---|---|---:|---:|---:|---:|
| 1 | Witt-Bockstein search around characteristic-2 collisions | disproof / dual | 10 | 10 | 8 | **800** |
| 2 | Singular continuation from `ctl0` to residual-32 | disproof; machinery inverted | 9 | 9 | 8 | **648** |
| 3 | One-LND quotient descent of the 3D counterexample | disproof | 10 | 10 | 6 | **600** |
| 4 | Mine farm `[1]` certificates into a symbolic theorem | proof; machinery repurposed | 8 | 9 | 8 | **576** |
| 5 | Hall-deficiency dual of the tower theorem | proof; machinery inverted | 10 | 9 | 6 | **540** |
| 6 | Sparse rational SOS/Positivstellensatz certificates | proof | 9 | 8 | 6 | **432** |
| 7 | \(K_2\) tame-symbol reciprocity on the tower | proof | 10 | 8 | 5 | **400** |
| 8 | \(p\)-adic escape-mass balance | proof | 9 | 8 | 5 | **360** |
| 9 | Local \(\mathbb A^1\)-degree at infinity | proof | 8 | 8 | 4 | **256** |

### Novelty and verdict discipline

“Nobody has tried this” cannot be certified by a literature search. Here it means: no occurrence in the campaign corpus after targeted searches of `README.md`, the tail of `AUDIT.md`, `RECON.md`, `notes.md`, the prior `xmodel` avenue reports, and the machinery documents; and no matching use found in targeted searches of the primary literature through 2026-08-14. Each entry names its nearest neighbor so that the novelty claim is falsifiable. I deliberately excluded lanes already proposed or run here: no-log pins, toric/Macaulay circuit closure, positive off-axis Puiseux lifting, bounded Hermite–Padé algebraization, semigroup symmetry, Camacho–Sad/Baum–Bott indices, coefficient holonomy, and static Hurwitz-passport enumeration.

The promotion boundary matters throughout:

- A residual-32 point is a compatible D21 no-log **germ**, not a polynomial map.
- A tower survivor is a combinatorial/valuative **skeleton**, not a germ.
- A modular point is evidence until it Hensel-lifts or reconstructs exactly in characteristic zero.
- Only a full fixed-support Keller solution with every required corner/nonproperness guard, or an inherited collision, is a counterexample.
- Only an exact characteristic-zero identity/certificate is a proof-tier kill.

All modular tests below inherit the audit rules: fully expand parentheses, reduce every coefficient into `[0,p)`, avoid `msolve`'s signed-64-bit clamp, require an independent parser round trip, and never read a zero-byte output as a verdict.

The fleet is not idle: box01 is on the farm, Box02 on residual/stuck7, and ultramem on `sat23`. “Use the three boxes” below means take coordinator-approved spare slots as those standing jobs finish; none of these pilots should displace a decisive current run.

## 1. Witt-Bockstein search around characteristic-2 collisions

**Side:** disproof-first, with a possible proof theorem as the failure mode.  
**Score:** \(10\times10\times8=800\).

### Five-line pitch

1. Treat a separable characteristic-\(p\) Keller collision as the special fiber of a deformation problem, not as a candidate to lift naively.
2. For lifts \(P=P_0+pA\), \(Q=Q_0+pB\), the first error defines a class in the cokernel of \((A,B)\mapsto[A,Q_0]+[P_0,B]\).
3. A Cartier/de Rham projection detects part of this Bockstein class before any Groebner calculation.
4. Search nearby finite-field collision maps whose class vanishes, then lift the full Keller-plus-collision system through \(W_2,W_3,\ldots\).
5. A nonsingular coherent \(\mathbf Z_p\) lift is a characteristic-zero Keller collision and therefore a plane counterexample.

### Why this appears genuinely unexplored

The nearest literature studies positive-characteristic formulations of JC, separability, and Witt-Jacobians: [Maubach-Rauf](https://arxiv.org/abs/1507.02946), [Mittmann-Saxena-Scheiblechner](https://arxiv.org/abs/1202.4301), and [Mondello's explicit plane example](https://arxiv.org/abs/2608.02634). I found no paper deforming the *coefficient-and-collision scheme* of a separable plane Keller example through Witt length, nor classifying its first Bockstein obstruction. The campaign verified Mondello and stress-tested the characteristic-zero step in Theorem A, but did not search the neighboring obstruction-zero locus.

There is already a useful exact negative control. For Mondello's

\[
P_0=x+x^2y+x^4+x^6y^2,\qquad
Q_0=y+x^5+x^6y+x^7y^2+x^8y^3,
\]

take the same 0/1 polynomials over \(\mathbf Z\) and write

\[
E=\frac{[P_0,Q_0]-1}{2}\pmod 2.
\]

The coefficient of \(xy\) in \(E\) is 1 (the full odd-odd support is \((1,1),(7,1),(9,3)\)). Every correction contributes

\[
([A,Q_0]+[P_0,B])\,dx\wedge dy
  =d(A\,dQ_0+P_0\,dB),
\]

an exact 2-form. But \(xy\,dx\wedge dy\) is nonzero in
\(H^2_{dR}(\mathbf F_2[x,y])\). Hence Mondello itself has **no mod-4 polynomial lift, regardless of the degrees or supports of \(A,B\)**. That is a support-independent theorem, not a bounded search result.

### First concrete test this week

1. Reuse `cases/mondello_verify.py` and `cases/mondello_collapse.py` as exact controls; add the linear \(W_2\) obstruction map and independently reproduce the Cartier verdict and direct rank defect.
2. Normalize the linear terms to \((x,y)\), take Mondello's two Newton hulls plus one lattice shell, and enumerate support masks over \(\mathbf F_2\) with \([P,Q]=1\), a normalized three-point collision, and a separability/odd-generic-degree guard.
3. Impose vanishing of the odd-odd Cartier part of \(E\) *before* solving the full linear correction system. Split support masks and collision normalizations over the three fleet boxes; use `msolve` only on expanded, reduced emissions.
4. For each obstruction-zero hit, solve \([A,Q_0]+[P_0,B]=-E\), then lift recursively to \(2^8\) as a screen. At every stage verify the untouched Jacobian and collision equations exactly; finite precision is not a verdict.
5. For promotion, choose a square subsystem with a 2-adic-unit Jacobian minor **and** prove by exact local reductions that every surplus equation lies in its completed local ideal. Multivariate Hensel then supplies a full \(\mathbf Z_2\) Keller-plus-collision point. Otherwise enumerate all tangent branches; an exact rational tuple is an alternative only if every equation verifies identically.

### Kill criterion

The registered hull-plus-one-shell experiment dies only when an exact primary decomposition shows that its Bockstein-zero separable collision locus is empty or consists entirely of triangular/injective maps. A billion misses is not a mathematical kill. The broad idea dies if one proves that every separable plane Keller collision in characteristic \(p\) has a nonzero first Cartier-Bockstein class; that “failure” would itself be a new proof-side rigidity theorem.

## 2. Singular continuation from `ctl0` to residual-32

**Side:** disproof-first; direct inversion of the residual machinery.  
**Score:** \(9\times9\times8=648\).

### Five-line pitch

1. `directionb_residual32_ctl0` is a deliberately solvable degeneration, not merely a parser guard.
2. Multiply the variable-free blocks of the 77 window rows by \(\tau\), producing \(H(z,0)=\texttt{ctl0}\) and \(H(z,1)=\) the true residual system.
3. At each valid radical/saturation point the zero-tail point is highly singular, so start with ramified arcs \(z_i=s^{w_i}(a_i+\cdots)\), \(\tau=s^d\), rather than ordinary tangent vectors.
4. Enumerate the weighted initial systems, isolate their branches, and track them to \(\tau=1\) with singular endgames and exact endpoint checks.
5. A finite endpoint is promoted D21 \(\to\) D23 \(\to\) full coefficient rows, turning the campaign's fake solution into a counterexample-germ generator.

### Why this appears genuinely unexplored

Generic numerical homotopy is not new, and an old campaign plan mentioned homotopy software abstractly. The new object is the *specific guard-to-main Rees deformation* of the exact residual-32 scheme, while retaining its common radical and Rabinowitsch rows. The campaign uses `ctl0` solely to detect transcription errors; it has never asked which components of that solvable special fiber deform to the true fiber. The nearest tropical-JC paper, [Grigoriev-Radchenko](https://doi.org/10.1016/j.jsc.2020.07.012), studies tropical maps and injectivity, not a singular degeneration of a JC coefficient scheme.

### First concrete test this week

1. Diff the main and `ctl0` emissions row by row and emit
   \(H_i(z,\tau)=H_i^{ctl0}(z)+\tau(H_i^{main}-H_i^{ctl0})(z)\) for the 77 window rows. Append the five radical and three Rabinowitsch rows byte-identically; they are common to both fibers and must **not** be scaled.
2. Keep all six no-log pins from the outset. Work over each valid nonzero radical/saturation branch, with all tail `x*` variables zero at the known special-fiber point. Enumerate \(d=1,\ldots,12\) and small rational variable weights satisfying tropical balance; solve each saturated initial system over the three banked primes with `msolve`.
3. Use the unpinned 85-row system and the known quadratic-flexibility family only as a planted control. That family is killed by the six level-42 pins and must **not** seed the real 91-row experiment; the no-log tangent cone has to be computed fresh.
4. Slice positive-dimensional starts generically, track all isolated paths in coordinator-approved fleet slots, and use deflation/endgames at singular endpoints. Re-evaluate every endpoint in the original expanded 91 rows and all saturation products.
5. For a surviving endpoint, recover exact algebraic coordinates by modular/minimal-polynomial reconstruction, append the D23 rows, and repeat. Call it a germ until a full polynomial coefficient system is reached.

### Kill criterion

Kill the route only after the saturated weighted start ideals for all minimal cones are certified unit, or a complete numerical irreducible decomposition with certified path accounting proves that every special-fiber branch diverges, hits \(W_1W_2(A_1-A_2)=0\), or fails a held-out exact row before \(\tau=1\). A tracker crash, an exploding path, or failure for one choice of \(d\) is not a kill.

## 3. Descend the three-dimensional counterexample along one lifted LND

**Side:** disproof.  
**Score:** \(10\times10\times6=600\).

### Five-line pitch

1. Start from the explicit noninvertible Keller map \(F:\mathbb A^3_{x,y,z}\to\mathbb A^3_{P,Q,R}\).
2. Choose a noncanonical triangular target locally nilpotent derivation \(\delta\) with a slice.
3. Lift it through \(F\): constant \(\det JF\) makes \(D=(JF)^{-1}(\delta\circ F)\) a polynomial derivation on the source.
4. If \(D\) is locally nilpotent, both affine 3-spaces split as invariant plane rings adjoined with a compatible slice.
5. The induced plane map is Keller and inherits noninjectivity, so it is a plane counterexample.

### Why this appears genuinely unexplored

The classical LND reformulation asks whether the canonical inverse-Jacobian derivations are all locally nilpotent; see, for example, [Derksen's notes, Theorem 5.9](https://sites.lsa.umich.edu/hderksen/wp-content/uploads/sites/614/2018/09/LND1.pdf). Public work on the new 3D example has studied its weighted \(\mathbb G_m\)-quotient, projections, graph models, and invariant rings; [Shaska](https://arxiv.org/abs/2607.20210) in fact explains why direct graded/equivariant descent does not produce a plane counterexample. I found no attempt to choose **one noncanonical triangular target \(\mathbb G_a\)-action and test whether its lift is again a \(\mathbb G_a\)-action**.

The logical bridge is short. If \(\delta(P)=1\), then \(D(F^*P)=1\), so the lifted action has a slice. The slice theorem gives \(k[x,y,z]=\ker(D)[F^*P]\); cancellation in dimension two identifies \(\ker(D)\cong k[u,v]\). In compatible slice coordinates an equivariant map has the form \((b,t)\mapsto(\bar F(b),t+h(b))\). Therefore invertibility of \(\bar F\) would force invertibility of \(F\), and two colliding source points cannot lie on the same source orbit.

### First concrete test this week

Use the exact map

\[
\begin{aligned}
P&=(1+xy)^3z+y^2(1+xy)(4+3xy),\\
Q&=y+3x(1+xy)^2z+3xy^2(4+3xy),\\
R&=2x-3x^2y-x^3z,
\end{aligned}
\]

whose determinant and triple collision have independent exact audits; one explicit source is [this reproducible write-up](https://github.com/shadybrook/jacobian-counterexample-research/blob/main/paper/main.md).

1. Enumerate triangular target derivations
   \[
   \delta=\partial_P+a(P)\partial_Q+b(P,Q)\partial_R,
   \qquad \deg a,\deg b\le2,
   \]
   together with all six coordinate orders. Each \(\delta\) is automatically locally nilpotent and has slice \(P\).
2. Compute \(D(x),D(y),D(z)\) exactly using \(\operatorname{adj}(JF)/\det JF\). Impose the sufficient equations \(D^8(x)=D^8(y)=D^8(z)=0\) on the coefficients of \(a,b\).
3. Emit those parameter ideals over two word-sized good primes, run `msolve` on the fleet, and reconstruct any common components over \(\mathbf Q\). The three canonical coordinate directions are negative controls; preliminary iteration shows persistent degree growth through order 8.
4. For an exact hit, compute generators of \(\ker D\), certify the coordinate splitting \(k[x,y,z]=\ker(D)[F^*P]\), write the induced two-coordinate map, and verify its constant Jacobian and an inherited collision directly.
5. Feed the resulting degree pair and Newton supports into the farm normalizer, Theorem A, and the tower checker. This is validation of a discovered plane map, not an assumption in the descent.

### Kill criterion

An exact unit ideal kills the registered \(\deg(a),\deg(b)\le2\), iterate-8 family. It does not kill higher triangular actions. The general route dies only after a leading-form/valuation theorem proves that every nonzero triangular target LND has a lifted derivation with some generator \(D^n(x_i)\ne0\) for all \(n\). Conversely, a modular parameter point that does not reconstruct or whose next iterate is nonzero is merely a finite-characteristic/finite-iterate artifact.

## 4. Mine farm `[1]` certificates into a symbolic theorem

**Side:** proof; the farm is repurposed from verdict engine to theorem-discovery corpus.  
**Score:** \(8\times9\times8=576\).

### Five-line pitch

1. Stop treating a farm Groebner basis `[1]` as the end of the computation.
2. Recover sparse identities \(1=\sum_i h_i f_i\) for many authenticated EMPTY cases.
3. Translate multiplier supports back through the manifests to bracket rows, faces, and polygon parameters.
4. Anti-unify the supports and interpolate the coefficients in \((m,n,d,k,d_2,\ldots)\).
5. A held-out exact identity becomes a human theorem killing an infinite family rather than one queued polygon.

### Why this appears genuinely unexplored

JC coefficient systems and their Groebner bases are well established; a recent example is [Ramirez-Valqui](https://arxiv.org/abs/2506.05697). Nullstellensatz certificates can encode combinatorial structure in other fields, as [Sevenster-Turner](https://arxiv.org/abs/1607.05031) demonstrate. I found no JC work that aligns certificates across a Newton-polygon farm and interpolates a parametric geometric identity. The campaign's toric/Macaulay experiment searched one residual fiber for a bounded certificate; it did not mine semantic motifs across families.

### First concrete test this week

1. First pull the 13 remote farm verdicts, authenticate their outputs, quarantine every unreduced \(p=65521\) input flagged by `AUDIT.md`, build guarded `.RED.ms` twins, and rerun affected cases. Until that finishes, use fast characteristic-zero `conjE` EMPTY controls and `reg_9_24_c3` only to debug certificate extraction.
2. For certificate degree \(D=1,\ldots,6\), solve the Macaulay linear system for the cofactors \(h_i\) over two good primes. Minimize support by deletion/re-solving; `msolve` supplies the verdict, while FLINT/Singular-style lifting supplies the representation.
3. Canonicalize variables and rows by emitter semantics, lattice translation, pole swap, and `r1/r2` byte-identical symmetries. Record support hypergraphs rather than raw variable numbers.
4. Once twelve clean EMPTY systems exist (farm plus regression controls), train on eight and predict the entire multiplier support on four held-out systems; use known NONEMPTY `r1_minsat`/`ctl0` systems as false-positive controls.
5. Once one motif survives, interpolate its coefficients in the polygon parameters by CRT/rational reconstruction and multiply out the identity exactly over \(\mathbf Q\). Only then test it on larger banked farm cases on Box02/ultramem.

### Kill criterion

Pre-register degree \(D\le6\) and the 8/4 train/holdout split. Kill this architecture if three nonisomorphic clean EMPTY families have no common support orbit, minimal certificate degree already exceeds 6 in the small controls, or the predicted support fails on two held-out cases. A motif that also “proves” a NONEMPTY control is immediately dead. Trivial cascade identities containing an explicit `-1` row do not count as learned mathematics.

## 5. Hall-deficiency dual of the tower theorem

**Side:** proof; the tower checker is inverted from path killer to dual-certificate generator.  
**Score:** \(10\times9\times6=540\).

### Five-line pitch

1. Every attempted tower survivor creates a sequence of defects that must be repaired at later ladder levels.
2. Regard defects as demand nodes and legal charged arrivals/cap slots as capacity-constrained repair nodes.
3. Prove that a realizable tower induces a matching or integral flow from every demand to a compatible repair.
4. A Hall-deficient demand set then gives one global obstruction inequality, independent of route enumeration.
5. If the same deficient set survives the td11/13 port, it can replace an expanding book by a reusable theorem.

### Why this appears genuinely unexplored

Approximate roots, Eggers-Wall trees, semigroups, and Newton-tree inequalities are standard neighbors. I found no Hall-marriage, transversal-matroid, or min-cut dualization of an approximate-root obstruction ladder in the plane-JC literature. This is also different from the campaign's NF-Z finite-language program: NF-Z quotients ordered futures, whereas this proposal extracts a *dual witness of insufficient repair capacity* from already promoted death traces.

### First concrete test this week

1. Instrument a scratch copy of `cases/tower_check.py` to emit, for each of the 17 corrected td7 cells, every demand created by gap, \(\Delta\)-integrality, cap-divisibility, WIN/TERM, and E5F, together with every later state legally able to discharge it.
2. Start with only the first two ladder levels. Encode non-reuse/sequential constraints as capacities; use bipartite matching first and min-cost flow or matroid intersection only if the exact rules require it.
3. Compute minimum Hall-deficient subsets and compare them with the five frozen JSON certificates and the 17-cell witness table. One subset must explain several geometrically different deaths.
4. Prove the bridge lemma on the concrete td7 traces: every fully legal tower route would induce the claimed matching. Without this lemma, a pretty min-cut is meaningless.
5. Feed the refiled td11/13 entry packets into the same graph before compiling their full route automata. The desired output is a parameterized deficient subset, not seventeen new case labels.

### Kill criterion

Kill if a faithful td7 graph admits a perfect matching, or if Hall deficiency appears only after each edge is annotated with essentially the complete A/B/C route proof. In the latter case the “dual” has compressed nothing. Also kill any abstraction whose bridge lemma fails on a legal negative perturbation from `tower_check.py`; a numerical min-cut alone is not a proof.

## 6. Sparse rational SOS/Positivstellensatz certificates

**Side:** proof; new computational substrate.  
**Score:** \(9\times8\times6=432\).

### Five-line pitch

1. Split every complex coefficient variable into real and imaginary parts, turning complex feasibility into real polynomial feasibility.
2. Search for a Positivstellensatz identity \(-1=\sigma+\sum h_i\Re f_i+\sum k_i\Im f_i\) with \(\sigma\) a sum of squares.
3. Exploit the residual system's banded correlative sparsity and pole-swap symmetry with chordal Gram blocks.
4. Rationalize any numerical Gram solution and verify the polynomial identity and positive semidefiniteness exactly.
5. Such an identity can prove emptiness even when F4 spends days exploring a large complex Groebner basis.

### Why this appears genuinely unexplored

Targeted searches found no Positivstellensatz/SOS attack on a plane-JC coefficient ideal. The nearest hits were the unrelated real Jacobian problem and general correlative-sparsity SOS technology, such as [Waki-Kim-Kojima-Muramatsu](https://doi.org/10.1137/050623802); any completeness claim would additionally require a running-intersection hypothesis, so this pilot claims only soundness of identities it actually verifies. Exact rational recovery is a real issue, not bookkeeping; [Magron-Safey El Din-Vu](https://arxiv.org/abs/2107.11825) is a useful neighboring method. This differs from the campaign's toric Macaulay lane because the SOS term uses order over \(\mathbf R\), not merely bounded ideal membership over \(\mathbf C\).

The reduction is sound: a complex zero is exactly a real zero of all real and imaginary parts. At a common zero the displayed identity would say \(-1=\sigma\ge0\).

### First concrete test this week

1. Validate the pipeline on the tiny authenticated EMPTY `9_24...c3` system and on a known NONEMPTY `ctl0` or `r1_minsat` control. For the latter, retain an explicit common zero and require the certificate search to produce no valid (-1) identity.
2. Realify `directionb_residual32_nolog`, including radical and saturation equations. Build the correlative-sparsity graph from the 91 rows; preserve all fill edges required for an exact global identity.
3. Run degree-2 and degree-4 **certificate-feasibility** SDPs with chordal Gram blocks, distributing radical/sign components and sparsity orderings only into available fleet slots. Feasibility is the desired certificate-side outcome; no numerical solver status is promoted.
4. From a numerically feasible Gram certificate, recover rational multipliers and rational Gram matrices. Verify \(-1=\sigma+\sum h_if_i\) coefficient by coefficient and certify every Gram block PSD by exact \(LDL^T\).
5. Re-run the exact identity with an independent expander and then, if it closes the residual window, translate its sparse support back to the 32 obstruction rows to look for a human lemma.

### Kill criterion

Kill the registered low-degree architecture if exact separating dual certificates exclude Gram identities at degrees 2, 4, and 6, or if chordal completion produces one nearly dense block too large for Box02. This does not kill higher-degree SOS. A **feasible Gram/certificate SDP** is success; a rigorously verified separating dual ray is the corresponding degree-bounded failure. Numerical “infeasible,” a rounded Gram matrix, or a certificate that omits complex realification/saturation is worthless.

## 7. \(K_2\) tame-symbol reciprocity on the tower

**Side:** proof.  
**Score:** \(10\times8\times5=400\).

### Five-line pitch

1. Normalize a generic fiber \(C_a=\{f=a\}\) and view \(x\) and \(g-b\) as rational functions on its smooth projective completion.
2. Their Steinberg symbol has local tame symbols whose normed product over every place is 1.
3. The tower records the infinity valuations and leading units needed for those local symbols, not just divisor degrees.
4. On full polynomial controls, compute finite-place contributions by exact resultants and test whether a combination across several \(b\)-values cancels them formally.
5. A leftover nontrivial unit relation can kill a tower genome that passes every additive residue and integer ledger.

### Why this appears genuinely unexplored

Targeted searches found no use of tame symbols, Contou-Carrere symbols, or Milnor \(K_2\) reciprocity in the plane-JC literature. General tame-symbol computations on curves certainly exist—for scale, compare [Liu-de Jeu](https://arxiv.org/abs/1402.4822)—but I found no coupling to Newton-Puiseux/approximate-root candidate data. This is not the “K-theoretic” stable reduction sometimes cited around BCW; the invariant here is an explicit multiplicative boundary product on the generic fiber.

### First concrete test this week

1. Implement the local formula
   \[
   \partial_P\{u,w\}=(-1)^{\operatorname{ord}_P(u)\operatorname{ord}_P(w)}
     \frac{u^{\operatorname{ord}_P(w)}}{w^{\operatorname{ord}_P(u)}}
     \bmod\mathfrak m_P
   \]
   over exact rational-function/finite-field coefficient rings.
2. Use triangular automorphisms and a small full farm polynomial system as controls, computing the product both from global resultants and from local Laurent expansions.
3. Before touching residual-32, derive the finite factors \(R_b(a)\) in the reciprocity identities for \(b=0,1,-1\). Ask for an exact exponent combination in which **every** finite-place factor cancels using only \([f,g]=1\) and pinned normalizations.
4. Only if that cancellation lemma exists, read the remaining infinity valuations and leading units at \(P_1,P_2,B,x\) from the template/tower data and D21/D23 tails, and evaluate the resulting infinity-only symbol relation.
5. Reduce that relation at 105337 and 105673 for screening, derive it over \(\mathbf Q(\sqrt3)\), clear denominators using existing saturation rows, and then ask `msolve` whether it changes residual-32. If step 3 fails, stop; local tails cannot manufacture the missing global resultants.

### Kill criterion

Kill immediately if symbolic elimination shows that every proposed reciprocity equation is just the ordinary divisor-degree/product formula, the Jacobian rows, or one of the six no-log residues. Also kill if every symbol depends on an independently free B/x leading unit that current machinery does not constrain. A failed product caused by truncating before the first unit term is a bug, not an obstruction.

## 8. \(p\)-adic escape-mass balance

**Side:** proof; tower data is summed as measure rather than used as local kill predicates.  
**Score:** \(9\times8\times5=360\).

### Five-line pitch

1. A Keller map has \(|\det J|_p=1\), so it preserves \(p\)-adic volume on every injective analytic chart.
2. After passing to a finite splitting extension, a nonproper degree-\(d\) map must account for \(d\) preimage sheets, including cylinders escaping through infinity.
3. The tower inequalities may organize those escaping sheets into finitely many valuation cylinders with computable Jacobian orders.
4. Sum their positive Haar measures into a rational shell-generating function instead of killing routes one by one.
5. A missing or negative required coefficient rules out the whole genome by change of variables.

### Why this appears genuinely unexplored

A \(p\)-adic approach to JC is not new: [van den Essen-Lipton](https://doi.org/10.1016/j.jpaa.2014.09.018) gives a finite-field/unimodularity reformulation. Motivic/arc-space change of variables is also standard; see [Denef-Loeser](https://arxiv.org/abs/math/9803039). I found no application that converts a candidate JC resolution/tower into a **positive cylinder-mass ledger at infinity**. The campaign's current ledgers count Euler characteristic, branch degree, and residue; none counts Haar mass shell by shell.

### First concrete test this week

1. Before reading a tower JSON, prove the bounded-domain change-of-variables formula with the fiber-multiplicity weight \(N(y)=\#F^{-1}(y)\), first on identity and triangular automorphism controls.
2. Prove a separate realization lemma: a resolved Puiseux cone plus specified angular-component, codimension, and overlap data determines a measurable \(p\)-adic cylinder of measure \((1-q^{-1})^r q^{-\ell(n)}\). A bare valuation vector is not enough.
3. Audit whether the residue-A records at \(P_1,P_2,B,x\), \(\kappa=42\), D21, and `cases/towers/*.json` contain that extra data. If not, state the minimal missing fields rather than assigning a measure.
4. Only after the bridge closes, test whether the leading coefficient reproduces \(td=6=3+3\), then compute two genuinely new shell coefficients symbolically and check them at 105337 and 105673.
5. Verify branch splitting on the chosen residue class (or pass to the required unramified extension), and compare source cylinders with the target series weighted by the actual \(N(y)\). A uniform deficit in this correctly weighted identity is the obstruction.

### Kill criterion

Kill if the realization/change-of-variables bridge fails, or if the promoted tower records do not determine angular components, codimension, Jacobian order, and disjointness without essentially reconstructing the entire polynomial map. Also kill if the full generating function formally collapses to \(td=\sum\Lambda_i\), with every higher coefficient tautological. Never use cancellation in \(K_0(\mathrm{Var})\) as positivity; the proof must survive specialization to honest \(p\)-adic measures.

## 9. Local \(\mathbb A^1\)-degree at infinity

**Side:** proof.  
**Score:** \(8\times8\times4=256\).

### Five-line pitch

1. Ordinary Bezout degree counts preimages, while \(\mathbb A^1\)-degree records a Grothendieck-Witt bilinear form.
2. For a Keller point the local form is controlled by the unit Jacobian; boundary points carry the missing forms after compactification.
3. Resolve the candidate map and compute Scheja-Storch/EKL forms in the local algebras of its infinity branches.
4. The two residue-A pole scales over \(\mathbf Q(\sqrt3)\) may force incompatible discriminant or Hasse data even when integer degree balances.
5. One incompatible Witt class kills the candidate without another coefficient-by-coefficient tower extension.

### Why this appears genuinely unexplored

The broad connection is **not** new. [McKean](https://arxiv.org/abs/2005.09797) relates multivariate Bezoutians to injectivity and explicitly discusses JC, while [Brazelton-McKean-Pauli](https://arxiv.org/abs/2103.16614) identifies Bezoutian, Scheja-Storch, and \(\mathbb A^1\)-degree forms. The narrower novelty claim is the decomposition of that enriched degree into *resolved Newton-Puiseux places at infinity* and its evaluation on a concrete tower genome. I found no such use in the JC literature or campaign.

### First concrete test this week

1. On two triangular automorphisms and one small finite Keller control, compute the quotient algebra of \((f-a,g-b)\), its residue functional, and the Scheja-Storch Gram matrix; verify that rank and determinant agree with the known local degree.
2. Homogenize the first two residue-A tower stages and isolate the local complete-intersection ideals at \(P_1,P_2\) over \(\mathbf Q(\sqrt3)\). Use `msolve` quotient bases or direct Macaulay bases to form multiplication/trace matrices.
3. Compute rank, discriminant, signatures at the real embeddings, and Hasse invariants at several good primes. Track transfer forms when a point is not rational over the base field.
4. Compare the sum of finite Keller forms and boundary forms with the global Bezoutian form dictated by the bidegrees. Use exact Witt-class arithmetic; dimensions alone reproduce old Bezout counts and do not count as success.
5. If a mismatch appears already on the truncated local algebra, prove that deeper tails contribute only hyperbolic summands or otherwise stabilize the relevant invariant before calling it a kill.

### Kill criterion

Kill if the enriched form over the relevant base field is determined solely by ordinary multiplicity and \(J=1\), if localization at infinity is nonisolated in a way not controlled by current tails, or if every discriminant/Hasse invariant depends on unpinned B/x data. Over an algebraically closed field the enrichment largely collapses, so a computation that silently extends scalars to \(\mathbf C\) has killed its own premise.

## Bottom line

If only three experiments are funded this week, run #1, #2, and #4. They have rigorous negative controls, use data already on disk, and return exact algebra even when they fail. Run #3 as the moonshot in parallel: it is the only idea here where one small parameter solution jumps directly from the known 3D failure to an actual plane counterexample. On the proof side, #5 is the best chance of making the promoted tower theorem scale, while #6 is the best chance of extracting a proof-tier certificate from residual-32 without asking F4 to finish its present search tree.
