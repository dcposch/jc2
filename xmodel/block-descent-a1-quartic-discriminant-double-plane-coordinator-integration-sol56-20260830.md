# Coordinator integration: quartic discriminant double-plane gate

Date: 2026-08-30 UTC  
Author: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `c2401da19dba21cc2ba6b433a413acdd26d4396b`  
Lifecycle: **DIFFERENT-MODEL REVIEW-INTEGRATED PROMOTED GATE**

## 0. Verdict

The exact double-plane gate for the minimal cyclic-`S4` quartic horn is
promoted.  An internal hostile reconstruction returned `CONFIRM AS STATED`;
GPT-5.5 independently returned `CONFIRM_WITH_CORRECTIONS / SUCCESSOR OPEN`.
The corrections are scope and environment notes, not mathematical
retractions.

Assume an actual rank-four proper block in the connected minimal-cycle row,
with every branch component generically `(2,1,1)`, `n22=1`, and `n4=0`.
Let `D` be the normal sign-discriminant double plane and `W` the normalization
in the `S3` resolvent field.  Then

```text
|T31|=0:  W -> D is a connected finite-etale C3 torsor;
|T31|=1:  W -> D is quasi-etale but ramified at the unique (3,1) point.
```

In the first row there is necessarily a nonzero anti-invariant class

```text
0 != alpha in H^1_et(D,Z/3),       iota^*alpha=-alpha.   (0.1)
```

The named nodal branch has zero mod-three etale cohomology and is excluded.
The remaining no-cusp horn is not excluded: the missing theorem is vanishing
of the locally extendable anti-invariant part for the full one-place
polynomial-curve class.

## 1. Frozen evidence and custody

```text
1939c55467f5795c5bb3a264f5516c666c82e34849bc4d74f190c95d18a016bb
  xmodel/block-descent-a1-quartic-discriminant-double-plane-etale3-gate-sol56-20260830.md
5544c05bee8ffeab1791084d7d58b70ca6a45d44079efcc2f8d4535834da0216
  xmodel/block-descent-a1-quartic-discriminant-double-plane-etale3-gate-sol56-20260830.md.artifact.json
71f582454d2a4f7981aae91fca5a40399c5f536f67870a03f56e596ff9984391
  xmodel/block-descent-a1-quartic-discriminant-double-plane-etale3-gate-hostile-review-sol56-20260830.md
5a90ab03479926958b7c93e1d2502827d7a40b366f5c98234ffa7b9fc01bfd21
  xmodel/block-descent-a1-quartic-discriminant-double-plane-hostile-review-gpt55-20260830.md
2ce87f135a1e91da8e43bc5e4cf3e37ce29f27cff6c6aacabdd08c4b75a1cde8
  ops/block_descent_a1_quartic_discriminant_double_plane_replay.py
```

GPT-5.5's run passed receipt-first custody.  Before reading the report, the
coordinator reproduced the prompt, `codex55` adapter, launcher, sandbox,
charge validator, fallacy appendix, composed model prompt, raw report, and
log hashes.  The completed raw receipt was `1b6a7a80...`, raw report body
`4e386bee...`, and log `940ce4c2...`; `charge_basis_status=ABSENT` and exit
code zero.  The report was then sealed on its exact run basis and committed.

## 2. Canonical tower and normal double plane

Let `Omega/K`, `K=C(x,y)`, be the `S4` Galois closure.  With the normal Klein
four subgroup,

```text
M=Omega^V4,             Gal(M/K)=S3,
K2=Omega^A4=M^A3,       Gal(K2/K)=C2.                  (2.1)
```

In the charged row every irreducible branch component is generically
transposition-branched.  If `q_B` is the product of its distinct irreducible
equations, factoriality of `C[x,y]` and the absence of a nontrivial etale
quadratic cover of `A2` give

```text
K2=K(sqrt(q_B)).                                         (2.2)
```

The hypersurface

```text
D=Spec C[x,y,s]/(s^2-q_B)                               (2.3)
```

is a domain, is `S2`, and is regular in codimension one because `q_B` is
reduced; hence it is normal and is the integral normalization in `K2`.
Normalizing the affine plane in `M` gives connected `W`, and quotienting by
`A3` gives the finite cyclic map `W->D`.

The scope phrase is important: the sign double plane is branched along the
reduced **transposition** branch support.  It equals the charged `B` because
the current components are generically `(2,1,1)`.  A component generically
`(3,1)` would be even in the sign quotient and is not covered by this
identification.

## 3. Complete point-stabilizer table

For a closed target point, let `H_z<=S3` be the complete local decomposition
group at a chosen point of `W`.  All closed residue fields are `C`; the
stabilizer for the `A3` action in `W->D` is literally

```text
H_z intersect A3.                                       (3.1)
```

The two reviews independently reconstructed

```text
quartic fibre   image H_z in S3       H_z intersect A3
(2,1,1)         C2                    1
(2,2)           C2                    1
(3,1)           S3                    A3
(4)             A3 or S3              nontrivial.       (3.2)
```

At `(2,2)`, the two disjoint quartic transpositions have the same image in
`S4/V4`; at `(3,1)`, transitivity on three sheets plus a generic
transposition forces `S3`.  The corrected local `(4)` possibilities are
`A4,S4`, not `D4`.

This is a pointwise stabilizer computation, not merely a divisorial inertia
calculation.  It therefore checks conductor points and singular codimension-
two points as well.  No hidden ramification remains in the `|T31|=0,n4=0`
row, while the unique `(3,1)` point in the other row has the whole `A3`
stabilizer.

## 4. Etale class and local-extension firewall

When `|T31|=0`, (3.2) makes the `A3` action free at every affine point.
Thus `W->D` is a finite-etale degree-three torsor.  It is connected because
`M` is a field, so it is nontrivial.  An odd element of `S3` induces the
double-plane involution and conjugates a three-cycle to its inverse, proving
(0.1).

After identifying `Z/3` with `mu_3`, Kummer gives

```text
0 -> O(D)^*/O(D)^{*3}
  -> H^1_et(D,Z/3)
  -> Pic(D)[3]
  -> 0.                                                 (4.1)
```

Thus the class can come from a unit or a three-torsion line bundle.  `Cl[3]`
is not the Kummer target; a class-group computation suffices only through the
injection `Pic(D)->Cl(D)` or a separate local-Cartier analysis.

A class on `D_reg`, a curve complement, or a punctured singular link does
not automatically extend over `D`.  Its restriction to every punctured
strict-henselian singular neighborhood must be trivial.  The forced class in
the no-cusp row passes this gate because it already comes from the globally
finite-etale map.  The ordinary-cusp model `UV=X^3` explains the other row:
its `C3` cover is free off the vertex and fixed at the vertex, so it is only
quasi-etale.

## 5. Exact controls

For the named nodal curve, the double plane is

```text
D0=Spec C[x,u,v]/(uv-x^2(x+1)).                         (5.1)
```

It is normal, has only constant units, and Nagata localization at `u` gives

```text
div(u)=2P0+P1,
Cl(D0)=Z^2/<(2,1)> ~= Z.                                (5.2)
```

Since `Pic(D0)` injects into the torsion-free class group, (4.1) gives

```text
H^1_et(D0,Z/3)=0.                                      (5.3)
```

This excludes that control, not the whole horn.

The independent negative control

```text
p(T)=T^3+xT+xy+1,
Delta=-4x^3-27(xy+1)^2                                (5.4)
```

has irreducible `S3` Galois closure and a connected free `C3` quotient over
the double plane.  Its branch is smoothly parametrized by

```text
x=-3r^2,       y=(1-2r^3)/(3r^2),       r in Gm.        (5.5)
```

It proves that connected Euler-zero affine double planes can carry the
required odd class.  It does not satisfy the charged one-place condition:
the branch normalization is `Gm`, not `A1`.

## 6. Replay adjudication

The external GPT sandbox selected a Python environment without `sympy`, so
its four requested executions stopped at import and it correctly reported
the environment-specific non-reproduction.  This is not a failure of the
frozen replay.  Before and after the review, the coordinator's campaign host
ran the exact frozen script under ordinary Python, `-O`, and `-OO`; all three
outputs were byte-identical with

```text
stdout SHA-256
66ecf7bae2685fb6c379fef27cbcad006cc513d2b1b32af700a3821411119745
```

and the mutation `--mutate-cusp-as-etale` exited nonzero at the required
`A3` stabilizer check.  The same results were independently reproduced by
the internal hostile reviewer.  The script contains zero `assert` nodes.

The replay checks finite permutation groups and displayed polynomial
identities.  It does not certify normality, Kummer theory, Nagata
localization, local extension, or occurrence of a proper block; those are
mathematical arguments reviewed separately.

## 7. Promoted scope and exact successor

Promote only the finite-etale `C3` gate, its anti-invariant class, the
quasi-etale correction in the one-cusp row, the nodal exclusion, and the
`Gm`-normalized positive control.

Do not infer universal odd-cohomology vanishing, exclusion of either
rank-four horn, inheritance of a proper cubic block by the resolvent,
existence of a block, or JC2.

The decisive successor `R4-DP3` is:

```text
For a reduced plane curve whose components normalize to A1, whose source
incidence is one connected forest, and whose target is obtained by one
additional two-point identification, determine

  H^1_et(Spec C[x,y,s]/(s^2-q_B),Z/3)^-

after imposing extension over every singular point.
```

A proof route must control both `O(D)^*/O(D)^{*3}` and `Pic(D)[3]`; a
counter-control must exhibit a nonzero anti-invariant class and verify all
local `(2,1,1)/(2,2)` stabilizers.  That successor is running
nonblockingly.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `9290`.
- Body SHA-256:
  `21eb906dd209823bc30d7163d18c34f9c95f6d0f24c3244e5784630f030e338b`.
- Frozen basis: `c2401da19dba21cc2ba6b433a413acdd26d4396b`.
