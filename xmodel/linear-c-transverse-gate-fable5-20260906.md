# Gate: transverse-line full-C rank191 theorem and W-filtration lemma

2026-09-06. Gate: Fable 5.1 (different model from producer Astra), lane
/tmp/jc2-lane.rM5Jkj. Evidence: independent desk re-proof, independent
source reconstruction, own exact-rational controls, normal-mode replay.
No AWS, no jc2-lean, no heavy CAS, no live cross-report read, no ledger edit.

Verdict: PASS on all four gated claims, each in exactly the scope the
producer states. No claim was found overstated. Three items remain typed
OPEN because the producer does not claim them and nothing here proves them.

Primary producer report
xmodel/linear-c-transverse-rank-astra-20260906.md, full SHA256
8cf51bd8ab5c338e927543347b8790a2451573c86263efd7cf9d5cd98712adf0.
All eight charged inputs in the lane directory hash-match the index
(charged-inputs.list); the repo copy of line_support_check.py is
byte-identical to the charged copy (a9e0e465...).

## Independent reconstruction of the literal source

Everything below was recomputed from delta2_stage8.strongest.json
(778eda93...) and complete_export.json (b91d706e...) with my own parsers
(box/linear-c-transverse-gate-fable5-20260906/census.py, hlift.py), not by
replaying producer asserts.

| Fact | Reconstructed value |
|---|---|
| Distinct names in h3,C2,C3,B2 | 245 (Hc,C2c,C3c,B2c plus E82, minor_a2, rho, u) |
| Base coordinates incl. target_a, target_b | 247 |
| Distinct names in A3 (C space) | 192; all A3c_*; disjoint from base |
| Occurring coordinates / declared free | 439 / 444; unused: Z55, leader55, target_c,d,e |
| Export coordinate order | 600 = 439 + 160 Hfact + Zj |
| Source residual_rows | empty |
| W=0 rows | h3: Hc_11_0; C2: C2c_22_0; C3: X + C3c_33_0; B2: B2c_64_0 X + B2c_65_0; A3: A3c_97_0 X + A3c_98_0 |
| Constant entries anywhere | C3 (32,0)=1; h3 (0,8..11)=1,3,3,1 and (4,5)=-8/3; none in A3, B2, C2 |
| h3 top (r=0) | X^3W^8+3X^2W^9+3XW^10+W^11 = (X+W)^3 W^8 = H; no degree-10 part |
| deg bounds from min r | C2<=14, C3<=14, D<=34, C<=35, h3=11 exactly |
| A3 W-exponent | max 32; no row with z=33; degree-33 rows have z=24..32 |
| h physical slots (sympy, h=h3^3+C2 h3+C3) | 178; 18 constant, 160 nonconstant; nonconstant max degree 31 |
| h W=0 slots | (0,0) = Hc_11_0^3 + C2c_22_0 Hc_11_0 + C3c_33_0 (nonconstant), (1,0) = 1 |
| h degree-33 part | exactly H^3=(X+W)^9 W^24; degree-32 part empty; W^33 coefficient 1 |
| Hfact_i_j names | equal the 160 nonconstant (X-exp,W-exp) slots exactly; swapped convention fails |
| h coefficient stats | 9,913 literal terms, max 535 per coefficient, source degree 12 (matches export metadata) |

So the census clarification in the prompt is confirmed from the metadata:
247 base coordinates, 160 Hfact = nonconstant h positions only, 178 slots.
The producer's counts (247 source variables, 407 on the h-lift) are right.
The 7 constant slots other than H^3 and X sit at degrees 5,9,...,29 and are
irrelevant to both the W=0 line and the top form.

Consequences used by the proofs, all now independently established at every
base point over any characteristic-zero field: h(X,0)=X+c with
c=Hc_11_0^3+C2c_22_0 Hc_11_0+C3c_33_0; h_top=H^3; deg h=33;
G(X,0)=X^2+(2c-b/3+B2c_64_0)X+(c^2-bc/3+B2c_65_0), monic quadratic;
G_top=H^6 since deg D<=34 and deg(bh/3)<=33; every P in V_C has
deg<=35, W-degree<=32 and no W^33 monomial. On the unrestricted h-lift
(Hfact free, 18 constants literal) h_lift(X,0)=X+Hfact_0_0 and
h_lift top=H^3, because the only W=0 slots are (0,0),(1,0) and the only
slots of degree>31 are the ten constant H^3 slots.

## Primary paper, read directly

arXiv:math/0608157v2 (PDF SHA256 70429c38...), p.5. Lemma 4: char k=0,
f,g nonconstant are algebraically dependent over k iff the Jacobian matrix
has rank 1 (all 2x2 minors vanish). Lemma 5: "Let k be a field"; f,g
nonconstant are algebraically dependent over k iff there is a closed
h in k[x_1..x_n] with f,g in k[h]; its proof uses Noether normalization and
Proposition 1 (integral closure of k[f] is k[h]), both stated for an
arbitrary field. The producer's interface statement is accurate, including
"over the given field, not merely its algebraic closure". Note that the gate
does not even need this: kernel dimension of a k-linear map is invariant
under field extension, so a closure-only lemma would give the same theorem.
In two variables with G nonconstant in characteristic zero the gradient of
G is nonzero, so rank 1 is exactly J(P,G)=0 for nonconstant P; correct.

## Claim (1): full C kernel is k·1 uniformly, actual source and h-lift

Proof audited step by step; every step holds.
J(P,G)=0, P nonconstant: Lemma 4 then Lemma 5 give G=phi(R), P=psi(R),
R nonconstant. Restricting to W=0, G(X,0)=phi(R(X,0)) has X-degree 2, so
R(X,0) is nonconstant and deg phi divides 2. Total degree: 66=deg phi·deg R.
deg phi=1 forces deg R=66 and deg P=deg psi·66>=66>35. deg phi=2 forces
deg R=33, deg psi=1, and alpha R_top^2=H^6; at X=0 this reads
alpha R_top(0,W)^2=W^66, so R_top has nonzero W^33 coefficient, hence so
does P=lambda R+mu, contradicting the reconstructed support. Kernel = k·1,
and 1 is in V_C (identity slot A3c_98_0). No generic nonvanishing is used;
the argument is pointwise in the base and valid on the h-lift by the slot
facts above, hence on its quotient by the 160 monic definitions.

Own controls (controls.py; exact Fractions, rank mod 2^61-1; a mod-p rank
of 191 with a kernel known to contain 1 pins the Q rank to exactly 191):

- Three actual base points (random integers; D=0,b=0; D=constant 5, b=3):
  deg h=33, deg G=66, G_top=H^6, G(X,0) monic quadratic, full C rank 191.
- CTRL A (transverse line dropped): G=H^6, P=H; J=0; H in V_C verified by
  a span test, not by trusting the 1,3,3,1 assignment; G(X,0)=0.
- CTRL C' (new; coefficient mutation of G_top INSIDE the actual V_C):
  P = basis polynomial of A3c_97_0 = X-56X^4W^9+210X^5W^12-336X^6W^15
  +280X^7W^18-120X^8W^21+21X^9W^24, G=P^2. Then J=0, deg G=66,
  G(X,0)=X^2 monic quadratic, but G_top lacks W^66. So the H^6 top (its
  nonzero W^66 coefficient) is a load-bearing hypothesis, not decoration.
- CTRL B (index mutation, W^33 admitted): P=H^3+X, G=P^2, J=0; P not in V_C.
- CTRL D (restriction degree mutated to 4): P=H^3+X^2, G=P^2, J=0; not in V_C.
- CTRL E: J(X,X^2+W)=1, positive-only kernel is not the full kernel.
- Sign of J is irrelevant to a kernel; X alone is NOT in V_C (A3c_97_0 is
  mixed into six other rows), XW^32 alone is.

Producer script replay, normal mode: rc 0, output SHA256
4f21b2ef4a28af4c264b935c9c9100247b6906fb17c775a390ab25f03265a20f, equal to
the shipped line_support_check.json. All its asserts were re-derived above
by independent code. No optimized mode exists or is claimed.

## Claim (2): positive (C,a) uniqueness only at an actual Keller base

Audited; correct as a conditional theorem. At a base whose G admits ANY F
with J(F,G)=j in k*, deg F=99: a nonconstant Q with J(Q,G)=0 gives
G=phi(R), and j=phi'(R)J(F,R) forces phi'(R) to be a unit, so deg phi=1 and
Q in k[G]. With P=Delta C+(Delta a/2)h and J(P,G)=kappa, Q=P-(kappa/j)F
lies in k[G]; kappa!=0 would give deg Q=99, not a multiple of 66; so
kappa=0, P in k[G] with deg<=35, P constant, and the W^33 coefficient
Delta a/2 (h has W^33 coefficient 1, reconstructed) vanishes. Kernel is the
additive constant only. Only J(F,G) in k* and deg F=99 are used; the
argument survives base points over any extension field.

Hostile check of the C+a block off the Keller locus: the FULL (C,a)
matrix degenerates exactly where J(h,G)=J(h,D)=0. My D=0,b=0 sample and my
D=5,b=3 sample both give (C,a) rank 191 (kernel dimension 2, direction
h-b/6). So the degeneracy locus contains every base point with D constant,
not just the producer's D=0,b=0 example; D=lambda h+mu with lambda!=0 is
impossible (B2 has no W^33 slot). A uniform (C,a) statement is therefore
false on the unrestricted base, as the producer says; the random point had
(C,a) positive-only rank 192, an observation and not a theorem.

## Claim (3): maximal-minor ideal is the unit ideal; polynomial left inverse

Audited; correct. M has 191 columns over A=Q[247 vars] (target_a does not
occur, so even Q[246]) or over the 407-variable lift ring. If the ideal of
191-minors were proper it would lie in a maximal ideal m; A/m embeds in
Qbar, giving a Qbar-point where all minors vanish, contradicting the
pointwise rank 191 from claim (1) at that point. So sum q_S det M_S=1 and
L=sum q_S adj(M_S)E_S gives LM=I_191, which persists under every base
change including nonreduced Q-algebras. The (t,1-t) example correctly
shows this does not produce a constant selected minor, sparse cofactors or
a cheap certificate; none is claimed. The claim is properly separated from
the filtered pilot's chosen 189-minor and from any properness statement.

## Claim (4): 190 constant positive pivots in a W-adapted basis

Audited; the desk lemma is correct. V_0={P in V_C: P(X,0)=0} has
dimension 190 because P(X,0)=A3c_97_0 X+A3c_98_0 with both parameters
free. Echelonising V_0 in the monomial order (W-exponent ascending,
X-exponent descending) yields 190 distinct leading monomials X^i W^r,
r>=1. The identity [W^(r-1)]J(P,G)=-r p_r(X) G_X(X,0) is exact (the
P_X G_W term has W-order>=r), so row (i+1,r-1) carries -2r on the
diagonal; later columns with larger r cannot reach W^(r-1), and same-r
columns with smaller i cannot reach X^(i+1). Lower-triangular for EVERY
G; diagonal -2r whenever G(X,0) is monic quadratic. All rows have degree
i+r>=1. After these 190 pivots one nonconstant coordinate remains and its
Schur-complement column generates the unit ideal by claim (1) plus the
Nullstellensatz; no constant entry follows.

Own instantiation (controls.py), which the producer did not do: the adapted
basis exists with r from 1 to 32, 190 distinct rows, all positive degree.
At two actual G samples the 190x190 selected matrix is upper-zero with
diagonal exactly -2r. Negative controls: G=H^6 (G(X,0)=0) and G=H^6+X
(restriction linear, an index mutation of the row rule) give 190 zero
diagonal entries; G=H^6+3X^2 gives -6r. The symbolic 190-column source
transform over the base ring, its benchmark, and any constant 191-minor
remain unemitted, exactly as the producer states.

## FALLACY-v2 checks and typed OPEN items

Variable/ring map declared and reproduced (X=x, W=y-x, det 1, rows
(r,z,e) -> e X^(N-r-z) W^z, field Q); floors versus exact values kept
separate (rank 191 is exact; 190 pivots is a constructed minor, not a
maximum claim); no sat(), remainder, pole or exit-charge reasoning occurs,
so no charge_basis line is declared. Not inherited: any prior gate's
rejection; the counts were re-derived here and are right.

- OPEN[POSITIVE-ONLY-C-UNIFORM]: uniform rank 191 of the positive-only
  C block (Delta a=0) off Keller bases is neither claimed nor proved; a drop
  would require a nonconstant P in V_C with J(P,G) in k*.
- OPEN[CONSTANT-191-MINOR]: no constant 191-minor or explicit Bezout left
  inverse exists in any artifact.
- OPEN[W-ADAPTED-EMISSION]: the 190-pivot source transform is verified
  only at exact samples here; its universal triangularity is a desk proof.

## Artifacts and custody

Owned, new, read-only after this report:
box/linear-c-transverse-gate-fable5-20260906/ (23,811 bytes total):
census.py ce796b96..., census.out cf02eb7f..., hlift.py e3e7b314...,
hlift.out ef225c24..., controls.py 632a32c7..., controls.out d221469d...,
replay.json 4f21b2ef..., ap_lemmas4-5_p5.txt a77c591a... (pdftotext
excerpt of the fetched primary PDF, SHA256 70429c38...). Runtimes: 0.04 s
replay, 9.6 s sympy h expansion, 12.8 s controls, on the lane host only.
Replay: python3 <script> from any cwd; inputs are read by absolute lane
path. No charged file, worker, ledger or scratch of another lane was
written or read beyond the eight charged inputs. This gate is a
verification of theorem interfaces; it is not a properness, performance,
counterexample or JC2 result.

<!-- BODY-END -->
