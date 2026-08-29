# Hostile review — repaired one-P0 nested-U2 semilinear family (Opus 5)

Date: 2026-08-29
Reviewer: Opus 5, independent adversarial lane, different model from the
Sol 5.6 producer.
Target: `xmodel/m2-u2-one-p0-semilinear-family-record-r1-sol56-20260829.md`
Lifecycle of the target: post-review follow-up to a **speculative child of a
provisional** producer result. This review promotes neither the target, nor
its producer, nor the provisional nested-U2 parent.

## 0. Verdict

**`PASS_WITH_REPAIR`**

The central claim is correct and it is a real, load-bearing find. The
reviewed `nu=2K` ray is uniformly dead by promoted N1/L6 primitivity; the
producer and its Grok hostile review both missed that predicate; and the
repaired `t=5`, `nu=5K`, `K==1 (mod 6)` ray survives every promoted local
predicate I can find in the pinned grammar. Every displayed field on the
repaired ray, the `t==5 (mod 6)` characterisation, the `K mod 6` residue
table, the full-index transport `(1,2,10K)`, and the full degree/`D` values
reproduce exactly from the pinned sources by four partly independent routes.
The semilinear/non-semilinear boundary is correctly drawn and I supply an
explicit witness for the negative half. Scope fencing is accurate: nothing
in the report proves occurrence, landing, gluing, a counterexample, or any
JC2 conclusion.

One repair is required.

- **R1 (must fix, record-level).** The inner-U2 field `dq_0` is displayed as
  `4` in §2 and shipped as `inner_u2.dq:4` in the §4 record. The correct
  value is `3`. `4` is exactly the *naive, eta-not-absorbed* `dq=1+r+L`,
  which the pinned U2 primary declares **illegal at `nu=1`**. The error is
  overdetermined five ways against the target's own tuple (§3.1 below) and
  a consumer that recomputes `M=gcd(dp,dq)` from the shipped record gets
  `M_0=2`, fails St 8.4 `l=3 | M_0`, and wrongly kills the whole family.
  Nothing else in the report is computed from `dq_0`, so the verdict, the
  N1 finding, the repaired ray, and the transport are unaffected.

One narrowing and three nits are in §7. None of them changes a clause.

Explicit counterexample attempts are in §8; the mandatory `t=2` negative
control is retained and strengthened in §2.

## 1. Custody, execution basis, and provenance

Worked only in `/Users/dc/code/math/jc2`. **No** `jc2-lean` access of any
kind — not entered, enumerated, searched, read, built, statused, modified,
or controlled. No web, AWS, heavy compute, CAS, canonical edit, target
edit, round-artifact edit, commit, or push. This session **did** have a
shell; arithmetic below is exact desk `int`/`Fraction` in scratch scripts
under `/tmp`, plus the printed recurrences. No search caps are load-bearing:
every quantified claim is closed by a closed form, and the finite scans are
corroboration only.

Body-hash convention (target and this report): all bytes strictly before
the final `\n---\n`, i.e. `b[:b.rfind(b"\n---\n")]`.

| item | expected | recomputed | match |
|---|---|---|---|
| target, full | `19fcd0133c72eba01dc4a554638111760a8813231a3b983a752d7d7528f58f82` | same | YES |
| target, body | `ce5cf26906d3c736e75c791c3600be201b65279aabbbacbf0b12014d51497c29` | same | YES |
| producer `...one-p0-nested-boundary-r1-sol56...` | `350ec5ceb152524588cbb33e72b09c82d5e0250593583f3b60eda42eba32dc04` | same | YES |
| Grok review `...one-p0-nested-boundary-r1-hostile-review-grok46...` | `2391b96cb131bf6b647c519e37c1423573d95d76917081d7dc31d5b45a5635ed` | same | YES |
| direct-edge/`i`-sync audit | `59fd30425df7bf4e9138c56b2d4ba4247d0c35f2ddeb409bc09b5cb6c7c45a0f` | same | YES |
| `ladder/BOOK-OFFAXIS.md` | `7679db8aa0526941804e3196920a5ad299bc68c1f5c4ebd82d55388ca7667f77` | same | YES |
| `ladder/SHEET6-DEPTH.md` | `ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d` | same | YES |
| `ladder/SHEET6-III.md` | `59a2fa489f7f999b24aabc4c707254b7e54f8db02d69690226754e3224f9bdda` | same | YES |
| `ladder/TEMPLATE-ATTACK.md` | `15457f185748249d57558f52f88727ae00efd16a4d485a51160e045a5e490229` | same | YES |
| `ladder/REDUCTION.md` | `b0b6c276b1fe28a9b94556e29a058264201267dfc496b3100c416f027bc7aa0f` | same | YES |
| `APPROACHES.md` | `27a208c58af3eb192bff51b2dc8f58cb9f6efcbd22816f88de6c9d428595a05b` | same | YES |
| `AUDIT.md` | `7cb5d4a8a3a4162a8a204facb79e68a9ef4f353275912d440170ae9898cd41f8` | same | YES |
| U1 record producer (Opus) | `7ed65bc22f836230dada03776a1b3c6f9110c955a35b52fa28c21d0811a6c99d` | same | YES |
| U1 record review (Grok) | `8755bd5d3d1cd2721d32e5956c5b139b2cc6e0e805662d5278ededff896135ba` | same | YES |
| `refs/sigray_full.pdf` | `9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae` | same | YES |

All 15 pins verified. The target's §1 line-range citations are also
accurate: `SHEET6-III.md` 123--133 brackets the §3 heading plus the whole
N1 paragraph (125--133); `TEMPLATE-ATTACK.md` 58--70 brackets the L6
statement (57--70).

Additional pinned grammar consumed, not listed by the target but needed to
rebuild the U2 normal form: `xmodel/m2-u2-nu1-unbounded-lex-primary-grok46-20260829.md`
(`9c20947b...`, itself pinned by the producer §1), §1 transport display and
§2 absorbed/naive discussion. This is the file that settles R1.

## 2. Attack 1 — the old `t=2`, `nu=2K` ray, and whether N1/L6 kills it

### 2.1 The rule is real, promoted, and case-agnostic

`SHEET6-III.md` §3 (lines 125--133) states it as an *identity*, not a
filter: for `G` with `nu_G>=2`, i.e. `G=I_P(alpha_j) in V_{1,a}`,

```text
kbar_G = (kappa-beta_j)/e_j,
gcd(kbar_G, nu_G) = gcd(beta_j, e_{j-1})/e_j = e_j/e_j = 1,
```

"**gcd(kbar_G, nu_G) = 1 at every nu >= 2 vertex.** (Def 3.1 + Not 3.4/3.5
only; case-agnostic.)" `TEMPLATE-ATTACK.md` §1a restates it as promoted law
**L6** — "at every characteristic vertex the e-sequence must drop by exactly
`nu`, forcing `gcd(kbar_V, nu_V)=1`" — and, decisively for this route, gives
the very shape at issue: "`kbar = w(nu+1)` at w-conserving segment vertices".

Three independent confirmations that it is *live*, not stage-R-inert:

1. `BOOK-OFFAXIS.md` line 779 lists "N1/L6 primitivity `gcd(kbar,nu_G)=1`
   (SHEET6-III:121-129)" among **"Unchanged filters"** and records that it
   "NOW BITES: four E5-realizable T1-alive cells die by N1 alone".
2. `TEMPLATE-ATTACK.md` §0 uses it to prune "7 (2,3)-type a=2,nu=2 pole
   entries book-wide (`kbar_P = a(alpha+beta) = 10, gcd(10,2) = 2`)".
3. `SHEET6-III.md` supplies a structurally identical precedent: 9.7(iv)'s
   node "has `gcd(nu,kbar)=gcd(s,2)*(unit)` ⟹ only odd `s` are realizable".

That last precedent is the same parity filter, on the same kind of
one-parameter ray, as the one the target applies. Contrast with `i`-sync and
`n_e`, which `BOOK-OFFAXIS` §10 P5 and the U1 record's rider 2 both hold
back as *not yet promoted to kills*. N1/L6 is not in that bucket.

### 2.2 The P0 vertex is in the rule's domain

A standard `nu>=2` P0 chain vertex lies in `V_{1,a}` and is not a 0-edge —
the Grok review's own §2 asserts exactly this, and `SHEET6-DEPTH` DS1 states
that *every* segment vertex is a `V_{1,a}` characteristic vertex of its own
pole. So the rule's hypothesis is met by the very vertex the family builds.

### 2.3 The kill is uniform, and it is the *only* failure

For the neutral P0 step (`eps=k=lex=Sm=0`, `s=1`, `E=l`), the BOOK §10 P0
transport `kbar_F = l*w_G*dq/E` gives `kbar_1 = w_0(nu+1) = 2nu+2`
identically in `n_e`, so

```text
gcd(kbar_1, nu) = gcd(2nu+2, nu) = gcd(2, nu).
```

At `t=2`, `nu=2K` is even for every `K`, hence `gcd=2` and the vertex is
**imprimitive**: DEAD, uniformly, for every `q>=0`. Exhaustive exact scan,
`q=0..3000` (`K=1..18001`): every member fails, and **`N1_L6` is the sole
failing predicate** — positive edges, searrow/(R)/NE, St 8.4 both edges,
MP2, arrival coprimality, the P2 neutral arrival law `nu ≡ -1 (mod h)`, the
clean P0 ODE, both U2 T1 verdicts, `kbar_1` integrality, and integrality of
all `i` and `D` all pass, exactly as the target's §7 control asserts. The
control is therefore maximally sharp: it isolates precisely the omitted
predicate and nothing else.

### 2.4 The omission in the prior lane is real

I re-read both prior reports for the predicate. The producer's §5 typing
list is `l|M_0`, `h|M_1`, `gcd(nu,h)=1`, `M_i>=2` — no `gcd(kbar_1,nu)`.
Grok's §4 list adds only `nu ≡ -1 (mod h)`. More seriously, Grok's §6 is an
explicit sweep titled "Searched the pinned source for a local kill already
in force", enumerating sheet-index/`i`-sync, sibling-sync, first-separation
/ Cor. 7.1, full-vs-local degree, arrival coprimality and St 8.4, and
NE/(R)/MP2/searrow — and concludes "No genuine omitted *local* rule was
found." **N1/L6 primitivity is absent from that sweep.** The conclusion is
false as stated, and Grok's `PASS` was granted on an incomplete filter list.
The target's §0 characterisation ("checked integrality of `kbar` but not
this primitivity condition") is exactly right for both lanes.

**Attack 1 result: N1/L6 kills the `nu=2K` ray uniformly. CONFIRMED.**

## 3. Attack 2 — every displayed field on the repaired `t=5` ray

I rebuilt the route from scratch out of the pinned transports rather than
from the target's displays: inner/outer U2 from the U2 primary §1
(`dp=r*mu`, `dq=r+L`, `E=mu*L`, `kbar=mu*w*dq/E`, `M=gcd(dp,dq)`), the P0
from `BOOK-OFFAXIS` §10 P0 (`kbar_F=l*w_G*dq/E`, `w_F=l*w_G(dq-1)/(nu E)`,
`M_F=gcd(dp,dq)`, `X_F=kbar_F*dp/dq`), and `rho=X/dp`,
`w=(kbar-rho)/nu` from §10 P1/P2.

### 3.1 R1: the one wrong field, `dq_0`

The target's §2 fixed inner tuple is `(dp_0,dq_0,kbar_0,rho_0,w_0,M_0) =
(6,4,3,1,2,3)`, and the record ships `inner_u2 = {... dp:6, dq:4, ...
kbar:"3/1", rho:"1/1", w:"2/1", M:3, lambda:0}`. With `a=1, r=2, mu=3, L=1`:

| route to `dq_0` | with `dq_0=3` | with `dq_0=4` |
|---|---|---|
| `dq = deg q = deg(Rad*S) = r+L` | `3` ✓ | contradicts `3` |
| `M_0 = gcd(dp_0,dq_0)` (target asserts `3`) | `gcd(6,3)=3` ✓ | `gcd(6,4)=2` ✗ |
| St 8.4 `l=3 | M_0` | holds ✓ | **fails** ✗ |
| `E_0 = mu*dq_0-dp_0` must be `mu*L=3` | `3` ✓ | `6` ✗ |
| `rho_0 = (kbar_0*dp_0/dq_0)/dp_0` (target asserts `1`) | `1` ✓ | `1/2` ✗ |
| `D_0 = rho_0*degp_0` (target's §6 asserts `6`) | `6` ✓ | `3` ✗ |

The value `4` is precisely `1+r+L`, which the pinned U2 primary §2 names as
"the naive (eta-not-absorbed) formulae `dq=1+r+L` ... the `nu>=2`
specialisations", and calls **"illegal at `nu=1`"**. The producer and Grok
both used the legal value implicitly, each writing `M_0=gcd(6,3)=3`. The
target introduced `4` as a *new* displayed field and then shipped it.

Note the target is internally *inconsistent between its own two U2 vertices*:
the outer uses the absorbed `dq_2 = R+K = K+2` (which is what makes
`M_2=gcd(6,K+2)=3`, `E_2=h*K`, and `kbar_2=2(K+2)/K` all come out right),
while the inner uses the naive value. Repair `dq_0: 4 -> 3` in §2 and
`inner_u2.dq: 4 -> 3` in the record. No other field moves.

This matters at record level rather than at theorem level. §7 stop rule 1
makes "drift or a missing mandatory predicate ... a hard failure", and
`legality` includes `"St8.4"`; a conforming consumer recomputing
`M_0=gcd(dp,dq)` from the shipped blob returns `2`, fails `l=3 | M_0`, and
reports the family DEAD for the wrong reason. It also changes the record's
canonical JSON, hence its family hash.

### 3.2 Everything else on the ray reproduces exactly

With `K=6q+1`, `nu_1=5K`, all values below were recomputed independently and
matched the target for `q=0..12` field-by-field, and the closed forms were
then verified for `q=0..3000`:

```text
nu_1   = 5K   = 30q+5        dp_1 = 15K = 90q+15
dq_1   = 5K+1 = 30q+6        kbar_1 = 10K+2 = 60q+12
rho_1  = 2                   w_1 = 2        M_1 = gcd(3,5K+1) = 3
lambda_1 = 0                 j = 10K-1 = 60q+9
dp_2   = 6                   dq_2 = K+2 = 6q+3
M_2    = gcd(6,K+2) = 3      lambda_2 = 0
kbar_2 = (2K+4)/K = (12q+6)/(6q+1)          n = 18
rho_2  = 2/K       X_2 = 12/K       w_2 = 2(K+1)/K = (12q+4)/(6q+1)
```

- **P0/U2 equations.** `E_1 = l*dq_1-dp_1 = 3(5K+1)-15K = 3 > 0`;
  `E_2 = h*dq_2-dp_2 = 3(K+2)-6 = 3K > 0`. Both searrows strict.
  `n = nu*kbar_2-kbar_1 = 4nu/K-2 = 4t-2 = 18`, and the outer coupling
  `K(n*dq_1+z) = z*nu*s*R` is an **identity** on the ray: both sides equal
  `100K^2+20K` (the `t=2` analogue is Grok's `16K^2+8K`, also confirmed).
- **gcd / primitivity.** `gcd(kbar_1,nu_1) = gcd(10K+2,5K) = gcd(2,5K) = 1`
  because `K` is odd. N1/L6 ALIVE for every `q`. `kbar_1 in Z` ✓ (N1 also
  needs this); `kbar_2` need **not** be integral since `nu_2=1` turns N1
  off, and indeed `kbar_2 = (2K+4)/K` is non-integral for all `K>4`.
- **St 8.4 / MP2.** `l=3 | M_0=3`; `h=3 | M_1=3`; `M_0=M_1=M_2=3 >= 2`.
- **Arrival coprimality.** `gcd(nu_1,h) = gcd(5K,3) = 1` since `K ≡ 1 (3)`.
  I also checked the strictly stronger BOOK §10 P2 neutral arrival law
  `nu_H ≡ -1 (mod mu)`: `5K ≡ 2 ≡ -1 (mod 3)` ✓. (It is equivalent here to
  `h | M_1` given `M_1 = gcd(l, nu+1)`, so `"St8.4"` in the record covers it.)
- **Rational reductions.** All four displayed U2 fractions are in lowest
  terms, and — the load-bearing point for §5 — the *affine* numerator and
  denominator laws are coprime for **every** `q`, verified `q=0..20000` and
  proved: `gcd(12q+6,6q+1)=gcd(6q+1,4)=1`, `gcd(2,6q+1)=1`,
  `gcd(12,6q+1)=1`, `gcd(12q+4,6q+1)=gcd(6q+1,2)=1`, all because
  `K ≡ 1 (mod 6)` forces `gcd(K,6)=1`. Reduction is a no-op, so the stored
  pairs really are affine rather than affine-then-reduced.
- **T1, both ends.** Inner: `Rad=t^2-A`, `S=t`, `L=1`, and the U2-ODE
  `r*Rad*S'-L*Rad'*S = 2(t^2-A)-2t^2 = -2A != 0`, with
  `C = mu*C'/(r+L) = -2A != 0`. Outer: I rederived the recurrence from the
  U2-ODE rather than taking it on trust. Writing `S=sum s_p t^p`, the
  coefficient of `t^m` gives `(m-1-K)s_{m-1} = A(m+1)s_{m+1}` and the
  constant term gives `C' = -2A s_1`. At `m=K`: `s_{K-1}=0`, so the
  opposite-parity chain vanishes from the top; for even `K` that chain
  reaches `s_1`, giving `C'=0` (dead), while for odd `K` walking `s_K=1`
  down to `s_1` has denominators `-2,-4,...,1-K` (all nonzero) and
  numerators `AK, A(K-2), ..., 3A` (all nonzero), so `s_1 != 0` and
  `C' != 0`. Alive for **every** odd `K`, no window, no extrapolation.
  Admissibility is automatic: a shared or repeated root of `S` would make
  the left side vanish there, contradicting `C' != 0` — so `S` is squarefree
  and coprime to `Rad`. (`S(0)=s_0=0` for odd `K`; that is the licensed
  `e0=1` specialisation, and it does not change `dq_2=r+L`.)
- **P0 ODE.** Verified symbolically, not by pattern-match. With `Z=eta^nu-c^nu`,
  `p=Z^3`, `q=eta*Z`, `delta=dp_1/dq_1=3nu/(nu+1)`:
  `delta*p*q'-p'*q = Z^3[delta*Z + nu*eta^nu(delta-3)]`, and `delta-3 =
  -3/(nu+1)`, so the bracket is `(3nu/(nu+1))(Z-eta^nu) = -delta*c^nu`.
  Hence `= -delta*c^nu*p`, nonzero for `c != 0`, **uniformly in `nu`**.
  Degrees match: `deg p = 3nu = dp_1`, `deg q = nu+1 = dq_1`.

### 3.3 The `t == 5 (mod 6)` characterisation and the residue table

The four filters in §3 of the target are individually correct
(`gcd(2,nu)=1` iff `t` odd; `M_1=gcd(3,nu+1)=3` iff `t ≡ 2 (3)`;
`gcd(nu,3)=1` iff `t ≢ 0 (3)`; `M_2=3` and outer T1 from `K ≡ 1 (6)`), and
an independent scan of `t=1..40` against `K in {1,7,13,19}` returns exactly
`t in {5,11,17,23,29,35}` — precisely `t ≡ 5 (mod 6)`, least positive `5`.

The `K mod 6` table at fixed `t=5` reproduces **including its fine
distinctions**, which is where a sloppy table would fail:

| `K mod 6` | recomputed failing predicates | `M_1` | `M_2` | target's row |
|---:|---|---:|---:|---|
| 0 | N1, `h|M_1`, MP2, `gcd(nu,h)`, P2-arrival, outer T1 | 1 | 2 | matches |
| 1 | none — ALIVE | 3 | 3 | matches |
| 2 | N1, `h|M_1`, MP2, P2-arrival, outer T1 | 1 | 2 | matches |
| 3 | `h|M_1`, MP2, `gcd(nu,h)`, P2-arrival | 1 | 1 | matches |
| 4 | N1, outer T1 **only** | 3 | 6 | matches |
| 5 | `h|M_1`, MP2, P2-arrival | 1 | 1 | matches |

Row `K ≡ 4` is the discriminating one: `M_1=3` and `M_2=6` there, and the
target correctly does **not** claim `M_1=1` on that row, citing only N1 and
outer T1. The table is a correct finite periodic consumer, as claimed.

**Attack 2 result: CONFIRMED, with the single exception R1 (`dq_0`).**

## 4. Attack 3 — full-index transport, degrees, `D`, and contradiction hunt

### 4.1 The transport is right, and the orientation is the audited one

The pinned direct-edge audit certifies `(IS)`: `i_H*dp_H = i_O*mu_e`, with
`H` the arriving/finer vertex, `O` the coarser, from Statement 3.17(i) plus
Proposition 8.1(i) at both ends. Applying it twice with `i_0=1`:

```text
edge 1 (H=inner U2, O=P0,       mu_e=l=3):   i_0*6   = i_1*3  => i_1 = 2
edge 2 (H=P0,       O=outer U2, mu_e=h=3):   i_1*15K = i_2*3  => i_2 = 10K
```

matching the target's `(i0,i1,i2) = tau*(1,2,10K)` exactly. Divisibility is
not accidental: St 8.4 gives `mu_e | M_H` and Prop 8.1(v) gives `M_H | dp_H`,
so `dp_H/mu_e` is an integer on both edges (`6/3=2`, `15K/3=5K`).

`degp = (6, 30K, 60K)` and `D = (6, 60K, 120)` then follow, and I checked
them by **four routes** that do not all reduce to one another:

1. `degp_V = i_V*dp_V` and `D_V = rho_V*degp_V` — definitional.
2. Prop 9.3(d): `kbar_O=(kbar_H+n_e)/nu_H` — holds on both edges.
3. Prop 9.3(c): `D_O=(D_H+n_e*degp_H)/nu_H` — gives `D_1 = 6+(10K-1)*6 =
   60K` and `D_2 = (60K+18*30K)/(5K) = 120`, as displayed.
4. The audit's §4 handshake `X_O = mu_e*(kbar_O - w_H)` with
   `w_H=(kbar_H-rho_H)/nu_H`, cross-checked against BOOK §10's
   `X_F = kbar_F*dp/dq`. Both give `X_1 = 30K` and `X_2 = 12/K`, hence
   `D_1 = 60K`, `D_2 = 120`, `rho_2 = 2/K`, `w_2 = 2(K+1)/K`.

All of (1)--(4) agree for `q=0..30`, and the general-`t` closed forms
`i_2=2tK`, `degp_1=6tK`, `degp_2=12tK`, `D_1=12tK`, `D_2=24t`, `n=4t-2`,
`j=2tK-1` were verified for `t=5..59 (mod 6)`.

I attempted the DEPTH handshake `kbar_G - D_G/i = w_e` as a contradiction:
it gives `(2K-8)/K = 2`, i.e. `-8=0`. That is **not** a contradiction — that
identity is `SHEET6-DEPTH`'s `mu_e = 1` specialisation (its §1 is explicitly
on the `M=1` axis, and the audit §3.2 declines to inherit that scope). The
general form `X_O = mu_e(kbar_O - w_H)` reduces to it at `mu_e=1`; here
`mu_e=3`. Attempt withdrawn.

### 4.2 Grok's `i`-mismatch is not a mismatch — the target is right

Grok's §6 reported "`i_F=2` at the P0 vertex, while ... `i_G=4K` at the
outer merge. That mismatch is real as a *hierarchy* number, and it is
visible already at `K=1` (`i=2` vs `i=4`)." Those two numbers are exactly
`i_1` and `i_2` for the `t=2` ray and are arithmetically right. But `(IS)`
*requires* `i` to change across an edge by the factor `dp_H/mu_e`; at `K=1`,
`4 = 2 * (6/3)` is the law being satisfied, not violated. Treating `i_1 != i_2`
as evidence of a kill is a misreading of `(IS)` as a constancy law. The
target's §6 correction is correct, and it also correctly notes Grok's
numbers were not *wrong*, only wrongly interpreted.

### 4.3 Manufactured-contradiction attempts (all failed)

- **Index integrality.** `i_1=2`, `i_2=10K`, `D_0,D_1,D_2` all integral for
  every `q`. No obstruction.
- **Mixed-`t` siblings.** I tried to break the outer merge by pairing
  arrivals with different `t` or different `K`. Equal-weight R2.1(i) is
  satisfied automatically because `w_1 = 2` **independently of `t` and `K`**,
  and `(IS)` constrains only the common full degree `deg(p_{H_e}^full) =
  i_O*3`, which is solvable with unequal `i_{H_e}`. So the sibling layer is
  *weaker* than the target needs, not stronger: no contradiction, and the
  target's use of two symmetric copies is a safe over-specification.
- **Outer merge budget.** All displayed `lambda = 0`, so St 9.4 exerts no
  pressure at the displayed vertices; `w_2 = 2(K+1)/K in (2,4]` is bounded
  and `M_2 = 3` is constant, so the downstream descent to a P1 terminal
  (`w<1`, `M>=2`) is a uniform-in-`K` problem and does not discriminate.
- **T1 zero-chain law (`dp | dq`).** `dp_2 | dq_2` iff `6 | K+2` iff
  `K ≡ 4 (mod 6)` — excluded by `K ≡ 1 (mod 6)`. `dp_1 | dq_1` is impossible
  (`15K > 5K+1`). Never fires.
- **St 8.5.** Per `SHEET6-III` §2, St 8.5 requires the parent `∉ V_{2,a}`,
  so it cannot be applied against the outer U2 merge.

**Attack 3 result: transport and all degree/`D` values CONFIRMED; no index
or sibling contradiction available at this tier.**

## 5. Attack 4 — auditing the semilinear-record claim

**Fixed `t=5`: semilinear. CONFIRMED.** The §4 generator

```text
(K,nu1,dp1,dq1,kbar1,j,dq2,kbar2_num,kbar2_den,n,i2,degp1,D1,degp2,D2)
= (1,5,15,6,12,9,3,6,1,18,10,30,60,60,120)
+ q*(6,30,90,30,60,60,6,12,6,0,60,180,360,360,0)
```

has 15 well-formed components; every one matches my rebuild at `q=0` and in
slope. That is a single linear set, hence trivially semilinear. The claim is
*not* vacuous, because the rational fields could have failed it: it survives
only because the affine numerator/denominator pairs are already coprime for
every `q` (§3.2), so no `q`-dependent reduction occurs. The remaining
rational fields (`rho_2`, `X_2`, `w_2`) are recoverable from `K` by the
displayed laws, consistent with §4's "derived quantities may be recomputed".

**Both `t` and `K` varying: not semilinear. CONFIRMED, with a witness.**
Intersect the two-parameter graph with the Presburger-definable slice
`t = K+4` (i.e. `u=q` under `t=6u+5`, `K=6q+1`). Semilinear sets are closed
under intersection with Presburger sets and under projection, so this would
force `{(6q+5)(6q+1) : q>=0} = {5,77,221,437,725,...}` to be a semilinear
subset of `N`, i.e. eventually periodic. Its consecutive gaps are
`72,144,216,288,...`, unbounded — so it is not. The two-parameter union is
therefore genuinely an infinite collection of fixed-`t` rays, exactly as the
target says. The identical argument disposes of `i_2 = 10K*tau` with `tau`
free (take `tau=q`: values `70,260,570,1000,...`, gaps `190,310,430,...`).

**Coefficient data.** §5.2's exclusions are right and the record's
`coefficient_character` tags are accurate. In particular "unique monic `S_K`"
is a theorem, not a slogan: for fixed `Rad=t^2-A` and `K`, requiring
`r*Rad*S'-L*Rad'*S` to be constant is `K` linear conditions on the `K`
unknown sub-leading coefficients, solved uniquely by the downward recurrence
of §3.2. Storing the tag rather than the field elements is the correct call.

**Source scale.** Routing absolute `i` to a typed consumer rather than
claiming a uniform absolute-index quotient is correct; see the narrowing in
§7 for the one thing this fence does not say.

**Coverage and realization.** `coverage_status`, `coverage_debt`, and the
`consumers` list are accurate against what was actually proved. The
`EQJOIN-FAMILY/v1` normalization/hash rules cited in §4 match the pinned U1
record verbatim (sorted-key canonical JSON, no floats, `"a/b"` in lowest
terms, minimal period before hashing, residues reduced, members carrying the
family key as provenance and never keyed on the cell tuple alone).

**Attack 4 result: CONFIRMED on both halves of the boundary.**

## 6. Attack 5 — what the family does and does not obstruct

It **does** obstruct a literal finite-cell claim at the declared tier. The
map `q -> ` (labelled route) is injective — `K`, `nu_1`, `dp_1`, `dq_1`,
`kbar_1`, `dq_2`, `kbar_2`, `w_2` all move with `q` (500 distinct signatures
in `q=0..499`) — and all 3001 members scanned pass every promoted local
predicate. So no theorem of the form "finitely many cells satisfy [positive
edges, (R)/NE, St 8.4, MP2, arrival coprimality, N1/L6, P0 ODE, both U2 T1
verdicts]" can hold, and in particular `L_outer = K` is not bounded by that
list. The producer's original point survives the repair intact.

It is also a *sharper* obstruction than the producer's: there the reduced
state `(w_1,M_1,lambda)=(2,3,0)` was constant while `(nu,kbar,K)` escaped;
here I note additionally that the outer merge's own reduced frame
`w_2 = 2(K+1)/K` takes infinitely many distinct values, so the infinitude is
visible in the outer U2's reduced data, not only in the forgotten P0 fields.

It **does not** contradict any promoted theorem. `BOOK-OFFAXIS` §10 P5's
2026-08-29 correction already states that the finite reduced `(w,M)` theorem
"[does not quotient] last-vertex `nu`, `kbar`, full pattern degree,
partner-dependent merge legality, and mixed/full-cell families ... for all
consumers", and records the census as `0 DEAD / 0 ALIVE / 2691 OPEN`. This
family is a concrete witness for that already-declared rider, not a
counterexample to it. The target's §8 says exactly this.

It **does not** prove occurrence, landing, coefficient gluing, Statement 3.9
compatibility, a polynomial pair, a counterexample, a panel conclusion, a
degree bound, `G2`, or JC2. I found no sentence in the target that
overreaches on any of these; §0, §2's last paragraph, §7 stop rule 4, and §8
each restate the fence, and the record's `realization="NOT_ASSERTED"` plus
`coverage_debt` carry it into the artifact.

**Attack 5 result: CONFIRMED in both directions.**

## 7. Required repair, one narrowing, three nits

**R1 (required).** `dq_0 = 4 -> 3`, in §2's fixed inner tuple and in the
record's `inner_u2.dq`. Basis and consequences in §3.1. This changes the
record's canonical JSON and therefore its family hash.

**N1 (narrowing, not a defect).** §0's headline "Full `i`-synchronization
does not kill the repaired family" is established only for the *ratio /
agreement* content of `(IS)`, which is what §6 actually proves. It is not
established against an **absolute bound** on the index. Per
`TEMPLATE-ATTACK` §1a L5/MP6(b), the common merge index is
`i = b_e*alpha*prod(nu_seg)`, and on this ray `prod(nu_seg) = nu_1 = 5K =
i_2/(2 i_0)` is the *unique* `K`-growing global quantity. So any promoted
upper bound on `i` — or equivalently on `prod(nu_seg)`, or on the entry
`e`-sequence, since L6's e-ladder forces `nu_1 | e_{j-1}` — caps `K` and
kills all but finitely many members at a stroke. §6's escape hatch is
phrased as source scales that *disagree*, and §7 stop rule 4 as an
"independently variable source `i` scale"; the operative risk is
**boundedness**, not disagreement. Suggested one-line addition to §6, and a
`coverage_debt` entry `"absolute_index_or_prod_nu_bound"`.

**Nit 1.** The record names `"N1_L6"` in `legality` but carries no dedicated
N1 certificate field, even though N1 is the entire reason this report
exists. The pinned `EQJOIN-FAMILY/v1` precedent does carry one
(`n1_radical`). The predicate is recomputable from the stored affine laws
(`gcd(60q+12, 30q+5) = gcd(30q+5,2) = 1`), so this is a completeness nit,
not an error; §4's own sentence "the ... N1 certificate ... may not be
dropped" reads oddly against a record that stores only the label. Suggested:
`n1_certificate = {kbar_mod_nu:"2", reason:"t odd and K odd => gcd(2,5K)=1"}`.

**Nit 2.** §2 labels the middle vertex `P1` while `BOOK-OFFAXIS` §10 uses
`P0/P1/P2` for the priced-step, terminal-psi, and merge-pricing *rules* —
and the same paragraph calls that vertex "one clean neutral P0". A reader
can easily parse "two symmetric P1 arrivals" as invoking the terminal rule.
Rename the vertices `V0/V1/V2` or `U_in/P/U_out`.

**Nit 3.** §5.2 says the outer coupling "becomes affine on this ray". On the
ray it is stronger than affine: it is an identity (both sides `100K^2+20K`),
so it imposes nothing. Worth saying, since a consumer might otherwise
re-derive it as a live constraint.

## 8. Counterexample attempts

**Primary attempt — kill the repaired ray with a promoted local rule.** For
`q=0..3000` (exact `Fraction`, no caps in the closed forms) I evaluated
every predicate I could source from the pinned grammar: N1/L6 at the P0;
N1 vacuity at both `nu=1` U2 vertices; `kbar_1 in Z`; `kbar_2` non-integral
but legal; St 8.4 on both edges; MP2; arrival coprimality; the P2 neutral
arrival law `nu ≡ -1 (mod h)`; positivity and integrality of `j` and `n`;
strict searrow at both vertices; NE/(R); the §11 T1 zero-chain law `dp|dq`;
St 8.5 applicability; integrality of `i_1,i_2` and of `D_0,D_1,D_2`; both
Prop 9.3 transports; the outer coupling; and both T1 verdicts. **Every
predicate returns the identical value on every member** — the value set for
each is a singleton across the whole range. There is no `q` at which the ray
can be separated. The attempt **fails**; no counterexample exists at this
tier.

**Secondary attempt — the DEPTH handshake.** Described and withdrawn in
§4.1: it is the `mu_e=1` specialisation and does not apply at `mu_e=3`. This
one is worth recording because it is the most inviting false kill in the
file: it produces a crisp-looking `-8=0`.

**Tertiary attempt — mixed-`t` / mixed-`K` siblings.** Described in §4.3.
Failed, and it revealed that equal-weight plus `(IS)` are weaker than the
symmetric-copy assumption, so no sibling contradiction is reachable.

**Negative control (mandatory, retained).**

```text
K=6q+1, t=2, nu=2K, kbar_1=4K+2  =>  gcd(kbar_1,nu)=2  =>  DEAD_N1_L6, all q.
```

Verified exhaustively for `q=0..3000` with `N1_L6` the **sole** failing
predicate, which is what makes it a sharp validator: it detects exactly the
omission in both prior lanes and nothing else. Any successor validator that
accepts this mutation has dropped N1/L6.

## 9. Cheapest exact discriminator and minimum safe canonical statement

**Cheapest exact discriminator.** Decide whether the merge index `i` (or,
equivalently, `prod(nu_seg)` along the inter-merge segment, or the entry
`e`-sequence value `e_{j-1}` that L6's ladder forces `nu_1` to divide) is
bounded at a fixed entry. This is the cheapest by a wide margin: it is one
inequality against a quantity the campaign already computes
(`i = b_e*alpha*prod(nu_seg)`, `TEMPLATE-ATTACK` §1a L5), it needs no new
local-grammar theorem, and on this ray `nu_1 = 5K` is the *only* `K`-growing
global quantity — so a bound `i <= B` immediately gives `K <= B/(10 i_0)`
and collapses the family to finitely many members. Everything else on the
shortlist is strictly more expensive: promoting `i`-sync to a *kill* changes
nothing here (§4.2), the sibling layer cannot discriminate (§4.3), the
downstream terminal descent is uniform in `K` (§4.3), and coefficient
gluing / Statement 3.9 is the most expensive branch of all.

**Minimum safe canonical statement.** At the declared tier the following is
theorem-grade, and I would not promote a word more:

> Fix characteristic zero and the labelled three-vertex route
> `inner U2 (nu=1, a=1, r=2, mu=3, L=1)` --case II, `l=3`--> `clean neutral
> P0 (eps=k=lex=Sm=0, s=1, E=3)` --case I, `h=3`--> `outer U2 (nu=1, R=2,
> L_outer=K)`. (a) With `nu_P0 = 2K` the route is **dead for every `K`** by
> N1/L6 primitivity, `gcd(kbar_1,nu_1)=gcd(4K+2,2K)=2`; every other
> predicate on the reviewed list passes, so this is a sharp negative
> control. (b) With `nu_P0 = tK` the route passes the full promoted local
> list — positive edges, strict (R)/NE and searrow, St 8.4 on both edges,
> MP2, arrival coprimality and the P2 neutral arrival law, N1/L6, the clean
> P0 ODE, and both U2 T1 verdicts — **iff `t ≡ 5 (mod 6)` and
> `K ≡ 1 (mod 6)`**. (c) At each fixed such `t` the resulting set of routes,
> together with its edge indices `j=2tK-1`, `n=4t-2`, its primitive index
> ratios `(1,2,2tK)`, its full degrees `(6, 6tK, 12tK)` and `D`-values
> `(6, 12tK, 24t)`, and its reduced rational frame data, is one linear set
> in `q` where `K=6q+1`, hence one semilinear family record. (d) The union
> over `t` is not semilinear, since its graph contains `nu=tK`. (e)
> Consequently no invariant that factors only through the reduced P0 state
> `(w,M,lambda)=(2,3,0)`, the two local edge equations, St 8.4, MP2,
> arrival coprimality, N1/L6, or local T1 bounds `L_outer`.
>
> This is a statement about formal labelled routes only. It asserts no
> landing from a source entry, no coefficient gluing, no polynomial-pair
> realization, no bound on the absolute index or on `prod(nu_seg)`, no
> panel decision, no degree ceiling, no `G2`, and no JC2 conclusion.

Clause (a) is the part that is new and that the prior lane got wrong;
clauses (b)--(e) are the target's contribution, and they stand as written
once `dq_0` is corrected to `3`.

No web, AWS, heavy computation, canonical edit, target edit, round-artifact
edit, commit, push, or `jc2-lean` access of any kind was used.

---

Report-body SHA-256 (all bytes strictly before the final separator):
`11bcc272d379622cc0105f50a7351fc728f4609f87e7e711cf8bf7a28d40b06c`.
