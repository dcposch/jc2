# Hostile review — Sol 56 `td=8` A-copy approximate-root persistence

Lane: Grok 4.6, different-model adversarial referee. Date: 2026-08-29 UTC.

Target: `xmodel/m2-td8-a-copy-tower-persistence-r1-sol56-20260829.md`.

The producer claim is treated as an allegation. Algebra is reconstructed
from the printed source and the four hash-pinned reviewed dependencies; it
is not accepted by agreement. No `jc2-lean` access, no web, no AWS, no
heavy CAS, no canonical edit, no commit or push. Arithmetic is desk
`int`/`Fraction` plus one-variable Taylor coefficients. Only this file is
written.

---

## 0. Custody

Producer full SHA-256, recomputed on this host *before* the file was
opened for mathematics:

```text
9ee0dcde58fa05bef85740467da6ff3d187e3b2ca10efcfe1c146b13359b815c  6300 bytes
```

matches the brief. Body hash of the 6162 bytes strictly before the
separator line `---`, including the newline after `repository.`:

```text
3b9c8cacb647579e02ca4b37e7950924636c5626909e9f1adf28252da17ed9a0
```

matches the report's own `Report-body SHA-256` line.

Hash-pinned reviewed dependencies, recomputed this session, all MATCH:

```text
910d3216ad7476b743eb920e3d68026f05efc8ffe1a409c476fb90ce277f6ad4  st39 transport primary (Fable)
e469e94dbf4393fe820345678c2582ca7f7a528695c25d065fb224b4f796cf61  st39 transport review (Opus)
991e1b350ad2f8b2b82808fdc84dec71154f9ae17250c18953a36ac8f6588508  exact-separation primary (Opus)
ec3557953c6387ce35dcf4efe1df267fb828771119c479eb00c8f1793e0ee370  exact-separation review (Fable)
```

Printed source re-read on-page (`refs/sigray_full.pdf`, printed page =
PDF page, SHA-256 `9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae`):
pp. 19–20 (Proposition 4.2 with the strict `δ_j` descent and the printed
Jacobian slip), p. 21 (Notation 4.1), p. 23 (Proposition 4.6 `(11)`–`(17)`).
The promoted complete Proposition 4.2 repair in `ladder/SIGRAY-AUDIT.md`
(SHA-256 `ded3051d1a2009498f49bed20e5168d34b823518ab1b94ed340b380b37da6d15`)
is used only as the already-reviewed terminal `(1,0,c)` and exact-product
reading that the Statement-3.9 review already carries; it is not a new
lemma of this note.

Prompt SHA-256
`2179af537446fa9ac6252502a822fca451d8b1a3beae042ef35e1d337c9e28ca`.

---

## 1. Lead verdict

**`PASS_WITH_REPAIR`.**

The theorem `TD8-A-TOWER-PERSISTS` survives a hostile reconstruction:
both extra-direction `f`-branches at each reviewed A-vertex remain a
double root of the leading form through every fine step with `D_f>0`,
hence cannot separate before `θ=7`, hence `Δ_A=2`, independently at both
A-copies and independently of the affine parameter `t`. The first-child
discriminant identity `(2.1)` is exact, and the full tower forces
`(2.2)` locally at each copy.

Three written proof sentences are false or overstated (R1–R3 below).
None of them flips the inequality range, the exhaustion `e∈{1,2}`, or
the charge. After those repairs the argument is a theorem at the
producer's own formal scope.

Not proved here, and not claimed by a correct reading of the target:
trunk charge, exact total `λ`, cross-twin source gluing, polynomial
landing, realization, `δ_a=0`, the four-element cv census, or JC2.

---

## 2. Clause-level scorecard

| clause | verdict |
|---|---|
| Producer full/body hashes | **CONFIRMED** |
| `(k_0,l_0)=(2,3)` at the A-vertex; `μ_F=3/2` | **CONFIRMED** |
| Every later *preterminal* stage has `k_j=1` | **CONFIRMED** |
| Strict descent of shift exponents; first shift in `{1,2}` if it exists | **CONFIRMED** (R4: the shift may be absent) |
| Terminal formula `h=g^2-s_0 f^3-P(f)`, `deg P≤2` | **CONFIRMED** |
| `J(f,h)=2 c_0 g` | **CONFIRMED** |
| Lattice `(3.2)` for `e=1` and `e=2`; `D_h=12e` at `j=0` | **CONFIRMED** (R3: the `12` must be derived) |
| Exhaustion `e∈{1,2}` of branch behaviour | **CONFIRMED** |
| Highest-part cusp `G_j^2=s_0 F_j^3`; UFD forces `F_j` a square | **CONFIRMED** |
| `h` and `P(f)` strictly below `3 D_f` through `j=7e-1` on every legal track | **CONFIRMED** |
| Exact Jacobian band `(3.4)`; resonance exactly at `j=5e` | **CONFIRMED** |
| Resonance *forces* a drop of at least one unit of `D_h` | **REFUTED** as a forcing (R1); both continuations still keep the theorem |
| Common `H`-factor persists through `j=7e-1` | **GAP** if read universally (R2); not load-bearing for `F` square |
| First-child discriminant `(2.1)` | **CONFIRMED** (exact, including the prefactor) |
| Full tower forces `(2.2)` separately at each A-copy | **CONFIRMED** |
| Split quadratic at `θ=7`; conjugate `e=2`; short towers `m=1` / `(2)` / `(2,1)` | none evades; **CONFIRMED** as non-counterexamples |
| Scope firewall (trunk, gluing, landing, realization, JC2) | **ACCURATE** |

---

## 3. Proposition 4.2 hypotheses, independently rebuilt

### 3.1 Stage zero is `(2,3)` and `μ_F=3/2`

The reviewed A-vertex has full pattern degree `D=42`, q-side degree
`Q=36`, reduced extra-orbit data `(dp,dq)=(21,15)`. Proposition 8.1(ii)
gives `Q=D(μ-1)+dq`, so

```text
36 = 42(μ-1) + 15  ⇒  μ-1 = 1/2  ⇒  μ_F = 3/2,
```

and with `i_A=2` the same identity yields `k=i(μ-1)=1`. Independently,
type `(α,β)=(2,3)` at the poles (Proposition 5.3 / Statement 5.2, as
already forced by the Statement-3.9 review) supplies the unique first
Abhyankar step `(k_0,l_0)=(2,3)`. Printed Proposition 4.2(iv) then
reads

```text
μ_F = (k_0-1)l_0/k_0 + Σ_{1≤j<m} (k_j-1)l_j/k_j = 3/2 + Σ_{j≥1} (k_j-1)l_j/k_j.
```

Every summand is nonnegative. A later preterminal stage with `k_j≥2`
contributes at least `(k_j-1)/k_j ≥ 1/2`, hence `μ_F≥2`, contradicting
`μ_F=3/2`. The repaired terminal `(k,l,s)=(1,0,c)` is not preterminal.
Therefore every later preterminal stage has `k_j=1`.

Stage zero is enslaved at this vertex: `m_F≥1`, because
`p_{f,F}=C Φ^2` is a square, so the leading parts satisfy
`(g^+)^2=s_0(f^+)^3` and the leading Jacobian `J(f^+,g^+)` vanishes.
The printed dichotomy (10) therefore continues past `j=0`.

### 3.2 Strict shift descent and `deg P≤2`

For a `k_j=1` step, Proposition 4.2(iii) gives `h_j^+=s_j(f^+)^{l_j}`,
so `d_{h_j}=l_j d_f`. The next polynomial is `h_{j+1}=h_j-s_j f^{l_j}`,
whose leading parts cancel, and the printed strict inequality
`d_{h_{j+1}}<k_j d_{h_j}` yields `l_{j+1}<l_j` whenever the next stage
is again a preterminal shift. Thus the shift exponents are a strictly
decreasing sequence of positive integers.

The remainder of `g^2-s_0 f^3` after the weight-`3 D_f` cancellation
sits strictly below `3 D_f=42` (in `κ_F` units). If that remainder is
itself enslaved, its degree is an integer multiple `l_1 D_f` with
`1≤l_1≤2`. If it is not enslaved, the process has already stopped
(`m=1`) and there is no shift. The repaired constant terminal is
degree `0`. Hence `P` is a sum of `f^2`, `f`, and/or a constant, or
is absent:

```text
h = g^2 - s_0 f^3 - P(f),   deg P ≤ 2.                         (3.1)
```

**R4.** The target's phrase "the first shift exponent in `{1,2}`" is
true of every *existing* preterminal shift and false as an existence
claim. The `m=1` tower `P=0` is legal and is already covered by
`(3.1)`.

### 3.3 The Jacobian identity

The identity `J(f,P(f))=0` is polynomial, so

```text
J(f,h) = J(f,g^2) = 2 g J(f,g) = 2 c_0 g.
```

This uses only `k_0=2` and does not pass through the printed
Proposition 4.2 proof, which drops every `k_j` and assumes `J(f,g)=1`.
The Statement-3.9 review's exact product law specialises to the same
formula. The chart normaliser in Proposition 4.1 is `1` (that review's
`-bbox` pin), so the leading-part constant `γ` in the band below is a
nonzero multiple of `c_0`.

---

## 4. Ramified-lattice degree table

Write `K=e κ_F` with `e=E_+`, the number of conjugates of the extra
place that still agree through `π(F)`. Reviewed Theorem A gives
`E_+≤m=2`, so `e∈{1,2}`:

- `e=1`: contact (two distinct places, `κ` does not jump);
- `e=2`: conjugate pair (`κ_{P*}=2κ_F`).

No other ramification of the two-member extra-direction group exists.
A finer suitable `κ` only inserts zero layers (reviewed Theorem D(i))
and does not create a third branch. Multiple coincident drops are
impossible because `N≥1` and a characteristic jump with `e=1`
terminates the conjugate chain.

Before separation, `N=deg(p_{I(u)})=2` and Statement 3.10 supplies
slope `-2` in fine units. Type `(2,3)` plus the cusp of §5 force the
`g`-slope `-3`. The initial triple in `κ_F` units is
`(D_f,D_g,kbar)=(14,21,5)` from the Q-datum. The identity
`J(f,h)=2c_0 g` in the `(ξ,η)` chart has leading weight
`D_f+D_h-kbar` on the left and `D_g` on the right, so

```text
14 + D_h - 5 = 21  ⇒  D_h = 12
```

at `j=0` (equivalently Proposition 8.1: `1-u+k δ=5+7=12`; equivalently
`ρ=1/3` times `deg p_h=36`). Scaling to the fine lattice and dropping
by the pattern degrees gives the target's `(3.2)`:

```text
D_f = 14e-2j,   D_g = 21e-3j,   D_h = 12e-2j,   kbar = 5e-j.
```

**R3.** This derivation is not in the target; `(3.2)` is stated as a
fait accompli. The identities are nonetheless correct, and

```text
D_f + D_h - kbar = D_g
```

holds for every `j` on the slope-`(-2,-3,-2)` track.

Reconstructed tables, through the first vanishing of `D_f`:

`e=1` (contact):

```text
 j   D_f   D_g   D_h   kbar   3 D_f   D_f-2 D_h
 0    14    21    12      5      42         -10
 1    12    18    10      4      36          -8
 2    10    15     8      3      30          -6
 3     8    12     6      2      24          -4
 4     6     9     4      1      18          -2
 5     4     6     2      0      12           0   resonance
 6     2     3     0     -1       6           2   last / D_h=0
 7     0     0    -2     -2       0           4   stop, θ=7
```

`e=2` (conjugate):

```text
 j   D_f   D_g   D_h   kbar   3 D_f   D_f-2 D_h
 0    28    42    24     10      84         -20
 ...
10     8    12     4      0      24           0   resonance
11     6     9     2     -1      18           2
12     4     6     0     -2      12           4   D_h=0 on no-drop
13     2     3    -2     -3       6           6   last
14     0     0    -4     -4       0           8   stop, θ=7
```

Separation cannot occur at `D_f=0` in the sense of the extra-direction
count: that is the cv level `θ=7`. The tables exhaust the legal fine
steps.

---

## 5. Cusp equation and the `3 D_f` wall

The identity `g^2-s_0 f^3=P(f)+h` is polynomial, hence holds at every
Puiseux weight. On any face where the current leading weight of `f` is
`D_f(j)=14e-2j>0` and both `h` and `P(f)` lie strictly below `3 D_f`,
the highest parts of `g^2` and `s_0 f^3` cancel:

```text
G_j^2 = s_0 F_j^3.
```

Here `F_j` is the degree-`N=2` leading form of `f` in the residual
coordinate `L`, and `G_j` is the corresponding form of `g`. Then
`2 deg G=3 deg F`, so `deg G=3`. Unique factorization in `C[L]`: a
degree-2 polynomial whose cube is a square has even multiplicities, hence
is a square, hence has a double root. Translating the root to the origin,

```text
F_j = a_j L_j^2,   G_j = b_j L_j^3,   a_j b_j ≠ 0.            (3.3)
```

A double root of the leading form means the two extra-direction branches
still share the residual value at this order. This is the no-separation
statement at step `j`.

The same UFD applies on the conjugate lattice. At an odd fine step the
two Galois values are `c*±a`; the degree-2 form is `L^2-a^2`, which is a
square in `C[L]` if and only if `a=0`. Thus a conjugate split is blocked
exactly as a contact split is blocked.

Wall for `P(f)`. If `deg P≤2` then `P(f)` has weight `≤2 D_f=28e-4j`.
Compare with `3 D_f=42e-6j`:

```text
28e-4j < 42e-6j  ⇔  j < 7e,
```

which is `D_f>0`. Degree `3` would sit *on* the wall at every `j` and
would pollute the cusp; it is already forbidden by `μ_F=3/2`.

Wall for `h` on the slope-`(-2)` track: `D_h=12e-2j < 42e-6j` iff
`j<7.5 e`. The last inductive step is `j=7e-1`, and `7e-1<7.5e` for
every `e≥1`. The target's appeal to `e≤2` is unnecessary for this
comparison (R5). The bound `e≤2` is used only as the exhaustion of
§4.

Both walls are strict through `j=7e-1` on the no-drop track, so the
cusp applies at every fine step with `D_f>0`, and `F_j` remains a
square. That is the theorem.

---

## 6. Jacobian band, resonance, and the common-factor claim

### 6.1 The band

Write `H_j=v_2 L^2+v_1 L+v_0`, which is the general degree-`≤2` form
(the h-pattern at `c*` has multiplicity `2` at the vertex, from
`p_h=D Φ Ψ` with `Φ` and `Ψ` each simple at `T=B`, and pattern degree
is non-increasing). Substitute `(3.3)` into the leading Jacobian
`D_f F H'-D_h F' H=γ G` with `γ≠0`:

```text
2a(D_f-D_h) v_2 L^3 + a(D_f-2 D_h) v_1 L^2 - 2a D_h v_0 L = γ b L^3.
```

Coefficient comparison:

- `L^1`: `D_h v_0=0`, so `v_0=0` unless `D_h=0`;
- `L^2`: `(D_f-2 D_h) v_1=0`. Now `D_f-2 D_h=2(j-5e)`, so `v_1=0`
  unless `j=5e`;
- `L^3`: `2a(D_f-D_h)v_2=γ b`. Always `D_f-D_h=2e≠0`, so `v_2≠0`.

Off resonance and while `D_h≠0`, therefore `H_j=v_2 L^2`: the h-form
is a square on the same root as `F_j`, the h-multiplicity along the
chosen branch stays `2`, and `D_h` continues to drop by `2` per step.

This off-resonance vanishing of `v_1` *is* load-bearing. An illegal
early drop of h-degree to `1` would replace the slope `-2` by `-1`,
giving `D_h=12e-j` at the end. At `j=7e-1` that is `D_h=5e+1`, which
equals `3 D_f=6` for `e=1` and strictly exceeds it for `e=2`. The cusp
hypothesis would fail. The band is what prevents that path, not a
decorative alignment of `H` with `F`.

### 6.2 Resonance `j=5e`

At `j=5e` one has `kbar=0`, `D_h=2e≠0`, so `v_0=0` still, while `v_1`
is free. Thus `H=L(v_2 L+v_1)` with `v_2≠0`. Two continuations:

**No extra drop** (`v_1=0`). Stay on `(3.2)`. Walls of §5 already hold
through `j=7e-1`.

**Extra drop** (`v_1≠0`). The chosen branch sees h-multiplicity `1`.
Thereafter `D_f` still drops by `2` and `D_h` by `1`, so
`D_f=4e-2s`, `D_h=2e-s` at `s=j-5e`. In particular
`D_f-2 D_h=0` *persists*, the one-unit-too-high Jacobian coefficient
vanishes automatically once `v_0=0`, and the actual leading of
`J(f,h)` matches `g` from lower terms. At the last step `j=7e-1` one
has `D_h=1<6=3 D_f`. The cusp still applies, `F` remains a square, and
`L` still divides `H` while `D_h≠0`.

**R1.** The target says the resonance "forces" the chosen branch to
lose at least one unit of `D_h`. That forcing is false: `v_1` is a
free scalar of the leading band. Both continuations are legal, and
both keep `F` a square through `j=7e-1`. Rewrite the sentence as a
case split, not a drop.

### 6.3 Common factor through `j=7e-1`

On the extra-drop path, `D_h=1` at `j=7e-1`, so `v_0=0` and `L` still
divides `H`. On the no-drop path, `D_h=0` already at `j=6e`, which is
the last step for `e=1` and two steps before the last for `e=2`. At
`D_h=0` the `L^1` constraint is vacuous, `v_0` is free, and
`H=v_2 L^2+v_0` need not vanish at `L=0`.

**R2.** The claim that a common `H`-factor persists through `j=7e-1`
is therefore not universal. It is also not needed: `F` is a square by
the cusp UFD, not by sharing a root with `H`. Restrict the sentence to
the locus `D_h≠0`, or drop it.

The band is used once more at the vertex itself as a sanity check:
Proposition 4.6 `(14)` holds at `T=B` (`mult_f+mult_h-1=3=μ·mult_f`)
and `(13)` fails (`1≠14/12`), matching the exclusive dichotomy.

---

## 7. First-child discriminant and `(2.2)`

Reviewed vanishing and `ν=7` semi-invariance (Theorem D, under the
Fable `κ_F`-grading repair R1) give exactly the target's general
forms

```text
P'_0 = C(T-A)^4(T-B)^2,
P'_1 = η^4(T-A)^3(T-B) R_1(T),
P'_2 = η(T-A)^2 R_2(T).
```

These are the general polynomials of weights `(0,4,1)` with the
forced orders at both orbits. Only the values `R_1(B)` and `R_2(B)`
enter the first `κ_F`-child.

Let `c^7=B=(3/2)A`, `U=B-A=A/2`, `V'(c)=7c^6`. The Taylor
coefficients of the `κ_F`-child `c_0 η^2+c_1 η+c_2` are

```text
c_0 = C U^4 (V'(c))^2 = (49/16) C A^4 c^{12},
c_1 = c^4 U^3 V'(c) R_1(B) = (7/8) A^3 R_1(B) c^{10},
c_2 = c U^2 R_2(B) = (A^2/4) R_2(B) c.
```

Then `c_1^2` carries `c^{20}=B c^{13}`, and

```text
Disc = (49/64) A^6 c^{13} [B R_1(B)^2 - 4 C R_2(B)].          (2.1)
```

This was checked as an identity in `Q(A,C,R_1(B),R_2(B))` after
reducing `c^7=B`, including the gauges `(A,C,R_1)=(1,1,1)` which
recover the reviewed jet-L numbers `c_0=(147/32)c^5`,
`c_1=(21/16)c^3`, `c_2=s c/4` and the vanishing `s=3/8`.

The full tower of §§3–6 forces `F_j` to be a square at the first
`κ_F`-child (`j=e`). Pattern degree is non-increasing, so a first-child
split cannot be undone. Therefore `Disc=0`, and since the prefactor
`(49/64)A^6 c^{13}` is nonzero at `c∈C*` and `A≠0`,

```text
B R_1(B)^2 = 4 C R_2(B)                                     (2.2)
```

holds locally at each A-copy. In the gauge `A=C=R_1=1` this is
`R_2(B)=3/8`. There is no cross-twin equation between the two scalars:
each copy has its own `(C_e,R_{1,e},R_{2,e})` related by `(2.2)` with
an independent `u_e=R_{1,e}`.

The earlier nonzero-discriminant filling (reviewed Theorem E, jet E,
`Δ_A=8`) is compatible with Statement 3.9 plus the tops plus `(V)/(W)`,
and is incompatible with the approximate-root tower. That is a genuine
forcing, not a re-packaging of the first jet.

---

## 8. Counterexamples and short towers

None of the following evades the theorem.

1. *Split quadratic at `θ=7`.* At `j=7e` one has `D_f=0`. A split
   cv quadratic is a `θ=7` endpoint and still has `Δ_A=2` by reviewed
   Theorem B. A square cv quadratic is `θ>7` and also has `Δ_A=2`.
   Both are allowed. They are not counterexamples.

2. *Conjugate / ramified branch `e=2`.* The table of §4, the walls of
   §5, and both resonance continuations of §6 run through `j=13`.
   Odd-step UFD blocks a conjugate split. Exhaustion `e∈{1,2}` is
   `E_+≤2`.

3. *Short tower `m=1`, `P=0`.* Then `h=g^2-s_0 f^3` is already the
   terminal polynomial, and `D_h=12` is forced by `J(f,h)=2c_0 g`
   independently of `P`. The same track applies.

4. *Shifts `(l)=(2)`, `(1)`, or `(2,1)`.* All have `deg P≤2`. The
   `P(f)` wall is strictly slacker for `deg P≤1`.

5. *Degree-`3` remainder.* Would sit on the `3 D_f` wall, but is
   forbidden by `μ_F=3/2` together with enslavement of stage zero.

6. *Early h-degree drop.* Forbidden by the off-resonance band
   (§6.1). If it were allowed it would break the `e=2` endgame; it is
   not allowed.

7. *Jet E (`Disc≠0` at the first child).* Compatible with the printed
   local constraints and incompatible with the tower. It confirms
   `(2.2)`, it does not refute `θ≥7`.

8. *A `(2,1)` chain at a quadratic cv vertex.* That object lives
   downstream of this theorem (Proposition 7.1 at `deg(p_H)=2`) and
   cannot be used to evade the A-vertex `(2,3)` stage.

---

## 9. Maximum safe conclusion, and what is not proved

**Strongest surviving theorem.** Let `F` be either reviewed A-vertex of
the `td=8` equal-join affine route, with the displayed Q-datum, the
rigid ratio `B=(3/2)A`, `p_{f,F}=C Φ^2`, `p_{h,F}=D Φ Ψ`, the reviewed
first approximate-root stage `(2,3)`, `μ_F=3/2`, and `J(f,g)=c_0≠0`.
Then the two extra-direction `f`-branches remain a double root of the
leading form on the lattice `K=e κ_F` for every fine step with
`D_f>0`, for both `e=1` and `e=2`. Equivalently `θ≥7`, and the exact
A-charge is `Δ_A=2`. The same holds at both A-copies, independently,
and is independent of `t`. Consequently `(2.2)` holds locally at each
copy, and a first-child filling with nonzero discriminant does not
extend to the tower.

This is the target's Theorem, after R1–R4 are applied to the proof
text. The endpoint distinction (split versus square at `θ=7`) remains
harmless for the charge.

**Not proved, and not licensed by this pass.**

- Trunk charge, the exact one-`i_F`-unit area defect, or any total
  `λ`. Reviewed Theorem F would combine with `Δ_A=2` at both copies to
  put the remaining budget bit on the trunk, but that combination is
  a dependency, and the cv lane has separately quarantined printed
  Proposition 7.5 / literal `δ_a`. This note does not restore those.
- Cross-twin gluing of the two copies of `(2.2)`. Formal CRT at the
  two merge-orbit ideals is available as Laurent data and is not
  polynomial landing.
- Source landing, a polynomial pair, Keller realizability, a degree
  ceiling, `G2-PSC`, `G2-BD`, or JC2.
- The cv discriminants `Ω_e`. They decide only `θ=7` versus `θ>7`
  and do not move the charge.

---

## 10. Repairs

**R1 (false forcing, §3 of the target).** Delete "so the chosen branch
loses at least one unit of `D_h`". Replace by the case split of §6.2:
`v_1` is free at `j=5e`; both `v_1=0` and `v_1≠0` keep `F` a square
and keep `h` strictly below `3 D_f` through `j=7e-1`. Record that the
band *is* load-bearing off resonance, because an early h-degree drop
would violate the wall.

**R2 (overstated, same paragraph).** The common `H`-factor need not
persist at steps with `D_h=0` (no-drop path, `j=6e`). The square of
`F` does not use it. Restrict or delete.

**R3 (missing derivation, `(3.2)`).** Derive `D_h=12` from
`J(f,h)=2c_0 g` and `(D_f,D_g,kbar)=(14,21,5)`, or from Proposition
8.1. Do not list the lattice as an axiom.

**R4 (imprecise, shift existence).** Allow `m=1`, `P=0`. If a
preterminal `k=1` stage exists, its exponent lies in `{1,2}` and later
shift exponents strictly decrease.

**R5 (cosmetic).** The comparison `D_h<3 D_f` through `j=7e-1` does
not use `e≤2`; exhaustion of branch behaviour does.

None of R1–R5 changes a number in `(2.1)`, `(2.2)`, `(3.1)`, `(3.2)`,
or `(3.3)`.

---

## 11. Cheapest next discriminator

Stop spending A-side budget work on the free scalar `P'_2(c)`. Under
the tower it is pinned by `(2.2)` and cannot distinguish charges.
The A-side `Ω_e` values remain a contact-type bit (`θ=7` versus
`θ>7`) and a source-realization test; they are not a budget
discriminator.

The cheapest exact-budget datum that can still kill or promote the
route is the trunk ramification / area-defect condition for
`Δ_{\mathrm{trunk}}=2` (reviewed Theorem C: `κ_H=κ_F` and `τ_0=9`,
equivalently a drop of exactly one `i_F` unit of branch-area over
nine normalised steps). That is desk-scale in the printed descent
law and does not need a first A-jet.

No AWS, web access, canonical engine edit, or heavy computation was
used. This review does not access or depend on the separately owned
formalization repository.

---

Report-body SHA-256 (all bytes before the separator line above):
`b48b1c190336df0689e8a9521c41ce6ca4870f149960df28856de8bc9a88f22a`.
