# Frozen custody — Sigray Proposition 4.2 constant-shift repair

Frozen producer:

```text
10bc55d53f9cf9a9e6a4535787f6e208a25f0ebfbd6dbd803f68b00f8ca8f5cd  xmodel/sigray-prop42-constant-shift-repair-sol-ultra-20260828.md
```

Primary source:

```text
9bf9f0320497dd8d5da6d7fe68ec900c1879663e6f11c121853482ca7e1623ae  refs/sigray_full.pdf
```

Printed page custody (the PDF page number equals the printed page number):

- p. 13: Statement 3.7 and Notations 3.9--3.10, finite Laurent expansion,
  leading order, and residual polynomial;
- pp. 18--20: Proposition 4.1, Proposition 4.2, equations (8)--(10), the
  disputed sentence, and integer `delta_j` descent;
- p. 21: Notation 4.1 and Proposition 4.4 tower-prefix typing;
- p. 29: Notation 6.1, the `T_a^nearrow/T_a^searrow` split;
- pp. 39--40: Notation 8.1 and Proposition 8.1, approximate-root degrees and
  `M_F`/`M_F^*`;
- p. 48: Notation 9.1, `Q(F)`;
- pp. 49--50: Proposition 9.2 and Statement 9.5, pole characteristic
  sequences and the `T_a^searrow` budget path.

Reproducible extraction custody for the charged printed proof:

```sh
pdftotext -f 18 -l 21 -layout refs/sigray_full.pdf - | nl -ba
```

In that extraction, Proposition 4.2 is lines 51--151; its statement is
51--71, equation (9) is 94--98, equation (10) is 101--109, the invalid
`l_j != 0` inference is 120--126, and `delta_j` descent is 131--147.
Proposition 4.3 starts at 153, and Proposition 4.4's separate typing starts
at 204.  These line numbers are extraction-local and are recorded only to
make page custody reproducible.

Supporting frozen context read by the producer (not primary authority):

```text
f4964e2fdfef7b3081a3effb0f54eb2cac0f52d34a7c1118ef329ddefc2090d2  ladder/SIGRAY-AUDIT.md
5751fdacd00351b84c4fc14f7203eeca1265bda78f24099441230ed04056fb5b  xmodel/sol-landing1.md
e88ef03a7edbf6128de1e54be7a029e23e776e12422a205f9493b6a52c1d9447  xmodel/sol-gluing-design.md
```

The checker is standard-library exact arithmetic only.  It deliberately
contains the abstract inverse-dependence control `p=q=1`, then mutates `p`
to a nonconstant polynomial to test the load-bearing fiber firewall.

