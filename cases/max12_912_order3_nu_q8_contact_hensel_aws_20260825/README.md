# Corrected-Q8 factorwise source Hensel lift

This AWS-only producer lifts the full eight-equation localized source at
`w=0` over each irreducible factor of `Q8bar`:

```text
three rational contacts and one degree-five Frobenius orbit.
```

It uses the frozen corrected contact coordinates and full `8x8` unit
Jacobian, Newton-doubles all eight source variables, and then measures the
order of `H(w,v(w))` on the unique formal source branch.  It never imposes
`H=0`; therefore a high vanishing order is genuine source/plane contact.

The order-256 run is a scaling/control gate.  Any escalation is AWS-only.  A
finite-order zero is not an identity; the residual cycle bound separately
determines which finite order is enough to force an H-supported contact.
