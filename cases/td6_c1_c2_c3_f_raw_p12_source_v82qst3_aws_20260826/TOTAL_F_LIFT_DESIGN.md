# Successor design: propagation-qualified total-`F` lift

Date: 2026-08-26

Status: design only; not a launched or proved identity.

## Why V82QST2 cannot be lifted as-is

V82QST2 substitutes `F=0` before source construction and then solves FIRST,
PREVIOUS/POLE, and CURRENT through rational affine parameterizations.  Its
`('X0',12)` contradiction has coefficient one only among the already-composed
CURRENT rows.  The emitted source combination does not unwind FIRST,
PREVIOUS/POLE, or transport, and its common chart denominator contains
unregistered divisors.  There is consequently no object in that endpoint to
divide by `F` and no proof that `F` was not inverted in a total family.

V82QST3 is intended to repair the first issue on the fixed A3 special fibre:
it uses genuine P12 and packed FIRST rows and clears only registered factors.
It still freezes the transverse source parameters, so it is not the total
family required by the valuative-propagation interface.

## Required total-family ring

Introduce a literal independent parameter `t` and construct the center as

```text
C0=(V^2-U^3+t)/U,
```

so the raw identity is `F=t`.  Work over a polynomial coefficient ring in
`t,U,V` and every transverse coordinate licensed by the chosen total chart;
do not use a fraction field in `t`.  The complete chart contract must name
which q, dead-stretch, correction, pole, and boundary coordinates are retained
and which are proved gauges.  A square-zero 33-axis tangent object is not a
nonlinear total chart.

The registered multiplicative set `S` may contain only the total lifts of
the named chart units.  It must not contain `t`, an unregistered pivot minor,
or a factor introduced by an echelon choice.

If the total TD6 chart is obtained by a blowup or ordered divisor routing,
form the actual total Rees algebra before setting `t=0`.  A blowup of the
already-specialized ring need not be its special fibre because `t`-torsion
can be lost.  Likewise, a naive symmetric-algebra chart is insufficient when
the selected generator can be a zero divisor: use the Rees kernel, or a
separately proved saturation/presentation, and audit `t`-torsion explicitly.
This is the base-change firewall of
`xmodel/cross-iterated-blowup-cech-valuative-propagation-20260826.md`.

## Exact construction

1. Build the complete unsolved raw source rows `f_i(t)` in this ring.  If the
   existing transport compiler is used for acceleration, carry an exact DAG
   back to these rows; post-transport rows alone are not the theorem source.
2. Specialize the complete rows at `t=0` and obtain on each registered chart
   a cleared certificate

   ```text
   s = sum_i a_i*f_i(0),  with s in S.
   ```

3. Lift each `a_i` coefficientwise to the total ring and compute

   ```text
   R = s - sum_i a_i*f_i(t).
   ```

   After one common clearing by an element of `S`, assert coefficientwise
   exact divisibility `R=t*h`; emit the quotient `h` and replay

   ```text
   s = sum_i a_i*f_i(t) + t*h.
   ```

4. Audit every denominator in `a_i,h` termwise against `S`, prove `t` is not
   inverted, and include an omitted-source-row negative control.
5. If more than one source/normalization chart is needed, emit the finite
   cover, overlap identities, and routing of every zero section before any
   positive-valuation conclusion.
6. For every Rees/blowup presentation, verify that specialization of the
   total chart is literally the frozen special chart; record the kernel or
   saturation identity and a `t`-torsion negative control.

## Fast fail conditions

The successor fails closed if the V82QST3 special certificate has an outside
factor; if a total source row cannot be traced through transport; if `R` is
not exactly divisible by `t`; if `h` gains a `t` pole or an unregistered
factor; if any transverse coordinate was silently set to zero; or if the
principal opens do not cover the special fibre.

Only after these checks does the identity satisfy the contract in
`xmodel/cross-empty-special-fibre-valuative-propagation-20260826.md`.  Until
then no positive-`F` valuation arc, TD6, SP-2, or JC2 conclusion is licensed.
