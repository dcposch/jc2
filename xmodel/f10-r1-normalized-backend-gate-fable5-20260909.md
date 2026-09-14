# F10 r1 normalized backend: first static implementation gate (Fable 5.1)

2026-09-09. Launch 19:18:05 UTC; controlling stop 19:43:00 UTC (earlier of
19:43:00 and launch+25 min), never reset. Static text review only: no
subprocess, CAS, arithmetic script, import, compile or test of any size; no
network, AWS, SSH, /proc or agents. Owned outputs: this file and
box/f10-r1-normalized-backend-gate-fable5-20260909/ only.

## Custody

All 23 ordered SHA256 values matched the charged inputs before any body read
(sha256sum over /tmp/jc2-lane.d8KkiG/inputs; the list is reproduced in
box/f10-r1-normalized-backend-gate-fable5-20260909/custody.txt). exact.json
was used as hash 168bdfd3..., 88634 bytes and key schema only; no coefficient
was dumped or evaluated.

Read WHOLE: the charged report, algebra.py (170 lines), generator.py (136),
checker.py (246), execution_gate.py (72), DISABLED.json, DELTA.md,
VALIDATION.md, READ-SCOPE.md, artifact.json, retained_transformer.py (232),
retained_checker.py (328). Accepted parents were consulted only by grep at the
named lines below; no accepted lemma is re-reviewed. Disclosure: one shell
command at 19:32 UTC accidentally contained two no-op python3 invocations
(empty stdin, and -c pass); they imported nothing from the packet and did
no arithmetic, but they were subprocesses and are recorded here.

## Verdict summary

A CONFIRMED, B CONFIRMED, C CONFIRMED (two minor inventory gaps named), D
CONFIRMED (enforced/upstream split named), E CONFIRMED (helper identity is
documentary; minimal batch named). No REFUTED item. No dependent runtime is
stopped by this gate; nothing here authorizes one. All defects below are
real line-level observations; none is a generic hardening request.

## A. Exact full-B rational arithmetic: CONFIRMED

- Modulus: algebra.py:52-54 builds p=24R^2+(280-1344v)LR+49EL^2 densely;
  checker.py:28-31 rebuilds it as a sparse dict with its own plus/times and
  requires max degree 7; checker.py:73 compares the literal 8-entry string
  list. Two constructions, same accepted formula (retained_transformer.py:66).
- Coefficient wires: algebra.py:127-128 emits [exponents, num-string,
  den-string]; checker.py:51-64 (Flat.read) re-parses with str(int(n))==n,
  gcd, den>0, nonzero, strictly sorted keys, e[6]<7 and e[3]==0 for width 7.
  Fraction is the only number type; checker.py:65-69 rejects float in both
  artifacts. No native-number roundtrip: exponents are ints, coefficients are
  strings (generator.py:106-121).
- Signed s exists only in the base Ring.read (algebra.py:138, axis 3 exempt)
  which generator.py never calls, and in the checker's own mapping shifts
  (checker.py:97-98). Emitted normalized wires cannot carry s (checker.py:58).
- Generator reduction is dense grouping by non-v exponent then dd(...,monic)
  (algebra.py:81-91); checker reduction is monomial long reduction by the
  sparse lower table (checker.py:33-44). Powers: binary (algebra.py:92-99)
  versus repeated multiplication (checker.py:45-49). Distinct as claimed.
- Divisions: Q only (dd leading coefficient algebra.py:37, dxg normalisation
  :49, eigenvalues j-3i generator.py:41-43, 1/(4i+1) :24, 1/i :79, 1/12 :83,
  1/112 :16, fixed rationals in h4 :89). B-inverses only via Ring.inv
  (algebra.py:100-105: gcd==1 required, then a*out==1 checked) on L, w, f5,
  a, det1, det2, and Ring.pair (:106-112: ideal (a,b,p) gcd 1, then the
  literal a*l+b*r==1 checked). Nothing else divides in B. Flat.inv raises.
- Adjugate indexing (algebra.py:162-167): out[i][j]=invdet*(-1)^(i+j)*det of
  M with row j and column i removed, which is adj(M)[i][j]/det; correct, and
  M*out==I is asserted for every entry before return. Determinant: Laplace
  on row 0 (:158-160). The checker uses the explicit six-permutation sum
  (checker.py:126), independent.
- Shared surface actually used by the checker: c, atom, add, scale, sub, diff,
  coeff, compose, at_z_s2, bracket, eq, wire, matvec, require, Q. compose and
  bracket dispatch to the overridden Flat.mul/pow, so only the trivial
  linear helpers and diff/coeff are truly shared. A diff or coeff bug would
  not be self-cancelling: all 19 low rows are bound to the original rows
  (checker.py:185-187) which do not pass through diff.
- Shared literal not named by the report: the f5 five-partition expression is
  byte-for-byte the same in generator.py:17 and checker.py:81. The accepted
  retained_transformer.py:88-100 used the falling-factorial route instead; the
  new generator dropped it. f5 is therefore bound only by the identity
  f5*f5inv==1 and the accepted literal, not by two routes.
- Ring.dense (algebra.py:69-71) silently ignores v-exponents >=7; harmless
  because every input is a reduced product and inv/pair re-check the product.

## B. Source maps: CONFIRMED

- Leading recurrence generator.py:19-24: from 4CD'-7C'D=-t^7 the t^n
  coefficient is (4n-29)D_(n-2)+(4n-18)F D_(n-1)+(4n-7)H D_n+4(n+1)a D_(n+1).
  With n=7-i this is -(4i+1)D_(5-i)=(4i-10)F D_(6-i)+(4i-21)H D_(7-i)
  +(4i-32)a D_(8-i): exactly the three multipliers and the -1/(4i+1) scale.
  D_5=1, D_0==b is checked (:25) and the whole ODE is re-asserted (:27) and
  re-asserted independently in checker.py:88 and bound to the actual leading
  S-band of B (checker.py:170).
- Target: generator.py:33-34 uses Pi=z t-U t^2+S t^3 and
  -(E t Pi + t Pi^2); checker.py:171-173 recomputes J=bracket+E t Pi+t Pi^2.
  This is composition (11) without s^7 and U s^5 tau; those enter only as the
  E0/S0 and E1/S0 additions (checker.py:186), matching (16).
- Euler step generator.py:38: [t^(j+2)] bracket equals (j+3)k'B_(j+3)
  +(j+2)h'B_(j+2)+(j+1)f'B_(j+1)+jB_j-hB'_(j+2)-2fB'_(j+1)-3SB'_j, so the
  transposed right side and the eigenvalue j-3i on S^i are correct. Resonant
  slots (0,0) and (3,1) are hard failures if forced (:42) and otherwise
  absent, which is the zero gauge; checker.py:190 asserts all three gauges.
- Completed matrices: probes at unit vectors with z=0 (generator.py:52-66).
  By the weight grading (x1,y2,z3,S1,t1; U2,E4,D0 1,V0 2,V1 1,K1 3,K2 2,K3 1)
  row E1/S7 has weight 1 and E1/S6 weight 2, so z (weight 3) and products of
  unknowns cannot enter the extracted linear parts; the probes are exact, not
  an approximation. rho rows 4a[S^6]B0-7bK3 and 4a[S^5]B0-7bK2 match the
  accepted (9) and (13) of the first/second producers. Solves are (0,0,x)
  and (-c2,y) with q=-U, V0=l-Fq (generator.py:62,69; checker.py:134-135).
- Third map: e_i=[t^i]C^-2 by series inversion with e_0=a^-2
  (generator.py:72-74); lambda3 = F[t^6](C^2 I_r)-1/2[t^5](C^2 I_r) with
  I_r=sum(r0 e_(i-1)+r1 e_(i-2))t^i/i through i=6 (:75-81). This is literally
  the accepted third gate formula (f10-r1-third-band-gate line 42). c3 is the
  actual rows at low2 with z kept (:70), not a shifted D formula. l3*h3==1
  is asserted (:85). Signs: rows become -l3[1]Phi3 and +l3[0]Phi3 with
  Phi3=h3[0]c3[1]-h3[1]c3[0] (:87,:94), verified by direct expansion.
- Fourth map: l4=pair(h4) (generator.py:90) inverts neither entry.
  d=lambda'-lambda with d.h=0 and lambda.h=1 gives d_A=B(lambda_B d_A
  -lambda_A d_B)=tB and d_B=-tA over any commutative ring, so
  E'-E=-t(Bc0-Ac1)=-t Phi4 with Phi4=h4[1]c4[0]-h4[0]c4[1] (:92). DELTA.md
  lines 28-39 state exactly this. final=make(low4) (:92) regenerates A, B,
  Pi, J, forcing; G, H0, H1 are read from final (:95-96). Nothing is
  asserted byte-identical to the Gram representatives.
- Not confirmable from charged text: the literal h3 (generator.py:83-84) and
  h4 (:89) coefficients (the fourth producer grep shows no 44/15, 8/15).
  They are runtime-enforced: checker.py:146 rebuilds each column as the
  probe difference of the original source rows and requires equality.

## C. Checker binding of every original slot: CONFIRMED

- Parameter map checker.py:95-98 is [U/s,E/s^3,D0/s,F/s,V0/s^2,V1/s^2,
  H/s^2,K1/s^3,K2/s^3,K3/s^3,a/s^3,w f5 s^8,S] in the original variable
  order (checker.py:72), after z->s^2 on the map values. Row scale s^(7-h)
  (:104), A_j scale s^(3-j), B_j scale s^(5-j) (:160), forcing s^(5-j)
  (:180), B0 in rho s^5 (:106), a s^-3 and b s^-5 (:194-195). These follow
  from Ahat=s^3 A(t/s), Bhat=s^5 B(t/s), bracket = s^7 [A,B](t/s).
- Injection: eqz compares Laurent images; emitted wires have no s (:58), so a
  hidden z-s^2 multiple cannot pass. No s=1 anywhere.
- All 20 slots: ids asserted on both artifacts (:100-101); all 19 low rows
  bound including E1/S8 and E0/S9 (:181-187) with the unsquared additions
  U s^5 and s^7 at S^0 (:186, precedence correct); guard (:188,:196).
  Zero coefficient slots (:165-168) both as projections and as original slot
  substitutions. A/B whole coefficients (:160), envelopes (:161,:175),
  weights (:164), gauges (:189-190), tops and restoration (:191-195),
  scales (:102).
- Completed matrices bound to source rows and original B0 (:113-121), both
  inverses as identities (:125), determinants literal and unit (:126-128),
  backmaps (:131,:135), preserved maps (:136,:148-149), affine forcing and
  columns (:145-146), left inverses (:142), eliminations (:147),
  compatibilities (:151), five whole forcings (:180).
- Producer-supplied objects are never accepted as expected sides without an
  anchor: Jhat, Pi, G, H0, H1 are compared to the checker's own J from
  source-bound A/B; Phi3/Phi4 to source-bound columns and forcings.
- Gap C1 (minor): data['c2'] length is not inventoried (checker.py:132-135).
  zip at :133 would truncate an oversized list; both used entries are still
  bound, and a short list fails at :135 with IndexError, not silently.
- Gap C2 (coverage note): original['residuals'] and original['resonances']
  are not read by the new checker; rows cover residuals slot-wise, and the
  three gauge projections cover resonances. Not a defect, but the report's
  "all original residual slots" means rows, not the residual polynomials.

## D. Bracket, Pi, bands, poles, projections: CONFIRMED

Enforced by checker.py: full J (:173-174), t-envelope <=7 (:175), bands
2..7 identically zero (:176), bands 0,1 bound row-wise to source (:187),
Pi (:172), negative part of the direct inverse S=pZ^3-zZ^2+UZ, tau=Z^-1
(:200-211, only i<j terms, all negative monomials collected, inventory
guard then total vanishing), removed rows (:213) and both compatibility
pairs (:216), nine G projections (:217-219), H0/H1 (:220), weights and
s/S/t-freedom (:221-224). The pole inventory (:199) only labels error
messages; the enforced claim is that the whole negative part is zero.

Accepted upstream, not enforced here: that the normalized system is
equivalent to the original (composition (16)); that det1, det2 are units
and that the columns are unimodular (only tested, not proved, by inv/pair);
that the original exact.json rows themselves are correct (the checker binds
to them, it does not re-derive them); that the third lambda is the accepted
representative (any left inverse passes :142). No source-degree expansion,
nonzero, independence, rank, ideal or endpoint claim is made by the code.

## E. Entrypoint authority, pins, validation plan: CONFIRMED

- Both entrypoints call authorize before importing algebra (generator.py:125
  then :13 inside generate; checker.py:232 then :13 inside verify). Pins:
  original SOURCE hash and registration (generator.py:128, checker.py:235,
  :239), algebra.py and generator.py registration (:130; :236-237), artifact
  hash (:239), producer binding via implementation_sha256 (:241). Outputs
  are created with mode 'x' at the registered argv paths.
- DISABLED.json has enabled:false and empty file_sha256, so
  execution_gate.py:19 refuses. Helper hash cbfe55ff... equals the charged
  copy; neither charged composition gate records the helper hash, so
  "byte-identical accepted helper" is a documentary claim of the report.
- Provenance note: the artifact records only generator.py's hash, not the
  build-time algebra.py hash. Validity is unaffected because the checker
  re-verifies every object, but two builds with different algebra.py would be
  indistinguishable from the artifact alone.
- VALIDATION.md names the positive pair and twelve control groups and
  correctly refuses to call early-binding failures late bracket/pole
  coverage (items 10, 11). It does not name a minimal subset. A minimal
  meaningful batch is: the positive pair, then groups 3 (matrix entry),
  4 (shifted c3), 6 (Pi sign, reaching checker.py:172), 7 (H0/H1, :220)
  and 12 (precision). Late pole path (:200-211) can only be exercised
  positively, as the plan says. Static acceptance here permits ROOT only to
  consider a separately registered bounded validation; no syntax success,
  artifact, resource estimate or solver authority is implied.

## Defects and OPEN quantities

Defects (none blocking): C1 c2 length not inventoried; A f5 literal shared
between generator and checker; E artifact lacks a backend hash. Smallest
repairs, not applied: require len(c2)==2 at checker.py:132; restore the
falling-factorial f5 route in the generator; add backend_sha256 to the
artifact and check it at checker.py:241.

No new OPEN identifier is created. Pending quantities remain the two named
by the producer: one bounded runtime validation (positive pair plus the
five groups above, each rejection observed at its named line) under ROOT's
separately registered authority, and nothing else. Own-only collision check
result is recorded under COLLISIONS below.

## COLLISIONS

status: EMPTY

- NONE - this report and its box were absent at launch; own-only
  publication. Scan at 19:32 UTC found three non-owned items carrying the
  gate name, none a competing report: the harness files
  xmodel/f10-r1-normalized-backend-gate-fable5-20260909.log and .run.v2, and
  box/f10-r1-normalized-backend-gate-20260909/root-invite.prompt.md (a ROOT
  invite prompt). None was read, written or relied on.

<!-- BODY-END -->
