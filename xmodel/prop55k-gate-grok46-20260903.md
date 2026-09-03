# PROP 5.5(k) hostile gate — Grok 4.6 — 2026-09-03

Lane `prop55k-gate-grok46-20260903`. Charged inputs frozen in
`/tmp/jc2-lane.Cg8UT1/inputs`. Manifest generated from
`xmodel/prop55k-gate-grok46-20260903.run.v2` (`charged_input_<i>_sha256=`
paired with `charged_input_<i>_basename=`); `sha256sum -c` returned **9/9
OK**. Stop-on-mismatch did not trigger.

Moh 1983 from `refs/moh1983_jram340_configurations_of_roots.pdf`
(`6c8847a8…`). Rendered `pdftoppm -r 200`; journal page `N` = PDF page
`N−139` (printed page numbers on the PNGs match). Pages opened **as
images**, named in `box/prop55k-gate-20260903/moh-pages/`:

`p151, p164, p165, p166, p168, p169, p170, p171, p172, p176, p177, p178,
p179, p186, p187, p188, p207`.

Every Moh citation below is `SOURCE-READ` of those images, or typed
`SOURCE-UNVERIFIED`. Prime marks `n', m', M_i', V_i', d_i', δ_i', A', 𝔄, k`
are **labels**. `f_i'(x)`, `g_σ'(π)`, `T'_{1,σ}(π)` **are** derivatives
(p.151, p.187). Discipline: no ledger edit; `jc2-lean` not inspected; no
`ideation-20260903T1200Z-*` file and no in-progress lane report opened.
Drivers in `box/prop55k-gate-20260903/`. FALLACY-v2 applied; no exit-price
assertion, so no `charge_basis` line.

AUDIT delta 17(z) remains PROVISIONAL and is **not consumed**.

## 0. Verdict table

| # | charged claim | verdict |
|---|---|---|
| (1) | J enters only via Prop 4.1; `J=cx^k` replaces `−1` by `−(k+1)` in 4.4(3),(6) and 4.6(3); Φ | **CONFIRMED** (primitive entry unique; Moh already wrote the `x^l` remarks) |
| (2) | closed form; 10/10 p.207; 20 NP | **CONFIRMED** (10/10; 20/20 exist and 0 killed; 19/20 NP at `<2·10^{-3}`, C3 at `~7·10^{-3}`; 7/7 independent NP) |
| (3) | `r=1` ODE survives `J=cγ^k`, constant only | **CONFIRMED** (p.170 display + p.171 order-match; Moh “verbatim proof”) |
| (4) | PROP 5.5(k) at `δ_2'=-1`: `d_2'≤(k+1)V_2'`, `g_0\|(k+2)V_2'-d_2'`, `g_0≥V_2'`, sharp | **CONFIRMED** (family attains equality; exact `J=-(k+1)aγ^k`) |
| (5) | modulus `𝔄=A'/gcd(A',L)`; `A'` kills two controls and Moh’s `(21,14;16;2;X)` | **CONFIRMED** as an *extension* correction; **not** an ERRATUM to printed Prop 5.5. Precision GAP on “Prop 5.5 level” (kill is A5-SIMPLE, not Moh’s XOR) |
| (6) | G2/G3 not killed under `𝔄` | **CONFIRMED** (negative) |
| (7) | `k=0` kills 980/980; `k=1..8` kills 88.4–95.5% | **CONFIRMED** (independent census, same integers) |
| (8) | (T) does not follow; obstruction = window `V_2'>d_2'/(k+2)`; `CONJ[APPII-UNIFORM]` | **CONFIRMED** that (T) fails; obstruction named and realised; CONJ remains a conjecture, not proved here |

## 1. Source-read: Prop 4.1, 4.4, 4.6, and Φ

**p.164, Prop 4.1.** With `x=t^{-1}` and `σ=Σ a_j t^j + π t^δ` a `π`-root of
`g`,

```
J_{t,π}(h(σ),g(σ))
  = [λ_h h_σ g'_σ − λ_g g_σ h'_σ] t^{λ_g+λ_h−1} + ⋯
  = − h_f(σ) t^{−2+δ}.
```

Proof, chain rule, printed:

```
J_{t,π}(h(σ),g(σ)) = J_{f,g}(h,g) · J_{x,y}(f,g) · J_{t,π}(x,σ)
                   = h_f(σ) · 1 · J_{t,π}(x,σ) = −h_f(σ) t^{−2+δ}.
```

The factor `1` **is** `J_{x,y}(f,g)`. That is the only place the Jacobian
of the pair enters the radius machine as a coefficient. Replacing it by
`c x^k = c t^{−k}` multiplies the right-hand side by `c t^{−k}` and shifts
its `t`-order by `−k`. Equating orders then sends

```
(n − M_r) λ = −1 + δ     ↦     (n − M_r) λ = −(k+1) + δ.
```

**p.168–171.** Prop 4.4(3) is `λ<(−1+δ)/(n−M_i)`; (6) is
`ord T_r^ψ=(−μ_r+M_r−n)λ−1+δ`. Prop 4.6(3) is `λ=(−1+δ)/(n−m_r)`,
identified in the p.170 proof with order-matching of Prop 4.1(1).
**p.169 Remark (SOURCE-READ):** Moh already treats `J_{x,y}=x^l` “with a
verbatim proof”, replacing (6) by `(6)*` (insert `−l`). **p.171 Remark:**
Prop 4.6 remains valid with (3) replaced by
`(3)* λ=(−1−l+δ)/(n−m_r)`. So `−1 ↦ −(k+1)` (`l=k`) is Moh’s own
localisation. Conditions (1),(2),(4),(5) of 4.6 and the `r≥2` conclusions
are Jacobian-free.

Nit, not a refutation: p.169 lists only `(6)*` for 4.4, not (3). Charged
4.4(3) also acquiring `−(k+1)` is the consistent completion of Prop 4.2(3)
p.165. Primitive entry remains Prop 4.1.

**Φ.** The radius system is `ord g(σ)=nλ`, `ord T_i^ψ(σ)=(−μ_i)λ`
(homogeneous in `(δ,λ)`) closed by the single inhomogeneous relation
above. Scaling `(δ,λ)↦(k+1)(δ,λ)` maps the `k=0` solution onto the `k`
solution. Hence `δ_i^{(k)}=(k+1)·δ_i^{(0)}=(k+1)·`Def 5.1(3) on the same
`(n,M,V)` at `s=2`. Lemma 5.1 p.176 (`δ_s=−1/(n−M_s−1)`) and Def 5.1(3)
p.179 carry that `−1`; they are not a second Jacobian entry.

Scope of the theorem: pairs to which Def 5.1’s major-disc tower applies,
with `J=c x^k`. Not a statement about deforming a fixed pair, and not
checked here for a tower with `s>2` beyond the same scaling (Lemma 5.2
p.177–179 is algebraic in the `δ`-formulae and uses
`(n−L)λ^*=−1+δ^*`, which likewise scales). **Promotable as a theorem
inside that scope.**

## 2. Source-read: `r=1` ODE

**p.170 last display:** if `r=1` then `D(n,−M_1,g_σ,T_{1,σ}^ψ)=` nonzero
constant (Def 4.1 p.164). **p.171:** `T_1^ψ=f+`(poly in `g)`, so
`(T_1^ψ)_f=1`; orders of Prop 4.1(1) match, hence the leading forms
satisfy `D`. Under `J=c t^{−k}`: `λ_g=nλ`, `λ_h=(−M_1)λ`, `ord h_f=0`,
`(3)*` gives `(n−M_1)λ=−(k+1)+δ`. Both sides of Prop 4.1(1) have order
`δ−k−2`. The constant in `D` absorbs `c/λ`. No `π^k`. Moh’s p.171
“verbatim proof” includes this clause. Charged “Prop A.3 form” is
slightly loose (A.3 is the `r≥2` reduction; the ODE is the 4.6 display).
Coprimality p.187 and Prop A.5 p.207 survive.

## 3. Source-read: Prop 5.5 and the Galois modulus (claim 5)

**p.186–187.** Prop 5.5: `s=2`, `g` monic, `deg_y g=n>2`, then either
`k[x,y]=k[T_1^ψ,g]=k[f,g]` or a degree-reducing automorphism exists.
From Prop 5.4: `i=2`, `M_2=n−2`, `δ_2=−1`. Window
`d_2>V_2>d_2/2`, so `0<U_2=d_2−V_2<V_2`. Radius

```
δ_1 = ((n*+m*)U_2 − 1)/((n*+m*)V_2 − 1) = B/A   (reduced),
```

and `0<δ_1<1`, `A>1`. Then `D(n,−M_1,g_σ,T_{1,σ})=` nonzero constant.

**p.188, the Galois step, printed words:**

> “The conjugations of `k((t^{1/A}))` over `k((t))` show us that if the
> reduced denominator `A` of `δ_1` is not a factor of `deg g_σ=n*V_2`
> then `π` is a factor of `g_σ`. Moreover if `A` is a factor of `n*V_2`
> then `g_σ∈k[π^A]` and `π` is a factor of `(d/dπ)g_σ`.”

Then XOR `(A|n*V_2` and `A∤ m*V_2)` or the symmetric alternative, and the
chain `V_2 > V_2−U_2 = C(D+E) ≥ D ≥ V_2`. Contradiction.

**Is “common part in `k((t))`” used at p.188?** **Yes, as the field of
conjugations, not as a numbered hypothesis.** The generator of
`Gal(k((t^{1/A}))/k((t)))` fixes series with integer `t`-exponents and
acts on `π t^{B/A}` by `π ↦ ξ^B π`. Def 5.1(4) p.179 writes
`σ_i=Σ α_j t^j + π t^{δ_i}` without stating `j∈ℤ`. If some `j` has
denominator `L>1`, the correct base is `k((t^{1/L}))` and the modulus
shrinks to `𝔄=A/gcd(A,L)`. Prop 5.6 p.188 *does* assume
`σ_1=π t^{δ_1}` (empty common part); p.207 Appendix II chooses coordinates
so that `σ=π t^{1/4}` on the first row. Prop 5.5 itself never writes that
choice.

At Prop 5.5’s own hypotheses (`k=0`, `δ_2=−1`) one has
`denom(δ_2)=1`, so `L=denom(δ_2)` gives `𝔄=A`. Moh’s modulus is then
identical to `𝔄`. **Printed Prop 5.5 is not refuted by the correction.**
`OPEN[COMMON-PART-LATTICE]` (can an *intermediate* fractional exponent
occur before `δ_1` with no extra major disc?) is still open; a yes at
`k=0` would be an erratum candidate. No witness in this gate.

**Replay of `(21,14; 16; 2; X)` p.207.** Independent arithmetic
(`gate_replay.out` §B), `n'=21`, `m'=14`, `M_2'=16`, `V_2'=2`, `k=1`:

```
δ_2' = −1/2,  δ_1' = 7/6,  A' = 6,  deg(g_σ,T_σ)=(6,4).
L=1:  𝔄=6,  res=(0,4)  →  XOR holds;  A5-SIMPLE: π^4 ‖ T_σ  → KILLED.
L=2:  𝔄=3,  res=(0,1)  →  SURVIVES.
```

So: (i) **uncorrected `A'` does kill the printed row**, but the kill is
**A5-SIMPLE**, which Moh does **not** use at p.188 (he cites A.5 only for
the two coprimalities). Moh’s XOR is *satisfied* at `A'=6`. (ii) The row
is an Appendix-II descended pair with `δ_2'≠−1` and `J=X` (`k=1`); it is
**not in the domain of printed Prop 5.5**. Calling this “killed at Prop
5.5 level” is a precision GAP in the headline; §3.4 of the charged report
states A5-SIMPLE and is accurate.

**ERRATUM vs extension (source-ledger question).** `𝔄=A'/gcd(A',L)` is a
**correction to the extension** of p.188 to `k≥1` and to `δ_2'≠−1` (and
to the new A5-SIMPLE cut). It is **not** an ERRATUM candidate for Moh’s
proof of Prop 5.5 as printed, on the printed hypotheses, unless
`OPEN[COMMON-PART-LATTICE]` is answered yes at `k=0`.

Two existing pairs **do** kill the uncorrected modulus (constructed and
measured below): `(8,4)` and `(12,6)`. That is the fail-closed evidence
that `L=denom(δ_2')` is the working lattice on these objects.

## 4. Closed form, p.207, NP, sharpness (claims 2, 4)

Closed form, `d_2'=gcd(n',m')`, `Π=n*+m*`, `U_2'=d_2'−V_2'`,
`R=n'−M_2'−1`:

```
δ_2' = −(k+1)/R,
δ_1' = (k+1)(Π U_2' − R) / (R(Π V_2' − 1)).
```

Independent `def51` / `closed` / `phi` agree with each other and with the
p.207 table (`p207.png`) on all ten rationals (`gate_replay.out` §A,
`phi_delta.out`, `prop55k.out` §A). At `k=0,R=1` this is Moh’s `B/A`
p.187.

**Newton–Puiseux.** Charged `control_pairs.py` (path-fixed local copy,
`dps=200`): **20/20** have `s'=2`; **0/20** killed by TEST-55(k) with
`𝔄`; **19/20** match the closed form at `<2·10^{-3}`; C3 (`δ_1'=7/2`)
measures `3.493` (charged `~7·10^{-3}`), fail-closed still OK.

Independent `independent_np.py` (`dps=80`, no import of `control_pairs`),
seven constructed pairs with exact `J=cγ^k` and `deg=deg_π`: sharpness
`(4,2,k=1)`, `(6,3,k=2)`, `(9,3,k=2)`, `(15,5,k=4)` all match closed
`(−1, (qk−1)/q)` and SURVIVE both moduli; compositions `(8,4,k=1)` and
`(12,6,k=2)` match `(−1/2,5/4)` and `(−1/2,9/4)`, SURVIVE `𝔄`, **KILLED
by `A'`**; lower-term `(6,3,k=2)` matches `(−1,3/2)`. **7/7** radii
match; **0/7** killed by `𝔄`.

**Leading forms of `(8,4)`** (`leading_form_84.out`), `σ=ω t^{−1/2}+π t^{5/4}`,
`ω^4=1`, `U=t^{1/4}`:

```
P(σ) = 4 ω^3 π t^{−1/4} + 6 ω^2 π^2 t^{3/2} + ⋯     →  T_σ = 4ω^3 π   (exp {1})
Q(σ) = (16 ω^2 π^2 + ω) t^{−1/2} + ⋯               →  g_σ : exp {0,2}
```

(`16ω^6π^2+ω` of the charged report equals `16ω^2π^2+ω` because `ω^4=1`.)
One class mod 2, two classes mod 4: `L=2`, `𝔄=2`, not `A'=4`.

**Sharpness.** For `P=π^{k+1}−γ^{k+1}`, `Q=P^q+aπ`, sympy Jacobian is
exactly `−a(k+1)γ^k` on six pairs `(k,q)∈{(1,2),(2,2),(2,3),(3,3),(4,2),(4,3)}`.
`d_2'=k+1=(k+1)V_2'` with `V_2'=1`; `g_0=1=V_2'` and
`(k+2)V_2'−d_2'=1`. Equality in (ii). Cannot be strengthened for any
`k≥1`. `char_data` on the same family gives `s'=2` and
`M_2'=n'−k−2` (so `δ_2'=−1`). **CONFIRMED + sharp.**

PROP 5.5(k) as stated (XOR `{0,1}` mod `𝔄`; at `δ_2'=−1` and `L=1` the
divisibility chain; window `V_2'<d_2'` and `V_2'>d_2'/(R+1)`) is the
correct generalisation. At `k=0` it contradicts the window (Moh Prop 5.5).

## 5. G2/G3, census, K=16 ray, (T)

**G2/G3 (claim 6).** Independent `galois_test`:

```
G2 (15,10;4;1;k=4): δ'=(−1/2,5/4), A'=4, L=2, 𝔄=2, deg=(3,2), res=(1,0) SURVIVES
                    L=1: Aa=4, res=(3,2) KILLED four ways (GALOIS-neither, two A5, MONOMIAL)
G3 (21,14;8;1;k=2): δ'=(−1/4,9/8), A'=8, L=4, 𝔄=2, deg=(3,2), res=(1,0) SURVIVES
                    L=1: Aa=8, res=(3,2) KILLED four ways
```

Negative reported. Charged `descent-radii` COUNTING-BOUND on G2/G3 is
**not consumed**.

**Census (claim 7).** Independent sweep, `δ_2'=−1`, `n'≤60`, same
admissibility as `census55k.py` (`V_2'>d_2'/(k+2)`, `V_2'<d_2'`, skip
`A'=1` as inapplicable):

```
 k   rows  A'=1  killed     %    survivors
 0    980     0    980  100.0        0
 1   1654     0   1580   95.5       74
 2   1936    29   1772   92.9      135
 3   2082    33   1882   91.8      167
 4   2169    51   1905   89.9      213
 5   2228    68   1952   90.4      208
 6   2264    72   1941   88.5      251
 7   2288    78   1971   89.2      239
 8   2306    99   1950   88.4      257
```

Byte-identical to `census55k.out`. Charged `k=0` extension `n'≤120`:
5338/5338, XOR holds on **0** rows (Moh’s chain is the proof that XOR is
arithmetically empty at `k=0`; the census is an independent check, not
the proof). DIVCHAIN/MASTER contribute **0** kills at every `k` in the
`n'≤60` table: once `k≥1`, the residue is exactly the XOR set, and (ii)
holds on it. **CONFIRMED.**

**K=16 descendants (task c).** `(n',m')=(12t+4, 8t+4)`, `M_2'=12t+1`,
`V_2'=3`, `k=1`, `t=1..6`. Always `d_2'=4`, `R=2`, `δ_2'=−1`,
`δ_1'=t/(3t+1)`, `A'=𝔄=3t+1`, `res=(0,1)`, `g_0=Ψ=5≥3`,
`d_2'=4≤6=(k+1)V_2'`. **None killed** (expected). `t=1` is Moh’s
`(16,12;13;3;X)` row. Window is *not* `U>V` here (`U_2'=1<3`); they
survive because `{0,1}` is satisfiable and (ii) is consistent.

**Claim (8).** Theorem (T) at `δ_2'=-1` does **not** follow from
PROP 5.5(k) for `k≥1`. The named obstruction is Def 5.1(2):
`V_2>d_2/(n−M_2)` becomes `V_2'>d_2'/(k+2)` rather than `V_2>d_2/2`, so
`U_2'<V_2'` can fail and the p.188 chain closes to the consistent
`d_2'≤(k+1)V_2'`, attained by the sharpness family. **CONFIRMED.**
`CONJ[APPII-UNIFORM]` is a typed conjecture about Appendix II’s level-2
datum; this gate did not run it. `OPEN[A-PRIME-ONE]` and
`OPEN[COMMON-PART-LATTICE]` remain open; neither was filled by cap.

## 6. Promotability

**Φ.** Promote as a theorem: for a pair with `J_{x,y}=c x^k` (equivalently
`J_{γ,π}=c γ^k` in the descended gauge) to which Def 5.1 applies at
`s=2`, the geometric radii in `t=x^{-1}` are
`δ_i = (k+1) · Def 5.1(3)(n,M,V; s=2)`. Proof: Prop 4.1 + uniqueness of the
linear system closed by Prop 4.6(3)*; Moh p.169 and p.171 already record
the `x^l` change of that closing. Confirmation: 10/10 printed p.207, 20
existing-pair NP (7 reconstructed independently).

**Corrected modulus.** Promote as the Galois modulus of the **extension**
of p.188 to `k≥1` / `δ_2'≠−1`, with working rule `L=denom(δ_2')`
fail-closed on every control of this gate. **Do not** enter it in the
source ledger as an ERRATUM to Moh Prop 5.5. A5-SIMPLE is a new cut
(Moh uses A.5 only for coprimality at p.187); it is what makes the `k=0`
census close by Galois/A5 arithmetic rather than by firing DIVCHAIN.

## 7. FALLACY-v2

No cv-flag / place / series identification. Prime marks kept as labels.
Floor vs attainment: (ii) is a theorem *and* has an attaining family, so
sharpness is not a floor misread as equality. No `sat()` wrapping. No
merge-free / M-descent claim. No new exit-price. `OPEN`s left `OPEN`.
G2/G3 negative is not converted into a kill by the uncorrected modulus.

## 8. Drivers

`box/prop55k-gate-20260903/`: named `moh-pages/pNNN.png` (200 dpi);
`gate_replay.py` (closed form, `(21,14)`, G2/G3, K=16, sharpness `J`,
census); `independent_np.py` (7 constructed pairs); path-fixed
`control_pairs_local.py` (20/20); reruns of `prop55k.py`,
`census55k.py`, `phi_delta.py`; `leading_form_84.out`. Deterministic.

## Typed block

```text
CONFIRMED     Phi: unique primitive Jacobian entry is J_{x,y}=1 in Prop 4.1
              p.164; J=c x^k sends Prop 4.4(6) / Prop 4.6(3)  -1 |-> -(k+1)
              (Moh p.169 (6)* and p.171 (3)* already).  delta_i^{(k)} =
              (k+1) delta_i^{(0)}.  Theorem, scope = Def 5.1 tower, s=2.
CONFIRMED     closed form 10/10 p.207; 20/20 existing pairs s'=2, 0 killed
              by 𝔄; 19/20 NP <2e-3, C3 ~7e-3; 7/7 independent NP.
CONFIRMED     r=1 ODE D(n,-M_1,g_σ,T_{1,σ})=nonzero const is invariant
              under J=c gamma^k (orders still match via (3)*; value c/λ).
CONFIRMED     PROP 5.5(k)(ii) at delta_2'=-1, L=1: g0>=V2',
              g0 | (k+2)V2'-d2', hence d2'<=(k+1)V2'; sharp via
              P=pi^{k+1}-gamma^{k+1}, Q=P^q+a pi, J=-(k+1)a gamma^k.
CONFIRMED     𝔄=A'/gcd(A',L) is the correct modulus of the EXTENSION of
              p.188 to k>=1 and delta_2'!=-1.  A' kills existing (8,4)
              and (12,6).  p.188 DOES use conjugations over k((t)).
GAP           "A' kills Moh's (21,14;16;2;X) at Prop 5.5 level": arithmetic
              yes, by A5-SIMPLE not by XOR; the row is App. II, k=1,
              delta_2'=-1/2, outside printed Prop 5.5.  Not an ERRATUM
              to Moh's proof of Prop 5.5 (k=0, delta_2=-1, 𝔄=A).
CONFIRMED     G2/G3 SURVIVE under 𝔄 (res=(1,0)); KILLED under A'.
CONFIRMED     census n'<=60: k=0 980/980; k=1..8 95.5,92.9,91.8,89.9,
              90.4,88.5,89.2,88.4 % ; K=16 descendants t=1..6: 0 killed.
CONFIRMED     (T) does not follow for k>=1 at delta_2'=-1; obstruction =
              window V2' > d2'/(k+2).  CONJ[APPII-UNIFORM] untested here.
NOT-CONSUMED  AUDIT delta 17(z); descent-radii COUNTING-BOUND on G2/G3;
              OPEN[A-PRIME-ONE]; OPEN[COMMON-PART-LATTICE];
              OPEN[MINOR-DICHOTOMY].
SOURCE-READ   Lemma 2.1 p.151; Prop 4.1+Def 4.1 p.164; Prop 4.2 p.165;
              Prop 4.4 p.168 + x^l remark p.169; Prop 4.6 p.170 + r=1
              proof and x^l remark p.171; Lemma 5.1 p.176; Lemma 5.2
              p.177-179; Def 5.1 p.179; Prop 5.4/5.5 p.186-188;
              Prop 5.6 p.188; Prop A.5 + p.207 table + sigma=pi t^{1/4}.
```

<!-- BODY-END -->
