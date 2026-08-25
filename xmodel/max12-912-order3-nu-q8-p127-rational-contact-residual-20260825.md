# Selected-Q8 rational-contact residual obstruction over `F_127`

Date: 2026-08-25  
Status: **PRODUCER-EXACT CONTACT COMPUTATION; COMPOSED CLAIM PROVISIONAL
PENDING BIDEGREE REVIEW**

## 1. Exact conditional conclusion

Consume the reviewed theorem that the selected localized mod-127 source has
at least one component whose projected image is the geometrically integral
curve `H`, and the producer bidegree theorem that the complementary non-`H`
projected cycle `R` satisfies

```text
I(H,R) <= 35,582.                                      (1)
```

Then at least one of the three **rational** corrected-Q8 contacts

```text
(w,v)=(0,26), (0,58), (0,67)                           (2)
```

lies on an `H`-supported source component.

The two order-16384 AWS endpoints and the order-8192 dependency are exact and
frozen.  The composition with (1) is provisional until the bidegree report is
hostile-reviewed.

## 2. Distinct-contact provenance

The frozen full-contact algebra gives the squarefree factorization

```text
Q8bar(v)=(v+101)(v+69)(v+60)
          *(v^5+53v^4+38v^3+26v^2+118v+79)
```

over `F_127`.  The three displayed linear factors have the distinct roots
`26,58,67`.  Thus (2) consists of three different plane points; no repeated
root, residue-field conjugacy, or one-point multiplicity is being counted
three times.

At every corrected-Q8 contact, the same full divided localized source has
relative `8 x 8` Jacobian a unit.  Hence each point has one reduced formal
source branch, with `w` a local parameter, and the localizer remains a unit.

## 3. Exact contact orders

For a chosen rational factor, the AWS generator works in

```text
F_127[s]/(s^N),       s=w,
```

starts at the frozen full-contact section, and Newton-lifts all eight internal
coordinates against the same eight source equations.  The final gate
rebuilds all eight equations and evaluates the pinned plane polynomial `H`.

The accepted endpoints are:

```text
root  factor       N       final_fail   H contact
 67   linear67    16384        0        at least 16384
 58   linear58    16384        0        at least 16384
 26   linear26     8192        0        at least 8192.
```

Every lane also reports `base_fail=0`, unit contact Jacobian, and rc-zero
fail-closed metadata.  The two earlier 64-GiB order-16384 attempts ended in
explicit memory failures and are not consumed.  Two 384-GiB mirrors were
terminated as redundant only after both V5 endpoints passed; they are not
consumed either.

## 4. Additivity and contradiction

Suppose none of the three branches in (2) is `H`-supported.  By the unique
local-branch calculation, each then lies on the non-`H` residual source cycle
and its image contributes the displayed finite valuation of `H` to the local
intersection with `R`.  Projection-formula multiplicities are positive, so
the displayed valuation is a lower bound even if the source-to-image map has
additional multiplicity.

Local intersection numbers at distinct plane points add.  Therefore

```text
I(H,R) >= 16384+16384+8192 = 40,960.                    (3)
```

But `40,960>35,582`, with strict margin `5,378`, contradicting (1).  Hence at
least one of these three branches is `H`-supported.

This argument proves only an existential disjunction.  It does not identify
which of `26,58,67` is selected and it says nothing about the separate
quintic orbit.

## 5. Custody

Portable case:

```text
cases/max12_912_order3_nu_q8_contact_hensel_order16384_aws_20260825/
```

Primary accepted outputs:

```text
linear67 stdout  4bff2931b472c831a17546b6f0f098a1bd4651e819f99591faf8810d978d5889
linear67 stderr  dc67e8bc1af59be0ed72571b0df13d90e3ac438785f95d8bbef1494f657f43bb
linear58 stdout  be897a19ca10b762badf0757fc48bf179463b13291523cc49138a07d0d3a6dbb
linear58 stderr  b10e1d77670eeb7e2934d8d518e17ece3661ea498991d7665ebe8794eef6d0a3
linear26 stdout  359cc2d3187037a741bbced81ac0bee211cea7012fdc10fd74ded84678d6a4be
```

`replay.py` independently checks the dependency hashes, Q8 factor product,
root distinctness, every accepted endpoint, negative-control classification,
and (3).

## 6. Scope firewall

The unconditional new evidence is the three exact finite contact lower
bounds.  The residual-component conclusion is conditional on the
review-pending bidegree bound (1).  Even after that review, the theorem says
only **at least one of these three rational contacts** is on an H-supported
mod-127 source component.

It does not prove which contact, all three, all eight, source degree one,
global coordinate regularity, characteristic-zero no-merger, Taylor
realization, terminal dynamics, a rational trajectory, a maximum-12
exclusion, or JC2.
