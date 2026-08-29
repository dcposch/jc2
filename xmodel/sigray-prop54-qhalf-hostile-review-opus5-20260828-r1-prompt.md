# Hostile review: Sigray Proposition 5.4 `q`-half repair

You are the independent adversarial referee.  Work in
`/Users/dc/code/math/jc2`.  Read the complete frozen producer:

```text
xmodel/sigray-prop54-qhalf-sol-ultra-20260828.md
SHA256 f2ee74b5c8f07048488c3b78e5f76bc293beae4b7199614ce75b8e1c18165f75
```

Read and run the exact checker:

```text
cases/sigray_prop54_qhalf_20260828/verify_qhalf.py
SHA256 4c6164b9cf01a797ca6d1029e038f44d7e9f32b34e405c38ec53b2c2f2256bea
```

Read its custody file:

```text
cases/sigray_prop54_qhalf_20260828/CUSTODY.md
SHA256 21cd5407791da8a8426d2792548b177183fae73d732e4ff11c33657360f7430f
```

Read the primary source itself, not merely campaign paraphrases:

```text
refs/sigray_full.pdf
SHA256 9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
```

At minimum inspect printed/PDF pp. 8--9, 15, 17, and 23--27.  Read the
Proposition 5.4 row and relevant source corrections in
`ladder/SIGRAY-AUDIT.md`, plus actual promoted consumers
`ladder/SHEET6-TDUNIFORM.md`, `ladder/SHEET6-AF3.md`, and any directly cited
review needed to type those uses.  Do not read or touch `jc2-lean`.

## Charge

Try hard to refute the producer.  In particular:

1. Re-derive exactly what Proposition 5.3(iii) says from Proposition
   4.6(11) at `m_F=0`.  Check that the right side is a nonzero constant, that
   the suppressed scalar is harmless, and that writing
   `(k_f,k_g)=s(alpha,beta)` is licensed without using the inverted printed
   ratio in Proposition 5.3(ii)/(viii).
2. Audit the source chain giving
   `p=eta^epsilon P(eta^nu)`, `epsilon in {0,1}`, and a simple root.  Check
   axes, `F in V_a`, canonical removal of powers of `eta^nu`, squarefreeness,
   nonconstancy/more-than-one-root, and whether any of these conclusions
   already consumes `alpha>=2`.
3. Recompute the `mu_nu` isotypic projectors and differentiation law.  Check
   signs and characters in
   `L(q_r)` and prove that the inhomogeneous component is precisely
   `r=1-epsilon`, including `nu=2` and zero components.
4. Attack the local kernel proof.  At a simple root, check both the initial
   evaluation `R(a)=0` and the order-`m` coefficient
   `alpha*m-beta`; look for constant, rootless, Laurent/rational, or
   characteristic exceptions.  The theorem claims only polynomial `R` over
   `C`.
5. Attack `alpha=1` independently.  Verify or refute the exact mixer
   `(nu,alpha,beta,p,q)=(3,1,2,eta,1+eta^2)`, including bracket,
   squarefreeness, coprimality, degree ratio, and character mixing.  Then
   decide rigorously whether any mixer can satisfy the independently imposed
   pole-vertex hypothesis `deg p>=2`; audit the producer's subtraction of
   `C p^beta` and no-solution conclusion.  State precisely whether the
   existing audit phrase "for alpha=1 genuine counterexample solutions
   exist" is correct, needs qualification, or is false.
6. Audit the auxiliary-`h` `kappa`/common-lcm discussion against the freshly
   exposed Statement 3.9 defect.  Decide whether the q-half genuinely avoids
   Statement 3.9 and whether the proposed finite common lcm is enough for
   any surrounding use.  Do not let this report silently repair arbitrary
   tower consumers.
7. Re-derive the downstream Statement 5.2(ii) divisibility menu from the
   two character patterns plus the corrected degree ratio.  Check every gcd
   step.  Inspect every promoted direct consumer of Proposition 5.4 or
   Statement 5.2(ii), especially TDUNIFORM R2 and AF3 parity, and report
   whether this theorem supplies exactly what they use or whether another
   unproved assertion remains.
8. Enforce separation from Proposition 4.2's constant-shift repair,
   Proposition 5.1's finite-puncture repair, Proposition 5.8, later
   decorated-tree propagation, landing, and JC2.
9. Audit the checker rather than trusting its PASS: matrix orientation,
   augmented-rank consistency, cap sufficiency, squarefree/gcd routines,
   positive fixtures, wrong-character mutations, and the alpha=1 control.
   Add at least one genuinely independent nonconstant exact control (not a
   copy of a listed fixture), by hand or a separate small standard-library
   calculation.  Do not use heavy local CAS.

## Output contract

Write exactly one new concise report:

```text
xmodel/sigray-prop54-qhalf-hostile-review-opus5-20260828-r1.md
```

Do not edit the producer, checker, custody file, canonical ledgers, primary
source, any other file, or `jc2-lean`.  The worktree is heavily dirty from
other live lanes; do not interpret unrelated changes as yours.

Begin with model/version and a one-word terminal verdict:

- `PASS`: theorem and scope stand as written (minor prose nits may be listed);
- `REPAIR`: core result survives but exact mathematical/textual repairs are
  needed; give replacement text;
- `FAIL`: exhibit the exact counterexample, circularity, or missing theorem.

Give page-cited derivations, not deference.  Separate producer errors from
pre-existing source errors.  End with the SHA256 of your report and state
whether all four frozen input hashes still match.
