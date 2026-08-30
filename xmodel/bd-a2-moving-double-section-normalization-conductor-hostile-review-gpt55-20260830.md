# Hostile review: moving-double-section normalization and conductor

Date: 2026-08-30 UTC
Reviewer: GPT-5.5 xhigh hostile lane
Review basis: `f43ee99da2bc9f831d94e403dcd90622e87e8756`

## 0. Verdict

`CONFIRM_WITH_CORRECTIONS`.

The producer's main mathematical conclusion is safe to promote in the charged
presentation scope: the remaining moving double `(1,1)` section has blowup
normalization with conductor quotient `O_C(-2)`, hence irregular normalization,
and it is incompatible with the dominant `A2` first leg.  I find no decisive
counterexample and no open mathematical gap in the squarefree charged case.

The corrections are real but local: several prose steps must be replaced by
explicit two-chart lemmas so that promotion does not rely on generic conductor
or tangent-cone language.  In particular the integration should spell out the
`ell=0` chart, the derivative test for multiple quartic roots, the local
conductor annihilator, and the exact open surface used for the forest
obstruction.

Inputs read and hash-checked:

* Producer:
  `9557f2c1396daba190927e6a220774362a02068b4197103357d30e8cfc78b75e`
  `xmodel/bd-a2-moving-double-section-normalization-conductor-sol56-20260830.md`.
* Section 0 charged block input:
  `ba69b33fba97215ac3e4b2481b06917baf004e884508a15aef136575a9440778`
  `xmodel/block-descent-structure-coordinator-integration-sol56-20260830.md`.
* Section 0 charged nonnormal input:
  `6b324824e0c075b938bd5b7015d4e8d134bad7cb845ac7597212b61d91dfa7a5`
  `xmodel/bd-a2-nonnormal-quadratic-content-cone-dichotomy-sol56-20260830.md`.
* Later forest input needed for Section 7 audit:
  `6a8558e42a67f1ec5c8bcf12321b6e6805b30a570eba17862c6e7e24cd631b08`
  `xmodel/bd-a2-rational-forest-coordinator-integration-sol56-20260830.md`.

No new exit-price assertion is made here, so no `charge_basis` line is
declared.

## 1. Predecessor Scope and Exact Form

Verdict: `CONFIRMED`.

The predecessor really leaves only the moving repeated section:

```text
Phi^h = Q^2 L + T Q S + T^2 R,
C = {T=Q=0},              [C]=(1,1),
D_0 = {T=L=0},            [D_0]=(0,1).
```

This is exactly the survivor in the nonnormal quadratic-content packet, not a
new classification made by the producer.  The same packet also charges affine
normality of `X_aff`, integrality of the projective incidence, and the fact
that all other repeated infinity patterns are already excluded.

The transverse equation along `C` is literally homogeneous of normal degree
two.  Locally choose a fibre coordinate `z` along `C` and use `(T,Q)` as normal
coordinates.  Since `L,S,R` are constant binary forms in the fibre variables,
they become functions of `z` alone.  Therefore

```text
F = ell(z) Q^2 + s(z) TQ + r(z) T^2
```

has no higher normal-degree terms.  This is stronger than saying the normal
cone has that equation, and it is exactly what later conductor computations
need.

The assertion `ell,s,r` never vanish simultaneously is correct, but the final
writeup should cite integrality/primitivity rather than the looser phrase
"generic irreducibility."  If `ell(p)=0`, the corresponding fibre point is the
unique zero of the binary linear form `L`.  If also `s(p)=r(p)=0`, then the
binary forms `S` and `R` are divisible by `L`, so the whole cubic
`Q^2L+TQS+T^2R` is divisible by `L`.  That contradicts the charged integral
projective incidence.

## 2. Discriminant and Squarefreeness

Verdict: `CONFIRMED_WITH_CORRECTIONS`.

At the generic point of `C`, `ell` is a unit and the completed local equation
is a binary quadratic over `C(C)`.  If

```text
delta_C = s^2 - 4 ell r
```

is zero, the equation is a square and the local hypersurface is generically
nonreduced along `C`.  If `delta_C` is a nonzero square in `C(C)`, the equation
splits into two linear factors and the local ring has zero divisors.  Both
contradict integrality.  Thus `delta_C` is nonzero and nonsquare.

The stronger squarefree step is also valid, but it needs the following explicit
local proof in the promoted version.

First, no multiple zero can occur over `ell=0`.  The section `ell` has one
simple zero on `C ~= P1`.  If `s(p) != 0`, then `delta_C(p)=s(p)^2 != 0`.  If
`s(p)=0`, the already-proved no-common-zero statement gives `r(p) != 0`, and
with a local parameter `z=ell` one has

```text
delta_C = s^2 - 4 z r,
```

so the zero is simple.

Every hypothetical multiple zero therefore lies where `ell` is a unit.  In the
blowup chart `Q=T w`,

```text
G(z,w)=ell(z)w^2+s(z)w+r(z)
```

is independent of the radial parameter `T`.  At a double root
`w_0=-s(z_0)/(2ell(z_0))`, the identities `G=G_w=0` hold.  Moreover

```text
delta_C'(z_0) = -4 ell(z_0) G_z(z_0,w_0).
```

Hence a multiple zero of `delta_C` is exactly a singular point of the plane
curve `G=0`.  Since the surface equation is `G=0` times the free radial
parameter, the strict transform has singular locus

```text
{(z_0,w_0)} x A1_T.
```

The part with `T != 0` is outside the exceptional divisor and maps
isomorphically into `X_aff`.  That would put a codimension-one singular locus
inside the charged normal affine incidence, impossible.  This proves
squarefreeness.

This argument also covers all quartic multiplicity rows.  Rows `2+2`, `4`, and
`delta=0` are eliminated already by nonsquare/nonzero integrality.  Rows
`2+1+1` and `3+1` have a multiple zero with `ell != 0`, so the exact product
chart above makes the blowup nonnormal along a nonexceptional affine line.
Only the `1+1+1+1` row survives.

## 3. Blowup and Normalization

Verdict: `CONFIRMED_WITH_CORRECTIONS`.

The two blowup charts are correct:

```text
Q=T w:       w^2 L+wS+R=0,
T=Q tau:     L+tau S+tau^2 R=0.
```

Over a point of `C`, the exceptional fibre is the length-two zero scheme of

```text
ell q^2+sqt+rt^2=0 in P1_[q:t].
```

Because `ell,s,r` never vanish together, no whole exceptional `P1` is contained
in the strict transform.  Fibres over `X-C` are singletons and fibres over `C`
are finite.  The map is proper, quasi-finite, and birational, hence finite.

The normality proof is sound after making the codimension-one checks explicit.
The strict transform is a Cartier hypersurface in the smooth blowup, so it is
`S_2`.  Off the exceptional curve it is isomorphic to `X-C`; by the charged
predecessor, the affine codimension-one points are normal and the residual
infinity component is generically regular.  Along the exceptional curve, the
squarefree discriminant makes the total conductor cover smooth.  In the
`ell`-unit chart this is just `G(z,w)=0` times the radial parameter.  In the
`ell=0` chart, take `z=ell`; the equation is

```text
z + tau s(z) + tau^2 r(z)=0,
```

after a unit rescaling, and its `z`-derivative is a unit at the exceptional
point.  Thus branch fibres and the `ell=0` fibre are regular on the strict
transform.

There is no unhandled codimension-one singularity along the residual section
`D`.  Away from `E`, the blowup is an isomorphism.  At `D cap E`, the same
`ell=0` chart gives a smooth surface, with `D` given by `z=tau=0` and `E` by
the radial coordinate zero together with the displayed equation.  Therefore
the strict transform is `S_2` and `R_1`, hence normal, and the finite birational
map is the normalization.

Repair required: replace the sentence "Equations (1.4)--(1.5) make the
relative quadratic curve smooth" by the two-chart argument above.  The fibres
over branch points are not reduced as fibres of `E -> C`; what is smooth is
the total curve `E` and the product surface along it.

## 4. Conductor and Canonical Formula

Verdict: `CONFIRMED_WITH_CORRECTIONS`.

The conductor computation is correct and can be made fully local.  At a point
of `C`, after an invertible linear change of the two normal parameters, write

```text
R = A[[t,q]]/(a q^2+b tq+c t^2),     a in A^*,
S = A[[t]][w]/(a w^2+bw+c),          q=t w,
```

where `A=O_{C,p}`.  Then

```text
R = A[[t]] direct-sum A[[t]] q
  = A[[t]] direct-sum A[[t]] t w
subset
S = A[[t]] direct-sum A[[t]] w.
```

Thus

```text
S/R ~= A w.
```

Multiplication by `t` kills this quotient because `tw=q in R`, and
multiplication by `q` kills it because `qw=t w^2 in R`.  Conversely an element
`f(t)+g(t)q` kills the class of `w` only if `f(0)=0`.  Hence the annihilator is
exactly `(t,q)R`, i.e. downstairs the conductor is exactly `I_C=(T,Q)O_X`.
After the same parameter change this also covers the `ell=0` and branch cases.

Upstairs the extended conductor is `(t,q)S=tS` in the `Q=Tw` chart, and
similarly the radial parameter ideal in the other chart.  Globally this is
`O_Xnu(-E)`.

The conductor square then gives

```text
0 -> O_X -> nu_*O_Xnu direct-sum O_C -> pi_*O_E -> 0.
```

For the finite flat double cover, trace splitting gives
`pi_*O_E = O_C direct-sum M`.  Its discriminant is the quartic
`delta_C in H^0(C,O_C(4))`, so `M^{-2}=O_C(4)`.  Since `C ~= P1`,
`M=O_C(-2)`, and therefore

```text
nu_*O_Xnu/O_X = O_C(-2).
```

The canonical formula has the right sign and coefficient.  Since the center is
a codimension-two smooth complete intersection in the smooth threefold,

```text
K_Bl = rho^*K_W + E_W,
Xnu = rho^*X - 2E_W,
```

and adjunction gives

```text
K_Xnu = nu^*K_X - E,
K_Xnu + E = nu^*K_X.
```

Repair required: state explicitly that the local normal-parameter change is
allowed at every point because the quadratic form is never identically zero on
an exceptional fibre.  Do not present the conductor as a generic calculation
followed by extension.

## 5. Cohomology and the First Leg

Verdict: `CONFIRMED`.

For `W=P2 x P1` and `X` of class `(2,3)`,

```text
0 -> O_W(-2,-3) -> O_W -> O_X -> 0
```

has `H^i(W,O_W(-2,-3))=0` in the degrees needed, because all cohomology of
`O_P2(-2)` vanishes.  Hence

```text
H^1(X,O_X)=0,       H^2(X,O_X)=0.
```

Using the normalization quotient,

```text
0 -> O_X -> nu_*O_Xnu -> O_C(-2) -> 0
```

and `C ~= P1`, one obtains exactly

```text
h^1(Xnu,O_Xnu)=1,       h^2(Xnu,O_Xnu)=0.
```

For any resolution `r:Xtilde -> Xnu`, normality gives
`r_*O_Xtilde=O_Xnu`, and the Leray edge map injects

```text
H^1(Xnu,O_Xnu) -> H^1(Xtilde,O_Xtilde).
```

Thus every resolution has `q >= 1`.

The dominant first leg is properly typed after charging the block coordinator
and the Stein/function-field identification: it gives a dominant rational map
`A2 --> Xnu` with finite function-field degree.  Resolve indeterminacy from a
projective rational surface and resolve the target.  The resulting morphism is
generically finite and dominant.  Pullback of holomorphic one-forms is
injective in characteristic zero, while the source is rational and has
`q=0`.  Hence the target resolution must have `q=0`, contradicting the
previous paragraph.

Repair required: the promoted text should say "resolve indeterminacy of the
rational first-leg map from a projective rational source" rather than only
"compactify and resolve"; this prevents confusion with a morphism defined on
all of `A2`.

## 6. Forest Boundary and Attachments

Verdict: `CONFIRMED_WITH_CORRECTIONS`.

The forest obstruction is legitimately independent of the cohomology
obstruction.  Take the smooth open target used by the first leg inside the
resolved normalization over the affine target.  The conductor curve `E` lies
over `T=0`, hence outside that open.  Since the normalization is smooth along
`E`, every SNC completion/resolution contains the strict transform of `E` as a
boundary component, possibly after blowing up points on it.  Its geometric
genus remains one in the charged squarefree row.  The binding forest theorem
forbids a positive-genus boundary component under a dominant rational
`A2` first leg.

The residual section attachment count is also correct.  Let `p0` be the unique
point where `C` meets `D0`, equivalently the unique zero of `ell=L|_C`.  In
exceptional coordinates `[Q:T]`, the fibre equation is

```text
T(s(p0)Q+r(p0)T)=0.
```

The strict transform of `D0` approaches the direction `[Q:T]=[1:0]`, because
on `D0` one has `T=0` and, away from `p0`, `Q != 0`.  If `s(p0) != 0`, the
conductor cover is unramified over `p0` and has two points, but `D` meets only
the `[1:0]` point.  If `s(p0)=0`, then `r(p0) != 0`, the fibre is ramified,
and `D` meets the unique branch point.  Thus there is exactly one physical
attachment in both cases.

Repair required: define the open `U` used for the forest theorem before
claiming monotonicity under shrinking.  The argument is valid because the
generic first-leg image lies over `T != 0` and the charged block input already
keeps it in the smooth affine target away from the missed branch/singular
locus.

## 7. Degenerate Quartic Threat Map

Verdict: `CONFIRMED`.

The degenerate rows are correctly separated from the charged surface
normalization.  A nonsquare quartic of type `2+1+1` gives an integral nodal
conductor curve with normalization `P1`; type `3+1` gives a cuspidal conductor
curve with normalization `P1`.  In both cases the exact product chart makes
the blowup fail `R_1` along a radial line meeting the affine incidence, so
affine normality eliminates them before any boundary-forest argument is used.

The split rows `2+2` and `4` are excluded by generic reducibility of the
normal quadratic, not by curve genus.  The row `delta=0` is excluded by
generic nonreducedness.  The producer does not rely on the false shortcut that
a nodal or cuspidal first blowup is already normal, and it does not use
arithmetic genus alone to close the surface normalization problem.

One small wording repair: in the threat map, keep saying "curve-theoretic
pre-normalization contribution" for `tau(E union D)` in degenerate rows.  The
actual surface normalization would introduce further conductor and exceptional
data, so those rows must not be recycled as completed surface cases.

## 8. Maximum Theorem Safe to Promote

Verdict: `CONFIRMED_WITH_CORRECTIONS`.

The safe theorem is the following presentation-scoped statement.

Assume the charged proper-block first leg and the charged nonnormal quadratic
presentation packet.  In the surviving fixed quadratic trace-zero
presentation

```text
X = V(Q^2L+TQS+T^2R) subset P2 x P1,
C=(T,Q),        [C]=(1,1),
```

with `X_aff` normal and `X` integral, the discriminant
`delta_C=(S|_C)^2-4(L|_C)(R|_C)` is nonzero, nonsquare, and squarefree.  The
strict transform of `X` in `Bl_C(P2 x P1)` is the finite normalization.  The
downstairs conductor is `(T,Q)O_X`, the upstairs conductor is `O_Xnu(-E)`, the
conductor cover is a smooth connected genus-one double cover of `C`, and

```text
pi_*O_E = O_C direct-sum O_C(-2),
nu_*O_Xnu/O_X = O_C(-2),
K_Xnu + E = nu^*K_X,
h^1(Xnu,O_Xnu)=1,
h^2(Xnu,O_Xnu)=0.
```

Consequently every resolution of `Xnu` has positive irregularity, while the
dominant rational `A2` first leg would force irregularity zero.  Equivalently,
the genus-one conductor is also a forbidden boundary component under the
charged rational-forest theorem.  Therefore this moving-double-section
nonnormal quadratic presentation cannot occur in a proper cubic block.

This does not promote any of the following:

* arbitrary quadratic-basis coverage;
* invariance of the infinity divisor under all basis changes;
* the normal-singular/ADE quadratic incidence lane;
* existence of a polynomial map or a counterexample;
* any source different, full affine target discriminant, finite-prefix, formal
  arc, or JC2 conclusion.

## 9. Precise Repairs

Before promotion, make these textual repairs in the integration:

1. Replace "contrary to generic irreducibility" in the no-common-zero argument
   by "contrary to the charged integrality of the primitive projective
   incidence."
2. Insert the identity
   `delta_C'(z0)=-4 ell(z0) G_z(z0,w0)` in the squarefree proof and explicitly
   state that the product with the radial parameter gives a codimension-one
   singular locus.
3. Add the `ell=0` chart:
   `z + tau s(z) + tau^2 r(z)=0`, with unit `z`-derivative, covering both the
   unramified and ramified fibre over `D cap C`.
4. State that branch fibres of `E -> C` are nonreduced as fibres but the total
   curve `E` and the strict transform surface are smooth there.
5. Replace the conductor prose by the local module calculation
   `R=A[[t]]+A[[t]]tw subset S=A[[t]]+A[[t]]w`, whose quotient is `A w` and
   whose annihilator is exactly `(t,q)`.
6. Define the open surface used in the forest theorem as the smooth resolved
   first-leg target over `T != 0`, with any missed affine branch/singular locus
   removed.

## 10. Cheapest Decisive Successor

The cheapest immediate successor is a correction-only coordinator integration,
not a new computation: insert the six repairs above and promote
`MOVING-DOUBLE-Q2-CLOSED` exactly in the fixed-presentation scope.  No CAS,
Singular, finite-prefix search, or Lean work is needed.

After that, the next mathematical successor is the separate normal-singular
quadratic packet: classify the ADE-decorated `D9` boundary/different cases.
Keep the basis-orbit coverage problem separate, because this review confirms
only that any basis already producing the nonnormal moving-double-section form
is impossible.
<!-- BODY-END -->
