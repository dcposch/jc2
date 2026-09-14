# Minimal F2 receiver: fixed-field B reconstruction and one exact target gauge

Status: **PROVISIONAL COMPRESSION DISCRIMINATOR**, 2026-09-06. No A-dependent forcing or residual substitution was expanded. No CAS, builder, solve, point or AWS work. Frozen basis `0d39df3c9fd69c939a8420c54d03228b9077777d`.

## Outcome

The proposed reconstruction is valid for the exact full-face receiver contracts in the terminal preflight. The homogeneous B blocks have fixed coefficient-field matrices, with precisely four kernel coordinates at degrees5,10,15,20. All other free B coordinates are reconstructed triangularly from A, those four scalars and previously reconstructed higher blocks, using **only fixed nonzero coefficient-field divisors**. Known inner-face coefficients are forcing terms, not discarded columns or extra freedoms.

The same-field target shear `B -> B-[gamma^0*pi^15]B * A` removes the degree15 kernel coordinate and preserves every prescribed outer/inner face, monicity, c, fixed origin and—if included—all105 polynomiality rows. It adjusts lower B blocks as well; deleting a standalone H³ term without those adjustments is not the asserted operation.

| case | free A / free B before reconstruction | fixed-field B pivots | kernel coordinates | reduced coordinates after the target gauge |
|---|---:|---:|---:|---:|
| unequal | `71 / 196` | `192` | `4 -> 3` | `71+3=74` |
| common3 | `77 / 214` | `210` | `4 -> 3` | `77+3+2(c,z)=82` |
| common4 | `98 / 269` | `265` | `4 -> 3` | `98+3+2(c,z)=103` |

Keeping the two lift parameters adds two coordinates: **76 /84 /105**. These are presentation counts, not dimensions or existence results. Optional elimination of those two parameters belongs to the separate terminal lift contract; it is not needed or implemented here. Keeping all B nodes in a reconstruction circuit instead of substituting them does not literally reduce the ring's variable count unless their graph equations are used/eliminated.

**Critical residual boundary:** B degrees24 through1 use Jacobian total degrees37 through14. There is no B0 pivot, because the constant is fixed. Retain **all Jacobian degrees0 through13**, including degree13 as well as0–12, the actual target at degree2, and every unselected compatibility row in degrees14–37. Top degree38 is the known identity `[H³,H⁵]=0`, and may remain as a zero row. Reconstruction is not completion of the Jacobian or polynomiality equations.

## 1. Frozen inputs and coefficient fields

Consumed terminal inputs:

- T4 composition `xmodel/d125-minimal-monomial-receiver-composition-astra-20260906.md`, SHA `7dec79af1aa62946b46ecb209a710dd95e1b226b6b78229a3f232160a5385413`.
- Whole mathematical gate `xmodel/d125-minimal-receiver-gate-fable5-20260906.md`, SHA `cd69c23885de119e4bd910992dad5ef695e7b12013168ec1c401546d8aa6ed8d`.
- Whole exact-face/support preflight `xmodel/d125-minimal-receiver-client-preflight-astra-20260906.md`, SHA `e0debc7da22b8864ba43f0d29928e2104f2d8f161421ad26f29d8017f7b95e80`.

Work over k=Q or `k=Q[rho]/(rho²-3rho+1)`. Unknown coefficients range over an algebraically closed extension, not only k-rational points. A residual equation with golden coefficients is one equation over k; it must not be split into two independent equations in its rational/rho components. Pairs of rationals in the owned witness file represent **fixed field constants**, not a coefficient-field cut on unknowns. Both conjugate embeddings are retained.

The fixed outer forms are `A15=H³`, `B25=H⁵`, where

`H=pi²(pi³+gamma³)`, or `H=pi²(pi+gamma)(pi+(1-rho)gamma)²`.

Both have coefficient1 at pi⁵ and nonzero coefficient kappa at gamma³*pi², with kappa=1 orrho. The entire inner faces and origins are exactly those in the preflight: A0=B0=0; unequal low A endpoint1 and fixed `c=-5/(9*kappa)`; common inner parameter mu=1 and free c with `z*c-1`.

No live lift gate, baseline engineering output, code/log/receipt or protected project was consumed. The baseline exporter belongs to another agent and was not edited.

## 2. Same-field homogeneous kernel proof

For a homogeneous polynomial C of degree d, write

`H(gamma,pi)=gamma⁵ h(z)`, `C(gamma,pi)=gamma^d c(z)`, `z=pi/gamma`.

Direct differentiation gives

`[H,C]=gamma^(d+3) (5h c'-d h'c)`.

In both branches h has a **simple root at z=-1**: its derivative there is3 in the rational branch and rho² in the golden branch. Both are nonzero in k. If C!=0 and its bracket with H is zero, taking the order at that root in `5h c'-d h'c=0` gives

`5 ord_(-1)c=d`.

Thus 5 divides d. Write d=5r; then `(c/h^r)'=0` in k(z), so characteristic zero gives `c/h^r in k`. Conversely every scalar H^r commutes with H. Consequently

`ker(C homogeneous degree d -> [H,C]) = k H^(d/5)` if 5 divides d, and zero otherwise.

The case d=0 consists of constants, but B0 is already fixed. Also `[H³,C]=3H²[H,C]` has the same kernel because k[gamma,pi] is a domain. This is a same-field polynomial proof; no algebraic extension, generic point, unproved centralizer theorem or parameter localization is used. The projective root multiplicities have gcd1 in both cases; the simple rational root already suffices for the argument.

The primitivity condition is essential: replacing H by pi⁵ makes pi^d a kernel vector for every d. The actual fixed-matrix rank verifier rejects that changed H at d=24.

## 3. Literal free columns, known face rows and exact ranks

For each `1<=d<=24`, write

`B_d=K_d + sum_(i=0)^q_d b_(i,d-i) gamma^i pi^(d-i)`,

where K_d contains the **known inner-face terms** and every displayed b is free. The literal support/face quotient gives consecutive free columns with

`q_d=floor((7d+4)/12)` for unequal,

`q_d=min(d,floor((d+4)/2))` for common3,

`q_d=min(d,14)` for common4.

These formulas are checked against the full closed lattice sets with every prescribed outer/inner slot removed, including prescribed zero coefficients. For d<25 the known nonzero inner terms are:

- unequal: `K1=(5/(9*kappa))*gamma`, `K13=(5*kappa²/3)*gamma⁸*pi⁵`; other K_d=0.
- common3: at `d=5+2j`, `0<=j<=9`, `K_d=kappa⁵*binomial(10,j)*(-1)^(10-j)*gamma^(5+j)*pi^j`.
- common4: at `d=15+j`, `0<=j<=9`, `K_d=kappa⁵*binomial(10,j)*(-1)^(10-j)*gamma^15*pi^j`.

The j=10 terms meet B25 and are already in its fixed full outer face. B0=0. These known K_d are retained in every forcing expression.

Each H^r, `1<=r<=4`, lies in the free columns of degree5r. Indeed its support is a scaled subset of the convex B envelope, its gamma degree is at most3r, and its maximum B-inner weight is r for the unequal/common3 normals, or3r for common4. These are strictly below the prescribed B-inner weights5,5,15. It has no constant term and lies below degree25. Thus the unrestricted kernel vector is present in the actual free-slot subspace, rather than merely in a larger homogeneous space.

Let n_d=q_d+1. The exact restricted rank is

`rank L_d=n_d-1` for `d in {5,10,15,20}`, and `rank L_d=n_d` otherwise.

The table gives **columns/rank**, and applies separately to Q and the golden field:

| d | unequal | common3 | common4 |
|---:|---:|---:|---:|
|1|1/1|2/2|2/2|
|2|2/2|3/3|3/3|
|3|3/3|4/4|4/4|
|4|3/3|5/5|5/5|
|5|4/3|5/4|6/5|
|6|4/4|6/6|7/7|
|7|5/5|6/6|8/8|
|8|6/6|7/7|9/9|
|9|6/6|7/7|10/10|
|10|7/6|8/7|11/10|
|11|7/7|8/8|12/12|
|12|8/8|9/9|13/13|
|13|8/8|9/9|14/14|
|14|9/9|10/10|15/15|
|15|10/9|10/9|15/14|
|16|10/10|11/11|15/15|
|17|11/11|11/11|15/15|
|18|11/11|12/12|15/15|
|19|12/12|12/12|15/15|
|20|13/12|13/12|15/14|
|21|13/13|13/13|15/15|
|22|14/14|14/14|15/15|
|23|14/14|14/14|15/15|
|24|15/15|15/15|15/15|
|sum|196/192|214/210|269/265|

## 4. Checkable fixed-field pivot matrices

Write `H³=sum_(p=0)^9 h_p gamma^p pi^(15-p)`, with h0=1. The entry of L_d in output gamma exponent r and input column i is

`M_d[r,i]=(p*d-15*i) h_p`, `p=r+1-i`,

and zero if p is outside0..9. Output rows range0..d+13, so the matrices have at most **38 rows and15 columns**. The nonzero literal support uses only fixed field coefficients; no A-dependent entry occurs on this diagonal.

Rows `r=i-1`, columns `i=1..q_d`, give a triangular block with diagonal **-15i**. Hence q_d constant rational pivots are immediate. Set C0=1 and solve the associated homogeneous triangular system by

`C_i=(1/(15i))*sum_(j=0)^(i-1) ((i-j)d-15j) h_(i-j) C_j`.

If 5 divides d, the resulting vector is precisely the coefficient vector of H^(d/5), including trailing zeros. Every remaining matrix row annihilates it. Otherwise the first remaining nonzero row produces an exact scalar Schur coefficient S_d in k. The selected minor, in column order `1,...,q_d,0`, is

`((-15)^q_d*q_d!)*S_d != 0`.

This supplies one more fixed-field pivot. The scalar inverse is a coefficient-field constant, not a rational function of any receiver variable. In the golden field, the inverse of a+b*rho is `(a+3b-b*rho)/(a²+3ab+b²)`; the owned witness checks the denominator is nonzero for every selected S_d.

`exact-witnesses.json` records every block's selected rows, exact S_d and exact nonzero minor as canonical pairs of rational numbers, for all three cases and both fields. The checker recomputes them using the displayed recurrence and verifies an independent full-matrix rank modulo101 with rho=24. That modular check is only a rank crosscheck; **it is not a modular point, properness certificate or characteristic-zero nonemptiness claim**. The exact field computation already certifies the pivots. No A-dependent forcing is evaluated.

## 5. Descending reconstruction and all residual obligations

For d=24 down to1, the total-degree `(d+13)` Jacobian layer is

`[H³,B_d] + sum_(i+j=d+15, 0<=i<15, j>d) [A_i,B_j]`.

Terms involving B_j with j>d are already reconstructed, and K_d is fixed. No lower B_j can enter this layer because it would require an A degree greater than15. Thus the selected constant pivot rows solve B_d by a finite triangular circuit over the polynomial ring in A and the four kernel coordinates. At d=5r choose the free kernel coordinate as the literal coefficient `beta_r=[gamma^0*pi^(5r)]B`; H^r is monic in pi, and K_d has no such term.

All unselected rows of the layer remain as compatibility equations in A and the kernel coordinates. After the descent, **degrees0..13 of the Jacobian remain**, including the target at degree2 and degree13 (B0 is constant and supplies no pivot). The common scalar guard remains. If the105 lift rows are included, every one is retained with the reconstructed B; rank does not make any of them automatic. No irreducibility, old Moh condition or source-family equivalence is introduced.

Algebraically, using these triangular constant pivots and retaining every other row yields an exact coefficient-ring elimination: each solved variable is expressed polynomially over k in earlier variables, so the quotient is isomorphic to the smaller presentation with all substituted residuals. There are no hidden components lost to parameter denominators. This is an existence of a finite reconstruction circuit, **not an implementation of its possibly enormous expanded form**. The known fixed-face terms must participate in the forcing even when their own free-slot columns are absent.

## 6. Same-field target gauge and preservation of the lift equations

Let `s=[gamma^0*pi^15]B` and put `B'=B-s A`. Because the pi^15 coefficient of A is1, `[gamma^0*pi^15]B'=0`. The scalar s is a coefficient parameter, not a physical-variable function, so `[A,B']=[A,B]` identically.

All A support lies inside the corresponding B polygon; the owned lattice check verifies the inclusion. A has total degree15<25 and its maximum B-inner weight is3<5 in unequal/common3 or9<15 in common4. Therefore the **entire** fixed B outer and inner faces are unchanged. B monicity, every fixed nonorigin endpoint, c and its guard are unchanged. A0=B0=0 implies B'0=0. The operation is same-field and uses no root or inverse parameter.

The inverse description is `B=B'+sA` with an independent scalar s. Since `(0,15)` is a free B slot in all three cases, this gives a polynomial coordinate decomposition of the coefficient space into the gauge slice times an affine line. It removes one of the four kernel freedoms, specifically the degree15 one. It also changes the lower B coefficients, including the degree5/10 kernel coordinates in general; no claim is made that simply deleting beta_3*H³ alone would be a target shear.

For any chosen inverse-source parameters, coefficient extraction is linear, so the source pair changes by

`P'=P`, `Q'=Q-sP`.

Every P-negative row belongs to the Q-negative row envelope (30 rows are contained in75). Hence each Q lift row is changed by subtracting s times the corresponding P row, interpreted as zero outside the P envelope. Keeping all P rows makes this an invertible row operation on the full105-row ideal. This proves preservation of the full lift equations **without assuming a point already satisfies them**. The scalar guard is unchanged, and source degree125 exceeds75, so the exact Q leader is also unchanged.

Thus the gauge slice has exact same-field nonemptiness equivalence with the full receiver-plus-lift system, and indeed the described affine-line coefficient decomposition. This argument does not use the live lift gate. It makes no assertion about any additional external Roy/Moh pins not present in the frozen contract.

## 7. Controls, cost boundary and terminal custody

Owned `box/d125-minimal-receiver-b-reconstruction-20260906/check.py` performs only tiny exact coefficient-field arithmetic. It verifies the free slots and known-face removal, all24 block sizes per case, the rational triangular recurrence, all exact extra Schur pivots and their inverses, H^r kernels, sum ranks, independent mod101 full-matrix ranks, support inclusion and strict face weights for the gauge, a literal target-shear bracket/inverse/origin fixture, and inclusion of the lift-row index sets. Normal and `-O` runs pass. Actual changed-input controls replace H by the nonprimitive pi⁵ and feed a false kernel vector to the same matrix verifier; both are rejected in both modes.

All constant matrices and witness data fit below the stated 30-wall-second,25-CPU-second,512-MiB command caps. The exact rank run itself is small; **no solver runtime follows from it**. Descending substitution can produce substantial degree growth and dense coefficients in A and the remaining kernel parameters. Keeping a circuit may help, but its complete node count, compatibility-row expansion, CAS import and solve performance have not been measured. This optional discriminator does not authorize a descendant expansion or delay the separately owned baseline builder.

Registration, source pins, the exact witness file, replay and custody are in the owned box. No shared ledger, earlier artifact, protected project, live engineering or lift gate was read/edited. All owned writers finish before handoff; no process or worker is retained. **STOP:** fixed-field reconstruction and a valid gauge are banked, not a point, proper ideal, exclusion, expanded small system or solver win.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15099`.
- Body SHA-256:
  `cbfaa8a0e6a0079c6482c3fc67ba357180095e9eed46e92853243c5888d6f252`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
