"""Registered AWS-only metadata inspection; no CAS/scientific source import."""
import os, sys
from pathlib import Path
if Path('/sys/class/dmi/id/board_asset_tag').read_text().strip() != 'i-0a59ae3233f3774a6':
    raise SystemExit('wrong registered worker')
import hashlib, json, stat
base = Path('/opt/jc2-mixed-20260912')
raw = (base/'prep/assembled/native-manifest.json').read_bytes()
if len(raw) > 1048576: raise SystemExit('manifest cap')
d = json.loads(raw)
paths = set(d['files']) | set(d['directories'])
for name in tuple(paths):
    paths.update(str(p) for p in Path(name).parents)
for name in sorted(paths):
    s = os.stat(name)
    if s.st_uid != 0 or s.st_mode & 0o022: raise SystemExit('unsafe ownership/mode: '+name)
    if any(a.startswith('system.posix_acl_') for a in os.listxattr(name)):
        raise SystemExit('ACL: '+name)
for name, h in d['files'].items():
    if hashlib.sha256(Path(name).read_bytes()).hexdigest() != h: raise SystemExit('native drift')
    prefix = str(base/'lib')+'/'
    if name.startswith(prefix):
        original = Path('/usr/lib/python3/dist-packages')/name[len(prefix):]
        if hashlib.sha256(original.read_bytes()).hexdigest() != h: raise SystemExit('package-copy mismatch')
for label, expected in [('science', ['authority.py','check.py','produce.py']),
                        ('runtime', ['dispatch.py','probe.py','run_capped.py']),
                        ('lib', ['mpmath','sympy'])]:
    if sorted(os.listdir(base/label)) != expected: raise SystemExit('directory census: '+label)
if sys.path != d['python_path']: raise SystemExit('base startup paths')
if os.path.lexists('/etc/ld.so.preload'): raise SystemExit('unexpected loader preload')
print(json.dumps({'status':'METADATA_PINS_PATHS_MODES_ACL_COPY_CHECKED_NOT_SCIENCE',
                  'files':len(d['files']),'directories':len(d['directories']),
                  'sys_path':sys.path,'python':sys.version,'flags':str(sys.flags)},sort_keys=True))
