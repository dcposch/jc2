# Correction addendum — Sigray Proposition 6.7/6.8 hostile review

Date: 2026-08-28  
Status: frozen correction to the Opus 5 review; the reviewed file itself is
unchanged.

## Custody

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
c3d6ff9239fb136cc35b815de6e229755f7d27b640481e7751d03d63291d1ebd  xmodel/sigray-prop67-prop68-source-audit-sol-ultra-20260828.md
eb37373b3bf84c83b0f4774968690f650fb3a62635baa66e35e81096f8f30db4  xmodel/sigray-prop67-prop68-source-audit-hostile-review-opus5-20260828-v1.md
```

## Two corrections

1. **The ratio criticism in Section 3 is withdrawn.**  The primary-source
   display in Notation 2.4, printed p. 9, defines

   ```text
   alpha/beta = k_f/k_g.
   ```

   Therefore `d_(g,F)/d_F=k_g/k_f=beta/alpha`, and the producer's display
   `kappa*d_(g,F)=beta/alpha` is correct.  The hostile review accidentally
   inverted the fraction while reading the text extraction.  Its related
   criticism of the Proposition 5.3 ledger row and item 5 of its amendment
   list are also withdrawn.  The producer's nonintegrality argument needs
   only `alpha>=2` together with `gcd(alpha,beta)=1`, exactly as written.

2. **The finite-threshold aside in Section 3 is withdrawn.**  Under the
   campaign's repaired Proposition 5.1, finite-puncture thresholds lie in
   `T_a^-`, pole thresholds lie in `T_a^+`, and neither lies in `T_a^0`.
   Notation 7.1 instead defines the distinct critical-value set
   `T_(a,cv) subset T_a^0`; Proposition 7.2 characterizes a finite value
   `g(P)` by the existence of such a critical-value vertex somewhere on the
   branch.  It does not identify that vertex with the repaired Proposition
   5.1 threshold.  The hostile review conflated these two constructions.
   Consequently its suggestion to strike the Proposition 5.1/no-first-corner
   dependencies from the producer's Section 2.1 is not established and is
   withdrawn; the producer's explicit finite-versus-pole disambiguation may
   be retained.

## Verdict after correction

The terminal verdict remains **REPAIR**, with no rollback of Propositions 6.7
or 6.8.  The surviving repairs are the load-bearing `h=h_G` completion, the
two missing microstep-to-vertex steps, completion of the cyclic residual
semi-invariance proof, the Proposition 6.8 printed-bound correction, and the
open audit dependency on Lemma 6.1.  This addendum changes no canonical file.
