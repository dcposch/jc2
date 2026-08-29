# Hostile review: Section 7 resolution-free quotient repair

Date: 2026-08-28  
Reviewer: GPT-5.6-terra / Codex  
Reviewed coordinator hash: `71aba565608db6e882b6ffd724ab82a14d3de5b678500221190fea4f24904eea`  
Overall verdict: **FAIL AS FILED; the repair is close, but quotient-level
cross-fibre transport and weight transport are not yet well-defined as
written.**

The resolution-free idea is legitimate: no common divisor or compactification
is needed if a fixed abstract coefficient quotient is put in bijection with
clusters.  The report correctly imports, rather than hides, the every-fibre
Proposition 5.8 replacement.  Its failure is narrower: corrected Statement
3.14 gives a common root-of-unity *coordinate change*, not automatically the
identity on `eta^m`.  The induced quotient-line isomorphism must be chosen and
tracked.  In addition, preservation of the repaired jump/max `kappa_F` is not
proved by matching the prefix below `u` alone.

## Clause ledger

| clause | verdict | hostile check and smallest repair |
|---|---|---|
| Arbitrary rational stabilizer on the `y`-side | **PASS** | With `e=gcd(K,{r<n:c_r!=0})`, including `K`, `mu_e` fixes `x=t^(-K)` and the prefix.  Its action `eta -> zeta^(-n)eta` has effective order `m=e/gcd(e,n)`.  Thus `C[eta]^(mu_m)=C[eta^m]`. |
| `x`-side and denominator refinement | **PASS** | Interchanging `x,y` gives the same action.  Under `K'=LK`, `t=(t')^L` scales `n,e,N` by `L`, so `m` is unchanged.  For transport to a new fibre, say explicitly that a pairwise common multiple may be chosen; no single denominator over all `a` is required. |
| Zero-order descent | **PASS** | The finite Laurent expansion gives `H_N(zeta^(-n)eta)=zeta^(-N)H_N(eta)`.  At `d_(h,F)=0`, the selected source index is `N=0`; hence `p_(h,F)` is invariant and descends to a polynomial in `z=eta^m`.  This is valid for `f-a` and `g` at a cv flag. |
| The quotient is the EW2 geometric root-orbit quotient | **CONDITIONAL** | The deck calculation gives a formal orbit quotient.  The report must explicitly identify its `mu_m`-orbits with the “root orbits” in EW2/Notation 3.8 for arbitrary rational `u`: reparametrization by `mu_e` yields the same outgoing direction, and distinct effective orbits are distinct directions.  EW2 as restated says that root orbits give directions, but does not name this newly constructed group.  Add this identification (or make it an explicit corrected input). |
| Exact Statement 3.14 aligned-prefix/common-twist content | **FAIL** | Corrected Statement 3.14 only supplies residual patterns after one common root-of-unity change `eta_ref=omega eta_a`.  The report replaces this by equality of functions on one fixed quotient line.  If `omega^m!=1`, the induced map is `z_ref=omega^m z_a`, not the identity.  Thus (4.1), as written in an independently chosen target coordinate, is unsupported. |
| Formal witness to that defect | **FAIL** | Take `m=2`, a descended reference residual `P(z)=z`, and an allowed common cover twist `eta_ref=i eta_a`.  Then `z_ref=-z_a`, so the transported residual is `-z_a-a`, not `P(z_a)-a`.  This is not a counterexample after identifying the two quotient lines by `z_ref=-z_a`; it is a counterexample to the report's untracked identity claim. |
| Correct quotient-level transport | **CONDITIONAL** | For every `i,a`, choose an aligned-cover isomorphism `eta_ref=omega eta_a` and define `tau_(i,a):U_(F_i(a))->U_i` by `[eta_a] -> [omega eta_a]`.  Then define the target parameter to be `z=tau_(i,a)([eta_a])`; (4.1) is true in that transported parameter.  Prove that another aligned choice differs by a prefix stabilizer, so `tau_(i,a)` is independent of the choice.  A scalar not in the stabilizer merely makes `tau` a nontrivial automorphism of `A1_z`; it is not removed by taking the quotient. |
| Preservation of `d_g=0` | **PASS after the preceding `tau` is recorded** | A common aligned expansion preserves every Laurent exponent of the fixed polynomial `g`, hence its zero order.  This gives the cv condition together with the centred first residual equation. |
| Preservation of `kappa_F` and cluster weight | **FAIL** | “The prefix and current gcd index agree” is not enough for the repaired `kappa_F`: at a characteristic height the relevant jump data involve the current characteristic/contact presentation, and printed Notation 3.5 was already ambiguous.  The report must invoke the corrected jump/max convention and prove/cite that Statement 3.14 preserves the rooted contact-jump data.  Only then is `b_F=kappa_F(pi(F)-1)` constant across the transported family. |
| Every `z` is realized after `a=P_i(z)` | **CONDITIONAL** | Once `tau_(i,a)` and the EW2-orbit identification are installed, `P_i(z)=a` makes the corresponding covered orbit a centred root and EW2 realizes it.  As filed the target coordinate may be off by `omega^m`, so this inference is not valid for the displayed `z`. |
| Surjectivity to all finite-value clusters | **CONDITIONAL** | EW1 gives the unique flag and corrected Statement 3.14 gives its unique reference flag; EW2 then gives its orbit.  The result is a unique reference point only after the quotient transport `tau_(i,a)` is fixed. |
| No cyclic and no cross-flag duplication | **CONDITIONAL** | Cyclic injectivity follows from the required orbit-quotient identification.  Cross-flag injectivity additionally uses injectivity of the corrected Statement 3.14 tree isomorphism: if a cluster has flag `F_i(a)=F_j(a)`, transport back gives `i=j`.  Merely saying one puncture has one flag omits this intermediate possibility. |
| `P_i` nonconstant and finite fibres | **PASS, after transport is repaired** | For each `a`, the transported reference cv flag has an actual centred root by the aligned construction/EW2, so the correctly transported `P_i(z)=a` has a solution.  Thus `P_i` is nonconstant and `varphi_i` has finite fibres. |
| Generic covered-root simplicity, including `z=0` | **PASS, after transport is repaired** | Avoid the finite critical-value sets of all `P_i` and, for `m_i>1`, avoid `P_i(0)`.  Then a simple quotient root is nonzero and remains simple in `eta` because `d(eta^m)/deta` is nonzero.  This is exactly the required hypothesis for the simple clause of repaired Proposition 7.3. |
| Every-fibre Proposition 5.8 | **PASS** | The report states the exact reviewed replacement and hash, and uses it only for the all-fibre meromorphic-degree identity in (7.1).  Its polynomial-Keller and normalized-fibre scope is the required one; it is not derivable from EW1--EW4. |
| Constructibility and Euler-Fubini | **PASS, conditional on the cluster bijection** | A polynomial `P_i` with positive degree makes `varphi_i:A1->A2` quasi-finite; its geometric fibre count is constructible and has compact-Euler integral `chi_c(A1)=1`.  Keller étaleness gives quasi-finiteness of `Phi`, so `integral N dchi_c=chi_c(A2)=1`.  Ramification and shared image curves are handled correctly by source-point counts. |
| Global `(22-cl)` | **FAIL AS FILED** | The Euler algebra after (5.2) is correct, and the explicit Proposition 5.8 import is sufficient on that side.  But (5.2) and the constancy of `b_i` remain unproved for the displayed fixed lines, so the theorem is not yet licensed globally. |

## Minimal clean repair

Replace the claim that “the quotient removes” the Statement 3.14 twist by
the following transport lemma.

```text
For every reference flag F_i and every a, an aligned Puiseux presentation
induces an isomorphism tau_(i,a): U_(F_i(a)) -> U_i.  If
eta_ref=omega eta_a on the covers, then
tau_(i,a)([eta_a])=[omega eta_a].  A different aligned choice differs by
the prefix stabilizer and hence gives the same quotient isomorphism.
In this transported coordinate,
p_(f-a,F_i(a)) = P_i-a and p_(g,F_i(a))=Q_i.
```

Add the elementary bridge saying that its effective deck orbits are exactly
EW2's root orbits/directions, and cite the corrected jump/max transport lemma
for `kappa` (hence `b_i`).  Then the report's set-bijection, genericity, and
constructible Euler calculation go through without a common resolution.  No
divisorial or final-boundary claim needs to be restored.
