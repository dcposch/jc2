# Independent gate: 189 universal C pivots and the complete residual contract

2026-09-06. Reviewer: Opus 5 (different model). Producer: Astra,
xmodel/linear-c-filtered-pilot-astra-20260906.md, full SHA
dbfa3716deb005f68858984ffab01d1897ebc64e0c0f56b2d0062628497a4119 (verified,
body 14,380 B / 5a56fbd1eb5d258a11fe1a1d14198c8c1f1b115ee4f44fb7080ee4a68c82389f).
All ten charged receipt hashes in /tmp/jc2-lane.1CmqE8/inputs match the repo
copies. No worker launched, terminated or retagged; no solve; no ideation
submission, live Fable gate, live Sol report/log, jc2-lean or shared ledger
read; no shared ledger or charged artifact edited.

Method: I did NOT reuse producer code for the mathematics. Every quantitative
claim below was recomputed from the frozen source JSON and the certificate with
my own parser, echelonization and Jacobian-coefficient derivation (a third
index convention, derived directly from C_X G_W - C_W G_X). The producer's own
verifier was additionally replayed and mutation-tested (Claim 4).

| # | Subject | Verdict |
|---|---|---|
| 1 | Source C map, kernel lemma, 189 actual pivots, universal minor | **CONFIRMED** |
| 1b | "247 other syntactically occurring physical coordinates" | **REFUTED** (245 / 241) |
| 2 | Exact quotient graph map, both directions, retained residual | **CONFIRMED** |
| 2b | Nominal 250 / 410 / 1440 presentation counts | **GAP** (unreproducible) |
| 3 | Highest face: ranks 8,7; degree-68 injectivity; reduced locus | **CONFIRMED** |
| 4 | Cost/certificate scope statements | **CONFIRMED** |
| 4b | Producer's pivot and selected-only negative controls | **REFUTED** (vacuous) |

No exit-price assertion is made by this review.

## 1. Actual source C map, kernel lemma, and the 189 constant pivots

**CONFIRMED.** Independent recomputation from delta2_stage8.strongest.json:

- The A3 map has 201 rows at 201 distinct physical positions p=(98-r-z,z);
  every row parses as a **homogeneous linear** form over Q in exactly 192 names
  with **zero affine offset** and no nonlinear product. Physical degrees run
  0..35, so deg C <= 35 holds on the nose.
- **Injectivity is certified twice.** All 192 parameters have an exclusive
  coefficient-1 identity slot (so 192 of the 201 positions are permutation
  slots), and my own exact Q elimination on the 201x192 matrix returns
  rank 192.
- Disjointness from h3,C2,C3,B2 holds: the intersection is empty.
- **The count 247 is wrong (REFUTED).** The set of names occurring
  syntactically in the h3,C2,C3,B2 maps has **245** elements, of which **241**
  match a physical slot pattern `Xc_i_j` (B2 182, C3 31, C2 25, H 3) and 4 are
  gauge scalars (E82, minor_a2, rho, u), which are not "physical-source
  coordinates". A third natural reading, full_free_coordinates minus the 192,
  gives 252. No reading gives 247. Separately, `target_a`/`target_b` occur only
  in `degree_premap` and are in none of these sets, yet F, G and K need them,
  so the base ring A owes two more generators. This is a bookkeeping defect
  only: the reduction is A-linear for whatever A actually is, so nothing
  mathematical downstream moves.

**Physical normalization.** The premise that makes the whole construction
universal is not assumed, it is forced: the degree-11 part of the h3 map is
literally {(3,8):1,(2,9):3,(1,10):3,(0,11):1} with **constant, parameter-free**
coefficients, i.e. exactly H=(X+W)^3W^8. Hence h_top=H^3 and G_top=H^6 at
*every* point of the base, and deg(G-G_top) <= 65. I also verified the stated
algebra symbolically: J(F,G) - K - J(C,G) = 0 identically for
F=h^3+(3D+a)h/2+C, G=h^2-bh/3+D, K=((3D+a+bh)/2)J(h,D). Top degrees measured
from the source: h3 11, C2 14, C3 14, B2 34, A3 35, so deg h=33, deg G=66,
deg J(F,G) <= 99.

**Homogeneous Jacobian kernel lemma (char 0), proof.** Let P be homogeneous of
degree l over a field k of characteristic 0 with J(P,H^6)=6H^5 J(P,H), so
J(P,H^6)=0 iff J(P,H)=0. Euler gives X P_X + W P_W = l P and X H_X + W H_W =
11 H. On the open set where the Euler vector field is nonzero, J(P,H)=0 forces
the gradients to be proportional, and contracting both Euler relations against
that proportionality yields 11 H dP = l P dH, i.e. d(P^11/H^l)=0. In
characteristic 0 a rational function with vanishing differential is constant,
so P^11 = c H^l. Comparing (X+W)- and W-valuations of both sides gives
11 ord_{X+W}(P) = 3l and 11 ord_W(P) = 8l, so 11 | l and P is a scalar multiple
of H^{l/11}; conversely J(H^m,H)=0. The kernel is therefore 1-dimensional
exactly when 11 | l and 0 otherwise. I checked this computationally for every
l = 0..40 (nullity equals 1 iff 11|l, no exceptions), with J(H^k,G_top)=0 for
k=0..3 as positive controls and J(X^11,G_top) != 0 as the negative control.
The proof uses characteristic 0 twice (Euler, and constancy of a closed
rational differential); it is not a characteristic-free statement.

**Actual 189 pivots, not the general 188 bound. CONFIRMED.** Rebuilding the
filtration-adapted subspace from the raw source with my own descending-degree
column echelonization reproduces the certificate exactly:

- degree profile **byte-identical** to the certificate's 36 rows; dimensions
  sum to 192, ranks to 189, kernel slots to 3;
- kernel-deficient degrees are exactly {22, 11, 0}; **degree 33 has dimension 9
  and rank 9**;
- 189 active pivots at 189 distinct output positions of degrees 65..99, and 3
  free coordinates of degrees 22, 11, 0;
- all 192 basis polynomials and all 192 source combinations reproduce, and each
  basis vector equals its declared combination applied to the *raw* source;
- the 192x192 source transform determinant is nonzero and my value agrees
  digit-for-digit with the producer's (-1/1.468...e386).

**The absent degree-33 kernel is licensed by the actual source.** The degree-33
physical slots present in the C support are exactly (1,32),(2,31),...,(9,24);
the slot (0,33) is **absent**. Since H^3=(X+W)^9W^24 has W^33 coefficient 1,
no nonzero scalar multiple of H^3 lies in the degree-33 graded piece, so that
block is kernel-free and the deficiency is 3, not the generic 4. This is a
property of this frozen source, not of the ambient degree bound.

**Source mixing is real, and the degree-22 tails are genuine.** The source
column of A3c_76_16 is supported at (9,25),(8,22),(7,19),(6,16), i.e. its
leading form sits in degree **34** while its identity slot sits in degree 22.
Discarding displayed leading parts would lose rank. The retained free basis is
B22 = H^2 - 3X^5W^13 + 3X^4W^10 - X^3W^7 (top H^2 at degree 22 plus real tails
at degrees 18, 14, 10), B11 = H exactly, B0 = 1; all three reproduce from the
raw source, and B0's source column is literally the single monomial slot of
A3c_98_0, which appears in exactly one A3 row and in exactly one basis
combination.

**The universal minor. CONFIRMED, identically, not sampled.** I recomputed all
189x192 entries as Q-linear forms in arbitrary lower coefficients g_uv
(u+v <= 65), with the degree-66 part pinned to H^6. Result: **15,391 nonzero
entries, 42,131 literal terms**, entry-by-entry identical to the certificate;
**zero** upper-triangle violations (every (i,j) with i<j<189 is the zero form,
not a zero sample) and every diagonal is the constant form 1. Hence the
selected 189x189 matrix is unit lower triangular over Q[g_uv] and its
determinant is the constant 1. Column 191 (the constant) has no entry in any
selected row. Off-diagonal columns are confined to {j<i} u {189,190}: the
triangular structure asserted by the DAG is a property of the data, not an
assumption. 188 distinct lower-G coordinates occur, of physical degrees 34..65,
all of which are genuinely populated by G = h^2 - bh/3 + D.

**Survival under base specialization.** Because the identity holds in
Q[g_uv], it is preserved by *every* Q-algebra map, in particular by the
specialization g_uv -> the actual (nonlinear) coefficients of G over
A: the minor stays unit lower triangular with determinant 1 at every point of
Spec A, and (as noted above) G_top = H^6 is automatic there. I verified this
concretely at a random rational base point (Part F below). What does **not**
survive: (i) the *count* 189, which needs char 0 (kernel lemma) plus the
degree-33 support fact, and is a statement about this frozen source only;
(ii) any integral or positive-characteristic model. Over basis and entries
together the construction inverts exactly the primes
{2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79} (largest
denominator 55,035,789,120), so it is defined over Z[1/N] for that N and
**11 itself is inverted**. For a prime p outside that set the *triangular
elimination* still descends, but the pivot census does not: the field claim
"Q, not a claimed integral or arbitrary-characteristic model" is correct and
necessary.

## 2. The exact quotient graph map

**CONFIRMED, in both directions, with the counts qualified.**

Write A for the base ring, u_0..u_188 for the pivoted new coordinates and
v22=u_189, v11=u_190, v0=u_191. Since J is bilinear and G does not involve C,
*every* coefficient of K+J(C,G) is affine-linear in the C coordinates, with
coefficients in A. The 189 selected rows are therefore
M u + N (v22,v11)^t + K_R = 0 with M unit lower triangular over A.

Forward: define phi: A[u_0..u_191,Zj] -> A[v22,v11,v0,Zj] by
u_i |-> -K_Ri - sum_{j<i} M_ij u_j - N_i,22 v22 - N_i,11 v11 (recursively,
i <= 188), u_189,u_190,u_191 |-> v22,v11,v0 and Zj |-> Zj. Every coefficient
lies in A and the recursion terminates, so phi is a well-defined A-algebra map
killing the 189 selected generators. Backward: psi sends v22,v11,v0 |-> the
classes of u_189,u_190,u_191. Modulo the selected ideal, u_i is congruent to
its reconstruction, so psi o phi-bar = id and phi-bar o psi = id. Hence
A[u,Zj]/(189 selected) = A[v22,v11,v0,Zj] as A-algebras, and after adjoining
the images of every other generator,
A[c_1..c_192,Zj]/I_full = A[v22,v11,v0,Zj]/phi(I_rest). The change c <-> u is a
linear substitution with an invertible rational matrix (determinant verified
nonzero), so the passage from old source coordinates to the 189 monic
reconstruction coordinates is an isomorphism, not a chart.

No localization, saturation, radical, generic open set or parameter denominator
appears: the only divisions are by the fixed nonzero rationals of Section 1.
**CONFIRMED**, and I checked the certificate directly: every off-diagonal
declared entry has column j<i or j in {189,190}.

**The constant is a polynomial-ring factor, correctly qualified.** J(1,G)=0
identically, so v0 occurs in no row of J(C,G) - positive, or the constant slot
under Zj. I verified J(B_191,G)=0 exactly at a real base point. Therefore
phi(I_rest) is generated inside A[v22,v11,Zj] and
A[c,Zj]/I_full = (A[v22,v11,Zj]/I_rem)[v0]. This is a free polynomial factor,
**not** an unqualified ring isomorphism; the report says so and is right. The
two nonconstant free coordinates are *not* claimed to be in the kernel of the
full G and their residual rows are retained - correct and required.

**Residual census: CONFIRMED.** Independently: 5,049 physical slots of degrees
1..99 minus 189 selected = **4,860** conservative rows; the frozen factored-J
label stream (local copy, 1,470 lines) has **1,469** distinct positions, the
189 selected are a subset, and removing them and (0,0) leaves exactly **1,279**
known-nonzero rows. The Zj row is retained.

**Presentation counts: GAP.** 250 = 247+2+1 inherits the refuted 247; the
honest unlifted count on the syntactic reading is 245+2+1 = 248, or 250 only if
one silently adds target_a and target_b, which the stated decomposition does
not. The 410 and 1440 figures are **hardcoded literals** in
reconstruction_dag.py (lines 86-88) with no computation behind them; they are
self-consistent through an unexplained "160 h-definition variables"
(410 = 250+160, 1440 = 1279+160+1), but 160 matches no count I can derive:
h = h3^3+C2*h3+C3 occupies **178** distinct physical slots, and the h3+C2+C3
maps have **94** rows. Since these are only nominal presentation sizes and the
report already refuses to call the residual system a completed input, this
does not touch the reduction - but the numbers should not be cited.

**Structural strengthening the pilot does not state.** Because every J row is
affine-linear in C and the graph is triangular with coefficients in A, each
reconstructed coordinate is **affine-linear in (v22,v11)**:
u_i = alpha_i + beta_i v22 + gamma_i v11 with alpha,beta,gamma in A, and
alpha is in addition linear in the K coefficients. Consequently **every
retained residual row has the form P_r + Q_r v22 + S_r v11 with P,Q,S in A**:
I_rem is a *linear* system in two unknowns over A (plus one Zj row). I
confirmed this numerically to the last coefficient at a random base point. The
"abstract g,K,v degree at most 35" language understates this: the v-degree is
exactly 1.

**End-to-end point check (Part F).** At a random rational point of the base
(all 245 map parameters plus a,b): deg h = 33, deg D = 34, deg G = 66,
top(G) = H^6, the selected minor is unit lower triangular, and the DAG
reconstruction makes **all 189 selected rows vanish exactly** while **exactly
1,279 retained positive rows remain nonzero** - independently re-deriving the
1,279 census from the other side. Affine-linearity in (v22,v11) and total
invisibility of v0 both verified at that point.

## 3. Highest face

**CONFIRMED, with the field/scheme distinction correctly drawn.**

The degree-99 face algebra checks symbolically:
J(H^3,(3/4)d^2-2H^3 c) = (3/2)d J(H^3,d) + 2H^3 J(c,H^3), and
J(c,H^6) = 2H^3 J(c,H^3), so the face of K+J(C,G) is as displayed (the a/2 and
bh/2 parts of K have degrees 65 and 98, below 99). The degree-68 map
S |-> J(H^3,S) has **exact rank 69 of 69** by my own Q elimination, hence is
injective - as the kernel lemma predicts, since 11 does not divide 68. A
rational left inverse then gives **equality of coefficient ideals** between the
face and (3/4)d^2 - 2H^3 c; this is a linear-algebra identity and is valid over
any Q-algebra.

Actual source top supports, recomputed: d ranges over exactly
X^2W^25 * (homogeneous degree 7) (8 monomials, W-exponents 25..32) and c over
exactly X^3W^26 * (homogeneous degree 6) (7 monomials, W-exponents 26..32). The
source maps onto these with **exact ranks 8 and 7** (D-top from 12 parameters,
C-top from 7), the rows are linear, and the D and C top parameter sets are
**disjoint**, so the joint map onto the 15-dimensional (d,c) space is
surjective. Over any field of characteristic 0, (3/4)d^2 = 2H^3 c with
H^3 = (X+W)^9W^24 gives 2 ord_{X+W}(d) >= 9, hence ord_{X+W}(d) >= 5 and
d = X^2(X+W)^5W^25 L with L homogeneous quadratic; then
c = (3/8)X^4(X+W)W^26 L^2 is forced. Both expressions satisfy the face equation
and land inside the source supports (verified), d is **linear** in the three
coefficients of L and c is quadratic, so the parametrization is a closed
immersion of A^3 and a bijection on k-points for every field k containing Q.
Hence V(face)_red is isomorphic to A^3.

**Attack on scheme equivalence: the nilpotent control stands.** Over
Q[eps]/(eps^2) take d = eps X^9W^25 (and (9,25) *is* in the actual source D top
support) and c = 0: the face equation holds because d^2 = 0, yet comparing
eps-components would need X^7 = (X+W)^5 L in Q[X,W], which is false. So no L
representation exists and the face ideal is not radical. The divisibility step
uses that k[X,W] is a UFD over a *reduced* base; the report's restriction to
field points is exactly the right one.

**Does replacing the top face by its radical preserve nonemptiness and
properness after pullback and with all lower J rows?** **Yes for emptiness /
properness, and here is the exact argument.** Let I_face and I_lower be ideals
of the same ring. Then sqrt(I_face + I_lower) = sqrt(sqrt(I_face) + I_lower).
Since 1 lies in an ideal iff 1 lies in its radical, 1 in I_face + I_lower iff 1
in sqrt(I_face) + I_lower; both inclusions are immediate from
I_face subset sqrt(I_face) and the displayed radical identity. So the system is
inconsistent with the face iff it is inconsistent with the radical of the face,
and the k-bar point sets coincide. The pullback is legitimate at the reduced
level because the source top map is a **surjective linear** map, hence smooth,
and the preimage of a reduced closed subscheme under a smooth morphism is
reduced; the preimage of the parametrized locus is A^3 x (a linear fibre). The
same surjectivity lifts the nilpotent witness, so no equality of the *original*
ideals holds and none is asserted here. I also confirm that sqrt(I_face) is the
prime ideal of the parametrized graph: V(I_face) has the same underlying space
as the closed immersion image of A^3 (each point is a point over its residue
field, so lies in the image), and A^3 is integral.

**The coupling caveat is load-bearing and correct.** The W^25 coefficient of d
is B2c_47_13 + 4B2c_51_10 + 10B2c_55_7 + 20B2c_59_4 + 35B2c_63_1; solving it
for B2c_47_13 moves lower D coefficients, because those B2 parameters occur in
lower-degree rows of the B2 map. Any use of the parametrization must carry the
same substitution into all lower J rows and must not treat the coupled lower
coefficients as free. Treating them as free would be a genuine
carrier/attainment error, not a bookkeeping one.

## 4. Cost, certificate scope, and controls

**Scope statements: CONFIRMED.** The graph has 42,131 + 189 = **42,320**
literal terms and uses **188** lower-G coordinates of physical degrees 34..65;
724 of the 15,391 entries carry no lower-g dependence at all. Those 188
coordinates are themselves nonlinear polynomials in the base, so the DAG is
indeed an object in abstract g,K coordinates, **not** a 42,320-term object in
the source coordinates. The report says exactly this and is right.

**3.29e62: CONFIRMED as neither a measurement nor a lower bound.** I reproduce
the literal integer 329321309261706864157000551752128693403980556754525116134127842
and the degree bound 35 from the same recurrence. It is the count of paths in
the DAG when like terms are never collected - the uncollected Neumann expansion
of a unitriangular inverse with mean fan-in 80.4 and maximum fan-in 167. It
bounds nothing that any implementation would actually build, and the report's
warning framing is the correct one.

**Cheapest representation/solver discriminator.** Given the affine-linearity
established in Section 2, the decisive and cheapest measurement is: expand
**only the two v-columns** of the reconstruction, i.e. run the triangular back
substitution with the two right-hand sides N_{.,22} and N_{.,11} to obtain
beta_i and gamma_i in A, and record their *collected* term counts as i grows.
That is 2 x 15,103 A-multiplications with no K contribution and no 189x189
inverse, it produces the exact coefficients Q_r and S_r of the residual rows,
and it decides the representation question outright: if beta,gamma stay small
the residual is a small linear system in two unknowns over A and expanded input
is affordable for an F4/msolve-class solver; if they blow up, only the DAG or
an evaluation/black-box interface is viable. A capped variant (expand with a
hard term cap and report the index at which the cap trips) costs minutes. This
is a measurement proposal only; I did not implement dense substitution and did
not launch a solver.

**Negative controls: two are REFUTED as vacuous.**

- verify_filtered.py:100-101 builds `bad` from `actual[0,0]`, adds 1 to the
  constant, and asserts `bad != {(-1,-1):1}`. That is a tautology about a dict
  it just mutated; the checking code is never re-run, so it is not a mutation
  test of the verifier. The prompt's characterization is exactly right.
- reconstruction_dag.py:76-77 asserts `0 == 0 and 0-1 == -1`. It touches
  neither the selected equations nor a retained row, so the
  "selected-only old-pass / remaining-row-fail" control is empty.
- verify_filtered.py:107-110 (mixed-degree source) **is** a real test, though
  it is a toy on X^2+W / X^2-W rather than on the actual source. The concern it
  models is genuine here: A3c_76_16 leads in degree 34 while its identity slot
  is in degree 22, so filtration adaptation is not optional.

**Replacement controls I ran.** Ten end-to-end mutations of the certificate
were fed to the producer's own verifier (a copied script, guard adjustment
reported below). **All ten were rejected**, rc=1, with specific messages:
diagonal 1->2, an injected forbidden upper entry, a perturbed off-diagonal
coefficient, a deleted entry and a swapped selected row all trip "Universal
derivative coefficient mismatch"; a perturbed basis polynomial, a perturbed
source combination and a non-unit free constant trip "Basis reconstruction"; a
perturbed source column trips "Source columns"; minor size 188 trips "Census".
The unmutated replay passes and reports the same source-transform determinant
I computed independently. Separately, the **meaningful** selected-only control
is Part F above: at a real base point the graph satisfies all 189 selected
rows while 1,279 retained rows are nonzero, so the selected equations
demonstrably are not the full ideal.

**Optimized mode: no claim is needed.** AST scan of all three payloads:
**0 `assert` statements, 0 `__debug__` references, 0 eval/exec**; every check
is a `require()` call raising ValueError (31, 31 and 12 calls respectively).
`python -O` and `-OO` therefore cannot weaken a single guard. The producer's
"ordinary Python mode only" claim is honest and, on this evidence, not
load-bearing.

## Scope not covered, custody and artifacts

Out of scope by instruction and not audited here: the separate live full
lifted-J dense stream gate (I read only the frozen label TSV positions, never
its coefficients), and any properness or counterexample claim - none is made by
the pilot and none is made here. This review confirms a linear elimination and
an exact quotient presentation; it does **not** show the remaining system is
easy, small, proper or empty.

Guard adjustments, reported explicitly as required: I copied verify_filtered.py
to a local `verify_patched.py` and changed **only** the four environment guards
(hostname, EC2 DMI, registration tag, scratch root) to `require(True, ...)`,
disjoined the certificate pin with a MUTATE environment flag so mutants could
be fed, and renamed the summary output. The four-line diff is retained. This
host has no python-flint, so a 30-line pure-Python `flint.py` stand-in
(fmpq, fmpq_mat.det/rank over Fraction) was supplied; it is used only by the
producer's script, never by my own checks, and its determinant output agrees
with my independent elimination. No producer guard was modified in place; no
script wrote into the original pilot, C-reduction or root-replay directories;
nothing on the root-owned worker i-0da0cebfc97c9fd54 / 172.30.0.56 was
touched. All arithmetic ran locally in a single Python process, well under one
subprocess-minute and under 200 MiB.

Local evidence, box/linear-c-filtered-gate-opus5-20260906/: rev_a_source.py,
rev_b_pivots.py, rev_c_ident.py, rev_e_face.py, rev_f_point.py with their .out
transcripts; rev_g.out (denominators, cost bounds); mutation_results.txt;
mut/ with the guard diff, the flint stand-in and the mutation driver.

Recommendation: promote Claim 1 (189 universal constant pivots, minor
identically 1), Claim 2 (quotient graph with the polynomial-ring factor and
all residual rows retained) and Claim 3 (reduced-locus parametrization with the
field/scheme distinction). Correct 247 to 245/241, add target_a and target_b to
the base ring, and withdraw or derive 250/410/1440 before any of them is cited.
Record the affine-linearity of the residual in (v22,v11), and measure only the
two v-columns before choosing a representation for the next solver.

Terminal custody is returned. No writers remain.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone body-end marker
  line (`BODY-END` HTML comment), including its terminating newline; this seal
  is outside the body.
- Body bytes: `23861`.
- Body SHA-256:
  `257d8d47be0f6a5d30f1380d3c9335d9ed306bd5b3a4a84ffd0d6c82c4d898dc`.
- Reviewed pilot SHA-256:
  `dbfa3716deb005f68858984ffab01d1897ebc64e0c0f56b2d0062628497a4119`.
- Certificate SHA-256:
  `c2b5965278e0fa30f0490b7f5a019434abe5291e50b748d3a3c0795c8175f906`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
