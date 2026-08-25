# AS fixed-support residue-ball collision and compactness theorem

Status: **PRODUCER-EXACT MATHEMATICAL LEMMA; DIFFERENT-MODEL REVIEW PENDING**

Date: 2026-08-25

## 1. Result

For the Artin--Schreier special fibre

```text
F_0(x,y)=(x-x^3,y)  over F_3,
```

collision variables add no new existence condition to a **complete**
determinant-one lift at a fixed finite precision.  More precisely, let
`R_n=Z/3^n Z`, and let `F=(P,Q)` be a polynomial map over `R_n` satisfying

```text
det J(F)=1 in R_n[x,y],             F mod 3 = F_0.
```

Then the restrictions of `F` to each of the three source residue balls above
`(0,0)`, `(1,0)`, and `(2,0)` are bijections onto the target residue ball
above `(0,0)`.  Hence there are unique points in all three balls over any
chosen target in that ball.  Choosing the first two gives

```text
(a,b) = (0,0) mod 3,     (c,d) = (1,0) mod 3
```

with the same prescribed target in that ball.  These are moving Hensel
preimages; they need not be the fixed marked representatives `(0,0)` and
`(1,0)` over `R_n`.  They are distinct and
`a-c` is a unit, so a unique `u in R_n` satisfies

```text
P(a,b)=P(c,d),   Q(a,b)=Q(c,d),   u(a-c)=1.
```

Consequently, if the same fixed finite map support admits a complete
determinant-one AS lift modulo `3^n` for every `n`, then there is a
determinant-one polynomial map over `Z_3` with an off-diagonal collision.
The associated finite integral collision scheme has a `Q_3` point, hence a
`Qbar` point and therefore a complex Jacobian-conjecture counterexample.

This theorem does **not** say that such fixed-support maps exist at all
depths.  It says that collision preservation is automatic if they do.

## 2. Finite-ring induction

Let `r` be any of `(0,0)`, `(1,0)`, or `(2,0)`, and let `z in R_n^2` reduce to
`(0,0)`.  The special-fibre identity gives

```text
F(r)=z mod 3.
```

Suppose `x_k`, reducing to `r`, has been constructed modulo `3^k` with
`F(x_k)=z mod 3^k`, where `1 <= k < n`.  Every lift has the form

```text
x_{k+1}=x_k+3^k h,       h in F_3^2.
```

Polynomial Taylor expansion gives

```text
F(x_k+3^k h)
  = F(x_k)+3^k JF(x_k)h             mod 3^(k+1).
```

All terms of order at least two are divisible by `3^(2k)`, and
`2k >= k+1`.  Reduction of `JF(x_k)` modulo three is invertible because its
determinant is one.  Therefore the two-by-two linear equation for `h` has
exactly one solution over `F_3`.  Induction gives one and only one preimage
of `z` in each prescribed source residue ball.

The three preimages lie in different residue balls, so every pairwise
x-coordinate difference is a unit.  This proves both the moving collisions
and the displayed unit-localizer equation.  The same proof works for any
prime and any two distinct source residues having the same image under a
special-fibre map with invertible Jacobian.

## 3. Fixed-support compactness and transfer to characteristic zero

Fix finite monomial supports `S_P,S_Q`.  Encode the AS residue component by
integral variables, for example

```text
P = x-x^3 + 3 A,       Q = y + 3 B,
```

with `A,B` supported in the fixed sets.  Let `X_n` be the set of coefficient
vectors in `Z_3^N` for which every coefficient of

```text
P_x Q_y-P_y Q_x-1
```

vanishes modulo `3^n`.  A solution over `Z/3^n Z` has arbitrary lifts of its
coordinates to `Z_3`, so nonemptiness of the complete fixed-support scheme
modulo `3^n` makes `X_n` nonempty.  Each `X_n` is closed in compact
`Z_3^N`, and

```text
X_1 superset X_2 superset X_3 superset ... .
```

Thus nonemptiness for every `n` implies a point in their intersection.  This
is equivalently the finite-branching König argument: arbitrarily deep nodes
in the reduction tree force an infinite compatible branch.  Its
fixed-support polynomials over `Z_3` have determinant exactly one and reduce
to `F_0`.  The same digit induction, now through all levels, supplies two
`Z_3` source points in the residue balls above `(0,0)` and `(1,0)` with a
common target and unit x-separation.

Equivalently, consider the finite integral collision scheme with:

1. all fixed map-coefficient variables;
2. every coefficient equation of `det J(F)-1`;
3. source variables `(a,b),(c,d)`;
4. the two equations `P(a,b)-P(c,d)=0` and
   `Q(a,b)-Q(c,d)=0`;
5. the equation `u(a-c)-1=0`.

The `Z_3` map and its Hensel collision define a point of this scheme over
`Q_3`.  Evaluation therefore shows that its defining ideal in a polynomial
ring over `Q` is proper.  Faithful flatness under `Q -> Qbar` preserves
properness, and the weak Nullstellensatz supplies a `Qbar` point.  The unit
equation preserves off-diagonality.  Embedding `Qbar` in `C` produces a
complex polynomial map with constant Jacobian one and a genuine collision,
which is a JC2 counterexample.

Compatibility of separately found finite-level points is not an additional
hypothesis: nested compactness constructs a compatible coefficient point.

## 4. Exact mod-9 and mod-27 controls

The portable replay uses the already frozen cap-seven triangular map

```text
P=x+2x^3+441x^5+108x^7,
Q=y-6x^2y+18x^4y-27x^6y.
```

Its literal integer determinant is

```text
1 + 2187x^4 - 12393x^6 + 34992x^8
  - 45927x^10 - 20412x^12,
```

so it is one modulo both `9` and `27`.  At each modulus the two points

```text
(a,b)=(0,0),       (c,d)=(7,0)
```

both map to `(0,0)`.  Since `a-c=-7`, the unit equation holds with

```text
u=5 mod 9,          u=23 mod 27.
```

The replay also constructs these points by the exact digit induction and
checks uniqueness at each step.  The negative control `(x-x^3,3y)` misses
the target `(0,3)` from the source ball above `(0,0)` modulo nine, showing
that invertibility of the Jacobian is load-bearing.

The controls are finite-depth regressions, not evidence for all-depth
fixed-support survival.

## 5. Firewalls and exact campaign consequence

The compactness/transfer conclusion requires all of the following:

- the same finite supports and coefficient variables at every depth;
- every determinant coefficient equation at every depth;
- honest solutions of those integer equations, or a proved and replayed
  reconstruction from any digit/carry encoding;
- one fixed AS residue component;
- no depth-dependent constants, changing normalizations, or unencoded
  denominators/localizers.

It does not consume:

- filtered high-row survival;
- a chronological state that still owes lower source rows;
- a changing or growing support;
- simultaneous gauge variables that do not reconstruct the map;
- a solver model without direct integer substitution;
- finite survival at only finitely many depths.

Therefore the present aligned `D=7` carry campaign may use this lemma only
after a state reconstructs a complete determinant-one map at its stated
precision.  The lemma removes a separate collision-search burden; it does
not remove any remaining map-completion or all-depth burden.

## 6. Artifacts

Portable case:

```text
cases/as_fonly_residue_ball_collision_20260825/
```

AWS replay command:

```sh
cd cases/as_fonly_residue_ball_collision_20260825
/usr/bin/time -v python3 replay_controls.py \
  > replay.stdout 2> replay.stderr
```

Result hashes and custody are frozen only after the AWS execution.
