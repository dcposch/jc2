# Q3 scratch note: algebraic bridge, bounded search, real size limits

Only the frozen packet, tacnode, t8 gate, and FALLACY-v2 were read. The parent verified all charged hashes. No uncharged report, ledger, worker copy, or Lean tree was used. Computations below ran in memory; this is the only file written by this sublane.

## 1. The bridge actually printed

Put A=4eta+3b*l2. Frozen `k16-tacnode-fable5-20260905.md:185–207` proves A^2+4T2+24E2=0, wt(A)=2t, wt(T2)=4t. The identity applies algebraically also at b=0; the interpretation j0=ord(D) only applies at b!=0. `:224–245` gives the weights and low-index memberships. `:264–270` explicitly states that A in sqrt(J) only reduces (R) to the additional radical assertion B*eta in sqrt(J+(A)). Thus packet:17's displayed equivalence needs an extra printed bridge; it is not supplied by the tacnode theorem.

A ring lemma sufficient for combining future certificates is: for a commutative ring S and ideal I, if A^e belongs to I and f^q belongs to I+(A), then f^(eq) belongs to I. Proof: write f^q=uA+i and raise to the e-th power; every term is in I. Taking f=B*eta gives the missing second obligation explicitly. This is suitable for a small future Lean proof without importing algebraic geometry. Here no Lean work is authorized/performed.

## 2. A universal emitter, derived directly from the printed UF

Source: tacnode:44–48 prints UF, the jets, p=1/(4(2d+1)), and 3d^2=N=t+1. Normalize its unit y by (L,b,P,B,eta) -> (yL,yb,y^2P,y^2B,y^2eta); UF scales by y^4. Now

    L=x^N+c1*x^(N-1)+...+c_(N-2)*x^2-b,
    P_(2N)=p=1/(4(2d+1)), 3d^2=N,
    F=(theta-3)(P^2)+(3/2)L(L+b)P-BxP
      -(3/16)L^2*(L*(L+2b)-4Bx)+eta*x^2*(bL/2+Bx).

The coefficient of the new unknown P_(2N-r) in [x^(4N-r)]F is

    K_r=2(4N-r-3)p+3/2=(4N-r+6d)/(2(2d+1)).

For every integer N>=4 and 1<=r<=2N this is nonzero on BOTH field factors. Indeed the smaller real numerator is at least 2N-2sqrt(3N)>0; 2d+1 is nonzero. Thus the high spine can be emitted directly by coefficient convolution and exact divisions, with every actual modular pivot checked. The N=3,d=-1 resonance is excluded deliberately and matches the printed exceptional family at tacnode:144–146.

The high coefficients determine P down to P1; P2=eta and P1=-B then determine the corresponding marked parameters when their actual linear pivots are units. Set P0=-b^2/4. The residual rows are F_k for 4<=k<=2N, with weights 4N-k, in S=k[c1,...,c_(N-2),b], weights (1,...,N-2,N). Rather than assume those two last pivots uniformly, an implementation may retain B,eta and both matching equations until they are proved invertible. The N=4 finite check below checks them explicitly.

## 3. Small rejected idea: B rows are not a diagonal-rescaled gradient

From t8 gate:46–59 the B_r weights are N+r, r=1,...,N-2. These match the derivatives of a potential of weight 2N-1, differentiating by c_(N-1-r). A tempting cheap ansatz was therefore lambda_r B_r=partial(V)/partial(c_(N-1-r)), with nonzero constants lambda_r. It is already false in the directly regenerated N=4 UF system.

Computation ring/order: F_31991[c1,c2,b,B,eta], d=14162, 3d^2=4; p=21936. These prime/root controls are printed at tacnode:210–218. All high K_r used are units. B's jet pivot is 20072. Convolution checks give every F_k=0 for k<4 and k>8 after jet reconstruction. Write T_r=F_(8-r)=a_r b^2+b_r b+c_r, r=0,1,2. The scalar a0=4807 is a unit. Set B_r=a0*b_r-a_r*b0. Direct coefficient extraction gives

    B1=29578*c1^5+18265*c1^3*c2+31707*c1*c2^2,
    B2=2518*c1^6+13633*c1^4*c2+28635*c1^2*c2^2+24177*c2^3.

The c1^4 and c1^2*c2 coefficients of partial_c1(B1) are (19926,22804), and those of partial_c2(B2) are (13633,25279). Their proportionality minor is 12665 mod 31991, NONZERO. Thus no constant diagonal rescaling makes these two derivatives equal. This is a negative test of this precise ansatz, not of potentials after triangular changes of coordinates or polynomial row operations. Fresh-zero polynomial objects were used in the final computation; an earlier scratch implementation accidentally aliased its zero during coefficient extraction and was discarded. Final run exits 0 and checks the nonzero minor explicitly. The original independent N=5,6 exploration also found nonproportional derivatives, but N=4 alone suffices.

## 4. A bounded uniform certificate lane worth pricing, not claiming

Target exact identities A^e(t) in J_t and (B*eta)^q(t) in J_t+(A). A possible starting exponent schedule is e(t)=ceil(t/2)+1, q(t)=ceil(t/4)+1. These are ANSATZ bounds, not consequences of the printed finite data or a theorem. The first matches the printed A nilpotence powers at t=3,4,5; the second safely includes the displayed residual memberships but need not be minimal.

Do not assemble the whole Macaulay matrix. Search a dictionary of at most 128 coefficient-convolution templates

    [x^m] L(x)^a P(x)^b (theta^j F)(x),  j<=2,

with m fixed by the target weight and 4N-k row weights, and total L/P exponent within two of the minimum required by that weight. Add at most 128 analogous templates multiplied by A for the residual assertion. Require scalar template coefficients to be affine in (N,d), or, after clearing a predeclared product of actual spine pivots, to have numerator total degree<=2. Specify the exponent/shift list before fitting. Every template is a compact family of legitimate cofactors for the FULL terminal rows, including the truncation boundary; it is not a residue argument. A discrete telescoping identity in coefficient index would be the output.

Instrument: regenerate UF at t=3,...,6, solve the bounded coefficient system by modular evaluation, reserve independent coefficient assignments, both d signs and t=7,8 as holdouts, then prove any survivor as a formal coefficient identity for arbitrary N. Finite passing data never certify the uniform identity. If the chosen dictionary has no exact solution, or a held-out evaluation differs, reject that dictionary and stop after one expansion to 256 templates. A modular mismatch refutes a fully specified p-integral candidate identity; modular nonmembership alone need not refute an unrestricted rational certificate. No candidate identity is presently found.

Price: one 3-hour lane, 2 vCPU, 8 GiB RAM, <=8 MB retained notes/candidate formulas; no host matrix dumps. An extra 3-hour symbolic proof allocation is conditional on a holdout survivor. Failure within this cap is a useful negative result, not an index promotion. This lane offers a uniform theorem if it succeeds, whereas a new t=9 calculation offers one more index.

## 5. Why ordinary Macaulay and t9 norm jobs need honest prices

Exact Hilbert-count DP using the declared weights, e(t)=ceil(t/2)+1 and target W=2t*e(t) gives the following full homogeneous Macaulay dimensions. Cofactor columns sum h_(W-d) for every terminal generator degree d=2(t+1),...,4t; rows are h_W. Counts are independent of generator coefficients.

|t|W|Monomial rows|Cofactor columns|Dense storage at 4 bytes/entry|
|---|---:|---:|---:|---:|
|6|48|6,917|11,266|0.312 GB|
|7|70|85,442|187,597|64.1 GB|
|8|80|377,981|760,767|1.15 TB|
|9|108|5,117,251|13,195,731|270 TB|

These are raw matrix dimensions, not lower bounds for all algorithms. They refute a price for a generic dense t9 Macaulay job inside 64 GiB. Sparse templates or compressed quotient multiplication must do real work before the resource claim becomes credible.

For the orbit-free rank construction in t8 gate:46–81, the uniform scalar target is the weighted resultant of top rows F_(2N),...,F_(N+2) in N-1 variables of weights (1,...,N-2,N). Its nonvanishing is equivalent to the top-tail cone having only the vertex, hence is stronger than the requested T2 target. A resultant proof can avoid irreducibility and selected points, as the fixed t8 gate did. A conjectural finite-width block elimination for its Koszul resultant matrix would be a plausible uniform instrument; a finite list of nonzero resultant values is not a proof.

Conditionally on the expected-height determinantal resolution, put k=N-2. The weighted rank-cone degree is

    dGamma(N)= [u^(k-1)] { product_(r=1)^k (1+(N+r)u)/(1-Nu) } / k!.

At N=9 it gives 52140, agreeing exactly with t8 gate:196. At N=10 it gives 3064347/10; at N=11 it gives 1817465. These are CONE degrees, not measured affine lengths. The t9 main chart could therefore have roughly 306,000-dimensional multiplication algebra; a dense matrix at 4 bytes/entry costs about 376 GB. A feasible t9 lane needs certified sparse multiplication or more memory, and must retain every boundary chart. Neither the expected-height hypothesis nor the boundary contribution has been measured at t9 here.

Finally, a mod-p unit result on J+(A-1) cannot by itself be promoted by properness. Generic points with A!=0 may specialize to A=0 in the projective family. The printed t8 proof promotes WHOLE-cone emptiness (t8 gate:121–148), not arbitrary affine target emptiness. Exact characteristic-zero power identities are safe; a modular target computation is only a detector until its missing lifting hypothesis is proved.

No new exit price is asserted.
