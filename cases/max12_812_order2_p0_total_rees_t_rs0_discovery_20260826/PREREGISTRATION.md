# Preregistration: total-Rees `T-rs-0` moving-source discovery

Date: 2026-08-26

Status: **DISCOVERY-ONLY SOURCE-FIDELITY PREFLIGHT.  NO REES, CHART,
MOVING-`p`, ORDER-TWO, MAXIMUM-TWELVE, OR JC2 VERDICT.**

## Question

The first `D_+(rs)` total-Rees client was stopped before launch because the
literal substitution `p=-2*rho^2` erased the frozen moving connection jets.
This preflight uses the corrected total source

```text
pTot = -2*rho^2 + 2*sigma*ell1 + 2*sigma^2*ell2 + ...,
cTot = sigma^2 C(sigma),
rTot = (pTot^2 + sigma^2 R(sigma))/4,
```

with `rho` and `sigma` independent.  It asks only:

1. what is the actual common `sigma` order through grade 12;
2. which finite primitive jets really occur in those rows;
3. whether `rho=0` recovers every frozen owner row through grade 12;
4. whether the rows are invariant under `rho -> -rho`; and
5. whether the reviewed raw cusp identity and omitted-`g10_3` negative
   control are recovered on the special fibre.

No Rees kernel, saturation, standard basis, radical, or chart unit is
computed here.

## Candidate ceiling

The compiler works modulo `sigma^13`.  Before any cancellation, a primitive
series shifted by `b` cannot need a jet above `12-b`.  The deliberately
overcomplete candidate ceiling is therefore

```text
p:       ell1..ell12                         (shift 0)
C,R:     leading coefficient through jet 10 (shift 2)
A0,A1,
E0,E1:   leading coefficient through jet 7  (effective shift 5)
K10:     leading coefficient through jet 8  (load shift 4)
K6:      leading coefficient only            (load shift 12)
K2:      no coefficient can occur             (load shift 20)
targets: no coefficient can occur             (first shift 26).
```

The frozen names are retained at their original indices.  New names are
namespaced (`az3`, `ac3`, `ez3`, `ec3`, `k10_3`, and so on).  The AWS output
prints a dependency bit for every candidate.  This V0 run does **not** know
the expected minimal manifest and therefore cannot pass a completeness
gate; its only valid output is the manifest to freeze into V1.

## Exact source obligations

All seven 569-monomial frozen Faber/source rows are reconstructed from the
charged `tails.json`.  In the quotient by `sigma^13`, the engine must check:

- exact rowwise equality after `rho=0` with the independently emitted frozen
  owner prefix, without setting the extra total-source jets to zero;
- rowwise invariance under `rho -> -rho`;
- recursive coefficient extraction at every grade `0,...,12`, with every
  multiplication-back identity;
- rowwise equality of every specialized extracted coefficient with its
  frozen counterpart;
- the exact V2 special-fibre certificate

  ```text
  32768*g12_6 - 35*k*rs^4
    + 4096*rs*g10_2 + 8192*cs*g10_3 = 0;
  ```

- the exact omitted-row residue `-1536*cs*c0*c1`;
- total difference `Delta` is even in `rho`, has zero special fibre, and is
  exactly divisible by `rho^2` in the coefficient ring.

The literal wrong source `p=-2*rho^2` is a mandatory negative control: after
`rho=0` it must fail comparison with the frozen prefix.  A second synthetic
omission of a discovered required jet must also be detected.

## Execution and interpretation

V0 runs independently at two good primes on separate AWS hosts.  Agreement
of the common order, dependency manifest, term counts, and Boolean controls
is navigation evidence only.  The manifest is then frozen before exact Q
and a fresh good-prime V1 rerun.  Any timeout, source-pin mismatch, missing
sentinel, nonunique sentinel, deck failure, prefix mismatch, or quotient
failure is `FAIL/UNRESOLVED`, never a mathematical verdict.

Even a later V1 PASS licenses only `T-rs-1`, the exact Rees/base-change test
for this one chart.  Five other standard charts, seven low-contact `A`
shards, the terminal square/Chebyshev receiver, `D(rho)` overlap, and every
global landing obligation remain open.
