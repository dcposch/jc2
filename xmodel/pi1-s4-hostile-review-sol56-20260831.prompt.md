# Hostile review: PI1-S4 decision report (Opus) — is the Main Theorem sound?

You are the different-model promotion gate for the claimed closure of
the rank-four residual on the coprime stratum. The charged report
proves: Theorem A (literature-free: braid at infinity `delta^n`,
Hurwitz-fixedness forces `Pi^n=1`, sign and orbit constraints, `n>=3`,
divisibility splits); Theorem B (Nori 3.27 on the blow-up at infinity;
inequality `C'^2 = nd > (n-1)(d-1)` identically); Theorem C
(nodalization in `P_{d,n}` transports the representation through a
nearby nodal curve); MAIN THEOREM: NO to PI1-S4 whenever
`gcd(deg p, deg q)=1`. Default to refutation.

charged_input=xmodel/pi1-s4-decision-opus5-20260831.md
charged_input=xmodel/block-descent-a1-b0-coordinator-integration-fable5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
010330d208c5899ce41832f1187b73d9a63268725d809b0370f2b4d9cd66eadd  {{LANE_INPUTS}}/pi1-s4-decision-opus5-20260831.md
bbd48de1b028f6c71f006c3f27c10a3b96c593e6da58088c8393a992bde4a963  {{LANE_INPUTS}}/block-descent-a1-b0-coordinator-integration-fable5-20260831.md
```

Verify line-by-line (CONFIRMED/REFUTED/GAP per item):

1. §1 normalization: the WLOG `d>n` shear/swap; `deg D = d`;
   properness of the vertical projection; the `(a,b)=(d-n,d)` place
   data; the genus identity (G); Riemann-Hurwitz count (V)=d-1 —
   including whether "gamma is an immersion everywhere" really follows
   from the smooth-branches hypothesis; and (A) via H_1 = Z.
2. §2 local braids: the vertical-tangency relation (T); the
   `A_{2k-1}` local braid `sigma^{2k}` and the single relation
   (N_k); the disjointness verdict (disjoint transpositions satisfy
   the FULL nodal commutation, hence all (N_k)); and the ZvK
   presentation with NO extra relation at infinity (the report cites
   properness — is that right for `C^2-D` vs `P^2-Dbar`?).
3. §3 Theorem A: the Hurwitz-action framework; the identification
   `rho_infty = delta^n` up to conjugacy on the coprime stratum
   (single Puiseux cycle, first-order separation — is the torus-knot
   claim airtight, and is conjugacy in B_d enough given the Hurwitz
   argument only uses fixedness and the product?); the exponent-sum
   cross-check; the delta-action formula (re-derive at d=3,4); parts
   (1),(2),(3) including the bi-infinite-sequence argument and the
   orbit enumeration over S_4 elements.
4. §4 Theorem B: the two Nori statements as quoted (re-fetch
   nori_ens1983.pdf from Numdam, verify hash
   1b848c19dcaaa016ff8070a7843cfd89db70cbbec3ce13cd9de080074739cc45
   and the page-331 statement verbatim); the blow-up bookkeeping in
   Lemma 4.4 (Euclidean recursion for M and N; the seven checked
   sequences; the case a=1); Lemma 4.3's algebra; whether Prop 3.27's
   hypotheses are FULLY satisfied on X' (transversality of C' and
   B_infty; nodal C'; irreducibility; and the `C^2>2r` per irreducible
   curve IN D_Nori — D_Nori=C' only, or must the exceptional curves be
   audited?; also E=B_infty is a normal-crossings reducible divisor —
   does 3.27 permit that E?); and the simply-connected endgame.
5. §5 Theorem C — the subtlest: Lemma 5.3 (delta_infty constant on
   P_{d,n}); Lemma 5.4's codimension count (are (i)-(iii) really
   independent conditions, and is 'generic member nodal' licensed at
   this level of detail?); Lemma 5.5 (conservation of double-point
   length); Lemma 5.6 (braid comparison — the tube argument, the
   B_2-abelian collapse, and the claimed presentation (*): is the
   quotient direction RIGHT? phi kills the added relators, so phi
   factors through pi_1(C^2-D_t) — check the map direction against
   Zariski's specialisation principle as invoked); and whether the
   final contradiction is complete.
6. §6 scope discipline: the report claims NO on (C1) but explicitly
   does NOT discharge (C1) for the campaign's D_1 — confirm that
   caveat is respected everywhere, and confirm the three
   (C1)-independent gains (Theorem A; the §2 verdict; Lemma 4.3
   reduction) are correctly scoped.
7. §9 residual typing: (M-INF) equivalence via Lemma 4.3; the worked
   (4,2) example; the (ii-a)/(ii-b) fork; and the §9 successor
   hypothesis being correctly typed as NOT a result.

End with promotion recommendation per theorem, exact scopes, and any
corrected statements.

Desk-scale exact reasoning only; you may fetch and hash primary
literature (record exact sources); never run any CAS or computation of
uncertain duration on this machine. Do not edit canonical ledgers, any
charged file, or inspect `jc2-lean`. 4 hours hard budget.

Write one report and no other file:

```text
xmodel/pi1-s4-hostile-review-sol56-20260831.md
```

Create the report file with a skeleton of section headers as your very
first action and append each completed section as you finish it. Keep
it under roughly 6,000 words. End its body with a single standalone
`<!-- BODY-END -->` line and write absolutely nothing after that line.
Do not include a `charge_basis` declaration.
