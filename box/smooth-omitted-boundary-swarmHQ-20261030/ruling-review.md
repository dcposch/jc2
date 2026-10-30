# PROJECTIVEREVIEW2325 — hostile review of the projective-base graph lemma

Verdict: **PASS_CONDITIONAL.** The abstract graph-extension lemma is correct under the exact hypotheses stated below. Its application to a hypothetical Keller normalization remains conditional on the imported normal-affine/open-immersion package; that package was supplied as an input premise and was not re-audited here. The lemma is a structural reduction, not a polynomial Keller exclusion.

Requested reviewer was the existing Sol adapter/model `gpt-5.6-sol`, ultra. Actual hosted identity is unverified. This was a sole hostile review: no agent, job, worker, or coordinator action was launched.

## Exact accepted statement and hypotheses

Let `R=C[x,y]`, let `X=Spec B` be a finite-type normal integral affine surface over `C`, and let the specified map `j:U=Spec R -> X` be a dense open immersion. Via restriction, identify `B` with its image in `R`; density also identifies `Frac(B)=Frac(R)`. Pick any nonconstant `b in B`. If `ell` is outside the finite set of source linear forms described below, then

1. `R=B[ell]`;
2. the rational function `ell in Frac(B)` extends uniquely by the construction to a morphism `q:X->P1`;
3. scheme-theoretically, `q^{-1}(A1)=U`, and for every geometric finite base point `c`, `q^{-1}(c)=Spec(Cbar[v])` after the corresponding base change, hence is the reduced coordinate `A1`;
4. `q^{-1}(infinity)` is an effective Cartier divisor whose support is exactly `X\U` (the empty Cartier divisor if the boundary is empty).

No smoothness of `X`, regularity of `ell` on all of `X`, connectedness/reducedness/smoothness of the infinity fibre, Cartier property of each boundary component, or coefficient bound is needed or obtained.

## 1. Generic monicity really gives finiteness

Let `d>0` be the total degree of the image of `b` in `C[x,y]`, and let `b_d` be its nonzero top homogeneous form. A linear form `ell` is bad precisely when `b_d` vanishes on the one-dimensional direction `ker(ell)`. On `P1` this is a finite set. For any other `ell` and any complementary linear coordinate `v`, the coefficient of `v^d` in `b(ell,v)` is nonzero. Scaling `b` by that nonzero constant, which neither leaves `B` nor changes `C[b,ell]`, makes

`b(ell,v)=v^d+a_{d-1}(ell)v^{d-1}+...+a_0(ell)`.

Thus `v` satisfies a monic equation over the actual subring `C[b,ell]`. Since `R=C[ell,v]`, the powers `1,v,...,v^{d-1}` generate `R` over `C[b,ell]`. They also generate it over the intermediate ring `B[ell]`. Therefore `R` is finite over `B[ell]`. This argument neither assumes that `b` is a source coordinate nor assumes the conclusion `R=B[ell]`.

## 2. The finite graph is a closed immersion

For `G=(j,ell):U->X x A1`, the coordinate map is

`B[T] -> R,  T |-> ell`.

The preceding module finiteness makes `G` finite. It factors as the closed graph immersion `U->U x A1` followed by the open immersion `U x A1->X x A1`; hence `G` is an immersion. The standard theorem that a finite immersion is a closed immersion now applies. Consequently the displayed ring map is surjective, which is exactly

`R=B[ell]`.

There is no circular use of this equality: finiteness was established first from the one chosen nonconstant element `b`.

## 3. Closure acquires no finite-`ell` boundary

Let `Z` be the scheme-theoretic closure of `G(U)` in `X x P1` and put `Gamma=Z_red`. Restricting a scheme-theoretic closure to an open subscheme gives the closure there. Because `G(U)` is already a closed reduced subscheme of `X x A1`,

`Gamma intersect (X x A1)=G(U)`

as schemes, not just as sets. Similarly, the graph of `ell:U->P1` is closed in `U x P1`, so `Gamma intersect (U x P1)` is exactly that graph. These equalities of open subschemes remain equalities after arbitrary base change. In particular, over any geometric point of `X\U`, every point of the base-changed fibre of `Gamma->X` lies on the base-changed infinity section; no finite-`ell` boundary point, reduced or infinitesimal, is being discarded.

The topological closure of the integral graph is irreducible, and reduction makes `Gamma` integral.

## 4. Projection is an isomorphism without smoothness

The projection `p:Gamma->X` is projective and is an isomorphism over the dense open `U`, hence birational. Its image is closed by properness and contains `U`, so it is all of the integral `X`.

Over a geometric point of `U`, the fibre is the graph point. Over a geometric point of `X\U`, the preceding open-subscheme equality confines the fibre to the single point of the infinity section, while surjectivity makes it nonempty. A finite-type scheme over a field with one-point support is zero-dimensional and finite over that field, even if nonreduced. Thus all geometric fibres of `p` are finite, so `p` is quasi-finite. Proper plus quasi-finite makes `p` finite.

Finally, on any affine open `Spec A` of normal `X`, the finite inverse image is `Spec C` with `A subset C subset Frac(A)` and `C` integral over `A`; birationality gives the middle inclusion into the same fraction field. Integral closedness of `A` gives `C=A`. Hence `p` is an isomorphism. Normality is used exactly here; neither regularity nor surface smoothness is hidden in the argument.

## 5. Scheme fibres and the exact Cartier/multiplicity conclusion

Transporting the second projection through `p^{-1}` gives `q:X->P1`. The equality in Section 3 transports to the scheme-theoretic equality

`q^{-1}(A1)=U`,

and `q|_U=ell`. Therefore for every finite geometric `c`, the fibre is cut out inside `Cbar[ell,v]` by `ell-c` and is `Spec Cbar[v]`: an actual reduced coordinate line, not merely a set-theoretic `A1`.

The point `infinity` is an effective Cartier divisor on `P1`. The morphism `q` is dominant because its restriction `ell:A2->A1` is dominant. Consequently a local equation for `infinity` pulls back to a nonzero element at the generic point of the integral `X`, hence to a nonzerodivisor. Its pullback is therefore an effective Cartier divisor. Its open complement is the already verified `U`, so its support is exactly `E=X\U`.

If `E` has prime components `E_i`, normality permits the Weil-divisor expression

`q^*(infinity)=sum_i m_i E_i`, with `m_i=ord_{E_i}(q^*(infinity))` positive integers.

That is the full multiplicity conclusion. The proof supplies no assertion that any `m_i=1`, no upper bound, no common-multiplicity restriction, and no assertion that an individual `E_i` is Cartier. The total combination is Cartier. Normality/S2 and the nonzerodivisor make the fibre pure of codimension one, but do not make it reduced, smooth, irreducible, or connected. If `E` is nonempty, `q(U)=A1` and `q(E)={infinity}`, so `q` is surjective.

## 6. Retained control and the absence of a regular source coordinate

For the supplied control

`B=C[a,b,z]/(ab-z(z-1)(z-2))`, `z=uv`, `a=u(z-1)`, `b=v(z-2)`,

put `ell=u+v`. Directly,

`a+b=ell*z-u-2v`,

so

`u=a+b-ell*z+2ell`, and `v=ell*z-ell-a-b`.

Thus both `u` and `v` lie in `B[ell]`, proving `C[u,v]=B[ell]` exactly as claimed. At the generic point of `D1={b=0,z=1}`, the formula `u=a/(z-1)` gives a simple pole of `ell`; at the generic point of `D2={a=0,z=2}`, `v=b/(z-2)` does the same. Here the infinity fibre is the disconnected reduced divisor `D1+D2`, illustrating at least the claimed absence of connectedness.

The old all-functions obstruction is also consistent. In its normal form, the leading exponent pairs are `(j,j)`, `(2i+j,i+j)`, and `(i+j,2i+j)`; they are pairwise distinct in their respective ranges. Hence the top form of every nonconstant element pulled back from `B` is divisible by `uv`. Every level curve then has both projective infinity points `[1:0:0]` and `[0:1:0]`, whereas a polynomial coordinate level has only the single image of parameter infinity. Thus no source polynomial coordinate lies in `B`, in particular `ell` does not. The equality `R=B[ell]` only adjoins the rational function `ell`; `q` makes it projective-valued at the boundary rather than a regular `A1`-valued function on all of `X`. There is no conflict.

## Remaining Keller gap

For a hypothetical Keller pair, the application additionally imports that its finite normalization `A=C[P,Q] subset B subset R` is a normal affine `X=Spec B` containing the whole marked `U=Spec R` by a dense open immersion. Taking the nonconstant `b=P` then satisfies the abstract lemma for generic `ell`.

What remains is a genuinely Keller-specific argument showing that the infinity fibre `E` is empty (or otherwise deriving a contradiction) from the finite map `X->Spec A` and the constant-Jacobian source map. The conclusions `R=B[ell]` and `sum m_iE_i` Cartier do not put `ell` in `B`, do not make `ell` integral over `A`, and do not make `R` finite over `A`. They give neither `N=1`, properness/surjectivity of the original polynomial map, nor JC2. This is the remaining polynomial Keller gap; the graph lemma is only the projective-base structural reduction. No stopped complete-base family is reopened, and no exit-price assertion is made.

## Independent custody and coverage

Measured events:

- First action: `2026-10-29T23:23:40.747923487Z`, measured immediately before the first manifest window in the same command.
- Full nine-governor plus `HQ-STATE.md` coverage was observed complete at `2026-10-29T23:26:47.501023106Z`.
- A substantive unsealed partial was observed to exist after its write at `2026-10-29T23:27:53.831389459Z`, SHA-256 `880016b75e17c285e739df547981c34e24cbd001d778eecd1cd4e642f436782a` at that observation.
- The complete input post-hash pass was observed complete at `2026-10-29T23:29:38.509661274Z`.
- Terminal body and final post-seal existence times are necessarily established by commands after writing stops; no preceding clock is labeled a write-completion time.

The manifest was read first and completely. Its SHA-256 was the required `7cf1787b4ff6732509f3d03d7601b026f39555d4c7c335272dd9b43684762598`. One metadata-only pass covered every declared record before any declared body: exact bytes/LF below, actual launcher snapshot mode `0400` for every file, and no symlink ancestor or symlink leaf. The manifest declares original packet mode `0444`; original provenance paths were not read. Candidate and control seals were verified before either body:

- `candidate.md`: verifier PASS, body bytes `4210`, body SHA-256 `0009790aec1450b97bd80e89515345f47c5ef0798983f75fab390faffbf2fc2f`, basis `a0b799468cd065da71cbd13b8bb578438ca5e9f3`.
- `ruling-control.md`: verifier PASS, body bytes `8465`, body SHA-256 `e950fc314e136dffe1162dd6034001819b0896f3e9e86071c2ae2611696d0baf`, basis `0d39df3c9fd69c939a8420c54d03228b9077777d`.

Exact metadata and pre/post full-file hashes (the twelve declared records, plus the manifest) were:

- `input-manifest.json`: `5610` bytes, `163` LF, mode `0400`, no symlink component; pre `7cf1787b4ff6732509f3d03d7601b026f39555d4c7c335272dd9b43684762598`; post `7cf1787b4ff6732509f3d03d7601b026f39555d4c7c335272dd9b43684762598`.
- `HQ-AGENTS.md`: `1520` bytes, `23` LF, mode `0400`, no symlink component; pre `06ba4c0898c8a4272478b16f8b72f2877cf235ed3a8af5016059d1114dd0c34f`; post `06ba4c0898c8a4272478b16f8b72f2877cf235ed3a8af5016059d1114dd0c34f`.
- `HQ-POLICY.md`: `6755` bytes, `112` LF, mode `0400`, no symlink component; pre `6e53d77c4bfca8553df5510bbe5f94f7d0955347c4d8bba58a67e4c15a275634`; post `6e53d77c4bfca8553df5510bbe5f94f7d0955347c4d8bba58a67e4c15a275634`.
- `HQ-RESEARCH_POLICY.md`: `9551` bytes, `162` LF, mode `0400`, no symlink component; pre `1ce21f90ddbfad47bdbeff07940f1704643465df5a0bd8446fc2b8e9cc614c62`; post `1ce21f90ddbfad47bdbeff07940f1704643465df5a0bd8446fc2b8e9cc614c62`.
- `HQ-RESTRICTIONS.md`: `18817` bytes, `259` LF, mode `0400`, no symlink component; pre `f90beac94a223085b0b4d342138a40200b2779869d0d29fc75caf4a0a60477ed`; post `f90beac94a223085b0b4d342138a40200b2779869d0d29fc75caf4a0a60477ed`.
- `HQ-RUNBOOK.md`: `34745` bytes, `507` LF, mode `0400`, no symlink component; pre `4e874134c6bbb925415545050eb3e30de3d61171899ba727ed2123c9a3eb0c06`; post `4e874134c6bbb925415545050eb3e30de3d61171899ba727ed2123c9a3eb0c06`.
- `HQ-STATE.md`: `59674` bytes, `222` LF, mode `0400`, no symlink component; pre `df2802a069b58c08e64a5abd68e72fb5f173291e24b10e3f246e75636429138f`; post `df2802a069b58c08e64a5abd68e72fb5f173291e24b10e3f246e75636429138f`.
- `PUBLIC-AGENTS.md`: `1229` bytes, `22` LF, mode `0400`, no symlink component; pre `31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f`; post `31f54fa5b1a9f76dc5455dd6c42615e565b47b96499c6fc69f389980e762a96f`.
- `PUBLIC-README.md`: `5391` bytes, `102` LF, mode `0400`, no symlink component; pre `7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf`; post `7181a9dd4cf928e5327ee5324ccf7861098e2b7321395852418aa8c7808fbbdf`.
- `PUBLIC-COORDINATION.md`: `6042` bytes, `107` LF, mode `0400`, no symlink component; pre `9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e`; post `9b7a45ae6bd49550a0da48c7a27cee2bef9c8db37a8a95f53110f1c17705d46e`.
- `PUBLIC-FALLACY-v2.md`: `1985` bytes, `36` LF, mode `0400`, no symlink component; pre `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5`; post `e47fd16cfcc91bc7bfdac4ba1b5f46152db8235e6609dca6e29a5966549c38f5`.
- `candidate.md`: `4542` bytes, `42` LF, mode `0400`, no symlink component; pre `d86012d37f83631b4a61744362c3e836776bd5c66324062b772b380775bb69f3`; post `d86012d37f83631b4a61744362c3e836776bd5c66324062b772b380775bb69f3`.
- `ruling-control.md`: `8797` bytes, `84` LF, mode `0400`, no symlink component; pre `5585d8b34b45552330a95950fd01c4907f70527ea5d5f9c3b10b016ae5e160ce`; post `5585d8b34b45552330a95950fd01c4907f70527ea5d5f9c3b10b016ae5e160ce`.

Actual displayed body ranges were contiguous and complete:

- `input-manifest.json`: `1-24,25-48,49-72,73-96,97-120,121-144,145-163` (`163` LF).
- `HQ-AGENTS.md`: `1-23` (`23` LF).
- `HQ-POLICY.md`: `1-24,25-48,49-72,73-96,97-112` (`112` LF).
- `HQ-RESEARCH_POLICY.md`: `1-24,25-48,49-72,73-96,97-120,121-144,145-162` (`162` LF).
- `HQ-RESTRICTIONS.md`: `1-24,25-48,49-72,73-96,97-120,121-144,145-168,169-192,193-216,217-240,241-259` (`259` LF).
- `HQ-RUNBOOK.md`: consecutive 24-LF windows `1-24` through `481-504`, then `505-507` (`507` LF).
- `PUBLIC-AGENTS.md`: `1-22` (`22` LF).
- `PUBLIC-README.md`: `1-24,25-48,49-72,73-96,97-102` (`102` LF).
- `PUBLIC-COORDINATION.md`: `1-24,25-48,49-72,73-96,97-107` (`107` LF).
- `PUBLIC-FALLACY-v2.md`: `1-24,25-36` (`36` LF).
- `HQ-STATE.md`: consecutive 8-LF windows `1-8` through `209-216`, then `217-222` (`222` LF, separately charged).
- `candidate.md`: `1-24,25-42` (`42` LF).
- `ruling-control.md`: `1-24,25-48,49-72,73-84` (`84` LF).

Accordingly, the nine copied non-STATE governors were `1330` LF; candidate plus control were `126` LF; declared non-STATE bodies were exactly `1456` LF; the manifest added `163` LF, for actual non-STATE displayed coverage `1619` LF. STATE coverage was separately exactly `222` LF. Total displayed input body coverage was `1841` LF. There were no repeated, clipped, cropped, or unread ranges. Every body response contained one window, no non-STATE window exceeded 24 LF, and no STATE window exceeded 8 LF. Own-report body rereads were `0` LF; only targeted metadata/hash and mandated seal operations followed.

Primary-source bodies: `0`. Source searches/downloads: `0`. Repository/history queries: `0`. CAS/computation: `0`. Control-family exploration: `0` (only the mandated retained control was checked). Agents/jobs: `0`. Shared-document/source/input edits: `0`. Commits/pushes/auth/configuration/operational ticks/automatic-memory writes: `0`.

<!-- BODY-END -->

## Seal

- Body definition: every byte through the unique standalone `<!-- BODY-END -->` line,
  including its terminating newline; this seal is outside the body.
- Body bytes: `15641`.
- Body SHA-256:
  `b9839bb3bd09a3cea41f0e3a70c8e5fff2094e25b4966e5b18efd2c3ffd2db9b`.
- Frozen basis: `a0b799468cd065da71cbd13b8bb578438ca5e9f3`.
