# Research lane: COMPANION-CURVE-ALLN — the reducible-branch contradiction (Path-2 flagship)

DC directive (standing): the campaign optimizes for RESOLVING JC2;
this lane is one of the two endorsed all-degree critical paths.

Context. In the reducible-A_F branch, the charged REP-96 §7 (R3-R4)
found at the N=4 profile (core (2,1,0), W=(1,2), b=1 branched
component by (RC2)): the block-free (M') identity
sum_i a^(i) chi_c(D_i \ Sing D) + sum_p a_p = 1 - d*chi_c(V)
collapses to chi_2 + sigma_2 = 1 — the branched component's node
count s_1 CANCELS IDENTICALLY, and (M') constrains ONLY the
companion component D_2: rational (normalization A^1), degree >= 2
(Lemma NL), meeting D_1 transversally. The budget DEMANDS this
companion exist. The charged CAGE-N-R2 (confirmed by review)
gives the general-N reducible cage; (RC2) forces b=1 at N=4,5.

Task, flagship effort — turn the forced companion into an
all-degree contradiction, or characterize the survivors:
(1) GENERALIZE THE COLLAPSE: run the block-free (M') at general N
    on the cage's residual profiles (charged CAGE-N-R2 report;
    W-vectors and a^(i) = N - W_i). Determine: does the branched
    component's singularity data always cancel? What does (M')
    force on the companion(s) at each N — genus, chi, node count,
    crossing count j with D_1? Derive the general-N analogue of
    chi_2 + sigma_2 = 1 exactly, per profile.
(2) EXISTENCE PRESSURE ON THE COMPANION: the companion is a
    trivial-dicritical image component of weight W_2 with
    a^(2) = N - W_2 fixed generic meridian count, rational, with
    prescribed transversal crossings of D_1 and prescribed
    behavior at infinity (it is a component of the Jelonek set of
    a Keller map — use the charged cage's constraints on A_F
    components: degrees, weights, Newton data). Attack: Bezout /
    genus-degree / log-Chern or BMY-type inequalities / the
    Zaidenberg-Lin-style rational-curve constraints — does a
    rational companion with the forced data exist for ANY N? If a
    known family realizes the data at some N, EXHIBIT it (that is
    a survivor, not a failure); if the data is contradictory for
    all N >= some N_0, prove it and state N_0 exactly.
(3) INTERFACE WITH THE (9,6,2) SUBSTRATE: the realized (9,6,2)
    curve is a candidate D_1 at N=4 whose companion D_2 must
    satisfy chi_2 + sigma_2 = 1, deg >= 2, and the crossing data
    j from (M')'s a_p census (a_p = 1 at transverse D_1-D_2
    points). Instantiate YOUR general machinery at this concrete
    case: what is the complete forced datum of D_2, and is there
    a finite-dimensional family to search? Specify the exact
    Groebner/qqideal job that would decide D_2's existence (the
    coordinator can run it on AWS immediately; msolve 0.10.1 +
    qqideal are live).
(4) Typed verdict block + OPENs + deviations. Hostile standard.
    Do NOT conflate the two b symbols (dicritical-count b vs
    branched-component b — REP-96 §7 R3 keeps them apart; so
    must you).

Report: `xmodel/companion-curve-alln-opus5-20260902.md`.
Seal-at-completion contract: skeleton WITHOUT the marker, bounded
per-section writes (<1500 words each), seal only at completion.
Target 25-35KB.
charged_input=xmodel/rep-96-inner-opus5-20260901.md
charged_input=xmodel/reducible-all-n-r2-opus5-20260901.md
charged_input=xmodel/b0-reducible-n5-opus5-20260831.md

Your inputs are frozen read-only copies in `{{LANE_INPUTS}}`;
verify these SHA-256 hashes first and stop on mismatch:

```text
a47945ab0fdb8e8245f2ec03558eaafc0cab9b64bd4bbcd2c859afb370db2401  {{LANE_INPUTS}}/rep-96-inner-opus5-20260901.md
bdd857c9d8c55fa000fcffee05f9f3084c5d073fb4d06285edf2af0d3c369339  {{LANE_INPUTS}}/reducible-all-n-r2-opus5-20260901.md
48d417d6980e52d61550a733f0dcded7d26a0c4e127677ac73bd544a8a00713b  {{LANE_INPUTS}}/b0-reducible-n5-opus5-20260831.md
```
