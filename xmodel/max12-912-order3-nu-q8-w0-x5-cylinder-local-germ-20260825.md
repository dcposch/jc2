# Corrected-Q8 finite `x5=0` cylinder: exact local-germ exclusion

Date: 2026-08-25  
Status: **PRODUCER-EXACT; DIFFERENT-MODEL REVIEW PENDING**

## 1. Scope

Let

```text
X = V(e1,e3,e5,e7,e2,e4)
    subset Spec Q[w,c,d2,d4,x1,x3,x5]
```

be the same six divided approximate-cubic quotient rows used in the reviewed
selected corrected-Q8 leaf, before setting `w=0`.  Work on `D(x3)` and define

```text
B: x5=0, x1=x3, d2=d4=0, c*x3=1.
```

Thus `B` is the smooth twofold with coordinates `(w,a)`, `a=x3!=0`.
The claim below is only a source-scheme local statement along finite `B`.
It does not classify `a=0`, `a=infinity`, projective coefficient escape,
Taylor-polynomial realization, terminal reconstruction, `p=0`, other
`(9,12)` leaves, maximum twelve, Keller pairs, or JC2.

## 2. Exact source identities

The generator hash-pins the quotient compiler and its transitive
order-three source, then substitutes the full cylinder ideal

```text
E=(x5,x1-x3,d2,d4,c*x3-1,ib*x3-1).
```

Two independent AWS/Singular implementations return, without diagnostics,

```text
dim(B)=2,
e1=e3=e5=e7=e2=e4=0 mod E,
d(e1,e3,e5,e7,e2,e4)/dw = 0 mod E.
```

For the full `6 x 7` Jacobian in
`(w,c,d2,d4,x1,x3,x5)`, all seven `6 x 6` minors vanish modulo `E`.  The
`5 x 5` minor obtained by dropping source row `e5` and coefficient column
`c` is exactly

```text
(1024/1594323)*x3^6,
```

a unit on `D(x3)`.  Hence the full Jacobian has rank exactly five at every
geometric point of `B`.  The coefficient tangent

```text
(-a^-2,0,0,1,1,0) in (c,d2,d4,x1,x3,x5)
```

is killed by the six-row Jacobian; together with the `w` direction it is the
two-dimensional tangent space.  In particular, the predecessor rank test
`rank(J_y)=rank([J_y|F_w])=5` did **not** exhibit a direction approaching
`D(x5)`: here `F_w=0` and the displayed two tangent directions both have
`delta x5=0`.

The two retained lower invariants have exact normal forms on the whole
cylinder

```text
e6 = -4*a^3/81,
e8 = 0.
```

They are recorded for a later terminal/Taylor composition; no trajectory
claim is inferred from them here.

## 3. Local-algebra consequence

Fix a geometric point `q in B`.  Since `B subset X`, the local ring
`O_(X,q)` has Krull dimension at least two.  The rank-five Jacobian identity
gives embedding dimension `7-5=2`.  Therefore

```text
dim O_(X,q) = embdim O_(X,q) = 2,
```

so `O_(X,q)` is a two-dimensional regular local ring, hence a domain.  The
closed immersion `B subset X` induces a surjection

```text
O_(X,q) -> O_(B,q).
```

Both rings have dimension two.  A nonzero kernel in the regular local domain
would have positive height and would make the quotient have dimension at
most one.  Thus the kernel is zero: `X` and `B` have identical local schemes
at every finite point `a!=0`.

Equivalently, near every such `q`, `x5` vanishes identically on `X`.
Consequently

```text
q notin closure_X(X intersect D(x5)).
```

In particular, no closure of the selected generic open
`D(w*x5*(x3-2*x5))` can land at a finite point of this cylinder.  This
conclusion is source-local and does not rely on the still-running global
saturation computation.

## 4. Exact endpoints and replay

The accepted lanes are V3 only.  V1 is preserved with its two source-level
construction defects; V2 proved the displayed identities but emitted a
harmless Singular `redefining` diagnostic and therefore failed closed.

```text
Box02: std / dp
  rc=0, wall=6.83 s, max RSS=33148 KiB
  stdout SHA256 0b12669b9faa754325966a0ed9d07b6ae0b0365db361455d0dea2728bfc76b69

Box03: slimgb / block
  rc=0, wall=11.42 s, max RSS=34364 KiB
  stdout SHA256 2ccb5db3d8cde38dcb959996e4c2fe7713763895c199d015dae9f0b06c6ed1b8
```

Their generated Singular inputs differ by engine/order and have SHA256

```text
Box02 c089ea4f4800716578c73ff8f9fbd78a6bd5a59297bbdf34b11f0620fe6ee76a
Box03 e7a647537e4d065bebde46ccedd15a761071b8ae6914725e71583ab92b9c30d7
```

The AWS-only fail-closed replay checks fixed output/input hashes, all source
pins, unique markers, cylinder generators, zero runner codes, and absence of
every banned diagnostic.  It returns

```text
Q8_W0_X5_CYLINDER_LOCAL_GERM_V3_REPLAY_PASS
```

with stdout SHA256
`ecad27d9b47d66eafdb9edbc9b32be635c0493dd58eb3b5eda43835dd3782208`.

## 5. Remaining boundary

Combined only with the separately exact raw-special-fibre facts that
`A=x3-2*x5=0, x5!=0` is empty and the loaded overlap is empty, this removes
the finite `x5=0,x3!=0` cylinder from the selected-open closure.  The honest
remaining finite escape is the unloaded overlap

```text
x3=x5=0, e6=0,
```

and coefficient/projective infinity remains separate.  Those are the next
gates; this report does not claim their exclusion.
