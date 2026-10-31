# Smooth pencil without A1 fibres: independent review

Verdict: PASS
Lifecycle: independent hostile review; MANUAL
Candidate SHA-256: 129038db01bb40a2cc951a9a7a34190c04ef04053bc3efe4d160afbde1e1af3a
Configured model: gpt-5.6-sol; hosted identity: UNVERIFIED
Started UTC: 2026-10-31T17:21:50.910816+00:00
Completed UTC: 2026-10-31T17:26:05.265531+00:00

## Exact scope

Over C, for f=xy-1 and g=x+y(xy-1), the map h=[f:g]:A2->P1 is a
smooth surjection. Its fibres are irreducible C* or A1 with two points
removed, never A1. This refutes the shortcut asserting that smoothness
and surjectivity of such a pencil alone force a special A1 fibre.
It does not refute any statement retaining the constant-Jacobian or
radial-etaleness hypothesis. It is not a Keller counterexample.

## Base points and smoothness

Direct expansion gives
(1+y^2)f-yg=-1.
Thus f and g generate the unit ideal and [f:g] is a morphism everywhere.
With df=y dx+x dy and dg=(1+y^2)dx+(2xy-1)dy, direct collection gives
g df-f dg=dx+(x^2-f^2)dy.
The dx coefficient is one. On g!=0 this form divided by g^2 is d(f/g);
on f!=0 its negative divided by f^2 is d(g/f). In either target chart
the relative graph equation has a unit partial derivative. The relative
hypersurface Jacobian criterion therefore proves smoothness, including
the fibre over infinity; no flatness inference is being assumed.

## Every finite fibre and both inverse maps

For [lambda:1], set D=y-lambda-lambda*y^2 and F=f-lambda*g. Expansion gives
F=xD+lambda*y-1,
Dg-1=(1+y^2)F.
Hence in A_lambda=C[x,y]/(F), D is a unit with inverse g and
x=(1-lambda*y)/D. The map C[y,D^(-1)]->A_lambda sends y to its class.
The reverse map sends y to y and x to (1-lambda*y)/D; F maps to zero.
The displayed relations make both composites the identity. These are
inverse regular maps, not a birational parametrization.

For lambda=0, D=y and the fibre is C*. For lambda=1/2,
D=-(y-1)^2/2; for lambda=-1/2, D=(y+1)^2/2. Inverting either square
inverts its linear factor, so both double-root fibres are C*. For every
other nonzero lambda, discriminant 1-4lambda^2 is nonzero and D has two
distinct roots, giving A1 minus those two points. No exceptional value
or nonreduced double-root scheme is omitted.

## Infinity, nonemptiness, and components

On g=0, the Bezout identity makes 1+y^2 invertible, while
x=y/(1+y^2) and f=-1/(1+y^2).
Substitution in both directions gives
C[x,y]/(g) isomorphic to C[y,(1+y^2)^(-1)],
so the infinity fibre is A1 minus i and -i.

Every displayed ring is a nonzero localization of C[y]. It is a reduced
domain, hence its fibre is nonempty, irreducible and connected. Each ring
has a nonconstant unit, whereas C[t] has only constant units. Thus no
fibre is A1, and irreducibility rules out a separate A1 component.
The finite fibres plus the nonempty infinity fibre prove surjectivity.

## Jacobian, radial failure, and Keller boundary

The polynomial Jacobian is
J(f,g)=xy^2-x-y,
which is nonconstant and vanishes at (0,0). On a finite generic fibre,
g=1/D and dg/dy=(2lambda*y-1)/D^2. At y=1/(2lambda) this derivative
vanishes, while D=(1-4lambda^2)/(4lambda) is nonzero when
lambda is not 0, 1/2, or -1/2. At infinity,
f=-1/(1+y^2) has derivative zero at y=0. Thus radial etaleness fails.
(The three finite C* exceptional fibres themselves have nowhere-zero
radial derivative; this does not repair failure on the other fibres.)

For comparison, if J(P,Q) is a nonzero constant and (P,Q) has no common
zero, then on P=lambda*Q the radial Q is nonzero. A tangent annihilating
both d(P-lambda*Q) and dQ would also annihilate dP, contradicting
dP wedge dQ!=0. Thus Q restricts etale to every finite fibre component;
the same argument uses P at infinity. The present pair omits (0,0) but
fails precisely this Keller hypothesis. JC2 and Keller surjectivity
remain unresolved.

## Reading and output audit

Packet preflight verified all 15 members and the candidate seal.
Required bodies read in full: 1,726 non-STATE LF and 200 STATE LF in
44 verified windows; all returned continuations were consumed.
Repeated body LF: 0. Unrecovered/truncation credit: 0.
Reader help invocations: 2. Preflight body LF: 0.
ACK/report file-body previews: 0; startup emitted one status line only.
One post-reading report command failed in its wrapper before Python
launched and changed no file; the corrective write was immediate.
No source/history query, web access, CAS/scientific computation,
secondary model, subagent, Git action, or protected-tree access occurred.
CHECKS.json was treated only as a symbolic receipt; every identity above
was checked independently. The false y^2-1 coefficient was not inherited.
Novelty remains unassessed. ROOT alone decides promotion; no successor.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4741`.
- Body SHA-256:
  `c16c3647668b31b7a03419875b49d739cc704256eddf958267aa74e230ab815b`.
- Frozen basis: `c2d8ede89f709b2c9da2851ba00f34e5b6b703e3`.
