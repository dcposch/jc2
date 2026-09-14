# FIRST gate: radial Euler ring/conductor descent control (Fable 5.1)

Lane `radial-euler-descent-gate-fable5-20260912`. Different-model hostile
FIRST of the completed ROOT manual proof
`xmodel/radial-euler-descent-control-root-20260912.md`. First action
2026-09-12T13:17:57Z; reserve 13:28Z, hard 13:31Z (never reset). Manual
reconstruction only: no interpreter, CAS, helper, network, agent, corpus,
protected tree, live peer output or literature import. Result stays
PROVISIONAL; no JC2 conclusion is asserted; no charge_basis declared.

## Custody

Inputs read WHOLE and unclipped from `/tmp/jc2-lane.c5IrpP/inputs`,
COORDINATION first. Both SHA-256 match the expected pins:

- `COORDINATION.md`
  `33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597`
- `radial-euler-descent-control-root-20260912.md`
  `08423d2cc779e1f655336ef0342f74d5fe1f88ab4aa4b3114a0294c499031979`

## A. Actual radial map and fields

Reconstructed from scratch with `p=x^3`, `q=y/(3x^2)+(4/3)x+(10/9)x^2`,
`T=xy/6-x^4/3-4x^5/9`, `R=C[x,x^-1,y]`, `alpha=(x dy-y dx)/2`.

- `J(p,q)=p_x q_y-p_y q_x=3x^2*(1/(3x^2))-0=1`. CONFIRMED.
- `q_x=-2y/(3x^3)+4/3+(20/9)x`, `q_y=1/(3x^2)`, so
  `p dq=(-2y/3+(4/3)x^3+(20/9)x^4)dx+(x/3)dy` and
  `alpha-p dq=(y/6-(4/3)x^3-(20/9)x^4)dx+(x/6)dy`. `T_x=y/6-(4/3)x^3-(20/9)x^4`,
  `T_y=x/6`: the identity `dT=alpha-p dq` is exact. CONFIRMED.
- Pole: `3x^2 q=y+4x^3+(10/3)x^4` has constant term `y` along `x=0`, so `q`
  has a genuine order-2 pole there and is not in `C[x,y]`; it lies in `R`
  only because `x` is inverted. Nothing full-plane is used. CONFIRMED.
- Inverse formulas: `x^3=p`, `x^4=px` give `y=3x^2 q-4p-(10/3)px` and
  `x^-1=x^2/p`. Hence `A[X]->R`, `X->x`, is surjective. CONFIRMED.
- Injectivity (ROOT's sentence is terse; I supply the step). `J!=0` makes
  `p,q` algebraically independent, so `A=C[P,P^-1,Q]` and `Frac A=C(p,q)`
  with `p` of `p`-adic valuation 1, not a cube; a cubic without a root is
  irreducible, so `X^3-p` is irreducible over `C(p,q)`. Thus `1,x,x^2` are
  `C(p,q)`-linearly independent inside `C(x,y)`, and `C(p,q)(x)` contains
  `y` by the inverse formula, so `[C(x,y):C(p,q)]=3`. An `A`-relation
  `a0+a1x+a2x^2=0` forces `a0=a1=a2=0`: `R=A[X]/(X^3-p)`, free of rank 3.
  Etale since `3x^2` is a unit of `R`. CONFIRMED.
- `R=C[x,x^-1,q]` because `y` is an `x`-polynomial in `q`. CONFIRMED.
- `pq/2=xy/6+(2/3)x^4+(5/9)x^5`; subtracting `T` gives `x^4+x^5`; dividing
  by `p` gives `tau=x+x^2`. `x(tau+1)=x^3+x^2+x=p+tau`. `tau+1=x^2+x+1` is a
  nonzero element of the domain `R`, so `x=(tau+p)/(tau+1)` lies in
  `Frac B`, then `y` does, so `Frac B=C(x,y)` directly. `B=A[T]=A[tau]`
  since `T=pq/2-p tau` with `p` a unit of `A`. CONFIRMED.

Verdict A: CONFIRMED, every displayed identity replays; one omitted
linear-independence sentence, supplied above, not a gap.

## B. Graph, singular support and exact conductor

- Cubic: `tau^3=x^3+3x^4+3x^5+x^6=p+3px+3px^2+p^2`, `3p tau=3px+3px^2`, so
  `W=tau^3-3p tau-p-p^2=0`. CONFIRMED.
- Minimality and kernel: `tau=0*1+1*x+1*x^2` has nonzero coordinates in the
  free basis, so `tau` is not in `C(p,q)`; degree 3 is prime, so
  `C(p,q)(tau)=C(x,y)` and the monic cubic `W` is the minimal polynomial.
  Any `f` in `A[Z]` with `f(tau)=0` has a remainder of degree at most 2 mod
  the monic `W`, which vanishes at `tau`, hence is 0. Kernel is exactly
  `(W)`; `B=A[Z]/(W)` is the graph ring. CONFIRMED.
- Normalization: `R` is generated over `A`, hence over `B`, by `1,x,x^2`,
  so finite; `R` is a localization of `C[x,y]`, hence regular and normal;
  same fraction field, so `R` is the normalization of `B`. `j` is finite,
  birational, surjective by lying-over. `Omega_{R/A}=R/(3x^2)=0` and
  `Omega_{R/B}` is its quotient, so `j` is unramified. CONFIRMED.
- Singular support: `B` is a hypersurface in the smooth threefold
  `Spec C[p,p^-1,q,tau]`, so the Jacobian criterion is literal.
  `W_tau=3(tau^2-p)`, `W_p=-3tau-1-2p`, `W_q=0`. `W_tau=0` gives `p=tau^2`
  and then `W=tau^3-3tau^3-tau^2-tau^4=-tau^2(tau+1)^2`; `p` a unit forces
  `tau=-1`, `p=1`, where `W_p=3-1-2=0`. `Sing B={p=1,tau=-1}xA^1_q`.
  CONFIRMED.
- Sheets over `p=1`: `x^3=1`. `tau(1)=2` with `W_tau=3(4-1)=9`, smooth;
  `tau(omega)=omega+omega^2=-1=tau(omega^2)`, the colliding pair.
  Slopes `d tau/dp=(1+2x)/(3x^2)`: at `omega`, `(omega+2omega^2)/3`; at
  `omega^2`, `(omega^2+2omega)/3`; difference `(omega^2-omega)/3!=0`. Each
  branch is a smooth curve in the `(p,tau)` slice since `dp/dx=3x^2!=0`, so
  two smooth branches with distinct tangents: a line of nodes. CONFIRMED.
- Conductor, inclusion `IR` in `C_R` with `I=x^2+x+1=tau+1`: the three
  `A`-module products are `I=tau+1`, `Ix=tau+p` (the recovery identity),
  `Ix^2=x^4+x^3+x^2=px+p+x^2`, while `tau^2=x^2+2p+px` so
  `tau^2-p=x^2+p+px`, equal. All three lie in `B`, `IR=AI+AIx+AIx^2` is an
  `R`-ideal inside `B`, hence inside the conductor. CONFIRMED.
- Reverse inclusion: `r` in `C_R` gives `r,rx` in `B`. Elements of `B` are
  polynomials in `p,p^-1,q,tau`, so they take equal values at the source
  points `(omega,q0)` and `(omega^2,q0)`, which share `(p,q,tau)=(1,q0,-1)`.
  So `r` takes one value `a` at both, and `rx` gives `omega a=omega^2 a`,
  `a=0`. `r` vanishes on both whole lines. `R/(x-omega)=C[q]` is reduced, so
  `x-omega` divides `r`; likewise `x-omega^2`; non-associate primes, so
  `I` divides `r`. `C_R=IR` exactly, both inclusions. CONFIRMED.
- Saturation: `F(x,q)=(x^3,q)` maps `D={x=omega}` isomorphically onto the
  closed line `p=1`; `F^-1(F(D))={x^3=1}` is three lines, so neither `D` nor
  the union of the two colliding lines is saturated; the smooth line `x=1`
  is always missed. Literal images. CONFIRMED.

Verdict B: CONFIRMED. The ideal equality is established by the three
products plus the two-point evaluation, not by the radical alone.

## C. Euler failure, positive control, scope

- Euler action: `E=(x d_x+y d_y)/2` scales `x^a y^b` by `(a+b)/2`, and
  `E(x^-1)=-x^-1/2`, so `E` preserves `R`. `E(tau)=x/2+x^2=tau-x/2`.
  CONFIRMED.
- `x` not in `B`: `x` takes `omega` and `omega^2` at the two source points
  with one graph image, while every element of `B` takes equal values
  there. Hence `E(tau)` is not in `B` (else `x=2(tau-E(tau))` would be),
  although `tau` is: `E(B)` is not inside `B`. The two values of `E(tau)`
  differ by `-(omega-omega^2)/2=(omega^2-omega)/2`. CONFIRMED.
- Conductor: `E(I)=E(tau)=x(1+2x)/2`; at `x=omega` this is
  `omega(1+2omega)/2`, nonzero since `omega!=-1/2`, and likewise at
  `omega^2`. Every element of `IR` vanishes on both lines, so `E(I)` is not
  in `IR=C_R` while `I` is: `E(C_R)` is not inside `C_R`. CONFIRMED.
- Positive control: `q0=y/(3x^2)+(4/3)x`, `T0=xy/6-x^4/3`. `J=1` (same
  `q_y`); `p dq0=(-2y/3+(4/3)x^3)dx+(x/3)dy`, and `alpha-p dq0=
  (y/6-(4/3)x^3)dx+(x/6)dy=dT0`. `pq0/2=xy/6+(2/3)x^4`, minus `T0` is
  `x^4`, over `p` is `x`. So `A0[T0]=A0[x]`, which contains
  `y=3x^2 q0-4p` and `x^-1=x^2/p`: it is `R`. Same `alpha`, same
  `dx^dy=dp^dq0`, same degree-3 etale map `R=A0[X]/(X^3-p)` by the same
  irreducibility argument; graph smooth and embedded, conductor `R`,
  `E(R)` inside `R`. Matched-term check: `p*(10/9)x^2` adds `(5/9)x^5` to
  `pq/2` and `-4x^5/9` in `T` adds `4x^5/9`, total `x^5=p x^2`, exactly the
  `x^2` of `tau`; and `d(-4x^5/9)=-(20/9)x^4 dx=-p d((10/9)x^2)`, so the
  potential identity survives the deletion. CONFIRMED.
- Own meaningful check (new, not in ROOT): `E` does not even preserve the
  target ring `A`. `E(p)=3p/2` is in `A`, but
  `E(y/(3x^2))=(1/3)(y x^-2/2-y x^-2)=-y/(6x^2)`, `E((4/3)x)=(2/3)x`,
  `E((10/9)x^2)=(10/9)x^2`, giving `E(q)=-q/2+(4/3)x+(5/3)x^2`, whose `x`
  and `x^2` coordinates in the free basis are nonzero constants. Cross-check:
  with `X_T=T_y d_x-T_x d_y` one has `E=p d_p+X_T` (since
  `iota_E(dx^dy)-p dq=dT`), and `X_T(p)=3x^2*x/6=p/2`, so `E(p)=p+p/2`,
  consistent. Consequence: the descent failure is already visible at
  `A` inside `B`. The same holds in the positive control
  (`E(q0)=-q0/2+(4/3)x` is not in `A0`) where `E(R)` is nevertheless inside
  `R`; so `E`-stability of the target ring is neither implied nor tested.
- Scope. The example refutes exactly the displayed inference: radial
  canonical potential, `J=1`, primitive field generation, finite
  birational unramified graph normalization, on the OPEN plane with `p`
  inverted and `q` carrying a genuine pole, do not force `E(B)` inside `B`
  or `E(C_R)` inside `C_R`. It is not a full-plane Keller counterexample
  (`q` is not in `C[x,y]`; `F` is not a polynomial map of `A^2`); not an
  actual-source normality failure (the source `R` is regular; only the
  constructed graph `B` is non-normal); not a BGV refutation; no new
  unrestricted theorem. A version of the arrow that additionally assumes
  full-plane polynomiality, or `E`-stability of `A`, is untouched.

Verdict C: CONFIRMED as an open-plane discriminator. GAP only in reach: if
the named next-step inference assumed `E(A)` inside `A`, this control does
not test it (own check above).

## Verdicts

- A. CONFIRMED. `J(p,q)=1`, `dT=alpha-p dq`, inverse formulas,
  `R=A[X]/(X^3-p)` injective free rank 3 etale, `tau=x+x^2`,
  `x(tau+1)=tau+p`, `Frac B=C(x,y)` proved directly; pole of `q` retained.
- B. CONFIRMED. `W=Z^3-3pZ-p-p^2` minimal and exact kernel; `R` the finite
  birational unramified normalization; `Sing B={p=1,tau=-1}xA^1_q`;
  sheets `omega,omega^2` collide, `x=1` smooth with `W_tau=9`; slope gap
  `(omega^2-omega)/3`; `C_R=(x^2+x+1)R` by both inclusions; `D` and the
  colliding union unsaturated.
- C. CONFIRMED. `E(tau)=tau-x/2`, `x` not in `B`, `E(B)` and `E(C_R)` not
  inside `B`, `C_R`; positive control gives graph ring `R` with the same
  radial form and degree-3 etale map. Refutes only the open-plane
  automatic descent; nothing full-plane, BGV or normality is refuted.
- Own check: `E(A)` not inside `A` (`E(q)=-q/2+(4/3)x+(5/3)x^2`), a reach
  limit on what the control discriminates, not an error in ROOT.
- ROOT seal replay: body through the marker line is 6811 bytes, SHA-256
  `81dc61fd204f1b67fcec1a7065b4cdd2a0cd3968623edc068ba2bee2304c13ef`,
  matching its printed seal.

No OPEN raised, no descendant, no family enlargement, no charge_basis.
Protocol postpin `33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597`;
ROOT postpin `08423d2cc779e1f655336ef0342f74d5fe1f88ab4aa4b3114a0294c499031979`.
Destination is this single file; quantity/scope/control as bounded above.

<!-- BODY-END -->
