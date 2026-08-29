# Hostile review: Sigray Proposition 5.1 forced-puncture-shift repair

You are the independent adversarial referee.  Work in
`/Users/dc/code/math/jc2`.  Read the complete frozen producer:

```
xmodel/sigray-prop51-forced-puncture-shift-sol-ultra-20260828.md
SHA256 a0470416481378c02cc5a20e8aef826be1203c32c6dbfe664ae197cfdc34b9dc
```

Read the exact checker and run it:

```
cases/sigray_prop51_forced_puncture_shift_20260828/verify_threshold.py
SHA256 f719ef535d1d27ac0a172eb41c6eef6f4027b484404cb7bb7b1df63586507fab
```

Read its custody file:

```
cases/sigray_prop51_forced_puncture_shift_20260828/CUSTODY.md
SHA256 f3ece41268fdc1af9119dad3b598a3c4d9e819bc9101c6bdb2ba27b4224395c6
```

Read the primary source itself, not merely campaign paraphrases:

```
refs/sigray_full.pdf
SHA256 9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae
```

At minimum inspect printed/PDF pp. 13--18 (definitions and Statements
3.9--3.18), pp. 18--24 (Propositions 4.1--4.3, Proposition 5.1 and Notation
5.1), and pp. 35--37 (Propositions 7.2--7.3).  Also read the relevant rows and
consumer notes in `ladder/SIGRAY-AUDIT.md`.  You may inspect other top-level
Sigray/landing contracts as needed.  Do not read or touch `jc2-lean`.

## Charge

Try hard to refute the producer.  In particular:

1. Check that `p_{f-a,F_v}` really has positive degree for every rational
   truncation on `P`, including nonvertices and after the last characteristic
   exponent.
2. Check the proof that the forced `B_P=g-b_P` satisfies condition (7) for
   every `v`.  Audit the use of corrected Statement 3.15, its no-common-root
   hypothesis, and the zero/finite-nonzero/pole label swap.
3. Re-derive the leading-bracket formula
   `d p q' - e p' q`.  Check the claim that `rho>0` plus (7) forces
   `deg q>=1`, including `d=0`, `e=0`, and Laurent/inverse cases.
4. Re-derive continuity, monotonicity, the slope
   `1-deg p-deg q`, finite-breakpoint use, existence of a zero, persistence
   of zero, and rationality/minimality of the first zero.  Look for a jump or
   open-endpoint countermodel.
5. Check whether translating to `(f-a,g-b_P)` genuinely licenses corrected
   Proposition 4.2 on `T_a^+` and Proposition 4.3 on `T_a^-`, and whether
   `m=0 iff rho=0` is exact.
6. Decide the all-`v` typing point independently: is `m_F` actually undefined
   on `T_a^0`, or is there an implicit convention elsewhere in the thesis?
   Is the producer's global leading-Jacobian predicate the cleanest repair?
7. Test uniqueness/necessity of `b_P=g(P)` at finite punctures.  Check the
   stable-tail model (4.1)--(4.2), including signs under the audited correction
   of Statement 3.15.  Distinguish what is proved geometrically from what the
   checker merely samples.
8. Check whether Proposition 7.3 is only corroboration or is used circularly.
   Determine exactly what Proposition 5.1/Notation 5.1 is repaired, and what
   downstream results (Statement 5.1, Notation 5.2, Proposition 7.2, etc.)
   still require separate proof or wording changes.
9. Enforce the pole firewall: for `g(P)=infinity`, does `b_P=0` leave the
   selected positive pole vertex, `m_F=0`, `h_0=g`, `M_F`, `Q(F)`, `Lambda`,
   and existing pole-only campaign consumers unchanged?  Flag any hidden
   finite-threshold leakage into pole claims.
10. Check separation from the promoted Proposition 4.2 repair.  Do not let a
    claim about one theorem silently supply the other.

## Output contract

Write exactly one new report:

```
xmodel/sigray-prop51-forced-puncture-shift-hostile-review-opus5-20260828-r1.md
```

Do not edit the producer, checker, custody file, canonical ledgers, source
PDF, any other file, or `jc2-lean`.  The repository is heavily dirty from
other live lanes; do not interpret unrelated changes as yours.

Begin with model/version and a one-word terminal verdict:

- `PASS`: theorem and scope stand as written (minor prose nits may be listed);
- `REPAIR`: core result survives but exact mathematical/textual repairs are
  needed; give replacement text;
- `FAIL`: exhibit the exact counterexample, circularity, or missing theorem.

Give page-cited derivations, not deference.  Separate producer errors from
pre-existing source errors.  End with the SHA256 of your report and state
whether the three frozen input hashes still match.
