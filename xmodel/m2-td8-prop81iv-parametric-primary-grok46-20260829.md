# Primary research — td=8 affine family, Prop. 8.1(iv)

Lane: Grok 4.6, independent primary research, not a referee of an Opus
solve. Date: 2026-08-29. Object: the parametric reduced ODE on the
equal-join affine merge cell of
`xmodel/m2-td8-equal-join-route-family-sol56-20260829.md`.

Packet: `cases/m2_td8_prop81iv_parametric_grok46_20260829/`.

No access of any kind to `jc2-lean`. No web, AWS, Singular, msolve, Sage,
PARI, or other heavy CAS. Arithmetic is desk `int` / `Fraction`. Canonical
files were not edited. Ordinary and `-O` tests plus adversarial mutations
were run. Opus output produced after the prompt was not read.

---

## 0. Verdict

**`PROVED` at local Prop. 8.1(iv) formal-cell scope.**

For every integer `t >= 0` the affine cell

```text
nu = 4+3t,
(dp, dq, M, kbar, X, rho_frame, w) = (24+18t, 9+6t, 3, 6+4t, 16+12t, 2/3, 4/3)
```

admits an explicit admissible solution of the printed identity
`delta p q' - (1-u) p' q = ⊖ p`, unique up to scale, over `Q`. There is no
log/residue obstruction and no exceptional `t`. The reduced patterns are

```text
p(eta) = (eta^nu - a)^3 (eta^nu + a)^3 = (eta^{2 nu} - a^2)^3,
q(eta) = eta (eta^nu - a)(eta^nu + a) = eta (eta^{2 nu} - a^2),
a != 0,
```

with gauge `a = 1` giving `p, q in Z[eta]`. Every printed root / eta /
simple-root / nonzero-constant / searrow / root-mult / `M` / `gcd(M,nu)`
condition holds identically.

**`PARTIAL` as a route, lambda, landing, or JC2 theorem.** Those gates are
not solved and are not claimed. Local formal survival of an infinite
family is the opposite of a degree bound.

The preferred outcomes, in the brief's order: a uniform log obstruction
does not exist; the exceptional set is empty; an explicit admissible
formal solution family is written below.

---

## 1. Custody

Files read, and only these, for mathematics:

- `xmodel/m2-td8-equal-join-route-family-sol56-20260829.md`
  (full `9a778862816aa96d251c33aac7e98a2fb3bfc1b3fc7c83f4463ac862de31815a`,
  body `bd35c43baf91c6306d4bb651a09e4886340ab7eb836ffd41d6b1ba6a85ea02d7`);
- `xmodel/m2-td8-equal-join-route-family-hostile-review-grok46-20260829.md`
  (body `a53a78dbabaaa6f1c2a30247ad016b99bf2d2011132736a2e8b7c5f098552c49`);
- `cases/m2_td8_equal_join_route_family_r1_20260829/` (producer, tests,
  README; hashes as in the Sol report);
- `refs/sigray_full.pdf` printed pp. 17–19, 23, 32, 39–41, 48
  (Not. 8.1, Prop. 8.1, St. 8.2, Cor. 6.1, St. 3.16–3.18, Prop. 4.6,
  Not. 9.1);
- `ladder/SHEET6-L1.md`, `ladder/SHEET6-A3L1-REVIEW.md`,
  `ladder/SHEET6-MULTIPOLE.md` (MP1–MP2, R2.3/O as cited),
  `ladder/BOOK-OFFAXIS.md` §§6–7 R1.0–R2.3 and §11 T1,
  `ladder/BOOK-OFFAXIS-REVIEW.md` §1 R1.0,
  `ladder/SHEET6-DEPTH.md` §1 i-normalization,
  `cases/l1_ode_check.py`.

Packet hashes of this solve:

```text
ce8bfc54d1cec0057dd840fb9f1b4613332cf4c42199e579cbd855d46a6ec320  prop81iv_td8_affine.py
46ab374fa7ae64a7c9b270e7c74829ded9c09d876e8ef319376b8f2a96188d64  test_prop81iv_td8_affine.py
024438a665672115d2b7f8f15ba01322e61a66d0b0d7cb23f51078a467e262c3  README.md
a3d59f3b75255056847d8b7d871996ae0d8c961c225df5cc9b29fd9dc585f513  charged JSON stdout
```

Certificate SHA-256 (sorted compact JSON without the hash key):

```text
6935db46999f1da2640154ab8155223df875b8d4609851cb7e6a6094c6f107a8
```

Ordinary and `-O` suites each print
`TD8_PROP81IV_PARAMETRIC_GROK46_TEST_PASS checks=1362`.

---

## 2. Printed identity and hypotheses

Prop. 8.1 (printed pp. 39–41). For `F in T_a^&`, `u := pi(F)`,
`i := deg(p_F)/M*_F in N*`, there exist a polynomial `p` and `delta in Q`
with `(xi^delta p(eta))^i = ⊖ f_{F+}`, a polynomial `q` with
`k = i(mu_F - 1)`, and

```text
(iii)  J(xi^delta p(eta), xi^{1-u} q(eta)) = ⊖ xi^{delta - u} p(eta),
(iv)   delta * p * q' - (1-u) * p' * q = ⊖ p,
(v)    M_F = gcd(deg p, deg q).
```

Not. 8.1: `M_F` is the gcd of `deg p_F` with all `deg p_{h_j,F}`;
`M*_F` omits `h_m`. DEPTH §1: the full `f`-pattern satisfies
`p_full = ⊖ (xi^delta p_red)^i`, so `deg(p_F) = i * deg(p_red)` and
`deg(p) = M*_F`. The Jacobian expansion of (iii) with first argument
`xi^delta p(eta)` is exactly (iv).

Hypotheses used, all printed:

- `F` is a searrow vertex other than `(0,y)` (the merge is in `V_{1,a}`,
  `nu >= 4`), so Cor. 6.1 supplies case (16): top degree of (iv) cancels
  and `rho := delta/(1-u) = deg(p)/deg(q)`.
- `delta != 0` and `1-u != 0` (St. 8.2's own hypotheses). The second is
  immediate from `kbar = kappa(1-u) = 6+4t != 0`; the first from
  `rho in Q>0`.
- R1.0 / the root law, derived from (iv) by valuation: every `p`-root is
  simple in `q`; every off-`p` `q`-root is simple; `eta` divides `q`
  exactly once for `nu >= 2`; hence `dq ≡ 1 (mod nu)` and
  `gcd(M, nu) = 1`. At a `p`-root of multiplicity `mu*` the order-`mu*`
  coefficient forces `rho != mu*`, i.e. `dp != mu* dq`.
- St. 8.2: searrow iff `deg(q) * mult(p,c) > deg(p)`.
- St. 3.16: `p(eta) = eta^l ptilde(eta^nu)`; here `l = 0`.
- St. 3.18: one tree continuation per `nu`-orbit.

The campaign frame `rho_frame = 2/3` is `D / deg(p_full) = X / dp`. It is
**not** the ODE ratio. Confusing the two is the main normalization trap
on this cell.

After dividing (iv) by `1-u`, the coefficient problem is the
chart-independent equation

```text
rho * p * q' - p' * q = ctilde * p,   ctilde = ⊖ / (1-u) != 0,
rho = deg(p)/deg(q).
```

The split of `(delta, u)` depends on the auxiliary integer `kappa` of the
`(xi, eta)` chart (`kbar = kappa(1-u)`, `X = kappa * delta`). Only the
ratio `rho` enters (iv) after Cor. 6.1. No numerical `u = pi(F)` is
claimed.

---

## 3. Full/reduced pin of the affine cell

The Sol family is the equal-arrival merge with two nonzero edges
`(mu, w_arr) = (3, 2/3)`, `eps = k = lex = 0`. R2.2 therefore forces the
reduced `eta`-patterns, which **are** the Prop. 8.1 polynomials:

```text
p(eta) = (eta^nu - c1^nu)^3 (eta^nu - c2^nu)^3,     deg p = 6 nu = 24+18t,
q(eta) = eta (eta^nu - c1^nu)(eta^nu - c2^nu),      deg q = 2 nu + 1 = 9+6t.
```

| quantity | value | source |
|---|---|---|
| reduced `deg p` | `6 nu = 24+18t` | R2.2, two orbits of mult. 3 |
| reduced `deg q` | `2 nu + 1 = 9+6t` | R1.0, `r0=2`, `k=lex=0` |
| `M*_F` | `6 nu` | Prop. 8.1: `deg p = M*` |
| `M_F` | `gcd(6 nu, 2 nu+1) = 3` | Prop. 8.1(v); `2 nu+1 = 3(3+2t)` |
| `i` | `14` | St. 3.17(i) chain below |
| full `deg p_F` | `i * 6 nu = 84 nu` | DEPTH §1 |
| `D` | `X * i = 56 nu` | `X = D/i` |
| `rho_frame` | `D / deg(p_full) = 2/3` | campaign `rho` |
| `rho_ODE` | `deg p / deg q = 6 nu / (2 nu+1)` | Cor. 6.1 |
| `X/kbar` | `4 nu / (6+4t) = 6 nu/(2 nu+1)` | equals `rho_ODE` |
| `kbar` | `6+4t` | `w_arr * dq` |
| `w` | `4/3` | reduced successor, not `pi(F)` |
| `delta / (1-u)` | `rho_ODE` | definition of `rho` |
| coefficient field | `Q` | gauge `a=1` |
| `⊖`-normalized constant | `ctilde = rho_ODE * pi` | §5; `pi = -a^2` |

The integer `i = 14` is **not** the handshake quotient
`deg(p_H^{red}) / mu = 21/3 = 7`. That 7 is `i_G / i_A = 14/2`. The
Prop. 8.1 exponent is the full-pattern one:

```text
Q(pole) = (2, 4, 3, 2, 5)          =>  deg(p_pole full) = 4,
St. 3.17(i): 4 = i_A * l_A = i_A * 2   =>  i_A = 2,
A-step reduced dp = 21                 =>  deg(p_A full) = 42,
St. 3.17(i): 42 = i_G * mu = i_G * 3   =>  i_G = 14.
```

The ODE in `rho` form does not use `i`. The pin is required to stop the
`i = 7` misidentification, which would corrupt full-degree / `D`
bookkeeping but not the coefficient problem.

Orbit/root shape: two distinct nonzero `nu`-orbits of reduced
multiplicity 3, no 0-root, no non-chain `p`-root, no extra `q`-orbit.
This is the R2.3(ii) `l = 0` no-resonance cell. Searrow
`3(2 nu+1) > 6 nu` is the identity `3 > 0`, so the mixed-`mu` (S)-prune
of R2.3(ii) does not fire. T1 of BOOK-OFFAXIS §11 is a zero-chain law
(`p = (t-A)^mu`) and does not apply; in any case `dp` does not divide
`dq` here.

R2.3(i) (proportional `q = ⊖ p^h eta^s`) also does not apply:
`q = eta * r` and `p = r^3` is not a polynomial power of `p`.

---

## 4. Reduction of (iv) to a quadratic identity

Write `t_var = eta^nu`, `r = (t_var - a)(t_var - b) = t_var^2 - sigma t_var + pi`,
`p = r^3`, `q = eta * r`. This is the same substitution as
SHEET6-A3L1-REVIEW Front 6 / `l1_ode_check.py` family A, with extras
absent and multiplicity 3.

```text
p'(eta) = r'(t_var) * 3 r^2 * nu eta^{nu-1},
q'(eta) = r + nu t_var r'.
```

The `rho`-normalized ODE becomes, after dividing by the nonzero
polynomial `r^2`,

```text
E(t_var) := rho * r + nu * t_var * (rho - 3) * r'   =   ctilde.
```

`E` is of degree 2. The three coefficients are rational in `nu`:

```text
[t_var^2]  = rho + 2 nu (rho - 3)
           = 6 nu/(2 nu+1) + 2 nu (6 nu/(2 nu+1) - 3)
           = 0,     identically (Cor. 6.1),

[t_var^1]  = - sigma * (rho + nu (rho - 3))
           = - sigma * 3 nu / (2 nu+1),

[t_var^0]  = rho * pi.
```

The `t_var^1` factor `3 nu/(2 nu+1)` is nonzero for every `nu >= 2`.
Hence `E` is constant if and only if `sigma = 0`. Then
`ctilde = rho * pi`, which is nonzero if and only if `pi != 0`.

`sigma = 0` is `a + b = 0`, i.e. opposite orbit values. `pi != 0` is
`a != 0`, which is also distinctness (`a != -a`) and the eta-law
(`r(0) != 0`). One scale remains; the gauge `a = 1`, `b = -1`,
`pi = -1` is defined over `Z`.

The same `t_var^1` factor, with 3 replaced by a general equal
multiplicity `mu`, is `nu mu / (2 nu+1) != 0`. Opposite orbits are
therefore the unique-up-to-scale solution of every equal-`mu`
two-orbit `l = k = eps = 0` cell, not a `mu = 3` accident. The affine
constraint `nu = 4+3t` is kbar-integrality, not an ODE constraint: the
same patterns solve (iv) at neighbouring `nu` as well, and those `nu`
are simply not cells of the family.

There is no integration step and no partial-fraction residue. The L1b
log obstruction (nonzero residues of `p^{-(l+2)/2}` at even `l`, `nu = 1`)
does not occur.

---

## 5. The explicit family, and the full `eta` identity

For every integer `t >= 0`, with `nu = 4+3t` and gauge `a = 1`:

```text
p(eta) = (eta^{2 nu} - 1)^3,
q(eta) = eta (eta^{2 nu} - 1),
rho    = 6 nu / (2 nu + 1),
ctilde = - 6 nu / (2 nu + 1) != 0.
```

Let `S = eta^{2 nu} - 1`. Then `p = S^3`, `q = eta S`, and

```text
rho p q' - p' q
  = S^3 * ( (rho + 2 nu (rho - 3)) eta^{2 nu} - rho )
  = S^3 * ( 0 - rho )
  = ctilde * p.
```

This is an identity of polynomials in `eta`, uniform in `nu`, hence
uniform in `t`. Samples: `t = 0` gives `ctilde = -8/3`; `t = 1` gives
`-14/5`; `t = 2` gives `-20/7`. The two `nu`-orbits of `eta^nu = 1` and
`eta^nu = -1` are distinct because no `nu`-th root of unity squares to
`-1` in the value of `eta^nu` (`zeta^nu = 1 != -1`). They are not a
single stabilizer-`2 nu` orbit: the Q-datum `nu` is `4+3t`, and
St. 3.16 is `p = ptilde(eta^nu)`.

Uniqueness up to scale: the `(sigma, pi)`-plane has one linear
constraint independent of `pi`, so the solution is the line `sigma = 0`,
`pi != 0`. Projectively, one point. Swapping the two orbits is the same
solution.

---

## 6. Printed side conditions, all of them

Checked identically in `t`, not only the ODE coefficients.

| condition | status |
|---|---|
| identity (iv) in `rho` form | holds, `ctilde = -6 nu/(2 nu+1)` |
| `⊖ != 0` | `ctilde != 0` and `1-u != 0` |
| Prop. 8.1(v) `M = gcd(deg p, deg q)` | `= 3` |
| R1.0: each `p`-root simple in `q` | q-mult 1 on both orbits |
| R1.0: off-`p` `q`-roots simple | no extras |
| R1.0: `eta ‖ q` exactly once | `q = eta * S`, `S(0) != 0` |
| `dq ≡ 1 (mod nu)` | `2 nu+1 ≡ 1` |
| `gcd(M, nu) = 1` | `gcd(3, 4+3t) = 1` |
| `rho != mu = 3` | `6 nu != 3(2 nu+1)` |
| St. 8.2 searrow on both edges | `3(2 nu+1) > 6 nu` |
| root-mult (R) | `dp != 3 dq` |
| St. 3.16 | `p = ptilde(eta^nu)`, `l = 0` |
| St. 3.18 two distinct orbits | `a != -a` |
| roots nonzero | `pi != 0` |
| `kbar in Z`, `nu >= 2` | family `t >= 0` |

No further printed local constraint remains. St. 8.5 exempts `V_{2,a}`
and is not needed: the vertex is typed `V_{1,a}` by DS1, and the
argument never used `M`-descent through the merge.

---

## 7. The four gates

**1. Local formal cell survival under Prop. 8.1(iv).**
SURVIVES, all `t >= 0`, explicit coefficients. This is the theorem.

**2. Exact lambda versus recorded lower bound.**
Not upgraded. The merge itself has `k = lex = eps = 0`, so under P2
there is nothing to price and the merge contribution 0 is exact as a
P2 accounting identity. The two incoming `(21,15)` steps and the
`(85,35)` trunk still carry recorded AF2 floors of 2 each. Local
solvability of those patterns (the A-step is the St. 9.6(iii)(A) shape
solved in L1 family C at `B = (3/2)A`) does not compute their true
lambda. If any of those three actual lambdas strictly exceeds 2, St. 9.4
kills the route. The recorded sum 6 meeting `td-1-psi` is still only
filter survival.

**3. Source landing / geometric realizability.**
Not claimed. The merge solution is rigid (`b = -a`). Each incoming
A-step is itself rigid. Matching the two sides through the actual
substitution of St. 3.9, beyond degrees and top coefficients, is a
transport problem. Opposite orbits at `G` may or may not be reachable
from two copies of `B = (3/2)A`. That computation is not this packet.

**4. Degree bound or JC2.**
None. An infinite affine family of locally admissible formal merge cells
at fixed `td = 8` is a positive formal-cell statement. It does not bound
topological degree and does not produce a Keller map.

---

## 8. Packet, tests, mutations

Packet: `cases/m2_td8_prop81iv_parametric_grok46_20260829/`.

```sh
cd cases/m2_td8_prop81iv_parametric_grok46_20260829
python3 test_prop81iv_td8_affine.py
python3 -O test_prop81iv_td8_affine.py
python3 prop81iv_td8_affine.py
```

Check census, 1362 per suite: 1 (`i`-chain) + `81*16` (family box
`t = 0..80`: degrees, `M`, `kbar`, `X`, `i`, both `rho`s, `w`, closed
`t^2`/`t^1` forms, side-condition bundle, `sigma`, `ctilde`) + 39
(full `eta` identities `t = 0..11` and three rational gauges) + 4
(uniqueness scans) + 10 (in-suite mutations) + 11 (certificate /
firewall / stdout identity) + 1 (invalid `t`).

Independent `/tmp` reconstruction, packet not imported: the three
reduced coefficients as rational functions of `nu`, including
`nu = 4+3*1000`; full `eta` identities at `t = 0..7, 10, 15`;
Jacobian/`rho` form at `t = 0`; `i`-chain. All matched.

`/tmp` mutations of a producer copy, packet untouched:

| mutation | result |
|---|---|
| `sigma = 1` | `reduced E is not constant after sigma=0` |
| `rho_ODE` replaced by frame `2/3` | `ODE rho is not 6 nu / (2 nu + 1)` |
| `p = S` instead of `S^3` | `deg p mismatch` |
| `i = 7` | `i_prop81 disagrees with the pole/A-step chain` |

In-suite mutations additionally reject `pi = 0`, a dropped `eta` factor,
an extra `q`-orbit, and the R2.3(i) proportional pattern `q = eta p`.
Equal-`mu = 2` with the same opposite-orbit gauge **does** solve the
shape ODE (positive control that the `sigma = 0` law is `mu`-uniform);
the cell's multiplicity remains 3.

No AWS design is required: the honest computation is a degree-2 identity
in one variable, uniform in `t`.

---

## 9. Clause-level claim firewall

| clause | status |
|---|---|
| Printed (iv) is `delta p q' - (1-u) p' q = ⊖ p` | PINNED from pp. 39–41 and the Jacobian of (iii) |
| Campaign `rho = 2/3` is the ODE ratio | FALSE; ODE ratio is `6 nu/(2 nu+1)` |
| `i = 7` is Prop. 8.1's `i` | FALSE; `i = 14` by St. 3.17(i) from the pole |
| `u = pi(F)` pinned numerically | NOT CLAIMED; only `1-u != 0` and the ratio `rho` |
| Uniform log/residue obstruction in `t` | ABSENT (DISPROVED as a kill) |
| Exceptional `t` | EMPTY |
| Explicit admissible formal solution, all `t >= 0` | PROVED |
| Uniqueness up to scale | PROVED (`sigma = 0`, `pi != 0`) |
| All printed root/eta/simple-root/`⊖`/searrow/(R)/`M` conditions | PROVED |
| T1 zero-chain law applied | NOT DONE (wrong shape) |
| R2.3(i) proportional kill | DOES NOT FIRE |
| Merge lambda exactly 0 under P2 | YES, accounting identity, not an AF2 floor |
| Incoming/trunk lambda exact | NOT CLAIMED |
| Source landing / St. 3.9 transport | NOT CLAIMED |
| Geometric realizability | NOT CLAIMED |
| Degree bound | NOT CLAIMED |
| JC2 | NOT CLAIMED |
| Infinitude of full cells (Sol D2) | USED as input typing, not re-proved |
| Completeness of all `td = 8` merges | NOT CLAIMED |

---

## 10. What this does to M2

The Sol D2 family is not killed at the first coefficient gate. A
numerical `kbar` cap is already impossible at the recorded-book tier; it
is also impossible as a Prop. 8.1(iv) filter on this cell. The reduced
successor remains the single state `(w, M) = (4/3, 3)`, now with an
explicit rigid pattern at every full cell.

The next exact obligation, not discharged, is transport: whether the
opposite-orbit rigidity at `G` can be matched to two incoming
`(21,15)` patterns. Keep lambda-exactness on the priced chain/trunk
steps, source landing, and realizability as separate gates. Nothing
here restores a prime-`td` exclusion, a cofinal bound on `td`, or a
Keller counterexample.

---

## 11. Reproduction

```sh
python3 -c "import hashlib,pathlib; p=pathlib.Path('xmodel/m2-td8-prop81iv-parametric-primary-grok46-20260829.md'); print(hashlib.sha256(p.read_bytes()).hexdigest())"
cd cases/m2_td8_prop81iv_parametric_grok46_20260829
python3 test_prop81iv_td8_affine.py
python3 -O test_prop81iv_td8_affine.py
python3 prop81iv_td8_affine.py
python3 -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('prop81iv_td8_affine.py').read_bytes()).hexdigest())"
```

Blindness: no ideation bodies; no Opus output after the prompt; no
`jc2-lean`; no workspace-wide search; no canonical edit.

**Verdict: `PROVED` (local Prop. 8.1(iv), all `t >= 0`); `PARTIAL` (lambda
exactness beyond the merge-0, landing, realizability, JC2).**

---

*Report body ends. Self-hash below covers everything above this line.*

report_body_sha256 = cc7035dec2949f674064f7495c209abbf1037dee3179f1abd876a8e292366416
(sha256 of this file up to and including the line "*Report body ends. Self-hash below covers everything above this line.*", i.e. of the first 17822 bytes)

Full-report SHA-256 is the hash of the complete file bytes, including this appendix. Compute with:

```
python3 -c "import hashlib,pathlib; print(hashlib.sha256(pathlib.Path('xmodel/m2-td8-prop81iv-parametric-primary-grok46-20260829.md').read_bytes()).hexdigest())"
```
