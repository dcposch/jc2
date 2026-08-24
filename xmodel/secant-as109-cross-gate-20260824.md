# SECANT-IDEMPOTENT × AS109 cross-connection gate

- Status: **FROZEN — COSTUME /
  NEED-GLOBAL-BOUNDED-ALGEBRAIC-OFF-DATUM**
- Requested trichotomy: **`COSTUME`**
- Date: `2026-08-24`
- Producer: OpenAI Codex, provisional cross-connection child
- Launch basis: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`
- Secant parent: `xmodel/fresh-connection-gate-20260824.md`, SHA-256
  `666bde51ea8bb78bd2c031122183148708b2b7de08547dc407191e633a712c4b`
- Parent tier: **PROVISIONAL** pending its different-model review.  This child
  neither reviews nor promotes it.
- AS109 dependency: only the banked conditional Hensel lemma from
  `xmodel/as109-support-gate-20260824.md`, with the carry erratum.  An exact
  fixed-support lift is assumed hypothetically; existence is not inferred.
- No canonical edit, generic support search, exponent rectangle, AWS, new
  Witt level, or counterexample claim.

## Verdict

The secant construction exactly recovers the already-known Hensel sheet
decomposition and adds no independent coefficient constraint to a cubic or
higher coupled AS109 compiler.

Modulo 109, after putting `t=x-u`, the seed self-collision algebra is

```text
I_0=(t(1-t^108),y-v),
e_0=1-t^108.
```

The diagonal is `t=0`; the off algebra is

```text
F_109[u,y,t]/(t^108-1)
  ~= product_(r in F_109^*) F_109[u,y].              (0.1)
```

Thus `e_0` is simply the Fermat indicator: one on the diagonal and zero on
the 108 nonzero residue-difference sectors.  All 108 sector idempotents and
their seed Teichmuller roots lift uniquely through the tested 109-adic
levels.  For a hypothetical exact determinant-one lift, multivariate Hensel
already lifts the same sectors as analytic collision graphs between the 109
source balls.

On every off sector, however, `x-u` is a 109-adic unit.  The universal
adjugate identity

```text
e(x-u)=a_22 f_1-a_12 f_2                         (0.2)
```

makes the secant equation `e=0` an exact member of the localized ideal of the
two collision equations.  At an off solution its tangent row is likewise

```text
de=(x-u)^(-1)(a_22 df_1-a_12 df_2).                (0.3)
```

Consequently the secant row adds algebraic rank zero to a coupled coefficient
compiler.  Idempotent lifting, factor count, trace, norm, and the automatic
degree bound on `e` all record the split-sheet geometry but do not constrain
the correction coefficients beyond the determinant/collision equations.

The precise missing input is a **global bounded algebraic realization of the
off sectors**—for example a bounded-support polynomial factorization or a
finite normalization/branch algebra tying all local analytic graphs together
and producing a coefficient equation outside the localized collision ideal.
No such datum is supplied by Hensel or by fixed support of `P,Q` alone.

## 1. Exact seed calculation modulo 109

Let

```text
P_0=x-x^109,       Q_0=y
```

over `F_109`.  For the fixed `x`-then-`y` divided-difference convention, the
secant matrix is diagonal and

```text
a_11
 =1-sum_(i=0)^108 x^(108-i)u^i
 =1-(x-u)^108,                                      (1.1)
a_22=1,
e_0=det A_0=1-(x-u)^108.
```

The second equality is the characteristic-109 freshman's dream.  The
collision equations become

```text
P_0(x)-P_0(u)=(x-u)(1-(x-u)^108),
Q_0(y)-Q_0(v)=y-v.                                  (1.2)
```

Changing variables from `(x,u)` to `(t=x-u,u)` gives the exact product

```text
C_0
 =F_109[u,y,t]/(t(1-t^108))
 ~=F_109[u,y] x F_109[u,y,t]/(t^108-1).             (1.3)
```

The first factor is the diagonal.  Since

```text
t^108-1=product_(r in F_109^*) (t-r)
```

and every root is simple, the off factor splits as (0.1).  Relative to the
second source point it has rank 108; including the diagonal gives 109 local
correspondence sheets.  Over a fixed target ball there are `109^2=11881`
ordered pairs, of which `109*108=11772` are off diagonal.

The replay constructs every Lagrange idempotent

```text
epsilon_r(t)
 =(108)^(-1) sum_(k=0)^107 (t/r)^k
       in F_109[t]/(t^108-1)                        (1.4)
```

and checks its values at all 108 nonzero roots: `11664/11664` evaluations
pass, and the 108 projectors sum to one.  It also Hensel-lifts every root of
`t^108-1` uniquely through `109^3` and verifies all 108 lifted roots are
distinct and reduce to the registered residue.

The Teichmuller roots are a **seed control**, not a claimed factorization of
the deformed secant determinant.  Under a hypothetical lift the sector
idempotents persist in the completed local collision algebra, but their
representatives and collision graphs may be infinite 109-adic analytic
series rather than bounded polynomials in `t`.

## 2. Hensel lifting across the source balls

Assume hypothetically

```text
F=(P,Q) in Z_109[x,y]^2,
F mod 109=(x-x^109,y),
det J_F=1.                                           (2.1)
```

Fix `b in F_109` and the target ball

```text
T_b=(0,b)+109 Z_109^2.
```

The reduction has identity derivative at every residue point.  The banked
multivariate Hensel lemma therefore makes each source ball

```text
B_(a,b)=(a,b)+109 Z_109^2,       a in F_109,
```

map analytically bijectively onto `T_b`.  Over a chosen second source ball,
the completed self-fiber product is the product of 109 analytic graphs: one
diagonal graph and 108 off graphs.  Over the target ball it is the product of
all 11881 ordered-pair graphs.

The secant idempotent is therefore the tuple

```text
(1,0,...,0)
```

relative to the second-source decomposition.  Its trace is one, the trace of
its complement is 108, and both nontrivial projectors have norm zero.  Over
the target-based `109^2` split, the diagonal projector has trace 109.  These
are ranks of already-split factors, not coefficient identities; their
divisibility by 109 creates no contradiction.

Idempotents lift uniquely across nilpotent `109^n -> 109^(n-1)` kernels and
in the 109-adic completion.  This proves persistence of the decomposition,
not persistence of finite polynomial representatives or fixed support.

## 3. Why the secant equation adds rank zero

Write the two exact collision differences as

```text
f_1=a_11(x-u)+a_12(y-v),
f_2=a_21(x-u)+a_22(y-v),
e=a_11a_22-a_12a_21.                                (3.1)
```

The adjugate identity gives (0.2) and its companion

```text
e(y-v)=-a_21 f_1+a_11 f_2.                          (3.2)
```

On an AS109 off sector, `x-u mod 109` is nonzero, so `x-u` is a unit.  Hence

```text
(f_1,f_2,e) localized at (x-u)
  =(f_1,f_2) localized at (x-u).                     (3.3)
```

Differentiate (0.2) at a collision with `e=f_1=f_2=0`; all product-error
terms disappear and (0.3) follows.  Thus adding `e` supplies neither a new
equation nor a new tangent cut to a coefficient system that already carries
the collision equations.

For a packed correction

```text
P=x-x^109+109A,
Q=y+109B,
```

write the secant entries as

```text
a_11=c+109 alpha,       a_12=109 beta,
a_21=109 gamma,         a_22=1+109 delta,
```

where `c` is the integral seed secant.  Then exactly

```text
e
 =c+109(alpha+c delta)
    +109^2(alpha delta-beta gamma).                  (3.4)
```

Any apparent digit equation obtained from `e=0` on an off collision is the
corresponding digit of (0.2), including its base-109 carries.  It is not an
independent successor equation for the coupled cubic compiler.

The same point holds if the compiler omits marked collisions: under (2.1),
Hensel supplies them automatically for every coefficient solution.  Adding
existential local branch variables therefore cannot cut the exact-lift
coefficient locus.

## 4. Degree, support, trace, and norm checks

If `deg P=d` and `deg Q=q`, the fixed secant entries have degrees at most
`d-1` and `q-1`, so

```text
deg e <= d+q-2.                                      (4.1)
```

For fixed supports of `P,Q`, the support of `e` lies in explicit Minkowski
sums of the divided-difference supports.  This is a deterministic derived
support bound, not a new restriction.  Reduction already forces the degree-108
term `1-(x-u)^108`, so the AS109 seed satisfies the obvious lower demand.

The single polynomial `e` distinguishes diagonal from the union of all off
sectors.  Refining that union into 108 lifted sectors requires idempotents in
the completed collision algebra.  Hensel guarantees them analytically, but
does not bound their polynomial degrees, monomial supports, or coefficient
heights.  Trace and norm only recover the ranks in Section 2.  None yields a
finite coefficient equation not already in (3.3).

## 5. Exact controls

### 5.1 Tame controls

The exact triangular source gauge

```text
G_7=(x+109y^7,y)
```

has Jacobian one and secant determinant literally one, so its off ideal is
the unit ideal.  This prevents the unbounded source-gauge representatives
from being mistaken for AS collision sectors.

The nontrivial tame automorphism

```text
(x+(y+x^2)^2,y+x^2)
```

has the parent's nonconstant nine-term secant determinant.  Independent
exact Groebner reduction again gives off basis `[1]`.  The mechanism is not
limited to triangular controls whose projector is visibly constant.

### 5.2 Growing-support all-Witt control

For every `n>=1`, the banked finite-level maps

```text
F_n=(x-x^109,
     y sum_(j=0)^(n-1)(109x^108)^j)        mod 109^n
```

satisfy

```text
det J_(F_n)=1-109^n x^(108n)=1 mod 109^n.             (5.1)
```

Their marked pair `(0,0),(1,0)` has secant projector zero at every level.
The replay checks (5.1) and the marked projector for `n=1,...,6`.  Meanwhile
the second coordinate has exactly `n` monomials.  Compatible finite-level
secant idempotents therefore coexist with the already-known linearly growing
support and nonpolynomial inverse limit.  Idempotent persistence does not
separate a fixed-support polynomial lift from this escape.

## 6. Deterministic replay and provenance

Artifact:

```text
cases/secant_as109_20260824/secant_as109.py
```

Replay:

```text
uv run --no-project --with sympy==1.14.0 \
  python3 cases/secant_as109_20260824/secant_as109.py
```

Result:

```text
29/29 Boolean checks PASS
11664/11664 CRT projector evaluations PASS
constraint_rank_added_on_off_sectors = 0
verdict = COSTUME / NEED-GLOBAL-BOUNDED-ALGEBRAIC-OFF-DATUM
```

Deterministic stdout SHA-256:
`3f9edfc6327d2859c32c8bfcd2e9aaff1d9fe39308a55989aa9c63a9655263e6`.

Frozen artifact/input hashes:

| Artifact | SHA-256 | Use |
|---|---|---|
| `cases/secant_as109_20260824/secant_as109.py` | `8024f629060624d86c88029452c8c4df85c0728a1e5388ae789965311c0ef98c` | present replay |
| `xmodel/fresh-connection-gate-20260824.md` | `666bde51ea8bb78bd2c031122183148708b2b7de08547dc407191e633a712c4b` | **PROVISIONAL secant parent** |
| `xmodel/as109-support-gate-20260824.md` | `b73aefd1c70667b041d13d40747ee273d6359ac1d7bbc600492595081d9268b5` | banked Hensel dependency |
| `xmodel/as109-support-gate-20260824-erratum.md` | `ca8a549c8b75873179fef536361c992c346ce5ac203b7e376c65ab4a116b9bbb` | carry scope |

The current quadratic-`y` no-go was read only to understand why the intended
client is cubic-or-higher; this gate does not depend on that provisional
result and supplies it no new equation.

## 7. Precise missing datum and resurrection condition

This route can resume only with an object that couples the local off sectors
**globally and algebraically**.  Any useful child must provide at least one of:

1. a finite normalization or polynomial branch algebra whose multiplication
   matrices realize all lifted off sectors with a proved degree/support bound;
2. a bounded polynomial factorization of the global secant/off algebra whose
   coefficient relations survive localization and are not generated by
   `f_1,f_2`; or
3. an elimination theorem showing that compatibility of all 108 analytic
   sector graphs forces a nonzero ideal in the fixed-support correction
   coefficients.

The success test for a cubic compiler is explicit: after quotienting by its
determinant and collision relations, the new row must have positive generic
rank.  Equation (3.3) proves the raw secant row has rank zero, so feeding it
to the compiler would only enlarge the presentation.

No exact lift, contradiction, characteristic-zero map, proof, or
counterexample is produced.  The secant parent remains provisional, and no
canonical campaign state is changed.
