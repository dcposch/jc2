# Max12 `(9,12)` selected-Q8 infinity-contact passport gate

This lightweight case pins the reviewed corrected-Q8 local geometry and the
review-corrected terminal Belyi classification.  It checks the exact
`e_pass=2` noncube terminal/Kummer control and records the contact-order and
Mason-sharp consequences.  It does not run a CAS.

```sh
python3 cases/max12_912_order3_nu_q8_infinity_contact_passport_20260824/replay.py \
  | diff -u cases/max12_912_order3_nu_q8_infinity_contact_passport_20260824/replay.json -
shasum -a 256 -c \
  cases/max12_912_order3_nu_q8_infinity_contact_passport_20260824/MANIFEST.sha256
```

The theorem is conditional on an actual trajectory whose quotient image lies
on the global irreducible component selected by the corrected-Q8 formal
branch.  The positive control realizes only the terminal/Kummer subsystem;
the seven-row coefficient fibre, both complete Taylor polynomiality families,
and all projective boundaries remain charged.
