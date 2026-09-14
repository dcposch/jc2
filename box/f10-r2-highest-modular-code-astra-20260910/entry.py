"""Prospective metadata boundary only; bindings are not ROOT authentication."""
import os
import sys

TAG = 'f10-r2-highest-modular89-v1'
BASE_SHA = 'dac655a7ce75287b06010171bce66af1a644aff81de9620a452457a5f65a9587'
BASE_BYTES = 1652675
ARITH = {'produce': 'fe9ab1abe9a96fc43b889e1bcb598f8e8c65fd194732c48f3542e13c476e0345',
         'check': 'e5dd4bcb6114df2bdd79c8336583942c18d698d99fffd6f4b171e46a5d503d6e'}


class Inconclusive(ValueError):
    """A required sufficient-place or boundary condition did not hold."""


def need(ok, why):
    if not ok:
        raise ValueError(why)


def sufficient(ok, why):
    if not ok:
        raise Inconclusive(why)


def enter(mode):
    if sys.platform != 'linux':
        raise SystemExit('REFUSED: Linux EC2 only')
    try:
        with open('/sys/class/dmi/id/sys_vendor', 'r', encoding='ascii') as f:
            vendor = f.read(128).strip()
    except OSError:
        raise SystemExit('REFUSED: no EC2 DMI identity')
    if vendor != 'Amazon EC2':
        raise SystemExit('REFUSED: off AWS')
    flags = ('--registered-job', '--root-registration-sha256', '--self-sha256',
             '--entry-sha256', '--arithmetic', '--baseline', '--certificate', '--receipt')
    if len(sys.argv) != 17 or tuple(sys.argv[1::2]) != flags or sys.argv[2] != TAG:
        raise SystemExit('REFUSED: exact registered modular-highest vector required')
    ctx = dict(zip(flags, sys.argv[2::2]))
    for k in ('--root-registration-sha256', '--self-sha256', '--entry-sha256'):
        p = ctx[k]
        need(len(p) == 64 and all(c in '0123456789abcdef' for c in p)
             and p != '0' * 64, 'external pin required')
    import hashlib
    import stat
    import json

    def canonical(p):
        need(os.path.isabs(p) and os.path.realpath(p) == p and len(p) <= 512
             and all(c not in p for c in ('\n', '\r', '"')), 'canonical path required')
        return p

    paths = {k: canonical(ctx[k]) for k in
             ('--arithmetic', '--baseline', '--certificate', '--receipt')}
    me, entry = canonical(os.path.abspath(sys.argv[0])), canonical(os.path.abspath(__file__))
    need(len(set(paths.values()) | {me, entry}) == 6, 'distinct paths required')
    ctx.update(paths)
    sources = {me: ctx['--self-sha256'], entry: ctx['--entry-sha256'],
               paths['--arithmetic']: ARITH[mode]}

    def read(path, cap):
        fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW)
        with os.fdopen(fd, 'rb') as f:
            st = os.fstat(f.fileno())
            need(stat.S_ISREG(st.st_mode) and st.st_size <= cap, 'file bound/type')
            raw = f.read(cap + 1)
            en = os.fstat(f.fileno())
            need(len(raw) <= cap and (st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns, st.st_ctime_ns)
                 == (en.st_dev, en.st_ino, en.st_size, en.st_mtime_ns, en.st_ctime_ns), 'file drift')
            return raw

    def sha(raw):
        return hashlib.sha256(raw).hexdigest()

    def recheck():
        for path, pin in sources.items():
            need(sha(read(path, 1048576)) == pin, 'source pin mismatch')
        base = read(ctx['--baseline'], 15728640)
        need(len(base) == BASE_BYTES and sha(base) == BASE_SHA, 'baseline pin mismatch')
        return base

    raw = recheck()
    need(not os.path.lexists(ctx['--receipt']), 'receipt collision')
    if mode == 'produce':
        need(not os.path.lexists(ctx['--certificate']), 'certificate collision')
    need(hasattr(sys, 'set_int_max_str_digits'), 'integer guard unavailable')
    sys.set_int_max_str_digits(4300)

    def pairs(items):
        result = {}
        for k, v in items:
            need(k not in result, 'duplicate JSON key')
            result[k] = v
        return result

    def number(_):
        raise ValueError('JSON numeric coefficient forbidden')

    def load(raw):
        return json.loads(raw.decode('ascii'), object_pairs_hook=pairs,
                          parse_int=number, parse_float=number, parse_constant=number)

    def encode(obj):
        return (json.dumps(obj, sort_keys=True, separators=(',', ':'), ensure_ascii=True) + '\n').encode('ascii')

    def write(path, raw, cap):
        need(len(raw) <= cap, 'output byte cap')
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o600)
        with os.fdopen(fd, 'wb') as f:
            need(f.write(raw) == len(raw), 'short write')
            f.flush(); os.fchmod(f.fileno(), 0o444); os.fsync(f.fileno())
        fd = os.open(os.path.dirname(path), os.O_RDONLY | os.O_DIRECTORY)
        try:
            os.fsync(fd)
        finally:
            os.close(fd)
        need(read(path, cap) == raw, 'disk readback mismatch')

    ctx.update(read=read, sha=sha, load=load, encode=encode, write=write,
               recheck=recheck, sources=sources, raw=raw, mode=mode)
    return ctx


def arithmetic(ctx):
    import importlib.util
    name = '_modular_producer_arithmetic' if ctx['mode'] == 'produce' else '_modular_checker_arithmetic'
    spec = importlib.util.spec_from_file_location(name, ctx['--arithmetic'])
    need(spec is not None and spec.loader is not None, 'module loader')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def receipt(ctx, status, certificate_sha=None):
    ctx['recheck']()
    data = {'schema': 'f10-r2-highest-modular89-receipt/v1', 'status': status,
            'science_outcome': 'NONE', 'mode': ctx['mode'], 'prime': '89', 'root': '0',
            'root_registration_sha256': ctx['--root-registration-sha256'],
            'sources': ctx['sources'], 'baseline_sha256': BASE_SHA,
            'baseline_bytes': str(BASE_BYTES), 'certificate_sha256': certificate_sha}
    ctx['write'](ctx['--receipt'], ctx['encode'](data), 32768)
