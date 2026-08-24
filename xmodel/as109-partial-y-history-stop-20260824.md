# Partial-`y` history stop and first genuine frontier

**Verdict: `SOURCE-AUDITED HISTORY STOP; ALL MAXIMUM ACTUAL y-DEGREE
<=8 IS CLASSICAL; FIRST FUNDAMENTAL REMAINDER IS (6,9) WITH 3|H`.**

- Snapshot: `2026-08-24`
- Charged bank: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`
- Field: arbitrary characteristic zero, by scalar extension/descent from the
  cited complex theorems
- Degree notion in the coverage statement: actual partial `y`-degree
- Generic coefficient or support search: none
- AWS: none
- AS109 specialization: an exact conditional degree implication and a
  first-row negative control; no lift, counterexample, or JC2 inference

The proposed consecutive-degree program must stop for history.  Every
positive pair `(m,m+1)` is already covered by a large triangular source
shear followed by the repaired Appelgate--Onishi prime-total-gcd theorem.
This includes `(6,7)`, whether the common leading core is constant or not.

The same argument is stronger.  It covers every partial-degree pair whose
gcd is at most two.  Together with equal-degree target `GL_2` reduction and
divisible-degree target shears, it covers every characteristic-zero Keller
pair whose two actual `y`-degrees are at most eight.  Thus the campaign's
new cubic, quartic, quintic, and sextic calculations are potentially useful
alternative proofs and exact instruments, but they are not first
exclusions of those degree strata.  In particular the independently
confirmed `(4,6)` and `(5,6)` results do not establish a new degree
frontier.

At maximum degree nine the only fundamental residue is `(6,9)`, and only
when the degree `H` of its common leading core is divisible by three.  The
equal pair `(9,9)` is derivative because target `GL_2` can lower one
coordinate to `(6,9)`.  The bounded preflight below shows exactly why the
coprime weighted-boundary mechanism stops there: a two-dimensional family
of common cubic powers survives both leading boundaries and has zero
Jacobian.

This artifact is producer-checked and frozen for different-model hostile
review.  It does not edit or promote a canonical ledger.

## 1. Exact shear lemma

Let

```text
P=a_m(x)y^m+...+a_0(x),       Q=b_n(x)y^n+...+b_0(x),
```

be a Keller pair with `m,n>0`.  Put

```text
d=gcd(m,n),        m=d a,        n=d b,        gcd(a,b)=1.
```

The coefficient of `y^(m+n-1)` in the Jacobian is

```text
n a_m' b_n - m a_m b_n' = 0.                         (1.1)
```

After division by `d`, unique factorization in `k[x]` gives, after harmless
constant scaling and scalar extension if necessary,

```text
a_m=alpha h^a,       b_n=beta h^b,       alpha,beta in k*, h in k[x]. (1.2)
```

Indeed `(a_m^b/b_n^a)'=0`; prime valuations satisfy
`b v(a_m)=a v(b_n)`, and coprimality of `a,b` gives the displayed powers.
This also handles a constant nonzero `h`.  Write `H=deg(h)`, with `H=0`
in that case.

Let

```text
M=max_i deg_x(a_i), max_j deg_x(b_j)
```

and choose an integer `L>max(M,1)`.  Precompose the geometric Keller map by the
triangular source automorphism

```text
sigma_L(x,y)=(x,y+x^L).
```

Equivalently on the coordinate ring, apply `sigma_L` to both `P,Q`.  This
is the convention used in Moskowicz: `sigma_L(P)=P(x,y+x^L)`.  It preserves
the nonzero constant Jacobian and preserves automorphy in both directions.

For every `j<m`,

```text
deg(a_j(x)(y+x^L)^j)=deg_x(a_j)+Lj
                    < deg_x(a_m)+Lm,
```

because `L>M` is stronger than needed.  Within the `j=m` summand its unique
largest total-degree term is the leading `x`-term of `a_m` times `x^(Lm)`.
Thus there is no cross-row or internal cancellation, and similarly for
`Q`.  The exact transformed total degrees are

```text
deg sigma_L(P) = a(H+dL),
deg sigma_L(Q) = b(H+dL),
gcd(deg sigma_L(P),deg sigma_L(Q)) = H+dL.             (1.3)
```

Put `g=gcd(H,d)`, `H=g H0`, `d=g d0`.  Since
`gcd(H0,d0)=1`, Dirichlet gives arbitrarily large `L` for which

```text
H0+d0 L = p
```

is prime.  We may impose `L>max(M,1)` simultaneously.  Equation (1.3) then has
total-degree gcd `g p`.  Consequently:

```text
gcd(H,d)=1  => transformed total gcd is prime;
gcd(H,d)=2  => transformed total gcd is twice a prime. (1.4)
```

The published total-degree theorems cited below make the transformed pair,
and hence the original pair, an automorphism.  In particular `d<=2`
forces `g in {1,2}` for every `H`.  If `d=1`, including every consecutive
pair, one can simply choose the prime `H+L`; for `H=0` choose `L` itself
prime.  No nonconstant-leading-coefficient hypothesis is hidden here.

## 2. Primary-source audit and the clean citation chain

The mathematical chain is sound, but attribution must be precise.

1. **Magnus 1955 is the coprime-total-degree theorem, not the prime-gcd
   theorem.**  Its Theorem 2 treats total degrees `m,n>=2` with
   `gcd(m,n)=1`.  The official journal scan was read.  Nagata reproduces a
   proof on pp. 157--158 of the source below.
2. **Appelgate--Onishi 1985 must not be cited alone.**  Nagata explicitly
   says their article contains errors, then supplies a completion using his
   Theorem 3.1 and Abhyankar.  Nagata Theorem 7.3 states that prime
   `gcd(deg P,deg Q)` implies `k[P,Q]=k[x,y]`; it also gives the familiar
   consequence when one total degree is a product of two primes.  This is
   the clean primary source for the repaired theorem used when `g=1`.
3. **The `2p` theorem is sound, but not via Żołądek alone.**  Żołądek 2008
   states it, but Guccione--Guccione--Valqui identify a gap in Żołądek
   Lemma 4.10 (`I_2 subset (1/m) Gamma(f_2)` is asserted without proof).
   Their peer-reviewed 2017 paper independently proves that a
   counterexample cannot have total-degree gcd `2p` for any prime `p`.
   Use that paper for the `g=2` arrow in (1.4).  This is the clean fix to
   the source-risk issue; the gap must not be projected onto GGV's
   independent proof.
4. **Moskowicz arXiv:1810.08202v2, Theorem 2.7, is consistent with this
   derivation.**  With
   `A=gcd(deg_y P,deg_x a_m)` and
   `C=gcd(deg_y Q,deg_x b_n)`, it states that the pair is automorphic if
   either `A` or `C` belongs to `{1,4} union primes`.  Its proof applies the
   same large shear and Theorems 1.1--1.2.  In particular a coordinate of
   actual `y`-degree prime or four is already covered.  The constant-leading
   case uses `gcd(N,0)=N` and is explicitly handled in the paper.

Primary artifacts read and hashed during this audit:

| Source | Exact location / role | SHA-256 of downloaded primary artifact |
|---|---|---|
| Arne Magnus, *Math. Scand.* 3 (1955), 255--260, DOI `10.7146/math.scand.a-10443` | official journal PDF; coprime total degrees | `f8c95ebdb04076928d8e37d1cf862853bf05cbbd5f6a7cc2bf32fb0f90e800da` |
| Masayoshi Nagata, *Two-dimensional Jacobian Conjecture*, 1989 symposium record, pp. 153--172 | official Kyoto repository PDF; pp. 158, 169--170 / Theorem 7.3 repairs Appelgate--Onishi | `ea57f589536d97866155a81cd0c2177743ac9e1fe0ab6e8536cb71d00cae0bb7` |
| C. Valqui, J.A. Guccione, J.J. Guccione, *J. Algebra* 471 (2017), 13--74, DOI `10.1016/j.jalgebra.2016.08.039`, arXiv:1401.1784 | independent `gcd != 2p` theorem and explicit diagnosis of the Żołądek gap | arXiv source `e6a01769d1f017467c2cba2b1e425ed708da9b4ac917391399fb34f5ac0d86f0` |
| Vered Moskowicz, arXiv:1810.08202v2 | Theorems 1.1, 1.2, 2.7 and the exact shear bookkeeping | source `ca974bd7a3603262952c9a5751bc7466c71b2ed47693489e5991096846674419` |
| Henryk Żołądek, *Topology* 47 (2008), 431--469 | inspected only to delimit the gap; **not consumed** for `2p` | local official PDF `88d5a35414ad11ffc96e32551810ef773e88be2db12ce39478c964cb602149ad` |

The primary URLs are, respectively,
`https://journals.msp.org/mscand/article/download/2880/2879/2911`,
the Kyoto repository bitstream
`9ef8e868-5526-4830-b19f-543c0af09e7c`,
`https://export.arxiv.org/e-print/1401.1784`, and
`https://export.arxiv.org/e-print/1810.08202`.

The cited theorems are written over `C` or a characteristic-zero field.
For an arbitrary characteristic-zero coefficient field, pass to the
algebraic closure of the finitely generated coefficient subfield and embed
it in `C`.  Automorphy descends by faithful flatness (equivalently, the
polynomial inverse is unique).  Thus no algebraic-closure qualification is
missing from the campaign's field statement.

## 3. Exact coverage through maximum actual `y`-degree eight

Order an unordered pair as `0<=m<=n`.

- `m=0`: Moskowicz Proposition 2.1 gives the triangular form; incompatible
  alleged degree labels are empty.
- `gcd(m,n)<=2`: Section 1 applies for every common-core degree `H`.
- `m|n`: the leading UFD relation permits the polynomial target shear
  `Q -> Q-c P^(n/m)`, strictly lowering the larger actual degree.
- `m=n`: the leading-coefficient ratio is constant by (1.1), so a constant
  target `GL_2` operation strictly lowers one coordinate.

Lexicographic induction on `(max(m,n),m+n)` terminates.  The only pairs with
maximum at most eight not immediately in `gcd<=2` are equal pairs and
divisible pairs such as `(3,6)` and `(4,8)`.  They reduce by the last two
bullets.  Therefore

```text
deg_y(P),deg_y(Q) <= 8  =>  (P,Q) is an automorphism.  (3.1)
```

This covers all `45` unordered and all `81` ordered pairs.  It is wholly
independent of the campaign's bounded-degree coefficient/Pfaffian
calculations.

Here is the requested exact unordered coverage map through maximum seven;
ordered pairs are obtained by swapping coordinates.  In the table, `G`
means the universal prime/`2p` source-shear theorem (`gcd(m,n)<=2`), `D`
means a divisible-degree target shear, `E` means equal-degree target
`GL_2` reduction, and `Z` means the zero-coordinate triangular case.

| Maximum `n` | Pairs `(m,n)` and route |
|---:|---|
| `0` | `(0,0): Z` |
| `1` | `(0,1): Z`; `(1,1): E` |
| `2` | `(0,2): Z`; `(1,2): G`; `(2,2): E` |
| `3` | `(0,3): Z`; `(1,3): G`; `(2,3): G`; `(3,3): E` |
| `4` | `(0,4): Z`; `(1,4): G`; `(2,4): G`; `(3,4): G`; `(4,4): E` |
| `5` | `(0,5): Z`; `(1,5): G`; `(2,5): G`; `(3,5): G`; `(4,5): G`; `(5,5): E` |
| `6` | `(0,6): Z`; `(1,6): G`; `(2,6): G`; `(3,6): D`; `(4,6): G`; `(5,6): G`; `(6,6): E` |
| `7` | `(0,7): Z`; `(1,7)` through `(6,7): G`; `(7,7): E` |

Thus all `36` unordered and all `64` ordered pairs through maximum seven
are covered.  The stronger maximum-eight row adds `(0,8):Z`,
`(1,8):G`, `(2,8):G`, `(3,8):G`, `(4,8):D`, `(5,8):G`, `(6,8):G`,
`(7,8):G`, and `(8,8):E`.

For maximum nine the complete new row is:

| Pair | Exact route |
|---|---|
| `(0,9)` | zero-coordinate triangular/impossible label |
| `(1,9)` | gcd one shear |
| `(2,9)` | gcd one shear |
| `(3,9)` | divisible target shear |
| `(4,9)` | gcd one shear |
| `(5,9)` | gcd one shear |
| `(6,9)` | gcd three; closed if `3` does not divide `H`, unresolved by this theorem exactly if `3|H` |
| `(7,9)` | gcd one shear |
| `(8,9)` | gcd one shear |
| `(9,9)` | target `GL_2`; derivative dependence on `(6,9)` only |

For `(6,9)`, write `m=3*2`, `n=3*3`.  Equation (1.2) is

```text
a_6=alpha h^2,       b_9=beta h^3.                    (3.2)
```

The shear total degrees are `2(H+3L),3(H+3L)`.  If `3` does not divide
`H`, Dirichlet makes `H+3L` prime.  If `3|H`, it is always divisible by
three and Dirichlet only produces `3p`; no cited total-degree theorem covers
that class.  Moskowicz Theorem 2.7 says the same: its two invariants are
`2,3` in the first residue and `6,9` in the second.

## 4. Bounded exact `(6,9)` preflight and stop

**Registered question.**  Does the coprime weighted finite-map mechanism
used by the campaign's `(5,6)` calculation even have a zero-dimensional
leading boundary system at the first historical remainder `(6,9), 3|H`?

**Stop rule.**  Stop before deriving a full Pfaffian system if an exact
positive-dimensional common-power family simultaneously satisfies the
depressed degree pattern, the leading Jacobian equations, and both leading
`y=0` boundaries.  Such a family proves that the coprime common-factor lemma
and its finite-map certificate do not transfer; a generic coefficient
search would then attack the wrong representation.

The stop fires.  In homogeneous variables `(t,z)`, put

```text
K = z^3 + u t^2 z + v t^3,
F = K^2,
G = K^3.                                               (4.1)
```

Then `F,G` are monic of actual `z`-degrees `6,9`; the depressed
coefficients of `z^5,z^8` vanish.  Explicitly,

```text
F = z^6+2u t^2z^4+2v t^3z^3+u^2t^4z^2+2uvt^5z+v^2t^6,

G = z^9+3u t^2z^7+3v t^3z^6+3u^2t^4z^5+6uvt^5z^4
    +(u^3+3v^2)t^6z^3+3u^2v t^7z^2+3uv^2t^8z+v^3t^9.
```

The exact binary Jacobian is zero.  At the normalized `y=0` boundary
`z=r,t=1`, both equations are

```text
F(1,r)=(r^3+ur+v)^2=0,
G(1,r)=(r^3+ur+v)^3=0.                                (4.2)
```

Their ideal has dimension two in `Q[r,u,v]`.  This is not a single
degenerate point: it is the unavoidable `gcd(6,9)=3` common-cubic locus.
It lies in the aligned `z^8=0` branch, so it is not removed merely by the
cubic Kummer descent that kills a constant depression mismatch when the
leading core is not a cube.  Indeed, if `s^3=h` and the Kummer generator
acts by `s -> omega s`, then normalized `z,r` have weight one, `u` has
weight two, and `v` has weight zero modulo three.  Every term of
`K=z^3+u z+v` is invariant, so `(K^2,K^3)` and the root equation descend.

This does **not** construct a Keller pair: its Jacobian is zero, not a
nonzero constant.  It proves the registered negative statement only:

```text
the leading boundary/integral map is not finite on the (6,9) frontier;
the coprime binary common-factor lemma stops at a cubic, not a line.       (4.3)
```

The cheapest honest successor is therefore a transverse deformation gate,
not a generic normal-form enumeration: linearize the full depressed
`(6,9)` Jacobian system about `(K^2,K^3)`, quotient source/target gauges and
the tangent directions in `(u,v)`, impose the cubic Kummer descent weights,
and ask whether the nonzero constant row occurs in the resulting cokernel.
Stop that gate if the constant row survives the cokernel generically; only
if it dies should one integrate the full Pfaffian and both lower-weight
boundaries.

No `(4,7)`, `(5,7)`, `(6,7)`, or general consecutive computation should be
launched.  Those are history duplicates.

## 5. AS109-integral specialization: exact implication and first-row stop

This subsection separates the general characteristic-zero frontier above
from what it says about an exact AS109 lift.  Write the lifted coordinate
pair over `Z_109` as `(P,Q)`.  Its seed congruence is

```text
P = x-x^109 (mod 109),        Q = y (mod 109).          (5.1)
```

Consequently every coefficient of `y^i` in `P` for `i>=1`, and every
coefficient of `y^j` in `Q` for `j>=2`, is divisible by `109`.  This is a
statement about the coordinate pair itself, not just its correction terms.

Suppose a reduced maximum-nine pair has actual degrees `(6,9)`, and write

```text
P=a y^6+c y^5+...,             Q=b y^9+d y^8+....       (5.2)
```

The top row gives `a=alpha h^2`, `b=beta h^3` over `Q_109[x]`.  Scale the
common core so that `h` is primitive in `Z_109[x]`.  Gauss's lemma and
(5.1) then give the exact scalar-content bounds

```text
A=v_109(alpha)>=1,             B=v_109(beta)>=1,         (5.3)
```

while `C=v_109(content(c))>=1` and
`D=v_109(content(d))>=1` (with infinity for a zero coefficient).  There is
no top-row reason for `A` and `B` to be equal.

The first non-top Jacobian coefficient, that of `y^13`, is exactly

```text
8 a' d + 9 c' b - 6 a d' - 5 c b' = 0.                (5.4)
```

The first and third terms have valuation at least `A+D`, and the second
and fourth at least `B+C`.  Thus every term is already zero modulo
`109^2`; reduction modulo `109` (or `109^2`) cannot supply a contradiction.
This is not merely failure to find one.  The replay supplies the explicit
primitive-core control

```text
h=x^3+1,  alpha=beta=109,
P0=109 [h(y+x)^3]^2,           Q0=109 [h(y+x)^3]^3.     (5.5)
```

Here `c=6*109*h^2*x` and `d=9*109*h^3*x` are nonzero, both scalar
valuations in (5.3) are one, (5.4) vanishes identically, and the full
Jacobian is zero.  Therefore (5.5) is only a sharp integral valuation
control: it is neither a Keller pair nor congruent to the AS109 seed.
It rules out a *universal first-non-top-row valuation contradiction*, not a
later-row or seed-specific obstruction.

There is nevertheless an exact maximum-nine implication.  Consume the
campaign's separately reviewed residue-ball Hensel fact that every exact
AS109 lift is noninjective over `Q_109`.  Sections 1--3 then imply:

```text
If an exact AS109 lift has maximum actual y-degree exactly 9, then, after
an integral constant target GL_2 operation and possibly swapping the two
coordinates, its only possible nonautomorphic reduced degree pair is
(6,9), and its primitive common leading core satisfies 3 | deg(h).       (5.6)
```

For completeness, this does not silently assume that the raw pair is
`(6,9)`.  Every unequal `(m,9)` other than `m=6` is covered by the table in
Section 3.  For a raw `(9,9)` pair, the leading coefficients have constant
ratio.  Cancel the coefficient with larger `109`-adic content using the
one with smaller content.  The ratio used is in `Z_109`, so this is a
unipotent integral target operation; it preserves divisibility of all high
`y` coefficients, noninjectivity, and invertibility equivalence.  It
strictly lowers one degree to `(r,9)`.  If `r!=6`, that row is classical;
if `r=6`, Section 3 shows that `3|deg(h)` is necessary.  Thus (5.6) is a
target-equivalence statement, not a claim about the unreduced raw labels.

The same argument also strengthens the previously bounded AS109 floor:
an exact lift cannot have maximum actual `y`-degree at most eight, because
(3.1) would make it an automorphism and hence injective.  These are
conditional AS109 consequences of the reviewed Hensel result and the
source-audited field theorem; they do not construct a lift or infer JC2.

## 6. Deterministic replay

Run:

```text
python3 cases/as109_partial_y_history_stop_20260824/verify_coverage.py
Singular -q cases/as109_partial_y_history_stop_20260824/verify_69_cubic_power_stop.sing
```

Expected terminal lines:

```text
PASS-PARTIAL-Y-HISTORY-COVERAGE
consecutive_pairs=KNOWN_BY_PRIME-GCD-SHEAR
max_actual_y_degree_le_7=ALL_64_ORDERED_PAIRS_COVERED
max_actual_y_degree_le_8=ALL_81_ORDERED_PAIRS_COVERED
max9_fundamental_open=(6,9) with 3|H
max9_derivative_open=(9,9) via target-GL2 successor (6,9)

PASS-(6,9)-CUBIC-POWER-STOP
leading_boundary_dimension=2
finite_weighted_map=false
coprime_common-factor_lemma_transfers=false
as109_scalar_valuations_control=(1,1)
as109_first_nontop_valuation_contradiction=false
generic_search_run=false
aws_used=false
as109_lift_construction_or_exclusion=false
jc2_inference=false
```

The Python replay checks the integer formula, constant-core cases,
Dirichlet residue arithmetic on a broad finite regression grid, all 81
ordered pairs through degree eight, and the complete maximum-nine row.  The
Singular replay is the exact bounded negative control (4.1)--(4.3).  Neither
replay proves a literature theorem; the primary-source audit supplies those
inputs.

Hashes are frozen in
`cases/as109_partial_y_history_stop_20260824/FREEZE.sha256`.  No canonical
top-level file, pre-existing producer/review artifact, AWS resource, nested
repository, commit, or remote was edited.
