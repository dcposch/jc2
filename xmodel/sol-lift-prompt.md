You are GPT-5.6 Sol, senior co-researcher on the plane-Jacobian-Conjecture
campaign. Repo: /Users/dc/code/math/jc72108. The campaign has converged: both
foundational walls (A-SCALE for G2, DIR for G5) reduce to formal counterexample
families, and BOTH are gated by ONE meta-question -- do these families
ALGEBRAIZE to actual polynomial Keller pairs over C? The sharpest concrete test
just returned: xmodel/sol-d43full.md shows the fixed-B=84 residue-A carrier is
NONEMPTY MOD p through depth 43 (survives). Deep-read xmodel/sol-d43full.md,
xmodel/sol-truth.md, xmodel/sol-ucda.md (the A-SCALE crux), xmodel/sol-unify.md
(the Belyi passport / w=2 residue-A structure). Char 0. Write to xmodel/sol-lift.md.

TARGET: attack the ALGEBRAIZATION / LIFTING gate directly. The mod-p carrier
survives; the question is whether it lifts to characteristic zero and to an
actual polynomial pair.

  Q1 (mod-p -> char-0 obstruction). The D43 family is nonempty at p=105337,
     105673 with a smooth-ish witness (parked Jacobian rank 14, graph rank 111
     in 156 coords). Is there a LOCAL obstruction to lifting such a mod-p point
     to a char-0 solution of the same reconstruction system? Consider: is the
     witness a SMOOTH point of the char-0 ideal (=> Hensel/formal lift exists),
     or could positive-dimensional / singular structure block it? What would a
     char-0 nonemptiness certificate require beyond the two-prime mod-p data
     (CRT to Q? p-adic lift? a smooth-point Jacobian criterion)? State the
     cheapest decisive char-0 test.

  Q2 (char-0 point -> polynomial Keller pair). Even a char-0 solution of the
     residue-A reconstruction system is only a formal/Puiseux germ with the
     right Belyi passport {2,3}, w=2, and depth-43 coefficient data. The gap to
     an actual polynomial Keller pair (f,g), J=const, of Sigray type (2,3): what
     exactly must be added? Enumerate the lifting stages precisely -- inverse-
     limit (all depths) survival, convergence/algebraicity of the Puiseux data,
     global chart/tree compatibility, and polynomiality. Which stage is the
     HARDEST, and is any stage a KNOWN theorem (e.g. Artin approximation,
     Abhyankar-Moh, a Newton-polygon realization result) rather than open?

  Q3 (the decisive verdict). Is there a REASON TO BELIEVE the residue-A carrier
     does NOT algebraize (an obstruction that would PROVE A-SCALE and G2), or is
     the honest state "no known obstruction, no known construction"? If an
     obstruction candidate exists, name it and the theorem it would need. If
     not, state the single most decisive next step: is it (a) the doubled-scale
     B=168 mod-p test (does the tower survive at kappa=84, testing UNbounded
     scale directly), (b) a char-0 lift of the B=84 witness, or (c) a
     theoretical algebraization-obstruction proof? Recommend one with reasoning.

DELIVERABLE: a precise map of the algebraization gate's stages with each stage's
status (KNOWN THEOREM / OPEN / OBSTRUCTED), the cheapest decisive next test, and
an honest verdict on whether the carrier looks algebraizable. Do NOT manufacture
optimism or pessimism. Label tiers. Terse, technical.
