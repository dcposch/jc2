# Research lane: B0 — no trivial dicritical for a Keller map

You are the campaign's flagship proof lane. Question B0, on which the
entire rank-four transposition horn, the `A_F=B` custody item, and the
strong all-degree component bound now ride:

> Can a Keller map `F:C^2->C^2` (Jacobian a nonzero constant, `F` not
> invertible, geometric degree `N`) have a dicritical divisor `l` with
> affine image curve (a component of `A_F`) and generic local degree
> `mu_l = 1` — equivalently, by promoted Lemma 4.2, a dicritical
> divisorial valuation `v` at infinity with `v(dx∧dy)=0`?

A proof of NO at `N=4` closes the transposition horn and `A_F=B`
there, making the promoted (M′) family hold verbatim at rank four in
both classes. A proof of NO at all `N` additionally upgrades the
promoted weighted bound to `2m<=N-1` (giving `m<=2` at `N=5`).
A YES (an explicit Keller-consistent configuration or a proof that no
obstruction exists) is equally valuable — type it as a structured
candidate. Fail closed: a typed OPEN at a named missing lemma is a
good outcome; an unsourced closure is the only bad one.

charged_input=xmodel/trivial-dicritical-literature-registry-grok46-20260831.md
charged_input=xmodel/round1033-sheet-gate-opus5-20260831.md
charged_input=xmodel/round1033-sheet-gate-hostile-review-sol56-20260831.md
charged_input=xmodel/block-descent-a1-mprime-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
264ddba858b0eb54544fbf612a390c5ded9bd07eb37729b2700965015e369462  {{LANE_INPUTS}}/trivial-dicritical-literature-registry-grok46-20260831.md
6d8f6667fc7d52d1e46fc4ac55f2aa2049603f06c1764ae4ac51b078435d90eb  {{LANE_INPUTS}}/round1033-sheet-gate-opus5-20260831.md
21bbc70c0cb8007be244d576625119eae55e67fd125b149fc7c15fe87d7a5e1a  {{LANE_INPUTS}}/round1033-sheet-gate-hostile-review-sol56-20260831.md
69970f4d2c4a2c5760e116400b1b27426edc41fdf6a8d15936df14cc567855c9  {{LANE_INPUTS}}/block-descent-a1-mprime-coordinator-integration-fable5-20260831.md
```

The registry types three attack routes; work them in this order and
stop at the first that closes (or reduce to the sharpest possible
typed OPEN):

1. **Chart-Jacobian / Newton–Puiseux** (registry §7.1): in a resolved
   non-properness chart the open bit is `l-k=1` with the chart Jacobian
   `v^{l-k-1}` a unit along the dicritical; derive the transformation
   law of Chau's unresolved-chart order `det DF_phi = -m J t^{n-2m-1}`
   under the blowups producing a smooth map-dicritical, and determine
   whether the Jacobian condition excludes `l-k=1`. One valuation,
   desk-scale. Use cached `refs/` PDFs (Orevkov `jc86.pdf`, Chau) and
   fetch Żołądek 2008 (Prop 6.5-6.7) — hash everything at execution.
2. **Image-singularity / covering split** (registry §7.2): split
   `mu=1` by the covering degree `s_l` of `l` over its image. For
   `s_l=1`: immersive image (Żołądek 6.5) + smooth image excluded
   (Chau 1999 Thm 4.4 under Jung form `d>e>1` via
   Abhyankar–Moh–Suzuki) — the surviving case is an immersed nodal
   image; determine whether a `mu=1, s_l=1` dicritical onto a NODAL
   affine curve is consistent with the Keller condition (this is the
   exact surviving configuration; attack it with the promoted
   conversion law `a_p=s_p-b_p` and the (2.3′) cycle type at the
   nodes of the image, where the promoted reduced-pullback and
   semicontinuity facts apply). For `s_l>=2`: the collapsed covering
   argument on `pi_1` of the complement of a singular uniruled curve.
3. **Unique-versus-mixed at `N=4`** (registry §7.3): rewrite
   Domrina–Orevkov's unique-dicritical argument with Orevkov's
   correction terms visible so the `mu=1` dismissal becomes a numbered
   lemma; then attack the mixed remainder `(mu=2)+(mu=1)` directly —
   note the promoted budget identity forces the correction terms of
   BOTH dicriticals to vanish in the mixed profile at `N=4`
   (`sum(mu_l + corr_l) = 3 = 2+1`), so Orevkov's Lemma 4.2 equality
   case applies; determine what `corr_l=0` forces on the `mu=1`
   component (Orevkov defines `corr_l` via the local multiplicities
   `mu_x` along the chain — equality means every `mu_x = mu_l`; what
   does that rigidity give?).

Guardrails: the promoted Lemma 4.2 and conversion law may be consumed
as theorems (cite the integration). Do not consume anything the
integration marks PROVISIONAL (no `A_F=B`, no `b=0`, no `f=2` — those
are what you are proving). Distinguish map-dicriticals from
function-dicriticals (registry R15 warning). Every literature statement
must be pinned with page/lemma number and PDF hash at execution.
Deliverable: theorem with full proof (scope: `N=4` or all `N`), or a
structured YES-candidate, or typed OPEN naming the exact missing lemma
per route with your best partial results proved unconditionally.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation
of uncertain duration on this machine. Do not edit canonical ledgers,
any charged file, or inspect `jc2-lean`. Six hours hard budget.

Write one report and no other file:

```text
xmodel/b0-trivial-dicritical-proof-opus5-20260831.md
```

Create the report file with a skeleton of section headers as your
very first action and append each completed section as you finish it.
Keep it under roughly 6,000 words. End its body with a single
standalone `<!-- BODY-END -->` line and write absolutely nothing
after that line. Include a `charge_basis` declaration only if you
assert a genuinely new exit price with a direct mathematical-source
citation; otherwise omit it entirely.
