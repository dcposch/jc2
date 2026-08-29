# Primary research — td=8 closed cv/contact gate

Lane: Grok 4.6, independent primary mathematics, not a review. Date:
2026-08-29. Object: the exact equality configuration that the Opus
exact-lambda report alleges is necessary for the reviewed td=8 equal-join
affine route to fit its shared budget.

Packet: `cases/m2_td8_cv_weight_contact_gate_grok46_20260829/`.

No access of any kind to `jc2-lean`. No web, AWS, Singular, msolve, Sage,
PARI, or other heavy CAS. Arithmetic is desk `int` / `Fraction` plus
hand-rolled polynomial lists. Canonical files were not edited. Ordinary and
`-O` tests plus ten adversarial mutations of a producer copy were run. The
Opus report was read only as an allegation. Fable's active exact-separation
review, Fable's active coefficient transport, the active td=12 trunk lane,
and later model output were not read.

Target configuration (allegation):

```text
td=8; two Lambda=4 poles;
Delta_A1=Delta_A2=Delta_trunk=2; lambda_(0,y)=0; delta_a=0;
T_{a,cv} consists exactly of weights {2,2,2,1};
each A extra-direction branch has deg(p_H)=2 at its cv vertex.
```

---

## 0. Verdict

**`CV_CONFIGURATION_FORMALLY_SURVIVES`.**

Conditional on the reviewed td=8 equal-join route and on the exact-separation
premise, until that premise passes different-model review.

1. **Item 4, first.** Budget equality does force the four-vertex set
   `T_{a,cv} = {H_{A1}, H_{A2}, H_{tr}, H_x}` of weights `2,2,2,1`, but
   *not* by printed Proposition 7.5 `(22)`. That equality, the literal
   per-puncture `delta_a`, and fixed-baseline `(22-cl)` are quarantined.
   The forcing uses actual-weight Corollary 7.1 (inequality), H3-psi, St 7.1
   integrality, and MP1 distinctness. The omitted nonnegative is `delta_a`;
   it does not add a cv vertex and is not forced to zero. Nested `Y(F)`
   versus first-exit does not merge the two A flags.

2. **Quadratic cv recursion.** Proposition 7.1 at `deg(p_H)=2` forces
   `k_j | 2` for every non-terminal step, hence `k_j in {1,2}` with `l_j`
   odd when `k_j=2`, plus the unique repaired terminal `(1,0)`. Independently,
   `Delta_A=2` (St 3.10 + the A-step numbers `D=14`, `kbar=5`, `m=2`) forbids
   a degree drop and a ramification jump on `(pi(A), pi(H)]`, so `H^circ = A`
   and `p_H` is a double root. At that parent, `M*_A=21` forces some `k_j=2`.
   A pure-power filling of the recursion collapses identically to `0`. A
   one-parameter family of fillings with a linear first remainder does not:
   any number of `(k,l)=(2,1)` steps on `p=eta^2` with `r_0 = a eta + b`,
   `a b != 0`, stays degree one. This is formal source-data, not a polynomial
   pair.

3. **Closed global census.** Two copies of table `(23)` row 4 give
   `Lambda(F)=4+4=8=td` by the promoted Proposition 5.8 replacement, hence
   no third pole (Proposition 5.7: `Lambda >= beta=3`). Each pole has exactly
   the places of formula `(18)`: `Lambda=1` at `c=0` and `Lambda=3` on the
   unique nonzero `nu=3` continuation. The four cv vertices of weights
   `2,2,2,1` meet every sum, gcd, orbit, place, and distinctness constraint
   used here. On each A-copy, Proposition 7.3 gives only the inequality
   `sum Lambda(P) >= 2`, because the root is double.

4. **Reconciliation.** The two interfaces are simultaneously realised at
   the formal source-data tier by the double-root `(2,1)`-chain together with
   the four-vertex census. The printed source does not pin the actual
   Jacobian length `m_A` of the A-vertex, nor the subtop of `f^A` at `c*`.
   Those are not needed to exhibit one legal filling, and they are not
   guessed.

Survival proves no gluing, landing, realizability, counterexample, degree
ceiling, or JC2 result. The affine family is not killed at this gate. Exact
`Delta=2` on the actual extra branches remains an extra contact statement.

---

## 1. Custody

Files read for mathematics, and only these:

| file | sha256 (full) | bytes |
|---|---|---|
| `xmodel/m2-td8-cv-weight-contact-gate-primary-grok46-prompt-20260829.md` | `6649946582fb383f305f6cfb7a2406910b81ef827bc62ad2d319a238d49c743e` | 3665 |
| `xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md` | `991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508` | 32759 |
| `xmodel/m2-td8-equal-join-route-family-sol56-20260829.md` | `9a778862816aa96d251c33aac7e98a2fb3bfc1b3fc7c83f4463ac862de31815a` | 5623 |
| `xmodel/m2-td8-equal-join-route-family-hostile-review-grok46-20260829.md` | `d3f378a1c5ed6a649b53885ce2d965c4fad4acad64b98df96ed2ed71ad6b2d8e` | 20866 |
| `xmodel/m2-td8-equal-join-exact-lambda-primary-grok46-20260829.md` | `99b136da9930c76f833de66c437ffb7ef8b07ab017e0e6719fbb7c888c16e919` | 21095 |

The Opus report is an allegation, not a lemma. The three equal-join files
are the reviewed td=8 source row and its Grok review / exact-lambda parent;
they supply the route numbers recomputed in the packet, not the cv-gate
theorems.

Printed source, on-page (`refs/sigray_full.pdf`, printed page = pdf page),
re-read as display lines for every load-bearing formula:

- pp. 10–13: Def 3.1–3.4, Not 3.1–3.8 (`nu_F`, `kappa_F`, `F^circ`);
- pp. 19–23: Prop 4.2 (with the promoted `(1,0,c)` terminal), Not 4.1,
  Prop 4.6 `(11)`–`(17)` including the exclusivity clauses;
- pp. 26–28: `(18)`, Prop 5.6 `(19)`, Prop 5.7, Def 5.1, Prop 5.8 `(20)`;
- pp. 35–38: Not 7.1, St 7.1–7.3, Prop 7.1 (the degree formula is the
  displayed `deg(r_j)=(l_j/k_j) deg(p)`), Prop 7.3, Not 7.3, Prop 7.4–7.5
  `(22)`, Cor 7.1;
- pp. 39–40: Not 8.1, Prop 8.1 head and the proof line
  `deg(p_{h_j,F})=(l_j/k_j) deg(p_F)`;
- pp. 46–49: table `(23)` row 4, Not 9.1, St 9.3 `(24)` (E6 sign), Not 9.3,
  St 9.4 `(25)`.

The stacked-fraction hazard was respected: Prop 7.1, Prop 4.6 `(11)`–`(17)`,
`(18)`–`(20)`, and `(22)`/`(24)`/`(25)` were re-read as displayed blocks
(pages 23, 35–36 rendered).

Promoted corrections used, at the quoted extent: `ladder/SIGRAY-AUDIT.md`
(Prop 4.2 complete repair, Prop 5.1 sidedness, Prop 5.8 replacement, Section 7
quarantine of printed `(22)` / literal `delta_a`); `ladder/SHEET6-AF2.md`
§§1–3 (E6, first-exit, derived AF2); `ladder/SHEET6-H3.md` §4a (H3-psi);
`ladder/SOL-PROP58.md` (every-fiber Prop 5.8); `ladder/SHEET6-MULTIPOLE.md`
MP1; `ladder/SHEET6-DEPTH.md` §1 i-normalisation, as cited. Corollary 7.1 is
the actual-weight inequality `c253bd12...` / Terra gate `727f5850...`, not
the printed Euler equality.

Packet hashes of this solve are in §8.

---

## 2. Item 4: budget equality and the four-vertex set

Printed Proposition 7.5 `(22)` is

```text
td = 1 + sum_{F in T_{a,cv}} kappa_F (pi(F)-1) + sum_a delta_a.
```

The promoted correction is that this equality, the literal per-puncture
`delta_a` of Notation 7.3, and the attempted fixed-baseline `(22-cl)` are
not established. What is promoted is actual-weight Corollary 7.1: for any
finite subset `{F_1,...,F_n}` of `T_{a,cv}`,

```text
td  >=  1 + sum_i kappa_{F_i}(pi(F_i)-1).
```

H3-psi / repaired St 9.4 `(25)` supplies the matching upper bound on
first-exit charges: `sum lambda_i^exit <= td-1-psi`. The reviewed row has
terminal `w=2/5`, `M=5`, `j=3`, `psi=ceil(M/j)-1=1`, so the ceiling is
`8-1-1=6`.

The three priced extras have floors `2,2,2` (corrected `(24)` plus the
A-step integers `D=14`, `kbar=5`, `m=2` giving gap `2`, and the trunk
integrality `3/2 -> 2`). The merge is a P2 identity: both reduced orbits are
arrivals, so `lambda_G=0` exactly. Thus `2+2+0+2=6` meets the ceiling, and
each of `Delta_{A1}`, `Delta_{A2}`, `Delta_{trunk}` is forced to exactly `2`.
There is no other y-side first-exit charge.

The x-side cluster is disjoint (other tree component) and has weight
`W_x >= psi=1`. Corollary 7.1 on the three weight-two flags plus the x-side
gives `td >= 1+6+W_x`, hence `W_x <= 1`. Combined with `W_x >= 1`, one has
`W_x=1`. Statement 7.1 plus the Prop 7.3 integrality line make every cv
weight a positive integer, so `W_x=1` is exactly one x-side cv vertex of
weight one, and a fifth cv vertex is impossible.

MP1: `sum_{r(G)>=2}(r(G)-1)=m-1=1`, so the unique 2-ary merge is the equal
join of the two chain arrivals. The two extra-direction flags cannot
reconverge, so `H_{A1} != H_{A2}`, and neither equals the trunk extra or
the x-side vertex.

`(0,y)` itself is not a cv vertex: `pi=0`, contradicting St 7.1. The
allegation `lambda_{(0,y)}=0` is the empty-exit statement on the chain
continuation, already used as the P2 identity at the merge and as the
unpriced searrow continuation to the root.

**What is not forced.** Printed `delta_a=0` is not forced. Excess
`Lambda(P) - weight` at a double root (Prop 7.3's inequality, not equality)
can be positive. That excess is not a fifth vertex.

So the four-vertex census of weights `2,2,2,1` stands, with the indexing
repair "first-exit + actual-weight" in place of "printed `(22)` + nested
`Y`". The quadratic condition on the two A-copies is a separate descent
statement, next.

---

## 3. Interface 1: Proposition 7.1 at a quadratic cv vertex

### 3a. The printed recursion

Proposition 7.1, displayed on pp. 35–36. `F in T_{a,cv}`, `p:=p_F`,
`q:=p_{g,F}`, `G:=F^circ in T_a^+`, and `(K,L,S)_G` from Proposition 4.2:

```text
r_0 := q
r_{j+1} := r_j^{k_j} - s_j p^{l_j}    (j = 0, ..., m-2)
deg(r_j) = (l_j / k_j) * deg(p)       (0 <= j <= m-1).
```

Proposition 4.2: `gcd(k_j,l_j)=1`, `k_j in N*`, `l_j in N*`, uniqueness of
the tower. Promoted repair: `l_j=0` is legal once, as the unique terminal
shift `(k,l,s)=(1,0,c)`, with `gcd(k,0)=k`.

Specialise `deg(p)=2`. Then `deg(r_j)=2 l_j/k_j` lies in `N union {0}`.
For `l_j>0` and `gcd(k_j,l_j)=1`, the condition `k_j | 2 l_j` forces
`k_j | 2`, hence

```text
k_j in {1,2};
k_j=1: any l_j in N*, deg(r_j)=2 l_j;
k_j=2: l_j odd,     deg(r_j)=l_j;
terminal: (1,0),    deg(r_{m-1})=0.
```

This range is source-derived: no external bound is imposed. Every pair with
`1 <= k,l <= 40` was scanned in the packet; the only survivors have `k in
{1,2}`. In particular `(k,l)=(7,5)` and `(14,5)` are illegal at a quadratic
cv vertex (`2*5/7` and `2*5/14` are not integers).

### 3b. `Delta_A=2` pins `deg(p_H)=2` and `H^circ=A`

A-step numbers, recomputed, `t`-free: `D_F=14`, `kbar_F=5`,
`m=mult(p_F,c*)=i_A * 1=2`, `i_A=2`, `Q(A)=(14,42,7,3,5)`, reduced
`(dp,dq)=(21,15)`. Statement 3.10: `d` is convex piecewise-linear of slope
`-deg(p_{I(u)})`. Normalise `tau = kappa_A (u - pi(A))`. Then
`integral_0^{tau_0} deg(p) d tau = D_F=14`, and
`kappa_A(pi(H)-1)=tau_0-5`.

With `m=2` the only possible drop is `2 -> 1`, at some `theta in (0, tau_0)`.
The linear (no-drop) law is `tau_0=7`, local charge `2`. A drop at
`theta < 7` gives `tau_0=14-theta`, local `9-theta`. Combined with
`kappa_H/kappa_A in {1,2}` (the two extra series, `E_+ <= m=2`) and
integrality of `kappa_H(pi(H)-1)` (Prop 7.3's generic-perturbation line,
upgraded from the St 9.4-proof integer):

- contact (`ratio=1`): `theta in N*`, early charges `{8,7,6,5,4,3}`, or `2`
  if `theta >= 7`;
- conjugate (`ratio=2`): `theta in 1/2 + N`, early charges
  `{17,15,13,11,9,7,5}`, or `2` if the pair has not split by `u_0`.

Any integer `>= 3` at a single A-copy overshoots `td-1-psi=6` uniformly in
`t`. Therefore `Delta_A=2` if and only if there is no degree drop before
`d=0` and no ramification jump, i.e. if and only if `deg(p_H)=2`.

On `(pi(A), pi(H)]` a `V_1` vertex would jump `kappa` and a `V_2` vertex
would be the contact of the two extra series, after which `deg(p)=1`. Both
are forbidden. Notation 3.3: `H^circ` is the last vertex below `H`. The only
remaining vertex is `A` itself, which is searrow. The extra microstep
`A * c*` is nearrow (gap `> 0`) but need not be a vertex; the next vertex
`A+c*` sits at or after `H`. So `G = H^circ = A`.

(The control in the packet that a *hypothetical* nearrow parent of degree
two dies by Prop 4.6 `(17)` plus the exclusivity of `(13)` and `(14)` is
therefore a control on an empty case.)

Because the two extra series have not separated, they share the same `eta`
value at `H`: `p_H` is a double root, `c (eta-r)^2`. A split pattern at `H`
would already be a `V_2` event.

### 3c. The characteristic denominator at `A`

Proposition 8.1's proof (p. 40) records, at a searrow vertex,

```text
deg(p_{h_j,F}) = (l_j/k_j) deg(p_F),    M*_F | that degree.
```

At `A`: `deg(p_A)=42`, `i_A=2`, `M*_A=21`. Write `d_j=42 l_j/k_j in N`.
Then `gcd(42, d_0, ..., d_{m-1})=21`. Since `21` is odd and `42` is even,
some `d_j` is odd. Combined with `gcd(k_j,l_j)=1` this forces `v_2(k_j)=1`
and `l_j` odd, hence some `k_j=2`. Equivalently `l_j/k_j` is a half-integer
`t/2`, and some `t` is odd.

This is the actual characteristic denominator entering the recursion: `nu_A=7`
divides `M*=21=3*7`, and the 2-adic part of `i_A=2` forces a genuine
`k_j=2` step. The quadratic menu `{1,2}` of §3a is therefore realised, not
merely permitted.

`m_A=0` is incompatible with `i_A=2`: `M*` would equal `deg(p_A)=42`.
Proposition 5.1(ii) on the pole place already required `m != 0` below the
pole; the `i`-datum is the load-bearing form used here.

### 3d. The recursion on a double root

Translate so `p = eta^2`. For a `k_j=2` step, `r_j` has degree `l_j` odd,
and `r_{j+1} = r_j^2 - s p^{l_j}` with `s` the leading-coefficient ratio.

If `r_j = eta^{l_j}` exactly, then `r_j^2 = p^{l_j}` and the remainder is
the zero polynomial. The packet checks `l in {1,3,5,7}`. A pure-power
filling is illegal (`h_{j+1}` is non-constant by Prop 4.2). Nontrivial
subtop is therefore mandatory. That is the same missing jet the Opus
allegation isolated; here it is forced by the recursion rather than by
St 3.9(ii).

If `r_0 = a eta + b` with `a b != 0` and `(k,l)=(2,1)`, leading cancel
gives `s=a^2` and remainder `2 a b eta + b^2`, still degree one. The map
`l |-> 2l-1` of generic remainder degree has a fixed point at `l=1`. Any
finite string of `(2,1)` steps is a legal Prop 7.1 filling on a double-root
quadratic. The packet runs one, two, three, and four steps, and both signs
of `b`.

This filling is compatible with `M*_A=21` (every `(2,1)` step has
`d_j=21`) and with `some k_j=2`. It does not pin `m_A`, and it does not
produce a polynomial pair `(f,g)`.

---

## 4. Interface 2: closed global census

### 4a. Poles

Table `(23)` row 4, printed p. 46, type `(2,3)`:

```text
(D, D_g) = (2, 3),   (deg p, deg q) = (4, 6),   nu=3,   Lambda(F)=4.
```

This is the census pole `(Lambda, a, b, nu)=(4,1,2,3)`:
`Lambda = a b alpha beta / nu = 1*2*2*3/3=4`. Two copies, one per entry
chain.

Proposition 5.6 `(19)`: `Lambda(F)=D_g deg(p)/nu=3*4/3=4`. Statement 5.2
repaired: `D/D_g=deg(p)/deg(q)=alpha/beta=2/3`. Proposition 5.4(ii):
`p=eta p*(eta^3)` with `deg p*=1`, `q=q*(eta^3)` with `deg q*=2` (the
`p=p*(eta^nu)` side has non-integral `deg p*`). Formula `(18)`: the `c=0`
continuation contributes `D_g/nu=1`; the unique `epsilon` with
`F*(epsilon c)` defined on the nonzero orbit contributes `D_g=3`. Sum `4`.

Proposition 5.8, via the promoted every-fiber replacement: `td = sum
Lambda(F)` over poles. Two copies give `8`. Proposition 5.7:
`Lambda(F) >= beta=3` at every pole, so a third pole has mass `>=3` and
overshoots `td`. There are no other poles, and four pole-places:
`(1, c=0)` and `(3, nonzero)` at each of two vertices.

### 4b. Curve vertices

Section 2 already forces four cv vertices of weights `2,2,2,1`, distinguished
as the two A extras, the trunk extra, and the x-side. Constraints checked:

- **sum:** `2+2+2+1=7=td-1`, saturating Cor 7.1;
- **gcd / characteristic denominator:** at each A-copy, `M*=21`, `M=3`,
  `nu=7`, some `k_j=2` (§3c);
- **orbit:** extra direction is the `B`-orbit of the reduced pattern, `c* != 0`,
  unique `epsilon` by corrected St 3.18; one direction at `H` because `p_H`
  is a double root;
- **place:** Prop 7.3 inequality `sum Lambda(P) >= 2` on that one direction
  (equality is the simple-root case, not this one);
- **distinctness:** MP1, plus x-side on the other component.

The trunk cv of weight `2` is *not* required to have `deg(p)=2`. Theorem C
of the allegation makes `Delta_trunk=2` a positive defect of area `i_F` over
nine normalised steps; that profile is outside this gate. The x-side vertex
of weight `1` is the `psi` cluster, not the root `(0,x)` (`pi=0`, forbidden
by St 7.1).

No tuple `(Lambda(P), kappa_F, pi(F), degree/multiplicity)` compatible with
the two `Lambda=4` poles, `delta_a` unforced, and the four weights is
contradictory in the affine parameter `t`. The A-step numbers used above are
`t`-free; `t` lives in `kappa_A=7(4+3t) kappa_{tr}` and cancels in every
charge.

---

## 5. Reconciliation at the formal source-data tier

Interface 1 survives: the legal `(k,l)` menu is nonempty, `G=A` is the only
parent, a double-root quadratic admits a finite `(2,1)`-chain with subtop,
and `M*=21` is satisfied. Interface 2 survives: the pole census and the
four-vertex census are compatible, and Prop 7.3 does not overconstrain
double-root places. They are realised simultaneously by the following
formal filling, which uses only printed source data plus the reviewed row:

```text
td=8; two table-(23) row-4 poles;
T_{a,cv} = {H_A1, H_A2, H_tr, H_x} of weights 2,2,2,1;
each A extra: G=A, p_H = (eta-r)^2, some k_j=2, r_0=a eta+b with a b != 0,
any finite string of (2,1) steps; Delta_A=2; Delta_trunk=2;
lambda_G=0; W_x=1; no fifth cv vertex.
```

Smallest datum the printed source does not pin: the actual length `m_A` of
the Jacobian tower at `A`, equivalently the subtop of `f^A` at `c*` that
keeps the remainder of the first `k_j=2` step nonzero. The packet treats
this as a finite typed discriminator (`(2,1)`-chain versus collapse) rather
than guessing a value. Existence of one legal filling is the survival
statement; uniqueness of the filling is not claimed.

---

## 6. Packet, tests, mutations

Packet: `cases/m2_td8_cv_weight_contact_gate_grok46_20260829/`.

```sh
cd cases/m2_td8_cv_weight_contact_gate_grok46_20260829
python3 test_cv_weight_contact_gate_td8.py      # TD8_CV_WEIGHT_CONTACT_GATE_GROK46_TEST_PASS checks=351
python3 -O test_cv_weight_contact_gate_td8.py   # identical
python3 cv_weight_contact_gate_td8.py --json
```

Neither the producer nor the test file contains an `assert` statement
(line-start scan). The `-O` identity is therefore structural.

Check census, 351 per suite: route / i-chain / Q-datum over
`t in {0,1,2,3,7,20,100,1000}` including two invalid-`t` rejections; pole
census (row 4, formula `(18)`, Prop 5.7/5.8, four places); A-step descent
(no-drop charge `2`, contact menu `{8..3}`, conjugate menu `{17,15,...,5}`,
`theta=7` rejection); budget four-vertex (psi, floors, weights, no printed
7.5); quadratic `(k,l)` window of side 40 with `k|2`; `M*=21` forces some
`k_j=2`; parent `H^circ=A`; double-root `(2,1)` fillings and pure-power
collapse; nearrow Prop 4.6 control; cv-tuple roles; in-suite mutation
controls; certificate / firewall / stdout identity; no-`assert` scan.

Independent `/tmp` mutations of a producer copy (packet untouched), 10/10
rejected, 0 survivors:

| mutation | rejected by |
|---|---|
| gap sign flipped (unrepaired `(24)`) | A linear charge `12 != 2` |
| `k`-menu `{1,3}` in place of `{1,2}` | `k | 2` |
| `M*` taken as `42` | `M*` identity |
| third pole permitted (`td` check `+4`) | two poles exhaust `td` |
| `psi=0` | terminal `psi=1` |
| weights `{2,2,2,0}` | `psi` / weight-one |
| pure-power collapse inverted | remainder `=0` |
| `i_A` forced to `1` | `i_A=2` |
| no-drop charge forced to `3` | A linear charge |
| quadratic degree test dropped (`k | 2l` never checked) | `k | 2` on a `k=2` sample |

---

## 7. Clause-level claim firewall

| clause | status |
|---|---|
| Prop 7.1 degree formula `deg(r_j)=(l_j/k_j) deg(p)` | PINNED (displayed, pp. 35–36) |
| Prop 4.2 `gcd(k,l)=1`; repaired terminal `(1,0)` | PINNED / PROMOTED REPAIR |
| `deg(p)=2` => `k_j in {1,2}`, `l_j` odd when `k_j=2` | PROVED |
| `Delta_A=2` iff no drop and no kappa jump iff `deg(p_H)=2` | PROVED (St 3.10 + A-step numbers) |
| Contact early menu `{3..8}`, conjugate `{5,7,...,17}` | PROVED |
| `H^circ=A`; `p_H` a double root | PROVED from `Delta_A=2` |
| `M*_A=21` forces some `k_j=2` | PROVED (Prop 8.1 proof line + 2-adic) |
| Pure-power filling of `r^2 - s p^l` collapses | PROVED (packet, `l=1,3,5,7`) |
| `(2,1)`-chain with `a b != 0` stays degree one | PROVED (packet) |
| Two table-`(23)` row-4 poles, `Lambda=4+4=8`, no third pole | PROVED (Prop 5.6/5.7/5.8 replacement) |
| Four pole-places, Lambdas `1,3` per pole | PROVED (formula `(18)`) |
| Four cv vertices of weights `2,2,2,1` | PROVED from Cor 7.1 + H3-psi + St 7.1 + MP1 |
| Printed Prop 7.5 `(22)` and `delta_a=0` | NOT USED (quarantined) |
| Prop 7.3 equality `Lambda=weight` at an A-cv | NOT CLAIMED (double root) |
| Actual `m_A`; actual subtop of `f^A` at `c*` | NOT PINNED (typed discriminator) |
| The `(2,1)` filling realised by a polynomial pair | NOT CLAIMED |
| Uniform `Delta_A >= 3` | NOT DERIVABLE (unchanged) |
| Exact `Delta=2` on the actual extra branches | NOT PROVED (unchanged) |
| Route killed / route promoted | NEITHER (configuration survives) |
| Source landing, gluing, realizability, counterexample, degree ceiling, JC2 | NOT CLAIMED |
| AWS launched; canonical file edited; commit/push; `jc2-lean` accessed | NONE |

---

## 8. Seals

**Packet seals.**

```text
8a457b2135dab817a5fadce308eea72d5c1199329075ef07867fa952ce8f59e8  cv_weight_contact_gate_td8.py
7f5474e20087de009525cf828a683521f21b903c87c5791f32664e51ffff028f  test_cv_weight_contact_gate_td8.py
d98da18aa59db4084852e7195958da0d4d07d783d084290d4c33f493bc7f370c  README.md
85beaff0d4fe939cf96519e80d09201bc47c965b1eb1f904997e6c8fb497745f  charged JSON stdout
1f0babfe41c720658078a4ea44470079ea4ac1ec23c704a7bbcebdfade251544  certificate (sorted compact JSON, hash key removed)
```

**Reproduction.**

```sh
python3 -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('xmodel/m2-td8-cv-weight-contact-gate-primary-grok46-20260829.md').read_bytes()).hexdigest())"
cd cases/m2_td8_cv_weight_contact_gate_grok46_20260829
python3 test_cv_weight_contact_gate_td8.py
python3 -O test_cv_weight_contact_gate_td8.py
python3 cv_weight_contact_gate_td8.py --json | shasum -a 256
```

---

*Report body ends. Self-hash below covers everything above this line.*

report_body_sha256 = 39f94bf51b4c78e90ba5e48a0f35f81c8db64a4650fcf9f6ee9fe9104a38cfeb
