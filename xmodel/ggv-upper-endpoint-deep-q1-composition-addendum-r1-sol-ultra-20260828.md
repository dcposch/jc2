# Repaired full-system q1 composition: window obstruction and the D25 `q3` collapse

Date: 2026-08-28  
Status: **R1 REPAIR — RAW-GAUGE CLAIM REFUTED; D25/`q3` DETERMINES `U` ON BOTH q1 BRANCHES; NEITHER BRANCH YET EMPTY**

Supersedes:

```text
xmodel/ggv-upper-endpoint-deep-q1-composition-addendum-sol-ultra-20260828.md
```

The predecessor's Section 3 claim that a constant source translation
preserves every authoritative raw window is false.  Its formal determinant
covariance is correct, but lower raw-support bounds obstruct the translation.
Accordingly, this r1 report retracts the claimed equivalence of the
`lambda=0` and `lambda!=0` q1 branches.

This repair also independently audits and agrees with the frozen coordinator
`q3` composition:

```text
xmodel/ggv-upper-endpoint-deep-q1-q3-composition-sol-ultra-20260828.md
SHA256 6958c3986022e28484ea1a0a15a0b09a562dbd94cc2154ade4fe6dbc35000715
```

The frozen report is used only as a pinned comparison target; the r1 checker
reconstructs the complete `q3` numerator, primitive equation, D12 reduction,
and constants independently.

## 1. Repaired verdict

After the licensed D23/q1 gate, the active deep component still has the exact
split

```text
R0=lambda A,
V0=3lambda A A',
S=3lambda A'.                                          (Q1)
```

The two branches must be treated separately:

- `lambda=0`: `S=0` at all four roots.  The earlier common-root theorem and
  square-face tangent calculation remain valid on the exact-`D=0`,
  active-`c2` branch.  More strongly, once D25 licenses `q3`, the reviewed
  D12 lift `A|U` and the `q3` exactness equation force `U=0`.  Thus this
  branch is compressed by one entire polynomial, but is not proved empty.
- `lambda!=0`: `S=3lambda A'` is a unit at every simple root of `A`.  Its
  normalized leading face is the same fourth power at all four roots, but
  no legal raw-window gauge to `S=0` is known.  The complete D25 `q3` gate
  nevertheless determines `U` explicitly from `lambda` and `Q`; this remains
  a distinct unit-root branch.

The literal `S=1` homogeneous family remains non-q1 and D22-only.  Nothing
in this r1 pass promotes it to a D23 or full-system survivor.

## 2. What failed in the translation argument

Put `a=3lambda/4`.  The identities

```text
F1=a F0',
G1=a G0'
```

are correct, and formal precomposition

```text
tau_a(P)(X,t)=P(X-a t,t)
```

kills both weight-one coefficients.  It is also an exact symmetry of

```text
E(F,G)=F_X(12-t partial_t)G+(t partial_t-8)F G_X
```

and fixes the target `t^22`.

The error was checking only the upper degree inequality.  The exact
coefficient transport is

```text
(tau_a P)_n=sum_(k=0,...,n) (-a)^k P_(n-k)^(k)/k!.
```

The authoritative windows have lower as well as upper bounds.  In
particular,

```text
F8 allows X^0,...,X^8,       F9 allows only X^1,...,X^7,
G12 allows X^0,...,X^12,     G13 allows only X^1,...,X^11.
```

The legal mutations `F8=X` and `G12=X` produce

```text
(tau_a F)_9[X^0]=-a,
(tau_a G)_13[X^0]=-a,
```

in forbidden slots.  Hence the formal symmetry is not an automorphism of
the finite raw alphabet.  It remains possible that the determinant solution
locus forces every forbidden shear tail to cancel, but no such theorem is
available and r1 does not assume it.

## 3. The two q1 root faces after repair

The derivation of `(Q1)` is unchanged: modulo `A`, q1 gives
`A'R0=0`; squarefreeness gives `A|R0`; and `deg R0<=4` gives
`R0=lambda A`.

At a simple root `alpha`, put `z=t/A`.  The active lift gives

```text
A^-4 F(X,Az) -> (1+S(alpha)z/4)^4.
```

For `lambda!=0`, normalize `w=A'(alpha)z`.  Since
`S(alpha)=3lambda A'(alpha)`, all four roots have the universal face

```text
(1+3lambda w/4)^4.                                    (UF)
```

This is a valid root-local normalization because `A'(alpha)!=0`; it is not
a global raw-window source change.  The direct successor should exploit
`(UF)` while keeping all lower window floors.

For `lambda=0`, every root is a common root of `A,S`.  On exact `D=0`, the
previous Newton theorem still gives

```text
A|P1,
A|F7,
```

and the even face

```text
p_alpha(z)=(1-Q(alpha)z/16)^2
             +e1(alpha)z^3/2048+F8(alpha)z^4.
```

The exact 20-equation square-face linearization also remains correct at this
scope:

```text
rank=13,
endpoint-augmented rank=14.
```

That is a genuine one-point tangent obstruction for the leading D14--D22
face system.  It does not compare the two lambda branches and is superseded
for the full D25 system by the theorem below.

## 4. D25 licensing of `q3`

For an endpoint target

```text
E=t^22+O(t^N),
```

the reviewed tower licenses `q_n dX` exact precisely when `n+22<N`.
Consequently:

```text
D23=0 licenses q1,
D24=0 licenses q2,
D25=0 licenses q3.                                    (LIC)
```

Thus the theorem in the next section is a D25/full-system consequence.  It
must not be imported into a D22-only or D23-only endpoint packet.

The reviewed all-order coefficient formula is

```text
q_n = 2/(n+2) [t^n] F^((n+2)/8).
```

At `n=3` this is equivalently

```text
q3=p^5[F3/(4H^2)-3F1F2/(32H^4)+11F1^3/(512H^6)],
p^4=H.                                                 (q3)
```

## 5. Exact D25 collapse on `lambda=0`

Assume:

1. characteristic zero;
2. `A` is a squarefree quartic;
3. the active `c2!=0`, exact-`D=0` successor through the reviewed D12 lifts;
4. `lambda=0`, so `S=V0=F1=0`;
5. D23, D24, and D25 are imposed, so `(LIC)` licenses exactness of `q3 dX`;
6. the authoritative raw degree bounds, in particular `deg U<=5`.

On branch P, `H=A^2`, `p^2=+A` or `p^2=-A`, and

```text
F3=A^2U/8.
```

Formula `(q3)` reduces on either twist to

```text
q3=p U/32,                                             (Q3a)
```

because `p^4=A^2`.  The logarithmic derivative is the same on both twists:

```text
p'/p=A'/(2A).
```

An exact odd differential `q3 dX` has an odd primitive `c p`; the even
primitive component is constant.  Therefore `(Q3a)` is exact if and only if

```text
c'+A'c/(2A)=U/32,

4A^2 c'+2AA'c=A^2U/8.                                (Q3b)
```

Here `c` is initially rational.  It has no finite poles:

- away from `A=0`, a pole of `c` makes `c'` one order more singular than
  every other term;
- at a simple root of `A`, a pole of integer order `m<0` has leading
  coefficient `m+1/2`, which never vanishes.

Thus `c` is polynomial.  Cancel one `A` in `(Q3b)`:

```text
4A c'+2A'c=A U/8.                                     (Q3c)
```

Modulo `A`, squarefreeness gives `A|c`.  Write `c=Ar`; then

```text
6A'r+4Ar'=U/8.                                        (Q3d)
```

The reviewed D12 repair gives `A|L`; with `S=0`, `L=4U`, so

```text
A|U.                                                   (D12U)
```

Reducing `(Q3d)` modulo `A` now gives `A|r`.  Hence

```text
A^2|c.                                                 (Q3e)
```

Finally, if `c` is nonzero of degree `d`, the left side of `(Q3c)` has
degree `d+3` and leading coefficient `4(d+2)lc(c)`, while the right side has
degree at most nine.  Thus `deg c<=6`.  Since `deg A^2=8`, `(Q3e)` forces

```text
c=0,
U=0.                                                   (Q3zero)
```

This is a universal full-system collapse on the `lambda=0`, exact-`D=0`
branch once D25 is imposed.  It is not a contradiction: the square
homogeneous seed already has `U=0`, so further endpoint or later-row work is
still required.

### Load-bearing D12 mutation

The D12 lift is essential.  Without `A|U`, take

```text
c=A,
U=48A'.
```

Then `deg U=3` is legal and `(Q3b)` holds exactly, but `A` does not divide
`U`.  Thus `q3` alone does not force zero; the theorem is genuinely the
composition `D12U + D25/q3`.

## 6. Complete D25 `q3` composition for arbitrary `lambda`

The same calculation extends without setting `S=0`.  On the active q1
component put

```text
S=3lambda A',
Z=(S^2-AQ)/2.
```

Substitution of the complete reviewed formula `(q3)` gives

```text
q3=N/(512p),
N=S^3+A(16U-2SQ),                                     (GN)
```

on the `p^2=A` twist; the other twist changes only an irrelevant overall
sign.  After scaling the primitive by a nonzero constant, exactness is
equivalent to a rational `C` satisfying

```text
2A C'+A'C=N.                                          (GC)
```

The same local pole argument makes `C` polynomial.  Since `deg N<=9`, the
leading coefficient of the left side is `2(d+2)lc(C)` for `deg C=d`, so
`deg C<=6`.  Reducing `(GC)` modulo `A` gives

```text
C=27lambda^3(A')^2+A r,              deg r<=2.         (Cr)
```

Substitution in `(GC)` cancels the `S^3` term and yields

```text
16U=2SQ+108lambda^3 A'A''+3A'r+2Ar'.                  (Ur)
```

Now impose the reviewed D12 lift

```text
A | L,                     L=QS+4U.
```

Reduction of `(Ur)` modulo `A` gives a degree-at-most-two polynomial
divisible by the quartic `A`, hence the literal equality

```text
r=-6lambda Q-36lambda^3 A''.                          (rfix)
```

Substitution back into `(Ur)` gives the exact universal collapse

```text
U=-(3lambda/4)(A'Q+AQ')-(9/2)lambda^3 A A''',         (Ufix)
L=-3lambda A(Q'+6lambda^2 A''').                      (Lfix)
```

All constants in `(GN)`--`(Lfix)` were independently expanded in the r1
checker.  At `lambda=0`, `(Ufix)` specializes to `U=0`, agreeing with the
separate double-divisibility proof in Section 5.

This is a real compression, not an exclusion: on `lambda!=0` it removes the
polynomial `U` as an independent variable, while on `lambda=0` it restricts
the even-face successor to `S=U=0`.

## 7. Remaining branches and next discriminators

After the D25 theorem, the full-system active q1 problem has two honest
pieces:

```text
lambda=0:   S=U=0, with the finite even-face system still active;
lambda!=0:  S=3lambda A', with S(alpha)!=0 at every A-root and U given by (Ufix).
```

The clean next choices are:

1. on `lambda=0`, append `U=0` and compile the licensed triangular odd gates
   `q5,q7,...` against the finite four-root system.  Already
   `F1=F3=0`, `F5=A P1/256=A^2r_5/256`, so the Lagrange formula gives the
   exact first successor `q5=F5/(4p)=p^3r_5/1024`; the stronger proposed
   restrictions from `q5,q7,q9` remain provisional until separately frozen;
2. derive the direct unit-`S` Newton successor from the universal face
   `(UF)` after substituting `(Ufix)`, retaining the exact lower windows; or
3. prove, rather than assume, that all forbidden translation tails vanish
   on the determinant solution locus, which would restore the formal shear
   as a solution-locus map.

The direct-face routes are safer.  The next row should consume `(Ufix)` as a
proved substitution, not carry `U` as a free polynomial.

## 8. Reproducibility and scope

R1 checker:

```text
cases/ggv_8_28_upper_endpoint_deep_q1_composition_r1_20260828/
  verify_deep_q1_composition_r1.py
```

Replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B \
  cases/ggv_8_28_upper_endpoint_deep_q1_composition_r1_20260828/verify_deep_q1_composition_r1.py
```

Expected marker:

```text
PASS_EXACT_DEEP_Q1_COMPOSITION_R1
```

The checker pins the preceding Newton packet, the r0 face-rank code, the
independent translation-gauge negative audit, and the frozen coordinator
`q3` report.  It reconstructs both
forbidden lower-window mutations, retains only the honest `lambda=0` face
rank, verifies every constant in `(Q3a)`--`(Q3d)` and `(GN)`--`(Lfix)`,
proves exact full column rank for the degree-bounded `c,U` system at
`A=X^4-1`, and verifies the `c=A,U=48A'` mutation.

No claim is made that D1--D22 licenses q1 or q3, that the two lambda branches
are raw-gauge equivalent, that `lambda!=0` is empty, or that JC2 is proved.
