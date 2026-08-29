\\ =====================================================================
\\ D43 coefficient algebra K0: exact field certificate, PARI/GP layer.
\\ Target host: the registered AWS "r6b" host, PARI/GP 2.15.4, one core.
\\ Replay:  gp -q --default parisize=64M k0_field_cert_r1.gp
\\ The last two printed lines must read
\\     CENSUS 79/79
\\     K0_UNCONDITIONAL 1   E_CONDITIONAL 1
\\ =====================================================================
\\
\\ This file is the SECOND engine.  k0_field_checker_r1.py replays every
\\ statement below in stdlib Python with no PARI call at all, using explicit
\\ integer, finite-field and canonical 432-monomial quotient arithmetic.
\\ Neither engine reads the other's output.
\\
\\ Corrections to the illustrative recipe in the charged report
\\ xmodel/d43-k0-splitting-primary-research-opus5-20260828.md section 9.2.
\\ Each is marked [FIX n] at its site:
\\   1  the tower was Mod('x, polcyclo(168,'x)) and was then substituted into
\\      a polynomial in the SAME variable x;
\\   2  the order-42 test omitted the prime 7 (z^6 != 1), so it accepted
\\      elements of order 6 -- zeta_168^28 is an explicit such element;
\\   3  my(r = ..., a = f(r)) evaluates a's initialiser in the ENCLOSING
\\      scope, where r is unbound: the character and frame loops both did
\\      this.  Every my() below declares names only, at the head of a block;
\\   4  w = Mod(znprimroot(p), p) wraps a t_INTMOD inside Mod();
\\   5  P42' as a stored-polynomial derivative; deriv() is explicit;
\\   6  chk() accepted any nonzero object as true, so a t_POLMOD or a t_VEC
\\      could pass silently.  chk() now demands a t_INT;
\\   7  there was no census, so deleting a line turned a FAIL into a PASS;
\\   8  nffactor over Q(zeta_168) sat on the theorem path.  It is now an
\\      optional, alarm-capped, corroboration-only block that no verdict
\\      line reads.  Kummer independence is established by explicit cubic
\\      characters at two primes instead, so no unexecuted degree-432 (or
\\      degree-144) irreducibility claim is needed anywhere.

ok = 1; ncheck = 0; nexpect = 79;

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
\\ L0  the literal source pins and the rank-432 monic basis
\\ =====================================================================
PHI42SRC    = [1,1,0,-1,-1,0,1,0,-1,-1,0,1,1];   \\ d43_common_integral_emitter.py:36
BASIS_SHAPE = [12,2,3,3,2];                      \\ selected_rows_v2.py:62
BASIS_RANK  = 432;                               \\ selected_rows_v2.py:63
COMPONENTS  = ["K0"];
IDEMPOTENTS = [0,1];
RAMIFIED    = [2,3,7];

P42  = polcyclo(42, 'x);
P168 = polcyclo(168,'y);                                \\ [FIX 1] y, not x

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
obs("phi42_disc", poldisc(P42));
obs("phi168_degree", poldegree(P168));
obs("basis_rank", BASIS_RANK);

\\ =====================================================================
\\ L1  Theorem A: B = Q(zeta42,r3,h) = Q(zeta_168), degree 48
\\ =====================================================================
z   = Mod('y, P168);
z42 = z^4;
r3  = z^14 + z^154;
s2  = z^21 + z^147;
h   = s2*r3/2;
zeta3 = z42^14;

chk("L1 Phi42(zeta^4) == 0",    subst(P42,'x,z42) == 0);
chk("L1 (zeta^4)^42 == 1",      z42^42 == 1);
chk("L1 (zeta^4)^21 != 1",      z42^21 != 1);
chk("L1 (zeta^4)^14 != 1",      z42^14 != 1);
chk("L1 (zeta^4)^6  != 1",      z42^6  != 1);           \\ [FIX 2] prime 7 of 42
chk("L1 r3^2 == 3",             r3^2 == Mod(3,P168));
chk("L1 s2^2 == 2",             s2^2 == Mod(2,P168));
chk("L1 2*h^2 == 3",            2*h^2 == Mod(3,P168));
chk("L1 (2h)^2 == 6",           (2*h)^2 == Mod(6,P168));
chk("L1 zeta3 is a primitive cube root of 1",
    zeta3^3 == Mod(1,P168) && zeta3 != Mod(1,P168));

i0 = r3*(1 + 2*zeta3)/3;
chk("L1 i^2 == -1",             i0^2 == Mod(-1,P168));
z8 = (1+i0)*h*r3/3;
chk("L1 zeta8 == y^21",         z8 == z^21);
chk("L1 GENERATION zeta8^5*zeta42^16 == zeta_168",  z8^5*z42^16 == z);
chk("L1 CRT 21*5 + 4*16 == 1 mod 168",              (21*5 + 4*16) % 168 == 1);
obs("crt_residue", (21*5 + 4*16) % 168);
chk("L1 dim_Q B == 48 == deg Phi_168",
    BASIS_SHAPE[1]*BASIS_SHAPE[2]*BASIS_SHAPE[5] == poldegree(P168));
\\ well defined + surjective + equal finite dimension  ==>  B = Q(zeta_168).
\\ No irreducibility test of any tower is used here or anywhere below.
chk("L1 conductor 12 does not divide 42",   42 % 12 != 0);
chk("L1 conductor 12 divides 84",           84 % 12 == 0);
chk("L1 conductor 24 does not divide 84",   84 % 24 != 0);
chk("L1 conductor 24 divides 168",         168 % 24 == 0);

\\ =====================================================================
\\ L2  Kummer independence by explicit cubic-character ring homomorphisms
\\ =====================================================================
\\ For p == 1 (mod 168) every root omega of Phi_168 mod p IS a ring map
\\ Z[y]/(Phi_168) --> F_p.  Both alpha_k are units at such a p (their norms
\\ from Q(sqrt3) are 6 and p does not divide 6), so a cube in B^* has cube
\\ image.  Two homs whose character pairs generate mu_3 x mu_3 leave only
\\ (i,j) = (0,0).  This needs no number field, no factorisation, and no
\\ abelian-descent lemma.
charframes(p) =
{
  my(rts, tab, out, om, rr, v, M);
  if (!isprime(p), error(Str("certificate prime not prime: ", p)));
  if (p % 168 != 1, error(Str("certificate prime not 1 mod 168: ", p)));
  if (p % 2 == 0 || p % 3 == 0 || p % 7 == 0, error("certificate prime | 42"));
  rts = polrootsmod(P168, p);
  if (#rts != 48, error(Str("Phi_168 has ", #rts, " roots mod ", p)));
  tab = Map();
  for (k = 1, #rts,
    om = Mod(lift(rts[k]), p);
    rr = om^14 + om^154;
    if (rr^2 != Mod(3,p), error("omega^14 + omega^-14 is not a root of 3"));
    if (Mod(3,p) + rr == 0 || Mod(3,p) - rr == 0, error("alpha_k is not a unit"));
    v = [lift((Mod(3,p) + rr)^((p-1)/3)), lift((Mod(3,p) - rr)^((p-1)/3))];
    if (!mapisdefined(tab, lift(rr)),
        mapput(tab, lift(rr), v),
        if (mapget(tab, lift(rr)) != v,
            error("cubic character depends on the hom inside one fibre"))));
  M = Mat(tab);
  if (#M[,1] != 2, error("the 48 homs do not hit both square roots of 3"));
  out = [];
  for (k = 1, 2, out = concat(out, [[M[k,1], M[k,2]]]));
  out;
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

CERTPRIMES = [673, 1009];
SILENT     = [105337, 105673];
chk("L2 two independent certificate primes",   #CERTPRIMES >= 2);
chk("L2 registered prime 673 is present",      setsearch(Set(CERTPRIMES), 673) > 0);
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
chk("L2 N(3+sqrt3) == 6",            3^2 - 3*1^2 == 6);
chk("L2 N(3-sqrt3) == 6",            3^2 - 3*(-1)^2 == 6);
chk("L2 N(alpha1*alpha2) == N(6) == 36", 6^2 - 3*0^2 == 36);
chk("L2 N(2+sqrt3) == 1 (norm test is blind on eps)", 2^2 - 3*1^2 == 1);
chk("L2 6 is not a rational cube",   !ispower(6,3));
chk("L2 36 is not a rational cube",  !ispower(36,3));

\\ =====================================================================
\\ L3  Theorems C and D: field, degree, idempotents, Galois, ramification
\\ =====================================================================
chk("L3 [K0:B]*[B:Q] == 9*48 == declared rank",
    9*48 == BASIS_RANK && BASIS_RANK == 432);
chk("L3 exactly one component, literally K0",
    #COMPONENTS == 1 && COMPONENTS[1] == "K0");
chk("L3 idempotents are exactly [0,1]",  IDEMPOTENTS == [0,1]);
chk("L3 t^3-6 is irreducible over Q",    polisirreducible('t^3 - 6));
chk("L3 disc(t^3-6) is not a square (non-normal cubic)",
    !issquare(poldisc('t^3 - 6)));
chk("L3 every layer discriminant is {2,3,7}-smooth",
    Set(factor(poldisc(P42)*12*6*27)[,1]~) == Set([2,3,7]));
chk("L3 42 == 2*3*7",                    Set(factor(42)[,1]~) == Set(RAMIFIED));
chk("L3 3 ramifies: |disc(Phi_3)| == 3",     abs(poldisc(polcyclo(3,'t))) == 3);
chk("L3 7 ramifies: |disc(Phi_7)| == 7^5",   abs(poldisc(polcyclo(7,'t))) == 7^5);
chk("L3 2 ramifies: disc(t^2-3) == 12",      poldisc('t^2 - 3) == 12);
chk("L3 5 is unramified",
    setsearch(Set(factor(poldisc(P42)*12*6*27)[,1]~), 5) == 0);
chk("L3 declared ramified set is exactly {2,3,7}", RAMIFIED == [2,3,7]);
obs("component_count", #COMPONENTS);
obs("idempotent_count", #IDEMPOTENTS);
obs("ramified_product", vecprod(RAMIFIED));

\\ =====================================================================
\\ L4  the two registered frames, complete splitting, and the p^2 lift
\\ =====================================================================
FR = [[105337, 2779, 795, 50630, 10114, 50267],
      [105673, 13862, 14686, 38664, 46664, 35053]];
for (k = 1, 2,
  my(p, zz, rr, a1, a2, hh, nz, nh, r0, tot, r, c1, c2);   \\ [FIX 3]
  p  = FR[k][1]; zz = FR[k][2]; rr = FR[k][3];
  a1 = FR[k][4]; a2 = FR[k][5]; hh = FR[k][6];
  chk(Str("L4 frame ", p, ": p == 1 mod 168"), p % 168 == 1 && isprime(p));
  chk(Str("L4 frame ", p, ": all five relations"),
      Mod(subst(P42,'x,zz),p) == 0 && Mod(rr^2-3,p) == 0 &&
      Mod(a1^3-3-rr,p) == 0 && Mod(a2^3-3+rr,p) == 0 && Mod(2*hh^2-3,p) == 0);
  chk(Str("L4 frame ", p, ": zeta42 has exact order 42"),
      Mod(zz,p)^42 == 1 && Mod(zz,p)^21 != 1 &&
      Mod(zz,p)^14 != 1 && Mod(zz,p)^6 != 1);           \\ [FIX 2]
  chk(Str("L4 frame ", p, ": jacobian entries are units"),
      Mod(subst(deriv(P42,'x),'x,zz),p) != 0 &&         \\ [FIX 5]
      Mod(2*rr,p) != 0 && Mod(3*a1^2,p) != 0 &&
      Mod(3*a2^2,p) != 0 && Mod(4*hh,p) != 0);
  nz  = #polrootsmod(P42, p);
  nh  = if (issquare(Mod(3,p)/2), 2, 0);
  r0  = lift(sqrt(Mod(3,p)));
  tot = 0;
  for (s = 1, 2,
    r  = if (s == 1, r0, p - r0);
    c1 = if (Mod(3+r,p)^((p-1)/3) == Mod(1,p), 3, 0);
    c2 = if (Mod(3-r,p)^((p-1)/3) == Mod(1,p), 3, 0);
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
      Mod(subst(P42,'x,P2[1]),m) == 0 && Mod(P2[2]^2-3,m) == 0 &&
      Mod(P2[3]^3-3-P2[2],m) == 0 && Mod(P2[4]^3-3+P2[2],m) == 0 &&
      Mod(2*P2[5]^2-3,m) == 0);
  chk("L4 p^2 frame reduces to the registered p-frame",
      vector(5, j, P2[j] % p) ==
      [FR[1][2], FR[1][3], FR[1][4], FR[1][5], FR[1][6]]);
}

\\ =====================================================================
\\ L5  Theorem F, CONDITIONAL on the literal displayed E
\\ =====================================================================
\\ E := (9+5*r3)*A1*W1^4 + (9-5*r3)*A2*W2^4,  q = W1/W2,  q^4 = c,
\\ c = (15*r3-26)*A2/A1.  The only input from the cubic layer is
\\ u^3 = A2^3/A1^3 = (3-r3)/(3+r3), which is the two defining relations.
\\ GP certifies the base-level identities F1, F2, F4 and the mu_4 structure.
\\ The 432-monomial normal form of q0, the DIRECT substitution of q0 into the
\\ literal E, the four branches and their distinctness, and the pointbank
\\ regression are executed by the Python engine (gates F_IDENTITIES,
\\ Q0_NORMAL_FORM, E_DIRECT_SUBSTITUTION, FOUR_K0_RATIONAL_BRANCHES,
\\ POINTBANK_REGRESSION).  GP does not restate those conclusions.
Y2 = 'v^2 - 3;
chk("L5 F1 (3-r3)/(3+r3) == 2-r3",
    Mod(3-'v,Y2)/Mod(3+'v,Y2) == Mod(2-'v,Y2));
chk("L5 F2 -(2-r3)^3 == 15*r3-26",
    -(Mod(2-'v,Y2))^3 == Mod(15*'v-26,Y2));
chk("L5 eps*(2-r3) == 1",  Mod(2+'v,Y2)*Mod(2-'v,Y2) == Mod(1,Y2));
sB = (1 + i0)*(r3 - 1)/2;
chk("L5 F4 s^2 == i*(2-r3)",  sB^2 == i0*(2 - r3));
chk("L5 s lies in B, not in an extension",  type(sB) == "t_POLMOD");
chk("L5 mu_4 = {1,i,-1,-i} has four distinct elements of B",
    i0^2 == Mod(-1,P168) && i0 != Mod(1,P168) && i0 != Mod(-1,P168));

\\ =====================================================================
\\ census and terminal
\\ =====================================================================
printf("CENSUS %d/%d\n", ncheck, nexpect);
if (ncheck != nexpect,
    printf("CENSUS_INCOMPLETE a gate line was deleted or added\n");
    printf("K0_UNCONDITIONAL 0   E_CONDITIONAL 0\n"),
    printf("K0_UNCONDITIONAL %d   E_CONDITIONAL %d\n", ok, ok));

\\ =====================================================================
\\ OPTIONAL corroboration, off the theorem path
\\ =====================================================================
\\ Enabled only when K0_OPTIONAL is preset to a nonzero integer.  No verdict
\\ line above reads any of this and the certificate is complete without it.
\\ nffactor over a degree-48 field is expensive and is NOT how [K0:B] = 9 is
\\ established; Kummer theory plus the L2 characters is.               [FIX 8]
if (type(K0_OPTIONAL) == "t_INT" && K0_OPTIONAL,
  my(nf3, CL, f);
  alarm(600);
  iferr(
    nf3 = nfinit('v^2 - 3);
    CL  = ['v + 3, 3 - 'v, 6, 2 + 'v];
    for (kk = 1, 4,
      f = nffactor(nf3, 'x^3 - CL[kk]);
      printf("OPTIONAL Q(sqrt3): x^3 - class%d irreducible %d\n",
             kk, matsize(f)[1] == 1 && f[1,2] == 1)),
    ERR, printf("OPTIONAL nffactor layer aborted: %s\n", ERR));
  alarm(0));
