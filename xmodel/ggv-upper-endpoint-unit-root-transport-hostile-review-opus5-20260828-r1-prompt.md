# Opus 5 hostile review: unit-root transport to the D22 endpoint

You are the hostile reviewer, not a coauthor. Work in
`/Users/dc/code/math/jc2`.  Your final report **must** be written to exactly

`xmodel/ggv-upper-endpoint-unit-root-transport-hostile-review-opus5-20260828-r1.md`

and your independent executable checker **must** be written to exactly

`cases/ggv_8_28_upper_endpoint_unit_root_transport_review_opus5_20260828/verify_unit_root_transport_review_opus5.py`.

Use only Python standard-library exact arithmetic for the checker.  Keep the
checker small enough to run locally in seconds.  You may create that one case
directory.  Apart from the required report and checker, do not write or edit
anything.  In particular, do not edit `APPROACHES.md`, `AUDIT.md`,
`COORDINATION.md`, `PROGRESS.md`, `notes.md`, any producer artifact, any
adapter, or any other case.  Never enter, list, search, read, build, status, or
modify `jc2-lean`.  Do not use AWS, Singular, Sage, Mathematica, network
access, or a heavy/local long-running CAS job.  Preserve the dirty worktree.

## Frozen claim under review

Producer report:

`xmodel/ggv-upper-endpoint-unit-root-transport-sol-ultra-20260828.md`

Live SHA-256 when assigned:

`98f5e97d570e4d73f4824888731162eb63588e51edfba8cff9c309fae619005f`

Producer case:

`cases/ggv_8_28_upper_endpoint_unit_root_transport_20260828/`

Assigned live hashes:

```text
48d5393afff34c02925566413da07cf3578a7045413e44aa85060ebbf0ee2412  verify_unit_root_transport.py
22c4ad5065cd22635c96816c118f7981c1da4235d3b27c93aee550f4ae959903  RESULT.json
fbe61174523d4650df006dbc5ce2bf3885130e16b506da7e276cf55ea78af2b8  TARGET.json
203aa3482192126f3079ec90af98ce1a98c54e23cdc07cdaac659b6fefe2515f  README.md
538d8b8c784d17f0544a94abba3742f880abef080122d4610cadf6bdec972e21  SOURCE.sha256
d51bd6e1797ab3b7811f35ca187ae8a3a9514d8ea61d2dbb22b1c0eeac465eb4  EVIDENCE.sha256
```

First verify the bytes and report any mismatch.  Read the producer claim and
its pinned sources, especially the complete fixed-cascade proof and the
289/289 Grok hostile review.  Do not treat any producer checker passing as
evidence for the new bridge.  Reconstruct the bridge independently from the
mathematics and cite exact source sections/identities for every imported
step.

## Required adjudication

Work over a characteristic-zero field after adjoining a simple root `alpha`
of squarefree `A`, in the DVR at `alpha`, with `nu=V0` a unit.  Decide whether
the claimed theorem is valid:

> Under exactly the reviewed reduced branch-P prefix, complete characteristic
> mode schedule, regular raw `G0,...,G21`, absent raw `G22`, and target
> `D22=1`, the existence of one simple root with `V0(alpha) != 0` is
> impossible.  Equivalently all endpoint strata with `gcd(A,V0) != A` are
> field-point empty.  This uses neither q1 nor the provisional D9 repair.

Return exactly one headline verdict:

- `PASS` only if the theorem and all load-bearing dependencies survive;
- `REPAIR` if a precisely stated narrower theorem is proved and the original
  statement is overstated but not fundamentally false;
- `REFUTE` if the bridge has a fatal gap or a counterexample survives.

Do not use the producer's narrative as a proof outline.  Independently
reconstruct and audit all of the following.

1. **Local Newton model.**  Put `X=alpha+epsilon`,
   `A=epsilon*a(epsilon)`, `t=epsilon^2*s`, and
   `H=epsilon^-4 F(alpha+epsilon,epsilon^2*s)`.  Derive the exact identity,
   the leading square, and the coefficient/mode valuation formula.  Verify
   all load-bearing mode exponents and coefficients with your own exact
   implementation.  Include at least two live mutations that fail for the
   intended mathematical reason.

2. **Normalization algebra.**  Test
   `Fbar_i=nu^-i F_i`, `gbar_n=nu^-n g_n`, and
   `cbar_m=nu^-m c_m` for every principal and homogeneous mode through weight
   22.  Distinguish carefully between a scalar characteristic constant
   `c_m` and the root-dependent local function `cbar_m`.  Determine whether
   the fixed proof ever needs `cbar_m` to remain a ground-field scalar,
   differentiates it, compares it at another root, or invokes a raw
   determinant equation not invariant under the normalization.

3. **The entire D7--D21 cascade, not a slogan.**  Audit the recursively pinned
   fixed packet row by row.  Produce a dependency ledger for D7,...,D21
   stating what each step actually uses: fractional-power recurrence,
   regularity, a local `A`-adic quotient, scalar constancy, an `X` derivative,
   a global degree/window bound, a coefficient equation at another root, or
   an exact raw-row identity.  In particular inspect every kill of
   `c6,c10,c14,c18,c20`, the surviving positive/other modes including
   `c4,c8,c12,c16`, and every named quotient polynomial
   `R,Q,T,Y,M,N,O,P,S,U`.  Prove that replacing global quotient polynomials by
   DVR elements is legitimate, or identify the first failing row.

4. **Raw receiver firewall.**  Inspect the literal `G18,G19,G20,G21` raw
   windows, their dimensions `5,3,2,1`, and how regularity of the raw
   coefficients is converted into the conditions on the complete
   characteristic coefficients.  Decide whether any global polynomial degree
   or rank condition, rather than local regularity alone, is load-bearing.
   Explicitly guard against silently transporting a determinant equation
   under `t -> t/nu(X)`, since `X`-differentiation creates `nu'` terms.

5. **D22 endpoint.**  Independently derive the universal same-row operator in
   the original, unnormalized coordinates, its sign and coefficients, and the
   effect of absent raw `G22`.  From the strongest legitimately obtained bound
   on `ord_alpha(g22)`, decide whether `D22_raw(alpha)=0`.  Treat the optional
   `c22*A^-5` mode explicitly, including whether `c22` is scalar and whether
   the operator kills it.  Verify the target really is the unit `1` at this
   row and that no omitted raw receiver can absorb it.

6. **Scope and independence.**  Check whether q1, the D9 repair, D23, a choice
   of square-root sheet, algebraic closure, squarefreeness of all of `A`, or
   merely simplicity of the selected root is used.  State the exact field
   scope: geometric/field-valued versus scheme-theoretic, and what changes for
   nonsquarefree `A`.  Do not promote this to a raw-normal-form landing,
   branch-coverage theorem, Keller theorem, or JC2 result.

7. **Mixed D12 fixture.**  Independently inspect the pinned proper-divisor D12
   packet.  Recompute enough exact gcd/Bezout and local data to decide whether
   all three `B` roots are simple `V0`-unit roots with the claimed exact
   order-two pole, and whether this is genuinely a local illustration rather
   than evidence smuggled into the general proof.

## Deliverables and evidence standard

Your report must include:

- frozen input hashes and your output checker hash;
- the single `PASS`/`REPAIR`/`REFUTE` verdict near the top;
- a claim-by-claim table labeled `EXACT-OPUS`, `DERIVED-OPUS`,
  `REPLAY-ONLY`, or `UNPROVED`;
- the D7--D21 dependency ledger and the first failing dependency if any;
- exact checker output and mutation output;
- a concise statement of what may and may not be promoted canonically;
- any minimal correction wording required even under `PASS`.

Your checker must be independently written: do not import the producer
checker as a Python module and do not copy its implementation.  It may read
frozen source data, but it must recompute its asserted identities.  Run it
before finalizing the report.  Also run `git diff --check` restricted to your
two authored text/code paths.  Do not modify the producer merely to make the
claim pass.
