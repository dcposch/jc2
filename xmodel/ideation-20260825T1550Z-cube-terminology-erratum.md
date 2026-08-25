# Terminology erratum — `20260825T1550Z` cube-owner report

Date: 2026-08-25  
Status: **NONMUTATING TERMINOLOGY CORRECTION**

The sealed report

```text
xmodel/ideation-20260825T1550Z-cube.md
SHA-256 e5e85f071257d6be9c225c351ba3fc8a84bee6d64a42ac7e87bca9acf793b890
```

uses “right-conjugates”, “right-conjugacy”, and “AS-conjugate coordinates”
in several headings and summary labels.  Replace every such occurrence in
mathematical consumption by the corresponding form of:

> **integral right-compositions, equivalently integral source transforms**,
> and **AS source-transformed coordinates**.

Precisely, with `A(s,t)=(s-s^3,t)`, the seeds are

```text
G9=A o B9,
G8=T8 o A o B8,
```

where `B8,B9` are determinant-one polynomial source automorphisms and
`T8(s,t)=(t,-s)` is a determinant-one target change.  Conversely an integral
lift `F` of either seed is transported back to the AS residue chart by

```text
T^(-1) o F o B^(-1).
```

This is not group conjugation `B^(-1) o A o B`, and no claim in the sealed
report requires such conjugation.  All formulas, degree counts, collision
statements, scope firewalls, and experiment rankings are unchanged.
