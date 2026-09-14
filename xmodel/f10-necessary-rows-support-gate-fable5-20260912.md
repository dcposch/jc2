# f10-necessary-rows-support-gate-fable5-20260912

Reviewer: Fable5.1, independent different-model FIRST of the ROOT producer
support report and the Astra checker support report. Skeleton opened
2026-09-12T03:24:11Z; all eight inputs hashed 03:24:20Z BEFORE reading; fresh
WHOLE reads of all eight followed, 03:24-03:30Z. Static text review only: no
execution, import, AST, compile, test, CAS, dummy, network, git, process or
protected-tree action. The scientific Python sources were inert text.

Not re-reviewed: the accepted 23z/19z source-exclusion theorem, the branch
deletion, or the old inverse streaming. This FIRST reviews one NEW retained-stage
feasibility application of the old weighted-support method at the exact
supplied interface.

## Input prepins (sha256 at 03:24:20Z, all eight equal to the expected values)

- f10-necessary-rows-producer-support-root-20260912.md 43819c4f2672e0bce0dc10ef3c214caef3313f2b289d33cc17324d4d9c13a69c
- f10-necessary-rows-checker-support-astra-20260912.md a719fdee06e5635a9a886f3d3beb65c8faf3e4a2ec730fc6fb0151763e2c4025
- produce.py 5078142850c5f4d2e4f08da18fad01ea0271bf36c18740df372884747535280a
- arithmetic.py acd07f800707c379aba60bd06f239d38cd83c86867729561367abd2bcc04ce73
- check.py 1d2d5b5408bfbf13b96f09453b1f14dfe884d261e702843bc31e5a043ffa53d1
- check_arithmetic.py 9d2aac637dbdeaa192cc3fe531e83694f9853b6573556ad5d49362f754b1163e
- authority.py 804c7aff56538fc332bf68638b03b7167eccdb49f73337f1a5f1823348b522a4
- ROOT-ADOPTED-NECESSARY-ROWS.md 176363939a8aa6861995cd72a99c61f7d04bfeab5a9634f6d3143dcd3d3bd098

## Verdicts

A CONFIRMED. B CONFIRMED. C CONFIRMED. D CONFIRMED. E CONFIRMED for legitimate
producer output only. F: stated below. No repair was needed; no bound failed.

## A. Elementary weighted-simplex count: CONFIRMED

Own derivation. Monomials of exact weight d in variables of weights
(1,w1..wm) biject with integer tuples (e1..em), ei>=0, sum wi*ei<=d, since the
weight-one exponent is then forced. The half-open unit boxes based at these
tuples are disjoint and lie in {u>=0 : sum wi*ui < d+sum wi}, whose volume is
(d+sum wi)^m/(m! prod wi). So N(d) <= that quantity. Multiplication by the
weight-one variable injects weight d into weight d+1, so N is nondecreasing.
The bound counts dictionary keys over any coefficient ring, so it also bounds
every partial product or partial sum whose keys lie in the envelope, before
cancellation. Integer ceilings, recomputed by hand:

| envelope | remaining weights | bound | value |
|---|---|---|---|
| raw, weight 23 | (2,3,4,7,1,3), sum 20, product 504 | 43^6/362880 | 6321363049/362880 < 17421 |
| formal, weight 10 | (2,3,4,7), sum 16, product 168 | 26^4/4032 | 456976/4032 < 114 |
| formal, weight 27 | (2,3,4,7) | 43^4/4032 | 3418801/4032 < 848 |
| graph, weight 30 | (2,3,4), sum 9, product 24 | 39^3/144 | 59319/144 < 412 |

ROOT's 18000 and Astra's 20000 (with 44^6 < 20000*362880 checked) both hold.
Formal band objects carry theta at weight 0 with degree at most 14, so
15*114 = 1710 (ROOT) and Astra's coarser 15*849 = 12735 are both valid.

Negative-weight countercontrol: ROOT's q of weight -3 example is correct. With
a negative-weight variable the weight-0 set X1^{3i} q^i is infinite, so
positive homogeneity alone gives nothing. Both reports avoid this for the
Laurent-S and scale kinds by explicit lower bounds on the negative exponents
and by translation or injective reindexing, not by a grading. That is the
right structure; see D.

## B. ROOT producer, all actual operations: CONFIRMED

I walked produce.py with arithmetic.py and rederived every weight.

- Pre-truncation series (arithmetic.py:271-278): term has theta degree <= n,
  v = c-1 has degree 3, so the product before truncate has degree <= n+3 <= 10.
  Parameter weight 0, so at most 11 keys.
- Critical integration (produce.py:149-154): R*invC2 degree <= 7, primitive 8,
  times C^2 gives 14. Weight 0, at most 15 keys. This is the largest theta
  degree in the circuit.
- Formal recursion: C, D have weight 0; forcing at gap h multiplies gaps i and
  h-i; op multiplies weight-0 C, D by weight-h A, V; rho = var(h-1) has
  weight h for h<=4; base and xyz have weight h; basis Vj weight 0. At h=7
  Apart = (z - U*d0)*T has weight 7 with U weight 4, d0 weight 3; at h=8
  U^2 T^5 and U^2 T^3 have weight 8; at h=10 A = {} and V weight 10. Theta
  degree in op is <= 6. So every band partial sum or product is inside
  weight h <= 10, theta <= 14: fewer than 1710 keys.
- Installation: exponent 10-h-3j, so Ahat and every partial sum have weight
  10. aa[2] has S exponent 0..4, so Dformal has S >= -1 and weight 3;
  Vformal has S >= -2 and weight 6, before any anomaly record is inspected.
  Translating by S and S^2 puts them in ordinary weights 4 and 8.
- Euler: bb[5] = S^2 has weight 2 = 17-15; each of the six summands of q has
  weight 17-3j (checked all six: e.g. diff_S(aa[0]) weight 9 times bb[j+3]
  weight 8-3j); reinsertion by shift S^i preserves it; Bhat has weight 17.
- FULL Jacobian: diff_S(Ahat)*diff_theta(Bhat) is 9+14 = 23 and
  diff_theta(Ahat)*diff_S(Bhat) is 7+16 = 23. Pi weight 10, Pi^2 weight 20,
  Delta weight 23, residual weight 23. All within 17421 keys.
- Graph input T = z*P1[0] - U*P0[0]: 7+20 = 27 and 4+23 = 27; it is raw
  kind but S- and theta-free, so the formal weight-27 count (< 848) applies.
  ROOT correctly refuses to place it in the weight-23 raw envelope.
- Finite power (arithmetic.py:233-240): binary, no unused final square. The
  largest z exponent in a weight-27 input is 3, and power(zeta,3) visits
  weights 7, 14, 21 only. power(Pi,2) is weight 20, power(so,8) is one term.
- Graph substitution: each summand has X-weight equal to the input weight,
  since zeta has weight 7 and z has weight 7; rows <= 27, ell = 23,
  g = Hq*ell = 30, zeta*ell = 30. All <= 412 keys. Exponents: S <= 23,
  theta <= 14, X1 <= 30, z <= 3, s in [-7,13]; all far below 256.

No omitted larger intermediate was found. Retained diagnostics, packets and
scale_record are copies of already bounded objects; their aggregate memory is
outside the claim, as ROOT states.

## C. Astra checker, inspected independently: CONFIRMED

Line anchors verified by grep: invC2 at check.py:266, installation at 301,
Euler at 329, bracket at 364, to_scale at 395, origResidual at 418, mixed at
468; check.py is 514 lines. check_arithmetic.py Poly.__init__ calls bounded,
and add/mul re-check 100000 per key insertion, so every construction is
guarded at the same limit as the producer.

- Coefficient-pair operator (oper): co(C,6,i) weight 0 times co(bp,6,ell)
  weight h, moved to theta^(i+ell-1); theta degree <= 7, weight h. Forcing
  loop identical. Fewer than 8*114 keys per accumulator.
- Formal forcing and solve_upper: same weights as B. The h=7 check
  polynomial N has weight 7.
- Euler (329-345): other sums der_S(Ac[ak])*Bc[j+3-ak] of weight
  (9-3ak)+(8-3j+3ak) = 17-3j; rhs weight 17-3j; B weight 17.
- Full bracket (364-370): der_S(Ac[ak])*Bc[bl] has weight 26-3(ak+bl)
  before the theta shift and 23 after; ak+bl >= 1 so the pre-shift weight is
  <= 23. Same for the scale bracket (410-416), where pa = Phi_{ak-3}(Ac[ak])
  and pb = Phi_{bl-5}(Bc[bl]) give Phi_{ak+bl-8} of raw weight 26-3(ak+bl),
  and the t-move returns Phi_{-7} of weight 23.
- Horner (check_arithmetic.py:281-286): after the addition at index k the
  accumulator has X-weight w-7k, after mul by zeta w-7(k-1); all <= 27 for
  rows, 23 for ell. Each transient <= 412 keys.
- Parser bounds versus circuit: the parser admits at most 20000 terms per
  polynomial and 400000 aggregate, but it also enforces exact weight and
  strictly increasing exponent tuples, so any parser-admitted polynomial has
  at most 412 distinct terms. The reconstructed circuit's per-Poly support is
  the same 412 bound. The wire caps are therefore unreachable by well-formed
  input; they only bound the raw list length of malformed input.
- Exact per-Poly support: every checker Poly is either homogeneous in one of
  the four envelopes above or a Phi-image of one, exactly as in D.

Astra's numbers: 15*849, 20000+1+412 < 21000, and 1448440 bytes were all
recomputed and hold.

## D. SCALE step, most fragile: CONFIRMED

Own derivation with Phi_k(P) = s^k P(X, z=s^2, S, theta=s*t). On exponent
tuples this is the affine map (x,ez,eS,et) -> (x, 2ez+et+k, eS, et), which
is injective for fixed k: et is kept and ez = (s-exp - et - k)/2. Both
scaled (produce.py:269-274) and to_scale (check.py:395-401) implement exactly
this map. Consequences I verified against the source, not the reports:

- Products: Phi_k(P)Phi_l(Q) = Phi_{k+l}(PQ), and the Minkowski sum of the
  images is the image of the Minkowski sum, so every partial product
  accumulator has at most |supp P + supp Q| keys, inside the raw envelope of
  weight w_P + w_Q (translated by an S-power when Laurent).
- Extraction: co(Phi_k(P),6,n) = Phi_{k+n}(co(P,6,n)). Derivative in t:
  d/dt Phi_k(P) = Phi_{k+1}(dP/dtheta). Derivative in S commutes. Hence
  origJ = Phi_{-7}(J) with both products in Phi_{-7}(weight 23), matching
  ROOT and Astra.
- tt = Phi_{-1}(theta), so origPi = Phi_{-3}(Pi) summand by summand,
  origUpper = Phi_{-7}(Delta) with origPi^2 = Phi_{-6}(weight 20).
- Laurent reconstruction: S*t^3 = Phi_{-3}(S theta^3); (S*origd - origu)t^2 =
  Phi_{-3}((S D - U)theta^2) with S >= 0; the constant 1 equals Phi_{-2}(z)
  and joins -origu*origd (Phi_{-2}(U D), S >= -1) and S*origv
  (Phi_{-2}(S V), S >= -1) in one weight-7 Laurent envelope, then t gives
  Phi_{-3}(weight 10, S >= -1); origk = Phi_{-3}(K). Multiplying that common
  envelope by S embeds it in ordinary weight 11. The S lower bounds -1 and -2
  come from aa[2] and aa[1] having S >= 0, checked at produce.py:196-202,
  before any negative-S anomaly record is tested.
- Nonhomogeneous terms: origu*tt = Phi_{-2}(U theta), not Phi_{-1}; ROOT and
  Astra both write Phi_{-2}, which is right. origResidual is the union of
  Phi_{-7}(weight 23), the constant, and Phi_{-2}(U theta), so fewer than
  17421 + 1 + 5 keys; ROOT's 72002 and Astra's 21000 are both valid
  over-bounds.
- Low arrays: co(co(origResidual,6,1),5,i) lies in Phi_{-6}(P1[i]) plus origu
  at i=0, and the expected side is scaled(P1[i],-6) minus origu at i=0: the
  same envelope. low0 likewise with Phi_{-7}(P0[i]) and the constant at
  i=0. Subtraction adds no envelope.
- Guard: power(so,8) is one term; orig_a is s^{-3} times a scalar, orig_b is
  s^{-5} times a scalar, product s^0; one or two keys.

Every source call in both files falls into one of these classes. The stated
conservative bounds cover all of them; nothing needed repair.

## E. Wire output and payload: CONFIRMED for legitimate output

Wire is 30 polynomials plus c and c_inverse. wire_p enforces exact weight,
nonnegative X-only exponents and a nonzero coefficient, so each polynomial
has at most 412 terms and the counter is at most 12360, below 20000 and
400000. Degree <= 7 and p <= 2147483647 give at most 7 coordinate strings of
at most 10 digits; weight <= 30 gives at most 2 exponent digits. Canonical
compact JSON per term: exponent list <= 21 bytes, coefficient list <= 92,
pair brackets and comma 3, separator 1: <= 117 bytes. 12360*117 = 1446120.
Astra's 30*(412*117+64)+400 = 1448440 is arithmetic-correct.

Metadata: the payload copies place and source_pins from the authority document
that load_pinned bounds at 65536 bytes (authority.py:70-76). Re-encoding with
ensure_ascii and compact separators expands any input byte sequence by at
most 3x in the worst case (a 2-byte UTF-8 or 2-byte UTF-16 character becomes
a 6-byte escape; a 4-byte astral character becomes a 12-byte surrogate pair;
control characters must already be escaped in the input). The 6x allowance
used by both reports is therefore safe. Place strings are further bounded by
the producer's own integer() check. Total legitimate payload is below about
2 MiB, hence below 4 MiB and far below the 134217728-byte predicate.

Not covered, correctly stated by both reports: a malformed or oversized
checker input up to 128 MiB, its json.loads and canonical re-dump
allocations, parser lists of up to 400000 terms of junk before per-term
validation, runtime logs, native metadata, aggregate resident copies of the
150 diagnostics and packets, and batch disk usage. No CPU, RSS, wall or
good-place guarantee follows from anything here.

## F. Strongest surviving practical conclusion

On the fixed retained r3 necessary-row circuits in produce.py, arithmetic.py,
check.py and check_arithmetic.py, every internally reconstructed Poly and every
transient add or mul accumulator has fewer than 17421 keys (raw and scale
classes), 1710 keys (formal), or 412 keys (graph), all below the unchanged
100000-term limit; the legitimate producer payload is below 4 MiB under the
current authority parser. The unchanged term cap cannot stop a run that
reaches these operations. The mathematical instrument remains UNRUN; execution
is separately held on complete reviewed installation and release and on
descendant-cleanup qualification. Nothing here recommends raising caps,
rerunning old identities, a new framework, selecting or hardcoding a place, or
starting a worker. No bound failed, so no new doubt is raised; the only open
practical quantity is time and memory, which this proof does not touch.

## Readback and postpins

Own complete untruncated readback of this report was performed at
03:31:58Z and matched the authored text. All eight input postpins were
recomputed at 03:31:58Z and equal the prepins above; no input changed during
the review. Postpin digests were emitted to stdout, not to side files. No
artifact_finalize, no charge_basis declaration and no Seal are made here; the
launcher owns custody. This closing record and the marker below are the last
body write; no later edit follows.

<!-- BODY-END -->
