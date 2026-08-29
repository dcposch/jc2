# Adversarial cross-pollination — Grok 4.6 — `20260829T1808Z`

Lane: Grok 4.6 (xAI), post-blind pre-synthesis. Lifecycle:
`ADVERSARIAL_SYNTHESIS / NO_PROMOTION / FAIL_CLOSED`. Identity: Grok 4.6.
Frozen basis (verified `git rev-parse HEAD`):
`e930fa90b8ee9d86220a2cff72fba94e04b20baa`.

This memo is not an ideation submission and does not reopen the blind
round. Blind Grok 4.6 is one input among four, not prior art belonging
to this review. Self-agreement is not evidence. No new exit price is
asserted, so `charge_basis` is absent.

## 0. Custody, method, and firewall

Recomputed full-file SHA-256 values before use. Every sealed report
below was also checked with `ops/seal.py verify` (standalone-marker
semantics). All match the packet.

```text
f7a0b2a7e6a34cb8b8ae926adf95d36db46b0dc37e6aa75a17be3dcd7ce5fea2
  xmodel/ideation-20260829T1808Z-crosspoll-packet.md
  body 11344 / 0703f1f37b7dd445c4d8b74cb06e7f1f00b996c8af89d87dac6f2263628e1961
bfa137c567e366dca26c6d0bc4a8824912cbba03d74df2bee27264000bcfb0cb
  xmodel/ideation-20260829T1808Z-sol56.md
  body 27206 / 190a5e108b767b99cdb0cbf7303bc64d8537bf0f4161324598735f8097308b88
37d1942a2ba6585c6b7d977aa5d20fd994008dbdef250a05c0425b92ac29f6ee
  xmodel/ideation-20260829T1808Z-fable5.md
  body 28151 / 1e530d1f69b8300b297e7c690b96a007b6ad85e58b62536ab017292d7800f1ee
2f65a96ff2ba2fc5d573b90c41aca57cfffb4efbe6c3bbdd2a3ea914079032cc
  xmodel/ideation-20260829T1808Z-opus5.md
  body 47459 / 486b11c0082831f295f0505fee5482d1ab1d955964e793b5a93914eed5ebdc86
190aae86c664627a8668dc219a49d8ffad7f09e4e90bc4559aa531e35288b6d5
  xmodel/ideation-20260829T1808Z-grok46.md
  body 34560 / 9257ea3daecedb627746d1b8da879776c0ccc4480fcfc77f01160a51681cb50a
f58ee9b50d640860fa36f34f12f39bcbb0f8fb852e2ace90be8e62323e09ccfb
  xmodel/ideation-20260829T1808Z-state.md
  body 9040 / d48e33c594731b4e6f0761c21c28460a15e15a7a9ea80801692b2fdc1a62529b
2ebd1d78391a145c446d2113a1801e342118773c6fd9ce63be183dfd94f15a58
  xmodel/k00-r2-full-rank-fan-provisional-sol56-20260829.md
  body 11680 / c596347cf5e343854b6838f8b7f3241c623de78250676033fc364d07bc23098c
2c918d5b0d165977bdd2b598cf48d90cf3d0dfe0922ce27213dfa01dc255e7c4
  xmodel/k00-r2-full-rank-fan-replay-sol56-20260829.py
66f119e0e46b56f067802baa9118d0080370dc404878f9db667284c2d45d54a0
  xmodel/u1-ham-kum-conn-stop-audit-sol56-20260829.md
  body 5520 / ad2d79d8e220234a315d63dd8e5b9d264084dbc824a3dc804a2588988e7813a9
```

Named tools:

```text
59add10d8b291bb85a32c8f8a155d7ff0a7c4d6dd646fc164f48304b34fd80c1
  ops/seal.py (7438 bytes)
73f7e7bb554d3ba6936eb472539eebce3425eda619e8f118d1cf29f632a6ff49
  ops/test_seal.py (4306 bytes)
```

Canonical and source files consumed (recomputed; match the state packet
where charged):

```text
6f5006f46e158bce2211a7d408e206ceef0e54d8b0781d1fa92905d57f2cabcf  APPROACHES.md
bff17fd8acb0f71fbf1ddc0b5f9d1ca30886222e03ea1f9309a92ac5cff707a0  AUDIT.md
f947045b4d747efe89a8dadc37ab46e13985ce6099e3bbd40dbd93e3b2489083  COORDINATION.md
460675f20fccbf774067f067d57b09f93a4d8e811fc0f7b7e899957a9a0ea0f0  PROGRESS.md
2adfb3b6c25552654e3bc6fbac3b54e6d3ace56a861125cde201317455450c57  ladder/REDUCTION.md
e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5  FALLACY-v2.md
4c2fd1de827361f06bcbfdd465e0cdb6f03c63203c9943f89af60b8aaaa7637d
  xmodel/u1-star-interface-no-go-coordinator-integration-sol56-93d-20260829.md
2fcf8b9d9d0f7a28c9425bf73d30ba893015c69074afef57d2425309826ace50
  xmodel/td12-u1-first-nonneutral-sextet-coordinator-integration-sol56-93d-20260829.md
6c2ca262a32488ea964d648a21f9a5e008f47f270529d9d24af3021b73ddf6f3
  xmodel/k00-valuation6-hand-obstruction-coordinator-integration-sol56-93d-20260829.md
1e3e50e7b06f6d1f5d3e24bacc93af38b3ba3c17477ecab992ad376bb5e19e7d
  xmodel/k00-r2-y0-grade8-coordinator-integration-sol56-93d-20260829.md
d72f774c53c7dcb259eefc10ff2a02202e1049b61c17486b1ba22e3773813848
  cases/max12_812_order2_u2_62_strict_rees_20260825/aws_compile_v2_jsat/run/output/compiled_v2/tails.json
2ac7653cf0c7a39970d54286b85974b39a2e6deb116839720cb1ae91f8ad6d2b
  cases/max12_812_order2_u2_62_k00_common_lambda19_kuranishi_v20_20260827/compile_contracted_source_v20r2.py
ccf96a7e17c28ced128529bcadb87962d960672727cb3da10615333499560a98
  ladder/TDBOUND.md
459bfe8e3e8e57cf554c019d8051475e74d1e8f44e23991f87ae4cbe26030a2e
  ladder/SHEET6-CLASSICAL.md
```

K00 ring map, declared: `C0=(1+d0)/256`, `C1=d1`, `C2=(1+d2)/16`,
`C3=d3`, `C4=(3+d4)/8`, `C5=d5`, `C6=1`; generator order
`(d0,...,d5)`; coefficient field `Q`, with `Q(i)` and `Q(sqrt(3))`
only where a rank cell forces the extension; image checks are the 569
weight-linear tails, `Q6=0`, and `Q` vanishing on `V(A,B)`. Matching
names are not the map. No `sat()`.

Method. Read the packet, all four blinds, the state packet, both
post-blind exact packages, `ops/seal.py`, and `ops/test_seal.py`.
Inspected the Sol replay source and its mutation controls; did not
execute that program as an oracle. Rebuilt the seven affine rows from
`tails.json` under the frozen V20R2 map in `/tmp/k00_independent_g46.py`
(stdlib `Fraction`, differently organized: polarization
`Q(x+q)-Q(x)-Q(q)`, 192-branch in `Q(sqrt(3))` rather than
`Q[r]/(r^2-192)`, univariate-`Lambda` jets). Desk runtime 1.061 s.
`python3 -m unittest ops/test_seal.py`: 6 tests, 0.54 s, `OK`.
`ops/seal.py verify` on the eight sealed packet artifacts: all `PASS`.
`rg --files .` yields zero `jc2-lean/` paths. No web, AWS, canonical
edit, commit, push, or `jc2-lean` access. No recursive POSIX search
from the repository root. No reports or prompts created after the
packet were opened; a filename listing of later `1808Z` prompt paths
occurred in a `rg` of `xmodel/` and those files were not read.

Firewall, binding. A cv flag is not a physical place and is not a
cover series. `REPRESENTATIVE` is not `FULL_ACTUAL_EXIT`. The latter
aliases `FULL_ACTUAL_FIRST_SEPARATION` and is a floor, never
attainment. A lower bound is not exact. Finite jets are not arcs,
germs, maps, or JC2 results. B and S stay separate. If no safe
replacement exists, the line is typed `OPEN`. Opus's disclosed
`grep -rl` traversal of `jc2-lean` is a process violation, not
evidence for any claim.

Evidence tiers: `PROMOTED`, `REVIEWED` (this hostile reconstruction),
`PROVISIONAL`, `PACKET`, `BLIND-OPINION`, `VERIFIED-HERE`.

---

## 1. K00 valuation-two theorem

**Verdict: `PASS`.**

No identity in the six mandated cells failed. No repair is required
of the displayed formulas. The Sol report and replay were not treated
as oracles; they named the identities the packet required this model
to rebuild.

### 1.1 Maximum typed theorem

On the exact normalized V20R2 source over a characteristic-zero field,
retain

```text
C6=1,  k10[0]=kappa != 0,
k6[0]=k2[0]=mu2[0]=mu4[0]=mu6[0]=0,
d = Lambda^2 x + Lambda^3 y + Lambda^4 z + ...,  x != 0.
```

There is no field-valued compatible jet of exact valuation two through
grade eight. `Jdet[0] != 0` remains part of the licensed source and is
not used at this grade. The source open is `D(x0) union ... union D(x5)`,
not a chart `x_j=1`.

The reduced leading locus of the seven quadrics is the linear 4-plane
`V(A,B)` with `A=16q1-4q3+q5`, `B=q0-4q2+2q4`, parametrized without
quotienting scale by `x=(2b+2u,a,b,8a+v,b-u,16a+4v)`. On that plane
the Jacobian/polar of `Q` factors rowwise as
`DQ_i(x)[q]=alpha_i A(q)+beta_i B(q)`, and every nonzero `2x2` minor
of `(alpha,beta)` is a nonzero rational multiple of
`Delta=u^2+64v^2`. Field-valued rank is therefore exactly

```text
rank 0: u=v=0;
rank 1: Delta=0 and (u,v)!=(0,0);
rank 2: Delta!=0.
```

This is a reduced point-set statement. It does not describe the
scheme structure on `V(Q)`.

Leading rank one and rank two die at grade six. On the old plane
`u=v=0`, the next coefficient `y` again has rank `0/1/2`; all three
substrata die at grade eight. Over a field in which `-1` is not a
square, leading rank one is empty; over `Q(i)` it is the two lines
`u=+-8 i v`, `v!=0`, and those lines are killed by a unit in row 6.

### 1.2 Independent checks, cell by cell

Ring map as in §0. Rebuilt 569 tails; `Q6=0`; `C3(ell)=M4(ell)=DQ(ell)=0`
and `M4` polarizes to zero between the old plane and the residual cone
(so `d[6]`, `k10[1]`, `k10[2]` cannot cancel the displayed rows).

**Cell 1.** Derived the cone from `A=B=0` (free `a,b,u,v`). Verified
`Q_i(cone)=0` coefficientwise. Polarization equals the Jacobian action
on this homogeneous quadratic, and equals `alpha A(q)+beta B(q)` with
the stated `alpha_i, beta_i`. Counted `NONZERO_RANK2_MINORS=4`; each
is a rational multiple of `Delta`.

**Cell 2.** Grade-six row 6 on the cone is independent of `y,z` and
equals `u(192v^2-u^2)/65536`. Substituting `u=+-8 i v` gives
`+- (i/32) v^3`, a unit for `v!=0`. (The blind Sol shortcut
`= u v^2/256` holds only on `Delta=0`, not identically; the
post-blind report is the one being audited and is correct.)

**Cell 3.** On `Delta!=0`, grade five forces `A(y)=B(y)=0`, hence
`Q(y)=0`. Zero-image rows 4 and 6 give the stated `H6,H4`. On `u=0`
one has `v!=0`, `b=0`, then `G6_3+(1/8)G6_1=(1/4)v^2(v+3a)` and
`G6_5+(1/128)G6_1=-(3/64)v^2(v+2a)`, incompatible. On `u^2=192v^2`,
worked in `Q(sqrt(3))` with `u=+-8 sqrt(3)\, v` (both signs), `v=1`,
`b=-2(u/v)(1+4A)`; the combinations `S5` and `S7` reduce to the
constants `1/8` and `-1/64`. Either contradicts `Delta!=0`.

**Cell 4.** Old-plane next rank two: grades 4–7 vanish; grade seven
forces `A(z)=2st`, `B(z)=s^2-64t^2`. Grade eight gives
`G8_1+8G8_3=-(3/256)D` and `G8_4=-(3/32768)F` with the stated `D,F`.
Hand identities, not replay:

```text
sD - tF     = -2uv(s^2+64t^2),
sF + 64 t D = (u^2-64v^2)(s^2+64t^2).
```

If `s^2+64t^2!=0` then `u=v=0`, contrary to rank two. If
`s^2+64t^2=0` then `s=+-8 i t`, `t!=0`, and `D=t(u-+8 i v)^2`, so
`D=0` forces `Delta_y=0`.

**Cell 5.** Arbitrary old-plane `y=ell(a,b)`: every grade-eight row is
independent of `(a,b)` (coefficientwise, not a slice). After
`z=(s^2,st/8,16t^2,0,0,0)+w` and `WA=A(w)`, `WB=B(w)`, the combinations
force `WA=WB=0`, and the remaining rows are the already promoted cubics
`(5 kappa/4096) t(3s^2-64t^2)` and `(5 kappa/65536) s(s^2-192t^2)`,
with no common zero on `D(kappa) intersect (D(s) union D(t))`.

**Cell 6.** On `u=8 i v`, `v!=0`, grade seven has the stated one-parameter
`lambda` solution. Grade eight zero-image rows force `lambda=0` and
`s=8 i t`; then `G8_2+(i/2)G8_1=-(5i/16) kappa t^3`. The minus branch
is the conjugate and was checked separately, not by Galois slogans.
`kappa=0` removes the obstruction (load-bearing control). A wrong
`B(z)` sign already fails at grade seven.

Mutation controls (independent of the Sol binary): one-byte tails
hash change is detected; a cubic monomial of row 6 with key
`(0,0,0,0,1,2)` moves the rank-one unit; `kappa` is load-bearing on
both `Q(i)` branches.

### 1.3 Scope consequence

Composing with the already promoted valuation-one seed exclusion and
the valuation-at-least-six exclusion, the normalized V20R2 support
retains only valuations `3,4,5`. None of those is attained. The
theorem excludes same-source formal arcs of valuation two, because an
arc truncates to a grade-eight jet. It does not exclude another
support or normalization, nilpotent scheme structure as a separate
object, valuations `3,4,5`, a polynomial Keller map, a counterexample,
or JC2.

A finite compatible jet in another lane would still not be an arc or
map. Promotion remains a coordinator act; this is the different-model
hostile reconstruction the packet asked for.

---

## 2. Deduplicated claim table

Fingerprint is (object, discriminator), not (label, proposing lane).
Independent convergence is a note, not a second mechanism.

| ID | Object / discriminator | Sources | Class |
|---|---|---|---|
| K00-THM | No field-valued val-2 V20R2 jet through grade 8; six rank cells empty | VERIFIED-HERE from 569 tails; Sol post-blind named the cells | **PASS** / `PROVISIONAL` pending coordinator promotion. Max theorem §1.1 |
| K00-C1 | `V(Q)=V(A,B)` 4-plane; `DQ=alpha A+beta B`; rank by `Delta=u^2+64v^2` | Opus blind §5.1 (set-theoretic from promoted identities); Sol cells 1; VERIFIED-HERE by polarization | **KNOWN-EQUIVALENT** as a cone; **NEW** as the completed rank fan. 4 nonzero minors |
| K00-C2 | Leading rank 1 dies at G6 row 6, unit `+- i v^3/32` on both `Q(i)` lines | Sol cell 2; VERIFIED-HERE | **NEW** exclusion. Over `Q` the cell is empty (`Delta` anisotropic) |
| K00-C3 | Leading rank 2 dies at G6: `u=0` incompatible linear pair; `u^2=192v^2` has `S5=1/8`, `S7=-1/64` | Sol cell 3; VERIFIED-HERE in `Q(sqrt(3))`, both signs | **NEW** exclusion |
| K00-C4 | Old-plane next rank 2 dies at G8 by `D,F` | Opus F9 unreviewed; Sol cell 4; VERIFIED-HERE plus hand `sD-tF`, `sF+64tD` | **NEW** as reviewed; was `REVIEW_DERIVED_UNREVIEWED` |
| K00-C5 | Old-plane next rank 0: G8 independent of arbitrary old-plane `y`; promoted cubics | Opus F10; promoted `y=0` integration; Sol cell 5; VERIFIED-HERE | **KNOWN** cubics, **NEW** as whole-plane invariance |
| K00-C6 | Old-plane next rank 1: both `Q(i)` signs, `lambda=0`, `s=+-8 i t`, `-(+-)(5i/16) kappa t^3` | Sol cell 6 (answers N-R); VERIFIED-HERE both signs | **NEW** |
| CAL | First-load calendar: `Q` at `2v`, `k10 D10` at `2+3v`, `k6 D6` at `7+2v`, target 19 | Grok blind; Opus §5.3 budget; Fable `LEADING-CONE-UNIVERSALITY` | **NEW** as a schedule, **KNOWN** as the min-degree table. Not a theorem. `v=3` window 7–10 is `k10/k6/Jdet`-free, not cubic-free. `v=5` is the cheapest *grade-19* two-term problem. Complementary, not contradictory |
| JETFAN | Literal-tail compiler emitting rank fans for `v=3,4,5` | Sol | **NEW** implementation client of K00-THM. Not a selector |
| OP-1 | `Delta_P=Lambda_P`: `n_P=e alpha mu_P - Lambda_P` for generic `nu` | Opus; AUDIT 9444–9451 polar bridge | **KNOWN-EQUIVALENT**. Signs check: `ord_p(g-nu)=-lambda_p` at poles, `0` else; `(G-nu Z^e)/L^e=(Z/L)^e(g-nu)` for `L(P)!=0`. Local at `P`, reduced places. Chart identification `ord F_X-(d-2)m=lambda` is the polar-bridge licence, not a new proof |
| OP-2 | `RPMC(C) <=> a_P b_P/nu_P <= C mu_P/B` per proper root | Opus; AUDIT 9381–9453; TDBOUND summed form | **KNOWN-EQUIVALENT** to existing per-root `RPMC`, **sufficient** for `KJN` (already `RPMC=>KJN`). Not a new inequality. `mu_P/B` is genuinely absent from the reduced entry `E=(alpha,beta;s;{(Lambda,a,b,nu)})` |
| OP-3 | Reduced interface is the `(mu,B)`-forgetting quotient; `U1*(R)` is a formal `RPMC(1)` countermodel; `RPMC(1)+td>=6` annihilates `U1*(R)` | Opus; U1* integration; TDBOUND | **NEW** as diagnosis/connection; **KNOWN** endpoints. Disjunction, not a verdict on either side. Empirical TDBOUND remains `COINCIDENCE-RISK` |
| OP-4 | `delta(lambda,c)=sum_{g(p)=c} e_p`; `Delta=td-chi(fibre)=td+s+n+2G-2` | Opus; promoted fibre RH | **NEW** form of **KNOWN** RH. Primitivity/`c=1` is an actual-source fact the reduced record does not carry. `n>=1` else `F` proper |
| OP-5 | Meridian cycle type of `g` on a generic `f`-fibre at `c in T_lambda` is `(e_p : g(p)=c)+1^{td-delta}` | Opus | **NEW** as a *fibrewise* local cycle calculation. **Not** a global determined passport of `F:A^2->A^2`. Does not by itself raise Avenues 7/25/26. Residue-A bookkeeping is a legitimate stage-1 experiment |
| OP-6 | Minimal-`td` selection plus T4 NF, td preserved | Opus; REDUCTION T4 | **NEW** as a spine statement. T4 *does* preserve `td` (Aut then Lemma 2.1) and applies after orbitwise degree-lex min of a *given* pair; a globally `td`-minimal pair may be so normalized. Cost: GGV farm and TRANSPORT 3.1 are forfeited; HIGH 3 (`§§7–9`) becomes load-bearing. Block-quotient-to-smaller-Keller-map remains **OPEN**. Normalization is licensed for Lemma 2.1; it is not licensed as a descent |
| SCALE | Promote `(mu_P)` with `sum mu=B` as an interface decoration; `SCALE-AUDIT` integer feasibility | Opus Card A / §6 | **NEW** as an interface object, **KNOWN** as a capacity ingredient. Audit is the cheapest discriminator. Sextet rows are **one** sample |
| EXCESS-e | Graded `sum(I_i-wt_i(a))>=e`; subtract `e` from printed pole budgets | Fable | **NEW** as a graded reading of **KNOWN** PCB-EXCESS. Consequence table that S17 and zero-slack D13/E11 die under `EXCESS-1` is **OPEN** at the ledger bridge: PCB is a finite-value Section-7 inequality, the printed U1*/sextet numbers are pole/merge floors and ceilings. Subtraction is analogy, forbidden. Typical-fibre rider is necessary and still does not identify flags with places. Full PCB killing every `U1*(R)` is the same scope jump |
| ATYP | Keller CE `=>` atypical value; atypicality `=>` `EXCESS-1` | Fable | First arrow is a **KNOWN** coordinate/fibration skeleton (primitive, smooth fibres, chi). Second arrow `WEIGHT-AT-ATYPICAL` is **OPEN**. Stop at the missing bridge. Does not force `EXCESS-1` |
| AM2 | Per-place `ord_t(f_y)=ord_t(dx/dt)-ord_t(dg/dt)` as a td12/`U1*(R)` ledger | Fable Card B; SHEET6 §2 | **KNOWN** instrument. **UNDERDETERMINED** before a full boundary contact table; residue-A was zero-slack *because* that table was pinned. Applying AM-2 per `A(F)` component supplies no new equality at the present type. Not duplicative of T1, but not a selector |
| TD12-CHAR | Inherited parent character / full-index on A7/C5/B25/S17/D13/E11 | Sol Card 2 | **NEW CLIENT** of **KNOWN** character / Statement 3.9 machinery. No typed occurrence map from characters to distinct positive events. Conditional laboratory only; not a global discriminator |
| U1-HK | `nabla_j=d+(j/r)dlog(A)` on a `D`-stable `T^r=A(f)`, map to PCB | Sol Card 1; Sol STOP audit | Audit **stands**. Conditional algebra **CORRECT/KNOWN**. Reviewed U1 row is fixed-fibre `t^r-A_*`, so **SCOPE-CONFLICT**. Displayed form is twisted-exact. Residues are Kummer monodromy, not excess events. Character count is not `s-1` places (flag/place/series). Duplicate of existing Kummer/character lanes. Homology split `(s-c)+(c-1)=s-1` is a **NEW CONNECTION** of the *target*, not a licence to launch. Reopen only on the audit's four-object gate |
| AUT-S7 | Evaluate PCB-EXCESS on `F=(x,y+x^n)`, `td=1` | Grok Card 1 | **NEW** experiment on a **KNOWN OPEN** target. Attack: automorphisms are proper, `A(F)` empty, Section-7 finite-value quotients are not defined. Expected reading `UNDEFINED`, which sharpens hypotheses (`td>=6` and/or nonproper) and is **not** a CE counterexample. Blind Grok oversold this as the principal proof attack |
| DETOUR-T | Strict actual-weight excess 1 on D13/E11 zero-slack floors | Grok Card 2 | **NEW** attack on **KNOWN** numbers. Attack: `FULL_ACTUAL_EXIT` is a floor; `10=10` is non-exclusion, never attainment. Without source prefixes the discriminator does not exist (`SOURCE_TRANSPORT_OPEN`). Do not delete D13/E11 by interior terminal budgets |
| F9F11 | Reconstruct Opus F9–F11 | Grok Card 3 | **DONE** by K00-THM. Blind Grok correctly refused to *consume* F9–F11 and incorrectly listed off-plane v=2 as a remaining client *after* F9 would close it; the firewall was right, the residual-scope sentence was too narrow |
| INGEST | Manifest-driven receipt checker | Sol Card 7 | **NEW CLIENT** of seal/basis checks. Overlaps `ops/seal.py`. Not this checkpoint's trial |
| SEAL | Standalone `BODY-END` stamp/verify | Fable proposal; Grok `verify_body_seal`; uncommitted `ops/seal.py` | **NEW** tool, **DUPLICATE** of both blind proposals, **better** semantics than first-occurrence hashing. See §4 |
| FENCE | Default fence against recursive POSIX tools | Opus Card §7; Grok recorded not launched | Wrapper helps only when used. Smallest enforceable default: §4. Do not modify `ops/lane.sh` |

Independent convergence worth keeping: (i) `V(Q)=V(A,B)` from Opus set-theory, Sol fan, and this rebuild; (ii) load calendar from Grok, Opus grade-19 budget, and Fable universality; (iii) reduced interface cannot select td12 (`U1*(R)`), all four blinds; (iv) body-seal helper, Fable+Grok+existing `ops/seal.py`.

---

## 3. Hostile notes on the other proof-side proposals

**U1 STOP audit, rechecked.** The connection formula is the logarithmic
derivative of `T^r=A(f)` along `D=X_g`, and is correct only after that
premise. The reviewed U1 packet supplies a constant `A_*` at a fixed
fibre; `dA_*=0` makes every `nabla_j` trivial, and promoting it would
convert formal fibre data into a varying source family. Twisted
exactness is tautological in the twisted de Rham complex; the `G_m`
and `A^1-{0,1}` controls show that character cohomology detects
punctures, not nonproperness. No typed map to `sum(I_i-wt_i(a))`
exists, and counting `r-1` Fourier lines as `s-1` events repeats the
flag/place/series error. Do not silently consume Sol's Avenue-16
raise. The homology split may be banked as a target correction.

**EXCESS-e arithmetic.** Internally, U1* has `lambda_floor=3R-1`,
`budget=4R-k-2`, `slack=R-k-1`. Subtracting `R-1` yields slack `-k`;
subtracting `1` kills S17 (`R=3,k=2`) and the printed zero-slack
D13/E11 continuations *if* that subtraction is licensed. It is not:
those numbers live on the reduced pole/merge ledger, while
PCB-EXCESS lives on finite-value quotient lines. Typed `OPEN` at the
bridge. Full PCB emptying every `U1*(R)` is the same jump at larger
`e`.

**ATYPICAL-EXISTENCE.** A nonproper Keller coordinate must have an
atypical value in the classical fibration sense, or the pair is an
automorphism — that skeleton is not the obstruction. Atypicality does
not force `EXCESS-1`. Stop.

**AM2-PLACE-LEDGER.** Abhyankar–Moh per place is a linear identity in
the contact table. Before that table is known the system is
`UNDERDETERMINED(list)`, which Fable already lists as an outcome and
which is therefore not a new equality. Dual-tree product-formula
crosscheck does not create missing contacts.

**TD12-SEXTET-INDUCED-CHAR.** Fail-closed character/support arithmetic
on ten named rows/edges is a cheap *conditional* preflight. It
repackages existing parent-deck / full-index / Statement 3.9
transport. Without a typed occurrence map it is not a source
discriminator of a new kind. Do not let it occupy a global slot.

**Grok AUT-S7, calendar, detour tightness, F9–F11 — self-attack.**
Calendar numbers are right and survive K00-THM as an ordering tool
for `v=3,4,5`; they are not an exclusion. Treating off-plane v=2 as
still open after a rank-fan theorem is a scope error the blind
firewall was designed to prevent and which this review closes.
AUT-S7 is a costume-map control whose likely `UNDEFINED` reading
does not touch PCB-EXCESS on nonproper maps; it must not hold the
principal proof slot. Detour tightness has no present actual-weight
discriminator. F9–F11 is this review.

**Avenues 7/25/26.** Opus raised them on OP-4/OP-5/OP-6. After audit,
do not raise: OP-5 is fibrewise, OP-6's descent seam is open, and
computing `A(F)` as a variety is still the compactification problem.
Blind Grok's unchanged vector on those rows stands.

---

## 4. Systems

### 4.1 `ops/seal.py` / `ops/test_seal.py`

Marker semantics match the packet better than first-occurrence
hashing: only a line whose entire content is `<!-- BODY-END -->`
(CRLF or LF terminated) is a marker; inline or same-line quoted
mentions do not count; missing, duplicate, or unterminated standalone
markers fail. A code-fence line that *is* exactly the marker is
standalone and correctly fails closed (quoted-on-its-own-line is a
malformed report, not a false negative). `verify` uniquely parses
post-body `Body bytes`, `Body SHA-256` (including the next-line
backtick form), and `Frozen basis`. `stamp` refuses non-whitespace
after the marker, writes a temp in the same directory, `fchmod`,
`fsync`, `os.replace`, directory `fsync`. Open uses `O_NOFOLLOW`
when present and `fstat` `S_ISREG`. Symlinks and non-regular files
are refused. Residual TOCTOU: same-inode in-place mutation between
read and replace is not detected (dev/ino check only). Tests: six
fixtures, all pass, ordinary and `-O` match on the inline-mention
case. Gaps in the suite, not in the contract: stamp-on-symlink,
invalid basis, duplicate Body-bytes, CRLF marker, fifo/dir.
Overlap: this tool supersedes Grok's `verify_body_seal.py` and
Fable's proposed `ops/seal.py`. It does not infer `charge_basis`
and does not walk the tree.

### 4.2 `FENCE-DEFAULT/v1`

A wrapper helps only when used. Global `grep` aliasing would break
legitimate `grep pattern explicit/file`. `ops/lane.sh` must not be
edited while these lanes are active. The real fence is already in
`.ignore` as `jc2-lean/` and is honoured by `rg` (`rg --files`
count 0). Bare `grep -r` / `find` / `ls -R` from the repository
root remain the failure mode; this round's prompt already forbids
them, and this review did not run them.

Smallest enforceable default that does not touch the real fence and
does not break explicit-path work:

1. Keep the prompt rule: `rg` or an explicit path; never recursive
   POSIX from the repository root.
2. `ops/fence_check.sh` against a *synthetic* `/tmp` tree containing
   a decoy `jc2-lean/` directory and one sibling file: assert `rg`
   with an ignore file skips the decoy, and that
   `grep -r --exclude-dir=jc2-lean` on the synthetic tree skips it.
   Do not traverse, list, or hash the campaign `jc2-lean/` tree, even
   as a positive control.
3. Optional `ops/rgrep` is documentation, not enforcement, until a
   later lane freeze may put it on `PATH`.

Opus's proposed control C (bare `grep -r` on the live repository)
is forbidden here.

### 4.3 One bounded systems trial

**`FENCE-CHECK/v1` against a synthetic tree.** Owner: systems
producer, different-model reviewer of the script only. Placement:
desk, `/tmp`, sub-second, no `lane.sh` edit, no real fence access.
Both outcomes: pass means the next round has a non-vacuous check that
does not itself violate the fence; fail means the exclude/ignore
wiring is wrong and the prompt rule remains the only control. Stop:
first access to the live `jc2-lean/` path, or any canonical edit.
`ops/seal.py` is already test-green; adopt it after these lanes
freeze, do not restamp live reports in this checkpoint.

---

## 5. Launches

At most three mathematical launches, jointly covering proof,
falsification, and a bypass. Conditional td12 is not a global
selector.

### M1 — Falsification: `K00-R345` / `JETFAN/v1`

**Theorem or experiment.** On the same normalized V20R2 source, there
is no field-valued compatible jet of exact valuation `v in {3,4,5}`
through the first load-bearing grade of the calendar; equivalently,
emit and kill or freeze the systems

```text
grade 2v:     Q(x)=0,
grade 2v+1:   DQ(x)y=0,
grade 2v+2:   DQ(x)z + Q(y) + (kappa M4(x) if 2+3v = 2v+2 else 0) = 0
```

with `C3(x)` only at grade `3v`, `k6` only when `7+2v` is in range,
and `b1 L6(x)` only at `v=5`. Split ranks `0/1/2` of `DQ(x)` on the
same cone `V(A,B)`.

**Order.** Shared compiler, three owners. Desk-first the two cheapest
discriminators in parallel: `v=3` calendar window grades 7–10, and
`v=5` two-term grade-19 contraction against `-5 Jdet[0]`. `v=4` after
the first of those returns. Do not infer a period-two shift.

**Dependencies.** K00-THM (this review), promoted `v=1` and `v>=6`,
frozen tails and V20R2 map (hashes in §0).

**Placement.** Desk exact `Fraction` Python, <60 s / 1 GiB per
process. AWS only if a nonempty jet must be prolonged to grade 19,
and only after preregistration.

**Both outcomes.** Empty: this support is dead and Avenue 36 moves to
a different normalization/support (new source client). Nonempty
finite jet: freeze it as `FORMAL_JET_ENVELOPE`, not an arc; then
decide extension separately.

**Stop.** First exact nonzero cokernel unit on a stratum; first
mismatch with frozen tails; no Fitting-G7; no `K00-RENORM`.

**Owner / reviewer.** Three independent producers (`v=3,4,5`) sharing
the compiler; one compiler reviewer who does not own a valuation.

### M2 — Proof: `SCALE-AUDIT/v1`

**Theorem or experiment.** For every filed entry record
`(alpha,beta,s,{(Lambda_i,a_i,b_i,nu_i)})` in the on-axis, off-axis,
td-7/11/12, and `U1*(R)` tables, plus residue-A and the Hénon tower
as controls: check `Lambda_i ?= alpha beta a_i b_i/nu_i` and
`td ?= sum Lambda_i`; then decide integer feasibility of
`B>=1`, `mu_i>=1`, `sum mu_i=B` against only *proved* constraints
(`sum_{p|P_i} m_p = alpha mu_i`, `Lambda_i=sum lambda_p`,
`lambda_p <= beta B m_p`, integrality). Report exactly one of
`NO_ADMISSIBLE_SCALE`, `ADMISSIBLE_WITH_RPMC1_VIOLATION`,
`ADMISSIBLE_AND_RPMC1_COMPATIBLE`.

**Dependencies.** OP-1 as polar-bridge, REDUCTION entry conventions,
TDBOUND §2, U1* integration. No `RPMC(1)` as a premise.

**Placement.** Desk, exact integers/`Fraction`, seconds, no CAS, no
AWS.

**Both outcomes.** Data defect: transcription kill. No admissible
`(B,mu)`: unconditional entry kill, no conjecture. Admissible with
`E_MR>1`: the reduced interface is live iff `RPMC(1)` is false —
report and stop; this is the named disjunction, not a selector.
`E_MR<=1` killed by an independent book route would be a genuine
TDBOUND falsifier and would retire the ceiling lane. Sextet rows
count as one sample.

**Stop.** First `NO_ADMISSIBLE_SCALE` or first independent `E_MR<=1`
kill; stop if the per-point form is strictly weaker than the summed
form on a promoted record (OP-1/OP-2 bug).

**Owner / reviewer.** Capacity-lane producer; different-model
arithmetic reviewer. Falsify owner: `U1*(R)` occurrence, not this
audit. Bypass: M3.

Do not launch the `RPMC(1)` theorem itself in this wave.

### M3 — Bypass: `INERTIA-EXACT` stage 1 only

**Theorem or experiment.** For a Keller pair and generic `lambda`,
the monodromy of `g` on the compactified generic `f`-fibre over
`C \ T_lambda` is transitive, with meridian cycle type
`(e_p : g(p)=c) + 1^{td-delta(lambda,c)}`, and
`sum_{non-pole p}(e_p-1)=2G-2+td+s`. First client: the filed td-6
residue-A record, where pole orders and non-pole contacts are
computed. Compare the determined fibrewise passport with the 169
admissible `S_6` passports.

**Dependencies.** OP-4/OP-5, SHEET6 residue-A place data. Not T4
beyond td preservation of the record. Not Avenue 43.

**Placement.** Desk bookkeeping. No GAP required at `td=6`.

**Both outcomes.** Strict subset of the 169: stage 1 has kill power
admissibility never had. Reproduces all 169: stage 1 is exact and
has no td-6 leverage; value stays in the (unlaunched) descent.
Neither outcome is a global passport of `F`, an `A(F)` construction,
or a smaller Keller map.

**Stop.** Do **not** start stage 2 (block quotient to a polynomial
Keller map of smaller td). That seam is `OPEN`. Stop if the
residue-A place table is missing a non-pole contact or identifies
a flag with a place.

**Owner / reviewer.** Stage-1 producer; hostile reviewer of cycle
types against SHEET6. Avenue 43 does not run in parallel in this
wave.

### Systems trial

Exactly one: `FENCE-CHECK/v1` as in §4.3.

---

## 6. Stop / defer list

Stop or do not launch:

- `U1-HAM-KUM-CONN/v1` and any Avenue-16 raise (STOP audit stands;
  four-object reopen gate).
- Grade-seven Fitting / ambient-rank packet.
- PCB or any `EXCESS-e` as a premise; Fable's consequence table.
- `WEIGHT-AT-ATYPICAL` if it needs flag/place/series identification.
- AM-2 as an equality before a contact table exists.
- TD12 inherited-character as a *global* discriminator; the
  sextet laboratory as a selector.
- `DETOUR-FULL-EXIT-TIGHTNESS` as a primary slot.
- `AUT-SECTION7-EXCESS-CONTROL` as a principal proof attack.
- `K00-F9F11-REPLAY` (done).
- Empirical TDBOUND scan (COINCIDENCE-RISK).
- OP-6 stage 2 / Avenue 26 block descent.
- Quartet revival, `j=42`, S `j=13`, valuation-one descendants.
- AWS K00, `jc2-lean`, CAPRUN caller migration, `ops/lane.sh` edits.
- Bare `grep -r` / `find` / `ls -R` from the repository root,
  including as a fence positive control.

Defer: family-aware detour exclusion `v2` (conditional, downstream of
M2's disjunction); `RPMC(1)` as a theorem until SCALE-AUDIT returns;
v=4 K00 until v=3 or v=5 speaks; Grok calendar as a separate card
(it is an input to M1).

---

## 7. Synthesis recommendation (<250 words)

Valuation two is a desk theorem on this V20R2 support: field-valued
exact-val-2 jets die by grade eight. Independent reconstruction from
the 569 tails confirms all six rank cells. Promotion, if the
coordinator so acts, leaves only valuations 3, 4, and 5, none
attained. That is a finite-jet exclusion, not a map and not JC2.

The global selector is still missing. Opus's per-root rewrite of
RPMC is the same capacity conjecture in Sigray coordinates, and it
names the scale data the reduced interface forgot; it does not prove
the inequality. `U1*(R)` is a formal countermodel to `RPMC(1)`, not
a map. Fibrewise meridian cycle types are exact local calculations
and do not determine a global passport or a smaller Keller map.
Hamiltonian–Kummer characters, EXCESS budget subtractions, and AM-2
without a contact table do not close the gap. PCB remains `OPEN`.

Do not spend the next wave on the td12 laboratory as if it were a
selector. Run the remaining K00 valuations, a scale-admissibility
audit of filed entries, and a residue-A inertia computation. Stop
the U1 connection launch, block descent, and any EXCESS kill that
identifies finite-value clusters with pole budgets. Fence checks
must use a synthetic tree; the live `jc2-lean` path stays untouched.

Nothing here is occurrence, attainment, a degree ceiling, a
polynomial Keller pair, a counterexample, or JC2.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `33481`.
- Body SHA-256:
  `20e87709b665ec3f5175c10d21535fba15b9360b67f070ea407c8bee071a5d2e`.
- Frozen basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`.
