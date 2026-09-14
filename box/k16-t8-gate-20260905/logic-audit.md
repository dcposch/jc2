Logic audit for the K16 t=8 hostile gate, Astra sublane.

Root mechanically verified all six frozen charged inputs before delegating this audit. References below abbreviate the frozen Galois report as G = `/tmp/jc2-lane.yGKJor/inputs/k16-gamma-galois-fable5-20260905.md`, the frozen onepoint report as O = `/tmp/jc2-lane.yGKJor/inputs/k16-t8-onepoint-grok46-20260905.md`, and the frozen harvest as H = `/tmp/jc2-lane.yGKJor/inputs/k16-t8-fglm-harvest-opus5-20260905.md`. Supplementary banked sources were read, not edited. No ledger, jc2-lean, or ideation-* file was used.

The orbit-free implication is mathematically sound once the modular equations are known to be reductions of the exact equations. Its clean proof is the banked positive-weight projective promotion lemma. The frozen exposition has two errors of explanation: calling proper specialization a reverse use of the étale lifting lemma, and claiming n'=n from modular boundary length without justifying that those boundary points persist in characteristic zero. Neither is needed for the orbit-free result. The second defect is also repaired below by an independent, exact univariate computation.

1. Literal statement and the actual dependency split.

G:348–352 states exactly: if CONE dim=1 modulo the chosen prime ideal and the whole positive-weight cone V(I2+(W1,...,W7)) is {0}, then clause(ii) holds over A8. This is the statement the producer invokes; it requires neither an orbit count nor a rational point. G:76–82 defines K=A8=Q(sqrt(3)), P=K[b4,q2,...,q7] with weights1,...,7, Ttop=a0*b3^2+b0*b3+c0, the matrix N with rows(Cr,Br), and Wr=a0*Cr^2-b0*Br*Cr+c0*Br^2. At a rank-one point with some Br nonzero, beta=-Cr/Br and Wr=Br^2*Ttop(P,beta). The no-finite-kernel case B=0,C!=0 instead has some Wr=a0*Cr^2!=0. The scalar a0 is nonzero for t>=3.

For each lemma:

- G:124–130, Lemma3.3: the integral model A=R[b4,q]/I2 has a one-dimensional special cone. Properness of ProjA bounds generic projective dimension above; the determinantal height bound gives generic cone dimension at least1, so it equals1. Eagon–Northcott has its expected height over both fields. The common graded shifts yield equal Hilbert functions. Each finite R-module A_d has rank HF_K(d), so equal residue dimension rules out its torsion. A is R-flat, and M=A/(b4-1)=(A[b4^-1])_0 is torsion-free and flat as well. This is a valid flatness argument, conditional on an integral common model and the stated expected-height/EN input.
- G:132–137, Lemma3.4: for torsion-free M of finite generic rank n', lifts of a residue basis of size n are K-linearly independent, so n'>=n. If equality holds, the valuation argument shows the lifts span over R; hence M is finite free. The equality n'=n is an extra hypothesis, not a consequence of flatness by itself.
- G:139–143, Lemma3.5: if n'=n and the special q2-minimal polynomial has degree n, the finite-free model makes multiplication by q2 integral. Reduction forces the characteristic-zero minimal polynomial to specialize to the degree-n modular polynomial. This concerns a point polynomial; it is unnecessary for the orbit-free W-locus certificate.
- G:145–149, Corollary3.6: after3.5 and squarefreeness, factor degrees give Frobenius cycles and constrain degrees of characteristic-zero factors. This is a transitivity test. It is unnecessary for Prop7.1. Reducibility at one prime and absence of degree-one factors cannot refute clause(ii).
- G:151–156, Lemma3.7: a simple rational point of the flat finite-presentation chart has an étale neighborhood and a unique lift to the completed DVR. Nonvanishing modulo the maximal ideal remains nonvanishing at that lift. No equality n'=n is needed. Simplicity is a real input: a quotient by all coordinate equations of an already known point always has length1, so that printed length alone is not a simplicity certificate. The printed full chart Jacobian rank is the relevant check. In the orbit-free proof no simple point is selected, so this lemma is not applied and its hypotheses are not discharged by inventing a point.

The banked lemma replacing the point is the homogeneous-cone promotion lemma in `xmodel/k16-properness-gate-opus5-20260903.md:99–113`, not Lemma3.7. G:345–346's phrase “by3.7 applied in reverse” is incorrect: étale lifting is a local special-to-generic statement, whereas this proof uses properness to specialize a generic projective point. G:350–352 is correct after replacing the literal affine-coordinate extension statement with the projective argument below. The original affine coordinates need not all remain integral or keep b4=1; a generic affine point can specialize to the projective boundary. The complete boundary W-test is therefore essential.

2. Direction of specialization, with no hidden flatness claim.

Let R be the local domain at the selected good prime of the number field, and require every actual exact generator to lie in R[b4,q2,...,q7] and reduce to the modular polynomial used by the solver. Put

    J=I2(N)+(W1,...,W7),  S=R[b4,q2,...,q7]/J,  X=Proj(S).

Every generator of J is homogeneous for the positive weights(1,...,7); finite generation is immediate, and S_0=R. Consequently X→SpecR is proper. Proj commutes with base change. The whole-cone modular statement is equivalent to X_k=empty. The image of a proper morphism is closed, and a nonempty closed subset of a local scheme contains its closed point. Since that point is absent from the image, X is empty, hence X_K is empty, hence V(J_K)={0}. This is precisely the banked lemma at `xmodel/k16-properness-gate-opus5-20260903.md:99–113`; its positive-weight/Proj equivalence is at81–88 and finite-generation properness input at58–65.

The banked gate explicitly says **“No flatness”** at117–119. Thus the prompt's premise that empty special fibre requires the flat-model hypothesis is too strong for this projective situation. Properness supplies the needed direction; flatness alone does not. For example Spec(R[z]/(p*z-1))=Spec(R[1/p]) is finite-type and flat, has empty special fibre, and nonempty generic fibre. Promoting the inhomogeneous affine unit ideal without the boundary/projective argument would be invalid. The model flatness furnished by G:124–130 is compatible with the literal hypotheses of Prop7.1 but is logically surplus for promoting this homogeneous emptiness. The assertion n'=n is also surplus.

An external primary-source cross-check agrees: [Stacks, Lemma27.8.11, tag01MF](https://stacks.math.columbia.edu/tag/01MF) gives the valuative existence/uniqueness property for Proj of a graded algebra finite over its degree-zero base as an algebra; [Stacks, Proper morphisms, tag01W0](https://stacks.math.columbia.edu/tag/01W0) defines properness through finite type, separatedness, and universal closedness and records stability under base change and closed immersion. No Hensel argument enters this empty-fibre deduction.

3. The two modular pieces cover the whole geometric cone.

H:79–88 distinguishes H1=CONE dim1, H2a=boundary W-locus {0}, and H2b=affine chart W-locus empty. H:88–92 uses positive weighted homogeneity. If b4!=0, scaling by lambda=b4^-1 sends b4 to1 because its weight is1 and preserves every homogeneous zero equation. If b4=0 and another coordinate is nonzero, choose its first index j; over the algebraic closure a j-th root gives a scaling to qj=1. Hence the first-nonzero strata j=2,...,7 exhaust the nonzero boundary. This argument is geometric and needs no Fp-rational normalization for weight j>1.

O:113–115 and H:98–108 report the full special boundary partition: j2 empty, j3 length6, j3+(W) empty, and j4,...,7 empty. The unit ideal in the affine chart and the empty W-subschemes on every boundary stratum imply V(J_k)={0}. The six-point count is not being used as an orbit count or a claim of attainment for Ttop; the W-unit-ideal test excludes every geometric point at once. If the root's independent computation corroborates these data and the common-model map, this closes the geometric part of the promotion.

4. CONE dim1 and the CI chart are justified in the correct order.

O:178–182 identifies the modular CI system G1,...,G7 at b4=1 with the b3-lift of the minors chart, using the already measured modular B-hsop: V(B_k)={0}. On b4=1 there is therefore always some Br!=0, and the equations Gr=0 solve uniquely for b3. On each principal open Br!=0, eliminating b3 yields exactly the minors; these local isomorphisms glue. Thus the finite CI quotient length52138 in O:200–213 is the length of Y8_k, not merely a numerical projection bound. This identification requires B-hsop at the modular prime, which has no characteristic-zero integrality problem as an assertion about the actual modular equations.

The chart b4!=0 is Gm times its b4=1 slice, so it has dimension1. The entire remaining slice b4=0 has dimension1 by O:113. The union therefore gives CONE dim1. O:215–218's prose should be read as using BOTH pieces: a zero-dimensional b4=1 chart by itself would not rule out a larger component lying entirely in b4=0. With both supplied, Lemma3.3 applies after common-model integrity is established.

5. A genuine n'=n gap in the frozen argument, and its completed repair.

O:223–226 invokes G:158–162 (Lemma3.8) to turn the modular j3 length6 into a characteristic-zero boundary contribution at least2, hence n'<=52138. That transfer is not justified by ambient flatness alone. Lemma3.8's formula dGamma=n'+sum(eL/gL) is a formula within the generic fibre when it uses n'. A positive special boundary length does not prove positive generic boundary length.

A concrete counterexample is R=Z_(p), A=R[x,y]/((y-x)*(y-p*x)) with both weights1 and chart b4=y. A is flat, each cone has dimension1, and ProjA is a finite flat degree-two family with reduced special fibre. On y=1 the generic algebra K[x]/((1-x)*(1-p*x)) has length n'=2, while the special chart k[x]/(1-x) has length n=1. The special boundary y=0,x=1 has length1, but the generic boundary is empty. Inserting that modular boundary length into dGamma-n' would falsely give n'<=1. Even a simple special boundary point may lift to a generic affine point: here [1:0] lifts to [1:p].

This gate now supplies a direct exact repair, not a flatness assumption. The read-only exact source `box/k16rank-20260903/terminal_t8_exact_none.out` has SHA256 `8f41559606bbf9f2c592f5569ee0feef596d7196d39d2290941bdf889990f767`, mechanically checked against `box/k16rank-20260903/artifacts.sha256:174`; manifest/check are `logic-source.sha256` and `logic-source.check.log` in this gate's notes directory.

The new emitter `box/k16-t8-gate-20260905/exact_boundary_restriction.py:15–27` applies the exact K-algebra map

    b4,q2,q4,q5,q7→0; q3→1; q6→z; b3→b3;
    K=Q[yy]/(3468*yy^2-1836*yy+234), target K[z,b3] with dp order.

It re-parses top rows T15,...,T8, checks their quadratic splits, forms Br,Cr from those exact rows, and computes D=B3*C6-B6*C3. Substitution commutes with coefficient extraction in b3 because the map fixes b3 and sends only base coordinates. The output `exact_boundary_restriction.out:1–14`, with empty stderr and no FAIL/error marker, is:

    B_r=C_r=0 for r=1,2,4,5,7;
    B3,C3,B6,C6 are nonzero;
    deg D=6, deg gcd(D,D')=0, D(0)!=0, a0!=0;
    deg gcd(D,B3,B6)=0;
    deg gcd(D,W3,W6)=0;
    EXACT_BOUNDARY_RESTRICTION_DONE.

This exact subsecond Singular computation proves six distinct characteristic-zero points (0,0,1,0,0,z,0), all z!=0. All minors vanish there because the only surviving matrix rows are3 and6 and their determinant is D. The stabilizer gcd of the nonzero weights is gcd(3,6)=3. The six z-values give six distinct weighted cone lines: the residual mu3 preserving q3=1 acts trivially on q6. Each line has multiplicity at least1, so the **generic** weighted boundary contribution is now at least6/3=2. With dGamma8=52140 (EN, after dimension is known) and Lemma3.4's n'>=n=52138, one obtains n'=n=52138 correctly. Equality also shows the generic boundary contribution is exactly2. This uses a lower bound plus an independent upper bound, rather than promoting a modular count to generic attainment.

The monic exact sextic is preserved as `exact_boundary_minor.txt`; its SHA256 is `7c0b0e5db1734884d168b00c6db37aab68c06923b9e765f99f34236b49d3aefd`. An independent image check (`exact_boundary_image.sing/.out/.err`) reduces this actual exact sextic at(32003,11288) and prints `EXACT_BOUNDARY_MOD32003_IMAGE_MATCH=1` against the charged sextic in O:124–125, with no error and empty stderr. The accepted restriction driver/output hashes are `4909dc42e9c452a5ee842efd45a5f87083c8f41b667eb2e92b34b0ef87700966` and `8c9d1d4ba155b1746570b817b3c65455dae9b9eb249e0e73fad5be028f759660`. An initial emitter version accidentally named coefficient b3, colliding with the ring variable; its error was detected immediately and its results rejected. The corrected aa/bb/cc coefficient names produced the accepted output just cited. No result from the rejected run is used.

6. Scope of the historical detector caveat and redundancy of a separate (i) certificate.

`xmodel/k16-rank-criterion-fable5-20260903.md:498–510` explicitly separates H-gen (reduce exact rows and form derived generators by ring operations, only division2) from H-int. At t8,p32003,yy11288 there was no PINT PASS, only the absence of Singular's `? div. by 0` detector. O:232–236 and H:432–436 inherit that caveat. Properness cannot manufacture the missing identification between unrelated exact and modular equations. If that integrity remains unverified, the proof as supplied is conditional on it. One good prime is mathematically sufficient once the identification is certified; a second prime is replication, not a missing theorem hypothesis.

There is an additional direct implication: V(B,C)⊆V(I2,W), because each minor and each Wr vanishes whenever all Br,Cr vanish. Therefore the full exact H2 conclusion itself implies clause(i). Its integral implementation also implies clause(i) from H2 without relying on the separately banked rank-lane promotion. This does not magically eliminate a shared exact-row integrality uncertainty: H2's source map must still be verified. But after that check succeeds, the separate rank-lane detector qualification is redundant for T, even if one retains it as historical metadata on the stronger B-hsop claim.

More directly, any nonzero zero of all top-tail rows satisfies all Gr=0, hence Cr=-Br*b3, hence I2=0 and Wr=0. A nonzero P-coordinate contradicts the promoted H2 cone; at P=0, Ttop=a0*b3^2 forces b3=0. Thus H2 and a0!=0 already imply V0-tail. The usual banked chain is `xmodel/k16-rank-criterion-fable5-20260903.md:491–496`: V0-tail→V0→(8.1)→T. This audit makes no exit-price assertion, so no charge_basis line is due.

Logic disposition: CONFIRMED after common-model integrity, using the banked properness lemma and the exact n'=n repair above. If source integrality is left DETECTOR-ONLY, type the original characteristic-zero promotion CONFIRMED-CONDITIONAL on H-int; do not call an additional prime a logical requirement. Final computational verdict and worker custody belong to the root lane.
