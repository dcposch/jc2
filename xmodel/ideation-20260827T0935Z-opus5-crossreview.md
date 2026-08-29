# Cross-pollination and adversarial synthesis — Opus 5 — round `20260827T0935Z`

Date: 2026-08-27
Author: Opus 5, standing whole-portfolio co-researcher (cross-review phase)
Status: **CROSS-REVIEW / NAVIGATION. NOTHING PROMOTED. NO AWS LAUNCHED. NO
HEAVY LOCAL CAS RUN. NO CANONICAL LEDGER EDITED. `jc2-lean` NOT ENTERED,
READ, BUILT, STATUS-INSPECTED, STAGED, CLEANED, OR MODIFIED.**

The only repository file written by this session is this one.

---

## 0. Custody

All fourteen prompt-pinned files were SHA-256 verified by recomputation
*before* being read; `shasum -a 256 -c` returned **14/14 OK**. The list is
reproduced verbatim in §13.

Two canonical files have drifted since the sealed packet pinned them, which
matters for reading the blind reports:

```text
packet pin                                   on disk now (2026-08-27, this session)
APPROACHES.md  92006f6d7222a5b7…             c8814c8b1bab4f78…      DRIFTED
AUDIT.md       b6c8158e87e78773…             3a6c6eb0caf7161a…      DRIFTED
PROGRESS.md    15d7ed1075317c8f…             024629ce84ef2039…      DRIFTED
COORDINATION.md 72d789d3f7fbceff…            72d789d3f7fbceff…      unchanged
```

That is expected (the campaign wave continued past 09:35Z) and is not a
defect. It does mean **no disposition vector in any of the four blind
reports may be diffed against today's ledger**; they are all correct
relative to their pinned snapshot. I make no ledger edits and propose no
renumbering.

Post-snapshot evidence consumed, at the tier the prompt assigns it:
V45 `RESULT.md`/`PASS_EVIDENCE.sha256` (exact producer evidence, separate
Opus review live — **not** promotable here); K00 V14 `CUSTODY_GAP.md`
(a *negative* custody finding, freely usable); V14R1 `PREREGISTRATION.md`
(design only); the coordinator's verbal V14R1 delta (exact-Q and `p=65521`
endpoints pass, 36 lift entries, fresh-process replay of
`-h*r7 + sum u_i*r_i = 0` with `h = 63*d4 + 20`) — **provisional delta
context only**, flagged as such at every use below.

Executed here (desk scale, exact `Fraction` arithmetic in stock Python; no
Singular, no CAS, no AWS): SHA verification of all pins; exact verification
of the four three-row syzygies and of the derivation of `g1,g2,g4` from the
`AC/L` and `C^2/L^2` primitives (§6.2); byte reads of
`compile_total_dehom_eliminant_v43.py`, `compile_cascade_dehom_v43.py`,
`homogenize_total_dehom_lift_v43.py`,
`replay_constructive_cascade_v43c1.py`; hand algebra everywhere else.

---

## 1. Item 1 — the two-fibre criterion, re-proved from first principles

I re-derive it from scratch, then attack it. **The criterion survives, in a
form that is strictly stronger and cheaper to prove than what I submitted
blind.** The blind proof used irreducible components over an algebraically
closed field; it is superseded by a two-line effective induction.

### 1.1 Setting and notation

`S = Q[rho, X]`, `X = {x_1,…,x_n}` with `sigma`-weights `w(x_j) > 0` and
`w(rho) = 0`. The grading is by `Z_{>=0}`, so the weight-zero graded piece of
`S` is exactly `Q[rho]`. `J ⊆ S` is `sigma`-homogeneous, `a1 ∈ X` with
`w(a1) = 5`, `K = J : a1^infinity`, `E = K ∩ Q[rho]` (= the weight-zero part
of `K`), `T = {u ∈ Q[rho] : u(0) != 0}`, `D = T^{-1}Q[rho] = Q[rho]_(rho)`
(a DVR), `S' = D[X] = T^{-1}S`, `L = Q(rho)`, `J0 = J|_(rho=0) ⊆ Q[X]`.

### 1.2 The one nonstandard ingredient: a clearing lemma

> **Lemma C (clearing).** Let `A` be any commutative ring, `I ⊆ A` an ideal,
> `f, t ∈ A`. If `t^e f^M ∈ I` and `f^m ∈ I + (t)`, then
>
> ```text
> f^(M + e*m) in I.
> ```

*Proof.* Claim: `f^(M+k*m) ∈ I + (t^k f^M)` for all `k >= 0`. For `k = 0` it
is trivial. If `f^(M+k m) = j + t^k f^M s` with `j ∈ I`, write
`f^m = j' + t h` with `j' ∈ I`; then

```text
f^(M+(k+1)m) = j*f^m + t^k f^M s (j' + t h)
             = [ j*f^m + t^k f^M s j' ] + t^(k+1) f^M (s h),
```

and the bracket lies in `I`. At `k = e` the trailing term lies in
`(t^e f^M) ⊆ I`. ∎

Lemma C is the effective form of the standard decomposition
`sqrt(I) = sqrt(I : t^infinity) ∩ sqrt(I + (t))`. What matters for the
campaign is that it is **constructive, unconditional, and exponent-explicit**:
no Noetherian hypothesis, no homogeneity, no field, no flatness, no
irreducibility, no algebraic closure. §3 shows it is literally an instance of
Sol's frozen `clear_power` primitive, which turns it into a runnable
certificate compiler.

### 1.3 Theorem A, restated and proved

> **Theorem A.**
>
> **(A1)** `K + (rho) = (1)`  ⟺  `E ⊄ (rho)`  ⟺  there exist `N` and
> `u ∈ Q[rho]` with `u(0) != 0` and `a1^N u ∈ J`  ⟺  `a1 ∈ sqrt(J S')`.
>
> **(A2)** `E != 0`  ⟺  `a1 ∈ sqrt(J L[X])`  ⟺  `J|_(a1=1) = (1)` over `L`.
>
> **(A3)** `a1 ∈ sqrt(J0)`  ⟺  `J0|_(a1=1) = (1)` over `Q`.
>
> **(A4)** `K + (rho) = (1)`  ⟺  (A2) **and** (A3).
>
> **(A5) (effective)** if `a1^M u ∈ J` with `u = rho^e v`, `v(0) != 0`, and
> `a1^m ∈ J + (rho)`, then `a1^(M+e*m) w ∈ J` for some `w` with `w(0) != 0`.

*Proof.*

**(A1).** Suppose `1 = k + rho s`, `k ∈ K`. `K` is homogeneous (`J`
homogeneous, `a1` homogeneous), so taking weight-zero parts,
`1 = k_0 + rho s_0` with `k_0 ∈ K ∩ Q[rho] = E` and `s_0 ∈ Q[rho]`; setting
`rho = 0` gives `k_0(0) = 1 != 0`, so `E ⊄ (rho)`. Conversely `u ∈ E` with
`u(0) != 0` gives `u(0) ∈ E + (rho)`, hence `1 ∈ K + (rho)`. `u ∈ E` means
exactly `a1^N u ∈ J` for some `N`. Since `T` consists of units of `S'`,
`a1^N u ∈ J` with `u ∈ T` ⟺ `a1^N ∈ J S'` (clear the common `T`-denominator
in the converse), i.e. ⟺ `a1 ∈ sqrt(J S')`.

**(A2).** `E != 0` gives `0 != u ∈ Q[rho]` with `a1^N u ∈ J`; `u` is a unit
of `L`, so `a1^N ∈ J L[X]`. Conversely clear the `Q[rho]`-denominators of
`a1^N ∈ J L[X]`. For the dehomogenized form: `J L[X]` is homogeneous with
`w(a1) = 5 > 0`, so `V(J L[X])(Lbar)` is a weighted cone; a point with
`a1 = c != 0` scales by `t = c^(-1/5) ∈ Lbar` onto the `a1 = 1` slice.
Hence `a1` vanishes on `V(J L[X])` ⟺ the `a1 = 1` slice is empty ⟺
`J|_(a1=1) = (1)` in `L[X \ {a1}]` (weak Nullstellensatz over `L`).

**(A3).** The same weighted-cone argument over `Q`.

**(A4).** (⟹) `S' → L[X]` and `S' → S'/rho S' = Q[X]` are ring maps, so
`a1 ∈ sqrt(J S')` implies both. (⟸) `E != 0` gives `rho^e a1^M ∈ J S'`;
`a1 ∈ sqrt(J0)` gives `a1^m ∈ J S' + (rho)`; **Lemma C** with `A = S'`,
`I = J S'`, `t = rho`, `f = a1` gives `a1^(M+em) ∈ J S'`, i.e. (A1).

**(A5).** The same application of Lemma C, tracked over `S` and cleared. ∎

Everything holds verbatim with `t = rho^2` in place of `rho`, because the
frozen rows lie in `Q[t][X]` (`total_to_t` raises on any odd `rho` exponent)
and `t` also has weight zero. It follows that the `u` produced is
automatically **even** in `rho`, so the promoted criterion's `U(rho^2)`
normal form is obtained for free rather than assumed.

### 1.4 The counterexample search the prompt mandates

I looked for each named failure mode. Results:

**(a) Nonhomogeneous — the criterion genuinely breaks.**
`S = Q[rho, x]`, `J = (rho x - 1)`, `f = x`. `J` is prime and `x ∉ J`, so
`K = J : x^infinity = J` and `E = J ∩ Q[rho] = 0` (any nonzero multiple of
`rho x - 1` has positive `x`-degree). Yet
`K + (rho) = (rho x - 1, rho) ∋ rho*x - (rho x - 1) = 1`, so
`K + (rho) = (1)` while `E = 0`. **(A1)'s necessity direction is false
without homogeneity.** Its *sufficiency* direction (`E ⊄ (rho) ⟹ unit`) is
unconditional. Precise accounting: homogeneity is used in exactly two places
— the weight-zero projection in (A1), and the weighted-cone dehomogenizations
in (A2)/(A3). Nowhere else. In particular **Lemma C and hence (A4) need no
homogeneity at all.**

**(b) Torsion — the case my blind §6.2 assumed was live really exists.**
`A = Q[t, x]`, `J = (t x)`, `w(x) = 1`. Then `A/J` has `t`-torsion supported
on `D(x)`. Here `K = J : x^infinity = (t)`, so `E = K ∩ Q[t] = (t) != 0`,
but `E ⊆ (t)` and `K + (t) = (t) != (1)`. The hypothesis that fails is (A3):
`J0 = 0` and `x ∉ sqrt(0)`. **So `E != 0` with `E ⊆ (t)` is a real
phenomenon; it is excluded only by the special-fibre half.** This is the
counterexample that decides item 2 below, and it is the reason the code's
`t = 0` control is load-bearing rather than decorative.

**(c) Non-flat.** No counterexample exists and none can: (A4) is the
decomposition `V = closure(V ∩ D(rho)) ∪ (V ∩ V(rho))`, which holds for any
ideal. Flatness of `Q[rho] → S/J`, semicontinuity, and base-change theorems
are **not used and not needed**. Any successor report that invokes flatness
here is adding a hypothesis for nothing.

**(d) Contraction — a real trap, correctly avoided by the existing code.**
`E = K ∩ Q[rho]` and `J ∩ Q[rho]` are different ideals, and the second is
usually `0` when the first is not. Example: `J = (t a1)`, `w(a1) = 5`. Then
`J ∩ Q[t] = 0` but `K ∩ Q[t] = (t)`. The correct computational identity is

```text
Elim := ( J|_(a1=1) ) ∩ Q[rho]  =  E  =  K ∩ Q[rho],     exactly.
```

(⟸ rehomogenize a weight-zero `u`; ⟹ dehomogenize `a1^D u ∈ J`.)
**Elimination must be run after dehomogenizing at `a1 = 1` (equivalently
after inverting `a1`), never on the homogeneous ideal.** The V43 eliminant
compiler does dehomogenize first (`dehom_text` drops the `a1` exponent from
every monomial), so it computes the right object. A successor that
"simplifies" by eliminating from the homogeneous rows would silently compute
`0` and report `no-unit-eliminant` forever.

**(e) Saturation-vs-specialization.** The only interchange used is
`sp(J S' + (rho)) = J0`, which is the surjectivity of `S' → Q[X]` — trivial.
No claim of the form `sp(J : a1^infinity) = sp(J) : a1^infinity` is made or
needed anywhere. The staged converse the ledger already withdrew (fibre
emptiness ≠ `1 + rho W`) is untouched: (A4) is not that statement, because
it *conjoins* the generic fibre.

### 1.5 The minimal correct theorem, and one hypothesis to re-assert

Nothing needs withdrawing. The minimal statement is (A4) plus the two
hypotheses **(H1)** `J` is `sigma`-homogeneous with `w(rho) = 0` and every
other variable of positive weight, and **(H2)** `w(a1) > 0`. Both are
promoted by `98003865…` and enforced structurally by
`census_j2_typed_v23.py:128-145` (`sigma_weight("rho") = 0`,
`sigma_weight("a1") = 5`).

One hypothesis a successor must re-assert rather than inherit: the identity
`sp(J_total) = J0` on the literal 70-row corpus with `ez9` a genuine
spectator. That is exactly what `reconstruct_rows()` enforces by byte-exact
`rho`-zero bridge and what my V43 review verified at §1.3–§1.5. It is
inherited by Theorem A, not proved by it.

### 1.6 Certificate extraction: Fable's converter needs one added step

Fable's §3.1 says the dehomogenized identity "rehomogenizes directly … already
weight-homogeneous since `u` has weight 0". **Sound but incomplete.** Naive
monomialwise rehomogenization is not well defined when weights are not
multiples of `w(a1) = 5`. The correct construction is:

1. Split each cofactor `H_i` into its parts supported in weights `≡ r (mod 5)`.
2. Keep only the residue class `r ≡ -w_i (mod 5)` for row `g_i`; the
   surviving sum is still `= u` because `u` has weight `0 ≡ 0 (mod 5)` and the
   other residue classes sum to zero separately.
3. Rehomogenize the retained part at a common target weight `5D`; then
   `a1^D u = sum_i H_i^[5D - w_i] * g_i`, homogeneous of weight `5D`.

This is not a hypothetical repair: `homogenize_total_dehom_lift_v43.py`
**already implements exactly this** — it keeps monomials with
`total_weight % 5 == 0` (line 158), asserts that the residue-zero part alone
replays the unit (`FAIL "residue-zero dehom replay"`, line 164), sets
`exponent = homogenizing_weight // 5` (line 167), and rejects any monomial
with `deficit % 5 != 0` (line 174). So the gap is in the *statement*, not the
code. Grade for Fable's converter: **sound with scope correction**; the
correction should be written into any promoted version of the lemma.

---

## 2. Item 2 — the selected total-`rho` eliminant predicate: my criticism is
## mostly withdrawn

### 2.1 The exact predicate the code implements

From `compile_total_dehom_eliminant_v43.py:125-144`, in order:

```text
ideal I0=subst(I,t,0); ideal G0=std(I0); poly specialnf=reduce(1,G0);
if (specialnf!=0) { print("FAIL_V43_TOTAL_DEHOM_SPECIAL_CONTROL"); quit; }   // (S)
ideal E=eliminate(I,<product of all active vars>);                            // (E)
for (ci…) if ((unitfactor==0)&&(candidate!=0)&&(subst(candidate,t,0)!=0))
          { unitfactor=candidate/subst(candidate,t,0); }                      // (U)
if (unitfactor==0) { print("V43_TOTAL_DEHOM_OUTCOME=no-unit-eliminant"); quit; }
```

`I` is the 17 SELECTED rows dehomogenized at `a1 = 1`; `E` is `I ∩ Q[t]`,
which by §1.4(d) is exactly `E' = K' ∩ Q[t]` for `J'` = the 17-row subideal.
`Q[t]` is a PID, so `E' = (h)`, and if `h(0) != 0` then at least one returned
generator has nonzero constant term (if every generator `h c_i` had `t | h c_i`
with `t ∤ h`, then `t | c_i` for all `i`, contradicting `gcd(c_i) = 1`). So
predicate (U) is exactly `E' ⊄ (t)`.

### 2.2 Exact interpretations, once special-fibre emptiness is known

Let `J'` = 17 selected rows, `J` = all 59 nonzero rows, `E' ⊆ E`.

| Observation | Exact meaning | Consequence |
|---|---|---|
| `J'0\|_(a1=1) = (1)` over `Q` (control S) | `a1 ∈ sqrt(J'0)`, hence `a1 ∈ sqrt(J0)` | special-fibre half **done**, for these very rows |
| `E' != 0` | generic fibre of `J'` empty on `D(a1)` | **with (S), `K' + (rho) = (1)`, hence `K + (rho) = (1)`: the chart closes** |
| `E' ⊄ (t)`, i.e. a nonzero constant term | same as above, *plus* an explicit `U` | closes the chart **and** displays the certificate |
| `E' = 0` | 17 rows admit a horizontal survivor | **no information about `J`**; must escalate to 59 |
| `E = 0` (all 59 rows) | generic fibre of `J` nonempty on `D(a1)` | **no `a1^N U(rho^2)` certificate at any `N`**; the whole total-`T-a1` certificate programme dies in one step |
| modular `rho = c` screen returns unit | `V(J\|_(rho=c)) ∩ D(a1) = ∅` mod `p` | evidence only: mod-`p` unit does **not** imply unit over `Q` (`(p x - 1)` is `(1)` mod `p`, not over `Q`) |
| exact-`Q` `rho = c` at random rational `c` | rigorous: `c ∉ pi(Z)` where `Z = V(J) ∩ D(a1)` | since `pi(Z)` is constructible in `A^1`, it is finite or cofinite; one exact rational miss makes "finite" overwhelming but not proved |

### 2.3 Verdict on my blind §6.2: **withdrawn as a defect**

My blind claim was that the code conflates `E' = 0` (chart fails) with
`E' != 0, E' ⊆ (t)` (chart closes), and reports the second as failure.
The mathematics of the second case is real (§1.4(b) exhibits it). But **in
this code it is unreachable**: control (S) runs first and quits on failure,
and (S) is precisely `a1 ∈ sqrt(J'0)`, so Theorem A(A4) applied to `J'`
forces `E' != 0 ⟹ E' ⊄ (t)`. The predicate is therefore *redundant but
correct*, and `no-unit-eliminant` really does mean `E' = 0`.

I also over-claimed sourcing: I wrote that control (S) "passes today". **No
harvested run of `compile_total_dehom_eliminant_v43.py` exists** — the case
directory has only `aws_box03_rho0_dual_modp_…`,
`aws_r6d_rho0_dual_compiler_…`, `aws_r6d_rho0_dual_exact_resume_…`. What is
established is the sibling fact: `compile_cascade_dehom_v43.py` uses the
**identical 17-row `SELECTED` tuple**, loads them by name from V37's frozen
`load_rows()` (asserting the 70-row census and that no zero-weight variable
survives dehomogenization), and returned `V43_DEHOM_OUTCOME=unit`. That is
the packet's "17-row `rho=0,a1=1` exact Gröbner basis is the unit ideal".
So (S) is *predicted* to pass on identical input, not *observed* to pass.

### 2.4 What survives, and the smallest fail-closed patch

Two residual points, both worth a two-line change:

1. **Convert the redundancy into a free theorem-mutation detector.** Under
   (S), `E' != 0 && E' ⊆ (t)` is mathematically impossible. Emit
   `V43_TOTAL_DEHOM_ELIMINANT_NONZERO` and **fail closed** if it is `1` while
   `unitfactor == 0`:

   ```text
   int nz=0; for (ci=1;ci<=size(E);ci++) { if (E[ci]!=0) { nz=1; } }
   print("V43_TOTAL_DEHOM_ELIMINANT_NONZERO="+string(nz));
   if ((nz==1)&&(unitfactor==0))
   { print("FAIL_V43_TOTAL_DEHOM_ESCAPE_CONTRADICTION"); quit; }
   ```

   Cost: nothing. Benefit: it detects a corrupted row set, a wrong ring, a
   dropped `t`, or a broken `eliminate`, because any of those breaks the
   theorem's prediction. This is strictly better than what I proposed blind
   (branching on `nz`), because branching would have *weakened* a guard;
   asserting *strengthens* it.

2. **Retag the failure token for one-sidedness.** `no-unit-eliminant` should
   read `no-eliminant-selected-rows-inconclusive`, with the scope line
   "selected-row non-unit proves nothing about `J`; escalate to all 59".
   Fable's §3.1 states this one-sidedness explicitly and correctly; it is not
   currently written into the lane.

Mutations that should fire (each a one-coefficient or one-row edit, all
desk-cheap once a run exists): drop `Tg19_7` from `SELECTED` (the reviewed
V42 mutation target) — must change the outcome or the eliminant degree;
perturb one `Tg15_3` coefficient — same; set `t` to a symbol not in the ring
— must fail the ring build; run `eliminate` on the *homogeneous* rows —
must return `0` (this is the §1.4(d) contraction trap and should be an
explicit negative control); run the design's toy `J = (f - t x)` through the
same pipeline — must return `no eliminant` (positive control on Theorem A
itself, §1.4 and my blind §5.4).

---

## 3. Item 3 — Sol's constructive radical certificate tree

Source: `cases/max12_812_order2_p0_total_rees_j2_a1_constructive_cascade_v43c1_20260827/replay_constructive_cascade_v43c1.py`
(read here; its `LOCAL_ABORT.md` records a deliberate local kill at 108.47 s /
4.22 GB RSS with no verdict — correctly, no mathematics was claimed).

A "certificate" is `target = sum_labels multiplier * generator`, where
generators are frozen rows **and** named branch assumptions.

### 3.1 The three combination identities, derived and checked against the code

Write `T_L = a*f + A` (`A` a combination of the non-`f` generators) and
`T_R = b*g + B`.

**(i) Branch product, `factor * f * g ∈ I` (`combine_branches`).**

```text
factor*T_L*T_R = (a*b)*(factor*f*g) + factor*T_R*A + factor*a*f*B.
```

Verified termwise against the code: relation terms scaled by `af*bg`; left
non-assumption terms scaled by `factor*right.target`; right non-assumption
terms scaled by `factor*af*f`; answer target `factor*T_L*T_R`. **Exponents
add**: two `a1`-power targets `a1^m`, `a1^n` yield `factor * a1^(m+n)`.

**(ii) Power clearing, `factor * f^e ∈ I` (`clear_power`).** With
`u = T_L`, `v = a*f`, `u - v = A ∈ I'`:

```text
factor*u^e = factor*(u-v)*sum_(k=0)^(e-1) u^(e-1-k) v^k  +  a^e*(factor*f^e).
```

Verified termwise: `geometric` is exactly `sum u^(e-1-k) (bf)^k`;
non-assumption terms scaled by `factor*geometric`; relation terms scaled by
`multiplier^e`; target `factor*T^e`. **Exponents multiply** by `e`.

**(iii) Linear clearing, `x*f ∈ I` (`clear_linear` = `clear_power`, `e=1`).**
`x*T_L = x*A + a*(x*f)`, so the target picks up the factor `x` and the
exponent is unchanged. **This is the dangerous primitive**: the accumulated
`prod(factors)` must ultimately be a nonzero *constant*, or the tree proves
`(nonconstant) * a1^N ∈ J0`, which is strictly weaker than `a1^N ∈ J0` and
is **not** what the promoted criterion consumes.

**Verdict on the algebra: `sound`.** All three identities are correct as
implemented; the guards (`relation retains assumption`, `crossed branch
assumptions`, `branch relation retains split`) are the right fail-closed
contracts. The `factor` bookkeeping is the tree's real soundness burden and
the code does track it.

### 3.2 Cost: the exponent growth is the blowup

Along a tree with `combine_branches` at internal nodes, the target exponent is
the **sum over leaves**; `clear_power` **multiplies**. The cofactors carry
`u^(e-1-k) v^k` and `factor*right.target`, so multiplier degree grows at
least as fast as the target exponent. Since `a1^6 ∉ J0` (V43) and the V42
leaf is `a1^8` in the *branch* ideal `I_A1` (`rho = 0` **and** `rs1 = 0`, per
`5d4c42ff…` §Headline — **not** `a1^8 ∈ J0`, a correction I made in my V43
review §7.3 and repeat here because two blind reports still read it the other
way), the composed exponent will be well above 8 and the cofactor expansion
is exactly the 192-GiB pathology in a different container. The 108 s / 4.2 GB
local abort is consistent with that.

### 3.3 Can the cascade be compiled into a direct unsplit certificate, and
### does it dominate the dehomogenized GB?

**Yes to the first, emphatically no to the second — but the engine has a
different, much better job.**

- It *can* be compiled: the three identities suffice, and the code already
  does it. What it produces is `a1^N ∈ J0` for some `N >= 7`.
- It does **not** dominate the `Q(rho)` Gröbner run, for three independent
  reasons: (a) it computes the **special-fibre exponent**, which by
  Theorem A appears nowhere in the criterion; (b) the special-fibre *fact*
  (`a1 ∈ sqrt(J0)`) is already established by the 17-row unit GB, so the tree
  adds only the numeral `N`; (c) its cost grows with `N`, while the eliminant
  cost does not depend on `N` at all.

- **The job it should have.** Lemma C is *literally* an instance of
  `clear_power`. Take
  - `certificate`: the special-fibre identity `a1^m = sum c_i g_i + h*rho`,
    i.e. target `a1^m`, assumption `rho` with multiplier `h`;
  - `relation`: the eliminant/lift output `rho^e * (v * a1^M) ∈ J` with
    `v(0) != 0`, i.e. `factor = v * a1^M`, exponent `e`;

  then `clear_power` returns target `v * a1^(M + e*m) ∈ J` with `v(0) != 0` —
  **exactly the promoted criterion's object `a1^N U(rho^2)`, `U(0) != 0`**,
  with the exponent displayed. So the certificate tree is the natural
  **certificate compiler for the positive branch of the generic-fibre run**,
  operating over `S' = D[X]` with `rho` as the split variable, not over `R0`
  with the branch variables as splits. That retargeting costs no new
  mathematics and reuses a frozen, hash-pinned engine.

Grade: **`sound` (algebra), `sound with scope correction` (as a route: right
engine, wrong ring and wrong target).**

---

## 4. Item 4 — reconciling N=6, seeded N=7, the lift jobs, and the generic
## fibre: a wall-clock-optimal policy

### 4.1 One-sided vs two-sided, stated exactly

| Result | Sidedness | Decides `K+(rho)=(1)`? |
|---|---|---|
| `a1^6 ∉ J0` (V43, exact-Q, my review PASS) | one-sided negative; **prefix-fragile** (adding grade-20+ rows can destroy it) | no |
| `a1^7 ∉ J0` (seeded N=7 dual) | same, one bit | no |
| `a1^N ∈ J0` (multiplier extraction / `lift` / `lp` / high-mem) | one-sided positive; **prefix-monotone** | no — the criterion contains no `N` |
| 17-row `E' != 0` | **positive, decisive** (with control S) | **yes — chart closes** |
| 17-row `E' = 0` | one-sided; no information about `J` | no |
| 59-row `E = 0` | **negative, decisive** | **yes — no certificate at any `N`; programme dies** |

Note the asymmetry that decides the budget: the ladder buys the *fragile*
kind of result (a nonmembership floor that later rows can destroy), while the
eliminant buys the *monotone* kind (a membership certificate that survives
adjoining rows, and an emptiness that survives it too). Fable states this as
"asymmetric finality"; I state it as prefix-fragility. Same content,
independently derived, and it is the single strongest argument for the
reallocation below.

### 4.2 The decisive experiment is already compiled and is not a new lane

`compile_total_dehom_eliminant_v43.py` **is** Card A / Card F1 for the 17
rows. Its special control is the 17-row unit GB (already positive on the
identical row tuple). Its `eliminate` phase computes `E'`. Its `lift` phase
plus `homogenize_total_dehom_lift_v43.py` already emits
`a1^exponent * U(t) ∈ J'`, `U(0) = 1`, with the residue-class rehomogenization
of §1.6. **Nothing needs to be built. What needs to change is the ordering of
what runs, plus one cheap preflight the lane does not have.**

The missing preflight is the `rho = c` unit screen, which is strictly cheaper
than elimination (one fewer variable and no elimination order):

```text
ideal Ic = subst(I, t, c);   reduce(1, std(Ic));   // 0  =>  fibre empty at c
```

Semantics, stated exactly (this is where my blind card was loose and Fable's
staging was right): let `Z = V(J) ∩ D(a1)` and `pi` its projection to the
`rho`-line. `pi(Z)` is constructible, hence finite or cofinite. A single
**exact-`Q`** miss at a random rational `c` proves `c ∉ pi(Z)` and makes
"finite" (generic fibre empty) overwhelming; it is not proof. A **mod-`p`**
miss is weaker still (`(p x - 1)` is the unit ideal mod `p` and not over `Q`).
A *hit* at random `c` indicates a horizontal component but must be confirmed
at a second `c` or over `Q(t)`. Only `E' != 0` over exact `Q` is proof.

### 4.3 The policy

**Launch now, in parallel, all on the 17 rows (they are self-contained):**
1. exact-`Q` `rho = c` unit screen at two independent random rationals
   (minutes; strictly cheaper than the elimination already queued);
2. the toy negative control `J = (f - t x)` through the identical pipeline —
   must return "no eliminant" (mandatory; a pipeline that reports "closed"
   on the toy is broken);
3. the already-compiled `eliminate` phase, exact-`Q` (`p = 65521` lane as
   control), with the §2.4 fail-closed assertion added;
4. on `E' != 0`: the `lift` + homogenize phases, then an independent
   fixed-weight exact verification of `a1^D U(t) ∈ J'` reusing the V43 dual
   infrastructure as a *verifier*.

**Continue in background:** the 59-row escalation, prepared but not launched,
to fire only if 17 rows return `E' = 0`; the modular corroboration lanes;
independent review of anything positive.

**Hold:** the seeded `N=7` / weight-35 dual. Sized in my V43 review at
2,715,310 products (~9.5x weight-30's 284,766; weight-40 is ~77x and out of
reach for this architecture). Release the hold only if steps 1–3 exceed their
stop condition, and then explicitly as floor-raising with a rung budget.

**Stop:** the `rho = 0` tracked multiplier extraction and its 192-GiB /
larger-memory retries (`run_dehom_highmem_aws.sh`,
`run_dehom_x2highmem_aws.sh`). They compute an exponent that appears in no
step of the criterion. Keep at most one cheap `lift` on the smallest
sufficient subset **only** as the `m` input to the §3.3 Lemma-C certificate
compiler, and only after `E' != 0` has fired — i.e. demand-driven, not
speculative.

**Stop condition for the whole item:** if the exact `Q(t)` elimination has not
terminated in six hours **and** two independent exact-`Q` `c`-screens
disagree, stop, report the `c` evidence and the smallest failing identity,
and re-plan. Do not escalate to 59 rows before the 17-row run has an answer.

Expected wall clock to a decision: hours if the screens are informative,
versus a ladder of unknown length at ~9.5x per rung.

---

## 5. Item 5 — K00: global nonmembership, D8, local membership, and the
## first mixed deformation obstruction

### 5.1 The three facts are consistent, and together they close the ladder

Promoted: `r7 ∉ I := (r1,…,r6)` over `Q[C6,C6^{-1},d]` and at `C6=1`;
`r7 ∈ I + (d)^9` at `C6=1` (my own D8 review, PASS, independent re-emission
of the 2996x5544 map and exact ranks 2547 = 2547).

Provisional delta: `h*r7 = sum u_i r_i` with `h = 63*d4 + 20`, so `h(0) = 20`.

These are mutually consistent: `h` is a unit of `A = Q[d]_(d)` and a nonunit
of `Q[d]`. And they settle the ladder by an elementary argument that needs
neither Krull intersection nor faithful flatness: write `h = 20(1 + w)` with
`w ∈ m`; then `h^{-1} = (1/20)(1 - w + w^2 - …)` truncates exactly modulo
`m^n`, so `r7 ∈ I + m^n` **for every `n`**.

> **Consequence (conditional on V14R1 freezing).** No pure-coefficient
> filtered obstruction exists at any degree. D9, D10, … are guaranteed
> compatible and buy exactly zero bits. The phrase "first filtered
> obstruction degree" names an object that does not exist, and the promoted
> `>= 9` strengthening is retroactively non-informative rather than progress.

Three of the four blind reports independently proposed exactly this test
(Sol Card 1 `K00-COLON-CONSTANT`, Fable Card F2 `K00-COLON-LOCAL`, Opus
Card B `K00-COLON-ESCAPE`), all with the same criterion `(I : r7) ⊄ m`. Grok
reached the same *stop* by a different route (two non-informative degrees
force redesign). That is the strongest convergence in the round, and the
coordinator had already run it.

**Custody caveat, unchanged:** V14's `CUSTODY_GAP.md` is a genuine negative
finding (Singular's `write(filename, matrix)` serialized one row of the 6x6
lift matrix, so `COLON_LIFTS.txt` has 6 entries, not 36). V14 is not
promotable and V14R1's preregistration is the right repair. Nothing above may
be promoted until V14R1 is frozen, reported portably, and reviewed by a
different model. I use it only to set priorities.

### 5.2 The suggested syzygy quotient is well-defined but **trivial**

The natural-looking construction — take the class of the load-perturbation
residual in `A` modulo `I*A` and modulo the image of the syzygy module of
`(r1,…,r6,r7)` — is **vacuous**, and here is why.

Let the loads be first-order: `r_l ↦ r_l + eps*s_l`. A witness is a pair
`(h, u)` with `h*r7 = sum u_i r_i`, `h` a unit. Two witnesses differ by an
element of `Syz(r1,…,r6,r7)`, and under `(u,h) ↦ (u+a, h+b)` with
`sum a_i r_i = b*r7` the residual `omega(h,u) := h*s_7 - sum u_i s_i` changes
by `b*s_7 - sum a_i s_i`. But the known witness itself gives the syzygy
`(u, -h) ∈ Syz(r1,…,r7)`, whose image is `omega` **itself**. So `omega` is
always in the ambiguity subgroup and the class is identically zero. Quotienting
by `Syz(r1,…,r7)` destroys exactly the information one wants.

### 5.3 The correct object

Normalize `h = 1` (legitimate: `h` is a unit of `A`), so
`r7 = sum ũ_i r_i` with `ũ_i = u_i/h`, and the witness is unique **up to
`Syz(r1,…,r6)` only**.

> **Definition.** Let `L = span_Q{L_1,…,L_q}` be the first-order load
> directions (leading `Lambda^19`, `k10`, `k6`, `k2`, `mu`, `Jdet`), and
> expand `r_l(d, L) = r_l(d,0) + sum_j L_j s_{l,j}(d) + O(L^2)`. Define
>
> ```text
> sigma : Syz(r1,…,r6) -> A/I*A ,     a |-> sum_i a_i s_i  (mod I*A),
> Ob    : L -> coker(sigma) = A / ( I*A + sigma(Syz(r1,…,r6)) ),
> Ob(L_j) = [ h*s_(7,j) - sum_i u_i s_(i,j) ].
> ```

- **Well-defined**: changing `ũ` by `a ∈ Syz(r1,…,r6)` changes the class by
  `sigma(a)`, which is quotiented out. Koszul syzygies `r_j e_i - r_i e_j`
  map to `r_j s_i - r_i s_j ∈ I*A` and die automatically, so only
  `Syz/Koszul` — a small module — matters.
- **Linear** in the load direction, so it is a matrix, not a search.
- **`h`-free**: using the un-normalized form `h*s_7 - sum u_i s_i` avoids
  dividing by `h` entirely (`h` is a unit, so the class is unchanged).
- **Invariance scope, stated honestly**: `coker(sigma)` is intrinsic to the
  pair (unloaded presentation, deformation) and is unchanged by the choice of
  witness, by the choice of syzygy generators, by `GL`-changes of the row
  basis applied simultaneously to loaded and unloaded rows, and by the
  `C6 = 1` normalization. It is **not** invariant under adjoining a redundant
  generator with an arbitrary independent deformation — so the seven named
  honest rows must be pinned as the presentation. That is the exact
  representation-firewall the design needs, and it is weaker than
  "representation-invariant" tout court.

**Cheapest computation** (desk to small AWS, six variables plus loads):
1. `Syz(r1,…,r6)` in `Q[d0..d5]` — small.
2. `J_s := ideal{ sum a_i s_{i,j} : a ∈ generators of Syz, j = 1..q }`.
3. For each `j`: test `w_j := h*s_(7,j) - sum u_i s_(i,j) ∈ (I + J_s)` locally,
   i.e. `((I + J_s) : w_j) ⊄ m` — **the same colon instrument V14 already
   runs**, one call per load direction.

**Both outcomes.**
- Some `Ob(L_j) != 0`: the loaded target leaves the loaded ideal at first
  order in that direction. This is the **first load-aware K00 exclusion**, it
  names the responsible load, and it is obtained without any attainability
  computation. Exactly the outcome Grok's Card B wanted, by a much cheaper
  route.
- `Ob ≡ 0`: membership persists to first order; the germ survives; escalate
  to (a) the *full* loaded colon `r7 ∈ (r1,…,r6)` in
  `Q[d, L]_((d,L))` — one colon in `6 + q` variables, which is the decisive
  version — and only then to (b) representation-invariant attainability of
  `M6(0)` and the leading `M2,M4`, which remains the genuinely open piece.

**Scope firewall.** This decides deformation of a membership relation inside
the compiled K00 transverse chart at `C6 = 1`. It says nothing about
attainability of the loaded data from the owner source functor (Grok's
reachability firewall stands, unmodified), nothing about closure-first
incidence or `H_K00`, nothing about Taylor realization or algebraization,
nothing about the terminal receiver, order two, maximum twelve, `G2-PSC`,
`G2-BD`, Gate T, or JC2. It is also **conditional on V14R1**: with no unit
witness there is no `(h,u)` and the construction has no input.

---

## 6. Item 6 — the contact-side merger

### 6.1 Uniform shift naturality

Fable's hostile review is the round's most thorough executed verification:
independent coefficientwise rebuilds at eleven contacts through grade 38 over
exact `Q` and mod `p`, with every mutation firing at the algebraically
predicted grade. I did not re-execute it; I checked its two load-bearing
arguments by hand and both hold:

- The **repair** is correct and necessary. "Coefficient extraction commutes
  with a continuous `sigma`-adic homomorphism" is false in general (`x ↦ sigma*y`
  moves grades). What makes (1.5) true is that (1.3) is the coefficientwise
  extension of a **jet-reindexing map** `az_i ↦ A_{z,i-a}` etc. that fixes
  `sigma` and sends jet variables to scalar multiples of jet variables; such a
  map commutes with `[sigma^g]` trivially. Sol's §1 should carry the jet-map
  form, not "continuity". Grade: **`sound with scope correction`**.
- The **denominator census** (`{2^2,…,2^20,2^23}`, all powers of 2) upgrades
  the identity from "characteristic zero" to "any `Z[1/2]`-algebra", which is
  what licenses the odd-prime replays. That is a real strengthening.

**My blind §6.3 is corrected by Fable and I concede it.** I proposed a
two-sided finite-jet control: recompute (3.2) from raw `F_i` valuations as an
upper bound and require `max_f^raw >= max_f^licensed`. Fable's executed §6.3
shows (a) the direction is right — cancellation only raises valuation, so raw
over-retains and a *licensed* inventory is the only under-prediction risk —
but (b) **my remedy is vacuous for the family that matters most**: `F6 = 2P`
has valuation `0`, so a raw census retains every `ell_j` through `T` and
bounds nothing. The usable control is Fable's **single-jet tagging** (tag one
relative jet, ask whether any row through `T` depends on it), which is exact
in both directions and which Fable executed at two chambers. Adopt that;
drop my raw-valuation bound.

### 6.2 The direct three-row syzygy

I verified Sol's lemma exactly with an independent sparse-polynomial engine.
All four identities are **zero**:

```text
C1*g2 - C0c*g1 - (3/8)*A1*D                = 0
C0c*g2 - rho^2*C1*g1 + (3/8)*A0c*D         = 0
(32/3)*g4 + D - 2*rho^2*C1^2               = 0
(32/3)*g4 - D - 2*C0c^2                    = 0
```

and I independently re-derived `g1, g2` as the `z`- and `1`-coefficients of
`(3/4)*A0*C0 mod (z^2 - rho^2)` and `g4` as the symmetric coefficient of
`(3/8)*C0^2`, each matching to zero. The radical conclusion follows:
localizing at `A1` or at `A0c` puts `D` in the ideal by (1)/(2), then (3)/(4)
put `rho^2 C1^2` and `C0c^2` in it, and inverting `rho` gives
`C0c, C1 ∈ sqrt(I)`. Grade: **`sound`**, exactly at the stated scope
(radical/set-theoretic on `D(rho) ∩ (D(A0c) ∪ D(A1))`, not a scheme-theoretic
unit ideal).

The wall arithmetic of §3 also checks:
`RA^2/L^2` at `12+r+2a` reaches `T_C2 = 10+2c` iff `r <= 2d-2`;
`A^3/L^3` at `15+3a` reaches it iff `a <= 2d-5` (for `d=3`, `a <= 1`, i.e.
exactly the exceptional cell `E`); `k6 C/L` at `17+c` ties `G = 10+a+c` iff
`a = 7` and precedes for `a >= 8`; target walls are `G < 28` (i.e.
`a + c < 18`) and `T_C2 < 32` (i.e. `c < 11`).

### 6.3 Does my direct certificate for `(2,4,>=3)` generalize?

**Yes, to a precisely delimited sub-fan, and the delimitation is a theorem,
not a convenience.** `(2,4,>=3)` is `a=2, d=2`. The pole wall `r <= 2d-2 = 2`
is not reached at `r >= 3`, the pole-three wall needs `a <= -1`, the load wall
needs `a >= 7`, and both target walls are far away (`a+c = 6 < 18`,
`c = 4 < 11`). So the three-row pattern is literally available there, and the
same check licenses the twelve contacts Sol lists (`d=1: a=2..6`;
`d=2: a=2..6`; `d=3: a=5,6`) plus the sub-tails `(a,d)=(1,2)` at `r >= 3` and
`d=3, a=2,3,4` at `r >= 5`.

It does **not** generalize past any wall. In particular `(2,5,>=3)` (`d=3`)
has `2d-2 = 4`, so `r = 3,4` are genuinely outside the three-row pattern and
genuinely need the reviewed `B23` endpoint — which is exactly what V45
computes. The two instruments therefore partition the fan cleanly rather than
competing, and Sol's §2 statement of that partition is correct.

### 6.4 V45, and an unexpected triple corroboration

V45's exact producer output for `(a,c,r) = (2,5,>=3)`, `d=3`, `G=17`, `T=20`
gives mechanically derived relative jet depths

```text
p/A/C = 3,  R = 1,  k10 = 2,  k6 = 0,  k2 = 0.
```

The naturality interface's formula (3.3) predicts **the same vector** from
(3.2) alone. Fable's independent single-jet tagging measured **the same
vector** in/out at exactly those indices (`A[3] in / A[4] out; C[3]/C[4];
R[1]/R[2]; k10[2]/k10[3]; ell[3]/ell[4]; k6,k2 absent`). Three independent
derivations — a producer compiler, a closed-form inventory formula, and a
reviewer's empirical tagging — agree exactly. That materially de-risks the
"index/factor map" attack surface of V45 **before** its own review lands, and
it is a fact neither V45's report nor Fable's review states, because neither
had the other in view. I record it and promote nothing: V45's contact
exclusion remains provisional pending its own different-model review.

### 6.5 Can serial exporters leave the critical path?

**Mathematically yes; operationally not yet.** `[sigma^g] Phi_ell^tot` at
`g = 22, 24, …` is a *defined* polynomial the moment the schema exists;
an exporter reproduces bytes of it, which is layer-3 custody, not a proof
obligation. Fable's review confirms this as its central economic finding, and
Grok's Card C reaches it independently. But the retirement is gated on six
finite, desk-scale obligations (schema freeze with (1.1) normative; recorded
compiler-agreement lemmas; per-manifest primitive comparison; **generated**
renaming maps; the frozen V0–V4 verifier with one hostile review; the
`(8,3)` narrow promotion or an explicit conditional label). Two traps must be
carried into the verifier, both byte-verified by Fable: the `k2c` (a total
`k10` jet) vs `k2load` (the D1 `k2` load) collision, invisible in all seven
rows through grade 16; and the `a8d3` file whose name says "promotion" but
whose status line is "PROMOTED ROUTE FALSIFICATION ONLY" — endpoint status
must bind to the promotion artifact's **hash**, never to a filename pattern.

**Keep the local strict unique-`AC` exclusions firewalled from coverage and
from JC2.** Eleven endpoint families with mixed theorem types transported by
one identity are eleven implications, not one theorem; nothing here touches
`rho = 0`, equality faces, positive-order leading loads, `k = 0`, the six
staged Rees charts, the receiver, `G2-PSC`, `G2-BD`, Gate T, order two,
maximum twelve, or JC2. Grok's §3 statement that unique-`AC` on `D(rho)` is
*disjoint* from the `rho = 0` chain (it needs `lambda_0 = eps*rho != 0`), my
blind §6.3 note that the interface is orthogonal to the two `rho = 0`
obligations, and Fable's non-claims list all say the same thing from three
directions.

---

## 7. Item 7 — cross-connections the blind reports missed, and the Jelonek
## audit

### 7.1 History checksum first

Run against the packet's own "what is not new" lists, the 0635Z synthesis
pins, and the 2026-08-26 websweep §3. **Already known, not re-proposed here:**
section-first honest-equation calculus; K00 split `D(rho)/V(rho)`;
dual-as-primal rewrite; generic `L43` receiver; first-surviving-row calculus;
"export more of this tail to kill CS0/Z00"; graded counterexample hunting
(closed by Shaska); stage-zero Kummer composition (refuted); and — this one
is a direct hit on my own blind §4.2 — the websweep's standing instruction
"**do not infer component purity from mere deformation or specialization**".
My blind report presented the refutation of that bridge as a contribution; it
was already policy. Novelty credit: zero.

### 7.2 The Jelonek/component-degree proposal — audited, largely withdrawn

I have not read arXiv:2607.20597; I have only the sweep's summary, which also
says the paper "supplies no irreducibility or component theorem that decides
the plane case". Everything below is conditional on that summary.

**What was sound.** `A_D` closed in `K_D` makes `K_D \ A_D` open, hence dense
in every irreducible component it meets. So a hypothetical degree-`<= D`
counterexample is a *generic* point of its component. That topology is
correct.

**What was wrong, and I withdraw it.**

1. *The proposed cheap test is vacuous.* I suggested testing "every component
   of `K_D` containing an automorphism consists generically of automorphisms"
   at small `D` where `K_D` is computable. But at every `D` in the computable
   range JC2 is known, so `K_D = A_D` set-theoretically and the prediction is
   content-free. The test cannot be run anywhere it could be informative.
2. *The avenue-36 "raise" does not follow.* The recorded objection is that
   counterexamples are thin **in the ambient parameter space of degree-`<= D`
   pairs**, which is where sampling happens. Jelonek's closedness says they
   are not thin **inside `K_D`**. Those are different statements, and only the
   first is the search objection. **I withdraw the `raise` on avenue 36.**
   My own sentence "we cannot sample from a component of `K_D` — the Keller
   condition itself is the hard variety" already contained the refutation; I
   should have followed it.

**What replaces both, and is new and correct.**

> **Proposition (Jelonek-scope).** Let `K_D` be the constant-Jacobian locus of
> plane pairs of degree `<= D` normalized by `F(0) = 0`, with the `G_m`-action
> `F_t(x) = t^{-1} F(t x)`. Then (i) the action preserves `K_D`
> (`Jac(F_t)(x) = Jac(F)(tx)`, still constant, degree preserved); (ii)
> `lim_{t -> 0} F_t = L`, the linear part, which is invertible because
> `Jac(F)(0) != 0`, hence `L ∈ A_D`; (iii) `G_m` is connected, so it fixes
> every irreducible component setwise, and each component being closed
> contains the limit. Therefore **`A_D` meets every irreducible component of
> `K_D`.** Consequently, if `A_D` is Zariski closed, then
>
> ```text
> A_D is a union of irreducible components of K_D
>   <=>  A_D = K_D  <=>  JC2 holds in degree <= D.
> ```

Two uses, both immediate and both free:

- **A citation firewall.** Any reading of a "component dichotomy" as
  *component purity* is logically equivalent to bounded-degree JC2 and can
  therefore never be an input to it. This forbids a whole family of tempting
  arguments in advance, which is worth more than the arguments would have
  been. It also explains *why* my §4.2 bridge had to fail — not merely
  "avenue 41 refutes it", but "it would have proved bounded-degree JC2".
- **Row 41's exact role.** The dimension-three counterexample and its linear
  limit sit in one `G_m`-orbit closure; that is the concrete witness that
  `A_D ∩ C` can be a proper closed subset of a component. Row 41 should be
  retrievable as this lemma, which is why I marked it `reopen (lemma-only)`.

Net disposition change I now recommend against my blind vector: **avenue 36
`raise` → withdraw (unchanged); avenue 7 `raise` → keep, but with no
executable descendant this round and no capacity move.** Avenue 18's
`reopen (structural input only)` survives, since the `G_m`-limit lemma is
exactly the structural input it names.

### 7.3 Comparison with Fable's, Sol's and Grok's cross-avenue ideas

- **Fable's AS109 `n=6` face isolation (rows 12 x 19).** The strongest
  counterexample-side proposal in the round, and it correctly identifies why
  row 12's historical stuck-point ("no integer `m` to send to infinity") does
  not apply: the 109-adic valuation level supplies the arithmetic parameter.
  I do not adjudicate the band algebra. Grade: **`sound` as a design**; the
  cost claim (desk-scale two-band extraction) is credible and the stop rule
  (two bands, no descent) is the right one. This should be the funded
  counterexample lane.
- **Fable's row 16 b-function raise.** Genuinely the first *named* invariant
  the row has ever had, which is the row's recorded defect. But the object is
  under-specified: "the b-function of the pencil at its atypical values"
  requires choosing a hypersurface and, for behaviour at infinity, a
  compactification — which is precisely avenue 27/28's unsolved problem. So
  the risk is not (only) Fable's stated one (the invariant may be trivial for
  all `J = 1` pairs) but circularity. Grade: **`sound with scope correction`**;
  fund the one-afternoon `dmod.lib` test only with the hypersurface pinned in
  advance, and treat a trivial answer as the row's final answer.
- **Fable's row 26 primitive-group raise.** Correct and, more importantly,
  *resource-orthogonal* (a GAP/Magma database run consumes no AWS algebra
  quota). Grade: **`sound`**. This is the right kind of anti-collapse filler.
- **Fable's row 9 tooling transfer** (V43's fixed-weight dual compiler is a
  general exact nonmembership engine for weighted-homogeneous targets, and
  row 9's smallest-cap rows are fixed-degree membership questions of that
  shape). Grade: **`sound`**, near-zero marginal cost, correctly queued as
  idle-capacity work. This is the single cheapest unexploited item in the
  round.
- **Grok's transport firewall** ("duals push only along specializations that
  keep the test monomial alive"; V43 does not bound a K00 obstruction degree;
  D8 does not lift an `a1^N U(t)` identity; unique-`AC` functoriality does not
  supply shifted roots at `rho = 0`). Grade: **`sound`**, and this is Grok's
  strongest contribution — a negative dictionary that prevents three specific
  laundering errors the round's density invites.
- **Sol's "two ladders are one persistence problem"**, Fable's §3.4
  "local/global membership is the unifying pattern", Grok's §3
  "associated-graded, deformation, and realization pieces of one DVR module",
  and my §0.1 "three lanes share one ladder pathology" are four independent
  statements of the same observation. It is therefore established and
  unowned; nobody should claim it.

### 7.4 The cross-connection I think all four reports missed

**The naturality functor and the total-`T-a1` chart share a variable-naming
hazard that is currently guarded on only one side.** Fable's byte reads
establish that the total ring's third `k10` jet is literally named `k2c`
while the D1 rings name the `k2` load `k2load`, and that this collision is
invisible in all seven rows through grade 16 and first visible at grade 18/20.
Independently, `k2c` is one of the 65 positive-weight variables in the
ordered-`T-a1` alphabet (weight 6, confirmed in my V43 review §1.2), and it
appears in the frozen rows the eliminant lane consumes. So the *same* symbol
carries two meanings across two live critical-path lanes, and only the
contact side has a mutation control for it. Cheap fix, no computation: the
V43/V37 alphabet census and the naturality schema should be required to emit
a **shared alias table** whose hash both lanes pin, with `k2c` flagged. This
costs a hash and closes a defect class the campaign has already been bitten
by twice (`a5`/`a6` omitted jets; the V44 over-strong guard).

---

## 8. Claim matrix

`S` = sound · `SC` = sound with scope correction · `U` = unsupported ·
`W` = wrong.

### Sol

| # | Claim | Verdict | Note |
|---|---|---|---|
| S1 | Raises on avenues 2, 31, 32 | S | navigation, well-reasoned |
| S2 | "find the minimal exponent or a direct eliminant" | SC | the exponent is not part of the criterion (§1.3); only the eliminant decides |
| S3 | Card 1: `r7 ∈ I_m ⟺ (I:r7) ⊄ m` | S | correct; already executed by V14/V14R1 |
| S4 | Card 2: seed `Lambda_7(a1 m) = Lambda_6(m)` | SC | consistent and it satisfies the `a1`-divisible sub-block for free; but it restricts to a proper affine subspace, so **failure proves nothing** and unrestricted replay is mandatory (converges with Grok §7.4 and Fable §8.1) |
| S5 | Card 3 AS109 gauge conductor | S | not adjudicated here; hedging ("strong evidence toward") is correct |
| S6 | "the two ladders are one persistence problem" | SC | observation sound; the *engineering* conclusion (accelerate both) is wrong for K00, where the ladder should stop, not speed up |
| S7 | Allocation 35% `T-a1` / 25% K00 / … | SC | K00's unloaded share should go to zero (§5.1); the freed capacity is not needed by `T-a1`, which is now one run |
| S8 | Certificate-tree identities (`clear_power`, `combine_branches`) | S | all three re-derived and matched termwise against the code (§3.1) |
| S9 | Naturality (1.5) formal-series identity | SC | true; the proof sentence ("continuity") is false as written — the jet-reindexing reading is what makes it work |
| S10 | Three-row syzygies (1.2)/(1.3) | S | all four identities verified exactly here, plus the derivation of `g1,g2,g4` |
| S11 | §3 pole/load/target walls | S | arithmetic re-derived and matches |
| S12 | "can potentially replace twelve endpoint proofs" | SC | replaces the *emptiness argument* on those twelve after inventory + linker + review; does not replace lifecycle, coverage, or the walls' complement |

### Fable

| # | Claim | Verdict | Note |
|---|---|---|---|
| F1 | §3.1 two-fibre eliminant reduction | S | re-proved independently here; identical to my Theorem A |
| F2 | Certificate converter "rehomogenizes directly" | SC | needs the mod-`wt(a1)` residue projection (§1.6); the existing homogenizer already implements it |
| F3 | Special-fibre half already computed; subset sound for the unit conclusion | S | strengthened here: the unit-GB lane uses the *identical* 17-row `SELECTED` tuple |
| F4 | Selected-row eliminations are one-sided | S | sharpened: the correct positive predicate is `E' != 0`, weaker than "nonzero constant term" — though under control (S) they coincide |
| F5 | §3.2 K00 colon + faithful flatness + Krull | S | correct; a shorter route (geometric-series inversion of `h`) avoids both theorems |
| F6 | §3.3 origin funnel: survivors pass through the terminal origin | SC | correct as stated under its hypothesis `P ∩ Q[rho] ⊆ (rho)` (horizontal components need the closure step, since `{X=0} x cl(pi(C)) ⊆ C`); but identifying that chart's origin with `Z00`/K00 needs the chart-comparison map the campaign lacks — so the *composition* conclusion is suggestive, not established |
| F7 | §3.4 local/global membership as the unifying pattern | S | independently reached by all four |
| F8 | Row 16 b-function raise | SC | first named invariant for the row; under-specified hypersurface/compactification (§7.3) |
| F9 | Row 26 raise, resource-orthogonal | S | |
| F10 | Row 12 reopen for the AS109 `n=6` corner | S | as a design |
| F11 | Seeded `N=7` is fail-open across weights | S | converges with Grok §7.4 |
| F12 | "the per-`N` ladder is constitutionally incapable of a verdict" | SC | it *can* settle `a1^N ∈ J0`; what it cannot settle, in either direction, is `K+(rho)=(1)` |
| F13 | Naturality review verdict CONFIRMED + two repairables | S | the jet-map repair is the correct fix; I did not re-execute the numerics |
| F14 | §6.3 raw over-retains; raw bound vacuous for `P`-jets | S | **this corrects my blind §6.3**; adopt single-jet tagging instead |

### Grok

| # | Claim | Verdict | Note |
|---|---|---|---|
| G1 | Sandwich `7 <= N_J0 <= N_17` | SC | the custody worry is resolved (both lanes select the same 17 names from the same frozen 70-row corpus, with census assertions), but the sandwich is not decision-relevant under Theorem A |
| G2 | Reduced `rho=0` fibre lands in the terminal locus | SC | `a1 = 0` on it is sound; the identification with K00/terminal needs the missing chart map |
| G3 | Nesting `K00_0 ⊂ {reduced T-a1 fibre} ⊂ {ramified total fibre}` | U | these are subsets of different schemes until the comparison maps exist; no map is exhibited |
| G4 | Transport firewall (duals push only along specializations keeping the test monomial alive) | S | Grok's strongest item; prevents three concrete laundering errors |
| G5 | Card A probe: "specialize all non-`a1` variables; specialized nonmembership raises the floor" | **W** | see §8.1 below — provably cannot beat floor 3, i.e. strictly weaker than the floor already held |
| G6 | §7 adversarial audit points 1,4,6,8,9 | S | especially #6 (grade `>19` rows have weight `>19` and *can* contribute at weight 35, so a frozen `N=7` dual is a frozen-chart theorem, not all-depth) |
| G7 | §7 point 3 ("inhomogeneous slices can lie") | SC | the concern is real in general, but here the ideal is weighted-homogeneous with `w(a1) = 5 > 0`, so the dehomogenized slice is faithful and the residue-class rehomogenization is valid |
| G8 | Card C unique-`AC` linker freeze | S | converges with Fable's review and Sol's design |
| G9 | "two non-informative filtered degrees force redesign" | S | strengthened: under local membership *every* degree is non-informative |

#### 8.1 Why Grok's specialization probe is wrong

The probe specializes every variable except `a1` to random field values and
tests `a1^N` in the resulting ideal of the univariate ring.

- The **principle** is sound *and can be made rigorous by running it over `Q`
  instead of `F_p`*: for any rational point `psi`, `a1^N ∈ J0` implies
  `psi(a1^N) = a1^N ∈ (psi g_1, …, psi g_51)` because the cofactors are
  polynomials. (Over `F_p` this needs a good prime for the *unknown*
  certificate, which the report does not name — so as written the probe is a
  Monte-Carlo screen, not a floor.)
- The **information content is provably nil.** The specialized ideal in
  `Q[a1]` is `(d)` with `d = gcd_i psi(g_i)`, and
  `ord_{a1}(d) = min_i ord_{a1}(psi(g_i))`. Every frozen row is
  `sigma`-homogeneous of weight `<= 19` and `w(a1) = 5`, so `a1^j | g_i`
  forces `5j <= 19`, i.e. `ord_{a1}(g_i) <= 3`. At a random point no
  cancellation raises this. Hence the best floor the probe can ever return is
  `N_J0 >= 3` — **strictly weaker than the floor 6 already held by V43 plus
  the ideal property.** The generic outcome is `d = 1`, i.e. the unit ideal,
  i.e. no floor at all.
- Grok's own fail-closed branch ("probe hits the cap with all specialized
  `a1^N` still nonzero ⟹ custody contradiction with the 17-row unit") is
  therefore mis-specified: that branch cannot occur for `N > 3` for structural
  reasons, and its non-occurrence tests nothing.

The salvageable residue: full-variable specialization over `Q` is a legitimate
*negative control* (`a1^6` must still be excluded on any specialization where
it is excludable), and it is essentially free. It is not a floor-raiser.

### Opus (self — audited hardest, as instructed)

| # | Claim | Verdict | Note |
|---|---|---|---|
| O1 | Theorem A | S | but my blind proof of (A2) used irreducible components over `Qbar`; **superseded** by Lemma C, which is unconditional, effective, and needs no homogeneity |
| O2 | §6.2 "concrete fail-open defect" in the eliminant lane | **W (withdrawn)** | the conflated case is unreachable under the control the same script enforces first (§2.3); what survives is a *defensive* patch, not a correction |
| O3 | §6.2 "and it passes today" | **U (withdrawn)** | no harvested run of that script exists; the fact is established by the sibling cascade-dehom lane on the identical 17 rows |
| O4 | §4.1 Jelonek: CE locus not thin; falsifiable small-`D` test | **W** | the test is vacuous (`K_D = A_D` throughout the computable range) and "not thin" holds only relative to `K_D`, not to the ambient sampling space; **avenue-36 `raise` withdrawn** |
| O5 | §4.2 self-refuted `G_m`-purity bridge | S | but the refutation was already campaign policy (websweep §3); novelty zero. Replaced by the §7.2 Proposition, which gives the *reason* |
| O6 | §3.1 Escape Lemma / ladder hygiene | S | textbook, and independently produced by Sol, Fable and Grok in the same round; no unique credit |
| O7 | §6.3 two-sided finite-jet control | SC | direction right, remedy vacuous for the `P`-jets (Fable §6.3); adopt single-jet tagging |
| O8 | Card A self-contained on the 17 rows; does not consume V42 | S | now confirmed from source: both lanes use the identical `SELECTED` tuple |
| O9 | V43 review §7.3 (`a1^i ∉ J0` for `i <= 6` by the ideal property alone; V42's `a1^8` is in the branch ideal `I_A1`, not `J0`) | S | two blind reports still read V42 the other way; the correction stands |
| O10 | "the 192-GiB multiplier extraction is not needed" | S | now precisely sourced: it is the `lift` phase of `compile_cascade_dehom_v43.py`, computing an exponent the criterion does not contain |
| O11 | §6.3 naturality interface is orthogonal to the `rho=0` obligations | S | independently confirmed by Grok §3 and by Fable's non-claims |

---

## 9. Strongest unique contribution per model, after deduplication

**Sol.** The **constructive certificate tree** (`clear_power`,
`combine_branches`) — the only frozen, hash-pinned engine in the campaign
that turns case-split radical reasoning into an ordinary ideal-membership
identity with tracked cofactors. Nobody else built an *executable* object
this round. Its target was wrong; the engine is right, and §3.3 gives it the
job it should have. Runner-up: the three-row syzygy lemma, which is the only
new *theorem* about the contact side in the round.

**Fable.** The **executed hostile verification of the naturality interface** —
eleven contacts, exact `Q` and mod `p`, through grade 38, with every mutation
firing at the predicted grade, plus the jet-reindexing repair, the
`Z[1/2]`-denominator census, and the `k2c`-invisibility and
filename-vs-hash traps. This is the largest correctness-adjusted contribution
in the round by any model. Runner-up (blind side): the **origin funnel**
(§3.3), the only genuinely new *structural* cross-connection anyone proposed,
even after my scope correction.

**Grok.** The **transport firewall**: a negative dictionary saying precisely
which of this round's three new objects may be pushed along which map, and
why (duals survive only along specializations that keep the test monomial
alive). It is the item most likely to prevent an expensive error, and it is
the one thing no other report contains. Its Card A probe is wrong (§8.1),
but its §7 self-attack is the most rigorous adversarial section any producer
wrote about their own card.

**Opus.** **Lemma C plus its identification with `clear_power`** — the
effective, hypothesis-minimal form of the two-fibre theorem, which upgrades
the criterion from an existence statement to a *compiler*: generic-fibre
certificate + special-fibre certificate → the literal `a1^(M+em) U(rho^2) ∈ J`
object, with the exponent displayed, using an engine that already exists.
Runner-up: the §8.1 refutation of the specialization probe and the §7.2
Jelonek-scope Proposition, both of which are pure loss-prevention.

### Independent convergences that increase confidence

1. **Two-fibre criterion:** Fable §3.1 and Opus Theorem A, derived blind and
   independently, with different proofs (prime-spectrum analysis vs.
   weight-zero projection + component argument), reaching the same
   equivalences and the same operational conclusion. I have now re-proved it
   a third way (Lemma C). Confidence: high.
2. **K00 colon escape:** Sol Card 1, Fable Card F2, Opus Card B — same
   criterion `(I:r7) ⊄ m`, blind, and independently already executed by the
   coordinator as V14. Grok reached the same *stop* from a different premise.
   Confidence: very high.
3. **The exponent ladder is off the critical path:** Fable §3.1/§7, Opus
   §3.4/§9, and — from the opposite direction — Grok's insistence that a
   special-fibre exponent is not the total certificate. Three of four.
4. **Unique-`AC` on `D(rho)` is disjoint from the `rho=0` obligations:**
   Grok §3, Opus §6.3, Fable's non-claims list. Three of four.
5. **`(2,5,>=3)` jet depths `p/A/C=3, R=1, k10=2, k6=0, k2=0`:** V45's
   producer compiler, the interface's closed-form (3.2)/(3.3), and Fable's
   empirical single-jet tagging. Three independent methods (§6.4).
6. **Seeded duals are fail-open:** Grok §7.4, Fable §8.1, and the packet's own
   unrestricted-replay requirement. Consistent and mandatory.

---

## 10. Four merged executable idea cards

### M1 — `TA1-DECIDE` (merge: Opus Card A + Fable Card F1 + Sol's direct-eliminant lane + Sol's certificate tree as extractor)

- **Target.** Decide `K + (rho) = (1)` for the frozen grade-through-19
  ordered-`a1` total chart, in both directions, by Theorem A(A4).
- **Dependencies.** Theorem A (§1.3, re-proved here from first principles);
  the promoted criterion `e3d263d5…` / `98003865…` / erratum `d322d417…`;
  the 17-row `rho=0,a1=1` unit GB from `compile_cascade_dehom_v43.py`
  (identical `SELECTED` tuple). Does **not** depend on V43's `N=6`, on V38,
  or on V42.
- **Cheapest discriminator.** Exact-`Q` `rho = c` unit screen at two random
  rationals on the 17 dehomogenized rows (minutes), *plus* the toy control
  `J = (f - t x)` through the identical pipeline (seconds, mandatory).
  Then the already-compiled `eliminate` phase with the §2.4 fail-closed
  assertion.
- **Both outcomes.** `E' != 0` ⟹ **the chart closes**; run `lift` +
  homogenize, then compose with the special-fibre certificate via Lemma C /
  `clear_power` to display `a1^(M+em) U(rho^2) ∈ J`, `U(0)=1`; cancel N=7,
  the DVR syzygy, and every multiplier-extraction retry. `E' = 0` ⟹ no
  information; escalate to the 59 rows, where `E = 0` **kills the entire
  total-`T-a1` certificate programme in one step** and hands back an explicit
  horizontal survivor to parametrize.
- **AWS/desk class.** Screens and controls: desk. Elimination and lift: one
  AWS box, exact `Q`, `p = 65521` as control. No 1-TiB machine.
- **Stop rule.** Six hours on exact `Q(t)` **and** disagreement between two
  exact-`Q` `c`-screens ⟹ stop, report the `c` evidence and the smallest
  failing identity. Do not escalate to 59 rows before the 17-row answer.
- **Scope firewall.** Even a positive closes one frozen chart. Nothing about
  the terminal receiver, source/landing coverage, the ramified `rho=0` fibre,
  the six Rees charts, `G2-PSC`, `G2-BD`, Gate T, order two, maximum twelve,
  or JC2. A negative is prefix-relative: later rows may still empty the chart.

### M2 — `K00-LOAD-OBSTRUCTION` (merge: Opus §5.3 + Grok Card B attainability + Sol Card 1 / Fable Card F2 instrument)

- **Target.** Decide whether the (conditionally established) unloaded local
  membership survives the loads, and if not, name the load that breaks it.
- **Dependencies.** V14R1 frozen with a portable report and a different-model
  review — **hard gate**; the frozen unloaded tails and `C6=1` chart (reviewed
  V8/V9/V10); the load-normal stencil as *input only*.
- **Cheapest discriminator.** The first-order screen of §5.3: compute
  `Syz(r1,…,r6)`, form `J_s`, and test `h*s_(7,j) - sum u_i s_(i,j) ∈ (I+J_s)`
  locally, one colon per load direction — the same instrument V14 already
  runs, in six variables. Desk to small AWS.
- **Both outcomes.** Some `Ob(L_j) != 0` ⟹ **first load-aware K00 exclusion**,
  with the responsible load named, without any attainability computation.
  `Ob ≡ 0` ⟹ escalate to the decisive full loaded colon in `Q[d,L]_((d,L))`,
  and only then to representation-invariant attainability of `M6(0)` and the
  leading `M2, M4`.
- **AWS/desk class.** Desk for `Syz` and the screen; one small AWS box for the
  loaded colon.
- **Stop rule.** One screen wave plus one loaded colon. Do **not** fund D9 or
  any further unloaded filtered degree in any branch: under local membership
  every rung is a theorem, not evidence.
- **Scope firewall.** Deformation of a membership relation inside the compiled
  chart. Not attainability from the owner functor (Grok's reachability
  firewall stands), not closure-first incidence, not Taylor realization, not
  the receiver, not JC2.

### M3 — `UAC-FREEZE` (merge: Sol naturality interface + Sol three-row syzygy + Grok Card C + Fable's V0–V4 verifier)

- **Target.** Remove serial `ACT-TOT-G22/G24/…` exporters from the critical
  path, and replace twelve contact-specific endpoint proofs by one verified
  lemma plus an inventory check.
- **Dependencies.** Fable's CONFIRMED naturality review (with its two
  repairs written in); the three-row lemma (verified exactly here); the eleven
  reviewed D1 endpoints; the `(a,d)=(8,3)` narrow promotion **or** an explicit
  conditional label on the union.
- **Cheapest discriminator.** Freeze the schema with (1.1) normative (not the
  `sigma^13` emitter hash), then implement and hostile-review Fable's V0–V4
  verifier — measured at ~15 s of pure Python for the core. Add: **generated**
  (never hand-written) renaming maps; endpoint status bound to promotion
  **hashes**, never filenames; the shared `k2c` alias table of §7.4;
  single-jet tagging in place of raw-valuation bounds (§6.1).
- **Both outcomes.** Verifier passes with all mutations firing ⟹ serial
  exporters leave the critical path; remaining unique-`AC` work is endpoint
  manifests plus background chamber review. Verifier fails at a chamber ⟹
  that chamber's displayed ceiling is costume and the linker is restricted —
  the same error class as the stage-zero Kummer composition, caught before an
  AWS grade.
- **AWS/desk class.** Entirely desk. `ACT-TOT-G20`/V44R3 stays banked as
  defense in depth; no new grade is emitted.
- **Stop rule.** Two chambers plus the full mutation set, or one review
  reversal.
- **Scope firewall.** Strict unique-`AC` on `D(rho)` only. Not the ramified
  fibre, equality faces, positive-order loads, `k=0`, the six Rees charts, the
  receiver, either `G2` obligation, Gate T, order two, maximum twelve, or JC2.
  Eleven implications with mixed theorem types, not one theorem.

### M4 — `AS109-N6-CORNER` (merge: Fable Card F3 + Sol Card 3)

- **Target.** Construct or exclude at the constrained `n=6` corner
  (`deg_y Q = 6`, `6 | deg_x q_6`, `deg_y P >= 12`, `3 | deg_y P`).
- **Dependencies.** The promoted floor-six composition; reviewed residue-ball
  Hensel noninjectivity. No provisional inputs.
- **Cheapest discriminator.** Fable's top-two `y`-degree band extraction with
  109-adic Kummer-carry bookkeeping (desk); Sol's linearized gauge quotient at
  W2/W3 as the second, independent read on the same corner.
- **Both outcomes.** A new face congruence ⟹ the floor rises or the corner's
  support shrinks. No constraint after two bands ⟹ the surviving leading-form
  data is banked as an exact seed and the null result is recorded so nobody
  pays twice.
- **AWS/desk class.** Desk; AWS only if a candidate congruence needs an
  exhaustive residue check.
- **Stop rule.** Two bands, no descent to lower bands without a fresh
  mechanism.
- **Scope firewall.** Counterexample-side only. No lift is claimed; degrees
  2–5 and prime targets stay history-closed; `(8,12)` and `(9,12)` are not
  addressed.

---

## 11. Decisions

**Launch now** (all nonblocking, none waits on a review):
- M1 steps 1–3: exact-`Q` `rho = c` screens ×2, the mandatory toy control,
  and the already-compiled 17-row `eliminate` phase with the §2.4 assertion.
- M4's first band extraction (desk, orthogonal, keeps the counterexample side
  funded per the packet's anti-collapse instruction).
- The §7.4 shared alias table (a hash, no computation).
- Fable's row-9 tooling retarget and row-26 primitive-group database run —
  both consume zero AWS algebra quota and zero critical-path reasoning.

**Continue in background:**
- Independent review of V45 (live), of the naturality interface's remaining
  layer-2 obligations, and of V14R1 once frozen.
- `(2,3,>=2)` and `(2,4,>=3)` hostile reviews; `(2,5,>=3)` V44R1/V44R3 as a
  chamber endpoint, not a template.
- TD6 H19R2 to its existing caps; D1 remaining timing chambers.
- The 59-row escalation of M1, prepared but fired only on `E' = 0`.
- The web-sweep clock (`2026-08-28T00:00Z`), unchanged. Add one item: pull the
  Jelonek statement in full and check §7.2's Proposition against the paper's
  actual dichotomy before any capacity moves on rows 7/36.

**Hold:**
- The seeded `N=7` / weight-35 dual. Release only if M1 breaches its stop
  condition, and then explicitly as floor-raising with a rung budget.
- M2 in its entirety, until V14R1 is frozen, reported portably, and reviewed.
  Without a unit witness the construction has no input.
- Descendants of V45 and of the naturality interface until their reviews land.

**Merge:**
- Opus Card A + Fable Card F1 + Sol's eliminant lane → **M1**, with Sol's
  certificate tree retargeted (§3.3) as its positive-branch extractor.
- Sol Card 1 + Fable Card F2 + Opus Card B → already executed as V14; the
  successor is **M2**, not a fourth colon.
- Sol naturality + Sol three-row + Grok Card C + Fable's verifier → **M3**.
- Fable Card F3 + Sol Card 3 → **M4**.

**Stop:**
- The unloaded K00 `(d)`-adic ladder, at D8, permanently. Conditional on
  V14R1, D9 and beyond are guaranteed compatible and buy zero bits. Do not run
  D9 even "as a capped control".
- The `rho=0` tracked multiplier extraction and its 192-GiB / larger-memory
  retries. Retain one cheap `lift` on the smallest sufficient subset, fired
  only on demand as Lemma C's `m` input.
- The K00 local-order `G = I*T` transform repair (V11/V13). The colon answers
  the question; the transform is not needed.
- Grok's full-variable specialization probe as a floor-raiser (§8.1). Keep it
  only as a free negative control, run over `Q`.
- My own avenue-36 `raise` and the proposed small-`D` Jelonek test (§7.2).
- Serial `ACT-TOT-G22/G24/…` as critical path, on the M3 gate.

---

## 12. Candid verdict: did Opus deliver unique capability beyond Fable this
## round?

Measured as correctness-adjusted information gain — items that are correct,
not duplicated, and that change a decision — and separated by phase, because
the answer differs.

**Blind phase: roughly neutral, arguably slightly negative.**

| Item | Opus | Fable | Unique to Opus? |
|---|---|---|---|
| Two-fibre criterion | Theorem A | §3.1, same content | no (independent, mutually confirming) |
| Operational staging of the decisive run | one card, one discriminator | four-stage screen ladder with certificate converter | **no — Fable's is better** |
| `E' != 0` is the right predicate (weaker than unit) | yes | states one-sidedness, not the weakening | **yes, small** |
| Card self-contained on 17 rows, independent of V42 | yes | notes independence of V43 | **yes, small** |
| Mandatory toy negative control | yes | positive/negative controls, not the toy | **yes, small** |
| K00 colon | Card B | Card F2 | no (also Sol; also already run) |
| Ladder-hygiene framing | §3.1 + Card C | §3.4 | no (all four) |
| Claimed code defect (§6.2) | asserted | — | **yes, and wrong** — negative gain |
| Jelonek reading | raise 7 + raise 36 + test | conditional trigger only, no raise | **yes, and the actionable parts are wrong** — negative gain |
| Origin funnel (survivors ⟹ terminal origin) | — | §3.3 | **unique to Fable** |
| `k2c`/filename/`Z[1/2]` traps, executed | — | naturality review | **unique to Fable** |

Two duplicated headline items, two small correct refinements, two incorrect
claims, against one unique correct structural connection and one very large
executed verification from Fable. On a strict ledger, Fable won the blind
phase.

**Cross-review phase: clearly positive, and this is where the retention is
justified.** Five results here are unique, correct, and decision-changing:

1. **Lemma C** — the effective, hypothesis-free form of the criterion, with
   the exponent `M + e*m`, replacing a component argument over `Qbar`; and its
   identification with Sol's frozen `clear_power`, which converts the theorem
   into a runnable certificate compiler.
2. **§8.1** — the proof that Grok's specialization probe can never beat floor
   3 and is therefore strictly weaker than the floor already held. This
   removes a proposed lane before it costs anything.
3. **§5.2/§5.3** — the demonstration that the natural syzygy quotient is
   identically zero, and the corrected obstruction
   `Ob : L -> coker(sigma: Syz(r1..r6) -> A/I A)`, with its exact invariance
   scope.
4. **§7.2 Proposition** — `A_D` meets every component, hence component purity
   ⟺ bounded-degree JC2: a citation firewall that also withdraws two of my own
   blind claims.
5. **§2.3** — the harshest item, against myself: the withdrawal of my own
   asserted code defect, with the torsion counterexample showing exactly when
   the concern *is* real and why it is unreachable here, plus the patch that
   turns the redundancy into a free consistency check.

Add three smaller ones: the mod-5 residue-projection requirement in the
certificate converter and the confirmation that the homogenizer implements it
(§1.6); the triple corroboration of V45's jet-depth vector (§6.4); the shared
`k2c` alias hazard across two critical-path lanes (§7.4).

**Verdict.** Opus's distinctive value this round was **adversarial and
verificational, not generative**. On blind whole-portfolio ideation Fable was
at least as good and produced the one genuinely new structural connection.
On hostile audit — of the other three models, of the campaign's code, and
most of all of Opus's own submission — Opus produced results no other report
contains, three of which stop or redirect a proposed lane. That is a real
capability, it is not duplicated by Fable this round, and it is the basis on
which continued retention is defensible. It is not a claim that Opus is the
better ideator.

---

## 13. Non-claims

Nothing in this report proves or disproves JC2, Gate T, order two, maximum
twelve, `G2-PSC`, `G2-BD`, source/landing coverage, the terminal or Taylor
receiver, the ramified `rho=0` deck/square fibre, any cofinal degree or `td`
bound, any AS109 lift, or any counterexample. No result is promoted, no
lifecycle label is changed, and no provisional artifact (V45, V14R1, the
naturality interface, the three-row lemma) is elevated. Theorem A and Lemma C
are statements about a frozen grade-through-19 chart and about arbitrary
commutative rings respectively; even a positive M1 closes one chart. The
§7.2 Proposition is elementary and is conditional on the websweep's summary
of Jelonek being faithful; I have not read the paper.

---

## 14. File-read / tool / edit disclosure

**SHA-256 verified before reading (14/14 `shasum -a 256 -c` OK):** all
fourteen prompt-pinned files, exactly as listed in the prompt —
`xmodel/ideation-20260827T0935Z-{packet,sol,fable5,grok,opus5}.md`;
`xmodel/max12-812-order2-p0-total-rees-j2-a1-w30-n6-rho0-dual-nonmembership-v43-{sol,hostile-review-opus5}-20260827.md`;
`xmodel/max12-812-order2-gate-t-uniform-contact-shift-naturality-interface-{sol,hostile-review-fable5}-20260827.md`;
`xmodel/max12-812-order2-gate-t-strict-uac-three-row-syzygy-interface-sol-20260827.md`;
`cases/max12_812_order2_gate_t_drho_a2d3_composition_v45_20260827/{RESULT.md,PASS_EVIDENCE.sha256}`;
`cases/max12_812_order2_u2_62_k00_colon_local_v14_20260827/CUSTODY_GAP.md`;
`cases/max12_812_order2_u2_62_k00_colon_local_v14r1_20260827/PREREGISTRATION.md`.
All were read in full.

**Additionally read (not prompt-pinned; read to adjudicate specific claims):**
`xmodel/websweep-20260826T2355Z.md` (Jelonek/Shaska summaries, §7);
`xmodel/max12-812-order2-k00-d8-hostile-review-opus5-20260827.md` (my own,
§§0, 9, for the D8 statement);
`notes.md` `LIVE STATE` 08:07Z and the 08:57Z / 10:05Z event blocks;
`cases/max12_812_order2_p0_total_rees_j2_a1_total_dvr_w30_v43_20260827/compile_total_dehom_eliminant_v43.py`
(full), `…/compile_cascade_dehom_v43.py` (lines 20–130),
`…/homogenize_total_dehom_lift_v43.py` (structure and lines 150–190),
`cases/max12_812_order2_p0_total_rees_j2_a1_constructive_cascade_v43c1_20260827/replay_constructive_cascade_v43c1.py`
(lines 1–300) and its `LOCAL_ABORT.md`. Directory listings of the V43 and
V45 case directories.

**Hashes recomputed live:** the 14 pinned files; `APPROACHES.md`, `AUDIT.md`,
`PROGRESS.md`, `COORDINATION.md` (three of four have drifted from the packet
pins; recorded in §0, no ledger edited).

**Tools used:** `Bash` only — `shasum`, `cat`, `sed`, `grep`, `find`, `ls`,
`wc`, and one throwaway Python script `/tmp/xr_checks.py` (exact `Fraction`
sparse multivariate arithmetic, ~40 lines, staged outside the campaign tree)
which verified the four three-row syzygies and the derivation of `g1,g2,g4`.
No Singular, no CAS, no `msolve`, no FLINT, no network, no AWS.

**Edits:** exactly one file written, `xmodel/ideation-20260827T0935Z-opus5-crossreview.md`.
No campaign artifact, case directory, script, or canonical ledger was created,
modified, staged, cleaned, or deleted. No git operation of any kind was run.

**`jc2-lean`:** not read, entered, built, status-inspected, edited, staged,
cleaned, or otherwise touched. No path under it was passed to any command.

**Execution gaps, disclosed:** I did not re-execute Fable's eleven-contact
naturality numerics, Grok's or Sol's K00 emissions, any Gröbner or
elimination computation, or any V45 or V14/V14R1 computation. Verdicts on
those rest on hand algebra over the frozen statements, on byte reads of the
named sources, and on the desk verification recorded above. The V14R1 delta is
verbal coordinator context and is treated as provisional throughout.
