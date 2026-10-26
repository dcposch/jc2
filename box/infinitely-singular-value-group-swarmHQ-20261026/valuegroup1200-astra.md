# VALUEGROUP1200 — the eigenextension index and the unresolved global extensions
Author: retained primary Astra, freshglobal1740_astra; co-research, not independent review.
Basis: 9e18a9552f1a978847c64295de48d1c0fe8b4464; frozen public 4859301bf066fe77efb1998a39a8dacb0d165a17.
Status: INTERNAL / UNPROMOTED. Branch-specific progress at the explicit FJ plane-valuation/normal-form import tier; the actual global degree conclusion remains GAP. No JC2 proof or counterexample, no successor.

## Scope and exact source tier
Let F be an actual normalized polynomial Keller map (det DF=1) of generic field degree N>1. Use only the reviewed starting eigenvaluation nu with lambda=lambda1(F) an integer >=N, F_*nu=lambda nu, finite thinness A(nu)=0, and nu infinitely singular. In particular N<lambda^2. Put K=C(x,y), K0=F* K, and Gamma=nu(K*), normalized by nu(generic affine linear function)=-1.
The pinned FJ2011 text supplies the plane Puiseux description in Section1.2, the eigenvaluation framework in Propositions2.3/2.5, and the analytic triangular normal form in Theorem3.1(b), explicitly assigned to the infinitely singular case at lines538-548. Theorem3.1 is used as a named source theorem, not reconstructed here from all its dependencies.
The printed normal-form proof invokes earlier [30]Theorem7.7 and the rigid-germ classification[27]. The plane-valuation foundations are likewise cited by FJ to [30]/[28]. These underlying works were NOT newly accessed or independently audited. The derivation below spells out the finite-prefix and value-group steps beyond those named imports; it is not a new proof of the complete plane classification.
The sole added valuation-theoretic source is selected Stacks15.125.2 and its proof: for ONE extension, e_v f_v<=N. No summed equality, defectless theorem, henselization degree formula or uniqueness theorem is imported. The cached FJ2011 is distinct from stopped Favre2010. The mismatching current INTAKE is unused.

## Scaling is not ramification index
Under the identification K~=K0 induced by F*, the restricted valuation is lambda nu. Thus its value group is lambda Gamma, and the eigenextension has
  e_*=[Gamma:lambda Gamma],     f_*=[C:C]=1.               (1)
The residue assertion is justified below. The admitted inequality is e_* f_*<=N, not lambda<=N. The existing H_m=(y,y^m-x) check already has generic degree1 and scaling m; it was not rerun or extended into a family.
For any additive subgroup Gamma of Q containing1, set h_p=sup{a>=0:1/p^a belongs to Gamma}. Then for any positive integer lambda,
  [Gamma:lambda Gamma]=product_(p|lambda, h_p finite) p^v_p(lambda).   (2)
Here infinity is allowed for h_p. Non-discreteness alone does not make the product empty.
To prove (2), first note that a/b in reduced form belongs to Gamma only if 1/b does, by Bezout. Thus membership is determined by the allowed prime-power denominator heights; conversely, Bezout expresses 1/b as an integer combination of its prime-power reciprocal factors.
If h_p is infinite, these denominator rules show pGamma=Gamma. If h_p=h is finite, reduction of p^h gamma modulo p is a surjective map Gamma->F_p whose kernel is pGamma. The kernel assertion follows because division by p then stays within the allowed heights. Hence [Gamma:pGamma]=p. Multiplication identifies successive subgroup indices, proving (2) prime by prime.
This is a group calculation only. Abstract groups with various heights are not Keller maps or valuation realizations. The actual dynamical prime-height input must come separately.

## Plane valuation facts and the analytic coordinate transfer
For an infinitely singular plane valuation, the local Puiseux description writes w=h(z)=sum a_j z^beta_j, with a_j nonzero and beta_j positive increasing rational numbers whose denominators are unbounded; normalize by a=nu(z)>0. Only the essential initial sequence before its first accumulation exponent is needed. Its order is omega; terms beyond that accumulation may be invisible to the valuation and are not identified in the argument.
We use the local description at the regular boundary parameter z in FJ's normal-form coordinates. Equivalently, one performs the finite Newton/Puiseux approximations in that regular coordinate pair: cancel the leading coefficient after a finite ramification z=t^q and repeat. Rational values and residue C determine each finite step. Infinite singularity is precisely the unbounded-denominator alternative rather than the divisorial, irrational or bounded-denominator formal-curve alternatives. This local plane-classification input is included in the named tier above.
Evaluation in this Puiseux description shows Gamma is a subgroup of Q containing1, and the residue field is C: a value-zero rational function has as residue the ratio of its leading complex coefficients. Non-discreteness, and detection of particular denominator heights, follow from the finite-prefix products described next, rather than from treating every exponent as itself a rational-function value.
For a finite prefix h_j of common minimal denominator q_j, take the product Q_j(z,w)=product_sigma(w-sigma(h_j(z))) over its distinct Puiseux conjugates. This has coefficients in C[z] in local positive exponents (or C[z,z^-1] before moving to the local chart). At the chosen branch one factor has next value a beta_(j+1); all other factors have first-difference values from earlier exponents. Therefore
  nu(Q_j)/a=beta_(j+1)+c_j,    c_j in (1/q_j)Z.            (3)
Whenever a new exponent has larger p-denominator height than all preceding ones, (3) detects that new height in a value. Multiplication by the fixed nonzero rational a changes heights by only a bounded amount. Unbounded p-heights of essential exponents therefore imply infinite p-height in Gamma.
Analytic normal-form coordinates do not enlarge the rational value group for this purpose. In rational regular local parameters u,v at p, put epsilon=min(nu(u),nu(v))>0. An analytic germ of finite value has the same value as a sufficiently high Taylor polynomial: the remainder lies in m^k and has value >=k epsilon. Apply the inverse analytic coordinate change as well. Hence every finite value used in (3) is attained by a rational function on the algebraic surface, and conversely. No algebraicity of z,w is asserted.

## The actual infinitely singular normal form forces the relevant prime heights
FJ Theorem3.1(b), with its stated hypotheses, supplies local analytic coordinates at the centre p of nu in which
  Phi(z,w)=(z^lambda, mu z^c w+P(z)),
  c>=1, mu!=0, P(0)=0, and the local boundary is z=0.      (4)
This is a holomorphic germ of the actual lifted map. It is NOT a finite global polynomial model, and its visible exponent lambda is not declared to be N.
The actual Keller volume identity gives an extra constraint here. Since p is smooth with sole boundary z=0, write Omega=z^ell H(z,w) dz wedge dw, where ell is an integer and H is an analytic unit. Pulling back under (4) gives
  (lambda-1)(ell+1)+c=0,    lambda mu H(Phi(z,w))=H(z,w).
Evaluation at p gives lambda mu=1. Then H composed with Phi equals H, and iteration toward the superattracting fixed point forces H constant. Consequently kappa=c/(lambda-1)=-ell-1 is a POSITIVE INTEGER and Omega is a constant multiple of z^(-kappa-1) dz wedge dw. No global rationality of these coordinates follows.
The image Puiseux expression in t=z^lambda is
  h_F(t)=mu t^(c/lambda)h(t^(1/lambda))+P(t^(1/lambda)).   (5)
Since F_*nu=lambda nu, h_F and h determine the same normalized valuation. Their essential finite Puiseux prefixes therefore coincide up to compatible roots-of-unity characters. Those characters change coefficients but not exponents.
Here is the finite-prefix justification for that last assertion. Products Q_j over conjugate prefixes detect the first exponent at which two branches differ. If their next exponents differ, their Q_j-values differ. Once that exponent is fixed, products for the next candidate prefix detect its coefficient up to the finite stabilizer of the preceding prefix. Induction gives compatible conjugate choices at every finite stage. This identifies precisely the essential initial sequence, not any arbitrary Hahn-series tails after accumulation.
Let S be this essential support, let B be its first accumulation exponent (possibly +infinity), and put T(beta)=(c+beta)/lambda. Formula (5) changes T(S) only at the finite set of exponents of P(t^(1/lambda)), with cancellation allowed there. Its first infinite accumulation is T(B). Equality of the essential prefixes gives B=T(B).
If B is finite it equals kappa=c/(lambda-1), and supports are compared only below kappa. If B is infinite there is no cutoff. In either case, away from that finite polynomial-support set, forward application of T preserves membership in S as long as it stays in the essential range.
There must be a nonstationary infinite forward T-orbit in S. Otherwise every beta in S would eventually reach the finite exceptional set or kappa. Backward T is beta->lambda beta-c, an integer-affine map, so all those backward orbits have bounded denominators. This contradicts the unbounded denominators of S.
A nonstationary forward orbit above kappa would be strictly decreasing, impossible in the increasing essential support. Hence its starting beta_0 is below kappa, and
  beta_n=kappa+(beta_0-kappa)/lambda^n increases to kappa. (6)
In the case B=+infinity, (6) would give an infinite bounded subsequence of the initial increasing sequence, a contradiction. Thus B=kappa, and (6) lies throughout the essential range where the comparison is justified.
For every prime p|lambda, kappa is p-integral because p does not divide lambda-1. The second term in (6) has p-adic order v_p(beta_0-kappa)-n v_p(lambda), tending to minus infinity. Therefore the reduced denominators in (6) have unbounded p-height. Taking successive new-height records and using (3) transfers this to Gamma.
Consequently, at the explicit FJ plane-Puiseux/normal-form tier,
  pGamma=Gamma for every p|lambda;  lambda Gamma=Gamma;
  e_*=1 and f_*=1.                                      (7)
Equation (7) comes from the actual local dynamics, not from non-discreteness alone. The selected one-extension inequality now says only 1<=N. It does not imply N=1.

## Other extensions: actual constraints, but not exclusion
Consider any other extension w to K of the valuation on K0 fixed above. The selected Stacks inequality makes Gamma_w a finite-index extension of the base group lambda Gamma=Gamma and its residue a finite extension of C. Thus its residue is C and e_w<=N.
The group Gamma_w is again rank one and rational: multiplying any element by its finite quotient order places it in Gamma. It is nondiscrete since it contains Gamma. A finite-index rational overgroup preserves every infinite prime height, so Gamma_w is p-divisible for each p|lambda. The finite quotient Gamma_w/Gamma is then p-divisible and has no p-primary part. Thus
  gcd(e_w,lambda)=1,    f_w=1.                           (8)
These statements concern each existing extension; they do not import a summed fundamental equality or supply a count exhausting N.
Every such extension has centre at infinity on the original source plane: a valuation centred at an affine point is nonnegative on all source polynomials, contradicting its negative value on F*(a generic affine target linear function). The four-type plane classification, together with rational rank one and nondiscreteness, then makes w infinitely singular. Divisorial and curve types have discrete groups; irrational type has rational rank two.
Nothing proved makes w fixed under F_bullet or places it in V1. FJ Theorem2.4(a) is uniqueness of a FIXED eigenvaluation with alpha>=0, not uniqueness of preimages or field extensions. The displayed Jacobian use at450-454 is stated on V1; it is not applied here to every w without a subtree argument.
Even if a separate defectless total-degree equality were later justified, (7) would merely leave N=1 plus the contributions from the other extensions. Their exclusion is still required. No henselian or complete-field hypothesis is silently added to the rational function field.

## The attempted global dynamical closing step and its exact failure
The actual Keller condition does exclude the skew-product exception in FJ Theorem3.1: after a polynomial conjugacy, a skew product has Jacobian P'(x)Q_y(x,y)=constant. Both factors are then constant, making P linear and Q linear in y, hence the map an automorphism. This is incompatible with N>1.
Therefore Theorem3.1's eventual contraction conclusion applies to every visible boundary prime on its chosen tight compactification. The printed argument568-578 proves this by attracting each such divisorial valuation to the chart p.
This does not control all centres infinitely near boundary points or exceptional curves appearing when the rational lift is resolved. Nor does forward contraction of those visible primes make the neighbourhood of p backward invariant for every valuation extension. Other lifts can lie outside the analytic chart used in (4).
The first failed global inference is thus: eigenextension e=f=1 plus an attracting germ and eventual contraction of the chosen model's boundary primes implies that this is the only valuation extension of the target eigenvaluation. No such implication follows from the cited theorem or the one-extension inequality.
A valid completion would have to show that ALL extensions enter a common controlled backward fibre and coincide, together with an appropriate total-degree theorem at the actual valued-field scope. Neither a global injectivity statement for the tree nor absence of hidden resolution contributions has been established here.
The local small-segment homeomorphism statement at FJ369-371 is only a pointer to[30]Theorem7.4 and is not used as global injectivity. The analytic triangular expression is not used to count global sheets. No divisorial lambda=N, unique extension, residue theorem, or compact Y/W attachment has been transferred to this branch.

## Coverage and disposition
This is a scoped ramification-index calculation and an actual-global GAP certificate. It neither proves the infinitely singular alternative impossible nor rules out all uses of valuation dynamics. No general minimization, degree search, new control family or successor is proposed.
Fresh fixed28 physical pins include the PDF as binary bytes/hash/mode with lines=null; all12 archive physical/current-launch comparisons, STATE launch equality and two canonical parent verifiers passed. The legacy Fable review was ordinary pinned text, not canonically verified. The cached PDF was not newly visually read; selected LF text windows supplied the source reading.
Whole frozen STATE196 was personally read before mathematics. Selected producer/review, source-scope and Stacks proof readings, exact FJ windows, named unread dependencies, fresh postpins and original lifecycle/verifier/collision streams are recorded separately. There is no whole-FJ-paper or classification-proof coverage claim.
Measured ACK12:00:50.166380Z; pregate12:01:53.389180Z; input DRAFT12:05:55.302853Z; checked partial12:17:29.391300Z. Original12:20/12:40/12:55/13:00 clocks and14:00 intake retained. Capability and original begin stdout were privately persisted0600 with file+directory fsync before allocated body; no token printed.

## OPENS RAISED
None. The existing actual infinitely singular/global-extension gap remains.
## COLLISIONS
The original frozen-public terminal scan is retained separately after canonical verification; EMPTY is not novelty evidence.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15662`.
- Body SHA-256:
  `2bcd284c6f2a3b86ce73755e3caf7f6c3ef6b8b8259ae05d534cbbe3ebda6c3f`.
- Frozen basis: `9e18a9552f1a978847c64295de48d1c0fe8b4464`.
