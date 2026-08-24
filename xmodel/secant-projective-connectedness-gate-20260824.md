# Secant projective-connectedness gate

- Status: **FROZEN — PARENT PROVISIONAL / COSTUME /
  NEED-Z-SATURATED-INFINITY-DATUM**
- Date: `2026-08-24`
- Producer: OpenAI Codex, bounded speculative child
- Launch basis: `51aa1cc210b20d6c57c5bb0ba3b4a6dfa5fc8f54`
- Parent dependency:
  `xmodel/fresh-connection-gate-20260824.md`, frozen SHA-256
  `666bde51ea8bb78bd2c031122183148708b2b7de08547dc407191e633a712c4b`
- Parent tier: **PROVISIONAL**; its different-model review was already running
  when this child launched.  Nothing below promotes or widens the parent.
- Scope: one projective-connectedness discriminator only.  No generic sparse
  search, AWS, book/D/Witt work, canonical edit, or public communication.

## Verdict

Projective complete-intersection connectedness gives no new obstruction at
this gate.  It returns the precise stop

```text
PROJECTIVE-CONNECTEDNESS = COSTUME / KNOWN-NONPROPERNESS.
```

There are two distinct reasons, both exact.

1. The naive two-equation homogenization can retain whole components supported
   at infinity.  These components make the projective complete intersection
   connected even for a polynomial automorphism.  Passing to the honest
   projective closure requires saturation by the homogenizing variable `Z`;
   that saturation removes the artificial components but also destroys the
   two-equation complete-intersection presentation on which the connectedness
   argument relied.
2. When an honest off-diagonal component does exist, its closure may meet the
   diagonal closure only at infinity without conflicting with the affine
   secant idempotent.  The characteristic-three Artin--Schreier Keller
   collision realizes this mechanism exactly: the two saturated components
   meet along a doubled line `Z^2=0` at infinity.

Thus connectedness says only that missing sheets have to attach somewhere in
a proper closure.  For an affine etale nonproper map, “somewhere” is the
boundary; that is the known nonproperness/asymptotic-set problem in projective
language.  No characteristic-zero Newton/degree family is killed, and no
proof or counterexample is obtained.

## 1. Typed projective setup

Assume the provisional parent statement for this child.  For a determinant-one
map `F=(P,Q)` over a field, put

```text
I = (P(x,y)-P(u,v), Q(x,y)-Q(u,v))
    in k[x,y,u,v].
```

The parent supplies an affine idempotent `e` modulo `I`, with the diagonal
factor `e=1`, the off factor `e=0`, and provisionally

```text
I : (x-u,y-v)^infinity = I+(e).                    (1.1)
```

Now homogenize the two difference equations, each at its honest polynomial
degree, in

```text
k[X,Y,U,V,Z].
```

Call their homogeneous ideal `K`.  Its affine chart `Z=1` recovers `I`, but
the closure of the affine scheme is not in general `Proj(k[...]/K)`.  It is

```text
Proj(k[X,Y,U,V,Z] / (K:Z^infinity)).                (1.2)
```

If the two homogenized equations retain height two, `K` is a projective
complete intersection of dimension two and is connected.  If height drops at
infinity, even that hypothesis fails.  In either case, the connectedness
theorem applies to `K`, while the honest closure uses `K:Z^infinity`.

The affine idempotent does not extend as a degree-zero regular idempotent on a
connected projective closure.  Its homogenization is a section of a positive
twist and can vanish or acquire poles at `Z=0`.  Consequently affine clopen
components may have projective closures that intersect on the boundary.  An
honest graph or resolved compactification avoids naive `Z`-torsion, but then
one must compute its boundary intersection data directly; it does not retain
the free complete-intersection argument.

## 2. Identity and nontrivial tame automorphism controls

### 2.1 Identity

For `F=(x,y)`, the homogeneous difference ideal is already

```text
K_id = (X-U, Y-V).
```

It is `Z`-saturated with saturation exponent zero.  Its projective scheme is
only the diagonal plane.  This is the no-degree-loss control.

### 2.2 Two-step tame map

Use the exact automorphism control already present in the campaign:

```text
Q = y+x^2,
P = x+Q^2 = x+(y+x^2)^2.
```

Let

```text
q_1 = X^2+YZ,
q_2 = U^2+VZ,
H_Q = q_1-q_2,
H_P = XZ^3+q_1^2-UZ^3-q_2^2.
```

Two exact homogeneous identities recover the diagonal only after dividing by
powers of `Z`:

```text
H_P-(q_1+q_2)H_Q = Z^3(X-U),
H_Q-(X+U)(X-U)   = Z(Y-V).                          (2.1)
```

On `Z=1`, these identities give `X=U` and `Y=V`, as they must for an
automorphism.  At infinity, however,

```text
H_Q|_(Z=0) = (X-U)(X+U),
H_P|_(Z=0) = (X^2+U^2) H_Q|_(Z=0).                 (2.2)
```

The naive homogeneous complete intersection therefore contains both whole
surfaces

```text
Z=X-U=0,        Z=X+U=0.                           (2.3)
```

They are absent from the affine map and supply projective connectivity at no
mathematical cost.

Independent exact saturation gives

```text
(H_P,H_Q):Z^infinity = (X-U,Y-V),
saturation exponent = 4.                           (2.4)
```

The parent's nonconstant nine-term secant determinant homogenizes to

```text
E = -U^3-U^2X-UVZ+UX^2+UYZ-VXZ+X^3+XYZ+Z^3.
```

For the putative projective off ideal,

```text
(H_P,H_Q,E):Z^infinity = (1),
saturation exponent = 3.                           (2.5)
```

So the honest off closure is empty, while its naive homogenization has only
infinity-supported residue.  This is a direct automorphism falsifier for the
idea that a projective component forced by the homogeneous equations is an
off-diagonal sheet.

## 3. Artin--Schreier mechanism control

Over `F_3`, take the exact Keller collision

```text
F=(x-x^3,y),        det J_F=1.
```

Its homogenized equations factor as

```text
E   = Z^2-X^2-XU-U^2,
H_P = (X-U)E,
H_Q = Y-V.                                            (3.1)
```

The homogeneous pair is already `Z`-saturated, with exponent zero, and has
the exact decomposition

```text
(H_P,H_Q)
  = (X-U,Y-V) intersect (E,Y-V)
  = D intersect O.                                    (3.2)
```

Here `D` is the diagonal closure and `O` is the honest off closure selected
by the secant determinant.  They meet in the scheme

```text
D+O = (X-U,Y-V,Z^2)       over F_3.                  (3.3)
```

Thus their intersection is supported on the diagonal line at infinity and
has a doubled `Z` structure.  The marked affine points
`(x,y)=(0,0)` and `(u,v)=(1,0)` lie on `O`, so this is not an artificial
infinity component.  It is the exact projective attachment of a genuine
Keller collision.

The same polynomial in characteristic zero is the useful rejection control.
Its Jacobian is `1-3x^2`, and on the diagonal

```text
E|_D = Z^2-3X^2.                                     (3.4)
```

The diagonal and off components then meet on an affine critical locus as well
as at infinity.  Reducing to characteristic three makes the derivative a
unit and moves the whole meeting scheme to `Z^2=0` at infinity.  This shows
exactly what constant Jacobian contributes here: it excludes affine
diagonal/off contact.  It does not prohibit contact at the boundary or force
an incompatible intersection multiplicity.

## 4. Replay and hashes

Artifacts:

```text
cases/secant_projective_20260824/projective_gate.py
cases/secant_projective_20260824/independent_replay.sing
```

Primary replay:

```text
uv run --no-project --with sympy==1.14.0 \
  python3 cases/secant_projective_20260824/projective_gate.py
```

Result: `18/18` exact Boolean checks passed.  Deterministic stdout SHA-256:
`b8fe2974cca7805212f84c7b35f77879752ba7e2e1b7932826aff4de002c563e`.

Independent saturation/decomposition replay:

```text
Singular -q cases/secant_projective_20260824/independent_replay.sing
```

It returned five `PASS` lines, covering identity saturation, tame pair and
off-ideal saturation, the Artin--Schreier saturated decomposition/meeting
scheme, and the characteristic-zero non-Keller rejection.  Deterministic
stdout SHA-256:
`8878dfd1d12f43dadf1ca3c0e14d933b055a83de2e681ec78bd24d4e4d5b81bb`.

Artifact hashes:

| Artifact | SHA-256 |
|---|---|
| `cases/secant_projective_20260824/projective_gate.py` | `76f4ae48a2f7382a3b3fd0a11e9c99961f30b2e356dbd5617692fd08cfc82494` |
| `cases/secant_projective_20260824/independent_replay.sing` | `ca5cd4ce255c84d9f046e70dbc1eefba4dbad70f43ad4c01e2f6513077bedefd` |

## 5. Failure mode and resurrection condition

### Exact stop

- Naive connectedness can be carried entirely by `Z`-torsion/pure-infinity
  components, including on a nontrivial automorphism.
- Honest `Z`-saturation can add generators, remove components, and discard the
  complete-intersection presentation.
- If an honest off component survives, affine etaleness merely forces its
  intersection with the diagonal closure onto the boundary.  That behavior
  is compatible with a genuine Keller collision.
- The secant determinant identifies the off component but supplies no sign,
  positivity, or characteristic-zero prohibition for its boundary
  intersection cycle.

Therefore neither projective connectedness nor the explicit affine
idempotent yields a new obstruction for an arbitrary Keller map or any named
characteristic-zero Newton family at this gate.

### Missing infinity datum

A live descendant would need a source-polynomial theorem about the **honest
`Z`-saturated boundary intersection**, not the naive homogeneous complete
intersection.  Sufficient resurrection triggers include one of:

1. a named polynomial-origin family whose saturated leading ideal and
   diagonal/off intersection cycle can be computed exhaustively;
2. a characteristic-zero theorem that the saturated closure remains pure
   Cohen--Macaulay/complete-intersection with a specified diagonal normal
   bundle, plus an intersection number incompatible with boundary-only
   meeting;
3. a resolved graph compactification with all exceptional components,
   multiplicities, and target images pinned, and a positive intersection or
   conductor formula that the Artin--Schreier mechanism fails.

The third item is essentially the missing asymptotic-set/global-boundary
datum in avenue 7/31 language.  A bare leading-form factorization, another
homogenization, or a connectedness citation does not satisfy it.

No result here proves or disproves JC2, promotes the provisional parent, or
changes the live td6/AS109 allocation.
