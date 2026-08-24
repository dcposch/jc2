# Weighted D-source gate — `WEIGHTED-D-SOURCE-GATE-20260824`

**Frozen verdict:** **`NO-TYPED-SOURCE/NO-QUOTIENT`**  
**Frozen UTC:** `2026-08-24T06:45:54Z`  
**Basis:** `dd11599b07eb05591b5c006791005eef19457d8e`  
**Frozen synthesis:** `xmodel/ideation-20260824T0453Z-synthesis.md`,
SHA-256 `76d9b7685771f65138fcb3c3dba1cfdd1ab104a9a5b21a7e3262c971f96ff790`

This is a source-typing verdict only.  It edits no shared ledger, enters no
band 28/deeper D calculation, consumes no integral D43 object, and launches
no syzygy or generic state search.

## 1. Result and first stop

The exact normalized polynomial factors are defined abstractly by

\[
U_f=1+\sum_{m=1}^{42}\alpha_m t^{42m},\qquad
U_g=1+\sum_{m=1}^{63}\beta_m t^{42m}.
\]

The repository does **not** contain a promoted producer registry giving a
named full-polynomial source point and tangent maps for even
`alpha_1,beta_1`.  The reviewed D-state producer records

```text
alpha_beta_classification: null
typed_shift_projection_map_present: false
```

and its pure-y constructor has signature `build_jets(point,p,Z)` with exactly
the 30 y-streams and no x-factor input.  The next coefficients
`alpha_2,beta_2` occur only in the implementation specification's formal
finite sequence; there is no implementation registry, completion value,
held/derived/independent classification, or chain rule for them.

The P4P1 producer does not fill this gap.  It adjoins `Xf_alpha` and
`Xg_beta` as **external independent symbols** after loading the band-42
checkpoint; both checkpoints contain zero occurrences of those names.  The
exact correction is a valid compiler-interface identity, but the external
symbols are not the tangent of a named polynomial-source scheme.  Likewise,
`cases/eplus43.py` explicitly says that its independent tangent declaration
and `alpha=beta=0` value are fail-closed constructor choices because no
repository derivation exists.  That tool is internal/unreviewed and reaches
only `O(t^84)`, not the second factor coefficient.

The first-stop rule therefore fires before a quotient or recognizable-state
test is licensed.  The verdict is not `TWO-DRIVER`: the universal second-level
formula contains a carrier term, but no sourced tangent exists on which to
decide whether that term is independent, derived, or zero.  It is not a
Hankel pivot: there is neither a typed input alphabet nor a producer-declared
full-source state dimension.

## 2. Actual producer perimeter and hashes

### 2.1 Full-source expressions and the missing registry

| Artifact | SHA-256 | Exact content relevant here | Boundary |
|---|---|---|---|
| `ladder/SHEET6-DIRECTIONB.md` | `1b26369fdadfa41c7c575b9106d386d2bad182d7e0b91f7a0a604dac8ad3cdef` | Branch-product J identity; `phi_f,phi_g` have degrees 42,63 and first enter at `t^42`. | Gives onset, not coefficient values/tangents. |
| `ladder/SHEET6-DIRECTIONB-REVIEW.md` | `5da561d3faf834cdb3acc764b3a4c4fba4150832886b50c1279b183a3e096a18` | Independently checks the clean window and `1+O(t^42)` factor. | Stops before the x-factor source model. |
| `xmodel/sol-xside-spec.md` | `f946a4ae65965200d5138b6a213945f1a3be6076fa8da1bfac9d4ba24381d9ff` | Exact definitions `alpha_m=c_{f,42-m}/c_f`, `beta_m=c_{g,63-m}/c_g`; exact full product rule. | Labels `X-SIDE-DERIVATION` and `X-SIDE-30` conjectural; says no values are present. |
| `ladder/SHEET6-R1.md` | `ad63701bc1614dfd53edf99ade0e5c1743ceada3c9a9cdac38ef29a5e9701fe9` | Section 16.5 specifies the needed R2 x-side/h-Newton build. | Explicit future work, not a registry. |
| `cases/valuation_e2.py` | `c1a858fbe53c291038b0386c124dbfd4bc79400eedc6b9d5d49a4088736d08f8` | Actual promoted pure-y registry and unreduced producer. | `build_jets(point,p,Z)`; 30 y streams, no alpha/beta. |
| `cases/eplus43.py` | `94db6c25df5254a040522b7bd5afe38f19577c267c8e61f57b05d3b0dfd3fe1c` | Multiplies by `1+alpha*t^42`, `1+beta*t^42` before Euler rows. | Internal/unreviewed; independently declares tangents and zero values while explicitly admitting no source derivation; no level two. |

The reviewed D-state chain which confirms the absence is pinned by:

| Artifact | SHA-256 |
|---|---|
| `cases/round2_dstate_gate/MANIFEST.sha256` | `725edba2f34a20bcd4a062ac97baf0924000c84efccab38dbb1565b3fefbaa99` |
| `cases/round2_dstate_gate/dstate_gate.py` | `d312c84bfe601e667c74b2453ef09287d5b2dd9796e4201d57b6b364debae309` |
| `cases/round2_dstate_gate/results.json` | `4ca07ad9c922acec962b508e857d69c5db7ae336c3f0723837e2a0799d6f225f` |
| `xmodel/round2-dstate-gate-20260824.md` | `57536d0557d4aaaf267ce493c3236b33eed1c1d2829484e496211934ea78d512` |
| `xmodel/review-dstate-grok.md` | `b4a0fec6d4aa0e21ccaf325c8ad12b78c426b131698903500c018393251426dc` |

### 2.2 P4P1 producer and registry status

The exact band-42 assembler sources are:

| Artifact | SHA-256 | Registry fact |
|---|---|---|
| `cases/d43_family2.py` | `8c0f7fd3ea1efb54293036e1caa481519682251ec554e8dac4cb254b4f2ca013` | Says alpha,beta are adjoined as independent variables. |
| `cases/d43_nf_certificate.py` | `41865448d3de9d0d47a9c0d086a343ea7a46b00688699d2e8b304adb0be5945b` | Creates the two external one-symbol groups in `rung_kernel`. |
| `cases/round2_p4p1_honesty/MANIFEST.sha256` | `fef9eae832f53634e4cb29e8b850ba79d28f326688fab919787dc1ad1aeb10c2` | Pins the producer/replay perimeter. |
| `cases/round2_p4p1_honesty/results.json` | `d0123adb31a1ee7aead8c7b5b0899fc68094a87700bbdff69867514f2efd002c` | Both checkpoints: sidecar absent; base extension variables exactly `Xf_alpha,Xg_beta`. |
| `xmodel/round2-p4p1-honesty-20260824.md` | `c744c983c41055f45a509b0764b60d07312d5b172ef162183fa4342b7be1042f` | Producer verdict `ORIGIN-ONLY`. |
| `xmodel/review-p4p1-honesty-grok.md` | `64a64c29493c46f86e05657457666b02ecab053cfe2e025ca914e6eb7af14d6e` | Different-model confirmation of the identity and external-symbol boundary. |

The complete 25-file source-hash inventory is stored in the replay result.
All hashes matched disk.

## 3. Predeclared source, target, and state category

The preregistration froze the required source as the producer-certified
Zariski tangent `T_src=T_s(S_full)` at one named normalized polynomial-source
completion.  Through factor level two it must provide stable maps

\[
D\alpha_1,D\beta_1,D\alpha_2,D\beta_2:T_{src}\longrightarrow k
\]

and every relation or held/derived/independent classification.  A free formal
span in those four symbols is allowed for algebra replay only; it cannot
support a source verdict.

The predeclared codomain is unreduced:

\[
Y_{[1,2]}=k[\eta]e_{42}\oplus k[\eta]e_{84}.
\]

No eta selector, normal form, modular row, or origin specialization is part
of this target.  The allowed state category is a causal finite-dimensional
linear recognizable transducer on factor index `m`, with the Euler counter
admitted over the Ore relation `S*m=(m+1)*S`.  A Hankel minor could refute
only a producer-declared dimension in that category.  No such full-source
dimension is registered.

Preregistration SHA-256:
`200fa1189174260f426ce7d639cadb909a8155fabfff86721be84e0ad5f8cdd6`.

## 4. Universal two-level derivation from the unreduced product

This algebra is exact but ambient: it records what a future source registry
must feed.  Put `q=t^42` and write

\[
\begin{aligned}
U_f&=1+\alpha_1q+\alpha_2q^2+O(q^3),\\
U_g&=1+\beta_1q+\beta_2q^2+O(q^3),\\
C&=1+c_1q+c_2q^2+O(q^3),\\
R&=1+r_1q+r_2q^2+O(q^3).
\end{aligned}
\]

Direct division and multiplication give

\[
\begin{aligned}
c_1&=\beta_1-\alpha_1,\\
c_2&=\beta_2-\alpha_2+\alpha_1^2-\alpha_1\beta_1,\\
r_1&=3\alpha_1-2\beta_1,\\
r_2&=3\alpha_2-2\beta_2+3(\alpha_1-\beta_1)^2.
\end{aligned}                                                \tag{4.1}
\]

The replay independently verifies `U_f=RC^2` and `U_g=RC^3` through
`q^2`.  Every coordinate-change tangent term is

\[
\begin{aligned}
\delta c_1&=\delta\beta_1-\delta\alpha_1,\\
\delta c_2&=\delta\beta_2-\delta\alpha_2
 +(2\alpha_1-\beta_1)\delta\alpha_1-\alpha_1\delta\beta_1,\\
\delta r_1&=3\delta\alpha_1-2\delta\beta_1,\\
\delta r_2&=3\delta\alpha_2-2\delta\beta_2+6c_1\delta c_1.
\end{aligned}                                                \tag{4.2}
\]

Let `Phi=Phi_y`, `Gamma=Gamma_y`, and define the unreduced series

\[
\begin{aligned}
B&=(\theta\Phi-12\Phi)\Gamma_\eta
   -\Phi_\eta(\theta\Gamma-18\Gamma),\\
A&=\Phi\Gamma_\eta-\Phi_\eta\Gamma,\\
D&=2\Phi\Gamma_\eta-3\Phi_\eta\Gamma.
\end{aligned}
\]

Substitution of `U_f=RC^2`, `U_g=RC^3` into the product rule, before
coefficient selection, gives the exact identity

\[
\boxed{
B_{\rm full}=R^2C^5B+RC^5(\theta R)A+R^2C^4(\theta C)D.}     \tag{4.3}
\]

For the exact leading forms `Phi_0=S_Mp^2`, `Gamma_0=G_Mp^3`,

\[
B_0=0,\qquad D_0=0,\qquad A_0=S_MG_Mp^4p'.                 \tag{4.4}
\]

Write `B_42=[t^42]B`, `A_42=[t^42]A`, and similarly at 84.  The first
genuine factor occurrence is

\[
\boxed{[t^{42}]B_{\rm full}=B_{42}+42r_1A_0.}              \tag{4.5}
\]

Its complete tangent is

\[
\delta[t^{42}]B_{\rm full}
=\delta B_{42}+42(A_0\delta r_1+r_1\delta A_0).             \tag{4.6}
\]

At the current held-leading-form convention, `delta A_0=0`; (4.5) then
specializes to the reviewed P4P1 correction

\[
42S_MG_M(3\alpha_1-2\beta_1)p^4p'.
\]

The second factor occurrence, still before any row reduction, is

\[
\boxed{
\begin{aligned}
[t^{84}]B_{\rm full}={}&B_{84}+(2r_1+5c_1)B_{42}
 +42r_1A_{42}\\
&+\{84r_2+42r_1(r_1+5c_1)\}A_0+42c_1D_{42}.
\end{aligned}}                                             \tag{4.7}
\]

Set

\[
H=84r_2+42r_1(r_1+5c_1).
\]

Retaining every chain-rule term gives

\[
\boxed{
\begin{aligned}
\delta[t^{84}]B_{\rm full}={}&\delta B_{84}
 +(2\delta r_1+5\delta c_1)B_{42}
 +(2r_1+5c_1)\delta B_{42}\\
&+42\delta r_1A_{42}+42r_1\delta A_{42}\\
&+\delta H\,A_0+H\,\delta A_0
 +42\delta c_1D_{42}+42c_1\delta D_{42},\\
\delta H={}&84\delta r_2
 +(84r_1+210c_1)\delta r_1+210r_1\delta c_1.
\end{aligned}}                                             \tag{4.8}
\]

Equations (4.2) and (4.8) include both x-factor and pure-y chain rules.  A
future producer must supply their pullback to `T_src`; none is presently
banked.

The structural information is sharper than the row-42 sidecar alone:

- level 42 sees only the weighted invariant `r_1`;
- level 84 sees the new invariant `r_2` **and the old carrier coefficient
  `c_1`** through four displayed couplings; and
- `c_2` drops out at this level only because the exact identities
  `B_0=D_0=0` kill its two possible leading terms.

Thus first-order cancellation of the common carrier is not source-stable by
formal algebra alone.  Conversely, (4.7) is not a `TWO-DRIVER` certificate:
on the true source, `Dc_1` could be zero, derived from `Dr`, or annihilated by
relations among `B_42,A_42,D_42`.  Deciding that requires precisely the
missing producer tangent.

The canonical formal formula/Jacobian digest is
`4491acc66ea6c2931ecd3c31d501439bae6505787869f4f15023fdc322a6207b`.

## 5. Fail-closed decision table

| Required gate | Result |
|---|---|
| Exact finite definitions of `alpha_m,beta_m` | **PASS**, specification tier |
| Named full-polynomial source scheme and completion | **MISSING** |
| Producer values/classification for `alpha_1,beta_1` | **MISSING**; external compiler symbols and a named zero control are not provenance |
| Producer registry for `alpha_2,beta_2` | **MISSING** |
| `Dalpha_i,Dbeta_i` pullback to stable source labels | **MISSING** |
| Covariance of the common-carrier action on the normalized source | **NOT PROVED** |
| Sourced absorption of `C` | **NOT PROVED**; formal level 84 contains `c_1` |
| Producer-declared full-source state dimension | **MISSING** |
| Licensed Hankel or recurrence test | **NO** |

The first missing row is already enough for the frozen verdict.  Formal
identities (4.1)--(4.8) are banked only as the exact acceptance target for a
future R2/full-source producer.

## 6. Replay artifacts and reproduction

| Artifact | SHA-256 |
|---|---|
| `cases/weighted_d_source_gate_20260824/PREREGISTRATION.md` | `200fa1189174260f426ce7d639cadb909a8155fabfff86721be84e0ad5f8cdd6` |
| `cases/weighted_d_source_gate_20260824/replay.py` | `2c63d6859f2d4bacd27a5536fc1e8bbbf7171ccd2d2229b4c0b63d7ec6ee247a` |
| `cases/weighted_d_source_gate_20260824/results.json` | `ed385ba935b509b5b573d31d4b2fab5c9cbe56bf473d3d61e5eede03cb6884ac` |

Replay:

```text
python3 cases/weighted_d_source_gate_20260824/replay.py \
  --expected cases/weighted_d_source_gate_20260824/results.json
```

It returns

```text
PASS NO-TYPED-SOURCE/NO-QUOTIENT
95eceeb60465bc21948ab39263ffe91dfd269e8c04a993946f689b93842b0b4a
```

The replay is read-only.  It hashes the complete producer perimeter, parses
the actual constructor signature and reviewed JSON fields, checks the
external-sidecar status at both primes, expands the weighted coordinate
change through `q^2`, verifies (4.3)--(4.8) in an exact integral polynomial
ring, and asserts that no forbidden work was entered.

## 7. Resurrection condition

Reopen this gate only when one producer artifact supplies a named normalized
polynomial-source completion through factor level two, stable source labels,
values and tangent maps for `alpha_1,beta_1,alpha_2,beta_2`, and all source
relations.  The artifact must reconstruct those coefficients from
`phi_f,phi_g` or an exact R2/h-Newton model and replay the chain rule.  A new
external sidecar assignment, another modular D row, or the line
`3 alpha_1-2 beta_1=0` is not a resurrection trigger.

No recurrence, pivot, syzygy, D43 integral claim, germ, characteristic-zero
point, or JC2 inference is emitted.
