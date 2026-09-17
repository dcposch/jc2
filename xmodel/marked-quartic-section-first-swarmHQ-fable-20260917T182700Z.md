# Publication custody note

ROOT publishes the following Fable-authored review verbatim, after independently
verifying terminal process state and collecting its receipt first on September17,
2026. The external lane completed at18:23:46 UTC with exit0, DONE, CLEAN boundary,
and all six charged inputs unchanged. Its original body and receipt are retained
unchanged; the body ends at the completion marker and carries no canonical seal.
This separately named copy adds only this provenance note and the finalizer's
post-body integrity seal. It does not retroactively change the legacy receipt.

Original review body SHA-256:
`0f9732a5a8b5ce8b00c7774af11eced8e29f1d3812e50d0470bbfc69c460013b`.
Original terminal receipt SHA-256:
`172c5727445690e0fb9d2c001b8ced6c55fb4aea890205e8657d3d66054bc3f4`.
Frozen reviewed public commit: `fa27d0de22b0df529a1a9ffcf6dde7b1622bd19f`.
The coordinator's corpus collision check is EMPTY; no new OPEN is raised.
The review's mathematical scope and model-identity qualifications are unchanged.

---

# Independent hostile review: MARKED-QUARTIC-SECTION-1 (marked-quartic section exclusion)

Reviewer: swarmHQ Fable independent reviewer, September 17, 2026 (utc_start
2026-09-17T18:15:42Z). Adapter request: model=fable, effort=max. The exact
hosted model identity is not independently exposed to this lane; the session
self-reports claude-fable-5-1 and this cannot be verified from inside the lane.
Lifecycle: review-only, NO promotion authority; no artifact_finalize, no seal.py
(legacy lane parent owns custody). Evidence: MANUAL mathematical reading only.
No CAS, scientific Python, network, farm, descendants, Git mutation or shared edits.
Frozen public basis: `fa27d0de22b0df529a1a9ffcf6dde7b1622bd19f`.
Reviewed claim: MARKED-QUARTIC-SECTION-1 in
[the producer report](marked-quartic-section-swarmHQ-root-20260917T181100Z.md)
(producer basis `582bf727e707799bb570dfe35a2fd5ec3b71b257`).

## 0. Verdicts

- **Section (Sec. 2, first part):** CONFIRMED. The quartic reconstructed from the
  literal n=4 marked-root formula restricts at x=y=0 to T S^3 + z3 T^3 S + z4 T^4,
  giving (I,J)=(-3 z3,-27 z4), (u,v)=(z3,z4); sigma(a,b)=(0,0,a,b) is a polynomial
  section of q, u,v are algebraically independent, and evaluation at x=y=0 is a
  C[u,v]-algebra retraction R -> C[u,v]. Signs and normalization are right.
- **Relative-algebraic-closure lemma and its application:** CONFIRMED. The general
  lemma (normal domain R, subdomain A0, A0-algebra retraction R -> A0 implies
  Frac(A0) relatively algebraically closed in Frac(R)) is correct as written; the
  application to R=C[x,y,z3,z4], A0=C[u,v] satisfies every hypothesis. I could
  not break it; the two negative controls isolate normality and the retraction.
- **Arbitrary-rational-quotient Keller consequence (Sec. 3):** CONFIRMED,
  conditional on exactly one named import, the classical birational Keller
  theorem (a polynomial map with nonzero constant Jacobian that is birational is
  an automorphism). Its hypotheses are met, and I sketch its standard proof below.
  No hypothesis on rho's generic fibers is missing; the proof never composes rho
  with the section.

Scope limitations are listed in Sec. 6. All verdicts are for the exact statement
with the displayed polynomials as the definition; no upstream Jacobian, degree or
fiber assertion of the marked-root manuscript or of the SL2 report is a premise.

## 1. Reconstruction of the quartic from the literal n=4 formula

The marked-root report defines, with p=1+xy,
Phi(T)=(1-yT)^(n-1)(pT-x)+(pT-x)^2[n y(yT+1/2)+z3(pT+x/2)+sum_{j>=4} z_j T^(j-2)].
At n=4 the producer's homogenization L=pT-xS, V=S-yT,
W=4y(yT+S/2)S+z3(pT+xS/2)S+z4 T^2, Phi=L V^3+L^2 W is exactly this formula at
S=1: L V^3 -> (pT-x)(1-yT)^3 and L^2 W -> (pT-x)^2[4y(yT+1/2)+z3(pT+x/2)+z4 T^2].
Each of L V^3 and L^2 W is homogeneous of degree 4, so Phi=A T^4+B T^3 S+C T^2 S^2
+D T S^3+E S^4 with A,...,E in R=C[x,y,z3,z4] (the 1/2's are scalars).

Coefficient checks (by hand):

- D (coefficient of T S^3, i.e. of T at S=1). From L V^3: pT*1+(-x)(-3yT)
  = (p+3xy)T = (1+4xy)T. From L^2 W with (pT-x)^2=p^2T^2-2pxT+x^2 and
  W(T,1)=z4 T^2+(4y^2+z3 p)T+(2y+z3 x/2): x^2(4y^2+z3 p)-2px(2y+z3 x/2)
  = 4x^2y^2-4pxy (the z3 terms cancel) = -4xy(p-xy) = -4xy. Total D=1. This
  matches the producer's two displayed contributions and the marked-root
  normalization "+T" of the linear term.
- A = p^2 z4 - p y^3 = p(p z4 - y^3), which is the marked-root C4 at n=4.
- B = 3p y^2 + x y^3 + 4p^2 y^2 + p^3 z3 - 2px z4 = (4p^2+4p-1)y^2 + p^3 z3 - 2px z4
  (using x y^3 = (p-1) y^2), which is the marked-root C3 at n=4.
- C = -3y(1+2xy) + 2p^2 y - 8pxy^2 - (3/2)p^2 x z3 + x^2 z4; at p=0, x=rho,
  y=-1/rho this is rho^2 z4 - 3/rho, the marked-root A2 at n=4. E = -x+2x^2y
  +x^3 z3/2, so A0=-E at p=0 is 3rho - rho^3 z3/2, the marked-root A0 at n=4.

So the producer's quartic is the literal n=4 marked-root polynomial. At x=y=0
(p=1): L=T, V=S, W=z3 T S+z4 T^2, hence Phi = T S^3 + z3 T^3 S + z4 T^4, i.e.
(A,B,C,D,E)=(z4,z3,0,1,0). Then I=12AE-3BD+C^2=-3 z3 and
J=72ACE+9BCD-27AD^2-27B^2E-2C^3=-27 z4. With u=-I/3, v=-J/27 the section
values are u=z3, v=z4, so q(sigma(a,b))=(a,b): q composed sigma is the identity
of A2. This includes a=b=0, where Phi=T S^3 has a repeated root; no
discriminant or x!=0 chart is used. Signs: CONFIRMED.

Normalization: the displayed I,J are 12 and 432 times the classical invariants of
a X^4+4b X^3Y+6c X^2Y^2+4d XY^3+e Y^4 (I_cl=ae-4bd+3c^2, J_cl=ace+2bcd-ad^2-b^2e-c^3)
written in unnormalized coefficients, and are byte-identical to formula (4) of the
SL2 quotient report; the section values agree with that report's normal-frame
display v X^4+u X^3 Y+X Y^3 with (X,Y)=(T,S). SL2-invariance and the classical
normalization are NOT load-bearing here: the statement is about the fixed
polynomial map q, and only the displayed polynomials enter the proof.

Algebraic independence: if F(u,v)=0 with F in C[U,V], pulling back along sigma
gives F(a,b)=0 identically, so F=0. CONFIRMED. Retraction: epsilon(f)=f(0,0,a,b)
with a,b renamed u,v is a C-algebra map R -> C[u,v] with epsilon(u)=u,
epsilon(v)=v, hence the identity on A0=C[u,v]; kernel (x,y). CONFIRMED.

## 2. The general lemma

Hypotheses: A0 a domain, R a normal domain containing A0, epsilon: R -> A0 an
A0-algebra retraction; K=Frac(A0), M=Frac(R), R_K=(A0\{0})^(-1)R.

- R_K is a localization of a normal domain, hence normal, with R subset R_K
  subset M, so Frac(R_K)=M. Correct.
- epsilon_K(r/s)=epsilon(r)/s is well defined (if r/s=r'/s' then rs'=r's, apply
  epsilon, use epsilon(s)=s, epsilon(s')=s') and is a K-algebra map R_K -> K
  restricting to the identity on K. Correct.
- alpha in M algebraic over K has a monic minimal polynomial over K subset R_K,
  so alpha is integral over R_K and lies in R_K by normality; alpha^(-1) is
  algebraic over K too, so nonzero algebraic elements are units of R_K. Correct.
- The relative algebraic closure K' of K in M is a field inside R_K. For alpha
  in K', beta=alpha-epsilon_K(alpha) lies in K' (both terms do) and
  epsilon_K(beta)=0 because epsilon_K is the identity on K. If beta!=0 it is a
  unit of R_K and epsilon_K(beta)epsilon_K(beta^(-1))=1, contradicting
  epsilon_K(beta)=0. Hence K'=K. Correct.

Equivalent cleaner finish: epsilon_K restricted to K' is an injective K-linear
map K' -> K, so dim_K K' <= 1. The lemma is the classical fact that a normal
integral K-variety with a K-rational point has K algebraically closed in its
function field, here applied to the generic fiber Spec R_K of q with the
K-point induced by sigma. No hidden hypothesis. CONFIRMED.

Application: R=C[x,y,z3,z4] is a UFD, hence normal; A0=C[u,v]; epsilon as in
Sec. 1. So C(u,v) is relatively algebraically closed in C(x,y,z3,z4). CONFIRMED.
The producer's equivalence with geometric integrality of the generic fiber
(finitely generated extension in characteristic zero: K algebraically closed in M
iff M tensor_K Kbar is a domain, separability automatic) is standard and, as the
producer says, unused.

## 3. The Keller consequence and the undefined-section trap

Let rho=(r,s) with r,s in M, H=(H1,H2) in C[X,Y]^2 with det Jac(H) in C^*, and
H composed rho = q as rational maps. Equality of rational maps to A2 is equality
of the pulled-back coordinates, so H1(r,s)=u and H2(r,s)=v in M. Hence
K=C(u,v) subset N=C(r,s) subset M.

- N/K is finite: trdeg_C K = 2 = trdeg_C N forces N algebraic over K, and N is
  generated over K by r,s. The producer's route (nonzero Jacobian in
  characteristic zero makes H1,H2 algebraically independent, so C(X,Y)/C(H1,H2)
  is finite, and X->r, Y->s is an isomorphism C(X,Y) -> N carrying C(H1,H2)
  onto K) is also correct. Dominance of rho is in fact automatic from the
  identity, since q is dominant; assuming it is harmless.
- K relatively algebraically closed in M and N algebraic over K give N=K, so
  C(H1,H2)=C(X,Y): H is birational. Correct.
- Classical birational Keller theorem: H polynomial, det Jac(H) in C^*,
  birational, therefore an automorphism. Hypotheses are met exactly. Independent
  sketch: H is etale and birational, so by Zariski's main theorem an open
  immersion onto U subset A2; a curve in A2\U would supply a nonconstant unit
  on U, hence on A2, impossible; so codim(A2\U)>=2, C[U]=C[X,Y] by Hartogs, and
  H^* is an isomorphism. This is Keller's own 1939 birational case; I treat it as
  the named import the producer declares and do not consume AUDIT.md for it.
- (I,J) in place of q: if H composed rho = (I,J) = Lambda composed q with
  Lambda(u,v)=(-3u,-27v), then Lambda^(-1) composed H is Keller with
  (Lambda^(-1) composed H) composed rho = q, so it is an automorphism and so is H.
  Correct.

Undefined-section trap: rho may indeed have components like z3/x, undefined on
the whole plane x=y=0. The proof never evaluates r or s along sigma. The only
evaluation is epsilon_K on elements of R_K, i.e. polynomial numerators over
nonzero denominators in C[u,v], which is always defined. A posteriori the lemma
shows r,s themselves lie in R_K (they are algebraic over K), so a component
like z3/x is transcendental over C(u,v) and cannot occur. CONFIRMED that the
argument avoids the trap.

Missing hypothesis on rho's generic fibers: none. The argument uses only that N
is a subfield of M algebraic over K. Whether N is relatively algebraically
closed in M (the generic fiber of rho) never enters, in contrast with the
two-endpoint condition of the connected-quotient tower theorem in the frontier.
CONFIRMED.

## 4. Negative controls

- **a^2 - t b^2.** Irreducible in C[t,a,b] because t b^2 is not a square in the
  UFD C[t,b], so D=C[t,a,b]/(a^2-t b^2) is a domain. The map a,b -> 0 is a
  C[t]-algebra retraction D -> C[t] (the relation lies in (a,b)). In Frac(D),
  (a/b)^2=t, and t is not a square in C(t), so C(t) is not relatively
  algebraically closed: the conclusion fails. Nonnormality: a/b is integral
  (root of X^2-t); if a/b were in D it would be homogeneous of degree 0 for
  deg a=deg b=1, deg t=0 (quotient of homogeneous elements in a graded domain),
  so in D_0=C[t], and d(t)^2=t is impossible. The producer's compressed sketch
  is this argument. Valid control isolating normality. CONFIRMED.
- **C[x^2] subset C[x,y].** Normal source; x is algebraic over C(x^2) and not in
  it; a C[x^2]-algebra retraction would need h(w)^2=w in C[w], impossible, and
  no polynomial section of x^2 exists. Valid control isolating the retraction.
  CONFIRMED.
- **Repeated-root point.** sigma(0,0) gives Phi=T S^3, I=J=0; the section and
  retraction are global, no localization. CONFIRMED.

## 5. Boundary, distinctions and comparison

- **Fixed target map.** The exclusion is exactly the quotient direction: any
  factorization q = H composed rho with rho a dominant rational quotient and H
  Keller forces H to be an automorphism. The producer's disclaimer for maps
  A2 -> A4 is necessary and correct: h(a,b)=(0,0,f,g) gives q composed h=(f,g),
  so precomposition realizes EVERY polynomial pair, including any hypothetical
  counterexample; nothing about that direction is or can be claimed.
- **Old slices.** The marked-root report classifies fibers of (C3,C4) over
  constants and substitutions A2 -> A4 landing in them, with target (A2,A0).
  The present target is (u,v)=(-I/3,-J/27) and the object is a quotient, not a
  substitution; no plane component of a slice is assumed. Distinct. CONFIRMED.
- **SL2 quotient source.** That report's source is the resultant-one variety
  Z = SL2 x A2 with its own u,v; its invariant-ring identities and the upstream
  map's Jacobian/degree/fiber assertions are not used here, and I did not audit
  them. (Observation only, not used: Phi=L(V^3+LW) with det(L,V)=p-xy=1 and
  (V^3+LW)(x,p)=1, so A4 maps into Z; this is consistent with, but not a
  dependency of, the section computation.) The producer's statement that the
  SL2 result does not transfer a generic-fiber statement to A4 by itself, and
  that the section supplies the whole-source attachment, is accurate.
- **Frontier.** APPROACHES.md (pinned) records the SL2 quotient and the
  connected-quotient tower theorem (both endpoint generic fibers geometrically
  integral). The present claim needs only the target-side closure, obtained from
  the section; it does not overlap or contradict those entries. It is not a JC2
  reduction and gives no construction.

## 6. Scope limitations and residual remarks (no GAP raised)

- One named import: the classical birational Keller theorem. Everything else is
  displayed elementary algebra that I recomputed by hand.
- Strength: because q has a polynomial section, the result is a closure of a
  route that could never have produced a counterexample by quotienting; it is
  correct but weak, as the producer's own boundary list already implies.
- Not covered, per the producer and confirmed: other projections/targets, other
  target subfields, arbitrary maps A2 -> A4, other donors or degrees, special
  fibers, global bundle or inverse statements.
- The producer cites a Sol review hash (63d08b15...) for the SL2 report; that
  file is not a charged input and I did not verify or consume it.
- I did not audit the marked-root scheme classification or the SL2 invariant
  ring beyond the coefficient identities recomputed in Sec. 1.

FALLACY-v2 check: ring map declared (R, A0, R_K, epsilon, epsilon_K) with
generator names and coefficient field; no sat(), remainder, pole or exit-price
step occurs; no charge_basis line is required; no OPEN raised by analogy or cap.

## 7. Integrity record (custody evidence, not mathematical proof)

- Pre-read and post-read SHA-256 of all six inputs in /tmp/jc2-lane.nr710K/inputs
  matched the charged pins (sha256sum, read-only): producer
  `31a05849a5b5dba8a249be386133894dfe9f761d7f9021c91282863b4e8fcdaa`;
  marked-root `a56a1de74b34a283e1c4f32bc4e316f0da372f4c75a18c60afd1fd96589333e5`;
  SL2 `f5781c10bbc848ef39b140312b8f0d8e3871a6df0cd1f4208f661566fc4fa593`;
  FALLACY-v2 `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5`;
  COORDINATION `9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e`;
  APPROACHES `9f0bdd52a554475c30e6e5df497f7c9685a74f1ecb9a190e221c22f77cb3783d`.
- Read limits: the three reports, FALLACY-v2 and COORDINATION were read in
  full; APPROACHES was read by grep and lines 160-260, 300-340 for scope and
  history comparison only. No other live report, log, ledger or receipt was
  consumed; no source retrieval; jc2-lean and jc2-web untouched.
- Outputs: /home/ubuntu/swarmHQ/runtime/marked-quartic-review-20260917/FABLE-STARTUP.md
  (apply_patch, chmod 444) and this report (apply_patch). No other writes.

## COLLISIONS

status: EMPTY

- NONE -- this review raises no OPEN[...] entry and commissions no successor.
  Producer block: EMPTY; comparison: consistent, no collision. This block was
  written manually because the lane permits only read-only shell and
  apply_patch; ops/open_collision.py was not run.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `16020`.
- Body SHA-256:
  `582f9d34e09564142f5dcbe69f8dc500cc6811a6e0ac80da61b7f5d924f60b0f`.
- Frozen basis: `fa27d0de22b0df529a1a9ffcf6dde7b1622bd19f`.
