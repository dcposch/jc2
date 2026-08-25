# Hostile ramified-arc audit: selected Q8 overlap, normal rank-drop line

Date: 2026-08-25  
Auditor: independent hostile algebraic geometer (Claude; separate from the Fitting/tangent Grok review and from the slope-three producer lane).  
Field: algebraically closed, characteristic zero.  
Question: does there exist a nonconstant formal or Puiseux arc in the pinned six-row source whose generic point lies in `D(w x5 (x3-2 x5))` and whose special point lies on the raw overlap `w=x1=x3=x5=0` along the normal rank-drop line `d2=d4+1`?  
Verdict: **NOT_CONFIRMED**.

The ordinary `delta w=1` theorem on the unloaded overlap, and the unramified slope-three obstruction in the chart `x5=t`, both survive as narrowly scoped statements. They do not decide the question. Slope two is impossible on the generic rank-drop line and is not impossible at the rank-one value `b=d4=1`. Slope three at `b=1` is a remaining leading candidate, not the only one. The residual `-108` does not exclude ramified or mixed-order branches, nor the unramified slope-two cone at `b=1`. A substitution `t |-> t^m` of the frozen continuation is not a ramification argument.

## 0. Scope, objects, and firewall

Ambient ring `Q[w,c,d2,d4,x1,x3,x5]`. Overlap `A3: (w,x1,x3,x5)`. Rank-drop support `d2-d4-1=0` inside `A3`. Write `b:=d4` along that line, so the line is `(d2,d4)=(b+1,b)` with `c` free. The rank-one point is `(d2,d4)=(2,1)`.

An arc means a nonconstant `k[[t]]`- or Puiseux `k[[t^{1/m}]]`-point of `V(I)` with:

- special point on `A3` and on `d2=d4+1`;
- generic point in the selected open `D(w x5 (x3-2 x5))`.

No terminal, no Taylor jet, no `e6,e8`, no coefficient-projective chart, and no global horizontal saturation is used as a theorem in this audit. Custody hashes and AWS stdout are cited only as coefficient witnesses for identities that are either re-derived by hand or named as the first missing expansion.

Explicitly not licensed by anything in the corpus, and not claimed here:

- a trajectory through the selected open;
- global `I:(w x5 (x3-2 x5))^infinity` emptiness;
- coefficient infinity;
- Taylor or terminal realization;
- `(9,12)`, maximum twelve, Keller, or JC2.

## 1. Exact six-row source

The pinned compiler `cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py` emits approximate-cubic coordinates `["w","c","d2","d4","x1","x3","x5"]` with imposed tuple `(1,3,5,7,2,4)`. Chart `k=0` is internal (monomials with `ek` are skipped). Both rank-drop generators refuse to emit unless that tuple and those names match. Frozen `input.sing` on the weighted, `b=1` slope-two, and slope-three V3 endpoints all write the eight approximate-cubic tails and then impose exactly

```text
SI = (se1, se3, se5, se7, se2, se4).
```

The unused tails `se6,se8` are compiled into the ring and never enter `SI`, any weighted initial, or any continuation jet. No generator adjoins `inv*w*x5*(x3-2*x5)-1`, a terminal, or a Taylor remainder as an equation. Selected factors appear only as saturators of already-formed initials, or as the open in which an arc is required to live.

The six imposed polynomials, copied from the frozen inputs, are

```text
e1 = -4/9*w*c*d4^2-8/9*c*x3*x5+4/3*c*x5^2+4/9*d2*x3-8/9*d2*x5
     +4/9*d4*x1-8/9*d4*x3-4/27*d4*x5^2+4/3*d4*x5+4/9*x5

e2 = 2/3*w*c^2*x5^2-8/9*w*c*d2*x5-8/9*w*c*d4*x3+8/3*w*c*d4*x5
     +2/9*w*d2^2-8/9*w*d2*d4-4/27*w*d4^2*x5+2/3*w*d4^2+4/9*w*d4
     +4/9*x1*x3-8/9*x1*x5-4/9*x3^2-4/27*x3*x5^2+4/3*x3*x5
     +20/81*x5^3-8/9*x5^2

e3 = 4/3*w*c^2*d4*x5-8/9*w*c*d2*d4+32/27*w*c*d4^2-4/81*w*d4^3
     -8/9*c*x1*x5-4/9*c*x3^2+64/27*c*x3*x5+20/81*c*x5^3-20/9*c*x5^2
     +4/9*d2*x1-20/27*d2*x3-4/27*d2*x5^2+28/27*d2*x5
     -20/27*d4*x1-8/27*d4*x3*x5+28/27*d4*x3+56/81*d4*x5^2
     -4/3*d4*x5+4/9*x3-20/27*x5

e4 = 14/27*w^2*c^2*d4^2+28/27*w*c^2*x3*x5-16/9*w*c^2*x5^2
     -20/27*w*c*d2*x3+16/9*w*c*d2*x5-20/27*w*c*d4*x1+16/9*w*c*d4*x3
     +56/81*w*c*d4*x5^2-28/9*w*c*d4*x5-20/27*w*c*x5
     -8/27*w*d2^2-8/27*w*d2*d4*x5+20/27*w*d2*d4+4/9*w*d2
     -4/27*w*d4^2*x3+52/81*w*d4^2*x5-4/9*w*d4^2-16/27*w*d4
     +2/9*x1^2-16/27*x1*x3-4/27*x1*x5^2+20/27*x1*x5
     -4/27*x3^2*x5+10/27*x3^2+52/81*x3*x5^2-8/9*x3*x5
     +5/243*x5^4-140/243*x5^3+14/27*x5^2

e5 = -4/9*w*c^3*x5^2+20/27*w*c^2*d2*x5+20/27*w*c^2*d4*x3-20/9*w*c^2*d4*x5
     -8/27*w*c*d2^2+32/27*w*c*d2*d4+16/27*w*c*d4^2*x5-76/81*w*c*d4^2
     -16/27*w*c*d4-4/27*w*d2*d4^2+16/81*w*d4^3
     -16/27*c*x1*x3+32/27*c*x1*x5+16/27*c*x3^2+44/81*c*x3*x5^2
     -152/81*c*x3*x5-224/243*c*x5^3+4/3*c*x5^2
     -4/9*d2*x1-20/81*d2*x3*x5+40/81*d2*x3+40/81*d2*x5^2-44/81*d2*x5
     -20/81*d4*x1*x5+40/81*d4*x1-4/27*d4*x3^2+88/81*d4*x3*x5
     -44/81*d4*x3+16/243*d4*x5^3-328/243*d4*x5^2+16/27*d4*x5
     +4/9*x1-4/9*x3-8/81*x5^2+40/81*x5

e7 = -8/81*w^2*c^3*d4^2-16/81*w*c^3*x3*x5+8/27*w*c^3*x5^2
     +20/81*w*c^2*d2*x3-44/81*w*c^2*d2*x5+20/81*w*c^2*d4*x1
     -44/81*w*c^2*d4*x3-164/243*w*c^2*d4*x5^2+8/9*w*c^2*d4*x5
     +20/81*w*c^2*x5+16/81*w*c*d2^2+16/27*w*c*d2*d4*x5-40/81*w*c*d2*d4
     -8/27*w*c*d2+8/27*w*c*d4^2*x3-104/81*w*c*d4^2*x5+208/729*w*c*d4^2
     +32/81*w*c*d4-8/81*w*d2^2*d4+8/27*w*d2*d4^2+8/243*w*d4^3*x5
     -52/243*w*d4^3-4/81*w*d4^2
     -4/27*c*x1^2+32/81*c*x1*x3+20/81*c*x1*x5^2-40/81*c*x1*x5
     +8/27*c*x3^2*x5-20/81*c*x3^2-304/243*c*x3*x5^2+416/729*c*x3*x5
     -40/729*c*x5^4+820/729*c*x5^3-76/243*c*x5^2
     -4/27*d2*x1*x5+4/27*d2*x1-8/81*d2*x3^2+136/243*d2*x3*x5
     -100/729*d2*x3+8/243*d2*x5^3-140/243*d2*x5^2+92/729*d2*x5
     -4/27*d4*x1*x3+112/243*d4*x1*x5-100/729*d4*x1+8/27*d4*x3^2
     +8/81*d4*x3*x5^2-296/243*d4*x3*x5+92/729*d4*x3
     -152/729*d4*x5^3+2368/2187*d4*x5^2-28/243*d4*x5
     -4/27*x1-8/81*x3*x5+4/27*x3+40/243*x5^2-100/729*x5
```

Every monomial of every imposed row carries a positive power of `w` or of an `x`-variable, so the six rows vanish on `A3`. That is the raw overlap, not a hidden load.

## 2. Leading forms used by the weighted analysis, by hand

Write `d4=b+delta4`, `d2=b+1+u`, with `v(u)>0` and `v(delta4)>0` along any arc landing on the drop line. The `A3`-linear part of `e1` rewrites exactly as

```text
(4/9) [ b x1 + (1-b)(x3-x5) + delta4 x1 + u (x3-2 x5) + delta4 (-2 x3 + 3 x5) ]
- (4/9) w c d4^2  +  (quadratic in x).
```

The displayed selected factor `x3-2 x5` occurs as the coefficient of `u`. Restricting to the drop (`u=delta4=0`) gives the four odd linear forms

```text
e1_lin = (4/9)  [ b x1 + (1-b)(x3-x5) ]
e3_lin = (4/27) [ (3-2b) x1 + 2(b-1)(x3-x5) ]
e5_lin = (4/81) [ b x1 + (1-b)(x3-x5) ]
e7_lin = (8/729)[ b x1 + (1-b)(x3-x5) ].
```

Thus `e1,e5,e7` are proportional on the drop, and `e3` is independent of that common form if and only if `b != 1`. (The identity `3-2b = lambda b` and `-2(1-b)=lambda(1-b)` forces `lambda=-2` then `3=0`.) At `b=1` every odd row reduces to a unit times `x1`. This is the rank drop: generic rank two, rank one at `(d2,d4)=(2,1)`.

The even `w`-derivatives on `A3` are the tangent-package polynomials. Substituting `d2=b+1`, `d4=b` yields the constant identities

```text
L2 := e2_w |_{A3, drop} = 2/9,
L4 := e4_w |_{A3, drop} = 4/27.
```

(The `b`-linear and `b`-quadratic terms cancel; first missing identity if these constants fail is a monomial in the expansion of `e2_w` or `e4_w` along `d2=d4+1`.) In particular `L2` is the nonzero constant `2/9` at every `b`, including `b=1`. The first-order correction is

```text
L2 = 2/9 + (4/9)(1-b)(u - delta4) + quadratic(u, delta4).
```

At `b=1` the linear correction in `(u,delta4)` vanishes.

The `w=0` quadratic of `e2` factors identically,

```text
Q2 = (4/9)(x3-2 x5)(x1 - x3 + x5).
```

The `w=0` cubic of `e2` is `(4/81) x5^2 (5 x5 - 3 x3)`. On the generic kernel `x1=0`, `x3=x5` this cubic is `(8/81) x5^3`.

The `w=0` quadratic of `e4` is

```text
Q4_2 = 2/9 x1^2 - 16/27 x1 x3 + 20/27 x1 x5 + 10/27 x3^2 - 8/9 x3 x5 + 14/27 x5^2.
```

These are the only leading pieces the Rees screens can see. The weighted generator substitutes

```text
w = t^m W,  d2 = b+1+t U,  d4 = b,  x1=t X1,  x3=t X3,  x5=t X5
```

over `Q(c,b)`, divides each row by the highest power of `t` that divides it identically as a polynomial, specialises `t=0`, and saturates by `W X5 (X3-2 X5)`. That procedure has three structural defects, not software defects:

1. `d4` is frozen at `b`, so `delta4`-drift is absent.
2. The identical-power division does not refine extra vanishing on a kernel (if `Q2` is not the zero polynomial, `e2` is divided only by `t^2` even when `Q2` vanishes on the kernel of the odd rows).
3. Saturating the initial ideal by the leading load discards the component `X3=2 X5` of the special fibre; an actual selected arc may have `v(x3-2 x5) > v(x5)` with the factor nonzero at higher order.

The printed generic screens are therefore routing evidence for those equal-weight charts, not a list of all leading systems. Both engines give the same bases: `m=1,2` unit; `m=3,...,8` equal to `(X1, X3-X5)`. The `m=2` kernel identity `E2in ≡ (2/9) W mod (U,X1,X3-X5)` is the polynomial fact `Q2|_ker=0` plus `L2=2/9`, and is proved by hand below.

## 3. Valuation ratios, without `ord(x5)=1`

Let `v` be the `t`-adic valuation of a Puiseux expansion, scaled so that `v(t)=1` after a finite ramification of the parameter (every formal branch over an algebraically closed field of characteristic zero is Puiseux, so there is no leftover irrational face). Set

```text
α = v(x5) ∈ (0,∞),     β = v(x3) ∈ (0,∞],     γ = v(x1) ∈ (0,∞],
μ = v(w) ∈ (0,∞),      σ = v(u) ∈ (0,∞],      τ = v(delta4) ∈ (0,∞],
ρ = v(c-c(0)) ∈ (0,∞].
```

Selected open: `μ,α,v(x3-2 x5)` all finite. Write `κ := min(α,β,γ) > 0` and `δ_sel := v(x3-2 x5) ≥ min(α,β)`, with strict inequality iff `β=α` and the leading coefficients satisfy `η=2 ξ`.

### 3.1 The even constraint from `e2`

The pure-`w` summand of `e2` has valuation exactly `μ` on the drop, because its coefficient specialises to `2/9 ≠ 0`. Terms `w·(u,delta4,x)` have valuation at least `μ+min(σ,τ,κ) > μ`. Hence

```text
v(e2) = min( μ,  v(Q2),  v(cubic_x),  higher ).
```

Now `v(Q2) = δ_sel + v(x1-x3+x5) ≥ 2κ`, and `v(cubic_x) ≥ 3 min(α,β)`. A unique lowest summand cannot vanish. Therefore `μ ≥ 2κ`. In particular there is no selected arc with `μ < 2κ`. This includes every ordinary first-order lift with `μ=κ` (the Fitting/`delta w=1` face on the drop): it is excluded independently by `L2=2/9 ≠ 0`, which is the same identity as `K2=K1=K0=(1)` on the drop. That is the ordinary theorem, and only that.

### 3.2 Odd rows at order `κ`

The odd `w`-terms have valuation `μ ≥ 2κ > κ`. Drift terms `u·x` and `delta4·x` have valuation at least `σ+κ` and `τ+κ`. If `σ≥κ` and `τ≥κ`, they start at order `≥ 2κ`. Thus at order `κ` the odd rows are exactly the linear forms of §2.

- If `b ≠ 1`, those forms cut the kernel `X1=0`, `X3=X5`. A nonzero leading `(X1,X3,X5)` in that kernel forces `α=β=κ`, equal leading coefficients `ξ=η ≠ 0`, and `γ > κ`. The selected factor does not cancel: `x3-2 x5 ~ -ξ`, so `δ_sel=κ`. (The competing leading `η=2ξ` would require `X3=2 X5`, contradicting `X3=X5` unless `ξ=0`.)
- If `b=1`, the kernel is only `X1=0`, so `γ>κ`, while `(α,β)` remain free at this order.

If `σ<κ` or `τ<κ`, coefficient motion occurs on `A3` before the first normal lift. Equations on `A3` are tautological, so this is a genuine jet of `(c,d2,d4)` along the overlap, not a reparametrisation of the special point. It is a ramified (relative to `x5`) family and is not present in any frozen chart that freezes `d4=b` and sets `u=t·(order-α)`.

### 3.3 Generic `b ≠ 1`, after the kernel

On `X1=0`, `X3=X5` the quadratic `Q2` vanishes at order `2κ`. The next `e2` faces are `μ` against `κ+min(γ,ν)` (the extra vanishing of `Q2`, with `ν:=v(x3-x5)>κ`) against the cubic `8/81 ξ^3` of valuation `3κ`. The cubic leading coefficient is nonzero. Hence `μ ≤ 3κ`, so

```text
μ ∈ { 2κ }  is impossible: Q2 vanished and the cubic is strictly later,
μ ∈ (2κ, 3κ) is impossible unless min(γ,ν) lands in between and cancels w,
μ = 3κ     is the only remaining generic equal-order face.
```

The printed generic Rees bases `m=3,...,8` equal to `(X1,X3-X5)` are the unrefined identical-power initials (defect 2 above). They do not license slopes `> 3`. The cubic forbids `μ>3κ` on this kernel provided `σ,τ ≥ κ`.

Slope two at generic `b` is therefore empty on `D(W)`: `e2` reduces to `(2/9) W`. This is the preregistered `generic_slope2_e2_identity`, now a hand identity, and it is why both engines print `weight_m=2 loaded_initial_empty=1`.

### 3.4 The value `b=1`, slope two, by hand

At `b=1` the odd order-`κ` condition is only `X1=0`. Take the equal-weight face `μ=2κ`, `α=β=κ`, `σ≥κ`, `τ≥κ`. Then `e2` and `e4` at order `2κ` are

```text
(2/9) W + Q2(0,X3,X5) = 0,
(4/27) W + Q4_2(0,X3,X5) = 0,
```

with cubics and `w·x` strictly later. Explicitly

```text
Q2(0,X3,X5) = (4/9)(X3-2 X5)(X5-X3),
```

so `W = 2 (X3-2 X5)(X3-X5)`. Substituting into the `e4` conic and clearing `27` produces

```text
18 X3^2 - 48 X3 X5 + 30 X5^2 = 0,
(3 X3 - 5 X5)(X3 - X5) = 0.
```

The factor `X3=X5` gives `W=0`, excluded by `D(W)`. The factor `X3=5/3 X5` gives `W=-4/9 X5^2`. On `D(X5)` one has `X3-2 X5=-1/3 X5 ≠ 0` and `W ≠ 0`. Cubics in `x` have valuation `3κ>2κ`, so they do not disturb this initial. This is exactly the printed `b=1` slope-two basis

```text
( 3 X3 - 5 X5,  X1,  4 X5^2 + 9 W )
```

of both engines. Slope two is therefore not impossible at `b=1`. It is a nonempty selected leading cone.

(The same two conics kill the unequal faces `β<α` and `α<β` at `b=1`: `(X3,X5)=(η,0)` and `(0,ξ)` produce incompatible values of `W` from `e2` and `e4`. First missing identity if an unequal face survives is a cancellation of `Q2` at those axes coming from a term not in `Q2`.)

### 3.5 Slope three is not the only remaining leading candidate

The slope-three continuation chart is the equal-weight refinement

```text
d4 = b,
d2 = b+1 + Q1 t,
x5 = z t + Z2 t^2,
x3 = z t + X2 t^2,
x1 = U2 t^2,
w  = W t^3,
```

i.e. `α=β=1`, `γ≥2`, `σ=1`, `τ=∞`, `μ=3`, common leading `z`. On `D(z)` the two exact-Q engines, after saturating the coefficient ideal by `z`, print a Groebner basis mutually containing

```text
( b-1,  U2,  3 Q1 - (3c-1) z,  3(X2-Z2)+z^2,  9 W - 2 z^3 ).
```

Hand checks on this locus, not a full derivation of the ideal:

- `e1` at `t^1` vanishes on the kernel.
- `e1` at `t^2` is `(4/9)b U2 + (4/9)(1-b)(X2-Z2) - (4/9) Q1 z + (4/9)c z^2 - (4/27)b z^2`, and this is identically zero on the displayed generators.
- `e2` at `t^3` is `(2/9)W - (4/9) z (U2-X2+Z2) + 8/81 z^3`. On the displayed generators this forces `W=2 z^3/9`, i.e. `9W-2 z^3=0`.
- Deep contact `X2=Z2` (cubic versus `w` with `Q2` still higher) would give `W=-4/9 z^3`, which is incompatible with `3(X2-Z2)+z^2=0` on `D(z)`. So that face is not in this chart.

The first missing identities for a hand proof that the coefficient ideal equals the displayed five generators are the `t^2` coefficient of `e3` (linear plus quadratic plus the `u`-correction `(8/27) Q1 z`, which does cancel the leftover at `b=1`) and the `t^3` coefficient of `e4`. The AWS two-engine containment is the computational witness, not a hand GB.

Even granting that identity, the chart does not exhaust leading candidates. Remaining, after §3.1--3.4:

1. The `b=1` slope-two cone of §3.4, including its unramified realisations with `α=1`.
2. Arcs with `σ < α` or `τ < α` (coefficient / `u` motion before `x5`), of arbitrarily large ramification index `α/σ`.
3. The selected-factor face `η=2ξ` at `b=1` (`δ_sel > α`), which the Rees saturator deletes from the initial and which the slope-three chart never imposes.
4. Early `c`-jets (`ρ < α`) mixing into the quadratics.

Item 1 already falsifies “slope three at `b=1` is the only remaining leading candidate.” Items 2--4 are the ramified gap.

## 4. The residual `-108` does not exclude ramified arcs

### 4.1 What the unramified continuation actually computes

After the leading chart, the V3 continuation freezes `x5=t` exactly and substitutes

```text
c    = c + C1 t,
d4   = 1 + B1 t + B2 t^2,
d2   = 2 + (B1 + c - 1/3) t + (B2 + Q2) t^2,
x3   = t - t^2/3 + X3 t^3,
x1   = U3 t^3,
w    = 2/9 t^3 + W4 t^4.
```

It extracts the `t^3` coefficients of `e1,e5,e7` only. Both engines print

```text
C1e =  4/81 c + 4/9 C1 - 4/9 Q2 + 4/9 U3 + 4/81
C5e = -104/729 c + 4/81 C1 - 4/81 Q2 + 4/81 U3 - 4/27 B1 - 20/243
C7e =  332/6561 c + 8/729 C1 - 8/729 Q2 + 8/729 U3 + 4/81 B1 - 232/6561
```

and `continuation_unit=1`, `third_residual=-108`.

Hand expansion of `e1` along this map, modulo `t^4`, gives `C1e` identically (the `t^1` and `t^2` coefficients cancel by the leading chart; `X3` and `B2` cancel at `t^3`; `W4` does not enter `e1` at `t^3`). Setting `A:=C1-Q2`,

```text
C1e = (4/81) ( 9(A+U3) + c + 1 ),
C5e = (4/729) ( -26 c - 27 B1 + 9(A+U3) - 15 ),
C7e = (4/6561)( 83 c + 81 B1 + 18(A+U3) - 58 ),
```

the last two by matching the printed coefficients to the preregistered `P5,P7` (nonzero scalars). The first missing identities for a fully hand `e5`/`e7` expansion are those two `t^3` substitutions. Granting the printed coefficients, `P1=P5=0` force `B1=-c-16/27`, and then

```text
P7 = 83 c + 81(-c-16/27) + 2(-c-1) - 58 = -108.
```

The constant `-108` is an elementary linear combination. The three-row coefficient ideal is the unit ideal. There is no `k[[t]]` continuation of this slope-three jet with `x5=t`.

Rows `e2,e3,e4` are unnecessary for emptiness once those three coefficients already generate `(1)`.

### 4.2 `x5` is a local parameter only in this chart

The continuation sets `x5=t` as a power series of order one. That licenses `x5` as a uniformiser of the parameter DVR, and licenses the Weierstrass reparametrisation that kills a `t^2` term in `x5`. It does not license `x5` as a uniformiser of an arbitrary branch through the drop.

A substitution `t |-> t^m` of a nonexistent unramified solution produces nothing. The subclass of ramified series obtained by substituting `t |-> t^m` into a solution of the frozen chart would indeed carry the same residual, hence is empty. That subclass is characterised by every valuation being a multiple of `v(x5)`. It is not the set of all Puiseux arcs.

Missing mixed-order branches, already forced into existence as leading cones or as valuation faces:

**(R1)** Unramified over `x5`, wrong slope. The `b=1` slope-two cone with `α=1`,

```text
x5 = z t,   x3 = (5/3) z t + O(t^2),   x1 = O(t^2),
w  = -4/9 z^2 t^2 + O(t^3),   d4 = 1 + O(t),   u = O(t).
```

Here `x5` is a local parameter, the branch is unramified over the `x5`-disk, and the continuation map of §4.1 never applies because it locked `μ=3`, `W=2/9`. The residual `-108` is silent.

**(R2)** `u` as uniformiser, `x5` ramified. After scaling so that `min(μ,α,β,γ,σ,τ,ρ)=1`, the remaining faces with `α≥2` include `σ=1`:

```text
u = t,   x5 = ξ t^m + ···  (m≥2),   x3 = ξ t^m + ···,
x1 = O(t^{m+1}),   w = O(t^{2m}) or O(t^{3m}),
```

possibly with `d4=b+O(t)` and `c=c(0)+O(t)`. Then `u = (x5/ξ)^{1/m}` does not lie in `k[[x5]]`. The branch is ramified over `x5` of index `m`. No finite list of substitutions `t |-> t^N` in the frozen `x5=t` chart produces these series.

**(R3)** The same with `τ=1` (`d4`-uniformiser) or `ρ=1` (`c`-jet first), `α≥2`.

**(R4)** Selected-factor higher contact `v(x3-2 x5)>α` at `b=1`.

The index `m` in (R2)--(R3) is unbounded. A finite list of ramification indices is not a proof.

### 4.3 Unit changes in the leading coefficient of `x5`

The leading chart already contains a free unit `z`. The relations `X2-Z2=-z^2/3` and `W=2 z^3/9` are weighted-homogeneous. Setting `s=z t` gives

```text
x5 = s,   x3 = s - s^2/3 + ···,   w = (2/9) s^3 + ···,
```

so a unit leading coefficient is absorbed by scaling the parameter. After that normalisation the three `t^3` equations are the displayed `P1,P5,P7` and do not depend on a leftover `z`. Unit changes do not alter the unramified obstruction and do not create new ramified families.

A non-unit change — `x5 = z t^m` with `m≥2`, or a series for `x5` whose order does not divide `v(u)` — is not a unit change. That is (R2).

## 5. Smallest finite exact successor

A finite list of weighted charts indexed by ramification index cannot close (R2)--(R3). The Newton faces of a polynomial ideal in `(w,u,x1,x3,x5)` are finite, but the correct object cutting all of them at once is saturation of `I` by the selected load. That is already the preregistered primary mode of the loaded-Rees case, and it was not run: that directory contains only `weighted` and `weighted_b1` endpoints.

Saturation suffices, and is the unique smallest finite exact certificate, because a selected formal or Puiseux arc is a DVR point of `V(I) ∩ D(Load)` whose specialisation lies on `L=(w,u,x1,x3,x5)`. Equivalently it is a point of `V(I : Load^∞) ∩ V(L)`. Emptiness of that scheme is a unit Groebner basis. Non-emptiness is a finite reduced basis, which is then the exact survivor (to be rebuilt at exceptional coefficient strata, not treated as failure).

Parametric coefficient fields `Q(c,b)` drop the loci where leading coefficients in `(c,b)` vanish. The preregistration already isolated `b=1` for that reason. The mathematically honest ring therefore keeps `c` and `b` as variables.

**Computation (two exact-Q AWS shards, fail-closed, no terminal, no `e6,e8`, no localiser equation).**

Source: the same six rows, specialised by `d2=b+1+u`, `d4=b`. Load `Q = w x5 (x3-2 x5)`. Landing centre `L=(w,u,x1,x3,x5)`.

- Shard G (generic line, `c,b` variables):

```text
ring S = 0, (c,b,w,u,x1,x3,x5), dp;          // twin: slimgb / (dp(5),dp(2))
ideal I = phi(SI);
list LS = sat(I, Q);  ideal Csel = LS[1];
ideal Tsel = Csel, w, u, x1, x3, x5;
ideal GTsel = engine(Tsel);
certificate: reduce(1, GTsel) == 0,  or print the reduced basis of GTsel.
```

- Shard B1 (rank-one value; do not infer from Shard G):

```text
ring S1 = 0, (c,w,u,x1,x3,x5), dp;           // twin: slimgb / block
// d4=1, d2=2+u
same saturation and landing, with b specialised to 1.
```

Unit certificate on both shards empties every selected formal/Puiseux/ramified arc through the drop line (Shard G) and through `(d2,d4)=(2,1)` (Shard B1), for all finite `c`. A nonunit basis is the survivor scheme in `(c,b)` or in `c`. If a generator of `GTsel` involves only `(c,b)`, those coefficient strata are the exceptional rebuild list; they are not a license to quote emptiness.

The already-coded `generate.py --mode loaded` is Shard G over `Q(c,b)` rather than over `Q`. That is acceptable as a generic emptiness test if and only if Shard B1 is run independently and the printed generic basis is not promoted across poles in `(c,b)`. Prefer the two rings above.

Do not accept a weighted `m=1..N` screen as a substitute: `N` is not a bound on `α/σ`.

Cheaper negative controls, not replacements: the next-order coefficient ideal of the `b=1` slope-two chart

```text
w=t^2 W, u=t U, x1=t X1, x3=t X3, x5=t X5, d4=1, d2=2+t U
```

on the open `D(X5 (3 X3-5 X5))` after imposing the initial `(X1, 3 X3-5 X5, 9 W+4 X5^2)`, extracting coefficients of `t^{κ+1}` in the six rows, and testing unit. That decides (R1) only.

## 6. Separation of theorems

| Statement | Status in this audit | First missing identity if granted too widely |
|---|---|---|
| Ordinary `delta w=1` on raw `A3`: exact rank-three incidence is the reduced line `d2=d4=0`; ranks `2,1,0` contribute no such tangent; rank-drop scheme is `(d2-d4-1)^2`; branch `(4,2)` has residual `729 L7=-432` | Licensed by the Fitting/tangent package and the Grok review §§2--7. Independent of ramification. | A nonzero ordinary horizontal tangent on the drop, i.e. a failure of `L2=2/9` |
| Generic slope two on the drop is empty on `D(W)` | Hand, §3.3 | A kernel vector with `Q2` nonzero or `L2=0` |
| `b=1` slope-two leading cone is nonempty and selected | Hand, §3.4, matching both `weighted_b1` engines | An odd quadratic at order `2κ` cutting `(3 X3-5 X5, X1, 9W+4 X5^2)` to the load |
| Slope-three leading chart on `D(z)` with `σ=α=1`, `τ=∞`, `γ≥2` forces `b=1` and `W=2 z^3/9` | AWS two-engine ideal identity; `e1` `t^2` and `e2` `t^3` checked by hand on the locus | `t^2(e3)` or `t^3(e4)` off the displayed generators |
| No `k[[t]]` continuation of that jet with `x5=t`; residual `-108` | `e1` `t^3` by hand; `e5,e7` by printed coefficients and the linear combination `P7 ≡ -108 (mod P1,P5)` | The raw `t^3` expansions of `e5` and `e7` |
| Unit leading `z` is absorbed and does not change `P1,P5,P7` | Hand, §4.3 | A non-homogeneous leftover in those three polynomials |
| Every ramified or mixed-order selected arc through the drop is empty | **Not proved** | A unit selected landing, or a theorem forcing `σ,τ,ρ ≥ α` and killing slope two at `b=1` |
| Full finite horizontal saturation `I:(w x5 (x3-2 x5))^∞` on the whole ambient | Not computed in the corpus used here | The saturation itself |
| Coefficient-projective infinity | Not in scope | A chart at `c=∞` or `b=∞` |
| Taylor / terminal realisation | Not in scope | A terminal row or a Taylor remainder in `I` |
| Trajectories, max-twelve, JC2 | Not in scope | Any of the above plus a global selected emptiness |

The Fitting sentence that “the ordinary first-order overlap is exhausted” is true for ordinary `delta w=1` and false for arcs. The slope-three producer paragraph that the residual is “not yet a general ramified-arc exclusion” is correct and is the bound of that theorem.

## 7. Defects in the frozen rank-drop packages, relative to the question

None of these is a source-identity error.

1. The weighted Rees screens freeze `d4=b` and equalise `wt(u)=wt(x_i)=1`. They cannot see (R2)--(R3). Their `m≥3` bases are unrefined kernels, not slope existence.
2. Saturating initials by `W X5 (X3-2 X5)` deletes the selected-factor face (R4).
3. The `loaded` mode of the same generator, which would have been the correct successor over `Q(c,b)`, has no endpoint in that case directory.
4. The slope-three continuation is honest about `ord(x5)=1` and then, in the remaining-gate sentence, points at “the separately running full `b=1` selected saturation”. That saturation is not a theorem in the files this audit was instructed to use. It is the computation of §5.

No repair of producer prose converts `-108` into a ramified exclusion.

## 8. Verdict

The six-row source is `(e1,e3,e5,e7,e2,e4)` on the raw overlap, with `e6,e8` unused and with no hidden load or terminal. Ordinary `delta w=1` tangents do not exist on the rank-drop line. Generic slope two is empty. At `b=1`, slope two has a nonempty selected leading cone `(X1, 3 X3-5 X5, 9 W + 4 X5^2)`. A slope-three leading jet on `D(z)` with `v(u)=v(x5)=1` lives only at `b=1` and has no unramified continuation `x5=t`; the residual `-108` is a correct linear combination in that chart. Unit leading coefficients of `x5` are absorbed. Mixed-order Puiseux branches with `v(u)<v(x5)`, `d4`-first or `c`-first jets, the unramified slope-two cone, and selected-factor higher contact remain. The remaining formal-arc question at the raw Q8 overlap along the rank-drop line is therefore open.

NOT_CONFIRMED

Narrowest exact next computation: the two-shard selected landing of §5 (Shard G in `Q[c,b,w,u,x1,x3,x5]` and Shard B1 in `Q[c,w,u,x1,x3,x5]`), source `I=(e1,e3,e5,e7,e2,e4)` specialised by `d2=b+1+u`, `d4=b` (resp. `b=1`), saturator `w x5 (x3-2 x5)`, certificate `reduce(1, engine(Csel+(w,u,x1,x3,x5)))==0` on mirrored exact-Q `std/dp` and `slimgb/block` lanes, or a printed reduced survivor basis. That is the smallest finite exact computation that can empty every selected formal or Puiseux arc through the drop, ramified or not.
