# Primary research — exact Sigray lambda on the td=8 equal-join route

Lane: Grok 4.6, independent primary research, not a referee of a later
solve. Date: 2026-08-29. Object: the three priced steps of the reviewed
affine equal-join family in
`xmodel/m2-td8-equal-join-route-family-sol56-20260829.md`.

Packet: `cases/m2_td8_equal_join_exact_lambda_grok46_20260829/`.

No access of any kind to `jc2-lean`. No web, AWS, Singular, msolve, Sage,
PARI, or other heavy CAS. Arithmetic is desk `int` / `Fraction`. Canonical
files were not edited. Ordinary and `-O` tests plus adversarial mutations
were run. Opus/Fable/Sol output produced after the reviewed route family
and its Grok review was not read.

---

## 0. Verdict

**`PARTIAL`.**

The recorded lower-bound budget is exactly `2+2+2=6` and meets
`td-1-psi=6`. None of the three charged contributions is proved equal to
2, and none is proved to be at least 3. A uniform `lambda>=3` at any one
priced step is not derivable from the printed definition together with
the reconstructed top-pattern data, so the affine route is not killed at
this gate. Exact `lambda=2` is the linear-model value on each incoming
`(21,15)` step and is compatible with St 9.4 integrality there; it is
*not* a theorem, because equality in corrected St 9.3(24) is an extra
contact/ramification statement. On the `(85,35)` trunk the same linear
model predicts `3/2`, which cannot be the actual `kappa_H(pi(H)-1)` if
that quantity lies in `N`, so a strictly positive correction is forced
and the integer may be 2 or any larger integer.

The two incoming extras are first-separation independent: MP1 allows only
one 2-ary merge at `m=2`, so the extra branches cannot reconverge and
cannot share a cv flag. Their shared merge does not impose a coupled
lambda *count*. It can still couple the missing subtop jet of the trunk,
and that jet may depend on `t` even though the reduced trunk successor
`(w,M)=(2/5,5)` and the reduced gap `3/2` do not.

Narrowest maximum consequence: the family remains a budget-fitting
superset-formal route. The lambda gate is not discharged. No member is a
source landing or a Keller map.

---

## 1. Custody

Files read, and only these, for mathematics:

- `xmodel/m2-td8-equal-join-route-family-sol56-20260829.md`
  (full `9a778862816aa96d251c33aac7e98a2fb3bfc1b3fc7c83f4463ac862de31815a`,
  body `bd35c43baf91c6306d4bb651a09e4886340ab7eb836ffd41d6b1ba6a85ea02d7`);
- `xmodel/m2-td8-equal-join-route-family-hostile-review-grok46-20260829.md`
  (body `a53a78dbabaaa6f1c2a30247ad016b99bf2d2011132736a2e8b7c5f098552c49`);
- `xmodel/m2-td8-prop81iv-parametric-primary-grok46-20260829.md`, used only
  as established local pattern context at the merge;
- `cases/m2_td8_equal_join_route_family_r1_20260829/` (producer identities);
- `refs/sigray_full.pdf` printed pp. 13–18, 34–42, 48–54
  (Not. 3.9–3.14, St. 3.9–3.18, Not. 7.1, St. 7.1/7.3, Cor. 7.1, Prop. 8.1,
  St. 8.2, Not. 9.1–9.3, St. 9.3–9.6, Prop. 9.3);
- `ladder/SHEET6-AF2.md` §§1–3 (corrected (24), derived AF2, E6/E7);
- `ladder/SHEET6-H3.md` §§3–4a (St. 9.4 family, H3-psi, first-exit);
- `ladder/BOOK-OFFAXIS.md` §10 P0–P2;
- `ladder/SHEET6-L1.md` §§1, 1a, 5 (root/eta laws, family C);
- `ladder/SHEET6-DEPTH.md` §1 i-normalization;
- `ladder/SHEET6-MULTIPOLE.md` MP1–MP2 as cited;
- `ladder/SHEET6-CAMPAIGN.md` §0a assembly layer;
- `ladder/REDUCTION.md` T8/T9 and CRITICAL 4, as scope only;
- `cases/l1_ode_check.py` family C header.

Packet hashes of this solve:

```text
14623e3f12e0ae2796c9280c4345ddefe5c95ee32fb36277dbcae32c891c07cc  exact_lambda_td8.py
24e83a59ab173efaec150dabc0eb99710bb9af0f848a162078fae729c589ef2c  test_exact_lambda_td8.py
10f3ecd7ca52cfc00759f1d8aac319dbe95b95f0121c89b7fd10b4fe8bf9331c  README.md
7ec7a834d2673ca444bd4d70e59fc2b39b076b81e1bfcab6315d4c5fa6465a47  charged JSON stdout
```

Certificate SHA-256 (sorted compact JSON without the hash key):

```text
3086acb228368017efdba4e8b3052b1a27b5b77ab568ebc0384a098cd0780600
```

Ordinary and `-O` suites each print
`TD8_EXACT_LAMBDA_GROK46_TEST_PASS checks=103`.

---

## 2. Printed definition of lambda, and every theorem used for AF2/the floor

### 2a. The quantity

Notation 7.1 (p. 35): `T_{a,cv} := {F in T_a^0 : d_{g,F}=0}`. Curve
vertices are the unique `d_f=0` points of St 3.13 at which also
`d_g=0`. St 7.1: `pi(H)>1`. St 7.3: a branch through a northeast vertex
carries a cv vertex.

Notation 9.3 (p. 49), verbatim structure:

```text
Y(F) := { H in T_{a,cv} : exists P in R_a \ Rbar_a
          with F = I_P(u) and H = I_P(pi(H)) }
lambda_F := sum_{H in Y(F)} kappa_H (pi(H) - 1).
```

Literal `Y(F)` is nested along a characteristic sequence. The promoted
replacement (AF2 supporting cast, H3-psi §4a, actual-weight Cor. 7.1
`c253bd12...`) assigns each cv flag to the unique first-separation exit
set of the vertex at which the branch leaves the chain. Write
`lambda_F^exit` for that disjoint charge. St 9.4(25) in the repaired
reading is `sum lambda_i^exit <= td-1-psi`. This report prices
`lambda^exit`, never nested `Y`.

### 2b. The lower bound: St 9.3(24) with E6

St 9.3 (p. 49). `F in T_a^searrow cap V_a`, extra child
`G := F + c* in T_a^nearrow`, `H = I_P(w) in T_{a,cv}`. Printed (24)
has the E6 sign slip `kappa_F(pi(F)-1)` for `kappa_F(1-pi(F))`. The
intended inequality, the one used by every p. 53 application and derived
in AF2 §1 against the proof's own chain, is

```text
kappa_H(pi(H)-1)  >=  D_F / mult(p_F, c*)  -  kbar_F     (c* != 0)
kappa_H(pi(H)-1)  >=  (D_F / mult(p_F, c*) - kbar_F)/nu_F  (c*=0),
```

with `kbar_F := kappa_F(1-pi(F))`. Prop. 8.1(i) gives
`mult(p_F, c*) = i * mult(p, c*)`, so the reduced gap is
`X/m - kbar` with `X = D/i` and `m = mult(p, c*)`.

Proof of (24), equality conditions (c* ≠ 0). The printed chain is two
inequalities:

1. `kappa_H >= kappa_F`, hence `kappa_H(w-1) >= kappa_F(w-1)`;
2. St 3.11 at `d_H=0`: `w-u >= d_F / mult(p_F,c*)`, hence
   `kappa_F(w-u) >= D_F/mult`.

Equality in (1) is no extra ramification between `F` and `H`. Equality
in (2) is St 3.11 equality from `F` to the unique `T_a^0` point, i.e.
linear drop of `d` at slope `-mult(p_F,c*)` with no intermediate vertex
changing the pattern. St 3.9(iii) *is* equality at every microstep
`d_{F*c} = d_F - mult/kappa`. St 3.10 makes `d` linear between vertices.
Deviation from the linear model occurs only if a new `V_a` vertex or
characteristic exponent appears strictly before `d` hits 0.

St 3.11 as printed is the campaign ERRATUM (missing prime on the first
term). The proof of (24) uses the `d_H=0` evaluation, which is the
corrected vanishing statement at a cv, not the false equality-propagation
clause. H5a/Not 3.5 is not used: `kbar` and `X` are the chart-free
Not 9.1 coordinates.

### 2c. Derived AF2, integrality, and the recorded floor

AF2 §2 (promoted local pricing, now on first-separation exits): for extra
orbits of reduced multiplicity `m_j` and a free 0-root if present,

```text
lambda_F^exit  >=  sum_j max(1, ceil(X/m_j - kbar))
                 + [eps>=1] max(1, ceil((X/eps - kbar)/nu)).
```

The `ceil` uses the St 9.4-proof line `kappa_H(pi(H)-1) in N`. The
`max(.,1)` is automatic once regularity plus repaired Props 6.7/6.8
force every alternative gap strictly positive (AF2 R2–R4). On this
route every extra gap is positive by the northeast test, so the floor
is regularity-free. Clean `eps=k=0` costs 0 (St 9.6(v); P2).

P0 of BOOK-OFFAXIS §10 is this rule. P2 prices merge extras the same
way and prices arriving edges and q-extras 0. P1 / H3-psi: at the last
searrow vertex above `(0,y)`, `j=M(1-w) in N*` and
`psi = ceil(M/j)-1 = ceil(1/(1-w))-1`. St 9.4(25) is one shared budget
over pairwise-distinct searrow vertices.

St 9.6(iii) (p. 53) is the printed specialisation to the `(21,15)` step:
`Q(F)=(7j,21j,7,3,5)` and `lambda_F >= 2`. The thesis never upgrades
`>=` to equality. E7 (q-pattern power 2 vs degree 1) is already
corrected by the root law of Prop. 8.1(iv) / L1 §1a; this report uses
the radical `q`.

Printed (22) / literal nested `Y` / zero-`delta` ledger remain
quarantined (CAMPAIGN overlay, REDUCTION T8/T9). They are not used.

---

## 3. The three priced steps, reconstructed

Entry: unique off-axis `td=8,m=2`, type `(2,3)`, both poles
`(Lambda,a,b,nu)=(4,1,2,3)`, `(w,M)=(3/2,2)`. Pole full degree 4, so
St 3.17(i) along `l=2` gives `i_A=2` and full A-degree 42. Then
`42 = i_G * 3` gives `i_G=14`. The trunk has
`i_F = 14*(24+18t)/3 = 28(4+3t)`. Reduced gaps use `D/(i m)=X/m`, so
`i` cancels.

### 3a. Each incoming `(21,15)` A-step

Pattern (St 9.6(A), E7-corrected, L1 family C):

```text
l=2, nu=7, eps=0, k=1, Sm=1, lex=0,
p(t) = (t-A)^2 (t-B),   w(t)=(t-A)(t-B),   t=eta^7,
q = eta * w,
(kbar,X,rho,w,M)=(5,7,1/3,2/3,3).
```

Unique extra orbit, reduced multiplicity 1, full multiplicity `i_A=2`.
No 0-root. Gap `X/1-kbar=2`. AF2 floor `max(1,ceil(2))=2`. Parent-edge
`n=10` of St 9.6(A) is t-free. Incoming merge labels `n_e=37+28t` are
the *continuation* toward G, not the extra.

Prop. 8.1(iv) in rho form, `rho=21/15=7/5`. After Cor. 6.1 the `t^2`
coefficient of `E/p` is

```text
rho + 2 nu rho - 3 nu = 7/5 + 98/5 - 21 = 0.
```

The `t^1` coefficient is `A(-21/5)+B(14/5)`, hence uniquely
`B=(3/2)A`. Then `ctilde=rho A B=(21/10)A^2 != 0`. Gauge `A=1` is
integral. This is L1 family C, re-derived here; uniqueness up to scale
is the vanishing of one linear form. Side conditions: `B != A`, `B != 0`,
eta-law `w(0)!=0`. The extra *direction* is therefore rigid. The extra
*subtop jet* is not.

Linear model along that unique extra. Microstep
`E=F*_kappa(epsilon B^{1/7})` has, by St 3.9(iii),

```text
d_E = d_F - (i_A * 1)/kappa_F = 14/kappa_F - 2/kappa_F = 12/kappa_F > 0,
```

so E is still in `T_a^+`. Constant slope `-2` to `d=0` gives
`kappa_F(pi(H)-1)=7-5=2`. This integer is compatible with St 9.4
integrality, and equals the AF2 floor. It is the exact lambda if and
only if (i) no intermediate vertex occurs before `d=0` and (ii)
`kappa_H=kappa_F`. Neither is a printed consequence of the top pattern.

### 3b. Merge (not priced)

Equal arrivals `(mu,w)=(3,2/3)`, `eps=k=lex=0`, `nu_G=4+3t`. Established
local pattern (own Prop. 8.1(iv) report): opposite orbits
`p=(eta^{2 nu}-1)^3`, `q=eta(eta^{2 nu}-1)`. No extra orbit and no free
0-root, so P2 charges exactly 0. That 0 is an accounting identity, not
an AF2 floor.

### 3c. Trunk `(85,35)`

Pattern, unique at `nu=17`:

```text
l=3, nu=17, eps=0, k=1, Sm=2, lex=0,
p(t)=(t-C)^3 (t-D)^2,   w(t)=(t-C)(t-D),   t=eta^17,
q=eta*w,
(kbar,X,rho,w,M)=(7,17,1/5,2/5,5).
```

Unique extra orbit, reduced multiplicity 2, full multiplicity
`i_F*2=56(4+3t)`. Gap `X/2-kbar=17/2-7=3/2`. AF2 floor
`max(1,ceil(3/2))=2`. The simple-orbit slogan `ceil(X-kbar)=10` is the
wrong rule and is not used. Parent-dependent continuation label
`n_F=22+17t`; companion X-handshake `X=l(rho_G+n)/nu_G=17` is
t-independent, as is the reduced successor.

Prop. 8.1(iv), `rho=85/35=17/7`. The `t^2` coefficient of `E/p` is

```text
rho + 2 nu rho - 5 nu = 17/7 + 578/7 - 85 = 0.
```

The `t^1` coefficient is `C(-68/7)+D(51/7)`, hence uniquely
`D=(4/3)C`. Then `ctilde=rho C D=(68/21)C^2 != 0`. The extra direction
is rigid. The extra subtop jet is not.

Linear model: `kappa_F(pi(H)-1)=3/2`. If `kappa_H(pi(H)-1) in N`, this
cannot be the actual value. A strictly positive correction is forced.
The smallest compatible integer is 2; 3,4,... remain open. The
correction may be extra contact, a kappa jump, or both. No printed
statement forces the correction to be at least 1 in the integer scale
beyond the ceil already booked.

Terminal: `j=5*(1-2/5)=3`, `psi=ceil(5/3)-1=1`, ceiling `8-1-1=6`.

---

## 4. Why `lambda>=3` is not a uniform kill

A uniform extra unit at any one of the three priced vertices would give
recorded sum `>=7>6` and St 9.4 would kill every `t>=0`.

No such unit is printed.

- Each step has exactly one extra `nu`-orbit. St 3.18 supplies one
  direction per orbit, hence typically one first-separation cv flag.
  Multiplicity 2 at the trunk is one double reduced root, not two
  orbits; AF2 prices it as one gap `X/2-kbar`.
- There is no 0-root (`eps=0`).
- Nested `Y` would overcount and is not the budget quantity.
- St 9.6(iii) lists this exact A-step as `lambda>=2`, not `>=3`. That is
  not a proof of equality, but it is a proof that the thesis does not
  contain a hidden extra unit on `(21,15)`.
- Integrality on the trunk upgrades `3/2` to `>=2`, which is already
  the recorded floor, not to `>=3`.
- First-separation independence of the two A-copies (next section)
  forbids charging one extra cv twice.

Therefore outcome 1 of the brief is not derivable. The affine route is
not killed at the lambda gate.

---

## 5. Why exact `lambda=2` is not proved

Do not infer equality from the floor. The definition is the sum of
`kappa_H(pi(H)-1)`, and St 9.3 is a lower bound.

On each A-step the linear model *equals* 2, so equality holds if and
only if the extra branch is linear in `d` from `F` through its unique
`T_a^0` point with constant `kappa`. That is a statement about the
first subtop homogeneous piece of `f_F` in the Prop. 8.1 chart, or
equivalently about the first extra-branch Puiseux coefficient after
the separating term `B`. The top Jacobian Prop. 8.1(iii)–(iv) does not
constrain that piece. St 3.9(ii) transports only leading coefficients
of the top. Pole rigidity plus one characteristic jump determines the
top at `F`, not the subtop.

On the trunk the linear model cannot be the exact value, so
`lambda=2` would require a correction of exactly `+1/2` in
`kappa(pi-1)` units and no further cv flag. That is one of infinitely
many integer possibilities compatible with present data.

St 7.3 plus St 3.13 do force the cv to sit at the unique `d_f=0` point
of the extra branch, so there is no “`d_g` misses `d_f`” loophole.
That pins the *locus*, not the *coordinate* `pi(H)`.

---

## 6. Two incoming copies, and the affine parameter

MP1: `sum(r-1)=m-1=1`. The configuration has exactly one 2-ary merge.
An extra branch at `A1` that met an extra branch at `A2` would be a
second merge. So the extra first-separation exit sets are disjoint.
There is no coupled lambda *count*. The extras are not the merge
arrivals: the A-step extra ratio is `B/A=3/2`, while the merge
identification is opposite continuation orbits.

Coefficient coupling through St 3.9 matching of the two continuations
into opposite merge orbits is a transport/landing constraint on the
continuation edges. It does not identify the extra cv flags. It can
feed the *trunk* parent jet, because the merge expansion is the parent
of `(85,35)`.

A-step local Q-datum, parent `n=10`, extra ratio `3/2`, and linear
prediction 2 are all t-free. Any exact A-step lambda computed from
pole→A transport is therefore constant in `t` and equal on the two
copies.

Trunk reduced Q-datum and reduced gap `3/2` are t-free, but `i_F`,
`n_F=22+17t`, and the merge pattern `nu_G=4+3t` are not. The subtop
jet at the trunk may depend on `t`. The reduced successor does not
pin the exact valuation.

---

## 7. Missing datum and finite discriminator

Keep four objects distinct:

| object | status here |
|---|---|
| local pattern | rigid at all three vertices (A: `B=3A/2`; merge: opposite orbits; trunk: `D=4C/3`) |
| compatible route | reviewed infinite affine family, recorded floors sum to 6 |
| actual source landing | not claimed |
| realizable Keller map | not claimed |

**Typed missing datum.** At a priced vertex `F`, in the Prop. 8.1 chart
with suitable `kappa`,

```text
f_F(xi, eta) = xi^{kappa delta} p(eta)^i  +  xi^{kappa delta - r_*} p_*(eta)  +  lower,
```

where `r_* in N*` is minimal such that `p_*` is not a `Q`-multiple of
`p^i`. The pair `(r_*, p_*)` is the first extra-branch jet. Equivalently:
the first Puiseux coefficient of a branch `P*` through
`F*(epsilon c*)` after the separating term `c*`.

**Finite discriminator**, to be handed to the transport lane.

Let `m` be the reduced extra multiplicity, `L := X/m` (so `L=7` on each
A-step and `L=17/2` on the trunk), and let `sigma` be the first
Newton–Puiseux increment along `P*` computed from `(p, r_*, p_*)`. Let
`u_0` be the unique rational of St 3.13 on `P*`, and set

```text
Delta(F) := kappa_{I(u_0)}(u_0 - 1)  in N.
```

Then `lambda_F^exit` of the unique extra equals `Delta(F)`.

- If `sigma >= L/kappa_F` and `kappa` stays, then `Delta(F)` equals the
  linear prediction (`2` on each A-step; `3/2` on the trunk, which is
  then impossible, so this branch cannot occur on the trunk).
- If `sigma < L/kappa_F` or `kappa` jumps, recompute `u_0` from the
  broken-linear `d`-path and output the integer `Delta(F)`.

Inputs already rigid:

- A-steps, t-free: pole `Q=(2,4,3,2,5)`, child top with `B=(3/2)A`,
  parent characteristic `n=10`. Pole→A is one characteristic jump.
  The two copies are identical.
- Trunk: parent merge top `p=(eta^{2 nu_G}-1)^3`, child top with
  `D=(4/3)C`, edge `n_F=22+17t`. This jump depends on `t` and may
  consume the merge subtop produced by the two A-arrivals.

Output:

- any `Delta>=3` kills the whole affine route
  (`ROUTE_KILLED_BY_STRICT_LAMBDA`);
- all three `Delta=2` is `EXACT_LAMBDA_TWO_PROVED` at the lambda gate
  only;
- `Delta_trunk(t)` not constant is the exact-valuation t-dependence.

The computation is finite: one homogeneous piece below the top at each
priced vertex, or one Newton–Puiseux step from that piece. It is not
performed here because `(r_*, p_*)` is not a consequence of Prop. 8.1(iv)
or of the Q-datum.

---

## 8. Packet

Packet: `cases/m2_td8_equal_join_exact_lambda_grok46_20260829/`.

```sh
cd cases/m2_td8_equal_join_exact_lambda_grok46_20260829
python3 test_exact_lambda_td8.py
python3 -O test_exact_lambda_td8.py
python3 exact_lambda_td8.py
python3 exact_lambda_td8.py --json
```

Check census, 103 per suite: 10 (floors) + 8 (closed forms and scaling)
+ 5 (mutations) + 65 (i-chain `t` in `{0,1,2,3,10,15,100,1000}` and
invalid `t`) + 3 (MP1) + 2 (uniqueness scans) + 7 (certificate/firewall)
+ 3 (stdout identity). Independent closed forms of the two `t^1`
vanishing laws are the uniqueness proofs; the scans are regression.

`/tmp` mutations of a producer copy, packet untouched: `B=2` and `D=2`
reject the ODE; frame `rho=2/3` in place of `7/5` rejects the A-step;
coincident extra/continuation roots reject both patterns.

---

## 9. Clause-level claim firewall

| clause | status |
|---|---|
| Printed lambda is `sum kappa_H(pi(H)-1)` over first-separation cv flags | PINNED, Not 9.3 + promoted exit repair |
| Nested literal `Y` used as the budget quantity | NOT DONE |
| AF2 floor derived from corrected (24) + St 9.4 integrality | PINNED |
| Recorded floors `2,2,2` and merge P2 exact 0 | PROVED |
| Budget equality `6=td-1-psi` | PROVED (filter only) |
| Linear model A-step `=2`, trunk `=3/2` | PROVED as the equality-case of (24) |
| Trunk linear value compatible with `kappa(pi-1) in N` | FALSE |
| Equality in (24) from top pattern / Prop. 8.1(iv) | NOT PROVED |
| Uniform `lambda>=3` at any priced step | NOT DERIVABLE |
| Exact `lambda=2` at any priced step | NOT PROVED |
| A-step extra ratio `B=(3/2)A` unique | PROVED |
| Trunk extra ratio `D=(4/3)C` unique | PROVED |
| Two incoming extras share a cv flag | FALSE (MP1) |
| Affine `t` changes reduced gap or reduced successor | FALSE |
| Affine `t` can change the trunk subtop jet | OPEN (discriminator) |
| Source landing / realizability / JC2 | NOT CLAIMED |
| Prop. 8.1(iv) at the merge | USED as established local pattern, not re-proved |
| Completeness of all `td=8` merges | NOT CLAIMED |

---

## 10. What this does to M2, and the next lemma

The Sol D2 family is not killed by a printed extra lambda unit, and it
is not promoted to an exact-cost family. The reduced successor remains
`(4/3,3)` at the merge and `(2/5,5)` at the trunk. Quotienting by
reduced state still loses the affine cell parameter; exact lambda, if
ever computed, may or may not restore a `t`-bound on the trunk.

**Next lemma (transport lane).** Compute the first extra-branch jet
`(r_*, p_*)` at each priced vertex from one characteristic jump of
St 3.9 / Newton–Puiseux, using the rigid tops of §3, and evaluate
`Delta(F)` of §7. That single integer per vertex decides among
`ROUTE_KILLED_BY_STRICT_LAMBDA`, `EXACT_LAMBDA_TWO_PROVED`, and a
t-dependent trunk remainder.

Nothing here restores a prime-`td` exclusion, a cofinal bound on `td`,
or a Keller counterexample.

---

## 11. Reproduction

```sh
python3 -c "import hashlib,pathlib; p=pathlib.Path('xmodel/m2-td8-equal-join-exact-lambda-primary-grok46-20260829.md'); print(hashlib.sha256(p.read_bytes()).hexdigest())"
cd cases/m2_td8_equal_join_exact_lambda_grok46_20260829
python3 test_exact_lambda_td8.py
python3 -O test_exact_lambda_td8.py
python3 exact_lambda_td8.py
python3 -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('exact_lambda_td8.py').read_bytes()).hexdigest())"
```

---

Report-body SHA-256 (bytes before the separator line above): `00a7b77a078711726f8d8537366ba2aa5e69ffd407f0e7536a6989da0792b719`
