# Coordinator integration: reviewed one-cusp quartic function-pair theorem

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `65d42c3468f115359ada65ce84ad2196c7630939`  
Lifecycle: **REVIEW-INTEGRATED PROVISIONAL THEOREM / HORN OPEN**

## 0. Verdict

GPT-5.5 independently reconstructs and confirms the cyclic normalization,
minimal-degree comparison, finite completion, Orevkov--Chau infinity budget,
irreducibility and saturation consequences, Chau singular-image step, and
Euler/orbit ledger in the charged `R4-CYCLE-1` function-pair producer.  The
older Opus 5 review independently confirms the pseudo-plane input and
Miyanishi cyclic pseudo-cover on which the producer rests.

The maximum safe theorem is therefore:

> Every strict-block survivor in the connected rank-four one-cusp row
> canonically produces a noninvertible plane Keller map
>
> ```text
> H=pi o f_mu:A2->A2,        deg_geo(H)=4mu,
> H(A2)=A2-{n},              rho o f_mu=a+lambda*x^mu,
> ```
>
> where `x` is a polynomial coordinate.  For a minimal-degree Keller
> counterexample `mu=d1`.  The Orevkov--Chau budget forces the target branch
> `B` to be irreducible and is exactly saturated.  The nonproper-value set of
> `H` has a second component `C0=pi(Phi)!=B`; its normalization is an
> immersive polynomial line and it has a multibranch self-identification.
> Equivalently there are `p!=p'` on the same multiple-fibre line `Phi` with
> `pi(p)=pi(p')`, at a value distinct from the omitted node `n` and the unique
> cusp `c`.

For `T=U times_(A2) B`, `A=T intersect Phi`, `N=#A`, and
`D=V(b o H)`, the exact companion identities are

```text
e(D)=-3mu-(mu-1)N,
D intersect {x=0}=A,
sum_(nonzero orbit representatives)(nu-#D_x)=N+3.       (0.1)
```

This does not exclude the horn.  Its remaining content is an infinity-link,
quartic-algebra, or ruling-coupling theorem that makes the new collision cost
a positive boundary jump, locates it incompatibly on `B`, or computes `N`
incompatibly with (0.1).

## 1. Charged custody

```text
0a6272060a03c0071ad8b4c71aef00f3c724284d9590dcab61a2e75169a8713f
  xmodel/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md
70c1e16270564af7138cdc9f4b4ef396a17b398698694330ee5146ec8a273f5d
  xmodel/block-descent-a1-quartic-cycle1-function-pair-cyclic-normalization-sol56-20260830.md.artifact.json
32780967e3567ae1acc325e70798d78157d86127b7304f52079fef798009b6f1
  xmodel/block-descent-a1-quartic-cycle1-function-pair-hostile-review-gpt55-20260830.md
d50058ea7ac8b8c213d2e578deba8c83679306ea1865105be00c0e4f7e227109
  xmodel/block-descent-a1-quartic-cycle1-function-pair-hostile-review-gpt55-20260830.run.v2
2ea4002f77357e26658d9f8eecb6fcbabb7ea248446f199822509c4d934e47e9
  xmodel/block-descent-a1-quartic-cycle1-function-pair-hostile-review-gpt55-20260830.log
f845a2c15f2ae08e21c323602bca09a9d0dd33fb3228ab0ccac1612ad5c74bb2
  xmodel/block-descent-a1-quartic-cycle1-pseudoplane-companion-hostile-review-opus5-20260830.md
bb7c65b47f930e73e61fc73d6fad52d0c57ad236e5e609f1cd56017fd65d200f
  xmodel/block-descent-a1-quartic-cycle1-pseudoplane-companion-hostile-review-opus5-20260830.run.v2
0df6a69a65cc96cdecf6cbeea55211954681f21b518afb7b344f30ca614151c7
  xmodel/block-descent-a1-quartic-cycle1-pseudoplane-companion-hostile-review-opus5-20260830.log
```

GPT's raw returned body is
`9e41fdf54b2a6db8908c50830c0b97fe70d7d5a83a71ff994c95baeb16cc0240`;
the sealed full hash above binds it to basis `7ff3257e...`.  Opus's raw body is
`eb4000c1a5d54bc159adfde607642d349a843773e42fc27179e5062c3d06c3aa`,
bound to basis `31007140...`.  Both external runs exited zero with all prompt,
adapter, launcher, validator, fallacy, model-prompt, sandbox, report, and log
hashes reproduced before either report was read.  Neither asserted a charge
basis.

## 2. Cyclic normalization and degree

The one-cusp row gives a smooth rational affine `Q`-homology plane `U`, an
`A1`-fibration `rho:U->A1` whose reduced fibres are single affine lines, and
one multiple fibre `mu*Phi`, `mu>=2`.  Miyanishi Lemma 2.5.2 constructs the
finite cyclic cover before deleting `mu-1` lines.  The retained open is `A2`
and maps surjectively and etale to `U` with generic degree `mu`.

The retained map is not finite and need not be stable under the full deck
action; the Galois assertion belongs to the finite cover and function-field
level.  The induced `A1`-fibration on the retained `A2` is smooth with every
scheme fibre an affine line.  The standard smooth-`A1`-bundle theorem over a
regular curve, followed by `Pic(A1)=H^1(A1,O)=0`, trivializes it and makes its
base parameter a polynomial coordinate `x`.  Hence

```text
rho o f_mu=a+lambda*x^mu.                               (2.1)
```

Both `f_mu` and `pi|U` are etale on their displayed domains, though neither
is finite there.  Their composite is a polynomial local isomorphism; its
nowhere-zero polynomial Jacobian is constant.  Surjectivity of `f_mu`, the
quartic field tower, and the exact companion image give

```text
deg_geo(H)=4mu,             H(A2)=A2-{n}.               (2.2)
```

For an original counterexample chosen with minimal geometric degree,
minimality gives `4mu>=4d1`, while the pseudo-plane Kummer step gives
`mu|d1`; therefore `mu=d1`.  In the exact canonical `d1=1` specialization
of this row, `mu|1` contradicts `mu>=2`.  No arbitrary rank-four `d1=1`
statement outside this package follows.

## 3. Boundary budget and the second asymptotic curve

Normalize `Y` in the finite cyclic cover.  The retained `A2` has boundary
equal to the inverse image of `R=Y-U` plus the deleted lines.  The first part
maps to `B`; all deleted lines map to `C0=pi(Phi)`.  Thus

```text
NonProper(H)=B union C0.                                (3.1)
```

There is no hidden boundary divisor.  Also `n notin C0`, because the retained
line is in the source while `H(A2)=A2-{n}`.

Orevkov's formula must be applied on a regular extension.  Resolution only
refines the finite-normalization boundary packets and cannot lower their
contributions.  If `r=#Irr(B)`, generic ramified rank costs `2mu*r`; the
unibranch `(3,1)` cusp costs another `mu`; and the `mu-1` deleted lines cost at
least `mu-1`.  The two-preimage `(2,2)` node is budget-free because it changes
the image identification, not the local degree along either normalization
branch.  Consequently

```text
4mu-1 >= 2mu*r+mu+(mu-1)=2mu*r+2mu-1.                  (3.2)
```

Therefore `r=1` and equality holds in every contribution.  Now `C0!=B`.
Equality makes every deleted line degree one over the `A1` normalization of
`C0`, without finite ramification; etaleness makes that normalization map
immersive.  Chau Theorem 4.4 forces singularity of the asymptotic image
curve, not criticality of its parametrization.  Hence the singularity is a
multibranch self-identification, giving the collision stated in Section 0.

## 4. Exact Euler/orbit ledger and firewalls

The full cyclic pullback of `T` has Euler number `mu*e(T)=-3mu`.  Removing
the `mu-1` copies of the finite set `A` proves the first two identities in
(0.1).  The map `x:D->A1` is quasi-finite: a vertical component would map
onto the irreducible `B` and therefore contain its omitted point `n`.  A
finite flat completion shows every special fibre has at most its generic
cardinality.  Nonzero exceptional values occur in free cyclic orbits;
constructible Euler integration then gives the last identity in (0.1).

The valid residue statement is `e(D)=N mod mu`; neither `mu|e(D)`, `mu|3`,
nor `N=0` follows.  The producer's all-`mu` hyperelliptic family realizes the
Euler/orbit ledger with one cusp orbit and no bad ambient ruling fibre.  It is
only a polynomial-fibre firewall: it does not realize a Keller pair, quartic
algebra, omitted node, companion census, pseudo-plane Picard group, or
canonical package.

## 5. Exact remaining gate

The cheapest live successor is the saturated two-component link at infinity
of `B union C0`, charged together with the quartic companion algebra.  A
successful theorem must do at least one of:

1. force the `C0` self-identification onto `B` and derive an incompatible
   divisor/intersection packet;
2. force a critical boundary jump, contradicting saturation of (3.2);
3. force a second reducible ruling fibre, contradicting `Q=0`; or
4. compute `N` incompatibly with (0.1).

Do not launch the obsolete extension route asking for a defining section of
`T_i` with zero valuation on `R_i`: the unique defining function has valuation
two there, and zero valuation would contradict the already-proved boundary
class injection.  Function-pair work is a useful coordinate tactic, not
independent first-leg data; Miyanishi manufactures the first leg from
`(U,rho)`.

Nothing here excludes `R4-CYCLE-1`, constructs a proper block, establishes an
unconditional Keller counterexample, treats the zero-cusp or primitive horns,
or proves or disproves JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8930`.
- Body SHA-256:
  `69e0e3808e562ac8c6b561d9b778b1f50b60d696c0c0dc2d5df88d8f6dbe6bf7`.
- Frozen basis: `65d42c3468f115359ada65ce84ad2196c7630939`.
