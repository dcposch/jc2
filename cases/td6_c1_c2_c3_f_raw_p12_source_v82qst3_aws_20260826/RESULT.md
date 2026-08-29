# TD6 V82QST3 raw `F=0` genuine-P12 result

Date: 2026-08-26

Producer verdict: **PASS on Box02 and r6a, q2 and q10.**

## Exact result

On the fixed source-typed A3 specialization

```text
C0=(V^2-U^3)/U,  F=0,
```

the genuine 2,893-term raw P12 polynomial and 28 active packed FIRST source
rows satisfy an exact cleared identity

```text
V^4*U^9*(V^2-4U^3)^3
  = h_P*P12 + sum_i h_i*FIRST_i.
```

The emitted coefficient table has 1,490 nonheader entries: one P12
multiplier and 1,489 FIRST multiplier monomials across 28 source rows.  The
replay audits 612,828 scalar coordinates of cleared multipliers and termwise
products; every one lies in `Q[U,V]`.  Exact source replay, an active-row
omission negative control, and the cleared identity all pass.

Before inversion and clearing, the P12 remainder is

```text
(-126/25,171/25,-72/25,18/25,0,...,0)
```

in the frozen degree-18 coefficient field.  Its SHA-256 is
`b9445255e063a82f827a01b7e18c3bdd2f3da41de14903a73fc2ae68121df7a0`;
the specialized genuine-P12 polynomial SHA-256 is
`da0d595ecbdc1922b127bba6b54d935a4631618eed617fb99c9fa95cbdec534f`.

The clearer factorization is exactly

```text
(V^2-4U^3)^3 * V^4 * U^9,
```

with no outside factor.  Therefore the fixed-A3 `F=0` system is empty on
`D(U*V*(V^2-4U^3))`, which is stronger than the preregistered open that also
inverted `V^2+8U^3`.

## Source and Box02 custody

- wrapper SHA-256:
  `6977d0acb3d178447effe225f80f7f415a23042090092a648a8bbfbfc462a497`;
- imported V82QST2 wrapper SHA-256:
  `5a1054269237d9a2da5c7f5e51ae001ad59f61607ac36f2e7a9b059c972c74d5`;
- imported source archive SHA-256:
  `731eed3fdbaaf17b9f14468ca885f16bf4008f1b43bb8b276a99a530966a6d5c`;
- Box02 q2 stdout/stderr SHA-256:
  `8135c56ad8547e6e492df02b525fbba5bce06f6d1dddcaeade0ba218e5afef3f` /
  `a5b3d980182e56dae1c35c0992e21684ac92193b292748a17c33f5f5fa77befa`;
- Box02 q10 stdout/stderr SHA-256:
  `cf155aee39236827539775a6d72fbd7a4636cf5d574fe92add618a43a1838402` /
  `1f06161a9255acfb206925f06cdc2712f24e719160068f983a0d9af83f3f8492`;
- byte-identical q2/q10 certificate SHA-256:
  `8e892ffa914e0f93969abb9722f926486843f59cf77f5861c5ce3d3438281482`;
- selected q2/q10 base-result comparison SHA-256:
  `1e21693abf0f0354aa438c056b391ec2cf6aa0ecab6935b5186597c13b73dd91`.

q2 completed in 10:43.63 at 511,472 KiB maximum RSS; q10 completed in
10:58.15 at 510,720 KiB.  Both returned `rc=0`, used zero swap, and ended on
`TD6-V82QST3-F-RAW-GENUINE-P12-SOURCE PASS`.

The independent r6a endpoints also returned `rc=0` and the same PASS banner:

- q2 stdout/stderr SHA-256:
  `1f5fe66612d6508e5271e429bf31f1b5e14e4bbedbf719aff631a87e3d825455` /
  `4112405a7af1d519871dc5a0f0be66164a453a149ad62308c9b06af633932990`;
- q10 stdout/stderr SHA-256:
  `d181dfa757b40cfaf88212dd1679208a02787bfb77a3cfd4eece3cd9f8294c1a` /
  `95126e485437b61a65ae4c191485b84621726a81275c20631ea3966b756d1c68`.

r6a q2 completed in 17:20.18 at 510,188 KiB maximum RSS; q10 completed in
17:47.74 at 512,004 KiB.  Both used zero swap.  All four certificate files
are byte-identical with SHA-256 `8e892ffa...`; all four selected base-result
streams have SHA-256 `1e21693a...`.

## Scope firewall

This certificate bypasses PREVIOUS/POLE and staged CURRENT, so its narrow
fixed-fibre base conclusion does not depend on the V82QST1C Gate-1
alternate-pivot comparison.  It confirms that the thirteen V82QST2 outside
factors came from its global staged denominator over-approximation; it does
not adjudicate that staged CURRENT tangent table.

The identity is formed after `F=0` and freezes q, dead-stretch, and correction
directions.  It is not an identity in one total family of the form
`s=sum h_i*f_i+F*h`, so it excludes no positive-`F` valuation arc and proves
no whole fixed A3 result, TD6, SP-2, or JC2.  The required total-family
successor is specified in `TOTAL_F_LIFT_DESIGN.md`.
