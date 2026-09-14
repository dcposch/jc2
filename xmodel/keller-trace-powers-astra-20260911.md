# Power traces at a node: bounded rank discriminator

MANUAL / UNREVIEWED. First action 2026-09-11 20:35:48.310148101 UTC; original reserve 20:52 UTC / hard stop 20:55 UTC. Only TASK and the pinned TRACE-IC-1 producer are charged; its frozen provisional header is historical, and acceptance at the TASK's stated scope is retained.

## 1. Verdict and exact setting

There is NO finite cutoff depending only on rank, even with both divisorial pole orders fixed at one. All powers of one chosen element are also strictly weaker than the no-shared-escaping-cluster condition. For the entire actual source algebra, however, all-power membership follows immediately from accepted TRACE-IC-1; it supplies no new independent obstruction here.

Put S=C[[u,v]], K=Frac(S), and B=S[1/u]+S[1/v]. The trace below is the total trace of a finite etale K-algebra. Laurent expansions have finitely bounded negative exponents. Membership in B means that every coefficient with BOTH exponents negative vanishes. Equivalently, n/(u^a v^b) belongs to B exactly when n belongs to (u^a,v^b). No multiplication closure of B is asserted.

## 2. Arbitrarily late first failure at rank one

For any integer m>=0 take V=K and

    h_m = u^(-1) + u^m v^(-1).
    Tr(h_m^k) = sum_{j=0}^k binom(k,j) u^((m+1)j-k) v^(-j).

Trace is the identity, so there is NO trace-zero cancellation. For 1<=k<=m+1, the j=0 term lies in S[1/u]; every j>=1 term has u-exponent at least m+1-k>=0 and lies in S[1/v]. The k=0 trace is 1. At k=m+2, the j=1 term is

    (m+2)/(uv),

while j=0 is a pure u-pole and all j>=2 have nonnegative u-exponent. Hence this is the first failure. Given any proposed finite cutoff C at rank one, choose m+1>=C.

This also refutes every rank-N version: use V=K^N and h=(h_m,0,...,0). For k>=1 the trace is unchanged, while Tr(1)=N belongs to B. A connected field control is available too: take K(a), a^N=u, and the same base-field element h_m; traces are N h_m^k. Irreducibility follows from the u-adic Eisenstein criterion.

The pole orders of h_m along u=0 and v=0 are BOTH exactly one for every m: its numerator is v+u^(m+1), divisible by neither prime. Thus rank plus these two pole orders still gives no finite cutoff. The unbounded delay comes from tangential numerator vanishing. The characteristic polynomial in the rank-one example is literally T-h_m, but its recurrence multiplies by h_m. Newton or Cayley-Hamilton identities therefore do not close membership in the nonalgebra B. No resultant identification is used.

This does NOT refute the familiar polynomial-ring criterion. If the first N traces lie in a Q-subalgebra A of K, Newton identities put every characteristic coefficient in A. Cayley-Hamilton then puts all later traces in A and makes h integral over A. For normal A with K=Frac(A), integrality conversely puts these traces in A. The missing property in our question is precisely multiplication closure. Our rational controls are not asserted to be regular functions on a plane Keller source.

## 3. All powers of one element can miss a mixed boundary forever

Take the honest connected etale open T=S[1/(uv)] with generic algebra K and

    h = v/u + u/v.
    h^k = sum_{j=0}^k binom(k,j) u^(2j-k) v^(k-2j).

The two exponents in each term sum to zero, so they cannot both be negative. Consequently EVERY h^k belongs to B, although h has a genuine pole on both branches and this open misses both branches. Nevertheless Tr(T)=S[1/(uv)] is not contained in B: the element 1/(uv) witnesses failure.

This is a changed-source local model, not a polynomial-plane Keller source or a counterexample to TRACE-IC-1. It proves that testing all powers of a selected element does not itself recover branch-cluster disjointness. Its S-subalgebra S[h] lies in B, while the full open algebra does not.

## 4. Honest Kummer controls and total traces

For e>=1, let

    T_u = S[a]/(a^e-u)[1/a].

This is finite free etale of rank e over S[1/u]. For h=a^(-1), Tr(h^k)=0 unless e divides k, and Tr(h^k)=e*u^(-k/e) when it does. All powers belong to B. In fact Tr(T_u)=S[1/u]: inclusion follows from its finite free trace, and the reverse inclusion from Tr(f/e)=f. The analogous v-cover has trace S[1/v]. Products of these factors, and unramified factors over S, therefore have every power of every element tracing into B. Arbitrary choices in different factors are legitimate elements of that PRODUCT algebra; they are not automatically global source polynomials.

For a connected cover ramified on BOTH branches, take e>=2 and

    T_uv = S[t]/(t^e-uv)[1/t].

The polynomial is u-adically Eisenstein, so the generic algebra is a field of rank e. Inverting t inverts uv and thus u and v; the cover is finite free etale over S[1/(uv)], since e*t^(e-1) is a unit. For h=t^(-1), the first e-1 positive traces vanish, whereas Tr(h^e)=e/(uv) does not belong to B. This is genuine cancellation followed by a mixed-pole witness. It does not rescue a rank-only theorem for arbitrary h, already disproved in section 2. The cover before deleting t=0 is singular at the node; the stated etale open is the control being used.

## 5. Actual-source and base-change boundaries

Accepted TRACE-IC-1 states Tr(R) after ordinary flat base change to S equals B. Since every h^k is again in R, all-power membership for every actual polynomial h is automatic. It is not additional evidence beyond that accepted image theorem.

Here is the precise conditional cluster argument. Suppose the ACTUAL base-changed source algebra T=R tensor_A S decomposes with a component T_i on which uv is invertible. If its component idempotent epsilon_i belongs to T, then z=epsilon_i/(uv) belongs to T and

    Tr_total(z)=n_i/(uv) not in B,

where n_i>0 is that generic component's rank. This contradicts TRACE-IC-1 already at the first trace. The hypotheses are actual component/open membership, not merely a generic field splitting. A missing branch in a generic description alone does not supply z in T.

No arbitrary global polynomial idempotent is required: any z in the ordinary tensor product is a finite sum of s_j tensor r_j. Trace commutes with flat base change, so Tr_total(z)=sum s_j Tr(r_j), which belongs to the S-module B. Thus a genuine local witness contradicts the global trace-image condition without pretending that z itself is one global polynomial. Conversely, the one-branch product models of section 4 automatically satisfy every power test. At this specified local level the tests give no stronger cluster condition. We do not assert a classification of all source algebras from these models.

## 6. Remaining quantity and stopping conclusion

The smallest decisive extra datum is an ACTUAL source-attached element, or finite S-linear combination of source elements, whose total trace has a nonzero mixed Laurent coefficient. An explicit denominator presentation n/(u^a v^b) reduces its check to n not in (u^a,v^b); actual membership of epsilon_i/(uv) is another sufficient datum. Rank and divisorial pole orders cannot replace numerator information, as section 2 proves. No effective tangential-jet bound is established here.

QUANTITY: one source-attached mixed coefficient, together with its exact local-membership and total-trace justification. CHEAPEST TEST: manual inspection of that finite certificate if supplied; no such certificate is supplied or computational job authorized. No new OPEN identifier. The relaxed counterexamples and Kummer formulas above are checked by displayed binomial/roots-of-unity identities, not samples or execution.

Read scope: both pinned inputs were freshly read WHOLE after matching hashes. TASK has 47 lines; the accepted producer has 272 lines, read in ranges 1-260 and 261-400 through EOF, including its seal. No provenance links were followed. Its historical provisional header is overridden only by TASK's stated acceptance of (T) and node specialization. This report is a new manual, UNREVIEWED discriminator; no source example, degree bound, Keller exclusion or JC2 conclusion follows. No code, external source or live report was used.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8083`.
- Body SHA-256:
  `ed3bfd2777c7cb996a0f87908180b6611cc87904293c3268280c671212b76d56`.
- Frozen basis: `0d39df3c9fd69c939a8420c54d03228b9077777d`.
