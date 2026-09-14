# Independent gate: complete coefficient-lifted Jacobian presentation (99,66) delta2

2026-09-06. Reviewer: Fable (Claude Fable 5.1). Producer: Astra. Charged producer
report SHA d870a8a647ae2e8dd9fb39bc85add9f15c10e01270322e15ee998f8a548f311b;
charged launch input complete_checked.sing SHA
50792efed4a5ed47cf2da5bf1f0d3b65e4f68efcba8e528b7dc29a541b72e091.
Frozen basis 0d39df3c9fd69c939a8420c54d03228b9077777d. No solve, std, slimgb or
msolve was run; no worker launched or terminated; producer files untouched.

| Claim | Verdict |
|---|---|
| 1. Physical source maps, polynomiality, reconstruction, identity, degrees 99/66 | CONFIRMED |
| 2. Monic graph, complete positive-J set, J0 and localizer, quotient equivalence | CONFIRMED (one free cylinder variable noted) |
| 3. Closed literal stream, serialization repair, Singular driver | CONFIRMED by exact sparse identity; in-script exact mutation controls did not execute (cap), replaced by direct-route controls |
| 4. One-way conclusion (point => Keller non-automorphism; proper => counterexample) | CONFIRMED; source necessity remains GAP |
| 5. Measured cost comparison; solver liabilities; bounded next experiment | MEASURED ONLY; no solver win claimed |

## Custody and process state

The 11 indexed receipt inputs verified by SHA-256 both in the lane inputs directory
and at their repository paths (charged-inputs.list and the .run.v2 fields agree).
Worker 172.30.0.56 answered IMDSv2 as i-0da0cebfc97c9fd54, r7i.8xlarge, hostname
ip-172-30-0-56, up 44 min at 10:30:26Z, 32 vCPU, 247 GB RAM, 22 GB disk free. At
that time no Singular, msolve, run_capped or producer python process existed and
load was 0.00. All 54 custody artifacts re-hashed on the worker before and after
my work equal custody.json; the latest producer mtime is 10:20:24Z (custody
publication), so nothing was modified. The producer directory has read-only modes.
My scratch subtree /home/ubuntu/factored-jacobian-review-20260906 did not exist
before and now holds the reviewer scripts, logs, result JSONs and one 436 MB
scratch copy review.sing (hash ab2133ce...); compact copies are under
box/factored-jacobian-gate-20260906/evidence (300 KB), scripts hashed in
box/factored-jacobian-gate-20260906/scripts.sha256. Every arithmetic subprocess ran
under ulimit -v 48 GiB and timeout 600 s; the aggregate never exceeded 64 GiB
(largest 33.1 GB plus Singular 15.3 GB at different times; free RAM stayed above
217 GB). Custody observation: two foreign scratch directories
/home/ubuntu/linear-c-discriminator-20260906 (10:33-10:48Z, with its own
custody.json) and /home/ubuntu/linear-c-root-replay-20260906 (10:55Z) were created
on this worker during the gate window by another root-authorized activity; I did
not read or touch their contents beyond a directory listing, and no process of
theirs was alive at 11:01Z. The worker is returned running, untouched, under root
custody; I did not terminate it.

## Claim 1: source maps, reconstruction, identity, degrees (CONFIRMED)

Independent host-side parse of the frozen source (SHA 778eda93...): residual_rows is
empty; field Q; branch delta2; stage 8; normalization {A3:98, B2:65, C2:22, C3:33,
h2:33, h3:11}. Every coefficient expression of the five maps is a polynomial over Q
(integer literals, non-negative integer exponents, numeric denominators only, no
symbol in a denominator); every support point has r+z <= N, no duplicates. Supports:
h3 24 rows, C2 33 (min r 8), C3 37 (min r 19), B2 194 (min r 31), A3 201 (min r 63).
The maps use 437 identifiers; with target_a, target_b that is 439, all inside the
444 declared free coordinates; exactly Z55, leader55, target_c, target_d, target_e
never occur, so dropping them is an exact product-with-affine-space removal.

Physical map: (r,z,e) -> e X^(N-r-z) W^z, X = x, W = y-x, Jacobian matrix
[[1,0],[-1,1]] of determinant +1, matching build_direct.py map_table/string_table
and the prior gate's Arrow 1. The degree_premap rows encode F and G exactly: all
220 A2c rows equal 3*B2c_r_z/2, with target_a/2 added at A2c_65_0; all 162 B1c rows
are 0 except B1c_32_0 = -target_b/3. Hence F = h^3 + (3D+a)h/2 + C and
G = h^2 - bh/3 + D with h = h3^3 + C2 h3 + C3, D = physical(B2), C = physical(A3).

Identity. With F_h = 3h^2 + (3D+a)/2, F_D = 3h/2, F_C = 1, G_h = 2h - b/3, G_D = 1,
G_C = 0 and a, b constants for d/dX, d/dW, the chain rule gives
J(F,G) = F_h G_D J(h,D) + F_D G_h J(D,h) + F_C G_h J(C,h) + F_C G_D J(C,D)
= ((3D+a+bh)/2) J(h,D) + (2h-b/3) J(C,h) + J(C,D). This is a formal identity in any
Q-algebra with two commuting derivations killing the coefficients, so it also holds
with h replaced by the lifted H. controls.py additionally checks three explicit
rational instances; I re-derived them by hand.

Degrees, computed on the worker from the maps: deg h3 = 11, deg C2 = 14, deg C3 = 14,
deg h = 33, deg D = 34, deg C = 35 (evidence reconstruct.log, PASS physical_degrees).
The degree-33 part of h is exactly W^24 (X+W)^9 = y^9 (y-x)^24 with all ten
coefficients numeric, so at every parameter point F has degree 99 with top form
W^72 (X+W)^27 and G has degree 66 with top form W^48 (X+W)^18, because the
corrections have degree at most 67 and 34 (PASS h_top_form_fixed, FG_exact_degrees).
J(F,G) has physical degree at most 99 (34+65, 33+66, 67); the literal support
reaches exactly 99. No Keller, T2 or T3 hypothesis was used anywhere in this claim.

## Claim 2: graph definitions, positive-J set, J0, quotient equivalence (CONFIRMED)

The 600-name order is sorted(439 source names) + Hfact sites sorted by (i,j) + Zj;
the JSONL header, complete_export.json coordinate_order and the ring line of both
.sing files agree with it (PASS variable_order_literal, sing_ring_line). My
recomputed h has 178 physical positions, 9,913 source terms, source degree 12;
exactly 160 positions are non-constant and they are precisely the 160 Hfact names;
the 18 constants are the ten top-form binomials, (1,0) = 1 and
(k+1,3k) = (-1)^k C(8,k) for k = 1..7 (PASS sites_match_Hfact_list). Every
define_Hfact_i_j row parsed exactly equals Hfact_i_j - h_ij(source) (160/160), and
the stream audit independently verified each definition is monic in its own Hfact
with a residual free of every Hfact and of Zj.

Exact sparse identity (review_reconstruct.py, differently organised from the
producer's coefficient tables): one 602-variable flint polynomial ring over Q
(600 ideal variables plus X, W), H, D, C as single polynomials, flint derivatives
and products, J = ((3D+a+bH)/2) J(H,D) + (2H-b/3) J(C,H) + J(C,D). Then every
literal J_i_j row was parsed, multiplied by X^i W^j and tree-summed; the difference
J_mine minus that sum equals exactly the 12-term J0 obtained independently from the
linear jets F_X(0)G_W(0) - F_W(0)G_X(0); J_mine has 11,289,124 terms (PASS
EXACT_IDENTITY_full_J at 113.6 s). This
proves at once: every one of the 1,468 rows is the exact physical coefficient, no
non-zero coefficient of J at any position (i,j) != (0,0), i+j <= 99, is missing,
all out-of-support slots are identically zero polynomials (so omitting them imposes
nothing), and the (0,0) coefficient of the bracket-identity J is J0. The inverse row
equals Zj*J0 - 1 exactly; J0 composed with Hfact -> h_source equals the source-jet
J0 (45 terms, degree 8), and both texts in complete_export.J0.json parse to these
polynomials. J0 is therefore the genuine constant term of J(F,G), not a
characteristic leader; the constant term is the same in (x,y) since the coordinate
change is linear. Degrees are distinguished throughout: physical degree in X,W
(rows up to 99) versus semantic degree in the 600 variables (J rows <= 4, inverse
5, definitions <= 12; every literal degree field re-verified).

Quotient equivalence. Let A = Q[439 source coordinates], R = A[Hfact_1..160, Zj],
Gamma = (Hfact_ij - h_ij). The A-algebra map phi: R -> A[Zj], Hfact_ij -> h_ij,
Zj -> Zj is surjective with kernel Gamma, and phi(J^lift_ij) = J^src_ij because
the rows are the same polynomial expressions in the coefficients of H, D, C, a, b.
So R/(Gamma + (J^lift_ij) + (Zj J0^lift - 1)) is isomorphic to
A[Zj]/((J^src_ij) + (Zj J0^src - 1)), whose points are exactly the source points
with J(F,G) a non-zero constant: the same physical full-J locus with J0 != 0, in the
frozen 439-coordinate affine chart. Nothing here asserts equivalence to any T2/T3
system or necessity of the chart. Observation: A3c_98_0 (the constant term of C,
hence of F) occurs in no generator (stream audit); the locus is a cylinder over it,
which is harmless for properness and lets a solver drop it (599 variables).

## Claim 3: closed literal stream, serialization, Singular driver (CONFIRMED)

Stream audit (review_stream_audit.py, 85 s, 125 MB): header ring Q / global dp /
600 names; indices 0..1628 sequential; labels unique; kinds 160 define, 1 inverse,
1,468 J with i+j <= 99 and no J_0_0; every row non-zero with terms and degree
fields equal to the exact parse; footer generators 1,629, terms 11,299,180, maximum
degree 12, generator_stream_sha256 9fd637ac... recomputed over the generator lines;
no trailing data; Zj occurs only in inverse_J; every identifier in every row is a
declared variable; largest row J_8_52 with 30,218 terms. complete_checked.sing:
line 1 is the exact ring line, line 2 "ideal I=", then 1,629 rows each equal to my
own wrapping of the JSONL text (1,325 rows contain rationals), then the exact
footer that prints the four markers and quits; complete_export.sing has the same
layout with the unwrapped texts. Repair audit: export_complete.py's double-escaped
patterns never match, so the original file is unwrapped; check_serialization.py's
patterns are correct. A Singular 4.3.2 micro test on the worker shows 1/2*x^9-3/4*y
and (1/2)*x^9-(3/4)*y parse identically to 1/2x9-3/4y (int/int is a number in a
char-0 ring), 33075/2*y^2 and -1/3*x parse as intended, while x^9/32768 is a
genuine error; that pattern is provably absent (the wrapper asserts it on every
row). So the charged checked file is safe and the retained original would have
parsed to the same ideal; charging complete_checked.sing is correct and harmless.

Singular driver: I parsed the first 1,631 lines of complete_checked.sing plus my
own footer (review.sing, SHA ab2133ce...) with Singular 4.3.2, parse-only, printing
for each generator size, deg, leading coefficient/monomial and trailing
coefficient/monomial: rc 0, 100.5 s, 15.3 GB RSS, markers ALL_ROWS_PARSED,
GENERATORS=1629, VARIABLES=600; all 1,629 six-tuples equal flint's under the same
dp order (invariants_compare.json, 0 mismatches). A specialization control by a
different route (review_scalar_direct.py): at a fixed small-integer point, explicit
bivariate F and G were built and the unfactored J = F_X G_W - F_W G_X computed
directly; all 1,468 literal rows evaluated at the point agree, no unlisted position
is non-zero, all 160 definitions vanish, the inverse row is 0 with J0 = -230872758.
Negative mutation controls: J(G,F) 1,468 mismatches; sign of a flipped 640;
W -> -W convention 734; one coefficient of J_8_52 perturbed 1; dropping J_1_0 one
unlisted non-zero position. GAP (closed): the exact-level sign-flip, perturbation
and dropped-row controls coded in review_reconstruct.py did not execute because the
process aborted at the 48 GiB virtual cap right after the identity passed (rc 134,
33.1 GB RSS); the identity result itself is complete and logged, and the controls
above stand in. No timestamp or hash of any producer file changed.

## Claim 4: one-way conclusion (CONFIRMED; necessity GAP retained)

Let K be a field of characteristic zero and P a K-point of the ideal I in
Q[600 variables]. By Claim 2, P is a source point s with all positive coefficients
J_ij(s) = 0 and Zj J0(s) = 1, so J(F_s,G_s) = J0(s) in K^x, since specialization
commutes with d/dX, d/dW. By Claim 1, deg F_s = 99 and deg G_s = 66 with the
fixed top forms. Jung-van der Kulk (any field): if K[F,G] = K[x,y] then one degree
divides the other; 99 and 66 divide neither way, so (F_s,G_s) is a Keller pair that
is not an automorphism, over K and hence over C. If I is proper in the polynomial
ring (the localizer is an ordinary generator, order global dp), Zariski's lemma
gives a Qbar-point, so exact properness over Q would yield a counterexample. No
properness and no point is claimed or evidenced here. Conversely a unit result would
exclude only this specified 439-coordinate gauged stage-8 locus; the map from an
arbitrary (99,66) Keller pair to this chart is unproved (typed GAP, unchanged from
the full-ideal gate), so a unit or a timeout cannot be read as an exclusion of the
degree pair. T2/T3 equivalence is neither needed nor asserted.

## Claim 5: measured comparison, liabilities, next experiment (MEASURED ONLY)

| Object (all measured, custody-hashed) | Rows | Literal terms | Max semantic degree | Wall | Peak RSS |
|---|---:|---:|---:|---:|---:|
| Frozen T2 subset, certificate-build.json | 466 | 6,448,959 | 34 | 1,192.2 s | 85.39 GiB |
| Unlifted full J, modular, killed at cap | 100 of 1,469 | 32,728,432 | 26 | > 600 s | 6.59 GB sampled |
| Complete lifted ideal, producer export | 1,629 | 11,299,180 | 12 (J <= 4) | 137.1 s | 1.71 GiB |
| Reviewer single-polynomial rebuild + identity | 1,629 | same | 12 | 113.6 s | 33.1 GB |

The largest T2 row has 4,607,718 terms against 30,218 here. My rebuild's memory is
a layout artefact (602-variable exponent vectors and a full tagged copy), not a
construction cost. This is a construction comparison only. Solver liabilities: 600
variables against 449; 160 degree-12 definitions with up to 535 terms whose
elimination reproduces the 32.7-million-term unlifted rows; 1,468 dense J rows;
the stock msolve 32-bit offset guard fails since 11,299,180 x 600 = 6,779,508,000
exceeds 2,147,483,647; parse alone costs 15 GB in Singular. Cheap construction is
not a solver win. Bounded next experiment (not launched, not authorized here):
band-wise exact std from the top, first the 51 rows of physical degree 98-99, which
by the site pattern involve no Hfact (h enters only through its numeric top form),
then the 256 rows of degree >= 90, each as its own Singular std over Q under
600 s / 48 GiB with the four markers and reduce(1,std) reported; result [1] would
exclude this locus only, otherwise report dimension only. No J0 = 1 or other
normalization is licensed, since no scaling action on this gauged chart is proved.

## FALLACY-v2

Variable/ring map declared (X = x, W = y-x, determinant +1; 600-name order; field
Q; image checks by exact identity). Exact degrees come from a parameter-free top
form, not from a floor. No sat(), raw remainder or Keller hypothesis is used. No exit
claim is made, so no charge_basis line applies. Every incomplete item is typed GAP
above; no cap was turned into confirmation or refutation.

<!-- BODY-END -->
