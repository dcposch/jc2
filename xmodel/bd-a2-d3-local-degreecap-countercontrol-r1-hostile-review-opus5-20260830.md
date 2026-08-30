# Hostile review: corrected D3 local raw-degree-three counter-control (R1)

Date: 2026-08-30 UTC
Reviewer: Opus 5, fresh hostile lane, independent reconstruction
Audited artifact: `bd-a2-d3-local-degreecap-countercontrol-r1-sol56-20260830.md`
Verdict: **CONFIRM_WITH_CORRECTIONS** — the corrected counter-control is
sound, the refutation stands, and the result is materially **stronger** than
the report prices it.

This review asserts no exit price.  No `charge_basis` line is emitted;
receipt status `ABSENT` is expected and correct.

## 0. Custody, execution environment, scope discipline

All six charged hashes reproduce byte-exactly:

```text
13677719...8879  bd-a2-d3-local-degreecap-countercontrol-r1-sol56-20260830.md          OK
71e17cac...132b  ...-r1-sol56-20260830.md.artifact.json                                OK
82f930ff...c79b  bd-a2-d3-local-degreecap-countercontrol-sol56-20260830.md             OK
55b836a7...96b2  ...-sol56-20260830.md.artifact.json                                   OK
c0ace16d...c8ab  bd-a2-d3-sectioned-one-support-threat-map-sol56-20260830.md           OK
95f2f9ff...ca79  bd-a2-d3-hodge-level-divisor-coordinator-integration-sol56-20260830.md OK
```

Internal seal of the R1 report also verifies: exactly one standalone
`<!-- BODY-END -->` (line 277), body `7793` bytes, body SHA-256
`4e0c58a36bf8645603dc86d9d5b1ce042415139400ef8738022aeae33764ac62`, matching
both the seal block and `body_sha256`/`source_sha256` in the artifact JSON.

Execution: a real shell was available.  Everything reported below as
"machine-verified" was executed locally under CPython 3.9.6 / SymPy 1.14.0
with assertions live (`__debug__` true).  Nothing was run on AWS and no heavy
CAS was invoked; the largest computation was a lex Groebner basis in three
variables.  No sibling prompt/log/report/receipt was opened, and `jc2-lean`
was not inspected, listed, searched, stat'd, built, modified, or controlled.

## 1. Raw model, degree cap, point, shear — `CONFIRM_WITH_CORRECTIONS`

Machine-verified expansion, reproducing (1.1) exactly:

```text
Phi = x^3 + 3t x^2z + 3t^2 xz^2 + t^3 z^3 + t y^3 + t^3 x^2y
```

| monomial | coefficient | `t`-degree |
|---|---|---:|
| `x^3`   | `1`      | 0 |
| `x^2z`  | `3t`     | 1 |
| `y^3`   | `t`      | 1 |
| `xz^2`  | `3t^2`   | 2 |
| `x^2y`  | `t^3`    | 3 |
| `z^3`   | `t^3`    | 3 |

Literal raw cap is `3`, attained twice (`x^2y`, `z^3`), so the cap is exactly
three and not merely bounded.  Coefficient content in `t` is `1`, so the model
is primitive.  `Phi(-t,0,1)=0` verified.  The shear matrix in `(x,y,z)` is
`[[1,0,-t],[0,1,0],[0,0,1]]` with determinant `1` and integral inverse
`[[1,0,t],[0,1,0],[0,0,1]]`, so it is a genuine `SL_3(R)` gauge.

Also note `Phi mod t = x^3`: the reduction is the **triple line**, which is
row five of the threat-map five-orbit nullcone list, and `Phi` sits literally
in the coordinator family shape `F_0 + tF_1 + t^2F_2 + t^3F_3`.

**Raw versus transformed degree.**  I looked specifically for the misuse and
found none in the mathematics, but I did find a documentation regression.
Machine-verified raw `t`-caps along the chain:

```text
Phi     cap 3   content 1
Phi'    cap 5   content 1      <-- breaks the cap
Phi_1   cap 3   content 1
Phi_0   cap 3   content 1
```

The intermediate `Phi'` has raw `t`-degree **five**.  That is harmless because
the shear has `mu=1` and `det M=1`, hence `v(mu det M)=0` and every CFS
invariant and the level are preserved exactly; and because the charged cap is
asserted only for `Phi`.  But the superseded report stated this explicitly
(its lines 72--74: "Although (1.4) contains terms of `t`-degree four and five
after expansion, this is only an integral coordinate gauge.  The charged raw
presentation is (1.1)"), and **R1 deleted that disclaimer**.  A reader of R1
alone can reasonably infer that the cap survives the shear.  It does not.
Correction: restore one sentence to `Phi'` in R1 Section 1.

## 2. The two transformations and the Smith pair — `CONFIRM_WITH_CORRECTIONS`

Machine-verified, exactly as printed:

```text
Phi' = X^3 + t y^3 + t^3(X - t z)^2 y
Phi_1 = t^-3 Phi'(tX,ty,z) = X^3 + t y^3 + t^3(X - z)^2 y
Phi_0 = t^-3 Phi_1(tX,ty,z) = X^3 + t y^3 + t(tX - z)^2 y
                            = X^3 + t y^3 + t z^2 y - 2t^2 Xzy + t^3 X^2 y
```

Integrality is not assumed: I substituted and took the exact remainder.  With
the declared ordering `(z,X,y)`, i.e. weight-zero slot `z`, both

```text
Phi'(z, tX, ty) = 0 mod t^3        and        Phi_1(z, tX, ty) = 0 mod t^3
```

hold with zero remainder, which is the admissibility condition
`F(x, t^a y, t^b z) = 0 mod t^{a+b+1}` at `(a,b)=(1,1)`, `a+b+1=3`.  So the
coordinate ordering and every power of `t` check out.

Smith form of the **composite** `Phi -> Phi_1` (shear then scaling), whose
matrix is `[[t,0,-t],[0,t,0],[0,0,1]]`: invariant factors machine-computed as
`d_1=1`, `d_1d_2=t`, `d_1d_2d_3=t^2`, i.e. Smith normal form `diag(1,t,t)`.
The unimodular shear does not disturb the pair, so `(a,b)=(1,1)` survives
composition.  `v(mu det M) = -3 + 2 = -1` per arrow; the two-arrow composite
is `Phi_0(X,y,z) = t^-6 Phi(t^2X - tz, t^2y, z)` with `det = t^4` and
`v(mu det) = -2`.

The scaling law `(4,6,12)` is correct: for genus-one models of degree three,
`c4, c6, Disc` have weights `4, 6, 12` in `mu det M`, so `v(mu det M) = -1`
lowers `(v(c4),v(c6),v(Disc))` by `(4,6,12)` and `v(Disc)` by one level.

Two provenance corrections:

- R1 says "the invariant valuations" without naming them.  The superseded
  report named `(v(c4),v(c6),v(Disc))`.  Restore.
- **R1 carries no bibliographic citation at all.**  The superseded report
  cited Cremona--Fisher--Stoll, *Minimisation and reduction of 2-, 3- and
  4-coverings of elliptic curves*, ANT 4 (2010), Theorem 4.3 and Lemma 4.4,
  and printed the admissibility congruence explicitly.  R1 invokes "CFS
  admissible pair" and "CFS Lemma 3.14" with neither the reference nor the
  defining congruence.  Since R1 declares itself the only consumable report,
  the definitions it depends on are now uncitable from it.  Restore both.

Framing nit (not an error): R1's "refutes any universal no-go based on
exhausting `(0,1),(1,1),(1,2),(2,3)`" is true but for a simpler reason than
stated — the witness satisfies every hypothesis and violates the conclusion,
so exhaustiveness of the menu is irrelevant to the refutation.

## 3. Terminal invariants, `IV*`, and the ladder — `CONFIRM_WITH_CORRECTIONS`

I did **not** accept the report's hand-entered quartic.  I derived the whole
of Section 2 mechanically from `Phi_0`.

Lemma coordinates `(X_l,Y_l,Z_l)=(X,z,y)` give
`F = X^3 + tZ^3 + tY^2Z - 2t^2XYZ + t^3X^2Z`, whose `Y^3` coefficient is `0`
(so `[0:1:0]` is on the curve).  Extracting coefficients of `F` as a
polynomial in `Y` returns

```text
f1 = tZ            (degree 1)
f2 = 2t^2XZ        (degree 2)
f3 = -(X^3 + tZ^3 + t^3X^2Z)   (degree 3)
```

with `f1Y^2 - f2Y - f3 - F = 0`.  This reproduces R1 (2.2) and **refutes**
superseded (3.2), which printed `Z^3` in place of `tZ^3`.  Then

```text
w^2 + 2t^2XZ w = f1 f3 = -tX^3Z - t^2Z^4 - t^4X^2Z^2      matches R1 (2.3)
W = w + t^2XZ  =>  W^2 = -tZ(X^3 + tZ^3)                   matches R1 (2.4)
```

and the superseded `(3.4)` `W^2=-tZ(X^3+Z^3)` is machine-refuted.  Extracting
`(a,b,c,d,e)` from the derived quartic returns exactly `(0,-t,0,0,-t^2)`, and
`I=0`, `J=27t^4`, `(4I^3-J^2)/27 = -27t^8`, so `(v(I),v(J),v(Disc)) =
(inf,4,8)`.  In the chart `Z=1` with `U=-tX`, `V=tW`: `V^2=U^3-t^4`, hence
`c4=0`, `c6=864t^4`, `Disc=-432t^8`, and `c4^3-c6^2-1728 Disc = 0` verified.
Minimality: `v(c6)=4<6` blocks any `u` with `v(u)>=1`.  Kodaira `IV*` from
`(v(c4),v(c6),v(Disc))=(>=3,4,8)` in residue characteristic zero, cross-checked
against the `y^2=x^3+t^n` family at `n=4` (`n=4 mod 6 -> IV*`, `v(Disc)=2n=8`).

**Stronger route found (supersedes the report's Lemma-3.14 dependence).**  The
projection is unnecessary.  Machine-verified identity, with
`G(U,V,W) = V^2W - U^3 + t^4W^3` the Weierstrass ternary cubic:

```text
G(-tX, -t^2(Y - tX), Z) - t^3 F(X,Y,Z) = 0        (exact, all t)
M = [[-t,0,0],[t^3,-t^2,0],[0,0,1]],  det M = t^3,  mu = t^-3,
mu * det M = 1   exactly.
```

Because `mu det M = 1`, `F` and `G` are genus-one models with **literally
equal** `c4, c6, Disc` — no unit ambiguity, no appeal to CFS Lemma 3.14, and
no dependence on the projection being invariant-preserving.  As a second,
independent confirmation I tracked the invariant differential:
`F_Y = -2t(tX - Y)`, `V = t^2(tX - Y)`, and

```text
(dU/(2V)) / (dX/F_Y) = 1        (machine-verified)
```

so the model differential of `Phi_0` is exactly the Weierstrass differential
of `V^2=U^3-t^4`.  Both routes give (2.6).

Ladder, therefore exact:

```text
             Phi_0     Phi_1      Phi
v(c4)         inf       inf       inf
v(c6)          4         10        16
v(Disc)        8         20        32
CFS level      0          1         2
```

Level two is exact because `v(Disc(Phi_0)) = 8 < 12` and integral models have
`v(Disc) >= 0`, so no further level-lowering arrow exists — this is the
superseded report's alternative argument, which survives the correction and is
strictly cheaper than R1's `v(c6)<6` route.  Coordinator gate (5.2) at `k=2`
verified: `v(c4)=inf>=8`, `v(c6)=16>=12`, `v(Disc)=32>=24`, and the upper
disjunction holds through `v(c6)=16<18`.  Threat-map (4.2) also holds:
`26 <= 24+8 = 32 <= 34`.

R1 (2.8) verified: the projection `y=sX` in chart `z=1` factors off `X` and
leaves `(1+ts^3+t^3s)X^2 - 2t^2sX + ts`, quadratic discriminant
`-4ts(1+ts^3)`, whose binary-quartic invariants are `I=0`, `J=1728t^4`,
`v(Disc)=8` — orders `4,8` as claimed.

Correction: R1 labels (2.8) "an independent check".  It is not independent.
It is the same projection from the same point recomputed in an affine
parametrisation; the resulting quartic is `4` times the coordinate swap of
(2.4).  It is a corroborating recomputation and should be labelled as such.
The genuinely independent checks are the two given above.

## 4. Generic smoothness and the total singular locus — `CONFIRMED`

Partials machine-verified against the report:

```text
Phi_x = 3u^2 + 2t^3xy,   Phi_y = 3ty^2 + t^3x^2,   Phi_z = 3t u^2,   u = x+tz
```

**Generic fibre.**  I did not rely on the report's case split.  In each of the
three charts I saturated by `t` (adjoining `u` with `ut=1`) and computed a
Groebner basis of `(Phi_x, Phi_y, Phi_z, ut-1)`:

```text
chart z=1: GB = [1]      chart y=1: GB = [1]      chart x=1: GB = [1]
```

So the generic cubic is smooth over every field extension, i.e. geometrically
smooth, not merely `C((t))`-smooth.  The report's hand argument is also valid,
though its clause "projectivity forces `y!=0`, a contradiction" is compressed:
the contradiction is with `3y^2 + t^2x^2 = 0` forcing `y=0`, not with
projectivity itself.

**Total space.**  Full Jacobian ideal `(Phi, Phi_x, Phi_y, Phi_z, Phi_t)` in
`P^2_{C[[t]]}`, all three charts, lex Groebner:

```text
chart z=1:  unique solution (x,y,t) = (0,0,0)
chart y=1:  GB = [1]     (no singular point)
chart x=1:  GB = [1]     (no singular point)
```

Hence (3.2) is **complete**; I found no omitted generic or closed-fibre point.
Two candidate traps were checked and are clean: the generic point of the
closed fibre (the line `x=0`, where `Phi_t|_{t=0}=3x^2z+y^3` reduces to the
unit `y^3`, so `Phi` lies outside the square of the maximal ideal and the
local ring is a DVR), and the closed-fibre point `[0:1:0]` (where
`Phi_t|_{t=0}=1`).  The germ at the singular point has multiplicity `3`.

Integrality: verified `Phi` irreducible in `Q[t][x,y,z]` and primitive in `t`;
with the generic cubic smooth hence geometrically integral, Gauss's lemma
gives `(Phi)` prime.  `S_2`: `P^2_{C[[t]]}` is regular (`C[[t]]` a DVR), so a
hypersurface in it is Cohen--Macaulay.  `R_1`: `dim X = 2` and the singular
locus is one closed point of codimension two.  Serre gives normality.  The
codimension count and the Serre application are correct as written.

## 5. Comparison with the superseded report — `CONFIRM_WITH_CORRECTIONS`

R1 explicitly retracts: the terminal `I_0^*` label; the valuations
`(inf,3,6)`; the level-one and level-two discriminant orders `18` and `30`.
It adds a blanket clause: "every conflicting fibre label or valuation in the
superseded report is retracted."

Full consequence ledger of the dropped `t`, with retraction status:

| superseded item | status in R1 |
|---|---|
| (3.2) `f3 = -(X^3+Z^3+t^3X^2Z)` | corrected by R1 (2.2) |
| (3.3) quartic RHS `-tX^3Z-tZ^4-t^4X^2Z^2` | corrected by R1 (2.3) |
| (3.4) `W^2=-tZ(X^3+Z^3)` | corrected by R1 (2.4) |
| (3.6) `V^2=U^3-t^3` | corrected by R1 (2.5) |
| (3.5) `v(Disc(Phi_0))=6`, type `I_0^*` | explicitly retracted |
| (3.7) `v(Disc(Phi_1))=18`, `v(Disc(Phi))=30` | explicitly retracted |
| (3.8) `v(c6(Phi))=15` | **blanket only, not named** |
| Sec 5 and Sec 8 `I_0^*` narrative | covered by the label retraction |
| Sec 6 replay tuple `(0,-t,0,0,-t)`, `J=27t^3` | replaced, not flagged |

Every conflicting **value** is therefore retracted, if only by the blanket
clause.  I found no stale numeric statement that survives incorrectly into R1.

But one **method**, not merely a value, is wrong and is nowhere flagged.
Superseded Section 3 argued:

```text
"The binary quartic Z(X^3+Z^3) has four distinct roots over C, so its
 discriminant is a unit.  Scaling a binary quartic by t scales its
 discriminant by t^6; hence v(Disc(Phi_0))=6."
```

With the corrected quartic `-tZ(X^3+tZ^3)` this reasoning is not merely
mis-arithmetic — it is unsound, because `X^3+tZ^3` is **not** a form with unit
discriminant: it degenerates to `X^3` modulo `t`.  The correct answer `8`
cannot be obtained by "count distinct roots over `C`, then scale".  R1 silently
replaces the argument with a direct `I,J` computation but never says the old
route was invalid.  Correction: R1 must add one line retracting the
root-counting/scaling method, otherwise a successor will reuse it.

Separately, four **correct** statements of the superseded report were dropped
without replacement and should be restored: the `Phi'` degree-4/5 disclaimer
(Section 1 above), the CFS citation and the admissibility congruence
(Section 2 above), and the `v(Disc) < 12` minimality argument (Section 3
above, which is cheaper than the route R1 kept).

## 6. Replay audit — `CONFIRM_WITH_CORRECTIONS`

The R1 replay was executed verbatim, unmodified, under ordinary CPython with
assertions live.  It exits `0` and prints exactly

```text
D3_LOCAL_DEGREECAP_COUNTERCONTROL_R1_PASS
```

No optimized-mode evidence is used anywhere in this review.

**However, the replay does not discriminate the correction it exists to
support.**  I also executed the superseded report's replay verbatim.  It also
exits `0` and prints its banner.  The reason is structural: in both scripts the
binary-quartic coefficients are **hand-entered constants**

```text
R1:          a,b,c,d,e = 0,-t,0,0,-t**2
superseded:  a,b,c,d,e = 0,-t,0,0,-t
```

and are never derived from `Phi_0`.  The single step that was wrong is exactly
the step the replay does not cover.  This is the producer-authored-banner
failure mode: a PASS proves the author's arithmetic is self-consistent with
the author's own input, not that the input follows from the model.

Two further weaknesses: `assert I == 0` is vacuous, because with
`a=c=d=0` the expression `12ae-3bd+c^2` is the Python integer `0` before any
model is consulted; and `s.degree(c,t)` on the constant coefficient of `x^3`
returns `0`, which happens to be right but is incidental.

Separation of executable from hand proof in R1:

```text
EXECUTABLE : expansion; raw cap; the point [-t:0:1]; the Phi'/Phi_1/Phi_0
             identities; the t=0 partial-derivative vector; I,J of a supplied
             tuple; the projection quadratic discriminant.
HAND ONLY  : extraction of f1,f2,f3; passage to the generalized binary
             quartic; square completion; the (U,V) substitution; minimality;
             the Kodaira symbol; the (4,6,12) weight law; the level ladder;
             integrality, S_2, R_1, Serre normality.
```

Minimal repair, verified by me to work and to be cheap: replace the hand tuple
by mechanical extraction from `Phi_0`, and add the one-line linear-equivalence
assertion.  Both reproduce, respectively, `(0,-t,0,0,-t^2)` and an exact zero:

```text
F  = expand(Phi0.subs({z:Y, y:Z}, simultaneous=True))
PF = Poly(F, Y); f1 = PF.coeff_monomial(Y**2); f2 = -PF.coeff_monomial(Y)
f3 = -PF.coeff_monomial(1)
assert expand(f1*Y**2 - f2*Y - f3 - F) == 0
Q  = Poly(expand(f1*f3 + f2**2/4), X, Z)          # derived, not supplied
assert expand(t**3*(V**2*W - U**3 + t**4*W**3).subs(
        {U:-(x+t*z)/t, V:t*x, W:y/t**2}, simultaneous=True) - Phi) == 0
```

The second assertion also fails loudly on the superseded model, so it is a
true discriminator.

## 7. Narrow pricing — `CONFIRM_WITH_CORRECTIONS`

**The refutation itself is genuine.**  The conjectured local impossibility —
that literal raw coefficient `t`-degree three, normality of the total surface,
generic smoothness, `C((t))`-solubility and exact CFS level two cannot hold
together over `C[[t]]` — is **REFUTED**, by a witness all of whose hypotheses I
reconstructed independently.  This closes the gap the threat map left open at
its Section 0.4: the degree-thirteen control `y^2z=x^3+t^13z^3` failed only the
literal degree-three presentation gate, and that gate no longer rejects.  The
refutation does not depend on any later global success.

**But R1 prices the result too low on three checkable points.**  R1 Section 5
asserts flatly that the counter-control "does not supply a rational global
surface, a dominant `A^2` map, a proper-block occurrence, a compatible
discrepancy row, a polynomial map, or JC2", and lists global integrality,
normality "especially `S=0`", rationality and boundary topology as OPEN.  I
computed the natural class-`(3,3)` homogenization (5.1) and three of those
items are decided, affirmatively.  All of the following is my own computation,
is not part of the charged artifact, and is **UNREVIEWED**:

```text
Xbar = V( S^3x^3 + S^2T(3x^2z+y^3) + ST^2(3xz^2) + T^3(z^3+x^2y) ) in P^2 x P^1
```

- Irreducible (verified), and its complete singular locus is **exactly two
  points**: `p_0 = ([0:0:1],[1:0])`, the level-two point already found, and
  `p_inf = ([0:1:0],[0:1])`.  All six chart pairs were scanned; four give the
  unit ideal.
- `p_inf` has 2-jet `S^2+x^2` of rank two and cubic tail `z^3`, hence is a
  Du Val `A_2`.  So `Xbar` is a hypersurface in a smooth threefold with
  isolated singularities: `S_2` plus `R_1`, hence **normal**, including at
  `S=0`.
- `[x:y:z]=[-T:0:S]` is a global **section** (verified identically zero), so
  the row is `m=1`.
- The exact global plane-model invariants follow from the projective-linear
  equivalence of Section 3 above, whose `mu det N = -t^2`:

  ```text
  c4 = 0,      c6 = 864 S^2 T^16,      Disc = -432 S^4 T^32.
  ```

  The fibration is isotrivial with `j=0`; `Disc` is a monomial in `t`, so
  `t=0` is the **only** singular fibre in the affine base.
- Minimal Kodaira types: `IV*` at `t=0` (`v(Disc_min)=8`) and `IV` at `t=inf`
  (`(inf,2,4)`, minimal since `v(c6)=2<6`, `v(Disc_min)=4`).  Euler budget
  `8+4 = 12`, so `deg Disc_min = 12d` gives `d=1`, `chi(O_S)=1`, `K_S=-F`:
  the relatively minimal model is an **extremal rational elliptic surface**
  (Shioda--Tate: `10 = 2 + rk MW + 6 + 2`, so `rk MW = 0`).  Hence `Xbar` is
  **rational**, and therefore does admit a dominant *rational* map from `A^2`.
- `chi(O_Xbar) = 3` for a `(3,3)` hypersurface, and `chi(O_Y) = 1` since `Y`
  is rational; Leray gives `p_g(p_0) + p_g(p_inf) = 2` with `p_g(A_2)=0`, so
  `p_g(p_0) = 2`.  Thus `Z_GR` sits over `t=0` only, `T = 2[t=0]` has length
  two, and `D = K_S - F = -2F = -2F_0`.

That is **exactly row two of the coordinator table**: `section | T=2t |
D=-2F_t | exact local level 2 | >= 2 blowups | rho(Y) >= 12`.  It also passes
every conditional threat-map filter: `IV*` is in the additive list (0.3), and
(4.2) gives `26 <= 32 <= 34`.  As a bonus the instance independently
corroborates the coordinator's promoted "CFS level = local GR length" claim at
both base points (`2 = 2` at `t=0`, `0 = 0` at `t=inf`).

So the honest price is higher than R1 states: the sectioned one-support row is
**inhabited**, not merely un-eliminated.  It cannot be closed by any argument
using only raw degree three, normality, generic smoothness, solubility, exact
level two, additive fibre topology, the Euler budget, the `T`/`D` row, `chi`,
or rationality — because an explicit surface satisfies all of them.

**What is still not purchased, and I checked none of it:** the proper-block
occurrence, i.e. an everywhere-defined dominant morphism `A^2 -> V` with
controlled full image.  The threat map is explicit that its rational-forest
pruning (0.3) and (4.2) are unavailable without exactly that, and that
rational domination does not license it.  Also unpurchased: the plane-net
polarization cluster `{m_j}` of threat-map Section 3, the good-resolution
graph of `p_0`, finite flatness/ramification data for the target projection,
resolved boundary topology, a polynomial map, and JC2.

## 8. Maximum-safe theorem

Let `R = C[[t]]`, `K = C((t))`, and

```text
Phi(t;x,y,z) = (x + t z)^3 + t y^3 + t^3 x^2 y  in  R[x,y,z].
```

Then, all clauses independently reconstructed in this review:

1. `Phi` is primitive with literal raw coefficient `t`-degree exactly three,
   attained at `x^2y` and `z^3`; `Phi mod t = x^3` is the triple line; and
   `Phi(-t,0,1) = 0`, so the generic plane cubic is `K`-soluble.
2. `Phi` is projectively equivalent over `K` to the Weierstrass ternary cubic
   `G = V^2W - U^3 + t^4W^3` by the exact identity
   `Phi(x,y,z) = t^3 G(-(x+tz)/t,\ t x,\ y/t^2)`, whose character is
   `mu det N = -t^2`.  Hence exactly
   `c4(Phi) = 0`, `c6(Phi) = 864 t^16`, `Disc(Phi) = -432 t^32`, i.e.
   `(v(c4),v(c6),v(Disc)) = (inf, 16, 32)`.
3. `V^2 = U^3 - t^4` is minimal (`v(c6)=4<6`) of Kodaira type `IV*` with
   `v(Disc)=8`.  Therefore the CFS level of `Phi` is **exactly two**
   (`(32-8)/12 = 2`, and independently `v(Disc(Phi_0)) = 8 < 12` forbids a
   further arrow), and `Phi` satisfies the promoted level-two gate through
   `v(c6) = 16 < 18` and threat-map (4.2) through `26 <= 32 <= 34`.
4. The descent is realized by the determinant-one shear `X = x + tz` followed
   by two admissible CFS moves `[mu,M] = [t^-3, diag(1,t,t)]` in the ordering
   `(z,X,y)`, each with `v(mu det M) = -1`, each verified integral with zero
   remainder modulo `t^3`, and the composite verified to have Smith normal
   form `diag(1,t,t)`, i.e. the pair `(a,b) = (1,1)`.
5. `{Phi = 0} subset P^2_R` is integral and normal.  Its generic cubic is
   geometrically smooth, and its complete total-space singular locus is the
   single point `t = 0`, `[x:y:z] = [0:0:1]`, of multiplicity three and
   codimension two.

Consequently the proposed local impossibility is **false**: literal raw
coefficient-base degree three, normality, generic smoothness, `K`-solubility,
exact CFS level two, the full admissible-pair menu, and an additive minimal
fibre do not jointly yield a local contradiction.

Nothing above asserts a proper-block occurrence, a polynomial map, or JC2, and
nothing above depends on the global addendum in Section 7.

## 9. Cheapest useful successor

One packet, because both halves need the same object — the minimal resolution
of the single germ `u^3 + t y^3 + t^3(u-t)^2 y` at the origin, where
`u = x + tz`.  Desk-scale; no AWS.

1. **Resolve `p_0` and read the plane-net cluster.**  Compute `r: Y -> Xbar`
   at `p_0` (the `A_2` at `p_inf` is already known and crepant), then the
   relative minimalization `h: Y -> S` onto the `IV* + IV` extremal rational
   elliptic surface.  Read off `{m_j}` and check
   `sum m_j = 6`, `M^2 = 3 + sum m_j^2`, `m_j <= 3`.  Because `Xbar` is an
   actual instance, whichever of the seven retained partitions occurs is
   **realized and can never be excluded**, which immediately prunes the
   threat-map Section 3.3 elimination strategy.  Confirm `p_g(p_0) = 2` and
   `rho(Y) >= 12` directly as controls against the Leray derivation above.
2. **Decide the only remaining lever.**  From the same resolution, extract the
   dual graph of `p_0` with component genera and cycles, and test the morphic
   rational-forest theorem.  If the graph is a rational tree, then the
   sectioned one-support row survives every filter the campaign currently owns
   except the proper-block first-leg morphism itself, and the row must be
   attacked with a genuinely new invariant rather than with level, degree,
   normality, or fibre topology.

Lower-priority but near-free: apply the two-line replay repair of Section 6 to
the R1 artifact, and restore the five dropped statements catalogued in
Sections 1, 2 and 5.

## 10. Firewalls and nonclaims

- This review asserts no exit price; `charge_basis_status=ABSENT` is correct.
- Section 7's global findings are my own unreviewed computation.  They are not
  charged, are not part of the R1 artifact, and must be independently
  re-derived before any promotion.
- I did not compute the good-resolution graph of `p_0`, the plane-net cluster,
  local `p_g` by a Newton-polyhedron route, ramification of the target
  projection, or resolved boundary topology.
- I did not establish, and do not claim, an everywhere-defined dominant
  morphism `A^2 -> V`, a proper-block occurrence, a polynomial map, or
  anything about JC2.
- The exhaustiveness of the CFS admissible-pair menu
  `(0,1),(1,1),(1,2),(2,3)` was **not** audited; it is not needed for the
  refutation, and no clause above relies on it.
- Kodaira symbols are taken from the residue-characteristic-zero Tate table;
  every one used here was cross-checked against the `y^2 = x^3 + t^n` family.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `26012`.
- Body SHA-256:
  `0df3ee27d58b4f23af65f0325ac7d647ee882c1960eb2c1875d3e7414df1d55a`.
- Frozen basis: `4f6e9c3d98f34f5280251358c319660c1d027335`.
