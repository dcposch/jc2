# Fresh connection gate — secant idempotent and finite sheet algebra

- Status: **FROZEN — EXACT-SATURATION-REMOVAL / SOFTWARE-READY / NO JC2
  IMPLICATION**
- Producer: OpenAI Codex, fresh-connection lane
- Launch basis: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`
- Date: `2026-08-24`
- Scope: independent all-avenue connection search, orthogonal to the live
  sheet-six realizability and characteristic-109 support gates
- Canonical files read in full: `APPROACHES.md`, `AUDIT.md`, `PROGRESS.md`,
  the newest `notes.md` `LIVE STATE`, and
  `xmodel/ideation-20260824T0719Z-synthesis.md`
- No top-level canonical file was edited.  No web, AWS, D-depth, sheet-book,
  Witt-level, generic sparse-map, or public-communication lane was opened.

## Verdict

The selected discriminator is exact and useful, but it is an enabling
reformulation rather than a proof of JC2:

> **SECANT-IDEMPOTENT.**  Let `F=(P,Q)` be a polynomial map over a field and
> normalize `det J_F=1`.  In the self-fiber-product ring, the determinant of
> any polynomial divided-difference matrix for `F` is the unique idempotent
> cutting out the diagonal component.  Consequently the traditional
> off-diagonal saturation is exactly replaced by adjoining this one
> determinant.

Thus the collision ideal

```text
(P(x,y)-P(u,v), Q(x,y)-Q(u,v)) : (x-u,y-v)^infinity
```

is not an intrinsically saturating computation.  For a fixed telescoping
secant matrix `A(x,y;u,v)`, it is exactly

```text
(P(x,y)-P(u,v), Q(x,y)-Q(u,v), det A).
```

This gives avenue 32 a canonical, covariance-safe, three-generator exact
engine.  It does **not** show that the resulting ideal is the unit ideal for
an arbitrary characteristic-zero Keller map; that remaining assertion is
injectivity and hence JC2.  The advance is removal of an avoidable saturation
and an explicit diagonal/off-diagonal projector, not removal of the global
finiteness problem.

The repository already records a public collision-ideal neighbor using
“secant-determinant constructions” (`xmodel/websweep-2026-08-16.md`), and
multivariate Bezoutians are classical.  No literature novelty is claimed.
The campaign-new point is the exact saturation identity, its explicit
cofactor proof, and the replayable software interface.

## 1. Three idea cards

### Card A — `SECANT-IDEMPOTENT` (selected and executed)

**Connection.**  Avenue 32 (off-diagonal collision ideals) + avenue 39's
determinantal/cohomological language + avenue 46 (exact certification), with
the constant-Jacobian condition used at precisely one typed interface.

**Proposed object.**  A polynomial secant matrix `A` satisfying

```text
F(x,y)-F(u,v) = A(x,y;u,v) * (x-u, y-v)^T.
```

Use `e=det A`, not a saturation variable, to split the self-fiber product.

**Cheapest discriminator.**  Derive explicit cofactors for `e^2-e` and run
the resulting off ideal on automorphism, characteristic-positive collision,
and non-Keller controls.  Success means exact saturation removal; failure of
the arbitrary-Keller unit ideal is not counted as a refutation of the
construction.

**Why this was selected.**  It is source-polynomial, global, independent of
the held local books and support grammars, and can change software cost in the
same turn without assuming any unproved landing theorem.

### Card B — `TRIVIAL-CODIFFERENT / GLOBAL-CI-NOGO` (paper child, not run)

**Connection.**  Avenue 31 (finite normalization/Zariski Main) + the
completion-pair unit ledger + the codifferent/canonical-module interface.

For a hypothetical Keller map set

```text
A=C[P,Q],  B=C[x,y],  R=normalization of A in Frac(B).
```

The completion gate proves `R` finite free over `A`, `R subset B`, and
`Spec B -> Spec R` an open immersion.  The proposed lemma is:

> If the relative codifferent `Hom_A(R,A)` is free of rank one as an
> `R`-module, then the Keller map is an automorphism.

Indeed, write the codifferent as `eta R` inside the function field.  On the
etale open chart it becomes `B`, so `eta B=B`.  Since `B^*=C^*`, `eta` is a
scalar and the trace pairing on `R` is perfect.  The finite free algebra
`R/A` is then finite etale, hence trivial over `A^2_C`; the open immersion is
the automorphism endpoint.  If the base-change equality is hostile-confirmed,
this excludes at every rank any normalization that is a global relative
complete intersection (in particular any global monogenic normalization),
and says a counterexample completion must carry a nontrivial relative
canonical class.

**Firewall.**  “Gorenstein” alone only makes the canonical module invertible,
not globally free; its boundary line-bundle class can be nontrivial.  This
card makes no claim about arbitrary normalizations.  It generalizes the
mechanism of the reviewed rank-two gate but needs a separate duality/source
audit before promotion.  Literature priority is unchecked.

**Resurrection condition.**  A source-derived normalization `R` or surface
family with an exactly computable codifferent.  A free codifferent kills the
family; a nonfree/invertible boundary class supplies the next typed datum.

### Card C — `FINITE-SHEET-ALGEBRA` (architecture card, held)

**Connection.**  Avenues 31 and 32 + the failed trace/different receivers.
Instead of the generally nonfinite ring `B tensor_A B`, base-change the finite
normalization:

```text
S = B tensor_A R.
```

This is finite free of rank `td` over `B`.  The diagonal section is closed
because the projection is finite and open near its image because the Keller
map is etale there.  Hence it is clopen and

```text
S ~= B x S_off,
```

where `S_off` is finite projective of rank `td-1`, therefore free over
`B=C[x,y]` by Quillen--Suslin.  Its multiplication matrices are the finite
global “other-sheet” receiver that the contact-only trace packets lacked.

**Failure mode.**  Constructing `R` is the global finiteness/completion
problem; the split algebra does not manufacture it from a Sigray packet or a
formal D window.  No software starts from an abstract rank alone.

**Resurrection condition.**  An actual finite-normalization presentation, a
source-derived multiplication algebra, or an honest completion-pair surface.
Then the diagonal split, associativity, trace, codifferent, and collision
checks form a finite exact certificate.

## 2. Exact derivation of Card A

Let

```text
S = k[x,y,u,v],
f1 = P(x,y)-P(u,v),
f2 = Q(x,y)-Q(u,v),
I = (f1,f2),
C = S/I,
delta = (x-u,y-v)^T,
J_delta = (x-u,y-v) C.
```

Choose any polynomial `2 x 2` divided-difference matrix

```text
A delta = (f1,f2)^T,
e = det A.
```

The fixed replay uses the `x`-then-`y` telescoping convention, so on the
diagonal `A=J_F`.  The proof has three steps.

### 2.1 Adjugate annihilation

In `C`, `A delta=0`.  Multiplying by `adj(A)` gives

```text
e(x-u)=0,    e(y-v)=0.                              (2.1)
```

The replay checks the stronger polynomial identities

```text
e(x-u) = a22*f1-a12*f2,
e(y-v) = -a21*f1+a11*f2.
```

### 2.2 Diagonal normalization and idempotence

Because `det J_F=1`, restriction to the diagonal gives `e=1`.  Therefore

```text
e-1 = c_x(x-u)+c_y(y-v)                            (2.2)
```

for explicit polynomial divided differences `c_x,c_y`.  Multiply (2.2) by
`e` and use (2.1):

```text
e^2-e = (c_x a22-c_y a21) f1
      + (-c_x a12+c_y a11) f2.                    (2.3)
```

Thus `e` is an idempotent in `C`.  Moreover `e J_delta=0` and
`1-e in J_delta`.  It is the unique element with these properties: if `e'`
has them too, then `e=e e'=e'`.

For a nonzero constant Jacobian `c`, the same proof uses
`e=c^(-1) det A`.  The normalized determinant-one form loses no generality.

### 2.3 Exact saturation identity

In `C`, `(e) subset (0:J_delta)`.  Conversely, if
`h J_delta^m=0`, then `1-e in J_delta` and idempotence gives
`(1-e)^m=1-e`; hence `h(1-e)=0` and `h=he in (e)`.  Therefore

```text
0 : J_delta^infinity = (e) in C,
I : (x-u,y-v)^infinity = I+(e) in S.               (2.4)
```

Since `c` is a scalar unit, `(e)=(det A)`.  The product decomposition is

```text
C ~= eC x (1-e)C,
eC ~= B                 (diagonal),
(1-e)C ~= C/(e)         (off-diagonal component).
```

This is scheme-theoretic: it removes embedded diagonal structure as well as
diagonal points.  Different telescoping conventions give the same class of
`e` in `C` by uniqueness, so this does not repeat the raw-boundary covariance
failure.

## 3. Executed discriminator

Artifacts:

```text
cases/fresh_connection_20260824/secant_idempotent.py
cases/fresh_connection_20260824/independent_replay.sing
```

Primary exact replay:

```text
uv run --no-project --with sympy==1.14.0 \
  python3 cases/fresh_connection_20260824/secant_idempotent.py
```

Result: `44/44` Boolean checks passed.  The script constructs all cofactors
in (2.1)--(2.3) before using a Gröbner basis, then independently reduces the
idempotence equation and the off ideal.

| Control | Characteristic | `det A` / off ideal | Result |
|---|---:|---|---|
| identity | 0 | `det A=1` | off ideal `(1)` |
| `(x,y+x^4)` | 0 | `det A=1` | off ideal `(1)` |
| `(x+(y+x^2)^2,y+x^2)` | 0 | nonconstant nine-term `det A` | off Gröbner basis `[1]` |
| `(x-x^3,y)` | 3 | `1-x^2-xu-u^2` | off basis `[u^2+ux+x^2-1, y-v]`; marked `(0,0),(1,0)` lies on it |
| `(x^2,y)` | 0 | `x+u` | rejected: `J=2x`, idempotence remainder nonzero |

The nontrivial tame control's determinant is

```text
-u^3-u^2*x-u*v+u*x^2+u*y-v*x+x^3+x*y+1.
```

Its off ideal is nevertheless the unit ideal, so the test is not merely
detecting maps whose chosen secant determinant happens to be the literal
constant one.  The Artin--Schreier control shows the opposite behavior in a
setting with a genuine Keller collision.

Independent exact replay:

```text
Singular -q cases/fresh_connection_20260824/independent_replay.sing
```

It returned four `PASS` lines: characteristic-zero idempotent/off-unit,
characteristic-three surviving marked off component, and rejection of the
non-Keller square control.

Deterministic stdout SHA-256 values are
`1e0d473785ebe403db50248642c26e29831328fb8865fe2a2e91ce862326d4a3`
for the JSON replay and
`06678206d168206341293bca00788c22dfa1cff729327d851b16d261ba4572c6`
for the Singular replay (hashes exclude the shell's locale warnings).

Artifact SHA-256 values:

| Artifact | SHA-256 |
|---|---|
| `cases/fresh_connection_20260824/secant_idempotent.py` | `c55f9f1173aef8a16ecc13c2162ee2fd89bb6916cfaa95f4e9d57b7030105eef` |
| `cases/fresh_connection_20260824/independent_replay.sing` | `bd5469b4a28f4a84c8f6635f6c95b3dcc6295d94a195d6ad2e36f903edefc891` |

Input SHA-256 values at the read cutoff:

| Input | SHA-256 |
|---|---|
| `APPROACHES.md` | `de3ea6344af96e7371391377aa07b720fb4b4ffbcbccff35260cc128b5861f88` |
| `AUDIT.md` | `561b965b9ea9d93b6831d9881941eb30ce181e83caa5c3179886cfef3ff28cb1` |
| `PROGRESS.md` | `093090c547d5a0d9bcc5ac8d52f48731127468c94f73dd0559d10fa3ac813854` |
| `notes.md` | `80e47682ac95e3e2193e6bcb821a64ed8e52f7364a2f25e24e8e9fb699cb1290` |
| `xmodel/ideation-20260824T0719Z-synthesis.md` | `c2de1aec94ac42c07028bfe759ac8fb4f5100f204abaedc1dc032aa098931c60` |

## 4. Scope, failure mode, and next exact client

### What is established

- The secant determinant is a canonical diagonal idempotent modulo the
  collision equations for any determinant-one polynomial map.
- The off-diagonal saturation equals a three-generator ideal exactly.
- The statement is global and source-polynomial; it consumes no local
  compactification, formal germ, finite support, or unreviewed claim.
- A deterministic exact implementation and a second algebra engine agree on
  all registered controls.

### What is not established

- There is no proof that the off ideal is `(1)` for every complex Keller map.
  That assertion is the injectivity endpoint.
- No degree, support, height, or Gröbner bound follows merely from replacing
  saturation by `det A`.
- No GGV packet is transported into a Sigray book, no sheet-six class is
  realized or killed, and no characteristic-109 lift is constructed.
- The characteristic-three survivor is only the already-known
  Artin--Schreier control; it is not a characteristic-zero counterexample.
- No literature novelty or public claim is made.

### Cleanest next use

Package (2.1)--(2.4) as a small source-independent collision module.  A later
source-derived polynomial family can then emit `f1,f2,det A` directly, avoid
ideal saturation, and use the same four controls as mandatory gates.  The
first worthwhile client is a **named, bounded polynomial-origin family** for
which the old saturation was the actual bottleneck.  It is not a license for
generic sparse widening or AWS search.

### Resurrection / promotion conditions

Promote the theorem only after hostile algebra review of the saturation
equality and a priority check against the recorded collision-ideal/Bezoutian
literature.  Promote a client result only if it supplies one of:

1. an independently checked unit certificate for the off ideal on an honest
   exhaustive polynomial-origin family;
2. a nonunit characteristic-zero off ideal plus an explicit point, direct
   `J=1`, and a verified nontrivial collision (an actual counterexample); or
3. a structural degree/support theorem for `det A` that makes an exhaustive
   global family finite without importing a book-landing or td ceiling.

Absent one of these, `SECANT-IDEMPOTENT` remains an exact software/theory
accelerator and avenue-32 refinement, not a proof/disproof avenue promotion.

No statement in this report proves or disproves JC2.
