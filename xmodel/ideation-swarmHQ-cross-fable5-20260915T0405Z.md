# FULL0405 adversarial cross — Fable5.1

Round 20260915T0405Z; cross publication basis 8532cd5896d780b3d0be73e5b78bcd8d5beeaee8;
scientific packet basis 6f8d50d5c0b7a20e945cb3acdc7ac8bffbd4656f. External lane
custody (no artifact_finalize, no seal.py). MANUAL, UNPROMOTED; no computation,
no peer cross report, no web, no ledger. Started 04:27:47 UTC; supervisor 600 s.

## 0. Custody: eight charged inputs read WHOLE

Read from `/tmp/jc2-lane.wTBVGZ/inputs`; every pre-read hash matched CROSS.md.
COORDINATION.snapshot.md (41 KB) was read in two byte ranges (1--21000,
21001--end) to pre-empt clipping; the join "ideatio|n round" was verified.
No read clipped; no repair was needed. Post-read hashes are in Section 8.

```text
2c99ec4475d13d06c439954f0aad0778b3ca54f2d572ba9641da7066e9623607  CROSS.md
a91dc40b94a542c95f4aeb667c93eed57e65f7cecab9760d6a0be4b10822d6aa  ideation-swarmHQ-root-20260915T0405Z.md
736e0a98982f276d59dc3e37f645ca397e6884d733bfa20d93c7c3d6353f717c  ideation-swarmHQ-astra-20260915T0405Z.md
aca2ec441f67f63ca69463356476b08dcf4feeec74851d0513684dc3f718384b  ideation-swarmHQ-fable5-20260915T0405Z.md
7598d814832d75bb59fa5c623b137713cb9336b1818c4388df8bbd5cca93fc81  AUDIT-DELTA.md
4ce5b29af5a70e096a04b942cb978b1df425f9f0648decb720ec1f089ff37ac4  COORDINATION.snapshot.md
50cf45483cddf637e717ddfa2d136be4df074d13d360b851c1fb62a9e73edb0a  SWARM-POLICY.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
```

<!-- SKELETON-END -->

## 1. Verdict

NO_NEW_CLOSING_TEST. Combining the blinds exposes only the already-missing
actual-source bridge (normality/finiteness of R over A; equivalently, the
p!=0 normalization S has no missed prime). Three Fable-blind statements are
corrected below; each sharpens a scope record, none changes a decisive test.

## 2. Q1: Fable Section3(a) is FALSE as stated

Torus weights are not ordinary degrees. F=(x+y^3, y, z) satisfies
F(t^3x, ty, z)=t.F(x,y,z), so it is equivariant for weights (3,1,0), and
also for (3,1,-4), which is effective with trivial determinant character.
Correct rule: x+H (H cubic homogeneous) is T-equivariant iff every monomial
of H_i has the weight of x_i; only the scalar torus is excluded by degree.
What fails is the smooth-quotient hypothesis: for (3,1,-4) the invariants are
C[xyz, y^4z, x^4z^3]=C[p,q,r]/(p^4-qr), an A_3 singularity, not C[u,v].
Corrected interface record: SCOPE MISMATCH with a nonempty consumer, not
NO HIT. For block weights ((1,-1,0) in n=3; (1,0),(-1,0),(0,1),(0,-1) in n=4)
all VNTQ-1 hypotheses hold and the equivariant maps are exactly
x_i*phi_i(u,v) with u,v the block products (n=3: H=(a x^2y+b xz^2,
c xy^2+d yz^2, e xyz+f z^3)); VNTQ-1 makes their Keller members automorphic.
A thin slice: no reduction supplies such a T for an arbitrary cubic map.

## 3. Q2: condition N is LPD-1 at first-leg degree1

Specialization audit: p=f, q=g, m=deg_u g=[C(f,u):C(f,g)] (automatic for a
degree-m polynomial in a transcendental u), embedding C(f,u)=C(x,y). Valid.
The rewrite "no w in R, M with f^M g=Phi(w), Phi monic of degree d over
C[f,1/f]" is equivalent ONLY with the field-generation clause C(f,w)=C(x,y)
(equivalently deg Phi=d=[C(x,y):C(f,g)]) retained; Fable dropped it. Without
it the statement is LPD-1 at first-leg degree d/deg Phi>=2, the theorem's
original proper-block scope. So N is a specialization either way, never a
new landing. The step u in R_f (u integral over A_f, R_f normal) is correct.
The "strict position between Abhyankar--Moh and Chau" is UNSUPPORTED here
(neither source is a charged input), not refuted.

Chain-rule remark (MANUAL, unreviewed, no promotion): with g=G(f,u),
1=J(f,g)=G_U(f,u)*J(f,u); both factors lie in R_f, so G_U(f,u) is a unit of
R_f. G_U has u-degree d-1>=1 over C(f) and u is transcendental over C(f), so
G_U(f,u) is not in C(f). For irreducible f, R_f^*=C^* f^Z lies in C(f):
contradiction. Hence N for irreducible f is three lines; the reducible case
is LPD-1's own content. Either way OPEN[LPD1-SELF-COMPOSITION-HISTORY]
resolves KNOWN; ROOT's documentary checksum closes it at zero research
allocation. The tranche request is withdrawn.

## 4. Q3: Section5's implication (ii) is vacuous

f is a unit of A_f, hence of S, so div_S(f)=0 and "P a component of
div_S(f)" is impossible. Corrected argument: if nP=div_S(s) with P missed by
Spec R_f, then s in R_f has no codimension-one zero, so s is a unit of R_f.
For irreducible f, s=c f^j is a unit of S and nP=0: contradiction. So every
missed prime is NON-torsion in Cl(S), and the sole surviving sub-target is
(i): Keller forces no missed prime. That is the single-pair bridge in
class-group form; LPD-1 got it free from m*Cl(S)=0 (cyclic quotient) and the
actual source does not. R_f^*=C^* f^Z holds only when f is a constant times a
power of one irreducible; with r>=2 distinct factors R_f^* is C^* x Z^r and
the factors need not lie in S, so the step fails. Exact remaining premise: a
Keller f is non-composite (df is nowhere zero, excluding f=a(h) with
deg a>=2), so f-c is irreducible for all but finitely many c, and the route
fixes such a translate at the outset. No assumption on every fibre, no
weakened-ring family. The proposed EXACT-VOLUME-NO-COORDINATE-1 test of
(ii) is ill-posed: the corrected argument predicts a non-torsion missed
class on any such ring, Keller or not, so it separates nothing.

## 5. Q4: avenue34 and allocation

The four exclusions (rational mate, monomial target, fixed triangular twist,
Laurent donor) each close a registered scope; LPD-1 itself records no
arbitrary leading coefficient, no rational u-dependence, no multi-pole
twist. A negative result closes only its scope: the avenue stays UNCHANGED,
and the COORDINATION two-tranche rule STOPS family expansion as scheduling,
which is what Fable's "lower" actually meant. ROOT/Astra's disposition is
the precise one. The history check earns no allocation (Section3).

## 6. Q5: paging

Bounded reading tactic (lane side, no custody change): read any input above
about 20 KB in byte ranges from the first read; the existing pre/post
whole-file hash already attests coverage. Measurement: Fable blind, 115 KB
file, one clipped read plus two repairs; this cross, 103 KB over eight files
with pre-emptive ranging, zero clipped reads. Runner change (page files plus
SHA256SUMS.pages): REJECTED. It alters the charged-input set and receipt
custody; "no regression risk" is unjustified, since either the validator
ignores unpinned files or the receipt format changes. NO_UPGRADE; prompt
guidance only; the original48-hour systems debt is retained.

## 7. Ranking, connection, decision

By content: Astra (complete per-ID table, correct scope composition) >=
ROOT (correct; sharpest on the missing target-compatible presentation) >
Fable (most concrete; three errors corrected here, an unlicensed lower, an
untested custody change). Cross-avenue connection: the corrected Q3
argument shows exactly where LPD-1 used its source (Cl(S) torsion from the
cyclic quotient), placing avenue34's mechanism inside avenue31's bridge;
the corrected Q1 gives 35/17 a thin nonempty consumer. Decisive test: NONE
scientific. CONTINUE the single-pair bridge with (i) as its honest form.
REDESIGN launch criteria as ROOT states. STOP donor expansion, genus/metric
successors, the (ii) control and the runner paging change. No OPEN raised,
no exit price, no charge_basis.

## 8. COLLISIONS (own-report checker, exit0 at 04:34:55 UTC) and post-read hashes

```text
## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.
```

EMPTY is lexical only. Post-read hashes at 04:34:55 UTC, all eight unchanged:

```text
2c99ec4475d13d06c439954f0aad0778b3ca54f2d572ba9641da7066e9623607  CROSS.md
a91dc40b94a542c95f4aeb667c93eed57e65f7cecab9760d6a0be4b10822d6aa  ideation-swarmHQ-root-20260915T0405Z.md
736e0a98982f276d59dc3e37f645ca397e6884d733bfa20d93c7c3d6353f717c  ideation-swarmHQ-astra-20260915T0405Z.md
aca2ec441f67f63ca69463356476b08dcf4feeec74851d0513684dc3f718384b  ideation-swarmHQ-fable5-20260915T0405Z.md
7598d814832d75bb59fa5c623b137713cb9336b1818c4388df8bbd5cca93fc81  AUDIT-DELTA.md
4ce5b29af5a70e096a04b942cb978b1df425f9f0648decb720ec1f089ff37ac4  COORDINATION.snapshot.md
50cf45483cddf637e717ddfa2d136be4df074d13d360b851c1fb62a9e73edb0a  SWARM-POLICY.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
```

All sections complete; none typed OPEN for time. Tools: input reading and
hashing, date, apply_patch, own-report reading, `ops/open_collision.py` on
this report only. No web, peer cross report, computation, AWS, nested agent,
Git or code mutation; both nested repositories untouched.

<!-- BODY-END -->
