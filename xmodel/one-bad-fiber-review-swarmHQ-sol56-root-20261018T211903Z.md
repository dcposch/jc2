# One-bad-fiber pullback: independent FIRST and binding integration

Status: FIRST CONFIRMED at the exact scope below; JC2 remains open.
Producer: swarmHQ ROOT. Independent reviewer: retained Sol5.6-assigned native
seat `/root/affine_radial_first_sol56_2157`; hosted model identity unverified.
Reviewer completion: 2026-10-18 21:19:03 UTC; ROOT receipt: 21:21:31 UTC.
This report transcribes/synthesizes the terminal native review; ROOT is its
artifact writer, not a second independent reviewer. No machine proof is claimed.
Basis: public `246f5aceb778112f95e248864b3464fcd0bce3cd`.

## Frozen claim and custody

[Producer](one-bad-fiber-pullback-swarmHQ-root-20261018T211327Z.md),
95 lines /5955 bytes, mode0444,
SHA256 `b667e52762928375b7ae18b0ccb996527b938220ea48fb3c9cfc25c54063d827`.
Manifest SHA256 `2d1d82dcd32f2c2928bdad73094f203c01edae81490236f271c7ba24e33dff55`.
The original producer remains sealed and historically UNPROMOTED; this separate
review records acceptance, without modifying that artifact or its chronology.

Let F=(P,Q):A2_C -> A2_C be Keller and identify K=C(u,v) in L=C(x,y) by F*.
Let f=a/b be nonconstant with coprime a,b in C[u,v], and C(f) algebraically
closed in K. Suppose all but at most one of the affine divisors
div(a-lambda b), lambda in C, and div(b) are reduced; an empty divisor is reduced.
Then C(f) is algebraically closed in L. Affine basepoints are permitted.
Neither rational generic fiber nor a basepoint-free pencil is assumed.

## Independent reconstruction and hostile checks

1. A finite intermediate E/C(f) in L is the function field of a curve dominated
   rationally by A2. Restrict to a suitable line and extend to P1; Riemann-Hurwitz
   gives genus zero. Over C, E=C(s), so f(F)=R(s), n=deg R.
2. Pullbacks of a,b have no common prime: such a source curve would map to the
   finite target base locus, impossible for a quasi-finite Keller map. Etaleness
   preserves reduced affine fiber divisors, including the pole fiber.
3. If alpha is a ramification point of R over a good value, a component of the
   affine s=alpha fiber would acquire multiplicity
   e_alpha(R)*ord_C(s-alpha)>1 in the good composite fiber. It must therefore be
   empty. The valuation formulation includes alpha=infinity in a local parameter.
4. A rational function g/h on A2 with coprime numerator and denominator omits at
   most one P1 value at divisor level. Two empty values make two independent
   linear combinations of g,h nonzero constants, contradicting nonconstancy.
   Thus R has at most one ramification POINT outside the unique possible bad
   value b0. This is stronger than merely one critical VALUE.
5. For m=#R^-1(b0), ramification over b0 totals n-m. Riemann-Hurwitz requires
   n+m-2 outside it. Support at at most one point bounds this by n-1. If n>1,
   m=1 and equality follows: exactly two totally ramified points over distinct
   values. Therefore R=M composed with z^n composed with N for Mobius maps M,N.
6. Every target prime divisor D is dominated by a source prime: d(P,Q) is
   nonconstant, and quasi-finiteness prevents contracting a prime factor curve.
   Its generic ramification index is one. Consequently, if h(F) is an nth power,
   all affine prime valuations of h are divisible by n. The UFD C[u,v] and
   algebraic closedness of C give h=t^n in K.
7. Apply this to h=M^-1(f). For n>1 the resulting proper finite C(t)/C(f)
   inside K contradicts target primitivity. Hence n=1 for every E as above.

The reviewer independently confirmed each step using standard Keller/curve
facts; no external-source audit or formal verification is asserted. In particular,
this does NOT reuse the Sep25 whole-fiber-gcd inference: reducedness holds on
EVERY component of a good fiber, so the actual-component multiplicity identity
is sufficient. No properness, target-genus or nonproper-set theorem is smuggled in.

## Explicit client, negative control, and limits

For f=(v^2-u^3)/u^2, all finite fiber numerators are squarefree and the only
nonreduced fiber is the pole divisor 2{u=0}. With z=v/u one has
u=z^2-f, v=z(z^2-f), hence K=C(f,z), proving target primitivity. The pencil has
the genuine affine basepoint (0,0), outside the previous basepoint-free theorem.

For any rational R(s) of degree>1, the dominant donor
H_R(s,t)=(t^2-R(s), t(t^2-R(s))) satisfies f composed with H_R=R(s).
A dominant finite rational source substitution yielding a polynomial Keller pair
would embed the forbidden proper finite C(s)/C(R(s)) in its source field.
Thus no such source repair exists, at these FIXED target functions.
The reviewer also checked f=u^n, F=id as a negative control: dropping target
primitivity makes the conclusion false even with only one nonreduced fiber.

This does not exclude arbitrary birational target changes, all pencils, or all
donors; it supplies no suitable-pencil existence theorem for a general Keller map.
It does not prove finite normalization equals C[x,y], surjectivity, or JC2.
Novelty relative to all literature is UNKNOWN. General reduced-fiber existence
or selection is not silently adopted as a corollary or an automatic next task.

## Review read record

The terminal reviewer reported whole producer and manifest reads, custody VERIFIED,
fresh Sep25 journal373-436, and matching own prior basepoint-free proof1-96.
New frozen STATE1-339 and changed APPROACHES1-918 were read whole; other governing
whole reads were reused only at the reviewer's own matching pins. Pre/postpins
matched. The reviewer reported no writes, queries, network, CAS, descendants,
protected-tree access or deviations. ROOT received the terminal message, not a
live report file. This record is the reviewer's attestation, not a new ROOT reread.

## OPEN(S) RAISED

None. Existing JC2 gaps remain open; this scoped result does not rename them.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `246f5aceb778112f95e248864b3464fcd0bce3cd` (Git blobs only).

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6002`.
- Body SHA-256:
  `2715b4cbbf09045d884aab5aad33470fb1db382e856c022d8ca5eb29cf195d5d`.
- Frozen basis: `246f5aceb778112f95e248864b3464fcd0bce3cd`.
