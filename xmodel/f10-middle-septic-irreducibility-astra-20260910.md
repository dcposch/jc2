# Actual septic irreducibility: three uniform residue classes proved

First 2026-09-10 07:23:59 UTC; cap 07:41:59, reserve 07:39:59. Seven current-pinned inputs, exact WHOLE/reuse scope recorded. Manual mathematics, zero scientific execution.

**Partial theorem:** for every integer r>=2 with r congruent to 1,2,3 modulo 7, S_(r/(3r+1)) is irreducible over Q_7, hence over Q. Consequently Z is a unit for EVERY actual middle h at these r, in the entire accepted leading algebra and every base change. This is an infinite-family result, not generic-parameter irreducibility or sampled evidence. Four residue classes remain unresolved.

First put tau=r/(3r+1) with r congruent to 1,3 modulo 7. Respectively, the denominator is a 7-adic unit and tau is congruent to 2,1. Import the accepted exact formulas

    D=12V²-12(1-tau)V+(1+tau)(2-3tau),
    K=-840V³+840(1-tau²)V²
       +42(1+tau)(2+tau)(4tau-3)V+k0,
    k0=2(2-3tau)(1+tau)(2+tau)(3+tau),
    S=2K²-140tau(1+tau-6V)KD+245gamma D²,
    deg(gamma)=3, lc(gamma)=-120tau.

All coefficients lie in Z_7. At tau congruent to 1 or 2, every factor of k0 is a unit. Also

    K=k0+7L, deg(L)<=3, L(0)=0.

Let S=sum_(i=0)^7 a_i V^i and normalize v_7(7)=1. The formulas give

    v_7(a0)=0;
    v_7(a_i)>=1 (1<=i<=3);
    v_7(a_i)>=2 (4<=i<=6);
    v_7(a7)=2.                                         (1)

Here a0 is 2k0² modulo 7. In 2K², terms not divisible by 49 have degree at most three. In the middle term, 140 contributes one factor 7 and the part using k0 has degree at most three; higher terms use the extra 7L. The last term has factor 245=5*49. Finally only that term reaches degree seven, with a7=-245*120*144*tau, of valuation exactly two. Zero intermediate coefficients cause no exception.

For completeness, (1) proves irreducibility directly. Extend v_7 to an algebraic closure and let x be a root, t=v_7(x). If t>-2/7, the constant term has uniquely smallest valuation. If t<-2/7, the leading term does: for i=1,2,3 the valuation difference is at least -1-(7-i)t>0; for i=4,5,6 it is at least (i-7)t>0. The constant also has larger valuation. A sum with a uniquely least-valued term cannot vanish. Therefore EVERY root has valuation exactly -2/7.

If a factor over Q_7 had degree d between one and six, its constant/leading coefficient ratio, the signed product of its roots, would have valuation -2d/7. That valuation must be an integer for a nonzero element of Q_7. Thus 7 divides d, contradiction. This proves the theorem without invoking a computed Newton polygon or irreducibility test.

For r congruent to 2 modulo 7, put b=1/tau in 7Z_7. Rescale V=tau X and Sbar=tau^-8*S(tau X). Directly from the same formulas,

    Dbar=tau^-2*D(tau X)=12X²+12(1-b)X+(1+b)(2b-3),
    Kbar=tau^-4*K(tau X)
      =-840bX³+840(b²-1)X²
        +42(1+b)(1+2b)(4-3b)X
        +2(2b-3)(1+b)(1+2b)(1+3b),
    gbar=tau^-4*gamma(tau X)
      =(1+b)(1+2b)(1+3b)-30(1+b)(1+2b)X
        +180(1+b)X²-120X³,
    Sbar=2Kbar²-140(1+b-6X)Kbar*Dbar+245gbar*Dbar².

All coefficients are integral at 7; Kbar's constant is -6 modulo 7, every nonconstant coefficient is divisible by 7, and Sbar's leading coefficient is -245*120*144. The identical argument gives (1) for Sbar and irreducibility. Nonzero rational rescaling preserves irreducibility, covering this entire third family regardless of v_7(3r+1).

By accepted17zzd, B_nu=Q[V]/(S), D is a unit and DZ=T, with T of degree exactly five and leading coefficient 10080. Irreducibility implies gcd(S,T)=1. A rational Bezout identity aS+bT=1 then gives Z inverse bD in B_nu. Unitness survives Laurent scale extension and all further base changes, including nonreduced ones. No component or guard is removed.

**Remaining scope:** r congruent to 0,4,5,6 modulo 7 is not settled. The proof's valuation hypotheses fail there; failure is not reducibility. No actual reducible S or resonant leading point is exhibited. Squarefree degree seven alone is not irreducibility; it did not replace (1).

No new OPEN ID. Remaining quantity: uniform irreducibility or S,T coprimality on those four actual integer families. Cheapest next proof obligation is a uniform obstruction there, not more samples or generic specialization. No full-source, forcing, JC2, novelty, speed or execution claim. Own WHOLE read and final OPEN/collision review completed 07:34 UTC; no placeholder, pending writer or unquantified raised OPEN remains. Inputs unchanged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `4455`.
- Body SHA-256:
  `7adc6a874a145570c6d38a083663b582e99fd9637c83629100a751931098282b`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
