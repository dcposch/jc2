# Hostile review — one-P0 nested-U2 obstruction (Grok 4.6)

Date: 2026-08-29  
Reviewer: Grok 4.6, independent adversarial lane, different model from the
Sol 5.6 producer.  
Target: `xmodel/m2-u2-one-p0-nested-boundary-r1-sol56-20260829.md`  
Lifecycle of the target: speculative child of a provisional producer
result, not a promoted claim. This review does not promote the parent.

## 0. Verdict

**`PASS`**

At the target's declared reduced/local-arithmetic and T1 scope, the two
load-bearing statements survive an independent rebuild from the hash-pinned
dependencies and the printed Prop. 9.3 / BOOK-OFFAXIS §10 grammar.

1. The incoming edge from an inner `nu=1` U2 vertex to a standard `nu>=2`
   P0 vertex is Prop. 9.3 case II with printed (a)--(d). Target N1
   integrality forces the inner frame integral, hence `L_inner | A r`.
2. After one P0 step the outer case-I coupling is
   `K(n dq_1+z)=z nu s R`. It is a finite divisor equation only at frozen
   P0 data. On the zero-cost neutral ray it does not bound `K`.
3. The displayed family for every `K==1 (mod 6)` reconstructs exactly,
   including both U2 T1 tests, the clean P0 ODE, gcd/MP2, St 8.4,
   arrival coprimality, root-multiplicity, modeled price, and equal weight.
4. No pinned *local* rule silently kills the family. Sheet-index /
   full-degree product, sibling first-separation, and Statement 3.9 gluing
   are present in the source but are stage-R-inert or outside the declared
   scope. The target already names them as the extension candidates.

The maximum safe theorem is exactly the target's §6 paragraph. The family
is a genuine infinite *formal* local obstruction to any invariant that
factors only through `(W_1,M_1,lambda)`. It is not a realization.

Non-blocking nits are recorded in §8. None changes a clause.

## 1. Custody and provenance

Worked only in `/Users/dc/code/math/jc2`. No `jc2-lean` access of any
kind. No ideation packet. No web, AWS, CAS, canonical edit, source /
prompt / adapter edit, commit, or push. Arithmetic is desk
`int`/`Fraction` plus the printed recurrences; no search caps.

Body-hash convention (target and this report): all bytes strictly before
the final `\n---\n`, i.e. `b[:b.rfind(b"\n---\n")]`.

| item | expected | recomputed | match |
|---|---|---|---|
| target, full | `350ec5ceb152524588cbb33e72b09c82d5e0250593583f3b60eda42eba32dc04` | `350ec5ceb152524588cbb33e72b09c82d5e0250593583f3b60eda42eba32dc04` | YES |
| target, body | `16dcbfcf26259f76cefa42eaced12fff4a334514f113d672f173818ce6a3c31b` | `16dcbfcf26259f76cefa42eaced12fff4a334514f113d672f173818ce6a3c31b` | YES |
| `ladder/BOOK-OFFAXIS.md`, full | `7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77` | `7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77` | YES |
| provisional parent nested-U2, full | `99bbe233f8f6f7273b2e5f89705aa5f2189681ce649a8723a66a0f99fa92912b` | `99bbe233f8f6f7273b2e5f89705aa5f2189681ce649a8723a66a0f99fa92912b` | YES |
| parent, body | `11e44767526044590b2f3ed8ceaed6b0aa3eaa98b30008e15bc725149d8b90cf` | `11e44767526044590b2f3ed8ceaed6b0aa3eaa98b30008e15bc725149d8b90cf` | YES |
| U2 `nu=1` primary, full | `9c20947be6d2ac6aad19176fae66f0b4acfb6ec6bce257a2169d8d266c667613` | `9c20947be6d2ac6aad19176fae66f0b4acfb6ec6bce257a2169d8d266c667613` | YES |
| Fable U2 primary review, full | `e156f94ca83026fe04b287100ca79f72325c80a82f8ed3f3f8a94044db440740` | `e156f94ca83026fe04b287100ca79f72325c80a82f8ed3f3f8a94044db440740` | YES |
| P0 skeleton R2 repair, full | `3a7c604b1972681ef90982a94a10c61076d1f16502603ac39cefc802d7439398` | `3a7c604b1972681ef90982a94a10c61076d1f16502603ac39cefc802d7439398` | YES |
| Fable skeleton R1 review, full | `3dab7f080ebc9ae5568d76cb4a60085646f2365ee7a277c6a0dd8028d4135b1f` | `3dab7f080ebc9ae5568d76cb4a60085646f2365ee7a277c6a0dd8028d4135b1f` | YES |
| Grok skeleton R1 review, full | `bf4c56ae3afdd34197ff4296c8f90112c6661ca09477bf498e7d9d2b038a0912` | `bf4c56ae3afdd34197ff4296c8f90112c6661ca09477bf498e7d9d2b038a0912` | YES |

Literal source grammar consumed: printed Prop. 9.3 (a)--(d) and Prop. 8.1
(iv) in `refs/sigray_full.pdf` pp. 39--42 and 50--51; BOOK-OFFAXIS §10
P0/P1/P2 and R1.2/R1.5/R2.1 (the P0 transport, St 8.4, arrival law, merge
handshake); DEPTH i-normalized (b) with `l`-cancellation; the absorbed U2
frame and r=2 T1 classification as narrowed by the Fable review (ODE
layer PASS, theorem-grade for all odd extra degrees). The provisional
parent is used only as motivation and as a frame-table cross-check; no
clause here depends on its unreviewed direct-edge finiteness theorem.

## 2. Charge 1 — incoming case II and the integral-reset lemma: CONFIRMED

Prop. 9.3 classifies the *lower* vertex `F` of `G=F+c`. A standard
`nu>=2` P0 vertex lies in `V_{1,a}` and is not a 0-edge, so the edge is
case II. Cases I and II share printed (a)--(d); the II label is the
`V_1` classification, not a second transport law.

Printed (d), equivalently BOOK R1.2 / R2.1 after i-normalization:

```text
kbar_F = (kbar_G + n)/nu_G,     n in N*.
```

Here `G` is the inner U2 merge (`nu_G = nu_0 = 1`) and `F` is the P0
vertex, so

```text
kappa_1 = (kappa_0 + j)/nu_0 = kappa_0 + j.
```

P0 at `nu>=2` is N1-on: BOOK P0 requires `kbar = l w dq / E in Z`. Thus
`kappa_1 in Z` and `j in N*` force

```text
kappa_0 = kappa_1 - j in Z.                 (IR)
```

The inner U2 frame from the reviewed primary is `kappa_0 = a(r+L)/L`.
Writing `a=A/B` in lowest terms and `kappa_0=z_0 in N*` with `B z_0 > A`
gives the identity (IL) exactly as printed, hence `L | A r`. The list of
candidates is finite and depends only on the fixed inner base data. If
`B z_0 - A = 0` then `A r = 0`, which is impossible.

The direct nested-U2 argument cannot use this reset: its outer vertex
also has `nu=1`, so N1 is off and that frame may stay rational. That
remark is correct and is the only place this note leans on the parent.

No omitted mandatory chain edge sits between the inner U2 merge and this
single P0 vertex. The U2 child weight `W_0 = a(L+r-1)/L` is the P0
arrival weight `w_G`; at `nu_G=1` one also has `w_G = kbar_G - rho_G`,
so the merge frame and the transported child weight are compatible. P2
prices the U2 arrivals at 0; the P0 step, if clean/neutral, prices at 0.
Neither price enters (IR).

## 3. Charge 2 — P0 frame and outer case-I equation: CONFIRMED

P0 transport, rebuilt from BOOK P0 / R1.2 / R1.4:

```text
s = 1+k+lex,   C = l(k+lex)-Sm,
dp_1 = eps + nu(l+Sm),   dq_1 = 1 + nu s,
E = l dq_1 - dp_1 = (l-eps)+nu C > 0,
kappa_1 = l W_0 dq_1 / E in Z,
rho_1 = kappa_1 / dq_1 = l W_0 / E,     (frame rho, not ODE slope)
W_1 = l W_0 s / E = l W_0 (dq_1-1)/(nu E),
M_1 = gcd(dp_1, dq_1).
```

The outer U2 merge is the lower vertex of the next edge, with `nu=1`,
hence `F in V_{2,a}\V_{1,a}`: case I, still (a)--(d). R2.1 with `G` the
merge and `e` the P0 arrival is the same formula with opposite naming,

```text
kappa_2 = (kappa_1 + n)/nu,     n = nu kappa_2 - kappa_1 in N*.
```

The characteristic index on the *source* of this edge is the P0 `nu>=2`;
the target U2 contributes `nu_F=1` only as the case label. Substituting
the U2 outer frame `kappa_2 = W_1(R+K)/K` and `W_1 = l W_0 s / E` gives

```text
n = (l W_0 / E) [ nu s (R+K)/K - dq_1 ].
```

The identity `dq_1 = 1+nu s` cancels the `nu s` terms and yields the
printed (OE), then (OC)

```text
K(n dq_1 + z) = z nu s R,     z = kappa_1 in N*.
```

Positivity `n>0` with positive frames is exactly `K < nu s R`. The second
printed comparison `K < z R / n` is true on the later family but is not a
general rearrangement of (OE) without extra inequalities; it is not used
as a bound. Denominators: `E>0` is the P0 searrow gate; `K>=1`; `dq_1>=3`.
No extra priced object is required on a clean P0 step plus a U2 merge
(`eps=k=0` at both, MP8). An omitted dirty P0 step would only tighten
the inner reset (budget), not restore an unbounded inner `L`.

At frozen full P0 data, (OC) is a finite divisor equation in `K`. On the
neutral ray `eps=k=lex=Sm=0` one has `E=l`, `W_1=W_0`, `kappa_1=W_0(nu+1)`,
and both `nu` and `z` are free, so the right-hand side of (OC) co-scales
with those forgotten coordinates. That is the precise loss relative to
the direct nested-U2 integer anchor.

## 4. Charge 3 — the displayed family, reconstructed: CONFIRMED

Fix `a=1`, `r=2`, `mu=3`, `L=1`. Then

```text
kappa_0 = 3,   rho_0 = 1,   W_0 = 2,   M_0 = gcd(6,3) = 3.
```

`L=1` divides `A r = 2`. For `K=6q+1`, `q>=0`, the neutral P0 step
`l=3`, `eps=k=lex=Sm=0`, `s=1`, `E=3`, `nu=2K` gives

```text
dp_1 = 6K,   dq_1 = 2K+1,   kappa_1 = 4K+2,   rho_1 = 2,
W_1 = 2,     M_1 = gcd(6K, 2K+1) = gcd(3, 2K+1) = 3,
j = 4K-1 in N*.
```

R1.2 independently: `Delta=1`, `t = W_0 nu_G / Delta = 2`,
`n_e = t nu - rho_0 = 4K-1`, matching `j`. The i-normalized (b)
proportion is `(rho_0+j):(kappa_0+j) = 4K:(4K+2) = nu:dq_1`. The `l=3`
thickening cancels, as R1.2 requires. Handshake check at the outer merge
below likewise closes.

Outer U2 with `R=2`, `h=3`, `L_outer=K`, two equal copies of this P0
arrival:

```text
dp_2 = 6,   dq_2 = K+2,   M_2 = gcd(6, K+2) = 3,
kappa_2 = 2(K+2)/K,   n = nu kappa_2 - kappa_1 = 6 in N*.
```

(OC) holds identically: both sides equal `16 K^2 + 8K`. Equal weight is
tautological for two copies of the same `W_1=2`. Typing:

```text
l=3 | M_0,     h=3 | M_1,     gcd(nu,h)=gcd(2K,3)=1,
M_0=M_1=M_2=3 >= 2,
nu = 2K == -1 (mod h)          (P2 neutral arrival law).
```

The modulus `6` is forced, not decorative: `r=2` T1 needs `K` odd, and
`h=3 | M_1` needs `K == 1 (mod 3)`, hence `K == 1 (mod 6)`. The other
odd classes `K==3,5 (mod 6)` give `M_2=1` and die on MP2. Root-mult
inequalities are strict: chain/arrival searrow is `l dq_1 - dp_1 = 3` and
`h dq_2 - dp_2 = 3K > 0`; NE extras are absent. Modeled P0 price is 0
(clean/neutral, St 9.6(v)); U2 extras price 0 (P2). Reduced state
presented to the outer merge is constantly `(W_1,M_1,lambda)=(2,3,0)`
while `(nu, kappa_1, K)=(2K, 4K+2, K)` escapes.

Desk reconstruction for `K in {1,7,13,19,25,31,37,43}` matches every
displayed integer/rational.

## 5. Charge 4 — both U2 T1 tests and the P0 ODE: CONFIRMED

Inner cell: `Rad = t^2-A`, `S=t`, `L=1`. The U2-ODE is

```text
2 (t^2-A) * 1 - 1 * (2t) * t = -2A != 0.
```

`C = mu C'/(r+L) = -2A != 0`. This is the `e0=1` odd-`L` slot, legal.

Outer cell: `r=2`, extra degree `K` odd. Rebuild of the classification,
independent of the charged window `L<=13`. On any squarefree quadratic
the monic degree-`K` map is square (Fable: injective because a degree
`d<K` kernel element has top term `(2d-2K) t^{d+1} != 0`). Translation
covariance reduces to `Rad=t^2-A`. The recurrence

```text
(p-1-K) s_{p-1} = A (p+1) s_{p+1}
```

seeds only the parity of `K`; the opposite-parity chain is killed at the
top by `s_{K-1}=0`. Thus `C' = -2 A s_1`. For even `K`, `s_1=0` and the
cell is dead. For odd `K`, walking down from `s_K=1` to `s_1` has
denominators `-2,-4,...,1-K`, all negative even and never zero, and
numerators `A K, A(K-2), ..., 3A` with `A!=0`. Hence `s_1 != 0` for
*every* odd `K`, not merely the charged list. Fable's admissibility gift
applies: `C'!=0` forces `S` squarefree and coprime to `Rad` automatically.
`K==1 (mod 6)` is odd, so the outer quadratic case is T1-alive for the
whole family. (Centered `t^2-A` is the shape that survives the odd-`S`,
`S(0)=0` specialization; that is the reviewed family, not a generic
quadratic with a forced eta slot.)

P0 ODE. Put `Z=eta^nu - c^nu`, `p=Z^3`, `q=eta Z`,
`delta = dp_1/dq_1 = 3 nu/(nu+1)`. Then

```text
delta p q' - p' q
  = Z^3 [ delta Z + (delta-3) eta Z' ]
  = Z^3 [ delta Z + (delta-3) nu eta^nu ]
  = - delta c^nu p != 0
```

for `c!=0`. Degrees: `deg p = 3 nu = 6K = dp_1`, `deg q = 1+nu = 2K+1 = dq_1`.
Roots: `p` is the single `nu`-orbit of multiplicity `l=3`; `q` is `eta`
times that orbit simply. This is the clean P0 shape of R1.0/R1.2 with
`n_F=1`. Top terms of the Wronskian cancel by `delta=dp/dq`, as required
for the reduced Prop. 8.1(iv) form.

## 6. Charge 5 — omitted local rule versus global gap: CONFIRMED as a gap

Searched the pinned source for a local kill already in force.

- *Sheet-index / i-sync.* BOOK-OFFAXIS §10 trust perimeter: `n_e in N*`
  and i-sync are never used to kill (stage-R policy). The U2 primary
  inherits the same rider. i-normalized full degrees on this family are
  `deg(p_G)=i_F l_F` hence `i_F=2` at the P0 vertex, while R2.1
  `deg(p_H)=i_G h` at the outer merge yields `i_G=4K`. That mismatch is
  real as a *hierarchy* number, and it is visible already at `K=1`
  (`i=2` vs `i=4`). It is not a silent local omission: the target
  excludes full hierarchy by name and lists "full hierarchy `i`/degree-product
  synchronization" as the candidate extension. Activating i-sync would
  change the theorem, not repair a local arithmetic error.
- *Sibling-synchronization.* Equal-weight is R2.1(i), local, and
  tautological for two copies of one arrival. Synchronizing two
  first-separated branches so that both carry the same growing `nu=2K`
  is a global realization/gluing problem (Statement 3.9 territory).
  The target does not assert it.
- *First-separation / Cor. 7.1.* This assigns St 9.4 charges to disjoint
  exit sets. The family has modeled `lambda=0` at every displayed vertex,
  so the budget constraint is vacuous rather than obstructive.
- *Full pattern degree vs local `(dp,dq)`.* The reviewed U2 and P0
  packets work in local pattern degrees. Full `i`-multiples are the
  sheet-index item above.
- *Arrival coprimality and St 8.4.* Both hold, as in §4. R1.5's
  `gcd(nu_H, mu_e)=1` at depth `>=1` is satisfied, not omitted.
- *NE / (R) / MP2 / searrow.* All hold strictly. No phantom dirty orbit.

No genuine omitted *local* rule was found. The remaining exclusions are
global realization, landing, or a promoted i-product law — exactly the
scope fence in the target's §6.

## 7. Charge 6 — maximum safe result

The following is theorem-grade at the declared scope.

> For fixed pre-inner-U2 data `(a=A/B, r, mu)`, any path consisting of
> that `nu=1` U2 vertex, exactly one standard `nu>=2` P0 vertex, and then
> a `nu=1` U2 merge has `L_inner | A r`. No theorem bounding `L_outer`
> follows from the reviewed reduced P0 state `(w,M)`, the modeled lambda
> budget, the two local edge equations, MP2, St 8.4, the arrival
> coprimality law, or local T1. Any invariant that factors only through
> `(W_1, M_1, lambda)` cannot distinguish the displayed family and
> therefore cannot prove outer finiteness.

The family is an infinite formal local arithmetic/T1 witness that the
neutral-ray coordinates `(nu, kbar)` must be controlled by something
outside `(w,M,lambda)`. It is not a polynomial-pair realization and does
not settle sibling index-product compatibility, full degrees, landing,
Statement 3.9, a panel, a degree ceiling, `G2`, or JC2.

The provisional parent's direct-edge finiteness is untouched: that
theorem explicitly declined the intervening-P0 case, which is the case
treated here.

## 8. Counterexample attempt, nits, next discriminator

**Attempt to break the family at the local tier.** Attacks tried and
failed: (i) mis-orienting Prop. 9.3 so that `nu` in (d) is the target's
rather than the source's — the printed (d) and R2.1 both put `nu_G` of
the upper/arrival vertex in the denominator, and both displayed edges
use that orientation; (ii) comparing unreduced `dp_1/dq_1` to the
i-normalized (b) ratio — R1.2 cancels `l` and the reduced proportion
`nu:dq_1` holds; (iii) (NE) on `S(0)=0` at odd outer `K` — that is a
`q`-root (`e0=1`), not a `p`-root, and is the reviewed unbounded-`L`
support lemma, not a kill; (iv) MP2 on the other odd classes — those
classes are already excluded by the `mod 6` filter; (v) P0 ODE degree
or remainder failure — the identity is exact and the degrees match;
(vi) outer T1 only in a charged window — the recurrence has no zero
denominator on any odd `K`. No local counterexample exists. The family
itself is the counterexample to outer finiteness at this scope, which is
the target's intended use.

**Non-blocking nits.**

- N1. Cases I and II share (a)--(d). One sentence would prevent a reader
  from hunting a different case-II formula.
- N2. `K < z R/n` is a family inequality, not a general positivity
  corollary of (OE). Drop it or derive it separately.
- N3. The outer T1 claim can cite Fable's all-odd-`L` theorem rather
  than "the reviewed quadratic classification" plus an implicit
  continuation of a charged window. The mathematics is already that
  theorem.

**Cheapest next discriminator.** Compute the i-normalized full-degree
product on this family as a *promoted* local rule: `i_F=2` at the P0
vertex versus `i_G=4K` at the outer merge. Already at `K=1` these
differ. If a successor lifts i-sync / degree-product out of stage-R and
into the one-P0 local grammar, the family dies without realization and
outer finiteness may be recoverable. If i-sync remains inert, the next
cheapest test is whether two first-separated siblings can both realize
the same growing `nu=2K` at equal weight — a Statement 3.9 / gluing
question, not a local-arithmetic one.

No web, AWS, heavy computation, canonical edit, commit, or push was used.

---

Report-body SHA-256 (all bytes before the separator line above):
`b90ece915d174c80ed69e310cca6dfd7552f46f13330ebda3e0de8eec1d5217a`.
