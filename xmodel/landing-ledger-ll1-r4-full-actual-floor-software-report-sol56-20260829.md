# LL1-R4 typed full-actual-floor software report

**Date:** 2026-08-29  
**Producer:** Sol 5.6  
**Basis HEAD:** `76c746f698103d20019bfeb72654a361ccc5371d`  
**Packet:** `cases/landing_ledger_ll1_r4_20260829/`  
**Disposition:** `PROVISIONAL_SOFTWARE_AWAITING_DIFFERENT_MODEL_REVIEW`

## 1. Result

The new LL1-R4 packet is implemented and passes its compiler, independent
validator, manifest, mutation battery, and ordinary/optimized acceptance
tests. It preserves LL1-R3 and the legacy reprice checker byte-for-byte.

R4 explicitly separates the two price carriers:

```text
REPRESENTATIVE
  legacy selected-witness AF2 floor

FULL_ACTUAL_FIRST_SEPARATION = canonical FULL_ACTUAL_EXIT
  complete distinct actual cv carrier + lower floor only
  no attainment
```

Only actual nonzero up directions in this fixed-fibre two-pole consumer are
typed `FULL_ACTUAL_FIRST_SEPARATION`. Their floor is `delta` for positive
integral `delta` and `ceil(2*delta)` otherwise. Epsilon/zero and pure-epsilon
directions remain explicitly `REPRESENTATIVE` under the legacy rule. Every
emitted component carries its type, certificate, applied and representative
floor, `LOWER_FLOOR_ONLY` semantics, and `attainment=false`.

## 2. Exact replay delta

All 16 unique frozen-R3 dirty cells are re-derived. Exactly four change:

| cell | representative | R4 full | epsilon/zero |
|---|---:|---:|---:|
| `(17,5)@nu2` | 2 | 3 | 1 |
| `(51,15)@nu7` | 2 | 3 | 1 |
| `(85,25)@nu12` | 2 | 3 | 1 |
| `(119,35)@nu17` | 1 | 2 | 0 |

The remaining 12 cells do not move. The reduced-superset inventory is exactly
`13 -> 7`; six rows are removed and none added:

```text
(2/7,7,3,ALIVE)
(1/2,2,4,ALIVE_FRAGILE)
(1/2,4,4,ALIVE_FRAGILE)
(2/11,11,4,ALIVE_FRAGILE)
(2/13,13,4,ALIVE_FRAGILE)
(2/5,5,4,ALIVE_FRAGILE)
```

`ALIVE` remains a reduced-superset predicate, never existence.

## 3. Frozen canonical source custody

All seven canonical inputs matched before and after the build:

```text
b3993495eff1913b09f1fc6750b2af08ecf90a9f9f38c97f85be47ba9c9a54d0  ladder/BOOK-OFFAXIS.md
f11cbe1fcad375fdd722be979731f7c30f989889bfeb33232ab86e64deee1774  ladder/SHEET6-MULTIPOLE.md
c66ff941d3954143b51f4dc2ac0dd77d6e1d5be81c0d6cdca3e1bd2a058b9a64  ladder/SHEET6-2POLE.md
c63bd1673b2b180173799f5bee07f7fc0e51047945a41010a28a0aeeeeb92253  FALLACY.md
29270ff6192fcee2eecb4ba68578010b2b3f0c5519feb71dc67baa7f68bb784b  ladder/REDUCTION.md
ad9ced6c0420902f8cf63edf3636bed8633be511e925f208d24a24c35d71036d  ladder/SHEET6-DEPTH.md
841fa120fa2ae801578834c7b52c5aad600eb48df73b683e1db5c954caf7f7ac  ladder/SHEET6-DEPTH-REVIEW.md
```

The compiler verifies 49 exact consumed-clause anchors across these bytes.

## 4. Theorem/review/software provenance

Eight immutable evidence files are full-hash pinned; all six sealed reports
also have independently checked body-prefix seals:

```text
82d2f6c3eb2c3985569da428def3d5c2e125ca5b0aa29ebfc7973b68ee843a7a  Sol carrier theorem; body 21235 / 0c808734cf2f0c98d085503e8d0aaf8e0ca645c34adfb925c757d0beb6223428
f7853d39a17fd7329feaec101f1767ef5edddd07a2f0d5f8030a0cb023f95efe  Opus primary; body 61389 / 2fe6a14ca8a04033d176547704de20ccd7d1c7e5dd19599970dffab3a60cbe18
32402983a357ef25de363a9532a47fa9a2cb4b4e8e1bab918d6f6e07a3fb3a10  cross-comparison; body 9484 / 1026e3a240b93563a3f521acd07ab139f329a6658568f8dc2c83a4634c58ec22
1b3be27da8ba495d80cbf473d844055583a672d136ccea40611dfe9fc0b7023e  stable Grok review; body 32456 / 3be6ab6b8db8ba7c89c0f382f201a17b2bae6000720d2c04ef2de3925b90a47a
aaa7496bd6182bd124935b8534307ad3167fffe9393efad3e56cf349942ddeb7  legacy reprice producer; body 12149 / 2d873e680cfdc464fc0bc707aec5c072ba9310ee0600a98786643c0ca8c93ac5
3e3cea4aa6e0bda907dd291a0f1e62e1ffa744e84463e5596c2e0e0e408a166b  stable Opus reprice review; body 34525 / 7b23f8cadfc8e4afcbebd64add68449bd8e08f2cacfc6dede26d651dc681e302
205e7f5825604e0e334d1a822b13a595dfe6b9ce06d0f011b199a0ddcb725a1e  frozen LL1-R3 book
6ca098b8145f091884d7f11ab1d6aac49dadaab91a6ba7ed18f7c022efce99b5  frozen legacy reprice checker
```

## 5. Verification

Commands were run from repository root with `PYTHONDONTWRITEBYTECODE=1`:

```text
python3     cases/landing_ledger_ll1_r4_20260829/ll1_compiler.py
python3 -O  cases/landing_ledger_ll1_r4_20260829/ll1_compiler.py
  both rc=0; stdout SHA-256 f1a5f8756f1775f1df46fb776615c6fcd2ad023d498c8d91ebe8b5cdecdc7998

python3     cases/landing_ledger_ll1_r4_20260829/ll1_validator.py
python3 -O  cases/landing_ledger_ll1_r4_20260829/ll1_validator.py
  both rc=0; stdout SHA-256 5001bdea3c9ddd59c1d0bd61ec4f8c3548151f233ed4aee9fb181e3dfd716088

python3     cases/landing_ledger_ll1_r4_20260829/test_ll1_r4.py
python3 -O  cases/landing_ledger_ll1_r4_20260829/test_ll1_r4.py
  both rc=0; byte-identical stdout
  LL1-R4 acceptance   passed: 166   failed: 0
  ALL TESTS PASS (166 checks)
  stdout SHA-256 a078cdd81f4d735c283db3dcb528a84f90fb4ccd8fd3cd02b3af0d57b0c54eb9
```

The suite also runs the immutable legacy reprice checker in ordinary and
optimized modes; both produce stdout SHA-256
`4498beacf2f119d4f3d1b1750e857549e98f76900899983dd32db5d4e5da0011`.

## 6. Packet manifest

```text
314947ef2068b736d57119b2dca1f59b1a868781f30e0d673d4fb86b3f5416a0  ll1_compiler.py
09a731b7dea0b71442fda193f31a245a4e3210c143ef2193b6f3ad7c7d019dd5  ll1_validator.py
32cf3fddb828b0651b3c5ee1ab246c006d45450d0138b3165307631fd0dfd744  test_ll1_r4.py
25e3fd3c0300e53b041054dd06e0bddd60fc9e0dfc4153af07e276aac8a78c68  INVENTORY.md
7715083c811a3d9fd011aeed245c23ede31c56d9fbf055a571c11bfe08aaef04  out/ll1_book.json
29bc125bea86dc35d9d181d445b4927babb154ce88e9c9720efb60d0ee33c689  out/ll1_summary.json
```

`MANIFEST.sha256` hashes
`23e56710ad5ba6e2b8a0c9e8e2a4cb802f7ef545dadea22164f9aacdb185998a`
and verifies 6/6.

Immutable baseline recheck:

```text
LL1-R3 compiler / validator / test / inventory
839d3801... / 76cfec34... / 2cebe74b... / 5acc4b79...
LL1-R3 book / summary
205e7f58... / 7c7cfd3b...
legacy reprice checker
6ca098b8...
```

## 7. Limitations and disposition

This is desk-scale exact arithmetic only. It does not rerun the historical
26-shape/351-route engine, prove candidate-grammar completeness, source
landing, realization, attainment, a degree ceiling, `td != 6`, or JC2.
Generic MP8/MFE remains representative. No canonical file, R3 file, legacy
checker, commit, remote, AWS resource, or heavy CAS was changed.

The software packet is locally complete but remains
`PROVISIONAL_SOFTWARE_AWAITING_DIFFERENT_MODEL_REVIEW`. A reviewer should
attack carrier leakage into epsilon/pure-epsilon rows, the old/new graph
replay, exact four-cell exhaustiveness, evidence/source mutation closure,
and ordinary/`-O` behavior before promotion.

<!-- END-SEALED-BODY::landing-ledger-ll1-r4-full-actual-floor-software-report-sol56-20260829 -->

## Seal (outside the sealed body)

Convention: the sealed body is the byte range from the first file byte through
and including the newline terminating the unique `END-SEALED-BODY` marker
immediately above. This seal section is excluded.

```text
sealed-body bytes      6753
sealed-body SHA-256    f645432f935fd39515ae3c59f8c4835dac8181fe5b6eed051e2012a04438b43a
cut at 6752 bytes      ad01c681db638c889bd602c2b89dff70cb8d522a61bae85b24865dd6445f3d91
cut at 6754 bytes      a126013be309f339b15c63f49c53baa4765bdfa6d37c8db33e7d56bd87a97cb5
```
