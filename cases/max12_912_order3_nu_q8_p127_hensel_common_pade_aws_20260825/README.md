# Simultaneous Padé for the selected-Q8 moving-v lift

`common_pade.py` parses the exact Singular series for all seven lifted
coordinates and all 190 moving-v coefficients. It first checks that order 16
is an exact prefix of order 32. It then searches for one scalar denominator
`D(s)` shared by all `7*190` sequences.

The order-16 coefficients are the training set and coefficients 16--31 are a
true holdout. A separate full-order-32 fit is emitted for later order-64
validation. The script includes synthetic known-rational and perturbed
negative controls.

Any recurrence is **provisional**. Acceptance as a global coordinate graph
requires reconstruction of all numerators followed by exact substitution of
the seven rational functions in every original quotient row modulo
`H(w,v)`. All substantive execution is AWS-only.

