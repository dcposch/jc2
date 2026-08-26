# `(8,12)` order two: principal-part/UFD theorem, saturation-slice erratum V2

Date: 2026-08-26

Status: **CORRECTED PRODUCER THEOREM.  V1 IS IMMUTABLE AND HAS VERDICT
`REPAIR`; ONLY ITS §4 GLOBAL SATURATION-BEFORE-SLICE EQUALITY IS
WITHDRAWN.**

## 0. Frozen V1 and hostile review

```text
988d659f0a25f14a612d316608a8dc7c36d839c3f253c35e7e785d33e5923fb5
  xmodel/max12-812-order2-first-normal-principal-part-ufd-theorem-20260826.md
affd9b6004abc8078e2ae5b3ddc88307d7242d3ac8aa18eac36a21da0fed3639
  xmodel/max12-812-order2-first-normal-principal-part-ufd-review-grok-20260826.md
```

The hostile review confirms V1 identities `(1.1)`, `(2.1)`, `(3.1)`--
`(3.6)`, including every sign and constant, and confirms that the square
family solves the full first gate for arbitrary `k10`.  It identifies one
gap only: V1 §4 interchanged saturation and the slice `k10=0` when stating a
global reduced-support equality.

This document is a nonmutating erratum and corrected theorem.  It supersedes
V1 §4 and the corresponding phrase in the V1 status line.  All other V1
firewalls remain in force.

## 1. Exact principal-part theorem retained

Write

```text
K=z^4+p*z^2+c*z+r,
N=n3*z^3+n2*z^2+n1*z+n0,
f_Lambda=K^2+Lambda*N,
w_Lambda=f_Lambda^(1/8),
w0=K^(1/4),
H_Lambda(T)=T^12+Lambda^2*k10*T^10+O(Lambda^6).
```

With the frozen convention `H(w)-g(z(w))=sum r_l*w^-l`, the coefficient of
`Lambda^2` in the complete Faber tail is

```text
sum_(l>=1) q_l*w^-l
  = [ (3/8)*N^2/K + k10*K^(5/2) ]_-^z evaluated at z=z0(w),   (1.1)
```

where `z0` is the inverse of `w0=z+O(z^-1)`.  The signs are both positive.
The seven first-normal rows are the first seven coefficients of (1.1), and
the change from the first seven negative `z`-coefficients to the first seven
negative `w`-coefficients is unitriangular.

On `k10=0`, exactly

```text
q1=...=q7=0  iff  K divides N^2 in L[z].                         (1.2)
```

Over an algebraic closure, if

```text
K=prod_a (z-a)^m_a,
D_K=prod_a (z-a)^ceil(m_a/2),
```

then `K|N^2` iff `D_K|N`.

Away from the zero-normal section this gives precisely two irreducible
closures on the `k10=0` slice:

```text
S: K=(z^2+s)^2,
   N=(z^2+s)*(alpha*z+beta),
   k10=0;                                                        (1.3)

D: K=(z-a)^2*(z^2+2*a*z+d),
   N=lambda*(z-a)*(z^2+2*a*z+d),
   k10=0.                                                        (1.4)
```

Here `D` covers `[2,1,1]` and `[3,1]`; squarefree `K` forces `N=0`.
Moreover, the equations defining `S` solve every first-normal row for
arbitrary `k10`, since both `N^2/K` and `K^(5/2)` are polynomials on the
square locus.  Thus the arbitrary-load square closure is an exact family in
the full first gate.

## 2. Saturation notation

Let

```text
I  = (q1,...,q7),
A  = (p,c,r),
B  = (n0,n1,n2,n3,k10),
I* = ((I:A^infinity):B^infinity).                              (2.1)
```

This `I*` is the reviewed first-normal ideal `Q1*`: saturation occurs in the
full space before any `k10=0` slice.

Define instead the sliced-then-saturated ideal

```text
I0* = (((I+(k10)):A^infinity):B^infinity).                     (2.2)
```

On the slice, `D(B)` is simply the nonzero-normal open
`D(n0,n1,n2,n3)`.

## 3. Correct reduced-support statements

The following statements are exact.

### 3.1 Sliced-then-saturated equality

```text
V(I0*)_red = S union D.                                        (3.1)
```

Proof.  On `k10=0`, (1.2) and the UFD classification give exactly (1.3),
(1.4), or the zero-normal section.  Saturation by `B` deletes components
supported wholly on that zero section.  Both `S` and `D` meet `D(A)` and
the nonzero-normal open densely, so neither is deleted.  Taking closures
gives (3.1).  This is a reduced-support statement, not equality of
nonreduced ideals.

### 3.2 Equality on the actual first-contact open

Let

```text
O=V(k10) intersect D(A) intersect D(n0,n1,n2,n3).
```

Then

```text
(V(I*) intersect O)_red = ((S union D) intersect O)_red.       (3.2)
```

Indeed saturation does not change the geometric solution set on the two
declared opens, and every raw first-gate point in `O` is classified by
(1.2).  This is the source-relevant contact-order-one statement.

### 3.3 What survives after saturation-before-slice

Both named closures survive the full saturation:

```text
S union D  subset  V(I*) intersect V(k10).                     (3.3)
```

Each is an irreducible family in `V(I)` with a dense set in both saturation
opens.  Therefore its full affine closure, including its zero-normal and
weighted-origin boundary points, lies in `V(I*)`.

Conversely, every point of `V(I*) intersect V(k10)` outside `S union D`
must lie on the zero-normal section and have nonsquare `K`:

```text
E := (V(I*) intersect V(k10)) \ (S union D)
     subset V(k10,n0,n1,n2,n3) intersect {K nonsquare}.         (3.4)
```

This follows from (3.2) away from the zero-normal section; a square `K`
with `N=0` already belongs to `S`.

The set `E` is not proved nonempty.  It records exactly the unresolved
possibility that a nonsquare branch with `k10!=0` specializes to a
squarefree zero-normal point when `k10` tends to zero.  Full-space
saturation retains such a limit even though slicing first and then
saturating removes the isolated zero-normal section.

Therefore V1's displayed equality

```text
V(I*)_red intersect V(k10) = S union D
```

is withdrawn.  The exact unconditional replacements are (3.1)--(3.4).

## 4. Conditional recovery by the Padé lemma

If one proves the characteristic-zero support statement

```text
k10!=0 and q1=...=q7=0  =>  K is square,                       (4.1)
```

then `E` is empty and the withdrawn global reduced-support equality follows.
Indeed every component whose generic point has `k10!=0` is then contained
in the closed square locus, and all components contained in `k10=0` are
controlled by the sliced UFD classification after deleting zero-section
components.

The two-prime minAss agreement is navigation evidence for (4.1), not a
proof of it.  It supplies no characteristic-zero radical, reducedness, or
specialization theorem.

## 5. Scheme and campaign firewall

This V2 theorem proves:

- the exact principal-part identity (1.1);
- the exact `k10=0` divisibility criterion (1.2);
- the sliced/open reduced-support split (3.1)--(3.2);
- survival of both explicit closures in the full saturated gate (3.3);
- the exact location (3.4) of every still-possible extra point; and
- the arbitrary-`k10` square solution of the full first gate.

It does not prove (4.1), equality of nonreduced ideals, absence of embedded
components, reducedness of `I*`, or a complete characteristic-zero radical.
It does not construct a strict arc, control the higher-contact zero section,
impose the terminal `[6,2]` passport or either Taylor boundary, exclude
order two, close `(8,12)`, prove maximum twelve, or prove JC2.
