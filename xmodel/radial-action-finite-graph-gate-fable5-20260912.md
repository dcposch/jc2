# FIRST gate (Fable 5.1): radial action and finite canonical source graph

Tag `radial-action-finite-graph-gate-fable5-20260912`. Different-model hostile FIRST of the completed manual producer `xmodel/radial-action-finite-graph-astra-20260912.md`. First action 2026-09-12 13:00:29 UTC; reserve 13:12 UTC, HARD 13:15 UTC, never reset. Mathematics remains PROVISIONAL; JC2 is not resolved by this packet or by this gate.

## Custody

Snapshots hashed in `/tmp/jc2-lane.qU2CuC/inputs` before any body was read; both matched the expected pins.

- `COORDINATION.md` (48725 B, 806 lines): `33cfa6106972fe557a95ca81a9a05bb72300a82b2fbb7908915441cf75377597`
- `radial-action-finite-graph-astra-20260912.md` (10087 B, 114 lines): `77669329f1c41ad39522bdf7a6484c59f63e45fd20eace77857845ed93115298`

Both read fresh and WHOLE in unclipped chunks, COORDINATION first (1-140, 140-290, 290-460, 460-630, 630-806), then the producer (1-60, 60-114). No inherited reader, no original/corpus/source expansion, no linked body, no live peer output, no further input. No scientific interpreter, CAS, helper, code, network, git mutation, agent, or shared edit. Only read-only text/hash/UTC commands and `apply_patch` writes to this single file. Basis commit `0d39df3c9fd69c939a8420c54d03228b9077777d`. No `charge_basis` line (no exit price asserted); no `artifact_finalize` for this external lane.

Notation: `R=C[x,y]`, `L=Frac R`, `F=C(f,g)`, `A0=C[f,g]`, `alpha=(x dy-y dx)/2`, `E=(x d_x+y d_y)/2`, `J=f_x g_y-f_y g_x=1`.

## Exact statements charged

- (A) For any polynomial Keller pair and any polynomial `T` with `dT=alpha-f dg`: `C(f,g,T)=L`.
- (B) After a determinant-one linear change with `f_m(0,1)!=0` and `N>max(deg T,2)`, `H=T+x^N` makes `R` a finite `C[f,H]`-module, hence finite over `B=C[f,g,H]`.
- (C) The shear `X=x`, `Y=y+(2N/(N-2))x^(N-1)` makes `H` radial-canonical; `Frac B=L`; `R` is the integral closure of `B`.
- (D) `Omega_(R/B)=0`; the nodal control is finite birational unramified nonnormal; `B` normal iff `(f,g)` is an automorphism.

## A. Radial field generation — CONFIRMED

Reconstruction. `d alpha=dx^dy=df^dg` (Jacobian one), so `alpha-f dg` is a closed polynomial 1-form, exact on the plane; `T` exists, unique up to a constant. `df,dg` is an `L`-basis of `Omega_L`, so the dual derivations are forced: solving `a f_x+b f_y=1, a g_x+b g_y=0` gives `d_f=g_y d_x-g_x d_y` and likewise `d_g=-f_y d_x+f_x d_y`; I checked `d_f f=J=1, d_f g=0, d_g f=0, d_g g=1`. Contracting `dT=alpha-f dg`: `T_f=alpha(d_f)=(x(-g_x)-y g_y)/2=-E(g)`; `T_g=alpha(d_g)-f=(x f_x+y f_y)/2-f=E(f)-f`; `alpha(E)=(x y/2-y x/2)/2=0`, so `E(T)=-f E(g)=f T_f`. All three producer identities hold.

Descent. `f,g` are algebraically independent (a minimal relation would make `df,dg` dependent), `trdeg L=2`, so `L/F` is finite and separable. A derivation of `F` extends uniquely to any intermediate field and to `L` (formula `D(a)=-(Dm)(a)/m'(a)`); the restriction of the `L`-extension to `K=F(T)` is the `K`-extension by uniqueness, hence `T_f,T_g in K`. Then `E(f)=f+T_g`, `E(g)=-T_f`, `E(T)=f T_f` lie in `K`, and the Leibniz/quotient rules give `E(K) subset K`. The third identity is indeed load-bearing; without it `E(T)` is only known in `L`.

Projection. `E` multiplies a degree-`i` monomial by `i/2`, so for a polynomial `A in K` of degree `<=n` the Lagrange operator `prod_(j!=i)(E-j/2)/((i-j)/2)` returns the homogeneous piece `A_i`, and it stays in `K` because only nonzero rational constants are divided. Applying it with `i=1` to `f,g` (constants `f_0,g_0` are killed by the `j=0` factor, so retained constant terms are harmless) gives `f_1=f_x(0)x+f_y(0)y`, `g_1=g_x(0)x+g_y(0)y` in `K`, with matrix the Jacobian matrix at the origin, determinant `J(0)=1`. So `x,y in K`, `K=L`. Confirmed. Note `T` differs from the old potential `S` (`dS=x dy-f dg`) by `S-T=xy/2`; the statement is a different generation theorem, not a restatement.

Controls recomputed. Translated identity `f=x+a,g=y+b`: `alpha-f dg=-(x/2)dy-(y/2)dx-a dy=d(-xy/2-ay)`, so `T=-xy/2-ay`; `T_f=T_x=-y/2=-E(g)`, `T_g=T_y=-x/2-a=E(f)-f`, `E(T)=-y(x+a)/2=fT_f`; `f_1=x,g_1=y`. Punctured rational control `f=x^2,g=y/(2x)` on `x!=0`: `J=2x/(2x)=1`, `f dg=(x/2)dy-(y/2)dx=alpha`, so `T` is constant and `K=F`; `L=F(x)`, `x` has minimal polynomial `Z^2-f` because `(x,y)->(-x,-y)` fixes `f,g` and moves `x`, so `[L:F]=2` and generation fails. Exactly the hypothesis the projection step uses (polynomiality of `g`, so that `g` is a finite sum of `E`-eigenvectors) is what this control removes; `E(g)=0` there, consistent. Own check: `f=x,g=y+x^2`: `T=-xy/2-2x^3/3`; `T_f=T_x-2xT_y=-y/2-x^2=-E(g)`, `T_g=T_y=-x/2=E(f)-f`, `E(T)=-xy/2-x^3=fT_f`; and the `i=1` operator on `g` (`n=2`) is `-4E(E-1)`: `Eg=x^2+y/2`, `(E-1)g=-y/2`, `E(-y/2)=-y/4`, giving `y` exactly.

Verdict A: CONFIRMED. Scope caveat: for every known Keller pair `F=L` already, so the theorem has content only on a hypothetical counterexample; its value is that `T` is a canonical (up to affine-unimodular frame and a constant) primitive element of `L/F`.

## B. Algebraic finiteness — CONFIRMED

Linear choice. `m=deg f>=1` (`f` nonconstant). `f_m` is a nonzero form, so some `v` has `f_m(v)!=0`, and any `w` with `det(w,v)=1` exists; the substitution `(x_old,y_old)=wx+vy` has determinant one, preserves `J=1`, preserves `alpha` (it is `SL_2`-invariant) and total degrees, and gives `f_m(0,1)=f_m(v)!=0`, i.e. `f_m=c y^m+x(...)`, `c!=0`. `T` is recomputed in the new frame; `deg T` is unchanged.

Quotient bound. `N>max(deg T,2)` makes the top form of `H=T+x^N` equal to `x^N` and `N-2>0` for C. Homogeneous `P` of degree `d`: divide by `c^-1 f_m` in `C[x][y]` (monic in `y`), `P=q f_m+r`, `q,r` homogeneous, `deg_y r<m`, so `r=sum_(j<m) c_j x^(d-j) y^j`. If `d>=N+m-1` then `d-j>=N` for all `j<=m-1`, so `r in x^N R`. Hence every form of degree `>D=N+m-2` lies in `(f_m,x^N)` with homogeneous coefficients of degrees `d-m`, `d-N`, both nonnegative. Cross-check: `f_m,x^N` is a regular sequence (coprime forms), Hilbert series `(1-t^m)(1-t^N)/(1-t)^2`, socle degree `m+N-2=D`; the spanning set `x^i y^j`, `i<N`, `j<m`, is in fact a basis.

Filtered induction. Claim: the monomials of degree `<=D` generate `R` over `A=C[f,H]`. For `deg P=d>D`, write `P_d=f_m a+x^N b`; the degree-`d` part of `fa+Hb` is exactly `f_m a+x^N b` because the lower terms of `f` and `H` only contribute below `d`, so `deg(P-fa-Hb)<d`, while `deg a=d-m<d`, `deg b=d-N<d`. Strong induction on degree puts `P-fa-Hb`, `a`, `b` in the module, hence `P`. Every lower term of `f` and `H` is retained; termination is strict in `d`. So `R` is a finite `A`-module. Integrality preserves Krull dimension, so `dim A=2` and `C[U,W]->A` is injective: `f,H` algebraically independent, `(f,H):A^2->A^2` finite and (closed, dominant) surjective. Since `A subset B subset R`, the same generators make `R` finite over `B`, and lying-over gives surjectivity of `j_H`. Nothing is claimed for `C[f,g]`; finiteness of `(f,g)` is exactly JC and remains UNPROVED.

Own check (instance). Start from `f=x,g=y+x^2`; `f_1(0,1)=0`, so take `v=(1,0)`, `w=(0,-1)`, `det=1`; new frame `f=y`, `g=-x+y^2`, `T=xy/2-2y^3/3` (checked: `d T=alpha-f dg`), `deg T=3`, `N=4`, `D=3`. Then `x^4=H-(f/2)x+(2/3)f^3 in A.1+A.x`, and `y=f in A`, so `1,x,x^2,x^3` do generate. The producer's degree bookkeeping is reproduced.

Verdict B: CONFIRMED.

## C. Canonical shear and normalization — CONFIRMED

Coefficient recomputed with both terms. `X=x`, `Y=y+k x^(N-1)`: `X dY=x dy+k(N-1)x^(N-1)dx`, `Y dX=y dx+k x^(N-1)dx`, so `(X dY-Y dX)/2=alpha+(k(N-2)/2)x^(N-1)dx`. Requiring this to equal `alpha+d(x^N)=alpha+N x^(N-1)dx` forces `k=2N/(N-2)`, the producer's value. Negative control: at `N=2` no `k` works, matching the pole; indeed linear shears preserve `alpha` exactly, so `x^2` cannot be absorbed, which is why `N>2` is needed. Instance `N=4`: `k=4`, `Y=y+4x^3`, `(X dY-Y dX)/2=alpha+4x^3dx=alpha+d(x^4)`.

Consequences. The shear is a polynomial automorphism with polynomial inverse `y=Y-kX^(N-1)` and Jacobian one, so `f,g` are polynomials in `X,Y` with `J_(X,Y)(f,g)=1`, and `dH=dT+d(x^N)=(X dY-Y dX)/2-f dg`. Part A applies verbatim in the `(X,Y)` frame (its dual derivations and Euler field are those of `X,Y`; the origin is the same point), giving `C(f,g,H)=C(X,Y)=L`. Finiteness of `R` over `C[f,H]` is a ring statement, unaffected by the coordinate change. Hence `j_H: Spec R -> Spec B` is finite, birational, surjective; `R` is integral over `B` and normal (UFD), and anything in `L` integral over `B` is integral over `R`, so `R` is the integral closure of `B` in `L`: `j_H` is the normalization of the graph surface `Spec B`. The three objects are correctly separated: `(f,H)` finite (proved); `j_H` finite birational (proved); `F=(f,g)` finite (unproved; equivalent to JC for the pair).

Scope remark, not a refutation: `B` depends on the chosen `SL_2` frame, on `N`, and the shear; "canonical" means "radial-canonical relative to a chosen polynomial frame", not frame-independent. Additive constants in `T,H` change nothing.

Verdict C: CONFIRMED.

## D. Global gap and control — CONFIRMED (conditional argument and converse), gap correctly typed

`Omega_(R/A0)=(R dx+R dy)/(R df+R dg)=0` since the Jacobian matrix is invertible over `R`; `Omega_(R/B)` is a quotient, so also `0`. So `j_H` is unramified, and unramified plus finite plus birational plus smooth simply connected source does not give an isomorphism, as the control shows.

Nodal control audited. `R0=C[t,s]`, `B0=C[u,v,s]`, `u=t^2-1`, `v=tu`. Finite: `t^2=u+1`, so `R0=B0+B0 t`. Fraction field: `t=v/u`. Relation: `v^2=u^2(u+1)`, irreducible, so `B0=C[U,V,S]/(V^2-U^2(U+1))`, a nodal cubic times a line. Collision: every element of `C[u,v]` takes equal values at `t=1` and `t=-1`, `t` does not, so `t notin B0`, `(1,s)` and `(-1,s)` map to one point, `B0` is not normal and `R0` is its normalization. Unramified: `du=2t dt`, `dv=(3t^2-1)dt`, `3t du-2dv=2dt`, so with `ds` the module `Omega_(R0/B0)` vanishes. It is a map to `A^3`, not a Keller map, and its base `C[u,s]` fails the Keller condition (`Omega_(R0/C[u,s])=R0/(2t)!=0`), which is exactly why the conditional argument below does not apply to it.

Conditional normality argument audited step by step. (i) `B` normal means integrally closed in `L=Frac B`, and `R` is the integral closure, so `B=R`; then `R=A0[H]`. (ii) `phi: C[U,V,W]->R`, `(U,V,W)->(f,g,H)`, is onto a 2-dimensional domain from a 3-dimensional UFD, so `ker phi` is a height-one prime, principal, `=(P)`, `P` irreducible; `P notin C[U,V]` because `f,g` are algebraically independent, so `deg_W P>=1`. (iii) `Omega_(R/A0)=R dW/(R P_W dW)=R/(P_W(f,g,H))`, and this is `0` by Keller, so `P_W(f,g,H)` is a unit of `R=C[x,y]`, hence a nonzero constant `c` (`R^*=C^*` is the source-specific input). (iv) `P_W-c in (P)` has `W`-degree `deg_W P-1<deg_W P` (characteristic zero), while nonzero multiples of `P` over the domain `C[U,V]` have `W`-degree `>=deg_W P`; so `P_W=c`, `P=cW+Q(U,V)`. (v) `P(f,g,H)=0` gives `H=-Q(f,g)/c in A0`, `R=A0`, so `(f,g)` is an automorphism. Every step holds. Converse: an automorphism gives `A0=R`, so `A0 subset B subset R` forces `B=R`, normal. Hence normality of `B` is equivalent to invertibility of `(f,g)`; it is a reformulation of JC for the pair, not progress toward it, and the producer says so. Own check in the trivial direction: for `f=x,g=y+x^2` (original frame, `N=4`) `H=-fg/2-f^3/6+f^4`, so `P=W+UV/2+U^3/6-U^4`, `P_W=1=c`.

No normality, saturation, invertibility, conductor, BGV import, or JC2 consequence is inferred from finiteness of `j_H` or from simple connectedness, and none is inferred here. The remaining gap is exactly: decide whether `B=C[f,g,H]` is normal, equivalently whether `H in C[f,g]`; no source proof is offered, and no generic or punctured substitute is accepted.

Verdict D: CONFIRMED as stated (`Omega=0`, control, conditional argument, converse). The JC2 gap is untouched.

## Summary of verdicts

- A: CONFIRMED. `C(f,g,T)=L` for every polynomial Keller pair; controls and an own nonlinear check reproduced.
- B: CONFIRMED. `R` finite over `C[f,H]` with all lower terms retained; degree bound `D=N+m-2` matches the socle degree; instance reproduced.
- C: CONFIRMED. Shear coefficient `2N/(N-2)` from both terms; `Frac B=L`; `R` = integral closure; the three finiteness notions kept distinct; `N=2` pole is a genuine obstruction.
- D: CONFIRMED. `Omega_(R/B)=0`; nodal control finite/birational/unramified/nonnormal; `B` normal iff automorphism, both directions.

No REFUTED item. No new OPEN, no charge_basis, no descendant, no family/control enlargement, no formalization, no literature import. The useful contribution is a source-specific radial-canonical finite graph with explicit normalization; arbitrary finite primitive graphs were already known, and no exhaustive novelty claim is made or endorsed.

## Closeout

Own WHOLE readback and both postpins performed before the marker; destination is the single file named in the task; quantity, scope, and control statements above match the producer's charged claims. No edits after completion.

<!-- BODY-END -->
