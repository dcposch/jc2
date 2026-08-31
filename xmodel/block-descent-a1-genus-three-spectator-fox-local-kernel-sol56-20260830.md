# Genus-three charged control: affine Fox class killed exactly by the cusp links

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra (`double_plane_kernel_recovery` lane)  
Frozen basis: `eecdbc8c63f88a3aaff8cc8302382e6075d2bc17`  
Lifecycle: **FINAL+VERIFIED EXACT NEGATIVE CONTROL**

## 0. Verdict

The polynomial curve

```text
Bsp: (x,y)=(t^3-3t,t^4-2t^2)                          (0.1)
```

has normalization `A1`, one place at infinity, total affine delta three,
one ordinary node, two ordinary cusps, and `b1(Bsp)=1`.  Its infinity knot is
`T(3,4)`, so its boundary Fox determinant is divisible by three.  Unlike the
earlier determinant-only false positives, it also has a genuine nonzero
**affine** sign/Fox class:

```text
dim_F3 H^1(A2-Bsp,L_sign)=1.                            (0.2)
```

Nevertheless the class does not extend over the singular double plane.  For

```text
Dsp={w^2=q_Bsp(x,y)},
```

the exact two-cusp restriction is, after choosing generators,

```text
H^1(A2-Bsp,L_sign)=F3 -> F3 direct-sum F3,
lambda |-> (lambda,lambda).                            (0.3)
```

It is injective.  The node contributes no mod-three link group.  The exact
localization theorem therefore gives

```text
Pic(Dsp)[3]=0.                                         (0.4)
```

This is the first total-delta-three control that passes both the infinity
determinant and the separate affine braid relations but fails precisely at
the codimension-two local-extension gate.  It proves that neither boundary
Fox colorability nor affine Fox colorability is sufficient for the quartic
double-plane horn.

## 1. Charged interface and scope

The load-bearing predecessor is

```text
60ba8f43fc549991c618a646b4f3061bc7cc54a7245c78de2407186581081e32
  xmodel/block-descent-a1-quartic-double-plane-fox-localization-kernel-sol56-20260830.md
```

which proves, for reduced connected branch `B`,

```text
Pic({w^2=q_B})[3]
 = ker[H^1(A2-B,L_sign) -> direct-sum_p H^1(M_p,F3)].   (1.1)
```

The right side is exact only at the middle term; no surjectivity to the sum
of local link groups is used here.  Reduced Fox three-colorings modulo the
constant-color line compute the middle group.  At an `A1` surface link the
mod-three group is zero; at an `A2` surface link it is `F3`, and the local
restriction is the difference of the two colors in a local two-strand basis.

This report computes (1.1) for the single explicit curve (0.1).  It does not
claim universal Picard vanishing for all rational one-place branches, and it
does not assert that (0.1) is an actual proper block or a Keller branch.

## 2. Exact curve and singularity census

Eliminating `t` from (0.1) gives

```text
q_Bsp = -x^4-6x^2 y+2x^2+y^3-6y^2+9y.                 (2.1)
```

Direct substitution proves `q_Bsp(x(t),y(t))=0`.  As a cubic in `y`, its
discriminant is

```text
Disc_y(q_Bsp)=-27 x^2(x-2)^3(x+2)^3.                  (2.2)
```

The common zeros of the two parameter derivatives are `t=+1,-1`:

```text
x'=3(t^2-1),             y'=4t(t^2-1).                (2.3)
```

At either point the determinant of the second- and third-derivative vectors
is `96`, so both singularities are ordinary `A2` cusps.

For `t!=u`, divide the two equal-coordinate equations by `t-u`.  They become

```text
t^2+tu+u^2=3,
(t+u)(t^2+u^2-2)=0.                                   (2.4)
```

The second-factor alternative gives `tu=1` and then `(t-u)^2=0`, contrary to
`t!=u`.  The other alternative gives

```text
u=-t,                     t^2=3.                       (2.5)
```

Thus there is one unordered two-point fibre, `{sqrt(3),-sqrt(3)}`.  Its two
tangent vectors have nonzero determinant, so it is an ordinary node.  There
are no other finite singularities.  Consequently

```text
Delta_aff=1+1+1=3,          b1(Bsp)=2-1=1.            (2.6)
```

The degrees `(3,4)` are coprime and give one normalization place at infinity
with knot `T(3,4)`.

## 3. Based braid factorization

Project to the `x`-axis.  The critical values in (2.2) are the two cusp
values and the node value.  With a real based Hurwitz system and the standard
three-strand generators, the local factors are

```text
left cusp:   sigma1^3,
node:        (sigma2 sigma1 sigma2^-1)^2,
right cusp:  sigma2^3.                                 (3.1)
```

Their product is exactly the infinity braid:

```text
sigma1^3 (sigma2 sigma1 sigma2^-1)^2 sigma2^3
  = (sigma1 sigma2)^4                                  (3.2)
```

in `B3`.  The replay checks (3.2) using the standard map to `SL2(Z)` and the
exponent sum.  Equality of both invariants is conclusive here: the kernel of
the matrix map has exponent sum divisible by twelve, while both displayed
words have exponent eight.

The middle half twist joins the two outer real normalization sheets at the
node.  Its conjugated form in (3.1) is therefore not an arbitrary algebraic
rewrite; it records the based vanishing arc of (2.5).

## 4. Full affine Fox calculation

Label a transposition of `S3` by a color in `F3`.  In the Artin convention
used by (3.1), a positive generator acts on adjacent colors by

```text
(a,b) |-> (2a-b,a).                                    (4.1)
```

Enumerating all `3^3=27` color triples gives:

```text
fixed by the infinity braid:                         9,
fixed by all three affine factors separately:        9,
constant triples:                                     3.              (4.2)
```

Thus both the boundary and affine reduced Fox spaces have dimension one.
The cusp cubes act trivially over `F3`; the single affine equation is the
node relation.  The nine affine triples are

```text
(a,a,a),
(a,a+1,a+2),
(a,a+2,a+1),             a in F3.                     (4.3)
```

For the node half twist `h=sigma2 sigma1 sigma2^-1`, first applying `sigma2`
puts (4.3) into its adapted local basis.  The two node colors are then equal,
which is exactly the local `C2` condition.  This also agrees with the fact
that the node double-plane link is `A1` and has no mod-three cohomology.

Quotient by the constant-color line by taking the representatives with first
color zero.  On the two nonzero representatives, the left and right cusp
residues are

```text
(c0-c1,c1-c2)=(1,1) or (2,2).                          (4.4)
```

Equations (4.3)--(4.4) prove the diagonal map (0.3).  In particular the
affine class is nonzero before localization, and each cusp detects it.  The
simultaneous local kernel contains only the constant-color class, which is a
coboundary.  Substitution in (1.1) proves (0.4).

## 5. Why this control matters

There are now three logically distinct failure modes in the rank-four
double-plane search.

1. The infinity determinant can fail, so no boundary sign class exists.
2. The determinant can pass while separate affine tangency or singular braid
   relations kill the boundary class.
3. As (0.1) shows, a nonzero affine class can survive every finite braid
   relation and still be punctured at the singular double-plane links.

Only a class surviving all three stages contributes to `Pic(D)[3]` and can
be the connected finite-etale cubic resolvent torsor forced by the no-cusp
quartic row.  The local map must therefore remain explicit in every future
candidate computation.

The curve is also the branch of the already banked finite-free quartic
spectator after affine rescaling.  In that quartic, its two cusps have local
`S3` resolvent image, exactly matching the two nonzero residues in (4.4).
That spectator is outside the proper-block row and is not promoted here.

## 6. Deterministic replay and firewalls

The exact replay is

```text
0cb933cc8e45dc2cc00fce6622c6d316d67c990c363dc887e15e113806824ac7
  ops/block_descent_a1_genus_three_spectator_fox_kernel_replay.py
```

Ordinary, `python3 -O`, and `python3 -OO` executions are byte-identical:

```text
stdout SHA-256
7a86f637681833b563413741940c74531bb522eb21745e8e644478d692f2e575
```

The mutation

```text
--mutate-omit-local-cusp-map
```

exits nonzero because it incorrectly promotes the nonzero punctured affine
class to the locally extendable kernel.  The script has no `assert`
statements.  It checks (2.1)--(2.5), the cubic discriminant, the `B3`
factorization, all 27 Fox triples, the node-adapted relation, and the complete
two-cusp restriction map.

The replay does not prove the general localization theorem, comparison with
etale cohomology, the Zariski--van Kampen theorem, or the identification of
an `A2` surface-link residue.  Those are written interfaces charged from the
finalized predecessor in Section 1.

No top-level campaign ledger, active sibling artifact, or formalization tree
was modified by this report.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `8625`.
- Body SHA-256:
  `7d9ab940046285ab053f4af884e07a77228e0db9853f097ab180645ce02a75d7`.
- Frozen basis: `eecdbc8c63f88a3aaff8cc8302382e6075d2bc17`.
