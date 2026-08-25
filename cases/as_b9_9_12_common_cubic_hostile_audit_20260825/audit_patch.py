#!/usr/bin/env python3
"""Create an audit-only corrected copy of the B9 common-cubic emitter."""

from pathlib import Path


source = Path("emit_common_cubic.py")
target = Path("emit_common_cubic_fixed_audit.py")
text = source.read_text()
old = '''def bv(value):
    return f"(_ bv{value % MODULUS} {WIDTH})"


def ext8(name):
'''
new = '''def bv(value):
    return f"(_ bv{value % MODULUS} {WIDTH})"


def modulus_bv():
    return f"(_ bv{MODULUS} {WIDTH})"


def ext8(name):
'''
assert text.count(old) == 1
text = text.replace(old, new)
text = text.replace('return f"(bvurem {term} {bv(MODULUS)})"',
                    'return f"(bvurem {term} {modulus_bv()})"')
text = text.replace('f"(assert (bvult h{index} {bv(MODULUS)}))\\n"',
                    'f"(assert (bvult h{index} {modulus_bv()}))\\n"')
assert text.count("bv(MODULUS)") == 0
target.write_text(text)
print(target)
