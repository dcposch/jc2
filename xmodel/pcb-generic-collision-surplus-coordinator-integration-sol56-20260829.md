# Generic PCB as quotient-collision surplus: coordinator integration

Coordinator: Sol 5.6  
Date: 2026-08-29 UTC  
Frozen campaign basis: `31777ce90994a106aade85064c0d868e32863f94`  
Lifecycle: `PROMOTED EXACT IDENTITIES / META-CLAIMS REPAIRED / QCS OPEN`

## Binding verdict

Promote the exact `QCS-IDENTITY` package below.  Do not promote the
producer's stronger dependency-independence language, do not treat its local
germ and Hurwitz passport as one structure, and do not spend the proposed
full `QCS-MARGIN/v1` packet on the filed residue-A template.  The cheapest
margin is

```text
Xi = d-s-sum_i b_i,
```

but residue A has neither an actual `PairRef` nor a complete generic quotient-
line baseline inventory.  Its only licensed result is
`UNDERDETERMINED(first_absent=PairRef)`.

This integration renames the pointwise weight excess `X(a)` to keep it
distinct from the Euler jump notation used in the Suzuki sources.

## Evidence

The Sol producer is
`xmodel/pcb-generic-collision-surplus-sol56-20260829.md`, full SHA-256
`412091929a68e8539148d00c24ee71e1d0c45185571b48be55be19d3efe0813f`,
body SHA-256
`a2cf302ad66c01980e2e70c482ab0d9914b9b616525736d5735a9de7900a147f`.

Opus 5 independently rederived every displayed identity and recomputed both
controls in
`xmodel/pcb-generic-collision-surplus-hostile-review-opus5-20260829.md`,
full SHA-256
`a1bfad2be65ed8cb0e4a9459fbe487db504f8bf012d6029fd6b49a4e8df4424e`,
body SHA-256
`7d2ab10a696a94f3160310fc7a985fd649e6bd006d83c7e6439e391466e816c3`.
Its items 1--7 are `CONFIRMED`; items 8--9 are `GAP` because the matched
controls are not one model of all reviewed inputs and the proposed successor
packet omitted cheaper and load-bearing source fields.

The independent source audit is
`xmodel/qcs-margin-residue-a-source-audit-sol56-20260829.md`, full SHA-256
`d708b3074dbe9538ce99f07d8324ab1fcd4f27871f1ca04ae276a24476c95e76`,
body SHA-256
`3e1a3824e0d4db85281f12b0c7de6c3b9d785ff5fca8148cecc7dd7c35c97be3`.
It distinguishes the minimal evaluator, full collision/Suzuki cross-check,
and downstream exit-to-line transport, and fails residue A closed before
mixing formal counts from different interfaces.

## Promoted exact identity package

Let `(f,g)` be a polynomial Keller pair, let `d=td(f,g)`, and assume the
delta-gate-passed Section-7 quotient package indexed by the proper
critical-value flags:

```text
U_i ~= A1_z,       phi_i=(P_i,Q_i),       d_i=deg(P_i),
w_i(z)=actual cluster weight,             b_i=kappa_i^+(u_i-1),
I_i=integral_(U_i) w_i dchi_c,            q_i(a)=#P_i^-1(a),
X(a)=sum_i sum_(P_i(z)=a)(w_i(z)-b_i).
```

The index set is finite: `sum_i I_i=d-1` and `I_i>=b_i>0`.  The flag sum is
one term per quotient line, as in the reviewed proof of repaired Corollary
7.1, not one term per cluster.  Then for every `a in A1`, with distinct
geometric roots counted once,

```text
d-chi_c(f^-1(a)) = sum_i sum_(P_i(z)=a) w_i(z),
X(a) >= 0,
chi_a-chi_gen = sum_i b_i(d_i-q_i(a)) - X(a).
```

Summing over `a` gives

```text
sum_a X(a)
  = sum_i(I_i-b_i)
  =: E_gen
  = d-1-sum_i b_i.
```

For a connected generic fibre of compactification genus `G`, with `s`
physical pole ends and `n` physical finite-value ends,

```text
n = sum_i d_i,
chi_gen = 2-2G-s-n,
E_gen = sum_i b_i(d_i-1)+chi_gen-1.
```

Without connectedness, replace the Euler formula by
`chi_gen=2c-2G-s-n`; the corresponding expression shifts by `2(c-1)`.
For an actual Keller pair the needed generic connectedness comes from the
reviewed primitivity input.

Consequently the generic PCB margin has two exactly equal forms:

```text
Xi
 = E_gen-(s-1)
 = d-s-sum_i b_i
 = sum_i b_i(d_i-1)-(2G+2s+n-2).
```

Generic-fibre PCB is equivalent to `Xi>=0`, equivalently
`sum_i b_i<=d-s`.  Transport from this generic statement to an every-fibre
PCB additionally needs the reviewed quotient-line interpretation and the
rider `max_a s(a)<=s`; no such transport is implicit here.

The collision identity has the opposite sign from the abandoned shortcut:
an Euler jump is collision capacity minus weight excess.  Combining it with
the Ha--Le/Suzuki nonnegative-jump criterion gives

```text
0 <= chi_a-chi_gen <= sum_i b_i(d_i-q_i(a)).
```

Thus every atypical value lies among the images of
`{0} union Crit(P_i)` and forces at least one quotient collision.  Atypicality
alone supplies no positive lower bound on `X(a)`.

## Exact control and repaired modality

For every integer `u>=2`, in the analytic boundary chart
`x=t s^u`, `y=s^-1`, the Jacobian-one ansatz `g=t` is exactly

```text
f=s^(u-1)/(u-1)+phi(t).
```

For every polynomial `phi`, its quotient line has `P=phi`, `Q=z`, baseline
`b=u-1`, and actual local cluster weight identically `w=b`, including every
collision multiplicity.  Hence the local analytic excess is zero.  This
exact family kills the cheapest claim that a collision by itself forces
strict weight excess, but every member pays a boundary pole in `f` of order
`b`.  It is not a global polynomial Keller pair.

The producer's separate degree-six Hurwitz passport agrees numerically with
one such germ, but the two objects are not glued.  Therefore they prove only
that strictness is absent from the recorded numerical/topological content;
they do not establish an independence theorem from all reviewed Section-7,
Suzuki, fibre-cover, and local inputs.  The lifecycle phrase “bridge refuted”
is superseded by this narrower statement.

## Source packet tiers and next discriminator

The minimal evaluator needs one actual source-bearing packet containing:

1. `PairRef=(f,g)` and a generic-fibre rider;
2. the complete proper-cv quotient-line inventory and every baseline `b_i`;
3. `d` and the complete physical pole list giving `s`.

The full collision/Suzuki cross-check additionally needs all `P_i,d_i`, the
actual `G,n`, an independent `n=sum_i d_i` check, connectedness provenance,
and auditable lattice data for each `b_i`.  Downstream consumption by a
selected exit budget additionally needs an injective selected-exit-to-
quotient-line map.  These three tiers must not block one another.

For residue A, formal `d=6,s=2` cannot be combined with selected lower floors
in place of the missing complete `b_i` inventory; formal series counts cannot
stand in for `n` or the quotient degrees.  No margin or budget is printed.

The cheapest live positive discriminator is now
`STRICT-COLLIDE-POLY`: decide whether polynomial origin—equivalently the
absence of the control family's boundary pole in the relevant function—forces
`w_i(z_0)>=b_i+1` at a quotient collision.  A positive theorem would give
`E_gen>=#atypical values`, still short of full QCS until an independent bound
`#atypical values>=s-1` is proved.  A falsifier must be one source-compatible
polynomial-origin germ with a collision and `w=b`; another formal or analytic
surrogate is not enough.

## Scope

This integration proves neither QCS nor PCB, constructs no actual residue-A
pair, and consumes no book budget.  It makes no flag/place/series
identification, no occurrence or attainment claim, no counterexample, and no
JC2 conclusion.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `7094`.
- Body SHA-256:
  `85c279638f2d13203f5a6e22af23785c4981c4d5f286c81127bfd91c66e37b56`.
- Frozen basis: `31777ce90994a106aade85064c0d868e32863f94`.
