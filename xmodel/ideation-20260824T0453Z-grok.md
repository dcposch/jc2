# Full-spectrum ideation report — grok

- Round/snapshot ID: `20260824T0453Z-dd11599`
- Producer: Grok 4.6 via grok CLI `1.0.5 (5115b46bc909) [stable]`
- Adapter: `ops/adapters/grok.sh` (`--permission-mode bypassPermissions`, `--output-format plain`)
- Python: 3.14.6; host Darwin arm64; UTC at write `2026-08-24T05:02:33Z`
- Lane: independent Grok research ideator, sealed blind submission
- Basis commit: `dd11599b07eb05591b5c006791005eef19457d8e`
- State cutoff: `2026-08-24T04:53:35Z`
- Packet: `xmodel/ideation-20260824T0453Z-packet.md`
- Packet SHA-256: `042ff4d1d3754236d0ddcb7183e1f3903ef80e0a5e345952d27fe0cb1cbcadd5` (recomputed; match)
- Contract: blind submission. Read the packet and every required input it names, including all 46 rows of `APPROACHES.md`. Did not read any other `xmodel/ideation-20260824T0453Z-*.md` file. Did not inspect other agents' submissions. Did not promote a claim, launch compute, contact anyone, use the network, or edit a shared ledger.
- Stance: ideation, not promotion. Labels below are evidence tiers, lifecycle states, or experiment proposals. The three queued redesigns (typed global receiver/source, full D-source typing, bounded-complexity Witt descent of the present seed) are treated as candidates, not as an assignment.

## Hash verification and files actually read

All packet-listed SHA-256 hashes matched the files on disk at read time, with one listed digest shorter than SHA-256.

| Input | Packet SHA-256 | Result |
|---|---|---|
| `COORDINATION.md` | `ad6388abed8cf38f9a3688525dc976b4dd249e0ef1ff072856baf0a0591942b3` | match |
| `APPROACHES.md` | `302956aae6ac68d15805edab1c60c25f3c2a00001c8336dbd65590874b5cd89f` | match |
| `AUDIT.md` | `a0033b88030fbd73b1f342d64ed99f5568e4385f33d30f37124e69a17dcca32` | listed 63 hex chars; on-disk `a0033b88030f0bd73b1f342d64ed99f5568e4385f33d30f37124e69a17dcca32` |
| `PROGRESS.md` | `8a3f057a20d48379719a0b80381234b2ec7a4217debd2aab5c29d5c4472bccdc` | match |
| `notes.md` | `582f0f93562cf21b92fe3b7771a77f1cf7d3ba861c79b14d8b63b04fb66fb49b` | match |
| `xmodel/ideation-20260824T0156Z-synthesis.md` | `9c0455ddae2388d7f5256ec46094c0d97dd5bc6748f2b61177f736cc23581f50` | match |
| `xmodel/ideation-20260824T0156Z-dedup.md` | `69949b1432df0f100e3090dead3c3c9418858c8bda3bf0d7d9eaf20afa15444a` | match |
| `xmodel/round1-dtransition-fullcell-20260824.md` | `2b25b3ac5591360f2bac2f1c74f1c97bb936f1826f6aaed3d2969ad37be1f5df` | match |
| `xmodel/review-dtransition-fullcell-grok.md` | `9bdeb228e2f1778fa102607687a82aae44ee54bf9af03629c97524e9830af7da` | match |
| `xmodel/round2-norm-moment-sep-20260824.md` | `6bbdad39f53f17e39f59ebcc60d157722100b92cb858cfa9a127883d66515fa9` | match |
| `xmodel/review-norm-moment-sep-grok.md` | `f1a4a6d92d917ed3b05b38b2a4374793abc05293dcde4f51117a57ab67afcf06` | match |
| `xmodel/round2-dstate-gate-20260824.md` | `57536d0557d4aaaf267ce493c3236b33eed1c1d2829484e496211934ea78d512` | match |
| `xmodel/review-dstate-grok.md` | `b4a0fec6d4aa0e21ccaf325c8ad12b78c426b131698903500c018393251426dc` | match |
| `xmodel/round2-witt-oddprime-20260824.md` | `09b901f2a27f825a627da2ad0835d1875212716693769d505ab465b04bae6ff1` | match |
| `xmodel/review-witt-oddprime-claude.md` | `4660cff91b3cc07db6c4d7df7ace77bca5a282b33b103331124a9a3e17ddb008` | match |
| `xmodel/witt-tate-control-20260824.md` | `c38d0209b8bc4b4d2ad4fd3d371966fac5441e8e10c029d837647b6797fb8eb2` | match |
| `xmodel/review-witt-tate-control-claude.md` | `b3eae1f5a1420cec99bb8d75c8b0cddfd7a2db1e2027032e3f0be3b4fc6735a2` | match |
| `xmodel/round2-p4p1-honesty-20260824.md` | `c744c983c41055f45a509b0764b60d07312d5b172ef162183fa4342b7be1042f` | match |
| `xmodel/review-p4p1-honesty-grok.md` | `64a64c29493c46f86e05657457666b02ecab053cfe2e025ca914e6eb7af14d6e` | match |

Read scope, as required: `COORDINATION.md` full; `APPROACHES.md` full (all 46 avenues plus correction/overlay); `AUDIT.md` full (founding claims, msolve errata, 2026-08-23/24 promotions, G2 split, D/Witt/P4P1/receiver entries); `PROGRESS.md` current day `2026-08-24`; `notes.md` newest `LIVE STATE` only (`2026-08-24 04:00Z`); both named `0156Z` synthesis/dedup files full; all twelve named producer/review reports full.

Additional files read only for this report's format/version, not as mathematical premises: `ops/adapters/grok.sh`; the header of `xmodel/ideation-20260824T0156Z-grok.md` (previous-round format only). Workspace listing and `git rev-parse HEAD` / `shasum` were used to confirm basis `dd11599…` and to avoid opening other `0453Z` markdown files; those names were not opened.

Lifecycle used below, at cutoff only (all different-model confirmed at the stated scopes; none is a JC2 theorem):

- Full-cell D gate: modular nonempty locus on one `p=105337` `a00pp` cell; generic differential rank at least five; no rank-exactly-five, dimension, persistence, inverse limit, germ, or characteristic zero.
- `D-STATE-GATE`: exact six-band affine law on the pure-`y` source through band 40; `NO-TYPED-STATIONARITY` because `α_1,β_1` are untyped. No Ore/Spencer object.
- `NORM-MOMENT-SEP`: `DIFFERENT-INSUFFICIENT`. Native GGV type gate not reached.
- `W2-SURVIVOR` plus unrestricted all-Witt Artin–Schreier control: growing-support compatible tower; inverse limit restricted-analytic, not polynomial.
- `P4P1-SOURCE-HONESTY`: `ORIGIN-ONLY`; sidecar `42 S_M G_M (3α-2β) p^4 p'`; zero locus the line `3α-2β=0`.
- Holds remain as in the packet. No review debt. No live mathematical research lane. Box01 retains checkpointed `build_tails43.py` (PID 130360 at snapshot); do not stop it without accepting the recorded recomputation loss.

---

## Independent landscape, then hostility

Proof-side, JC2 remains: a finite étale endomorphism of \(\mathbb{A}^2\) is an automorphism. Constant Jacobian already gives étaleness over \(\mathbb{C}\); finiteness is the missing global assertion. Every honest rewrite — integrality of \(x,y\) over \(A=\mathbb{C}[P,Q]\), \(B=\mathbb{C}[x,y]\) equal to the integral closure \(\overline{A}\) of \(A\) in \(L=\mathbb{C}(x,y)\), emptiness of \(A(F)\), regularity of the first \(d\) power traces — is map-by-map equivalent to that missing finiteness. The 0156Z synthesis already recorded the exact ring inclusion \(\overline{A}\subset B\) supplied by Zariski's Main Theorem; the missing theorem is that the complementary open immersion has empty boundary, not that a finite receiver exists.

This round killed the remaining local costumes of that rewrite. Two exact Darboux completions share finite local algebra, different, conductor, selected contact, valuations, local two-form, and the first trace principal part, and still differ at \(\operatorname{Tr}(x^2)\). Coordinate multiplication carries the missing data. Therefore any proof that only names \(\overline{A}/A\) (different, complementary module, contact packet, first moment) is now a known non-proof. Hybrid GGV→Sigray still owes `G2-PSC`. A pure Sigray route may refuse GGV, and then still owes an independent source, complete landing/coverage, and a bounded/cofinal type menu; type-relative KJN is not that menu. Internal characteristic-zero emptiness for cCa2/cCa6 remains absent. External exact terminals on the two Proposition-4.3 residual systems do not prove the GGV reduction/transcription bridge.

Counterexample-side, three honest doors remain: a nonempty GGV family that algebraizes; a residue-A / D-series germ that algebraizes to a nonautomorphic polynomial pair; a characteristic-\(p\) collision that lifts with uniformly polynomial complexity. All three currently return data consistent with JC2 true. The new facts rearrange those doors rather than open one.

- The D-series is a correspondence with a nonempty modular compatibility locus of generic rank at least five on one cell, and a typed pure-`y` six-band law, and an untyped full source. The first omitted interface is exactly the P4P1 sidecar. The named origin is the sidecar-zero completion. Graph witnesses already sit off that line. Origin-centric D language is therefore the least CE-shaped reading of the banked data.
- The odd-prime Artin–Schreier seed survives \(W_2\) and then every finite Witt level once support may grow. Its coefficientwise limit is \((x-x^p, y/(1-p x^{p-1}))\), finite étale of rank \(p\) on the \(p\)-adic bidisc, determinant one, and not a polynomial endomorphism of affine two-space. Unrestricted finite Witt is closed for this seed. The control factorizes as \((x-x^p,y)\circ(x, y S_n(x))\): determinant-one normalization of a \(P_y=0\) family *forces* the geometric series. That slice is therefore not a polynomial CE source. A different mixing, or a different seed, would be required.

Hostile lens after that scan, not instead of it: do not infer a germ from a nonempty modular cell; do not treat rank \(\ge 5\) as dimension nine extra fiber; do not consume \(U_g^2=U_f^3\) to cancel \(3α-2β\); do not call the Tate limit a JC2 counterexample; do not run \(W_3\) on the same \(P(x)\)-only family; do not treat `ORIGIN-ONLY` as `SOURCE-ZERO` or as a licence for graph witnesses; do not build TRACE-REG or a local-different proof; do not launch band 28, integral D43, B=168, D75, new book cells, or primitive groups without a support bound.

The three queued redesigns are real, but they are not the highest-information next objects. Local receiver schema, Ore typing of the 30-state, and bounded descent of the *present* \(P_y=0\) seed each continue a stopped representation under a new name. The objects below start one step off those tracks.

---

## 1. Disposition vector (avenues 1–46)

Legend: `unchanged` / `raise` / `lower` / `reopen`. A reason is given only for a change. Rank here is research priority given this snapshot, not a probability that JC2 is true.

| # | Approach | Disposition | Reason if changed |
|--:|---|---|---|
| 1 | GGV Newton-polygon corner families + degree farm | **lower** | No `G2-PSC`; internal cCa certificates still owed; more farm does not globalize. |
| 2 | Sheet-number ladder / Eggers–Wall / dicritical trees | **lower** | No new landing/coverage; new book cells held; hybrid still owes transport. |
| 3 | Vertex-gap / strip ODEs / residue functional | unchanged | |
| 4 | Formal-germ certification + algebraization (D-series) | **reopen** | Current depth/Ore/origin representation is stopped. The live object is the sidecar line, not another window. |
| 5 | Jung–van der Kulk degree descent | **raise** | Tate factorization is a composition identity; amalgam/unit-twist language is now a CE discriminator. |
| 6 | Abhyankar–Moh one-place / coordinate recognition | unchanged | |
| 7 | Nonproperness / Jelonek \(A(F)\) | **raise** | After `DIFFERENT-INSUFFICIENT`, the ZMT boundary of \(\operatorname{Spec} B\to\operatorname{Spec}\overline{A}\) is the honest global object. This is not “compute \(A(F)\) from present books”. |
| 8 | Formal-inverse combinatorics | unchanged | |
| 9 | Lee–Li Conjecture E / Magnus remainder | unchanged | |
| 10 | HC4 ⇒ JC2 Hessian bridge | unchanged | Held; no new evidence. |
| 11 | Mathieu / GMC / Poisson / Zhao ladder | unchanged | Dead. |
| 12 | Face isolation / p-adic multinomials | unchanged | |
| 13 | Dixmier DC(2) | unchanged | |
| 14 | End(\(A_1\)) disproof / Zheglov DC(1) audit | unchanged | |
| 15 | Spectral surfaces / commuting PDOs | unchanged | |
| 16 | D-module / holonomic index | unchanged | Still no named invariant cheaper than the conductor of Card A. |
| 17 | BCW / Druzkowski / Yagzhev cubic | unchanged | |
| 18 | Graded / equivariant / GIT | **reopen** | Closed as a CE hunt (Shaska). Reopen only as a control on the cube/sidecar line, not as a search. |
| 19 | Char-\(p\) CE + Witt lifting | **reopen** | Unrestricted finite Witt of this seed is stopped. Mixed-support / \(P_y\neq 0\) and Ritt rigidity of the \(P_y=0\) slice are a different mechanism. |
| 20 | Reduction mod \(p\) / p-curvature formalism | unchanged | Known bridge still consumes false statements. |
| 21 | p-adic injectivity / Hensel / model theory | **raise** | The Tate control makes the missing uniform degree/support bound an explicit, witnessed compactness hypothesis. |
| 22 | Diophantine integral points / heights | unchanged | |
| 23 | Analytic global inverse / holomorphic analog | **lower** | An explicit det-1 noninjective restricted-analytic endomorphism now sits on disk. Analytic slogans fail in that category by example. |
| 24 | Real JC / Pinchuk deformation | unchanged | |
| 25 | Fiber monodromy / dessins / passports | **lower** | Raw passports and contact packets are costumes; coefficient convolution still has no source functor. |
| 26 | Primitive-monodromy td bound | **lower** | Still no independently proved support/type bound. Packet forbids proposing the census without it. |
| 27 | Links at infinity / splice diagrams | unchanged | |
| 28 | Log surfaces / BMY / log-Kodaira | unchanged | |
| 29 | LND / Hamiltonian completeness | unchanged | |
| 30 | Affine-surface classification / ML | unchanged | |
| 31 | Integrality / ZMT / Rees valuations | **raise** | Primary proof object this round: the conductor of \(\overline{A}\subset B\), which must see \(B\)-multiplication. |
| 32 | Off-diagonal collision ideal | unchanged | Still equivalent to injectivity without a handle. |
| 33 | Global symplectic exactness / action residues | **raise** | Cheapest polynomial-origin probe of the conductor gap; Darboux is now the hostile control that local two-forms fail. |
| 34 | 2D tangent-sweep / pole removal | unchanged | |
| 35 | Descent of dim \(\ge 3\) CEs | unchanged | |
| 36 | Guided CE search / sparse / SAT | **lower** | Generic sparse held; below-cutoff already empty; above-cutoff thin. |
| 37 | Finite-field census | unchanged | |
| 38 | Tropical geometry beyond Newton | unchanged | |
| 39 | Cohomological cluster | unchanged | |
| 40 | Free-associative Jacobian lift | unchanged | |
| 41 | Naive scaling deformation | unchanged | Dead. |
| 42 | Markus–Yamabe / Hurwitz realization | unchanged | |
| 43 | Ritt decomposition / composite coordinates | **raise** | New exact connection: the Tate tower is a composition, so Ritt-type rigidity applies to the \(P_y=0\) slice. |
| 44 | Moskowicz “no prime td” | unchanged | Unvetted; no new test. |
| 45 | Differential Galois / Liouvillian inverse | unchanged | |
| 46 | Lean / AI formalization-as-route | unchanged | Leaf identities only. |

---

## 2. Reranked bottlenecks after these deltas

Proof bottlenecks, in order:

1. **Polynomial origin of \(x,y\) as elements of \(B\), equivalently the conductor ideal \(\mathfrak{f}=(\overline{A}:B)_B\).** Exact rewrite of finiteness. Local different/contact/first-moment packets are now known not to determine even \(\operatorname{Tr}(x^2)\). This is not `G2-PSC` and not a GGV fingerprint schema.
2. **`G2-PSC`:** hybrid GGV→Sigray still has no provenanced packet-to-tree functor. Unchanged as a theorem debt; demoted as a compute root because this round supplied no new interface field.
3. **Complete landing/coverage** of an arbitrary Keller pair into a finite Sigray/book configuration, if the Sigray frame is used at all.
4. **Absolute/cofinal type menu.** Type-relative KJN remains local and one-way. Henon already refutes unrestricted UCD.
5. **Internal characteristic-zero cCa/R1 certificate repair**, wherever those artifacts are still invoked. External Helali/Suzuki terminals do not discharge the GGV-Horruitiner bridge.

Counterexample / falsification bottlenecks, in order:

1. **A uniformly polynomial-complexity lift that is not a \(P_y=0\) unit-twist of Artin–Schreier.** The present seed's \(P_y=0\) slice has an explicit all-Witt escape whose limit is nonpolynomial. The open CE door is mixed support at bounded degree, or a different seed.
2. **Algebraization of a D-series / residue-A germ off the sidecar-zero line.** The origin is the completion where the first x-side correction vanishes. Graph witnesses with \(\alpha\neq 0\) are the actual extra-state points and sit outside `ORIGIN-ONLY`. Band 28 and integral D43 remain the wrong next experiment.
3. **Algebraization of a nonempty GGV family**, still the only farm-shaped CE door, still blocked by transport and by the internal cCa gap.
4. **Algebraization of the formal DIR / A-SCALE Newton towers.** Failure to algebraize those families would not prove the bounds.

What dropped out of the leading ranks: unrestricted next Witt level; raw passports; contact-only TRACE-REG; local-different proofs; primitive-group enumeration; more D depth; DIR/A-SCALE census expansion.

---

## 3. Idea cards

Collectively: Card A is a new mechanism and the strongest proof attack; Card B is a new cross-avenue connection and the strongest counterexample/falsification attack; Card C is the software acceleration / decisive experiment, and redesigns D without continuing a stopped representation.

None of the three is “type a GGV receiver”, “type the 30-state recurrence”, or “descend the present seed through one more bounded Witt level”.

### Card A — Conductor of the ZMT open immersion

**Exact target claim (proposed theorem, not presently proved).** Let \(A=\mathbb{C}[P,Q]\), \(B=\mathbb{C}[x,y]\), \(L=\operatorname{Frac}(B)\), and \(\overline{A}\) the integral closure of \(A\) in \(L\). Then \(\overline{A}\subset B\) (exact, 0156Z synthesis correction 1; Japanese/Nagata finite generation of \(\overline{A}\) over \(A\) is classical). The conductor
\[
\mathfrak{f}=(\overline{A}:B)_B=\{b\in B: bB\subset\overline{A}\}
\]
cuts out the complement of \(\operatorname{Spec} B\) in \(\operatorname{Spec}\overline{A}\). JC2, for this map, is \(\mathfrak{f}=B\). This is a proof claim. It is not a reformulation of the different of \(\overline{A}/A\).

**Avenue IDs.** 31, 7, 33; controls from 32 and from the confirmed Darboux pair.

**Novelty.** New mechanism. The queued “typed global receiver” is a finite \(\overline{A}/A\) record (local algebra, different, tagged traces). `NORM-MOMENT-SEP` is the exact statement that that record, even with conductor-of-the-finite-extension and first moment, does not determine coordinate multiplication. The conductor of the *open immersion* is a \(B\)-ideal; it cannot be formed without \(B\)-multiplication. That is a different object from `PAIR-IR`, from Bacon's derivation lattice in \(\overline{A}\), and from Nash's proposed signed different. Zero-base in the sense that row 31 was untried as a JC2 program and is not one of the three queued redesigns.

**Evidence used.** Confirmed `DIFFERENT-INSUFFICIENT` and P2 collision; confirmed `COSTUME` on raw boundary passports; 0156Z exact inclusion \(\overline{A}\subset B\); dual-confirmed pure-boundary identity as the polynomial-origin two-form; automorphism and \((x^2,xy)\) controls already used by the receiver gate.

**Dependencies / evidence tiers.**

- Exact: ZMT inclusion, Japanese finiteness of \(\overline{A}/A\), definition of \(\mathfrak{f}\), Darboux separator, automorphism primitives exist and are polynomial.
- Exact conditional deduction: if \(\mathfrak{f}=B\) then \(B=\overline{A}\) is finite over \(A\), hence the map is finite étale, hence an automorphism of \(\mathbb{A}^2\) by the standard finite-étale theorem in dimension two. That deduction is not JC2; it is the named reduction.
- Heuristic: that \(\mathfrak{f}\) is cheaper to see on explicit maps than a GGV functor.
- Proposed experiment: the discriminator below.

**Cheapest discriminator (proposed experiment, \(\le\) one working day, no fleet).**

1. Re-derive \(\mathfrak{f}\) by hand for \(\operatorname{id}\) and for \(T_n=(x,y+x^n)\). Expected: \(\mathfrak{f}=(1)\). Negative control: if the implementation returns a proper ideal, the instrument is wrong (`RECEIVER-BUG` analogue).
2. Compute \(\overline{A}\) and \(\mathfrak{f}\) for \((x^2,xy)\). Expected: \(x\) integral, \(y\) not, \(\mathfrak{f}\) supported at the origin, matching the nonproper value \((0,0)\). If \(\mathfrak{f}=(1)\) here, the instrument is pole-blind.
3. Independently form \(f\,dg-x\,dy\) and \(g\,df-y\,dx\) for those three maps, and for one tame product of elementaries of degrees 3 and 4. Record polar divisors at infinity in two compactification charts. This is the row-33 experiment, now with Darboux as a *formal-local* hostile control: the same primitives exist for the Darboux pair and will see \(b\)-dependence exactly where traces do. The comparison asked is not “are primitives illegal for residue-A”; it is “do polynomial primitives determine more than the local two-form that Darboux holds fixed?”
4. Stop before any GGV farm parse, any book cell, and any claim that \(\mathfrak{f}=(1)\) for a general Keller pair.

**Outcomes and interpretation.**

- `CONDUCTOR-TAUTOLOGY`: on every polynomial test map one can write down, \(\mathfrak{f}=(1)\) for automorphisms and a proper ideal for \((x^2,xy)\), and the primitive polar divisor of automorphisms is already a consequence of \(J=1\) (`COSTUME`). Interpretation: the object is correct and not a new invariant. Stop the representation. Do not promote a lemma.
- `PRIMITIVE-SEES-MULTIPLICATION`: the polynomial primitives distinguish two maps that share the Darboux-fixed local packet, or the conductor of \((x^2,xy)\) is generated by an element invisible to the different of \(\overline{A}/A\). Interpretation: freeze one identity for hostile review. Maximum tier: exact lemma on explicit maps. No JC2 descendant.
- `NO-EXPLICIT-SOURCE`: one cannot form \(\mathfrak{f}\) without already knowing a finite presentation of \(B\) over \(A\). Interpretation: this is `NO-TYPED-FUNCTOR` on the \(B\)-side. Bank it. Do not pretend a GGV packet populates the conductor.

**Cost / time.** One reasoner, a few hours of exact computer algebra on maps of degree \(\le 4\); no AWS; no msolve.

**Stop condition.** First tautology, first instrument bug, or first missing field needed to form \(\mathfrak{f}\) for a non-written map. Two non-informative formulations stop the representation. No theorem descendant in the same generation.

**Expected information gain.** High per hour: either the proof object that survived `DIFFERENT-INSUFFICIENT` is a rename of finiteness, or it supplies a single covariant polynomial-origin identity that local packets lack. That is the strongest remaining proof attack because every weaker packet has already failed an exact control.

**Resurrection trigger.** A native polynomial source that populates \(B\) as an \(A\)-algebra (a real GGV pair, or a completed book with affine coordinates). Then \(\mathfrak{f}\) becomes a computational target rather than a slogan. Until then, only explicit maps.

### Card B — \(P_y=0\) rigidity and mixed-support escape

**Exact target claim, in two layers.**

1. **Exact conditional deduction, already essentially on disk.** For odd \(p\) and every \(n\), the maps \(F_n=(x-x^p, y\sum_{j=0}^{n-1}(p x^{p-1})^j)\) are the unique determinant-one polynomial lifts of \((x-x^p,y)\) in the *restricted class* \(P\in R_n[x]\), \(Q\in y\cdot R_n[x]\) (no \(P_y\), \(Q\) linear in \(y\)). Their degrees grow linearly, and the inverse limit is not polynomial. This is the Tate control plus the reviewer's factorization \(F_n=(x-x^p,y)\circ(x,y S_n)\). It is not a new computation; it is the structure theorem of the stopped slice.
2. **Proposed theorem / proposed experiment.** There is no uniformly bounded-degree polynomial Keller lift of the marked Artin–Schreier collision in which \(P\) is allowed to depend on \(y\) at order \(p\) and higher, in degrees \(\le 4\) over \(W_2(\mathbb{F}_3)\) and, only if a survivor appears with \(\deg\le 4\), through one further bounded level. Separately: any characteristic-zero polynomial map that reduces to a \(P_y=0\) Artin–Schreier map is composite in the Ritt sense with a univariate twist, hence cannot stay of bounded degree while keeping \(J=1\).

**Avenue IDs.** 19, 43, 5, 21. Not a revival of unrestricted \(W_3\).

**Novelty.** New cross-avenue connection: Ritt / JvdK composition (rows 43, 5) with the confirmed Tate factorization (row 19), plus a *transverse* mixing space that the queued “bounded-complexity descent of this seed” never opened. The present seed and both enumerators froze \(P\in k[x]\) and \(Q=y\) on the special fibre; the \(W_2\) correction added \(x^2 y\) to \(Q\) but never mixed \(y\) into \(P\). Reviewer C2/C3 and the restricted 24-column box already flag that the correction space was a witness-finder. The new mathematical object is the first-order mixed correction
\[
P=x-x^p+p A(x,y),\qquad Q=y+p B(x,y),
\]
with \(A,B\) of bounded degree, not another truncation of \(S_n\).

**Evidence used.** Confirmed `W2-SURVIVOR`; confirmed all-Witt control and factorization; confirmed Mondello char-2 stratum remains dead on a different support; `sol-witt.md` §6 criterion (fixed support or polynomial limit), now witnessed.

**Dependencies / evidence tiers.**

- Exact: identities (1.1)–(4.3) of the Tate control; \(P_y=0\) slice degree growth; Mondello never-vanishes on its stratum.
- Exact conditional: if a polynomial lift exists with \(\deg\le D\) at every Witt level, the inverse limit is polynomial of degree \(\le D\). Contrapositive: the Tate tower is excluded from every bounded-degree theorem. This does *not* exclude mixed \(A,B\).
- Heuristic: a genuine plane CE, if one comes from this special fibre, must mix \(y\) into \(P\) to cap degree.
- Proposed experiment: the bounded mixed census.

**Cheapest discriminator (proposed experiment).**

Freeze before execution: \(p=3\), marked collision \((0,0),(1,0)\mapsto(0,0)\), \(\deg A,\deg B\le 3\), work in \(W_2(\mathbb{F}_3)=\mathbb{Z}/9\), exhaust the coefficient space of \((A,B)\) modulo the already-known particular solution \((A,B)=(0,x^2 y)\) and modulo linear automorphisms that preserve the special fibre. Stdlib polynomials, no solver farm, no \(W_3\) unless a survivor has \(\deg\le 3\) *and* a preregistered uniform-degree predicate.

In parallel, on paper: prove or refute the uniqueness statement that every \(P\in R_n[x]\), \(Q\in y\cdot R_n[x]\) solution is \(F_n\) up to \(R_n^\times\). That is an exact structure lemma, not a search.

**Outcomes and interpretation.**

- `SLICE-RIGID + MIXED-EMPTY`: \(P_y=0\) uniqueness holds and the degree-\(\le 3\) mixed scheme over \(\mathbb{Z}/9\) is only the known twist, up to automorphism. Interpretation: this special fibre is a dead polynomial-CE seed at the first mixed cap. Stop avenue 19 on Artin–Schreier. Do not enlarge support. Do not say JC2 is true.
- `MIXED-W2-SURVIVOR`: a mixed \((A,B)\) of degree \(\le 3\) gives a det-1 collision over \(\mathbb{Z}/9\) not equivalent to \((0,x^2 y)\). Interpretation: freeze for different-model review. It is a finite-ring object. One bounded \(W_3\) child is permitted only if the same degree bound is part of the freeze; otherwise stop.
- `SLICE-NOT-RIGID`: a bounded-degree \(P(x)\)-only lift other than \(F_n\) exists at some \(n\). Interpretation: the Tate control is not the universal escape; reopen bounded descent of the original seed. This would invalidate part of the ranking below.

**Cost / time.** Structure lemma: hours. Mixed census at degree 3 over \(\mathbb{F}_3\): coefficient count is small enough for exact enumeration on a laptop (after torus/linear normalization). No box01 interaction.

**Stop condition.** First mixed survivor (review, do not expand), empty mixed cap at the frozen degree (stop the seed), or a proof that mixing cannot cancel degree growth (stop the seed). No unrestricted level. No characteristic-zero inference from one finite ring.

**Expected information gain.** Highest CE-side value in the snapshot: the only live Witt seed has just been shown to escape *in the category the campaign was using*. Either mixed support reopens a genuine polynomial door, or Artin–Schreier is retired the way Mondello's char-2 stratum was retired.

**Resurrection trigger.** A different char-\(p\) collision, not Aut-equivalent to Artin–Schreier or to the Mondello hull-plus-shell, with a vanishing first Witt class and a *uniform* degree bound stated before search. Or a proof that every plane Keller reduction mod \(p\) is composite-univariate, which would be a proof-side Ritt theorem and would move this card out of the CE column.

### Card C — Sidecar line, unit-twist software, no new depth

**Exact target claim (proposed experiment plus one exact identity already confirmed).** The first full-source interface
\[
[t^{42}]\mathcal{E}_{\mathrm{full}}=[t^{42}]\mathcal{E}_y+42 S_M G_M(3\alpha_1-2\beta_1)p(\eta)^4 p'(\eta)
\]
is the same polynomial as the P4P1 sidecar, and its zero locus is the line \(3\alpha-2\beta=0\). That line contains every named D43 origin completion. It does not contain the graph-reconstruction witnesses. The proposed claim to test, *not* to assume, is:

> Polynomial origin plus the residue-A leading-form ratio \((F_0,G_0)\propto(p^2,p^3)\) forces the x-side factors onto the cube line at first order, and the cube line plus \(J=1\) is automorphism-shaped (origin, not extra fiber).

This is not an Ore stationarity theorem and not a classification of \(\alpha,\beta\) as held/derived/independent.

**Avenue IDs.** 4, 18, 5, 43. Software also serves Card B.

**Novelty.** New connection among confirmed objects: D-state row-42, P4P1 sidecar, residue-A \((2,3)\) genome, and the closed graded-plane theorem (row 18) as a *control*, not as a CE hunt. The software object is a unit-twist factorizer: given \(F\), decide whether \(F=A\circ U\) with \(U=(x, y\cdot s(x))\) or \((x, y+h(x))\). That instrument does not exist in-repo; it is what makes the Tate factorization and the Euler factorization \(\Phi_{\mathrm{full}}=U_f\Phi_y\) the same kind of thing.

**Evidence used.** Confirmed `NO-TYPED-STATIONARITY`; confirmed `ORIGIN-ONLY` and the line \(3\alpha-2\beta=0\); confirmed graph witnesses with \(\alpha\in\{93268,98561\}\), \(\beta=0\), off the line (review of P4P1, not a D43 nonemptiness claim); confirmed pure-`y` six-band law; Shaska 2026 graded automorphy as a literature control, to be source-checked before use; Tate factorization as the model unit-twist.

**Dependencies / evidence tiers.**

- Exact: the displayed identity; origin vanishing; line as zero locus; graph witnesses off the line; pure-`y` affine law at two primes through band 40.
- Exact forbidden: `CONJECTURE X-CUBE-RELATION` / \(U_g^2=U_f^3\) as a licence to set \(3\alpha-2\beta=0\). The D-state review already quarantines that move.
- Heuristic: origin = automorphism-shaped completion; extra fiber, if any, lives off the line.
- Proposed experiment: factorizer plus a first-order sidecar adjoint on *existing* full-cell Jacobians. No band 28, no D43 point, no integral emitter.

**Cheapest discriminator.**

1. **Software (unit-twist factorizer).** Exact univariate/bivariate polynomial division. Replay: \(T_n\); tame products; \(F_n\) at \(n=1,2,3\) for \(p=3\); the Euler leading jet \((S_M p^2, G_M p^3)\). Negative control: a random degree-4 map must fail to factor. Byte-replay the Tate identity \(F_2=(x-x^3,y)\circ(x,y(1+3x^2))\) over \(\mathbb{Z}/9\).
2. **Sidecar adjoint, existing cell only.** Treat \((3\alpha-2\beta)\) as an external linear form, not as a new tail. Re-evaluate the six confirmed compatibility functions at the origin (must remain zero) and at one stored graph witness's \((\alpha,\beta)\) *symbolically in that form only*. Do not assemble band 28. Do not call `eplus43` as a source classification. Ask one question: does the first x-side correction, as a linear form, lie in the span of the six functions or in a new direction?
3. **Graded control (literature, source-check first).** If Shaska's statement applies only to globally weighted-homogeneous maps, it does *not* force the cube line. Record `NO-GRADED-BRIDGE` and stop that branch. Do not quote it as a D-series theorem.

**Outcomes and interpretation.**

- `LINE-IS-GAUGE`: the sidecar form is linearly dependent on the six compatibility functions at the origin, and the factorizer sees only triangular automorphisms. Interpretation: extra x-side state is not new fiber at first order. Does *not* license Ore, band 28, or `STATIONARY-SOURCE-SIGNAL`.
- `LINE-IS-NEW-DIRECTION`: the sidecar form is independent of the six functions, and graph-witness \((\alpha,\beta)\) is a genuine extra coordinate. Interpretation: the origin is the wrong CE point; the D-series, if it is a CE door, lives off the line. Still modular, still not a germ. Integral D43 remains held. The honest next D question is a source classification of \(\alpha,\beta\), which is a *later* redesign, not this card.
- `FACTORIZER-SEES-TATE-ONLY`: the instrument works and finds no other bounded twist. Interpretation: software success, no D theorem.
- `GRADED-DOES-NOT-APPLY`: stop the Shaska branch. Expected, and not a failure of the card.

**Cost / time.** Factorizer: a few hours. Sidecar adjoint: a few hours on the already-reviewed cell, stdlib, no Groebner. No box01, no band 28.

**Stop condition.** Any attempt to emit band 28, to import `eplus43` as a typed state map, to consume \(U_g^2=U_f^3\), or to promote a germ. Two non-informative linear-algebra outcomes stop the adjoint. The factorizer remains reusable for Card B.

**Expected information gain.** High for allocation: it decides whether the campaign's origin-centric D43/D-state language is looking at the automorphism completion. That is the D-series redesign this round actually owes. Software reuse across Cards B and C is the acceleration.

**Resurrection trigger.** A source-derived chain rule that types \(\alpha,\beta\) as held, derived, or independent *without* inventing the state map. That would reopen a finite full-source state, and only then an Ore/Spencer object. Not before.

---

## 4. Lane calls

| Lane | Call | Scope |
|---|---|---|
| **D-series** | **redesign** | Stop the current representation: no band 28, no Ore/Spencer/Fitting, no all-depth claim, no origin-as-CE, no integral D43. The pure-`y` six-band law may be cited as a scoped modular fact. Next D work, if any, is Card C (sidecar line / unit-twist), not full-source typing of the 30-state. |
| **GGV/Sigray** | **stop** as a live compute root; **theorem debt unchanged** | No new book cells, no farm expansion, no residue-A F4. Hybrid still owes `G2-PSC`. Pure Sigray still owes source, landing/coverage, and a type menu. This round did not supply an interface field. Keep the fork on paper. |
| **Boundary/trace** | **redesign** onto Card A; **stop** the local packet | Raw passports remain `COSTUME`. TRACE-REG remains a finiteness rename. Local different/contact/first-moment proofs are `DIFFERENT-INSUFFICIENT`. Continue only polynomial-origin conductor/primitives on explicit maps. Native GGV type gate stays unreached and must not be backfilled from this packet. |
| **Local-bound programs** | **stop** | No DIR/A-SCALE/KJN census, no sublinear-type hunt, no unrestricted delay. Henon already killed unrestricted UCD. Formal Newton towers remain algebraization questions, not book jobs. Keep the local arrows as written. |
| **Witt** | **redesign** | Unrestricted finite Witt of this seed is stopped. Bounded descent of the *same* \(P_y=0\) family is the Tate series under a degree cap, hence empty as a polynomial limit. Next is Card B: slice rigidity plus mixed support. Char-2 Mondello stratum stays closed. |
| **External artifacts** | **stop** as a research root | Preserve the SuperMind/Guo/Helali/Suzuki *conditional* perimeter. Coordinate equivalence is not an independent vote. No author contact, no public wording, no msolve disclosure. Internal cCa/R1 char-0 repair remains owed if those strata are reused. |

Box01: do not kill PID 130360 / `GB42` without accepting the recorded recomputation loss. Box02/Box03 stay stopped.

---

## 5. Hidden assumptions, self-attack, invalidating event

**Shared hidden assumptions of the three cards.**

1. Polynomial origin is the only remaining information after local \(\overline{A}/A\) data were separated from coordinate moments. If some other global, non-polynomial invariant determines \(\operatorname{Tr}(x^2)\), Card A is mis-aimed.
2. Artin–Schreier is still the right odd-prime CE seed to attack. It may be as special as Mondello's stratum: a composition, not a generic collision.
3. The D-series origin is automorphism-shaped because the sidecar vanishes there. That is a reading, not a theorem; a continuous gauge could still eat the rank-5 kernel.
4. Explicit low-degree maps are informative about general Keller pairs. They may only see automorphisms and one non-Keller nonproper map, i.e. the already-used control suite.
5. Mixed \(A(x,y)\) of degree \(\le 3\) is a large enough first cap to retire the seed if empty. A CE might start at degree 4 or at \(p=5\).

**Hostile attack on the leading proposal (Card A).**

Computing \(\mathfrak{f}\) for a general Keller pair *is* the compactification problem. On maps one can write down, \(\mathfrak{f}=(1)\) for automorphisms by definition of invertibility, and a proper ideal for \((x^2,xy)\) by a calculation the campaign already knows in other language. The Darboux family is not a polynomial \(B\), so it cannot certify a conductor identity in the JC2 category; it can only kill objects that ignore \(B\). Row-33 primitives on tame automorphisms are the experiment Grok already specified in the 46-row shortlist; `COSTUME` predicts they will see \(J=1\) and nothing else. So Card A may spend a day reconfirming that finiteness is finiteness, then stop. That is an acceptable information outcome, and it must be pre-registered as `CONDUCTOR-TAUTOLOGY`, not dressed as progress. The only way the card is more than a rename is if the conductor of \((x^2,xy)\), or the primitive of a tame product, produces an element that the confirmed local packet cannot see. If it does not, the proof ranking in §2.1 collapses back to `G2-PSC` plus a type menu, which this round did not improve.

**Event that invalidates the ranking.**

Any one of: a polynomial-origin identity that *does* determine the quadratic moment from the local packet (reverses the interpretation of `DIFFERENT-INSUFFICIENT`); a bounded-degree \(P(x)\)-only all-Witt polynomial lift other than a coordinate change of \(F_n\) (`SLICE-NOT-RIGID`); a source-derived proof that \(3\alpha-2\beta=0\) identically for polynomial D-series maps (collapses the sidecar, reopens pure-`y` Ore); a continuous gauge accounting for the full rank-5 kernel (kills CE-shaped D rhetoric); or an external proof or characteristic-zero counterexample of JC2.

---

## 6. Proposed four-root portfolio

Respects holds, empty review debt, background-only coordination, and the one-generation speculative limit. No root consumes an unreviewed claim. No fifth mathematical root. Box01 is not a research root.

| Root | Share | Work now | Review / provisional discipline | Hard stop |
|---|---:|---|---|---|
| **C — coordination** | 15% | Bank this round; maintain holds and the claim DAG; adjudicate box01 at the next checkpoint without killing `GB42`; complete web sweep #9 by `2026-08-24 21:25Z`. No mathematical child. | None. | Quarantine only affected descendants on a later reversal. |
| **P — polynomial-origin conductor / primitives** | 35% | Card A on explicit maps only. | Independently re-derive \(\mathfrak{f}\) and primitives; different-model review of any surviving identity before a descendant. | `CONDUCTOR-TAUTOLOGY`, instrument bug, or `NO-EXPLICIT-SOURCE`. |
| **F — mixed-support / Ritt rigidity of AS** | 30% | Card B: paper uniqueness of the \(P_y=0\) slice, then the frozen degree-\(\le 3\) mixed \(W_2\) census. | Different-model replay of any mixed survivor. At most one explicitly provisional bounded-degree \(W_3\) child, and only if the degree cap was frozen before the \(W_2\) run. | Mixed empty at the cap; slice uniqueness plus no mixed survivor; any unrestricted level or support expansion. |
| **D — sidecar-line / unit-twist instrument** | 20% | Card C: factorizer first (also serves F), then the linear sidecar adjoint on the reviewed cell. | No D43, no `eplus43` as state map, no cube-relation consumption. Review the factorizer as software before using it as evidence. | Band 28, integral D43, Ore object, or two non-informative adjoint outcomes. |

Deferred, not launched: typed GGV receiver / native type gate (no source functor, previous R-root stopped at `DIFFERENT-INSUFFICIENT`); full D-source Ore typing (no state map); bounded descent of the present \(P_y=0\) seed (Tate series); primitive groups; HC4; new book cells; cCa6 F4; generic sparse; public communication.

Why this is not a selection among the three queued redesigns: P is a \(B\)-ideal, not an \(\overline{A}/A\) receiver schema; F is mixed support plus Ritt, not another truncation of \(S_n\); D is a line geometry / factorizer, not a 30-state classification. The queued three remain available if these roots tautologize.

---

**Frozen.** This report edits no shared ledger and launches no descendant. It does not promote a claim.
