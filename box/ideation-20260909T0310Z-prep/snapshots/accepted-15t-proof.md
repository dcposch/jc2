# Triple-root cubic chart and a strengthened conditional coalesced consumer

September9,2026. **NEW / PROVISIONAL PURE-PROOF RESULT.** The formal cubic right-normalization is proved directly. Under the explicit additional source-reference hypotheses below, every stated coalesced balance with d<=5 and 0<r<5/3 is impossible, not only balances23r<36. This is an independently typed sibling of the pending late-contact theorem; no late-contact conclusion, triple reference framework, separated cubic cover or source-family exclusion is a premise or conclusion.

## 1. Input meaning and conditional boundary

Let K have characteristic zero. Throughout, “combined degree D” means **combined-homogeneous** for deg(s)=deg(g)=deg(p)=1. A mere upper bound is insufficient for the Euler assertions: R=H+s has total combined degree5 but its constant deformation has weight1, not5. Formal right-normalization still exists for that example; the requested homogeneous weights do not.

For the CHART theorem assume only

\[
R\in K[s,g,p]\text{ combined-homogeneous of degree5},\quad
R_0=H=p^2(p-g)^3,
\]
\[
F\in K[s,g,p]\text{ combined-homogeneous of degree15},\quad
\operatorname{ord}_s F=j<\infty,\quad
d=\operatorname{ord}_{p-g}F_j\le5.
\]

Here d>=0. For the CONSUMER assume additionally j>=1, ordinary combined-homogeneous A,B of degrees15/25, scalars alpha,a0,c in K with c!=0, and the exact identities

\[
A=R^3+\alpha s^{10}R+a_0s^{15}+F,
\quad B_0=H^5,
\quad[A,B]_{g,p}=cs^{36}g^2.                 \tag{S}
\]

Equivalently B-R^5 belongs to sK[s,g,p]. These are stated source hypotheses, not conclusions obtained by assuming that a pending reference theorem extends to the triple H. No G decomposition, first-contact divisibility, canonical normality, weight bound on g/p, polygon, parity or lift equation is used.

The whole pinned actual-Moh source07e53340... and gateeade8ec8... retain the named conditional125/75-to-ordinary25/15 receiver map and its actual-degree centering. The whole accepted weight-free local-consumer d4fd2a0e... was read as proof-pattern context only; its two H patterns do not include this triple profile. The actual-Moh map alone does not supply this task's r/coalescence/d conditions for every receiver. All three exact full hashes and read scopes are in input-pins.json, checked before and after publication. No current blind/cross, live gate or pending late-contact proof was read or used in this task.

## 2. Exact cubic right-normalization

Set X=p, g=X+w, and work over the coefficient field

\[
E=\overline K(X^{1/3}).
\]

X is a generic nonzero coordinate, not a source specialization. Initially put zeta0=-X^(2/3)w. Then H=-X²w³=zeta0³ exactly. Give X and s weight1 and zeta0 weight5/3. The substitution is invertible over E, with g=X-X^(-2/3)zeta0 and p=X. It turns R into an element of E[zeta0][s] with initial cube and combined weight5.

Construct successively an s-adic change zeta0=zeta0(s,zeta,X), equal to zeta modulo s, which puts R in the exact form

\[
\widetilde R=\zeta^3+a_s(X)\zeta+b_s(X),
\qquad a_s,b_s\in sE[[s]].                 \tag{1}
\]

At stage l>=1, suppose all lower orders are already linear or constant in zeta. Write the remaining order-l polynomial uniquely as

\[
f_l(\zeta)=\zeta^2 h_l(\zeta)+a_l\zeta+b_l.
\]

Replace the old zeta by the new zeta minus s^l h_l(zeta)/3. At order l the initial cube changes by -s^l zeta²h_l, which removes exactly that multiple. Changes to earlier a_s zeta have order at least l+1 because a_s starts at positive order; higher changes also occur later. Record a_l,b_l and proceed. No division by zeta occurs: h_l is the polynomial quotient of terms already divisible by zeta². The only scalar division is by3.

Every finite stage is polynomial in zeta coefficientwise in s. The changes are the identity modulo s, so their infinite composition and inverse exist in the s-adically complete algebra E[zeta][[s]]. In particular every fixed s coefficient is a polynomial in zeta, all s/zeta exponents are nonnegative, and every s-order is integral. At each finite order only finitely many preceding changes contribute. The inverse can also be constructed order by order by solving its identity-mod-s equation. This supplies an actual formal right-equivalence, not a finite truncation or an unsupported analytic convergence claim.

The construction preserves weights. f_l has weight5-l; h_l has weight5/3-l; therefore the shift s^l h_l has weight5/3. Consequently zeta0(s,zeta,X) has weight5/3, the inverse g(s,zeta,X) has weight1, a_s has weight10/3, and b_s has weight5. All coefficients belong to E; no negative s powers or further roots are required. Fractional/negative X powers are allowed in this generic-line coefficient field and do not assert global polynomiality of the chart.

Both deformation terms are necessary. For the actual degree5 polynomial R=H-s*p³*(g-p), the initial chart gives R=zeta0³+s*X^(7/3)*zeta0. An identity-mod-s change alters the order1 coefficient only by a zeta² multiple, so it cannot remove this linear term. Likewise R=H+s*p4 has an unavoidable order1 constant in that quotient. Thus the fictitious form xi_s+zeta³ is not available for a general cubic deformation. These are manual changed-object controls on degree5 factors, not an executed calculation.

## 3. Transport of every F coefficient and of the full bracket

Write the actual transformed series as

\[
\widetilde F=\sum_{n\ge0}c_n(s,X)\zeta^n.
\]

The inverse change has nonnegative s-order and is the specified linear change at s=0. Therefore every ord_s c_n>=j. The order-j coefficient is exactly F_j(X-X^(-2/3)zeta,X). Since p-g=X^(-2/3)zeta, the multiplicity hypothesis gives

\[
\operatorname{ord}_s c_d=j,\qquad
\operatorname{ord}_s c_n>j\quad(n<d).        \tag{2}
\]

The leading coefficient is X^(-2d/3)*(F_j/(p-g)^d)(X,X), which is nonzero in E. Vanishing c_n have order infinity. No claim about later coefficients is inferred from a static jet: the c_n here are the full moving coefficients. Each has combined weight15-5n/3.

For (S), the exact chain rule at fixed s is

\[
[\widetilde A,\widetilde B]_{\zeta,X}
=cs^{36}g(s,\zeta,X)^2g_\zeta(s,\zeta,X).   \tag{3}
\]

The g_X terms cancel in the determinant since p=X. At s=0,

\[
g=X-X^{-2/3}\zeta,\qquad g_\zeta=-X^{-2/3}.
\]

Thus the PURE s-order36 coefficient, before a transverse rescaling, is

\[
-cX^{-2/3}(X-X^{-2/3}\zeta)^2,
\]

not a zeta-independent constant. This distinction is load-bearing. After zeta=s^rY with any r>0, its leading weighted coefficient is exactly -cX^(4/3), independent of Y. All zeta-dependent terms gain positive order, and the nonlinear change contributes corrections of positive integral s-order. Hence in the (zeta,X) convention the substituted target starts at order36 with that constant; in the (Y,X) bracket it starts at order36+r. This is the negative sign from the actual coordinate determinant, not a reversal of the source component order.

## 4. Complete coalesced initials and uniform tail bounds

Define

\[
r=\min_{0\le n\le d}\frac{\operatorname{ord}_s c_n}{9-n},
\qquad0<r<5/3,
\qquad\operatorname{ord}_s a_s\ge2r,
\qquad\operatorname{ord}_s b_s\ge3r.         \tag{4}
\]

Infinity is allowed in any individual order; r is finite because c_d has order j. Its denominator comes from an integer order divided by one of9,8,...,9-d. One may adjoin a finite fractional power of s only now, to express the rescaling; the original c_n orders remain integers.

For n<=d, every c_n zeta^n has rescaled order at least9r, and at least one attains9r. Since r<=j/(9-d), terms with n>d have order at least j+(d+1)r>=10r. The latter is a uniform bound on the infinite tail, not a truncation. Therefore F has a nonzero polynomial initial U(Y) of degree at most d<=5 at order9r. Coalescence gives the R initial

\[
V(Y)=Y^3+\mathfrak a(X)Y+\mathfrak b(X)
\]

at order3r; an indicated coefficient is zero if its required equality order is absent or infinite. The A scalar terms are later: 10+3r>9r and15>9r. Hence the full A initial is the monic degree9 polynomial

\[
P=V^3+U\quad\text{at order }9r,\qquad U\ne0. \tag{5}
\]

Put h=5/3-r>0. Combined homogeneity implies Euler homogeneity under X*d_X+h*Y*d_Y: P has degree15-9r=9h. More generally, an actual B initial at order nu has Euler degree25-nu. This follows coefficientwise: a term s^i*zeta^n*f(X) of B has X-weight25-i-5n/3, and after i+nr=nu its Euler weight is25-nu. Constants of X-differentiation in E are precisely Kbar.

The full transformed B-R^5 has every coefficient of s-order>=1. If B has an earlier initial Q at nu<15r, its largest Y-degree n consequently satisfies

\[
nr<\nu.                                   \tag{6}
\]

R^5 itself starts at15r. Positive r and nonnegative integral indices ensure that only finitely many terms can contribute below any chosen weighted order, so Q is a genuine polynomial with a genuine nonzero top coefficient. At15r the correction has degree<15; R^5 therefore contributes an uncancellable monic degree15 term. These bounds use the whole series, not a selected subset of B rows or a G hypothesis.

## 5. Earlier B initials are excluded even at the nonzero target

Suppose nu<15r exists, and let q_n be the nonzero leading coefficient of Q. The first possible order of the bracket in the (zeta,X) convention is

\[
\theta=8r+\nu.
\]

If theta>36, the left side of (3) starts too late to equal its nonzero order36 target: differentiation lowers the transverse order by at most r, while X differentiation does not lower s-order. If theta<36, the initial [P,Q]_(Y,X) vanishes. If theta=36, that initial equals -cX^(4/3), a polynomial CONSTANT in Y by §3.

In both theta<=36 cases, the coefficient of Y^(8+n) in [P,Q] must be zero. It equals 9q_n': P is monic9, so P_X has degree<=8 and the product P_X Q_Y has degree<=7+n. Hence q_n'=0 and q_n belongs to Kbar. Euler homogeneity of Q now gives

\[
(25-\nu-nh)q_n=0.
\]

But (6) and h>0 imply

\[
25-\nu-nh>25-\frac{5\nu}{3r}>0
\qquad(\nu<15r),
\]

a contradiction in characteristic zero. This includes n=0. The argument does not require P to be homogeneous for its top-coefficient step, does not set the nonzero equality target to zero, and does not assume the bracket's top degree is attained without cancellation. It checks the actual top coefficient and uses its forced vanishing. Therefore there is no earlier B initial in ANY of the three target-order comparisons.

## 6. The monic15 initial, all three endpoint comparisons

By §4–5, B starts at15r with monic degree15 initial Q, Euler degree25-15r=15h. The first possible bracket order is23r.

If23r>36, (3) is impossible by the same too-late argument. If23r<36, one has [P,Q]=0. Euler differentiation then gives

\[
X[P,Q]=h(15P_YQ-9PQ_Y)=0.
\]

Since h!=0, Q³/P5 is Y-constant. Monicity makes it1. Unique factorization in E[Y] yields a monic cubic W with P=W³ and Q=W5. Now

\[
U=W^3-V^3=(W-V)(W^2+WV+V^2).
\]

If W!=V, the second factor has degree6 and leading coefficient3, so the nonzero difference has degree at least6. This contradicts deg U<=5. If W=V, then U=0, also a contradiction. This is a factored degree argument, not an expansion of a degree9/15 pair.

Finally, equality23r=36 cannot occur under the original integral s-orders. Some finite index0<=n<=d realizes the minimum in (4), so r=i/(9-n) with i an integer. Equality would force

\[
23i=36(9-n).
\]

Since gcd(23,36)=1, this requires23 to divide9-n, whereas4<=9-n<=9. This is impossible. The subsequent fractional-power rescaling does not change the already established integral order i. The linear and constant cubic deformations, including their equality cases, were retained throughout.

Consequently the explicitly stated coalesced hypotheses (4), with0<=d<=5 and0<r<5/3, are inconsistent with (S). This extends the strict23r<36 consumer to the entire specified interval; it is not an analysis of any separated cubic regime.

## 7. Manual controls, read scope and exact stopping statement

The following identify real dependencies rather than certify a sample source point.

- The degree5 controls in §2 exhibit actual linear/constant deformation terms that cannot be removed modulo zeta² at their first order. Dropping a_s is genuinely wrong, not merely a different normalization choice.
- If the correction-degree cap is relaxed from5 to6, a common cubic W=V+kappa with kappa!=0 has W³-V³ of degree6. Thus the factor-degree contradiction in §6 genuinely uses the cap. This formal common-factor object is not claimed to satisfy the nonzero monomial-J source.
- If one permits fractional s-orders BEFORE defining r, c5=s^(144/23) would give r=36/23. It violates the actual integral-order hypothesis and shows why that hypothesis cannot be silently replaced after rescaling.
- A wrong plus sign for the coordinate determinant contradicts the explicit derivative g_zeta=-X^(-2/3) at s=0. A claim that the entire pure s-order36 coefficient is constant contradicts the explicit zeta-dependent expression in §3. Only its positive-r weighted initial is constant, which is exactly what the comparison uses.
- A merely degree-bounded, nonhomogeneous reference such as H+s loses the Euler weights, as stated in §1. The proof does not infer them from a degree upper bound.

All controls are manual factored/scalar reasoning. No mathematical subprocess of any size, high H/R power, full source, 9/15 pair, CAS/Python/SymPy/free-symbol test, AWS/SSH/web, agent, shared/protected write or current-round/live-peer read occurred. Only bounded metadata hashing/publication scripts ran. Whole exact source/gate reports and the whole local-consumer proof were read; their historical code and upstream source bodies were not re-executed or newly re-audited. Metadata pins and all owned artifacts are recorded in terminal custody.

The first theorem is an exact formal chart over the generic-line coefficient field. The second is an exclusion of an EXPLICIT HYPOTHETICAL coalesced source interface. It does not show that every actual receiver reaches (4), prove the pending triple reference construction, handle three-simple or one-plus-double separated cubics, exclude a whole historical[3] receiver or original source, or yield a scheme/unit/JC2 conclusion. No further descendant or separated cover is launched. All writers are IDLE after transaction sealing; fixed stop01:58 UTC remains unchanged.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14388`.
- Body SHA-256:
  `60cf87eb93271fc3011ff16fea8873559f5477b4af8e72a0e311942b45a43b53`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
