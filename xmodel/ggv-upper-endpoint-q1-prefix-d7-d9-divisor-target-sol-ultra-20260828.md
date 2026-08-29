# Genuine q1-compatible branch-P endpoint prefix: the D7 divisor split

Date: 2026-08-28  
Author: Sol Ultra  
Status: **EXACT PROVISIONAL PRODUCER / SIGNIFICANT NEWS / AWAITING HOSTILE REVIEW**

## Verdict

The uniform endpoint collapse proved on the negative-control slice `V0=1`
does **not** transport verbatim to the genuine branch-P prefix.  The first
change is already weight seven, and the changed branch is real through
weight eight.

Start from the reviewed reduced prefix

```text
F0=A^4,
F1=A^2 V0,
F2=(V0^2+A^2 Z)/4,
F3=(V0 Z+A T)/8,                                      (1)
```

where `A` is a monic squarefree quartic.  On the q1-compatible locus the
exact convention is

```text
V0=A'R0+2AR0',        deg R0<=4.                       (2)
```

For the c2-zero component put

```text
K=64F4-Z^2,
C=gcd(A,V0)=gcd(A,R0),
A=CB,  V0=CV1,  T=BU.                                  (3)
```

Then D7 polynomiality is exactly

```text
C | U(K-2UV1),                                         (4)
```

not `A|T`.  D8 polynomiality is exactly

```text
A^2 | (K-4UV1)^2 - 8B^2U^2Z
      +1024A(c6 C^2V1^2+F5BU).                         (5)
```

The zero set of `V0` in the etale root algebra `Kbar[X]/(A)`—equivalently
the squarefree divisor `C` after splitting—is the gauge-invariant
replacement for the fixed-slice assertion that `V0` is a unit at every
root.

This is not merely a loose necessary condition.  For

```text
A  = X^4-1,
R0 = X-1,
V0 = 6X^4-4X^3-2,
C  = X-1,
B  = X^3+X^2+X+1,
T  = B,                         so A does not divide T,
Z  = 9/2,
K  = 18X^3+2X^2+2X+2,
F4 = 89/256 + X/32 + X^2/32 + 9X^3/32,
F5=F6=F7=F8=0,
all characteristic modes = 0,
```

the checker reconstructs literal raw `F_n,G_n` coefficient windows and
verifies the determinant recurrence directly:

```text
D0=D1=...=D8=0,
D7 numerator / A^2 = 2+4X+6X^2,
D8 polar numerator = 0.
```

Thus a nontrivial q1 root stratum with `A` not dividing `T` survives D8.
The displayed point itself is killed at D9.  More strongly, the complete
D9 leading classes repair **every** such escape: on the full q1-compatible
c2 branch cover,

```text
D1=...=D9=0  ==>  A|T.                                 (D9-repair)
```

at field points.  The next obstruction is therefore the square defect
after writing `T=A U0`, not the original D7 divisor split.

## 1. Inputs and source firewall

The authoritative lower-prefix input is the reviewed D1--D6 branch-P
parametrization.  Its c2 branch condition is retained literally:

```text
c2=0  or  A|V0.                                         (6)
```

The characteristic compiler reconstructs

```text
G = F^(3/2) + sum c_m t^m F^((12-m)/8)
```

with every mode at `m=2,4,6,8,10,12,14,16,18,20`.  The raw windows
`deg F_n<=16-n`, `deg G_n<=24-n` are retained through D8.  Full g7/g8
term censuses and hashes in `RESULT.json` include regular terms; the small
target drops none, it merely observes that regular terms do not affect
polynomiality.

The frozen 513-generator endpoint JSON is **not** a source for this
calculation: it hardcodes `A=X^4-1,V0=1`.  Instead, the live fixture is
serialized into its genuine raw coefficient slots and replayed directly
against

```text
D_n=sum_(i+j=n) ((12-j)F_i'G_j+(i-8)F_iG_j').            (7)
```

This gives literal window evidence without silently importing the old
slice.

The q1 locus is strategically prioritized, not inferred from the endpoint
prefix.  The reviewed de Rham theorem licenses q1 only when its D23 row is
available; D1--D22 alone do not imply it.

## 2. Exact q1 convention and the active-c2 sublocus

Let

```text
T_A(Q)=2AQ'-3A'Q.
```

Then an exact product-rule calculation gives

```text
T_A(A^2R0)=A^2(A'R0+2AR0')=A^2V0.                       (8)
```

This fixes the plus sign and the coefficient two in (2).  The reviewed
differential certificate writes the literal equality with an additional
overall factor two; over a characteristic-zero field it defines the same
image subspace.  The checker includes a wrong-minus-sign mutation with a
nonzero residual.

Moreover

```text
A|V0  <=>  A|R0,
```

because `V0 mod A=A'R0` and `gcd(A,A')=1`.  Since `deg R0<=4`, the active
c2 q1 component is exactly

```text
R0=lambda A,        V0=3lambda A A'.                    (9)
```

This small component must remain separate; neither c2 nor c6 may be killed
there by importing the `V0=1` argument.

## 3. D7: the first changed weight

On `c2=0`, the independently reconstructed negative part is

```text
g7^- = 3T(AK-2TV0)/(2048 A^2).                          (10)
```

Therefore polynomiality is equivalent to

```text
A^2 | T(AK-2TV0).                                       (11)
```

Modulo a simple root of `A`, (11) says `T^2V0=0`.  For `V0=1`, this forces
`A|T`.  For a q1 polynomial, `V0 mod A=A'R0`; it can vanish at a subset of
the four roots.  With (3), exact cancellation gives

```text
T(AK-2TV0)=CB^2 U(K-2UV1),
A^2=C^2B^2,
```

which proves (4), including its second-order content.

On the active component write `V0=AS`.  All c2 terms in g7 become regular,
and

```text
g7^- = 3T(K-2TS)/(2048A),
A | T(K-2TS).                                            (12)
```

So the reviewed c2 union is respected exactly.

## 4. D8: exact successor and a live nonuniform branch

Before divisor splitting, the c2-zero negative part is

```text
g8^- = 3 N8/(32768 A^4),

N8=(AK-4TV0)^2-8A^2T^2Z
   +1024A^3(c6V0^2+F5T).                                (13)
```

Substitution of (3) factors `A^2` and gives exactly (5).  Its root core is

```text
mod C: U(K-2UV1)=0,
       (K-4UV1)^2-8B^2U^2Z=0;

mod B: K-4UV1=0.                                        (14)
```

If `B` is nonconstant, the lifted square in (14) has order at least two at
each B-root, while the c6 term in (5) has only order one.  Hence D8 forces
`c6=0`.  If `B=1`, this argument disappears and c6 remains live.

The displayed fixture was engineered directly from (14): at the C-root,
choose `U=1`, `K=4V1-6B`, and `Z=9/2`; then
`(K-4V1)^2=36B^2=8B^2Z`.  The exact replay confirms both divisibilities and
all raw degree bounds.  Two live mutations guard the construction:

* replacing `T=B` by `T=1` leaves a nonzero D7 remainder modulo `A^2`;
* replacing `Z` by `Z+1` while holding `K` fixed leaves a nonzero D8
  remainder modulo `A^4`.

On the generic q1 chart `C=1`, the old architecture does continue:

```text
T=AU,
K-4UV0=64AW,
c6=0,
g9^- = -3V0W^2/(16A^2)
        +3F5W/(4A)-3UZW/(256A).                         (15)
```

Since `V0` is a unit modulo `A`, D9 forces `A|W`.  This proves only the
generic continuation through D9, not the later endpoint collapse.

## 5. The D9 repair theorem and the q1 operator echo

For every c2-zero stratum with `B` nonconstant, D8 has killed c6.  Direct
recurrence gives

```text
g9^- = N9/(65536 A^6),                                  (16)
```

where

```text
N9 = -48T^2V0^3 +1536AF4TV0^2 -24ATV0^2Z^2
     -12288A^2F4^2V0 +384A^2F4V0Z^2 +48A^2T^2V0Z
     -3A^2V0Z^4 -768A^3F4TZ -8A^3T^3 +12A^3TZ^3
     +768A^3F5(AK-4TV0) +6144A^5F6T.                   (17)
```

The checker independently substitutes (3), eliminates
`F4=(K+Z^2)/64`, and obtains the exact factorization

```text
N9=C^3 B^2 P9,

P9=-3V1 D^2-12B^2UZD-8B^4U^3
   +768CB^2F5D+6144C^2B^4F6U,
D=K-4UV1.                                                (18)
```

At a root of a proper `C`, suppose `U!=0`.  D7 gives `K=2UV1`, hence
`D=-2UV1`; the leading D8 equation gives
`2B^2Z=V1^2`.  Reducing (18) modulo C then cancels the first two terms and
leaves

```text
P9=-8B^4U^3 !=0.                                        (19)
```

But `A^6|N9` requires `C^3B^4|P9`, contradiction.  Thus `U=0` at every
C-root; squarefreeness gives `C|U`, and `T=BU` is divisible by `CB=A`.
The generic stratum `C=1` already had `A|T` at D7.

The full divisor `C=A`, including the active-c2 component, needs a separate
leading-class calculation because c2 and c6 remain live.  Write `V0=AS`
and `J=K-2TS`.  Extracting the complete literal A^-3 coefficient of g9
gives

```text
[-3S J^2+12T J(S^2-Z)-12ST^2(S^2-2Z)-8T^3]/65536.       (20)
```

Every c2, F5, and F6 contribution begins only at A^-2, so none can cancel
(20).  If `T!=0` at a root, D7 gives `J=0`; the leading D8 equation then
gives `S^2=2Z`.  Equation (20) becomes `-8T^3/65536`, again impossible.
Thus `A|T` on this component as well.  The load-bearing `-8` cubic is
guarded by live scalar mutations on both reductions; deleting it makes
both test branches vanish.

This proves the D9-repair theorem on the complete q1/c2 branch cover.

There is a useful but carefully typed operator echo.  The same-row raw
operator at weight nine is

```text
L9(R)=12A^3A'R-8A^4R'=-4A^3 T_A(R).                     (21)
```

The checker verifies (21) on every monomial in the raw `R9` window
`deg R9<=15` and rejects a sign mutation.  This is the same differential
operator as q1, but **not the same map**: the q1 primitive has degree at
most 12, while D9 uses `T_A:K[X]_(<=15)->K[X]_(<=18)`, preceded by the
necessary divisibility of the mixed row by `A^3`.

For the displayed D8 survivor, that preliminary divisibility already
fails.  Its D9 mixed row has a nonzero remainder modulo `A^3`; equivalently
the characteristic fraction reduces to

```text
(25+23X+21X^2-89X^3-6X^4-4X^5-2X^6)
---------------------------------------------------- .
             16384 C^3 B^2
```

So (21) cannot rescue this point: it dies before the `T_A` image test.  It
does, however, explain the exact shape of the next linear correction once
an N7/N8 branch reaches the `A^3` threshold.

The post-repair target is now smaller.  Write

```text
T=A U0,
Delta4=F4-V0 U0/16-Z^2/64=A W.                          (22)
```

On c2=0 the exact remaining D9 polar block is

```text
g9^- = 3W[-16V0W+A(64F5-U0Z)]/(256A^2),

A^2 | W[-16V0W+A(64F5-U0Z)].                           (23)
```

If `V0=CV1`, (23) forces `B|W`; it does not yet force `C|W`.  Thus the
gauge-invariant root split has moved from the first square-root coefficient
`T` to the next square defect `W`.  On the active-c2 component, the c2
lower-pole terms must be retained separately.  This is the smallest frozen
successor in `TARGET.json`; no D22 transport is licensed before it is
resolved.

## 6. Scope and next action

Promotable after hostile replay:

* the exact D7/D8 polynomiality formulas for the reviewed general prefix;
* the q1 divisor stratification and active-c2 reduction;
* the literal raw-window D0--D8 survivor with `A` not dividing `T`;
* its exact D9 failure;
* the global D9 repair `A|T` on both the proper-C and active-c2 components;
* the post-repair square-defect target (23) and identity (21).

Not claimed: emptiness of any complete q1 stratum; extension of the fixed
`V0=1` D22 contradiction; resolution of the active-c2 post-repair lower
block; implication of q1 by D1--D22; a GGV landing, counterexample, or JC2
conclusion.

The fastest next step is not a broad D22 elimination.  It is an exact desk
solve of the square-defect split (23), in parallel with the active-c2
post-repair block.  Only a surviving branch should be compiled onward.

## Replay

```bash
cd cases/ggv_8_28_upper_endpoint_q1_prefix_d7_d8_target_20260828
python3 -B verify_q1_prefix_target.py --check
shasum -a 256 -c SOURCE.sha256
shasum -a 256 -c EVIDENCE.sha256
```

The replay is deterministic, standard-library only, and takes under one
second on the producer machine.
