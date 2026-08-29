# Hostile review: general-squarefree Keller-face rational-mode theorem R4

**Reviewer:** Grok 4.6 (independent hostile referee). **Date:** 2026-08-27.  
**Target:** the charged freeze of Sol's additive R4 general-squarefree transport

`cases/ggv_keller_face_general_squarefree_modes_r4_20260827/`  
together with `xmodel/ggv-keller-face-general-squarefree-rational-mode-theorem-r4-sol-20260827.md`.

**Additive follow-up, not a retrial of R3 and not an import of the endpoint
criterion as a jet theorem.** The completed R3 hostile review

```text
27fcd25640f62a92c147863e7a8ef8ca4b7b004f05d54450c8d2d8811c97cdc6
  xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-hostile-review-grok-20260827.md
```

confirmed only the rational-mode normal form and squarefree replacement-edge
exclusion at the single polynomial `H=X^8-1`. That verdict is preserved and
is **not** evidence for a general-`H` statement. The separately audited
endpoint criterion

```text
d382c21f416afdc150d621506c38076aa4ec2b96e4680c0a938ddd56f06394ed
  xmodel/ggv-superelliptic-endpoint-criterion-hostile-audit-actual-20260827.md
```

is a theorem about the rational ODE `2Hg'+H'g=2H` after the change
`g=-8H^2d`. It explicitly left general-`H` mode completeness and denominator
provenance **OPEN**. R4 is reviewed only as a self-contained derivation in
`K(X)[[t]]` that claims to close that mode/provenance gap on the squarefree
locus, and to stop on the first perfect-square resonance.

**Claim under review (narrow):** over a characteristic-zero field `K`, for
every nonconstant squarefree `H∈K[X]` of degree at least two, there is no
polynomial-`X` formal jet `F,G∈K[X][[t]]` with `F_0=H^2`, `G_0=H^3`, and
`E=12F_XG-8FG_X-t(F_XG_t-F_tG_X)=t^{22}+O(t^{23})`. The argument is that the
six homogeneous rational modes of R3 remain complete through weight 22 for
every such `H`, including the negative-power modes, after which the endpoint
pole reduction still yields `4HY'+6H'Y=1` with no polynomial `Y`. Degree one
is charged only as endpoint silence. Separately, `H=X^2` with `F=X^4` admits
the new exact homogeneous mode `t^{22}F^{-5/4}=t^{22}X^{-5}`. **Not** under
review: raw `2S/3S` provenance, a genuine GGV family, a Keller pair, landing,
`G2-PSC`, `G2-BD`, cofinality, or JC2.

**Method.** Rehashed the five charged artifacts, the four freeze-internal
lines, and every dependency pinned by R4. Independently constructed the
formal square-root branch in `K(X)[[t]]` for split, irreducible, and linear
`H`; independently differentiated `E(F,t^n F^γ)`; independently expanded the
first residual from `F_0=H^2` only; independently solved the logarithmic ODE
in `K(X)` at every `K`-irreducible, at infinity, and for constant `H`;
independently traced denominators of the six displayed modes; independently
expanded the weight-22 operator, the change `g=-8H^2d`, the local coefficient
`8m-20`, the substitution `d=-Y/(2H)`, and the degree law for `M`. Desk-scale
exact arithmetic in `Q[X]` and truncated series in `Q(X)[[t]]/(t^7)` were
used as mutation guards, not as the proof. Producer `PASS`, the Python
tables, and the completed R3 review were not used as evidence for the
general-`H` transport. No AWS, no CAS, no producer-file edits, no
canonical-ledger edits, no `jc2-lean` access.

**Firewall.** The maximum permitted R4 verdict is the artificial
`F_0=H^2`, `G_0=H^3` formal replacement-edge theorem for arbitrary nonconstant
squarefree `H` of degree at least two, plus the nonsquarefree stop at
`H=X^2`. A complete rational-mode normal form is not a polynomial
source/target cleanup. A square/cube leading face is not a Keller jet.

---

## Verdict table

| Item | Verdict |
|---|---|
| 1. Custody and additivity over R3 | **CONFIRMED** |
| 2. Identity `E(F,t^n F^γ)=t^n F^γ F_X(12-8γ-n)` and subtraction of `F^{3/2}` | **CONFIRMED** |
| 3. Complete rational kernel weights `0,4,8,12,16,20` through 22 | **CONFIRMED** |
| 4. Weight-22 endpoint, `g=-8H^2d`, and `4HY'+6H'Y=1` | **CONFIRMED** |
| 5. Pole provenance, local coefficient `8m-20`, `Hd` polynomial | **CONFIRMED** |
| 6. Degree cutoff `deg H≥2`, and degree-one silence only | **CONFIRMED** |
| 7. Nonsquarefree stop `H=X^2`, `t^{22}X^{-5}` | **CONFIRMED** |
| 8. Script versus omitted cases and hard-coded conclusions | **GAP/REPAIR** |
| 9. Scope / promotion boundary | **CONFIRMED** |

No theorem item is **REFUTED**. No smallest failing mode, weight, pole,
coefficient, field hypothesis, or omitted finite denominator was found inside
the charged squarefree jet statement. Item 8 is a verifier defect: the script
is a freeze lock with several tautologies and one false “dense polynomial
fixtures” comment. That defect is not a substitute for the identities, which
were rederived here and survive.

---

## Independent hashes

Recomputed SHA-256, all matching the charged prompt and the internal
`FREEZE.sha256` lines:

```text
11cad1dbdf3d49ffd5f15a84de2969fbb79ac7b134aea18e079061e109322f56
  xmodel/ggv-keller-face-general-squarefree-rational-mode-theorem-r4-sol-20260827.md
9235df1bb0fa7876befab39cf40fe2814186cfaa7eba5540415a42b203b7acf9
  cases/ggv_keller_face_general_squarefree_modes_r4_20260827/FREEZE.sha256
ccf8a0dbd492cccd3a026de542db377d790fed43058b4628e6900fda18ec9916
  cases/ggv_keller_face_general_squarefree_modes_r4_20260827/verify_r4.py
ea767e11f78f34705445640fd86574286b60bd2e631a4e177caf200fd173b7a4
  cases/ggv_keller_face_general_squarefree_modes_r4_20260827/RESULT_R4.json
25a34fcbbacc12506dbf4474de795b38f28bf9c156b9d3bc35c49c1e521f39a6
  cases/ggv_keller_face_general_squarefree_modes_r4_20260827/README.md
```

Freeze-internal lines, matching the live bytes of the four hashed producer
files:

```text
ccf8a0dbd492cccd3a026de542db377d790fed43058b4628e6900fda18ec9916  verify_r4.py
ea767e11f78f34705445640fd86574286b60bd2e631a4e177caf200fd173b7a4  RESULT_R4.json
25a34fcbbacc12506dbf4474de795b38f28bf9c156b9d3bc35c49c1e521f39a6  README.md
11cad1dbdf3d49ffd5f15a84de2969fbb79ac7b134aea18e079061e109322f56  ../../xmodel/ggv-keller-face-general-squarefree-rational-mode-theorem-r4-sol-20260827.md
```

Pinned dependencies, all matching the live bytes. These pins are custody
only. None of their mathematical conclusions is imported as evidence for the
general-`H` transport:

```text
e752b86b5a8953649a3ce8c55379d18eca2dc1bdc8ab4fcd030c63dd64071823
  cases/ggv_8_28_keller_face_rational_mode_exclusion_r3_20260827/FREEZE.sha256
b1851156c83657fa85eb875df7e191a99fd339bfcb79ca1a752742ddff9f70b7
  xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-sol-20260827.md
27fcd25640f62a92c147863e7a8ef8ca4b7b004f05d54450c8d2d8811c97cdc6
  xmodel/ggv-8_28-keller-face-rational-mode-exclusion-r3-hostile-review-grok-20260827.md
1c17b61f00079802b20fc459550eea7bc7b09bcdcc98f27c233bde91cf348968
  xmodel/ideation-20260827T1349Z-opus5.md
d382c21f416afdc150d621506c38076aa4ec2b96e4680c0a938ddd56f06394ed
  xmodel/ggv-superelliptic-endpoint-criterion-hostile-audit-actual-20260827.md
```

Repository `HEAD` at review time: `418e413593120d19e15e6546eb50c985f4b1f038`.

A freeze-internal replay of `verify_r4.py` reproduces frozen `RESULT_R4.json`
byte-for-byte. That is custody consistency only. It is not evidence for any
identity below.

---

## 1. Custody and additivity — CONFIRMED

All five charged digests match the prompt. The four lines inside
`FREEZE.sha256` match the four hashed producer files. All five R4 pins match
the live bytes.

R4 lives in a new directory and a new sol report. It does not rewrite the R3
freeze, the R3 sol report, or the completed R3 review. Rollback as written —
delete only the new R4 case/report — is therefore possible. Additivity of
bytes is intact.

R4 is genuinely distinct from R3 rather than a silent scope rewrite of the
R3 *claim*. R3 charged, and only charged, `H=X^8-1`. The R3 review confirmed
that theorem and used `deg H=8` at the final degree law (`deg M=d+7`,
leading coefficient `4d+48`) and, in one sentence, `v_∞(H)=-8`. R4 does not
relabel those R3 sentences as already general. It pins R3 as the special
case, states that R3 itself “explicitly charged only `H=X^8-1`”, and keeps
canonical scope at that special case until this review. The degree law is
rewritten with a free `h=deg H`, which is the honest transport, not a
back-edit of R3.

History. Repository search for a general-squarefree rational-mode theorem,
for `F^{-5/4}`, and for a weight-22 perfect-square homogeneous mode hits the
charged R4 artifacts, the R4 review prompt, and a contemporaneous
coordination note that the R4 producer is frozen and unreviewed. It does not
hit an earlier campaign theorem. The completed R1 review explicitly refused a
statement about general squarefree `H`. Opus5 / the endpoint audit left
general-`H` mode completeness open. The six-mode display at arbitrary
squarefree `H`, the degree-one silence, and the stop example `(0.7)` are
therefore additive objects.

---

## 2. Linearization identity and `F^{3/2}` — CONFIRMED

**Hypotheses, used as such below.** `K` is a field of characteristic zero.
`H∈K[X]` is nonzero. `F,G∈K[X][[t]]` with `F_0=H^2` and `G_0=H^3`. The
ambient working ring is `K(X)[[t]]`, with commuting derivations `∂_X` and
`∂_t`. Squarefreeness, `deg H`, and the roots of `H` are not used in this
section. Characteristic not two is implied by characteristic zero and is
load-bearing for the square-root branch.

**Existence and uniqueness of `S=F^{1/2}` with `S_0=H`.** Write
`F=H^2(1+tW)` with `W∈K(X)[[t]]`. `H^2` is a unit of `K(X)`, so

```text
(1+tW)^{1/2} = Σ_{k≥0} binom(1/2,k) (tW)^k
```

is a well-defined formal series, uniquely determined by constant term `1`.
Thus `S:=H(1+tW)^{1/2}=H+O(t)` exists uniquely in `K(X)[[t]]`. Equivalently,
the recurrence `S_0=H` and `2H S_n=F_n-Σ_{i=1}^{n-1} S_i S_{n-i}` divides by
the unit `2H` at each step. The second formal square root `-S` is excluded
by `S_0=H` and independently by `G_0=H^3≠(-H)^3`. The construction is
purely formal: no analytic radius, no algebraic closure of `K`, and no
global polynomial square root. Coefficients `S_n` generally have denominator
a power of `H`.

Independent truncation on `H∈{X+1, X^2-1, X^2+1}` with a dense jet through
`t^3` recovered `S^2=F` through `t^6` in `Q(X)[[t]]`. Diagnostic only.

**`E` is linear in the second slot.** Put `R=G-F^{3/2}` in `K(X)[[t]]`. Let
`Q=F^{3/2}=F S`. The chain rule gives `Q_X=(3/2)F^{1/2}F_X` and
`Q_t=(3/2)F^{1/2}F_t`. Substitute:

```text
E(F,Q)
  = 12 F_X F^{3/2} - 8 F · (3/2) F^{1/2} F_X
    - t( F_X · (3/2) F^{1/2} F_t - F_t · (3/2) F^{1/2} F_X )
  = 12 F_X F^{3/2} - 12 F^{3/2} F_X
    - t · (3/2) F^{1/2} (F_X F_t - F_t F_X)
  = 0.
```

The first two summands cancel because `8·(3/2)=12`. The Jacobian block
cancels because `Q` is a composite of `F` alone. Thus `E(F,G)=E(F,R)`.
Independent truncation recovered `E(F,F^{3/2})=0` through `t^6` on the same
three `H`. Diagnostic only.

**The homogeneous identity.** Let `n∈Z` and `γ∈Q`, and set `Z=t^n F^γ`
whenever the binomial series of `(1+tW)^γ` exists in the ambient ring
(always, in characteristic zero, as a formal series in `t` with coefficients
in a finite extension of `K(X)` generated by `H^{2γ}`; for the kernel modes
below, `2γ` is an integer and the coefficients already lie in `K(X)`). Then
`Z_X=t^n γ F^{γ-1} F_X` and
`Z_t=n t^{n-1} F^γ + t^n γ F^{γ-1} F_t`. Substitute into `E`. The two
`γ F^{γ-1} F_X F_t` Jacobian terms cancel, leaving the identity of formal
series

```text
E(F, t^n F^γ) = t^n F^γ F_X (12 - 8γ - n).
```

The kernel condition is `γ=(12-n)/8`. This uses only differential algebra
and the weights `(12,8)`. It does not use squarefreeness, degree, or roots.

Independent truncation guards, all in `Q[X][[t]]` or `Q(X)[[t]]` through
`t^6` or `t^8`, on split and irreducible quadratic `H` and on `H=X+1`:

- `E(F,F)=4 F F_X` (`γ=1`, `n=0`);
- `E(F,t^4 F)=0`;
- `E(F,t^3 F)=t^3 F F_X` (`12-8-3=1`), guarding a dropped `n` or a swapped
  `8γ`;
- `E(F,S)=8 S F_X` (`γ=1/2`, `n=0`);
- `E(F,S^{-1})=16 S^{-1} F_X` (`γ=-1/2`, `n=0`);
- `E(F,F^{-1})=20 F^{-1} F_X` (`γ=-1`, `n=0`);
- `E(F,t^8 S)=0` on `H=X^2+1`.

The negative-exponent cases exist because `F_0=H^2` is a unit of `K(X)`, so
`F` is a unit of `K(X)[[t]]`. One is not inverting a series with vanishing
constant term.

The constant field of `K(X)` under `d/dX` is `K` in characteristic zero.
That fact is not required for the identity of this section; it is used in
§3.

---

## 3. Complete rational kernel through weight 22 — CONFIRMED

Suppose a residual `D∈K(X)[[t]]` vanishes below weight `n`, so
`D=t^n r_n+O(t^{n+1})` with `r_n∈K(X)`. Write `F=H^2+t F_1+···`. Collecting
`t^n` in `E(F,D)`:

- `12 F_X D` contributes `12·(2HH') r_n=24 H H' r_n`;
- `-8 F D_X` contributes `-8 H^2 r_n'`;
- `-t F_X D_t` contributes `-2n H H' r_n`;
- `+t F_t D_X` starts at order `n+1`, because `F_t` has `t`-valuation `0`
  and the extra `t` pushes it to `n+1`.

Every positive-grade `F_k` likewise lands at order `≥n+1`. Therefore

```text
E_n = (24-2n) H H' r_n - 8 H^2 r_n'
    = 2H ( (12-n) H' r_n - 4 H r_n' ).
```

This formula uses only `F_0=H^2` and characteristic not two. Independent
truncation with `F=H^2+t F_1+t^2 F_2` and `G=t^n r` for `n=0..4` on
`H∈{X+1,X^2-1,X^2+1}` recovered exactly this `t^n` coefficient, with all
lower coefficients zero.

`K(X)` is a field and `2H≠0`, so `E_n=0` iff `(12-n)H' r_n-4H r_n'=0`. For
`r_n≠0`,

```text
r_n'/r_n = q_n H'/H,    q_n=(12-n)/4.
```

**Every nonzero rational solution is `r_n=c H^{q_n}` with `c∈K`.** This is
the step that must survive a non-algebraically-closed constant field, poles
at infinity, constants, and repeated factors.

*Finite `K`-irreducibles, no algebraic closure.* Write a nonzero `r∈K(X)` in
lowest terms as `r=c ∏ p^{e_p}` over monic irreducibles of `K[X]`. Then
`r'/r=Σ e_p (p'/p)`. Likewise `H'/H=Σ_p ord_p(H) (p'/p)`. The functions
`p'/p` for distinct monic irreducibles are linearly independent over `K`: if
`Σ c_p p'/p=0`, clearing the product of the `p` yields a polynomial identity
in which each `p` divides every summand except `c_p p'·(product of the
others)`, and `p` does not divide `p'` (each irreducible is separable in
characteristic zero). Matching coefficients therefore forces: the only
primes of `r` are the primes of `H`, and `e_p=q_n ord_p(H)` at each such
prime. Valuations of rational functions are integers, so `q_n ord_p(H)∈Z`
is necessary.

If `H` is squarefree then `ord_p(H)=1` at every prime of `H`, hence `q_n∈Z`
is necessary, and then `r=c H^{q_n}`. Equivalently, in the DVR at `p`,
`r'/r - e_p (p'/p)` is regular while `p'/p` has valuation `-1`, so the
equation `r'/r=q_n H'/H` forces `e_p=q_n`. This is a valuation statement,
not a residue-in-`K` statement. For a linear prime the two coincide; for
`deg p>1` the residue lives in the residue field, but the valuation match is
unaffected. The sol report’s phrasing “at every irreducible factor `p`”
(not “at every `K`-rational root”) is the correct generality. No splitting
of `H`, and no algebraic closure of `K`, is used.

Galois-unbalanced candidates cannot occur in `K(X)`. Over `Q`, a function
with different valuations at `i` and `-i` is not in `Q(X)`. The
`K`-irreducible form automatically enforces Galois invariance: the only
candidate built from `X^2+1` is a power of `X^2+1` itself. An extra finite
prime is visible as an extra summand of `r'/r`. Independent check:
`r=(X^2+1)X` does not satisfy `r'/r=(X^2+1)'/(X^2+1)`, and
`r=(X^2-1)/(X^2+1)` is not a `K`-multiple of `(X^2+1)'/(X^2+1)`.

*Infinity.* Logarithmic derivatives of rational functions are `O(1/X)` at
infinity and have no polynomial part. If `r=c H^{q_n} X^k` with an extra
power of the uniformizer at infinity, the leading `1/X` coefficients would
read `deg r=q_n deg H+k` versus `q_n deg H`. Matching forces `k=0`. There is
no further constraint and no extra polynomial factor. The R3 sentence
`v_∞(H)=-8` is the special case `deg H=8`; the general statement is
`v_∞(r)=-q_n deg H`, still automatic.

*Constants.* In characteristic zero, `{f∈K(X): f'=0}=K`. Thus `c` is a
constant of `K`, not a nonconstant with vanishing derivative. If `K` is
itself a function field in another variable, that variable is still constant
for `d/dX`. The constant field of `K(X)` under `d/dX` is exactly `K`, as the
sol report states.

*Nonconstancy.* If `H` is constant then `H'=0` and the first-residual
equation becomes `-4H r_n'=0`, so every weight has a constant rational
kernel. Nonconstancy is necessary and is charged.

*Repeated factors.* Squarefreeness is used exactly once in this section: to
conclude that `q_n` itself is an integer, rather than that `q_n e_p` is an
integer for each multiplicity `e_p`. For `0≤n≤22` the integral values are
exactly `n=0,4,8,12,16,20`. In particular `q_{22}=-5/2∉Z`, so weight 22 has
no nonzero rational homogeneous solution on the squarefree locus. The
repeated-factor relaxation is the stop of §7, not a hole in the squarefree
list.

*Exact lift and inductive subtraction.* At an integral `q_n` put
`γ_n=(12-n)/8`, so `2γ_n=q_n`. Writing `F=H^2 U` with `U∈1+t K(X)[[t]]`
gives `F^{γ_n}=H^{q_n} U^{γ_n}∈K(X)[[t]]` by the binomial series of `U`.
The identity of §2 says that the full series `t^n F^{γ_n}` vanishes
identically in `E`, not merely at its first coefficient. Subtracting
`c_n t^n F^{γ_n}` therefore:

- kills the leading residual at weight `n`;
- introduces no lower `t`-terms, so earlier custody is unchanged;
- does not change `E` at any weight;
- absorbs the higher coefficients of the mode into later residuals rather
  than into a second kernel at the same weight.

The modes are supported at distinct lowest weights, so the constants `c_n`
are unique. After the five positive subtractions one has the charged normal
form `(3.5)` in `K(X)[[t]]`. This is a differential-ring identity, not a
polynomial source transformation.

The negative-power modes at `n=16,20` are legitimate comparison objects for
a polynomial jet because `K[X][[t]]⊂K(X)[[t]]`, because `F_0=H^2` is a unit
of `K(X)`, and because `E` is linear in the second slot. High-order
`H`-poles in the tails of `F^{-1/2}` and `F^{-1}` are absorbed into later
coefficients of `D`, including `d`. They do not invalidate the subtraction.

---

## 4. Weight-22 endpoint — CONFIRMED

After the five positive modes are subtracted, `D=t^{22}d+O(t^{23})`. The
general first-residual formula of §3 at `n=22` is

```text
E_{22} = 2H((12-22)H'd - 4 H d') = -20 H H' d - 8 H^2 d'.
```

Signs match `(24-2n)=24-44=-20` and `-8`. Positive-grade `F_k` and the block
`t F_t D_X` start at `t^{23}`. The charged target `E=t^{22}+O(t^{23})` makes
the coefficient of `t^{22}` the constant polynomial `1`, so

```text
-20 H H' d - 8 H^2 d' = 1
```

in `K(X)`. This uses only `F_0=H^2` and the first-residual calculus. It does
not use squarefreeness, degree, or roots.

**Change `g=-8H^2 d`.** Differentiating gives
`g'=-16 H H' d - 8 H^2 d'`. Then

```text
2H g' + H' g
  = 2H(-16 H H' d - 8 H^2 d') + H'(-8 H^2 d)
  = -32 H^2 H' d - 16 H^3 d' - 8 H^2 H' d
  = -40 H^2 H' d - 16 H^3 d'
  = 2H (-20 H H' d - 8 H^2 d').
```

Thus, identically as rational functions,

```text
2H g' + H' g = 2H · E_{22}.
```

On the charged target `E_{22}=1` this is the audited endpoint ODE
`2Hg'+H'g=2H`. The sol report’s wording “always gives” the ODE is the
composition of this identity with the charged target; the identity itself is
`2Hg'+H'g=2H·E_{22}` for every nonzero `H` and every rational `d`. No
squarefree hypothesis is used. Independent evaluation on an arbitrary
rational `d` for every producer fixture and for `H=X^2` recovered the
identity. Mutating the prefactor from `-8` to `-4` breaks it. Mutating the
sign of the `-20` term makes `E_{22}≠1` on the linear survivor.

The repaired normalization of the endpoint audit is respected: on the
squarefree locus of §5 one will have `d=-Y/(2H)`, hence `g=4HY`, not the
unrepaired `g=HY`.

**Reduction to `4HY'+6H'Y=1`.** Assuming the pole conclusion `d=-Y/(2H)` of
§5 (proved there, not here),

```text
d' = -Y'/(2H) + Y H'/(2 H^2).
```

Substitute:

```text
E_{22}
  = -20 H H' · (-Y/(2H)) - 8 H^2 · (-Y'/(2H) + Y H'/(2 H^2))
  = 10 H' Y + 4 H Y' - 4 H' Y
  = 4 H Y' + 6 H' Y.
```

Define `M(Y):=4HY'+6H'Y`. The charged endpoint is `M(Y)=1`. The factor `2`
in `d=-Y/(2H)` is a normalisation matching this operator. Independent
substitution on linear, split-quadratic, irreducible-quadratic, and cubic
`H` recovered `E_{22}=M(Y)` exactly. On `H=aX+b` the choice `Y=1/(6a)` gives
`E_{22}=1` and `g=(2/3)H=4HY`.

This also matches the audited criterion: squarefree `H` has `A=1`, `B=H`,
and `M=4 N_H` with `N_H(v)=H v'+(3/2)H' v`, so `M(Y)=1` iff `1∈im(N_H)`
after `K`-scaling. Agreement is recorded; the proof above does not import
the criterion.

---

## 5. Pole provenance — CONFIRMED

**Finite poles of `d` lie over `H`.** Two independent arguments.

*(Mode trace.)* `d=[t^{22}](G-Σ modes)`. `G_{22}` is polynomial. Each mode
coefficient is built from polynomial `F_i` by the operations of §2: `F`,
`t^4 F`, and `t^{12}` are polynomial in `X`; `S=F^{1/2}` divides by `2H` at
each recurrence step; `F^{3/2}=FS` multiplies by a polynomial; `F^{-1}` is
`H^{-2}(1+tW)^{-1}`; `F^{-1/2}=S^{-1}` divides by `H`. Binomial coefficients
of `(1+tW)^γ` for `γ∈{3/2,1,1/2,0,-1/2,-1}` contribute only integers and
powers of `2`, invertible in characteristic zero, not new finite primes in
`X`. Cancellation of numerator and denominator can only remove poles.
Therefore every finite denominator of `d` divides a power of `H`.
Independent truncation of `S`, `S^{-1}`, `F^{-1}`, and `F^{3/2}` on
`H∈{X+1,X^2-1,X^2+1}` had all coefficient denominators a power of `H` times
a unit.

*(Regularity of `E_{22}=1`, even without the mode trace.)* Let `q` be a
finite irreducible with `v_q(H)=0` and `v_q(d)=-m`, `m≥1`. Then
`v_q(d')=-m-1` in characteristic zero (the leading term of `d'` is
`-m a q'/q^{m+1}` with `-m a q'≠0`). The summand `-8 H^2 d'` therefore has
valuation `-m-1`. The summand `-20 H H' d` has valuation `v_q(H')-m≥-m`,
strictly milder even if `q` divides `H'`. The `d'` term cannot cancel, so
`E_{22}` would pole at `q`. Distinct off-`H` places cannot cancel one
another.

Smallest attempted hidden-pole counterexamples, all of which *fail* (so are
not counterexamples to the lemma):

| `H` | `d` | what fails |
|---|---|---|
| `X^2-1` | `1/X` | `v_X(E_{22})=-2` |
| `X^2+1` | `1/X` | pole of `E_{22}` at `X` |
| `X^2+1` | `1/X+1/(X-1)` | two off-`H` poles, `E_{22}` still polar |
| `X(X-1)` | `1/(X-2)` | `v_{X-2}(H)=0` and `v_{X-2}(E_{22})<0` |

No cancellation producing a hidden finite pole of `d` off `H` was found. The
smallest off-`H` probe is `H=X^2-1`, `d=1/X`.

**Local coefficient `8m-20`.** At a simple zero of `H` (equivalently, in the
DVR at an irreducible `p` dividing squarefree `H`), `H` is a uniformizer
times a unit. Write `d=a H^{-m}+O(H^{1-m})` with `a` a unit. Then
`d'=a' H^{-m} - m a H' H^{-m-1}+···`. The `a'` contribution to `E_{22}` is
order `H^{2-m}`, strictly milder than `H^{1-m}` for `m≥1`. The two leading
terms are

```text
-20 H H' · a H^{-m} = -20 a H' H^{1-m},
-8 H^2 · (-m a H' H^{-m-1}) = 8 m a H' H^{1-m}.
```

Sum: `(8m-20) a H' H^{1-m}`. At a simple place `H'≠0` and `a≠0`, so the
leading polar term vanishes iff `8m-20=0`, i.e. `m=5/2`. That is not an
integer order of a rational function. For integer `m≥2`, `8m-20≠0`
(`m=2` gives `-4`). Regular `E_{22}=1` therefore forbids `m≥2`. For `m=1`
the same scalar is `-12`, and the contribution is regular of order `H^0`,
as required of a simple-pole particular solution. Independent Laurent check
on the uniformizer `H=X`: `E_{22}(X^{-m})=(8m-20) X^{1-m}` exactly for
`1≤m≤12`.

Target-weight mutation, same leading scalar `2(12-n+4m)`: at `(n,m)=(20,2)`
the scalar vanishes, recovering the exact mode `t^{20}F^{-1}∼t^{20}H^{-2}`;
at `(22,2)` it is `-4`. Weight 22 does not admit a double-pole homogeneous
solution on the squarefree locus.

On-`H` high-pole probe `H=X^2-1`, `d=1/(X-1)^3`: `v_{X-1}(E_{22})=-2=1-3`,
matching `H^{1-m}` with `8·3-20=4≠0`. Simple pole `d=1/(X-1)` is regular at
that place, matching `m=1`.

**`Hd` is polynomial.** `d` has no finite poles off `H` and at most simple
poles along `H`. `H` is squarefree, so the denominator of `d` in lowest
terms divides `H`. Clearing the missing factors of `H` into the numerator
gives `d=P/H` for some `P∈K[X]`. Characteristic not two lets us set
`Y=-2P∈K[X]`, i.e. `d=-Y/(2H)`, hence `Hd` is polynomial. The polynomial
part of `d` is included: `Y` may have any degree. Behaviour at infinity is
that of a rational function, already encoded by `deg Y`. This uses
squarefreeness twice: the local parameter has `ord(H)=1`, and one global
factor `H` clears all allowed poles. It uses no root locations or degree.

No hidden pole or cancellation producing a non-polynomial `Hd` was found.

---

## 6. Degree cutoff — CONFIRMED

Let `h=deg H≥1` and let `Y` be nonzero of degree `y` with leading
coefficient `ℓ≠0`. Then `4HY'` and `6H'Y` both have degree `y+h-1`, with
leading coefficients `4y·lc(H)·ℓ` and `6h·lc(H)·ℓ`. There is no cancellation
of top terms in characteristic zero: `4y+6h≠0`. Thus

```text
deg M(Y) = y+h-1,    lc M(Y) = (4y+6h) lc(H) lc(Y).
```

The formula includes `y=0`, where `Y'=0` and `M(Y)=6H'Y` has degree `h-1`
and leading coefficient `6h·lc(H)·ℓ`. Independent monomial checks
`Y=X^y` for `0≤y≤11` on linear, split-quadratic, irreducible-quadratic,
cubic, quintic, and degree-eight squarefree `H`, plus a dense cubic `Y` on
`H=X^2+1`, recovered the degree and leading coefficient exactly.

If `h≥2`, then `deg M(Y)≥1` for every nonzero polynomial `Y`, while
`M(0)=0`. So `M(Y)` cannot be the constant polynomial `1`. This is the
general-squarefree exclusion. It holds over every characteristic-zero field:
such a field contains `Q`, and a product of nonzero elements is nonzero. No
splitting of `H` is used.

If `h=1`, write `H=aX+b` with `a≠0`. Then `deg M(Y)=y`, so only a constant
`Y` can hit a degree-zero target. For constant `Y`, `M(Y)=6a Y`, hence
`Y=1/(6a)=1/(6H')` uniquely. Independent checks: `M(X+1,1/6)=1`; the same
for `(a,b)∈{(2,3),(-5,0),(1/4,-7)}`; no other tested constant works; a
nonconstant `Y` produces positive degree. Mutating to `Y=1/(4H')` fails.

Degree one is therefore exact endpoint silence, not existence of a
polynomial jet. Lifting the particular `d=-Y/(2H)` back through the six
rational modes while keeping `F,G` in `K[X][[t]]` is a different problem and
is not claimed. The sol report, README, and `RESULT_R4.json` all stay on
that side of the line.

This also agrees with the audited squarefree special case of `A∈im(N_B)`:
`A=1`, `B=H`, and `1∈im(N_H)` if and only if `deg H=1`.

---

## 7. Nonsquarefree stop — CONFIRMED

For a general factorization `H=∏ p^{e_p}=A^2 B` with `B` squarefree, the
first-residual equation of §3 is unchanged. A nonzero rational leading mode
at weight `n` exists iff `q_n e_p∈Z` for every `p`, equivalently iff `4`
divides `(12-n)e_p` for every `p`. That much of the nonsquarefree
classification is safe, and is not a pole/provenance theorem.

If `B` is nonconstant, some `e_p` is odd, hence coprime to `4`, so `4`
divides `12-n` and the leading rational weights through 22 remain
`0,4,8,12,16,20`. Weight 22 is still non-integral at that odd place
(`(12-22)·odd=-10·odd ≡2 mod 4`). Independent multiplicity inventory
`[2,1]` recovered exactly those six weights. This does **not** transport the
squarefree pole lemma: even-multiplicity places are no longer uniformizers,
and their endpoint poles must be reclassified. The sol report does not claim
otherwise.

If `B` is constant, every `e_p` is even. Already the smallest example
`H=X^2` has `q_{22}=-5/2` and `q_{22}·2=-5∈Z`, solved by `r_{22}=c X^{-5}`.
Direct substitution into the kernel equation:

```text
(12-22) H' r - 4 H r'
  = -10 · (2X) · X^{-5} - 4 · X^2 · (-5 X^{-6})
  = -20 X^{-4} + 20 X^{-4}
  = 0.
```

For the constant formal edge `F=X^4`, the identity of §2 with
`γ=(12-22)/8=-5/4` gives the exact charged mode
`t^{22} F^{-5/4}=t^{22} X^{-5}`. Independent checks: the kernel vanishes as
a rational function; `E_{22}` annihilates `X^{-5}`; a particular solution of
the inhomogeneous equation is `d=-1/(16X^3)`, with `g=-8H^2 d=X/2` and
`2Hg'+H'g=2H`; arbitrary multiples of `X^{-5}` may be added to `d`. Mutating
the exponent to `X^{-4}` breaks the kernel.

A multiplicity-two signature admits every even weight `0,2,...,22`. A
fourth-power signature admits every weight. Most importantly, weight 22
itself is resonant: the homogeneous kernel of the endpoint equation is no
longer zero, and the squarefree uniqueness/pole-provenance package cannot be
transported through this branch.

**What the example refutes.** It refutes any uniform `H=A^2B` transport of
the squarefree six-mode list *and* the squarefree pole lemma, including the
claim that weight 22 has no rational homogeneous mode for every nonzero `H`.
It refutes uniqueness of the weight-22 residual on the perfect-square
branch. It is the correct stop for a general nonsquarefree
mode/provenance theorem.

**What the example does not refute.** It does not refute the squarefree
theorem of §§3–6. It does not refute R3 at `H=X^8-1`. It does not refute the
leading-weight list when `B` is nonconstant. It does not refute the rational
endpoint ODE `2Hg'+H'g=2H` itself: that ODE remains true and, for `H=X^2`,
is solved by `g=X/2`. It does not produce a polynomial-`X` jet, a GGV
family, or a Keller pair.

---

## 8. Script — GAP/REPAIR

The script is a valid freeze lock. It rehashes the five pins, rebuilds
`RESULT_R4.json` in memory, and byte-compares the frozen file. Replay
succeeds. The following live checks inside it are genuine and matched an
independent rederivation:

- squarefree `gcd(H,H')=1` on the five named fixtures, including
  `1-X+X^3` and `1+X+X^5`;
- the degree/leading-coefficient law of `M` on monomials `Y=X^y`,
  `0≤y≤24`;
- the linear survivor `M_{X+1}(1/6)=1`;
- the pole scalars `8m-20` for `1≤m≤12`, nonzero for `m≥2`;
- the multiplicity inventories `[1,1,1]`, `[2,3,5]`, `[2]`, `[4]`;
- `q_{22}·2=-5` and `γ_{22}=-5/4`.

The following are not evidence, and two of them overclaim.

1. The loop `gamma=Q(12-n,8)` followed by `assert Q(12)-8*gamma-n==0` is
   tautological. It does not differentiate `E`. R3’s verifier had the same
   tautology; R4 does not repair it.
2. The comment “The endpoint change `g=-8H^2d` is checked on dense
   polynomial fixtures” is false. The code is

   ```text
   assert -32 - 8 == -40
   assert -16 == -16
   ```

   Those two integers are the correct coefficients of `H^2 H' d` and
   `H^3 d'` in `2Hg'+H'g`, but they are not an evaluation on any polynomial.
   The second assert is a tautology. This is the smallest failing
   script-level honesty defect.
3. The stop mutation is `assert -10*2 + (-4)*(-5)==0`, not a construction of
   the Laurent function `X^{-5}`.
4. Omitted as live algebraic objects, though not as holes in the theorem:
   an irreducible quadratic `H` (the fixtures `X^2-1` and `X^8-1` split over
   `Q`); a truncated `E(F,Z)` evaluation; an ODE solve of `(3.1)`; a
   polynomial model of mixed multiplicities.

These defects do not touch items 1–7 or 9. The identities were rederived
independently, including on `H=X^2+1` and on truncated series that the
script never builds. The repair, if desired, is to delete the dense-fixture
sentence and to evaluate `2Hg'+H'g-2H E_{22}` on an actual rational `d`, as
R3 evaluated `M` on dense `Y`. Promotion of the theorem does not wait on
that repair.

Live mutations run here, not in the producer script: flipping the sign of
`-20` breaks the linear survivor; replacing `-8` by `-4` in `g` breaks
`L(g)=2H`; `Y=1/(4H')` does not solve the linear endpoint; `X^{-4}` is not
the `n=22` kernel on `H=X^2`. All four mutations fail in the expected
direction.

---

## 9. Scope — CONFIRMED

The charged artifacts claim, and only claim:

1. the six-mode rational normal form through weight 22 for every nonconstant
   squarefree `H`, with the same exact `H^2/H^3` leading edge and charged
   operator;
2. exclusion of a polynomial-`X` formal jet with that leading edge and
   `E=t^{22}+O(t^{23})` when `deg H≥2`;
3. endpoint silence, not a constructed jet, when `deg H=1`;
4. the stop example `H=X^2`, `F=X^4`, `t^{22}X^{-5}`, as the obstruction to
   a uniform `H=A^2B` mode/provenance theorem.

The sol report, README, `RESULT_R4.json` `scope` / `rollback` /
`claims_not_made` fields, and the status string
`PASS-GENERAL-SQUAREFREE-MODES-AND-STOP-SQUARE-W22-RESONANCE` all stay
inside that firewall. They do not claim:

- existence of a polynomial jet for squarefree linear `H`;
- a general `H=A^2B` normal-form or pole/provenance theorem (the
  `B`-nonconstant leading-weight observation is scoped as the safe fragment
  that explains the stop, not as a mixed-multiplicity jet theorem);
- raw `2S/3S` polynomial-source provenance;
- landing a genuine complete GGV chain in this leading edge;
- a GGV-family exclusion, `G2-PSC`, `G2-BD`, a counterexample, cofinality,
  or JC2.

Until this review, the producer correctly left canonical scope at the
reviewed R3 theorem at `H=X^8-1`.

---

## Exact promotion boundary

**Promoted, as an additive theorem over reviewed R3.**

Let `K` be a characteristic-zero field and let `H∈K[X]` be nonconstant and
squarefree. Suppose `F,G∈K[X][[t]]` satisfy `F_0=H^2` and `G_0=H^3`. Then
in `K(X)[[t]]`, after subtracting the unique formal branch `F^{3/2}` with
leading term `H^3`, the complete list of rational homogeneous modes of
`E(F,·)` through weight 22 is

```text
t^4 F,    t^8 F^{1/2},    t^{12},    t^{16} F^{-1/2},    t^{20} F^{-1},
```

together with the already-subtracted `F^{3/2}`. Weight 22 has no nonzero
rational homogeneous solution. After those subtractions, `E=t^{22}+O(t^{23})`
if and only if `d=[t^{22}](G-Σ modes)` satisfies `-20HH'd-8H^2d'=1`,
equivalently `2Hg'+H'g=2H` under `g=-8H^2d`. Squarefreeness forces
`d=-Y/(2H)` for some `Y∈K[X]`, hence `4HY'+6H'Y=1`.

- If `deg H≥2`, no such polynomial `Y` exists. Therefore no such
  polynomial-`X` formal jet exists.
- If `deg H=1`, the unique polynomial solution is `Y=1/(6H')`. This is
  endpoint silence, not a constructed jet.

**Promoted as a stop, not as a theorem.** For `H=X^2` and `F=X^4`,
`t^{22}F^{-5/4}=t^{22}X^{-5}` is an exact rational homogeneous mode at the
charged weight. A uniform `H=A^2B` transport of the squarefree normal form
and pole lemma is therefore false on the perfect-square branch. No general
nonsquarefree mode/provenance theorem is promoted.

**Not promoted.** Raw provenance, a genuine GGV family, a Keller pair,
landing, `G2-PSC`, `G2-BD`, cofinality, JC2, existence of a polynomial jet
for linear squarefree `H`, and any mixed-multiplicity pole lemma.

No smallest failing coefficient or hypothesis was found inside this
boundary. The only GAP/REPAIR is the producer verifier’s tautologies and
false dense-fixture comment, which are not part of the theorem.

Maximum permitted verdict, and the verdict reached: the artificial
`F_0=H^2`, `G_0=H^3` formal replacement-edge theorem for arbitrary
nonconstant squarefree `H` of degree at least two, plus the nonsquarefree
stop at `H=X^2`.
