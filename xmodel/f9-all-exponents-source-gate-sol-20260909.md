# Independent Sol gate: all-exponent F9 source interface

tag=f9-all-exponents-source-gate-sol-20260909
reviewer=Sol
invitation=ROOT RELEASE 2026-09-09 08:17 UTC
overall_verdict=GAP AT THE UNCONDITIONAL ALL-q SOURCE ATTACHMENT; CONDITIONAL RECEIVER ARROW CONFIRMED

## 0. Frozen scope, custody and verdict boundary

I read WHOLE, by literal `sed` output, exactly the eight frozen lane objects in `/tmp/jc2-lane.rljzCG/inputs`: `01-new-source-proof.md`, `02-new-source-transaction.json`, `03-producer-READ-SCOPE.md`, `04-accepted16ab-joint-gate.md`, `05-primary-ggv-excerpts.txt`, `06-primary-gghv-excerpts.txt`, `07-primary-lower-excerpts.txt`, and `PINS.json`. Their SHA-256 values respectively are

    744dbc9c8144c3aa37e13fc14e34d95088e7c46b97e9fb5dd56b8fb88261c7ad
    f3400ef09d2d7b3c3c133b45b35d125a41e5497117775e88c0351ffd298ff11c
    59748b5595a40e75ca172b44915f1631538040a276c04dc8df5de5af68f9f4d2
    f33820d2bf5f4f75229938b3cfb6d03d21cd05bb8c09a9cf340e3edaa351f7bd
    bda523c7316aeca24175653ef4de81105e65e59f645d84e045f6fd254d20fd84
    080ffdbb7a42f00eb24a6432f39a8376254fb4bf842763fc3e93d4457a319e21
    ebed877ded74f6ec248285737f23684a58dc73a526b9db06387900a94359b5f3
    ce396bfce96b833f9a5da4b4ce2f488adf3c01d94cff4b4d2cfa58d418ec447b

These match the current lane pin vector. The charged primary scope was GGV1401 lines 100–188, 218–280, 350–405, 680–824, 1419–1517 and 1870–2182; GGHV1708 lines 30–100, 155–205, 640–820, 1184–1240 and 1350–1415; and lower1605 lines 160–303. In particular, GGHV1000–1060 and lower304 onward were absent and were neither reconstructed nor presumed. The producer READ-SCOPE's statements that its author read GGHV1000–1060 and lower through 315 are provenance quotations, not this review's permission or read scope.

No original provenance path, other report, 0730 blind/cross, live proof/log/receipt, coordinator local proof, protected project material, network source, AWS or SSH was read. No mathematical subprocess, checker, expansion, solver, CAS, Python, agent or numerical experiment was used. Administrative operations were limited to the lane pin/custody state, clock, target-absence check, metadata hashes and this exact external-lane output.

The status distinction is essential. The manuscript proves a conditional theorem beginning with an already ordinary rectangular Keller pair having an actual F9 chain. It does not obtain such a pair for every F9 parameter. Therefore the conditional mathematics can survive while the advertised independent all-q incoming attachment remains a source GAP.

## 1. Incoming ordinary rectangular F9 object — GAP

Read the family parameter as the integer `q in Z_{>=0}`, as in the printed table's `j in N_0`; otherwise the manuscript's gcd assertion is not even typed. Then

    m=q+2,  n=2q+3,  gcd(m,n)=gcd(q+2,-1)=1,

so every printed F9 exponent pair satisfies the retained coprime-integers and `m,n>1` hypotheses.

The primary arrows, however, run only in the necessary direction. GGHV's introduction says that falsity of JC supplies some ordinary attained rectangular normalization with some `a,b,m,n`. Theorem 2.20 sends each actual standard pair to a complete chain. The bounded algorithm then lists F9 as an admissible chain family. Neither theorem reverses that direction, and the F9 row does not assert existence of a Keller pair realizing each `q`. GGV Definition 4.3 is weaker still: bare standardness is defined in `L^(1)=K[x,x^-1,y]` and supplies neither ordinaryness nor the two rectangular coordinate bounds. Proposition 5.20 preserves polynomiality when `P,Q` are already in `L`; it does not turn an arbitrary Laurent standard pair into an ordinary rectangular one.

Thus the exact first failed hypothesis is the attempted arrow

    printed admissible F9 row at q
      ==> actual ordinary attained rectangular normalized Keller representative at q.

That arrow is absent. Calling it an “imported incoming arrow” is REFUTED as an attribution to the charged sources; mathematical existence for a given `q` is a GAP, not a nonexistence theorem. Table-label matching, same-degree data, or selection of a minimal representative cannot fill it. The accepted16a/b report remains at its named tier: it supplies the special degree-84/140, `m=3,n=5` (`q=1`) attachment, but expressly does not supply arbitrary `q`.

Surviving narrower claim: for any characteristic-zero field and any `q in Z_{>=0}`, **if** an ordinary pair in `K[u,v]` already has the two attained rectangles and the actual F9 starting/selected data stated in section 1, then the source-interface construction may be tested conditionally. No existence of that input, no coverage of all counterexamples, and no claim for bare Laurent standard pairs survives.

## 2. Starting face, roots, Euler ratio and vertical shift — CONFIRMED conditionally

For either exponent `e=m,n`, the actual endpoints `e(1,0)` and `e(7,21)` and Proposition 2.1 give, up to a nonzero output unit,

    ell_(7,-2)=alpha_e R^e,
    R=u r(z),  z=u^2 v^7,

because the ordinary weight-seven lattice is exactly `(i,j)=(1+2k,7k)`. Both endpoint coefficients are nonzero, so `r` is cubic with nonzero constant coefficient. The selected child ordinate 2 gives multiplicity `2e`; at a nonzero fractional root characteristic zero preserves multiplicity under the seventh-power parameter. Hence the common cubic has exactly one double nonzero root `a` and one distinct simple nonzero root `b`:

    r(z)=(z-a)^2(z-b),  ab(a-b) != 0.

There is no degree left for an omitted root, and a triple root would have the wrong selected multiplicity. Over the working field the unique monic gcd of `r,r'` is `z-a`, so `a`, then `b`, is in that field; alternatively the entire argument is valid after a finite algebraic extension.

For the polynomial Theorem 2.6 Euler element `E`, the relation for `R^m` gives `[mE,R]=R`. Every ordinary weight-five monomial is `u^(1+2k)v^(1+7k)`, so writing `mE=uv f(z)` yields

    5 z r' f - 7 z r f' - r f = r.

After division by `r`, the logarithmic-derivative poles at both the double root `a` and simple root `b` force `f(a)=f(b)=0`. The leading coefficient for degree `d>2` is proportional to `14-7d`, so no higher-degree or retained leading term survives. Thus `f=C(z-a)(z-b)`, and direct factored substitution gives

    C((3a-2b)z-ab)=1.

Since `ab!=0`, this forces `b=3a/2` and `C=-1/(ab)`. This handles rather than suppresses the exceptional scalar cases: `a=0` or `b=0` contradicts the attained constant endpoint, `a=b` contradicts exact selected multiplicity, and `C=0` cannot solve the Euler equation.

At the vertical face, write the top coefficient of `P0` as `f_0(u)` of actual degree `7m`. Theorem 2.6 gives `v a_0(u)` and

    21m a_0' f_0-a_0 f_0'=f_0.

Constants fail and every degree at least two has an uncancellable term above degree `7m`; hence `a_0=A u+B`, `14m A=1`, and `f_0=alpha(u+r_0)^(7m)`. The top coefficient of `Q0`, of actual degree `7n`, satisfies the top-Jacobian equation and is `beta(u+r_0)^(7n)` with the same `r_0`. Characteristic zero and the nonzero corner coefficients are used here.

The common translation `u -> u-r_0` lowers `(7,-2)`-weight whenever it changes a power, so it preserves the complete starting faces and all their root multiplicities. It preserves both rectangular guards: the top-`v` coefficients become pure top powers, while at maximal `u` the face bound forces `j=21e`, so the unique top-right coefficient is unchanged. No polynomial-specific Euler theorem is later applied blindly to the Laurent child.

## 3. Positive interval, two lower cuts and post-shear edge — CONFIRMED conditionally

After the swap, `C_e=(21e,7e)` is the unique maximum in each coordinate, and `d_0=(-2,7)` has normalized start `(21,7)`. If `d=(rho,sigma)` is the first lower direction in the union, an ordinary positive-axis term in at least one member forces `3rho+sigma>0`; otherwise both restrictions to `y=0` would be constant and the constant Jacobian would vanish there. The arc from `d` to `d_0` is shorter than a half-circle because `7rho+2sigma>rho>0`, and `C_e` maximizes throughout it. Positivity therefore holds on the whole required interval, not only at its ends.

At every such lower endpoint the possible leading-bracket weight is exactly

    7(m+n)(3rho+sigma)-(rho+sigma)
      =(7(m+n)-1)(3rho+sigma)+2rho > 0.

Thus the leading faces commute. Their positive weights have ratio `m/n`, so Proposition 2.1 makes both faces powers of a common nonmonomial root; an edge on one side cannot be matched by a monomial on the other.

Corollary 7.4 applies with `l=1`, `q_E=7`, not with the family parameter. It gives a `7e`-th-power face and a root with normalized endpoint `(3,1)`. At this first cut a Laurent root whose positive power is ordinary has nonnegative minimum `x`-exponent, so the root is ordinary and has exactly the two terms

    a_1 x^3 y+b_1 x^(3-k),  a_1 b_1 != 0.

The source lattice makes `k` integral whenever this corollary is used. Independently, lower Proposition 2.1 excludes the rational interval `0<k<1` at the endpoint `C_e`, and Corollary 1.6 excludes `k=1`; positivity excludes `k>=3`. Hence the first edge is exactly `k=2`, with one common nonzero `lambda`. Its value is in the coefficient field from the ratio of the next face coefficient to the nonzero corner coefficient, divided by `7e`.

The shear `psi:y -> y+lambda x^-2` has determinant one and collapses precisely this edge. The manuscript's next-edge assertion is valid, but the needed justification is: the entire `d_0` face is unchanged because the replacement term has weight 4 rather than 7; that face contains its nonzero constant and cubic endpoints and is nonmonomial. Hence the sheared polynomial is still nonmonomial. Since `C_e` remains the unique maximum in both coordinates, its finite Laurent Newton polygon has another incident lower edge. This rules out the otherwise possible “collapsed to a monomial” failure.

For a proposed next slope `2<kappa<3`, the same whole-interval and bracket-gap argument applies. The Theorem 2.6 element after the shear is not assumed to be the old polynomial element. Instead, two weight-five Euler solutions differ by a homogeneous `Z` commuting with `R_0=y r(x^7y^2)`. If `Z!=0`, Proposition 2.1 gives `Z^7=unit*R_0^5`; taking the integral `y`-valuation gives `7 ord_y(Z)=5`, impossible in `K[x,x^-1,y]`. Thus `Z=0`, including all retained kernel terms, and the constructed Euler element and denominator 7 are unique after transformation. Corollary 7.4 then gives a `y`-linear Laurent root whose `x`-exponents are integers, forcing `kappa` integral, a contradiction. A slope-three edge is retained and no positive-weight theorem is applied there.

This finding imports Corollary 7.4 at the charged primary theorem tier, whose printed proof says to mimic Corollary 7.2; it does not claim a new proof of that source theorem.

## 4. Support, exponent map, attainment, degrees and sign — CONFIRMED conditionally

Before the shear, ordinaryness and the actual starting face give `i,j>=0` and `-2i+7j<=7e`, whence

    i-2j >= (3/7)i-2e >= -2e,

with equality only at the actual point `(0,e)`. A shear term maps `(i,j)` to `(i-2t,j-t)`, preserves `i-2j`, lowers `-2i+7j` by `3t`, and keeps `j>=0`. For each sheared polynomial the next incident lower slope is at least 3; its supporting inequality, together with `j<=7e`, gives `i<=3j` for every support point, including the slope-three boundary. Thus the full, not merely facewise, support satisfies

    j>=0,  i<=3j,  -2i+7j<=7e,  i-2j>=-2e.

The literal toric substitution `x=g^-1`, `y=g^3p` maps

    (i,j) -> (I,J)=(3j-i,j).

The four inequalities become `I,J>=0`, `2I+J<=7e`, and `I-J<=2e`; hence ordinaryness follows term by term and not from cancellation or degree labels.

Attainment is separate from permission. `(0,7e)` is the unchanged top corner; `(3e,e)` is the image of the uniquely retained `(0,e)` term; `(2e,0)` is its unique `t=e` shear contribution and has coefficient proportional to `lambda^e!=0`. The origin can be attained by choosing an output constant outside one forbidden value; this changes neither bracket nor positive faces. Consequently the actual total degree is `7e` with unique leader `p^(7e)`, and the actual `g`-degree is `3e`. These are not the pre-map degrees `28e` or merely weighted degrees.

For the complete source substitution

    (u,v)=(g^3p+lambda g^2-r_0,g^-1),

the determinant in the declared order `(g,p)` is

    u_g v_p-u_p v_g=0-g^3(-g^-2)=g.

Thus `[Abar,Bbar]=c_0 g`, with positive sign. The equivalent factorization has swap determinant `-1`, shear determinant `+1`, and toric determinant `-g`, again giving `+g`. No omitted term or degree label determines this sign.

## 5. Faces, scalings, fields and direction of the map — CONFIRMED necessary map; GAP beyond it

The upper face is

    Hbar=p(p^2-ag)^2(p^2-bg),  b=3a/2,

and the unique equality line from `(0,e)` gives the complete lower face

    alpha_e r(0)^e g^(2e)(gp+lambda)^e.

Choose nonzero `mu` in a finite algebraic extension with `mu^3=a lambda`, put `kappa=lambda/mu`, substitute `(g,p)->(kappa g,mu p)`, and divide the two outputs by their respective nonzero leading units. Then

    a kappa/mu^2=1,
    b kappa/mu^2=3/2,
    lambda/(kappa mu)=1,
    r(0) kappa^3/mu^6=-3/2.

All denominators are nonzero by the already checked root, edge and corner guards. The two normalized faces are therefore exactly `H^m,H^n` and `(-3/2)^e g^(2e)(gp+1)^e`. The new bracket coefficient is

    c=c_0 kappa^2 mu/(alpha beta mu^(7(m+n))) != 0;

it is not silently normalized to one. Only finitely many scalar roots are adjoined, so the result is over a finite algebraic extension of the characteristic-zero coefficient field. Diagonal and output scalings preserve all support and attainment statements.

This confirms the all-exponent **necessary receiver map** for every coprime `m,n>1` having the explicit source profile, hence conditionally for every integer F9 parameter. It does not repair obligation 1. The reverse lift is a GAP and is not needed for necessity: the displayed inverse uses `g=v^-1` and has extra polynomiality/divisibility conditions. A bracket of receiver type alone cannot supply a reverse arrow (for example `(g,gp)` has bracket `g` but recovers `p` only by division by `g`). Matching the two faces likewise supplies neither all inverse source inequalities nor the full constant-Jacobian equation. No complete-equations ideal, source existence, family exclusion, degree exclusion, properness assertion or JC2 nonexistence follows.

## 6. Manual changed-object and hypothesis controls

- Remove the rectangle while keeping the face/corner labels: adjoining a formal support term `u^(7e-1)v^(21e+1)` preserves total degree `28e`, the maximal-`u` endpoint and the `(7,-2)` face (its weight is `7e-9`), but destroys the vertical bound. This is not offered as a Keller pair; it isolates exactly why metadata cannot license the vertical Euler step.
- Change the simple root ratio while retaining two nonzero distinct roots: with `b!=3a/2`, the factored Euler substitution leaves the nonconstant residual `(3a-2b)z`. The failed hypothesis is Theorem 2.6's polynomial Euler solution, not a claimed counterexample.
- Set any guarded scalar to zero: `alpha` or `beta` removes an attained leading face, `a` or `b` removes the nonzero constant endpoint, `lambda` makes the first lower root monomial and kills `(2e,0)`, and `mu=0` makes the diagonal map noninvertible. None is an exceptional continuation of the proof.
- Replace the integral Laurent lattice by fractional `x`-powers: the formal root `x^3y+x^(3-kappa)` can then exist for nonintegral `2<kappa<3`. This changes the ring and pinpoints the integer-gap hypothesis.
- Omit `i<=3j`: a retained term with `i>3j` maps to a negative `g`-exponent. Thus receiver ordinaryness comes from the actual next-edge inequality, not polygon labels or cancellation.
- Remove the unchanged nonmonomial `d_0` face: collapsing the only known lower edge would no longer prove that a next edge exists. In the charged object that guard survives the shear, so this control fails exactly where the real proof succeeds.
- Reverse the map without inverse polynomiality: `g=v^-1` remains a denominator even when the forward determinant and receiver faces are correct. Necessary image data cannot be promoted to a lift or exclusion.

## 7. Final adjudication and writer state

1. Incoming actual ordinary rectangular all-q F9 attachment: **GAP**. First missing arrow is admissible-table family to actual Keller realization. The fixed `q=1` accepted attachment and the explicit conditional source hypothesis survive.
2. Complete starting face, multiplicities, cubic Euler ratio, nonzero units, common vertical shift and both source guards: **CONFIRMED**, conditional on that source hypothesis and characteristic zero.
3. Whole positive interval, exact bracket-gap identity, both lower cuts, existence of a nonmonomial post-shear next edge, rational-slope exclusion, and transformed Euler uniqueness: **CONFIRMED**, at the charged Corollary 7.4 theorem tier.
4. Full support transport, integral exponent map, ordinaryness, attained vertices, actual degrees and determinant/sign: **CONFIRMED**.
5. Both normalized faces, nonzero scaled Jacobian, finite extension and conditional all-exponent scope: **CONFIRMED AS A NECESSARY MAP**. Reverse lift, full CE ideal and any exclusion: **GAP / NOT CLAIMED**; any inference of receiver, family or JC2 nonexistence is **REFUTED** by the direction of the proved map.

Promotion as an unconditional “all-q source attachment” is denied. The safe replacement is the conditional theorem: every already-existing ordinary rectangular actual-F9 source with integer parameter `q>=0` maps, over a finite algebraic extension, to the stated ordinary receiver. No exit-price assertion is made.

terminal_writer_state=COMPLETED THROUGH THE EXISTING EXTERNAL LANE; exact target `xmodel/f9-all-exponents-source-gate-sol-20260909.md`; target was absent before this sole write; no alternate output, Seal or charge_basis was authored.

<!-- BODY-END -->
