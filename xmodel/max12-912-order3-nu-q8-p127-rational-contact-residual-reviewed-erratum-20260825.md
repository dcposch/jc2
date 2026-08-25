# Selected-Q8 rational-contact residual obstruction: reviewed erratum

Date: 2026-08-25  
Status: **REVIEW-CLEARED MOD-127 EXISTENTIAL CONTACT THEOREM AT THE STATED SCOPE**

This nonmutating successor repairs the two defects identified by the hostile
Claude review of the frozen bidegree/contact package.  The frozen producer
reports and cases remain byte-immutable and are superseded only for the
numerical residual bound and the definition of the bounded cycle.

## Correct bounded cycle and bidegrees

Let `Z` be the full localized one-cycle of the six-row selected source: every
one-dimensional component not contained in

```text
x5*(x3-2*x5)=0.
```

This definition includes both the reviewed `H`-witness component and the
components through the three rational corrected-Q8 contacts, because the
localizer is a unit at all eight contacts.  Let the pushforward of `Z` to
`P1_w x P1_v` have class `(A,B)`.  The two exact origin-augmented affine-BKK
computations give

```text
A <= 176,     B <= 550.
```

The earlier affine generic-line value `658` bounds plane degree only.  It
does **not** give `A+B<=658`: every bihomogenized affine line has the fixed
base point `(infinity,infinity)`, and `H` itself passes through that point.
The old `35,582` bound and threshold `4,448` are therefore retired.

The reviewed component theorem supplies at least one `H` summand, of class
`(21,190)`.  Removing all `H`-supported summands leaves an effective residual
class `(a,b)` with

```text
a <= 155,     b <= 360.
```

Consequently the honest projective intersection bound is

```text
I(H,R) = 190*a+21*b <= 190*155+21*360 = 37,010.       (1)
```

No `A+B` constraint is used.  The corresponding single-contact threshold is
`37,011`; the equal eight-contact threshold is `4,627`.

## Reviewed existential conclusion

The frozen source-Hensel lanes give three distinct rational contact lower
bounds

```text
(0,67): 16,384,
(0,58): 16,384,
(0,26):  8,192,
total:  40,960.
```

At each point the full `8 x 8` relative Jacobian and localizer are units, so
there is one reduced source branch with parameter `w`; the final lane gate
substitutes that branch into all eight source equations and into the pinned
`H`.  If all three components were residual, their distinct local
intersection contributions would add to at least `40,960`.  This contradicts
(1), with strict margin

```text
40,960-37,010 = 3,950.
```

Therefore **at least one** of the three full contacts with `v=26,58,67` lies
on an `H`-supported mod-127 selected-source component.

## Review and custody

The hostile review verdict is `CONFIRMED_WITH_REPAIRS`:

```text
xmodel/max12-912-order3-nu-q8-p127-rational-contact-residual-review-claude-20260825.md
SHA256 658341959f39cdcad00e5f42d440af8bdb7fb2454b6676c96e6b00bddb10b562
```

It independently checked the two fibre bounds, `H` bidegree, three rational
Q8 factors, full source/Jacobian provenance, exact contact additivity,
negative-control classification, and all repaired arithmetic.  The
load-bearing vertical BKK value remains a single-run attestation, as the
review discloses; its source-only subset records agree bytewise with the
reviewed sparse pipeline.

## Firewall

This theorem is existential over exactly the three rational contacts.  It
does not identify which contact, include the quintic orbit, force all eight,
prove source degree one, or supply characteristic-zero specialization by
itself.  It makes no Taylor, terminal, trajectory, maximum-twelve, or JC2
claim.
