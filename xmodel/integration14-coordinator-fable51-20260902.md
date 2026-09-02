# INTEGRATION #14 — coordinator binding (Fable 5.1, 2026-09-02)

Basis 6557a4ad. Supplements integration #13 (7f6a1917) and its deltas
(a) (CH2 vacuous for minimal counterexamples, producer-level) and (b)
(the reviewed scope). Different-model hostile review satisfied on every
PROMOTED item; hashes are the sealed report files' SHA-256 prefixes as
recorded in notes.md.

## A. The shape of the boundary tree of a minimal Jacobian pair
## (producer opus 7b0ffec7; reviewer gpt55 b1e09351)

**PROMOTED — THEOREM FIRST-FORK** (wording repair: it counts REDUCED
points at infinity; tangency to L_infty lengthens the chain above one
reduced point without splitting the neighbour): for any dominant F,
the valency of E_0 in the boundary tree and in the polar subtree T_+
(when nu >= 2) equals nu = the number of reduced points at infinity of
the generic pencil member = the number of distinct roots of the top
form of the max-degree coordinate; E_0 is a leaf iff nu = 1 and a fork
iff nu >= 3 (then Psi >= D). Six-map replay reproduces val(E_0) = nu.
**PROMOTED — (LF) and (MIN):** for a Jacobian pair that is a
counterexample, l(P) = alpha H^d, l(Q) = beta H^e with gcd(d,e) = 1,
deg H = K = gcd(deg P, deg Q); at a degree-minimal representative
d, e >= 2, d ≠ e, D = K·max(d,e) >= 3K.
**PROMOTED — the SUBRECTANGULAR normal form, in GGV's scope:** a
GGV-minimal counterexample (minimal gcd over all counterexamples)
admits a degree-preserving subrectangular gauge in which the top form
is a monomial x^u y^v with u, v >= 1, so nu = 2: E_0 is a FREE vertex of
the polar tree — never a leaf, never a fork; T = T_class there. The
bridge from Aut × Aut orbit-minimality of an arbitrary counterexample
to GGV minimality is OPEN[SUBRECT-ORBIT-BRIDGE].
**PROMOTED — THEOREM E0-LEAF-CAP** (no Keller): Psi = 0 and E_0 a leaf
⇒ D <= N + 1 − 2 g_L; hence integration #13's CH2, in ANY gauge, together
with Moh's floor would kill every N <= 99 — CH2's hypothesis is the
theorem, not a lemma. **Binding consequence:** CH2's hypothesis is
FALSE for GGV-minimal counterexamples; at N = 4 it is refuted
unconditionally by `polar-chain-n4-grok46-20260902` (Psi = 0 and E_0 a
leaf jointly impossible: 7 >= 2n + kappa >= 9; the polar tree of the
(mu, corr) = (2,1) profile forks, with 1 or 2 spine-forks on DO's six
graphs, and DO kills all six by transfer-determinant identities, not by
Psi > 0). CH1 (Psi = 0) fails already for automorphisms ((x, y + x^k):
Psi = k = D). Neither CH1 nor CH2 is a kill; the nine N = 2W cells stay
OPEN.
**PROMOTED — the sharpened Moh floor:** D_min = K·max(d,e) with K >= 16
(GGV Cor 6.6, verified in refs/) and max(d,e) >= 3, so D_min >= 102 for
every noninvertible Keller map and D_min has a divisor K with
16 <= K <= D_min/3 (which excludes 101, 103, 106, 107, 109, 113, 118 in
[101, 120]; Moh's surviving degree pairs have exactly this shape).
**RETYPED — the satellite price is ONE-WAY:** T_ext <= tau on a
degree-minimal representative in an H2 cell with one dicritical
(W <= 3) gives D_min <= 2(tau + N) (HALF-CAP + DEG-SPLIT), so
tau <= 50 − N contradicts Moh; the converse is refuted. The producer's
own floor T >= D_min/2 − kappa >= 51 − N sits one unit above the target.
Newton-polygon theory leaves T free: T is the continuant data of the
satellite chains — the PUISEUX CHARACTERISTIC at infinity — and GGV's
corner theory constrains only the first corner (u >= 4, v <= u(u − 1),
u + v >= 16).

## B. Records (not promoted)

`sing-witness-gpt55-20260902` (34f9b423): a non-Keller, non-étale
witness at N = 6 with singular A_F (cusp U^2 = V^{2k+1}) and g_L → ∞;
the bounded-pair version is moot by MF-EXACT (bounded n ⇔ bounded g_L
at fixed (W, S)); the datum a ceiling must bound is the cusp TYPE.
`polar-chain-n4-grok46-20260902` (64a4ebd6): OPEN[POLAR-CHAIN] at N = 4
answered NO (see §A). `mf-rational-grok46-20260902` (9454c3e9): g_L = 0 is
numerically empty at N = 2 and open for N >= 3 (MF-RH-EXIST). The (B3)
census at N = 5, 6 (`b3-census-deg5-deg6-sol56-20260902`, 4ad3e221):
exact counts; no legal pruning before a general-N assembly theorem;
demoted. Lanes running at binding: `depth-ceiling-opus5-20260902` (the
Puiseux depth: Moh's recursion versus N), `keller-cluster-census-
codegen-sol56-20260902`.

## C. The binding reading of the day (integrations #9–#14)

Under H2 the residual is (B2) ∪ (B3) below N = 17 (case (A) EMPTY at
every N). Every instrument built today — the cusp/homology cage, the
source curve E, the Domrina–Orevkov boundary package at general N, the
exact meridian floor, the polar ledger with the Noether equations for
degree-N maps, the pencil genus / fork mass, the satellite mass —
yields FLOORS, all exact and priced against Moh's D >= 101 (now 102);
the two conditional ceilings proposed today (CH1, CH2) are refuted or
vacuous; no lattice, homology, profile or Noether-equation instrument
can bound the degree at fixed N (NO-CEILING[LATTICE-LEDGER],
NEG-GENUS, PROFILE-WITNESS, LEDGER-BLIND, the NOETHER-K correction).
The remaining question is exactly the Puiseux depth at infinity of a
degree-minimal Jacobian pair — the same object as the GGV corner
theory's "next pair" (APPROACHES row 1, the campaign's origin) — and
the only place the Jacobian condition can still enter is the structure
of the leading forms at depth, not any ledger identity.

## D. Standing fronts after this integration

1. The depth (`depth-ceiling`): Moh's recursion versus N — either a
   bound T <= tau(N) or the exact free datum, and whether N enters the
   recursion at all.
2. OPEN[SUBRECT-ORBIT-BRIDGE]; OPEN[FORK-MASS] (= ANTICANON-DEFECT);
   OPEN[SAT-MASS] (= the ceiling at W <= 3).
3. The reducible branch and the counterexample census — unchanged;
   the Keller-cluster census instrument in build.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `5837`.
- Body SHA-256:
  `b2e5844f040ea60ec2e5e5d674c19a85e204e3786862f663c4a15b8665e4e8c4`.
- Frozen basis: `6557a4ad6a9d0cbe8fba9394e3371b938235a56f`.
