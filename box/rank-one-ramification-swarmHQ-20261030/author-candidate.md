# Smooth ramification at a rank-one point

Status: INTERNAL / ROOT-MANUAL / UNREVIEWED CANDIDATE. No JC2 conclusion or novelty claim.
Task: RAMCURVE1645. Public basis: 5ed1dba19564865a10dee632055fca07110f969f.
This is a local analytic argument; the actual finite normalization need not be smooth, and its differential need not have rank one everywhere on the omitted boundary.

## Statement

Let f:(S,p)->(T,q) be a finite holomorphic map of smooth complex surface germs.
Suppose the reduced ramification divisor near p is a single smooth curve E, and rank(df_p)=1.
Then E maps unramifiedly to the normalization of the image branch f(E) at the point over q.
Here unramified means local parameter order one; it does not assert that f(E) is smooth or immersed in T.
The standard existence and local-parameter description of finite normalization of a complex curve germ are used.

## Proof

Choose a target coordinate P whose pullback has nonzero differential at p, and use p=P as a source coordinate with a second coordinate v.
Write the other target coordinate as Q(p,v). If P restricted to E has nonzero differential, its order one already proves the claim.
Otherwise, smoothness of E makes E a graph p=h(v) with h(0)=h'(0)=0.
If h were identically zero, the ramification identity Q_v=p^k U(p,v), k>=1 and U a unit, would make Q(0,v) constant.
Then f would contract E, contradicting finiteness. Thus ord(h)=m is a finite integer at least two.
A change of the source coordinate v by an invertible holomorphic germ puts h(v)=v^m.
Because the ramification support is exactly E, in these coordinates

    Q_v(p,v) = (p-v^m)^k U(p,v),   k>=1,   U(0,0)=c != 0.

Subtract the target function B(P), where B(p)=Q(p,0). This is an invertible local change of the second target coordinate.
Consequently, on E,

    (Q-B(P))|E = integral from 0 to v of (v^m-s^m)^k U(v^m,s) ds.

Give p weight m and v weight one. The constant term c of U contributes

    c * v^(mk+1) * integral from 0 to 1 of (1-s^m)^k ds.

The displayed integral is a nonzero rational number (it is positive for these positive integers m,k).
Every remaining monomial of U has positive weight and contributes strictly higher order in v after integration and substitution p=v^m.
Thus the restrictions of P and Q-B(P) to E have respective orders m and mk+1.
If the map E->normalization(f(E)) had local parameter order delta, the orders of all pulled-back target functions would be multiples of delta.
Therefore delta divides both m and mk+1. Their greatest common divisor is one, proving delta=1.

## Rank zero is not automatically excluded

The finite polynomial map

    P(u,v)=v^2+u^3,   Q(u,v)=2v^3+3u^3*v

has determinant 9u^5, hence smooth reduced ramification curve E={u=0}, but its differential has rank zero at the origin.
Finiteness follows directly from v^3-3Pv+Q=0 and u^3=P-v^2: both source coordinates are integral over C[P,Q].
The restriction E->f(E) is v->(v^2,2v^3), whose normalization parameter is v; this example does NOT refute the proposed unramified conclusion at rank-zero points.
It refutes only the shortcut that smooth ramification support forces rank one.
It is not an actual Keller normalization with a whole omitted-boundary complement A2: its complement S\E is Gm x A1.
No family search or CAS was performed.

## Remaining gap and prospective use

If this local lemma survives independent review, at a smooth normalization point with rank-one differential it would exclude ramification of the omitted curve over its image normalization.
Rank-two points are already locally unramified. Singular source points and rank-zero smooth points remain untreated.
The broader statement for every smooth reduced ramification curve is OPEN here; no degree-one conclusion for an entire omitted A1 curve follows.
Do not use this candidate to constrain the actual boundary degrees before independent review.
The local finite example is only a scope control, not a polynomial-Keller counterexample or a global exclusion.

## Collision scope

Two complete frozen Markdown searches were performed. The current APPROACHES routing ranges91-114 and1083-1106 were read (48LF).
The canonical historical avenues/DC2-REVIEW.md failed seal verification: no standalone BODY-END marker. Its body was not read, repaired, or sought through a copied alternative.
Thus possible historical priority for this local argument remains unassessed. Existing SNC and zero-support statements were not reproved or promoted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4485`.
- Body SHA-256:
  `2d5946d04d6538d98e6a836c0e657507833226dad71a9fb744aaf16ff78f596d`.
- Frozen basis: `5ed1dba19564865a10dee632055fca07110f969f`.
