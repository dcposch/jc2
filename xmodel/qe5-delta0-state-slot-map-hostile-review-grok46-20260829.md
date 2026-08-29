# Q+E5 delta-zero state-slot map: custody-invalid Grok diagnostic

Date: 2026-08-29. Requested reviewer: Grok 4.6 through the campaign Grok
adapter. Target:
`xmodel/qe5-delta0-state-slot-map-r1-sol56-20260829.md`.

## Verdict

**INPUT_MUTATED / NO_PROMOTION.** This launch is not a hostile-review
certificate and supplies no lifecycle upgrade for the target. A declared local
source, `ladder/REDUCTION.md`, changed while Grok was reading it. Independently,
the injected `FALLACY.md` prompt dependency changed during the lane, so the
runner itself quarantined the result. The coordinator terminated the call before
the atomic checkpoint; Grok emitted no report. This document is a post-run
custody diagnostic assembled from the frozen run/log evidence and a bounded
desk replay. It must not be cited as a different-model pass.

## 1. Invocation evidence

- Tag: `qe5-delta0-state-slot-map-hostile-review-grok46-20260829`.
- Adapter: `ops/adapters/grok.sh`; CLI disclosure in the log is
  `grok 1.0.13 (5e9a58528b76) [stable]`, permission mode
  `bypassPermissions`. The packet requested Grok 4.6; because the call did not
  finish, there is no completed model self-disclosure beyond the configured
  adapter assignment.
- Basis recorded at launch: `eaad172e59742ef8cfd055eace9bc6d3b2da8463`.
- Start/end: `2026-08-29T09:30:30Z` / `2026-08-29T09:42:37Z`.
- Exit: signal `INT`, code `130`, `final_status=CANCELLED`, adapter report
  `MISSING`.
- Prompt SHA-256:
  `d43fa05876c5ae009fd775b6b80cf1b9654189512e6a15104d6a4c67c04ece5a`.
  Composed model-prompt SHA-256:
  `52dcc233d80a545f628fdb4163f967aa3d3fd77a4585416210bd46da62790573`.
- Adapter SHA-256:
  `b5db8bdb42546ae1cd2377c60573e051b298542a168d41faba44fdcae3775027`.
- Run/log SHA-256 after termination:
  `d21dc1061845898d63780b7f0044e36221a1248518ed0aa38fae6288ffec4fa2` /
  `a47ac046f98d84bb5339fc61f55bf1cc1f5fa492a4fec73c4ae9502f316ecff2`.

The run record pins the initial appendix hash as
`c89be697b35c8fcfa8d4f88289d71fc6fc889676182613d014bdf52da9a81824`
and the post-run hash as
`36eafbf4915cec4db685118acb6710d17bab44500e0ae5e75a08501257a07701`.
Its log therefore ends with `hashed lane input changed during execution;
result is quarantined`.

## 2. Source-custody failure

The target itself is SHA-256
`bccf157880bf868d6c204f300a62a2e96a2ee5ce4d1d2be94789079110155cb8`.
Its claimed body seal independently recomputes exactly: `18948` bytes and
`b27e7436eab58c75fbf5949626214c50942ff9ec6316b65a6069e765e7cecd91`.

The target records `ladder/REDUCTION.md` as
`b0b6c276b1fe28a9b94556e29a058264201267dfc496b3100c416f027bc7aa0f`.
A desk read during this launch obtained
`5e777d9b2a64dd22ec9565594a26cdb6f506230515ae49588f85f055e55613ab`;
a later double read obtained
`6bea12ccd5c710d9ddd1c694ad7b65632ccedf75af0d93013486388fdb4f2c39`.
Grok independently logged that the file differed from the producer table and
then differed across two of its own reads. This is an observed input race, not
a hash typo that may be silently repaired.

At the bounded desk sample, the other cited load-bearing files matched the
producer table exactly: `BOOK-OFFAXIS` `7679db8a...`, `SHEET6-DEPTH`
`ad9ced6c...`, `SHEET6-III` `59a2fa48...`, `SHEET6-MULTIPOLE`
`93adb7ac...`, `sol-h5a` `dd09069b...`, `grok-h5a-review` `3b8bd5c9...`,
the Fable R3 producer `885e5cc2...`, the Opus R3 review `9660ffe9...`,
`TOWER-UNIFORM` `d996f57b...`, and `cases/book_offaxis.py` `c22e3a1f...`.
That does not cure the declared-source mutation.

## 3. Non-promotional desk findings

These observations are retained only to make the fresh rerun cheaper.

1. Fixed positive `M_G`, forced `nu_G`, and a menu value `K=kbar_G`,
   together with the equal-state data, give
   `X=mu*(K-w)`. Reducing `X/K=a/b` and imposing
   `M_G=gcd(dp,dq)` uniquely gives `(dp,dq)=(M_G*a,M_G*b)`. The two degree
   congruences then uniquely give `s` and `Sm`. They do **not** uniquely give
   `(k,lex,mults)`; the target correctly presents those only as a canonical
   witness or a finite list.
2. The displayed cap replay is algebraically coherent at the stated pattern
   tier: `D=nu_G*(mu*s-Sm)`, strict NE gives `mu*s-Sm >= s >= 1`, and
   `gcd(M_G,nu_G)=1` with `M_G|D` and `nu_G|D` gives
   `M_G*nu_G|D`. Hence
   `dq/D <= 2+1/(M_G*nu_G)` and
   `K <= mu*w*(2+1/(M_G*nu_G))`.
3. For `Sm>0`, strict NE is exactly
   `1 <= m_j <= floor((dp-1)/dq)=mmax`. A positive bounded partition with
   at most `s` parts exists exactly when `ceil(Sm/mmax)<=s`; the `Sm=0`
   branch has `k=0, lex=s`. No defect was found in this gate during the desk
   replay.
4. `cases/book_offaxis.py:219-265` reconstructs `(dp,dq)` from `M_G` but
   loops over `nu=1` and every divisor index of `dq-1`; it has no fixed
   `nu_G` input and no `gcd(kbar,nu)` check. For the target's leakage fixture
   `(K,X,dp,dq)=(7,11,11,7)`, `nu=1,2,6` fail and `nu=3` passes, while forced
   `nu_G=2` fails divisibility. The diagnosis is correct.
5. The R3 migration sketch at
   `xmodel/m2-caseiii-two-pole-e5-local-index-r3-repair-fable5-20260829.md:369-409`
   destructures `zero` without `M_U` at line 376 and uses `M_U` at line 389.
   This is a genuine unbound pseudocode slot, not a defect in Theorems A--D.
   A typed zero-arrival state carrying `M_U` is the smallest repair.

These checks do not constitute the requested independent review because Grok
did not finish on a stable source basis. They also do not test ODE, edge,
i-sync, source, polynomial, route, or Keller realization.

## 4. Required next action

After the coordinator's atomic checkpoint, launch a fresh Grok 4.6 review from
one pinned basis, record hashes of every declared source both before and after
the call, and require equality before considering its verdict. Do not reuse
this tag, run record, or diagnostic as promotion evidence. If the fresh review
agrees with the desk algebra, it should still decide independently whether the
target's Section 3.1 heading should say “route-facing fail-closed envelope”
rather than literally “minimal input”; that wording issue has no theorem
consequence.

*End of diagnostic body.*

## Seal

- Body definition: all bytes before the literal `## Seal` heading.
- Body byte count: `6078`.
- Body SHA-256: `d03ddad0d02a06c2df0bba7994a0658df1ddf49b43636a1df81ef4e827cdbbf1`.
