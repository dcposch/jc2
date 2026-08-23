# Sol independent generative round — 2026-08-21

**Independence and scope.** This list was derived from a fresh pass over the repository and direct replay of the emitted D25 equations; it is not organized from, or against, a Fable list. “VERIFIED” below means exact for the two current emitted modular presentations, at $p=105337$ and $p=105673$. It does **not** by itself promote emission fidelity or a characteristic-zero statement. The decisive triangular transcript is a fresh read-only computation and should be banked and independently replayed before it is cited as a repository theorem.

**Scoring.** Impact and feasibility are each on a 1–10 scale; the displayed product is the ranking score. Every unproved mathematical or performance assertion is explicitly labelled **CONJECTURE**.

## Five-line executive summary

1. **D25 is already decided at the registered modular scope:** every parked fiber and both selector unions are NONEMPTY of dimension 14, not the pre-registered 13; the projected base has dimension 10, so the compatibility pair has height one, not two.
2. **No large Gröbner basis is needed:** two lift pivots and eight Laurent-unit base pivots identify each parked D25 scheme with 16 disjoint copies of $\mathbb A^{14}_{\mathbb F_p}$; independently, an all-$x$-zero four-coordinate point annihilates all 34 parked and all 38 union rows at both primes.
3. **The carrier mechanism survives qualitatively but misses numerically by one:** $H:q^\infty=H$ has base dimension 10, while $H+(q)$ has dimension 9; every top component meets the $q$-open carrier and $q=0$ is a genuine divisor.
4. **The proposed “36 character systems” split is not valid:** the 36 labels are primitive idempotent fibers, whereas character spaces multiply into one another; the valid uses are exact torsor untwisting to one fiber and 36 character blocks inside each union F4 linear-algebra batch.
5. **Operational priority:** bank the tiny pivot/reconstruction certificate, stop treating the 48-hour union jobs as verdict lanes, and add a quotient/pivot compiler; retain Hilbert, degeneration, and trace methods only as certificate fallbacks or D27+ infrastructure.

## Ranked list

### 1. Exact D25 Schur–Laurent triangular certificate — VERIFIED — impact 10 × feasibility 10 = 100

This is the answer to the current D25 question. In a parked fiber, write the five residuals as affine forms in the six lift variables

\[
(x33,x38,x16,x19,x24,x27).
\]

The minor of residual rows $R_1,R_2$ in columns $x33,x38$ is

\[
75772\,uW1^2uW2^2\pmod {105337},\qquad
9899\,uW1^2uW2^2\pmod {105673}.
\]

It is a unit on the emitted Laurent chart. Thus $R_1,R_2$ solve $x33,x38$ exactly, the four other lift variables are free, and the other three Schur compatibilities have rank two after the known identity

\[
R_2+6R_3+30R_4+144R_5=0.
\]

One especially sparse compatibility basis is:

```text
p=105337
hcore = x72*x53*uW1 + 76812*x72*x58*uW2 + 103071*x72^2
        + 56654*x55*uW1 + 42591*x60*uW2
hlin  = 19253*x72^2 + 101463*x71 + 3874*x73

p=105673
hcore = x72*x53*uW1 + 92223*x72*x58*uW2 + 85924*x72^2
        + 83637*x55*uW1 + 28534*x60*uW2
hlin  = 4330*x72^2 + 48619*x71 + 57054*x73
```

These two rows are already normal modulo the stored D23 basis. In the sparse 22-variable base presentation, successively solve the unit-linear pivots

\[
x71, x55, x70, x53, x58, x52, x47, x54
\]

from `hlin`, `hcore`, and zero-based source rows `28,26,27,10,11,13`, reducing $W_i uW_i=1$ after every substitution. The ten untouched base variables are

\[
T=(x57,x59,x60,x62,x63,x65,x66,x68,x72,x73).
\]

All remaining source equations vanish except the two inverse rows and six trinomials in $(U,V,1)=(W1^4,W2^4,1)$. Their coefficient matrices are

\[
\begin{array}{c|ccc}
&U&V&1\\ \hline
\multicolumn{4}{c}{p=105337}\\
&81190&11537&71983\\
&21068&40041&102675\\
&91127&14342&11531\\
&102882&73079&60568\\
&86415&37898&45675\\
&29262&89263&75336
\end{array}
\quad\leadsto\quad
\begin{pmatrix}1&0&47664\\0&1&52125\\0&0&0\\\vdots&\vdots&\vdots\end{pmatrix},
\]

and

\[
\begin{array}{c|ccc}
&U&V&1\\ \hline
\multicolumn{4}{c}{p=105673}\\
&62322&85289&102850\\
&97729&25028&7845\\
&65138&63462&50448\\
&57279&19175&12220\\
&20272&17266&48552\\
&37031&29570&71293
\end{array}
\quad\leadsto\quad
\begin{pmatrix}1&0&61274\\0&1&13635\\0&0&0\\\vdots&\vdots&\vdots\end{pmatrix}.
\]

Therefore

\[
(W1^4,W2^4)=
\begin{cases}
(57673,53212),&p=105337,\\
(44399,92038),&p=105673.
\end{cases}
\]

The exact base quotient is

\[
\mathbb F_p[T,W1^{\pm1},W2^{\pm1}]/
(W1^4-c_{1,p},W2^4-c_{2,p}).
\]

Both constants are nonzero fourth powers and $p\equiv1\pmod8$, so this is 16 copies of $\mathbb F_p[T]$. Restoring the four free lifts gives

\[
V_{25,\ell}\simeq\coprod_{16}\mathbb A^{14}_{\mathbb F_p},
\qquad
\#V_{25,\ell}(\mathbb F_p)=16p^{14}.
\]

The 36-selector union is consequently 576 copies of $\mathbb A^{14}$, with exact point count $576p^{14}$. In particular it is reduced, smooth, NONEMPTY, and has dimension 14. The five D25 residuals have total effective codimension three—two lift solves plus a height-one compatibility cut—not the pre-registered four. Thus **CONJECTURE ECO-D25 is refuted at both registered primes**.

There are two independent checks already completed in this round:

- Singular 4.4.1 on the raw 29 D23 rows plus `hcore,hlin` finished in about 1.4 seconds at each prime, returned a proper 630-element standard basis, and reported base dimension 10.
- Eliminating two obvious compatibility pivots first gave a 20-variable presentation whose `std` and `slimgb` bases both had 158 elements and dimension 10, with mutual normal forms zero.

The bankable proof object should be the ten-pivot reconstruction DAG, the $6\times3$ terminal RREF, and zero remainders for the original rows—not the 630-element basis.

### 2. Finish the D25 carrier interpretation by one terminal linear form — VERIFIED — impact 9 × feasibility 10 = 90

The unexpected extra dimension is not a boundary artifact. For the `a00pp` carrier

\[
q=x70(x65-x57)+A(x54-x63)+B(x59-x66),
\]

put $Z=W2^2uW1^2$. The triangular reduction gives

\[
\begin{aligned}
p=105337:\quad \bar q&=(24129Z+100248)
 [(x59-x66)+8603x72(x57-x65)],\\
p=105673:\quad \bar q&=(6523Z+44573)
 [(x59-x66)+96695x72(x57-x65)].
\end{aligned}
\]

The terminal equations say $Z^2=87046$ and $Z^2=847$, respectively. The first factors are units: their norms are 23212 and 2824, both nonzero. Hence $q$ is associate on every one of the 16 branches to a monic linear polynomial in the free coordinate $x59$. It follows scheme-theoretically that

\[
H:q^\infty=H,\qquad \dim H=10,\qquad \dim H+(q)=9.
\]

An independent direct Singular computation of the raw 29 rows plus `hcore,hlin,q` returned dimension 9 and basis size 346 at both primes. After restoring $\mathbb A^4$, the full $q$-open closure has dimension 14 and the nonempty boundary has dimension 13. Thus every maximal D25 component still meets the D23 carrier, and the boundary is a divisor. The qualitative carrier story survives; the registered numerical pair $(9,\le8)$ is refuted by exactly $+1$.

This also gives exact carrier point counts per parked fiber:

\[
\#(q=0)=16p^{13},\qquad
\#D(q)=16(p^{14}-p^{13}).
\]

### 3. Add a certificate-producing Laurent pivot pass to the quotient compiler — impact 9 × feasibility 9 = 81

The prior quotient/Schur idea is not new. The new software increment is to continue automatically through chart-unit linear pivots and emit a reversible certificate rather than hand a dense inherited basis to F4.

The pass should:

1. detect variables occurring affinely in the new residual block;
2. compute the coefficient matrix, constant left kernel, and chart-unit minors;
3. emit compatibility rows and certify both inclusions of their span;
4. find scalar-times-Laurent-monomial pivots, substituting through a DAG while canonicalizing $W_i uW_i=1$ after each step;
5. retain source-row IDs, pivot units, inverse formulas, and zero-remainder checks;
6. reverse-reconstruct the eight base pivots and then
   
   \[
   x33=(bs-er)/\Delta,\qquad x38=(dr-as)/\Delta
   \]
   
   from $R_1=ax33+bx38+r$ and $R_2=dx33+ex38+s$;
7. emit the final constant matrix/RREF, sparse witnesses, Jacobian minors, and pristine-row evaluation transcript.

Measured here, the full eight-base-pivot replay takes below 0.1 seconds and negligible memory; the terminal object is 8 rows, 14 variables, and 22 terms. **CONJECTURE (engineering):** a production FLINT/Singular implementation is only a few hundred lines, and the same pass will turn many D27+ “new residual over an old survivor” jobs into small Fitting/triangular problems before Gröbner machinery starts.

This also diagnoses the parked-fiber miss: the PF1 experiment prepended the 509 dense D23 basis elements and asked F4 to solve 514 rows. It did not test the raw 34-row parked representative. For current D25, neither should now be run: the exact 31-row base quotient and then the triangular DAG dominate both.

A cheap first stage should also try structured sparse ansätze, especially all non-chart variables zero. It would have found the following exact witnesses immediately:

| prime | selector tuple $(A1r,A2r,h1r,h2r)$ | $(W1,W2,uW1,uW2)$ | exact checks |
|---:|---:|---:|---|
| 105337 | $(50630,10114,50267,50267)$ | $(31931,9457,64754,22756)$ | all 34 parked and all 38 union rows vanish |
| 105673 | $(38664,46664,35053,35053)$ | $(8021,20111,13662,64399)$ | all 34 parked and all 38 union rows vanish |

Every `x*` coordinate, including all six lifts, is zero at these points. The parked Jacobian ranks are 14 in 28 variables and the union ranks are 18 in 32 variables. The same parked $14\times14$ minor has determinant 9870 and 39560 at the two primes. The sparse witnesses alone settle NONEMPTY; the triangular certificate settles the global dimension and scheme structure. Notice that these particular sparse points lie on $q=0$, although their components do not.

### 4. Untwist the selector torsor before any union Gröbner computation — impact 9 × feasibility 8 = 72

This is the correct nonlinear use of the promoted equivariance theorem. In the 36-point selector algebra, normalize the selector coordinates at `a00pp`:

\[
\alpha=A1r/A1_0,\quad \beta=A2r/A2_0,\quad
\eta=h1r/h1_0,\quad \theta=h2r/h2_0.
\]

They are units satisfying the appropriate order-three/order-two laws. If $x_j$ has character $(a,b,u,v)$, introduce

\[
y_j=\alpha^{-a}\beta^{-b}\eta^{-u}\theta^{-v}x_j
\]

and divide each row by its row-character unit. Exact covariance on all 36 reduced selector points implies equality in the selector algebra, so the transformed union is

\[
B_{36}\otimes_{\mathbb F_p} I_{a00pp},
\]

not merely a collection of equidimensional-looking fibers. This turns an equivariant 32-variable union job into one representative solve plus four finite étale selector laws, without emitting 36 specializations and without nonlinear Fourier fiction.

The algebraic reduction is a corollary of the promoted theorem. **CONJECTURE (performance):** implementing this variable normalization in `d25_assemble.py` will give an order-of-magnitude reduction for future union jobs whose representative does not itself triangularize.

### 5. Replay the tiny terminalization over the source number field — CONJECTURE — impact 10 × feasibility 7 = 70

Two modular fibers do not prove a characteristic-zero D25 statement. They do, however, expose a much cheaper bridge than rational Gröbner reconstruction.

Build the `a00pp` system over the actual selector/radical number field, untwist the torsor first, and replay exactly the same ten pivots. The proof obligations are only:

- the lift determinant has nonzero number-field norm;
- each of the eight base pivot coefficients has nonzero norm;
- the terminal six rows have rank two in $(W1^4,W2^4,1)$;
- their solved fourth-power constants are nonzero; and
- every pristine source row reduces to zero through the recorded DAG.

If those gates pass, the characteristic-zero emitted scheme has dimension 14 and a finite étale $W$-factor after adjoining fourth roots. If a norm vanishes, the modular collapse is exceptional and the precise failed pivot identifies why. **CONJECTURE:** the identical support, pivot sequence, terminal rank, and smooth points at two split primes reflect a characteristic-zero triangular identity rather than two coincidences. This route should be attempted before any characteristic-zero F4 run.

### 6. Stop F4 on a dimension sandwich, not on a completed basis — impact 8 × feasibility 8 = 64

Maintain the monomial ideal $M$ generated by every provenance-bearing leading monomial produced after a completed F4 batch. Since

\[
M\subseteq\operatorname{in}(I),
\qquad
\dim R/I\leq\dim R/M,
\]

the height of $M$ is a rigorous upper-bound certificate. For a monomial ideal its height is the minimum hitting-set size of the supports of its generators, so the callback is a small hypergraph computation.

For the D25 base, height 12 in 22 variables proves dimension at most 10. A certified ten-parameter family, or the 16-state border algebra below, proves dimension at least 10. Once the bounds meet, stop: no reduced basis and no later critical-pair rounds are needed. After eliminating `x71,x55`, the corresponding target is height 10 in 20 variables.

The certificate must use leading terms from one genuine global term order. A coefficient-field projection, or independently chosen terms from different orders, is not valid. This corrects a tempting but false shortcut: a purported raw-LT height 11 in the 20-variable eliminated ring is impossible when the verified quotient dimension is 10.

### 7. Use a 16-state border-basis replay as the independent dimension checker — impact 7 × feasibility 9 = 63

Over $K=\mathbb F_p(T)$, the terminal algebra has basis

\[
\{W1^aW2^b:0\le a,b<4\}.
\]

Store the two $16\times16$ multiplication matrices. Check that they commute, satisfy the two quartics and inverse relations, annihilate every terminal/source generator after back-substitution, and preserve the cyclic vector 1. A nonzero finite $K$-algebra simultaneously proves that the ten parameters are algebraically independent in the quotient and that the generic fiber is zero-dimensional. This is a compact checker with very different failure modes from Singular and a much more informative artifact than a Hilbert-function plateau.

For a future D25-like system that is finite over the old degree-80 D23 Noether chart but does not triangularize, a related **CONJECTURE** is to form multiplication matrices $M_{h_1},M_{h_2}$ and the norm pencil

\[
N(s)=\det(M_{h_1}+sM_{h_2}).
\]

The coefficients of $N(s)$, or more robustly the Fitting ideal of the joint cokernel, describe where $h_1,h_2$ share a fiber zero. Black-box determinant evaluation/interpolation may expose structurally why an apparent two-row obstruction has height one. The current 16-state terminal algebra makes that expensive degree-80 experiment unnecessary here.

### 8. Character-block F4 and invariant-only emptiness sidecar — impact 8 × feasibility 6 = 48

The emission names do reveal a diagonal $G=(C_3)^2\times(C_2)^2$ action, but the proposed conclusion needs correction.

- The 36 labels are the primitive idempotent/evaluation factors of $B_{36}$. Those are 36 actual specialized ideals, already known to be isomorphic by promoted equivariance; solving all 36 is redundant.
- The Fourier monomials are the 36 character spaces. They are not ideals because $R_\chi R_\psi\subset R_{\chi\psi}$. Therefore there are no 36 independent nonlinear “character-isotypic systems.”
- The exact grading lives in the 32-variable union before selector specialization. A scalar parked fiber generally loses it because selector coefficients supplied part of each row’s weight.

The valid solver acceleration is linear-algebraic. Every F4 multiple and S-polynomial is homogeneous in total character, so each union Macaulay matrix permutes exactly to

\[
M_d=\bigoplus_{\chi\in\widehat G}M_{d,\chi}.
\]

Bucket rows and columns by a 0–35 character ID after symbolic preprocessing, reduce the blocks independently, then merge pivots in global monomial order. The reported $278\text{k}\times753\text{k}$ matrix would have average blocks near $7.7\text{k}\times20.9\text{k}$, although a histogram must be measured because balance is not guaranteed. **CONJECTURE (performance):** memory drops close to the number of occupied balanced blocks and arithmetic improves superlinearly; implementation requires an msolve/Groebner.jl backend change.

For an emptiness-only search, 1 has trivial character. Reynolds averaging shows that a Nullstellensatz certificate can be chosen in total character zero, so a sidecar may build only that Macaulay block and retain sparse cofactor provenance. A hit is an exact unit certificate; a miss is inconclusive without a degree bound. **CONJECTURE:** for some future empty union the trivial block reaches 1 well before a full GB finishes.

### 9. Certified Hilbert-series truncation on the compressed quotient — CONJECTURE — impact 6 × feasibility 5 = 30

A visible Hilbert-function plateau is not a dimension proof. A finite truncation becomes exact only with a persistence certificate: a proven regularity bound, Gotzmann/Macaulay equality in the required range, or an involutive/border closure proving all next-degree prolongations reduce.

If an independent D25 check is still wanted, homogenize the 22-variable compatibility quotient—not the 32-variable union—and compute sparse Macaulay ranks degree by degree. Either saturate by the homogenizer or show that any extra component at infinity is already below the target dimension. Character blocks can accelerate this only in the unspecialized union; the parked quotient instead benefits from the pivot compression.

For current D25 this is dominated by the explicit terminal algebra, whose weighted Hilbert series and dimension are immediate. Its value is as a generic fallback when triangular pivots stop but a full GB remains excessive.

### 10. Search for a tiny weighted degeneration certificate — CONJECTURE — impact 7 × feasibility 4 = 28

Use the derived sparse consequences, not the raw generators, and solve a small linear-programming problem for a weight vector whose selected initial monomials include twelve dependent-variable pure powers. If the ideal generated by those initial forms has dimension 10, then

\[
\langle\operatorname{in}_w(f_i)\rangle
\subseteq\operatorname{in}_w(I)
\]

gives the required upper bound; a ten-parameter component gives the lower bound. The certificate is just the weight vector, the derived polynomials with provenance, and a height-12 monomial cover. Pairwise-coprime leading monomials can reduce the Buchberger check to product criteria.

This is effectively what the current triangular presentation has already achieved by coordinate elimination. **CONJECTURE:** an ILP search over pivot-derived supports can find similarly small degenerations at D27 when literal unit pivots no longer finish the system.

### 11. Replace single-center WTC by a normalized multi-Rees/b-divisor inequality — CONJECTURE — impact 9 × feasibility 3 = 27

The current WTC lane still tries to transport each packet to one ordinary pencil center and then prove concentration. A genuinely different target is the normalized multi-Rees algebra of the two residual pencil ideals. Its exceptional primes are canonical Rees valuations, so chart descent and center identity are absorbed into one birational object rather than proved packet by packet.

Record each packet as a valuation vector on that normalized blowup. Then seek the PCC square mass as a mixed-multiplicity or nef b-divisor intersection inequality. This would permit a packet to remain a cluster vector and could bypass **CONJECTURE WTC-ORD** as a single-center concentration statement; the price is a new global inequality strong enough to control the quadratic energy directly.

The nearest prior route is “complete ideals and proximity.” The new reframe is logical, not terminological: do not use complete ideals to prove WTC-1 and then PCC-COVER; use the paired normalized multi-Rees space to formulate and prove the global inequality without WTC-1. The first finite test is one integral Corollary-7.4 trace: compute its two Rees-valuation vectors and verify that their intersection contribution matches the packet energy predicted by WTC-VEC.

### 12. Turn PCC-COVER into an exact convex-dual certificate search — CONJECTURE — impact 8 × feasibility 3 = 24

Once an occurrence forest and proximity matrix exist, encode all allowed center identifications, capacities, and branch-divergence rules as a finite integer convex program minimizing

\[
\sum_p c_p^2
\]

subject to the certified packet data. Its rational SOCP/SDP relaxation has a dual. A successful dual solution can be reconstructed exactly as a sum-of-squares/proximity-potential telescope proving $\sum c_p^2\ge B^2-1$; a violating primal solution identifies the precise missing Keller constraint instead of merely returning another scalar countermodel.

This does not solve WTC-CHART or occurrence completeness, and an unexplained numerical optimum proves nothing. Its role is proof discovery for the isolated residual-energy wall: search small faithful forests, rationally reconstruct stable dual multipliers, and then prove the resulting symbolic local inequality by induction on branch divergence.

### 13. Trace and Lang–Weil are the wrong primary D25 test — impact 3 × feasibility 4 = 12

For current D25, exact point counts are already available:

\[
16p^{14}\quad\text{per parked fiber},\qquad 576p^{14}\quad\text{for the union}.
\]

No estimate can improve that. More generally, zero $\mathbb F_p$-points does not imply geometric emptiness, and Lang–Weil becomes decisive only after effective degree and absolute-irreducibility control—the hard information the proposed estimate was meant to avoid. Direct random sampling in a codimension-14 ambient presentation is also hopeless.

The useful trace variant is a generic-function-field or sliced quotient: build a finite algebra, prove it is nonzero, and use multiplication/Frobenius matrices to detect extension-field points when no rational point exists. A single reconstructed algebraic point is a one-sided exact NONEMPTY certificate. Failure to find one remains probabilistic unless a complete border basis or effective bound is supplied. This is sound fallback infrastructure, not a competitive current lane.

## What not to relaunch or call new

- The $36\to1$ representative reduction, the 18/6/3 coefficient-class census, and idempotent-vector normal forms were already banked; the new symmetry work above is torsor **untwisting** and within-F4 character blocks.
- Generic quotient/Schur compression, term-order portfolios, `-q1/-l44`, more primes, larger machines, Magma/FGb/Groebner.jl/slimgb races, and telemetry were already proposed. The new computational object is the exact D25 compatibility pair followed by the Laurent pivot/reconstruction DAG.
- The 514-row PF1 lane is not evidence that the raw parked system is hard; it solved a different, densely padded presentation.
- The two 48-hour union runs are now useful only as solver-stress telemetry. A timeout or `rc=124` changes none of the exact modular conclusions above, and no replacement union GB should be launched for the D25 verdict.
