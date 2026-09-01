-- corrected_964.m2
-- corrected Delta=(9,6,4) incidence
-- CONVENTION: GROBNER-mode output basis=[1] means UNIT IDEAL means EMPTY.
-- Companion .ms file is comment-free: msolve parses the first line as the
-- variable list (campaign 2026-08-24 in-band-comment hazard).
-- M2 is authoritative. Footguns observed: diff(var,poly); first degree;
-- no pi as a variable; name maps before applying; close stdin (exit 0).
-- No saturate(). Opens are Rabinowitsch. Rings asserted.
-- Corrected (9,6,4) incidence ideal, audit r2 §7.1.
-- G96 = p^2-q^3 + a15 p q + a12 q^2 + a9 p + a6 q.
-- Closed: g_j = [t^j] G96 = 0 for 5<=j<=16 (all degrees).
-- Open: u*g_4-1. Chart identity: g_17=0 automatically. Constants omitted.
-- SIX-NODE QUESTION: delta_aff=6 (audit §3/§7.1; pa(9)=28, beta_1=23, delta_inf=22).
-- Corrected locus is known NONEMPTY (HF-twin). Iopen emptiness is NOT the nodal test.
-- REALIZED iff some closed point of Iopen passes idpPostcheck(p,q,6).

R0 = QQ[a15, a12, a9, a6, A, P6, B, P4, C, P2, D, a, Q3, b, Q1, MonomialOrder => GRevLex];
assert(isPolynomialRing R0);
assert(numgens R0 == 15);
assert(coefficientRing R0 === QQ);

St = R0[symbol t];
assert(numgens St == 1);
use St;
p = t^9 + A*t^7 + P6*t^6 + B*t^5 + P4*t^4 + C*t^3 + P2*t^2 + D*t;
q = t^6 + a*t^4 + Q3*t^3 + b*t^2 + Q1*t;
G96poly = p^2 - q^3 + a15*p*q + a12*q^2 + a9*p + a6*q;

-- Name the ring map before applying (footgun: unnamed maps).
killt = map(R0, St, {0_R0});
assert(killt(t) == 0_R0);

gj = (j) -> coefficient(t^j, G96poly);
closedIdx = {16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5};
closedGens = apply(closedIdx, j -> gj(j));
I0 = ideal closedGens;
assert(ring I0 === R0);
gopen = gj(4);
use R0;
assert(ring gopen === R0);
R = R0[u];
assert(numgens R == 1);
Iopen = sub(I0, R) + ideal(sub(gopen, R)*u - 1);
assert(ring Iopen === R);

-- even-odd cover: P6=P4=P2=Q3=Q1=0 (degree-3 cover of a (3,2) cusp)
Cover0 = ideal(P6, P4, P2, Q3, Q1);
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

<< "=== corrected_964 dim Iopen " << dim Iopen << endl;
<< "=== corrected_964 dim Icolon " << dim Icolon << endl;
<< "=== corrected_964 dim IimmColon " << dim IimmColon << endl;
Gb = gens gb Iopen;
<< "=== corrected_964 gb Iopen " << Gb << endl;
if Iopen == ideal(1_R) then << "=== corrected_964 EMPTY" << endl else << "=== corrected_964 NONEMPTY" << endl;

-- Double-point scheme post-check for a CLOSED point (p0,q0) in QQ[tt].
-- N = delta_aff = 6. No saturate(). Variable Pi, not pi.
-- Conversion: Delta(tt^n) = sig*Delta(tt^{n-1}) - Pi*Delta(tt^{n-2}),
-- Delta(tt^0)=0, Delta(tt^1)=1.

dividedDiffTable = (maxn, sig, Pi) -> (
  L := new MutableList from toList((maxn+1):0_(ring sig));
  L#0 = 0_(ring sig);
  if maxn >= 1 then L#1 = 1_(ring sig);
  if maxn >= 2 then L#2 = sig;
  for n from 3 to maxn do L#n = sig*(L#(n-1)) - Pi*(L#(n-2));
  toList L
);

polyToDelta = (f, L) -> (
  Kt := ring f;
  tt := Kt_0;
  df := first degree f;
  acc := 0_(ring L#1);
  for n from 0 to df do (
    c := coefficient(tt^n, f);
    acc = acc + sub(c, ring L#1) * L#n;
  );
  acc
);

idpPostcheck = method();
idpPostcheck(RingElement, RingElement, ZZ) := (p0, q0, N) -> (
  Kt := ring p0;
  assert(Kt === ring q0);
  assert(numgens Kt == 1);
  tt := Kt_0;
  dp0 := diff(tt, p0);
  dq0 := diff(tt, q0);
  gg := gcd(dp0, dq0);
  immersive := (gg == 1_Kt);
  Rsp := QQ[sig, Pi, MonomialOrder => GRevLex];
  sig := Rsp_0;
  Pi := Rsp_1;
  maxn := max(first degree p0, first degree q0);
  L := dividedDiffTable(maxn, sig, Pi);
  Dp := polyToDelta(p0, L);
  Dq := polyToDelta(q0, L);
  I := ideal(Dp, Dq);
  assert(ring I === Rsp);
  << "idp: dim=" << dim I << " degree=" << (if dim I == 0 then degree I else -1) << endl;
  << "idp: immersive=" << immersive << endl;
  if dim I != 0 then (
    << "idp: FAIL not 0-dimensional" << endl;
    return false;
  );
  if degree I != N then (
    << "idp: FAIL length " << degree I << " != expected " << N << endl;
    return false;
  );
  if I != radical I then (
    << "idp: FAIL not reduced" << endl;
    return false;
  );
  << "idp: PASS reduced length " << N << endl;
  true
);

<< "=== corrected_964 six-node question: idpPostcheck(p0,q0,6) on a closed point of Iopen" << endl;
<< "=== corrected_964 corrected locus is known NONEMPTY (HF-twin); EMPTY of Iopen would contradict that control" << endl;

-- GROBNER-mode companion: basis=[1] means UNIT IDEAL means EMPTY.
exit 0
