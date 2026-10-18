# One non-reduced affine fiber: primitivity survives Keller pullback

Claim ID: ONE-BAD-FIBER-PULLBACK-1. Producer: swarmHQ ROOT, Astra-assigned; hosted identity unverified.
Date2026-10-18. Basis822390c4a50c0573613c1c5140ba2eaa9eadcfec.
Evidence: MANUAL, using the named standard curve and etale facts below.
Lifecycle: PRODUCER-CHECKED / UNPROMOTED; independent hostile review pending.
External novelty UNKNOWN. This is not a proof or counterexample to JC2.
## Statement and definitions

Work over C. Let F=(P,Q):A2_source->A2_target have nonzero constant Jacobian.
Write K=C(u,v), L=C(x,y), identifying K with its image under F*. Let f=a/b in K
be nonconstant, with coprime a,b in C[u,v], and assume C(f) is algebraically closed in K.
For lambda finite set D_lambda=div(a-lambda*b) on the AFFINE target; set D_infinity=div(b).
An empty divisor is reduced. Assume at most ONE of these divisors is non-reduced.
Then C(f), embedded through F*, is algebraically closed in L.
No basepoint-free, target-fiber genus, properness or nonproper-locus hypothesis is imposed.
## Elementary source facts

1. A nonconstant rational function s=g/h on A2, with coprime g,h, has at most one
   empty affine fiber divisor. Such a divisor is empty exactly when g-alpha*h
   (or h at infinity) is a nonzero constant. Two distinct such linear combinations
   would force both g and h constant. This includes pole fibers and affine basepoints.
2. Every target prime divisor D is dominated by a source prime divisor C under F.
   If d is its irreducible equation, d(P,Q) is nonconstant by dominance, hence has
   a prime divisor C. Etaleness makes F quasi-finite, so C cannot map to a point;
   its image is dense in D. Etaleness also gives ramification index one at C.
3. Consequently, if h in K* pulls back to an n-th power in L*, then h is an n-th
   power in K*: fact2 makes every affine prime valuation of h divisible by n;
   factor numerator/denominator in the target UFD and take an n-th root of the constant.
4. Pullback preserves reduced fiber divisors. Indeed etaleness preserves their
   generic multiplicities. Also a(P,Q),b(P,Q) are coprime: a common source prime
   would map into the finite target basepoint set, contradicting quasi-finiteness.
   Thus these pullbacks are exactly the fiber divisors of f composed with F.
## Proof

Let E/C(f) be any finite intermediate field in L. The smooth projective curve with
function field E is dominated rationally by A2. Restrict a nonconstant rational map
to a suitable line and complete it to a nonconstant map P1->C_E. Riemann-Hurwitz
forces genus(C_E)=0; over C this gives E=C(s). Write f(F)=R(s), where R in C(z)
has degree n=[E:C(f)]. Suppose n>1. Choose b0 in P1 containing the possible bad
fiber value (arbitrary if no bad fiber exists).
If R ramifies at alpha with R(alpha)!=b0, fact4 says the corresponding fiber of
R(s) is reduced. Any prime in the s=alpha fiber would have multiplicity
e_alpha(R)*ord_C(s-alpha)>1 (use local coordinates also at infinity). Hence that
s-fiber is empty. By fact1 there is at most one such ramification point alpha.
Let m be the number of distinct points of R^-1(b0). Their total ramification is n-m.
Riemann-Hurwitz on P1 gives total ramification outside that fiber n+m-2. It is
supported at at most one point, of contribution at most n-1. Thus m=1, and there
is exactly one outside ramification point, with contribution n-1. Both are totally
ramified, over distinct values. Therefore R=M o (z^n) o N for Mobius maps M,N:
send the two branch values to0,infinity and use the divisor n(alpha1-alpha0).
It follows that (M^-1 o f)(F)=(N(s))^n. Fact3 gives M^-1 o f=t^n in K for some t.
Then C(t)/C(f) has degree n, contradicting target primitivity. Hence n=1 for every E.
## A pencil with an affine basepoint and a construction consequence

Take f=(v^2-u^3)/u^2. Its only bad fiber is D_infinity=2{u=0}; each finite
numerator v^2-u^3-lambda*u^2 is squarefree. With t=v/u one has u=t^2-f and
v=t(t^2-f), so K=C(f,t), proving primitivity. The basepoint (0,0) is genuinely affine.
For ANY R in C(s) of degree>1, the donor H_R(s,t)=(t^2-R(s),t*(t^2-R(s)))
therefore has NO dominant finite rational source substitution producing a polynomial
Keller pair: its pullback of f is R(s), supplying a forbidden intermediate C(s).
This does not cover arbitrary target transformations or supply a pencil for a general Keller map.
## Dependencies, prior comparison, and negative control

Standard imports: Keller implies dominant etale/quasi-finite; curve function-field
correspondence, extension of rational maps from smooth projective curves, Riemann-Hurwitz,
and genus-zero curves over C. The remaining arguments are explicit UFD/divisor arguments.
The Sep25 HQ different-pencil gap inferred only multiplicity of an ACTUAL component,
not the whole fiber gcd. Here every component of a good fiber has multiplicity1;
no gcd inference is made. The basepoint-free theorem at public822390c4 assumes a
morphism with rational generic fiber; this theorem allows basepoints and arbitrary genus,
but imposes its separate reduced-fiber hypothesis. No equivalence of the two scopes.
Primitivity cannot be dropped: F=id and f=u^n,n>1, satisfy the one-bad-fiber condition
but C(u^n) is not algebraically closed in C(u,v). No computation or primary-paper audit.
## OPEN(S) RAISED

None. Global finite normalization and JC2 remain unresolved; no automatic extension is claimed.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

Corpus basis: `822390c4a50c0573613c1c5140ba2eaa9eadcfec` (Git blobs only).
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5623`.
- Body SHA-256:
  `78d0b78beb47fc797759b92433c95eb6797ee1211d95088f5a8e207d750448bb`.
- Frozen basis: `822390c4a50c0573613c1c5140ba2eaa9eadcfec`.
