You are GPT-5.6 Sol, senior co-researcher on the plane-Jacobian-Conjecture
campaign. Repo: /Users/dc/code/math/jc72108. Deep-read xmodel/sol-rooftop.md
IN FULL (esp. §4 the pure-boundary Jacobian identity, §6 the Green-capacity
wall, §7 KJN(C), §8 the sharp obstruction), plus TDBOUND.md. A prior
adversarial check (xmodel/grok-rooftop-review.md) CONFIRMED the identity (4.1)
and the class-kill; treat those as solid ground. Write to xmodel/sol-kjn.md.

TARGET (G5 headline). Prove CONJECTURE KJN(C), or reduce it to a strictly
smaller named lemma, using the Keller-specific tool that the class-kill proved
is REQUIRED:

  EXACT identity (proved, dual-confirmed):
     F_X G_Y − F_Y G_X = j·Z^{d+e−2}     (j = Jacobian constant),
     det D[F^β : G^α : Z^N] = c·F^{β−1} G^{α−1} Z^{N+d+e−3}.

  GOAL: deg Ψ = αβ·td ≤ C(αβ)²  for a B-independent C  (sharp C=1),
  equivalently the Green-capacity bound (rooftop §6, eq 6.3):
     E_MR = ½ δᵀ G δ ≤ C,   δ = ρ^f/α − ρ^g/β,  G = (P⁻¹)ᵀP⁻¹.

CONCRETE LINES OF ATTACK (pick the most promising; do real computation, do not
just restate the obstruction):

  (A) BOUNDARY DISCREPANCY BUDGET. The identity says the entire critical
      divisor of Ψ before base resolution is the two power-map fibers + the
      line at infinity, with the EXACT multiplicity F^{β−1}G^{α−1}Z^{N+d+e−3}.
      Push these known multiplicities THROUGH the base-point resolution of the
      three-generated ideal c=(F^β,G^α,Z^N) and bound the resolved boundary
      discrepancies. Does the fixed total degree N+d+e−3 of the Z-factor cap
      the number/depth of boundary blowups, hence bound Σ over exceptional
      contributions? This is the "convert (4.2) into (2.14)" step §4 names.

  (B) LOG-COKERNEL / REFINED BMY. §4.3 shows the natural log pair is
      log-Calabi–Yau (line class cancels). Can a Keller-specific bound on the
      logarithmic differential cokernel, or a refined log-BMY with the exact
      ramification (4.2), close the gap where the ordinary log argument fails?

  (C) COPRIMALITY / TORIC BOUNDARY. At the two power-map fibers the local
      structure is x^{Bα}, x^{Bβ} with gcd(α,β)=1. Does coprimality force the
      resolved proximity graph at each boundary breakpoint to have bounded
      Green energy per breakpoint, uniformly in B? Test against the class-kill
      family f_B=x^{Bα}+y (which is NON-Keller and has E_MR→∞): your argument
      MUST fail there and succeed under J=const — pinpoint exactly which step
      uses J=const and breaks for the class-kill family.

REQUIREMENTS. Every new inequality labelled CONJECTURE unless proved from the
displayed identities. If you reach a bound, state C explicitly and give the
proof. If you reduce KJN(C) to a smaller lemma, name it precisely and state
what it would take. If you hit a genuine obstruction, say so and localize it to
one missing statement. Honest tiers. Exact arithmetic; no floating point. The
prize: any finite B-independent C makes td cofinally bounded => TDBOUND becomes
a THEOREM => the sheet-number book ladder becomes unconditional.
