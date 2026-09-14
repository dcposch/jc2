# D125 finite-boundary composition gate (Fable 5.1, 2026-09-08)

Independent hostile review of the Astra composition `producer-composition.md`
(file SHA-256 `f31ba53481ecb24c5f7c2127f0a91f1eeddf5edce192a46406c46b86b931fd89`,
body re-hashed here over 9230 bytes to `b17dab46…`, whole text read), launched
00:19:06 UTC, light-only, from `/tmp/jc2-lane.KdMH7p/inputs` (26 pins, all
verified before and after; the lane directory is read-only and was never
written). Theorem under review: with S the finite raw odd 14c polynomial
Q-ring without z, I the entire unguarded source ideal, J=I:k^∞, no prime of S
contains J+(k); hence J+(k)=S, k is a unit in S/J, S/J is the guarded
localization, and I=J∩(I+(k^N)) with a CRT split. Not claimed and not reviewed
as claims: J=S, guarded emptiness/properness, an actual point, forced finite
degeneration, full125 coverage, JC2. Accepted 14c/f/g and 14p/q/s/t/v, 15e and
(per `post-state-15f.md`, promoted 00:07 UTC as 17(fffffffffffffff)) 15f are
imported at their existing scope, not re-reviewed. With 15f accepted, the
producer's "sole conditional premise" is discharged; the composition's own
text still labels itself conditional, which is now merely stale wording.
No AWS/SSH/CAS/solver/network/live peer/protected tree; no source powers.
No exit price is asserted, so no charge_basis line.

## Verdict table

| arrow | verdict |
|---|---|
| 1. Raw ring/arcs: literal S, I, J; order of operations; domain factoring; 14g rows before saturation; arbitrary char-0 residue fields | **CONFIRMED** |
| 2. Complete center cover: h0/δ0/α0 trichotomy; 14p literal k=s^m via finite extension plus τ=s·v(s) | **CONFIRMED** (own control E covers a non-rational root) |
| 3. Pure references/β: same A-determined t, α, F, j in 14v/15e/15f; ord α split incl. ∞; full shear; β0=243 slice | **CONFIRMED** (own controls C, D) |
| 4. Every prime over J+(k) → DVR → L[[s]] arc entering a stated case; map direction; finite-type hypotheses | **CONFIRMED** against the frozen Stacks proofs |
| 5. No prime ⇒ J+(k)=S exactly; (C) isomorphisms with nilpotents; N, intersection, CRT over nonreduced S/I | **CONFIRMED**; no weaker corrected arrow needed |
| 6. Controls/limits: hyperbola, dual numbers, vertical CRT, shear, unit-root toy; mutations change actual objects | **CONFIRMED**; unit-root toy scope is narrow (§3) |

## 1. Arrows 1–3: ring, cover, references

**Arrow 1.** S has the odd 14c slots and k, no z; I holds every unguarded
Jacobian, negative-lift and prescribed-face row (so B_(1,0)=5k²/9 and the
other 14c face values are equations in I); J is the union of the colons
I:k^n. Order of operations is right: saturation is defined on the raw ring,
zk−1 is never adjoined. An arc S→K[[s]] over a char-0 field with k(s)≠0 kills
J: k^n f∈I gives k(s)^n f(s)=0 in a domain, so f(s)=0; conversely I⊆J. The
three 14g rows a, 9e−5kx, x²−3ky satisfy k²a, k³h1, k⁴h2 ∈ I_low ⊆ I by the
accepted certificates, so they lie in J; then I ⊆ I+(a,h1,h2) ⊆ J forces the
same saturation. This is an ideal statement, not a claim that the raw low
ideal equals its saturation. Residue fields: 14f classifies over every char-0
field without root extraction; 14p/q/s/v/15e/15f are stated over arbitrary
char-0 K with K̄ and Puiseux extensions used only inside contradictions. The
restricted odd λ2=0, λ3=1 chart is what S is; the producer says so and claims
nothing about other D125 sources.

**Arrow 2.** By 14f the L-point at k=0 is (t0,α0,β0,γ0)∈L⁴ with h0=t0+3 and
δ0=γ0−β0α0+5α0²/9 (the 14t gate's own identity D=81δ0). The producer's table
is a trichotomy in the field L: h0≠0 goes to 14p, whose own proof derives
α0=γ0=0 from a01=−α0h0 and e0=−γ0h0, so no extra hypothesis is borrowed;
h0=0, δ0≠0 goes to 14q, stated for any α0 and any leading unit; h0=0, δ0=0,
α0≠0 goes to 14s, any leading unit; h0=0, δ0=0, α0=0 forces γ0=δ0=0, the
pure center with β0 free, which is exactly 14v's center (B0=R⁵+β0R³). Every
arc enters one case. 14p needs literal k=s^m. Write k=s^m u(s), u(0)≠0; adjoin
v0 with v0^m=u(0) (finite extension L'), solve v(s)^m=u(s) coefficientwise
with the unit pivot m·v0^(m−1), set τ=s·v(s). Its linear coefficient v0≠0
gives a two-sided compositional inverse σ, and f↦f∘σ is a continuous
L'-algebra isomorphism L'[[s]]→L'[[τ]] fixing constant terms. Rows are
Q-polynomial identities in the coefficient series, hence preserved; the
center, (g,p)-supports, parity and fixed faces are untouched; the moving
faces become τ^m, 5τ^m/3, 5τ^(2m)/9, c0τ^(3m); k=τ^m literally, and the
base change L[[s]]⊆L'[[s]] keeps h0≠0. No rational root of k is assumed.
Own control E does m=2, u=2+s, v0=√2∉Q to order 9: v²=u, τ²=k, σ∘τ=τ∘σ=id,
k(σ(τ))=τ²; the changed object v0=1 fails.

**Arrow 3.** 14v defines t=[p¹³]A/3, h=t+3, α=([p³]A+h³)/t, R_s=R_t(s)=R+hS,
F=A−R_s³−αR_s, j=ord F, with t0=−3 a unit, α(0)=0, F≠0 because
[g²p]F=k(s) (neither R_s nor R_s³ has a g²p slot), 1≤j≤m, and 14v itself
proves j<m and F_j=RC. 15e writes "in the notation of 14v" and 15f "use the
actual 14v references"; both display the same R_s=R+h(s)S and F, and the
15f gate checked R_t−R_(−3)=(t+3)S. These quantities depend on A alone, so
15f's proof-only subtraction β(s)A from B and 14v's β/γ kernel removals do
not move t, α, F or j. The split a=ord α is exhaustive: finite a<j is 15e's
contradiction hypothesis; finite a≥j and a=∞ (α≡0) are 15f's stated scope.
Field hypotheses are the parents' own. Shear: own control C proves, as a
polynomial identity in Q[α,β,γ,λ], δ(β−λ, γ−λα)=δ(β,γ) and the exact
z-polynomial transport; omitting the γ transport leaves the residual λα and
fails. A's slots sit inside B's free envelope (14f: weight 3<5, degree 15<25),
so B's prescribed faces, odd parity, lifts and [A,B] are unchanged. Slice:
own control D takes the pure-p part p⁵−3p³ of R_(−3) and finds
[p¹⁵]R⁵=−243, [p¹⁵]R³=1, [p¹⁵]R=0, so [p¹⁵]B0=0 means β0=243, and
[p¹⁵]A=1 makes the entire shear available; β0=0 fails. The sliced ideal
I'⊇I has J'⊇J, so J'+(k)=S follows from the unsliced theorem; no mismatch.

## 2. Arrows 4–5: from a prime to the exact ideal identity

**Arrow 4.** Take ANY prime q⊇J+(k), a point of X=Spec S/J in V(k). k is a
nonzerodivisor on S/J (kf∈J ⇒ k^(n+1)f∈I ⇒ f∈J), so k lies in no associated
or minimal prime; every generic point of every component is in U=D(k), U is
topologically dense, and S/J↪(S/J)[1/k] makes it schematically dense. Stacks
Lemma 32.15.1 (frozen 0CM1, statement and proof read: Morphisms 29.6.5 for
the specializing point, Krull–Akizuki 10.119.13 for the DVR) is applied with
f the open immersion U→X. X is finite type over Q hence Noetherian, so the
open immersion is quasi-compact hence finite type, Y=X is locally Noetherian,
and q is in the closure of f(U)=X. It returns a DVR A and Spec A→X, i.e. a
ring map S/J→A (this is the direction used: coordinates land in A), closed
point to q, generic point to a generic point η of a component with
Frac A=κ(η)∈U. So k∈m_A and k≠0 in A: 0<ord_A k<∞. Completion A↪Â is
injective (Krull), Â is a complete regular local ring of dimension 1
containing Q since S is a Q-algebra; Lemma 10.160.10(1) (frozen 0C0S, proof
read including the injectivity clause) gives Â≅L[[s]] with L its residue
field, L⊇κ(q)⊇Q. A ring map out of a Q-algebra is Q-linear, so every
Q-coefficient row holds in L[[s]], and the arc's generic point is a guarded
point over L((s)). Its center is an L-point of S/(I+(k)), classified by 14f
over L directly; the arrow-2 trichotomy is decided in L, so nonvanishing at
q persists and no root extension is needed for the split. The argument
assumes q and derives a contradiction; it never infers a boundary point from
U≠∅. Nilpotents of S/J die in A, which is exactly why this step yields only
"no prime" and arrow 5 must convert that into the ideal identity.

**Arrow 5.** If J+(k)≠S it lies in a maximal ideal, a prime containing J+(k),
forbidden by arrow 4 for every prime. So J+(k)=S exactly: some b has kb−1∈J.
No radical, no Nullstellensatz, and no claim J=S. (C): k is already a unit in
S/J, so S/J=(S/J)[1/k]; localization is exact and J·S[1/k]=I·S[1/k] since
each f∈J has k^n f∈I, so (S/J)[1/k]=(S/I)[1/k]; S[z]/(zk−1)≅S[1/k] gives
S[z]/(I,zk−1)≅(S/I)[1/k]. These are Q-algebra isomorphisms carrying
nilpotents (own control F: ε≠0 in Q[k,w,ε]/(kw−1,ε²), which equals its own
k-localization, certified by a Q-algebra map onto the dual numbers; putting ε
into the ideal breaks the certificate). (D): S is Noetherian, so I:k^n
stabilizes at some N with J=I:k^N and k^N J⊆I; kb≡1 gives k^N b^N≡1 mod J,
so J+(k^N)=S. Intersection: f=i+k^N a∈J ⇒ k^N a∈J ⇒ a∈J:k^N=J ⇒ k^N a∈I ⇒
f∈I; the reverse inclusion is trivial. This identity is unconditional (own
control A verifies it also for the changed object I=k²w, whose J+(k) is
proper); comaximality is what CRT needs, and it holds only on the hyperbola
side. CRT for comaximal ideals holds in any commutative ring, nonreduced S/I
included; k is nilpotent in S/(I+(k^N)) and a unit in S/J. N, b and the
projectors are existential, as stated. Either factor may be zero; the
producer draws no conclusion about that. The proof supports the statement at
full strength, so no corrected arrow is required.

## 3. Arrow 6: controls, limits, mutations

Hyperbola I=(kw−1): 1=kw−(kw−1), point (2,1/2): J+(k)=S with J≠S, which
refutes reading J+(k)=S as guarded emptiness. Dual numbers: ε≠0, ε²=0, k a
unit: the unit identity is not reducedness. Vertical split I=k²(kw−1):
J=(kw−1), N=2, 1=k²w²−(kw−1)(kw+1); own control A adds the idempotent
e=k²w² (e≡1 mod J, e≡0 mod k², e²≡e mod I) and own control B the exact
certificate kw−1=z²·k²(kw−1)−(kw−1)(zk+1)(zk−1), showing (C) on the toy.
Full shear: the producer checks one rational point (α,β,γ,λ)=(2,3,4,5); own
control C is the polynomial identity. Unit-root toy: k=s³·8(1+s)³,
τ=2s(1+s), τ³=k is exact, but u(s)=8(1+s)³ is a perfect cube with the
rational root 2, so the toy exercises neither the recursive root with a
non-rational pivot, nor the field extension, nor the compositional inverse;
own control E supplies those. This is an evidence-scope note, not a theorem
defect. The five producer flags change actual objects (H=kw+1, certificate
sign, law ε²=ε, γ left untransported, v=2+3s); no need(True) or constant
predicate exists in the checker; the AST zero-Assert node check is hygiene.

## 4. Tiny replay (own scratch copy) and own controls

Copied `producer-check.py` byte-for-byte to
`box/d125-finite-boundary-composition-gate-fable5-20260908/scratch/check.py`
(hash equal, `fd8d4720…`); never edited; `--record` was not run anywhere.
Each child: `/usr/bin/python3 -I -B [-O] scratch/check.py [flag]` under
`ulimit -t 25; ulimit -v 524288; timeout 30`. Positive stdout is byte-equal to
the frozen `producer-witness.json` in both modes. All twelve (optimized,
mutation, returncode, stdout hash) rows equal the frozen `producer-replay.json`;
mutation stderr hashes differ from it only by the path-dependent traceback,
and the failure markers match the messages the frozen `--record` code expects.
| optimized | mutation | rc | stdout sha256 (16) | marker | wall s |
|---|---|---|---|---|---|
| normal | positive | 0 | `57ede9d764ded48e` |  | 0.043 |
| normal | --change-hyperbola | 1 | `e3b0c44298fc1c14` | ValueError: actual nonempty hyperbola point | 0.103 |
| normal | --change-CRT-sign | 1 | `e3b0c44298fc1c14` | ValueError: exact comaximal CRT certificate | 0.102 |
| normal | --change-nilpotent-algebra | 1 | `e3b0c44298fc1c14` | ValueError: actual nonreduced unit-k algebra | 0.102 |
| normal | --omit-gamma-shear | 1 | `e3b0c44298fc1c14` | ValueError: actual beta gamma shear invariant | 0.102 |
| normal | --change-unit-root | 1 | `e3b0c44298fc1c14` | ValueError: actual unit-root parameter identity | 0.102 |
| -O | positive | 0 | `57ede9d764ded48e` |  | 0.159 |
| -O | --change-hyperbola | 1 | `e3b0c44298fc1c14` | ValueError: actual nonempty hyperbola point | 0.519 |
| -O | --change-CRT-sign | 1 | `e3b0c44298fc1c14` | ValueError: exact comaximal CRT certificate | 0.520 |
| -O | --change-nilpotent-algebra | 1 | `e3b0c44298fc1c14` | ValueError: actual nonreduced unit-k algebra | 0.521 |
| -O | --omit-gamma-shear | 1 | `e3b0c44298fc1c14` | ValueError: actual beta gamma shear invariant | 0.517 |
| -O | --change-unit-root | 1 | `e3b0c44298fc1c14` | ValueError: actual unit-root parameter identity | 0.516 |

Own `fable5_composition_controls.py` (stdlib, zero Assert nodes, same caps,
six checks A–F described above; one superseded dead-code block in E is
cosmetic and overwritten by the loop that runs): positive stdout byte-identical
normal and −O; each changed object exits 1 at its named gate in both modes.
| optimized | mutation | rc | stdout sha256 (16) | marker |
|---|---|---|---|---|
| normal | positive | 0 | `55f1812ce3e4989f` |  |
| normal | --line | 1 | `e3b0c44298fc1c14` | ValueError: actual comaximality J+(k^N)=S needed for CRT (fails for the changed object H=w) |
| normal | --omit-gamma | 1 | `e3b0c44298fc1c14` | ValueError: symbolic delta invariance under B->B-lambda*A (beta and gamma both transported) |
| normal | --beta-zero | 1 | `e3b0c44298fc1c14` | ValueError: [p^15]B0=0 slice forces beta0=243 (not 0) at t0=-3 |
| normal | --rational-root | 1 | `e3b0c44298fc1c14` | ValueError: recursive unit root v^2=u with pivot 2*v0 (mod s^9) |
| normal | --kill-eps | 1 | `e3b0c44298fc1c14` | ValueError: Q-algebra map kills every ideal generator (changed object with eps in the ideal fails) |
| -O | positive | 0 | `55f1812ce3e4989f` |  |
| -O | --line | 1 | `e3b0c44298fc1c14` | ValueError: actual comaximality J+(k^N)=S needed for CRT (fails for the changed object H=w) |
| -O | --omit-gamma | 1 | `e3b0c44298fc1c14` | ValueError: symbolic delta invariance under B->B-lambda*A (beta and gamma both transported) |
| -O | --beta-zero | 1 | `e3b0c44298fc1c14` | ValueError: [p^15]B0=0 slice forces beta0=243 (not 0) at t0=-3 |
| -O | --rational-root | 1 | `e3b0c44298fc1c14` | ValueError: recursive unit root v^2=u with pivot 2*v0 (mod s^9) |
| -O | --kill-eps | 1 | `e3b0c44298fc1c14` | ValueError: Q-algebra map kills every ideal generator (changed object with eps in the ideal fails) |

## 5. Imported versus independently checked

Imported at existing trust, not re-reviewed: the 14c chart and its face
values; the 14f field classification and its Arzhantsev–Petravchuk
centralizer import; the 14g certificates; the 14p, 14q, 14s, 14t, 14v, 15e
theorems and the 15f theorem as recorded accepted in `post-state-15f.md`
(root's replay receipt there is provenance only). Independently checked here:
all 26 pins and the producer body hash; the saturation and domain algebra of
arrows 1 and 5; the density, finite-type and direction facts against the two
frozen Stacks proofs; the exhaustiveness of the center trichotomy against
each parent's literal hypothesis line; the extension-plus-parameter change
with a non-rational root (control E); the symbolic shear and the β0=243 slice
(controls C, D); the vertical CRT idempotent, the localization certificate and
the nilpotent survival (controls A, B, F); the twelve-run replay. Producer
custody facts not in the frozen set (its `seal_custody.py`, `witness-O.json`)
are root's, though the recorded `witness-O.json` hash equals my −O output.
No historical cross, low-alpha, axis or geometry report was used as a premise.
Typed gaps: none charged to the theorem. Uncharged evidence notes: the
producer's unit-root toy is narrow (§3) and its report still calls the result
conditional after 15f's acceptance.

## 6. Custody
Frozen input pins before and after the gate: IDENTICAL (27 entries).

| own artifact | sha256 |
|---|---|
| `prepins.txt` | `f0b9c0578d58946685ea951daf5ade5db75a1a6f64c497b23770e085f33bac93` |
| `postpins.txt` | `f0b9c0578d58946685ea951daf5ade5db75a1a6f64c497b23770e085f33bac93` |
| `scratch-check-hash.txt` | `6fb69c5eea515ba6575054da39f7bfc070be4699f398eeeeac3ae7278be372ff` |
| `producer-body-rehash.txt` | `7da43b85707b93a1f9a3a1498bb1e573c7a385385ed55800e569b93822591fec` |
| `run_replay.sh` | `155aef5ba859f9b53f036f2f56b8869a479e5a06f89f1ad7d1006b1d6cd66c22` |
| `replay/replay-individual.tsv` | `42212ad80c5abc87dbc8f9a67462f2516df183c4ea39b049aec84bc7b3c009e1` |
| `replay/out_normal.txt` | `57ede9d764ded48e047aaf5f1a7b6431279f0ab1b790dea46414469e1ed3bca2` |
| `replay/out_-O.txt` | `57ede9d764ded48e047aaf5f1a7b6431279f0ab1b790dea46414469e1ed3bca2` |
| `fable5_composition_controls.py` | `43ee18cc0e304895e1d21735ed0414a75584ae7f73cabb34bb37aa6406a504b1` |
| `controls/runs.tsv` | `bdb22d8b9794e3159c7b965b09bfd102f28b1f061ab7d1134e795a64d7b1539b` |
| `controls/out_normal_positive.txt` | `55f1812ce3e4989f12811b016e8a72134d34ae3f2f7da28599a72d49206da2e0` |
| `controls/out_-O_positive.txt` | `55f1812ce3e4989f12811b016e8a72134d34ae3f2f7da28599a72d49206da2e0` |

All children exited (largest wall 0.52 s); no background process, no frozen
byte altered, no canonical file edited, no descendant launched. Overall: all
six arrows CONFIRMED at the stated scope; with 15f accepted, the composition's
(C)/(D) conclusions rest only on accepted parents. Root alone decides
promotion. STOP/IDLE.

<!-- BODY-END -->
