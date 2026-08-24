# Hostile audit — dual-pencil infinity-defect gate

Date: 2026-08-24  
Producer basis: `c17bd2542b40f3178ec619ae4a73501550555336`  
Original producer SHA-256:
`9b84cbd2e217ba8847899e787c5ae8adf8ed36c39da1f4a5f27a7e34b6891e5b`  
Corrected report SHA-256:
`b96a6564f4f1f494c6c86c3fa69f0131e9c772d5823558fae6b0ee9d0a34e1ec`

Verdict: **PASS WITH SCOPED CORRECTION**.  Keep the producer verdict
`PRIOR-ART / JUMP-ONLY / TYPE-FAIL`; no GRR descendant is licensed.

## Decisive chain — pass

For every target direction \(\ell\), \(H_\ell=aP+bQ\) is a polynomial
submersion.  Suzuki's primitive factorization gives a connected generic
fiber, and the Euler defects satisfy

\[
 \epsilon_c(H_\ell)\ge0,\qquad
 \delta(H_\ell)=\sum_c\epsilon_c(H_\ell)
 =1-\chi(G_{H_\ell})=b_1(G_{H_\ell}).
\]

Zero defect makes the generic fiber an embedded affine line, so
Suzuki/Abhyankar--Moh--Suzuki makes \(H_\ell\) a coordinate.  One coordinate
direction triangularizes the full Keller pair.  A hypothetical
nonautomorphic Keller map therefore has \(\delta(H_\ell)\ge1\) for every
\(\ell\).  The raw universal defect has horizontal support over the whole
dual line and is not a finite divisor there.  This is the decisive
`TYPE-FAIL` and is unchanged.

The constructibility/generic-constancy argument, the careful non-identification
with the nonproperness curve, and aggregate resolution invariance also pass.

## Scoped correction — jump sign

The original report incorrectly said that no sign was available for the
finite jump cycle.  Put

\[
 E_{\deg}=\{\ell:\deg H_\ell<\max(\deg P,\deg Q)\};
\]

then \(\#E_{\deg}\le1\).  Siersma--Tibăr Proposition 5.1 applied to the
constant-degree FISI deformation gives

\[
 \delta(H_{\ell_0})-\delta_{\rm gen}\le0
 \quad(\ell_0\notin E_{\deg}).
\]

Thus the full formal jump cycle remains defined on all directions and is
anti-effective away from the possible degree-drop direction; that one
coefficient is uncontrolled.  This does not touch the positive generic
horizontal baseline and supplies no degree-zero endpoint.  Deleting the
degree-drop term would noncanonically discard exactly the possible
compactification correction.

The corrected report incorporates this statement.  It also corrects the
Siersma--Tibăr bibliography to Moscow Math. J. 3 (2003), no. 2, 661--679,
Proposition 5.1, discussion after Corollary 5.2, and Examples 8.3--8.4;
Example 8.4 is non-FISI and is not used as a Keller-pencil sign theorem.

## Scope

The audit proves no generic-zero statement, no degree formula, and no JC2
result.  It stops the proposed raw-defect/effective-divisor mechanism, not
every possible use of a dual target pencil.
