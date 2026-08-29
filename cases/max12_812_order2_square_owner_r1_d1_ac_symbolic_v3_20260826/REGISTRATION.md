# Registration: `r=1` / symbolic-`d=1` V3 reserved-token repair

Date: 2026-08-26

V2 repaired the etale-root identifier collision, but Singular still parsed
the three long identifiers containing the token `_or` as an operator/type
collision after `primdec.lib` was loaded.  Every mathematical sentinel before
that deployment point and both residue expressions passed in both fields;
the validator rejected the diagnostics.

V3 pins V2 and changes only `D1AC_or15`, `D1AC_or16`, and `D1AC_orient` to
collision-resistant identifiers with no `_or` token.  The exact replacement
count is mandatory.  Mathematical scope and dual-AWS caps are unchanged.

