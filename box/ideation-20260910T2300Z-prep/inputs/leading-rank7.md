# Remaining middle unit question: GAP; complete seven-point reduction

First 06:57:30 UTC; stop 07:15:00, reserve 07:13:00. Five current-pinned inputs; WHOLE/reuse scopes recorded separately. Manual mathematics only.

**GAP:** no uniform Z-unit proof or actual resonance point. The concrete simplification below removes every leading localization and proves exactly seven geometric normalized leading points. The old Laurent scale remains external; no full-source normalization is performed.

Fix r>=2, r+2<=h<=2r, m=3r+1, n=5r+2, nu=n/m, alpha=(m+n-h)/m. Write tau=2-nu, and abbreviate accepted full-boundary (3),(8) by D(V),K(V),beta(V),gamma(V), so

    Q_nu-7E_nu=K+210DW, E_nu=360W²+beta W+gamma.

Manual polynomial division gives

    K=[-70V+70tau(1-tau)]D+56f(V-v*),
    f=(2tau-1)(3tau-1)(3tau-2), v*=3(1+tau)/14,
    D(v*)=(1+tau)(6tau-1)/49.                            (1)

Indeed the remainder coefficients are 56f and -12(1+tau)f. Since 2/7<=tau<1/3, both f and e=D(v*) are nonzero rationals. An explicit Bezout identity AD+BK=1 is

    q=-70V+70tau(1-tau), J=12(V+v*)+12(tau-1),
    A=(1+Jq/(56f))/e, B=-J/(56fe),

because D=e+(V-v*)J. In the full leading algebra K=-210DW, hence D(A-210BW)=1: no component is discarded.

Using P,ell,Z from accepted 17zz (6), define

    S=2K²-140tau(1+tau-6V)KD+245gamma D²,
    T=DP-ell K.                                        (2)

Here S=245D²E_nu(V,-K/(210D)), degree exactly seven, leading coefficient -245*120*144*tau. Also S mod D=2K², so gcd(S,D)=1. Consequently the mutually inverse substitutions

    Q[V,W]/(E_nu,Q_nu) <-> Q[V]/(S), W=-K/(210D)        (3)

are exact, including nilpotents: S enforces E, and K+210DW enforces Q-7E. No mathematical computation of a gcd is claimed; its nonvanishing follows from (1).

The original guard is automatic. Without using that guard, E=Q=0 gives d=c^nu+O(z^8), where c=1+z+Vz²+Wz³ and d=trunc_5(c^nu). Thus mc d'-nc'd is polynomial O(z^7), with coefficient -W*t5. In any maximal residue field with W*t5=0 it vanishes, forcing m*deg(d)=n*deg(c). But 5m-3n=-1 gives gcd(m,n)=1, m>=7, and 1<=deg(c)<=3: impossible. Therefore W*t5 is a unit of the entire algebra (3).

The septic is squarefree, not assumed so. At any geometric point, c,d are simple and coprime by mc d'-nc'd=-W*t5*z^7. An infinitesimal leading variation has c_dot=e_V*z²+e_W*z³ and d_dot=nu*c^(nu-1)c_dot+O(z^8). Thus

    H=n*c_dot*d-m*c*d_dot=lambda*z^8.

With k=lambda/(W*t5), subtracting k*z times the leading identity gives

    n(c_dot-kzc')d=mc(d_dot-kzd').

Coprimality and degrees imply c_dot-kzc' is a constant multiple of c. Its constant term makes that multiple zero; its linear term makes k=0. Hence the tangent vanishes. The finite algebra (3) becomes reduced over an algebraic closure (each Artin-local maximal ideal has zero cotangent, hence equals its square and is zero). Thus it is finite-etale of rank seven; all seven points retain the guard.

Finally DZ=T in this algebra. T has degree exactly five with leading coefficient 10080. Hence at least two of the seven geometric normalized leading points are nonresonant for each actual pair. The unresolved issue is whether any of the other at most five points satisfies T=0. Neither separability nor degree proves gcd(S,T)=1. Abstract control: a split septic and a product of five of its linear factors have precisely this failure; that is not an actual leading counterexample.

No new OPEN ID: remaining quantity is the exact common-point question for this explicit septic/quintic, uniformly at linked r,h. Cheapest remaining proof obligation: their uniform coprimality, retaining all seven components; a sample cannot close it. No source, forcing, JC2, irreducibility, novelty, speed or execution claim. Own WHOLE read completed 07:09:30 UTC; final OPEN/collision clarification reread before marker. All inputs immutable.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `3886`.
- Body SHA-256:
  `9321ca778aac08de9f1414eabc111c93bdcfab1ddecf1023ceb44a608d3e7164`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
