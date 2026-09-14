# Independent gauge audit for the repaired (99,66) charts

**Scope update:** the parent lane subsequently found a separate problem with
the strict h3 equality face. The branch recommendations at the end of this
note were conditional on that face audit and therefore are not final branch
verdicts. `face_minor_probe.py`, `face-minor-probe.json`,
`corrected_face_engine.py`, its complete `.patch`, and
`corrected-face-controls.json` now provide a diagnostic repair with
`[t^4 z^5]K3=-8/3` and the second equality coefficient free. Both exact minor
leader solves are consistent; the diagnostic engine's initial controls pass.

This note audits the frozen engine and precise replay. It does not adopt the
Opus/Sol interpretation of `"b0":"fixed_zero"`. The direct charged hashes
were verified by the parent lane before delegation. No input, ledger,
`jc2-lean`, or `ideation-*` file was modified. The executable identities are
`gauge_checks.py` and `gauge-checks.json` in this directory; the latter is PASS.

## Findings

1. Two independent source translations survive placement of the two infinity
   directions. The claim that there is only one constant source parameter is
   false. The two centre intercepts can both be set to zero with those two
   parameters. Freeing minor `jet0` is nevertheless a safe enlargement.
2. The remaining translation after centring the major direction is diagonal.
   It **does not change `Hc_11_0`**. That pin is not a legitimate second
   translation spend, and it is not the minor `jet0` pin in different notation.
3. Historical code used `Hc_11_0=0` as an ODE compatibility, whereas `b0` was
   the additive constant of a different polynomial `q1`. Conflation of the two
   is a variable/ring-map fallacy. A conditional ODE calculation survives
   `jet0` release, but the source licence for prolonging Xu's face equation to
   the actual global approximate root should not be assumed.
4. This disputed pin is dispensable at the stage-8 endpoint: it first enters
   `K3` at `t^11`, while both endpoints use `max_t=8`. Freeing it leaves all
   endpoint equations unchanged. Hence the parent lane can establish a
   gauge-correct delta=5/2 kill without the disputed ODE licence.

## Source translations: an explicit calculation

Use the pullback convention

```
T_(a,b)(x,y)=(x+a,y+b),  F_new=F o T_(a,b), G_new=G o T_(a,b).
```

Its determinant is 1, so the Jacobian scalar is unchanged. Constants do not
change either leading homogeneous form. In projective coordinates it is
`[X:Y:Z] -> [X+aZ:Y+bZ:Z]`, which is the identity on `Z=0`. Thus placing the
directions `y=0` and `y=x` cannot consume either source translation.

Write the old major expansion `y=x+A+alpha*x^(-1/3)+...` and the old minor
expansion `y=j+u*x^(-1)+v*x^(-2)+...`. Then the new intercepts are

```
A_new=A+a-b,                 j_new=j-b.
u_new=u,                    v_new=v-a*u  (delta=5/2).
```

Terms generated beyond the indicated radii are harmless tails of the same
generic points. The map `(a,b)->(a-b,-b)` has determinant -1. Taking
`b=j, a=j-A` sets both intercepts to zero. After setting `A=0`, the residual
subgroup is `T_(a,a)`, and it shifts `j` by `-a`. Consequently the pristine
absence of `jet0` and the centred major point are compatible source gauges;
the precise replay leaves this residual subgroup unused. The erroneous
one-translation reasoning in frozen Opus lines 99–102, 279–284 and frozen Sol
lines 72–85 does not invalidate the safe enlargement itself.

The original engine reconstructs the major coordinate as
`K_Q=t^D Q(t^-1,w/t)`, `z=w-1` (frozen `band_engine.py:459–460`), and the
pristine minor substitutions are encoded at lines 545–565. The precise
substitutions are recorded directly at `band_engine.py:316–327` and evaluated
in `local_rows` at lines 571–600.

## Why Hc_11_0 cannot be paid by the second translation

The template is frozen `band_engine.py:242–254`. Its lower basis term is

```
Hc_(r,d) t^r (w-1)^v w^(d-v),
v=ceil((33-3r)/4),  1<=r<=11,  v<=d<=11-r.
```

In source coordinates, after multiplication by `t^-11`, this is

```
Hc_(r,d) x^(11-r-d) (y-x)^v y^(d-v).
```

For every `r<=10`, `v>=1`. At `r=11`, the only term is `Hc_11_0`. The top
`y^3(y-x)^8` also vanishes on `y=x`. Therefore the exact polynomial identity is

```
h3(x,x)=Hc_11_0.
(h3 o T_(a,a))(0,0)=h3(a,a)=Hc_11_0.
```

This is checked symbolically from the complete template in `gauge_checks.py`.
The residual source parameter cannot normalize this coefficient to zero.
More invariantly, after centring an affine major line, `Hc_11_0` is the
constant value of `h3` on that line. Simultaneously translating the line and
the polynomial preserves that value. An arbitrary shift of `h3` would not be
a source translation either; `h3` is the uniquely depressed approximate root
inside `h2=h3^3+C2*h3+C3`, so such a shift introduces an `h3^2` term.

The pristine branch map imposes `(11,0):0` at lines 275–278 and calls it
`ODE_compatibility` at line 304. The precise map retains exactly that pin at
lines 293–298 and calls it ODE compatibility at line 327. Those executable
facts do not establish a source gauge. The precise module's opening comment
at lines 20–22 that this pin and `jet0=0` spend the same gauge is false.

## Complete normalization ledger

The table distinguishes genuine group choices from canonical polynomial
coordinates and imposed equations. It would be incorrect to demand a source
group parameter for a theorem-imposed equation or an invertible coordinate
change. Citations without another prefix are to the frozen charged
`band_engine.py`; precise citations are to the replay engine.

| Engine choice | Element or derivation | Parameter ledger and scope |
|---|---|---|
| Preliminary source-support recentring | `y -> y+eta(x)` from the support theorem, if needed before reaching the finite total-degree chart | This constructs a suitable polynomial source coordinate; `trace=0` is not an additional retained equation in this engine. Later affine transformations preserve finite total degree. |
| Directions `Lmin=y`, `Lmaj=y-x` | A triangular linear map `(x,y)->(x,lambda*y+mu*x)` sends two distinct finite slopes to 0 and 1 | One shear `mu` and one nonzero linear scale `lambda`. No translation spent. The top appears in the template at 243 and `P^3` at 364–366. |
| Leading coefficients of F and G equal 1 | Target scaling `(F,G)->(aF,bG)` with the inverse two nonzero top coefficients | Two independent target scales. The tower then has monic h2 and h3 automatically; there is no extra source spend for their monicity. `build_FG`:484–493. |
| `K2` D2 face `(pi^3-1)^8`, choosing the child root 1 | After top monicity, uniform source dilation with compensating target scales: `F_lambda=lambda^-99 F(lambda*x,lambda*y)`, `G_lambda=lambda^-66 G(lambda*x,lambda*y)` | If the unnormalized face is `(pi^3-beta)^8`, then `beta -> beta*lambda^-4`; choose `lambda^4=beta`, available over the algebraic closure. Selecting one conjugate child after that is a choice of generic-point representative. Equality coefficients:367. |
| Major constant centre zero | `T_(a,b)` with `a-b=-A` | One source-translation combination. Residual `T_(a,a)` is still available. It is harmless to use the convenient representative `(x,y)->(x,y+A)` and leave the residual combination unused. |
| Minor constant zero, pristine only | Residual diagonal `T_(a,a)` | One second, independent source-translation combination; the two pristine centre pins are compatible. Precise `jet0` free at 273–298 spends no parameter. |
| Delta=2 double root at `zeta=0` | A generic-point shift would be `zeta -> zeta+kappa`, but must also be propagated to the evaluated series `y=j+ut+(kappa+zeta)t^2` | Additional open audit item: the engine evaluates `y=j+ut+zeta*t^2` and sets the double root to 0 simultaneously. A generic-variable rename alone does not exhibit this as a source gauge. `rho` remains free with `rho!=0`; lines 258–268,289–296. The safe added parameter is tested in `face_minor_shift_probe.py`. |
| Delta=5/2 shape `pi(pi^2-c)` | The denominator-2 deck action gives `pi -> -pi`, hence an odd monic cubic with a fixed zero root and one ± pair | No extra parameter spend. In particular neither engine sets `c=1`; `c` is free and localized, 278,297–304 and precise 295–327. |
| `Hc_11_0=0` on delta=5/2 | No source group element exists after centring the major line | Unsupported as a source normalization. It may be derived from an additional ODE hypothesis, treated separately below. The robust endpoint fix is to release it. |
| No `h3^2` term in h2; no `h2^2` term in F | Characteristic-zero Tschirnhausen construction of the unique approximate roots; algebraically shift an intermediate root by one third of its offending coefficient and transform the remainder coordinates | Internal triangular coordinate definitions with `(F,G)` unchanged, not finite-dimensional source gauges. The chart reads `h2=h3^3+C2*h3+C3`, `F=h2^3+A2*h2+A3`, `G=h2^2+B1*h2+B2`. Predecessor frozen design lines 115–126; engine lines 307–388,484–493. |
| `K2c` output coordinates replace C2/C3, seven D1 pivots, subsequent rational pivots | Invertible unit-triangular output change and exact rational row elimination | No normalization of a group orbit. All inversions are in Q*, 191–239,314–361; parameter localizers are excluded by 749–750. |
| D2 and D1 support restrictions and faces | Equations of the source-licensed centred generic-point orders, with the exact face rather than equality inferred from a floor | No additional group spend. Template:242–254; h2:328–377; outer:392–470. Necessity is conditional on the centre/radius source audit performed by the parent lane. |
| Ramification `t=s^2`, D1 `t=e^9`, and `z=w-1` | Variable changes for the cover series and the placed major direction | No source-orbit normalization beyond the preceding direction placement. The coefficient of the generic variable can be set to 1 because that variable is indeterminate. |
| `rho!=0` or `c!=0` | Rabinowitsch localization `Zrho*rho-1` or `Zc*c-1` | An open-stratum condition, not a normalization; lines 608–663. No nonzero parameter is fixed numerically. |
| `jacobian_normalization_control` | A symbolic verification of the coordinate formula for J, lines 506–537 | Its name is misleading if read as a gauge: the engine imposes positive-degree Jacobian coefficients =0, not `J0=1`. Lines 666–722 only reach degree 155 at stage8. Thus uniform dilation used for the D2 face is not spent a second time on a Jacobian scalar. |
| Finite stage/pole truncations | Coefficient equations selected by `stage_spec`, with omitted equations left out | No parameter spend. Dropping equations gives a superset; removing unknown coefficients would need a separate theorem. Lines 666–746. |
| Target additive constants | `(F,G)->(F+eF,G+eG)` | Available, unused here. They do not alter the approximate-root constant H; each changes only the relevant outer constant term. |

The dilation formula deserves one explicit check. If
`K_D=t^D Q(t^-1,w/t)`, then its normalized pullback is
`K_D(t/lambda,w)`. A centre offset `alpha*t^(4/3)` becomes
`alpha*lambda^(-4/3)*t^(4/3)` and its cube `beta` becomes
`beta*lambda^-4`. The Jacobian scalar becomes `lambda^-163 J0`. Since the
engine uses only homogeneous equations `J_d=0` with `d>0`, every one of
those equations is preserved, whether or not the scalar is normalized.

## The historical b0 conflation and the conditional ODE

The historical driver treats two different variables:

* `c_11_0` is the last free degree-11 polynomial coefficient after imposing
  the minor leader. The source is
  `legacy/inputs/joint_probe.py:303–319,346–376` under the precise replay.
* `b0` is the additive constant of `q1`, a different polynomial in the split
  parameter. `legacy/inputs/xu_joint_extension.py:205–210` carries it freely.
  `legacy/inputs/joint_probe.py:470–478` explicitly records the separate
  optional additive-constant normalization and dimension count.

The original report even separates them at
`legacy/inputs/g9966-global-design-sol56-20260903.md:490–518`. The label
`"b0":"fixed_zero"` attached to the h3 map therefore does not identify
`Hc_11_0` with that additive constant. Matching labels are not a ring map.

The independent symbolic calculation with `j=jet0` and H restored gives

```
h3(s^-2,j+u*s^2+v*s^4+pi*s^5)
  = p/s + H-d*p' + O(s),
p=pi*(pi^2-c),   d=u^2-j^2*u+2*j*v,   H=Hc_11_0.
```

Assume, as an additional hypothesis, that there is a polynomial-coefficient
series `Q=q1+B1*s+...` satisfying the prolonged equation
`D_s(Q,h3)+2*s^2*h3^4=0`. Its `s^-1` coefficient is

```
(p*B1)' + 8*p^3*(H-d*p')=0.
```

The additive constant in q1 is absent. Integrating gives

```
p*B1 = 2*d*p^4 - 8*H*I + C,
I = pi^10/10 - 3*c*pi^8/8 + c^2*pi^6/2 - c^3*pi^4/4.
```

Polynomiality of B1 implies C=0 by setting pi=0. Reducing modulo
`pi^2-c` gives `H*c^5/5=0`, so H=0 on `c!=0`. This does not use the
historical artificial bound `deg B1<=18`. It is an exact algebraic implication
and it survives free `jet0` and free q1 additive constant.

However, Xu's printed p.13 gives the *face* equation in `q1` and `p*t^-1/2`.
The source-to-full-global-h3 prolongation is an additional identification.
The older local-lift report itself says it "imposed" the prolonged equation
(`xmodel/xu-delta52-lift-gpt55-20260903.md:182–194`). This note does not replace
a licence for that identification by prior-validator confidence. The parent
lane's H-free endpoint argument avoids the issue completely.

## Direct endpoint fix: release H rather than promote the ODE hypothesis

At delta2 stage4 the maximum pole local power is 8; at delta52 stage8 it is
16 in s. Both engines set `max_t=8` at these endpoints, from pristine lines
666–682,740–744 and precise lines 842–846. H enters K3 only as `H*t^11`.
Multiplication never lowers t-order, and `tz_mul` discards exponents beyond
`max_t` (129–135). Therefore H contributes to neither truncated h3cube nor
the high-q h2 output coordinates used at these endpoints. The seven initial
h2 D1 equations have weights 97/98, whereas the earliest possible H term in
high-q output has weight at least 121; the low-q output coordinates are
independent `K2c` variables. The minor h3 leader test stops at s21, before
the H contribution at s22.

One can consequently replace precise `(11,0):0` by free H, add H to the
delta52 free list, and change the inner count from 103 to 104. All endpoint
polynomial rows, the ordered rational pivot sequence, and the stage8 unit
identity stay exactly the same, now over the polynomial extension by H.
No row is inferred by specializing a variable. The proof establishes the
opposite direction: the full enlarged rows are H-independent before taking
the quotient. It contains the precise chart at H=0 and the pristine chart
at H=jet0=0.

Subject to the parent lane's independent centre/face and replay custody
audits, the gauge conclusions are:

```
delta=2:   CONFIRMED, with the ledger corrected to two source translations.
delta=5/2: CONFIRMED-WITH-FIX on the jet0-and-Hc_11_0-free chart.
```

The claim "retained H is the legitimate second source translation spend" is
REFUTED. That false rationale is separable from the branch kill because the
extra coefficient lies beyond every endpoint equation.

## Additional delta=2 at-level centre audit

The table's at-level caution is substantive. In an unshifted generic variable
the general two-root cubic is

```
p(zeta)=(zeta-a)^2*(zeta-a+3*rho),   rho!=0.
```

Equivalently one may require the displayed engine target
`zeta^2*(zeta+3*rho)` and evaluate the source at
`y=j+ut+(a+zeta)t^2`. One must change both the face and the source evaluation
under a generic-variable shift; renaming a symbol is not a second map.

`face_minor_shift_probe.py` performs exactly this latter evaluation on the
diagnostic repaired h3 face. It finds 18 rational pivots, zero residual, and
free h coefficients `Hc_10_1,Hc_11_0,Hc_7_4,Hc_8_3`, with free
`j,u,rho,a`. Thus the displayed major and minor leader equations do not force
a=0. The entire `face-minor-shift-probe.json` stores the resolved map and its
every-row symbolic recheck. This is an independent algebraic chart
coordinate, not an attained Keller pair.

Under the residual diagonal source translation, the unshifted coefficient
changes as `a_new=a-A*u` for translation parameter A. On `u!=0`, one may use
that residual parameter to set a=0 and retain j freely. On `u=0`, it does not
change a. No source-licensed normalization of the missing a=nonzero slice has
been supplied in these engines. The simplest safe implementation is to free
and propagate a without splitting. The diagnostic `corrected_face_engine.py`
keeps a=0, explicitly advertises this limitation, and has not been changed
after its parent-lane runs were launched. Its results cannot themselves close
that additional chart-coverage question.

Accordingly the earlier conditional branch recommendations in this note must
be read with both qualifications: the strict h3 face audit failed separately,
and the delta2 at-level normalization also needs coverage or release. The
final report, not this sub-audit, assigns the branch verdicts.
