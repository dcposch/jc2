# f10-all-r-scale-cover-gate-fable5-20260910 — FIRST Fable 5.1 review: uniform complete-source scale cover

status: UNSEALED (adapter seals; no Seal section and no charge_basis authored here)
lane: f10-all-r-scale-cover-gate-fable5-20260910
first_action_utc: 2026-09-10T09:26:06Z (hash of all 10 inputs); stop earlier of 09:40:06Z and 09:42:00Z; reserve 09:40:00Z; never reset
mode: manual math/text/hash only; zero subprocess/CAS/script arithmetic; only date, ls, wc, cat, head, tail, od, grep, sha256sum, mkdir, apply_patch ran
owned: xmodel/f10-all-r-scale-cover-gate-fable5-20260910.md, box/f10-all-r-scale-cover-gate-fable5-20260910/ (both absent at 09:26:06Z)
premises: accepted 16r (whole-mate Euler elimination + its gate), 17zz (resonance unit + its gate), 17zzd (univariate unit + septic gate) exactly at their charged scopes. 17zz's H-unit is inherited from accepted 17o through 17zz; not re-audited. No r2 scale theorem, no new ell theorem, no middle/late unit premise.

## 0. Custody (10 ordered immutable snapshots, hashed BEFORE any body read, all read WHOLE)

Table in box/f10-all-r-scale-cover-gate-fable5-20260910/input_custody.md: all 10 sha256 equal the charged ordered list (b6c5e894, 989e2aba, 0830b4eb, e49c2566, a5ab487c, 77d59f7b, 8cf54b2f, dc43ef1c, 890e5c9c, cff18a06); every file read WHOLE by a single untruncated cat, no clipped interval. Producer seal recomputed from bytes: 8698 bytes through the marker line, sha256 beab00a9fbf5254ba246e84b7590ae7a48acc445fdfec467e091ac56fcb060fc, equal to the artifact json; timeline (first 09:09:30.169621309, reserve 09:19:30, cap 09:21:30, closed 09:14:53Z, finalized 09:15:02Z) consistent with READ-SCOPE, ROOT-CARD (first+12 min earlier than 09:23) and the charged IDLE 09:16:14. No link followed; no other file opened.

## A. Leading quotient L = B_nu[s,s^-1] from the two top rows

Own rederivation. With wt(S,t)=(1,r) the weight-m part of A=St^3+(Sd-u)t^2+(1-ud+Sv)t+k is S^m C(t/S^r), C=theta^3+d_r theta^2+v_2r theta+k_m, so F=d_r, H=v_2r, a=k_m; the weight-n part of B is S^n D(t/S^r) with D_j=[S^(n-rj)]B_j, D_5=1, D_0=b. With theta=t/S^r: A_S=S^(m-1)(mC-r theta C'), A_t=S^(m-r)C', likewise for B, so [A,B]_top=S^(m+n-r-1)(mCD'-nC'D) and -S^2t^7=-S^(7r+2)theta^7 with m+n-r-1=7r+2: mCD'-nC'D=-theta^7 exact. Pivot of D_j in the theta^(j+2) row is mj-3n, equal to the top Euler eigenvalue j-3(n-rj): values -(3r+2), -(6r+3), -(9r+4), -(12r+5), -(15r+6), all nonzero, so D_4..D_0=b are the same polynomials in F,H,a as the top coefficients of the 16r B*. Top slots: [S^(6r+2)]E1_res=[theta^1](mCD'-nC'D) since 2k'B2, h'B1, hB1', fB0' contribute only products of leading coefficients and -u has degree 0; [S^(7r+2)]E0_res=[theta^0](...) likewise; theta^7 automatic. Hence Q[F,H,a,omega]/(two top rows, omega ab-1) is exactly 17zz's L (its D_i, b eliminated by the five pivots, ab inverted), and A_r = L[u,ell,d_(<r),v_(<2r),k_(<m)]/(remaining rows) as rings, the lower generators free over L before those rows. L=B_nu[s,s^-1] is the accepted 17zz/17zzd two-sided normalization (nilpotents included, B_nu=Q[V]/(S) etale rank 7 by 17zzd); no component, field or r mod 7 selection anywhere. A_r is declared as the gauge-fixed 16r coefficient ring, with the field/gauge equivalence to compact pairs left at 16r's scope. CONFIRMED.

## B. Full-mate normalization, weights, free-z argument, counts

Direct substitution t=vartheta/s: s^3 A gives S vartheta^3+(S Dpar-U)vartheta^2+(z-U Dpar+S Vpar)vartheta+Kpar and s^3 Pi=z vartheta-U vartheta^2+S vartheta^3: (2) exact. Chain rule: d/dvartheta=(1/s)d/dt, so [Ahat,Bhat]_(S,vartheta)=s^3 s^4 A_S B_t - s^2 s^5 A_t B_S = s^7 Delta(S,vartheta/s) = s^7+U s^5 vartheta-E vartheta Pihat-vartheta Pihat^2: both low targets and both s-powers exact. Leading values: s d_r=V/W, s^2 H=1/W, s^3 a=1/W, weight 0, in B_nu. Weights (3): every term of Ahat and Pihat has weight m (checked all seven: S vartheta^3, S Dpar vartheta^2, U vartheta^2, z vartheta, U Dpar vartheta, S Vpar vartheta, Kpar); fhat=S Dpar-U has weight r+1, hhat weight q, so each Euler forcing Qhat_j has weight n-rj; hatted upper targets vartheta^2..vartheta^6 are -Ez, EU-z^2, 2zU-ES, -U^2-2zS, 2US (weights n, n-r, n-2r, n-3r, n-4r), i.e. s^(5-j)delta_(j+2) under u=U/s, ell=E/s^3, z=s^2. Diagonal inversion by j-3i keeps weight n-rj-i per slot; Bhat_j=s^(5-j)B_j by uniqueness of the gauged diagonal solution, and Qhat_j=s^(5-j)Q_j inductively, so the two kernel compatibilities are s^2[S^1]Q_3 and s^5[S^0]Q_0, both zero in Q[X_lead,X,s,s^-1] by accepted 16r (polynomial identities in the free parameters). Free z: the map Q[X_lead,X,z]->Q[X_lead,X,s,s^-1], z->s^2, sends distinct monomials to distinct monomials, hence is injective over any coefficient ring; so both compatibilities vanish as polynomials in free z, and Bhat, hence every K1_i,K0_i, lies in B_nu[X,z], homogeneous of weight n / 6r+2-i / 7r+2-i. This is a polynomial-ring identity over Q, then base-changed; it holds in every B_nu-algebra, reduced or not, with no quotient-only identity promoted. Gauges k(0)=0, beta=gamma=0 are homogeneous zero conditions and survive scaling. Counts: r+2r+3r+2=6r+2 variables; E1 slots 0..6r+2 and E0 slots 0..7r+2 give 13r+6, of which the two top slots are the L rows, 13r+2 are positive-index and 2 are low; with the guard absorbed into L this is 16r's 13r+7. No slot above 6r+2 / 7r+2 exists (16r degree bounds) and no negative slot exists. CONFIRMED.

## C. Cover w^q = s, weights, both low rows

A_r[w]/(w^q-s) is free of rank q with basis 1,...,w^(q-1); w^-1=w^(q-1)/s since s is a unit; q=2r+1. For a weight-k homogeneous row K(X,z), substituting X_j=w^(2a_j)Y_j, z=w^(2q) gives w^(2k)K(Y,1). Low rows: K0_0 has weight 7r+2 and s^7=w^(7q), 7q-(14r+4)=3; K1_0 has weight 6r+2 and U s^5=w^(2(r+1)+5q)U0, 12r+7-(12r+4)=3. Hence w^(14r+4)(L0-w^3) and w^(12r+4)(L1-U0 w^3): (6) exact, and the common cube exponent 3 is r-independent. All a_j positive (r-i, 2r-i, m-i, r+1, m at least 1). CONFIRMED.

## D. Common-cover isomorphism, bases, maps, base change, conclusion scope

B_nu[s,s^-1,X,w]/(rows,w^q-s)=B_nu[X,w,w^-1]/(rows at s=w^q); the change X_j=w^(2a_j)Y_j is invertible over B_nu[w^+-]; rows become the 13r+2 slices, L0-w^3 and L1-U0 w^3, and (L0-w^3,L1-U0 w^3)=(L0-w^3,L1-U0 L0) by the displayed identity. With R=B_nu[Y]/(slices,L1-U0 L0), the ring is R[w]/(w^3-L0)[w^-1]; since w^3=L0 there, inverting w is inverting L0, so it equals R[L0^-1][w]/(w^3-L0)=C_r[w]/(w^3-L0), free of rank 3 with basis 1,w,w^2. L0 is forced a unit (L0=w^3, w a unit because s is). Forward map s->w^q, X_j->w^(2a_j)Y_j and inverse Y_j->w^(-2a_j)X_j, L0^-1->w^-3 are well defined on every relation (checked L0->w^(-14r-4)K0_0=w^(-14r-4)s^7=w^3, and L1-U0L0 -> unit times (K1_0-Us^5) minus U0 times unit times (K0_0-s^7)), mutually inverse on generators, polynomial in both directions because w^-1 exists. omega=1/(ab)=W t5 s^8=W t5 w^(8q). Both sides free of positive rank, so A_r=0 iff C_r=0; the isomorphism and both ranks are preserved under any base change B_nu->T, nilpotents included, giving A_r(x)T=0 iff C_r(x)T=0. The producer claims exactly this and explicitly not A_r isomorphic to C_r, not s=1, not a point, bound, exclusion, nonemptiness or JC2. CONFIRMED.

## E. Mixed row, weight 8r+3, envelopes

L1-U0L0=(zK1_0-UK0_0)(Y,1); zK1_0 has weight q+6r+2=8r+3 and UK0_0 has weight r+1+7r+2=8r+3, so the mixed row is the z=1 slice of a homogeneous polynomial of weight 8r+3, not 6r+2. A monomial Y^e of a weight-k slice satisfies sum a_j e_j = k-qe for a unique former z exponent e, so sum a_j e_j<=k and k-sum a_j e_j in qN; L0 has bound 7r+2 and J L0-1 bound 7r+3 (ordinary degree bounded by weighted degree because every a_j>=1). No coefficient count, height, rank or runtime is asserted, correctly. CONFIRMED.

## F. Controls, repairs, extension degrees

Dropping L0^-1 admits L0=0, contradicting L0=w^3 with w a unit in any nonzero ring; repair is to keep the localization (it is the transported s-unit, not a new guard). Setting w=1 imposes L0=1, an unlicensed extra equation; repair is to keep w free. Dropping the second low row deletes the retained row L1-U0L0; the producer calls it "independent", which is not proved in any charged input (the 16r family shows only the E0 constant slot non-automatic: in that family E1_res(0)=0), but the theorem retains the row, so nothing depends on it. Field-point-only reasoning is not used: the equivalence rests on free bases. Extension degrees: a C_r-point over K gives K[w]/(w^3-L0(pt)) nonzero of dimension 3, residue field of degree at most 3; conversely at most q; these are cover ranks, not degrees of any source map, as the producer states. No commutation with band eliminations is claimed. CONFIRMED; minimal repair for the one imprecision: replace "independent residual" by "retained residual, redundancy unproved".

## Verdict table

| item | verdict |
|---|---|
| A two top rows give L=B_nu[s,s^-1], pivots mj-3n, guards, no component selection, A_r = gauge-fixed 16r ring | CONFIRMED |
| B normalization (2), derivative s^-1, z=s^2, targets s^7 and U s^5, weights m/n/7r+2, forcing and resonances and gauges retained, free-z injectivity over arbitrary B_nu-algebras, counts 6r+2 / 13r+4 / 13r+2, top slots accounted | CONFIRMED |
| C free faithful rank q, invertible w, X_j=w^(2a_j)Y_j, both low rows (6) | CONFIRMED |
| D isomorphism (7), bases 1..w^(q-1) and 1,w,w^2, both maps, forced L0 unit, omega=W t5 w^(8q), nonreduced base change, conclusion A_r=0 iff C_r=0 only | CONFIRMED |
| E mixed row slice of zK1_0-UK0_0 of weight 8r+3, bounds 7r+2 / 7r+3, unique former z exponent | CONFIRMED |
| F three controls, field-point independence, extension degrees <=3 / <=q | CONFIRMED (one wording imprecision, no verdict change) |

REFUTED: none. GAP: none in the derivation. Attacks tried and failed: a missing top slot (none above 6r+2/7r+2); a lower variable entering a top row (leading-product check per term); an s-power leaking into the upper reconstruction (targets at vartheta^0,1 only); a wrong cube exponent (both differences are 3); an identity true only at z=s^2 (monomial injectivity); a hidden field or reducedness hypothesis (none; freeness only). Strongest surviving statement: for every r>=2, A_r=0 iff C_r=0, uniformly, over every B_nu-algebra; C_r=0 remains uncomputed and nothing about source points, bounds or JC2 follows.

## OPEN(S) RAISED

None. No new canonical OPEN ID; the remaining quantity is the producer's C_r=0 for each r>=2, uncomputed and not requested here.

## COLLISIONS

status: EMPTY

- NONE. This lane wrote exactly xmodel/f10-all-r-scale-cover-gate-fable5-20260910.md and box/f10-all-r-scale-cover-gate-fable5-20260910/input_custody.md, both absent at 09:26:06Z; no Seal, no charge_basis, no source or coefficient artifact, no subprocess, no rerun of any accepted report.

## Completion

Own WHOLE read of this report at 09:35:31Z, before the 09:40:00Z reserve; raised-OPEN check (none) and own-only collision check (EMPTY) precede the marker. Every 64-hex token in this file and in the custody file equals a charged input hash from live sha256sum output or the recomputed producer body hash (11 distinct tokens, 11 matches). All ten input hashes rechecked unchanged at that read. Authoring attestation: all mathematics above is manual; all writes were apply_patch; zero scientific subprocess. The marker below is the only standalone marker in this file and nothing follows it. All writers idle at the marker.

<!-- BODY-END -->
