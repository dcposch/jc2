# Source-typing lane: the dicritical hypotheses (D1)--(D4)

You are a bounded source-audit research lane. A hostile review found that
the campaign's rank-four component bound `m<=3` rests on an untyped bridge
between Chau's dicritical *series* and Orevkov's dicritical *lines*. Your
job is to type that bridge exactly from primary sources, or show it fails.
Do not edit canonical ledgers, any charged file, or inspect `jc2-lean`.

charged_input=xmodel/block-descent-a1-rank4-reducible-component-tree-ledger-hostile-review-sol56-20260831.md

Your charged input is a frozen read-only copy in `{{LANE_INPUTS}}`; verify
its SHA-256 first and stop on mismatch:

```text
ed0d288bec800bc1cfb59506a60ac76243aa47378692330f54f9d0860d754fb9  {{LANE_INPUTS}}/block-descent-a1-rank4-reducible-component-tree-ledger-hostile-review-sol56-20260831.md
```

Its §5 states the four hypotheses to type, for a Keller map `F` of
geometric degree `N` with nonproper-value curve `A_F`:

```text
(D1) every Orevkov dicritical l in L_F has one irreducible nonconstant image alpha(l);
(D2) alpha: L_F -> Irr(A_F) is surjective;
(D3) mu_l is a positive integer for every such l;
(D4) N-1 = sum_l (mu_l + corr_l), with every corr_l >= 0.
```

Task, in order:

1. Obtain the primary sources: Orevkov's 1987 paper containing the
   degree-at-infinity identity the campaign cites as "Orevkov Lemma 4.2"
   (with Chau 1999 Remark 4.9 as the secondary restatement), and
   Le Van Thanh--Chau / Chau 2004 containing "Lemma 1" (dicritical images
   cover `A_F`) and "Corollary 2" (one set-theoretic point at infinity).
   Fetch exact texts (arXiv, journal scans); record URL, hash or exact
   bibliographic identification, and quote the exact statements verbatim
   with their hypotheses. If a source is unobtainable, say so explicitly —
   never reconstruct a statement from memory and present it as sourced.
2. For each of (D1)--(D4), give a verdict `SOURCED` (with the exact quoted
   statement and a proof of the campaign form from it), `DERIVED` (proved
   by you from sourced statements, proof included), or `UNSOURCED` (with
   the precise gap). Pay attention to: the definition of a dicritical line
   versus a dicritical series/branch; whether `mu_l` in the source is
   defined so that `mu_l >= 1` for dicriticals (or can vanish); whether
   the identity's correction terms are proved nonnegative; and whether
   the sum ranges over exactly the dicritical lines.
3. Address the reviewer's specific attack: can a realizing line have
   `mu_l = 0`? Either exclude it from the sourced definitions or exhibit
   the failure mode.
4. State the exact resulting theorem: under the sourced/derived subset of
   (D1)--(D4), what bound on `#Irr(A_F)` (hence on `m` for a branch
   subcurve) follows at geometric degree `N`, and what remains open.
5. Separately verify the companion-sheet floor `f(B_i) >= 1` used by the
   conditional Lemma 2.3 summation: locate its promoted source in the
   campaign ledgers (the reviewer says it is used but unlisted), and
   state it as an explicit consumed hypothesis.

Computation rules: reading, exact quotation, and desk-scale proof only.
Never run Singular, msolve, any CAS, or any computation of uncertain
duration or memory on this machine.

Write one report and no other file:

```text
xmodel/block-descent-a1-rank4-dicritical-typing-d1-d4-grok46-20260831.md
```

Create the report file with a skeleton of section headers as your first
action and append each completed section as you finish it. Keep it under
roughly 6,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line. Do
not include a `charge_basis` declaration: this lane asserts no new exit
price.
