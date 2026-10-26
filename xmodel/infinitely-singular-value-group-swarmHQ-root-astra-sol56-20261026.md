# Infinitely singular Keller eigenvaluations: a conditional ramification constraint

**Status:** PROMOTED / MANUAL / CONDITIONAL, after independent review. JC2 remains unresolved.
ROOT and Astra co-researched the calculation; configured Sol 5.6 supplied the independent review.
This is a source-qualified local/value-group result, not a degree-one or properness theorem. No novelty claim.

## Exact setting and imported premises
Let F be an actual complex polynomial plane Keller map, normalized by det DF=1, with field degree N>1.
Use the [reviewed dynamical input](keller-dynamical-minimization-swarmHQ-root-20260914.md): lambda=lambda_1(F) is an integer, lambda>=N, and an eigenvaluation nu in V_1 has finite thinness A(nu)=0.
This report concerns the case where nu is infinitely singular. Put K=C(x,y), K_0=F^*K, and Gamma=nu(K^*), normalized by value -1 on a generic affine linear polynomial.
**Mandatory additional premise:** equality of these normalized plane valuations identifies every finite essential Puiseux prefix, before first accumulation, up to compatible root-of-unity conjugacy.
This uses the plane-valuation classification/injectivity foundations cited by Favre–Jonsson; it does not follow from their displayed triangular normal form alone. The underlying dependencies [27], [28], [30] were not audited here.
The [independent review qualification](../box/infinitely-singular-value-group-swarmHQ-20261026/valuegroupreview1245-sol56-proof-gate-qualification.json) is part of the claim, not an optional caveat.

## Conditional conclusions
1. Gamma is lambda-divisible: lambda Gamma=Gamma. The selected eigenextension of K_0 to K has ramification index and residue degree e_*=f_*=1.
2. For every other existing valuation extension w of the same base restriction, f_w=1 and gcd(e_w,lambda)=1. Such an extension is again infinitely singular and centred at infinity.
3. In the local triangular normal form, the actual Keller volume forces an integral limiting exponent kappa and fixes the transverse coefficient mu=1/lambda.
None of these assertions counts the other extensions or proves N=1. No divisorial equality lambda=N is transferred to this case.

## Value-group calculation
For a subgroup Gamma of Q containing 1, let h_p=sup{a:1/p^a belongs to Gamma}.
Then [Gamma:lambda Gamma]=product over p|lambda with h_p finite of p^{v_p(lambda)}.
Indeed localization at p identifies a finite-height group with p^{-h_p}Z_(p), while infinite height gives Q; the finite quotient has precisely the displayed primary factors.
Nondiscreteness alone does not imply lambda-divisibility: the primes whose denominator heights are infinite must be identified.

## The actual volume calculation
The infinitely singular case of [Favre–Jonsson, Theorem 3.1(b)](https://annals.math.princeton.edu/wp-content/uploads/annals-v173-n1-p06-p.pdf) supplies analytic coordinates at a smooth boundary point with

    Phi(z,w)=(z^lambda, mu z^c w+P(z)),    c>=1, mu!=0, P(0)=0.

Write the pulled-back Keller form as Omega=z^ell H(z,w) dz wedge dw, with H an analytic unit.
The identity Phi^*Omega=Omega gives (lambda-1)(ell+1)+c=0 and, on units, lambda mu H(Phi)=H.
Evaluation at the fixed point gives lambda mu=1. Iteration to the superattracting fixed point then makes H constant.
Thus kappa=c/(lambda-1)=-ell-1 is a positive integer, and Omega is a constant times z^{-kappa-1} dz wedge dw.
These are local analytic identities; the coordinates are not asserted algebraic, and the local germ is not asserted finite.

## Essential prefixes and rational-function values
Before first accumulation, the essential Puiseux support transforms by T(beta)=(c+beta)/lambda, apart from the finite support contributed by P.
The explicit classification premise above makes this comparison legitimate prefix by prefix; no equality of unrestricted Hahn tails is used.
If every orbit terminated in the finite exceptional set or at kappa, the inverse map T^{-1}(beta)=lambda beta-c would bound all denominators, contradicting infinite singularity.
Hence an infinite nonstationary orbit exists below kappa, with beta_n=kappa+(beta_0-kappa)/lambda^n. The first accumulation is kappa.
Because kappa is integral, these exponents have unbounded p-denominator height for each prime p dividing lambda.
For a finite prefix h_j with denominator q_j, the product Q_j over its distinct root-of-unity conjugates detects the next exponent:

    nu(Q_j)/a = beta_{j+1}+c_j,    c_j in (1/q_j)Z,    a=nu(z)>0.

Earlier exponents bound the p-height of c_j; selecting successive record heights prevents cancellation of the new denominator.
The values obtained in analytic coordinates are rational-function values: finite positive valuation of the maximal ideal makes sufficiently high Taylor remainders have arbitrarily large value, in either coordinate system.
Thus Gamma has infinite p-height for every p|lambda, and the group formula proves lambda Gamma=Gamma.
The [producer proof](../box/infinitely-singular-value-group-swarmHQ-20261026/valuegroup1200-astra.md) and [independent review](../box/infinitely-singular-value-group-swarmHQ-20261026/valuegroupreview1245-sol56.md) retain the detailed argument and its source limits.

## Other extensions and the surviving global gap
For an existing extension w, the [one-extension valuation inequality](https://stacks.math.columbia.edu/tag/0ASF) gives e_w f_w<=N. Only Lemma 15.125.2 and its displayed proof were admitted here.
Its residue field is a finite extension of C and hence C. Its value group is a finite-index rational overgroup of the base group lambda Gamma=Gamma.
Infinite p-height persists in that overgroup, and a finite quotient by a p-divisible subgroup has no p-primary part. Therefore gcd(e_w,lambda)=1.
The group remains nondiscrete; the residue is C; the centre is at infinity since the base contains a polynomial of negative value. The named four-type classification makes w infinitely singular.
A Keller map in the exceptional skew-product alternative would satisfy P'(x)Q_y(x,y)=constant, hence be triangular of degree one; that alternative is excluded for N>1.
Favre–Jonsson's eventual contraction of visible boundary primes is still insufficient: other lifts may lie at different or infinitely near centres, including resolution exceptionals not controlled by that statement.
Uniqueness of a fixed eigenvaluation is not uniqueness of its backward valuation fibre. No summed degree formula, defectlessness or extension-count theorem is imported.
The remaining task is a global constraint on all extensions or their centres; the calculation above alone neither supplies it nor excludes N>1.

## Verification and source scope
ROOT read producer 92/92 LF, review 107/107 LF, and the mandatory qualification 10/10 LF; canonical seals, fixed physical inputs and launch archive blobs passed fresh checks.
The independent review is PASS / CONDITIONAL / GLOBAL GAP. ROOT is a co-researcher, not a second independent reviewer; no separate review of this integration's formatting is claimed.
FJ was read in selected windows only; its PDF was binary-gated, and the foundational dependencies were not audited. The Stacks source was restricted to one extension and supplies no degree sum.
The [evidence index](../box/infinitely-singular-value-group-swarmHQ-20261026/README.md) preserves original reports and qualification byte for byte, plus source hashes and bounded coverage.

## OPENS RAISED
None. The existing infinitely singular global extension-count/degree gap remains.

## COLLISIONS
Frozen-public collision output is retained in the evidence package. An empty lexical result is not novelty evidence.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7643`.
- Body SHA-256:
  `24088497a7d77dc6cc6e6dc4989041c151e9fb391f1213b93a05187008e9cdde`.
- Frozen basis: `4859301bf066fe77efb1998a39a8dacb0d165a17`.
