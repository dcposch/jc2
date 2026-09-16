# A fixed nonsingular genus-one function on the pseudo-plane has no regular mate

Producer: swarmHQ (gpt-6-astra, ROOT); fixed submersion/genus check by native
gpt-6-astra affine_target_planes, terminal 2026-09-16 06:30:42 UTC.
Date: 2026-09-16 UTC.
Basis: 863c614a344b39567826a5aac963fd447dcc6237.
Evidence tier: MANUAL.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED; same-model corroboration is not FIRST.

## Statement and scope

Over C let S=Spec C[A,U,Z]/(U^2-A-A^2 Z), with the nowhere-zero form
Omega=dA wedge dU/(2A^2), extended across A=0. Put

    eta(A,U,Z)=(4U^2,2U(1+2AZ),Z), h0=A+U,
    B=1+2AZ, w=4UB, h=h0 composed with eta^2=w^2+w(2B^2-1).

Claims: (A) h is nonsingular on all S; (B) its geometrically integral
generic fiber has smooth projective genus one; (C) there is no g in O(S)
with dh wedge dg=c0 Omega for any nonzero constant c0.
Thus nonsingularity on this literal S does not force rational generic fibers,
but this fixed h supplies no scalar-bracket pair. No arbitrary-S pair
exclusion, plane Keller pair, JC2 proof or counterexample follows.

## Dependencies and prior work

The accepted explicit eta and eta*Omega=2Omega are in
[the invariantization producer](danielewski-invariantization-root-20260911.md),
SHA256 28fb540a4bb834ad40d1aa0349b8a2458cf7665951484e4896638f18275e3189,
with [Fable review](danielewski-invariantization-gate-fable5-20260911.md).
These are existing foundations, not newly asserted selfmap theorems.
The [historical construction map](../history/APPROACHES-through-20260915.md)
section 7 records h0 as a submersion and the rational-mate polar-fiber
correction principle. Claim C is a fixed application of that known mechanism,
not a new global mechanism. The earlier plane genus controls do not imply
claim A on this surface. A targeted history search found no exact fixed
two-iterate calculation; this is not an exhaustive novelty claim.
Standard characteristic-zero differentials and Riemann--Hurwitz are used below.
No external unread theorem is imported. FALLACY-v2 checked; no exit-price claim.

## Argument

### A. Whole-source submersion

S is smooth: for G=U^2-A-A^2 Z the simultaneous vanishing of its partials
would imply A=U=0 and G_A=-1, a contradiction. On A!=0, (A,U) are
coordinates and dh0=dA+dU is nonzero. At A=0 one has U=0; (U,Z)
are local coordinates and dA=0 in the cotangent space, so dh0=dU!=0.
The accepted eta is etale everywhere, hence h=h0 eta^2 is a submersion
on ALL S. The relation gives B^2=1+4U^2 Z and A(B+1)=2U^2.
Direct substitution gives

    h=16U^2 B^2+4UB(1+8U^2 Z)=w^2+w(2B^2-1).

### B. Actual generic-fiber field, not a rational quotient

The inverse rational substitutions are

    U=w/(4B), A=2U^2/(B+1), Z=(B^2-1)/(4U^2).

Thus C(S)=C(w,B). With K=C(c), c transcendental, the entire generic
fiber satisfies c=w(w+2B^2-1). Hence w, U and B are units there, and
A(B+1)=2U^2 makes A and B+1 units too. No generic component lies outside
the chart. Explicitly its ring is

    K[w^{+/-1},B^{+/-1},(B+1)^(-1)]/(2wB^2-c-w+w^2).

Over the algebraic closure of K, (c+w-w^2)/(2w) has simple zeros at
the distinct nonzero roots of w^2-w-c and simple poles at 0 and infinity.
It is not a square, so the displayed ring is geometrically integral.
Its quadratic field is branched at four points; Riemann--Hurwitz gives
genus one. Equivalently y=2wB gives y^2=-2w^3+2w^2+2cw, a smooth
generic projective cubic. The localized affine fiber is not identified
with the entire projective cubic. Replacing B by B^2 takes a quotient
and incorrectly discards the double cover.

### C. All regular mates of this fixed function are excluded

On the birational chart a direct differentiation gives

    Omega=dU wedge dB/(4U^2)=B dw wedge dB/w^2.
    q=1/(8w^2), dh wedge dq=Omega.

Indeed dh=(2w+2B^2-1)dw+4wB dB and dq=-dw/(4w^3).
If dh wedge dg=c0 Omega, normalize by c0 and put k=g/c0-q.
The relative differential dk over C(h) vanishes. In characteristic zero
the kernel consists of the relative algebraic constants; geometric
integrality from B makes C(h) algebraically closed in C(S). Therefore

    g/c0=q+r(h), r in C(h).

Consider two prime divisors in h=0. First D0={B=0} is the nonempty smooth
curve A=2U^2, Z=-1/(4U^2), U!=0. Here B is a local parameter, w=4UB
has order one, and w+2B^2-1 is a unit. Hence ord_D0(h)=1 and q has
a pole of order two.

For the second, take the component D1 of h=0 through
P=(A,U,Z)=(1/16,-1/4,0). At P, B=1 and w=-1, so w is a unit and
w+2B^2-1=0. Since h is a submersion, this fiber is reduced and
ord_D1(h)=1. The generic point of D1 has w!=0, so q is regular there.
D1 is distinct from D0.

A pole of r at 0 forces a pole on D1, which regular q cannot cancel.
Thus r must be regular at 0. It then cannot cancel q's pole on D0.
This contradiction excludes every regular g, with no degree bound.

## Replay and negative controls

Desk-only algebra and divisor valuations; no CAS, executable mathematics,
seed or prime. The native same-model check covered A/B independently, not C.
Meaningful comparison: after only ONE iterate h1=4U^2+2UB. On h1=c,
U!=0 and B=c/(2U)-2U, so its generic field is K(U), rational. The
two-iterate field must not be conflated with this one-iterate case or
with a double cover of another surface. For claim C the pole comparison
uses actual divisors of S, including explicit points, not missing chart
divisors or merely formal places. Rational q exists; regular g does not.
Administrative lifecycle and collision checks provide integrity, not proof.

## Limitations and next test

The rational-fiber shortcut fails; the resulting h is not a construction
seed for a regular scalar pair. Independent different-model hostile review
of A--C is required before promotion. No further iterates, parameter family,
degree scan, arbitrary-S exclusion, or descendant is authorized by this note.
General scalar-pair existence on S and actual plane JC2 remain unresolved.

## OPENS RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6046`.
- Body SHA-256:
  `64965504363833ac6197605bd817c4091a0501d58dc18c4ae68bd1a562827b35`.
- Frozen basis: `863c614a344b39567826a5aac963fd447dcc6237`.
