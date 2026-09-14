# FIRST Fable 5.1: mixed univariate actual code and instantiated algebra

Owner Fable 5.1 (claude-fable-5-1). Actual first action 2026-09-12 19:29:33 UTC;
own target absent at 19:36:18 UTC. Reserve 19:46 / HARD 19:50 UTC, never reset.
STATIC FIRST / MANUAL MATH AND TEXT / UNREVIEWED. No interpreter, CAS, import,
syntax, fixture, network or execution; inspected code was not run.

All thirteen snapshots in /tmp/jc2-lane.rgFLoW/inputs were hashed at 19:29:33 UTC
before any body read; every digest equalled the charged pin by basename
(COORDINATION 33cfa610..., reduction-root 7b8545a6..., septic-gate cff18a06...,
kernel-scalar f6fe0986..., scalar-unit-gate aa8b0148..., elimination-gate
2217dea3..., source-report 8a275441..., authority.py 1b7cc411..., produce.py
8aee305b..., check.py 1ab7f3b3..., CONTRACT 4bdb1b58..., VALIDATION 2fd6330f...,
template 32cc40bd...). Each was then read freshly WHOLE, COORDINATION first.
Nothing else was read. The 17zzd septic theorem, its automatic Y*d5 guard and
U-unitness on the whole algebra are imported at their existing scope.

## Verdict table

| Issue | Verdict |
|---|---|
| 1 old/new constants, linear elimination, ring map | CONFIRMED (hand-verified) |
| 2 recurrence vs finite sums, indices, F, degrees | CONFIRMED |
| 3 gcdex orientation, clearing, identity, exceptions | CONFIRMED |
| 4 DATA-only parser closes executable-certificate defect | CONFIRMED at source scope |
| 5 traced parser / A1+1 / (7t-12) controls | CONFIRMED branches; exit 1 shared |
| 6 guard-before-CAS, argv slot, fail-closed outputs | CONFIRMED narrowly; installed APIs GAP |

REFUTED: none. No scalar unit, source array, REG/model comparison, source zero,
all-F10 or JC2 consequence is established or claimed.

## 1. Instantiated old/new map: CONFIRMED

With tau=2-t: 1-tau=t-1, 1+tau=3-t, 2-3tau=3t-4, 2+tau=4-t, 3+tau=5-t,
4tau-3=5-4t. The checker's literal D, Kold (check.py 69-70) are byte-faithful to
the accepted 17zzd gate section A. Then D=12X^2-12(t-1)X+(3-t)(3t-4)=4U with
U=3X^2-3(t-1)X-(t-3)(3t-4)/4: CONFIRMED. Kold coefficients: X^2 840(t-1)(3-t)
=-840(t-3)(t-1); X^1 42(3-t)(4-t)(5-4t)=-42(t-3)(t-4)(4t-5); X^0
2(3t-4)(3-t)(4-t)(5-t)=-2(t-3)(t-4)(t-5)(3t-4); so Kold=-840V exactly with the
ROOT V (X/20 and /420 terms match after scaling by 840): CONFIRMED.

Linear elimination, recomputed termwise from the accepted d6,d7 cubics with
c_j=binomial(t,j): (t-2)c2=3c3 kills Y^2 in d7-(t-2)d6; the Y coefficient over
c3 is 3X^2+(3(t-3)-6(t-2))X+((t-3)(t-4)/4-(t-2)(t-3))=U; the Y^0 part over c3
has X^3 coefficient (t-3)-(t-2)=-1, X^2 -(t-3)(t-1), X^1 -(t-3)(t-4)(4t-5)/20,
X^0 (t-3)(t-4)(t-5)[(t-6)-7(t-2)]/840=-(t-3)(t-4)(t-5)(3t-4)/420, i.e. -V.
Also d6/c3=3Y^2/(t-2)+(6X+t-3)Y+K with K as displayed (c6/c3, 5c5/c3, 6c4/c3).
CONFIRMED; check.py 72 tests exactly this identity at run time.

Septic scaling: old S=245D^2E(V,-Kold/(210D)) and -Kold/(210D)=840V/(840U)=V/U,
the same substitution as Y=V/U. With E=120(t-2)d6/c3 (its Y^2 term 360 and its
Y term 120(t-2)(6X+t-3)=120tau(1+tau-6X)=beta are checked at check.py 75),
S=245*16*120*(t-2)U^2[3V^2/((t-2)U^2)+(6X+t-3)V/U+K]=470400(t-2)P=470400P0.
CONFIRMED. Degree: V^2 and (6X+t-3)VU have X-degree 6, only KU^2 reaches X^7,
coefficient 1*3^2=9, so LC(P0)=9(t-2); consistent with the old LC
-4233600tau=4233600(t-2) and 4233600/470400=9. CONFIRMED (check.py 82).
The old Q_nu=7E+(Kold+210DY)=840(t-2)d6/c3+840(UY-V)=840d7/c3, so (E,Q)=(d6,d7)
and the old unguarded algebra is Q[X,Y]/(d6,d7); U=D/4 is a unit there by the
imported whole-algebra 17zzd Bezout, hence Y=V/U and S_r=Q[X]/(P) with the
Y*d5 localization automatic. Remark, not a defect: gamma is derived from d6
(check.py 76) rather than from an old literal gamma; correctness of the ring
map needs only D and Kold, and the scaling check remains a genuine consistency
test. produce.py 11-14 match the ROOT compact U,V,K,P0 literally, with exact
sympy division (no float). Issue 1 CONFIRMED.

## 2. Recurrence, finite sums, indices, F and degrees: CONFIRMED

produce.py trunc: k a_k = sum_{j<=min(3,k)} ((s+1)j-k) phi_j a_{k-j} follows
from comparing u^{k-1} in phi A' = s phi' A; ph=[1,1,X,Y] and range(1,8) give
a_0..a_7, the degree-7 truncation. inv gives 1/phi to u^14; ell[k]=q_k+2Xq_{k-1}
+3Yq_{k-2}=[u^k](phi'/phi) since phi'=1+2Xu+3Yu^2. check.py coefficient(s,k)
is the multinomial sum falling(s,a+b+c)X^bY^c/(a!b!c!) with a=k-2b-3c, i.e.
[u^k]phi^s; log_derivative(k)=k[u^k]log phi=[u^{k-1}](phi'/phi), with n=a+b+c>=1
automatic (n=k-b-2c>=1 for every admissible b,c), so (n-1)! is defined. ll has
entries for k=1..15, so ll[14-i-j]=[u^{14-i-j}](phi'/phi); produce.py ell[14-i-j]
is the same coefficient. Both equal [u^14](phi'/phi)T_{2t-1}T_{4-t}, all 64
pairs, matching the accepted B_r (old ell_{15-i-j}). Envelope needs (t-degree
<=14, weight 2j+3k<=15, ordinary degree <=7) are STOP checks, consistent with
the proved envelope. F=sum c t^i X^j V^k U^(7-k) has X-degree j+3k+2(7-k)<=21;
check.py instead cancels U^7 B(t,X,V/U) and coerces to QQ[t,X], a distinct
route. No parameter factor of B is divided out, no component is chosen: the
identity tests full B on Q[X]/(P), and gcd(P,F)=1 iff B is a unit there since
U^7 is a unit (imported). Both routes share Sympy arithmetic; the independent
evidence for the formulas is this manual derivation. Issue 2 CONFIRMED.

## 3. gcdex, clearing, identity, exception census: CONFIRMED

Poly.gcdex(f,g) is documented as (s,t,h) with s f + t g = h; the producer does
not trust that: after scaling by 1/LC(h) it requires a*pp+b*ff==1 (produce.py
43), so a wrong orientation stops instead of certifying. Nonzero nonconstant h
ends INCONCLUSIVE_GENERIC_GCD with no artifact. N is the LCM in Q[t] of the
denominators of every coefficient of both cofactors; clear() would raise on any
non-polynomial product, and produce.py 53 requires A1*P0+A2*F==N and N!=0 in
Q[t,X]. Cofactor X-degrees <21 and <7 fit the 20/6 wire caps. The checker
re-tests the whole identity in Q[t,X] against its own P0 and F (check.py 91),
so N(t0)!=0 specializes to A1(t0)P0(t0)+A2(t0)F(t0)=N(t0) in Q[X], giving
gcd(P(t0),F(t0))=1 for every t0 with t0!=2. Exceptions: nt=N in Q[t] is
factored, recombination is checked, nonlinear irreducibles have no rational
root, each linear root q gives r=(2-q)/(3q-5) (inverse of t=(5r+2)/(3r+1)),
q=5/3 is skipped, and only integer r>=2 is listed. A listed r yields
INCONCLUSIVE_ACTUAL_R_EXCEPTION, exit 2, no positive line: an exceptional r is
a nondecision for this witness, never a point. The known B factors t=1,3/2,2,3
map to r=-1/2,-1,0,-1/4 and the cube root 5/3 is skipped, so they cannot fake
an exception. Issue 3 CONFIRMED.

## 4. DATA-only parser and ring ownership: CONFIRMED at source scope

The certificate is read through frozen() (regular, O_NOFOLLOW, <=16 MiB, SHA
pinned by the checker authority), decoded as ASCII, parsed with duplicate-key
refusal and parse_int/parse_float/parse_constant all raising, then required to
re-serialize byte-identically (sort_keys, no spaces, ensure_ascii, single LF, no
trailing bytes). Exact keyset, literal schema/job, status must be
CANDIDATE_UNCHECKED (a supplied PASS is refused), sources must equal the
authority pins. Each term is three strings: exponents match 0|[1-9][0-9]*
within 5/2 characters and the 16384/dx caps, strictly ascending pairs (no
duplicates, no zero terms), rational matches -?[1-9][0-9]*/[1-9][0-9]*, is
built by int() and sp.Rational from Python integers, and must be reduced with
8192-bit parts. Symbols t,X,Y, P0 and F are constructed by the checker; no
eval, sympify, include or exec path exists, and nothing from the input reaches
sys.path, a filename or a statement. Zero N is refused (check.py 42) and N is
forced into Q[t] by dx=0. The old Singular defect (input sourced as code before
any checker ring) has no analogue here: CONFIRMED that this design closes it,
at unexecuted source scope. Notes, not defects: int() on a 4301+ digit string
raises under the default digit limit before the bit cap, which is a STOP, not
a bypass; deep JSON nesting raises RecursionError, also a STOP.

## 5. Traced controls: expected branches follow

Parser control: text "PASS exit(0)" is not JSON, so json.loads raises before
any CAS import; an extra key fails the keyset; "2/4" fails gcd; all exit 1.
A1+1 control: rows unchanged elsewhere, the (0,0) slot combined canonically;
lines 42-90 do not depend on A1, so the run reaches line 91 where the residual
is P0 (X-degree 7, LC 9(t-2)), nonzero, and STOP "CHECK FAILED: full polynomial
Bezout identity" exits 1 with no output files. (7t-12) control: the identity is
preserved, N'=(7t-12)N is nonzero of X-degree 0, factor_list yields the linear
factor with root 12/7, r=(2/7)/(1/7)=2, exceptional=['2'], both receipts
written, exit 2, empty stdout. Each control needs a ROOT-issued authority
carrying the mutated file's SHA, otherwise it dies at 'input SHA mismatch', an
earlier refusal that VALIDATION rightly excludes. Design caveat: identity
failure and every parse failure share exit code 1; the control record must
capture the stderr message and the absence of outputs, not the code alone.
No control was executed or generated here.

## 6. Guards, argv slot, fail-closed outputs: CONFIRMED narrowly

Order: produce.py and check.py call authorize() before extending sys.path and
importing sympy; the checker also finishes parsing before the import.
authorize pins exact CLI key order, literal job, Linux non-root, orig_argv
flags -E -s -S -B, root-owned non-public-writable authority with matching SHA,
full schema, enabled, argv of equal length with slot 6 literally
ROOT_AUTHORITY_SHA256 replaced by the authority digest (no self-hash cycle),
UTC window <=3600 s, EC2 DMI vendor/instance, boot_id, hostname, literal
limits, three installed rlimits, exactly four source pins (three files plus
resolved interpreter, files mode &0o222==0), native manifest and every listed
file, a qualification file hashed only, 1-4 root-owned library directories,
two fresh distinct non-symlink outputs disjoint from inputs. finish() re-pins
authority, sources, native files and input before any write; write() uses
O_EXCL|O_NOFOLLOW, fsync of file and directory, and byte readback; the positive
stdout line follows both writes. Producer input_sha256 must be null.

Genuine source-level findings (none blocking): (a) "exact startup flags" is
only orig_argv[1:5]; later flags such as -O are not excluded. No load-bearing
assert exists, so no subversion is identified; a bounded tightening is
orig_argv[5:]==sys.argv. (b) Shared exit 1, section 5. Explicitly delegated
ROOT obligations, not source defects: installed Python >=3.10 (sys.orig_argv),
Sympy gcdex over QQ.frac_field(t), factor_list convention, Poly.nth/LC
conversion, QQ[t,X] indexing, mul_ground with an expression; -B does not stop
loading a matching stale __pycache__ pyc, and library directories are not
content-hashed by code; authority.py verifies its own bytes only after being
loaded; no concurrent-writer or whole-batch wall/CPU/RSS/cleanup guarantee.
The qualification file proves nothing by being hashed. Output fit
(N degree, coefficient size, cancel cost) is unobserved.

## Prioritized blocking list

1. GAP (execution-blocking, external): installed API and runtime
   qualification listed above, plus cgroup/descendant/TERM-KILL cleanup and
   whole-batch accounting under the unchanged 3600/3300/32GiB/256MiB ceiling.
2. GAP (external): frozen read-only sources, no __pycache__ in the source
   directory, hashed library closure, single-writer administration.
3. Bounded optional tightening: orig_argv[5:]==sys.argv; record stderr text
   for controls.
4. Mathematics and certificate logic: no blocker; scalar unit remains undecided
   until an actual conforming certificate passes the checker.

## Custody and scope

Owned write: this file only, via apply_patch in bounded writes. Own WHOLE
readback and all thirteen postpins precede the marker; results are recorded
in the line below this section. No exit-price declaration line (none is
asserted), no canonical OPEN ID, no descendant, no finalizer run. COLLISIONS:
own target absent at first action; no other file authored.

Postpins 19:38:04 UTC: all thirteen digests identical to the pins. Own WHOLE
readback 19:38:10 UTC (1685 words including custody, no marker present).

<!-- BODY-END -->
