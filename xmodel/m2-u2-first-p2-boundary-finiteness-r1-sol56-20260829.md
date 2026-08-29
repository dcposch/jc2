# U2 first-P2-boundary finiteness — a merge-inclusive repair

Author: Sol 5.6 coordinator/primary. Date: 2026-08-29 UTC.
Lifecycle: `PRODUCER_CHECKED`; different-model review required.

## 0. Result

The reviewed U2 terminal theorem is not confined to families whose P0 prefix
ends directly at P1.  Its outer-`L` finiteness conclusion extends to families
cut immediately before a first later merge whenever that incoming boundary
has the printed root-multiplicity equality law with integral `kbar`.

**Theorem (`U2-FIRST-P2-BOUNDARY-FINITE`).** Fix

```text
r >= 2,  mu >= 1,  w in Q_{>0},  B in N,
W_L = w(L+r-1)/L,  M_L = gcd(r*mu,r+L),  L >= 1.
```

Suppose a continuation from `(W_L,M_L)` consists of P0 steps (with the
reviewed standing hypothesis `nu>=2`) of total modeled cost at most `B` until
the incoming parent immediately before a first P2 transition is `(W,M)`.
Suppose that this parent carries one root-multiplicity equality orbit with
integers

```text
l | M,        1 <= m < l,        kbar in N*,
kbar = l*W/(l-m).                                      (EQ)
```

Then only finitely many integers `L` can reach that boundary.  The finite set
is effective from `(r,mu,w,B)` and the reviewed P0 grammar; it is uniform in
the equality-orbit string length, the later merge data, and everything after
the first P2 boundary.

Consequently, for fixed absorbed-U2 data, every continuation which either

1. stays in P0 and ends at P1, or
2. first leaves P0 through an integral-`kbar` equality boundary (EQ),

uses only finitely many U2 parameters `L`.  The remaining merge-inclusive
scope includes first boundaries where (EQ) is unavailable — most notably a
nested `nu=1`/rational-`kbar` U2 merge or a source transition not proved to be
of equality-orbit type.  No exhaustive downstream merge grammar is claimed.

## 1. Reviewed inputs

1. Grok's absorbed U2 transport, as independently narrowed by Fable:
   `xmodel/m2-u2-nu1-unbounded-lex-primary-hostile-review-fable5-20260829.md`,
   full SHA-256
   `e156f94ca83026fe04b287100ca79f72325c80a82f8ed3f3f8a94044db440740`.
   In particular `W_L=w(L+r-1)/L`, `M_L | r*mu`, and `r>=2`.
2. The P0-to-P1 product theorem and its backward laws:
   `xmodel/m2-u2-terminal-finiteness-r1-repair-sol56-20260829.md`, full
   `3989703ae243705166843dfe5183bbc83cba44d9284071e49deca19cd935933e`.
3. Opus's different-model review and strengthenings:
   `xmodel/m2-u2-terminal-finiteness-r1-repair-hostile-review-opus5-20260829.md`,
   full
   `9a1775f6c9de92e8204098be3a422222f159d0a4f74baf13a75b1d43598c4a58`.
   It proves the exact P0 four-family partition, `M'|T`, the sharp safe bound
   `Mhat=M0*2^B`, finite path types, and the opposite-side product lemma.  Its
   section 8 derives (EQ) for the charged equality-orbit family and explicitly
   notes that its old P1-target proof does not itself cover that family.

This note uses (EQ) as a literal boundary hypothesis.  Whether every relevant
`nu>=2` first P2 transition in the complete source grammar supplies (EQ) is a
separate coverage question charged to the reviewer; it is not hidden here.

## 2. Finite boundary-weight lemma

Let `M0=r*mu`.  Along every charged P0 prefix of budget at most `B`, Opus's
review gives

```text
M <= Mhat := M0*2^B,
0 < W <= What := r*w*Mhat^B.                           (1)
```

At an (EQ) boundary, `l|M` gives `1<=l<=Mhat`.  Since `1<=m<l`,

```text
W = kbar*(l-m)/l >= 1/Mhat.                            (2)
```

Combining (1) with (EQ),

```text
1 <= kbar = l*W/(l-m) <= Mhat*What.                    (3)
```

Thus every possible boundary weight lies in the explicit finite set

```text
T_EQ = { k*(l-m)/l :
         1<=l<=Mhat, 1<=m<l, 1<=k<=floor(Mhat*What) }.
```

This argument does not bound the equality-orbit string parameter `s` or the
child value `M'=nu*s+1`.  Indeed Opus exhibits infinitely many P1-legal
children for one parent.  It instead proves the only fact needed here: the
*incoming parent weight* belongs to a finite, uniformly positive set.

## 3. Finite-target extension of the product lemma

The reviewed terminal proof used that a P1 target belongs to a finite set of
positive weights.  Nothing in its backward argument requires the target to be
P1 once that property is supplied.

**Lemma (`P0-FINITE-TARGET`).** With fixed `(r,mu,w,B)`, let `T` be any finite
subset of `Q_{>0}`.  Only finitely many `L` admit a P0 path of modeled cost at
most `B` from `(W_L,M_L)` to a state whose weight belongs to `T`.

**Proof.** If `T` is empty there is nothing to prove.  Otherwise put
`tau_min=min(T)>0`.  The reviewed estimates with `tau_min` in place of the P1
lower bound give uniform bounds on `M`, every multiplicity, all intermediate
weights, charged depth, resonant depth, and every weight-changing local `nu`.
Explicitly, every intermediate weight satisfies
`W_i>=tau_min/Mhat^B`; if the target lower bound is incompatible with the
upper estimate `r*w*Mhat^B`, there is no path.  Neutral runs collapse to
divisor records, so only finitely many path types remain.

For a fixed target `tau in T` and fixed path type, backward composition is

```text
w(1+(r-1)/L)
 = q * product_i (v_i-a_i/x_i),                        (4)
```

where `q>0`, every `a_i>0`, and each unbounded integer `x_i` occurs in a
factor approaching its limit `v_i` strictly from below.  Since `r-1>0`, the
left side approaches `w` strictly from above.  The independently reviewed
opposite-side product lemma therefore gives only finitely many integer tuples,
hence finitely many `L`, for (4).  A finite union over `T` and path types is
finite.  QED.

Applying the lemma to `T=T_EQ` proves the theorem.

## 4. Why this closes the charged later-merge objection

Take a continuation with at least one non-P0 transition and stop immediately
before the first one.  Everything before that boundary is a P0 prefix.  If
the first transition supplies (EQ), section 2 makes its incoming parent
weight a
member of `T_EQ`; section 3 permits only finitely many `L`.  Later children,
later merges, and even an infinite family of equality-orbit string lengths
cannot restore an excluded outer `L`, because they occur after this cut.

If there is no later merge, the already reviewed P0-to-P1 theorem applies.
Thus the first-boundary cut converts the apparent failure of the old proof
(`M'` unbounded and factors approaching from above *after* the merge) into an
irrelevant downstream phenomenon for outer-`L` finiteness.

## 5. Exact scope and remaining leak

This note proves no statement when:

- the first non-P0 transition has only rational/unbounded `kbar` and no
  finite-denominator replacement for (EQ), as can happen in `nu=1` U2;
- the absorbed input data `(r,mu,w)` themselves depend on an independent
  inner parameter (`L_inner,L_outer` nesting);
- `l|M`, `1<=m<l`, or the equality identity is not source-licensed;
- the continuation uses a transition outside the charged P0/P2 grammar.

It proves finiteness of the outer U2 parameter, not finiteness of full cells.
Neutral indices, actual arrival vertices, full degrees, exact lambda,
Statement 3.9, gluing, landing, and polynomial-pair realization remain outside
the reduced record.  No panel, degree ceiling, `G2-PSC`, `G2-BD`, or JC2
conclusion follows.

## 6. Best next discriminator

Classify the first nested `nu=1` boundary with two parameters
`(L_inner,L_outer)`.  Derive the exact equal-weight and integrality equations
without caps and decide whether one parameter pins the other into finitely
many divisibility classes.  A finite-denominator analogue of (EQ) closes U2
recursively; an explicit two-parameter family surviving every first-boundary
equation is the honest counterfamily target.

No AWS, web, canonical edit, or heavy computation was used.  This note does
not access or depend on the separately owned formalization repository.

---

Report-body SHA-256 (all bytes before the separator line above):
`220aa9752200fa3d4188290200e6ad0d15965670de972d35fb5f42e5e5d08951`.
