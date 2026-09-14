# Independent gate: F9 weighted polynomial reference

tag=f9-weighted-reference-gate-sol-20260909  
reviewer=Sol, root fallback  
frozen_basis=0d39df3c9fd69c939a8420c54d03228b9077777d  
absolute_deadline=2026-09-09 06:57 UTC (retained)  
status=CONFIRMED AS A NECESSARY POLYNOMIAL-REFERENCE THEOREM; NOT AN EXCLUSION THEOREM

## 0. Custody, scope, and overall result

I read `PINS.json` first and then read whole the frozen new proof and transaction, the accepted joint gate, the complete accepted 16a/b excerpt, both charged algebraic-template excerpts, and the two charged metadata files. The eight payload hashes match the values in `PINS.json`; the new proof also matches the full hash in its transaction. The original Fable tag and `PREP_ONLY_NOT_INVITED` field remain preparation metadata; the root fallback invitation supplies this reviewer and output only. No uncharged source path, live peer, reverse gate, D108 material, protected project, or mutable ledger was opened.

The new theorem is **CONFIRMED**. Under exactly the displayed hypotheses over a characteristic-zero field,

    deg_w A=21, deg_w B=35, in_w(A)=H^3, in_w(B)=H^5,
    [A,B]_(g,p)=c*g, c != 0,
    H=p*(p^2-g)^2*(p^2-(3/2)g),

there is a finite polynomial reference for which the nonzero first residual satisfies

    1 <= j <= 13,       F_j=H*C,       H does not divide C.

All references and quotients used to obtain this conclusion are polynomial. In particular, no inversion of `p`, `b`, `H`, `K`, or a branch parameter occurs. This is only a necessary reference conclusion. It neither eliminates the remaining `H`-divisible first-contact branch nor proves the existence of a source pair.

The accepted source/map/ratio material is consumed only at its existing primary-import tier. I did not repeat its code, certificate, or primary-theorem review. Its relevant interface is that an actual 84/140 source yields, over the accepted complex extension and normalization, a 21/35 receiver satisfying the displayed hypotheses. The theorem reviewed here is separately valid over every characteristic-zero coefficient field `k` in which such a normalized pair is already given; it does not assert descent of the source normalizer to an arbitrary original field.

No mathematical subprocess, CAS, expansion, coefficient-row computation, solver, agent, worker, or remote job was used. The comparisons below are independent factored derivations, not validation by agreement with either historical template.

## A. Source, cover, and centralizer — CONFIRMED

With weights `w(g,p)=(2,1)`, every factor `p^2-g` and `p^2-(3/2)g` has weight 2, so `H` has weight 7 and its third and fifth powers have weights 21 and 35. The substitution

    g=a^2, p=b

is injective, and in characteristic zero its image is exactly the subring of polynomials even in `a`. It turns weighted degree into ordinary `(a,b)` degree and sends `H` to

    M=b^2-a^2,  V=b*(b^2-(3/2)a^2),  K=M^2*V,

of ordinary degree 7. Thus the pulled-back leaders are `K^3,K^5`.

For the stated bracket orientation, the chain rule gives

    [mathcal A,mathcal B]_(a,b)
      =2a*(A_g B_p-A_p B_g)(a^2,b)
      =2c*a^3.

The sign is positive and the omitted-cover-factor alternative is wrong: the cover determinant is `2a`, not a unit. Under the ordinary homogeneous dilation,

    mathcal A_s=s^21 mathcal A(a/s,b/s),
    mathcal B_s=s^35 mathcal B(a/s,b/s),

the bracket contributes `s^(21+35-2)` and the target contributes `(a/s)^3`. Hence

    [mathcal A_s,mathcal B_s]=2c*s^51*a^3.

Both sides have combined degree 54. The target order is 51, not the constant-J value 54 and not the historical 15/25 value 36.

The polynomial centralizer is indeed `k[K]` over the given field itself. For a nonzero homogeneous `U` of degree `r` with `[K,U]=0`, proportionality of the two gradients in `k(a,b)`, together with Euler's identities, gives

    dU=(rU/(7K))*dK,
    d(U^7/K^r)=0.

The common constant field of the two ordinary partial derivations of `k(a,b)` is `k`: first use the `a` derivative in `k(b)(a)`, then the `b` derivative. Therefore `U^7=lambda*K^r` with `lambda` in `k*`. The polynomial-prime valuation at `b` is decisive: `ord_b K=1`, so

    7 ord_b(U)=r.

Thus `r=7n`; substituting this back gives `d(U/K^n)=0`, hence `U` is a scalar multiple of `K^n` without choosing a seventh root in any extension. For a nonhomogeneous polynomial, the brackets of its homogeneous components have the distinct degrees `r+5`, so each component centralizes separately. Arbitrary constants are the `n=0` case. This proves `ker[K,-]=k[K]` and uses neither roots in `k` nor a generic-fibre theorem.

First gap in A: **none**. The only external boundary is the expressly accepted source interface and its complex normalization; that boundary is not upgraded to coefficient-field descent here.

## B. Canonical polynomial reference — CONFIRMED

For lexicographic order `a>b`, direct factored leading-term selection gives

    LM(K)=(-3/2)a^6 b,       LM(K^2)=(9/4)a^12 b^2.

At stages `q=1,...,7`, the order-`q` residual has degree `21-q`. Division by the single polynomial `3K^2` therefore gives a homogeneous quotient of degree `7-q`; adding `s^q` times that quotient to `R` removes exactly the divisible part through the linear cube term `3K^2 R_(7-q)` and changes only later orders. Polynomial monomial division uses only the nonzero leading scalar. It never divides by `b` or localizes at `K`. The `q=7` quotient is a scalar and is the necessary scalar `R_0` correction; it absorbs a possible quadratic reference kernel rather than deleting it.

At order 14 the residual has degree 7. Division by `K` has a scalar quotient `alpha`, and subtraction of `alpha*s^14 R` leaves an `LM(K)`-normal coefficient. At order 21 the remaining degree-zero coefficient is removed by `a0*s^21`. Thus

    F=mathcal A_s-R^3-alpha*s^14*R-a0*s^21

is finite and combined-homogeneous of degree 21, with `F_21=0`.

It cannot vanish. If it did, then over `k(s)[a,b]`

    (3R^2+alpha*s^14)[R,mathcal B_s]=2c*s^51*a^3.

The first factor has `(a,b)` degree 14, while the nonzero target has degree 3. Degree additivity in the polynomial domain makes this impossible. Consequently `1<=j=ord_s F<=20` and `deg F_j=21-j`.

The global nondivisibility check has no missing range. For `j<=7`, `F_j` is `LM(K^2)`-normal, so a nonzero multiple of `K^2` cannot equal it. For `j>=8`, its degree is at most 13, below `deg K^2=14`. Hence `K^2` never divides `F_j`. The special `j=14` coefficient also retains its separate `LM(K)` normality.

Every dividend and divisor in these divisions is even in `a`; the leading `a` exponent of each divisor is even. Each quotient monomial therefore has even `a` exponent, and each subtraction preserves evenness. Homogeneity is preserved at the same time. No total-odd restriction is imposed: all reference orders 1 through 7 are allowed. The construction is over a field, not a point or a nilpotent coefficient ring.

First gap in B: **none**.

## C. All B kernels and the order-2j equation — CONFIRMED

Retain all five scalars by writing `beta_i=b_i*s^(35-7i)`. For

    f_B=z^5+beta4*z^4+beta3*z^3+beta2*z^2+beta1*z+beta0,
    q=(5/3)z^2+(4/3)beta4*z+beta3-(5/9)alpha_s,
    tau=2beta2-(4/3)beta4*alpha_s,
    delta=beta1-beta3*alpha_s+(5/9)alpha_s^2,

termwise multiplication gives exactly

    f_B'=(3z^2+alpha_s)q+tau*z+delta.

Here the prime is only formal differentiation in `z`. With

    G=mathcal B_s-f_B(R)-q(R)F,

formal exterior differentiation in the independent symbols `R,F,G` yields

    [mathcal A_s,mathcal B_s]=[R,T]+[F,G],
    T=(3R^2+alpha_s)G-(tau R+delta)F
        -((5/3)R+(2/3)beta4)F^2.

The three relevant coefficients are respectively

    -(tau R+delta)-q'(R)F,   3R^2+alpha_s,   1.

Thus `alpha`, `beta4`, both summands of `tau`, all three summands of `delta`, and the differential constants `a0,beta0` are accounted for. In particular, deleting `beta4` would simultaneously change `q`, `tau`, and the `(2/3)beta4 F^2` term and would no longer be this identity.

The five scalar choices at orders 7, 14, 21, 28, and 35 have the exact effects

    -e*s^7 *(R^4+(4/3)RF),
    -e*s^14*(R^3+F),
    -e*s^21*R^2,
    -e*s^28*R,
    -e*s^35

on `G`. Their designated leading coefficients are respectively `-eK^4,-eK^3,-eK^2,-eK,-e`; every additional displayed term starts later. Sequential single-divisor projection therefore leaves the five designated coefficients normal and does not alter the source.

If a first nonzero `G_l` occurred with `l<2j`, then the exact identity at order `l` would reduce to

    [K,3K^2 G_l]=0.

Indeed, `F^2` starts at `2j`, `(tau R+delta)F` starts no earlier than `21+j>2j`, `[F,G]` starts after `l`, and the target starts at 51. The centralizer forces `G_l` to be a scalar power of `K`, possible only at the five projected orders; normality there forces it to vanish. Hence `ord_s G>=2j`, including the case `G=0` (infinite order).

At order `2j<51`, no mixed, `tau`, `delta`, `alpha`, `beta4`, or target term survives, and the complete equation is

    [K,3K^2 G_(2j)-(5/3)K F_j^2]=0.

The homogeneous inner polynomial has degree `49-2j`. For `1<=j<=20`, a nonzero centralizer value can occur only as a scalar `K^5` at `j=7` or a scalar `K^3` at `j=14`; these exceptions are retained. Both are divisible by `K^2`, so the equation implies `K|F_j^2`.

Now `M` and `V` are coprime and squarefree. This statement does not require `b^2-(3/2)a^2` to split: in the UFD `k[a,b]`, its irreducible factors remain distinct and occur once. Since `K=M^2V`, prime valuations give

    F_j=M*V*C0,       deg C0=16-j,       j<=16.

Solving the order-`2j` equation without discarding its kernel gives

    G_(2j)=(5/9)V*C0^2+Z,

where `Z=0` except that it may be a scalar `K^3` for `j=7` or a scalar `K` for `j=14`.

First gap in C: **none**.

## D. True order 3j and both M branches — CONFIRMED

After the radical bound, `3j<=48<51`, and `T` has order at least `2j`. Remove its coefficients successively only for `q<3j`. Once all earlier coefficients are zero, the order-`q` identity is `[K,T_q]=0`, because `[F,G]` starts at `3j` and the target at 51. Homogeneity and the centralizer give

    T_q=e_q K^n,       n=(49-q)/7.

Whenever this is nonzero, `q<48` makes `n` positive. Replacing `T` by

    T-e_q*s^q*R^n

kills that coefficient, preserves combined degree 49, and leaves `[R,T]` exactly unchanged because `[R,R^n]=0`. Corrections in later coefficients of `R^n` are not ignored: the finite increasing-order procedure processes every one that lands below `3j`. This includes the `K^5/K^3` term initially generated at order `2j` in the exceptional cases. It changes neither `F`, `G`, nor the source.

For the resulting polynomial `Ttilde`, all lower coefficients vanish. At order `3j`, positive-order terms of `R` can pair only with already-zero lower coefficients of `Ttilde`, and `ord F=j`, `ord G>=2j` leave only the pair `(F_j,G_(2j))`. Therefore the full equation is precisely

    [K,Ttilde_(3j)]+[F_j,G_(2j)]=0.

There is no target term because `3j<51`, and the retained `tau`, `delta`, `beta4`, and other mixed contributions are already contained in the exact polynomial `Ttilde`; none is sheared away.

Both partial derivatives of `K=M^2V` are divisible by `M`, so the first bracket is zero modulo `M`. For the exceptional `Z`,

    [F_j,K^n]=nK^(n-1)[F_j,K]

is also divisible by `M`; here `n=3` or `1`, not zero. Modulo `M`, the remaining bracket is therefore represented by

    (5/9)V*C0^2*([M,V]C0+2V[M,C0]).

This factor is obtained directly from the product rule for `F_j=MVC0`; no cancellation on a generic open set is used.

Let `d=deg C0=16-j`. Direct differentiation gives `[M,V]=3a^3`. On each of the two distinct `k`-rational branches `b=epsilon*a`, `epsilon=+1,-1`,

    V(a,epsilon a)=-(epsilon/2)a^3.

Euler's identity for the homogeneous polynomial `C0` gives, on that whole branch,

    [M,C0](a,epsilon a)=-2epsilon*d*C0(a,epsilon a).

The restricted polynomial identity in the domain `k[a]` is consequently

    (5/9)(3+2d)a^3 V(a,epsilon a) C0(a,epsilon a)^3=0.

Characteristic zero makes `3+2d` nonzero, and the other displayed factor outside `C0^3` is a nonzero polynomial. Hence `C0` vanishes identically on both branches. The two nonassociate primes `b-a` and `b+a` both divide `C0`, so their product `M` divides it in the UFD. This is polynomial branch restriction, not point sampling and not generic-open cancellation.

It follows that `K|F_j`. Writing `F_j=K*C` gives `deg C=14-j`. Degree excludes `j>14`; at `j=14`, the quotient would be a nonzero scalar, contradicting the retained `LM(K)` normality. Thus

    1<=j<=13,       F_j=K*C.

Finally `K` cannot divide `C`, because that would contradict the already proved `K^2` nondivisibility of `F_j`.

First gap in D: **none**.

## E. Descent and nonexclusion — CONFIRMED

The cover source, `R,F,G`, the original exact `T`, and the successively corrected `Ttilde` are all even in `a`. From `F_j=K*C` and evenness of `F_j,K`, cancellation in the domain also makes `C` even. The equality between the even subring and `k[a^2,b]` therefore gives unique polynomials over `k[s,g,p]`. For any two descended polynomials their cover bracket is `2a` times the pullback of the `(g,p)` bracket; cancelling the nonzero polynomial `2a` descends the exact identity. Divisibility descends with its polynomial quotient. No localization is introduced.

The direction

    H^2/p = p*(p^2-g)^4*(p^2-(3/2)g)^2

is polynomial of weight 13, hence has the first-contact index `j=21-13=8`. On the cover it is `K^2/b=K*(K/b)`. Since `K/b` is polynomial but lacks the simple `b` factor of `K`, this coefficient is divisible by `K` and not by `K^2`. It therefore survives the proved first-contact divisibility and normality restrictions. This is only a surviving polynomial direction: it is not an actual source point, does not provide the remaining coefficients, and is not a solution of the full Jacobian equation. Absorbing it into `R` would require the forbidden Laurent quotient `1/b` (downstairs `1/p`).

The conclusion uses only the weighted 21/35 leaders and the bracket `c*g`. It does not use lower faces, inverse ordinaryness, or a reverse receiver-to-source lift. It proves none of the following: exclusion of the remaining `H`-divisible source branch; exclusion of actual degrees 84/140; a maximum-140 result; existence or nonexistence of an ideal point; reverse polynomiality; a coefficient ideal or computation certificate; a nilpotent-scheme statement; or any JC2 conclusion.

First gap in E: **none**.

## Counterfactual hypothesis controls

These are prose consequences of changed objects or hypotheses, not claims that an executable manual test was run.

- Omitting the cover determinant replaces `2c*a^3` by a false target and destroys the order-51 accounting.
- Omitting `beta4` changes three linked places—`q`, `tau`, and the `F^2` coefficient—so the asserted exact bracket identity no longer follows.
- Setting the exceptional order-`2j` centralizer scalars to zero without proof loses the possible `K^5`/`K^3` inner terms and the corresponding `K^3`/`K` terms in `G_(2j)`; the finite commuting subtraction and the modulo-`M` argument are what make them harmless.
- Replacing polynomial `K^2/b` by a presumed `K^2` multiple silently inverts `b`; their different `b`-valuations are exactly why the `j=8` direction remains.
- Moving the target to order `3j` adds a nonzero right-hand side to the branch equation and invalidates the deduction `M|C0`.
- In a characteristic where `3+2d` vanishes, the two-branch restriction need not force `C0` to vanish. Characteristic zero is therefore load-bearing.

## OPEN(S) RAISED

None.

## COLLISIONS

status: EMPTY

- NONE — no typed OPEN is raised and no corpus scan is claimed.

<!-- BODY-END -->
