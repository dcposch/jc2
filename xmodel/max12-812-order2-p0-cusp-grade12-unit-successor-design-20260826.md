# `(8,12)` order two: `p=0` cusp grade-12 unit successor

Date: 2026-08-26

Status: **CORRECTION-AWARE HAND DERIVATION AND EXACT-SOURCE AWS DESIGN.  THE
GRADE-12 UNIT IS A PRODUCER CANDIDATE UNTIL THE COMPLETE FROZEN-TAIL REPLAY
PASSES.  NO ORDER-TWO OR `(8,12)` VERDICT.**

## 0. Exact scope and charged inputs

This is the disjoint successor to the eliminated odd sheet.  After the sharp
third-tail theorem has forced `M=0`, it treats the other reduced region of the
`p=0` half-weight special fibre,

```text
d=rs != 0,       k0 != 0,
```

in the source-typed exact-order-two, terminal `[6,2]` client.  The open called
`D(rs)` below always retains the inherited half-weight open `D(k0)`.  It is
disjoint from the promoted odd sheet `V(rs) intersect D(cs*k0)`.

The charged sources are the exact half-weight rows and review at SHAs
`eb2cd8036a0abf87a1ff7a58c116346b11973efc47f35f9cb76105a6ccd485af`
and `49744ab901f05ae6d8f0163fd195f3b0219e725f051c3aeebf31fcdaa13c4214`,
the frozen seven tails at SHA
`d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848`,
and the odd-sheet terminal compiler only as a factor-DAG/source-typing
template (SHA
`2d8507bcdab953f94a19bc6f794fe8233f466c74afcbab4f21497aab4280951a`).
The odd-sheet normalization itself is not reused.

## 1. The raw cusp open is already smooth

Write `s=cs`, `d=rs`,

```text
A=a1*z+a0,       C=(c1*z+c0)/2,       R=s*z+d/4.
```

At `p=0` the four nonzero raw grade-ten rows are

```text
(15/256)k0*s*d^2+(3/8)(a1*c0+a0*c1),
(5/1024)k0*d^3 +(3/8)a0*c0+(3/32)c1^2,
(3/16)c0*c1,
(3/32)c0^2.                                      (1.1)
```

There is no conductor or nilpotent calculation left to do on `D(d*k0)`.
Indeed, the last row makes `c0` nilpotent.  The second row then makes `c1^2`
a unit (a unit plus a nilpotent), so `c1` is a unit; the third row consequently
forces `c0=0` in the raw localized quotient, not merely in its radical.  The
first two rows become

```text
96*c1^2+5*k0*d^3=0,
96*a0*c1+15*k0*s*d^2=0.                           (1.2)
```

Put

```text
u=c1/d.
```

Then `u` is a unit and (1.2) is exactly

```text
c1=d*u,       a0=3*s*u,       5*k0*d+96*u^2=0.    (1.3)
```

Thus the reduced normalization is already an isomorphism on this open.  It
may be presented either as

```text
k0=-96*u^2/(5*d),       d*u != 0,                  (1.4)
```

or, retaining the load as an independent coordinate,

```text
d=-96*u^2/(5*k0),       k0*u != 0.                 (1.5)
```

For fixed `k0`, (1.5) is the usual `(2,3)` parametrization:

```text
wt(u)=1,       wt(d)=2,       wt(c1)=3,
wt(a0)=wt(s)+1,       wt(k0)=0.                    (1.6)
```

The conductor belongs to the removed closure `d=0`; computing it in this
client would only waste a source round.

Two involutions must not be conflated.  The sign involution of (1.5) sends
`(u,c1,a0)->(-u,-c1,-a0)` with `s` fixed.  The source deck `z->-z` sends

```text
(u,s,a1)->(-u,-s,-a1),       d,k0,a0 fixed.         (1.7)
```

## 2. Complete first successor and its four rows

Use the normalized arc, with every displayed correction independent before
later equations are solved,

```text
Lambda=sigma^2,
p=2*sigma*ell1+2*sigma^2*ell2+...,

R=s*z+d/4+sigma*(s1*z+d1/4)+sigma^2*R2+...,
A=a1*z+3*s*u+sigma*(aa1*z+aa0)+sigma^2*A2+...,
C=(d*u*z+sigma*(e1*z+e0)+sigma^2*C2+...)/2,
k10=k0+sigma*k1+sigma^2*k2c+...,

K=(z^2+p/2)^2+sigma^2*R,
f=K^2+sigma^5*((z^2+p/2)*A+C),                    (2.1)
```

with (1.4) imposed in the Laurent coefficient ring.  Corrections have their
literal `sigma` order; in particular the moving centre, `R1,A1,C1`, and
`k1` all have correction weight one.

Let `L=z^2`, `R0=s*z+d/4`, `C0=d*u*z/2`,
`A0=a1*z+3*s*u`, and put

```text
R1=s1*z+d1/4,       A1=aa1*z+aa0,
C1=(e1*z+e0)/2.
```

The grade-ten Laurent receiver is

```text
h10=[(3/4)A0*C0/L+(3/8)C0^2/L^2
     +(5/16)k0*R0^3/L]_-;                          (2.2)
```

it vanishes identically under (1.3).  Direct binomial expansion gives the
complete grade-eleven receiver

```text
h11=[
 (3/4)*((A0*C1+C0*A1)/L
        +(C0*C1-ell1*A0*C0)/L^2-ell1*C0^2/L^3)
 +(5/16)*(k1*R0^3/L+3*k0*R0^2*R1/L
          -k0*ell1*R0^3/L^2)
 +(5/8)*k0*C0*R0/L
]_-.                                               (2.3)
```

Formula (2.3) retains the first moving-centre term, both first `R` and load
motions, and the `D*K^(1/2)` cross term.  The omitted `A0*R0` part of the
last cross term is polynomial, not discarded by valuation.  `R2,A2,C2,k2c`,
the lower loads, and all targets occur later.

Before normalization, the moving Laurent-to-Faber relation is

```text
g11[ell]=h11[ell]
 +((ell-2)/2)*ell1*h10[ell-2]       (ell>=3).       (2.4)
```

Because (2.2) is identically zero after (1.3), the normalized source rows
equal the coefficients of (2.3).  They are

```text
g11[1]=(3/8)*(a1*e0+3*s*u*e1+d*u*aa0)
       +(15/256)*k1*s*d^2
       -(9/8)*u^2*(2*s*d1+d*s1)
       +6*ell1*s^3*u^2/d-(3/2)*d*u^3,

g11[2]=(9/8)*s*u*e0+(3/16)*d*u*e1
       -(3/8)*ell1*a1*d*u+(5/1024)*k1*d^3
       -(9/32)*d*u^2*d1+(9/2)*ell1*s^2*u^2,

g11[3]=(3/16)*d*u*e0,
g11[4]=-(3/32)*ell1*d^2*u^2,
g11[5]=g11[6]=g11[7]=0.                           (2.5)
```

Hence on `D(d*u)` the fourth and third rows force, without a radical,

```text
ell1=0,       e0=0.                                (2.6)
```

For completeness the next two rows are triangular rather than obstructive:

```text
e1=(3/2)*u*d1-(5/192)*k1*d^2/u,

aa0=4*u^2+3*u*s1+(3/2)*(s*u/d)*d1
     -(5/64)*(s*d/u)*k1.                           (2.7)
```

The unit below needs only (2.6), not the solutions (2.7).

## 3. The grade-twelve sixth row is a unit

Form every grade-twelve source row before applying (2.6).  Modulo the two
triangular grade-eleven pivots, only two terms can reach the sixth Laurent
pole.  The order-two coefficient of `(3/8)*D^2/K` contributes

```text
[z^-6] (-(3/8)*R0*D0^2/L^4)
 =-(3/128)*d^3*u^2,                                (3.1)
```

because the lowest term of `D0=L*A0+C0` is `(d*u/2)z`.  The fourth binomial
term of the charged `k10*K^(5/2)` contributes

```text
[z^-6] (-(5/128)*k0*R0^4/L^3)
 =-(5/32768)*k0*d^4
 = +(3/1024)*d^3*u^2.                              (3.2)
```

All second corrections have too small a pole order to enter row six; the
`k10*D*K^(1/2)` correction has at most the lower poles, and the grade-twelve
`k6*L^3` term is polynomial.  In the moving Faber transform, the possible
connection terms contain `ell1` or a grade-ten row of index at least four,
so they vanish after (2.2) and (2.6).  Row six has no target (and its first
possible target would in any event be at absolute grade thirty-six).

Consequently the predicted complete source identity is

```text
g12[6] mod (g11[4],g11[3])
 =-(21/1024)*d^3*u^2.                              (3.3)
```

This is a raw unit on `D(d*u)=D(d*k0)`.  A focused frozen-tail sign sentinel
sets `d=u=1`, `s=a1=0`, all corrections to zero, and `k0=-96/5`.  Then

```text
a4=(1/2)*sigma^2,       a1=(1/2)*sigma^5,
a0=(1/16)*sigma^4,
```

and the four canonical row-six monomials at grade twelve contribute

```text
-9/1024,       -3/256,       +3/256,       -3/256,
```

whose sum is `-21/1024`.  This focused check fixes the Faber row and sign;
the complete correction-aware replay remains the promotion gate.

## 4. What can and cannot be reused

- The odd-sheet terminal compiler's canonical-tail hashing, exact factor
  DAG, target masks, and row manifests are reusable.  Its hard-coded series,
  normalization, predecessor `F`, and grade range are not.  If (3.3) passes,
  no later terminal or finite-Taylor row is needed for this cusp.
- The universal Taylor term emitter can run as a nonblocking typing control,
  but actual finite regularity would require a new cusp-to-global Gate A.
  The unproved odd-sheet Gate A does not transfer to (1.3).
- The nonsquare K3 theorem is not licensed here.  Its open is `D(b*m)`, where
  `b` is a nonzero root separation; the present centre has `b=0`, and (2.6)
  forces the first moving-centre/root-separation jet to vanish.  A later
  separated face may be routed only after an exact K2 row transform proves
  that open.
- Generic common-quartic artifacts supply the frozen tails and source
  transforms, not an elimination theorem on this collision open.

## 5. Minimal AWS producer and stop rules

The smallest decisive client reconstructs all seven frozen source rows only
through grades ten, eleven, and twelve.  It should run exact `Q` on one AWS
host and an independent good-prime control on another, and it must:

1. verify the raw localized reduction (1.1)--(1.3) by two-sided normal forms,
   without a radical or saturation by `c0,c1,d,u`;
2. use a true Laurent coefficient ring for (1.4), or an inverse-variable
   graph whose reductions are checked at every extracted coefficient;
3. form all raw grade-eleven and grade-twelve rows before solving any row;
4. reproduce (2.2)--(2.5), including the moving transform (2.4), and certify
   absence at grade eleven of `ell2,R2,A2,C2,k2c,k6,k2` and all targets;
5. retain every second correction and every load while extracting grade
   twelve, certify exact target grades `28,32,36,38`, and prove (3.3) by
   reduction only by the two explicit unit pivots (2.6);
6. print source/full row hashes, correction/load support, deck checks (1.7),
   the unsolved raw rows, and the exact multiplier
   `-1024/(21*d^3*u^2)` producing one.

Run the four-monomial focused replay independently of the complete compiler.
If both exact-Q constructions agree, freeze the source and launch hostile
review immediately; the modular lane is software evidence only.  A missing
correction, a wrong moving-row connection, a modular-only unit, a timeout,
or reduction by anything beyond `(d*u,g11[4],g11[3])` is no verdict.  If the
unit fails, freeze the complete raw grade-twelve component and continue the
same factor DAG rather than switching to Taylor or K3.

## 6. Scope firewall

Even after exact-source confirmation, (3.3) excludes only the post-`M=0`,
unit-`k0`, `p=0` cusp `D(rs)` in this `(8,12)`, exact-order-two, `[6,2]`
client.  It does not cover positive-order or fractional-load fans, the
boundary `rs=0` outside the already eliminated odd open, other infinity
supports or terminal profiles, the whole square branch, all order two, all
`(8,12)`, maximum twelve, or JC2.
