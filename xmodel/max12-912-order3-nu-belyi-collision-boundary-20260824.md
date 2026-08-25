# `(9,12)` order-three `nu!=0` full B/W absorption boundary

Date: `2026-08-24`  
Status: **PRODUCER-EXACT / HOSTILE DIFFERENT-MODEL REVIEW REQUIRED**  
Verdict: on the reviewed order-three `k=mu=0`, `nu!=0` landing, no actual
Keller trajectory survives when the complete ramification divisor of the
quadratic spectral Wronskian `B` is absorbed by `W=g^3-f^4=0`.

## 1. Scope and exact input

Work over `K=C(x)` and the nontrivial order-three Kummer field
`L=K(u)`, with `u^3=h`. The reviewed maximum-twelve preflight and Faber
landing give monic depressed polynomials `f,g in L[z]` of degrees `9,12`.
On the invariant leaf considered here,

```text
k=mu=0,                r6=nu in C*,
r8'=j/(9u),             j != 0.                         (1.1)
```

No normalization of `nu` is required below; setting `nu=1` is a harmless
constant scaling for the coefficient-fibre computation.

Put

```text
W=g^3-f^4,       beta=g^3/f^4,
B=3*f*g_z-4*g*f_z.
```

Writing `f=w^9`, `g=w^12-T`, the first tail is
`T=nu*w^-6+r8*w^-8+...`. Hence

```text
W=-3*w^24*T+3*w^12*T^2-T^3,
deg_z(W)=18,          [z^18]W=-3*nu.                    (1.2)
```

The top exponents contributed by the three displayed terms are respectively
`18,0,-18`; thus (1.2) has no hidden leading cancellation.

The exact tail-to-Wronskian identity gives, on this leaf,

```text
B=18*nu*F3'+60*r8
 =54*nu*z^2+18*nu*p+60*r8,                              (1.3)
F3=z^3+pz+q.
```

Thus `B` has degree exactly two and

```text
disc_z(B)=-1296*nu*(3*nu*p+10*r8).                      (1.4)
```

The theorem below uses only (1.1)--(1.4), the actual Keller equation, and
fixed-passport Hurwitz finiteness. It does not consume a component
decomposition or either Taylor boundary.

## 2. Squarefree/coprime firewall

The original Keller equation in the depressed coordinate is

```text
D=f_x*g_z-f_z*g_x=j/u in L*.                            (2.1)
```

If a nonconstant `d` divides both `f` and `g`, then `d` divides every term of
`D`, contradicting (2.1). If `d^2` divides `f`, then `d` divides both `f_x`
and `f_z`, again contradicting (2.1); the same argument applies to `g`.
Consequently, on every actual trajectory,

```text
gcd(f,g)=1,             f and g are squarefree.         (2.2)
```

In particular, `B` cannot vanish at a root of `f` or `g`: at a root of `f`,
`B=-4*g*f_z` is nonzero, and at a root of `g`, `B=3*f*g_z` is nonzero.
Coefficient-fibre components violating (2.2) are algebraic artifacts and
cannot be imported into a trajectory claim.

## 3. Exact full-absorption passports

Direct differentiation gives

```text
beta_z=g^2*B/f^5.                                       (3.1)
```

By (1.2), infinity is a point of ramification index `18` over `beta=1`.
The simple roots of `g` give `3^12` over `0`, and the simple roots of `f`
give `4^9` over infinity.

There are exactly two ways for the complete degree-two ramification divisor
of `B` to be absorbed by `W=0`.

1. `disc(B)!=0` and both roots of `B` lie in `W` (equivalently, `B|W`).
   At each root, (3.1) has a simple zero, so `beta-1` has multiplicity
   exactly two. The fibre over `1` is

   ```text
   (18,2,2,1^14).                                      (3.2)
   ```

2. `disc(B)=0` and the double root of `B` lies in `W`. At that root,
   (3.1) has order two, so `beta-1` has multiplicity exactly three. The
   fibre over `1` is

   ```text
   (18,3,1^15).                                        (3.3)
   ```

Every other finite root of `W` is simple: a repeated root of `W`, away from
`f*g=0`, would make `beta_z=0` and hence would be a root of `B`. Therefore in
both cases `beta` has only the three branch values `0,1,infinity`.

The Riemann--Hurwitz ledger is sharp in either case:

```text
12*(3-1)+9*(4-1)+[(18-1)+2*(2-1)] = 70,
12*(3-1)+9*(4-1)+[(18-1)+(3-1)]   = 70,
2*36-2                                      = 70.       (3.4)
```

## 4. Isotrivial scaling and contradiction

For either fixed passport (3.2) or (3.3), there are finitely many transitive
permutation triples in `S_36`. Hence the corresponding three-point maps are
isotrivial over `L`. This uses only fixed-passport Hurwitz finiteness, not a
unitree or equality-pair census.

The zero and pole divisors of `beta` recover the monic pair `(f,g)` uniquely.
The point of index `18` over `1` is unique, so every source identification
fixes infinity and is affine. Depression kills its translation part. After a
finite extension of `L`, choose a constant template `(F,G)` and write

```text
f(z)=lambda^-9*F(lambda*z),
g(z)=lambda^-12*G(lambda*z).                            (4.1)
```

If `W0=G^3-F^4` and `C18=[Z^18]W0 in C*`, then

```text
W(z)=lambda^-36*W0(lambda*z),
[z^18]W=C18*lambda^-18.                                (4.2)
```

Combining (1.2) and (4.2) gives

```text
C18*lambda^-18=-3*nu,
lambda^18=-C18/(3*nu) in C*.                           (4.3)
```

This is insensitive to a finite source-stabilizer twist: every choice of
`lambda` satisfies (4.3). Since `C` is algebraically closed, (4.3) forces
`lambda in C*`. Thus every coefficient of `f,g`, and in particular the
Laurent tail `r8`, is differential-constant. This contradicts the terminal
row in (1.1):

```text
9*r8'=j/u != 0.                                        (4.4)
```

Therefore neither full-absorption passport supports an actual Keller
trajectory.

## 5. Boundary route and scope firewall

The exact quadratic route is:

| `B` stratum | `W` collision | status here |
|---|---|---|
| two distinct roots | neither | retained |
| two distinct roots | exactly one | retained (four-point family) |
| two distinct roots | both | **excluded by (3.2)--(4.4)** |
| double root | root not in `W` | retained (four-point family) |
| double root | root in `W` | **excluded by (3.3)--(4.4)** |

Collision of the two distinct non-`1` critical values is also retained; it
does not make (3.2) unless both critical points themselves lie over `1`.

**Producer conclusion.** Complete absorption of the quadratic `B`
ramification by `W=0` is impossible on an actual `nu!=0` order-three Keller
trajectory.

**Not concluded:** exclusion of the generic `nu`-loaded fibre, the one-root
collision, the double-`B` four-point family, equal non-`1` critical values,
Taylor-boundary compatibility, the order-one core, all `(9,12)`,
maximum-twelve automorphy, a counterexample, or JC2.

## 6. Replay

Run:

```sh
python3 cases/max12_912_order3_nu_belyi_collision_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_belyi_collision_20260824/replay.json -
```

The replay checks (1.2), (1.4), both fibre partitions, both
Riemann--Hurwitz sums, and the scaling exponent in (4.2). Fixed-passport
finiteness and isotriviality are proof steps, not software outputs.
