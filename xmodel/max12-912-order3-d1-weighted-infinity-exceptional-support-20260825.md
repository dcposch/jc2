# D1 weighted-infinity exceptional support is the common-cubic curve

Date: 2026-08-25  
Status: **PRODUCER THEOREM; INDEPENDENT REVIEW REQUIRED**

## Theorem

Let `I_inf` be the eight-tail exceptional ideal of the cyclic-D1
coefficient-infinity Rees gate over a characteristic-zero field.  Thus
`s=1`, the finite-load Rees coordinates `K,M,N,R` vanish, and

```text
f=z^9+B7*z^7+...+B0,  g=F12(f),  r1=...=r8=0.
```

Evaluate on the `t=1` sheet above `s=1`.  The other two sheets are its
weighted cube-root orbit, so the descended exceptional rows vanish exactly
when the eight original tails vanish.

After saturation by the irrelevant ideal `(B0,...,B7)`, its reduced support
is exactly the depressed common-cubic curve

```text
C=z^3+p*z+r,  f=C^3,  g=C^4.                       (1)
```

Equivalently,

```text
B7=3p, B6=3r, B5=3p^2, B4=6pr,
B3=p^3+3r^2, B2=3p^2r, B1=3pr^2, B0=r^3.          (2)
```

This identifies the radical support only.  It does not assert that the raw
eight-tail ideal is radical or classify its nilpotent/embedded thickness.

## Proof

Let `z=z(w)=w+O(w^-1)` be the exact inverse root, so `f(z(w))=w^9`.
Because `g=F12(f)` on the exceptional divisor, its Faber expansion is

```text
g(z(w))=w^12-sum_(ell>=1) r_ell*w^(-ell).
```

The eight vanished tails therefore give

```text
g(z(w))=w^12+O(w^-9).
```

Put `W=g^3-f^4`.  Substitution into the last display gives

```text
W(z(w))=O(w^15).
```

Since `z(w)=w+O(w^-1)`, a nonzero polynomial retains its ordinary degree
under this substitution.  Therefore

```text
deg_z W <= 15.                                     (3)
```

Suppose `W!=0`.  Let `D=gcd(g^3,f^4)`, `e=deg D`, and

```text
A=g^3/D,  B=-f^4/D,  C=-W/D.
```

Then `A+B+C=0` and `A,B,C` are pairwise coprime.  Also `D|W`, so (3) gives
`e<=15` and `deg C<=15-e`, while

```text
deg A=deg B=36-e.
```

Mason--Stothers over characteristic zero yields

```text
36-e
 <= deg rad(ABC)-1
 <= deg rad(fg)+(15-e)-1
 <= (9+12)+(15-e)-1
 = 35-e,
```

a contradiction.  (If `e=36`, then `D` already has the full monic degree
and `W=0`; for nonzero `W`, divisibility and (3) force `e<=15` as used.)
Hence `g^3=f^4`.

Unique factorization and `gcd(3,4)=1` now give a monic cubic `C` with
`f=C^3` and `g=C^4`.  If
`C=z^3+c2*z^2+p*z+r`, the absent `z^8` term of the depressed `f` is
`3*c2`, so `c2=0`.  This proves (1); expansion gives (2).  Conversely, the
exact Faber construction sends `f=C^3` to `F12(f)=C^4`, whose inverse-root
tails all vanish.  Thus the two reduced supports agree.  Saturation removes
components supported only at the affine origin; it does not literally remove
that point from the affine cone.  `Proj` ignores the irrelevant point, and no
axis or discriminant stratum was localized away.

## Ramified-chart consequence

For an actual rational pole, write the slope as `m/n>3` in lowest terms and

```text
s-1=tau^n,  Lambda=tau^m,
B_i=tau^(m(9-i))*A_i(1+tau^n).
```

Rationality forces `n` to divide the gcd of the active leading weights.
On (2):

- if `p*r!=0`, weights `2,3` are active and `n=1`;
- if `r=0,p!=0`, the active weights are `2,4,6`, so `n|2`;
- if `p=0,r!=0`, the active weights are `3,6,9`, so `n|3`.

Thus no denominator beyond `3` occurs on the reduced exceptional support.
This is a finite denominator reduction, not a finite numerator reduction:
`m` remains unbounded.  The exceptional equations admit integer slopes
`m>=4` and the licensed half/third-axis slopes, so this theorem does not
exclude a coefficient-infinity arc at order zero.

## Scope firewall

An associated-graded common cubic need not persist to a common-cubic
trajectory.  The latter would have zero source bracket, but persistence is
the unproved normal Kuranishi problem.  Fixed-total-D12 common-cubic work and
the `(6,9)` common-cubic theorem do not cover this unbounded-total divisor.
No Taylor realization, D1 existence/exclusion, counterexample, or JC2 claim
is made.

## Frozen inputs

- `cases/max12_912_order3_d1_weighted_infinity_20260825/FREEZE.sha256`
- `cases/max12_912_order3_d1_passport_full_fibre_taylor_v2_20260825/compile_gate_v2.py`
- `xmodel/max12-912-order3-d1-classical-degree-split-20260825.md`
