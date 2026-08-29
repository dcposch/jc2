# LL1-R2 packet inventory — cases/landing_ledger_ll1_r2_20260829/

Corrected `td=6, m=2` LANDING-LEDGER LL-1 packet (repair of the sealed
Fable5 design at its `nu=1` discriminator, per the Grok 4.6 hostile
review).  Producer report:
`xmodel/landing-ledger-ll1-r2-repair-fable5-20260829.md`.

| file | role |
|---|---|
| `ll1_compiler.py` | Exact-rational compiler: T7 entry solve, DS3 closure, the corrected `nu=1` family-I normalization (`(l,eps_q=1) == I@L=l+1`), the reconstructed D9 log-obstruction with exact linear-algebra verification, IIa uniqueness theorem, ZCH/root laws, P0 priced-step enumerator (soundness first-principles, completeness cited to P0), P1/St 9.4 terminals, budget-exhaustion residue BFS with route-death fixpoint, synthetic UNCOVERED probe, deterministic JSON emission. |
| `ll1_validator.py` | Fail-closed validator: re-derives every record's arithmetic and the whole summary from record level; enforces token whitelists, CAP-tier prohibition on COVERED records, `M = gcd(dp,dq)` everywhere, `W-CLOSED-FORM` on the admitted merge child, UNCOVERED h/instance/consumers discipline, and the theorem-kill check on UNCOVERED rows; re-runs the residue enumeration and D9/terminal arithmetic.  No `assert` statements (identical under `python -O`). |
| `test_ll1_r2.py` | Acceptance tests A1–A5 + hostile mutation battery (122 checks; exact count printed).  Runs identically under `python -O`. |
| `out/ll1_book.json` | Deterministic compiled book (canonical JSON, sorted keys, no timestamps or absolute paths). |
| `out/ll1_summary.json` | Derived summary (recomputed, never hand-written); validator recomputes it independently. |
| `INVENTORY.md` | This file. |
| `MANIFEST.sha256` | SHA-256 of every packet file (excluding itself). |

Reproduction:

    cd cases/landing_ledger_ll1_r2_20260829
    python3 ll1_compiler.py      # emits out/*.json, prints hashes
    python3 ll1_validator.py     # exit 0 iff the book validates
    python3 test_ll1_r2.py       # 122 checks
    python3 -O test_ll1_r2.py    # identical under -O
    shasum -a 256 -c MANIFEST.sha256

Scope firewall: this packet tests the corrected LL-1 quotient and hand-run
at `td=6, m=2` only.  It is not a proof that the candidate grammar equals
all geometric configurations, does not bound depth, and proves no source
landing, ceiling, Keller, or JC2 statement.
