# Registration: D1 `a>=13` grade-38 odd-row `J` obstruction

Date: 2026-08-26

Status: **PREREGISTERED DUAL-AWS UNIFORM EXACT-SOURCE OBSTRUCTION.**

## Claim under test

On the D1 high-contact chart, write

```text
A=sigma^13*theta*Abar,
C=sigma^14*theta*Cbar,
R=sigma^13*theta*eta*Rbar.
```

Substitution `theta=sigma^n` and `eta=sigma^s` represents every integer
contact

```text
a=13+n,  c=a+1,  r=a+s,  n,s>=0.
```

Retain independent moving jets of `p,k10,k6,k2,mu2,mu4,mu6` and the sparse
nonzero `J/4` target.  Through absolute grade 38, every ordinary source term
on this cone has pole denominator at most `L^2`; the first possible
`k2*C/L^3` term is grade `26+a>=39`.

For any source with pole order at most two, the complete moving odd Faber rows
satisfy the formal-series recurrence

```text
Phi7 = (p(sigma)/4)*Phi5
     + (p(sigma)^2/32)*Phi3
     + (p(sigma)^3/128)*Phi1.                 (R)
```

The literal target contributes only `-sigma^38*J/4` to `Phi7`.  Therefore the
complete source should satisfy

```text
Phi7-(p(sigma)/4)Phi5-(p(sigma)^2/32)Phi3
    -(p(sigma)^3/128)Phi1
  = -sigma^38*J/4 mod sigma^39.              (J38)
```

If every source row vanishes, `(J38)` forces `J=0`, contradicting the Keller
chart `D(J)`.  No radical, contact-coefficient localization, or broad standard
basis is required.

## Exact acceptance tests

1. Rebuild all seven frozen literal source rows at the symbolic baseline
   `a=13`, retaining enough independent jets to determine every coefficient
   through grade 38.
2. Verify exact divisibility of the odd recurrence by `sigma^38`, exact
   coefficient `-J/4`, and the congruence `(J38)` before radicals.
3. Verify the contradiction scheme-theoretically by adjoining `iJ*J-1` and
   obtaining the unit ideal.
4. Verify the identity polynomially in independent `theta,eta`; this is the
   homogeneous translation certificate for all `n,s>=0`, not a finite sample.
5. As a sharp negative control, rebuild `a=12` and require the coefficient of
   `(R)` at grade 38 after removing `-J/4` to be nonzero and to depend on the
   leading `k2` load.  This is the expected `k2*C/L^3` wall and prevents
   extending the theorem to `a=12`.
6. Run exact Q on Box03 and `F_65521` on r6d; require rc 0, no diagnostics,
   frozen ancestry, a nonempty Chebyshev/Pell control, and zero swap.

## Scope firewall

A PASS excludes only the registered D1 contacts `a>=13,c=a+1,r>=a` on the
Keller `D(J)` chart, after the cited upstream square/D1 gates and for the seven
literal Faber rows.  It does not settle `a=10,11,12`, other contact cells,
`p=0` or `k0=0` lifecycle routing, the whole square component, order two,
`(8,12)`, maximum twelve, or JC2.

