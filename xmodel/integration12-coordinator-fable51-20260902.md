# INTEGRATION #12 — coordinator binding (Fable 5.1, 2026-09-02)

Basis 872c4f41. Supplements integration #11 (96a4c0b1). Different-model
hostile review satisfied on every PROMOTED item; hashes are the sealed
report files' SHA-256 prefixes as recorded in notes.md.

## A. The all-degree ceiling in invariant form (producer opus ca915761;
## reviewer gpt55 05d59097 — items 2, 3, 5, 6 CONFIRMED with repairs;
## item 1 at lower-bound scope; item 4 at LATTICE-LEDGER scope)

Scope: Keller, noninvertible; H2 where marked; no case split except in
the consequences; case (A) EMPTY (integration #9) and not consumed.
**PROMOTED — the invariant D_min.** D_min(F) := min over Aut(C^2) ×
Aut(C^2) (psi ∘ F ∘ chi) of max(deg G_1, deg G_2). Right composition
fixes A_F, N, a, W, (s_l, mu_l), delta_aff, Gamma, (d, e) and R_0 (Chau
2004) and moves only K = gcd(deg P, deg Q); so D_min = min_psi
[max(d,e) · K_min]. Any "map degree bounded by N" statement is about
D_min; for the raw degree it is FALSE (right composition alone).
**PROMOTED — NEG-GEN at lower-bound scope:** for F_{N,c} = (x, x^c y^N),
geometric degree N, A_F = {u = 0}, n_min = 1, and
ceil((c+N+1)/2) <= D_min(F_{N,c}) <= c + N; the lower bound alone refutes
any general-dominant bound at fixed N; the datum spent is deg Jac
(= N x^c y^{N−1}). NOT promoted: the exact value D_min = c + N.
**PROMOTED — the polar ledger, with definitions:** on the resolution
X → P^2 of the common-degree rational map (boundary base points on
L_infty blown up, X \ L~ = A^2), Z = Phi^* L_infty = D H − sum a_i E_i,
kappa = sum_{C→L_inf} k_C <= N, T = the satellite mass (sum of the
satellite a_i); m_{E_0} = D; N = sum_{C→L_inf} m_C k_C; e_C = m_C for
the L_infty-sheets; the boundary components form a Z-basis of Pic X,
so det = ±1 for EVERY compactification of A^2 (an identity, blind to
forks and chain length); PROP DN (a dicritical has exactly one boundary
neighbour with m > 0, and s_l n = m_{C_l}: D and n are two values of one
polar multiplicity). **DEG-SPLIT** (all dominant F): D = sum_l s_l n +
kappa + T. **CAP-STRICT:** deg A_F-bar <= D − kappa − T <= D − 1
(Chau's cap is never attained; D_min >= n_min + 1; in Chau parameters
K >= S m + 1) — so the (9,6) row admits no degree-9 component at all
(CLAIM [D] strengthened). **NOETHER-K** (Keller, H2; for general
dominant maps an extra affine term Z·R_aff appears): sum a_i = 3D − 2N
− kappa + n(W − S), sum a_i^2 = D^2 − N; at N = 1 these are Noether's
equations for plane Cremona maps. Machine-verified on 41 exactly
resolved maps. Log control: the log ramification formula on
(X, L~ + E-bar) reduces identically to [P3].
**PROMOTED — NO-CEILING[LATTICE-LEDGER]:** no constraint of the form
Z nef, Z^2 = N, proximity/effectivity, I1–I6, DEG-SPLIT, or a
determinant identity can bound D at fixed N (Hodge index gives only
D >= sqrt N; the nef hyperboloid is unbounded in Z·H); two
machine-verified dominant families realise it (D → ∞ with all growth in
T; deg A_F → ∞). NOT promoted as a universal impossibility: a
Keller-specific canonical inequality is exactly what survives.
**PROMOTED — MERIDIAN-FLOOR+:** p(W − S) >= N − 1 with p = min deg_t
l(a,b) <= n − 1, hence n >= ceil((N−1)/(W−S)) + 1 — one unit sharper
than the promoted floor at every cell; at W = 2, n >= N and D_min >=
N + 1; re-derives the Chau lane's n >= 4 at N = 4 from group theory.
**PROMOTED (reviewer's consequence) — OPEN[MF-DEFECT] CLOSED POSITIVE:**
with MF-EXACT (integration #11), MERIDIAN-FLOOR+ gives
2 g_L + theta_inf >= W − S + 1; the equality case g_L = 0, theta_inf = 1
is EXCLUDED. The +1 is banked at every cell.
**PROMOTED — the one-integer reduction:** NOETHER-K is the boundary
shadow of Jac F ∈ C^*, and Z·K_X = sum a_i − 3D = −2N − kappa + n(W − S);
hence Z·K_X <= f(N) ⇒ n <= (3N + f(N))/(W − S) ⇒ delta_aff <= p_a(n):
OPEN[DELTA-AFF-VS-N] is EQUIVALENT to a bound on the anticanonical
defect — **OPEN[ANTICANON-DEFECT]** (bounded quantity: the integer
Z·K_X = deg(branch divisor of Phi, with multiplicity) − 3N). Honest
scope: FALSE in the ambient dominant class (defect up to +7 at N = 3);
the log form Z·(K_X + L~_red) <= 0 is FALSE; the only Keller data are
automorphisms, where −3 is forced by Noether — any proof must use the
Keller condition essentially. Coordinator's adjunction reading
(unreviewed, recorded): Z·K_X = 2 g_L − 2 − N, so the integer is the
genus of the generic pencil member.
**PROMOTED — MOH-CROSS:** Moh 1983 (verified in refs/; normalisation
repaired: no Jacobian counterexample with BOTH coordinate degrees <=
100 after the standard reductions, i.e. max(deg f, deg g) <= 100) gives
D_min >= 101 for every noninvertible Keller map, with no gap to D_min.
Hence ANY proved bound D_min <= C(N) with C(N) <= 100 kills geometric
degree N outright — every case, every W. Price, exact: (B2) at
5 <= N <= 16 and (B3) at 4 <= N <= 8 are both closed by
[ANTICANON-DEFECT with f(N) <= (W − S)·100 − 2N] + [SAT-MASS with
T <= 100 − S n − kappa]; the conditional ceiling n <= 3N alone makes
the (B3) enumeration finite per (N, W) but reaches no (B2) threshold.
RECORDED: OPEN[SAT-MASS] (is T = D − S n − kappa bounded in N for a
degree-minimal representative); OPEN[N-VS-MAPDEG] (upper half) =
OPEN[DELTA-AFF-VS-N] ∧ OPEN[SAT-MASS]; its lower half strengthened to
D_min >= ceil((N−1)/(W−1)) + 2 and to D_min >= 101.

## B. Records (not promoted)

Lanes running at binding: `keller-pencil-genus-opus5-20260902` (the
n-half in genus form, symplectic datum), `sat-mass-opus5-20260902`
(the D-half), `b3-census-deg5-deg6-sol56-20260902`,
`mf-defect-mult-vs-beta-grok46-20260902` (now an independent second
derivation of MF-DEFECT and the owner of MULT-VS-BETA). Drivers
preserved under box/nvm-drivers-20260902.

## C. Standing fronts after this integration

1. **THE PRICE, in one line:** every (B2)/(B3) cell at 4 <= N <= 16 (and
   up to N = 33 with a 3N-shaped ceiling) is closed by two bounds on a
   degree-minimal Keller pair — the anticanonical defect (equivalently
   the genus of the generic pencil member, equivalently deg A_F) and the
   satellite mass — against Moh's D >= 101. No reviewed instrument
   supplies either; both must use Jac F ∈ C^* essentially. Two flagships
   own the two halves.
2. **The (B3) horn:** census at N = 5, 6 with the spine data running;
   the affine cage and the BMY/embedding routes closed by theorem.
3. **(B2):** the floors force delta_aff far above the beta thresholds;
   the beta-route is dead as a mechanism; (B2) dies only with the
   ceiling.
4. **Reducible branch, A2 (untyped), counterexample census:** unchanged
   from #10/#11.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `6746`.
- Body SHA-256:
  `2fdceea11085f5530f832a4215c6ba512e967face15e1a5984be76d2dd20b158`.
- Frozen basis: `872c4f41b254f87bec4045c7434c80d2db3ec237`.
