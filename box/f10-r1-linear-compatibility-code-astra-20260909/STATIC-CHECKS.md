# Documentary static checks — no execution

2026-09-09 22:11UTC: new compatibility.py, dispatch_batch.py, both JSON
plans, VALIDATION, READ-SCOPE and private report read WHOLE as text.
Five frozen copies cmp-identical. Harness/plan SHA literals in the new
caller equal current sha256sum output. caller.diff is literal diff -u;
its exit1 records changed text, not a failed runtime control.

Manual trace: twelve exercise calls (five positives, seven negatives);
two2x5 RREF loops;23 explicit fmpq constructions. All mathematics is
inside main after unchanged authorize and metadata/package checks.
Neither solver nor evidence.verified is invoked. Generic fixtures carry
no source acceptance. Precision positive reaches the unchanged checker;
the rounded-string and float controls reach different checks. These are
unexecuted code-path observations, not measured results.

Own raised-OPEN quantity and cheapest future test stated. No TODO/TBD/FIXME
or premature marker; own targets absent before begin. Input current pins,
transaction and final custody are documentary metadata only.
