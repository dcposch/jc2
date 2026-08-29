# Gate T: finite-flat Kummer descent and a bounded source-row bridge

Date: 2026-08-27

Status: **DERIVED-HERE ELEMENTARY INTERFACE THEOREM AND DESK-REPLAY PASS FOR
THE SEVEN ACTUAL-TOTAL / CHARGED-`D1AC` RAW ROWS AT GRADE 15.  THE SAME
FORMAL SOURCE IDENTITY COVERS GRADE 16, BUT NO FROZEN ACTUAL-TOTAL GRADE-16
EXPORT WAS LOCATED.  HOSTILE REVIEW IS REQUIRED.  NO WHOLE DECK/SQUARE,
RAMIFIED-FIBRE, GATE-T, ORDER-TWO, MAXIMUM-TWELVE, OR JC2 VERDICT.**

## 0. Outcome

There are two different interfaces in the phrase “deck/square bridge,” and
they must not be conflated.

1. The scalar extension

   ```text
   k[p0] -> k[rho],                 p0 |-> -2*rho^2                 (K)
   ```

   is globally finite faithfully flat, including over `p0=rho=0`.  Therefore
   literal source quotients, both staged Rees algebras, their Proj blowups,
   and their standard charts commute with this base change.  This removes a
   possible *base-ring/Rees* mystery.
2. The root-value coordinates used by the generic-square clients are regular
   only on `D(rho)`.  Their determinants are multiples of `rho`.  Thus the
   generic `D(rho)` comparison is clean, but it gives no regular root chart on
   the ramified fibre `rho=0`.  That fibre remains the separate six-chart
   staged Gate-T problem plus its terminal receiver.

On `D(rho)`, the root-value map sends

```text
J1=(rs,cs,c0,c1)       to (Rplus,Rminus,Cplus,Cminus),
J2=(a0,a1)             to (Aplus,Aminus).                         (0.1)
```

For one charged generic-square source, the desk replay obtains a concrete
positive result: the universal unsplit total emitter specializes **exactly**
to the frozen `D1AC` emitter.  All seven coefficient primitives `F0,...,F6`,
all three loads, all four targets, and the canonical 569-tail polynomial are
the same.  Functoriality gives equality of every formal raw row under the
map.  In particular, it gives a concrete equality for all seven frozen
actual-total grade-15 rows and the charged `D1AC` grade-15 rows.  The formal
identity also covers the seven `D1AC` grade-16 rows, but those are not called
an actual-total comparison until a grade-16 total export is frozen.  The
grade-15 result is exact, not a parity inference or radical comparison.

The bridge is not thereby globally closed.  Other generic-square clients
still need their finite source/presentation maps checked, downstream
analytic auxiliary relations must retain their reviewed provenance, and the
ramified fibre has no regular root-coordinate inverse.

## 1. History check and novelty boundary

Close-synonym searches covered `deck-equivariant`, `deck/square`,
`generic-square overlap`, `root-value`, `rho-even`, `Rees base change`, and
`finite etale descent`.  The closest charged artifacts are:

```text
3518ac6c1505098a7b9e19c7b7ca2610dce42ff741e3f39065d0618b926ddb10
  xmodel/max12-812-order2-p0-dk0-support-exhaustion-ramified-closure-design-20260826.md

6995a991b1e7803a26bbf5374b10d54a0cda7d17158ad9f1595db76218aadb92
  xmodel/cross-iterated-blowup-cech-valuative-propagation-20260826.md

5e91571d84b1bae92306bad0a31924a2b4fe3bf183ee8d75ace558bc2dd52c0d
  xmodel/max12-812-order2-p0-total-rees-t-rs-implementation-audit-codex-20260826.md

e645d822aa49199b69464f98b7b94846e6773e635bd389cb94a3a24806a3e341
  xmodel/ideation-20260826T2350Z-crosspollination-opus5.md

7b83e24c00e1b5e2c76f41590806596c586fa067102882677e740b7978983e6b
  xmodel/max12-812-order2-square-d1-tied-a1c5r2-maxpole2-hostile-review-grok-20260826.md
```

The first two pose the `D(rho)` comparison as an obligation.  The third
recovers the root-value formulas but does not instantiate an unsplit source
map.  The fourth proves an isotypic/Reynolds certificate lemma and explicitly
warns that invariance does not identify the charged receiver.  Individual
generic-square reports use finite-etale descent after splitting `p`, but no
located artifact composes the global finite-flat Kummer map, the two staged
Rees ideals, the root-coordinate matrices, and an exact frozen source map.

The new content here is precisely that composition, plus the explicit
`D1AC` source specialization and its replay.  It is not a claim that every
generic-square compiler already has this map.

## 2. Exact rings and raw-row ideals

Work over a field `k` of characteristic zero.  For a finite grade bound `G`,
let `U_G` be the polynomial `k[p0]`-algebra on `sigma`, the retained jets

```text
ell_i; cs_i,rs_i; az_i,ac_i,ez_i,ec_i;
k10_i,k6_i,k2_i; mu2,mu4,mu6,J,
```

using the frozen total-emitter names and finite ranges needed through `G`.
Set

```text
p(sigma) = p0 + 2*sum_(i>=1) sigma^i*ell_i,
c(sigma) = sigma^2*Cseries(sigma),
r(sigma) = (p(sigma)^2 + sigma^2*Rseries(sigma))/4,

n3 = sigma^3*Azseries,
n2 = sigma^3*Acseries,
n1 = sigma^3*(p*Azseries+Ezseries)/2,
n0 = sigma^3*(p*Acseries+Ecseries)/2.                (2.1)
```

The seven ordinary coefficient primitives are

```text
F6=2p,                         F5=2c,
F4=p^2+2r,                    F3=2pc+sigma^2*n3,
F2=c^2+2pr+sigma^2*n2,       F1=2cr+sigma^2*n1,
F0=r^2+sigma^2*n0.                                      (2.2)
```

For `1<=ell<=7`, let `Phi_ell` be the canonical frozen-tail polynomial in
`F0,...,F6,k10,k6,k2`, with `Lambda` replaced by `sigma^2`, minus

```text
sigma^(2*(12+ell))*delta_ell,
(delta_1,...,delta_7)=(0,mu2,0,mu4,0,mu6,J/4).       (2.3)
```

Let

```text
I_G = ([sigma^g]Phi_ell : 1<=ell<=7, 0<=g<=G) in U_G,
A_p,G = U_G/I_G.                                      (2.4)
```

This names a finite raw-row ideal.  It does not set a target or a later load
to zero unless the displayed source map does so.

## 3. The Kummer map is globally faithfully flat

Define

```text
B = k[p0,rho]/(p0+2*rho^2) ~= k[rho],
kappa : k[p0] -> B,              p0 |-> -2*rho^2.     (3.1)
```

Division by the monic polynomial `rho^2+p0/2` gives the unique normal form

```text
b0(p0)+rho*b1(p0).
```

Hence `B` is free of rank two over `k[p0]`, with basis `{1,rho}`.  It is
therefore faithfully flat.  Put

```text
U_rho,G = U_G tensor_(k[p0]) B,
I_rho,G = I_G*U_rho,G,
A_rho,G = A_p,G tensor_(k[p0]) B = U_rho,G/I_rho,G. (3.2)
```

The deck involution is

```text
tau(rho)=-rho,
tau fixes U_G.                                        (3.3)
```

On `D(p0)`, equivalently `D(rho)`, (3.1) is finite etale: `rho` is a unit
and the derivative `2*rho` is a unit.  At `p0=rho=0` it is ramified but
remains faithfully flat.  Etaleness must not be substituted for flatness at
that fibre.

For the unit-load generic open, name the multiplicative sets

```text
S_p   = {(p0*k)^n:n>=0} in A_p,G,
S_rho = {(rho*k)^n:n>=0} in A_rho,G.                 (3.4)
```

Because `p0=-2rho^2`, the base change of `S_p^(-1)A_p,G` is canonically
`S_rho^(-1)A_rho,G`.  No root value is silently inverted in (3.4).

## 4. Both staged Rees algebras and every named saturation

In `A_p,G`, define

```text
J1_p=(rs,cs,c0,c1).
```

In `Abar_p,G=A_p,G/J1_p`, define

```text
J2_p=(a0,a1).
```

Their Kummer extensions are

```text
J1_rho=J1_p*A_rho,G,
Abar_rho,G=A_rho,G/J1_rho,
J2_rho=J2_p*Abar_rho,G.                              (4.1)
```

Name the Rees algebras

```text
R1_p   = Rees_(A_p,G)(J1_p),
R1_rho = Rees_(A_rho,G)(J1_rho),
R2_p   = Rees_(Abar_p,G)(J2_p),
R2_rho = Rees_(Abar_rho,G)(J2_rho).                 (4.2)
```

Flatness gives, degree by degree,

```text
R1_p tensor B ~= R1_rho,
R2_p tensor B ~= R2_rho.                            (4.3)
```

Indeed `J^n tensor B -> A tensor B` remains injective and its image is
`(JB)^n`.  Thus Proj and every standard chart commute with (3.1).

For completeness, name the exact chart saturations.  At stage `m=1,2`, let
`f` be a displayed generator of `Jm_p`, let the other generators be `f_j`,
and use ratio variables `y_j`.  In the polynomial chart ring define

```text
P^p_(m,f) = (f*y_j-f_j : j!=f),
K^p_(m,f) = P^p_(m,f) : f^infinity,
C^p_(m,f) = A_stage,p[y_j]/K^p_(m,f).               (4.4)
```

Define `P^rho_(m,f)`, `K^rho_(m,f)`, and `C^rho_(m,f)` by the identical
formula after Kummer base change.  Equation (4.3), rather than an assumed
commutation of a guessed symmetric presentation, gives canonical maps

```text
beta_(m,f): C^p_(m,f) tensor B -> C^rho_(m,f),       (4.5)
```

and every `beta_(m,f)` is an isomorphism.  The named list is

```text
m=1: f in {rs,cs,c0,c1};
m=2: f in {a0,a1}, after quotient by J1.             (4.6)
```

Ordered-stratum equations such as `rs=0` on the later `cs` stratum are
ordinary further quotients of (4.5), so they commute as well.  The terminal
receiver is the separately named quotient

```text
A_p,G/(J1_p+(a0,a1))
```

and its Kummer base change.  Nothing in this section proves that receiver
empty.

## 5. Root coordinates: exact only on `D(rho)`

In `A_rho,G[1/(2rho)]`, define the map `psi_root` by

```text
Rplus  = rs/4 + rho*cs,       Rminus = rs/4 - rho*cs,
Cplus  = (c0+rho*c1)/2,       Cminus = (c0-rho*c1)/2,
Aplus  = a0+rho*a1,           Aminus = a0-rho*a1.    (5.1)
```

Its inverse is

```text
rs=2*(Rplus+Rminus),          cs=(Rplus-Rminus)/(2rho),
c0=Cplus+Cminus,              c1=(Cplus-Cminus)/rho,
a0=(Aplus+Aminus)/2,          a1=(Aplus-Aminus)/(2rho). (5.2)
```

The three forward determinants, in `(rs,cs)`, `(c0,c1)`, and `(a0,a1)`,
are respectively

```text
-rho/2, -rho/2, -2rho.                                (5.3)
```

Consequently `psi_root` is an isomorphism precisely on the registered
`D(2rho)` open, and (0.1) follows by equality of ideals under an invertible
linear change.  The deck (3.3) swaps every `plus/minus` pair.

At `rho=0`, all three determinants vanish.  Equations (5.1) still define a
map, but (5.2) is unavailable.  Thus no generic root-value chart may be used
to replace the ramified collision charts.  Global finite-flat Rees base
change and generic root-coordinate invertibility are different facts.

## 6. Concrete raw-row equality: total source to frozen `D1AC`

Let `D_16` be the polynomial ring used by

```text
e024a13d24a11519f70b535d4b47c47c62538a684b8bc71e79216410cd8ecb7c
  cases/max12_812_order2_square_owner_r1_d1_ac_symbolic_20260826/compile_r1_d1_ac.py
```

before its analytic auxiliary variables are imposed.  To distinguish names,
attach a superscript `D` to its `a`, `aa`, `c`, and `cc` variables.  Define
the source map

```text
delta_D1 : U_16 -> D_16
```

by the following finite table (unlisted later jets map to zero):

```text
p0 -> p,                    ell1 -> ell1,       ell_i (i>=2) -> 0;

(cs,cs1,cs2,...) -> (0,0,theta*eta*b1,0,...),
(rs,rs1,rs2,...) -> (0,0,4*theta*eta*b0,0,...),

(a1,aa1,aaa1,az3,...) -> (0,0,theta*a1^D,theta*aa1^D,0,...),
(a0,aa0,aaa0,ac3,...) -> (0,0,theta*a0^D,theta*aa0^D,0,...),

(c1,e1,ee1,ez3,ez4,...) ->
    (0,0,0,2*theta*c1^D,2*theta*cc1^D,0,...),
(c0,e0,ee0,ec3,ec4,...) ->
    (0,0,0,2*theta*c0^D,2*theta*cc0^D,0,...),

k -> k0,                   k10_i (i>=1) -> 0,
k6 -> k6,                  k6_1 -> 0,
k2 -> k2load,              k2_1 -> 0,
(mu2,mu4,mu6,J) fixed.                                      (6.1)
```

The factors `4` and `2` are load-bearing.  Substitution in (2.1) gives

```text
p = p+2*sigma*ell1,
c = sigma^4*theta*eta*b1,
r = (p+2*sigma*ell1)^2/4 + sigma^4*theta*eta*b0,

Azseries = sigma^2*theta*(a1^D+sigma*aa1^D),
Acseries = sigma^2*theta*(a0^D+sigma*aa0^D),
Ezseries/2 = sigma^3*theta*(c1^D+sigma*cc1^D),
Ecseries/2 = sigma^3*theta*(c0^D+sigma*cc0^D).       (6.2)
```

These are exactly the arguments of the frozen `D1AC`
`source_coefficients` function.  Therefore

```text
delta_D1(Fi_total)=Fi_D1             for i=0,...,6.  (6.3)
```

The current actual-total grade-15 exporter is also frozen:

```text
c965726d2308358bf01c533fe89f2e28551abd9e3549fc699cd3e36d40ac82a6
  cases/max12_812_order2_p0_total_rees_allrows_g15_export_v22_20260827/export_allrows_g15_v22.py
```

It pins the grade-13--14 total-series module
`5c233e0f2193bc4cb6384e0ad16f3d8b063494541389463853365a7ac443a587`,
builds all seven actual-total grade-15 rows, and uses the same source series
as (2.1)--(2.2) after `p0=-2rho^2`.

Both source branches call the same frozen `tail_text` function

```text
77f25216f0ab17abb3a8f4be271b2ea38f883806a72523cdca1be659df90dcdc
  cases/max12_812_order2_square_load_ladder_20260826/compile_square_load_ladder.py
```

on the same 569-tail JSON, with the same load and target maps.  Polynomial
functoriality and coefficient extraction now give the exact equality

```text
delta_D1([sigma^g]Phi_ell^total)
  = [sigma^g]Phi_ell^D1                              (6.4)
```

for every coefficient of the formal universal emitter.  At `g=15`, the V22
exporter supplies current actual-total custody, so (6.4) is a concrete
equality for all seven frozen actual-total rows and all seven charged `D1AC`
rows.  Their grade-15 raw row ideals are equal in `D_16`; no radical,
saturation, or generic-point argument is used.

The same polynomial identity gives (6.4) at `g=16` for the universal source
and the charged `D1AC` emitter.  No frozen actual-total grade-16 exporter was
located in the history search, so this report does **not** record the seven
grade-16 equations as an actual-total artifact comparison.

After adjoining

```text
D_16^spl = D_16[lambda,1/(2*lambda*k0)]/(p+2*lambda^2), (6.5)
```

identify `rho=lambda`.  Equations (5.1)--(5.3) then give both root
orientations and their deck swap.  This is the exact source-level
composition available to any already reviewed `D1AC` endpoint whose
auxiliary analytic relations have separately been proved from these raw
rows.  It does not automatically certify a different generic-square client
or an auxiliary relation absent that provenance.

## 7. Exact countermodel: deck parity is not receiver identity

Let

```text
E=k[p0,x],             I=(x),             J=(x+p0).  (7.1)
```

After (K),

```text
I_B=(x),               J_B=(x-2*rho^2) in k[rho,x]. (7.2)
```

Both ideals are fixed by `tau(rho)=-rho`, but they are unequal: the generator
of `J_B` has residue `-2rho^2 != 0` modulo `I_B`.  Hence rho-even rows,
deck-stable ideals, or an averaged certificate cannot identify a pre-existing
charged generic-square receiver.  Literal source/presentation equality such
as (6.4) is necessary.

## 8. Bounded discriminator and stop rule

Name the completed discriminator **`KRB-D1-15`**.

Inputs are exactly the six pinned files in the replay: total source compiler,
the V20/V22 current total exporters, generic-square tail compiler, `D1AC`
compiler, and 569-tail JSON.  It checks:

1. every map in (6.1);
2. equality (6.3) for `F0,...,F6`;
3. identity of load maps, target maps, and the weighted 569-tail census;
4. all three root matrices and inverses on `D(2rho)`;
5. the parity-only countermodel (7.1)--(7.2);
6. negative controls omitting the factor `4`, omitting the factor `2`, or
   omitting the moving term `2*sigma*ell1`; each must be detected.

The two possible outcomes are:

- **PASS** (the observed outcome): (6.4) follows for all seven current
  actual-total / charged-`D1AC` grade-15 rows.  Bank this exact source
  interface and stop this bounded client.  Do not spend AWS time expanding
  569 polynomial tails merely to recheck functorial substitution.  Grade 16
  remains a formal source identity until an actual-total exporter is frozen.
- **FAIL:** freeze the first unequal primitive/map/hash.  Quarantine any
  attempt to import the affected `D1AC` endpoint into Gate T.  Repair the
  source map before computing any chart saturation or invariant ring.

The replay is

```text
python3 xmodel/max12-812-order2-gate-t-kummer-row-bridge-replay-20260827.py
```

and returns

```text
PASS-GATE-T-KUMMER-ROW-BRIDGE-DESK-REPLAY
```

with a 569-tail census, all seven primitive equalities, all three inverse
matrices, and all negative controls passing.  It is desk-scale (`<0.1 s` in
the recorded run) and launches no CAS or AWS job.

### Next finite manifest, not launched

For another charged generic-square client, the same protocol is finite:
register that compiler's exact source map, its finite emitted row grades, its
chart relations, its multiplicative set, and compare the two saturated
presentation ideals in both directions.  If polynomial expansion or a
standard basis is required, shard by row and run exact `Q` plus a distinct
good-prime control on AWS only.  Stop on the first mismatch or after the
finite manifest passes.  No such heavy job is authorized or launched here.

## 9. Coverage and global-obligation firewall

This report separates three notions:

- **Gate-T ramified coverage:** the four `J1` charts, two `J2` charts, and
  terminal receiver over `rho=0`.  Sections 3--4 preserve their exact Rees
  geometry, but sections 5--6 do not close them.
- **Gate-T generic overlap:** the `D(rho*k)` comparison with charged
  generic-square root charts.  Sections 5--6 close the raw source interface
  only for the named `D1AC` grades 15--16 client.
- **Global source-to-books coverage:** neither of the above proves that every
  order-two source, still less every Keller pair, enters this post-`M=0`,
  unit-`k10` family.

Finally, the two global `G2` labels remain disjoint and untouched:

```text
G2-PSC = GGV packet/corner -> decorated Sigray pole-tree
         transport and fidelity;

G2-BD  = bounded delay/carrier after a residue-A configuration
         has already been reached.                              (9.1)
```

There is no implication in either direction.  The present Kummer/Rees
interface proves neither one, supplies no global Sigray landing theorem, no
off-family `k10=0` coverage, no whole exact-square receiver, no cofinal
complexity bound, and no JC2 conclusion.
