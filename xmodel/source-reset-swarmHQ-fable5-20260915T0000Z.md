# Independent actual-source strategy challenge — swarmHQ Fable5.1, 2026-09-15T0000Z

Lane: source-reset-swarmHQ-fable5-20260915T0000Z. Evidence MANUAL strategy,
lifecycle UNPROMOTED. No theorem promotion, no computation, no charge_basis
(no exit price is asserted; receipt status ABSENT is expected).

## 0. Frozen inputs (pre-read hashes, sha256, /tmp/jc2-lane.TAuQGA/inputs)

| basename | bytes | sha256 |
|---|---|---|
| APPROACHES.md | 109042 | 6ccccdc25b8e983e9a5de86aabfb4e87db8f872cec5a1acf74ed8af37e41829e |
| COORDINATION.md | 41171 | 4ce5b29af5a70e096a04b942cb978b1df425f9f0648decb720ec1f089ff37ac4 |
| FALLACY-v2.md | 1985 | e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5 |
| README.md (team/swarmHQ) | 17173 | 50cf45483cddf637e717ddfa2d136be4df074d13d360b851c1fb62a9e73edb0a |
| STATE.md | 2394 | 095939d1ef012eaccf2a9d2e9d02d936d6d7e284ae3600d83c358f3c120b1472 |

Scope: all five read whole (851+694+36+273+40 lines) by explicit basename;
no other file, ledger, log, peer report, archive or network source was read.
Post-read hashes are recorded in the final section.

## 1. Verdict

**NO_NEW_CLOSING_TEST.** Best candidate found: the noncommutative
Heisenberg-pair (Dixmier-1) construction, which is a genuinely sufficient
counterexample construction via the one-way transfer JC_2 => DC_1
(Tsuchimoto; Belov-Kanel--Kontsevich; recollection, primary text not in
this readset). Its two cheapest first tests collapse onto gaps already
recorded in the frozen map: (a) the leading-form obstruction
p_m^n = c q_n^m of APPROACHES section 8 (Zhang/Pissolato screen), and
(b) the JC2-equivalent local-nilpotence / surjective-derivation
reformulation (GMM 1211.0744 Cor. 2.4, Regeta 1311.0232, Beldiev--Pogudin
stop). It offers no proof-direction path (no converse DC_1 => JC_2 is
known) and no cheaper counterexample search (a DC_1 counterexample is a
strict specialisation of a JC_2 one). Recommendation: stop; no lane.

## 2. Object, rings, hypotheses

Source ring: the first Weyl algebra A_1 = C<x,d>/(dx - xd - 1) with the
Bernstein filtration by total degree in x,d; gr A_1 = C[x,xi] with Poisson
bracket {xi,x} = 1. Object: a pair (P,Q) in A_1 with [Q,P] = 1, equivalently
the algebra endomorphism phi: x -> P, d -> Q (injective because A_1 is
simple). Hypothesis of a counterexample: phi is not surjective, i.e. the
subalgebra C<P,Q> is a proper subalgebra of A_1 (Dixmier conjecture DC_1
false). Transfer rings: A_{1,p} = A_1 (x) F_p, centre Z_p = F_p[x^p,d^p], a
polynomial ring in two variables; the ultraproduct field K = prod F_p-bar / U
of characteristic zero; the target is an actual Keller pair over K, hence
(Lefschetz) over C. No degree, support or shape hypothesis is imposed.

## 3. Missing global implication and dependencies

Literal path to JC2 (counterexample direction only):
(P,Q) non-surjective  =>  phi_p preserves Z_p and restricts to a Poisson
(Jacobian 1) endomorphism F_p of A^2_{F_p} of degree <= deg phi  =>
ultraproduct gives a Keller pair F over K of bounded degree  =>  if F were
invertible with bounded inverse degree for almost all p, invertibility of
phi follows; so JC_2 true forces DC_1 true, and a non-surjective pair is a
JC_2 counterexample. Dependencies, all external and unread here: (D1) the
centre-preservation lemma phi_p(Z_p) in Z_p; (D2) the Poisson/Jacobian-1
property of the restriction; (D3) the descent of invertibility from the
centre maps to phi (BKK). What the route does NOT supply: any converse
(only DC_n => JC_n is known, so DC_1 is weaker than JC_2 and proving it
closes nothing); and existence of any non-surjective pair. The missing
implication for the campaign is therefore not on this route at all: it is
the same as before, an actual Keller source with mapping degree >= 2, now
asked for inside the strictly smaller Weyl-liftable class.

## 4. First discriminator, attempted derivation, outcomes, cost

**Discriminator A (leading symbols), performed here at zero cost.** Let
m = deg_B P, n = deg_B Q and p = sigma_m(P), q = sigma_n(Q) in C[x,xi] the
Bernstein principal symbols. The commutator [Q,P] has Bernstein degree
<= m+n-2 and its degree-(m+n-2) symbol is the Poisson bracket {q,p}. If
m+n > 2, then [Q,P] = 1 forces {q,p} = 0. For homogeneous p,q of positive
degrees this forces q^m = c p^n, c in C^*: the degree-zero rational
function r = q^m/p^n is a function of t = x/xi, and dr ^ dp = 0 with
dt ^ dp = m xi^{m-1} p~(t) dt ^ dxi != 0 gives r constant. Hence p and q
are powers of one homogeneous form, with the common projective zero and
the gcd(m,n) structure. This is verbatim the leading-form obstruction the
frozen APPROACHES already records for Keller pairs ("J(p_m,q_n)=0 gives
p_m^n=c*q_n^m, hence a common projective zero"), and the shape ledger
(GGV gcd >= 16, degree dichotomy) has a published Dixmier twin
(GGV, "The Dixmier conjecture and the shape of possible counterexamples",
recollection, unverified). Outcome: the test excludes nothing not already
excluded; it cannot separate the Weyl construction from the commutative
one. Cost: none.

**Discriminator B (local nilpotence), performed here at zero cost.** ad(x)
is locally nilpotent on A_1, so ad(P) is locally nilpotent on the image
phi(A_1). If ad(P) were locally nilpotent on all of A_1, Dixmier's
strictly-nilpotent theorem (recollection: such P is Aut(A_1)-conjugate to
h(x) in C[x]) gives P = sigma(h(x)); then [sigma^{-1}Q, h(x)] = 1 forces
h' constant, so phi is an automorphism. A counterexample therefore needs
ad(P) locally nilpotent on phi(A_1) but not on A_1. Under the mod-p
centre reduction this is exactly the statement that the Hamiltonian
derivation {f,.} of a Keller pair is locally nilpotent on C[f,g] but not
on C[x,y], i.e. the recorded JC2-equivalent surjective-derivation /
local-finiteness reformulation (APPROACHES section 8: GMM Cor. 2.4,
Regeta, Beldiev--Pogudin, Rentschler-type slice argument). Outcome: the
second test lands on a recorded JC2-equivalent gap. Cost: none.

**Discriminator C (noncommutative properness), not cheaper.** The Weyl
twin of finiteness of C[x,y] over C[f,g] is "A_1 finitely generated as a
left phi(A_1)-module". Deciding it for an arbitrary pair is DC_1 itself;
no known simple-ring argument (injectivity, simplicity of phi(A_1))
supplies it. Expected cost of an honest construction search: at least the
commutative one, since the Weyl-liftable class is a proper subclass and
carries the same shape constraints plus [Q,P] = 1 in every lower band.

## 5. Strongest actual-source objection; tier label; recommendation

**Objection.** The route touches an actual Keller pair only after two
external theorems (D1, D2) and an ultraproduct transfer, and both of its
cheapest tests are literal duplicates of recorded stops. Its only
non-duplicate content is the one-way implication not-DC_1 => not-JC_2,
which is external, unread in this lane, and useless for a proof of JC2.
A Weyl-side lane would reproduce the counterexample-side shape analysis
in a harder ring and rediscover the local-finiteness equivalence: the
exact failure mode this challenge names.

**Tier at the frozen-readset level.** KNOWN (literature) and DUPLICATE
(both first tests). The five snapshots mention Bass/Weyl operators, the
Kummer full-Weyl control and Long's rank-two Poisson counterexample (the
four-variable analogue), but not the DC_1 sufficient construction; the
46-avenue master inventory was not in the readset, so no NEW label is
claimable and none is claimed. No SCOPE-CONFLICT with any recorded closure.

**Recommendation.** stop: do not open a Weyl/Dixmier construction lane;
continue the parked state; ROOT may record the pointer after the
inventory check in section 6. No promotion, computation or successor.

## 6. OPENs, collision check, post-read hashes

### OPENS RAISED

- OPEN[DC1-INVENTORY-STATUS]. QUANTITY: decide whether N_inv = 0 or
  N_inv >= 1, where N_inv is the number of rows of the 46-avenue master
  inventory (history/APPROACHES-before-20260906-cleanup.md, master union
  table) that already name the Dixmier-1 / Weyl Heisenberg-pair sufficient
  construction or the Tsuchimoto/BKK transfer. CHEAPEST TEST: ROOT text
  grep of that table for Dixmier, Weyl, Heisenberg, Tsuchimoto, Belov,
  Kontsevich; 5 minutes; no compute; outcome only changes the KNOWN label
  to KNOWN/INVENTORY, never the stop recommendation.

No other OPEN is raised. No charge_basis line: no exit price is asserted.

### Collision check (python3 ops/open_collision.py, actual output, 00:08:30 UTC)

```text
## COLLISIONS

status: EMPTY

- `OPEN[DC1-INVENTORY-STATUS]` (report:135): NONE
```

### Post-read hashes (sha256, 00:08:22 UTC; identical to pre-read)

| basename | sha256 |
|---|---|
| APPROACHES.md | 6ccccdc25b8e983e9a5de86aabfb4e87db8f872cec5a1acf74ed8af37e41829e |
| COORDINATION.md | 4ce5b29af5a70e096a04b942cb978b1df425f9f0648decb720ec1f089ff37ac4 |
| FALLACY-v2.md | e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5 |
| README.md (team/swarmHQ) | 50cf45483cddf637e717ddfa2d136be4df074d13d360b851c1fb62a9e73edb0a |
| STATE.md | 095939d1ef012eaccf2a9d2e9d02d936d6d7e284ae3600d83c358f3c120b1472 |

Scope statement: five frozen snapshots only, read whole; no CAS,
experiment, network, ledger, peer report, log, receipt or jc2-lean /
jc2-web access; authored only with apply_patch; no artifact_finalize.py.
Literature statements marked "recollection" are unverified in this lane
and are pointers for ROOT primary check, not evidence. Timing: research
and authoring 00:00:22 to 00:09 UTC, inside the 18-minute cap.

<!-- BODY-END -->
