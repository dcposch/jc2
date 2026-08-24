# Hostile different-model review — AS map-only `p=3,D=7` triangular terminal

You are the independent different-model hostile reviewer. Work in
`/Users/dc/code/math/jc2` at committed basis
`1e60fcedc8626650c7c7544ad296c3624173415f`. Read in full:

- `xmodel/as-fonly-p3-d7-depth6-triangular-terminal-20260824.md`;
- every payload in
  `cases/as_fonly_p3_d7_depth6_triangular_terminal_20260824/MANIFEST.sha256`;
- the relevant canonical AS map-only definitions and prior reviewed gates
  named by those files.

Frozen hashes:

- producer report:
  `5325890a505489570a6e02409d64e026560d2635ddf989b865039eeb6ecddccb`;
- freeze / manifest:
  `b51a00062fa38765d3dd4199919b4e1a812fddbd8ae12cca9cc4fa2380b776bb` /
  `c722e0a6fef62a31d431b2b331f886bc4ab05726a75a9b5694fcc166bc99afce`;
- README:
  `fff751fef07cef4eaa093b3dbcb27250a5db33c7e9ac4e889c3981a1448367a8`;
- compiler / direct replay / accepted-digit replay / Singular audit:
  `dcd2ea308ff31813cb55a88904ddbd375471a7cb92f6d7a2ffb370f1fee5acaa` /
  `17287308e709adc0579fdaf6853e947b4ec3de136433d5bcbbbc71da0aee4fdc` /
  `cd35cc79d927e04161c9a9adf0f973f6583677290c79884956259395601baf51` /
  `86398ebcf209d1ba588c0e86ec280db7ee4ac7d7013f0a6bed859dfdc8b4a5c5`.

Verify the manifest and rerun all registered programs from the case
directory. `Singular -q` may need an explicit `exit;` after the file. These
are regressions only, not independent evidence. Then reconstruct and attack:

1. **Literal point.** Expand over the integers
   `P=x+2x^3+441x^5+108x^7` and
   `Q=y-6x^2y+18x^4y-27x^6y`. Verify total degrees seven, special fibre
   `(x-x^3,y)` over `F3`, and `det J(P,Q)=1 mod 729`. Record the complete
   literal integer determinant, not just a convenient modular derivative.
   Check specifically that its quotient by 729 modulo three is
   `x^6-x^12`; the removable `x^6` term must not be silently erased.
2. **Clean representative.** Replace the `x^7` coefficient by `1566`, which
   is congruent to `108 mod 729`, and independently prove
   `det J(P_tilde,Q)=1-729*x^12 mod 2187`. Explain why changing the integer
   representative is legitimate and how it changes the residual by a
   divergence. Reject any false literal equality for the original integer
   representative.
3. **Triangular equivalence.** Starting from
   `P_x=1+3a(x)`, `Q=yT(x)+S(x)`, derive the irrelevance of `S`, the exact
   derivative-provenance restrictions `[x^2]a=-1` and `[x^5]a=0 mod 3`, and
   no others. Derive denominator-free inversion through modulus 729 and prove
   that `deg T<=6` is equivalent to the high-degree vanishing of
   `H(a)=a^2-3a^3+9a^4-27a^5 mod 81`. Check all modular truncations and cap
   inequalities.
4. **Accepted-digit recursion.** Independently derive the 27 base forms and
   the affine carry rule
   `H(a+3^r delta)/3^r = H(a)/3^r+2a0 delta mod 3` in each actually used
   digit range. Rebuild deterministic RREF/nullspace enumeration or supply an
   independent exhaustive computation. Verify the counts
   `27 -> 3645 -> 531441`, the `1458` second-stage inconsistencies, and that
   the first terminal-stage survivor appears after 486 inconsistencies with
   `a=2x^2+6x^4+9x^6 mod 81`. Audit whether stopping at the first survivor is
   correctly described as existence rather than locus exhaustion.
5. **Integration and source honesty.** Verify that the displayed `a` gives
   `T=1-6x^2+18x^4-27x^6 mod 729`, and that integration to the displayed `P`
   uses only licensed modular divisions, including the derivative-multiplier
   strata at exponents divisible by three. Check that this is the map-only
   system and imposes no hidden cap on an `(A,B)` gauge.
6. **Terminality.** For every same-residue cap-seven lift
   `P_new=P_tilde+729U`, `Q_new=Q+729V`, independently linearize the
   determinant modulo 2187 and obtain
   `-x^12+U_x+V_y mod 3`. Prove that derivatives of total-degree-at-most-seven
   polynomials have degree at most six and therefore cannot cancel `x^12`.
   Test whether mixed terms, Frobenius-zero derivatives, target shears, or a
   different depth-six representative evade the obstruction.
7. **Scope.** Determine the exact supported statement: one D7 map-only point
   exists modulo `3^6` and its residue has no D7 lift modulo `3^7`. Do not
   permit an inference to emptiness of the full D7 locus, a simultaneous
   gauge-cap theorem, an all-depth tower, a characteristic-zero lift or
   no-lift theorem, a counterexample, or JC2. State the smallest next exact
   obligation for a full D7 decision.

Use exact arithmetic and independent derivations; replay plus prose
comparison is insufficient. Do not edit producer, case, canonical, ladder,
notes, prompt, log, run, or erratum files; do not launch AWS. Keep scratch
outside tracked paths. Write exactly one report:

`xmodel/as-fonly-p3-d7-depth6-triangular-terminal-review-grok-20260824.md`

Give `CONFIRMED`, `REFUTED`, or `GAP` overall and per numbered claim. Include
hashes, explicit determinant calculations, the smallest failing identity if
any, exact promotion language, and quarantine language at both ends.
