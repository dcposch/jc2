# PURITY0820 — local cyclicity and the remaining actual-global obstruction
Author: retained primary Astra, freshglobal1740_astra; co-research, not independent review.
Basis: ffee3a22d731b252492a5444ac3b0642a87701b4; frozen public d6a4dceea8f02bf9ce04a934e3b0b6a1102e9b84.
Disposition: INTERNAL / UNPROMOTED / GLOBAL GAP. No proof or counterexample of JC2; no successor.

## Scope and consumer
Let h:X->A2 be the actual finite target normalization of a polynomial Keller map F on the WHOLE open U=A2, with degree e. The accepted omitted curves E_i are disjoint and have finite-bijective A1 normalizations. Their image normalizations are A1; write phi_i for the polynomial map of degree delta_i, r_i for generic transverse ramification, t_x for its local degree, and m_x for the finite fibre length.
The accepted identities are e-1=sum_i r_i delta_i+sum_x s_x, s_x=m_x-r_i t_x>=0, and #F^-1(y)=1+sum_i r_i delta_i(1-b_i(y))+S_off(y). Repeated image curves are counted for each source E_i. No projective divisorial package or rational-singularity hypothesis is imposed.
The proposed consumer is to rule out missing fibres or the omitted boundary by localizing all ramification/slack and using actual global geometry. The local conclusion below is insufficient by itself.

## The selected smooth-branch local statement
Fix x in E_i over y and suppose the analytic image branch selected by x is smooth. This refers to one normalization branch, not to the whole image curve at y. The finite-bijective normalization makes E_i analytically unibranch at x.
For a sufficiently small target bidisc about y, split the finite inverse image into its local connected blocks and select the block through x. Proper finiteness separates the other points over y. In that block the omitted germ is only E_i: the other E_j are disjoint, and the other normalization points over y are in other blocks.
Choose target coordinates (u,v) with the selected image branch u=0. Shrink so that the image of the omitted germ lies in this branch and no other germ. Away from u=0 every point of the selected block belongs to U, where h is etale. Thus there is no other discriminant branch in this block, even if other global image branches meet at y.
The complement of the full analytic hypersurface h^-1(u=0) in the irreducible normal germ is connected. Its finite etale map over the punctured bidisc Delta* x Delta is consequently a connected finite covering. This base has fundamental group Z. Its index-m subgroup is mZ, so the connected covering is analytically (s,v)->(s^m,v) away from s=0.
The original finite normal block and the smooth cyclic model are the normal extensions of this same covering. Uniqueness follows by taking the integral closure of the target local ring in the covering field; equivalently, normal finite extensions agree when they agree on the dense complement. Hence the map germ is analytically (s,v)->(s^m,v).
Normal surface local rings are Cohen–Macaulay; a finite map to the smooth target is locally free, so its local rank m is the fibre length m_x. In the displayed model the generic ramification along E_i is also m. Therefore m=r_i, X and E_i are smooth at x, t_x=1, and s_x=0.
This also covers r_i=1. Such an omitted point is locally unramified; it must not be erased from the omitted set merely because it is not on the finite map's branch locus. Intrinsically cuspidal image branches are not covered.

## Exact localization, including higher finite lengths
Call x bad when its selected normalized image branch is not immersed. There are finitely many such normalization parameters and hence finitely many such x. The local statement places every nonzero s_x and every t_x-1 at bad points. It does not bound either quantity there.
For a polynomial phi_i:A1->A1, its derivative has total zero order delta_i-1, so sum_(x in E_i)(t_x-1)=delta_i-1. Combining this with the accepted sheet identity gives the exact all-Keller equality
  e-1 = sum_i r_i + sum_(bad x)(r_i(t_x-1)+s_x)
      = sum_i r_i + sum_(bad x)(m_x-r_i).                 (1)
No divisorial approximation replaces m_x. A global node whose selected branches are both smooth contributes nothing to the final sum, although it still changes b_i(y).
If every image normalization branch is immersed, every phi_i has no derivative zero and is linear. Thus delta_i=1, all s_x=0, X is smooth everywhere, each E_i is A1, and
  e=1+sum_i r_i,
  #F^-1(y)=1+sum_i r_i(1-b_i(y)).                        (2)
These are consequences at the actual global scope, not a replacement finite-cover model.

## Main consumer: the remaining finite-fibre condition
Equation (2) imposes the genuine simultaneous inequalities sum_i r_i(b_i(y)-1)<=1 for all y. A missing value would require equality, not merely a multibranch point. Images not through y contribute -r_i to this sum; repeated images retain separate weights. Neither contribution can be dropped.
For example, a missing value in this all-immersed case requires gcd_i(r_i)=1, directly from equality to 1. This elementary conditional exclusion is only an arithmetic consequence of (2); it does not exclude the remaining actual configurations or prove properness.
If every r_i=1 in this same case, the local statement makes h etale on all X. A connected finite etale cover of simply connected A2 is trivial, so e=1. Therefore any nontrivial all-immersed case has some r_i>1. The mixture of ramified and omitted unramified blocks is not excluded by this observation.
The actual missing-fibre problem left by (2) is whether global polynomial attachment forbids equality at every possible individual multibranch image point. Neither nonnegativity of fibre lengths nor the global sum alone gives strict inequality there. The local cyclic proof gives no bound on these global self-identifications or on their interaction with other image curves.

## What whole U and the finite map actually add topologically
Let D be the union of the image curves, V=A2 minus D, and U0=h^-1(V)=F^-1(V). This is a connected finite covering of V. Choosing a sheet identifies pi1(U0) with its stabilizer subgroup in pi1(V).
Passing from U0 to U fills the affine curves F^-1(D). Since U is simply connected, van Kampen kills pi1(U0) by the normal closures of their meridians. These are the unramified local sheets over D that actually lie in U. Omitted sheets are not filled in U.
This is a real constraint on the actual cover, but is a normal-closure statement in the sheet stabilizer. It does not furnish one globally based inertia generator per E_i, nor bound the union of supports of those selected generators. Transport from one smooth image branch to another or to another point conjugates inertia.
At an ordinary node the selected local cyclic blocks have disjoint sheet supports locally; this does not identify the based supports after global transport. No global abelian fundamental group or support-sum transitivity bound is inferred. The previously stopped node/transport argument remains stopped.
Thus the precise missing topological inference would be a justified global restriction on those transports or on the stabilizer filling relations strong enough to force strict inequality in (2). No such restriction has been established here.

## Smooth-source and boundary-tree check
All-immersed smoothness also gives K_X=div(F*dx wedge dy)=sum_i(r_i-1)E_i. This uses the actual finite map and not a supposed rational-singularity theorem.
On a smooth completion resolving only infinity, the reviewed boundary-tree construction gives closures Ebar_i=P1 meeting the connected infinity tree C once each, and not one another. Write Ebar_i squared=q_i and div(Omega)=sum_i(r_i-1)Ebar_i+sum_v a_v C_v. At the unique attachment v(i), adjunction gives
  -2-q_i=(r_i-1)q_i+a_v(i), hence a_v(i)=-2-r_i q_i.       (3)
Affineness supplies a positive boundary-supported divisor. It supplies no sign for the canonical coefficients a_v or for q_i that turns (3) into a contradiction. The principal pullbacks of affine target curves likewise require their full infinity contributions; deleting those terms would be invalid.
The governing Wright control already stops canonical effectivity plus a ruling as a sufficient obstruction; that control is not an actual Keller normalization. It was not rerun, generalized, or substituted for the actual finite-h question. No surface classification or new control family is used.
The actual extra finite-h information retained here is exactly the local models, full lengths, global identities, and covering/filling constraints above. A further global inequality tying them to the infinity intersection data is missing.

## Disposition and coverage
The selected smooth-branch bridge is proved, including global image nodes. It localizes normalization ramification and full slack to nonimmersed image branches, and makes the all-immersed source smooth. Its proposed global consumer does not close: equality in (2) is not excluded, and neither the stopped transport step nor canonical effectivity repairs that gap.
This is not a no-go theorem for all uses of these local models or actual finite maps. No isolated lemma is proposed for promotion and no new campaign successor is requested.
Fresh fixed27 metadata, three canonical verifiers, all12 archive metadata/launch blobs, and frozen STATE-to-launch equality passed. Whole STATE194 and new public pointwise62 were personally read; own unchanged governor and accepted sheet97/affinetree153 baselines were reused only after matching hashes. No archive science body or new history query/preview was read; no external source theorem was imported.
Measured ACK08:32:54.086263Z, whole input reading/DRAFT08:35:00.904600Z, checked partial08:39:48.295102Z. Original08:55 author and09:05/09:10 clocks remain. Detailed coverage, original raw lifecycle/collision outputs, and terminal postpins are retained separately. Original begin output and capability were persisted0600 with file+directory fsync before the allocated body was written.

## OPENS RAISED
None. The existing actual-global missing-fibre and properness gaps remain.
## COLLISIONS
Original terminal frozen-public output is retained separately after canonical verification; EMPTY is not novelty evidence.
<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `10239`.
- Body SHA-256:
  `2472473290c93572114f5097e628dab60843c6c6d7070a6c8c8c03cfdb8b0f68`.
- Frozen basis: `ffee3a22d731b252492a5444ac3b0642a87701b4`.
