# Analytic certificate: cutoff-five characteristic core becomes unit after `v^2`

Date: 2026-08-28  
Producer: Sol Ultra, independent characteristic-mode lane  
Status: `EXACT CONDITIONAL CERTIFICATE; AWAITING LITERAL-SOURCE v^2 PROVENANCE`

## Charged statement

Work over a characteristic-zero field in the fixed branch-P square-baseline
cutoff-five specialization.  This report consumes only the licensed
field-radical parameterizations through `D14` and the three exact scalar
compatibilities in the frozen cutoff-five packet.  Put

```text
a = p32  = G15[X^1],
b = p139 = F7[X^0],
c = p86  = G11[X^0],
d = p91  = F11[X^1],
e = p120,
v = V0,
r = R0.
```

The literal endpoint and carrier relation are

```text
E0 = 1 + a*b - c*d,
Ec = c - (3/16)*v*(v+4*r).
```

The cumulative `D13`--`D15` scalar core is

```text
E15 = e*b - (3/4)*b^2 - (1/8)*v^3,
E13 = e*v - (3/4)*b*v + (3/2)*b*r - (3/8)*r^2,
E14 = e*r + (3/4)*b^2 - (3/2)*b*r + (3/16)*r^2.
```

Let `Ev=v^2`.  Then

```text
(E0,Ec,E13,E14,E15,Ev) = (1).
```

Thus, once a literal-source row combination proves `v^2=0` after the same
progressive substitutions, the necessary cutoff-five endpoint system is
empty.  No division, carrier normalization, branch choice, Groebner basis,
or algebraically closed-field argument is used in this final step.

## Exact identity

First, direct expansion gives

```text
3*b^3
 = 2*b*E13 + 4*b*E14 - (4*r+2*v)*E15
   - v*(v/4+r/2)*Ev.                                  (1)
```

Define

```text
q = (3/16)*v*(v+4*r).
```

Then a second direct expansion gives

```text
c^2 = (c+q)*Ec + (9/256)*(v+4*r)^2*Ev.                (2)
```

Finally put `x=a*b-c*d`.  The fourth power splits without any remainder as

```text
x^4
 = (a^4*b - 4*a^3*c*d)*b^3
   + (6*a^2*b^2*d^2 - 4*a*b*c*d^3 + c^2*d^4)*c^2.    (3)
```

The geometric identity

```text
(1-x+x^2-x^3)*E0 = 1-x^4                              (4)
```

together with (1)--(3) is an explicit polynomial unit certificate.  More
literally, substitute the right side of (1), divided by `3`, for `b^3` in
(3), substitute the right side of (2) for `c^2`, and add the result to the
left side of (4).  The outcome is exactly `1` as a polynomial over `Q`.

This also supplies a short field-only reading: `Ev=0` gives `v=0`; (1)
then gives `b=0`; `Ec=0` gives `c=0`; and `E0=0` becomes `1=0`.

## Status of the `v^2` target and the weight-eight gauge

`Ev=v^2` is the smallest sufficient next target, but it is not derived in
this report.  In particular, a naive continuation of the oriented rational
square root of `F` past weight seven is invalid because it misses an exact
gauge direction.

The raw coordinate

```text
p129 = F8[X^0]
```

occurs in none of the determinant generators `D10,...,D22`.  This is not a
compiler accident.  For an arbitrary scalar `mu`, the change

```text
delta F = mu*t^8
```

satisfies

```text
(delta F)_X = 0,
(t*d/dt-8)(delta F) = 0,
```

so it leaves the full determinant recurrence unchanged.  If one writes the
oriented rational square root as

```text
S = H + t/2 + (V/2)t^5 + (R/2)t^6 + ...,
F = S^2,
```

then this free constant changes the weight-eight coefficient of `S` by a
term proportional to `mu/H`.  Its denominators propagate into later square-
root coefficients.  Consequently, the degree windows of `F9` and `F10`
alone do not prove that those later square-root coefficients are polynomial,
and they do not by themselves yield `V0^2=0`.

Any repaired characteristic-mode argument must first quotient or explicitly
track this gauge—for example by proving a statement about
`F8-Q/2` modulo the free constant line—and must then reconstruct `v^2` from
literal source rows.  Until such a witness is frozen, `Ev` remains an open
conditional input to the exact unit identity above.  No heuristic
square-root continuation is claimed.

## Independent source checks

The authoritative raw system has SHA-256

```text
ead2fa404a741c5bc55934de6a1651d417701422f4b5311e3de7e3dccca0e5a0
```

and the raw-slot inventory has SHA-256

```text
28b9b05c02224aadec30d52b66ed22db80aabe416ffdc0186f6931f1978f1876.
```

In the independently recompiled cutoff-five source, the four raw maps are
literally

```text
g_1_0 -> p32,   f_0_1 -> p139,
g_0_1 -> p86,   f_1_0 -> p91,
```

and the unique `D22[X^0]-1` generator is

```text
-1-p32*p139+p86*p91.
```

This agrees with `E0=1+a*b-c*d` and fixes all endpoint signs.

## Scope firewall

The identity above is unconditional algebra in its six displayed
generators, but application to the raw determinant system remains
conditional on a tracked literal-source proof of `v^2` after the licensed
progressive substitutions.  Moreover, the substitutions through `D14` use
field-radical squarefreeness steps.  Even after the missing witness is
confirmed, the promoted conclusion is only emptiness of characteristic-zero
field-valued points in the fixed cutoff-five square-tail specialization.
It is not a unit certificate for the upstream nonreduced raw ideal, does not
cover the full branch-P family or another GGV branch, and makes no Keller-pair,
counterexample, or JC2 claim.  `D23` is not imposed and `G22` is absent.
