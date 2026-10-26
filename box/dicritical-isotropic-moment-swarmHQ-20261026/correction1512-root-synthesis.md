# Dicritical correction: isotropic exclusion and the canonical-boundary moment

Status: PROVISIONAL / MANUAL / CONDITIONAL; independent review pending. JC2 remains unresolved. No novelty claim.
ROOT and Astra independently derived the isotropic observation; Astra supplied the finite-model moment calculation, checked here by ROOT. The abstract operator check is ROOT's. None supplies a positive-square contradiction.

## Hypotheses and imported tier
Let F:A2_C→A2_C be an actual polynomial Keller map, det DF=1, of finite function-field degree N. Use the named FJ2011 plane-valuation/Riemann–Zariski L2 framework from the reviewed campaign inputs.
Let nu be the adopted infinitely singular eigenvaluation in V1 with F_*nu=lambda nu, lambda>0, and put Z=Z_nu. Thus Z is nonzero nef, Z²=alpha(nu)>=0 and F_*Z=lambda Z. Its residue field C and polynomial nonpositivity imply nu(c)<0 for every nonconstant polynomial c.
The two reviewed inputs are public commits3a60479f (value group/residue, with explicit unaudited classification premise) and9635a77d (fixed-F nonescape and chosen-dicritical pairing). Their exact scopes and qualifications persist.
Write T=F^*, P=F_* for bounded operators on L2. Imported identities: P is the intersection adjoint of T, PT=N I, and T preserves nef classes. The intersection form is Lorentzian: a positive line-class direction plus a negative Hilbert space. These named foundations and referenced proofs are not newly audited.
If an actual boundary divisor E maps onto the affine curve C={c=0} with degree f_E, the reviewed compatible-model formula is (TZ.E)=-f_E nu(c)>0. On target models separating the centre of nu from the closure of C, every valuation preimage w of nu has (Z_w.E)=0. No existence of E is assumed unless explicitly stated.

## 1. The isotropic pushforward eigenclass excludes an actual dicritical divisor
Add the hypothesis alpha(nu)=Z²=0. Then (TZ)²=(Z.PTZ)=N Z²=0 and (TZ.Z)=(Z.PZ)=lambda Z²=0.
Both Z and TZ are nonzero nef classes; nonzero follows for TZ from PT=N I. In a Lorentzian Hilbert space, two nonzero vectors in the same closed positive cone, each null and mutually orthogonal, are positive proportional: write each as a positive time coordinate and a spatial vector, and use equality in the Hilbert Cauchy–Schwarz inequality.
Consequently TZ=aZ for a>0. Applying P gives N Z=a lambda Z, hence a=N/lambda.
Suppose an actual dicritical E exists as above. Because nu is itself a valuation preimage of nu, the compatible separation gives (Z.E)=0. It follows that (TZ.E)=(N/lambda)(Z.E)=0, contradicting the reviewed strict positive pairing.
Thus Z²=0 excludes such an E. Equivalently, whenever such an E exists, this adopted eigenvaluation has alpha(nu)>0. This is a conditional subcase reduction, not a proof that all eigenclasses are isotropic or that all Keller maps are proper.
In particular, the FJ A.8 identity (theta^*)²=0 concerns the PULLBACK eigenclass. The pushforward eigenclass Z=theta_* is different; its square is not set to zero by A.8. The original typeset PDFpage35 (printed245) was inspected to resolve the text-extraction ambiguity.
No general extension discrepancy identity, preimage-only A7 expansion, or convergence of a corrected infinite expansion is used in this subcase.

## 2. The natural finite-model thinness moment retains a positive boundary term
Let g:X→Y be a resolved generically finite morphism of smooth projective compactifications of the marked source/target affine planes, agreeing with F on A2. Let B_X and B_Y be the reduced full boundaries, taken SNC. Use canonical divisors defined by the same standard affine two-form Omega and g*Omega=Omega.
For every boundary prime E mapping onto an affine curve C_E={c_E=0}, write r_E for its generic divisorial ramification index and f_E for the degree E→C_E. This r_E is not the index of an infinitely singular valuation extension. Use reduced irreducible affine equations c_E and closures of C_E on Y.
Riemann–Hurwitz gives K_X=g*K_Y+R_g. At a prime mapping onto a target boundary prime, R_g has coefficient r_E-1, while B_X-g*B_Y has coefficient1-r_E: they cancel.
At a dicritical prime E over an affine curve, the coefficient in K_X+B_X-g*(K_Y+B_Y) is (r_E-1)+1=r_E. Interior source primes contribute zero because F is étale and maps the affine source to the affine target. Primes contracted by g have zero divisor pushforward.
Therefore, as divisor classes on Y,
    g_*(K_X+B_X)=N(K_Y+B_Y)+sum_(E dicritical) r_E f_E [closure(C_E)].
Choose a divisorial target valuation nu_j=ord_D/b_D represented by a boundary prime D of Y. Its dual class pairs with K_Y+B_Y as A(nu_j). Since div(c_E)=closure(C_E)+sum_(D' boundary)ord_D'(c_E)D', it pairs with closure(C_E) as -nu_j(c_E).
Projection then yields the exact finite-model identity
    (g*Z_nu_j . K_X+B_X)=N A(nu_j)+sum_(E dicritical) r_E f_E[-nu_j(c_E)].
For nu_j in V1 the summands on the right are nonnegative. Constant Jacobian has removed interior ramification, but it has not removed the dicritical terms or set this moment to zero.
The divisor K_X+B_X varies with the resolving model. This calculation does not provide a fixed continuous L2 functional, a zero moment for the infinitely singular limit, or an identity obtained by interchanging an infinite sum with that limit. No such passage is needed to reject a zero-moment inference from constant Jacobian alone.

## 3. Why the class identities and positivity alone give no positive-square contradiction
This is an abstract necessary-condition test, not a realized surface, boundary configuration or Keller map. Fix any N>0 and lambda>sqrt(N), and put a=sqrt(lambda²-N). On H=R⊕ell2(N0), use (t,x).(s,y)=ts-<x,y> and the unilateral shift S(e_j)=e_(j+1).
Define T(t,x)=(lambda t, a t e_0+sqrt(N)Sx). Its Lorentz adjoint is P(s,y)=(lambda s-a y_0,sqrt(N)S*y). Direct substitution gives PT=N I and (Tu.Tv)=N(u.v).
Both maps preserve the future Lorentz cone: this is immediate for T from its squared norm and time coordinate; for P it follows from cone self-duality and adjointness (or the same Cauchy–Schwarz calculation). Thus these are compatible with the cone consequences of nefness; no actual nef/effective cone is asserted.
For Z=(1,0), Z²=1 and PZ=lambda Z. Define abstract tests E_j=(0,-e_j); then (Z.E_j)=0 and (TZ.E_0)=a>0.
For n>=1,
    T^n Z=(lambda^n, a sum_(j=0)^(n-1)lambda^(n-1-j)N^(j/2)e_j),
    (T^nZ-lambda^nZ).Z=0, and (T^nZ-lambda^nZ)²=N^n-lambda^(2n).
All displayed correction coordinates are positive, but their normalized squared magnitudes form a convergent geometric series. The available negative intersection norm grows at exactly the rate needed to accommodate them; positivity alone does not exhaust an incompatible finite budget.
The model also has an isotropic pullback eigenvector theta^*=(1,(a/lambda)sum_(j>=0)(sqrt(N)/lambda)^j e_j), with Ttheta^*=lambda theta^* and Z.theta^*=1. Thus isotropy of theta^* is compatible with positive square of the pushforward eigenvector Z.
No integrality, effective-prime realization, canonical divisor, thinness functional, valuation-tree constraints or Keller polynomial pair is supplied. This refutes only deduction of a contradiction from the listed operator/cone identities and positive test pairing alone.

## Disposition and source scope
The exact remaining all-degree implication is actual-Keller control of the positive-square correction beyond these identities and the positive canonical-boundary moment. No such bound or different global consumer is supplied here; positive-square design disposition NO_NEW_TEST, with no automatic E-only/moment-limit/control-family successor.
The isotropic exclusion and finite-model moment are provisional scoped observations submitted for hostile review before any descendants or promotion. The plane-specific ingredient is the Lorentzian surface intersection form; no higher-dimensional conclusion follows.
Cached official FJ2011 PDF SHA256e85b214ae52e6d04a42807f5e4234d945b17bcdd12e2939efbb7fa7c41ae2381; text SHA25630400b3a1e1df8e99b8a4461546d9a32cd5aec4715038125ef7f9443e17ea874. ROOT selected text375-398,1518-1554,1583-1606 and PDFpage35; older exact-hash own framework coverage is reused. Underlying classification/retraction and[8] proofs remain unaudited. No whole-paper claim.
History: frozen HQb6210a41/public9635a77d captures correction1505,24 previews and68 old bodyLF only; originalarchive10536-10555 and Sep20journal1470-1517 define the earlier properness and determinant obstructions. Remaining hits unread; no novelty inference. The new input is the exact reviewed positive dicritical pairing.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8630`.
- Body SHA-256:
  `f023536aa99f18079bef0f020b72973fa702c2eaeeb603d0e4925e2a38cd0581`.
- Frozen basis: `2b5bd5eade993a67554f3ebcb53ae17053c593df`.
