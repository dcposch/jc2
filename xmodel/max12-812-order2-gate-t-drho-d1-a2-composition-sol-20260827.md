# Gate T: first bounded `D(rho)` total-source / generic-square contact composition

Date: 2026-08-27

Status: **DERIVED-HERE NARROW COMPOSITION THEOREM, PENDING HOSTILE REVIEW.
THE ACTUAL-TOTAL UNIQUE-`AC` CONTACT `ord(A)=2`, `ord(C)=3`,
`ord(R)>=2` IS EXCLUDED ON `D(rho*k)` AFTER THE REVIEWED GENERIC-SQUARE
GATES.  THIS IS ONE GENERIC CONTACT, NOT A COVER.  NO `rho=0`, WHOLE
DECK/SQUARE, GATE-T, `G2-PSC`, `G2-BD`, ORDER-TWO, MAXIMUM-TWELVE, OR JC2
VERDICT.**

## 0. Exact outcome

The finite-flat Kummer/source-row bridge composes with one already promoted
generic-square endpoint.

Let `k` be a characteristic-zero field and let `V` be a normalized DVR with
uniformizer `sigma`.  In the Kummer total source put

```text
p0=-2*rho^2
```

and work on `D(rho*k)`, where `k` is the leading unit-`k10` coefficient.
Assume the reviewed generic-square first-normal, half-weight, and `M=0`
gates, and suppose the square correction has the unique-`AC` contact

```text
ord_sigma(A)=2,  ord_sigma(C)=3,  ord_sigma(R)>=2.       (0.1)
```

Then no such finite-order normalized total-source DVR arc exists.

This is the `a=2` slice of the promoted generic-square D1 contact ladder,
transported into the literal Kummer total source.  Both root allocations are
included and exchanged by `rho |-> -rho`.  The proof uses the actual total
raw rows at grades 15 and 16.  It does not use a parity argument, a radical
comparison, a specialized Rees chart, or an inverse root transform at
`rho=0`.

## 1. History check and novelty boundary

Close-synonym searches covered `total D1`, `D1AC`, `deck/square`,
`generic-square overlap`, `D(rho)`, `grade 15/16`, `contact coverage`, and
`root allocation`.  The closest frozen artifacts are

```text
1b583d5a58ae3c26edd2f394e85e2540871ccfd996ec0bc798b84235c564361a
  xmodel/max12-812-order2-gate-t-kummer-row-bridge-discriminator-sol-20260827.md

973f7953d42fdd994d9c7da8ea70fceffc2e8da9002b33f38ea1a17c6922d6d1
  xmodel/max12-812-order2-square-d1-finite-band-a2-a5-promotion-20260826.md

e03de4e1fc1816a7141c6bb8060b4a75c2a6b5a08ea4d56ca63582b875cad335
  xmodel/max12-812-order2-square-d1-finite-band-a2-a5-hostile-review-grok-20260826.md

c9ecfe4000092912464e29ecc526ac5c065f950778d31cac81f58fe06622954d
  xmodel/max12-812-order2-square-fan-lower-hull-reduction-20260826.md
```

The first artifact proves the universal total-to-`D1AC` primitive identity,
the grade-15 actual-row comparison, and the root-coordinate isomorphism on
`D(rho)`.  It deliberately stops before importing a two-grade endpoint
because it located no frozen general-`rho` grade-16 exporter.  The second and
third artifacts promote and review the two-grade `a=2` endpoint.  The fan
artifact identifies its contact as one proper subcell of the unit-load
horizontal fan.

The new content here is the exact finite-jet composition at grade 16 and the
resulting total-source exclusion (0.1).  It does not claim that the whole
generic-square compiler suite has been mapped, or that an empty contact
client is a cover of the total source.

## 2. Rings, maps, rows, and localizers

Use the finite raw total ring `U_16` and rows `Phi_ell`, `1<=ell<=7`, from
Sections 2 and 6 of the Kummer bridge.  Its Kummer pullback is

```text
U_16^rho = U_16 tensor_(k[p0]) k[rho],
p0 |-> -2*rho^2.                                      (2.1)
```

Let

```text
I^tot_16=([sigma^g]Phi_ell : g<=16, 1<=ell<=7)
```

in `U_16^rho`.  The multiplicative set for this theorem is

```text
S_tot={(rho*k)^n:n>=0}.                              (2.2)
```

Let `D_16` be the raw polynomial ring of the frozen `D1AC` compiler, before
its analytic auxiliary relations, and let

```text
I^D1_(15,16)=([sigma^g]Phi_ell^D1:
               g in {15,16}, 1<=ell<=7).             (2.3)
```

After adjoining `lambda` and imposing

```text
p+2*lambda^2=0,  lambda=rho,
```

the D1 localizer `p*k` pulls back to `-2*rho^2*k`; hence

```text
D(p*k)=D(rho*k).                                    (2.4)
```

No factor of `rho` is used outside this explicitly registered generic open.

The total staged ideals remain

```text
J1=(rs,cs,c0,c1),
J2=(a0,a1) after quotient by J1.                    (2.5)
```

On `D(rho)` the invertible root-value map is

```text
Rplus  = rs/4+rho*cs,       Rminus = rs/4-rho*cs,
Cplus  = (c0+rho*c1)/2,     Cminus = (c0-rho*c1)/2,
Aplus  = a0+rho*a1,         Aminus = a0-rho*a1.     (2.6)
```

Its three determinants are `-rho/2,-rho/2,-2rho`.  Thus (2.6) is available
in this theorem and unavailable at the ramified fibre.

On contact (0.1), the stage-zero coordinates in (2.6) themselves vanish:
the first nonzero `R,C,A` coefficients occur two, three, and two source
steps later.  The nonzero root allocations below must therefore be read in
the corresponding **shifted jet pairs**, not in `(rs,cs)`, `(c0,c1)`, or
`(a0,a1)`.  Explicitly, (4.2) gives

```text
R0plus  = rs2/4+rho*cs2,       R0minus = rs2/4-rho*cs2,
C0plus  = (ec3+rho*ez3)/2,     C0minus = (ec3-rho*ez3)/2,
A0plus  = aaa0+rho*aaa1,       A0minus = aaa0-rho*aaa1. (2.7)
```

These are the same invertible matrices, applied coefficientwise.  This
shift is load-bearing: using the zero stage coordinates as the D1 leading
forms would be a false composition.

## 3. Grade-16 actual-source custody: exact scope

The earlier bridge's sentence “no frozen actual-total grade-16 exporter was
located” remains literally correct if *exporter* means seven serialized
general-`rho` polynomial files.  This report does not relabel the `rho=0`
V28 files as general-`rho` rows.

A frozen current producer nevertheless supplies the actual construction
path:

```text
6c76dc541d27b436a289f1decccd6e90c1424b3a586685e128331c8490b06480
  cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g16_v28_20260827/
  prolong_boundary_g16_v28.py
```

Before imposing its unrelated ordered-`a1`, `rho=0` face, V28 constructs

```text
p=-2*rho^2+2*sum_(i=1)^16 sigma^i*ell_i,
c=sigma^2*Cseries,
r=(p^2+sigma^2*Rseries)/4,
n3=sigma^3*Azseries,  n2=sigma^3*Acseries,
n1=sigma^3*(p*Azseries+Ezseries)/2,
n0=sigma^3*(p*Acseries+Ecseries)/2,                 (3.1)
```

then the same seven `F_i`, the same frozen 569 tails, and all seven total
coefficients `[sigma^16]Phi_ell`.  Only after those objects exist does it
apply `rho=0` and the ordered-face quotient.  Its exact-Q execution freezes
the grade-16 construction path and the seven face outputs.

The general-`rho` row equality used below is not inferred from those face
outputs.  It is the polynomial identity already proved in the Kummer bridge:
the total and D1 substitutions give the identical seven primitives, load
map, target map, and tail polynomial, so coefficient extraction commutes at
every grade.  V28 establishes that (3.1) is also the current actual-total
producer path through grade 16.  A dedicated general-`rho` serialization
would improve documentary custody but is not an additional mathematical
hypothesis of the composition.

## 4. Finite-jet factorization lemma

The literal map in the Kummer bridge sets later total jets to zero.  An
arbitrary DVR arc in (0.1) need not factor through that quotient as a full
formal series.  What is true, and sufficient, is the following finite-jet
statement.

> **Lemma `CF-D1-A2`.**  On the contact (0.1), the fourteen total rows at
> grades 15 and 16 factor through the frozen `D1AC` finite-jet ring.  Their
> values are independent of every discarded later jet.  The induced rows
> are exactly `I^D1_(15,16)`.

Write the leading square corrections as

```text
A=sigma^2*(A0+sigma*A1+...),
C=sigma^3*(C0+sigma*C1+...),
R=sigma^2*(eta*R0+...),                            (4.1)
```

where `A0,C0` are nonzero linear polynomials, and use `eta=0` in the
two-grade truncation when `ord(R)>2`.  The explicit total-jet map is

```text
ell1 -> ell1;

(cs,cs1,cs2,...) -> (0,0,eta*b1,0,...),
(rs,rs1,rs2,...) -> (0,0,4*eta*b0,0,...),

(a1,aa1,aaa1,az3,...) -> (0,0,a1D,aa1D,0,...),
(a0,aa0,aaa0,ac3,...) -> (0,0,a0D,aa0D,0,...),

(c1,e1,ee1,ez3,ez4,...) -> (0,0,0,2*c1D,2*cc1D,0,...),
(c0,e0,ee0,ec3,ec4,...) -> (0,0,0,2*c0D,2*cc0D,0,...),

k -> k0;  k6 -> k6;  k2 -> k2load; targets fixed.   (4.2)
```

The factors `4` and `2` are forced by (3.1).  A common nonzero leading
factor `theta` in the symbolic D1 compiler is absorbed into the nonzero
coefficients at exact contact `a=2`; equivalently set `theta=1`.

Completeness through grade 16 is a support calculation, not a claim that
the ellipses vanish.  With `a=2`, the decisive grades are

```text
g=11+2a=15,  g+1=16.                               (4.3)
```

The only polar families in this window are

```text
AC/L       at 15,
C^2/L^2   at 16,
k10*R*C/L at 16 when ord(R)=2,
k10*R^3/L at 16 only when ord(R)=2.                 (4.4)
```

The next possible families have grades `>=18`; `k6*C/L` starts at 20,
`k2*R/L` at 24, and the four targets at 28,32,36,38.  The moving row basis
uses offsets zero and one only, so `ell1` occurs but `ell2` and later
connection jets do not.  The next `R` jet is likewise later than grade 16.
These are exactly the completeness checks in the confirmed finite-band
review.  Substitution of (4.2) into (3.1) is the primitive identity from the
Kummer replay, proving the lemma.

## 5. Narrow `D(rho)` deck-square exclusion

Put

```text
L=z^2+p/2=z^2-rho^2.                                (5.1)
```

The grade-15 D1 row forces `L | A0*C0`.  Because `L` is squarefree on
`D(rho)` and `A0,C0` are nonzero linear polynomials, there are precisely two
allocations:

```text
plus:   A0=au*(z-rho),  C0=cv*(z+rho),
minus:  A0=au*(z+rho),  C0=cv*(z-rho),              (5.2)
```

with `au,cv` nonzero.  The deck involution exchanges them.  At grade 16,
after putting the double-pole numerator over `L^2` and evaluating at the
`A0` root, both orientations give

```text
(3/2)*rho^2*cv^2.                                  (5.3)
```

Every competing in-window term in (4.4) has only a simple pole and hence
acquires a factor `L` after passage to the `L^2` numerator; it vanishes at
the root.  Expression (5.3) is nonzero on the registered open.  The promoted
D1 endpoint therefore contradicts the fourteen total row equations via
Lemma `CF-D1-A2`, proving (0.1).

In total-source names, (5.2) is an allocation of the shifted pairs in
(2.7): `aaa0+rho*aaa1=0` and `ec3-rho*ez3=0` in the plus orientation, with
the two equations exchanged in the minus orientation.  No nonzero claim is
made about the vanished stage-zero pairs.

This is an arcwise/set-theoretic exclusion.  It makes no reduced-scheme or
nilpotent claim.

## 6. Exact coverage no-go and the missing composition interface

An empty contact quotient is not an ambient cover, even when every map is
deck equivariant.  The exact countermodel is

```text
A=Q[rho,u],                    tau(rho)=-rho, tau(u)=u,
I=(u-1),
q:A -> A/(u),                  u |-> 0.             (6.1)
```

Then `q(I)=(-1)=(1)`, so the specialized client is empty.  But
`V(I) intersect D(rho)` contains the point `rho=1,u=1`.  The ideal, the
quotient, and the open are deck invariant.  Thus deck equivariance plus
literal row equality on one client cannot supply source coverage.

For an actual `D(rho)` Gate-T theorem, let `X_rho` denote the registered
post-gate total DVR arcs on `D(rho*k)`.  A finite or parametric family of
contact clients `q_i:Y_i -> X_rho` must supply both:

1. **finite-jet fidelity:** every decisive total row pulls back to the
   charged client row, with all later-jet independence proved; and
2. **valuative coverage:** every arc of `X_rho` factors through at least one
   `q_i`, including equality faces and the exact-square zero-normal
   receiver.

Client emptiness plus (1) without (2) is precisely the false inference in
(6.1).  The current theorem discharges both requirements only for the
single contact (0.1).  The unit-load lower hull still contains the rest of
the unique-`AC` fan, the primary `C2`, `R3`, `RC`, `A2` faces, their
intersections, and the zero-normal receiver.  Positive-order `k10`, `k=0`,
and other source families are outside this fan altogether.

## 7. Ramified fibre and the two global `G2` obligations

Nothing here crosses `rho=0`.  The Kummer algebra is globally faithfully
flat, but all three root-coordinate determinants in (2.6) vanish at that
fibre.  The ramified source remains the four `J1` charts, two `J2` charts,
and the separate terminal receiver.  No generic root allocation is a
replacement for those six charts.

The global labels remain separate:

```text
G2-PSC = GGV packet/corner -> decorated Sigray pole-tree
         transport and fidelity;

G2-BD  = bounded delay/carrier after a residue-A configuration
         has already been reached.                              (7.1)
```

The present theorem starts after a generic-square landing and at two fixed
source grades.  It constructs no GGV-to-Sigray functor, so it gives no
`G2-PSC`.  It contains no variable or estimate measuring a residue-A carrier
delay, so it gives no `G2-BD`.  The quotient countermodel (6.1) is also a
sharp logical warning against using downstream local emptiness as either
transport or coverage.

## 8. Bounded discriminator, outcomes, and stop rule

Name this client **`KGT-DRHO-D1-A2`**.

It checks the frozen Kummer bridge, the V28 grade-16 construction path, the
promoted/confirmed D1 `a=2` endpoint, the complete two-grade support window,
both root allocations, (5.3), and the coverage negative control.

The outcomes are:

- **PASS** (observed): bank the arcwise exclusion (0.1), mark this exact
  `D(rho*k)` contact as transported, and stop all further `a=2` endpoint
  algebra.  Successor work must move to a new contact-map manifest or to the
  cover/zero-normal receiver.
- **FAIL:** freeze the first hash, primitive, support, allocation, or residue
  mismatch; quarantine the `a=2` import and repair that interface before any
  new saturation or fan computation.

The separate whole-cover discriminator has two outcomes:

- **COVER-PASS:** a proof-carrying family of contact maps satisfies both
  items in Section 6 and every client, including the zero-normal receiver,
  is empty.  Only then may the registered `D(rho)` Gate-T overlap be called
  empty.
- **COVER-FAIL:** one DVR arc, prime, equality face, or receiver point lies
  outside the images, or one row map fails.  Freeze that first witness and
  stop composing local endpoint claims as a cover.

The present whole-cover outcome is **INCOMPLETE**, not PASS and not a
counterexample.

The desk replay is

```text
python3 xmodel/max12-812-order2-gate-t-drho-d1-a2-composition-replay-20260827.py
```

and returns

```text
PASS-GATE-T-DRHO-D1-A2-COMPOSITION-DESK-REPLAY
```

in about `0.04 s` locally.  It launches no CAS process and no AWS job.

## 9. Firewall

This report proves one finite-jet contact exclusion after named upstream
gates.  It does not prove a Rees-chart equality, a terminal-receiver
exclusion, a generic-square fan cover, the ramified fibre, another load ray,
global source-to-books landing, `G2-PSC`, `G2-BD`, a cofinal complexity
bound, Gate T, order two, maximum twelve, JC2, or a counterexample.
