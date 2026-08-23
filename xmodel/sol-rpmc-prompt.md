You are GPT-5.6 Sol, senior co-researcher on the plane-Jacobian-Conjecture
campaign. Repo: /Users/dc/code/math/jc72108. Deep-read xmodel/sol-kjn.md IN
FULL (esp. §5 the thick-line gradient cokernel / matrix factorization, §6 the
per-root energy split, §7 CONJECTURE RPMC(C) + Theorem 7.1 + "what a proof must
show"). Everything there is accepted as EXACT/PROVED input. Write to
xmodel/sol-rpmc.md. Char 0 throughout.

TARGET. Prove CONJECTURE RPMC(C) for a single proper boundary root, or make
decisive partial progress on the concrete §7 proof program. Since Theorem 7.1
(PROVED) gives RPMC(C) => KJN(C) => TDBOUND theorem, ANY finite B-independent C
here is the G5 headline.

RPMC(C): at one proper root P_i of H (F_d=xi H^alpha, G_e=eta H^beta, deg H=B,
mult mu_i), complete the surface at P_i, take the minimal simultaneous
principalization of the two pencil ideals and the balanced ideal, assume the
germs come from homogeneous integrable F,G with the pure-minor identity
F_X G_Y - F_Y G_X = j Z^M (M=d+e-2). Then
    E_i = (1/2) sum_{p > P_i} (R_p/alpha - S_p/beta)^2  <=  C * mu_i / B.

THE CONCRETE PROGRAM (§7, three bullets -- do real algebra, not restatement):
  1. CLASSIFY / estimate the two-generated graded matrix factorizations of Z^M
     whose two columns are GRADIENTS, i.e. A=[[F_X,G_X],[F_Y,G_Y]] with
     det A = j Z^M and the integrability constraints (F_X)_Y=(F_Y)_X,
     (G_X)_Y=(G_Y)_X. Localize at the boundary root P_i (work in the completed
     local ring at P_i on L_inf). What are the possible Z-adic elementary
     divisors / the local normal form of A there?
  2. RELATE the Z-adic elementary-divisor jumps of A at P_i to the point-basis
     multiplicity discrepancies beta R_p - alpha S_p appearing in E_i (6.6).
     Key lever: after removing exceptional monomials, the transformed det is a
     UNIT off the strict transform of Z=0 (no residual Jacobian curve). Turn
     "unit off Z" into control of how long a nonzero discrepancy can persist
     along a free/satellite proximity chain over P_i.
  3. Prove the square sum E_i <= C mu_i/B (sharp C=1), or the best bound you can.

CRITICAL SANITY GATE (must hold): your argument MUST FAIL on the non-Keller
class-kill control f_B=x^d+y, g_B=x^e+y^{e-1} (single root mu_P=B, E_P=B^2-B/beta
which violates every fixed C). There Q_B has an EXTRA Jacobian curve
(Fitt_0=(Q_B) not (Z^M)). Pinpoint EXACTLY which step of your proof uses the
pure-minor/no-residual-curve hypothesis and therefore breaks for the control.
If your argument does not break there, it is wrong -- find the error.

DELIVERABLE: state precisely what you proved and at what tier. If you get a
finite C, give the full proof and the value. If you get a partial bound (e.g.
control of the discrepancy SIZE but not its persistence length, or a bound
under an extra hypothesis), state exactly what is proved and what single step
remains. Label every unproved inequality CONJECTURE. Exact arithmetic; no
floating point. Honest tiers. Terse and technical.
