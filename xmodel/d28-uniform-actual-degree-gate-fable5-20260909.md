# Hostile different-model gate: D28 actual-degree column source selection (Fable 5.1)

tag=d28-uniform-actual-degree-gate-fable5-20260909
reviewer=Claude Fable 5.1 (claude-fable-5-1)
frozen_basis=0d39df3c9fd69c939a8420c54d03228b9077777d (provenance only)
launch=root actual release 09:31 UTC; review opened 09:32 UTC; absolute deadline 09:57 UTC
subprocesses=ZERO mathematical subprocesses. Commands run: date, ls, cat, sha256sum, and this one report write. No script, CAS, checker, solver, agent, SSH, or shared write.

## 0. Custody

All 11 lane copies under /tmp/jc2-lane.qbqgh4/inputs were hashed with sha256sum and compared token by token against the sha256 and bytes fields of the matching PINS entry; all 11 match (proof 579199ec/18075, transaction 46ee9fc3/710, read-scope 1721bc41/4318, input-pins c45f0d55/2703, custody 817dd92f/4033, 15x proof aeeddd6a/20625, 15x gate 2d6f3869/25439, 15x status 152fa422/6164, 16h status a7aeb124/4604, ggv bundle d0a3118c/8155, gghv bundle ab7bc071/29136). PINS itself hashes 1fae41fceee37c06b88deff062e283ffb7e2b62713bfe6b9067bbedc9e63d485 at 7307 bytes; 12 charged objects total. No PINS source path, live gate, cross, log, receipt, peer report, F2/F10 pending result, or new F10 map was opened.

## 1. Read scope

Read WHOLE from lane copies: the new D28 proof (body through its BODY-END marker), its READ-SCOPE, the frozen 15x status entry 17(xxxxxxxxxxxxxxx), the frozen 16h status entry 17(hhhhhhhhhhhhhhhh), the accepted GENERAL 15x producer (all nine sections) and its Fable gate (all seven sections). Transaction, input-pins and custody JSON read for integrity only. Primary bundles read WHOLE: GGV 718-790 (Rem 4.2, Def 4.3, Lemma 4.4, Rem 4.5, Prop 4.6 statement and partial proof) and 1431-1461 (Prop 5.20 statement and proof, Cor 5.21 statement); GGHV 640-820 (end of Alg 6, Thm 2.20 statement and whole proof, Rem 2.21, start of Rem 2.22), 910-979 (subsection 2.4, Rem 2.24, (2.13), Def 2.25, admissibility sentence), 1180-1255 (Def 3.3, N0 parameterization, (3.20), Lemma 3.4 statement), 1350-1425 (Section 5 header with the swap instruction, both whole tables, k/e_k sentence, start of the F18-F21 exclusion). Not charged and not read: GGV Props 5.13/5.16-5.18/Thm 7.6, GGHV Prop 3.2 statement and (3.17)/(3.18), Algorithms 8/9 output; these stay imported at statement scope.

## 2. Group 1: GENERAL normalization, uniform in q. CONFIRMED

Set m0=q+2, n0=2q+3=2m0-1. gcd(m0,n0)=gcd(m0,-1)=1; m0>=2, n0>=3; m0|n0 would force m0|1, and n0>m0 forbids n0|m0. So the degrees 28m0, 28n0 are nondividing for every q>=0, and the Division Lemma makes any constant-J pair with these degrees a counterexample over C. The accepted 15x Section 3 is stated for arbitrary coprime m,n>1 and D>0 (its conclusion (B) hypotheses), was reviewed generically in the accepted gate's Group 1, and is applied by 15x Section 6 to arbitrary coprime m,n. Nothing in it depends on the values 3,5,25. Instantiating (m,n,D)=(m0,n0,28) for each q is therefore inside the accepted perimeter; no q-dependent step is added.

Derivation replayed by hand. ML's polynomial source automorphism gives Pbar a joint corner (r,s), 0<r<s, and positive-weight bracket vanishing gives Qbar a corner (t,u)=lambda(r,s) on the same ray. With inverse coordinates U,V of degrees M,N>=1 (nonconstant because psi is an automorphism), (r,s) is the unique maximizer of Mi+Nj on the rectangle, and U_M^r V_N^s is nonzero in the domain C[x,y] whatever the dependence of U_M,V_N. Hence deg P=Mr+Ns, deg Q=Mt+Nu=lambda deg P, so lambda=n0/m0 is derived. Coprimality: m0 | n0 r and m0 | n0 s force (r,s)=m0(a,b), (t,u)=n0(a,b), 0<a<b integers. Then 28m0=m0(Ma+Nb) gives the exact identity 28=Ma+Nb>=a+b. No global minimum, no affine assumption, no Laurent inverse enters.

GGV Def 4.3 for (Pbar,Qbar) in ordinary L: bracket a nonzero constant (source automorphism multiplies J by its constant Jacobian); v11 ratio (r+s)/(t+u)=m0/n0; v10 ratio r/t=m0/n0; en10(Pbar)=(r,s) so v_(1,-1)=m0(a-b)<0. Prop 5.20 then applies to each such pair; its proof's phi is id or y->y+lambda, which maps x^i y^j into [0,i]x[0,j], so the rectangles [0,7m0]x[0,21m0] style supports and the corner coefficients are preserved, and v11 of both members and en10(P) are preserved by the statement. The "Moreover" successor clause is a conditional extra conclusion, not consumed.

Field transfer. Nonexistence: coefficients of a K-pair lie in a finitely generated F over Q, F embeds in C, the embedding preserves supports, degrees and the nonzero constant bracket, so a K-pair yields a C-pair. The q=2 positive statement is asserted only over C (or over an algebraic extension by finite witness), never as descent of the normalizer to K. The proof keeps these apart correctly.

## 3. Group 2: complete table, parameter, orientation filter. CONFIRMED

Corner sums from both printed tables: F1 (4,12)=16; F2-F6 (5,20)=25; F7,F8 (6,15)=21; F9,F10,F11 (7,21)=28; F12 (8,24)=32; F13 (9,21)=30; F14-F17 (9,24)=33; F18,F19 (6,18)=24; F20,F21 (6,24)=30; F22-F24 (8,24)=32. Rows with a+b<=28 are exactly F1-F11, F18, F19 (13 rows); the other 11 rows sum to 30, 32 or 33. All 24 printed families are accounted for.

Exact inverse identity, not the inequality: (5,20): 28=5(M+4N), impossible since 5 does not divide 28; kills F2-F6. (6,15): 28=3(2M+5N), impossible; kills F7, F8. (6,18): 28=6(M+3N), impossible; kills F18, F19 without the paper's separate F18-F21 exclusion. (4,12): 28=4(M+3N) gives M+3N=7 with positive solutions (4,1),(1,2); F1 survives the identity and needs Group 3. (7,21): M+3N=4 forces (M,N)=(1,1). Orientation invariance: swapping the outputs keeps A0, because (1/m0)(r,s)=(1/n0)(t,u)=(a,b); swapping the source axes exchanges M,N and the divisibility of Ma+Nb by 5, 3 or 6 is symmetric.

Row formulas checked against literal Definition 3.3 (a≀l,b) with e_k=gcd(k,bl-a) and (m+n)bk-n(bl-a)=k. F1 (7≀4,3): bl-a=5, k<5/3 so k=1, 3m-2n=1, (3,4),(5,7),... = (2j+3,3j+4). F2 (7≀5,2): bl-a=3, k=1, 2m-n=1 = (j+2,2j+3). F3/F4 (8≀5,3): bl-a=7, k in {1,2}; k=1: 3m-4n=1 = (4j+3,3j+2); k=2: 6m-n=2 with gcd filter (odd m) = (2j+3,12j+16). F5/F6 (9≀5,4): bl-a=11, k in {1,2}; k=1: 4m-7n=1 = (7j+9,4j+5); k=2: 8m-3n=2 = (3j+4,8j+10). F7/F18 (7≀3,4): bl-a=5, k=1, 4m-n=1 = (j+2,4j+7). F8/F19 (8≀3,5): bl-a=7, k=1, 5m-2n=1 = (2j+3,5j+7). F9 (11≀7,2): bl-a=3, k<3/2 so k=1, 2m-n=1 = (j+2,2j+3). F10/F11 (13≀7,3): bl-a=8, k<8/3 so k in {1,2}; k=1: 3m-5n=1 = (5j+7,3j+4); k=2: 3m-n=1 = (j+2,3j+5). Every retained printed formula is the literal solution set of Def 3.3 with j in N0; the column parameter q is never pre-identified with j. Coprimality of the F9 and F10 formulas: 2(j+2)-(2j+3)=1 and (5j+7)-(3j+4)=2j+3, (3j+4)-(2j+3)=j+1, (2j+3)-2(j+1)=1.

Literal-table observation, non-load-bearing: for F6, e_2=gcd(2,11)=1, so k/e_k=2, contradicting the printed sentence "in all the cases except F4 we have k/e_k=1", and gcd(3j+4,8j+10)=gcd(j+2,2)=2 at even j, so the printed F6 formula lists non-coprime pairs that Def 3.3 excludes; the true F6 family is the odd-j subprogression. F6 has A0=(5,20) and is dead by 5 not dividing 28 for every (m,n), so the column is unaffected. Recorded only so that "published enumeration literal" is not overstated.

Both orientations are retained: the header sentence says the (3.18) cases are obtained by swapping m with n, and the proof compares the column's smaller/larger ratio against min/max of each printed row, which covers printed and swapped rows. That the actual pair's (m,n) lies in the MN family of its final corner (GGHV Prop 3.2, statement outside the charged intervals) is an import the accepted 15x gate named explicitly; the new proof subsumes it under "published complete Section 5 formulas". Naming only.

## 4. Group 3: independent hand ratio proof. CONFIRMED

r(q)=(q+2)/(2q+3). Upper: 3(q+2)<=2(2q+3) iff 0<=q, equality iff q=0, so r(q)<=2/3 with equality only at q=0. Lower: 2(q+2)>2q+3 iff 4>3, always, so r(q)>1/2 strictly for every finite q; 1/2 is never attained.

F1: first entry smaller (difference j+1). (2j+3)/(3j+4)-2/3=(6j+9-6j-8)/(3(3j+4))=1/(3(3j+4))>0, so the ratio exceeds 2/3>=r(q) for every j; at j=0 it is 3/4. Reverse orientation exceeds 1. Never matches. F11: (j+2)/(3j+5)<1/2 iff 2j+4<3j+5 iff j>-1, always; at j=0 it is 2/5. Never matches. F9: (q+2)(2j+3)=(j+2)(2q+3) expands to 2qj+3q+4j+6=2qj+3j+4q+6, i.e. j=q; both pairs coprime, so the reduced pairs coincide, no hidden scaling. F10: first entry larger by 2j+3, so the swapped ratio (3j+4)/(5j+7) must be used: (q+2)(5j+7)=(2q+3)(3j+4) expands to 5qj+7q+10j+14=6qj+8q+9j+12, i.e. qj+q-j-2=0, i.e. (q-1)(j+1)=1. With q,j nonnegative integers, j+1>=1 forces q-1=1, j+1=1: q=2, j=0, printed (7,4), column pair (4,7), actual degrees 112 and 196. q=0 gives j=-2, q=1 gives 0=1. Rational-index remark: with q integral, a rational j>=0 still forces q-1=1/(j+1) in (0,1], so only q=2,j=0; spurious values arise only if q itself were rational (q=3/2 with j=1). The proof's sentence is imprecise about which parameter but nothing rests on it, since both are integers by construction and by (3.20).

Control demanded by the prompt: omitting the swapped orientation compares (5j+7)/(3j+4)>1 with r(q)<1 and wrongly kills F10 for all q, which would fabricate exclusion of q=2. The swapped (7,4) row at j=0 is retained by (2), and no realization is inferred from it.

## 5. Group 4: full ordinary attachment. CONFIRMED (one supplied step recorded)

M+3N=4 with M,N>=1: N=1 forces M=1; N>=2 forces M<=-2. So M=N=1, both inverse coordinates are linear, the ML normalizer is affine, and Prop 5.20's y->y+lambda is affine. Actual degrees of the standard pair are m0(a+b)=28m0 and 28n0, supports in [0,7e]x[0,21e] with (7e,21e) attained for e=m0 and e=n0, which is the rectangle premise absent from bare Laurent standardness.

Theorem 2.20: (6) A0=(1/m)en10(P)=(7,21) and (A0,(rho0,sigma0)) is a regular corner of type II. Direction: dir(A0-A0')=dir(6,21) is the primitive (rho,sigma) with 6rho+21sigma=0, rho>0, i.e. (7,-2). Both table rows with A0=(7,21) that survive have A0'=(1,0) and A1 in {(11/7,2),(13/7,3)}, and A1 differs from A0'. Item (7) says type II.a forces A1=A0', so index 0 is type II.b by (6). Item (8): l1=lcm(rho0,l0)=lcm(7,1)=7>1, and (2.5) with A0'=(1,0) reads A1=(1,0)+(m_lambda/m)(2/7,1); A1=(11/7,2) iff m_lambda=2m (F9), A1=(13/7,3) iff m_lambda=3m (F10, F11). Item (13): the greatest index with l_t=1 is t=0, so (A0,(7,-2)) is the unique regular corner of the standard pair itself, of type II.b, A0' its last lower corner, and (P0,Q0)=(P,Q). This is the actual starting triple ((7,21),(1,0),(7,-2)), not a label and not a later Laurent child.

Standardness under output swap, audited. ell10(P)=x^(ma) f(y), ell10(Q)=x^(na) h(y), deg f=mb, deg h=nb. Bracket: d_x(x^(ma)f) d_y(x^(na)h) - d_y(x^(ma)f) d_x(x^(na)h) = a x^((m+n)a-1) (m f h' - n f' h). Its x-degree (m+n)a-1>=4 exceeds 0, the x-degree of the constant [P,Q], so m f h' - n f' h=0, i.e. (h^m/f^n)'=0, h^m=c f^n with c nonzero. Then m ord_y h=n ord_y f, st10(Q)=(n/m)st10(P), and v_(1,-1)(st10 Q)=(n/m)v_(1,-1)(st10 P)<0. With [Q,P]=-[P,Q] nonzero, en10(Q)=n(a,b), and both ratios n/m, (Q,P) is a standard (n,m)-pair in L. Sign and derivation as printed are correct.

Supplied step (the proof asserts it via the multiplicities 21 and 12 but does not display it): the F9/F10 dichotomy is intrinsic to the pair, not to its orientation. On the (7,-2) face the monomials are x^(m+2k) y^(7k), so ell_(7,-2)(P)=x^m Pt(w), ell_(7,-2)(Q)=x^n Qt(w) with w=x^2 y^7, deg Pt=3m, deg Qt=3n. The bracket's (7,-2)-weight 7(m+n)-5 is positive, so the face bracket vanishes; computing, [x^m Pt, x^n Qt]=7 x^(m+n+1) y^6 (m Pt Qt' - n Pt' Qt), hence Qt^m=c Pt^n. A root of multiplicity 3m (resp. 2m) in Pt is a root of multiplicity 3n (resp. 2n) in Qt, and 2m+3m>3m shows the two patterns are exclusive. So the swapped (7,4)-pair has A1=(13/7,3) exactly when the unswapped (4,7)-pair does, with selected multiplicity 3*7=21 in the degree-196 member and 3*4=12 in its mate. Without this step the swapped pair could numerically also be "F9 swapped at j=2", which the table alone does not exclude. With it, and with (7,4) verified directly in MN_1(13≀7,3) (21-20=1) while (4,7) is not (12-35), the exceptional representative is exactly the printed F10(0) row: (m,n)=(7,4), A0=(7,21), A0'=(1,0), A1=(13/7,3), k=1, direction (7,-2), type II.b, degrees 196/112. This closes an exposition gap by a manual factored derivation; it is not a genuine GAP.

## 6. Group 5: exact 16h quantifiers. CONFIRMED

16h's promoted statement: for every integer q>=0, every hypothetical ordinary rectangular standard Keller pair with supports [0,7e]x[0,21e], attained (7e,21e), actual chain A0=(7,21), A0'=(1,0), direction (7,-2), type II.b, selected A1=(11/7,2), maps to the 16g receiver, and 16g's exclusion makes that set S_q empty for every q. Each antecedent is discharged above for the F9 branch of the unswapped standard pair: ordinary (phi in Aut(L), affine); rectangular with attained corners (Group 4); standard (m0,n0)-pair with nonzero constant J (Group 1); A0=(7,21), A0'=(1,0), direction (7,-2), type II.b at index 0 with l0=1 and (P0,Q0)=(P,Q) (Group 4); selected A1=(11/7,2) is the definition of the F9 branch; j=q and P first match m=q+2, n=2q+3 (Group 3); k=1 is forced since I(11≀7,2)={1}. So the standard pair lies in S_q, contradiction. No row-to-realization arrow is used: the chain of the hypothetical pair is one of the rows by imported completeness, and the row is then consumed only as a necessary profile.

Exhaustion of the alternative: if the unswapped chain has A1=(13/7,3), its (m0,n0) must be F10 or F11 in printed or swapped orientation; F10 printed has first entry larger, F11 printed needs 3q+5=2q+3, F11 swapped has first larger, F10 swapped gives (q-1)(j+1)=1. So q=2 is forced, and then the swapped pair is the F10(0) representative of Group 4. For q not 2 the only branch is F9(q), dead by 16h, which is the column nonexistence. At q=2 the F9 branch is dead and only the F10(0) alternative remains; the proof asserts neither existence nor exclusion for it, uses no pending F2/F10 gate and no new F10 map.

## 7. Group 6: controls and scope. CONFIRMED

Manual changed-object and changed-hypothesis controls, none executed, none a Keller example.

- Inverse identity dropped, keeping only a+b<=28: F2's (j+2,2j+3) ratio-matches at j=q for EVERY q, and the whole column would fall to an F2 alternative; the identity 5(M+4N)=28 is what kills it. Independently found: F3 at j=0 ((3,2), swapped (2,3)) ratio-matches q=0, and F5 at j=0 ((9,5), swapped (5,9)) ratio-matches q=3 because (4j+5)/(7j+9)=(q+2)/(2q+3) reduces to q=2+1/(j+1). Both survive the ratio filter and die only by 5 not dividing 28. Hence the divisibility identity is load-bearing at q=0, q=3 and every q, not just at F2.
- Ratio dropped: F1's identity M+3N=7 has positive solutions (4,1) and (1,2), so F1 is killed only by the strict inequality 1/(3(3j+4))>0. Changed numerical hypothesis: a column of ratio 3/4 with D=16, degrees (48,64), would pass F1 at j=0 with M=N=1; the D28 column never does because r(q)<=2/3.
- Swapped F10 omitted: fails as in Group 3, fabricating an all-q exclusion. Changed endpoint: replacing 3j+4 by 3j+5 in F10 turns (2) into q(j+3)=j-1, whose only solution is q=0,j=1, showing the q=2 survivor is arithmetic of the literal row, not a convention.
- Ordinary versus Laurent: a Laurent or zero-degree inverse coordinate breaks the unique maximizer of Mi+Nj and the bound a+b<=28, letting the sum-30 to sum-33 rows re-enter; a Laurent-standard pair with the same en10 can carry a higher v11 through negative x-powers, so a preserved endpoint alone gives neither the total leader nor the degree. The ordinary rectangle from ML plus the constant translation supplies the missing support condition.
- Same-model separation: I did not consult the accepted 15x gate's verdicts as evidence for the D28 steps; every arithmetic step above was rederived.

Field transfer, assessed separately: the nonexistence for q not 2 needs only the embedding of a finitely generated coefficient field into C. The optional finite-witness transfer for the q=2 representative (finitely many polynomial equations and inequations in the affine normalizer, translation, scalings and inverse over F, proper over F because solvable over C, hence solvable over an algebraic closure of F inside an algebraic closure of K) is valid and unnecessary; the proof states it as optional and claims no K-normalizer.

Imported trust, precisely: Division Lemma and ML pp.302-305 via accepted 15x; GGV Def 4.3 and Prop 5.20 at statement scope (interior Props 5.13, 5.16-5.18 uncharged); GGHV Thm 2.20 (proof read, its citations to GGV Thm 7.6 and Remarks 5.8-5.12 imported), subsection 2.4 admissibility, Prop 3.2 membership of (m,n) in the final corner's MN family, Def 3.3 and (3.20) (read and hand-verified), published completeness of the M=35 enumeration and the (3.17)/(3.18) swap sentence at literal scope; accepted 16h composed with 16g as a frozen emptiness theorem. First genuine GAP: none found. The only omitted step (face-intrinsic A1 under swap) is supplied in Group 4 from charged material.

## 8. Verdicts

Source selection (Groups 1-4, 6): CONFIRMED at the named imported and accepted tier. For every q>=0 the normalized profile is F9(q) or, only at q=2, the swapped F10(0) row; the necessary exception is exactly actual 112/196 with the printed (7,4) representative and the data stated in the proof's Section 1.

16h composition (Group 5): CONFIRMED. The F9 branch satisfies every ordinary, rectangular, actual-chain antecedent of the accepted emptiness theorem for every q, so no ordinary characteristic-zero constant-J pair of actual degrees 28(q+2), 28(2q+3) exists unless q=2. At q=2 only the F10(0) alternative remains; no existence, exclusion, maximum-196, D28-ratio coverage, certificate, solver permission, or JC2 conclusion follows. No next task is promoted or launched.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — own-only review; no corpus scan performed.

<!-- BODY-END -->
