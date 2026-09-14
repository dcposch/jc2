# Removing a rational mate's poles on irreducible fibers

Producer: swarmHQ ROOT / Astra. Date: 2026-09-14.
Basis: a8152e3232505eadcf0acbf03aa88333b04b3eed.
Evidence: MANUAL, self-contained algebra. Lifecycle: PRODUCER-CHECKED,
UNPROMOTED; same-model co-research is not different-model FIRST.

## Statement and construction interface

Let R=C[x,y], let p in R have no critical point, and let q in Frac(R)
satisfy J(p,q)=1. Suppose that every fiber p=a supporting a pole of this
GIVEN q is irreducible. Then

    q=q0+r(p),  q0 in R,  r in C(t),  J(p,q0)=1.

Only finitely many fibers are tested. No irreducibility assumption is
needed for fibers supporting no pole. In particular, the conclusion holds
if every fiber of p is irreducible. It does NOT follow from submersivity
alone. No rational mate for a new noncoordinate p is supplied here.

This gives a candidate-specific way to discharge polynomiality after an
exact rational mate has been found: identify its polar fibers, check their
irreducibility, and perform the finite pole removal below. It gives neither
a rational-integration algorithm nor a search bound, uniform family,
measured acceleration, automorphy theorem, or JC2 resolution. The algebra
is elementary and may be classical; no literature novelty is asserted.

## Proof

Put D=J(p,-), a derivation of R and its fraction field. Let h be an
irreducible polar factor of q and m=-v_h(q)>0. In the DVR R_(h), write
q=h^(-m)u with u a unit. D preserves R_(h). If h does not divide Dh,
then

    Dq=h^(-m)Du-m h^(-m-1)u Dh

has valuation -m-1: the second term has that valuation and the first has
valuation at least -m. This contradicts Dq=1. Thus h divides Dh.

D therefore induces a derivation on the domain R/(h). It is nonzero:
its values on x,y are -p_y,p_x, and these cannot both vanish modulo h
because p has no critical point. A nonzero C-derivation of a curve's
function field has constant field C. Indeed, any nonconstant element
killed by it makes the curve field a finite algebraic extension of C(s);
characteristic-zero separability would then make the derivation zero.
Since Dp=0, p modulo h is a scalar a. Consequently h divides p-a.

By the hypothesis on this polar fiber, p-a is irreducible. It is also
reduced, since p is a submersion. Hence h is an associate of p-a. This
holds for every polar factor. Unique factorization now supplies a
polynomial S(t), all of whose roots are polar values, such that

    F=S(p)q in R,       DF=S(p).

If S is nonconstant, choose a root a. On the irreducible curve p=a,
the induced derivation is nonzero and DF vanishes. Its kernel in the
coordinate ring is C by the same function-field argument. Therefore
F modulo p-a is a scalar c, and F=c+(p-a)F1 for F1 in R. Write
S(t)=(t-a)S1(t). Then

    q-c/S(p)=F1/S1(p),       DF1=S1(p).

The subtracted term belongs to C(p), so its D-derivative is zero.
The denominator degree drops by one, and no new pole values occur.
Iteration ends with a constant denominator. Summing the subtracted
terms proves the statement. No localization is identified with R,
no quotient is treated as an algebra when it is only a module, and
no polynomial inverse is assumed.

## Controls and failure boundary

Positive: p=x and q=y+1/x have J(p,q)=1. The only polar fiber is
the irreducible x=0. F=xq=xy+1 reduces to c=1 there; subtracting 1/x
leaves the polynomial mate y. The pole-free case requires no correction.

Negative: p=x+x^3*y^2, s=xy, q=s/p satisfy

    Ds=x*p_x-y*p_y=p,       Dq=1.

Here p_x=1+3*x^2*y^2 and p_y=2*x^3*y never vanish simultaneously.
Nevertheless p=0 has three disjoint components x=0, xy=i and xy=-i.
The numerator F=s reduces to the incompatible constants 0,i,-i on them.
The rational q=y/(1+x^2*y^2) is regular generically on x=0 and has
poles on the other two components. Any r(p) with a pole at p=0 has
a pole on ALL three components, including x=0; an r regular at zero
cannot cancel q's poles. Thus no correction of the asserted form exists.
This is a rational, NOT polynomial, Keller pair. It is not a JC2
counterexample, and submersivity has not been confused with irreducibility.

More generally, at a reducible smooth fiber the curve-derivation kernel
is componentwise constants, not one diagonal copy of C. Our proof stops
exactly at that distinction. It does not assert that every reducible
polar fiber prevents correction: the constants may agree. No full
algorithm for that more general case is implemented or claimed.

## History, checking and disposition

ROOT checked the current canonical rational-mate and genus scopes in
APPROACHES7--8 and searched the ledgers and scoped reports for rational
mates, polar fibers and rational slices. The September13 13:32 journal
already records the BGM2014 fiber-integration/vanishing-period endpoint
and the exact Cassou-Nogues candidate rejection. The September14 rational
source-substitution and monomial-target exclusions remain stopped; the
present proof does not extend or reopen either family. Older rational
slices occur in xmodel/hamiltonian-kappa-gate-20260824.md and its review,
and in xmodel/ideation-20260903T1200Z-fable5.md. These located passages
are not whole-report reaudits. No exhaustive history or novelty claim.

Native Astra independently checked the displayed algebra and finite-polar-
fiber refinement, message-only, then completed before ROOT finalization.
It found no hidden constant-field premise and verified the negative
control. This is NOT different-model FIRST. No mathematical subprocess,
CAS, fleet worker, or external model lane ran. The proof is replayable by
the displayed DVR calculation and polynomial identities, not a software
certificate; there are no engine versions, random seeds or tested modes.

Primary discovery was limited: the BGM2014 abstract describes the already
known vanishing-period route, not a new supplied hypothesis. A fresh DOI
open returned a non-retryable safe-open error; it was not retried or
bypassed. No fresh whole-paper read or external theorem import is claimed.
The proof above is independent of that paper and of its analytic inputs.

The conditional construction interface is clearer: after finding a rational
mate, finite polar-fiber irreducibility can suffice to obtain a polynomial
mate. There is currently NO new noncoordinate p and q to which this is
attached. We select no finite-family search, period/control successor,
promotion or dependent lane. A consequential use requires ordinary FIRST;
this report remains producer-checked research, not an AUDIT entry. Global
ranking and the actual construction gap remain unchanged.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6708`.
- Body SHA-256:
  `0ed3beb175d4a86bd655d9082ce84d0a309ccbc13084c768094096d4b09c4eb9`.
- Frozen basis: `a8152e3232505eadcf0acbf03aa88333b04b3eed`.
