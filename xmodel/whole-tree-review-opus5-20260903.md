# Hostile review: WHOLE-MAJOR-TREE necessity (Moh 1983, §§4–6 + Appendix I)

Date: 2026-09-03
Reviewer: opus5 hostile lane (second reader on `moh-program-review-sol56-20260903.md`)
Status: complete (sealed)

## 0. Frozen-input gate, method, budget

`sha256sum -c` on the ten frozen copies in `/tmp/jc2-lane.pTHpRi/inputs`
returned `OK` for all ten before any mathematical input was opened. No
mismatch, no stop.

Source reading was image-first at 300 dpi (`pdftoppm -r 300`), journal page
`p` = PDF page `p-139`; pages 146, 170–172, 179–183, 185, 188–190, 200, 201,
205. No formula below was recovered from `pdftotext`.

Writes are confined to this report and `box/wholetree-drivers-20260903/`; the
charged drivers were copied there byte-for-byte and run there. Nothing I ran
wrote to `box/mohprog-drivers-20260903/` — its only change during my window is
a `__pycache__/…opt-1.pyc` at 12:05:07, produced by a concurrently running lane
(`python3 -O`, which I never invoked; my own byte-caches are in my box at
11:22–11:43). No ledger edit, no `jc2-lean`, no `ideation-*` file, no other
lane's report; the only non-charged repo files read are the two modules the
charged scripts import (`full_tree_partition.py`, `moh_skeleton_full_frozen.py`).

Budget: one core, peak RSS 62 MB, ≈ 6 minutes total wall (largest job: the
`candidate_eval.py` replay, 77.3 s). Desk-scale respected.

No new exit-price assertion is made here, so the FALLACY-v2 `charge_basis`
line is inapplicable.

---

## 1. Executive verdict

The charged report's **numbers all replicate**, including from a third,
independently written recursion: 658 → 60 → 58 → 55 → 23 → 20 at `n ≤ 100`,
the `(75,50)` residue `{M₂=55, V₂∈{2,3}}`, and the `48 ≤ D ≤ 120` triples
`1692/1189/670`, `183/113/57`, `152/96/45`. Its component (a) (universal
quantifier), (b) (orbit partition and capacity), (d) (the ODE step) survive
hostile reading and are **stronger** than the report types them; (e) (the
passport) is **derivable from Moh's own equation** and should be retyped from
`EXTERNAL` to `DERIVED`.

The decisive negative finding is different from the one the report flags. The
report's `OPEN[FULL-TREE-RECENTER]` is misplaced: Moh **does** state the
edgewise recentring, on p.190, and the correct citation is not Prop.5.4. What
is *not* justified — in the exploratory rule **and equally in the bare
`C_FULL_TREE`/`C_ZERO_PATH` rule that the report promotes** — is the step

> every edge of the chain carries the zero factor ⟹ `σ₁ = π t^{δ₁}`

which silently assumes that the centre of `D₁` contains **no terms other than
the chain's own edge centres**. Moh's own p.190 computation exhibits exactly
such an extra term (the constant `b`), and disposes of it only because at
`s = 2` the increment lattice is `ℤ`. For `s ≥ 3` — every row Moh searches,
by his own (6) `3 ≤ s ≤ 5` — the lattice is finer and the free coefficients
are never pinned by the tower data. Quantified on the frozen 658 rows: the
Prop.5.6 component alone accounts for **288 of the 598 kills**, and the
gap-free residue is **204 rows / 21 classes**, not 55 / 11.

Consequences the campaign must absorb before moving its frontier:

* the `(75,50)` discriminator `{55/2, 55/3}` **is not** gap-free: the repaired
  screen leaves five `(M₂,V₂)` pairs `{40/1, 40/2, 55/2, 55/3, 60/9}`;
* raw emptiness of `D = 105` **is not** gap-free (2 rows / 2 groups survive the
  repair); emptiness of `D = 117` **is**;
* **but** the *pinned-N* emptiness of both `D = 105` and `D = 117` is gap-free:
  0 UNI and 0 mixed groups survive even the weakest source-derived screen;
* **both rays die, gap-free.** All four members of the `A₂ = 6` ray
  (`n = 9(7t+6)`, `t = 0..3`) and all four of Sol's `L = 8a+5` ray
  (`a = 0..3`) are killed by the partition/sibling necessity alone, with no
  use of Prop.5.6, no recentring, and no passport. The killer is the forced
  zero sibling at `D₂` failing (12)/(13).

---

## 2. (a) The universal quantifier

### 2.1 The exact hypothesis of Prop. 5.3 (p.180, image)

> **Proposition 5.3.** *Suppose that `g(x,y)` is monic in `y` with `y`-degree
> `n>1` and for `r ≧ 2` a tower of major discs `D_s ⊋ D_{s−1} ⊋ ⋯ ⊋ D_r` is
> constructed. **Let `π − C_r` be a factor of `p(π)` as in the conclusions of
> Proposition 4.6 with multiplicity `V_r` satisfying***
> `deg p(π) = V_{r+1}(d_r/d_{r+1}) ≧ V_r > d_r/(n − M_r).`
> *… **Moreover the tower** `D_s ⊋ ⋯ ⊋ D_r ⊋ D_{r−1}` **is a tower of major
> discs.***

The hypothesis is a bare "Let … be a factor … with multiplicity `V_r`
satisfying [threshold]": **no selection clause, no existential**. Read as
mathematics is read, it is universally quantified over all factors above the
threshold, and the proof (pp.181–183) confirms this: `τ = Σ α_j t^j +
c_r t^{δ_r}` is built from the chosen `c_r` and nothing else, `σ*` and `σ**`
are defined only by `ord(σ − τ) > δ_r`, and the verifications feed Prop.4.4 and
Prop.4.6 with `v = V_r(d_{r−1}/d_r)`. Nothing distinguishes one root of `p`
from another. **PROVED-IN-SOURCE.**

### 2.2 Prop. 5.2's own wording (p.179, image)

> *Proposition 5.2 simply states that among the disjoint minimal subdiscs of
> `D_s` … which cover the roots of `g(y)∏T_i^ψ(y)` in `D_s` **any subdisc can
> be used as `D_{s−1}` if it contains more than the average number of roots**.
> The existence of such a subdisc is ensured by Proposition 4.6.*

"any subdisc can be used" is the universal; "the existence … is ensured" is the
separate existential. The report's reading is right and the sentence is not, as
the charge worried, an existence-only clause.

### 2.3 The p.200 Theorem quantifier

> *(4) if the number of roots of `g(y)` in `E_i` is `> n/(n − M_r)` then the
> tower of major discs `D_s ⊋ ⋯ ⊋ D_r` can be extended to `D_s ⊋ ⋯ ⊋ E_i`,*
> *(5) if the number of roots of `g(y)` in `E_i` is `≦ n/(n − M_r)`, then `E_i`
> is a minor disc …*
> *(6) The number of subdiscs `E_i` is bounded by `(n − M_r)·V_{r+1}/d_{r+1}`,*
> *(7) there must be at least one `E_i` satisfying the requirement in (4).*

`E_i` is bound by the preceding sentence "The roots … can be covered by a
disjoint union of subdiscs `⋃E_j`", so (4)/(5) are a universally quantified
dichotomy over that cover and (7) is the separate existential. **Yes, (4) is
"for every `i`"**, and (7) is the "at least one" that Prop.A.3(4) supplies.

The two thresholds agree. By Def.5.1(1) the number of roots of `g` in the child
disc is `(n/d_r)V_r`, so `(n/d_r)V_r > n/(n−M_r) ⟺ V_r > d_r/(n−M_r)`,
Prop.5.3's threshold, `= P_j/Q_j` (§3.1), `=` Prop.A.3(4)'s `m/n` — where
A.3's local `m, n` are `deg p, deg q`, **not** the global `deg f, deg g`; the
name collision is Moh's and is declared here once.

### 2.4 One thing the recursion *may* skip, checked

Neither charged implementation branches at level `s`; both start at `j = s−1`
with `V_s` from the row. Sound: `deg p` at `D_s` is `V_{s+1}d_s/d_{s+1} = d_s`,
the threshold is `d_s/(n−M_s) = d_s/2` (as `M_s = n−2`), and Def.5.1(2) forces
`V_s > d_s/2`, so every other factor has multiplicity `≤ d_s − V_s < d_s/2`
and is minor — **0 violations on all 658 rows**. Lemma 5.3 (p.185) says more:
the highest homogeneous form of `g` has *exactly two* roots.

**Verdict (a): PROVED-IN-SOURCE.** "Every above-threshold sibling extends" is
Moh's statement (p.200(4)) *and* a consequence of his proof (Prop.5.3 uses
nothing about the choice). Not an over-reading.

---

## 3. (b) The partition (3.3) and the capacity (3.4)

### 3.1 Node degrees, re-derived

p.182 (image), at the end of the Prop.5.3 proof, applying Prop.4.6 with `r−1`
replacing `r`:

> `deg q(π) = V_r((n − M_{r−1})/d_r) > 1,  deg p(π) = V_r(d_{r−1}/d_r).`

With `j = r−1` this is exactly the report's (3.1),
`P_j = V_{j+1}d_j/d_{j+1}`, `Q_j = V_{j+1}(n−M_j)/d_{j+1}`, and
`P_j/Q_j = d_j/(n−M_j)` is the major threshold. Prop.4.6 conclusions (3),(4),(5)
(p.170) give `q` squarefree, `roots(p) ⊆ roots(q)`, `p` not a power of `q`.

### 3.2 The orbit sizes are exactly `A_j` — and (10)/(11) *are* the partition

p.201(8)–(9) define `L`, `A_{r−1} = den(L δ_{r−1})`, and
`V_r(d_{r−1}/d_r) = △_{r−1}A_{r−1} + □_{r−1}`. With `(t̄)^{L A_{r−1}} = t`,
`L δ_{r−1} = B/A` in lowest terms, so `t^{δ_{r−1}} = t̄^{B}` and the
automorphism `t̄ ↦ ω t̄` (`ω^A = 1`) acts on the disc coordinate by
`π ↦ ω^{−B}π`. Since `gcd(B,A)=1`, the induced group on `π` is exactly `μ_A`
acting by multiplication. Therefore

* the fixed locus is `{0}` (for `A > 1`), so **every nonzero orbit has size
  exactly `A`** — delta 17(j) is right;
* multiplicities are constant on orbits, hence
  `P = b + A·Σ_ℓ u_ℓ` and `b ≡ P (mod A)` — the report's (3.3) — with `b =
  mult₀(p)`.

This is not an inference *about* Moh; it **is** Moh's (10)/(11). For a nonzero
root all `A` conjugates carry `V_{r−1}`, so `A·V_{r−1} ≤ P = △A + □` gives
`V_{r−1} ≤ △` = **(10)**; for the zero root `b ≡ P ≡ □ (mod A)` gives
`V_{r−1} = jA + □` = **(11)**. **PROVED-IN-SOURCE.**

`b` is *not* determined, only its residue; `b` ranges over
`{P mod A, P mod A + A, …}`. Both implementations enumerate that range. But the
*minimum* is `P mod A`, so the useful universal corollary is sound: **if
`P mod A > d_j/(n−M_j)` then every admissible `b` is above threshold and a
major zero sibling is forced.** That is the whole of `C_ZERO_PATH`'s
"mandatory residue" step, and it is exactly Moh's own p.188 sentence at the
bottom level: *"if the reduced denominator `A` of `δ₁` is not a factor of
`deg g_σ(π) = n*V₂` then `π` is a factor of `g_σ(π)`."*

### 3.3 `A | Q − 1` is DERIVED (not "Lemma 5.2's content"), and it is automatic

Moh states it only at the bottom (p.188, image): *"Moreover we always have from
the very definition of `A` the following `A|(n*+m*)V₂ − 1`."* Note
`(n*+m*)V₂ = Q₁`. The general statement is a three-line derivation, not a
quotation:

Write `L` for Moh's (8) lcm and `L*` for Lemma 5.2's parameter (the two are
different objects with the same printed letter). Lemma 5.2 at `L* = M_{r−1}`
gives `λ = (−1+δ_{r−1})/(n−M_{r−1})`, and `λ* = d_rλ` equals the Def.5.1(3)
sum, so with `R = d_rδ_s + Σ_{i>r} V_i(d_r/d_i)(δ_{i−1}−δ_i) − V_rδ_r` and
`b_r = (n−M_{r−1})/d_r ∈ ℤ` (by p.201(5), `d_r = gcd{n,M_1,…,M_{r−1}}`):

```
    b_r ( R + V_r δ_{r−1} ) = −1 + δ_{r−1}
 ⟹ (L δ_{r−1})(b_r V_r − 1) = −L − b_r (L R) ∈ ℤ
 ⟹ A_{r−1} | Q_{r−1} − 1        since  b_r V_r = Q_{r−1}.
```

(`L R ∈ ℤ` because every `δ_i`, `i ≥ r`, has denominator dividing `L` and
`d_r/d_i ∈ ℤ` for `i ≥ r`.) The report's attribution "Lemma 5.2's content" is a
citation slip; the statement itself is correct.

**Consequence, which fixes the zero-root count.** `q` is squarefree and
`μ_A`-stable, so `Q ≡ #{fixed roots of q} (mod A)` with `#fixed ∈ {0,1}`. With
`A | Q−1` and `A > 1`, `#fixed = 1`: **`0` is a root of `q`, and `q` has exactly
`(Q−1)/A` nonzero orbits.** Unused slots — `q`-roots with `p`-multiplicity 0 —
are exactly the subdiscs of p.200(6) that carry roots of `T_r^ψ` but none of
`g`; they are correctly allowed. For `A = 1` the group is trivial, `S = Q−1`,
the "zero root" degenerates to an arbitrary `q`-root, and the bookkeeping
`1 + S = Q` slots still holds.

**Measured.** Over all **1,996** nodes reachable in the whole tree of the 658
rows (sibling branches included), `A_j | Q_j − 1` fails **0 times**. This check
matters: `full_tree_partition.py` enforces the congruence *only* in passport
mode (`"passport requires A | Q-1"`), so 58 → 55 could have been partly a
capacity effect. It is not — toggling the congruence in my implementation gives
60/60 and 58/58, so **the whole of 58 → 55 is the passport inequality**.

**Verdict (b): PROVED-IN-SOURCE** for the orbit sizes, `b ≡ P (mod A)`, the
capacity structure and the unused slots; **DERIVED** (short, checked) for
`A | Q−1` above the bottom level.

---

## 4. (c) The recursion: what the child inherits, and what the DP must remember

### 4.1 The `M`-chain is global; only `V` branches

p.201(4)–(5), verbatim: *"`{n, M_1,…,M_s}` is the part of characteristic data
of `(f,g)` which are less than `n−2`"*, *"`d_r = g.c.d.{n, M_1,…,M_{r−1}}`"*.
These are data of the pair, not of a branch. So when a sibling of multiplicity
`u` becomes the next major disc `D_{j−1}`, its `M_{j−1}` and `d_{j−1}` are the
same global values the recorded path uses. Its degrees are

```
    P_{j−1} = u·d_{j−1}/d_j ,    Q_{j−1} = u·(n − M_{j−1})/d_j ,
```

so **yes, the child's `Q` is determined by `u` and the level alone**, exactly as
the DP assumes (p.182, quoted above).

### 4.2 The radii are *not* level data — the DP must carry the branch path

Def.5.1(3) (p.179, image):

```
                 (n − M_i) ∏_{j=i+1}^{s} [ V_j(n − M_j) − d_j ]
    δ_i = 1 −  ───────────────────────────────────────────────────
               (n − M_s − 1) ∏_{j=i+1}^{s} [ V_j(n − M_{j−1}) − d_j ]
```

`δ_i` depends on `V_{i+1},…,V_s`, i.e. on the branch's own choices. Hence
`L_j = lcm(den δ_s,…,den δ_{j+1})` and `A_j = den(L_jδ_j)` are branch data too.
**A DP whose state is `(level, multiplicity)` would be unsound.** Neither
charged implementation makes that error: `full_tree_partition.radius(i, path)`
and `tree-independent.delta(i, high_from_i)` both recompute from the full
`V`-path, and both cache on `(j, path[j+1:], …)` — the correct state. My own
implementation independently carries `high = (V_{j+1},…,V_s)`. Verified
indirectly: three implementations with three different state layouts agree
row-for-row (§8).

Structural sanity over the same 1,996 nodes: `δ_s = −1` always, `−1 < δ_j < 1`
strictly for `j < s` (**0** out-of-range), and every integral `δ_j` equals `0`
(**81** occurrences, **0** nonzero-integral). So the "integral non-positive
radius" of the recentring rule (§7) means `δ_j = 0` and nothing else.

### 4.3 Worked example 1 — Moh's printed `(99,66; M₂=77, M₃=97; V₂=8, V₃=8)`

By hand, then machine-confirmed:

```
 d = (99, 33, 11, 1)              s = 3,  V_4 = d_4 = 1
 δ_3 = 1 − 2/1 = −1
 δ_2 = 1 − 22(8·2−11) / (1·(8·22−11)) = 1 − 110/165 = 1/3
 δ_1 = 1 − 165·(8·22−33)(8·2−11) / ((8·165−33)(8·22−11)) = 1 − 5/9 = 4/9
 L_2 = 1,  A_2 = den(1·1/3) = 3        L_1 = 3,  A_1 = den(3·4/9) = 3
 node D_2 :  P_2 = 8·33/11 = 24,  Q_2 = 8·22/11 = 16,  threshold 33/22 = 3/2
 (9)      :  24 = 8·3 + 0     ⟹ △ = 8, □ = 0
 (10)     :  V_2 = 8 ≤ 8  ✔      (11): 8 ≢ 0 (mod 3)  ✘  → the edge is NONZERO
 A_2 | Q_2 − 1 :  3 | 15  ✔      S = (16−1)/3 = 5
```

Partition: `b = 0` is admissible (`□ = 0`), i.e. `0` need not be a root of `p`;
then `P = 24 = 3·8` is one nonzero orbit of three roots each of multiplicity 8,
which is the selected factor. `q` carries 16 roots: the fixed `0` plus five
orbits; one orbit is used, **four are unused slots**. Passport weights
`W = [ (24−16·0)/3, 24−16·8, 24, 24, 24, 24 ] = [8, −104, 24, 24, 24, 24]`,
`ΣW = 0`, `g = 8`, `d₊ = 104`, `d₊/g = 13 ≥ S = 5` ✔. Bottom: `A_1 = 3`,
`n* = 3`, `m* = 2`, `V_2 = 8`: `3 | 3·8` and `3 | 2·8 − 1 = 15`, so **(12)**
holds. No zero factor exists at all, so Prop.5.6 has nothing to bite on. This is
why the row survives every screen.

### 4.4 Worked example 2 — an excess row killed gap-free by a sibling

`(36,24; M₂=16, M₃=34; V₂=1, V₃=3)` (row #7 of the charged ten-row audit):

```
 D_2 :  δ_2 = 2/7,  A_2 = 7,  P_2 = 9,  Q_2 = 15,  threshold d_2/(n−M_2) = 3/5
        9 mod 7 = 2  ⟹  b ∈ {2, 9};  both exceed 3/5, so the zero factor is a
        FORCED MAJOR sibling, and it must itself reach D_1 obeying (12)/(13):
          b = 2 → V_2 = 2 : A_1 = 9  → (12) false, (13) false   ✘
          b = 9 → V_2 = 9 : A_1 = 22 → (12) false, (13) false   ✘
        no admissible partition at D_2  ⟹  the row dies.
```

The selected `V_2 = 1` itself passes (12)/(13); the row is killed **purely by
the sibling that Moh's construction forces to exist**, using only (3.3),
Prop.5.3's universal quantifier and (12)/(13). No Prop.5.6, no recentring, no
passport. This is the clean core of the charged theorem, and it is sound.

**Verdict (c): PROVED-IN-SOURCE / correctly implemented.** `Q_{j−1}` is a
function of `u` and the level; radii and `A`s are branch-specific and are
recomputed per branch in all three implementations.

---

## 5. (d) The ODE step (3.7)

### 5.1 The right-hand side is `cp` — quoted

**Proposition A.3 (p.205, image), verbatim:**

> *Let `m = deg p(π)`, `n = deg q(π)`. Suppose that the polynomials `p(π)` and
> `q(π)` satisfy* `D(m, n, p(π), q(π)) = c p(π)` *where `c ≠ 0 ∈ k`. Then we
> have: (1) every root of `p(π)` is a root of `q(π)`, (2) `q(π)` has no multiple
> root, (3) `p(π)` is not a power of `q(π)`, (4) there is at least one root of
> `p(π)` with multiplicity `> m/n`.*
>
> *Proof. The differential equation can be rewritten as*
> `n q(π)p'(π) = (m q'(π) − c) p(π).`

So the right-hand side **is** `cp(π)`, and the rewrite pins the convention
`D(m,n,p,q) = m p q' − n q p'`. The report's (3.5) is exact.

### 5.2 But A.3 is a *hypothesis*; where does the node get it?

This is the load-bearing check the charged report skips. Prop.4.6's displayed
differential equation is stated only for `r = 1` and for `(g_σ, T^ψ_{1,σ})`
with a *constant* right-hand side. The equation actually used at a node is on
p.171:

> `(6)  D(nλ, (−μ_r)λ, g_σ(π), T^ψ_{r,σ}(π)) = C` *the leading coefficient of*
> `T_r^ψ(π)_f`, with `g_σ(π) = C_0 p(π)^{n/d_r}` and
> `(T^ψ_{r,σ}(π))_f = C_r p(π)^{(−μ_r+M_r)/d_r}`, and
> `T^ψ_{r,σ}(π) = p(π)^{(−μ_r+M_r−n)/d_r}·q(π)` (Prop.4.6(2)).

Writing `N = n/d_r`, `e = (−μ_r+M_r−n)/d_r`, `𝔭 = deg p = v`,
`𝔮 = deg q = v(n−M_r)/d_r`, a direct expansion of (6) gives

```
 D(nλ, (−μ_r)λ, C_0p^N, p^e q) = λ C_0 n · p^{N+e−1} [ p q' − (𝔮/𝔭) q p' ]
                               = (λ C_0 n / 𝔭) · p^{N+e−1} · D(𝔭, 𝔮, p, q),
```

because `n e + μ_r N = −n(n−M_r)/d_r` and `(n−M_r)/d_r = 𝔮/𝔭`. Setting this
equal to `C·C_r p^{(−μ_r+M_r)/d_r}` and using
`(−μ_r+M_r)/d_r − N − e = 0` yields

```
                    D(deg p, deg q, p, q) = c·p(π),   c ≠ 0,
```

which is precisely A.3's hypothesis. (Moh's displayed simplification prints
the two weight arguments transposed, `D(v(−μ_r/d_r), v, p, T)`; matched to
their polynomials,
`D(v, v(−μ_r/d_r), p, T) = p^e·D(𝔭,𝔮,p,q)` and his `C*p^{e+1}` gives the same
conclusion — a source typo, not a different equation.) Def.5.1(4) asserts
Prop.4.6's conditions at every `σ_i`, and Prop.5.3 concludes that the extended
tower again satisfies Def.5.1, so **(3.5) holds at every node of the tree,
sibling nodes included**, for `j ≥ 2`.

### 5.3 (3.6) and (3.7), re-derived

Let `a` be a root of `q` (all simple, by A.3(2)), `q = (π−a)q_a`,
`p = (π−a)^u p_1`, `p_1(a) ≠ 0`, `u = mult_a p ≥ 0`. Expanding
`P p q' − Q q p' = c p` and dividing by `(π−a)^u`:

```
 P p_1 q_a + P(π−a)p_1q_a' − Q u q_a p_1 − Q(π−a) q_a p_1' = c p_1 ,
```

and at `π = a`, dividing by `p_1(a) ≠ 0`,

```
             (P − Q u) q_a(a) = c ≠ 0     ⟹     P ≠ Q u.
```

Exact; the hypotheses (`a` a simple root of `q`, which A.3(2) supplies for
every `q`-root) are met, and for a root of `p` we have `u ≥ 1`. It is **not**
the strict window restated: the window `u > P/Q` covers major factors, while
(3.7) additionally forbids a **minor** factor of multiplicity exactly `P/Q`.

**Measured mechanism.** (3.7) kills exactly 2 of the 60 rows, and in both the
excluded multiplicity is minor and sits exactly at the threshold:

```
 (84,56; 70,77,82; V=5,10,5)  D_3: P=10 Q=5  P/Q = 2 = threshold  (integral)
 (96,72; 84,88,94; V=3, 9,3)  D_2: P=18 Q=9  P/Q = 2 = threshold  (integral)
```

exactly as the report describes.

**Verdict (d): PROVED-IN-SOURCE (assembled).** RHS is `cp`; the identity holds
at every node; (3.6)/(3.7) are exact and independent of the window.

---

## 6. (e) The passport (3.8): DERIVED, not merely external

Divide `P p q' − Q q p' = cp` by `pq`: with `h = p^Q/q^P`,

```
        h'/h  =  Q p'/p − P q'/q  =  −c/q .
```

`div(h)` is supported on `roots(q)`, with `ord_a h = Q·mult_a(p) − P = −W_a`.
Since `Σ_a W_a = QP − PQ = 0`, `h` has neither zero nor pole at `∞`. Push down
to `z = π^A` (legitimate: everything is `μ_A`-invariant). Then `π^{A−1}q(π) =
z·∏_{ℓ=1}^{S}(z − z_ℓ) =: 𝔮(z)` is squarefree of degree `S+1`, `S = (Q−1)/A`,
and `H(z) := h(π)` satisfies

```
        H'/H = −(c/A)/𝔮(z),
        div(H) = − Σ_{i=0}^{S} W_i [z_i],
        W_0 = (P − Qb)/A ,  W_ℓ = P − Qu_ℓ ,  unused slots carry W = P.
```

All `W_i ≠ 0` by (3.7); `A | (Qb − P)` because `b ≡ P` and `Q ≡ 1 (mod A)`, so
`W_0 ∈ ℤ`. Put `g = gcd|W_i|`; since `div(H)/g` has degree 0 on `P¹` it is
principal, so `H = c′H_1^g` with `deg H_1 = d₊/g`, `d₊ = Σ_{W_i>0}W_i`.
Finally `H'/H ~ −(c/A)z^{−(S+1)}` at `∞` and `H(∞) = c_∞ ≠ 0,∞` give
`ord_∞(H − c_∞) = S`, hence `ord_∞(H_1 − ζ_0) = S`, hence

```
                    S ≤ deg H_1 = d₊ / g .            (3.8)
```

This is (3.8), derived from **Moh's own equation** plus the p.201 orbit
structure; nothing external is used beyond "a degree-`D` map attains a value
with multiplicity at most `D`". `S ≥ 1` because p.182 gives `deg q > 1` and
`A | Q−1`; characteristic 0 is used (as everywhere in Appendix I).

**It is also the *only* numerical passport condition available.** `H_1` is
branched over exactly `{0, ∞, c_∞}`, and with `D = deg H_1`,
`z₀ = #H_1^{-1}(0)`, `p₀ = #H_1^{-1}(∞)`, `z₀ + p₀ = S+1`, Riemann–Hurwitz
reads `2D − 2 ≥ (D−z₀) + (D−p₀) + (S−1) = 2D − 2` — equality. So the third
partition is forced to be `[S, 1^{D−S}]` and RH imposes nothing beyond
`D ≥ S`. A stronger cut would need a Hurwitz-existence (realisability) input,
not arithmetic.

**Measured.** The passport removes 3 of the 58 rows; the certificates are
explicit, e.g.

```
 (100,40; 70,95,98; V=8,4,4): A=1, P=8, Q=4, S=3, b=0, orbits [4,4]
     W = [8, −8, −8, 8]  g = 8  d₊ = 16  d₊/g = 2 < S = 3   ✘
```

**Verdict (e): DERIVED (source-consequence), not `EXTERNAL`.** Retype
`C_FULL_TREE_PASSPORT` accordingly. The Davenport–Zannier / polynomial-abc
*name* is external; the mathematics is Moh's equation. This is a genuine
upgrade of the charged typing.

---

## 7. (f) The recentring rule — and the gap it shares with the bare tree

### 7.1 What Prop. 5.4 proves (p.183, image)

> **Proposition 5.4.** *… Then the smallest disc which contains all roots of
> `g(y)T_1^ψ(y)` is the `D_i` with `i = max{ r : V_{r+1}d_r/d_{r+1} > V_r }`.
> Moreover if `δ_i > −1` then either `k[x,y] = k[T_1^ψ, g] = k[f,g]` or there
> exists an automorphism of `k[x,y]` which reduces the degrees of
> `T_1^ψ(f,g)`, `g` and `f` simultaneously.*

That is a statement about **one globally selected index**, and about a
*degree-reducing* automorphism (the proof uses `x → x + a^{−l}y^l`, p.185). The
charged report is right that Prop.5.4 licenses no edgewise translation — but
Prop.5.4 is the wrong citation.

### 7.2 What Moh actually states — p.190 (image), verbatim

> *To deduce Proposition 5.5 from Proposition 5.6 we note that we only have to
> consider … `δ_2 = −1`, `0 < δ_1 < 1`. Thus we have for suitable constants `a`
> and `b` the following* `σ_1 = a t^{−1} + b + π t^{δ_1}` *. And an automorphism
> of the following form* `x → x, y → y − a x − b` *will change `σ_1` to
> `π t^{δ_1}`. Proposition 5.5 follows from Proposition 5.6.*

This is **exactly** the campaign's recentring rule: kill a coefficient at
exponent `−1` (the top edge) and one at exponent `0`. The substitution
`y ↦ y − ax − b` preserves the Jacobian, preserves `deg = deg_y` for both `f`
and `g` (`deg_y` is untouched and `deg ≤ deg_y` forces equality), and preserves
every `M_i` (they are contact orders `ord(τ_i − τ_j)`, p.146, invariant under a
common translation of all roots). It also justifies the implementations'
`danger = True` at the root: the level-`s` centre `C_s t^{δ_s} = C_s x` is
removable, so **WLOG the selected top factor is `π`**. Radii increase strictly
along a chain, so at most one `δ_j = 0` and one `δ_j = −1` occur and a single
affine map suffices; and since the automorphism may be chosen adversarially,
requiring *every* dangerous branch to die is correct, not over-strong. So the
exploratory rule is not an unlicensed quantifier change — it is Moh's own
p.190 rule, and `OPEN[FULL-TREE-RECENTER]` is aimed at the wrong target.

### 7.3 The real gap: the centre of `D₁` is larger than the edge centres

Def.1.3 (p.146, image): *"Let `σ = Σ_{j<δ} a_j t^j + π t^δ ∈ k[π]⟪t⟫` with
`a_j ∈ k`"* — the sum runs over **all** exponents below `δ` in the Puiseux
value group, not over the tower radii. The centre of `D_{j−1}` is therefore

```
   centre(D_{j−1}) = centre(D_j) + C_j t^{δ_j} + Σ_{δ_j < e < δ_{j−1}} a_e t^e ,
```

and Moh's own p.190 display is an instance: at `s = 2` the constant `b` sits at
exponent `0`, which is **not** a radius (`δ_2 = −1`, `δ_1 ∈ (0,1)`). His `s=2`
argument closes only because the p.201 conjugation forces the centre into
`k⟪t̄^{A_1}⟫`, i.e. its support lies in `(1/L_1)ℤ` with
`L_1 = lcm(den δ_s,…,den δ_2) = den(−1) = 1`; the integral exponents in
`[−1, δ_1)` are then exactly `{−1, 0}` and **both** are killed by `y ↦ y−ax−b`.

For `s ≥ 3` — Moh's own (6) gives `3 ≤ s ≤ 5`, and all 658 rows have
`s ∈ {3,4,5}` (212/388/58) — `L_1` is no longer 1, and the window
`[δ_{i+1}, δ_i)` at level `i` admits support on `(1/L_i)ℤ`,
`L_i = lcm(den δ_s,…,den δ_{i+1})`. Every such lattice point that is neither a
radius nor an integer carries a coefficient that the tower data never pins and
that no polynomial automorphism can remove (`δ_1 < 1` always, so the only
integral exponents in range are `−1` and `0`). If any of them is nonzero then
`σ_1 ≠ π t^{δ_1}` and **Prop.5.6 simply does not apply** — no matter how many
edges are the zero factor.

Measured on the selected chain of each of the 658 rows: the free set is
non-empty for **500 of 658**; among Moh's six printed rows it is non-empty for
five and empty only for `(99,66)`:

```
 (64,48; 3,3): δ = (−1, 1/4, 9/16)   free = {1/2}
 (75,50; 2,4): δ = (−1, 1/5, 2/3)    free = {2/5, 3/5}
 (75,50; 3,4): δ = (−1, 1/5, 1/2)    free = {2/5}
 (84,56; 2,3): δ = (−1, 2/7, 16/21)  free = {3/7, 4/7, 5/7}
 (84,56; 5,3): δ = (−1, 1/4, 7/12)   free = {1/2}
 (99,66; 8,8): δ = (−1, 1/3, 4/9)    free = ∅  → Prop.5.6 available
```

Moh's p.201 closing sentence — *"the situation indicated by the equation (11)
can not always happen as established by Proposition 5.6"* — is the assertion
the campaign has been reconstructing. It is an aside, not a proved search
condition, and as literally read it needs the vanishing of those free
coefficients. **This is the single unstated hypothesis on which the charged
`C_ZERO_PATH` and `C_FULL_TREE` rest.**

### 7.4 A repaired, gap-free screen

Gate the Prop.5.6 kill on the chain's free set being empty (and, since it is
now justified, always use the p.190 removals at `−1` and `0`). Decomposition at
`n ≤ 100`, every line keeping 6/6 printed rows:

| screen | rows | `(n,m)` classes |
|---|---:|---:|
| baseline `PATH-ARITH(1–13)` | 658 | 63 |
| partition + universal siblings + (12)/(13) — **no Prop.5.6** | **348** | 52 |
| … + ODE (3.7) | 347 | 52 |
| … + passport (3.8) | **330** | 52 |
| … + **gated** Prop.5.6 (repaired) | 216 | 21 |
| … gated + ODE | 215 | 21 |
| … gated + ODE + passport | **204** | **21** |
| charged `C_FULL_TREE` (ungated Prop.5.6) | 60 | 12 |
| charged `C_FULL_TREE_ODE` | 58 | 12 |
| charged `C_FULL_TREE_PASSPORT` | 55 | 11 |
| charged `…_POLYNOMIAL` / `…_POLYNOMIAL_PASSPORT` | 23 / 20 | 7 / 7 |

So **288 of the 598 rows** that `C_FULL_TREE` removes are removed by the
ungated Prop.5.6 step. The gap-free residue is 204 rows / 21 classes.

**Verdict (f): the recentring rule is PROVED-IN-SOURCE (p.190, not Prop.5.4);
the zero-chain application of Prop.5.6 to `s ≥ 3` towers is SOURCE-ASSERTED
with a PROOF GAP (OVER-READING as a universal rule).**

---

## 8. (g) Independent replay

### 8.1 The charged drivers, rerun byte-identically

`candidate_eval.py` (SHA-256 = frozen) exited 0 in **77.32 s** and reproduced
the charged table row for row — all 33 candidates, all four count columns, all
`printed killed` entries; its regenerated `candidate-results.json` is
structurally identical to the frozen artifact modulo timing fields. In
particular:

```
 base_printed_1_13          658/63   0 killed   23720/14016/8831
 C_ZERO_PATH                153/15   0          7431/3212/2221
 C_FULL_TREE                 60/12   0          3090/1516/978
 C_FULL_TREE_ODE             58/12   0          2824/1384/865
 C_FULL_TREE_PASSPORT        55/11   0          2581/1261/803
 C_FULL_TREE_POLYNOMIAL      23/ 7   0          1691/848/590
 …_POLYNOMIAL_ODE            20/ 7   0          1420/686/459
 …_POLYNOMIAL_PASSPORT       20/ 7   0          1315/631/429
 (75,50) under every tree screen:  55/2  55/3
```

`tree-independent.py` (also byte-identical) reproduced 60/40, 55/37, 23/15,
20/12 rows/groups with `published_kept = 6` and `published_missing = []` in
under a second each.

### 8.2 A third implementation

`box/wholetree-drivers-20260903/opus5_probe.py` was written from the page
images with its own state layout, its own partition search and its own
knapsack. It returns **60 / 58 / 55 / 23 / 20 / 20** rows and
**12 / 12 / 11 / 7 / 7 / 7** classes, 6/6 printed in each — matching both
charged implementations exactly. On `48 ≤ D ≤ 120` it independently returns

```
 baseline               1692 / 1189 / 670   (charged: 1692/1189/670)
 C_FULL_TREE             183 /  113 /  57   (charged:  183/113/57)
 C_FULL_TREE_PASSPORT    152 /   96 /  45   (charged:  152/96/45)
```

so the charged `D`-range measurements are confirmed by a third code path. The
55-row survivor set's eleven classes are four printed plus the seven excess
classes `(72,48), (80,32), (90,60), (96,64), (96,72), (96,80), (100,80)`,
matching the charged `OPEN` bound exactly.

One cross-check worth recording: an early version of my recursion omitted the
free-subtree obligation on the zero factor when the selected path shared its
multiplicity, and returned 118 instead of 60. The charged implementations do
**not** have that hole — `option_data` checks `child_global` on the zero factor
unconditionally — and `(60,40; −10,45,58; V=1,8,4)` isolates the difference.

`48 ≤ D ≤ 190` sweep of my implementation (`Kmin = 16`; the `191..200` tail is
dropped — one `s = 6` skeleton at `D = 192` makes the *unscreened* partition
search exceed the desk budget. The truncation affects only this table):

| screen | rows | groups | UNI alive `N ≥ 6` | degrees emptied among baseline-nonempty |
|---|---:|---:|---:|---|
| baseline | 13584 | 8434 | 5417 | — |
| partition-only | 6628 | 3501 | 2086 | 48, 54, 63, 88, 102, 110, 130 |
| partition + ODE + passport | 6204 | 3304 | 1953 | same 7 |
| gated tree | 5573 | 2863 | 1847 | + 104, 114, **117**, 152, 153, 154, 170, 182, 186, 190 |
| gated + ODE + passport | 5227 | 2702 | 1727 | + 174, 184 |
| ungated `C_FULL_TREE` | 1615 | 843 | 544 | + **60, 81, 105** |
| ungated + ODE + passport | 1309 | 686 | 434 | (22 degrees) |

The charged empty-degree list is reproduced exactly on the overlap. **`60`,
`81` and `105` are the three degrees whose emptiness depends on the ungated
Prop.5.6 step.**

### 8.3 `D = 105` and `D = 117`: which sibling kills what

`Kmin = 16` census, matching the charged `D`-tables.

```
 D = 105 : baseline 15 rows / 14 groups
           partition-only            5 / 4
           gap-free gated tree       2 / 2      (m=63, M=[91,103], V=7,6
                                                 m=70, M=[90,103], V=5,3)
           charged C_FULL_TREE       0 / 0
 D = 117 : baseline  7 rows /  7 groups
           partition-only            2 / 2
           gap-free gated tree       0 / 0
           charged C_FULL_TREE       0 / 0
```

Per-row attribution (my implementation, all 22 rows classified):

```
 D = 105 (15 rows): 10 die by the partition/sibling necessity alone
                     3 more die by the GATED (gap-free) Prop.5.6
                     2 die only under the ungated, gapped Prop.5.6 step
 D = 117 ( 7 rows):  5 die by the partition/sibling necessity alone
                     2 more die by the GATED Prop.5.6;  none needs the gap
```

A gap-free kill, which is also the `A₂ = 6` ray's `t = 1` member:

```
 (117,78) M=[52,115] V={2:1,3:11}:  δ_2 = 1/6, A_2 = 6, P = 33, Q = 55,
     threshold 3/5.  33 mod 6 = 3, so b ∈ {3,9,15,21,27,33}; every one exceeds
     3/5, so the zero factor is a FORCED MAJOR sibling, and each choice gives
     A_1 = 7, 22, 37, 52, 67, 82 with (12) and (13) both false.  No admissible
     partition at D_2.  (The selected V_2 = 1 itself satisfies (13), A_1 = 2.)
```

The two rows that need the gapped step are exactly the two gap-free survivors,
and in both the recorded path *is* the zero factor, so the ungated rule kills
them by Prop.5.6 while the free set is non-empty:

```
 (105,63) M=[91,103] V={2:7,3:6}: δ = (−1, 1/11, 3/11), free = {2/11}
 (105,70) M=[90,103] V={2:5,3:3}: δ = (−1,  5/8, 19/24), free = {3/4}
```

**Pinned-`N`.** Both degrees are empty at the level the campaign actually uses,
under *every* screen including the weakest gap-free one: `D = 105` and
`D = 117` have **0 UNI groups alive at integer `N ≥ 6` and 0 mixed groups alive
in `N ∈ [6,16]`** already under `partition-only`. The two `D = 105` gap-free
survivors have `q = 15/11, u = 18` and `q = 1/4, u = 21`, neither attaining an
integer `N ≥ 6`.

### 8.4 The two rays

**`A₂ = 6` ray**, `P = 7t+6`, `n = 9P`, `m = 6P`, `M = (4P, 9P−2)`, `V₂ = 1`,
`V₃ = 6t+5`, `t = 0..3` (`D = 54, 117, 180, 243`). All four pass baseline
(1)–(13). All four **die under `partition-only`** — no Prop.5.6, no recentring,
no ODE, no passport:

```
 t: δ = (−1, 1/6, 7/12) for every t;  A_2 = 6 constant;  P_2 = 3(6t+5),
    Q_2 = 5(6t+5),  threshold 3/5,  P_2 mod 6 = 3.
 So b ≡ 3 (mod 6), b ≥ 3 > 3/5: the zero factor of p is FORCED and MAJOR.
 Every admissible b fails the bottom:
   t=0 (D=54):  b=3,9,15                → A_1 = 7,22,37, all (12)✘ (13)✘
   t=1 (D=117): b=3,9,15,21,27,33        → A_1 = 7,22,37,52,67,82, all ✘
   t=2 (D=180), t=3 (D=243): same pattern, every admissible b fails.
 The selected V_2 = 1 itself satisfies (13) with A_1 = 2 — it is the forced
 sibling, not the recorded path, that kills the ray.
```

**Sol's `L = 8a+5` ray**, `n = 21L`, `m = 14L`, `M = (7(3L+1)/4, 21L−2)`,
`V₂ = 1`, `V₃ = 5`, `a = 0..3` (`D = 105, 273, 441, 609`). Same verdict, same
mechanism:

```
 a=0 (L=5,  D=105): δ_2 = 7/18,  A_2 = 18, P = 25, Q = 55, thr = 5/11,
                    25 mod 18 = 7 → b ∈ {7,25}: A_1 = 17, 62, both ✘
 a=1 (L=13, D=273): δ_2 = 19/48, A_2 = 48, P = 65, Q = 145, thr = 13/29,
                    65 mod 48 = 17 → b ∈ {17,65}: A_1 = 7, 9, both ✘
 a=2 (L=21, D=441) and a=3 (L=29, D=609): identical pattern, both b values ✘
```

**Neither ray survives the sourced tree, and the verdict does not depend on
anything I flag as gapped.** The `A₂ = 6` ray's `N = 6` orbit-admissibility and
Sol's cofinal-nonemptiness consequence are both statements about a skeleton
space that the whole-major-tree necessity empties.

---

## 9. Typed verdict block

```text
(a) UNIVERSAL QUANTIFIER          PROVED-IN-SOURCE  (Prop.5.3 hypothesis is a
      bare "Let pi-C_r be a factor ... satisfying [threshold]", its proof uses
      nothing about the choice; p.200(4) is a per-i dichotomy, (7) the separate
      existential; Prop.5.2: "any subdisc can be used".  Level s vacuous,
      0/658 violations; Lemma 5.3 gives exactly two top roots.)

(b) ORBIT PARTITION (3.3)          PROVED-IN-SOURCE  (Moh's (10) and (11) ARE
      the two halves of P = b + A*sum(u); orbit size exactly A; b = P mod A;
      one fixed q-root; unused slots.)
    CAPACITY A_j | Q_j - 1 (3.4)   DERIVED  (3 lines from Lemma 5.2 +
      Def.5.1(3); Moh states it only at j = 1, p.188 -- "Lemma 5.2's content"
      is a citation slip).  MEASURED automatic: 0 failures at 1,996 nodes, so
      58 -> 55 is entirely the passport inequality.

(c) RECURSION / DP STATE           PROVED-IN-SOURCE  (M, d global, p.201(4),(5);
      child's P,Q depend on u and the level alone, p.182; radii, L, A are
      branch data, Def.5.1(3)).  A (level, multiplicity) state would be
      unsound; all three implementations recompute per branch.

(d) ODE STEP (3.7)                 PROVED-IN-SOURCE (assembled)  (A.3's RHS is
      c*p, quoted p.205; its hypothesis is established at every node by
      p.171 (6) + Prop.4.6(2), re-derived here -- Moh's printed weight
      arguments are transposed).  (3.6) exact; strictly more than the window.
      Measured 2 kills, both a minor sibling at integral P/Q = threshold.

(e) PASSPORT (3.8) d_+/g >= S      DERIVED -- retype from EXTERNAL  (from Moh's
      own equation: h = p^Q/q^P, h'/h = -c/q, descent to z = pi^A,
      ord_inf(H_1 - zeta_0) = S <= deg H_1).  Riemann-Hurwitz is tight, so no
      stronger NUMERICAL passport condition exists.  Measured 3 kills.

(f) RECENTRING RULE                PROVED-IN-SOURCE at p.190 ("y -> y-ax-b"),
      NOT Prop.5.4; the same rule licenses danger = True at the root.
    PROP.5.6 CHAIN, s >= 3         OVER-READING / SOURCE-ASSERTED WITH A GAP.
      "All edges zero => sigma_1 = pi t^{delta_1}" needs the centre of D_1 to
      carry no term outside the chain's radii; Def.1.3 (p.146) allows the whole
      lattice (1/L_i)Z per window and Moh's own p.190 exhibits such a term,
      disposing of it only because L_1 = 1 at s = 2.  All 658 rows have
      s in {3,4,5}; the free set is non-empty on 500 of 658 selected chains and
      on five of the six printed rows.  Cost: 288 of the 598 C_FULL_TREE kills.

(g) REPLAY                         CONFIRMED  60 / 58 / 55 / 23 / 20 and the
      (75,50) residue {55/2, 55/3} by both charged drivers rerun byte-
      identically AND by a third, independent recursion; likewise
      1692/1189/670, 183/113/57, 152/96/45 on 48<=D<=120.
      D=105: 15/14 -> 0 under C_FULL_TREE but 2/2 gap-free; D=117: 7/7 -> 0
      under both; both 0 at pinned N under every screen.
      RAYS: A2=6 ray t=0..3 and L=8a+5 ray a=0..3 -- 8 of 8 DIE, gap-free,
      killed by the forced zero sibling at D_2 failing (12)/(13).
```

### Promotion recommendation

**Promote, as source-derived necessity:**

* the universal-sibling extension (a), the orbit partition and capacity (b),
  the branch-correct recursion (c), the ODE step (d), and the passport (e) —
  the last **retyped `DERIVED`**;
* the composite screen **without** the Prop.5.6 component,
  `n ≤ 100` → **330 rows / 52 classes** (partition + ODE + passport); and, if
  the gate of §7.4 is accepted as the correct repair, the stronger gap-free
  screen `n ≤ 100` → **204 rows / 21 classes**;
* the **ray verdict**: the `A₂ = 6` ray and the `L = 8a+5` ray are both dead
  under source-derived necessity. This is the frontier-moving result and it is
  gap-free.

**Do not promote as a source-derived necessity:**

* `C_ZERO_PATH` (153/15) and the Prop.5.6 component of `C_FULL_TREE`
  (60/12), `C_FULL_TREE_ODE` (58/12), `C_FULL_TREE_PASSPORT` (55/11),
  `…_POLYNOMIAL*` (23/20) — retype these `SOURCE-ASSERTED, GAPPED`;
* the headline "the source-derived tree gives exactly Moh's two rows at
  `(75,50)`". Gap-free, `(75,50)` retains five pairs
  `{40/1, 40/2, 55/2, 55/3, 60/9}`; the exact `{55/2, 55/3}` needs the gapped
  step;
* "`D = 105` is empty" **at raw-row level** (2 rows survive gap-free). "`D =
  105` and `D = 117` are empty at pinned `N`" **is** promotable, as is
  "`D = 117` is empty at raw-row level".

**Retract from the charged report:** `OPEN[FULL-TREE-RECENTER]` as stated —
Prop.5.4 is the wrong locator and p.190 supplies the rule. Replace it with
`OPEN[CENTRE-SUPPORT]` below.

---

## 10. OPENs (bounded quantity + cheapest test)

### `OPEN[CENTRE-SUPPORT]` — new, and the one that matters

Decide whether, in a tower of major discs satisfying Def.5.1 for a
Jacobian pair with `deg = deg_y`, the centre of `D_1` can carry a nonzero
coefficient at a lattice exponent that is neither one of the tower radii nor an
integer. Equivalently: is Moh's p.201 sentence *"the situation indicated by the
equation (11) can not always happen"* a theorem for `s ≥ 3`?

*Bounded quantity.* A proof of vanishing restores the charged numbers exactly:
`n ≤ 100` residue 204 → 55 rows, 21 → 11 classes; `48 ≤ D ≤ 190`
5227/2702/1727 → 1309/686/434; and it re-empties `D = 60, 81, 105` at raw-row
level. A refutation costs the campaign 149 rows and 10 classes at `n ≤ 100`
and the three degrees. Either way the ray verdict and the pinned-`N`
emptiness of `D = 105, 117` are unaffected.

*Cheapest test (desk-scale).* Take the single row whose free set is already
empty, `(99,66; 77,97; V=8,8)`, plus one row with a one-element free set,
`(75,50; 55,73; V=3,4)` with free set `{2/5}`. For the latter, write the
generic `σ_1 = C_2t^{1/5} + a_{2/5}t^{2/5} + πt^{1/2}` (after `y ↦ y−ax−b`),
substitute into the Prop.4.6 leading-coefficient computation at `D_1`, and ask
whether `a_{2/5} ≠ 0` is compatible with `deg g_σ = n*V_2` and with
`D(n, −M_1, g_σ, T^ψ_{1,σ}) =` nonzero constant. That is one resultant in two
unknowns over `ℚ`; sympy, minutes. If `a_{2/5}` is forced to 0 the gap likely
closes in general; if it is free, the refutation is immediate.

### `OPEN[MOH-PROGRAM-ARTIFACT]` — inherited, re-based

Unchanged in kind (recover the CDC 6500 listing). Its **bounded residual must
be re-based** from the charged "49 excess rows / 32 excess groups after
`C_FULL_TREE_PASSPORT`" to the gap-free **324 excess rows / 48 excess classes
after partition + ODE + passport** (or 198 excess rows / 17 excess classes if
the gated Prop.5.6 is accepted). Cheapest test unchanged: archival, not
mathematical.

### `OPEN[SIBLING-COEFFICIENT-COMPATIBILITY]` — the ranked residual

The screens are per-node: each node's partition is checked in isolation, and
the passport is checked per node. Nothing yet forces the sibling polynomials
`p_j, q_j` at *different* nodes to come from one pair `(f,g)`. This is the
interaction Moh names in his introduction (p.143) and is the only remaining
route to an exact discriminator. *Bounded quantity:* at most the 330 gap-free
rows at `n ≤ 100`. *Cheapest test:* for the seven surviving excess classes of
the 55-row set, attempt an explicit `q_j`-root configuration satisfying the
full residue system `q'(a_i) = c/(P − Q u_i)` simultaneously at two adjacent
levels — a small polynomial system per class.

---

## 11. Reproducibility

All artifacts are in `box/wholetree-drivers-20260903/`. Entry points:

```bash
cd box/wholetree-drivers-20260903
python3 candidate_eval.py                      # charged driver, 77 s
python3 tree-independent.py --nlo 4 --nhi 100 --zero-only [--passport]   # 60 / 55
python3 tree-independent.py --nlo 4 --nhi 100 [--passport]               # 23 / 20
python3 -c "import opus5_probe as O; O.run_n100(); O.run_repaired()"
python3 struct_probe.py   # 1996 nodes: A|Q-1, delta range, top-level vacuity
python3 sens_probe.py     # the Prop.5.6 component switched off: 348/347/330
python3 repair_probe.py   # the free-exponent gate on the six printed rows
python3 residue_probe.py  # (75,50), D=105, D=117 under every screen
python3 kill_trace2.py    # which sibling kills each D=105 / D=117 row
python3 ray_probe.py ; python3 ray_trace.py    # both rays, with mechanism
python3 ode_probe.py ; python3 worked_probe.py ; python3 drange_probe.py
```

Every driver and output in the box is hashed in
`box/wholetree-drivers-20260903/SHA256SUMS` (34 entries). Key ones:

```text
4402bf528d18f8c409935433ce7a0bea5e3b2e6c23a1735f4341218035d11ad9  opus5_probe.py
a0e4e30ce91bdc20905276a842bba4de589dbe056d14463c138057f36c681223  struct_probe.py
358c2c7265b24340629b3b35619cb0b75c3c70e810afe8e766f8a2d70c96a9a6  repair_probe.py
c706a4a10c93a9790b5bebfdb1ed5b7c754269cd3ebe7a5c88f36f343dfde1b4  ray_probe.py
d4681fc2f907e5169be10b4cd2195e327450f6d47560d2423d8aaec384276e93  candidate_eval-replay.log
9e27c0abdee7663e741f2c22c1b3678cad2b114662dc361ac2bfc3a6c109b1d3  drange-48-190.json
```

Charged drivers, unmodified copies (hashes equal to the frozen inputs):
`candidate_eval.py 5d1b21…e553`, `tree-independent.py c2a276…6baf9`,
`moh_skeleton_full_frozen.py d20bf0…506d2`; plus the repo module the charged
harness imports, `full_tree_partition.py 875c09…5fef8`. Page images used are
under `box/wholetree-drivers-20260903/pages/`.

<!-- BODY-END -->
