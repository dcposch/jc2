# V22R1 harvest and custody record

Date: 2026-08-27

Status: **DUAL-AWS PRODUCER PASS; DIFFERENT-MODEL REVIEW PENDING.**

## V1 quarantine and R1 repair

V1 produced no accepted grade-15 export.  Both V1 lanes failed closed at the
first historical V9 byte comparison because two equal polynomials had
different term/factor order.  The exact strings, failed roots, and stderr
hashes are recorded in `V22_V1_SERIALIZATION_BRIDGE_ERRATUM.md` (SHA-256
`caf6261223c8b196d43806112d4d3534e05269c5911a60f92e74921095015d13`).

R1 retained the frozen V1 exporter byte-for-byte at
`c965726d2308358bf01c533fe89f2e28551abd9e3549fc699cd3e36d40ac82a6`,
deferred only the named serialization comparison failures, and required all
35 historical coefficients to pass exact polynomial equality in ordinary
Singular.  Nineteen distinct byte comparisons were deferred in each lane;
all 35 semantic comparisons passed.

R1 freeze manifest SHA-256:

```text
f58db2ff91c83bf3b52357889bb91d01f90dde2770eb0516fc89937f9db6ffb2
```

Shared source archive SHA-256, as recorded independently by both launchers:

```text
4f56f8cf355c54195e452d43826f5693a1e22e1ff6b03d679e2fbfb43a24f54e
```

The transient archive is not retained locally.  Each host's harvested
`freeze_check.stdout` records successful verification of every R1 and nested
V1 freeze entry after extraction.

## Distinct AWS executions

```text
Q:
  host ip-172-30-0-186
  pid 350975
  tag max12_812_order2_p0_total_rees_allrows_g15_export_v22_r1_20260827T031729Z_q
  compiler 49.95 s wall, 43,732 KiB max RSS, 99% CPU, rc=0
  Singular 0.03 s wall, 11,544 KiB max RSS, rc=0

F_65521 serialization/control lane:
  host ip-172-30-0-45
  pid 362464
  tag max12_812_order2_p0_total_rees_allrows_g15_export_v22_r1_20260827T031729Z_p65521
  compiler 49.91 s wall, 44,604 KiB max RSS, 99% CPU, rc=0
  Singular 0.02 s wall, 11,256 KiB max RSS, rc=0
```

The two compiler invocations reconstruct the same sparse polynomial over
exact `Fraction` arithmetic and serialize it differently by characteristic;
they are distinct executions, not independent algebraic derivations.  The
ordinary-Singular controls run in distinct characteristic-zero and
characteristic-65521 rings.  Independent coefficientwise reduction is
recorded below.

## Harvest hashes and completeness

```text
                                      Q                                           F_65521
RESULT.json                           829239c93c9a8bcb34a0428391c378ddd662dbc70cfdd27a6b2cc3b6cdcf00b8  04c777e97b9113da9848c2c47fcfb3d880cc7b11319b74a0030dcc92aa92c94c
EVIDENCE.sha256                       f213026a454c8f3171c0ce3c8b6cdfb6fe1a22e663caec08d47d08666309def9  7e862a38d91ee12913ab35af62ab1ed229f3335a2a375604b03e5ab47dc64d40
compiled/result.json                 ba9cb4f2e30bd570e4231a262fad0a616111f9602ecdd00d61cb19427496c4f0  8e6a66100af7fe5a6981fbd396eeff6d0548c57a368d5c78395fa1143e023ec6
```

After remapping each remote `/source/` prefix to the local repository, all
24/24 listed files in each evidence manifest rehashed exactly.  Each harvested
root contains exactly those 24 files plus its manifest, so there is no
unlisted harvested file.

## Independent local harvest verification

The post-harvest restricted-AST verifier
`verify_harvest_v22r1.py` (SHA-256
`08b4cbabd1260b6c1b7c5b3999908eab3235c5a7114e451614309d62b08794d4`)
parsed the fourteen literal coefficient files without importing producer
code.  Its result
`INDEPENDENT_HARVEST_VERIFICATION.json` (SHA-256
`4a0b1f81a8b74b066b157487f238d01c935a7a1a703b42720a7b3b8898929d85`)
establishes:

- all seven exact-Q supports and every coefficient reduce exactly to their
  harvested F_65521 counterparts, with no disappearing modular term;
- term counts are `133,224,355,140,585,200,759` in both serializations;
- every monomial has literal sigma-weight 15 and even rho exponent;
- `CS0` and `Z00` give zero in all seven rows;
- `A00` leaves only `Tg15_6=-1/16`;
- `A10` leaves `Tg15_3=-1/16`, `Tg15_5=-(3/32)rho^2`, and
  `Tg15_7=-(3/128)rho^4`.

This verifier is an independent parser/evaluator of the exported bytes, not
an independent reconstruction of the 569-tail source model.

## Producer-level conclusion and firewall

The harvested artefacts support the seven full literal grade-15 polynomials
of the frozen actual-total source model.  Grade 15 is the first source grade
that breaks the `A00` and `A10` named points, while this finite source remains
identically zero on `CS0` and `Z00` at every depth by the separately reviewed
V21 theorem.

This is still producer-tier until a different model completes hostile review.
Even after review it is a statement about the frozen seven-row source and
four named point evaluations.  It does not by itself certify a `J2` chart,
the unwritten Rees equations, a full formal arc, Gate T, order two, maximum
twelve, or JC2.
