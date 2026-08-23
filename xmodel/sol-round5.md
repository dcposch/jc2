# Instrument Round 5: from a D23 fiber to a germ test and D25

## Five-line executive summary

1. **FACT:** D23 is nonempty on the promoted radical fiber, but the decisive Jacobian is the Euler/Ore operator obtained by differentiating the original series equation; it is not any scalar Jacobian currently emitted by `valuation_e.py`.
2. **CORRECTION:** the six tail functions split by the exact mod-6 grading into 30 \(u=t^6\) input streams, against 29 η-component output streams; the square block is \(29\times29\), leaving one input stream free, and `pencil/tails` is the closest of the six failed readings.
3. **PROMOTION GATE:** a computed \(e\le 11\) is still only `E_CANDIDATE` until either the Euler terms are conjugated away or a filtered differential Newton lemma plus the completed-ideal bridge is proved; ordinary `DEPTH-STAB.md` does not yet supply that theorem.
4. **FACT/CORRECTION:** \(g_1,g_2,g_3\) are constant-linearly independent; their conormal classes have rank one on lower-dimensional local components at every banked witness, while the mechanism behind the global \(13\to11\) dimension drop remains Conjecture K.
5. **DESIGN:** emit only pristine Row 24, Schur its rank-4 ten-variable frontier to at most five residuals, reduce their base coefficients through the cached 509-element \(G_{23}\), and build the other-35-fiber D23 atlas before launching family-wide D25 solves.

## 1. The exact \(e\)-object

### 1.1 Source map and its six function variables

Fix one reconstructed point \(s\) from `cases/d23_witnesses_p105337.json`, including one of its `deep_draws`. Work over \(k=\mathbb F_{105337}\), with \(R=k[[t]]\), and hold fixed the radical branch, \(A_i,v_{i,34},v_{i,36},W_i,HW_i\), the B-side data, and the dead-stretch data. In particular, \(W_i\) and \(HW_i\) are base/chart units, not function variables.

Put

\[
 P(t)=t^{12}+u_{18}t^{18}+u_{24}t^{24}+u_{30}t^{30},
 \qquad Y=P+t^{32}z.
\]

The six variable tail functions are exactly the six streams made by `build_generators` in `cases/r1_experiment.py`:

\[
\begin{aligned}
z_{f_i}&=A_i+v_{i,34}t^2+v_{i,36}t^4+W_i t^5
       +\sum_{\substack{r\ge6\\r\ne10}} \mathit{tf}_{i,32+r}t^r,\\
z_{g_i}&=A_i+v_{i,34}t^2+v_{i,36}t^4+HW_i t^5
       +\sum_{\substack{r\ge6\\r\ne10}} \mathit{tg}_{i,32+r}t^r,\\
z_{0_i}&=A_i+v_{i,34}t^2+v_{i,36}t^4
       +\sum_{\substack{r\ge6,\ r\ne10\\r\ {\rm even}}}
          \mathit{tg0}_{i,32+r}t^r,
\qquad i=1,2.
\end{aligned}
\]

The coefficient at \(r=10\), level 42, is `PIN42 = 0` in all six streams and is never a tangent direction. The finite \(u_f/v_f\) data and all pole scales are likewise fixed when \(e(s)\) is computed. Thus the correct column mode is `tails`, never `tailsW`.

Let Φ and Γ be the exact normalized cyclic-orbit products from the three f-orbits and six g-orbits, with the B-orbits frozen. The `gm_jet2` constructor computes their pure-y truncation; x-side corrections first enter at \(t^{42}\). With \(\theta=t\,d/dt\), the chosen gauge \(c_fc_g=1\) gives

\[
 \mathcal E(\Phi,\Gamma)
 = (\theta\Phi-12\Phi)\Gamma_\eta
   -\Phi_\eta(\theta\Gamma-18\Gamma)+42t^{20}
 \in R[\eta].                                           \tag{E}
\]

Without that gauge the last coefficient is \(42/(c_fc_g)\). This is the equation in `cases/directionb_strike.py` and `SHEET6-DIRECTIONB.md` §0. Its derivative at \(s\), for a six-tuple \(h\) of tail-function variations, is

\[
\begin{aligned}
D\mathcal E_s(h)={}&(\theta\,\delta\Phi-12\delta\Phi)\Gamma_\eta
 +(\theta\Phi-12\Phi)(\delta\Gamma)_\eta\\
&-(\delta\Phi)_\eta(\theta\Gamma-18\Gamma)
 -\Phi_\eta(\theta\,\delta\Gamma-18\delta\Gamma),       \tag{L}
\end{aligned}
\]

where δΦ and δΓ are obtained by dual-number differentiation of the same orbit-product constructor. Equation (L), not a Jacobian of coefficient rows, is the series-valued Jacobian. It contains θ acting on the unknown functions and is therefore an Euler/Ore differential operator, not an \(R\)-linear matrix.

### 1.2 The deterministic square block

The square-block construction requires the following **all-depth cyclic-character lemma**, not merely a D23 pattern match:

\[
 \mathcal E=\sum_{a=0}^{28}E_a(t)\eta^a,\qquad
 E_a(t)=t^{s_a}H_a(t^6),\qquad
 s_a=6+2((a+1)\bmod 3),
\]

with \(E_{29}=0\) identically and the sole start exception \(s_{28}=16\). It must be proved symbolically from the cyclic orbit selectors for the universal products, including the selected normalized x-side factors from \(t^{42}\) onward, and regressed at finite depths. D23 labels alone do not prove it. Set \(u=t^6\). Subject to that lemma, \(H_0,\ldots,H_{28}\) are the 29 output functions; the 76/86 finite scalar rows are merely their coefficient unpacking.

Split each ordinary tail variation into its six residues modulo 6 and each even `tg0` variation into residues \(0,2,4\). This gives

\[
 4\cdot6+2\cdot3=30
\]

input \(u\)-series. Their initial global-\(t\) shifts are \(r_\rho=6+\rho\), except residue 4 starts at \(r_4=16\), because the would-be \(r=10\) coefficient is pinned. Thus

\[
 \sum_{a=0}^{28}s_a=240,
 \qquad \sum_{c=1}^{30}r_c=288.
\]

This exposes a candidate one-function modulus hidden by the 77 individual coefficient columns; its existence still depends on finite filtered invertibility. For each candidate free stream \(c\), let \(B_c\) contain all 29 output streams and the other 29 input streams. Enumerate \(c\) in the fixed family order

```text
tf1, tf2, tg1, tg2, tg01, tg02; then increasing allowed residue.
```

Discard blocks without a certified finite filtered inverse. Among the rest choose the block with smallest promoted \(e_c\) under §1.3, with the order above as tie-break; if none promotes, report no DEPTH \(e\). This is deterministic; selecting six convenient η rows would define a different, unjustified problem.

For implementation, use

\[
 \theta(t^rZ(u))=t^r(r+6\Theta)Z(u),\qquad \Theta=u\frac d{du}.
\]

After the residue split, \(D(H)_s|_{B_c}\) is a \(29\times29\) matrix over

\[
 k[[u]]\langle\Theta\rangle,
 \qquad \Theta u=u(\Theta+1),\qquad
 L_{aq}=\sum_{m\ge0}u^m(A_{aqm}+B_{aqm}\Theta).           \tag{O}
\]

The affine dependence on the coefficient index that `valuation_e.py` observed is exactly the action of (O), not unknown noise.

### 1.3 Tomorrow's computation and certificate

For every one of the six witnesses and each recorded deep-kernel draw:

1. Reconstruct the named source point using the existing verified `fiber_coordinates_22`, band-pivot, auxiliary, and `deep_tails` data. Make a deterministic zero completion: set `uf30`, the four level-51 tails, the four level-53 tails, every later unspecified tail, and every unspecified normalized x-side coefficient at \(t^{42+}\) to zero, and hash that choice. This is one polynomial representative, not a coordinate-invariant “canonical” completion. The x-side zero choice is admissible for an \(e\le11\) pilot only after the below-12 invariance lemma; an all-depth parametrix must instead be given the actual x-side completion. Do not random-fill future derivatives.
2. Rerun `gm_jet2`/`jrows` over dual numbers to obtain the exact \(A_{aqm},B_{aqm}\) in (O). Assert the 29 support starts above, the raw-label bijection below, `eta29 == 0`, and invariance under a second direct differentiation path.
3. Give the shifted source and target spaces their global-\(t\) filtrations:
   \[
   X_c=\bigoplus_{q\in B_c}t^{r_q}k[[u]],\qquad
   Y=\bigoplus_{a=0}^{28}t^{s_a}k[[u]],\qquad
   F^nM=M\cap t^nM_{\rm ambient}.
   \]
   The operative differential quantity is the **delayed inverse loss**
   \[
   \ell_c=\min\{\ell\ge0:\ 
       F^{n+\ell}Y\subseteq L_c(F^nX_c)\ \text{for every }n\ge0\}. \tag{P}
   \]
   A certificate is an explicit causal delayed solver/parametrix proving (P), with all weighted shifts included. If no finite \(\ell\) exists, put \(\ell_c=\infty\). An unqualified right inverse is the wrong object when a positive delay is present.
4. As a diagnostic, for each truncation \(N\) form the causal \(29N\times29N\) coefficient matrix \(M_c(N)\) from input coefficients \(u^0,\ldots,u^{N-1}\) to output coefficients of the same range, and put
   \[
   \delta_c(N)=29N-\operatorname{rank}M_c(N).
   \]
   Bounded or apparently stable \(\delta_c(N)\) does not by itself prove (P). First derive the finite-memory periodic recurrence and close its initial transient; only then may one complete mod-\(p\) period plus its boundary state certify it. An exact Ore identity/normal form is preferable. Recurring resonance or unbounded defect makes the block fail.
5. If an exact Ore-Popov/Smith-like normal form proves finite diagonal delays, a bounded defect \(d_c\), and a delayed parametrix, compute the determinant-index analogue in global \(t\)-units:
   \[
   e_c^{\rm idx}=6d_c+\sum_a s_a-\sum_{q\in B_c}r_q
                 =6d_c+r_c-48.                          \tag{V}
   \]
   Formula (V) is an index diagnostic, not a theorem for a general Ore operator. Promote it to a DEPTH-compatible \(e_c\) only when the normal form also proves
   \(0\le\ell_c\le e_c^{\rm idx}\), \(e_c^{\rm idx}\ge0\), and the direct global-\(t\) weighted-pivot checksum. Otherwise report \(\ell_c\) as `E_LOSS` and \(e_c^{\rm idx}\) as unpromoted `E_INDEX`. Define \(e(s)=\min_c e_c\) only over promoted blocks. Stop a block once a certified lower bound for either required quantity exceeds 11.

The certificate must contain the witness/deep-draw and zero-completion hashes, free stream, all shifts, operator hash, recurrence/Ore certificate, \(\delta_c(N),d_c,\ell_c,e_c^{\rm idx},e_c\), and the delayed-parametrix identity/inclusions at period boundaries. A finite \(e\le11\) test may omit the \(t^{42}\) x-side correction only after a filtration lemma proves that terms starting there cannot change either (P) or (V) below 12; an all-depth parametrix must otherwise include those corrections.

The surplus bridge lives before numerical evaluation. Let
\[
\mathscr C_s=\varprojlim_N
 \widehat{\left(
 k[\text{tail coefficients of level}<N,\ \text{chart units}^{\pm1}]
 \right)_{\mathfrak m_{s,N}}}
\]
be the inverse-limit completed universal coefficient algebra determined by the chosen witness cylinder. Define

\[
 \widehat I_E=\overline{\bigl([u^j]H_a:0\le a\le28,\ j\ge0\bigr)}
 \subset\mathscr C_s.
\]

Every raw source label must be mapped and checked as

\[
 (n,a)\longleftrightarrow
 \left(a,\frac{n-s_a}{6}\right),
\quad n\equiv s_a\pmod6,
\]

for every depth, and every other purported η component must reduce identically to zero. This is the all-depth cyclic-character/source-generation proof required above, with finite D23/D25 label maps as regressions. There are then no surplus function equations: all 29 \(H_a\) are in the square block, while the orbit/template factorization equations are identities of the parametrization. Radical, saturation, Rabinowitsch, pivot-definition, and `W`-pin rows are base-chart conditions and must not enter \(D\mathcal E_s\). If an emitted Schur/pivot presentation is used instead of reconstructing the source point, it additionally owes explicit localized unit transformations proving equality with \(\widehat I_E\); set-theoretic equality is not enough for this bridge.

Of the six current readings (`pencil|weighted|rank` times `tails|tailsW`), **`pencil/tails` is closest**; `valuation_e.py` already says so. Its corrections are exact and substantial: replace 77 coefficient columns by 30 residue-function streams and a 29-column block, replace random beyond-window fill by dual-jet coefficients at the zero-extended point, and replace truncated Smith on a fictitious series matrix by filtered Ore elimination. `tailsW` wrongly moves fixed chart units; `weighted` and `rank` treat scalar coefficients as independent variables, so their ranks 35/37 do not measure this \(e\). The old unstable sums 135/137 versus 62 are diagnostics of the wrong object, not bounds on (V).

**THEOREM STATUS — CONJECTURE E-HENSEL.** `DEPTH-STAB.md` banks ordinary Tougeron for an \(R\)-algebraic source map; its toy gate does not prove the differential, characteristic-\(p\) statement needed here. A headline follows in either of two ways:

- exhibit an admissible nonlinear change of source coordinates and equations that makes the full map algebraic over \(k[[u]]\) and whose derivative eliminates every Θ term in (O), then use ordinary Smith/Tougeron; a row/column conjugation of the linearization alone is insufficient; or
- prove the filtered differential Newton lemma: a completed-ideal bridge, a derivative with delayed-parametrix loss at most \(e\), and the quadratic remainder estimate imply lifting whenever \(D\ge2e+1\).

The second route is plausible because θ preserves the \(t\)-filtration, but multiples of \(p\) are a real resonance hazard. Until one route is banked, tomorrow's \(e\le11\) is `E_CANDIDATE`, **not yet a certified formal germ**. Once the theorem and bridge gates pass, \(e\le11\) at any D23 witness is indeed the campaign headline.

## 2. What the dimension-drop-two dependency actually is

### 2.1 Two different syzygies were being conflated

Let \(I_{21}\) be the 22-variable D21 fiber ideal. At \(p=105337\), the three exact normal-form conditions are

\[
\begin{aligned}
g_1&=(x_{57}-x_{65})^2uW_1^2+50008x_{53}uW_1+103704x_{72},\\
g_2&=(x_{57}-x_{65})^2uW_2^2+4803x_{58}uW_2+13955x_{72},\\
g_3&=x_{70}+52700x_{72}.
\end{aligned}
\]

The support pattern is identical at all three primes. **FACT:** these three polynomials are constant-linearly independent modulo \(I_{21}\), are already reduced normal forms, and span the three-dimensional compatibility-condition space. In particular, \(g_3\notin I_{21}\). The phrase “one linear dependency among \(g_1,g_2,g_3\)” in the dimension note is therefore false if “linear” means constant coefficients.

The rank-2 factorization directly explains only an earlier dependency. The six D23 compatibility normal forms have

\[
 A=C\operatorname{diag}(uW_1^2,uW_2^2,uW_1^2,uW_2^2),
 \qquad \operatorname{rank}C=2.
\]

Hence `leftker(C)` has dimension four. One left-kernel vector annihilates the inhomogeneous term identically, and the other directions span exactly \(g_1,g_2,g_3\). Equivalently, the four preliminary eliminants \(R_2,\ldots,R_5\) have one exact constant syzygy and reduce to three conditions; at \(p=105337\) it is
\[
 77149R_2+16527R_3+81917R_4+R_5=0.
\]
That is the structural reason for “four becomes three”; it does **not** explain why the maximal dimension falls only from 13 to 11.

### 2.2 Exact local evidence and the structural model

This round's exact witness diagnostics sharpen the dimension-drop statement. At all six witnesses at each of \(105337\) and \(105673\):

- the Jacobian of the original 26-row \(I_{21}\) system has rank 10 in 22 variables, so its Zariski tangent space has dimension 12;
- adding all three \(g_i\) raises the rank only to 11, giving tangent dimension 11;
- each single \(dg_i\) raises the rank by one, while every pair and the triple still raise it by only one.

Thus the conormal classes of \(dg_1,dg_2,dg_3\) have rank one at every witness. Their measured quotient ratios are constant across all six witnesses within a prime:

\[
\begin{array}{c|cc}
p &[dg_2]/[dg_1]&[dg_3]/[dg_1]\\ \hline
105337&29311&42896\\
105673&101767&105528
\end{array}
\quad\text{modulo }\operatorname{span}(dI_{21}).
\]

An independent replay with the 397- and 509-element reduced bases gives the same ranks at \(105337\). **MEASURED/INTERNAL this round:** msolve 0.10.1 gives 553- and 528-element bases for \(I_{21}+(g_1,g_3)\) and \(I_{21}+(g_2,g_3)\); both have dimension 11, but the omitted \(g\) has nonzero normal form. In each tested pair, the omitted equation is not an ideal consequence; equal dimension only says it does not lower the maximal component dimension.

**FACT:** no 13-dimensional component of the globally dimension-13 D21 fiber passes through these witnesses, because their D21 tangent space already has dimension 12. Component selection/non-equidimensionality is therefore load-bearing for the local geometry of the banked witnesses; whether it explains the maximal 11-dimensional survivor component remains conjectural.

**CONJECTURE K (best structural explanation):** there is a 12-dimensional irreducible D21 component \(K\), or its reduced support, carrying the maximal survivors; reaching \(K\) accounts for \(13\to12\), and the D23 obstruction is locally one transverse divisor on \(K\), accounting for \(12\to11\). On \(K\cap V(g)\), two componentwise conormal/depth-ladder syzygies make \([dg_2]\) and \([dg_3]\) multiples of \([dg_1]\). The shared square

\[
 \Delta^2=(x_{57}-x_{65})^2
          = (\mathit{tg2}_{38}-\mathit{tg02}_{38})^2
\]

in the two pole equations, together with the merge bridge \(g_3=x_{70}+\epsilon x_{72}\), makes a pole-channel/τ depth-ladder identity plausible. Rank \(C=2\) alone does not prove it.

Promotion requires an equidimensional/primary decomposition of \(I_{21}\), localization of the witness component \(K\), and a syzygy or conormal-module calculation for \(g_1,g_2,g_3\) modulo \(I(K)\). Saturations or radical equalities must be checked componentwise. That computation should seek polynomial-coefficient syzygies; another constant relation is ruled out.

### 2.3 Does it predict D25?

**FACT:** not as a theorem. Row 24 has nine η components and a rank-4 ten-variable first-occurrence symbol, hence at most five existential compatibility residuals. For a fixed full D23 point, only the six new level-56 variables move, their sub-symbol has rank two, and seven residuals can remain. Neither count inherits the D23 global dimension-drop-two observation.

**CONJECTURE K-D25:** if \(K\) is a genuine depth-ladder component rather than a fiber-specific lower-dimensional component, the five Row-24 residuals should again have conormal rank well below five after reduction on each 11-dimensional survivor component. A bare 22-variable witness is insufficient: first treat the four dormant level-51 values and the remaining D23 lift-fiber coordinates symbolically over each base witness, form the five existential residuals, and measure their **projected** conormal rank after eliminating the reactivated variables; then repeat over each minimal component of \(G_{23}\). If the residual module descends to the 11-dimensional base (\(r=0\)), base-conormal rank 1–2 predicts a 9–10-dimensional D25 projection and rank 5 roughly dimension 6, still not generic emptiness. For \(r>0\), only the eliminated projected maximum-dimension drop supports a base-dimension prediction. A D25 kill would require an exceptional nonlinear incompatibility or unit ideal, not merely “five equations.”

## 3. D25 quotient/Schur compiler and the family lift

### 3.1 The input object is larger than the 509-element basis

Let \(G_{23}\) denote `cases/directionb_det23_gb_p105337.out.txt`: 509 polynomials, 405,524 terms, maximum degree 16, 15.18 MB, in 22 variables. It defines the 11-dimensional **projected base**, not the full D23 coefficient locus.

Over this base, the emitted 82-variable D23 locus has set-theoretic affine reconstruction fibers of dimension 32: the compatibility system solves two of 28 old free directions, leaving 26, and the rank-4 deep block leaves six of ten directions. Thus its reconstructed set has dimension 43; calling it an \(\mathbb A^{32}\)-bundle scheme would additionally require an ideal-level isomorphism not yet banked. The complete formal D23 registry has nine additional coordinates absent from every current row/header,

```text
uf30,
tf1_51, tf2_51, tg1_51, tg2_51,
tf1_53, tf2_53, tg1_53, tg2_53,
```

so its fully registered set has 41 affine reconstruction directions and dimension 52. Row 24 definitely reactivates the four level-51 coordinates. The compiler input must consequently be

\[
 (G_{23},\ \text{sparse source generators},\
   \text{reconstruction DAG},\ \text{dormant registry}),
\]

with hashes, variable order, fiber label, radical branch, and chart units. \(G_{23}\) alone is insufficient.

### 3.2 Exact emission contract

1. **Build only pristine Row 24.** Use `VDEG_CAP=25`, B frozen, and `PIN42`, retaining canonical raw names. Assert Row 23 is identically zero and the nonzero η powers are exactly \(2,5,\ldots,26\). Reproduce the 90-entry first-occurrence digest
   `ab5ee038b118ba6d0b6303c6b2b55b110dc9872c203e1c6b2d60044458e69d29`
   from `cases/sol_algkill.py` before consuming the full nonlinear row. Its `build_frozen(25, front, "ALGKILL")` call is **symbol-only**: it pins every older free coordinate to zero and must never supply the nonlinear payload. Rebuild the full pristine Row-24 payload with every D23/lift coordinate live, pinning only B and the six level-42 streams; feed that live row, not the frozen symbol slice, to Schur and normal form.
2. **Schur the exact frontier.** In order, use

   ```text
   tf1_51, tf1_56, tf2_51, tf2_56,
   tg1_51, tg1_56, tg2_51, tg2_56, tg01_56, tg02_56.
   ```

   The \(9\times10\) symbol has uniform rank four; certified unit pivots are `tf1_51,tf1_56,tf2_51,tf2_56`. For existential projection, all ten coordinates participate and Schur gives five compatibility rows \(c_{24}=L_{24}b_{24}\), plus a saved six-dimensional frontier kernel and solve map. For extension of one fixed D23 point, level 51 is fixed and the six new level-56 columns have rank two, so use seven compatibilities instead. Never mix these two questions.
3. **Replay the lift manifest.** Choose the 21 old band-free coordinates

   ```text
   x18..x23, x26..x31, x33..x36, x38..x41, x48,
   ```

   plus `x16,x24,x69`. Free `x32,x37` and recover `x17,x25` with the certified unit \(2\times2\) minor. Reconstruct the 22 band pivots in reverse at-use order. Choose six Row-22 deep-kernel coordinates and solve four. Of the nine old dormant coordinates, the frontier now owns the four level-51 tails; separately register `uf30` and the four level-53 tails, plus the four possible new level-55 tails in the D25 registry. Substitute this DAG only into the five Schur compatibility rows, never into all nine pristine rows.
4. **Reduce coefficientwise.** Write each residual as
   \[
   c_j(z,a)=\sum_\alpha c_{j,\alpha}(z)a^\alpha,
   \]
   where \(z\) are the 22 det23 variables and \(a\) are unresolved lift variables. Reduce every \(c_{j,\alpha}\) modulo \(G_{23}\); keep the \(a\)'s as polynomial variables, never as an invertible coefficient field. Use a leading-monomial divisibility index and cache by `(basis hash, monomial order, polynomial hash)`. Reduce after each DAG substitution, strip only recorded \(W\)-unit content, and Schur a newly exposed affine block only after a constant/unit-rank certificate. Otherwise retain it or cover every determinantal rank chart.
5. **Emit control and quotient from one source.** The rank-complete control is the full D23 fiber plus all nine pristine Row-24 components: 81 equations and between 92 variables (the guaranteed existing 82 plus the ten frontier coordinates) and the 101-variable full-registry ceiling. The nine possible coordinates beyond 92 are `uf30`, the four level-53 tails, and four ordinary level-55 tails; the nonlinear occurrence census, not the registry alone, decides which enter. The sparse quotient target is the 26-row, 5,348-term D21 fiber core plus \(g_1,g_2,g_3\), totaling 29 rows and 5,360 terms, followed by \(s\) nonzero reduced D25 residuals, \(0\le s\le5\). Its honest shape is \((22+r)\) variables/\((29+s)\) equations. Only when \(r=0,s=5\) is it 22 variables/34 equations; fewer residuals are smaller, not a failure. A rank-complete pre-Schur quotient is \((32+r)\) variables/38 equations.

Use the 509-element basis as a normal-form engine; do not prepend its 405,524 terms to an ordinary F4 solve. Accept a quotient point only after reconstructing every eliminated and dormant coordinate and checking every pristine D23 and Row-24 row.

Required gates are exact source/GB/order/fiber hashes; affine, rank, and chart-unit certificates; absence of removed variables; raw-versus-quotient random evaluation; backsolve at all six witnesses per prime (all 12 for the two-prime replay); replay of every pristine Row-24 row; τ and all \(h\)-sign branches; \(W\)-chart saturation; the `+42` mutation; cross-prime support; and every rank boundary.

### 3.3 Size, runtime, and stopping rules

**LOCAL MEASUREMENT (current workstation, not yet a banked benchmark):** a read-only Python/FLINT parse loaded all 405,524 terms of \(G_{23}\) in 1.95 seconds with 105.4 MiB peak RSS. The banked D23 raw build took 5,587 seconds; its raw Row-22 block has 35,988 terms, while the rejected “substitute before Schur” route reached 4,971,007 terms.

**ESTIMATE:** pristine Row 24 will contain roughly 40,000–200,000 terms; the full control should be about 100,000–260,000 terms or 2–10 MB. The existing nonincremental Python builder may take 1–4 hours; a slot-incremental cached series builder should take 5–30 minutes. **CONJECTURE:** Schur plus coefficient normal forms will take seconds to a few minutes and stay below 1 GB if both the intermediate and final reduced blocks stay under 100,000 terms. Preflight one residual and meter intermediate terms/RSS: warn at 100,000 terms or degree 16; stop expansion at 250,000 terms and retain the hybrid/DAG representation.

**CONJECTURE RUNTIME:** if \(r\le5\) and the final sparse input is at most 50,000 terms, a 30–60 minute F4 pilot should either finish or expose the next cliff. No “minutes-cheap” completion claim is justified before that pilot.

### 3.4 Reuse across the other 35 fibers

The raw Row-24 generator, dormant registry, rank-4 polewise factorization, Schur code, reconstruction topology, and normal-form compiler are reusable across the \(3\cdot3\cdot2\cdot2=36\) finite radical components. A specialized D23 ideal/basis is not: identical counts or leading-monomial profiles do not prove an isomorphism between fibers. Cross-prime-identical staircases permit reuse of an operation skeleton only with replayed coefficient-cancellation and support guards.

Split the family computation into two tiers. The cheapest meaningful first statement is:

> **Tier-1 target at \(p=105337\):** every one of the 36 finite radical components has a proper D23 projection of dimension 11 (a maximal-dimension drop of two from its D21 fiber) and the same initial staircase; replay the already structural rank-4 Row-24 factorization on every specialization as a gate.

Merely proving the union nonempty adds nothing to the promoted one-fiber result. Build a 36-fiber D23 normal-form/GB atlas first, hash the feature matrices, and search for an explicit transport between fibers. Baselines are about 11 seconds for a D21 fiber and 63 seconds for representative det23; if they persist, the other 35 components have a solver-only lower bound of about 43 serial minutes per prime. Final G23 files alone cost about 0.53 GB per prime; a reproducible atlas retaining the D21 bases is already at least about 0.9 GB per prime before emissions, logs, dimension, conormal work, and I/O. Three primes therefore mean roughly 2.2 serial job-hours, not 2.2 CPU core-hours, plus those omitted costs.

Repeat at \(105673\) only after the first atlas is understood. **Tier 2** then adds rational witnesses or componentwise conormal-module calculations to test the dependency signature; it is not part of the 43-minute baseline. Finally specialize the five Row-24 residuals over the atlas and compare \(r\), support, degree, and projected conormal rank. Do not launch 36 D25 F4 jobs before that comparison.

All statements in this section remain mod-\(p\), B-frozen, no-log, and chart-local. The finite-fiber atlas is the cheapest family-level lift; it is not yet a characteristic-zero or global-chart theorem.
