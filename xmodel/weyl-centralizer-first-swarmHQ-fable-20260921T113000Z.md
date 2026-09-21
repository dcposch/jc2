# Hostile FIRST: Weyl division centralizer and rational indecomposability

status: COMPLETE (checked partial saved 11:35:43Z; final completion below)
seat: Fable5.1/max (claude-fable-5-1), hostile FIRST; hosted identity not
independently attested. Different model from the producer's Astra seat.
unit: weyl-centralizer-first-20260921T113000Z
draft_created_utc: 2026-09-21T11:29Z; startup_utc: 2026-09-21T11:28:44Z

reviewed_contribution: b4fe627842934b2fa33b2f6965f05e2240108d4c
producer_basis: 94cb17776c26eb163bb904f519aa817c1f4baf0d
hq_governance_basis: bbfb2f2b085a4957b4a3e20b8d74f7d777dd0242
reviewed_report: xmodel/weyl-rational-indecomposability-swarmHQ-root-20260921T111800Z.md
(whole SHA256 1ac2d320ee1293db8469c90e2c22a61a422e9641a60836ff82aa6ccaeb5b6248;
artifact body 9800 bytes, body SHA256 02b324ce...41f29 as recorded in its .artifact.json)

## Verdict summary

Overall: CONFIRMED. No unsupported implication found. Every step was
reconstructed independently below; the only remarks are expository, none
changes a conclusion. Scope statements are accurate. This is a desk proof
audit, not computational verification, and not a novelty certification.

| Item | Verdict |
| --- | --- |
| 1. finite length of W/I | CONFIRMED |
| 2. End_W(S)=C, Hom bound | CONFIRMED |
| 3. central denominator | CONFIRMED |
| 4. GGV Theorem 2.11 import | CONFIRMED |
| 5. C_D(P)=C(P), deg R=1 | CONFIRMED |
| 6. embedding donor consequence | CONFIRMED |
| 7. Mobius and b=x t(t+2)/(t+1) controls | CONFIRMED |
| 8. scope | CONFIRMED |

## 1. Finite length of W/I (CONFIRMED)

Bernstein filtration F_k = span{x^i d^j : i+j<=k}; gr W = C[X,D], a domain,
so deg(ba)=deg b+deg a. Hence Wa cap F_k = F_{k-m} a for m=deg a, and
gr(Wa)=C[X,D]sigma(a) with the induced filtration. Strict exactness of
induced/quotient filtrations gives gr(W/Wa)=C[X,D]/(sigma(a)). For m>0
(forced: a nonunit, I!=W) I recomputed dim F_k(W/Wa)
= (k+1)(k+2)/2 - (k-m+1)(k-m+2)/2 = mk + m(3-m)/2, linear with leading
coefficient m as claimed. M=W/I is a quotient, so dim F_k M <= mk+const:
growth at most linear, cyclic hence finitely generated.

Trace: on a finite-dimensional module, tr([d,x])=0 but tr(1)=dim M, so
dim M=0 (char 0). Consequence used: for any finitely generated N with a
good filtration whose Hilbert polynomial has degree <=1, dim gr_j N is
eventually a constant nonnegative integer e(N); e(N)=0 iff dim N finite
iff N=0 (F exhaustive and increasing, so N=F_k N for large k). Thus every
nonzero subquotient of M has e>=1, an integer. Submodules are finitely
generated (W Noetherian); induced filtrations on submodules are good
because gr N' is a submodule of the finitely generated C[X,D]-module gr N
(C[X,D] Noetherian); 0->gr N'->gr N->gr N''->0 is exact, so e is additive.
A strict chain M=M_0>...>M_r=0 with induced/quotient filtrations gives
e(M)=sum e(M_i/M_{i+1})>=r. All strict chains are bounded by e(M)<=m, so
a maximal one is a composition series: finite length. The lemma proves
finite length rather than assuming it; the trace obstruction is exactly
what excludes zero-dimensional factors. I=W gives M=0.

## 2. End_W(S)=C and the Hom bound (CONFIRMED)

S simple is cyclic, S=Ws, spanned by the countable set x^i d^j s. E=End_W(S)
is a division ring (Schur) with C central (scalars commute with W-linear
maps). Evaluation phi->phi(s) is C-linear and injective since a nonzero
endomorphism of a simple module is bijective. If A in E were
transcendental, the field C(A) embeds in E and (A-lambda)^-1, lambda in C,
are linearly independent: a relation sum c_lambda (A-lambda)^-1=0 over a
finite set, multiplied by prod(A-lambda), gives q(A)=0 with
q(z)=sum c_lambda prod_{mu!=lambda}(z-mu); q(lambda_0)=c_{lambda_0}
prod(lambda_0-mu)!=0, so q!=0, contradiction. Their images in S form an
uncountable independent set in a countable-dimensional space. So A is
algebraic; p(A)=prod(A-lambda_i)=0 in the commutative subring C[A] of a
ring without zero divisors forces A=lambda_i. Uses C uncountable and
algebraically closed.

Hom bound: induction on length(M)+length(N) with the left-exact sequences
0->Hom(M'',N)->Hom(M,N)->Hom(M',N) and 0->Hom(M,N')->Hom(M,N)->Hom(M,N'');
for simples, Hom is 0 or End(S)=C. So dim Hom_W(M,N)<=length(M)length(N),
End_W(M) is finite-dimensional, and 1,A,A^2,... are dependent: a nonzero
polynomial annihilates any endomorphism.

## 3. Central-denominator lemma (CONFIRMED)

I_U={a in W : aU in W}. Left ideal: (ba)U=b(aU). Nonzero: W is a
Noetherian domain, hence left and right Ore, and D is its (two-sided)
quotient ring; writing U=s^-1 t with s,t in W, s!=0, gives sU=t in W, so
s in I_U. Right-P stability uses only UP=PU: (aP)U=a(UP)=(aU)P in W. So
r_P(w+I_U)=wP+I_U is well defined and left W-linear (associativity). If
I_U=W then U in W and f=1 works. Otherwise 0!=I_U!=W, M=W/I_U has finite
length by item 1, End_W(M) is finite-dimensional by item 2, and some
nonzero f has f(r_P)=0. Since r_P^k(w+I)=wP^k+I, f(r_P)(1+I)=f(P)+I=I,
i.e. f(P) in I_U, so f(P)U in W. It commutes with P because both factors
do. f(P)!=0: P nonscalar has Bernstein degree n>=1, deg P^k=kn are
distinct, so no nonzero scalar polynomial vanishes at P. Only right-P
stability of I_U is used; no two-sided ideal, no right-Q stability, no
integrality shortcut. The lemma is proved exactly as stated.

## 4. Guccione--Guccione--Valqui Theorem 2.11 (CONFIRMED)

Read whole (8 pages). Ambient: "the Weyl algebra W of index 1 over k",
k a characteristic zero field, generated by X,Y with [Y,X]=1 (page 1);
Z(P) is "the subalgebra of W consisting of all the Q's such that PQ=QP"
(start of Section 2). Theorem 2.11: if P,Q in W satisfy [Q,P]=1 then
Z(P)=k[P]. With k=C, X=x, Y=d this is [d,x]=1, exactly the report's W and
hypothesis. The proof (Section 2) works entirely inside W: Dixmier
imports [D,3.2,3.3] for Lemma 2.1 and [D,Cor.4.5] for commutativity of
Z(P), then Theorems 2.2/2.3, Corollary 2.8, Lemma 2.9, Proposition 2.10,
and the derivation ad_Q on Z(P). Nothing about Frac(W) is asserted or
used. The report imports only C_W(P)=C[P]; its C_D(P)=C(P) is deduced in
item 5 from item 3, not smuggled. The paper's remark that the Dixmier
conjecture would imply the theorem is a converse-direction comment, not a
dependency.

## 5. C_D(P)=C(P) and rational indecomposability (CONFIRMED)

U in C_D(P): item 3 gives B=f(P)U in W with [B,P]=0, so B in Z(P)=C[P] by
item 4, and U=f(P)^-1 B lies in C(P), the subfield of D generated by the
transcendental P (C[P] is a commutative domain inside a division ring, so
its fraction field embeds). Reverse inclusion is trivial. Only the
commutative subfields C(P), C(T) are used; no localization of W or D as a
whole. Statement 3: P nonscalar (it has a mate) forces T nonscalar, and a
nonscalar element of D is transcendental over algebraically closed C, so
R(T)=h(T)^-1 g(T) is defined. T commutes with P in C(T), so statement 2 gives
T in C(P); with P in C(T) this yields C(T)=C(R(T)). The field-degree
formula [C(T):C(R(T))]=max(deg g,deg h)=deg R (lowest terms) gives deg
R=1. Mobius, not necessarily affine, is the correct conclusion.

## 6. Embedding donor consequence (CONFIRMED)

Ore identities: [d,h(x)]=h'(x) for polynomial h, and [d,h^-1]=-h^-1 h' h^-1
=-h'/h^2, so d acts on C(x) subset D as ordinary differentiation. With
the coefficient on the LEFT, Q0 P0-P0 Q0=(1/R')(R d+R')-(1/R')R d=1, using
R'!=0 (char 0, R nonconstant). For a unital C-algebra embedding sigma:D->D
with P=sigma(P0), Q=sigma(Q0) in W: [Q,P]=sigma(1)=1, and
sigma(R(x))=R(sigma(x)) because sigma fixes C and sends inverses to
inverses (h(sigma(x)) is nonzero by injectivity). So P=R(T), T=sigma(x)
in D, with a polynomial mate, and item 5 forces deg R=1. Surjectivity,
Aut(D) classification and generation are never used; only ring-hom
properties and injectivity. The argument actually needs only that some
Q0 in D with [Q0,P0]=1 lands in W, which the displayed donor supplies.

## 7. Sharp controls (CONFIRMED)

Mobius: R=1/x, R'=-1/x^2, donor (x^-1,-x^2 d). Using d x^-1=x^-1 d-x^-2:
[-x^2 d,x^-1]=-x^2(x^-1 d-x^-2)+x d=1. The assignment sigma(x)=x^-1,
sigma(d)=-x^2 d satisfies [sigma(d),sigma(x)]=1 by the same computation,
so it defines W->D, injective since W is simple, hence extends to D->D by
the universal property of Ore localization. sigma(x^-1)=x,
sigma(-x^2 d)=-x^-2(-x^2 d)=d: the donor lands on (x,d). sigma^2 fixes
x and d, so sigma is an involutive automorphism. This shows deg 1 is
attained by a nonaffine R, so "affine" would be false in the embedding
scope. Consistency: the older inner/polynomial-word result excludes
nonaffine R for inner maps, so sigma is not inner; no conflict.

Nonpolynomial b: t=xd, t x=x(t+1), hence f(t)x=x f(t+1) for f in C(t)
(conjugation by the unit x). With r=t(t+2)/(t+1): b^2=x^2 r(t+1)r(t)
=x^2 (t+1)(t+3)/(t+2) * t(t+2)/(t+1)=x^2 t(t+3); b^3=b^2 b
=x^3 (t+1)(t+4) r(t)=x^3 t(t+2)(t+4). Both displayed values verified.
Weight-1 test: S=C[t]\{0} is an Ore set in the Z-graded ring
W[x^-1]=(+) x^j C[t] (s a=a s(t-j) for a of weight j), and the graded
localization (+) x^j C(t) contains b as a homogeneous weight-1 element;
W is a graded subring with W_1=x C[t] (GGV Lemma 2.1(2), Dixmier), so
b in W would force r in C[t], but r has a pole at t=-1. So b not in W
while b^2,b^3 in W. This refutes only the shortcut "U with polynomial
powers lies in W". It does not touch item 3: with P=b^2 (nonscalar, in
W) and U=b, f(z)=z gives f(P)U=b^3 in W, exactly as the lemma predicts.
Side consistency: b in C_D(b^2) but [C(b):C(b^2)]=2, so item 5 says b^2
has no polynomial mate; no contradiction anywhere. Makar-Limanov pp4--5
(physical 8--9) supply only the mechanism r(t)r(t+1)...in C[t] and the
rank-one remarks; his "deg(r)=1" is a growth degree, not the P1 map
degree, and the report does not misuse it.

## 8. Scope (CONFIRMED)

C enters through: trace (char 0), uncountability and algebraic closure
(item 2), algebraic elements of D being scalars (item 5), and GGV's
char-0 field. The report says so. Statement 4 covers arbitrary unital
C-algebra embeddings of D applied to the exact family (R(x),(1/R')d);
it classifies no rational Weyl pair and proves nothing about JC2/DC1 or
the Dixmier conjecture. Compared with the earlier report's Statement and
scope section (input 8, not re-audited): that result treats inner maps
and finite words with polynomial Weyl automorphisms and concludes R
affine; the new result treats all embeddings and concludes deg R=1. The
classes and conclusions differ in the right direction, the Mobius control
shows the weaker conclusion is sharp for the larger class, and neither
result invalidates the other.

## First unsupported implication

NONE. Every implication was reconstructed from the stated inputs
(PBW/Bernstein filtration, Noetherianity of C[X,D], Ore localization,
Schur, the field-degree formula, GGV Theorem 2.11 with its Dixmier
imports). No stronger undocumented theory was substituted. Expository
remarks only: (a) item 1 would read more cleanly with "eventually
constant dim gr_j N" made explicit, since that is where integrality of
the multiplicity comes from; (b) the weight-1 membership test in item 7
is rigorous once the graded localization (+) x^j C(t) is named.

## Lifecycle recommendation

Promotion-eligible at exactly the stated scope: MANUAL, with named
classical imports (GGV 2.11 and its Dixmier inputs). Retain the failed
stronger readings (affine, integrality) as recorded.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — this review raises no `OPEN[...]` entries. Trusted collision
  checker not run by this seat (no scratch/run writes authorized); ROOT
  runs it terminally.

## Pre/post pin, read and deviation manifest

Charged snapshots read by basename from /tmp/jc2-lane.CiK03W/inputs,
all ten SHA256 matched the admission pins before reading:
README 7181a9dd..., AGENTS 31f54fa5..., COORDINATION 9b7a45ae...,
APPROACHES 9e6f87d4..., FALLACY-v2 e47fd16c..., report 1ac2d320...,
artifact.json 6247276b..., input8 cbc331aa..., guccione e1d10e7e...,
makar d7b3dc28... (full digests in the admission text; measured
identical). Inputs 1--7 read whole (APPROACHES in five <=11.5KiB byte
chunks). Input 8: only lines 12--41, "Statement and scope" through the
next heading. Input 9: pdftotext to stdout, pages 1--2, 3--4, 5--6, 7--8
(8 pages total, all read). Input 10: pdftotext to stdout, physical pages
8--9 only. HQ git show at bbfb2f2b...: AGENTS.md 06ba4c08..., POLICY.md
29d6bcea..., RESEARCH_POLICY.md 710fcf0c... (root path; the docs/ path
does not exist at that basis), RUNBOOK.md b9964e42...; all four match
the pins and were read whole.

Authored files: the 444 ACK (1865 bytes, written once) and this report.
Deviations: one compound Bash call (cd + cat + grep) was denied by the
harness and reissued with absolute paths; no other retries. The first
RESEARCH_POLICY pin attempt used docs/RESEARCH_POLICY.md and returned
the empty-input hash; corrected to the root path. This report was
rewritten once (delete + add) from the 958-byte draft to this checked
partial. No scratch, cache, notes, memory, index, settings or credential
writes; no Git mutation; no subcalls; no network; no CAS; no jc2-lean or
jc2-web access; every tool output stayed under 12KiB; no output overrun.
No automatic persistence observed (CLAUDE_CODE_DISABLE_AUTO_MEMORY=1).

## Completion

Whole author readback performed in two chunks (head 6700 bytes, tail
from byte 6701) after the checked partial; content matched intent. One
wording fix applied in this final write (item 5 self-reference changed
to "statement 2"). No hand seal, no artifact_finalize; external legacy
receipt custody applies. Measured completion UTC: 2026-09-21T11:36:16Z.

<!-- BODY-END -->
