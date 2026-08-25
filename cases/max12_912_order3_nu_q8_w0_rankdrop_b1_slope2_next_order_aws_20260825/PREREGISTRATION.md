# Preregistration: b=1 selected slope-two next-order continuation

Date: 2026-08-25  
Scope: exact finite-jet routing only; never an arc-closure theorem.

Use exactly the pinned six-row source `(e1,e3,e5,e7,e2,e4)`.  Start from the
reviewed selected leading cone at `(d2,d4)=(2,1)` and normalize the unit
leading coefficient of `x5` by taking `x5=t`:

```text
c  = c + C1*t
d4 = 1 + B1*t
d2 = 2 + (B1+Q1)*t
x5 = t
x3 = (5/3)*t + X2*t^2
x1 = U2*t^2
w  = -(4/9)*t^2 + W3*t^3.
```

This retains first jets of `c`, `d4`, and the transverse difference
`u=d2-d4-1`; setting `x5=t` is licensed only for unramified branches with
`ord(x5)=1`.  Verify the leading coefficients vanish, then form the next
coefficient ideal from order two in the four odd rows and order three in the
two even rows.  Compute it by exact-Q `std/dp` and `slimgb/block`, print its
full basis, and eliminate all jet variables to `Q[c]`.

Acceptance is source regeneration, zero leading residuals, two exact engines,
rc zero, no diagnostic, and exact printed bases.  A unit next ideal excludes
only this normalized finite jet.  A nonunit ideal is a routing survivor.  A
nonzero `c` eliminant is only a necessary exceptional-value list at this jet
depth.  No finite jet excludes ramified/mixed-order arcs, coefficient drift at
earlier orders, the full selected saturation, Taylor/terminal realization,
general `(9,12)`, maximum twelve, or JC2.

