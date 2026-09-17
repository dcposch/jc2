# Cubic polynomial-base unit counterexample, with a no-Jacobian-mate certificate

Claim: CUBIC-BASE-UNIT-COUNTEREXAMPLE-1.
Producer: swarmHQ ROOT (Astra); same-model manual co-check by Astra/Maxwell.
Lifecycle: PROVISIONAL. Evidence: MANUAL, explicit identities and curve argument.
Different-model hostile review is required before promotion.
Frozen campaign basis: 3919319a87322590501ac0703e74273046f9fb8a.
Proof completed September 17, 2026; filename time is an identifier, not a
claim that the report was frozen at that instant.

## Exact statement and excluded readings

There is a polynomial P in C[x,y] with no critical point, with every closed
fiber P-c irreducible and with geometrically integral generic fiber, such
that a finite polynomial base change t=h(s) gives a global non-base unit
on X_h={P(x,y)=h(s)}. Equivalently, the proposed constant-resultant-norm
rigidity for this literal plane-based algebra is false.

This refutes the auxiliary assertion that nonsingularity and irreducibility
of EVERY fiber alone force scalar geometric-generic units. It does NOT
refute JC2: the very same P admits no rational Q with nonzero constant
Jacobian J(P,Q). The Keller hypothesis is absent and cannot be inferred.
There is no claim of novelty, identification with a named example, general
classification, or proof of unit behavior for Keller components.

## Explicit construction and norm

Work over C, in characteristic zero. Define

    k = 1+xy,
    a = 1+x^2 k,
    h(s) = s^3-3s,
    P = -3y-3x^2 k y-x^3 k^3.

The actual total degree of P is 9 (top term -x^6 y^3); its degree in y is 3.
These degrees describe a method counterexample, not a JC2 pair search.
Direct expansion gives the polynomial identity

    a^3-3ax^2+Px^3 = 1.                         (1)

For an explicit check, a^3-3ax^2 equals

    1+3x^2(k-1)+3x^4 k(k-1)+x^6 k^3,

and k-1=xy cancels exactly with Px^3.
Set T=C[x,y,s]/(s^3-3s-P). It is free of rank 3 over C[x,y], with ordered
basis (1,s,s^2). In T put

    w = a+xs,
    b = a^2-axs+x^2 s^2-3x^2.

Multiplication, using s^3-3s=P, gives

    wb = a^3-3ax^2+x^3(s^3-3s)=1.

Consequently w is a global unit. For the convention Res(f,g) with the
monic cubic f first, its determinant norm is

    Res_s(s^3-3s-P,a+xs)=a^3-3ax^2+Px^3=1.

No numerical roots, finite-field calculation, degree truncation or CAS
certificate are being substituted for this identity.

## The plane source really satisfies the hypotheses

On x != 0, introduce the birational coordinate change

    z=1/x,  v=a/x=x+x^2 y+1/x.

It is an isomorphism C[x,x^-1,y]=C[z,z^-1,v], with inverse

    x=1/z,  y=z^2 v-z-z^3.

Its Jacobian det(d(z,v)/d(x,y)) is -1. Dividing (1) by x^3 yields

    P=z^3-v^3+3v=z^3-h(v).                       (2)

For x != 0, z != 0, and the partial derivative of (2) with respect to z
is 3z^2 != 0. At x=0, P(0,y)=-3y and P_y(0,y)=-3. Thus P has no critical
point anywhere on the WHOLE affine plane, including the missing chart.

For each c in C the localized fiber has equation

    z^3=v^3-3v+c,  z != 0.                       (3)

The right side is not a cube in C(v). Indeed a rational cube root is
integral over C[v], hence polynomial since C[v] is integrally closed.
It would have degree one, av+b. Its leading coefficient has a^3=1;
the v^2 coefficient forces b=0, which makes the coefficient of v zero,
contradicting -3. A degree-three polynomial z^3-g over a field is reducible
only if it has a root. Thus (3) is irreducible in C(v)[z], then in C[v,z]
by Gauss's lemma, and remains irreducible after inverting z.

This also proves that P-c is irreducible before inverting x. Any extra
factor would become a unit in C[x,x^-1,y], hence would be a scalar times
a power of x; but x does not divide P-c because (P-c)(0,y)=-3y-c.
The localized irreducible factor is not itself a unit. All multiplicity
possibilities are excluded by the same factorization argument. In
particular the fibers are reduced and irreducible for EVERY c, including
c=2 and c=-2. The affine cubic in (3) can have its singular point at z=0
for these parameters; that point is outside this localized chart, so
there is no conflict with nonsingularity of P on the whole plane.

The noncube proof works verbatim over any characteristic-zero extension
field of C, with c any element of that field. Taking c=t over the algebraic
closure of C(t) proves geometric generic integrality. Taking c=h(s) over
C(s) gives generic integrality of X_h over the s-line. Since its equation
is monic in s, or equivalently by its localization and the same x-factor
test, the whole surface X_h is integral. It is smooth: at every point at
least one of P_x,P_y is nonzero, so the gradient of h(s)-P is nonzero.

## The unit is not from the base

There is a section of X_h over the s-line:

    s |-> (x=0, y=-h(s)/3, s).

The restriction of w to this section is 1. If w belonged to C(s) in the
function field of X_h, generic evaluation on the section would therefore
force w=1. But in the unique rank-three normal form over C[x,y], w-1 has
s-coefficient x != 0, and cannot vanish in T. Thus w is non-base.

The same section and normal-form argument work after extending the generic
base to an algebraic closure. Since t=h(s) is a finite extension of C(t),
w supplies a nonconstant unit on the geometric generic fiber of P.
It is not merely a unit on an unrelated abstract curve or a formal cover.

## This particular P has no rational constant-Jacobian mate

This is an additional scope certificate, not a claimed JC2 obstruction
applicable to arbitrary P. Put K=C(t). The smooth projective model of
the generic fiber is the plane cubic

    C_t: Z^3=V^3-3 V W^2+t W^3.

In its affine chart W=1 use coordinates z,v as in (2). An affine singular
point would require z=0, v=1 or -1, and t=2 or -2, impossible for the
transcendental element t in K. At W=0, Z^3=V^3 and V,Z are nonzero, so
the projective gradient is nonzero. Hence this is a smooth projective
geometrically integral curve. Define the nonzero differential

    eta = dv/(3z^2).

It is holomorphic everywhere. Away from z=0 this is immediate. At z=0,
the fiber equation gives 3z^2 dz=(3v^2-3)dv, hence

    eta=dz/(3v^2-3),

whose denominator is nonzero over the generic parameter. At infinity set
u=1/v, Z0=z/v. Then Z0^3=1-3u^2+t u^3 and

    eta=-du/(3 Z0^2),

regular and nonzero at each point u=0, Z0^3=1.

Suppose Q in C(x,y) had J_xy(P,Q)=c != 0 constant. The displayed chart
Jacobian gives J_zv(P,Q)=-c. On the generic fiber,

    d_K Q = [J_zv(P,Q)/(3z^2)] dv = -c eta.     (4)

For completeness, this follows from dz=(3v^2-3)dv/(3z^2) and
P_z=3z^2, P_v=-3v^2+3. A rational function on a smooth projective
characteristic-zero curve cannot have a pole while its differential is
holomorphic: a pole of order m differentiates to a pole of order m+1,
with nonzero leading coefficient. Thus (4) forces Q to have no poles,
and so to be constant on the geometric projective curve. Its relative
differential is zero, contradicting c eta != 0. No rational, hence no
polynomial, nonzero-constant-Jacobian mate exists for this P.

## Dependencies, controls and campaign implications

Only elementary polynomial factorization, the Jacobian chain rule,
smooth projective curve completion, and the elementary pole/differential
fact enter the proof. There is no unread paper used as a theorem import.
The exact identities, x=0 chart, c=+/-2 parameters, generic-field change,
non-base section and no-mate differential are the meaningful scope checks.
The P=x control would give T=C[y,s] and scalar global units; the present
P cannot be treated as a coordinate merely because it is nonsingular.

The reviewed [horizontal-unit polynomial-base reduction](horizontal-unit-polynomial-base-swarmHQ-root-20260917T211700Z.md)
and [geometric-unit globalization](geometric-unit-globalization-swarmHQ-root-20260916T232700Z.md)
remain intact. They reduce or globalize an existing geometric unit and
never asserted its vanishing. This example rules out adding scalar
global units on all such polynomial-base surfaces as an automatic final
step under nonsingularity and all-fiber irreducibility alone.

The [D4 fixed-cover counterexample](d4-rational-base-counterexample-swarmHQ-root-20260917T191600Z.md)
had a different object: an abstract prescribed-cover criterion. Here
the entire polynomial plane source and its units are given explicitly.
Earlier cyclic-prime/degree-four source-scope gaps are not resolved by
assuming their hypotheses. Earlier Briancon/genus-drop controls in the
journal were consulted; no exact identity with a named published example
was established, and no novelty claim is made. The stopped 2015
factorially-closed-rings paper remains unread; no contradiction to its
unread hypotheses is asserted.

The admitted general norm-vanishing test therefore stops with a qualifying
counterexample. Any future Keller-specific route must use additional
Keller structure; neither a family search nor a genus/degree ladder follows
from this report. No new exit-price assertion and no new OPEN are raised.

## Evidence and custody

ROOT reconstructed all calculations manually. Astra/Maxwell independently
checked the same claims and returned the final co-check at 21:55:10 UTC;
the native task was independently observed COMPLETED at collection. This
same-model check is not the required different-model FIRST review.
No CAS, exact-Python scientific execution, worker, random seed, primes,
numerical experiment or external theorem-body retrieval was used.
Artifact sealing and collision checking are integrity operations only.

Charged context hashes, SHA-256:

    horizontal producer a9a9c3818c065b8cecbb844ca0a847d9500a753abc1b64496cdd5cb90a0ba3a5
    globalization producer 87dc47e2ff7ae6caab9e5b0d434b1cdc596b5b958ce83ccbf6ad60aded89cf21
    D4 producer 65906bbadc41f8107df0a2d76f7c8966b77b07e52289c689a2a5867f86d4a29a
    APPROACHES.md 905313fb08c6e94410b8c4a9a4537bf69ac3ff63284a14c9a34761263fc1505f
    FALLACY-v2.md e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5
    COORDINATION.md 9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e

## COLLISIONS

Actual command, run from the research checkout:

    python3 ops/open_collision.py xmodel/.cubic-base-unit-counterexample-swarmHQ-root-20260917T215500Z.md.partial-54328a4dd71b6cb4f2ad3dac2b08ed08 --root .

Terminal exit 0; output:

    ## COLLISIONS

    status: EMPTY

    - NONE — the report contains no explicitly raised `OPEN[...]` entries.

This is the checker outcome, not an exhaustive novelty assessment. All
six listed context pins were rechecked unchanged after authoring at
22:00 UTC. Scientific authoring is complete.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10680`.
- Body SHA-256:
  `50d6fbd180731bea263ac1945c1c69712c41c3a708fba25fd9137ab9f69703a3`.
- Frozen basis: `3919319a87322590501ac0703e74273046f9fb8a`.
