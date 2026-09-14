# Bounded actual-map discriminator: generic cubic auxiliaries

ROOT assignment issued September11,2026 at approximately12:53UTC. First action
time must be recorded. Publication reserve13:07UTC; absolute hard stop13:10UTC,
not reset. Research, not review or promotion; no execution authority.

## Exact question

Let k be algebraically closed of characteristic zero, and let
F:A^n_k -> A^n_k be a polynomial Keller map, n>=2, with geometric degree N>=3.
For V_d=k[x_1,...,x_n]_(total degree<=d), d>=3, decide this proposed statement:
there is a nonempty Zariski open O in V_d such that every h in O is primitive
for k(x)/k(F) and j_h=(h,F) has an irreducible divisorial component D of
j_h^-1(Sing Z_h), Z_h=closure(j_h(A^n)), with F^-1(F(D)) != D.

This is an unconditional implication about ANY hypothetical actual Keller map,
not a parameter cover or bounded-total-degree search for F. The auxiliary's
cubic degree must not be confused with a degree bound on F. Prove, refute, or
type the exact gap. Do not assume such a noninvertible F exists.

## Candidate mechanism to attack

Shrink the target to a nonempty U on which F is finite etale of degree N.
Use its finite etale full-labeling cover, choose N distinct source points in
one fibre, and impose exactly one equality h(p1)=h(p2), every other unordered
pair unequal. In V_3, evaluation differences for distinct unordered pairs
should not be proportional: separate at most four points by a linear form
and interpolate a polynomial of degree<=3. The single equality can also be
made transverse as the target point varies, using cubic Hermite interpolation
at p1,p2. The incidence projection should therefore have nonempty open image
in V_d. At the resulting fibre, p1,p2 collide, while p3 is a smooth graph point;
a divisor through p1 then cannot be saturated for F. Check algebraic openness,
primitivity, graph smoothness at p3, and global closure carefully. In particular
the required saturation is for F, NOT for j_h; irreducibility of the double
curve does not include the remaining N-2 sheets.

Prior accepted17zd only proves persistence of an ALREADY WITNESSED bad divisor
under h' = a(F)h+b(F), a nonzero, and gives a torus cubic-cover countercontrol
to a generic linear combination of two auxiliaries. It expressly did NOT
prove generic failure for every actual Keller map. Do not simply reissue it.
No need to reread/review it; prove the current statement self-contained.

Required controls: degree-one F; the N=2 missing-third-sheet boundary; a
non-Keller finite etale open e(x,y)=(x^3,y) on G_m x A1 with h=x (good) versus
h=x^2+lambda*x, lambda!=0 (bad); do not assert ALL h fail, nor use the BGV
automorphy theorem to prove this proposed genericity statement circularly.
Do not expand to degree2 optimization or another generic projection farm.

## Deliverable and boundaries

Own only box/bgv-generic-cubic-collision-astra-20260911/ (TASK is ROOT-owned)
and transactional xmodel/bgv-generic-cubic-collision-astra-20260911.md plus
its manifest. Frozen basis0d39df3c9fd69c939a8420c54d03228b9077777d. TASK is the
sole scientific input; hash before WHOLE read/reuse and at completion. Ordinary
metadata/hashing/artifact_finalize transactions only. NO scientific execution
of any size, imports/AST/syntax/test/dummy/CAS; no network, AWS, agents, process
inspection, shared ledgers, unrelated paths or protected jc2-lean access.

Use artifact_finalize begin/close/finalize/expected verify. First skeleton must
omit completion marker; bounded sections separately, final BODY-END only at
completion. Preserve original reserve/hard; if incomplete, bank exact GAP.
At completion write PINS.json and custody.json with original clocks, all input/
report/manifest pins and expected transaction; last return custody SHA and
COMPLETED/all writers IDLE. ROOT must observe terminal state before custody
FIRST/report consumption. No novelty claim, theorem promotion, actual source
point, JC2 conclusion or global strategy reset.
