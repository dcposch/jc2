# Gate T: exact `D(rho*k)` unique-`AC` ledger and the next contact import

Date: 2026-08-27

Status: **DERIVED-HERE NARROW COMPOSITION THEOREM, PENDING HOSTILE REVIEW.
AFTER THE REVIEWED GENERIC-SQUARE GATES, THE ACTUAL-TOTAL CONTACT
`ord(A)=2`, `ord(C)=4`, `ord(R)>=3` IS EMPTY ON `D(rho*k)`.  THIS IS THE
VALUATION-MINIMAL UNTRANSPORTED STRICT UNIQUE-`AC` CONTACT AFTER
`(2,3,>=2)`.  IT IS NOT THE WHOLE UNIQUE-`AC` FAN OR A GENERIC-SQUARE
COVER.  NO EQUALITY FACE, `rho=0`, `G2-PSC`, `G2-BD`, GATE T, ORDER TWO,
MAXIMUM TWELVE, OR JC2 VERDICT.**

## 0. Result and gates

Let `K` be a characteristic-zero field, let `V` be a normalized DVR with
uniformizer `sigma`, and use the Kummer total source

```text
p0=-2*rho^2.
```

Retain, without weakening, the reviewed generic-square hypotheses:

```text
first-normal support;
the registered half-weight ray;
the exact reduced M=0 gate;
unit leading k10, q=ord(k10)=0;
p0!=0, equivalently rho!=0;
a=ord(A)>=1, r=ord(R)>=2, c=ord(C)>=3.
```

Write `k` for the constant unit coefficient of `k10`.  On a Keller source
the terminal target `J` is also a unit, so the common open
`D(rho*k*J)` is named `D(rho*k)` below.  No statement is made on `V(k)`,
for a positive-order leading load, or before any of the displayed gates.

Under these assumptions, there is no finite-order total-source DVR arc with

```text
ord(A)=2,  ord(C)=4,  ord(R)>=3.                    (0.1)
```

Both opposite-root allocations are included.  The deck involution
`rho |-> -rho` exchanges them.

## 1. History check and novelty boundary

Close-synonym searches covered `unique-AC`, `D1 contact ladder`, `d23`,
`total D1`, `D(rho)`, `deck/square`, `a2d2`, `grade 18`, `contact map`, and
`coverage ledger`.  The nearest immutable artifacts are

```text
1b583d5a58ae3c26edd2f394e85e2540871ccfd996ec0bc798b84235c564361a
  xmodel/max12-812-order2-gate-t-kummer-row-bridge-discriminator-sol-20260827.md

db0ecebf37cf8283c27e36ed8f0ba10ae9bcf1887d1854affe73cf61c8f367cd
  xmodel/max12-812-order2-gate-t-drho-d1-a2-composition-sol-20260827.md

85533441f2e2b5b04d499e30399ca0f9d62110379e01b50716cdbb3febd36680
  xmodel/max12-812-order2-square-d1-unitload-d1-contact-ladder-composition-promotion-20260826.md

cdd2305804073e771b26d00a22030486a3d8347c6d70c41f4d6a7a7b6482e1c7
  xmodel/max12-812-order2-square-d1-unitload-unique-ac-d23-composition-audit-20260826.md

94a6037db532165a50ce03b40da0e6ca2be12d5c79aacc4ee3d95baecdabc5ab
  xmodel/max12-812-order2-square-d1-unitload-unique-ac-d23-composition-hostile-review-grok-20260826.md
```

The Kummer report proves the globally finite faithfully flat rank-two base
change, the staged-Rees base change, the root-coordinate isomorphism only on
`D(rho)`, and the universal total/D1 primitive and tail identity.  The next
report transports only `(a,c,r)=(2,3,>=2)`.  The D1 artifacts close the
strict unique-`AC` endpoint families on their D1 source, but do not supply
their maps from the actual total source.  No prior artifact located in the
search transports (0.1).

The novelty here is twofold: an exact lifecycle/transport ledger for every
reviewed strict unit-load unique-`AC` endpoint, and the finite-jet total/D1
composition for the first missing contact (0.1).

## 2. Exact endpoint ledger

Put

```text
d=c-a,  s=r-a.
```

The strict unique-`AC` criterion in the registered unit-load fan is exactly

```text
d in {1,2,3},  s>=0,  a+3*s>d,                     (2.1)
```

together with `a>=1`, `r>=2`, `c>=3`.  Its first `AC/L` grade and the
terminal endpoint grade are

```text
G=10+2*a+d=10+a+c,       T=G+d.                    (2.2)
```

For `d=1`, (2.1) is the one parametric cell

```text
a>=2, c=a+1, r>=a,
```

literally partitioned by `a=2..5`, `a=6,7`, `a=8`, `a=9`, and `a>=10`.
The union is promoted and reviewed at `85533441...` / `bd5b3dd5...`.

For `d=2,3`, the least closed `R` tail is

```text
d=2: s_min=1 for a=1,2;       s_min=0 for a>=3;
d=3: s_min=1 for a=1,2,3;     s_min=0 for a>=4.    (2.3)
```

The exact finite ledger `1<=a<=9`, written `(a,d,r_floor)`, is

```text
(1,2,2), (1,3,2),
(2,2,3), (2,3,3),
(3,2,3), (3,3,4),
(4,2,4), (4,3,4),
(5,2,5), (5,3,5),
(6,2,6), (6,3,6),
(7,2,7), (7,3,7),
(8,2,8), (8,3,8),
(9,2,9), (9,3,9).                                (2.4)
```

The lifecycle routing is exact:

| Contacts | D1 endpoint state | Immutable promotion / review |
|---|---|---|
| eleven entries of (2.4) with `a<=6`, excluding `(1,3,2)` | promoted, reviewed | `8b92c22...` / `841f0d6c...` |
| `(1,3,2)` | promoted exceptional pole-three endpoint, reviewed | `2ff74f69...` / `984783ea...` |
| `(7,2,7),(7,3,7)` | promoted load-tie endpoint, reviewed | `b5c38f1b...` / `1ae7f6d9...` |
| `(8,2,8)` | promoted load-first endpoint, reviewed | `9cc68702...` / `0558ea1e...` |
| `(8,3,8)` | target-shadow endpoint **CONFIRMED**, but no narrow promotion | review `02cbae00...` |
| `(9,2,9),(9,3,9)` | promoted grade-38 endpoint, reviewed | `551ca2f6...` / `f922fab0...` |
| all `a>=10,d=2,3,r>=a` | promoted closed source ceiling, reviewed | `470ea478...` / `f75d885d...` |

Thus every strict unique-`AC` D1 endpoint is independently reviewed.  The
old `d=2,3` union audit/review remains lifecycle-conditional because it
predates the completed `(8,3,8)` review, and no updated narrow promotion was
found.  This ledger records that distinction; it does not silently promote
the union.

Every row is endpoint-compatible with the formal Kummer primitive/tail
identity, but **endpoint-compatible is not total-transported**.  Before this
report, the only banked total contact was

```text
(a,c,r_floor)=(2,3,2),  d=1, G=15, T=16.
```

All other rows still required a finite-jet map and current actual-row
custody at their terminal grade.

## 3. The minimal uncovered contact

Use either of the two explicit well-orders

```text
K_val=(a,c,r_floor),
K_grade=(G,a,c,r_floor),                              (3.1)
```

with lexicographic comparison.  The two `a=1` endpoints `(1,3,2)` and
`(1,4,2)` precede the already transported `(2,3,2)`; they are not silently
discarded.  In both orders, the first baseline strictly after `(2,3,2)` is

```text
(a,c,r_floor)=(2,4,3), d=2, G=16, T=18.             (3.2)
```

This is (0.1).  After the composition below, the next untransported contact
in valuation order is `(2,5,3)`, with `d=3`, `G=17`, `T=20`.

## 4. Rings, maps, opens, and saturations

Let `U_18^rho` be the finite actual-total raw polynomial ring through grade
18 from the Kummer report after

```text
p0 -> -2*rho^2,
```

and let

```text
I^tot_18=([sigma^g]Phi_l : 0<=g<=18, 1<=l<=7)
```

be its literal seven-row ideal.  Let

```text
S_tot={(rho*k*J)^n:n>=0}.                            (4.1)
```

On a Keller source `J` is a unit, so `S_tot^{-1}` is the campaign's
`D(rho*k)` source.

Let `D_22` be the finite polynomial ring of block `B22` in the frozen
low-`a`, `d=2,3` compiler.  Its moving connection and Hensel-root quotient
are

```text
P=p+2*ell1*sigma+2*ell2*sigma^2,
lambda(sigma)=lam+rho1*sigma+rho2*sigma^2,

H_root=(p+2*lam^2,
        2*lam*rho1+ell1,
        rho1^2+2*lam*rho2+ell2).                    (4.2)
```

Write `B_22=D_22/H_root` and localize at `lam*k0*au*cv`.  The factors have
the exact meanings: `lam` is a chosen squarefree root, `k0` is the unit
load, and `au,cv` are the nonzero leading exact-`A,C` scalars.  The reviewed
compiler needs only `lam,cv,k0` to make the terminal residue a unit, but
exact contact also has `au!=0`.

The `+` finite-jet map

```text
delta_22^+ : U_18^rho -> B_22[1/(lam*k0*au*cv)]
```

sends `rho -> lam`, retains `ell1,ell2`, and has the following nonzero
contact coordinates:

```text
aaa1 -> a1D,       az3 -> a1D_1,       az4 -> a1D_2,
aaa0 -> a0D,       ac3 -> a0D_1,       ac4 -> a0D_2,

ez4 -> 2*c1D,      ez5 -> 2*c1D_1,     ez6 -> 2*c1D_2,
ec4 -> 2*c0D,      ec5 -> 2*c0D_1,     ec6 -> 2*c0D_2,

cs3 -> b1,         rs3 -> 4*b0,
k -> k0,
k6 -> k60,         k2 -> k20,
(mu2,mu4,mu6,J) fixed.                               (4.3)
```

It kills every lower contact jet

```text
cs,cs1,cs2, rs,rs1,rs2;
a1,aa1,a0,aa0;
c1,e1,ee1,ez3,c0,e0,ee0,ec3,                        (4.4)
```

and later jets that cannot enter through grade 18.  The factors `2` and `4`
are forced by the actual-total source formulas.  Indeed (4.3) gives

```text
c_total=sigma^5*b1,
r_total=P^2/4+sigma^5*b0,
n3=sigma^5*A_z, n2=sigma^5*A_c,
Ezseries/2=sigma^4*C_z, Ecseries/2=sigma^4*C_c,      (4.5)
```

which are exactly the `B22` D1 source arguments.  Polynomial functoriality
of the already proved universal primitive/tail identity therefore gives

```text
delta_22^+([sigma^g]Phi_l^tot)
  =[sigma^g]Phi_l^B22,  g<=18, 1<=l<=7.             (4.6)
```

The `-` map sends `rho -> -lam`; equivalently it is obtained from (4.3) by
the deck involution and swaps all root labels.  It is not discarded by a
symmetric saturation.

For exact naming of the contact saturation, let `V_2243` be the ideal of
the lower-jet vanishings (4.4), adjoin `au,cv` and one of the allocation
ideals in (5.2), and put

```text
E_22^epsilon =
  (I^tot_18+V_2243+H_root+Alloc_epsilon)
      : (rho*k*J*au*cv)^infinity, epsilon in {+,-}. (4.7)
```

No leading coefficient of `R` is inverted: (4.7) is the closed tail
`ord(R)>=3`.  The staged Rees chart saturations remain exactly the six
`K^rho_(m,f)` named in the Kummer report (`f=rs,cs,c0,c1` at stage one and
`f=a0,a1` at stage two).  Equation (4.7) is a downstream contact
saturation, not a proof that those Rees charts or their terminal receiver
are covered by this contact.

## 5. Actual grade-18 custody and finite-jet completeness

The current actual-total builder is

```text
5941bf876e3ace184190130841046ccc2573615be5cc159608698c5bbdcac36d
  cases/max12_812_order2_p0_total_rees_j2_a1_boundary_prolong_g18_v33_20260827/
  prolong_boundary_g18_v33.py
```

It constructs the general-`rho` source series, all three loads, the frozen
569 tails, and all seven total rows through grade 18 before imposing its
unrelated ordered-`a1`, `rho=0` face.  Its exact-Q result and compiled result
are frozen at

```text
22018489bbf27c91d5d973ac6e2ec00780fa079e6b07b6d386ce45dc5737de1f
22f64fbb9d2107508f7218a9aabaea03d6c502219baef84bb918352f7e38df0f.
```

Only the specialized `rho=0` face rows are serialized.  This report does
not call those bytes general-`rho` rows.  General-`rho` equality is (4.6),
the formal source identity; V33 supplies current custody that the actual
total producer follows that construction through grade 18.

The exact `B22` source inventory is

```text
G=16, T=18, primitive_count=4, maxpole=2,
jet maxima: p=2, A=2, C=2, R=0, k10=0,
            k6=0, k2=0, mu2=0, mu4=0.              (5.1)
```

Thus every arbitrary total DVR arc satisfying (0.1) factors through (4.3)
at the finite row level: discarded later jets cannot enter grades 16--18.
This is not the false assertion that its full infinite series factors
through the quotient setting those jets to zero.

## 6. Both orientations and the terminal obstruction

At the contact-leading level, the root-value coordinates are the shifted
pairs

```text
R0plus/minus = rs3/4 +/- rho*cs3,
C0plus/minus = (ec4 +/- rho*ez4)/2,
A0plus/minus = aaa0 +/- rho*aaa1.                  (6.1)
```

The stage-zero pairs `(rs,cs)`, `(c0,c1)`, and `(a0,a1)` vanish here.  They
must not be substituted for (6.1).

Put `L=z^2+p/2=z^2-rho^2`.  The grade-16 primitive is
`(3/4)AC/L`; it forces `L | A0*C0`.  Since `L` is squarefree on `D(rho)`
and the exact leading `A0,C0` are nonzero linear polynomials, the exhaustive
allocations are

```text
Alloc_+ : A0=au*(z-rho), C0=cv*(z+rho),
Alloc_- : A0=au*(z+rho), C0=cv*(z-rho).             (6.2)
```

They multiply to `au*cv*L`, and the deck exchanges them.  With

```text
lambda0=epsilon*rho,
lambda1=-ell1/(2*lambda0),
lambda2=-(ell2+lambda1^2)/(2*lambda0),              (6.3)
```

the series `lambda(sigma)` satisfies `lambda(sigma)^2+P/2=0` through the
charged terminal grade for either `epsilon=+1` or `-1`.

The four complete polar primitives through grade 18 are

```text
(3/4) AC/L            at grade 16,
(5/32) k*A^2/L        at grade 18,
(5/8)  k*R*C/L        at grade 18,
(3/8)  C^2/L^2        at grade 18.                 (6.4)
```

The reviewed moving pole-two functional is

```text
Psi=Phi4+lambda(sigma)*(Phi3+(P/4)*Phi1).           (6.5)
```

For each orientation, its coefficients at grades 16 and 17 vanish, while

```text
[sigma^18]Psi=(3/2)*lambda0^2*cv^2
             =(3/2)*rho^2*cv^2.                   (6.6)
```

Rows 1, 3, and 4 are target-free through 18.  Expression (6.6) is a unit on
the exact-contact open.  Hence each saturated ideal `E_22^epsilon` in (4.7)
is the unit ideal, proving (0.1).  This is an arcwise/set-theoretic
exclusion; no common reduced-scheme structure is asserted for the endpoint
union.

## 7. What the ledger does and does not cover

After this report, the exact total-transport ledger begins

```text
(2,3,>=2): transported, pending hostile review;
(2,4,>=3): transported here, pending hostile review;
(2,5,>=3): first remaining valuation baseline, T=20;
all other reviewed strict unique-AC endpoints: D1-reviewed but their
  individual total finite-jet manifests are not yet banked.             (7.1)
```

This is not yet a cover even of the strict unique-`AC` fan, and strict
unique-`AC` is itself only one part of the generic-square fan.  The primary
`C2`, `R3`, `RC`, and `A2` cells, every equality intersection, the special
`RA2=A2=R3` locus, the exact-square zero-normal receiver, positive-order
loads, `V(k)`, and the staged terminal receiver remain separate.

The next contact `(2,5,>=3)` requires actual-total construction custody
through grade 20.  Formal source naturality alone must not be relabeled as a
current actual-row exporter.  If no such frozen custody exists, the exact
next missing lemma is:

> **`ACT-TOT-G20`.**  The current actual-total producer constructs all seven
> unspecialized general-`rho` rows through grade 20 before any face quotient,
> from the same frozen source series, loads, targets, and 569 tails.

No new saturation should be launched for `(2,5,>=3)` until that documentary
interface is exact.

## 8. Ramified fibre and the two `G2` obligations

The Kummer algebra remains globally faithfully flat at `rho=0`, but the
three root-coordinate determinants vanish there.  Equations (4.3), (6.1),
and (6.2) use the inverse root transform only on `D(rho)`.  The ramified
fibre, its four `J1` charts, two `J2` charts, and separate terminal receiver
are untouched.

The global labels remain disjoint:

```text
G2-PSC = GGV packet/corner -> decorated Sigray pole-tree
         transport and fidelity;

G2-BD  = bounded delay/carrier after a residue-A configuration
         has already been reached.                              (8.1)
```

This local source-row composition supplies neither.  In particular, a
reviewed local endpoint cannot be used backward as a source-to-landing
theorem.

## 9. Outcomes and stop rule

Name this discriminator **`KGT-DRHO-UAC-A2D2`**.

- **PASS** (observed): both well-orders select (3.2); all pins, shifts,
  Hensel equations, source sentinels, endpoint inventory, orientations, and
  residue agree.  Bank only (0.1), mark `(2,4,>=3)` transported pending
  hostile review, and stop its algebra.
- **FAIL:** freeze the first hash, ledger wall, jet, source, orientation, or
  residue mismatch; quarantine this contact import and repair the interface
  before any contact saturation.

For the next contact:

- **G20-CUSTODY-PASS:** only then compose `(2,5,>=3)` by an explicit
  terminal-grade-20 map.
- **G20-CUSTODY-FAIL/ABSENT:** freeze `ACT-TOT-G20` as the minimal missing
  transport lemma and stop; do not substitute `rho=0` row bytes or a formal
  emitter for actual-total custody.

The desk replay is

```text
0c124179041b1a3cc115e24d1e5bce4f7ca9edcbc0e3224c302dd20d85b8867e
  xmodel/max12-812-order2-gate-t-drho-unique-ac-ledger-a2d2-composition-replay-20260827.py

python3 xmodel/max12-812-order2-gate-t-drho-unique-ac-ledger-a2d2-composition-replay-20260827.py
```

It returns

```text
PASS-DRHO-UNIQUE-AC-LEDGER-A2D2-COMPOSITION-DESK-REPLAY
```

in about `0.1 s`, with no CAS or AWS job.

## 10. Firewall

This report proves one new contact exclusion after named upstream gates and
records an exact endpoint ledger.  It does not prove the stale `d=2,3`
union audit promoted, a strict unique-`AC` total cover, a complete
generic-square fan cover, an equality face, another primary face, a Rees
chart or terminal receiver, positive-order load routing, `k=0`, the
ramified fibre, source-to-landing coverage, `G2-PSC`, `G2-BD`, Gate T,
order two, `(8,12)`, maximum twelve, JC2, or a counterexample.
