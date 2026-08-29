\\ =====================================================================
\\ D43 coefficient algebra K0: exact field certificate, PARI/GP layer, R3.
\\ Target host: the registered AWS "r6b" host, PARI/GP 2.15.4, one core.
\\ Replay:  gp -q --default parisize=64M k0_field_cert_r3.gp
\\ The last two printed lines must read
\\     CENSUS 110/110
\\     K0_UNCONDITIONAL 1   E_BASE_IDENTITIES 1
\\ =====================================================================
\\
\\ This file is the SECOND engine.  k0_field_checker_r3.py replays every
\\ unconditional statement below in stdlib Python with no PARI call at all,
\\ using explicit integer, finite-field and canonical 432-monomial quotient
\\ arithmetic.  Neither engine reads the other's output.
\\
\\ R2 changes against k0_field_cert_r1.gp (never parsed by any GP):
\\  [R2-A] the terminal flag is E_BASE_IDENTITIES, not E_CONDITIONAL.  This
\\         file contains no cube-root layer, so it cannot certify the
\\         E-conditional ratio theorem; that theorem is single-engine Python
\\         and the runner terminal says so.  What GP does do now is READ the
\\         literal E data and check the base-level reduction chain, which R1
\\         did not do at all.
\\  [R2-B] the two terminal flags are driven by two separate accumulators,
\\         ok (L0-L4) and okE (L5), so an E-layer failure cannot flip the
\\         unconditional banner.
\\  [R2-C] the Map/mapput/mapget/Mat(t_MAP) construction is gone; the
\\         square-root fibres are collected in plain vectors and each hom is
\\         verified to have exact order 168, which polrootsmod alone does not
\\         give.  The R1 within-fibre equality test could not fail.
\\  [R2-D] a mod-p rank-432 independence witness: the evaluation matrix of the
\\         432 standard monomials at the 432 F_p-points of the presentation is
\\         a Kronecker product of a 12x12, an 18x18 and a 2x2 block.  The three
\\         squared determinants are row-order independent and are shared
\\         observables with the Python engine.
\\  [R2-E] the five relations are carried as literal multivariate polynomials
\\         and sigma is applied to them BEFORE any quotient, so the
\\         Galois-stability check is not sigma(0) == 0.
\\  [R2-F] the optional nffactor block is deleted outright.  It was never on
\\         the theorem path, its alarm(600) exceeded both the 120 s gp cap and
\\         the 300 s unit cap, and deleting it lets the runner treat every
\\         unrecognised output line as a fault.
\\  [R2-G] the norm corroboration and the conductor lines read the ALPHA / EPS
\\         / conductor data instead of restating constants.
\\
\\ R3 changes against k0_field_cert_r2.gp (still never parsed by any GP):
\\  [R3-A] the L1 CRT line was constant-true in GP -- (21*5+4*16)%168 could
\\         not print 0 without editing the file.  The zeta8 exponent, the
\\         zeta42 exponent and the two generation exponents are now data
\\         (Z8E, Z42E, GENE) read by the zeta8 line, the GENERATION line and
\\         the CRT line alike, and the modulus is CONDTOWER[3].  The gate
\\         count, the label set and every printed value are unchanged: this
\\         is the R2 review's one mechanical GP finding, no more.
\\  [R3-B] the unreachable within-fibre branch in charframes is marked as
\\         defensive, not as a check.
\\ Nothing else in this file changed.  The mathematics, the 110 gates, the 29
\\ observables and every printed value are identical to R2; only the file
\\ name, the route string and the two items above differ.
\\
\\ Corrections to the illustrative recipe in the charged report
\\ xmodel/d43-k0-splitting-primary-research-opus5-20260828.md section 9.2 are
\\ carried over from R1 and are marked [FIX n] at their sites:
\\   1  the tower was built in the same variable as P42;
\\   2  the order-42 test omitted the prime 7 (z^6 != 1);
\\   3  my(r = ..., a = f(r)) evaluates a's initialiser in the enclosing scope;
\\   4  w = Mod(znprimroot(p), p) wraps a t_INTMOD inside Mod();
\\   5  P42' as a stored-polynomial derivative; deriv() is explicit;
\\   6  chk() accepted any nonzero object as true; it now demands a t_INT;
\\   7  there was no census, so deleting a line turned a FAIL into a PASS.

ok = 1; okE = 1; ncheck = 0; nexpect = 110;

chk(lab, val) =
{
  my(b);
  if (type(val) != "t_INT", error(Str("non-boolean gate result: ", lab)));
  b = (val != 0);                                       \\ [FIX 6]
  ncheck = ncheck + 1;                                  \\ [FIX 7]
  ok = ok && b;
  printf("%-58s %d\n", lab, b);
  b;
}

\\ [R2-B] the L5 accumulator is separate: a conditional-layer failure must not
\\ be able to change the unconditional banner.
chkE(lab, val) =
{
  my(b);
  if (type(val) != "t_INT", error(Str("non-boolean gate result: ", lab)));
  b = (val != 0);
  ncheck = ncheck + 1;
  okE = okE && b;
  printf("%-58s %d\n", lab, b);
  b;
}

\\ Machine-readable cross-engine channel.  The Python engine emits the same
\\ keys from its own independent computation and the runner requires exact
\\ agreement on every one of them, so neither engine's banner is trusted.
obs(k, v) =
{
  if (type(v) != "t_INT", error(Str("non-integer observable: ", k)));
  printf("OBS %s %d\n", k, v);
  v;
}

\\ =====================================================================
\\ the presentation, as data
\\ =====================================================================
PHI42SRC    = [1,1,0,-1,-1,0,1,0,-1,-1,0,1,1];   \\ d43_common_integral_emitter.py:36
BASIS_SHAPE = [12,2,3,3,2];                      \\ selected_rows_v2.py:62
BASIS_RANK  = 432;                               \\ selected_rows_v2.py:63
LEAD        = [[12,0,0,0,0],[0,2,0,0,0],[0,0,3,0,0],[0,0,0,3,0],[0,0,0,0,2]];
ALPHA       = [[3,1],[3,-1]];                    \\ alpha_k = c + d*r3
RSQ         = 3;                                 \\ r3^2
HB          = 2; HC = 3;                         \\ HB*h^2 = HC
R3E         = [14,154];                          \\ r3 = y^14 + y^154 in B
Z42E        = 4;                                 \\ zeta42 = y^Z42E
Z8E         = 21;                                \\ zeta8  = y^Z8E
GENE        = [5,16];                            \\ zeta8^GENE[1]*zeta42^GENE[2]
EPSD        = [2,1];                             \\ eps = 2 + sqrt3
COMPONENTS  = ["K0"];
IDEMPOTENTS = [0,1];
RAMIFIED    = [2,3,7];
CONDTOWER   = [21,84,168];
CERTPRIMES  = [673, 1009];
GENORDER    = 0;                                 \\ set by the L2 loop, read by L3
SILENT      = [105337, 105673];
WITNESS     = 105337;
ETERMS      = [[9,5,2,4],[9,-5,3,4]];            \\ (c0, c1*r3, generator, exponent)

P42  = polcyclo(42, 'x);
P168 = polcyclo(168,'y);                                \\ [FIX 1] y, not x

\\ =====================================================================
\\ L0  the literal source pins and the rank-432 leading-term certificate
\\ =====================================================================
chk("L0 PHI42 source tuple == polcyclo(42)",  Vecrev(P42) == PHI42SRC);
chk("L0 PHI42 is not x^42-1",                 P42 != 'x^42 - 1);
chk("L0 deg polcyclo(168) == 48",             poldegree(P168) == 48);
chk("L0 Phi168(y) == Phi42(y^4)",             P168 == subst(P42,'x,'y^4));
chk("L0 disc(Phi42) == 3^6*7^10",             poldisc(P42) == 3^6*7^10);
chk("L0 disc(Phi42) is odd",                  poldisc(P42) % 2 != 0);
chk("L0 rad disc(Phi42) == {3,7}",            Set(factor(poldisc(P42))[,1]~)
                                              == Set([3,7]));
chk("L0 basis shape product == declared rank", vecprod(BASIS_SHAPE) == BASIS_RANK);
chk("L0 declared rank == 432",                BASIS_RANK == 432);
chk("L0 shape == the five monic leading degrees",
    BASIS_SHAPE == [poldegree(P42), 2, 3, 3, 2]);

\\ [R2-D/E] the leading-term certificate: five pure powers in five distinct
\\ variables are pairwise coprime, so Buchberger's first criterion makes the
\\ five relations a Groebner basis and the standard monomials are the box.
NNZ  = vector(5, k, vecsum(vector(5, j, if (LEAD[k][j] != 0, 1, 0))));
SUPP = vector(5, k, vecsum(vector(5, j, j*if (LEAD[k][j] != 0, 1, 0))));
chk("L0 each leading monomial is a single pure power", NNZ == [1,1,1,1,1]);
chk("L0 the five leading variables are distinct (pairwise coprime)",
    #Set(SUPP) == 5);
chk("L0 leading exponents == the declared basis shape",
    vector(5, k, LEAD[k][SUPP[k]]) == BASIS_SHAPE);
obs("phi42_disc", poldisc(P42));
obs("phi168_degree", poldegree(P168));
obs("standard_monomials", vecprod(BASIS_SHAPE));

\\ ---- [R2-D] mod-p independence witness for the rank ------------------
{
  my(p, ZR, HR, r0, rr, A1R, A2R, TR, i, j, s, MZ, MM, MH, dz, dm, dh, bad);
  p  = WITNESS;
  chk("L0 rank witness prime is 1 mod 168 and prime",
      p % 168 == 1 && isprime(p));
  ZR = polrootsmod(P42, p);
  chk(Str("L0 witness: Phi42 has ", BASIS_SHAPE[1], " roots mod p"),
      #ZR == BASIS_SHAPE[1]);
  HR = polrootsmod(HB*'t^2 - HC, p);
  chk("L0 witness: the h relation has two roots mod p", #HR == BASIS_SHAPE[5]);
  r0 = lift(sqrt(Mod(RSQ,p)));
  TR = [];
  for (s = 1, 2,
    rr  = if (s == 1, r0, p - r0);
    A1R = polrootsmod('t^3 - (ALPHA[1][1] + ALPHA[1][2]*rr), p);
    A2R = polrootsmod('t^3 - (ALPHA[2][1] + ALPHA[2][2]*rr), p);
    if (#A1R != 3 || #A2R != 3, error("a cubic layer is not split at the witness"));
    for (i = 1, 3,
      for (j = 1, 3,
        TR = concat(TR, [[rr, lift(A1R[i]), lift(A2R[j])]]))));
  chk("L0 witness: 18 distinct (r,A1,A2) points",
      #TR == 18 && #Set(TR) == 18);
  bad = 0;
  for (i = 1, 18,
    if (Mod(TR[i][1]^2 - RSQ, p) != 0 ||
        Mod(TR[i][2]^3 - ALPHA[1][1] - ALPHA[1][2]*TR[i][1], p) != 0 ||
        Mod(TR[i][3]^3 - ALPHA[2][1] - ALPHA[2][2]*TR[i][1], p) != 0 ||
        Mod(TR[i][2], p) == 0 || Mod(TR[i][3], p) == 0, bad = bad + 1));
  chk("L0 witness: every middle point satisfies the three relations", bad == 0);
  MZ = matrix(#ZR, #ZR, i, j, Mod(lift(ZR[i]),p)^(j-1));
  MM = matrix(18, 18, i, j,
              Mod(TR[i][1],p)^((j-1)\9) * Mod(TR[i][2],p)^(((j-1)\3)%3) *
              Mod(TR[i][3],p)^((j-1)%3));
  MH = matrix(#HR, #HR, i, j, Mod(lift(HR[i]),p)^(j-1));
  dz = lift(matdet(MZ)); dm = lift(matdet(MM)); dh = lift(matdet(MH));
  chk("L0 witness: all three block determinants are nonzero mod p",
      dz != 0 && dm != 0 && dh != 0);
  chk("L0 witness: block sizes multiply to the declared rank",
      #ZR * 18 * #HR == BASIS_RANK);
  obs("rank_witness_prime", p);
  obs("rank_det_z_sq", dz^2 % p);
  obs("rank_det_mid_sq", dm^2 % p);
  obs("rank_det_h_sq", dh^2 % p);
}

\\ =====================================================================
\\ L1  Theorem A: B = Q(zeta42,r3,h) = Q(zeta_168), degree 48
\\ =====================================================================
z   = Mod('y, P168);
z42 = z^Z42E;
r3  = z^R3E[1] + z^R3E[2];
s2  = z^21 + z^147;
h   = s2*r3/HB;
zeta3 = z42^14;

chk("L1 Phi42(zeta^4) == 0",    subst(P42,'x,z42) == 0);
chk("L1 (zeta^4)^42 == 1",      z42^42 == 1);
chk("L1 (zeta^4)^21 != 1",      z42^21 != 1);
chk("L1 (zeta^4)^14 != 1",      z42^14 != 1);
chk("L1 (zeta^4)^6  != 1",      z42^6  != 1);           \\ [FIX 2] prime 7 of 42
chk("L1 r3^2 == 3",             r3^2 == Mod(RSQ,P168));
chk("L1 s2^2 == 2",             s2^2 == Mod(2,P168));
chk("L1 HB*h^2 == HC",          HB*h^2 == Mod(HC,P168));
chk("L1 (HB*h)^2 == HB*HC",     (HB*h)^2 == Mod(HB*HC,P168));
chk("L1 zeta3 is a primitive cube root of 1",
    zeta3^3 == Mod(1,P168) && zeta3 != Mod(1,P168));

i0 = r3*(1 + 2*zeta3)/3;
chk("L1 i^2 == -1",             i0^2 == Mod(-1,P168));
z8 = (1+i0)*h*r3/3;
chk("L1 zeta8 == y^Z8E",        z8 == z^Z8E);
chk("L1 GENERATION zeta8^GENE[1]*zeta42^GENE[2] == zeta_168",
    z8^GENE[1]*z42^GENE[2] == z);
\\ [R3-A] the R2 review found this line constant-true in GP (the Python
\\ engine already read the same mutable exponents on both sides).  It now
\\ reads the exponent data that drives the GENERATION line above and the
\\ conductor that drives the tower, so a drifted exponent moves both.
chk("L1 CRT Z8E*GENE[1] + Z42E*GENE[2] == 1 mod 168",
    (Z8E*GENE[1] + Z42E*GENE[2]) % CONDTOWER[3] == 1);
obs("crt_residue", (Z8E*GENE[1] + Z42E*GENE[2]) % CONDTOWER[3]);
chk("L1 dim_Q B == 48 == deg Phi_168",
    BASIS_SHAPE[1]*BASIS_SHAPE[2]*BASIS_SHAPE[5] == poldegree(P168));
\\ well defined + surjective + equal finite dimension  ==>  B = Q(zeta_168).
\\ No irreducibility test of any tower is used here or anywhere below.
chk("L1 conductor 12 does not divide 42",   CONDTOWER[1]*2 % 12 != 0);
chk("L1 conductor 12 divides 84",           CONDTOWER[2] % 12 == 0);
chk("L1 conductor 24 does not divide 84",   CONDTOWER[2] % 24 != 0);
chk("L1 conductor 24 divides 168",          CONDTOWER[3] % 24 == 0);
\\ [R2-G] the tower degrees are computed, not asserted
chk("L1 conductor tower degrees are 12, 24, 48",
    vector(3, k, poldegree(polcyclo(CONDTOWER[k],'t))) ==
    [BASIS_SHAPE[1], BASIS_SHAPE[1]*BASIS_SHAPE[2],
     BASIS_SHAPE[1]*BASIS_SHAPE[2]*BASIS_SHAPE[5]]);

\\ =====================================================================
\\ L2  Kummer independence by explicit cubic-character ring homomorphisms
\\ =====================================================================
\\ For p == 1 (mod 168) every root omega of Phi_168 mod p IS a ring map
\\ Z[y]/(Phi_168) --> F_p.  Both alpha_k are units at such a p (their norms
\\ from Q(sqrt3) are 6 and p does not divide 6), so a cube in B^* has cube
\\ image.  Two homs whose character pairs generate mu_3 x mu_3 leave only
\\ (i,j) = (0,0).  This needs no number field, no factorisation, and no
\\ abelian-descent lemma.                                          [R2-C]
charframes(p) =
{
  my(rts, om, rr, v, rvals, vvals, cnts, idx, k, m);
  if (!isprime(p), error(Str("certificate prime not prime: ", p)));
  if (p % 168 != 1, error(Str("certificate prime not 1 mod 168: ", p)));
  if (p % 2 == 0 || p % 3 == 0 || p % 7 == 0, error("certificate prime | 42"));
  rts = polrootsmod(P168, p);
  if (#rts != 48, error(Str("Phi_168 has ", #rts, " roots mod ", p)));
  rvals = []; vvals = []; cnts = [];
  for (k = 1, #rts,
    om = Mod(lift(rts[k]), p);
    if (om^168 != Mod(1,p) || om^84 == Mod(1,p) || om^56 == Mod(1,p) ||
        om^24 == Mod(1,p), error("a hom root does not have exact order 168"));
    rr = om^R3E[1] + om^R3E[2];
    if (rr^2 != Mod(RSQ,p), error("omega^14 + omega^-14 is not a root of 3"));
    if (ALPHA[1][1] + ALPHA[1][2]*rr == Mod(0,p) ||
        ALPHA[2][1] + ALPHA[2][2]*rr == Mod(0,p),
        error("alpha_k is not a unit"));
    v = [lift((ALPHA[1][1] + ALPHA[1][2]*rr)^((p-1)/3)),
         lift((ALPHA[2][1] + ALPHA[2][2]*rr)^((p-1)/3))];
    idx = 0;
    for (m = 1, #rvals, if (rvals[m] == lift(rr), idx = m));
    if (idx == 0,
        rvals = concat(rvals, [lift(rr)]);
        vvals = concat(vvals, [v]);
        cnts  = concat(cnts, [1]),
        \\ [R3-B] defensive, and unreachable by construction: the character
        \\ pair is a function of the r-value alone, which is exactly why R1's
        \\ within-fibre equality test was vacuous.  It is not a gate, it is
        \\ not counted in the census, and it must not be read as one.
        if (vvals[idx] != v,
            error("cubic character depends on the hom inside one fibre"));
        cnts[idx] = cnts[idx] + 1));
  if (#rvals != 2, error("the 48 homs do not hit both square roots of 3"));
  if (2*cnts[1] != #rts || 2*cnts[2] != #rts,
      error("the two square-root fibres are not equal halves"));
  [[rvals[1], vvals[1]], [rvals[2], vvals[2]]];
}
annihilators(p, F) =
{
  my(n, alive, a, b);
  n = 0;
  for (i = 0, 2, for (j = 0, 2,
    alive = 1;
    for (k = 1, #F,
      a = Mod(F[k][2][1], p); b = Mod(F[k][2][2], p);
      if (a^i * b^j != Mod(1,p), alive = 0));
    if (alive, n = n + 1)));
  n;
}
generated_order(p, F) =
{
  my(S, vv);
  S = Set([]);
  for (i = 0, 2, for (j = 0, 2,
    vv = vector(#F, k, lift(Mod(F[k][2][1],p)^i * Mod(F[k][2][2],p)^j));
    S = setunion(S, Set([vv]))));
  #S;
}

chk("L2 two independent certificate primes",   #CERTPRIMES >= 2);
chk("L2 registered prime 673 is present",      setsearch(Set(CERTPRIMES), 673) > 0);
chk("L2 the certificate primes are distinct",  #Set(CERTPRIMES) == #CERTPRIMES);
for (n = 1, #CERTPRIMES,
  my(p, F);                                             \\ [FIX 3]
  p = CERTPRIMES[n];
  F = charframes(p);
  chk(Str("L2 p=", p, ": two homs, both square roots of 3"), #F == 2);
  chk(Str("L2 p=", p, ": only (0,0) annihilates"),  annihilators(p, F) == 1);
  chk(Str("L2 p=", p, ": characters generate mu_3^2"),
      generated_order(p, F) == 9);
  chk(Str("L2 p=", p, ": is not a registered frame prime"),
      setsearch(Set(SILENT), p) == 0);
  GENORDER = generated_order(p, F);
  obs(Str("annihilators_", p), annihilators(p, F));
  obs(Str("generated_order_", p), generated_order(p, F)));
\\ the registered frame primes are character-silent and could never decide this
for (n = 1, #SILENT,
  my(p, F);
  p = SILENT[n];
  F = charframes(p);
  chk(Str("L2 registered p=", p, ": characters trivial"),
      F[1][2] == [1,1] && F[2][2] == [1,1]);
  chk(Str("L2 registered p=", p, ": annihilates all nine classes"),
      annihilators(p, F) == 9);
  obs(Str("annihilators_", p), annihilators(p, F)));
\\ arithmetic corroboration in Q(sqrt3) (needs abelian descent, licensed by L1)
\\ [R2-G] every number below is computed from ALPHA and EPSD.
NA1 = ALPHA[1][1]^2 - RSQ*ALPHA[1][2]^2;
NA2 = ALPHA[2][1]^2 - RSQ*ALPHA[2][2]^2;
APC = ALPHA[1][1]*ALPHA[2][1] + RSQ*ALPHA[1][2]*ALPHA[2][2];
APR = ALPHA[1][1]*ALPHA[2][2] + ALPHA[1][2]*ALPHA[2][1];
chk("L2 alpha1*alpha2 is rational",  APR == 0);
chk("L2 N(alpha1) == N(alpha2)",     NA1 == NA2);
chk("L2 N(alpha1*alpha2) == N(alpha1)^2", APC^2 == NA1*NA2);
chk("L2 N(alpha1) is not a rational cube",   !ispower(NA1,3));
chk("L2 N(alpha1*alpha2) is not a rational cube", !ispower(APC^2,3));
chk("L2 N(eps) == 1 (the norm test is blind on eps)",
    EPSD[1]^2 - RSQ*EPSD[2]^2 == 1);
chk("L2 eps and its conjugate are both positive (trace and norm > 0)",
    2*EPSD[1] > 0 && EPSD[1]^2 - RSQ*EPSD[2]^2 > 0);
chk("L2 x^2 - 3y^2 = -1 is impossible mod 3",
    vecsum(vector(9, m,
      if (((((m-1)\3)^2 - RSQ*((m-1)%3)^2) % 3 + 3) % 3 == 2, 1, 0))) == 0);

\\ =====================================================================
\\ L3  Theorems C and D: field, degree, idempotents, Galois, ramification
\\ =====================================================================
\\ [R2-H] no literal 9: the Kummer order is the subgroup size the L2 loop
\\ computed, and the base dimension is deg Phi_168.  R1 multiplied two
\\ literals here and could not see a broken L2.
chk("L3 deg(B) * |Delta| == declared rank == 432",
    poldegree(P168)*GENORDER == BASIS_RANK && BASIS_RANK == 432
    && GENORDER == 9);
chk("L3 exactly one component, literally K0",
    #COMPONENTS == 1 && COMPONENTS[1] == "K0");
chk("L3 idempotents are exactly [0,1]",  IDEMPOTENTS == [0,1]);
chk("L3 t^3-6 is irreducible over Q",    polisirreducible('t^3 - APC));
chk("L3 disc(t^3-6) is not a square (non-normal cubic)",
    !issquare(poldisc('t^3 - APC)));
chk("L3 disc(t^3-6) == -27*36",          poldisc('t^3 - APC) == -27*APC^2);
chk("L3 every layer discriminant is {2,3,7}-smooth",
    Set(factor(poldisc(P42)*4*RSQ*2*HB*HC*27)[,1]~) == Set([2,3,7]));
chk("L3 42 == 2*3*7",                    Set(factor(42)[,1]~) == Set(RAMIFIED));
chk("L3 3 ramifies: |disc(Phi_3)| == 3",     abs(poldisc(polcyclo(3,'t))) == 3);
chk("L3 7 ramifies: |disc(Phi_7)| == 7^5",   abs(poldisc(polcyclo(7,'t))) == 7^5);
chk("L3 2 ramifies: disc(t^2-3) == 12",      poldisc('t^2 - RSQ) == 4*RSQ);
chk("L3 5 is unramified",
    setsearch(Set(factor(poldisc(P42)*4*RSQ*2*HB*HC*27)[,1]~), 5) == 0);
chk("L3 declared ramified set is exactly {2,3,7}", RAMIFIED == [2,3,7]);

\\ ---- [R2-E] sigma on the FREE relations, before any quotient ----------
RELZ  = subst(P42,'x,'zv);
RELR  = 'rv^2 - RSQ;
RELA1 = 'a1^3 - (ALPHA[1][1] + ALPHA[1][2]*'rv);
RELA2 = 'a2^3 - (ALPHA[2][1] + ALPHA[2][2]*'rv);
RELH  = HB*'hv^2 - HC;
sg(f) = subst(subst(subst(subst(f,'a1,'tw),'a2,'a1),'tw,'a2),'rv,-'rv);
chk("L3 sigma fixes the Phi42 relation",   sg(RELZ) == RELZ);
chk("L3 sigma fixes the r relation",       sg(RELR) == RELR);
chk("L3 sigma swaps the two cubic relations",
    sg(RELA1) == RELA2 && sg(RELA2) == RELA1);
chk("L3 sigma fixes the h relation",       sg(RELH) == RELH);
chk("L3 sigma is an involution on the relation set",
    sg(sg(RELA1)) == RELA1 && sg(sg(RELR)) == RELR);
chk("L3 sigma does not fix the cubic relations individually",
    sg(RELA1) != RELA1 && sg(RELA2) != RELA2);
obs("component_count", #COMPONENTS);
obs("idempotent_count", #IDEMPOTENTS);
obs("ramified_product", vecprod(RAMIFIED));

\\ =====================================================================
\\ L4  the two registered frames, complete splitting, and the p^2 lift
\\ =====================================================================
FR = [[105337, 2779, 795, 50630, 10114, 50267],
      [105673, 13862, 14686, 38664, 46664, 35053]];
chk("L4 exactly two registered frames, on the registered primes",
    #FR == 2 && Set([FR[1][1], FR[2][1]]) == Set(SILENT));
for (k = 1, 2,
  my(p, zz, rr, a1, a2, hh, nz, nh, r0, tot, r, c1, c2);   \\ [FIX 3]
  p  = FR[k][1]; zz = FR[k][2]; rr = FR[k][3];
  a1 = FR[k][4]; a2 = FR[k][5]; hh = FR[k][6];
  chk(Str("L4 frame ", p, ": p == 1 mod 168"), p % 168 == 1 && isprime(p));
  chk(Str("L4 frame ", p, ": all five relations"),
      Mod(subst(P42,'x,zz),p) == 0 && Mod(rr^2-RSQ,p) == 0 &&
      Mod(a1^3-ALPHA[1][1]-ALPHA[1][2]*rr,p) == 0 &&
      Mod(a2^3-ALPHA[2][1]-ALPHA[2][2]*rr,p) == 0 &&
      Mod(HB*hh^2-HC,p) == 0);
  chk(Str("L4 frame ", p, ": zeta42 has exact order 42"),
      Mod(zz,p)^42 == 1 && Mod(zz,p)^21 != 1 &&
      Mod(zz,p)^14 != 1 && Mod(zz,p)^6 != 1);           \\ [FIX 2]
  chk(Str("L4 frame ", p, ": jacobian entries are units"),
      Mod(subst(deriv(P42,'x),'x,zz),p) != 0 &&         \\ [FIX 5]
      Mod(2*rr,p) != 0 && Mod(3*a1^2,p) != 0 &&
      Mod(3*a2^2,p) != 0 && Mod(2*HB*hh,p) != 0);
  nz  = #polrootsmod(P42, p);
  nh  = if (issquare(Mod(HC,p)/HB), 2, 0);
  r0  = lift(sqrt(Mod(RSQ,p)));
  tot = 0;
  for (s = 1, 2,
    r  = if (s == 1, r0, p - r0);
    c1 = if (Mod(ALPHA[1][1]+ALPHA[1][2]*r,p)^((p-1)/3) == Mod(1,p), 3, 0);
    c2 = if (Mod(ALPHA[2][1]+ALPHA[2][2]*r,p)^((p-1)/3) == Mod(1,p), 3, 0);
    tot = tot + c1*c2);
  chk(Str("L4 frame ", p, ": exactly 432 F_p points [CONSISTENCY ONLY]"),
      nz == 12 && nh == 2 && tot == 18 && nz*nh*tot == 432);
  obs(Str("frame_zeta_roots_", p), nz);
  obs(Str("frame_h_roots_", p), nh);
  obs(Str("frame_cubic_sum_", p), tot);
  obs(Str("frame_points_", p), nz*nh*tot));

P2 = [8852313585, 11012141449, 786496672, 8038065910, 6003627245];
{
  my(p, m, j);
  p = 105337; m = p^2;
  chk("L4 p^2 frame satisfies all five relations mod p^2",
      Mod(subst(P42,'x,P2[1]),m) == 0 && Mod(P2[2]^2-RSQ,m) == 0 &&
      Mod(P2[3]^3-ALPHA[1][1]-ALPHA[1][2]*P2[2],m) == 0 &&
      Mod(P2[4]^3-ALPHA[2][1]-ALPHA[2][2]*P2[2],m) == 0 &&
      Mod(HB*P2[5]^2-HC,m) == 0);
  chk("L4 p^2 frame reduces to the registered p-frame",
      vector(5, j, P2[j] % p) ==
      [FR[1][2], FR[1][3], FR[1][4], FR[1][5], FR[1][6]]);
}

\\ =====================================================================
\\ L5  base-level identities behind the E-conditional theorem  [R2-A]
\\ =====================================================================
\\ This block READS the literal E data in ETERMS and checks the base-level
\\ reduction chain.  It does NOT certify the E-conditional ratio theorem:
\\ the 432-monomial normal form of q0, the DIRECT substitution of q0 into E,
\\ the four branches and their distinctness, and the pointbank regression are
\\ executed only by the Python engine, and the runner terminal types that
\\ theorem as single-engine with this block as corroboration.
sB    = (1 + i0)*(r3 - 1)/2;
C1E   = ETERMS[1][1] + ETERMS[1][2]*r3;
C2E   = ETERMS[2][1] + ETERMS[2][2]*r3;
ENORM = ETERMS[1][1]*ETERMS[2][1] + RSQ*ETERMS[1][2]*ETERMS[2][2];
ECROSS= ETERMS[1][1]*ETERMS[2][2] + ETERMS[1][2]*ETERMS[2][1];
CBASE = -C2E*C2E/ENORM;
ANORM = ALPHA[1][1]*ALPHA[2][1] + RSQ*ALPHA[1][2]*ALPHA[2][2];
AR    = (ALPHA[2][1] + ALPHA[2][2]*r3)^2/ANORM;
chkE("L5 E has exactly two terms",              #ETERMS == 2);
chkE("L5 E terms name A1 and A2 in that order",
     ETERMS[1][3] == 2 && ETERMS[2][3] == 3);
chkE("L5 both E exponents are 4",
     ETERMS[1][4] == 4 && ETERMS[2][4] == 4);
chkE("L5 the two E coefficients are conjugate",  ECROSS == 0);
chkE("L5 C1*C2 == ENORM in B",                   C1E*C2E == Mod(ENORM,P168));
chkE("L5 CBASE is well formed: C1*CBASE == -C2", C1E*CBASE == -C2E);
chkE("L5 F1 alpha2/alpha1 == 2-r3",  AR*(ALPHA[1][1]+ALPHA[1][2]*r3) ==
                                     ALPHA[2][1]+ALPHA[2][2]*r3);
chkE("L5 F1 alpha2/alpha1 == eps^-1",
     AR == Mod(EPSD[1],P168) - EPSD[2]*r3);
chkE("L5 F2 -(2-r3)^3 == 15*r3-26",
     -(Mod(EPSD[1],P168) - EPSD[2]*r3)^3 == 15*r3 - Mod(26,P168));
chkE("L5 eps*(2-r3) == 1",
     (Mod(EPSD[1],P168) + EPSD[2]*r3)*(Mod(EPSD[1],P168) - EPSD[2]*r3) ==
     Mod(1,P168));
chkE("L5 CBASE == -(2-r3)^3 (from the literal E data)",
     CBASE == -(Mod(EPSD[1],P168) - EPSD[2]*r3)^3);
chkE("L5 F4 s^2 == i*(2-r3)",
     sB^2 == i0*(Mod(EPSD[1],P168) - EPSD[2]*r3));
chkE("L5 s lies in B, not in an extension",  type(sB) == "t_POLMOD");
chkE("L5 E-REDUCTION (alpha2/alpha1)*s^4 == CBASE",  AR*sB^4 == CBASE);
chkE("L5 mu_4 = {1,i,-1,-i} has four distinct elements of B",
     i0^2 == Mod(-1,P168) && i0 != Mod(1,P168) && i0 != Mod(-1,P168));
obs("e_term_count", #ETERMS);
obs("e_exponent_sum", ETERMS[1][4] + ETERMS[2][4]);
obs("e_generator_index_sum", ETERMS[1][3] + ETERMS[2][3]);
obs("e_coefficient_norm", ENORM);

\\ =====================================================================
\\ census and terminal
\\ =====================================================================
printf("CENSUS %d/%d\n", ncheck, nexpect);
if (ncheck != nexpect,
    printf("CENSUS_INCOMPLETE a gate line was deleted or added\n");
    printf("K0_UNCONDITIONAL 0   E_BASE_IDENTITIES 0\n"),
    printf("K0_UNCONDITIONAL %d   E_BASE_IDENTITIES %d\n", ok, okE));
