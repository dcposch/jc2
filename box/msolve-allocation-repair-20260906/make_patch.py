#!/usr/bin/env python3
"""Generate an incremental patch from the immutable twice-patched source."""
from pathlib import Path
import difflib
import hashlib
import json

root = Path(__file__).resolve().parent
baseline = root.parent / 'full-j-solver-pilot-20260906/evidence/msolve-source'
parts = []
for rel in ('src/msolve/iofiles.c', 'src/msolve/checked-input-size.h', 'src/neogb/io.c'):
    old = baseline / rel
    new = root / 'edited' / rel
    parts.extend(difflib.unified_diff(old.read_text().splitlines(True) if old.exists() else [],
        new.read_text().splitlines(True), fromfile='a/'+rel if old.exists() else '/dev/null',
        tofile='b/'+rel))
patch = root / 'msolve-0.10.1-checked-input-allocation-v2.patch'
with patch.open('x') as f:
    f.writelines(parts)
files = [patch, root/'msolve-0.10.1-heap-sort-permutation.patch',
         root/'msolve-0.10.1-int64-input-offset.patch']
record = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
record['edited_source'] = {str(p.relative_to(root/'edited')): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in (root/'edited/src').rglob('*') if p.is_file()}
with (root/'source-inputs-v2.json').open('x') as f:
    json.dump(record, f, indent=2, sort_keys=True)
    f.write('\n')
print(json.dumps(record, sort_keys=True))
