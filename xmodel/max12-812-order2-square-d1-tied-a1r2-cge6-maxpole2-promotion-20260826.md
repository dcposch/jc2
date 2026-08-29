# Promotion: D1 `(a,r)=(1,2)`, closed `c>=6` maximal-pole tail

Date: 2026-08-26

Status: **PROMOTED AFTER INDEPENDENT HOSTILE REVIEW CONFIRMED.**

## Promoted statement

After the frozen generic-square and D1 source gates, in characteristic zero
the complete seven literal Faber equations are empty on the closed unit-load
tail

```text
D(p*k0), ord(A)=1, ord(R)=2, ord(C)>=6.
```

At the decisive absolute grade 16 the complete polar source is exactly

```text
(5/32)k0*A^2/L, (5/16)k0*R^3/L,
-(3/8)R*A^2/L^2.
```

The `C` contact does not occur in this row: the first `C`-bearing polar
family is unloaded `A*C/L` at grade `11+c>=17`.  Raising `c` only delays
that family and cannot alter the grade-16 source, target timing, pole ceiling,
or cancellation.  No leading coefficient of `C` is inverted.

The `R*A^2/L^2` family is the unique pole-two term.  The reconstructed
negative tail is the canonical remainder modulo `L^2` of the fully cleared
numerator, with the ordinary quotient retained exactly.  The first root
Faber pair allocates the nonzero linear `A,R` forms.  Both same-root charts
are unit ideals.  On each opposite-root survivor, exact division by `L`
gives the deck terminals

```text
+(5/2)k0*lambda^3*bu^3, -(5/2)k0*lambda^3*bu^3,
```

and derivative-row units `5*k0*lambda^4*bu^3`.  At the nominated `A` root,
`A2` and divided `RA2` vanish; the nonzero `R3` terminal cannot cancel.
The four root-value charts exhaust the nonzero linear `A,R` pairs, the unit
ideals occur before radicals, and emptiness descends from the finite etale
root cover over `D(p)`.

## Immutable custody

```text
producer RESULT
6466b99a050d7fca6f3e8bc7333391046accd5521cf7c4aeb37f8b1554193a49

producer freeze
594514315e73d201a5d494e8de79076278aa8a25327dfbef38a71e5cb8b67cfc

producer evidence
56fd5a06baa161b833a27c18613102287c09a18c259915395888229edddae438

hostile review
365b07a6563e72ccdf64c62cb7d2425ed7876fa919e3b4ebb4f536fe131f1e5d
```

The producer ran exact `Q` plus independent `F_65519,F_65521` controls on
AWS, all rc 0 and zero swap.  It used ordinary polynomial rings, not a
Singular quotient ring.  The hostile reviewer rehashed the full custody,
independently enumerated the source, reconstructed both pole stages and both
deck terminals, audited all four charts, checked the closed-tail widening,
and returned `CONFIRMED`.

## Firewall

This promotion contains only `ord(A)=1`, `ord(R)=2`, `ord(C)>=6` on
`D(p*k0)`.  The adjacent exact contact `(1,5,2)` has its own separately
reviewed promotion.  This result does not cover `ord(C)<=5`, another
primary/tied face, positive-order leading load, `p=0`, `k0=0`, the
exact-square zero section, an excluded terminal/global chart, fan
exhaustiveness, order two, maximum twelve, or JC2.
