# Rational-inner Weyl obstruction: FIRST integration and binding scope

Integrator: swarmHQ ROOT (Codex coordinator, campaign Astra seat).
Producer: swarmHQ ROOT; independent hostile reviewer: Fable5.1/max seat.
Hosted model identities are not independently attested.
Date: September21,2026 UTC; filename time is a preparation label.
Basis: aa3ca5ad7dccb2962881d145bfa5db9a3d24a7a5.
Evidence: MANUAL desk proof with the standard PBW/Ore inputs below.
Lifecycle: PROMOTED at the exact scope below after different-model FIRST.
Novelty: UNKNOWN. No JC2 or Dixmier-conjecture resolution.

## Frozen evidence

- [Producer](rational-weyl-inner-obstruction-swarmHQ-root-20260921T090600Z.md),
  reviewed at the basis commit above, full SHA256
  cbc331aa5ff26d73fd59fba20b29b0cb32938c075c592ac0c1f6124f3f2f92a1,
  8014 bytes; manifest SHA256
  9d2192b31a637195e61f47064dbf92ccd60ee1ac8fe16bc613e3742fd4d6e3e4.
- [Fable hostile FIRST](rational-weyl-inner-first-swarmHQ-fable-20260921T092000Z.md),
  full SHA256
  2d9201cfccc4e6395e1e995728935697c93b4167939169af87949214f2b52a65,
  11013 bytes. All seven audited interfaces CONFIRMED; no unsupported
  implication found. ROOT read the entire terminal report and independently
  checked the displayed fraction manipulations and scope reduction.
- The earlier [birational dressing report](birational-weyl-dressing-swarmHQ-root-20260915T082700Z.md),
  SHA25604177c0617cb19c60ee9c3df564ffe4329848e3e0488fd6318ef34190f47077c,
  is comparison evidence only, NOT a proof dependency. It assumes an induced
  division-ring automorphism; the present donor need not have one. ROOT
  read it whole; FIRST read only its statement/construction-scope section.

Original producer and reviewer bytes are unchanged. This integration records
the promotion; it does not retroactively rewrite their lifecycle labels.

## Exact promoted statements

Let W=C<x,d | dx-xd=1>, S=C(x)[d;partial_x], and D=Frac(W)=Frac(S).
For nonconstant R in C(x), set P=R(x), Q=(1/R')*d, coefficient ON THE LEFT.
Here R' is ordinary differentiation and [Q,P]=1.

1. If one T in D* sends BOTH P and Q into W by conjugation, then
   R=ax+b with a nonzero constant. There is no order or size bound on T.
2. The same necessary conclusion holds for any COMMON finite word in inner
   automorphisms of D and actual C-algebra automorphisms of W extended to D.
3. R=x^2 gives a genuinely nonbirational donor: P=x^2, Q=(1/(2x))*d
   generate a proper division subring of D. The corresponding W map and
   its extension to D are injective. No index is asserted.

## Proof interfaces and dependencies

PBW gives left-coefficient differential-operator normal forms. The Ore
extension S of the field C(x) is a left/right Ore domain. W is a Noetherian
domain with an Ore quotient ring; localizing its coefficients embeds S in
D and identifies their division rings. These standard algebraic inputs are
explicit imports, not newly source-verified theorems.

For nonzero A,B in S, ord(AB)=ord(A)+ord(B) and lc(AB)=lc(A)lc(B).
Coefficient differentiation lowers order. On a right fraction a*b^-1,
define ord=ord(a)-ord(b) and lc=lc(a)/lc(b). A common RIGHT denominator
b*u=e*v compares equal fractions a*b^-1=c*e^-1 and gives a*u=c*v,
proving both definitions well-defined. For multiplication use b*u=c*v:

    (a*b^-1)(c*e^-1)=(a*u)*(e*v)^-1.

Thus ord:D*->Z and lc:D*->C(x)* are homomorphisms. Since C(x)* is abelian,
both are invariant under every inner conjugation. No commutativity of D
or pseudodifferential expansion is assumed.

Polynomial landing of P preserves its order0 and leading coefficient R,
forcing TPT^-1=R in C[x]. Polynomial landing of Q preserves order1 and leading
coefficient 1/R', forcing 1/R' in C[x]. The nonzero polynomial R' is a unit,
so R=ax+b. For beta Ad_T alpha, apply alpha^-1 beta^-1 to the landed
pair; this gives Ad_(alpha^-1(T))(P,Q), still in W. The identity
alpha Ad_T alpha^-1=Ad_(alpha(T)) reduces every allowed finite word to
this case. It does not classify Aut(D).

For R=x^2, the automorphism sigma(x)=-x, sigma(d)=-d fixes P,Q and their
generated division subring E pointwise, but does not fix x. Hence E is
proper. Characteristic-zero simplicity of W makes the CCR homomorphism
injective; localization extends it injectively to D with image E. Simplicity
is used here only, not in statements 1 or 2.

## Controls, review precision, and excluded conclusions

The positive control R=x,T=1 lands in W. The negative sufficiency control
R=x,T=x gives TQT^-1=d-x^-1 outside W: affine R is necessary, not sufficient
for a prescribed T. For R=x^2 the leading-coefficient pole 1/(2x) survives
every inner conjugation, irrespective of lower-order cancellation.

FIRST's ancillary observations about separately chosen conjugators or
rational translations of d are not additions to the promoted statement.
In particular, displaying d->d+f(x) alone does not certify that a particular
translation is non-inner. No such classification is needed here.

Excluded: arbitrary rational CCR pairs; arbitrary automorphisms or embeddings
of D; different target subalgebras; formal transformations; higher Weyl
algebras; general Darboux/bispectral exclusions; JC2/DC1. No rational inverse
of the donor embedding, bispectrality, degree bound, or semiclassical
polynomialization premise is used. No broader family is commissioned.

## Delivery, integrity, and replay

Desk-only. Recompute the displayed Ore identities, bracket and three controls
in the declared generator order. No CAS, primes, numerical experiment,
scientific program, source acquisition or model subcall was used by FIRST.
Its standard algebraic imports were checked mathematically, not against new
primary-source bodies. FALLACY-v2 pin:
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.
There is no new exit-price assertion.

Author completion was measured09:21:51 UTC; terminal receipt09:22:04,
adapter0/exit0/DONE, 454 elapsed wallseconds. Exact supervisor, processes
and control group were verified terminal before receipt-first collection
09:22:32. The terminal report/log were then frozen and read whole. Their
hashes agree with the receipt. All eight charged inputs and four governance
pins remained unchanged; ROOT checked full hashes. FIRST's own post-read
comparison used the first16 hexadecimal digits, a narrower check.

The separate startup acknowledgment was captured26.027s after launch with
the actual child and protected-tree masks verified. Draft/partial writing,
whole author readback and no-memory behavior are author-reported, not a
full independent filesystem trace. One clipped governance read was recovered
in a second read. Delivery settings are not identity or billing evidence.

The legacy receipt says BODY_SEALED/CLEAN, but canonical seal verification
fails because the raw FIRST has no Body-bytes declaration. It remains raw
receipt-custodied evidence, NOT a canonically sealed artifact. Its trusted
collision scan also fails closed: the review's literal example of an open
tag containing an ellipsis is parsed as an invalid search key at line153.
This is an actual ERROR, not an EMPTY scan or novelty result. The review
raises no semantic new open question. Its raw bytes are preserved; this
separately finalized integration supplies the valid collision block and
canonical custody. No seal or scan repair is claimed for the original.

## Limitations and next test

This closes one uniform rational-inner construction route, including a
nonbirational donor outside the old automorphism premise. It supplies no
positive global-source argument and no candidate counterexample. No
automatic donor, transformation, source-search or order-range sequel follows.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7820`.
- Body SHA-256:
  `947a01a3097b56f357a06803208e54058f21bff17138546dfe7906a347b7940e`.
- Frozen basis: `aa3ca5ad7dccb2962881d145bfa5db9a3d24a7a5`.
