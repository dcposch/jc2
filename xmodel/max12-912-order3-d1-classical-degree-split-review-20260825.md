# Independent review — D1 classical degree split

Date: 2026-08-25  
Verdict: **CONFIRMED**

## Reviewed target

```text
1424037680ac7ceeb0927388c59e5028f43ca9b7d37916cfea61809ca5ed7361  xmodel/max12-912-order3-d1-classical-degree-split-20260825.md
```

The stated implication is correct: after the polynomial source shear makes
`R0` regular at `s=1`, the bounds

```text
d_i=max(0,-ord_(s=1)(A_i)) <= 3(9-i)
```

force the exact ordinary total degrees `(27,36)`.  The
Guccione--Guccione--Valqui/Heitmann necessary condition then excludes a
counterexample because `gcd(27,36)=9<16`.

## Independent checks

1. The source shear is legitimate.  Depression gives
   `[y^8]P=9u^9R0=9h^3R0`.  Polynomiality therefore confines the finite poles
   of `R0` to the zero divisor of `h`; subtracting the polynomial part of
   `R0` by `(x,y)->(x,y-q(x))` makes `R0` regular at infinity.  This
   precomposition leaves `f`, `g`, and every `A_i` unchanged and preserves
   both the constant-Jacobian condition and automorphism status.

2. There is no ramification gap at coefficient infinity.  Over the finite
   constant field `L`, normalize `v=v_(s-1)` on `L(s)` by `v(s-1)=1`.
   The extension `t^3=s` is etale above `s=1`, since the reduction
   `T^3-1` is separable in characteristic zero.  Thus every place above
   `s=1` has ramification index one, `t` is a unit, and
   `v(u)=v(t^2/(s-1)^2)=-2`.  The invariant functions `A_i` consequently
   have the same integral valuation at every such place.  The positive-part
   convention `d_i=max(0,-v(A_i))` is the correct pole-order convention;
   allowing negative `d_i` is unnecessary and would no longer literally
   denote pole order.

3. Stage B kills the `t` and `t^2` components of each Taylor coefficient and
   imposes `L[x]` membership on its invariant component.  Since
   `x=s/(s-1)=1+(s-1)^(-1)`, the degree of a nonzero element of `L[x]`
   equals its pole order at `s=1`.  This justifies every conversion from the
   displayed local bounds to coefficient `x`-degree bounds.

4. For `P`, the `i`th contribution to `[y^ell]P` has pole order at most
   `d_i+2i <= 27-i <= 27-ell`; the monic `i=9` term obeys the same bound.
   Hence `deg_total(P)<=27`.  The coefficient `[y^9]P=u^9=h^3` contains the
   nonzero monomial `x^18y^9`, so equality is forced and cannot be cancelled
   by a term with a different `y`-exponent.

5. The Faber grading, including the load, is exact:

   ```text
   wt(z)=1,  wt(a_i)=9-i,  wt(F_12)=12,
   wt(F_6)=6,  wt(k)=6.
   ```

   Therefore a monomial in the `z^j` coefficient of
   `F_12+kF_6` satisfies

   ```text
   sum_i e_i(9-i)+6e_k+j=12,
   ```

   with `e_k` equal to zero or one.  Its Taylor contribution has pole order
   at most `36-18e_k-j <= 36-ell`.  Thus
   `deg_total(Q)<=36`; `[y^12]Q=u^12=h^4` supplies the uncancellable monomial
   `x^24y^12`, giving equality.

6. The cited GGV theorem is stated over an arbitrary characteristic-zero
   field, so passing to a finite constant extension causes no field-scope
   gap.  It applies to the sheared pair itself, whose counterexample status
   is the same as that of the original pair.

## Firewall

This review confirms only the bounded-pole implication and its classical
closure.  It does not prove the pole bounds, classify the strict sector
`d_i>3(9-i)`, classify the zero-tail/common-cubic boundary, or infer anything
from a fixed-load modular fibre.  It does not close another passport,
`k=0`, the order-one Kummer leaf, `(8,12)`, the full partial-`y` frontier, or
JC2.

## Frozen-source hashes checked

```text
a4fdac5d613e1af82ab135e220fedee5e41384c41e3068bcdf8921f60ababbcf  cases/max12_912_order3_fibre_20260824/order3_fibre.py
b9df8e900f4f07017a8d04bb30888356a4dbf0fc68ec0ad966a0bd7985f2080c  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/compile_gate_v2.py
67343b569db54f61f4a9e56e4262c0bf4fa781323a1287addbaf4fff93844623  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/independent_reconstruct.py
37beb7284ca579d5bdad4d7b609f49cfbedb141c60c1a90f6b69e72e1aae99a4  cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/stage_b_taylor.py
def1c2a141a6843f11886940d1a9c71f09adba0edee1088cbcbf0fa0c693c4a8  xmodel/sol-fixed-total-d12-classical-closure-v2-20260825.md
511d8a552a07c278a83e79263f883b2dd15f8b4155c30d49fd20cfa7254c5e4e  xmodel/sol-fixed-total-d12-classical-closure-review-as-20260825.md
```
