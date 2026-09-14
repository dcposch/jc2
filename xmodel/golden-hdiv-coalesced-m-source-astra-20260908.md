# Golden H-divisible correction: the coalesced-M source exclusion

September 8, 2026. **PROVED HERE / UNREVIEWED FIELD-SOURCE IMPLICATION.** The coalesced-M argument works in the two explicitly stated strata below. Its proof is independent of the pending simple-L result. The condition on the moving critical value is retained, not inferred from a static Hermite value. Separated sheets, whole-golden exclusion, nilpotent coefficient schemes and JC2 are outside this report.

## 1. Exact statement and accepted inputs

Let K be a characteristic-zero field containing either root rho of `rho²-3rho+1=0`. Put

\[
t=1-\rho,\quad L=p+g,\quad M=p+tg,\quad H=p^2LM^2,
\quad w(g)=5,\ w(p)=-7.
\]

Suppose the literal polynomial source satisfies

\[
\deg A=15,\ \deg B=25,\quad A_{15}=H^3,\ B_{25}=H^5,
\quad w(A)\le3,\ w(B)\le5,\quad[A,B]_{g,p}=cg^2,
\quad c\in K^*.
\]

Use exactly the canonical references of the accepted source report, with ordinary homogeneous dilation in s. Thus `[A_s,B_s]=cs^36g²`, s,g,p have combined degree1, and

\[
R_s=H+\sum_{a=1}^5s^aR_{5-a},\quad
A_s=R_s^3+\alpha s^{10}R_s+a_0s^{15}+F,
\quad j=\operatorname{ord}_sF,\quad F_j=HC\ne0.
\]

The accepted H-divisible source bounds give `1<=j<=9`, `deg C=10-j`, `w(C)<=2`, `deg_g C<=2`. No parity is imposed. No reference coefficient or source constant is set to zero. The accepted B construction retains all five scalar kernels and gives G of order at least2j. We need only its weaker consequence

\[
\mathcal E_s:=B_s-R_s^5\in sK[s,g,p],                 \tag{1}
\]

which also follows directly from `B_0=H^5=R_0^5`. It retains *all* B terms rather than choosing a truncation of G.

At the moving M-critical point choose the exact Morse coordinate described in Section2 and write

\[
R_s=\xi_s+\zeta^2,\qquad
F(g(s,\zeta,p),p)=\sum_{n\ge0}c_n(s,p)\zeta^n,
\qquad\kappa=\operatorname{ord}_s\xi_s.
\]

Here are the two separate assertions.

| Stratum | d | Definition and bound for r |
|---|---:|---|
| `C(-p/t,p)!=0` | 2 | `r=min_{0<=n<=2} ord(c_n)/(6-n) <= j/4 <= 9/4` |
| `L M` divides C | 3 | `r=min_{0<=n<=3} ord(c_n)/(6-n) <= j/3 <= 2` |

In either row **the additional condition `kappa>=2r` is impossible** for the stated source. Zero series have infinite order. The minimum is finite because the coefficient c_d has order exactly j, proved below. These two strata exhaust the possibilities if `L|C` is imposed independently: the first is `M∤C`, the second `M|C`. No simple-L theorem is used to impose `L|C`. In particular the unassumed stratum `M|C, L∤C` is not silently covered.

Accepted input pins, checked before proof-body access:

- Whole source: `xmodel/golden-two-regime-initial-discriminator-astra-20260908.md`, SHA `14c4cdeddf9b1166046759022378775fc7ebc147c7d939579cf93f6b78aa51c6`.
- Whole frozen AUDIT15m: `box/ideation-20260908T2220Z-poststate/snapshots/audit-15m-only.md`, SHA `b02ae267bb8cfef6956d6e0cec0b6188196b222d3d9d78e3d1582f4a5cc1a440`.
- Accepted gate provenance/hash lookup only, not another body review: `xmodel/golden-nonh-composition-gate-fable5-20260908.md`, SHA `ddd2077da0d63d53aea062373f82ce7bdb21d9df1fcf4180127789e98409b9e2`.

The original source's authored UNREVIEWED header is preserved in its immutable bytes; AUDIT15m supplies its accepted scoped post-state. No other pending theorem is a premise.

## 2. Exact Morse field and the first Taylor coefficients

Set `g0=-p/t`. The accepted degree-five identity is

\[
H(g_0+w,p)=t(t-1)p^3w^2+\rho p^2w^3.
\]

All lower R components have g-degree at most2. Formal implicit solution of `R_{s,g}=0` gives `g_c(s,p)`, with constant g0. Writing

\[
R_s(g_c+w,p)=\xi_s+w^2(a_s+\rho p^2w),\qquad
a_s=R_{s,gg}(g_c,p)/2,
\]

gives `a_s|_{s=0}=t(t-1)p³`, a unit over the coefficient field (unrelated to the source constant a0). Choose `a²=t(t-1)` and work in `E=Kbar(p^(1/2))` with the extended p-derivation. The coordinate

\[
\zeta=w\sqrt{a_s+\rho p^2w}
\]

has an inverse `w_s(zeta)` in `E[[s,zeta]]`, with invertible linear coefficient. Thus `g=g_c+w_s(zeta)` has **no negative s-orders**, and `g_zeta(0,0,p)=1/(a p^(3/2))`. Coefficients may have p-poles; no regularity at p=0 is used. Both square-root choices are allowed.

Since F starts at s^j before substitution, every c_n has order at least j. At order j the substituted series is exactly

\[
\zeta^2 C(g_0+w_0(\zeta),p),                    \tag{2}
\]

because `H(g0+w0(zeta),p)=zeta²`. Therefore:

- In the first stratum, `c_0,c_1` have orders greater than j and `[s^j]c_2=C(g0,p)!=0`.
- In the second stratum, normality in g and homogeneity force
  `C=lambda*p^(8-j)*L*M`, with `lambda!=0`. Its weight is `7j-46<=2`, so j<=6. The M zero is simple because L and M are distinct. Hence `c_0,c_1,c_2` have orders greater than j and

\[
[s^j]c_3=\frac{\lambda(t-1)}a\,p^{15/2-j}\ne0. \tag{3}
\]

For (3), `C_g(g0,p)=lambda*(t-1)*p^(9-j)` and `w_0'(0)=1/(a p^(3/2))`. All field factors are units for both rho roots. These are actual Taylor coefficients of the moving-source substitution, not a claim that a static jet bounds its later coefficients. Every later moving constant/linear coefficient remains in the minimum defining r.

## 3. Uniform control of the infinite series and the A initial

Take the r of the appropriate table row, and clear its rational denominator by one finite s-Puiseux extension. Put `zeta=s^rY`. Since `r>0`, for every finite order bound only finitely many Taylor indices n can contribute: the uniform lower bound is `j+nr`. Thus the substitution and its coefficientwise initial forms are well-defined; this is not an unproved truncation.

For `n>d`,

\[
j+nr\ge j+(d+1)r>6r,
\]

because `r<=j/(6-d)`. The terms with `n<=d` all have order at least6r by the definition of r, and at least one attains it. Consequently F has initial a **nonzero** polynomial `U(Y)` of degree at most d at order6r. Ties cannot cancel between different Y-degrees; within each c_n its actual order was used.

Now impose the explicit coalesced condition `kappa>=2r`. Then R has order2r and initial `S=Y²+b`, with b zero unless `kappa=2r`. Infinite kappa is included. Since `r<5/2`, both `10+2r>6r` and `15>6r`. All A scalar references are strictly later, and the full A initial is therefore

\[
P(Y)=(Y^2+b)^3+U(Y),\qquad \deg U\le d\le3,
\quad U\ne0,\quad\operatorname{ord}A_s=6r.       \tag{4}
\]

Uniqueness of the implicit/Morse constructions under scaling makes `g_c` combined degree1, xi degree5, and zeta degree5/2. After substitution define `h=5/2-r>0` and the coefficient Euler derivation

\[
\mathscr D=p\partial_p+hY\partial_Y.
\]

More explicitly, a transformed coefficient of `s^a zeta^n` has p-degree `D-a-5n/2`, where D is15 for A and25 for B. At a selected order `a+nr=mu`, its Euler degree including Y is `D-mu`. Cancellations cannot change this degree. The original combined degree15 therefore gives `mathscr D P=(15-6r)P=6hP`. Fractional p-powers obey this derivative literally in E; no common constant across branches or nilpotent coefficient ring is involved.

## 4. Every earlier B initial is excluded, including all kernels

By (1), after the same exact Morse substitution write

\[
\mathcal E_s(g(s,\zeta,p),p)=\sum_{n\ge0}e_n(s,p)\zeta^n,
\qquad\operatorname{ord}_s e_n\ge1\quad\text{for every n}. \tag{5}
\]

The uniform bound follows from substitution into `s*K[s,g,p]`; it does not require bounding a particular G coefficient or discarding b4, alpha, tau, delta or a constant. It also controls the infinitely many terms: at order nu, only `n<nu/r` are possible.

The reference `R_s^5=(xi_s+zeta²)^5` has order10r and a monic Y-degree10 initial. From (5), no term of E at or before10r has Y-degree10 or more. Therefore B has a nonzero initial Q at some `nu<=10r`; it cannot vanish identically. If `nu<10r`, its degree n satisfies

\[
n r\le\nu-1<\nu,\qquad n<10,\qquad
\mathscr D Q=(25-\nu)Q.                         \tag{6}
\]

The exact chain rule, with s constant, gives

\[
[A_s(g(s,\zeta,p),p),B_s(g(s,\zeta,p),p)]_{\zeta,p}
=cs^{36}g(s,\zeta,p)^2g_\zeta(s,\zeta,p).       \tag{7}
\]

After rescaling, its right-hand side has order exactly36: `g0²/(a p^(3/2))!=0`. The initial bracket coefficient on the left is `[P,Q]_{Y,p}` at order `5r+nu<=15r`. The two strata give respectively `15r<=135/4<36` or `15r<=30<36`. Thus `[P,Q]=0` even if its leading coefficient happens to cancel; equality with a nonzero target is never assumed away.

Here is the required elementary lower-B lemma. For monic P of degree6 and nonzero Q of degree n with leading coefficient q_n, the coefficient of `Y^(5+n)` in `[P,Q]` is `6q_n'`. Hence `q_n'=0`. On the other hand (6) gives

\[
p q_n'=(25-\nu-nh)q_n,
\qquad
25-\nu-nh>25-\frac{5\nu}{2r}>0.
\]

The first strict inequality uses `n<nu/r` and h>0; the second uses `nu<10r`. This contradicts `q_n!=0`. The same proof includes n=0. It does not require P to be Euler-homogeneous, nor require coefficients regular in p. **Every earlier B initial is excluded.**

## 5. The order10r contradiction

It follows that nu=10r. Q is monic of degree10 by (5), and the combined degree of B gives `mathscr D Q=10hQ`. The same strict target-order comparison gives `[P,Q]=0`. Euler elimination yields

\[
p[P,Q]=h(10P_YQ-6PQ_Y)=0.
\]

Therefore the Y derivative of `Q³/P⁵` is zero. Its value belongs to E, and monicity forces it to be1. Unique factorization in the FIELD polynomial ring E[Y] implies

\[
P=W^3,\qquad Q=W^5,
\quad W=Y^2+uY+v\ \text{monic}.
\]

Equation (4) has Y5 coefficient0 and Y4 coefficient3b. The corresponding two coefficients of W³ are3u and, after u=0,3v. Consequently `u=0`, `v=b`, and `W=Y²+b`. This forces `U=0`, contradicting its definition. These are two symbolic leading-coefficient projections, not an expanded degree6/10 pair calculation. A common quadratic alone would not be a contradiction; the correction degree at most3 is essential.

## 6. Scope checks, evidence and stop

The first stratum requires no L divisibility. The second imposes L and M divisibility explicitly and obtains its nonzero cubic Taylor coefficient from the literal source bounds. No implication from the pending simple-L theorem, no separated-sheet substitution, and no assumption on an earlier P0 constant was used. If `kappa<2r`, this proof does not supply a source exclusion: already the formal degree-two control `R_s=s+zeta²`, `r=1`, has reference order1 rather than2r. It refutes dropping the coalesced hypothesis, not the original source. Likewise (5) is load-bearing for monicity: without positive s-order, an added formal term `-zeta^10` could cancel the reference's degree10 leader. Neither control is a source point.

All denominators are fixed nonzero field elements or rational p functions inside the formal chart. Passing to Kbar and a finite Puiseux extension is legitimate for contradiction to a field-valued source; no same-ring isomorphism, nilpotent-base proof, inverse-lift equivalence or computed ideal certificate is asserted. Both rho embeddings and both Morse signs are covered, since signs cannot change the nonzero coefficients or order minima. All infinite-order cases are covered by the finite c_d order and by setting b=0 when xi vanishes.

This result establishes the stated COALESCED source exclusion only. It does not prove that every H-divisible source is coalesced, exclude all golden or common receivers, or settle JC2. Root retains review and composition authority.

Evidence consists of the whole proof above and three frozen input hashes, checked again at publication. No mathematical checker, sample census, CAS, high H/R powers, full source pair or row stream was executed or materialized. The optional formal controls are written scope counterexamples, not advertised as executable changed-object tests. The only subprocesses are bounded artifact publication/pin operations, using Python -I -B and no assertions for acceptance. No web, AWS, SSH, new agents, live peer artifacts, canonical edits or protected-tree inspection occurred. The own custody packet records exact current inputs and publication hashes. All writers finish before terminal handoff; STOP/IDLE.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `12109`.
- Body SHA-256:
  `5396b4d2029a85805efc008166a4339342af8bfbe6f0e00a4332a133bdbc1d78`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
