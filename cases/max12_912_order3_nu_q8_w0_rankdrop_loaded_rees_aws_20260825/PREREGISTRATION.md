# Preregistration: rank-drop-line loaded closure and weighted Rees screens

Date: 2026-08-25  
Status: **FROZEN BEFORE CAS**

Use exactly the hash-pinned six-row approximate-cubic source

```text
I=(e1,e3,e5,e7,e2,e4).
```

Translate the normal-rank-drop support by

```text
d4=b,  d2=b+1+u.
```

The landing centre is

```text
L: w=u=x1=x3=x5=0,
```

over the exact coefficient field `Q(c,b)`.  This is the generic point of
the rank-drop line; exceptional algebraic parameter strata remain charged.

The primary `loaded` mode computes exactly

```text
Csel = I : (w*x5*(x3-2*x5))^infinity
```

over `Q(c,b)` and tests `Csel+L`.  It also computes the conservative
off-boundary closure `Coff=I:(w,x1,x3,x5)^infinity` and tests `Coff+L`.
If either landing ideal is unit, the corresponding generic landing is
excluded.  A nonunit is a survivor and must be printed, not treated as
failure.

The independent `weighted` mode forms exact weighted strict transforms for

```text
wt(u)=wt(x1)=wt(x3)=wt(x5)=1,
wt(w)=m,  m=1,...,8,
```

divides every source row by its full common exceptional power, specializes
the Rees parameter to zero, and saturates by the leading selected load
`W*X5*(X3-2*X5)`.  These are exact screens for those weight charts only;
they are routing evidence and do not exhaust arbitrary weights.

As an explicit source-level control, at generic `b!=1` and on the first
normal kernel impose `U=X1=X3-X5=0`.  For slope `m=2`, the divided `e2`
initial form must reduce exactly to `(2/9)*W`; saturating by the selected
leading load must therefore be empty.  Run `b=1` separately over `Q(c)`:
this is the rank-one parameter value and may not be inferred from the
generic coefficient field.  Its slope-two loaded initial ideal must be
printed, whether empty or surviving.  Slopes at least three remain charged
unless the exact loaded saturation itself resolves the landing.

Acceptance requires mirrored exact-Q AWS `std/dp` and `slimgb/block` lanes,
source hashes, zero return codes, printed bases, and no diagnostics.  No
output may be promoted beyond the generic rank-drop line without separately
rebuilding every exceptional `(c,b)` stratum.  Global horizontal saturation
remains the final arbiter.
