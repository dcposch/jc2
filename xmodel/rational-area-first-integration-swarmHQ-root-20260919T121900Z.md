# Independent FIRST of the rational area/invariant theorem

Independent reviewer: Fable5.1, requested through the campaign's Claude adapter.
Integration and binding scope corrections: swarmHQ ROOT/Astra.
Date: September 19, 2026 UTC.
Evidence: MANUAL, different-model hostile review; model identity is not proof.
Verdict: all six charged proof interfaces CONFIRMED, subject to the
corrections to added REVIEWER wording in section3. No producer correction.
This is a structured ROOT integration, not a verbatim copy of the raw review.
Promotion is owned by the RATIONAL-AREA-INVARIANT-1 entry in AUDIT.md.

## 1. Frozen evidence and terminal collection

The [producer](rational-area-invariant-swarmHQ-root-20260919T120200Z.md)
was reviewed at public commit e19163aba8a1b84d4f84813b5bed7cb39cbc277c.
Its pre-authoring basis2730e5d5 differs normally from this publication commit.
Its whole-file SHA256 is
95d8795106dda6cb0e6dbcd670d168b8791f0bcc16d1f5784bc29373de17f537.

Four charged snapshots were read whole, with matching pre/post pins:

- Producer as above.
- [Prior positive-genus producer](positive-genus-invariant-swarmHQ-root-20260919T035200Z.md):
  7f0a3fe3422271ca42286cf1185eef984c945cb32eea23c3bf0924c68b32a1f9.
- COORDINATION.md: 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e.
- FALLACY-v2.md: e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5.

The reviewer completed at12:16:28 UTC. The external lane terminated at
12:16:44 with adapter/parent exit0. ROOT independently checked terminal
process/cgroup absence, collected the version2 receipt FIRST, then read
the entire233-line raw report and25-line final-only log. All charged input,
prompt, launcher and adapter pins stayed unchanged. Raw evidence hashes:

- Review: 1b397f026e84ec7bdc7f07fafad23c9b28a49b582fc2c60a385b4bd07e989971.
- Final-only log: f39ef37cd9498ff1fddb39921ae59191fd86970eb87af4fca755e2ea94530ea5.
- Terminal receipt: 86af022d2999df47e38d2ba166ca1360f29756c4c8d88683d541bffd2d24519f.

All three raw artifacts were retained read-only with identical pre/post
hashes. Producer bytes and its historical UNPROMOTED header are unchanged.
No live report/log/receipt was inspected. No source, CAS or scientific
computation was used. The reviewer reports no unauthorized writes or reads;
the final-only log is not a complete execution/write trace, so that report
is not upgraded to a full delivery audit. Requested model and self-reported
hosted identity are distinguished; no independent provider attestation.

## 2. Independent proof reconstruction

### Compact-curve poles — CONFIRMED

For a nonconstant self-map f of degree d on a smooth projective curve in
characteristic zero, local uniformizers give

    ord_p(f*eta) = e_p*(ord_{f(p)} eta+1)-1.

Hence f*eta=eta makes the finite pole set satisfy f^(-1)(S)=S. If nonempty,
surjectivity makes f|S a permutation; every pole has a single full geometric
preimage, with index d. Around a pole cycle of length m, the iterate has
index d^m. Order equality forces a simple pole if d>1. Its nonzero residue
would then equal d^m times itself, impossible in characteristic zero.
The review checks full preimages, index multiplication, simple-pole order
and the nonzero residue separately; no puncture or genus assumption is hidden.

### Pole-free case — CONFIRMED

The curve, map, regular differential and invariant identity descend using
finitely many coefficients to a field finitely generated OVER Q. Smoothness,
geometric integrality, properness, map degree and the nonzero regular
differential persist. Such a field embeds into C; there is no requirement
to embed the entire original field while fixing all complex constants.
On the resulting compact connected Riemann surface, the positive finite
integral I of i*eta wedge conjugate(eta) obeys I=d*I. The degree formula
follows from the oriented finite covering away from the finite branch set.
Thus d=1. This argument covers every pole-free genus.

### Relative algebraic closure and degree — CONFIRMED

For L=C(x,y), let K be the algebraic closure of C(r) inside L. With u
transcendental over C(r), algebraic/purely transcendental disjointness gives

    [K:C(r)] = [K(u):C(r)(u)] <= [L:C(r)(u)] < infinity.

H* preserves K and is an injective C(r)-linear endomorphism, hence an
automorphism of finite order e. Its e-th iterate tau fixes K. Repeated
isomorphic field extensions give [L:tau(L)]=N^e. Algebraic closedness
of K in L and characteristic zero make L/K regular, so its smooth
projective K-curve is geometrically integral. Scalar extension retains
the degree of the finite curve map. No affine base-point assumption.

### Relative differential class — CONFIRMED

Finite separability gives Omega_(K/C)=K dr, and the exact differential
sequence gives Omega_(L/K)=Omega_(L/C)/(L dr). Since dr!=0, wedge by dr
identifies this quotient with Omega^2_(L/C). The class eta defined by
dr wedge eta=dx wedge dy exists uniquely and is nonzero. Tau fixes dr
and the area form, so fixes the CLASS eta. No invariant absolute
representative is claimed. After geometric scalar extension the class
is an invariant rational differential on the compact generic curve.
The compact-curve lemma gives N^e=1, hence N=1.

### Determinant scope — CONFIRMED with reviewer wording narrowed below

The fixed rational map (x^2,y/x) has Jacobian2, degree2 and invariant xy.
Its relative logarithmic form is multiplied by2, not fixed. Normalizing
the second output gives Jacobian1 but sends xy to xy/2, destroying this
invariant. The map is not polynomial and supplies no JC2 counterexample.

### Comparison and conjugacy — CONFIRMED with reviewer wording narrowed below

The older positive-genus theorem assumes a polynomial map and a
geometrically integral positive-genus pencil, but no determinant condition.
The present theorem assumes exact area preservation, while allowing a
rational map, every genus and a disconnected original pencil. Their
hypotheses are different. A matched birational conjugacy transports a
fixed invariant function, not automatically the STANDARD area form.
Independent changes at the two ends do not automatically preserve a
self-map invariant. The inherited birational Keller endpoint is consumed
only for the polynomial corollary, not re-established by this review.

## 3. Binding ROOT corrections to additional reviewer language

The reviewer found no producer gap. ROOT accepts all six proof verdicts,
but does NOT adopt the following overstatements in the review commentary:

1. The review calls the boundary "exactly J identically 1." The promoted
   theorem assumes exact preservation; the J=2 example only prevents
   replacing it by an ARBITRARY nonzero constant. This is not a necessity
   theorem excluding every other constant determinant or every other proof.
2. With original Jacobian c constant and tau=(H*)^e, the scalar on the
   relative form is c^e, not c: the review's shorthand tau*eta=J*eta must
   use the Jacobian of the ITERATE. All charged proof steps have c=1,
   so this notation correction changes no theorem or verdict.
3. The review says standard-area invariance is inherited under conjugacy
   "only when psi itself preserves" the standard form. Exact preservation
   by psi is sufficient, not necessary: even a constant nonzero multiplier
   cancels between psi and psi^(-1). The binding statement is solely that
   GENERAL birational conjugacy does not automatically preserve the
   displayed standard form. Likewise read the independent-endpoint warning
   as "not automatically," not an impossibility for every pair of changes.

These corrections narrow reviewer additions. The producer already uses
the scoped statements, and its sealed bytes require no repair. No broader
transported-form theorem or nontrivial base-map semiconjugacy is promoted.

## 4. Accepted scope and stopping point

Accepted: a dominant rational plane self-map preserving dx wedge dy EXACTLY
and a nonconstant rational function has generic degree one. If polynomial,
the inherited birational Keller theorem gives automorphy. Original pencil
geometric connectedness and positive genus are unnecessary.

Not supplied: an invariant for arbitrary Keller maps, an arbitrary constant-
Jacobian rational version, unrelated source/target repairs, a complete
counterexample, or JC2. A map moving the pencil's base parameter does not
meet the fixed-invariant hypothesis. No automatic family or descendant.
No literature novelty or formal-proof claim. The manual theorem may be
used only with its exact hypotheses and named classical curve/differential
and complex-integration facts.

## OPEN(S) RAISED

None. No new bounded experiment or provisional descendant is raised.

## COLLISIONS

status: EMPTY

- NONE — no explicitly raised `OPEN[...]` entries.

ROOT integration author completion: 2026-09-19 12:20:57 UTC, after whole
body readback and collision check. Original producer/reviewer bytes unchanged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8963`.
- Body SHA-256:
  `6a5646149774b69670c7a11907c5da86ac9a7fc5a517b5500b301b3519606838`.
- Frozen basis: `e19163aba8a1b84d4f84813b5bed7cb39cbc277c`.
