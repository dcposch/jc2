-- corrected_869.m2
-- corrected Delta=(8,6,9) incidence
-- CONVENTION: GROBNER-mode output basis=[1] means UNIT IDEAL means EMPTY.
-- Companion .ms file is comment-free: msolve parses the first line as the
-- variable list (campaign 2026-08-24 in-band-comment hazard).
-- M2 is authoritative. Footguns observed: diff(var,poly); first degree;
-- no pi as a variable; name maps before applying; close stdin (exit 0).
-- No saturate(). Opens are Rabinowitsch. Rings asserted.
-- Corrected (8,6,9) incidence ideal, audit r2 §7.1.
-- G86 = p^3-q^4 + a22 p^2 q + a20 p q^2 + a18 q^3 + a16 p^2 + a14 p q + a12 q^2.
-- Closed: g_j = [t^j] G86 = 0 for j=10..22 (all degrees, not raw odds).
-- Open: u*g_9-1. Chart identities: g_23=0 automatically.
-- I_DP post-check length N=delta_aff=10 is not in this Groebner job.
-- in-chart gcd-2 cover: B=D=F=gam=e=0.

R0 = QQ[a22, a20, a18, a16, a14, a12, B, C, D, E, F, G, b, gam, d, e, f, MonomialOrder => GRevLex];
assert(isPolynomialRing R0);
assert(numgens R0 == 17);
assert(coefficientRing R0 === QQ);

St = R0[symbol t];
assert(numgens St == 1);
use St;
p = t^8 + B*t^5 + C*t^4 + D*t^3 + E*t^2 + F*t + G;
q = t^6 + b*t^4 + gam*t^3 + d*t^2 + e*t + f;
G86poly = p^3 - q^4 + a22*p^2*q + a20*p*q^2 + a18*q^3 + a16*p^2 + a14*p*q + a12*q^2;

-- Name the ring map before applying (footgun: unnamed maps).
killt = map(R0, St, {0_R0});
assert(killt(t) == 0_R0);

gj = (j) -> coefficient(t^j, G86poly);
closedIdx = {22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10};
closedGens = apply(closedIdx, j -> gj(j));
I0 = ideal closedGens;
assert(ring I0 === R0);
gopen = gj(9);
use R0;
assert(ring gopen === R0);
R = R0[u];
assert(numgens R == 1);
Iopen = sub(I0, R) + ideal(sub(gopen, R)*u - 1);
assert(ring Iopen === R);

Cover0 = ideal(B, D, F, gam, e);
assert(ring Cover0 === R0);
Cover = sub(Cover0, R);
assert(ring Cover === R);

colonInf = (I, J) -> (
  assert(ring I === ring J);
  K := I;
  npass := 0;
  while true do (
    npass = npass + 1;
    if npass > 50 then error "colonInf: exceeded 50 passes";
    Knext := K : J;
    assert(ring Knext === ring I);
    if Knext == K then break;
    K = Knext;
  );
  K
);

Icolon = colonInf(Iopen, Cover);
assert(ring Icolon === R);

-- immersive open: Res_t(p', q') != 0. diff(var, poly) argument order.
dp = diff(t, p);
dq = diff(t, q);
resSt = resultant(dp, dq, t);
res0 = killt(resSt);
assert(ring res0 === R0);
Rv = R0[u, v];
Iimm = sub(I0, Rv) + ideal(sub(gopen, Rv)*u - 1, sub(res0, Rv)*v - 1);
assert(ring Iimm === Rv);
IimmColon = colonInf(Iimm, sub(Cover0, Rv));
assert(ring IimmColon === Rv);

<< "=== corrected_869 dim Iopen " << dim Iopen << endl;
<< "=== corrected_869 dim Icolon " << dim Icolon << endl;
<< "=== corrected_869 dim IimmColon " << dim IimmColon << endl;
Gb = gens gb Iopen;
<< "=== corrected_869 gb Iopen " << Gb << endl;
if Iopen == ideal(1_R) then << "=== corrected_869 EMPTY" << endl else << "=== corrected_869 NONEMPTY" << endl;
-- GROBNER-mode companion: basis=[1] means UNIT IDEAL means EMPTY.
exit 0
