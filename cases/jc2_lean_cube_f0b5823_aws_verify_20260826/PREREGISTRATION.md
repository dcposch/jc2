# Preregistration — AWS verification of cube landing commit `f0b5823`

Date: 2026-08-26 02:29Z

Status: **BUILD/AXIOM HYGIENE ONLY; NOT SOURCE-COMPLETENESS EVIDENCE**

Frozen source:

```text
commit=f0b5823c2d008807fa6524401faf2e1413d7a5f8
archive_sha256=856c337c42b6dea21abaafc65ac794e39a1deaf47c4c72462871cf2bcf59d982
solution_sha256=6407444078ad5ea0ce93ec55440b2629d10676abcff6614887ef47c97e8e0de2
```

Required AWS/Linux gates:

1. reproduce both frozen hashes and record EC2 DMI, hostname, tag, UTC times,
   Lean/Lake versions, and source-file hashes;
2. run `lake exe cache get`, `lake build`, and direct
   `lake env lean Solution.lean` under a 16 GiB / 3600 s cap;
3. require the named landing/gluing and every consumed branch theorem in the
   direct axiom stream;
4. reject any `sorryAx` occurrence and require rc zero;
5. preserve stdout/stderr/rc and rehash locally after retrieval.

Passing proves only that the exact declarations compile and have the printed
axiom dependencies.  In particular,
`GCD369CubeTrajectoryLandingEmpty : GCD369CubeTrajectoryLanding K -> False`
does not itself prove that every genuine cube source constructs an inhabitant
of `GCD369CubeTrajectoryLanding K`.  That source-to-landing coverage map is a
separate mathematical obligation under hostile review.
