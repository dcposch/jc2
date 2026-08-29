# Desk attack: AS109 `deg_y Q=6` top-two-band face isolation

Act as an adversarial characteristic-zero / 109-adic algebra researcher.  The
task is a bounded discriminator, not a request to restate campaign history.

## Charged question

Let

```text
P=x-x^109+109*A,       Q=y+109*B
```

be a hypothetical exact polynomial map over `Z_109` with `det J(P,Q)=1`.
Promoted inputs force the first open target corner to satisfy

```text
n=deg_y Q=6,
m=deg_y P>=12,  3|m,
6|deg_x(q_6),
d=gcd(m,6) in {3,6},
p_m=alpha*h^(m/d), q_6=beta*h^(6/d),
d=3 => 3|deg_x(h),   d=6 => 6|deg_x(h).
```

Because the seed has no positive `y`-degree in `P` and only degree one in
`Q`, all top coefficients in this corner come from `109*A,109*B`.

Fable5 proposed extracting the top two `y`-degree bands of the exact
Jacobian-one identity and doing 109-adic/Kummer-carry bookkeeping, with a
hard stop after two bands.  Determine whether this yields any new exact
constraint beyond the promoted common-core/divisibility conditions.

## Required work

1. Rehash and read in full these load-bearing files before reasoning:

```text
xmodel/as109-one-sided-prime4-composition-sol-20260827.md
xmodel/as109-one-sided-prime4-composition-hostile-review-grok-20260827.md
xmodel/as109-partial-y-history-stop-20260824.md
xmodel/as109-partial-y-history-review-grok-20260824.md
xmodel/ideation-20260827T0935Z-fable5.md                 (Card F3 only)
xmodel/ideation-20260827T0935Z-grok-crossreview.md      (§7.2/Card 4 only)
```

2. Search the AS109 history for an already-derived general `(m,6)` top-band
   equation.  Distinguish genuine novelty from the earlier `(6,9)`, `(4,6)`,
   `(5,6)`, and bounded-`y<=6` analyses.
3. Write

```text
P=sum_(i=0)^m p_i(x)y^i,  Q=sum_(j=0)^6 q_j(x)y^j
```

and derive coefficientwise, from scratch, the `y^(m+5)` and `y^(m+4)`
rows of `P_x Q_y-P_y Q_x`.  Substitute the common-core form for `p_m,q_6`.
Do not assume monicity, nonconstant `h`, or equality of 109-adic contents.
Handle zero next coefficients explicitly.
4. Use the AS109 congruence to track exact scalar-content lower bounds of
   every term.  Test reductions modulo `109`, `109^2`, and the first modulus
   at which a non-tautological normalized relation can survive.  Division by
   109 is allowed only after proving every coefficient is divisible by it;
   division by `h`, `alpha`, or `beta` requires an explicitly named ring or
   localization and cannot be used for an integral conclusion without
   descent.
5. Attack the strongest candidate relation with:
   - the exact `(12,6)` determinant-one automorphism control
     `u=x+y, v=y+u^6, (P,Q)=(u+v^2,v)` (not AS109, scope control);
   - a common-power zero-Jacobian family matching the relevant `(m,6)` top
     degrees whenever one exists;
   - constant-leading `h`, `d=3`, and `d=6` cases;
   - unequal 109-adic contents of `alpha,beta,p_(m-1),q_5`;
   - the seed-specific lower coefficients, to decide whether they enter either
     charged band at all.
6. Return exactly one of:
   - `NEW_CONSTRAINT`, with a fully proved integral statement and the smallest
     exact finite replay needed to promote it;
   - `TWO_BANDS_TAUTOLOGICAL`, with explicit equations/controls proving why
     no constraint is available and a precise stop under Card F3;
   - `REPAIR_DESIGN`, with the smallest missing datum needed before the two
     bands can be interpreted.
7. If the two bands are null, decide whether the already-proposed W2/W3
   gauge-conductor is genuinely the next independent object or is itself a
   history duplicate of the reviewed bounded-polar/wild-symplectic gates.
Give one executable successor only if it changes the unrestricted exact-lift
state in both outcomes.

## Scope and resource rules

- This is desk-scale exact algebra.  You may use a throwaway `/tmp` script
  with stock Python exact arithmetic for checks, but no heavy CAS, Singular,
  AWS, or web access.
- Treat finite-field arithmetic as a check only, never as a characteristic-
  zero proof.
- Do not infer existence or nonexistence of an AS109 lift from a finite band
  unless the proof actually establishes it.
- Do not edit canonical ledgers or any producer artifact.  Do not enter,
  read, build, status-inspect, or modify `jc2-lean`.
- Write exactly one file:
  `xmodel/as109-n6-top-two-y-bands-face-isolation-grok-20260827.md`.

The report must include exact equations, history checksum, controls, strongest
surviving conclusion, and a launch/stop recommendation.
