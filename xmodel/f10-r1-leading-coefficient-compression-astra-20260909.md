# F10 r1 leading coefficients: exact rational univariate compression

2026-09-09, nonemptiness_certificate. PRODUCER-ONLY pending independent review. First action16:07:40 UTC; controlling cap16:19:40 UTC. Pure manual algebra, ZERO mathematical subprocesses. This is a leading-face interface, not a complete residual solution, an ideal decision, a source point or computation authorization.

## 1. Accepted scope and the recovered recurrence

The two original WHOLE inputs are the accepted16q compact contract (SHA6c6fe089...) and accepted16r Euler elimination (SHAa5ab487c...). During the task root explicitly added the WHOLE accepted16l standalone resonance report (SHA38cf3fb9...). Exact paths and full hashes are in input-pins.json. No other local mathematical input was read. In particular the pending DZ/tree report is not a premise.

For r=1 the normalized source leading forms are

    A_top=S*t^3*C(T), B_top=S^2*t^5*D(T), T=S/t,
    C=1+F*T+H*T^2+a*T^3, D=sum_(i=0)^5 D_i*T^i,
    D_0=1, a!=0, b=D_5!=0.

Here F=d_1,H=v_2,a=k_4 in accepted16r; its highest Jacobian coefficient gives exactly

    7T C'D-4T CD'-CD=-1.                         (1)

For i>=1 coefficient extraction gives, with negative indices zero,

    (4i+1)D_i+(4i-10)F D_(i-1)
        +(4i-21)H D_(i-2)+(4i-32)a D_(i-3)=0.   (2)

Thus D1 through D5 are uniquely reconstructed using only fixed rational units. For convenient read-back:

    D1=6F/5,
    D2=(12F^2+65H)/45,
    D3=(-24F^3+356FH+900a)/585,
    D4=(-6F D3+5H D2+16a D1)/17,
    D5=(-10F D4+H D3+12a D2)/21.

The ENTIRE remaining equations are

    q6=14F D5+3H D4-8a D3=0,
    q7=7H D5-4a D4=0.                           (3)

The degree8 coefficient is identically zero, since its aD5 multiplier is4*8-32=0; there are no higher coefficients. Nothing has been replaced by a leading part of (3).

For a direct zero-chart check, H=0 would give D4=0 from q7 and D3=F D2 from q6 and the D5 recurrence. The D3 recurrence then gives F^3=5a. The D4 recurrence gives F(F^3-12a)=0. Since a!=0, F is nonzero and these contradict. Thus H!=0 follows here, without importing a max-h claim. This is also already encoded by accepted16l's complete normalized description. The recurrence and bivariate classification are RECOVERED/NO_NEW_ALGEBRA, not a new closure.

## 2. Exact connection to the accepted normalized bivariate recipe

Write z for the variable of a monic cubic and define

    s=H/a, v=F*a/H^2, w=a^2/H^3.

All divisions are now licensed. Then

    C(s*z)/(a*s^3)=z^3+z^2+v*z+w=:C_m(z).

Likewise divide D(s*z) by b*s^5 to get a monic quintic D_m. Multiplying (1) by3 after these substitutions gives precisely accepted16l's equation with m=4 and exponent7/4. Its complete reciprocal recipe is therefore applicable, not merely a similarly named cubic equation. Let

    f_i(v,w)=[x^i](1+x+v*x^2+w*x^3)^(7/4),
    D_m(z)=sum_(i=0)^5 f_i(v,w)*z^(5-i).

The finite-partition meaning of each f_i is the accepted rational polynomial, not an analytic branch. ALL normalized solutions are exactly f6=f7=0. That accepted theorem proves w!=0 and f5!=0 at every such field point, and finite normalized support; it did not compute a univariate eliminant or distinct-root count. No novelty is claimed for those results.

The source leading coefficients are recovered, over the same coefficient field, by retaining s as an independent NONZERO scalar:

    F=v/(w*s), H=1/(w*s^2), a=1/(w*s^3),
    D(T)=D_m(T/s)/f5, b=1/(s^5*f5).             (4)

Indeed a*s^3=1/w and b*s^5=1/f5 restore C(0)=D(0)=1. Conversely (4) gives H/a=s and the stated v,w, so no geometric scale or zero-v chart has been discarded. This is a coefficient reparametrization; it is NOT permission to apply a new automorphism to the full source or set lower coefficients to constants.

## 3. New r1 delta: one degree-seven polynomial, without a resultant calculation

Root proposed the following smaller elimination during this task; the producer independently checked it from the finite-partition coefficients. Put

    E(v)=39-360v+960v^2-512v^3,
    L(v)=192v^2-144v+25,
    R(v)=7168v^3-6720v^2+2016v-195.

For exponent7/4 the falling products begin21/16,-21/64,105/256,-945/1024,12285/4096,-208845/16384. Substitution into the accepted finite formulas gives exactly

    (65536/7)f6=6144w^2+(640-3072v)w+E(v)=:E6,
    f7+f6/4=(R(v)-112L(v)w)/131072.             (5)

For example the w^2 coefficients in the second equation cancel; its remaining w coefficient is-7L/8192 and constant part R/131072. These individual rational identities fix both sign and normalization. All denominators are fixed nonzero rationals.

There is NO missing L=0 branch. Manual division gives

    R=((112/3)v-7)L+(4/3)(56v-15),
    L(15/56)=10/49!=0.                         (6)

Thus L and R are coprime in Q[v]. Set

    p(v)=24R(v)^2+(280-1344v)L(v)R(v)
                        +49E(v)L(v)^2.         (7)

This has EXACT degree7: only49EL^2 contributes degree7, with nonzero leading coefficient49*(-512)*192^2. The polynomial p was not expanded or factorized; no resultant, numerical approximation, root count or arithmetic subprocess was used. Equations (5)-(7) give exact equivalence

    f6(v,w)=f7(v,w)=0
       <=> p(v)=0, w=R(v)/(112L(v)).           (8)

In fact if L vanished at a root of p, then p=24R^2 would force R=0, contradicting (6). Substituting w into E6 and multiplying by(112L)^2/256 gives exactly p; the three factors are6144/256=24,112*(640-3072v)/256=280-1344v, and112^2/256=49. This also verifies the reverse implication, not just necessary elimination.

## 4. Finite algebra, retained full source, and exact limits

Let B=Q[v]/(p). It is a nonzero seven-dimensional Q-algebra, because p has degree7. This is a vector-space dimension, NOT a claim of seven distinct roots, seven fields, or seven rational solutions. L is a unit in B by (6)-(7), so w=R/(112L) is an actual element of B. More strongly, the normalized bivariate ring Q[v,w]/(f6,f7) is isomorphic to B, including possible nilpotents: (5) replaces the equations by E6 and112Lw-R; (6) makes L a unit in that quotient; (7) then eliminates w reversibly. These are polynomial identities with fixed rational units and an explicitly justified invertible L, not a generic localization.

The accepted field-point proof also makes w and f5 units in this finite algebra: if either were a nonunit, some maximal ideal would give a characteristic-zero residue field and a normalized f6=f7 point with that value zero, contradicting accepted16l. Therefore (4) is defined on B[s,s^-1]. Separability, reducedness, irreducible factors and a primitive number-field choice have NOT been established. None is needed to state this exact finite algebra or its full-scaling field-point parametrization.

For the full r1 presentation, substitute only

    d1=v/(w*s), v2=1/(w*s^2), k4=1/(w*s^3)

and retain u,ell,d0,v0,v1,k1,k2,k3 and every reconstructed mate coefficient/equation. Accepted16r's guard becomes

    omega/(w*s^8*f5)-1=0,

or equivalently omega-w*s^8*f5=0 after multiplying by a proved unit. This records the original top-restoration scalar rather than setting it to1. Every coefficient of BOTH full residuals must still vanish. One may clear only powers of the proved units s,w,f5,L when writing them algebraically. The finite algebra B itself is only a leading-face object: it is not a full compact-system point or a counterexample certificate. No full residual has been substituted, emitted or solved in this task.

Manual changed-hypothesis controls: removing q6 or q7 leaves an unchecked coefficient of (1); dividing L without (6) would risk deleting a chart; setting s=1 would discard unlicensed full-source scalings; and dropping the final residual is concretely refuted by accepted16r section8's guarded upper-row family with constant residual-1. No division by v is made anywhere, so any v=0 possibility is tested by p rather than silently removed. Actual source degrees remain112/196 if every full condition later holds; the degree7 here is an auxiliary algebra dimension, not a source degree or map degree.

## Completion and raised OPEN

NEW narrow delta: explicit degree-seven univariate read-back and full-source retained-scale substitution. RECOVERED: the complete normalized bivariate leading description, its finite field-point set and nonvanishing. No literature novelty or uncharged tree conclusion is claimed.

OPEN quantities: zero irreducible factors or separability certificates computed; zero full residual substitutions verified. Cheapest subsequent test, only if independently authorized after review, is literal exact read-back of (5)-(8) and every unchanged full residual under (4), retaining s and all guards. No builder, branch farm, solve, new representation dispatch or descendant is authorized. Own WHOLE read and own raised-OPEN check precede the completion marker. All writers IDLE at handoff.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8898`.
- Body SHA-256:
  `45bd1db800143193db8e318c19292d1358f48be191c7d7a7c02dcc3006699b88`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
