# `PAIR-SQUARE-QCS/v1`: fibre-square ramification theorem and baseline-map gate

Author: Sol 5.6 independent proof-side lane  
Date: 2026-08-30 UTC  
Frozen repository `HEAD`: `0d7544ebd5cb12def6bac892646010301098be3c`  
Lifecycle: `SEALED INDEPENDENT REPORT / EXACT CURVE LEMMAS / QCS OPEN`

## 0. Verdict

The proposed generic-fibre reduction has an exact core, but that core does
not prove QCS.

Let `Cbar` be the smooth projective completion of a generic fibre of `f` and
let `h=g|Cbar:Cbar -> P1` have degree `d`.  The Cartier residual to the
diagonal in `Cbar x_(P1) Cbar` meets the diagonal in the ramification divisor
of `h`.  Since `Jac(f,g)=1`, `h` has no ramification on the affine fibre.  If
the pole orders are `e_1,...,e_s`, its pole part consequently has length

```text
sum_j(e_j-1)=d-s.
```

Thus the promoted generic QCS inequality

```text
sum_i b_i <= d-s
```

can be read exactly as “the total baseline rank is at most the pole-diagonal
contact length.”  The implication stops there.  The pair square constructs
the capacity `d-s`; it does not construct an injection of the baseline data
into that capacity.

The augmentation formulation makes the missing arrow especially sharp.  For
the sheet set `Omega`, put `V=Q[Omega]/Q*1`.  If `sigma_infty` has the `s`
pole cycles, then

```text
dim V=d-1,   dim V^(sigma_infty)=s-1,
dim im(sigma_infty-1)=d-s.
```

A subspace `B` of dimension `sum_i b_i` with
`B intersect V^(sigma_infty)=0` exists if and only if QCS already holds.
Consequently its unconstructed existence is a reformulation, not a proof.
The filed quotient package supplies integers `b_i`, but no canonical
sheet-labelled, braid-descended `B`.  Even after choosing local inertia
cycles, the intrinsic moving subspace of a `b_i`-cycle has dimension
`b_i-1`, while the full `b_i`-sheet block depends on choices, can overlap
other blocks, and need not be transverse to the pole-fixed space.

The sharp outcome is therefore

```text
PAIR-SQUARE-QCS/v1 = OPEN(BASELINE-TO-POLE MAP BEFORE INJECTIVITY).
```

No compactification calculation should start before that map is typed.

## 1. Custody and reviewed inputs

I read the exact `PAIR-SQUARE-QCS/v1` card in
`xmodel/ideation-20260829T2254Z-sol56-alt.md`, full SHA-256
`72aa958a0e69606886e035fecca8c85790ec2bb3ebc20c065938879fcdddd297`,
and the promoted identity integration
`xmodel/pcb-generic-collision-surplus-coordinator-integration-sol56-20260829.md`,
full SHA-256
`cee4e1f8079b5a20ee6fca3c7fa58dda1d8c90aeb235cd411d5fc485b9eb7936`.
I also used the sealed producer and the repaired braid/category audit only as
controls:

```text
412091929a68e8539148d00c24ee71e1d0c45185571b48be55be19d3efe0813f
  xmodel/pcb-generic-collision-surplus-sol56-20260829.md

8efa07d8875b66d8d4bbcb1cd8795970372661f433f5b6e637e3416534f6cbae
  xmodel/qcs-repaired-control-braid-equivariance-audit-sol56-20260829.md
```

The latter audit is not promoted by this report.  Pre-existing worktree
changes and sibling artifacts were preserved and excluded.  I made no
canonical or formalization-tree edit and used no heavy CAS.

## 2. Exact residual-diagonal theorem

Work over an algebraically closed field of characteristic zero.  Let

```text
h:Cbar -> P1
```

be a finite morphism of degree `d` from a smooth connected projective curve.
In the smooth surface `S=Cbar x Cbar`, let

```text
Y=Cbar x_(P1) Cbar
```

and let `Delta` be the diagonal.  Since `h` is separable, `Delta` occurs in
the Cartier divisor `Y` with generic multiplicity one.  Define its Cartier
residual `R=Y-Delta`; equivalently, locally divide the equation of `Y` by the
equation of `Delta`.

At a point `p` of ramification index `e`, tame formal coordinates put the two
copies of `h` in the form

```text
t=u^e,   t=v^e.
```

Hence

```text
Y: u^e-v^e=0,
R: (u^e-v^e)/(u-v)=0.
```

Restriction to `Delta`, where `u=v`, gives

```text
e*u^(e-1)=0.
```

Therefore the local intersection length is `e-1`.  At an unramified point it
is zero.  Globally, as zero-cycles on `Delta ~= Cbar`,

```text
Delta . R = Ram(h).                                      (2.1)
```

This proves both the support and multiplicity assertion.  In particular

```text
length(Delta . R)=2 genus(Cbar)-2+2d.                    (2.2)
```

The residual `R` is the closure of the off-diagonal fibre square.  If the
card first normalizes that closure, the safe formulation needs one
qualification: the normalization is not literally a divisor in `S`.
Write `nu:Rtilde -> R`.  Over the displayed local model,

```text
(u^e-v^e)/(u-v) = product_(zeta^e=1,zeta!=1)(u-zeta*v),
```

so `nu^*Delta` has `e-1` reduced geometric points, each of contact order one,
and its pushforward has length `e-1`.  Thus (2.1) is scheme-theoretic on the
Cartier residual; after normalization one should state the pullback/pushforward
zero-cycle or its length, not an undefined literal intersection.

This curve theorem is compactification-independent: a smooth affine curve
has a unique smooth projective completion and `h` has a unique extension.
It does not prove invariance of any surface boundary chain complex under
admissible blowups.

## 3. Keller specialization and the exact pole length

Let `(f,g)` be a polynomial Keller pair.  Every affine fibre of `f` is smooth,
because `df=0` would force `df wedge dg=0`.  On such a fibre the tangent
vector

```text
T=(-f_y,f_x)
```

satisfies

```text
dg(T)=f_x*g_y-f_y*g_x=1.
```

Hence `g` restricted to the affine fibre is unramified.  For a generic fibre,
all of the diagonal contact (2.1) is therefore at its boundary.

Let the distinct pole ends have pole orders `e_1,...,e_s`.  They are exactly
the points over infinity for `h`, so

```text
sum_j e_j=d.
```

Applying the local calculation with the target coordinate `1/g` gives

```text
length Ram_infinity(h)
  =sum_j(e_j-1)
  =d-s.                                                  (3.1)
```

This proves the candidate `d-s` statement at exact generic-fibre scope.
Notice that it is true for any finite curve cover after all finite branch
points have been deleted from its affine source.  The open pair square by
itself therefore has not yet used polynomial `A2` origin.

## 4. What the other diagonal contacts count

Under the promoted delta-gate-passed quotient package, a generic `f`-fibre
has `d_i` finite-value ends belonging to quotient line `i`, and the local
degree of `g` at each of them is the high baseline `b_i`.  Consequently the
finite-value part of (2.1) has length

```text
R_fin=sum_i d_i*(b_i-1),                                (4.1)
```

not `sum_i b_i`.  With `n=sum_i d_i`, (2.2), (3.1), and
(4.1) give

```text
(d-s)+sum_i d_i*(b_i-1)=2G-2+2d,
sum_i d_i*b_i=d+2G+s+n-2=d-chi_gen.                    (4.2)
```

Thus the fibre-square calculation independently recovers the promoted
generic deficit/Riemann--Hurwitz identity.  It supplies no inequality.

There are three distinct ranks here and they must not be conflated:

```text
pole diagonal contact:              d-s,
finite-end diagonal contact:        sum_i d_i*(b_i-1),
one-baseline-per-quotient-line:     sum_i b_i.
```

The quotient-collision event count
`sum_i b_i*(d_i-1)` is different again: it records ramification of the
parameter maps `P_i` as `f` varies, not ramification of `g` on one fixed
generic fibre.  A surface-level pair square might relate these objects, but
the generic-fibre residual divisor does not do so automatically.

Combining (3.1) with the promoted identity gives only the exact rephrasing

```text
Xi=d-s-sum_i b_i
  =length Ram_infinity(h)-sum_i b_i.                   (4.3)
```

So QCS is precisely the missing incidence statement, not a consequence of
ramification support.

## 5. Augmentation representation: exact calculation

Choose a regular target value of `h` and let `Omega` be its `d` sheets.  Put

```text
E=Q[Omega],   V=E/Q*1.
```

Let `sigma=sigma_infinity`.  Its cycles are the pole blocks of sizes
`e_1,...,e_s`.  Since invariants are exact in characteristic zero,

```text
E^sigma = {vectors constant on each pole cycle},
dim E^sigma=s,
V^sigma=E^sigma/Q*1,
dim V^sigma=s-1.                                       (5.1)
```

The canonical moving space is

```text
W_infinity=im(sigma-1)
          ={vectors whose coordinate sum on every pole cycle is zero},
dim W_infinity=sum_j(e_j-1)=d-s.                       (5.2)
```

The standard permutation pairing gives the equivariant direct sum

```text
V=V^sigma direct-sum W_infinity.                        (5.3)
```

Equations (5.1)--(5.3) confirm the proposed fixed-space dimensions and give a
clean representation-theoretic form of the pole capacity.

Now set `m=sum_i b_i`.  For any `m`-dimensional subspace `B` of `V`,

```text
B intersect V^sigma=0  implies  m+(s-1)<=d-1,
```

which is exactly `m<=d-s`.  Conversely, if `m<=d-s`, any `m`-dimensional
subspace of `W_infinity` has zero intersection with `V^sigma`.  Therefore

```text
there exists B of dimension m transverse to V^sigma
                  iff
sum_i b_i<=d-s.                                        (5.4)
```

Existence in (5.4) is equivalent to QCS.  Calling `B` canonical does not
alter the logical burden; it adds a naturality/descent burden before the
injectivity burden.

## 6. Why the filed baseline data do not define `B`

The quotient package gives a flag `i`, a quotient line, and the integer
`b_i`.  It does not give a linear map from a baseline vector space into the
sheet local system `E`.

Even after adding paths and sheet labels, a generic finite end of weight
`b_i` gives a local inertia cycle `tau` on a support `S` of `b_i` sheets.  The
intrinsic moving space is

```text
im(tau-1),   dimension b_i-1.                          (6.1)
```

This is exactly the local residual-diagonal rank.  To obtain dimension
`b_i`, one can instead project the full coordinate block `Q[S]` to `V`, but
that proposed repair has four unresolved defects:

1. a quotient line has `d_i` generic finite ends, so selecting one support
   `S` is not canonical and need not descend under the root braid of `P_i`;
2. taking all `d_i` supports has the wrong nominal rank `d_i*b_i`;
3. supports from different ends or flags may overlap, so their block spaces
   need not form a direct sum;
4. the extra constant-on-`S` direction omitted by (6.1) can lie in, or acquire
   a component in, `V^sigma`; no Keller or pair-square identity presently
   removes it.

Thus neither the normalized residual branches nor local inertia provides the
requested rank-`b_i` summand.  A path-independent projection of selected
blocks to `W_infinity` would be the missing theorem, and proving that its
direct sum is injective would prove QCS verbatim.

## 7. Small exact controls

### 7.1 Local normalization control

For `h(u)=u^e`, the residual is the union of the `e-1` lines
`u=zeta*v`, `zeta!=1`.  Before normalization its diagonal intersection is the
possibly nonreduced scheme `u^(e-1)=0`; after normalization there are `e-1`
separate simple contacts.  This checks both the multiplicity and the
normalization qualifier in Section 2.

### 7.2 Degree-six cover control

On six letters, with right-to-left multiplication, recheck

```text
sigma_plus     =(1 2 3 4 5),
sigma_minus    =(0 1 2 4 3),
sigma_infinity =(0 3 1 5 2),
sigma_plus*sigma_minus*sigma_infinity=1.
```

All three have type `(5,1)`, and the generated action is transitive.  Total
ramification is `12`, so Riemann--Hurwitz gives genus one.  Removing the two
finite ramification points and the two points over infinity leaves an affine
curve on which `h` is unramified.  At infinity

```text
d=6, s=2, pole contact length=4,
dim V=5, dim V^sigma=1, dim W_infinity=4.
```

The matched static baseline assignment `b=5` would require `B` of dimension
five.  Then `B=V` and its intersection with `V^sigma` is the fixed line.  This
is the filed degree-six curve/passport control showing that finite-cover
monodromy, Riemann--Hurwitz, affine unramifiedness, and the pair-square
ramification theorem do not imply QCS.

This control is not a common quotient-family packet: the recorded local germ
and this passport are not glued, and repaired cubic passports fail the filed
braid-equivariance test.  It therefore refutes only a derivation from the
curve-cover/pair-square layer.  It does not refute QCS for actual polynomial
Keller pairs.

### 7.3 Block-overlap control

In a sheet permutation module, two local inertia supports can overlap.  For
example, supports `{1,2}` and `{2,3}` have a common coordinate line, so the
sum of their full two-sheet block spaces is not the direct sum of two
rank-two sources.  Monodromy cycle types and baseline integers do not record
or exclude this overlap.  This is a typing control, not a source-compatible
Keller example.

## 8. Sharply typed OPEN gate

The next admissible `PAIR-SQUARE-QCS` packet must construct, on one actual
source-bearing generic-fibre packet, all of the following:

1. the sheet local system of `h=g|Cbar`, its pole monodromy `sigma`, and the
   canonical target `W_infinity=im(sigma-1)`;
2. the complete quotient-line/baseline inventory and a baseline source
   object `A_base` of certified rank `sum_i b_i`;
3. a source-labelled map

   ```text
   alpha_F:A_base -> W_infinity;
   ```

4. descent of `A_base` and `alpha_F` under root braids, changes of sheet
   paths, and admissible compactification changes;
5. injectivity of `alpha_F` using an input that distinguishes a global
   polynomial Keller pair from the degree-six curve control.

The cheapest stop tests come before injectivity:

```text
BRAID-DESCENT: does one-baseline-per-line survive permutation of the d_i roots?
BLOCK-DIRECTNESS: do the selected sheet blocks define rank sum_i b_i?
TARGET-TYPING: does the map land in W_infinity rather than finite-end contact?
POLYNOMIAL-INPUT: where exactly does global A2/Jacobian origin enter?
```

Failure of any test stops the card without topology or surface normalization.
If they pass, injectivity proves QCS and only QCS at the actual-map generic
scope.  A kernel falsifies this bridge, not QCS unless the packet is an actual
polynomial Keller pair and the construction was a necessary one.

## 9. Maximum safe scope and nonclaims

Safe exact output:

```text
PAIR-SQUARE-RAMIFICATION:  Delta.R=Ram(h) on a smooth generic fibre.
KELLER-AFFINE-UNRAMIFIED:  Ram(h) is supported at boundary ends.
POLE-CONTACT:              length Ram_infinity(h)=d-s.
AUGMENTATION-POLE-RANK:    dim im(sigma_infinity-1)=d-s.
QCS-REPHRASING:            Xi=length Ram_infinity(h)-sum_i b_i.
```

Not proved: a baseline module inside the sheet representation; an incidence
or transport map from finite quotient events to poles; compactification
invariance of a surface chain complex; injectivity; QCS/PCB; an actual
`PairRef`; a selector; a polynomial map; or JC2.

The pair-square card remains live only as a **map-construction** experiment.
The curve ramification and augmentation ranks are now controls, not the
missing bridge.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `14967`.
- Body SHA-256:
  `06669e22077e4b784b0490d4150ff9aa1a54900087d37d8135bf44d0635bc52a`.
- Frozen basis: `0d7544ebd5cb12def6bac892646010301098be3c`.
