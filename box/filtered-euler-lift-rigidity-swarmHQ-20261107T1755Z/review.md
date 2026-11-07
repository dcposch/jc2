# EULERREVIEW1740 — hostile review of the exact filtered Euler theorem

Verdict: **CONFIRM_EXACT_FILTRATION_THEOREM**

Lifecycle: independent hostile review at the admitted exact scope; no public promotion or automatic successor.
Configured role: gpt-5.6-sol / ultra through the Sol adapter; hosted identity remains **UNVERIFIED**.
Startup UTC: 2026-11-07T17:31:29.857373+00:00.
Useful DRAFT/INCOMPLETE UTC retained: 2026-11-07T17:38:25.542080986Z.
Final-write UTC observed: 2026-11-07T17:40:02.907713935Z.

## Exact scope confirmed

Let `B=C[x,y]`, `w=x^2-y^5`, and give the unique normal form
`f(y,w)+xg(y,w)` the maximum weight for
`wt(x,y,w)=(5,2,3)`. Let `F*:B->B` send `x` to `P` and `y` to
`Q`, have constant nonzero Jacobian, and satisfy

`delta(F*f)=e delta(f)`

for every nonzero `f`, where `e` is a positive integer. Then necessarily

`e=1`, `P=alpha x`, `Q=beta y`, and `alpha^2=beta^5`,

with `alpha,beta` nonzero. In particular, no `e>1` map satisfies these
hypotheses.

This also excludes every surviving `k>=2` **full global homogeneous
polynomial lift** in the single Rees family

`S=C[X,Y,W,T]/(X^2-Y^5-WT^7)`

under the exact hypotheses in `PRIOR_LIFT.md`: the prescribed injective
graded Poisson reduction, `T |-> T^e`, homogeneous weights
`(5e,2e,3e)`, and the full relation `U^2-V^5=T^(7e)H`.

## Checkable proof

### 1. Filtration and associated graded ring

The monic identity `x^2=y^5+w` gives the asserted normal basis. Its
leading relation is `X^2-Y^5`, so

`gr_delta(B)=A0=C[X,Y,W]/(X^2-Y^5)`.

This is a domain. Therefore `delta` is multiplicative, and every filtered
piece is finite dimensional. For `E=5x partial_x+2y partial_y`, one has
`E(w)=10w`; hence `E` preserves every normal monomial and
`delta(Ef)<=delta(f)`. The ordinary Euler weight of `w` is 10, while its
filtration weight is 3; the proof does not identify those gradings.

### 2. Polynomial transport and finite filtered order

With `J=Jac(P,Q)`, define

`D_P=(Q_y partial_x-Q_x partial_y)/J`,
`D_Q=(-P_y partial_x+P_x partial_y)/J`,
`D=5P D_P+2Q D_Q`.

Constancy and nonvanishing of `J` make these polynomial derivations, and
chain rule gives

`D(P)=5P`, `D(Q)=2Q`, and `D(F*f)=F*(Ef)`.

For any polynomial derivation `L`, put

`q=max(delta(Lx)-5, delta(Ly)-2, delta(Lw)-3)`,

with zero terms assigned `-infinity`. Leibniz applied to each normal
monomial proves `delta(Lf)<=delta(f)+q`; thus every polynomial derivation
has finite filtered order. If `q>0`, a generator attaining the maximum
has nonzero leading image, so `L` induces a nonzero degree-`q` derivation
on `A0`.

Exact filtration scaling induces an injective graded map
`phi:A0->A0` multiplying degrees by `e`. If the order of `D` were
positive, its nonzero leading derivation `Dbar` would annihilate every
`phi(in_delta(f))`, because

`delta(D(F*f))=delta(F*(Ef))<=e delta(f)=delta(F*f)`.

Thus `Dbar` annihilates all of `phi(A0)`.

Set `L0=Frac(A0)` and `K0=Frac(phi(A0))`. Both have transcendence degree
2 over `C`. Moreover `L0` is finitely generated over `K0`, so equal
transcendence degree makes `L0/K0` finite algebraic. Characteristic zero
makes it separable. Extending `Dbar` to `L0`, differentiation of a
minimal polynomial over `K0` gives `m prime(a)Dbar(a)=0`; separability
makes `m prime(a)` nonzero. Hence `Dbar=0`, a contradiction. No
integrality of `B` over `F*(B)` is used. Therefore the order of `D` is at
most zero.

### 3. Complete small-piece derivation calculation

For a derivation `L` of order at most zero,

`F_2=<1,y>` and `F_5=<1,y,w,y^2,x,yw>`.

Consequently

`Ly=a+by`,
`Lx=c0+c1 y+c2 w+c3 y^2+c4 x+c5 yw`.

The `yw` term is present. Direct normal reduction gives

`Lw=(2c4-5b)y^5+2c5 xyw+2c3 xy^2+2c2 xw`
`   -5a y^4+2c1 xy+2c0 x+2c4 w`.

Since `delta(Lw)<=3`, independence of the degree-10 normal monomials
`y^5,xyw` forces `2c4=5b` and `c5=0`. Degrees 9, 8, 7, and 5 then force
respectively

`c3=0`, `c2=a=0`, `c1=0`, and `c0=0`.

Thus `L=mu E`, where `mu=b/2`. This checks the omitted-term risk,
including `yw`, without invoking a group-action classification.

### 4. Divergence and the diagonal conclusion

Mixed-partial equality and constant `J` give
`div(D_P)=div(D_Q)=0`. Therefore

`div(D)=5D_P(P)+2D_Q(Q)=7=div(E)`.

From the preceding classification `D=mu E`, so `mu=1`. Hence
`E(P)=5P` and `E(Q)=2Q`. For the ordinary positive grading
`wt(x,y)=(5,2)`, the weight-5 and weight-2 eigenspaces are respectively
`Cx` and `Cy`. Thus `P=alpha x`, `Q=beta y`; the Jacobian makes both
scalars nonzero. Applying exact scaling to `y` gives `e=1`. Finally

`F*w=alpha^2 w+(alpha^2-beta^5)y^5`.

Its required filtration degree is 3, so the degree-10 term must vanish:
`alpha^2=beta^5`.

### 5. Full-lift consumer

For a full lift, bracketing `U^2-V^5=T^(7e)H` with `V` gives

`-2U{U,V}=T^(7e){V,H}`.

The ideal `(T)` is prime because `S/(T)=A0` is a domain, and `U` is not
`T`-divisible because its prescribed reduction is nonzero. Repeated
prime cancellation gives `T^(7e) | {U,V}`. The quotient is homogeneous
of degree zero in the positive grading, hence is a scalar `c`. Reduction
modulo `T` and the prescribed Poisson identity
`{V0,H0}=-2U0` force `c=1`. Specializing `T=1` therefore gives
`Jac(P,Q)=1`.

For completeness, the exact scaling needed above follows from the Rees
map itself. If `f` has filtration degree `m`, take its degree-`m`
homogenization `f_tilde` in `S`. The lift sends it to degree `em`, and
its reduction modulo `T` is `phi(in_delta(f))`, which is nonzero by
injectivity. Hence the specialization at `T=1` has filtration degree
exactly `em`, not merely at most `em`. Thus the theorem applies. In the
retained classification, every surviving `k>=2` has
`e=k+1+3j>=3`, so every such full polynomial lift is excluded.

## Limits and custody

This confirmation does **not** show that an arbitrary hypothetical
Keller map supplies this filtration. It does not exclude completed-local,
rational, or localized lifts with poles; prove finite-normalization or
primitive no-fold statements; classify other filtrations; or prove JC2.
No completeness, local finiteness, finite Rees map, normalization
regularity, or unproved integrality premise was used.

Packet preflight verified all 18 declared inputs and three report seals.
Whole-reading counts are: nonSTATE `1979/3500` LF, STATE `115/160` LF,
and historical `299/320` LF. Reader help/syntax display was `16/100` LF;
one invalid top-level `help` request returned no body and was not retried,
then `window -h` supplied syntax. Repeats and own-report body previews
were zero. No narrow digest/numeric correction was invoked.

No source/web/history/repository search, CAS, native or secondary model,
degree/control-family farm, shared-document or Git mutation, settings,
adapter, authentication, or protected-tree access occurred. The startup
ACK was immutable mode `0444`; it proves neither hosted identity nor
mathematics.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6901`.
- Body SHA-256:
  `c036a0828faf606b20013c02d7d5502720c22254c8bdce1c46873141ce578caf`.
- Frozen basis: `a636e88e7cfc086340c87f66ff149e48f0120d63`.
