# Erratum to the T1820Z TD6-owner ideation submission

## Custody and status

- Frozen submission: `xmodel/ideation-20260824T1820Z-td6-owner.md`
- Frozen submission SHA-256: `a3d56f67a3eea45db761ba72a41c2f424fc10e1509e50630c5515cacdb9866e2`
- Lifecycle: **ERRATUM / SCOPE-CONFLICT**
- Scope: the proposed single localized affine Smith/syzygy certificate for all post-transport stages of the `c1` family.
- This erratum does **not** alter the frozen submission. It supersedes only that proposed certificate's source-validity claim.

## Exact post-collection compiler check

The attempted dependency-complete construction compiled the raw transport system over
`E[c1]`, obtained the already certified generic transport rank `3470/3602`, and selected
`132` free transport variables. It then attempted to compile first, previous/pole, and
current equations simultaneously as an affine `110 x 132` matrix.

That attempt is not source-valid. Before the first-band equations are solved and
substituted, the previous/pole and current equations contain genuine parameter
monomials of degree at least two in the 132 transport variables. The affine compiler
therefore stopped at its invariant

```text
assert len(monomial) == 1
```

rather than emitting a false affine matrix. Private deterministic check artifacts:

- `/tmp/td6-centering.yycIQu/c1_dependency_complete.py`
  SHA-256 `cf6ca560b0b6ed7fc34db6ae393d904b2d702a9656fb90340fad1055c589d385`
- `/tmp/td6-centering.yycIQu/c1_dependency_complete.stdout`
  SHA-256 `fc8773b5e8ebde1c5822b7082486b14332ab6b867b679bf18d183dbf8a0cdcfc`

The stdout records the exact transport pass and exceptional transport factors
`c1` and `c1-3`; the subsequent affine compilation failed before producing a
dependency-complete later-stage object.

## Correct source-typed replacement

The licensed exact gate is stagewise.

1. On the first-stage pivot open, solve and substitute the first-band equations.
2. On the previous/pole pivot open, solve and substitute those equations.
3. Only then clear denominators and compute current-stage Smith/syzygy or Fitting
   data. Such a certificate covers current-stage pivot roots only inside the earlier
   opens.
4. Every root of a previous-stage pivot factor must be specialized and rebuilt from
   its parent first-stage parameterization; every root of a first-stage factor must be
   rebuilt from the transport parameterization.
5. The raw transport fibres `c1=0` and `c1=3` must be rebuilt adaptively from the
   original 3,602-column transport system.

An alternative, substantially more expensive gate would retain the nonlinear
post-transport ideal and seek a Nullstellensatz/Fitting certificate. It cannot be
represented by the rejected affine `110 x 132` matrix.

## Claims unaffected

This correction does not change the exact generic `c1` incompatibility, the staged
dual-number `c3` computation, the degree-36 Belyi passport observation, or any other
portion of the frozen report. It licenses no family kill and no SP-2 or JC2 conclusion.

