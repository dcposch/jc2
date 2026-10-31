# Zero-slack trace lemma: independent hostile review

Verdict: PASS_CONDITIONAL
Lifecycle: terminal review; promotion remains ROOT's decision.
Configured reviewer: gpt-5.6-sol / ultra; hosted identity UNVERIFIED.
Started UTC: 2026-10-31T10:15:53.135673+00:00
Completed UTC: 2026-10-31T10:21:41.348659+00:00
Candidate: CANDIDATE.md, SHA-256 f4c7ef536022d81e757e0d7d124acfd9bc82f16bdb88773eac3d69d30e47a470.

## Scope and inherited premises

I reviewed the exact INTERNAL / MANUAL / ROOT-CHECKED / INDEPENDENTLY UNREVIEWED candidate, not a strengthened theorem and not a new research lane.

Accepted parents were used only at their frozen scopes:

- BUDGET.md, SHA-256 5c4baaef7e6d5d1ab6edc68a1eb249b02732f001f5846e294557ee701eee5907: the finite-flat all-Keller normalization, local lengths, and nonnegative sheet-slack identity.
- SMOOTH.md, SHA-256 6fac5370b29226212461bebfa437fe00dde4c1351d2dedbc3f9ab796224a97a6: the immersed-selected-branch cyclic model and its zero-slack consequence.
- The current adopted smooth-E package is an explicit inherited conditional premise. I did not reprove or source-audit it.

The local lemma checked here assumes A=C[[s,t]], a height-one prime (f), a normal local domain B finite free of rank m over A, a height-one P over (f), normal C=B/P, ramification index r at P, residue-field degree d=[Frac(C):Frac(A/(f))], and m=rd. Characteristic zero is used to invert m.

## Hostile check of the local lemma

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

## Corrections, qualifications, and limits

No mathematical correction to the candidate is required. For independent checkability, any promotion should retain three explicit clarifications used above: the unique-prime special fibre is a DVR quotient with r residue-field graded pieces; d=t_x is a complete-local-field degree/local-degree identity; and other formal target branches have zero P-valuation.

The producer's canonical parent reading was 192 LF, within its 200-LF allowance but 32 LF over the conservatively overlapping historical 160-LF cap. I do not certify that all producer input caps passed.

The result supplies only local slack support under the inherited package. It proves no properness, polynomial inverse, global trace extension, global no-fold theorem, missing-value configuration, or JC2 conclusion. It makes no novelty claim and creates no automatic successor.

## Reading and output audit

Packet preflight passed for all declared members and all three canonical report seals before body reading.

Actual required body reading: non-STATE 1942/3000 LF and STATE 195/200 LF. It used 54 sequential verified windows: 43 non-STATE and 11 STATE. Repeated body LF: 0. Cropped or truncated lines credited: 0. Reader-help displays: 2.

Model-visible own-report body previews: 0. ACK-body previews: 0. One compact startup status object was displayed; it was not the ACK body. The immutable startup ACK was written once at mode 0444 and never modified. Four quiet report writes occurred: the startup draft, two mandated useful unsealed checkpoints, and this terminal body.

No web, repository, history, or source query; secondary model; model probe; CAS or scientific computation; helper/scratch file; automatic retry; Git action; or protected-tree access was used. The original six-hour hard time remains 2026-10-31T16:10:03.203044+00:00. ROOT alone decides promotion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7028`.
- Body SHA-256:
  `a54dc0129631cc3a2aed68de5f721ba55ff06e91e6fc81e6d2c5b2a61dcef70e`.
- Frozen basis: `88ce078b25b3884da052f3d15181fcf700a7e101`.
