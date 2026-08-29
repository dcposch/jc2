# Deep q1 lambda-zero branch: independent q5--q13 odd-tail audit

Date: 2026-08-28  
Lane: independent sharp-successor audit  
Status: **PASS THROUGH q13; THE FIVE ODD GATES LEAVE A UNIVERSAL AT-LEAST-NINE-DIMENSIONAL RAW SURVIVOR**

## 1. Verdict

Work in characteristic zero on the reviewed squarefree branch-P component
with `c2!=0`, exact `D=0`, and the fully licensed q1/q3 consequence

```text
lambda=0,  S=U=0.
```

The q5/q7/q9 producer is correct.  In particular, the q9 denominator is
`2^23`, not `2^22`, and the polynomial connection-image condition is both
necessary and sufficient.  The frozen comparison packet is

```text
xmodel/ggv-upper-endpoint-deep-q1-lambda0-odd-gate-prefix-sol-ultra-20260828.md
SHA256 db230f946e04a3be58dd3e59877d47b23097ec79079109120fce91163be138bf

cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_odd_gates_20260828/
  verify_lambda0_odd_gates.py
SHA256 d93ca0c7753097c4dcf6aae1cc58d1966780256700df4179e6e6fda9e30e1f64
```

Writing `F6=Ae/2048`, the complete odd coefficients through q13 are

```text
q_n=p^3 h_n,

h5  = r/1024,

h7  = f/4-Qr/65536,

h9  = F9/4-3Qf/256-3Q^2r/2^23,

h11 = A F11/4-5QF9/256+5Q^2f/2^15
        +5r(Q^3+32e)/2^29,

h13 = A^2 F13/4-7AQF11/256+21Q^2F9/2^15
        +7f(Q^3+32e)/2^21
        +7rF8/2^13+7rQe/2^30+35rQ^4/2^37.          (1)
```

For every fixed legal even prefix `(A,Q,e,F8)`, imposing exactness of all
five odd differentials gives a homogeneous linear system on the literal raw
odd windows.  It is **never universally inconsistent**: its raw solution
space has dimension at least nine.  Exact matrices on two unrelated
squarefree quartics have the maximal possible rank and hence dimension
exactly nine.  Exact dimension nine is fixture evidence; the universal
theorem is the lower bound.

There is also a clean universal even-gate result.  Every even `q_n` on this
branch is a polynomial divisible by `A`, so every even differential is
automatically exact.  Thus no interleaved even gate adds a constraint; the
odd sequence really is the sharp de Rham tail.

This does not solve the endpoint locus.  The first no-new-raw-odd-slot gate
q15, later odd gates, and the endpoint/half-step equations remain.

## 2. Reduced prefix and exact raw windows

The reviewed common-root and q3 consequences give

```text
F0=A^4,
F1=F3=0,
F2=-A^3Q/8,                       deg Q<=2,
F4= A^2Q^2/256,
F5= A^2r/256,                     deg r<=3,
F6= Ae/2048,                      deg e<=6,
F7= Af,                           deg f<=5.             (2)
```

Here `A|P1` at all four simple roots gives the second factor of `A` in
`F5`, and `A|F7` gives the displayed form of `F7`.  The later authoritative
raw windows needed in this pass are exactly

```text
F9  in span( X,...,X^7 ),          dimension 7,
F11 in span( X,...,X^5 ),          dimension 5,
F13 in span( X^2,X^3 ),            dimension 2.          (3)
```

The lower floors in `(3)` are imposed literally in the verifier.  In
particular, no constant coefficient is silently restored to `F9` or `F11`,
and neither the constant nor linear coefficient is restored to `F13`.

## 3. Independent Lagrange derivation

Start from

```text
q_n=2/(n+2) [t^n] F^((n+2)/8).                         (4)
```

Let

```text
E(t)=1+F2 t^2/A^4+F4 t^4/A^4+F6 t^6/A^4+F8 t^8/A^4+...
```

be the even normalized series.  Through weight 13, at most one odd
coefficient can occur in a contributing partition, since the first odd
weight is five and `5+5+5>13`.  Differentiating the binomial series once in
its odd part gives, for odd `n<=13`,

```text
q_n = p^(n-6)/4 *
      sum_(j=5,7,...,n) F_j [t^(n-j)]E(t)^((n-6)/8),   (5)
```

where `p^2=A`.  Substitution of `(2)` in `(5)` gives exactly `(1)`.  A
self-contained sparse Laurent-polynomial expansion in the checker verifies
all five identities symbolically, rather than sampling the producer's
implementation.  It also rejects the load-bearing mutation

```text
-3Q^2r/2^23  -->  -3Q^2r/2^22
```

in `h9`.

The identities are unchanged up to harmless nonzero sheet scalars on the
other quadratic twist, so their exactness conditions are the same.

## 4. Exact odd primitive-image theorem

Define the polynomial connection

```text
T5(d)=(5A'd+2Ad')/2.                                  (6)
```

For every polynomial `h`,

```text
p^3 h dX is exact in K(X,p)  iff  h=T5(d)
for some d in K[X].                                   (7)
```

Sufficiency is an identity:

```text
d(p^5d)=p^3(5A'd+2Ad')/2 dX.
```

For necessity, take the odd-character part of a rational primitive and
write it as `pC`.  Exactness gives

```text
2AC'+A'C=2A^2h.                                       (8)
```

At a simple root of `A`, a pole of integral order `m>=1` in `C` would have
uncancelled leading multiplier `1-2m`; away from `A`, the derivative raises
the pole order.  Hence `C` is polynomial.  Reducing `(8)` modulo `A` gives
`A|C`; writing `C=AE` and reducing once more gives `A|E`.  Put `E=Ad`.
Equation `(8)` then reduces exactly to `h=T5(d)`, proving necessity and
sufficiency with no omitted rational primitives.

If `deg d=k`, the leading coefficient of `2T5(d)` is

```text
(2k+20) lc(d) X^(k+3).
```

It never vanishes in characteristic zero.  Thus `T5` has no polynomial
kernel, and if `deg h<=D` then `deg d<=D-3`.

As the first application, `h5=r/1024` and `deg r<=3` force `d` to be a
scalar and hence recover the exact producer conclusion

```text
r in K*A'.                                             (9)
```

## 5. The complete triangular system and its dimension

Equations `(1)` and `(7)` give the following literal finite system:

| gate | newest raw polynomial | raw dimension | `deg h_n` | primitive `deg d_n` | coefficient equations |
|---|---:|---:|---:|---:|---:|
| q5 | `r`, degrees `0..3` | 4 | <=3 | <=0 | 4 |
| q7 | `f`, degrees `0..5` | 6 | <=5 | <=2 | 6 |
| q9 | `F9`, degrees `1..7` | 7 | <=7 | <=4 | 8 |
| q11 | `F11`, degrees `1..5` | 5 | <=9 | <=6 | 10 |
| q13 | `F13`, degrees `2..3` | 2 | <=11 | <=8 | 12 |

For fixed `(A,Q,e,F8)`, all five equations are homogeneous and linear in

```text
(r,f,F9,F11,F13,d5,d7,d9,d11,d13).
```

There are

```text
24 raw variables,
25 primitive variables,
40 scalar coefficient equations.                          (10)
```

Therefore the extended solution space has dimension at least
`49-40=9`.  Projection to the 24 raw variables is injective: if all raw
variables vanish, then every `T5(d_n)` vanishes, and the zero-kernel result
above forces every `d_n=0`.  Consequently:

```text
dim{legal raw odd tails satisfying q5,...,q13} >= 9     (11)
```

for every fixed legal even prefix.  This is a universal dimension theorem,
not a generic-fixture inference.  The all-zero odd tail is the most obvious
section, but `(11)` shows that nonzero tails necessarily remain as well.

For the two exact fixtures

```text
A=X^4-1,
A=X^4+X+1,
```

with unrelated dense legal choices of `Q,e,F8`, the complete matrices have

```text
40 rows, 49 columns, rank 40, nullity 9.                (12)
```

This proves exact dimension nine only on those fixtures.  Rank may drop on
special even prefixes, which would enlarge rather than eliminate the
survivor.

## 6. Even gates add no constraints

Let `v_i` be the guaranteed `A`-valuation of `F_i`.  From `(2)`, the
common-root theorem, and raw polynomiality,

```text
v2=3, v4=2, v5>=2, v6>=1, v7>=1, v_i>=0 for i>=8,
F1=F3=0.                                               (13)
```

Consider a binomial monomial contributing to an even `q_n`.  If its `r`
positive-weight factors have indices `i_1,...,i_r` summing to `n`, its
total `A`-exponent after the `F0=A^4` normalization is

```text
E=(n+2)/2-4r+sum_j v_(i_j)
  =(n+2)/2-sum_j delta_(i_j),
delta_i=4-v_i.                                        (14)
```

Every allowed index in `(13)` satisfies `2 delta_i<=i`: this is equality
at `i=2,4,6`, strict at `i=5,7`, and follows from `i>=8` for every later
raw polynomial.  Hence

```text
E >= (n+2)/2-(sum_j i_j)/2 = 1.                       (15)
```

Every monomial of every even `q_n` is therefore in `A K[X]`.  In
characteristic zero its polynomial one-form has a polynomial primitive.
Thus the even gates are automatic on this branch and add no constraints.

The checker independently reconstructs the first nontrivial checksum

```text
q8=A(F8/4-Qe/2^18-Q^4/2^23),                          (16)
```

which displays `(15)` directly.

## 7. Licensing, remaining work, and scope

The five gates consume later determinant rows:

```text
q5: D27,   q7: D29,   q9: D31,   q11: D33,   q13: D35.
```

They are full-system consequences and cannot be imported into the D22
endpoint packet by itself.  Conversely, once licensed, the even gates need
no separate solve by Section 6.

The sharp next discriminator is q15: there is no raw `F15` slot, so it is
the first odd exactness condition in this tail with no newest raw odd
coefficient.  It should be composed with the four-root endpoint face and
half-step conditions, not treated as though q5--q13 had already emptied the
branch.

Nothing here proves q15 exactness, endpoint compatibility, emptiness of the
lambda-zero branch, a Keller theorem, or JC2.

## 8. Frozen verifier

```text
cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_odd_gate_tail_20260828/
  verify_lambda0_odd_gate_tail.py
```

Replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_upper_endpoint_deep_q1_lambda0_odd_gate_tail_20260828/verify_lambda0_odd_gate_tail.py
```

Expected marker:

```text
PASS_EXACT_LAMBDA0_ODD_GATE_TAIL
```

The verifier uses only Python standard-library exact rational arithmetic.
It pins but does not import the producer artifacts, reconstructs `(1)` in a
sparse symbolic Laurent ring, checks `(16)`, enforces all five lower and
upper raw windows, rejects the q9 denominator mutation, and freezes the two
exact rank-40 fixtures.
