# Independent bounded co-research: Liouville primitive as field generator

ROOT task issued September12,2026 at12:09UTC. Astra primary co-research,
not different-model FIRST. This is an independent proof/disproof attempt,
not reliance on a promoted ROOT assertion. JC2 remains unresolved.
Original reserve12:25UTC / HARD12:28UTC, NEVER reset; finish early if decisive.

Exactly one scientific report:
xmodel/liouville-primitive-element-astra-20260912.md.
Use the existing artifact_finalize begin/close/finalize/expected verify
transaction, writing only its leased private partial via apply_patch.
Administrative PINS/custody in this TASK directory are allowed; do not
modify TASK, any shared ledger, existing artifact or old task output.
Read/hash COORDINATION.md first, then this TASK, both WHOLE. Protocol pin
33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597;
TASK expected pin will be in the invitation. No other mathematical input.
Basis0d39df3c9fd69c939a8420c54d03228b9077777d.

Candidate theorem to attack from scratch:
Let f,g in C[x,y], J(f,g)=1, and let S in C[x,y] satisfy
dS=x dy-f dg (exists by polynomial Poincare). Is
C(f,g,S)=C(x,y) ALWAYS true? Constants in S do not matter.
If it is false, give a genuine counterexample or locate the precise gap,
not a hypothetical noninvertible Keller map. No JC2 conclusion is claimed.

ROOT's possible proof route (unreviewed, check every arrow):
Set K=C(f,g,S) and E=x partial_x. The derivations partial_f,partial_g
extend uniquely over the finite characteristic-zero field extension K/C(f,g).
The identities S_f=-x g_x and S_g=x f_x-f would imply E(f),E(g) in K,
hence E(K) subset K. For every polynomial in K, finite interpolation in E
would put each homogeneous x-weight component in K. In particular, writing
f=sum x^i f_i(y), g=sum x^j g_j(y), one gets f_0,g_0,x f_1,x g_1 in K.
At x=0 the Keller equation is f_1 g_0'-f_0' g_1=1. A polynomial Luroth
argument would give C(f_0,g_0)=C(h(y)) with f_0,g_0 polynomials in h;
h' then divides1, forcing deg h=1. Thus y in K and at least one of
x f_1,x g_1 is nonzero, forcing x in K.

Required output:
1. Exact proof or gap for this FULL characteristic-zero plane statement.
   Supply the polynomial Luroth step, including constant coefficient cases;
   do not assume rational generator is already polynomial. Check descent
   of E without assuming the C* action integrates on K beforehand.
2. A genuine negative control for a stronger reading. In particular do
   NOT assert C[f,g,S]=C[x,y], finiteness, graph normality, injectivity,
   divisor saturation, or a JC2 result from field generation. If an actual
   stronger counterexample would require a JC2 counterexample, say GAP,
   not REFUTED. A punctured-plane or formal control must retain that label.
3. Is there any immediate NEW source-level consequence beyond an arbitrary
   generic primitive auxiliary? The special form dS=xdy-fdg is important,
   but do not manufacture a missing global condition. Keep this to a short
   final section; no broad speculation/family extension or descendant.

Scope: manual mathematics only. No scientific interpreter/CAS/import/AST/
syntax/test/helper, network/AWS/SSH, agent or protected-tree operation.
Inert hashes, text, current clock and existing administrative finalizer
are allowed. NEVER enter/enumerate/search/read/status/control jc2-lean or
the public mirror. No general corpus search. ROOT handles literature.
All file edits apply_patch only; no heredoc/shell redirection/tee/printf
file writes. Max scientific body about9000bytes; quantity/scope/control,
own WHOLE readback and all input postpins before unique BODY-END LAST.
No charge_basis declaration (no exit price asserted). No canonical OPEN.
Report final/manifest WHOLE and expected verify, custody FIRST hash and
ALL WRITERS IDLE with actual UTC before FINAL. Do not revise after idle.
No promotion, second gate or further lane is authorized by this task.
