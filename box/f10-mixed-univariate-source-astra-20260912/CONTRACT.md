# Prospective mixed univariate certificate contract

STATIC / UNEXECUTED / UNREVIEWED. Job `f10-mixed-univariate-bezout-20260912`.
No authority, host, installed library, measured performance or mathematical outcome is issued here.

## Mathematics and independent routes

Producer forms literal U,V,K,P0 from the charged ROOT note. P0=(t-2)P is an allowed scalar normalization: actual t=(5r+2)/(3r+1) lies in (5/3,12/7], so t-2 never vanishes. It forms B by the recurrence for phi^s and inverse-series recurrence for phi'/phi; all 64 pairs i,j=0..7 contribute with derivative coefficient 14-i-j. It then forms F by summing c*t^a*X^b*V^c*U^(7-c). B has ordinary (X,Y)-degree<=7, hence F degree<=21. It does NOT remove any parameter factor of B.

There is exactly ONE `Poly.gcdex` on Q(t)[X]. A nonconstant gcd ends INCONCLUSIVE, not a counterexample. A constant gcd is normalized to1. The LCM in Q[t] of EVERY coefficient denominator of both Bezout cofactors clears the identity into Q[t,X]. No parameter-polynomial denominator remains in A1,A2,N. The producer checks its own full identity, but this is not the independent certificate decision.

Checker imports neither producer nor its reconstruction helper. It owns new symbols and reconstructs phi powers by finite multinomial falling-factorial sums, and logarithmic derivative by differentiated finite log sums. It derives E=120(t-2)d6/c3 and its Y coefficients; the independently literal old D and Kold give U=D/4,V=-Kold/840. It reconstructs Sold=2Kold^2-140*tau*(1+tau-6X)*Kold*D+245*gamma*D^2, then P0=Sold/470400. It explicitly checks the linear d7 elimination, the old/new septic scaling and leading term. Its rational substitution U^7 B(t,X,V/U), followed by QQ[t,X] coercion, is distinct from the producer's termwise polynomial substitution. The two routes share trusted Sympy exact arithmetic, not code, symbols, matrices or producer results.

The accepted17zzd chart imports automatic Y*d5 guard and U-unitness on the entire septic algebra, including nilpotents; this code does not discover that theorem or discard components. It does not re-establish the earlier forcing attachment that the old mixed-scalar FIRST left absent.

## Exact wire and decision

Certificate is canonical ASCII JSON: sort_keys=True, separators comma/colon, ensure_ascii=True, exactly one final LF. Exact keyset is schema/job/status/sources/A1/A2/N. Status must be CANDIDATE_UNCHECKED, never PASS. Each polynomial is a list of [t-exponent,X-exponent,numerator/denominator] strings, strictly ascending numerical exponent pairs; no duplicates or explicit zero terms; zero polynomial is []. Reduced rational denominator is positive. No numeric JSON, floats, eval, sympify, executable includes, extra fields or trailing bytes are accepted. Bound:16MiB artifact,100000 terms per polynomial,t-degree16384, A1 X-degree20,A2 X-degree6,N X-degree0; numerator/denominator8192bits each. These are refusal ceilings, NOT observed or proved output sizes. Zero N is refused. Every received string is checked before construction from exact Python integers and Sympy Rational.

Full identity A1*P0+A2*F=N is checked in Q[t,X], including all positive X powers. N is then factored over Q[t] by the checker, not supplied as a trusted factor list. Recombination is checked. An irreducible nonlinear factor has no rational root; each linear root q gives the sole possible r=(2-q)/(3q-5). q=5/3 is unattained; every integer r>=2 makes the result INCONCLUSIVE. A factorization/library failure is STOP, never absence of exceptions. A scalar N with an actual-r zero need not mean B fails there: only this certificate is insufficient.

Producer exit0: artifact plus receipt CANDIDATE_UNCHECKED, stdout empty. Producer exit2: receipt INCONCLUSIVE_GENERIC_GCD, NO artifact, stdout empty. Checker exit0: two bounded receipts and exactly `MIXED_UNIT_ALL_INTEGER_R_CHECKED\n` stdout. Checker exit2: two receipts INCONCLUSIVE_ACTUAL_R_EXCEPTION, stdout empty. All exceptions exit1 with STOP stderr and no positive verdict; partial files remain forensic, not accepted results. Final output/receipt write failure precludes success. Checker receipts bind actual raw input SHA, not a reserialized surrogate. No other text is a verdict.

## Disabled CLI / no SHA cycles

Future commands use an actual ROOT-pinned interpreter with flags `-E -s -S -B`:

    PYTHON -E -s -S -B ABS/produce.py --job f10-mixed-univariate-bezout-20260912 --authority PRODUCE_AUTH --authority-sha256 AUTH_SHA --output CERT --receipt PRODUCE_RECEIPT
    PYTHON -E -s -S -B ABS/check.py --job f10-mixed-univariate-bezout-20260912 --authority CHECK_AUTH --authority-sha256 AUTH_SHA --output CHECK_RESULT --receipt CHECK_RECEIPT --input FROZEN_CERT

The registration argv is Python sys.argv (script through final argument), not interpreter flags. Exactly slot6 is the typed literal ROOT_AUTHORITY_SHA256; code substitutes the current authenticated authority digest there and nowhere else. Therefore no self-hash cycle. ROOT freezes separate producer/checker authorities; checker authority requires the future frozen certificate's exact SHA. There is no predicted candidate SHA. Three same-directory source files and resolved interpreter are the exact four source pins, also bound into the artifact. The schema is literal in authority.py and the template is deliberately disabled/null.

## External ROOT obligations / strict limits

Before any run: one different-model actual-code FIRST, ROOT registration, current EC2 physical/boot identity, native/library/ordinary-Python qualification, exact argv/environment, actual bounded process-tree/cgroup supervision and mandatory cleanup regression. Code checks Linux/unprivileged UID, DMI Amazon EC2/instance, boot/hostname, exact flags and sys.argv, offset-explicit UTC interval<=3600, three installed rlimits, source/interpreter/native-file hashes and a pinned external qualification document. That document is a ROOT trust assertion, NOT a code audit of its contents or loaded-unit behavior. Code does not prove the manifest closes all imports, aliases, installed pyc, directory inventories or loaded libraries. ROOT must establish those properties and guarantee no concurrent source/native/input/authority writer. Qualification/native manifests and source directories are outside writable outputs; immutable administration and readable ancestry are ROOT duties.

ROOT supplies1..4 fixed library directories appended after authorization because -S disables site setup. Their exact import precedence, stdlib closure, Sympy version/API and installed native backend must be qualified before science. Missing libraries fail closed; no install/retry/fallback. Scientific entrypoints call authorize before CAS import or construction; internal helpers are not separately authorized entrypoints.

Ceiling for ENTIRE separately registered batch:3600wall,3300CPU,32GiB,256MiB aggregate files; per-process rlimits do not establish whole-descendant accounting.16MiB is each candidate cap,32768 each receipt. ROOT must choose phase allocations within that unchanged joint ceiling and include preflight/controls/custody. Wall checks here are admission/end checks, not asynchronous kill mechanisms. External absolute+monotonic timers, closed child scope, native pre/post, output inventory and terminal durable custody are NOT implemented by this minimal package. No wrapper is supplied or authorized. Outputs use O_EXCL/O_NOFOLLOW/fsync/readback; fresh private parent and single writer are required, not inferred from apply_patch. ROOT freezes candidate before checker, retains all terminal bytes, and rejects any missing/abnormal receipt or cleanup failure.

All behavior is prospective. No -O/-OO test, native compatibility, output bound, runtime fit, scalar result, source exclusion, REG, all-F10 or JC2 claim.
