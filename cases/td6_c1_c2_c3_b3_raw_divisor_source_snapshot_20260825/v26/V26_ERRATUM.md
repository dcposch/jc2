# V26 custody erratum to V25

V25's listed source closure passed and its producer bytes were pinned, but
the archive also inherited unlisted `__pycache__/*.pyc` files from a local
import smoke.  Those files are not licensed dependencies and make V25
unsuitable for immutable theorem custody even though direct execution uses
the pinned source producer.

V26 removes every bytecode/cache entry from the payload, changes only the
bundle/runner names, and retains the V25 source guard correction unchanged.
The recursive archive listing must contain no `__pycache__` directory or
`.pyc` file, and every remaining regular payload file is listed in
`SOURCE.sha256`.  V25 remains a diagnostic run only.
