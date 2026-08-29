# Opus 5 different-model hostile review — TD12-FORMAL-CASCADE-RANK/v1

Date: 2026-08-29
Reviewer: Opus 5 (different-model hostile mathematical review; producer was Sol 5.6)
Frozen Git basis: `ccb6cd52eeab95f169b40f0a48668c3acd7a607e`

Review only. No source, canonical, code, or other file was modified; no commit,
no push. No web, AWS, heavy CAS, or `jc2-lean` access. No
`ideation-20260829T1224Z-*` lane prompt, log, or report was read.

## 0. Disposition

```text
C1  custody / seals / control reproduction ............... PASS
C2  eta->t root-floor factorization (3.1)-(3.2), floor ... PASS
C3  injectivity on C[t] (Theorem 4.1) ................... PASS
C4  nominal + intrinsic cokernel q (Theorem 4.2) ........ PASS
C5  sharp endpoint-resonance formula (4.5) + tables ..... PASS_WITH_REPAIR
C6  formal binomial response through s<=i (Section 5) ... PASS_WITH_REPAIR
C7  scoping of "no B24/S16 formal kill" ................. PASS_WITH_REPAIR
C8  rank theorem vs structured-image lemma vs PairRef ... PASS
C9  R1 erratum (integral index rider) ................... PASS_WITH_REPAIR
C10 cases/.../check.py controls ......................... PASS_WITH_REPAIR
```

No component fails. Every repair is a scope/《statement》 repair; no theorem in
the packet is false. Two of the repairs make the packet **stronger** than it
claims, one corrects a factual sentence about the checker, and one asks a bare
disposition token to carry the rider that already appears in the body.

Maximum safe promotion is in §9.

`NOT_AN_EXIT_CLAIM` — this packet makes no exit, per-ray, or first-separation
charge, so no `charge_basis=` line is emitted. Emitting one here would declare a
basis that does not exist.

## 1. Custody

All five pinned hashes recomputed with `shasum -a 256` and matched exactly:

```text
30aa29260c2bc3b206f757a90fe42ec6dcd98c733a7bf073bd0a86c9f48cdf67  xmodel/td12-formal-cascade-rank-v1-provisional-sol56-76c-20260829.md
b50d8fdf41033bdd5d786db7948fba5b1cb304e09739208a429948fdbc2ad13a  xmodel/td12-formal-cascade-rank-v1-provisional-r1-erratum-sol56-76c-20260829.md
ea911af2906b71802507bd02a5aab728645e823e2148d04b8a35e44fb5fca261  cases/td12_formal_cascade_rank_v1_20260829/check.py
1a60264334ae99f60ff79f1ed8b4a75cb42abf30f5e4ae8001a51b9064056d84  xmodel/td12-bchild-v1-primary-fable5-76c-20260829.md
876d1717efdc69865cfae6c8b5d4ef983440a5f0997a9edf3cf13a2a5cc70aab  xmodel/td12-bchild-v1-primary-fable5-hostile-disposition-r1-sol56-76c-20260829.md
```

Both body seals recomputed and matched:

```text
provisional : body 13264 / 805e551279f47ff7cecc235f906a940b80ad384e1db05178f6792240448ee853
erratum     : body 1431  / f0e82363af25b5ada505fbd87e73d48e4d06f9e9e729d9fdc5bb5185f3ebb4a9
```

The packet's own declared `README.md` hash `cd3288b6...` also matches.

Ordinary and `-O` control runs, this desk:

```text
ordinary : 648 bytes, 35f6f1719154755b82c58d13db8fdc9045152f8f780053cca59102d6b9e6f008, 2.71s
-O       : 648 bytes, 35f6f1719154755b82c58d13db8fdc9045152f8f780053cca59102d6b9e6f008, 2.74s
cmp      : BYTE_IDENTICAL
```

Exactly as declared, including the `2.7 s` figure and the twelve matrix cases
(`6 + 6`, recounted from the sample-order/cap logic). `require` is a real
function, so `-O` genuinely re-executes every check — that is a correct design
choice and I confirmed it is load-bearing.

Both published table hashes reproduce from my **independently written**
implementation (shared no code with `check.py`):

```text
B  1d52051fec7bfbdcb76f6a2326640567a6dedc7bfe6a3ea929cab2beb757d69c   reproduced
S  f1074d459ee4bc4414e15ed491aba7db1ad4cab1b926216814faa5134a3b0c03   reproduced
```

## 2. C2 — the eta-to-t factorization and all floors: PASS

The packet's own checker verifies (3.1)–(3.2) only in **pre-divided `t`-level
form**: `raw_operator_factor_check` compares `P·[e F_s R + nu t (F_s R)'] -
(nu i - s) t P' F_s R` against `F_s C · T_s(R)`. The chain-rule step that turns
`d/deta` into `d/dt` — the step where an error would actually live — is done by
hand in the report and is **not** covered by the control.

I closed that gap. Building genuine `eta`-polynomials, substituting
`Z = eta^{e_s} F_s(eta^nu) R(eta^nu)` and forming
`L_s(Z) = D_F P Z' - i(D_F - s) P' Z` with `' = d/deta` throughout, then
comparing against `nu·i·eta^{e_s-1} F_s C · T_s(R)`:

```text
B  nu=25 i=2 s=1 (deg_eta L = 196)   exact
B  nu=25 i=2 s=2 (deg_eta L = 168)   exact
S  nu=17 i=2 s=1 (deg_eta L = 182)   exact
S  nu=17 i=2 s=2 (deg_eta L = 144)   exact
b5 nu=5  i=4 s=1..4                  exact
s7 nu=7  i=3 s=1..3                  exact
```

Hand derivation agrees: with `P' (eta) = nu t P'_t / eta` and
`(F_s R)'_t` expanded, `P = C S`, `P'_t = C J`, `U_s = S F_s'/F_s`, one gets
(3.2) on the nose. The root-exponent claim is also right: at a `t`-root of
multiplicity `m_j`, `P^{r-1} F_s C` contributes
`m_j(r-1) + (m_j i - s) + (m_j - 1) = m_j(r+i) - s - 1`.

FALLACY.md compliance is clean here and it is not accidental:

- **Prime label/derivative.** The report explicitly declares `d/deta` before the
  reduction and `d/dt` for `P, F_s, S` after. Both conventions are used and both
  are stated. This is the guardrail's exact hazard and it is discharged.
- **Floor/attainment.** `eta^{e_s-1} P^{r-1} F_s C` is labelled a *floor*, with
  the quotient polynomial kept separate; no equality is asserted. Correct — the
  quotient `T_s(R)` can itself vanish at the roots.
- **Variable/ring map.** `t = eta^nu`, coefficient field, and generator order are
  declared. The domain identification is sound *because* the roots are nonzero:
  `eta^{e_s}` is coprime to `eta^nu - a_j`, so
  `(eta^nu-a_j)^k | eta^{e_s}H(eta^nu) <=> (t-a_j)^k | H(t)`. The report declares
  `A,B` (resp. `A,B_±`) nonzero and distinct, matching the T1-reviewed source
  (`p(0) != 0`, `eps = 0`). Nonzero-ness is load-bearing and is declared.

Independent residue cross-check against the parent, which derives `e_k` a
different way (`N_1 = -kbar_F`, `e_k = N_1^{-1} k`):

```text
B: -M s == 22 s == (-17)^{-1} s (mod 25)  for all s in 1..24   agree
S: -M s == 13 s == (-13)^{-1} s (mod 17)  for all s in 1..16   agree
   [M * kbar_F == 1 (mod nu) in both routes]
```

So the report's `e_s == -M s` form and the parent's `N_1^{-1} s` form are the
same object. `gcd(M,nu)=1` holds in both routes, so `e_s != 0` on the window.

## 3. C3 — injectivity on `C[t]`: PASS

Verified by exact rank at **every** `s in [1, nu-1]` in both routes, at
`i = nu-1`, `24` and `30`, and at caps running past the resonance
(`N = n_* + 3`): rank is always `N+1`, zero kernel. Also verified on two extra
rational root sets (`B' = {-3, 5/7}`, `S' = {2/3, -1, 11/5}`) to rule out an
accident of the checker's `{1,2}` / `{1,2,3}` choices.

The report's proof is correct. A shorter and more robust replacement, which I
recommend adopting because it never leaves the polynomial ring: let `rho` be an
`eta`-root of a **simple nonzero** `t`-root of `P`, and `v = ord_rho(Z) >= 0`.
Matching leading terms in `D_F P Z' = i(D_F-s) P' Z` gives `D_F v = i(D_F - s)`,
i.e. `v = i - s/nu`, not an integer for `nu` ∤ `s`; and `v = 0` would force
`i(D_F - s) = 0`, false since `D_F = nu i > s`. Hence `Z = 0`.

Load-bearing and declared: existence of a simple nonzero `t`-root (B: `t-B`;
S: `t-B_±`), and `1 <= s < nu`.

## 4. C4 — nominal and intrinsic cokernel `q`: PASS

`dim coker(T_s : C[t]_{<=N} -> C[t]_{<=N+q}) = q` verified by exact rank at every
`s` in both windows and at four route/root configurations. The nominal count is
in one sense a bookkeeping consequence of the declared target, and the report is
right not to oversell it; the substantive statement is (4.4).

(4.4) `dim C[t]/T_s(C[t]) = q` is a genuine theorem and it is **true**. The
report's one-line justification ("for `N>n_*`, adjoining the next source monomial
and the next highest target monomial adds one pivot") is looser than the fact it
asserts. The step actually needed is:

```text
for N >= n_*,  im(T_s) ∩ C[t]_{<=N+q} = T_s(C[t]_{<=N}).
```

Proof: if `deg R = n != n_*` then `deg T_s(R) = n+q`, forcing `n <= N`; if
`n = n_*` then `n <= N` already. The single edge case is `deg R = n_* = N+1`,
whose image has degree `n_*+q-1 = N+q` — and that is excluded exactly by
`N >= n_*`. The filtration then exhausts `C[t]` with stable codimension `q`.
I verified the stabilization numerically as well (codimension `q` flat across
`N = n_*-2 .. n_*+4` at `s = 1,5,9,16` in both routes).

This is a real correction to the Fable primary's "exactly one infinity cokernel"
(§8.3 there), and the correction is not cosmetic: `2` vs `3` is route-dependent,
so no shared count exists — precisely the objection the Sol disposition raised
(§5, QUARANTINE) and could not yet resolve.

Strong consistency check that the reconstruction is faithful to what it corrects:
the natural cap gives domain dimension `N_nat + 1 = q s`, i.e. `2s` for B and
`3s` for the sibling — exactly Fable's "fresh f-side unknowns … dimension `2s`
(trunk; `3s` sibling)". The packet is correcting the right object.

`N_nat(s) = q s - 1` re-derived independently: `e_s + nu(M i - q s + N) <= M nu i`
with `0 < e_s < nu`.

## 5. C5 — sharp endpoint-resonance formula and tables: PASS_WITH_REPAIR

The packet's checker rank-verifies only **four** orders per route
(`s in {1, boundary, boundary+1, nu-1}`) and then emits the full 24- and 16-entry
tables from the closed formula. I verified the tables by **actual exact rank at
every order**:

```text
B  nu=25 M=3 q=2 (i = 24 and 30):
   nominal cokernel = 2 at all s = 1..24
   sharp   cokernel = 1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2
   endpoint resonance orders = 1..8
S  nu=17 M=4 q=3 (i = 16 and 30):
   nominal cokernel = 3 at all s = 1..16
   sharp   cokernel = 2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3
   endpoint resonance orders = 1..4
```

Identical on the two extra root sets. `h_s = (Ms+e_s)/nu = ceil(Ms/nu)`
confirmed for every `s`. `N_nat = n_*  <=>  h_s = 1  <=>  Ms < nu` confirmed
(`gcd(M,nu)=1` rules out `Ms = nu`). Both table digests reproduce.

Cross-check that the resonance is Fable's object relocated, not a new one: the
resonant `Z` has `deg_eta = M(nu i - s)`, so on the `G`-side
`M nu (r-i) + M(nu i - s) = 75r - 3s` (B) and `68r - 4s` (S) — exactly Fable's
`N_res`. The packet has moved the same resonance into the reduced quotient and
then found that it is *not* the whole cokernel. That is the correct diagnosis.

**REPAIR C5-1 (unstated rider).** Theorem 4.3's proof needs `n_* >= 1`, since
attainment of `d_s(N) = N+q-1` at `N = n_*` is witnessed by `T_s(t^{n_*-1})`. The
report never states this. It is true here — `n_*(1) = q-1 >= 1` and `n_*` is
strictly increasing whenever `q >= 2` and `0 < M <= nu` — but `q >= 2` and
`M < nu` are used and not declared as hypotheses of the general formula (4.5).
Measured minima: `n_* >= 1` (B), `n_* >= 2` (S). Add the rider; no number changes.

The report's own framing of the drop as "a cap-endpoint artifact" is accurate and
is the honest reading. I endorse it.

## 6. C6 — the formal binomial response: PASS_WITH_REPAIR (sound, and stronger than claimed)

### 6.1 The mechanism is correct

The load-bearing sentence is "since `g_hat` is a truncated formal function of
`f_hat`, its chart Jacobian with `f_hat` vanishes coefficientwise", together with
"`D_g=(3/2)D_F`, so the top powers align". Both check out, and the second is
exactly the non-obvious step:

```text
f = x^{D_F/kbar_F} f_hat(z),  g = x^{D_g/kbar_F} g_hat(z),  z = x^{-1/kbar_F}.
g = c_g f^{3/2} as a function of (x,eta)  <=>  D_g = (3/2) D_F,
and then J_{x,eta}(f,g) = f_x·(3/2)c_g f^{1/2} f_eta - f_eta·(3/2)c_g f^{1/2} f_x = 0.
```

Since `f_hat = P^i(1+w)`, `g_hat = c_g P^r (1+w)^{3/2}` is `c_g f_hat^{3/2}`
precisely because `r = 3i/2`. Truncation at `z^{d+1}` is harmless: the `z^s`
coefficient of `J` involves only indices `<= s`.

I re-derived the whole lift a second, independent way — from
`g_hat^2 = c_g^2 f_hat^3`, which is what type `(2,3)` *means* and which needs no
binomial series at all — and recovered the packet's (5.3) exactly:

```text
G_1 == (3/2) c_g p^{r-i} P_1                       reproduced
G_2 == c_g p^{r-i}((3/2)P_2 + (3/8) P_1^2/p^i)     reproduced   [packet (5.3)]
F_1^2 / p^i == F_2                                 reproduced   [packet floor identity]
```

### 6.2 Verified far beyond the packet's single control

The checker tests the lemma at `s = 2` only. I tested the **full** `E_s` — all
`a+b=s` terms, `E_s = sum_{a+b=s}[(D_F-a)P_a G_b' - (D_g-b)P_a' G_b]` — with
nonzero arbitrary jets `P_s` in the declared class, on the real routes:

```text
B nu=25 i=24 r=36 : E_s = 0 exactly for s = 1..26     (depth 24 covered)
B nu=25 i=30 r=45 : E_s = 0 exactly for s = 1..26     (depth 24 covered)
S nu=17 i=16 r=24 : E_s = 0 exactly for s = 1..18     (depth 16 covered)
S nu=17 i=18 r=27 : E_s = 0 exactly for s = 1..18     (depth 16 covered)
plus 5 auxiliary routes (nu = 5,7,11) at i = 3,4 through s = 1..7
```

and confirmed in every case that the lift's `G_s` satisfies the g-side vanishing
ladder `ord >= m_j r - s`, the weight class `e_s`, and the natural top-degree cap
`M nu r` — i.e. the report's "weight residues add to `e_s`, and the top-degree
caps are preserved" is correct as stated.

Negative controls all fire: perturbing `G_2` by `+1`, rescaling `G_1` by
`1.001`, or replacing the binomial coefficient `3/8` by `1/3` each break `E_s`;
`E_0` with `G_0 = c_g p^r` holds.

### 6.3 REPAIR C6-1 — the reach is `s <= r = 3i/2`, not `s <= i`

The report restricts to `d <= i` and says that "at `s=i+1` the simple-root
divisibility proof (5.2) no longer follows from these floors". That sentence is
imprecise, and the restriction is not sharp.

`(5.2)` computes the **g-side** exponent `m r - s`, which is `>= 0` iff
`s <= m r`, i.e. `s <= r` at a simple root. What fails at `s = i+1` is the
*separate* `Z_s` exponent `m i - s >= 0`. But `E_s` only requires `G_s` to be a
polynomial; `Z_s = G_s/(c_g p^{r-i}) - (r/i)P_s` is the packet's bookkeeping for
routing `K_s` through the reduced operator, and is not needed to solve `E_s`.

General bound (mine): splitting the grade-`s` monomials by whether `s_j <= m i`,

```text
exponent >= m r - m i k' - sum_{T} s_j >= m r - s,   for every k, every composition,
```

so the lift is polynomial for all `s <= r`. Measured, and **sharp** — the first
failure lands at exactly `s = r+1` every time:

```text
B nu=25 i=16 r=24 : E_s = 0 for s = 1..24, G_25 not polynomial   (depth 24 covered)
B nu=25 i=14 r=21 : E_s = 0 for s = 1..21, G_22 not polynomial   (depth 24 NOT covered)
S nu=17 i=12 r=18 : E_s = 0 for s = 1..18                        (depth 16 covered)
S nu=17 i=10 r=15 : E_s = 0 for s = 1..15, G_16 not polynomial   (depth 16 NOT covered)
n11 i=4 r=6       : E_s = 0 for s = 1..6,  G_7  not polynomial
```

Consequences, all in the packet's favour:

1. The rider `i >= depth` may be replaced by the sharp `r = 3i/2 >= depth`:
   **B: `i >= 16`** (not 24); **S: `i >= 12`** (not 16; `i >= 32/3` with `i`
   even). Confirmed at `B, i=16` and `S, i=12` above.
2. To state the lemma for `s > i` one must use the clamped floor
   `prod_j (t-a_j)^{max(0, m_j i - s)}`. The report's `F_s` is ill-formed for
   `s > i` (negative exponent at simple roots). The clamped form is the faithful
   reading of the source (V) ladder anyway, since `P_s` is a polynomial.
3. Failure of *this* lift at `s = r+1` is **not** an obstruction. It shows the
   construction stops, nothing more. The report correctly claims nothing there,
   and the repaired statement must preserve that restraint.

### 6.4 What the lemma really says — and why it kills the lane

Worth stating plainly, because the report under-emphasizes it. The lift is the
`J ≡ 0` solution. It satisfies *every* homogeneous row, so the entire Keller
content of the problem sits in the single inhomogeneous row at
`s* = D_F + D_g - kbar_F` (B: `25(i+r)-17`; S: `17(i+r)-13`), which is far above
both windows. Therefore Fable's proposed "typed future kill lane" (§8.3 there,
"first bite at `s=2`") is not merely unproved — it is **structurally dead as a
window strategy** whenever `3i/2 >= depth`, because a solution to all window rows
always exists. That is the packet's real contribution and it is correct.

One scope point the report does not claim but is entitled to: window
*contamination* (Fable §3.4 gap 2) is harmless to this lemma, because the lemma
quantifies over **all** members of the (V)/(W) class and contamination perturbs
values, not the class. Conversely, one caveat it does not state: cap preservation
is cap-specific — if the true `P_s` cap exceeds the natural one by `delta_s`, the
g-side cap degrades additively by `sum_j delta_{s_j}`.

## 7. C7, C8 — scoping, and rank theorem vs structured image vs `PairRef`

**C7: PASS_WITH_REPAIR.** The rider is present in the body: §0 "under the
explicit rider `i>=depth`", §5 "under `i>=24`, neither the B depth-24 nor sibling
depth-16 window…". So the claim *is* scoped. The defect is presentational and
matters for downstream consumption: the §0 disposition token

```text
NO_FORMAL_CASCADE_KILL_IN_WINDOW
```

is printed bare, three lines above the rider, and is exactly the string a
descendant lane will lift. **REPAIR C7-1:** make the token carry its rider, e.g.
`NO_FORMAL_CASCADE_KILL_IN_WINDOW_GIVEN_3i/2>=depth_AND_ROUTE_OCCURRENCE`.

Riders I audited for being load-bearing but unspoken — none found:

```text
type-(2,3) pin D_g/D_F = 3/2   declared, conditional on occurrence (§1, §8)
r in Z_{>0}                    erratum; and *derived* in the parent §3.1
nonzero, distinct t-roots      declared (§2); load-bearing for domain + injectivity
i >= s                         declared (§2)
gcd(M,nu) = 1                  declared (§2)
natural cap not source-pinned  declared (§2), and labelled Fable's heuristic
direct entry / i = 6n          not used; explicitly disclaimed in the erratum
completion / PairRef           not used; §7 not-licensed, §8 firewall
q >= 2, M < nu, n_* >= 1       NOT declared -> REPAIR C5-1
clamped floor for s > i        NOT declared -> REPAIR C6-1
```

**C8: PASS.** The three objects are kept properly distinct, which is the specific
failure mode this lane was commissioned to avoid (parent §6.3: "It must not call
its formal jet envelope a `PairRef`"). Theorems 4.1–4.3 are linear rank
statements about `T_s` on an explicitly declared domain and target; §5 is a
nonlinear existence lemma about the structured image; §7 not-licensed item 3
forbids treating the lift as a polynomial `g` or a `PairRef`; §8 firewalls the
rest. `NOT_A_PAIRREF` is in the disposition. No `PairRef` claim appears anywhere,
and none could: the lift has `J ≡ 0` and so is *never* a Keller pair — it fails
at `s*` by construction. The report says this.

Also correct and worth recording: §7 not-licensed item 1 forbids identifying
`Y_{s,N}` with the unknown source `K_s` target. That is the right firewall — the
cokernel `q` is a statement about `T_s`, and the report explicitly declines to
convert it into a condition on `K_s` (§5, first paragraph). Under FALLACY.md's
carrier/attainment rule this is the correct restraint.

## 8. C9, C10 — erratum and controls

**C9: PASS_WITH_REPAIR.** The substance is right, and in fact stronger than
presented: `r in N*` is not an added hypothesis, it is **derived** in the parent
(§3.1 — unique factorization of `P_0 = p^i` forces multiplicity `r` at a simple
root of `G_0`). Given the type pin `D_g/D_F = 3/2`, `i` even is therefore a
*consequence*, not a supplement. The erratum's claim that the `P^{r-1}` floor,
its nominal target and the `P^r` binomial response need integral `r`, while the
factorization/injectivity/rank layer does not, is exactly right.

**REPAIR C9-1 (factual).** The sentence "The exact checker uses `i=30`, `r=45`,
so its controls already satisfy the repaired hypotheses" is false for the
order-two binomial control, which runs at `i=6, r=9`
(`def tiny_order_two_control(route, i=6)`, called from `run_route` with no `i`;
`i = 30` is the *matrix-case* index). The erratum's conclusion survives, because
`(6,9)` also satisfies `i,r in Z_{>0}`, `r = 3i/2`, `i` even. Fix the sentence to
name both indices. The provisional report's §6 has the same slip
("The checker uses … `i=30`" reads as global).

Related coverage note: **no control in the packet exercises the binomial lemma at
`i >= depth`** — the only binomial control is at `i = 6`, well below both 16 and
24. I closed that gap in §6.2 above (`B` at `i=24,30`; `S` at `i=16,18`).

**C10: PASS_WITH_REPAIR.** I mutation-tested a `/tmp` copy (original untouched).
13 of 14 mutations killed by internal `require`s:

```text
KILLED   q -> q+1 in nominal cokernel assert        KILLED   K_2: (D_F-1) -> D_F
KILLED   resonance n* = qs-h -> qs-h+1              KILLED   K_2: (D_g-1) -> D_g
KILLED   residue e = -Ms -> +Ms                     KILLED   prefactor P^(r-1) -> P^r
KILLED   floor m*i-s -> m*i-s+1                     KILLED   T_s drops the e_s*S term
KILLED   order-2 coefficient 3/8 -> 1/3             KILLED   B route nu 25 -> 24
KILLED   order-2 g1 coefficient 3/2 -> 1            KILLED   r = 3i/2 -> 2i
KILLED   L_s: i(D_F-s) -> i*D_F
SURVIVED S mults (2,1,1) -> (1,1,1)
```

That `r = 3i/2 -> 2i` is killed confirms the type-`(2,3)` ratio is genuinely
tested, not decorative. The survivor is not a false pass: the checker derives
`M` and `q` from `mults`, so the mutant is internally consistent — it simply
checks a *different, valid* route. It is caught by the published stdout hash:

```text
mutant stdout sha256  44b44c7ed8b887f539263f3452b427a3d12eb28d41f801e0d74e0d12d0596770
sealed stdout sha256  35f6f1719154755b82c58d13db8fdc9045152f8f780053cca59102d6b9e6f008
```

**REPAIR C10-1:** add an explicit pin (`require(route["M"] == 3 and route["q"] == 2)`
for B, `4`/`3` for S) so the declared `(nu, M, q)` are asserted rather than
inferred; or state in the README that the stdout hash, not the assertions, is the
binding pin on route identity.

Three further coverage gaps, all closed by me above rather than by the packet:
(a) only 4 of 24/16 orders are rank-verified (I verified all);
(b) the binomial lemma is controlled at `s=2` only (I verified to `s=26`/`s=18`);
(c) the factorization control is `t`-level only (I verified the `eta`-level chain
rule). None of these is an error; they are limits on what the controls evidence,
and the report is honest that "these controls sample the theorem; they do not
establish it by enumeration."

## 9. Maximum safe promotion

Promotable now, route-separated, as a formal rank result on a **declared** domain
and target — not as source data:

```text
1. the exact root-floor quotient operator (3.1)-(3.2) and the output floor
   eta^{e_s-1} P^{r-1} F_s C, with root exponent m_j(r+i)-s-1;
2. injectivity of T_s on C[t] for 1 <= s < nu (Theorem 4.1);
3. nominal cokernel q on C[t]_{<=N} -> C[t]_{<=N+q}, and the intrinsic
   dim C[t]/T_s(C[t]) = q  (Theorem 4.2; q = 2 for B, 3 for the sibling);
4. the cap-endpoint resonance formula (4.5) and the two complete natural-cap
   tables, WITH the added rider n_* >= 1 (holds: q >= 2, 0 < M < nu);
5. the type-(2,3) formal lift lemma in its REPAIRED sharp form:
      for arbitrary f-side jets in the (V)/(W) class with clamped floors,
      g_hat = c_g f_hat^{3/2} gives a polynomial g-side response satisfying
      the g-side ladder, weight class and natural cap, and solves every
      homogeneous row E_s for all s <= r = 3i/2;
6. the consequent negative result:
      NO_FORMAL_CASCADE_KILL_IN_WINDOW, conditional on 3i/2 >= depth
      (B: i >= 16; S: i >= 12) and on route occurrence.
```

Retire, as refuted by this packet and confirmed by me:

```text
Fable primary §8.3 "exactly one infinity cokernel per order"   -> it is q (2 / 3)
Fable primary §8.3 "cascade conditions are real, first bite at s=2"
                                                               -> not a formal bite
```

Both were already quarantined by the Sol disposition (§5); this packet closes
them, and the commissioning brief (parent §6.3) is discharged.

Not licensed — I concur with the packet's own §7 list and add two:

```text
- identifying Y_{s,N} with the unknown source K_s target;
- a one-dimensional cascade, an order-two kill, or any depth-gate verdict;
- treating the formal lift as a polynomial g, an exact pair, or a PairRef;
- a standalone source recurrence engine, or any AWS/CAS launch;
+ asserting that a formal obstruction BEGINS at s = r+1 (the lift merely stops);
+ using the cap-preservation clause under any cap larger than the natural one
  without re-deriving the additive degradation.
```

The next lane remains route-separated `PairRef`/completion construction
(`TD12-B25-PAIRPACK/v1`, `TD12-S17-SIBLING-PARENT-PAIRPACK/v1`), unchanged. A
purely formal successor should target the single inhomogeneous row at `s*`, not
the window — §6.4 is the reason the window has nothing left in it.

## 10. Scope firewall

This review supplies no exact pair, source realization, completion, germ,
landing, gate verdict, exclusion, degree bound, counterexample, occurrence proof,
software migration, or JC2 consequence. It does not link the B and sibling source
states. It makes no exit or charge claim. No source, canonical, code, or other
file was modified; all my computations ran in `/tmp`. No commit, no push.

## Seal

- Body length: `25485` bytes (all bytes before this heading).
- Body SHA-256: `66b15f5d535d68a84c1324cdea826a067ceeb25345a637a8c53e79db07b7afc9`.
- Frozen Git basis: `ccb6cd52eeab95f169b40f0a48668c3acd7a607e`.
