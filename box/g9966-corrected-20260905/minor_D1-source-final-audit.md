# Independent audit of the D1 differential face and terminal certificate path

The extra D1 rows in `run-code-source-full/deep_gauge_accelerated.py` are
necessary on the complete corrected chart. Their addition repairs a genuine
logical omission of the chart containing only support, pole, and positive
Jacobian rows: a point with all outer remainders zero makes F=H2^3 and G=H2^2
and has identically zero Jacobian, so it fails the printed nonvanishing
condition. Such a point cannot be advertised as surviving every printed face.
This note asserts no unit; actual branch status requires the exact computations.

Moh's printed p179, Definition5.1(4), invokes Proposition4.6 at each specified
disc (`moh-layout.txt:2137-2138`). The printed r=1 conclusion on p170 is
the differential expression equal to a nonzero constant
(`moh-layout.txt:1646-1648`). The specific expression implemented here is
derived directly from the physical coordinate Jacobian, avoiding any ambiguity
between Moh's T labels and derivative marks.

Use the source-derived D1 substitution

    t=e^9, z=e^12+Pi*e^13,
    x=e^-9, y=e^-9+e^3+Pi*e^4.

The coordinate determinant d(x,y)/d(e,Pi) equals -9e^-6. The physical leading
orders from Definition5.1 and the root counts are F=e^-3 P(Pi)+higher terms
and G=e^-2 Q(Pi)+higher terms. Therefore the leading Jacobian is

    J_e0 = (3 P Q' - 2 P' Q)/9.

Every higher physical e-order contributes a strictly positive e-order to the
Jacobian after division by the coordinate determinant. Thus a constant Keller
Jacobian must equal this entire polynomial. This derives every coefficient
row of `J_e0-Jc`, and the sole extra relation `ZJ*Jc-1` asserts nonvanishing.
Jc remains a free nonzero scalar; no target dilation is spent to set Jc=1.
The source translation has determinant1 and preserves this condition, so the
global slice proof in `minor_gauge-final-audit.md` applies to the stronger chart.

The P and Q polynomials are computed, not prescribed. If H denotes the
coefficient of e^296 in normalized K2=h3^3+C2*h3+C3, and a2,a3,b1,b2 denote
the computed D1 outer faces at thresholds583,879,287,583, respectively, then

    P=H^3+a2*H+a3, Q=H^2+b1*H+b2.

The one-t shift in each outer remainder is accounted for exactly:
583+9+296=879+9=888=9*99-3, and
287+9+296=583+9=592=9*66-2. Thus no shift, scale, or face term is missing.
The production helper's low D2-weight cutoff98 for building H is exact:
the smallest e-exponent of a normalized monomial of D2-weight W is3W,
so every term of weight99 or more starts at e^297 and cannot affect e^296.
This is a coefficient-extraction cutoff, not an unsupported omission of an
unknown. Existing D1 support rows guarantee that the extracted terms really
are the first possible terms of F and G. If cancellation annihilates either
face, the generated differential rows correctly reject that degeneration
under the nonzero-J condition.

There is in fact no missing degree localization at this disc. The mechanical
`minor_D1-leader-control.py/json` check shows that the41 stage0 outer pivots
annihilate every first D2 weight layer; the resulting outer D1 face degrees
are at most13,21,5,13. The K2 equality layer gives
`((1+Pi*e)^3-1)^8`, whose e^8 coefficient has leading term3^8 Pi^8.
Every higher D2 layer contributes Pi degree at most5 at e^296. Hence the
outer contributions have degrees at most21 in P and13 in Q, while H^3 and
H^2 have degrees24 and16, with fixed leaders3^24 and3^16. These leaders
cannot cancel. Later necessary rows preserve these conclusions.

The additional origin row in the same wrapper is also necessary. A normalized
degree-D polynomial K=t^D Q(x,y) has physical first Taylor data

    Q(0,0)=K[D,0],
    Qx(0,0)=K[D-1,0]-K[D-1,1], Qy(0,0)=K[D-1,1].

This follows by expanding the source basis x^(D-r-p)(y-x)^p. The wrapper
uses the correct normalization degree for h3,C2,C3 and the actual degree of
each unshifted outer block. Its product-rule formula equals FxGy-FyGx at the
origin. The equation is J(0,0)-Jc, using the SAME scalar as the D1 face.
The origin coefficient can be added early to reject degenerations; it does
not impose any new source-coordinate gauge.

`minor_final_verify.py` now recognizes the exact certificate row families
`gauge_D1_J_face_Pi{k}`, `gauge_J_nonzero_wrapper`, and
`gauge_early_J_constant`. It rebuilds the D1 source series in e and Pi first,
then multiplies those series up to the required exponent; it does not call
the production D1 extractor or weighted multiplication. It computes the
coordinate determinant and Jacobian symbolically before extracting the
order-zero expression. It independently rebuilds physical first Taylor
polynomials and differentiates F/G for the origin row, rather than using
the production corner wedge formula. Each family is regenerated on the
saved `map_before` locus before its new QQ* reductions. When Jc has already
been solved, its recorded image is applied, ensuring that later rows use
the same scalar rather than silently introducing another constant.

`minor_d1-final-controls.py/json` compares both independent methods with the
production helper on nontrivial symbolic source blocks, successfully
regenerates20 D1 coefficient/wrapper rows and one origin row, and checks
that higher physical e-orders do not change the D1 result. Fresh exact-Q
Singular controls on BOTH branch localizations show that Jc=0 plus its inverse
is a unit, while Jc=7 with inverse1/7 and rho=1 or c=1 is nonempty. These
controls explicitly distinguish the Jacobian nonvanishing localization from
the branch localizer and confirm that no numerical Jc=1 normalization was
silently imposed. The verifier records the D1 helper's SHA-256 alongside
the immutable engine, source, and driver files. Full saved-phase replay and
fresh residual-ideal Singular verification remain required for any endpoint
promotion.

The stronger resume harness introduces named face coordinates only by exact
graph equations `Zface_{name}_{k} = [Pi^k]face`. The verifier checks the
explicit new generator declarations and independently reconstructs every
coefficient on the preceding source locus. It also checks the entire face,
including rational coefficients for which no new coordinate is introduced,
so the graph cannot omit a coefficient or pin one. Subsequent QQ* exchanges
preserve the full locus. The compressed D1 rows are independently checked
by the physical chain-rule formula in these certified face coordinates.

A real serialization hazard was found in the historical Singular exporter:
expressions containing rational coefficients adjacent to powers can be parsed
incorrectly when written by plain string replacement. The final verifier now
scales EACH residual row by a recorded nonzero rational to a primitive integer
polynomial and checks the exact identity before writing Singular syntax. It
rejects parser errors. New nonlinear regression controls using q4^9/32768
distinguish a unit and a rational-point ideal correctly. Earlier source-stage
and complete-pole checkpoint verifications have zero residual rows, so this
export issue does not affect their dimension computations. No nonlinear
endpoint is accepted using the unsafe exporter.
