# Exact-square affine-`mu2` support theorem

Date: 2026-08-26

Status: **PRODUCER THEOREM; CAS-FREE SET-THEORETIC PROOF PLUS EXACT-Q
RADICAL CERTIFICATE.  PENDING HOSTILE REVIEW.**

## 1. Charged custody

```text
cases/max12_812_order2_exact_square_affine_mu2_20260826/RESULT.md
  55adc49f379b36b425322218ccdfed9a6359ed6e6e41713543125da01f3f1f95

cases/max12_812_order2_exact_square_affine_mu2_20260826/EVIDENCE.sha256
  f285b6df59805fa6291eef974ad45c4d05db9942a7e28482b362174e568273ef

cases/max12_812_order2_exact_square_affine_mu2_20260826/FREEZE.sha256
  88440f2a46078f0c9708587ea6db8c6d4f3e5f306affe35c94d2da521e8d4e5e

cases/max12_812_order2_exact_square_affine_mu2_20260826/compile_affine_mu2.py
  4eb04bca26c3bee1c76534f8fc02efdbb982316071e583676b65fb395f5f2c4b

xmodel/max12-812-order2-exact-square-affine-mu2-hand-elimination-20260826.md
  20cc74b60fdf0b599094c8b5d6cf61e48773391d3c861409ef0e20f4a8a85ff2

xmodel/max12-812-order2-exact-square-pell-chebyshev-support-theorem-20260826.md
  523a32dd0da666029e2dee1531e0cd0775c0010d07d40ef440dfe5164cf152cf
```

The evidence manifest verifies every retrieved V2 compiler, generated
Singular source, result, launch-registration, engine, and validator file.
The characteristic-zero lane is the producer.  The characteristic-65521
lane is an independent software/control comparison only.

## 2. Statement

Let `K` be a characteristic-zero field and work after extension to its
algebraic closure.  Put

```text
Q=z^4+p*z^2+c*z+r,
H=sqrt(Q)*(Q^2+beta*Q+gamma),
H-[H]_+ = sum_(ell>=1) h_ell*z^(-ell),
```

where `sqrt(Q)=z^2+O(1)` at infinity.  Consider the affine receiver

```text
h1=h3=h4=h5=h6=h7=0,       h2=mu2.                 (2.1)
```

Its reduced support is exactly

```text
V(c,mu2,p^2-4*r)

union

V(c,mu2,16*beta-5*(p^2-4*r),
          256*gamma-5*(p^2-4*r)^2)

union

V(p,c,5*r^2+8*r*beta+16*gamma,
      32*mu2-r^2*(5*r+4*beta)).                    (2.2)
```

In particular, there is no point on `D(c)`.  The third component is the
only support not already present in the seven-zero-tail square/Pell
receiver.

Over `Q`, if `I` is the integerized ideal of (2.1), the exact producer also
certifies the scheme-independent reduced equality

```text
rad(I) = I_square intersect I_Chebyshev intersect I_affine.  (2.3)
```

Each displayed component ideal is prime.

## 3. Proof

The integerized coefficients use

```text
(h1,h2,h3,h4,h5,h6,h7)
 =(E1/256,E2/1024,E3/512,E4/2048,
   E5/2048,E6/32768,E7/4096).                      (3.1)
```

On `D(c)`, divide the odd rows by `c` and write `Delta=p^2-4*r`.
The exact combinations in the charged hand elimination first give

```text
beta=5*Delta/8,
gamma=(15*Delta^2+40*p*c^2)/128.                  (3.2)
```

The remaining odd rows then reduce to

```text
F5=5*Delta^3+40*p*Delta*c^2+24*c^4,
F7=-5*p*(3*Delta^3+24*p*Delta*c^2+8*c^4).         (3.3)
```

If `p` is nonzero, the indicated linear combination of (3.3) forces
`c^4=0`, a contradiction.  If `p=0`, `F5=0` and the sixth row reduce to

```text
F5=8*(3*c^4-40*r^3),       E6=-3840*r^4,           (3.4)
```

so first `r=0` and then `c=0`, again a contradiction.  Thus all points of
(2.1) have `c=0`.

On `c=0` there is the exact identity

```text
h4=-(p/2)*h2.                                      (3.5)
```

On `D(p)`, (3.5) forces `mu2=0`; the hostile-reviewed seven-zero-tail
theorem then gives exactly the square and Chebyshev/Pell components in
(2.2).  At `p=c=0`, the odd rows and `h4` vanish identically and the only
remaining conditions are

```text
E6=-256*r^2*(5*r^2+8*r*beta+16*gamma)=0,
E2=  64*r*(5*r^2+6*r*beta+8*gamma),                (3.6)
```

with `E2=1024*mu2`.  If `r=0`, this is the square limit with `mu2=0`.
If `r` is nonzero, (3.6) is equivalent to the affine component in (2.2).
This proves the set-theoretic classification.

The three component ideals are prime because each quotient eliminates its
displayed dependent coordinates and leaves a polynomial ring.  The exact-Q
Singular run independently computed `rad(I)`, computed their intersection,
reduced both ideals against one another to zero, and returned exactly three
minimal associated primes.  This proves (2.3) and provides a software check
of every coefficient used above.

## 4. New component and successor sentinel

Writing `t=5*r+4*beta`, the new component is rational:

```text
beta=(t-5*r)/4,
gamma=r*(5*r-2*t)/16,
mu2=r^2*t/32.                                      (4.1)
```

The charged hand derivation proves the generalized-Pell identity and

```text
h10=-r^4*(t-r)/512.                                (4.2)
```

Equation (4.2) is a successor-design sentinel only.  It is not a row in
(2.1), and this theorem does not claim that a source correction or terminal
receiver imposes it.

## 5. Scope firewall

This is a theorem about the affine seven-row Laurent receiver on the
`k10=1` exact-square chart.  It is not a literal total-Rees pullback and does
not cover `k10=0`, correction jets, target/deck compatibility, terminal
`[6,2]`, Taylor receivers, or the other square and discriminant charts.  It
does not construct or exclude a strict arc, close order two or `(8,12)`,
prove maximum twelve, or prove or disprove JC2.
