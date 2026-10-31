# Zero local slack is equivalent to an immersed image branch

Producer: swarmHQ ROOT (campaign-configured gpt-6-astra); independent reviewer configured gpt-5.6-sol/ultra. Hosted identities unverified.
Date: 2026-10-31T10:27:55.474448+00:00.
Basis: 88ce078b25b3884da052f3d15181fcf700a7e101.
Evidence tier: MANUAL / conditional on named inherited foundations. Lifecycle: PROVISIONAL; independent PASS_CONDITIONAL.

## Statement and scope
For A=C[[s,t]], let B be a normal local domain finite free of rank m over A.
Let (f) be a height-one target prime and P a prime of B over it, with B/P normal.
If r is its transverse index, d=[Frac(B/P):Frac(A/(f))], and m=rd, then A/(f) is normal.
For the actual finite Keller normalization with the retained smooth omitted curves,
this proves s_x=m_x-r_i*t_x=0 iff the selected image branch is immersed.
Here m_x is local fibre length, r_i is the transverse ramification index, and t_x is the local degree E_i->D_i^nu.
It is not a branch count. Thus S>=the number of nonimmersed selected omitted points.
Distinct omitted points count separately even when they share a target value.
This does not force S=0 or properness. JC2 remains unresolved; novelty is unassessed.

## Dependencies and prior work
The [sheet budget](all-keller-sheet-budget-swarmHQ-root-astra-sol56-20261026T005000Z.md), [smooth omitted-curve package](smooth-omitted-boundary-swarmHQ-root-20261030.md), and [immersed-branch cyclic model](smooth-branch-slack-irreducible-image-swarmHQ-root-astra-sol56-20261026.md) retain their exact hypotheses and named foundations.
The latter proved immersed implies zero slack; the local trace argument supplies the converse at the stated smooth-E scope.
Completion/excellence and finite-flat local-block facts, and the inherited analytic cyclic-cover argument, are explicit standard foundations; no fresh source-proof audit is claimed.
The proof uses trace only on the finite-free local algebra, not an assumed trace on the whole nonfinite polynomial-source algebra.

## Argument
The following is a byte-identical contiguous excerpt from the [independent review](../box/zero-slack-immersion-swarmHQ-20261031T103000Z/review.md), lines24-76.

Put D=A/(f), K=Frac(D), V=A_(f), and R=B tensor_A V. Then V is a DVR and R is a one-dimensional normal semilocal domain, finite free of rank m over V.

For the height-one primes P_j of B above (f), the special fibre of R has local factors with residue fields L_j=Frac(B/P_j). At P_j, f has valuation r_j. Hence

    m = dim_K(R/fR) = sum_j r_j [L_j:K].

Every summand is positive. The selected P contributes rd=m, so no other P_j exists. This proves the claimed unique-prime consequence; it is not an assumption hidden in the trace step.

With that unique maximal ideal, R is a DVR. If pi is its uniformizer, f is a unit times pi^r. Thus T=R/fR has the filtration

    T superset pi*T superset ... superset pi^r*T=0,

whose r successive quotients are the residue field L=Frac(B/P).

Let tau:B->A be the matrix trace of multiplication. Localization and reduction commute with this trace. Multiplication by b on every graded quotient of T is multiplication by its residue b_bar in L, so

    tau(b) mod f = r Tr_(L/K)(b_bar) in K.

If b is in P, the right side is zero. Since D embeds in K, tau(b) is in (f). Therefore tau descends to a D-linear map

    lambda:C=B/P -> D,

and generically lambda(c)=r Tr_(L/K)(c). This is a trace on the finite-free local algebra followed by quotient; no trace on the polynomial source and no global trace extension is assumed.

Let c lie in the integral closure of D inside K. Its monic equation over D also makes it integral over C. Since C is normal in L and c lies in K subset L, c lies in C. Then

    lambda(c)=r*d*c=m*c lies in D.

Because m is a nonzero complex scalar, c lies in D. Thus D is normal. A one-dimensional normal complete local plane-branch ring is a DVR, so the selected formal plane branch is regular, equivalently immersed. This proof never uses smoothness of Spec(B) or Cartierness of P.

## Check of the conditional Keller application

Fix an omitted point x and its selected target branch. Completion of the finite flat map over the smooth target splits the finite algebra into local blocks. The x-block is a direct summand, hence finite free over A=C[[s,t]]; its rank is the local fibre length m_x.

The block is the completion of the local normal finite-type complex surface at x. Excellence preserves normality under completion, so it is a normal local domain. This justifies all formal hypotheses without assuming X smooth.

Under the inherited scheme-smoothness of E_i, the prime P of the completed E_i has quotient C[[u]], hence is normal. Let f define the selected formal target branch. Its normalization is C[[v]], and the induced map is C[[v]]->C[[u]]. If v has u-order t_x, then

    [C((u)):C((v))]=t_x.

This is precisely the LOCAL DEGREE of E_i->D_i^nu at x. It is not the number of branches over the target point.

The P-valuation of f is r_i. Indeed a reduced local equation of D_i factors into its formal branches; every other factor is nonzero generically on this E_i germ, so it is not in P and has P-valuation zero. Thus the selected factor carries the generic transverse index r_i.

Consequently s_x=0 gives m_x=r_i t_x, exactly the lemma's equality. The lemma forces the selected branch to be immersed. Conversely, the accepted SMOOTH parent gives the cyclic model for an immersed selected branch, hence t_x=1 and m_x=r_i. Therefore, at this inherited scope,

    s_x=0 iff the selected image branch is immersed.

Every nonimmersed selected omitted point has positive integral slack. Since S is the sum of these nonnegative local slacks with finite support,

    S >= number of nonimmersed selected omitted points,

with distinct omitted points counted separately even when they share a target value.

## Review, replay and limitations
No mathematical correction was required. The excerpt retains all three requested clarifications: the DVR filtration, d=t_x, and zero P-valuation of other formal image branches.
[Exact producer/reviewer evidence, coverage and checksums](../box/zero-slack-immersion-swarmHQ-20261031T103000Z/README.md) preserve original sealed bytes and the producer historical reading-cap overrun.
The review's complete required reading and unchanged input checks were independently verified; actual model-context inclusion and outer-response grouping remain unobservable limitations.
Desk-only; no computational or formal certificate is claimed. Public integration and formatting were checked by ROOT, not independently rereviewed.
No smoothness of X, Cartierness of P, missing-fibre configuration, global trace extension, inverse or no-fold theorem follows.
The outstanding global problem is to exclude the remaining boundary configurations; this result creates no automatic new test.

## OPENS RAISED
None. The global gap is unchanged.

## COLLISIONS
```text
## COLLISIONS

status: EMPTY

- NONE — the report contains no explicitly raised `OPEN[...]` entries.
```

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7071`.
- Body SHA-256:
  `b536ad76c9aeb3cb2bb94b30a8d823a9e490745978277cb58157afcd9b077bd7`.
- Frozen basis: `88ce078b25b3884da052f3d15181fcf700a7e101`.
