# Hostile review: msolve 0.10.1 char-0 `-g` `[1]` erratum

Reviewer: Grok 4.6 (adversarial verifier). Date: 2026-08-23.
Engine: box01 `msolve` 0.10.1 (`/usr/local/bin/msolve`; source `/home/ubuntu/msolve` @ `1e3af01`). Local msolve not used.
Target: uncommitted `AUDIT.md` superseding erratum (char-0 `-g` `[1]` = first machine prime; cCa2/cCa6 archives demoted; chartG untouched).

**VERDICT: CONFIRMED.** The erratum stands for the campaign's archived char-0 `[1]` outputs. msolve 0.10.1 `-g 2` on characteristic-0 input returns after the first modular F4 when that modular reduced GB is `{1}`, with no second prime, no CRT, no rational reconstruction, and no cofactor. The printer then hardcodes `#field characteristic: 0`. A proper Q-ideal can hit this path: the lucky-prime filter inspects input coefficients only, so a determinant/resultant unlucky prime is not skipped. The naive coefficient-planted trap (coordinator) is the one case the filter *does* catch; it does not refute the bug.

Scoped non-claim: `-g 2` on a *non-unit* first modular GB *does* enter the apply/CRT/ratrecon loop (dummy `[x-1,y-1]`; the same trap at a different seed). Help text / `CERT-UPGRADE.md` "always first prime" is true for `-g 1` (leading monomials) and for the unit-ideal `-g 2` short-circuit, and overstates the non-unit `-g 2` path. Campaign invocations are `-g 2`; the dangerous path is exactly `is_empty`.

Bug vs evidence-tier: this is an msolve soundness bug *and* a certificate-philosophy gap. Even a multi-prime `[1]` without a reconstructed `1 = Σ h_i f_i` is not a Q-membership certificate (`CERT-UPGRADE.md` bounds). Here the engine does not even reach a second prime.

---

## 1. Source

### (a) Prime filter: every input coefficient, nothing else

`src/neogb/modular.h:41-60` (`is_lucky_prime_ui`): a prime is "lucky" (excluded) iff it divides **any** coefficient of **any** generator in the current basis. Not leading-only, not content-only, not intermediate F4 coefficients, not GB denominators.

```c
for (i = 0; i < bl; ++i) {
  cf  = bs->cf_qq[bs->hm[i][COEFFS]];
  for (j = 0; j < bs->hm[i][LENGTH]; ++j) {
    if (mpz_divisible_ui_p(cf[j], prime) != 0) {
      return 1;
    }
  }
}
```

First prime, `-g` / `core_groebner_qq` (`src/msolve/lifting-gb.c:1312-1318`):

```c
prime = next_prime(rand() % (1303905301 - (1<<30) + 1) + (1<<30));
while(fc == 0 && is_lucky_prime_ui(prime, bs)){
  prime = next_prime(rand() % (1303905301 - (1<<30) + 1) + (1<<30));
}
primeinit = prime;
msd->lp->p[0] = primeinit;
```

`rand()` is `srand(time(0))` by default, or `srand(SEED)` with `--random-seed SEED` (`main.c:488-495`). Range is machine primes in `(2^30, 1303905301]`. `generate_lucky_primes` runs first and is then overwritten at `p[0]`.

The `-g` path (`print_msolve_gbtrace_qq` → `groebner_qq` → `core_groebner_qq`) does **not** call `remove_content_of_initial_basis` (that is the `msolve.c` parametrization path). Content of a generator is excluded only if it is one of the stored coefficients.

### (b) Unit-ideal handling: first-prime exit, no second prime, no cofactor

Learning-phase F4 at `lp->p[0]`. `is_empty` is set when the modular reduced GB has one element and that element has all exponents 0 (`lifting-gb.c:775-788`):

```c
int is_empty = 0;
if(bs->lml == 1){
    if(info_level){
        fprintf(VERBSTREAM, "Grobner basis has a single element\n");
    }
    is_empty = 1;
    for(int i = 0; i < bht->nv; i++){
        if(bexp_lm[i]!=0){
            is_empty = 0;
        }
    }
    if(is_empty){
        free_basis_without_hash_table(&(bs));
        return is_empty;
    }
}
```

Immediate return of that modular basis, **before** the apply/CRT loop (`lifting-gb.c:1363-1370`):

```c
if(is_empty == 1 || print_gb == 1 || (*modgbsp)->ld == 0){
  ...
  return modgbsp;
}
```

Three first-prime exits:

| condition | campaign relevance |
|---|---|
| `is_empty == 1` (modular GB = `{1}`) | **yes** (`-g 2`) |
| `print_gb == 1` (leading monomials only) | no (campaign is `-g 2`) |
| `(*modgbsp)->ld == 0` | empty export |

No second-prime check. No cofactor lift. `msolve --help` documents no membership-certificate flag (`CERT-UPGRADE.md` §1). If `is_empty == 0` and `print_gb == 2`, control continues to `New prime = ...` / `#primes` / CRT / ratrecon (verified below).

### (c) Char-0 header is hardcoded, not a record of the computation

`print_msolve_gbtrace_qq` (`lifting-gb.c:1852-1853`):

```c
fprintf(ofile, "#---\n");
fprintf(ofile, "#field characteristic: 0\n");
```

Always `0` on this path, including after the `is_empty` return. Help text (`main.c:104-105`): "Prints reduced Groebner bases of input system for first prime characteristic". The 8-line `#Reduced Groebner basis data` / `length of basis: 1 element` / `[1]:` surface is therefore compatible with a completed first-prime modular calculation and does not attest reconstruction over Q.

---

## 2. Experiment (box01)

`--random-seed 0` makes the first non-lucky prime deterministic: **1266886877**. Dummy `I = (x-1, y-1)` at that seed lifts (`#primes 3`, `#bad 0`, GB `[y-1, x-1]`), so the seed is usable as a known first prime for inputs whose coefficients it does not divide.

**Trap** (det = first prime; no input coefficient divisible by that prime):

```
x,y
0
633443439*x+633443438*y-1,
633443438*x+633443439*y
```

Let `p = 1266886877`, `a = (p-1)/2 = 633443438`. Matrix `[[a+1, a], [a, a+1]]` has det `(a+1)^2-a^2 = 2a+1 = p`. Over Q: unique point `x = (a+1)/p`, `y = -a/p`, ideal proper. `p ∤ a`, `p ∤ a+1`, `p ∤ 1`. Mod `p`: rows become linearly dependent and inconsistent ⇒ unit ideal.

| run | first prime | `#primes` / CRT | output | algebra |
|---|---|---|---|---|
| trap, seed 0 | **1266886877** (= det) | none. stderr: `Grobner basis has a single element`; no `New prime` | char-0 header + `[1]:` | **wrong** |
| trap, seed 42 | 1145617999 ≠ det | 5 primes, 0 bad | `[1266886877*y+633443438, 1266886877*x-633443439]` | **correct Q-GB** |
| trap, seed 12345 | 1226679379 ≠ det | 5 primes, 0 bad | same correct Q-GB | **correct** |
| trap, char `p` | (input char) | n/a | char-`p` header + `[1]:` | modular `[1]` is real |
| naive `p*x-1, y-1`, seed 0 | **1230182279** (p skipped) | 5 primes, 0 bad | `[y-1, 1266886877*x-1]` | correct; coefficient filter fired |
| true unit `1`, seed 0 | 1266886877 | none, same `single element` exit | char-0 `[1]:` | correct answer, first-prime path |
| dummy `-g 1`, seed 0 | 1266886877 | none (`print_gb==1` exit) | leading ideal `[y, x]` | LMs only, first prime |

Coordinator's planted-coefficient trap is reproduced (skip + lift). The hidden-det trap is the case that probe could not reach, and it **does** return a wrong char-0 `[1]`. Same binary, same input, only the first prime changed: seed 0 lies, seed 42 tells the truth and puts `p` in the denominators — which is exactly the unlucky prime the filter never saw.

glibc note: `srand(0)` and `srand(1)` generate the same sequence, so seed 1 is not an independent contrast.

---

## 3. Forensics (campaign archives)

`jc72108/run_probes.sh` and `ops/FLEET.md` invoke `msolve -g 2` **without** `-v`. Verbose lines (`Initial prime`, `New prime`, `#primes`, `#bad primes`, `Grobner basis has a single element`) are therefore not in the banked files.

| artifact | what is there | distinguisher |
|---|---|---|
| `runs/open_8_28_c2_cCa2.q.out` (307 B, 8 lines, 2026-07-30) | `#field characteristic: 0` + `length of basis: 1 element` + `[1]:` | **none.** Byte-identical surface to the false trap and to the true-unit probe |
| `runs/open_8_28_c2_chartG.q.out` | same 8-line surface | not load-bearing: `systems/open_8_28_c2_chartG.q.ms` generator 1 is the literal `-1` |
| `systems/open_8_28_c2_cCa2.q.ms` / `..._cCa6.q.ms` | char 0; first generator `-1+a1*b3`, **no** literal `-1` | — |
| `runs/cCa2_lift.txt` | empty | no cofactor |
| `runs/open_8_28_c2_cCa6.q.out` | **absent** locally and on box01 | fleet report only (`notes.md` 2026-08-01: 17h43m, 761 GB peak, "proper reduced-GB header") |
| `runs/open_8_28_c2_cCa6.p65521.out` | 0 bytes | no local modular archive |

17h43m / 761 GB on cCa6 is consistent with a **single** large modular F4 (the learning-phase call that sets `is_empty`). It is not evidence of CRT. The 8-line header is exactly what `print_msolve_gbtrace_qq` writes after that return. There is no archived `#primes` / reconstruction trace that would upgrade cCa2 or cCa6 to multi-prime, let alone to Q.

chartG remains an exact internal theorem by the literal generator, independent of msolve.

---

## 4. What this does and does not certify

- Archived char-0 `[1]` under `-g 2` certifies: *the reduced GB modulo the first selected machine prime was `{1}`*. It does not certify `1 ∈ I ⊂ Q[vars]`.
- That first prime is random in `(2^30, 1.30e9]` subject only to "divides no input coefficient". A hidden unlucky prime (denominator of the Q-GB, vanishing of an intermediate LC, inconsistent linear image, …) is in scope.
- Independently of the bug: `n` modular `[1]`s without a rational cofactor or a proved bound with `Σ log p_i > H1` are corroboration, not a Q-certificate (`CERT-UPGRADE.md` §3; the `(p1 p2 p3 x - 1)` example in the erratum). The cCa2/cCa6 banked primes sit far below that bound. The bug means the char-0 lane is not even a second independent modular sample: it *is* the first machine prime.

Campaign implication (agreeing with the uncommitted erratum): internal three-stratum char-0 proof of (72,108) subcase (2) is incomplete at cCa2/cCa6. chartG holds. External Helali/Suzuki exact artifacts in `archive/crosscheck.tgz` / `jc72108/CROSSCHECK.md` are a separate route and were not re-audited here.
