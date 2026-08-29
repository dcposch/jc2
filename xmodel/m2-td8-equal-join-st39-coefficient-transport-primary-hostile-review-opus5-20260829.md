# Opus 5 hostile review — Fable td=8 Statement-3.9 coefficient transport

Lane: Opus 5, different-model adversarial referee. Date: 2026-08-29 UTC.

Target: `xmodel/m2-td8-equal-join-st39-coefficient-transport-primary-fable5-20260829.md`.
Packet: `cases/m2_td8_equal_join_st39_transport_fable5_20260829/`.

**Verdict: `PASS_WITH_REPAIR`** at the Statement-3.9 formal-transport scope.

---

## 0. Custody — every declared hash recomputed this session

```
910d3216ad7476b743eb920e3d68026f05efc8ffe1a409c476fb90ce277f6ad4  target (full)      MATCH
3b7851eaaee3f35c23de8d201eb22ad664ab2dba1614d6d4fc04cba562461171  target (body)      MATCH
d2e1003465d0938d1056f6a47ca213d41c249fc458124cc0509f982e5f6270b3  st39_transport_check.py        MATCH
832b9ed6fb6926bf143fcccede01da3ec1ed74baf831521252c04c60acfb9844  test_st39_transport_check.py   MATCH
f4259b15ca02ab1b31b5451398f74d7f72f56746d7906ea6d48d684f1accecaf  README.md                      MATCH
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf           MATCH
9a778862816aa96d251c33aac7e98a2fb3bfc1b3fc7c83f4463ac862de31815a  route-family-sol56             MATCH
aeb7714e656b7c112ce2933b48b6da6c18fdec3136b2d2651c44e6d9874c5584  prop81iv-route-sol56           MATCH
c2a112fa84e0c11085f285ddab79999caf6b00d8a8fe37a84390a13ee7cfc675  prop81iv-route-review-fable5   MATCH
```

Body hash reproduced by `head -n 368 <target> | shasum -a 256` (separator at
line 368 of 369).

Printed source re-extracted by me, not taken from the target: pp. 11–13
(Def. 3.4 vertices, Not. 3.3–3.5), 14–18 (Prop. 3.1, St 3.8–3.18, Prop. 3.2),
19–23 (Prop. 4.1–4.6), 24–27 (Prop. 5.1–5.5, St 5.1–5.2), 29–33 (Not. 6.1,
St 6.1–6.2, Prop. 6.2–6.7, Cor. 6.1), 39–44 (Not. 8.1, St 8.1–8.5,
Prop. 8.1–8.4). Layout and `-bbox` extraction both used, the latter to
adjudicate dropped `⊖` glyphs. Not read: any exact-lambda/cv-census output,
any later model report, `jc2-lean`. No web, AWS, commit, push, canonical
edit, heavy CAS, long/high-memory process, global `git status`, or
workspace-wide search. Only this file was written; scratch in `/tmp/st39rev`.

Replay of the target packet (from the packet directory, ≈0.1 s each):

```
python3 st39_transport_check.py        →  ST39_TRANSPORT_CHECK_PASS checks=24987   (0.09s)
python3 -O st39_transport_check.py     →  ST39_TRANSPORT_CHECK_PASS checks=24987   (0.08s)
python3 test_st39_transport_check.py   →  ST39_TRANSPORT_TEST_PASS checks=24987 mutations=2  (0.19s)
```

All three reproduce the declared banners and census exactly.

Independent reconstruction (my own code, no producer code reused), 468
exact checks, `/tmp/st39rev`:

```
e0b6a22677df355fa5f30c99b1376cf24989ee986aef6bec11072ace0d779457  indep.py   108 checks
99ae29427dbc8bd8a991d66f6abdcc47993aa60a086a3e4071f1a60895c4bac8  indep2.py   72 checks
71622bf7e3437a6225349ba651424f6c2438011ff13a68ef18edf046bb307567  indep3.py  117 checks
51e631d06a24907a19d35f0b0b84a0314a240f23db4a1f2eb417c9e69725950c  indep4.py  171 checks
```

---

## 1. Verdict and scorecard

**`PASS_WITH_REPAIR`.** The mathematical core survives a hostile
re-derivation from the printed statements: the exact product law, the
drop-stage law, the twin law and the existence of a compatible formal
coefficient system are all correct, and I closed two printed gates the
target never checked, both of which pass. Two statements in the report text
are, however, **false as written** (§3's `β`, §7's exponent sentence), and
four more are imprecise or mis-cited. None flips the verdict; all must be
repaired before any consumer cites §3 or §7.

| clause | verdict |
|---|---|
| exact product law (E), `⊖` pinned on both branches | **CONFIRMED, and sharper than claimed** — the chart normalizer is exactly `1`, not an unpinned rational |
| drop-stage law `l_m/k_m = Q_W/D_W`, stage table | **CONFIRMED** — but weaker than the printed source, one mis-citation, and §9's ambiguity menu is wrong |
| twin law `(A₁/A₂)² = ω^{−15}` | **CONFIRMED as an identity; NARROWED** — it is a derived consequence, not a closure condition, and cannot obstruct |
| compatible formal coefficient system exists | **CONFIRMED** — reproduced by an exact free-abelian-group solve, stronger than the packet's float-phase P6 |
| §3 interior binomial lemma | **conclusion CONFIRMED, mechanism REFUTED** — `β = 0` is forced, not free |

Verdict word for the charged question is unchanged: **`ST39_TRANSPORT_SURVIVES`**
for every integer `t ≥ 0`, uniformly, with no exceptional residue.

---

## 2. What I re-derived, independently

### 2.1 The exact upgrade (E) — confirmed, and pinned harder than the target dares

Prop. 4.2(ii) gives `h_{j+1} = h_j^{k_j} − s_j f^{l_j}`, hence
`J(f,h_{j+1}) = k_j h_j^{k_j−1} J(f,h_j)` and

```
J(f, h_m) = (∏_{j<m} k_j) · J(f,g) · ∏_{j<m} h_j^{k_j−1}          (exact, in C[x,y])
```

The **printed proof of Prop. 4.2 is wrong here**: it writes
`J(f,h_j) = J(f,h_j) h_{j−1}^{k_{j−1}−1} = … = h_0^{k_0−1}…h_{j−1}^{k_{j−1}−1}`,
dropping every `k_j` and silently using `J(f,g) = 1`. The target's `∏k_j`
and its symbol `c₀ := J(f,g)` are exactly the repair; the target does not
say that it is repairing a printed slip, and it should.

Passing to initial parts is legitimate **at `m = m_F`** and only there:
by the definition of `m`, `J(f_F^+, h_{m,F}^+) ≠ 0` (Prop. 4.2(10)), so the
top term cannot cancel and `init_F` commutes with the Jacobian. Below `m`
the printed dichotomy gives `0`, and the identity would be vacuous — the
target does not state this restriction but never violates it.

The chart factor: **Prop. 4.1's proof prints
`J(f^F(ξ,η),(g−b)^F(ξ,η)) = ξ^{−n/κ}` with no `⊖`.** I settled this by
`-bbox`: the `ξ` on that line sits at `xMin = 112.183`, flush with the proof
left margin (compare the paragraph indent at `120.443`), whereas every
genuine dropped-`⊖` site (e.g. Prop. 8.1(i) `(ξ^δp)^i = ⊖ f_F^+`) shows a
multi-point gap. So the chart Jacobian constant is **exactly 1**, and the
target's hedge "the `κ_F`-normalizers are explicit nonzero rationals" is
unnecessary. The only residual rational in the vertex equation is the
ODE-ray scale `λ_V := δ_V / X_V ∈ Q_{>0}` (the reviewed local lane pins
`(δ_V, 1−u_V)` only up to the positive ray `(X_V, k̄_V)`), and `λ_V` is
literally equal on the two twins.

Reduction of (E) to the vertex equation. With `P = C Φ^i`,
`Q = B Φ^k Ψ`, `d = iδ`, `d_h = (1−u)+kδ`, `k = i(μ−1)`:

```
d·P·Q′ − d_h·P′·Q = i·C·B·Φ^{i+k−1}·[ δ Φ Ψ′ − (1−u) Φ′ Ψ ]
```

— the `kδ Φ′Ψ` terms cancel identically. I verified this polynomial
identity on 60 random exact instances (`indep.py`). Substituting
Prop. 8.1(iv) `δΦΨ′ − (1−u)Φ′Ψ = R_V Φ` and `i+k−1 = iμ−1`, and
`∏_{j<m} p_{h_j,V}^{k_j−1} = (∏ t_{j,V}^{k_j−1}) Φ^{iμ}`, gives **exactly**
the target's (★)

```
i_V · C_V · B_V · R_V = (∏_{j<m_V} k_j / λ_V) · c₀ · T_V ,   T_V = ∏_{j<m_V} t_{j,V}^{k_j−1}
```

**Answer to attack 2: yes.** The printed `⊖` of (11)/8.1(iv) can be
replaced by one globally pinned product, and by the *same* product on both
branches.

### 2.2 The vertex-local constants, re-derived by hand

All four re-derived from the reviewed families without using the packet:

* `Φ_H = (η⁷−A)²(η⁷−B)`, `B = (3/2)A`: `7ΦΨ′−5Φ′Ψ = (21/2)A²·Φ` ✓
  (the route certificate's `p=(T−2)²(T−3)` gives `42 = (21/2)·2²` ✓).
* `Φ_G = (η^ν−a)³(η^ν+a)³`: `(16+12t)ΦΨ′−(6+4t)Φ′Ψ = −(16+12t)a²·Φ` ✓
  (certificate's `T²+1` is `a² = −1`, giving `+δ` ✓).
* `Φ_tr = (η^17−A)³(η^17−B)²`, `B=(4/3)A`: `17ΦΨ′−7Φ′Ψ = (68/3)A²·Φ` ✓
  (certificate's `p=(T−3)³(T−4)²` gives `204 = (68/3)·3²` ✓).
* Merge orbits: `Φ_G ≈ (νc_1^{ν−1})³(2a)³(η−c₁)³` at `c₁^ν = a`, so
  **`L_e = 8ν³a⁶/c_e³` at both orbits**, and at `c₂` the two sign flips
  cancel ✓. `Ψ_G = η^{2ν+1} − a²η ⇒ Ψ_G′(c_e) = (2ν+1)a² − a² = 2νa²` at
  both ✓. `Φ_H ≈ (7c⁶)²(−A/2)(η−c)²` ⇒ **`K_e = −(49/2)c^{19}`** ✓.
  `Φ_tr ≈ (17c^{16})³(−A/3)²(η−c)³` ⇒ `L_tr = (17³/9)c^{48}A_F²` ✓.

### 2.3 The chain dictionary, re-derived

`St 3.17(i)` chain: `2·i_H = 4 = D_P`, `3·i_G = 42 = D_H`,
`3·i_tr = 336+252t = D_G`. From the printed gcd list of Not. 8.1 I get,
**for every `t` and every value of the un-pinned shift exponent `l₁`**,

```
M*_H  = gcd(42,63,42l₁) = 21          ⇒ i_H  = 2
M*_G  = gcd(D_G, (3/2)D_G, (6/7)D_G, l₁D_G) = 24+18t   ⇒ i_G  = 14
M*_tr = gcd(D_tr,(3/2)D_tr,(6/7)D_tr,85l₃, l₁D_tr) = 85 ⇒ i_tr = 112+84t
```

The last needs `gcd(4+3t, 635+476t) = 1`, for which I have the identity
**`3·l₃ − 476·ν = 1` in `Z[t]`** (all `t`, one line — replaces a scan).
`M_F` census `(M_H,M_G,M_tr,M_P) = (3,3,5,2)`; St 8.4 `mult(p,c) | M_child`
holds at all three edges (`3|3`, `3|3`, `2|2`); St 8.2's searrow
inequalities `deg(q)·mult > deg(p)` hold strictly at all three
(`30>21`, `27+18t>24+18t`, `105>85`). The target's `i = 14` pin is
reproduced without the parametric lane.

### 2.4 Two printed gates the target never checked — both pass

**(G1) Statement 8.5 is a live kill and the target never invokes it.**
St 8.5 says: `F ∈ T_a^& ∩ V_a`, `G := F°`, **`G ∉ V_{2,a}` ⇒ `M_G | M_F`**.
On this route that would demand `M_tr | M_G` i.e. `5 | 3`, and
`M_H | M_P` i.e. `3 | 2` — **both false, so the route would be dead**. The
gate is escaped only because every route vertex is genuinely branching:
`Φ_H`, `Φ_G`, `Φ_tr` each have exactly two root orbits, so none is of the
printed single-orbit form `(η^ν − c^ν)^l`, so all three lie in `V_{2,a}`
(Def. 3.4) and St 8.5 is inapplicable. This is a load-bearing structural
fact that carries the whole route and it appears nowhere in the target.
(It is also the reason the merge has exactly two children: two orbits,
one continuation per orbit by St 3.18 — the "equal join".)

**(G2) Statement 3.9(i) for the first *non*-tower element at each vertex.**
At `V` the polynomial `h_{m_V+1} = h_{m_V}^{k} − s f^{l}` is still a
tower element upstream, so 3.9(i) constrains it. Naively
`p_{h_{m+1},V} = p_{h_m,V}^{k} − s\,p_{f,V}^{l}` has degree `k·Q_V`, but
3.9(i) demands `k·Q_V − dq_V + 1`. So `dq_V − 1` leading coefficients must
cancel — 14 of them at `H`. **I proved the cancellation is automatic.**
Put `U := Ψ^{k}/Φ^{N}`, `N = k·dq/dp`. Since `(k,N) ∝ (δ,1−u)`,
Prop. 8.1(iv) gives `U′/U = (k/X)·R/Ψ`, so `U′ = O(η^{−dq})`,
`U − 1 = O(η^{−(dq−1)})` and

```
deg(Ψ^k − Φ^N) = k·dq − dq + 1 ,   lc(Ψ^k − Φ^N) = − k·R / (X (dq−1))
```

Verified exactly on all three families. At `H` (`k=7`, `N=5`) this is
`Ψ⁷ − Φ⁵ = (T−A)⁷(T−B)⁵(A³ − (3/4)A²T)`, `T = η⁷`: degree **91**, leading
coefficient `−(3/4)A²`, hence

```
deg p_{h₃,H} = 7·21 + 91 = 238 = k_G·3 + 1 = mult(p_{h₃,G}, c_e)     ✓ 3.9(i)
```

Also required and also automatic: `B_H⁷ = s₂ C_H⁶` at `H` even though the
*polynomial* enslavement fails there (`m_H = 2`), because the transported
leading coefficients still satisfy it. The target asserts this telescoping
in §5 without ever testing the one place it could bite.

**(G3) The interior telescope and the vertex equation are the same
equation.** Continuing (G2): the transported `γ` on the incoming edge equals
that leading coefficient **iff** (★_V) holds. Explicitly, with
`W_edge := d_{f,V} − (1−u_V)D_V = i_Vλ dp(1−dq)`,

```
γ = (∏_{j<m_V}k_j)·k_{m_V}·c₀·T_V·B_V^{k−1} / (C_V·W_edge)
  = B_V^{k}·(−k R/(X(dq−1)))   ⟺   i_V C_V B_V R_V = (∏_{j<m_V}k_j) c₀ T_V
```

so (★) is **forced**, not merely consistent. Underneath this sits the
`(η−c)^ρ` coefficient of Prop. 8.1(iv),

```
Ψ_V′(c) · [ δ_V − (1−u_V)·ρ ] = R_V      (ρ := mult(Φ_V,c))
```

which I verified at **every** orbit of all three families
(`H`: `−(7/2)A²·(−3λ)` and `(21/4)A²·(2λ)` both `= (21/2)A²λ`; `G`:
`2νa²·(−2) = −(16+12t)a²`; `tr`: `−(17/3)A²·(−4)` and `(68/9)A²·3` both
`= (68/3)A²`). This is the bridge that makes the interior/vertex interlock
automatic, and it is absent from the target.

### 2.5 The formal coefficient system — rebuilt exactly

I rebuilt the six-vertex system from the printed statements and solved it in
the free `Q`-vector space of multiplicative exponents (exact; the packet's
P6 is float-phase with `tol = 1e−6`). Generators: `c₀, s₀, s₂, s₃, C_tr,
B_tr, ω`, plus **the six frame factors kept as free symbols** so that the
report's prefactor-invariance claim is tested rather than assumed.

Top-down: `(★_tr) → A_F²`; `L_tr = (17³/9)c^{48}A_F² → C_G, t_{0,G},
t_{2,G}, B_G`; `(★_G) → a²`; `L_e = 8ν³a⁶/c_e³ → C_{H_e}, t_{0,H}, B_H`;
`(★_{H_e}) → A_e²`; `K_e = −(49/2)c_P^{19} → C_P, B_P`; `(★_{P_e}) → r_e³`.

Result at `t ∈ {0,1,2,3,10,37}`: **all six (★) residuals are the trivial
monomial**, all enslavement telescopes `t_{j}^{k_j} = s_j C^{l_j}` hold at
`tr, G, H₁, H₂` and — notably — `B_P² = s₀C_P³` holds at the poles as
transported leading-coefficient arithmetic even though `m_P = 0` makes the
polynomial enslavement *false* there (`p_{f,P}` has four simple roots, so
`p_{f,P}^{3/2}` is not a polynomial). The target's phrasing "Pole feed:
`B_P = t₀`-transport, `B_P² = s₀C_P³`" is correct precisely because it is a
coefficient statement; a reader could easily mis-take it for enslavement.

Twin ratio: `(A₁²/A₂²)·(fr_{H₂}/fr_{H₁})` is **exactly `ω^{−15}`**, with no
other generator surviving, at every tested `t`. Two exponent mutations
(`t₀` transport exponent `21→20`, `t₂` exponent `12→13`) break it.

**Attack 5 answer: no hidden closed cycle, no shared-`s_j` or shared-`c₀`
over-determination.** The tree has no cycles; `c₀` and each `s_j` enter once
each as free initialization; every vertex contributes exactly one equation
and consumes exactly one fresh gauge; the system is triangular-monomial and
every pinned quantity is a product of nonzero factors.

### 2.6 Drop-stage law and stage table

`St 8.3` gives `ψ := deg(p_{h_m,F})/deg(p_F) = Q_F/D_F` and, since `h_m` is
enslaved at the predecessor, `ψ = l_m/k_m`. **The paper prints the
reciprocal `k_m/l_m` twice** in the proof of St 8.3 (and once more as
`deg(p_{h_j,F}) = (k_j/l_j)deg(p_F)`), contradicting its own Prop. 4.2(iii);
the target's orientation `l_m/k_m` is the correct one — the pole check
`Q_P/D_P = 6/4 = 3/2 = l₀/k₀` with type `(α,β) = (2,3)` settles it.

All stage arithmetic re-derived: `μ_H = 3/2`, `k_H = 1`, `(k₂,l₂) = (7,6)`;
`μ_G = 3/2 + 36/7 = 93/14`, `k_G = 79`, `Q_G = 1905+1428t`;
`(k₃,l₃) = (112+84t, 635+476t)`; and

```
k_tr = i_tr(μ_tr−1) = 79(8+6t) + (111+84t)(635+476t) = 39984t² + 106650t + 71117
```

reproduced coefficient-by-coefficient in `Z[t]`. Coprimality of `(k₃,l₃)`
for all `t`: I have the Bezout identity **`3·l₃ − 17·k₃ = 1`** in `Z[t]`,
which is a proof rather than the target's `t ≤ 2000` Euclid scan.
Integrality of every transport exponent confirmed
(`i_H·3/2 = 3`, `i_G·3/2 = 21`, `i_G·6/7 = 12`, `i_tr·l₃/k₃ = l₃`,
`i_tr·3/2 = 168+126t`, `i_tr·6/7 = 96+72t`).

### 2.7 Twin law

```
(A₁/A₂)² = (L₁/L₂)^{i_G(μ_H − 1 − l₂/k₂)} = (L₁/L₂)^{−i_G·dq_H/D_H}
         = (ω³)^{−5} = ω^{−15},        ω^{ν_G} = −1
```

Every step re-derived: the `C`, `B`, `T` ratios contribute exponents
`i_G`, `i_G l₂/k₂`, `i_G μ_H` respectively (the last because
`μ_F = Σ_{j<m}(k_j−1)l_j/k_j` is Prop. 4.2(iv) verbatim); `L₁/L₂ = ω³`
from `L_e = 8ν³a⁶/c_e³`; `ω^ν = −1` from the reviewed *opposite*-orbit
rigidity (`σ = A+B = 0`). Deck freedom (St 3.18) replaces `ω` by
`(ε₂/ε₁)ω`, still a `ν`-th root of `−1`; the exponent `−i_G dq_H/D_H` is
independent of every un-pinned tower choice, as claimed. `x² = ω^{−15}` is
solvable in `C*` for every admissible `ω`; a common polynomial source is
**not** thereby produced, and the target says so.

---

## 3. Defects — what must be repaired

**R1 (false, §3, load-bearing section).** "`β` free (resonant)" and "the
arriving top is absorbed by the next face's free `β`" are **wrong**.
`β = 0` is *forced*. Proof: at the first interior face `V*c`,
`deg p_{h_m,V*c} = mult(p_{h_m,V},c) = k_V·ρ + mult(Ψ_V,c) = k_Vρ + 1`
(the `+1` is Prop. 6.3 via the printed (14), quoted inside Prop. 8.1's own
proof), which equals `s₀ = A(μ−1)+1`; the target itself proves
`s* > s₀` on `T_a^&`, so a nonzero `β` would make the degree `s*` and
contradict 3.9(i). By induction `β = 0` at every interior face and
`Q_face = γ(η−c)^{s₀}` throughout. **Repair:** delete the resonant-`β`
mechanism and state instead that `β = 0` is forced, so the q-side pattern
on an edge is a *pure monomial* and the transported coefficient is `γ`.
The report's operative conclusion (a) is then not merely preserved but
*strengthened* — there is even less freedom than claimed. Also note that
`γ` is edge-invariant because `d_F − (1−u)A` is: `d ↦ d − A/κ`,
`u ↦ u + 1/κ` leaves it fixed (verified), and its value is St 6.2's
`W = d_{f,W} − (1−u_W)D_W < 0`. That part of §3 is right.

**R2 (false numeral, §7).** "By the drop-stage law the exponent is
`−i_G·dq_H/D_H = −15`". That quantity is `−14·(15/42) = **−5**`; `−15` is
the exponent of `ω`, since `L₁/L₂ = ω³`. The displayed equation is right;
the sentence is not. **Repair:** "the `(L₁/L₂)`-exponent is
`−i_G·dq_H/D_H = −5`, hence the `ω`-exponent is `−15`".

**R3 (imprecise, §2).** The `⊖` is pinned *harder* than the report says:
the chart normalizer is exactly `1` (Prop. 4.1 proof, `-bbox` verified), so
the constant in (E) is exactly `(∏_{j<m}k_j)·J(f,g)`, and the only residual
rational in (★) is the ODE-ray scale `λ_V = δ_V/X_V`. The report should
also state that (E) *repairs a printed error* (Prop. 4.2's proof drops every
`k_j` and assumes `J(f,g)=1`), and that initial-part extraction is licensed
only at `m = m_F`.

**R4 (under-specified, §2/§8).** "the pole family forced to `σ = (3/2)r`,
`π = (3/8)r²` … `(9/8)r³`" holds only in the packet's convention
`p = η⁴ − rη`, `q = η⁶ − ση³ + π`. Under the naive reading
`q = η⁶ + ση³ + π` with `p = η⁴ + rη` one gets `σ = (3/2)r`, `π = (3/8)r²`
but constant `−(9/8)r³`. The report states neither `p` nor the sign
convention. No verdict impact (`r³` is a pinned gauge either way). The
"`(1,2)` frame is dead" line is true but needs no computation: Prop. 5.3(vii)
plus `deg p/deg q = 4/6` forces coprime `(k_f,k_g) = (2,3)`.

**R5 (mis-citation, §2).** "Tower depth `m_F` is non-increasing child-ward
(St 8.3, **St 8.5** mechanism)" — St 8.5 is about `M_G | M_F`, not depth.
The correct chain is Prop. 4.4 + Prop. 6.3 + Cor. 6.1.

**R6 (§4 lemma is true but not new, and its hypothesis is vacuous).**
Cor. 6.1 gives strictly more than the target's drop-vertex lemma: **every**
`F ∈ T_a^& ∩ V_a \ {(0,y)}` satisfies (16), hence `F ≺ F′`, hence drops.
Moreover (16) ⟺ (15) ⟺ `dq > 1` (since `D+Q−1 = μD + dq − 1`), so
`dq_W > 1` holds at *every* such vertex and "`dq_W>1` ⇒ drop" separates
nothing. **Repair:** demote §4's headline to a corollary of Cor. 6.1 and
keep the genuinely useful part, the stage identity `l_{m_W}/k_{m_W} = Q_W/D_W`.

**R7 (§9 ambiguity menu is wrong; the residue is smaller than claimed).**
`μ_H = 3/2` is *forced* by `(D_H,Q_H,dq_H) = (42,36,15)`, and
`μ_H = 3/2 + Σ_{1≤j<m_H}(k_j−1)l_j/k_j`, so every stage strictly between 0
and `m_H` must have `k_j = 1`. **"`k₁ ≥ 2` alternatives" do not exist.** The
only ambiguity is how many pure-shift stages are inserted, and every such
insertion is inert for `μ`, `∏k_j`, `T_V`, `M*_F`, `i_V` and the twin
exponent (I re-ran `M*` with `l₁ ∈ {1,2,3,5,11,97}`: unchanged). Consequence:
the report's proposed "smallest data … the single integer `deg(p_{h₁,H})`"
is **not a discriminator for anything in this report** — the shape it pins
is inert. The honest smallest datum is the one in the report's "exact next
lemma": the `(0,y)`-side initialization.

**R8 (citation fidelity, §2).** "for a root `c ∈ C*` exactly one `ν_F`-th
rotation `εc` continues (St 3.18)". The typeset statement introduces `ε`
and then writes "`F ∗ c` exists" with **no `ε`** — `-bbox` shows `∗` ending
at `363.918` and `c` beginning at `366.570`, a 2.65 pt gap, too small for an
`ε` (width ≈ 5.5 pt). So the printed statement is defective and the target's
`εc` is a *repair reading*, not a quotation. The repair is almost certainly
intended and is the reading that makes the two-orbit/two-child merge and the
`V_{2,a}` bookkeeping coherent, but it should be labelled as a reading.

**R9 (test suite is regression-only).** `test_st39_transport_check.py`
re-runs the check script, pins `checks=24987`, and applies two source-string
mutations (`6/7→5/7`, `ω^{−15}→ω^{−14}`). It restates the target's own
formulas and validates no source semantics. P6's phase arithmetic is float
with `tol=1e−6`; I replaced it with an exact free-abelian-group solve, which
passes — so this is a methodology complaint, not a result complaint.

---

## 4. Attacks that found nothing

* **Symbol collision at pole / chain vertex / merge / trunk.** `i_V`, `M*_V`,
  `μ_V`, `dq_V`, `k_V = i_V(μ_V−1)` are used consistently; the one place the
  meaning genuinely changes is the pole (`m = μ = 0`, `i = 1`, no
  enslavement, Prop. 4.2(iv) directly rather than Prop. 8.1(iv)), and the
  target handles it correctly by keeping the scale `d_P/2` explicit. The
  table's "— (`m=0`)" for `i_P` should read `i_P = 1` (cosmetic).
* **Edge orientation.** Confirmed root-ward: trunk → merge → `H₁,H₂` →
  poles, via `deg(p_child) = mult(p_parent,c)` (St 3.17(i)).
* **Satellite roots feeding the chain instead of an escape.** With `β = 0`
  the interior q-pattern is `γ(η−c)^{s₀}` — there are no satellite roots at
  all. §3(c) is right for a stronger reason than given.
* **Tower-depth change feeding the route.** The drop is at the last
  elementary step into each vertex (Cor. 6.1 `F ≺ F′`); extra mid-edge drops
  would only lengthen the tower, and every quantity used is indexed by
  `m_W < m_V` which survives.
* **Root-of-unity / exponent-parity / residue kill.** None. Every transport
  exponent is an integer for every `t`; `3i_V/2 ∈ Z` since `i_H=2`,
  `i_G=14`, `i_tr = 28(4+3t)` are all even; `x² = ω^{−15}` always solvable;
  every gcd/Bezout identity holds in `Z[t]`, so there is no exceptional `t`.
* **Merge attachment asymmetry.** The merge's two orbits both have
  multiplicity 3 and full degree `3i_G = 42 = D_H`; the attachment is forced
  and symmetric; swapping is absorbed by the deck. Confirmed.
* **Trunk ratio consuming the merge scale.** Confirmed: `s₄` (equivalently
  `B_tr`) is a fresh global used nowhere below the trunk.

---

## 5. Maximum safe consequence

For every integer `t ≥ 0`: the displayed td=8 equal-join tree admits an
explicit assignment of f-side top coefficients, enslaved tower tops, q-side
drop tops, orbit gauges and discrete deck/branch choices that simultaneously
satisfies — **as formal data, with all quantities in the free multiplicative
group generated by `c₀, s₀, s₂, s₃, C_tr, B_tr` and roots of unity** —
Statement 3.9(i)(ii)(iii) along every displayed edge for `f` and for every
tower element `h_j` (including the first non-tower element at each vertex),
Prop. 4.2(i)–(iv) with one global tower shared by both branches,
Prop. 4.4/4.6 and its exact form (E), Prop. 8.1(i)–(v) with the reviewed
rigid families at all four pattern vertices, Prop. 5.3/5.4/St 5.2 at both
poles, and the gates St 8.2, St 8.4, St 8.5, Cor. 6.1. The assignment is
unique given the free initialization, up to discrete root choices, and every
pinned quantity is nonzero. **Therefore no vertex-local or cross-vertex
coefficient-transport discriminator at the printed-statement tier removes the
D2 family, for any `t`.**

This proves **no** exact lambda, **no** subtop-jet recursion, **no** source
landing, **no** realization by a polynomial pair, **no** panel exclusion,
**no** degree bound, **no** completeness of the td=8 book, and **no** JC2
result. In particular the constructed system is formal: no `(f,g)` is
produced, and nothing here shows these leading coefficients arise from any
pair of polynomials. The completeness program must proceed through the
`(0,y)`-side initialization, exact lambda, or a global argument, exactly as
the target's §11 firewall states.

**Valid narrow residue preserved:** the two derived laws are sound and
citable after R1–R8 are applied — the drop-stage identity
`l_{m_W}/k_{m_W} = Q_W/D_W` (equivalently `l_m/k_m − (μ_W−1) = dq_W/D_W`)
with the pinned stages `(k₂,l₂) = (7,6)`, `(k₃,l₃) = (112+84t, 635+476t)`,
`k_G = 79`, `k_tr(t) = 39984t²+106650t+71117`; and the twin-gauge identity
`(A₁/A₂)² = ω^{−15}`, read as a *derived* rigidity, not a closure condition.
I add three results the target does not have and which any successor should
carry: the automatic `3.9(i)` cancellation lemma
`deg(Ψ^k − Φ^N) = k·dq − dq + 1`, `lc = −kR/(X(dq−1))`; the root identity
`Ψ_V′(c)[δ_V − (1−u_V)ρ] = R_V`; and the `St 8.5 ⇒ V_{2,a}` structural
necessity, which is what actually keeps this route alive.

**Smallest repair:** two sentences — §3's `β` clause and §7's `= −15`
clause. **Smallest source datum still needed:** unchanged and correctly
identified by the target's §9 "exact next lemma", namely whether
`(C_tr, B_tr, s₀, s₂, s₃, s₄, c₀)` is realizable as the treetop of a
degree-ratio-`(2:3)` pair; the report's alternative candidate
(`deg(p_{h₁,H})`) is inert and should be withdrawn (R7).

No AWS was used or is authorized. No canonical file was edited. This review
does not license any consumer to cite the target's §3 or §7 as written.

---
Report-body SHA-256 (bytes through the separator line above): 0de875253b50684042f8913f5b29781e58d4a7ff38d3a640831808e9b55705d8
