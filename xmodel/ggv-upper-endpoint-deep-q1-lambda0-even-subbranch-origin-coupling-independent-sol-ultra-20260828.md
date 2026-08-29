# Lambda-zero parity attack: the even subbranch is empty, but the odd target fiber survives the first composition

Date: 2026-08-28  
Lane: independent parity/endpoint composition  
Status: **ALL-F-ODD-ZERO REFUTED EXACTLY; q7--q15 + ORIGIN TARGET + G11/G15 WINDOWS STILL CONSISTENT**

## 1. Verdict

On the reviewed `lambda=0`, `c2!=0`, exact-`D=0` branch, the exact
even-in-`t` subbranch

```text
F_odd=0
```

is empty.  The obstruction is the literal constant coefficient of the raw
endpoint row:

```text
D22[X0]=F11[X1]G11[X0]-F7[X0]G15[X1]=1.              (1)
```

Both first-component factors vanish when `F_odd=0`, so the left side is
zero.  This exclusion does not need q17, the four-root resultant, a
localization, or a CAS solve.

The tempting stronger claim that q5--q15 plus polynomiality of G15 always
forces the left side of `(1)` to vanish is false outside the exact square
slice.  I give an exact `Q=X` mutation satisfying

- q7, q9, q11, q13, q15 exactness;
- the active mode `c2!=0`;
- the full characteristic formulas for G11 and G15;
- both literal G11 and G15 raw windows; and
- a nonzero value of the left side of `(1)`.

After one harmless quadratic constant-field scaling, that value is exactly
one.  This mutation is not a full endpoint survivor: the other
characteristic windows, four-root endpoint compatibility, and remaining
determinant rows are not imposed.  It shows precisely that the next
exclusion must use more than the q-gates and G15 polynomiality.

For completeness, the parity substitution `s=t^2` reduces the all-even raw
system to a Laurent weighted-Jacobian family with pole orders `(4,6)`.
The inherited family is empty by `(1)`; it is not the already closed AS109
sextic `(4,6)` normal form, whose support and polynomial-base hypotheses are
different.

## 2. Frozen origin input and independent window derivation

The coordinator's frozen origin lemma and checker are

```text
xmodel/ggv-upper-endpoint-origin-odd-coupling-sol-ultra-20260828.md
SHA256 3e4a0f03acec2ee5e3cdfff558c481e14735408aa18486d23215958ed8d4bb3a

cases/ggv_8_28_upper_endpoint_origin_odd_coupling_20260828/
  verify_origin_odd_coupling.py
SHA256 f23a6d959dc9a8854f051c16a1fe287dea91d5b66b01a63198a64715c08c04c8
```

The raw row is

```text
D_n=sum_(i+j=n)((12-j)F_i'G_j+(i-8)F_iG_j').          (2)
```

To contribute to `[X0]`, the differentiated factor must use its `X1` slot
and the other factor its `X0` slot.  At weight 22, independent enumeration
of both exact floors gives

```text
first summand:  (i,j)=(11,11), coefficient 12-j=+1;
second summand: (i,j)=(7,15),  coefficient i-8=-1.    (3)
```

The apparent neighbours vanish structurally: `(10,12)` has `12-j=0`, and
`(8,14)` has `i-8=0`.  Every other pair lacks a required literal slot.
Equations `(2)`--`(3)` prove `(1)` with its sign.

In particular,

```text
F_odd=0  ==>  F7[X0]=F11[X1]=0  ==>  D22[X0]=0,       (4)
```

contradicting the target.  The conclusion does not require `G_odd=0`,
although the complete even-mode characteristic would imply it.

## 3. Complete characteristic form of the coupling

The full reviewed characteristic is

```text
G=F^(3/2)+sum_(k=1,...,10)c_(2k)t^(2k)F^((6-k)/4).    (5)
```

There is a compact exact way to reconstruct the two needed slots without
dropping any mode.  Put

```text
Phi(t)=F(0,t),              Psi(t)=F_X(0,t).
```

Then

```text
G11[X0]=[t^11]{Phi^(3/2)
  +sum_k c_(2k)t^(2k)Phi^((6-k)/4)},                  (6)

G15[X1]=[t^15] Psi*{(3/2)Phi^(1/2)
  +sum_k ((6-k)/4)c_(2k)t^(2k)Phi^((2-k)/4)}.         (7)
```

Only shifts that can reach the displayed weight contribute, but `(6)`--`(7)`
retain the complete schedule automatically.  When evaluating fractional
powers, the branch factors are the reviewed literal powers `A^(6-k)`.
Replacing them by an unchosen scalar branch of `(A^4)^((6-k)/4)` can reverse
signs when `A(0)=-1`; the checker contains an explicit guard against that
error.

Substitution of `(6)`--`(7)` in `(1)` is the smallest exact coupling of the
q-gate odd fiber to the raw target.

## 4. Exact q-gate/target mutation

Take

```text
A=X^4-1,          Q=X,          e=F8=r=0,
c2=c6=1,          all other displayed modes zero.     (8)
```

Write `F7=A f` and choose the literal raw odd tail

```text
f   =(2^29/75)(-1+11X^4),
F9  =(2^23/75)(7X-27X^5),
F11=F13=0.                                             (9)
```

All floors are legal.  The exact primitive witnesses for

```text
h_n=(5A'd_n+2Ad_n')/2
```

are

```text
d7 = (2^27/75)X,
d9 =-(2^21/15)X^2,
d11=(2^14/3)X^3,
d13=-(7*2^8/15)X^4,
d15=X^5.                                               (10)
```

Direct substitution in the independently derived q7--q15 formulas verifies
all five equations exactly.

The complete characteristic expansion `(5)`, not a truncated mode replay,
then gives

```text
G11=A*P11,

P11=(3*2^21/5)X-(7*2^18/25)X^2
    -(49*2^21/15)X^5+(27*2^18/25)X^6,

G15=-(2^21/5)X+(2^10/3)X^3.                           (11)
```

Thus G11 lies in its literal `X^1,...,X^13` window and G15 lies in its
literal `X^1,...,X^9` window.  In particular, G15 has no pole at any root of
`A`; polynomiality alone does not kill this mutation.

Here `F11[X1]=G11[X0]=0`, while

```text
F7[X0]=2^29/75,        G15[X1]=-2^21/5.
```

Therefore the left side of `(1)` is

```text
2^50/375 != 0.                                            (12)
```

Scale every odd raw coefficient and every odd primitive in `(9)`--`(10)`
by a constant `theta`.  Through weight 15 the characteristic odd
coefficients scale linearly, and every q equation remains homogeneous.
After adjoining

```text
theta^2=375/2^50,
```

equation `(12)` becomes exactly one.  This proves:

> q5--q15 exactness, the active c2 open, the raw origin target, and the full
> G11/G15 polynomial windows are jointly consistent on an exact algebraic
> fixture.

It does not assert consistency of any omitted row or window.

### Scope of the square-face identity

On the narrower fixed slice `Q=e=F8=0`, the coordinator found that q-gate
primitive coordinates factor the endpoint through the X coefficient of a
G15 pole numerator.  G15 polynomiality then forces the endpoint to zero.
The mutation `(8)`--`(12)` shows the load-bearing role of `Q`: that
factorization cannot be promoted unchanged to arbitrary `Q`.

## 5. The all-even weighted-Jacobian reduction

Although `(4)` already excludes the all-even locus, its reduced system is a
useful structural checksum.  Put

```text
s=t^2,
f(X,s)=F(X,t),            g(X,s)=G(X,t).
```

Then `t partial_t=2s partial_s`, and the determinant equation is

```text
D(F,G)=2R(f,g),

R=f_X(6-s partial_s)g+(s partial_s-4)f g_X.            (13)
```

For

```text
f=sum_(i=0,...,7)f_i s^i,
g=sum_(j=0,...,10)g_j s^j,
```

the complete coefficient system is

```text
R_n=sum_(i+j=n)((6-j)f_i'g_j+(i-4)f_i g_j'),

R_11=1/2,                  R_n=0 for n!=11.            (14)
```

All odd original determinant rows vanish on the parity-fixed locus.  The
literal even windows contain 75 F-slots and 157 G-slots; the checker
reconstructs every one.

Equivalently, put

```text
U=f/s^4,                  V=g/s^6.
```

An exact calculation gives

```text
det partial(U,V)/partial(X,s)=-R/s^11.                 (15)
```

Thus `(14)` is a constant Laurent-Jacobian equation

```text
det partial(U,V)/partial(X,s)=-1/2                    (16)
```

with the inherited parity Newton windows and pole orders `(4,6)` along
`s=0`.  This is a strict weighted Laurent subfamily of the GGV upper chart.
It is not automatically the AS109 polynomial-in-`z` sextic normal form:
positive powers of `s` remain legal.  The exact legal mutation

```text
f6=X^2,            g10=X^4
```

already kills the top high-high row, so the upper rows alone do not simply
erase every positive Laurent tail.

The inherited weighted family is nevertheless empty because its constant
target coefficient is exactly `(4)`.

## 6. Smallest unresolved obstruction

The leading four-root even face still supplies the reviewed 15 quotient
coordinates in `K[X]/(A)`:

- 12 after eliminating `c14,c16,c18,c20` from the four regularity rows;
- 3 after eliminating the endpoint kernel scalar from the primitive-
  difference row.

But the all-even section cannot be used as a fiber over that resultant.
Every true endpoint survivor must have a nonzero odd tail satisfying `(1)`.

After the mutation in Section 4, the smallest unresolved exact intersection
is therefore:

1. the 15-coordinate four-root even resultant;
2. the q5--q15 odd connection equations plus `(1)`;
3. the remaining raw characteristic windows beyond G11/G15; and
4. the determinant rows not implied by those necessary conditions.

The fixed-square `G15` numerator identity is a useful specialization and
mutation control, but it is not the universal resultant.  A credible next
elimination should work in `K[X]/(A)` with arbitrary `Q`, rather than set
`Q=0` before extracting the origin equation.

No half-step equation can resurrect the all-even subbranch: `(1)` has
already killed it.  Half-step equations can only restrict the required
nonzero odd fiber.

## 7. Frozen verifier

```text
cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_even_subbranch_20260828/
  verify_even_subbranch_reduction.py
```

Expected marker:

```text
PASS_EXACT_LAMBDA0_EVEN_SUBBRANCH_REDUCTION
```

The checker uses Python standard-library exact rational arithmetic.  It
pins the origin packet, re-enumerates `(1)`, reconstructs all 232 even raw
slots and the Laurent identity `(15)`, verifies `(9)`--`(12)` including the
literal G windows, and retains a positive-tail mutation.  No heavy local CAS
or AWS computation was used.

No claim is made that the Section 4 mutation satisfies all raw G windows,
the 15-coordinate endpoint resultant, D23--D35, a Keller pair, or JC2.
