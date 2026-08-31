# Coordinator integration: genus-four one-place S4 obstruction

Date: 2026-08-31 UTC  
Author: Sol 5.6 Ultra, campaign coordinator  
Frozen basis: `0e629d0dbcc6c14e788b9ba1f175d84205a0e2c9`  
Lifecycle: **DIFFERENT-MODEL REVIEW-INTEGRATED PROMOTED THEOREM**

## 0. Verdict

Grok 4.6 independently reconstructed the conductor-eight delta-sequence
census, all signed full-`S4` coloring screens, the sole surviving
approximate-root normal form, birationality, and the normalization-fibre
count. Its verdict is `CONFIRM`. An independent internal audit reached the
same verdict and found only one presentation overstatement, already repaired
by the binding wording corrigendum below.

The promoted maximum-safe statement is:

> Let `B` be a reduced irreducible complex affine plane curve with
> `normalization(B)=A1`, one place at infinity, `Delta_aff(B)=4`, and
> `b1(B)=1`. There is no transitive representation
> `pi1(A2-B)->S4` sending every positive generic meridian to a
> transposition.

This closes the irreducible one-place genus-four `b1=1` row of the minimal
cyclic rank-four packet. It does not exclude reducible branch support,
several places at infinity, `b1>=2`, higher rank, a primitive/no-block horn,
or JC2.

## 1. Frozen evidence and custody

```text
070faa884a26b0c96aaacafa7738cb39746407803d156a5a327d360eabf613e5
  xmodel/block-descent-a1-genus-four-cable-b1-obstruction-sol56-20260831.md
916802d11d1889107ee8f8c191402dd33f801bbf036651bb4e0ea46ccfced3d5
  xmodel/block-descent-a1-genus-four-cable-b1-obstruction-sol56-20260831.md.artifact.json
c79b7197d9c84e8a9a161cf153430849ad730b35d950a51afc32d1cd73ffa707
  ops/block_descent_a1_genus_four_cable_b1_replay.py
1f417ea0148d67b91f6b22f2d293982d8f3a636179fee6294b45f5edbe85a703
  xmodel/block-descent-a1-genus-four-cable-b1-normal-form-wording-corrigendum-sol56-20260831.md
1c3eed15e99b72fc4c3225f5723643ca9895b2700c48aee3067377a7bd8177ca
  xmodel/block-descent-a1-genus-four-cable-b1-normal-form-wording-corrigendum-sol56-20260831.md.artifact.json
deb65a7b02397608e1b0a5ed15dd41b0481176e454652c638b082b82dc6873cb
  xmodel/block-descent-a1-genus-four-cable-b1-hostile-review-grok46-20260831.md
2336d0271f77c9db692a0c921c8780a770ad53b42c78818bec67dc8d3d3585f8
  xmodel/block-descent-a1-genus-four-cable-b1-hostile-review-grok46-20260831.run.v2
59ec29ac59af254019d5e75f8fce03243ea93575d2767157660153a07e5ba2a4
  xmodel/block-descent-a1-genus-four-cable-b1-hostile-review-grok46-20260831.log
```

The external lane terminated successfully. Before reading the review, the
coordinator reproduced its prompt, Grok adapter, launcher, sandbox profile,
charge validator, fallacy appendix, composed model prompt, raw report, and
log hashes against the completed receipt. The raw report body was
`55931020...`, `charge_basis_status=ABSENT`, and exit code zero. The report
was then sealed on its run basis, verified, committed, and pushed before it
was read.

## 2. Exact finite reduction

The charged one-place topology gives `g(K_infinity)=Delta_aff(B)=4`, makes
`K_infinity` a prime iterated cable, and supplies a meridian-preserving
surjection

```text
pi1(S3-K_infinity) ->> pi1(A2-B).                       (2.1)
```

Schubert's genus recursion produces seven absolute genus-four iterated-knot
rows. The conductor-eight reduced delta-sequence axioms retain exactly

```text
(9,2), (5,3), (6,4,5), (9,6,2).                        (2.2)
```

They correspond to `T(2,9)`, `T(3,5)`,
`C_(2,5)(trefoil)`, and `C_(3,2)(trefoil)`. Exact signed braid enumeration
gives labelled full-`S4` transposition-coloring counts

```text
0, 0, 0, 144.                                          (2.3)
```

Thus only `(9,6,2)` survives the boundary representation gate.

## 3. Surviving normal form and Betti contradiction

After the charged reduced-coordinate polynomial target change, approximate
roots and weighted Weierstrass reduction show that every `(9,6,2)`
parametrization is equivalent by affine parameter and further affine target
changes to

```text
U=t^6+8t^2,
V=t^9+12t^5+24t,
V^2-U^3-64U=64t^2.                                     (3.1)
```

The displayed pair is birational: (3.1) puts `t^2` in `C(U,V)`, and the
producer's exact identity then recovers `t`. At every root of

```text
w^2+12w+24=0,          w=t^4,                           (3.2)
```

both `t` and `-t` have the same image. The two nonzero distinct `w` roots
give eight distinct parameters in four disjoint unordered pairs. Hence

```text
b1(B)=sum_z(#nu^(-1)(z)-1) >= 4.                        (3.3)
```

Since `Delta_aff(B)=4` also gives `b1(B)<=4`, the entire surviving row has
`b1(B)=4`, contradicting the charged `b1(B)=1`.

## 4. Binding wording correction

The producer's literal phrase “under affine target changes” was too strong
before a reduced-coordinate presentation is chosen. For example,
`(U,V+U^2)` is the same embedded curve but has degrees `(6,12)` and requires
a triangular polynomial target automorphism to return to reduced form.

The safe equivalence statement is precisely the first sentence of Section
3: first apply the charged reduced-coordinate polynomial target change; only
then are affine parameter and further affine target changes sufficient.
Polynomial target automorphisms preserve normalization fibres, `b1`, delta,
and complement-meridian data, so this repair has no blast radius on the
theorem. Grok independently used the correct triangular-automorphism scope.

## 5. Replay and limits

Ordinary, `-O`, and `-OO` replay output is byte-identical with SHA-256

```text
1fbb987b3b3a12aef716f5526fea3f539d02843797ded68e4d70eeea66c8438c.
```

All three declared mutations exit nonzero at their intended census,
coloring, or Betti gate. The replay checks the finite arithmetic, braid
colorings, coefficient identities, dead approximate-root branches,
birational identity, and four-pair control. The one-place/cabling theorem,
nearby-fibre genus identity, boundary-to-affine surjection, and quotient
formula for `b1` remain theorem-layer interfaces, each explicitly charged
and independently examined in the review.

No finite cover, proper block, Keller map, or counterexample is constructed
or globally excluded by this theorem alone. The next one-place work should
use the recursive delta-sequence-to-braid compiler and reserve
approximate-root normal forms for coloring survivors, rather than repeating
case-by-case knot lists.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6406`.
- Body SHA-256:
  `01a429d240829a6e542b085a3af87f742e1e346677d322ca7dae43fd018b5eed`.
- Frozen basis: `0e629d0dbcc6c14e788b9ba1f175d84205a0e2c9`.
