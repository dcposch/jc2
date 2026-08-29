# Primary research — the first extra-branch jet and the exact Sigray lambda at td=8

Lane: Opus 5, independent primary mathematics, not a review. Date: 2026-08-29.
Object: the narrow missing datum isolated by Grok's exact-lambda report — the
first extra-branch jet `(r_*, p_*)` at the two identical `(21,15)` A-steps and
at the `(85,35)` trunk of the reviewed td=8 equal-join affine route — and the
exact first-separation charge `Delta(F) = kappa_{I(u_0)}(u_0 - 1)`.

Packet: `cases/m2_td8_first_extra_jet_exact_lambda_opus5_20260829/`.

No access of any kind to `jc2-lean` or to any nested formalization tree. No web,
AWS, Singular, msolve, Sage, PARI, or other CAS. Arithmetic is desk
`int`/`Fraction` plus hand-rolled polynomial lists. No canonical file was
edited; nothing was committed or pushed. Ordinary and `-O` suites plus ten
adversarial mutations were run. No later peer output on this question was read
(none existed at the paths checked when this lane opened).

---

## 0. Verdict

**`NOT_DETERMINED_FROM_PRINTED_DATA_WITH_EXACT_SEPARATION_LAW`.**

The brief's fourth outcome, delivered together with as much of the third as is
actually true.

1. **The jet is not derivable.** Statement 3.9(ii) pins exactly one coefficient
   of the child pattern `p_{F*c*}` — the leading one. Proposition 8.1 constrains
   only `f_F^+` and `h_F^+`, i.e. the top. Two further constraints on the subtop
   *are* derivable and are proved below (§8): a `kappa`-lattice vanishing and a
   **pinned `nu_F`-semi-invariance weight** for every subtop piece. Even after
   imposing both, the discriminant of `p_{F*c*}` on an A-step remains a free
   affine function of one scalar, `p_{n-2}(c*)`, which no printed statement
   sees. Two admissible fillings are exhibited, with charges `Delta = 8` and
   `Delta = 2`. So `(r_*, p_*)` is **not** a consequence of St 3.9 plus the
   characteristic jump plus the rigid tops.

2. **What replaces it is an exact law, not a bound.** Normalizing
   `tau := kappa_F (u - pi(F))`, the exact charge is

   ```text
   Delta(F, c*) = (kappa_H / kappa_F) * (tau_0 - kbar_F),
   D_F = integral_0^{tau_0} deg(p_{I(u)}) d tau,     deg(p_{I(0^+)}) = m := mult(p_F, c*).
   ```

   The corrected St 9.3(24) gap `D_F/m - kbar_F` is exactly the constant-profile
   case. Every excess over the gap is a *branch separation* below the cv vertex.

3. **The A-step charge has a finite menu.** With `m = i_A * 1 = 2` only one
   degree drop `2 -> 1` can occur, `kappa_H/kappa_F` is forced into `{1,2}`, and
   integrality of `kappa_H(pi(H)-1)` (proved, §2c) forces the separation level
   `theta := kappa_F(O - pi(F))` into `N*` (contact) or `1/2 + N` (conjugate).
   Hence

   ```text
   Delta_A  in  {2, 3, 4, 5, 6, 7, 8}  u  {5, 7, 9, 11, 13, 15, 17},
   Delta_A = 2  <=>  theta >= 7  <=>  the extra-direction pair does not separate
                                      before d reaches 0  <=>  deg(p_H) = 2.
   ```

4. **The trunk charge is 2 only with an exact positive defect.** `m = 2 i_F`,
   gap `= 3/2`, so `Delta_trunk = 2` forces `kappa_H = kappa_F` **and**
   `tau_0 = 9`, i.e. the branch group must shed exactly one `i_F` unit of
   branch-area over the nine normalized steps. `Delta_trunk = 2` is therefore
   *not* the linear model; it is the linear model plus a strictly positive,
   exactly-sized correction.

5. **Budget knife-edge (new).** `sum lambda^exit <= td - 1 - psi = 6`, the merge
   contributes exactly `0`, and each of the three priced charges is an integer
   `>= 2`. Therefore the affine family survives the exact-lambda gate **iff all
   three charges are exactly 2**, and additionally `lambda_{(0,y)} = 0`,
   `delta_a = 0`, and `T_{a,cv}` is exactly four vertices with weights
   `2, 2, 2, 1`. A single early separation at *either* A-copy raises the total to
   `>= 7 > 6` and kills **every** member of the family at once.

Not claimed anywhere: a route kill, exact `lambda = 2`, source landing, Keller
realizability, a counterexample, a degree ceiling, or JC2.

---

## 1. Custody

Files read for mathematics, and only these:

| file | sha256 (full) | bytes |
|---|---|---|
| `xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-prompt-20260829.md` | `5a0b7ed4ce2270bf315cbfdbd3e91623a1b5bd0125d37ef470f4dc7f8a7cee71` | 2511 |
| `xmodel/m2-td8-equal-join-exact-lambda-primary-grok46-20260829.md` | `99b136da9930c76f833de66c437ffb7ef8b07ab017e0e6719fbb7c888c16e919` | 21095 |
| `xmodel/m2-td8-equal-join-route-family-sol56-20260829.md` | `9a778862816aa96d251c33aac7e98a2fb3bfc1b3fc7c83f4463ac862de31815a` | 5623 |
| `xmodel/m2-td8-equal-join-route-family-hostile-review-grok46-20260829.md` | `d3f378a1c5ed6a649b53885ce2d965c4fad4acad64b98df96ed2ed71ad6b2d8e` | 20866 |
| `xmodel/m2-td8-prop81iv-parametric-primary-grok46-20260829.md` | `2d9fa6fa73da2f8d276301ef9f2153eb305f3e87e5bb307d127ee4adcfcf94a1` | 18335 |
| `xmodel/m2-td8-prop81iv-parametric-hostile-review-fable5-20260829.md` | `13b6e430ee3dec615e964e3455368bbc113c2b1c076f118de17e260e8d4911fa` | 25642 |

Body hashes independently recomputed and matching each report's own appendix:
Grok exact-lambda `00a7b77a078711726f8d8537366ba2aa5e69ffd407f0e7536a6989da0792b719`;
Sol D2 `bd35c43baf91c6306d4bb651a09e4886340ab7eb836ffd41d6b1ba6a85ea02d7`;
Grok D2 review (first 20342 bytes) `a53a78dbabaaa6f1c2a30247ad016b99bf2d2011132736a2e8b7c5f098552c49`;
Grok Prop 8.1(iv) (first 17822) `cc7035dec2949f674064f7495c209abbf1037dee3179f1abd876a8e292366416`;
Fable review (first 25122) `9e594a2343bfcdfe8b2631506543139210f1fa178f4a616c7e09d93ba54da82b`.

Ladder, with the exact extent opened recorded: `SHEET6-AF2.md` in full
(corrected (24), E6/E7, derived AF2, §6 trust perimeter); `SHEET6-L1.md` in full
(root law, eta law, §5 family C `B = (3/2)A`); `SHEET6-DEPTH.md` §§0–2 through
DS1 (i-normalization, `w = (kbar-rho)/nu`, equal-quotient transport);
`SHEET6-H3.md` §§3–4a (Not 9.1, St 9.2, Prop 9.3(IV), St 9.4(25) verbatim, the
H3-psi theorem and its first-separation exit-set repair); `SHEET6-MULTIPOLE.md`
MP1–MP2 (`sum_{r(G)>=2}(r(G)-1) = m-1`, so `m=2` has exactly one 2-ary merge;
MP2's `M != 1` at interior vertices). No other ladder file was opened; the
`BOOK-OFFAXIS` P0/P1/P2 and `REDUCTION` T8/T9 content is used only as quoted in
the cited packets, and carries no weight in any theorem below.

`refs/sigray_full.pdf`, read on-page (printed page = pdf page):
pp. 10–13 (Def 3.1–3.4, Not 3.1–3.11, St 3.1–3.7),
pp. 14–16 (Prop 3.1, **St 3.9**, St 3.10, St 3.11, Not 3.13–3.14, St 3.13, St 3.14),
pp. 17–18 (St 3.16, Prop 3.2, St 3.17, St 3.18) via the cited packets' quotations,
pp. 26–27 (Λ(P) formula (18), Prop 5.6 (19), Prop 5.7),
pp. 28–32 (Not 6.1, St 6.1, St 6.2, Props 6.2–6.4, **Cor 6.1**),
pp. 34–37 (Lemma 6.1, **Prop 6.8**, Not 7.1, St 7.1–7.3, Prop 7.1, **Prop 7.3**),
pp. 38–39 (Prop 7.4, **Prop 7.5**, **Cor 7.1**, Not 8.1, St 8.1, Prop 8.1 head),
pp. 48–51 (Not 9.1, St 9.1–9.2, **St 9.3**, Not 9.3, **St 9.4**, Prop 9.2, **Prop 9.3**, St 9.6),
pp. 52–55 (St 9.6 proof with the (A)/(B)/(C) Diophantine, St 9.7, St 9.8).

The PDF stacked-fraction hazard was respected: every load-bearing formula quoted
here is a display line, and (24), St 3.9(ii)/(iii), Prop 7.3 and Prop 7.5 were
re-read as displayed blocks.

Packet hashes of this solve are in §12.

---

## 2. Ground truth: the four printed facts the whole solve rests on

### 2a. Statement 3.9 (p. 15), verbatim structure

> Let `h(x,y)` be a polynomial. Assume `kappa in N*` is suitable and has the
> property of Proposition 3.1. Then for any `F in T_a` with `kappa pi(F) in N`,
> and for any `c in C` such that `F * c` is defined, we have
> (i) `mult(p_{h,F}, c) = deg(p_{h,F*c})`.
> (ii) If `l = deg(p_{h,F*c})` and `p_{h,F}(eta) = sum_{j=l}^m a_j (eta-c)^j` and
> `p_{F*c} = sum_{j=0}^l b_j eta^j`, then `a_l = b_l`.
> (iii) `d_{h,F*c} = d_{h,F} - mult(p_{h,F}, c)/kappa`.

**Clause (ii) transports exactly one coefficient**: the *leading* coefficient of
the child pattern equals the *lowest* Taylor coefficient of the parent's top
pattern at `c`. It says nothing about `b_0, ..., b_{l-1}`. That single sentence
is the whole obstruction of this report.

### 2b. Where the remaining child coefficients live (derived, §8a)

Write `f^F(x,eta) = sum_j x^{j/kappa} p_j(eta)` (St 3.7), `n := kappa d_F`,
`p_n = p_F`. The proof of St 3.9 expands
`f^{F*c}(x,eta) = sum_j x^{j/kappa} p_j(x^{-1/kappa} eta + c)`, whose
`x^{(n-r)/kappa}` coefficient is `sum_{s=0}^{r} ([(eta-c)^s] p_{n-r+s}) eta^s`.
Since St 3.9(i)+(iii) make `d_{F*c} = d_F - m/kappa` with `m := mult(p_F,c)` and
`deg(p_{F*c}) = m`, every `r < m` layer must vanish identically, i.e.

```text
(V)   ord_c(p_{n-k}) >= m - k       for k = 0, 1, ..., m-1,
(C)   p_{F*c}(eta) = sum_{k=0}^{m} c_k eta^{m-k},   c_k := [(eta-c)^{m-k}] p_{n-k}.
```

`c_0 != 0` is St 3.9(ii). `c_1, ..., c_m` are the **first extra-branch jet** in
coordinates: they are precisely Grok's `(r_*, p_*)` read off the diagonal of the
subtop pieces.

### 2c. The descent geometry (St 3.10, St 3.13, Prop 3.1)

Prop 3.1(*): `deg(p_{h,I(u)})` is the number of Puiseux series of the fiber
agreeing with `I(u)` strictly below `u`. For `h = f - a` and
`u in [pi(F), u_0]` this equals `deg(p_{f,I(u)})`, since `d_f >= 0` there and a
constant cannot change the leading form.
St 3.10: `omega(u) := d_{I(u)}` is continuous, monotone decreasing, and locally
linear with slope `- omega^*(u) = - deg(p_{I(u)})`; `omega^*` is monotone
decreasing. Hence **`omega` is convex, piecewise linear, with integer slopes
that increase (in magnitude, decrease) exactly at the levels where the branch
group loses members.**
St 3.13: there is a unique `u_0` with `d_{I(u_0)} = 0`.
St 7.3 + St 7.1 + St 3.13 together force the cv flag of the branch to sit at
that same `u_0`, so `H = I_{P*}(u_0)` and `pi(H) = u_0 > 1`.

**Integrality.** Prop 7.3's geometric proof perturbs `a` to a generic `a*`,
uses St 3.14 to carry `p_F, p_{g,F}` unchanged, and obtains
`Lambda(Q) = kappa_G pi(G) - kappa_G = kappa_F pi(F) - kappa_F` for a point `Q`
with `mult(p_G - a*, c*) = 1`. `Lambda` is a pole/zero order of `g - b` at a
place — a positive integer ((18) on p. 26). Hence

```text
kappa_H (pi(H) - 1)  in  N*                                   (INT)
```

is **proved**, not merely a proof line of St 9.4. This report uses (INT) as a
theorem and records it as an upgrade of a pre-existing AF2 perimeter item.

### 2d. The corrected (24) as a special case

St 9.3 (p. 49) with the E6 sign repair (AF2 §1) reads, for `c* != 0`,
`kappa_H(pi(H)-1) >= D_F/mult(p_F,c*) - kbar_F`, `kbar_F := kappa_F(1-pi(F))`.
Its printed proof is exactly two inequalities: `kappa_H >= kappa_F`, and
St 3.11's `w - u >= d_F/mult(p_F,c*)`. Theorem A below identifies the *exact*
defect in each.

---

## 3. Normalization ledger

Four different constants are called `rho`, `i`, or `kappa` in this thread. They
are kept apart throughout; a single confusion silently changes every number.

| symbol | value on the A-step | value on the trunk | meaning / source |
|---|---|---|---|
| `i` (Prop 8.1) | `i_A = 2` | `i_F = 28(4+3t)` | `deg(p_F)/M*_F`; `f_F^+ = (xi^delta p)^i`; St 3.17(i) chain from the pole `Q=(2,4,3,2,5)` through `i_G = 14` |
| `mult_red` | `1` | `2` | multiplicity of the extra orbit in the **reduced** pattern (`Sm`) |
| `m = mult(p_F,c*)` | `i_A * 1 = 2` | `i_F * 2 = 56(4+3t)` | Prop 8.1(i); the branch count leaving in the extra direction |
| `D_F` | `X i = 14` | `X i = 17 i_F` | Not 9.1 slot 1 |
| `kbar_F` | `5` | `7` | Not 9.1 slot 5, `= kappa_F(1-pi(F))` |
| frame `rho` | `1/3` | `1/5` | `D_F/deg(p_F)` (DEPTH §1); campaign slope |
| ODE ratio `rho` | `21/15 = 7/5` | `85/35 = 17/7` | `deg p / deg q` of Prop 8.1(iv) via Cor 6.1 |
| `kappa_F` | `7 kappa_G` | `kappa_trunk` | Not 3.5, `= kappa_P/e_j`; `nu_F | kappa_F` |
| `nu_F` | `7` | `17` | Not 3.4 |
| `tau` | `kappa_A(u - pi(A))` | `kappa_T(u - pi(T))` | the normalized descent coordinate of §4 |

`i` never enters Prop 8.1(iv); it *does* enter every `D`, every `m`, and hence
every charge. The Fable review's `i = 14` pin at the merge and the derived
`i_A = 2` / `i_F = 28(4+3t)` are reproduced independently in the packet.
`kappa_F` never has to be known numerically: every charge below is a ratio in
which it cancels, except through the divisibility `nu_F | kappa_F`, which is used
once (in §8b) and is a printed consequence of Not 3.4/3.5.

---

## 4. Theorem A — the exact descent law

> **Theorem A.** Let `F in V_a cap T_a^searrow`, let `c* != 0` be a root of
> `p_F` with `F * c*` defined and `F * c* in T_a^nearrow`, put
> `m := mult(p_F, c*)`, let `P*` be a branch through `F * c*`, let `u_0` be its
> St 3.13 level and `H := I_{P*}(u_0) in T_{a,cv}`. Normalize
> `tau := kappa_F (u - pi(F))` and `N(tau) := deg(p_{I_{P*}(u)})`. Then
>
> 1. `N` is a non-increasing, integer-valued step function on `(0, tau_0]` with
>    `N(0^+) = m` and `N >= 1`, where `tau_0 := kappa_F(u_0 - pi(F))`;
> 2. `D_F = integral_0^{tau_0} N(tau) d tau`;
> 3. `kappa_F (pi(H) - 1) = tau_0 - kbar_F`;
> 4. `kappa_H / kappa_F = E_+ / E_0`, where `E_+ := kappa_{P*}/kappa_F` is the
>    number of conjugates of `P*` agreeing with it through `pi(F)`; in
>    particular `E_+ <= m`, so `kappa_H/kappa_F` divides `E_+` and is `<= m`;
> 5. `Delta(F, c*) := kappa_H(pi(H)-1) = (kappa_H/kappa_F)(tau_0 - kbar_F) in N*`,
>    and `tau_0 >= D_F/m` with equality **iff** `N == m` on `(0, tau_0]`.
>
> Consequently `Delta = D_F/m - kbar_F` exactly when the branch group through
> `F*c*` loses no member before `d` reaches `0` and `kappa` does not jump; and
> the corrected St 9.3(24) is the `N == m`, `kappa_H = kappa_F` case.

*Proof.* (1) is Prop 3.1(*) plus St 3.10(i): the set of series agreeing with
`P*` below `u` shrinks with `u`, starts at `deg(p_{F*c*}) = m` (St 3.9(i)), and
always contains `P*`. (2) is St 3.10(ii)+(iii): `omega` is continuous and its
slope is `-N`; rescaling `u` by `kappa_F` turns `d_F = omega(pi(F))` into
`D_F = kappa_F d_F`, and `omega(u_0) = 0` by St 3.13. (3) is
`kappa_F(pi(H)-1) = kappa_F(u_0-pi(F)) - kappa_F(1-pi(F))`. (4): `kappa_{I(u)}`
is the lcm of the denominators of the exponents of `P*` up to `u` (Not 3.5), so
`kappa_{I(u)} = kappa_{P*}/E(u)` with `E(u)` the number of conjugates of `P*`
still agreeing below `u`; `E` is a divisor chain, `E(pi(F)^+) = E_+` and
`E(u_0) = E_0`; and those `E_+` conjugates are among the `m` series counted by
`deg(p_{F*c*})`, giving `E_+ <= m`. (5) is (3), (4) and (INT); the inequality is
(2) with `N <= m`. `p_F` is `nu_F`-semi-invariant with `pi(F)` a characteristic
level, so `P*` inherits `kappa_{I(u)} = kappa_F` immediately above `pi(F)`; that
is what makes (4) start at `E_+`. QED

**Where the two printed inequalities lose.** `kappa_H >= kappa_F` loses exactly
the factor `E_+/E_0`; `w - u >= d_F/mult` loses exactly the area
`integral (m - N)`. Both losses are **separation events of the extra-direction
branch group**, and nothing else. That is the content of Theorem A.

Sanity, machine-checked: `local_charge(D=14, kbar=5, m=2, no drop) = 2` and
`local_charge(D=17 i_F, kbar=7, m=2 i_F, no drop) = 3/2`, reproducing the AF2
gaps exactly.

---

## 5. The A-step: a finite menu, and the exact equality condition

Data (recomputed in the packet, `t`-free): `l=2, nu=7, eps=0, k=1, Sm=1, lex=0`,
`(dp,dq,E) = (21,15,9)`, `(kbar,X,rho,w,M) = (5,7,1/3,2/3,3)`, `i_A = 2`,
`Q(F) = (14, 42, 7, 3, 5)` — the St 9.6(iii)(A) badge at `j = i = 2`. Reduced
pattern `p = (T-A)^2 (T-B)`, `T = eta^7`, `q = eta (T-A)(T-B)`, ODE ratio `7/5`,
and `B = (3/2) A` uniquely (L1 family C; re-derived here as the vanishing of one
linear form). Full pattern `p_F = ((eta^7-A)^2(eta^7-B))^2`, degree 42,
`mult(p_F, c_A) = 4`, `mult(p_F, c*) = 2` — both verified exactly in
`K = Q[eta]/(eta^7 - 3/2)`.

Because `m = 2`, `N` can take only the values `2` then `1`: **one** separation
event, at `theta := kappa_F(O(S_1,S_2) - pi(F))`. Theorem A gives

```text
tau_0 = 14 - theta   (theta <= 7),      tau_0 = 7   (theta >= 7),
kappa_F (pi(H)-1) = 9 - theta   or   2,
Delta_A = (kappa_H/kappa_F) * that.
```

`E_+ <= m = 2` gives `kappa_H/kappa_F in {1,2}`, and the two cases are exactly:

* **contact separation** (`E_+ = 1`): `S_2` belongs to a different place,
  `O(S_1,S_2)` is a `V_{2,a}` level, `kappa_H = kappa_F`, `Delta_A = 9-theta`;
  (INT) forces `theta in N*`, so `theta in {1,...,6}` and
  `Delta_A in {8,7,6,5,4,3}`, or `theta >= 7` and `Delta_A = 2`.
* **conjugate separation** (`E_+ = 2`, `kappa_{P*} = 2 kappa_F`): `S_2` is the
  conjugate of `S_1`; they part at a characteristic exponent `b/kappa_{P*}` with
  `b` odd, and `kappa_F pi(F) in Z` forces `theta in 1/2 + Z`, so
  `Delta_A = 2(9-theta) in {17,15,13,11,9,7,5}` for `theta < 7`, and `= 2` for
  `theta > 7` (there `u_0 < O`, so `E_0 = E_+` and `kappa` does not jump).

> **Theorem B.** `Delta_A in {2,3,4,5,6,7,8} u {5,7,9,11,13,15,17}`, and
> `Delta_A = 2` **iff** the two branches through `F * c*` do not separate before
> `d` reaches `0`, i.e. iff `deg(p_H) = 2` at the cv vertex.

This is a strict sharpening of both prior readings: Grok's "`lambda = 2` is the
linear-model value, compatible but unproved" becomes a decidable geometric
equality condition, and the "`lambda >= 3`" kill becomes "the pair separates
early", with an explicit menu of the resulting integers.

---

## 6. The merge: exactly 0, and why that is an identity

At `G` the reduced pattern is `(eta^{2 nu_G} - a^2)^3` — two nonzero orbits, both
of them *chain arrivals* — with `q = eta(eta^{2 nu_G} - a^2)`, `eps = k = lex = 0`.
Every root of `p_G` carries an incoming chain, so by St 3.18 there is no
direction `G * c*` other than the two `searrow` arrivals: `Y(G)^{exit}` is empty
and `lambda_G = 0` is an accounting identity (P2), not an AF2 floor. Theorem A
never fires here because there is no `c*`. This reproduces the Grok/Fable
finding without re-proving Prop 8.1(iv) on the family.

---

## 7. The trunk: `Delta = 2` needs an exact positive defect

Data: `l=3, nu=17, eps=0, k=1, Sm=2, lex=0`, `(dp,dq,E) = (85,35,20)`,
`(kbar,X,rho,w,M) = (7,17,1/5,2/5,5)`, `i_F = 28(4+3t)`, `m = 2 i_F`,
`D_F = 17 i_F`, gap `= 17/2 - 7 = 3/2`. Terminal `j = 3`, `psi = 1`.

Theorem A gives `Delta_trunk = (kappa_H/kappa_F)(tau_0 - 7)` with
`tau_0 >= 17/2`. By (INT), `Delta_trunk >= 2`.

> **Theorem C.** `Delta_trunk = 2` **iff** `kappa_H = kappa_F` and `tau_0 = 9`,
> equivalently iff the branch group sheds exactly one `i_F` unit of branch-area:
> `integral_0^{9} (2 i_F - N) d tau = i_F`. Any ramification jump is fatal:
> `(kappa_H/kappa_F) >= 2` gives `Delta_trunk >= 2*(3/2) = 3`.

*Proof.* `(kappa_H/kappa_F)(tau_0-7) = 2` with `tau_0 >= 17/2` forces the ratio
to be `1` (any larger integer gives `>= 3`), hence `tau_0 = 9`; and
`integral_0^9 N = D_F = 17 i_F` while the constant profile would give `18 i_F`. QED

So on the trunk the recorded AF2 floor `ceil(3/2) = 2` is attainable **only**
through a strictly positive, exactly-sized separation defect. One explicit
profile realizing it (verified in the packet, all `t`): exactly half the group,
`i_F` branches, leaves at `tau = 8`, one normalized step before `u_0`. Nothing
printed selects that profile, and nothing printed forbids it.

---

## 8. The jet layer: what is derivable, and what is not

### 8a. Two derived constraints on the subtop

**(V), the vanishing ladder**, was derived in §2b from St 3.9(i)+(iii) alone:
`ord_c(p_{n-k}) >= mult(p_F,c) - k` at every root `c` of `p_F` with `F*c`
defined. On the A-step this is `ord_{c*}(p_{n-1}) >= 1` and
`ord_{c_A}(p_{n-1}) >= 3`, `ord_{c_A}(p_{n-2}) >= 2`.

**(W), the semi-invariance weight law** — new here, and pinned:

> **Theorem D.** Let `F in V_{1,a}` with `nu_F >= 2` and `pi(F)` its own
> characteristic level. Write `f^F = sum_j x^{j/kappa} p_j(eta)`,
> `n = kappa d_F`. Then
> (i) `p_{n-k} == 0` unless `(kappa/kappa_F) | k`;
> (ii) for `k = (kappa/kappa_F) k'`, the polynomial `p_{n-k}` is supported on
> `eta`-exponents congruent to `(k' - D_F) N_1^{-1} (mod nu_F)`, where
> `N_1 := kappa_F pi(F) mod nu_F`. Since `nu_F | kappa_F` (Not 3.4/3.5),
> `N_1 = (- kbar_F) mod nu_F` — a datum of `Q(F)` alone.
> (iii) `k' = 0` recovers St 3.16's `l` for the top pattern.

*Proof.* Apply `x^{1/kappa} -> zeta x^{1/kappa}` (which fixes `x` and `y`) to
the identity `f(x,y) = sum_j x^{j/kappa} p_j(eta_F)` of St 3.7/Not 3.9. For
`zeta` in the stabilizer of the truncation (order `kappa/kappa_{F^o}`),
`eta_F -> omega eta_F` with `omega = zeta^{kappa pi(F)}`, and matching
`x^{j/kappa}` gives `p_j(omega eta) = zeta^{-j} p_j(eta)`. The kernel of
`zeta -> omega` has order `kappa/kappa_F` and kills every `p_j` whose index is
not divisible by it, which is (i) after `kappa d_F = (kappa/kappa_F) D_F`. On the
survivors, writing `xi := zeta_0^{kappa/kappa_F}` (a generator of `mu_{nu_F}`)
and `omega_0 = xi^{N_1}` gives (ii). QED

On the A-step, `kbar_F = 5`, `nu_F = 7`, so `N_1 = 2`, `N_1^{-1} = 4`, and

```text
e_0 = 0   (matches the printed l = 0),    e_1 = 4,    e_2 = 1     (mod 7).
```

On the trunk, `kbar_F = 7`, `nu_F = 17`: `N_1 = 10`, `N_1^{-1} = 12`, and
`e_0 = 0`, `e_1 = 12`, `e_2 = 7`. In both cases `e_2 = 2 e_1 (mod nu_F)` and
`e_0 = 0` reproduces St 3.16 — a non-trivial consistency check the packet runs.

### 8b. Theorem E — the jet is not determined

> **Theorem E.** Fix the A-step vertex `F` with all of: `Q(F) = (14,42,7,3,5)`;
> the full pattern `p_F = ((eta^7-A)^2(eta^7-B))^2` with `B = (3/2) A`; the
> h-pattern `q = eta(eta^7-A)(eta^7-B)`; `i_A = 2`; the entire preceding
> characteristic jump from the pole `Q = (2,4,3,2,5)`; (V); and (W) with the
> pinned weights `e_1 = 4`, `e_2 = 1`. Then the discriminant of
> `p_{F*c*}(eta) = c_0 eta^2 + c_1 eta + c_2` is still a non-constant affine
> function of the single scalar `c_2 = p_{n-2}(c*)`. Both
> `disc != 0` and `disc = 0` are realized by admissible subtop pieces, giving
> `theta = 1` (`Delta_A = 8`) and a jet compatible with `theta >= 7`
> (`Delta_A = 2`) respectively.

*Proof and construction.* Take, with `A = 1`, `B = 3/2`, gauge-free:

```text
p_{n-1}(eta) = eta^{4} (eta^7 - 1)^3 (eta^7 - 3/2)            (weight e_1 = 4)
p_{n-2}(eta) = eta^{1} (eta^7 - 1)^2 * s                      (weight e_2 = 1)
```

Both satisfy (W). `ord_{c*}(p_{n-1}) = 1` and `ord_{c_A}(p_{n-1}) = 3` satisfy
(V); `ord_{c_A}(p_{n-2}) = 2` satisfies (V). Then
`c_0 = [(eta-c*)^2] p_F != 0` (St 3.9(ii)), `c_1 = p_{n-1}'(c*) != 0`, and
`c_2 = s * p_{n-2}^{unit}(c*)` is a free `C`-multiple of a fixed nonzero element
of `K`. The map `s |-> c_1^2 - 4 c_0 c_2` is affine with nonzero slope, so:

* **Jet E** (`s = 1`): `disc != 0`, `p_{F*c*}` has two distinct roots, the pair
  separates at the first available level, `theta = 1`, `Delta_A = 8`.
* **Jet L** (`s = 3/8`, computed exactly in `K` and verified to be a *rational*
  scalar — i.e. realizable inside the pinned weight class): `disc = 0`,
  `p_{F*c*} = c_0(eta - c_1/(2c_0))^2`, the pair does **not** separate at the
  first level, and the same freedom recurs at `F * c* * c^{(1)}`, where
  Prop 8.1 no longer applies at all (`F*c* in T_a^nearrow`).

The rationality of the tuning constant is exactly the weight law `e_2 = 2 e_1`
at work: the packet's scan confirms that on-weight the square jet is realizable
for every admissible `e_1`, and off-weight it is **not** — so (W) is
load-bearing and still insufficient. QED

**Minimal missing source datum.** In one line: *the value at `c*` of the second
subtop homogeneous piece of `f^F`*, i.e. the `K`-scalar `p_{n-2}(c*)` (and, if
that is tuned to the square, its analogues one microstep deeper). Equivalently
and intrinsically: **the contact level `O(P*, P**)` of the two branches leaving
the A-vertex in the extra direction** — a `V_{2,a}` datum of the actual `f`, not
a pattern datum. On the trunk the same datum is the whole degree profile `N` of
the `2 i_F`-member group. Neither is a consequence of Prop 8.1(iv), of the
Q-datum, or of St 3.9.

### 8c. Top-pattern identity vs source-realizability

Kept strictly apart:

* **Top-pattern identities** (proved, vertex-local): `B = (3/2)A` at the A-step,
  `D = (4/3)C` at the trunk, opposite orbits at the merge, `i_A = 2`,
  `i_G = 14`, `i_F = 28(4+3t)`, (V), (W), Theorems A–D.
* **Source-realizability assertions** (NOT made): that any particular jet, any
  particular `theta`, or any member of the affine family is realized by an actual
  polynomial pair `(f,g)`. Jets E and L are *formal fillings compatible with the
  printed local constraints*, nothing more. Exhibiting a global `f` realizing
  either is the JC2 question itself and is not attempted.

---

## 9. Theorem F — the budget knife-edge

> **Theorem F.** Along either pole's characteristic sequence the St 9.4(25)
> ceiling is `td - 1 - psi = 8 - 1 - 1 = 6`. The priced vertices are `A_1`,
> `A_2`, `G`, the trunk, and `(0,y)`; `lambda_G = 0` exactly (§6); and each of
> `Delta_{A_1}, Delta_{A_2}, Delta_{trunk}` is an integer `>= 2`. Therefore the
> route survives the exact-lambda gate **iff**
> `Delta_{A_1} = Delta_{A_2} = Delta_{trunk} = 2` and `lambda_{(0,y)} = 0`.
> Moreover Prop 7.5 then forces `delta_a = 0` and
> `T_{a,cv} = {H_1, H_2, H_tr, H_x}` with weights `2, 2, 2, 1` and no other cv
> vertex at that `a`.

*Proof.* The floors are the corrected (24) plus (INT) (`3/2 -> 2` on the trunk);
`2+2+0+2 = 6` already meets the ceiling, so no slack exists. For the last part,
Prop 7.5 reads `td = 1 + sum_{cv} kappa(pi-1) + sum_a delta_a` with `delta_a >= 0`
(Prop 7.4); `td - 1 = 7 = 2+2+2+1` exhausts it, and the St 9.4 proof's `(0,x)`
cv vertex carries `>= psi = 1`. QED

Two consequences worth recording.

* **`t`-uniform kill.** `Delta_A >= 3` at a *single* A-copy gives `>= 3+2+2 = 7 > 6`
  and kills every member of the affine family simultaneously. The A-step's
  Q-datum, extra ratio `B=(3/2)A`, `m = 2`, `kbar = 5`, `D = 14`, weights
  `(e_1,e_2) = (4,1)` and menu are all `t`-free; only `kappa_A = 7(4+3t)kappa_{tr}`
  carries `t`, and it enters `theta` only through the choice of unit. Whether
  `theta` itself is `t`-free is *not* settled here — recorded as open.
* **The gate is exactly one bit per priced vertex**, not a size question: "does
  the extra-direction group separate before `d = 0` (A-copies), and does it shed
  exactly one `i_F` unit (trunk)".

---

## 10. Packet, tests, mutations

Packet: `cases/m2_td8_first_extra_jet_exact_lambda_opus5_20260829/`.

```sh
cd cases/m2_td8_first_extra_jet_exact_lambda_opus5_20260829
python3 test_first_extra_jet_td8.py      # TD8_FIRST_EXTRA_JET_OPUS5_TEST_PASS checks=411
python3 -O test_first_extra_jet_td8.py   # identical
python3 first_extra_jet_td8.py --json
```

The packet contains **no `assert` statement** (grep-verified), so the `-O`
identity is structural rather than accidental.

Check census, 411 per suite: 170 route / i-chain / frame checks over
`t in {0,1,2,3,7,20,100,1000}` including two invalid-`t` rejections; 77
descent-law checks (gap recovery, the `9 - theta` closed form against an
independent integrator at 27 rational levels, multi-drop profiles, five
convexity guards, ramification scaling); 38 A-step menu checks (contact and
conjugate families, parity, integrality filter, positivity guards); 48 trunk
checks over `t in {0,1,4,33}` (half-drop realization, under- and over-shoot
controls, ramification exclusion); 21 budget checks; 34 jet-layer checks (pinned
weights at both vertices, vanishing ladder, `K`-arithmetic, the two jets, the
14-entry on/off-weight scan); 15 in-suite mutation controls; 8
certificate / firewall / stdout-identity checks.

Independent `/tmp` mutations of a producer copy (packet untouched), 10/10
rejected, 0 survivors:

| mutation | rejected by |
|---|---|
| gap sign flipped (the printed, unrepaired (24)) | A gap `12 != 2` |
| charge law drops the `kbar` shift | 37 checks |
| `tau_lin` taken as `X - kbar = 2` instead of `D/m = 7` | A menu missing `theta=6` |
| `i` dropped from the trunk multiplicity | degree profile becomes illegal |
| `i_G` misidentified as `7` (reduced-over-reduced) | same |
| weight law broken (`e_2 := e_1`) | square jet unrealizable on-weight |
| weight `N_1 := +kbar` instead of `-kbar` | pinned weights `(2,0,4,1)` fail |
| forced vanishing dropped from `p_{n-1}` | square jet unrealizable |
| late-separation collapse removed | `theta = 7` gives `4 != 2` |
| extra-orbit ratio `B = 2A` instead of `3A/2` | 2 checks |

---

## 11. Clause-level claim firewall

| clause | status |
|---|---|
| St 3.9(ii) pins only the leading child coefficient | PINNED (verbatim, p. 15) |
| Vanishing ladder `ord_c(p_{n-k}) >= m-k` | DERIVED from St 3.9(i)+(iii) |
| Child pattern `= sum c_k eta^{m-k}` with `c_k` the subtop diagonal | DERIVED |
| `nu_F`-semi-invariance of subtops, weights pinned by `(kbar_F, nu_F, D_F)` | DERIVED (Theorem D), new |
| `e_0 = 0` reproduces St 3.16's printed `l = 0` | VERIFIED at both vertices |
| Exact descent law `Delta = (kappa_H/kappa_F)(tau_0 - kbar_F)` | PROVED (Theorem A) |
| Corrected (24) is the constant-profile case | PROVED |
| `kappa_H(pi(H)-1) in N*` | PROVED via Prop 7.3 + (18) (upgrade of an AF2 perimeter item) |
| `kappa_H/kappa_F` divides `E_+ <= m`; on the A-step `in {1,2}` | PROVED |
| A-step menu `{2..8} u {5,7,...,17}` | PROVED (Theorem B) |
| `Delta_A = 2 <=> deg(p_H) = 2` | PROVED |
| Trunk `Delta = 2 <=> kappa_H = kappa_F` and `tau_0 = 9` | PROVED (Theorem C) |
| Merge `lambda_G = 0` exact | CONFIRMED (P2 identity; St 3.18) |
| All three exit charges forced to exactly 2; `lambda_{(0,y)} = 0`; `delta_a = 0` | PROVED (Theorem F) |
| The jet `(r_*, p_*)` derivable from St 3.9 + jump + tops | **REFUTED** (Theorem E) |
| Two admissible jets with charges 8 and 2 exhibited | PROVED at printed-constraint scope |
| Either jet realized by an actual polynomial pair | NOT CLAIMED |
| Uniform `Delta >= 3` at any priced vertex | NOT DERIVABLE (unchanged) |
| Exact `Delta = 2` at any priced vertex | NOT PROVED (unchanged) |
| Route killed / route promoted | NEITHER |
| `theta` constant in `t` | OPEN (recorded, not asserted) |
| Prop 8.1(iv) on the family, completeness of td=8 merges | USED as reviewed input / NOT CLAIMED |
| Source landing, Keller realizability, counterexample, degree ceiling, JC2 | NOT CLAIMED |
| AWS launched; canonical file edited; commit/push; `jc2-lean` accessed | NONE |

---

## 12. Next lemma, and seals

**Next lemma (contact lane, not this packet).** The gate is now one `V_{2,a}`
question per A-copy: *does the two-member branch group leaving the A-vertex in
the `B`-orbit direction have contact `O >= pi(F) + 7/kappa_F`?* Equivalently, is
`deg(p_H) = 2` at its cv vertex? Two attacks are visible and neither needs the
subtop values:

1. **Prop 7.1 at a `deg(p) = 2` cv vertex.** With `p := p_H` quadratic, the
   recursion `r_{j+1} = r_j^{k_j} - s_j p^{l_j}` must satisfy
   `deg(r_j) = (l_j/k_j) * 2` for `0 <= j <= m_H - 1`. That is an integrality
   ladder on the `(k_j, l_j)` of the cv vertex; if it is unsatisfiable for every
   admissible `(K,L,S)` compatible with `td = 8` and `Lambda(P) = 2`, then
   `Delta_A >= 3` and the whole affine family dies for all `t`.
2. **Prop 7.5 with `delta_a = 0` and a four-element `T_{a,cv}`** of weights
   `2,2,2,1`. Theorem F makes that a *closed* configuration; a census of
   `(Lambda(P), kappa_{F_P}, pi(F_P))` against Prop 5.6 (19) and Prop 5.8 (20)
   at `td = 8` with two `Lambda = 4` poles is a finite check that the transport
   lane can run without any AWS.

Neither is attempted here. Nothing in this report restores a prime-`td`
exclusion, a cofinal bound on `td`, or a Keller counterexample.

**Packet seals.**

```text
e2a4dcbb83ed53c9fd333339a436ee447aeccaf6a2dde7ad6f7b8483b1261cd5  first_extra_jet_td8.py
c5330c19e7529be8f7cefa21abf8754709d576674e2b0c4a12e4a2dfa35d5d4d  test_first_extra_jet_td8.py
3066d1c25dec8b732e65c7a145b9c0e3b8b281d807de420ccdf5719554b51bc8  README.md
2c80cf51187822ef16221d44385bfa8e3efad214a55c24999c4f53ffa3754100  charged JSON stdout
4b20f925a2c5c5344a88a3714f1c5106b1a7f2dda934c374cd66cf7fb9c42879  certificate (sorted compact JSON, hash key removed)
```

**Reproduction.**

```sh
python3 -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('xmodel/m2-td8-first-extra-jet-exact-lambda-primary-opus5-20260829.md').read_bytes()).hexdigest())"
cd cases/m2_td8_first_extra_jet_exact_lambda_opus5_20260829
python3 test_first_extra_jet_td8.py
python3 -O test_first_extra_jet_td8.py
python3 first_extra_jet_td8.py --json | shasum -a 256
```

---

*Report body ends. Self-hash below covers everything above this line.*

report_body_sha256 = f1ae6c2b1dd94ab2dcf26dfb16e149067eab0617b549817d5620c728d6936d11
