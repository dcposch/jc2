# Hostile review: Sigray pp. 39--45 later-`M` package (Opus 5, 2026-08-28)

**Audited artifact:** `xmodel/sigray-later-m-package-source-audit-sol-ultra-20260828.md`
SHA-256 verified `5fc6b1634dc1ef0a0abe578411644fa166ffbfa16b8608cbce2a7b7b61465cd5`.
**Primary source:** `refs/sigray_full.pdf`, SHA-256 verified
`9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae`,
printed page = PDF page. Layout text plus `pdftotext -bbox` on the load-bearing
fractions (guarding the known stacked-fraction trap). No AWS, web, or heavy CAS;
one exact rational polynomial check in pure Python. No existing artifact edited.

## 0. Bottom line

The producer's package is **substantially correct and its central negative
finding survives hostile attack**. All seven printed-slip lists check out
verbatim. The two new mathematical contributions -- the local order lemma
`(L6-root)` and the UFD/valuation repair of Propositions 8.1/8.2/Statement 8.4 --
are correct and load-bearing. I confirm the root-endpoint gap in Proposition 8.4
and the required rollback.

Against the producer I record: **one missed source defect of the same severity
as the ones it reports** (Statement 8.5's `ε ≡ 1 mod ν` step, §3.3 below), **one
missed corroboration** (the source's own Notation 9.2 *is* `(Reg)`), **one
mis-typed dependency** in the axis step (§5.1), **two residual existence
hypotheses** in the `(Reg)` repair, and **one dependency on a Section 9 statement
outside the audited block**. None of these overturns a verdict; three of them
change what may be promoted as self-contained.

---

## 1. `(L6-root)` and Corollary 6.1 --- **CONFIRMED, proof complete**

Setup verified against the source: for `F ∈ T_a^&` write `u=π(F)`, `p=p_F`,
`q=p_{h_F,F}`, `d=d_F`, `e=d_{h,F}`, `µ=µ_F`.

* `d_F>0` for all `F ∈ T_a^+` (used, unstated, inside Proposition 6.6's proof:
  "`(1-v)deg(p_G) ≤ 0 < d_G`"). With `d>0` and `d<(1-u)deg p`, one gets `u<1`.
* Proposition 4.2(iv) `⇒ e=(µ-1)d+1-u` (the source derives exactly this inside
  Proposition 6.1's proof). Hence `e/d = µ-1+(1-u)/d > µ-1`. ✓
* Proposition 4.6 (p. 23, verified by bbox): at a root `c`, with `a=mult(p,c)`,
  `b=mult(q,c)`, either `(12) a+b-1<µa` **and** `(13) a/b=d/e`, or `(14) a+b-1=µa`.

Under (12)+(13): `b=(e/d)a>(µ-1)a`. The producer's integrality step is sound and
I reprove it independently: (11) reads `d·pq' - e·p'q = ⊖ p^µ` with `⊖` a nonzero
scalar (Proposition 4.1 fixes that reading). The left side is a polynomial, so
`p^µ` is a polynomial, so `µ·mult(p,c) ∈ ℤ` at every root; hence `(µ-1)a ∈ ℤ`.
With `b ∈ ℤ`, `b>(µ-1)a` upgrades to `b ≥ (µ-1)a+1`, i.e. `a+b-1 ≥ µa`,
contradicting (12). Therefore (14) holds at **every** root:

```
(L6-root)   mult(p_{h,F}, c) = (µ_F - 1)·mult(p_F, c) + 1     for all F ∈ T_a^&.
```

**Verdict: CONFIRMED.** This is a genuine *campaign replacement theorem*: the
printed Corollary 6.1 (p. 32) cites Proposition 6.7 for it, and Proposition 6.7
(p. 33) states only (a) `F*c ∈ T_a^+` and (b) existence of one `c` with
`F*c ∈ T_a^&`. The citation is a **source gap**, correctly diagnosed.

Corollary 6.1's repair also checks: summing (L6-root) over the `r` distinct roots
gives `deg q ≥ (µ-1)deg p + r`, so the degree alternative (17)
`deg q=(µ-1)deg p+1` forces `r=1`, contradicting Statement 3.16.

*Producer erratum (harmless):* the argument needs `F ≠ (0,x)` as well, since
Statement 3.16 excludes both axis vertices. It is automatic --- Theorem 6.1's
proof gives `d_{(0,x)}=k_f > l_f = deg p_{(0,x)}`, so `(0,x) ∈ T_a^↗`, and the
source uses this openly in Statement 9.4's proof.

*Also unrecorded by the producer, but needed:* (L6-root) gives `v_c(q)=1` at each
root, hence `deg q ≥ r ≥ 2` at a nonroot vertex --- **this** is why Statement
8.2's proof opens with "`p` has more than one root". Without `deg q ≥ 2` the
top-degree comparison in (iv) is vacuous.

## 2. Proposition 8.1 --- **CONFIRMED after the producer's repairs**

All seven printed slips reproduce exactly on pp. 40--41: raw Bezout product
called polynomial; "`j=1/i` ... proves property (ii)" (should be (i));
`iµ_G` for `iµ_F`; `H(ξ,u)` for `H(ξ,η)`; `l=1-u` computed then `H=ξ^{u-1}q`
printed; Proposition 6.3 cited for the root-order equality; `M_F` printed twice
in (v) where `M_F^*` is required.

**Degree ratio.** Proposition 4.2(iii) is `(h_{j,F}^+)^{k_j}=s_j(f_F^+)^{l_j}`, so
`k_j·deg p_{h_j,F} = l_j·deg p_F`, i.e. `deg p_{h_j,F}/deg p_F = l_j/k_j`. The
producer's orientation is right. **Precision correction:** p. 40 prints this
ratio *correctly*; the reversals are on pp. 41--43 only, not "pp. 40--43".

**`i` is exactly `lcm(k_j)`.** Reproved: `k_j | D` since `D_j=(l_j/k_j)D ∈ ℕ` and
`gcd(k_j,l_j)=1`; `gcd(D,(l_j/k_j)D)=D/k_j`; so
`M_F^* = gcd_j(D/k_j) = D/lcm_j(k_j)` and `i = lcm(k_0,…,k_{m-1})`. ✓
(`m=0`: `M_F^*=D`, `i=1`.)

**Perfect power.** From `p_{h_j,F}^{k_j} = ⊖ p_F^{l_j}`: for each irreducible `r`,
`k_j v_r(p_{h_j,F}) = l_j v_r(p_F)`, so `k_j | v_r(p_F)`, so `i | v_r(p_F)`.
Hence `p_F = ⊖ p^i` with `p` a *polynomial*, and moreover
`p_{h_j,F} = ⊖ p^{r_j}`, `r_j = i·l_j/k_j ∈ ℕ*`. ✓ The Bezout product's valuation
at each irreducible is `N^*v_r(p_F)+ΣN_j^*v_r(p_{h_j,F}) = v_r(p_F)/i ≥ 0`,
which is precisely the missing negative-exponent justification. ✓

`k=i(µ_F-1) ∈ ℤ` since `k_j | i` makes `i(k_j-1)l_j/k_j ∈ ℤ`. ✓

**Polynomiality of `q`.** `k ≤ 0` trivial; `k>0`: poles only at roots of `p`, and
(L6-root) gives `v_c(p_{h,F}) = (µ-1)i·v_c(p)+1 = k·v_c(p)+1`, so `v_c(q)=1`. ✓

(iii)⇒(iv) verified: `J(ξ^δp,ξ^{1-u}q) = ξ^{δ-u}[δpq'-(1-u)p'q]`. ✓
(v): `deg p_{h,F}=k·deg p+deg q` and `M_F^*=deg p` give
`M_F = gcd(M_F^*,deg p_{h,F}) = gcd(deg p, deg q)`. ✓

**Verdict: PASS.** Repairable errata only; the mathematics is complete.

## 3. Statements 8.3--8.5

### 3.1 Orientation --- CONFIRMED

Proposition 3.2 (p. 18) defines `F := G + c` with `G = F°`. So in Statement 8.4
`G = F + c` puts **`F` at the lower/rootward vertex and `G` at the upper child**.
The producer's reading is correct, and its consequence -- Statement 8.4 says
`mult(p_F^{red},c) | M_G`, *not* `M_F | M_G` -- is correct.

### 3.2 Statement 8.4 --- **PASS, and root-independent**

Printed defects all reproduce on p. 42: `N_m^*` for `N_m`; product truncated at
`h_{m-1,F}` while the next line uses `N_m`; Proposition 6.7 cited for
polynomiality/perfect-power; final transported degree subscripted `F` not `G`.

Producer's direct proof audited against check 3's demand that *every* tower
member used be nonterminal at the lower vertex and a positive integral power of
the same reduced pattern:

* `G ≺ F` strictly (Corollary 6.1 at `G` -- legitimate, `G ≠ (0,y)` since `G` is
  an upper vertex -- plus Proposition 6.3), so `m_G < m_F` and every index
  `j ≤ m_G` satisfies `j < m_F`: **nonterminal at `F`, including `j=m_G`.** ✓
* Hence `p_F=⊖p^i`, `p_{h_j,F}=⊖p^{r_j}`, `r_j = i l_j/k_j ∈ ℕ*`: positive
  integral powers of one reduced pattern. ✓
* Adjacent transport (Statement 3.17(i) plus the adjacent form of 8.3(ii)):
  `deg p_G = i·a`, `deg p_{h_j,G} = r_j·a` with `a=mult(p,c)`; gcd gives `a | M_G`. ✓

**Additional finding in the producer's favour:** the lower vertex may be `(0,y)`.
`(0,y) ∈ T_a^&` under the source's operative convention and Corollary 6.1 is
applied at `G`, not at `F`. So Statement 8.4 is valid *including at the root
edge*, exactly as claimed.

### 3.3 Statement 8.5 --- **PASS only after a repair the producer did not supply**

The producer's corrections (systematic `k/l` inversion; final line must read
`gcd(ν, deg p_{h,G})=1`, not `p_{h,F}`; `c=0` allowed) all check.

**Missed defect.** The source's last step -- "since `p_G(η)=p̃(η^ν)`, by
Proposition 4.6 one gets `p_{h,G}(η)=η r(η^ν)`" -- does **not** follow from
Proposition 4.6, and the producer merely restates it as `η^ε r(η^ν)`,
`ε ≡ 1 (mod ν)`, without proof. This is the only step that yields
`gcd(ν, deg p_{h,G})=1`, i.e. the whole theorem.

Repair (mine). Write `q = p_{h,G} = Σ_{s<ν} q_s` by η-degree residue mod `ν`.
With `p=p_G=p̃(η^ν)` and `p' = νη^{ν-1}p̃'(η^ν)`, both `pq_s'` and `p'q_s` sit in
class `s-1`, and `⊖p^µ` sits in class `0`. So (11) splits:

```
s = 1 :  d_G·p q_1' - d_{h,G}·p' q_1 = ⊖ p^µ
s ≠ 1 :  d_G·p q_s' = d_{h,G}·p' q_s   ⟹   q_s = C·p^{d_{h,G}/d_G}.
```

A nonzero solution of the homogeneous equation has all η-degrees `≡ 0 (mod ν)`,
so `q_s=0` for `s ∉ {0,1}`, and `q_0 = C p^{d_{h,G}/d_G}` with
`deg q_0 = (d_{h,G}/d_G)deg p_G`. If `G ≠ (0,y)`, Corollary 6.1 applies at `G`
and gives `deg q = (d_{h,G}/d_G)deg p_G = deg q_0`; but `deg q_0 ≡ 0` and
`deg q_1 ≡ 1 (mod ν)` cannot both equal that number, so `q_0=0` and `q=q_1`,
whence `deg q ≡ 1 (mod ν)`. If `G=(0,y)` then `ν_G=1` (Statement 9.2(ii)) and the
conclusion `gcd(νM_F,deg q) | M_F` is immediate.

**Verdict: PASS with repair.** Classification: *source gap* (not an erratum);
the producer's write-up currently promotes an unproved step.

## 4. Proposition 8.2 / Corollary 8.1 --- **CONFIRMED after restoring `h_0`**

Confirmed on p. 43: the Bezout equation carries `N_0` but the product runs
`∏_{j=1}^m`; the `h_0` factor is omitted.

Check 4's worry is the right one and the producer answers it correctly, though
tersely. Positive valuation at one root would *not* suffice in general. It
suffices here because `F ≺ G` strictly, so every index `j ≤ m_F` is nonterminal
at `G`, hence *every* factor is a power of one reduced pattern `p_*`:
`p = ⊖p_*^w`, `w = N i_G + ΣN_j ρ_j ∈ ℤ`. Then
`mult(p,c^*) = w·mult(p_*,c^*) = M_F ≥ 1` forces `w ≥ 1`, so **all** valuations
are `w·v_r(p_*) ≥ 0` and `p` is a polynomial. ✓

Remainder verified line by line: `mult(p_G,c) ≥ deg(p_F)/M` reduces to
`mult(p_*,c) ≥ 1/w`; and
`d_H+(π(H)-1)deg p_H = d_G+(v-1)mult(p_G,c) = d_F+(u-v)deg p_F+(v-1)mult(p_G,c) ≤ 0`
under the stated hypothesis, so `H ∉ T_a^↗` and Statement 6.1 gives `H ∈ T_a^&`. ✓
Corollary 8.1 (`M=1`) is immediate from `d_F<(1-u)deg p_F`. ✓ Both already
exclude `(0,y)`.

## 5. Proposition 8.3 and `(Reg)` --- **CONFIRMED, with two hidden hypotheses**

The printed hypothesis ("for any `H ∈ T_a^& ∩ (V_a\{(0,y)})`, `G ≠ H°`") is
contradicted by `H=F`. **The printed Proposition 8.3 is vacuous.** ✓

**Corroboration the producer missed.** The source itself later introduces exactly
`(Reg)`: Notation 9.2 (p. 48) --- "`G` is regular over `F` if for any
`H ∈ V_a ∩ T_a^& \ {(0,y)}` with `H° = G` one has `H = F`". This upgrades the
producer's `(Reg)` from a plausible reconstruction to the source's own notion,
and should be cited in any promotion.

**Residual gaps in (i) under `(Reg)` alone.** The step "`G ∈ V_{2,a}` produces a
second down *actual child*, violating `(Reg)`" needs the branch above
`G*c` to contain a **vertex**. Corollary 8.1 delivers down *microsteps*; nothing
in the audited package guarantees a next vertex exists in a given direction.
Under the singleton-pole hypothesis this is repairable at microstep level, and
more cleanly than the producer's route: for any `c` with `G*c ∈ T_a^&`, either
`deg p_{G*c} ≠ 1` and repaired Proposition 6.8 puts a pole weakly above on that
branch, or `deg p_{G*c}=1` and Lemma 6.1 + Proposition 5.1 put `G*c` itself at a
pole. Distinct directions give distinct poles (branches disjoint above `G`);
poles are vertices by Proposition 5.3(iv). **So singleton pole ⟹ at most one down
direction at `G`.** That simultaneously yields §9.1's sibling exclusion (where
`deg p ≥ 2` is anyway automatic by Statement 3.16 for `H ∈ V_a\{(0,x),(0,y)}`),
the `V_{2,a}` exclusion in 8.3(i), and clause (iii).

**Clause (iii) consumes a Section 9 statement.** "Two distinct roots give two down
children" needs `ν_{(0,y)}=1`, i.e. **Statement 9.2(ii)** (p. 48), so that every
root of `p_{(0,y)}` -- not merely every `ν`-orbit -- carries a child
(Statement 3.18). This is outside the audited pp. 39--45 block and is missing from
the producer's §12.1 minimal trust set. The printed citation of Statement 3.16 in
(iii) is indeed outside that statement's domain. ✓

**Clause (ii).** `M` is unbound (or inherits `M_F=1` from Proposition 8.2, making
the clause false); `r = deg p_G/ν_G` is the right reading. Confirmed unused by
Proposition 8.4. ✓

## 6. Proposition 8.4

### 6.1 Nonroot theorem --- **REPROVED, valid**

Descent: `F_0=F`, `F_{j+1}=F_j°` while `π(F_j) ≠ 0` (printed `F_{n+1}=F°`: index
typo, confirmed). `F_n=(0,y)`, `H=F_{n-1}` defined iff `n ≥ 1`. `M_H=1` by
repaired 8.3(i) at each `(Reg)` step; 8.3(iii) gives `p_R = ⊖(η-c)^r`.

Axis step, reproved:

* For `j < m_R`, Proposition 4.2(iii) at `R` gives
  `(deg p_{h_j,R}, d_{h_j,R}) = (l_j/k_j)(deg p_R, d_R) = (l_j/k_j)(k_f,l_f)`.
  Since `m_H < m_R`, every `j ≤ m_H` qualifies: all summands are on the axis.
* `p_{h_j,R} = ⊖(η-c)^{r l_j/k_j}` is a pure power, so
  `deg p_{h_j,R} = mult(p_{h_j,R},c)`; adjacent transport then gives
  `= deg p_{h_j,H}`, and `deg p_R = mult(p_R,c) = deg p_H` (Statement 3.17(i)).
  Hence `k = M_H = 1` (printed `deg(p_H,c)`: typo for `deg(p_H)`).
* `(k,l)=w(k_f,l_f)`, `k=1 ⇒ w=1/k_f`, `l=l_f/k_f`. Lemma 2.1(i) gives
  `k_f,l_f>0` and Theorem 6.1 gives `l_f<k_f`, so `0<l<1` while `l ∈ ℤ`. ⨳

**Producer dependency erratum.** §9.3 attributes the axis proportionality to
"repaired Corollary 6.1 + Proposition 6.3/tower-persistence". Corollary 6.1
*explicitly excludes* `(0,y)` and cannot be applied at `R`. The correct typing is:
Proposition 4.2(iii) **at `R`** for `j<m_R`, plus `m_H<m_R` from Corollary 6.1
**at `H`** and Proposition 6.3, plus the adjacent-transport lemma. The source
makes the same mis-citation; the producer inherited it.

**Verdict: corrected nonroot Proposition 8.4 is PROVED**, on
`F ∈ T_a^& ∩ (V_a \ {(0,y)})` with `T_{a,pole}` a singleton.

### 6.2 Root clause --- **OPEN PROOF GAP** (not proved, not refuted)

For `F=(0,y)`: `π(F)=0`, the descent stops at once, `n=0`, `H=F_{-1}` undefined.
`(0,y) ∈ V_a` (Definition 3.4) and `(0,y) ∈ T_a^&` under the source's operative
convention (`deg p_{(0,y)}=d_{(0,x)}=k_f`, `d_{(0,y)}=deg p_{(0,x)}=l_f`, p. 32
plus Theorem 6.1's proof; and Corollary 6.1/Propositions 8.2/8.3 all remove
`(0,y)` *from* `T_a^&∩V_a`, so the source plainly regards it as a member).
**The root is inside the quantified set and outside the proof.** ✓

I add the exact structural reason the argument cannot be restarted at `R`: the
axis argument needs *every* member of the `M`-list at `R` to be proportional to
`(k_f,l_f)`. Proposition 4.2(iii) supplies this for `j<m_R` only; the terminal
member `h_{m_R,R}` needs precisely Corollary 6.1's degree/order equality, which is
the one statement whose proof (via Statement 3.16) is unavailable at `(0,y)`. The
gap is not an accident of the descent's indexing.

The producer's claim that no reverse propagation exists is confirmed: 8.3(i)
propagates `M=1` rootward; 8.5 gives `M_{lower} | M_{upper}`; 8.4 gives
`mult(p_F^{red},c) | M_G` upward, which with a one-root `p_R` reads `1 | M_G` --
vacuous. Singleton pole removes siblings but supplies no divisibility.

**Root data checks.** At `R`: `u=0`, `(deg p_R,d_R)=(k_f,l_f)`, `p_R=⊖p^i`,
`δ=l_f/i`, `deg p=k_f/i`, and (8.1-iv) becomes `δpq'-p'q=⊖p`. Top-degree
comparison: either `deg q=1` or `δ deg q = deg p`, i.e. `deg q=k_f/l_f`. I note a
sharpening the producer did not: **if `deg q=1` then `M_R=gcd(deg p,1)=1`
automatically**, and the ODE then forces `p=⊖(η-c)^{deg p}` (the logarithmic
derivative `(η-c)Σa_j/(η-c_j)` must be constant), i.e. `p_R` a pure power --
which is also exactly the configuration in which the printed Statement 8.2's
conclusion `deg(q)·mult(p,c) ≠ deg(p)` **fails**. So Statement 8.2's root
exclusion is not cosmetic; the equality case is realized on the same branch.

**Producer's packet is not a countermodel, as it states.** I verified its algebra
exactly (pure-Fraction expansion): with `F=P^2Y^2+aY+b`, `G=P^3Y^3+cY^2+dY+e`,
killing the `Y^5,Y^4,Y^3` coefficients of `G^2-F^3` forces
`c=(3/2)Pa`, `d=(3/2)Pb+3a^2/(8P)`, `e=3ab/(4P)-a^3/(16P^3)`, and

```
[Y^2](G^2 - F^3) = -(3/(64P^2))·(a^2 - 4P^2 b)^2 ,
```

matching the report. With `P=X^2`, polynomiality of `e` forces `X^2 | a`; writing
`a=X^2β` gives `[Y^2] = -(3/64)X^4(β^2-4b)^2`, divisible by `X^4`, so it can never
be the `X^3` required by `h_1^+=ξ^2η^3` (and `β^2=4b` kills the `Y^2` term
entirely). ✓ The packet `p=η^2,q=η,δ=1`, type `(2,3)`, `(k_f,l_f)=(4,2)`,
`µ=3/2`, `m_R=1` satisfies every displayed identity but admits no polynomial
one-step tower lift.

**Verdict: OPEN PROOF GAP / QUARANTINE.** Not "false": no fully typed polynomial
tower countermodel exists in the package, and a bare ODE/leading-form packet does
not count. Not "proved": nothing in pp. 39--45, repaired, reaches it.

*Flag (no verdict impact).* A literal reading of Notations 3.9/3.10 at
`π=0` (`η_{(0,y)}=y`, expansion in `x`) would give `d_{(0,y)}=deg_x f=k_f` and
`(0,y) ∈ T_a^↗`, i.e. the opposite of p. 32's `d_{(0,x)}=deg p_{(0,y)}`. The
source's Section 8 is internally consistent only with the p. 32 convention. Under
either reading `M_{(0,y)} ≠ 1` is unavailable, so the rollback stands
unconditionally; but any promotion asserting "`(0,y) ∈ T_a^&`" (as
`SHEET6-AF3.md` does) is resting on a source-level convention, not on a checked
computation.

## 7. Canonical-consumer blast radius --- **CONFIRMED, spot-verified**

The decisive rule (nonroot `M=1` kills; root-only `M=1` does not) is correct, and
Proposition 5.3(i) does make every pole nonroot, so pole-entry uses are safe.
Spot checks: `ladder/SHEET6-CAMPAIGN.md:44` reads "`M_F ≠ 1` for every `F` in the
tree" ✓ must be restricted; `ladder/SHEET6-AF3.md:135-138` asserts "Prop 8.4
(p. 44 -- `(0,y) ∈ T_a& ∩ V_a`) forbids 1, forcing `M_{(0,y)}=3`" ✓ unsupported;
`ladder/SHEET6-TDU-REVIEW.md:~190` same ✓; `ladder/SHEET6-MULTIPOLE.md:44` MP2
quantifies over `F ≤ G^*`, which includes `(0,y)` ✓ must exclude it;
`papers/paper2/main.tex:107,163` imports Statement 8.4, Corollary 6.1,
Proposition 8.1, Statement 8.5 -- **not** Proposition 8.4 ✓ unaffected;
`ladder/REDUCTION.md:618-622` uses the single-pole mechanism at a prime-`d` pole
entry ✓ nonroot, no rollback.

## 8. Verdicts on the producer's Section 15 promotions

| # | Promoted item | Verdict |
|---|---|---|
| 1 | `(L6-root)` + nonroot Corollary 6.1 | **PROMOTE.** Proof complete and independently reproved. Add the `F ≠ (0,x)` remark and record the `deg q ≥ r` corollary that Statement 8.2 consumes. |
| 2 | Proposition 8.1 with UFD/valuation polynomiality | **PROMOTE.** All five clauses verified; `i=lcm(k_j)` reproved. Depends on item 1. |
| 3 | Adjacent tower-transport lemma | **PROMOTE WITH CAVEAT.** Prefix case is Proposition 4.2 persistence; the terminal case is stated, not proved, in the producer report (it is the corrected `ψ` computation of p. 42 moved to an edge). Promote as a *stated lemma with proof sketch*, not as verified. |
| 4 | Statement 8.4, direct gcd form | **PROMOTE.** Cleanest result in the package; valid including at the root edge; independent of the Proposition 8.4 defect. |
| 5 | Corrected Proposition 8.3(i),(iii) under `(Reg)` | **PROMOTE WITH REPAIR.** Cite Notation 9.2 for `(Reg)`. (i) additionally needs the microstep-level pole argument of §5 (or the singleton-pole hypothesis) to exclude `V_{2,a}`; (iii) additionally consumes Statement 9.2(ii) (`ν_{(0,y)}=1`), which is outside the audited block. Add both to the trust set. |
| 6 | Corrected **nonroot** Proposition 8.4 | **PROMOTE.** Reproved in §6.1. Correct the dependency typing (Proposition 4.2(iii) at `R`, not Corollary 6.1 at `R`). Consumes item 5, hence Statement 9.2(ii). |

Quarantines (Statement 8.2 at the root; Proposition 8.3(ii) unless renamed
`r=deg p_G/ν_G`; every use of `M_{(0,y)} ≠ 1`; any suffix theorem whose quantified
set contains `(0,y)`): **all four CONFIRMED as necessary.** I strengthen the first:
Statement 8.2's equality case is *realized* exactly in the `deg q=1`, pure-power
`p_R` configuration, so this is a **false statement at the root**, not merely an
unsupported one.

**Not promotable as audited:** Statement 8.5. Its `gcd(ν,deg p_{h,G})=1` step is
unproved in both the source and the producer report. With the §3.3 repair it is
promotable; without it, Proposition 8.3(i) -- and therefore the whole nonroot
Proposition 8.4 -- rests on an unestablished step.

## 9. Claims needing theorems not established in the audited package

1. **Statement 9.2(ii)** (`ν_{(0,y)}=1`), p. 48 -- consumed by repaired
   Proposition 8.3(iii).
2. **Repaired Propositions 6.7/6.8** in the campaign sense (`c3d6ff92`, sweep r2
   `581219e0`, per `ladder/SHEET6-MULTIPOLE.md:90`), including the
   microstep-to-next-vertex bridge -- consumed by §9.1 sibling exclusion and by
   Proposition 8.3(i). The *printed* 6.7/6.8 do not supply the bridge.
3. **Adjacent tower transport** (item 3 above) -- stated, not proved.
4. **Statement 8.5's residue step** -- see §3.3.
5. **A separate root theorem** ("singleton pole + `M_{(0,y)}=1` is impossible") --
   does not exist anywhere in the package. The producer's recommendation to open it
   as its own producer is correct; the sharpened target is: rule out
   `p_R = ⊖(η-c)^{k_f}` with `deg q = 1`, using polynomial/global data.

## 10. Defect typing summary

* **False statements:** printed Proposition 8.3 (vacuous hypothesis); printed
  Statement 8.2 at the root; printed Proposition 8.3(ii) as literally exponented;
  printed Proposition 8.4's root clause (unproved, and its proof text is
  ill-formed there).
* **Source gaps (proof missing, statement believed true):** Corollary 6.1's
  root-order input; negative-Bezout polynomiality in Propositions 8.1/8.2 and
  Statement 8.4; the `h_0` omission in Proposition 8.2; Statement 8.5's
  `ε ≡ 1 (mod ν)`; the `V_{2,a}`/next-vertex existence step.
* **Repairable errata:** all seven pp. 39--41 slips; the five Statement 8.4 slips;
  `k_j/l_j` inversions on pp. 41--43; `p_{h,F}` for `p_{h,G}` on p. 43;
  `F_{n+1}=F°`; `deg(p_H,c)` for `deg(p_H)`.
* **Campaign replacement theorems:** `(L6-root)`; the UFD perfect-power lemma;
  the direct gcd proof of Statement 8.4; `(Reg)`-based Proposition 8.3; the
  corrected nonroot Proposition 8.4.
* **Producer errata (this review):** ratio reversal scope "pp. 40--43" → 41--43;
  axis-step dependency mis-typed as Corollary 6.1 at `R`; missing `F ≠ (0,x)` in
  the Corollary 6.1 repair; Notation 9.2 not cited; Statement 8.5's key step
  asserted; Statement 9.2(ii) absent from the minimal trust set.
