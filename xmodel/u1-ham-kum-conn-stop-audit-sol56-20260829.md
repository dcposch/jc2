# U1 Hamiltonian--Kummer connection: post-blind stop audit

Coordinator: Sol 5.6  
Date: 2026-08-29 UTC  
Frozen campaign basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`  
Lifecycle: `POST_BLIND_HOSTILE_AUDIT / STOP`

## Verdict

`U1-HAM-KUM-CONN/v1` must not launch as a PCB/global-selector lane.  Its
connection formula is correct only after adding a source-family premise that
the reviewed U1 packet does not supply.  Even under that premise, the displayed
connection form is twisted-exact and its character count has no typed map to
distinct positive PCB excess events.

Classification:

```text
conditional differential algebra     CORRECT / KNOWN
instantiation on the reviewed U1 row  SCOPE-CONFLICT
connection-form obstruction class     REFUTED AS STATED
map to PCB excess                      ABSENT
novelty                                DUPLICATE of existing Kummer/character lanes
campaign disposition                   STOP
```

This audit overrides the provisional Avenue-16 raise and launch proposal in
the sealed blind Sol report.  The blind report remains immutable evidence of
the idea; it is not the campaign verdict.

## 1. Conditional calculation

Normalize `J(f,g)=1` and set

```text
D = X_g = g_y partial_x - g_x partial_y,
Df = 1,
Dg = 0.
```

If one additionally has a `D`-stable Kummer algebra

```text
T^r = A(f)
```

on a base where `A` is nonzero, then

```text
DT = (1/r)(A'/A)T,
D(u T^j) = (Du + (j/r)(A'/A)u)T^j.
```

Thus the `j`th eigensummand carries

```text
nabla_j = d + (j/r) dlog(A),
```

up to the harmless sign convention for horizontal sections.  This is a
conditional identity, not a consequence of `Df=1` alone.  Moreover `X_g`
supplies only the `f` direction at fixed `g`; it does not automatically define
a connection on a two-dimensional parameter base.

## 2. Why the reviewed U1 packet does not instantiate it

The reviewed U1 relation is

```text
R(t) = t^r - A_*
```

at a fixed fibre.  Here `t` is a local root/Puiseux variable and
`A_* in C^*` is constant.  The packet does not construct a source-field
element `T`, a varying function `A(f)`, an open parameter stratum, or
`D`-stability.  At the licensed fixed-fibre tier `dA_*=0`, so the proposed
character connections are trivial; over `C`, `t^r-A_*` also splits.

Promoting the formula would therefore convert fixed formal fibre data into a
varying source family.  That is exactly the prohibited formal-data-to-map
scope jump.

## 3. Exactness and controls

Let `omega_j=(j/r)dlog(A)`.  In its own twisted de Rham complex,

```text
omega_j e_j = nabla_j(e_j).
```

Hence the displayed connection form is automatically twisted-exact; it is not
a canonical obstruction class.  It may fail to be rationally gauge-trivial on
the base, but becomes gauge-trivial on the Kummer cover via `T^{-j}`.  Its
residues record finite monodromy, not positive PCB excess.

Two controls show why nontrivial character monodromy cannot be counted as an
obstruction:

- For `A(a)=a` on `G_m`, every nontrivial character for `r=3` or `r=5` has
  `H^0_dR=H^1_dR=0`; on Laurent monomials the coefficient is `n+j/r`, never
  zero for integral `n`.
- For `A(a)=a(a-1)` on `A^1-{0,1}`, nontrivial characters can have
  one-dimensional `H^1`, but the dimension is supplied by punctures.  The
  same auxiliary cover can be attached to the identity Keller map, so this
  cohomology alone detects neither nonproperness nor PCB.

## 4. No typed map to `PCB-EXCESS`

`PCB-EXCESS` concerns actual finite-value direction-cluster quotient lines and
requires distinct positive events contributing to

```text
sum_i (I_i - wt_i(a)) >= s(a)-1.
```

The Hamiltonian direction fixes `g` and moves in the `f` direction.  A
Section-7 quotient curve has the form `phi_i(z)=(P_i(z),Q_i(z))`; the
Hamiltonian direction is tangent only under an extra condition such as
`Q_i'(z)=0`.  No theorem supplies that condition or any map to the excess
sheaves.

In addition, the `r-1` nontrivial characters are Fourier eigenspaces of one
cyclic root orbit.  They are not `r-1` physical pole places, critical-value
flags, quotient lines, or independent upward jumps.  Semisimplicity in
characteristic zero splits these lines and creates no forced coupling or
positivity.  Counting characters as `s-1` units would repeat the campaign's
flag/place/series identification error.

## 5. History and reopen gate

The core algebra already occurs in the promoted face theorem through
connections `d+(m/4)dH/H`, Kummer eigensummands, horizontal solutions, and an
exact twisted-`H^1` index.  `U1-CHAR-TOR`, `ORB-FUSE`, `SIGMA-ZERO`,
`ACS-FOX`, and Avenue 29 already own the character-transport,
augmentation-representation, and Hamiltonian/Gauss--Manin receiver ideas.

Reopen only after all four objects are constructed and typed:

1. an actual U1 occurrence over an open parameter stratum;
2. a `D`-stable source Kummer algebra `T^r=A(f)`;
3. a map to the Section-7 quotient lines or excess sheaves;
4. an injective, no-duplication assignment from pole relations to distinct
   positive weight jumps.

Until then, retain the notation only as a possible future source-transport
client.  Do not raise Avenue 16 and do not launch a standalone lane.

## Nonclaims

This audit says nothing about whether U1 occurs, whether PCB is true, or
whether another D-module invariant can constrain a Keller map.  It only stops
this particular composition at its present type and exactness gates.  No exit
price, occurrence, attainment, map, or counterexample is asserted.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5520`.
- Body SHA-256: `ad2d79d8e220234a315d63dd8e5b9d264084dbc824a3dc804a2588988e7813a9`.
- Frozen basis: `e930fa90b8ee9d86220a2cff72fba94e04b20baa`.
