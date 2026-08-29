# td12 U1 sibling: exact reduced Prop. 8.1(iv) / T1 ratio solve

Date: 2026-08-29  
Producer: Sol 5.6 (Ultra), exact desk algebra  
Status: sealed producer result; different-model review required before use

## 0. Result

For the P0 cell

```text
(nu,dp,dq,E,kbar,X,l,k,Sm,eps,lex)
  = (17,68,52,36,13,17,2,2,2,0,0),
```

with one distinguished arrival orbit of multiplicity two and two distinct
simple nonzero northeast orbits, the reduced Proposition 8.1(iv) / T1 system
is **NONEMPTY AND RIGID UP TO ONE COMMON SCALE**.

Writing `t=eta^17`, let `A` be the arrival orbit value and `B,C` the two NE
orbit values.  Up to nonzero scalar factors, the only source-typed shapes are

```text
p(eta) = (t-A)^2 (t-B)(t-C),
q(eta) = eta (t-A)(t-B)(t-C).
```

The exact coefficient equations force

```text
B+C = 9A/4,                 BC = 45A^2/32,
B/A = (9+3i)/8,             C/A = (9-3i)/8,
```

up to swapping `B,C`.  Equivalently,

```text
B/C in {(4+3i)/5, (4-3i)/5}.
```

The raw root locus has the expected one parameter `A in C*`; common
`t`-dilation is the standard chart gauge, so the quotient has one unordered
ratio point (two ordered points).  Overall nonzero scalars of `p` and `q` are
also inessential for the root-pattern solve.  The requested classification is
therefore:

```text
FINITE RATIOS / RIGID ONE-SCALE TEMPLATE,
not EMPTY, and not positive-dimensional after genuine gauges.
```

At gauge `A=1`, a rational-coefficient representative is

```text
p = (t-1)^2 (t^2-(9/4)t+45/32),
q = eta (t-1)(t^2-(9/4)t+45/32).
```

It satisfies the reduced Wronskian equation with nonzero right side.  Thus T1
does **not** kill the sibling.  This result neither consumes nor reviews the
provisional sibling charge theorem beyond using the stated P0 tuple; if that
theorem survives its independent gate, the twin source-child tests remain the
next layer.

## 1. Custody and scope

Exact read inputs:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf
7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77
  ladder/BOOK-OFFAXIS.md
e766bfe27ac9a06ef6eab053dbea666f8b3d3e70a48ee8c76b88e45246c3bea9
  cases/l1_ode_check.py
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271
  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
91b36515950f038d08a444df16f9c09ee9763adb7950d46e9c50e43451f25c0f
  xmodel/m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md
52ffafa2e79823e275e084d9d3c3a36329401cc9449a6e572379ce1ee0390b69
  xmodel/m2-td12-u1-sibling-exact-charge-r1-sol56-20260829.md
```

The sibling charge report was treated only as a provisional carrier of the
tuple and execution order.  Its Fable hostile review, prompt, log, and run
record were not read.  No conclusion below depends on charge `4+4`, budget
saturation, a source-child gate, or the existence of this cell in an actual
configuration.

The printed source was read at Proposition 8.1 (printed pp. 39--41) and the
case-(II) displays in Statement 9.6 (pp. 51--53).  The current BOOK P0 repair
was read at `BOOK-OFFAXIS` R1.0, R1.3, and P0.  The old checker was inspected
only as a negative-control dictionary for the already-reviewed root law; no
new machine solve is a proof dependency.

Only short desk algebra was used.  There was no web access, AWS action, heavy
local computation, canonical edit, commit, or push.

## 2. Reconstruct the literal P0 shapes

The tuple has

```text
l=2,       k=2,       Sm=1+1=2,       eps=0,       lex=0,       nu=17.
```

BOOK P0 gives, for an arrival orbit `A` and NE orbits `B,C`,

```text
p = alpha (eta^17-A)^2 (eta^17-B)(eta^17-C),
```

because the arrival multiplicity is two, the two non-chain multiplicities
are one, and there is no zero factor.  Proposition 8.1(iv)'s root valuation,
recorded as BOOK R1.0, says every root of `p` is an **exactly simple** root of
`q`, every other `q`-root is simple, and for `nu>=2` one has `eta || q`.
Since `lex=0`, there is no q-only nonzero orbit.  Hence

```text
q = beta eta (eta^17-A)(eta^17-B)(eta^17-C),
```

with `alpha,beta != 0`.

The degrees check without interpretation:

```text
deg p = 17(2+1+1)=68,
deg q = 1+17(1+1+1)=52.
```

The remaining P0 inequalities also check:

```text
E = l*dq-dp = 2*52-68 = 36 > 0,
1*dq < dp < 2*dq,       gcd(dp,dq)=4,       gcd(4,17)=1.
```

Thus the simple orbits are NE and the double orbit is the distinguished
arrival direction.

### 2.1 Printed Statement 9.6 is not the controlling q-shape

The uncorrected printed case-(II)(a) display repeats the double arrival factor
in `q`.  That cannot be used here:

- it violates the root valuation forced by Proposition 8.1(iv), since a
  `p`-root must occur exactly once in `q`; and
- with this cell it would give q-degree `1+17(2+1+1)=69`, not `52`.

The cleanest correction is exactly BOOK R1.0/P0: retain the multiplicity-two
factor in `p`, replace every p-orbit factor in `q` by its radical, retain the
forced simple `eta`, and then add only the explicitly recorded `lex` q-only
orbits (none here).  This repair is load-bearing for T1.

## 3. The exact Wronskian equation

Proposition 8.1(iv) reads

```text
delta p q' - (1-u) p' q = Theta p,       Theta != 0.
```

Top-degree cancellation gives

```text
delta/(1-u) = dp/dq = 68/52 = 17/13.
```

Multiplying by the common denominator, or equivalently using the
`(X,kbar)=(17,13)` normalization, gives the exact T1 equation

```text
17 p q' - 13 p' q = Theta p,             Theta != 0.          (3.1)
```

All derivatives in (3.1) are with respect to `eta`.

Put

```text
t=eta^17,
r(t)=(t-A)(t-B)(t-C),
s(t)=(t-B)(t-C)=t^2-sigma*t+pi,
sigma=B+C,       pi=BC.
```

Then, after removing the harmless scalars,

```text
p_0=(t-A)r,             q_0=eta*r.
```

The chain rule gives

```text
q_0' = r+17t r',
p_0' q_0 = 17t p_0,t r.
```

Substitution into (3.1), followed by division by `p_0`, gives

```text
r + 17t r' - 13t (p_0,t/p_0) r = chi,
chi := Theta/(17 beta) != 0.
```

Since `p_0=(t-A)r`, this is

```text
r + 4t r' - 13t r/(t-A) = chi.
```

Finally `r=(t-A)s` reduces the entire Wronskian to the first-order polynomial
ODE

```text
4t(t-A)s' - (8t+A)s = chi.                              (3.2)
```

No root, degree, or genericity condition was used to cancel a potentially
zero scalar; (3.2) is a polynomial identity obtained in the fraction field
from the nonzero polynomial `p_0`.

## 4. Exact coefficient solve

Insert

```text
s=t^2-sigma*t+pi,            s'=2t-sigma
```

into (3.2).  Direct expansion gives

```text
4t(t-A)s'-(8t+A)s
  = (4sigma-9A)t^2 + (5A sigma-8pi)t - A pi.             (4.1)
```

Therefore the complete coefficient system is

```text
4sigma-9A=0,
5A sigma-8pi=0,
chi=-A pi != 0.                                          (4.2)
```

It has the unique solution

```text
sigma=9A/4,             pi=45A^2/32,
chi=-45A^3/32.
```

In particular `A!=0`, as already required by P0, makes the right side
nonzero automatically.  The two NE orbit values are the roots of

```text
z^2-(9A/4)z+45A^2/32=0.
```

Its discriminant is

```text
(9A/4)^2-4(45A^2/32) = -9A^2/16,
```

so over `C`

```text
B=(9+3i)A/8,            C=(9-3i)A/8,
```

up to interchange.  The original RHS constant is

```text
Theta = 17 beta chi = -765 beta A^3/32 != 0.
```

This also gives an immediate exact substitution check at `A=1`:

```text
s=t^2-(9/4)t+45/32,
4t(t-1)s'-(8t+1)s = -45/32.
```

Thus existence is proved over `Q(i)` at the root level and even over `Q` at
the coefficient level.

## 5. Admissibility and negative controls

Every P0 side condition is strict on the solution.

1. **NE roots distinct.**  The discriminant `-9A^2/16` is nonzero.
2. **NE roots nonzero.**  `BC=45A^2/32 != 0`.
3. **No collision with the arrival orbit.**

   ```text
   (A-B)(A-C)=s(A)=A^2-(9/4)A^2+45A^2/32=5A^2/32 != 0.
   ```

4. **The zero orbit is not a p-root.**

   ```text
   p_0(0)=A^2 BC=45A^4/32 != 0.
   ```

   Hence the forced `eta` factor of `q` is a simple q-only zero root, exactly
   as R1.0 requires; it is not a free p-direction because `eps=0`.
5. **The RHS is not the homogeneous branch.**  Equation (4.2) gives
   `chi=-A*pi != 0`.  Conversely `chi=0` would force `A*pi=0`, contradicting
   the nonzero arrival and NE roots.
6. **Root-multiplicity mutation.**  Squaring `(t-A)` in `q` fails both the
   local valuation and degree control (`69 != 52`).  Omitting `eta` gives
   degree `51` and fails the `nu>=2` semi-invariance/root law.
7. **Coefficient mutations.**  Changing `sigma` leaves the residual
   `(4sigma-9A)t^2`; after fixing `sigma=9A/4`, changing `pi` leaves
   `(45A^2/4-8pi)t`.  Thus no hidden continuous ratio parameter survives.
8. **Translation is not a gauge.**  Translating all three t-orbit values by
   `h` sends `(A,sigma)` to `(A+h,sigma+2h)`.  The first equation in (4.2)
   acquires residual `-h`, so only `h=0` preserves T1.  This agrees with the
   source typing: `eta=0` is the distinguished simple q-root.

These controls rule out the common false positives: the uncorrected printed
q-shape, a zero NE root, a repeated NE orbit, an arrival/NE collision, a
zero-RHS homogeneous solution, and a spurious affine-translation modulus.

## 6. Genuine gauges and dimension

There are three harmless continuous rescalings in the raw presentation.

1. `p -> alpha p` changes no root data and cancels from (3.1).
2. `q -> beta q` rescales `Theta` by the same factor and changes no root data.
3. `eta -> gamma eta` gives `t -> gamma^17 t`, hence a common dilation
   `(A,B,C)->lambda(A,B,C)`, `lambda=gamma^17`.  Over `C` every
   `lambda in C*` occurs.  Equations (4.2) are homogeneous under

   ```text
   (A,sigma,pi,chi) -> (lambda A, lambda sigma,
                         lambda^2 pi, lambda^3 chi).
   ```

The deck subgroup `gamma^17=1` fixes `t` and only rescales the displayed
`eta` factor in `q`, already absorbed by `beta`.  The only remaining symmetry
is the discrete swap `B<->C`.

Thus the raw admissible root locus is the one-scale cone `A in C*`, while its
genuine quotient has a single unordered point.  If the NE roots are ordered,
the quotient has the two reciprocal ratio values

```text
B/C=(4+3i)/5,             C/B=(4-3i)/5.
```

This is the precise sense in which the answer is **finite ratios**, rather
than a positive-dimensional moduli family.

## 7. Maximum safe consequence

At reduced Proposition-8.1/T1 scope:

> The td12 U1 sibling P0 cell `(17,68,52)` is coefficient-compatible with the
> reduced Wronskian.  Its orbit polynomial is uniquely the rigid one-scale
> template
>
> ```text
> (t-A)^2 (t^2-(9A/4)t+45A^2/32),
> ```
>
> and the q-radical is
>
> ```text
> eta (t-A)(t^2-(9A/4)t+45A^2/32).
> ```

Accordingly the sibling is **T1-ALIVE**.  A conforming campaign execution may
continue to the two first-child coefficient vectors and their coupled Keller
recurrences only after the provisional charge/source-gate packet clears its
independent review.

This report does not prove that the reduced cell occurs in a complete tree,
that the top pattern lifts to lower source coefficients, that the twin child
conditions pass, that a formal germ or polynomial Keller pair exists, or that
any td12 configuration, counterexample, or JC2 conclusion follows.

## 8. Hostile-review checklist

1. Re-derive the q-radical from Proposition 8.1(iv), rather than copying the
   squared q-factor in printed Statement 9.6.
2. Check the chain-rule factors `17` and the normalization
   `X:kbar=17:13`; a missing factor changes both ratios.
3. Check that `A,B,C` are orbit values (`raw coefficient^17`), not 51 raw
   roots to be counted separately.
4. Check every division leading to (3.2) and expand (4.1) independently.
5. Check that common dilation, not translation, is the admissible root gauge.
6. Keep T1 compatibility separate from the provisional exact-charge theorem,
   source realization, and landing.

*End of sealed report body.*

## Seal (outside the sealed body)

- Body length: `11879` bytes (the complete file before this seal heading,
  including the blank separator after `*End of sealed report body.*`).
- Body SHA-256:
  `d505e3668a9c2152762e8beb7101e12a52db48c4c1d110ab55fcac2b383892ba`.
