# ALLTHIN0525 — pullbacks of a zero-thinness valuation
Status: INTERNAL / UNREVIEWED; source-fit lemma, no novelty or JC2 claim.
Let H=(P,Q):A2_C -> A2_C be dominant polynomial with JH in C*, E=C(P,Q), K=C(x,y). Let eta be a real, finite-valued valuation of the target function field, trivial on C*, normalized by min{eta(1),eta(X),eta(Y)}=-1, with A(eta)=0.
For every real valuation extension w of eta to K under X->P,Y->Q, define b=-min{w(1),w(x),w(y)}.
Claim: b is finite and positive; nu=w/b belongs to V0 and D_H^o, H_bullet(nu)=eta, and A(nu)=0. No uniqueness or degree conclusion follows here.
Proof: w is finite on nonzero field elements. If w(x),w(y)>=0, every nonzero polynomial in x,y has nonnegative w-value; this contradicts min{w(1),w(P),w(Q)}=-1. Thus b>0, and nu has the specified V0 normalization.
Since w|E=eta, H_*(nu)=eta/b, hence d(H,nu)=1/b>0 and H_bullet(nu)=eta. Definition7.1 puts nu in D_H^o, contained in D_H.
Apply Favre--Jonsson Lemma7.6: nu(JH)+A(nu)=d(H,nu) A(H_bullet(nu)). The first term is zero because JH is a nonzero constant, and the right side is zero by hypothesis. Hence A(nu)=0.
In particular the lemma applies to every such valuation extension of the already obtained zero-thinness infinitely singular eigenvaluation. Existence/classification/ramification indices of those extensions are not proved here and are not needed for this implication.
Excluded: alpha(nu)>=0, nu in V1, nu fixed by H_bullet, uniqueness of an extension, any summed degree identity, properness, surjectivity, or N=1. No properness-only preimage formula is used.
Source: Favre--Jonsson, Eigenvaluations, Ann. Sci. ENS40(2007),309-349, https://www.numdam.org/article/ASENS_2007_4_40_2_309_0.pdf , Definition7.1 and Lemma7.6 (7.2); local Lemma4.7 proof sketch says continuity reduces to divisorial change of variables. These named published results/definitions are imported; foundational continuity/geometric-interpretation proofs were not reaudited.
Exact source PDF SHA256 c5a001004feae45e3465d2eee990f4b3f66ad68c59ed591b0bec6625fb9ec38b; extraction SHA256 d077dd8c0e9a33c34b12e00969ae10fe1b5537ffb4d69c7cdd33c19197b9d5d2. Selected LF windows1387-1410,1515-1538,885-908; no whole-PDF reading claim. Historical citation in frozen public notes37950-37955 establishes this is a reused primary source; current gap is application to every extension, not a new Jacobian identity.
