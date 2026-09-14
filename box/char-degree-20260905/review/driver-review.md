# Independent driver review

**Later update:** `normalized-review.md` audits the repaired normalized backend, the additional Proposition4.5 total-degree/top-form necessity, and the full-face nondegeneracy theorem. The serializer defect recorded below has been repaired in the subsequently inspected backend and its controls pass.

The `(99,66)` driver’s characteristic algebra, source premap, physical coefficient encoding, and y-degree extraction are correct in the versions inspected. The D108 four-division reduction is also algebraically correct. A concrete Singular serialization failure was found in the initial D108 emitter and reported immediately to its owner and the coordinator. The owner must repair and revalidate serialization before using any computation.

## `(99,66)` source map and full characteristic block

`g9966_driver_control.py/.json` checks every outer offset 0 through 7 (stage 8 uses offset 7). The premap sets `B1=-b/3` and `A2=(3*B2+a)/2`, using only rational leaders. Every surviving A2/B2 coefficient identity is rechecked in the actual source coordinate maps. All new source images lie in the declared remaining ring; no unbound symbols occurred.

The two identities follow in that order from the full degree condition. For monic `h` of y-degree 33 and outer coefficients of y-degree less than 33, the original expression has h^5 coefficient `3*B1+b`. Every other term has y-degree below 165 after isolating that term, so its coefficient polynomial must vanish. The resulting h^4 coefficient is `3*B2-2*A2+a`; every lower h term has y-degree below 132, so that coefficient vanishes too. Since the target is 55, both reductions are necessary. Neither selects a component or inverts a source variable.

The physical map `(r,q) -> x^(D-r-q)*(y-x)^q` is exactly inverse to the normalized coordinates `t=1/x,z=y/x-1`. Full normalized h3, C2, C3 and the surviving outer blocks are retained. In particular the full `h=h3^3+C2*h3+C3` has exact y-degree 33 and leader 1; the lower coefficient boxes cannot alter that leader.

The four displayed coefficients `L3,L2,L1,L0` in the initial driver agree identically over Q with the original family after these two substitutions. The independent test expands both sides and obtains zero. The extraction of every x coefficient of y-degree above 55, plus the positive-x parts of y55 and a free scalar target subtraction, is correct. The extra target constant e remains in the declared ring even though the degree/leader rows cannot see it.

The later H-adic method avoids forming h^2 and h^3. Dividing `L2=u2*h+v2`, `L1=u1*h+v1`, and `L0=(u00*h+v00)*h+v0` yields

`Q=(L3+u2)*h^3+(v2+u1+u00)*h^2+(v1+v00)*h+v0`.

Every displayed digit has y-degree below 33. Thus the first two digits vanish coefficientwise, and the h digit has exact y-degree 22 and scalar unit leader. This is equivalent to the original y-degree 55 condition. Monic division with y as the first lexicographic variable uses no source-variable denominators. Its coefficient operations are triangular with unit diagonal, so it gives an ideal-equivalent set of rows, not just a set-theoretic shortcut. The dense symbolic H-adic test in the control passes.

The source finite cap is copied from the corrected engine's finite schedule, while the characteristic block uses full physical source polynomials. There is no zero-padding of an omitted t143 coefficient. The driver correctly labels an exact nonunit ideal as `EXACT-Q-NONUNIT-NO-POINT`, and a unit as a candidate requiring independent gate replay.

## Depressed four-division reduction, both degrees

Write the original source pair after the first two reductions as

`F=h^3+(3D+a)*h/2+C`, `G=h^2-b*h/3+D`.

Set

`H=h-b/6`, `A=a+b^2/4`, `dd=d+b*c/2`,

`p=dd-A^2/3`, `q=e+c^2/4-A*dd/3+2*A^3/27`,

`v=D+a/3+b^2/18`, `V=C-b*D/4+a*b/12+b^3/54-c/2`.

The original characteristic polynomial is identically

`-2V*H^3+(3v^2/4+p)*H^2-3vV*H+v^3-V^2+p*v+q`.

All these shifts are auxiliary polynomial coordinate operations. They do not spend another source gauge. For k=33 or 36, H is monic of y-degree k and v,V have y-degree below k. Define the four monic divisions

`v^2=U*H+R`, `v*U=P*H+R1`, `v*R=Q1*H+R2`, `U^2=W*H+R3`.

The first high digit forces `V=3U/8`. The remaining expression is

`(3R/4+p-P/8)*H^2+(Q1-R1/8-9W/64)*H+(R2-9R3/64+p*v+q)`.

Every digit has y-degree below k. The H^2 digit is zero coefficientwise, and the H digit has exact degree 22 or 27 with scalar unit leader. The last digit is below the target and remains free. This verifies the D108 proposed degree63 emitter and the same alternative for degree55.

`depressed_division_control.py/.json` verifies both the complete translation identity and the four-division identity. An explicit difference certificate, after imposing V=3U/8, is

`(3H^2/4+v)*(v^2-UH-R)-H/8*(vU-PH-R1)+(vR-Q1H-R2)-9/64*(U^2-WH-R3)`.

Thus the equivalence is certified by the actual division identities over Q. No analogy between the two towers is used. D108's normalized h2 has total-degree bound 36, so building it through t36 captures the whole polynomial; its physical source cap is correct.

## Concrete parser rejection found

The initial D108 driver used `str(expr).replace('**','^')` and literal expressions such as `target_b^2/4`. On the installed Singular binary, the exact negative control

`ring R=0,(b),dp; poly h=b^2/4;`

produces `poly ^ number failed` because the quotient enters the exponent. The positive control

`ring R=0,(b),dp; poly h=(1/4)*b^2;`

succeeds. Parentheses around an entire coefficient containing `b^2/4` do not cure the internal parse. The defect also affects SymPy-serialized coefficients such as `q^9/32768`, already documented by the frozen corrected report.

The required repair is a rational-prefix serializer, applied to all physical coefficients and residual rows, and rational-prefix spelling of literal polynomial formulas. Any output containing parser diagnostics must be rejected before reading result markers. Both actual Singular control logs are recorded in this directory. This review does not claim that the repair has been deployed or that any full branch computation passed after it.
