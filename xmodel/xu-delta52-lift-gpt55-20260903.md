# Xu delta=5/2 lift for `(99,66)`

`TYPE`: `LOCAL-NECESSARY-LIFT / COUNTING-BOUND`, not a full Keller-pair
construction and not an exclusion of Xu's open case.

## Mechanical inputs

I generated `/tmp/xu52-manifest.sha256` mechanically from
`xmodel/xu-delta52-lift-gpt55-20260903.run.v2`, using the
`charged_input_<i>_sha256=` and `charged_input_<i>_basename=` lines, and ran
`sha256sum -c`.  All eight frozen inputs in `/tmp/jc2-lane.jkejDP/inputs` were
`OK`.  A first attempt to write the manifest inside the read-only input
directory failed with a filesystem error only; it was not a hash mismatch.

Lane-local source page artifacts:

```text
box/xu52-20260903/source-pages/xu-pdfpage-10.png
box/xu52-20260903/source-pages/xu-pdfpage-11.png
box/xu52-20260903/source-pages/xu-pdfpage-12.png
box/xu52-20260903/source-pages/xu-pdfpage-13.png
box/xu52-20260903/source-pages/xu-pp10-13-layout.txt
box/xu52-20260903/source-pages/moh-pp196-199-pdfpage-57.png ... -60.png
box/xu52-20260903/source-pages/moh-pp196-199-layout.txt
box/xu52-20260903/source-pages/moh-pp207-209-pdfpage-68.png ... -70.png
box/xu52-20260903/source-pages/moh-pp207-209-layout.txt
```

## Source read

Xu Section 7.2 states the ODE lemma used later: if
`deg p=m`, `deg q=(l-1)m+1`, and the determinant expression
`D(m,m(l-1),p,q)=c p^l` holds with `c != 0`, then
`q=(c/m)(pi-a)p^(l-1)` for some `a`; see
`box/xu52-20260903/source-pages/xu-pp10-13-layout.txt:14`.

Xu Section 7.3 then introduces effective quasi-approximate roots
`T_i(f,g) in K[f,g]`, with `T_0=g`, `T_1=f`, and `deg T_i=-mu_i`;
for a principal-minor multiplicity `m u_s/d_s`, the corresponding
multiplicities for `T_0,...,T_{s-1},T_s` are
`(-mu_0)u_s/d_s,...,(-mu_{s-1})u_s/d_s,(-mu_s-2)u_s/d_s+1`
(`xu-pp10-13-layout.txt:21`).  Equation (7.1) is the Jacobian equation

```text
partial(T_s(sigma),g(sigma))/partial(t,pi)
  = -J*(T_s)_f(sigma)*t^(-2+delta).
```

The displayed source is `xu-pp10-13-layout.txt:131`.

For `(99,66)`, Xu quotes Moh p.209 and says Moh's treatment needs three
claims: no principal-minor split except at order `delta=2`, no three-root
case at `delta=2`, and no further split before final inside the double packet
(`xu-pp10-13-layout.txt:148`).  Xu says he proves the second and third, but
leaves one exception to the first open.  The two tools he explicitly uses are:
the denominator bound `den(delta) <= u_s = 3`, and equation (7.1)
(`xu-pp10-13-layout.txt:163`).

The numerical data are exactly:

```text
n=99, m=66, M2=77, M3=97, V3=8, V2=8,
delta2=1/3, delta1=4/9, -mu2=55, -mu3=145.
```

With `sigma` a principal-minor `pi`-root of order `delta`, Xu displays
(`xu-pp10-13-layout.txt:169`):

```text
f(sigma)       = p(pi)^6  t^( 6(-8+3delta)) + ...
g(sigma)       = p(pi)^9  t^( 9(-8+3delta)) + ...
T2(sigma)      = p(pi)^5  t^( 5(-8+3delta)) + ...
(T3)_f(sigma)  = p(pi)^22 t^(22(-8+3delta)) + ...
T3(sigma)      = q(pi)    t^(13(-8+3delta)-1+delta) + ...
deg p=3, deg q=40.
```

At `delta=5/2`, the last exponent is `-5`, not `-23/2`:
`13(-8+15/2)-1+5/2 = -5`.  The prompt's `q t^{-23/2}` line is therefore an
arithmetic slip; the reduced equation and Xu's display both use the `t^-5`
branch.

For the non-exceptional split orders `delta != 2,5/2`, Xu says equation (7.1)
forces `q=p^13(pi-c)` and then cannot hold (`xu-pp10-13-layout.txt:179`).
For `delta=2`, he prints the two-root identity (8.2) and says it produces
Moh's two-root split case (`xu-pp10-13-layout.txt:183`).  For `delta=5/2`,
he derives

```text
q(pi)=p(pi)^10 q1(pi),       deg q1=10,
partial(q1(pi), p(pi)t^(-1/2))/partial(t,pi)
  = -p(pi)^4 t^(-3/2).
```

He then says this can hold for any `p`, with
`q1=-2 integral p(pi)^3 dpi`, and so possible
`p(pi)=pi(pi^2-c)`; "Thus this case is open and it suggests case (99,66) is
open" (`xu-pp10-13-layout.txt:188`, checked against
`source-pages/xu-pdfpage-13.png`).  Here "open" means Xu did not impose the
full original-coordinate coefficient equations, the complete `J(f,g)=1`
system beyond the displayed leading ODE, or a recomposed polynomial pair.

Moh pp.196--199 supply the inversion/descent context for minor discs:
Proposition 6.3 is stated on printed p.197 and uses a minor-disc logarithmic
radius hypothesis; Proposition 6.4 on printed p.199 is the special `u_s=1`
descent.  The `(99,66)` row has `u_3=3`, so this automatic descent is not the
one used for the open `delta=5/2` split.  Moh Appendix II pp.207--209 gives the
coefficient-count motivation and the radius-two branch.  Printed p.209 shows
the unique radius-two root

```text
sigma = a_-1 t^-1 + a_0 + a_1 t + pi t^2,
g(sigma)=g_sigma(pi)t^-18 + ...
```

and the second possibility transform
`x -> x^-1, y -> a0+a1*x+a2*x^2+y*x^3`, with leading terms
`Omega(f)=x^6 y^18+...`, `Omega(g)=x^9 y^27+...`,
`Omega(T2^psi)=x^5 y^15+...`, `Omega(T3^psi)=x^15 y^40+...`, and
`J(Omega(f),Omega(g))=x`.  This was read from
`source-pages/moh-pp207-209-pdfpage-70.png`; the layout text drops parts of
the display.

## Symbolic verification of Xu's `q1`

With `p=pi(pi^2-c)`,

```text
q1 = -2 integral p^3 dpi
   = -pi^10/5 + (3c/4)pi^8 - c^2 pi^6 + (c^3/2)pi^4
```

after setting the integration constant to zero.  The constant is invisible to
the reduced derivative equation; this lane normalizes it away.

The driver checks

```text
D_s(q1, p/s) + 2*s^2*(p/s)^4 = 0,       s^2=t,
```

which is equivalent to Xu's displayed
`partial(q1,p t^-1/2)/partial(t,pi)=-p^4 t^-3/2`.  It also checks
`q1' + 2p^3 = 0`.  Result: `PASS`.

Driver: `box/xu52-20260903/scripts/xu52_reduced_lift.py`.
Result JSON: `box/xu52-20260903/results/xu52_reduced_lift.json`.

## Next-level setup

In original monic source coordinates, with `x=t^-1`, the `delta=5/2`
principal-minor expansion has the form

```text
sigma = a_-1 t^-1 + a_0 + a_1 t + a_2 t^2 + pi t^(5/2).
```

The tower fixes the principal minor direction and multiplicity data.  After a
linear normalization of the two top directions, the degree-11 common
approximate-root leader has top form `Y^3(Y-kappa X)^8`; the chosen minor line
is the multiplicity-3 direction.  The data force the face multiplicities

```text
g: 27,   f: 18,   T2: 15,   (T3)_f: 66,
```

and the displayed powers `p^9,p^6,p^5,p^22`.  They do not determine
`a_0,a_1,a_2`, nor the full lower coefficients of `f,g,T2,T3`.  A fail-closed
original-coordinate system would need the coefficient arrays for

```text
h = y^11 + lower terms,       h(sigma)=p t^-1/2 + ...
f = h^6 + sum_{i=1}^6 alpha_i h^(6-i),
g = h^9 + sum_{i=2}^9 beta_i h^(9-i),
T2 = h^5 + lower h-adic terms,
T3 with local quotient T3/h^10 = q1 + ...
```

plus the effective quasi-approximate-root recurrences in `K[f,g]` and the
original `J(f,g)=1` equations.  Xu does not print those equations.

For the bounded prolongation I used the straightened local chart

```text
s^2=t,        x=s^-2,        y=pi*s^5,
h = p/s + A0(pi) + A1(pi)s + A2(pi)s^2 + ...
Q = q1(pi) + B1(pi)s + B2(pi)s^2 + ...
```

and imposed

```text
D_s(Q,h)+2*s^2*h^4 = 0.
```

The `h` supports are not arbitrary: a monomial `x^i y^j` of a degree-11
polynomial contributes to `[s^r]h` only when `5j-2i=r` and `i+j<=11`.
Through the computed orders this gives

```text
r=0: pi^0,pi^2
r=1: pi^1,pi^3
r=2: pi^2
r=3: pi^1,pi^3
r=4: pi^2
r=5: pi^1,pi^3
```

The `Q` coefficients were allowed up to degree 18 at each new order.  This is
a local necessary/superset computation: inconsistency would be meaningful, but
consistency is only a counting bound because it does not enforce the full
`T3 in K[f,g]` bridge or all original polynomiality correlations.

The first two omitted equations can be written compactly before solving.  Put
`p=pi(pi^2-c)`, `h=p/s+A0+A1*s+...`, and `Q=q1+B1*s+B2*s^2+...`.  The
coefficient of `s^-1` in `D_s(Q,h)+2*s^2*h^4` is

```text
(p B1)' + 8 p^3 A0 = 0.
```

With the degree-11 straightened `h` support, `A0=u0+u2*pi^2`.  Polynomiality of
`B1` forces `u0=-(c/3)u2`; in the driver's free-parameter coordinate this is

```text
A0 = (b1_9*c)/2 - (3*b1_9/2) pi^2.
```

The coefficient of `s^0` is

```text
p B2' + 2p' B2 + 10p^3 A1 + 12p^2 A0^2 + B1 A0' = 0.
```

The straightened support gives `A1=v1*pi+v3*pi^3`.  After substituting the
first-order solution, the exact solve leaves one new free parameter `b2_8`:

```text
A1 = ((3*b1_9^2 - 2*b2_8)/10) pi
   + (2*(9*b1_9^2 + 4*b2_8)/(15*c)) pi^3.
```

Thus the requested next two omitted orders are not merely "not contradicted";
they have an explicit localized polynomial solution branch over `Q[c,c^-1]`.

## Computation

Wrapper controls in `Q[c,T]` passed:

```text
ideal(c,T*c-1)       -> unit ideal
ideal(c-1,T*c-1)     -> non-unit ideal
```

Controls reproducing Xu's exclusions:

* `delta=2`, `[1,1,1]`: equation
  `2p q' - 25p' q = k p^14`.  Since `c != 0`, `p=pi(pi^2-c)` is squarefree.
  At each simple root of `p`, if `q` has multiplicity `r`, the left side has
  multiplicity `r` because `2r-25 != 0`; the right side has multiplicity 14.
  Thus `r=14` at all three roots, so `deg q>=42`, contradicting Xu's
  `deg q=40`.  Verdict: `EXCLUDED`.
* `delta=7/3`: after Xu's non-exceptional reduction
  `q=p^13(pi-d)`, the reduced polynomial is
  `k*c*pi - k*pi^3 + 12*c*d - 21*c*pi - 36*d*pi^2 + 45*pi^3`.
  Saturating by `c != 0` with `T*c-1` gives Groebner basis `[1]`.
  Verdict: `EXCLUDED`.

The `delta=5/2` local lift stayed consistent through `s^4`, i.e. through six
coefficient levels including the leading `s^-2` reduced equation and the
omitted levels `s^-1,s^0,s^1,s^2,s^3,s^4`.  The requested "next two orders"
are `s^-1` and `s^0`; both are consistent.

The order records from `xu52_reduced_lift.json` are:

```text
s^-1: 21 equations, 21 new variables, 20 solved, free b1_9
      a0_0 = b1_9*c/2
      a0_2 = -3*b1_9/2
s^0 : 21 equations, 21 new variables, 20 solved, free b2_8
      a1_1 = (3*b1_9^2 - 2*b2_8)/10
      a1_3 = 2*(9*b1_9^2 + 4*b2_8)/(15*c)
s^1 : 21 equations, 20 new variables, 20 solved, no new free parameter
      a2_2 = -b1_9*(3*b1_9^2 + b2_8)/(2*c)
s^2 : 21 equations, 21 new variables, 20 solved, free b4_8
s^3 : 21 equations, 20 new variables, 20 solved, no new free parameter
s^4 : 21 equations, 21 new variables, 20 solved, free b6_8
```

Every emitted coefficient was rechecked symbolically after substitution.
Denominators are rational constants and powers of `c`; the computation is on
the localized component `c != 0`.

Dimension count:

```text
through next two orders s^-1,s^0:  c plus b1_9,b2_8  -> dimension 3 localized
through s^4:                       c plus b1_9,b2_8,b4_8,b6_8
                                  -> dimension 5 localized
after the slice c=1:               dimension 4 through s^4
```

This count excludes the normalized-away additive constant in `q1`.

## K=16 preprocessing note

The charged `triangular_preprocess.py` was read for method and controls.  I did
not run it as evidence for the `(99,66)` `delta=5/2` branch: its declared ring
and tuple are the K=16 charts
`(12t+4,8t+4;12t+1,3)` with `Phi=(-1,t/(3t+1))`, not Xu's `(99,66)` system.
Using it directly here would violate the variable/ring-map guardrail in
`FALLACY-v2.md`.  The local driver instead copies the relevant safeguards:
declared ring, Rabinowitsch localization, positive/negative wrapper controls,
and explicit symbolic rechecks.

## Verdict

`SURVIVES[DELTA-5/2-REDUCED-LOCAL-LIFT-THROUGH-s^4]`.

The next two orders that Xu did not impose are consistent after saturation by
`c != 0`; no certificate excludes the `delta=5/2` principal-minor split.  The
deepest computed local order is `s^4`, with localized family dimension 5
including `c`, or 4 after the `c=1` slice.

`OPEN[FULL-X-Y-KELLER-LIFT]`: this lane did not build the full
original-coordinate coefficient system for `f,g,T2,T3`, did not solve the
effective quasi-approximate-root recurrences in `K[f,g]`, and did not produce
a polynomial pair with direct `J(f,g)=1` and degrees `(99,66)`.  Therefore the
`delta=5/2` branch is not excluded, and `(99,66)` cannot be reduced to Moh's
`delta=2` branch B from the computations here.

Artifacts:

```text
box/xu52-20260903/scripts/xu52_reduced_lift.py
box/xu52-20260903/results/xu52_reduced_lift.json
box/xu52-20260903/logs/xu52_reduced_lift.out
box/xu52-20260903/results/artifacts.sha256
```

No exit-price assertion is made, so no `charge_basis=...` line is emitted.

<!-- BODY-END -->
