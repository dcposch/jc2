You are GPT-5.6 Sol, senior co-researcher on the plane-Jacobian-Conjecture
campaign. Repo: /Users/dc/code/math/jc72108. Deep-read xmodel/sol-k2c.md IN FULL
(esp. Theorem 2.1 the Henon tower, §3.2 the fixed-degree bounds kappa_i<=d_f and
#char<=log2 d_f, §5 UCD-A-min), xmodel/sol-bdelay.md §5 (UCD), and
xmodel/sol-unify.md §1 (the Puiseux gcd dictionary prod nu_j = kappa_i, the
residue-A ladder 1->7->21->42). Accept all as EXACT/PROVED. Write to
xmodel/sol-ucda.md. Char 0.

TARGET (the G2 wall). Prove or decisively attack CONJECTURE UCD-A-min: there is
an integer K_A such that every lexicographically degree-minimal, NONautomorphic
Keller pair in Sigray normal form of type (2,3) carrying the residue-A td=6
two-pole inventory has pole Puiseux denominator max_i kappa_i <= K_A. By the
depth dictionary (prod nu_j = kappa_i, nu_j>=2), this gives d_sh <= log2(K_A) =>
bounded delay => G2. This closes the SECOND foundational wall (G5's chain is
KJN<=RPMC<=>PC, handled separately).

THE CRUX (identified by sol-k2c). The Henon automorphism tower realizes
kappa=42*2^r->inf at td=1, so bounded td alone does NOT bound kappa. BUT that
family is an AUTOMORPHISM: it degree-minimizes to the identity; its long
approximate-root chain is a REMOVABLE re-embedding, not an Aut-orbit invariant.
The whole content of UCD-A-min is therefore: a DEGREE-MINIMAL, NONautomorphic,
noninvertible Keller germ cannot hide an unbounded removable carrier chain.

ATTACK LINES (do real algebra, use the tools the formal tier ignores):
  1. DEGREE-MINIMALITY vs APPROXIMATE ROOTS. The Henon chain works because each
     H_q is invertible, so the whole chain is undone by K = Phi^{-1}. For a
     NONinvertible Keller pair (td=6), the analogous carrier insertions are NOT
     removable by an automorphism. Formalize: if inserting an l=0, nu=2 carrier
     factor could be undone by a polynomial automorphism of A^2, the pair was
     not degree-minimal. Conversely, does a genuinely non-removable carrier
     insertion FORCE a degree increase that a fixed (td=6, type (2,3)) budget
     cannot pay? I.e. is there a degree bound deg <= Phi(td, type) for
     degree-minimal reps, so that kappa_i <= d_f <= Phi(6,(2,3)) = K_A?
  2. CONSTANT JACOBIAN ALONG THE POLE BRANCH. Use the pure-boundary identity
     F_X G_Y - F_Y G_X = j Z^{d+e-2} restricted to the residue-A pole branch:
     it constrains successive Puiseux coefficients. Does J=const + the fixed
     A_4/Belyi passport {2,3} + the two-pole handshake actually bound the NUMBER
     of nu=2 gcd-drops between pole entry and merge (the free direction the
     formal calculus leaves open)? The formal tower has arbitrary q>=2; does
     polynomial origin at fixed reduced type collapse this?
  3. SEMIGROUP / CONDUCTOR AT FIXED td. For a NONautomorphic pair the branch has
     positive delta-invariant / conductor; unlike the automorphism (delta=0
     after minimization). Is there a conductor or genus quantity, bounded by td
     and type, that prices each added characteristic factor for a nonautomorphic
     germ -- so the count is bounded even though it is unbounded for
     automorphisms? This is the exact place the Abhyankar-Moh one-place
     inequality fails for multi-place residue-A; find the correct multi-place
     substitute.

CRITICAL SANITY GATE: your argument MUST FAIL for the Henon automorphism family
(td=1, kappa->inf) -- pinpoint exactly the step that uses NONautomorphic /
degree-minimal / positive-conductor and breaks for the automorphism. If it does
not break there, it is wrong.

DELIVERABLE: proof + explicit K_A if obtained; else the decisive partial (a
degree bound under an extra hypothesis, or the single missing inequality named)
and whether UCD-A-min looks TRUE (evidence) or is itself the crux where a
counterexample could live. Label unproved steps CONJECTURE. Exact arithmetic.
Honest tiers. Terse, technical.
