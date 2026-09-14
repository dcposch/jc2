# Three residue families: a uniform unit subfamily and exact common obstruction

First 2026-09-10 07:56:11 UTC; stop 08:14:11, reserve 08:12:11. Seven pinned inputs, exact WHOLE/reuse scope recorded. Manual only; neither later valuation report is used.

**Partial theorem; full target GAP.** For r congruent to 4,5,6 modulo 7, respectively, Z and H7_h are units for every allowed h EXCEPT the following still-unresolved residue sets:

| r modulo 7 | Unresolved h modulo 7 |
|---|---|
| 4 | 3,4,5 |
| 5 | 0,3,5 |
| 6 | 0,1,3 |

This is one uniform infinite-family criterion, not sampled evidence. No actual resonance is exhibited.

Set m=3r+1, tau=r/m, nu=2-tau, alpha=(8r+3-h)/m. Use accepted17zz/17zzb/17zzd's exact D,K,gamma,S,P,ell,Z,T, with B_nu=Q[V]/S, W=-K/(210D), D and the original guard units, and T=DZ. All parameters are 7-integral; tau has residue 3,6,4 respectively. Thus

    k0=2(2-3tau)(1+tau)(2+tau)(3+tau)=0 modulo 7.

Every nonconstant K coefficient is also divisible by 7. Put J=K/7 in Z_7[V]. The WHOLE septic becomes

    S/49=2J²-20tau(1+tau-6V)JD+5gamma D².              (1)

This is integral with leading coefficient -5*120*144*tau, a 7-adic unit. Every root V is therefore integral: at negative valuation the highest-degree term of the monic-up-to-unit polynomial (1) would be uniquely least-valued. At each such root, beta,gamma are integral, so E_nu=360W²+beta W+gamma=0, with 360 a 7-adic unit, similarly forces W integral. This covers ALL seven points, without requiring D to be a 7-adic unit or discarding a guard.

Let f(X)=(X-3)(X-4)(X-5)(X-6), and let

    B3=[f(alpha)-f(nu)]/(alpha-nu)

mean the polynomial divided difference. Accepted Z has all nonconstant terms divisible by 7:

    Z=840V³+420(alpha+nu-7)V²+42B2 V+B3+210ell W.

Consequently its residue at EVERY leading point is the SAME rational scalar B3 modulo 7. Here nu has residue u in {6,3,5}, respectively. If R={3,4,5,6}, polynomial specialization gives exactly

    B3 modulo 7 = product_(b in R, b!=u)(alpha-b).      (2)

In particular alpha=u is NOT exceptional: (2) then equals f'(u)!=0. No division by alpha-nu in a residue field occurred. Since alpha has residue h, 4-4h, 6-3h in the three families respectively, (2) gives precisely the table above.

Outside that table every point has nonzero Z, hence gcd(S,T)=1 over Q_7 and Q. A rational Bezout identity aS+bT=1 supplies Z inverse bD in the entire B_nu. Unitness survives the free Laurent scale and every base change, including nilpotents; the accepted rational prefactor gives H7_h-unitness. No inverse was inferred merely from a generic component.

The remaining obstruction is sharper than an unknown resultant: for EVERY listed residue pair, Z reduces to zero at EVERY leading point, not merely at a possible exceptional component. Indeed the product of its seven values, the rational norm N(Z), is 7-integral and satisfies

    N(Z)=B3^7 modulo 7.                                 (3)

On the residual locus, more precisely, every Z-value is divisible by 7 in its valuation ring, so N(Z) belongs to 7^7*Z_7. Thus this entire first integral reduction is exhausted there. Divisibility neither forces the rational norm to be zero nor proves it nonzero. Control: the nonzero rational scalar 7 itself has these properties but is a unit in B_nu. Also retaining Q_alpha alone would wrongly retain alpha=nu modulo 7; polynomial division (2) is essential.

No new OPEN ID. Remaining quantity: actual linked pairs in the nine table cells, still with r+2<=h<=2r and every original leading equation/guard. Cheapest new proof obligation is a uniform nonzero-norm/common-root obstruction on this whole residual locus, using information beyond (3), not more first-level samples. No actual factor/common root, all-family closure, forcing/source exclusion, finite-r bound, JC2, speed or execution claim. Own WHOLE, exact-divisibility/OPEN/collision review completed 08:01 UTC before marker. No unfinished writer or unquantified raised OPEN remains.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4018`.
- Body SHA-256:
  `6b89500c54e6ae7ce8f2f037626340ddab6302607dcf2bb7ac10c5fe888249b2`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
