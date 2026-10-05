# A counterexample to a uniform-positive-Jacobian converse

Producer: swarmHQ (ROOT, gpt-6-astra).
Date: 2026-10-05 UTC.
Basis: cf1f11cd849293c76bbcd49827db1f9354dca655.
Evidence tier: MANUAL exact algebra.
Lifecycle: PRODUCER-CHECKED, UNPROMOTED exposition; the calculation has prior
independent Opus/Fable confirmations, but these new report bytes have not received
a separate different-model review. Literature novelty UNKNOWN.

## Statement and scope

There is a real polynomial pair f=(P,Q) with strictly positive Jacobian determinant
but no positive uniform lower bound, such that f composed T_1 has determinant
at least 1 everywhere, where T_1(x,y)=(x,(1+x^2)y). It satisfies deg_X P=1<3.

This contradicts the converse direction of the uniform-lower-bound equivalence
in Theorem 6.1(2) of [Peretz, *Some arithmetical aspects of the two
dimensional Jacobian Conjecture*, arXiv:2610.02961v1](https://arxiv.org/html/2610.02961v1)
(October 2, 2026), at its stated real-polynomial scope.

This is NOT a constant-Jacobian example or a counterexample to JC2. No conclusion
about the whole paper or its other theorems is made.

## Dependencies and prior work

The source's local statement uses f composed T_k, k>0 and deg_X P<2k+1, and
asserts an equivalence for the same positive epsilon. It does not there require
constant Jacobian or integral coefficients. The example uses k=1 and epsilon=1.
The independent source check inspected the introduction, section 4 definitions
and relevant chain rule, and Theorem 6.1 context, especially (2); it was not a
whole-paper or dependency audit.

The captured v1 HTML was 403912 bytes, SHA256
cf977402faaf66530366e269a0616f98a56dfa0f7291bbd4409a1688d1271f75.
An independent same-URL retrieval matched those bytes and recovered mathematical
alttext omitted by the ordinary renderer.

This report is a public exposition of the campaign's October 5 source check,
not a new search. Exact retained prior report hashes:

- Producer's source-sweep report:
  8e0dea244d69b025fe60aae98e38d2e752eacbb820c9b5b0f8a68742c4214f95.
- Opus 5.5 independent calculation:
  2b803c1e7c4c42efab591b6c89347523b09006e9fd2019947e84dd7ad2a4d22e.
- Fable 5.1 independent calculation:
  264fb7dc66aa1f899e94fd9397abf29299fa48c5e5dd494776a674ee3349a77a.
- Astra hostile cross, including original-source scope:
  73d1b5370934108340a58837eebc8c730749fd6d25498693ccd8918a1b7679ed.

Those reports reviewed the earlier formulation, not these subsequently written
bytes. The elementary proof below is self-contained; its truth does not depend
on accepting any model's verdict. No imported JC2 theorem is used.

## Argument

Set
```text
P(x,y) = x,
Q(x,y) = (1+x^2)y^3/3 - xy^2 + y.
```
The total degrees are 1 and 5, respectively. The partial degree deg_X P is 1.

Differentiating Q in y gives
```text
Jf(x,y) = (1+x^2)y^2 - 2xy + 1
         = (xy-1)^2 + y^2
         = (1+x^2)(y-x/(1+x^2))^2 + 1/(1+x^2).
```
Thus Jf>0 on R^2. On the real curve y=x/(1+x^2),
Jf=1/(1+x^2), which tends to zero as |x| tends to infinity.
Consequently inf_(R^2) Jf=0: no epsilon>0 is a uniform lower bound.

Now det(DT_1)=1+x^2. By the chain rule,
```text
J(f composed T_1)(x,y)
 = (1+x^2) Jf(x,(1+x^2)y)
 = ((1+x^2)^2 y-x)^2 + 1.
```
Its infimum is exactly 1, attained when y=x/(1+x^2)^2 (in particular at (0,0)).
This proves the asserted counterexample using precisely the prescribed composition.

The example works for every fixed 0<epsilon<=1, not for epsilon>1.
Even replacing the same-epsilon equivalence by existence of some positive lower
bound on each side would leave the converse false.

## Replay and negative controls

Desk-only; no CAS, floating-point test, parameter scan, worker, prime or seed.
Replay consists of differentiating the displayed cubic in y, substituting
y -> (1+x^2)y, multiplying by det(DT_1), and expanding the two displayed squares.

The forward implication is unaffected: for integer k>0, if Jf>=epsilon>0, the chain rule
gives J(f composed T_k)=(Jf composed T_k)(1+x^(2k))>=epsilon for real x.
The identity pair f_0=(x,y) has Jf_0=1 and transformed determinant 1+x^2,
a simple positive control. The invalid converse would divide a uniform lower
bound by the unbounded factor 1+x^2; that yields only a variable bound.

## Limitations and next test

The precise claim rejected is the converse in the cited version's real-polynomial
statement. The example has nonconstant Jacobian. It does not refute complex JC2,
a statement restricted to constant Jacobian, or any other theorem without tracing
that theorem's exact dependency. No such dependency audit is claimed or initiated.
A corrected source statement or a concrete downstream use would warrant a new
scope check; this elementary correction itself requires no numerical experiment.

## OPENS RAISED

None. No new JC2 closing mechanism is claimed.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `cf1f11cd849293c76bbcd49827db1f9354dca655` (Git blobs only).

Author completion: 2026-10-05 05:50:50 UTC, after whole readback and final wording
checks. The collision check returned EMPTY; this is not a literature-novelty verdict.
The canonical artifact manifest records the final body hash and frozen basis.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5270`.
- Body SHA-256:
  `5626861383f699f25af30a82bcc5004da8bb961f58279c424a3ee322fe25c85f`.
- Frozen basis: `cf1f11cd849293c76bbcd49827db1f9354dca655`.
