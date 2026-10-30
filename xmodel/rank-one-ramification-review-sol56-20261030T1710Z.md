# Independent rank-one ramification review

Status: FINAL
Verdict: PASS
Completed UTC: 2026-10-30T17:13:05.331358+00:00
Role: independent hostile review, not coauthor or method designer.
Configured model: gpt-5.6-sol. Actual hosted identity: UNVERIFIED.

## Exact scope reviewed

I reviewed the sealed CANDIDATE.md at SHA-256 `6d817111ca63b8b7fe651a893c2a9eb8d101ea4cb08083159d07bde5a5e2a92e` and basis `5ed1dba19564865a10dee632055fca07110f969f`.
The claim is only local: for a finite holomorphic map between smooth complex surface germs, if the reduced ramification support is one smooth curve E and the differential has rank one at the point, then E has local parameter order one over the normalization of its image branch.

## Proof audit

1. Rank one supplies a target coordinate P whose pullback has nonzero differential. The holomorphic coordinate theorem permits using that pullback as a source coordinate p and completing both source and target coordinate systems. In these coordinates the Jacobian determinant is Q_v.

2. If d(P|E) is nonzero, P|E has order one. After factoring the finite nonconstant map E to its image through the normalized image curve, every pulled-back target function has order divisible by the local parameter order delta. Thus delta divides one.

3. If d(P|E)=0, smoothness of E and dp nonzero make E a graph p=h(v) with h(0)=h'(0)=0. If h is identically zero, the single-support factorization Q_v=p^k U makes both P and Q constant on E; that would put a curve in one fibre, impossible for a finite map.

4. Otherwise m=ord(h)>=2. Writing h(v)=v^m after an invertible holomorphic reparametrization is valid: take an analytic m-th root of the unit multiplying v^m. The derivative change contributes only a unit, so the ramification factorization remains
   `Q_v=(p-v^m)^k U`, with k>=1 and U(0,0)=c nonzero.

5. B(p)=Q(p,0) is holomorphic, and replacing Q by Q-B(P) is an invertible triangular target-coordinate change. On E its restriction is exactly
   `integral_0^v (v^m-s^m)^k U(v^m,s) ds`.

6. Give p weight m and v weight one. The constant c contributes order mk+1 with coefficient
   `c integral_0^1 (1-t^m)^k dt`,
   which is nonzero (indeed positive rational after binomial expansion). A monomial p^a s^b of U with (a,b)!=(0,0) contributes order `mk+ma+b+1`, strictly larger. Hence there is no leading-term cancellation.

7. The two target restrictions therefore have exact orders m and mk+1. If t is a uniformizer of the normalized image and its pullback to E has order delta, the DVR order formula makes delta divide both. Since gcd(m,mk+1)=1, delta=1.

This uses no smoothness or immersion of the image curve. The normalization may parametrize a cusp; only its one-dimensional normal local ring and uniformizer are used.

## Finite rank-zero example

For `P=v^2+u^3` and `Q=2v^3+3u^3 v`, direct differentiation gives
`P_u Q_v-P_v Q_u=3u^2(6v^2+3u^3)-2v(9u^2v)=9u^5`.
Thus the reduced ramification curve is the smooth line E={u=0}, while every first derivative vanishes at the origin and the differential there has rank zero.

The identities `v^3-3Pv+Q=0` and `u^3=P-v^2` prove finiteness: v is integral over C[P,Q], u is integral over C[P,Q][v], and integrality is transitive.
On E the parametrization is `v -> (v^2,2v^3)`, with image equation `Q^2=4P^3`. Its local ring has integral closure C{v}; equivalently its function field contains `v=Q/(2P)`. Hence v is the primitive normalization parameter and the map to the normalization has order one.
The example therefore refutes only the shortcut “smooth reduced ramification support implies rank one.” It neither refutes nor proves the rank-zero analogue.

## Foundations used

The proof uses standard complex-analytic facts: the holomorphic coordinate/implicit-function theorems; factorization by the reduced equation of a smooth divisor in a regular analytic local ring; analytic roots of units; finiteness implying zero-dimensional fibres; existence and universal property of normalization of a reduced curve germ; and the DVR order formula under a finite map of smooth curve germs. These are identified foundations, not a new literature audit.

## Limitations and forbidden strengthenings

- The smoothness of both surface germs, the single smooth reduced ramification component, and rank one at the point are essential premises of this proof.
- It does not treat a singular normalization surface, a singular reduced ramification support, or a rank-zero point.
- Parameter order one over the normalized image does not say that the image is smooth or immersed in the target.
- A pointwise rank-one lemma is not a theorem that an entire omitted curve has degree one. No global attachment, properness, boundary-degree, corank-zero, Keller, N=1, or JC2 conclusion follows.
- The polynomial example is not a Keller map and its complement is `G_m x A^1`; it is only a finite local/global scope control.
- Review was manual and packet-confined. No CAS, scientific computation, source query, or new control search was performed.

## Collisions and novelty

Outside-packet search was not authorized. The stopped historical DC2-REVIEW body was not supplied or read, so novelty and historical priority remain unassessed.

## Reading and output audit

- Required non-STATE body displayed: exactly 1650 LF, comprising MANIFEST.json 210 LF and the other required non-STATE inputs 1440 LF; cap 2400 LF.
- STATE.md displayed: exactly 156 LF under its separate allowance.
- Repeated input-body LF: 0. Clipped-output LF credited: 0.
- Own ACK/report body preview LF: 0; all report writes were quiet and the ACK body was never displayed.
- One malformed reader invocation emitted command usage only and no packet body; it contributes 0 LF and no reading credit. The corrected required window was then read once.
- Pinned helper sources were executed only and received no human-reading credit.

## Verdict

PASS for the exact local rank-one lemma, the stated finite rank-zero example, and the candidate’s explicit limitations. This verdict supplies no novelty finding and authorizes none of the stronger conclusions excluded above.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6136`.
- Body SHA-256:
  `2ca3393c3e7882e9a008b70bdc9d548bd2dbe7c0cafbbf9a8ac55d66b1140768`.
- Frozen basis: `5ed1dba19564865a10dee632055fca07110f969f`.
