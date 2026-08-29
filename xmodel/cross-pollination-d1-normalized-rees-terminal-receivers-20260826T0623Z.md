# Cross-pollination: D1 as a normalized-Rees control and receiver test

Date: 2026-08-26 06:23Z

Status: **POST-BLIND SYNTHESIS; STRATEGY AND INTERFACE TEST ONLY.**

Named packets read after the blind phase closed:

```text
8f365717f5212d2891cdcacafa9befc7ee548169f2c3b5674806ea5af67099bb
  xmodel/ideation-20260826T0550Z-root-significant-news.md
daf28d30ce25f4f312ef2d78beb83a4e5604e44d749d5322ebb7e89d51cfcd59
  xmodel/ideation-20260826T0557Z-td6-owner-significant-news.md
878837c55d4b013797019109253b40d88b74de77187319e9835245834240eb4e
  xmodel/ideation-20260826T0615Z-order2-owner-significant-news.md
```

## Finding 1: D1 is a good small toric control, but not yet a full-source control

The V10 atlas is the expected normalized weighted blowup of the two-variable
monomial filtration `wt(a)=1`, `wt(h)=3`.  At the level of the degree-three
monomial ideal

```text
J=(a^3,h) in L[a,h],
```

the two ordinary blowup charts are

```text
h=a^3*s,                    a-chart,
a^3=h*q,                    h-chart,
s*q=1                       on the overlap.
```

V10's displayed h-chart

```text
h=theta^3,  a=theta*b
```

is the finite Kummer cover of the second chart, with `q=b^3` and
`s=b^(-3)`.  Thus a normalized-Rees tool should recover the ray `(1,3)`,
the two invariant charts, and their Cech overlap.  It need not literally
emit the Kummer cover; the correct comparison is the invariant quotient of
that cover.

This makes D1 a genuine **toric atlas-generation positive control** after a
small normalization/universal-property certificate is added.  V10 alone is
not yet a positive control for normalization of the complete six-normal
strict-Rees source: it starts after the V8 witness cone and the `(a,h)`
coordinate action have been selected.  In particular it cannot certify that
every double-root normal valuation lands in V8.  That missing normal-fan
exhaustion must not be hidden inside the software regression label.

## Finding 2: receiver composition is typed, not automatic

Inside D1, the terminal coordinate is already source-compatible with the
ordinary chart:

```text
r8=t_base,  t_base=1+tau,
gamma_8=1+tau,
row 8 target=Lambda^20*(1+tau).
```

So the cyclic-D1 terminal fixture is carried into the local Rees equations;
it is not an independent constraint waiting to be appended after V10/V11.
The global passport statement and the Taylor-polynomiality receiver do not
follow from that local identity.  V8--V11 neither prove global landing nor
pull the complete Taylor ideal through the weighted atlas.

Across order two, order one, D1, and TD6, only the interface pattern
composes:

```text
source component
 -> normalized Rees charts with a Cech certificate
 -> pullback of that source's own terminal/Taylor/passport equations
 -> overlap equality and boundary-divisor audit.
```

The receiver theorem itself does not transfer between degrees.  Order two
must retain terminal `[6,2]` and its two Taylor families; order one must
retain its `r7` two-branch/pure-power map; D1 retains `r8=t_base` and the D1
passport.  TD6 needs its own source-typed receiver.  A common compiler may
carry these objects, but no cross-program algebraic implication is licensed.

## Cheapest discriminator

Before running the normalized-Rees engine on the order-two component
intersection or the TD6 maximal-minor ideal, run one bounded dual-AWS D1
control on `J=(a^3,h)`:

1. emit a semigroup/normalization certificate for the single exceptional
   ray `(1,3)`;
2. emit the two invariant charts above and prove their overlap by two-sided
   ring maps;
3. compare the second chart with the `mu_3`-invariant quotient of
   `h=theta^3,a=theta*b`;
4. pull back only the typed D1 terminal target
   `Lambda^20*(1+tau)` and the discriminant
   `-27*h*(4*a^3+h)` through both charts, and require dictionary equality on
   the overlap.

This is the cheapest experiment because it separates three failure modes
without reconstructing the eight tails:

- wrong fan or an extra ray: normalization/filtration bug;
- correct fan but failed invariant quotient or overlap: chart/Cech bug;
- correct atlas but failed terminal/discriminant pullback: receiver-typing
  bug.

A complete pass licenses D1 as a small normalized-Rees **software** positive
control.  It still does not supply the missing theorem that the full D1
six-normal double-root fan lies in V8, and it gives no order-two, TD6,
global-D1, or JC2 verdict.
