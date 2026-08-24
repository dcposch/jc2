# Round-2 `NORM-MOMENT-SEP` — bounded R-root report

- **Producer/session:** OpenAI Codex, Bacon/R receiver lane
- **Round:** `20260824`, consolidated R root
- **Basis commit:** `8bf25a52f5f6c20886b77c6d9aeeb879eb18f8e4`
- **Preregistered:** `2026-08-24T02:40:55Z`, SHA-256
  `15caf35ca825f7a56bb6766cf585b4845c41a491904a748301264a7eb708330b`
- **Run frozen:** `2026-08-24T02:50:27Z`
- **Status:** INTERNAL / EXACT PRODUCER-CHECKED; no shared-ledger promotion

## Verdict: `DIFFERENT-INSUFFICIENT`

The preregistered fixed-different separator fired and stopped the entire root.
Two exact denominator-42 formal Darboux completions have the same finite local
algebra, different and target-derivation conductor, selected contact/gcd
decoration, coordinate valuations, local Jacobian two-form, and full first
principal part of `Tr(x)`, but different quadratic principal parts.  Their
`t^-1` coefficients in `Tr(x^2)` are respectively `84` and `168`.

This is the narrow negative result the gate was designed to detect: the listed
local algebra/different/contact data do not determine the quadratic coordinate
moment.  It is not a global identity, a polynomial Keller countermodel, or a
statement about JC2.

## 1. Frozen contract and confirmed review

The preregistration was written and hashed before computation at
[`PREREGISTRATION.md`](../cases/round2_norm_moment_sep/PREREGISTRATION.md).
It fixed four records, moments `m=1,2`, two independent trace/different
calculations, exact verdict precedence, and a hard stop before the native type
gate when `DIFFERENT-INSUFFICIENT` fires.  It forbade all-`m` trace work,
resultant construction, theorem descendants, network use, external contact,
and shared-ledger edits.

The confirmed P1/P2 review was read at
[`review-round1-proof-gates-claude.md`](review-round1-proof-gates-claude.md),
SHA-256
`ef0bf14d10abfedb5c4b8921344ff9de1dc0078f287ed5c6fe3fc7a24a522e11`.
It confirms the P1 `COSTUME` perimeter and the P2 `INSUFFICIENT-DATA` trace
formulas/collision.  No round-1 code was imported: the local algebra, different,
and moments below were separately rederived and implemented using Python's
standard library.

## 2. Independent exact derivations

Put `K=QQ(q)((t))`, `L=QQ(q)((u))`, and `t=u^e`.  In the power basis
`1,u,...,u^(e-1)`, companion reduction gives

```text
u^n = t^floor(n/e) u^(n mod e),  0 <= n mod e < e.
```

Taking diagonal entries of the multiplication matrix, independently of the
roots-of-unity/divisibility filter, gives for every integer `n`

```text
Tr_(L/K)(u^n) = e*t^(n/e)  if e divides n,
                 0          otherwise.
```

The minimal-polynomial derivative gives

```text
Different(QQ(q)[[u]] / QQ(q)[[t]]) = (e*u^(e-1)).
```

Independently, the trace-pairing matrix has one nonzero entry in each row.  Its
determinant is

```text
(-1)^floor((e-1)/2) * e^e * t^(e-1),
```

which agrees exactly with the norm-of-different calculation, including the
sign, for all four records.  The implementation keeps these as distinct
algorithms, and all comparisons passed.

## 3. Receiver and controls

Each exact record carries a target-affine divisor tag, the finite monogenic
local algebra and basis, different/discriminant, completed-factor census,
rational coordinate multiplication expressions, retained decoration, local
Jacobian data, and canonical first/second principal-part hashes.

| Record | Exact role | Decisive observation | Result |
|---|---|---|---|
| `C1` | triangular automorphism `(P,Q)=(x,y+x^2)` | unit different; no negative principal part for `x,x^2,y,y^2` | PASS |
| `C2` | nonproper non-Keller map `(P,Q)=(x^2,xy)` | `Tr(y^2)=2q^2/t`, while both first moments cancel | PASS |
| `D1` | formal Darboux completion, `e=42,b=1` | quadratic residue `84` | PASS |
| `D2` | formal Darboux completion, `e=42,b=2` | quadratic residue `168` | PASS / STOP |

For `b=1,2`, the separately constructed pair is

```text
x_b = u^-84 + u^-42 + u^-30 + u^-10 + u^-5 + b*u^42,
y_b = q*42*u^41 / (d x_b/du),
t = u^42.
```

Direct differentiation verifies

```text
dx_b wedge dy_b = d(u^42) wedge dq = 42*u^41 du wedge dq.
```

Both cases have `ord_u(x_b)=-84`, `ord_u(y_b)=126`, different
`(42u^41)`, gcd chain `42 -> 6 -> 2 -> 1`, characteristic indices
`(7,3,2)`, and the same retained contact-visible terms.  Two independent trace
algorithms agree with

```text
Tr(x_b)   = 42*(t^-2 + t^-1 + b*t),
Tr(x_b^2) = 42*(t^-4 + 2*t^-3 + t^-2
                       + 2*b*t^-1 + 2*b + b^2*t^2).
```

Consequently the complete first principal parts coincide, while the quadratic
principal parts do not.  Positive `u`-valuation certifies that the first two
`y_b` moments have no negative principal part.

## 4. Hard stop and perimeter

The exact stage results are:

```text
receiver controls:         PASS
fixed-different separator: PASS_STOP
native source type gate:   NOT_REACHED_BY_PREREGISTERED_HARD_STOP
global separator:          UNAVAILABLE_NOT_PREREGISTERED
```

Thus this run makes no `NO-TYPED-FUNCTOR` finding and no claim about whether a
native GGV packet populates the receiver.  The pinned farm manifest was only
hash-audited; the conditional type gate was not executed after the earlier
stop.

The separator applies only to an argument whose hypotheses consist of the
displayed local finite algebra, different/derivation conductor, selected
contact decoration, coordinate valuations, and local Jacobian two-form.  The
coordinate multiplication data themselves differ and, as they must, determine
the differing moments.  A genuinely global polynomial-origin identity could
still impose additional relations.  The Darboux completions are formal-local
controls rather than polynomial Keller maps; `m<=2` is a discriminator, not an
integrality test.  Nothing here proves trace regularity, finiteness,
properness, an automorphism, a counterexample, or any conclusion about JC2.

## 5. Artifacts and replay

- Exact implementation:
  [`norm_moment_sep.py`](../cases/round2_norm_moment_sep/norm_moment_sep.py),
  SHA-256
  `150cdc2fb211d20685694e698eeb14f295c7d660be419eb8642d339815255601`.
- Compact certificate:
  [`results.json`](../cases/round2_norm_moment_sep/results.json).
- Replay instructions:
  [`README.md`](../cases/round2_norm_moment_sep/README.md).
- Full deterministic JSON stdout: 41,522 bytes, SHA-256
  `c81c75b0cc3721f1198d3dc049f66cd3c87fdb24c81e6542d7cecfd15bffae96`.

Replay from the repository root:

```sh
python3 cases/round2_norm_moment_sep/norm_moment_sep.py \
  | LC_ALL=C shasum -a 256
```

The run uses exact integers/fractions and sparse Laurent polynomials over
`QQ[q]`; it performs no sampling, moment above two, network access, or external
write.
