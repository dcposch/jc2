#!/usr/bin/env python3
"""Create the bounded t=5, b4=1 slimgb fallback without altering its source."""

from pathlib import Path


root = Path(__file__).resolve().parent
source = root / "terminal_laurent_t5_b4_1_exact.sing"
target = root / "canonical_t5_b4_1_full10_slimgb_fallback.sing"
text = source.read_text()
needle = "ideal G=std(I);"
if text.count(needle) != 1:
    raise SystemExit(f"expected exactly one {needle!r}")
text = text.replace(
    '// source=terminal_laurent_t5.json t=5 b4=1',
    '// source=terminal_laurent_t5_b4_1_exact.sing; bounded slimgb fallback',
    1,
)
text = text.replace(needle, "ideal G=slimgb(I);", 1)
target.write_text(text)
print(target)
