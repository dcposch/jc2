# HOSTILE GATE — descent invariance under Proposition 6.3 — Sol 5.6 — 2026-09-06

## Verdict first

**OVERALL: CONFIRMED-WITH-FIX.** The unamended claim is not promotable, but the
typed repair below is. Identities (I1), (I2), (I5), and (I6) are confirmed on
their stated copied/transported ranges. The actual-stabilizer version of (I4)
is confirmed after a type correction, and its apparent `s >= 4` gap closes.
(I3), however, is **REFUTED AS WRITTEN** once the frozen orbit-transport
convention reserves `N` for an actual centre-orbit size: that orbit size is not
fixed by descent. The repaired invariant is Moh's pair of bottom root-count
quantities

```text
B_g := (n/d_2)V_2,       B_f := (m/d_2)V_2,
```

and these do satisfy `B'_g=B_g`, `B'_f=B_f`. Also, Moh's `A_1` is a
**relative denominator increment**, not the total centre-orbit size. With
`A_1^act := den(L_act delta_1)`, where `L_act` is generated only by nonzero
coefficients of the actual outer centre, `A'_1=A_1^act` at `u_s=1` for every
length. Total orbit sizes need not be equal.

The producer's broad corollary needs the same scope repair. Arithmetic
expressions literally identified by (I1)--(I6) transport. This does **not**
give parent counterparts to child finite-line integrality, independently
enumerated child completions, or the child's own Galois residue conditions.

Per-identity verdicts:

| item | verdict | promoted reading |
|---|---|---|
| (I1) | **CONFIRMED** | raw copied characteristic data scale by `c=u_s/d_s`; an ineffective `n'-1` tail may then be dropped |
| (I2) | **CONFIRMED** | radius identity for a fixed licensed first-support route |
| (I3) | **REFUTED AS WRITTEN** | `V'_2=V_2` and `B'_g=B_g`, `B'_f=B_f`; never rename these counts `N` |
| (I4) | **CONFIRMED-WITH-FIX** | equality of actual relative increments; not equality of total orbit sizes |
| (I5) | **CONFIRMED** | ratio at every matched level; degree pair guaranteed equal only on the copied range, with no converse asserted |
| (I6) | **CONFIRMED** | exponent formula and contradiction of the typed simple/minor `(SD)` cell |
| corollary | **CONFIRMED-WITH-FIX** | only the transported arithmetic subfamily; child-only tests remain child-only |

## 1. Custody and method

Before any mathematical read, I extracted the numbered
`charged_input_<i>_sha256` / `_basename` pairs from
`xmodel/descent-invariance-gate-sol56-20260906.run.v2` with `awk`, wrote the
mechanical manifest, and ran `sha256sum -c` against
`/tmp/jc2-lane.qOmz6C/inputs`: **7/7 OK**. The manifest SHA-256 is
`d6e4132f2b4da222d16d81cc25053ee3f6484ddf9ce233a4d15fb7602029be86`.
All paper citations below were checked on page images rendered from the charged
PDF; printed page equals PDF ordinal plus 139.

The tested executable was the repo import copy of `box/lib/descend_own.py`,
which is byte-identical to the frozen charged copy, SHA-256
`3fbb5bb885acbd7f50f307ac083a762020b7ca1158e18d06a84a0325b2a3dcc2`.
Its unavoidable imports `box/lib/own_v_routes.py` and `box/lib/__init__.py`
were runtime dependencies only, not independent mathematical evidence. Exact
rationals were used throughout. Full per-row data are in
`box/descent-invariance-gate-20260906/tests.json` (63,971 bytes; SHA-256
`83a320ae7e000927af4081ecc5f9a8c5978041f1439ab8c830ef7754eb531320`).
No fleet, ledger edit, `jc2-lean`, or `ideation-*` input was used.

## 2. What the print actually says

Moh p.150 defines `d_1=n`, `d_{i+1}=gcd(n,M_1,...,M_i)`, the characteristic
`M_i`, and `mu_i=lambda_i/d_i`. Definition 5.1(2)--(4), p.179, supplies the
`V` inequalities, the rational radius formula, and Proposition 4.6 parameters.
Proposition 4.6, p.170, makes the two ODE degrees

```text
P_i = V_{i+1} d_i/d_{i+1},
Q_i = V_{i+1}(n-M_i)/d_{i+1}.
```

The p.171 Remark says the proof remains verbatim for Jacobian `x^l`, with
condition (3) replaced by `(3)*`, whose numerator is `-1-l+delta`. Lemma 6.2,
pp.196--197, is an exact inversion statement: the two truncated Puiseux series
determine one another, and membership in each `1/p` Puiseux subfield is
equivalent. This exact field statement is what upgrades denominator
divisibility to equality for actual supports in Section 3.4 below.

Proposition 6.3, p.197, uses `y^{-1}=theta`, `gamma=theta^(1/u_s)`,
`z=y-bx-e`, and a root `sigma=c(gamma)+pi gamma^{v_s}`. Thus the declared map is

```text
y = gamma^{-u_s},
x = (gamma^{-u_s}-e-c(gamma)-pi gamma^{v_s})/b.
```

It gives `x_pi=-gamma^{v_s}/b`, `y_gamma=-u_s gamma^{-u_s-1}`, hence

```text
J_{gamma,pi}(x,y)=-(u_s/b) gamma^{v_s-u_s-1}.
```

This is exactly conclusion (3) printed on p.197. The p.198 proof display is
corrupt twice: it prints `x_pi=-1/(b gamma^{v_s})`, then prints a final
reciprocal power which is not even the determinant of that displayed matrix.
The theorem statement and direct differentiation agree; no negative Jacobian
exponent is licensed. Put

```text
ell=v_s-u_s-1,       H=ell+1=v_s-u_s.
```

## 3. Re-derivation of (I1)--(I6)

### 3.1 (I1): scalar transport of the raw characteristic lattice

Proposition 6.3(2) prints the monic `pi`-degrees
`u_s n/d_s, u_s(-mu_1)/d_s, ..., u_s(-mu_{s-1})/d_s`. With
`c=u_s/d_s`, these are `n'=cn` and `mu'_i=c mu_i`. Since
`mu_1=M_1=-m`, also `m'=cm` and `M'_1=cM_1`.

The remaining claims follow without a circular gcd assumption. From p.201(5),
`d_s` divides `n,M_1,...,M_{s-1}`. Therefore
`d'_2=gcd(cn,cM_1)=c d_2`. Inductively, the p.150 recurrence

```text
mu_i=(d_{i-1}/d_i)mu_{i-1}+M_i-M_{i-1}
```

first gives `M'_i=cM_i`, and then the gcd definition gives
`d'_{i+1}=c d_{i+1}`. Hence all raw copied `M,d,mu` data scale by `c`,
`d'_s=u_s`, and `n'/d'_2=n/d_2`, `m'/d'_2=m/d_2`. If the last raw value is
`M'_{s-1}=n'-1`, p.174's Definition--Remark drops that ineffective tail; the
identity concerns the raw Prop.6.3 list before this deletion. **Confirmed.**

### 3.2 (I2): radius transport

Write the unscaled Definition 5.1 radius as `delta_i=1-F_i`. Repeating its
proof with p.171 `(3)*` replaces the unit-Jacobian normalization by
`delta'_i=(ell+1)(1-F'_i)`. For copied indices, the scalar in (I1) cancels from
each quotient `F'_{i-1}/F'_i`; consequently `F'_i=rho F_i` for one constant.

Fix the typed first nonzero source level `j`, with
`epsilon=delta_j>0`. Lemma 6.2 and the explicit inversion give the at-level
value `delta'_j=v_s-u_s/delta_j`. Solving for `rho` and then returning to all
`i<=j` yields

```text
delta'_i = (v_s-u_s) - (u_s/delta_j)(1-delta_i),
delta'_j = v_s-u_s/delta_j.
```

This compares radius values on one licensed route; it does not identify a
flag, physical place, and cover series. The five p.207 controls reproduce the
printed child radii exactly. **Confirmed.**

### 3.3 (I3): bottom `V`, Moh counts, and the fatal `N` collision

For the reduced, nonzero-centred selected `D_1` route, inversion preserves its
root multiplicity, so the licensed own-data rule has `V'_2=V_2`. This is not a
naked conclusion of Proposition 6.3: it consumes the fixed nonempty route and
the reduced-source hypothesis. Combining it with (I1) proves

```text
B'_g=(n'/d'_2)V'_2=(n/d_2)V_2=B_g,
B'_f=(m'/d'_2)V'_2=(m/d_2)V_2=B_f.
```

Those are the quantities in Moh's bottom tests (12)/(13), p.201. They are not
the `N` of the frozen orbit-transport gate. In R001, for example, the first
active exponent is `epsilon=2/7`: the actual selected-centre orbit denominator
is 7 before descent and 2 after descent, while `(B_g,B_f)=(6,4)` on both sides.
All 15 tested rows similarly had unequal selected-centre orbit denominators.
Thus `N'=N` is false under the mandated actual-orbit meaning of `N`.
**As written, (I3) is refuted; the `B_g,B_f` repair is confirmed.**

### 3.4 (I4): actual bottom increment, and closure of the `s>=4` gap

Type the objects first. Let `E` be the nonzero exponent support of the actual
outer centre above level 1, let `L_act` be its denominator-lattice index, and
define the relative bottom increment

```text
A_1^act = den(L_act delta_1).
```

Zero coefficients do not enter `E`; Moh's coarse l.c.m. of every printed
radius is a different object. The total orbit size after adjoining the bottom
term is `L_act A_1^act`, not `A_1^act`.

Let the first active exponent be `epsilon=a/b` in lowest terms. Since it lies
in `E`, write `L_act=bC`. At `u_s=1`, the active exponents transform by

```text
phi(q)=H+(q-1)/epsilon.
```

Lemma 6.2(1),(2) makes this an equality of actual truncation fields, not just a
formal denominator bound. Expressing the active exponents over denominator
`L_act` shows their image lattice has exact index
`L'_act=aC=aL_act/b`: a common divisor left in the image numerators would
either contradict that the original active numerators generate `L_act`, or
divide both coprime `a` and `b`. Finally, by (I2),

```text
L'_act delta'_1
 = aC H - bC(1-delta_1)
 ≡ L_act delta_1                         (mod Z).
```

Therefore `A'_1=A_1^act` for every `s` at `u_s=1`. This identifies the
producer's unexplained factor `L''` as the actual quotient `C=L_act/b`; it may
be greater than 1 when `s>=4`, but it causes no gap. The earlier proof obtained
only `A'_1 | den(b_j delta_1)` because it inserted zero-route denominators into
a coarse l.c.m. The gap is **real for that coarse proof and closed for the
sound actual-support convention**.

R001 is also the type negative control: `L_act=7`, `A_1^act=3`, while
`L'_act=2`, `A'_1=3`. Relative increments agree, but full bottom orbit sizes
are `21` and `6`. Calling `A_1` an actual total orbit size would therefore make
the identity false. **Confirmed-with-fix.**

### 3.5 (I5): ODE degrees

At any matched level, (I1) gives

```text
P'_i/Q'_i=d'_i/(n'-M'_i)=d_i/(n-M_i)=P_i/Q_i.
```

If `i+1<=j`, the own route copies `V'_{i+1}=V_{i+1}`, so the individual
definitions on p.170 also give `P'_i=P_i` and `Q'_i=Q_i`. At the child top,
`lo'=d'_{s'}/(n'-M'_{s'})=lo_{s-1}`. The phrase "on the copied range only"
is an assertion boundary: no equality is promised outside it, but neither is
an iff/non-equality theorem. The p.171 Remark licenses the same ODE form for
`J=C gamma^ell`; it does not identify independently chosen child factor
patterns or residues. **Confirmed on that scope.**

### 3.6 (I6): second descent and the contradictory cell

Call the multiplicity chosen for the second descent `h`, to keep it distinct
from the first `u_s`. Composing the second Prop.6.3 Jacobian factor with
`gamma^ell` gives

```text
l'' = (v'-h-1)-h ell.
```

For a simple point `h=1`, `v'=d'_{s'}-1` and (I1) gives

```text
l'' = u_s d_{s-1}/d_s - d_s + 2u_s - 2,
l'' = d_{s-1}/d_s-d_s                         when u_s=1.
```

At `u_s=1`, Definition 5.1 at the deleted source top gives, with
`X=n-M_{s-1}`,

```text
delta'_{s'}=-1  iff  X=d_s(d_s-1).
```

Now enter the `(SD)` cell only after checking all its types: child top radius
`-1`, a simple point, `l''<0`, and MINOR. Put `w=d_{s-1}/d_s`. The exponent
inequality gives `w<d_s`; minority gives
`1<=lo'=w/(d_s-1)`. Hence `w=d_s-1` and `P'/Q'=lo'=1`.

The p.171/Proposition 4.6 equation reduces to
`D(P',Q',p,q)=c p`, `c!=0`. At a simple root of `p`, Proposition 4.6 makes
`q` simple there too, and the lowest coefficient is proportional to
`P'-Q'`; it vanishes when `P'=Q'`, contradicting `c!=0`. Thus the typed cell
is logically empty, not merely absent from the census. Heavy second descent
`h>=2` and its radius licence remain outside this result. **Confirmed.**

## 4. Executable tests

The complete licensed `u_s=1`, nonempty-route frame has 46 rows. Moh's five
p.207 controls are `R001,R002,R003,R004,R007`. To avoid control overlap, I
sorted the other 41 row IDs and drew ten without replacement using Python
`random.Random(20260906)`, with no redraw:

```text
R036 R031 R046 R060 R013 R008 R050 R027 R005 R009
```

Every row was reconstructed from its frozen source `(n,m,s,M,V)` by the
charged `descend_own`. For each route the checker independently recomputed the
raw scalar lattice, affine radii, `B_g,B_f`, the actual support lattice and
bottom increment, every ODE degree pair/ratio, `lo'`, `l''`, the top-radius
lattice equivalence, and `(SD)` membership.

| cohort/test | result |
|---|---:|
| all six repaired identities, five p.207 rows | **5/5** |
| exact p.207 tuple `(n',m',M'_2,V'_2,delta'_1,delta'_2,ell)` | **5/5** |
| all six repaired identities, random complete rows | **10/10** |
| actual relative increment `A'_1=A_1^act`, combined | **15/15** |
| ratio every level and degree pair on copied range | **15/15** |
| typed `(SD)` kill cell occupied | **0/15** |
| actual selected-centre orbit size unchanged | **0/15** (required negative control) |

The five printed child rows were reproduced as

```text
R004 (16,12,13,3; 1/4,-1; ell=1)
R001 (21,14,16,2; 7/6,-1/2; ell=1)
R007 (21,14,18,5; 1/3,-1; ell=1)
R003 (15,10,11,3; 1/2,-1; ell=2)
R002 (15,10,11,2; 4/3,-1; ell=2).
```

The random draw includes two `s=4` rows, R060 and R027; both satisfy the
actual (I4). As a supplementary non-random check, the same checker passed all
six repaired identities on **46/46** complete rows. In four of them
(`R019,R040,R048,R059`) the child's coarse l.c.m. differs from its actual
support lattice, directly demonstrating why the convention matters even
though the bottom increment happens still to agree.

## 5. Exact boundary of the corollary

The promotable corollary is:

> For a fixed nonempty licensed Prop.6.3 route, every parent arithmetic
> assertion whose child expression is literally identified by (I1)--(I6)
> retains its truth under transport. In particular the repaired Moh bottom
> divisibility test uses the same `B_g,B_f,A_1^act`; copied ODE degree data are
> the same; all matched degree ratios are the same; and the typed simple/minor
> second-descent kill cell is contradictory.

It does **not** say any of the following:

* a child route exists when `descend_own` returns an empty set;
* necessary configurations or factor packets are in bijection;
* child finite-line multiplicity or integrality has a parent counterpart;
* the child's own Galois residues at new/uncopied levels follow from parent
  residues;
* passing the transported values lets one skip independent child tests;
* a necessary row is attained by a polynomial pair; or
* heavy second descent or the `u_s>1` terminal prefix is licensed.

This is exactly compatible with the frozen orbit-transport gate: transported
**values** may agree while child configuration existence and child-only
arithmetic remain new constraints. The producer's sentence "every printed
finite numerical condition" is too broad unless read as shorthand for the
transported subfamily just listed. The stronger reading is refuted.

## 6. Promotion decision and FALLACY-v2 audit

**Do not promote the unamended statement. Promote the repaired typed lemma.**
Required edits are: reserve `N` for actual centre-orbit size; write `B_g,B_f`
in (I3); define `A_1^act` as a relative increment over `L_act`; replace the
`s>=4` OPEN by the active-lattice proof above; read (I5)'s copied range as a
guaranteed scope rather than an iff; and narrow the corollary to expressions
actually transported.

FALLACY-v2 controls pass after those edits. Flags, places, series, Moh bottom
counts, total orbit sizes, and relative increments are separately typed.
The p.198 defect is checked against the declared variable map. Prime marks are
generation labels; derivatives in the ODE are derivatives with respect to
`pi`. The `(SD)` pole/interior argument is entered only after the radius,
simple-point, and minor-vertex hypotheses. No representative is treated as an
actual pair, and no floor is promoted to attainment. No new exit-price
assertion is made, so no exit-charge declaration is applicable.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15697`.
- Body SHA-256:
  `769c3ba68ec6a8e58eafb484ac8b324047e1c70d2017ca27ff9c5ff9ab28ddb3`.
- Frozen basis: `81ac7b6553dd0d57e613bddbb1315fee509667c2`.
