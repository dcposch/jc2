# Corrected-Q8 full-contact Jacobian over `F_127`

Date: 2026-08-25  
Status: **PRODUCER-EXACT BOUNDARY-LOCAL CERTIFICATE; review required**

The same pinned divided localized source used by the selected-Q8 quotient
probe was evaluated over

```text
A = F_127[v]/(Q8bar(v)).
```

Here `Q8bar` is squarefree.  The contact section uses the corrected formula

```text
x5 = -36 v^2 (3v^2+3v+1)/(3v^2-2),
x3 = x5(v+2),
x1 = x5(v+1) + x5^2(3v+1)/(9v).
```

The remaining coordinates `c,d2,d4` were not imported from a different
presentation: they were solved in `A` from rows `e3,e5,e7` of the same
approximate-cubic divided source.  Its normal `3 x 3` determinant is a unit.
The resulting degree-less-than-eight representatives for all eight section
coordinates are recorded in `aws_box02_v1/result.json`.

Exact substitution gives zero for all six source rows

```text
e1,e3,e5,e7,e2,e4,
```

for `v*x5-x3+2*x5`, and for
`inv*x5*(x3-2*x5)-1`.  The elements

```text
v, 3v^2-2, 3v^2+3v+1, normal determinant,
x5, x3-2x5, x5(x3-2x5), 9v
```

all have gcd one with `Q8bar` and nonzero norm.  Thus the displayed rational
contact formulas define an integral section of this finite etale algebra and
the localization is licensed at all eight geometric contacts.

At fixed `w=0`, take the full relative Jacobian of those eight equations with
respect to

```text
(c,d2,d4,x1,x3,x5,inv,v).
```

Its determinant has degree-less-than-eight representative

```text
[101,42,36,116,8,110,107,14]
```

(low-to-high in `v`), gcd one with `Q8bar`, and norm `88 mod 127`.
Consequently the full divided localized source has relative rank eight at
every conjugate corrected-Q8 contact.  This is stronger local data than, and
logically separate from, the plane projection check `H_v != 0`.

As a negative control, replacing the corrected factor `(3v+1)/(9v)` by the
old erroneous `1/(27v)` makes every one of the six source-row residuals
nonzero in `A`.

The AWS Box02 endpoint completed rc zero in 10.15 seconds with 24,848 KiB
maximum RSS.  Source, dependency, output, metadata, and portable custody
checks are frozen with the case.

This certificate proves only the full-source boundary-local statement in
characteristic 127.  It does **not** prove that the candidate plane curve is
a quotient component, that the eight characteristic-zero formal branches
belong to one component, that components cannot merge in reduction, or any
trajectory/max-12/Jacobian conclusion.  Those global graph and good-reduction
bridges remain charged.
