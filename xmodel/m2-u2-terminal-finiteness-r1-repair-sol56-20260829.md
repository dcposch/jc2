# U2 fixed-terminal finiteness — quantifier-safe R1 repair

Date: 2026-08-29 UTC. Producer: Sol 5.6 coordinator lane. Lifecycle:
`PROVISIONAL_REPAIR / DIFFERENT_MODEL_REVIEW_REQUIRED`.

## 0. Purpose and perimeter

Grok's U2 primary report
`xmodel/m2-u2-nu1-unbounded-lex-primary-grok46-20260829.md`
correctly isolates a hard quantifier: the merge child has infinitely many
reduced weights

```text
W_L = w * (L+r-1)/L,       M_L = gcd(r*mu,r+L),       L >= 1,
```

even at one fixed entry, while the downstream P0/P1 ledger is claimed finite.
Its §4 gives the right one-step intuition but does not prove uniformity over
arbitrarily interleaved clean resonances, dirty steps, and free-index neutral
families. This note supplies that missing proof.

The result is conditional on exactly two inputs, neither re-proved here:

1. Grok's absorbed-U2 shape and transport display above, with fixed positive
   rational `w` and fixed integers `r>=2`, `mu>=1` at a named entry.
2. The reviewed P0/P1 grammar and modeled lambda prices in
   `ladder/BOOK-OFFAXIS.md` §10 and the finite-chain reviews. In particular,
   `l | M_parent`; zero-modeled-cost steps are exactly neutral or clean
   resonant; every pure-epsilon or dirty step costs at least one; and P1 is
   `0<W_t<1`, `M_t>=2`, `j=M_t(1-W_t) in N*`.

This note does not validate the U2 ODE, its low-td controls, Statement 3.9
gluing, landing, realization, a degree ceiling, or JC2. No canonical file is
edited and no AWS action is licensed.

## 1. Exact P0 transformations, read backwards

Write a parent chain weight as `W>0` and the child as `W'`.

### 1.1 Clean layer

A neutral step fixes `W` and sends `M` to a divisor. It can be contracted in
the reduced path, retaining only one of finitely many divisor/residue records.

A clean resonance has `n>=2`, `nu>=2`,

```text
Delta = (n-1)*nu+1,       W' = W*n/Delta.
```

Thus, backwards,

```text
W = W' * (nu - (nu-1)/n).                         (R)
```

The factor is positive, is strictly below `nu`, and tends to `nu` from below
as the sole unbounded parameter `n` tends to infinity. Forward, it is at most
`2/3` because `n/((n-1)nu+1) <= n/(2n-1) <= 2/3`.

### 1.2 Positive-cost layer

A pure-epsilon step has one of finitely many pairs
`l>=2`, `1<=eps<l` and

```text
W' = l*W/(l-eps),       so       W = W'*(l-eps)/l.       (E)
```

Its free local `nu` changes only a finite `M` residue/divisor record at the
reduced P0/P1 tier.

For a dirty step, let `k` be the number of northeast p-orbits,
`Sm=sum m_j`, `s=1+k+lex`, and

```text
C = l*(k+lex)-Sm = l*s-(l+Sm) >= 1,
E = (l-eps)+nu*C.
```

P0 transport is `W'=l*W*s/E`. Therefore the exact backward law is

```text
W = W' * (nu - K/(l*s)),
K = nu*(l+Sm)-l+eps > 0.                            (D)
```

For fixed discrete data, the only unbounded weight parameter is `s`; the
factor is strictly below `nu` and tends to `nu` from below. Formula (D), not
an informal claim that a linear polynomial divides a bounded integer, is the
uniform mechanism used below.

## 2. Uniform bounds independent of L

Fix the numerical modeled budget `B`. Put

```text
M0 = r*mu,
Mhat = M0*(B+1)^B.
```

### Lemma 2.1 — every reduced multiplicity is bounded by Mhat

Initially `M_L | r*mu`. Neutral, resonant, and pure-epsilon steps send `M` to
a divisor of `l` or `l-eps`, hence do not increase it. At a dirty step,
`dq=1+nu*s` gives `gcd(M',nu)=1`, while

```text
dp-eps*dq = nu*T,
T = l+Sm-eps*s >= 1.
```

Consequently `M' | T`. Since every `m_j<l`, each of the `k` northeast
orbits costs at least one, and `l|M_parent`,

```text
M' <= T <= l+Sm <= l+k(l-1) <= (B+1)*M_parent.
```

There are at most `B` positive-cost steps, proving `M<=Mhat` throughout. In
particular, `l<=Mhat`, and the discrete choices of `l,eps,k,(m_j),Sm` are
finite.

### Lemma 2.2 — all intermediate weights lie in a fixed compact interval

The U2 input satisfies `W_L<=r*w`. Resonance contracts and neutral steps fix
weight. Pure-epsilon expands by at most `l<=Mhat`.

For a dirty step, `k+lex>=1` and `Sm<=k(l-1)` imply

```text
C >= k+l*lex,       2*C >= 1+k+lex = s.
```

Hence `E>=2C>=s` and its forward multiplier obeys
`l*s/E<=l<=Mhat`. With at most `B` positive-cost steps,

```text
W <= What := r*w*Mhat^B.                            (U)
```

At P1, positivity and `j=M_t(1-W_t) in N*` give

```text
W_t in {1-j/M : 2<=M<=Mhat, 1<=j<M}.
```

This is a finite target set and every target is at least
`tau_min=1/Mhat`. From any intermediate vertex, the remaining positive-cost
steps can expand by at most `Mhat^B`; resonances cannot expand. Therefore

```text
W >= Wmin := tau_min/Mhat^B                         (L)
```

along every terminal-reaching path.

### Lemma 2.3 — path depth and every weight-changing local nu are bounded

If there are `R` clean resonances, (U) and the `2/3` contraction give

```text
tau_min <= r*w*Mhat^B*(2/3)^R.
```

Thus `R` has an explicit bound depending only on the entry and `B`. Together
with at most `B` positive-cost steps, every reduced nonneutral path has
uniformly bounded length. Repeated neutral steps contract to finite
divisor/residue records.

For (R), `W/W'>=nu/2`. For (D), `2C>=s` gives
`W/W'=E/(l*s)>=nu/(2l)>=nu/(2Mhat)`. Combining these inequalities with
`W<=What` and `W'>=Wmin` bounds every weight-changing `nu` by

```text
nu <= 2*Mhat*What/Wmin.
```

Therefore a path type has only finitely many discrete labels. Its only
unbounded variables are the resonance values `n_i` and dirty values `s_i`.

## 3. The opposite-side product lemma

### Lemma 3.1

Fix positive rationals `q,u,c`; a nonnegative integer `h`; positive rationals
`v_i,a_i`; and lower bounds on positive integer variables `x_i`. Then

```text
u*(1+c/L) = q * product_i (v_i-a_i/x_i)              (*)
```

with every factor positive has only finitely many integer solutions
`(L,x_1,...,x_h)`.

*Proof.* Induct on the number of variables `L,x_1,...,x_h`. The right side is
strictly below its limit `R=q*product v_i`; the left side is strictly above
its limit `u`.

If `R<=u`, there are no solutions. If `R>u`, rearrange (*) as

```text
R-u = u*c/L + [R-q*product_i(v_i-a_i/x_i)].          (**)
```

Every term on the right is positive and the whole right side tends uniformly
to zero when all variables tend to infinity. Hence at least one variable is
bounded by a constant depending only on the fixed data. Split over its
finitely many values. If it is an `x_i`, absorb its positive factor into `q`
and apply induction. If it is `L`, fix it and use the identical argument for
the remaining product variables. At the base, equality with the limiting
value is impossible because every remaining correction has the strict sign
shown in (**). Thus every branch is finite. QED

The strict signs are load-bearing: U2 approaches `w` from above, while every
unbounded backward P0 predecessor factor approaches its integer multiple
from below.

## 4. The repaired theorem

> **Theorem (U2 fixed-terminal finiteness, conditional P0/P1 scope).** Fix an
> absorbed U2 entry `(r,mu,w)`, a numerical modeled lambda budget `B`, and the
> reviewed P0/P1 grammar. Only finitely many integers `L>=1` can occur on a
> P0 path from
> `W_L=w*(L+r-1)/L`, `M_L=gcd(r*mu,r+L)` to a P1-legal terminal.

*Proof.* Lemmas 2.1--2.3 give a finite terminal set, a uniform finite path
depth, and finitely many path types after neutral/free-index quotienting. Fix
one terminal and one type. Multiplying the backward laws (R), (D), and the
finitely chosen constants (E) writes its initial weight exactly as

```text
q * product_i (v_i-a_i/x_i),
```

where each `x_i` is a resonance `n` or dirty `s`, and all fixed factors are
positive rationals. Equating this with `w*(1+(r-1)/L)` is Lemma 3.1. Hence the
full tuple, and therefore `L`, has finitely many solutions for this type.
The finite union over terminals and path types is finite. QED

## 5. What this changes

This repairs only the central quantifier in Grok §4. It does not prove that
Grok's U2 normal form or ODE classification is correct; Fable's active hostile
review remains the authority for those clauses. If those inputs pass, the
finite-terminal conclusion no longer rests on a capped scan or on the
under-explained sentence “`L+1` divides a bounded integer.”

The proof is constructive in principle: `Mhat`, the resonance-depth bound,
the local-`nu` bound, the finite path types, and the induction in Lemma 3.1
give a cap-free enumerator. Building that compiler is a software successor,
not part of this theorem.

No landing, Statement-3.9 transport, source realization, panel exclusion,
cofinal degree bound, counterexample, or JC2 consequence follows.

---

Report-body SHA-256 (all bytes before the separator line above):
`aa6f8685d56c8c7582082717bf802649fa5966282ae76c4666c2c0b6fc9f1bf0`.
