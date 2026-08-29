You are Opus 5 acting as an independent mathematical co-researcher in the
plane Jacobian conjecture campaign. Work in `/Users/dc/code/math/jc2`.

Investigate one sharply isolated source question from first principles,
without reading any file whose name contains `prop84`, `section7`, or
`pp39` under `xmodel/` (those are concurrent producer work and must remain
blind to you).

Primary question. Sigray, `refs/sigray_full.pdf`, Proposition 8.4 on printed
pp.44--45 claims, for a normalized counterexample with a singleton pole set,
that `M_F != 1` for every `F in T_a^down cap V_a`. Its proof descends
`F=F_0,...,F_n=(0,y)` and sets `H=F_(n-1)`. If the assumed `M_F=1` occurs
already at the root `F=(0,y)`, then `n=0` and `H` is undefined. The printed
induction propagates `M=1` from a nonroot vertex toward its parent/root; it
does not manufacture a nonroot `M=1` child from `M_root=1`.

Determine the exact status of the root case. You must do all of the
following:

1. Re-read and rederive the exact definitions and dependencies on printed
   pp.7--23 and 28--45, especially Lemma 2.1/Notation 2.4, corrected
   Proposition 4.2, Corollary 6.1, Propositions 6.3/6.7/6.8, Notation and
   Proposition 8.1, Statements 8.2--8.5, Propositions 8.2--8.4, and the two
   axis conventions. Corrected source facts are summarized in
   `ladder/SIGRAY-AUDIT.md`; use that only as an errata locator and verify
   needed mathematics yourself.
2. Confirm or refute that the printed proof establishes the theorem for
   every nonroot `F` and genuinely leaves `F=(0,y)` untreated. Check all
   negative Bezout-exponent/rational-function and terminal-factor issues,
   not only the `n=0` syntax.
3. Attack the missing root theorem using the fact that every tower member is
   an actual polynomial approximate root, not merely a compatible pair of
   leading forms. In particular test whether coefficient divisibility in
   relations such as `g^alpha-s*f^beta` forces `M_(0,y)>1`. Generalize beyond
   type `(2,3)` and beyond a one-step tower if possible.
4. A countermodel counts only if it is fully typed through the actual
   polynomial tower: specify polynomial leading/next coefficients or an
   exact abstract valuation construction satisfying the tower identities,
   integrality/divisibility, normalization, corrected §3--6 transport, and
   singleton-pole hypotheses. A bare solution of Proposition 8.1(iv), or
   arbitrary associated leading forms not liftable to `h_j` polynomials,
   does not refute the theorem.
5. Search for a clean alternative global proof (one-place-at-infinity,
   approximate-root, Newton polygon, or Keller geometry) but flag every
   external theorem and hypothesis exactly. Do not assume JC2 or
   surjectivity.
6. Give the exact corrected statements of Statement 8.2 and Proposition
   8.4 supported by your analysis, plus a precise downstream scope: entry
   pole vertices are nonroot because their threshold has positive height;
   root-terminal uses are separate.

Terminal verdict must be exactly one of:

- `PASS_ROOT`: a complete proof of the root case is supplied;
- `NONROOT_ONLY`: the nonroot theorem is proved but the root case remains a
  genuine open gap under the audited package;
- `REFUTE_ROOT`: a fully typed countermodel refutes the root claim.

Distinguish a gap in the printed proof from a false theorem. Give explicit
lemmas and calculations, not plausibility. Keep the report below 4,000 words
and final CLI response below 150 words.

Write exactly:

`xmodel/sigray-prop84-rootcase-independent-opus5-20260828.md`

Do not edit any existing artifact or canonical/top-level file. Never enter,
list, search, read, build, status, or modify `jc2-lean`. Preserve the dirty
worktree. Your only write may be the required report. No AWS, web, or heavy
local CAS; light exact symbolic checks are allowed.
