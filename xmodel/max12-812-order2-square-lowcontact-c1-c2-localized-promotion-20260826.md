# Promotion: localized low-contact `c=1,2` square gate

Date: 2026-08-26

Status: **PROMOTED, HOSTILE-REVIEW CONFIRMED.**

## Exact statement

On the generic-square first-normal chart `D(p*k0)`, after the reviewed
first-normal and half-weight reductions, the complete seven source/Faber rows
force the leading `C` correction to vanish when its finite `sigma`-contact is
one or two.

- At contact one, the grade-11/12 rootwise identity is integral.
- At contact two, the unlocalized grade-14 identity has the exact nonzero
  obstruction

  ```text
  (3/8)*ell1*a0*a1*bs1 + (3/32)*ell1*a1^2*br1,
  ```

  but that obstruction vanishes in the proper saturation by `p*k0`.

The lower-unitriangular moving Laurent transformation makes the seven source
rows equivalent to the seven analytic principal-part rows.  Since
`L=z^2+p/2` is squarefree on `D(p)`, grade 12 kills `C` at every root where
`A` is nonzero, and the localized grade-14 square identity kills it at an
`A`-root.  A linear `C` therefore vanishes at both roots and is zero.

This is an arcwise/set-theoretic contact-raising theorem for reduced formal
source arcs and for the support of nilpotent arcs.  It is not a reduced-scheme
assertion: the computation proves the relevant square identity after
localization, not membership of `C` itself in the saturated ideal.

## Custody

- producer result:
  `cases/max12_812_order2_square_owner_lowcontact_c1_c2_v4_localized_delta_20260826/RESULT.md`,
  SHA-256
  `b8ae74e5ca69b50ee346c2a11acf3282bf68bd42522fa9a10bab537d7ab14e7d`;
- producer result manifest SHA-256
  `6931164bb265fc94deb4241b280a02a1110c120dc4cfe1664e38e3a3e3af7da1`;
- frozen V4 source-file SHA-256
  `beea0c90fad4da24b386333917f2fea445ae941ad059e0ec2a4ceb69fe77123e`;
- hostile review:
  `xmodel/max12-812-order2-square-lowcontact-c1-c2-localized-review-grok-20260826.md`,
  SHA-256
  `ca1a669d718e6c7080a8ead3138ba3ecbd12a89ec120e3e821ae4dc4d043470f`,
  verdict `CONFIRMED`;
- immutable unlocalized V3 negative-control freeze-file SHA-256
  `676f97810cc0c758ba864efe3463c2798f3c5d8f3fd70d57dee8ba0fb7457b57`.

The review rehashed the complete nested source chain, verified exact engine
`rc=0`, the validator, saturation semantics and properness, both V3 field
controls, all seven source rows, the Laurent bridge, and the rootwise
implication.

## Firewall

The theorem covers only the two finite leading contacts `c=1,2` on
`D(p*k0)`.  It does not cover positive horizontal contact of `A`, `p=0`,
`k0=0`, the exact-square zero section, fan exhaustiveness, the whole square
branch, exact order two, maximum twelve, or JC2.
