# Hostile different-model review — Moskowicz prime-degree source audit

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`, with frozen uncommitted
artifacts on top.

Read in full:

- `xmodel/moskowicz-prime-degree-source-audit-20260824.md`
- every file under `cases/moskowicz_prime_degree_audit_20260824/`
- official arXiv:2407.13795v1, including source if needed
- the cited MathOverflow question and Laurent Moret-Bailly answer 472877
- the paper's cited Wang and Gwozdziewicz statements as needed to assess the
  repaired second case

Frozen hashes:

- report: `929469d903d156d18e32a3b98e847a07145c72352d3baecf37b50eb10d9d4210`
- replay: `1a6174fcd8fc1648e283df316c22206ccad6d9bb103224d3704f4d6c4c9408fb`
- freeze: `272e85c4364e33990d7dd66445ad193686263088cc371c49aec9850330eb2f3f`
- official compressed TeX retrieved by producer:
  `a41bf70500b9c95c774221b0c7261d50e6bd8465b8f375e334adbbfc75adbf42`

Independently attack exactly:

1. Locate the paper's exact load-bearing inference from the rare property to
   extension degree two. Determine what the MathOverflow answer actually
   proves; distinguish the answer from assertions added later by the
   questioner.
2. Verify or refute the all-degree countercontrol
   `C(s^n,v) subset C(s,v)`, `x=s+v`, `y=s+2v`. Check polynomial source
   generators, algebraic independence, extension degree, the cyclic action,
   all exponent patterns including equal multiplicities, and the UFD
   factor-matching argument.
3. Decide the precise logical consequence: whether this refutes the printed
   proof step, the first-case theorem, or the headline mathematical statement.
   Do not confuse an unsupported theorem with a constructed Keller
   counterexample.
4. Audit the paper's second case. Check the product-of-polynomials step, why
   its Step 2 does or does not reuse the chosen-line property correctly, and
   whether choosing nonzero `mu` makes both steps unnecessary via
   `mu*x=H(p_mu,q_mu)`. Verify the hypotheses of Wang intersection and
   injectivity-on-one-line before accepting the repair.
5. Assess the campaign consequence: whether arXiv:2407.13795 can exclude
   prime degree 109, and whether `xy in K(P,Q)` is a valid independent
   successor gate. Check that no finite degree ansatz for `H` is called
   exhaustive without a bound.
6. Rerun the registered regression and verify every hash and scope statement.

Use primary sources. Try hard to rescue the first case or break the proposed
countercontrol/second-case repair. Do not edit producer/canonical files or
launch AWS.

Write exactly one report file:

`xmodel/moskowicz-prime-degree-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
source links/hashes, exact logical scope, and promotion/quarantine advice.
