"""Replay terminal reviewer's unchanged checker with its removed bundle relocated.

Only the hardcoded FROZEN path is replaced in memory; this trampoline is also
the --probe entry point. No authority, engine or production source is used.
"""
import ast
import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent/'d125-hybrid81-caller-repair-gate-sol56-20260907/gate_checks.py'
data = SOURCE.read_bytes()
if hashlib.sha256(data).hexdigest() != '6006db6bea500abc12182b33db07dd9e1ba6767f4f0bb6a8645ddb9c8799c816':
    raise RuntimeError('terminal reviewer checker drift')
text = data.decode()
old = "FROZEN = Path('/tmp/jc2-lane.q9z0fq/inputs')"
if text.count(old) != 1 or any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(text))):
    raise RuntimeError('path adaptation/AST drift')
text = text.replace(old, 'FROZEN = Path('+repr(str(HERE/'inputs'))+')', 1)
exec(compile(text, str(SOURCE), 'exec'), {'__name__': '__main__', '__file__': __file__})
