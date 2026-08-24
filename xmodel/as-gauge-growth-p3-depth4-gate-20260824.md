# AS-GAUGE-GROWTH at p=3 through depth four

**Producer verdict: EXACT EQUAL-CAP MINIMA 3,5,7 AT p=3 THROUGH DEPTH
FOUR; THE COTANGENT-SLOPE LAW SURVIVES THIS FINITE TEST ONLY.**

- Snapshot: 2026-08-24
- Charged bank: 1e4480c14f2ab9c4145eb6f6c74f0ac348baf76a
- Frozen input: confirmed bounded polar-conductor producer and hostile review
- Exact engine: Python with SymPy 1.14.0 over integers and F_3
- Support grammar: total-degree simplices only
- Required canonical different-model review: not yet run

**Verdict.** For the frozen equal-cap systems B_(3,n)(D,D), the exact
minimum total-degree caps at depths n=2,3,4 are respectively

~~~text
3, 5, 7.
~~~

Thus no depth-four survivor occurs below seven. The proposed formula
(n-1)(p-1)+1 survives this first unknown test, but nothing here proves it
at depth five or in general. The depth-seven point is the cotangent
truncation, not a polynomial lift.

No p=109, AWS, exponent rectangle, no-lift conclusion, A_infinity
identification, or JC inference is used.

## 1. Exact gauge elimination

For any odd prime p put

~~~text
g(T)=T-T^p,                 D(T)=1-pT^(p-1),
C_p=(g,y/D).
~~~

For a hypothetical polynomial depth-n map F=(P,Q) and its identity-branch
gauge Phi_F=(A,B), the confirmed orientation is

~~~text
C_p o Phi_F=F.
~~~

Coordinate comparison gives, without an ansatz,

~~~text
A-A^p=P,                    B=Q D(A).                  (1)
~~~

The derivative of T-T^p-P at an identity-branch approximation is
1-pT^(p-1), a unit. Hensel gives a unique A congruent to x modulo p. Then B is
forced by (1). Conversely,

~~~text
C_p(A,QD(A))=(P,Q)
~~~

exactly in the Tate algebra. Differentiating P=A-A^p gives
dP=D(A)dA, and

~~~text
det J(A,QD(A))
 =D(A) det(dA,dQ)
 =det J(P,Q);                                           (2)
~~~

the term QD'(A)dA wedges to zero with dA.

At finite depth n, write

~~~text
S_(p,n)(T)=sum_(j<n)p^jT^(j(p-1)).
~~~

Since

~~~text
D(A)S_(p,n)(A)=1-p^n A^(n(p-1)),
~~~

(1) is an exact bijection between the original bounded-gauge points and
the following F-only points:

~~~text
deg(P),deg(Q)<=D,
F=(P,Q)==(x-x^p,y) mod p,
det J(F)=1 mod p^n,
deg(A_n(P)),deg(QD(A_n(P)))<=D,                        (3)
~~~

where A_n(P) is the unique identity-branch root of A-A^p=P modulo p^n.
The last two inequalities are essential: eliminating the gauge and then
forgetting its cap would define a different system. In the coefficient
proof below, A and B are reintroduced only as the canonical digit
coordinates determined by F, not as independent choices.

All remaining calculations specialize to p=3.

## 2. Universal depth-four expansion, including nonlinear carries

Write the unique gauge modulo 81 as

~~~text
A=x+3a+9c+27e,            B=y+3b+9d+27f,              (4)
~~~

where every digit lies on the total-degree simplex of radius D. Direct
integer expansion gives

~~~text
A-A^3 =
 x-x^3
 +3a
 +9(c-x^2a)
 +27(e-x^2c-xa^2-a^3)                    mod 81,       (5)

B S_4(A) =
 y
 +3(b+x^2y)
 +9(d+x^2b+2xay+x^4y)
 +27(f+x^2d+2xab+x^4b+2xcy
       +a^2y+x^3ay+x^6y)                 mod 81.       (6)
~~~

For the source determinant, put

~~~text
L1=a_x+b_y,
L2=c_x+d_y+{a,b},
L3=e_x+f_y+{a,d}+{c,b},
{u,v}=u_xv_y-u_yv_x.
~~~

Then

~~~text
det J(A,B)=1+3L1+9L2+27L3 mod 81.                     (7)
~~~

The replay verifies (5)--(7) as universal polynomial congruences. In
particular the a^2, a^3, ab, mixed-bracket, and divided-divergence carries
are retained.

## 3. Depth two has exact minimum three

Every F reduces to (x-x^3,y), so no equal cap D<3 is possible. At D=3,
take the identity gauge:

~~~text
F=C_(3,2)=(x-x^3, y(1+3x^2)) mod 9.
~~~

Its determinant is one and both coordinates have degree at most three.
Hence min D at depth two is exactly three.

## 4. Depth three has exact minimum five

Modulo 27 only the first digits a,b matter to the over-cap rows:

~~~text
A-A^3=x-x^3+3a+9(c-x^2a),

B S_3(A)=y+3(b+x^2y)
 +9(d+x^2b-xay+x^4y),                                  (8)
~~~

where 2=-1 in F_3. The determinant first digit is

~~~text
a_x+b_y=0.                                             (9)
~~~

For D<=4, the first-coordinate cap in (8) forces deg(a)<=D-2<=2.
The coefficient of x^2 in (9) then forces

~~~text
[x^2y]b=0.
~~~

But the forbidden x^4y coefficient in the second line of (8) is

~~~text
[x^2y]b - [x^3]a + 1 = 1.                             (10)
~~~

Thus D=3 and D=4 are empty. The replay independently reconstructs the
entire affine first-digit systems from exact integer composition:

| D | variables | coefficient rank | augmented rank | verdict |
|---:|---:|---:|---:|---|
| 3 | 20 | 15 | 16 | empty |
| 4 | 30 | 21 | 22 | empty |
| 5 | 42 | 28 | 28 | first digit consistent |

At D=5 the identity gauge gives the positive cotangent control

~~~text
C_(3,3)=(x-x^3,y(1+3x^2+9x^4)) mod 27.
~~~

Therefore the exact depth-three minimum is five, not merely the older
statement that cap three fails.

## 5. Depth four: D=5 and D=6 are empty

It is enough to treat D=5,6; every D<=4 already dies on reduction to depth
three.

### 5.1 Forced degree bounds

The depth-three first-coordinate cap in (5) first gives

~~~text
deg(a)<=D-2.
~~~

For D=6, the homogeneous degree-12 part of the next digit is the cube of
the degree-four part of a. Frobenius is injective over F_3, so that part
vanishes. The remaining homogeneous degree-nine part is the cube of the
degree-three part, so it also vanishes. For D=5 the same degree-nine
argument starts immediately. Hence, in both cases,

~~~text
deg(a)<=2.                                             (11)
~~~

Now the depth-three second-coordinate cap in (6) forces

~~~text
deg(b)<=3 for D=5,             deg(b)<=4 for D=6.      (12)
~~~

The x^7 coefficient of the first-coordinate 27-digit in (5), together
with (11), gives

~~~text
c_[x^5]=0.                                             (13)
~~~

Finally the x^2 coefficient of (9) gives

~~~text
a_[x^3]=b_[x^2y]=0.                                   (14)
~~~

### 5.2 The determinant row cannot cancel x^6y

Let

~~~text
U=[x^5y](ab),                 K=[x^4]{a,b}.
~~~

Because of (11)--(12), only the top products contribute:

~~~text
U=a_[x^2] b_[x^3y]+a_[xy] b_[x^4],

K=2a_[x^2] b_[x^3y]-4a_[xy] b_[x^4]
 =-U in F_3.                                           (15)
~~~

For D=5, both displayed top b-coefficients are outside deg(b)<=3 and are
read as zero; the same identity then holds trivially. For D=6 they are the
only possible top coefficients.

The coefficient of x^4 in L1 is exactly zero over the integers: producing
it would require x^5 in a or x^4y in b, both excluded by (11)--(12).
Therefore the divided carry L1/3 contributes nothing to this row. The
x^4 coefficient of determinant one modulo 27 is

~~~text
5c_[x^5]+d_[x^4y]+K=0.
~~~

Read x^6y in the 27-digit of (6). Equations (11) and (14) remove all terms
except

~~~text
d_[x^4y]+2U+2c_[x^5]+1.
~~~

Subtract the determinant row and use (14)--(15):

~~~text
(Q row)-(determinant row)-b_[x^2y]
 =2U-K+(2-5)c_[x^5]+1
 =1 in F_3.                                            (17)
~~~

This is an explicit unit certificate. Notice that the c_[x^5] terms cancel
modulo three, so (13) is an independently checked cap row rather than a
hidden necessity of the final contradiction.

Thus the coefficient is 27 times a unit modulo 81. It cannot be removed
by e or f, whose supports have degree at most D. This excludes both D=5
and D=6, with every nonlinear carry and the sole relevant determinant
carry accounted for.

## 6. Depth-four positive control and exact minimum

At D=7 the identity gauge gives

~~~text
C_(3,4)=
(x-x^3, y(1+3x^2+9x^4+27x^6)) mod 81.                (18)
~~~

The geometric-series identity gives determinant one modulo 81. Its second
coordinate has exact degree seven because 27 is nonzero modulo 81.
Together with Sections 3--5:

~~~text
min D for B_(3,2)(D,D) = 3,
min D for B_(3,3)(D,D) = 5,
min D for B_(3,4)(D,D) = 7.                           (19)
~~~

This is finite quantitative evidence for the proposed slope, not a
general growth theorem. The survivor (18) is a finite cotangent
truncation, not a lift to all depths.

## 7. Deterministic replay and scope

Run without network:

~~~text
uv run --offline --no-project --with sympy==1.14.0 python \
  cases/as_gauge_growth_p3_depth4_20260824/replay.py

uv run --offline --no-project --with sympy==1.14.0 python \
  cases/as_gauge_growth_p3_depth4_20260824/independent_check.py
~~~

The replay:

1. verifies the universal mod-81 formulas (5)--(7);
2. rebuilds the complete depth-three affine systems at D=3,4,5 from exact
   integer compositions on total-degree simplices;
3. checks the symbolic coefficient identity (15)--(17) for D=5,6; and
4. verifies the cotangent controls and their exact degrees at n=2,3,4.

It terminates with PASS-AS-GAUGE-GROWTH-P3-DEPTH4 and explicit markers
refusing a polynomial-lift or JC inference.

The second script is a separately written same-model internal audit. It
does not import the producer, independently extracts the generic simplex
coefficients, and enumerates all 81 four-slot top tuples for each of D=5
and D=6; every tuple leaves x^6y digit one. At D=5 the two displayed top
b-slots are absent, so these are nine distinct effective assignments
repeated across the irrelevant slots; at D=6 all 81 are distinct. It terminates with
PASS-INDEPENDENT-AS-GROWTH-HOSTILE-CHECK. This is an internal negative
control, not the required canonical different-model hostile review.

Frozen inputs, read without modification:

~~~text
2baa7a7a17454e4b30a974841071104283917c424d208f03e3d5e12b8a12dc0b  xmodel/as109-bounded-polar-conductor-gate-20260824.md
bda4dda7d24d36bf75b6c55b566f708ee300c80aeb3344c4bb724bfc7e7787fa  xmodel/as109-bounded-polar-conductor-review-grok-20260824.md
aa07a878b41adfbe9e07beaa48aa793562fb49228ffae8982aa8773f600df4e2  cases/as109_bounded_polar_conductor_20260824/FREEZE.sha256
~~~

No outcome of this gate proves the formula at n>=5, constructs or excludes
an all-depth polynomial lift, runs p=109, identifies the exterior polar
divisor with A_infinity, or implies anything about JC2.
