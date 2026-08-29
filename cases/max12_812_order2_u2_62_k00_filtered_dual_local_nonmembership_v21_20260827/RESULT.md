# V21R1 exact filtered-dual corollary for V17 local nonmembership

Date: 2026-08-27

Status: **EXACT PRODUCER PASS; PROVISIONAL PENDING DIFFERENT-MODEL HOSTILE
REVIEW.**

## Exact theorem

In

```text
R=Q[d0,...,d5],  m=(d0,...,d5),
J_X=(r1,...,r6)+E_X,
D_X=h*a7^X-sum_i u_i*a_i^X,
```

for each `X in {K10,K6,K2}` from the frozen V17 source,

```text
D_X notin (J_X)_m.
```

Thus the three exact V17 mathematical branches are

```text
K10=LOCAL_NONZERO,  K6=LOCAL_NONZERO,  K2=LOCAL_NONZERO.
```

## Proof and exact certificates

If `D_X` belonged to `(J_X)_m`, there would be `s(0)!=0` with
`s*D_X in J_X`.  The image of `s` is a unit in every
`R/m^(D+1)`, so `D_X` would belong to `J_X+m^(D+1)`.

The fresh V21R1 replay gives exact rational functionals on those finite
quotients:

| direction | cutoff | matrix rank witness | dual support | pairing |
|---|---:|---:|---:|---:|
| `K10` | 4 | 603 ideal-image columns in 210 rows | 37 | `25/45056` |
| `K6` | 3 | 492 ideal-image columns in 84 rows | 11 | `45/11264` |
| `K2` | 2 | 70 ideal-image columns in 28 rows | 4 | `-25/352` |

Each functional annihilates every displayed ideal-image column and pairs
nontrivially with the target.  Therefore the corresponding truncated
membership is impossible, and the local membership is impossible by the
unit lemma.

## Independent replay and custody

V21R1 did not trust the V18R2 result sentinel.  On registered Box01 it:

- replayed all 66 serialized six-row syzygies over `Q`;
- freshly recomputed `Syz(r1,...,r6)`, obtained 66 generators, and checked
  mutual generation vector-by-vector; the serialized and fresh module files
  are in fact byte-identical, both SHA-256
  `83832f380ce11a491c9799e50ff8b36b5fbc3a6b0d5b5dc52d90b6239c129a7a`;
- regenerated all three 66-generator images and all three targets from the
  exact load rows and V14R1 `h,u_i`, with a sign-mutation control;
- independently reparsed the exact polynomials and byte-reemitted each
  complete truncated Macaulay matrix and its row/column map; and
- replayed all three exact rational duals and pairings.

The R1 source freeze manifest has SHA-256
`4c35362b7223566317ca346bd261fb13023fbb3d8a48aef2908dd00d1a168026`.
The 31-input manifest has SHA-256
`38c6dd45b888ec04a5c0b9bdd4b93625a1df491b4e4f63851f5546cb1d7d465f`.
The exact result JSON has SHA-256
`7341d67bb6abfba9ce1b99d6670360721214aaf6bbb51165dbf84964c65e7ad3`.
The 49-file harvested evidence manifest has SHA-256
`00159ec022932932373fc294980541ca791a173e5bbdbe58072d84d6b3b74b49`.

R1 used one core, 59,536 KiB maximum RSS, 10.40 seconds wall time, and zero
swap.  R0 is preserved separately and is nonpromotable: it failed closed on
wrapper semantics before matrix or dual replay.

## Dependency repair and scope

This corollary supersedes only V18R2's preregistered administrative order
`no promotion before monolithic V17-Q`.  It does so by supplying an exact
proof of the same three V17 local-nonmembership statements from stronger
finite exact certificates.  It changes neither the definitions nor the
mathematics of V17/V18.  The monolithic colon lane continues as an
independent cross-check; disagreement would force an audit.

The theorem consists of three separate first-order load classes in the
normalized K00 coefficient-local ring.  It does not couple the loads,
restore Lambda weights, include `mu/Jdet` through grade 19, give honest-source
reachability, exclude an arc, decide closure incidence, or imply order two,
maximum twelve, or JC2.

