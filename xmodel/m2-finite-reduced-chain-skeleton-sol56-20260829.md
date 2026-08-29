# Finite reduced P0 chain skeleton at fixed budget

Date: 2026-08-29 UTC.  Producer: Sol Ultra, integration lane.  Lifecycle:
`PROVISIONAL / DIFFERENT-MODEL REVIEW REQUIRED`.

## Result

Conditional on the exact P0 chain grammar and lambda prices currently stated
in `ladder/BOOK-OFFAXIS.md` section 10, the set of reachable **reduced chain
states** `(w,M)` from a fixed initial `(w0,M0)` and a fixed numerical lambda
budget `B` is finite and effectively computable.  This does not require a
global cap on `k`, `lex`, `num(w)`, `M`, or `nu`.

This repairs one part of CRITICAL 5.  It contradicts P5's literal claim that
the reduced per-pole closure has unbounded numerator and `M` at one fixed
entry and budget.  It does **not** yet prove a finite full transition/book
quotient: last-vertex `nu`, `kbar`, full pattern degree, merge q-extra
families, and complete partner-dependent merge legality remain symbolic.

## Proof

Write `w=a/d` in lowest terms.  At a state `(w,M)` the arrival multiplicity
`l` is a divisor of `M`, so only finitely many `l` occur.

1. A neutral clean step keeps `w` and sends `M` to a divisor of `l`, hence a
   divisor of `M`.  Its free `nu` changes no reduced state.
2. A resonant clean step has
   `Delta=(n-1)nu+1 >= 3`, `Delta | a`, and
   `w' = w*n/Delta`.  There are finitely many divisors `Delta`, finitely many
   factorizations `Delta-1=(n-1)nu`, and finitely many `l|M`.  Moreover
   `n<Delta`, so after reduction the positive integer numerator strictly
   decreases.  Thus zero-cost resonance cannot form an infinite reduced
   chain; neutral moves cannot increase `M`.
3. A pure-epsilon step chooses `l|M` and `1<=eps<l`, costs at least one, and
   has `w'=l*w/(l-eps)`, `M'=gcd(l-eps,nu+1)`.  The possible `M'` and the
   exact `nu+1` congruence classes are finite.  They can be obtained modulo
   `lcm(l-eps, d(l-eps)/gcd(d(l-eps),la))`.
4. For every remaining dirty step, P0 gives

   ```text
   C = l(k+lex)-Sm >= 1,
   T = Sm+l-eps(1+k+lex) >= 1,
   E = (l-eps)+nu*C,
   E | l*a*T,          nu >= 2.
   ```

   Each of the `k` northeast p-orbits costs at least one lambda unit, and an
   epsilon root costs another, so `k` is bounded by the remaining budget.
   Then `k <= Sm <= k(l-1)`.  If `eps>0`, `T>=1` gives

   ```text
   lex <= floor((Sm+l-eps(1+k)-1)/eps).
   ```

   If `eps=0`, `T=Sm+l` while
   `l+2C <= E <= l*a*T`, hence

   ```text
   C <= floor((l*a*T-l)/2),
   lex <= floor((Cmax+Sm)/l)-k.
   ```

   Thus the dirty parameter set is finite.  For each candidate, `E` ranges
   over divisors of `l*a*T`, and `nu=(E-(l-eps))/C` is then determined.  The
   remaining integrality, strict-NE, partition-price, and gcd tests are exact.
5. Every step outside the clean family costs at least one, so a budget `B`
   permits at most `B` such steps.  Between them, the zero-cost reduced graph
   is finite by items 1--2.  Finite branching and finite positive-cost depth
   prove the claim.

The proof is an abstract-state theorem.  The unbounded neutral `nu` ray is
real; it is quotiented because P0 chain transitions see it only through
finitely many congruence classes.  Whether every later merge consumer is
eventually uniform on those classes is a separate lemma.

## Exact implementation and charged replay

Packet:
`cases/m2_finite_reduced_chain_skeleton_r1_20260829/`.

- `finite_chain_skeleton_r1.py`: no historical global cap.  It derives the
  two `lex` bounds above, enumerates divisor-bound `E`, and represents the
  pure-epsilon free-`nu` family by exact residue classes.
- `test_finite_chain_skeleton_r1.py`: 35 checks under both ordinary and
  optimized Python, including an independent finite residue brute check,
  bound-stop mutations, deterministic charged hash, cap-token refusal, and
  scope firewalls.

Charged command:

```sh
python3 cases/m2_finite_reduced_chain_skeleton_r1_20260829/finite_chain_skeleton_r1.py \
  --w 3/2 --M 2 --budget 5 --output /tmp/m2-skeleton-r1.json
python3 cases/m2_finite_reduced_chain_skeleton_r1_20260829/test_finite_chain_skeleton_r1.py
python3 -O cases/m2_finite_reduced_chain_skeleton_r1_20260829/test_finite_chain_skeleton_r1.py
```

Observed:

```text
state_count 69
expanded_edge_count 295
max_reduced_w_numerator 3
max_M 25
max_k_observed 2
max_lex_observed 0
max_derived_lex_bound 27
zero_cost_reduced_nonincrease True
state_table_sha256 c2835aaf8450ab938170ae3808b5852d53f2c7b1ae29b14ca77b7965bf37f1ad
FINITE_CHAIN_SKELETON_R1_TEST_PASS checks=35
FINITE_CHAIN_SKELETON_R1_TEST_PASS checks=35
```

The exact 69-state/minimum-cost map equals the current legacy
`book_offaxis.close_p(3/2,2,5)` map; that legacy call returns `capped=False`,
maximum numerator 3, and maximum `M=25`.  Hence P5's prose example “70
states” is stale relative to its own current engine, in addition to the more
important incorrect word “unbounded.”

Current source hashes:

```text
6e413ff68a0b75f6a7fe28e091f1989b5cb74ed5f2d0f123630cb7520add8218  finite_chain_skeleton_r1.py
cd80757dd068c2af6bc1d0c2e15575e7a696224664dffa9645fc877c144ac38e  test_finite_chain_skeleton_r1.py
74f82b75fade7464dde5e9b57adb418110c0c8fc576a62a4898ef678c487cb18  charged JSON output
```

The README hash is intentionally omitted because this report records a
result appended to it after the first hash observation.

## First generic-AP consumer closed exactly

The packet also proves Grok's `S3/S5` discriminator uniformly, rather than
storing both values forever.  Freeze chain 1 at `(mu,w)=(1,2)` and let chain
2 arrive at the 0-direction with `(mu0,w,nu_H)=(2,3/2,h)`, where the neutral
ray has odd `h>=3`.  The two case-III handshakes give
`kbar=3h-2`, `X=3h-4`.  For the P3 ZCH shape

```text
dp=g+2, dq=(l+1)g+1, g=nu_G>=2, l>=1,
```

the ratio equation is exactly

```text
g*((3h-4)l-2)=3h.
```

If `l>=2`, the parenthesis is at least `6h-10>3h/2` for `h>=3`,
contradicting `g>=2`.  Thus `l=1`, and the equation becomes
`g(h-2)=h`; hence `h-2|2`.  Odd `h>=3` forces `h=3`, `g=3`.
The unique special value produces `(dp,dq,M_G)=(5,7,1)`, the known interior
MP2 kill.  Every odd `h>=5` is uniformly case-III-ZCH empty.

`td7_caseiii_special_nu_r1.py` emits this certificate.  Its independent
test scans the rectangle `3<=h<=1001`, `1<=l<=100` as a negative control,
checks the analytic inequality/divisibility proof, rejects cap tokens, and
passes 17 checks under ordinary and optimized Python.  Source hashes are
`f064e0930dc11d05c7276fa0420418ecf1efc62eed9a9b10a69bc626b88fa558`
and `f4cfa83df42cd38975482160848bc35146f8c26a5c66a7f5b5190638201ab7a8`;
the emitted JSON hashes `1e70f2e384eace6b325753a752e1db9247f7e07ba29dbdc2548440bdbba4f3b5`.

## What remains

The next theorem is not “finite states.”  It is **generic-AP uniformity for
every later consumer**: split each free-`nu` family into finitely many exact
special values and finitely many residue classes on which case I/II/III,
merge-shape integrality, downstream P0 menus, and terminal/budget typing are
uniform.  Grok's `S3/S5` pair already proves `(w,M,nu mod M)` is too coarse;
the exceptional-value table is load-bearing.

The first fixed-partner case-III discriminator now passes: its special table
is `{h=3}` and its generic odd ray is empty.  The next discriminator is to
generate this proof pattern for **every** partner/state in the finite charged
`td=7` skeleton, then compare the resulting cap-free cell book with P3/P4 and
E5.  Failure means some consumer contains an unbounded non-semilinear
dependency; success supplies the first cap-free `M>=2` quotient packet.

## Scope firewall

This result is conditional on P0 and covers reduced chain states only.  It
does not prove P0's imported sheet theorems, merge completeness, a full
configuration ledger, `G2-BD`, `RPMC(C)`, a cofinal topological-degree bound,
realizability, a Keller counterexample, or JC2.

---
Report-body SHA-256 (bytes before the separator line above): `8587625b2f12e486f9a3a3773ee5f4dcac7f853edcaddf69221dbab9ea7b1bcb`
