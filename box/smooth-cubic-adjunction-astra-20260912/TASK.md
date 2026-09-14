# Smooth finite cubic covers: positive-genus adjunction obstruction

ROOT September12,2026. Astra independent co-research, manual only. First
action UTC/hash; THIS TASK fresh WHOLE, sole scientific input. No peers,
corpus, network, scientific/code/CAS execution, AWS, Git/process/protected
inspection or new agents. Documentary date/hash/text, apply_patch and
existing artifact transaction only. Prior tasks completed and distinct.

One report xmodel/smooth-cubic-adjunction-astra-20260912.md <=2000words;
begin/close/finalize/expected verify via ops/artifact_finalize.py, basis
0d39df3c9fd69c939a8420c54d03228b9077777d. Own leased partial and own box
PINS/custody only. Unsealed skeleton first, bounded sections, own WHOLE,
postpins, BODY-END LAST; terminal custody-FIRST ALL WRITERS IDLE.
Original reserve02:51/HARD02:54 UTC, no extension. Honest GAP, no
promotion/canonical OPEN/descendant or automatic singular-cover extension.

Let phi:Y->P2 be finite of degree3, Y a SMOOTH RATIONAL projective
complex surface. Put L=phi*O(1), so L ample globally generated,L^2=3.
Let R=div(det dphi)=K_Y+3L be the effective ramification divisor, and
g=1+(K_Y+L).L/2 the genus of a general smooth member of |L|.
Assume g>=1. For ANY target line ell let
 U=Y minus (Supp(R) union Supp(phi*ell)).
QUANTITY: prove or refute that no dominant REGULAR morphism A2->U
exists, of ANY degree. This is an actual finite-cover donor exclusion,
not a statement that arbitrary Keller intermediates have this model.
CHEAPEST TEST: the following exact adjunction/log-pole argument, manual
<=20min. The potential resolution gap is central, not cosmetic.

Proposed steps, all UNPROVED until checked:

1. Rational-surface Riemann--Roch gives chi(K_Y+L)=g, and
h2(K_Y+L)=h0(-L)=0. Hence h0(K_Y+L)>=g>=1. Choose a nonzero section.

2. Every divisorial coefficient of R is e-1<=2 by finite degree3.
One might then write 2(K_Y+R_red) >= 3(K_Y+L) in divisor classes.
BUT a section of 2(K_Y+R_red) need not extend logarithmically to a
resolution if R_red is singular. Do not accept that naive argument.
Instead prove that the pair (Y,R/2) is LOG CANONICAL, locally at every
point, so on an embedded resolution rho:Y'->Y of the whole boundary,

 2(K_Y'+B') - rho*(2K_Y+R) is effective,

where B' is the reduced full boundary (strict transforms and exceptional
divisors) of U. This would be the actual pole-order inequality needed.

3. A suggested local proof: finite maps between smooth surfaces are
flat, so each local scheme fibre has length<=3. If both pulled-back
target parameters lay in m^2, their two-generated ideal cannot contain
all three independent quadratics in m^2/m^3, forcing length>=4. Thus
dphi has rank>=1 everywhere. Choose one target parameter as a source
coordinate s. Then phi=(s,h(s,t)); at a point of local fibre length
n<=3, ord_t h(0,t)=n after subtracting the target value. The different
h_t is a unit, a smooth equation, or a Weierstrass quadratic in t.
In the quadratic case, completing the square makes R locally
unit*(t^2+a(s)). If a!=0 it is analytically equivalent to t^2+s^m
for some m>=1; if a=0 it is twice a smooth divisor.
Prove (Y,R/2) log canonical for these forms, by explicit resolution
or a clearly labeled standard theorem with its exact hypotheses.
The double cover v^2=t^2+s^m is uv=s^m, an A_(m-1) singularity,
which may provide a short exact argument. Do not confuse log
canonicity of R/2 with log canonicity of R_red.

4. Since 2K_Y+R is linearly equivalent to 3(K_Y+L), cubing the
nonzero adjoint section gives a nonzero rational tensor-square of a
2-form with allowed pole divisor R. The verified inequality in2
would put its pullback in H0(Y',2(K_Y'+B')). Any dominant regular
A2->U would pull this back to a nonzero logarithmic pluricanonical
form on a compactification of A2. Explain the contradiction: a
nonzero h(dx wedge dy)^2 has pole order deg(h)+6>=6 along the
infinity line, exceeding the allowed order2; blowups outside A2
do not alter its strict-transform order. Polynomial h follows from
regularity of the pullback on A2. No properness of A2->U assumed.

Controls/scope: target ell may itself be branched, nonreduced on
pullback, tangent to R or pass through singular points. The proof
must use R/2 and boundary resolution so these are all included.
No generic-line assumption may be substituted. Finiteness of phi
is essential; for a merely generically finite morphism contracted
curves can have large different multiplicities. Rationality supplies
chi(O_Y)=1; do not silently generalize. The genus-zero case is
outside this task; ROOT separately checks whether it reduces to F1.
If a step fails, bank the precise obstruction, not a weaker renamed
theorem without saying what was lost. No theorem is promoted here.
