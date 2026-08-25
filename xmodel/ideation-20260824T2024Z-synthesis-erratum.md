# Erratum to `20260824T2024Z` ideation synthesis — parity-normal rank gate

Date: 2026-08-24  
Parent synthesis SHA-256:
`769c1aac6f9ce5d53dfdcb74a4edca9e2ca10a856fe7ef436365f002ebda0f79`

The parent synthesis correctly records the blind proposals and overall
allocation, but its post-cutoff `M12-Q12-KURANISHI` row and the corresponding
paragraph in section 6 are superseded.

Hostile review
`xmodel/max12-912-order3-nu-parity-normal-q12-review-grok-20260824.md`
(SHA-256
`fc0b0216784bdcec8f9b0955c5a6c71d57870ae2265ed927f306d19d31a79c30`)
found that the producer replay used

```text
x1=x5*p^2*(v+1)+x5^2/(27v)
```

instead of the actual-fibre substitution

```text
x1=x5*p^2*(v+1)+x5^2*(3v+1)/(9v).
```

The former does not satisfy `r2=r4=0`; its passing `Q12` determinant is an
off-fibre identity.  The `Q12` checkpoint and its dependent formal-branch
package are therefore `QUARANTINED`, byte-preserved, and excluded from every
allocation premise and lifecycle count.

The reviewer independently reconstructs a squarefree residual octic

```text
Q8=-999v^8-1539v^7+1782v^6+6498v^5+7320v^4
   +4428v^3+1548v^2+296v+24,
```

coprime to the chart factors and to `Q12`.  This is reviewer evidence, not a
replacement theorem.  The exact successor is to freeze the determinant on
the correct chart with an old-pass/new-fail control, then retest the formal
branch argument at `Q8` from scratch.

Unaffected: the reviewed parity genus-five exclusion, the confirmed full-
absorption theorem, the DZ20 theorem, the root-free critical-value-norm idea,
and the synthesis ranking of normalized maximum-12 strata ahead of ambient
primary decomposition.  No proof or counterexample to JC2 was claimed.
