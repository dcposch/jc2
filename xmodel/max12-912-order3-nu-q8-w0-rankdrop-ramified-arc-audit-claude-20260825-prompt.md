# Independent ramified-arc audit: selected Q8 overlap rank-drop

Act as a hostile algebraic geometer.  The goal is to decide the remaining
formal-arc question at the raw Q8 overlap, not to summarize the campaign.
Use only repository reads/searches and mathematical reasoning.  Do not run
Bash, Python, Singular, Sage, SMT, or any other local computation.  Do not
modify producer files.  Write one self-contained report to

`xmodel/max12-912-order3-nu-q8-w0-rankdrop-ramified-arc-audit-claude-20260825.md`

and leave all other files unchanged.

Read at least:

- `cases/max12_912_order3_nu_q8_global_quotient_probe_20260824/quotient_compiler.py`;
- `xmodel/max12-912-order3-nu-q8-w0-overlap-normal-rank-fitting-20260825.md`;
- `xmodel/max12-912-order3-nu-q8-w0-overlap-horizontal-tangent-20260825.md`;
- the coherent mathematical sections 2--9 of
  `xmodel/max12-912-order3-nu-q8-w0-overlap-normal-rank-tangent-review-grok-20260825.md`
  (its lines 13--20 suffered a stdout/file-write packaging collision; do not
  consume those damaged lines);
- `xmodel/max12-912-order3-nu-q8-w0-rankdrop-slope3-continuation-20260825.md`;
- all source/preregistration files in
  `cases/max12_912_order3_nu_q8_w0_rankdrop_loaded_rees_aws_20260825/` and
  `cases/max12_912_order3_nu_q8_w0_rankdrop_slope3_continuation_aws_20260825/`.

Work over an algebraically closed characteristic-zero field.  Consider a
nonconstant formal or Puiseux arc in the six-row source whose generic point
lies in the selected open
`D(w*x5*(x3-2*x5))` and whose special point lies on the overlap
`w=x1=x3=x5=0`, specifically on the normal rank-drop line
`d2=d4+1`.  Audit the following.

1. Reconstruct the exact six-row source and check every leading equation
   used by the weighted/Rees analysis.  Keep the source rows distinct from
   unused rows `e6,e8`, terminal/Taylor conditions, and selected localizers.
2. Derive all possible valuation ratios without normalizing
   `ord(x5)=1`.  Prove whether slope 2 is impossible and whether slope 3 at
   `b=d4=1` is the only remaining leading candidate.  Treat cancellations,
   zero leading coefficients, and `x3-2*x5` explicitly.
3. Decide whether the reported unramified residual `-108` excludes every
   ramified arc.  A mere substitution `t -> t^m` is not enough: justify that
   `x5` is a valid local parameter / the branch is unramified, or exhibit the
   missing fractional-Puiseux branches.  Check whether unit changes in the
   leading coefficient of `x5` alter the three next-order equations.
4. If arbitrary ramification is not settled, give the smallest finite exact
   successor: a weighted blow-up chart, strict-transform ideal, saturation,
   finite list of exceptional leading systems, or a precise theorem showing
   why one of these suffices.  State variables, weights, localizers, and the
   exact unit/emptiness certificate required.  Prefer a calculation that can
   be sharded safely on AWS.
5. Separate the ordinary `delta w=1` theorem, the unramified slope-3 theorem,
   the full finite horizontal saturation, coefficient-projective infinity,
   and terminal/Taylor realization.  Do not infer a trajectory exclusion,
   max-twelve theorem, or JC2 result beyond what is proved.

For each proposed conclusion give either a hand derivation or the first
missing identity.  End with one of `CONFIRMED`, `CONFIRMED_WITH_REPAIRS`, or
`NOT_CONFIRMED`, followed by the narrowest exact next computation.
