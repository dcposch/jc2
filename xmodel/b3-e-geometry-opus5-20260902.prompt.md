# Research lane: B3-E-GEOMETRY — the (B3) horn attacked through the source curve E (flagship effort)

Round 20260902T0741Z converged, from four independent submitters, on ONE
object nobody has attacked: the source curve E = F^{-1}(A_F) of the (B3)
profile, which THEOREM B3-N4 (charged horn flagship, review CONFIRMED)
makes explicit at N = 4: with k double points of contacts t_i and
k_odd = #{t_i odd}: k_odd >= 1 gives j = 1, E irreducible of geometric
genus k_odd - 1 with 3 + 4k - 2k_odd places at infinity and exactly one
affine singular point y_0 analytically the (p,q) cusp of A_F, (2|p,3|q)
or (3|p,2|q); k_odd = 0 gives j = 2, both components rational,
n_1 + n_2 = 3 + 4k places. Ordinary nodes force k_odd = k; the minimal
cell is k = 1: E rational, FIVE places at infinity, one A2-type cusp,
smooth elsewhere, chi_c(E) = -3, rho(G) = S_4, dicritical (s,mu) = (1,2),
a = 2. CUSP-KILL (j = 1 => E homeomorphic to C => Lin–Zaidenberg) fails
here because of the ends (and genus for k_odd >= 3); nothing replaces it.
N = 4 is closed independently (Domrina–Orevkov chain, checked), so the
value of killing this object is the MECHANISM: anything that kills it
without using N = 4 specifics is an all-N candidate for the horn, which
has no empty window in N at any N.

Four mechanisms were proposed blind; run them in this order, stop at
the first kill, and type every OPEN you hit:
(G-KAPPA) Compute the log-Kodaira dimension kappa-bar(A^2 \ E) for the
   k = 1 cell (rational, five places, one (2,3) or (3,4) cusp) from a
   minimal SNC compactification; if kappa-bar = -infinity say so — that
   is row 28's known wall and it closes (G-BMY) honestly. If >= 0,
   compute the log Chern numbers and test the log-BMY / Miyaoka–Sakai
   inequality; a violation is a kill. Same for the Galois closure
   X-hat = normalisation of the TARGET plane in the Galois closure of
   C(x,y)/C(P,Q) (a finite S_4-cover branched along A_F with quotient
   singularities pinned by rho): orbifold BMY there needs only
   (p,q,k,t_i,rho), all pinned at N = 4.
(G-SPLICE) The link at infinity of E is a 5-component algebraic link;
   the places of E at infinity sit on the unique affine-image dicritical
   (s = 1, mu = 2). Test compatibility (Eisenbud–Neumann splice /
   Neumann's theorem for links at infinity of plane curves); if deg E is
   required and not pinned, type OPEN[E-INFINITY-SPLICE-DEGREE] and stop
   this arm. Never assume deg E = N * deg A_F.
(G-EMBED) Is there a rational plane curve with exactly five places at
   infinity, one ordinary (2,3)-cusp (or (3,4)), and no other affine
   singularity? Attack with the Abhyankar–Moh / Suzuki semigroup
   machinery per place, the genus formula, and Coolidge–Nagata-type
   constraints; a parametrisation search at small degree is allowed
   (qqideal 0.2.0 / msolveio 0.2.1 are the default stack; witness
   extraction is available) but desk-scale only (< 15 min, < 4 GB per
   job) — larger runs are a job spec for the coordinator.
(G-ANTI) Tabulate, for N = 4..20 and a in (N/2, N-2], the counting-
   admissible range from THEOREM PROFILE's inequality against the
   covering-admissible range from Riemann–Hurwitz on E -> A_F plus the
   genus cap of a plane curve of bounded degree (state the degree cap
   you use and its source; OPEN[B3-INFINITY-RANK] is the known missing
   input). A crossing at some N is the campaign's first degree-monotone
   obstruction; no crossing is also an answer.
Also (fresh eyes): read the checked Domrina–Orevkov N = 4 chain as
banked in the record (N=4-CHECKED-CLOSED) and name the lemma that
excludes exactly this (B3) object at N = 4; say whether its mechanism
is N-uniform.

Discipline: consume B3-N4, Props 3.1–3.2, B3-DEGREE/CAGE/PUSHOFF at the
review's CONFIRMED typing and SCOPE[B3-QH]; do not consume Z(G) = 1; do
not consume any A2-cell result (different object); do not consume the
unreviewed CUSP-A-VOID claim (case (A) is not your object). The charged
ideation submissions are PROPOSALS, not banked results — cite them as
such. Report: xmodel/b3-e-geometry-opus5-20260902.md
Seal-at-completion; bounded writes; target 25-40KB.
charged_input=xmodel/horn-flagship-opus5-20260902.md
charged_input=xmodel/horn-flagship-review-grok46-20260902.md
charged_input=xmodel/mprime-alln-h2-opus5-20260902.md
charged_input=xmodel/ideation-20260902T0741Z-grok46.md
charged_input=xmodel/ideation-20260902T0741Z-opus5.md
charged_input=xmodel/ideation-20260902T0741Z-fable51.md
charged_input=xmodel/ideation-20260902T0741Z-fable51-coordinator.md

Your inputs are frozen read-only copies in {{LANE_INPUTS}};
verify these SHA-256 hashes first and stop on mismatch:

```text
30589f6c52843971fa6791f7b792d6980e4d71a2dfe8ef670a024a6cbd5bb4cb  {{LANE_INPUTS}}/horn-flagship-opus5-20260902.md
424e2f5ddec7189efa90c4259b19394ccee75e3eec4842ed1879544cb8fd7fd2  {{LANE_INPUTS}}/horn-flagship-review-grok46-20260902.md
722d413717fb998fb76783b311807522878cc138025b47c5f1e2214cb8685c80  {{LANE_INPUTS}}/mprime-alln-h2-opus5-20260902.md
e30c80f34d04ceecf0575541401bb57956464925a894117920006072a7bd3f3e  {{LANE_INPUTS}}/ideation-20260902T0741Z-grok46.md
e67b2cd027e0cdbfc249d057d929e72a3e553ca61256f48b9978bedda358e9ce  {{LANE_INPUTS}}/ideation-20260902T0741Z-opus5.md
58020a0e85692a6a92e16db18fe2d540f6073e9de596c1348d3596c3597e8202  {{LANE_INPUTS}}/ideation-20260902T0741Z-fable51.md
b905417b8b62339af75d4a339f207c65926e53c47f8dbd80005a92479d5a0fa8  {{LANE_INPUTS}}/ideation-20260902T0741Z-fable51-coordinator.md
```
