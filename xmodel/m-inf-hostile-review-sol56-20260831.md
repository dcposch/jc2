# Hostile review: M-INF report

## 0. Scope, frozen inputs, and method

Verdict snapshot: **Piece 1 holds, with two local repairs to the written proof; Piece 2 is REFUTED as stated, not OPEN.**  The `(6,2)` nodal upgrade is sound after Piece 1, but the claimed `(6,4)` proof and hence the blanket `d <= 7` nodal closure are not sound.

Before reading, I ran SHA-256 on the three frozen inputs.  All matched the charge exactly:

```text
084346b52b0d67e1d147ec839aa1e75a2bfe816aa4b39d7ff58b8905c3745450  m-inf-semigroup-grok46-20260831.md
b9a83b0783f4b9b844bc881739e0b3c7c63efeb8683f862e007e6584af238696  pi1s4-close-residual-r2-opus5-20260831.md
bafe5e8929a77aa306e76ebdee1b300bbaf579a685f793cd8684ad861f041270  block-descent-a1-b0-n19-coordinator-integration-fable5-20260831.md
```

Below `M`, `R`, and `I` denote those three files.  Line references are to the frozen copies.  Literature was streamed from the exact URLs recorded in §3 and hashed without creating another report artifact.  All calculations below are displayed desk-scale arithmetic.  I used no CAS, did not inspect `jc2-lean`, and did not edit a charged file or canonical ledger.

## 1. Convention lock

The mathematical lock is consistent with the operative residual notation.  In `M:56-73`,

```text
v=s^a,  u=sum c_k s^k,  e_0=a,
beta_i=min{k:c_k!=0 and e_{i-1} does not divide k},
e_i=gcd(e_{i-1},beta_i),  e_h=1
```

uses **integer characteristic numerators**, with `a=mult(C)` and `{v=0}` transverse.  This is precisely `R:76-88,329-333`; the rational exponent in the unrelated explanatory aside `R:66-69` is not called `beta_h` and creates no collision.  The semigroup generators `bar-beta_i` are correctly separated from the characteristic numerators.  The first wording repair is that `M:56`'s “not tangent to the v-axis” is backwards under the usual axis naming: it should say “not tangent to `{v=0}`.”  The displayed brace condition is unambiguous, so this is not a mathematical change.

`M_emb` is also aligned.  It is the sum of strict-transform multiplicities at the centers in the branch-alone standard embedded resolution, ending only when the reduced total transform has normal crossings.  Thus its terminal multiplicity-one centers are included.  That is Zhang Definition 2.6 and is the same cluster as `R:308-333`, not the resolution of the pair `(C,L_infty)`.  The one-pair sequences in both reports confirm this convention: a `(2,3)` cusp contributes `(2,1,1)`, not merely its singular center.

Consequently Piece 1 evaluates exactly the residual's `M_emb`.  With the residual's intended exact reading of (4.1), `M_infty=max(M_emb,d)`, and `d<=3d-3` in the residual range `d>=2`, the scalar reduction is indeed

```text
(M-INF) <=> a+beta_h-1 <= 3d-3 <=> beta_h <= 2d+n-2.
```

For literal promotion, `R:319`/`M:75` should remove or resolve the phrase “up to one trailing multiplicity-1 point”: an unresolved possible `+1` is incompatible with calling the displayed reduction an equivalence.  This indexing qualifier does not affect any row promoted below, all of which have at least three units of slack.

## 2. Embedded-resolution identity

**Re-derivation.**  Put `Delta_1=beta_1` and `Delta_i=beta_i-beta_{i-1}` for `i>=2`.  Enriques--Chisini gives the full standard-resolution multiplicity sequence as the consecutive Euclidean blocks

```text
M(e_0,Delta_1), M(e_1,Delta_2), ..., M(e_{h-1},Delta_h).
```

The equal-valued runs at a block boundary are consecutive distinct blow-up centers; combining their displayed multiplicities neither deletes nor duplicates a center.  Since `e_{i-1}` divides `beta_{i-1}`,

```text
gcd(e_{i-1},Delta_i)=gcd(e_{i-1},beta_i)=e_i.
```

For a complete Euclidean block, orient `P=max(p,q)`, `Q=min(p,q)`, write `P=kQ+r`, and induct on `P+Q`; this gives

```text
sum M(p,q)=p+q-gcd(p,q).
```

Therefore

```text
M_emb=(a+beta_1-e_1)
      +sum_{i=2}^h(e_{i-1}+beta_i-beta_{i-1}-e_i)
     =a+beta_h-e_h=a+beta_h-1.
```

This also shows the sole formal defect in `M:129-131`: its induction writes `q=lambda p+r` without first orienting the pair.  When `0<q<p`, `lambda=0` and its recursive pair `(q,p)` has the same sum, so the asserted induction has not descended; its own `M(2,1)` uses this case.  The orientation above is the complete one-line repair.  The gcd equality used in the telescoping block should also be stated explicitly.

**One-pair checks.**  Direct Euclidean division gives

| `(a,beta_1)` | multiplicities | sum | `a+beta_1-1` | `delta=sum m(m-1)/2` |
|---|---:|---:|---:|---:|
| `(2,5)` | `2,2,1,1` | 6 | 6 | 2 |
| `(3,4)` | `3,1,1,1` | 6 | 6 | 3 |
| `(4,5)` | `4,1,1,1,1` | 8 | 8 | 6 |

**Both two-pair checks.**  For `(v,u)=(s^4,s^6+s^7)`, the blocks are `M(4,6)=(4,2,2)` and `M(2,1)=(1,1)`, hence sum `10=4+7-1`.  Directly, after `u=v u_1` and then `v=u_1v_2`, take `U=u_1`, `W=v_2-u_1`; their orders are `(2,3)`, so the cluster is `(4,2,2,1,1)`.  Its semigroup is `<4,6,13>`, conductor 16, and delta 8, agreeing with the cluster.

For `(s^4,s^6+s^9)`, the second block is `M(2,3)=(2,1,1)`, giving `(4,2,2,2,1,1)` and sum `12=4+9-1`.  In the same blow-up chart `ord(U,W)=(2,5)`.  The semigroup `<4,6,15>` has conductor 18 and delta 9, again matching.

**Piece 1 verdict: HOLDS; PROMOTE-AS-CORRECTED.**  The axis wording and non-descending induction should be repaired, but neither hides a counterexample.  The theorem is valid for every singular plane branch at the stated convention.

## 3. Negative analysis and primary-source audit

### 3.1 Source custody and the AM statement

The exact GB--P bytes were re-fetched from `https://arxiv.org/pdf/1208.0913v1`: 442,536 bytes, SHA-256

```text
f9af327748bbc4f3f4d31934510ec0fcbf3c547dc39f79d61278962cab69cc15
```

This exactly reproduces `M:29-36`.  Theorem 6.4 says that for the `n`-minimal sequence `(b_0,...,b_h)` of the infinity branch of a permissible degree-`n` curve, `e_{h-1}b_h<n^2`; its proof states `b_0=n`, `b_1=n'=mult_O C`.  Corollary 6.5 says, with `d=gcd(n,n')`,

```text
c <= (n-1)^2-(n/d-1)(n-n').
```

Thus `M:215-223` quotes and converts both correctly (`n_source=d_residual`, `n'=a`).  The original Abhyankar--Moh article is *Embeddings of the line in the plane*, JRAM 276 (1975), 148--166, DOI `10.1515/crll.1975.276.148`.  The official article page was found, but its PDF endpoint did not yield defensible article bytes; like the charged report, I do not pretend to have re-hashed or consumed it.  The quoted theorem and corollary are GB--P's.

Two other exact source records used here are:

```text
cf1157ef455cf12340c5dbf68f64dcce0f456d67e4edb8a6d8de5879fca3bacd  294334 bytes
  https://arxiv.org/pdf/1907.06281v3 (Zhang, Theorem 2.8)
637acfd15d3d73b47f2ddc75b713063ee6e236ff6fef271417d96d5846d5a4c9  241372 bytes
  https://arxiv.org/pdf/0910.2613v2 (Galindo--Monserrat, Theorem 2.1 and Proposition 2.1)
210f6817a431b61b242b292a567c3fb597950b1f99a8fd334c9fa2a035863733  75910 bytes
  https://arxiv.org/pdf/1407.0176v1 (numerical definition of an AM semigroup)
```

The charged citation `0910.02613` is malformed; the paper is arXiv **0910.2613**.

### 3.2 What AM controls, and the missed conversion

The central warning `b_h != beta_h` is correct.  For `(s^4,s^6+s^7)` with contact `d=6`, the transverse last numerator is 7 while the `6`-minimal semigroup sequence is `(6,4,13)`.  But `M:227,235` overstates the one-pair case.  For `(v,u)=(s^2,s^6+s^7)`, there is one transverse Puiseux pair, while the `6`-minimal sequence is `(6,2,7)`; `a+beta=9`, not `d+b_h=13`.

Nor is conversion absent.  GB--P Corollary 3.4 converts a `d`-minimal sequence to the intrinsic minimal semigroup generators; the charged recurrence

```text
bar-beta_{i+1}=n_i bar-beta_i+beta_{i+1}-beta_i
```

is invertible.  More directly, Galindo--Monserrat Proposition 2.1 converts an affine delta-sequence to the local maximal-contact generators.  What is missing is a sufficiently strong inequality or a rational-realization obstruction after conversion, not a map between the data.

This exposes the `(8,6)` arithmetic error.  `(8,6,3)` does satisfy Theorem 2.1: `n_1=4`, `n_2=2`, `24 in <8>`, `6 in <8,6>`, and `3<24`.  But `<8,6,3>=<3,8>` has conductor 14 and gaps `{1,2,4,5,7,10,13}`, hence genus **7**, not 8 (`M:233`).  Since local orders are `2|8`, Proposition 2.1 gives

```text
bar-beta_0=2,  bar-beta_1=8^2/gcd(8,6)-3=29.
```

Thus the corresponding local `8`-minimal sequence is `(8,2,29)`.  Conversely `(8,2,31)` would force affine delta-sequence `(8,6,1)`, which fails axiom (2) because `2*1` is not in `<8,6>`.  It is not merely “unrealized” at type `(8,6)`; it is incompatible with the cited theorem.  The genuine numerically admissible but rationally unrealized threat is beta 29 (and also 25, 23, 21), not 31.  Galindo's converse does automatically realize `(8,6,3)` by a degree-8 one-place curve; what is not automatic is normalization `A^1` with seven affine delta units.  The charged explanation based on possible incompatibility of degree-3 cancellation with degrees `(8,6)` is therefore also wrong.

### 3.3 Piece 2 has an exact counterexample

Set

```text
p(t)=t^6+(3/2)t^3+3/8,       q(t)=t^4+t.
```

Then

```text
p^2-q^3=(1/8)t^3+9/64.
```

Hence `z=t^3=8(p^2-q^3)-9/8` lies in `C[p,q]`; conversely `p=z^2+(3/2)z+3/8`.  Therefore

```text
C[p,q] isomorphic to C[z,y]/(y^3-z(z+1)^3),   y=q=t(z+1).
```

Its fraction field contains `t=y/(z+1)`, while `t` is integral over the ring by `t^3-z=0`; hence the map is birational with normalization `A^1`, and only `t=infinity` lies over infinity.  Thus it is a polynomial curve of type `(d,n)=(6,4)`.  The monic normal form in `y` has basis `1,y,y^2` over `C[z]`; the leading degrees `3i+4j` for `j=0,1,2` are in distinct residue classes modulo 3.  Therefore `S_aff=<3,4>` exactly and `delta_aff=3`.

At infinity put `u=1/p`, `v=q/p`, and `s=1/t`.  Then `v=s^2*unit`, and the exact identity

```text
u-v^3=(p^2-q^3)/p^3=s^15*unit
```

shows, after taking the analytic square root that makes `v=r^2`, that the sole transverse characteristic numerator is `beta_h=15`.  But

```text
15 > 2*6+4-2 = 14.
```

Equivalently Piece 1 gives `M_emb=2+15-1=16>15=3d-3`.  This is a desk-scale counterexample to Piece 2 exactly as stated.  For its affine equation, `F_y=3y^2` and `F_z=-(z+1)^2(4z+1)`; the only singular point is `(-1,0)`, where the tangent cone is `y^3+(z+1)^3`, three distinct lines.  It is an ordinary triple point.  The example therefore does **not** refute the residual's nodal subclass; it does refute the general “polynomial curve” theorem and destroys the supplied proof for the nodal `(6,4)` row.

## 4. Failed substitutions

The five rejections at `M:283` are directionally safe, but two explanations require correction and the report omits the substitution it actually used incorrectly.

1. **`beta_h=b_h`: correctly rejected.**  The `(4;6,7)` branch has transverse `beta_h=7` and `6`-minimal last generator 13.
2. **`a+beta_h=d+b_h`: correctly rejected.**  The report's claim that it is true for every one-pair germ is false.  Already `(a,d,beta)=(2,6,7)` has `d`-minimal sequence `(6,2,7)`, so the two sides are 9 and 13.  Equality in the coprime-contact one-pair case does not extend to `a|d`.
3. **AM Corollary 6.5 as the desired scalar bound: correctly rejected.**  At `(8,6)` it permits the AM ceiling 31, far above 20; Galindo lowers the genuine numerical ceiling to 29, still far above 20.
4. **A numerical AM semigroup as a rational type-`(8,6)` curve: correctly rejected as an inference, but mistyped.**  Conditions G1--G3 define a numerical AM semigroup and GB--P Theorem 9.5 realizes a local branch; neither is a global rational-realization theorem.  Moreover Galindo rules out `(8,2,31)` at this degree pair altogether.  The replacement unrealized threat is `(8,6,3)` / local `(8,2,29)`.
5. **The original degree triangle after Tschirnhausen: correctly rejected.**  Substituting `u -> u-cv^{d/a}` when `a|d` does not preserve ordinary support `i+j<=d`, so that polygon cannot cap the later characteristic exponent.

The fatal omitted item is the residual's substitution “odd extra generator `c` means `c>=7`” at `R:386-389,494-497`.  Galindo admits `(6,4,3)`:

```text
3*4=12 in <6>,   2*3=6 in <6,4>,   3<12.
```

Thus `<3,4>` has only three gaps, not at least five.  The counterexample in §3 attains it.  Accordingly `M:239`'s “No countermodel family” and `M:241,265`'s OPEN verdict are false for the theorem as written.

## 5. Consequence table

For `d<=7`, the noncoprime possibilities in the residual normalization are exactly `(4,2)`, `(6,2)`, `(6,3)`, `(6,4)`.  The correct proof status is:

| `(d,n)` | nodal residual status | exact reason |
|---|---|---|
| `(4,2)` | **CLOSED** (indeed outright) | `R:93-98` forces the `(2,5)` infinity cusp and `delta_aff=1`, hence one affine node.  `M_infty=6<=9`; the residual also has its independent braid kill. |
| `(6,2)` | **CLOSED after Piece 1** | Here `a=4`, `beta_1=6`, `e_1=2`, and `h=2`.  The conductor is `beta_2+9`; `delta_aff>=1` and total genus 10 give `beta_2<=9`.  Piece 1 now yields `M_infty<=4+9-1=12<=15`.  This is exactly the formerly CHECKED dependency at `R:488-490`. |
| `(6,3)` | **CLOSED** | Here `a=3` and the germ has one pair.  `delta_infty=beta_1-1<=9`, so `beta_1<=10` and `M_infty<=12<=15` (`R:491-493`). |
| `(6,4)` | **OPEN in the nodal subclass** | The asserted `delta_aff>=5` is false; the sharp delta-sequence floor is 3.  The §3 curve attains it and violates (M-INF), but has an ordinary triple point.  No charged theorem either realizes the same infinity type with three nodes or excludes it under nodality. |

Thus promote the `(6,2)` upgrade, retain `(4,2)` and `(6,3)`, and **do not promote** `(6,4)`, `R:482-504`'s “every `d<=7`,” or `M:267-273,285`'s corresponding table.  The source counterexample is enough to invalidate the proof; it is not being mislabeled as a nodal counterexample.

At `d=8`, one individual noncoprime row does close after Piece 1.  For `(8,2)`, `a=6`, `beta_1=8`, and the conductor is `beta_2+27`; `delta_aff>=1` gives `beta_2<=13<16`, hence `M_infty<=18<=21`.  But `(8,4)` and `(8,6)` retain admissible numerical threats: delta-sequences `(8,4,6,3)` and `(8,6,3)` convert to transverse last numerators 19 and 29, against targets 18 and 20.  Thus no blanket `d>=8` closure fires.  “Does not fire” must not be read as “no individual degree-8 row can be proved.”

The campaign consequence is material: the coordinator's statement that a degree bound `deg D_1<=7` would close the nodal residual is no longer supported.  Its `<=4` closure remains safe.  All these fundamental-group closures continue to consume the residual's separately sourced Nori step; this review changes only the infinity-bound input.

## 6. Verdicts and promotion recommendation

| item | verdict | recommendation |
|---|---|---|
| Convention lock | **HOLDS-AS-CORRECTED** | Keep the integer transverse characteristic convention; fix the axis wording and make (4.1)'s trailing-point indexing exact. |
| Piece 1, `M_emb=mult+beta_h-1` | **HOLDS** | **PROMOTE-AS-CORRECTED.**  Repair the Euclidean induction for `q<p` and state the block gcd equality. |
| Residual scalar reduction | **HOLDS under exact (4.1)** | It is a genuine equivalence, not merely an implication, once the cluster indexing is fixed. |
| Piece 2 for every polynomial curve | **REFUTED** | Do not promote the OPEN typing.  Bank the explicit `(6,4)` counterexample. |
| Piece 2 restricted to nodal residual curves | **OPEN** | This is the safe replacement.  It needs a nodal realization/exclusion theorem, not a cap or analogy. |
| GB--P Theorem 6.4 / Corollary 6.5 quotation | **HOLDS** | Source and formulas may be promoted at their stated necessary-bound scope. |
| `(8,2,31)` threat | **REFUTED at type `(8,6)`** | Replace it by the Galindo-compatible `(8,6,3)` / `(8,2,29)` unrealized rational threat. |
| `(6,2)` nodal row | **HOLDS** | **PROMOTE** on the residual's Nori basis; Piece 1 removes its only CHECKED local formula. |
| blanket nodal `d<=7` row | **REFUTED as a proof claim** | Retain `(4,2),(6,2),(6,3)`; return `(6,4)` to OPEN. |

The FALLACY-v2 guardrail changes no verdict: no flag, exit-set, pole, saturation, ring-map, or descent assertion is introduced here.  Most importantly, a semigroup floor is never treated as attainment, a numerical AM condition is not promoted to a global rational curve, and the nonnodal counterexample is not promoted to the nodal subclass.

<!-- BODY-END -->
