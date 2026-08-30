# Coordinator integration: pair-square/QCS curve gate and corrected surface successor

Date: 2026-08-30 UTC  
Coordinator: Sol 5.6 Ultra  
Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: **BINDING CURVE-LEVEL LEMMAS / SURFACE CARD LIVE AND UNTESTED**

## 0. Evidence and correction policy

This integration binds the conservative intersection of

```text
c02c11732defca176da0ce63f71017eb497d1cf56f213a6fa2d6b6d9571f6bfa
  xmodel/pair-square-qcs-gate-sol56-20260830.md
f6a8d6e1b21c588e34fd7788c28533eb00aa81ab653a5d7fa901573b54ee4552
  xmodel/pair-square-qcs-gate-hostile-review-opus5-20260830.md
cee4e1f8079b5a20ee6fca3c7fa58dda1d8c90aeb235cd411d5fc485b9eb7936
  xmodel/pcb-generic-collision-surplus-coordinator-integration-sol56-20260829.md
8efa07d8875b66d8d4bbcb1cd8795970372661f433f5b6e637e3416534f6cbae
  xmodel/qcs-repaired-control-braid-equivariance-audit-sol56-20260829.md
```

The Opus verdict is `CONFIRM_WITH_CORRECTIONS`. It independently recomputed
the local curve algebra, global intersection length, Keller specialization,
augmentation representation, and degree-six passport. The corrected surface
successor below supersedes the producer's harder baseline-to-pole phrasing.

One custody paragraph in the review comments on the excluded nested
formalization's parent-worktree status. That unscoped observation was outside
the mandate and is not consumed. No mathematical statement below depends on
it.

## 1. Promoted generic-curve pair-square theorem

Let `h:Cbar->P1` be the degree-`d` map obtained by restricting the second
coordinate of a Keller pair to a smooth connected compactification of a
generic fibre of the first coordinate. In

```text
Y=Cbar times_(P1) Cbar subset Cbar times Cbar,
```

the diagonal occurs with multiplicity one. Divide its Cartier equation out
and call the residual divisor `R`. Separability also makes every generic
off-diagonal component reduced, so `R` is the cycle-theoretic closure of the
off-diagonal square, not merely its support.

At a ramification point of index `e`, tame coordinates give

```text
(u^e-v^e)/(u-v) restricted to u=v = e*u^(e-1),
```

hence diagonal-residual contact length `e-1`. Globally,

```text
Delta . R = Ram(h),
length(Delta . R)=2*genus(Cbar)-2+2d.                (1.1)
```

After normalizing `R`, the correct statement is pull back the diagonal
Cartier divisor and push the resulting zero-cycle forward; it is not a
literal intersection of the normalized curve with the diagonal.

For a Keller pair,

```text
T=(-f_y,f_x),       dg(T)=1,
```

so `h` is unramified on the affine fibre and all ramification lies at its
boundary places. If the pole fibre has `s` places with indices `e_j`, then

```text
length Ram_infinity(h)=sum_j(e_j-1)=d-s.             (1.2)
```

The identifications used here are explicit: `deg(h)=td(f,g)` on the connected
generic fibre, and `h^{-1}(infinity)` is exactly the set of physical pole
places. If generic connectedness is dropped, the previously promoted
component-count rider and its `2(c-1)` shift must be restored.

For a finite-value quotient flag `i`, the cluster weight `b_i` is the local
degree/ramification index of `h` at each of its `d_i` physical ends. Thus

```text
finite-end diagonal contact = sum_i d_i*(b_i-1),
pole diagonal contact       = d-s,
quotient collision capacity = sum_i b_i*(d_i-1),
one baseline per flag       = sum_i b_i.             (1.3)
```

These four quantities are distinct. Combining (1.1)--(1.3) cross-checks the
promoted identity `sum_i d_i*b_i=d-chi_gen`; it does not produce an inequality
because it shares the defining identification of `b_i`.

## 2. Augmentation-space theorem and why it is tautological

Let `Omega` be the `d` sheets and

```text
V=Q^Omega/Q*1,        dim V=d-1.
```

If pole monodromy has `s` cycles, then

```text
dim V^sigma=s-1,
W_infinity=im(sigma-1),     dim W_infinity=d-s,
V=V^sigma direct-sum W_infinity.                    (2.1)
```

For `m=sum_i b_i`, existence of an abstract `m`-dimensional subspace
`B subset V` transverse to `V^sigma` is equivalent to

```text
m<=d-s,
```

which is QCS itself. Positing such a `B` by dimension therefore proves
nothing. A canonical construction adds braid/descent/typing burdens; it does
not remove the inequality.

Two independently desk-checked obstructions sharpen this conclusion.

**Support obstruction.** For a nonempty sheet set `S subset Omega`, with pole
cycles `C_j` of lengths `e_j`,

```text
[1_S] in W_infinity
  iff |S intersect C_j|=|S|*e_j/d for every j.        (2.2)
```

This exact proportionality generally fails, including for every proper
nonempty support in the filed degree-six control. Full sheet blocks therefore
do not naturally land in the moving pole space.

**Canonical direction obstruction.** If `tau_c` are finite local monodromies
and `product_c tau_c * sigma_infinity=1`, then

```text
W_infinity subset sum_c im(tau_c-1).                 (2.3)
```

The natural direct-sum inertia map followed by projection onto `W_infinity`
is surjective. Its source dimension is the finite ramification length
`sum_i d_i(b_i-1)=2G-2+d+s`, so its kernel has dimension

```text
2G-2+2s.
```

It can be injective only in the degenerate `G=0,s=1` case; QCS already needs
no extra `s-1` there. Thus local inertia supplies a canonical map in the
wrong direction and with a structural kernel.

## 3. Corrected live surface card

The producer studied a curve square over `P1`. The registered
`PAIR-SQUARE-QCS/v1` card asks for a different object over a two-dimensional
target open:

```text
X=F^{-1}(U),
Z=(X times_U X) minus diagonal,
```

together with a boundary pair-event complex functorial under admissible
blowups. That surface object, its invariance, and an identification of its
dimension are **UNTESTED**, not refuted by the curve calculation.

The exact residual target is

```text
source: V^sigma = reduced H_0(physical pole places;Q), dimension s-1;
target: a source-labelled surface collision/excess module C_coll(F),
        dimension E_gen=sum_a X(a);
map:    iota_F:V^sigma -> C_coll(F).
```

The previously promoted `X(a)>=0` already gives `E_gen>=0`; injectivity of
`iota_F` supplies precisely the remaining increment `E_gen>=s-1`. If one
instead constructs an injection `alpha:A_base->V` of rank `sum_i b_i`, then

```text
C_coll=coker(alpha),
dim C_coll=(d-1)-sum_i b_i=E_gen,
iota_F injective iff im(alpha) intersect V^sigma=0.
```

This is a valid dual dictionary, but constructing `alpha` re-proves the
already known baseline inequality and is strictly harder. The campaign
therefore restores the pole-to-excess direction.

The surface construction must use actual two-dimensional polynomial-map
input. Curve monodromy, local inertia, abstract blocks, or braid descent alone
are barred by (2.2)--(2.3). The degree-six passport remains an exact curve-
layer negative control with `Xi=-1`; it is not glued to the filed local germ,
is not a Keller map, and does not refute a genuinely surface-labelled module.

## 4. Lifecycle and next stop tests

The correct lifecycle is

```text
CURVE PAIR-SQUARE/RAMIFICATION LEMMAS: PROMOTED;
CURVE-ONLY QCS CONSTRUCTION: INSUFFICIENT;
SURFACE POLE-TO-EXCESS MAP: OPEN / UNTESTED.
```

The next report must separately pass:

1. surface target typing and `dim C_coll(F)=E_gen`;
2. functoriality under admissible boundary blowups;
3. a canonical map from physical pole components, not formal quotient flags;
4. an honest Keller-pair input that excludes the degree-six curve control;
5. injectivity or a faithful surface countercontrol.

No QCS, PCB, selector, actual pair-reference, polynomial map, counterexample,
or JC2 conclusion is promoted here.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7685`.
- Body SHA-256:
  `b1229bda029cc93683203579651860c77da2534d4c5954bff33b57ecd8da3da7`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
