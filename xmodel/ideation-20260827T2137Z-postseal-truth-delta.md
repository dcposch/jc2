# Post-seal truth delta for cross-review — round `20260827T2137Z`

Status: review input only. This file was created after all four blind submissions
were sealed. It does not alter their custody or retroactively change their basis.

## Sealed submissions

- Sol Ultra: `xmodel/ideation-20260827T2137Z-sol.md`, SHA-256
  `2112a0ad5fbc4fcc5d1a26efd725c01500186f6299b5b591e2849eb0a865ac32`.
- Grok 4.6: `xmodel/ideation-20260827T2137Z-grok46.md`, SHA-256
  `bfd18a275165e1740f883222c1a6e0f8b43cb5e2737d18b8eea01b9c2615d57e`.
- Opus 5: `xmodel/ideation-20260827T2137Z-opus5.md`, SHA-256
  `49dd042a15670f082ea4335610150eee3022fc7a37282df200e2ae3a052ea0a0`.
- Fable 5: `xmodel/ideation-20260827T2137Z-fable5.md`, SHA-256
  `edd383ad33838268cc7e700f2aa913dab73eb6744a60133a131a69eb7ef476bb`.

## Facts established after the packet freeze

1. **The Corollary-7.4 physical-other-chart interpretation is refuted.**
   Opus 5's source-level hostile review proves that the transposed 7.3/7.4
   packet is subsumed by native 7.1/7.2 and, on live `8_28`, certifies the
   same physical `upper_dir=(-3,1)` edge. Native 7.2 is strictly stronger
   for `l>1`. The exact powers 12 and 8 remain correct, but are already
   supplied natively. Source:
   `xmodel/g2-c74-place-exit-rpmc-hostile-review-opus5-20260827.md`, SHA-256
   `968b42ced94bd6c59b33bfdab30677e2ad6ad91a349fc978a271c01083d11e7d`.

2. **`C74-PLACE` is mislocalized and must split.** L1 face-power custody is
   available natively; L2 multiplicity convention is available; L3
   `H-TRUNC` remains open; L4 chart coverage belongs to the exact-pair
   constructor; L5 deck/leaf-place bijection remains open. Therefore no
   review may treat the old `C74-PLACE -> EXIT-RPMC(C)` corridor as a live
   source of the missing physical chart.

3. **`EXIT-RPMC(C)` is equivalent to existing `RPMC(C)` as stated.** Its
   clause 1 already assumes every dicritical subtree exits, and under that
   clause the proposed exit inequality is just the original sum. It
   localizes notation but removes no proof cost.

4. **VGG minimal re-selection is chart-rigid.** The general van den Essen
   normalizer is tame, not a priori affine, but VGG Proposition 4.7 forces
   the final normalizer between oriented minimal representatives to be
   affine; UFD forces its linear part diagonal, since anti-diagonal swaps
   the ordered degrees. Proposition 5.20 adds only a translation. Thus
   same-orbit VGG re-selection preserves the two physical place sets and
   cannot expose the missing chart. Source:
   `xmodel/g2-vde-normalizer-chart-tracking-source-audit-sol-ultra-20260827.md`,
   SHA-256
   `a5a9c04a6cb1d8b4b65fe64ae9365cf5b51cf2a9761843f75709ce4c42778566`.

5. **Finite-end identity confirmed; marked refinement is narrower.** For a
   generic fibre, `sum_N e_S = td + b1 - 1` is confirmed. Chau's component
   degree theorem gives a new-to-repository marked-profile congruence:
   counts of each generic marked asymptotic-component type are `0 mod alpha`.
   On the clean residue-A, `alpha=2` census this prunes 169 passports to 48,
   but kills none of those 48. Ordinary passports lose the marking on
   `e=1` fixed ends, and braid orbits are on branch values, not sheet blocks.
   Source:
   `xmodel/g2-finite-end-asymptotic-monodromy-connection-sol-ultra-20260827.md`,
   SHA-256
   `0f201502716ca9c9bf33718412739e0254981c2eb7204657dc78ee7fbcd653c1`.

6. **Small repairs for any G2 reuse.** Frozen orientation has
   `(m,n)=(beta,alpha)=(3,2)` and `(alpha,beta)=(2,3)`. Proximity closure
   means the full relation “proximate to,” not merely the parent edge. The
   correct primary-source hashes are VGG TeX
   `b4908fd596d555c745b3bdce9613e64c056052d7237efc1419d9c24c0e6004d5`
   and GGV5 TeX
   `8f5571e527c4e579b185f7e75dcf48cd6c92fa88c82c46c33019d38ab89d78f5`.

## Cross-review rule

Judge every blind proposal against these facts. Preserve ideas that do not
depend on the refuted corridor, but explicitly delete or refile any stale
dependency. Separate an exact theorem from optimistic independence or
realizability assumptions, and state the narrowest promotable result plus the
cheapest decisive next test. Do not inspect, list, search, or modify
`jc2-lean`; do not modify any campaign artifact except the assigned report.
