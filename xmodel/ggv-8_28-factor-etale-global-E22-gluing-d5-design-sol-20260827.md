# HOLD design: smallest factor-etale to global polynomial `E22` interface

Date: 2026-08-27  
Lane: `a1_total_lift_design` / Sol2

## Design outcome

The smallest honest gluing interface should make the **direct raw
determinant coefficient** authoritative and use D4R1 only to check a
commutative square.  This avoids the central failure mode: root/factor data
determine `E22 mod H`, not the global `H`-multiple.

This design is on HOLD.  It does not consume D4R1 before fresh review and
contains no descendant result.

## 1. Global path first

Let `C` be the exact polynomial ring on the 400 positive-weight raw slots,
with `F0=H^2`, `G0=H^3`, and set `S=C[X]`.  Compile directly

```text
D_n=sum_(i+j=n) ((12-j)F_i'G_j+(i-8)F_iG_j') in S.
```

In particular, `D22` is a literal global polynomial expression with every
raw-row provenance edge visible.  No local coordinate, factor pattern, or
alias participates in its definition.

Divide by the monic `H=X^8-1`:

```text
D22=H Q22+R22,  deg R22<8.
```

This pair is the minimal custody object:

- `R22` is exactly what all factor/root values can recover by CRT;
- `Q22` is the otherwise invisible global `H`-multiple;
- together they reconstruct the authoritative `D22`.

The confirmed `M` reducer can then act on this literal `D22` and emit seven
expressions in the raw coefficient ring.  It must not act on a degree-`<8`
interpolant substituted for `D22`.

For the normalized Keller target, the exact global condition is

```text
R22=1, Q22=0,
```

not merely `R22=1`.

## 2. Local path as a naturality check

After—not before—a D4R1 review PASS, its factor-local output supplies in
`A=C[c]/(c^8-1)`:

```text
xi=c+s(t), q0=u_X(xi,t), U(t), V(t).
```

For the Morse expansion, the constant channel is

```text
C_n=sum_(i+j=n)V_i(j-8)U_j.
```

Exact coordinate naturality gives the full truncated identity

```text
sum_n t^n D_n(xi(t)) = q0(t) sum_n t^n C_n mod t^23.   (* )
```

The future compiler should replay `(*)` generically node-for-node.  This
does two useful jobs at once: it checks the cleanup DAG against the literal
raw determinant, and it preserves the determinant/orientation unit instead
of silently setting it to `H'(c)` at all weights.

The lower-row gate must be explicit.  Substitution `X=xi(t)` normally mixes
Taylor derivatives of `D_0,...,D_21` into the weight-22 coefficient.  Only
after an exact raw identity or frozen quotient proves

```text
D0=...=D21=0
```

does `(*)` reduce at weight 22 to

```text
D22(c)=H'(c) C22.
```

That equality identifies `R22`; it still says nothing about `Q22`.

## 3. Exact maps and tag custody

The interface uses only these maps:

```text
C[raw rows] -> C[X,t]/(t^23)              raw chart
C[X] -> C[c]/(c^8-1)                      reduction mod H
C[c]/(c^8-1) -> product_p C[c]/(p)        tagged CRT projections
C[X] -> C[X]_{<8} x C[X]                  P |-> (R_H(P),Q_H(P))
```

The four factor IDs remain `X-1`, `X+1`, `X^2+1`, `X^4+1`.  Each local
packet retains its factor, chart, deck, orientation, and determinant tags.
CRT gluing yields one element of `C[c]/H`; it is not a lift to `C[X]` beyond
the canonical degree-`<8` representative.

## 4. Cheapest decisive controls

The most important mutation is

```text
D22 -> D22+H.
```

Every factor value and `R22` remain unchanged, while `Q22` increases by one
and the `M` seven-vector changes.  Any interface that misses this mutation
has silently dropped the exact object the campaign needs.

Other required controls are:

- keep a nonzero `D21` and critical shift, and ensure the simplified
  endpoint comparison refuses to run;
- mutate a determinant-recurrence sign and require direct/local naturality
  failure;
- delete or permute a factor/deck/orientation tag and require CRT failure;
- mutate a raw row and require the direct coefficient digest to change; and
- attempt a 16-branch-pattern interpolation and reject it as lacking a
  raw-ring map.

## 5. Implementation size

The direct `D_n` compiler is only quadratic in the raw rows that occur in
pairs `i+j=n`; no Groebner basis or AWS job is needed.  It should serialize
sparse monomials as

```text
(raw_slot_1, raw_slot_2, X_degree) -> rational coefficient
```

with linear terms represented by the fixed leading rows.  Monic division by
`H`, CRT projection, and `M` reduction are exact linear passes.  The only
potentially larger step is the D4R1 node evaluation for the naturality
square, already desk-scale in the producer.

## Scope

A future reviewed PASS would establish a raw/local commutative interface and
exact `H`-multiple custody.  It would not solve the raw Keller system,
establish `Q22=0`, exclude a face/family, prove source/landing coverage,
`G2-PSC`, `G2-BD`, or JC2.
