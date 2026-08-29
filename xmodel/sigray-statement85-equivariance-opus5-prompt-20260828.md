# Blind repair audit: Sigray Statement 8.5 residue law

Work in `/Users/dc/code/math/jc2`.  This is a hostile mathematical audit, not
an editing task.  Never enter, list, search, read, build, modify, status, or
control `jc2-lean`.

Audit the load-bearing residue claim in Sigray's printed Statement 8.5
(`refs/sigray_full.pdf`, printed pp. 42--43): when a nonroot parent vertex
`G` is not in `V_{2,a}` and

```
p_G(eta) = \tilde p(eta^nu) = (eta^nu-c^nu)^l,
```

the source asserts

```
p_{h,G}(eta) = eta r(eta^nu),
```

and hence `gcd(nu, deg p_{h,G})=1`.  The source cites Proposition 4.6,
which on its face only gives the ODE.  Read the definitions and results needed
from Sections 3, 4, 6, and 8 rather than trusting campaign paraphrases.

Also audit the proposed repair in
`xmodel/sigray-section8-full-hostile-review-opus5-20260828.md`, Section 3.3.
There is a specific possible hole to resolve: decomposing
`q=p_{h,G}` into eta-degree classes modulo `nu` gives an inhomogeneous
grade-1 part, but the homogeneous equation can permit a grade-0 term
`C p^(d_h/d)`.  The review's degree argument appears not, by itself, to rule
out `q=q_1+C p^r` when `r=d_h/d` is integral and `deg q_1<r deg p`.

Determine rigorously which of the following is correct:

1. A general cyclic semi-invariance lemma for the leading coefficient
   `p_{h,G}` of **every polynomial** `h(x,y)` says it occupies one residue
   class modulo `nu`; then derive its character carefully from the Puiseux
   stabilizer/chart and show that the ODE forces character 1.
2. The tower construction/normalization of the terminal polynomial `h_G`
   excludes the homogeneous term; identify the exact definition or prove the
   needed normalization.
3. Another printed/corrected theorem removes the term.
4. No such theorem is available and Statement 8.5 remains unproved or false.

Do not infer semi-invariance merely from Statement 3.16, which is printed only
for `p_F=p_{f,F}`; prove the generalization with all denominator and stabilizer
indices, or explicitly mark it as an extra lemma/hypothesis.  Check the root
`nu=1` case separately.  If useful, compare the earlier campaign discussion in
`ladder/SHEET6-A3L1-REVIEW.md` around its "DERIVATION GAP", but do not trust it.
Try to construct a fully typed local or polynomial counterexample if the term
cannot be removed.  Distinguish a bare ODE packet from a genuine Sigray vertex.

Give a verdict `PROVED`, `REPAIRABLE WITH NEW LEMMA`, `UNPROVED`, or `FALSE`;
state the cleanest complete proof or smallest exact gap; and list the blast
radius for Proposition 8.3, nonroot Proposition 8.4, and the campaign's eta
law.  Be explicit about any external standard theorem used.

Write only
`xmodel/sigray-statement85-equivariance-opus5-20260828.md`.  Do not edit any
canonical or existing file.  No heavy local CAS.  End with the SHA-256 of the
new report in your stdout.
