# TD6 V89H12 R2 packaging erratum

Date: 2026-08-26

Both R2 AWS lanes returned rc 127 before checksums, imports, or algebra.  A
packaging command accidentally inserted the run script into the archive as

```text
run_v89h12_allq_p12_full_normal_FORM.sh
```

while the Linux launcher correctly requested the registered lowercase name

```text
run_v89h12_allq_p12_full_normal_form.sh.
```

The case-insensitive packaging host masked the basename mismatch; Linux did
not.  R2 is deployment-negative only and has no mathematical interpretation.
R3 rebuilds the archive from a clean source directory using only the exact
registered lowercase basename.  The R2 mathematical client and corrected
94-variable preregistration are unchanged.
