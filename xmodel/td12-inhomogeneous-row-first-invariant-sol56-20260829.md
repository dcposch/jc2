# TD12 distant inhomogeneous row: first source-honest invariant

Date: 2026-08-29  
Producer: Sol 5.6, independent desk-algebra lane  
Frozen Git basis: `92ebe92ad5986a47f01af9ed901260595dfed869`

## 0. Binary disposition

```text
DOES_NOT_KILL_B_OR_S_ON_THE_FROZEN_BASIS
ENDPOINT_HERMITE_CLASS_PROVED
TERMINAL_T1_QUOTIENT_ALREADY_SATISFIED
SOURCE_ENDPOINT_PACKET_OPEN
```

The first genuinely inhomogeneous Keller row does give a sharp finite
compatibility that was not written in the frozen td12 reports.  Let
`K_(s*)` be the cross-sum using only positive lower indices.  On either
route, after folding the deck character to `t=eta^nu`,

```text
K_(s*)(t) == kappa_F  mod H_i(t),

H_i(t)=gcd(P_0,P_0')=product_j (t-a_j)^(m_j*i-1).
```

Thus B carries `3i-2` endpoint Hermite conditions and S carries `4i-3`.
This modulus is the maximum forced by the two fresh endpoint operators
alone.  In particular the lower cross-sum has value `kappa_F`, not zero, at
every top root.

This is not a route kill.  The reviewed Proposition-8.1 terminal quotient
of the same Keller content is

```text
nu*p*q' - kbar*p'*q = Theta*p,       Theta != 0,
```

and the already-reviewed B and S templates solve it exactly.  The B24 and
S16 gates neither serialize the original `g` tail nor determine the endpoint
cross-sum.  Mere polynomial finiteness supplies no cap below `s*`.  The
smallest useful new source object is therefore a route-separated,
source-provenanced endpoint unit (or, more strongly, the Hermite class), not
another homogeneous-window recurrence.

## 1. Exact hypotheses and notation

Fix one route occurrence in an actual characteristic-zero polynomial Keller
pair and one exact completion.  B and S remain separate occurrences.  Use

```text
P_0=p^i,             G_0=c_g*p^r,
D_F=nu*i,            D_g=nu*r,
r=3i/2 in Z_(>0),    s*=D_F+D_g-kbar,
```

where `p=P(t)`, `t=eta^nu`, and

```text
B: nu=25, kbar=17, P=(t-A)^2(t-B),
   (m_j)=(2,1), M=3;

S: nu=17, kbar=13,
   P=(t-A)^2(t-B_+)(t-B_-),
   (m_j)=(2,1,1), M=4.
```

All displayed roots are nonzero and distinct.  Primes in Sections 2--5 are
derivatives with respect to `eta`, except where a `t` subscript is printed.
The route coefficient equation is

```text
E_s := sum_(a+b=s)
       ((D_F-a)P_a G_b'-(D_g-b)P_a'G_b)
     = kappa_F * 1_(s=s*).                         (1.1)
```

The exact source assumptions used below are: the reviewed weight law for the
actual chart pieces; the clamped root floors

```text
ord_zeta(P_a) >= max(0,m*i-a),
ord_zeta(G_b) >= max(0,m*r-b)                       (1.2)
```

at an eta-root `zeta` of a `t`-root of multiplicity `m`; and ordinary
polynomiality of every piece.  No natural cap, occurrence inferred from a
reduced cell, absent completion, or formal independent jet is used.

## 2. The sharp endpoint Hermite congruence

Separate the fresh terms in (1.1):

```text
A_s[P_s] := (D_F-s)P_s G_0' - D_g P_s'G_0,
B_s[G_s] := D_F P_0 G_s' - (D_g-s)P_0'G_s,

K_s := sum_(1<=a<=s-1)
       ((D_F-a)P_a G_(s-a)'
        -(D_g-s+a)P_a'G_(s-a)).                    (2.1)
```

Since `G_0=c_g p^r` and `P_0=p^i`,

```text
A_s[P_s]
 = c_g*p^(r-1)
   ((D_F-s)r*p'*P_s-D_g*p*P_s'),

B_s[G_s]
 = p^(i-1)
   (D_F*p*G_s'-i(D_g-s)*p'*G_s).                   (2.2)
```

Let `R=rad(p)=product_j(t-a_j)`.  In characteristic zero, with all
`a_j!=0`,

```text
H_i := gcd(P_0,P_0') = P_0/R
     = product_j(t-a_j)^(m_j*i-1).                 (2.3)
```

Every bracket in (2.2) is divisible by `gcd(p,p')`; hence `B_s[G_s]` is
divisible by `H_i`.  The analogous divisor of `A_s[P_s]` is
`product_j(t-a_j)^(m_j*r-1)`, which contains `H_i` because `r>=i`.
At `s=s*`, (1.1) therefore gives the exact polynomial congruence

```text
K_(s*) - kappa_F in H_i*K[eta].                    (2.4)
```

It is sharp at the endpoint-operator tier.  Indeed `D_g-s*=kbar-D_F` is
nonzero, and a weight-one polynomial `G_(s*)=eta` makes the second term of
`B_(s*)` have exact order `m_j*i-1` at every top root.  Thus no larger common
root divisor follows from the fresh operators without an additional source
premise.

## 3. Deck folding and the route-specific invariant

The reviewed weight residue is `e_a == -M*a (mod nu)` on both f and g.
Since

```text
s* == -kbar (mod nu),
M*kbar == 1 (mod nu)          (3*17==1 mod25; 4*13==1 mod17),
```

one has `e_(s*)=1`.  Each summand in `E_(s*)` loses one deck character under
differentiation and is invariant.  Hence `K_(s*)` belongs to `K[t]`, and
(2.4) folds without loss to

```text
Kcal_(s*)(t) == kappa_F mod H_i(t).                 (3.1)
```

Explicitly:

```text
B: H_i=(t-A)^(2i-1)*(t-B)^(i-1).

   Kcal(A)=kappa_F,
   (d/dt)^j Kcal(A)=0 for 1<=j<=2i-2,
   Kcal(B)=kappa_F,
   (d/dt)^j Kcal(B)=0 for 1<=j<=i-2.

S: H_i=(t-A)^(2i-1)*(t-B_+)^(i-1)*(t-B_-)^(i-1),

   the same A conditions, and
   Kcal(B_+)=Kcal(B_-)=kappa_F,
   (d/dt)^j Kcal(B_+)=(d/dt)^j Kcal(B_-)=0
     for 1<=j<=i-2.
```

Thus the B class has `deg H_i=3i-2` scalar Hermite slots and the S class
has `deg H_i=4i-3`.  The two S evaluations are coupled evaluations of one
polynomial; they are not independent source states.  A single mismatch at
the double orbit `A` would already kill the route.

## 4. What the multiple root forces from source support

Evaluate (2.1) at an eta-root `zeta` over a `t`-root of multiplicity `m`.
Because the fresh terms vanish there for `i>1`,

```text
K_(s*)(zeta)=kappa_F != 0.                           (4.1)
```

The clamped floors (1.2) show that a summand can be nonzero at `zeta` only
in one of the following two ranges:

```text
P_a*G_b'  : a>=m*i   and b>=m*r-1,
P_a'*G_b  : a>=m*i-1 and b>=m*r,       a+b=s*.       (4.2)
```

Consequently at least one source term attaining (4.1) exists, and at the
double orbit it necessarily uses

```text
a>=2i-1,       b>=2r-1=3i-1.                         (4.3)
```

This is an attainment conclusion forced by the nonzero right side, not a
claim that every floor is attained.  It also gives a minimal support
penetration statement: if `C_f,C_g` are the last nonzero chart grades, then
`C_f+C_g>=s*`, and the local tails at the double orbit must reach the ranges
(4.2).

For the sharp transparent-window thresholds this already lies beyond the
homogeneous row window:

```text
B: i>=16, r>=24  => a>=31, b>=47, while depth=24;
S: i>=12, r>=18  => a>=23, b>=35, while depth=16.
```

This comparison is only with the homogeneous Keller-row windows.  A
recentered depth gate can consume other f-side Taylor data; no claim is made
that its full recursive source footprint stops at grade 24 or 16.

## 5. Quotienting the homogeneous binomial response

There are two distinct, source-honest statements here.

### 5.1 What is forced before the first resonance

Let `G^bin=c_g F^(3/2)` be expanded coefficientwise from the actual f-side
pieces.  If the actual and binomial g-pieces agree below order `s<nu`, their
difference at order `s` lies in the polynomial kernel of `B_s`.  That kernel
would be generated formally by

```text
p^(r-s/nu),
```

which is not a polynomial because `0<s<nu` and `p` has a simple nonzero
root.  Thus induction gives

```text
G_s=G_s^bin for 1<=s<nu.                              (5.1)
```

The first transverse homogeneous datum can occur at `s=nu`, where the
kernel becomes `K*p^(r-1)`.  This is exactly one order beyond the associated
homogeneous-row windows (`24=25-1` and `16=17-1`).  It is not supplied by
either depth gate.  Subsequent resonant data and the approximate-root tower
are likewise absent.

### 5.2 The terminal source quotient

The repaired Proposition 8.1 supplies, for the terminal approximate root,
polynomials `p,q` satisfying, up to nonzero route scales,

```text
nu*p*q' - kbar*p'*q = Theta*p,       Theta != 0.      (5.2)
```

At a root `zeta` of `p` of multiplicity `m`, the repaired root law says
`q` has a simple zero.  Dividing (5.2) by `p` and taking the limit gives the
finite root invariant

```text
(nu-m*kbar)*q'(zeta)=Theta.                           (5.3)
```

For B the coefficients are `-9` on the double orbit and `8` on the simple
orbit.  For S they are `-9` and `4,4`.  These are precisely the equations
whose reviewed solutions are

```text
B: B/A=9/8;
S: B_+ + B_-=9A/4,  B_+*B_-=45A^2/32.
```

So the maximum source-certified quotient currently available is compatible,
not contradictory.

There is a useful conditional literal identification.  If the first
resolvent is already terminal,

```text
h_1=g^2-s_0*f^3=h_F,       s_0=c_g^2,       m_F=1,
```

then Proposition 4.2 has `mu=3/2`, the first surviving coefficient of
`h_1` occurs exactly at grade

```text
3D_F-((1/2)D_F+kbar)
 = D_F+D_g-kbar=s*,
```

and has the form `p^(i/2)q`.  The leading coefficient of
`J(f,h_1)=2g` reduces exactly to (5.2).  This explains how the distant row
becomes T1 after removing the homogeneous common power.  The frozen route
does not instantiate `m_F=1`, the intermediate resolvents, their constants,
or their coefficient maps, so this literal first-resolvent identification
is a conditional lemma only.  For a longer tower, repaired Proposition 8.1
still licenses (5.2), but no unrecorded map from the original `P_a,G_b` to
the terminal `q` may be invented.

## 6. Why the depth gates plus polynomiality do not kill

1. The homogeneous Keller-row analysis attached to B24/S16 stops immediately
   before the first polynomial homogeneous kernel in (5.1).  The gates
   themselves constrain f-side child polynomials; they do not fix the new
   g-side resonant scalar at `s=nu` or its descendants.
2. The endpoint unit (4.1) is a bilinear expression in original f and g
   tails.  At the double root it necessarily uses the deep ranges (4.3).
   No reviewed theorem maps the pure-power child conditions to that bilinear
   unit.
3. Polynomiality says the source tails are finite, but the route packet pins
   neither cap.  In fact (4.1) forces the joint support to reach `s*`; a cap
   below that would contradict the existence of the hypothetical pair, not
   exclude the reduced route independently.
4. The one compressed source compatibility that is available, T1, has
   already been solved and passed on both routes.

Therefore neither route is invalidated.  This is a proof that the frozen
data do not yield the proposed endpoint contradiction, not a construction
of a formal germ or an assertion that either reduced route occurs.

## 7. Smallest missing premise and packet

The strongest finite consumer is the class

```text
[Kcal_(s*)] in K[t]/(H_i),                            (7.1)
```

whose required value is the constant class `[kappa_F]`.  The smallest kill
client is only its value at the double orbit,

```text
EndpointUnit_A := Kcal_(s*)(A),       required = kappa_F.   (7.2)
```

A route-separated `TD12-ENDPOINT-UNIT/v1` packet need not serialize every
global polynomial.  It is sufficient to carry

```text
PairRef_R + route occurrence + exact completion and deck orbit;
i,r,kappa_F and the top normalization P_0=p^i, G_0=c_g*p^r;
the source-provenanced local 1-jets at one eta-root over A of
  P_a and G_(s*-a), 1<=a<=s*-1;
a support-completeness certificate for the omitted grades;
the exact convolution replay producing EndpointUnit_A.
```

For the full Hermite class, replace the local 1-jets by the finite Taylor
jets through order `2i-1` at A and `i-1` at each simple orbit (one extra
source derivative is needed because `K_(s*)` already contains first
derivatives).  Direct exact polynomials plus the completion map may replace
all lists.

The smallest missing mathematical premise for a kill is correspondingly
one source theorem deriving

```text
EndpointUnit_A != kappa_F
```

from route occurrence, global support/minimality, and the depth-gate
conditions.  No such theorem is in the frozen basis; the already-solved T1
equation points the other way at the terminal quotient tier.  A complete
instantiated approximate-root tower could be a more compressed producer,
but it must include the literal transgression from original jets to `q` and
must keep B and S source states separate.

## 8. History, custody, and scope firewall

Frozen-basis history search found the exact recurrence, the `p^(i-1)` fresh
factor, the formal rank/cokernel theorem, and the instruction to attack
`s*`; it found no endpoint congruence modulo `gcd(P_0,P_0')`, no route
Hermite class, and no double-root support-penetration statement.  The T1
ODE and both root templates are prior reviewed work and receive no novelty
claim here.

Actually charged full-file SHA-256 hashes:

```text
7af80df724d880a47452de96a731ff1c4e17b8244fdbae8fc76eb1461e7bcc22
  xmodel/post1224-next-wave-packet-20260829T1335Z.md
bb70bc4b96d37a5a87bcbf9cba26db7fb96b45e9e0189204fde18f104a517900
  xmodel/td12-bchild-v1-minimal-source-packet-audit-sol56-76c-20260829.md
79df783a0ed9e370621e750f4e6564dc9871b53e1481898e77dcdd037711ad1c
  xmodel/td12-bchild-v1-minimal-source-packet-audit-r1-erratum-sol56-76c-20260829.md
1a60264334ae99f60ff79f1ed8b4a75cb42abf30f5e4ae8001a51b9064056d84
  xmodel/td12-bchild-v1-primary-fable5-76c-20260829.md
876d1717efdc69865cfae6c8b5d4ef983440a5f0997a9edf3cf13a2a5cc70aab
  xmodel/td12-bchild-v1-primary-fable5-hostile-disposition-r1-sol56-76c-20260829.md
97ba497fffcf0a0ee5c9ee259acc325810659a9fd5376a47b38c87476fd2c5b4
  xmodel/td12-formal-cascade-rank-v1-coordinator-integration-sol56-20260829.md
5fc6b1634dc1ef0a0abe578411644fa166ffbfa16b8608cbce2a7b7b61465cd5
  xmodel/sigray-later-m-package-source-audit-sol-ultra-20260828.md
4c3f2236a11f296f7eb194bb26e8cdc8ff0b91f10d8d7151e6314caa62629304
  xmodel/g2-psc-typed-source-to-pole-tree-interface-sol-ultra-20260827.md
f7de3ae12918c9103d595e81ddc7fcb9082ba950698f70966ade3ea576cc79a1
  xmodel/g2-psc-typed-source-to-pole-tree-interface-hostile-review-opus5-20260827.md
599e2a9123194c580b89b822f5b7a218fa5e9735b16bcb744e0f0e4231584271
  xmodel/m2-td12-u1-trunk-consumer-primary-grok46-20260829.md
91b36515950f038d08a444df16f9c09ee9763adb7950d46e9c50e43451f25c0f
  xmodel/m2-td12-u1-trunk-consumer-hostile-review-opus5-20260829.md
9a9e948cafbea9fa448b84435c0ce004dec92903ba56984759353bf6a8d132bc
  xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-sol56-20260829.md
432a4152387cff943e220a6236912f2481a1ea3004d2c53ae95f14eb267f1ab0
  xmodel/m2-td12-u1-sibling-t1-ratio-solve-r1-hostile-review-grok46-20260829.md
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
  refs/sigray_full.pdf
```

Literal source passages charged: Statement 3.7 and Notations 3.9--3.11
(chart coefficients), Propositions 4.1--4.2 (first nonzero Jacobian row and
approximate roots), and repaired Proposition 8.1 (terminal polynomial
quotient), all in the pinned PDF.  The exact-pair interface is used only for
the conditional assertion that an actual pair plus completion emits the
pieces; its reviewed rectangle, tower-gap, and source-map riders remain in
force.

This report supplies no `PairRef`, route occurrence, coefficient values,
completion, endpoint-unit value from a source, gate verdict, landing,
exclusion, degree bound, counterexample, or JC2 conclusion.  It does not
identify B and S, does not identify the two S roots as independent states,
and does not extend the binomial lift past a proved polynomial range.  No
canonical/source/code file, AWS resource, commit, or `jc2-lean` object was
touched.  Desk algebra only was used.

<!-- END-SEALED-BODY::td12-inhomogeneous-row-first-invariant-sol56-20260829 -->

## Seal (outside the sealed body)

- Body byte count: `15383` (all bytes before this heading).
- Body SHA-256:
  `36381aca4e450047507d46cbf9f2c1a1f17a6f4d4fd3333e372b491f28f8de41`.
- Full-file SHA-256 is emitted with the transmittal after this seal is
  immutable; reproduce it with
  `shasum -a 256 xmodel/td12-inhomogeneous-row-first-invariant-sol56-20260829.md`.
- Frozen Git basis: `92ebe92ad5986a47f01af9ed901260595dfed869`.
