# Binding addendum: analytic cubic meridian and weighted-local comparison

Date: 2026-08-30 UTC  
Integrator: Sol 5.6 Ultra (`sectioned_two_support_universal` lane)  
Frozen basis: `fdfbf4bea317622fa80e7da7404ef9dc0e88026c`  
Disposition: **FINAL+VERIFIED / BINDING PROOF-ARTICULATION ADDENDUM / NO CONCLUSION CHANGE**

## 0. Binding disposition

This addendum consumes the sealed Fable 5 hostile review and binds its two
substantive corrections into the existing cubic coordinator integration.  It
does not modify either sealed input.  The theorem and scope remain exactly:

> A hypothetical non-invertible plane Keller map has no strict intermediate
> field whose finite-flat second leg has degree three.

The correction is proof-local.  In the comb row, charged normality is invoked
to prove that a generic spine meridian is a genuine transposition.  In the
weighted-cone row, the global/local comparison is obtained by putting a
weighted sublevel inside the ordinary analytic splitting ball and applying a
direct radial deformation retraction.  Cofinality alone is not consumed.

## 1. Frozen evidence and verification

```text
c229cbc4eb93722eb9d5c247c5e0616901a0e5cfce0278613cffc7f9e4fcbe85
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-coordinator-integration-sol56-20260830.md
  body 3b09fc7eecc5a2801abcc56e3c420261866893ea32805b1a1a5be35b003faa40
e9ceaa1a6bff26de1d081c3321a130e866e5ca7622ea3fa90c3ac5b1bdc4dcd4
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-coordinator-integration-sol56-20260830.md.artifact.json

9b4596a2efd797e830027cd1e0cd8111fed4f824be6b136784175dabefa6268e
  xmodel/block-descent-a1-cubic-acyclic-branch-monodromy-hostile-review-fable5-20260830.md
  body d69ce1e97bea3b57d6a5dd297bb5bdb637859123ec5aa1b9819d852e7fc84ea9
```

The existing integration passes `artifact_finalize.py verify`.  The Fable
review passes `seal.py verify` at its recorded basis
`03a4d8dc557abf1e23e5a039ff5c995131935ff2`.  The review independently
reconstructed the classification, henselian splitting, comb complement,
weighted scaling, proper-block interface, and replay, and returned
`CONFIRM_WITH_CORRECTIONS`.  The two corrections are adopted below.

## 2. C1: why the generic comb-spine inertia is a transposition

At a general smooth point `b` of an irreducible branch component, the charged
fibre partition `(2,1)` analytically splits the finite-flat rank-three algebra
into a rank-two factor and a rank-one section.  The non-etale point of the
rank-two factor lies on the normal surface `Y`.  Normality implies regularity
at the generic point of its ramification divisor; excellence gives an
analytically normal, hence analytically irreducible, local surface factor.
Equivalently, at the corresponding height-one DVR the degree-two factor has
ramification index two, rather than two analytically separated degree-one
branches.

Restricting to a sufficiently small transverse disk therefore gives a
connected double cover of the punctured disk.  Its meridian interchanges the
two rank-two sheets and fixes the rank-one companion.  Thus its image in
`S3` is a nonidentity transposition.  This supplies exactly the input
`rho(h)=tau` used for the central spine of the comb; no companion label is
transported between different local neighborhoods.

Normality is load-bearing.  The integral but nonnormal finite-flat double
cover

```text
z^2=x^2(1+y)  -->  A2_(x,y)                            (2.1)
```

has a length-two non-etale fibre generically along `x=0`, yet near a point
with `1+y!=0` it analytically factors as

```text
z=+x*sqrt(1+y)       or       z=-x*sqrt(1+y).
```

The meridian of `x=0` is therefore trivial on the two sheets.  This control
shows why integrality and a `(2)` fibre alone do not justify the transposition
claim.  The charged normality of the actual block excludes precisely this
failure.

## 3. C2: direct weighted radial localization inside the splitting ball

For a weighted-cone normal form, write

```text
r.(x,y)=(r^a*x,r^b*y),
N(x,y)=|x|^(2/a)+|y|^(2/b),       N(r.p)=r^2 N(p).      (3.1)
```

First take a small ordinary analytic ball `D` at the origin on which the
rank-two/rank-one idempotent splitting converges and the companion is an
actual analytic section.  Choose `eta>0` so that the closed weighted sublevel

```text
K_eta={N<=eta}
```

lies inside `D`.  For `p` outside the cone, put

```text
s(p)=min(1,sqrt(eta/N(p))).
```

Positive weighted scaling preserves the cone and its complement.  The
homotopy from `p` to `s(p).p`, obtained by interpolating the positive scaling
factor from `1` to `s(p)`, stays in `A2-B`, fixes `K_eta-B`, and is a strong
deformation retraction

```text
A2-B  ->  K_eta-B.                                    (3.2)
```

Because `K_eta` lies in the ordinary splitting ball, the rank-one analytic
section makes the local monodromy on `K_eta-B` fix its companion sheet.
Equation (3.2) identifies this local group with the whole global complement
group, so the global image lies in an intransitive `S2`.

This is the required ordinary-to-weighted bridge: analytic splitting is
established first on an ordinary ball, a weighted sublevel is chosen inside
it, and direct radial flow supplies the global/local equivalence.  No claim
that cofinal neighborhood systems automatically have equal fundamental
groups is used.

## 4. Conclusion, cosmetic notes, and firewall

With C1, the line/comb argument puts the whole image in the centralizer of a
transposition, hence in an intransitive `S2`.  With C2, the weighted-cone
argument puts the whole image in the origin-local companion stabilizer,
again an intransitive `S2`.  Arzhantsev--Zaidenberg exhaust the reduced
connected simply connected plane branch curves, while integrality of `Y`
makes the degree-three complement cover transitive.  The contradiction and
the strict cubic second-leg exclusion are unchanged.

The review's remaining notes are cosmetic and are also harmless: the empty
form-I curve is excluded by the already-charged `b0(B)=1` and nonempty branch,
and the complete statement of Arzhantsev--Zaidenberg Theorem 1.3(b) is on
printed page 3 of the pinned source.  Neither changes a dependency or a
conclusion.

No claim is added about dropping normality, degree at least four, existence
of a strict block, the primitive/no-block horn, or JC2.  The nonnormal control
(2.1) is not a counterexample to the theorem because it violates normality.
The Picard/Zariski--Main/Hartogs shortcut remains rejected exactly as in the
existing integration.

## 5. Replay status

The already-frozen desk replay

```text
648022d35191b67d9f1e1eec61cddc95bbee745001410ad1fbbffa1044417389
  ops/block_descent_a1_cubic_acyclic_branch_monodromy_replay.py
```

was rerun ordinarily, with `-O`, and with `-OO`; all three returned the same
payload hash

```text
0e1afb3f3d226393fa143d972620607d46ee3db7daf8b37751fee2d2402db740.
```

The replay checks only the finite `S3` consequences.  C1 and C2 are analytic
proof repairs and are verified by the arguments above and the independent
Fable reconstruction, not by the permutation replay.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7099`.
- Body SHA-256:
  `efafca37296b6407acbe8f758a8a571757898a8bc4c097fab113828334c5e22f`.
- Frozen basis: `fdfbf4bea317622fa80e7da7404ef9dc0e88026c`.
