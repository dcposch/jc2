# V22R1 semantic historical-bridge repair

Date: 2026-08-27

Status: **PREREGISTERED DUAL-AWS REPAIR.**

The V22 V1 mathematical and source contracts remain unchanged, except that
the 35 historical bridges are required to be exact polynomial equalities in
an ordinary Singular ring rather than byte-identical serializations.  The
V1 diagnostic proved that byte identity is too strong: V9 and V22 order the
same terms and factors differently.

R1 must:

1. import the frozen V1 exporter at SHA-256
   `c965726d2308358bf01c533fe89f2e28551abd9e3549fc699cd3e36d40ac82a6`;
2. defer only failures whose exact tag is `old coefficient byte bridge`;
3. require at least one and at most 35 such serialization deferrals, record
   every `(grade,row)`, and leave every other V1 failure fatal;
4. run and pass the existing ordinary-Singular equality tests for all 35
   historical coefficients before validation;
5. retain the dual-field, section, homogeneity, parity, sensitivity, custody,
   resource, and scope contracts of V1 exactly.

The two failed V1 trees are quarantined evidence only.  R1 is a fresh launch
with a new freeze and tag.

