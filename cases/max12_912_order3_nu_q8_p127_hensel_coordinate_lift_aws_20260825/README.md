# Q8 degree-190 coordinate Hensel lift over `F_127`

This producer lifts the exact `w=25` lex-shape algebra through the candidate
monic relation `H(w,v)` without recomputing a generic Groebner basis.

It works in the fixed finite etale algebra

```text
B0 = F_127[a]/(H(25,a))
```

and in its truncated power-series thickening

```text
B0[s]/(s^N),  s=w-25.
```

The generator first proves that the six-by-six Jacobian of the six divided
quotient rows is a unit in `B0`.  Newton iteration then lifts simultaneously:

- the root `v(s)` of `H(25+s,v)` with `v(0)=a`;
- the six true-centre coordinates `(c,d2,d4,x1,x3,x5)`;
- the localization inverse.

The endpoint requires all six original quotient rows, `H`, the defining
`v` relation, and the localizer to vanish modulo `(s^N,H(25,a))`.

This is a formal local reconstruction only.  It does not by itself prove
that the series are rational, that the candidate is a global component, or
that any characteristic-zero components cannot merge modulo 127.  Those are
separate exact gates.

All substantive runs are AWS-only.

