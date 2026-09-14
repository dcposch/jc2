# Cohort atlas: exact inventory and conditional interfaces

This auxiliary audit replays the frozen lane's cited historical sharpened
candidate cohort. It is not a new promoted census and does not reopen source
rows already killed by separate certificates. The source snapshot hash is
checked against both its upstream provenance record and the previous Astra
cohort audit before any counts are emitted. Every row is also checked against
the frozen `moh_skeleton_full.py` class: its windows and conditions (8)–(13)
hold, its terminal radius is −1, and its terminal gcd is `u_s+v_s`.

Run from the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 box/recvatlas-20260905/cohort_inventory.py
sha256sum -c box/recvatlas-20260905/cohort/new-read-inputs.sha256
```

The exact replay produces 296 source rows, 132 coarse keys, 87 rows with
`ell=1`, and 32 keys with `ell=1`. Among these 87 rows, 72 have `(u,v)=(2,4)`
and 15 have `(u,v)=(3,5)`. The Jacobian exponent alone does not certify a map
into the requested forward wedge receiver.

The same hash-checked snapshot independently reproduces Fable's `671/1110`:
all records with `phase=us_eq_1` number 1110, of which 671 have `ell=1`.
Their full exponent histogram is `{1:671,2:317,3:71,4:9,5:33,6:3,7:6}`.
This is the pre-filter snapshot cohort. Applying either stored
`xu_ok_promoted` or `xu_ok_candidate` instead gives 1076 rows and 647 at
`ell=1`. These distinct cohorts must not be silently conflated. The complete
replay is banked in `us1-residue-audit.json`; no new enumeration was needed.

| ell | Keys | Rows |
|---:|---:|---:|
| 0 | 43 | 141 |
| 1 | 32 | 87 |
| 2 | 19 | 22 |
| 3 | 11 | 18 |
| 4 | 11 | 11 |
| 5 | 6 | 7 |
| 6 | 8 | 8 |
| 7 | 1 | 1 |
| 8 | 1 | 1 |
| Total | 132 | 296 |

Coverage is deliberately typed:

* Requested literal forward wedge `deg_gamma [pi^j] <= 3j`, including
  `j=0`, with `J=c*gamma`: **0/132 certified; 132/132 UNASSIGNED**.
* Broad finite polynomial receiver with `J=c*gamma^ell`: **132/132 keys
  have a coefficient map on the licensed radius branch**, covering all 296
  licensed source charts. This is a new necessary overapproximation, not an
  identification of pre-existing terminal coefficient charts.
* Complementary split branches: **296/296 UNASSIGNED**. Every cohort row has
  `u_s>=2`; automatic radius from Moh Proposition 6.4 cannot be used.
* Source rows killed by these broad receiver certificates: **0**. Each broad
  receiver has the explicit point `P=pi`, `Q=pi+gamma^(ell+1)`,
  `c=-(ell+1)`, `rho=-1/(ell+1)`. The inventory checks that this point fits
  every declared support rectangle.

## The exact source and receiver rings

Work over `QQ`, or any field of characteristic zero. For each actual source
record, take `n,m,u,v` from its metadata and put `ell=v-u-1`. Let

```
F(X,Y) = sum_(r+s<=n) f_rs X^r Y^s,
G(X,Y) = sum_(r+s<=m) g_rs X^r Y^s,
A(gamma) = sum_(0<=r<v) a_r gamma^r,
x = beta*(gamma^(-u)-e-A(gamma)-pi*gamma^v),
y = gamma^(-u).
```

The source coefficient ring has generator order
`b,beta,e,a_0,...,a_(v-1),f_rs,g_rs`, with the two coefficient families each
ordered lexicographically by `(r,s)`. Its declared localization is represented
by the equation `b*beta-1`. The source necessary ideal contains this equation,
all coefficients of `J_XY(F,G)-1`, all negative-gamma coefficient rows of
`F(x,y),G(x,y)`, and all rows above pi-degrees `n'=nu/(u+v)` and
`m'=mu/(u+v)`, respectively. These are new enlarged source charts. Necessity
of the polynomiality and degree rows for the licensed branch is precisely
Moh Proposition 6.3, printed pp.197–198; it is not inferred from the
arithmetic metadata.

The actual source orientation is `F=source g`, `G=source T1`, with source
Jacobian normalized to `+1`. Taking all `a_r` for `0<=r<v` is a safe
enlargement of the finite sigma truncation displayed in Moh's proof. No
claim that arbitrary choices of these coefficients come from an actual
source is required.

For a coarse key, let `Bp=max(v*n)` and `Bq=max(v*m)` over its source
records. Define

```
P = sum_(0<=i<=Bp,0<=j<=n') p_ij gamma^i pi^j,
Q = sum_(0<=i<=Bq,0<=j<=m') q_ij gamma^i pi^j.
```

The common receiver coefficient ring has generator order
`c,rho,p_ij,q_ij`, each coefficient family lexicographically ordered by
`(i,j)`. Its ideal consists of all coefficients of
`J_gamma,pi(P,Q)-c*gamma^ell` and `c*rho-1`. No monicity or exact pi-degree
is imposed. The declared rectangle is finite, necessary, and deliberately
larger than all source supports. Different inherited characteristic
decorations are retained in `inventory.json`; they have not been identified.

The literal contravariant homomorphism is

```
phi(p_ij) = [gamma^i pi^j] F(x,y),
phi(q_ij) = [gamma^i pi^j] G(x,y),
phi(c) = -u*beta,
phi(rho) = -b/u.
```

Coefficient extraction is a finite polynomial expression in the declared
source generators: substituting the displayed finite sums and expanding
defines it without a solver or a matching-name convention. Extra receiver
coefficients beyond a source's support map to zero. Source support is
bounded between gamma exponents `-u*n` and `v*n` for `F`, and analogously
for `G`.

For completeness, set `LF=F(x,y)`, `LG=G(x,y)`, and let `P*=phi(P)`,
`Q*=phi(Q)` be the retained rectangles. Let `EF=LF-P*`, `EG=LG-Q*`, whose
coefficients are the discarded negative-gamma or excessive-pi rows. With
`H=J_XY(F,G)-1`, the exact identity is

```
J(P*,Q*)+u*beta*gamma^ell
 = -u*beta*gamma^ell*H(x,y) - J(EF,LG) - J(P*,EG).
```

The chain-rule determinant is `J(x,y)=-u*beta*gamma^ell`. Every coefficient
on the right is a polynomial combination of source necessary generators.
The inverse row pulls back literally as
`phi(c*rho-1)=b*beta-1`. This proves ideal containment before any receiver
emptiness is considered. Discarding either the polynomiality rows or the
excessive-pi rows would invalidate this proof.

## Three concrete interfaces

The first two are Astra's collided example. They have different inherited
characteristic sequences and different conditional terminal radii. Both map
to the same broad receiver because the explicit substitution and common
necessary ideal above prove that they do, not because the key matches.

| Source `(n,m)` | `M2..Ms` | `V2..Vs` | `(u,v)` | Key `(n',m',ell,V2')` | Inherited `M'` |
|---|---|---|---|---|---|
| (126,84) | (−14,63,124) | (5,10,5) | (2,5) | (36,24,2,5) | (−24,−4,18) |
| (126,84) | (112,119,124) | (5,10,5) | (2,5) | (36,24,2,5) | (−24,32,34) |
| (144,120) | (132,138,142) | (5,5,4) | (2,4) | (48,40,1,5) | (−40,44,46) |

For the first two rows, the licensed radius is `delta_star>=5/2`,
`A=a_0+...+a_4*gamma^4`,
`x=beta*(gamma^-2-e-A-pi*gamma^5)`, `y=gamma^-2`,
`phi(c)=-2*beta`, and `phi(rho)=-b/2`. The common target has caps
`(deg_gamma P,deg_pi P) <= (630,36)` and
`(deg_gamma Q,deg_pi Q) <= (420,24)`, with Jacobian `c*gamma^2`.
Their terminal anchors are 17 and 1; the corresponding inherited-radius
formula gives −3/17 and −3. Those different radii are preserved and are
not substituted for the licensing radius of the source minor disc.

For the third row, the licensed radius is `delta_star>=2`,
`A=a_0+...+a_3*gamma^3`,
`x=beta*(gamma^-2-e-A-pi*gamma^4)`, `y=gamma^-2`,
`phi(c)=-2*beta`, and `phi(rho)=-b/2`. Its target caps are `(576,48)`
for `P` and `(480,40)` for `Q`, and its Jacobian is `c*gamma`.
This is an actual exponent-one receiver assignment, but it is to the broad
receiver, not to the unsupported forward wedge. Its inherited terminal
anchor is 1 and its corresponding inherited terminal radius is −2.

All three rows return **UNASSIGNED** for the requested literal wedge.
All three licensed descent branches return a proved broad coefficient map.
All three complementary split branches remain **UNASSIGNED**.

The full 296 source records and all 132 common receiver declarations are in
`inventory.json`; `pilot-interfaces.json` retains the three full interfaces,
including source gcd sequences and all original rational radii. The exact
small-map algebra control is supplied by the root lane; this cohort driver
performs only exact arithmetic and inventory checks and starts no CAS jobs.
