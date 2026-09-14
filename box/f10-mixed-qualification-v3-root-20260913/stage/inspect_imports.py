"""AWS-only bounded import metadata; no source program or algebra operation."""
import sys
from pathlib import Path

if Path('/sys/class/dmi/id/sys_vendor').read_text().strip() != 'Amazon EC2':
    raise SystemExit('not EC2')
if Path('/sys/class/dmi/id/board_asset_tag').read_text().strip() != 'i-05ceda98fbb668717':
    raise SystemExit('wrong registered instance')
import hashlib, json

base = Path('/opt/jc2-mixed-20260912')
expected = [str(base/'meta'), '/usr/lib/python312.zip', '/usr/lib/python3.12',
            '/usr/lib/python3.12/lib-dynload']
if sys.path != expected:
    raise SystemExit('unexpected metadata-script startup paths')
if not (sys.flags.ignore_environment == 1 and sys.flags.no_user_site == 1
        and sys.flags.no_site == 1 and sys.flags.dont_write_bytecode == 1):
    raise SystemExit('startup flags')
with (base/'prep/assembled/native-manifest.json').open('rb') as stream:
    raw = stream.read(1048577)
if len(raw) > 1048576:
    raise SystemExit('native manifest cap')
files = json.loads(raw)['files']
sys.path.append(str(base/'lib'))
import sympy as sp
import mpmath
from sympy.external.gmpy import GROUND_TYPES

for module, label in ((sp, 'sympy'), (mpmath, 'mpmath')):
    if not Path(module.__file__).resolve().is_relative_to(base/'lib'/label):
        raise SystemExit('wrong private package location')
if GROUND_TYPES != 'python':
    raise SystemExit('unexpected optional arithmetic backend')
for name in ('symbols', 'Rational', 'Integer', 'Poly', 'expand', 'cancel'):
    if not callable(getattr(sp, name, None)):
        raise SystemExit('missing module API: '+name)
for name in ('terms', 'degree', 'gcdex', 'mul_ground', 'LC', 'all_coeffs',
             'as_expr', 'lcm', 'from_dict', 'nth', 'factor_list'):
    if not callable(getattr(sp.Poly, name, None)):
        raise SystemExit('missing Poly API: '+name)
if not hasattr(sp.Poly, 'is_zero') or not callable(getattr(sp.QQ, 'frac_field', None)):
    raise SystemExit('missing domain/property API')
loaded = {}
for name, module in sorted(sys.modules.items()):
    path = getattr(module, '__file__', None)
    if name == '__main__' or path is None:
        continue
    resolved = str(Path(path).resolve())
    if resolved not in files:
        raise SystemExit('loaded module absent from native files: '+resolved)
    with open(resolved, 'rb') as stream:
        data = stream.read(67108865)
    if len(data) > 67108864 or hashlib.sha256(data).hexdigest() != files[resolved]:
        raise SystemExit('loaded module byte mismatch: '+resolved)
    loaded[name] = resolved
print(json.dumps({'status': 'IMPORT_PATHS_APIS_PINS_CHECKED_NOT_ALGEBRA',
                  'sympy_version': sp.__version__, 'mpmath_version': mpmath.__version__,
                  'ground_types': GROUND_TYPES, 'startup_paths': expected,
                  'final_paths': sys.path, 'loaded_modules': loaded}, sort_keys=True))
