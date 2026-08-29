# Cross-review — GATE-REC theorem R8 (quarter-root sector gate recurrence)

Date: 2026-08-27
Reviewer: **Opus 5**, independent hostile review
Producer: Sol Ultra (different model ⇒ this is a valid promotion leg if it survives)
Charged report: `xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-sol-ultra-20260827.md`

Charged SHA-256, recomputed **before** reading:

```text
71befadb3496f5f6c8e3136e7019de95dec2f205f2655734eac2c84d8e0e24d1
  xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-sol-ultra-20260827.md
```

## 0. Headline verdict

**The theorem survives. CONFIRMED WITH REPAIRS, at exactly the scope the
producer claims and no wider.**

Theorem 4.1 (every fixed-receiver class coordinate of the correctly
gauge-normalized residue-sector series is D-finite in `z` / P-recursive in
the row index, at fixed characteristic-zero `H,F`) is a genuine new theorem.
It closes the item the reviewed post-seal ledger recorded as

```text
gate/residue coordinates P-recursive        OPEN (plausible, not automatic)
```

and it does so by supplying exactly the missing ingredient that review named
(a creative-telescoping argument compatible with the `X`-dependent raw
recurrence), not by re-asserting raw P-recursiveness.

The load-bearing normalization repair — that the transported class series has
coefficients `p^{-(b+22)} q_(b+4k)` and **not** `H^k q_(b+4k)` — is correct,
and I confirmed it by an independent derivation carried out in *Fable5's own*
`T_m(Y)=4HY'+(m-12)H'Y` convention, plus an explicit numerical separation of
the two series at `z^2` on a frozen fixture (§4.3 below).

Four repairs are required, one of them substantive:

| # | Item | Class |
|---|---|---|
| R-1 | The Puiseux/trace descent (4.3)–(4.4) needs the **module grading** `O(V_H\|_U)=⊕_j p^j A` with `p^e` a unit in `A`; the report's one-line "no connectedness required" does not supply it | **REPAIRED (substantive)** |
| R-2 | Crude bound (2.5)/`614656` omits the `K(zeta)` adjunction; safe crude value is `32 D^4 = 1229312` | REPAIRED (cosmetic) |
| R-3 | Prefix formula (6.4) has no term forcing `N0 >= ell_max-1` when `A_ellmax` has **no** nonnegative root, and no per-`b` maximum | REPAIRED (recipe-level) |
| R-4 | Variable collisions: `n` = row index (§1–3) vs `n=[E:K(z)(X)]` in (0.1)/(5.1); `N` = Puiseux index (4.3) vs recurrence index (§6); `R` vs `R_Q`. Also the dropped R7R1 factor `-(n+2)/16` and a spurious `b=2,3` parenthetical in §3 | REPAIRED (cosmetic, but ironic in a typing-repair report) |

One item I could not verify and must record as a **GAP**: the attribution of
(0.1) to *Corollary 15* of Chen–Kauers–Koutschan (2016). I have no network in
this session. I independently re-derived the bound's **form** and validated it
in the rational (`n=1`) degeneration, but I cannot certify the corollary
number or that paper's exact hypothesis list.

One novelty correction: the sector shift is **not new**. "Row `m=n+22` lands
in the `m mod 4` summand" is already the confirmed content of the Opus5 torsor
theorem (`0ccdc259…`, §3 and §7). What is genuinely repaired is (a) the
`p`-power normalization silently dropped by the notation `[q_n dX]` in two of
the three cited reviews, and (b) Fable5's `Gamma_a = sum H^k q_(a+4k) z^k`.

Nothing here licenses row independence, nonlinear nonvacuity, polynomial
descent, an endpoint verdict, or JC2. All six of the report's firewalls hold.

## 1. Custody

Every additional local file I read is one the charged report explicitly cites.
All five hashes reproduce the producer's §10 custody block **exactly**:

```text
8bad7ca04ae9a6f45efde305b208309f528173820250d20dab67d00bc32d73a4
  xmodel/ideation-20260827T2137Z-postseal-exact-hostile-review.md
0ccdc259358267fc805c2af477bc6b0f48620dbd2e76c016cdb85caee1ba3cba
  xmodel/ideation-20260827T2137Z-opus5-hostile-review-sol-ultra.md
d7e810f75ca2158fa8839a60e2005a85e655c5ad9309dda35963f2daee14ea3b
  xmodel/ideation-20260827T2137Z-fable5-hostile-review-sol-ultra.md
5beb555075c662e76f8b86062efdf89b2c3a4dd0eb80ffd52fbf3c38bf130d55
  xmodel/ideation-20260827T2137Z-fable-linear-vacuity-hostile-review-sol-ultra.md
9d35c678cfc257c5c518f87c19df25942cbaca3b5aa8186a22507f1f1e1f3ae1
  xmodel/ggv-quarter-root-characteristic-de-rham-tower-r7r1-sol-20260827.md
```

No other repository file was opened, listed, globbed, or searched. `jc2-lean`
was never entered. No `ideation-20260827T2255Z*` or `…T2259Z*` file was read.
No canonical file (`APPROACHES.md`, `AUDIT.md`, `COORDINATION.md`,
`PROGRESS.md`, `notes.md`) was read or edited. No AWS resource was contacted.
Local work was exact rational desk arithmetic only (largest object: an
8-term power-series reversion over Laurent polynomials in one variable).

I record without endorsing that the producer self-disclosed a `find ..` that
may have stat'd the nested tree. It carries no mathematical content and does
not affect any verdict here; I performed no such traversal.

## 2. Charge item 1 — sector shift, gauge normalization, literal vs transported

### 2.1 The `b -> b+22` shift — CONFIRMED as mathematics, novelty OVERSTATED

`q_n` has `p`-character `zeta^(n+2)`, so the row's receiver index is
`n+2 mod 4`. Writing it as `n+22` matches R7R1's `w_(n+22)` indexing, and
`n+22 == n+2 (mod 4)`. The producer's §3.1 statements are exact, including
"if you want the receiver literally named `nabla_a`, take `b == a-2 (mod 4)`".

But **`22` versus `2` is pure bookkeeping**: `V_(n+2)` and `V_(n+22)` are
identified by multiplication by the unit `H^5`, so they give identical gate
verdicts. Desk check B confirms this for `n=0..11`. Only the residue class
mod 4 is material, and that was already sealed by the confirmed Opus5 torsor
theorem, §7: *"Every licensed gate row `m` lands in the `m mod 4` summand."*

So headline item 1, framed as a "load-bearing typing repair", repairs no
literal statement in the cited evidence bank. It is correct, useful as an
explicit warning, and **not new**. The report should name the statement it
repairs; it names none.

### 2.2 The `p`-power normalization — CONFIRMED as a genuine repair

Two of the three cited reviews literally write

```text
[q_n dX] lands in H^1_dR(U, nabla_m),     m = n+22
```

(`0ccdc259…` §3; `5beb5550…` §3 item 1). That is mistyped: `q_n ∈ p^(n+2)A`,
so `q_n dX` is not an `A dX` element and `nabla_m` does not act on it. The
producer's (3.4)–(3.5), `c_(b,k) = p^(-m_k) q_(b+4k) ∈ A`, is the correct
typing. **CONFIRMED.** Verified: `p^(-m_k) q_(b+4k) = p^(4k-20) r_(b+4k) = H^(k-5) r_(b+4k)`,
which is the report's own displayed identity and is `b`-independent (so the
report's parenthetical hedge "`b=2,3` merely changes the bookkeeping by one
additional fixed power of `H`" is spurious — R-4).

The normalization is not arbitrary. It is exactly the one the **confirmed**
linear-vacuity theorem uses: there, `(q_n)_lin = (1/4)F_n p^(n-6) = p^m · F_n/(4H^7)`
with `m=n+22` and `p^28=H^7`, i.e. `p^(-m)(q_n)_lin = F_n/(4H^7)`. That
agrees termwise with the producer's `c_(b,k)`. **Cross-consistent.**

### 2.3 `sum H^k q_(b+4k) z^k` is NOT the transport — CONFIRMED (independently re-derived)

(0.2) reads `H^k p^(-(b+22+4k)) q_(b+4k) = p^(-(b+22)) q_(b+4k)`, i.e. the
gauge `H^k = p^(4k)` **cancels** the `k`-dependent part of the row's `p`-power.
Trivially verified. The substantive question is whether Fable5's object

```text
Gamma_a(X,z) = sum_k H^k q_(a+4k)(X) z^k                (d7e810f7…, §2.2)
```

is the transport. It is not. I re-derived this **inside Fable5's own
convention** rather than the producer's, so as not to inherit the producer's
normalization:

* `T_m(Y) = 4HY' + (m-12)H'Y = 4H · nabla_(m-12)(Y)` (verified, desk check G),
  so Fable5's receiver index carries a further `-12` offset — same class mod 4.
* Writing `w_m = p^(m-12) Y` and using R7R1's `w_(n+22)' = -(n+2)q_n/16`
  gives the direct row equation `T_(n+22)(Y) = -(n+2)/4 · H q_n p^(-(n+10))`.
* For `n = a+4k`: `p^(-(n+10)) = p^(-(a+10)) H^(-k)`.
* Transporting by `[f] |-> [H^k f]` (Fable5's own confirmed cokernel direction)
  gives `H^k · H q_n p^(-(n+10)) = H q_(a+4k) p^(-(a+10))`.

**The `H^k` cancels.** Fable5's `Gamma_a` therefore carries one extra factor
`H^k` relative to the true transport. **The producer's repair is CONFIRMED.**

It is a material difference, not a change of representative: multiplication by
`H` does **not** descend to an endomorphism of `V_(m_0)` (it maps `V_(m_0+4) -> V_(m_0)`),
so the two series are different linear functionals of the same rows. Made
explicit on `H=X^4` (where `V_m = K·[X^(-m-1)]`, `lambda_m(f)=[X^(-m-1)]f`):

```text
correct  C_b[k] = [X^(-m_0-1)]      ( p^(-m_0) q_(b+4k) )     fixed residue index
literal  (3.11) = [X^(-m_0-1-4k)]   ( p^(-m_0) q_(b+4k) )     index drifts by -4k
```

and numerically separated at `k=2` in §4.3 below.

### 2.4 The literal series' own typing (3.11) — CONFIRMED

`H^k q_(b+4k) ∈ p^(b+8k+2) A`, one fixed character `zeta^(b+2)`, so
`pi_j(p^(-j) Gamma_b^lit dX)` with `j == b+2 (mod 4)` types correctly, and
Theorem 4.1 applies to it verbatim. The producer's sentence "it is simply a
different class series, not the gauge transport of the gate rows" is exactly
right.

### 2.5 Dropped scalar — REPAIRED (cosmetic)

R7R1's gate is `w_(n+22)' = -(n+2)q_n/16`; the report's `C_b` drops the
`-(n+2)/16`. Harmless: the factor is a nonzero rational in char 0, so
vanishing is unchanged, and multiplying a coefficient sequence by a polynomial
in `k` preserves D-finiteness. But `C_b` as printed is the bare class series,
not literally the `w`-solvability obstruction series, and the report should
say so.

## 3. Charge item 2 — algebraicity and whether reduction-based CT really proves it

### 3.1 Four-sections (2.1)–(2.3) — CONFIRMED

`Q_b(X,zeta u) = zeta^b Q_b(X,u)` verified by reindexing; `u^(-b)Q_b` is
manifestly a series in `u^4`. Sections of an algebraic **univariate** series
are algebraic (unlike diagonals of bivariate ones): each `Q(X,zeta^ell u)` is
algebraic over `K(zeta)(X,u)` and algebraic elements form a ring. Substituting
`u^4=z` (resp. `Hz`) keeps this over `K(zeta)(X,z)`, and descent to `K(X,z)`
by the Galois norm is standard. **CONFIRMED.**

`P^8 = sum_(i=0)^d F_i s^i P^i` has `P`-degree exactly `max(8,d)` with nonzero
leading coefficient in all three cases `d<8`, `d=8`, `d>8`. **CONFIRMED.**

### 3.2 The eliminant (2.4) — CONFIRMED, with a missing one-liner

The report asserts the elimination ideal is nonzero. It is, but the report
does not say why. Supplied: over `\bar{K(X,z)}` the fibre of the system over
each `(X,z)` is finite (`u`: ≤4 values; each `Y_ell`: ≤`D`; `Y` determined),
so the image in `(X,z,Y)`-space is 2-dimensional in a 3-fold, hence contained
in a hypersurface. Branch selection "by as many initial coefficients as
needed" is effective but the report prints no bound; recipe-level only.

### 3.3 Crude degree bound (2.5) — REPAIRED (R-2)

`4D^4` and `16D^4` are right for the stated adjunctions, and `16·14^4 = 614656`
checks. But `zeta` is adjoined in (2.1) and never charged. A fully safe crude
bound is `32 D^4 = 1229312`. Immaterial — the bound is explicitly crude and
used only for finiteness.

### 3.4 Theorem 4.1 and the descent (4.2)–(4.5) — CONFIRMED WITH REPAIR (R-1)

The chain is sound and I verified each link:

1. `Omega_b = p^(m_0) Y_b dX = S_b dX` — legitimate because `p^(m_0)` is
   `z`-free, so `∂_z^nu` commutes with it.
2. Existence of `L_z` with `L_z(Omega_b) = d_X B`: standard reduction-remainder
   pigeonhole in a finite-dimensional `K(z)`-space. **CONFIRMED** (this is the
   step the post-seal review correctly said was "an additional theorem").
3. Puiseux expansion + finite-trace descent (4.4): correct. `d_X` extends
   uniquely to the finite extension `M/L` in char 0 and commutes with
   `Tr_(M/L)`; `[M:L]` is invertible.
4. Regularity: if `eta_N` is regular on `U` and `g'=eta_N`, then `g` has no
   pole over `U`, because in char 0 a genuine pole of order `k>=1`
   differentiates to a pole of order `k+1`. **CONFIRMED.**
5. **R-1.** Step 4 gives `g ∈ O(V_H|_U)`. The report then jumps straight to
   `[p^(-m_0) eta_N dX] = 0 in V_(m_0)`. That needs `g` to lie in the single
   graded piece `p^(m_0) A`, and the report's justification is only the
   sentence "one may work in the selected field component and use (3.2)".
   The Opus5 torsor review explicitly warns that on **branch P** (`H=A^2`) the
   degree-four torsor is disconnected and `L=K(X)(p)` does **not** carry
   `p -> i p`, so no `mu_4` character projection is available. Supplied repair:
   the argument is purely **module-theoretic**, not automorphic. Let
   `e = [L:K(X)]`. Then `O(V_H|_U) = ⊕_(j=0)^(e-1) p^j A`, `p^e` is a **unit in
   `A`** (its `4/e`-th power is `H`, so its zeros lie in `Z(H)`), and `d`
   respects the grading because `p' = H' p/(4H)`. Since `eta_N` is a `K`-
   combination of `q_(b+4k) ∈ p^(m_0) H^(k-5) A ⊆ p^(m_0)A`, it is homogeneous;
   project `g` onto the piece `j_0 = m_0 mod e`; then `f := p^(-m_0) g_(j_0) ∈ A`
   and `eta_N dX = p^(m_0) nabla_(m_0)(f) dX`. **No `mu_4` action and no
   connectedness is used.** With this inserted, the descent is CONFIRMED,
   including the fully degenerate case `L=K(X)` (verified on `H=X^4`, desk
   check G).
6. `pi_(m_0)` is `K`-linear and `L_z` acts on `z`-coefficients by `K`-linear
   shift-and-scale, so `pi_(m_0) ∘ L_z = L_z ∘ pi_(m_0)` coefficientwise;
   (4.5) follows. **CONFIRMED.**

The report's §3.2 diagnosis — `lambda_i` is `K`-linear, not `K(X)`-linear,
which is exactly why the raw `q_n` P-recurrence cannot be pushed through
`pi_(m_0)` — is correct and is precisely the objection raised by the post-seal
review. The producer answers it rather than evading it.

Also confirmed, and worth flagging as an improvement: the report's proof of
`q_n ∈ p^(n+2)A` via `F^((n+2)/8) = p^(n+2)(1+sum F_i H^(-2) t^i)^((n+2)/8)`
needs **no deck automorphism**, so it survives on branch P where the earlier
character-based argument does not. **CONFIRMED.**

## 4. Reproducible desk-check section

All scripts are pure-Python + `fractions`, no CAS, no network, seconds of
runtime. Staged at `/tmp/r8_desk.py`, `/tmp/r8_deskB.py`, `/tmp/r8_deskG.py`.

### 4.1 (1.1) and (1.2) re-derived by independent series reversion

I did **not** reuse the Lagrange formula as an input. I solved
`P^8 = X^8 + F_1 s P` for `P ∈ K(X)[[s]]` with `P(0)=p` by Newton iteration
over Laurent polynomials in `X`, formed `Q=P^2`, and compared with
`q_n = 2/(n+2) [t^n] F^((n+2)/8)`.

```text
[F1 = 4X^4]      Lagrange (1.1) == reversion of P^8=F(X,sP), n=0..7   : True
[F1 = 4X^4]      (1.2) all X-exponents == n+2 (mod 4), n=0..7          : True
[F1 = X^4+X^8]   Lagrange (1.1) == reversion, n=0..7                   : True
[F1 = X^4+X^8]   (1.2) all X-exponents == n+2 (mod 4), n=0..7          : True

q0..q4 on F = X^8+4X^4 t :  X^2,  X^-1,  -X^-4,  (11/8)X^-7,  -(15/8)X^-10
```

`q0=X^2` and `q1=1/X` reproduce R7R1's load-bearing counterfixture exactly.
`q3=(11/8)X^-7` also reproduces the `q3` closed form quoted in the Fable5
review (`p^5[F3/(4H^2) - 3F1F2/(32H^4) + 11F1^3/(512H^6)]` at
`F1=4X^4, F2=F3=0`). **Both are cross-validated by a path independent of both.**

### 4.2 The typing (3.4)–(3.5) reproduces R7R1's exactness verdicts

On `H=X^4`: `A=K[X,X^-1]`, `nabla_m(X^a)=(a+m)X^(a-1)`, so `V_m=K·[X^(-m-1)]`,
`dim V_m = 1`. That agrees with (3.3): `r=1`, `e_1=4`, `k_m=1` always, so
`r-1+k_m = 1`.

```text
row n=0 : p^-22 q_0 = X^-20  -> lambda_22 = 0  -> EXACT
row n=1 : p^-23 q_1 = X^-24  -> lambda_23 = 1  -> NONZERO CLASS
row n=2 : p^-24 q_2 = -X^-28 -> lambda_24 = 0  -> EXACT
row n=3 : p^-25 q_3 = (11/8)X^-32 -> lambda_25 = 0 -> EXACT
```

R7R1: *"`q0=X^2` is exact, but `q1=1/X` has nonzero residue."* **MATCH.**
Also verified: `m=n+2` and `m=n+22` give identical verdicts for `n=0..11`.

### 4.3 Numerical separation of the transported and literal series

Fixture `H=X^4`, `F = X^8 + (X^4+X^8)t`, sector `b=1` (`m_0=23`, `j=3`).
With `A_n = (2/(n+2)) binom((n+2)/8, n)`, the coefficients are
`A_(4k+1)·C(4k+1, k+1)` (correct) versus `A_(4k+1)·C(4k+1, 2k+1)` (literal):

```text
k :  correct C_1[k]                literal (3.11)[k]
0 :  1/4                           1/4
1 :  1275/65536                    1275/65536
2 :  -77626185/2147483648          -232878555/4294967296     <- ratio 3/2
3 :  -4572409616775/281474976710656 -2743445770065/70368744177664
```

Agreement at `k=0,1` is the numerical accident `C(5,2)=C(5,3)=10`. From `k=2`
the two series genuinely differ. **The producer's repair changes the object,
not just the notation.**

### 4.4 Gauge identities, verified as rational-function identities

Certified by exact evaluation at 40 random rational points (degrees bounded):

```text
(3.6)  nabla_m0(H^k f) = H^k nabla_(m0+4k)(f)      k=1,2,5 ; m0=22..25   PASS
       T_m(HY) = H T_(m+4)(Y)                      m=17,22,23,30         PASS
       T_m = 4H nabla_(m-12)                       m=22,23,30            PASS
(3.2)  d(p^m f) = p^m nabla_m(f)  on p=X, H=X^4    m=22..25              PASS
```

The last line is the degenerate branch where `L=K(X)` has **no** `mu_4` action
at all, confirming the R-1 module-grading repair is what carries (3.2)/(4.5),
not connectedness.

### 4.5 Coefficient extraction (6.2)–(6.3) and the order-bound counting

```text
(6.2) verified exactly on c=(1-z)^-2 annihilated by (1-z)d_z - 2       PASS
      -> shifts: A_1(N)=N+1 (ell_max=1), A_0(N)=-(N+2)

rational (n=1) degeneration of (5.1): f = 1/(X^2-z)
  d_Hermite = X^2-z (squarefree, deg_X=2), no polynomial part, dim N_V=0
  (5.1) predicts R <= 1*2 + 0 = 2
  exact certificate: (d_z + 1/(2z)) f = d_X[ -(1/(2z)) X/(X^2-z) ]      PASS
  actual order 1 <= 2                                                    consistent
```

### 4.6 Arithmetic

```text
D = max(8,14) = 14 ;  4D^4 = 153664 ;  16D^4 = 614656  (report's value)  OK
fully safe crude bound including K(zeta): 32D^4 = 1229312                (R-2)
linear-vacuity window: m>=28  <=>  n>=6 ; on branch P k_m=1 <=> m even   OK
```

## 5. Charge item 3 — the order bound `R <= n deg_X(d_Hermite) + dim N_V`

**Form: CONFIRMED (re-derived).** After algebraic Hermite reduction the
remainder is `(sum_(i=1)^n num_i · omega_i)/d_Hermite` with `omega_i` an
integral basis of degree `n = [E:K(z)(X)]` and `deg_X num_i < deg_X d_Hermite`,
contributing `n · deg_X(d_Hermite)` dimensions; polynomial reduction against a
basis integral at infinity leaves the finite complement `N_V`. The first
`K(z)`-dependence among the reduced `∂_z^nu Omega_b` therefore occurs by
`R <= n deg_X(d_Hermite) + dim N_V`. It degenerates to the classical rational
bound (verified, §4.5).

**Hypotheses: correctly transferred.** `Omega_b` is an algebraic differential
in one integration variable `X` with one parameter `z` — literally CKK's
setting. The `nu`-independence of the remainder space rests on the standard
fact that `∂_z` raises pole orders only at the *same* fixed places of
`E/K(z)`, which Hermite reduction returns to simple. I found no
mis-transferred hypothesis.

**Attribution: GAP.** I cannot verify offline that this is *Corollary 15* of
arXiv:1602.00424, nor that paper's precise hypothesis list. Recommend the
canonical record cite it as "the reduction-remainder dimension count of
Chen–Kauers–Koutschan 2016 (numbering unverified in review)".

**Variables: REPAIRED (R-4).** `n` in (0.1)/(5.1) is the field degree, while
`n` in §1–3 is the row index; `N` is the Puiseux index in (4.3) and the
recurrence index in §6; `R` collides with `R_Q`. No mathematical consequence,
but in a report whose thesis is that a typing conflation cost the campaign a
theorem, this needs fixing before promotion.

## 6. Charge item 4 — finite prefix and singular indices

* (6.2)/(6.3) — **CONFIRMED**, verified numerically.
* Forward propagation past the last nonnegative root of `A_ellmax` —
  **CONFIRMED**. The induction is sound for `ell_max` of either sign, since
  every other term has strictly smaller index.
* (6.4) as printed — **REPAIRED (R-3)**. If `A_ellmax` has no nonnegative root
  the "last root" term is undefined and the formula degenerates; and indices
  `< ell_max` must be covered. Correct display:
  `N0 = max(startup indices, ell_max - 1, rho + ell_max)` with `rho` the last
  nonnegative root when one exists. The report hedges ("compute the precise
  dependency graph rather than blindly use this coarse display"), so this is a
  recipe defect, not a theorem defect. Termination is CONFIRMED.
* "One operator annihilates the whole vector, so one `N0` decides all
  coordinates" — **CONFIRMED.**
* **Missing scope line:** `N0` is per-residue `b`. Deciding the tower needs
  `max_(b in Z/4) N0^(b)`. The report never says this.
* §7.1's "decidable by finite exact algebra" — **CONFIRMED**, and correctly
  firewalled in the same paragraph as saying nothing about polynomial-window
  descent, mixed `G` rows, or `D22=1`.

## 7. Charge item 5 — generic parameter cell, and refusing a uniform `N0`

* Generic theorem over `K(S)` — **CONFIRMED.** Theorem 4.1 applies verbatim
  with `K` replaced by the computable char-0 field `K(S)` (`S` irreducible).
  Because `H` stays in `K[X]`, `dim V_(m_0) = r-1+k_(m_0)` is unchanged and a
  basis `e_i` can be taken in `A_K`, so the coordinates `c_(i,k)` are
  polynomial in the parameters. **CONFIRMED.**
* Specialization on the open locus where denominators, integral-basis pivots
  and the leading coefficient survive — **CONFIRMED.** The identity
  `L_z(S_b) = ∂_X B` is an identity of series with parameter-rational
  coefficients; specializing where nothing blows up preserves it.
* One clarification: §7.2's "a generic operator is not evidence on its
  exceptional locus" is right about *that operator*, but D-finiteness itself
  still holds at every exceptional point by §7.1 (with a possibly larger
  operator). As written it invites the opposite reading. **REPAIRED
  (clarification).**
* Refusal of a uniform `N0` via `A(N,theta) = N - theta` — **CONFIRMED**, and
  I can strengthen it: the set of bad specializations is
  `∪_(N>=0) {theta : A_ellmax(N,theta) = 0}`, a **countable** union of proper
  closed sets. It is not closed, so this route yields no Zariski-open uniform
  bound at all — not merely "an extra theorem is needed". (Over an uncountable
  field a *very general* uniform bound could still exist; it would not be
  constructible.) The producer's refusal is correct and, if anything,
  understated.
* Noetherian stabilization of `I_N = (c_(i,0),…,c_(i,N))` — **CONFIRMED**, and
  it matches the corrected version in the Fable5 review §3 (as opposed to the
  refuted Krull-separation argument). Correctly labelled non-effective.
* §7.3, varying `H` — **CONFIRMED.** When `H` varies, `r` and `k_m` jump, the
  cover's component count can change, and there is no fixed basis (3.12), so
  no unstratified claim. Consistent with the confirmed de Rham codimension law.

## 8. Charge item 6 — firewalls

Checked one by one; **all hold**.

1. **Linear-vacuity reconciliation (§8) — CONFIRMED.** `m>=28 <=> n>=6`;
   on branch P `k_m=1 <=> m` even. The linear-vacuity normalization
   `p^(-m)(q_n)_lin = F_n/(4H^7)` is *termwise identical* to the producer's
   `c_(b,k)`, so the two theorems are stated in the same presentation and
   there is no conflict: (8.1) is a statement about `∂/∂F_n` of one
   coefficient, Theorem 4.1 about the whole sequence including nonlinear
   carry. Item 4 ("for `n>=15` the frozen upper window has no new `F_n` block")
   matches the frozen slot table `n=1..8: 16,15,14,13,12,11,10,9`,
   `n=9..14: 7,6,5,3,2,1`, `n>=15: 0`.
2. **Row independence — NOT IMPLIED. CONFIRMED.** A recurrence for the class
   coordinates says nothing about whether successive rows cut new conditions
   on the 124 positive-`F` slots. Receiver dimension remains a capacity
   ceiling (confirmed torsor budget theorem), never realized codimension.
3. **Nonlinear nonvacuity — NOT IMPLIED. CONFIRMED.** D-finiteness is
   compatible with the entire tail being identically zero.
4. **Polynomial descent — NOT IMPLIED. CONFIRMED.** Everything here lives on
   `A = K[X,H^-1]`. R7R1 gives polynomial-row solvability ⟹ class gate; the
   converse over the frozen polygon windows is unproved, and the report lists
   "equality between localized class gates and polynomial-window cokernels"
   among its non-results. Correct.
5. **Endpoint / `D22=1` / `D1..D21` / GGV family / Keller / JC2 — NOT IMPLIED.
   CONFIRMED.** §9's non-results list is complete and I found no sentence
   elsewhere in the report that leaks past it.
6. **No numerical `N0` is printed.** Correct, and correctly explained: no full
   `F` point was charged. The report is a **theorem plus an algorithmic
   recipe**, not an executed computation — the distinction is maintained
   throughout (§5 "no heavy computation is needed to prove the theorem;
   producing a useful small operator … is a separate exact-computation task").

**Pointwise vs family-uniform**, restated cleanly:

```text
PROVED, pointwise           D-finiteness / P-recursiveness at any fixed (H, F-point)
PROVED, pointwise-effective an N0 computable at that point (per residue b)
PROVED, generic             operator + order bound over K(S) on an irreducible cell
NOT PROVED                  a numerical N0 valid across a positive-dimensional cell
NOT PROVED                  anything unstratified in H
NOT PROVED                  any statement about realized codimension or JC2
```

## 9. Itemized disposition

| Assertion | Verdict |
|---|---|
| (1.1) Lagrange–Bürmann all-`n` formula | CONFIRMED (re-derived by independent reversion) |
| (1.2) `q_n ∈ p^(n+2)A` without a deck automorphism | CONFIRMED |
| (1.3) `P` algebraic of degree `max(8,d)` | CONFIRMED |
| (2.1)–(2.3) four-sections algebraic | CONFIRMED |
| (2.4) elimination gives a nonzero annihilator | CONFIRMED (report omits the dimension one-liner) |
| (2.5) `4D^4` / `16D^4 = 614656` | REPAIRED — `zeta` uncharged; safe value `32D^4` |
| (3.2) `d(p^m f) = p^m nabla_m(f)` | CONFIRMED |
| (3.3) `dim V_m = r-1+k_m` | CONFIRMED (matches the confirmed codimension law; rechecked on `H=X^4`) |
| (3.6) `H^k` gauge intertwiner | CONFIRMED |
| (3.7)/(0.2) transported coefficient is `p^(-m_0)q_(b+4k)` | **CONFIRMED — the real repair** |
| `sum H^k q_(b+4k) z^k` is a different series | CONFIRMED (numerically separated at `k=2`) |
| (3.9) sector is `n+2 mod 4`, not `n` | CONFIRMED as mathematics; **novelty overstated** (already in `0ccdc259…` §7) |
| (3.10)/(3.11) redefined-`q` and literal typings | CONFIRMED |
| §3.2 `lambda_i` `K`-linear ⇒ raw recurrence does not push through | CONFIRMED |
| **Theorem 4.1** (D-finite / P-recursive fixed-receiver coordinates) | **CONFIRMED WITH REPAIR (R-1)** |
| Puiseux + trace descent (4.3)–(4.4) | CONFIRMED |
| Descent into the *selected component's graded piece* | REPAIRED — needs `O=⊕p^jA`, `p^e ∈ A^×`; supplied here |
| (4.5) `L_z C_b = 0` | CONFIRMED |
| §4.2 period reading | CONFIRMED (correctly non-load-bearing) |
| (5.1) order bound, structural form | CONFIRMED (re-derived; validated at `n=1`) |
| (5.1) attributed to CKK "Corollary 15" | **GAP** — unverifiable offline |
| (5.1) variable transfer | REPAIRED (R-4) — `n`, `N`, `R` collisions |
| (6.2)/(6.3) coefficient extraction | CONFIRMED (verified) |
| (6.4) prefix bound | REPAIRED (R-3) — missing `ell_max-1` floor; missing `max` over `b` |
| §6 termination | CONFIRMED |
| §7.1 fixed-point decidability | CONFIRMED |
| §7.2 generic operator + bound over `K(S)` | CONFIRMED |
| §7.2 refusal of a uniform numerical `N0` | CONFIRMED (and strengthened: bad set is a countable, non-closed union) |
| §7.2 Noetherian non-effective existence | CONFIRMED |
| §7.3 stratification required when `H` varies | CONFIRMED |
| §8 compatibility with linear vacuity | CONFIRMED |
| §9 non-results list | CONFIRMED complete |
| Any row-independence / nonvacuity / descent / endpoint / JC2 consequence | **NONE — correctly disclaimed** |

## 10. Promotion recommendation

**Promote Theorem 4.1 and its normalization, at fixed-instance and
generic-cell scope, after the four repairs are folded in.** This review is a
genuinely independent different-model leg: the producer is Sol Ultra, I am
Opus 5, I verified the charged hash before reading, and the load-bearing
checks (series reversion for (1.1)/(1.2); the `H^k` cancellation re-derived in
Fable5's `T_m` convention rather than the producer's; the numerical separation
at `k=2`; the module-grading descent; the rational-degeneration validation of
(5.1)) were all carried out from primitives rather than replayed.

Promote as:

> **Fixed-receiver sector recurrence theorem.** Fix a computable char-0 field
> `K`, `H ∈ K[X]\{0}`, `A=K[X,H^-1]`, `F = H^2 + sum_(i=1)^d F_i t^i`, `p^4=H`,
> and let `Q=P^2=sum q_n s^n` come from `t=sP`, `P=F^(1/8)`. For `b ∈ Z/4` put
> `m_0=b+22` and `C_b(z) = sum_k [p^(-m_0) q_(b+4k) dX] z^k`, valued in the
> finite-dimensional `V_(m_0)=coker(nabla_(m_0))`, `dim V_(m_0)=r-1+k_(m_0)`.
> This — **not** `sum_k H^k q_(b+4k) z^k` — is the `H`-gauge transport of the
> licensed gate rows into one fixed receiver, and its row sits in connection
> sector `b+2 (mod 4)`. Then every scalar coordinate of `C_b` is D-finite over
> `K(z)` and P-recursive; a single nonzero telescoper annihilates all of them;
> it is computable by algebraic Hermite plus polynomial reduction on the
> four-section, with order at most (field degree)·`deg_X(d_Hermite) + dim N_V`;
> and after singular-index analysis a finite prefix `N0` decides the whole
> infinite tower at any charged point. The same holds over `K(S)` at the
> generic point of an irreducible parameter cell with `H` fixed. **No
> numerical campaign `N0`, no cell-uniform `N0`, no unstratified statement in
> `H`, no row independence, no nonlinear nonvacuity, no polynomial-window
> descent, no endpoint verdict, and no JC2 consequence follows.**

Do **not** promote: the sector shift as a novel result (it is the confirmed
torsor theorem's `m mod 4`); the CKK corollary number; (6.4) verbatim; or any
sentence reading "the frozen family is decided by row `N`".

Cheapest honest successor, agreeing with the producer's §9 with two additions:
preregister the exact receiver index, the `p^(-(b+22))S_b` normalization, the
selected irreducible four-section factor and its `z=0` branch, the
Hermite/polynomial bases and the (5.1) instance, the singular-index `N0`
**maximized over `b`**, and mutation controls including *"`H^k` applied to
`q` instead of to the de-`p`-powered representative"* — which §4.3 above shows
is a live, non-vacuous mutation that changes the series at `z^2`. Run it on
one already-pinned survivor cell of branch P with `H=(X^4-1)^2`, smallest
receiver first, under the AWS-only heavy-computation rule.

## 11. Process disclosure

Read: the charged report and exactly the five files it cites, all hash-matched
to its custody block. No globbing, no repository traversal, no `jc2-lean`
access, no `…T2255Z*`/`…T2259Z*` file, no canonical file read or edited, no
AWS. Local computation: exact rational desk arithmetic, three short scripts,
seconds of runtime, no CAS. Exactly one output file was written, this one.
I did not audit the producer's claim that it wrote exactly one file.

Self-hash convention: the SHA-256 below is of this file's bytes **up to and
including the newline preceding the final line**, i.e. everything above the
`sha256(body)` line. Reproduce with

```text
sed '$d' xmodel/ggv-quarter-root-sector-gate-rec-theorem-r8-crossreview-opus5-20260827.md | shasum -a 256
```

sha256(body) = aef5fa1ae63499c5d8f71f755c6845075768db0818febca767d96f8ca1de80c4
