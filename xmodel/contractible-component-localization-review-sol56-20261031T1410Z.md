# Connected nonproper component localization: independent review

Verdict: PASS_CONDITIONAL
Completed UTC: 2026-10-31T14:13:00.621178+00:00
Reviewer configuration: gpt-5.6-sol/ultra; hosted identity UNVERIFIED.
Candidate SHA-256: 5bfbe7a7c7ea20f4dd7e6cf01ee4ddc8fa92b9091605236393eb66c88d9656b3.
Public basis: 38e3067ed1ad71c748e0bdca305e3ad2e4fe7ee6.

## Exact scope

Let F:A2_C -> A2_C be a noninvertible polynomial Keller map of geometric degree N>1, with nonempty reduced nonproper-value curve D. Retain BUDGET's actual finite-flat normalization: the whole source U is open in X; the omitted E_i are pairwise disjoint with chi_c(E_i)=1 and A1 normalizations; their image curves have A1 normalizations; s_x=m_x-r_i*t_x>=0; and
    N-1 = sum_i r_i*delta_i + sum_i sum_(x in E_i) s_x.
Retain TREE, ZEROSLACK, and the named classical curve and injective-line foundations at exactly their reviewed conditional scopes. Then no connected component of D is contractible, and
    b1(D) >= b0(D),    chi_c(D) <= 0.
This does not exclude a contractible irreducible curve inside a connected cyclic union. Noncontractible configurations and JC2 remain unresolved.

## Checkable review

### 1. Exact localization

For a connected component D_alpha, put Z_alpha=F^(-1)(D_alpha), let I_alpha index the E_i mapping into it, and define
    W_alpha = sum_(i in I_alpha) r_i*delta_i
              + sum_(i in I_alpha) sum_(x in E_i) s_x.
For y in D_alpha, rank-N flatness of h:X->A2 and etaleness on U give
    #F^(-1)(y) = N - sum_(x in X minus U, h(x)=y) m_x.
Compactly supported Euler integration applies to this constructible finite-fibre function. For i in I_alpha,
    integral_(E_i) m_x dchi
      = r_i*chi(E_i) + sum_x(m_x-r_i)
      = r_i + r_i*sum_x(t_x-1) + sum_x s_x
      = r_i*delta_i + sum_x s_x,
using sum_x(t_x-1)=delta_i-1. Hence the exact localized identity is
    chi_c(Z_alpha) = N*chi_c(D_alpha) - W_alpha.                 (L)
The I_alpha partition all omitted curves, so sum_alpha W_alpha=N-1. Every nonempty D_beta contains the image of an E_i, and r_i*delta_i>=1; therefore every W_beta>=1. This is one partitioned global budget, not an independent N-1 budget for each target component.

### 2. The inverse Euler lower bound

Assume D_alpha is contractible and another target component exists. Then chi_c(D_alpha)=1 and positivity of every OTHER weight gives
    W_alpha = N-1-sum_(beta != alpha) W_beta <= N-2,
so (L) yields chi_c(Z_alpha)=N-W_alpha>=2.
For a reduced union of irreducible affine curves, ordered inclusion-exclusion subtracts only finite nonnegative intersection cardinalities. Each irreducible H satisfies chi_c(H)=2-2g-p-b<=1. Thus some irreducible Gamma in Z_alpha has positive Euler characteristic; necessarily chi_c(Gamma)=1, its normalization is A1, b=0, and Gamma is everywhere unibranch and topologically contractible.

### 3. Smooth Gamma

Because the irreducible D_j in D_alpha have A1 normalizations, D_alpha is homotopy equivalent to its finite gluing graph. Contractibility makes it a tree. A self-identification on one normalization creates a cycle that later gluings cannot erase, so each D_j is unibranch and A1->D_j is bijective.
If Gamma is smooth, Abhyankar-Moh rectifies it to an actual source line. The lift of F|Gamma to the normalization of its image is a nonconstant polynomial a:A1->A1. If deg(a)>1, a' has a zero and d(F|Gamma) kills the line tangent there, contradicting etaleness. Hence deg(a)=1. Injectivity on the source line follows from BOTH deg(a)=1 and target-normalization bijectivity, not from normalization degree one alone. The inherited injective-on-line theorem would make F invertible, a contradiction.

### 4. Singular Gamma

Lin-Zaidenberg rectifies Gamma to x^p-y^q=0 with coprime p,q>1. Let Z_0 be the connected component of Z_alpha containing Gamma. Every irreducible H in any other connected component is a CLOSED affine plane curve: Z_alpha is closed, and its finitely many connected and irreducible components are closed. It is disjoint from Gamma. TREE's cusp-disjointness lemma therefore applies exactly and gives chi_c(H_normalization)<0; finite gluing makes every such other connected component have negative Euler characteristic.
Every connected reduced affine curve has Euler characteristic at most one, so chi_c(Z_0)<=1. Adding the negative other components, if any, gives chi_c(Z_alpha)<=1, contradicting the lower bound >=2.

### 5. Connected case and graph conclusion

If D_alpha is the only target component, it is the whole D, whose contractibility TREE already excludes. Thus no connected component of D is contractible. Each component is a connected finite gluing graph of A1 normalizations, so chi=1-b1 and noncontractibility gives b1>=1 componentwise. Summing proves b1(D)>=b0(D) and chi_c(D)<=0.

## Conditions, limitations, and audit

This verdict is conditional on unchanged BUDGET, ZEROSLACK, TREE, and named classical foundations; no source-proof re-audit is claimed. PRIOR-SCOPE is only a 40-LF rank-four collision record, not a proof or all-degree novelty certificate. Novelty is unassessed. ROOT decides promotion; there is no automatic successor.
Packet preflight passed all 18 members and all four canonical report seals.
Actual required reading: 2041/3000 non-STATE LF in 47 body windows; 199/199 STATE LF in 11 body windows.
Repeated body lines: 0. Truncated-body credit: 0. Reader help invocations: 2.
Observed report-body previews: 0. Observed startup-ACK-body previews: 0.
Two finalization attempts failed before file open (one Python string escape, one line-target assertion); neither mutated or previewed the report. They were corrected as output formatting, with no packet-input, lane, scientific, or model retry.
No source/history/repository query, web access, secondary model, child, CAS, scientific computation, helper/scratch file, or automatic lane retry.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5890`.
- Body SHA-256:
  `0af7da1505b54ae2782e9bcd605829b18f2aeef193b839291f8754c4cc251a83`.
- Frozen basis: `38e3067ed1ad71c748e0bdca305e3ad2e4fe7ee6`.
