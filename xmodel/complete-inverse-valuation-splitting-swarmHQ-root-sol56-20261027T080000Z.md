# Exact inverse-valuation splitting after degree normalization

Producer: swarmHQ ROOT; independent retained Sol reviewer (policy seats; actual hosted model identities unmeasured).
Date: 2026-10-27 UTC.
Basis: fe3531246b2852d20237f886cbc48fbd2eb0af7a.
Evidence tier: MANUAL, conditional on the named published valuation-theory foundations.
Lifecycle: PROVISIONAL; original mathematical review and final-text review are linked in the evidence bundle.

## Statement and scope

For a polynomial Keller map F over C of field degree N>=2, a polynomial target automorphism gives a representative H of stable degree d and a finite-valued infinitely singular eigenvaluation eta with H_*eta=d eta. For every n>=1, eta has exactly N^n distinct normalized preimages in V0 under (H^n)_bullet, all with thinness A=0. Every successive degree-N valued-field extension has e=f=1, raw value group Gamma and residue field C.
This is a necessary presentation of a hypothetical counterexample, not its exclusion. It proves no nonnegative skewness, V1 membership or fixedness for the other preimages, no preimage-only class formula, no vanishing dicritical correction, and no N=1 or JC2 conclusion. The output change need not preserve the old eigenvaluation.

## Dependencies and prior work

The [generic-output reduction](generic-output-infinitely-singular-reduction-swarmHQ-root-astra-sol56-20261026.md), including its mandatory custody, supplies the eigenvaluation. Its FJ2011 and valuation-type foundations are imported, including finite values and residue field C for the infinitely singular valuation.
The thinness formula below is [Favre–Jonsson, Eigenvaluations, Definition7.1 and Lemma7.6](https://www.numdam.org/article/ASENS_2007_4_40_2_309_0.pdf). It applies on D_H, not only V1. The count uses [Kuhlmann, Valuation Theory, Chapter11](https://www.fvkuhlmann.de/bookch11.pdf), equation11.2, Section11.2 and Theorem11.23: in residue characteristic zero, the sum of e f over all prolongations of any finite field extension equals its degree, without assuming a henselian base.
These named theorems are imported, not newly proved or fully source-audited. The [evidence bundle](../box/split-swarmHQ-20261027T080000Z/README.md) records selected source reading, hashes, reviews and qualifications. No novelty claim is made. The new arithmetic normalization bypasses the old finite-essential-prefix premise for this argument, without retroactively validating the older argument for an unmodified map.

## Argument

1. Let F=(P,Q) be a polynomial Keller map over C of field degree N>=2. Put D=deg P>=1, q=deg Q>=1, T=N! D(q+N+1), M=T^(N+1), and d=DM. The target automorphism tau(s,t)=(s,t+s^M) preserves N and the constant nonzero Jacobian. A generic determinant-one linear output change produces H=B o tau o F with stable degree deg H^n=d^n. The generic-output report applies after swapping the two components with a determinant-one rotation: degrees d>D; its open leading-direction conditions are nonempty. Normalize the initial constant Jacobian to1 if needed before making these choices.

2. Import the generic-output reduction's finite-valued infinitely singular FJ eigenvaluation eta, trivial on C*, with residue field C and H_*eta=d eta. Import its named valuation-tree/type foundations; The FJ Jacobian formula gives A(eta)=d A(eta); A(eta) is finite because eta is in V1, hence A(eta)=0 since d>1. The earlier map's eigenvaluation is not preserved by the output change.

3. Set Gamma=eta(C(x,y)^*) as an ordered subgroup of R. Restrict eta to H^*C(x,y); its value group is d Gamma. The finite field degree N gives [Gamma:d Gamma]<=N. Elementary justification: representatives of distinct value-group cosets are linearly independent over the smaller field because a nontrivial linear combination has a unique least-valued term.

4. Group lemma: for a torsion-free abelian group Gamma, multiplication by p^j induces Gamma/p Gamma isomorphic to p^j Gamma/p^(j+1) Gamma. If Gamma is not p-divisible, each quotient has at least p elements; hence [Gamma:p^a Gamma]>=p^a, whether or not the total index is finite. For p|d and a=v_p(d), d Gamma is contained in p^a Gamma, so [Gamma:d Gamma]>=p^a if Gamma is not p-divisible.

5. Every prime p|d divides T because D|T, and v_p(d)>=N+1; therefore p^v_p(d)>N. Thus Step3 forces Gamma=p Gamma for every p|d, and d Gamma=Gamma. Also every prime p<=N divides N! and hence d. This argument requires neither rational rank1 nor a finite essential Puiseux prefix.

6. Consider any finite field extension L/K of degree N of a valued field (K,v) with value group Gamma and residue C, and any prolongation w. The fundamental inequality bounds e=[Gamma_w:Gamma]<=N and f=[kappa_w:C]<=N. Algebraic closedness of C gives f=1. If e>1, choose a prime p|e, so p<=N and Gamma is p-divisible. A finite abelian group Gamma_w/Gamma of order e contains an element of order p. But p gamma in Gamma implies p gamma=p delta for some delta in Gamma; torsion-freeness gives gamma=delta, a contradiction. Hence e=f=1 for every prolongation.

7. Named external import: Kuhlmann, author-hosted Valuation Theory, Chapter11, equation(11.2), Section11.2 definition and Theorem11.23. Every valued field of residue characteristic0 is defectless, and the finite-extension degree equals the sum of e f over all distinct prolongations. This explicitly applies without assuming K henselian; no unstated equality e f=N for a single prolongation is used. Therefore there are exactly N prolongations in Step6.

8. Apply Step6-7 to the degree-N field embedding H^*:K->K with initial eta. Each prolongation still has exactly Gamma as its raw value group and residue C. Repeat one degree-N step at a time; each vertex has exactly N prolongations, and distinct parent restrictions cannot merge. Equivalently, the tower H^{n*}K subset H^{(n-1)*}K subset ... subset K has N^n distinct prolongations of the target eta (transported by the field isomorphism H^{n*}). All successive e=f=1; all raw groups equal Gamma. No argument using only e<=N^n and primes<=N is made.

9. Each resulting raw valuation w satisfies w(H^{n*}f)=eta(f). It extends to a real-valued valuation: its ordered value group equals Gamma, with the prescribed embedding into R. Put b=-min(0,w(x),w(y)). If b=0, all source polynomials have nonnegative value, contradicting eta's normalization through the polynomial map H^n; hence b>0. The normalized nu=w/b lies in V0 at infinity and (H^n)_bullet nu=eta. Definition7.1 gives nu in D_{H^n}^o because d(H^n,nu)=1/b>0. Lemma7.6 then gives nu(JH^n)+A(nu)=d(H^n,nu)A(eta)=0. Since JH^n is a nonzero constant, A(nu)=0.

10. Distinct raw prolongations remain distinct after normalization. If w1/b1=w2/b2, restricting to H^{n*}K gives eta/b1=eta/b2. Eta is nontrivial, so b1=b2 and then w1=w2. Consequently eta has exactly N^n normalized preimages in V0 under (H^n)_bullet, all of zero thinness. Conversely each normalized preimage has a unique positive rescaling restricting exactly to eta.

11. Scope: no alpha sign, V1 membership, fixedness, uniqueness among these branches, isotropy, or preimage-only class formula is established. The positive dicritical class correction remains. Exactly N^n branches is a prospective input to a geometric exclusion argument, not a contradiction or N=1. Named FJ existence/type/residue and Jacobian-formula foundations remain imported.

12. This removes the old finite-essential-prefix requirement specifically for the group divisibility and splitting/count conclusion after the new output normalization. It does not retroactively validate every statement in the older value-group report or grant the old unmodified map this stronger arithmetic normalization.


The converse in Step10 also covers V0 semivaluations: A normalized V0 preimage nu of eta under H^n has finite values on every nonzero element of C[H_1^n,H_2^n]. It cannot have a nonzero polynomial g with nu(g)=+infinity: g is algebraic and nonzero over the target fraction field, so clearing denominators in its minimal polynomial gives a_0(H^n)+a_1(H^n)g+...+a_r(H^n)g^r=0 with nonzero a_0. The constant term has finite value and every other term has infinite value, contradicting the valuation inequality. Thus nu has zero kernel and extends to a field valuation; its unique rescaling with restriction eta is one of the counted prolongations.

## Replay and negative controls

Desk-only proof; no CAS, degree census or numerical test supports the claim. Original proof and independent review receipts are preserved byte-for-byte in the [bundle](../box/split-swarmHQ-20261027T080000Z/README.md). The group argument and degree-N induction are explicit above. Degree one would give one inverse branch; the count itself is not an invertibility argument.

## Limitations and next test

A global geometric argument must still exclude these branches for a noninvertible Keller map. Exact counts and zero thinness do not remove the known dicritical correction or prove backward V1 membership. No unchanged canonical-moment or pure-preimage-class argument is renewed.

## OPENS RAISED

None. The existing geometric exclusion remains open; this report launches no computation or source audit.

## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9303`.
- Body SHA-256:
  `19b3e5a7fafd571aa9c1f10073687762b6be9d65dd2a7f82ce2a1f7be5af31a6`.
- Frozen basis: `fe3531246b2852d20237f886cbc48fbd2eb0af7a`.
