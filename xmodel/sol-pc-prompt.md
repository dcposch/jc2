You are GPT-5.6 Sol, senior co-researcher on the plane-Jacobian-Conjecture
campaign. Repo: /Users/dc/code/math/jc72108. Deep-read xmodel/sol-rpmc.md IN
FULL (the two-block thick-line degeneration §1-§2, the exact intersection-defect
identity E_P=Delta_P/(alpha beta), and the EXACT polar bridge Delta_P =
sum_{gamma|P} max{0, ord_gamma F_X - (d-2)m_gamma}), and xmodel/sol-kjn.md §5-§7
for the matrix-factorization context. Everything there is accepted EXACT/PROVED.
Write to xmodel/sol-pc.md. Char 0.

TARGET. Prove CONJECTURE PC(C), equivalently RPMC(C) (Thm 7.1 => KJN(C) =>
TDBOUND theorem). Any finite B-independent C is the G5 HEADLINE.

PC(C): at a proper boundary root P of H (F_d=xi H^alpha, G_e=eta H^beta,
deg H=B, mult mu), on the normalization branches gamma of a general F-fiber
above P with m_gamma = ord_gamma z,
    sum_{gamma|P} max{0, ord_gamma F_X - (d-2) m_gamma}  <=  C alpha beta mu / B.

The exact tools already PROVED in sol-rpmc (use them, do not re-derive):
  - one transverse Smith defect of size c=alpha*mu-1; two z-blocks (r, M-r),
    1<=r<=d-1, M-r>=e-1; jump counts min(q,r,M-q) determined.
  - Delta_P is a nonnegative integer = total pole order on a generic fiber
    = the positive polar excess (0.6).

CONCRETE LINES (do real algebra):
  1. ADJUNCTION / POLAR CLASS. ord_gamma F_X - (d-2)m_gamma is a polar-excess
     term. On the normalization of a general F-fiber (a curve of geometric
     genus bounded via the pure-minor identity), relate sum_gamma ord_gamma F_X
     to a ramification/different and (d-2) sum m_gamma to the fiber's
     intersection with the boundary. Does adjunction on the fiber (or the
     Zeuthen-Segre / polar formula) cap the POSITIVE part by the local root
     weight mu (times alpha beta/B)? The generic F-fiber has degree e and meets
     L_inf in the mu-supported cluster; that is where the 1/B comes from.
  2. TWO-BLOCK LEVER. The split r (1<=r<=d-1) plus the single Smith defect
     alpha*mu-1 already bound the FIRST filtration step. Show the higher
     jump exponents ell_{q,a} telescope: the sum of all positive polar excesses
     equals Delta_P = alpha beta B mu - n_P, and n_P (the local intersection of
     the two DISPLACED members) is ALMOST maximal because both members share
     the leading power H^alpha, H^beta. Bound alpha beta B mu - n_P directly by
     bounding how much the intersection can drop below alpha beta B mu.
  3. SEMICONTINUITY. n_P = i_P(F-lambda Z^d, G-nu Z^e) for general lambda,nu.
     Compare to the special members F, G themselves (lambda=nu=0): the drop is
     controlled by the common tangent cone H. Coprimality (alpha,beta)=1 forces
     the two power maps H^alpha, H^beta to separate quickly.

CRITICAL SANITY GATE: your bound MUST FAIL on the non-Keller class-kill control
f_B=x^d+y (single root mu=B, but Delta_P = alpha beta(B^2 - B/beta) which
violates PC). There the residual Jacobian curve adds branch order de-d-1 to the
polar excess. Pinpoint EXACTLY the step that uses Fitt_0=(Z^M) / no-residual-
curve and breaks for the control. If it does not break, the argument is wrong.

DELIVERABLE: full proof + explicit C if obtained; else the exact partial (which
of the three positive-excess sources you bounded, which remains) and the single
missing inequality, named. Label unproved steps CONJECTURE. Exact arithmetic.
Honest tiers. Terse, technical.
