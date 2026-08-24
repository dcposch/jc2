# Hostile different-model review — D73 equality control

You are the independent different-model reviewer. Work in
`/Users/dc/code/math/jc2`. The committed basis is
`c17bd2542b40f3178ec619ae4a73501550555336`; the producer report is a frozen
uncommitted addition on top of it.

Read in full:

- `xmodel/d73-strict-or-equality-20260824.md`
- the cited portions of `ladder/SHEET6-LROOT.md` and
  `ladder/SHEET6-LT-REVIEW.md`
- the relevant definitions and Proposition 7.3 in `refs/sigray_full.pdf`

Frozen producer SHA-256:

- report: `90546ffb50b5cf8325195dc04a4e39b550e4075c057049529e29d8d188b698de`

An internal hostile audit independently passed the construction. Do not treat
that as evidence; recompute the claims yourself. Attack exactly:

1. In the chart `s=y^-1`, `t=xy^4`, verify the two Jacobian determinants and
   the sign of `J_(x,y)(f,g)=1` for
   `q=t+t^25`, `g=q(t)`, `f=t^15+s^3/(3q'(t))`.
2. Verify the height-four leading data, including
   `(k_f,l_f)=(60,15)`, `(k_g,l_g)=(100,25)`, `pi(G)=4`, `kappa_G=1`, and
   multiplicity 15 of the direction root.
3. Normalize the special fiber exactly. Check the number of branches, their
   pole orders/contact, membership in `R*_0`, and each `Lambda`, hence
   `sum Lambda=3=pi(G)-1`.
4. Audit the generic `a != 0` argument: all 15 roots and punctures really lie
   in one sufficiently small local neighborhood, their `g`-values are
   pairwise distinct after shrinking, every local multiplicity is 3, and the
   cover degree over any one target value remains 3. Identify any hidden
   summation across different fibers.
5. Check the source wording: Proposition 7.3 gives equality *if* the
   direction is simple, not an iff. Decide whether the germ locally refutes
   the proposed strict upgrade for multiplicity greater than one.
6. Check scope. The germ is analytic/rational in `(x,y)`, not a global
   polynomial Keller pair; it neither kills nor realizes any of the eight
   terminal classes. The only permitted conclusion is that direction
   multiplicity alone cannot yield the desired strict local defect.

Use exact algebra and primary text. Identify the smallest failing identity or
missing hypothesis if any. Do not edit the producer or any canonical file.

Write exactly one file:

`xmodel/d73-strict-or-equality-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
the frozen hash, source caveats, promotion advice, and explicit exclusions.
